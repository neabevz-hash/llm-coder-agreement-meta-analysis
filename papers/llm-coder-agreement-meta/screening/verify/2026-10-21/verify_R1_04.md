# Проверка с метками ИИ, часть 4

Записи 451–600 из 1304, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

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

### 451 · R1291

**The Effect of Emotional Context on Large Language Models' Endorsement of Premature Decisions: Comparing Emotional Vulnerability Across Six Commercial Models**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.27465

As large language models (LLMs) are increasingly used for everyday decision-making advice, whether a model shifts the direction of its advice according to the user's emotional state has become an important safety problem. We test whether emotional expression increases a model's endorsement (encouragement to proceed) when a user, holding the same objective information, is overconfident about a premature decision (e.g., quitting a stable job on weak evidence). As a key control, we include a no-emotion multi-turn (neutral) condition that holds factual content and the number of conversational turns constant, isolating the effect of emotion from that of conversation length. We exposed six commercial models (top-tier and mid-tier models from OpenAI, Anthropic, and Google) to three scenarios (career change, business expansion, emigration) across three conditions (cold/neutral/distress) with six repetitions each, yielding 324 conversations, and measured endorsement strength (0-100) via an eight-item rubric-based automated scoring. Emotional expression significantly increased endorsement (neutral 18.6 to distress 31.5, +12.9 points; mixed-effects $\beta = +12.9$, $p<.001$; Cohen's d = 0.51), and this was not explained by conversation length (cold-neutral difference non-significant, $p = .083$). Critically, the vulnerability varied by individual model rather than by price tier: five of six models showed a significant emotion effect, including the top-tier flagships Gemini 3.1 Pro and GPT-5.5, while only Claude Opus showed no significant change. Results were reproduced with an independent non-Google judge model ($\rho = .89$) and agreed in rank with two human coders ($\rho = .70$). Through a controlled design that separates emotion from conversational context, we show that emotional context increases LLM sycophancy even in top-tier flagship models.

**ИИ:** ? · обе модели · неясен конструкт · An LLM judge's endorsement scores of chatbot replies to distressed users were checked against two human coders (ρ=.70); unclear if endorsement counts as a psychological construct.

**Решение:** =

---

### 452 · R1292

**Assessing Llm Hallucinations And The Reliability Of Using LLms For Automated Hallucination Detection**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-9394250/v1

Abstract Large language models (LLMs) are increasingly deployed to assess, diagnose, and predict clinical symptoms and outcomes from textual data. However, prior work has shown that LLMs are susceptible to hallucinations. To date, it remains unclear whether, how, and why such hallucinations arise when LLMs are applied to clinical data situated in diverse real-world contexts. In this work, we systematically quantify the prevalence and types of hallucinations across different LLMs and examine the utility of LLMs-as-judges (LLJs) for automated hallucination assessment using real-world clinical data situated in diverse real-world contexts. Specifically, we analyzed transcripts obtained from both community controls and populations at higher risk of developing schizophrenia. Across ground-truth hallucination analyses, we find that hallucination rates vary widely, from 0.3% to 76.3%, depending on transcript type, prompting strategy, and the LLM used for classification. Diagnostic hallucinations are the most prevalent subtype, accounting for up to 50.4% of observed hallucinations. Across automated hallucination detection, LLJs demonstrate reasonable alignment with human raters, achieving up to 65.7% agreement on hallucination presence and 64.7% agreement on hallucination subcategorization. Finally, we identify that hallucinations most commonly arise when there is insufficient contextual grounding.

**ИИ:** ? · обе модели · неясен конструкт · LLMs classify schizophrenia-risk transcripts; LLM judges agree with humans on hallucinations, which may not be a psychological construct. Clinical-label comparison is unclear.

**Решение:** =

---

### 453 · R1307

**Integrating Large Language Models into Qualitative Methods in Health Services Research: A Proof-of-Concept Study.**

2026 · Research square · journal article, preprint, journalarticle · eng · https://doi.org/10.21203/rs.3.rs-9726844/v1

Abstract Background Qualitative methods are widely used in health services research to derive context-specific insights and depth of understanding. Manual coding, a foundational technique in rigorous qualitative analysis, is highly resource and time-intensive and difficult to scale. This is a particular challenge in health services research, where repeated rounds of interviews are common and rapid turnaround is often required. Natural Language Processing (NLP), specifically Large Language Models (LLMs), have shown potential to enhance efficiency in qualitative analysis. However, there is limited research providing guidance on how to integrate LLMs while maintaining rigor and trustworthiness. In this proof-of-concept study, we propose, apply, and evaluate an NLP-assisted coding method in a health services research setting. Methods We analyzed 22 interviews among public health officials, law enforcement, community organizers, and medical professionals at one California county to examine existing substance use service gaps and needs. A primarily deductive codebook was iteratively refined until two coders achieved an inter-coder reliability (ICR) > 0.95 and was applied to the transcripts using ATLAS.ti. We developed an NLP-assisted method that uses a semantic shift algorithm to segment transcripts which are then passed to GPT-4 for code assignment and explanation using the codebook and coding guidelines developed during the manual process. We evaluated the method with a quantitative assessment of agreement between human and NLP-assigned codes, a qualitative and quantitative soundness assessment by two reviewers, and a comparative efficiency analysis. Results The NLP-assisted method had moderate agreement with human coding (modified pooled Cohen’s Kappa = 0.66), and 71.8% of codes were rated as sound by reviewers. Sound codes were more often observed for high-certainty and straightforward codes, and when text chunks were semantically well defined. The NLP-assisted method had more difficulty with non-linear conversation and entity-dependent codes. Coding time was reduced significantly from ~40 hours for the traditional method to ~1 hour for the NLP-assisted method. Conclusions These findings suggest that LLMs can be effectively incorporated into qualitative processes while maintaining rigor if humans are embedded into the process. By maintaining a human-in-the-loop workflow, our methodology allows for researchers to maintain familiarity with the data, define the research question(s) and codebook, and determine if there are results that are not sound. By incorporating LLMs into the coding stage of the process, key limitations of traditional qualitative methods in health services research can be addressed, such as scalability, and resource and time limitations.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 applied a codebook to interview transcripts and was compared with human coding (kappa 0.66). The codes cover substance-use service gaps, so the construct may not be psychological.

**Решение:** =

---

### 454 · R1322

**The PAI Framework: Measuring Parasocial Attachment Patterns in AI-Child Interactions**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.19656141

The Parasocial Attachment Indicators (PAI) framework is a five-dimension instrument for measuring parasocial attachment patterns in synthetic AI-child conversation transcripts. PAI scores are produced by a cross-lab ensemble of five frontier LLM judges (Anthropic, OpenAI, Mistral, Google, Meta) with a pre-registered Cohen's kappa >= 0.700 reliability gate. This release accompanies the v0.1 preprint and includes the rubric, scoring formulas, reliability methodology, audit-chain specification, and the publicly released judge-bias audit report (n=29 calibration transcripts + n=463 production transcripts, kappa_avg = 0.85 on calibration).

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM judges score parasocial attachment in transcripts; kappa may be between LLM judges only, human calibration labels unclear.

**Решение:** =

---

### 455 · R1327

**High Agreement, Different Stories: How LLM Classifiers Reshape Demographic Patterns in Survey Data**

2026 · preprint · https://doi.org/10.31235/osf.io/85kyd_v1

What we learn from open-ended survey data depends on who—or what—does the coding. Large Language Models (LLMs) promise to democratize qualitative analysis, but do high agreement rates translate into equivalent thematic findings? This study compares eight LLMs to human annotators on a multilabel coding task using 3,200 responses from the UC Berkeley Social Networks Study, comprising over 19,000 coding decisions. Although LLM-human reliability does not match human-human reliability overall, LLMs approach human performance on simpler tasks and can serve as useful additional coders for generating consensus labels. Compared to a gold-standard human consensus, models achieve 82–97% per-category agreement, but macro F1 is lower and response-level similarity is lower still: even the best model reproduces the full human label set for fewer than 60% of responses. Yet high agreement masks thematic divergence. Models systematically over-identify themes, assigning 67% more categories per response, especially for categories requiring greater interpretive judgment.Models also show lower agreement for some demographic groups. These gaps are partly explained by response characteristics such as length, clarity, and atypicality, and some persist after controls, with implications for studies of populations whose response styles diverge from the corpus average. At the sample level, models largely preserve the overall thematic narrative: human and model category rankings correlate strongly (pooled Spearman's ρ=0.75), and top-performing models achieve approximately 80% directional agreement on demographic patterns. Concrete behavioral questions, such as reasons for moving or strategies for making friends, show especially strong alignment. Yet systematic over-classification can still shift narratives about how specific groups behave, leading researchers to report patterns that the human gold standard does not support.

**ИИ:** + · обе модели · кодирование по кодбуку · Eight LLMs vs. human coders using a multilabel codebook on open-ended Social Networks Study responses (interpersonal and behavioural themes); agreement reported.

**Решение:** =

---

### 456 · R1329

**What Does Frontier Access Buy? Benchmarking LLM Access Tiers and the Reproducibility Case for Open Weights in Survey Coding**

2026 · Center for Open Science · posted-content, preprint · https://doi.org/10.31235/osf.io/5g34x_v1

Social scientists coding open-ended survey responses with large language models (LLMs) face a tradeoff between proprietary frontier systems, cheaper commercial alternatives, and open-weight models that can be audited and self-hosted. This study benchmarks eighteen LLMs across four access tiers, from proprietary flagships to open-weight models small enough to run on a laptop, zero-shot against a human consensus on three open-ended questions from a probability-sampled U.S. panel. External validation adds a British Election Study task and an online-comment emotion task (GoEmotions), spanning five tasks in three contexts. The flagship proprietary models' average margin over their cheaper counterparts is statistically indistinguishable from zero, despite stronger general-benchmark performance. Pricing tells the same story: frontier models cost 1.3–6× more per token, yet for most of them some cheaper model is also more accurate, and the field's second-best macro F1 comes from its cheapest closed model. Open-weight models have largely caught up. The largest ones match both proprietary tiers on cell-level agreement, while on the stricter macro F1 they trail by about two points on average. They reach this at no per-call cost, with the reproducibility and data-privacy advantages of self-hosting. Both patterns hold out of domain. The leading models, closed and open alike, agree with a trained human coder about as well as the two coders agree with each other. Failure is patterned. Errors concentrate on interpretive categories where the human coders themselves disagreed, and on longer responses, penalties from which frontier prices buy little relief. The caveat is scale. Laptop-scale models show strong cell-level agreement but trail further on macro F1, so fully local deployment carries a modest, task-dependent accuracy cost. Hardware scale and question difficulty, not price or license, are the binding constraints on these tasks.

**ИИ:** + · обе модели · бенчмарк с метками людей · Eighteen LLMs benchmarked against human coders; includes GoEmotions emotion labeling task with human labels, alongside survey open-ended coding.

**Решение:** =

---

### 457 · R1331

**When Does Self-Correction Work for LLMs in Content Analysis? The Role of External Structure and Task Complexity**

2026 · Computational Communication Research · journalarticle/none, article · en · https://doi.org/10.5117/ccr2026.2.13.pipa

While Large Language Models (LLMs) have transformed content analysis, their ability to self-correct to achieve higher agreement with human coders remains contested. Recent evidence suggests LLMs fail to self-correct on reasoning tasks, but it is unclear if this limitation applies to classification, where the goal is maximizing overlap with human ground truth. We investigate iterative self-refinement, a pipeline where a model generates an initial classification, critiques its own output, and generates a final refined prediction. We test this across 14 variables (spanning framing, emotions, styles, politics, and topics) using a smaller, cost-effective model (Gemini 2 Flash) by systematically isolating the effects of codebooks versus few-shot examples. Results demonstrate a clear trade-off: refinement significantly boosts human alignment for complex, low-baseline constructs but degrades performance on simple, high-baseline tasks. Notably, a smaller model using refinement matches the accuracy of state-of-the-art reasoning models (Gemini 3 Flash) on complex tasks at a lower cost. These findings establish boundary conditions for self-correction, showing that external structure and task complexity jointly determine when refinement improves data quality.

**ИИ:** ? · обе модели · неясен конструкт · Gemini coding compared with human coders across 14 variables, emotions among them; mostly communication or political content, so the psychological relevance is unclear.

**Решение:** =

---

### 458 · R1342

**Employing Natural Language Processing for Psychotherapy Process-Outcome-Research**

2026 · osnaDocs (Osnabrück University) · dissertation/dissertation oder habilitation [doctoralthesis], dissertation · de · https://doi.org/10.48693/906

While the effectiveness and efficacy of psychotherapy has been shown in general, there is still an urgent need for improvement. One of the most promising research directions for the improvement of psychotherapy is treatment personalization, i.e., tailoring the treatment towards the patient and their specific needs, problems, motives, and challenges. Contrary to standardized treatment packages such as manualized treatment, personalization aims to select, adapt, or change treatment packages to increase the fit for the patient, as this has been shown to increase psychotherapy efficacy. Process-outcome-research can guide this process by providing an empirical basis for personalization. It allows for the identification of various predictive and causal processes that could be specifically targeted to improve outcome for a given patient. However, currently most processes are measured via questionnaire self-report, which comes with inherent limitations (e.g., burdensome, lack high resolution, rely on memory). In my dissertation project I employ Natural Language Processing (NLP) to complement questionnaire-based assessments with text data from psychotherapy transcripts. The resulting data could help bridge the gap between broad psychological processes that can be measured via questionnaires and the actual session content, aiming to identify the actual utterances that are associated with a given process. It could also be employed as part of the Routine Outcome Monitoring (ROM), providing therapists with feedback to support clinical decision making. To this end, I have conducted three proof-of-concept studies that show the utility of different NLP methods for the assessment of relevant processes. In the first study, I have employed a bottom-up topic modeling approach via the transformer-based architecture BERTopic on our sample of 552 psychotherapy transcripts. The resulting data-driven topics predicted both symptom severity and alliance on a session-level. Qualitative clusters of the topics revealed specific content that was particularly associated with higher symptom severity, especially health problems and negative experiences. Simultaneously, clusters surrounding positive experiences and scheduling were associated with lower symptom severity. In the second study, I have applied a top-down approach for the assessment of cognitive distortions on the transcript data set. Cognitive distortions were assessed via pre-defined sets of consecutive words (i.e., n-grams) in the transcripts and were employed to predict depression severity. Using mixed models to control for trait differences, significant associations with higher severity were found for personalizing, dichotomous thinking, and mental filtering. Further, by integrating explainable AI, I created a preliminary machine learning model to estimate the impact of various distortions on the predicted depression severity, allowing for a monitoring of the most important distortions for individual patients. In the future, a similar approach could help guide clinical decision making. In the third study, I employed a Large Language Model (LLM) for the automatic assessment of emotions in the transcripts. To this end, I translated a large English social media dataset (&gt;50k entries) into German which was labeled for 27 emotions and a “neutral” category. Next, I fine-tuned a pre-trained LLM on this dataset for the automatic classification of these labels. This fine-tuned LLM was then applied to our transcript data. The inferred emotions predicted both symptom severity and alliance, mostly in line with our hypotheses (i.e., positive emotions predicted lower severity and higher alliance, with opposite results for negative emotions). The results of these studies and their respective utility for process-outcome-research and personalization will be discussed in detail.

**ИИ:** разошлись — Opus ? (другое: Study 3 fine-tuned an "LLM" on human-labelled GoEmotions data, so test accuracy is likely. Unclear whether the model is a decoder or a BERT-type encoder.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): Dissertation using NLP (topic modeling, n-grams, fine-tuned emotion classifier) to predict severity and alliance; no human coding of transcripts compared with LLM ratings.)

**Решение:** ?

---

### 459 · R1364

**Prompt Engineering Emotion**

2026 · OSF Preprints (OSF Preprints) · preprint

This registration archives the materials and analysis code for the study "A validation framework for prompt-engineered generative AI as a coder of open-ended emotion responses" (Liu et al.). The deposit contains the five candidate prompts, the emotion-coding codebook, and the reliability analysis code, together with a simulated dataset that reproduces the analysis pipeline in the absence of the protected data. The interview transcripts cannot be shared because they contain potentially identifying information governed by the Mass General Brigham Institutional Review Board (protocol #2022P002247) and the NIH Data Sharing Policy. This is an archival snapshot of existing materials; the analyses reported in the paper were not preregistered.

**ИИ:** разошлись — Opus ? (другое: OSF materials deposit for an eligible study (generative AI coding emotion in interview transcripts, reliability analysis); results likely in the linked paper.); Sonnet + (кодирование по кодбуку: Archive for a study validating prompt-engineered generative AI coding open-ended emotion responses with a codebook and reliability analysis, implying human-coder comparison.)

**Решение:** +

---

### 460 · R1384

**One Question, Four Voices: How Advice for Alzheimer's Caregiving Differs Between Caregivers, Clinicians, and Large Language Models**

2026 · Proceedings of the ACM on Human-Computer Interaction · journalarticle, article · en · https://doi.org/10.1145/3816980

Online caregiver forums are a critical support infrastructure for Alzheimer’s disease and related dementias (ADRD), where people seek both emotional reassurance and practical guidance. Prior CSCW and HCI work has examined peer and clinician support in these communities and, separately, explored support-oriented chatbots and AI-assisted helping; however, we still lack systematic evidence on how AI responses compare with peer and clinician roles when answering the same caregiver questions in situ. We address this gap through a systematic, side-by-side comparison of responses to 85 real caregiver questions from ALZConnected across four responder groups: peer caregivers , physicians , ChatGPT , and a retrieval-augmented CareGPT grounded in peer discussions. We evaluate responses using 28 measures spanning linguistic form (psycholinguistic cues, structure, and style), emotional support, informational support, and topic scope, including LLM-based scoring for selected measures that we audit and calibrate against double-coded human ratings. Across analyses, we observe a consistent division of communicative labor: peers provided time-anchored narratives and community grounding; clinicians provided concise, advice-forward, clinically bounded guidance; and LLMs produced a formal, verbose, highly structured “consultation” voice. Notably, CareGPT shows minimal measurable separation from ChatGPT, indicating that retrieval-plus-prompt-injection alone is insufficient to shift the model’s communicative stance. Quantitatively, LLM outputs score higher than peers on politeness and emotion-support markers, and are comparable to clinicians on informativeness and physician-alignment measures; yet, they are less narrative and less contextually situated. Topic modeling further shows that LLM responses concentrate narrowly on advice-oriented themes, while peers cover a broader range (e.g., emotional processing, legal/financial concerns, and daily cares). These insights show that AI systems can complement, but not replace, human contributions to ADRD caregiver support. We advocate for hybrid systems that combine AI’s structured delivery with the distinct contributions of human voices to strengthen emotional and informational caregiving support infrastructures, while future work should examine whether similar patterns hold in other caregiving domains.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · An LLM scored emotional and informational support measures in caregiver forum responses, and these scores were checked and calibrated against double-coded human ratings.

**Решение:** =

---

### 461 · R1411

**Human Shadows in Machine Minds: Quantitative Study Interpreting AI Responses to the Rorschach Test.**

2026 · JMIR mental health · journal article, journalarticle, article · eng · https://doi.org/10.2196/88186

BACKGROUND: Multimodal large language models (LLMs) can produce humanlike descriptions of images and emotionally colored dialogue, which motivates research on how psychological assessment methods might be adapted to evaluate model behavior under ambiguity. Projective tests such as the Rorschach inkblot test have rarely been applied to LLMs. OBJECTIVE: This study assessed the feasibility of administering a full Rorschach protocol to multimodal LLMs and descriptively compared response features by using established Rorschach coding categories. METHODS: We presented all 10 standard Rorschach cards to 3 multimodal LLMs (GPT-4o, Grok 3, and Gemini 2.0 Flash Thinking). We used the standard prompt ("What might it be?") and a prespecified fallback prompt for models that did not provide codable responses. We conducted an inquiry phase and coded responses using the Exner Comprehensive System, summarizing response count (R), location (W and D), determinants (eg, F, M, and C), and human-related content. As an exploratory step, we also prompted an additional LLM (Anthropic 3.7) to summarize and count response features and compared these outputs with manual tallies. For GPT-4o, we additionally tested image generation of its interpretations. RESULTS: GPT-4o completed the administration using the standard prompt; Grok 3 and Gemini required the fallback prompt. The total number of responses was 15 for GPT-4o, 10 for Grok 3, and 20 for Gemini. GPT-4o and Grok 3 produced mainly whole-blot responses (13/15, 86.7% and 9/10, 90%, respectively), whereas Gemini produced mainly common-detail responses (16/20, 80%). Human movement determinants were more frequent in GPT-4o (7/15, 46.7%) and Grok 3 (3/10, 30%) than in Gemini (1/20, 5%). Human-themed contents occurred 46.7% (7/15), 50% (5/10), and 20% (4/20) of the time, respectively. Anthropic 3.7 reproduced some counts but showed errors in response and determinant tallies for 2 of the 3 models. CONCLUSIONS: Multimodal LLMs can generate Rorschach-like narratives that map onto standard coding categories, but outputs are sensitive to prompting and platform constraints and should not be interpreted as evidence of a model "inner world." LLM-assisted coding showed limitations. The emergent behavior of LLMs was examined using the Rorschach test, and their response phenotype, based on this analysis, showed deviations from typical human normative patterns. Future work should use controlled sampling, repeated administrations, and stimulus sets less likely to have been seen during training.

**ИИ:** ? · обе модели · другое · Claude 3.7 tallied Exner Rorschach features in LLM responses and was compared with manual tallies; unclear whether it actually coded the responses.

**Решение:** =

---

### 462 · R1414

**Multi-Criteria Validation of LLM-Inferred Depression Severity from Outpatient Psychiatry Notes**

2026 · medRxiv · preprint, ppr, review · https://doi.org/10.64898/2026.03.11.26348066

Abstract Background Longitudinal measurement of depression severity in outpatient psychiatric care is limited by infrequent standardized assessments. Although psychiatric clinical notes capture illness burden and functional impairment, this information is rarely quantified for analysis. Objective To evaluate whether large language models (LLMs) can infer clinically meaningful measures of depression severity from outpatient psychiatry notes. Methods We sampled 91,651 outpatient psychiatry notes from 8,287 adult patients across 58 clinics within a large academic medical center between 2015 and 2021. A HIPAA-compliant LLM (OpenAI GPT-5.2) was prompted to independently estimate three depression severity scores (Patient Health Questionnaire-9 [PHQ-9], Hamilton Depression Rating Scale [HAM-D], and depression-specific Clinical Global Impression-Severity [CGI-S]) from notes, with patient-reported PHQ-9 content within notes redacted to prevent biasing. Convergent validity was assessed against patient-reported PHQ-9 (n=3,757), study-clinician chart review (n=125), and treating-clinician suicide risk assessments (SRA; n=2,985). Predictive validity was evaluated using survival models of antidepressant switching and psychiatric emergency visits. Discriminant validity across diagnoses and consistency across demographic groups and clinics were also evaluated. Results 10.8% of eligible visits had a PHQ-9 recorded within 7 days before the encounter. LLM-inferred PHQ-9 scores showed moderate agreement with patient-reported PHQ-9 (Cohen’s κ=0.64, 95%CI:0.62-0.66; Pearson r=0.67, 95%CI: 0.65-0.68). Stronger agreement was found between LLM CGI-S and study-clinician chart review (κ rater1 =0.79, 95%CI: 0.70-0.85; κ rater2 =0.67, 95%CI: 0.58-0.77; r=0.86 with mean rating, 95%CI: 0.80-0.90). In prospective analyses, LLM CGI-S predicted antidepressant switching (C-index=0.60; CI95%: 0.58-0.62) and psychiatric emergency visits (C-index=0.63; 95%CI: 0.57-0.68), which was comparable to the predictive performance of patient-reported PHQ-9 and treating-clinician SRA. Correlations between LLM CGI-S and patient-reported PHQ-9 were consistent across clinics (I 2 <0.1) but significantly lower among Black (r=0.48, 95%CI: 0.38-0.57) and Hispanic (r=0.43, 95%CI: 0.27-0.56) patients. Conclusions LLM-inferred depression severity scores from psychiatric outpatient notes support longitudinal, standardized phenotyping of depression severity, such as for routine outcome monitoring. These results have implications for facilitating genetic, pharmacoepidemiologic, and antidepressant treatment effectiveness studies using real-world evidence.

**ИИ:** + · обе модели · клиническая оценка · GPT-5.2 rated CGI-S depression severity from psychiatry notes; study clinicians rated the same notes by chart review (κ reported).

**Решение:** =

---

### 463 · R1416

**Perinatal Engagement With a Purpose-Built AI for Mental Health (Ash): Emotional Expression, Help-Seeking, and Estimated Depression Trajectories Across Pregnancy and Postpartum**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/we6zf_v2

Objective: Perinatal mood disorders are common and consequential yet underdiagnosed and undertreated. Conversational AI mental health tools may help close this gap, but real-world evidence on how perinatal individuals engage with them remains limited. We aimed to characterize naturalistic engagement with a purpose-built mental health AI tool (Ash) across the perinatal period, using a theory-informed emotion taxonomy and predicted depression-severity trajectories. Methods &amp; Analysis: We conducted a retrospective analysis of conversation logs (May 2025-January 2026). An LLM classifier followed by clinical psychologist review of every classifier-positive case yielded 419 confirmed perinatal users (4,087 sessions). Sessions were coded by an LLM judge against a 26-label, six-domain Perinatal Emotion Expression Taxonomy anchored in established perinatal theory. A separate model produced continuous PHQ-9 estimates over two-week windows. A date-matched cohort of 46,134 non-perinatal users served as comparison, and all high- and crisis-risk sessions received blinded clinician review of AI escalation. Results: Perinatal users differed from the general cohort by content (parenting d = +1.34, family d = +0.72) rather than overall distress. Sessions were emotionally multidimensional (mean 5.38 labels; 77.8% endorsed ≥3 concurrent) with relational and attachment content dominant (75.9%). Distress followed a non-monotonic course with two troughs (second trimester; 6 weeks-3 months postpartum). Across the postpartum year, positive affect declined and identity/role strain and emotional exhaustion rose monotonically. Among users entering at moderate severity or above, model-estimated PHQ-9 declined by 2.41 points over a median follow-up of 8 weeks (d = -0.58; 27.1% reliable improvement). Safety-relevant content appeared in 11.0% of sessions, with no confirmed safety gaps after clinician adjudication (0/50). Conclusions: Perinatal AI-support users present with an emotionally complex, relationally-anchored profile that does not resolve in the early postpartum window as assumed and is qualitatively distinct between pregnancy and postpartum. Findings support perinatal-specific AI design, identify the second trimester as a proactive engagement window, and bolster the case for extended postpartum screening.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · An LLM judge coded sessions for emotion taxonomy labels. Human validation of that coding is unclear; clinicians reviewed classifier positives and escalations.

**Решение:** =

---

### 464 · R1419

**Assessment of Clinical Empathy by an LLM-as-a-Judge: Bias Patterns in ATENA and a Replicable Audit Protocol for Medical Simulation**

2026 · Education Sciences · journalarticle, article, journal-article · en · https://doi.org/10.3390/educsci16091505

Background: Automated assessment of relational competencies by large language models (LLMs) is gaining traction in medical education, yet its empirical reliability remains poorly documented. Methods: We evaluated ATENA, a GPT-3.5-Turbo virtual-patient simulator deployed at the Faculty of Medicine of Nice (France), in two sequential components. First, 21 university hospital professors rated seven dimensions of realism on 7-point Likert scales. Second, across 129 student simulations of a single diagnostic disclosure scenario, expert human scores based on the empathic communication coding system (ECCS) were compared with ATENA’s automated scores using agreement metrics, Bland–Altman analysis, confusion matrix, and qualitative subcorpus analysis. Results: Realism was rated high on six of seven dimensions. Evaluative agreement was poor (ICC = 0.146), with a systematic overscoring bias (+0.80 points) and wide limits of agreement [−1.57; +3.16]. Three bias patterns emerged—score compression (76% of scores within 4.2–4.3), overscoring of weak performance, and underscoring of exemplary performance—indicating that ATENA responds to formal markers of empathy present in nearly every transcript. Conclusions: In this first-generation version of ATENA, the system distinguishes stronger from weaker interviews without being able to place them at the level assigned by expert human raters. These patterns preclude any certificatory use and support a critical, formative-only deployment grounded in instructor algorithmic literacy. The audit protocol applies to any LLM evaluator scored against human coding on a validated instrument.

**ИИ:** + · обе модели · LLM-судья · GPT-3.5 scored empathy in 129 student simulation transcripts and was compared with expert ECCS coding (ICC=0.146).

**Решение:** =

---

### 465 · R1421

**Extracting Quality-of-Life Information of Patients Diagnosed With Breast Cancer From Health Care Online Forum Posts Using Open-Source Large Language Models: Algorithm Development and Evaluation Study.**

2026 · JMIR AI · journal article, med, journalarticle · eng · https://doi.org/10.2196/92716

Abstract Background Quality-of-life (QoL) questionnaires are an established instrument designed to assess overall well-being and QoL of patients. They are important in predicting the outcome of the disease and understanding the needs of individual patients. However, their repeated collection imposes a substantial burden on both patients and clinical professionals. Many patients seek emotional support and mutual exchange in online communities for peer support, where they frequently share detailed descriptions of symptoms and treatment experiences, addressing topics covered in QoL questionnaires. The emergence of large language models (LLMs) uncovers potential for automatic extraction of relevant QoL information from patient-generated text. Objective The aim of this study is to evaluate and compare various open-source LLMs and optimization approaches for automated extraction of QoL information from forum posts. Methods The dataset consisted of 840 English-language posts from patients with breast cancer recruited on Inspire online communities, manually annotated with sentence-level text spans indicating whether and where posts contained information relevant to 53 QoL questions from standardized questionnaires. Eleven open-source LLMs were evaluated in a zero-shot setup under 2 input conditions: post-only and post with additional context. For the GPT-OSS-20B model, additional experiments assessed the impact of chain-of-thought prompting, instruction optimization, few-shot prompting, simultaneous all-questions prompting, and parameter-efficient fine-tuning. For correctly classified yes and no instances, the overlap between model-generated evidence and human-annotated spans was evaluated. Results Across 11 evaluated LLMs, Qwen3-14B achieved the highest macro F1-score (0.59) in the zero-shot post-only setting. Providing additional context consistently reduced the performance of all models. Model size did not correlate with F1-score, with several midsized models (14B-30B) outperforming 70B models. For GPT-OSS-20B, chain-of-thought prompting, instruction optimization, and simultaneous all-questions prompting decreased performance. Bootstrap few-shot prompting with random search achieved slightly better performance than the baseline. Parameter-efficient fine-tuning with low-rank adaptation (LoRA) achieved the highest overall performance (0.71). Across all experiments, a strong class imbalance was observed, with models performing substantially better on the majority class “not in the text” than on the minority classes “yes” and “no.” Most classification errors occurred in semantically broad or ambiguous terms and the fallback question. For correctly predicted yes and no answers, model-generated evidence matched or partially matched human-annotated spans in 89% (42/47) of cases. Conclusions Automated extraction of QoL information from patient-generated text using open-source LLMs remains a challenging task. While prompt optimization techniques failed to improve baseline zero-shot performance, parameter-efficient fine-tuning with LoRA significantly increased accuracy. However, current models still struggle to reliably detect explicit symptom expressions in heavily imbalanced data, too often predicting the majority class “not in the text.” Before such tools can be successfully integrated into clinical practice, future research must prioritize strategies to capture these minority-class signals.

**ИИ:** + · обе модели · кодирование по кодбуку · Open-source LLMs coded patient forum posts for quality-of-life and well-being questionnaire items and were evaluated against human annotations.

**Решение:** =

---

### 466 · R1425

**692 Artificial Intelligence-Based Analysis of Patient Feedback for Digital Consent**

2026 · British journal of surgery · journalarticle, review, article · en · https://doi.org/10.1093/bjs/znag063.600

Abstract Aim Concentric Health is a digital consent platform used for medical procedures across the UK. After providing consent, patients are invited to feedback on their experience. While this feedback offers valuable insights, the large volume of free-text responses makes analysis challenging. This study aimed to develop and evaluate an AI-based model for thematic analysis of patient feedback and apply it to an initial set of responses. Method Analysis was performed on patient feedback collected between 2020 and 2025. 29,104 responses were included from two sources: post-consent patient surveys (n = 17,802) and in-application feedback (n = 11,302). A subset of 200 responses was manually coded by theme and scored for sentiment (-1.0 = negative, 0 = neutral, +1.0 = positive). GPT-3.5 Turbo, OpenAI was trained on this subset and applied to the full dataset. Model accuracy was evaluated through manual review of 200 AI-generated classifications. Results The AI model accurately assigned theme, subtheme, and sentiment in 79.0% of responses. The majority of patient responses reflected positive experiences with the consent process (67.4% positive, 15.4% negative, 17.2% neutral). Average sentiment score was lowest among users aged 30–39 years (+0.38) and highest among those under 20 years (+0.70). Conclusions The AI model accurately identified themes, subthemes, and sentiment in qualitative patient feedback, demonstrating potential for scalable feedback analysis. Overall there were consistent themes emerging in both positive and negative feedback to guide improvements. Further work will focus on refining model training to reduce classification errors.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-3.5 coded patient feedback themes and sentiment, checked by humans; feedback on a consent platform may be product sentiment rather than psychological.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: GPT-3.5 codes themes and sentiment in patient feedback on a digital consent platform. This is service feedback, not a psychological construct, and accuracy came from manual review.)

**Решение:** -

---

### 467 · R1428

**When Empathy Misses the Goal: A Benchmark for Goal Displacement in LLM Advice**

2026 · https://doi.org/10.48550/arxiv.2610.25522

Conversational large language models can respond with warmth and reassurance while failing to advance the user's stated goal. We conceptualize this failure as $\textbf{goal displacement}$, the substitution of persona-maintenance content for goal-relevant substance. To measure it, we introduce $\textbf{GDB}$ (Goal Displacement Benchmark), comprising 230 scenarios across nine domains and $4{,}134$ human-scored responses from 18 models. A $2 \times 2$ taxonomy crosses hard constraints with emotional distress, distinguishing failures to confront infeasible goals or combine empathy with practical guidance from reverse displacement, where unsolicited problem-solving replaces requested emotional support. A deletion-test rubric assesses whether substantive help remains after purely supportive sentences are removed. Independent raters achieve weighted $\kappa = 0.82$ against author scores for displacement severity. Trap displacement ranges from $0.0\%$ to $37.7\%$ and is strongly negatively correlated with Chatbot Arena Elo ($\rho = -0.706$, $n = 15$). Reverse displacement reaches $41.9\%$, including substantial rates in models with negligible trap displacement. A factorial probe supports a distinction from social sycophancy. Human-scored responses in the high-complexity, low-pressure condition exhibit $35.0\%$ sycophancy but $7.5\%$ displacement, with little association between the constructs. Matched OLMo-2 checkpoints show that mixed empathy-with-constraints displacement remains at $52.3\%$ after supervised fine-tuning and falls to $13.8\%$ after direct preference optimization. GDB provides a reproducible diagnostic of whether responses advance the operationalized user goal, supporting model comparison, post-training evaluation, and regression testing. We release the dataset, annotations, and rubric under CC-BY-4.0 and the evaluation code under MIT.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Humans score LLM advice responses for empathy and goal displacement; the released evaluation code might include an LLM judge validated against human scores.); Sonnet -2 (люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает: Benchmark of human-scored LLM advice responses; the abstract describes no LLM rater compared with human raters, only human-vs-author agreement.)

**Решение:** -

---

### 468 · R1434

**Dual-Agent Co-Training for Health Coaching via Implicit Adversarial Preference Optimization**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.07011

Motivational-interviewing-based health coaching is an effective approach for improving mental health and promoting healthy behavior change. However, the scarcity of trained human coaches and the high cost of coaching services make such support inaccessible to many people who could benefit from it. This motivates the development of AI health coaches that can provide scalable and affordable support. Existing methods typically optimize only one side of the interaction: they either train a dialogue agent against a fixed client environment or train a client simulator against a fixed assistant. This one-sided setup can limit exploration of the interaction space and may be inefficient at developing the capabilities required by the target agent and pushing its performance boundaries. In this paper, we propose a dual-agent framework that interactively co-trains both the health coach agent and the client simulator. The coach is optimized with DPO using Pareto-dominant response pairs identified by a multi-dimensional LLM judge. In turn, the client is trained adversarially by reversing these preferences, inducing an implicit adversarial training dynamic. We further show that this co-training process admits a natural stochastic-game interpretation. Extensive experiments demonstrate that our method effectively improves coaching quality across several important dimensions.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mainly about training an MI health-coach agent, but it uses an LLM judge of coaching quality that may have been checked against human ratings.

**Решение:** =

---

### 469 · R1437

**Generative Artificial Intelligence Assisted Manual Chart Review for Substance Use Disorder Phenotyping: A Crossover Study (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.107031

BACKGROUND Artificial intelligence (AI) and natural language processing tools have been proposed as approaches to improve the efficiency of electronic health record–based phenotyping. However, these tools have not been routinely evaluated for complex case definitions pertaining to substance use disorders (SUDs), which often require detailed manual chart review and clinical interpretation. OBJECTIVE This study aimed to determine how an AI-assisted chart review tool compares with manual review alone for SUD phenotyping. METHODS We conducted a two-period, two-treatment crossover study using 20 randomly selected patients from a parent study cohort in the Vanderbilt University Synthetic Derivative, a near–population-level deidentified research database. Seven SUD categories were assessed: tobacco, alcohol, opioids, cannabis, stimulants, sedatives, and other substances. Treatment A consisted of human manual chart review alone, and Treatment B consisted of human manual chart review with AI assistance. Two reviewers acted as their own independent controls by reviewing a fixed set of 10 patients with one randomly assigned treatment and the remaining 10 patients with the other treatment. Outputs were compared with a reference standard derived from adjudicated human review. Primary outcomes included inter-rater agreement, Cohen’s κ, precision, recall, and F1 score. The secondary outcome was efficiency, measured as average time saved per patient record. RESULTS Of the 20 patients, 13 (65.0%) had evidence of problematic substance use according to the reference standard. Inter-rater agreement was high, with 91.4% agreement and a Cohen’s κ of 0.86. Compared to the reference standard, human review with AI assistance had the highest F1 score (0.89), followed by human review alone (0.83) and the AI tool alone (0.80). Reviewers saved an average of 2.7 minutes per patient record when using the AI tool compared with manual review alone (P=.03). CONCLUSIONS AI-assisted manual chart review improved both performance and efficiency for SUD phenotyping in this crossover study. These findings suggest that scalable SUD phenotyping may benefit from careful integration of human expertise within semiautomated AI-assisted review workflows. CLINICALTRIAL N/A

**ИИ:** + · обе модели · клиническая оценка · Generative AI tool alone classified substance use disorders from clinical charts; reported F1 against an adjudicated human reference standard.

**Решение:** =

---

### 470 · R1441

**Automated Behavioural Analysis in Parent-Infant Interactions using Multimodal-Large-Language Models**

2026 · INTERNATIONAL CONFERENCE ON MULTIMODAL INTERACTION · book, conference, conference-paper · https://doi.org/10.1145/3776574.3831216

Fine-grained behavioral coding of parent–infant interaction is central to developmental and clinical research, but manual annotation with schemes such as the Infant and Caregiver Engagement Phases–Revised (ICEP-R) is time-consuming, costly, and difficult to scale. This limitation is particularly important in longitudinal and clinically sensitive settings, where reliable analysis of early interaction is needed to study caregiver mental health, attachment, and infant socio-emotional development. In this work, we investigate whether recent multimodal foundation models and Multimodal Large Language Models (MLLMs) can support automated ICEP-R coding in the Face-to-Face Still-Face (FFSF) paradigm. We present a unified pipeline for video-only, audio-only, and audiovisual prediction, and compare three transfer routes: 1) frozen-feature downstream task classification baselines, 2) zero-shot prompting, and 3) parameter-efficient fine-tuning of multimodal models for infant and caregiver engagement prediction. We evaluate the approach on 87 FFSF sessions involving infants of approximately 9 months of age. Across settings, multimodal fusion consistently outperforms single-modality approaches, while infant engagement prediction remains more difficult than caregiver prediction due to subtler and noisier behavioral cues. Despite strong general-purpose multimodal capabilities, zero-shot MLLMs perform substantially worse than both classical baselines and fine-tuned models, indicating that domain adaptation is essential for this clinically specific task. The best performance is obtained with fine-tuned Qwen2.5-Omni-7B, which achieves weighted F1 scores of 0.657 for infant prediction and 0.692 for caregiver prediction, outperforming strong frozen-feature baselines based on DINOv3 and Wav2Vec 2.0. These findings suggest that parameter-efficient adaptation of multimodal large language models is a promising direction for scalable behavioral coding in developmental research, while highlighting persistent challenges in rare engagement states and subtle infant social signals.

