# Protocol: Agreement between large language models and human experts in coding and rating psychological and clinical text — a systematic review and multilevel meta-analysis

**Version 1.0, frozen 2026-10-21** (git tag `llm-coder-agreement-prereg-v1.0`), before registration, before the final search and before any screening decision. Structured by PRISMA-P 2015 (Moher et al., 2015); item numbers in brackets. To be registered on OSF with the Generalized Systematic Review Registration form (van den Akker et al., 2023); PROSPERO does not register methodological reviews of this kind. Templates: `papers/ai-dependence-correlates/protocol.md` v1.0 and `papers/sports-betting-prevalence/protocol.md` v1.0. Novelty check: `novelty/novelty.md`; journals: `journals/journals.md`. Every reference was verified by DOI or arXiv ID (Crossref, DataCite, arXiv API) on 2026-10-21 (`novelty/refs_verified.json`).

Decisions of the author (R1) on 2026-10-21: the topic is taken with the scope "psychological and clinical text, four task types"; target journal Clinical Psychology & Psychotherapy (Comprehensive Review), then Computers in Human Behavior, then Behavior Research Methods; the research questions and hypotheses below were agreed as drafted.

**Changes from draft v0.1 (all on 2026-10-21, before registration).**

1. Search: arm B (LLM × psychological coding constructs) added after arm A alone found 13 of 22 eligible seeds; block 1 extended with GPT, GPTs and "pretrained" variants, block 2 with "deductive coding" and "codebook(s)"; "open-ended" alone replaced by specific phrases (§10).
2. De-duplication: rule 2b (a preprint merges with its published version of the same title) and rule 6 (exact-term consistency) added (§10, §11a).
3. Seed set confirmed by R1: 23 studies, 22 eligible and one unclear (§9).
4. The screener prompt was piloted on 103 records with known labels and frozen without changes (§11b; `screening/llm_screener_prompt.md`).
5. Load for R1 updated from the check run and the pilot.

---

## Administrative information

**[1] Title.** Agreement between large language models and human experts in coding and rating psychological and clinical text: a systematic review and multilevel meta-analysis.

**[2] Registration.** OSF Registries, Generalized Systematic Review Registration form, before the final search and before screening (R1 registers). Registered on 2026-10-21 at 13:36 UTC: https://osf.io/z63bs, DOI 10.17605/OSF.IO/Z63BS (public, CC BY 4.0); the four registered files match the package built from tag `llm-coder-agreement-prereg-v1.0` (SHA-256), and the 61 text fields match `registration/osf.md`.

**[3a] Author and contact.** Martin Rekhert, MA student in clinical psychology, Turan University, Almaty, Kazakhstan. ORCID 0009-0001-2402-2031. mrexert@gmail.com.

**[3b] Contributions.** Single author (R1): conceptualisation, eligibility decisions at every stage, data extraction, risk-of-bias appraisal, interpretation, final manuscript. An AI assistant (Claude Opus 5.5, Anthropic, run through Claude Code; Claude Sonnet 5.5 as the second screening pass) is used as a tool for the tasks in §9–§11 and §15: search code, de-duplication, draft screening labels, draft full-text decisions, draft extraction and risk-of-bias ratings, analysis code and text drafts. It is disclosed in the Methods and in the AI declaration. Every AI output is a draft; R1 checks each against the source and decides. Because the review is about LLMs as coders, the AI assistant's own agreement with R1 at each stage is reported as a secondary, descriptive result.

**[3c] Conflict of the author's own work.** R1's audit of grief-support chatbots (submitted to *Death Studies*, 2026) validated an LLM judge against human coders on clinically relevant dialogues and may be eligible. If included, it is extracted by the same procedure, flagged, and excluded in a sensitivity analysis.

**[4] Amendments.** Any change after registration is dated, justified and logged in `deviations.md`, and reported in the registration and in the paper.

**[5] Support.** No funding, no sponsor, no conflicts of interest.

---

## Introduction

**[6] Rationale.**

Large language models (LLMs) are increasingly used in psychology and psychiatry to do work that used to require trained human coders: applying codebooks to interview transcripts and open-ended responses, coding therapist and client behaviour in session transcripts, scoring psychological assessments with open responses, rating suicide risk or symptom severity in clinical text, and judging the safety and quality of responses in mental-health conversations ("LLM-as-a-judge"). Records that combine an LLM term, a human-agreement term and a psychological or clinical term grew from about 110 in 2024 to about 270 in 2025 and more than 500 in the first ten months of 2026 (`novelty/volume.json`). Most primary studies justify LLM coding with an agreement statistic against human coders, but the values range from near zero to above human–human agreement and depend on the task, the model, the prompt and how agreement is computed (Gilardi et al., 2023; Ziems et al., 2024; Baumann et al., 2025; Kunilovskaya et al., 2026; Goodall et al., 2026).

