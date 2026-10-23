# AI completion pass: moderators and risk of bias for the drafted estimates (v1.0 after a five-study check; git tag `llm-coder-agreement-extraction-prompt-v1.0`; deviations.md, D7)

Role (protocol §11c–§14, `forms/extraction_codebook.md`, `forms/rob.md`; D7): the numbers of every study were drafted at the full-text stage (`extraction/ft_estimates.csv`, built by `estimates_from_ft.py` from the full-text proposals and checked against the source texts by script). This pass reads the study's text once and adds what the analysis needs and the proposals lack: the tasks of the study and their moderators, a code line for each drafted estimate (task, prompting, reference, inclusion), human–human agreement, and the five risk-of-bias domains. For the reports whose proposal listed no statistics or hit the limit of 20, it also adds the missing overall estimates. Model: Claude Sonnet 5.5, effort medium, reference list cut (`complete.py`). Model attributes (developer, release date, open weights, parameters, reasoning) come from `forms/model_releases.csv`, built once per model. Template of the form: `extract_prompt.md` v0.1 (piloted on five studies 2026-10-23, `draft/pilot_2026-10-23.jsonl`), shortened.

## System prompt

```
You are coding studies for a systematic review and meta-analysis of AGREEMENT BETWEEN LARGE LANGUAGE MODELS AND HUMAN CODERS WHEN CODING OR RATING PSYCHOLOGICAL AND CLINICAL TEXT. The agreement values of this study were drafted earlier and are listed in the job with IDs (F0001...). You read the full text and code the study's tasks, each listed estimate, the human-human agreement and the risk of bias. Your output is a draft that a human reviewer checks. Accuracy matters more than completeness.

Rules:
- Take everything from the texts given. Never fill from general knowledge (model release dates, training cutoffs, dataset details known from elsewhere). Not reported: NR. Not applicable: NA.
- Do not compute anything. Copy numbers exactly as printed.
- Be brief: codes and short phrases, no explanations beyond the "basis" and "reason" fields.

Return only JSON matching the schema.
```

## User preamble (same for every job)

```
CODING FORM

A TASK is one coding or rating scheme applied to one set of units: one dataset x one construct (e.g., "Dreaddit stress, binary"; "MISC counsellor codes"; "C-SSRS risk level"). Datasets or constructs analysed separately are separate tasks. IDs A, B, C...

TASK fields:
- task_type [T1 / T2 / T3 / T4]: T1 codebook coding (categorical codes from a fixed scheme assigned to units: deductive qualitative codes, MISC/MITI codes, emotion or symptom presence, cognitive-distortion types); T2 assessment scoring (the scoring manual of a psychological assessment instrument applied to responses: Rorschach, sentence completion, AAI, reflective functioning, autobiographical specificity, divergent thinking or originality, AIHQ); T3 clinical state rating (level of risk, severity or functioning of the person who wrote or spoke the text: C-SSRS level, depression or PTSD severity, distress); T4 helper-response evaluation, LLM-as-a-judge (quality or safety of responses of chatbots, counsellors, peers or therapists: safety, empathy, therapist skills, competence, fidelity)
- construct (short), construct_type [manifest = presence of explicit content: a topic, a named behaviour, an explicit emotion word, a stated symptom / latent = inference about an unobservable state or quality: risk, severity, defence, empathy, competence, personality]; decide from the code definitions, not from the results
- n_categories: categories or scale points of the reference scheme ("4"; "1-5"; "10 codes x binary")
- unit [utterance / post / response / segment / transcript / session / document / other]; n_units: units coded by both the LLM and the humans in the evaluation (test set)
- text_type [therapy-session / clinical-interview / clinical-note / social-media / crisis-chat / open-ended-response / narrative / qualitative-interview / chatbot-response / other]; text_source [real / synthetic / mixed]
- dataset (public name and year as given, or "own data"); dataset_public [public before the study / private / released with this study / NR]; language of the texts (ISO 639-1; several: "MULTI: en, de")
- human_coders_n; human_expertise [clinician-or-expert / trained-coder / crowd / mixed / NR]; human_independent [yes / no / NR] (humans coded without seeing LLM output); reference_type [single-coder / each-of-several / consensus-or-adjudicated / majority-vote / mean-of-raters / NR]. For a public dataset, use what this report says about its annotation; if it only cites the dataset paper, write NR.
- basis: where these facts are (pages or sections), at most 200 characters

ESTIMATE CODES: one line for every listed estimate (F...), in the order given:
- include [yes / no]: no if the value is not agreement between a generative LLM and the human reference on an eligible task: an encoder model (BERT, RoBERTa) or classical machine learning, LLM-vs-LLM or run-to-run agreement, a human-only value, a value taken from an earlier study without being run here, a per-class or per-subgroup value when the overall value is also listed, or a statistic of another kind (balanced accuracy, MCC, AUC, loss). Encoder-decoder models (T5, Flan-T5, BART) are "yes" with exclude_reason "encoder-decoder" for the reviewer.
- exclude_reason: short, or NA
- task (A, B...); statistic_code [cohen_kappa / fleiss_kappa / weighted_kappa_linear / weighted_kappa_quadratic / weighted_kappa / krippendorff_alpha / gwet_ac1 / pabak / icc / pearson / spearman / kendall / ccc / percent_agreement / accuracy / f1_macro / f1_weighted / f1_micro / f1 / precision / recall / mae / rmse / other]; icc_form ("ICC(2,1)"... or NR)
- model_name: exact model and version as reported; prompting: one or more of [zero-shot / few-shot / chain-of-thought / fine-tuned / retrieval-augmented / agent-or-ensemble], ";"-separated; n_examples (few-shot) or NA
- reference [single-coder / each-of-several / consensus-or-adjudicated / majority-vote / mean-of-raters / NR] for this value; n_units for this value
- authors_primary [yes / no]: the authors' main or final configuration
- prevalence: minority or positive class share in the human labels if reported, else NR; mean_llm, mean_human: for T3 and T4 ordinal or continuous ratings, the mean rating of the LLM and of the humans on the same units if reported, else NA

ADDED ESTIMATES: only if the job says the list is incomplete. Overall values per configuration and task that are missing from the list; the same statistic rules (kappa family, alpha, AC1, ICC, correlations, percent agreement and accuracy always; of the F1 scores only the first available of f1_macro, f1_weighted, f1_micro, f1). For a sweep over one numeric setting of the same model and prompting type, only the authors' main setting. Each with value as printed, n_units, loc and a short verbatim quote.

HUMAN RELIABILITY: every human-human agreement value on the units of a task: task, same_units [yes / partial / no], comparison [coder-vs-coder / coder-vs-consensus / mean-pairwise / multi-rater], statistic (codes as above), value as printed, n_units, loc, quote (short, verbatim).

STUDY:
- pub_status [journal / conference / preprint / thesis / other]; field (authors' main field) [psychology / psychiatry-medicine / computer-science-NLP / public-health / education / other]
- all_configs_reported [yes / no = only the best or a selection of tested configurations reported / single configuration]
- tuned_on_eval [yes / no / NR]: prompt or settings chosen or revised on the evaluation units

RISK OF BIAS (low / high / unclear, each with a reason of at most 200 characters):
- rob_1 unit selection: low = random, consecutive or all units of a defined set (including a full public test split); high = hand-picked or selected for clarity or difficulty, or unexplained while a larger pool existed; unclear = not described
- rob_2 LLM configuration: low = fixed in advance or tuned only on a separate development set, AND all tested configurations reported (or one tested); high = tuned on the evaluation units, or only the best of several reported; unclear = not stated
- rob_3 human reference: low = trained or expert coders, independent of each other and of LLM output, with human-human reliability reported on these units; high = a single untrained coder, coders who saw LLM output, or no reliability reported; unclear = partly reported
- rob_4 data contamination: low = texts and labels private, or released after the models were run; high = public before the models were run (public benchmark or published dataset); unclear = dates not given
- rob_5 reporting: low = exact model version, run date, settings and the prompt (or a link) reported; high = model version or prompt not reported; unclear = partly reported
```

