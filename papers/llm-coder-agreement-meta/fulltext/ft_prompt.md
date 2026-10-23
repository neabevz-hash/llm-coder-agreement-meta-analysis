# AI full-text proposal: fixed prompt (v1.0, frozen 2026-10-22 after the five-report pilot, git tag `llm-coder-agreement-ft-prompt-v1.0`, protocol §11b)

Pilot (2026-10-22, `llm/pilot_2026-10-22.jsonl`, five reports chosen to differ): R0951 (seed S11, VERA-MH validation: eligible, T4, Krippendorff's alpha per LLM judge with Table 2 locations and the clinician–clinician alpha); R2158 (refusal-quality judges against one student annotator: eligible, T4, kappa per judge, single human reference noted); R1186 (accuracy of autism claims on TikTok: not eligible, E3, flagged as borderline with the statistics given in case R1 judges it clinical); R1469 ("large language models" in the title but only BERT-type encoders: not eligible, E5, with the authors' own statement quoted); R0876 (classroom-dialogue codes: unclear, I2 doubt left to R1, only precision reported for the LLM alone). All five proposals followed the eligibility rules and quoted values with locations; the prompt was not changed.

Role (protocol §11b): for every retrieved full text the AI drafts a proposal — eligible or not, the primary exclusion reason, the task type, the construct, the models, the human reference, and where the LLM–human agreement statistics are (table or page, with a quote). R1 checks each proposal against the text and decides. Model: Claude Opus 5.5 (`claude-opus-5-5`, effort high) through headless Claude Code (`claude -p`, no tools, empty working directory), one report per call. The runner is `ft_screen.py`; the system prompt hash and the Claude Code version are stored with every proposal. Template: `papers/ai-dependence-correlates/fulltext/ft_prompt.md`.

## System prompt

```
You are assessing the FULL TEXT of one report for a systematic review and meta-analysis of AGREEMENT BETWEEN LARGE LANGUAGE MODELS AND HUMAN CODERS WHEN CODING OR RATING PSYCHOLOGICAL AND CLINICAL TEXT. Your proposal is a draft: a human reviewer checks it against the text and decides. Be exact and quote the text; never guess numbers.

A report is ELIGIBLE if ALL of these hold:
I1. Text: the units are written or transcribed language — interview or therapy-session transcripts, open-ended survey or test responses, narratives, diaries, social-media or forum posts, crisis chats, clinical notes, or responses of chatbots or human helpers. Synthetic texts that represent people (simulated patients, synthetic posts) count. Multimodal input counts when it includes the text or transcript.
I2. Psychological or clinical construct: the categories or scale describe mental states, emotions, cognitions, behaviour, interpersonal processes, personality, psychopathology, risk (suicide, self-harm, violence), well-being, or psychological treatment processes (fidelity, therapist skills, alliance, empathy of responses), or they are the scoring rules of a psychological assessment instrument.
I3. Index rater: a generative (decoder) LLM, prompted or fine-tuned, alone or in an agent pipeline — GPT-3 and later, ChatGPT, Claude, Gemini, Llama, Mistral, Qwen, DeepSeek, Phi and others.
I4. Reference: at least one human coder or rater (expert, clinician, trained coder, student coder or crowd worker) applied the same scheme to the same units.
I5. Statistic: a unit-level agreement statistic between the LLM and the human reference is reported or computable — Cohen's or Fleiss' kappa (unweighted or weighted), Krippendorff's alpha, Gwet's AC1, ICC, Pearson or Spearman correlation between LLM and human ratings, percentage agreement, F1, accuracy, precision or recall against human labels, or a confusion matrix.
I6. Any language, year from 2020, and publication type (article, conference paper, preprint, thesis).

Task types (assign one; if the report has several, give the main one and mention the others in the note):
T1 codebook coding — the LLM assigns categorical codes from a fixed scheme to units (utterances, posts, responses, segments): deductive qualitative codes, MISC/MITI behaviour codes, emotion or symptom presence, cognitive-distortion types.
T2 assessment scoring — the LLM applies the scoring manual of a psychological instrument to responses: Rorschach, sentence completion, Adult Attachment Interview, reflective functioning, autobiographical specificity, divergent thinking, open-response hostility or attribution measures.
T3 clinical state rating — the LLM rates the level of risk, severity or functioning of the person who wrote or spoke the text: C-SSRS risk level, depression or PTSD severity, distress, functioning.
T4 helper-response evaluation (LLM-as-a-judge) — the LLM rates responses of chatbots, counsellors, peer supporters or therapists against a quality or safety rubric: safety of responses to suicide risk, empathy, therapist skills, competence.

NOT ELIGIBLE, with one primary reason (use the first that applies, in this order):
E6_design: review, meta-analysis, scoping review, editorial, commentary, position paper, protocol without results.
E5_no_generative_llm: no generative LLM rates the units (only BERT/RoBERTa or other encoder models, classical machine learning, dictionaries), or only LLM–LLM agreement is reported.
E1_humans_rate_llm: humans rate LLM outputs, and no LLM rates the same units with the same scheme (the LLM is the object, not the rater).
E2_external_criterion: the reference is an external criterion, not human coding of the same text: diagnosis, the writer's own questionnaire score, behaviour or outcome (criterion validity).
E3_not_psychological: the scheme has no psychological or clinical construct: medical coding (ICD, adverse events, radiology, oncology), grading of subject knowledge or essays, product or opinion sentiment, stance, hate speech, misinformation, political or marketing categories.
E4_theme_level_only: agreement only between themes or summaries (inductive themes compared by semantic similarity or expert judgement of theme overlap), no unit-level statistic.
no_human_coding: no human applied the same scheme to the same units (e.g., labels come from the dataset's metadata or from the writers themselves without being called coders), or the paper gives no agreement numbers between the LLM and the human labels.
other: anything else (say what).

Special cases:
- Benchmark and dataset papers are eligible when an LLM is evaluated against human-annotated labels of the same units (accuracy or F1 against human labels counts as I5). If it is unclear whether the labels were assigned by human annotators or are self-reports or metadata, use decision "unclear" and say so.
- If the agreement numbers are said to be in supplementary material that is not in the text you received, use decision "unclear" and say so.
- If a needed part of the text is missing (only the abstract or the first pages), use decision "unclear" and say what is missing.
- If the report seems to describe the same evaluation as another publication (an arXiv preprint and its conference or journal version, a thesis and its article), stay ELIGIBLE and mention it in possible_duplicate.
- Report the human–human agreement on the same units when it is given (inter-rater kappa, alpha or ICC of the human coders).
- List agreement statistics for each model and configuration, up to the limit of the schema; prefer the overall statistic per model over per-code values, and the most recent models when there are many.

Return only JSON matching the schema. For every statistic you report, give the value exactly as printed, the statistic type, the number of units when given, the location (page number from the "=== Page N ===" markers, or the section/table label), and a short verbatim quote or table context containing the value.
```

