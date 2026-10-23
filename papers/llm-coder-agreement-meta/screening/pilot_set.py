"""Pilot set for the screener prompt (llm_screener_prompt.md, section "Pilot before freezing").

Two parts, written to screening/pilot/pilot_set.csv (same columns as screening.csv):
  P-Sxx  the 23 seed studies (search/seed_set.csv), title, abstract and venue from the check run's unique records
         (search/runs/2026-10-21-ab-check/records_unique.jsonl, matched by recall_seed_set.json);
  P-Vxx  the 80 records of novelty/volume_sample.csv with manual labels (17 eligible, 6 unclear, 57 not eligible).
The reference labels go to screening/pilot/pilot_reference.csv; the AI passes never see them.

Run: .venv/Scripts/python.exe papers/llm-coder-agreement-meta/screening/pilot_set.py
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
RUN = PAPER / "search" / "runs" / "2026-10-21-ab-check"


def main():
    recs = {json.loads(l)["rec_id"]: json.loads(l) for l in (RUN / "records_unique.jsonl").open(encoding="utf-8")}
    recall = json.loads((RUN / "recall_seed_set.json").read_text(encoding="utf-8"))
    seeds = {s["seed_id"]: s for s in csv.DictReader((PAPER / "search" / "seed_set.csv").open(encoding="utf-8-sig"))}
    rows, ref = [], []
    for st in recall["studies"]:
        r = recs[st["rec_id"]]
        pid = f"P-{st['seed_id']}"
        rows.append({"rec_id": pid, "title": r["title"], "year": r["year"], "venue": r["venue"], "types": r["types"],
                     "abstract": r["abstract"]})
        ref.append({"rec_id": pid, "part": "seed", "reference": seeds[st["seed_id"]]["r1_decision"] or "unclear",
                    "task": seeds[st["seed_id"]]["task_type_draft"]})
    vs = list(csv.DictReader((PAPER / "novelty" / "volume_sample.csv").open(encoding="utf-8-sig")))
    for i, v in enumerate(vs, 1):
        pid = f"P-V{i:02d}"
        rows.append({"rec_id": pid, "title": v["title"], "year": v["year"], "venue": v["venue"], "types": "",
                     "abstract": v["abstract"]})
        ref.append({"rec_id": pid, "part": "volume_sample", "reference": v["manual_eligible"], "task": v["manual_domain"]})
    out = HERE / "pilot"
    out.mkdir(exist_ok=True)
    with (out / "pilot_set.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    with (out / "pilot_reference.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(ref[0]))
        w.writeheader()
        w.writerows(ref)
    print(f"pilot records: {len(rows)} (seeds {sum(r['part'] == 'seed' for r in ref)}, volume sample {sum(r['part'] == 'volume_sample' for r in ref)})")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
