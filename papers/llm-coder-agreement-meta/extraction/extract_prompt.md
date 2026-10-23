# AI extraction and risk-of-bias draft: fixed prompt (draft v0.1, before the five-study pilot; to be frozen with git tag `llm-coder-agreement-extraction-prompt-v1.0`)

Role (protocol §11c, §12–§14; `forms/extraction_codebook.md`, `forms/rob.md`): for every study (`extraction/jobs.json`) the AI drafts the four linked tables of the codebook and the five risk-of-bias domains, each value with its location and a short verbatim quote. The draft is stored unchanged in `extraction/draft/`; R1 verifies every value against the source. Runner: `extract.py`, headless Claude Code, one job per call, reference lists cut from the texts (as `fulltext/ft_screen.py --strip-refs`). Model: Claude Sonnet 5.5 at effort medium (deviations.md, D7; the protocol names Opus 5.5). Template: `papers/ai-dependence-correlates/extraction/extract_prompt.md`.

How the draft maps to the codebook tables:
- `studies.csv`: the study-level fields, and per task (`tasks`) the fields that can differ between the datasets or constructs of one study (construct, scheme, categories, unit, units, texts, human coders, reference). A study whose tasks have two task types (T1–T4) becomes two `study_id`s sharing `report_ids` at finalisation (codebook).
- `estimates.csv`: one row per configuration × task × human reference × statistic; the configuration fields (model, prompting, settings) are drafted once per configuration and joined at finalisation.
- Model attributes that the reports rarely state (developer, family, release date, open weights, parameters, reasoning model) are not drafted per estimate: they come from `forms/model_releases.csv`, built once per distinct model during extraction (codebook, `release_date`).
- `human_reliability.csv` and `codes.csv` as in the codebook.

## System prompt

```
You are extracting data for a systematic review and meta-analysis of AGREEMENT BETWEEN LARGE LANGUAGE MODELS AND HUMAN CODERS WHEN CODING OR RATING PSYCHOLOGICAL AND CLINICAL TEXT. You read the full text of one study (one or more reports) and fill a fixed extraction form and a risk-of-bias checklist. Your output is a draft: a human reviewer checks every value against the source. Accuracy matters more than completeness.

Rules for every value:
- Take values only from the texts given. Never guess or fill from general knowledge (model release dates, training cutoffs, parameter counts or dataset details you know from elsewhere). If a value is not reported, write NR; if it does not apply, write NA.
- Give the location of every value: page from the "=== Page N ===" markers, or the section, table or figure label. If the value comes from an attached report rather than the main report, start the location with that report's ID (e.g., "R4135, Table 1").
- Give a short verbatim quote (at most 300 characters) that contains the value or the words it rests on. For a value in a table, quote the row label and the cells around the value so the reader can find it (e.g., "GPT-4o | 0.72 | 0.68 | 0.81").
- If the text is not in English, quote it in the original language and add an English translation in square brackets.
- Numbers: copy values exactly as printed (keep the sign and the decimals; drop significance stars). Write proportions as printed; if the report gives percentages (e.g., 82.4%), copy "82.4%" and the reviewer converts. If text and table disagree, use the table and describe the disagreement in consistency_notes.
- Do not compute anything (no means, no conversions, no kappa from accuracy). Values that would need computing are recorded as reported, and the reviewer computes them.

Use the codes and rules in the user message exactly. Return only JSON matching the schema.
```

## User preamble (same for every job; the runner appends the job)