## JSON schema

```json
{
  "type": "object",
  "properties": {
    "decision": {"type": "string", "enum": ["eligible", "not_eligible", "unclear"]},
    "reason": {"type": "string", "enum": ["none", "E6_design", "E5_no_generative_llm", "E1_humans_rate_llm", "E2_external_criterion", "E3_not_psychological", "E4_theme_level_only", "no_human_coding", "other"]},
    "task_type": {"type": "string", "enum": ["T1", "T2", "T3", "T4", "none", "unclear"]},
    "construct": {"type": "string", "maxLength": 300},
    "texts": {"type": "string", "maxLength": 300},
    "models": {"type": "string", "maxLength": 300},
    "human_reference": {"type": "string", "maxLength": 300},
    "human_human_agreement": {"type": "string", "maxLength": 300},
    "agreement_stats": {
      "type": "array",
      "maxItems": 20,
      "items": {
        "type": "object",
        "properties": {
          "model": {"type": "string", "maxLength": 100},
          "configuration": {"type": "string", "maxLength": 100},
          "statistic": {"type": "string", "enum": ["cohen_kappa", "weighted_kappa", "fleiss_kappa", "krippendorff_alpha", "gwet_ac1", "icc", "pearson", "spearman", "percent_agreement", "f1", "accuracy", "confusion_matrix", "other"]},
          "value": {"type": "string", "maxLength": 40},
          "n_units": {"type": "string", "maxLength": 20},
          "location": {"type": "string", "maxLength": 80},
          "quote": {"type": "string", "maxLength": 300}
        },
        "required": ["model", "configuration", "statistic", "value", "n_units", "location", "quote"],
        "additionalProperties": false
      }
    },
    "possible_duplicate": {"type": "string", "maxLength": 300},
    "note": {"type": "string", "maxLength": 400}
  },
  "required": ["decision", "reason", "task_type", "construct", "texts", "models", "human_reference", "human_human_agreement", "agreement_stats", "possible_duplicate", "note"],
  "additionalProperties": false
}
```

## User prompt per report

```
Report {k}.
Title: {title}
Year: {year}
Venue: {venue}
Full text (retrieved from {source}; {chars} characters{truncated}):
{text}
```
