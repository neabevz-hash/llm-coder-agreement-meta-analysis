"""AI completion pass (deviations.md, D7): tasks, moderators, estimate codes, human-human agreement and risk of bias.

For every study (jobs.json) the runner sends the study's text (reference list cut) and the estimates drafted from the
full-text proposals (ft_estimates.csv, IDs F....); the model codes them with the fixed prompt in complete_prompt.md.
Studies whose full-text proposal listed no statistics or hit the limit of 20 are marked incomplete, and the model adds
the missing overall estimates. Appends one JSON line per job to extraction/draft/<name>.jsonl (resumable).
Default model: Claude Sonnet 5.5, effort medium.

Before a full run: state the number of calls and the expected share of a Claude Max window to R1, and check that no
runner is left over (python.exe with llm_screen, ft_screen, extract or complete in the command line; claude.exe -p).

Run (check): .venv/Scripts/python.exe papers/llm-coder-agreement-meta/extraction/complete.py --run 2026-10-21 --name check_<date> --only ST...
Run (all):   .venv/Scripts/python.exe papers/llm-coder-agreement-meta/extraction/complete.py --run 2026-10-21 --name complete_<date>
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from extract import MAX_CHARS, MODELS, Judge, judge_all, load_records, report_text  # noqa: E402
from estimates_from_ft import proposals  # noqa: E402

SEED = 20261027


def blocks(md: str) -> list[tuple[str, str]]:
    return re.findall(r"```(\w*)\n(.*?)```", md, re.S)


def s_(n: int) -> dict:
    return {"type": "string", "maxLength": n}


def e_(values: list[str]) -> dict:
    return {"type": "string", "enum": values}


def obj(props: dict) -> dict:
    return {"type": "object", "properties": props, "required": list(props), "additionalProperties": False}


def arr(item: dict, n: int) -> dict:
    return {"type": "array", "maxItems": n, "items": item}


def build_schema(spec: dict) -> dict:
    stats = e_(spec["statistics"])
    task = obj({**{k: s_(200) for k in spec["task_text"]}, **{k: e_(v) for k, v in spec["task_enums"].items()}})
    code = obj({"ft_id": s_(8), "include": e_(["yes", "no"]), "exclude_reason": s_(120), "task": s_(4),
                "statistic_code": stats, "icc_form": s_(30), "model_name": s_(120), "prompting": s_(120),
                "n_examples": s_(20), "reference": e_(spec["task_enums"]["reference_type"]), "n_units": s_(40),
                "authors_primary": e_(["yes", "no"]), "prevalence": s_(40), "mean_llm": s_(30), "mean_human": s_(30)})
    added = obj({"task": s_(4), "model_name": s_(120), "configuration": s_(160), "prompting": s_(120),
                 "statistic_code": stats, "icc_form": s_(30), "value": s_(60), "n_units": s_(40),
                 "reference": e_(spec["task_enums"]["reference_type"]), "authors_primary": e_(["yes", "no"]),
                 "loc": s_(120), "quote": s_(300)})
    human = obj({"task": s_(4), "same_units": e_(spec["same_units"]), "comparison": e_(spec["comparisons"]),
                 "statistic_code": stats, "value": s_(60), "n_units": s_(40), "loc": s_(120), "quote": s_(300)})
    rob_item = obj({"rating": e_(spec["rob_ratings"]), "reason": s_(200)})
    study = obj({**{k: e_(v) for k, v in spec["study_enums"].items()},
                 **{f"rob_{i}": rob_item for i in range(1, 6)}})
    return obj({"tasks": {"type": "array", "minItems": 1, "maxItems": 30, "items": task},
                "estimate_codes": arr(code, 120), "added_estimates": arr(added, 80),
                "human_reliability": arr(human, 40), "study": study, "note": s_(800)})


def load_prompt() -> tuple[str, str, str, dict]:
    md = (HERE / "complete_prompt.md").read_text(encoding="utf-8")
    b = blocks(md)
    system = next(body for lang, body in b if lang == "" and body.startswith("You are coding"))
    preamble = next(body for lang, body in b if lang == "" and body.startswith("CODING FORM"))
    job_tpl = next(body for lang, body in b if lang == "" and body.startswith("JOB {job_id}"))
    spec = json.loads(next(body for lang, body in b if lang == "json"))
    return system.strip(), preamble, job_tpl, build_schema(spec)


def build_items(run: str, only: list[str] | None) -> list[dict]:
    _, preamble, job_tpl, _ = load_prompt()
    recs = load_records(run)
    n_props = {k: len(p["agreement_stats"]) for k, p in proposals().items()}
    listed = defaultdict(list)
    for r in csv.DictReader((HERE / "ft_estimates.csv").open(encoding="utf-8")):
        listed[r["study_id"]].append(r)
    items = []
    for j in json.loads((HERE / "jobs.json").read_text(encoding="utf-8")):
        if only and j["job_id"] not in only:
            continue
        sid = j["study_id"]
        reports = [j["main"], *j["attached"]]
        rows = [] if j["scope"].startswith("Chapter 4 only") else listed[sid]
        incomplete = (not rows) or any(n_props.get(k, 0) >= 20 for k in reports)
        lines = "\n".join(f"{r['ft_estimate_id']} | report {r['rec_id']} | {r['model']} | {r['configuration']} | "
                          f"{r['statistic']} = {r['value_raw']} | n {r['n_units']} | {r['location']}" for r in rows)
        links = []
        if j["link_reason"]:
            links.append(f"Linked reports: {j['link_reason']}")
        if j["attached"]:
            links.append(f"Attached below: {', '.join(j['attached'])}")
        if j.get("job_notes"):
            links.append(f"Note: {j['job_notes']}")
        main_rec = recs[j["main"]]
        main_text = report_text(j["main"])
        att = []
        for e in j["attached"]:
            u, t = recs[e], report_text(e)
            att.append(f"\nATTACHED REPORT {e}\nTitle: {u['title']}\nYear: {u.get('year')}; venue: {u.get('venue')}\n"
                       f"Full text ({len(t):,} characters; reference list removed):\n{t[:MAX_CHARS]}")
        body = job_tpl.format(
            job_id=j["job_id"], study_id=sid, scope=j["scope"], links="\n".join(links), n_listed=len(rows),
            incomplete=("; INCOMPLETE: the proposal listed no statistics or at most 20 of them, so add the missing "
                        "overall estimates under ADDED ESTIMATES") if incomplete else "",
            listed=lines or "(none)", main_id=j["main"], main_title=main_rec["title"], main_year=main_rec.get("year"),
            main_venue=main_rec.get("venue"), main_doi=main_rec.get("doi") or "none", main_chars=f"{len(main_text):,}",
            main_truncated=f"; cut to the first {MAX_CHARS:,} characters" if len(main_text) > MAX_CHARS else "",
            main_text=main_text[:MAX_CHARS], attached="\n".join(att))
        items.append({"conv_id": j["job_id"], "prompt": preamble + "\n" + body, "incomplete": incomplete})
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--only", nargs="*", help="study ids")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--model", choices=list(MODELS), default="sonnet")
    ap.add_argument("--effort", default="medium")
    a = ap.parse_args()
    system, _, _, schema = load_prompt()
    items = build_items(a.run, a.only)
    judge = Judge(system_prompt=system, schema=schema, model=MODELS[a.model], effort=a.effort, timeout=1800,
                  extra_env={"CLAUDE_CODE_MAX_OUTPUT_TOKENS": "32000"})
    out = HERE / "draft" / f"{a.name}.jsonl"
    asyncio.run(judge_all(items, lambda it: it["prompt"], judge, out, concurrency=a.concurrency, seed=SEED,
                          limit=a.limit))


if __name__ == "__main__":
    main()
