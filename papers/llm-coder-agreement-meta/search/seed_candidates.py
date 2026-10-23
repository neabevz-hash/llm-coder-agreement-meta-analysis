"""Кандидаты в эталонный набор (seed set) для проверки полноты поиска.

Источник — списки литературы независимых синтезов (`seed_sources_refs.json`):
- OpenAlex `referenced_works` — Gierbolini-Rivera 2026, Hua 2025, Kempny 2026, Na 2025;
- Semantic Scholar `references` — Seyler 2025, Na 2025 (arXiv), Li L. 2026, Flathers 2026, Li C. 2026, Hua 2024 (arXiv).

Ссылки склеиваются по DOI, arXiv ID и названию, дополняются аннотациями из OpenAlex и помечаются признаками:
LLM, сравнение с людьми, психологический или клинический конструкт. Выход — `seed_candidates.csv`
для ручного отбора: Claude готовит черновик решения по §8 протокола, автор решает.

Запуск: .venv/Scripts/python.exe papers/llm-coder-agreement-meta/search/seed_candidates.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
import time
from pathlib import Path

import httpx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ENV = dict(l.split("=", 1) for l in (ROOT / ".env").read_text(encoding="utf-8").splitlines() if "=" in l and not l.startswith("#"))
KEY = ENV["OPENALEX_API_KEY"].strip()
client = httpx.Client(timeout=90, headers={"User-Agent": "llm-coder-agreement-seed/0.1 (mailto:mrexert@gmail.com)"})

LLM = re.compile(r"\b(large language models?|LLMs?|ChatGPT|GPT-?[345](\.\d)?o?|generative (AI|artificial intelligence|pre-?trained)|"
                 r"Claude|Gemini|Llama|Mistral|Qwen|DeepSeek|foundation models?)\b", re.I)
HUMAN = re.compile(r"(inter-?rater|inter-?coder|inter-?annotator|kappa|krippendorff|gwet|intraclass|\bICC\b|agreement|concordan|"
                   r"human (coders?|raters?|annotators?|experts?|evaluators?|judg|labels?|annotations?|coding|ratings?)|"
                   r"expert[- ](annotat|rat|cod|label|judg)|clinician[- ]?(rat|judg|annotat)|manual(ly)? (cod|annotat|label)|"
                   r"gold standard|as[- ]a[- ]judge|LLM[- ]judges?|automated (cod|scor)|automatic scoring)", re.I)
PSY = re.compile(r"(psycholog|psychiatr|psychotherap|counsel|mental health|depress|anxiety|suicid|self-?harm|trauma|PTSD|emotion|"
                 r"affect|personality|empathy|well-?being|motivational interviewing|therapist|therapeutic|crisis|distress|loneliness|"
                 r"eating disorder|substance use|addiction|psychosis|schizophren|bipolar|autism|ADHD|attachment|mentaliz|"
                 r"reflective functioning|cognitive distortion|defen[cs]e mechanism|projective|rorschach|sentence completion|"
                 r"narrative|qualitative|interview|open-?ended|divergent thinking)", re.I)


def norm(t: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def inv(i: dict | None) -> str:
    if not i:
        return ""
    pos = {p: w for w, ps in i.items() for p in ps}
    return " ".join(pos[k] for k in sorted(pos))


def openalex_batch(ids: list[str]) -> list[dict]:
    out = []
    for i in range(0, len(ids), 50):
        chunk = [x.rsplit("/", 1)[-1] for x in ids[i:i + 50]]
        r = client.get("https://api.openalex.org/works", params={"filter": "openalex_id:" + "|".join(chunk), "per_page": 50, "api_key": KEY})
        r.raise_for_status()
        out += r.json()["results"]
        time.sleep(0.3)
    return out


def main():
    src = json.loads((HERE / "seed_sources_refs.json").read_text(encoding="utf-8"))
    recs: dict[str, dict] = {}

    def add(key, rec, source):
        if key in recs:
            recs[key]["sources"].add(source)
            if len(rec.get("abstract") or "") > len(recs[key].get("abstract") or ""):
                recs[key]["abstract"] = rec["abstract"]
        else:
            rec["sources"] = {source}
            recs[key] = rec

    for source, ids in src.get("openalex", {}).items():
        for w in openalex_batch(ids):
            doi = (w.get("doi") or "").replace("https://doi.org/", "").lower()
            rec = {"title": w.get("title") or "", "year": w.get("publication_year"), "doi": doi, "arxiv": "",
                   "abstract": inv(w.get("abstract_inverted_index"))}
            add(doi or norm(rec["title"]), rec, source)
    for source, refs in src.get("s2", {}).items():
        for p in refs:
            ext = p.get("externalIds") or {}
            doi = (ext.get("DOI") or "").lower()
            ax = ext.get("ArXiv") or ""
            if not doi and ax:
                doi = f"10.48550/arxiv.{ax}"
            rec = {"title": p.get("title") or "", "year": p.get("year"), "doi": doi, "arxiv": ax, "abstract": p.get("abstract") or ""}
            add(doi or norm(rec["title"]), rec, source)

    # включённые исследования Seyler et al. 2025: DOI найдены по списку литературы PDF через Crossref
    # (seyler2025_included.json); совпадения с низким score (< 75) у [40] и [50] — чужие работы, не берём
    sey = HERE / "seyler2025_included.json"
    if sey.exists():
        for it in json.loads(sey.read_text(encoding="utf-8")):
            if not it["doi"] or (it["score"] is not None and it["score"] < 75):
                continue
            q = httpx.get(f"https://api.openalex.org/works/doi:{it['doi']}", params={"api_key": KEY}, timeout=60)
            if q.status_code != 200:
                rec = {"title": it.get("cr_title") or it["ref"], "year": None, "doi": it["doi"], "arxiv": "", "abstract": ""}
            else:
                w = q.json()
                rec = {"title": w.get("title") or "", "year": w.get("publication_year"), "doi": it["doi"], "arxiv": "",
                       "abstract": inv(w.get("abstract_inverted_index"))}
            add(it["doi"], rec, "Seyler2025")
            time.sleep(0.15)

    # аннотации из OpenAlex для записей без аннотации
    missing = [r for r in recs.values() if not r["abstract"] and r["doi"]]
    for r in missing:
        q = httpx.get(f"https://api.openalex.org/works/doi:{r['doi']}", params={"api_key": KEY}, timeout=60)
        if q.status_code == 200:
            r["abstract"] = inv(q.json().get("abstract_inverted_index"))
        time.sleep(0.15)

    rows = []
    for r in recs.values():
        ta = f"{r['title']} {r['abstract']}"
        llm, hum, psy = bool(LLM.search(ta)), bool(HUMAN.search(ta)), bool(PSY.search(ta))
        rows.append({"flag": int(llm) + int(hum) + int(psy), "llm": int(llm), "human": int(hum), "psy": int(psy),
                     "year": r["year"], "title": r["title"], "doi": r["doi"], "arxiv": r["arxiv"],
                     "sources": ";".join(sorted(r["sources"])), "abstract": (r["abstract"] or "")[:1500],
                     "ai_draft": "", "r1_decision": "", "note": ""})
    rows.sort(key=lambda x: (-x["flag"], str(x["year"])))
    with (HERE / "seed_candidates.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"references: {len(rows)}; all three flags: {sum(r['flag'] == 3 for r in rows)}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
