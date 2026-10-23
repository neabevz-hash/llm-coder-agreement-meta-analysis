"""Supplementary files built from the logs, the coded tables and the analysis results (no numbers typed by hand).

S1_studies.md      - included studies: reports, task types, publication status, risk of bias (forms/studies.csv)
S2_models.md       - model registry: release dates and their sources (forms/model_releases.csv)
S3_deviations.md   - every change after registration (deviations.md)
S4_search.md       - search strategies, dates and counts per source (PRISMA-S), de-duplication, recall, citation
                     searching, AI tools with models, prompts and outputs
S5_checklists.md   - PRISMA 2020, PRISMA-S and REGEMA checklists with the location of each item
S6_analyses.md     - all moderator models, sensitivity analyses, leave-one-out, small-study effects, SE sources
Template: papers/sports-betting-prevalence/manuscript/make_supplement.py.

Run: .venv/Scripts/python.exe -I papers/llm-coder-agreement-meta/manuscript/make_supplement.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent
OUT = HERE / "supplement"
RUN = PAPER / "search" / "runs" / "2026-10-21"
CHASE = PAPER / "search" / "runs" / "2026-10-23-citations"
RES = PAPER / "analysis" / "results"
TT = {"T1": "codebook coding", "T2": "assessment scoring", "T3": "clinical state rating", "T4": "LLM-as-a-judge",
      "all": "all tasks"}
SOURCES = {"pubmed": ("PubMed", "NCBI E-utilities, [tiab] fields; multi-word terms with proximity [tiab:~2]"),
           "europepmc": ("Europe PMC", "REST API, TITLE_ABS fields"),
           "openalex": ("OpenAlex", "API, title_and_abstract.search filters, one filter per block"),
           "s2": ("Semantic Scholar", "Graph API, bulk search, OR-joined phrases, run in chunks"),
           "arxiv": ("arXiv", "API, ti/abs fields, run in chunks"),
           "psyarxiv": ("PsyArXiv (OSF preprints)", "OSF API, LLM words in titles; blocks matched locally"),
           "crossref": ("Crossref", "REST API, query.bibliographic, 12 queries; blocks matched locally"),
           "datacite": ("DataCite", "REST API, titles and descriptions, run in chunks"),
           "core": ("CORE", "API v3, one Boolean query; paging stopped at HTTP 400")}


def rows(path: Path) -> list[dict]:
    return list(csv.DictReader(path.open(encoding="utf-8")))


def cell(x, n: int | None = None) -> str:
    s = re.sub(r"\s+", " ", str(x or "")).replace("|", "/").strip()
    return s if n is None or len(s) <= n else s[: n - 1].rstrip() + "…"


def num(x, d=2) -> str:
    try:
        return f"{float(x):.{d}f}".replace("-", "−")
    except (TypeError, ValueError):
        return "–"


def pval(x) -> str:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return "–"
    return "< .001" if v < 0.001 else f"{v:.3f}".lstrip("0")


def ci95(r: dict) -> str:
    if r.get("est") in (None, "", "NA"):
        return "not estimated (fewer than 3 studies)"
    if r.get("ci_lb") in (None, "", "NA"):
        return num(r["est"])
    return f"{num(r['est'])} [{num(r['ci_lb'])}, {num(r['ci_ub'])}]"


def table(head: list[str], body: list[list]) -> list[str]:
    return ["| " + " | ".join(head) + " |", "| " + " | ".join("---" for _ in head) + " |"] + \
        ["| " + " | ".join(cell(c) for c in r) + " |" for r in body]


# ------------------------------------------------------------------------------------------------------------- S1

def s1() -> str:
    st = rows(HERE / "supplement_S1_studies.csv")
    rob = (PAPER / "forms" / "rob.md").read_text(encoding="utf-8")
    rob_table = "\n".join(ln for ln in rob.splitlines() if ln.startswith("|"))
    L = [f"**Supplementary File S1.** Included studies (n = {len(st)}) with their reports, task types and risk of bias", "",
         "Risk-of-bias domains (protocol §14, adapted from QUADAS-2); each rated low, high or unclear, no summary score:", "",
         rob_table, "",
         "Task types: T1 codebook coding, T2 assessment scoring, T3 clinical state rating, T4 LLM-as-a-judge. "
         "Reports: record IDs of the search (R…) and of citation searching (R2….). RoB columns: 1 unit selection, "
         "2 LLM configuration, 3 human reference, 4 data contamination, 5 reporting (L low, H high, U unclear). "
         "The full coding of each study is in the repository (forms/studies.csv, forms/tasks.csv, forms/estimates.csv).", ""]
    ab = {"low": "L", "high": "H", "unclear": "U"}
    L += table(["Study", "First author", "Year", "Title", "DOI", "Reports", "Tasks", "Status", "1", "2", "3", "4", "5"],
               [[s["study_id"], s["first_author"], s["year"], cell(s["title"], 140), s["doi"], s["reports"].replace(";", "; "),
                 s["task_types"], s["pub_status"], *(ab.get(s[f"rob_{i}"], s[f"rob_{i}"] or "–") for i in range(1, 6))]
                for s in st])
    return "\n".join(L)


# ------------------------------------------------------------------------------------------------------------- S2

def s2() -> str:
    m = rows(PAPER / "forms" / "model_releases.csv")
    L = [f"**Supplementary File S2.** Model registry: {len(m)} models named in the included studies, with release dates "
         "used for hypothesis G3 and the model-generation counts", "",
         "Release dates: the developer's announcement for models released before 2025; for later models the creation date "
         "in the OpenRouter model list (/api/v1/models, field created). Names in reports: the spellings found in the "
         "studies that were mapped to the model (extraction/models.py). Estimates: kappa-family, ICC and correlation "
         "estimates attributed to the model.", ""]
    L += table(["Model", "Developer", "Release date", "Source of date", "Open weights", "Names in reports", "Estimates"],
               [[r["model"], r["developer"], r["release_date"], r["release_source"], r["open_weights"],
                 cell(r["names_in_reports"], 160), r["estimates"]] for r in m])
    return "\n".join(L)


# ------------------------------------------------------------------------------------------------------------- S3

def s3() -> str:
    md = (PAPER / "deviations.md").read_text(encoding="utf-8")
    md = re.sub(r"(?m)^# .*\n", "", md, count=1)
    md = re.sub(r"(?m)^## ", "#### ", md)
    return "**Supplementary File S3.** Deviations from the registered protocol (OSF, https://doi.org/10.17605/OSF.IO/Z63BS)\n\n" + md.strip()


# ------------------------------------------------------------------------------------------------------------- S4

def s4() -> str:
    log = json.loads((RUN / "search_log.json").read_text(encoding="utf-8"))
    dd = json.loads((RUN / "dedup_report.json").read_text(encoding="utf-8"))
    rc = json.loads((RUN / "recall_seed_set.json").read_text(encoding="utf-8"))
    ch = json.loads((CHASE / "chase_log.json").read_text(encoding="utf-8"))
    b = log["_blocks"]
    L = ["**Supplementary File S4.** Search strategies, dates and results per source (PRISMA-S), de-duplication, "
         "seed-set recall, citation searching and the use of AI tools", "",
         "#### S4.1 Sources, interfaces, dates and records", "",
         f"Search started {(RUN / 'started_utc.txt').read_text().strip()[:16].replace('T', ' ')} UTC, after "
         "registration at 13:36 UTC. "
         f"Publication years from {b['from_year']}. No language or document-type limits in the queries; no search "
         "filters; no study registries searched; no authors contacted. The strategy was not peer reviewed with PRESS; "
         f"it was validated against a seed set of {rc['seed_studies']} known eligible studies (recall "
         f"{rc['in_screening_list']}/{rc['seed_studies']}).", ""]
    L += table(["Source", "Interface and fields", "Searched (UTC)", "Records"],
               [[SOURCES[k][0], SOURCES[k][1], log[k]["searched_at_utc"][:16].replace("T", " "), f"{log[k]['records']:,}"]
                for k in SOURCES] + [["Total", "", "", f"{dd['records_total']:,}"]])
    L += ["", "#### S4.2 Term blocks", "",
          "Arm A = block 1 (generative LLM) AND block 2 (human agreement) AND block 3 (psychological or clinical). "
          "Arm B = block 1 AND block 4 (psychological coding constructs). A record entered screening only if its title "
          "or abstract matched all blocks of an arm as exact phrases, a rule applied identically to every source.", ""]
    for key, name in [("llm", "Block 1, generative LLM"), ("human", "Block 2, human agreement"),
                      ("psy", "Block 3, psychological or clinical"), ("coding_constructs", "Block 4, coding constructs")]:
        L += [f"*{name}* ({len(b[key])} terms): " + "; ".join(b[key]), ""]
    L += [f"*Crossref queries* ({len(b['crossref_queries'])}): " + "; ".join(b["crossref_queries"]), "",
          f"*PsyArXiv title words*: " + "; ".join(b["psyarxiv_words"]), "",
          "#### S4.3 Query strings as sent", "",
          "Exactly as recorded in search/runs/2026-10-21/search_log.json (long lists were sent in chunks; each chunk is "
          "listed).", ""]
    for k in SOURCES:
        meta = {x: v for x, v in log[k]["meta"].items() if x in ("query", "filters", "queries", "words")}
        L += [f"*{SOURCES[k][0]}*", "", "```", json.dumps(meta, ensure_ascii=False, indent=1)[:20000], "```", ""]
    auto = dd["auto_removed_non_study_records"] + dd["auto_removed_no_search_term_match"]
    L += ["#### S4.4 De-duplication and automatic removal", "",
          f"{dd['records_total']:,} records → {dd['unique_records']:,} unique ({dd['duplicates_removed']:,} duplicates removed "
          "by DOI, arXiv ID, PubMed ID and normalised title with year; search/dedup.py). "
          f"{dd['pointer_or_component_records_attached']:,} pointer or component records (e.g., figure or supplement DOIs) "
          f"were attached to their parent record. {dd['auto_removed_non_study_records']:,} non-study records (datasets, "
          f"software, registrations) and {dd['auto_removed_no_search_term_match']:,} records whose title and abstract did "
          f"not match an arm were removed automatically, leaving {dd['unique_records'] - auto:,} records for screening.", "",
          "#### S4.5 Seed-set recall", "",
          f"All {rc['seed_studies']} seed studies were in the screening list; {rc['eligible_found']} of {rc['eligible_drafts']} "
          "seed studies judged eligible were retrieved (search/runs/2026-10-21/recall_seed_set.json).", "",
          "#### S4.6 Citation searching (protocol §9; deviation D6)", "",
          f"Run {ch['run_at_utc'][:16].replace('T', ' ')} UTC. Backward and forward citations of every eligible full-text "
          "report, the five syntheses named in the protocol and two further reviews, via OpenAlex (references and cited-by) "
          f"and Semantic Scholar (reference lists). New unique records: {ch['new_unique_records']:,}; removed "
          f"automatically by the same rules as S4.4: {ch['new_unique_records'] - ch['to_screen']:,}; screened: "
          f"{ch['to_screen']:,} (search/runs/2026-10-23-citations/).", "",
          "#### S4.7 AI tools", "",
          "All AI steps ran through the Claude Code command-line interface in headless mode (`claude -p`) with a fixed "
          "system prompt and a JSON output schema (harness/llmaudit/judge.py); each output line records the model, the "
          "prompt hash and the time. Model training on the inputs was switched off. Every decision on eligibility was "
          "made by the author (R1); every number was checked against the source text by script (Method 2.5–2.6).", ""]
    L += table(["Step", "Model (effort)", "Prompt (frozen at git tag)", "Output in the repository", "Human role"], [
        ["Title/abstract screening, 5,852 records, two independent passes", "Claude Opus 5.5 and Claude Sonnet 5.5 (high)",
         "screening/llm_screener_prompt.md (llm-coder-agreement-prereg-v1.0)", "screening/llm/2026-10-21_*.jsonl (+ SHA-256)",
         "R1 calibrated 400 records blind, screened 1,000 directly (D3) and decided every record kept by either pass"],
        ["Citation records, 225, two passes", "Claude Opus 5.5 and Claude Sonnet 5.5 (high)", "same prompt",
         "screening/llm/chase_2026-10-23_*.jsonl", "R1 decided every record kept by either pass"],
        ["Full-text eligibility proposals with statistics and quotes", "Claude Opus 5.5 (high) for 209 reports; Claude "
         "Sonnet 5.5 (medium) for 557 + 17 reports (D5)", "fulltext/ft_prompt.md (llm-coder-agreement-ft-prompt-v1.0)",
         "fulltext/llm/*.jsonl", "R1 decided every report"],
        ["Moderators, risk of bias, statistic codes", "Claude Sonnet 5.5 (medium)",
         "extraction/complete_prompt.md (llm-coder-agreement-extraction-prompt-v1.0)",
         "extraction/draft/complete_2026-10-23.jsonl", "R1 reviewed all studies; corrections in extraction/r1_corrections.py (D8)"],
        ["Code, figures, tables, manuscript skeleton, language editing", "Claude Opus 5.5 (Claude Code)", "–",
         "all scripts in the repository", "R1 wrote and approved the text"]])
    return "\n".join(L)


# ------------------------------------------------------------------------------------------------------------- S5

PRISMA = [
    ("Title", "1", "Identify the report as a systematic review", "Title"),
    ("Abstract", "2", "Structured abstract (PRISMA 2020 for Abstracts)", "Abstract"),
    ("Introduction", "3", "Rationale", "1"),
    ("", "4", "Objectives", "1.1"),
    ("Methods", "5", "Eligibility criteria and grouping for the syntheses", "2.2, 2.3"),
    ("", "6", "Information sources, with dates", "2.4; S4.1, S4.6"),
    ("", "7", "Full search strategies", "S4.2–S4.3"),
    ("", "8", "Selection process, reviewers, automation tools", "2.5; S4.7"),
    ("", "9", "Data collection process, automation tools", "2.6; S4.7; S3 (D7, D8)"),
    ("", "10a", "Outcomes sought", "2.8"),
    ("", "10b", "Other variables", "2.6, 2.7; forms/extraction_codebook.md"),
    ("", "11", "Risk of bias assessment", "2.7; S1"),
    ("", "12", "Effect measures", "2.8"),
    ("", "13a", "Which studies were eligible for each synthesis", "2.8, 2.9"),
    ("", "13b", "Data preparation (missing statistics, conversions)", "2.6, 2.8"),
    ("", "13c", "Tabulation and display", "2.9; Tables 1–4; Figures 1–4"),
    ("", "13d", "Synthesis methods, model, software", "2.9"),
    ("", "13e", "Exploring heterogeneity", "2.9 (G2–G10)"),
    ("", "13f", "Sensitivity analyses", "2.9"),
    ("", "14", "Reporting bias assessment", "2.9 (small-study effects; G9 selective reporting)"),
    ("", "15", "Certainty assessment", "2.9 (GRADE)"),
    ("Results", "16a", "Study selection, flow diagram", "3.1; Figure 1"),
    ("", "16b", "Studies that seemed eligible but were excluded", "3.1; repository fulltext/decisions/"),
    ("", "17", "Study characteristics", "3.2; Table 1; S1"),
    ("", "18", "Risk of bias in studies", "3.7; S1"),
    ("", "19", "Results of individual studies", "S1; repository forms/estimates.csv"),
    ("", "20a", "Characteristics and risk of bias of contributing studies", "3.2, 3.7"),
    ("", "20b", "Results of all syntheses", "3.3, 3.4; Table 2; Figures 2–3"),
    ("", "20c", "Investigations of heterogeneity", "3.5, 3.6; Table 3; Figure 4; S6"),
    ("", "20d", "Sensitivity analyses", "3.8; Table 4; S6"),
    ("", "21", "Reporting biases", "3.5 (G9), 3.8"),
    ("", "22", "Certainty of evidence", "3.9; Table 2"),
    ("Discussion", "23a", "Interpretation in the context of other evidence", "4.1–4.4"),
    ("", "23b", "Limitations of the evidence", "5"),
    ("", "23c", "Limitations of the review processes", "5"),
    ("", "23d", "Implications for practice, policy and research", "4.5, 6"),
    ("Other information", "24a", "Registration", "2.1; Abstract; Declarations"),
    ("", "24b", "Access to the protocol", "2.1 (OSF)"),
    ("", "24c", "Amendments to the protocol", "2.10; S3"),
    ("", "25", "Support", "Declarations (Funding)"),
    ("", "26", "Competing interests", "Declarations"),
    ("", "27", "Availability of data, code and other materials", "Declarations; repository"),
]
PRISMA_S = [
    ("1", "Database name", "2.4; S4.1"), ("2", "Multi-database searching", "S4.1"),
    ("3", "Study registries", "not searched (S4.1)"), ("4", "Online resources and browsing", "none (S4.1)"),
    ("5", "Citation searching", "2.4; S4.6"), ("6", "Contacts", "none (S4.1)"), ("7", "Other methods", "none"),
    ("8", "Full search strategies", "S4.2–S4.3"), ("9", "Limits and restrictions", "S4.1 (years from 2020)"),
    ("10", "Search filters", "none (S4.1)"), ("11", "Prior work", "2.4 (seed set); protocol §10"),
    ("12", "Updates", "none"), ("13", "Dates of searches", "2.4; S4.1, S4.6"),
    ("14", "Peer review", "not peer reviewed; seed-set recall (S4.1, S4.5)"),
    ("15", "Total records", "3.1; Figure 1; S4.1"), ("16", "Deduplication", "S4.4"),
]
REGEMA = [
    ("Title", "1", "Title", "Title (inter-rater agreement; meta-analysis)"),
    ("Abstract", "2", "Abstract", "Abstract"),
    ("Introduction", "3", "Background", "1"), ("", "4", "Objectives", "1.1"),
    ("Method", "5", "Selection criteria", "2.2"), ("", "6", "Search strategies", "2.4; S4"),
    ("", "7", "Data extraction", "2.6; S1; repository forms/"),
    ("", "8", "Reported reliability (types of coefficients, separate syntheses)", "2.8"),
    ("", "9", "Reliability induction and other sources of bias",
     "induction not applicable: reports without LLM–human agreement were ineligible (2.2); other bias: 2.7, 2.9 (G9)"),
    ("", "10", "Data extraction of inducing studies", "not applicable"),
    ("", "11", "Reliability of data extraction", "2.5, 2.6; S3 (D7, D8); 5"),
    ("", "12", "Transformation method", "2.8 (kappa raw; Fisher z for ICC and r)"),
    ("", "13", "Statistical model", "2.9 (CHE, CR2)"), ("", "14", "Weighting method", "2.9 (inverse-variance CHE weights)"),
    ("", "15", "Heterogeneity assessment", "2.9 (τ², ω², multilevel I², prediction interval)"),
    ("", "16", "Moderator analyses", "2.9"), ("", "17", "Additional analyses", "2.9"),
    ("", "18", "Software", "2.9"),
    ("Results", "19", "Results of the study selection process", "3.1; Figure 1 (induction rates not applicable)"),
    ("", "20", "Mean reliability and heterogeneity", "3.3; Table 2; Figure 2"),
    ("", "21", "Moderator analyses", "3.4–3.6; Table 3; Figures 3–4; S6"),
    ("", "22", "Sensitivity analyses", "3.8; Table 4; S6"),
    ("", "23", "Comparison of inducing and reporting studies", "not applicable"),
    ("", "24", "Data set", "S1; repository forms/"),
    ("Discussion", "25", "Summary of results", "4.1–4.4"), ("", "26", "Limitations", "5"),
    ("", "27", "Implications for practice", "4.5"), ("", "28", "Implications for future research", "4.5, 6"),
    ("Funding", "29", "Funding and conflicts of interest", "Declarations"),
    ("Protocol", "30", "Protocol", "2.1; Declarations"),
]


def s5() -> str:
    L = ["**Supplementary File S5.** Reporting checklists with the location of each item", "",
         "Locations are section numbers of the manuscript, tables, figures and Supplementary Files S1–S6. Item topics are "
         "abbreviated; full wording in Page et al. (2021), Rethlefsen et al. (2021) and Sánchez-Meca et al. (2021).", "",
         "#### S5.1 PRISMA 2020", ""]
    L += table(["Section", "Item", "Topic", "Location"], [list(r) for r in PRISMA])
    L += ["", "#### S5.2 PRISMA-S (literature search)", ""]
    L += table(["Item", "Topic", "Location"], [list(r) for r in PRISMA_S])
    L += ["", "#### S5.3 REGEMA (reliability generalization meta-analyses)", "",
          "The 'scale' of REGEMA corresponds here to the human coding scheme applied by an LLM; reliability is LLM–human "
          "agreement on the same units, benchmarked against human–human agreement.", ""]
    L += table(["Section", "Item", "Topic", "Location"], [list(r) for r in REGEMA])
    return "\n".join(L)


# ------------------------------------------------------------------------------------------------------------- S6

def s6() -> str:
    mods = rows(RES / "moderators.csv") + rows(RES / "g3_release.csv")
    L = ["**Supplementary File S6.** Additional analyses (kappa family unless stated)", "",
         "#### S6.1 All moderator models", "",
         "CHE meta-regression, CR2 robust tests with Satterthwaite degrees of freedom; one row per coefficient (reference "
         "level omitted). Levels supported by fewer than three studies were dropped; models with fewer than 10 studies "
         "were not fitted. Unreliable: df < 4. Omnibus: robust Wald test of all coefficients of the moderator.", ""]
    L += table(["Moderator", "Studies", "Estimates", "Studies per level", "Term", "b [95% CI]", "df", "p", "Reliable",
                "Omnibus F (p)"],
               [[r["moderator"], r["k_studies"], r["k_estimates"], r.get("studies_per_level", ""), r["term"],
                 f"{num(r['b'])} [{num(r['ci_lb'])}, {num(r['ci_ub'])}]", num(r["df"], 1), pval(r["p"]), r["reliable"],
                 f"{num(r.get('wald_F'))} ({pval(r.get('wald_p'))})" if r.get("wald_F") not in (None, "", "NA") else "–"]
                for r in mods])
    sens = rows(RES / "sensitivity.csv")
    L += ["", "#### S6.2 Sensitivity analyses", ""]
    L += table(["Analysis", "Studies", "Estimates", "κ [95% CI]", "95% PI", "τ² study / estimate"],
               [[r["analysis"], r["k_studies"], r["k_estimates"], f"{num(r['est'])} [{num(r['ci_lb'])}, {num(r['ci_ub'])}]",
                 f"[{num(r['pi_lb'])}, {num(r['pi_ub'])}]", f"{num(r['tau2_study'], 3)} / {num(r['tau2_estimate'], 3)}"]
                for r in sens])
    loo = rows(RES / "leave_one_out.csv")
    lo, hi = min(loo, key=lambda r: float(r["est"])), max(loo, key=lambda r: float(r["est"]))
    L += ["", "#### S6.3 Leave-one-study-out", "",
          f"Removing each of the {len(loo)} studies in turn, pooled κ ranged from {num(lo['est'], 3)} (without "
          f"{lo['left_study']}) to {num(hi['est'], 3)} (without {hi['left_study']}); all 95% CIs lay between "
          f"{num(min(float(r['ci_lb']) for r in loo))} and {num(max(float(r['ci_ub']) for r in loo))} "
          "(analysis/results/leave_one_out.csv).", "",
          "#### S6.4 Small-study effects", ""]
    L += table(["Subset", "Studies", "Slope on SE", "p (CR2)"],
               [[TT.get(r["subset"], r["subset"]), r["k_studies"], num(r["slope_se"]), pval(r["p"])]
                for r in rows(RES / "small_study_effects.csv")])
    se = rows(RES / "kappa_se_sources.csv")
    lab = {"CI": "from the reported confidence interval", "n and observed p_e": "from n and the observed chance agreement",
           "n and imputed p_e": "from n and the median chance agreement of the other estimates (0.4853)"}
    L += ["", "#### S6.5 Source of the standard error of each kappa estimate", ""]
    L += table(["SE derived", "Estimates"], [[lab.get(r["se_source"], r["se_source"]), r["n"]] for r in se])
    g1 = rows(RES / "g1_delta_kappa.csv")
    L += ["", "#### S6.6 Human benchmark (Δκ = LLM–human κ − human–human κ on the same units)", ""]
    L += table(["Analysis", "Studies", "Estimates", "Δκ [95% CI]", "90% CI", "Within ±0.10"],
               [[r["analysis"], r["k_studies"], r["k_estimates"], ci95(r),
                 f"[{num(r['ci90_lb'])}, {num(r['ci90_ub'])}]" if r.get("ci90_lb") not in (None, "", "NA") else "–",
                 {"TRUE": "yes", "FALSE": "no"}.get(r.get("equivalent_within_0.10"), "–")] for r in g1])
    return "\n".join(L)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.mkdir(exist_ok=True)
    for name, f in [("S1_studies", s1), ("S2_models", s2), ("S3_deviations", s3), ("S4_search", s4),
                    ("S5_checklists", s5), ("S6_analyses", s6)]:
        text = f().rstrip() + "\n"
        (OUT / f"{name}.md").write_text(text, encoding="utf-8", newline="\n")
        print(f"{name}.md: {len(text):,} characters")


if __name__ == "__main__":
    main()
