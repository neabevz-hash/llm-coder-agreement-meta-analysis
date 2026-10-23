"""Recall of a search run on the seed set (protocol §9).

The seed set (seed_set.csv) is drafted from the reference lists of independent syntheses (Seyler et al., 2025;
Gierbolini-Rivera et al., 2026; Hua et al., 2025; Kempny et al., 2026; Na et al., 2025; Li, L., et al., 2026) by
seed_candidates.py, before the check run. A seed counts as found when a unique record carries its DOI or arXiv ID,
or its normalised title starts with the seed's first 60 title characters, and the record is not auto-removed.
Copied from papers/sports-betting-prevalence/search/recall.py.

Run: .venv/Scripts/python.exe papers/llm-coder-agreement-meta/search/recall.py --date 2026-10-21-check
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from dedup import norm_title

HERE = Path(__file__).resolve().parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    a = ap.parse_args()
    run = HERE / "runs" / a.date
    recs = [json.loads(line) for line in (run / "records_unique.jsonl").open(encoding="utf-8")]
    seeds = list(csv.DictReader((HERE / "seed_set.csv").open(encoding="utf-8-sig")))
    rows = []
    for s in seeds:
        keys = {s["doi"].lower()} | ({f"10.48550/arxiv.{s['arxiv'].lower()}"} if s.get("arxiv") else set())
        keys.discard("")
        nt = norm_title(s["title"])
        hit = next((r for r in recs if keys & set((r.get("all_dois") or "").lower().split(";"))), None) \
            or next((r for r in recs if nt and norm_title(r["title"]).startswith(nt[:60])), None)
        rows.append({"seed_id": s["seed_id"], "title": s["title"][:90], "task": s["task_type_draft"],
                     "ai_draft": s["ai_draft"], "found": bool(hit), "rec_id": hit["rec_id"] if hit else "",
                     "sources": hit["sources"] if hit else "", "to_screen": bool(hit) and not hit["auto_removed"]})
    found = sum(r["to_screen"] for r in rows)
    elig = [r for r in rows if r["ai_draft"] == "eligible"]
    report = {"run": a.date, "seed_studies": len(rows), "in_screening_list": found,
              "eligible_drafts": len(elig), "eligible_found": sum(r["to_screen"] for r in elig), "studies": rows}
    (run / "recall_seed_set.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    for r in rows:
        print(f"{'OK  ' if r['to_screen'] else 'MISS'} {r['seed_id']} {r['task']} {r['rec_id']:>6} {r['sources']:<40} {r['title']}")
    print(f"recall: {found} of {len(rows)} (eligible drafts: {report['eligible_found']} of {len(elig)})")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