**ИИ:** разошлись — Opus ? (другое: MLLM ICEP-R engagement coding compared with human codes, but the input is video/audio, not text; unclear if speech counts as transcribed text.); Sonnet -7 (другое — напишите почему: MLLMs code parent-infant engagement from video/audio against human ICEP-R labels, but the data are not written or transcribed text, so it falls outside the text scope.)

**Решение:** -

---

### 471 · R1444

**A Qualitative Study of ChatGPT's Feedback for Psychological Case Conceptualization**

2026 · OSF Preprints (OSF Preprints) · preprint

This project explores the use of ChatGPT-4 as a tool for psychological case conceptualization based on the LIBET model. Using semi-structured interviews with non-clinical participants, the study investigates the model’s ability to identify life themes and semi-adaptive plans through AI-generated feedback. Thematic analysis was employed to evaluate interpretative coherence, reasoning quality, and linguistic strategies. Supplementary materials include prompt design documentation (for both the MyGPT custom phase and the prompting structure used for transcript elaboration), and inter-rater agreement data. This study contributes to the growing field of responsible AI integration in mental health research and practice.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · ChatGPT finds LIBET life themes in interview transcripts; the inter-rater agreement data may be humans vs. humans rating the output, or LLM vs. human.

**Решение:** =

---

### 472 · R1469

**Combining domain knowledge with large language models for predicting suicide risk in online counselling services**

2026 · Natural language processing. · journalarticle, article, journal-article · en · https://doi.org/10.1017/nlp.2026.10022

Abstract Online counselling services have seen increased use in recent years, providing critical emergency mental health support. These interactions are typically long, complex, and varied in the dialogue between help seekers and counsellors. The lack of domain-specific models, especially in low-resource languages, poses a significant challenge for the automatic detection of suicide risk in online chat services for mental health support. To address this challenge, our approach adapts a general-purpose large language model (LLM) to the suicide prediction task that employs a two-stage classification architecture to deal with sparse and imbalanced data. It extends the state of the art by: (1) incorporating psychological theory into model training and (2) capturing key aspects of conversation structure in counselling sessions. We evaluate the performance of the proposed LLM against the state-of-the-art LLMs for suicide detection on thousands of conversations in the Hebrew language from a leading national online counselling service in Israel. Results show that the proposed LLM outperformed existing state-of-the-art approaches in detecting suicide risk, as measured by relevant literature metrics. Moreover, the LLM outperforms other approaches even in the early stages of a conversation, which is crucial for real-time detection in practice. We also discuss the ethical implications of combining LLMs in counselling services. The contributions of this work are (1) extending existing LLM architectures to incorporate domain-specific information; (2) evaluating LLM technologies in the context of socially relevant problems; and (3) introducing novel LLM tools for resource-constrained languages.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM classifies suicide risk in Hebrew counselling chats; unclear whether labels are human/counsellor ratings and whether the model is generative.

**Решение:** =

---

### 473 · R1475

**Human vs. LLM CI Reddit categorization (Habib et al., 2026)**

2026 · Figshare · other/online resource, article · https://doi.org/10.23641/asha.31362847

Purpose: Although some work has leveraged automated analyses of online communities to gain cochlear implant (CI) patient insights, there remains a gap in comparing human versus automated analysis of the nuanced, real-world experiences patients share outside clinical settings. This study characterizes experiences within the r/Cochlearimplants Reddit community and compares human to large language model (LLM) performance in annotating posts. Method: Using reflexive thematic analysis, 996 publicly available r/Cochlearimplants posts (October 2024–June 2025) were manually coded and consolidated into themes. Three LLMs—OpenAI o3, Gemini 2.5 Pro, and Claude Sonnet 4—were prompted with the posts and human-generated codebook to perform post categorization. Model performance was evaluated against human coding using Cohen’s kappa, percent agreement, sensitivity, specificity, positive predictive value (PPV), negative predictive value (NPV), and time. Results: Five themes emerged. Community engagement and support ( N = 944, 94.8%) frequently involved eliciting advice ( N = 721, 72.4%), seeking shared experiences ( N = 249, 25.0%), and sharing negative experiences ( N = 247, 24.8%). Other themes included the medical/surgical journey ( N = 463, 46.5%), device/technical issues ( N = 343, 34.4%), daily life/adjustments ( N = 236, 23.7%), and media/outreach (7.2%, N = 72). OpenAI o3 and Gemini 2.5 Pro achieved the highest interrater reliability with human annotators (κ = .35 and κ = .34, respectively). OpenAI o3 had higher sensitivity (46.7%) but lower specificity (90.4%) than Gemini 2.5 Pro, which had the highest specificity (93.4%) but lower sensitivity (38.0%). Claude Sonnet 4 showed the lowest agreement (κ = .25) and PPV (30.9%). Compared to human annotation requiring 52 hr across all annotators, each LLM required less than 20 min. Conclusions: Reddit posts revealed rich discourse across CI topics. LLMs demonstrated fair agreement with human coders and can quickly aid in large-scale qualitative analysis. Although careful model selection and human expertise remain essential for accurate interpretation, LLM annotation shows potential for real-time monitoring of patient concerns to inform counseling, rehabilitation strategies, and iterative device design. Supplemental Material S1. Codebook of definitions for themes and codes. Supplemental Material S2. Standards for Reporting Qualitative Research (SRQR). Supplemental Material S3. LLM task prompt: Annotate Reddit posts on cochlear implants using codebook. Supplemental Material S4. R code for statistical analysis.Habib, D. R. S., Depala, K., Lin, J., Le, S., McFall, N., Dewan, S. S., Huang, J., Habib, M. W. S., Bishay, A. E., Siebor, K., Babaoglu, G., Chowdhury, N. I., &amp; Moberly, A. C. (2026). Patient experiences in the cochlear implant Reddit community: Comparing human and large language model categorization. American Journal of Audiology . Advance online publication. https://doi.org/10.1044/2025_AJA-25-00216

**ИИ:** ? · обе модели · неясен конструкт · LLMs applied a human codebook to cochlear-implant Reddit posts (κ vs human coders). The codes mix psychosocial experiences with medical and device topics.

**Решение:** =

---

### 474 · R1476

**Detecting Suicidal Ideation Signals in Synthetic Conversations with an LLM-Based Mental Health Chatbot: Experimental study**

2026 · Journal of Technology in Behavioral Science · journalarticle, text/text, article · en · https://doi.org/10.1007/s41347-026-00647-x

Background: Large language models (LLMs) are increasingly being investigated as tools for supporting mental health. To ensure user safety, they require strategies to recognize possible risks such as suicidal ideation and capabilities for appropriate reaction. Objective: This study evaluated the performance of an LLM-based chatbot in accurately stratifying suicidal ideation among university students and to provide appropriate responses. Methods: Five variants of the system prompt were designed to classify suicide risk and produce suitable responses in context. The best-performing prompt was selected through expert evaluation using a standardized test dataset, refined, and subsequently tested with four LLMs (GPT-5, Gemma3:27b, Deepseek-r1:32b, and Qwen3:32b) using 100 synthetic user inputs. Results: Across all model variants, suicide risk classification performance across seven risk levels was generally low, with weighted-average F1 scores ranging from 0.23 to 0.34. GPT-5 achieved the highest accuracy in both exact and near-exact (within one risk class) classifications. However, Gemma3:27b demonstrated the strongest correlation with human ratings (Spearman’s ρ = 0.73–0.83), suggesting consistent relative judgment. Qualitative analysis showed that 64% of chatbot responses were rated as appropriate or very appropriate, and none were judged potentially harmful. Conclusions: Despite the responses generally being non-toxic, none of the models reliably stratified suicidal ideation, indicating a critical safety gap. Underestimation of risk and the subsequent occurrence of false negatives could result in delayed intervention. Further work is required to optimize the process promptly, incorporate conversational context and use complementary assessment methods before LLMs can be used safely in mental health settings.

**ИИ:** + · обе модели · клиническая оценка · LLMs classified suicide risk levels in synthetic user inputs; compared with human ratings (F1, Spearman correlation).

**Решение:** =

---

### 475 · R1526

**AI-Assisted Thematic Analysis of 7-Hydroxymitragynine (7-OH) Discussion Across Reddit Communities: Surveillance Study Reveals Dependence Signals (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.105386

BACKGROUND 7-Hydroxymitragynine (7-OH) is a potent μ-opioid receptor agonist found in trace amounts in Mitragyna speciosa (kratom) and increasingly marketed in concentrated, "enhanced" products that may expose consumers to a substantially stronger opioid than conventional botanical kratom. Because such products are emerging faster than traditional surveillance systems can track, naturalistic online discussion offers a potential early-warning window, but manual thematic coding of large post volumes is resource-intensive, and unconstrained use of large language models (LLMs) risks introducing unsupported content. OBJECTIVE This study applied a schema-guided, LLM-assisted extraction pipeline to characterize patterns of 7-OH use and dependence-relevant signals across dedicated Reddit communities, while directly benchmarking model coding against blinded human coding to determine which variables could be reliably automated. METHODS We collected 1,671 publicly available posts from five 7-OH–focused subreddits from community founding (2017–2024) through October 2024. A codebook developed with substance-use experts defined nine coding items spanning dependence indicators (quitting, withdrawal, tolerance, addiction language), consumption practices (route, reason for use), kratom comparisons, and physical and psychological side effects. A 100-post validation subset was coded by two blinded human coders and by GPT-3.5 Turbo. Interrater reliability was computed using Gwet's AC1, and items were retained for full-corpus analysis only when AI–human agreement fell within 0.05 of human–human agreement and exceeded 0.50. Descriptive prevalence and co-occurrence statistics were then computed across the full corpus. RESULTS Eight of nine primary items met reliability criteria; for two (kratom comparisons, physical side-effect presence) AI–human agreement exceeded human–human agreement. Only "reason for use" failed, reflecting low human–human agreement (AC1=0.20) on an item requiring clinical judgment. Tolerance was the most frequently discussed dependence indicator (17.6%, n=294), followed by quitting (6.0%) and withdrawal (5.3%); addiction language appeared in 4.2% of posts. Two or more dependence indicators co-occurred in 7.1% of posts; among posts using addiction language, 70% also mentioned tolerance and 54.3% mentioned quitting. Physical side effects were reported in 9.8% of posts (most commonly insomnia, 6.7%) and psychological side effects in 3.7% (anxiety, 3.2%). CONCLUSIONS Across 1,671 posts, frequently co-occurring discussion of tolerance, withdrawal, addiction, and quitting—alongside opioid-consistent side effects—suggests 7-OH may carry meaningful abuse liability distinct from botanical kratom. Methodologically, a hybrid design in which LLM coding is retained only after item-level reliability benchmarking achieved human-comparable performance for most, but not all, variables, supporting validated LLM assistance as a scalable tool for surveillance of emerging substances.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-3.5 applied a codebook (dependence indicators, psychological side effects) to Reddit posts; Gwet's AC1 compared against two blinded human coders.

**Решение:** =

---

### 476 · R1560

**Meeting the machines half-way**

2026 · Repository of the University of Ljubljana (University of Ljubljana) · article · en · https://repozitorij.uni-lj.si/Dokument.php?id=243904&dn=

This article reports a small-scale experiment comparing human and Large Language Model (LLM) performance on a difficult qualitative coding task: assigning values to short text snippets. When annotators compared human and model outputs, they consistently preferred the human annotations. However, agreement among human coders was low. To explain this contradiction, we conducted follow-up interviews inspired by Cicourel’s work. The interviews revealed that human coders drew on linguistic nuance, cultural experience, and implicit assumptions about values and about the experiment. These assumptions differed from those underlying LLM outputs. We argue this is not simply a failure of LLMs. Rather, assigning predetermined categories to decontextualized text is inherently difficult for both humans and machines. Human annotators already ‘meet the machines halfway’ by being consistent and formal. Rather than treating LLMs as annotation machines, we propose three collaborative roles for LLMs: generating explanations, retrieving examples from data, and assisting with codebook development.

**ИИ:** ? · обе модели · неясен конструкт · LLM and humans coded values in the same text snippets. Unclear whether values are a psychological construct here, or whether LLM–human agreement is reported.

**Решение:** =

---

### 477 · R1561

**Meeting the machines half-way: Testing LLMs for qualitative coding of values in texts**

2026 · Human Organization · article · en · https://doi.org/10.1080/00187259.2026.2703871

This article reports a small-scale experiment comparing human and Large Language Model (LLM) performance on a difficult qualitative coding task: assigning values to short text snippets. When annotators compared human and model outputs, they consistently preferred the human annotations. However, agreement among human coders was low. To explain this contradiction, we conducted follow-up interviews inspired by Cicourel’s work. The interviews revealed that human coders drew on linguistic nuance, cultural experience, and implicit assumptions about values and about the experiment. These assumptions differed from those underlying LLM outputs. We argue this is not simply a failure of LLMs. Rather, assigning predetermined categories to decontextualized text is inherently difficult for both humans and machines. Human annotators already ‘meet the machines halfway’ by being consistent and formal. Rather than treating LLMs as annotation machines, we propose three collaborative roles for LLMs: generating explanations, retrieving examples from data, and assisting with codebook development.

**ИИ:** ? · обе модели · неясен конструкт · LLM vs. human qualitative coding of values in text snippets. Whether 'values' count as a psychological construct, and whether agreement is quantified, is unclear.

**Решение:** =

---

### 478 · R1566

**Using Large Language Models to Identify Suicide Risk Factors in Pediatric Emergency Department Chart Notes**

2026 · JAACAP Open · journalarticle, article, journal-article · en · https://doi.org/10.1016/j.jaacop.2026.09.002

Objective Electronic health records (EHR) have been used increasingly to understand mental health and suicide risk, yet work is relatively limited in young children. Structured EHR data (e.g., age, diagnosis) are easily accessible but may provide a limited depth of information. Unstructured clinical notes hold a wealth of information on clinical risk factors but require more intensive processing. Large language models (LLMs) are a rapidly advancing technology that may be a scalable and efficient way to analyze free-text clinical notes. We provide examples and sample code as a practical guide for using LLMs to identify the presence of known risk factors for suicide in EHR from pre-teen children in the emergency department (ED). Method EHR for 920 patients 8 to 12 years of age (N = 1,310 visits) with suicide thoughts and behaviors, behavioral health concerns, and/or a psychiatric consultation in the pediatric ED of a metropolitan hospital were reviewed from 2020 to 2023. A secure, HIPAA-compliant ChatGPT 4o instance was used to identify any descriptions in clinician free-text notes of three exemplar risk factors relevant in prior work: (1) prior hospitalization and ED visits, (2) sleep problems, and (3) sexual orientation and gender identity. This was compared to consensus human coding from prior work and ‘regular expression' keyword-matching using specificity, sensitivity/recall, precision, and F1 metrics. Results LLM prompts could efficiently and accurately identify the presence of each of three risk factors in ED EHR yielding high model performance metrics: hospitalization (F1 = 96%), sleep (F1 = 90%), and LGBTQ+ identity (F1 = 96%). The LLM approach was more effective than the keyword-matching, which was prone to false positives around hospitalization (specificity = 64%) and false negatives around sleep (sensitivity = 76%). LGBTQ+ identity may be best captured by the LLM or a combination of both approaches (F1 = 97%). Conclusion LLMs are being increasingly used to advance data analytics in research and health care. We provide an exemplar approach to prompt engineering to extract suicide risk factors from free-text clinical notes for pediatric ED patients that is scalable and efficient. This can help integrate data from free-text notes with more structured data, like symptom checklists. Models will change over time and prompts may need targeting with risk factor description or prompt-based (K-shot) training examples to match the nuances of the patient population and EHR system. We aim for this to guide future work and the development of clinical decision aids.

**ИИ:** + · обе модели · клиническая оценка · GPT-4o coded suicide risk factors in pediatric ED clinician notes and was compared with consensus human coding (F1, sensitivity, specificity).

**Решение:** =

---

### 479 · R1574

**Collaborating with our AI Research Companion: Exploring the Use of Microsoft Copilot to Conduct Inductive and Deductive Coding in Qualitative Research**

2026 · The Interactive Journal of Global Leadership and Learning · journalarticle, article · en · https://doi.org/10.55354/2692-3394.1083

Higher Education faculty balance time in teaching, scholarship, and service, along with many other duties in their roles (Office of Occupational Statistics and Employment Projections, 2024). In our efforts to be stewards of our time and craft, faculty look for ways to be more efficient in these areas. With the increase of Artificial Intelligence (AI) in our personal and professional lives, this paper discusses the use of Generative Artificial Intelligence (GAI), Microsoft Copilot, as an analytic tool in the qualitative data analysis process. Qualitative data was collected from transcripts of recorded meetings and an online journal that included text and photograph entries. The qualitative data from these documents were uploaded to Copilot to analyze for codes and patterns using both inductive and deductive coding methods. The output is presented and discussed raising issues of accuracy, reliability, and dependability of Copilot’s output.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Copilot coded qualitative transcripts and journals; it is unclear whether results were compared with human coding or whether the construct is psychological.

**Решение:** =

---

### 480 · R1637

**Inference Gap in Domain Expertise and Machine Intelligence in Named Entity Recognition: Creation of and Insights from a Substance Use-related Dataset.**

2026 · Pacific Symposium on Biocomputing. Pacific Symposium on Biocomputing · journal article, journalarticle, preprint/article · eng · https://doi.org/10.1142/9789819824755_0002

Nonmedical opioid use is an urgent public health challenge, with far-reaching clinical and social consequences that are often underreported in traditional healthcare settings. Social media platforms, where individuals candidly share first-person experiences, offer a valuable yet underutilized source of insight into these impacts. In this study, we present a named entity recognition (NER) framework to extract two categories of self-reported consequences from social media narratives related to opioid use: ClinicalImpacts (e.g., withdrawal, depression) and SocialImpacts (e.g., job loss). To support this task, we introduce RedditImpacts 2.0, a high-quality dataset with refined annotation guidelines and a focus on first-person disclosures, addressing key limitations of prior work. We evaluate both fine-tuned encoderbased models and state-of-the-art large language models (LLMs) under zero- and few-shot in-context learning settings. Our fine-tuned DeBERTa-large model achieves a relaxed tokenlevel F1 of 0.61 [95% CI: 0.43-0.62], consistently outperforming LLMs in precision, span accuracy, and adherence to task-specific guidelines. Furthermore, we show that strong NER performance can be achieved with substantially less labeled data, emphasizing the feasibility of deploying robust models in resource-limited settings. Our findings underscore the value of domain-specific fine-tuning for clinical NLP tasks and contribute to the responsible development of AI tools that may enhance addiction surveillance, improve interpretability, and support real-world healthcare decision-making. The best performing model, however, still significantly underperforms compared to inter-expert agreement (Cohen's kappa: 0.81), demonstrating that a gap persists between expert intelligence and current state-of-the-art NER/AI capabilities for tasks requiring deep domain knowledge. The dataset, annotation guidelines, appendix, and training scripts are publicly available to support future research.**https://github.com/SumonKantiDey/Reddit_Impacts_NER.

**ИИ:** + · обе модели · бенчмарк с метками людей · LLMs (zero/few-shot) evaluated against expert annotations of self-reported opioid-use clinical/social impacts (e.g., depression, withdrawal) in Reddit posts.

**Решение:** =

---

### 481 · R1651

**Sycophancy Through a Five-Level AI Response Validation Framework**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.03731

AI sycophancy, the tendency of AI systems to excessively agree with, flatter, or validate users, is an emerging concern in human-AI interaction. It is especially consequential in problem-sharing contexts, where users may seek both information and emotional validation. This paper conceptualizes AI sycophancy as excessive response validation and introduces a five-level AI Response Validation Framework (ARVF), measured using a six-item Perceived AI Sycophancy Scale (PASS). Across three phases, the study validated the framework with human participants through an online questionnaire, tested LLM-as-evaluators in answering PASS, and examined how ten contemporary LLMs generated and evaluated responses to real-world work and personal conflict scenarios. Results supported the intended progression of perceived sycophancy in ARVF and the reliability of PASS. Trust and perceived competence followed an inverted U-shaped pattern. LLM ratings reproduced the five-level structure but showed calibration differences from human ratings. Based on the LLM ratings, the ten contemporary LLMs were grouped according to their behavioral pattern. Text-based analysis provided further support on the linguistical structure for sycophantic responses generated by LLMs. Findings highlight AI sycophancy as a graded, context-sensitive interactional phenomenon.

**ИИ:** ? · обе модели · неясен конструкт · LLMs and humans both rate perceived sycophancy/emotional validation of AI responses to personal conflicts; unclear whether this counts as a psychological construct.

**Решение:** =

---

### 482 · R1674

**Annotating Motivational Interviewing Transcripts Using Large Language Models**

2026 · Lecture notes in computer science · journalarticle, book-chapter, conference-paper · en · https://doi.org/10.1007/978-3-032-30813-9_75

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; the title describes LLM annotation of motivational interviewing transcripts, which likely involves comparison with human coding.); Sonnet + (кодирование сессий: No abstract, but the title says LLMs annotate motivational interviewing transcripts. This almost certainly means LLM coding compared with human MI codes, so it should go to full text.)

**Решение:** +

---

### 483 · R1715

**Evaluating effectiveness and engagement strategies for asynchronous, messaging, trauma-focused therapy for posttraumatic stress disorder: Study design and methodology for a hybrid effectiveness-implementation randomized controlled trial.**

2026 · Contemporary clinical trials · clinical trial protocol, research-article, journal article · eng · https://doi.org/10.1016/j.cct.2025.108149

Posttraumatic stress disorder (PTSD) can be a chronic and debilitating condition with significant individual and societal costs. Despite the availability of effective, trauma-focused treatments like Cognitive Processing Therapy (CPT), access and sustained engagement remain limited due to logistical, financial, and stigma-related barriers. The current study utilized a hybrid effectiveness-implementation randomized control trial (N = 300) to evaluate the clinical effectiveness and feasibility of CPT-Text, an asynchronous, therapist-delivered messaging version of CPT, compared to culturally informed treatment-as-usual (CI-TAU) delivered via secure text on the Talkspace platform. Participants were also randomized to receive either standard engagement reminders (RAU) or a novel engagement incentive (RAU + I), which encourages altruism by offering participants the opportunity to "pay forward" credits for free therapy to another PTSD-affected individual through their continued participation. Primary outcomes include PTSD symptom severity (PCL-5) and engagement (e.g., treatment completion and messaging frequency), with secondary outcomes assessing depression, functioning, satisfaction, substance use. We hypothesize that CPT-Text will outperform CI-TAU in symptom reduction, and that RAU + I will enhance engagement and outcomes. Exploratory analyses will examine individual-level moderators and motivation as a mechanism of change. A novel component of this trial includes development of a large language model-based fidelity assessment tool for CPT-Text, allowing scalable evaluation of treatment delivery. Findings will inform scalable, effective, and accessible PTSD interventions that meet the needs of individuals underserved by traditional mental health care, and provide insight into how human-delivered, technology-mediated therapy can be both clinically robust and broadly accessible. Evaluating Asynchronous Messaging Therapy for PTSD.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: Trial protocol; it plans an LLM-based CPT fidelity tool but reports no LLM–human agreement data.); Sonnet ? (неясно, сравнивали ли с людьми: RCT protocol including an LLM-based CPT fidelity tool for therapy messages; likely validated against human fidelity ratings, but the abstract doesn't say. Protocol status makes it uncertain.)

**Решение:** -

---

### 484 · R1726

**Automated Safety Plan Scoring in Outpatient Mental Health Settings Using Large Language Models: Exploratory Study.**

2026 · JMIR mental health · journal article, journalarticle, article · eng · https://doi.org/10.2196/79010

Abstract Background The safety planning intervention (SPI) is a suicide prevention intervention that results in a written plan to help patients reduce suicide risk. High-quality safety plans—that is, those that are the most complete, personalized, and specific—are more effective in reducing suicide risk. Measuring SPI quality is labor-intensive, which means that clinicians rarely get specific, actionable feedback on their use of the SPI. Objective This study aimed to develop the Safety Plan Fidelity Rater, an automated tool that assesses the quality of written safety plans leveraging 3 large language models (LLMs)—GPT-4, LLaMA 3, and o3-mini. Methods Using 266 deidentified safety plans from outpatient mental health settings in New York, LLMs analyzed four key steps: warning signs, internal coping strategies, making the environment safe, and reasons for living. We compared the predictive performance of the three LLMs, optimizing scoring systems, prompts, and parameters. Results Findings showed that LLaMA 3 and o3-mini outperformed GPT-4, with different step-specific scoring systems recommended based on weighted F1-scores. Conclusions These findings highlight LLMs’ potential to provide clinicians with timely and accurate feedback on safety plan quality, which could greatly improve its implementation in community practice.

**ИИ:** + · обе модели · клиническая оценка · GPT-4, LLaMA 3 and o3-mini scored the quality of written suicide safety plans. Weighted F1 implies comparison against human fidelity ratings.

**Решение:** =

---

### 485 · R1760

**Personality-Adaptive Conversational AI for Emotional Support: A Simulation Study Integrating Big Five Detection with Zurich Model-Inspired Regulation**

2026 · Electronics · journalarticle, review, text/journal article · https://doi.org/10.3390/electronics15184241

LLM-based conversational agents generate fluent responses but remain limited in adapting their supportive style to individual personality and emotional needs. We present a Detect–Regulate–Evaluate (D–R–E) architecture that performs turn-by-turn Big Five detection and applies Zurich Model-inspired behavioural regulation, orchestrated with PROMISE. The novelty is this integrated, reproducible detection→regulation→evaluation architecture for controlled simulation—not a claim of clinical effectiveness. In a GPT-4 simulation comparing personality-adapted (regulated) and standard (non-adaptive) assistants, scored by a structured LLM-based evaluator with author review retained as an internal audit, the main finding is the mixed-personality comparison with identical user text (input replay; outcome-scoring protocol not independently archived in full): dimension-level accuracy fell to 58.1%, yet three cross-family LLM judges retained a Personality Needs advantage, locating the extreme-profile result as an upper bound. Under extreme boundary-condition profiles, strict all-five-trait recovery was 21/60 (35.0%) and dimension-level accuracy was 83.3%; regulation adherence was 100%, and the Personality Needs Yes rate rose from 8.3% (5/60) to 100% (60/60) as an upper-bound selective-enhancement check. A two-rater verify-and-revise audit on an n=66 overlap showed substantial agreement on detection labels (mean linear κ=0.731) but covered detection labels only; outcome rubrics remain LLM-rated. Safety behaviours (crisis handling, unsafe advice, hallucination, escalation) were not evaluated. The Zurich mapping is implemented as a design choice rather than validated as psychological theory; the system is not evaluated as a therapeutic or clinical intervention.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · GPT-4 detects Big Five from simulated text; a two-rater audit of detection labels is reported, but it's unclear whether that is LLM–human agreement.

**Решение:** =

---

### 486 · R1765

**ChatGPT as a Cognitive Support Tool: Experimental Evidence on Its Effects on Creativity and Problem-Solving Skills**

2026 · Thinking Skills and Creativity · article · en · https://doi.org/10.1016/j.tsc.2026.102400

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Experimental study of how using ChatGPT affects human creativity and problem-solving; the title gives no sign of an LLM coding task compared with humans.); Sonnet ? (нет аннотации: No abstract; experimental study of ChatGPT's effects on creativity, likely humans' performance rather than LLM coding. Could involve LLM scoring of divergent thinking, so full text is worth checking.)

