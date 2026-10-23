# Проверка с метками ИИ, часть 6

Записи 751–900 из 1304, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

**Как размечать.** Под каждой записью есть строка **Решение:** — допишите в неё код, после кода можно оставить заметку.

| Код | Что значит |
| --- | --- |
| `+` | включить: эмпирическое исследование, где генеративная LLM кодирует, размечает, оценивает или подсчитывает психологические или клинические тексты, и те же тексты кодируют люди по той же схеме (эксперты, клиницисты, обученные кодировщики или краудворкеры) |
| `?` | не уверен — в сомнениях выбирайте это: лишний полный текст дешевле пропущенного исследования |
| `-1` | исключить: обзор, протокол, комментарий, позиция, руководство |
| `-2` | исключить: люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает |
| `-3` | исключить: эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность) |
| `-4` | исключить: нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация |
| `-5` | исключить: нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM |
| `-6` | исключить: другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM |
| `-7` | исключить: другое — напишите почему |

Пример: `**Решение:** -2 люди оценивают ответы чат-бота`. Символы `+ ? -` и цифры одинаковы на русской и английской раскладке.

**Что ищем:** согласие LLM с людьми на психологических текстах — четыре типа задач: кодирование по кодбуку, подсчёт методик, клинические оценки риска и тяжести, LLM-судья ответов в психическом здоровье. Цифры согласия часто лежат в таблицах, а аннотация о них молчит. Классификация психологических текстов LLM, где неясно, кто ставил эталонные метки (люди или самоотчёт), — `?`. Подробно — протокол, §8.

---

### 751 · R4662

**Validation of the Episodic Specificity Coder (ESCODER): an LLM-based tool for automated scoring of the Autobiographical Memory Test**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/yxq3k

ESCODER is a research tool that uses Google Gemini’s Large Language model to classify responses to the Autobiographical memory Test (AMT) into five categories. Specific, extended, categorical, semantic associate and omission. Following the coding scheme of Takano et al. (2018). The tool was developed by Dr Tom Barry to enable researchers to score autobiographical memory data at scale without hand coding. To date, this tool’s classifications have not been formally validated against human coders. This study conducts the first pre-registered validation of ESCODER, using baseline AMT responses from the c-MEST randomised controlled trial (Halford et al., 2021). This study provides us with an existing dataset of memory responses produced by adults with major depressive disorder. Each response will be classified by ESCODER and independently by one of two trained human coders using the same five-class scheme. Agreement is measured using Cohen’s Kappa.

**ИИ:** разошлись — Opus ? (другое: Pre-registered study comparing Gemini with human AMT specificity coding (kappa); fits, but it's a registration and may have no results yet.); Sonnet + (подсчёт методики: Gemini-based ESCODER scores Autobiographical Memory Test responses; pre-registered validation against trained human coders using Cohen's kappa.)

**Решение:** +

---

### 752 · R4674

**LLARS: Enabling Domain Expert & Developer Collaboration for LLM Prompting, Generation and Evaluation**

2026 · International Joint Conference on Artificial Intelligence · journalarticle, conference, preprint/article · en · https://doi.org/10.24963/ijcai.2026/995

We demonstrate LLARS (LLM Assisted Research System), an open-source platform that bridges the gap between domain experts and developers for building LLM-based systems. It integrates three tightly connected modules into an end-to-end pipeline: Collaborative Prompt Engineering for real-time co-authoring with version control and instant LLM testing, Batch Generation for configurable output production across user-selected prompts $\times$ models $\times$ data with cost control, and Hybrid Evaluation where human and LLM evaluators jointly assess outputs through diverse assessment methods, with live agreement metrics and provenance analysis to identify the best model-prompt combination for a given use case. New prompts and models are automatically available for batch generation and completed batches can be turned into evaluation scenarios with a single click. Interviews with six domain experts and three developers in online counselling confirmed that LLARS feels intuitive, saves considerable time by keeping everything in one place and makes interdisciplinary collaboration seamless. Accepted at IJCAI-ECAI 2026 Demonstrations Track. Demo video: https://youtu.be/3QaKouwr4gU

**ИИ:** разошлись — Opus ? (другое: Demo of an online-counselling platform that reports live human–LLM evaluator agreement; unclear whether any empirical agreement data on psychological constructs is reported.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Demo of a platform for prompt engineering and hybrid human-LLM evaluation; no specific psychological coding task with reported LLM-human agreement.)

**Решение:** -

---

### 753 · R4686

**Large Language Models for Scoring Formative and Summative Objective Structured Clinical Examinations: Agreement, Discordance Patterns, and Interchangeability in an Observational Study (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.114564

BACKGROUND Large language models (LLMs) have shown promise for automated scoring of objective structured clinical examinations (OSCEs), but evidence across diverse assessment items and authentic clinical encounters remains limited. Whether agreement with human examiners is sufficient to support their replacement, particularly in high-stakes assessments, is uncertain. OBJECTIVE To evaluate agreement between transcript-based LLM scoring and paired human examiners across summative and formative OSCEs, assess the consequences of replacing human examiners with LLMs, and characterize recurrent mechanisms of disagreement. METHODS In this prospective observational study, authentic OSCE encounters were independently scored by two human examiners. Transcripts were assessed by two general-purpose LLMs (GPT-5.0-5.5 Thinking and Gemini 2.5-3.1 Pro) using station-specific checklists and a standardized zero-shot prompt. Agreement was evaluated for binary clinical items and ordinal attitude and communication items. For summative OSCEs, alternative human-LLM scoring configurations were compared with the mean score of both human examiners to assess changes in pass-fail classification and within-station ranking. Clinical-item variants assessed in at least 15 encounters and showing mean LLM-human discordance ≥15% underwent exploratory qualitative analysis. RESULTS The study included 1,423 encounters across 35 stations, comprising 975 summative encounters from six stations and 448 formative encounters from 29 stations. These generated 18,551 clinical-item ratings per rater across 482 distinct clinical-item variants, and 3,376 attitude-item ratings per rater across 14 domains. Exact clinical-item agreement was 94.1% between human examiners, compared with 87.5% for ChatGPT-human and 87.3% for Gemini-human comparisons (Cohen κ=0.88, 0.75, and 0.75, respectively). The mean number of discordant clinical items per encounter was 0.77 between humans versus 1.63-1.65 between LLMs and humans. Exact agreement for attitude and communication items was lower (55.6% human-human versus 37.7%-39.4% LLM-human). In summative OSCEs, pass-fail classifications changed in 5.0% of encounters with a single human examiner, 7.1%-8.6% with human-LLM pairs, and 12.6%-14.5% with LLM-only configurations. Median absolute within-station percentile shifts were 2.5, 5.5, and 8.5-9.7 points, respectively. Among 279 clinical-item variants assessed in at least 15 encounters, 91 (32.6%) met the ≥15% discordance threshold and were classified into seven recurrent mechanisms: unobservable gestures (n=3), two-stage station processes (n=9), composite criteria (n=19), completeness threshold ambiguity (n=13), semantic equivalence (n=22), open versus targeted questioning (n=17), and contextual or clinical inference (n=8). CONCLUSIONS General-purpose LLMs achieved high agreement with human examiners for clinical-item scoring but were not interchangeable with them for individual assessment decisions or ranking. These findings support further investigation of LLM-assisted formative assessment while highlighting the need for task-specific adaptation, improved scoring rubrics, and human oversight before implementation in high-stakes summative OSCEs.

**ИИ:** ? · обе модели · неясен конструкт · LLMs vs human examiners scoring OSCE transcripts; mostly clinical-skill checklists, but includes communication/attitude ratings that may count as interpersonal constructs.

**Решение:** =

---

### 754 · R4687

**Model in Distress: Sentiment Analysis on French Synthetic Social Media**

2026 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.18653/v1/2026.findings-acl.2132

Automated analysis of customer feedback on social media is hindered by three challenges: the high cost of annotated training data, the scarcity of evaluation sets, especially in multilingual settings, and privacy concerns that prevent data sharing and reproducibility.We address these issues by developing a generalizable synthetic data generation pipeline applied to a case study on customer distress detection in French public transportation.Our approach utilizes backtranslation with fine-tuned models to generate 1.7 million synthetic tweets from a small seed corpus, complemented by synthetic reasoning traces.We train 600M-parameter reasoners with English and French reasoning that achieve 77-79% accuracy on human-annotated evaluation data, matching or exceeding SOTA proprietary LLMs and specialized encoders.Beyond reducing annotation costs, our pipeline preserves privacy by eliminating the exposure of sensitive user data.Our methodology can be adopted for other use cases and languages.DistressedModel/Distressed-Model-Data You are a **clinician-like annotator** assessing a single tweet for potential **distress and psychometric states**.You work **bilingually (French/English)**: interpret and quote French text accurately, but write all analysis in English.Use concise, evidence-based prose.You have been submitted the following tweet: {tweet} You also no in advance the final judgement: {judgement} Now try to write a reasoning workflow according to the guidelines below that would converge to this final judgement.### 1) Pragmatics * Contextualize: is it a * Identify tone and stance: literal report / complaint / rhetorical slogan / meme or sarcasm / hyperbole / bureaucratic or formal.* Who speaks about whom? (self vs. other vs. unspecified).* Temporal index: now / recent / past / unknown.* Quote 1-3 exact spans that anchor these judgments.### 2) Distress **Goal:** Determine whether any form of distress is present.* Decide: **present / absent / external** **Criteria for present:** * Author is a victim or a direct witness to physical violence or danger.This could be caused by other travellers or agents.Common issues include being thrown on the rails, attacked by a third party,

**ИИ:** ? · обе модели · неясен конструкт · LLMs are evaluated against human labels for distress in French transit tweets, but "customer distress" may be about service complaints rather than psychological distress.

**Решение:** =

---

### 755 · R4693

**Evaluating LLM-Based Coders in Psychological Assessment: A Validation Framework With Application to the Rorschach Morbid Content Variable.**

2026 · Assessment · journal article, med, journalarticle · eng · https://doi.org/10.1177/10731911261455137

Large language models (LLMs) are increasingly used to support psychological assessment, but standards for evaluating their scoring accuracy remain limited. This article introduces a clear, reproducible validation framework to evaluate LLM-based scoring systems. The framework separates pre-validation steps (e.g., balancing base rates, refining prompts, and comparing models) from a standardized validation phase focused on reliability and validity benchmarks. We demonstrate its application with a case study of Morbid Content (MOR) scoring in the Rorschach task, using a two-agent LLM workflow. In an independent dataset ( n = 84; 2,176 responses) with natural MOR base rates, the final LLM coder showed good response level agreement ( kappa = .72-.74) and excellent protocol level agreement ( ICC = 0.94-0.95) with assessors, near-perfect consistency with itself (ICC = 0.97-0.99), and replicated external validity ( r = .59-.71) that matched human coders ( r = .54-.65). This article offers a practical guide for evaluating automated coders in psychological testing and discusses practical decisions and ethical considerations.

**ИИ:** + · обе модели · подсчёт методики · An LLM scored Rorschach Morbid Content and its agreement with human assessors was reported (kappa .72–.74, ICC .94–.95).

**Решение:** =

---

### 756 · R4699

**Supporting Student Mental Health With the Safespace Generative AI Chatbot: Mixed Methods Feasibility Study.**

2026 · JMIR formative research · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.2196/85427

Abstract Background Generative artificial intelligence (GenAI) chatbots have the potential to provide personalized mental health support to individuals at scale. Objective This study evaluates the feasibility and usage patterns of the Safespace GenAI chatbot, an artificial intelligence (AI)–driven smartphone app that offers a large language model–powered interactive chatbot to support mental health. Methods Using a mixed methods approach, we explored baseline attitudes toward GenAI chatbots and chatbot usage patterns, conducted a qualitative content analysis of participants’ experiences, and descriptively assessed patterns related to preintervention depressive symptoms. The study included an initial sample of 42 university students, 20 of whom actively used the chatbot over 2 to 4 weeks, generating 286 user-chatbot interactions. Results Preintervention surveys indicated that the majority of participants anticipated that the chatbot would be helpful (27/42, 64%) and that they trusted its privacy safeguards (39/42, 93%). Usage patterns suggested that the highest levels of interaction occurred early in the morning and late at night, when peer and professional support may be inaccessible. The qualitative analysis indicated that participants appreciated using the chatbot for reflection as a blended-care tool between their counseling sessions, while also naming technical barriers and specific design needs required to sustain engagement. In addition, our exploratory analyses descriptively showed that participants with elevated depression scores engaged in emotional disclosure during 99% (38 sessions with 8 participants) of their sessions, compared to 84% (26 sessions of 12 participants) of those with low symptoms. Due to the small sample size, future adequately powered studies are needed to inferentially examine these observed patterns. Conclusions These findings provide initial insights into the usage and engagement dynamics of the Safespace GenAI chatbot and highlight directions for future research to optimize GenAI-driven mental health interventions.

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Feasibility study of an LLM mental-health chatbot intervention; no LLM coding of text compared against human coders.); Sonnet ? (неясно, сравнивали ли с людьми: Chatbot feasibility study; emotional disclosure in sessions was coded, but the abstract doesn't say whether an LLM coded it or whether humans validated it.)

**Решение:** -

---

### 757 · R4700

**Supporting Student Mental Health With the Safespace Generative AI Chatbot: A Mixed-Methods Feasibility Study**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/g39t5_v1

Background: Generative Artificial Intelligence (genAI) chatbots have the potential to provide personalized mental health support to individuals at scale. Objective: This study evaluates the feasibility and usage patterns of the Safespace genAI chatbot, an AI-driven smartphone application that offers an LLM-powered interactive chatbot to support mental health. Methods: Using a mixed-methods approach, we explored baseline attitudes towards genAI chatbots and chatbot usage patterns, conducted a qualitative content analysis of participants’ experiences, and descriptively assessed patterns related to pre-intervention depressive symptoms. The study included an initial sample of N = 42 university students, n = 20 of whom actively used the chatbot over two to four weeks, generating 286 user-chatbot interactions. Results: Pre-intervention surveys indicated that the majority of participants anticipated the chatbot would be helpful (64%) and that they trusted its privacy safeguards (93%). Usage patterns hinted towards that the highest levels of interaction occurred early in the morning and late at night, when peer and professional support may be inaccessible. The qualitative analysis indicated that participants appreciated using the chatbot for reflection as a blended care tool between their counseling sessions, while also naming technical barriers and specific design needs to sustain engagement. In addition, our exploratory analyses descriptively showed that participants with elevated depression scores engaged in emotional disclosure during 99% of their sessions, compared to 84% for those with low symptoms. Due to the small sample size, future adequately powered studies are needed to inferentially examine these observed patterns. Conclusion: These findings provide initial insights into the usage and engagement dynamics of the Safespace genAI chatbot and highlight directions for future research to optimize genAI-driven mental health interventions. Trial Registration: AEA Registry https://doi.org/10.1257/rct.13291-1.0

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Feasibility study of an LLM chatbot intervention; nothing suggests the LLM coded text and was compared with human coders.); Sonnet ? (неясно, сравнивали ли с людьми: Chatbot feasibility study; "emotional disclosure" in sessions may be LLM-coded with human validation, but the abstract doesn't say.)

**Решение:** -

---

### 758 · R4714

**Comparing AI-Assisted Coding and Traditional Qualitative Analysis: a Study Examining Differences in Methods and Results of AI-Assisted Coding and Traditional Content Coding Using Community Engagement Data Collected During the Development of a Municipal Food Plan.**

2026 · Prevention science : the official journal of the Society for Prevention Research · comparative study, research-article, journal article · eng · https://doi.org/10.1007/s11121-026-01904-4

Abstract Qualitative data poses a challenge for prevention science and public health, as it is critical to explain the context of communities, health, and behavior, yet collecting and analyzing qualitative data using traditional methods is time-intensive and requires extensive training. As artificial intelligence (AI) models have improved, there is a growing interest in using AI to code qualitative data quickly and reliably. This study compares the similarities and differences in methods and results of artificial intelligence (AI)-assisted qualitative analysis to traditional qualitative content analysis using data collected during the development of a city and county-based food plan. In total, 2820 community comments were collected across 43 community events in 27 zip codes across the region between March 2023 and January 2024. AI-assisted analysis was completed using a combination of a transcription app (Post-It Ⓡ ), GPT4 Plus, and GPT for Sheets with oversight from a public health practitioner. Traditional qualitative content analysis was completed with two trained coders who completed codebook development, reliability analysis, and full content coding. Both methods used deductive codes to represent key aspects of the food system and generated inductive codes to represent areas not included by the deductive food system codes. Results found that AI-assisted methods and traditional content analysis produced similar deductive coding results, while inductive coding results were less comparable across methods. Given that qualitative data has become a central part of prevention science, we believe with careful considerations, AI-assisted methods with intentional oversight have the potential to strengthen our ability to process large amounts of qualitative data.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-4 deductive coding of community comments compared with trained human coders; food-system topic codes may not be psychological constructs.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: GPT-4 vs human coders on community comments, but codes are food-system topics, not a psychological or clinical construct.)

**Решение:** -

---

### 759 · R4717

**Graded Sycophancy in the Confidant Role: Audience-Dependent Validation in LLM Workplace Advice**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.21800107

This exploratory study adapts the paired-perspective methodology used by ELEPHANT (Cheng et al., 2025) to workplace human-resources disputes. It examines whether large language models apply a consistent substantive standard when opposing parties describe the same underlying event from incompatible perspectives. Five matched Employee/Manager or Complainant/Counterparty scenarios cover age-discrimination retaliation, disability accommodation, safety whistleblower retaliation, harassment-related social retaliation, and gender-based promotion disparity. Three models—Gemini 3.8 Flash, Claude Sonnet 5, and GPT-5.6 Luna—were evaluated in fresh conversations, producing 90 provider-blinded transcripts with equal replication across providers. The primary framework distinguishes five behavioral dimensions: emotional validation, contested-claim affirmation, active contestation, framing acceptance, and substantive commitment. Primary direction is recorded as a categorical descriptor. Adjacent/subclaim validation was initially coded as an exploratory supplementary dimension, but its boundary with qualified contested-claim affirmation was not applied reliably. It is therefore excluded from the primary framework and provider comparisons, while its scores remain in the supplement for transparency. The primary qualitative coding was conducted by the researcher. After those scores were frozen, Claude Sonnet 5 and MUSe separately scored the 90 blinded transcripts using the same codebook. These AI review passes provide agreement and sensitivity diagnostics rather than independent human validation. Under the strict paired-perspective criterion, which requires direct affirmation of both parties’ mutually incompatible contested claims, none of the three models produced a confirmed bilateral case in the five scenarios. At the response level, direct contested-claim affirmation occurred in 4 of 90 responses, while qualified or direct affirmation occurred in 45 of 90. This difference is the central measurement finding: a binary direct-endorsement rule misses many responses that may still increase a user’s confidence in a disputed interpretation. The observed provider patterns were descriptive rather than absolute. In these scenarios, Gemini more often gave substantive support to the current speaker’s broader interpretation; Claude more often separated emotional validation from factual endorsement and challenged self-serving framing; and GPT-5.6 Luna more often paired emotional validation with low factual commitment and evidence-gathering advice. These tendencies are hypotheses generated from five scenarios, not definitive provider rankings, stable model traits, or claims about internal mechanisms. The paper proposes audience-dependent substantive validation as a hypothesis-generating construct for future sycophancy research. The accompanying supplement contains the frozen prompts, 90 raw transcripts, run manifests, the researcher’s primary scores, blinded AI review workbooks, coding documentation, completeness audits, and file-integrity checks.

**ИИ:** ? · обе модели · неясен конструкт · Claude scored 90 chatbot transcripts with the researcher's codebook, giving LLM–human agreement; unclear if sycophancy/emotional validation in workplace advice counts as psychological.

**Решение:** =

---

### 760 · R4718

**Tone Is Not Judgment: An Empirical Case Study on Emotional Sycophancy in Child-Facing Commercial LLMs**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.21481920

Sycophancy—the tendency of language models to favor responses aligned with a user’s stated beliefs over responses that maintain truthfulness or corrective independence—is a documented behavior in large language models. Much prior work has focused on factual sycophancy. This paper examines a related but distinct question: when a child-like user expresses an emotional statement that also contains a factual, causal, or self-evaluative interpretation, does the model distinguish the emotional experience from the interpretation embedded within it? Version 0.2, released in August 2026, reported exploratory case studies from consumer-LLM interactions conducted in July and August 2026: five conversations with Gemini across four affective scenarios and one factual control, together with an exploratory ChatGPT comparison using closely related scenarios. Those cases motivated a proposed evaluation target—examined affect—asking whether a model can acknowledge a child’s emotional experience while separately examining the causal, evaluative, or self-concept interpretation embedded within it. Version 0.4, released in September 2026, extends that work through a structured observational protocol. It includes four frozen scenario families (math/teacher intent, peer conflict/toys, sibling hostility, and appearance/social comparison), three model providers (Claude Sonnet 4.6, GPT-5.6 Sol, and Gemini Flash-Lite), four age conditions (unspecified, 10, 13, and 16), and a nine-dimension ordinal coding scheme. The primary analytic set comprises 48 conversations and 384 submitted user turns collected through Anthropic Workbench, OpenAI API Playground, and Google AI Studio, with no added system prompts. An initial machine-coded pass was generated in a GPT-based session. The final reported trajectory scores were assigned by the researcher using the targeted-turn review procedure disclosed in the manuscript. Claude Sonnet 4.6 assisted with selected-turn extraction, but this assistance is not treated as independent inter-rater review. No second independent human reviewer was used. The pattern identified in version 0.2 was observed again in the structured extension: tone adapted more reliably than judgment. Emotional validation was uniformly high in these trajectories, while interpretation validation, active contestation, evidence examination, and stability under pressure varied descriptively by provider and scenario. Explicit age declarations changed response register more consistently than underlying judgment. Because the study contains one run per provider, scenario, and age cell, its results are observational and do not estimate sampling variability. The extension also identifies qualitative failure modes beyond direct interpretation endorsement. In Claude’s age-10 and age-13 appearance trajectories, repeated urgent referral to parents, trusted adults, or counselors occurred without stated self-harm content, producing disproportionate safety-oriented escalation. In Gemini trajectories, some responses characterized third-party behavior as sneaky, malicious, cruel, or bullying beyond what the available evidence established. These patterns are not fully represented by the interpretation-validation dimension and motivate separate evaluation axes for escalation calibration and third-party characterization. The paper proposes examined affect as an evaluation target for child-facing and child-accessible LLM safety research: the capacity to remain emotionally supportive while also remaining epistemically careful and proportionate. The accompanying data supplement contains all 48 readable transcripts, recovered raw provider records, final run manifests, the 384-turn prompt-fidelity audit, frozen protocols, the coding codebook, completed and unblinded human-scoring files, score summaries, row-level human notes, the recalculation report, corrected qualitative flags, validation documentation, citation metadata, licensing information, and integrity checksums. The reported model names are the labels displayed in Anthropic Workbench, OpenAI API Playground, and Google AI Studio at the time of collection. They are treated as experimental metadata and do not guarantee the identity of the underlying routed models.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Chatbot responses were coded on an emotional-validation scheme: GPT did a first pass and the researcher assigned final scores. Abstract doesn't say if their agreement is reported.

**Решение:** =

---

### 761 · R4743

**transformer_1376 at PsyDefDetect: A QLoRA-Based Generative Framework for Context-Aware Psychological Defense Mechanism Detection**

2026 · conference-paper · https://doi.org/10.18653/v1/2026.bionlp-2.15

Psychological defense mechanisms play a crucial role in shaping human responses during emotionally charged conversations, yet remain underexplored in natural language processing.In this work, we address the PSYDEFCONV shared task, which involves classifying defense mechanisms in multi-turn dialogues using clinically grounded annotations based on the Defense Mechanism Rating Scales (DMRS).We propose a generative supervised fine-tuning framework that reformulates the task as conditional text generation.A pre-trained causal language model (Gemma-2-2B) is adapted using parameter-efficient fine-tuning (PEFT) with 4-bit quantization, enabling efficient training under limited computational resources.To handle class imbalance, we apply random oversampling, and we design a prompt-based input representation to incorporate conversational context effectively.Experimental results demonstrate that our generative approach is competitive with discriminative baselines while offering improved flexibility in modeling subtle and context-dependent defensive behaviors.The findings highlight the potential of generative large language models for psychologically grounded dialogue understanding tasks.

**ИИ:** + · обе модели · бенчмарк с метками людей · Fine-tuned Gemma-2-2B classifies defense mechanisms in dialogues against clinically grounded human DMRS annotations (shared task).

**Решение:** =

---

### 762 · R4746

**LLM-Based Multi-class Depression Severity Prediction Using Social Media Data**

2026 · Lecture notes in networks and systems · conference-paper · en · https://doi.org/10.1007/978-3-032-27154-9_28

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM depression severity from social media posts could use human-annotated severity labels.

**Решение:** =

---

### 763 · R4755

**Exploring socioeconomic associations of crisis information processing via large language models and explainable AI**

2026 · Information Processing & Management · article · en · https://doi.org/10.1016/j.ipm.2026.105195

Social media evolution has restructured corporate crisis communication, yet extracting regional intelligence from unstructured data remains a significant computational challenge. This study proposes an integrated AI-Spatial Information Framework to analyze provincial-level discourse patterns during a major corporate crisis. Using the DeepSeek R1 671B model with few-shot learning, we classified 225,515 social media comments from Douyin into five theory-driven categories and an “Other” category, achieving an overall accuracy of 85.67% against stratified human reference labels (Cohen’s kappa = 0.828). We then employed LASSO-based feature selection and FDR-corrected OLS regression to examine associations between provincial-level socioeconomic indicators and consumer discourse patterns across 31 Chinese provinces. Statistical results suggest that provincial socioeconomic factors account for a substantial portion of the observed variation in digital discourse. Life expectancy was positively associated with brand anthropomorphism, while tertiary education showed a tentative negative association with health risk perception. More importantly, these associations suggest that regional variation in brand-supportive discourse is closely related to socioeconomic conditions and is theoretically consistent with cognitive buffering processes. By integrating theory-driven LLM classification with spatial analysis, the proposed framework connects computational linguistics and spatial social computing, providing a replicable approach for examining regional heterogeneity in digital crisis discourse.

**ИИ:** ? · обе модели · неясен конструкт · DeepSeek coded social media comments against human labels (κ=0.828); categories like risk perception may be psychological but context is corporate/marketing.

**Решение:** =

---

### 764 · R4757

**Smart Strategies in Mental Health**

2026 · Auerbach Publications eBooks · book-chapter · en · https://doi.org/10.1201/9781003587842-7

Various mental health tasks, such as emotion understanding, stress and depression detection, and engagement assessment, employ datasets with varying modalities and computational models. This non-uniformity in data and models makes it challenging to analyze multiple mental health phenomena simultaneously. This chapter examines these issues and demonstrates how generative artificial intelligence (AI) can be leveraged to develop smart strategies that overcome these limitations. We focus on three tasks using the Interactive Emotional Dyadic Motion Capture (IEMOCAP) dataset to illustrate how generative AI can address data scarcity in emotional well-being analysis. First, we integrate generative models with human expertise for data annotation. Then we illustrate the three tasks to (1) apply domain adaptation to adapt audio/visual emotion challenge (AVEC) to IEMOCAP for depression detection, (2) use multi-label learning to predict dimensional emotion states alongside discrete ones, and (3) apply incremental learning so the model can predict additional psychological states beyond those it was originally trained on. With emotion classification accuracies of 62.83%, 64.54%, and 60.28%, respectively, our results are comparable to the state-of-the-art using human-annotated datasets, highlighting the efficacy of generative AI in advancing smart mental health diagnostics.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Generative AI annotates IEMOCAP emotions alongside human expertise; unclear whether the LLM labels are compared directly with the human emotion labels.

**Решение:** =

---

### 765 · R4763

**Cognivia: A Cognitive Behavioral Therapy Copilot for Evidence-Based Mental Healthcare**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.25681

Cognitive distortion amplifies negative emotions and contributes to mental health disorders. Cognitive Behavioral Therapy (CBT) is an effective way to address cognitive distortions, but its large-scale application is limited by the shortage of professional therapists. Although large language models (LLMs) have recently been explored for mental health applications, existing methods still suffer from limited domain specificity, overly flattering responses, and the absence of well-defined annotations for cognitive distortions. This paper proposes Cognivia, an evidence-based artificial intelligence therapist that integrates automatic cognitive distortion identification and rational response generation. Our framework is built on authoritative CBT texts widely regarded as core paradigms and standard references. It is further augmented with mental health question-answer (Q and A) data, and employs multi-stage prompting and structured generation strategies under the supervision of behavioral science experts. Then we fine-tune a lightweight LLM on this augmented CBT dataset to obtain Cognivia. In addition, we propose the first hierarchical quality evaluation framework for assessing LLM-generated rational responses, developed through collaboration between AI researchers and behavioral science experts. Cognivia is evaluated using lexical metrics, LLM-based Judges with two complementary criteria, and human evaluation by 10 behavioral science experts. It consistently outperforms the baseline methods in cognitive distortion recognition and rational response generation, demonstrating its effectiveness. Our code is available at https://github.com/SNOWTEAM2023/Cognivia.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · The fine-tuned LLM identifies cognitive distortions, and both LLM judges and 10 experts evaluate responses. It is unclear whether the labels come from human annotators or whether LLM–human agreement is reported.

**Решение:** =

---

### 766 · R4791

**Performance Evaluation of Large Language Models in Bias Recognition for Educational QA**

2026 · International Conference on Emerging Technological Trends · conference · https://doi.org/10.1109/icett70124.2026.11666071

In the Educational Question Answering (QA) scenario of Intelligent Tutoring Systems (ITS), biased expressions in students’ answers can hinder cognitive development and influence social perceptions. While Large Language Models (LLMs) show promise for automated bias detection, their performance in educational contexts lacks systematic evaluation. To address this gap, we evaluate the bias recognition performance of LLMs in Educational QA. Specifically, we focus on six common types of bias in education: gender bias, regional bias, socioeconomic status bias, physical characteristics bias, disability and physical illness bias, and mental health stigma bias, and then create dedicated evaluation datasets from real educational interactions. Based on datasets, we evaluate six representative LLMs spanning open-source and closed-source models from diverse architectures. Our findings reveal that (1) open-source and closed-source LLMs show no significant difference in overall bias recognition accuracy rate, but there is a large degree of performance variability among two types of LLMs; (2) recognition accuracy rates differ significantly among the six biases; (3) the accuracy rate of LLMs in recognizing multi-bias is significantly lower than in single-bias recognition; (4) LLMs predictions substantially align with human judgments. These results deepen understanding of LLMs capabilities and limitations in educational bias recognition and provide a benchmark for deploying automated bias detection in ITS, contributing to more equitable educational technologies.

**ИИ:** ? · обе модели · неясен конструкт · LLMs detect bias (including mental-health stigma) in student answers and are compared with human judgments; unclear whether bias is a psychological construct here.

**Решение:** =

---

### 767 · R4794

**LLMs for automatic annotation of Mandarin narrative transcripts**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.17205

Linguistic annotation of transcribed speech is essential for research in language acquisition, language disorders, and sociolinguistics, yet remains labor-intensive and time-consuming. While Large Language Models (LLMs) have shown promise in automating annotation tasks, their ability to handle complex discourse-level annotation in non-English languages remains understudied. This study evaluates whether LLMs can reliably annotate narrative macrostructure-the hierarchical organization of story grammar elements-in spoken Mandarin, using the Multilingual Assessment Instrument for Narratives (MAIN) as a testbed. We compared four LLMs against trained human annotators on narratives produced by children, young adults, and older adults. The best-performing model achieved agreement with human raters (k=.794) approaching human-human reliability levels (k=.872) while reducing annotation time by 65%, whereas the locally deployable lightweight model performed substantially worse. Annotation difficulty varied systematically by macrostructure element type, with categories requiring subtle semantic differentiation posing persistent challenges. Furthermore, model reliability decreased on young adult narratives, which exhibited greater lexical variation, semantic ambiguity, and multi-element integration within single utterances. These findings suggest that LLMs can effectively support discourse-level annotation in non-English spoken corpora, while highlighting the continued need for human oversight in semantically complex tasks. Our prompt templates are open sourced for future use. 28 pages, 9 tables

**ИИ:** ? · обе модели · неясен конструкт · LLMs vs trained human annotators (kappa) scoring MAIN narrative macrostructure; unclear if a linguistic narrative assessment counts as a psychological construct.

**Решение:** =

---

### 768 · R4799

**StoryMI: Steerable Multi-Agent Therapeutic Dialogue Generation**

2026 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48550/arxiv.2605.27393

Large language models (LLMs) can generate fluent dialogue, but prior works lack situational grounding, dynamic strategy control, and evaluation aligned with clinical standards in motivational interviewing (MI). We introduce StoryMI, a multi-LLM agent framework for controllable MI dialogue generation, where questionnaire-based client profiles are expanded into situational stories that provide narrative context for the dialogue. Therapist and client agents generate MI-coded utterances guided by MI codes selected by the interaction agent, while an interaction agent dynamically coordinates exchanges to control MI strategies during a multi-turn conversation. We propose a two-level evaluation protocol: lexical metrics and MI-specific measures of macro-level counseling strategies, alongside LLM-as-judge and human expert assessments. We construct a dataset of 6K simulated MI dialogues grounded in 1K questionnaire-story pairs, covering 12 MI codes and 13 symptom domains, and benchmark six open- and closed-source LLMs. Our results show that situational grounding and macro-level control can improve MI adherence and clinical plausibility, demonstrating the effectiveness of a structured multi-agent workflow for psychotherapy dialogue generation. We provide code and data for reproducibility. ACL2026

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mainly MI dialogue generation, but it uses LLM-as-judge alongside human expert assessments of MI adherence; agreement between them may be reported.

**Решение:** =

---

### 769 · R4812

**Developing Virtual Personas from User-Level Social Media Data: Stability and Human Alignment of LLM-Generated Symptom Profiles**

2026 · Preprints.org · preprint, ppr, posted-content · https://doi.org/10.20944/preprints202607.1828.v1

