"""Full-text decision files in Markdown (protocol §11b). Template: papers/ai-dependence-correlates/fulltext/ft_md.py.

Each retrieved report is one block: title, year, venue, links to the full text (local PDF or text, and the source
URL), and the AI proposal: decision, primary reason, task type, construct, texts, models, human reference,
human–human agreement, and the LLM–human agreement statistics with value, location and a verbatim quote. R1 writes a code in the decision line:
  =        agree with the AI proposal
  +        eligible
  -1 … -9  not eligible, the digit is the primary reason (REASONS below)
  ?        not decided yet (must be resolved before the files are closed)
Anything after the code is a note.

  make  --run 2026-10-21 --name ft_2026-10-21 ft_2026-10-21_sonnet   write fulltext/decisions/ft_R1_<nn>.md from fulltext/llm/<name>.jsonl
  parse FILE... --out CSV         decisions -> CSV, and a check that every report has a valid code
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
FILE_SIZE = 50
REASONS = {
    "1": ("E6_design", "обзор, метаанализ, комментарий, позиция, протокол без результатов"),
    "2": ("E5_no_generative_llm", "нет генеративной LLM (только BERT, классическое ML, словари) или только согласие LLM с LLM"),
    "3": ("E1_humans_rate_llm", "люди оценивают ответы LLM, а LLM сама ничего не размечает"),
    "4": ("E2_external_criterion", "эталон — диагноз, самоотчёт автора текста, поведение или исход, а не разметка людьми"),
    "5": ("E3_not_psychological", "нет психологического конструкта: медицинское кодирование, оценка знаний, тональность, позиция, хейт"),
    "6": ("E4_theme_level_only", "согласие только на уровне тем или выжимок, без статистики по единицам"),
    "7": ("no_human_coding", "люди не размечали те же единицы по той же схеме, или нет цифр согласия LLM с людьми"),
    "8": ("E7_duplicate", "та же оценка, что в другом отчёте (связать)"),
    "9": ("other", "другое — напишите почему"),
}
AI_TO_CODE = {"E6_design": "-1", "E5_no_generative_llm": "-2", "E1_humans_rate_llm": "-3", "E2_external_criterion": "-4",
              "E3_not_psychological": "-5", "E4_theme_level_only": "-6", "no_human_coding": "-7", "other": "-9"}
MODEL_RU = {"claude-opus-5-5": "Opus 5.5", "claude-sonnet-5-5": "Sonnet 5.5"}
HEADER_RE = re.compile(r"^###\s+(\d+)\s*·\s*(R\d{4,5})\b")
DECISION_RE = re.compile(r"^\**\s*Решение\s*:?\s*\**\s*:?\s*(.*)$", re.I)
AI_RE = re.compile(r"^\**\s*ИИ предлагает\s*:?\s*\**\s*:?\s*(\S+)")

GUIDE = """**Как размечать.** Откройте полный текст (ссылка в блоке), сверьте предложение ИИ и допишите код в строку **Решение:**.

| Код | Что значит |
| --- | --- |
| `=` | согласен с ИИ |
| `+` | подходит: генеративная LLM размечает или оценивает психологические тексты, люди размечали те же единицы по той же схеме, есть цифры согласия |
{reasons}
| `?` | пока не решил (до закрытия файла нужно решить) |

