"""Records R1 screens directly, without AI labels (deviations.md, D3).

On 2026-10-22, with both AI passes stopped about halfway, R1 chose to screen 1,000 of the remaining records himself.
The pool is every record of the screening list that neither pass has labelled and that is not in the calibration
sample; 1,000 are drawn with random.Random(SEED).sample over the sorted pool, in random order. The AI passes then
skip these records (llm_screen.py --exclude), so no AI label exists for them and R1 screens them blind.
Writes screening/manual/<run>/manual_ids.csv and manual_meta.json.

Run: .venv/Scripts/python.exe papers/llm-coder-agreement-meta/screening/manual_split.py --run 2026-10-21
"""
from __future__ import annotations

import argparse
import csv
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUNS = HERE.parent / "search" / "runs"
SEED, SIZE = 20261024, 1000


def labelled(run: str, p: str) -> set[str]:
    path = HERE / "llm" / f"{run}_{p}.jsonl"
    return {json.loads(line)["conv_id"] for line in path.open(encoding="utf-8") if line.strip()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    a = ap.parse_args()
    ids = sorted(r["rec_id"] for r in csv.DictReader((RUNS / a.run / "screening.csv").open(encoding="utf-8-sig")))
    sample = {r["rec_id"] for r in csv.DictReader((HERE / "calibration" / a.run / "sample.csv").open(encoding="utf-8-sig"))}
    done = {p: labelled(a.run, p) for p in ("opus", "sonnet")}
    pool = [i for i in ids if i not in sample and i not in done["opus"] and i not in done["sonnet"]]
    chosen = random.Random(SEED).sample(pool, SIZE)
    out = HERE / "manual" / a.run
    out.mkdir(parents=True, exist_ok=True)
    if (out / "manual_ids.csv").exists():
        sys.exit(f"{out / 'manual_ids.csv'} already exists; refusing to redraw")
    with (out / "manual_ids.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["order", "rec_id"])
        w.writerows(enumerate(chosen, 1))
    meta = {"run": a.run, "seed": SEED, "size": SIZE, "records_in_list": len(ids), "calibration_sample": len(sample),
            "labelled_opus": len(done["opus"]), "labelled_sonnet": len(done["sonnet"]),
            "labelled_by_either": len(done["opus"] | done["sonnet"]), "pool": len(pool),
            "drawn_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "rule": "deviations.md, D3"}
    (out / "manual_meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(meta, indent=1))


if __name__ == "__main__":
    main()
