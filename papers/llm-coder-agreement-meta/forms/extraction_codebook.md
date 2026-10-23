# Data extraction codebook (v1.0, frozen with protocol v1.0; piloted on five studies before use, any change logged in `deviations.md`)

Four linked tables (protocol §11c–§13). `studies.csv` has one row per study (all its reports linked). `estimates.csv` has one row per LLM configuration × task × human reference × statistic. `human_reliability.csv` has one row per human–human agreement value on the same units. `codes.csv` holds per-code κ with prevalence for G8, only from studies that report them (up to 30 codes per study). Unknown = `NR`; not applicable = `NA`. Template: `papers/ai-dependence-correlates/forms/extraction_codebook.md`.

**Procedure.**
- The AI assistant pre-fills every field from the full text and gives, for every value, the source location (page, table, figure) and a short verbatim quote. The draft is stored unchanged in `extraction/draft/<study_id>.json`.
- R1 verifies every field against the source and accepts or corrects it (`extraction/verify_md.py`, from the misophonia review).
- **[K]** marks key fields: R1 always checks them against the source table.
- Reported: share of AI values corrected (overall and [K]); share of AI quotes found verbatim (`quote_check.py`).

## studies.csv

| Field | Rule |
| --- | --- |
| `study_id` | `ST###` |
| `report_ids` | `rec_id`s of all reports (arXiv version, conference or journal version, thesis), `;`-separated; the most complete supplies the data |
| `first_author`, `year`, `doi`, `arxiv` | of the main report |
| `pub_status` | journal / conference (peer-reviewed proceedings, ACL Anthology) / preprint / thesis / other |
| `field` | psychology / psychiatry-medicine / computer-science-NLP / public-health / education / other (authors' main field) |
| `own_study` | yes if R1 is an author (protocol §3c), else no |
| `task_type` **[K]** | T1 codebook coding / T2 assessment scoring / T3 clinical state rating / T4 helper-response evaluation (protocol §8); a study with two task types gets two `study_id`s sharing `report_ids` |
| `construct` | free text, e.g., "change talk (MISC)", "suicide risk level (C-SSRS)", "Rorschach MOR" |
| `construct_type` **[K]** | manifest (presence of explicit content: topic, named behaviour, explicit emotion word) / latent (inference about an unobservable state or quality: risk, severity, defence, empathy, competence). Coded from the code definitions in the paper, before reading the agreement results |
| `scheme` | codebook or instrument name and source (e.g., MISC 2.5, C-SSRS, Exner CS) |
| `n_categories` **[K]** | number of categories or scale points of the reference scheme; multi-code schemes: number of codes and categories per code |
| `unit` | utterance / post / response / segment / transcript / session / document |
| `n_units` **[K]** | units coded by both the LLM and the humans |
| `text_type` | therapy-session / clinical-interview / clinical-note / social-media / crisis-chat / open-ended-response / narrative / qualitative-interview / chatbot-response / other |
| `text_source` | real / synthetic / mixed |
| `dataset` | public dataset name and release year, or own data |
| `language` | language of the texts (ISO 639-1); several: `MULTI` + list |
| `human_coders_n` | number of human coders on the evaluation units |
| `human_expertise` **[K]** | clinician-or-expert / trained-coder / crowd / mixed / NR |
| `human_independent` | humans coded independently of LLM output: yes / no / NR |
| `reference_type` **[K]** | single-coder / each-of-several / consensus-or-adjudicated / majority-vote / NR |
| `rob_1` … `rob_5` | low / high / unclear (`rob.md`), each with a quote in the draft |
| `notes` | |

## estimates.csv

| Field | Rule |
| --- | --- |
| `estimate_id` | `E####` |
| `study_id` | link |
| `model_name` **[K]** | as reported, with version or snapshot (e.g., gpt-4o-2024-08-06, Claude 3.5 Sonnet, Llama-3-70B-Instruct) |
| `model_family` | GPT / o-series / Claude / Gemini-PaLM / Llama / Mistral / Qwen / DeepSeek / other |
| `release_date` | release date of that model or snapshot (developer announcement; table in `forms/model_releases.csv`, built during extraction) |
| `reasoning_model` | yes (o1, o3, DeepSeek-R1, extended-thinking modes and similar) / no |
| `open_weights` | yes / no |
| `params_b` | parameters in billions if published, else NR |
| `prompting` **[K]** | zero-shot / few-shot / chain-of-thought / fine-tuned / retrieval-augmented / agent-or-ensemble (several allowed, `;`) |
| `n_examples` | few-shot examples in the prompt |
| `codebook_in_prompt` | full definitions / labels only / NR |
| `temperature`, `n_runs` | as reported |
| `run_date` | date or month of the LLM runs, if reported |
| `tuned_on_eval` | configuration chosen on the evaluation units: yes / no (separate development set) / NR |
| `all_configs_reported` | yes / no (only the best of several) / single configuration |
| `reference` **[K]** | which human reference this estimate compares with (consensus, coder A, mean over coders…) |
| `statistic` **[K]** | cohen_kappa / fleiss_kappa / weighted_kappa_linear / weighted_kappa_quadratic / krippendorff_alpha / gwet_ac1 / pabak / icc (+ form) / pearson / spearman / percent_agreement / f1_macro / f1_micro / f1_weighted / accuracy / precision / recall |
| `value` **[K]** | as reported (proportions, not percentages) |
| `ci_low`, `ci_high`, `se` | as reported |
| `p_o`, `p_e`, `prevalence` | observed and chance agreement, minority-class prevalence, if reported or computable |
| `confusion_matrix` | LLM × human counts as `a,b;c,d` (2×2) or JSON for larger tables, if reported |
| `per_code_mean` | yes if `value` is the unweighted mean of per-code values (protocol §13), with `n_codes` |
| `mean_llm`, `mean_human`, `sd_llm`, `sd_human` | for T3–T4 ordinal ratings (open question on error direction) |
| `source_location` | page, table or figure |

## human_reliability.csv

| Field | Rule |
| --- | --- |
| `hr_id` | `H###` |
| `study_id` | link |
| `same_units` **[K]** | yes if computed on the same units as the LLM estimates; partial; no |
| `comparison` **[K]** | coder-vs-coder / coder-vs-consensus / mean-pairwise |
| `statistic`, `value`, `ci_low`, `ci_high`, `se`, `n_units` | as in `estimates.csv` |
| `matched_estimate_ids` | estimates with which this value forms a matched Δκ pair (protocol §13) |

## codes.csv (only for G8)

| Field | Rule |
| --- | --- |
| `study_id`, `estimate_id` | links |
| `code` | code name as in the paper |
| `kappa`, `percent_agreement`, `prevalence`, `n_units` | per code, as reported |