No meta-analysis pools these values for psychological and clinical text. Syntheses of LLM–human agreement exist for essay scoring (Li, H., et al., 2025, descriptive; Li, S., 2026, registered multilevel meta-analysis) and for qualitative analysis (Seyler et al., 2025, 39 studies, medians only; median κ = .74). A scoping review of LLM-as-a-judge in health care reports medians without pooling (Li, L., et al., 2026). Meta-analyses in mental health pool diagnostic accuracy of LLMs against diagnoses or self-reports, not agreement with human coders of the same text (Leung et al., 2026; Fisher et al., 2026). The closest registered review (Webb et al., 2026, OSF j6589) will pool AI–human κ for deductive coding of qualitative data across education, health, business and the social sciences. It excludes assessment scoring, clinical records, rating scales and LLM-as-a-judge evaluation, and does not separate psychological constructs. A narrower registration covers NLP of psychotherapy transcripts (Biba et al., PROSPERO CRD420251146504).

A pooled, task-specific estimate matters for three groups: psychologists who want to know whether an LLM can replace or support a second coder; clinicians and developers who use LLMs to rate risk or to evaluate mental-health chatbots; and methodologists, because agreement depends on whether it is compared with how well humans agree with each other on the same material (Goodall et al., 2026; Liu et al., 2026).

**[7] Objectives.**

Review question:

- **Units:** texts produced by people (or simulated to represent them) in psychological and clinical contexts (§8).
- **Index rater:** a generative LLM that codes or rates the texts.
- **Reference:** one or more human coders or raters applying the same scheme to the same units.
- **Outcome:** agreement between the LLM and the human reference (§13); human–human agreement on the same units as a benchmark.

Research questions (estimation):

- **RQ1.** How strongly do LLMs agree with human experts when coding and rating psychological and clinical text (chance-corrected agreement, κ), overall and separately for four task types: codebook coding, scoring of psychological assessments, clinical ratings of the person's state, and evaluation of helper responses (LLM-as-a-judge)?
- **RQ2.** How does LLM–human agreement compare with human–human agreement on the same units?

Hypotheses (directional; G1 and G3 are the primary hypotheses, the others secondary):

- **G1. Human ceiling.** On average, LLM–human agreement is lower than human–human agreement (Δκ < 0). For models released in 2025–2026, the difference is within ±0.10 κ (equivalence; R1 expects differences for current models to be negligible).
- **G2. Shared difficulty.** The higher the human–human agreement on a task, the higher the LLM–human agreement.
- **G3. Model generations.** Agreement increases with the model's release date; within studies, newer models agree better than older ones; reasoning models agree at least as well as non-reasoning models.
- **G4. Task and construct.** Agreement is higher for manifest categories than for latent constructs and clinical judgements (risk, severity, projective scoring).
- **G5. Prompting.** Few-shot prompting or fine-tuning yields higher agreement than instructions alone.
- **G6. Categories.** Agreement decreases with the number of categories or scale points.
- **G7. Reference.** Agreement is higher against a consensus of several humans than against a single coder.
- **G8. Rare codes.** Low-prevalence codes show low κ despite high percentage agreement; percentage agreement overstates agreement (Feinstein & Cicchetti, 1990).
- **G9. Selective reporting.** Studies that report only the best of several configurations show higher agreement than studies that report all configurations.
- **G10. Language.** Agreement is lower for non-English texts.
- **Open question (no direction).** In clinical ratings and safety judgements, do LLMs err towards over-rating (stricter than humans) or under-rating (more lenient)?

Findings not covered by these questions are reported as post hoc and labelled as such.

---

## Methods

### [8] Eligibility criteria

**Study designs.** Any empirical study, including benchmark and dataset papers, that applies a generative LLM and at least one human coder to the same text units with the same coding or rating scheme and reports a quantitative agreement statistic, or data from which one can be computed.

**Inclusion criteria.**

- **I1. Text.** Written or transcribed language: interview and session transcripts, open-ended survey or test responses, narratives, diaries, social-media and forum posts, crisis chats, clinical notes, and responses of chatbots or human helpers. Synthetic texts that represent people (simulated patients, synthetic posts) are eligible and coded. Multimodal input is eligible when it includes the text or transcript.
- **I2. Psychological or clinical construct.** The categories or scale describe mental states, emotions, cognitions, behaviour, interpersonal processes, personality, psychopathology, risk (suicide, self-harm, violence), well-being, or psychological treatment processes (fidelity, therapist skills, alliance), or they are the scoring rules of a psychological assessment instrument.
- **I3. Index rater.** A generative (decoder) LLM, prompted or fine-tuned, alone or within an agent pipeline: GPT-3 and later, Claude, Gemini, Llama, Mistral, Qwen, DeepSeek and others.
- **I4. Reference.** At least one human coder or rater (expert, clinician, trained coder, or crowd worker; coded) applied the same scheme to the same units.
- **I5. Statistic.** A unit-level agreement statistic between the LLM and the human reference: Cohen's or Fleiss' κ (unweighted or weighted), Krippendorff's α, Gwet's AC1, ICC, Pearson or Spearman correlation, percentage agreement, F1 or accuracy against human labels, or a confusion matrix.
- **I6.** Any language; any publication status (journal article, conference paper including ACL Anthology venues, preprint, thesis); published from 2020 (GPT-3) to the search date.

**Exclusion criteria.**

