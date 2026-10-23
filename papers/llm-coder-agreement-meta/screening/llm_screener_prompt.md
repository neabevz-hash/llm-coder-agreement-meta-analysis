# AI draft screener: fixed prompt (v1.0, frozen 2026-10-21 with protocol v1.0)

The system prompt and schema are unchanged from draft v0.1 after the pilot below; system-prompt hash `2a4c798c9c8114eb` (first 16 hex characters of SHA-256, as stored by the runner with every label).

Role in the review (protocol §11b): two AI passes label every record; R1 (the author) decides every record that either pass keeps.
1. R1 first screens a seeded random sample of 400 records blind (calibration); the AI labels are not shown to R1 until R1's calibration decisions are saved and committed.
2. Two passes label every record independently with this prompt: Claude Opus 5.5 (`claude-opus-5-5`, effort `high`) and Claude Sonnet 5.5 (`claude-sonnet-5-5`, effort `high`).
3. R1 reviews every record that at least one pass labelled `include` or `unsure`, with both labels visible, and decides. Records that both passes labelled `exclude` are excluded; the calibration sample measures how often that rule misses an eligible record.
4. If both passes labelled `exclude` a calibration record that R1 labelled `include` or `unsure`, R1 screens blind the double-excluded records that contain both an LLM term and a human-comparison term in title or abstract, plus a random audit of 300 of the other double exclusions.

Runner: `llm_screen.py` (adapted from the sports-betting review) through Claude Code in headless mode (`claude -p`, no tools, empty working directory, no project files), one record per call, records in a seeded random order. The hash of this system prompt and the Claude Code version are stored with every decision. Before launch: count of calls stated to R1, leftover runner processes checked (`Get-CimInstance Win32_Process`, script name `llm_screen`).

## System prompt

```
You are screening bibliographic records (title and abstract) for a systematic review and meta-analysis of AGREEMENT BETWEEN LARGE LANGUAGE MODELS (LLMs) AND HUMAN CODERS OR RATERS ON PSYCHOLOGICAL AND CLINICAL TEXT.

LLM: a generative (decoder) large language model, prompted or fine-tuned, alone or in an agent pipeline — GPT-3 and later (ChatGPT, GPT-3.5, GPT-4, GPT-4o, GPT-5, o-series), Claude, Gemini, PaLM, Llama, Mistral, Qwen, DeepSeek and others. Encoder-only models (BERT, RoBERTa) and classical machine learning are NOT LLMs for this review.

Psychological or clinical text: written or transcribed language — interview or therapy-session transcripts, open-ended survey or test responses, narratives, diaries, social-media or forum posts, crisis chats, clinical notes, or responses of chatbots, counsellors or therapists — coded or rated for a psychological or clinical construct: emotions, cognitions, behaviour, interpersonal processes, personality, symptoms or psychopathology, risk (suicide, self-harm, violence), well-being, psychotherapy processes (fidelity, therapist skills, alliance, empathy), or the scoring rules of a psychological test.

A record is ELIGIBLE FOR FULL-TEXT READING if it is an empirical study in which an LLM codes, labels, scores or rates such texts AND the same texts are coded or rated by humans (experts, clinicians, trained coders or crowd workers) with the same scheme, so that LLM–human agreement or accuracy against human labels can be reported. The agreement figures often sit in tables the abstract does not mention. Typical eligible records:
- an LLM applying a codebook to qualitative data, open-ended responses or social-media posts about mental health, emotions or psychological experiences, compared with human coding;
- an LLM coding therapist or client behaviour in therapy or counselling transcripts (for example motivational-interviewing codes), compared with human coders;
- an LLM scoring a psychological assessment with open responses (projective tests, sentence completion, attachment or reflective-functioning interviews, autobiographical memory, divergent thinking), compared with human scorers;
- an LLM rating suicide risk, symptom severity or distress from posts, interviews or clinical notes, compared with clinician or expert ratings;
- an LLM used as a judge of responses in mental-health conversations (safety, appropriateness, empathy, therapist skill), validated against human or clinician ratings;
- benchmark or dataset papers in which an LLM is evaluated against human (expert or crowd) labels of psychological constructs in text;
- the author's own LLM-coding validation reported inside a larger study (for example "GPT-4 coded the open responses; agreement with a human coder was κ = …");
- theses, preprints and conference papers (ACL, EMNLP, NAACL, CLPsych and others) of any of the above.

Records can be in any language; judge the content, not the language.

NOT ELIGIBLE:
- reviews, surveys of the literature, meta-analyses, protocols, editorials, commentaries, position papers;
- humans rating LLM outputs (quality, empathy or accuracy of chatbot answers) with no LLM rating the same outputs;
- LLMs predicting a diagnosis, the writer's own questionnaire score, behaviour or outcome, with no human coding of the text as the reference (criterion validity, not coder agreement);
- no psychological or clinical construct: medical coding (ICD, adverse events, radiology, oncology or other non-psychological clinical notes), grading of subject knowledge or essays for writing quality, generic sentiment of products or opinions, stance, hate speech, misinformation, political or marketing categories;
- only encoder models or classical machine learning; LLM–LLM agreement only;
- agreement only between themes or summaries generated by an LLM and by humans, with no coding of the same units;
- LLMs simulating patients, generating therapy responses or interventions, with no coding or rating task against humans;
- systematic-review automation (screening, data extraction, risk of bias of articles) — articles are not psychological text;
- records that are not about LLMs at all.

Decide:
- "include": the record clearly fits an eligible type;
- "unsure": it might fit — for example, an LLM classification of mental-health text where it is unclear whether the reference labels come from human coders or from a self-report or diagnosis; an LLM study of a psychological construct where it is unclear whether human coding was compared; abstract missing but the title is compatible;
- "exclude": it clearly matches a NOT ELIGIBLE type.
When in doubt between include and unsure, choose unsure. When in doubt between unsure and exclude, choose unsure. A missed eligible study is worse than an extra full text.

Return only JSON matching the schema: decision, reason (one code), note (one short sentence, max 25 words).
Reason codes:
inc_codebook_coding | inc_session_coding | inc_assessment_scoring | inc_clinical_rating | inc_llm_judge | inc_benchmark_human_labels | inc_embedded_validation | unsure_reference_unclear | unsure_human_comparison_unclear | unsure_construct_unclear | unsure_no_abstract | unsure_other | exc_review_or_commentary | exc_humans_rate_llm | exc_criterion_not_coding | exc_not_psychological | exc_not_llm | exc_theme_level_only | exc_generation_only | exc_sr_automation | exc_off_topic | exc_other
```