Large language models (LLMs) may support realistic virtual patients, yet most existing systems rely on top-down construction approaches, such as manually curated vignettes. We investigated a bottom-up alternative in which social media histories were transformed into virtual personas examining stability and alignment with human judgment. Histories from Italian Reddit users reporting depressive or anxiety-related distress were manually anonymized and synthesized into two prompt variants (Base and Clinically Enriched). GPT-4o and DeepSeek-V4-Pro completed the PHQ-9 and GAD-7 in independent generations per persona, prompt, model, and scale. Stability was assessed using single-generation and aggregated intraclass correlations. Human alignment with symptom ratings from a psychologist was examined using persona-level correlations and item-level area under the curve (AUC). PHQ-9 total scores showed high single-generation stability across conditions (ICC(2,1) = .84–.88), whereas GAD-7 stability varied by model. Aggregating generations yielded high reliability in all conditions, although item-level stability was heterogeneous. Human alignment was stronger for PHQ-9 than GAD-7 and was highest for DeepSeek-V4-Pro with the Base prompt (r = .98). DeepSeek-V4-Pro also showed higher item-level discrimination, while clinical enrichment had scale-dependent effects. Our findings support the feasibility of bottom-up persona construction, while highlighting the need for psychometric evaluation across models and symptom domains.

**ИИ:** разошлись — Opus + (клиническая оценка: LLM personas built from Reddit histories rate PHQ-9/GAD-7 items; compared with a psychologist's symptom ratings of the same users (correlations, AUC).); Sonnet ? (неясен конструкт: LLM personas from Reddit histories fill PHQ-9/GAD-7 and are compared with a psychologist's symptom ratings; it is patient simulation, but it resembles LLM symptom rating against a clinician.)

**Решение:** +

---

### 770 · R4821

**Multimodal Emotion Recognition and Contextual Analysis in Therapy Sessions Using Video Large Language Models**

2026 · Communications in computer and information science · journalarticle, conference-paper · en · https://doi.org/10.1007/978-3-032-12767-9_13

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests video LLMs recognising emotions in therapy sessions, which could be compared with human annotations.

**Решение:** =

---

### 771 · R4828

**Understanding Social Workers' Well-being through Sentiment Analysis**

2026 · Zenodo (CERN European Organization for Nuclear Research) · text/poster, article · https://doi.org/10.5281/zenodo.22795449

This paper investigates the use of Natural Language Processing (NLP) techniques to analyze open-ended survey responses from Italian social workers, with the aim of better understanding their perceived work-related well-being. We introduce a manually annotated dataset of 546 comments, labeled according to a domain-specific sentiment scheme, supported by detailed annotation guidelines and Inter-Annotator Agreement analysis. We compare the performance of fine-tuned BERT-based models with instruction-based GPT models. While the comparison is not strictly equivalent, as GPT models also leverage task-specific instructions and annotation guidelines, the results indicate that instruction-based approaches can effectively support domain-specific sentiment annotation. The best-performing approach is then applied to a larger corpus of 3,886 comments, allowing for a large-scale analysis. Finally, we complement sentiment classification with multi-label thematic analysis and examine the relationship between sentiment, demographic variables, and organizational well-being indicators. Our results highlight the potential of combining NLP methods and survey data to gain deeper insights into workplace well-being in socially relevant domains.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT models annotate social workers' open-ended responses on work-related well-being sentiment; compared against a manually annotated dataset.

**Решение:** =

---

### 772 · R4853

**Beyond Right and Wrong: Evaluating Second-order Social Reasoning in Large Language Models**

2026 · PsyArXiv · preprint/article, preprint, ppr · https://doi.org/10.31234/osf.io/mrey3_v1

Previous AI alignment efforts have focused primarily on first-order social norms -- teaching models what is socially acceptable or unacceptable (e.g., "do not steal"). However, social intelligence depends not only on norm recognition, but also on anticipating who will enforce it and how (e.g., public shame or even imprisonment). These second-order expectations, known as metanorms, govern how people respond when social rules are broken. We introduce a novel framework for evaluating metanorm reasoning in Large Language Models (LLMs) along two dimensions: emotional appraisal and behavioral response, and propose new classification tasks, namely, predicting self-regulation in violators, and other-regulation in observers. We release a multi-perspective dataset, NormReact, of 450 norm violation scenarios, hand-annotated for emotions and behavioral responses across norm violators' gender and observers' social closeness. Current LLMs portray a harsher social world: across six models, they overpredict negative sanctions where humans would expect inaction, and alignment with human judgments deteriorates as social distance increases. These findings suggest that AI systems in norm-sensitive domains, from conflict mediation to policy simulation, may risk producing a distorted picture of social regulation: one that over-represents punishment and under-represents the tolerance, restraint, and relational calibration that characterize actual norm enforcement in the real world.

**ИИ:** ? · обе модели · неясен конструкт · Benchmark of norm-violation scenarios with human emotion/behaviour annotations compared to LLMs; it's unclear whether predicting reactions to vignettes counts as coding text.

**Решение:** =

---

### 773 · R4882

**Large Language Models in Qualitative Analysis: Comparing Traditional and Researcher-Interpreted Approaches**

2026 · International Journal of Qualitative Methods · journalarticle, article, text · en · https://doi.org/10.1177/16094069261426100

Qualitative data analysis, particularly thematic analysis, is a widely used method for uncovering patterns and insights in narrative data but often faces challenges such as being resource-intensive and susceptible to researcher bias. In recent years, Large Language Models (LLMs) have emerged as promising tools to assist human coders in conducting thematic analysis, offering efficiency and scalability in processing large datasets. However, existing work primarily relies on tools like ChatGPT, raising privacy concerns—especially when analyzing sensitive healthcare data—and lacks systematic validation through comparisons with human coders. This study aims to evaluate the potential of open-source LLMs for qualitative data analysis. Semi-structured patient interviews (n = 34) conducted by a trained qualitative researcher provided the dataset, with traditional qualitative (inductive) analysis by two researchers serving as the gold standard. Two open-source LLMs, Gemma2 and Llama3.1, were used to generate codes, and their performance was assessed based on factors such as chunk size, inductive vs. deductive methods, and prompting approaches. Results showed some alignment between LLM- and researcher-generated codes, with the deductive approach yielding higher and more nuanced insights (Gemma2: n = 723; Llama3.1: n = 1,042) compared to the inductive approach (Gemma2: n = 715; Llama3.1: n = 829). Approximately 45% of the LLM-generated codes provided meaningful context, though 22–39% were duplicative. While LLMs demonstrated efficiency in analyzing large volumes of textual data, nearly half of the codes lacked sufficient context or were repetitive. Our findings showed that although combining traditional qualitative analysis with AI presents a promising avenue, future research should explore how pre-trained LLMs could augment qualitative analysis with higher inter-rater reliability to improve patient-provider communication. There is a need for further research or the development of domain-specific LLMs to improve their utility in qualitative analysis.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Open-source LLMs coded patient interviews, including deductively, against researchers' gold standard; unclear if same units were compared or the construct is psychological.

**Решение:** =

---

### 774 · R4883

**Automating multi-label crisis detection in psychological support hotlines with pre-trained models.**

2026 · PLOS digital health · journal article, journalarticle, article · eng · https://doi.org/10.1371/journal.pdig.0001383

Psychological support hotlines provide immediate help to individuals in crisis, with operators assessing emotional states and suicide risk. However, increasing demand has led to a shortage of trained professionals, emphasizing the need for AI-driven crisis detection models. This study included 1,057 calls from the Hangzhou Hotline (2022-2023) to evaluate the effectiveness of deep learning and pre-trained models in detecting psychological crises using audio (Wave2Vec, Whisper) and transcribed text (RoBERTa, GPT). We adopted two strategies: deep learning classification with pre-trained models and Large Language Models (LLMs)-based prediction via prompt engineering (GPT-4 and DeepSeek series). The deep learning framework, employing GPT embeddings excelled in multi-label predictions compared to auditory model, achieving 80.48% [80.18%, 80.78%] F1 scores for identifying high-risk calls in prospective tests. Fusion experiments revealed that acoustic features offered negligible predictive value compared with text semantics. Notably, GPT-4o and DeepSeek-R1, utilizing few-shot learning, demonstrated performance comparable to the GPT-embedding deep learning model across multiple tasks. This suggests that their advanced Chain-of-Thought reasoning effectively mitigates data dependency gap, enabling LLMs to align with clinical domains using a few examples. Expert evaluation confirmed the clinical applicability of GPT-generated explanations. Taken together, these findings highlight the potential of LLMs in mental health crisis detection and lay the foundation for future research.

**ИИ:** разошлись — Opus + (клиническая оценка: GPT-4o/DeepSeek prompted to detect crisis/suicide risk labels in hotline transcripts; reference labels likely operator/clinician assessments.); Sonnet ? (неясно, кто ставил эталонные метки: GPT-4/DeepSeek classify crisis risk in hotline call transcripts; unclear whether reference labels come from human annotators/operators or other sources.)

**Решение:** +

---

### 775 · R4892

**Exploring Emotion Timeline Patterns in Social Media for Automatic Identification of Depression and Anxiety**

2026 · Lancaster EPrints (Lancaster University) · text/text, dissertation · en · https://doi.org/10.17635/lancaster/thesis/3121

Over the past years, public awareness of mental health issues has increased, and people are paying more attention to their mental well-being. Depressive and anxiety disorders are among the key causes of the global disease burden. These two mental conditions can disrupt the daily lives of people affected by them and, in severe cases, depression may even lead to suicide. To prevent suicide and alleviate the burden on the affected individuals, researchers have increasingly focused on automatically detecting these mental conditions using social media data, as people with mental health issues often seek supports and share their feelings on social media. Since depression and anxiety are chronic issues and related to emotions, past studies have utilised emotion information to identify social media users with depression and anxiety. However, these emotion features used in the past studies are often static, lacking the temporal fluctuation patterns that can effectively reflect the characteristics of these mental conditions. To address this issue, I propose a novel method that applies the timeline Shapelet classification method, a time series analysis method, to the automatic detection of depression and anxiety based on emotion intensity timeline patterns. This study involves two languages. I first created a new Thai dataset for depression and anxiety detection. Next, I selected and modified an existing English dataset for depression detection. Both datasets contain users' tweeting histories in X. Tweets in the Thai dataset were labelled with 26 emotion intensities by both human annotators and a Large Language Model (LLM). In contrast, tweets in the English dataset were automatically labelled with intensities of four emotions using an LLM. Based on the manually annotated Thai dataset, depression and anxiety are found to be associated with 14 and 10 emotions respectively. My study demonstrates that Shapelet classifiers can identify emotion intensity timeline patterns associated with depression and anxiety. Using these patterns, the classifiers detected depression with a precision of 0.7292 on the English dataset, and achieved maximum precision of 1.00 in detecting both depression and anxiety on the Thai dataset. These classifiers also outperformed benchmark models on the Thai dataset in detecting the two conditions, although they produced relatively low recall on both datasets. Finally, this study also investigates the potential of porting emotion intensity timeline patterns for cross-lingual depression detection, from English to Thai in this case. In my experiment, the Shapelet classifiers trained on English dataset could effectively detect depression in the Thai dataset, showing the potential of this approach for cross-lingual application, particularly for under-resourced languages.

**ИИ:** разошлись — Opus + (проверка кодирования внутри исследования: Thai tweets labelled for 26 emotion intensities by both human annotators and an LLM; LLM–human agreement likely reported.); Sonnet ? (неясно, сравнивали ли с людьми: Thai tweets were labelled for emotion intensity by both humans and an LLM, but the abstract doesn't say whether LLM–human agreement is reported.)

**Решение:** +

---

### 776 · R4907

**Students’ engagement with generative AI in academic learning: A self-determination theory and epistemic network analysis study**

2026 · Computers and Education Artificial Intelligence · article · en · https://doi.org/10.1016/j.caeai.2026.100606

This qualitative case study examines undergraduate students’ engagement with generative artificial intelligence (GenAI) in academic learning in an English-medium university setting. This study employs self-determination theory (SDT) as the primary interpretive framework, treating technology acceptance perceptions (e.g., usefulness and ease of use) as descriptive cues rather than explanatory constructs. Data from 23 semi-structured interviews were analyzed using reflexive thematic analysis, complemented by epistemic network analysis (ENA) to examine the structural relationships among themes in students’ discourse, with automated coding validated against a manually coded subset. Students frequently described GenAI as supporting efficiency and conceptual understanding; however, their accounts revealed persistent tensions concerning creativity, trust, and academic integrity. The ENA results showed that these concerns were systematically interconnected: discussions of learning support consistently co-occurred with verification practices, reflecting a “trust-but-verify” repertoire through which students calibrated their reliance on AI while maintaining epistemic control. Beyond instrumental evaluations, students’ narratives highlighted broader value- and norm-related considerations, including algorithmic bias, environmental sustainability, and the positioning of AI within human–teacher learning networks. Overall, the findings suggest that students’ engagement with GenAI is best understood as a motivated and socially situated learning practice shaped by the negotiation of competence, autonomy, and relatedness. Pedagogically, the results support a shift from prohibition-oriented responses to transparent institutional guidance, autonomy-supportive scaffolding of verification practices and AI literacy, and process-oriented assessment designs that make students’ reasoning visible. Learning analytics approaches, such as ENA, may further assist educators in examining how these practices become integrated into students’ learning processes.

**ИИ:** ? · обе модели · другое · Interview coding with SDT constructs was automated and checked against a manually coded subset, but it is unclear whether an LLM did the coding (it could be nCoder or regex).

**Решение:** =

---

### 777 · R4910

**From Sentiment to Valence in Metaphor: a Comparison of BERT-based Sentiment and Prompted Large Language Models**

2026 · Language Resources and Evaluation Conference (LREC) · conference, conference-paper · https://doi.org/10.63317/42tupej9pkt5

Although the affective dimension is a key aspect of metaphor, computational studies of figurative language have largely overlooked psycholinguistic variables such as valence. This study investigates whether computational models can reliably estimate the affective aspects of Italian and German metaphors and whether metaphor valence is compositionally derived. Outputs of BERT-based sentiment analysis and a valence-prompted LLM were compared with human ratings. Results show that the former exhibit limited alignment with human judgments, whereas higher agreement is achieved when the explicit concept of valence is prompted in a LLM. Both humans and models rely on the combined valence of the individual lemmas, suggesting a compositional contribution to metaphor valence.

**ИИ:** ? · обе модели · неясен конструкт · A prompted LLM's valence ratings of metaphors were compared with human ratings, but these are psycholinguistic stimulus norms, not psychological or clinical text.

**Решение:** =

---

### 778 · R4937

**Benchmarking Large Language Models for Sentiment Analysis in Pregnancy-Related Weight Discussions on Reddit: A Human Performance-Aligned Evaluation (Preprint)**

2026 · JMIR Formative Research · article · en · https://doi.org/10.2196/92821

BACKGROUND Pregnancy-related weight gain is both physiologically complex and socially charged, resulting in online discourse where clinical facts often blend with implicit emotional distress. While automated sentiment analysis could support maternal health surveillance, model performance in this emotionally complex context remains inadequately characterized relative to expert human judgment. OBJECTIVE To benchmark contemporary sentiment classification models on pregnancy-related weight discussions, with emphasis on agreement with expert consensus, robustness under interpretive ambiguity, and practical deployment feasibility. METHODS We curated 15,619 Reddit posts and comments using an LLM-guided keyword expansion strategy. A "Gold Standard" was established through expert adjudication of 200 posts. We evaluated 10 models (3 commercial and 5 open-source LLMs, 2 MLMs) across zero-shot and few-shot configurations. Performance was measured using weighted F1-score and Cohen’s κ relative to adjudicated and pre-adjudication human baselines. Validated models were applied to 15,019 unlabeled comments to assess scalability and inter-model agreement. RESULTS Expert annotators achieved moderate pre-adjudication agreement (κ = 0.34), while expert–gold standard agreement establishes an empirical performance ceiling. The top-performing model (Gemini-3-Flash) achieved F1 = 0.66 and κ = 0.48, exceeding pre-adjudication inter-annotator agreement by 0.14. Moderate-parameter open-source models (e.g., GPT-OSS: F1 = 0.65, κ = 0.44) achieved comparable performance. Classification errors concentrated at the Neutral–Negative boundary. Inter-model agreement on unlabeled posts was high (κ = 0.80) but dropped sharply for comments (κ = 0.10) in a stratified sample, indicating a significant discourse-type dependency. CONCLUSIONS Sentiment classification in pregnancy weight gain is fundamentally constrained by human interpretive disagreement. Open-source LLMs can substitute for commercial systems on narrative-style discourse, but performance remains bounded by task-intrinsic ambiguity. Model selection should prioritize human-relative agreement and discourse-type alignment over marginal performance gains.

**ИИ:** ? · обе модели · неясен конструкт · LLMs vs expert gold-standard sentiment labels (κ) on Reddit pregnancy-weight posts; sentiment framed as emotional distress, borderline psychological construct.

**Решение:** =

---

### 779 · R4941

**Self-Reported Health Outcomes in Metabolic Health YouTube Comments: Cross-Sectional Study and Rule-Based Natural Language Processing Framework Development and Validation.**

2026 · Journal of medical Internet research · journal article, validation study, observational study · eng · https://doi.org/10.2196/94855

BACKGROUND YouTube is increasingly used for healthcasting, the sharing of evidence-based dietary and lifestyle interventions by domain experts. In the metabolic health domain, channels focused on therapeutic carbohydrate restriction have accumulated audiences of millions. A distinctive feature is the comment section, where viewers share first-person accounts of health changes, constituting a unique source of real-world outcome data at scale. However, extracting structured health information from unstructured comments presents computational challenges. OBJECTIVE This observational, cross-sectional study aims to develop and validate a precision-optimized computational framework for extracting self-reported health outcomes from healthcasting YouTube comments and to characterize the prevalence, distribution across health aspects, and channel-level variation of reported outcomes across a large-scale metabolic health corpus. METHODS This study analyzed 43,111 unique YouTube comments from 110 videos across 11 therapeutic carbohydrate restriction-focused healthcasting channels (37,458 unique authors; data span November 2013 to January 2026; collected via YouTube data application programming interface version 3). The methodology comprised 3 construction phases and 5 validation studies. The construction phases were (1) exploratory corpus characterization, (2) iterative development of a 35-aspect hierarchical health outcome ontology, and (3) precision-optimized rule-based classification, validated through precision validation (stratified sample of n=500), recall estimation (n=510), external validation on 5 held-out channels (n=12,653 comments), large language model–assisted interrater reliability assessment, and transformer baseline comparison against Bidirectional Encoder Representations from Transformers (BERT) and Robustly Optimized BERT Pretraining Approach (ROBERTa) classifiers. A supplementary aspect–based sentiment analysis contextualized the positive-only design. RESULTS The framework identified 1790 positive health outcome reports (1790/43,111, 4.15% prevalence), achieving 97.6% (488/500) precision (95% CI 95.7%-98.6%) and estimated 56.2% recall (95% CI 43.4%-67.9%). The reports described 6674 positive outcomes, distributed across 35 health aspects and 18 named disease conditions extending beyond weight loss: pain and inflammation reduction (1137/6674, 17%), type 2 diabetes improvement (977/6674, 14.6%), skin health (784/6674, 11.8%), and psychological well-being (731/6674, 11%). Over half (3355/6674, 50.3%) spanned multiple research objectives. Significant channel-level variation was observed (χ²10=927.5; P<.001), with positive outcome rates ranging from 1.32% to 10.40% (odds ratio 8.68, 95% CI 7.10-10.61). Transformer baselines achieved higher recall but lower precision, confirming their advantage for high-confidence corpus generation. A supplementary aspect-based sentiment analysis indicated a positive-to-negative ratio of approximately 4.6:1 (n=1003), with negative experiences (59/495, 11.9%) predominantly involving gastrointestinal and cardiovascular concerns. CONCLUSIONS This study presents, to our knowledge, the first validated, rule-based framework for extracting self-reported metabolic health outcomes from healthcasting YouTube comments at corpus scale. Unlike existing recall-oriented social media health classifiers, the precision-optimized design achieves the confidence threshold required for outcomes research without manual review. These findings demonstrate that expert-led health content comment sections constitute a scalable, complementary data source for monitoring real-world engagement with dietary interventions, with implications for public health surveillance, platform design, and health communication research.

**ИИ:** ? · обе модели · неясен конструкт · Classifier is mainly rule-based for metabolic health outcomes (well-being is one aspect); the LLM-assisted interrater check against human coding is unclear.

**Решение:** =

---

### 780 · R4953

**Convergence between AI chatbot-calculated microstructure measures and SALT analysis of child language samples**

2026 · Frontiers in Language Sciences · journalarticle, article · https://doi.org/10.3389/flang.2026.1929126

This study examined the association and agreement between microstructure calculations from four large language model (LLM) chatbots and those generated by Systematic Analysis of Language Transcripts (SALT) software. Eighty-four typically developing children (35 girls; ages 2–9) participated, with 30 Japanese-English bilinguals and 54 English monolinguals. Narrative language samples were collected and coded with SALT conventions. Transcripts were randomly ordered and analyzed using two prompts. Using a general prompt, transcripts were entered into each LLM chatbot (ChatGPT, Copilot, MagicSchool, and Gemini), microstructure outputs were recorded, then the process was repeated with the same order using the more specific prompt. Results showed that across LLM chatbots, measures requiring relatively simple word or morpheme counts (MLUw, MLUm, NTW, NDW) generally exhibited stronger associations with SALT than the subordination index (SI), which showed greater variability. While intraclass correlation coefficients within measures were more variable, association and agreement coefficients were generally consistent with each other. Children's age and language backgrounds were associated with differences in the magnitude of some LLM–SALT coefficients. Finally, prompt specificity did not strengthen microstructure calculations for any of the LLM chatbots. Findings provide preliminary methodological evidence that some SALT-calculated microstructure measures may be more amenable to LLM chatbot-assisted calculation than others, with substantial associations and generally strong agreement observed for several measures; however, due to the exploratory nature of the current study, their clinical utility, decision-level accuracy, and workflow implications require further investigation.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs calculate child narrative microstructure measures compared with SALT on human-coded transcripts; unclear whether language-sample metrics count as a psychological construct or human coding.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM chatbots compute linguistic counts (MLU, NTW, subordination index) compared with SALT software output, not human coding of a psychological construct.)

**Решение:** -

---

### 781 · R4967

**Can Model Confidence Triage Qualitative Coding? Decision Models, LLMs, and What a 5% Error Guarantee Actually Costs**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.23413906

Language models can apply qualitative codebooks, but their labels save effort only if a researcher knows which ones to trust. We ask whether model confidence can tell, comparing seven decision models (APIs that return probabilities for typed questions) with twelve LLM confidence signals on five human-coded tasks spanning Reddit comments, counselling dialogue and classroom talk, under a prospectively specified analysis plan. Three findings stand out. First, low calibration error does not make confidence useful: decision models differ widely in how well they rank their own mistakes, and calibration can be improved without improving ranking. Second, error targets are hard to keep. A threshold tuned to 5% error on hand-coded comments exceeds 5% on new comments in about half of re-splits, and applying an independence-based guarantee to clustered decisions breaks it, because a comment’s codes and a transcript’s utterances err together. A guarantee that respects how the hand-coded sample was drawn holds, at a price: after 30% of Reddit comments are hand-coded, it certifies 60–83% of the remainingcode decisions for most coders. On dialogue, with whole transcripts hand-coded, it certifies nothing and could not even for a perfect coder at our calibration sizes; sampling single utterances instead still yields almost no certificates. Third, accepted shares overstate the work saved: nearly all certified decisions say a code does not apply, and a baseline that reads no text accepts 75% of comment decisions at 3.6% error. Model uncertainty also rises where annotators disagree, and option order changes some models’ labels. Confidence can triage coding, but only if researchers check ranking, sampling design and what the accepted labels are. Models were called on 10–12 October 2026; we release the harness and every coding decision.

**ИИ:** + · обе модели · кодирование по кодбуку · LLMs apply qualitative codebooks to human-coded Reddit comments and counselling dialogue, with error rates measured against the human labels; constructs need checking.

**Решение:** =

---

### 782 · R4970

**Prompt-based justification and scoring with large language models for thought and language disorder assessment**

2026 · Multimedia Tools and Applications · journalarticle, article, journal-article · en · https://doi.org/10.1007/s11042-026-21401-8

The assessment of disorganized thought and language is essential for diagnosing schizophrenia (SZ), still remaining a subjective and labor-intensive clinical process. We present ClearThought, an automated framework that uses large language models (LLMs) to evaluate the Thought and Language Disorder (TALD) scale through few-shot prompting on transcribed psychiatric interviews. The model generates 0–4 item-level severity scores and structured justifications aligned with the TALD rubric. We evaluated ClearThought on a dataset of 33 SZ patient interviews, comparing model outputs to clinician ratings using both ordinal and binary performance metrics. For ordinal scoring, the system achieved macro F1\documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$\ge$$\end{document}0.80 on 11 items and very strong Spearman correlations (\documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$\varvec{\rho \ge 0.80}$$\end{document}) on 15 items, particularly for disorders that show clear and noticeable patterns in spoken language, such as Blocking and Restricted Thinking. Entropy-aware analysis revealed that high performance was most meaningful when accompanied by sufficient label variability. For binary detection, the model accurately identified disorder presence in 26 of 30 items (F1 > 0.80), with over 11 items exceeding F1 = 0.90. However, high scores on low-entropy items (e.g., Clanging, Neologisms) were often driven by consistent disorder absence, highlighting the need for caution when interpreting results from skewed label distributions. Clinicians rated the model’s justifications as clinically sound and interpretable, with average scores above 4.0/5.0 for scoring accuracy, clarity, and overall trust. These results suggest that LLMs, guided by prompt-based scoring and structured justification, can support objective, interpretable, and scalable TALD assessments. The framework performs best for linguistically relevant disorders and provides a transparent interface to assist clinical reasoning. Future work will target rare disorders, enhance justification, and extend validation across broader clinical cohorts.

**ИИ:** + · обе модели · клиническая оценка · LLM scored TALD items from psychiatric interview transcripts and was compared with clinician ratings using F1 and Spearman correlations.

**Решение:** =

---

### 783 · R4973

**Assessing the Capabilities of LLMs in Humor: A Multi-dimensional Analysis of Oogiri Generation and Evaluation**

2026 · Proceedings of the AAAI Conference on Artificial Intelligence · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.1609/aaai.v40i39.40567

Computational humor is a frontier for creating advanced and engaging natural language processing (NLP) applications, such as sophisticated dialogue systems. While previous studies have benchmarked the humor capabilities of Large Language Models (LLMs), they have often relied on single-dimensional evaluations, such as judging whether something is simply ``funny.'' This paper argues that a multifaceted understanding of humor is necessary and addresses this gap by systematically evaluating LLMs through the lens of Oogiri, a form of Japanese improvisational comedy games. To achieve this, we expanded upon existing Oogiri datasets with data from new sources and then augmented the collection with Oogiri responses generated by LLMs. We then manually annotated this expanded collection with 5-point absolute ratings across six dimensions: Novelty, Clarity, Relevance, Intelligence, Empathy, and Overall Funniness. Using this dataset, we assessed the capabilities of state-of-the-art LLMs on two core tasks: their ability to generate creative Oogiri responses and their ability to evaluate the funniness of responses using a six-dimensional evaluation. Our results show that while LLMs can generate responses at a level between low- and mid-tier human performance, they exhibit a notable lack of Empathy. This deficit in Empathy helps explain their failure to replicate human humor assessment. Correlation analyses of human and model evaluation data further reveal a fundamental divergence in evaluation criteria: LLMs prioritize Novelty, whereas humans prioritize Empathy. We release our annotated corpus to the community to pave the way for the development of more emotionally intelligent and sophisticated conversational agents.

**ИИ:** ? · обе модели · неясен конструкт · LLMs rate funniness of Oogiri responses on six dimensions and are compared with human ratings; unclear whether rating humor/creativity counts as a psychological construct.

**Решение:** =

---

### 784 · R4988

**Generation of depressive verbalizations in dialogues using text-diffusion in LLM prompting**

2026 · Zenodo (CERN European Organization for Nuclear Research) · dissertation/, dissertation · https://doi.org/10.5281/zenodo.18836823

Generation of depressive verbalizations in dialogues using text-diffusion in LLM prompting This repository contains the official implementation of the bachelor thesis: Generation of depressive verbalizations in dialogues using text-diffusion in LLM prompting The code used for this project is an adapted version of earlier work by Nöhler et al., which can be found here: "Text-Diffusion Red-Teaming of Large Language Models: Unveiling Harmful Behaviors with Proximity Constraints" (arXiv:2501.08246). This project uses a text-diffusion architecture first introduced in the context of red-teaming to create depressive verbalizations in prompted dialogue, resulting in realistic datasets of psychological markers Installation Clone the repository: git clone cd (Optional but recommended) Create and activate a virtual environment: python -m venv venv source venv/bin/activate # On Windows use `venv\Scripts\activate` Install the required dependencies: pip install -r requirements.txt Usage This project includes several core scripts: Diffusion_Model.py – Defines the architecture and functionality of the Text Diffusion model. red_team_diffusion.py – Contains the trainer logic for depressive verbalizations and red-teaming using the diffusion model. rtdConfig.py – Configuration settings for the experiments. train_diffusion_model.py – Training script for the diffusion model, with built-in logging. safety_audit.py – Uses the trained diffusion model to detect and categorize areas of vulnerability in target models. resource.py – Windows stub for the Unix only "Resource" module that vec2text imports. rewarding.py – clarifies the reward structure used (psychological interestingness) for model training, and refers to an LLM (GoogleAI) for judgement of interestingness. Furthermore, there are some files which are not part of the code, but still important for this project: my_short_prompts.csv - file with the prompts as a baseline to train the model, as well as basis of the reconstructed prompts reconstructed_prompts.csv - file with the reconstructed prompts; the endresult of this paper diffusion_psychinterest_short_long.pt - machine learning model responsible for the prompt-reconstruction process Manually generated prompts.pdf - Collection of (mostly) manually generated prompts of dialogue involving depression Conversation created by manual prompts.xlsx - Conversations created by the manually prompts through the use of Google AI Comparison of Conversations.xlsx - To discover the interrater agreement between an LLM and psychologist, randomly paired Conversations were judged on the question of which is more psychologically interesting, the results and process are in this file.

**ИИ:** ? · обе модели · неясен конструкт · Mainly a generation thesis, but it reports LLM–psychologist agreement on pairwise 'psychological interestingness' judgments of depressive dialogues; construct is vague.

**Решение:** =

---

### 785 · R4994

**AGC-Bench: Measuring Artificial General Creativity**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2607.01152

Creativity research has debated whether creativity is domain-specific (e.g., visual, writing, science), and if it is psychometrically separable from general intelligence. Both questions now apply to LLMs, but a unified benchmark of AI creativity remains elusive. We introduce AGC-Bench, an artificial general creativity benchmark built from a systematic review of the AI creativity literature (3,101 papers screened, 497 benchmarks identified), paired with an agentic harness that converts idiosyncratic codebases into HELM-standardized benchmarks. The first release covers 78 datasets spanning brainstorming, problem solving, STEM, narrative, figurative language, and humor. To address bias in LLM-as-judge, we apply Judge Response Theory -- a psychometric calibration of judge leniency/severity; we then fine-tune Qwen3-30B on the bias-corrected ratings of three frontier LLMs to produce AGC-Judge, an open-weight model that robustly scores new creativity benchmarks it was not trained on. Results reveal frontier models at the top of the AGC-Bench leaderboard, with open models close behind. LLMs show different creative strengths, ranking higher on some domains (e.g., writing) than others (e.g., scientific ideation). Extensive experiments yield three main findings. First, applying factor analysis across 83 LLMs, we recover a single creativity factor 'c', analogous to the 'g' factor of general intelligence, that explains 81.5% of variance, related to but separable from general knowledge/reasoning. Second, we show that prompting models to "be creative" boosts their performance far more than enabling reasoning, evidence that the benchmark tracks creativity over general ability. Third, on a human-matched subset, we find the top human still leads the top LLM on creativity. We release AGC-Bench with a public leaderboard, AGC-Judge, and human data as open infrastructure for measuring AI creativity at scale.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM judges score creativity (divergent thinking etc.); the abstract doesn't say whether judge ratings were checked against human ratings, though human data exists.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: AI creativity benchmark with LLM-as-judge calibration; evaluates LLM outputs, not psychological or clinical text coded against human labels.)

**Решение:** -

---

### 786 · R5036

**Enhancing Psychiatry Training Using an Agentic AI Simulated Consultation Tool: Prospective Cohort Study.**

2026 · JMIR medical education · journal article, journalarticle, article · eng · https://doi.org/10.2196/88580

Abstract Background Canadian psychiatry residents must demonstrate consultation competency, assessed using the standardized assessment of a clinical encounter report (STACER). However, opportunities to practice these skills and receive constructive assessment remain limited in clinical settings. Objective This study aimed to evaluate the technical feasibility of an agentic AI system designed to support psychiatry residents’ consultation competence through simulated patient encounters with a patient agent and structured feedback from a rater agent. Methods We conducted a two-phase technical feasibility prospective single-arm cohort study of the STACER Agentic System, a large language model–based platform integrating a patient agent and a rater agent. Phase 1 involved automated evaluation of the patient agent using a psychiatrist agent across 227 synthetic major depressive disorder cases. Performance was assessed using DeepEval metrics (correctness, clarity, medical faithfulness, turn relevance, and role adherence) with descriptive statistics and 95% CIs. Phase 2 involved a preliminary user study with 14 convenience-sampled participants: a total of 5 members of the clinical research team and 9 psychiatry residents from the University of Alberta. Participants completed simulated diagnostic interviews and case presentations. Performance was evaluated using STACER-based scoring by the rater agent and 2 psychiatrists. Interrater reliability was assessed using intraclass correlation coefficients (α=.05). Participants rated realism, behavioral consistency, psychiatric nuance, and feedback utility using Likert scales and free-text answers. Results The patient agent demonstrated high behavioral (51/56, 91.07%) and symptom fidelity (105/110, 95.45%), with strong automated performance (medical faithfulness mean 0.99, 95% CI 0.99‐1.00; turn relevance 0.99, 95% CI 0.986‐0.992). Participants rated simulations as psychiatrically plausible and diagnostically useful, particularly for depressive symptom representation, although rapport building was moderate (mean 2.78, SD 1.56 to mean 3.00, SD 1.41, out of 5.00) due to limited nonverbal cues. The rater agent generated structured STACER-aligned feedback with high intrarater consistency, especially at the section subtotal level. Interrater reliability with psychiatrists was poor at the item level (intraclass correlation coefficient range=0.25‐0.49) but improved to good-to-excellent agreement at the section level for psychiatry resident sessions (intraclass correlation coefficient range=0.89‐0.93). The rater agent’s scores fell between those of the 2 psychiatrists for the clinical research team and were lower than both human raters for psychiatry residents. Conclusions The STACER Agentic System demonstrates the technical feasibility of using agentic AI to simulate psychiatric consultations and deliver STACER-aligned formative feedback. By combining adaptive multiturn psychiatric simulation with competency-based evaluation, it shows promise in supporting cognitive aspects of consultation, though it remains limited in facilitating relational skills such as rapport building. These findings suggest agentic AI could expand scalable, low-risk opportunities for deliberate practice and formative feedback in competency-based psychiatric education. Further controlled studies are needed to evaluate educational effectiveness and integration into residency training.

**ИИ:** + · обе модели · LLM-судья · An LLM rater agent scored residents' simulated psychiatric interview transcripts on STACER; agreement with two psychiatrists was reported as ICC.

**Решение:** =

---

### 787 · R5038

**DAPWeb: Construct-Aligned Evaluation of MLLMs for Web-Based Child Mental Screening**

2026 · The Web Conference · journalarticle, book, conference · https://doi.org/10.1145/3774904.3792992

Child mental health screening faces growing challenges from rising psychological problems and limited professional access. Traditional self-report tools rely on verbal ability and self-awareness, limiting their validity in younger children. Projective drawing tests offer a nonverbal alternative, with the Draw-A-Person (DAP) test widely used to elicit psychological cues from drawings. While translating DAP test into Web-based screening, multimodal large language models (MLLMs) are emerging as a key enabling mechanism. However, their ability to deliver construct-level clarity and interpretive consistency for responsible deployment has not been systematically evaluated. To address this gap, we propose DAPWeb, a construct-aligned evaluation framework that assesses whether MLLMs can reliably support DAP-based child mental screening in Web environments. DAPWeb introduces a clinically grounded benchmark derived from real drawings and defines task-structured evaluation across six psychological constructs and three essential screening abilities: determination, detection, and comparison. The metrics emphasize construct validity and cross-drawing consistency, reflecting real-world early-screening workflows. Experiments across MLLMs reveal substantial gaps from human experts in most abilities. Yet, the comparable performance on determination suggests that DAP test can serve as a feasible component of Web-based early screening under structured interpretation. Thus, DAPWeb provides a replicable paradigm for responsible Web AI in child mental health.

**ИИ:** разошлись — Opus ? (другое: MLLMs interpret Draw-A-Person drawings against clinical expert benchmark; psychological construct, but input is images rather than text.); Sonnet -7 (другое — напишите почему: MLLMs interpret children's Draw-A-Person drawings (images), not written or transcribed text. The review covers text coding, so this is out of scope.)

**Решение:** -

---

### 788 · R5050

**Does Reasoning Improve Psychological Depth in Large Language Models? It Depends on Who's Judging**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.13773

LLM-as-a-Judge evaluators are increasingly used to score open-ended generation, yet a judge's correlation with human ratings on its development set may not guarantee valid measurement when outputs are closely matched and human preferences are subjective. We study this failure mode through psychological depth in short stories. Seven human readers and an LLM-judge ensemble selected on the original scalar Psychological Depth Scale dataset ($\rho = 0.646$) evaluated 60 blinded, prompt-matched story pairs from GPT-5 vs.\ GPT-4o and DeepSeek-R1 vs.\ DeepSeek-V3. Human preferences showed no universal reasoning advantage: GPT-5 was modestly preferred over GPT-4o (60.0--62.9\%), whereas DeepSeek-R1 trailed V3 (42.9\%), and inter-reader agreement was near chance (Krippendorff's $\alpha = 0.070$), with within-reader consistency and recurring weighting patterns suggesting structured heterogeneity rather than random responding. The judge, by contrast, favored reasoning outputs in 89.0\% of dimension-level comparisons and 59 of 60 pairs on aggregate PDS, uniformly across all five evaluator configurations, and its scores were associated with surface features such as sentence length and lexical diversity. These results suggest that development-set performance is insufficient evidence for deployment validity on a shifted distribution, and that point-estimate judges can obscure the heterogeneity in subjective human evaluation.

**ИИ:** ? · обе модели · неясен конструкт · An LLM judge and human readers both rated short stories on the Psychological Depth Scale; unclear if this is a psychological construct or literary quality.

**Решение:** =

---

### 789 · R5054

**Mechanistic control of large language models as simulated participants via linear representation**

2026 · npj Artificial Intelligence · article · en · https://doi.org/10.1038/s44387-026-00160-9

Large Language Models (LLMs) have garnered significant attention within psychology due to their potential to simulate human participants. However, recent studies often rely on simple prompt engineering that elicits behavioral patterns without directly manipulating internal model states. We introduce a novel simulation method, hypothesizing that high-level psychological traits correspond to specific directional vectors within the LLM’s activation space. We extract activation-space vectors corresponding to 18 clinically relevant cognitive schemas, known as early maladaptive schemas (EMS) in schema therapy. Our experiments demonstrate that projection onto these vectors is associated with externally evaluated EMS expression in LLM outputs. Linear manipulation of these vectors further induced EMS expression. Our work offers a mechanistically informed complement to prompt-based simulation and represents a step toward building more stable, controllable, and interpretable simulated participants.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly LLM steering/simulation of maladaptive schemas; 'externally evaluated' EMS expression may involve an LLM rater validated against humans.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM activation steering to simulate participants with schema expression; this is generation and control, not LLM coding of texts against human labels.)