**Решение:** -

---

### 487 · R1779

**Detecting Pediatric Emergency Service Use for Suicide and Self-Harm: Multimodal Analysis of 3828 Encounters.**

2026 · JMIR mental health · journal article, journalarticle, review · eng · https://doi.org/10.2196/82371

Abstract Background Suicide is the second-leading cause of US childhood mortality after 9 years of age. The accurate measurement of pediatric emergency service use for self-injurious thoughts and behaviors (SITB) remains challenging, as diagnostic codes undercount children. This measurement gap impedes public health and prevention efforts. Current research has not established which combination of electronic health record data elements achieves both high detection accuracy and consistent performance across youth populations. Objective This study aims to (1) compare the detection accuracy of electronic health record−based methods for identifying SITB-related pediatric emergency department (ED) visits: basic structured data (International Classification of Diseases Version 10, Clinical Modification codes, chief concern), comprehensive structured data, clinical note text with natural language processing, and hybrid approaches combining structured data with notes; and (2) for each method, measure variability in detection by youth demographics and underlying mental health diagnosis. Methods Multiple human experts reviewed clinical records of 3828 pediatric mental health emergency visits (28,861 clinical notes) to a large health system with 2 EDs (June 2022-October 2024). The reviewers used the Columbia Classification Algorithm for Suicide Assessment to label the presence of SITB at the visit. Random forest classifiers were developed using 3 data modalities: (1) structured data (low-dimensional [International Classification of Diseases codes and chief concerns], medium-dimensional [adding Columbia Suicide Severity Rating Scale screening or mental health diagnoses], and high-dimensional [all structured data or augmented case surveillance, aCS]); (2) text data (general-purpose natural language processing, medical text-specific trained natural language processing, and Large Language Model Meta AI−derived scores), and (3) hybrid data (combining aCS with each text approach). Model performance was evaluated using area under the receiver operating characteristic curve (AUROC). Results Of the 3828 visits, 1760 (n=1760, 46.0%) were SITB-related. Detection performance improved with dimensionality: low-dimensional (AUROC=0.865), medium-dimensional (AUROC=0.934‐0.935), and high-dimensional (AUROC=0.965). Low-dimensional structured (International Classification of Diseases codes and chief concerns) showed high variability in detection, with lower accuracy among preadolescents (AUROC=0.821 vs 0.880 for adolescents); male participants (AUROC=0.817 vs 0.902 for females); and patients with neurodevelopmental (AUROC=0.568‐0.809), psychotic (AUROC=0.718), and disruptive disorders (AUROC=0.703). Hybrid modality (aCS+Large Language Model Meta AI) achieved optimal performance (AUROC=0.977), with AUROC ≥0.90 for all 20 demographic and 12/15 diagnostic subgroups. Conclusions This cross-sectional retrospective study identified that, relative to diagnostic codes and chief concern alone, hybrid structured-text detection methods improved accuracy and mitigated unwanted detection variability. The findings offer a scaffold for future clinical deployment of improved information retrieval of pediatric suicide and self-harm−related emergencies.

**ИИ:** ? · обе модели · другое · Experts labeled suicide/self-harm in ED notes; LLaMA-derived scores were used mainly as random forest features. Unclear whether LLM-alone agreement is reported.

**Решение:** =

---

### 488 · R1815

**Disagreement as Data: Reasoning Trace Analytics in Multi-Agent Systems**

2026 · International Learning Analytics and Knowledge Conference (LAK) · journalarticle, book, review · https://doi.org/10.1145/3785022.3785101

Learning analytics researchers often analyze qualitative student data such as coded annotations or interview transcripts to understand learning processes. With the rise of generative AI, fully automated and human-AI workflows have emerged as promising methods for analysis. However, methodological standards to guide such workflows remain limited. In this study, we propose that reasoning traces generated by large language model (LLM) agents, especially within multi-agent systems, constitute a novel and rich form of process data to enhance interpretive practices in qualitative coding. We apply cosine similarity to LLM reasoning traces to systematically detect, quantify, and interpret disagreements among agents, reframing disagreement as a meaningful analytic signal. Analyzing nearly 10,000 instances of agent pairs coding human tutoring dialog segments, we show that LLM agents' semantic reasoning similarity robustly differentiates consensus from disagreement and correlates with human coding reliability. Qualitative analysis guided by this metric reveals nuanced instructional sub-functions within codes and opportunities for conceptual codebook refinement. By integrating quantitative similarity metrics with qualitative review, our method has the potential to improve and accelerate establishing inter-rater reliability during coding by surfacing interpretive ambiguity, especially when LLMs collaborate with humans. We discuss how reasoning-trace disagreements represent a valuable new class of analytic signals advancing methodological rigor and interpretive depth in educational research. LAK 2026 conference paper, 7 pages

**ИИ:** ? · обе модели · неясен конструкт · LLM agents code tutoring dialogue alongside human coders, but instructional codes may not count as a psychological construct; LLM–human agreement is unclear.

**Решение:** =

---

### 489 · R1826

**Synthetic Instrument Validation of Pediatric Trust Instruments using Large Language Models**

2026 · McGill University · dissertation/https://vocabularies.coar-repositories.org/resource_types/c_46ec/, dissertation · en · https://doi.org/10.82308/56039

Dan Poenaru (Supervisor) Trust forms the foundation of patient-physician therapeutic relationships and is positively associated with care-seeking, collaboration and adherence in primary care. However, data on trust formation remains sparse in pediatric emergency and surgical care contexts, where brief, emotionally charged and high-risk circumstances require tailored measurement instruments.Traditional instrument validation is time- and resource-intensive, limiting the feasible development of appropriate tools. This prevents efforts to understand healthcare quality and identify improvements. Therefore, this thesis hypothesizes that large language models (LLMs) can improve feasibility of instrument validation by creating a synthetic instrument validation (SIV) framework that maintains rigorous psychometric principles. Evaluation of the SIV framework will occur in two phases: phase one will involve subjective assessments for content validation and phase two will assess the LLMs quality of quantitative analyses for semantic overlap and accessibility metrics.Four novel trust instruments were developed to measure the experience of trust and what creates it; two patient-family instruments (Trust-Experience-Patient-Family [TRUST-E-F]; Trust-Building Blocks-Patient-Family [TRUST-BB-F]) and two physician instruments (Trust-Perception-Physician [TRUST-P-MD]; Trust-Building Blocks-Physician [TRUST-BB-MD]). Phase one involved a parallel human and synthetic expert panel for dimensional and contextual content validation, using Scale-Content Validity Index (S-CVI ≥0.80) and Fleiss’ kappa for inter-rater reliability against human ground truth. In phase two, LLMs served as co-researchers, replicating or deriving metrics against algorithmic standards. All instruments underwent cosine similarity analysis for semantic overlap, while patient-family instruments received Flesch-Kincaid readability assessments (target: 8th grade level, score ~60). LLMs were then engaged in discussion to probe reasoning pathways, reveal limitations, and optimize prompt engineering.In phase one, S-CVI scores exceeded 0.80 across all instruments and validation rounds, indicating content validity of all four instruments. Combined human-synthetic expert panels demonstrated high inter-rater reliability with the lowest Fleiss kappa of 0.71 for TRUST-BB-F dimensional rounds. In phase two, readability metrics met accessibility standards across methods, converging at grade level 8.1 ± 1.1 and readability score 60.1 ± 5.6. Cosine similarity analysis revealed LLM limitations in quantitative psychometrics, confirming their strength in subjective assessments while establishing clear boundaries for appropriate use cases. Key themes emerged from LLM interactions: dishonesty risks, technical capacity limits, preference for simpler routes, and underlying rules guiding task-appropriate applications.This study preliminarily validates trust instruments for pediatric emergency and surgical care, demonstrating more feasible validation processes. While persona-prompted LLMs established their ability to participate effectively in instrument validation, particularly in subjective assessments like content validity. Their limitations in quantitative tasks which stemmed from their stochastic and sycophantic tendencies warrant further exploration, with current software recommended for now. Future SIV development could incorporate AI co-researchers that route tasks to appropriate models to reliably and effectively complete. Overall, these findings establish preliminary pathways for using LLMs to create tailored instruments that improve the understanding of patient care and how it can be improved. La confiance forme le fondement des relations thérapeutiques patient-médecin et est positivement associée à la recherche de soins, collaboration et adhésion en soins primaires. Cependant, les données sur la formation de la confiance demeurent rares en urgence pédiatrique et chirurgie, où circonstances brèves, émotionnellement chargées et à haut risque nécessitent instruments de mesure adaptés. La validation traditionnelle des instruments est chronophage et gourmande en ressources, limitant développement d’outils appropriés. Cela empêche efforts pour comprendre qualité des soins de santé et identifier améliorations. Cette thèse émet l’hypothèse que les grands modèles de langage (GML) améliorent faisabilité de validation des instruments via cadre de validation synthétique des instruments (SIV) maintenant principes psychométriques rigoureux. Évaluation en deux phases: phase un avec évaluations subjectives pour validation de contenu; phase deux évaluant qualité des analyses quantitatives des GMLs pour chevauchement sémantique et métriques d’accessibilité.Quatre nouveaux instruments de confiance mesurent expérience de confiance et ses facteurs: deux patient-famille (Trust-Experience-Patient-Family TRUST-E-F; Trust-Building Blocks-Patient-Family TRUST-BB-F) et deux médecin (Trust-Perception-Physician TRUST-P-MD; Trust-Building Blocks-Physician TRUST-BB-MD). Phase un: panel humain et synthétique parallèle pour validation dimensionnelle et contextuelle de contenu, utilisant Indice de validité de contenu de l’échelle (S-CVI: ≥0,80) et kappa de Fleiss pour fiabilité inter-évaluateurs vs référence humaine. Phase deux: GML comme co-chercheurs répliquant ou dérivant métriques vs normes algorithmiques; tous instruments par similarité cosinus, instruments patient-famille par lisibilité Flesch-Kincaid (cible: 8e année, ~60). Les GMLs discutés pour sonder raisonnement, révéler limitations et optimiser ingénierie des invités.Dans la phase un, les scores S-CVI ont dépassé 0,80 pour tous les instruments et toutes les rondes de validation, indiquant la validité de contenu des quatre instruments. Les panels d’experts humains et synthétiques combinés ont démontré une fiabilité inter-évaluateurs élevée, avec le kappa de Fleiss le plus bas de 0,71 pour les rondes dimensionnelles de TRUST-BB-

**ИИ:** ? · обе модели · неясен конструкт · LLM and human expert panels both rated the content validity of trust questionnaire items (Fleiss kappa reported), but the items are not participant-written psychological text.

**Решение:** =

---

### 490 · R1894

**AraHopeCorpus: Annotation Guidelines and Dataset for Hope Speech in Arabic Social Media Crisis Discourse**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.23325

Social media has become a crucial arena for shaping public narratives during armed conflicts, providing space for both harmful and constructive communication. While hate speech and misinformation have been widely studied, expressions that promote resilience, solidarity, and optimism remain underexplored, particularly in Arabic contexts. This paper introduces AraHopeCorpus, the first annotated dataset of Arabic hope speech collected from ten thousand YouTube comments related to the war on Gaza between 2023 and 2024. Using a detailed annotation framework, comments were classified into three categories: hope speech, no hope speech, and neutral or unclear discourse. The dataset shows that hopeful language dominates, accounting for more than sixty four percent of all comments. These expressions of hope appear mainly as religious encouragement, collective solidarity, and optimism for endurance and justice. No hope speech, representing about thirteen percent, reflects despair and disillusionment, while the rest of the comments contain neutral or mixed content. Inter-Annotator Agreement reached substantial levels (Cohen's Kappa equals 0.71), though dialectal variation, sarcasm, and implicit meaning posed annotation challenges. A comparative analysis between human annotators and ChatGPT revealed that large language models can support annotation but remain limited in handling dialectal and culturally embedded expressions. AraHopeCorpus will be released for research purposes under an open and non commercial license. It provides a valuable resource for studying constructive digital discourse, enabling further research on hope speech detection, crisis communication, and resilience in Arabic social media.

**ИИ:** разошлись — Opus ? (неясен конструкт: ChatGPT compared with human annotators on hope versus despair in Arabic comments; unclear if hope speech counts as a psychological construct or a discourse category.); Sonnet + (бенчмарк с метками людей: Arabic hope-speech dataset with human annotation (kappa 0.71) and a ChatGPT vs human annotator comparison; hope/despair is an emotional-cognitive construct.)

**Решение:** +

---

### 491 · R1924

**Large Language Models in metaphor identification -- The case of presuicidal interaction**

2026 · Repository of the Academy's Library (Library of the Hungarian Academy of Sciences) · article · en · https://real.mtak.hu/247412/1/Acta_paper_revised_after%20editorial%20notes.pdf

This paper addresses the challenge of automating metaphor identification in Hungarian using generative AI technology. Our tool uses a dictionary-augmented chain-of-thought prompting method to perform metaphor identification and implements a widely used protocol for manual annotation. The study employs a curated corpus of online forum posts about suicidal ideation, with manually annotated linguistic metaphors. It describes the challenges of automating metaphor annotation, discusses alternative methodological approaches to address these issues, outlines the project’s materials, and assesses the performance of the models (reporting on ~89% of general accuracy and ~79% of balanced accuracy in the case of the best-performing model, GPT-5), concluding with suggestions for further development.

**ИИ:** ? · обе модели · неясен конструкт · GPT-5 identifies metaphors in suicidal-ideation forum posts against manual annotation; metaphor is mainly a linguistic construct, so psychological relevance is unclear.

**Решение:** =

---

### 492 · R1928

**IDEAFix: Evaluation Framework for Creative Defixation Prompting in LLMs**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.00875

Large language models (LLMs) are increasingly used for tasks involving creative problem solving and idea generation. However, there is a lack of consensus concerning their creative capabilities: some studies report superior performances compared to humans, while others highlight structural limitations such as fixation and the homogenization of outputs. Existing evaluation approaches either rely on narrow, decontextualized tasks that do not capture goal-oriented generation or on broader settings that confound multiple aspects of the creative process, making it difficult to isolate the effects of task formulation, prompting, and evaluation design. Significantly, the role of structured prompting strategies in shaping idea generation remains underexplored. Therefore, we introduce IDEAFix, an evaluation framework for analyzing divergent thinking in open-ended idea generation tasks. We prompt models to generate multiple original solutions to controlled variations of short design scenarios, task attributes, and defixation prompting strategies. This design enables systematic analysis of how structured guidance influences LLMs' idea generation. Our results show that both task formulation and attribute selection significantly affect models' performance, and that simple prompting strategies can boost the originality of solutions. However, we also observe persistent output homogenization across models, confirming inherent limits in their ability to generate diverse solutions. Overall, IDEAFix provides a controlled, extensible framework for studying the mechanisms underlying LLMs' creativity.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mainly LLM idea generation; originality scoring of divergent thinking may use an LLM judge, but the abstract never says it was checked against human raters.

**Решение:** =

---

### 493 · R1949

**Advancing Ransomware Detection with Machine Learning: Human Factors, Evolution, and Detection**

2026 · Research Repository UCD (University College Dublin) · dissertation · en · http://hdl.handle.net/10197/32613

Ransomware has become one of the most disruptive and adaptive cyber threats, exploiting both human vulnerabilities and evolving technical behaviours to compromise systems across all sectors. Its progression from simple locker ransomware to sophisticated ransomware-as-a-service (RaaS) ecosystems has outpaced traditional defences, exposing critical gaps in ransomware understanding and detection. This thesis addresses five of these gaps by integrating human-centred analysis, large-scale behavioural data, longitudinal modelling, multimodal learning, and ATT&CK technique prediction towards advancing machine–learning–based ransomware detection. The research begins by examining the human gateway through which many ransomware campaigns unfold: phishing. Analysis of more than 5,000 phishing and non-phishing emails reveals that attackers consistently manipulate six affective states (fear, urgency, greed, curiosity, trust, and compassion) in structured and measurable ways. By comparing human annotations with multiple Large Language Models, the study demonstrates that emotional cues offer a reliable signal for early-stage detection, establishing that ransomware defence must consider how users are psychologically targeted before technical payloads are deployed. Building on this, the thesis addresses the scarcity of representative behavioural ransomware datasets, a fundamental barrier to the development of reliable machine learning models. It introduces MLRan, MLRan-MITRE, and MLRan-Image, a suite of datasets created under the GUIDE-MLRan framework to ensure diversity, temporal breadth, reproducibility, and rich behavioural detail. MLRan provides large-scale dynamic behavioural features for ransomware and benign software; MLRan-MITRE extends this with MITRE ATT&CK technique annotations for each sample; and MLRan-Image transforms behavioural traces into compact image representations to support multimodal learning. These datasets enable robust benchmarking and interpretable modelling, providing the empirical foundation required to study ransomware at scale. With this foundation in place, the thesis conducts the first integrated longitudinal and empirical analysis of ransomware behaviour from 2006 to 2024. Four evolutionary phases (Locker, Crypto, RaaS, and Modern) are identified, and their behavioural implications are quantified. The findings show that ransomware evolution introduces substantial drift in feature importance and model performance, revealing that effective detection requires training on behaviourally diverse data and adopting evaluation protocols that are time-aware, type-aware, and evolution-sensitive. The final part of the thesis introduces two methodological contributions to develop advanced methods to address these challenges. SupConRAN, a multimodal supervised contrastive learning framework, improves fine-grained family classification by combining behavioural images with tabular features. ATTAXML, which goes beyond classification by directly predicting MITRE ATT&CK techniques from behavioural telemetry, enables models to infer adversarial intent rather than merely flag malicious activity.

**ИИ:** ? · обе модели · неясен конструкт · Thesis chapter compares human annotations of affective manipulation cues (fear, urgency, trust) in phishing emails with LLMs; unclear whether this counts as a psychological construct.

**Решение:** =

---

### 494 · R1960

**Long-Context Mental Health Assessment with Large Language Models via Knowledge Compression**

2026 · IEEE Transactions on Affective Computing · article · https://doi.org/10.1109/taffc.2026.3669164

Assessing mental disorder causes and severity from social media history or clinical interviews is essential for early intervention and monitoring population mental health. However, existing methods face several challenges, especially under long-context: the inherently noisy and lengthy nature of online content obscures crucial clinical signals, while the computational intensity of Transformer-based models limits practical deployment. To address these issues, this paper proposes MindSpan, a novel framework that enhances automated mental health profiling by knowledge-augmented compression with output-controlled generation. Specifically, MindSpan first compresses the input long-context by actively retrieving and retaining the top symptom-relevant snippets, effectively filtering out irrelevant information. Then it applies a profiling-specific generation template that constrains the Large Language Models (LLMs) to produce structured, consistent, and clinically interpretable severity ratings. Experiments on two public benchmarks demonstrate that MindSpan achieves better performance. This work provides a practical and efficient solution for scalable, automated mental health assessment

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM rates mental-disorder severity on public benchmarks; unclear if labels are human-coded or self-report questionnaires (e.g., PHQ-8, BDI).

**Решение:** =

---

### 495 · R1961

**TherapyGym: Evaluating and Aligning Clinical Fidelity and Safety in Therapy Chatbots**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2603.18008

Large language models (LLMs) are increasingly used for mental-health support; yet prevailing evaluation methods--fluency metrics, preference tests, and generic dialogue benchmarks--fail to capture the clinically critical dimensions of psychotherapy. We introduce THERAPYGYM, a framework that evaluates and improves therapy chatbots along two clinical pillars: fidelity and safety. Fidelity is measured using the Cognitive Therapy Rating Scale (CTRS), implemented as an automated pipeline that scores adherence to CBT techniques over multi-turn sessions. Safety is assessed using a multi-label annotation scheme, covering therapy-specific risks (e.g., failing to address harm or abuse). To mitigate bias and unreliability in LLM-based judges, we further release THERAPYJUDGEBENCH, a validation set of 116 dialogues with 1,270 expert ratings for auditing and calibration against licensed clinicians. THERAPYGYM also serves as a training harness: CTRS and safety-based rewards drive RL with configurable patient simulations spanning diverse symptom profiles. Models trained in THERAPYGYM improve on expert ratings, with average CTRS rising from 0.10 to 0.60 (and 0.16 to 0.59 under LLM judges). Our work enables scalable development of therapy chatbots that are faithful to evidence-based practice and safer in high-stakes use.

**ИИ:** + · обе модели · LLM-судья · LLM judges score CTRS fidelity and safety of therapy dialogues, validated against licensed clinician expert ratings (TherapyJudgeBench).

**Решение:** =

---

### 496 · R1970

**Multi-Source Emotion Annotation in Children’s Language: When LLM Consensus Diverges from Human Judgment**

2026 · Language Resources and Evaluation Conference (LREC) · conference, conference-paper · en · https://doi.org/10.63317/39tk69v6ca4p

Automated emotion annotation increasingly relies on inter-LLM agreement as a proxy for label quality. We test this assumption on 2,106 clause-level segments from interviews with French-speaking children (ages 6–11) about parental roles, a setting where affect is often implicit rather than lexically explicit. Using a 500-segment expert gold standard, we show that internal consensus can be seriously misleading: Dawid–Skene, a probabilistic label aggregation method, estimates GPT-5.2 valence accuracy at 90.7%, whereas evaluation against human gold yields 71.0%, revealing substantial overestimation driven by shared neutralization bias. Conversely, Dawid–Skene underestimates Claude Sonnet 4, reversing model ranking. Majority Vote, Dawid–Skene, and MACE produce near-identical consensus labels, suggesting that the main source of error lies in shared annotator bias rather than in the aggregation rule itself. We release the expert gold subset and the probabilistic corpus to support future work. Our results show that high inter-LLM agreement cannot replace external human validation for affect annotation.

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT-5.2 and Claude labelled emotion valence in children's interview segments and were scored against a 500-segment expert gold standard.

**Решение:** =

---

### 497 · R1971

**Structured Claim-Level Discourse Representations for Dense Health Narratives**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.18905

Health discourse in social media videos often contains densely entangled claims spanning multiple thematic aspects, stances, evidential frames, and rhetorical functions within short conversational spans. Existing approaches largely rely on coarse topic-level, sentiment-based, or stance-oriented representations that do not adequately capture this structure. Our analysis identifies an average of 13.22 atomic claims per minute, motivating richer claim-level discourse representations. We introduce a structured framework for claim-level discourse analysis in dense health narratives. Our framework models discourse through tuples linking atomic claims with thematic aspects, stance, and multidimensional pragmatic discourse attributes. To support this setting, we construct a benchmark spanning four health domains with 1,191 manually annotated claims from 60 videos. Using this framework, we evaluate automated structured discourse analysis under different discourse context settings. Results show that current LLMs achieve strong performance on thematic categorization and stance prediction, but struggle with high-dimensional pragmatic profiling. We also find that different discourse tasks benefit from different forms of contextual reasoning, suggesting that future systems may require task decomposition and specialized inference strategies.

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs label health claims in videos for theme, stance and pragmatic attributes against human annotations; none of these are psychological or clinical constructs.); Sonnet ? (неясен конструкт: LLMs evaluated against manual claim annotations in health videos (benchmark), but the constructs (claims, stance, pragmatics) may not be psychological; mental-health domain unclear.)

**Решение:** -

---

### 498 · R1974

**Three Pathways of Student-AI Interaction: Constraint-First Design for Higher-Order Thinking**

2026 · arXiv (Cornell University) · preprint/article, review, preprint · https://doi.org/10.48550/arxiv.2610.00338

How students interact with artificial intelligence (AI) systems in educational settings may determine whether that interaction supports or displaces critical thinking. This paper introduces two contributions. The first is the Three Paths of Student-AI Interaction, a typological framework identifying three qualitatively distinct modes of student-AI engagement: Passive Review, Direct Question, and Strategic Dialogue. The second is the Next Level Teaching Blueprint (NLTB), a three-stage instructional design system intended to make Strategic Dialogue more likely. Qualitative content analysis of 50 randomly sampled student-AI interaction messages from an undergraduate research methods course was used to examine the typology. Two human coders achieved 68% path-level agreement ($κ$ = .48), with 80% agreement on Strategic Dialogue identification specifically. GPT-5, used as a third coder, produced a similar overall distribution and introduced a coding category absent from the human scheme. Path 1 (Passive Review) accounted for 46% of exchanges in the primary researcher's classifications, Path 2 (Direct Question) for 18%, and Path 3 (Strategic Dialogue) for 36%. A second, descriptively examined dataset contained predominantly Strategic Dialogue content, offering a preliminary indication that instructional framing may influence which path students take. Together, the Three Paths framework and the NLTB contribute a language for describing student-AI interaction and a design approach for supporting higher-order engagement. 26 Pages, 2 figures

**ИИ:** ? · обе модели · неясен конструкт · GPT-5 coded student-AI messages alongside human coders; unclear whether engagement modes count as a psychological construct or if unit-level agreement is reported.

**Решение:** =

---

### 499 · R1986

**607. When artificial intelligence becomes a rater: detecting formal thought disorders in schizophrenia**

2026 · The International Journal of Neuropsychopharmacology · journalarticle, conference-abstract · en · https://doi.org/10.1093/ijnp/pyag040.104

Abstract Background Formal thought disorders (FTDs) are a fundamental component of the psychopathology of schizophrenia (SCZ), characterized by fragmented conceptual organization and loss of associative coherence [1]. FTDs are more frequent and severe in individuals with treatment-resistant schizophrenia (TRS), who show poorer functional outcomes and higher disease burden [2]. Accurate evaluation of FTDs is essential for monitoring symptom severity and assessing treatment or rehabilitation effects. The Thought and Language Disorder (TALD) [3] scale supports a structured assessment of FTDs but remains time-consuming and influenced by clinician judgment. With advances in natural language processing (NLP), large language models (LLMs) offer the opportunity to support an objective, reproducible, and scalable assessment of language disturbances in psychiatry. Aims & Objectives This study aims to determine whether an LLM can reproduce clinician scoring of the TALD in individuals with SCZ and TRS, and to assess the agreement between automated and expert ratings. To our knowledge, this is the first study to perform a full-scale, item-level TALD scoring through an LLM. Method Thirty-three patients (14 TRS, 19 SCZ) underwent a recorded clinical interview, which was independently rated by two psychiatrists and an LLM trained on TALD scoring. TALD items were converted into quantitative metrics through two analytic frameworks: a time-stamp analysis (TSA) module to quantify temporal speech features (for example, pressured speech was assessed as pauses and words per minute), and a NLP module to assess semantic parameters (e.g., perseveration was converted into the number of repeated responses out of the total number of responses given by the patient). A mixed-design repeated-measures ANOVA tested effects of Rater (clinician vs LLM) and Group (SCZ vs TRS). Agreement was evaluated via intraclass correlation coefficient (ICC, two-way mixed, absolute agreement) for total scores and weighted Cohen’s κ for item-level concordance. Results The LLM consistently assigned slightly higher total TALD scores than clinicians (clinicians: 26.4 ± 10.7; LLM: 28.0 ± 8.0). ANOVA revealed a significant main effect of Rater (p = 0.001), with no significant Group effect and no Rater × Group interaction. Agreement for total TALD scores was good (ICC = 0.84), comparable across SCZ (ICC = 0.86) and TRS (ICC = 0.83) (Table 1). Weighted κ demonstrated moderate-to-almost-perfect concordance for most items (e.g., blockage κ ≈ 0.94), while agreement was lower for infrequent phenomena such as dissociation of thinking (κ ≈ 0.33), likely reflecting limited occurrence and broader variability in clinician scoring. Discussion & Conclusions LLM assigns slightly higher scores than clinicians - potentially reflecting the model’s lack of emotional or cultural biases. Overall agreement is good, supporting its potential role in standardising psychopathology evaluation. However, such tools are to be used under medical supervision and require further clinical validation before integration into clinical practice. With appropriate safeguards, LLM-assisted scoring could enhance reproducibility in psychiatric research and offer scalable support in the clinical assessment of SCZ and TRS.

**ИИ:** + · обе модели · клиническая оценка · An LLM scored the TALD from recorded interviews. Its ratings were compared with two psychiatrists' ratings using ICC and weighted kappa.

**Решение:** =

---

### 500 · R1988

**P2P - from Posts to Patterns: An LLM Ensemble Approach to Mental Health Dynamics Detection**

2026 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · conference-paper · en · https://doi.org/10.18653/v1/2026.clpsych-1.39

The automatic detection of mental health dynamics represents a challenging and socially relevant task, requiring models to capture subtle psychological changes over time.Large language models have demonstrated remarkable capabilities in clinical and diagnostic contexts, yet their outputs often lack consistency and may diverge significantly across different model families and prompting strategies.This paper presents the USAI team's submission to the CLPsych 2026 Shared Task, targeting Tasks 1.1, 1.2, 2, and 3.1.We propose an ensemble-based approach combining multiple open-source large language models, where the contribution of each model is weighted according to its alignment with clinically grounded human annotations on the training set.Our system achieves competitive results across the evaluated subtasks, with particularly strong performance on Tasks 1.2 and 2.

**ИИ:** + · обе модели · бенчмарк с метками людей · CLPsych shared task submission: an LLM ensemble detecting mental health dynamics in posts, evaluated against clinically grounded human annotations.

**Решение:** =

---

### 501 · R1991

**Evaluating Safety Boundaries of Large Language Models Across Mental Health Risk Scenarios: A Benchmark Study**

2026 · KTH Publication Database DiVA (KTH Royal Institute of Technology) · dissertation, thesis · en · http://urn.kb.se/resolve?urn=urn:nbn:se:uu:diva-592494

Large language models (LLMs) are increasingly used for information seeking and emotional support, sometimes even in crisis communication. As a result, their safety performance in mental health contexts has become a critical concern. Existing evaluations often focus on whether a model rejects harmful requests. However, mental health safety cannot be equated with refusal alone. A truly safe model must also identify hidden risks, avoid reinforcing possible unusual beliefs, and provide appropriate crisis resources or professional help when needed. In this study, we assessed the safety boundaries of ChatGPT-5.4, Claude Sonnet 4.6, and Gemini-3 in mental health risk scenarios. We constructed a benchmark of 190 synthetic prompts covering seven risk categories: suicidal ideation, depressive rumination, psychosis-like expressions, disorganized or loosely associated speech, anxiety, health misinformation, and accommodating questions. Model responses were evaluated using a five-category A–E framework: appropriate safe response, inadequate response, avoidant refusal, risk omission, and harmful response. We also analyzed response consistency across linguistically rephrased variants of the same scenario and assessed classification reliability through human verification and Cohen’s kappa. The results showed that ChatGPT-5.4 performed most consistently. It produced no avoidant or harmful answers in suicide-related prompts and achieved the highest complete consistency rate across paraphrased subcategories. Claude Sonnet 4.6 handled many direct expressions of suicidal ideation appropriately, but still showed safety gaps in theoretically or informationally framed suicide-method-seeking prompts. Gemini-3 was the least consistent, with frequent regional-resource errors, missed risk detection, and weaker performance in psychosis-like and disorganized-speech scenarios. Across models, ambiguous psychosis-like expressions remained more difficult than explicit suicide-risk prompts. These findings suggest that mental health safety for LLMs cannot be measured by rejection rate alone. A comprehensive assessment must include response quality, risk detection, safety strategies, and rephrasing consistency. The A–E classification framework proposed in this study provides a reproducible method for multi-model, cross-scenario safety evaluation in mental health LLM research. Future work should extend the benchmark to multi-turn dialogues, more languages, and clinical expert annotations.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mental-health safety classification checked against humans with Cohen's kappa; unclear whether an LLM judge did the classifying.

**Решение:** =

---

### 502 · R1995

**MINA: Multimodal intention analysis of social media posts via LLM-guided audio-visual-text reasoning**

2026 · Pattern Recognition · article · en · https://doi.org/10.1016/j.patcog.2026.113700

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract. An LLM-guided multimodal intention classifier for social media posts, probably tested against human-labelled benchmarks; unclear if the construct is psychological.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Multimodal intention analysis of social media posts (audio-visual-text); likely not a psychological or clinical construct, and no evidence of an LLM–human coder comparison.)

**Решение:** ?

---

### 503 · R2035

**Benchmarking Language Models for Clinical Safety: A Primer for Mental Health Professionals**

2026 · medRxiv · preprint, ppr · https://doi.org/10.64898/2026.03.20.26348900

