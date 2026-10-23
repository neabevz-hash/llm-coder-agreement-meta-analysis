"""AI full-text proposals (protocol, section 11b): Claude drafts a decision for every retrieved full text.
Template: papers/ai-dependence-correlates/fulltext/ft_screen.py (unchanged logic).

Reads the fixed prompt and schema from ft_prompt.md, the retrieved reports from retrieval_log.csv and their texts
from fulltext/text/<rec_id>.txt, and appends one JSON line per report to fulltext/llm/<name>.jsonl (resumable).
The proposals are drafts; R1 decides every report.

Run (pilot):  .venv/Scripts/python.exe papers/llm-coder-agreement-meta/fulltext/ft_screen.py --run 2026-10-21 --name pilot --only R.... (five reports)
Run (all):    .venv/Scripts/python.exe papers/llm-coder-agreement-meta/fulltext/ft_screen.py --run 2026-10-21 --name ft_2026-10-21
Run (D5):     ... --name ft_2026-10-21_sonnet --model sonnet --effort medium --strip-refs --skip fulltext/llm/ft_2026-10-21.jsonl
              (Opus used up the Claude Max limit; the remaining reports go to Sonnet 5.5 with the reference list cut; deviations.md, D5)
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
ROOT = PAPER.parents[1]
sys.path.insert(0, str(ROOT / "harness"))

from llmaudit.judge import Judge, judge_all  # noqa: E402

SEED = 20261025
MAX_CHARS = 400_000   # about 110k tokens; longer texts (some theses) are cut and the prompt says so
MODELS = {"opus": "claude-opus-5-5", "sonnet": "claude-sonnet-5-5"}
REF_HEAD = re.compile(r"^\s*(?:\d+\.?\s*)?(references|bibliography|works cited|literature cited|reference list)\s*$", re.I | re.M)
APPENDIX = re.compile(r"^\s*(?:[A-Z]\.?\s+)?(appendix|appendices|supplementary (?:material|materials|information)|online appendix)\b",
                      re.I | re.M)


def strip_refs(text: str) -> str:
    """Cut the reference list: from the last reference heading in the back 60% of the text to the next appendix
    heading or the end. Appendices after the references stay (agreement tables are sometimes there)."""
    heads = [m for m in REF_HEAD.finditer(text) if m.start() >= 0.4 * len(text)]
    if not heads:
        return text
    m = heads[-1]
    a = APPENDIX.search(text, m.end())
    end = a.start() if a else len(text)
    return text[:m.start()] + "\n[Reference list removed]\n" + text[end:]


def load_prompt() -> tuple[str, dict, str]:
    md = (HERE / "ft_prompt.md").read_text(encoding="utf-8")
    blocks = re.findall(r"```(\w*)\n(.*?)```", md, re.S)
    system = next(body for lang, body in blocks if lang == "" and body.startswith("You are assessing"))
    schema = json.loads(next(body for lang, body in blocks if lang == "json"))
    user = next(body for lang, body in blocks if lang == "" and body.startswith("Report {k}"))
    return system.strip(), schema, user


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--only", nargs="*", help="rec_ids to process (e.g., the pilot set)")
    ap.add_argument("--concurrency", type=int, default=3)
    ap.add_argument("--model", choices=list(MODELS), default="opus")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--strip-refs", action="store_true", help="cut the reference list before sending (D5)")
    ap.add_argument("--skip", help="JSONL of proposals already made, relative to the paper folder (their reports are skipped)")
    a = ap.parse_args()
    system, schema, user_tpl = load_prompt()
    recs = {}
    for line in (PAPER / "search" / "runs" / a.run / "records_unique.jsonl").open(encoding="utf-8"):
        u = json.loads(line)
        recs[u["rec_id"]] = u
    log = [r for r in csv.DictReader((HERE / "retrieval_log.csv").open(encoding="utf-8-sig")) if r["status"] == "retrieved"]
    skip = set()
    if a.skip:
        skip = {json.loads(line)["conv_id"] for line in (PAPER / a.skip).open(encoding="utf-8") if line.strip()}
    items = []
    for k, r in enumerate(sorted(log, key=lambda x: x["rec_id"]), 1):
        if (a.only and r["rec_id"] not in a.only) or r["rec_id"] in skip:
            continue
        raw = (HERE / "text" / f"{r['rec_id']}.txt").read_text(encoding="utf-8")
        text = raw.split("\n\n", 1)[1] if raw.startswith("REC_ID:") else raw
        if a.strip_refs:
            text = strip_refs(text)
        u = recs[r["rec_id"]]
        items.append({"conv_id": r["rec_id"], "k": k, "title": u["title"], "year": u["year"], "venue": u["venue"],
                      "source": r["source"], "chars": len(text),
                      "truncated": f"; cut to the first {MAX_CHARS:,} characters" if len(text) > MAX_CHARS else "",
                      "text": text[:MAX_CHARS]})

    def render(it: dict) -> str:
        return user_tpl.format(**{k: it[k] for k in ("k", "title", "year", "venue", "source", "truncated", "text")},
                               chars=f"{it['chars']:,}")

    judge = Judge(system_prompt=system, schema=schema, model=MODELS[a.model], effort=a.effort, timeout=900)
    out = HERE / "llm" / f"{a.name}.jsonl"
    asyncio.run(judge_all(items, render, judge, out, concurrency=a.concurrency, seed=SEED, limit=a.limit))


if __name__ == "__main__":
    main()