## Job template (the runner fills it)

```
JOB {job_id} (study {study_id})
What to code: {scope}
{links}
LISTED ESTIMATES ({n_listed}; drafted from the full-text proposal{incomplete}):
{listed}

MAIN REPORT {main_id}
Title: {main_title}
Year: {main_year}; venue: {main_venue}; DOI: {main_doi}
Full text ({main_chars} characters{main_truncated}; reference list removed):
{main_text}
{attached}
```

## Output fields

```json
{
  "task_enums": {
    "task_type": ["T1", "T2", "T3", "T4"],
    "construct_type": ["manifest", "latent"],
    "unit": ["utterance", "post", "response", "segment", "transcript", "session", "document", "other"],
    "text_type": ["therapy-session", "clinical-interview", "clinical-note", "social-media", "crisis-chat", "open-ended-response", "narrative", "qualitative-interview", "chatbot-response", "other"],
    "text_source": ["real", "synthetic", "mixed"],
    "dataset_public": ["public before the study", "private", "released with this study", "NR"],
    "human_expertise": ["clinician-or-expert", "trained-coder", "crowd", "mixed", "NR"],
    "human_independent": ["yes", "no", "NR"],
    "reference_type": ["single-coder", "each-of-several", "consensus-or-adjudicated", "majority-vote", "mean-of-raters", "NR"]
  },
  "task_text": ["task_id", "label", "construct", "n_categories", "n_units", "dataset", "language", "human_coders_n", "basis"],
  "statistics": ["cohen_kappa", "fleiss_kappa", "weighted_kappa_linear", "weighted_kappa_quadratic", "weighted_kappa", "krippendorff_alpha", "gwet_ac1", "pabak", "icc", "pearson", "spearman", "kendall", "ccc", "percent_agreement", "accuracy", "f1_macro", "f1_weighted", "f1_micro", "f1", "precision", "recall", "mae", "rmse", "other"],
  "study_enums": {
    "pub_status": ["journal", "conference", "preprint", "thesis", "other"],
    "field": ["psychology", "psychiatry-medicine", "computer-science-NLP", "public-health", "education", "other"],
    "all_configs_reported": ["yes", "no", "single configuration"],
    "tuned_on_eval": ["yes", "no", "NR"]
  },
  "comparisons": ["coder-vs-coder", "coder-vs-consensus", "mean-pairwise", "multi-rater"],
  "same_units": ["yes", "partial", "no"],
  "rob_ratings": ["low", "high", "unclear"]
}
```
