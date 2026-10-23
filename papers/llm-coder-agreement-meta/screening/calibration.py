"""Blind calibration sample for title/abstract screening (protocol, section 11b).

Draws a fixed sample of 400 records (protocol v1.0) from the records in search/runs/<run>/screening.csv with a fixed seed, in a random display order,
and writes screening/calibration/<run>/sample.csv: record fields only, no AI labels. The same sample is drawn
on every run of this script, so anyone can check that it was not hand-picked.

Template: papers/sports-betting-prevalence/screening/calibration.py.
Run: .venv/Scripts/python.exe papers/llm-coder-agreement-meta/screening/calibration.py --run YYYY-MM-DD
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEARCH_RUNS = HERE.parent / "search" / "runs"
SEED = 20261022          # fixed in protocol v1.0
SAMPLE_SIZE = 400
FIELDS = ["k", "rec_id", "title", "abstract", "year", "first_author", "venue", "types_plain", "language", "doi", "link"]


def types_plain(types: str) -> str:
    return "; ".join(sorted({t.split(":", 1)[1] for t in types.split(" | ") if ":" in t and t.split(":", 1)[1]}))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    src = SEARCH_RUNS / a.run / "screening.csv"
    rows = list(csv.DictReader(src.open(encoding="utf-8-sig")))
    ids = sorted(r["rec_id"] for r in rows)
    k = min(SAMPLE_SIZE, len(ids))
    sample = random.Random(SEED).sample(ids, k)          # random order = display order
    by_id = {r["rec_id"]: r for r in rows}
    out_dir = HERE / "calibration" / a.run
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "sample.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for i, rid in enumerate(sample, 1):
            r = by_id[rid]
            w.writerow({**r, "k": i, "types_plain": types_plain(r["types"])})
    meta = {"run": a.run, "seed": SEED, "sample_size_rule": SAMPLE_SIZE, "records_in_list": len(ids), "sample_size": k,
            "screening_csv_sha256": hashlib.sha256(src.read_bytes()).hexdigest(), "rec_ids_in_display_order": sample}
    (out_dir / "sample_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{k} of {len(ids)} records -> {out_dir / 'sample.csv'}")


if __name__ == "__main__":
    main()
