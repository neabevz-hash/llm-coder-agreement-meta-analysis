# Регистрация на OSF: пошагово и тексты полей

Шаблон — **Generalized Systematic Review Registration** (v6 на OSF; van den Akker et al., 2023, https://doi.org/10.1186/s13643-023-02281-7), тот же, что у мизофонии, ИИ-зависимости и ставок: 61 текстовое поле, все обязательные, и 2 поля для файлов. Тексты ниже на английском, вставляются как есть. Названия полей совпадают с формой. Числа — из проверочного прогона `search/runs/2026-10-21-ab-check/` и пилота промпта (`screening/pilot/`).

## Шаги

1. **Проект.** https://osf.io → *Create new project*:
   - Title: `Agreement between large language models and human experts in coding and rating psychological and clinical text: systematic review and meta-analysis`;
   - Storage location: любое.
2. **Файлы.** В *Files → OSF Storage* загрузите из `registration/osf_package/`:
   - `Rekhert_llm_coder_agreement_protocol_v1.0.pdf` — протокол;
   - `llm-coder-agreement-prereg-v1.0.zip` — весь пакет: протокол, формы, скрипты поиска и отбора, промпт скринера, эталонный набор, логи проверочного прогона и пилота;
   - `llm_screener_prompt.md` и `extraction_codebook.md` — отдельно, для полей с файлами.
3. **Регистрация.** *Registrations* → *New registration* → **Generalized Systematic Review Registration** → *Create draft*.
4. **Метаданные:** Title — как у проекта; Description — ниже; Category — *Project*; License — *CC-By Attribution 4.0 International*; Subjects — *Social and Behavioral Sciences → Psychology → Clinical Psychology* и *Social and Behavioral Sciences → Psychology → Quantitative Psychology*; Tags — ниже; Contributors — только вы.
5. **Поля формы** — по разделам ниже. Файлы: `llm_screener_prompt.md` (Screening → после *Screener instructions*), `extraction_codebook.md` (Extraction → после *Extractor instructions*).
6. **Отправка.** *Review* → *Register* → **Make registration public immediately**.
7. **Мне:** ссылку и DOI. Я впишу их в протокол и README; после этого — финальный поиск и калибровка вслепую.

---

## Metadata

**Description.** Protocol (v1.0) of a systematic review and multilevel meta-analysis of agreement between large language models (LLMs) and human experts when coding and rating psychological and clinical text. Agreement (Cohen's or Fleiss' kappa; ICC and correlations for rating scales, pooled separately) is pooled overall and for four task types — codebook coding, scoring of psychological assessments, clinical ratings of risk and severity, and LLM-as-a-judge evaluation of responses in mental-health conversations — and compared with human–human agreement on the same units. Moderators include model release date and reasoning models, prompting, number of categories, construct type, reference standard and language; an equivalence test (±0.10 kappa) asks whether models released in 2025–2026 agree with experts as well as experts agree with each other. Two AI passes (Claude Opus 5.5 and Claude Sonnet 5.5) draft screening labels; the author decides every record either pass keeps and every full text, and verifies every AI-drafted extraction value; a blind calibration sample of 400 records measures the miss rate of double AI exclusions. The files contain the protocol, forms, search and de-duplication code, the frozen screener prompt, the seed set and the check-run and pilot logs.

**Tags.** large language models; LLM-as-a-judge; inter-rater reliability; kappa; content analysis; qualitative coding; psychological assessment; psychotherapy; mental health; meta-analysis; reliability generalization; systematic review

---

## Review Methods

**Type of review**
Systematic review and multilevel meta-analysis of agreement coefficients (reliability-generalisation type), with a correlated-and-hierarchical-effects model and cluster-robust inference. The protocol follows PRISMA-P 2015; the review will be reported per PRISMA 2020, PRISMA-S and the REGEMA checklist. Risk of bias: five domains adapted from QUADAS-2 for rater-agreement studies. Certainty: GRADE adapted for agreement estimates. Full protocol: Rekhert_llm_coder_agreement_protocol_v1.0.pdf in this project.

**Review stages**
Preparation (novelty check, protocol, seed set, check run of the search, pilot of the screener prompt) → Registration (OSF) → Final search → Title/abstract screening: blind calibration by the reviewer on 400 random records, two independent AI passes on all records, reviewer decision on every record that either pass keeps, conditional blind screening of double AI exclusions → Full-text screening (AI proposal, reviewer decision) → Pilot extraction on five studies (prompts and forms frozen; any change logged) → Extraction and risk of bias (AI draft, reviewer verification of every value) → Synthesis → Reporting.

**Current review stage**
Protocol frozen on 21 October 2026 (v1.0, git tag llm-coder-agreement-prereg-v1.0); the files uploaded here are built from that tag. A check run of the frozen search code ran on 21 October 2026 (29,682 records, 6,551 to screen, recall 23 of 23 on the seed set) and the screener prompt was piloted on 103 records with known labels. No final search, screening decision, full-text assessment, extraction or analysis has been done.

**Start date**
2026-10-21 (novelty check).

**End date**
Not fixed in advance.

**Background**
Large language models are increasingly used in psychology and psychiatry to do work that used to require trained human coders: applying codebooks to interviews and open-ended responses, coding therapist and client behaviour in session transcripts, scoring psychological assessments with open responses, rating suicide risk or symptom severity in clinical text, and judging the safety and quality of responses in mental-health conversations. Primary studies justify LLM coding with agreement statistics against human coders, with values from near zero to above human–human agreement. No meta-analysis pools these values for psychological and clinical text. Existing syntheses cover essay scoring (Li, H., et al., 2025, descriptive; Li, S., 2026, registered meta-analysis), qualitative analysis without pooling (Seyler et al., 2025: 39 studies, median kappa .74), LLM-as-a-judge in health care without pooling (Li, L., et al., 2026), and diagnostic accuracy of LLMs against diagnoses rather than against human coders of the same text (Leung et al., 2026; Fisher et al., 2026). The closest registered review (Webb et al., 2026, OSF j6589) pools AI–human kappa for deductive coding of qualitative data across fields; it excludes assessment scoring, clinical records, rating scales and LLM-as-a-judge, and does not separate psychological constructs.

**Primary research question(s)**
(RQ1) How strongly do LLMs agree with human experts when coding and rating psychological and clinical text (chance-corrected agreement, kappa), overall and for four task types: codebook coding, assessment scoring, clinical state rating, and helper-response evaluation (LLM-as-a-judge)? (RQ2) How does LLM–human agreement compare with human–human agreement on the same units?

**Secondary research question(s)**
Moderators: model release date and generation, reasoning models, within-study contrasts of newer vs older models, prompting (zero-shot, few-shot, chain-of-thought, fine-tuned), number of categories, manifest vs latent constructs, reference standard (single coder vs consensus), code prevalence, selective reporting of the best configuration, language, open vs closed weights, human expertise, real vs synthetic texts, data contamination, publication type and year. Secondary outcome: ICC and correlations for rating scales. Open question: direction of LLM errors in clinical ratings and safety judgements (over- vs under-rating).

**Expectations / hypotheses**
G1 (primary): on average LLM–human agreement is lower than human–human agreement; for models released in 2025–2026 the difference lies within ±0.10 kappa (equivalence, 90% CI; the author expects negligible differences for current models). G2: higher human–human agreement goes with higher LLM–human agreement. G3 (primary): agreement increases with model release date; within studies newer models agree better than older ones; reasoning models agree at least as well as non-reasoning models. G4: agreement is higher for manifest categories than for latent constructs and clinical judgements. G5: few-shot prompting or fine-tuning yields higher agreement than instructions alone. G6: agreement decreases with the number of categories. G7: agreement is higher against a consensus reference than against a single coder. G8: low-prevalence codes show low kappa despite high percentage agreement. G9: studies reporting only the best of several configurations show higher agreement. G10: agreement is lower for non-English texts. Findings outside these questions will be labelled post hoc. Context: the author is a clinical psychology student; one study by the author (an LLM judge validated against human coders on grief-support chatbot dialogues) may be eligible and is excluded in a sensitivity analysis.

**Dependent variable(s) / outcome(s) / main variables**
Chance-corrected agreement between an LLM and the human reference on the same units: Cohen's kappa (Fleiss' kappa for several coders jointly; weighted kappa for ordinal scales, coded), on the original scale; Krippendorff's alpha and Gwet's AC1 in the kappa family with a type code. Benchmark: human–human kappa on the same units, used as matched within-study differences. Secondary: ICC and Pearson or Spearman correlations on Fisher's z. Percentage agreement, F1 and accuracy are tabulated, not pooled (percentage agreement is pooled on the logit scale only to test G8).

