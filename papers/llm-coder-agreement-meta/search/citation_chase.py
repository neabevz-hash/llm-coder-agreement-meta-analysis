"""Backward and forward citation searching of the included reports and the syntheses (protocol §9; deviations.md, D6).

Seeds: every report R1 judged eligible at full text, and the syntheses named in protocol §9 (Seyler et al., 2025;
Li, L., et al., 2026; Hua et al., 2025; Na et al., 2025; Flathers et al., 2026) plus the two other seed-set sources
(Gierbolini-Rivera et al., 2026; Kempny et al., 2026). Through OpenAlex (API key OPENALEX_API_KEY in .env):
  backward - every work in the seeds' reference lists (referenced_works);
  forward  - every work citing a seed (filter cites:).
Seeds whose OpenAlex record has no reference list (mostly arXiv and ACL papers) get their references from Semantic
Scholar (by DOI or arXiv ID), and seeds missing from OpenAlex get their citing works from Semantic Scholar (D6).

The works are compared with every unique record of the main search (DOI, OpenAlex ID, normalised title). New records go
through the main search's automatic rules: publication year from 2020 (I6), non-study record types, and rule 6 (an exact
arm-A or arm-B match in title or abstract, or no abstract and an LLM term in the title; search.matches_all). Records that
pass go to the AI screening passes (`chase_records.py`).

Writes search/runs/<date>-citations/: seeds.jsonl (OpenAlex works of the seeds, with authorships), raw_backward.jsonl,
raw_forward.jsonl, records_new.jsonl (new records with `auto_removed`) and chase_log.json.
Template: papers/ai-dependence-correlates/search/citation_chase.py.
Run: .venv/Scripts/python.exe -I papers/llm-coder-agreement-meta/search/citation_chase.py --run 2026-10-21
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
sys.path.insert(0, str(HERE))

import search as S  # noqa: E402  (helpers: get, ENV, inv_to_text, norm_doi, matches_all, RX1, DASHES)
from dedup import NON_STUDY, doi_key, norm_title  # noqa: E402

REVIEWS = {  # protocol §9, then the two other seed-set sources (§9 "Seed set"; D6)
    "Seyler et al. 2025": "10.31234/osf.io/gnx8p_v1",
    "Li, L., et al. 2026": "10.48550/arxiv.2605.25273",
    "Hua et al. 2025": "10.1038/s41746-025-01611-4",
    "Na et al. 2025": "10.18653/v1/2025.findings-acl.385",
    "Flathers et al. 2026": "10.31234/osf.io/fahuk_v1",
    "Gierbolini-Rivera et al. 2026": "10.2196/98551",
    "Kempny et al. 2026": "10.1186/s12874-026-02913-1",
}
SELECT = ("id,doi,title,publication_year,type,primary_location,abstract_inverted_index,authorships,ids,language,"
          "cited_by_count")
S2_FIELDS = "externalIds,title,abstract,year,venue,authors,publicationTypes"
ARXIV_DOI = re.compile(r"^10\.48550/arxiv\.(.+)$", re.I)


def oa(params: dict) -> dict:
    return S.get("https://api.openalex.org/works", {**params, "api_key": S.ENV["OPENALEX_API_KEY"]}).json()


def oa_filter_all(flt: str, select: str) -> list[dict]:
    out, cursor = [], "*"
    while cursor:
        d = oa({"filter": flt, "per_page": 200, "cursor": cursor, "select": select})
        out.extend(d["results"])
        cursor = d["meta"].get("next_cursor") if d["results"] else None
    return out


def oa_ids(r: dict) -> list[str]:
    """OpenAlex IDs among a main-search record's source IDs (stored as https://openalex.org/W...)."""
    return [p.rsplit("/", 1)[-1] for p in (r.get("source_ids") or "").split(";") if re.search(r"openalex\.org/W\d+$", p)]


def wid(w: dict) -> str:
    return w["id"].rsplit("/", 1)[-1]