- **E1.** Humans rate LLM outputs and no LLM rates the same units with the same scheme (the LLM is the object, not the rater).
- **E2.** The reference is an external criterion, not human coding of the text: diagnosis, the writer's questionnaire score, behaviour or outcome. This is criterion validity, not coder agreement.
- **E3.** No psychological or clinical construct: medical coding (ICD, adverse events, radiology, oncology notes), grading of subject knowledge, generic sentiment of products or opinions, stance, hate speech, misinformation, political or marketing categories.
- **E4.** Agreement only at the level of themes or summaries (inductive coding compared by semantic similarity), with no unit-level statistic.
- **E5.** LLM–LLM agreement only; encoder-only models (BERT, RoBERTa) and classical machine learning only. When a study also reports a generative LLM, only its estimates are used.
- **E6.** Reviews, protocols, editorials, commentaries.
- **E7.** Duplicate reports of the same evaluation; reports are linked and the most complete supplies the data.

**Task types (primary moderator; R1 assigns from an AI draft).**

| Type | What the LLM does | Examples |
| --- | --- | --- |
| T1 codebook coding | assigns categorical codes from a fixed scheme to units (utterances, posts, responses, segments), any speaker | deductive qualitative codes; MISC or MITI behaviour codes; emotion or symptom presence in posts; cognitive-distortion types |
| T2 assessment scoring | applies the scoring manual of a psychological instrument to responses | Rorschach variables; AIHQ open responses; sentence completion; Adult Attachment Interview; reflective functioning; autobiographical specificity; divergent thinking |
| T3 clinical state rating | rates the level of risk, severity or functioning of the person who wrote or spoke the text | C-SSRS risk level in posts; distress or depression severity from interviews; PTSD severity from narratives |
| T4 helper-response evaluation (LLM-as-a-judge) | rates responses of chatbots, counsellors, peer supporters or therapists against a quality or safety rubric | suicide-risk response safety; empathy of responses; therapist interpersonal skills; therapy competence ratings |

### [9] Information sources

Turan University has no access to Scopus, Web of Science, PsycINFO or the ACM Digital Library. Coverage relies on open indexes, preprint servers and citation searching, as in the previous reviews:

- **PubMed**; **Europe PMC** (with medRxiv, Research Square, PsyArXiv, SSRN, Preprints.org); **OpenAlex** (Crossref corpus, ACL Anthology, repositories, theses); **Semantic Scholar** (computer science and ACL Anthology); **arXiv API** (cs.CL, cs.AI, cs.HC, cs.CY and others); **Crossref** (posted content and conference papers); **DataCite** (OSF, Zenodo, figshare, theses); **OSF API** (PsyArXiv preprints); **CORE**.
- **Backward and forward citation searching** of included studies and of the syntheses in §6 (Seyler et al., 2025; Li, L., et al., 2026; Hua et al., 2025; Na et al., 2025; Flathers et al., 2026), through OpenAlex.
- **Google Scholar:** two queries, the first 200 results each, retrieved by R1 with Publish or Perish (Google Scholar blocks automated access).

**Seed set.** Search recall is checked against an independent set of eligible primary studies taken from the reference lists of independent syntheses: Seyler et al. (2025; included studies resolved from its reference list via Crossref), Gierbolini-Rivera et al. (2026), Hua et al. (2025), Kempny et al. (2026; OpenAlex reference lists), Na et al. (2025) and Li, L., et al. (2026; Semantic Scholar reference lists) — 476 references in total (`search/seed_candidates.py` → `seed_candidates.csv`). The AI assistant drafts eligibility against §8 from titles and abstracts; R1 confirms each seed (`search/seed_set.csv`; confirmed on 2026-10-21: 23 studies, 22 eligible and one unclear; T1 14, T2 1, T3 3, T4 5). Recall is reported and misses are examined one by one.

### [10] Search strategy

Two arms in title and abstract, from 2020 to the search date, no language limits. Strings are reported per PRISMA-S (Rethlefsen et al., 2021); code: `search/search.py`; term lists are in the code and in `search_log.json` of every run.

- **Arm A** — three concept blocks combined with AND:
  1. **LLM:** large language model(s), LLM(s), LLM-based, ChatGPT, GPT, GPTs, GPT-3, GPT-3.5, GPT-4, GPT-4o, GPT-5, generative AI, generative artificial intelligence, generative pre-trained (pretrained) transformer(s), foundation model(s);
  2. **Human comparison and agreement:** inter-rater, interrater, inter-coder, intercoder, inter-annotator, kappa, Krippendorff, Gwet, intraclass; agreement with or between humans, experts or clinicians; human coder(s), rater(s), annotator(s), expert(s), evaluators, judgements, labels, annotations, ratings; expert annotations, ratings, raters and coders; expert-annotated, human-annotated, manually annotated, manually coded, manual coding, manual annotation, gold standard, clinician ratings, trained coders; LLM-as-a-judge, LLM judge(s), LLM evaluator(s); automated coding, automated scoring, automatic scoring, deductive coding, codebook(s);
  3. **Psychological and clinical:** psychology, psychological, psychologist, psychiatry, psychiatric, psychotherapy, psychotherapist, counseling, counselling, counselor, mental health, mental illness, depression, anxiety, suicide, suicidal, self-harm, trauma, PTSD, emotion(s), emotional, affective, personality, empathy, well-being, motivational interviewing, therapist(s), therapeutic, crisis, distress, loneliness, eating disorder, substance use, addiction, psychosis, schizophrenia, bipolar, autism, ADHD, attachment, mentalization, reflective functioning, cognitive distortion(s), defence mechanism, projective, Rorschach, sentence completion, narrative(s), qualitative, interview(s), open-ended responses or answers, open-ended survey or questionnaire, free-text responses or answers, divergent thinking.