**Independent variable(s) / intervention(s) / treatment(s)**
The index rater is a generative (decoder) LLM — GPT-3 and later, Claude, Gemini, Llama, Mistral, Qwen, DeepSeek and others — prompted or fine-tuned, alone or in an agent pipeline. Encoder-only models and classical machine learning are not eligible.

**Additional variable(s) / covariate(s)**
Per study: task type (T1–T4), construct and construct type, scheme, number of categories, unit, number of units, text type and source (real or synthetic; dataset and release year), language, human coders (number, expertise, independence), reference type, human–human agreement. Per LLM configuration: model, version, family, release date, reasoning, open weights, parameters, prompting, examples, codebook in prompt, temperature, runs, run date, tuned on evaluation units, all configurations reported. Risk-of-bias domains 1–5.

**Software**
Python 3.12 (PubMed E-utilities, Europe PMC, OpenAlex, Semantic Scholar, arXiv, OSF, Crossref, DataCite and CORE APIs; de-duplication; calibration sampling; decision files) — search/search.py, search/dedup.py, search/recall.py, screening/*.py. Claude Code in headless mode running Claude Opus 5.5 (claude-opus-5-5) and Claude Sonnet 5.5 (claude-sonnet-5-5) for AI draft labels and drafts (screening/llm_screen.py; the version is stored with every output). R 4.6.1 with metafor and clubSandwich. Publish or Perish for Google Scholar. git. Windows 11.

**Funding**
None. The review is unfunded.

**Conflicts of interest**
None. The AI assistant used as a tool is produced by Anthropic, whose models may be among those evaluated in included studies; the author has no relationship with Anthropic beyond a paid subscription. Anthropic models are analysed like any other model family.

**Overlapping authorships**
One study by the author (validation of an LLM judge against human coders on grief-support chatbot dialogues, submitted to Death Studies in 2026) may be eligible. If included, it is extracted by the same procedure, flagged, and excluded in a sensitivity analysis.

---

## Search Strategy

**Databases**
PubMed; Europe PMC (MEDLINE, PMC and preprints from medRxiv, Research Square, PsyArXiv, SSRN, Preprints.org); OpenAlex (Crossref corpus, ACL Anthology, repositories, theses); Semantic Scholar (computer science and ACL Anthology); arXiv; PsyArXiv (OSF API); Crossref (posted content, proceedings); DataCite (theses, OSF, Zenodo, figshare); CORE. No access to Scopus, Web of Science, PsycINFO or the ACM Digital Library.

**Interfaces**
PubMed — NCBI E-utilities; Europe PMC — REST API (searchPOST); OpenAlex — API (title_and_abstract.search); Semantic Scholar — Graph API bulk search; arXiv — API (abs: fields); PsyArXiv — OSF API v2 preprints; Crossref — REST API (query.bibliographic, sorted by score); DataCite — REST API; CORE — API v3; Google Scholar — Publish or Perish.

**Grey literature**
Preprints (arXiv, PsyArXiv, medRxiv, Research Square, SSRN) through the arXiv API, the OSF API, Europe PMC and OpenAlex; conference papers (ACL Anthology venues, CHI, CSCW and others) through OpenAlex, Semantic Scholar and Crossref; theses through OpenAlex, DataCite and CORE; Google Scholar (first 200 results of two queries, searched by the author with Publish or Perish).

**Inclusion and exclusion criteria**
Inclusion: (I1) written or transcribed text (transcripts, open-ended responses, narratives, diaries, social-media posts, crisis chats, clinical notes, responses of chatbots or human helpers; synthetic texts coded); (I2) a psychological or clinical construct (mental states, emotions, cognitions, behaviour, interpersonal processes, personality, psychopathology, risk, well-being, psychotherapy processes, or scoring rules of a psychological instrument); (I3) a generative LLM as rater; (I4) at least one human coder applying the same scheme to the same units; (I5) a unit-level agreement statistic or data to compute it (kappa family, alpha, AC1, ICC, correlation, percentage agreement, F1 or accuracy against human labels, confusion matrix); (I6) any language and publication status, from 2020. Exclusion: (E1) humans rate LLM outputs and no LLM rates the same units; (E2) an external criterion as reference (diagnosis, the writer's own questionnaire score, outcome); (E3) no psychological or clinical construct (medical coding, grading of subject knowledge, generic sentiment, stance, hate speech, misinformation); (E4) agreement only between themes or summaries, no unit-level statistic; (E5) LLM–LLM agreement only, or encoder-only models or classical machine learning only; (E6) reviews, protocols, commentaries; (E7) duplicate reports (linked).

**Query strings**
Two arms in title and abstract, 2020 onwards. Arm A = block 1 (LLM) AND block 2 (human comparison and agreement) AND block 3 (psychological and clinical). Arm B = block 1 AND block 4 (psychological coding constructs). Block 1: large language model(s), LLM(s), LLM-based, ChatGPT, GPT, GPTs, GPT-3, GPT-3.5, GPT-4, GPT-4o, GPT-5, generative AI, generative artificial intelligence, generative pre-trained/pretrained transformer(s), foundation model(s). Block 2: inter-rater, interrater, inter-coder, intercoder, inter-annotator, kappa, Krippendorff, Gwet, intraclass; agreement with or between humans, experts or clinicians; human coder(s), rater(s), annotator(s), expert(s), evaluators, judgements, labels, annotations, ratings; expert annotations, ratings, raters, coders; expert-annotated, human-annotated, manually annotated, manually coded, manual coding, manual annotation, gold standard, clinician ratings, trained coders; LLM-as-a-judge, LLM judge(s), LLM evaluator(s); automated coding, automated scoring, automatic scoring, deductive coding, codebook(s). Block 3: 84 psychological and clinical terms (psychology, psychiatric, psychotherapy, counseling, mental health, depression, anxiety, suicide, trauma, emotion, personality, empathy, therapist, motivational interviewing, crisis, distress, psychosis, attachment, reflective functioning, cognitive distortion, projective, Rorschach, narrative, qualitative, interview, open-ended responses, free-text responses, divergent thinking and others). Block 4: 56 coding constructs (cognitive distortions, maladaptive schemas, mental manipulation, motivational interviewing, change talk, MITI, MISC, therapeutic alliance, counseling conversations and sessions, therapy and psychotherapy transcripts, clinical, psychiatric and diagnostic interviews, PTSD and depression severity, suicide risk, C-SSRS, psychiatric functioning, defense mechanisms, projective tests, sentence completion, reflective functioning, adult attachment interview, autobiographical memory, divergent thinking, empathy detection, emotion regulation strategies, therapist and counselor behaviors, counseling skills, treatment fidelity and others). Exact lists and strings per source are generated by search/search.py and stored in search_log.json. OpenAlex, Semantic Scholar, arXiv and DataCite: blocks 3 and 4 split into chunks because of URL length, results united. PubMed: (A) OR (B) in [tiab], two-word phrases as proximity [tiab:~2]. Europe PMC: the same with TITLE_ABS. PsyArXiv: OSF API with LLM words in title or description, arms checked locally. Crossref: 12 queries sorted by score, records kept when title or abstract matches an arm. CORE: LLM × agreement query, records kept when title or abstract matches an arm. Google Scholar: "large language model" "inter-rater" psychology; "LLM-as-a-judge" "mental health" clinicians.

**Search validation procedure**
Recall is checked against an independent seed set drafted from the reference lists of six syntheses (Seyler et al., 2025; Gierbolini-Rivera et al., 2026; Hua et al., 2025; Kempny et al., 2026; Na et al., 2025; Li, L., et al., 2026): 476 references screened, 23 seed studies (22 eligible, 1 unclear) confirmed by the author (search/seed_set.csv). With arm A only, recall was 13 of 22; arm B was added after examining the nine misses (benchmark papers that evaluate an LLM against human-labelled data without naming human coders in the abstract). The check run of the v1.0 code (21 October 2026) found 23 of 23 (search/runs/2026-10-21-ab-check/recall_seed_set.json). Misses in the final search, if any, are examined one by one.

**Other search strategies**
Backward and forward citation searching of included studies and of the syntheses listed in the protocol, through OpenAlex.

**Procedures to contact authors**
Authors are not contacted (the author's decision, as in the author's previous reviews). Studies without extractable statistics are listed as such.

**Results of contacting authors**
Not applicable.

**Search expiration and repetition**
If more than six months pass between the final search and submission, the search is updated with the same code; only new records are screened, by the same procedure. No living review is planned.

**Search strategy justification**
Agreement statistics often sit in tables of papers whose abstracts do not name them, and benchmark papers describe human-labelled datasets without naming human coders; arm A requires a human-comparison term, arm B requires a specific coding construct instead. OpenAlex and Semantic Scholar stem and match loosely, so records go to screening only if their title and abstract match an arm as exact phrases (de-duplication rule 6: 5,586 records removed in the check run). Without subscription databases, coverage relies on large open indexes, arXiv and conference proceedings, which hold most of the computer-science literature on this topic.

**Miscellaneous search strategy details**
All automated searches run from search/search.py, which logs query strings, dates, record counts and timings (search_log.json). De-duplication (search/dedup.py, from the author's earlier reviews) merges records on DOI (ignoring version suffixes), PMID and exact normalised title with years within ±1; rule 2b merges a preprint (arXiv or PsyArXiv DOI) with its published version of the same title; pointer-source records are attached to database records; records that every source types as a non-study record are removed (633 in the check run), and so are records without an exact search-term match (rule 6).

---

## Screening

**Screening stages**
(1) De-duplication by script. (2) Title and abstract: before seeing any AI label, the reviewer (R1, the author) screens 400 records blind, drawn with random.Random(20261022).sample over the sorted record IDs; the decisions are committed before any AI label is shown. Two AI passes (Claude Opus 5.5 and Claude Sonnet 5.5, same frozen prompt) label every record include / unsure / exclude with a reason code; SHA-256 hashes of both label files are committed before unblinding. R1 decides every record that at least one pass labelled include or unsure. Records that both passes labelled exclude are excluded; if, in the calibration sample, both passes excluded a record that R1 labelled include or unsure, R1 screens blind the double-excluded records that contain both an LLM term and a human-comparison term in title or abstract, plus a seeded random audit of 300 of the other double exclusions. (3) Full text: the AI drafts a proposal per report (eligible or not, primary exclusion reason, task type, location of the agreement statistics); R1 decides each report.

**Screened fields / blinding**
Title, abstract, year, venue, record type, language and DOI link are visible at title/abstract screening; author names are not shown. AI labels are hidden during the calibration and during the conditional blind screening.

**Used exclusion criteria**
Title/abstract stage: (1) review, protocol, commentary, position paper or guideline; (2) humans rate LLM outputs and the LLM codes nothing; (3) the reference is an external criterion (diagnosis, self-report of the writer, outcome); (4) no psychological or clinical construct; (5) no generative LLM, or LLM–LLM agreement only; (6) another task (themes or summaries without unit-level coding, generation or patient simulation without rating, systematic-review automation, not about LLMs); (7) other, with a note. Full-text stage: the criteria above, one primary reason per report.

**Screener instructions**
The AI screener's fixed prompt and JSON schema are in screening/llm_screener_prompt.md (attached). R1 applies the same eligibility criteria with the rule "when in doubt, unsure".

**Screening reliability**
One human screener (R1) and two AI passes. In the calibration sample: Cohen's kappa, Gwet's AC1 and PABAK between R1 (blind) and each pass and their union; sensitivity and specificity of the double-exclusion rule against R1 with Clopper–Pearson 95% CIs. Also reported: R1's overrides by direction, whether the safeguard was triggered, and how many included studies either pass had labelled exclude. Because the review is about LLMs as coders, these figures are also reported as a descriptive result in the paper.

**Screening reconciliation procedure**
There is no second human. R1 resolves every difference between the AI labels and their own judgement against the record (and the full text when needed); R1's decision is final.

**Sampling and sample size**
All eligible studies are included. Only the calibration sample is sampled: 400 records by the seeded procedure above. A pooled estimate requires at least three studies; moderators are tested when at least ten studies inform them.

**Screening procedure justification**
Single-reviewer screening misses about 13% of eligible studies on average (Waffenschmidt et al., 2019); LLM screeners reach high sensitivity on titles and abstracts (Oami et al., 2024). With about 6,500 records, a human check of every AI exclusion would multiply the reviewer's load without changing who decides inclusion: every record kept by either pass and every full text is decided by the reviewer. Two independent passes lower the chance of a miss, and the blind calibration measures the miss rate of the double-exclusion rule.

**Data management and sharing**
Search records, raw exports of the final search, R1's decision files (Markdown, with git history) and parsed decisions (CSV), both AI label files with model, prompt hash and Claude Code version (JSONL), and the list of double AI exclusions with reasons are released on GitHub with a Zenodo DOI at submission, under CC BY 4.0 (records of third parties excepted).

**Miscellaneous screening details**
R1 screens in Markdown files generated by screening/screen_md.py: one block per record with a decision line (+ include, ? unsure, -1 to -7 exclude with a reason, = accept the AI label shown when both passes agree). Each file is committed blank before R1 starts and again when R1 finishes.

---

## Extraction

**Entities to extract**
Four linked tables (forms/extraction_codebook.md): studies (report identifiers, publication status, field, task type, construct and construct type, scheme, number of categories, unit, number of units, text type and source, dataset, language, human coders and expertise, independence, reference type, risk of bias), estimates (one row per LLM configuration × task × human reference × statistic: model, version, family, release date, reasoning, open weights, parameters, prompting, examples, codebook in prompt, temperature, runs, run date, tuned on evaluation units, all configurations reported, statistic, value, CI or SE, observed and chance agreement, prevalence, confusion matrix, mean ratings), human reliability (human–human agreement on the same units, matched to estimates), and per-code values for the prevalence analysis.

**Extraction stages**
(1) Pilot on five studies; extraction prompt and forms frozen; any rule added goes to deviations.md. (2) The AI pre-fills every field with its source location; the draft is stored unchanged. (3) R1 verifies every value against the source.

**Extractor instructions**
forms/extraction_codebook.md (attached; piloted on five studies before use) defines the four tables, fields and rules.

**Extractor masking**
None; masking is not feasible in a single-author review. Construct type (manifest or latent) is coded from code definitions before the agreement results are read.

**Extraction reliability**
One human extractor (R1) verifying an AI draft of every value. Reported: the share of AI values R1 corrected, overall and for key fields (statistic, value, n units, categories, model, reference), and the share of AI quotes found verbatim in the source.

**Extraction reconciliation procedure**
R1 resolves every difference between the AI draft and the source by checking the source; R1's value is final. Ambiguous values are coded NR with a note.

**Extraction procedure justification**
Single-author review without a second human extractor: pre-filling by the AI with a source location for every value and verification of every value by R1 gives each number two independent looks.

**Data management and sharing**
AI drafts (JSON), verified tables (CSV) and risk-of-bias ratings are released on GitHub with a Zenodo DOI at submission, under CC BY 4.0. No embargo.

**Miscellaneous extraction details**
Unknown values are coded NR, not applicable NA. Retractions and expressions of concern are checked through Crossref. Model release dates come from developers' announcements and are kept in forms/model_releases.csv.

---

## Synthesis and Quality Assessment

**Planned data transformations**
Kappa on its original scale. SE from reported CIs, otherwise from SE = sqrt(po(1 − po) / (n(1 − pe)^2)) (Cohen, 1960); pe = (po − kappa)/(1 − kappa) when only kappa and po are given; when only kappa and n are given, pe is imputed from the median of comparable estimates and flagged. Confusion matrices are used to recompute kappa, PABAK and AC1. Per-code kappas without an overall value are averaged (unweighted), with the SE of the mean approximated under a between-code correlation of 0.5. Matched within-study differences Δkappa = kappa(LLM–human) − kappa(human–human), SE = sqrt(SE1^2 + SE2^2). ICC and correlations on Fisher's z. Release dates as years since June 2020.

**Missing data**
Authors are not contacted. Estimates without enough information for an SE are tabulated, not pooled. Missing moderator values are coded NR; moderator analyses use the studies with data, and the number is reported. No imputation except the flagged pe imputation above, removed in a sensitivity analysis.

**Data validation**
Key numbers are always checked against the source table; scripts check that kappa ≤ 1, that n is consistent, and that recomputed kappa from confusion matrices matches reported values within 0.02; duplicate evaluations across reports (arXiv and published versions) are linked; retractions and expressions of concern are checked through Crossref; influential estimates are examined with leave-one-out and influence diagnostics.

**Quality assessment**
Five domains adapted from QUADAS-2 (Whiting et al., 2011) for rater-agreement studies (forms/rob.md): unit selection; LLM configuration (tuned on evaluation units; only the best configuration reported); human reference (training, independence, blindness to LLM output, reported reliability); data contamination (evaluation data public before the model's training cutoff); reporting (model version, run date, settings, prompt). Rated low / high / unclear with quotes; no summary score; domains enter as moderators and sensitivity filters. Certainty: GRADE adapted for agreement estimates.

**Synthesis plan**
Correlated-and-hierarchical-effects model on kappa (random effects for studies and for estimates within studies, assumed within-study correlation 0.6) with CR2 cluster-robust standard errors and small-sample corrections (metafor::rma.mv, clubSandwich). Reported: pooled kappa with 95% CI and 95% prediction interval, variance components and I² per level, numbers of studies and estimates. RQ1: overall and by task type. RQ2/G1: the same model on matched Δkappa; G1a supported if pooled Δkappa < 0; G1b (equivalence) for models released from 2025-01-01: the 90% CI of pooled Δkappa within ±0.10 (two one-sided tests). G2: meta-regression of LLM–human kappa on human–human kappa. G3: release date (continuous) and generation (categories), reasoning models, and pooled within-study contrasts of newer vs older models on the same units. G4–G10: one moderator at a time (construct type, prompting, log number of categories, reference type, prevalence on the per-code subset, best-only reporting and risk-of-bias domain 2, English vs other languages). Pooling needs at least three studies; moderators at least ten studies; robust tests with fewer than four approximate degrees of freedom are reported as unreliable. Secondary: the same models on Fisher's z for ICC and correlations. Open question: standardised mean differences of LLM vs human ratings or the share of disagreements in which the LLM rated higher, pooled when at least five studies report it.

**Criteria for conclusions / inference criteria**
Estimates are interpreted with 95% CIs and prediction intervals; Landis and Koch labels are used only as descriptions. G1b uses the equivalence margin of ±0.10 kappa with 90% CIs. Moderator tests are two-sided at α = .05 with robust (HTZ) tests and are interpreted with their estimates; exploratory and post hoc analyses are labelled as such. Certainty of each main estimate is stated with GRADE.

**Synthesist blinding**
None. The synthesist is the author. The analysis plan is fixed in this registration before any data are extracted.

**Synthesis reliability**
One synthesist (the author). The analysis code is drafted by the AI assistant, checked by the author, and released; all results are reproducible from the released data and code.

**Synthesis reconciliation procedure**
Not applicable (one synthesist).

**Publication bias analyses**
Funnel plots per task type; an Egger-type test with the SE of kappa as a moderator in the multilevel model with CR2 inference (Rodgers & Pustejovsky, 2021); "best configuration only" and publication type as moderators; selective reporting within studies (models or codes named in the methods but missing from results) recorded.

**Sensitivity analyses / robustness checks**
(1) Excluding imputed SEs; (2) excluding weighted kappa; excluding alpha and AC1; (3) only peer-reviewed reports; (4) only matched comparisons for Δkappa, then adding unmatched ones; (5) within-study correlation 0.3 and 0.8; between-code correlation 0.2 and 0.8; (6) one estimate per study (the most recent model with the authors' primary configuration), standard random-effects model with Hartung–Knapp correction; (7) excluding high contamination risk; excluding synthetic texts; (8) excluding the author's own study; (9) leave-one-study-out and influence diagnostics.

**Synthesis procedure justification**
Studies usually report several estimates (models, prompts, references) on the same units; the correlated-and-hierarchical-effects model with robust variance estimation uses all of them without double-counting (Pustejovsky & Tipton, 2022). Kappa is analysed on its original scale, as in reliability-generalisation meta-analyses (REGEMA; Sánchez-Meca et al., 2021). Human–human agreement on the same units is the natural benchmark, because agreement depends on the difficulty of the task.

**Synthesis data management and sharing**
R scripts, their outputs, sessionInfo and the analysis data (CSV) are released on GitHub with a Zenodo DOI at submission, under open licences (code MIT, data CC BY 4.0). No embargo.

**Miscellaneous synthesis details**
Every change to this plan after registration is dated, justified and logged in deviations.md, and reported in the paper. The AI assistant's role is disclosed in the Methods and in the AI declaration.
