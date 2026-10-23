"""Analysis tables from the drafted estimates and the completion pass (deviations.md, D7).

Inputs: extraction/study_map.csv, extraction/ft_estimates.csv (numbers from the full-text proposals, checked against the
texts) and extraction/draft/<name>.jsonl (complete.py: tasks, estimate codes, added estimates, human-human agreement,
study fields and risk of bias). Writes:
  forms/studies.csv           one row per study: reports, publication fields, configuration reporting, risk of bias
  forms/tasks.csv             one row per study x task: task type and moderators (codebook study fields, per task)
  forms/estimates.csv         one row per included LLM-human value (drafted numbers coded by the pass + added ones)
  forms/human_reliability.csv one row per human-human value
Every number is checked against the source texts by script (value_in_text, quote_in_text), as in estimates_from_ft.py.
Run: .venv/Scripts/python.exe -I papers/llm-coder-agreement-meta/extraction/finalize.py --name complete_2026-10-23
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
FORMS = PAPER / "forms"
import sys  # noqa: E402
sys.path.insert(0, str(HERE))
from estimates_from_ft import norm, parse_value, text_of  # noqa: E402
from r1_corrections import apply, clean  # noqa: E402
from models import annotate  # noqa: E402


def check(value: str, quote: str, texts: list[str]) -> tuple[bool, bool]:
    v = norm(value).rstrip("%")
    num, _ = parse_value(value)
    parts = [norm(x) for x in re.split(r"\s*(?:\.\.\.|…|\|)\s*", quote or "") if len(x.strip()) >= 4]
    vin = bool(v) and any(v in t or bool(num and num in t) for t in texts)
    qin = bool(parts) and any(all(x in t for x in parts) for t in texts)
    return vin, qin


CHECKS = Path(__file__).resolve().parent / "text_checks.json"   # value and quote checks against the full texts,
HAVE_TEXTS = (Path(__file__).resolve().parents[1] / "fulltext" / "text").is_dir()   # reused where the texts are absent
_cache: dict[str, list[bool]] = {} if HAVE_TEXTS else json.loads(CHECKS.read_text(encoding="utf-8"))


def checked(value: str, quote: str, texts: list[str] | None, sid: str) -> tuple[bool, bool]:
    key = f"{sid}|{value}|{quote}"
    if texts is not None:
        _cache[key] = list(check(value, quote, texts))
    return tuple(_cache[key])


def write(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    cols = list(dict.fromkeys(k for r in rows for k in r))
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True, nargs="+", help="draft/<name>.jsonl runs of complete.py")
    a = ap.parse_args()
    sm = list(csv.DictReader((HERE / "study_map.csv").open(encoding="utf-8")))
    reports = defaultdict(list)
    for r in sm:
        reports[r["study_id"]].append(r)
    ft = {r["ft_estimate_id"]: r for r in csv.DictReader((HERE / "ft_estimates.csv").open(encoding="utf-8"))}
    drafts = {}
    for name in a.name:
        for line in (HERE / "draft" / f"{name}.jsonl").open(encoding="utf-8"):
            if line.strip():
                d = json.loads(line)
                drafts.setdefault(d["conv_id"], d["codes"])

    studies, tasks, estimates, human = [], [], [], []
    missing = []
    for sid, reps in sorted(reports.items()):
        d = drafts.get(sid)
        if d is None:
            missing.append(sid)
            continue
        main = next(r for r in reps if r["role"] == "main")
        sent = [r["rec_id"] for r in reps if r["role"] in ("main", "attached")]
        texts = [text_of(k) for k in sent] if HAVE_TEXTS else None
        st = d["study"]
        studies.append({
            "study_id": sid, "report_ids": ";".join(r["rec_id"] for r in reps), "main_report": main["rec_id"],
            "first_author": main["first_author"], "year": main["year"], "doi": main["doi"], "title": main["title"],
            "scope": main["scope"], "own_study": "yes" if "R3861" in sent else "no",
            **{k: st[k] for k in ("pub_status", "field", "all_configs_reported", "tuned_on_eval")},
            **{f"rob_{i}": st[f"rob_{i}"]["rating"] for i in range(1, 6)},
            **{f"rob_{i}_reason": st[f"rob_{i}"]["reason"] for i in range(1, 6)},
            "possible_overlap": main["possible_overlap"], "note": d["note"]})
        task_type = {}
        for t in d["tasks"]:
            task_type[t["task_id"]] = t["task_type"]
            tasks.append({"study_id": sid, **t})
        for c in d["estimate_codes"]:
            f = ft.get(c["ft_id"])
            if f is None or f["study_id"] != sid:
                continue
            estimates.append({
                "study_id": sid, "task_id": c["task"], "task_type": task_type.get(c["task"], ""), "source": "ft",
                "ft_estimate_id": c["ft_id"], "rec_id": f["rec_id"], "include": c["include"],
                "exclude_reason": c["exclude_reason"], "model_name": c["model_name"], "configuration": f["configuration"],
                "prompting": c["prompting"], "n_examples": c["n_examples"], "reference": c["reference"],
                "statistic": c["statistic_code"], "icc_form": c["icc_form"], "value_raw": f["value_raw"],
                "value": f["value"], "parse": f["parse"], "n_units": c["n_units"] or f["n_units"],
                "authors_primary": c["authors_primary"], "prevalence": c["prevalence"], "mean_llm": c["mean_llm"],
                "mean_human": c["mean_human"], "location": f["location"], "quote": f["quote"],
                "value_in_text": f["value_in_text"], "quote_in_text": f["quote_in_text"]})
        for x in d["added_estimates"]:
            num, how = parse_value(x["value"])
            vin, qin = checked(x["value"], x["quote"], texts, sid)
            estimates.append({
                "study_id": sid, "task_id": x["task"], "task_type": task_type.get(x["task"], ""), "source": "added",
                "ft_estimate_id": "", "rec_id": main["rec_id"], "include": "yes", "exclude_reason": "NA",
                "model_name": x["model_name"], "configuration": x["configuration"], "prompting": x["prompting"],
                "n_examples": "NR", "reference": x["reference"], "statistic": x["statistic_code"],
                "icc_form": x["icc_form"], "value_raw": x["value"], "value": num, "parse": how, "n_units": x["n_units"],
                "authors_primary": x["authors_primary"], "prevalence": "NR", "mean_llm": "NA", "mean_human": "NA",
                "location": x["loc"], "quote": x["quote"], "value_in_text": vin, "quote_in_text": qin})
        for h in d["human_reliability"]:
            num, how = parse_value(h["value"])
            vin, qin = checked(h["value"], h["quote"], texts, sid)
            human.append({"study_id": sid, "task_id": h["task"], "same_units": h["same_units"],
                          "comparison": h["comparison"], "statistic": h["statistic_code"], "value_raw": h["value"],
                          "value": num, "parse": how, "n_units": h["n_units"], "location": h["loc"], "quote": h["quote"],
                          "value_in_text": vin, "quote_in_text": qin})
    estimates = [{"estimate_id": f"E{i:04d}", **e} for i, e in enumerate(estimates, 1)]
    human = [{"hr_id": f"H{i:03d}", **h} for i, h in enumerate(human, 1)]
    # R1's review and value cleaning (r1_corrections.py, D8)
    estimates, unused = apply(studies, tasks, estimates)
    if unused:
        print("corrections that matched nothing:", unused)
    no_rule = annotate(estimates)
    print(f"model names without a rule: {len(no_rule)}")
    texts_of = {}
    for e in estimates:
        if e.get("source") == "r1_review" or "." in e["estimate_id"]:
            k = next(r["rec_id"] for r in reports[e["study_id"]] if r["role"] == "main")
            if HAVE_TEXTS:
                texts_of.setdefault(k, [text_of(k)])
            e["value_in_text"], e["quote_in_text"] = checked(e["value_raw"], e["quote"], texts_of.get(k), e["study_id"])
    excl_s = {s["study_id"] for s in studies if s["excluded_r1"]}
    excl_t = {(t["study_id"], t["task_id"]) for t in tasks if t["excluded_r1"]}
    for h in human:
        c = clean(h["value_raw"], h["statistic"])
        h.update({"value": c["value"], "ci_low": c["ci_low"], "ci_high": c["ci_high"], "value_note": c["value_note"],
                  "pool": "no" if (c["pool"] == "no" or h["study_id"] in excl_s
                                   or (h["study_id"], h["task_id"]) in excl_t) else "yes"})
    if HAVE_TEXTS:
        CHECKS.write_text(json.dumps(dict(sorted(_cache.items())), ensure_ascii=False, indent=0) + "\n",
                          encoding="utf-8", newline="\n")
    write(FORMS / "studies.csv", studies)
    write(FORMS / "tasks.csv", tasks)
    write(FORMS / "estimates.csv", estimates)
    write(FORMS / "human_reliability.csv", human)

    inc = [e for e in estimates if e["include"] == "yes" and e["pool"] == "yes"]
    kfam = {"cohen_kappa", "fleiss_kappa", "weighted_kappa_linear", "weighted_kappa_quadratic", "weighted_kappa",
            "krippendorff_alpha", "gwet_ac1", "pabak"}
    corr = {"icc", "pearson", "spearman", "kendall", "ccc"}
    summary = {
        "studies_coded": len(studies), "studies_missing": missing, "tasks": len(tasks),
        "task_types": dict(Counter(t["task_type"] for t in tasks)),
        "estimates_listed": len(estimates), "estimates_included": len(inc),
        "estimates_added": sum(e["source"] == "added" for e in estimates),
        "excluded_reasons": dict(Counter(e["exclude_reason"] for e in estimates if e["include"] == "no").most_common(10)),
        "studies_with_kappa_family": len({e["study_id"] for e in inc if e["statistic"] in kfam}),
        "studies_with_icc_or_correlation": len({e["study_id"] for e in inc if e["statistic"] in corr}),
        "studies_with_descriptive_only": len({e["study_id"] for e in inc} - {e["study_id"] for e in inc
                                                                            if e["statistic"] in kfam | corr}),
        "statistics_included": dict(Counter(e["statistic"] for e in inc).most_common()),
        "value_in_text_included": f"{sum(str(e['value_in_text']) == 'True' for e in inc)} of {len(inc)}",
        "studies_excluded_r1": [s["study_id"] for s in studies if s["excluded_r1"]],
        "outcomes": dict(Counter(e["outcome"] for e in inc)),
        "human_reliability_values": len(human), "studies_with_human_reliability": len({h["study_id"] for h in human}),
        "rob": {f"rob_{i}": dict(Counter(s[f"rob_{i}"] for s in studies)) for i in range(1, 6)},
    }
    (HERE / "finalize_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
                                                encoding="utf-8", newline="\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