- **Arm B** — block 1 AND block 4, **psychological coding constructs:** cognitive distortion(s), maladaptive schema(s), mental manipulation, motivational interviewing, change talk, sustain talk, MITI, MISC, therapeutic alliance, counseling conversation(s) or session(s), therapy session(s) or transcripts, psychotherapy transcripts or sessions, clinical, psychiatric or diagnostic interview(s), PTSD severity or assessment, depression severity, symptom severity, suicide or suicidal risk, C-SSRS, wellness dimensions, psychiatric functioning, defense mechanisms, psychological defenses, Rorschach, projective test(s) or technique, sentence completion, reflective functioning, adult attachment interview, autobiographical memory, divergent thinking, empathy detection or classification, emotion regulation strategies, psychological constructs, therapist or counselor behaviors, counseling skills, treatment or psychotherapy fidelity. Arm B catches benchmark papers that evaluate an LLM against human-labelled data without naming human coders or agreement statistics in the abstract.

| Source | Query form |
| --- | --- |
| OpenAlex | `title_and_abstract.search`, one filter per block; block 3 in three chunks and block 4 in two (URL length), results united |
| PubMed | (block 1 AND block 2 AND block 3) OR (block 1 AND block 4) in `[tiab]`; two-word phrases as proximity `[tiab:~2]` (PubMed drops quoted phrases missing from its phrase index) |
| Europe PMC | the same Boolean structure with `TITLE_ABS:` |
| Semantic Scholar | bulk search, chunked as in OpenAlex |
| arXiv | `abs:` fields, chunked as in OpenAlex |
| PsyArXiv | OSF preprints API with LLM words in title or description, then the two arms checked locally |
| Crossref | 12 relevance-sorted `query.bibliographic` queries, kept while the title or abstract matches an arm |
| DataCite | the blocks in titles and descriptions, chunked |
| CORE | LLM × agreement query; kept when the title or abstract matches an arm; CORE refuses offsets beyond about 1,100 for this query, so it stops there |

**Exact-term consistency (dedup rule 6).** OpenAlex and Semantic Scholar stem and match loosely. A unique record goes to screening only if its title and abstract match an arm as exact phrases (Unicode dashes read as hyphens); records without an abstract are kept when the title has an LLM term. Removed records are listed in `records_unique.jsonl`.

**Development of the strategy (2026-10-21; `search/runs/`).**

- **Arm A only** (`2026-10-21-check`; five sources): 9,566 unique records, 9,276 to screen without rule 6. Recall on the seed set: 13 of 22 eligible seeds. The nine misses were benchmark and clinical-NLP papers that evaluate an LLM against human-labelled data without naming human coders or agreement statistics in the abstract (cognitive distortions, maladaptive schemas, mental manipulation, MI client language, PTSD and psychiatric interviews, wellness dimensions). Arm B was added. A broad alternative (LLM × "dataset", "benchmark", "annotated", "F1" × psychological terms) would have returned about 44,000 records in OpenAlex alone and was not used.
- Rule 6 removed two seeds on the arm-A data: "GPTs" with a Unicode dash, and "deductive coding" without a human term. "GPT", "GPTs", "pretrained" variants, "deductive coding" and "codebook(s)" were added, and dashes are normalised. "Open-ended" alone was replaced by the specific phrases above, because it mostly retrieved evaluations of LLM answers to open-ended questions.
- **Arms A and B, check run of the v1.0 code** (`2026-10-21-ab-check`):

| Source | Records |
| --- | --- |
| OpenAlex | 11,158 |
| Semantic Scholar | 6,922 |
| DataCite | 4,863 |
| arXiv | 3,261 |
| Europe PMC | 1,468 |
| PubMed | 1,271 |
| Crossref | 305 |
| CORE | 249 |
| PsyArXiv | 185 |
| **Total** | **29,682** |

  - After de-duplication: 12,770 unique records. Removed automatically: 633 as non-study records, 5,586 under rule 6. **6,551 to screen**, 182 of them only through pointer sources.
  - **Recall on the seed set: 23 of 23** (22 eligible drafts and one unclear).

The final search runs with the v1.0 code after registration and before screening; dates, counts and software versions go to `search_log.json`.

### [11] Study records

**[11a] Data management.** As in the previous reviews: git repository with dated commits; de-duplication on DOI (version suffixes ignored), PMID and normalised title with years within ±1 (`search/dedup.py`, rules of the previous reviews). Rule 2b: when one of two records with the same title has a preprint DOI (arXiv 10.48550, PsyArXiv 10.31234), they merge, so that an arXiv paper and its conference or journal version are screened once; both DOIs are kept. Rule 6: exact-term consistency (§10). Linked versions of one study supply data from the most complete version. Data and code are released on GitHub with a Zenodo DOI at submission.

**[11b] Selection process.**