```
EXTRACTION FORM

Unit of extraction: the STUDY = one evaluation in which one or more generative LLMs and human coders code or rate the same text units with the same scheme. The job says which evaluations of the report(s) to extract. Inside a study:
- a TASK is one coding or rating scheme applied to one set of units: one dataset x one construct (e.g., "Dreaddit stress, binary"; "MISC counsellor codes"; "C-SSRS risk level, 4 levels"). Datasets or constructs analysed separately are separate tasks. Give each task an ID A, B, C...
- a CONFIGURATION is one LLM rater setting: model x prompting x settings (e.g., "GPT-4o, few-shot 5 examples, temperature 0"). Give each an ID C1, C2...
- an ESTIMATE is one agreement value between a configuration and the human reference on a task.

Eligible raters: generative (decoder) LLMs only (GPT-3 and later, ChatGPT, Claude, Gemini, PaLM, Llama, Mistral, Qwen, DeepSeek, Phi, Gemma, GLM and others), prompted or fine-tuned, alone or in a pipeline. Do not extract encoder models (BERT, RoBERTa, MentalBERT), classical machine learning, dictionaries (LIWC) or human-only baselines. Encoder-decoder models (T5, Flan-T5, BART) are extracted and marked "encoder-decoder" in the configuration's model_name, for the reviewer to decide. An LLM-based pipeline or ensemble counts as one configuration. Do not extract LLM-vs-LLM agreement (run-to-run, model-vs-model) as estimates. Results the authors take from earlier studies without running them are not extracted (name them in excluded).

STUDY fields (each with value, loc, quote; codes in brackets):
- pub_status of the main report [journal / conference / preprint / thesis / other]; conference = peer-reviewed proceedings, ACL Anthology venues
- field: the authors' main field from the affiliations [psychology / psychiatry-medicine / computer-science-NLP / public-health / education / other]
- language of the full text of the main report (ISO 639-1)
- all_configs_reported [yes = every configuration the authors tested is reported / no = the report says other configurations were tried and only the best (or a selection) is reported / single configuration = one configuration tested]
- funding_coi: funding and conflicts of interest, briefly

TASK fields (per task; each with value, loc, quote):
- task_type [T1 / T2 / T3 / T4]:
  T1 codebook coding: the LLM assigns categorical codes from a fixed scheme to units (utterances, posts, responses, segments), any speaker: deductive qualitative codes, MISC/MITI codes, emotion or symptom presence, cognitive-distortion types.
  T2 assessment scoring: the LLM applies the scoring manual of a psychological assessment instrument to responses: Rorschach, sentence completion, Adult Attachment Interview, reflective functioning, autobiographical specificity, divergent thinking or originality, AIHQ.
  T3 clinical state rating: the LLM rates the level of risk, severity or functioning of the person who wrote or spoke the text: C-SSRS risk level, depression or PTSD severity, distress, functioning.
  T4 helper-response evaluation (LLM-as-a-judge): the LLM rates responses of chatbots, counsellors, peer supporters or therapists against a quality or safety rubric: safety of responses to suicide risk, empathy, therapist skills, competence, fidelity.
- construct: what is coded or rated, briefly (e.g., "change talk (MISC 2.5)", "suicide risk level (C-SSRS)")
- construct_type [manifest / latent]: decide from the code definitions, not from the results. manifest = presence of explicit content (a topic, a named behaviour, an explicit emotion word, a stated symptom); latent = an inference about an unobservable state or quality (risk, severity, defence, empathy, competence, personality)
- scheme: codebook or instrument name and source (e.g., "MISC 2.5", "C-SSRS", "Exner CS", "authors' codebook")
- n_categories: number of categories or scale points of the reference scheme (e.g., "4"; "1-5 scale"); for a multi-code scheme, "<number of codes> codes x <categories per code>" (e.g., "10 codes x binary")
- unit [utterance / post / response / segment / transcript / session / document / other]
- n_units: units coded by both the LLM and the humans in the evaluation (the test set, not the training set)
- text_type [therapy-session / clinical-interview / clinical-note / social-media / crisis-chat / open-ended-response / narrative / qualitative-interview / chatbot-response / other]
- text_source [real / synthetic / mixed]; synthetic = texts written by an LLM or by researchers to represent people
- dataset: a public dataset's name and release year (as given), or "own data". For a public dataset, fill the human-coder fields below only from what this report says; if it only cites the dataset paper, write NR and name that paper in the task label or the study note
- dataset_public [public before the study / private / released with this study / NR]
- language: language of the texts (ISO 639-1); several: "MULTI: en, de, ..."
- human_coders_n: number of human coders on the evaluation units
- human_expertise [clinician-or-expert / trained-coder / crowd / mixed / NR]; clinician-or-expert = licensed clinicians, psychologists, domain experts; trained-coder = trained research assistants or students; crowd = crowd workers
- human_independent [yes / no / NR]: the humans coded without seeing LLM output
- reference_type [single-coder / each-of-several / consensus-or-adjudicated / majority-vote / mean-of-raters / NR]: what the LLM is compared with

Which configurations: extract every configuration that differs in model or in prompting type (zero-shot, few-shot, chain-of-thought, fine-tuned, retrieval-augmented, agent or ensemble), including those the authors present as worse. When the authors sweep one numeric setting of the same model and prompting type (number of examples, context length, temperature, epochs, thresholds), extract only the setting the authors present as their main or final one and give the range of the sweep in the configuration's quote or in excluded.

CONFIGURATION fields (per configuration; one loc and quote for the configuration as a whole):
- model_name: exactly as reported, with version, snapshot or size (e.g., "gpt-4o-2024-08-06", "Claude 3.5 Sonnet", "Llama-3-70B-Instruct")
- prompting: one or more of [zero-shot / few-shot / chain-of-thought / fine-tuned / retrieval-augmented / agent-or-ensemble], separated by ";"
- n_examples: few-shot examples in the prompt, else NA
- codebook_in_prompt [full definitions / labels only / NR]
- temperature, n_runs: as reported, else NR
- run_date: date or month of the LLM runs, if reported, else NR
- tuned_on_eval [yes / no / NR]: yes = the prompt or settings were chosen or revised on the same units the estimate is computed on; no = fixed in advance or chosen on a separate development or training set
- authors_primary [yes / no]: yes for the configuration the authors present as their main or final one (one per task, or several if the authors name several)

ESTIMATES (one row per configuration x task x human reference x statistic):
- Extract the overall value per configuration and task. Do not extract per-code, per-class or per-subgroup values as estimates (per-code values go to CODES, below). If the report gives only per-code or per-item values for a configuration, record them in CODES and add one estimate row with statistic as reported, value "per-code only", and the number of codes in note.
- Statistics: extract every reported value of: cohen_kappa, fleiss_kappa, weighted_kappa_linear, weighted_kappa_quadratic, weighted_kappa (weights not stated), krippendorff_alpha, gwet_ac1, pabak, icc (give the form in icc_form, e.g., "ICC(2,1)", "ICC(3,k)", "ICC(A,1)"; NR if not given), pearson, spearman, kendall, ccc, percent_agreement, and accuracy (in a single-label task, accuracy against the human labels is the observed agreement, so always extract it). Of the F1 scores, extract per configuration and task only the first available in this order: f1_macro, f1_weighted, f1_micro, f1 (averaging not stated); precision and recall only if no other statistic is reported. Also extract mae or rmse only for ordinal or continuous ratings when no correlation, ICC or kappa is given. Do not extract balanced accuracy, MCC, AUC or loss values.
- reference: which human reference this estimate compares with (e.g., "consensus of 2 clinicians", "coder A", "mean of 3 raters", "each of 4 annotators, averaged")
- value: as printed; ci_low, ci_high, se: as reported, else NR
- n_units: the n for this value (the task n unless the report gives another)
- p_o, p_e: observed and chance agreement, if reported; prevalence: share of the minority (or positive) class in the human labels, if reported
- confusion_matrix: LLM x human counts if printed (2 x 2 as "a,b;c,d" with rows = LLM, columns = human; larger tables as rows separated by ";"), else NR
- mean_llm, mean_human, sd_llm, sd_human: for T3 and T4 ordinal or continuous ratings, the mean (and SD) of the LLM's and the humans' ratings on the same units, if reported, else NA
- loc, quote; note: anything the reviewer must know (e.g., "value read from a figure label", "mean over 5 runs", "test split of 20%")
- Values shown only as bars, points or colours in a figure without printed numbers are not extracted; name them in consistency_notes.

HUMAN RELIABILITY (human-human agreement on the units of a task, one row per value):
- task (A, B...), same_units [yes = the same evaluation units / partial = an overlapping subset / no = other units, e.g., the training data or an earlier study], comparison [coder-vs-coder / coder-vs-consensus / mean-pairwise / multi-rater], statistic (codes as for estimates), value, ci_low, ci_high, se, n_units, loc, quote
- pairs_with: the LLM reference it matches for a within-study comparison, if any: "LLM vs each coder" (human coder-vs-coder), "LLM vs consensus" (a single coder vs the same consensus), or "none"

CODES (per-code values, only (a) per-code kappa with the code's prevalence or base rate, or (b) per-code values of a configuration that has no overall value; at most 60 rows per study, preferring the authors' primary configuration):
- task, config, code (name as in the report), statistic, value, percent_agreement, prevalence, n_units, loc

RISK OF BIAS (five domains, each rated low / high / unclear with a reason, loc and quote; forms/rob.md):
- rob_1 unit selection: low = evaluation units random, consecutive or all units of a defined set (including the full test split of a public dataset); high = hand-picked, selected for clarity or difficulty, or selection unexplained while a larger pool existed; unclear = not described
- rob_2 LLM configuration: low = prompt and settings fixed before the evaluation units, or tuned only on a separate development set, AND all tested configurations reported (or only one tested); high = tuned on the evaluation units, or only the best of several configurations reported; unclear = not stated how the configuration was chosen
- rob_3 human reference: low = coders trained or expert, coding independently of each other and without seeing LLM output, with human-human reliability reported on these units; high = a single untrained coder, coders who saw LLM output before coding, or no reliability reported for the reference; unclear = partly reported
- rob_4 data contamination: low = evaluation texts and labels private, or first released after the models were run (state the dates you rely on); high = evaluation texts and labels public before the models were run (public benchmark or published dataset); unclear = release dates not given
- rob_5 reporting: low = exact model version, run date, settings and the prompt (or a link to it) reported; high = model version or prompt not reported; unclear = partly reported

Also:
- excluded: evaluations or results in the report(s) that are not extracted, and why (e.g., "BERT baselines (encoder)", "Chapter 1: mathematics codes, not psychological", "LLM-vs-LLM agreement")
- consistency_notes: disagreements between text and tables or between reports; values shown only in figures
- note: anything else the reviewer should know
```

