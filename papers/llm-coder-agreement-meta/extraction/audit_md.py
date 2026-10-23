"""R1's check of the AI coding (deviations.md, D8): every study in one Markdown file to read.

For each study: title and links to the full text, the tasks with their codes, the included LLM-human values (model,
prompting, reference, statistic, value, location, quote, whether the script found the value in the text), the values
the AI excluded and why, the human-human values and the five risk-of-bias ratings. R1 reads and writes back only where
he disagrees.

Run: .venv/Scripts/python.exe -I papers/llm-coder-agreement-meta/extraction/audit_md.py
"""
from __future__ import annotations

import csv
import random
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
FORMS = PAPER / "forms"
N, SEED = 30, 20261023
ROB = {1: "отбор единиц", 2: "конфигурация LLM", 3: "эталон (люди)", 4: "утечка данных в обучение", 5: "отчётность"}


def rows(name: str) -> list[dict]:
    return list(csv.DictReader((FORMS / name).open(encoding="utf-8")))


def main():
    studies = {s["study_id"]: s for s in rows("studies.csv")}
    tasks, est, hr = defaultdict(list), defaultdict(list), defaultdict(list)
    for t in rows("tasks.csv"):
        tasks[t["study_id"]].append(t)
    for e in rows("estimates.csv"):
        est[e["study_id"]].append(e)
    for h in rows("human_reliability.csv"):
        hr[h["study_id"]].append(h)
    sample = sorted(studies)
    out = [f"# Проверка разметки ИИ: все {len(studies)} исследований\n",
           "Ничего заполнять не нужно. Прочитайте и напишите Claude, где не согласны (номер исследования и что не так), "
           "или «везде ок».\n",
           "Что смотреть в первую очередь: тип задачи (T1 кодбук, T2 подсчёт методики, T3 клиническая оценка, T4 "
           "LLM-судья); эталон и кто размечал; включённые цифры — те ли это значения согласия LLM с людьми; правильно ли "
           "отсеяны лишние; риск смещения.\n",
           "«в тексте: да» — скрипт нашёл это число в тексте статьи.\n"]
    for i, sid in enumerate(sample, 1):
        s = studies[sid]
        main = s["main_report"]
        links = [f"[PDF](../../fulltext/pdf/{main}.pdf)" if (PAPER / "fulltext" / "pdf" / f"{main}.pdf").exists() else "",
                 f"[текст](../../fulltext/text/{main}.txt)",
                 f"[онлайн](https://doi.org/{s['doi']})" if s["doi"] else ""]
        out.append(f"---\n\n## {i}. {sid} · {s['first_author']} {s['year']}\n\n**{s['title']}**\n\n"
                   f"Отчёты: {s['report_ids']} · {' · '.join(x for x in links if x)}\n\n"
                   f"Публикация: {s['pub_status']}; область: {s['field']}; все конфигурации показаны: "
                   f"{s['all_configs_reported']}; подбор на тех же данных: {s['tuned_on_eval']}\n")
        if s["scope"]:
            out.append(f"Что выписывали: {s['scope']}\n")
        out.append("**Задачи**\n")
        for t in tasks[sid]:
            out.append(f"- **{t['task_id']}. {t['label']}** — {t['task_type']}, {t['construct_type']}; категорий: "
                       f"{t['n_categories']}; единиц: {t['n_units']} ({t['unit']}); тексты: {t['text_type']}, "
                       f"{t['text_source']}, язык {t['language']}; датасет: {t['dataset']} ({t['dataset_public']}); "
                       f"люди: {t['human_coders_n']}, {t['human_expertise']}, независимо: {t['human_independent']}; "
                       f"эталон: {t['reference_type']}")
        inc = [e for e in est[sid] if e["include"] == "yes"]
        exc = [e for e in est[sid] if e["include"] != "yes"]
        out.append(f"\n**Включённые цифры ({len(inc)})**\n")
        for e in inc:
            found = "да" if e["value_in_text"] == "True" else "**нет**"
            out.append(f"- {e['task_id']} · {e['model_name']} · {e['configuration'][:80]} · {e['prompting']} · эталон {e['reference']} · "
                       f"**{e['statistic']} = {e['value_raw']}** (n {e['n_units']}) · {e['location']} · в тексте: {found}"
                       f"  \n  «{e['quote']}»")
        if exc:
            out.append(f"\n**Отсеяно ИИ ({len(exc)})**\n")
            for e in exc:
                out.append(f"- {e['model_name']} · {e['statistic']} = {e['value_raw']} — {e['exclude_reason']}")
        out.append(f"\n**Согласие людей между собой ({len(hr[sid])})**\n")
        for h in hr[sid] or []:
            out.append(f"- {h['task_id']} · {h['comparison']} · {h['statistic']} = {h['value_raw']} (n {h['n_units']}; "
                       f"те же единицы: {h['same_units']}) · {h['location']}")
        if not hr[sid]:
            out.append("- нет")
        out.append("\n**Риск смещения**\n")
        for k in range(1, 6):
            out.append(f"- {k}. {ROB[k]}: **{s[f'rob_{k}']}** — {s[f'rob_{k}_reason']}")
        out.append("")
    path = HERE / "verify" / "audit_R1_all.md"
    path.parent.mkdir(exist_ok=True)
    path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
    print(f"{path} ({len(sample)} studies)")


if __name__ == "__main__":
    main()
