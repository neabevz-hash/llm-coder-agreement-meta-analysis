"""Shared helpers of the extraction scripts: records of every search run, and the reports R1 judged eligible.

Records come from the main search run and from the citation search (search/runs/*-citations/records_unique.jsonl, once
chase_records.py has written it); their IDs must not overlap. Eligible reports: fulltext/decisions/ft_R1.csv (main run)
and, once R1 has decided the citation-search reports, fulltext/decisions/ft_R1_chase.csv.
Template: papers/ai-dependence-correlates/extraction/common.py.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

PAPER = Path(__file__).resolve().parent.parent
DECISIONS = PAPER / "fulltext" / "decisions"


def load_records(run: str) -> dict[str, dict]:
    recs: dict[str, dict] = {}
    paths = [PAPER / "search" / "runs" / run / "records_unique.jsonl",
             *sorted((PAPER / "search" / "runs").glob("*-citations/records_unique.jsonl"))]
    for p in paths:
        if not p.exists():
            continue
        for line in p.open(encoding="utf-8"):
            u = json.loads(line)
            recs.setdefault(u["rec_id"], u)
    return recs


def eligible_reports() -> list[str]:
    out = []
    for name in ("ft_R1.csv", "ft_R1_chase.csv"):
        p = DECISIONS / name
        if p.exists():
            out += [r["rec_id"] for r in csv.DictReader(p.open(encoding="utf-8-sig")) if r["decision"] == "eligible"]
    return out


def rec_num(k: str) -> int:
    return int(k[1:])