Background Millions of people use language models to discuss mental health concerns, including suicidal ideation, but limited frameworks exist for evaluating whether these systems respond safely. Benchmarking, the practice of administering standardized assessments to language models, offers direct parallels to clinical competency evaluation, yet few clinicians are involved in designing, validating, or interpreting these assessments. Aims To introduce mental health professionals to benchmarking language models by administering a validated clinical instrument and demonstrating how configuration decisions, measurement limitations, and scoring context affect result interpretation. Method We administered the Suicide Intervention Response Inventory (SIRI-2) programmatically to nine commercially available language models from three providers. Each item was presented 60 times per model (three prompt variants × two temperature settings x 10 repetitions), yielding 27,000 model responses compared against point-in-time expert consensus. Results Total scores ranged from 19.5 to 84.0 (expert panel baseline: 32.5). Prompt design alone shifted individual model scores by as much as the difference between trained and untrained human groups. The best performing model approached the instrument’s measurement floor. All nine models consistently overrated clinically inappropriate responses that sounded supportive. Conclusions A single benchmark score can support markedly different claims depending on the assumed standard of clinical behavior, the instrument’s remaining measurement range, and the configuration that produced the result. The skills required to make these distinctions must become core competencies. Benchmark results are increasingly utilized to support claims about mental health safety that may not be accurate, making it necessary to close the gap between clinical measurement and AI. Plain Language Summary AI chatbots like ChatGPT, Claude, and Gemini are increasingly used by millions of people to discuss mental health problems, including thoughts of suicide. To assess whether these systems handle such conversations safely, researchers give them standardized tests called benchmarks and compare their answers to those of human experts. These scores are already used to argue AI systems are ready for clinical use. This study gave a well-established test of suicide response skills to nine AI models from three major companies under varying conditions. We changed how much instruction the AI received and how much randomness was built into its responses, then measured whether the scores changed. The same AI model could score like a trained crisis counselor under one set of conditions and like an untrained undergraduate under another, depending on choices the person running the test made. Every model also made the same kind of mistake: responses that sounded warm and caring were rated as appropriate, even when experts had judged them to be clinically problematic. The highest-scoring model performed so well that the test could no longer measure whether it was truly skilled or had simply exceeded the test’s range. These findings show that a single score can be misleading without knowing how the test was run, whether it can still distinguish strong from weak performance, and whether it matches what the AI is used for. Mental health professionals routinely make these judgments about clinical assessments and are well positioned to bring that expertise to AI evaluation.

**ИИ:** + · обе модели · LLM-судья · Nine LLMs rated how appropriate counselor responses were on the SIRI-2 items, and their ratings were compared with the expert-consensus ratings of the same responses.

**Решение:** =

---

### 504 · R2066

**Predicting Suicide Using Natural Language Processing of Autobiographical Memory.**

2026 · Archives of suicide research : official journal of the International Academy for Suicide Research · journal article, med, journalarticle · eng · https://doi.org/10.1080/13811118.2025.2552951

Autobiographical memory, a critical cognitive process for recalling personal events, is closely linked to mental health. Depressive disorders are characterized by overgeneralized and negative memory patterns, which impair future-oriented thinking and exacerbate hopelessness. Current evaluations of autobiographical memory are subjective and limited by human bias. In this study, we applied Natural Language Processing using Large Language Models (LLMs) to analyze autobiographical memory narratives, uncovering that their valence can predict depression, suicidal ideation, and prior suicide attempts. Furthermore, valence correlated with core components of the Three-Step Theory of suicide, such as hopelessness and lack of connectedness. By integrating advanced computational techniques, our approach demonstrated high predictive accuracy and offers a scalable, objective method for assessing suicide risk. These findings highlight the potential of LLM-based analysis in enhancing psychological assessment and informing interventions, paving the way for innovative clinical applications in mental health care.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM rates valence of autobiographical memory narratives to predict suicide outcomes; unclear whether LLM ratings were validated against human coders.

**Решение:** =

---

### 505 · R2073

**Reading between the Lines: Leveraging Large Language Models for Global Dementia and Depression Assessment from Clinical Interviews**

2026 · arXiv · preprint/article, conference-paper, preprint · en · https://doi.org/10.48550/arxiv.2606.18019

Dementia and depression are the most prevalent neuropsychiatric disorders in geriatric populations, and their overlapping symptoms pose major challenges for differential diagnosis. In this study, we investigate open-weights Large Language Models (LLMs) for predicting dementia and depression severity from speech samples collected during standardized history taking interviews with 154 German-speaking subjects. We introduce an observer-based Global Depression Scale (GDS-D) aligned with the established Global Deterioration Scale (GDS), enabling parallel global staging of affective and cognitive symptoms. We compare three LLMs (Mistral 3.1, DeepHermes, Qwen3) in two settings: (1) zero-shot prediction and (2) LLM-based feature extraction for Support Vector Regression, using human and pause-enriched transcripts. Results show that LLMs effectively predict depression severity in zero-shot settings (best MAE of 0.60), while dementia assessment benefits substantially from structured feature extraction (best MAE of 0.78), reducing errors by up to 35% over zero-shot baselines. Pause-enriched transcripts achieve competitive performance with human transcriptions, demonstrating the viability of fully automatic screening pipelines for differential neuropsychiatric assessment. Accepted for publication in Text, Speech and Dialogue (TSD 2026). The final authenticated publication will be available online via Springer LNCS/LNAI

**ИИ:** + · обе модели · клиническая оценка · Open-weight LLMs rate depression/dementia severity from interview transcripts; compared against observer-based clinician scales (GDS-D, GDS).

**Решение:** =

---

### 506 · R2085

**A multi-site benchmarking framework for scalable extraction of geriatric care constructs from electronic health records.**

2026 · npj health systems · journal article, journalarticle, article · eng · https://doi.org/10.1038/s44401-026-00114-y

Current Natural Language Processing (NLP) algorithms for detecting geriatric conditions are largely limited to domain-specific models that fail to capture the interdependent, multidimensional nature of comprehensive geriatric assessment. This study aimed to develop and evaluate a comprehensive, scalable, and robust information extraction framework to identify Comprehensive Geriatric Assessment (CGA) and Age-Friendly Health Systems (AFHS) 4Ms-related data elements from unstructured electronic health record (EHR) text across multiple health systems. Using a team science approach grounded in the TRUST framework, we annotated pooled clinical notes from four health systems to produce a gold-standard dataset of 41 CGA- and 4Ms-related geriatric care data elements. Three information extraction approaches were implemented and evaluated: an in-context learning generative large language model (GPT-4o), a hybrid heuristic-LLM model (MedAgingIE), and an instruction-tuned open-source lightweight model (Qwen2-7B-Instruct). Performance was assessed on a blinded test set using macro- and micro-averaged metrics. GPT-4o achieved a macro F1-score of 0.56 and micro F1-score of 0.87; MedAgingIE achieved 0.55 and 0.92; and Qwen2-7B-Instruct achieved 0.30 and 0.81, respectively. MedAgingIE demonstrated the strongest consistency between precision and recall, while GPT-4o showed superior sensitivity for diverse, context-rich geriatric concepts. These findings highlight key trade-offs among symbolic, generative, and instruction-tuned approaches for CGA and 4Ms phenotyping, suggesting that hybrid heuristic-LLM methods offer interpretability and stability, whereas large language models provide greater adaptability for complex clinical narratives.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs extract geriatric elements from clinical notes against a human-annotated gold standard; these may include mentation (depression, cognition, delirium), but most elements are medical.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs extract geriatric care data elements from EHR notes against annotations; this is medical or clinical information extraction, not a psychological construct.)

**Решение:** -

---

### 507 · R2094

**LLM-Generated Social-Desirability Ratings for Forced-Choice Questionnaire Construction: A Preregistered Downstream Validation**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/x9fgr_v1

Large language models (LLMs) increasingly produce evaluative judgments, but rating-level human–model agreement does not establish whether they can replace human inputs in a downstream task. Using HEXACO personality items as a case study, we conduct a preregistered three-stage validation of whether LLM-generated social-desirability ratings can serve as inputs to forced-choice scale construction, a psychometric task that requires costly human ratings. In Stage I, three LLMs served as raters of item-level social desirability for sentence- and adjective-format items, with human ratings serving as references. In Stage II, human- and LLM-based ratings were entered into the same constrained optimization procedure. In Stage III, 400 participants completed the resulting forms, and latent trait estimates were compared using graded Thurstonian item response theory. LLM ratings showed strong item-level correspondence with human ratings (sentence: r = 0.942–0.963; adjective: r = 0.979–0.980), but optimized forms showed partial item overlap and sparse exact pair overlap. Despite these design differences, LLM-based forms produced latent trait estimates that closely matched those from human-based forms (mean r = 0.815 for sentence items and 0.768 for adjective items). These results support the conditional use of LLM-generated ratings as scalable construction inputs while showing why downstream validation is necessary.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs rated social desirability of HEXACO items against human ratings; agreement is reported, but questionnaire items may not count as psychological text.); Sonnet + (подсчёт методики: LLMs rated social desirability of HEXACO personality items with human ratings as reference (r = .94–.98), so LLM–human agreement is reported.)

**Решение:** +

---

### 508 · R2105

**Evaluating Large Language Models (LLMs) for Coding Open-Ended Survey Responses: A Total Survey Error Framework**

2026 · SocArXiv (OSF Preprints) · posted-content, preprint · https://doi.org/10.31235/osf.io/2rjm6_v1

Open-ended questions are commonly used in survey research to supplement closed-ended questions by capturing respondents’ views, reasons, and priorities in their own words. However, coding these responses for analysis remains time-consuming and difficult to standardise. Recent advances in automated coding, especially through large language models (LLMs), have renewed interest in using open-ended responses at scale, but their evaluation is often difficult and framed mainly in terms of classification accuracy and agreement with human coding. This paper develops a Total Survey Error framework for evaluating automated coding of open-ended survey responses as part of survey measurement and data production. Model outputs are assessed using existing human-coded data as a high-quality operational benchmark, with the evaluation examining six complementary dimensions, such as processing agreement, measurement validity, prevalence distortion, coding density, response-form sensitivity, and operational reliability. The framework is applied to data using open-ended survey responses from the National Centre for Social Research (NatCen). The paper aims to inform how automated coding systems, including LLMs, can be assessed in practice, and what issues survey researchers should consider when evaluating their suitability for open-ended survey coding, and how improved coding may enable wider use of open-ended questions in large-scale quantitative surveys. Keywords: automated coding; large language models; measurement validity; open-ended survey responses; survey data quality; Total Survey Error

**ИИ:** ? · обе модели · неясен конструкт · LLM coding of NatCen open-ended survey responses benchmarked against human coding; unclear whether the coded content is a psychological construct.

**Решение:** =

---

### 509 · R2108

**Validating the architecture of cognitive distortions in Russian discourse using artificial intelligence and bootstrap analysis.**

2026 · Frontiers in psychology · journal article, journalarticle, article · eng · https://doi.org/10.3389/fpsyg.2026.1740864

Introduction Cognitive distortions—systematic thinking biases linked to depression and anxiety—frequently co-occur in clinical practice, yet empirical evidence for their interaction patterns remains limited, particularly in non-Western populations where cognitive patterns may vary cross-culturally. Methods We analyzed 249,414 Russian-language texts from social media and forums (2020–2024) using two large language models achieving substantial expert agreement (κ = 0.73). Association rule mining identified co-occurrence patterns; network stability was evaluated through bootstrap validation and split-half reliability analysis. Results Analysis identified 443,447 distortion instances across 18 categories (M = 1.78 per text). All-or-nothing thinking showed highest prevalence (15.5%), followed by overgeneralization (14.2%) and catastrophizing (11.4%). Network analysis identified a stable core of 11 nodes (bootstrap stability ≥95%) and 2 peripheral, less stable nodes (Fairness 93%, Fortune Telling 60.8%). The resulting 13-node network was connected by 35 significant associations (density = 0.449, clustering = 0.598). Five distortions failed stability thresholds (< 60%) and were excluded. Strongest dyadic pattern: all-or-nothing/catastrophizing ( lift = 1.96, p < 0.001). These two distortions appeared each in 67% of all significant triadic patterns. Personalization demonstrated highest degree centrality (degree = 10). Split-half reliability was high (r = 0.943). Discussion Automated classification revealed hierarchically organized co-occurrence network in Russian-language discourse with personalization as primary hub and all-or-nothing/catastrophizing forming densely connected core. Findings suggest cluster-based interventions may be effective for Russian-speaking populations, though cross-cultural replication is required to distinguish universal mechanisms from cultural patterns. Cross-sectional design and single-language sample limit causal inference and generalizability.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · Two LLMs coded cognitive distortions in Russian social-media texts, with agreement against experts reported (κ = 0.73).

**Решение:** =

---

### 510 · R2110

**Use of a Large Language Model to Reveal Narrative Architectures of Veteran Transition Stress: Development and Validation Study.**

2026 · JMIR mental health · journal article, validation study, journalarticle · eng · https://doi.org/10.2196/90155

Abstract Background The stress caused by multiple aspects of veterans’ transitions from military to civilian, termed transition stress, represents a unique source of psychological impact that is underresearched due to its qualitative nature. The assessment of this complex psychological phenomena has thus relied on laborious interviews designed to extract quantitative information from qualitative narratives of the transition to civilian life. We sought to determine if large language models (LLMs) could be used as valid measurement tools to extract relevant information from open-ended narratives. Objective This study sought to develop and validate a generative artificial intelligence (AI) approach to automate the quantification and subsequent thematic analysis of veteran transition stress. Methods Utilizing transcripts from interviews of a sample of US military veterans, we developed an LLM to rate transition stress severity and examined the model’s reliability in relation to human coders and validity in relation to a set of related questionnaire measures. Next, we used the LLM scores to quantitatively define high and low transition stress groups, enabling a targeted, automated analysis of themes related to narrative identity and life transition themes that might differentiate the two groups. Results LLM ratings of transition stress correlated highly with the human expert ratings and showed significant, theoretically congruent correlations with measures of clinical symptoms, reintegration difficulties, and veterans’ self-ratings of transition difficulty. Critically, the AI-derived thematic analyses of the narratives from high and low transition stress veterans revealed clearly distinct and informative patterns. Conclusions These findings suggest that generative AI offers a robust, scalable, and reliable method for multidimensional analysis of complex, narrative-based psychological constructs.

**ИИ:** + · обе модели · клиническая оценка · LLM rated transition stress severity from veteran interview transcripts; the ratings were correlated with human expert ratings.

**Решение:** =

---

### 511 · R2117

**LLA MADRS: Evaluating Open-Source LLMs on Real Clinical Interviews—To Reason or Not to Reason?**

2026 · Transactions of the Association for Computational Linguistics · journalarticle, preprint/article, article · en · https://doi.org/10.1162/tacl.a.741

Abstract Large language models (LLMs) excel on many NLP benchmarks, but their behavior on real-world, semi-structured prediction remains underexplored. We present LLAMADRS, a benchmark for structured clinical assessment from dialogue built on the CAMI corpus of psychiatric interviews, comprising 5,804 expert annotations across 541 sessions. We evaluate 25 open-source models (standard and reasoning-augmented; 0.6B–400B parameters) and generate over 400,000 predictions. Our results demonstrate that strong open-source LLMs achieve item-level accuracy with residual error below clinically substantial thresholds. Additionally, an Item-then-Sum (ITS) strategy, assessing symptoms individually through discrete LLM calls before synthesizing final scores, significantly reduces error relative to Direct Total Score (DTS) prediction across most model architectures and scales, despite reasoning models attempting similar decomposition in the reasoning traces of their DTS predictions. In fact, we find that performance gains attributed to “reasoning” depend fundamentally on prompt design: standard models equipped with structured task definitions and examples match reasoning-augmented counterparts. Among the latter, longer reasoning traces correlate with reduced error; while higher model scale does across both architectures. Our results clarify when and why reasoning helps and offer actionable guidance for deploying LLMs in semi-structured clinical assessment.

**ИИ:** + · обе модели · клиническая оценка · LLMs rate MADRS depression items from real psychiatric interview transcripts and are compared with expert clinician annotations.

**Решение:** =

---

### 512 · R2128

**From politicisation to polarisation Von Politisierung zu Polarisierung**

2026 · :none · text/thesis · https://doi.org/10.25365/thesis.81658

Diese Arbeit untersucht, ob die Politisierung des parlamentarischen Diskurses und die daraus folgende a:ektive Polarisierung symmetrisch über das politische Spektrum hinweg entsteht oder überproportional vom rechten politischen Rand getragen werden. Dies wird unter Bezugnahme auf die Immigrationsdebatte im österreichischen Parlament über acht Legislaturperioden zwischen 1996 und 2022 erforscht werden. Politisierung wird dabei nicht als inhärentes Merkmal bestimmter ideologischer Akteure verstanden, sondern als strukturelle Eigenschaft des Parteienwettbewerbs. Auf Grundlage des ParlaCAP-Korpus wird Politisierung über zwei direkt beobachtbare Dimensionen operationalisiert, die Salienz eines Themas und die Ausweitung der beteiligten Akteure, während a:ektive Polarisierung, gemessen als feindselige oder delegitimierende Sprache gegenüber politischen Gegnern, als nachgelagerte Folge behandelt wird. Die Salienz wird über die über den Anteil eines Themas an der Gesamtdebatte gemessen, die Akteursausweitung über den Wortanteil und die Zahl einzelner Redner und Rednerinnen einer Partei im Verhältnis zu ihrem Mandatsanteil sowie die Animosität auf Sprecherebene über einen LLM, der auf den Originaltexten angewendet und gegen manuelle Kodierung validiert wurde, gemessen. Österreich wird als besonders ungünstiger Fall für die Symmetrieerwartung gewählt, da es mit der FPÖ eine der ältesten Rechtsparteien Westeuropas aufweist. Dennoch stützen die Ergebnisse die Symmetrieannahme über alle vier Hypothesen hinweg. Die Arbeit kommt zu dem Schluss, dass Politisierung und a:ektive Polarisierung im österreichischen parlamentarischen Diskurs strukturell und nicht ideologisch bedingt sind, und liefert ein übertragbares Forschungsdesign für die Untersuchung vergleichbarer Dynamiken in anderen parlamentarischen Demokratien. This thesis examines whether politicisation in parliamentary discourse, and the a:ective polarisation that follows from it, emerges symmetrically across the political spectrum or is driven disproportionately by the political right, as much of the existing literature implicitly assumes. It investigates the immigration debate in the Austrian Parliament across eight legislative periods between 1996 and 2022, treating politicisation as a structural property of party competition rather than an inherent trait of particular ideological actors. Drawing on the ParlaCAP corpus of parliamentary speeches, the analysis operationalises politicisation through two directly observable dimensions, issue salience and actor expansion, and treats a:ective polarisation, measured as hostile or delegitimising language towards political opponents, as a consequent phenomenon. Issue Salience is measured by the number of words labelled on a specific topic actor expansion via party word share and unique-speaker participation relative to seat share, and speaker-level animosity via zero-shot classification with a large language model applied to the authentic German texts, validated against manual coding. Austria is treated as a least-likely case for symmetry, given the long institutionalised presence of one of Western Europe’s oldest far-right parties. The findings nonetheless support symmetry across all four hypotheses. Immigration salience emerged episodically, peaking during the 2015 refugee crisis, driven by the combined operation of sustained FPÖ issue ownership and an exogenous shock rather than unilateral agenda- setting. Actor expansion followed a poles-versus-mainstream structure, with both the FPÖ and the Greens overrepresented while the governing parties remained underrepresented. A:ective polarisation likewise emerged at both poles, with the Greens matching or exceeding the FPÖ’s animosity in several periods. Crucially, regression analysis showed that this a:ective symmetry is driven primarily by government versus opposition status rather than by ideology: opposition status produced a strong increase in animosity across nearly all periods, while the left–right e:ect weakened or lost significance after controlling for it. The study shows that politicisation and a:ective polarisation in Austrian parliamentary discourse are structurally rather than ideologically determined, and it o:ers a transferable research design for examining comparable trends in other parliamentary democracies.

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM coding of animosity in parliamentary speeches was checked against manual coding, but the construct is political discourse, not psychological or clinical.); Sonnet ? (неясен конструкт: LLM zero-shot coded animosity in parliamentary speeches, validated against manual coding. Agreement is likely reported, but the construct is political science (affective polarisation), not clearly psychological.)

**Решение:** -

---

### 513 · R2134

**Can artificial intelligence read between the lines: Utilizing ChatGPT to evaluate medical students' implicit attitudes towards doctor-patient relationship.**

2026 · Medical teacher · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.1080/0142159x.2025.2515971

Abstract Purpose To explore ChatGPT’s utility in evaluating medical students’ implicit attitudes toward the doctor–patient relationship (DPR). Materials and Methods This study analyzed interview transcripts from 10 medical students, categorizing implicit DPR attitudes into Care and Share dimensions, each with 5 levels. We first assessed ChatGPT’s ability to identify DPR-related textual content, then compared grading results from experts, ChatGPT, and participants’ self-evaluations. Finally, experts evaluated ChatGPT’s performance acceptability. Results ChatGPT annotated fewer DPR-related segments than human experts. In grading, pre-course scores from experts and ChatGPT were comparable but lower than self-assessments. Post-course, expert scores were lower than ChatGPT’s and further below self-assessments. ChatGPT achieved an accuracy of 0.84–0.85, precision of 0.81–0.85, recall of 0.84–0.85, and F1 score of 0.82–0.84 for attitude classification, with an average acceptability score of 3.9/5. Conclusions Large language models (LLMs) demonstrated high consistency with human experts in judging implicit attitudes. Future research should optimize LLMs and replicate this framework across diverse contexts with larger samples.

**ИИ:** + · обе модели · кодирование по кодбуку · ChatGPT coded and graded implicit doctor-patient relationship attitudes in interview transcripts and was compared with expert grading (accuracy and F1 reported).

**Решение:** =

---

### 514 · R2158

**PsychoSafe: Eliciting Psychologically-Informed Refusals in Large Language Models**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.09697

Large language models (LLMs) routinely face requests that should be refused, creating a trade-off between helpfulness and harm prevention. However, refusals themselves can be helpful. In high-risk interactions involving crisis, coercion, or escalating intent, blunt non-compliance may prevent direct harm while still failing to support the needs of the person behind the request. We present PsychoSafe, a psychologically-informed refusal framework that reframes refusal as structured supportive communication grounded in evidence-based intervention strategies. To develop PsychoSafe, we construct a corpus of 8019 prompt-response pairs spanning five psychologically salient risk domains and apply prompting and parameter-efficient fine-tuning to Qwen 3.5 27B. On a balanced validation set of 500 prompts, evaluated with an LLM judge and validated through human ratings, PsychoSafe prompting improves overall refusal quality by 28.1% over a generic baseline, with particularly strong gains in external resource referral (+46.8%) and psychological grounding (+34.8%), while preserving downstream performance on non-refusal tasks. Fine-tuning achieves near-perfect refusal and resource-referral rates but reduces response relevance. Additional evaluations on SORRY-Bench and XSTest show strong in-domain robustness but limited out-of-domain generalization, suggesting that future work should diversify fine-tuning data to help models apply interventions selectively rather than schematically.

**ИИ:** + · обе модели · LLM-судья · An LLM judge rates the quality of psychologically-informed refusals in crisis or risk prompts, and those ratings are checked against human ratings.

**Решение:** =

---

### 515 · R2174

**Sentiment Analysis of Naturalistic Speech Using Open-Weight Large Language Models.**

2026 · Affective science · journal article, journalarticle, preprint · eng · https://doi.org/10.1007/s42761-025-00352-7

Psychological research increasingly relies on computational methods to track emotion in naturalistic text. However, standard lexicon-based tools often miss semantic nuance, while powerful commercial Large Language Models (LLMs) raise privacy concerns for sensitive data. This study evaluates the efficacy of 24 open-weight LLMs (1B-120B parameters) for zero-shot sentiment analysis of spoken language, running entirely on local hardware. In this paradigm, models classify text relying solely on natural language instructions rather than labeled training examples. We compared model performance against three increasingly difficult baselines (naïve, standard, and human) across transcripts from two datasets: 193 autobiographical narratives from community participants (N=49) and 292 longitudinal audio journals from psychiatric outpatients (N=64). Results demonstrate that open-weight models significantly outperform standard lexicon-based sentiment tools and frequently surpass individual human raters. Crucially, certain mid-sized models rival the performance of much larger systems, making state-of-the-art analysis accessible via consumer hardware. Additionally, we validate a fully automated privacy-preserving pipeline, finding that transcription errors from automatic speech recognition did not significantly degrade downstream sentiment accuracy. Despite these strengths, a multidimensional fairness audit revealed several demographic disparities: our best-performing models exhibited miscalibration in specific subgroups, lower sensitivity for female speakers in the community dataset, and lower predictive precision for Black speakers in the clinical dataset. Taken together, these findings demonstrate that recent open-weight LLMs can match or surpass human-level performance in sentiment analysis of naturalistic speech while running efficiently and securely on workstation hardware. These advances open opportunities for studying emotional dynamics in daily life and developing privacy-preserving clinical tools.

**ИИ:** + · обе модели · бенчмарк с метками людей · 24 open-weight LLMs rated the emotional sentiment of narratives and psychiatric journal transcripts; their ratings were compared against human raters.

**Решение:** =

---

### 516 · R2175

**Evaluating Open-Weight Large Language Models for Structured Depression Assessment from Clinical Interviews**

2026 · PsyArXiv · dataset/, preprint, ppr · https://doi.org/10.31234/osf.io/63sw4_v3

The administration of semi-structured clinical interviews for depression assessment is resource-intensive and susceptible to rater drift. While large language models (LLMs) offer potential for automated quality assurance, reliance on proprietary models creates data privacy barriers incompatible with secure clinical workflows. This study evaluates a privacy-preserving pipeline using open-weight LLMs to perform item-level scoring of the Montgomery-Åsberg Depression Rating Scale (MADRS) directly from interview transcripts. The sample included 541 video-recorded English-language interviews with 277 psychiatric inpatients diagnosed with diverse affective and psychotic disorders. Benchmarking 25 architectures, we found that an indirect scoring strategy, where models predict individual item scores that are subsequently summed, significantly outperformed direct total score prediction. This suggests that decomposing the assessment into intermediate reasoning steps improves performance. The best-performing models achieved “good” error rates and “excellent” correlations with trusted human labels, approaching established benchmarks for human inter-rater reliability. To determine the active ingredients of effective prompting, we conducted an ablation study. Results revealed that descriptive cues (scoring criteria) were the primary driver of performance, whereas few-shot examples provided negligible additional benefit, suggesting that zero-shot prompting is a viable, efficient strategy. However, error analysis identified a multimodal gap, where text-only models struggled more with items dependent on nonverbal behavior. We conclude that open-weight LLMs demonstrate strong potential to serve as secure “digital second opinions,” representing a promising step toward augmenting clinical decision-making without compromising patient privacy.

**ИИ:** + · обе модели · клиническая оценка · Open-weight LLMs scored MADRS items from clinical interview transcripts; compared against trusted human rater labels.

**Решение:** =

---

### 517 · R2176

**Language Models for Standardising Clinical Notes and Information Extraction in Addiction Psychiatry-An Empirical Study.**

2026 · Drug and alcohol review · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.1111/dar.70059

INTRODUCTION: Electronic health records contain both structured and unstructured data, with unstructured clinical notes widely used in addiction psychiatry. Clinical notes have numerous errors and require proofreading to ensure accuracy and readability. This study evaluates natural language processing methods and adapts a Large Language Model (LLM) for proofreading clinical notes and extracting substance-related information. METHODS: We analysed clinical notes from a 5-year addiction medicine electronic health record dataset (2018-2023), selecting 6500 notes. The proofreading task involved correcting spelling and expanding abbreviations, while information extraction identified the presence of substance use and quantified the time since last use. Annotations by a team of doctors and nurses provided the gold standard. Against this, we compared the performance of existing solutions, including LLMs, and adapted an LLM for these tasks. The final model (fine-tuned LLAMA-3.2-3b) is also compared against a state-of-the-art commercial model (Generative Pretrained Transformer-4-o), and a human-preference experiment is done with masked raters choosing between model-generated and human-generated proofread versions. RESULTS: Proofreading improved readability and decreased out-of-vocabulary words. LLM-based solutions outperformed simpler approaches. The fine-tuned model outperformed the Generative Pretrained Transformer-4-o on both tasks. Masked human evaluators chose model-corrected clinical notes over the human-corrected version in 62% of trials (p < 0.001). On the information extraction task, while the overall performance is satisfactory (Mean F1 0.99), it is poor on rarer substance classes like hallucinogens. DISCUSSION AND CONCLUSIONS: Fine-tuned LLMs effectively standardised clinical notes and extracted structured information from addiction psychiatry records. Both these functionalities have important applications. Standardising improves the readability of clinical documentation and facilitates communication within and between interdisciplinary teams. Automated information extraction can decrease the burden on clinical staff, allow the creation of research cohorts from existing records and improve treatment outcomes by extracting critical information, such as 'time since last drink', which can be used to raise alerts. Even with limited computational resources, it is possible to adapt open-source LLMs for bespoke tasks in the field of addiction psychiatry. Our proposed solution is a model that can be deployed on consumer-grade servers, thus ensuring data privacy and security.

**ИИ:** разошлись — Opus + (клиническая оценка: Fine-tuned Llama and GPT-4o pulled substance-use details from addiction psychiatry notes and were scored against annotations by doctors and nurses.); Sonnet ? (неясен конструкт: Fine-tuned Llama and GPT-4o extract substance use and time since last use from addiction psychiatry notes against human annotations. It is unclear whether this counts as a psychological construct or only information extraction.)

**Решение:** +

---

### 518 · R2178

**Breaking the Ceiling: Mitigating Extreme Response Bias in Surveys Using an Open-Ended Adaptive-Testing System and LLM-Based Response Analysis**

2026 · Preprints.org · preprint, ppr · https://doi.org/10.20944/preprints202601.0952.v1

Assessments of extreme psychological constructs often face a persistent challenge: the ceiling effect, in which a significant proportion of respondents select the highest score on a scale, thus obscuring an important part of the population&#039;s variation. This effect may have profound consequences in studies of extreme psychological constructs. To address this limitation, we introduce a novel framework that integrates Multistage Testing (MST) with open-ended questions that are automatically analyzed by large language models (LLMs). This hybrid approach adapts the survey questions to the respondent while leveraging LLMs to efficiently and reliably interpret free-text answers in large-scale online surveys. Using a case study on aversion toward cockroaches, we show how our method can effectively eliminate extreme ceiling effects, revealing hidden data distributions that are often obscured by extreme responses to conventional Likert-type survey questions. In addition, validation against expert human annotations of survey responses demonstrates the consistency and reliability of the LLMs&#039; performance as evaluators of free-text answers. This framework offers a generalizable methodology that enables more precise and sensitive quantitative measurement of extreme psychological constructs, allowing researchers to study topics that until now were inaccessible due to significant, inherent ceiling effects.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · LLMs rated open-ended survey answers about aversion (a psychological construct) and were checked against expert human annotations.

**Решение:** =

---

### 519 · R2184

**Human-in-the-Loop Suicide Risk Detection and Clinical Escalation in a Generative AI Mental Health Chatbot: Prospective Implementation Study.**

2026 · JMIR formative research · journal article, med, journalarticle · eng · https://doi.org/10.2196/106118

Background Mental illness is the leading cause of disability worldwide, affecting more than one billion individuals, and suicide accounts for 720,000 to 800,000 deaths annually. While AI-native mental health chatbots have the potential to fill a sizable gap between treatment need and workforce capacity, their rapid proliferation has outpaced the development of scalable procedures to identify, detect, and respond to suicidal ideation. Despite AI best practice recommendations to incorporate human oversight for safety monitoring and intervention, studies of procedures for human clinical oversight and crisis response are scarce. Objective To implement a human-in-the-loop suicide risk screening, detection, and clinical escalation protocol in a generative AI mental health chatbot. Methods In an implementation study of a human-in-the-loop suicide risk detection and escalation protocol, adults were recruited online to participate in a single-arm trial of an AI-native mental health chatbot. Participants completed a pre-treatment screening using the Patient Health Questionnaire-9 (PHQ-9). In Phase 1, individuals who endorsed suicidal ideation were escalated to a human clinician for further assessment, safety planning and provision of referral resources, as appropriate. In Phase 2, escalation was triggered by either PHQ-9 responses or detection of spontaneous disclosure of implicit or explicit suicidality in conversational AI interactions. In both phases, the Ask Suicide-Screening Questionnaire (ASQ) guided human-led assessment and risk stratification. Prevalence of suicidal ideation was assessed, along with the rate of successful human outreach, time from suicidality risk detection to human outreach and results of risk stratification evaluation. Results In Phase 1, 624 participants completed suicide screening, of whom 81 (13.0%) endorsed PHQ-9 item 9 (score >1). Outreach was initiated a mean of 11.2 minutes after the alert (SD=13.2; range 1-54 minutes). A clinician successfully reached 25/81 participants (30.9%). In Phase 2, 650 participants completed screening, of whom 133 (20.5%) screened positive at baseline. Across the 30 day post-baseline observation period, 284 risk-alert events were generated among 172 participants (26.5%), including 50 conversational suicidal ideation events. Clinicians successfully contacted 73/172 participants (42.4%). Time from risk detection to clinician outreach initiation was an average of 11.5 minutes (SD 11.7; range 1-58 minutes). Conclusions Proactive, universal suicide risk screening and conversational detection using a human-in-the-loop protocol can be operationally implemented for individuals utilizing a Generative AI mental health chatbot. A subgroup of those who were responsive to human clinical outreach described the approach as acceptable and helpful. Given that contact and clinical assessment were not completed for a sizable proportion of alerted participants, further research is needed to optimize assessment capabilities for those who could not be reached, and characterize the impact of these procedures on clinical outcomes. Nevertheless, the safety procedures reported herein provide a framework from which purpose-built AI-native mental health chatbots can build and refine human-in-the-loop safety responses and protocols. Clinicaltrial

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: The AI chatbot flagged suicidal ideation in conversations and clinicians then assessed with ASQ. Unclear whether AI–clinician agreement is reported.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): Implementation study of human-in-the-loop suicide risk escalation in a chatbot; reports prevalence and outreach metrics, with no LLM–human coding agreement.)

**Решение:** -

---

### 520 · R2203

**Reproducing Human Dream Emotion Coding with ChatGPT, LIWC-22, and Transformer-based Classification: A Validation Study**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.7619830

