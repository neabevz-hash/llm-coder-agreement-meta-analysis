"""Records of the citation search for screening (protocol §9, §11b; deviations.md, D6).

citation_chase.py found the works citing or cited by the included reports and the syntheses that the main search had
not found, and applied the main search's automatic rules (year from 2020, non-study record types, rule 6). The records
that passed go through the same selection as the main records: two AI title/abstract passes (screening/llm_screen.py,
same frozen prompt), then R1 decides every record that at least one pass kept, at full text when an open full text
exists. This script gives them record IDs R20001, R20002, ... (in source-ID order; the main run ends at R12786) in the
record format of the main search, and writes, in the same run folder:
  records_unique.jsonl - the records, read by fetch_oa.py, ft_screen.py, ft_md.py and extraction/common.py;
  screening.csv        - the input of llm_screen.py (--input).
Template: papers/ai-dependence-correlates/search/chase_records.py.

Run: .venv/Scripts/python.exe -I papers/llm-coder-agreement-meta/search/chase_records.py --run 2026-10-23-citations
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIRST_ID = 20001


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    run = HERE / "runs" / a.run
    hits = [r for r in (json.loads(l) for l in (run / "records_new.jsonl").open(encoding="utf-8")) if not r["auto_removed"]]
    hits.sort(key=lambda r: r["source_id"])
    out = []
    for i, h in enumerate(hits):
        out.append({
            "rec_id": f"R{FIRST_ID + i}", "title": h["title"], "abstract": h.get("abstract", ""), "year": h.get("year"),
            "first_author": h.get("first_author", ""), "venue": h.get("venue", ""), "doi": h.get("doi", ""),
            "all_dois": h.get("doi", ""), "pmid": h.get("pmid", ""), "types": f"{'s2' if h['source'].endswith('_s2') else 'openalex'}:{h.get('type', '')}",
            "language": h.get("language", ""), "sources": h["source"], "n_sources": 1,
            "source_ids": (f"https://openalex.org/{h['source_id']}" if h["source_id"].startswith("W") else h["source_id"]),
            "url": f"https://doi.org/{h['doi']}" if h.get("doi") else (
                f"https://openalex.org/{h['source_id']}" if h["source_id"].startswith("W") else ""),
            "link": f"https://doi.org/{h['doi']}" if h.get("doi") else "", "chase": h["source"], "auto_removed": "",
        })
    with (run / "records_unique.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    cols = ["rec_id", "title", "abstract", "year", "first_author", "venue", "doi", "pmid", "link", "language", "types", "sources"]
    with (run / "screening.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print(f"{len(out)} records: {out[0]['rec_id']}..{out[-1]['rec_id']} -> {run / 'records_unique.jsonl'}, screening.csv")


if __name__ == "__main__":
    main()