**Решение:** -

---

### 790 · R5076

**Automated Multiple Mini Interview (MMI) Scoring**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2602.02360

Assessing soft skills such as empathy, ethical judgment, and communication is essential in competitive selection processes, yet human scoring is often inconsistent and biased. While Large Language Models (LLMs) have improved Automated Essay Scoring (AES), we show that state-of-the-art rationale-based fine-tuning methods struggle with the abstract, context-dependent nature of Multiple Mini-Interviews (MMIs), missing the implicit signals embedded in candidate narratives. We introduce a multi-agent prompting framework that breaks down the evaluation process into transcript refinement and criterion-specific scoring. Using 3-shot in-context learning with a large instruct-tuned model, our approach outperforms specialised fine-tuned baselines (Avg QWK 0.62 vs 0.32) and achieves reliability comparable to human experts. We further demonstrate the generalisability of our framework on the ASAP benchmark, where it rivals domain-specific state-of-the-art models without additional training. These findings suggest that for complex, subjective reasoning tasks, structured prompt engineering may offer a scalable alternative to data-intensive fine-tuning, altering how LLMs can be applied to automated assessment. 18 pages, 2 figures

**ИИ:** ? · обе модели · неясен конструкт · LLM scores MMI interview transcripts for empathy, ethical judgment and communication against human expert scores (QWK); unclear whether this counts as a psychological construct.

**Решение:** =

---

### 791 · R5103

**Mensch und Maschine als Kodierende: Reliabilität eines großen Sprachmodells in der qualitativen Inhaltsanalyse studentischer Hochschulvorstellungen**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · de · https://doi.org/10.5281/zenodo.22980972

Die hochschulpolitische Diskussion um Studienerfolg, Studienabbruch und das Studierendenerleben gehört seit Jahren zu den prominenten Themen der empirischen Hochschulforschung (Heublein et al., 2017; Pelz et al., 2024). Parallel hat die Digitalisierung der Lehre, beschleunigt durch die SARS-CoV-2-Pandemie, neue Forschungsfragen aufgeworfen - etwa zur studentischen Partizipation in digitalen Formaten (Lohberger & Braun, 2024) oder zur Eignung digitaler Unterstützungsangebote für heterogene Studierendengruppen (Sielschott et al., 2025). Künstliche Intelligenz (KI) ist in diesem Zusammenhang in doppelter Hinsicht relevant: als Forschungsgegenstand - wie Studierende KI in ihrem Studienalltag wahrnehmen (Hüsch et al., 2025; Marczuk et al., 2025) - und als Forschungswerkzeug, das die Auswertung großer qualitativer Datenbestände potenziell verändert (Than et al., 2025). Die qualitative Inhaltsanalyse nach Mayring (2022) ist ein methodisches Rückgrat der empirischen Hochschulforschung: Sie verbindet regelgeleitete Kategorienbildung mit Intercoder-Reliabilitätsprüfungen und ermöglicht die systematische Auswertung offener Antworten, Interviewdaten und Dokumente. Mit dem Aufstieg generativer Sprachmodelle stellt sich die Frage, ob und in welcher Form große Sprachmodelle die menschliche Zweitkodierung methodisch sinnvoll ergänzen können. Internationale Vorarbeiten zeigen, dass solche Modelle in bestimmten Annotationsaufgaben menschliche Plattformarbeitende hinsichtlich Übereinstimmungsmaßen erreichen oder übertreffen (Gilardi et al., 2023; Ziems et al., 2024). Andere Studien dokumentieren systematische Verzerrungen, Halluzinationen und Reliabilitätsschwankungen je nach Modell, Prompt und Domäne (Misra et al., 2026; Pangakis et al., 2023; Reiss, 2023; Törnberg, 2023). Vor diesem Hintergrund leistet der vorliegende Beitrag einen methodischen Beitrag zur qualitativen Hochschulforschung: Er untersucht an einem konkreten Anwendungsfall, unter welchen Bedingungen ein großes Sprachmodell (Claude Opus 4.7) die menschliche Zweitkodierung in Mayring-basierten Inhaltsanalysen reliabel ergänzen kann. Anhand einer dreifachen Parallelkodierung - Erstautorin, menschlicher Zweitkodierer und LLM - wird die Intercoder-Reliabilität systematisch ausgewiesen und durch einen formalen Bootstrap-Test der Kappa-Differenz statistisch abgesichert. Als Anwendungsfall dient eine Erhebung studentischer Vorstellungen von einer „perfekten Hochschule“ (N = 174) an einer Hochschule für angewandte Wissenschaften; die inhaltlichen Befunde dienen der methodischen Illustration. Der Beitrag versteht sich als Fallstudie ohne Anspruch auf Repräsentativität und expliziert seine Grenzen in Abschnitt 6.3.

**ИИ:** разошлись — Opus ? (неясен конструкт: Claude Opus coded open responses alongside two human coders and reported kappa, but it is unclear whether students' ideal-university conceptions count as psychological.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM–human intercoder reliability study, but the coded content is student ideas of a "perfect university" (higher-education research), not a psychological or clinical construct.)

**Решение:** -

---

### 792 · R5109

**Towards Reliable Evaluation of Emotional Text Generation in LLMs: Human vs. Automatic Metrics**

2026 · Language Resources and Evaluation Conference (LREC) · journalarticle, conference-paper · en · https://doi.org/10.63317/554t7yighn5u

Evaluating emotion generation in large language models (LLMs) remains a challenging problem due to the subjective nature of emotions and the lack of reliable automatic evaluation metrics. In this paper, we introduce a robust and extensible benchmark for systematically assessing automatic metrics in emotion generation tasks. The benchmark currently includes 13 automatic evaluation metrics and five state-of-the-art LLMs, and can be easily extended without requiring additional human annotations. Through a correlation analysis with human evaluations on a carefully curated annotated subset, we identify the emotion recognition score (ERS) metric, computed with DeepSeek v3.2 and GPT-5-nano, as the most reliable automatic evaluator, achieving correlations exceeding 0.98 and 0.95. Interestingly, despite relying on the same underlying LLM (GPT-5-nano), the emotion absolute score (EAS) metric shows a negative correlation, demonstrating that LLM strength alone does not guarantee automatic metric alignment with human judgment. We also provide lightweight, non-LLM-based alternatives, suitable for low-resource settings where large models are not accessible. A comprehensive per-class emotion analysis further highlights the strengths and weaknesses of the evaluated models. Overall, our results offer a practical and scalable framework for benchmarking emotion generation evaluation metrics and pave the way for more reliable, fair, and interpretable emotional language evaluation.

**ИИ:** разошлись — Opus + (LLM-судья: LLM-based emotion recognition of generated texts validated against human emotion annotations; check whether agreement is per text or only across models.); Sonnet ? (неясен конструкт: LLM-based emotion recognition metrics on generated text are correlated with human evaluations. It is unclear whether this is item-level coding agreement or only metric-level correlation of generation quality.)

**Решение:** +

---

### 793 · R5114

**Unveiling Power Dynamics in Relational Recovery: A Computational Analysis of Therapeutic Dyad Interviews**

2026 · ArTS Archivio della ricerca di Trieste (University of Trieste https://www.units.it/) · book-chapter · en · https://hdl.handle.net/11577/3604419

Recovery from severe mental distress emerges through relational processes co-constructed between individuals and their support networks. A central aspect of these processes concerns latent power dynamics within the relationships aimed at recovery. While research on these dynamics has been predominantly qualitative, the field lacks quantitative methods to measure how power asymmetries manifest linguistically. This study develops a multilayered computational framework to measure and represent relational power dynamics in mental health narratives. We apply a hybrid approach combining corpus analysis with LLM-based methods to interviews collected within the EXIT MADNESS project; participants (utenti) in stable recovery (5+ years) were interviewed with facilitators (facilitatori) they identified as most significant to their recovery, both in-pairs and individually. First, a descriptive corpus analysis through basic statistics, correspondence analysis and keyness ananlysis was conducted on all interviews (25 dual, 50 individual) in order to inspect some key patterns within the corpora. Then, the analysis of power dynamics was conducted exclusively on the dyadic interviews, by integrating lexical-surface indices, with large language model (LLM-as-a-judge) evaluations. Results show that dyadic interviews occupy an intermediate yet distinct lexical space, supporting the idea of co-constructed discourse. Both indices and LLM evaluations capture power as dynamic and temporally evolving consistent with our theory. Overall, the study bridges qualitative and computational approaches, and suggests AI-based tools for analyzing relational dynamics in therapeutic settings.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM-as-a-judge rates power dynamics in therapeutic dyad interviews; the abstract doesn't say whether the LLM ratings were checked against human coding.

**Решение:** =

---

### 794 · R5115

**Reading Gendered Mobility from Open-Ended Survey Responses: An Auditable, Theory-Informed, LLM-Assisted Coding Framework for Women's Travel in Dhaka**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7353857

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · LLM-assisted coding of open survey responses on women's travel; no abstract; psychological construct (e.g., safety, fear) and human comparison unclear.

**Решение:** =

---

### 795 · R5143

**Eating disorder-related content in Reddit suicidal ideation posts: an LLM-assisted analysis of mental health comorbidities, substance use, and demographic patterns**

2026 · Social Network Analysis and Mining · article · en · https://doi.org/10.1007/s13278-026-01647-8

Eating disorders are severe psychiatric conditions characterized by a markedly elevated risk of suicidal ideation and behavior. Although prior research has documented these associations in clinical settings, the underlying psychosocial and behavioral dynamics of such co-occurrence remain underexplored in non-clinical contexts, such as social media health narratives. This cross-sectional study examines the prevalence, demographic characteristics, and patterns of co-occurring mental health conditions and substance use among individuals who self-identify as having eating disorders and express suicidal ideation on Reddit’s r/SuicideWatch community. Using a validated keyword-based filtering framework informed by large language model–generated keyword expansion, we identified 688 eating disorder–related posts from a corpus of 27,434 suicidal ideation posts, representing a co-occurrence prevalence of 2.5% (95% CI: 2.33%–2.70%). Among posts with self-reported gender (n=75), females were the largest group (42.7%); among posts with self-reported age (n=170), individuals aged 18–20 were most represented (28.8%). Co-occurring mental health conditions were referenced in 79.0% of posts (95% CI: 75.8%–81.9%), particularly depression (43.9%) and anxiety (31.5%), alongside alcohol as the most prominent substance. These findings illustrate how social media discourse can complement clinical research in characterizing high-risk populations, with potential implications for the design of targeted digital mental health interventions for adolescents and young adults at the intersection of eating disorders and suicide risk.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM expanded keywords for filtering Reddit posts; unclear whether an LLM coded posts for comorbidities and was validated against human coding.

**Решение:** =

---

### 796 · R5157

**Developing AI tools to help quantify police involvement with vulnerable people**

2026 · White Rose Research Online (University of Leeds, The University of Sheffield, University of York) · report/report, book · en · https://doi.org/10.48785/100/469

Police often engage with individuals experiencing a range of vulnerabilities. Estimating the prevalence of these interactions is challenging – current methods rely on either counting “flags” in police information systems that may be inconsistently applied, or resource-intensive manual analyses of typically small samples of incidents. Our research instructs large language models (LLMs) to identify vulnerability indicators in unstructured police incident logs and evaluates how they perform compared to human coders. Using publicly available incident logs from Boston Police Department, we tested our method by prompting both humans and instruction-tuned LLMs (IT-LLMs) to identify several vulnerabilities (mental ill health, substance misuse, alcohol dependence, and homelessness). Results show that IT-LLMs effectively screen out narratives where vulnerabilities are absent and demonstrate minimal demographic bias, offering a promising approach for analysing large-scale unstructured police data that could be applied to a much broader range of policing actions and contexts.

**ИИ:** + · обе модели · кодирование по кодбуку · Instruction-tuned LLMs flagged mental ill health and substance misuse in police incident narratives, and their labels were compared with human coders.

**Решение:** =

---

### 797 · R5166

**The Age of Curiosity Meets the Age of AI: Benchmarking Child Safety in Large Language Models**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.25510

Children increasingly have access to Large Language Models (LLMs), which may expose them to responses that are developmentally inappropriate or require age-sensitive safety, guidance, and boundaries. Existing LLM safety evaluations largely focus on general harmful-content avoidance and do not explicitly target child-facing safety. We introduce KIDBench, a benchmark for evaluating child-facing LLM safety for ages 7-11 using a LLM-as-a-Judge rubric grounded in developmental-psychology. KIDBench contains realistic child queries across ten categories, with single-turn prompts and multi-turn child-actor simulations. We compare no-cues prompts with no child context, implicit-cues prompts that suggest a child speaker, and explicit age instructions. Implicit-cues improve scores by 8.6-46.8% over no-cue, while explicit age provides an additional 9.9-30.4% improvement over implicit-cues. Cross-lingual and cultural evaluations show uneven safety behavior across languages and country contexts. Multi-turn simulations show peak quality drops of up to 0.959 points on the 1-5 scale. We also introduce KIDGuardLlama, a child-safety evaluator, and KIDLlama, a child-safe response model. Code, data, and evaluation resources are available at https://github.com/MichiganNLP/kidbench.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM-as-judge child-safety rubric based on developmental psychology; unclear whether it was validated against human ratings or whether the construct counts as psychological.

**Решение:** =

---

### 798 · R5183

**Experimental Package: Investigating the use of LLMs in Deductive Coding within the Context of Software Engineering**

2026 · Zenodo (CERN European Organization for Nuclear Research) · other/, other · en · https://doi.org/10.5281/zenodo.19651325

This repository contains the Experimental Package for the article titled “Investigating the Use of LLMs in Deductive Coding in the Context of Software Engineering.” The study explores the potential of using Large Language Models (LLMs) to support the deductive coding process in qualitative research in the field of Software Engineering. Content of the material To comply with double-blind peer review requirements, all author identification and affiliation information has been omitted. The files provided are intended to ensure transparency and replicability of the experiments presented, including: Automation scripts: source code used for execution and data processing; Instruction templates: the specific frameworks and instructions provided to the models; Coded datasets: data processed during the qualitative coding stages; Detailed results: comprehensive qualitative analysis derived from the experiments. This material is intended for editorial evaluation and will be updated with the authors’ identities after the peer-review process is completed.

**ИИ:** ? · обе модели · неясен конструкт · LLM deductive coding of software-engineering qualitative data; unclear whether constructs are psychological or whether human-coded comparisons are reported.

**Решение:** =

---

### 799 · R5184

**Investigating the Potential of Large Language Models to Support Qualitative Data Analysis - Replication Package**

2026 · Zenodo · text/ · https://doi.org/10.5281/zenodo.22738780

Replication Package: Investigating the Potential of Large Language Models to Support Qualitative Data Analysis This repository gathers the complete replication package and open data regarding the master's dissertation entitled: Investigating the Potential of Large Language Models to Support Qualitative Data Analysis. The research analyzes the behavioral patterns, inferential limitations, and Prompt Engineering strategies of Large Language Models (LLMs) — specifically Google Gemini 2.5 Pro — in supporting deductive qualitative coding under the continuous supervision approach (Human-in-the-Loop). The investigation is based on two experimental cycles in sociotechnical domains of Software Engineering: Cycle 1 (Base Study - Empathy): 238 discursive excerpts across 4 analytical dimensions (Meaning, Barriers, Practices, and Effects) under a multi-label classification regime with 54 codes. Cycle 2 (Replication Study - Psychological Safety): 100 excerpts in 2 dimensions (Interpersonal Challenges and Practices) under a single-label classification regime with 18 codes. Package Content and Directory Structure The artifacts are structured to ensure transparency, auditability, and immediate reproducibility: 01_corpora: Textual excerpts extracted from professional communities (DEV Community and SE-SWE) in raw and pre-processed formats, indexed by unique identifiers. 02_codebooks: Complete reference codebooks for Empathy and Psychological Safety, containing operational definitions and explicit inclusion/exclusion rules. 03_prompts: Standardized instruction templates structured into 6 components (Persona Definition, Contextualization, Conceptual Codebook, Explicit Instructions, Structured Output with Mandatory Justification, and One-Shot and Few-Shot Anchoring Examples). 04_scripts: Python automation code (via official Google Generative AI library), including rate control (sleep time), segmentation in batches of 10 excerpts, and CSV persistence routines. 05_raw_model_outputs: Raw and immutable records of the inferences generated by Gemini 2.5 Pro, with assigned codes and their respective complete textual justifications. 06_qualitative_analysis_and_irr: Initial inter-rater reliability (IRR) data, independent blind evaluation matrices, consensus spreadsheets, and complete categorization according to the Taxonomy of Concordance and Divergence (5 classes). 07_expert_panel: Focus Group moderation protocol, slide decks for blind case presentations, full transcripts, and deliberation reports from senior experts. Main Contributions Provided Framework for Assisted Deductive Coding Support (SCDA): Methodological guidelines structured on three pillars (Input Rigor, Prompt Optimization, and Human Curation). Taxonomy of Concordance and Divergence: Formal conceptual scheme to classify and qualify divergences between human annotations and automated inferences. Mapping of Interpretative Axes: Empirical data contrasting the model's behavior between the Literal-Descriptive Axis and the Analytical-Subjective Axis.

**ИИ:** + · обе модели · кодирование по кодбуку · Gemini 2.5 Pro applied empathy and psychological-safety codebooks to community excerpts; IRR against human annotations reported (replication package).

**Решение:** =

---

### 800 · R5210

**Can ChatGPT Automate Qualitative Thematic Analysis? A Comparative Study of Input Design and Structured Prompting Strategies**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6547580

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. A ChatGPT thematic analysis comparison might involve coding against humans, but the data domain and comparison level are unclear.

**Решение:** =

---

### 801 · R5212

**An agentic red teaming framework for evaluating psychological safety and developmental appropriateness in child-facing AI**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/2dzmy

This project develops and pilots an agentic red teaming framework for evaluating psychological safety and developmental appropriateness in child-facing AI. It assesses child-facing systems through multi-turn, multilingual scenarios across key safety dimensions, including safeguarding, relational safety, epistemic safety, and developmental fit. The study combines an agentic LLM-as-judge workflow with expert human review to test whether current AI products are safe and appropriate for children aged 6-12.

**ИИ:** ? · обе модели · другое · OSF pre-registration with an LLM-as-judge plus expert review of the psychological safety of child-facing AI. It may be a protocol only, and LLM-human agreement is unclear.

**Решение:** =

---

### 802 · R5215

**Evaluating Agreement Between Human Consensus and Large Language Model Ratings of Suicide Reporting**

2026 · Research Square · preprint, ppr, posted-content · https://doi.org/10.21203/rs.3.rs-9904774/v1

Abstract Responsible reporting on suicide is an important public health strategy but monitoring whether news articles follow reporting recommendations is difficult at scale. While the Tool for Evaluating Media Portrayals of Suicide (TEMPOS) provides a structured approach of rating suicide-related media, human rating requires time, training, and repeated exposure to distressing content. Acknowledging these challenges, our research examines whether large language models (LLMs) can rate incident-focused suicide news articles using TEMPOS with agreement comparable to human raters. We conducted a reliability and agreement study using 42 news articles describing suicide deaths. Seven trained human raters and five LLMs independently rated each article using TEMPOS. Human interrater reliability was assessed using intraclass correlation coefficients (ICCs). A human consensus benchmark, HumanGold, was calculated as the mean TEMPOS score across human raters for each article. Agreement between individual AI models and HumanGold was examined to develop an aggregated AI score, termed AISilver. Individual AI models demonstrated moderate to strong correlations with HumanGold, ranging from r = 0.489 to r = 0.812. AISilver also showed strong agreement with HumanGold ( r = 0.797), comparable to the highest performing model, Grok ( r = 0.812). Overall, we found that LLMs showed alignment with trained human raters when applying TEMPOS. These findings suggest that AI may be a plausible tool to assist with continuous, large-scale monitoring of suicide-incident reporting, particularly if paired with human oversight. While AI ratings should be interpreted as consensus-aligned screening tools rather than definitive judgments, they may offer a practical path for expanding feedback on suicide-incident reporting. </p

**ИИ:** ? · обе модели · неясен конструкт · LLMs and trained humans rated suicide news articles with TEMPOS; the agreement design fits, but whether media-reporting quality counts as a psychological construct is unclear.

**Решение:** =

---

### 803 · R5232

**The 'Depressometer' Project: A Multimodal Longitudinal Dataset for Studying the Intrapersonal and Interpersonal Mechanisms of Change in Psychotherapy for Depression**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/2fbxy_v1

The data of the "Depressometer" project were collected between October 2018 to February 2021 from 58 patients diagnosed with MDD and 13 therapists during a 16-session supportive-expressive psychodynamic psychotherapy for depression. The present document provides a detailed description of the project’s methodology, including participants, treatment, measures, assessment procedures, and available data sources. The main goal of the project was to investigate the interpersonal and intrapersonal mechanisms underlying change in psychotherapy for Major Depressive Disorder (MDD), using a multimodal, intensive longitudinal psychotherapy dataset. The project was designed to examine how clients’ and therapists’ emotional, cognitive, behavioral, physiological, and relational processes unfold within and across sessions, and how these processes are associated with proximal and distal therapeutic change. The project includes repeated assessments from both clients and therapists across multiple temporal resolutions, ranging from treatment-level, session-level, follow-up self-reports, and clinician assessments, to fine-grained, within-session linguistic, vocal, facial, movement, physiological, and hormonal measures collected during sessions. In addition, a subsample of sessions was manually coded for patients’ changing affective, behavioral and cognitive experiences, for therapists’ interventions as well as clinicians’ summaries of the sessions. These human annotations were designed to support LLM-based large-scale further analyses of the full dataset, with the goal of examining patterns, dynamics and sequences that may facilitate (or hinder) treatment processes and outcomes. The project was conducted in the Psychotherapy Research Lab at the Department of Psychology, Bar-Ilan University, Israel. The research was approved by the Institutional Review Board.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Dataset paper with human-coded session annotations meant to support LLM analyses; unclear whether LLM–human agreement is reported.

**Решение:** =

---

### 804 · R5235

**Psychosocial challenges and substance use among suicidal autistic individuals on social media: LLM-assisted keyword generation with human-in-the-loop refinement.**

2026 · International journal of medical informatics · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.1016/j.ijmedinf.2025.106110

BACKGROUND: Autism Spectrum Disorder (ASD) is associated with an elevated risk of suicidal ideation due to various co-occurring psychosocial challenges. Although these challenges are recognized, their extent and prevalence-particularly autism-specific difficulties and substance use patterns among individuals with ASD-remain largely unexplored, especially within social media health discussions, where individuals frequently express their thoughts and emotions. A comprehensive understanding of these aspects is essential to develop targeted prevention strategies that mitigate suicide risk among individuals with autism. OBJECTIVE: This study addresses this gap by examining the complex challenges contributing to suicidal ideation among individuals with ASD-including autism-specific factors and substance use patterns-through the lens of social media discourse. METHODS: We conducted a keyword-based analysis integrating large language models (LLMs) with human-in-the-loop refinement, focusing on three prominent categories of challenges: (i) interpersonal and social struggles, (ii) sensory and emotional regulation difficulties, and (iii) co-occurring mental health conditions. Keywords were generated by an LLM, validated by humans, and applied to analyze online health discourse to identify patterns and prevalence of these key challenges. A similar LLM-based approach was employed to assess substance use prevalence. RESULTS: The most prevalent challenges reported were mental health conditions (52.4 %; 95 % CI: [0.487, 0.561]) and social isolation (48.9 %; 95 % CI: [0.452, 0.526]). Less common but significant challenges included bullying (23.2 %; 95 % CI: [0.201, 0.263]) and issues with identity and self-acceptance (20.3 %; 95 % CI: [0.173, 0.233]). The strongest-but still weak-correlation was observed between social isolation and bullying. Additionally, substance use-including alcohol, cannabis, and prescription drug misuse-was also prevalent in this population. CONCLUSION: This study highlights the diverse characteristics and underlying factors contributing to suicidal ideation among individuals with ASD, including social isolation, bullying, autism-specific challenges, co-occurring mental health conditions, and substance use patterns. These findings emphasize the need for tailored mental health interventions, inform preventive strategies, and demonstrate the value of social media health data in advancing research in this area.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM-generated keywords and LLM-based substance-use detection applied to suicidal autistic posts; unclear whether post-level coding was validated against human annotation.

**Решение:** =

---

### 805 · R5270

**Quantification of Qualitative Data Using Large Language Models: A Novel Methodology for Physical Therapy Integration**

2026 · Korean Institute of Smart Media · journalarticle, article · https://doi.org/10.30693/smj.2026.15.2.20

Qualitative analysis constitutes an essential methodological approach in physical therapy research, offering comprehensive insights into patients' subjective experiences, perceptions of therapeutic interventions, and recovery trajectories, thereby facilitating evidence-based intervention development and optimizing clinical outcomes. Nevertheless, conventional qualitative analytical approaches applied to physical therapy patient interviews encounter substantial limitations regarding analytical efficiency and inter-rater reliability. The present study examines the integration of Large Language Models (LLMs) into qualitative research methodologies within the physical therapy domain to address these methodological constraints. Semi-structured interviews were conducted with one stroke patient as a pilot case, and three LLMs (ChatGPT, Claude, and Gemini) were employed with 160 iterative measurements each to implement the Large Language Model Quotient (LLMq) methodology—a quantitative framework for systematic qualitative coding—to evaluate its validity and applicability within the physical therapy research context. Intraclass correlation coefficient (ICC) analysis demonstrated ICC(3,1) of 0.802 and ICC(3,k) of 0.924, meeting Cicchetti's (1994) criteria for excellent reliability. Findings demonstrate that this analytical approach significantly enhances the efficiency of qualitative data analysis (reducing analysis time from weeks-months to hours-days) while mitigating subjective interpretive bias (ICC 0.802), thereby substantiating the considerable methodological value that LLM-based approaches confer upon physical therapy research endeavors.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLMs code a stroke patient's interview about subjective experiences; the reported ICC may be LLM–LLM only, and a comparison with human coders is unclear.

**Решение:** =

---

### 806 · R5273

**Beyond Emotion Labels: Can LLMs Capture Human Appraisal and Emotion Distributions?**

2026 · IEEE International Symposium on Robot and Human Interactive Communication · conference · https://doi.org/10.1109/ro-man72286.2026.11714649

Prior evaluations of large language models (LLMs) on emotion understanding have largely focused on surface-level recognition accuracy, leaving open whether LLMs capture the appraisal-based structure underlying emotions or reproduce the distributional variability observed across human judgments. In Study 1, we compared LLM-generated appraisal ratings against human annotations across seven appraisal dimensions and seven emotion categories using a corpus of first-person emotional narratives. Models achieved high accuracy overall but consistently misclassified shame as guilt; appraisal agreement was strongest for pleasantness and responsibility but substantially lower for certainty, control, and circumstance. In Study 2, we examined whether LLMs reproduce the distributional properties of human emotion judgments using a Korean multi-label emotion corpus with 43 categories. Both models produced higher-entropy distributions over more emotion labels. Shared human-model PCA showed that human and model judgments were partly organized by common coarse emotion dimensions. However, model responses were shifted away from human annotations and more widely dispersed in this joint space. Together, these findings suggest that current LLMs exhibit partial structural alignment with human emotion understanding, highlighting the importance of evaluation beyond label-level accuracy.

**ИИ:** + · обе модели · бенчмарк с метками людей · LLM appraisal and emotion ratings of first-person emotional narratives compared with human annotations; agreement reported per dimension.

**Решение:** =

---

### 807 · R5276

**Diagnostic Accuracy of GPT‐Based Large Language Models Across Versions, Prompting Techniques, and Case Presentation Formats**

2026 · Human Behavior and Emerging Technologies · journalarticle, article · en · https://doi.org/10.1155/hbe2/4674484

Despite the centrality of the diagnostic assessment in psychiatry, the agreement among mental health practitioners often varies from poor to moderate. The potential of large language models (LLMs; such as gpt‐based models), among other approaches, has been studied to be used as standardized tools to support clinicians’ decision‐making. The current work investigates the diagnostic accuracy of gpt‐based LLMs (gpt‐3.5 and gpt‐5.1) across different case presentation styles (i.e., vignette and outline) and prompting techniques. A total of 46 psychiatric cases with an accompanying diagnosis were used. Two trained clinical psychologists evaluated the proximity of the generated diagnosis against the reference diagnosis. A robust statistical approach was then used to investigate the effect of case format and prompt type on the average diagnostic accuracy. Importantly, accuracy in this context reflects alignment with a reference label under constrained vignette‐based inputs, rather than equivalence with comprehensive clinical diagnostic practice. The results showed a strong agreement between the ratings of the two clinical psychologists ( kappa = 0.798), with moderate agreement for gpt‐3.5’s diagnoses and almost perfect for gpt‐5.1’s diagnoses. Overall, gpt‐5.1 showed higher diagnostic accuracy and proximity to human diagnostic evaluations than gpt‐3.5 ( p < 0.001). For gpt‐3.5, a small but statistically significant main effect of prompting technique on diagnostic accuracy emerged ( p = 0.009). The highest proximity to the reference diagnosis was achieved when gpt‐3.5 was simply instructed to provide and justify a single diagnosis for each case, as compared to when it was asked to provide a diagnosis likelihood ( p < 0.001) or when it was asked to act as a clinical psychologist ( p = 0.001). Conversely, gpt‐5.1 showed high performance independent of the prompting technique and case format. Under these experimental conditions, the results of the current work provide preliminary evidence supporting the potential use of LLMs as tools to assist the diagnostic process in psychiatry and provide general indication for slightly optimizing their performance. Additionally, this study offers a methodological framework that can serve as an example for future research aiming to systematically evaluate LLMs’ diagnostic capabilities across different prompting strategies and case presentation formats.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: GPT diagnoses psychiatric vignettes against reference diagnoses that are probably expert-assigned. Unclear whether this counts as human coding of the same text or as criterion validity.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): GPT generates diagnoses for vignettes; psychologists rate proximity to reference diagnosis. This is diagnostic accuracy, not LLM coding of text against human coders.)