def oa_rec(w: dict, source: str) -> dict:
    loc = w.get("primary_location") or {}
    auth = w.get("authorships") or []
    return S.rec(source, wid(w), pmid=((w.get("ids") or {}).get("pmid") or "").rsplit("/", 1)[-1], doi=w.get("doi"),
                 title=w.get("title"), abstract=S.inv_to_text(w.get("abstract_inverted_index")),
                 year=w.get("publication_year"), venue=(loc.get("source") or {}).get("display_name") or "",
                 first_author=((auth[0].get("author") or {}).get("display_name") or "") if auth else "",
                 type=w.get("type") or "", language=w.get("language") or "")


def s2_batch(ids: list[str], kind: str) -> dict[str, list[dict] | None]:
    """Reference or citation lists from the Semantic Scholar batch endpoint, 20 papers per request.
    kind = references | citations. Value None: the paper is not in Semantic Scholar. The public pool answers 429 often;
    the request waits and retries (up to 30 times) instead of counting the paper as missing."""
    fields = ",".join(f"{kind}.{f}" for f in ["paperId", *S2_FIELDS.split(",")])
    out: dict[str, list[dict] | None] = {}
    for i in range(0, len(ids), 20):
        chunk = ids[i:i + 20]
        for attempt in range(30):
            try:
                r = S.client.post("https://api.semanticscholar.org/graph/v1/paper/batch", params={"fields": fields},
                                  json={"ids": chunk})
            except Exception:  # noqa: BLE001 - transport error, retry
                time.sleep(20)
                continue
            if r.status_code == 200:
                break
            time.sleep(20 + 10 * min(attempt, 6))
        else:
            raise RuntimeError(f"Semantic Scholar batch failed for {chunk[0]}...")
        for pid, p in zip(chunk, r.json()):
            out[pid] = None if p is None else [x for x in (p.get(kind) or []) if x and x.get("paperId")]
        time.sleep(3)
    return out


def s2_id(dois: list[str]) -> str | None:
    for d in dois:
        m = ARXIV_DOI.match(d)
        if m:
            return f"ARXIV:{m.group(1)}"
    return f"DOI:{dois[0]}" if dois else None


def s2_rec(p: dict, source: str) -> dict:
    ext = p.get("externalIds") or {}
    doi = ext.get("DOI") or (f"10.48550/arxiv.{ext['ArXiv']}" if ext.get("ArXiv") else "")
    return S.rec(source, f"S2:{p.get('paperId')}", pmid=str(ext.get("PubMed") or ""), doi=doi, title=p.get("title"),
                 abstract=p.get("abstract"), year=p.get("year"), venue=p.get("venue"),
                 first_author=((p.get("authors") or [{}])[0] or {}).get("name", "") if p.get("authors") else "",
                 type=";".join(p.get("publicationTypes") or []))


