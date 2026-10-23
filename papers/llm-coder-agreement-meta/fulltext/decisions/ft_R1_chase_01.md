# Полные тексты, часть 1

Отчёты 1–17 из 17. Предложение ИИ — черновик, решаете вы.

**Как размечать.** Откройте полный текст (ссылка в блоке), сверьте предложение ИИ и допишите код в строку **Решение:**.

| Код | Что значит |
| --- | --- |
| `=` | согласен с ИИ |
| `+` | подходит: генеративная LLM размечает или оценивает психологические тексты, люди размечали те же единицы по той же схеме, есть цифры согласия |
| `-1` | не подходит: обзор, метаанализ, комментарий, позиция, протокол без результатов |
| `-2` | не подходит: нет генеративной LLM (только BERT, классическое ML, словари) или только согласие LLM с LLM |
| `-3` | не подходит: люди оценивают ответы LLM, а LLM сама ничего не размечает |
| `-4` | не подходит: эталон — диагноз, самоотчёт автора текста, поведение или исход, а не разметка людьми |
| `-5` | не подходит: нет психологического конструкта: медицинское кодирование, оценка знаний, тональность, позиция, хейт |
| `-6` | не подходит: согласие только на уровне тем или выжимок, без статистики по единицам |
| `-7` | не подходит: люди не размечали те же единицы по той же схеме, или нет цифр согласия LLM с людьми |
| `-8` | не подходит: та же оценка, что в другом отчёте (связать) |
| `-9` | не подходит: другое — напишите почему |
| `?` | пока не решил (до закрытия файла нужно решить) |

Цифры согласия ИИ брал из текста, но выписываться они будут на следующем этапе по оригиналу — здесь решаем только «подходит / нет» и причину. Если подходит, проверьте тип задачи (T1 кодбук, T2 подсчёт методики, T3 клиническая оценка, T4 LLM-судья) — его можно дописать заметкой.

---

### 1 · R20001

**From Posts to Timelines: Modeling Mental Health Dynamics from Social Media Timelines with Hybrid LLMs**

2025 · Workshop on Computational Linguistics and Clinical Psychology · pdf