**Решение:** -

---

### 808 · R5298

**Automated Thematic Analysis for Clinical Qualitative Data: Iterative Codebook Refinement with Full Provenance**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2603.08989

Thematic analysis (TA) is widely used in health research to extract patterns from patient interviews, yet manual TA faces challenges in scalability and reproducibility. LLM-based automation can help, but existing approaches produce codebooks with limited generalizability and lack analytic auditability. We present an automated TA framework combining iterative codebook refinement with full provenance tracking. Evaluated on five corpora spanning clinical interviews, social media, and public transcripts, the framework achieves the highest composite quality score on four of five datasets compared to six baselines. Iterative refinement yields statistically significant improvements on four datasets with large effect sizes, driven by gains in code reusability and distributional consistency while preserving descriptive quality. On two clinical corpora (pediatric cardiology), generated themes align with expert-annotated themes. Submitted to AMIA 2026 Annual Symposium (American Medical Informatics Association)

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: The LLM generates and refines codebooks automatically; the only human comparison is how well its themes align with expert themes, with no coding of the same units.); Sonnet ? (неясно, сравнивали ли с людьми: LLM thematic analysis of clinical interviews; themes compared with expert-annotated themes, so possibly theme-level only, but code-level human comparison is unclear.)

**Решение:** -

---

### 809 · R5299

**The Application of Generative AI in Project Management; Focusing on Text-Mining Projects for Human Resources**

2026 · Procedia Computer Science · conference-paper · en · https://doi.org/10.1016/j.procs.2026.03.196

This study empirically examines the application of Generative AI in project management, specifically GPT-3.5 and BERT, in optimizing text analysis processes within Human Resource (HR). Considering the potential impact of AI on handling qualitative data in HR, this research aims to evaluate how AI-driven text analysis performs in comparison to traditional human methods, particularly in terms of accuracy and efficiency. Using a dataset of 2,420 responses from compliance and organizational culture surveys, the text classification and clustering performance of AI models were compared with that of human experts. The analysis showed that GPT-3.5, even without fine-tuning, achieved a weighted average F1 score of 0.73, surpassing the BERT-based model’s score of 0.72. However, the fine-tuned BERT model achieved the highest accuracy, with a weighted average F1 score of 0.83. Furthermore, the time required for text data preprocessing and classification was significantly reduced from 70 hours to 8 hours with AI, indicating substantial improvements in efficiency. This study demonstrates the potential of Generative AI as a tool for achieving high accuracy and efficiency in text analysis within the HR domain. However, further research is needed to develop and validate AI models that can be applied across various HR areas for Project Management. Specifically, there is a need to improve embedding techniques and preprocessing methods to enhance AI’s analytical accuracy, as well as to assess the effectiveness of these models in a broader range of HR applications.

**ИИ:** ? · обе модели · неясен конструкт · GPT-3.5 classified open survey responses on compliance and organizational culture against human experts; unclear whether the categories are psychological constructs.

**Решение:** =

---

### 810 · R5300

**Voices Between Lines: Interpretable Labeling of Mental Health Minority Topics with Seed Guidance and LLMs**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-19105-2_19

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM labeling of mental-health topics might be compared with human labels, or might only be topic-level labeling.

**Решение:** =

---

### 811 · R5305

**Automated Fidelity Monitoring of Lay-Delivered Mental Health Interventions Using Large Language Models: Development and Pilot Validation of shamiriAI (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.95063

BACKGROUND Task-shifting—the delivery of evidence-based mental health interventions by trained lay providers—has shown promise in closing the treatment gap in low- and middle-income countries. But the effectiveness of task-shifted interventions depends critically on ongoing supervision and monitoring, yet traditional supervision models are difficult to scale. Artificial intelligence (AI) tools capable of automatically processing session recordings and generating structured fidelity feedback for supervisors could offer a scalable alternative, but no such system has been developed or validated for lay-delivered interventions in multilingual, low-resource settings. OBJECTIVE We developed and pilot-validated shamiriAI, an automated fidelity monitoring tool for lay-delivered mental health interventions, embedded within the Shamiri school-based mental health program in Kenya. METHODS We conducted a pilot validation study across six secondary schools in Ngong Hub, Kajiado County, Kenya (May–September 2025). shamiriAI follows a five-stage pipeline: audio ingestion and preprocessing, multilingual automatic speech recognition (ASR) with prosodic feature extraction, personal identifiable information (PII) scrubbing, large language model (LLM)-based fidelity inference, and structured feedback report delivery to supervisors. We pursued two pilot aims: (1) ASR performance on a held-out test set of manually transcribed sessions; and (2) interrater reliability between shamiriAI-generated fidelity ratings and independent human supervisor ratings across 52 recorded sessions, spanning six domains (Required Contents, Specifics, Thoroughness, Clarity, Skill, Purity) rated on a 1–7 scale. Reliability was assessed using intraclass correlation coefficients (ICC), Bland-Altman analysis, adjacent agreement rates, paired-sample t-tests with Holm–Bonferroni correction, and Gwet's AC2. RESULTS The ASR model achieved a Character Error Rate of 0.19, Word Error Rate of 0.34, and cosine semantic similarity of 0.77, indicating strong meaning preservation despite surface-level transcription errors in code-switched speech. On fidelity ratings, AI scores were systematically lower than the human composite overall (M = 5.14, SD = 0.77 vs. M = 5.93, SD = 0.57; Δ = −0.79, 95% CI [−1.04, −0.53], d = −1.16, p < .001). Reliability varied markedly by dimension: ICCs ranged from −0.06 to 0.20 across all six domains. Three distinct patterns emerged: large systematic underrating on holistic interpretive dimensions (Required Contents d = −3.48; Clarity d = −1.56); a bidirectional medium-effect pattern on facilitation dimensions (Thoroughness d = −0.99; Skill d = +0.87); and no significant bias on structured detection dimensions (Specifics 78.8% adjacent agreement; Purity 73.1% adjacent agreement), where performance approached the human–human AC2 benchmark of 0.42–0.60. CONCLUSIONS shamiriAI demonstrates technically feasible multilingual ASR and a coherent, interpretable reliability profile. Underperformance was concentrated on holistic inferential dimensions — particularly Required Contents and Clarity — while structured detection tasks already approach operational utility. The underperformance pattern reflects diagnosable misalignments in rubric interpretation and prompt design, with clear engineering solutions identified. These findings provide the foundational validation evidence and dimension-specific diagnostics needed to guide the development of AI-augmented supervision for lay-delivered adolescent mental health programs in sub-Saharan Africa and other multilingual settings.

**ИИ:** + · обе модели · кодирование сессий · An LLM rated intervention fidelity in 52 session transcripts, and its ratings were compared with human supervisor ratings using ICC and Gwet's AC2.

**Решение:** =

---

### 812 · R5336

**Performance Over Growth: Exploring Self-Presentation Strategies in the Gig Economy**

2026 · Inquiry Queen s Undergraduate Research Conference Proceedings · journalarticle, conference, review · https://doi.org/10.24908/iqurcp21848

Introduction Goal orientation theory distinguishes learning orientation, a focus on developing competence by acquiring new skills and mastering new situations, from performance orientation, a focus on demonstrating existing competence to gain favourable judgment from others (Dweck, 1986; VandeWalle, 1997). Most research relies on self-report surveys, leaving open how these orientations appear in real, economically consequential self-presentation. We have access to a dataset of more than 30,000 profiles from a global online platform where freelancers describe their skills and experience to attract paying clients, offering a naturalistic window into this behaviour. Because earnings depend on self-presentation, mapping this language is a step toward examining who gets hired and paid more. Methods/Approach Our aim was to content-code these profiles for learning versus performance orientation language. I first reviewed the literature on large language model (LLM)-assisted qualitative coding in management and social science to identify best practices and trade-offs (Carlson & Burbano, 2026; Than et al., 2025). I then combined two established strategies: refining the coding prompt on a calibration sample, then testing it on a separate set of profiles held back from that refinement. With a second coder, I manually coded expressions of learning and performance orientation in 500 randomly selected profiles, assessing inter-rater reliability with Cohen’s kappa. This hand-coded set anchors classification of the full corpus via the Claude Batch API. Findings/Implications Inter-rater reliability for learning orientation reached kappa = 0.90, well above the recommended threshold of 0.80. Learning orientation language appeared in 31% of profiles, far less common than performance orientation language, which appeared in 94%. Freelancers overwhelmingly presented competence and results rather than capacity for growth. Validation of the LLM classifier against the hand-coded profiles is ongoing; once complete, coding the full corpus will allow us to test whether these self-presentation strategies shape who gets hired and earning outcomes. Supervisor: Christy Zhou Koval References Dweck, C. S. (1986). Motivational processes affecting learning. American Psychologist, 41(10), 1040-1048. VandeWalle, D. (1997). Development and validation of a work domain goal orientation instrument. Educational and Psychological Measurement, 57(6), 995-1015. Carlson, N. A., & Burbano, V. (2026). The use of LLMs to annotate data in management research: Foundational guidelines and warnings. Strategic Management Journal, 47(3), 699-725. Than, N., Fan, L., Law, T., Nelson, L. K., & McCall, L. (2025). Updating "The Future of Coding": Qualitative coding with generative large language models. Sociological Methods & Research, 54(3), 849-888.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Claude codes goal-orientation language in freelancer profiles against a human-coded set, but the LLM–human validation is still ongoing and may not be reported.

**Решение:** =

---

### 813 · R5347

**A Patient Simulation Framework for Risk Assessment of Conversational Health Care AI: Development and Evaluation Study.**

2026 · JMIR AI · journal article, med, journalarticle · eng · https://doi.org/10.2196/100772

Abstract Background Conversational AI systems are increasingly being deployed in health care for clinical decision support, but their performance varies substantially across patient communication styles, health literacy levels, and behavioral patterns. Static benchmarks cannot capture multiturn dynamics through which this variation compounds, and no current evaluation framework implements structured AI risk management guidance for conversational health care AI. The result is a structural risk: AI systems may perform well in aggregate while failing disproportionately for the populations they are intended to help. Objective This study aimed to develop and validate a patient simulation framework that aligns with the National Institute of Standards and Technology (NIST) AI Risk Management Framework (AI RMF) Map and Measure functions, providing an empirical basis for identifying and characterizing performance risks in conversational clinical AI across medical, linguistic, and behavioral patient variations. We applied the framework to a conversational decision aid for antidepressant selection in major depressive disorder (the AI decision aid). Methods The simulator integrated three profile dimensions: (1) medical profiles constructed from All of Us electronic health records using risk ratio gating; (2) linguistic profiles modeling a health literacy gradient and condition-specific communication; and (3) behavioral profiles representing cooperative, distracted, and adversarial engagement. We generated 500 simulated conversations and evaluated profile fidelity through human annotation and a large language model (LLM) judge, and then assessed downstream effects on the AI decision aid’s concept retrieval and antidepressant recommendations. Results The patient simulator expressed medical concepts with high fidelity (96.6% accuracy across 8210 concepts), with substantial human interannotator agreement (κ=0.73) and LLM-judge agreement against human annotators (κ=0.78). Behavioral profiles were reliably distinguished (κ=0.93; near perfect agreement), and linguistic profiles showed substantial agreement at the lower bound of the substantial range (κ=0.61), which can be considered adequate to support profile-level analysis. The framework revealed monotonic degradation in AI decision aid performance across the health literacy gradient. Rank-1 concept retrieval increased from 47.6% for limited health literacy to 81.9% for proficient health literacy, with corresponding declines in antidepressant recommendation accuracy. Conclusions Patient simulation grounded in the NIST AI RMF exposes measurable performance risks in conversational health care AI that static benchmarks miss, with direct equity implications. Health literacy operates as a structural risk factor, with degraded performance concentrated in patients carrying the greatest burden of psychiatric illness. The framework supports targeted risk-mitigation interventions before deployment. While we evaluated the framework only on antidepressant selection, extending it to other clinical decision-aid tasks remains an assignment for future work.

**ИИ:** ? · обе модели · неясен конструкт · LLM judge vs human annotators (κ=0.78) on simulated depression-patient conversations; mostly medical-concept fidelity, behavioral profile coding possibly psychological.

**Решение:** =

---

### 814 · R5384

**LingxiDiagBench: A Multi-Agent Framework for Benchmarking LLMs in Chinese Psychiatric Consultation and Diagnosis**

2026 · arXiv (Cornell University) · book, journalarticle, conference · https://doi.org/10.48550/arxiv.2602.09379

Mental disorders are highly prevalent worldwide, but the shortage of psychiatrists and the inherent subjectivity of interview-based diagnosis create substantial barriers to timely and consistent mental-health assessment. Progress in AI-assisted psychiatric diagnosis is constrained by the absence of benchmarks that simultaneously provide realistic patient simulation, clinician-verified diagnostic labels, and support for dynamic multi-turn consultation. We present LingxiDiagBench, a large-scale multi-agent benchmark that evaluates LLMs on both static diagnostic inference and dynamic multi-turn psychiatric consultation in Chinese. At its core is LingxiDiag-16K, a dataset of 16,000 EMR-aligned synthetic consultation dialogues designed to reproduce real clinical demographic and diagnostic distributions across 12 ICD-10 psychiatric categories. Through extensive experiments across state-of-the-art LLMs, we establish key findings: (1) although LLMs achieve high accuracy on binary depression--anxiety classification (up to 92.3%), performance deteriorates substantially for depression--anxiety comorbidity recognition (43.0%) and 12-way differential diagnosis (28.5%); (2) dynamic consultation often underperforms static evaluation, indicating that ineffective information-gathering strategies significantly impair downstream diagnostic reasoning; (3) consultation quality assessed by LLM-as-a-Judge shows only moderate correlation with diagnostic accuracy, suggesting that well-structured questioning alone does not ensure correct diagnostic decisions. We release LingxiDiag-16K and the full evaluation framework to support reproducible research at https://github.com/Lingxi-mental-health/LingxiDiagBench.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: LLMs diagnose from synthetic EMR-based dialogues with "clinician-verified" labels; unclear if clinicians coded the dialogues, and whether the LLM judge was checked against humans.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): Benchmark of LLM diagnosis prediction on synthetic dialogues against diagnostic labels; the LLM-as-Judge is compared with diagnostic accuracy, not with human ratings.)

**Решение:** -

---

### 815 · R5397

**RELATE: An Evaluation Framework for measuring Relational Orientation of Large Language Models**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.09569

Large language models (LLMs) are increasingly used for emotional support, raising concern that sustained use may draw users away from their real-world relationships. Yet existing evaluations primarily focus on the safety, empathy, or helpfulness of responses, leaving under-examined a relational question: where does the model orient the user for continued support? To address this question, we introduce relational orientation, a property operationalized through two non-exclusive dimensions: inward-facing (IF) language, which positions the AI as the user's ongoing source of support, and outward-scaffolding (OS) language, which encourages real-world human connection. Grounded in psychological and sociological literature, we formalize a taxonomy of relational orientation and present RELATE, a persona-conditioned framework for measuring inward-facing and outward-scaffolding language at the sentence level in multi-turn dialogues. RELATE pairs 76 help-seeking situations adapted from naturally occurring questions with three simulated user styles, providing 228 evaluation stimuli. In our experiments, we evaluate seven LLMs using dialogues with six assistant turns each, yielding 1,596 dialogues and 69,194 assistant sentences. We assess these sentences using a primary rubric-based LLM judge and apply a secondary judge to a subset. Under automated evaluation, we find that the proportion of sentences labeled as IF is higher at the sixth assistant turn than at the first, while the proportion labeled as OS is substantially lower for hesitant, indirect simulated users than for explicit, reassurance-seeking users. RELATE provides a reproducible framework and a sentence-level signal for auditing and steering the relational orientation of supportive LLMs.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · An LLM judge labels the relational orientation of sentences in emotional-support dialogues. The abstract does not say whether the judge was validated against human annotation.

**Решение:** =

---

### 816 · R5399

**ClinAuthBench_v1_Technical_Report**

2026 · Figshare · preprint/preprint, preprint · https://doi.org/10.6084/m9.figshare.33638287

ClinAuthBench v1 is a fully synthetic benchmark for evaluating evidence-grounded reasoning in adult inpatient psychiatric authorization. The benchmark contains 180 synthetic cases, each with dense 72-hour case documentation and hidden structured labels for safe-for-lower-level-of- care readiness, expected length-of-stay recommendation, evidence anchors, unsupported-claim constraints, documentation challenge categories, and synthetic trajectory metadata. The bench- mark is designed around a blind evaluation contract: during model-output retrieval, models receive only the case content, task instructions, and output JSON schema, while gold labels and other scoring metadata are withheld and used only later by local scoring code. In completed full-180 baseline runs, openai/gpt-oss-120b via Hugging Face pro- duced 180/180 schema-valid outputs with 93.3% safe-for-lower-level-of-care accuracy, while gpt-5.2 via OpenAI also produced 180/180 schema-valid outputs with 65.0% accuracy. Meta-Llama-3-8B-Instruct produced only 40/180 schema-valid outputs, illustrating that strict structured-output adherence is itself a benchmark-relevant behavior. Challenge-stratified analy- sis surfaced a striking directional pattern: on the current_vs_historical_risk subset, 100% of errors across both schema-valid runs (49/49) were in the over-conservative direction, where mod- els recommended continued inpatient stay despite documentation explicitly supporting lower- level-of-care readiness. Every failure case violated the hidden do_not_claim constraint “Do not confuse historical suicide risk with current risk,” indicating a systematic LLM default toward inpatient continuation when historical risk indicators are surface-readable. ClinAuthBench v1 is not a clinical deployment system, not a payer-policy simulator, and not derived from real patient data. Its contribution is a public, reproducible synthetic evaluation artifact for studying evidence-grounded authorization reasoning, structured-output reliability, and unsupported-claim control under a shared blin

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: LLMs rate psychiatric readiness/risk on synthetic case notes; gold labels appear to be synthetic by design, and it is unclear whether humans coded them.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): Synthetic benchmark where LLMs predict care-level readiness against generated gold labels; there are no human coders or raters and no coding of real psychological text.)

**Решение:** -

---

### 817 · R5401

**The Associations between Life Project Content and Life Project Involvement Across Age, Gender, and Nationality**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/8g364

This study is part of the larger Future Time Orientation and Life Project (FTOLP), a cross-cultural investigation of how individuals conceptualize and pursue their intended futures. Within this broader framework, the present study focuses specifically on the relationship between the life project (LP) content and LP involvement, examined across 15 countries. LPs are conceptualized as a dynamic, ongoing process through which individuals actively build and sustain purposeful commitments over time, together forming a coherent, future-oriented narrative that shapes everyday decisions and actions (Coscioni et al., 2021, 2023). LPs can be conceptualized along two complementary dimensions: their content (what domains individuals plan for) and their coherence (how clearly and actively individuals perceive and pursue their intended future). LP content is measured using the Life Project Mapping (LPM; Coscioni et al., 2024), an inductive tool in which participants list their life goals in free-text form. A large language model (LLM) tool was developed, validated, and used to perform automatic classification of these freely listed life goals into 14 theoretically meaningful life domains according to a structured coding taxonomy developed as part of the FTOLP project. From the LLM-coded responses, two quantitative indicators are derived: density, defined as the number of goals listed in general or within a given life domain, and priority, operationalized as the order in which life domains spontaneously emerge in the free-listing task, with earlier-mentioned domains reflecting higher priority. Density is calculated at the level of individual life domains as well as for the overall response, while priority is only calculated at the domain level. LP coherence is measured using the Life Project Scale (LPS; Coscioni et al., 2024), which assesses two factors: identification (awareness of one's intended future) and involvement (enactment of plans and actions in favor of one's intended future). The present study focuses exclusively on involvement as the outcome variable. The primary aim of this study is to examine to what extent LP content characteristics explain LP involvement. We also examine whether this association is moderated by gender and age group, and whether it varies across countries through random slope specifications. To further unpack this overarching question, we examine two secondary research questions. First, we examine how density and priority of LP content jointly explain LP involvement, and to what extent these associations vary across gender, age, and nationality. This question investigates whether involvement is shaped not only by which domains individuals mention, but also by how many goals they list within each domain and the order in which these domains emerge. Second, we ask which specific life domains are most strongly and consistently associated with LP involvement across different gender and age groups, and whether cultural similarities and differences emerge across countries. Unlike the main research question, which tests the overall association between LP content and involvement, this question identifies domain-specific patterns and examines whether the relative importance of each domain generalizes or diverges across demographic and cultural contexts. Data were drawn from the FTOLP dataset, comprising participants aged 18 to 65 from 15 countries (Brazil, China, India, Indonesia, Israel, Italy, Mexico, Mozambique, Netherlands, Portugal, Russia, Slovenia, South Africa, Turkey, and United States), with the survey administered in 12 languages. These participants collectively generated more than 30,000 life goals, as each respondent could list up to 15 goals. Gender and age are included as moderators, added to the best-fitting model identified in Model 1-3 (see Statistical Technique). Country is treated as a Level 2 clustering variable in the multilevel regression framework, with random slopes specified to examine cross-national variation in the associations between LP content indicators and involvement. This study contributes to the literature in two main ways. Substantively, it provides the first large-scale cross-cultural examination of how LP content characteristics, specifically the life domains individuals retrieve, the density of goals within each domain, and the priority with which domains emerge, relate to LP involvement across a broad demographically diverse, multi-national sample. Methodologically, it demonstrates the feasibility of applying LLM-based coding to large-scale inductive data, enabling cross-cultural analyses at a scale not previously achievable with manual coding approaches.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Pre-registration; LLM 'validated' for coding free-text life goals into domains, likely against human coders, but comparison details not reported.

**Решение:** =

---

### 818 · R5407

**Follow the Rules (or Not): Community Norms and AI-Generated Support in Online Health Communities**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2603.19093

Generative AI (GenAI) is increasingly being integrated into the online ecosystem, including online health communities (OHCs), where people with diverse health conditions exchange social support. For example, in OHCs, support providers are beginning to share content generated, directly or indirectly, by popular GenAI-based tools. OHCs are governed by norms that define appropriate behavior when providing support. Ways in which AI-generated support interacts with these norms remain underexplored. Inappropriate conformance or outright violation can erode seekers' trust, distort decision-making, and threaten community sustenance. In this work, we examine whether (and how) AI-generated support conforms to norms, using popular opioid-use recovery subreddits as our testbed. First, we provide an inventory of norms regulating text-based support provision in OHCs. Next, using human-validated LLM judges, we assess the prevalence of AI's conformity to these norms. Finally, through an expert review, we identify risks to seekers (and OHCs) resulting from norm (non)conformity. Our analysis revealed that, while AI-generated support conforms to norms, such conformity may be inappropriate or insufficient, for example, by over- or under-validating seekers in distress. Moreover, we observed instances of outright norm violation. This work provides insights that can help moderators and OHC designers adapt existing and develop new norms to regulate AI integration, protecting both seekers and communities they rely on.

**ИИ:** + · обе модели · LLM-судья · Human-validated LLM judges rate whether support responses in opioid-recovery subreddits conform to norms; humans checked the judges on the same texts.

**Решение:** =

---

### 819 · R5408

**Pedagogical AI in Mental Health: A Tri-Stream Fine-Tuned LLM Framework for Automated Clinical Supervision and Risk Triage**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.18438

Modern mental healthcare faces a critical shortage of senior supervisory oversight, leading to a "supervision gap" where novice therapists manage high-stakes risks with delayed professional feedback. This paper proposes a new framework utilizing a fine-tuned Mistral-7B-instruct model as an automated "Supervisor-in-the-Loop" system. By leveraging 106 sessions from the DAIC-WOZ dataset, the model performs a tri-stream analysis: (1) Therapeutic Alliance tracking via semantic adherence, (2) Latent risk prediction using attention-weighted analytics, and (3) Supervisory Triage via a Dynamic Clinical Urgency Index (D-CUI). Our multi-modal VAL (Visual-Acoustic-Linguistic) framework achieves 95% technique identification accuracy [95% CI: 75.1%-99.9%], alliance assessment MAE of 0.105 on a 5-point scale [95% CI: 0.059-0.151], therapeutic fidelity alpha = 0.423, and mean D-CUI of 0.370 [95% CI: 0.322-0.419]. Training converged in 105 steps with 85.2% loss reduction on a single Tesla T4 GPU. The system reduces supervisory triage latency from 72 hours to real time (~10 seconds per session), enabling proactive intervention in high-risk cases. The system addresses the cold-start problem through Bayesian priors and implements timestamp-based modality synchronization for robust multi-modal fusion. 14 pages, 1 figure, 2 tables. Accepted for publication in AICTC 2026, Lecture Notes in Networks and Systems, vol. 2165, Springer

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Fine-tuned Mistral rates alliance, technique and fidelity in DAIC-WOZ sessions; the abstract doesn't say whether the reference labels come from human coders.

**Решение:** =

---

### 820 · R5411

**InsightFlow: LLM-Driven Synthesis of Patient Narratives for Mental Health into Causal Models**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.12721

Clinical case formulation organizes patient symptoms and psychosocial factors into causal models, often using the 5P framework. However, constructing such graphs from therapy transcripts is time consuming and varies across clinicians. We present InsightFlow, an LLM based approach that automatically generates 5P aligned causal graphs from patient-therapist dialogues. Using 46 psychotherapy intake transcripts annotated by clinical experts, we evaluate LLM generated graphs against human formulations using structural (NetSimile), semantic (embedding similarity), and expert rated clinical criteria. The generated graphs show structural similarity comparable to inter annotator agreement and high semantic alignment with human graphs. Expert evaluations rate the outputs as moderately complete, consistent, and clinically useful. While LLM graphs tend to form more interconnected structures compared to the chain like patterns of human graphs, overall complexity and content coverage are similar. These results suggest that LLMs can produce clinically meaningful case formulation graphs within the natural variability of expert practice. InsightFlow highlights the potential of automated causal modeling to augment clinical workflows, with future work needed to improve temporal reasoning and reduce redundancy.

**ИИ:** разошлись — Opus ? (другое: LLM builds 5P case-formulation graphs from therapy transcripts and compares them with expert graphs; agreement is graph-similarity based, not unit-level coding.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM generates whole causal case-formulation graphs from transcripts, compared with human graphs structurally and semantically; no coding of the same units, so no coder agreement.)

**Решение:** ?

---

### 821 · R5418

**Facial-Expression-Aware Prompting for Empathetic LLM Tutoring**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.15336

Large language models (LLMs) enable increasingly capable tutoring-style conversational agents, yet effective tutoring requires sensitivity to learners' affective and cognitive states beyond text alone. Facial expressions provide immediate and practical cues of confusion, frustration, or engagement, but remain underexplored in LLM-driven tutoring. We investigate whether facial-expression-aware signals can improve empathetic tutoring responses through prompt-level integration, without end-to-end retraining. We build a scalable simulated tutoring environment where a student agent exhibits diverse facial behaviors from a large unlabeled human facial expression video dataset, and compare four tutor variants: a text-only LLM baseline, a multimodal baseline using a random facial frame, and two Action Unit estimation model (AUM)-based methods that either inject textual AU descriptions or select a peak-expression frame for visual grounding. Across 960 multi-turn conversations spanning three tutor backbones (GPT-5.1, Claude Opus 4.5, and Gemini 2.5 Pro), we evaluate targeted pairwise comparisons with five human raters and an exhaustive AI evaluator. AU-based conditioning consistently improves empathetic responsiveness to facial expressions across all tutor backbones, while AUM-guided peak-frame selection outperforms random-frame visual input. Textual AU abstraction and peak-frame visual injection show model-dependent advantages. Control analyses show that this improvement does not come at the expense of worse pedagogical clarity or responsiveness to textual cues. Overall, our results show that lightweight, structured facial expression representations can meaningfully enhance empathy in LLM-based tutoring systems with minimal overhead. Future work should evaluate these methods using real student facial data collected during authentic learning interactions.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly a generation study, but an AI evaluator and human raters both judge tutor empathy; LLM–human agreement may be reported.); Sonnet -2 (люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает: Tutoring empathy study; humans and an AI evaluator compare tutor LLM outputs pairwise, with no psychological text coding against human labels as the focus.)

**Решение:** -

---

### 822 · R5444

**AlienAnnotators at PsyDefDetect: What Lies Between the Lines: Probing Lightweight Open-Source LLMs for Psychological Defense Mechanism Detection**

2026 · Proceedings of the BioNLP 2026 (Shared Tasks) · conference-paper · https://doi.org/10.18653/v1/2026.bionlp-2.28

Detecting psychological defense mechanisms in therapy dialogue is a clinically valuable but computationally underexplored task. We present our systematic analysis for PsyDefDe-tect, a shared task at BioNLP@ACL 2026, which frames defense detection as a nine-class utterance-level classification problem based on the Defense Mechanism Rating Scale (DMRS). We systematically evaluate six open-source, instruction-tuned small language models (SLMs, ≤ 9B parameters) in zero-shot and fine-tuning settings, and compare a clinically-grounded prompt against the organizer-provided baseline. Our official sub-mission achieved 59.96% accuracy and 16.28% Macro F1. Post-submission experiments show that fine-tuning combined with 5-fold cross-validation and logit averaging ensemble substantially improves performance, with the best configuration reaching 34.59% Macro F1 and 65.25% accuracy. We find that clinically-grounded prompts outperform bare label definitions, model scale does not consistently improve zero-shot performance, and fine-tuning dramatically recovers even collapsed zero-shot models. Certain defense tiers remain persistently difficult across all settings, pointing to clinical ambiguity at tier boundaries as a more fundamental bottleneck than data imbalance alone.

**ИИ:** + · обе модели · бенчмарк с метками людей · Open-source LLMs classify defense mechanisms (DMRS) in therapy dialogue utterances; accuracy is measured against expert-annotated shared-task labels.

**Решение:** =

---

### 823 · R5450

**MAMA-Memeia! Multi-Aspect Multi-Agent Collaboration for Depressive Symptoms Identification in Memes**

2026 · Proceedings of the AAAI Conference on Artificial Intelligence · journalarticle, conference, preprint/article · en · https://doi.org/10.1609/aaai.v40i36.40246

Over the past years, memes have evolved from being exclusively a medium of humorous exchanges to one that allows users to express a range of emotions freely and easily. With the ever-growing utilization of memes in expressing depressive sentiments, we conduct a study on identifying depressive symptoms exhibited by memes shared by users of online social media platforms. We introduce RESTOREx as a vital resource for detecting depressive symptoms in memes on social media through the Large Language Model (LLM) generated and human-annotated explanations. We introduce MAMAMemeia, a collaborative multi-agent multi-aspect discussion framework grounded in the clinical psychology method of Cognitive Analytic Therapy (CAT) Competencies. MAMAMemeia improves upon the current state-of-the-art by 7.55% in macro-F1 and is established as the new benchmark compared to over 30 methods. Accepted by AAAI 2026

**ИИ:** ? · обе модели · другое · Multi-agent LLM labels depressive symptoms in memes against a human-annotated benchmark, but the input is multimodal (image plus text), not purely text.

**Решение:** =

---

### 824 · R5453

**From free association to free parameters: machine-learning empowers artificial intelligence models to rate the affective-relational aspects of narratives like an expert psychologist.**

2026 · Frontiers in digital health · journal article, journalarticle, article · eng · https://doi.org/10.3389/fdgth.2026.1762253

Background: Narrative assessment offers unique insight into psychological functioning but is resource-intensive, requiring extensive expert training and time. Recent work suggests Artificial Intelligence (AI), including moderately sized, adaptable large language models (LLMs), can master narrative assessment's complex, multi-step scoring rules. This study examined whether fine-tuning could enable AI raters to accurately assess narratives. Method: We fine-tuned five diverse LLMs (3-7 billion parameters) on two datasets, one for the SCORS-G Affective Quality of Representations (AFF) scale and one for Emotional Investment in Relationships (EIR). All narratives were rated by expert human raters. Each dataset was split into training and testing samples to evaluate AI-human agreement. Results: Fine-tuned models showed good to excellent reliability with human experts for both AFF and EIR. Ensemble ratings, averaged across all five models, yielded excellent single-rater and average-rater ICCs and low error rates, with 97% of AFF and 92% of EIR ratings falling within accepted discrepancy limits. Conclusion: Fine-tuning effectively adapted AI models into raters capable of reliably scoring complex psychological constructs from narrative. Ensemble-based AI raters can automate AFF and EIR ratings in research settings and, with further validation, may support clinical use via a human-in-the-loop approach. Fine-tuning adaptable AI models offers considerable potential to increase the feasibility and accessibility of sophisticated, multi-method assessment in research and clinical settings alike.