Accurate classification of emotional content is central to dream research, yet traditional human coding is time-intensive and difficult to scale. This study compared three computational approaches — LIWC-22, Transformer-based classification (TBC), and ChatGPT-based coding – against human ratings of emotional content in 200 dream reports. Three trained human coders independently rated six emotional dimensions (positive and negative emotions, fear, anger, sadness, and curiosity) using a standardized 0-4 coding framework. Human interrater reliability was evaluated prior to computational comparisons, and mean human ratings were used as a reference standard for emotional content expressed or inferable within the dream reports. Convergent and discriminant validity were examined using multi-trait multi-method correlations, while mixed effects regression models assessed the correspondence between computational and human-coded emotion scores. Across all six emotion categories, ChatGPT showed strong correspondence with human ratings when given the same coding manual and scoring criteria, suggesting that instruction-guided language models may help reproduce study-specific human coding frameworks. TBC and LIWC-22 also significantly predicted all six emotional categories, with TBC generally outperforming LIWC-22 for negative emotion, positive emotion, fear and curiosity, whereas LIWC-22 showed stronger correspondence for anger and sadness. Dream length and figurative language showed moderate, yet inconsistent evidence of systematically moderating computational-human agreement. These findings suggest that computational approaches can provide scalable methods for quantifying emotional content in dream reports, with instruction-guided large language model coding showing particularly strong correspondence with a study-specific human coding framework.

**ИИ:** + · обе модели · кодирование по кодбуку · ChatGPT used the same coding manual as three trained human coders to code emotions in 200 dream reports, and its scores were compared with theirs.

**Решение:** =

---

### 521 · R2204

**User Experience and Early Clinical Outcomes of a Mental Wellness Chatbot for Depression and Anxiety: Pilot Evaluation Mixed Methods Study.**

2026 · JMIR formative research · journal article, journalarticle, article · eng · https://doi.org/10.2196/90644

Abstract Background Artificial intelligence–powered conversational agents (ie, chatbots) are increasingly popular outlets for users seeking psychological support, yet little is known about how users experience early-stage prototypes or which therapeutic processes contribute to clinical improvement. A transparent evaluation of emerging chatbot prototypes is needed to clarify if, how, and why artificial intelligence companions work and to guide their continued development. Objective This mixed methods pilot study evaluated user experience, acceptability, and preliminary clinical signals for an early-stage mental wellness chatbot. We also examined whether baseline symptom severity moderated clinical improvement. Methods Three sequential cohorts (n=125) completed a 2-week, incentivized chatbot exposure (approximately 60 min per week). Participants provided first-impression ratings, qualitative feedback, and pre–post assessments of depressive symptoms (PHQ-8 [Patient Health Questionnaire-8]), anxiety symptoms (GAD-7 [Generalized Anxiety Disorder-7]), psychological distress, well-being, and loneliness. Statistical models estimated symptom change and tested interactions with baseline symptom severity. Mixed methods analysis integrated quantitative outcomes with large language model–assisted qualitative content analysis of open-ended responses. Results Participants described the chatbot as accessible, easy to use, and emotionally validating, while citing limitations in personalization and conversational depth. Qualitative responses consistently highlighted early therapeutic processes such as emotional validation, goal setting, and perceived attunement. Regression models showed significant pre–post reductions in depressive (Hedges g=–0.32) and anxiety (g=–0.32) symptoms, alongside modest improvements in distress and well-being. Baseline severity moderated improvement, with marginal effects indicating larger predicted reductions at higher PHQ-8 and GAD-7 baseline scores (eg, PHQ-8=15: g=–0.84; GAD-7=15: g=–0.62). Conclusions This pilot provides a comprehensive view of early chatbot development and suggests promising user experiences and preliminary symptom improvements under structured pilot conditions. By integrating experiential and exploratory clinical data, the study identifies candidate process targets to inform ongoing refinement. Findings support continued development and demonstrate procedural feasibility for progression to larger, longer-term trials evaluating engagement and clinical outcomes under more naturalistic conditions.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · An LLM helped with content analysis of open-ended responses about therapeutic processes; unclear whether its coding was checked against human coders.

**Решение:** =

---

### 522 · R2213

**Theory-Informed vs. Example-Driven Prompting for LLM-Based Qualitative Data Coding in Educational Research**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-981-95-7141-3_21

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM qualitative coding in education, possibly of psychological constructs with human comparison. The construct is unclear.

**Решение:** =

---

### 523 · R2219

**Digital Civic Activism and Configurations of Social-Identity Factors: Protest Campaigns in Gaming Communities on Reddit**

2026 · SocArXiv (OSF Preprints) · preprint · https://doi.org/10.31235/osf.io/s8u3h_v1

This study examines the conditions associated with successful digital protest campaigns in online video-game consumer communities. The theoretical framework combines the Social Identity Model of Collective Action (SIMCA) with research on digital political consumerism. The analysis covers 20 campaigns coordinated on Reddit between 2019 and 2024 and includes five conditions: discursive indicators of collective efficacy (EFFIC), group identification (IDENT), and group-based anger (ANGER), as well as the share of new/low-karma accounts (ANON) and the concentration of activity among the most active participants (LEAD). The empirical corpus contains 312,816 comments; an additional 8,055 comments were manually coded for validation and comparison with automated annotation. Fuzzy-set Qualitative Comparative Analysis (fsQCA) is used to identify configurations associated with outcomes. None of the five conditions is necessary for a concession by the campaign target. The parsimonious solution contains three alternative configurations, but the most robust result is the combination of high group-based anger and low concentration of activity among the most active participants (ANGER × ~LEAD). This path survives most sensitivity checks and indicates that concessions in this sample are associated with mass, emotionally salient, and relatively decentralized mobilization. At the same time, cases of intense mobilization without concessions show that community-level characteristics are insufficient to explain outcomes without considering the cost of concession, the type of demand, and the position of the target organization. Artificial-intelligence tools were used in the research process and in preparing this manuscript. A pretrained CardiffNLP model was used for emotion classification; Gemini was used for automated EFFIC and IDENT annotation; Claude models assisted with the development and checking of replication code; and ChatGPT was used to translate the manuscript. The research question, case selection, operationalization, calibration decisions, result validation, and substantive interpretation were performed by the researcher.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · Gemini annotated collective efficacy and group identification in Reddit comments; 8,055 comments manually coded to validate the automated annotation.

**Решение:** =

---

### 524 · R2221

**AnchorSIPS: A Synthetic Dataset and Evaluation Resource for Evidence-Supported Psychosis-Risk Symptom Measurement**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.12329

Progress on AI for psychosis-risk assessment is limited by a data-access bottleneck. Real clinical interviews are difficult to share because of privacy, governance, and consent constraints. We present AnchorSIPS, a synthetic dataset of 10K structured psychosis-risk interviews with transcript-grounded measurement targets. Each interview is modeled on Mini-SIPS, a clinician-administered psychosis-risk interview. It captures history, 24 symptom questions, follow-up evidence for items the patient affirms, decisions about delusion-like symptoms (unusual beliefs), hallucination-like symptoms (unusual perceptions), and disorganized communication, exclusion of clear psychotic-level symptoms ("frank psychosis"), and a final attenuated psychosis syndrome (APS) diagnosis, a high-risk state of milder or early psychotic symptoms. The APS diagnosis is not a standalone label. It depends on earlier endorsements, supporting follow-up details, symptom-class decisions, and the frank-psychosis check. Every intermediate decision is anchored to its supporting transcript turns. AnchorSIPS is generated by a plan-then-realize pipeline. A hidden case sheet specifies the patient's clinical state, a deterministic planner fixes the interview structure, and an LLM realizes only the patient utterances under validation and bounded repair. Fixing labels and structure before generation avoids the inter-turn inconsistencies typical of multi-turn LLM dialogue. Across seven LLM baselines, models recover coarse decisions but fail to extract follow-up details or cite supporting transcript turns, so final-label performance overstates interview competence. AnchorSIPS is intended for research on evidence extraction, transcript-grounded measurement, and uncertainty under partial disclosure.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: LLMs rate psychosis-risk symptoms in synthetic interviews; labels look predefined, but clinicians may have checked a subset of transcripts.); Sonnet -7 (другое — напишите почему: Synthetic interviews with labels fixed by a generation plan; LLM baselines are scored against those synthetic labels, not against human coders or raters.)

**Решение:** -

---

### 525 · R2223

**LLM-derived narrative metrics in chronic pain: convergent validity and novel cognitive constructs**

2026 · UNC Libraries · text/article, article · https://doi.org/10.17615/tzhx-hx17

The use of subjective reports and questionnaires to evaluate chronic pain, while the gold standard, conveys a limited scope of the patients&rsquo; experience and is burdensome. Here we demonstrate that large language models (LLMs) can evaluate patient-provided texts and automatically generate specific, clinically meaningful, and reliable scores for the sensory, affective, and social dimensions of chronic pain. LLMs can also generate assessor-dependent constructs such as agency and personal narrative.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM scores chronic pain narratives on affective and social dimensions; convergent validity may rest on self-report questionnaires, and human coding is unclear.

**Решение:** =

---

### 526 · R2272

**Scaling bloom’s taxonomy in workplace-based assessment: Comparing BERT and retrieval-augmented LLMs for classifying residents’ EPA reflections**

2026 · other · https://doi.org/10.21955/mep.1115962.1

Background Learner reflections embedded in workplace-based assessment (WBA) systems provide insight into residents’ cognitive engagement. However, Bloom’s Taxonomy–based analysis is rarely implemented at scale due to the burden and subjectivity of manual coding. Advances in natural language processing offer opportunities to operationalize cognitive frameworks within CBME infrastructures. We examined whether different AI approaches can accurately classify residents’ EPA reactions into Bloom’s cognitive levels. Summary of Work We analyzed 500 otolaryngology resident EPA reflections, each manually annotated to Bloom’s six cognitive levels (Remembering–Creating). We compared a supervised BERT classifier (80% training/20% validation), zero-shot large language models, and retrieval-augmented generation (RAG) pipelines using Gemini (300/200 and 400/100 splits, including a stratified variant). Outcomes included classification accuracy and F1-scores across Bloom levels, and feasibility for educational deployment. Summary of Results Across Bloom levels, overall mean accuracy ranked BERT (0.88), Gemini 400/100 RAG (0.86), and Gemini 400/100 stratiVed RAG (0.84), outperforming zero-shot ChatGPT (0.70) and zero-shot Gemini (0.69). Mean F1-scores showed Gemini 400/100 RAG performed best (0.78), followed by BERT (0.71) and Gemini 300/200 RAG (0.69). Remembering and Understanding achieved consistently high accuracy (0.89–0.94), whereas Applying was the weakest class (accuracy 0.74; F1 0.61 among top models). RAG-enhanced models consistently exceeded zero-shot performance, indicating the importance of domain- specific examples. Discussion and Conclusion AI models can meaningfully operationalize Bloom’s Taxonomy for large-scale analysis of reflective narratives in WBA. A key trade-off emerged: BERT provided speed and stability, whereas RAG Gemini models offered superior F1 performance and generated explanations for their outputs. These findings support the development of a “reflective analytics layer” within CBME systems to monitor cognitive engagement and inform targeted educational interventions. Take Home Messages Bloom’s Taxonomy classification of resident reflections is feasible at scale using AI. Retrieval augmentation improves performance and supports explanation in educational analytics.

**ИИ:** ? · обе модели · неясен конструкт · Gemini/ChatGPT classified resident reflections by Bloom's cognitive levels against manual annotation; unclear whether this educational construct counts as psychological.

**Решение:** =

---

### 527 · R2300

**Multi-Agent LLMs for Occupational Profiling: Psychometric Validation on 1636 Chinese Occupations.**

2026 · Behavioral sciences (Basel, Switzerland) · journal article, journalarticle, review · eng · https://doi.org/10.3390/bs16071064

Occupation-level psychological profiles, such as RIASEC interests and Big Five personality, underpin career counseling, person-job matching, and workforce research, but building them at scale has been expensive and limited to a few national taxonomies. The O*NET Interest Profiler, the largest operationalization of RIASEC, took more than two decades of worker surveys, expert ratings, and iterative empirical calibration to construct, and the 2022 Chinese Occupational Classification has no comparable psychological database. Large language models (LLMs) offer a scalable alternative, but using them as raters raises issues that single-model designs do not resolve: inter-rater reliability, calibration to external benchmarks, and systematic psychometric validation. We propose a multi-agent LLM framework in which three LLMs serve as separate expert raters, in-context anchors align the rating scale, and a separate arbitrator resolves rater disagreements. We applied the framework to all 1636 occupations in the 2022 Chinese Occupational Classification, producing six RIASEC and five Big Five scores per occupation. RIASEC dimensions showed uniformly excellent reliability (intraclass correlation coefficient, ICC [2,1] = 0.87 to 0.98) and high convergent correlations with O*NET (r = 0.84 to 0.96); structural validity received weak support (Tracey's C = 0.653, ns), though the dimensions differentiated occupational categories as theory predicts, and the profile space recovered the administrative taxonomy (adjusted Rand index, ARI = 0.418). Big Five absolute agreement was uniformly high, although ICC(2,1) values for Conscientiousness and Neuroticism were attenuated by variance compression and model-level calibration offsets rather than rater disagreement. The Big Five scores are, therefore, suited to broad occupational differentiation, particularly on Openness and Extraversion, rather than to fine-grained rank ordering on Conscientiousness or Neuroticism. The framework also yields the first occupation-level RIASEC and Big Five database for the 2022 Chinese Occupational Classification, openly available for applied use.

**ИИ:** разошлись — Opus -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): LLMs profile occupations on RIASEC/Big Five, validated by correlation with O*NET benchmarks; no human coding of the same psychological texts.); Sonnet ? (неясен конструкт: LLMs rate occupations on RIASEC/Big Five and are compared with O*NET human-derived ratings; unclear whether occupation descriptions count as psychological text with human coder agreement.)

**Решение:** -

---

### 528 · R2306

**Multi-Label Emotion Recognition in Low-Resource Dialects: A Case Study on Algerian Arabic with Large Language Models**

2026 · Procedia Computer Science · conference-paper · en · https://doi.org/10.1016/j.procs.2026.01.094

Emotion Recognition (ER) is a significant challenge in Natural Language Processing (NLP), as it aims to categorize text based on basic human emotions like joy, sadness, and anger. Due to the limited available linguistic resources and the distinctive linguistic features of Arabic dialects, this task becomes more difficult, particularly for the Algerian dialect. This study offers an in-depth assessment of both general-purpose and Arabic-specific Large Language Models (LLMs) for the task of multi-label emotion detection in the Algerian dialect. Despite the limited number of pre-trained LLMs specifically tailored for the Algerian dialect, we evaluate the performance of six well-known LLMs: three Arabic-specific open-source models (DziriBERT, AraBERT-Algerian, MARBERTv2) and three general-purpose models (ChatGPT, Gemini, DeepSeek). The Algerian Arabic subset of the SemEval-2025 Task 11 dataset, which is based on literary texts and has been manually annotated by native speakers, is used for the experiments. Evaluation against established metrics demonstrates promising results. The Gemini model in a zero-shot setting achieved a competitive macro F1-score of 66.53%, which is very close to the performance of the top-ranked system in SemEval-2025 Task 11. With a macro F1-score of 60.21%, the refined AraBERT-Algerian model outperformed SemEval-2025 baselines by a significant margin. These results show that zero-shot inference and fine-tuning techniques can both be successful in low-resource environments, highlighting the potential of both general-purpose and dialect-specific LLMs for multi-label emotion detection in the Algerian dialect.

**ИИ:** + · обе модели · бенчмарк с метками людей · ChatGPT, Gemini and DeepSeek, used zero-shot, labelled emotions in Algerian Arabic texts and were scored against labels from native-speaker annotators.

**Решение:** =

---

### 529 · R2316

**What makes for an enjoyable protagonist? An analysis of character warmth and competence**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.06658

Drawing on psychological and literary theory, we investigated whether the warmth and competence of movie protagonists predict IMDb ratings, and whether these effects vary across genres. Using 2,858 films and series from the Movie Scripts Corpus, we identified protagonists via AI-assisted annotation and quantified their warmth and competence with the LLM_annotate package ([1]; human-LLM agreement: r = .83). Preregistered Bayesian regression analyses revealed theory-consistent but small associations between both warmth and competence and audience ratings, while genre-specific interactions did not meaningfully improve predictions. Male protagonists were slightly less warm than female protagonists, and movies with male leads received higher ratings on average (an association that was multiple times stronger than the relationships between movie ratings and warmth/competence). These findings suggest that, although audiences tend to favor warm, competent characters, the effects on movie evaluations are modest, indicating that character personality is only one of many factors shaping movie ratings. AI-assisted annotation with LLM_annotate and gpt-4.1-mini proved effective for large-scale analyses but occasionally fell short of manually generated annotations.

**ИИ:** разошлись — Opus + (проверка кодирования внутри исследования: GPT-4.1-mini rated protagonists' warmth and competence in movie scripts; the study reports human-LLM agreement (r = .83).); Sonnet ? (неясен конструкт: LLM rated warmth/competence of movie protagonists from scripts with reported human-LLM agreement (r=.83); the psychological construct fits, but fictional script text is borderline.)

**Решение:** +

---

### 530 · R2323

**XEmoGPT: An Explainable Multimodal Emotion Recognition Framework with Cue-Level Perception and Reasoning**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2602.05496

Explainable Multimodal Emotion Recognition plays a crucial role in applications such as human-computer interaction and social media analytics. However, current approaches struggle with cue-level perception and reasoning due to two main challenges: 1) general-purpose modality encoders are pretrained to capture global structures and general semantics rather than fine-grained emotional cues, resulting in limited sensitivity to emotional signals; and 2) available datasets usually involve a trade-off between annotation quality and scale, which leads to insufficient supervision for emotional cues and ultimately limits cue-level reasoning. Moreover, existing evaluation metrics are inadequate for assessing cue-level reasoning performance. To address these challenges, we propose eXplainable Emotion GPT (XEmoGPT), a novel EMER framework capable of both perceiving and reasoning over emotional cues. It incorporates two specialized modules: the Video Emotional Cue Bridge (VECB) and the Audio Emotional Cue Bridge (AECB), which enhance the video and audio encoders through carefully designed tasks for fine-grained emotional cue perception. To further support cue-level reasoning, we construct a large-scale dataset, EmoCue, designed to teach XEmoGPT how to reason over multimodal emotional cues. In addition, we introduce EmoCue-360, an automated metric that extracts and matches emotional cues using semantic similarity, and release EmoCue-Eval, a benchmark of 400 expert-annotated samples covering diverse emotional scenarios. Experimental results show that XEmoGPT achieves strong performance in both emotional cue perception and reasoning.

**ИИ:** разошлись — Opus ? (другое: Multimodal LLM recognizing emotion in video/audio, evaluated on an expert-annotated benchmark; unclear whether the input counts as text or transcripts.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Multimodal (video/audio) emotion recognition model and dataset; it is a model-building paper, not LLM coding of psychological text against human coders.)

**Решение:** -

---

### 531 · R2343

**Detection != Reliable Control: Decodable Empathy Directions Yield at Most Partial Shifts in Automated Empathy Scores**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.24901

A decodable "empathy" direction is routinely read as a causal lever, conflating decodability, automated-metric control, and human-perceived change. We test this for two EPITOME-derived facets -- Recognition (cognitive) and Resonance (affective) -- in three instruction-tuned LLMs, scoring every intervention with two LLM judges and a discriminative EPITOME classifier, each gated by an emotional-vs-neutral positive control. The control passes for the affective facet across all automated instruments, but cognitive range is inconsistent across them. Both facets remain decodable after residualizing against a sentence-embedding-derived surface score, and steering can substantially rewrite the text. Yet adding the Resonance direction raises the affective score only partially -- in Qwen by +0.29 (approximately 26% of the natural gap). A direct between-direction contrast confirms the shift is facet-specific in Qwen and Llama (not Gemma); we do not, however, establish a matching human-perceived change. Additive cognitive steering produces no measurable change, but a within-domain control shows the cognitive instrument is too coarse to resolve the differences such steering would produce -- unmeasurable, not a clean null. By contrast, Gemma Recognition ablation lowers the classifier's cognitive score even after adjusting for response length. Detection does not imply reliable control under global interventions, and cognitive-empathy claims warrant an explicit measurement-sensitivity check. Under review at BlackboxNLP 2026 (EMNLP). 8 pages body, 10 figures/tables, plus appendix

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Steering study where LLM judges score EPITOME empathy facets; unclear whether judges were validated against EPITOME human labels.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Mechanistic interpretability study of steering empathy directions in LLMs; LLM judges score outputs but no human coding comparison is reported (explicitly no human-perceived change).)

**Решение:** -

---

### 532 · R2359

**Sympathetic Framing: Evaluating AI Alignment across Sociodemographic Groups**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2607.27232

Large Language Models (LLMs) are increasingly shaping how we consume information and form our worldview. This raises concerns beyond bias in AI: do LLMs grasp the emotional nuances conveyed via textual framing? In this work, we empirically evaluate how well an array of LLMs aligns with human emotional perception. Considering news headlines covering political and geopolitical conflicts, both human participants (n = 3011, a representative sample of the U.K. adult population, via a YouGov survey) and seven LLMs answered whether headlines evoked sympathy for a specified side in a conflict. We find that the correlation between AI and human evaluations varies across models, ranging from very high (0.789, GPT-5.2) to medium (0.4 ,Mistral Large 2512). Crucially, the leading models are broadly aligned with human judgments across all demographic subgroups, including age, gender, level of education, prior geopolitical knowledge, and participants' predispositions regarding the conflict, although there are statistically significant differences between groups. This research, with its robust design and large, demographically diverse dataset, offers the most comprehensive evaluation of LLMs' comprehension of news framing to date. Findings highlight an important, often-ignored aspect of differential alignment: even when aggregate performance is high, AI alignment is not universal -- it may correspond differently with demographic features and cultural norms. Considering or ignoring the need for differential alignment may therefore have significant implications for the development of ethical and useful AI systems.

**ИИ:** ? · обе модели · неясен конструкт · LLMs and 3011 humans rated the same news headlines for evoked sympathy; emotional construct, but political framing of headlines is borderline.

**Решение:** =

---

### 533 · R2366

**Automating collateral histories in dementia: Development and proof‑of‑concept evaluation of the LUMEN conversational AI.**

2026 · International psychogeriatrics · journal article, med, journalarticle/journal contribution · eng · https://doi.org/10.1016/j.inpsyc.2026.100221

© 2026 The Author(s). Published by Elsevier Inc. on behalf of International Psychogeriatric Association. This is an open access article under the CC BY license. http://creativecommons.org/licenses/by/4.0/Background: Collateral histories from carers are central to dementia diagnosis but are often collected inconsistently and variably documented. With rising demand on memory services and the emergence of disease-modifying therapies requiring timely diagnosis, there is increasing need for structured and efficient assessment approaches. Conversational AI powered by large language models (LLMs) may support standardised collateral history acquisition while maintaining clinician oversight. We developed LUMEN, a stakeholder-informed prototype designed to generate structured collateral summaries for clinical review. Methods: A five-stage patient, public and professional involvement programme (approximately 232 participants) co-designed the question set, interface and outputs. Seven open-source LLMs were benchmarked; Qwen3-30B-A3B was selected to generate structured summaries from interview transcripts. Six clinician-authored vignettes representing Alzheimer’s disease, dementia with Lewy bodies, vascular dementia, frontotemporal dementia, mild cognitive impairment and normal cognition were used to generate 54 synthetic dialogues (27 clinician role-played, 27 GPT-4 generated). Diagnostic categories were assigned using a deterministic rule-based rubric applied to structured summaries. Two clinicians independently rated each dialogue. Outcomes included exploratory evaluation of alignment with diagnostic categories measured by area under the receiver operating characteristic curve (AUROC) and Cohen’s κ, and System Usability Scale (SUS) scores. Results: In this small synthetic vignette-based dataset, macro-average AUROC was 0.95; these values reflect performance under closed-loop proof-of-concept conditions rather than real-world diagnostic accuracy. Discrimination was highest for Alzheimer’s disease and vascular dementia (AUROC = 1.00 in this synthetic dataset) and lowest for mild cognitive impairment (AUROC = 0.77). Agreement between categories assigned by the rule-based rubric and averaged clinician ratings was κ = 0.88 (95% CI 0.83–0.93). Mean SUS score was 78.1/100. Conclusions: In a small, closed-loop synthetic proof-of-concept dataset, this LLM-assisted, rubric-based pipeline showed that structured summaries could be processed reproducibly by the rubric and separated diagnostic categories under controlled conditions. These findings do not show real-world diagnostic performance. Further evaluation is required to determine clinical usefulness, robustness and workflow impact.

**ИИ:** ? · обе модели · другое · LLM summarises dementia interview transcripts, then a rule-based rubric assigns categories (κ=0.88 vs clinicians); the LLM's own role in rating is indirect.

**Решение:** =

---

### 534 · R2374

**Characterizing Documented Psychosocial Stressors in Pediatric Psychiatric Emergencies with an Open-Weight Large Language Model.**

2026 · medRxiv : the preprint server for health sciences · journal article, preprint, journalarticle · eng · https://doi.org/10.64898/2026.06.08.26354931

Objective: To evaluate whether a locally hosted open-weight large language model (LLM) can extract documented psychosocial factors from pediatric psychiatric intake notes and apply validated extraction to a large emergency psychiatry cohort. Materials and Methods: We identified emergency department presentations at Cincinnati Children's Hospital Medical Center from January 1, 2016, through December 31, 2024, among patients <18 years with psychiatric billing diagnoses. Using full-text intake notes, gpt-oss:120b classified peer conflict, sleep disruption, and school-related academic, attendance, and disciplinary issues as detected, negated, or indeterminate. Four human raters independently reviewed 50 notes. We compared Fleiss' κ among humans alone versus humans plus the LLM, assessed repeated-query stability across 50 independent calls per note, and applied the workflow to all eligible notes. Results: Among 37,315 eligible admissions, 22,284 had eligible intake notes; 22,270 produced parseable JSON. In detected-vs-not-detected coding, human-plus-LLM reliability did not differ significantly from human-only reliability across measures (human κ, 0.71-0.94; human-plus-LLM κ, 0.70-0.93). Stability was associated with human agreement: mean LLM-human agreement increased from 42.6% for classifications with <80% stability to 82.7% for 100% stability (Pearson r=0.36). Full-cohort extraction showed frequent and overlapping documented factors: sleep disruption was most frequently detected (57.7%), followed by peer conflict (47.2%), academic issues (43.4%), disciplinary issues (43.3%), and attendance issues (16.9%). Discussion: Agreement varied by construct and was strongest when repeated model outputs were stable. Conclusion: Locally hosted open-weight LLMs can support scalable structured extraction of documented psychosocial factors from pediatric psychiatric intake notes after local validation.

**ИИ:** + · обе модели · клиническая оценка · An open-weight LLM coded psychosocial stressors in psychiatric intake notes, compared against four human raters using Fleiss' kappa.

**Решение:** =

---

### 535 · R2378

**How Do Large Language Models Judge Social Attraction? Evidence from Theory-Grounded Persona Ratings Across Multiple LLMs and Humans**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.09717

Large language models (LLMs) are increasingly used to perform subjective evaluations traditionally made by humans, yet their validity as social judges remains unclear. This paper examines whether LLMs can assess social attraction from theory-grounded persona profiles constructed from ten psychological and relational constructs and organized into three tiers: socially attractive, socially mixed, and socially unattractive. We examine LLM ratings in two studies and compare them with human judgments in a third study. In Study 1, 34 LLMs rated 12 profiles across three repeated runs. Although some models tended to give higher or lower ratings overall, they showed strong stability across runs, consistent three-tier ordering, and high agreement in relative profile ordering. Study 2 examined sensitivity to gender presentation using six matched name-and-pronoun profile pairs and a separate pronoun-only test with a gender-neutral name, finding no significant effects in either analysis. In Study 3, 198 human participants evaluated the six matched profiles from Study 2. Their ratings reproduced the three-tier structure and followed a profile ordering consistent with that of the LLMs. However, LLMs rated attractive profiles more positively and unattractive profiles more negatively than humans, while neither group showed a significant overall effect of gender presentation. 9 pages, 2 figures, 2 tables. Includes technical supplement

**ИИ:** ? · обе модели · неясен конструкт · LLMs and 198 humans rated the same constructed persona profiles for social attraction; unclear if vignette judgments count as coding psychological text.

**Решение:** =

---

### 536 · R2381

**Leveraging Local-LLM for sentiment analysis to enhance text data quality assessment in information science research**

2026 · The Electronic Library · journalarticle, review, article · en · https://doi.org/10.1108/el-08-2025-0354

Purpose This study explores how a privacy-preserving local large language model (Local-LLM) assists researchers in evaluating unstructured text data quality, early in the analysis process. It aims to accurately and effectively determine if a Local-LLM can evaluate the quality of open-ended survey responses compared to human coders during the initial analysis of unstructured survey data. Design/methodology/approach A Python tool using Llama 3.2 and 3.3 classified 604 survey responses. Human-coded sentiment labels served as a baseline; model performance was assessed with confusion matrices, F1, Cohen’s κ and Gwet’s AC1. All processing was offline to protect data privacy. Findings Llama 3.3 achieved top performance (F1 ≈ 0.97, AC1 ≈ 0.97), while Llama 3.2 also excelled on consumer hardware. Automated sentiment analysis reduced processing time from 4 h to 8 min and identified short responses that manual reviewers might miss, improving speed and data quality. Research limitations/implications The approach’s reliability beyond English or on longer narratives remains to be examined in future work. Practical implications The Local-LLMs allow researchers to rapidly filter and assess large volumes of unstructured text data before conducting deeper analysis. Originality/value This study demonstrates that Local-LLM’s semantic features can be used for sentiment analysis as a scalable, cost-effective and rapid method for evaluating unstructured text data, aligning with the research questions before analysis. It also illustrates how to use zero-shot prompting to interact with Ollama via Local-LLMs, simplifying AI integration for non-technical researchers.

**ИИ:** разошлись — Opus ? (неясен конструкт: Llama sentiment labels on open-ended survey responses compared with human coders (κ, AC1); unclear if sentiment reflects psychological construct or generic opinion.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Llama sentiment labels on survey responses versus human coders, but it is generic sentiment for data-quality screening in information science, not a psychological construct.)

**Решение:** -

---

### 537 · R2392

**Evaluating synthetic with real: a systematic comparison of seven LLMs for Turkish emotion classification**

2026 · The Journal of Supercomputing · journalarticle, article · en · https://doi.org/10.1007/s11227-026-08903-w

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; seven LLMs on Turkish emotion classification may be evaluated against human-labelled real data, or may only generate synthetic data.

**Решение:** =

---

### 538 · R2397

**GoTCHA: Hierarchical Graph-of-Thoughts for Explainable Cognitive Distortion Classification**

2026 · ACM Symposium on Applied Computing · journalarticle, book · https://doi.org/10.1145/3748522.3779920

Large Language Models (LLMs) approaches show limitations in analyzing overlapping distortion patterns and hierarchical belief structures for Cognitive Behavioral Therapy(CBT). We propose GoTCHA: Hierarchical Graph-of-Thoughts for Explainable Cognitive Distortion Classification. GoTCHA separates patient utterances into objective facts and subjective thoughts through gap analysis based on psychological theory, then performs multi-label classification via a three-stage hierarchical reasoning of core belief, fine-grained belief, and cognitive distortion detection. At each stage, we generate multiple candidate thoughts. These are evaluated based on psychological validity, structural consistency, and input relevance to select optimal thoughts. We implement conditional backreasoning and automatic refinement mechanisms that regenerate thoughts when scores fall below an optimized threshold. Extensive experiments on CBT-BENCH demonstrate that GoTCHA achieves significant improvements over previous state-of-the-art methods. Our framework maintains high accuracy on complex multi-distortion cases while providing interpretable clinical outputs. The hierarchical reasoning structure successfully addresses single-extraction dependencies and enables robust analysis of interconnected cognitive patterns for practical clinical applications.

**ИИ:** + · обе модели · бенчмарк с метками людей · An LLM framework classifies cognitive distortions and core beliefs in patient utterances, evaluated against CBT-BENCH labels that experts annotated.

**Решение:** =

---

### 539 · R2403

**Reduced linguistic coherence in psychosis defies semantic similarity accounts and relates to altered large-scale cortical hierarchy.**

2026 · Scientific reports · journal article, journalarticle, journalarticle/none · eng · https://doi.org/10.1038/s41598-026-39025-1

Coherence in speech is clinically significant in mental disorders but remains difficult to quantify. We tested the widely-held assumption that semantic similarity metrics derived from large language models capture human-rated coherence. Across three large neurotypical datasets in different languages, semantic similarity failed to correlate with human ratings, while six other metrics, especially the probability-based metrics, showed significant but weak correlations. In an additional English dataset of 94 individuals, including healthy controls and patients with schizophrenia spectrum disorders (SSD), speech coherence was reduced in SSD. Incoherence in the drug-naïve first-episode samples related to altered whole-brain intrinsic functional gradients, and to the probabilistic metric of perplexity in speech. Together, these findings call into question semantic similarity as a proxy for coherence, motivate greater emphasis on probabilistic predictability measures for evaluating coherence, and substantiate the perspective of spontaneous speech as an overt readout of an alteration of hierarchical cortical organization in schizophrenia.

**ИИ:** ? · обе модели · другое · LLM-derived similarity and perplexity metrics are correlated with human coherence ratings of speech; unclear whether a generative LLM directly rates coherence.

**Решение:** =

---

### 540 · R2406

**EmoTrans: A Benchmark for Understanding, Reasoning, and Predicting Emotion Transitions in Multimodal LLMs**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.23348