- **Title and abstract** — the scheme of the AI-dependence and sports-betting reviews.
  1. **Blind calibration.** Before seeing any AI label, R1 screens a seeded random sample of 400 records (include / unsure / exclude with a reason code). Decisions are committed before any AI label is shown.
  2. **AI draft, two passes.** Claude Opus 5.5 and Claude Sonnet 5.5, effort high, label every record independently with the same frozen prompt (`screening/llm_screener_prompt.md`): include / unsure / exclude, a reason code, a one-sentence note; "unsure" whenever in doubt. SHA-256 hashes of both label files are committed before unblinding. Before launch, the number of calls is stated to R1 and leftover runner processes are checked.
  3. **Verification.** R1 reviews, with AI labels visible, every record that at least one pass labelled include or unsure, and decides.
  4. **Safeguard.** If a calibration record that R1 kept was excluded by both passes, R1 screens blind the double-excluded records that contain both an LLM term and a human-comparison term in title or abstract, plus a random audit of 300 of the remaining double exclusions (variant of the sports-betting review, deviation D6 there).
  - **Reported:** κ, Gwet's AC1 and PABAK between R1 (blind) and each AI pass and their union; sensitivity and specificity with Clopper–Pearson 95% CIs; whether the safeguard triggered.
  - **Pilot of the prompt (2026-10-21).** Both passes labelled 103 records with known labels: the 23 seeds and the 80 manually labelled records of the novelty check (17 eligible, 6 unclear, 57 not eligible). The rule "exclude only if both passes exclude" kept all 23 seeds and all 23 eligible or unclear records (46/46; 95% CI 0.92–1.00) and excluded 49 of the 57 not eligible (0.86; 0.74–0.94); the eight kept negatives were borderline `unsure` labels. The prompt was frozen without changes (system-prompt hash `2a4c798c9c8114eb`); files: `screening/pilot/`, `screening/llm/pilot_*.jsonl`.
  - **Seeds.** The calibration sample is drawn with `random.Random(20261022).sample` over the sorted record IDs (`screening/calibration.py`); the AI passes use seed 20261022 for the order of records; the audit of 300 uses seed 20261023.
- **Full text.** Open-access versions (arXiv, ACL Anthology, PMC, Unpaywall, repositories); arXiv and ACL papers are all open. The AI drafts a proposal per report: eligible or not, primary exclusion reason, task type, and where the agreement statistics are (table, page, quote). R1 checks each proposal and decides. Reports without an open full text are listed as not retrieved.
- **AI prompts** for full text, extraction and risk of bias are piloted on five studies, frozen with git tags and committed before use.

**[11c] Data collection process.**

- **Forms.** Linked tables: `forms/studies.csv` (one row per study), `forms/estimates.csv` (one row per LLM configuration × task × human reference × statistic), `forms/human_reliability.csv` (human–human agreement on the same units), `forms/codes.csv` (per-code estimates for G8, only from studies that report per-code κ with prevalence, up to 30 codes per study). Codebook: `forms/extraction_codebook.md`.
- **AI draft and verification.** The AI pre-fills every field with its source location; R1 verifies every value, and always checks the statistic, n, the number of categories, the model and the reference against the source. The share of corrected values and of verbatim quotes is reported (`quote_check.py`).

### [12] Data items

Per study: report details and version; publication type; field of the authors; language of texts; text type and source (real or synthetic; public dataset or own data; release date of the dataset); construct and coding scheme; task type (T1–T4); construct type (manifest or latent, from the code definitions); number of categories or scale points; unit of coding; number of units; human coders (number, expertise: clinician or expert, trained coder, crowd; training; independence from LLM output); reference type (single coder, each of several coders, consensus or adjudicated); human–human agreement on the same units (statistic, value, n).