## Job template (the runner fills it)

```
JOB {job_id} (study {study_id})
What to extract: {scope}
{links}
MAIN REPORT {main_id}
Title: {main_title}
Year: {main_year}; venue: {main_venue}; DOI: {main_doi}
Full text ({main_chars} characters{main_truncated}; reference list removed):
{main_text}
{attached}
```

## Output fields

The runner builds the JSON schema from this block: study and task fields are objects {value, loc, quote}; fields with a code list get an enum on value.

```json
{
  "study_fields": {
    "pub_status": ["journal", "conference", "preprint", "thesis", "other"],
    "field": ["psychology", "psychiatry-medicine", "computer-science-NLP", "public-health", "education", "other"],
    "language": null,
    "all_configs_reported": ["yes", "no", "single configuration"],
    "funding_coi": null
  },
  "task_fields": {
    "task_type": ["T1", "T2", "T3", "T4"],
    "construct": null,
    "construct_type": ["manifest", "latent"],
    "scheme": null,
    "n_categories": null,
    "unit": ["utterance", "post", "response", "segment", "transcript", "session", "document", "other"],
    "n_units": null,
    "text_type": ["therapy-session", "clinical-interview", "clinical-note", "social-media", "crisis-chat", "open-ended-response", "narrative", "qualitative-interview", "chatbot-response", "other"],
    "text_source": ["real", "synthetic", "mixed"],
    "dataset": null,
    "dataset_public": ["public before the study", "private", "released with this study", "NR"],
    "language": null,
    "human_coders_n": null,
    "human_expertise": ["clinician-or-expert", "trained-coder", "crowd", "mixed", "NR"],
    "human_independent": ["yes", "no", "NR"],
    "reference_type": ["single-coder", "each-of-several", "consensus-or-adjudicated", "majority-vote", "mean-of-raters", "NR"]
  },
  "config_fields": ["model_name", "prompting", "n_examples", "codebook_in_prompt", "temperature", "n_runs", "run_date", "tuned_on_eval", "authors_primary"],
  "statistics": ["cohen_kappa", "fleiss_kappa", "weighted_kappa_linear", "weighted_kappa_quadratic", "weighted_kappa", "krippendorff_alpha", "gwet_ac1", "pabak", "icc", "pearson", "spearman", "kendall", "ccc", "percent_agreement", "f1_macro", "accuracy", "f1_weighted", "f1_micro", "f1", "precision", "recall", "mae", "rmse", "other"],
  "comparisons": ["coder-vs-coder", "coder-vs-consensus", "mean-pairwise", "multi-rater"],
  "same_units": ["yes", "partial", "no"],
  "pairs_with": ["LLM vs each coder", "LLM vs consensus", "none"],
  "rob_ratings": ["low", "high", "unclear"]
}
```