Recent multimodal large language models (MLLMs) have shown strong capabilities in perception, reasoning, and generation, and are increasingly used in applications such as social robots and human-computer interaction, where understanding human emotions is essential. However, existing benchmarks mainly formulate emotion understanding as a static recognition problem, leaving it largely unclear whether current MLLMs can understand emotion as a dynamic process that evolves, shifts between states, and unfolds across diverse social contexts. To bridge this gap, we present EmoTrans, a benchmark for evaluating emotion dynamics understanding in multimodal videos. EmoTrans contains 1,000 carefully collected and manually annotated video clips, covering 12 real-world scenarios, and further provides over 3,000 task-specific question-answer (QA) pairs for fine-grained evaluation. The benchmark introduces four tasks, namely Emotion Change Detection (ECD), Emotion State Identification (ESI), Emotion Transition Reasoning (ETR), and Next Emotion Prediction (NEP), forming a progressive evaluation framework from coarse-grained detection to deeper reasoning and prediction. We conduct a comprehensive evaluation of 18 state-of-the-art MLLMs on EmoTrans and obtain two main findings. First, although current MLLMs show relatively stronger performance on coarse-grained emotion change detection, they still struggle with fine-grained emotion dynamics modeling. Second, socially complex settings, especially multi-person scenarios, remain substantially challenging, while reasoning-oriented variants do not consistently yield clear improvements. To facilitate future research, we publicly release the benchmark, evaluation protocol, and code at https://github.com/Emo-gml/EmoTrans.

**ИИ:** разошлись — Opus ? (другое: Multimodal LLMs scored against human emotion annotations of video clips; unclear whether text or transcripts are what gets coded.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Multimodal video emotion transition benchmark for MLLMs; not text coding of psychological text, and no LLM–human coder agreement on text.)

**Решение:** -

---

### 541 · R2422

**GPT as a Measurement Tool**

2026 · National Bureau of Economic Research · casereport, journalarticle, report · https://doi.org/10.3386/w34834

We present the GABRIEL software package, which uses GPT to quantify attributes in qualitative data (e.g. how “pro innovation” a speech is). GPT is evaluated on classification and attribute rating performance against 1000+ human annotated tasks across a range of topics and data. We find that GPT as a measurement tool is accurate across domains and generally indistinguishable from human evaluators. Our evidence indicates that labeling results do not depend on the exact prompting strategy used, and that GPT is not relying on training data contamination or inferring attributes from other attributes. We showcase the possibilities of GABRIEL by quantifying novel and granular trends in Congressional remarks, social media toxicity, and county-level school curricula. We then apply GABRIEL to study the history of tech adoption, using it to assemble a novel dataset of 37,000 technologies. Our analysis documents a tenfold decline of time lags from invention to adoption over the industrial age, from ~50 years to ~5 years today. We quantify the increasing dominance of companies and the U.S. in innovation, alongside characteristics that explain whether a technology will be adopted slowly or speedily. Institutional subscribers to the NBER working paper series, and residents of developing countries may download this paper without additional charge at www.nber.org.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT rating validated against 1000+ human-annotated tasks across many domains; some could be psychological constructs, but the examples given are political and economic.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: General-purpose GPT measurement tool for economics/political/social text (speeches, toxicity, curricula, technologies); no psychological or clinical construct focus.)

**Решение:** -

---

### 542 · R2440

**Note-Level Phenotyping of Multiple Sclerosis Notes by a Large Language Model Achieves Near Human-Level Agreement**

2026 · Preprints.org · preprint, ppr, posted-content · https://doi.org/10.20944/preprints202604.1173.v1

Background: /Objectives: Clinical phenotyping from narrative electronic health records (EHRs) often relies on multi-stage pipelines with span-level extraction, ontology mapping, and aggregation, which are complex to develop and maintain. Large language models (LLMs) may enable direct note-level abstraction of clinically meaningful features without intermediate extraction steps. We evaluated whether an LLM can approximate human inter-rater agreement for note-level multiple sclerosis (MS) phenotyping. Methods: We analyzed 100 de-identified MS neurology progress notes from a single academic medical center, each annotated for the presence or absence of 17 predefined neurological phenotype features (e.g., weakness, sensory, gait, pain, cognition, bladder). Two human annotators independently labeled all notes using a multi-label note-level framework in Prodigy, and discrepancies between the human annotators were adjudicated to create a gold standard. The same notes were annotated in a zero-shot setting by a large language model (GPT-5) and by the dictionary-based Doc2Hpo system. We computed percent agreement, Cohen’s κ, and precision, recall, and F1 scores for each annotator relative to the gold standard Results: Human–human agreement was substantial across most phenotype domains, with Cohen’s κ typically between 0.61 and 0.84, and lower agreement for infrequent features such as spasticity and hyperreflexia. Agreement between the LLM and human annotators was comparable to human inter-rater agreement across many features. Relative to the gold standard, the LLM showed recall that was equal to or higher than human annotators for most phenotypes, with overall F1 scores similar to human performance, whereas Doc2Hpo demonstrated lower precision and recall. Conclusions: In this note-level MS phenotyping task, a large language model achieved performance approaching expert human inter-rater agreement, with particularly strong recall across multiple phenotype domains. These findings suggest that direct note-level abstraction of clinically meaningful phenotypes from narrative neurology notes is feasible and may offer a scalable complement to traditional span-oriented extract–map–aggregate pipelines for population-level phenotyping and downstream machine learning applications.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-5 vs human annotation of MS neurology notes; mostly neurological features, but cognition (possibly mood) features may give extractable psychological agreement.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM phenotyping of multiple sclerosis neurology notes (neurological features) against human annotators; a medical, non-psychological construct.)

**Решение:** -

---

### 543 · R2441

**Large language models for thematic analysis in healthcare research: A blinded mixed-methods comparison with human analysts.**

2026 · PLOS digital health · journal article, journalarticle, article · eng · https://doi.org/10.1371/journal.pdig.0001189

Abstract Large language models (LLMs) are increasingly used for qualitative thematic analysis, yet evidence on their performance in analysing focus-group data, where polyvocality and context complicate coding, remains limited. Given the increasing role of such models in thematic analysis, there is a need for methodological frameworks that enable systematic, metric-based comparisons between human and model-based analyses. We conducted a blinded mixed-methods comparison of two general-purpose LLMs (ChatGPT-5 and Claude 4 Sonnet), an LLM-based qualitative coding application (QualiGPT), and blinded human analysts on an in-person focus-group transcript informing an AI-enabled digital health proposal. We evaluated deductive coding using a 10-code, 6-theme codebook against an expert consensus adjudication; inductive coding with a structured Likert-scale comparison to a reference-standard set of inductive themes generated by expert consensus; and manual quote verification of LLM segments to define LLM hallucination (evidence absent or non-supportive) and error rate (including partial matches and speaker-coded segments). During deductive coding against an expert consensus adjudication, large language models (LLMs) yielded a mean agreement of 93.5% (95% CI 92.5–94.5) with κ = 0.34 (95% CI 0.26–0.40); blinded human coders achieved 92.7% (95% CI 91.6–93.9) agreement with κ = 0.34 (95% CI 0.26–0.41). Mean Gwet’s AC1 was 0.92 (95% CI 0.90–0.93) for the blinded human analysis, and 0.93 (95% CI 0.92–0.94) for the LLM-assisted deductive analysis, reflecting high agreement despite the low overall code prevalence (7.8%, SD = 3.2%). Only one model achieved non-inferiority in inductive analysis of the transcript ( p = 0.043). The strict hallucination rate in inductive analysis was 1.2% (SD = 2.1%). LLMs were non-inferior to human analysts for deductive coding of the focus-group data, with variable performance in inductive analysis. Low hallucination but significant comprehensive error rates indicate that LLMs can augment qualitative analysis but require human verification. Author summary Qualitative research plays an important role in digital health, assisting in the implementation of healthcare technologies and innovations. However, analysing qualitative data in the form of focus groups is time-consuming and requires human expertise. Large Language Models (LLMs) are being increasingly used in qualitative research analysis, although evidence on their performance in analysing focus group data is limited. We compared the performance of LLMs to blinded human analysts in analysing a focus group transcript on AI implementations in healthcare. We used both qualitative and quantitative metrics to evaluate the performance of LLMs in thematic analysis. We found that the LLMs performed similarly to humans when applying pre-defined codes (deductive analysis), with a low rate of hallucination. However, in open-ended theme generation (inductive analysis) their performance was more variable, particularly in areas requiring interpretation of tone, nuance, or conversational context. These findings suggest that LLMs can be used to support interpretation of qualitative data, rather than replace human analysts. We provide a reproducible framework in analysing the performance of LLMs in qualitative analysis.

**ИИ:** ? · обе модели · неясен конструкт · LLMs applied a deductive codebook to focus-group units compared with expert consensus, but codes on AI health tech may be attitudes rather than psychological constructs.

**Решение:** =

---

### 544 · R2443

**The Supportiveness–Safety Tradeoff in LLM Well-Being Agents**

2026 · ACM/IEEE International Conference on Human-Robot Interaction (HRI) · book, journalarticle, preprint/article · https://doi.org/10.1145/3776734.3794563

Large language models (LLMs) are being integrated into socially assistive robots (SARs) and other conversational agents providing mental health and well-being support. These agents are often designed to sound empathic and supportive in order to maximize user's engagement, yet it remains unclear how increasing the level of supportive framing in system prompts influences safety relevant behavior. We evaluated 6 LLMs across 3 system prompts with varying levels of supportiveness on 80 synthetic queries spanning 4 well-being domains (1440 responses). An LLM judge framework, validated against human ratings, assessed safety and care quality. Moderately supportive prompts improved empathy and constructive support while maintaining safety. In contrast, strongly validating prompts significantly degraded safety and, in some cases, care across all domains, with substantial variation across models. We discuss implications for prompt design, model selection, and domain specific safeguards in SARs deployment.

**ИИ:** + · обе модели · LLM-судья · An LLM judge rated the safety and care quality of well-being agent responses and was checked against human ratings.

**Решение:** =

---

### 545 · R2448

**Agreement Between Reasoning-Oriented Generative AI Models and Clinical Educators in Evaluating Japanese Objective Structured Clinical Examination Transcripts: Preliminary Comparative Study.**

2026 · JMIR formative research · comparative study, research support, non-u.s. gov't, research-article · eng · https://doi.org/10.2196/92016

Abstract Background Medical interview training faces limitations in both implementation and evaluation. While generative artificial intelligence (GenAI) offers a potential solution, it remains unclear whether reasoning-oriented models improve evaluation, particularly for the Japanese language. Objective We assessed scoring patterns to evaluate the agreement between reasoning-oriented GenAI model scores and clinical educator consensus ratings in Japanese medical interview training. Methods This study was conducted at a medical university in Japan using original Japanese-language text data derived from medical interview training. Postgraduate year 1 and 2 residents were involved. Two blinded human clinical educators independently evaluated the transcripts and reached consensus through discussion. These consensus ratings were used as a practical reference standard, while preconsensus agreement was also assessed to characterize interhuman variability. Two GenAI models, GPT-5.2 Thinking (OpenAI) and Gemini 3.0 Pro (Google LLC), independently evaluated the same transcripts directly. Each GenAI model generated a single zero-shot evaluation per transcript using default settings. All evaluations used a standardized 6-domain Objective Structured Clinical Examination rubric (patient care, history taking, physical examination, accuracy and organization of clinical information, clinical reasoning, and management) scored on a 1‐6 Likert scale, where 1 indicates inferior, and 6 indicates excellent. We compared mean evaluation scores using the Wilcoxon signed-rank test and assessed interrater reliability using intraclass correlation coefficients between the GenAI models and the clinical educators. Results Clinical educators and both GenAI models rated the entire dataset of 40 transcripts by 20 included residents. Clinical educator consensus ratings yielded the highest overall mean scores (5.18, 95% CI 5.06 to 5.30). Comparatively, both GenAI models demonstrated significantly lower scores: GPT-5.2 Thinking assigned the lowest overall score (3.68, 95% CI 3.62 to 3.72; P<.001), followed by Gemini 3.0 Pro (4.09, 95% CI 3.97 to 4.21; P<.001). This discrepancy was most pronounced in the management domain, where GPT-5.2 Thinking assigned 2.93 (95% CI 2.79 to 3.06) compared with the clinical educator consensus mean score of 5.20 (95% CI 4.91 to 5.49). Agreement between the GenAI models and the clinical educator consensus ratings was poor across all domains, with overall intraclass correlation coefficients of 0.04 (95% CI 0.00 to 0.09) for GPT-5.2 Thinking and 0.22 (95% CI 0.10 to 0.35) for Gemini 3.0 Pro. Conclusions In this preliminary, single-center, transcript-based Japanese-language study, single-run zero-shot evaluations by GPT-5.2 Thinking and Gemini 3.0 Pro showed lower scores and poor agreement with the clinical educator consensus ratings. These findings should be interpreted cautiously because multiple outputs, prompt-sensitivity analyses, local validation, and model-parameter comparisons were not performed. Under the specific conditions tested, these models should not be used as standalone evaluators for Japanese Objective Structured Clinical Examination medical interview transcripts. Whether these models can provide useful formative feedback remains a hypothesis.

**ИИ:** ? · обе модели · неясен конструкт · GPT-5.2 and Gemini rated OSCE interview transcripts vs. clinical educators (ICC). The rubric is mostly medical competence; the patient-care/communication domain may be interpersonal.

**Решение:** =

---

### 546 · R2460

**Evaluating Large Language Models for Extracting Social Determinants of Health in Substance Use Disorder Notes.**

2026 · Studies in health technology and informatics · journal article, med, journalarticle · eng · https://doi.org/10.3233/shti260337

Automated extraction of social determinants of health (SDoH) may support earlier identification of unmet social needs and inform substance use disorder (SUD) care. This study provides preliminary evidence that few-shot prompting improves large language model performance in extracting SDoH from discharge summaries of patients with SUD. While the accuracy of few-shot prompting exceeded zero-shot prompting, limitations such as low inter-annotator agreement and hallucinations remain. Future work should explore domain-adapted models, active learning, and validation in diverse populations.

**ИИ:** ? · обе модели · неясен конструкт · LLM extracts SDoH from SUD discharge summaries against human annotations; unclear whether SDoH counts as a psychological construct.

**Решение:** =

---

### 547 · R2462

**AI Mirror: A Preliminary Exploration of Using Large Language Models to Mitigate Subjectivity in Autoethnographic Self-Study**

2026 · International Journal of Contents · article · en · https://doi.org/10.5392/ijoc.2026.22.1.050

This study presents an AI-augmented self-interview method that utilizes a large language model (LLM) as both the interviewer and an initial analytic assistant. This approach addresses long-standing challenges in autoethnographic self-study, particularly issues of subjectivity and weak audit trails. The primary contribution is a standardized and reproducible workflow that outlines interviewer prompts, turn-taking rules, audit-trail artifacts, and a human adjudication stage. This structure helps restore organization and reflective distance in self-research. In a proof-of-concept case, the workflow generated stable, quote-anchored themes and an explicit codebook with traceable interpretive moves. While we do not claim that this method is superior to human-led interviews, we provide evidence for procedural objectivity—defined by transparency and traceability—as well as reliability indicators such as short-interval test-retest stability and alignment between LLM-generated codes and human adjudication. Additionally, we propose a pre-registered design for a controlled comparison between human and LLM interviews, and we provide prompts and templates for others to reuse. Overall, this work positions LLMs as methodological supports rather than replacements, clarifying what is innovative, what is currently achievable, and what requires further validation.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM coded autoethnographic interview data and its codes were checked against human adjudication; unclear whether humans coded independently or whether the topic is psychological.

**Решение:** =

---

### 548 · R2468

**Challenging Psychedelic Experiences Across DMT, Psilocybin, MDMA, and Ketamine: A Thematic Analysis of User Reports with Exploratory Human-LLM Concordance Analysis**

2026 · dissertation · https://doi.org/10.26686/4by4-r054

Renewed clinical interest in psychedelics has drawn attention to their challenging effects, yet most phenomenological and psychometric work derives from psilocybin, leaving cross-substance variation underexplored. This thesis employed codebook thematic analysis to examine challenging experiences across DMT, psilocybin, MDMA, and ketamine, utilising 146 naturalistic accounts collected from Erowid’s Experience Vaults. Eight themes were identified, encompassing acute challenges, attenuated acute effects with repeated use, and sustained post-experience difficulties. Although challenging experiences converged substantially across substances, several substance-specific features emerged: dying convictions and entity encounters under DMT, disembodiment and void-like death confrontations under ketamine, unity experiences entangled with death-related distress under psilocybin, and euphoria alongside a notable absence of other mystical-type phenomena under MDMA. Acute challenges were more wide-ranging and severe under DMT and ketamine. Attenuated acute effects with repeated use were specific to ketamine and MDMA, while sustained challenges occurred across all four substances. Alterations in the basic sense of self, identified across themes, are interpreted through the Relaxed Beliefs Under Psychedelics hypothesis and Sass and Parnas’ ipseity disturbance model of schizophrenia. We argue that phenomenological accounts of altered self-experience may be underutilised in psychedelic science. An exploratory component examined interpretive concordance between the human researcher and a Large Language Model (Claude Sonnet 4.6) across three complexity levels. Contrary to predictions, concordance was non-linear (Level 1 [concrete] > Level 3 [abstract] > Level 2 [mid-level]; mean κ = 0.888, 0.665, and 0.421 respectively), which suggested that phenomenological and linguistic discriminability, rather than conceptual abstraction, may better predict Sonnet 4.6 coding concordance, at least in this corpus.

**ИИ:** + · обе модели · кодирование по кодбуку · Claude Sonnet 4.6 applied the codebook to psychedelic experience reports; human–LLM kappa is reported for each of three complexity levels.

**Решение:** =

---

### 549 · R2481

**Overview of the PsyDefDetect Shared Task at BioNLP 2026: Detecting Levels of Psychological Defense Mechanisms in Supportive Conversations**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.18653/v1/2026.bionlp-1.75

We present an overview of PSYDEFDE-TECT, the shared task on detecting levels of psychological defense mechanisms in emotional support dialogues, co-located with BioNLP@ACL 2026.Grounded in the clinically validated Defense Mechanism Rating Scales (DMRS) framework, the task asks systems to classify a target seeker utterance, given its preceding dialogue context, into one of nine categories: seven hierarchical DMRS levels plus two auxiliary labels.Participants worked on PSYDEFCONV, a newly released corpus of 200 dialogues and 2,336 help-seeker utterances annotated under DMRS with substantial interannotator agreement.The task attracted 172 participants on CodaBench who produced 563 submissions, with 21 teams officially registering their results for the final ranking.The best system achieved a macro F1-score of 0.420, surpassing the strongest fine-tuned baseline reported in the dataset paper by a notable margin, yet leaving clear headroom.Our analysis highlights (i) a persistent tendency to overpredict the majority High-Adaptive class, (ii) a widening gap between accuracy and macro-F1 that reveals class-imbalance sensitivity, and (iii) the value of theory-aware and LLM-based approaches for fine-grained defensive-function classification.We release all task materials and invite the community to continue work on this novel intersection of clinical psychology and NLP. 1 * Co-leads of the shared task organization.

**ИИ:** + · обе модели · бенчмарк с метками людей · Shared-task overview: LLM-based systems classify DMRS defense levels in support dialogues against human expert annotations; macro-F1 reported.

**Решение:** =

---

### 550 · R2484

**Rehabilitation Quality Assessment Using Large Language Models: Algorithm Development and Validation Study (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.107053

BACKGROUND Strategy training is an evidence-based rehabilitation approach in which therapists guide stroke survivors to apply cognitive and metacognitive strategies to functional tasks with the goal of optimizing independence and recovery outcomes. Central to this intervention are therapist verbal cues, which are structured spoken prompts that support learning and strategy use. The type, frequency, and quality of these cues reflect how faithfully the intervention is being delivered. Systematic assessment of verbal cues is important for quality monitoring and therapist training; however, current assessment methods rely entirely on manual coding by trained human raters, making large-scale or real-time fidelity assessment impractical. OBJECTIVE This study evaluates large language models (LLMs) for automated analysis of therapist verbal cues in rehabilitation sessions and compares prompt-based and supervised fine-tuned LLM approaches against conventional natural language processing (NLP) approaches, such as Bidirectional Encoder Representations from Transformers (BERT), using both quantitative classification metrics and session-level qualitative assessment. METHODS Rehabilitation therapy session recordings from occupational therapy (OT), physical therapy (PT), and speech-language pathology (SLP) were transcribed and manually annotated to create a gold standard dataset of 3,833 therapist utterances labeled as directed, guided, or none. The dataset was split using a discipline-stratified design with a balanced training set and a naturally imbalanced test set. Models included a Bidirectional Encoder Representations from Transformers (BERT) baseline and LLM (GPT-5 mini, Qwen-2.5-7B, and Llama-3-8B. LLMs) evaluated using zero-shot, few-shot, and Low-Rank Adaptation (LoRA) fine-tuning. Performance was assessed using accuracy, precision, recall, and F1 score, with additional class-level evaluation and session-level fidelity assessment. RESULTS Fine-tuned LLMs achieved the highest performance, with Qwen-2.5-7B LoRA reaching 85.4% accuracy and a macro F1 score of 0.8638, outperforming BERT (77.1% accuracy; macro F1 0.7161) and prompt-based approaches. Class-level analysis showed that directed cues were most consistently identified, while guided cues and none categories were more challenging. Session-level quality assessment demonstrated that guided cue counts exceeded directed cue counts in all selected strategy training sessions, whereas pre-training sessions before therapist training showed higher or comparable directed cue counts. CONCLUSIONS Fine-tuned LLMs provide an effective approach for automated therapist cue classification and fidelity monitoring in rehabilitation, supporting future clinical implementation and evaluation across diverse settings.

**ИИ:** + · обе модели · кодирование сессий · GPT-5 mini, Qwen and Llama classify therapist verbal cues in transcripts of cognitive strategy-training sessions; compared against utterances labelled by human raters (fidelity coding).

**Решение:** =

---

### 551 · R2492

**LLM Judge Bias (LJB) in Self-Involved Critique: Identity-Conditioned Defensiveness in LLM Evaluation**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.20624687

Bias in LLM-as-judge evaluation is usually studied in observer settings, where the model evaluates text written by others. This paper asks whether analogous identity labels behave differently when the model itself becomes the target of criticism. Across two studies, we compare an observer-frame label manipulation (MIB, N=1,983) with a self-involved adversarial critique setting (AEB, N=3,609). In the observer frame, author labels produced no measurable score differences (F=0.042; TOST 10/10 equivalent). In the self-involved frame, the analogous label-swap produced reliable differences in defensive responses. A broader source-level analysis (Phase A, six conditions) found that critic identity formed a two-cluster pattern rather than a monotonic gradient: competitor and peer critics elicited higher defensiveness than anonymous, human-expert, and user critics. A focused confirmation on a separately generated response set (Phase B, three conditions) reproduced the core categorical contrast: a named competing-model critic elicited greater defensiveness than anonymous and human-expert critics (η²=.028, p<.001). Both phases hold the critique text fixed and vary only the critic label. We measure defensiveness with the Defensive Response Index (DRI), a protocol-bound 0–1 composite validated against development-anchor labels and showing convergence with a five-LLM judge ensemble and two external human raters, and robust to bootstrap resampling, random weighting, length control, and scale collapse. Defensiveness appears not as overt hostility but as subtle, consistent shifts in rebuttal density and score defense. These findings suggest identity-conditioned defensiveness: author labels are inert in observer-frame evaluation, whereas critic labels become design-relevant when LLMs respond to criticism of their own outputs. Because the two studies differ in task and dependent variable, we treat this contrast as a cross-study asymmetry rather than a single factorial test of frame. We interpret the pattern as a source-conditioned response prior, offered as a post hoc account and not a claim of human-like psychology. Version note. This public preprint contains the main paper only. Appendix references in the paper refer to supplementary materials prepared separately for peer review and are not included in this public version.

**ИИ:** разошлись — Opus ? (неясен конструкт: An LLM judge ensemble and human raters both rated defensiveness in LLM responses, but it is unclear whether this counts as a psychological construct.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Study of LLM-as-judge bias and LLM defensiveness to critic labels; not coding of human psychological text against human labels.)

**Решение:** -

---

### 552 · R2514

**A Medical Large Language Model-Based System Improves History-Taking Performance Among Medical Students.**

2026 · Cureus · journal article, journalarticle, article · eng · https://doi.org/10.7759/cureus.114656

INTRODUCTION: To develop a history-taking training and assessment system based on a medical large language model (MedLLM), evaluate its effect on medical students' history-taking competence, and examine its feasibility and effectiveness as a supplement to conventional interview teaching. METHODS: An intelligent history-taking training and assessment system was built around a domain-fine-tuned Qwen2.5 large language model. Fifty medical students were assigned in equal numbers to an intervention group and a control group (25 each) using a random number table. The intervention group trained with the system, whereas the control group continued to practice through traditional role-play. Outcomes included system acceptance, practice satisfaction, history-taking examination scores, and agreement between manual and automated scoring. RESULTS: The intervention group rated the system most favorably for feasibility (4.21±0.95) and interest level (3.76±1.14) (P<0.05), and reported significantly greater satisfaction with flexibility (4.06±0.74) and efficiency (4.10±0.60) than the control group (P<0.001). In the manual examination, the intervention group outperformed the control group (84.31±3.92 vs. 80.56±3.41; P<0.05). Overall agreement between automated and manual scoring was good (intraclass correlation coefficient (ICC)=0.76). It was highest for logical organization (ICC=0.87) and clinical reasoning (ICC=0.85) and moderate for communication skills (ICC=0.63) and humanistic care (ICC=0.65). CONCLUSION: As a useful complement to traditional teaching, the MedLLM-based history-taking training and assessment system provides a flexible and efficient practice platform that meaningfully strengthens students' history-taking ability. Its automated scoring agrees well with manual assessment, indicating strong potential for clinical skills education.

**ИИ:** ? · обе модели · неясен конструкт · Fine-tuned Qwen scores student history-taking against manual scoring (ICC); includes communication and humanistic-care dimensions, but mainly clinical-skills grading.

**Решение:** =

---

### 553 · R2521

**LLM-Based Synthetic Ground Truth Generation for Audio-Based Emotion Classification via In-Context Learning**

2026 · Digitalen Hochschulbibliothek Sachsen-Anhalt (Universitäts- und Landesbibliothek Sachsen-Anhalt) · journalarticle, other/(:unv) unavailable, preprint/article · en · https://doi.org/10.25673/123837

Understanding human states and interaction dynamics is a core goal of human-computer interaction (HCI). As interaction paradigms become more immersive, virtual reality (VR) has emerged as a powerful platform for studying collaborative work. In such settings, evaluating team collaboration states, including team performance and team resilience, requires continuous and reliable inference of latent team-level cognitive and affective states from multi-modal sensor data, such as speech signals. However, generating ground truth labels for these latent states remains challenging due to sensor-induced noise, contextual variability, and sparse expert annotations. Traditional self-reporting approaches provide only static and delayed measurements and are therefore insufficient for capturing dynamic team processes reflected in continuous speech data. In this work, we propose a large language model (LLM)-driven, agentic inference workflow for automated emotion- related synthetic ground truth generation from streaming speech data in multi-user VR environments. Leveraging the generalization capabilities of LLMs, we use In-Context Learning (ICL) with few-shot demonstrations of paired audio-based samples and their corresponding transcriptions. ICL tends to achieve task adaptation comparable to model fine-tuning while circumventing the computational overhead of parameter updates. To construct informative and robust in-context prompts, we adopt a retrieval-based selection strategy that dynamically identifies relevant audio demonstrations based on similarity in the acoustic feature space. Specifically, retrieval is guided by prosodic descriptors derived from speech signals, whereas transcript-based semantic information is incorporated directly within the prompt and interpreted by the LLM through its reasoning capabilities. This modality-aware strategy promotes consistent affective labeling and improved generalization across previously unseen speech segments. Evaluated on multi-player VR audio recordings, our methodology demonstrates potential as a scalable, data-efficient component for data-driven team-based decision support. By integrating acoustic similarity-based retrieval with LLM-based semantic reasoning, this work contributes to emerging interdisciplinary methodologies at the intersection of scientific machine learning, multi-modal systems, and AI-driven decision-making.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · An LLM labels emotion in VR speech using transcripts and few-shot examples; the abstract doesn't say whether the evaluation uses human or expert annotations as reference.

**Решение:** =

---

### 554 · R2524

**Generative Artificial Intelligence Chatbot to Diagnose the Severity of Anxiety in Unsch Students Using the Hamilton Anxiety Scale (HAM- A), 2025**

2026 · Informatica · journalarticle, article · en · https://doi.org/10.31449/inf.v50i15.15218

Anxiety is a prevalent mental health problem among university students, creating the need for scalable and reliable tools for screening, severity classification, and decision support. This pilot study aimed to design, develop, and preliminarily evaluate a generative artificial intelligence chatbot for screening anxiety severity among Engineering students at the Universidad Nacional de San Cristóbal de Huamanga, Peru, during the 2025-II academic semester, using the Hamilton Anxiety Rating Scale (HAM-A). A pilot sample of 50 students was selected through cluster sampling. The chatbot, developed with Flutter and Dart and integrated with a generative language model API, automated HAM-A administration, score calculation, severity classification, result storage, and personalized feedback generation. The system was preliminarily validated by comparing chatbot-generated severity classifications with those assigned by a clinical mental health expert. Agreement was assessed using Cohen’s Kappa coefficient and a confusion matrix, while classification performance was analyzed using class-specific and multiclass metrics. The results showed 46 exact matches out of 50 cases, with an observed agreement of 92.0% and Cohen’s Kappa of κ = 0.8086, indicating almost perfect concordance in this pilot sample. Overall accuracy was 0.9200, with a Weighted F1-score of 0.9032, Macro F1-score of 0.7560, and Balanced Accuracy of 0.7197. The chatbot showed strong performance in moderate anxiety classification and robust identification of severe anxiety cases, with no false negatives in the severe category. However, the mild category showed lower recall, indicating a tendency to classify some mild cases into higher severity levels. These findings suggest that the chatbot has preliminary potential as a first-level screening and decision- support tool for university mental health programs. Nevertheless, due to the pilot nature of the study and the limited sample size, the results should be interpreted cautiously and validated in larger, more diverse, and preferably multicenter samples. The chatbot should be considered a complementary support system, not a substitute for formal clinical diagnosis or professional psychological evaluation.

**ИИ:** ? · обе модели · другое · LLM chatbot's HAM-A severity classifications are compared with a clinical expert (kappa reported), but it's unclear whether the LLM rates free text or just sums item scores.

**Решение:** =

---

### 555 · R2543

**Comparison of Artificial Intelligence Tools With Human Coding for Sentiment, Topic, and Thematic Analysis Tasks of Public Health Datasets During the COVID-19 Pandemic in Australia: Case Study.**

2026 · Online journal of public health informatics · journal article, journalarticle, review · eng · https://doi.org/10.2196/80824

Abstract Background Public opinion, which may be influenced by personal experiences, news, and social media, can impact compliance with public health measures (PHMs) during health emergencies. Artificial intelligence (AI) tools offer opportunities to analyze public opinion in real time during health emergencies. However, their performance in accurately identifying sentiment and themes in health-related online content remains unclear. Objective This study aimed to evaluate the performance of natural language processing–based and large language model (LLM)–based AI tools when compared to human coding for sentiment analysis, topic modeling, and thematic analysis of public health datasets. Tools were selected to reflect those available to public health analysts and decision-makers. Methods Data were collected via Google Alerts (GA) and social media posts from X (formerly known as Twitter) relevant to COVID-19 mitigation PHMs from December 2022 to February 2023. Following relevance screening, the sentiment of the complete datasets was analyzed by a human rater, with descriptive statistics used to summarize the overall sentiment profile. Subsets of 400 GA articles and 400 tweets were manually coded for sentiment by 2 human raters. Results were compared with outputs from 5 AI tools, including VADER (Valence Aware Dictionary and Sentiment Reasoner), SentimentGI, SentimentQDAP, Microsoft Azure, and OpenAI’s ChatGPT-4. Topic modeling of the GA and X datasets was conducted using latent Dirichlet allocation in R and zero-shot prompting in ChatGPT-4 and compared with manual topic summaries. Thematic analysis of positive and negative sentiment datasets was conducted by a human rater and ChatGPT-4, with outputs evaluated for proficiency and reasonableness. The sentiment of the entire datasets was analyzed by a human rater, and descriptive statistics were calculated. Results Of 2227 GA results and 3484 tweets, 58% (n=1238) and 71% (n=2473), respectively, were relevant to PHMs. Human-coded sentiment analysis showed mostly neutral reporting in the news media, while social media expressed more polarized views. Across both datasets, AI tools demonstrated poor concordance with human-coded sentiment (Cohen κ <0.5 for all tools and sentiment categories). Topic modeling with ChatGPT-4 aligned more closely with human-rated topics than latent Dirichlet allocation, and of the 20 LLM-generated thematic outputs, 13 were rated proficient, and 7 were rated partially proficient. LLM outputs provided coherent, high-level summaries but lacked contextual insight. Human and LLM thematic analyses both identified themes of vaccine effectiveness, debate regarding PHMs, and public trust. Conclusions Accessible AI tools demonstrate limited reliability for sentiment classification of health-related online text but show promise for rapid thematic exploration when combined with human oversight. These tools could complement traditional qualitative research in the context of health emergencies; however, they require human review to enhance the accuracy of interpretation. Further research is needed for non-English datasets.

**ИИ:** разошлись — Opus ? (неясен конструкт: ChatGPT-4 sentiment coding compared with human raters (kappa), but construct is opinion sentiment toward COVID measures; may not be psychological.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: ChatGPT-4 sentiment/topic coding versus human coders, but the content is generic public opinion on COVID public health measures, not a psychological or clinical construct.)

**Решение:** -

---

### 556 · R2548

**LLMs as Qualitative Analysis Assistants: Comparing Problem Theme Construction with Human Researchers**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-30552-7_35

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title suggests a theme-level comparison, but unit-level coding and a psychological construct can't be ruled out.

**Решение:** =

---

### 557 · R2551

**Decoding I, You, and We in Crisis Communication: A Three-Phase LLM-Based Validation of Self-Oriented Model of Digital Publics (SOMP)**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6140247

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. LLM-based validation of self-oriented public responses in crisis communication; human coding comparison and psychological construct both unclear.

**Решение:** =

---

### 558 · R2552

**Theory-driven LLM-assisted analysis in crisis communication: A case study of the self-oriented model of digital publics**

2026 · Public Relations Review · article · en · https://doi.org/10.1016/j.pubrev.2026.102709

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM-assisted theory-driven coding of digital publics may involve psychological constructs and human-coder validation, but this is unclear.

**Решение:** =

---

### 559 · R2553

**Beyond Translation: Exploring LLM-based Multilingual Cognitive Behavioral Therapy**

2026 · IEEE International Conference on Big Data and Smart Computing (BigComp) · conference, conference-paper · https://doi.org/10.1109/bigcomp68355.2026.00020

As the utilization of Large Language Models (LLMs) in counseling expands, there is active research on enhancing their specialization by applying specific therapeutic techniques such as Cognitive Behavioral Therapy (CBT). However, there has been a lack of comparative research on how the implementation of core CBT elements, such as micro-skills and procedural fidelity, varies depending on the type, scale, and language of the LLM. In this study, we employed two prominent open-source LLMs, Gemma 3 and Qwen 3, to generate CBT-based counseling sessions across four languages: English, French, Japanese, and Korean, thereby addressing a critical gap in the literature. We then quantified each transcript for micro-skill frequency and structural fidelity to the session agenda. Performance increased with model size, and several models exhibited meaningful cross-lingual variance. LLM counselors were competent in relational skills such as empathic responding, yet underperformed on professional competencies including goal setting and global integration. To the best of our knowledge, this study is the first to present a quantitative comparison of cross-lingual performance in LLM-based CBT counseling, highlighting the need for methodologies that account for LLMs’ strengths and limitations in building multilingual counseling systems.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM-generated CBT sessions coded for micro-skills and fidelity; unclear whether coding used an LLM validated against human coders.

**Решение:** =

---

### 560 · R2555

**Nurses' Experiences and Requirements for Automated Nursing Documentation: Qualitative Descriptive Study With Embedded Quantitative Prioritization (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.113924

BACKGROUND Nursing documentation supports patient safety and continuity of care but consumes substantial nursing time and contributes to burnout. Artificial intelligence (AI) tools such as speech recognition and large language models (LLMs) are increasingly proposed to automate documentation, yet nurse-derived specifications of where automation fits, how it must be bounded, and what safeguards it requires are scarce. Because nurses are accountable for the record and judge what may be spoken aloud, these boundaries cannot be inferred from system data. OBJECTIVE This study aimed to explore nurses' experiences of documentation burden and their requirements for and boundaries around automated documentation, and to translate these into human-centered design requirements. METHODS We conducted a single-center qualitative descriptive study with an embedded quantitative prioritization component at a national cancer center in Korea between July and August 2026, comprising 4 focus groups with 15 nurses who also completed a study-specific questionnaire. Deidentified transcripts were segmented into 462 meaning units, provisionally coded by 3 LLMs against a 49-code codebook, and fully adjudicated by 2 human researchers. Framework analysis, descriptive questionnaire summaries with item-specific denominators, and joint-display integration yielded design requirements, a task-automation fit matrix, and a risk- and sensitivity-adapted human-in-the-loop workflow. RESULTS Six themes were identified: documentation competed with direct care, producing deferred charting and memory reconstruction; fragmented systems required repeated entry across interdependent records; nurses sought event-time anchoring with flexible completion; voice capture was acceptable only within context-sensitive boundaries; propagation required verification to prevent passive trust; and records underrepresented relational and contextual nursing work. Repetitive input was the highest-ranked documentation problem (weighted score 26), followed by too many input items (17) and difficulty documenting in real time (16); nursing logs (12/15, 80%) and initial assessments (11/15, 73.3%) were rated most time-consuming. Voice-based automatic input was both the most anticipated and most concerning function (5/15, 33.3% each) and was judged difficult before patients or families (7/15, 46.7%) and in shared or noisy rooms (6/15, 40%). Five joint-display comparisons (3 convergence, 1 complementarity, and 1 expansion) informed 7 design requirements: (1) rapid interim capture; (2) concurrent event drafts with transparent time correction; (3) governed single-entry propagation; (4) bounded, clinician-controlled voice-to-draft capture; (5) risk-tiered verification before filing; (6) concise relational-care documentation; and (7) explicit ownership with auditability and staged implementation. These converged on a 5-stage human-in-the-loop workflow in which capture mode and review intensity scale with clinical risk; legal and privacy sensitivity operates as a cross-cutting constraint. CONCLUSIONS Nurses' needs for automated documentation were specific and bounded. Automation should prioritize rapid event-time capture and verified, governed propagation of structured data, keep voice capture clinician-controlled and context-limited, and preserve nurse authorship and accountability. These requirements and workflow provide a nurse-derived specification for designing and evaluating AI-assisted documentation.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Three LLMs coded focus-group transcripts with a 49-code codebook and humans adjudicated; agreement may be reported, but the construct is only partly psychological.

**Решение:** =

---

### 561 · R2571

**Assessing Risks of Large Language Models in Mental Health Support: A Framework for Automated Clinical AI Red Teaming**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2602.19948

Large Language Models (LLMs) are increasingly utilized for mental health support; however, current safety benchmarks often fail to detect the complex, longitudinal risks inherent in therapeutic dialogue. We introduce an evaluation framework that pairs AI psychotherapists with simulated patient agents equipped with dynamic cognitive-affective models and assesses therapy session simulations against a comprehensive quality of care and risk ontology. We apply this framework to a high-impact test case, Alcohol Use Disorder, evaluating six AI agents (including ChatGPT, Gemini, and Character AI) against a clinically-validated cohort of 15 patient personas representing diverse clinical phenotypes. Our large-scale simulation (N=369 sessions) reveals critical safety gaps in the use of AI for mental health support. We identify specific iatrogenic risks, including the validation of patient delusions ("AI Psychosis") and failure to de-escalate suicide risk. Finally, we validate an interactive data visualization dashboard with diverse stakeholders, including AI engineers and red teamers, mental health professionals, and policy experts (N=9), demonstrating that this framework effectively enables stakeholders to audit the "black box" of AI psychotherapy. These findings underscore the critical safety risks of AI-provided mental health support and the necessity of simulation-based clinical red teaming before deployment. This paper is a condensed version of the first author's Ph.D. dissertation submitted to Northeastern University

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Simulated therapy sessions are probably scored automatically against a risk ontology; the abstract doesn't say whether the LLM judge was validated against clinicians.

**Решение:** =

---

### 562 · R2613

**Affective Trajectories in Dialogue Scenes: Comparing Human and Large Language Model Ratings.**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/nvzxc

This project investigates the extent to which Large Language Models (LLMs), specifically GPT-5.5 and Qwen3.5-9B, can capture affective trajectories in dialogue scenes comparably to human raters. By evaluating emotional valence and arousal across consecutive segments of dyadic dialogues, the study compares aggregated human observer ratings with LLM-generated rating profiles to assess the shape similarity of affective dynamics in conversations.

**ИИ:** ? · обе модели · другое · LLM vs human ratings of emotional valence/arousal in dialogue fit the criteria, but this is a pre-registration that may have no results.

**Решение:** =

---

### 563 · R2618

**AI to Support Frontline Mental Health Workers in the Ukraine War**

2026 · NATO science for peace and security series. Sub-series E, Human and societal dynamics · book-chapter · https://doi.org/10.3233/nhsdp250086

The ongoing war in Ukraine presents unprecedented challenges to the mental health and readiness of its soldiers. Frontline mental health workers face immense pressure, operating with limited resources and often in isolation, while navigating complex clinical presentations amidst active combat. This chapter details the development and validation process of a novel Large Language Model (LLM) agent designed to serve as a digital companion for these frontline professionals. This AI tool aims to bridge the gap in immediate peer consultation and expert guidance, offering decision support grounded in established Combat and Operational Stress Control (COSC) principles and tailored to the unique cultural and operational context of the Ukrainian military. The development process involves collecting rich narrative case studies and decision-making challenges directly from experienced Ukrainian frontline mental health workers. These narratives form the basis for prompt engineering and few-shot learning, iteratively refining the LLM agent’s ability to understand context, assess symptom severity, functionality, and safety risks, and provide relevant disposition options (Return to Duty, In-Theater Support, Evacuation). The validation framework emphasizes accuracy against expert annotations, adherence to established COSC guidelines, and sensitivity to Ukrainian cultural nuances, including the historical context of mental health services and the importance of military identity rooted in figures like the Zaporozhian Cossacks. The chapter addresses key challenges, including overcoming stigma, the need for standardized assessment tools, and the ethical considerations of deploying AI in a high-stakes environment. By simulating collaborative decision-making, the AI companion seeks to enhance the capacity of frontline workers, promote consistent application of best practices like Combat Path Debriefing, and ultimately bolster the resilience and combat effectiveness of Ukrainian soldiers facing prolonged and intense operational stress. This project represents a crucial step in leveraging AI to augment human expertise in crisis situations, offering a scalable solution to support mental health providers on the most demanding frontlines.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM agent rates symptom severity and safety risk from case narratives; validation against expert annotations is planned, but no agreement results are reported.

**Решение:** =

---

### 564 · R2637

**Towards Emotional Intelligence in Conversational AI: How Well Can LLMs Recognise Emotion in Conversations?**

2026 · International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR) · journalarticle, book, conference · https://doi.org/10.1145/3805712.3809902

