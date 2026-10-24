# Agreement between large language models and human coders on psychological and clinical text: data and code

This repository contains the records, decisions, coded data and analysis code for

> Rekhert, M. (2026). *Agreement between large language models and human coders on psychological and clinical text: A systematic review and multilevel meta-analysis* [Manuscript submitted for publication]. Preprint: https://doi.org/10.5281/zenodo.23613737

- Protocol (OSF Registries, registered 21 October 2026 before the final search and screening): https://doi.org/10.17605/OSF.IO/Z63BS
- Archived release (Zenodo): https://doi.org/10.5281/zenodo.23613757
- Author: Martin Rekhert, Higher School of Psychology, Turan University, Almaty, Kazakhstan (ORCID [0009-0001-2402-2031](https://orcid.org/0009-0001-2402-2031))

## The review in brief

- **Question.** How closely do generative large language models (LLMs) agree with human coders on psychological and clinical text, in four task types — codebook coding (T1), assessment scoring (T2), clinical state rating (T3) and LLM-as-a-judge in mental health (T4) — and does LLM–human agreement reach human–human agreement on the same units?
- **Search.** 21 October 2026: PubMed, Europe PMC, OpenAlex, Semantic Scholar, arXiv, PsyArXiv, Crossref, DataCite and CORE, publication years from 2020; 29,171 records, 12,786 unique, 6,852 screened. Citation searching 23 October 2026 (OpenAlex and Semantic Scholar): 9,248 new records, 225 screened.
- **Selection.** One reviewer (the author, R1) made every decision. R1 calibrated 400 records blind and screened 1,000 records directly; two AI passes (Claude Opus 5.5 and Claude Sonnet 5.5 through Claude Code 2.1.289, fixed prompt, JSON output) labelled the other 5,852, and R1 decided every record kept by either pass. Full texts (open access only, 766 of 1,256 retrieved; 17 of 70 from citation searching) were decided by R1 with an AI eligibility proposal visible.
- **Coding.** The statistics come from the full-text proposals, each with its location and a verbatim quote; one AI pass added moderators and risk of bias; R1 reviewed the coding of every study, and every value was checked against the source text by script (deviations D7, D8).
- **Included.** 418 eligible reports → 377 studies (416 reports); 107 studies with 595 kappa-family estimates, 95 studies with ICC or correlations.
- **Analysis.** Correlated-and-hierarchical-effects models (`metafor`) with cluster-robust CR2 inference (`clubSandwich`), kappa on its raw scale, ICC and correlations as Fisher z; human benchmark Δκ on the same units with an equivalence test; preregistered moderators G2–G10; GRADE.
- **Main results.** Pooled kappa 0.62 (95% CI 0.58–0.65; prediction interval 0.15–1.00); ICC and correlations 0.71. In 23 studies with human–human agreement on the same units, Δκ = −0.11 (−0.18 to −0.03); models from 2025–2026 were not equivalent to human coders within ±0.10. No change with model release date; agreement tracked human reliability. Certainty low to very low.

## Repository layout

All study files are under `papers/llm-coder-agreement-meta/`.

| Path | Contents |
| --- | --- |
| `protocol.md` | Protocol v1.0 (frozen 21 October 2026, git tag `llm-coder-agreement-prereg-v1.0` in the working repository; registered on OSF) |
| `deviations.md` | Every change after registration, dated (D1–D8; Supplementary File S3) |
| `registration/` | The OSF registration form text and the script that built the registration package |
| `search/` | Search, de-duplication, recall and citation-searching scripts; `runs/2026-10-21/`: search log with every query, raw exports (zip), unique records, screening list (CSV, RIS), recall on the seed set; `runs/2026-10-23-citations/`: citation searching; the two `-check` runs are the pre-registration check runs (D1) |
| `screening/` | AI screening prompt and runner, the pilot, both AI passes with the SHA-256 of the label files, R1's blind calibration and direct screening (D3), verification worksheets and final decisions (`decisions/tiab_final.csv`) |
| `fulltext/` | Retrieval scripts and log (open access only), full-text prompt and runner, AI proposals (`llm/`), R1's worksheets and decisions (`decisions/ft_R1.csv`, `decisions/ft_R1_chase.csv`), PRISMA counts |
| `extraction/` | Study map (reports → studies), statistics from the full-text proposals (`ft_estimates.csv`), the completion prompt and its drafts (`draft/`), R1's review applied as code (`r1_corrections.py`), model registry rules (`models.py`), `finalize.py`; the v0.1 extraction prompt (`extract_prompt.md`) was used only in the pilot |
| `forms/` | Extraction codebook, risk-of-bias rules, and the analysis tables `studies.csv`, `tasks.csv`, `estimates.csv`, `human_reliability.csv`, `model_releases.csv` |
| `analysis/` | `analysis.R` (all analyses), `prisma.R`, `figures.R`, `tables.py`; `results/` and `figures/` as reported |
| `manuscript/` | Tables 1–4 (`tables.md`), Table S1 (`supplement_S1_studies.csv`) and Supplementary Files S1–S6 (`make_supplement.py` → `supplement/`) |
| `harness/` | `llmaudit`: the Claude Code runner used for the AI passes, agreement statistics |

Reviewer worksheets (`*.md` under `screening/`, `fulltext/decisions/`, `extraction/verify/`) have instructions in Russian, the reviewer's working language; records, AI outputs and decisions are in English, and every decision is also in a CSV file.

Not included: full texts and PDFs of the reports (copyright), API keys.

## Reproducing the analysis

The analysis runs from the released files and needs no API access. Tested with Python 3.12 and R 4.6.1 (metafor, clubSandwich, dplyr, readr, tidyr, jsonlite, ggplot2).

```bash
# coded drafts + R1's review -> analysis tables (forms/*.csv)
python papers/llm-coder-agreement-meta/extraction/finalize.py --name complete_2026-10-23
# meta-analysis -> analysis/results/; flow diagram and figures -> analysis/figures/
Rscript papers/llm-coder-agreement-meta/analysis/analysis.R
Rscript papers/llm-coder-agreement-meta/analysis/prisma.R
Rscript papers/llm-coder-agreement-meta/analysis/figures.R
# Tables 1-4, Table S1 and Supplementary Files S1-S6
python papers/llm-coder-agreement-meta/analysis/tables.py
python papers/llm-coder-agreement-meta/manuscript/make_supplement.py
```

Run the commands from the repository root. The release was checked by running them in a clean copy: the analysis tables, all result files, Tables 1–4 and Supplementary Files S1–S6 came out identical (line endings aside).

Re-running the search, retrieval or the AI passes needs network access and keys (`.env.example`): `OPENALEX_API_KEY` and `CORE_API_KEY` for the search, and `CLAUDE_CODE_OAUTH_TOKEN` (output of `claude setup-token`) for the Claude Code runs. Python packages for those steps: `httpx`, `lxml`, `pyyaml`, `jsonschema`, `pymupdf` (`pip install -e harness`).

## Licenses and citation

Code (`*.py`, `*.R`, `harness/`): MIT (`LICENSE`). Data and documents: CC BY 4.0 (`LICENSE-DATA.md`); bibliographic records, abstracts and quotations from the included reports remain with their copyright holders. Please cite the article and this repository (`CITATION.cff`).
