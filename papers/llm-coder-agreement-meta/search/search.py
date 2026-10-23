"""Automated searches for the meta-analysis of LLM–human agreement on psychological and clinical text (protocol §9–§10).

Two arms, title and abstract, publication years 2020 onwards:
  arm A: three concept blocks combined with AND — 1. LLM; 2. human comparison and agreement; 3. psychological and clinical;
  arm B: 1. LLM AND 4. psychological coding constructs (cognitive distortions, motivational-interviewing codes, therapy
         sessions, clinical interviews, suicide risk, projective tests ...). Added after the check run of 2026-10-21:
         arm A missed 9 of 22 seed studies — benchmark papers that evaluate an LLM against labelled data without
         naming human coders or agreement statistics in the abstract.
Writes raw records to search/runs/<date>/raw/<source>.jsonl and the log (query strings, counts, timestamps) to
search/runs/<date>/search_log.json; dedup.py then merges duplicates and builds the screening list.
Templates: papers/sports-betting-prevalence/search/search.py and novelty/fetch_sources.py of this review.

Sources:
  pubmed     PubMed E-utilities, blocks in [tiab] with truncation; two-word phrases as proximity [tiab:~2];
  europepmc  Europe PMC including preprints (medRxiv, Research Square, PsyArXiv, SSRN, Preprints.org), TITLE_ABS;
  openalex   OpenAlex, three title_and_abstract.search filters;
  s2         Semantic Scholar bulk search (computer science, ACL Anthology);
  arxiv      arXiv API, abs: fields;
  psyarxiv   OSF API preprints (provider psyarxiv): LLM words in title or description, then blocks 2 and 3 locally;
  crossref   relevance-sorted queries, kept when title or abstract matches all three blocks (posted content, proceedings);
  datacite   DataCite (theses, OSF, Zenodo, figshare), the three blocks in title and description;
  core       CORE API v3, the three blocks; kept when title or abstract matches all three blocks.

Run:  .venv/Scripts/python.exe papers/llm-coder-agreement-meta/search/search.py [sources...] [--date YYYY-MM-DD]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

import httpx
from lxml import etree

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FROM_YEAR = 2020

# ---------------------------------------------------------------- concept blocks (protocol §10)
B1_LLM = ["large language model", "large language models", "LLM", "LLMs", "LLM-based", "ChatGPT", "GPT-3", "GPT-3.5",
          "GPT-4", "GPT-4o", "GPT-5", "GPT", "GPTs", "generative AI", "generative artificial intelligence",
          "generative pre-trained transformer", "generative pre-trained transformers", "generative pretrained transformer",
          "generative pretrained transformers", "foundation model", "foundation models"]
B2_HUMAN = ["inter-rater", "interrater", "inter-coder", "intercoder", "inter-annotator", "interannotator", "kappa",
            "Krippendorff", "Gwet", "intraclass", "agreement with human", "agreement with humans",
            "agreement with experts", "agreement with clinicians", "agreement between human", "human agreement",
            "human-LLM agreement", "LLM-human agreement", "human coder", "human coders", "human rater", "human raters",
            "human annotator", "human annotators", "human expert", "human experts", "human evaluators",
            "human judgments", "human judgements", "human labels", "human annotations", "human ratings",
            "expert annotations", "expert ratings", "expert raters", "expert coders", "expert-annotated",
            "human-annotated", "manually annotated", "manually coded", "manual coding", "manual annotation",
            "gold standard", "clinician ratings", "trained coders", "LLM-as-a-judge", "LLM-as-judge", "LLM judge",
            "LLM judges", "LLM evaluator", "LLM evaluators", "automated coding", "automated scoring",
            "automatic scoring", "deductive coding", "codebook", "codebooks"]
B3_PSY = ["psychology", "psychological", "psychologist", "psychiatry", "psychiatric", "psychotherapy",
          "psychotherapist", "counseling", "counselling", "counselor", "counsellor", "mental health", "mental illness",
          "depression", "depressive", "anxiety", "suicide", "suicidal", "self-harm", "trauma", "PTSD", "emotion",
          "emotions", "emotional", "affective", "personality", "empathy", "empathic", "well-being", "wellbeing",
          "motivational interviewing", "therapist", "therapists", "therapeutic", "crisis", "distress", "loneliness",
          "eating disorder", "substance use", "addiction", "psychosis", "schizophrenia", "bipolar", "autism", "ADHD",
          "attachment", "mentalization", "mentalizing", "reflective functioning", "cognitive distortion",
          "cognitive distortions", "defense mechanism", "defence mechanism", "projective", "Rorschach",
          "sentence completion", "narrative", "narratives", "qualitative", "interview", "interviews",
          "open-ended responses", "open-ended answers", "open-ended survey", "open-ended questionnaire",
          "free-text responses", "free-text answers", "divergent thinking"]


B4_CODING = ["cognitive distortion", "cognitive distortions", "maladaptive schema", "maladaptive schemas",
             "mental manipulation", "motivational interviewing", "change talk", "sustain talk", "MITI", "MISC",
             "therapeutic alliance", "counseling conversation", "counseling conversations", "counselling conversations",
             "counseling session", "counseling sessions", "therapy session", "therapy sessions", "therapy transcripts",
             "psychotherapy transcripts", "psychotherapy sessions", "clinical interview", "clinical interviews",
             "psychiatric interview", "psychiatric interviews", "diagnostic interview", "diagnostic interviews",
             "PTSD severity", "PTSD assessment", "depression severity", "symptom severity", "suicide risk",
             "suicidal risk", "C-SSRS", "wellness dimensions", "psychiatric functioning", "defense mechanisms",
             "psychological defenses", "Rorschach", "projective test", "projective tests", "projective technique",
             "sentence completion", "reflective functioning", "adult attachment interview", "autobiographical memory",
             "divergent thinking", "empathy detection", "empathy classification", "emotion regulation strategies",
             "psychological constructs", "therapist behaviors", "counselor behaviors", "counseling skills",
             "treatment fidelity", "psychotherapy fidelity"]


def _rx(terms: list[str]) -> re.Pattern:
    alts = sorted({re.escape(t).replace(r"\-", "[- ]?").replace(r"\ ", r"[\s\-]+") for t in terms}, key=len, reverse=True)
    return re.compile(r"(?<![A-Za-z])(" + "|".join(alts) + r")(?![A-Za-z])", re.I)


RX1, RX2, RX3, RX4 = _rx(B1_LLM), _rx(B2_HUMAN), _rx(B3_PSY), _rx(B4_CODING)


DASHES = re.compile("[‐‑‒–—−]")


def matches_all(text: str) -> bool:
    """Arm A or arm B (protocol §10); Unicode dashes are read as hyphens."""
    text = DASHES.sub("-", text or "")
    return bool(RX1.search(text) and ((RX2.search(text) and RX3.search(text)) or RX4.search(text)))


def b3_chunks(n: int = 25) -> list[list[str]]:
    """Block 3 split for GET sources whose URLs cannot hold all terms; results are united by source ID."""
    return [B3_PSY[i:i + n] for i in range(0, len(B3_PSY), n)]


def union(lists: list[list[dict]]) -> list[dict]:
    out, seen = [], set()
    for lst in lists:
        for r in lst:
            if r["source_id"] not in seen:
                seen.add(r["source_id"])
                out.append(r)
    return out


# ---------------------------------------------------------------- HTTP
def load_env() -> dict[str, str]:
    env = {}
    for line in (ROOT / ".env").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


ENV = load_env()
UA = "llm-coder-agreement-meta/1.0 (mailto:mrexert@gmail.com)"
client = httpx.Client(headers={"User-Agent": UA}, timeout=120, follow_redirects=True)


def _request(method: str, url: str, params: dict | None = None, data: dict | None = None, tries: int = 10, **kw):
    r = None
    for i in range(tries):
        try:
            r = client.request(method, url, params=params, data=data, **kw)
        except httpx.TransportError:
            time.sleep(5 * (i + 1))
            continue
        if r.status_code == 200:
            return r
        if r.status_code in (429, 500, 502, 503, 504):
            time.sleep(5 * (i + 1))
            continue
        r.raise_for_status()
    if r is None:
        raise RuntimeError(f"no response: {url}")
    r.raise_for_status()
    return r


def get(url, params=None, **kw):
    return _request("GET", url, params=params, **kw)


def post(url, data, **kw):
    return _request("POST", url, data=data, **kw)


def inv_to_text(inv: dict | None) -> str:
    if not inv:
        return ""
    pos = {p: w for w, ps in inv.items() for p in ps}
    return " ".join(pos[k] for k in sorted(pos))


def norm_doi(d: str | None) -> str:
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", (d or "").strip()).lower()


def rec(source, source_id, **kw) -> dict:
    out = {"source": source, "source_id": source_id, "pmid": "", "doi": "", "title": "", "abstract": "", "year": "",
           "venue": "", "first_author": "", "type": "", "language": "", "url": ""}
    out.update({k: (v if v is not None else "") for k, v in kw.items()})
    out["doi"] = norm_doi(out["doi"])
    out["abstract"] = (out["abstract"] or "")[:6000]
    return out


# ---------------------------------------------------------------- PubMed
def _pm_term(t: str) -> str:
    if " " in t or "-" in t:
        return f'"{t.replace("-", " ")}"[tiab:~2]'
    return f"{t}[tiab]"


PM_B1 = "(" + " OR ".join(_pm_term(t) for t in B1_LLM) + ")"
PM_B2 = "(" + " OR ".join(_pm_term(t) for t in B2_HUMAN) + ")"
PM_B3 = ("(" + " OR ".join(["psycholog*[tiab]", "psychiatr*[tiab]", "psychotherap*[tiab]", "counsel*[tiab]",
                            "suicid*[tiab]", "depress*[tiab]", "emotion*[tiab]", "therapist*[tiab]", "narrative*[tiab]",
                            "interview*[tiab]"] + [_pm_term(t) for t in B3_PSY]) + ")")
PM_B4 = "(" + " OR ".join(_pm_term(t) for t in B4_CODING) + ")"
PM_QUERY = f"({PM_B1} AND {PM_B2} AND {PM_B3}) OR ({PM_B1} AND {PM_B4})"


def pubmed():
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    r = post(base + "esearch.fcgi", {"db": "pubmed", "term": PM_QUERY, "retmax": 9999, "retmode": "json",
                                     "datetype": "pdat", "mindate": str(FROM_YEAR), "maxdate": "3000"})
    res = r.json()["esearchresult"]
    ids = res["idlist"]
    out = []
    for i in range(0, len(ids), 200):
        x = post(base + "efetch.fcgi", {"db": "pubmed", "id": ",".join(ids[i:i + 200]), "retmode": "xml"}).content
        for art in etree.fromstring(x).findall(".//PubmedArticle"):
            pmid = art.findtext(".//MedlineCitation/PMID")
            title = "".join(art.find(".//ArticleTitle").itertext()) if art.find(".//ArticleTitle") is not None else ""
            abstract = " ".join("".join(a.itertext()) for a in art.findall(".//Abstract/AbstractText"))
            doi = next((e.text for e in art.findall(".//ArticleIdList/ArticleId") if e.get("IdType") == "doi"), "")
            year = art.findtext(".//JournalIssue/PubDate/Year") or (art.findtext(".//JournalIssue/PubDate/MedlineDate") or "")[:4]
            au = art.find(".//AuthorList/Author/LastName")
            out.append(rec("pubmed", f"PMID:{pmid}", pmid=pmid, doi=doi, title=title, abstract=abstract, year=year,
                           venue=art.findtext(".//Journal/Title") or "", first_author=au.text if au is not None else "",
                           type=";".join(p.text or "" for p in art.findall(".//PublicationType")),
                           language=art.findtext(".//Language") or ""))
        time.sleep(0.4)
    return out, {"query": PM_QUERY, "count": res.get("count"), "translation": res.get("querytranslation"),
                 "warnings": res.get("warninglist")}


# ---------------------------------------------------------------- Europe PMC
def _ep(terms):
    return "(" + " OR ".join(f'TITLE_ABS:"{t}"' for t in terms) + ")"


EP_QUERY = (f"(({_ep(B1_LLM)} AND {_ep(B2_HUMAN)} AND {_ep(B3_PSY)}) OR ({_ep(B1_LLM)} AND {_ep(B4_CODING)}))"
            f" AND (FIRST_PDATE:[{FROM_YEAR}-01-01 TO 2030-12-31])")


def europepmc():
    out, cursor, total = [], "*", None
    while True:
        d = post("https://www.ebi.ac.uk/europepmc/webservices/rest/searchPOST",
                 {"query": EP_QUERY, "format": "json", "pageSize": 1000, "cursorMark": cursor, "resultType": "core"}).json()
        total = d.get("hitCount", total)
        res = d.get("resultList", {}).get("result", [])
        for it in res:
            out.append(rec("europepmc", f"{it.get('source')}:{it.get('id')}", pmid=it.get("pmid") or "",
                           doi=it.get("doi"), title=it.get("title"), abstract=it.get("abstractText"),
                           year=it.get("pubYear"),
                           venue=(it.get("journalInfo") or {}).get("journal", {}).get("title") or it.get("bookOrReportDetails", {}).get("publisher", ""),
                           first_author=(it.get("authorString") or "").split(",")[0],
                           type=";".join(it.get("pubTypeList", {}).get("pubType", [])) + f"|{it.get('source')}",
                           language=it.get("language") or ""))
        nxt = d.get("nextCursorMark")
        if not res or nxt == cursor or (total is not None and len(out) >= total):
            break
        cursor = nxt
    return out, {"query": EP_QUERY, "hitCount": total}


# ---------------------------------------------------------------- OpenAlex
def _oa(terms):
    return "title_and_abstract.search:" + "|".join(f'"{t}"' if re.search(r"[\s\-']", t) else t for t in terms)


OA_FILTERS = ([",".join([_oa(B1_LLM), _oa(B2_HUMAN), _oa(ch), f"from_publication_date:{FROM_YEAR}-01-01"]) for ch in b3_chunks()]
              + [",".join([_oa(B1_LLM), _oa(B4_CODING[i:i + 30]), f"from_publication_date:{FROM_YEAR}-01-01"])
                 for i in range(0, len(B4_CODING), 30)])


def openalex():
    return union([_openalex_one(f) for f in OA_FILTERS]), {"filters": OA_FILTERS}


def _openalex_one(flt: str) -> list[dict]:
    out, cursor = [], "*"
    while cursor:
        d = get("https://api.openalex.org/works", {"filter": flt, "per_page": 200, "cursor": cursor,
                                                   "api_key": ENV["OPENALEX_API_KEY"]}).json()
        for w in d["results"]:
            loc = w.get("primary_location") or {}
            src = loc.get("source") or {}
            ids = w.get("ids") or {}
            out.append(rec("openalex", w["id"], pmid=(ids.get("pmid") or "").rsplit("/", 1)[-1], doi=w.get("doi"),
                           title=w.get("title"), abstract=inv_to_text(w.get("abstract_inverted_index")),
                           year=w.get("publication_year"), venue=src.get("display_name") or "",
                           first_author=((w.get("authorships") or [{}])[0].get("author") or {}).get("display_name", "") if w.get("authorships") else "",
                           type=w.get("type") or "", language=w.get("language") or "",
                           url=(w.get("open_access") or {}).get("oa_url") or ""))
        cursor = d["meta"].get("next_cursor")
        if not d["results"]:
            break
    return out


# ---------------------------------------------------------------- Semantic Scholar
def _s2(terms):
    return "(" + " | ".join(f'"{t}"' for t in terms) + ")"


S2_QUERIES = ([f"{_s2(B1_LLM)} + {_s2(B2_HUMAN)} + {_s2(ch)}" for ch in b3_chunks()]
              + [f"{_s2(B1_LLM)} + {_s2(B4_CODING[i:i + 30])}" for i in range(0, len(B4_CODING), 30)])


def semantic_scholar():
    return union([_s2_one(q) for q in S2_QUERIES]), {"queries": S2_QUERIES}


def _s2_one(query: str) -> list[dict]:
    out, token = [], None
    fields = "title,year,externalIds,publicationTypes,venue,abstract,authors,openAccessPdf"
    while True:
        params = {"query": query, "fields": fields, "year": f"{FROM_YEAR}-"}
        if token:
            params["token"] = token
        d = get("https://api.semanticscholar.org/graph/v1/paper/search/bulk", params).json()
        for p in d.get("data", []):
            ext = p.get("externalIds") or {}
            doi = ext.get("DOI") or (f"10.48550/arxiv.{ext['ArXiv']}" if ext.get("ArXiv") else "")
            out.append(rec("s2", f"S2:{p.get('paperId')}", pmid=str(ext.get("PubMed") or ""), doi=doi,
                           title=p.get("title"), abstract=p.get("abstract"), year=p.get("year"), venue=p.get("venue"),
                           first_author=((p.get("authors") or [{}])[0] or {}).get("name", "") if p.get("authors") else "",
                           type=";".join(p.get("publicationTypes") or []),
                           url=(p.get("openAccessPdf") or {}).get("url") or ""))
        token = d.get("token")
        if not token:
            break
        time.sleep(1.5)
    return out


# ---------------------------------------------------------------- arXiv
def _ax(terms):
    return "(" + " OR ".join(f'abs:"{t}"' if (" " in t or "-" in t) else f"abs:{t}" for t in terms) + ")"


AX_QUERIES = ([f"{_ax(B1_LLM)} AND {_ax(B2_HUMAN)} AND {_ax(ch)}" for ch in b3_chunks()]
              + [f"{_ax(B1_LLM)} AND {_ax(B4_CODING[i:i + 30])}" for i in range(0, len(B4_CODING), 30)])


def arxiv():
    res = [_arxiv_one(q) for q in AX_QUERIES]
    return union([r[0] for r in res]), {"queries": AX_QUERIES, "totalResults": [r[1] for r in res]}


def _arxiv_one(query: str):
    ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom",
          "os": "http://a9.com/-/spec/opensearch/1.1/"}
    out, start, total = [], 0, None
    while total is None or start < total:
        r = get("http://export.arxiv.org/api/query", {"search_query": query, "start": start, "max_results": 500,
                                                       "sortBy": "submittedDate", "sortOrder": "descending"})
        root = etree.fromstring(r.content)
        total = int(root.findtext("os:totalResults", namespaces=ns) or 0)
        entries = root.findall("a:entry", ns)
        for e in entries:
            aid = re.sub(r"v\d+$", "", (e.findtext("a:id", namespaces=ns) or "").rsplit("/abs/", 1)[-1])
            year = (e.findtext("a:published", namespaces=ns) or "")[:4]
            if year and int(year) < FROM_YEAR:
                continue
            au = e.find("a:author/a:name", ns)
            out.append(rec("arxiv", f"arXiv:{aid}", doi=f"10.48550/arxiv.{aid}",
                           title=" ".join((e.findtext("a:title", namespaces=ns) or "").split()),
                           abstract=" ".join((e.findtext("a:summary", namespaces=ns) or "").split()), year=year,
                           venue=e.findtext("arxiv:journal_ref", namespaces=ns) or "arXiv",
                           first_author=au.text if au is not None else "", type="preprint",
                           url=f"https://arxiv.org/abs/{aid}"))
        if not entries:
            break
        start += len(entries)
        time.sleep(3.5)
    return out, total


# ---------------------------------------------------------------- PsyArXiv (OSF API)
PSYARXIV_WORDS = ["large language model", "LLM", "ChatGPT", "GPT-4", "GPT-3", "GPT-5", "generative AI",
                  "generative artificial intelligence"]


def psyarxiv():
    out, seen, scanned = [], set(), 0
    for w in PSYARXIV_WORDS:
        for field in ("title", "description"):
            url, params, pages = "https://api.osf.io/v2/preprints/", {
                "filter[provider]": "psyarxiv", f"filter[{field}][icontains]": w, "page[size]": 100}, 0
            while url and pages < 80:
                d = get(url, params).json()
                for it in d.get("data", []):
                    if it["id"] in seen:
                        continue
                    seen.add(it["id"])
                    scanned += 1
                    a = it.get("attributes") or {}
                    t, ab = a.get("title") or "", a.get("description") or ""
                    if not matches_all(f"{t} {ab}"):
                        continue
                    year = (a.get("date_published") or a.get("date_created") or "")[:4]
                    if year and int(year) < FROM_YEAR:
                        continue
                    out.append(rec("psyarxiv", f"PsyArXiv:{it['id']}", doi=a.get("doi") or f"10.31234/osf.io/{it['id']}",
                                   title=t, abstract=ab, year=year, venue="PsyArXiv", type="preprint",
                                   url=f"https://osf.io/{it['id']}"))
                url, params = (d.get("links") or {}).get("next"), None
                pages += 1
                time.sleep(0.3)
    return out, {"words": PSYARXIV_WORDS, "scanned_unique": scanned, "local_filter": "blocks 1-3 in title or abstract"}


# ---------------------------------------------------------------- Crossref
CR_QUERIES = ["large language model agreement human coders psychology", "LLM inter-rater reliability mental health",
              "ChatGPT kappa human raters psychological", "GPT-4 coding qualitative interviews agreement human coders",
              "large language model psychotherapy transcripts coding", "LLM motivational interviewing coding",
              "LLM-as-a-judge mental health clinicians", "large language model suicide risk annotation agreement",
              "large language model scoring psychological assessment human raters",
              "large language model emotion annotation human annotators", "LLM content analysis human coders",
              "generative AI qualitative coding reliability"]


def crossref():
    out, seen, meta = [], set(), {}
    for q in CR_QUERIES:
        kept, offset = 0, 0
        while offset < 2000:
            d = get("https://api.crossref.org/works", {
                "query.bibliographic": q, "rows": 1000, "offset": offset, "sort": "score", "order": "desc",
                "filter": f"from-pub-date:{FROM_YEAR}-01-01", "mailto": "mrexert@gmail.com",
                "select": "DOI,title,type,issued,container-title,abstract,author,publisher"}).json()["message"]
            items = d["items"]
            page_kept = 0
            for it in items:
                t = " ".join(it.get("title") or [])
                ab = re.sub(r"<[^>]+>", " ", it.get("abstract") or "")
                if not matches_all(f"{t} {ab}"):
                    continue
                page_kept += 1
                if it["DOI"].lower() in seen:
                    continue
                seen.add(it["DOI"].lower())
                yr = ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0]
                out.append(rec("crossref", f"DOI:{it['DOI'].lower()}", doi=it["DOI"], title=t, abstract=ab, year=yr,
                               venue=" ".join(it.get("container-title") or []) or it.get("publisher") or "",
                               first_author=((it.get("author") or [{}])[0].get("family") or "") if it.get("author") else "",
                               type=it.get("type") or ""))
            kept += page_kept
            offset += len(items)
            if not items or page_kept < 10:
                break
            time.sleep(1)
        meta[q] = {"kept": kept, "scanned": offset}
        time.sleep(1)
    return out, {"queries": meta, "local_filter": "blocks 1-3 in title or abstract"}


# ---------------------------------------------------------------- DataCite
def _dc(terms):
    return "(" + " OR ".join(f'"{t}"' for t in terms) + ")"


DC_QUERIES = [" AND ".join(f"(titles.title:{_dc(b)} OR descriptions.description:{_dc(b)})" for b in (B1_LLM, B2_HUMAN, ch))
              + f" AND publicationYear:[{FROM_YEAR} TO 2030]" for ch in b3_chunks()] + [
    " AND ".join(f"(titles.title:{_dc(b)} OR descriptions.description:{_dc(b)})" for b in (B1_LLM, B4_CODING[i:i + 30]))
    + f" AND publicationYear:[{FROM_YEAR} TO 2030]" for i in range(0, len(B4_CODING), 30)]


def datacite():
    return union([_datacite_one(q) for q in DC_QUERIES]), {"queries": DC_QUERIES}


def _datacite_one(query: str) -> list[dict]:
    out, url, params = [], "https://api.datacite.org/dois", {"query": query, "page[size]": 1000}
    while url:
        d = get(url, params).json()
        for it in d.get("data", []):
            a = it["attributes"]
            title = " ".join(t.get("title", "") for t in a.get("titles") or [])
            desc = " ".join(x.get("description") or "" for x in a.get("descriptions") or [] if isinstance(x.get("description"), str))
            pub = a.get("publisher")
            out.append(rec("datacite", f"DOI:{(a.get('doi') or '').lower()}", doi=a.get("doi"), title=title,
                           abstract=desc, year=a.get("publicationYear"),
                           venue=pub if isinstance(pub, str) else (pub or {}).get("name", ""),
                           first_author=((a.get("creators") or [{}])[0].get("name") or "") if a.get("creators") else "",
                           type=f"{(a.get('types') or {}).get('resourceTypeGeneral')}/{(a.get('types') or {}).get('resourceType')}"))
        url, params = (d.get("links") or {}).get("next"), None
    return out


# ---------------------------------------------------------------- CORE
CORE_QUERY = ("(" + " OR ".join(f'"{t}"' for t in ["large language model", "large language models", "LLM", "ChatGPT", "GPT-4"])
              + ") AND (" + " OR ".join(f'"{t}"' for t in ["inter-rater", "interrater", "kappa", "human coders",
                                                          "human raters", "human annotators", "LLM-as-a-judge",
                                                          "agreement with human"]) + ")"
              + f" AND yearPublished>={FROM_YEAR}")


def core():
    out, seen, offset, total, dropped, stopped_400 = [], set(), 0, None, 0, None
    hdr = {"Authorization": f"Bearer {ENV['CORE_API_KEY']}"} if ENV.get("CORE_API_KEY") else {}
    while offset < 5000:
        r = None
        for i in range(6):
            try:
                r = client.get("https://api.core.ac.uk/v3/search/works", params={"q": CORE_QUERY, "limit": 100, "offset": offset},
                               headers=hdr)
            except httpx.TransportError:
                r = None
            if r is not None and r.status_code == 200:
                break
            time.sleep(10 * (i + 1))
        if r is not None and r.status_code == 400 and offset > 0:
            stopped_400 = offset   # CORE refuses deep offsets for this query; keep what was collected
            break
        if r is None or r.status_code != 200:
            raise RuntimeError(f"CORE failed at offset {offset}: {r.status_code if r is not None else 'no response'}")
        d = r.json()
        total = d.get("totalHits", total)
        res = d.get("results") or []
        page_kept = 0
        for w in res:
            t, ab = w.get("title") or "", w.get("abstract") or ""
            if not matches_all(f"{t} {ab}"):
                dropped += 1
                continue
            page_kept += 1
            if w.get("id") in seen:
                continue
            seen.add(w.get("id"))
            out.append(rec("core", f"CORE:{w.get('id')}", pmid=str(w.get("pubmedId") or ""), doi=w.get("doi"), title=t,
                           abstract=ab, year=w.get("yearPublished"), venue=w.get("publisher") or "",
                           first_author=((w.get("authors") or [{}])[0].get("name") or "") if w.get("authors") else "",
                           type=w.get("documentType") or "", url=w.get("downloadUrl") or ""))
        offset += len(res)
        time.sleep(7)
        if not res or offset >= (total or 0) or page_kept < 5:
            break
    return out, {"query": CORE_QUERY, "totalHits": total, "scanned": offset, "dropped_not_all_blocks": dropped,
                 "stopped_at_offset_http_400": stopped_400}


SOURCES = {"pubmed": pubmed, "europepmc": europepmc, "openalex": openalex, "s2": semantic_scholar, "arxiv": arxiv,
           "psyarxiv": psyarxiv, "crossref": crossref, "datacite": datacite, "core": core}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sources", nargs="*", default=list(SOURCES))
    ap.add_argument("--date", default=date.today().isoformat())
    a = ap.parse_args()
    run = HERE / "runs" / a.date
    (run / "raw").mkdir(parents=True, exist_ok=True)
    log_path = run / "search_log.json"
    log = json.loads(log_path.read_text(encoding="utf-8")) if log_path.exists() else {}
    log["_blocks"] = {"llm": B1_LLM, "human": B2_HUMAN, "psy": B3_PSY, "coding_constructs": B4_CODING, "from_year": FROM_YEAR,
                      "crossref_queries": CR_QUERIES, "psyarxiv_words": PSYARXIV_WORDS}
    for name in a.sources:
        t0 = time.time()
        try:
            recs, meta = SOURCES[name]()
        except Exception as e:  # noqa: BLE001
            print(f"{name}: FAILED {e!r}", file=sys.stderr, flush=True)
            log[name] = {"error": repr(e), "at": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
            continue
        with (run / "raw" / f"{name}.jsonl").open("w", encoding="utf-8") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        log[name] = {"records": len(recs), "meta": meta,
                     "searched_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                     "seconds": round(time.time() - t0, 1)}
        print(f"{name}: {len(recs)} records", flush=True)
        log_path.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