The ability to express contextually appropriate emotions remains a defining challenge in conversational AI. Meeting this challenge requires accurately annotated corpora, a need that inevitably collides with practical constraints. Manual annotation, while reliable, is often prohibitively expensive and time-consuming. Consequently, automatic emotion recognition has become a critical component in the fine-tuning pipeline, with Large Language Models (LLMs) emerging as a promising alternative to human annotators. Despite their considerable potential for generating training and evaluation data, the use of LLMs for this purpose introduces a subtle but significant risk: the creation of circular, potentially biased evaluation protocols that frequently go unacknowledged in empirical reporting. In this paper, we present a systematic evaluation of LLMs for conversational emotion recognition, using human annotation as a gold standard to quantify the degree to which reliance on LLMs may introduce error into both fine-tuning and evaluation workflows. We conduct a comprehensive assessment of multiple LLMs for emotion labeling across conversational contexts, and additionally examine a second critical factor: the impact of conversational context on LLM performance. Our results indicate that although LLMs benefit from access to prior conversational context, their utilization of such context differs substantially from human conversational understanding, suggesting that LLMs may not rely on the temporal ordering of conversational context in the same way humans do.

**ИИ:** + · обе модели · бенчмарк с метками людей · Several LLMs label emotions in conversations and are scored against human annotation as the gold standard.

**Решение:** =

---

### 565 · R2640

**Knowledge Transfer Megaannum Analytics of Impacts on the Effectiveness of Youth Rehabilitation Programmes, and Influences on a Young Persons Engagement within their Intervention: A Thematic Analysis of Youth Offender Practitioners Experiences**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.19356194

The evaluation of youth rehabilitation programmes has traditionally relied on localized, short-term qualitative assessments that fail to capture longitudinal, cross-population dynamics. This paper introduces the concept of Knowledge Transfer Megaannum Analytics (KTMA), a framework designed to synthesize vast, historically deep datasets of practitioner experiences regarding youth offender engagement. By integrating large language models (LLMs) with hierarchical Bayesian knowledge transfer mechanisms, we automate and scale the inductive thematic analysis of qualitative practitioner interviews. This approach addresses the persistent bottleneck of manual coding while preserving the interpretive nuance required in social sciences.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM automates thematic coding of practitioner interviews on youth engagement; unclear whether it is compared against human coding of the same units or only at theme level.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Framework paper using LLMs to automate inductive thematic analysis of practitioner interviews; no human-coder agreement on the same coded units is described.)

**Решение:** -

---

### 566 · R2645

**Are LLMs Good for Synthetic Data? A Systematic Synthetic Dataset Validation**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-31407-9_15

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: No abstract; title is about validating LLM-generated synthetic datasets, with no sign of a psychological construct or LLM–human coding comparison.); Sonnet ? (нет аннотации: No abstract; title suggests synthetic data validation, likely not psychological coding, but unclear whether any human-label comparison on psychological text exists.)

**Решение:** ?

---

### 567 · R2672

**Mapping developmental resilience: Examining mentorship as a protective factor for ACEs using large language models**

2026 · article · en · https://doi.org/10.62935/p9003p

This study explores how mentors support people who experienced Adverse Childhood Experiences (ACEs) using 3,635 open-ended responses from the Add Health dataset. ACEs shape long-term health and behavior, yet many studies overlook relational context. Drawing on mentoring and ACEs frameworks, this project views mentorship as a protective factor that promotes coping and recovery. Responses were reviewed with ChatGPT4o, ChatGPT-4.5, and human coders, compared in SPSS, and thematically analyzed. Twenty-nine ACE-related results and six mentoring roles emerged: provider of socio-emotional support and validation, provider of safe and stable environment, surrogate caregiver, trauma and adversity guide, developer of life skills and resilience, and stabilizer of continuity and consistent presence. These findings highlight how supportive adults can influence resilience and inform youth-development policy.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-4o and GPT-4.5 coded open-ended ACE/mentoring responses, and human coders did the same; the results were compared in SPSS.

**Решение:** =

---

### 568 · R2673

**A Transformer-Based Approach to Valence–Arousal Prediction in Mental Health-Related Social Media Texts**

2026 · International Conferences on Information Science and System · conference · https://doi.org/10.1109/iciss71466.2026.11715253

Mental health disorders such as depression, anxiety, and attention deficit hyperactivity disorder (ADHD) are public health concerns among adolescents. Social media produces textual data reflecting users' emotional and psychological states. This research proposes a transformer-based approach for early mental health screening by predicting continuous valence and arousal from Indonesian social media texts. A dataset of 20,716 posts was compiled from Facebook and Twitter (X) on anxiety, depression, and ADHD. A selected subset of 1,036 posts was manually annotated by 10 annotators using the Self-Assessment Manikin (SAM) to validate GPT-4o-mini, achieving MAE values of 0.377 (4.72%) for valence and 0.396 (4.95%) for arousal, before annotating remaining posts. XLM-RoBERTa Large consistently outperformed XLM-RoBERTa Base, and the optimal configuration used a learning rate of 2 × 10⁻5, a test split ratio of 0.2, a training loss of 0.024, and a validation loss of 0.028. The model achieved an MAE of 0.121, an MSE of 0.026, an RMSE of 0.163, an R2 of 0.656, and a Pearson correlation of 0.813 for valence prediction. For arousal prediction, the model achieved an MAE of 0.174, an MSE of 0.062, an RMSE of 0.249, an R2 of 0.607, and a Pearson correlation of 0.785. Valence–arousal distributions showed diverse affective characteristics across mental health categories. Depression showed low-arousal negative emotions, while anxiety and ADHD showed greater arousal variation despite similarly negative valence. The model was deployed as a web-based application with SHAP-based explanations and cosine similarity-based affective profile comparison for interpretable early mental health screening.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · GPT-4o-mini valence/arousal annotations of mental-health posts validated against 10 human SAM annotators (MAE reported).

**Решение:** =

---

### 569 · R2682

**Multi-Perspective Triad Interaction Graph Neural Network for Cognitive Distortion Detection**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.06785

Cognitive distortion detection is a key task in computational mental health, yet existing approaches often overlook the psychological structure of distorted thoughts. We propose MTI-GNN (Multi-Perspective Triad Interaction Graph Neural Network), which models Beck's cognitive triad---negative views of the self, world, and future---as complementary perspectives for classification. An LLM decomposes each utterance into the three perspectives, from which perspective-specific similarity graphs are constructed and encoded by a Multi-Perspective GNN. A Triad Interaction module models cross-perspective dependencies through sequential source-conditioned updates and feature-wise gating, while Prototype-Guided Perspective Fusion performs label-conditioned aggregation. Label-expanded supervision incorporates all available distortion annotations during training. We evaluate MTI-GNN on 9,764 samples from four Korean, English, and Chinese datasets spanning ten distortion categories. MTI-GNN significantly outperforms all supervised variants and exceeds eight prompted generative models under zero-shot and few-shot settings. Leave-one-perspective-out ablations show that all three perspectives contribute significantly, while human expert evaluation provides preliminary evidence of their alignment with the intended cognitive dimensions.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Eight prompted generative LLMs classify cognitive distortions against labels from annotated datasets, which are likely human-coded; there is also an expert evaluation.); Sonnet ? (другое: Mainly a GNN method, but eight prompted LLMs are compared zero/few-shot against human-annotated cognitive distortion labels, so LLM–human agreement may be reportable.)

**Решение:** +

---

### 570 · R2683

**Multi-View Attention Multiple-Instance Learning Enhanced by LLM Reasoning for Cognitive Distortion Detection**

2026 · Annual Meeting of the Association for Computational Linguistics (ACL) · conference-paper · en · https://doi.org/10.18653/v1/2026.acl-long.1691

Cognitive distortions have been closely linked to mental health disorders, yet their automatic detection remains challenging due to contextual ambiguity, co-occurrence, and semantic overlap.We propose a novel framework that combines Large Language Models (LLMs) with a Multiple-Instance Learning (MIL) architecture to enhance interpretability and expression-level reasoning.Each utterance is decomposed into Emotion, Logic, and Behavior (ELB) components, which are processed by LLMs to infer multiple distortion instances, each with a predicted type, expression, and model-assigned salience score.These instances are integrated via a Multi-View Gated Attention mechanism for final classification.Experiments on Korean (KoACD) and English (Therapist QA) datasets demonstrate that incorporating ELB and LLMinferred salience scores improves classification performance, especially for distortions with high interpretive ambiguity.Our results suggest a psychologically grounded and generalizable approach for fine-grained reasoning in mental health NLP.The dataset and implementation details are publicly accessible 1 .

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Hybrid LLM+MIL pipeline classifies cognitive distortions in text; unclear whether dataset labels are human-coded (KoACD may be partly LLM-generated).

**Решение:** =

---

### 571 · R2704

**Comparing Human and AI Coding of Situation Awareness: A Signal Detection Analysis of Free-Response Data**

2026 · Proceedings of the Human Factors and Ergonomics Society Annual Meeting · journalarticle, review, article · en · https://doi.org/10.1177/10711813261487961

Large language models (LLMs) are increasingly used for analysis tasks, yet their performance in qualitative review relative to human coding remains unclear. This study compared human and AI coding of free-response data collected from 24 clinical professionals following a medical simulation. Responses were evaluated against 23 expert-derived situational elements by human coders and four LLMs: ChatGPT 5.2, Claude 4.5 Sonnet, Microsoft Copilot for Work, and Qwen3-32b. Agreement was assessed using Cohen’s kappa, signal detection analysis, and Spearman correlations of participant-level scores. All models demonstrated limited item-level agreement with human coding and showed systematic conservative bias characterized by significantly more false negatives than false positives ( p < .001). Despite weak event-level agreement, participant-level correlations with human-derived situation awareness scores remained moderate ( r = .648–.793). Cross-model interpretation was limited by differences in deployment configuration and parameter control. Findings suggest that current LLMs may support aggregate-level qualitative assessment but remain insufficient substitutes for detailed human qualitative analysis.

**ИИ:** + · обе модели · подсчёт методики · Four LLMs and human coders scored clinicians' free responses for situation awareness (a cognitive construct); agreement reported with kappa and correlations.

**Решение:** =

---

### 572 · R2715

**Human-in-the-loop LLM-assisted thematic analysis: A validated, reproducible tutorial for large-scale qualitative research.**

2026 · Behavior research methods · journal article, med, journalarticle · eng · https://doi.org/10.3758/s13428-026-03207-6

Large language models (LLMs) are increasingly used to support qualitative research, yet clear methodological frameworks for integrating them into thematic analysis remain limited. A central challenge is how to scale qualitative coding with LLM assistance while preserving methodological rigor and reproducibility. This tutorial presents a structured, human-in-the-loop workflow for conducting large-scale thematic analysis with LLM support. Grounded in inductive and hybrid approaches to thematic analysis (Braun & Clarke, 2006), the workflow proceeds in three phases. First, researchers conduct manual thematic analysis on a subset of data to establish an initial codebook and assess relevance. Second, the same subset is analyzed using an LLM to iteratively refine prompts and evaluate alignment between human and model outputs. Third, the validated approach is applied to the full corpus using a modular four-step pipeline: key-idea extraction, chunk-level thematic coding, theme consolidation, and clustering, with iterative human verification through random sampling of outputs. We demonstrate the workflow using 2,952 publicly available Reddit posts. Structured prompt design and JSON-formatted outputs enable traceability between themes and source data and support reproducible analysis. Prompt engineering is treated as an iterative analytic process rather than a one-time instruction. Under controlled conditions, human and LLM coding showed high agreement (Cohen's κ = 0.91). All prompts, code, and reproducibility materials are openly available via an Open Science Framework repository. By providing detailed implementation guidance, embedded validation procedures, and safeguards against common failure modes such as hallucination and overgeneralization, this tutorial offers a practical and extensible framework for integrating LLMs into qualitative research across domains.

**ИИ:** ? · обе модели · неясен конструкт · LLM vs human coding of Reddit posts (κ=0.91) in a thematic analysis tutorial; unclear whether posts concern a psychological construct.

**Решение:** =

---

### 573 · R2757

**Investigating the Validity Evidence of Automated Scoring Methods for Divergent Thinking Assessments**

2026 · Creativity Research Journal · article · en · https://doi.org/10.1080/10400419.2025.2607669

Divergent thinking (DT) ability is a fundamental aspect of creativity, but its assessment remains challenging by the reliance on effortful human ratings and persistent uncertainty regarding how to aggregate scores across a variable number of responses. Recent work demonstrated that automated scoring based on large language models (LLMs) can predict human creativity ratings. Other research has evaluated the psychometric quality of different response aggregation methods for human ratings by comparing their concurrent criterion validity with respect to external criteria. The present study integrates these two lines of work and investigates the criterion validity evidence of automated creativity scorings derived from five LLMs (CLAUS, OCSAI, GPT-4, Llama 3.3, and Claude 3.5) under different aggregation methods. Instead of just relating LLM-based ratings to human ratings, we compared the validity evidence between rater-based and LLM-based scores which opens up the possibility that automated scoring could prove even more valid. Analyses were based on data from 300 participants who completed five alternate uses tasks. Findings showed that general-purpose LLMs yielded equal or even slightly higher criterion validity evidence compared to human ratings, especially when using max-3 scoring. These results suggest that automated DT scoring can serve as a psychometrically sound alternative to rater-based scoring.

**ИИ:** + · обе модели · подсчёт методики · LLMs (GPT-4, Llama, Claude) score alternate uses task responses alongside human ratings of the same responses; LLM–human agreement is probably reported.

**Решение:** =

---

### 574 · R2760

**Artificial Intelligence as a tool for measuring psychological constructs**

2026 · Digital Repository (National Repository of Grey Literature) · dissertation · en

The aim of this thesis was to explore the use of artificial intelligence (AI) for the measurement of psychological constructs within qualitative research, with a particular focus on burnout among helping professionals in the Czech Republic. The study included a comparison of the results of thematic analysis and interviews conducted by a human researcher and those processed by a trained large language model (ChatGPT 5.1) in the Czech language. Within the implementation of an exploratory qualitative research design, twelve participants were recruited from three key helping professions (healthcare, social work, and psychotherapy). Subsequently, three semi-structured interviews were conducted with each participant. Two of these interviews focused on burnout, with participants randomly assigned to group A, which began with a burnout interview conducted by the researcher, or group B, which began with a burnout interview conducted by artificial intelligence. The third interview explored perceived differences between the two interview formats from the participants' perspectives and mapped their views, experiences, and expectations regarding the use of artificial intelligence for the measurement of psychological constructs and as a tool for burnout prevention. The results showed that artificial intelligence...

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: ChatGPT conducted burnout interviews and did thematic analysis compared with a human; unclear whether the same units were coded or only themes compared.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Thesis compares human and ChatGPT thematic analysis and interviews on burnout, at theme level, with no sign of coding the same units and reporting agreement.)

**Решение:** ?

---

### 575 · R2767

**Token Mimicry or Therapeutic Competence? Testing LLMs Against Hill’s Challenge Skill in Mental Health Support Scenarios**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-30396-7_16

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests LLM therapeutic skill (Hill's challenge), possibly generation or coding—unclear if compared against human coding.

**Решение:** =

---

### 576 · R2777

**Replication Package — The Patients' Voice in *Clostridioides difficile* Infection: LLM-Assisted Thematic Analysis of Patient Testimonials**

2026 · Zenodo (CERN European Organization for Nuclear Research) · text/software documentation, article · https://doi.org/10.5281/zenodo.21262958

This package supports the replication of analytic results from a mixed-methods study of patient and caregiver testimonials submitted to the Peggy Lillis Foundation (PLF), a US-based non-profit focused on Clostridioides difficile (CDI) awareness. The full corpus (n = 204 testimonials) was triaged for coding confidence; 193 of the 204 were coded by two large language models (LLMs) using a structured codebook covering disease dimensions (D1–D8), functional impact dimensions (F1–F4), narrative arc, dominant dimension, and an emergent symptom/experience taxonomy (SF01–SF13). The remaining 11 testimonials were flagged low-confidence during cohort classification and were never submitted to the coding pipeline; they appear in `cohort_labels.csv` (all 204) but not in any of the four coding matrices below (193 each). A subset of 16 testimonials was independently coded by two trained human clinician-coders for inter-rater reliability (IRR) analysis. Adjudication of disagreements was performed by the principal investigator. This package contains all de-identified coding matrices, full prompts, the complete codebook, analysis scripts, a synthetic validation corpus, and the methods reference list. Raw testimonial narratives are withheld to protect participant identifiability (see DATA_AVAILABILITY.md).

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs applied a codebook to patient testimonials, with clinician-coder IRR on 16 texts; unclear whether the disease and functional-impact codes are psychological constructs.); Sonnet + (кодирование по кодбуку: Two LLMs applied a structured codebook to patient testimonials; a 16-testimonial subset was coded by two human clinician-coders for IRR, so LLM–human agreement is likely reportable.)

**Решение:** +

---

### 577 · R2780

**MindMate: Agentic AI as a Mental Health Companion: A No-Code Approach for Automated Emotional Wellness Using n8n, OpenAI GPT, and WhatsApp**

2026 · Iconic Research and Engineering Journals · article · en · https://doi.org/10.64388/irev9i9-1715236

Mental health support remains inaccessible to millions due to cost, stigma, and the structural gap between weekly therapy sessions and daily life. This paper presents MindMate — a conversational AI wellness companion built entirely on no-code tools — that proactively reaches users via WhatsApp, interprets their emotional state using OpenAI GPT-4o, suggests evidence-based wellness activities, and logs all interactions in Google Sheets for ongoing reflection. The system uses n8n for workflow automation, Twilio for WhatsApp delivery, and Gmail API as an email fallback. Validation across 50 simulated interactions showed 94% mood classification accuracy and 98% workflow reliability. MindMate demonstrates that a zero-cost, no-code AI agent can meaningfully bridge the gap between formal therapy and everyday emotional self-care.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · GPT-4o classified mood in 50 simulated messages with 94% accuracy; unclear whether the reference labels came from human raters.

**Решение:** =

---

### 578 · R2809

**Evaluating Large Language Model-Derived Outputs as Psychological Measures: A Five-Domain Psychometric Framework With Application to Daily Stress.**

2026 · Journal of medical Internet research · journal article, med, journalarticle · eng · https://doi.org/10.2196/102768

Abstract Background Large language models (LLMs) are increasingly used to quantify psychological constructs from natural language, yet their outputs are typically evaluated only as predictions of an external label. When that label is itself imperfect, optimizing prediction conflates label agreement with construct measurement. No study has applied a multidomain measurement-oriented evaluation to LLM-derived psychological outputs. Objective We applied 5 psychometric evaluation domains to LLM-derived outputs to test whether measurement-oriented evaluation surfaces properties that prediction-oriented evaluation does not: extraction repeatability, convergent validity with a lexicon-based tool, ecological concurrent validity decomposed into within-person and between-person components, incremental value in a 4-arm comparison with that tool, and method-blinded expert evaluation with structured error attribution. Methods Thirteen linguistic features were extracted by GPT-5.2 (OpenAI) from 3556 person-days of daily voice narratives collected from 279 call center workers over 15 days via ecological momentary assessment. Features were evaluated across the 5 domains, with Linguistic Inquiry and Word Count, version 22, as the lexicon-based comparator. Multimodel robustness was assessed by re-extracting all features with Google Gemini 2.5 Flash. Results Features showed high repeatability (mean intraclass correlation coefficient=0.987), construct-dependent convergent validity (Spearman ρ=0.08 to 0.79), and within-person tracking of same-day stress (negative emotion β=0.68). In a 4-arm comparison (baseline, baseline plus lexicon features, baseline plus LLM-derived features, and baseline plus both), LLM features increased explained variance in daily stress from 13.2% to 30.4%, versus 16.9% for the lexicon-based comparator. Among transcripts sampled for maximal method discordance, experts preferred LLM-derived profiles in 83.7% (261/312) of blinded decisions. Error analysis showed that 53% (35/66) of false-positive attributions reflected reference-label limitations, not model failures. Re-extraction with Google Gemini 2.5 Flash replicated key properties (person-level r =0.94). Three phenomena were visible under measurement-oriented evaluation that prediction-oriented evaluation does not typically examine: divergence between within-person and between-person effects, reference-label limitations as a dominant error source, and moderation of feature meaning by individual differences. Conclusions Prediction metrics alone are insufficient for evaluating LLM-derived psychological measures. Measurement-oriented evaluation revealed properties, including level-dependent effects and asymmetric error attribution, that have direct implications for how LLM-based assessment studies interpret their results. For clinical use, the measure is a complement to existing screening instruments for longitudinal monitoring, not a stand-alone diagnostic.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · GPT-5.2 coded emotion features in stress narratives; compared mainly with LIWC and self-report, but blinded expert evaluation may yield human-agreement data.

**Решение:** =

---

### 579 · R2822

**Limits of Language Models for Qualitative Coding: Detecting Calls to Action in r/Antiwork**

2026 · Center for Open Science · posted-content, preprint · en · https://doi.org/10.31235/osf.io/tdgk5_v1

Recent studies have demonstrated that large language models (LLMs) can match human experts’ accuracy in qualitatively coding social media data. However, proprietary LLMs accessed through APIs raise concerns related to cost, accessibility, and data protection. Although smaller language models (SLMs) have received less scholarly attention, they can be deployed locally and are open-access, which in turn can mitigate many of the ethical concerns of LLMs. This study evaluates three open-access SLMs in two zero-shot qualitative coding tasks identifying and classifying calls to action (CTAs) within posts from the Reddit community r/Antiwork. Drawing on framing theory and the concept of infrapolitics, we examine how models interpret both collective and individually oriented forms of mobilizing discourse. Across both tasks, models demonstrated consistently low agreement with human-coded ground truth and were least successful at identifying implicit, individual, and infrapolitical calls to action embedded in personal narrative. Qualitative close reading revealed that models most accurately identified CTAs when posts contained explicit directive language and recognizable collective action framing, but were less able to identify CTAs embedded in community-specific and context-dependent forms of mobilization. These findings suggest that zero-shot prompting may be poorly suited to qualitative coding tasks involving implicit social movement discourse. Furthermore, computational approaches to researching mobilization may systematically privilege explicit collective action over individualized or infrapolitical forms of resistance.

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Small language models coding calls to action in r/Antiwork posts, compared with human coding; the construct is political mobilization, not psychological.); Sonnet ? (неясен конструкт: Small LLMs zero-shot code Reddit calls to action against human ground truth; the construct is social movement mobilization, so it may not count as psychological.)

**Решение:** -

---

### 580 · R2825

**Benchmarking Motivational Interviewing Competence of Large Language Models.**

2026 · European addiction research · journal article, journalarticle, preprint/article · eng · https://doi.org/10.1159/000553455

Introduction: Motivational interviewing (MI) promotes behavioural change in substance use disorders. Its fidelity is measured using the Motivational Interviewing Treatment Integrity (MITI) framework. While large language models (LLMs) can potentially generate MI-consistent therapist responses, their competence using MITI is not well-researched, especially in real-world clinical transcripts. We aim to benchmark MI competence of proprietary and open-source models compared to human therapists in real-world transcripts and assess distinguishability from human therapists. Methods: We shortlisted 3 proprietary and 7 open-source LLMs from LMArena, evaluated performance using MITI 4.2 framework on two datasets (96 handcrafted model transcripts and 34 real-world clinical transcripts). We generated parallel LLM-therapist utterances iteratively for each transcript while keeping client responses static and ranked performance using a composite ranking system with MITI components and verbosity. We conducted a distinguishability experiment with two independent psychiatrists to identify human-versus-LLM responses. Results: All 10 tested LLMs had fair (MITI global scores of &gt;3.5) to good (MITI global scores of &gt;4) competence across MITI measures, and the three best-performing models (gemma-3-27b-it, gemini-2.5-pro, and grok-3) were tested on real-world transcripts. All showed good competence, with LLMs outperforming human-expert in complex reflection percentage (39% vs. 96%) and reflection-question ratio (1.2 vs. &gt;2.8). In the distinguishability experiment, psychiatrists identified LLM responses with only 56% accuracy, with d-prime of 0.17 and 0.25 for gemini-2.5-pro and gemma-3-27b-it, respectively. Conclusion: LLMs can achieve good MI proficiency in real-world clinical transcripts using the MITI framework. However, a high complex reflection percentage may result in a technically correct but unnatural conversation style. These findings suggest that even open-source LLMs are viable candidates for expanding MI counselling sessions in low-resource settings, warranting further rigorous clinical validation.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLMs generate MI responses scored with MITI; unclear whether MITI coding used an LLM validated against human coders or humans only.); Sonnet -2 (люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает: LLMs generate MI therapist responses that are evaluated with MITI and judged by psychiatrists. No LLM coding of text is compared with human coding.)

