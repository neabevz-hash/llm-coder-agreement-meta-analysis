"""Evaluation of the screener-prompt pilot (llm_screener_prompt.md, "Pilot before freezing").

Reads screening/llm/pilot_opus.jsonl, pilot_sonnet.jsonl and screening/pilot/pilot_reference.csv and reports:
- seeds: every seed must be kept (include or unsure) by at least one pass;
- volume sample: manually eligible and unclear records kept by at least one pass (sensitivity of the AI rule
  "exclude only if both passes exclude"), manually not-eligible records excluded by both (specificity), per pass and union;
- every record where the rule and the manual label disagree, with both notes, for prompt revision.
Writes screening/pilot/pilot_eval.json.

Run: .venv/Scripts/python.exe papers/llm-coder-agreement-meta/screening/pilot_eval.py
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(p: Path) -> dict:
    out = {}
    for line in p.open(encoding="utf-8"):
        if line.strip():
            d = json.loads(line)
            res = d.get("codes") or {}
            out[d["conv_id"]] = {"decision": res.get("decision"), "reason": res.get("reason"), "note": res.get("note")}
    return out


def main():
    ref = {r["rec_id"]: r for r in csv.DictReader((HERE / "pilot" / "pilot_reference.csv").open(encoding="utf-8-sig"))}
    titles = {r["rec_id"]: r["title"] for r in csv.DictReader((HERE / "pilot" / "pilot_set.csv").open(encoding="utf-8-sig"))}
    o, s = load(HERE / "llm" / "pilot_opus.jsonl"), load(HERE / "llm" / "pilot_sonnet.jsonl")
    keep = lambda d: d in ("include", "unsure")
    rows = []
    for rid, r in ref.items():
        od, sd = (o.get(rid) or {}).get("decision"), (s.get(rid) or {}).get("decision")
        rows.append({"rec_id": rid, "part": r["part"], "reference": r["reference"], "opus": od, "sonnet": sd,
                     "kept_union": keep(od) or keep(sd), "title": titles[rid][:110],
                     "opus_reason": (o.get(rid) or {}).get("reason"), "sonnet_reason": (s.get(rid) or {}).get("reason"),
                     "opus_note": (o.get(rid) or {}).get("note"), "sonnet_note": (s.get(rid) or {}).get("note")})

    def rate(sub, cond):
        sub = list(sub)
        return {"n": len(sub), "k": sum(1 for x in sub if cond(x))}

    seeds = [x for x in rows if x["part"] == "seed"]
    vs = [x for x in rows if x["part"] == "volume_sample"]
    pos = [x for x in vs if x["reference"] in ("yes", "unclear")]
    neg = [x for x in vs if x["reference"] == "no"]
    rep = {
        "seeds_kept_union": rate(seeds, lambda x: x["kept_union"]),
        "seeds_kept_opus": rate(seeds, lambda x: keep(x["opus"])),
        "seeds_kept_sonnet": rate(seeds, lambda x: keep(x["sonnet"])),
        "volume_eligible_or_unclear_kept_union": rate(pos, lambda x: x["kept_union"]),
        "volume_eligible_kept_union": rate([x for x in pos if x["reference"] == "yes"], lambda x: x["kept_union"]),
        "volume_not_eligible_excluded_by_both": rate(neg, lambda x: not x["kept_union"]),
        "volume_not_eligible_excluded_opus": rate(neg, lambda x: not keep(x["opus"])),
        "volume_not_eligible_excluded_sonnet": rate(neg, lambda x: not keep(x["sonnet"])),
        "missing_labels": [x["rec_id"] for x in rows if x["opus"] is None or x["sonnet"] is None],
        "disagreements": [x for x in rows if (x["reference"] in ("eligible", "yes", "unclear")) != x["kept_union"]],
    }
    (HERE / "pilot" / "pilot_eval.json").write_text(json.dumps({"summary": {k: v for k, v in rep.items() if k != "disagreements"},
                                                                "disagreements": rep["disagreements"], "rows": rows},
                                                               ensure_ascii=False, indent=1), encoding="utf-8")
    for k, v in rep.items():
        if k != "disagreements":
            print(k, v)
    print("\nDisagreements with the reference (rule = exclude only if both passes exclude):")
    for x in rep["disagreements"]:
        print(f"  {x['rec_id']} ref={x['reference']} opus={x['opus']}/{x['opus_reason']} sonnet={x['sonnet']}/{x['sonnet_reason']} | {x['title']}")
        print(f"      opus: {x['opus_note']}\n      sonnet: {x['sonnet_note']}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
