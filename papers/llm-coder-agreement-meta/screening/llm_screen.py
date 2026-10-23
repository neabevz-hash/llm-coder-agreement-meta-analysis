"""AI draft labels for title/abstract screening (protocol §11b): two independent passes.

Reads the fixed prompt and schema from llm_screener_prompt.md and the records either from
search/runs/<run>/screening.csv (--run) or from a pilot file (--input), and appends one JSON line per record to
screening/llm/<name>_<pass>.jsonl (resumable). Passes: opus = Claude Opus 5.5, sonnet = Claude Sonnet 5.5, same
prompt, same seeded order. When every record of a full run has a label, <file>.sha256 is written: its hash is
committed before R1's calibration is unblinded. Template: papers/sports-betting-prevalence/screening/llm_screen.py.

Before a launch: state the number of calls to R1 and check for leftover runners
(Get-CimInstance Win32_Process, command line containing llm_screen).

Run:
  .venv/Scripts/python.exe papers/llm-coder-agreement-meta/screening/llm_screen.py --input screening/pilot/pilot_set.csv --name pilot --pass opus
  .venv/Scripts/python.exe papers/llm-coder-agreement-meta/screening/llm_screen.py --run 2026-10-22 --pass sonnet
  ... --run 2026-10-21 --pass opus --exclude screening/manual/2026-10-21/manual_ids.csv   (D3)
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "harness"))

from llmaudit.judge import Judge, judge_all, utcnow  # noqa: E402

SEED = 20261022
PASSES = {"opus": "claude-opus-5-5", "sonnet": "claude-sonnet-5-5"}


def load_prompt() -> tuple[str, dict]:
    md = (HERE / "llm_screener_prompt.md").read_text(encoding="utf-8")
    blocks = re.findall(r"```(\w*)\n(.*?)```", md, re.S)
    system = next(body for lang, body in blocks if lang == "" and body.startswith("You are screening"))
    schema = json.loads(next(body for lang, body in blocks if lang == "json"))
    return system.strip(), schema


def render(item: dict) -> str:
    abstract = item["abstract"].strip() or "[no abstract available]"
    return (f"Record {item['k']} of the screening set.\n"
            f"Title: {item['title']}\n"
            f"Year: {item['year']}\n"
            f"Source/venue: {item['venue']}\n"
            f"Record type(s): {item['types_plain']}\n"
            f"Abstract: {abstract}\n")


def main():
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--run")
    src.add_argument("--input", help="CSV with rec_id, title, year, venue, types, abstract (relative to the paper folder)")
    ap.add_argument("--name", help="output name for --input (default: input file stem)")
    ap.add_argument("--pass", dest="pass_", choices=list(PASSES), required=True)
    ap.add_argument("--exclude", help="CSV with a rec_id column: records R1 screens directly (manual/<run>/manual_ids.csv; D3)")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--concurrency", type=int, default=3)
    ap.add_argument("--effort", default="high")
    a = ap.parse_args()
    system, schema = load_prompt()
    path = PAPER / "search" / "runs" / a.run / "screening.csv" if a.run else PAPER / a.input
    name = a.run if a.run else (a.name or Path(a.input).stem)
    rows = list(csv.DictReader(path.open(encoding="utf-8-sig")))
    excluded = set()
    if a.exclude:
        excluded = {r["rec_id"] for r in csv.DictReader((PAPER / a.exclude).open(encoding="utf-8-sig"))}
        rows = [r for r in rows if r["rec_id"] not in excluded]
        print(f"excluded {len(excluded)} records screened by R1 directly; {len(rows)} remain for the AI pass")
    items = []
    for k, r in enumerate(rows, 1):
        types_plain = "; ".join(sorted({t.split(":", 1)[1] for t in (r.get("types") or "").split(" | ")
                                        if ":" in t and t.split(":", 1)[1]}))
        items.append({"conv_id": r["rec_id"], "k": k, "title": r["title"], "year": r["year"], "venue": r["venue"],
                      "types_plain": types_plain, "abstract": r["abstract"]})
    judge = Judge(system_prompt=system, schema=schema, model=PASSES[a.pass_], effort=a.effort, timeout=600)
    out = HERE / "llm" / f"{name}_{a.pass_}.jsonl"
    out.parent.mkdir(exist_ok=True)
    asyncio.run(judge_all(items, render, judge, out, concurrency=a.concurrency, seed=SEED, limit=a.limit))
    done = {json.loads(line)["conv_id"] for line in out.open(encoding="utf-8") if line.strip()} if out.exists() else set()
    if a.limit is None and done == {it["conv_id"] for it in items}:
        digest = hashlib.sha256(out.read_bytes()).hexdigest()
        (out.parent / (out.name + ".sha256")).write_text(
            json.dumps({"file": out.name, "sha256": digest, "records": len(done), "written_at_utc": utcnow(),
                        "model": PASSES[a.pass_], "system_prompt_sha": judge.fingerprint()["system_prompt_sha"],
                        "excluded_screened_by_R1": len(excluded)}, indent=2) + "\n",
            encoding="utf-8")
        print(f"all {len(done)} records labelled; sha256 {digest}")


if __name__ == "__main__":
    main()
