"""Estimates drafted from the AI full-text proposals (deviations.md, D7): no separate extraction pass for the numbers.

The full-text proposals (fulltext/llm/*.jsonl; a report keeps its first proposal: Opus, then Sonnet, D5) already list
the LLM-human agreement statistics of every report: model, configuration, statistic, value, n, location and a verbatim
quote. This script turns them into the draft estimate table of each study (extraction/study_map.csv): the statistics of
the study's main and attached reports, each value once. The listed-only versions are not used (their values are in the
main report). Every value is checked against the source text by script:
  value_in_text  the value as printed (or its number) occurs in the report's text;
  quote_in_text  every part of the quote (split at "|" and "...") occurs in the text (whitespace and case ignored).
Values that are not a single number (ranges, several values, confusion matrices) are kept with parse = "complex".

Writes extraction/ft_estimates.csv (one row per statistic) and prints the check rates.
Run: .venv/Scripts/python.exe -I papers/llm-coder-agreement-meta/extraction/estimates_from_ft.py
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
RUNS = ["ft_2026-10-21", "ft_2026-10-21_sonnet", "ft_chase_2026-10-23"]   # first proposal per report wins (D5)
NUM = re.compile(r"^[-−–]?\d*[.,]?\d+%?$")


def norm(s: str) -> str:
    s = (s or "").replace("−", "-").replace("–", "-").replace("’", "'")
    return re.sub(r"\s+", " ", s).strip().lower()


def proposals() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for name in RUNS:
        for line in (PAPER / "fulltext" / "llm" / f"{name}.jsonl").open(encoding="utf-8"):
            if line.strip():
                d = json.loads(line)
                out.setdefault(d["conv_id"], {**d["codes"], "_model": d["judge"]["model_requested"]})
    return out


def text_of(k: str) -> str:
    raw = (PAPER / "fulltext" / "text" / f"{k}.txt").read_text(encoding="utf-8")
    return norm(raw.split("\n\n", 1)[1] if raw.startswith("REC_ID:") else raw)


def parse_value(v: str) -> tuple[str, str]:
    """(number as a proportion or as printed, parse status)"""
    s = v.strip().replace(",", ".").replace("−", "-").replace("–", "-")
    if not NUM.match(s):
        return "", "complex"
    if s.endswith("%"):
        return f"{float(s[:-1]) / 100:.4g}", "percent"
    return s, "number"


def main():
    props = proposals()
    sm = list(csv.DictReader((HERE / "study_map.csv").open(encoding="utf-8")))
    rows, texts, seen = [], {}, set()
    for r in sm:
        if r["role"] not in ("main", "attached"):
            continue
        k, sid = r["rec_id"], r["study_id"]
        if r["scope"]:   # a second study inside a thesis: its statistics stay with the report's first study
            continue
        p = props.get(k)
        if p is None:
            continue
        texts.setdefault(k, text_of(k))
        t = texts[k]
        for s in p["agreement_stats"]:
            key = (sid, norm(s["model"]), s["statistic"], norm(s["value"]), norm(s["configuration"]))
            if key in seen:
                continue
            seen.add(key)
            num, how = parse_value(s["value"])
            v = norm(s["value"]).rstrip("%")
            parts = [norm(x) for x in re.split(r"\s*(?:\.\.\.|…|\|)\s*", s["quote"]) if len(x.strip()) >= 4]
            rows.append({
                "study_id": sid, "rec_id": k, "role": r["role"], "ai_model": p["_model"], "task_type_ai": p["task_type"],
                "model": s["model"], "configuration": s["configuration"], "statistic": s["statistic"],
                "value_raw": s["value"], "value": num, "parse": how, "n_units": s["n_units"],
                "location": s["location"], "quote": s["quote"],
                "value_in_text": bool(v) and (v in t or bool(num and num in t)),
                "quote_in_text": bool(parts) and all(x in t for x in parts),
            })
    for i, x in enumerate(rows, 1):
        x["ft_estimate_id"] = f"F{i:04d}"
    cols = ["ft_estimate_id", *[c for c in rows[0] if c != "ft_estimate_id"]]
    with (HERE / "ft_estimates.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    studies = {x["study_id"] for x in rows}
    n = len(rows)
    print(f"{n} statistics in {len(studies)} studies (of {len({r['study_id'] for r in sm})}); "
          f"value in text {sum(x['value_in_text'] for x in rows)} ({sum(x['value_in_text'] for x in rows) / n:.1%}), "
          f"quote in text {sum(x['quote_in_text'] for x in rows)} ({sum(x['quote_in_text'] for x in rows) / n:.1%}), "
          f"complex values {sum(x['parse'] == 'complex' for x in rows)}")
    print("statistics:", dict(Counter(x["statistic"] for x in rows).most_common()))


if __name__ == "__main__":
    main()
