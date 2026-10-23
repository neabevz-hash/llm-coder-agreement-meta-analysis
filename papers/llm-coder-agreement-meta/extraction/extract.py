"""AI extraction and risk-of-bias drafts (protocol §11c, §14): Claude fills the extraction form for every study.

Reads the fixed prompt from extract_prompt.md and the jobs from jobs.json (make_study_map.py); the texts are sent with
the reference list cut (fulltext/ft_screen.strip_refs). Appends one JSON line per job to extraction/draft/<name>.jsonl
(resumable). The drafts are stored unchanged; R1 verifies every value. Default model: Claude Sonnet 5.5 at effort medium
(deviations.md, D7). Template: papers/ai-dependence-correlates/extraction/extract.py.

Before a full run: state the number of calls and the expected use of the Claude Max limit to R1, and check that no
runner is left over (Get-CimInstance Win32_Process, python.exe with ft_screen, llm_screen or extract in the command
line; claude.exe started by them).

Run (pilot): .venv/Scripts/python.exe papers/llm-coder-agreement-meta/extraction/extract.py --run 2026-10-21 --name pilot_<date> --only ST...
Run (all):   .venv/Scripts/python.exe papers/llm-coder-agreement-meta/extraction/extract.py --run 2026-10-21 --name extract_<date>
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
ROOT = PAPER.parents[1]
sys.path.insert(0, str(ROOT / "harness"))
sys.path.insert(0, str(PAPER / "fulltext"))

from llmaudit.judge import Judge, judge_all  # noqa: E402
from ft_screen import strip_refs  # noqa: E402

sys.path.insert(0, str(HERE))
from common import load_records  # noqa: E402

SEED = 20261026
MAX_CHARS = 400_000  # per report, after the reference list is cut (about 100k tokens)
MODELS = {"opus": "claude-opus-5-5", "sonnet": "claude-sonnet-5-5"}


def blocks(md: str) -> list[tuple[str, str]]:
    return re.findall(r"```(\w*)\n(.*?)```", md, re.S)


def text_(n: int) -> dict:
    return {"type": "string", "maxLength": n}


def enum_(values: list[str]) -> dict:
    return {"type": "string", "enum": values}


def field(enum: list[str] | None = None) -> dict:
    return {"type": "object",
            "properties": {"value": enum_(enum) if enum else text_(400), "loc": text_(160), "quote": text_(600)},
            "required": ["value", "loc", "quote"], "additionalProperties": False}


def obj(props: dict) -> dict:
    return {"type": "object", "properties": props, "required": list(props), "additionalProperties": False}


def build_schema(spec: dict) -> dict:
    stats = enum_(spec["statistics"])
    study = obj({k: field(v) for k, v in spec["study_fields"].items()})
    task = obj({"task_id": text_(4), "label": text_(200), **{k: field(v) for k, v in spec["task_fields"].items()}})
    config = obj({"config_id": text_(6), **{k: text_(200) for k in spec["config_fields"]},
                  "loc": text_(160), "quote": text_(600)})
    estimate = obj({
        "task": text_(4), "config": text_(6), "reference": text_(200), "statistic": stats, "icc_form": text_(40),
        "value": text_(60), "ci_low": text_(30), "ci_high": text_(30), "se": text_(30), "n_units": text_(40),
        "p_o": text_(30), "p_e": text_(30), "prevalence": text_(60), "confusion_matrix": text_(400),
        "mean_llm": text_(40), "mean_human": text_(40), "sd_llm": text_(40), "sd_human": text_(40),
        "loc": text_(160), "quote": text_(600), "note": text_(300)})
    human = obj({
        "task": text_(4), "same_units": enum_(spec["same_units"]), "comparison": enum_(spec["comparisons"]),
        "statistic": stats, "value": text_(60), "ci_low": text_(30), "ci_high": text_(30), "se": text_(30),
        "n_units": text_(40), "pairs_with": enum_(spec["pairs_with"]), "loc": text_(160), "quote": text_(600)})
    code = obj({"task": text_(4), "config": text_(6), "code": text_(120), "statistic": stats, "value": text_(40),
                "percent_agreement": text_(40), "prevalence": text_(40), "n_units": text_(40), "loc": text_(160)})
    rob_item = obj({"rating": enum_(spec["rob_ratings"]), "reason": text_(400), "loc": text_(160), "quote": text_(600)})
    rob = obj({f"rob_{i}": rob_item for i in range(1, 6)})
    return obj({
        "study": study,
        "tasks": {"type": "array", "minItems": 1, "maxItems": 30, "items": task},
        "configurations": {"type": "array", "maxItems": 80, "items": config},
        "estimates": {"type": "array", "maxItems": 400, "items": estimate},
        "human_reliability": {"type": "array", "maxItems": 60, "items": human},
        "codes": {"type": "array", "maxItems": 60, "items": code},
        "rob": rob, "excluded": text_(1500), "consistency_notes": text_(2000), "note": text_(1000)})


def load_prompt() -> tuple[str, str, str, dict]:
    md = (HERE / "extract_prompt.md").read_text(encoding="utf-8")
    b = blocks(md)
    system = next(body for lang, body in b if lang == "" and body.startswith("You are extracting"))
    preamble = next(body for lang, body in b if lang == "" and body.startswith("EXTRACTION FORM"))
    job_tpl = next(body for lang, body in b if lang == "" and body.startswith("JOB {job_id}"))
    spec = json.loads(next(body for lang, body in b if lang == "json"))
    return system.strip(), preamble, job_tpl, build_schema(spec)


def report_text(k: str) -> str:
    raw = (PAPER / "fulltext" / "text" / f"{k}.txt").read_text(encoding="utf-8")
    return strip_refs(raw.split("\n\n", 1)[1] if raw.startswith("REC_ID:") else raw)


def build_items(run: str, only: list[str] | None) -> list[dict]:
    _, preamble, job_tpl, _ = load_prompt()
    recs = load_records(run)
    items = []
    for j in json.loads((HERE / "jobs.json").read_text(encoding="utf-8")):
        if only and j["job_id"] not in only:
            continue
        main_rec = recs[j["main"]]
        main_text = report_text(j["main"])
        links = []
        if j["link_reason"]:
            links.append(f"Linked reports: {j['link_reason']}")
        if j["attached"]:
            links.append(f"Attached below: {', '.join(j['attached'])}")
        if j["listed_only"]:
            links.append(f"Other versions of this study, not attached (their values are in the reports given): "
                         f"{', '.join(j['listed_only'])}")
        for po in j["possible_overlap"]:
            links.append(f"Note for the study notes: {po}")
        if j.get("job_notes"):
            links.append(f"Note: {j['job_notes']}")
        att = []
        for e in j["attached"]:
            u = recs[e]
            t = report_text(e)
            att.append(f"\nATTACHED REPORT {e}\nTitle: {u['title']}\nYear: {u.get('year')}; venue: {u.get('venue')}; "
                       f"DOI: {u.get('doi') or 'none'}\nFull text ({len(t):,} characters; reference list removed):\n"
                       f"{t[:MAX_CHARS]}")
        body = job_tpl.format(
            job_id=j["job_id"], study_id=j["study_id"], scope=j["scope"], links="\n".join(links), main_id=j["main"],
            main_title=main_rec["title"], main_year=main_rec.get("year"), main_venue=main_rec.get("venue"),
            main_doi=main_rec.get("doi") or "none", main_chars=f"{len(main_text):,}",
            main_truncated=f"; cut to the first {MAX_CHARS:,} characters" if len(main_text) > MAX_CHARS else "",
            main_text=main_text[:MAX_CHARS], attached="\n".join(att))
        items.append({"conv_id": j["job_id"], "prompt": preamble + "\n" + body})
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--only", nargs="*", help="job ids (study ids) to process")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--concurrency", type=int, default=3)
    ap.add_argument("--model", choices=list(MODELS), default="sonnet")
    ap.add_argument("--effort", default="medium")
    a = ap.parse_args()
    system, _, _, schema = load_prompt()
    items = build_items(a.run, a.only)
    # Benchmark papers with many models can need a long answer.
    judge = Judge(system_prompt=system, schema=schema, model=MODELS[a.model], effort=a.effort, timeout=2400,
                  extra_env={"CLAUDE_CODE_MAX_OUTPUT_TOKENS": "64000"})
    out = HERE / "draft" / f"{a.name}.jsonl"
    asyncio.run(judge_all(items, lambda it: it["prompt"], judge, out, concurrency=a.concurrency, seed=SEED,
                          limit=a.limit))


if __name__ == "__main__":
    main()