def resolve_seeds(recs: dict[str, dict], elig: list[str]) -> tuple[dict[str, dict], list[str]]:
    """OpenAlex work per seed: by OpenAlex ID, then by any DOI, then by exact normalised title."""
    sel = SELECT + ",referenced_works"
    seeds: dict[str, dict] = {}
    want_w = {k: oa_ids(recs[k]) for k in elig}
    by_w: dict[str, str] = {w[0]: k for k, w in want_w.items() if w}
    ids = sorted(by_w)
    for i in range(0, len(ids), 50):
        for w in oa({"filter": "ids.openalex:" + "|".join(ids[i:i + 50]), "per_page": 50, "select": sel})["results"]:
            if wid(w) in by_w:
                seeds[by_w[wid(w)]] = w
    dois = {k: [d for d in (recs[k].get("all_dois") or recs[k].get("doi") or "").split(";") if d] for k in elig}
    todo = [k for k in elig if k not in seeds and dois[k]]
    by_doi = {doi_key(d): k for k in todo for d in dois[k]}
    keys = sorted(by_doi)
    for i in range(0, len(keys), 40):
        chunk = [d for d in keys[i:i + 40] if "|" not in d and "," not in d]
        if not chunk:
            continue
        for w in oa({"filter": "doi:" + "|".join(chunk), "per_page": 50, "select": sel})["results"]:
            k = by_doi.get(doi_key(w.get("doi") or ""))
            if k and k not in seeds:
                seeds[k] = w
    for k in [k for k in elig if k not in seeds]:
        t = norm_title(recs[k].get("title") or "")
        if len(t) < 25:
            continue
        q = " ".join(re.sub(r"[^\w\s-]", " ", recs[k]["title"]).split())[:200]
        try:
            hits = oa({"filter": f"title.search:{q}", "per_page": 10, "select": sel})["results"]
        except Exception:  # noqa: BLE001 - title the search API rejects
            continue
        for w in hits:
            if norm_title(w.get("title") or "") == t:
                seeds[k] = w
                break
    for label, doi in REVIEWS.items():
        d = oa({"filter": f"doi:{doi}", "per_page": 5, "select": sel})["results"]
        if d:
            seeds[label] = d[0]
    not_found = [k for k in [*elig, *REVIEWS] if k not in seeds]
    return seeds, not_found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="the main search run (records_unique.jsonl)")
    ap.add_argument("--date", default=date.today().isoformat())
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    run = HERE / "runs" / f"{a.date}-citations"
    run.mkdir(parents=True, exist_ok=True)
    main_recs = [json.loads(l) for l in (HERE / "runs" / a.run / "records_unique.jsonl").open(encoding="utf-8")]
    recs = {r["rec_id"]: r for r in main_recs}
    known_doi = {doi_key(d) for r in main_recs for d in (r.get("all_dois") or r.get("doi") or "").split(";") if d}
    known_w = {w for r in main_recs for w in oa_ids(r)}
    known_t = {norm_title(r["title"]) for r in main_recs if r.get("title")}
    elig = [r["rec_id"] for r in csv.DictReader((PAPER / "fulltext" / "decisions" / "ft_R1.csv").open(encoding="utf-8-sig"))
            if r["decision"] == "eligible"]

    if (run / "seeds.jsonl").exists():   # resumed run: the seeds were resolved already
        seeds = {d.pop("seed"): d for d in (json.loads(l) for l in (run / "seeds.jsonl").open(encoding="utf-8"))}
        not_found = [k for k in [*elig, *REVIEWS] if k not in seeds]
    else:
        seeds, not_found = resolve_seeds(recs, elig)
        with (run / "seeds.jsonl").open("w", encoding="utf-8", newline="\n") as f:
            for k, w in seeds.items():
                f.write(json.dumps({"seed": k, **w}, ensure_ascii=False) + "\n")
    print(f"seeds in OpenAlex: {len(seeds)}; not found: {len(not_found)}", flush=True)

    # backward: OpenAlex reference lists; Semantic Scholar for seeds without one (D6)
    ref_ids = sorted({x.rsplit("/", 1)[-1] for w in seeds.values() for x in (w.get("referenced_works") or [])})
    backward = []
    for i in range(0, len(ref_ids), 50):
        for w in oa({"filter": "ids.openalex:" + "|".join(ref_ids[i:i + 50]), "per_page": 50, "select": SELECT})["results"]:
            backward.append(oa_rec(w, "chase_backward"))
    no_refs = [k for k in [*elig, *REVIEWS] if not (seeds.get(k) or {}).get("referenced_works")]
    pid_of = {}
    for k in no_refs:
        dois = [REVIEWS[k]] if k in REVIEWS else [d for d in (recs[k].get("all_dois") or recs[k].get("doi") or "").split(";") if d]
        if s2_id(dois):
            pid_of[k] = s2_id(dois)
    lists = s2_batch(sorted(set(pid_of.values())), "references")
    s2_back_ok, s2_back_missing = 0, [k for k in no_refs if k not in pid_of]
    for k, pid in pid_of.items():
        refs = lists.get(pid)
        if not refs:
            s2_back_missing.append(k)
            continue
        s2_back_ok += 1
        backward += [s2_rec(p, "chase_backward_s2") for p in refs]
    print(f"backward: {len(ref_ids)} OpenAlex references; Semantic Scholar for {s2_back_ok} of {len(no_refs)} seeds "
          f"without an OpenAlex reference list", flush=True)

    # forward: OpenAlex cites: (50 seeds per filter); Semantic Scholar for seeds missing from OpenAlex (D6)
    seed_w = sorted({wid(w) for w in seeds.values()})
    forward = []
    for i in range(0, len(seed_w), 50):
        forward += [oa_rec(w, "chase_forward") for w in oa_filter_all("cites:" + "|".join(seed_w[i:i + 50]), SELECT)]
    pid_f = {k: s2_id([d for d in (recs[k].get("all_dois") or recs[k].get("doi") or "").split(";") if d])
             for k in elig if k not in seeds}
    pid_f = {k: v for k, v in pid_f.items() if v}
    cits = s2_batch(sorted(set(pid_f.values())), "citations")
    s2_fwd_ok = 0
    for k, pid in pid_f.items():
        if cits.get(pid) is not None:
            s2_fwd_ok += 1
            forward += [s2_rec(p, "chase_forward_s2") for p in cits[pid]]
    print(f"forward: {len(forward)} citing links", flush=True)

    for name, rows in (("raw_backward.jsonl", backward), ("raw_forward.jsonl", forward)):
        with (run / name).open("w", encoding="utf-8", newline="\n") as f:
            for x in rows:
                f.write(json.dumps(x, ensure_ascii=False) + "\n")

    new, seen_doi, seen_t, known_hits = [], set(), set(), {"chase_backward": 0, "chase_forward": 0}
    for x in [*backward, *forward]:
        t = norm_title(x["title"])
        dk = doi_key(x["doi"]) if x["doi"] else ""
        side = "chase_backward" if "backward" in x["source"] else "chase_forward"
        if x["source_id"] in known_w or (dk and dk in known_doi) or (t and t in known_t):
            known_hits[side] += 1
            continue
        if (dk and dk in seen_doi) or (t and t in seen_t) or not t:
            continue
        seen_doi.add(dk)
        seen_t.add(t)
        try:
            year = int(x["year"])
        except (TypeError, ValueError):
            year = 0
        text = DASH(f"{x['title']} {x['abstract']}")
        if year and year < S.FROM_YEAR:
            x["auto_removed"] = "before 2020"
        elif x["type"] and all(NON_STUDY.search(t) for t in x["type"].split(";")):
            x["auto_removed"] = "non-study record type"
        elif not (S.matches_all(text) or (len(x["abstract"]) < 50 and S.RX1.search(DASH(x["title"])))):
            x["auto_removed"] = "no exact search-term match"
        else:
            x["auto_removed"] = ""
        new.append(x)
    with (run / "records_new.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for r in new:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    log = {
        "run_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "main_run": a.run,
        "seeds": {"eligible_reports": len(elig), "syntheses": list(REVIEWS), "found_in_openalex": len(seeds),
                  "not_found_in_openalex": not_found},
        "backward": {"openalex_reference_ids": len(ref_ids), "seeds_without_openalex_references": len(no_refs),
                     "semantic_scholar_reference_lists": s2_back_ok, "no_reference_list_anywhere": s2_back_missing,
                     "works": len(backward), "already_in_main_search": known_hits["chase_backward"]},
        "forward": {"citing_links": len(forward), "semantic_scholar_citation_lists": s2_fwd_ok,
                    "already_in_main_search": known_hits["chase_forward"]},
        "new_unique_records": len(new),
        "auto_removed": {r: sum(1 for x in new if x["auto_removed"] == r)
                         for r in ("before 2020", "non-study record type", "no exact search-term match")},
        "to_screen": sum(1 for x in new if not x["auto_removed"]),
    }
    (run / "chase_log.json").write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(log, ensure_ascii=False, indent=2))


def DASH(s: str) -> str:
    return S.DASHES.sub("-", s or "")


if __name__ == "__main__":
    main()