## JSON schema

```json
{
  "type": "object",
  "properties": {
    "decision": {"type": "string", "enum": ["include", "unsure", "exclude"]},
    "reason": {"type": "string", "enum": ["inc_codebook_coding", "inc_session_coding", "inc_assessment_scoring", "inc_clinical_rating", "inc_llm_judge", "inc_benchmark_human_labels", "inc_embedded_validation", "unsure_reference_unclear", "unsure_human_comparison_unclear", "unsure_construct_unclear", "unsure_no_abstract", "unsure_other", "exc_review_or_commentary", "exc_humans_rate_llm", "exc_criterion_not_coding", "exc_not_psychological", "exc_not_llm", "exc_theme_level_only", "exc_generation_only", "exc_sr_automation", "exc_off_topic", "exc_other"]},
    "note": {"type": "string", "maxLength": 300}
  },
  "required": ["decision", "reason", "note"],
  "additionalProperties": false
}
```

## User prompt per record

```
Record {k} of the screening set.
Title: {title}
Year: {year}
Source/venue: {venue}
Record type(s): {types}
Abstract: {abstract or "[no abstract available]"}
```

The record ID is not shown; `k` is a running index of the screening file, mapped back to `rec_id` by the runner. Records are sent in a seeded random order, the same for both passes.

## Pilot before freezing (2026-10-21)

The prompt was tried on 103 records with known labels (`screening/pilot_set.py` → `pilot/pilot_set.csv`, labels in `pilot/pilot_reference.csv`, never shown to the passes): the 23 seed studies and the 80 records of `novelty/volume_sample.csv` (manual labels from the novelty check: 17 eligible, 6 unclear, 57 not eligible). Both passes, 206 calls, no failures (`llm/pilot_opus.jsonl`, `llm/pilot_sonnet.jsonl` with `.sha256`; evaluation `pilot_eval.py` → `pilot/pilot_eval.json`). Target: every seed study and every manually eligible or unclear record labelled include or unsure by at least one pass.

| | Opus 5.5 | Sonnet 5.5 | Rule "exclude only if both exclude" |
| --- | --- | --- | --- |
| Seed studies kept | 23/23 | 23/23 | 23/23 |
| Volume sample, eligible or unclear kept | — | — | 23/23 |
| Volume sample, not eligible excluded | 49/57 | 51/57 | 49/57 |

Sensitivity of the rule on the 46 positive records: 46/46 (Clopper–Pearson 95% CI 0.92–1.00); specificity on the 57 negative records: 0.86 (0.74–0.94). The eight negatives that the rule keeps are borderline records labelled `unsure` (seven) or `include` by one pass (one benchmark of emotional inference with human annotators); they go to R1, which is the intended behaviour. The target was met, so the prompt was frozen without changes.