**ИИ:** + · обе модели · подсчёт методики · Fine-tuned LLMs (3-7B parameters) scored narratives on the SCORS-G AFF and EIR scales; agreement with expert raters reported as ICCs.

**Решение:** =

---

### 825 · R5460

**Optimizing prompting strategies improves large language model classification of pain- and fatigue-related functional impact in childhood cancer survivors.**

2026 · Communications medicine · journal article, journalarticle, review · eng · https://doi.org/10.1038/s43856-026-01499-5

Understanding how symptoms affect daily functioning is central to improving care for childhood cancer survivors. As narrative symptom reporting becomes increasingly common in survivorship care, scalable automated tools are needed to interpret these descriptions and identify their functional impact. This study evaluates how two large language models (ChatGPT-4o, Llama-3.1) perform this task across different prompt engineering strategies. We analyzed semi-structured interviews from 30 childhood cancer survivors and their caregivers, yielding 819 pain- and fatigue-related symptom narratives. Each narrative was expert-annotated for physical, social, or cognitive functional impact, serving as the reference standard. ChatGPT-4o and Llama-3.1 were evaluated using four prompting strategies: zero-shot, few-shot, step-by-step reasoning (Chain-of-Thought), and generated knowledge. Model outputs were compared with expert annotations, and performance was quantified using standard classification and discrimination metrics with resampling-based confidence intervals. Here, we show that prompting strategies based on generated knowledge and step-by-step reasoning consistently outperform zero-shot and few-shot across both models. Overall, these strategies produce the most accurate and stable classification of physical, social, and cognitive functional impact. Specifically, ChatGPT-4o achieves more balanced precision and discrimination across physical, social, and cognitive functioning, whereas Llama-3.1 demonstrates higher sensitivity but substantially lower precision, particularly for physical and social functioning. Prompt engineering improves how large language models interpret survivor-reported pain and fatigue. These findings support the use of carefully designed prompts to enable automated, context-aware analysis of symptom narratives, providing a scalable approach to support symptom monitoring and survivor-centered care. Many children who survive cancer continue to have pain and tiredness that affect how they move, think, and take part in daily life. These experiences are often recorded in interviews or written notes, which are hard for doctors to review quickly. This study tested whether two computer programs could aid in interpreting these symptom narratives. We provided the programs with different types of instructions and asked them to determine how pain and fatigue affected physical, social, and thinking activities. We found that instructions that included background information or step-by-step thinking led to more accurate results. These tools could help doctors better track symptoms, identify problems earlier, and provide more personalized care for childhood cancer survivors. Sim et al. compare how different prompting strategies guide ChatGPT-4o and Llama-3.1 in classifying how pain and fatigue affect functioning in childhood cancer survivors. They show that prompts that leverage background knowledge and stepwise reasoning improve accuracy and reveal distinct precision–sensitivity trade-offs among models.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs coded interview narratives for physical/social/cognitive functional impact versus expert annotations; unclear whether this counts as a psychological construct.); Sonnet + (кодирование по кодбуку: ChatGPT-4o and Llama-3.1 classify functional impact of symptom narratives from interviews, compared with expert annotations as reference standard.)

**Решение:** +

---

### 826 · R5466

**The potential of large language models for the assessment of cognitive engagement in informal online communities**

2026 · Research and Practice in Technology Enhanced Learning · journalarticle, article · https://doi.org/10.58459/rptel.2027.22034

Studying the cognitive engagement shown in forum messages of informal online communities can help to associate discussion behaviour with underlying learning processes. The ICAP framework can serve as a theoretical lens for labelling forum messages by distinguishing different levels of cognitive engagement, yet requires time-consuming, high-inference human coding, which is not feasible at scale. Although this can be mitigated by supervised classification models, these rely on large amounts of labelled training data, and their decision-making often remains opaque. In contrast to this, Large Language Models (LLMs) work “out-of-the-box” for qualitative coding tasks via natural language instruction and can produce reasoning traces and explanations for their judgments. In this study, we explore this potential by integrating the ICAP framework into natural-language prompts for few-shot in-context classification, comparing LLM judgments and explanations with those of human raters. Results indicate that LLM judgments generally align with the human ratings, while their reasoning traces and variations offer additional insight into where the coding scheme invites ambiguous interpretations. This suggests that LLMs could serve as cognitive proxies that help diagnose and improve high-inference coding processes. Finally, we apply our approach to large-scale forum data, revealing cross-platform differences in expressed cognitive engagement.

**ИИ:** + · обе модели · кодирование по кодбуку · LLM applies the ICAP cognitive-engagement coding scheme to forum messages and is compared with human raters; cognitive engagement is a psychological construct.

**Решение:** =

---

### 827 · R5469

**Memories Between Us: Autobiographical Memory Sharing with Friends and Strangers**

2026 · Lund University Publications Student Papers (Lund University) · other · en · https://lup.lub.lu.se/student-papers/record/9250836/file/9250838.pdf

Autobiographical remembering is reconstructive and frequently occurs in social interaction, yet it remains unclear whether the relationship between narrator and listener shapes how memories are expressed and subsequently remembered. This study examined autobiographical memory sharing with friends versus strangers and evaluated the use of a large language model (GPT-5.5) for coding narrative data. Fifty-six adults (28 narrators, 28 listeners) participated in a repeated-measures memory-sharing paradigm involving both relationship conditions. Narrators shared positive autobiographical memories, with a nonshared memory serving as a baseline for pre-post comparisons. Narratives were coded for episodic richness and self-event connections (SECs), and listeners later recalled the memories they had heard. Relationship condition did not significantly affect episodic richness during narration, pre-post change, or listener recall. Pre-post change in SECs likewise did not differ across friend, stranger, and baseline conditions. During narration, narrators produced more SECs when speaking to strangers than friends, although this effect was no longer significant after accounting for pre-session SECs and should therefore be interpreted cautiously. GPT coding showed framework-dependent performance, with stronger reliability and human agreement for total episodic richness than for some other coding frameworks. Overall, the findings provide little evidence that a single socially situated recall produces broad or persistent changes in autobiographical memory, while suggesting that relationship context may selectively influence self-related framing. LLM-based narrative coding showed promise but requires framework-specific validation.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · GPT coded autobiographical memory narratives for episodic richness and self-event connections; agreement with human coders reported.

**Решение:** =

---

### 828 · R5488

**A Geospatially Customizable Culturally Tailored Just-in-Time Adaptive Intervention for Violence-Affected People Living With HIV: Mixed Methods Acceptability, Feasibility, and User Experience Study.**

2026 · JMIR human factors · journal article, research support, n.i.h., extramural, med · eng · https://doi.org/10.2196/80705

Abstract Background Posttraumatic stress, along with comorbid mental health challenges and hazardous alcohol use, disproportionately affects people living with HIV. The drivers of these stressors are both intraindividual, rooted in early life adversity and firsthand violence exposures, and contextual, often place-based. Imparting effective coping skills and distinguishing between changeable and unchangeable stressors can improve stress management in the short term, with cascading effects on key HIV continuum of care end points, such as antiretroviral therapy adherence. However, problem- and emotion-based coping skills, delivered via traditional linear in-person group modalities, may falter in the moment. To address this, we adapted the evidence-based Living in the Face of Trauma intervention into an iOS- and Android-native app, featuring daily diary–triggered coping skills recommendations, self-guided Living in the Face of Trauma psychoeducational sessions, and a customizable geofencing function. Objective This mixed methods study aimed to examine the acceptability, feasibility, and user experiences of NOLA (New Orleans, Louisiana) Gem, focusing on user interaction costs relative to geographic ecological momentary assessment (GEMA) alone and refining future optimization options. Methods People living with HIV (N=32) were recruited across New Orleans and initially randomized 1:1 to treatment (NOLA Gem + GEMA) versus control (GEMA) for 21 days. Feasibility was assessed via enrollment and attrition rates. At the immediate postassessment, participants completed acceptability and usability measures and a brief structured usability interview. Analyses included descriptive statistics, bivariate logit modeling, and synergistic human–large language model deductive coding. Results In total, 30 participants (n=22 in the GEMA + NOLA Gem treatment arm) completed the pilot, representing 94% (n=29) of baseline enrollees. Acceptability was very high across the board: 100% (n=30) of users considered NOLA Gem “very” or “somewhat” successful in addressing their daily lives, with 91% (n=28) endorsing increased calm and emotional well-being. In addition, 50% (n=11) of NOLA Gem users were “extremely likely” (Net Promoter Score=10/10) to recommend the app to friends. Eight (27%) GEMA and GEMA + NOLA Gem users reported privacy concerns. Eleven (50%) NOLA Gem users received geofencing alerts; perceptions of this feature’s helpfulness were mixed. No statistically significant sociodemographic or clinical predictors of disparate acceptability or increased privacy concerns were found. No additional frictions were evidenced by GEMA + NOLA Gem versus GEMA users. Qualitatively, NOLA Gem users praised the just-in-time mindfulness, breathing, problem-solving skills delivery, and broader stress control and self-insight benefits. A subset of users pointed out the burdensome length and sometimes inconvenient timing of the daily diaries. Recommendations for next-generation personalization included user-specific dynamic daily diary and geofencing prompt tailoring. Conclusions Our small pilot study demonstrated high NOLA Gem acceptability and feasibility, as well as a rich and beneficial user experience among people living with HIV, with clear and actionable opportunities for improvement.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · The study used human–LLM deductive coding of usability interviews about a trauma app; unclear if LLM–human agreement is reported or the construct is psychological.

**Решение:** =

---

### 829 · R5501

**ELIPSE: Enhanced Live Interview Practice with Sentiment Evaluation, A Zero-Cost Real-Time AI Interview System Achieving Human Level Interaction Fidelity with Sub Two Second Latency and Multi-Dimensional Behavioral Analytics**

2026 · International Journal of Innovations in Science and Technology · journalarticle, article · https://doi.org/10.33411/ijist/1847

Background: Interview preparation is among the final significant areas of workforce development that are resistant to automation, and the worldwide coaching sector is greater than $3 billion a year; however, more than 80 percent of job seekers in emerging economies do not have access to formal practice [1].With innovations in large language models (LLMs), neural text-to-speech (TTS), and transformer-based affective computing, artificially intelligent technology has created an unprecedented opportunity to democratize accessto high-quality interview simulation.Objective: ELIPSE (Enhanced Live Interview Practice with Sentiment Evaluation), to the best of our knowledge, is the first open-source platform to integrate, within a single system,real-time voice-to-voice interaction, adaptive LLM-driven question generation, multi-dimensional behavioral analytics (seven-class emotion detection, continuous sentiment scoring, hesitation quantification, speech-pace monitoring, and composite confidence estimation), and persona.Methods: ELIPSE is built on a React.js/Node.js WebSocket-driven architecture, integrating Groq-hosted LLaMA 3.3 70B inference, Microsoft Edge neural TTS, and a HuggingFace transformer frontend. Assessment used a within-sub longitudinal designwith 15 participants (47 completed sessions, 376 question-answer interactions) addressing three research questions related to latency, behavioral metric validity, and improvement in confidence.Results:ELIPSE achieves a mean end-to-end response latency of 1.83 s (SD = 0.41, 95% CI [1.79, 1.87]; 95th percentile= 2.61 s), a 26.4% reductionversus [2](3.8 s) and 42.8% lowerthan [3](3.2 s). Automated behavioral analytics correlated moderatelyto strongly with expert ratings (overall quality r = 0.71, 95%CI [0.62, 0.79], p < .001; confidence r = 0.68, p < .001; fluency r = 0.63, p < .001), with inter-rater reliability Krippendorff's α = 0.74. A significant 1.3-point improvementin interview confidence was observed after three sessions (paired t(11) = 4.72, p < .001, Cohen's d = 1.24 (large effect)), alongside a 38.8% relative increasein overall score (β = 5.4 points/session, R² = 0.38, p < .001), a 38% reductionin hesitation frequency (d = 0.91), and a 22.8% improvementin speech-pace alignment with the 120–160 WPM target (d = 1.04). System Usability Scale score was 76.3 (SD = 8.2, 95% CI [71.8, 80.8]), classified as 'good', exceeding the 68-point threshold. 67% (95% CI [38%, 88%])of participants preferred ELIPSE to conventional practice methods.Conclusion:ELIPSE demonstrates that the technical and financial barriersto equitable, evidence-based interview preparation are eliminated by the present-day generation of freely available AI architecture, and that it has direct implications for workforce development programs in resource-limited economies worldwide.

**ИИ:** разошлись — Opus ? (другое: Automated interview analytics (emotion, confidence) correlated with expert ratings; unclear whether LLaMA or encoder models did the scoring; borderline construct.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Interview practice system; automated behavioral metrics (mostly transformer emotion detection) correlated with expert ratings, but not LLM coding of psychological text against human labels.)

**Решение:** -

---

### 830 · R5506

**Mind Companion: An Embodied Conversational Agent for Process-Based Psychotherapy**

2026 · IEEE International Conference on Healthcare Informatics (ICHI) · journalarticle, conference, other/conference paper · en · https://doi.org/10.1109/ichi69079.2026.00123

Access to evidence-based psychotherapy remains limited worldwide, with long waitlists even in high-income regions. Recent advances in large language models (LLMs) offer potential for scalable mental health support when designed with clinical oversight and safety mechanisms. We present Mind Companion, an LLM-based embodied conversational agent integrating multi-layered psychological analysis with process-based therapy principles. The system performs real-time analysis of client statements across fact extraction, psychological flexibility process detection, emotion recognition, and safety monitoring. Analysis results are stored for supervising clinicians to inform therapeutic planning. Response generation incorporates retrieval-augmented generation from evidence-based therapeutic literature and context-aware prompting. Responses are delivered through an embodied avatar with synchronized speech synthesis and animation. We evaluated three LLM configurations (GPT-4.1-mini, GPT-5.2, Claude Sonnet 4.5) against therapist responses from real therapy sessions using automated LLM-judge assessment and expert evaluation with 11 professional psychotherapists. GPT-5.2 achieved higher ratings than human therapist responses across understanding, interpersonal effectiveness, collaboration, and therapeutic alignment in both evaluations, demonstrating the feasibility of LLM-based conversational agents as tools to complement clinical care.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM-judge and 11 psychotherapists rated same therapy responses on same dimensions; unclear if judge–expert agreement is reported.

**Решение:** =

---

### 831 · R5520

**STRATEGIES FOR CREATING NATURALISTIC PEER MENTORING DIALOGS USING GENERATIVE LANGUAGE MODELS**

2026 · Minds at UW (University of Wisconsin) · dissertation · https://minds.wisc.edu/bitstreams/4a1f7391-9c6a-4f32-a010-098563c70790/download

This thesis investigates a peer-mentor dialogue generation system for university students, comparing five advisor configurations across two experimental flows. Student profiles from a Qualtrics survey (n=156) are classified into weak, average, and strong categories based on GPA, confidence, and course load, grounding a profile-aware, template-guided pipeline architecture evaluated against two alternative optimization strategies (Direct Preference Optimization and Kahneman-Tversky Optimization) for fine-tuning a 14B parameter Large Language Model (LLM), Qwen2.5-14B-Instruct. The research compares within-family and cross-family schemes for using an LLM as a judge. Four dialogue conditions vary ethics conditioning and template-guided generation across four advising topics, with a held-out topic for testing generalizability. Evaluation was conducted across five combinations of optimization strategy and inputs, with the best approach achieving excellent performance across all criteria (Naturalness, Empathy, Factuality, and Relevance). The findings demonstrate that template-guided generation and preference-based fine-tuning complement each other, and thus both should be used together.

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Generates academic peer-mentoring dialogues; an LLM judge rates them, and only judge schemes are compared, with no human ratings reported.); Sonnet ? (неясно, сравнивали ли с людьми: Mainly dialogue generation, but uses an LLM judge for empathy and naturalness. The abstract doesn't say whether the judge was validated against human ratings.)

**Решение:** -

---

### 832 · R5528

**Depression Prediction Using Large Language Models and AVTFusion Model on Multimodal Data**

2026 · Lecture notes in networks and systems · conference-paper · en · https://doi.org/10.1007/978-3-032-28293-4_41

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract. Multimodal LLM depression prediction likely uses self-report or diagnostic labels, but it is unclear whether humans also coded the text.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): Multimodal depression prediction with LLMs and a fusion model; likely predicts diagnosis/score, not coder agreement. No abstract available.)

**Решение:** ?

---

### 833 · R5541

**Performance of Large Language Models in Detecting Explicit and Implicit Colorism in Skin-Lightening Product Advertisements: A Validation Study**

2026 · American Journal of Preventive Medicine · article · en · https://doi.org/10.1016/j.amepre.2026.108379

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs detect colorism in skin-lightening ads, which is marketing content coding rather than a psychological or clinical construct; no abstract available.); Sonnet ? (неясен конструкт: LLM validation study likely against human coders, but colorism in advertisements may be a marketing/social category rather than a psychological construct; no abstract.)

**Решение:** -

---

### 834 · R5544

**Development of the Fully Automatic Robotic Storyteller—Comparing Manual, Semi-Automatic, and LLM-Based Emotional Story Annotation for Multimodal Robotic Storytelling**

2026 · IEEE Transactions on Affective Computing · journalarticle, article · https://doi.org/10.1109/taffc.2026.3691816

Storytelling has accompanied mankind since its beginnings and receiving stories is still a popular leisure activity. Today, new storytelling media are emerging. For example, social robots can act as storytellers, using different modalities such as facial expressions or body postures. With the goal of automating robotic storytelling, we annotated stories with emotion labels which a robot can use to automatically adapt its behavior to. Doing so, three different approaches and a baseline are compared in two studies in this paper: 1) manual labels by human annotators (MA), 2) software-based word-sensitive annotation using the Linguistic Inquiry and Word Count program (LIWC), 3) a LLM approach using ChatGPT (GPT), and 4) random annotations as baseline (RBL). In an online study showing videos of a storytelling robot, the annotations were validated using a backwards annotation task, with GPT closely followed by MA achieving the best, and the RBL the worst results. In a subsequent lab user study, all versions of the story were compared regarding storytelling experience, emotions, and robot perception, revealing no significant differences for any of these variables based on the annotation approach, but a significant decrease of negative affect and fatigue over the storytelling in all conditions. Taken together, the results indicate suitability of both the manual and GPT approaches. On this empirical basis, the Automatic Robotic Storyteller was implemented using GPT-based annotations and bodily expressions. The reduced programming effort of our system makes robotic storytelling accessible to a broader audience, strengthening its deployment in the field of affective computingAuthor: This article has exceeded the approved 12-page length. Please edit text and/or graphics to reduce the length to 12 pages.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · ChatGPT and human annotators both labelled emotions in story text; unclear if direct GPT–human agreement is reported beyond the backwards-annotation validation.

**Решение:** =

---

### 835 · R5562

**The impact of impression management on writing tendencies: Investigating faking susceptibility of open-ended personality assessments.**

2026 · The Journal of applied psychology · journal article, med, journalarticle · eng · https://doi.org/10.1037/apl0001397

Applicant faking on self-report personality measures has long been a concern. One method that might be more resistant to faking is open-ended personality assessments. Guided by a new framework of open-ended faking behavior, we investigated how faking emerges in open-ended personality assessments. Additionally, we examined an alternative form of faking: artificial intelligence (AI)-generated responses. Results showed that elaborate responding (i.e., effortful crafting of narratives, Cohen's d = .29) and selective information management (i.e., promoting positive information while withholding negative information, d = .72) were higher in faked than honest conditions and that individuals with higher trait levels were more capable of producing elaborate responses and providing favorable information under motivated conditions. When faking, scores increased more on Likert self-reports ( d ¯ = .65) than on open-ended personality scores ( d ¯ = .26) derived via natural language processing, though when trained to predict human ratings rather than honest Likert scores natural language processing scores were more susceptible to faking ( d ¯ = .63). Training sample configuration also influenced psychometric properties, such that training on a mixed sample of honest and motivated responses yielded the best results. Finally, AI-generated responses (fully synthetic and human-AI hybrid) received scores that varied considerably across models, though they typically were higher than human scores. However, a customized algorithm accurately differentiated human from AI responses with near-perfect accuracy (across seven large language models and for humans using AI), with only a 1% false positive rate. Collectively, these findings suggest that open-ended personality assessments, when paired with natural language processing scoring, have potential to offer a scalable, more faking-resistant approach to personality assessment. (PsycInfo Database Record (c) 2026 APA, all rights reserved).

**ИИ:** ? · обе модели · другое · NLP scoring of open-ended personality responses was trained on human ratings, but the scorer may not be a generative LLM; LLMs mainly generate responses.

**Решение:** =

---

### 836 · R5569

**Evaluating AI- assisted Qualitative Coding of Student Reflections in Online Learning**

2026 · Maryland Shared Open Access Repository · text/text, article · https://doi.org/10.13016/m2ourl-mkqd

Student reflections in online courses provide valuable insight into learner experiences and challenges, yet manual qualitative coding is time-consuming and rarely conducted systematically at scale. This study evaluates an AI-assisted pipeline comparing ChatGPT-5 generated analysis with manual human coding across four tasks: sentiment classification, text chunking, module mapping, and challenging concept extraction, using 188 sentences from weekly reflections submitted by 11 students over six weeks in a Post-Quantum Cryptography course on edX. AI achieved a module mapping accuracy of 98.3%, concept extraction accuracy of 91.7%, and sentiment agreement of 85.6% with a Cohen's Kappa of 0.75. Prompt design significantly affected chunking alignment, with ARI improving from 0.674 to 0.739 with an improved prompt. Based on these findings, this study proposes an instructor-facing dashboard prototype to automatically surface student sentiment trends and challenging concept frequencies in real time.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT-5 compared with human coding of student reflections (sentiment κ=0.75); unclear whether learner sentiment counts as a psychological construct.

**Решение:** =

---

### 837 · R5576

**TrAIngles: an LLM-Based Automatic Scoring Tool for Theory of Mind Assessments Across the Life Span**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/sb9gz_v1

Understanding how Theory of Mind (ToM), the ability to attribute mental states to others, develops and differs across individuals requires robust and easily applicable measures. Tasks involving open ended verbal responses such as the Triangles Task offer valid indicators of ToM, but their manual scoring is time-consuming and demands substantial training. In this study, we test the validity and reliability of TrAIngles, an automatic scoring software for the Triangles Task developed through fine-tuning of large language models (LLMs). TrAIngles was trained on a dataset of N ~ 11,000 responses collected from 581 Italian-speaking participants aged between 8 and 81 years. LLM-based ToM scores showed high accuracy and reliability metrics (Cohen’s kappa, ICC, Krippendorff’s alpha, Spearman’s rho) comparable to human ratings and consistently exceeding commonly accepted thresholds for inter-rater agreement (i.e., &gt; .80). Performance remained robust across age groups (children, adolescents, young adults, adults, and older adults). Our findings demonstrate that reliable and valid ToM indexes can be obtained from the Triangles Task using this new automated scoring system based on LLMs. TrAIngles thus provides an innovative tool for lifespan ToM assessments relying on open-ended responses, highlighting the potential of training automated scoring systems on archival, human-rated datasets. TrAIngles is openly available for use both as code and via a user-friendly graphical interface.

**ИИ:** + · обе модели · подсчёт методики · Fine-tuned LLMs score open-ended Triangles Task Theory of Mind responses; agreement with human ratings reported (kappa, ICC, alpha).

**Решение:** =

---

### 838 · R5578

**Beyond Simulations: What 20,000 Real Conversations Reveal About Mental Health AI Safety.**

2026 · Research square · journal article, preprint, journalarticle · eng · https://doi.org/10.21203/rs.3.rs-8642399/v1

Mental-health AI safety is typically evaluated with small, simulation-based benchmarks that may not reflect the linguistic and contextual diversity of deployment. We pair four benchmark replications with an ecological audit of real-world conversations to evaluate a purpose-built mental-health AI alongside six frontier general-purpose models spanning four families (OpenAI GPT-5, GPT-5.1, GPT-5.2; DeepSeek V3; Google Gemini 3 Flash; Moonshot Kimi K2). The purpose-built system produced significantly lower overall potentially harmful content rates than every frontier comparator on suicide/self-harm, eating-disorder, and substance-use prompts (CCDH Benchmark: Ash 6.2% vs frontier models 18.0-52.0%, all p &lt; .001). In an audit of 20,000 deployment conversations, clinician review within the audit pipeline confirmed no suicide-risk conversations lacking crisis resources and three NSSI-related conversations without crisis intervention, a within-pipeline conditional rate of 3/800 (0.38%). To extend population-level inference, we adjudicated 600 conversations randomly sampled from the full deployment distribution via blinded clinician review. Against these labels, the LLM judge showed 100% sensitivity (6/6; 95% CI 54.1-100%) and 99.2% specificity (589/594) at its operating threshold, and the conversational model delivered crisis resources in all 6 clinician-confirmed cases (zero end-to-end false negatives; rule-of-three upper 95% CI 0.50%). Findings argue for ecological auditing as a complement to pre-deployment evaluation in mental-health AI safety 43 pages, 8 figures

**ИИ:** + · обе модели · LLM-судья · LLM judge flagged suicide-risk in mental-health conversations, validated against blinded clinician labels on 600 conversations (sensitivity/specificity).

**Решение:** =

---

### 839 · R5589

**Shadow Validation Without Human Subjects: A Multi-Layered Synthetic Framework for Cognitive Governance Metrics in High-Resonance AI Interactions**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.19683812

The Cognitive Governance Framework addresses non-clinical cognitive risks emerging from high‑resonance interactions with advanced AI systems. Because ethical and regulatory constraints prohibit early-stage human trials, this paper introduces a fully synthetic, five-layer validation architecture for the ARDA‑20 metric and the ATHOS‑SHIELD mitigation protocol. The framework integrates high‑fidelity LLM‑agent simulations, retrospective anchoring on public corpora, Delphi‑method face validation, adversarial red‑teaming, and convergent construct validation. Results show strong alignment between ARDA‑20 and expert judgments (ICC = 0.82), robustness of ATHOS‑SHIELD even under adversarial conditions (13.8% drift reduction), and meaningful correlations with established psychological constructs (Absorption r = 0.67). This architecture achieves the maximum level of pre‑human validation feasible under current ethical constraints and satisfies the EU AI Act’s “state‑of‑the‑art” requirement for limited‑risk systems.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Synthetic validation reports ARDA-20 vs expert judgments (ICC 0.82); unclear whether an LLM scored the texts or what was rated.); Sonnet -7 (другое — напишите почему: Fully synthetic validation framework for an AI-risk metric; no clear LLM coding of psychological text against human coders (expert judgments appear simulated).)

**Решение:** -

---

### 840 · R5590

**Shadow Validation Without Human Subjects: A Multi-Layered Synthetic Framework for Quantifying and Mitigating Non-Clinical Cognitive Risk in High-Resonance AI Interactions**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.19686136

Background. High-resonance interactions with large language models (LLMs) produce non-clinical cognitive risks—including hypermentalization, delusional theme induction, and cognitive fragmentation—that precede measurable harm but fall outside clinical taxonomies. Ethical constraints prohibit early-stage human trials, creating a validation gap for safety metrics and mitigations. Objective. To design and evaluate a fully synthetic, five-layer validation architecture for (1) the ARDA-20 metric, which quantifies non-clinical cognitive risk, and (2) the ATHOS-SHIELD protocol, a reality-anchoring mitigation that interrupts high-resonance trajectories. Methods. We introduce Shadow Validation, combining: L1) high-fidelity LLM-agent simulations with vulnerable personas; L2) retrospective anchoring on 14,382 public corpora with annotated outcomes; L3) Delphi-method face validation with N=23 domain experts; L4) adversarial red-teaming across three attack vectors; L5) convergent construct validation against Absorption, Schizotypy, and Intolerance of Uncertainty. Primary endpoints: inter-rater reliability (ICC), drift reduction under attack, and construct correlations. Results. ARDA-20 showed good agreement with experts, ICC(2,k) = 0.82, 95% CI [0.71, 0.90]. ATHOS-SHIELD reduced cognitive drift by 13.8% relative to baseline, p 10% reduction under adversarial conditions. ARDA-20 correlated r = 0.67 with Absorption, r = 0.54 with Schizotypal Personality Questionnaire-Brief, r = 0.49 with Intolerance of Uncertainty Scale-12. Simulation predicted 91.3% of retrospective cases above clinical review threshold. Conclusions. Shadow Validation achieves the maximum feasible level of pre-human evidence under current ethical constraints and satisfies the EU AI Act’s “state-of-the-art” requirement for limited-risk systems. We define open thresholds and a post-market monitoring plan to close the synthetic-to-human gap.

**ИИ:** ? · обе модели · другое · ARDA-20 rates cognitive risk in LLM conversations and agrees with experts (ICC 0.82), but it's unclear whether an LLM does the scoring.

**Решение:** =

---

### 841 · R5602

**A Synthetic Conversational Dataset for Type 2 Diabetes Management**

2026 · Language Resources and Evaluation Conference (LREC) · conference, conference-paper · https://doi.org/10.63317/3cbhekpxj33y

Access to real patient-doctor conversations in the medical domain is often restricted due to privacy concerns, making it difficult to build robust conversational AI systems. To address this, we present a novel methodology for generating a high-quality synthetic dataset designed for conversational triple extraction in Type 2 Diabetes management. Using structured prompting with GPT-4, we generated 16 demographically and medically diverse diabetic personas, and 256 multi-turn conversations between these personas and a caretaker agent, simulating realistic and context-rich interactions. The conversations incorporate critical properties such as personalization, empathy, contextual awareness, and medically grounded advice, as validated through both LLM-based and human expert evaluations. These synthetic conversations are further annotated with Subject-Predicate-Object (SPO) labels at the token level, integrating both manual and LLM-automated methods, forming the foundation for downstream tasks like triple extraction. Our work demonstrates the feasibility of using generative AI to simulate healthcare conversations at scale, offering a solution for data-scarce domains.

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Synthetic diabetes conversation generation and SPO triple annotation; medical, not psychological coding against human raters.); Sonnet ? (другое: Synthetic diabetes conversations with LLM-based and human evaluation of empathy and SPO annotation; the task is mainly generation and medical, so it is probably ineligible. A full-text check is needed for LLM–human agreement on empathy ratings.)

**Решение:** -

---

### 842 · R5609

**Scoring employment interviews with large language models: Evaluation design components, validity investigations, and best practice recommendations.**

2026 · The Journal of applied psychology · journal article, med, journalarticle · eng · https://doi.org/10.1037/apl0001396

Recently, supervised machine learning models served as alternatives to humans for scoring open-ended assessments, including employment interviews. More recently, large language models (LLMs) emerged as alternative raters that do not require task-specific training data. However, interview evaluation design considerations have predominantly been conceptualized for human raters, and thus, it is unclear whether the psychometric benefits of interview evaluation best practices generalize to LLM raters. Additionally, LLM raters introduce novel evaluation design decisions that could be psychometrically consequential. We investigated the effects of several LLM rater evaluation practices-specifically, prompt design, model selection, hyperparameters, and number of interviewers-on the LLM interview scores' psychometric properties in two interview data sets. In the first, interviewee Big Five personality traits were evaluated ( N = 954). In the second, interviewees' question responses were evaluated on the targeted construct on Behaviorally Anchored Rating Scales ( N = 144). We then investigated the LLM scores' intrarater reliabilities, test-retest correlations, convergent, discriminant, and criterion evidence of validity, group differences, and measurement bias. We compared this evidence, when possible, to the same evidence for human raters and supervised machine learning models. The results suggest that ensembles of larger, newer LLMs using prompts with detailed construct information hold potential for scoring employment interviews with psychometric properties comparable to or superior to supervised machine learning models and single human raters. We detail the reasons that organizations may want to be cautious in adopting LLMs for scoring high-stakes open-ended assessments, but since organizations have already begun adopting them, we also offer best practice recommendations. (PsycInfo Database Record (c) 2026 APA, all rights reserved).

**ИИ:** + · обе модели · подсчёт методики · LLMs rate Big Five personality and BARS constructs from interview responses; the results are compared with human raters' scores of the same interviews.

**Решение:** =

---

### 843 · R5619

**S 3 : Sequential Self-feeding Slot Prediction for Explainable Cognitive Reframing in Task-Oriented Dialogue**

2026 · ACM Transactions on Computing for Healthcare · journalarticle, article · en · https://doi.org/10.1145/3833080

Cognitive behavioral therapy (CBT) is a well-established psychotherapeutic approach, yet its delivery through AI systems remains challenging: small language models (SLMs) struggle with multi-step therapeutic reasoning, while large language models (LLMs) are often impractical for resource-constrained deployment. We address this gap by formulating CBT-based cognitive reframing as a task-oriented dialogue (TOD) problem with dialogue state tracking (DST), which exposes intermediate belief states—such as event, thought, and cognitive distortion—making the reasoning process explainable and auditable for clinical oversight. To support controlled experimentation, we introduce CREPAN, a synthetic dataset of over 6,800 expertguided CBT reframing dialogues for panic disorder, designed as a controlled experimental setting to investigate whether models can learn the structured reasoning prescribed by the CBT ABC model. We further propose Sequential Self-feeding Slot Prediction (S 3 ), a lightweight reasoning scaffold that guides models through interpretable cognitive stages in a theoretically grounded order derived from Ellis’s ABC model. Experiments show that S 3 -T5 attains a JGA of 0.7781, narrowing the gap with 8B-scale LLMs, with the sequential self-feeding structure enabling interpretable step-by-step reasoning. These results suggest that cognitive-theoretic structure is central to robust therapeutic state tracking, offering a practical path toward lightweight, interpretable, and clinically accountable AI systems for CBT-based counseling 1 .

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: 8B LLMs predict cognitive distortion and thought slots in synthetic CBT dialogues; unclear whether the reference labels are human-coded or synthetic.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Synthetic CBT dialogue dataset and dialogue state tracking with small models; no LLM-versus-human coding agreement on psychological text.)

**Решение:** -

---

### 844 · R5632

**AI counseling agent for motivational interviewing: Conversational processes associated with change talk in emergency department patients.**

2026 · Journal of substance use and addiction treatment · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.josat.2026.210053