Per LLM configuration: model name and exact version; developer; open or closed weights; parameter count where known; release date (from the developer's announcement); reasoning model (yes/no); prompting (zero-shot, few-shot with number of examples, chain-of-thought, fine-tuned, retrieval-augmented, agent or ensemble); codebook definitions in the prompt; temperature and number of runs; date of the runs; whether the configuration was chosen on the evaluation units; whether all tested configurations are reported.

Per estimate: statistic and its type; value; CI or SE; n units; observed agreement and prevalence or the confusion matrix where reported; for ordinal ratings, mean ratings of LLM and humans (for the open question).

### [13] Outcomes and prioritisation

**Primary outcome.** Chance-corrected agreement between the LLM and the human reference on the same units: Cohen's κ; Fleiss' κ when the LLM is compared with several coders jointly; weighted κ for ordinal scales (coded).

- κ is analysed on its original scale (Sánchez-Meca et al., 2021).
- SE from the reported CI; otherwise from SE = √[pₒ(1 − pₒ) / (n(1 − pₑ)²)] (Cohen, 1960); when only κ and pₒ are given, pₑ = (pₒ − κ)/(1 − κ); when only κ and n are given, pₑ is imputed from the median of comparable estimates and flagged (sensitivity analysis). Confusion matrices are used to recompute κ, PABAK and AC1.
- Krippendorff's α and Gwet's AC1 enter the κ family with a statistic-type code and are excluded in a sensitivity analysis.
- **One row per configuration.** When a study reports an overall κ for a configuration, it is used. When it reports only per-code κ, the unweighted mean is used, with its SE approximated from the per-code SEs under an assumed between-code correlation of 0.5 (0.2 and 0.8 in sensitivity analyses).

**Benchmark: human–human agreement.** κ between human coders on the same units. The within-study difference Δκ = κ(LLM–human) − κ(human–human) is computed only for matched comparisons: LLM vs each human compared with human vs human, or LLM vs consensus compared with a single human vs the same consensus. SE of Δκ = √(SE₁² + SE₂²), conservative because shared units induce positive covariance. Unmatched comparisons (for example, LLM vs consensus against human vs human) are coded and analysed only in a sensitivity analysis.

**Secondary outcome.** ICC and Pearson or Spearman correlations for continuous or ordinal ratings (mostly T2–T4), pooled separately on Fisher's z (ICC: Bonett, 2002; Shrout & Fleiss, 1979, for ICC forms, which are coded).

**Descriptive only.** Percentage agreement, F1, accuracy, precision and recall against human labels: tabulated, and the share of studies that report only such statistics is reported. Percentage agreement is also pooled on the logit scale to test G8 against κ.

**Open question (error direction).** For T3 and T4 with ordinal ratings: the standardised mean difference between LLM and human ratings, or, from confusion matrices, the proportion of disagreements in which the LLM rated higher. Pooled when at least five studies report it; otherwise narrative.

### [14] Risk of bias in individual studies

Five domains adapted from QUADAS-2 (Whiting et al., 2011) for rater-agreement studies, each low / high / unclear (`forms/rob.md`); the AI drafts each rating with a supporting quote and R1 decides:

1. **Unit selection:** units random, consecutive or complete vs selected or unexplained.
2. **LLM configuration:** prompt and settings fixed before the evaluation units, or tuned on a separate development set, vs tuned on the evaluation units; all tested configurations reported vs only the best.
3. **Human reference:** trained or expert coders, independent of each other and blind to LLM output, with reported human–human reliability, vs not.
4. **Data contamination:** the evaluation texts or labels were public before the model's training cutoff (possible memorisation) vs private or released after the cutoff.
5. **Reporting:** exact model version, run date, settings and prompt available vs not.

Domains enter as moderators and sensitivity filters; no summary score.

### [15] Data synthesis

**[15a] Narrative synthesis.** Study characteristics by task type, construct and text type; an evidence map of task types × constructs × statistics; reporting completeness (share of studies reporting human–human agreement, prevalence, all configurations, model version, prompt).

**[15b] Meta-analysis.**

- **Model.** Correlated-and-hierarchical-effects model on κ — random effects for studies and for estimates within studies, with an assumed within-study correlation of 0.6 between estimates (Pustejovsky & Tipton, 2022) — and cluster-robust (CR2) standard errors and tests with small-sample corrections (Pustejovsky & Tipton, 2018), in `metafor::rma.mv` (Viechtbauer, 2010) with `clubSandwich`. Estimates within a study are several models, prompts or references on the same units.
- **Reported:** pooled κ with 95% CI and 95% prediction interval (IntHout et al., 2016); variance components and I² per level; number of studies and estimates; interpreted with Landis and Koch (1977) labels only as descriptions.
- **RQ1:** pooled κ overall and by task type (T1–T4 as a categorical moderator and as separate models).
- **RQ2 and G1:** the same model on Δκ; G1a is supported if the pooled Δκ is below zero. G1b — equivalence for models released from 2025-01-01: the 90% CI of the pooled Δκ lies within ±0.10 (two one-sided tests; Lakens, 2017).
- **G2:** meta-regression of LLM–human κ on human–human κ of the same units.
- **G3:** release date (years since June 2020) as a continuous moderator; generation as categories (to March 2023; GPT-4 era to April 2024; GPT-4o era to December 2024; 2025–2026); reasoning model (yes/no); and within-study contrasts (newer minus older model on the same units) pooled in their own model.
- **G4–G10:** one moderator at a time — task type and construct type (G4); prompting (G5); log number of categories (G6); reference type (G7); minority-class prevalence on the per-code subset, and percentage agreement vs κ (G8); "best configuration only" vs "all reported" and risk-of-bias domain 2 (G9); English vs other languages (G10). Other moderators: open vs closed weights; human expertise; real vs synthetic texts; contamination (domain 4); publication type; year.
- **Minimum data:** pooling with at least three studies; moderators tested when at least ten studies inform them; robust tests with fewer than four approximate degrees of freedom are reported as unreliable.
- **Secondary:** the same models on Fisher's z for ICC and correlations.

**[15c] Sensitivity analyses.**

1. Excluding imputed SEs.
2. Excluding weighted κ; excluding α and AC1.
3. Only peer-reviewed reports.
4. Only matched comparisons for Δκ; adding unmatched ones.
5. Within-study correlation 0.3 and 0.8; between-code correlation 0.2 and 0.8.
6. One estimate per study (the most recent model with the authors' primary configuration), standard random-effects model with Hartung–Knapp correction.
7. Excluding high contamination risk; excluding synthetic texts.
8. Excluding R1's own study, if included.
9. Leave-one-study-out and influence diagnostics.

**[15d] If pooling is not appropriate**, estimates are tabulated and shown in forest plots without a pooled value.

**Software.** R 4.6.1 with metafor and clubSandwich; Python 3.12 for search, de-duplication, decision files and the AI runner; Claude Code (headless) for AI drafts, with the version stored with every output.

### [16] Meta-biases

- Funnel plots per task type; an Egger-type test with the SE of κ as a moderator in the CHE model with CR2 inference (Rodgers & Pustejovsky, 2021).
- "Best configuration only" and publication type as moderators (G9).
- Selective reporting: models or codes named in the methods but missing from results are recorded.

### [17] Confidence in cumulative evidence

GRADE adapted for agreement estimates, as in the previous reviews: certainty for pooled κ per task type and for the G1 equivalence test, downgraded for risk of bias (weight from studies with high risk in domains 1–3), inconsistency (prediction interval spanning more than one Landis–Koch band), imprecision (CI spanning more than one band, or crossing ±0.10 for Δκ), indirectness (mostly English texts, few clinical datasets) and publication bias.

Reporting follows PRISMA 2020 (Page et al., 2021) and the REGEMA checklist for reliability-generalisation meta-analyses (Sánchez-Meca et al., 2021).

---

## Load for the human reviewer (fixed in advance; one round)

Estimates from the novelty check, the check run and the pilot of the screener prompt; final numbers in the PRISMA flow diagram.

| Stage | Who | Approximate volume |
| --- | --- | --- |
| Title and abstract, blind calibration | R1 | 400 records |
| Title and abstract, verification | R1 | records that at least one AI pass kept, probably 1,000–2,000 of about 6,550 (check run; in the pilot the rule kept 14% of not-eligible records); double exclusions only if the safeguard triggers (then the targeted set plus an audit of 300) |
| Full text | R1 verifies an AI proposal | about 700–1,000 reports, about 85% open |
| Data extraction | R1 verifies an AI draft | about 100–150 studies; about 6,000–9,000 values (study fields, configurations, κ, human–human κ, moderators), each with its source location |
| Risk of bias | R1 verifies an AI draft | 5 domains per included study, each with a quote |

No further human coding rounds are planned. There is no second human reviewer; this is a limitation, partly offset by two AI passes, the blind calibration with a reported miss rate, R1's decision on every record kept and every full text, and verification of every extracted value.

---

## References

- Baumann, J., Röttger, P., Urman, A., Wendsjö, A., Plaza-del-Arco, F. M., Gruber, J. B., & Hovy, D. (2025). *Large language model hacking: Quantifying the hidden risks of using LLMs for text annotation* [Preprint]. arXiv:2509.08825
- Bonett, D. G. (2002). Sample size requirements for estimating intraclass correlations with desired precision. *Statistics in Medicine, 21*(9), 1331–1335. https://doi.org/10.1002/sim.1108
- Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement, 20*(1), 37–46. https://doi.org/10.1177/001316446002000104
- Feinstein, A. R., & Cicchetti, D. V. (1990). High agreement but low kappa: I. The problems of two paradoxes. *Journal of Clinical Epidemiology, 43*(6), 543–549. https://doi.org/10.1016/0895-4356(90)90158-L
- Fisher, H., Jaffe, N. M., Pidvirny, K., Tierney, A. O., Vaidean, M. S., Dongre, P., & Webb, C. A. (2026). Language-based detection of depression with machine learning: Systematic review and meta-analysis. *npj Digital Medicine, 9*. https://doi.org/10.1038/s41746-026-02448-1
- Flathers, M., Nguyen, P. A. H., Noorily, J., et al. (2026). *Mental health benchmarks for large language models: A systematic scoping review* [Preprint]. PsyArXiv. https://doi.org/10.31234/osf.io/fahuk_v1
- Gierbolini-Rivera, R. D., Franco Silva, M., Augusto de Paula da Silva, A., Brownson, R. C., Parra, D. C., Kepper, M. M., & Eyler, A. A. (2026). Generative artificial intelligence for qualitative methods in health research: Rapid review. *Journal of Medical Internet Research, 28*. https://doi.org/10.2196/98551
- Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *Proceedings of the National Academy of Sciences, 120*. https://doi.org/10.1073/pnas.2305016120
- Goodall, L. S., Shilton, D., Mullins, D. A., & Whitehouse, H. (2026). *Large language models struggle with ethnographic text annotation* [Preprint]. arXiv:2601.12099
- Gwet, K. L. (2008). Computing inter-rater reliability and its variance in the presence of high agreement. *British Journal of Mathematical and Statistical Psychology, 61*(1), 29–48. https://doi.org/10.1348/000711006X126600
- Hua, Y., Na, H., Li, Z., Liu, F., Fang, X., Clifton, D., & Torous, J. (2025). A scoping review of large language models for generative tasks in mental health care. *npj Digital Medicine, 8*. https://doi.org/10.1038/s41746-025-01611-4
- IntHout, J., Ioannidis, J. P. A., Rovers, M. M., & Goeman, J. J. (2016). Plea for routinely presenting prediction intervals in meta-analysis. *BMJ Open, 6*(7), e010247. https://doi.org/10.1136/bmjopen-2015-010247
- Kunilovskaya, M., Bhatia, G., Albertelli, L. S., et al. (2026). *Who annotates in NLP? A large-scale assessment of human annotation reporting between 2018 and 2025* [Preprint]. arXiv:2606.02255
- Lakens, D. (2017). Equivalence tests: A practical primer for t tests, correlations, and meta-analyses. *Social Psychological and Personality Science, 8*(4), 355–362. https://doi.org/10.1177/1948550617697177
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics, 33*(1), 159–174. https://doi.org/10.2307/2529310
- Leung, J., Johnson, B., McRae, K., et al. (2026). Generative large language models in mental health care settings: Systematic review and meta-analysis. *JMIR AI, 5*. https://doi.org/10.2196/87730
- Li, H., Chen, C. H., Fan, K., Young-Johnson, C., Lim, S., & Feng, Y. (2025). *Agreement between large language models and human raters in essay scoring: A research synthesis* [Preprint]. arXiv:2512.14561
- Li, L., Li, D., Chen, C., et al. (2026). *LLM-as-a-judge in healthcare: A scoping analysis of applications, methods, and human alignment* [Preprint]. arXiv:2605.25273
- Li, S. (2026). *How closely do large language models agree with human raters when scoring student essays? A systematic review and multilevel meta-analysis* [Registration]. OSF Registries. https://doi.org/10.17605/osf.io/4kqu2
- Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). *Agreement is not quality: Blind expert verification of human and LLM qualitative coding when human consensus is not ground truth* [Preprint]. arXiv:2607.28890
- Moher, D., Shamseer, L., Clarke, M., Ghersi, D., Liberati, A., Petticrew, M., Shekelle, P., Stewart, L. A., & PRISMA-P Group. (2015). Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015 statement. *Systematic Reviews, 4*, 1. https://doi.org/10.1186/2046-4053-4-1
- Na, H., Hua, Y., Wang, Z., Shen, T., Yu, B., Wang, L., Wang, W., Torous, J., & Chen, L. (2025). A survey of large language models in psychotherapy: Current landscape and future directions. In *Findings of the Association for Computational Linguistics: ACL 2025*. https://doi.org/10.18653/v1/2025.findings-acl.385
- Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71. https://doi.org/10.1136/bmj.n71
- Pustejovsky, J. E., & Tipton, E. (2018). Small-sample methods for cluster-robust variance estimation and hypothesis testing in fixed effects models. *Journal of Business & Economic Statistics, 36*(4), 672–683. https://doi.org/10.1080/07350015.2016.1247004
- Pustejovsky, J. E., & Tipton, E. (2022). Meta-analysis with robust variance estimation: Expanding the range of working models. *Prevention Science, 23*(3), 425–438. https://doi.org/10.1007/s11121-021-01246-3
- Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., Ayala, A. P., Moher, D., Page, M. J., Koffel, J. B., & PRISMA-S Group. (2021). PRISMA-S: An extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. *Systematic Reviews, 10*, 39. https://doi.org/10.1186/s13643-020-01542-z
- Rodgers, M. A., & Pustejovsky, J. E. (2021). Evaluating meta-analytic methods to detect selective reporting in the presence of dependent effect sizes. *Psychological Methods, 26*(2), 141–160. https://doi.org/10.1037/met0000300
- Sánchez-Meca, J., Marín-Martínez, F., López-López, J. A., Núñez-Núñez, R. M., Rubio-Aparicio, M., López-García, J. J., López-Pina, J. A., Blázquez-Rincón, D. M., López-Ibáñez, C., & López-Nicolás, R. (2021). Improving the reporting quality of reliability generalization meta-analyses: The REGEMA checklist. *Research Synthesis Methods, 12*(4), 516–536. https://doi.org/10.1002/jrsm.1487
- Seyler, A., O'Rourke, R., Huynh, N., Burton, C., Arnold, P., Cheung, T., & Crosbie, J. (2025). *How does generative artificial intelligence compare to human analysts in qualitative research? A systematic review of large language models* [Preprint]. PsyArXiv. https://doi.org/10.31234/osf.io/gnx8p_v1
- Shrout, P. E., & Fleiss, J. L. (1979). Intraclass correlations: Uses in assessing rater reliability. *Psychological Bulletin, 86*(2), 420–428. https://doi.org/10.1037/0033-2909.86.2.420
- van den Akker, O. R., Peters, G.-J. Y., Bakker, C. J., et al. (2023). Increasing the transparency of systematic reviews: Presenting a generalized registration form. *Systematic Reviews, 12*, 170. https://doi.org/10.1186/s13643-023-02281-7
- Viechtbauer, W. (2010). Conducting meta-analyses in R with the metafor package. *Journal of Statistical Software, 36*(3), 1–48. https://doi.org/10.18637/jss.v036.i03
- Webb, M., Werth, A., Kim, S., Huang, C., & Bahureksa, L. (2026). *How reliable is AI at applying a priori codebooks? A systematic review and reliability-generalization meta-analysis of AI–human agreement in deductive qualitative coding* [Preregistration]. OSF Registries. https://doi.org/10.17605/osf.io/j6589
- Whiting, P. F., Rutjes, A. W. S., Westwood, M. E., Mallett, S., Deeks, J. J., Reitsma, J. B., Leeflang, M. M. G., Sterne, J. A. C., & QUADAS-2 Group. (2011). QUADAS-2: A revised tool for the quality assessment of diagnostic accuracy studies. *Annals of Internal Medicine, 155*(8), 529–536. https://doi.org/10.7326/0003-4819-155-8-201110180-00009
- Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024). Can large language models transform computational social science? *Computational Linguistics, 50*(1), 237–291. https://doi.org/10.1162/coli_a_00502
- Registration cited: PROSPERO CRD420251146504 (Biba et al.; https://www.crd.york.ac.uk/PROSPERO/view/CRD420251146504).
