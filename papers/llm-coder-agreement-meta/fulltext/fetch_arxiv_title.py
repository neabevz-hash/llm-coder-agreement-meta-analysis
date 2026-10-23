"""Second retrieval step: arXiv versions of reports that fetch_oa.py could not retrieve (protocol §11b lists arXiv
among the open-access sources).

Many conference and journal papers on LLMs have an arXiv version without a DOI link to the published one. For every
report still "not retrieved" in retrieval_log.csv, the arXiv API is searched by title; a hit counts when the
normalised titles match (difflib ratio >= 0.93) and the arXiv year is within two years of the record's year. The PDF
is downloaded from arxiv.org and stored like the other texts; the log row records the arXiv id and the match ratio.
One query every 3 seconds (arXiv API terms).

Run: .venv/Scripts/python.exe -I papers/llm-coder-agreement-meta/fulltext/fetch_arxiv_title.py --run 2026-10-21
"""
from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import json
import re
import sys
import time
from pathlib import Path

from lxml import etree

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fetch_oa as oa  # noqa: E402  (shares the HTTP client, PDF and logging helpers)

ATOM = {"a": "http://www.w3.org/2005/Atom"}
MIN_RATIO, MAX_YEAR_GAP = 0.93, 2
STOP = {"the", "and", "for", "with", "via", "from", "into", "using", "are", "can", "does", "its", "their", "our", "how", "what", "not", "but", "than", "that", "this", "these", "who", "why", "when"}



def plain(t: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", (t or "").lower()).split())


def search(title: str) -> list[dict]:
    words = [w for w in plain(title).split() if len(w) > 2 and w not in STOP][:12]
    if len(words) < 3:
        return []
    q = "ti:" + " AND ti:".join(words)
    r = oa.get("http://export.arxiv.org/api/query", params={"search_query": q, "max_results": 5})
    if r is None or r.status_code != 200:
        return []
    root = etree.fromstring(r.content)
    out = []
    for e in root.findall("a:entry", ATOM):
        aid = e.findtext("a:id", default="", namespaces=ATOM).rsplit("/abs/", 1)[-1]
        out.append({"id": aid, "title": " ".join(e.findtext("a:title", default="", namespaces=ATOM).split()),
                    "year": int(e.findtext("a:published", default="0000", namespaces=ATOM)[:4] or 0)})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--limit", type=int)
    a = ap.parse_args()
    recs = {json.loads(l)["rec_id"]: json.loads(l) for l in
            (oa.PAPER / "search" / "runs" / a.run / "records_unique.jsonl").open(encoding="utf-8")}
    rows = {r["rec_id"]: r for r in csv.DictReader(oa.LOG.open(encoding="utf-8-sig"))}
    todo = sorted(rid for rid, r in rows.items() if r["status"] != "retrieved")
    if a.limit:
        todo = todo[:a.limit]
    print(f"{len(todo)} reports not retrieved; searching arXiv by title", flush=True)
    got = 0
    for n, rid in enumerate(todo, 1):
        rec = recs[rid]
        note = "arxiv-title:no match"
        try:
            year = int(rec.get("year") or 0)
            hits = search(rec["title"])
            best = max(hits, key=lambda h: difflib.SequenceMatcher(None, plain(h["title"]), plain(rec["title"])).ratio(), default=None)
            if best:
                ratio = difflib.SequenceMatcher(None, plain(best["title"]), plain(rec["title"])).ratio()
                if ratio >= MIN_RATIO and (not year or abs(best["year"] - year) <= MAX_YEAR_GAP):
                    url = f"https://arxiv.org/pdf/{best['id']}"
                    data, how = oa.fetch_pdf(url)
                    if data:
                        text, pages = oa.pdf_to_text(data)
                        if len(text) > 1500:
                            at = oa.utcnow()
                            header = f"REC_ID: {rid}\nSOURCE: arxiv_title\nURL: {url}\nRETRIEVED_UTC: {at}\n\n"
                            (oa.TEXT / f"{rid}.txt").write_text(header + text, encoding="utf-8")
                            (oa.PDF / f"{rid}.pdf").write_bytes(data)
                            rows[rid].update(status="retrieved", source="arxiv_title", url=url, chars=len(text), pages=pages,
                                             sha256=hashlib.sha256(data).hexdigest(), at_utc=at)
                            note = f"arxiv-title:{best['id']} (ratio {ratio:.3f})"
                            got += 1
                        else:
                            note = f"arxiv-title:{best['id']} pdf without text"
                    else:
                        note = f"arxiv-title:{best['id']} {how}"
                else:
                    note = f"arxiv-title:closest {best['id']} ratio {ratio:.3f}, year {best['year']}"
        except Exception as e:  # noqa: BLE001 - one failed record must not stop the run
            note = f"arxiv-title:error {type(e).__name__}"
        rows[rid]["tried"] = (rows[rid]["tried"] + " | " + note).strip(" |")
        with oa.LOG.open("w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=oa.LOG_FIELDS)
            w.writeheader()
            w.writerows(rows[k] for k in sorted(rows))
        print(f"[{n}/{len(todo)}] {rid} {note}", flush=True)
        time.sleep(3)
    total = sum(1 for r in rows.values() if r["status"] == "retrieved")
    print(f"arXiv by title: {got} more; retrieved {total} of {len(rows)}", flush=True)


if __name__ == "__main__":
    main()