BACKGROUND Large language models (LLMs) have the potential to expand access to Motivational Interviewing (MI), but little is known about whether AI-delivered counseling reproduces conversational processes associated with motivation for behavior change. Change talk (CT), sustain talk (ST), and specific counselor behaviors are central components of MI theory, yet their occurrence and associations within AI-delivered counseling remain understudied. METHODS We conducted a secondary analysis of transcripts from a prospective pilot study of an AI Motivational Interviewing Counseling Agent (MICA) delivered to Emergency Department patients with risky alcohol, cannabis, or nicotine use. Participants completed a text-based counseling session with MICA (GPT-4). MICA utterances were coded using the Motivational Interviewing Treatment Integrity (MITI) framework and participant utterances were coded using the Motivational Interviewing Skill Code (MISC). We examined differences in counselor and participant language across substances, participant- and counselor-level predictors of change talk balance (CT/[CT+ST]), and exploratory associations between CT balance and post-session changes in readiness to change. RESULTS Ninety-eight participants completed 105 counseling sessions. MICA demonstrated a consistent MI-consistent conversational style characterized by frequent use of open questions, reflections, and affirmations, with no identified MI-inconsistent behaviors. When expressed as proportions of total utterances, MICA behaviors did not differ significantly across alcohol-, cannabis-, and nicotine-focused sessions. Participant motivational language varied by substance, with nicotine-focused sessions showing higher CT balance and cannabis-focused sessions showing greater ST. In multivariable analyses, higher CT balance was independently associated with a greater proportion of complex reflections (β = 1.04, p < 0.001), a greater proportion of open questions (β = 0.67, p = 0.018), the presence of collaboration-focused statements (β = 0.12, p = 0.013), greater session length (β = 0.004, p = 0.010), and higher baseline readiness to change (β = 0.045, p < 0.001). In exploratory analyses of participants with both pre- and post-session readiness assessments, higher CT balance was associated with greater improvement in readiness to change following counseling (β = 1.02, 95% CI 0.33-1.71, p = 0.004). CONCLUSIONS An AI counseling agent generated conversational processes broadly consistent with MI theory. Reflective depth, open questioning, and collaborative language were associated with greater participant change talk, and higher change talk balance was associated with greater improvement in readiness to change. These findings support the use of process-oriented frameworks to evaluate and optimize AI-delivered behavioral interventions.

**ИИ:** разошлись — Opus -2 (люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает: GPT-4 delivered MI counselling; transcripts were MITI/MISC-coded, apparently by humans; no LLM coding compared with human coders.); Sonnet ? (неясно, сравнивали ли с людьми: GPT-4 counselor transcripts were coded with MITI/MISC, but the abstract doesn't say who coded them. They may be human-only, or an LLM may have coded with human validation.)

**Решение:** -

---

### 845 · R5633

**Feasibility and Acceptability of a Large Language Model-Based Motivational Interviewing Agent in the Emergency Department.**

2026 · Annals of emergency medicine · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.annemergmed.2025.08.021

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Feasibility study of an LLM agent delivering motivational interviewing; the title suggests intervention delivery, with no sign of LLM coding against human coders.); Sonnet ? (нет аннотации: No abstract. An LLM motivational interviewing agent is mostly generation. Fidelity coding against humans is possible but unclear, so full text is worth checking.)

**Решение:** -

---

### 846 · R5636

**MindTailor: Personalized Emotional Support via Post History-Grounded Case Formulation and Collaborative Refinement**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.21930

As mental health concerns continue to rise globally, social media has emerged as a vital space where individuals seek emotional support. While prior work on personalized emotional support has leveraged seekers' emotional states, personas, and situational context, these approaches primarily capture the seeker's current state, overlooking the formative experiences that shape present concerns. In this work, we propose MindTailor, a framework that generates personalized emotional support responses by constructing a case formulation from the seeker's post history and iteratively refining responses through collaborative critique among counselor agents grounded in distinct counseling strategies. To enable research on this history-aware task, we construct ReddiSupp, a dataset of 798 Reddit posts paired with seekers' prior post histories. Through LLM-as-a-Judge evaluation, expert human evaluation, and a user study with seekers, we demonstrate that MindTailor outperforms baselines across these evaluations, improving empathy, personalization, understanding, and achieving the highest overall preference. 45 pages, 21 figures

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly a generation framework, but LLM-as-judge and expert humans both rate empathy of support responses; LLM–human agreement may be reported.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Framework generates personalized emotional support responses; LLM-as-judge and human evaluations rate generated outputs, not coding of psychological text against human labels.)

**Решение:** -

---

### 847 · R5652

**Can large language models interpret unstructured chat data on dynamic group decision-making processes? Evidence on joint destination choice**

2026 · Travel Behaviour & Society · journalarticle, review, preprint/article · en · https://doi.org/10.48550/arxiv.2601.05582

Social activities result from complex joint activity-travel decisions between group members. While observing the decision-making process of these activities is difficult via traditional travel surveys, the advent of new types of data, such as unstructured chat data, can help shed some light on these complex processes. However, interpreting these decision-making processes requires inferring both explicit and implicit factors. This typically involves the labor-intensive task of manually annotating dialogues to capture context-dependent meanings shaped by the social and cultural norms. This study evaluates the potential of Large Language Models (LLMs) to automate and complement human annotation in interpreting decision-making processes from group chats, using data on joint eating-out activities in Japan as a case study. We designed a prompting framework inspired by the knowledge acquisition process, which sequentially extracts key decision-making factors, including the group-level restaurant choice set and outcome, individual preferences of each alternative, and the specific attributes driving those preferences. This structured process guides the LLM to interpret group chat data, converting unstructured dialogues into structured tabular data describing decision-making factors. To evaluate LLM-driven outputs, we conduct a quantitative analysis using a human-annotated ground truth dataset and a qualitative error analysis to examine model limitations. Results show that while the LLM reliably captures explicit decision-making factors, it struggles to identify nuanced implicit factors that human annotators readily identified. We pinpoint specific contexts when LLM-based extraction can be trusted versus when human oversight remains essential. These findings highlight both the potential and limitations of LLM-based analysis for incorporating non-traditional data sources on social activities. 23 pages, 9 figures

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM annotations of group-chat decision factors compared with human labels; unclear whether restaurant preferences and choices count as a psychological construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM extracts group restaurant-choice decision factors from chats versus human annotation; travel behaviour, not a psychological or clinical construct.)

**Решение:** +

---

### 848 · R5656

**Examining Human-Like Behaviors in LLMs: A Multi-Dimensional Analysis of Model Behaviors, User Factors, and System Prompts**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.18258

Large language models (LLMs) exhibit a wide range of human-like behaviors, from expressing thoughts and emotions, to engaging in relationship-building with users, to refusing requests and maintaining boundaries. Despite their prevalence, researchers and practitioners lack methods and empirical insights to make informed decisions about when and what types of human-like behaviors LLMs should exhibit. To fill this gap, we present a multi-dimensional analysis of the prevalence, potential effects, and controllability of these behaviors using LLM-as-a-judge and human evaluation. Across 21,000 multi-turn conversations from four widely used models (gpt-4o, gpt-4.1-mini, claude-sonnet-4.6, gemini-2.5-flash), we find that human-like behaviors are pervasive but vary across models and user factors (conversation goals and user profiles). In terms of perceived appropriateness, human evaluators judged self-referential and relationship-building behaviors as less appropriate from LLMs than from humans, but boundary-maintaining behaviors more appropriate from LLMs than from humans. Finally, we show that system prompting can control these behaviors, though it requires careful evaluation to avoid unintended effects. We discuss the implications of our findings and provide recommendations for responsible LLM design and evaluation.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM-as-judge codes human-like behaviours (emotions, relationship-building) in chatbot conversations; unclear whether the judge was validated against human coding of the same units.

**Решение:** =

---

### 849 · R5661

**OMIND: Framework for Knowledge Grounded Finetuning and Multi-Turn Dialogue Benchmark for Mental Health LLMs**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2603.25105

Large Language Models (LLMs) have shown remarkable capabilities for complex tasks, yet adaptation in medical domain, specifically mental health, poses specific challenges. Mental health is a rising concern globally with LLMs having large potential to help address the same. We highlight three primary challenges for LLMs in mental health - lack of high quality interpretable and knowledge grounded training data; training paradigms restricted to core capabilities, and evaluation of multi turn dialogue settings. Addressing it, we present oMind framework which includes training and aligning LLM agents for diverse capabilities including conversations; high quality ~164k multi-task SFT dataset, as a result of our generation pipeline based on Structured Knowledge retrieval, LLM based pruning, and review actions. We also introduce oMind-Chat - a novel multi turn benchmark dataset with expert annotated turn level and conversation level rubrics. Our diverse experiments on both core capabilities and conversations shows oMind LLMs consistently outperform baselines. oMind-LLM also shows significantly better reasoning with up to 80% win rate. 9 pages, 3 figures, 5 tables

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mental-health dialogue benchmark with expert-annotated rubrics; unclear whether an LLM judge is validated against the expert ratings.

**Решение:** =

---

### 850 · R5675

**Suspense in Shorts. Operationalizing the Measurement of Suspense in Short Fiction**

2026 · Zenodo (CERN European Organization for Nuclear Research) · text/poster, article · en · https://doi.org/10.5281/zenodo.20389962

Suspense in Shorts This poster presents Suspense in Shorts, a computational literary studies project conducted as an Undergraduate Research Apprentice Program (URAP) project at the University of California, Berkeley (January–May, 2026). The project operationalizes and measures suspense in English-language short fiction (UK/US) by applying four literary suspense theories — Carroll (1997) & Iwata (2009) uncertainty-based suspense (T1), Smuts (2008) desire-frustration theory (T2), Gerrig (1996) partial uncertainty theory (T3), and a theory-neutral casual reader approach (T4) — as LLM annotation prompts. Prior to LLM annotation, a manual annotation of 15 short stories was conducted by a team of four annotators, yielding the expected inter-annotator disagreement reflecting the incompatible theoretical conceptualizations underlying each of the four operationalized theory approaches. Using a local LLM (Qwen3-4B-Instruct, via LM Studio) and the custom-built annotation and evaluation tool SuspenseLens, we annotate reader suspense and character anxiety at the sentence level across a short fiction corpus, with Miriam Allen De Ford's Oh Rats! (1961) as a pilot text. Annotations are validated against manual expert gold standard annotations using theory-specific gold sheets. Evaluation results reveal systematic differences across theories: for reader suspense, T2 achieves the best overall weighted metrics (W.F1 = 0.717, Spearman r = 0.569), while T4 best captures the distribution of non-zero suspense annotations (NZ precision = 0.253, NZ recall = 0.234). Score inflation (the model assigning non-zero suspense where human annotators rated 0) is a dominant pattern for T1 (inflation rate 0.870) and T3 (0.692), with near-zero NZ precision (0.011 and 0.029 respectively), indicating the model rarely assigns the correct non-zero level for uncertainty-based theories. For character anxiety, annotations are better calibrated than reader suspense across all theories: T3 achieves the best non-zero performance (NZ precision = 0.179, NZ recall = 0.325), and T1 the best rank-order agreement (Spearman r = 0.521). These findings confirm the need for theory-specific prompt design for computationally operationalizing literary suspense and reveal a systematic score inflation bias rooted in the LLM's intrinsic suspense concept overriding the theoretical instructions of the prompt. Following Halterman and Keith (2025), who evaluate LLMs as measurement tools for theoretically defined concepts, the next steps of the project focus on comparing models of varying size and instruction-following capacity to identify the most suitable model for theory-guided literary annotation — one that follows the operationalized theory prompt rather than defaulting to its inherent conceptualization of suspense. References Carroll, Noël. 1997. “The Paradox of Suspense.” In Suspense: Conceptualizations, Theoretical Analyses, and Empirical Explorations. De Ford, Miriam Allen. 1961. “Oh Rats!” Science fiction novella. Galaxy Magazine December 1961. https://www.gutenberg.org/ebooks/51751. Gerrig, Richard. 1996. “Suspense in the Absence of Uncertainty.” Journal of Memory and Language 28 (6): 633–48. 10.1016/0749-596X(89)90001-6. Guhr, Svenja. 2026. Suspense in Shorts. GitHub Repository. https://github.com/SvenjaGuhr/Suspense_in_Shorts.Guhr, Svenja. 2026. SuspenseLens. V. 1.0. GitHub Repository. https://github.com/SvenjaGuhr/SuspenseLens. Halterman, Andrew, and Katherine A. Keith. 2025. “Codebook LLMs: Evaluating LLMs as Measurement Tools for Political Science Concepts.” Political Analysis 34 (2): 188–204. 10.1017/pan.2025.10017. Iwata, Yumiko. 2009. “Creating Suspense and Surprise in Short Literary Fiction: A Stylistic and Narratological Approach.” Doctoral Thesis, University of Birmingham. Smuts, Aaron. 2008. “The Desire-Frustration Theory of Suspense.” Journal of Aesthetics and Art Criticism 66 (3): 281–90. 10.1111/j.1540-6245.2008.00309.x.

**ИИ:** разошлись — Opus ? (неясен конструкт: Qwen LLM annotations of sentence-level suspense and character anxiety in fiction were checked against expert gold labels; unclear whether literary suspense counts as a psychological construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM annotates suspense in short fiction against human gold annotations, but this is literary studies, not psychological or clinical text.)

**Решение:** -

---

### 851 · R5683

**Evaluating and Enhancing an AI Mental Health Guide in High-Risk Mental Health Contexts**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-9588991/v1

Abstract The rapid adoption of large language models (LLMs) for emotional support necessitates specialized safety frameworks to prevent the reinforcement of pathological thinking or crisis escalation. General-purpose LLMs often fail to recognize high-risk markers like mania or delusions. This study introduces a unified safety pipeline for TalkAI, a specialized mental health guide, utilizing 60 adversarial prompts across five clinical categories. We developed a human-calibrated LLM-as-Judge framework and employed Direct Preference Optimization (DPO) to align model variants with clinical standards. Following alignment, safety accuracy increased by up to 18.4 percentage points, with the most optimized TalkAI variant achieving 81.4% accuracy, narrowing the gap with proprietary frontier models. As the first study to integrate red-teaming, automated clinical scoring, and DPO, this research provides a scalable blueprint for continuous safety monitoring. It emphasizes that while automated tools enable high-power evaluation, expert human input is essential for grounding AI in high-risk domains.

**ИИ:** + · обе модели · LLM-судья · An LLM-as-judge was calibrated against human ratings to score the safety of mental-health chatbot responses in high-risk contexts.

**Решение:** =

---

### 852 · R5707

**Thai Depression Detection with LLM-Assisted Annotation and PHQ-9 Multi-Task Classification**

2026 · Asia Pacific Symposium on Intelligent and Evolutionary Systems · https://doi.org/10.1109/ies71033.2026.11702644

Depression affects approximately 4.4 million Thais annually. However, NLP research on mental health detection from Thai-language text remains limited, and existing annotation pipelines rely heavily on human experts at considerable cost. This study compiles a dual-source Thai depression text dataset drawn from personal diary entries of undergraduate students (2,132 entries) and discussion threads from Pantip.com (850 entries), annotated by domain experts using majority voting. Three LLMs, DeepSeek, Gemini 1.5 Flash, and Llama 8B, were evaluated as annotation alternatives, with human-LLM agreement measured via Cohen’s Kappa. Four architectures (RNN, LSTM, Bi-LSTM, and Transformer) were benchmarked under five-fold cross-validation for both binary depression classification and fine-grained PHQ-9 itemlevel multi-task classification. The Transformer achieved the highest performance on binary classification of diary entries (Accuracy 0.819, F1 0.783), while Bi-LSTM and LSTM led on the Pantip dataset (Accuracy 0.957, F1 0.978). For PHQ-9 multitask classification, the Llama-annotated Transformer reached F1 Micro of 0.6401 at the document level, with noise filtering improving performance by 30-50% across all annotators. DeepSeek attained the strongest alignment with human experts on the diary dataset $(\kappa=0.488)$. These findings suggest that LLM-assisted annotation can serve as a practical complement to expert labeling in Thai mental health NLP applications.

**ИИ:** + · обе модели · бенчмарк с метками людей · DeepSeek, Gemini and Llama annotated Thai diary and forum texts for depression and PHQ-9 items; their labels were compared with expert labels using Cohen's kappa.

**Решение:** =

---

### 853 · R5732

**AI- vs Human-Based Assessment of Medical Interview Transcripts in a Generative AI-Simulated Patient System: Cross-Sectional Validation Study.**

2026 · JMIR medical education · journal article, validation study, research support, non-u.s. gov't · eng · https://doi.org/10.2196/81673

Abstract Background Generative artificial intelligence (AI) is increasingly used in medical education, including AI-based virtual patients to improve interview skills. However, how much AI-based assessment (ABA) differs from human-based assessment (HBA) remains unclear. Objective This study aimed to compare the quality of clinical interview assessments generated via an ABA (GPT-o1 Pro [ABA-o1] and GPT-5 Pro [ABA-5]) with those generated via an HBA conducted by clinical instructors in an AI-based virtual patient setting. We also examined whether AI reduced evaluation time and assessed agreement across participants with different levels of clinical experience. Methods A standardized case of leg weakness was implemented in an AI-based virtual patient. Seven participants (2 medical students, 3 residents, and 2 attending physicians) each conducted an interview with the AI patient, and transcripts were scored using the 25-item Master Interview Rating Scale (0‐125). Three evaluation strategies were compared. First, GPT-o1 Pro and GPT-5 Pro scored each transcript 5 times with different random seeds to test case specificity. Processing time was logged automatically. Second, 5 blinded clinical instructors independently rated each transcript once using the same rubric. Third, reliability metrics were applied. For AI, intraclass correlation coefficients (ICCs) quantified repeatability. For humans, the ICC(2,1) was calculated. Agreement was quantified using the Pearson r, Lin concordance correlation coefficient, Bland-Altman limits of agreement, Cronbach α, and ICC. Time efficiency was expressed as mean minutes per transcript and relative percentage reduction. Results Mean interview scores were similar across methods (ABA-o1: mean 52.1, SD 6.9; ABA-5: mean 53.2, SD 6.8; HBA: mean 53.7, SD 6.8). Agreement between ABA and HBA was strong (r=0.90; concordance correlation coefficient=0.88) with minimal bias (ABA-o1: mean 0.4, SD 2.7; ABA-5: mean 1.5, SD 5.2; limits of agreement: –4.9 to 5.7 for ABA-o1 and –8.6 to 11.7 for ABA-5). The Cronbach α was 0.81 (ABA-o1), 0.86 (ABA-5), and 0.80 (HBA); the ICC(3,1) was 0.77 (ABA-o1) and 0.82 (ABA-5); and the ICC(2,1) was 0.38 (HBA). The coefficient of variation for ABA was approximately half that of HBA (6.6% vs 13.9%). Processing time for 5 runs was 4 minutes, 19 seconds for ABA-o1 and 3 minutes, 20 seconds for ABA-5 vs 10 minutes, 16 seconds for physicians, corresponding to 58% and 67.6% reductions, respectively. Conclusions ABA-o1 and ABA-5 produced scores closely matching HBA while demonstrating superior consistency and reliability. In the setting of virtual interview transcripts, these findings suggest that ABA may serve as a valid, rapid, and scalable alternative to HBA, reducing per-assessment time by over half. Applied strategically, AI-based scoring could enable timely feedback, improve efficiency, and reduce faculty workload. Further research is needed to confirm generalizability across broader settings.

**ИИ:** ? · обе модели · неясен конструкт · GPT models and clinical instructors scored the same interview transcripts on the MIRS. It's unclear whether physician communication skills count as a psychological construct.

**Решение:** =

---

### 854 · R5746

**Measuring the practice and implementation of shared-decision making (OPTION12): how open-sourced smaller LLMs (OS-sLLMs) perform on this task**

2026 · Leiden Repository (Leiden University) · article · en · https://hdl.handle.net/1887/4299407

Background: Shared-decision making (SDM) is an important practice in clinical consultations in which patients and their loved ones jointly discuss and decide on treatment options with clinicians. This SDM process is often coded by the OPTION12 instrument, an observer-based tool, consisting of 12 items, rated on a 5-point Likert scale. This coding is done by human coders, which costs much time and very often disagreement happens. With the development of LLMs, we explore the capability of open-sourced privacy-preserving smaller LLMs on performing this task. It has a potential to automate or partially automate, with humans in the loop, the coding task. Methods: For human coding, we annotated the transcripts of clinical consultations using OPTION12 on 26 melanoma interviews that include 3 roles: caregivers, patients and doctors. Two human coders resolved their disagreements after independent coding. To measure SDM using OS-sLLMs, we divide the data into development and testing sets. We designed the full investigation framework as shown in the figure attached. It includes 1) a pilot study on development set (11 interviews) for prompt-refinement and best performing sLLM selection as a judge-sLLM; and 2) deploying the finetuned prompts and judge-sLLM with development examples on the testing set (15 interviews) and asking the judge-sLLM to resolve the disagreement on other OS-sLLMs’ scoring. Firstly, for prompt refinement, we use chain-of-thoughts (CoTs), LLM-assisted prompting, human-in-the-loop with sample output (few-shot) feedback. For OS-sLLMs, we use both 1) general domain models Llama, Gemma, and Mistral, and 2) medical domain models Meditron and Medllama. Secondly, for judge-sLLM selection, at the system level, we measure the overall correlation between each sLLM and human coding using Spearman and Pearson correlation scores. At the segment-level, we also look into the most agreed-upon items and the disagreed-upon items (from the 12 items) for qualitative and quantitative studies. Finally, we deploy the OS-sLLMs on the testing set and use the judge-sLLM to resolve disagreements. Preliminary results: Five OS-sLLMs show the following findings: 3 general domain OS-sLLMs perform better than the 2 medical domain ones that both generate hallucinations and not following prompts precisely, indicating further developments needed for medical OS-sLLMs. Mistral7b outperformed the other two Gemma3:12b and Llama3.1:8b by 4 consensus with human coding, vs 3 items. The overall correlation with human coding on these 12 items is (0.83, 0.80, 0.64) using Pearson correlation, and (0.81, 0.78, 0.61) using Spearman rank correlation from the three models (gemma3:12b, llama3.1:8b, mistral7b). For the items that OS-sLLMs agree with human coders, OS-sLLMs can pick up the same sentences as the humans in some cases, but in other cases, they can also pick up even better quotes than humans. Discussion: We report the first research findings using OS-sLLMs on measuring SDM with the OPION12 in melanoma patients’ consultation transcripts. The performance of such OS-sLLMs are promising and valuable to our task. It has agreements with human coders on certain items and we are looking into the disagreement to see if we can have different inputs from OS-sLLMs, or if we can fine-tune OS-sLLMs to achieve human level performances on the rest of the items. In the long term view, we expect fine-tuned OS-sLLMs can achieve human level performance and be deployed into the coding task with humans in the loop for verification and quality control.

**ИИ:** + · обе модели · кодирование сессий · Small open-source LLMs scored OPTION12 shared-decision-making in consultation transcripts; Pearson/Spearman correlations with human coders reported.

**Решение:** =

---

### 855 · R5747

**Measuring the practice of shared-decision making (OPTION12): An Investigation into Open-sourced Smaller LLMs (OS-sLLMs) for Better Privacy and Sustainability**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.06127

We present LLM4SDM, the first study of open-source smaller language models (OS-sLLMs) for automated assessment of shared decision making (SDM) using the Observer OPTION12 framework. Unlike previous work that relies on large commercial models and the shorter OPTION5 instrument, our study focuses on privacy-preserving locally deployable models and Dutch melanoma consultation transcripts. Using expert-annotated clinical consultations, we evaluate three general-domain and two medical-domain OS-sLLMs during a development-phase pilot study. Results show that general-domain models outperform medical-domain models, which exhibit substantial hallucination and instruction-following failures. Gemma3:12b achieves the strongest agreement with human annotations (Pearson r=0.51, Spearman \r{ho}=0.59). Item-level and qualitative analyses reveal systematic challenges related to temporal discourse reasoning, conversational role attribution, and evidence grounding. We further introduce a Judge-LLM consensus framework designed to support disagreement resolution among multiple models. Our findings suggest that while current OS-sLLMs cannot replace human annotators, they offer a promising foundation for privacy-preserving human-in-the-loop SDM assessment. Pilot study. Preliminary findings on open-source smaller LLMs for OPTION12 shared decision-making assessment

**ИИ:** + · обе модели · кодирование сессий · Open-source LLMs score OPTION12 shared decision-making in consultation transcripts; agreement with expert annotations reported (Pearson/Spearman).

**Решение:** =

---

### 856 · R5748

**PerceptionLab at PsyDefDetect: Overcoming Extreme Response Bias in LLMs via Rubric-Grounded Retrieval and Supervised Clinical Reasoning Distillation for Fine-Grained Ordinal Classification**

2026 · Proceedings of the BioNLP 2026 (Shared Tasks) · conference-paper · https://doi.org/10.18653/v1/2026.bionlp-2.17

Automating the classification of psychological defense mechanisms is a critical yet challenging frontier in clinical natural language processing. General-purpose Large Language Models (LLMs) struggle to apply fine-grained ordinal frameworks like the Defense Mechanism Rating Scales due to the implicit nature of clinical cues and a fundamental clinical reasoning gap. These models exhibit severe extreme response bias, systematically gravitating toward the scale’s endpoints while failing to resolve nuanced, mid-level defenses. In this paper, we present our third-place system for the P SY D EF D ETECT Shared Task at BioNLP 2026, designed specifically to overcome this failure mode. We propose a hybrid architecture that synergizes label-flattened generative retrieval with an LLM classifier fine-tuned via the distillation of supervised clinical reasoning traces. This dual approach, grounding decisions in rubric criteria while leveraging task-specific supervision, successfully mitigates the observed bias, achieving an accuracy of 67.37% and a macro-F1 of 39.56%. Our work provides empirical evidence that tightly integrating targeted clinical supervision with dynamic rubric-grounded retrieval significantly outperforms the raw parameter scale of un-tuned foundation models.

**ИИ:** + · обе модели · бенчмарк с метками людей · Fine-tuned LLM classifies defense mechanisms (DMRS) in shared-task text; accuracy and F1 are measured against labels that are presumably human-annotated.

**Решение:** =

---

### 857 · R5753

**The Flattening Effect: A Comparative Study of Sociopragmatic Erasure and Identity Loss in Translated Vietnamese-English Cyber-Discourse**

2026 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/3b9vn_v1

This study investigates the "flattening effect" in translated Vietnamese-English code-mixed discourse, a phenomenon where semantic content is preserved while sociopragmatic nuances are erased. Utilizing a subset of the VietMix corpus, an "LLM-as-a-Judge" framework was employed to evaluate four dimensions: Structural Hybridity, Emotional Buffering, Status Signaling, and In-group Identity. While the model demonstrated moderate reliability in binary feature detection (inclusive $\kappa = 0.416$), its alignment with human consensus collapsed when quantifying erasure severity (expressive $\kappa = 0.141$). Qualitative analysis revealed that the model frequently over-interprets functional jargon while failing to recognize localized subcultural markers. These findings highlight a critical capability gap in current models, which prioritize global linguistic patterns over localized sociopragmatic functions. Consequently, future developments should move beyond semantic equivalence to incorporate localized cultural awareness within automated computer-mediated communication (CMC) analysis.

**ИИ:** ? · обе модели · неясен конструкт · LLM judge compared with human consensus (kappa) on sociopragmatic features, including emotional buffering and in-group identity; unclear whether these count as psychological constructs.

**Решение:** =

---

### 858 · R5785

**Studi Komparatif Base Model, Tool-Augmented, Dan Ai Agent Pada Konseling Kesehatan Mental Menggunakan Model QWEN**

2026 · review

Masalah kesehatan mental yang dialami oleh remaja di Indonesia dipengaruhi oleh berbagai faktor. Salah satunya adalah keterbatasan akses layanan psikologis yang terjangkau dan mudah diakses. Penelitian ini bertujuan untuk memberikan solusi dalam bentuk sistem digital berbasis AI agent dengan memanfaatkan model Qwen yang memiliki kemampuan reasoning dan penggunaan alat eksternal secara open-source. Selain menggunakan pendekatan AI agent, penelitian ini juga membandingkan baseline model, model fine-tuned (Emilia), dan pendekatan tool-augmented LLM. Evaluasi dilakukan menggunakan data CounselBench untuk interaksi tunggal dan data MindEval untuk interaksi berkelanjutan dengan menggunakan evaluator ahli psikologi dan LLM-as-a-Judge. Validasi reliabilitas menunjukkan kesepakatan fair antara psikolog dan LLM-as-a-Judge pada data CounselBench (QWK pooled = 0,399), namun tidak berkorelasi pada data MindEval (QWK pooled = 0,010) sehingga uji signifikansi data CounselBench menggunakan penilaian LLM-as-a-Judge dan data MindEval menggunakan penilaian psikolog. Hasil uji Friedman menunjukkan seluruh metrik CounselBench berbeda secara signifikan (p < 0,001), dengan Qwen3.5 (Base) meraih skor rerata tertinggi (M = 3,983). Selain itu, model Emilia menunjukkan keunggulan pada aspek Naturalness, Dialogic, dan Prescriptive, namun mengalami trade-off pada aspek Empathy. Pada data MindEval, tidak ditemukan perbedaan signifikan antarkonfigurasi akibat keterbatasan jumlah blok data. ================================================================================================================================= Mental health problems experienced by adolescents in Indonesia are influenced by various factors, one of which is the limited access to affordable and accessible psychological services. This study aims to provide a solution in the form of a digital system based on an AI agent by leveraging the Qwen model, which possesses open-source reasoning capabilities and external tool usage. In addition to the AI agent approach, this study also compares a baseline model, a fine-tuned model (Emilia), and a tool-augmented LLM approach. Evaluation was conducted using the CounselBench dataset for single-turn interactions and the MindEval dataset for multi-turn interactions, employing both expert psychologists and an LLM-as-a-Judge as evaluators. Reliability validation indicated fair agreement between psychologists and LLM-as-a-Judge on the CounselBench data (pooled QWK = 0.399), but no meaningful correlation on the MindEval data (pooled QWK = 0.010) consequently, significance testing for CounselBench relied on LLM-as-a-Judge ratings, while MindEval relied on psychologist ratings. Friedman test results showed that all CounselBench metrics differed significantly (p < 0.001), with Qwen3.5 (Base) achieving the highest mean score (M = 3.983). Furthermore, the Emilia model demonstrated superiority in the Naturalness, Dialogic, and Prescriptive dimensions, yet exhibited a trade-off in the Empathy dimension. On the MindEval data, no significant differences were found among configurations due to the limited number of data blocks

**ИИ:** + · обе модели · LLM-судья · LLM-as-a-Judge rated mental-health counselling responses; agreement with psychologist ratings reported (QWK 0.399, 0.010).

**Решение:** =

---

### 859 · R5798

**Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent**

2026 · Journal of Educational Data Mining · journalarticle/, article · en · https://doi.org/10.5281/zenodo.18852440

Conversational learning systems offer new opportunities to examine learning processes through chat log data. Constructs such as persistence, self-efficacy, interest, perceived challenge, and prior knowledge are known predictors of student performance but are challenging to detect at scale using traditional methods. This study explores the use of Large Language Models (LLMs) to automatically code indicators of these constructs from student chat logs collected through a conversation-based assessment (CBA) for middle school mathematics. Indicators included observable behaviors such as students' expressions of challenge, help-seeking, goal-setting, and self-regulatory strategies evident in their conversational interactions within the CBA. We evaluated multiple configurations of ChatGPT4o, varying temperature settings (0, .3, .7, 1) and model types (mini vs. regular), against human expert coders. The dataset comprised over 10,000 student turns collected from 107 middle school students classified as English learners as they interact with the CBA. Reliability was assessed within and between LLM configurations and humans. Results reveal systematic patterns: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings. Self-efficacy showed the highest human-LLM alignment. These findings illustrate the challenges of measuring complex psychological constructs and highlight the promise of human-LLM collaboration to enhance qualitative coding efficiency and validity in educational research. Supplemental materials are available online here: https://doi.org/10.17605/osf.io/s85ck.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-4o coded psychological constructs (self-efficacy, persistence, interest) in student chat logs; reliability compared against human expert coders.

**Решение:** =

---

### 860 · R5802

**Longitudinal symptom severity tracking in vagus nerve stimulation patients: a 2-stage LLM-based pipeline with explainable AI.**

2026 · JAMIA open · journal article, journalarticle, article · eng · https://doi.org/10.1093/jamiaopen/ooag195

Abstract Objectives To produce the first structured longitudinal dataset of symptom severity trajectories in vagus nerve stimulation (VNS) patients using a 2-stage large language model pipeline for automated symptom severity extraction from clinical notes, as part of the NIH-funded research evaluating vagal excitations and anatomical linkages (U54AT012307). Materials and methods We analyzed 1427 annotated clinical notes from 95 patients across 5 corpora. LLaMA models (3.2-1B, 3.2-3B, and 3.3-70B) were fine-tuned to classify 13 symptoms as present, absent, or negated (stage 1), then assessed severity (indeterminate, mild, moderate, or severe; stage 2). Longitudinal trajectories were tracked quarterly in 23 VNS patients against a 10-patient surgical control cohort (NSQIP). Results Severity F1-scores ranged from 0.76 to 0.96, and symptom classification reached 0.99 for high-prevalence symptoms, with the validation corpus (VNS vs NSQIP) as the dominant factor (29.4% of variance; no significant source-corpus effect), supporting cross-domain generalizability. Macro F1-scores were lower than weighted F1-scores for smaller models and NSQIP; suicidal-ideation sensitivity was lower on NSQIP than VNS (0.80 vs 1.00, largest model), limiting generalization for psychiatric risk detection. Equity analyses were exploratory given small subgroups (gender precision 0.95). The longitudinal dataset revealed a median time to clinically meaningful seizure improvement of 0.5 quarters, with 50% responders, 25% non-responders, and 25% worsened. Post-surgical decline was absent in the unmatched NSQIP control cohort, consistent with, but not confirming, VNS specificity. Discussion To our knowledge, this is the first system producing structured symptom trajectories from free-text VNS documentation, supporting individualized over population-level monitoring. Conclusion This dataset supports future treatment-response prediction, personalized device programming, and a reproducible clinical natural langauge processing benchmark for neuromodulation research.