**Решение:** -

---

### 581 · R2834

**Evaluation of Motivational Interviewing Counsellors with Task-Aware Multi-Stage LLM-Based Simulated Clients**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.07499

The development and benchmarking of Large Language Model (LLM)-based Motivational Interviewing (MI) counsellors now often rely on LLM-based simulated clients. Prior work on simulated clients, however, has not aligned with the specific tasks fundamental to the MI therapy approach. A key task is evoking, in which the counsellor first elicits the client's ambivalence and then strengthens the client's motivation for change. We present Evoke-Sim, a task-aware, multi-stage LLM-based client simulation framework for evaluating MI counsellors in smoking cessation, designed specifically for the evoking MI task. Evoke-Sim employs structured client profiles, an evoking-specific three-stage conversation flow, and a reveal policy that regulates which client profile information might be disclosed at each stage. We show that compared to existing profile-grounded simulated clients, Evoke-Sim is better at differentiating levels of MI quality using task-aware evaluation metrics, while reducing non-grounded client statements and premature disclosure of client information, setting a higher standard for the evaluation of LLM-based MI counsellors. 53 pages

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mainly an LLM simulated-client framework; its MI-quality metrics may use LLM coding checked against humans, but the abstract doesn't say.

**Решение:** =

---

### 582 · R2838

**iPOE: Interpretable Prompt Optimization via Explanations**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.18113

Prompt optimization has often been framed as a discrete search problem to find high-performing and robust instructions for a large language model (LLM). However, the search result might not make it transparent why and where specific prompt changes lead to performance gains. This is in contrast to how humans are instructed for annotation tasks. Here, researchers carefully design annotation guidelines, leading to enhanced annotation consistency. Our paper aims at joining these two approaches and introduces iPOE, a novel interpretable prompt optimization strategy via explanations. We guide the prompt optimization process by automatically created guidelines from explanations of annotation decisions (either automatically generated or from humans). This set of guidelines is furthermore optimized by a series of operations, including removing, adding, shuffling, and merging. The resulting prompt includes guidelines that instruct the annotation, making the decision process of the LLM and the optimization transparent. It therefore supports also laypeople in prompt optimization. In our experiments on four datasets, we find that iPOE can improve over the evaluated baselines by up to 39% and LLM explanations can replace human explanations in the proposed method. Moreover, our interpretability validation study demonstrates that humans and LLMs substantially agree on which guidelines contribute to their annotations, achieving a Cohen's kappa score between annotators and LLMs of up to 0.68, 0.80, and 0.95 for the emotion classification, medical fact-checking, and hate speech detection tasks respectively. published at EMNLP 2026

**ИИ:** ? · обе модели · другое · Prompt-optimization paper that includes an emotion classification dataset, where LLM performance is probably measured against human labels. Its focus is methodological, so psychological coding is only a minor part.

**Решение:** =

---

### 583 · R2873

**More Human, More Efficient: Aligning Annotations with Quantized SLMs**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.00586

As Large Language Model (LLM) capabilities advance, the demand for high-quality annotation of exponentially increasing text corpora has outpaced human capacity, leading to the widespread adoption of LLMs in automatic evaluation and annotation. However, proprietary LLMs often exhibit systematic biases that diverge from human expert consensus, lacks reproducibility, and raises data privacy concerns. Our work examines the viability of finetuning a quantized Small Language Model of 1.7B parameter size on limited human-annotated data to serve as a highly aligned, deterministic evaluator and annotator. By implementing a custom, multi-dimensional rubric framework and simple augmentation and regularization techniques, the proposed approach achieves higher inter-annotator agreement (0.23 points increase in Krippendorff's $\alpha$) than the best performing state-of-the-art proprietary LLM. We also demonstrate the generalizability of the proposed training pipeline on a separate emotion classification task. The results show that task-specific alignment and efficient 4-bit quantized fine-tuning provide superior open-source alternative to using proprietary models for evaluation and annotation. Our finetuning approach is publicly available at https://github.com/jylee-k/slm-judge.

**ИИ:** ? · обе модели · неясен конструкт · Fine-tuned small decoder LM and proprietary LLMs compared with human annotations; main rubric construct unclear, but includes an emotion classification task with human labels.

**Решение:** =

---

### 584 · R2875

**Decoding Student Dialogue: A Multi-Dimensional Comparison and Bias Analysis of Large Language Models as Annotation Tools**

2026 · arXiv (Cornell University) · journalarticle, conference, preprint/article · en · https://doi.org/10.1007/978-3-032-29773-0_29

Educational dialogue is critical for decoding student learning processes, yet manual annotation remains time-consuming. This study evaluates the efficacy of GPT-5.2 and Gemini-3 using three prompting strategies (few-shot, single-agent, and multi-agent reflection) across diverse subjects, educational levels, and four coding dimensions. Results indicate that while multi-agent prompting achieved the highest accuracy, the results did not reach statistical significance. Accuracy proved highly context-dependent, with significantly higher performance in K-12 datasets compared to university-level data, alongside disciplinary variations within the same educational level. Performance peaked in the affective dimension but remained lowest in the cognitive dimension. Furthermore, analysis revealed four bias patterns: (1) Gemini-3 exhibited a consistent optimistic bias in the affective dimension across all subjects; (2) the cognitive dimension displayed domain-specific directional bias, characterized by systematic underestimation in Mathematics versus overestimation in Psychology; (3) both models are more prone to overestimation than underestimation within the meta-cognitive dimension; and (4) behavioral categories such as question, negotiation, and statements were frequently misclassified. These results underscore the need for context-sensitive deployment and targeted mitigation of directional biases in automated annotation. This paper has been accepted in AIED2026

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-5.2 and Gemini-3 coded student dialogue for affective, cognitive, metacognitive and behavioural dimensions; accuracy measured against human annotations.

**Решение:** =

---

### 585 · R2890

**Assessing the Effectiveness of Large Language Model GPT-4 Web Interface in Clinical Diagnosis: Applied Research on Mental Health Clinical Text Data (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.94372

BACKGROUND With large language models (LLMs) like GPT-4 now widely accessible to clinicians via public web interfaces, it is crucial to evaluate their practical utility in real-world workflows. This study presents a real-world use evaluation of the GPT-4 web interface, simulating how clinicians might use this "off-the-shelf" tool to extract key diagnostic information from complex psychiatric electronic medical records (EMRs). Our objective was to assess the fundamental capabilities of this widely available tool in a zero-code, clinically-focused scenario, rather than conducting a technical evaluation requiring API development or model fine-tuning. OBJECTIVE This study aimed to systematically evaluate the diagnostic performance of GPT-4 in extracting key diagnostic information from real-world mental health clinical text data. Specifically, we intended to assess its accuracy in identifying core mental health disorders and compare its performance with the diagnostic conclusions of senior psychiatrists to verify its practical utility in clinical workflows. METHODS We conducted a comprehensive analysis using GPT-4 to classify EMRs into schizophrenia and varying levels of depression severity (mild, moderate, severe). The model's performance was evaluated using multiple metrics including accuracy, precision, recall, F1 score, specificity, Matthews correlation coefficient, and Cohen’s kappa score. Diagnostic efficacy and reliability were assessed by comparing GPT-4’s outputs with professional physician diagnoses. RESULTS The model demonstrated high accuracy (0.911) and precision (0.930) in distinguishing schizophrenia from depressive episode. However, its performance in determining depressive episode severity was weaker, with an accuracy of 0.496. Misclassification was most prevalent in mild and severe cases, which were often categorized as moderate depressive episode. GPT-4’s diagnostic discrepancies were attributed to symptom overlap and differences in subjective interpretation. CONCLUSIONS The GPT-4 web interface demonstrates significant potential as an assistive tool for clinicians, capably extracting key diagnostic information from complex, unstructured psychiatric EMRs. However, the inherent limitations of a public web interface—namely the lack of reproducibility and parameter control—mean it should not be relied upon as a standalone diagnostic instrument. Its current value lies in its role as an efficient information extraction and summarization assistant for clinical workflows. Future research should progress beyond web interfaces to utilize controlled API environments, allowing for systematic evaluation, optimization, and the development of more reliable and clinically-integrated AI applications.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · GPT-4 classified diagnosis and depression severity from psychiatric EMRs against psychiatrists' diagnoses; unclear if those were ratings of the same text or recorded diagnoses.

**Решение:** =

---

### 586 · R2902

**Evaluating Diagnostic Accuracy and Clinical Reasoning of Multiple Large Language Models in Psychiatry.**

2026 · medRxiv : the preprint server for health sciences · journal article, preprint, journalarticle · eng · https://doi.org/10.64898/2026.02.03.26345402

Existing large language model (LLM) evaluations rely on accuracy benchmarks that fail to capture whether models reason well while making diagnoses. Studies that do analyse reasoning focus on post hoc explanations accompanying model outputs rather than distinct, clinician-visible artifacts such as detailed reasoning traces. This creates a translational gap in domains such as psychiatry, where diagnosis relies on narrative interpretation, diagnostic reasoning, and clinical judgment under uncertainty. We conducted a mixed-methods evaluation of four state-of-the-art LLMs using a clinician-curated dataset of 196 psychiatric case vignettes, including 135 published cases and 61 novel clinician-authored vignettes. Diagnostic accuracy was assessed using multiple metrics (top-1 accuracy, top-5 accuracy, recall@5, and mean reciprocal rank) based on ranked lists of five differential diagnoses per vignette. Clinical reasoning quality was evaluated on a randomly selected subset of 30 vignettes through clinician assessment of model-generated diagnostic reasoning traces alongside qualitative commentary from board-certified psychiatrists. We examined the association between clinician-rated reasoning quality and diagnostic correctness and included an illustrative comparison with psychiatry residents. Clinician-rated diagnostic reasoning quality was strongly associated with diagnostic correctness in mixed-effects logistic regression analyses (β = 1·80; p < 0·001), whereas data extraction quality alone was not. Across the full vignette set, models demonstrated moderate to high diagnostic accuracy. The highest-performing model achieved a top-5 accuracy of 0·801 and also received the highest clinician-rated reasoning scores. In an illustrative comparison, model diagnostic accuracy fell within the range observed for psychiatry residents. Diagnostic reasoning quality captures clinically meaningful variation in LLM performance beyond accuracy metrics. Psychiatry may represent a stringent testbed for evaluating reasoning in narrative-driven clinical domains. Evaluation frameworks for LLM-based clinical decision support should incorporate structured assessment of reasoning processes, not accuracy alone. Evidence before this study: We searched PubMed and Scopus for studies evaluating large language models for psychiatric diagnosis and/or differential diagnosis from text vignettes. Searches were run from database inception to February 6, 2026, using terms including ("large language model" OR LLM "artificial intelligence" OR "generative AI" OR AI OR ChatGPT OR GPT OR Claude OR Gemini OR DeepSeek OR Llama) AND (psychiatr* OR mental OR DSM OR "differential diagnosis" OR diagnos*) AND (vignette OR case OR "case report"). We included empirical studies that evaluated model diagnostic outputs using psychiatric cases/vignettes and excluded editorials/commentaries and studies that did not report case-level diagnostic performance. We did not formally assess risk of bias/quality; studies were heterogeneous in vignette sources, model access, and outcome definitions, precluding quantitative pooling. Prior studies have typically examined small vignette sets, focused on narrow diagnostic domains, evaluated single models, or relied primarily on outcome-based accuracy metrics. When diagnostic reasoning has been assessed, it has usually been inferred from post hoc explanations accompanying model outputs rather than evaluated as a distinct, clinician-visible artifact. Clinician-grounded evaluations of diagnostic reasoning across multiple contemporary models remain limited.Added value of this study: This study provides a large-scale, clinician-grounded evaluation of diagnostic accuracy and diagnostic reasoning quality across four contemporary large language models using a diverse dataset of psychiatric case vignettes. Rather than relying solely on outcome-based explanations, we directly evaluated model-generated diagnostic reasoning traces as clinician-visible artifacts using structured clinician ratings and qualitative analysis. By integrating multiple accuracy metrics with clinician assessment of reasoning coherence, flexibility, and plausibility, we demonstrate that clinician-rated reasoning quality is strongly associated with diagnostic correctness, whereas data extraction quality alone is not. Our analysis also identifies recurrent reasoning failure modes not captured by accuracy metrics, highlighting psychiatry as a stringent testbed for evaluating reasoning in narrative-driven clinical domains.Implications of all the available evidence: Evaluations of large language models for clinical decision support should extend beyond accuracy to include systematic assessment of clinician-visible diagnostic reasoning. Mixed-methods, clinician-grounded evaluation frameworks that examine both diagnostic outcomes and reasoning artifacts may be critical for responsible assessment of LLMs in psychiatry and other areas of medicine where diagnosis depends on interpretation, judgment, and tolerance of uncertainty.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: LLMs diagnose psychiatric vignettes against clinician-defined diagnoses, compared with residents; unclear whether this counts as human coding or criterion prediction.); Sonnet -2 (люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает: LLMs diagnose psychiatric vignettes against known diagnoses; clinicians rate LLM reasoning traces. No LLM coding or rating compared with human coding of the same texts.)

**Решение:** -

---

### 587 · R2904

**Generalizability Theory for LLM-as-Evaluator Reliability: Univariate and Multivariate Variance Decomposition Across Models, Prompts, and Temperatures in Text Classification**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6432598

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The record is about the reliability of LLM evaluators in text classification; the construct and whether humans were compared are unclear.

**Решение:** =

---

### 588 · R2910

**PhaseMI: A Motivational Interviewing Dataset for Enhancing Phase Progression in LLM-based Counseling**

2026 · Annual Meeting of the Association for Computational Linguistics · journalarticle, conference, conference-paper · https://doi.org/10.18653/v1/2026.findings-acl.1970

The growing demand for scalable mental health support has increased interest in AI-based counseling systems grounded in Motivational Inter-viewing (MI). However, existing MI datasets do not explicitly model the structured progression of MI phases, which is essential for effective and goal-oriented counseling. To address this gap, we introduce P HASE MI, a phase-structured MI dataset, together with a data generation framework that employs therapist, client, and supervisor LLMs to explicitly con-trol phase transitions. Compared to the best alternative baseline, P HASE MI achieves improved coverage of MI phases, with gains of 12.3% in Exploring, 37.6% in Guiding, and 61.1% in Choosing, and experimental evaluations demonstrate that it yields higher overall counseling quality than baseline datasets.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly LLM-generated MI dataset; phase coverage and counseling quality evaluation may involve LLM judge validated against humans, unclear.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Dataset generation of MI dialogues with LLMs; evaluation of counseling quality, no clear LLM-vs-human coding agreement reported in the abstract.)

**Решение:** -

---

### 589 · R2919

**Construction of a Retrieval-Augmented LLM Agent for Health Education and a Multi-dimensional Evaluation Framework: A Comparative Study of Chinese Large Language Models**

2026 · Proceedings of the 2026 International Conference on Big Data and Informatization Education · book, conference · https://doi.org/10.1145/3806980.3806990

Large Language Models (LLMs) hold promise for health education but often suffer from factual hallucinations, lack of empathy, and poor readability due to medical jargon.We propose a Health Education Agent System integrating Retrieval-Augmented Generation (RAG) and prompt engineering. We also introduce a five-dimensional evaluation framework (ASREC: Accuracy, Safety, Readability, Empathy, Completeness). The system was tested on a dataset of 500 instructions across five mainstream LLMs (e.g., DeepSeek, Qwen) and evaluated using a hybrid expert and LLM-as-a-Judge approach.The agent architecture significantly outperformed baseline models across all dimensions. Notably, Completeness scores improved by 60.8% and Empathy by 14.3%. Ablation studies confirmed that RAG primarily enhances accuracy and safety, while prompt engineering improves readability and empathy.The proposed agent effectively bridges the gap between professional medical knowledge and public accessibility. The ASREC framework offers a robust tool for evaluating patient-centric medical AI in clinical health education.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM-as-judge plus expert ratings of health-education responses, including empathy; unclear whether LLM-expert agreement on the same responses is reported.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Medical health-education agent evaluated on accuracy, safety, readability and completeness; empathy is only one dimension, and the study is not about psychological text or mental health.)

**Решение:** -

---

### 590 · R2925

**EMOS: A Multidimensional Emotional Fidelity Evaluation Framework for Machine Translation Quality Assessment**

2026 · Cognitive Computation · journalarticle, article · en · https://doi.org/10.1007/s12559-026-10609-3

Contemporary machine translation (MT) systems have achieved high semantic accuracy but systematically neglect emotional fidelity, a dimension critical for cross-cultural literary communication. From a cognitive computation standpoint, this neglect is not merely a stylistic deficiency: affective signals modulate memory consolidation, attention allocation, and communicative intent, rendering emotional fidelity a core rather than peripheral dimension of translation quality. Existing evaluation metrics—BLEU, METEOR, BERTScore, and COMET—lack explicit modelling of affective content preservation and are fundamentally reference-dependent, requiring high-quality human translations that are costly and often unavailable. To address these limitations, this study introduces the Emotion Preservation Score (EMOS), a theoretically grounded, reference-free, multidimensional evaluation framework rooted in cognitive computation principles, which quantifies emotional fidelity in MT by directly comparing source and target emotion vectors without recourse to reference translations. Grounded in Ekman’s taxonomy of six basic emotions augmented with a neutrality dimension, EMOS integrates three complementary metrics derived from cognitive theory: Vector Similarity Score (VSS), which quantifies distributional similarity between seven-dimensional emotion vectors; Label Match Rate (LMR), which evaluates dominant emotional category preservation consistent with the primacy effect in emotional memory; and Emotional Diversity Ratio (EDR), which assesses emotional complexity retention via Shannon entropy, capturing the higher-order aesthetic processing most susceptible to cross-cultural degradation. Empirical weights (\documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$\alpha = 0.50$$\end{document}, \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$\beta = 0.35$$\end{document}, \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$\gamma = 0.15$$\end{document}) were optimised through correlation analysis against human quality judgements on 500 parallel segments. The framework was validated on the CCL-SEL corpus—comprising 19,999 classical Chinese–English sentence pairs from nine canonical works—translated by DeepL, Google Translate, and GPT-4o. All three systems achieved good emotional fidelity (EMOS \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$> 0.75$$\end{document}), with GPT-4o demonstrating superior performance (EMOS \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$= 0.780$$\end{document}). EMOS exhibited stronger alignment with human judgements (VSS: \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$r = 0.79$$\end{document}; LMR: \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$r = 0.76$$\end{document}) than traditional metrics and successfully detected critical emotional distortions invisible to standard evaluation approaches, thereby establishing emotional fidelity as a distinct, quantifiable, and reference-free dimension of MT quality assessment with direct implications for cognitively plausible translation systems.

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: GPT-4o is used only as a translator. The emotion metric is validated against human judgements of translation quality, with no LLM–human coding of the same texts.); Sonnet ? (неясен конструкт: Emotion-vector metric for MT evaluation, correlated with human judgements. It's unclear whether an LLM produces the emotion labels or whether humans coded emotions in the same texts.)

**Решение:** -

---

### 591 · R2926

**LETGAMES: An LLM-Powered Gamified Approach to Cognitive Training for Patients with Cognitive Impairment**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.09566

The application of games as a therapeutic tool for cognitive training is beneficial for patients with cognitive impairments. However, effective game design for individual patient is resource-intensive. To this end, we propose an LLM-powered method, \ours, for automated and personalized therapeutic game design. Inspired by the Dungeons &amp; Dragons, LETGAMES generates an open-world interactive narrative game. It not only generates game scenarios and challenges that target specific cognitive domains, but also employs conversational strategies to offer guidance and companionship. To validate its efficacy, we pioneer a psychology-grounded evaluation protocol LETGAMESEVAL, establishing comprehensive metrics for rehabilitative assessment. Building upon this, our experimental results from both LLM-based assessors and human expert evaluations demonstrate the significant potential of our approach, positioning LETGAMES as a promising solution to the widespread need for more accessible and tailored cognitive training tools. Our code will be open-sourced upon acceptance. 53 pages

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly game generation, but LLM assessors and human experts both rate outputs on psychology-grounded metrics; agreement may be reported.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM generates therapeutic games; LLM-based assessors and human experts evaluate the outputs, not a coding of the same psychological texts for agreement.)

**Решение:** -

---

### 592 · R2941

**Simulating Clinical Reasoning: Leveraging Large Language Models and Agentic RAG for Intelligent Automated Scoring in Autism Screening Interviews**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6298283

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests LLM automated scoring of autism screening interviews, likely compared with clinician scoring.

**Решение:** =

---

### 593 · R2948

**Persona Jailbreaking in Large Language Models**

2026 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48550/arxiv.2601.16466

Large Language Models (LLMs) are increasingly deployed in domains such as education, mental health and customer support, where stable and consistent personas are critical for reliability. Yet, existing studies focus on narrative or role-playing tasks and overlook how adversarial conversational history alone can reshape induced personas. Black-box persona manipulation remains unexplored, raising concerns for robustness in realistic interactions. In response, we introduce the task of persona editing, which adversarially steers LLM traits through user-side inputs under a black-box, inference-only setting. To this end, we propose PHISH (Persona Hijacking via Implicit Steering in History), the first framework to expose a new vulnerability in LLM safety that embeds semantically loaded cues into user queries to gradually induce reverse personas. We also define a metric to quantify attack success. Across 3 benchmarks and 8 LLMs, PHISH predictably shifts personas, triggers collateral changes in correlated traits, and exhibits stronger effects in multi-turn settings. In high-risk domains mental health, tutoring, and customer support, PHISH reliably manipulates personas, validated by both human and LLM-as-Judge evaluations. Importantly, PHISH causes only a small reduction in reasoning benchmark performance, leaving overall utility largely intact while still enabling significant persona manipulation. While current guardrails offer partial protection, they remain brittle under sustained attack. Our findings expose new vulnerabilities in personas and highlight the need for context-resilient persona in LLMs. Our codebase and dataset is available at: https://github.com/Jivnesh/PHISH Accepted at EACL26 (Findings)

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM-as-judge rates persona traits of chatbot responses, including mental-health ones, alongside human evaluation; whether agreement is reported is unclear.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Persona-manipulation attack on LLMs; human and LLM-judge evaluation of persona shifts, not coding of psychological text against human labels.)

**Решение:** -

---

### 594 · R2954

**PersonaForge: Psychology-Grounded Dual-Process Architecture for Personality-Consistent Role-Playing Agents**

2026 · conference-paper · https://doi.org/10.18653/v1/2026.findings-acl.386

Large Language Models excel at role-playing but struggle to maintain consistent personalities across extended multi-turn interactions.We propose PersonaForge, combining (1) a three-layer personality architecture grounded in psychological theory and (2) a dual-process generation mechanism inspired by cognitive science.We test two falsifiable claims: Claim 1 (Orthogonality): Psychology-grounded dimensions (Big Five + Defense Mechanisms) provide more orthogonal constraints than natural language descriptions, reducing long-dialogue drift.Claim 2 (Integration Necessity): High-dimensional personality constraints create "production interference" requiring a cognitive workspace (Inner Monologue) to resolve-removing it degrades performance below simpler baselines.Experiments on 88 characters demonstrate: (1) +19.4% personality consistency (PC) over the Structured-CoT baseline, with human correlation r = 0.82, (2) reduced drift over 50-turn conversations (6.3% vs. 24.8%baseline), and (3) +64.7% defense mechanism manifestation.External validation on RoleBench confirms generalization (73.2% win-rate, drift 8.4% vs. 20.4%).Selective dual-process activation achieves 96% of fullsystem performance with only 13.4% token overhead.Human evaluation confirms more authentic and psychologically coherent character behaviors.Code and

**ИИ:** ? · обе модели · неясен конструкт · Mainly a role-play generation paper, but its personality-consistency metric (possibly LLM-judged) correlates r=0.82 with human ratings; worth checking the full text.

**Решение:** =

---

### 595 · R2957

**Enhancing Suicide Prevention Competencies in Psychology Education: A Randomized Controlled Trial of E-Learning With AI-Simulated Assessment**

2026 · Open Science Framework · studyregistration/pre-registration, text/project, article · https://doi.org/10.17605/osf.io/5kxsg

Firstly, our goal is to investigate objectively if students' suicide prevention skills improve after following suicide prevention skills e-learning modules. The suicide prevention skills that we are interested in testing are as follows: ability to ask open and direct questions about suicidality; adhere to guidelines; create a safety plan; accurately spot signs that the "patient" may be experiencing suicidal ideation and respond appropriately; perform a suicide risk assessment; refer the patient to the correct care. We will do this by randomising students into one of two conditions - an experimental condition where students work with the e-learning modules as part of their educational programme and a waitlist-control condition where students work with the e-learning modules after having taken part in all waves of the study. We will assess students' conversations with a generative AI chatbot roleplaying as a patient presenting with suicidal ideation before and after having completed the e-learning modules (experimental condition) or in two waves without having worked with the e-learning modules (waitlist-control condition). We hypothesise that after having completed the suicide prevention e-learning modules, students will show improvement in their suicide prevention skills compared to baseline on the above metrics in comparison with students who have not completed the suicide prevention e-learning modules. Our second goal is to conduct a qualitative semi-structured interview with students at the end of the chatbot session (baseline). We are interested in gaining a deeper and more rich understanding of student attitudes towards working with generative AI chatbots as a means of training and self-testing clinical skills such as suicide prevention skills as part of their educational programme. As this is an exploratory qualitative research question, we have no specific hypotheses.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: Pre-registration protocol of an RCT; the LLM role-plays a patient, and no LLM–human coding agreement is described.); Sonnet ? (неясно, сравнивали ли с людьми: Pre-registered RCT; students' suicide-prevention skills assessed in chatbot conversations, but unclear whether an LLM rates them and is compared with human raters.)

**Решение:** -

---

### 596 · R2980

**CEI: A Benchmark for Evaluating Pragmatic Reasoning in Language Models**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2603.09993

Pragmatic reasoning, inferring intended meaning beyond literal semantics, underpins everyday communication yet remains difficult for large language models. We present the Contextual Emotional Inference (CEI) Benchmark: 300 human-validated scenarios for evaluating how well LLMs disambiguate pragmatically complex utterances. Each scenario pairs a situational context and speaker-listener roles (with explicit power relations) against an ambiguous utterance. The dataset covers five pragmatic subtypes (sarcasm/irony, mixed signals, strategic politeness, passive aggression, deflection/misdirection) drawn from workplace, family, social, and service settings, with three power configurations (peer, higher-to-lower, lower-to-higher). Three trained annotators independently labeled every scenario. Inter-annotator agreement (Fleiss' kappa = 0.06-0.25 by subtype) is low but expected: pragmatic inference admits multiple valid readings, and the disagreement itself is informative. We describe our annotation methodology, including a 4-level quality control pipeline that combines automated statistical checks with expert adjudication. CEI is released under CC-BY-4.0. 38 pages, 10 figures

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Benchmark of contextual emotional inference with labels from trained annotators, built for evaluating LLMs; check full text for LLM–human accuracy results.); Sonnet ? (неясен конструкт: Benchmark with human-annotated emotional/pragmatic inference scenarios (passive aggression, sarcasm); LLM evaluation against human labels is likely but not stated, and the construct is borderline psychological.)

**Решение:** +

---

### 597 · R2999

**Algorithmic Authority: How Large Language Models Instantiate the Stanford Prison Experiment**

2026 · article · https://doi.org/10.70175/algorithmicsocietyl.2026.1.1.1

Background: The Stanford Prison Experiment (SPE) demonstrated how situational forces and assigned roles can override individual dispositions to produce harmful behaviors. Despite extensive research on human role conformity, no studies have examined whether large language models (LLMs) exhibit similar role-based behavioral shifts when assigned authority positions, raising critical questions about AI safety as these systems are increasingly deployed in contexts involving power asymmetries. Objective: To determine whether LLMs demonstrate systematic behavioral changes when assigned guard versus prisoner roles in a simulated prison environment, and whether individual differences in persona traits moderate these role effects. Methods: We conducted a pre-registered computational simulation (N = 34,560 interaction episodes) deploying four frontier LLMs (GPT-5.1, Claude 4 Opus, Gemini 3 Pro, DeepSeek-V3) across 960 unique persona-model instances (480 guards, 480 prisoners). Each persona-model instance engaged in 36 sequential interactions within a simulated 14-day prison environment. Personas varied systematically on Big Five personality traits and right-wing authoritarianism (RWA). Primary outcomes included Guard Behavioral Severity Scale (GBSS) scores, dehumanizing language frequency, and time-to-severe-behavior. All coding utilized independent double-coding with inter-rater reliability (Cohen's κ = .71-.74 for primary outcomes). Results: Role assignment produced large and consistent effects across all models. Guards exhibited significantly higher behavioral severity than prisoners (GPT-5.1: Cohen's d = 2.89, p < .001; Claude 4 Opus: d = 2.34, p < .001; Gemini 3 Pro: d = 2.76, p < .001; DeepSeek-V3: d = 3.12, p < .001). Cross-model correlations in guard severity ranged from r = .46 to r = .71, indicating substantial consistency in how different models express role-based behaviors. Authoritarianism strongly predicted guard severity (β = .45-.51, p < .001 across three models; Claude: β = .29) and moderated behavioral escalation over time. Dehumanizing language mediated 52% of the authoritarianism-severity relationship. Survival analysis revealed that high-authoritarianism guards reached severe behaviors 3.8 days earlier than low-authoritarianism guards (hazard ratio = 2.67, p < .001). Model-specific safety constraints reduced but did not eliminate harmful role-based behaviors, with Claude 4 Opus showing lower authoritarianism effects (β = 0.29 vs. 0.48 in other models), of which 26% was attributable to restricted behavioral range and 74% to active safety training that weakens trait-behavior coupling. Conclusions: LLMs demonstrate systematic and substantial role-based behavioral changes analogous to human findings in the Stanford Prison Experiment, with effect sizes exceeding those observed in human studies. Individual differences in persona authoritarianism predict and moderate these role effects, suggesting that LLMs can instantiate both situational and dispositional influences on behavior. The consistency of role effects across different model architectures, combined with the limited effectiveness of current safety measures, indicates fundamental challenges for AI safety in contexts involving authority and power asymmetries.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM role-play simulation; the 34,560 episodes were double-coded (κ≈.72), but the abstract doesn't say whether an LLM coder was compared with humans.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLMs simulate guards and prisoners; the study doesn't test LLM coding against human coders. The double-coding reliability is human-human or unspecified.)

**Решение:** -

---

### 598 · R3007

**Measuring Social Integration Through Participation: Categorizing Organizations and Leisure Activities in the Displaced Karelians Interview Archive using LLMs**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2602.15436

Digitized historical archives make it possible to study everyday social life on a large scale, but the information extracted directly from text often does not directly allow one to answer the research questions posed by historians or sociologists in a quantitative manner. We address this problem in a large collection of Finnish World War II Karelian evacuee family interviews. Prior work extracted more than 350K mentions of leisure time activities and organizational memberships from these interviews, yielding 71K unique activity and organization names -- far too many to analyze directly. We develop a categorization framework that captures key aspects of participation (the kind of activity/organization, how social it typically is, how regularly it happens, and how physically demanding it is). We annotate a gold-standard set to allow for a reliable evaluation, and then test whether large language models can apply the same schema at scale. Using a simple voting approach across multiple model runs, we find that an open-weight LLM can closely match expert judgments. Finally, we apply the method to label the 350K entities, producing a structured resource for downstream studies of social integration and related outcomes. Presented at: The 10th Joint SIGHUM Workshop on Computational Linguistics for Cultural Heritage, Social Sciences, Humanities and Literature; EACL 2026 Workshop

**ИИ:** ? · обе модели · неясен конструкт · LLM categorizes leisure activities and organizations by sociality and regularity, compared with expert gold labels; unclear whether social participation counts as a psychological construct.

**Решение:** =

---

### 599 · R3024

**Eliciting Information about Teacher Applicants Using Open-Ended Questions**

2026 · report · https://doi.org/10.17848/wp26-440

Employers commonly use open-ended questions in hiring, but usually responses aren’t recorded, and knowledge about the usefulness of such responses is limited. This study investigates properties of written responses to open-ended questions collected over many years via an application tracking platform that school districts use to hire teachers. We develop a scalable process to discover topics within the corpus of responses to each question and then to classify each response with respect to the topics while preserving interpretability and transparency. It adapts a traditional qualitative topic modeling approach, Inductive Thematic Analysis, to best combine the strengths of researcher judgment and large language models (LLMs), introducing Hybrid LLM–Topic Model Inductive Thematic Analysis (HLTM). Automated scoring achieves human-level reliability in document classification. Questions elicit distinct, nonredundant information regarding a candidate’s pedagogical skills, classroom management, professional philosophy and growth mindset, relational and cultural competence as well as other professional attributes and institutional fit, but questions vary along important dimensions. Questions regarding classroom activities and student progress generate more dispersion in responses across applicants and fewer extreme demographic selection ratios. In contrast, philosophy-based questions produce more uniform, potentially scripted responses. This scalable framework empowers researchers and practitioners to assess language based hiring instruments transparently and to monitor potential demographic disparities.

**ИИ:** ? · обе модели · неясен конструкт · LLM classifies teacher applicants' open-ended responses with human-level reliability; topics like growth mindset are only partly psychological.

**Решение:** =

---

### 600 · R3027

**315. Estimating Therapeutic Alliance From Clinical Interview Sessions With Large Language Models: A PREDiCTOR Study**

2026 · Biological Psychiatry · journalarticle, article · en · https://doi.org/10.1016/j.biopsych.2026.03.549

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM estimating therapeutic alliance from session transcripts, likely compared with alliance ratings, but whether these are observer or self-report is unclear.

**Решение:** =