Цифры согласия ИИ брал из текста, но выписываться они будут на следующем этапе по оригиналу — здесь решаем только «подходит / нет» и причину. Если подходит, проверьте тип задачи (T1 кодбук, T2 подсчёт методики, T3 клиническая оценка, T4 LLM-судья) — его можно дописать заметкой.
"""


def one_line(t: str) -> str:
    return re.sub(r"\s+", " ", t or "").strip()


def block(n: int, rid: str, rec: dict, ret: dict, prop: dict) -> str:
    c = prop["codes"]
    code = "+" if c["decision"] == "eligible" else ("?" if c["decision"] == "unclear" else AI_TO_CODE.get(c["reason"], "-7"))
    links = ([f"[PDF](../pdf/{rid}.pdf)"] if (HERE / "pdf" / f"{rid}.pdf").exists() else []) + [f"[текст](../text/{rid}.txt)"]
    if ret.get("url"):
        links.append(f"[онлайн]({ret['url']})")
    lines = ["---", "", f"### {n} · {rid}", "", f"**{one_line(rec['title'])}**", "",
             " · ".join(x for x in [str(rec.get('year') or ''), one_line(rec.get('venue')), ret.get('source', '')] if x), "",
             "Открыть: " + " · ".join(links), "",
             f"**ИИ предлагает:** {code} · {c['decision']} · {c['reason']} · {c['task_type']} · {MODEL_RU.get(prop.get('judge', {}).get('model_requested', ''), '')}", "",
             f"- Конструкт: {one_line(c['construct'])}", f"- Тексты: {one_line(c['texts'])}",
             f"- Модели: {one_line(c['models'])}", f"- Эталон (люди): {one_line(c['human_reference'])}",
             f"- Согласие людей между собой: {one_line(c['human_human_agreement'])}"]
    for d in c["agreement_stats"]:
        lines.append(f"- {one_line(d['model'])} ({one_line(d['configuration'])}): {d['statistic']} = {d['value']} "
                     f"[n = {d['n_units']}]; {d['location']}: «{one_line(d['quote'])}»")
    if one_line(c["possible_duplicate"]):
        lines.append(f"- Возможный дубль: {one_line(c['possible_duplicate'])}")
    if one_line(c["note"]):
        lines.append(f"- Заметка ИИ: {one_line(c['note'])}")
    lines += ["", "**Решение:** ", ""]
    return "\n".join(lines)


def make(a) -> None:
    recs = {json.loads(l)["rec_id"]: json.loads(l) for l in
            (PAPER / "search" / "runs" / a.run / "records_unique.jsonl").open(encoding="utf-8")}
    ret = {r["rec_id"]: r for r in csv.DictReader((HERE / "retrieval_log.csv").open(encoding="utf-8-sig"))}
    props = {}   # several runs (D5: Opus first, then Sonnet); a report keeps its first proposal
    for name in a.name:
        for l in (HERE / "llm" / f"{name}.jsonl").open(encoding="utf-8"):
            if l.strip():
                props.setdefault(json.loads(l)["conv_id"], json.loads(l))
    ids = sorted(props)
    out_dir = HERE / "decisions"
    out_dir.mkdir(exist_ok=True)
    reasons = "\n".join(f"| `-{d}` | не подходит: {t} |" for d, (_, t) in REASONS.items())
    for part, start in enumerate(range(0, len(ids), FILE_SIZE), a.first_part):
        chunk = ids[start:start + FILE_SIZE]
        path = out_dir / f"ft_{a.screener}_{part:02d}.md"
        if path.exists() and not a.force:
            sys.exit(f"{path} exists; refusing to overwrite R1's work")
        blocks = [block(start + i, rid, recs[rid], ret[rid], props[rid]) for i, rid in enumerate(chunk, 1)]
        head = (f"# Полные тексты, часть {part}\n\nОтчёты {start + 1}–{start + len(chunk)} из {len(ids)}. "
                f"Предложение ИИ — черновик, решаете вы.\n\n{GUIDE.format(reasons=reasons)}\n")
        path.write_text(head + "\n".join(blocks), encoding="utf-8", newline="\n")
        print(f"{path}  ({len(chunk)} reports)")


def parse_code(raw: str) -> tuple[str, str, str, str]:
    text = raw.strip().replace("−", "-").replace("–", "-").replace("—", "-")
    text = re.sub(r"^-\s+(\d)", r"-\1", text)
    if not text:
        return "", "", "", ""
    head, _, note = text.partition(" ")
    if head == "+":
        return head, "eligible", "", note.strip()
    if head == "?":
        return head, "undecided", "", note.strip()
    if head == "=":
        return head, "agree", "", note.strip()
    m = re.fullmatch(r"-([1-9])", head)
    if m:
        return head, "not_eligible", REASONS[m.group(1)][0], note.strip()
    return head, "", "", text


def parse(a) -> None:
    rows, problems = [], []
    for f in a.files:
        lines = [x.strip() for x in Path(f).read_text(encoding="utf-8").splitlines()]
        cur = None
        for i, line in enumerate(lines):
            h = HEADER_RE.match(line)
            if h:
                cur = {"file": Path(f).name, "k": int(h.group(1)), "rec_id": h.group(2), "ai_code": ""}
                continue
            if cur is None:
                continue
            m = AI_RE.match(line)
            if m:
                cur["ai_code"] = m.group(1)
                continue
            d = DECISION_RE.match(line)
            if d:
                raw = d.group(1)
                if not raw.strip():
                    nxt = next((x for x in lines[i + 1:] if x), "")
                    if nxt and not nxt.startswith("---") and not HEADER_RE.match(nxt):
                        raw = nxt
                code, decision, reason, note = parse_code(raw)
                if decision == "agree":
                    ai = cur["ai_code"]
                    _, decision, reason, _ = parse_code(ai) if ai else ("", "", "", "")
                    code = f"={ai}"
                    if decision == "undecided":
                        problems.append(f"{cur['rec_id']}: '=' but the AI proposal is unclear — choose a code")
                if not code:
                    problems.append(f"{cur['rec_id']}: no decision")
                elif not decision:
                    problems.append(f"{cur['rec_id']}: cannot read the code {code!r}")
                elif decision == "undecided":
                    problems.append(f"{cur['rec_id']}: still undecided ('?')")
                rows.append({**cur, "code": code, "decision": decision, "reason": reason, "note": note})
                cur = None
    if a.out:
        with Path(a.out).open("w", encoding="utf-8-sig", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["rec_id", "k", "file", "code", "decision", "reason", "note", "ai_code"])
            w.writeheader()
            w.writerows(rows)
    counts = {k: sum(1 for r in rows if r["decision"] == k) for k in ("eligible", "not_eligible", "undecided", "")}
    print(f"{len(rows)} reports: eligible {counts['eligible']}, not eligible {counts['not_eligible']}, "
          f"undecided {counts['undecided']}, no code {counts['']}")
    for p in problems[:40]:
        print("  " + p)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make")
    m.add_argument("--run", required=True)
    m.add_argument("--name", required=True, nargs="+", help="one or more fulltext/llm/<name>.jsonl runs")
    m.add_argument("--screener", default="R1")
    m.add_argument("--force", action="store_true")
    m.add_argument("--first-part", type=int, default=1, help="number of the first file (continue a series)")
    p = sub.add_parser("parse")
    p.add_argument("files", nargs="+")
    p.add_argument("--out")
    a = ap.parse_args()
    make(a) if a.cmd == "make" else parse(a)


if __name__ == "__main__":
    main()