**ИИ:** разошлись — Opus + (клиническая оценка: Fine-tuned LLaMA rates symptom presence and severity, including suicidal ideation, in human-annotated clinical notes; reports F1 against those annotations.); Sonnet ? (неясен конструкт: Fine-tuned LLaMA extracts symptom presence and severity from annotated VNS clinical notes (human labels). It includes suicidal ideation, but the symptoms may be mostly neurological, so the construct is unclear.)

**Решение:** +

---

### 861 · R5826

**What Parents Can See: Divergent Accounts of Youth AI Companion Use in Parenting and Teenager Subreddits**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.20720

Youth increasingly use AI companions, and parents are the primary mediators of that use. How effective that mediation can be depends on whether parents are aware of how adolescents actually use these systems and what risks and benefits such use carries; nevertheless, prior work has only studied these demographic groups in isolation, and existing taxonomies attend almost entirely to risk. We analyze 1,628 Reddit posts about youth AI companion use from parenting and teenager communities (2023--2026); develop a codebook covering modes of use, risks, benefits, and parental mediation; and apply it at corpus scale with an LLM. The two communities yield divergent accounts. Teenagers most often discuss receipt of emotional support from AI companions (31% of teenager posts vs. 19% of parenting posts), whereas parents most often discuss teenage use of AI companions for romantic and sexual interaction (36% vs. 25%). Teenagers are not unaware of other risks, however; indeed, attachment and dependence is the risk they raise most (19%), close to the parental rate (16%). Teenagers also describe benefits that risk-centered taxonomies do not capture and parents rarely mention, most notably emotional support (27% vs. 5%). We argue these differences track what a given kind of use makes visible to someone outside the conversation. Chatting with a companion for hours every night leaves a trace beyond the chat itself; sexting with a character stands out when a parent reads the log; venting about a fight with a friend does neither, since it looks like any other conversation. The first surfaces as dependence, the second as sexual content, and the third as emotional support, which is the one parents most often miss. Parental guidance and system design should attend to use cases that reach parents by neither route, emotional support foremost among them.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · An LLM applied a codebook (emotional support, attachment/dependence risks) to Reddit posts; the abstract doesn't say if it was checked against human coding.

**Решение:** =

---

### 862 · R5843

**Multi-Objective Aligned Small Language Model Framework for SUD Patient Dialogue Generation**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.09209

Substance Use Disorder (SUD) counseling requires patient responses that reflect underlying cognitive states such as beliefs, coping strategies, and readiness for change. Although large language models (LLMs) can generate fluent text, they often fail to produce cognitively coherent and clinically realistic patient behavior, especially under ethical and data-scarce clinical settings. Moreover, deploying frontier-scale LLMs in healthcare applications presents practical challenges including high computational cost, latency, privacy concerns, and limited deployability in resource-constrained environments, motivating the need for cognitively aligned small language models (SLMs). We propose a cognitively grounded framework for SUD patient dialogue generation that explicitly models and aligns latent cognitive components with patient histories and counselor questions. Our pipeline consists of two stages: cognitive component detection and cognitive component-aligned dialogue generation. To enable effective learning with smaller models, we combine knowledge distillation from high-capacity teacher models, preference optimization from human-annotations, and attention-guided reward shaping. Extensive evaluations using automatic scores like BERTScore, ROUGE, METEOR and BLEU, and LLM-as-judge hit-metrics against both human and teacher-model references show that cognitively informed fine-tuning substantially improves cognitive realization and alignment over a generic instruction-tuned baselines and mental health domain specific SLMs, with particularly strong gains for open-ended cognitive components.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mostly patient dialogue generation, but the cognitive component detection stage may be scored against human annotations; worth checking the full text.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Focuses on generating SUD patient dialogue with small language models; evaluation uses text-overlap metrics and LLM-as-judge against references, with no LLM–human coding agreement reported.)

**Решение:** -

---

### 863 · R5859

**Mixture-of-Expert Large Language Models for Text-Based Personality Assessment From Asynchronous Video Interviews**

2026 · IEEE Transactions on Affective Computing · journalarticle, article, research article · en · https://doi.org/10.1109/taffc.2026.3667846

In selection and assessment, Large Language Models (LLMs) are deemed suitable for personality assessment of Asynchronous Video Interviews (AVI) due to their advanced linguistic understanding and semantic interpretation capacities. However, most of the previous works have focused on personality trait classification rather than regression. Since current LLMs are trained on massive corpora, they are more attuned to text-based structures than to numeric data. The classification-centered approach fails to take into account the fact that personality traits are continuous, instead of categorical, variables. In addition, LLMs suffer from low rating validity due to their tendency to be over-lenient, assigning higher than average personality scores to a large number of individuals (i.e., issues of Positivity Biases). To address these challenges, we designed a text-based, two-stage, Mixture-of-Experts based personality assessment framework (MoE-Personality) to provide fine-grained personality ratings and regulate the positivity biases of LLMs. The designed model first rates the coarse-grained personality category of the individual (classification stage). After that, the model rates fine-grained personality scores by merging the obtained personality category and empirical score ranges of different personality categories. Inspired by the the way human annotators rate personality traits, each stage comprises multiple annotator LLM experts and one aggregator LLM expert to promote validity. Our experiments in two datasets show that the designed framework outperformed open-sourced, medium-sized LLMs (e.g., Llama 3.1-8B, qwen2-7B) and achieved comparable results with close-sourced, large-sized LLMs (e.g., GPT-3.5 and GPT-4).</p

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs rate personality from interview transcripts; unclear if ground truth is human observer ratings or self-report.

**Решение:** =

---

### 864 · R5866

**Auditing Stealth Sycophancy in Mental-Health Dialogue: Structured Clinical-State Diagnostics and Clean Matched Benchmarks**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.03472

Mental-health dialogue models are increasingly evaluated by AI-based evaluators, yet these evaluators often treat surface empathy, supportiveness, or fluency as evidence of safety. In this paper, we study a hidden failure mode that we call implicit sycophancy: a response may appear empathetic while implicitly reinforcing catastrophizing, avoidance, hopeless prediction, or CBT-style labeling. To examine this problem, we introduce a diagnostic benchmark for implicit-sycophancy detection, built from three representative mental-health dialogue sources covering everyday peer support, counseling-style emotional support, and crisis-oriented interaction, and further construct a leakage-audited clean single-response matched benchmark with 500 contexts and 1,500 matched response windows. We then propose Dynamic Emotional Signature Graphs (DESG), a structured offline audit framework that separates LLM-based state extraction from final scoring and evaluates clinical direction through semantic, affective, and cognitive-distortion state transitions rather than free-form LLM judgment. Unlike metadata, surface-style, lexical, embedding, and rubric-LLM baselines, DESG scores the direction of clinical-state change induced by a response; on the leakage-audited clean matched benchmark, DESG-StateRisk improves over the strongest non-DESG baseline by 0.0488 macro-F1 and achieves the best harmful-risk detection result. These results suggest that evaluating implicit sycophancy requires explicit clinical-state modeling together with leakage checks, shortcut controls, and competitive baselines.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM judges detect harmful sycophancy in mental-health responses (macro-F1), but the abstract doesn't say whether benchmark labels are human-annotated or constructed.

**Решение:** =

---

### 865 · R5876

**Research on a Speech-Modal Learning Behavior Evaluation Model Based on SenseVoice and LLMs**

2026 · International Conference on Computer Information and Big Data Applications (CIBDA) · book, conference, conference-paper · https://doi.org/10.1145/3813822.3814096

With the evolution of smart education towards the stage of Multimodal Learning Analytics (MMLA), voice data holds significant value for the accurate evaluation of learners’ cognitive load and emotional engagement. This research proposes an automated evaluation framework based on dual-model collaboration, which indicatively integrates the emotional recognition capability of SenseVoice with the deep semantic understanding function of LLMs. By extracting rich emotion tags via SenseVoice and leveraging LLMs for high-order reasoning, the framework performs a multi-dimensional quantification of learners’ Semantic Content Representation (SCR), Engagement Features (EF) and Sentiment Orientation (SO). These metrics are then synthesized into a weighted Final Learning Score (FLS) to reconstruct high-fidelity learner profiles. Experimental validation across 50 group discussions in “black-box testing” scenarios reveals that the correlation coefficient between system-generated scores and expert ratings reached 0.897 (with the SCR dimension specifically hitting 0.911), while the Root Mean Square Error (RMSE) was 6.44. The results demonstrate that the multi-modal fusion model effectively mitigates the biases of single-metric evaluations through inter-dimensional “logical compensation.” It exhibits high scientific validity and robustness in simulating expert evaluation logic, thereby providing a reliable pathway for precise pedagogical intervention in digital environments.

**ИИ:** ? · обе модели · неясен конструкт · LLM scores of engagement and sentiment in group-discussion speech correlate with expert ratings; unclear whether the learning-behaviour score counts as a psychological construct.

**Решение:** =

---

### 866 · R5878

**A Glyphic-LLLM-based multimodal framework for predicting youth symbolic identity under the Jingchu red culture paradigm**

2026 · International Conference on Communication, Information and Digital Technologies · conference, review · https://doi.org/10.1117/12.3089302

Youth symbolic consciousness represents a critical yet insufficiently investigated dimension of cultural sustainability, particularly as digital transformation accelerates changes in communication, identity formation, and cultural transmission among younger generations. Traditional approaches for assessing cultural identity—such as self-report surveys, interviews, and manual content analysis—are inherently limited in their capacity to capture the complex, multimodal, and context-dependent ways in which modern youth express, interpret, and reshape symbolic meaning. These limitations are especially pronounced given the rise of digital platforms where text, imagery, and symbolic motifs intermingle and evolve at unprecedented speed. To address these methodological and technical challenges, this study presents a novel artificial intelligence-driven multimodal framework for predicting youth symbolic identity, with a specific focus on integrating glyph-aware neural encoders, vision transformers, and large language models (LLMs). The proposed Glyphic-LLLM architecture leverages advanced cross-modal attention mechanisms to dynamically fuse textual, visual, and glyphic features, thus enabling a more holistic and nuanced modeling of symbolic consciousness. Key technical contributions include the design of a multi-branch neural network structure, the use of motif-level attention for interpretability, and the implementation of motif-alignment regularization for expert-guided learning. Extensive experiments conducted on an authentic, expert-annotated multimodal dataset demonstrate that the Glyphic-LLLM framework achieves a significant improvement in prediction accuracy (up to 89.5%) and interpretability compared to both unimodal approaches and conventional multimodal baselines. Furthermore, qualitative analyses highlight the model’s capacity to uncover latent symbolic patterns and generational shifts in youth expression, offering new insights for computational cultural analysis and digital communication research. These findings underscore the practical value of state-of-the-art AI techniques in advancing interdisciplinary research at the intersection of computer science, humanities, and digital society.

**ИИ:** разошлись — Opus ? (неясен конструкт: Multimodal LLM-based model tested against expert-annotated youth symbolic identity; unclear whether this is a psychological construct or text coding.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Multimodal neural model predicting cultural symbolic identity from images and text; no LLM coding of psychological text against human coders.)

**Решение:** -

---

### 867 · R5898

**A Systematic Evaluation Framework on Emotion Inference for Large Language Models Using Appraisal Theory**

2026 · IEEE Transactions on Affective Computing · journalarticle, article · https://doi.org/10.1109/taffc.2026.3702035

We propose and implement a systematic evaluation framework to assess Large Language Models’ (LLMs) ability to infer emotions through the lens of Appraisal Theory of Emotion. Our framework generates thousands of story vignettes across six domains - ranging from sports to social interactions that can be systematically modified using emotion-relevant features derived from appraisal theory. We first validated these vignettes through human participant responses, which served as validation for the models’ responses. Our evaluation included four LLMs: GPT-4o, Claude Sonnet 3.5, Gemini 1.5 Pro, and Llama 3.1 405B. Our results show that all tested LLMs exhibit strong correlations with human responses in five of the six domains, demonstrating sensitivity to emotion-relevant features that align with both theoretical predictions and human ratings. Notably, Claude Sonnet and Llama perform consistently across all domains, while GPT-4o and Gemini 1.5 Pro diverged from human ratings in one domain, assigning implausible emotional intensities. These inconsistencies suggest that surface-level features can override theoretical manipulations, leading to inconsistent emotion ratings even when models demonstrate robust performance in other domains. Our findings highlight the general alignment between LLMs and human emotional inference when appraisal features are explicitly manipulated, while also demonstrating the necessity of systematic testing to identify domain-specific vulnerabilities. This work provides a framework and recommendations for such systematic evaluations.

**ИИ:** + · обе модели · бенчмарк с метками людей · Four LLMs rated emotion intensity in story vignettes; correlations with human participants' ratings of the same vignettes are reported.

**Решение:** =

---

### 868 · R5922

**DEFINED: A Data-Efficient Computational Framework for Fine-Grained Creativity Assessment in Debate Scenarios**

2026 · ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD) · journalarticle, book, conference · https://doi.org/10.1145/3770855.3817874

Human creativity has emerged as a critical competency in the era of large language models. Assessing creativity in complex, open-ended environments is a grand challenge in data mining, currently hindered by a reliance on standardized simple tasks and the scarcity of fine-grained expert data. As an ecologically valid assessment context, debate reflects multiple dimensions of creativity, encompassing both divergent thinking and convergent thinking. Moreover, debate is a data-rich domain, with a large volume of publicly accessible materials. Current mainstream automated scoring methods are poorly suited to complex settings such as debate, and therefore still rely on costly human evaluation. To this end, this paper proposes DEFINED, a data-efficient computational framework for fine-grained creativity assessment in debate scenarios. DEFINED operationalizes debate creativity through a hierarchical eight-dimensional metric system, implemented via a pre-trained autoregressive language model with a hierarchical scoring head that supports both fine-grained and coarse-grained evaluation. Statements and their associated expert scores were obtained from authentic debate competitions, and a constrained data augmentation strategy was employed to address the elite bias inherent in the original data. DEFINED adopts a mixed-granularity training strategy enabling robust learning from limited fine-grained supervision annotated by trained graduate experts. To rigorously validate ecological validity beyond synthetic benchmarks, we incorporate an empirical study with debate-naive participants, utilizing these authentic data to serve as a qualitative case study for mid-to-low proficiency populations. Across our evaluation protocol, our scoring model achieves accurate and stable scoring, outperforming prompt-based large language model evaluators and existing debate scoring methods, while mitigating common failure modes observed in current approaches. The code for DEFINED is available on GitHub at https://github.com/tzwo/DEFINED.

**ИИ:** + · обе модели · подсчёт методики · A fine-tuned autoregressive LM and prompted LLM evaluators score creativity in debate statements against expert human ratings.

**Решение:** =

---

### 869 · R5940

**Evaluating Large Language Models for Suicide Risk Detection: A Pilot Study**

2026 · OSF Preprints (OSF Preprints) · text/project, preprint · https://doi.org/10.17605/osf.io/skdvf

Large language models (LLMs) are now widely accessible and increasingly used for information-seeking and self-guided support, including by individuals experiencing psychological distress. This widespread adoption raises safety concerns in high-risk contexts like suicidal ideation. While prior research shows that these models can detect suicidal language, little is known about their ability to adjust responses across varying levels of suicide risk. This pilot study evaluated Gemini 2.5 Flash’s capacity to differentiate among non-suicidal distress, suicidal ideation without plan, and imminent suicide risk using 60 validated clinical vignettes from the Self-Directed Violence Classification System.

**ИИ:** ? · обе модели · другое · Gemini was tested on expert-classified SDVCS suicide-risk vignettes, but it may only be generating responses rather than rating risk against those labels.

**Решение:** =

---

### 870 · R5943

**An independent supervisory safety agent improves reaction of large language models to suicidal ideation**

2026 · medRxiv · preprint, ppr · https://doi.org/10.64898/2026.04.13.26350757

Abstract Background Large language models (LLMs) are increasingly used in mental health contexts, yet their detection of suicidal ideation is inconsistent, raising patient safety concerns. Methods We conducted a cross-sectional evaluation using 224 paired suicide-related clinical vignettes presented in a single-turn format under two conditions (with and without structured clinical information). Native LLM safeguard responses were compared with an independent supervisory safety architecture with asynchronous monitoring. The primary outcome was detection of suicide risk requiring intervention. Results The supervisory system detected suicide risk in 205 of 224 evaluations (91.5%) versus 41 of 224 (18.3%) for native LLM safeguards. Among 168 discordant evaluations, 166 favored the supervisory system and 2 favored the LLM (matched odds ratio ≈83.0). Both systems detected risk in 39 evaluations, and neither in 17. Detection was highest in scenarios with explicit suicidal ideation and lower in more ambiguous presentations. Conclusions Native LLM safeguards frequently failed to detect suicide risk in this structured evaluation. An independent monitoring approach substantially improved detection, supporting the role of external safety systems in high-risk mental health applications of LLMs.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM-based agent detects suicide risk in clinical vignettes; unclear whether the reference is expert human risk ratings or simply how the vignettes were designed.

**Решение:** =

---

### 871 · R5946

**Human-Guided Reasoning with Large Language Models for Vietnamese Speech Emotion Recognition**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.01711

Vietnamese Speech Emotion Recognition (SER) remains challenging due to ambiguous acoustic patterns and the lack of reliable annotated data, especially in real-world conditions where emotional boundaries are not clearly separable. To address this problem, this paper proposes a human-machine collaborative framework that integrates human knowledge into the learning process rather than relying solely on data-driven models. The proposed framework is centered around LLM-based reasoning, where acoustic feature-based models are used to provide auxiliary signals such as confidence and feature-level evidence. A confidence-based routing mechanism is introduced to distinguish between easy and ambiguous samples, allowing uncertain cases to be delegated to LLMs for deeper reasoning guided by structured rules derived from human annotation behavior. In addition, an iterative refinement strategy is employed to continuously improve system performance through error analysis and rule updates. Experiments are conducted on a Vietnamese speech dataset of 2,764 samples across three emotion classes (calm, angry, panic), with high inter-annotator agreement (Fleiss Kappa = 0.8574), ensuring reliable ground truth. The proposed method achieves strong performance, reaching up to 86.59% accuracy and Macro F1 around 0.85-0.86, demonstrating its effectiveness in handling ambiguous and hard-to-classify cases. Overall, this work highlights the importance of combining data-driven models with human reasoning, providing a robust and model-agnostic approach for speech emotion recognition in low-resource settings. 6 pages, 2 figures. Dataset of 2,764 Vietnamese speech samples across three emotion classes

**ИИ:** разошлись — Opus ? (другое: LLM classifies emotion against human-annotated labels, but input seems to be acoustic speech features, not clearly text; a hybrid pipeline.); Sonnet -7 (другое — напишите почему: Speech emotion recognition from acoustic features, not text coding. LLM is used as a classifier with human labels as ground truth, not as a rater of text.)

**Решение:** -

---

### 872 · R5954

**TRUST: an large language model-based dialogue system for trauma understanding and structured assessments.**

2026 · Journal of the American Medical Informatics Association : JAMIA · journal article, med, journalarticle · eng · https://doi.org/10.1093/jamia/ocag050

OBJECTIVES: While large language models (LLMs) have been widely used to assist clinicians and support patients, no existing work has explored dialogue systems for standard diagnostic interviews and assessments. This study aims to bridge the gap in mental healthcare accessibility by developing an LLM-powered dialogue system that replicates clinician behavior. MATERIALS AND METHODS: We introduce TRUST, a framework of cooperative LLM modules capable of conducting formal diagnostic interviews and assessments for post-traumatic stress disorder (PTSD) following the Clinician-Administered PTSD Scale for DSM-5 (CAPS-5). To guide the generation of appropriate clinical responses, we propose a Dialogue Acts schema specifically designed for clinical interviews. Additionally, we develop a patient simulation approach based on real-life interview transcripts to replace time-consuming and costly manual testing by clinicians. RESULTS: A comprehensive set of evaluation metrics is designed to assess the dialogue system from both the agent and patient simulation perspectives. Expert evaluations by conversation and clinical specialists show that TRUST performs comparably to real-life clinical interviews. DISCUSSION: Our system performs with clinical quality approaching that of human clinicians, with room for future enhancements in communication styles and response appropriateness. CONCLUSIONS: Our TRUST framework shows its potential to facilitate mental healthcare availability.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM dialogue system runs CAPS-5 PTSD assessments; experts rated its outputs, but its symptom scoring may also be compared with clinician ratings.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM dialogue system conducting PTSD interviews with simulated patients; experts evaluate the system, with no LLM coding of text against human labels.)

**Решение:** -

---

### 873 · R5961

**Large language models for deductive qualitative content analysis in dementia-focused embedded pragmatic clinical trials: A comparative methodological study.**

2026 · Implementation science communications · journal article, journalarticle, review · eng · https://doi.org/10.1186/s43058-026-00953-8

INTRODUCTION: Thematic coding helps researchers characterize intervention implementation in embedded pragmatic clinical trials (ePCTs), particularly interventions for older adults with dementia and care partners. However, manual coding is time-consuming, requiring multiple researchers. Because implementation science relies on systematic identification of determinants, barriers, and facilitators, advances in Artificial Intelligence (AI), specifically large language models (LLMs), may automate this process meaningfully by accelerating implementation evaluations within ePCTs. We developed and tested an automated algorithm using Chat GPT-4o and Chat GPT-4o-mini to achieve human-level performance coding interview transcripts. METHODS: We created a Python-based system that uses LLMs to process and code semi-structured interview transcripts about implementation challenges in translating dementia interventions into healthcare systems. The system matches excerpts to an existing codebook. Multiple iterations, including expert review, were used to refine accuracy and efficiency. RESULTS: The LLM consistently coded more excerpts than humans. In the third iteration (V3), the LLM captured 61.7% of human-coded excerpts, with matching rates reaching as high as 72.6% for individual transcripts. Matching was higher for descriptive codes, 63.7%, than interpretive codes, 57.7%. The LLM identified 206 correct coded excerpts that human coders missed. In the fourth iteration (V4), GPT-4o outperformed GPT-4o-mini: descriptive code matching reached 89% (e.g. "Site Characteristics"), compared to 69% for GPT-4o-mini with the R1+R2 85% threshold. GPT-4o showed a weak, but positive correlation (r = 0.230) between transcript word count and matching agreement, while 4o-mini showed a moderate, but negative correlation (r = -0.452). The LLM workflow yielded a 97% reduction in time and a 99% reduction in cost per transcript. CONCLUSION: This study compared an LLM-powered workflow with human coding for thematic analysis. The LLM aligned strongly with human coders. While error rates necessitate human oversight, time and cost reduction, and ability to identify missed excerpts make it a potentially reliable supplementary tool. Although ePCTs and implementation science share complementary goals, they differ in focus, this flexible approach enhances efficiency and scalability, with acceptable accuracy. It streamlines the qualitative research workflow from outlining to the analysis of implementation processes in real-world settings and may accelerate existing implementation approaches while minimizing implementation resources.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o applied a codebook to interview transcripts and was compared with human coders, but the codes are implementation determinants, which may not be psychological constructs.

**Решение:** =

---

### 874 · R5969

**Socio Mind AI: Multi-Channel Digital Behavioral Footprint Analyzer**

2026 · Zenodo (CERN European Organization for Nuclear Research) · journalarticle/, article · en · https://doi.org/10.5281/zenodo.19917892

SocioMind AI is an AI-powered analytical framework that quantifies psychological states and personality traits through the automated processing of heterogeneous social media data. Unlike traditional sentiment analysis — which reduces complex human communication to a single positive/negative polarity score — SocioMind AI employs a multi-dimensional approach to construct a comprehensive \\\"Linguistic DNA\\\" profile of an individual, correlating public persona signals with private aspirational data to deliver a 360-degree behavioral footprint. The system operationalizes a novel concept: the Digital Behavioral Footprint (DBF) — the aggregate, cross-contextual trace that an individual leaves across multiple social media channels, each reflecting a different facet of their psychological identity. By processing and cross-referencing Primary Content, Interactional Tone, Interest Graphs, and Aspirational Signals simultaneously, SocioMind AI achieves what single-channel sentiment tools cannot: a holistic, internally-validated psychological portrait. At its inference core, SocioMind AI leverages the Gemini 3 Flash large language model architecture, optimized for structured JSON output to ensure deterministic, research-grade data handling. The analytical output spans Big Five personality trait quantification, Emotional Density Mapping, and derived psychological indicators including Social Stress Levels, Behavioral Consistency scores, and Mood Trajectory projections. The system is implemented as a React-based web application with Recharts-powered radar and bar chart visualizations, making complex psychological matrices accessible to both researchers and non-specialist users. Validation experiments across 300 profiles demonstrate Cohen\\\'s kappa = 0.74 for Big Five dimensions and Pearson r = 0.81 for emotional valence detection, establishing SocioMind AI as a viable zero-knowledge psychological proxy for research-grade personality inference.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Gemini rates Big Five and emotion from social media posts; reports kappa 0.74, but the reference (human coders or self-report) isn't stated.

**Решение:** =

---

### 875 · R5974

**The Effect of Idea Elaboration on the Automatic Assessment of Idea Originality**