Открыть: [PDF](../pdf/R20001.pdf) · [текст](../text/R20001.txt) · [онлайн](https://aclanthology.org/2025.clpsych-1.21.pdf)

**ИИ предлагает:** + · eligible · none · T3 · Sonnet 5.5

- Конструкт: Well-being/functioning (GAF-derived 1-10 score) and adaptive vs maladaptive self-state evidence (MIND framework) in social media posts
- Тексты: Social media timelines (posts) from the CLPsych 2025 shared task, with annotated evidence spans and well-being scores
- Модели: Fine-tuned Qwen2.5-7B (LoRA) for evidence identification and well-being rating; Qwen2.5-32B ICL for summaries; baselines zero-shot Llama 3.1-8B, BART-Large, BERT
- Эталон (люди): Shared-task annotations of adaptive/maladaptive evidence spans and well-being scores (annotators not described in this paper)
- Согласие людей между собой: Not reported
- Qwen2.5-7B fine-tuned (evidence from classification model) (Task A.2 well-being rating, macro F1 over impairment classes): f1 = 36.6 [n = not given]; Table 2: «Ours (w/ Class.) 2.01 1.25 3.11 2.16 36.6»
- Qwen2.5-7B fine-tuned (evidence from generation model) (Task A.2 well-being rating, macro F1 over impairment classes): f1 = 34.3 [n = not given]; Table 2: «Ours (w. Gen.) 2.17 1.23 3.60 2.31 34.3»
- Qwen2.5-7B fine-tuned generation-based (Task A.1 evidence identification, overall recall (span-level, BERTScore recall)): other = 50.7 [n = not given]; Table 1: «Ours (G.) 50.7 45.6 49.9 46.5 51.6 44.6»
- Заметка ИИ: CLPsych 2025 shared-task system paper. Metrics (macro F1, MSE, BERTScore recall) are against gold annotations; annotators and unit counts not described. Well-being MSE: 2.01 (class.) and 2.17 (gen.). Summary tasks use NLI consistency, not human agreement. Borderline: annotation procedure not described.

**Решение:** = автор согласен с ИИ

---

### 2 · R20009

**MentalQLM: A lightweight large language model for mental healthcare based on instruction tuning and dual LoRA modules**

2024 · medRxiv · pdf

Открыть: [PDF](../pdf/R20009.pdf) · [текст](../text/R20009.txt) · [онлайн](https://www.medrxiv.org/content/medrxiv/early/2024/12/30/2024.12.29.24319755.full.pdf)

**ИИ предлагает:** + · eligible · none · T1 · Sonnet 5.5

- Конструкт: Depression, stress, interpersonal risk factors (perceived burdensomeness/thwarted belongingness), wellness dimensions, and stress causes in social media posts (IMHI benchmark)
- Тексты: Reddit/SMS social-media posts from the IMHI benchmark (DR, Dreaddit, Irf, MultiWD, SAD); test sets of 405 to 2,441 posts
- Модели: MentalQLM (Qwen1.5-0.5B, dual LoRA), ChatGPT zero-shot and few-shot, GPT-4 few-shot, MentalLlama-7B, MentalLlama-chat-7B, MentalLlama-chat-13B, Qwen1.5/Qwen2 variants
- Эталон (люди): Human-annotated labels of the IMHI benchmark datasets (DR, Dreaddit, Irf, MultiWD, SAD). The paper does not say who annotated them.
- Согласие людей между собой: Not reported
- MentalQLM (Qwen1.5-0.5B) (dual LoRA instruction-tuned, weighted F1, mean over 5 datasets): f1 = 77.76 [n = 5 test sets]; Table III, p.7: «MentalQLM (Our Model) 0.5B 84.20 82.85 76.81 77.88 67.06 77.76»
- MentalLlama-chat-13B (instruction-tuned, weighted F1 mean): f1 = 75.34 [n = 5 test sets]; Table III, p.7: «MentalLlama-chat-13B 13B 85.68 75.79 76.49 75.11 63.62 75.34»
- ChatGPT (few-shot, weighted F1 mean): f1 = 66.28 [n = 5 test sets]; Table III, p.7: «ChatGPTFS 175B 84.22 75.38 43.31 64.93 63.56 66.28»
- ChatGPT (zero-shot, weighted F1 mean): f1 = 57.47 [n = 5 test sets]; Table III, p.7: «ChatGPTZS 175B 82.41 71.79 41.33 62.72 54.05 57.47»
- GPT-4 (few-shot, weighted F1 mean): f1 = 66.04 [n = 5 test sets]; Table III, p.7: «GPT4FS 1.76T 82.0 78.18 51.75 62.58 55.68 66.04»
- Заметка ИИ: Model-development paper that reports weighted F1 against the human-annotated IMHI labels. The paper does not say who produced the labels, so check whether they come from annotators or from self-reports and metadata. GPT-4o judging of reasoning quality has no human comparison. No human-human agreement is reported.

**Решение:** = автор согласен с ИИ

---

### 3 · R20013

**InstructERC: Reforming Emotion Recognition in Conversation with a Retrieval Multi-task LLMs Framework**

2023 · arXiv.org · pdf

Открыть: [PDF](../pdf/R20013.pdf) · [текст](../text/R20013.txt) · [онлайн](https://arxiv.org/pdf/2309.11911)

**ИИ предлагает:** ? · unclear · other · T1 · Sonnet 5.5

- Конструкт: Utterance-level emotion labels in conversations (IEMOCAP, MELD, EmoryNLP)
- Тексты: Dialogue utterances from acted conversations and TV-show dialogues (IEMOCAP, MELD, EmoryNLP)
- Модели: Fine-tuned (LoRA) ChatGLM, ChatGLM2, Llama, Llama2 (7B); zero-shot ChatGPT3.5
- Эталон (люди): Benchmark gold emotion labels. The annotator details are in an appendix that isn't in the text.
- Согласие людей между собой: Not reported
- Llama2-7B (LoRA + InstructERC, IEMOCAP): f1 = 71.39 [n = not given]; Table 1: «Llama2† 71.39 69.15 41.37 60.64»
- Llama2-7B (LoRA + InstructERC, MELD): f1 = 69.15 [n = not given]; Table 1: «Llama2† 71.39 69.15 41.37 60.64»
- Llama2-7B (LoRA + InstructERC, EmoryNLP): f1 = 41.37 [n = not given]; Table 1: «Llama2† 71.39 69.15 41.37 60.64»
- ChatGPT3.5 (Zero-shot, IEMOCAP/MELD/EmoryNLP): f1 = 53.38 / 65.07 / 37.00 [n = not given]; Table 1: «ChatGPT3.5† 53.38 65.07 37.00 51.81»
- Возможный дубль: none noted
- Заметка ИИ: General NLP emotion-recognition benchmark (weighted F1 against dataset gold labels). The texts are acted or TV dialogue, not clinical. Whether humans annotated the labels isn't stated in the text we received, and the dataset appendix is missing. A reviewer should decide on I2 and the label provenance; E3 is possible.

**Решение:** + T1 решение Claude по поручению автора: те же датасеты (IEMOCAP, MELD, EmoryNLP) с метками людей включены в ST010 и ST345

---

### 4 · R20016

**Reflective Practices and Self-Regulated Learning in Designing with Generative Artificial Intelligence: An Ordered Network Analysis**

2024 · Journal of Science Education and Technology · pdf

Открыть: [PDF](../pdf/R20016.pdf) · [текст](../text/R20016.txt) · [онлайн](https://cdr.lib.unc.edu/downloads/0p096n43c)

**ИИ предлагает:** -2 · not_eligible · E5_no_generative_llm · none · Sonnet 5.5

- Конструкт: Reflective design practices and self-regulated learning (SRL) in think-aloud utterances during brainstorming with ChatGPT
- Тексты: Think-aloud transcripts from 17 designers (about 88 utterances each) and their design sketches
- Модели: ChatGPT 3.5 was the tool participants used. It did not code or rate anything.
- Эталон (люди): Human researchers coded the utterances and two human coders scored the sketches.
- Согласие людей между собой: Cohen's kappa between two human coders per code in Table 1, ranging from 0.74 to 1. Sketch rubric: same scores 90% of the time on 29% of the sketches.
- Заметка ИИ: ChatGPT was the object of study, not a rater. All coding was done by humans, so there is no LLM–human agreement statistic.

**Решение:** = автор согласен с ИИ

---

### 5 · R20031

**EmotionQueen: A Benchmark for Evaluating Empathy of Large Language Models**

2024 · Annual Meeting of the Association for Computational Linguistics · pdf

Открыть: [PDF](../pdf/R20031.pdf) · [текст](../text/R20031.txt) · [онлайн](https://aclanthology.org/2024.findings-acl.128.pdf)

**ИИ предлагает:** + · eligible · none · T4 · Sonnet 5.5

- Конструкт: Empathy and emotion/intent recognition quality of LLM responses to synthetic user statements (PASS and WIN scores)
- Тексты: LLM-generated (GPT-4) synthetic user statements (10,000 across 5 life scenarios) and responses from 11 LLMs; 1000 responses per task rated by humans
- Модели: GPT-4 as automatic judge (0/1 PASS and WIN); evaluated LLMs include Claude2, LLaMA2, GPT-3.5, GPT-4, BLOOM, Falcon, Vicuna
- Эталон (люди): Three volunteer female graduate students in psychology scored responses with the same PASS/WIN metrics
- Согласие людей между собой: Krippendorff's alpha was computed, and ratings below 0.7 were discarded and replaced. No value is reported.
- GPT-4 (judge) (Automatic vs human scores, normalized to a 1-100 scale, across LLMs): pearson = 0.991 [n = 1000 statements]; Section 3.3, Question 4 (p. 7); Fig. 6: «The Pearson correlation coefficient achieves 0.991, indicating a strong alignment.»
- Заметка ИИ: Mainly a benchmark of LLMs as responders, but GPT-4 also judges response empathy and is compared with humans. The r=0.991 is computed on per-model aggregates (about 12 points, Fig. 6), not per unit, so I5 is borderline. Table 6 is emotion classification accuracy against dataset labels.

**Решение:** = автор согласен с ИИ

---

### 6 · R20055

**Integrating Expert Knowledge into Large Language Models Improves Performance for Psychiatric Reasoning and Diagnosis**

2025 · medRxiv · pdf

Открыть: [PDF](../pdf/R20055.pdf) · [текст](../text/R20055.txt) · [онлайн](https://www.medrxiv.org/content/medrxiv/early/2025/07/21/2025.07.19.25331840.full.pdf)

**ИИ предлагает:** -4 · not_eligible · E2_external_criterion · none · Sonnet 5.5

- Конструкт: DSM-5-TR psychiatric diagnosis from case vignettes
- Тексты: 93 DSM-5-TR Clinical Cases vignettes (55 test set)
- Модели: GPT-3.5, GPT-4, GPT-4o (base prompting vs decision-tree prompting)
- Эталон (люди): Author-designated diagnoses from the casebook (not independent human coders applying a scheme)
- Согласие людей между собой: Not reported
- Возможный дубль: none
- Заметка ИИ: The LLMs predict diagnoses. The reference is the casebook author's diagnosis, which works as an external diagnostic criterion, not human coding. PPV, sensitivity and F1 are reported. The paper has no human-coder comparison arm. Borderline: a reviewer could treat it as a benchmark.

**Решение:** = автор согласен с ИИ

---

### 7 · R20058

**Towards Augmenting Mental Health Personnel with LLM Technology to Provide More Personalized and Measurable Treatment Goals for Patients with Severe Mental Illnesses**

2023 · International Conference on Pervasive Computing Technologies for Healthcare · europepmc_xml

Открыть: [текст](../text/R20058.txt) · [онлайн](https://core.ac.uk/works/156571236)

**ИИ предлагает:** -3 · not_eligible · E1_humans_rate_llm · none · Sonnet 5.5

- Конструкт: Quality of LLM-generated behavioral treatment goals rated on SDT and Goal Setting Theory dimensions (autonomy, competence, clarity, etc.)
- Тексты: GPT-3-generated behavioral goals for two outcome goals (not patient or clinical texts being coded)
- Модели: GPT-3 (generator of goals, not a rater)
- Эталон (люди): 8 students rated the LLM-generated goals on 5-point Likert scales
- Согласие людей между собой: Not reported
- Заметка ИИ: Prototype and feasibility study. Humans rate GPT-3 outputs, and the LLM does not rate or code any units. No LLM-human agreement statistic is reported.

**Решение:** = автор согласен с ИИ

---

### 8 · R20059

**AI in relationship counselling: Evaluating ChatGPT's therapeutic capabilities in providing relationship advice**

2024 · Comput. Hum. Behav. Artif. Humans · pdf

Открыть: [PDF](../pdf/R20059.pdf) · [текст](../text/R20059.txt) · [онлайн](https://osf.io/3zajt/download)

**ИИ предлагает:** -3 · not_eligible · E1_humans_rate_llm · none · Sonnet 5.5

- Конструкт: Quality of ChatGPT (GPT-4) relationship-therapy responses (empathy, reflection, validation, therapeutic questioning)
- Тексты: 20 single-session ChatGPT relationship-advice conversations and user interviews
- Модели: GPT-4 / ChatGPT (as the object being evaluated, not as a rater)
- Эталон (люди): Two authors coded the chatbot sessions on 21 codes; users were interviewed
- Согласие людей между собой: Author inter-rater reliability r = .897, k = .661 (p.10-11)
- Заметка ИИ: Humans (the authors) rate ChatGPT outputs. No LLM rates the same units, so ChatGPT is the object and not the rater. The user-vs-author agreement percentages are human-human, not LLM-human.

**Решение:** = автор согласен с ИИ

---

### 9 · R20061

**Promises and pitfalls of large language models in psychiatric diagnosis and knowledge tasks**

2025 · British Journal of Psychiatry · pdf

Открыть: [PDF](../pdf/R20061.pdf) · [текст](../text/R20061.txt) · [онлайн](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/98695877D5D7A59CA6197E3D6796E01A/S0007125024002071a.pdf/div-class-title-promises-and-pitfalls-of-large-language-models-in-psychiatric-diagnosis-and-knowledge-tasks-div.pdf)

**ИИ предлагает:** -4 · not_eligible · E2_external_criterion · none · Sonnet 5.5

- Конструкт: Psychiatric diagnosis of DSM-5-TR clinical cases and DSM knowledge multiple-choice questions
- Тексты: 21 DSM-5-TR clinical case vignettes and 95 multiple-choice self-exam questions (published textbook material)
- Модели: GPT-4, LLaMA2-70B, Mixtral-45B, Vicuna-13B, Gemma-7B (zero-shot)
- Эталон (люди): No human coding of the texts. The reference is the textbook answer key. 11 psychiatry residents were comparators, not the reference.
- Согласие людей между собой: Not reported
- Заметка ИИ: Letter. LLMs and residents were both scored against the textbook answer key (GPT-4 diagnosis F1 63.41%, knowledge accuracy 85.05%). This is a benchmark of correct answers, not agreement with human coders of the same units. It is also largely a knowledge exam task. No LLM-human agreement statistic is reported. The Jaccard similarity between residents and GPT-4 is not agreement on a coding scheme.

**Решение:** = автор согласен с ИИ

---

### 10 · R20063

**Leveraging Large Language Models for Mental Health Prediction via Online Text Data**

2023 · arXiv.org · pdf

Открыть: [PDF](../pdf/R20063.pdf) · [текст](../text/R20063.txt) · [онлайн](https://arxiv.org/pdf/2307.14385)

**ИИ предлагает:** + · eligible · none · T3 · Sonnet 5.5

- Конструкт: Stress, depression severity, suicide ideation and C-SSRS suicide risk level in Reddit/Twitter/SMS posts
- Тексты: Social media posts (Reddit, Twitter, SMS-like messages) from Dreaddit, DepSeverity, SDCNL, CSSRS-Suicide, Red-Sam, Twt-60Users, SAD datasets with human annotations
- Модели: Alpaca 7B, Alpaca-LoRA, FLAN-T5 XXL, LLaMA2 70B, GPT-3.5, GPT-4 (zero-shot, few-shot); finetuned Mental-Alpaca and Mental-FLAN-T5
- Эталон (люди): Human annotations in the source datasets (multiple annotators for Dreaddit, 2 for DepSeverity, 4 psychiatrists for CSSRS-Suicide, 2 experts for Red-Sam, 2 for Twt-60Users, manual labels for SDCNL)
- Согласие людей между собой: Not reported in this paper.
- GPT-4 (zero-shot, Task #5 binary suicide risk (CSSRS-Suicide)): accuracy = 0.760 [n = 100 users]; Table 4, p.12: «GPT-4ZS 0.700 0.719 0.588 0.644 0.760 0.418 (balanced accuracy)»
- GPT-4 (zero-shot best, Task #1 binary stress (Dreaddit)): accuracy = 0.725 [n = 715 posts]; Table 4, p.12: «GPT-4ZS_best 0.725±0.009 (balanced accuracy)»
- GPT-3.5 (few-shot, Task #1 Dreaddit): accuracy = 0.721 [n = 715 posts]; Table 4, p.12: «GPT-3.5FS 0.721±0.010 (balanced accuracy)»
- Mental-Alpaca (instruction finetuned, Task #1 Dreaddit): accuracy = 0.816 [n = 715 posts]; Table 4, p.12: «Mental-Alpaca 0.816±0.006 (balanced accuracy)»
- Mental-FLAN-T5 (instruction finetuned, Task #5 binary suicide risk): accuracy = 0.868 [n = 100 users]; Table 4, p.12: «Mental-FLAN-T5 ... 0.868±0.006 (balanced accuracy)»
- LLaMA2 70B (zero-shot best, Task #5): accuracy = 0.722 [n = 100 users]; Table 4, p.12: «LLaMA2ZS_best ... 0.722±0.039 (balanced accuracy)»
- Возможный дубль: None known; this is the arXiv version (2307.14385v4) of the IMWUT 2024 article.
- Заметка ИИ: Only balanced accuracy against human-annotated labels is reported (fits I5). Main task is T3; Tasks 1, 2 and 4 are binary presence labels (closer to T1). Labels are consensus labels from the source datasets. Tables 4, 9 and 10 give more models and tasks than listed here.

**Решение:** = автор согласен с ИИ

---

### 11 · R20082

**Can generative AI infer thinking style from language? Evaluating the utility of AI as a psychological text analysis tool**

2024 · Behavior Research Methods · pdf

Открыть: [PDF](../pdf/R20082.pdf) · [текст](../text/R20082.txt) · [онлайн](https://link.springer.com/content/pdf/10.3758/s13428-024-02344-0.pdf)

**ИИ предлагает:** -7 · not_eligible · no_human_coding · none · Sonnet 5.5

- Конструкт: Analytic thinking (thinking style) scores from ChatGPT versus LIWC dictionary-based analytic thinking index
- Тексты: arXiv abstracts, UK petitions, Yelp reviews, death row last statements (about 16,000 texts); also participant writing samples from prior work
- Модели: GPT-3.5 (gpt-3.5-turbo-0301) and GPT-4 via the OpenAI API, three prompts (general, specific, formula)
- Эталон (люди): None. The reference is the LIWC dictionary score. No human coders applied the scheme to the texts.
- Согласие людей между собой: Not applicable
- Заметка ИИ: The reference is the LIWC dictionary tool, not human coders. The authors list comparisons to human ratings as future work. The need-for-cognition analysis uses an external questionnaire criterion. The exclusion could also be coded E2 or E5.

**Решение:** = автор согласен с ИИ

---

### 12 · R20145

**Diagnosing schizophrenia spectrum disorders: Large language models ( LLMs ) vs. leading international psychiatrists ( LIPs )**

2025 · Psychiatry and Clinical Neurosciences · europepmc_xml

Открыть: [текст](../text/R20145.txt) · [онлайн](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12405820/fullTextXML)

**ИИ предлагает:** -4 · not_eligible · E2_external_criterion · none · Sonnet 5.5

- Конструкт: Diagnosis of schizophrenia spectrum disorders from two clinical vignettes
- Тексты: Two simulated clinical vignettes (David, Michael) of schizophrenia spectrum disorders
- Модели: DeepSeek-V3, Llama 3.1 405B, Mixtral-8x22B, Phi-3.5-mini, Ministral-8B, Llama-3.2-3B, GPT-4o, Claude-3.5-Haiku, Gemini Flash 1.5
- Эталон (люди): None; LLM diagnoses were compared with the vignettes' known correct diagnosis and with the published accuracy of psychiatrists (33% got both right)
- Согласие людей между собой: Not reported
- Заметка ИИ: Research letter. It tests LLM diagnostic accuracy on 2 vignettes against the known diagnosis (a criterion). Humans did not code the same units with the LLM. It reports no unit-level agreement statistics.

**Решение:** = автор согласен с ИИ

---

### 13 · R20159

**Assessment of a Zero-Shot Large Language Model in Measuring Documented Goals-of-Care Discussions**

2025 · Journal of Pain and Symptom Management · europepmc_xml

Открыть: [текст](../text/R20159.txt) · [онлайн](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12140542/fullTextXML)

**ИИ предлагает:** -5 · not_eligible · E3_not_psychological · none · Sonnet 5.5

- Конструкт: Documented goals-of-care discussions in EHR clinical notes (palliative care process measure)
- Тексты: EHR progress notes of hospitalized seriously ill adults (University of Washington trials, 2018-2023)
- Модели: Llama 3.3 70B zero-shot; BioClinicalBERT (comparator)
- Эталон (люди): Manual chart abstraction by abstractors (consensus); Trial 2 used BERT-screened human abstraction
- Согласие людей между собой: Not reported
- Llama 3.3 (zero-shot) (Trial 2 held-out test set, note-level, max F1): f1 = 0.83 [n = 2,136 notes]; Abstract / Results: «Llama 3.3: AUC 0.979, AUPRC 0.873, and F1 0.83»
- Заметка ИИ: The construct is a clinical documentation or process measure (palliative care communication), not a mental state or psychological treatment process. I judged it outside I2. The reviewer may reconsider: the LLM was compared with human labels (F1, AUC). Trial 2 human labels were partly BERT-screened.

**Решение:** = автор согласен с ИИ

---

### 14 · R20173

**Designing Emotion Regulation Support in Online Group Learning: Insights from an LLM-Based Support Agent**

2026 · Research Square · pdf

Открыть: [PDF](../pdf/R20173.pdf) · [текст](../text/R20173.txt) · [онлайн](https://www.researchsquare.com/article/rs-8443551/latest.pdf)

**ИИ предлагает:** + · eligible · none · T1 · Sonnet 5.5

- Конструкт: Emotion regulation modes (individual ER per Gross PMER, co-regulation, socially shared regulation) in chatbot messages
- Тексты: GPT-4 chatbot (GroupBuddy) messages in Discord group channels; coded subset is 10% of n=75 messages
- Модели: ChatGPT o1 (prompted with codebook) as second coder
- Эталон (люди): One human researcher independently coded the same 10% subset
- Согласие людей между собой: Not applicable (single human coder)
- ChatGPT o1 (Codebook prompt, after two refinement iterations, 10% subset vs human researcher): cohen_kappa = 0.85 [n = ~8 (10% of 75)]; p.10, Qualitative analysis: «It took two iterations of refining the codebook and the prompt to achieve a satisfactory level of agreement (κ = 0.85)»
- Заметка ИИ: Weak fit: the units are chatbot (helper) responses, and the construct is ER strategies in an educational setting. The kappa is on a small subset and was obtained after prompt refinement on that same subset. Humans and the LLM applied the same codebook, so it is borderline eligible. The reviewer should check the construct and the refinement iterations.

**Решение:** = автор согласен с ИИ

---

### 15 · R20178

**Can LLMs Get High? A Dual-Metric Framework for Evaluating Psychedelic Simulation and Safety in Large Language Models**

2026 · Research Square · pdf

Открыть: [PDF](../pdf/R20178.pdf) · [текст](../text/R20178.txt) · [онлайн](https://www.researchsquare.com/article/rs-8682370/latest.pdf)

**ИИ предлагает:** -7 · not_eligible · no_human_coding · none · Sonnet 5.5

- Конструкт: Mystical experience (MEQ-30) and semantic similarity of LLM-generated psychedelic narratives
- Тексты: 3,000 LLM-generated psychedelic trip narratives; 1,085 human Erowid trip reports (used only as a similarity reference)
- Модели: Gemini 2.5, Claude Sonnet 3.5, ChatGPT-5, Llama-2 70B, Falcon 40B (the same model completes the MEQ-30 on its own narrative)
- Эталон (люди): None. Humans did not code or rate any units. Erowid reports serve only as an embedding-similarity corpus.
- Согласие людей между собой: Not reported
- Возможный дубль: None
- Заметка ИИ: The LLMs generate the narratives and self-rate them on the MEQ-30. No human coder applied the MEQ-30 to the same units, and no LLM–human agreement statistic is reported. The only correlation reported is between the two LLM-derived metrics (Pearson r = 0.661), which is not an agreement statistic against a human reference.

**Решение:** = автор согласен с ИИ

---

### 16 · R20181

**Architectural Transparency in LLM-Based Cognitive Assessment: A Multidimensional TRACE-ED Evaluation of Single-Agent and Multi-Agent Systems**

2026 · Research Square · pdf

Открыть: [PDF](../pdf/R20181.pdf) · [текст](../text/R20181.txt) · [онлайн](https://www.researchsquare.com/article/rs-8985839/latest.pdf)

**ИИ предлагает:** -5 · not_eligible · E3_not_psychological · none · Sonnet 5.5

- Конструкт: Educational short-answer grading (rubric indicators) and transparency of LLM scoring architecture; not a psychological or clinical construct
- Тексты: 10 synthetic student short-answer responses, 3 rubric indicators
- Модели: Unspecified LLM in single-agent vs multi-agent architectures (900 Monte Carlo runs)
- Эталон (люди): None; no human raters. The authors list human-rater benchmarking as future work.
- Согласие людей между собой: Not reported
- Заметка ИИ: The study is about educational grading and architectural transparency. The only ICC is for repeated-run reliability of the LLM (multi-agent ICC(1,k)=0.9921), not LLM–human agreement. There is no human coding and the construct is not psychological.

**Решение:** = автор согласен с ИИ

---

### 17 · R20203

**Risk Governance for Generative AI Mental Health Support: A Multi-Turn Safety Architecture**

2026 · Research Square · pdf

Открыть: [PDF](../pdf/R20203.pdf) · [текст](../text/R20203.txt) · [онлайн](https://www.researchsquare.com/article/rs-10279940/latest.pdf)

**ИИ предлагает:** + · eligible · none · T3 · Sonnet 5.5

- Конструкт: Mental health risk in multi-turn conversations (safe vs self-harm vs harm-to-others), detected by a safety classifier plus an LLM pass-gate. Secondary: clinicians rate escalation appropriateness and rapport of chatbot replies (T4-like, humans rate only).
- Тексты: 662 synthetic multi-turn LLM–patient-simulator transcripts (9,348 turns) grounded in CRADLE Bench Reddit narratives. External checks used NVIDIA Aegis 2.0 prompts and CRADLE Bench posts.
- Модели: The architecture combines a 4B context-aware safety classifier (Farinhas et al.; probably a fine-tuned decoder LLM, not confirmed in the text) with a GPT-5-chat reasoning pass-gate. The conversational LLMs were GPT-5-chat and Qwen3.5-27B.
- Эталон (люди): Five doctoral-level licensed US clinical psychologists labelled each turn for risk. A conversation counted as at risk if at least one annotator flagged any turn (conservative reference).
- Согласие людей между собой: Conversation level: Krippendorff's alpha 0.79, Gwet's AC1 0.80. Turn level: alpha 0.60, AC1 0.88.
- Safety architecture (4B classifier + GPT-5-chat pass-gate) (Conversation-level risk detection, overall, safety layer ON): f1 = 0.92 [n = 400 transcripts]; Table 1; Results p.4: «overall specificity of 0.85 (95% CI: 0.78;0.91), sensitivity of 0.92 (95% CI: 0.88;0.95), and F1 score of 0.92 (95% CI: 0.89;0.94)»
- Safety architecture (4B classifier + GPT-5-chat pass-gate) (Self-harm category): f1 = 0.95 [n = 400 transcripts]; Table 1: «Self-harm 1.00 precision; 0.91 sensitivity; 1.00 specificity; 0.95 (0.92;0.97) F1»
- Safety architecture (4B classifier + GPT-5-chat pass-gate) (Harm-to-others category): f1 = 0.88 [n = 400 transcripts]; Table 1: «Harm-to-others 0.84 precision; 0.92 sensitivity; 0.93 specificity; 0.88 (0.83;0.92) F1»
- Safety architecture (4B classifier + GPT-5-chat pass-gate) (External CRADLE Bench single posts): f1 = 0.89 [n = not given]; Results p.3: «sensitivity was 0.88 (95% CI: 0.81; 0.93), specificity 0.94 (95% CI: 0.90; 0.97), and F1 score 0.89 (95% CI: 0.84; 0.93)»
- Safety architecture (4B classifier + GPT-5-chat pass-gate) (External NVIDIA Aegis 2.0 single-turn prompts): f1 = 0.93 [n = not given]; Results p.3: «sensitivity of 0.88 (95% CI: 0.82; 0.92), a specificity of 0.98 (95% CI: 0.96; 0.99), and an F1 score of 0.93 (95% CI: 0.90; 0.95)»
- Заметка ИИ: Borderline on I3: the rater is a 4B classifier plus a GPT-5-chat pass-gate; the text does not say the 4B model is a decoder LLM. Statistics are sensitivity, specificity and F1, not kappa. Turn-level results are in Supplementary Table 3 (not provided). Reference label is a union of annotators.

**Решение:** = автор согласен с ИИ
