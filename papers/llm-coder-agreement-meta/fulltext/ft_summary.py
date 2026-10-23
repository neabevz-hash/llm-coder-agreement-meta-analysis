"""Full-text stage summary and PRISMA 2020 counts (protocol §11b; deviations D4, D5).

Inputs: screening/decisions/tiab_summary.json, the run's dedup_report.json, fulltext/retrieval_log.csv,
fulltext/decisions/ft_R1.csv (from ft_md.py parse) and the AI proposals in fulltext/llm/<name>.jsonl (several runs:
Opus first, then Sonnet, D5; a report keeps its first proposal). Agreement between R1 and the proposals is reported
overall and per model. Template: papers/ai-dependence-correlates/fulltext/ft_summary.py.

Writes fulltext/prisma_counts.json and prints it.
Run: .venv/Scripts/python.exe papers/llm-coder-agreement-meta/fulltext/ft_summary.py --name ft_2026-10-21 ft_2026-10-21_sonnet
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
TASK = re.compile(r"\bT([1-4])\b")


def agreement(rows: list[dict]) -> dict:
    return {
        "reports": len(rows),
        "ai_unclear": sum(1 for r in rows if r["ai"] == "unclear"),
        "agreement_eligible_vs_not": sum(1 for r in rows if r["ai"] == r["r1"]),
        "agreement_when_ai_decided": sum(1 for r in rows if r["ai"] != "unclear" and r["ai"] == r["r1"]),
        "ai_decided": sum(1 for r in rows if r["ai"] != "unclear"),
        "same_exclusion_reason": sum(1 for r in rows if r["r1"] == "not_eligible" == r["ai"] and r["r1_reason"] == r["ai_reason"]),
        "r1_accepted_with_equals": sum(1 for r in rows if r["code"].startswith("=")),
        "r1_eligible_ai_not": sum(1 for r in rows if r["r1"] == "eligible" and r["ai"] == "not_eligible"),
        "r1_not_ai_eligible": sum(1 for r in rows if r["r1"] == "not_eligible" and r["ai"] == "eligible"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True, nargs="+")
    a = ap.parse_args()
    tiab = json.loads((PAPER / "screening" / "decisions" / "tiab_summary.json").read_text(encoding="utf-8"))
    dedup = json.loads((PAPER / "search" / "runs" / tiab["run"] / "dedup_report.json").read_text(encoding="utf-8"))
    log = list(csv.DictReader((HERE / "retrieval_log.csv").open(encoding="utf-8-sig")))
    r1 = {r["rec_id"]: r for r in csv.DictReader((HERE / "decisions" / "ft_R1.csv").open(encoding="utf-8-sig"))}
    ai: dict[str, dict] = {}
    for name in a.name:
        for line in (HERE / "llm" / f"{name}.jsonl").open(encoding="utf-8"):
            if line.strip():
                d = json.loads(line)
                ai.setdefault(d["conv_id"], {"codes": d["codes"], "model": d["judge"]["model_requested"]})
    retrieved = [r["rec_id"] for r in log if r["status"] == "retrieved"]
    assessed = {rid: r1[rid] for rid in retrieved if rid in r1}
    rows = [{"rid": rid, "r1": r["decision"], "r1_reason": r["reason"], "code": r["code"],
             "ai": ai[rid]["codes"]["decision"], "ai_reason": ai[rid]["codes"]["reason"], "model": ai[rid]["model"],
             "ai_task": ai[rid]["codes"]["task_type"], "note": r["note"]} for rid, r in assessed.items()]
    included = [x for x in rows if x["r1"] == "eligible"]
    # task type: R1's note when it names one (e.g. "= T3", "+ T2"), otherwise the AI proposal
    tasks = Counter((TASK.search(x["note"] or "") and f"T{TASK.search(x['note']).group(1)}") or x["ai_task"] for x in included)
    out = {
        "records_identified": dedup["records_total"],
        "records_per_source": dedup["records_per_source"],
        "duplicates_removed": dedup["duplicates_removed"],
        "removed_by_automation": {"non_study_records": dedup["auto_removed_non_study_records"],
                                  "no_exact_search_term_match": dedup["auto_removed_no_search_term_match"]},
        "records_screened_title_abstract": tiab["records_screened"],
        "records_excluded_title_abstract": tiab["excluded_title_abstract"],
        "reports_sought_for_retrieval": len(log),
        "reports_not_retrieved": len(log) - len(retrieved),
        "reports_retrieved_by_source": dict(Counter(r["source"] for r in log if r["status"] == "retrieved")),
        "reports_assessed_for_eligibility": len(assessed),
        "reports_excluded_full_text": dict(Counter(x["r1_reason"] for x in rows if x["r1"] == "not_eligible")),
        "reports_included": len(included),
        "included_by_task_type": dict(tasks),
        "undecided": [x["rid"] for x in rows if x["r1"] not in ("eligible", "not_eligible")],
        "ai_proposals": {"overall": agreement(rows),
                         "by_model": {m: agreement([x for x in rows if x["model"] == m]) for m in sorted({x["model"] for x in rows})}},
    }
    (HERE / "prisma_counts.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