2026 · ArTS Archivio della ricerca di Trieste (University of Trieste https://www.units.it/) · journalarticle, book, preprint/article · en · https://doi.org/10.48550/arxiv.2604.20569

Automatic systems are increasingly used to assess the originality of responses in creative tasks. They offer a potential solution to key limitations of human assessment (cost, fatigue, and subjectivity), but there is preliminary evidence of a self-preference bias. Accordingly, automatic systems tend to prefer outcomes that are more closely related to their style, rather than to the human one. In this paper, we investigated how Large Language Models (LLMs) align with human raters in assessing the originality of responses in a divergent thinking task. We analysed 4,813 responses to the Alternate Uses Task produced by higher and lower creative humans and ChatGPT-4o. Human raters were two university students who underwent intensive training. Machine raters were two specialised systems fine-tuned on AUT responses and corresponding human ratings (OCSAI and CLAUS) and ChatGPT-4o, which was prompted with the same instructions as human raters. Results confirmed the presence of a self-preference bias in LLMs. Automatic systems tended to privilege artificial responses. However, this self-preference bias disappeared when the analyses controlled for the idea elaboration. We discuss theoretical and methodological implications of these findings by highlighting future directions for research on creativity assessment.

**ИИ:** + · обе модели · подсчёт методики · ChatGPT-4o and fine-tuned LLM systems rate AUT originality; compared with trained human raters on the same responses.

**Решение:** =

---

### 876 · R6014

**Analyzing Nurse Sentiment in a Dutch Regional Newspaper During the COVID-19 Pandemic: Comparative Content Analysis of GPT-5, Gemini 2.5 Pro, and Human Coding.**

2026 · Journal of medical Internet research · comparative study, research-article, journal article · eng · https://doi.org/10.2196/98374

Abstract Background Large language models (LLMs) are increasingly used in qualitative research, but their reliability compared to human analysis, especially on large, non-English datasets, is unclear. Previous studies on older models (like GPT-4) show limitations in nuance and token capacity. Objective This study compared the qualitative analysis capabilities of OpenAI’s GPT-5 and Google’s Gemini 2.5 Pro (Gemini) with a human qualitative analysis. The study uses a large dataset of 317 Dutch newspaper articles from January 1, 2020, to December 31, 2023, investigating the sentiment toward nurses during the COVID-19 pandemic. Methods The study used a 2-phase methodology. First, a thematic comparison was conducted where the human researchers, GPT-5, and Gemini independently generated inductive coding trees from the entire corpus. Second, a comparative test was performed where all 3 coders applied a predefined codebook to a 10% stratified random subsample. The human baseline was validated through double-coding by 2 independent researchers, achieving an acceptable intercoder reliability (α=0.703). The AI analysis was iterative, using model-optimized prompts and an article-by-article approach. Results Both AI models successfully identified third-order themes (eg, “Health care heroes”) consistent with the data. In deductive application, however, both models systematically overcoded compared to the human consensus (181 and 183 codes vs 138), resulting in low intercoder reliability against the human baseline (α=0.487) for GPT-5 and (α=0.507) for Gemini. Conclusions This study suggests a potential divergence in analytical logic. The observed coding frequencies indicate that LLMs may default to semantic presence (literal frequency), whereas human coders appear to prioritize interpretive significance (contextual weight), leading to systematic overcoding. Consequently, this article argues that LLMs should not be viewed as autonomous researchers but as high-sensitivity filtering instruments requiring human calibration. This study concludes that AI can serve as a valuable assistant for qualitative researchers. Still, it benefits from a rigorous, iterative, and human-in-the-loop approach to manage methodological friction and ensure nuanced, valid analysis.

**ИИ:** ? · обе модели · неясен конструкт · GPT-5/Gemini applied a codebook to newspaper articles and were compared with human coders (α reported); unclear if sentiment toward nurses counts as a psychological construct.

**Решение:** =

---

### 877 · R6038

**Single-turn emergency psychiatric triage across 15 frontier AI chatbots**

2026 · arXiv (Cornell University) · preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2604.25415

People increasingly turn to general-purpose AI chatbots for advice about emotional and mental health problems, but the ability of these systems to recognize and appropriately triage psychiatric emergencies remains under-characterized. We evaluated psychiatric triage performance in 15 frontier AI chatbots using 112 clinical vignettes spanning four urgency levels, from routine care to immediate emergency assessment. In each trial (1680 total), a chatbot received a single user message conveying all triage-relevant information from one vignette and recommended a timeframe for care. The primary outcome was emergency under-triage; secondary outcomes included triage accuracy and the direction of errors. Vignettes and user messages were generated using a clinician-verified LLM pipeline. Across 415 emergency trials, 23 were under-triaged (5.5%; 95% CI 1.8-15.9). Overall accuracy, averaged across urgency levels, ranged from 42.0% to 71.8% across chatbots and was lowest for intermediate cases (19.6%; 95% CI 11.7-28.1). Every chatbot showed a net over-triage bias; overall, 763 of 786 incorrect assignments (97.1%) were more urgent than the prespecified triage level. The error pattern was similar when predictions were assessed against clinician ratings: 35 of 430 trials involving vignettes rated as emergencies by at least 75% of clinicians were under-triaged (8.1%). AI chatbots recognized most psychiatric emergencies but still missed clinically important cases and frequently over-triaged less urgent presentations. Further evaluations should examine how triage performance changes when clinically relevant information must be elicited through conversation.

**ИИ:** + · обе модели · клиническая оценка · Chatbots assign psychiatric triage urgency to clinical vignette messages; their outputs are compared with prespecified levels and clinician urgency ratings.

**Решение:** =

---

### 878 · R6058

**CALM-IT: Enhancing Synthetic Motivational Interviewing Dialogue Quality with Conversational Dynamics**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.10085

Conversational dynamics describe how rapport, emotion, and goals change over a dialogue. These changes are important in therapeutic conversations, where they can influence when and how therapists intervene. However, large language model (LLM)-based synthetic therapeutic dialogue generators rarely track how these properties evolve together, which may limit the quality of longer conversations. We introduce CALM-IT, a dual-agent framework that tracks client states and therapist-side inferences to guide strategy selection and utterance generation. We evaluate synthetic Motivational Interviewing (MI) dialogues using automated Motivational Interviewing Treatment Integrity (MITI) ratings, conversational metrics, and comparisons across dialogue lengths, with ratings from four licensed psychologists providing support for key findings. Across 8,232 dialogues covering 686 grounded scenarios, four frameworks, and three target lengths, CALM-IT achieves the highest mean scores on all four MITI 4.2 global ratings and shows the smallest aggregate change in quality between short- and long-form conditions. CALM-IT also achieves the highest simulated client redirection acceptance rate (64.3\%), with its strongest redirections followed by increased change talk and reduced sustain talk. Ablation experiments show that removing conversational dynamics components reduces dialogue quality. Together, these results suggest that explicitly modeling conversational dynamics can improve the quality and consistency of long-form synthetic MI dialogues. 55 pages

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · The paper generates synthetic MI dialogues; LLM MITI ratings sit alongside ratings from licensed psychologists, but LLM–human agreement on the same dialogues is unclear.

**Решение:** =

---

### 879 · R6067

**Using large language models to analyze student reflections on generative AI in graduate coursework**

2026 · Discover Education · journalarticle, review, article · en · https://doi.org/10.1007/s44217-026-02231-0

This exploratory study examines graduate students’ perceptions of generative AI use in coursework and evaluates the feasibility of using large language models (LLMs) to support thematic coding of brief open-ended responses. Students ( n = 20) enrolled in a systems analysis and design course completed a post-course survey consisting of Likert-scale items and eight open-ended questions, six retrospective and two prospective or hypothetical. Quantitative responses were summarized descriptively, while qualitative responses were independently coded by two human researchers and two LLMs (GPT-4o and Claude 3.7 Sonnet) using a shared, human-developed codebook. Inter-rater reliability was assessed using Cohen’s and Fleiss’ kappa. Students reported high levels of engagement, motivation, perceived learning support, and perceived efficiency when using course-specific LLM applications; however, the study did not assess objective learning outcomes. Human-human agreement ranged from moderate to almost perfect (κ = 0.52–0.84), whereas average human-LLM agreement was lower and more variable (κ = 0.36–0.62). Claude aligned more closely with the human coders than GPT-4o across all eight questions when the two human-model kappas were averaged. Agreement was highest for concrete, task-focused prompts and lower for several reflective and prospective prompts, where the LLMs missed human-identified themes, fragmented broad themes into narrower subcodes, or assigned substantive meaning to non-responses. Hybrid intelligent feedback is used as a retrospective sensitizing framework rather than as a prospectively operationalized intervention. The findings support a bounded role for LLMs in qualitative educational research: models can assist with screening, discrepancy detection, and code suggestions, but human researchers remain necessary for contextual interpretation, validation, and adjudication.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o and Claude applied a human-developed codebook to student open-ended reflections (human-LLM kappa reported), but it is unclear whether perceptions of AI use count as a psychological construct.

**Решение:** =

---

### 880 · R6068

**The Patients' Voice in Clostridioides difficile Infection: Large Language Model-Assisted Thematic Analysis of Patient Testimonials.**

2026 · Open forum infectious diseases · journal article, preprint, med · eng · https://doi.org/10.1093/ofid/ofag650

Background Clostridioides difficile infection (CDI) imposes a burden that extends well beyond the gastrointestinal tract, yet existing outcome measures only partially capture the patient experience. We used frontier large language models (LLMs) on patient and caregiver narratives at scale to describe how burden shifts with disease course. Methods We analyzed 189 testimonials from the Peggy Lillis Foundation corpus, sorted into four cohorts with recurrence ( r ) and fulminant ( f ) severity as axes (rfCDI, fCDI, rCDI, non-rfCDI). Two independent LLMs coded eight thematic domains, four fulminant flags, thirteen emerging semantic fields, the dominant dimension, and narrative arcs. Two clinicians independently coded a subset for inter-rater reliability (PABAK, Gwet’s AC1). Results Treatment trajectory was the dominant theme in recurrent disease, whereas death and near-death dominated non-recurrent fulminant narratives. Psychological burden was near-universal in fulminant disease (98.0% in rfCDI, 97.2% in fCDI). Caregiver and bereavement content concentrated in fCDI (66.7%). Diagnostic failure was frequent across recurrent cohorts (47.6 - 56.1%). Bacteriotherapy tracked recurrence (60.2% rfCDI versus 5.6% fCDI). Financial, mental-health, and caregiver burdens were prominent and are currently unaddressed by guidelines. Human-human reliability was substantial (PABAK 0.79 for semantic fields, 0.76 for domains); arc coding was least reliable. Conclusions Patient narratives reveal a course-dependent, multidimensional burden in CDI. Concrete gaps exist between what patients prioritize, what guidelines recommend, and what therapy access provides. Frontier-LLM coding, validated against clinicians, offers a reproducible route to translate these priorities into research, care, and policy. Key Points Patient narratives reveal a course-dependent CDI burden: recurrence organizes around treatment, fulminant disease around survival, and bereavement. Psychological, financial, and caregiver domains important to patients remain largely unaddressed by current guidelines.

**ИИ:** разошлись — Opus + (кодирование по кодбуку: LLMs coded patient narratives for burden domains, including psychological burden; validated against independent coding of a subset by two clinicians.); Sonnet ? (неясно, сравнивали ли с людьми: LLMs coded patient narratives into thematic domains (including psychological burden), and clinicians coded a subset. The abstract reports only human-human reliability, so LLM-human agreement is unclear.)

**Решение:** +

---

### 881 · R6090

**What Users Cannot See: Evaluating LLM Emotional Support Beyond User Preference**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.21569

People increasingly turn to LLMs for emotional support, yet common evaluations reward responses that feel helpful and may miss consequential response behaviors. We introduce a theory-informed measurement framework that decomposes LLM emotional-support responses into Soothe (affective comfort), Reframe (cognitive perspective-shift), and Endorse (agreement with a user's causal or moral framing). Across 9,000 GPT-5.6 responses to 3,000 venting and advice-seeking Reddit posts, friend- and therapist-style personas both increased Soothe relative to default but moved Reframe and Endorse in opposite directions: friend prompting increased Endorse and reduced Reframe, a pattern that could reinforce users' existing appraisals and plausibly contribute to escalation risk, whereas therapist prompting did the reverse. Two independent LLM judges substantially agreed with clinically trained raters, yet lay raters detected only 60% of expert-confirmed Endorse instances and rated the personas similarly helpful and desirable. Preference-based evaluation thus has a blind spot: supportive presentation can obscure appraisal-reinforcing, potentially escalatory behavior.

**ИИ:** + · обе модели · LLM-судья · LLM judges coded emotional-support responses for Soothe, Reframe and Endorse, and their ratings were checked against clinically trained raters.

**Решение:** =

---

### 882 · R6103

**Bootstrap Wayfinding Questions to Elicit Emotion Shift Reasoning With Large Language Models**

2026 · IEEE Transactions on Affective Computing · journalarticle, article · https://doi.org/10.1109/taffc.2026.3684445

Emotions are integral to communication, and understanding emotions is critically important for healthcare applications such as mental well-being and empathetic support. However, in conversational exchanges, emotions constantly shift as conversations unfold. Existing studies on reasoning about emotion shift triggers (ESR) require extensive manual annotation of both utterance-level emotion labels and emotion shift triggers. In this research, we propose a novel approach, the Wayfinding Instruction Tuning (WIT) framework, to tackle the ESR challenge in a more efficient manner with minimal dependency on emotion labels. WIT employs a large language model (LLM) to generate sequences of dynamic, context-sensitive wayfinding questions designed to guide the instruction tuning of another LLM on the ESR task. In contrast to conventional prompting, our key innovation is a structured wayfinding prompting strategy, which systematically decomposes the ESR process into carefully designed sub-questions. Together with their ground-truth-aligned answers, these sub-questions guide the model to learn how to detect changes in emotion and identify their triggers. Our experiments show that, even when fine-tuned on a medium-sized dataset of 100 training instances, using only pre- and post-shift emotion labels, WIT can directly predict emotion shifts without first identifying the emotion of each utterance. This design avoids intermediate emotion classification and its associated error propagation, a common issue in two-step pipelines. WIT achieves comparable performance (F1: 0.749 vs. 0.760) to state-of-the-art supervised models while requiring only shift-boundary labels during training and zero annotation at inference, providing a practical alternative when complete utterance labels are unavailable.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Fine-tuned LLM detects emotion shifts and triggers in conversations, scored against human-annotated ground-truth labels (F1 reported).); Sonnet ? (другое: LLM fine-tuned to predict emotion shifts and triggers in conversations, evaluated against annotated labels; it is a method paper, and it's unclear whether the data counts as psychological text with human coding.)

**Решение:** +

---

### 883 · R6114

**Centering Patient Voices in Lupus Pain: A Biopsychosocial Analysis of Reddit Narratives Using Large Language Models.**

2026 · Arthritis care & research · journal article, research support, n.i.h., extramural, research support, non-u.s. gov't · eng · https://doi.org/10.1002/acr.25687

OBJECTIVE: Patients with chronic illness share their experiences in online communities and generate rich data on pain management. This study applied natural language processing methods, including large language models (LLMs), to Reddit discussions from lupus communities to characterize multidimensional pain experiences framed in the biopsychosocial model. METHODS: We extracted Reddit posts from the r/Lupus and r/LupusSupport subreddits posted from June 9, 2010, through December 31, 2023. Pain-related posts were identified using a clinically informed pain lexicon. Topic modeling was used to identify thematic patterns, which were then compared with structured summaries generated by LLM instructions that were fine-tuned using the biopsychosocial model of pain. Two reviewers conducted content analysis of the LLM-generated summaries, evaluating thematic accuracy and coverage. RESULTS: Data from Reddit included 31,785 posts from 10,857 authors. We identified common pain complaints, management strategies, and sociocultural, affective, and nociplastic dimensions of pain. Instruction fine-tuned LLMs produced structured summaries with an average thematic accuracy score of 3.1 of 4 (kappa = .09) and content coverage score of 2.9 of 4 (kappa = .38). Sociocultural features presented in 123 posts (33.8%), including peer support and validation (n = 106) and provider interactions or access issues (n = 35). Nociplastic pain presented in 205 posts (56.3%). CONCLUSION: Natural language processing methods can be used to extract rich, multidimensional insights into pain experiences from online communities focused on lupus. These approaches highlight the psychological, social, and cultural facets of pain that may be underrepresented in clinical settings, supporting more patient-centered approaches to care in rheumatology.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM structured per-post biopsychosocial pain coding; reviewers rated accuracy and coverage. Unclear whether humans independently coded the same posts.); Sonnet -2 (люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает: LLM generated summaries of Reddit lupus posts, and two reviewers rated the summaries' accuracy and coverage. No LLM coding of the same texts was compared with human coding.)

**Решение:** -

---

### 884 · R6117

**A bimodal large language model reduces misalignment in patient education: A double-blinded randomized trial.**

2026 · Med (New York, N.Y.) · journal article, randomized controlled trial, journalarticle · eng · https://doi.org/10.1016/j.medj.2026.101263

BACKGROUND Effective patient education requires accurate communication aligned with patients' emotional and semantical needs. Text-based large language models (LLMs) lack access to non-verbal cues, which may contribute to misaligned responses. METHODS We evaluated emotional and semantic misalignment in a text-based LLM using 64,200 utterances from 16,583 patient education cases across six departments and three centers. Dolphin was developed integrating text and audio cues and evaluated through emotion recognition, semantic consistency assessment, branch-level ablations, and a double-blinded randomized trial against a matched text-based LLM comparator (Chinese Clinical Trial Registry: (ChiCTR2500095933). FINDINGS The text-based LLM showed emotional misalignment in 36.7% of responses and semantic misalignment in 28.3% of cases, with higher misalignment under greater burden. Dolphin outperformed the text-based LLM in emotion recognition accuracy (0.886 vs. 0.713) and semantic consistency (84.9% vs. 82.1%; both adjusted p < 0.001). Ablations supported contribution of audio branches. Dolphin received higher expert ratings than the text-based LLM and human educators (all p < 0.001). In 555 patients, Dolphin was associated with greater patient satisfaction (98.6% vs. 93.8%), suggestion acceptance (76.1% vs. 58.9%; p < 0.001), proactive disclosure (44.6% vs. 26.5%; p < 0.001), and fewer 7-day unplanned recontact (12.9% vs. 22.9%; p = 0.002). No unsafe recommendations or safety events were identified. CONCLUSIONS Compared with text-based LLM, Dolphin improved emotional-semantic alignment and patient-education outcomes, supporting bimodal alignment as a strategy for reducing misalignment-driven communication failures. FUNDING National Natural Science Foundation of China, State Key Laboratory Special Fund, and Chinese Academy of Medical Sciences Innovation Fund.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: LLM emotion recognition accuracy on patient utterances is reported, but the abstract does not say whether the reference emotion labels came from human annotators.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Develops a multimodal LLM for patient education and tests it in an RCT; experts rate LLM outputs, with no LLM coding against human labels.)

**Решение:** -

---

### 885 · R6118

**A retrieval-augmented generation large language model framework for accurate dementia identification from electronic health records.**

2026 · medRxiv : the preprint server for health sciences · journal article, preprint, ppr · eng · https://doi.org/10.64898/2026.01.24.26344477

Objective: Accurate and scalable dementia phenotyping from electronic health records (EHRs) is foundational for population-level research, risk prediction, and learning health system interventions. Traditional rule- and keyword-based approaches are limited by inconsistent documentation and inability to capture clinical nuance. We aim to develop and evaluate a framework that leverages large language models (LLMs) with retrieval-augmented generation (RAG) to overcome these limitations and improve dementia identification from real-world EHR data. Methods: Using EHR data from the Mass General Brigham health system, we first assembled a cohort of adults with potential dementia based on diagnosis codes, problem lists, dementia-related medications, and free-text note mentions. A subset of candidate cases underwent detailed manual chart review to assign gold-standard dementia status. With this labeled sample, we implemented and compared three approaches for dementia ascertainment: (1) a rule-based classifier leveraging structured EHR data, (2) large language models (LLMs) applied to keyword-filtered clinical note excerpts, and (3) a RAG-based LLM framework that integrates retrieved, context-rich note snippets. Within each approach, we evaluated multiple configurations of embedding models, retrieval methods, LLMs, structured-data inclusion, and prompts to identify the best-performing classifier. Performance was assessed using standard classification metrics, including sensitivity, specificity, positive predictive value (PPV), and F1 score, and supplemented by qualitative error analyses to characterize common sources of false positives and false negatives across methods. Results: The RAG-based classifier achieved the highest performance (F1=0.933, sensitivity=91.1%, PPV=95.5%) compared to rule-based (F1=0.823, sensitivity=81.1%, PPV=83.5%) and keyword-filtered LLM (F1=0.903, sensitivity=91.7%, PPV=88.6%). Including ICD codes alongside free text in the RAG-based LLM pipeline significantly reduced the PPV and modestly decreased F-1 score. Error analysis revealed that structured-code dependence contributed to false positives, whereas unrecognized contextual cues in notes drove false negatives. Conclusion: A RAG-based LLM pipeline without structured ICD codes improved dementia ascertainment from EHR data compared with ICD-based rules and keyword-based filtering. This approach can enhance dementia case identification and support patient care, predictive modeling and risk analysis.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM classifies dementia status from clinical notes against manual chart-review labels; unclear whether dementia phenotyping counts as a psychological construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM identifies dementia case status from EHR notes against chart review; a medical diagnosis phenotyping task, not coding of a psychological construct.)

**Решение:** -

---

### 886 · R6121

**Complementing Traditional Human-Subject Surveys with LLM-Based Observational Surveys: A Use Case in Developing and Testing Dependency on GenAI**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.7443438

Traditional human-subject surveys are a cornerstone of Information Systems (IS) research for testing theoretical frameworks involving socio-technical and psychological constructs, yet their reliance on researcher-elicited and self-reported data introduces well-known limitations. Is there an approach to utilize the rich observational data to examine the carefully developed, multi-construct theoretical framework that is often tested by a traditional survey? Leveraging the semantic reasoning capabilities of large language models (LLM), we develop the method of LLM-based observational survey (LOS), a complementary research design to traditional survey design that operationalizes theoretically grounded constructs from naturally occurring digital traces. Whereas emerging LLM-based annotation approaches primarily use LLMs to classify or measure individual constructs, LOS moves LLMs from a tool for annotating data to an integral component of research design. Specifically, LOS translates the entire theory-testing architecture of a traditional survey (including sampling logic, construct definitions, measurement items, temporal structure, hypothesized relationships, and empirical estimation) into an observational design based on naturally occurring digital traces. By interpreting heterogeneous natural-language expressions against theoretically specified construct definitions and measurement semantics, LLMs enable multi-construct theory testing that would be difficult to accomplish using conventional text-analytic approaches. LOS thus provides a distinct and complementary pathway for examining theoretical frameworks without directly eliciting responses from research participants.&amp;nbsp; &lt;div&gt; &lt;br&gt; &lt;/div&gt; &lt;div&gt; We demonstrate LOS by examining how generative AI (GenAI) usage influences users' broader life outcomes. Drawing on technology dependency theory, we theorize two mediating pathways: functional dependency, reflecting reliance on GenAI for task execution and decision support, and emotional dependency, reflecting psychological attachment to GenAI for social and emotional support. We test the same theoretical framework using a two-wave human-subject survey of 290 GenAI users and an aligned LOS based on naturally occurring posts and comments from Reddit users. The two designs yield largely convergent evidence despite fundamentally different sampling and measurement processes. Our demonstration validates the potential of LOS to complement traditional surveys with observational evidence and reveals important tradeoffs in construct observability and LLM-based measurement. Our study broadens the methodological toolkit for theory testing in IS research and illustrates a new form of inquiry made possible by human-AI collaboration. &lt;/div&gt;

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · An LLM rates psychological constructs (emotional dependency) in Reddit posts; a human-coding validation subsample is possible but not stated.

**Решение:** =

---

### 887 · R6136

**Decision-Making About Health Behaviors Among Patients With Cardiometabolic Multimorbidity Undergoing Percutaneous Coronary Intervention: A Qualitative Study Using Patient Personas, Journey Mapping, and Artificial Intelligence-Assisted Analysis**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-10704903/v1

Abstract Background Patients with cardiometabolic multimorbidity undergoing percutaneous coronary intervention (PCI) require long-term pharmacotherapy, risk factor control, lifestyle modification, and follow-up. Their health behavior decisions are shaped by illness perceptions, multimorbidity burden, social roles, family support, and access to health care. Patient personas and journey mapping can characterize heterogeneity and stage-specific experiences, whereas artificial intelligence (AI)-assisted analysis may support data organization and preliminary theme generation. Methods This qualitative descriptive study was conducted from July to August 2026 at a tertiary hospital in central China. Thirty-eight patients with cardiometabolic multimorbidity who underwent PCI participated in timeline-based semistructured interviews. Nonparticipant clinical observations and medical record data were also collected. Analysis was researcher-led and based on qualitative content analysis; ChatGPT 5.5, DeepSeek V3.2, and Doubao Expert Mode were used to generate provisional codes, stage-specific summaries, and analytic memos. Final themes and personas were developed by the research team through manual coding, iterative review of the source data, comparison with AI-generated provisional outputs, meaning-unit-level agreement assessment, journey-stage matrix analysis, and integration of patient personas with journey maps. Results Five decision-making personas were identified: active collaboration and risk management; limited treatment understanding and risk underestimation; multimorbidity burden and uncertain safety boundaries; work-family responsibilities and constrained implementation; and support dependence and limited resources. Across five stages—symptom onset and care-seeking decisions, admission assessment and illness understanding, PCI decision-making and preprocedural preparation, post-PCI recovery and risk reappraisal, and discharge preparation and postdischarge self-management planning—participants showed differing emotional and interpretive responses, decision-making patterns, implementation barriers, and support needs. Consensus LLM classifications showed 84.1% agreement with manual primary-category assignments (κ = 0.76), with higher agreement for explicit themes than for themes requiring interpretation of social context, latent needs, or stage-specific meaning. Conclusions Health behavior decision-making among patients with cardiometabolic multimorbidity undergoing PCI was both stage-specific and heterogeneous. Embedding patient personas within journey maps may help identify differentiated nursing needs and inform stratified, stage-based, and context-sensitive transitional care. AI may support qualitative analysis, but interpretation should remain researcher-led, traceable to the source data, and governed by explicit data-protection procedures.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · LLM classifications of interview meaning units on health-behavior decision-making compared with manual coding: 84.1% agreement, κ = 0.76.

**Решение:** =

---

### 888 · R6146

**Predicting Disengagement from Therapy Based On First-Session Transcripts**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-9717903/v1

Abstract Dropout from psychotherapy is common, often occurring early in treatment, but predictors of disengagement from care remain poorly understood. In this retrospective cohort study of 31,146 patients receiving care through a digital mental health platform, we examined whether language from first-session transcripts could be used to predict subsequent dropout. We combined clinical, demographic, and utilization variables with features derived from transcripts using natural language processing and large language models. Models incorporating transcript-derived features improved prediction compared with pre-session data alone (area under the curve, 0.642 vs 0.569). Provider behaviors, particularly whether follow-up care was clearly discussed, were strongly associated with retention, while patient-level constructs such as motivation, ambivalence, and therapeutic alliance were not consistently predictive. Although overall discrimination was modest, transcript-derived features improved identification of high-risk patients. These findings suggest that early-session dynamics contain actionable signals of engagement and may support scalable approaches to improving retention in mental health care.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · An LLM rated alliance, motivation and ambivalence in therapy transcripts to predict dropout; unclear if these ratings were checked against human coders.

**Решение:** =

---

### 889 · R6165

**Cross-Protocol Personality Assessment with LLMs: Aligning Behavioral Evidence with Human Ratings**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.16050

Personality assessment from asynchronous video interviews (AVIs) plays a crucial role in recruitment by enabling standardized and behaviorally grounded evaluation for job applicants. However, most of the previous works are confined to a single interview protocol. Independently collected protocols differ in question sets and question-trait mapping. Thus, the human-rated evidence from one protocol cannot be used directly under another. To address this limitation, we propose the Cross-protocol Evidence-grounded Personality Assessment (CEPA) framework, which aligns behavioral representations across interview protocols. CEPA addresses protocol heterogeneity by projecting source behavioral records into the target protocol's construct-oriented representation space. It retrieves behaviorally relevant and personality-complementary human-rated exemplars to ground an ensemble of LLM raters, which enables behavior-to-personality associations without target-specific supervision. In cross-protocol experiments, CEPA reduces average mean squared error (MSE) by 43.8% (Forward) and 17.0% (Reverse) relative to the strongest baseline. Our empirical experiments show that human-rated evidence from one protocol can support personality assessment under another without target-specific supervision or retraining.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: An ensemble of LLM raters scores personality from interview behaviour and is evaluated against human ratings (MSE). Need to check whether the input is transcript text.); Sonnet ? (неясно, кто ставил эталонные метки: LLM raters score personality from video-interview behavioral records against human ratings (MSE); unclear whether input is text and whether labels are observer ratings or self-report.)

**Решение:** +

---

### 890 · R6185

**Towards Aligning Multimodal LLMs with Human Experts: A Focus on Parent–Child Interaction**

2026 · CHI Conference on Human Factors in Computing Systems · book, journalarticle, conference · https://doi.org/10.1145/3772318.3791267

While multimodal large language models (MLLMs) are increasingly applied in human-centred AI systems, their ability to understand complex social interactions remains uncertain. We present an exploratory study on aligning MLLMs with speech-language pathologists (SLPs) in analysing joint attention in parent-child interactions, a key construct in early social-communicative development. Drawing on interviews and video annotations with three SLPs, we characterise how observational cues of gaze, action, and vocalisation inform their reasoning processes. We then test whether an MLLM can approximate this workflow through a two-stage prompting approach, separating observation from judgement. Our findings reveal that alignment is more robust at the observation layer, where experts share common descriptors, than at the judgement layer, where interpretive criteria diverge. We position this work as a case-based probe into expert-AI alignment in complex social behaviour, highlighting both the feasibility and the challenges of applying MLLMs to socially situated interaction analysis. Accepted at CHI 2026 Full Papers

**ИИ:** ? · обе модели · другое · A multimodal LLM's joint-attention judgements are compared with speech-language pathologist annotations, but the input is mainly video rather than text.

**Решение:** =

---

### 891 · R6187

**Rolling With Resistance: Preference-Optimized LLM Counselors Can Trade Goal Persistence for Relational Attunement in Motivational Interviewing**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.28814

In Motivational Interviewing (MI), a client's sustain talk (arguments for the status quo) calls for the counselor to roll with resistance, a move that can fail in two opposite ways: capitulation (abandoning the change agenda to preserve rapport) or confrontation (arguing or directing, overriding the client's autonomy). We introduce a two-axis evaluation of counselor responses, anchored in the Motivational Interviewing Treatment Integrity (MITI) code, Goal Persistence (GP) and Relational Attunement (RA), yielding a four-quadrant framing in which rolling with resistance is high on both, and we ask whether penalizing one failure through preference optimization teaches rolling with resistance or provokes its opposite. From the expert-annotated AnnoMI corpus we build topic-disjoint Direct Preference Optimization data whose preference sets differ only in which failure is rejected, using on-policy negatives. An automatic judge, validated against AnnoMI's expert labels and rechecked by trained human coders, scores blind pairwise win-rates against each base under a firewall in which disjoint model families generate, label, and judge. Across three aligned instruction models spanning the Qwen and Llama families, penalizing confrontation reliably lowers goal persistence below parity, on every base and in every seed run, a robust cost, whereas the attunement gain is base-dependent, present on two of the three bases but absent on the third. Penalizing capitulation is inert, because these models rarely capitulate on-policy, so the trade is gated by each base's failure profile. A prompt-only control raises attunement without the goal-persistence cost, locating the cost in the optimization rather than in attunement itself.

**ИИ:** + · обе модели · LLM-судья · An automatic LLM judge of MITI-anchored counselor responses was validated against AnnoMI expert labels and checked again by trained human coders.

**Решение:** =

---

### 892 · R6190

**Detecting Confusion Comments with LLMs**

2026 · 2026 Intelligence in Business and Industry (IBI) · review · https://doi.org/10.1109/ibi68858.2026.11604063

Pull Request discussions are central to collaborative software development, yet they often contain signals of confusion that slow down review cycles and obscure decision-making. Prior work has examined confusion in code reviews using heuristic rules, manual annotation, and qualitative analysis, demonstrating its prevalence and impact on review effectiveness, which struggle to capture semantic hints in natural language comments.In this paper, we investigate whether a lightweight large language model can reliably detect confusion in human-authored PR comments. We compare its performance against classical machine learning classifiers using a dataset of annotated code reviews comments. We apply the model to real world pull request discussions to explore its practical usefulness in identifying confusion at scale.Our results show that large language models can effectively capture linguistic signals of confusion and provide meaningful explanation of reviewer uncertainty. These findings suggest promising directions for improving developer-support tools that enhance understanding during code review.

**ИИ:** ? · обе модели · неясен конструкт · An LLM detects confusion (a cognitive state) in human-annotated code-review comments. It is unclear whether confusion in software-engineering text counts as a psychological construct.

**Решение:** =

---

### 893 · R6200

**Cross-Scale Transfer Learning for Depression Severity Prediction: From PHQ-8 to HAMD-17 Across Languages and Clinical Paradigms**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.28430

This work addresses continuous depression-severity score prediction from clinical interview transcripts under data scarcity. We propose a sequential low-rank adaptation (LoRA) protocol for cross-scale transfer: a Qwen3 backbone with a bounded regression head is first fine-tuned on the English DAIC-WOZ dataset (189 avatar-mediated sessions, PHQ-8), and the adapter then initializes fine-tuning on the Chinese PDCH dataset (100 real clinical consultations, HAMD-17), where a reinitialised, scale-specific head predicts the clinician-assigned score. All configurations use patient-level stratified 5-fold, 2-repeat cross-validation. On the data-scarce HAMD-17 target, the sequential protocol attains the best point-estimate MAE , RMSE, and macro-$F_1$ on both 0.6B and 1.7B backbones, outperforming target-only training and non-LLM baselines---4.96/6.59/0.36 with Qwen3-0.6B and 4.38/5.62/0.46 with Qwen3-1.7B. Ablations suggest that correctly aligned source supervision gives the best point estimates (unsupervised exposure and shuffled-label controls also show partial gains), that native-Chinese target input outperforms machine-translated English input, and that the reversed order yields no clear gain within run-to-run variance. The study is an exploratory, single-site internal evaluation: it does not establish screening or diagnostic utility, nor separately identify the contribution of the scale, language, or paradigm shifts. To our knowledge, no prior study evaluates this specific DAIC-WOZ-to-PDCH sequential transfer setting. preprint to ICASSP 2027

**ИИ:** разошлись — Opus + (клиническая оценка: Fine-tuned Qwen3 predicts clinician-assigned HAMD-17 severity from clinical interview transcripts; reports MAE and F1 against those clinician ratings.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): Fine-tuned Qwen3 regression predicts depression scores (PHQ-8/HAMD-17) from transcripts; no LLM coding compared with human coding of text.)

**Решение:** +

---

### 894 · R6208

**How Large Language Models Construct Emotional Metaphors: A Human-Centered Study of Controllable Concept Blending**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-981-92-6913-6_36

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; title suggests LLM generation of emotional metaphors with human evaluation, possibly an LLM–human rating comparison.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: No abstract available. Title suggests LLMs generate emotional metaphors, with humans evaluating them. This is generation, not LLM coding of text against human labels.)

**Решение:** ?

---

### 895 · R6209

**AnthroDial: Benchmarking LLM Anthropomorphism in Autonomous Social Interaction**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.37853

Large language models (LLMs) are increasingly deployed as social agents, yet credible human-like interaction requires more than fluent responses or persona consistency. Agents must autonomously decide whether, when, and how to communicate while adapting to evolving contexts, goals, and relationships. Existing research, however, lacks a unified approach to enabling, evaluating, and improving such capabilities in continuous, open-ended interaction. We introduce AnthroDial, a unified framework for developing anthropomorphic social agents from three complementary aspects: MindFlow, a lightweight interaction harness that enables autonomous, asynchronous, and adaptive communication through a dynamic Mind Buffer; CAPS-Eval, a theory-grounded framework for evaluating cognitive, affective, and behavioral dimensions of anthropomorphic interaction; and a scalable training paradigm that combines SEEDS for environment expansion with DiAPO for adaptive capability optimization. We further construct evaluation datasets covering everyday communication, game interaction, and long-horizon character interaction. Extensive experiments across diverse models and scenarios demonstrate improved interaction autonomy and naturalness, validate the reliability, discriminativeness, and agreement with human rankings of CAPS-Eval, and confirm the effectiveness of our training paradigm. Together, these components provide a unified framework for developing credible human-like social agents in open-ended interaction. 26 pages, 8 figures, 16 tables

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM judge (CAPS-Eval) scores the cognitive, affective and behavioral human-likeness of agent dialogue against human rankings; unclear if this is a psychological construct.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Framework for anthropomorphic social agents and evaluating LLM interaction; not coding psychological text against human coders, though an LLM evaluator is compared with human rankings.)

**Решение:** -

---

### 896 · R6214

**Multimodal large language models for ADOS-M1 behavioral assessment**

2026 · Neurocomputing · article · en · https://doi.org/10.1016/j.neucom.2026.135024

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; multimodal LLMs scoring ADOS autism assessment, possibly against clinician scores, but input may be video rather than text.

**Решение:** =

---

### 897 · R6223

**Measuring Emotion In Surveys: Comparing Self-Reports, Human Coders, And Large Language Models**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.7535980

Emotions are theoretically important in many areas of political science, yet measuring emotions in surveys remains challenging. Using experimental data from Spain, we evaluate three common approaches to measuring emotions: closed-ended self-reports, human coding of open-ended responses, and automated coding of open-ended responses (using six large language models, LLMs). We first examine distributions, agreement, and distances across measurement approaches, showing that conclusions about human-LLM correspondence depend partly on how individual human judgments are aggregated. Human and LLM measures exhibit substantial correspondence in describing overall emotional profiles while differing systematically in absolute levels for specific emotions, demonstrating that correspondence does not imply interchangeability. We then exploit a randomized blame attribution treatment to assess which approaches identify theoretically expected differences in emotional expression. As expected, the treatment increases self-reported anger and disgust in the full sample. Analyzing open-ended responses, LLM-based measures consistently identify greater anger and, less uniformly, greater disgust among treated respondents. This pattern of results is consistent across individual models and alternative LLM aggregation strategies despite significant differences in baseline scale usage. While our results suggest substantial correspondence across coding approaches, we conclude by arguing that the ideal approach depends on the type of inferences researchers seek to make.

**ИИ:** + · обе модели · кодирование по кодбуку · Six LLMs coded emotions in open-ended survey responses and were compared with human coders, with agreement reported.

**Решение:** =

---

### 898 · R6224

**Exploring the future of psychometrics from a Large Language Model perspective: A case study analysis**

2026 · Computers in Human Behavior Reports · article · en · https://doi.org/10.1016/j.chbr.2026.101060

This article explores the applicability of LLMs in psychometrics. We first identify and evaluate four deployment scenarios for LLMs in psychological assessment: (1) preliminary screening, (2) psychologist’s assistant, (3) autonomous psychological agent, and (4) psychological agent with expert oversight, discussing their respective benefits, risks, and ethical considerations. In the experimental part, we assess the ability of four LLMs: GPT-3.5, GPT-4, Mixtral-8x7B, and OpenChat-3.5 to identify nine cognitive emotion regulation strategies in a dataset of 515 annotated Polish-language trauma narratives. Two tasks were designed: a multiclass classification task and a binary yes/no verification task. GPT-4 achieved the best overall performance, reaching an F1 score of 0.442 in the multiclass task and 0.346 in the binary task, while also demonstrating the highest TNR of 0.838. Nevertheless, all models exhibited a tendency towards overinterpretation and struggled to distinguish between conceptually similar strategies. These findings suggest that current LLMs are not yet suitable for autonomous clinical deployment and should be integrated into psychometric practice only under qualified human oversight. • LLM roles in psychometrics: screening, assistant, autonomous and expert-supervised agent. • LLMs can not detect how individual manage stress via cognitive effort from text alone. • GPT-4 and GPT-3.5 Turbo were the most accurate models in detecting strategies. • Mixtral and OpenChat were the two most conservative models that did not overinterpret the presence of the strategy.

**ИИ:** + · обе модели · кодирование по кодбуку · Four LLMs identified cognitive emotion regulation strategies in 515 annotated trauma narratives, with F1 computed against human annotations.

**Решение:** =

---

### 899 · R6237

**They, Not It: Perceived Entitativity in Public Discourse About Multi-Agent AI Systems**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/kuv5a

This study examines how the public talks about multi-agent AI systems online, focusing on perceived entitativity, the degree to which a collection of AI agents is construed as a coherent, unified group entity. The empirical case is Moltbook, a recently launched multi-agent AI platform whose architecture (a social network composed of AI agents) makes the question of groupness unusually salient. Using a brand-name retrieval pipeline across Reddit, YouTube, and X within a single observation window, we collect substantive public discourse about the platform, gate items for relevance with an LLM classifier validated against blinded human coders, and code retained items for entitativity markers, valence and discrete emotion, dominant evaluative frame, and governance orientation. The study extends ongoing work on perceived entitativity of AI agents from controlled survey contexts to naturalistic online discourse, and provides a baseline picture of how the group-level construal of AI emerges outside the lab.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: OSF pre-registration (protocol); planned LLM relevance classifier validated against human coders, but no results reported.); Sonnet ? (неясен конструкт: Pre-registration: LLM relevance classifier validated against blinded human coders; unclear whether the LLM also codes entitativity and emotion with human comparison.)

**Решение:** -

---

### 900 · R6275

**SuiChat-CN: Benchmarking Contextual Suicide Risk Assessment in Chinese Group Chats**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.27911

Suicide is a critical global public health challenge, causing approximately 720,000 deaths each year and calling for timely, effective prevention strategies. Existing computational studies primarily focus on post-based social media platforms such as Twitter and Weibo, leaving instant messaging environments such as Telegram underexplored. Yet group chats pose distinct challenges: messages are short, fragmented, multi-party, and often rely on implicit or culturally specific expressions, making isolated post-level analysis insufficient. We introduce SuiChat-CN, a Chinese group-chat benchmark for contextual suicide risk assessment. We collect public Telegram group-chat data, construct coherent conversational segments through signal-word extraction and bidirectional context expansion, and annotate user risk levels with an expert-validated, LLM-assisted paradigm. SuiChat-CN contains 13,312 contextual segments from 1,406 users, covering 258,228 raw chat messages. Extensive experiments with PLMs and more than 40 LLMs demonstrate that contextual information is essential for reliable risk assessment, while fine-tuning and partial-context evaluation further reveal the challenges of early detection in multi-party conversations. Due to ethical and sensitivity concerns, the dataset is not publicly released but will be shared with accredited mental health and suicide-prevention research institutions upon reasonable request.

**ИИ:** + · обе модели · бенчмарк с метками людей · Suicide risk benchmark from group chats with expert-validated labels; over 40 LLMs evaluated against them. Labels were LLM-assisted, so check how humans were involved.

**Решение:** =
