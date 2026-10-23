"""De-duplication and the screening list (protocol, section 11a).

Input: search/runs/<date>/raw/*.jsonl (search.py and import_manual.py).
Output in the same folder:
  records_unique.jsonl  unique records with all identifiers and sources;
  screening.csv         the title/abstract screening list (decision columns empty);
  screening.ris         the same for reference managers;
  dedup_report.json     numbers for the PRISMA flow diagram.

Rules:
  1. one record = one DOI (version suffixes .v1 /v1 _v1 and SciELO language suffixes pt/en/es are ignored);
     records without a DOI merge on PMID;
  2. then on the exact normalised title (case, accents, punctuation and spaces ignored) with years within +-1, unless the two records carry different DOIs:
     a preprint and its journal article stay two reports of one study; exception (2b, this review): when one of the two
     DOIs is a preprint DOI (arXiv 10.48550/arxiv., PsyArXiv 10.31234/), records with the same title merge, so that an
     arXiv paper and its ACL or journal version are screened once; both DOIs stay in all_dois;
  3. records from pointer sources (DataCite, OpenAIRE, CORE, Google Scholar, hand searching) and article
     components (figshare deposits, "Additional file 1 of ...", "Supplementary tables from ...") are attached
     to the first database record with the same title (for components: the title of the parent article) and
     years within +-1, whatever their DOIs; without such a record they are merged only among themselves;
     (3a) a pointer-source title shortened with an ellipsis (Google Scholar) joins the database record whose
     title contains its visible fragment of at least 30 characters, years within +-1;
  4. similar titles (similarity >= 0.93) are flagged in possible_duplicate_of, not merged;
  5. records that every source types as a non-study record (peer-review reports, errata, retractions,
     paratext, book reviews, dictionary entries, datasets, figures, tables, images, software, audiovisual
     material, study registrations, patents, grant records) are removed before screening ("removed by
     automation tools" in PRISMA 2020).
  6. (this review) search-term consistency: OpenAlex and Semantic Scholar stem and match loosely, so a unique record is
     removed before screening when neither arm of the search (protocol §10) matches its title and abstract as exact
     phrases (search.matches_all); records without an abstract (under 50 characters) are kept when the title has an
     LLM term. Removed records stay in records_unique.jsonl with auto_removed = "no exact search-term match".
Copied from papers/ai-dependence-correlates/search/dedup.py (misophonia v1.0 rules); SOURCE_ORDER adds arxiv and
psyarxiv, rule 2b merges preprints with their published versions, rule 6 checks search-term consistency.
Run: .venv/Scripts/python.exe papers/llm-coder-agreement-meta/search/dedup.py --date 2026-10-21-check
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

from search import DASHES, RX1, matches_all

HERE = Path(__file__).resolve().parent
SOURCE_ORDER = ["pubmed", "europepmc", "openalex", "s2", "arxiv", "psyarxiv", "crossref", "citations",
                "datacite", "core", "scholar", "hand"]
PREPRINT_DOI = re.compile(r"^10\.48550/arxiv\.|^10\.31234/")
POINTER_SOURCES = {"datacite", "openaire", "core", "scholar", "hand"}
NON_STUDY = re.compile(
    r"peer-review|erratum|correction|retraction|paratext|book-review|reference-entry|dataset|component|figure"
    r"|table|image|software|audiovisual|sound|workflow|physicalobject|registration|patent|grant|libguides"
    r"|supplementary-materials|outputmanagementplan|computationalnotebook", re.I)
COMPONENT_TITLE = re.compile(
    r"^(?:additional (?:file|material)s? \d+ (?:of|for)"
    r"|supplementary (?:material|information|data|table|figure|file|appendix|text|video|movie|audio)s?(?: \d+)?"
    r"(?: (?:from|for|of|to)|\s*[:\-–—])"
    r"|supplemental (?:material|information|data)s?(?: (?:from|for|of|to)|\s*[:\-–—])"
    r"|sj-[a-z0-9]+-\d+-\S+\s+[-–—]\s+supplemental material for)\s+|^(?:data_sheet|datasheet|table|image|figure|presentation|video|audio)_?\d+_", re.I)   # Frontiers: Data_Sheet_1_<title>.pdf
FILE_EXT = re.compile(r"\.(?:pdf|docx?|xlsx?|csv|zip|pptx?|txt|tif|png|jpe?g)$", re.I)   # file name of a deposited supplement
DEPOSIT_DOI = re.compile(r"^10\.6084/|^10\.25384/")   # figshare, including publishers' figshare portals


def norm_title(t: str) -> str:
    t = re.sub(r"<[^>]+>", " ", t or "")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def clean(t: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t or "")).strip()


def doi_key(d: str | None) -> str:
    d = (d or "").strip().lower()
    # SciELO gives language versions of one article their own DOIs: 10.1590/...-3080pt and ...-3080en
    d = re.sub(r"^(10\.1590/.+?\d)(pt|en|es)$", r"\1", d)
    # versions of one deposit or preprint: figshare .v2, Research Square /v1, OSF preprints _v1
    return re.sub(r"([./_])v\d+$", "", d)


class UF:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            self.p[max(a, b)] = min(a, b)


def year_int(y):
    try:
        return int(str(y)[:4])
    except (TypeError, ValueError):
        return None


def years_close(a, b) -> bool:
    ya, yb = year_int(a), year_int(b)
    return ya is None or yb is None or abs(ya - yb) <= 1


def is_component(r: dict) -> bool:
    return bool(COMPONENT_TITLE.match(clean(r.get("title")))) or bool(DEPOSIT_DOI.match(doi_key(r.get("doi"))))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    a = ap.parse_args()
    run = HERE / "runs" / a.date
    recs, per_source = [], {}
    for src in SOURCE_ORDER:
        p = run / "raw" / f"{src}.jsonl"
        if not p.exists():
            continue
        rows = [json.loads(line) for line in p.open(encoding="utf-8")]
        per_source[src] = len(rows)
        recs.extend(rows)
    unknown = sorted({p.stem for p in (run / "raw").glob("*.jsonl")} - set(SOURCE_ORDER))
    if unknown:
        raise SystemExit(f"unknown raw sources (add them to SOURCE_ORDER): {unknown}")

    n = len(recs)
    attachable = [r["source"] in POINTER_SOURCES or is_component(r) for r in recs]
    # title key without spaces, so that "U.S." and "US" or "Covid-19" and "Covid 19" still match
    spaced = [norm_title(FILE_EXT.sub("", COMPONENT_TITLE.sub("", clean(r.get("title"))))) for r in recs]
    title_key = [t.replace(" ", "") if len(t) >= 15 else "" for t in spaced]

    uf = UF(n)
    by_doi, by_pmid, by_title = {}, {}, defaultdict(list)
    for i, r in enumerate(recs):
        d = doi_key(r.get("doi"))
        if d:
            if d in by_doi:
                uf.union(i, by_doi[d])
            else:
                by_doi[d] = i
        pm = str(r.get("pmid") or "").strip()
        if pm:
            if pm in by_pmid:
                uf.union(i, by_pmid[pm])
            else:
                by_pmid[pm] = i
        if title_key[i]:
            by_title[title_key[i]].append(i)

    attached = 0
    for nt, idxs in by_title.items():
        core = [i for i in idxs if not attachable[i]]
        extra = [i for i in idxs if attachable[i]]
        # rule 2: database records with the same title merge unless they carry different DOIs
        for j in core[1:]:
            i0 = core[0]
            d0, d1 = doi_key(recs[i0].get("doi")), doi_key(recs[j].get("doi"))
            preprint_pair = bool(PREPRINT_DOI.match(d0) or PREPRINT_DOI.match(d1))
            if years_close(recs[i0].get("year"), recs[j].get("year")) and (not (d0 and d1 and d0 != d1) or preprint_pair):
                uf.union(i0, j)
        # rule 3: pointer records and components join the first database record with that title
        for j in extra:
            target = next((i for i in core if years_close(recs[i].get("year"), recs[j].get("year"))), None)
            if target is None:
                target = next((i for i in extra if i != j and years_close(recs[i].get("year"), recs[j].get("year"))), None)
            if target is not None and uf.find(target) != uf.find(j):
                uf.union(target, j)
                attached += 1

    # rule 3a: Google Scholar shortens long titles with an ellipsis ("Listening to people with misophonia: ... usi…");
    # such a pointer record joins the database record whose title contains the visible fragment (>= 30 characters)
    compact = [norm_title(clean(r.get("title"))).replace(" ", "") for r in recs]
    for j, r in enumerate(recs):
        t = clean(r.get("title"))
        if r["source"] not in POINTER_SOURCES or not re.search(r"…|\.\.\.", t):
            continue
        frags = [norm_title(x).replace(" ", "") for x in re.split(r"…|\.\.\.", t)]
        frag = max(frags, key=len)
        if len(frag) < 30:
            continue
        target = next((i for i in range(n) if not attachable[i] and frag in compact[i]
                       and years_close(recs[i].get("year"), r.get("year"))), None)
        if target is not None and uf.find(target) != uf.find(j):
            uf.union(target, j)
            attached += 1

    groups = defaultdict(list)
    for i in range(n):
        groups[uf.find(i)].append(i)

    unique = []
    for idxs in groups.values():
        members = [recs[i] for i in idxs]
        # best record: a database record that is not a component, with an abstract; then source priority
        best_i = max(idxs, key=lambda i: (not attachable[i], len(clean(recs[i].get("abstract"))) > 50,
                                          -SOURCE_ORDER.index(recs[i]["source"]), len(clean(recs[i].get("abstract")))))
        best = recs[best_i]
        dois = sorted({m["doi"] for m in members if m.get("doi")})
        main_doi = best.get("doi") or (dois[0] if dois else "")
        pmids = sorted({str(m["pmid"]) for m in members if m.get("pmid")})
        sources = sorted({m["source"] for m in members}, key=SOURCE_ORDER.index)
        cites = sorted({m["cites"] for m in members if m.get("cites")})
        abstract = max((clean(m.get("abstract")) for m in members), key=len)
        unique.append({
            "title": clean(best.get("title")), "abstract": abstract, "year": year_int(best.get("year")) or "",
            "first_author": best.get("first_author") or next((m.get("first_author") for m in members if m.get("first_author")), ""),
            "venue": best.get("venue") or next((m.get("venue") for m in members if m.get("venue")), ""),
            "doi": main_doi, "all_dois": ";".join(dois), "pmid": pmids[0] if pmids else "",
            "types": " | ".join(sorted({f"{m['source']}:{m.get('type')}" for m in members})),
            "language": next((m.get("language") for m in members if m.get("language")), ""),
            "sources": ";".join(sources), "n_sources": len(sources),
            "only_via_citations": sources == ["citations"], "cites_instruments": ";".join(cites),
            "only_via_pointer_sources": all(s in POINTER_SOURCES for s in sources),
            "component_only": all(attachable[i] and is_component(recs[i]) for i in idxs),
            "source_ids": ";".join(sorted({m["source_id"] for m in members})),
            "url": next((m.get("url") for m in members if m.get("url")), ""),
        })

    # order: year (newest first), author, title; then record IDs R0001...
    unique.sort(key=lambda u: (-(u["year"] or 0), u["first_author"].lower(), u["title"].lower()))
    for k, u in enumerate(unique, 1):
        u["rec_id"] = f"R{k:04d}"

    # similar titles: flagged, not merged
    by_first = defaultdict(list)
    for u in unique:
        nt = norm_title(u["title"])
        if nt:
            by_first[nt[:12]].append((u["rec_id"], nt))
    flags = defaultdict(set)
    for bucket in by_first.values():
        for x in range(len(bucket)):
            for y in range(x + 1, len(bucket)):
                (r1, t1), (r2, t2) = bucket[x], bucket[y]
                if SequenceMatcher(None, t1, t2).ratio() >= 0.93:
                    flags[r1].add(r2)
                    flags[r2].add(r1)
    removed_types = Counter()
    for u in unique:
        u["possible_duplicate_of"] = ";".join(sorted(flags.get(u["rec_id"], [])))
        u["link"] = (f"https://doi.org/{u['doi']}" if u["doi"]
                     else f"https://pubmed.ncbi.nlm.nih.gov/{u['pmid']}/" if u["pmid"] else u["url"])
        # Protocol rule, applied before screening: records that every source types as a non-study record.
        types = [t.split(":", 1)[1].lower() for t in u["types"].split(" | ") if ":" in t]
        u["auto_removed"] = "non-study record type" if types and all(NON_STUDY.search(t) for t in types) else ""
        if u["auto_removed"]:
            removed_types[u["types"]] += 1
        elif not (matches_all(f"{u['title']} {u['abstract']}")
                  or (len(u["abstract"]) < 50 and RX1.search(DASHES.sub("-", u["title"])))):
            u["auto_removed"] = "no exact search-term match"

    with (run / "records_unique.jsonl").open("w", encoding="utf-8") as f:
        for u in unique:
            f.write(json.dumps(u, ensure_ascii=False) + "\n")

    cols = ["rec_id", "title", "abstract", "year", "first_author", "venue", "doi", "pmid", "link", "language", "types",
            "sources", "n_sources", "only_via_citations", "only_via_pointer_sources", "component_only",
            "cites_instruments", "possible_duplicate_of", "decision", "reason", "note"]
    to_screen = [u for u in unique if not u["auto_removed"]]
    with (run / "screening.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for u in to_screen:
            w.writerow({**u, "decision": "", "reason": "", "note": ""})

    with (run / "screening.ris").open("w", encoding="utf-8") as f:
        for u in to_screen:
            f.write("TY  - JOUR\n")
            f.write(f"ID  - {u['rec_id']}\n")
            f.write(f"TI  - {u['title']}\n")
            if u["first_author"]:
                f.write(f"AU  - {u['first_author']}\n")
            if u["year"]:
                f.write(f"PY  - {u['year']}\n")
            if u["venue"]:
                f.write(f"JO  - {u['venue']}\n")
            if u["abstract"]:
                f.write(f"AB  - {u['abstract']}\n")
            if u["doi"]:
                f.write(f"DO  - {u['doi']}\n")
            if u["pmid"]:
                f.write(f"AN  - PMID:{u['pmid']}\n")
            f.write(f"N1  - {u['rec_id']}; sources: {u['sources']}\n")
            f.write("ER  - \n\n")

    report = {
        "records_per_source": per_source, "records_total": n, "unique_records": len(unique),
        "duplicates_removed": n - len(unique),
        "pointer_or_component_records_attached": attached,
        "auto_removed_non_study_records": sum(1 for u in unique if u["auto_removed"] == "non-study record type"),
        "auto_removed_no_search_term_match": sum(1 for u in unique if u["auto_removed"] == "no exact search-term match"),
        "auto_removed_by_types": dict(removed_types.most_common()),
        "records_to_screen": len(to_screen),
        "unique_only_via_instrument_citations": sum(1 for u in unique if u["only_via_citations"] and not u["auto_removed"]),
        "unique_only_via_pointer_sources": sum(1 for u in unique if u["only_via_pointer_sources"] and not u["auto_removed"]),
        "component_only_records_to_screen": sum(1 for u in to_screen if u["component_only"]),
        "flagged_possible_duplicates": sum(1 for u in unique if u["possible_duplicate_of"]),
        "unique_by_n_sources": {k: sum(1 for u in unique if u["n_sources"] == k) for k in range(1, len(SOURCE_ORDER) + 1)
                                if any(u["n_sources"] == k for u in unique)},
    }
    (run / "dedup_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "auto_removed_by_types"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
