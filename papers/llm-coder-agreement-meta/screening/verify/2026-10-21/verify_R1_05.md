# Проверка с метками ИИ, часть 5

Записи 601–750 из 1304, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

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

### 601 · R3066

**An LLM-Native Psychometric Instrument Reveals a Self-Report--Behavior Gap Across 25 Models**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.09843

Do large language models'(LLMs') answers to self-report questionnaires predict how they behave? Prior work finds they do not, but it uses human personality inventories, so the gap could reflect borrowed human constructs rather than LLM self-report itself. We test this with a self-report instrument built from LLM-specific behaviors (e.g., over-refusal, unsolicited disclaimers) whose structure is derived bottom-up. Administering 300 items 30 times to 25 LLMs from 17 developers yields five replicable, reliable factors (Tucker $\phi \geq .957$, $\alpha \geq .930$). We compare these self-reports with 2,500 open-ended behavioral samples rated by 151 humans and an LLM-judge ensemble. Humans and judges agree about model behavior ($\bar{r} = .51$), but self-report barely tracks human ratings ($\bar{r} = .09$, 95% CI $[-.07, .18]$) or rater-free text measures, and correcting for criterion unreliability leaves four of five factors near zero. Verbosity is the partial exception ($r = .40$, 71% of its reliability ceiling). On Responsiveness, self-report tracks LLM judges more than humans ($r = .53$ vs. $.18$; Steiger $p = .04$), and controlling for length and formatting does not remove this: agreement between LLM judges and LLM self-report is weak evidence that either tracks human judgment.

**ИИ:** разошлись — Opus ? (неясен конструкт: Humans and LLM judges rated the same LLM outputs (r=.51), but the constructs are LLM behaviours like verbosity and refusal, not clearly psychological.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM judges and humans rate general LLM output behaviors (verbosity, responsiveness, over-refusal), not psychological or clinical constructs in human or mental-health text.)

**Решение:** -

---

### 602 · R3082

**Human vs. machine - Evaluating GPT-4, GPT-4o and GPT-4o-mini in rating depression interviews in a convenience sample of the German population**

2026 · Computers in Human Behavior Reports · article · en · https://doi.org/10.1016/j.chbr.2026.100968

Despite high prevalence, depression often remains undetected. Artificial Intelligence (AI) screening methods may help address this gap. AI models’ proficiency in rating depression interviews in comparison with human raters has been demonstrated for clinical populations. The capacity of three Large Language Models (LLMs) for rating depression interviews was evaluated. The test dataset contained interviews from the general population to evaluate model capacity for screening. LLM ratings were compared with assessments provided by trained psychology students. GPT-4, GPT-4o and GPT-4o-mini were prompted to rate interview transcripts from N = 55 participants from a convenience sample of the German population on a depression scale. Models were used without task-specific fine-tuning. LLM performance was evaluated via intraclass correlations with trained psychology students’ assessments leveraging a scale explicitly designed to yield reliable ratings when applied by first-time raters. GPT-4 and GPT-4o achieved moderate to good interrater reliability with student raters (ICC 0.76 and 0.75) while ICC for GPT-4o-mini was moderate (0.55), with 98.88% CIs [0.38 to 0.70] indicating greater uncertainty. F1 accuracy scores ranged from 0.56 for GPT-4o-mini to 0.75 for GPT-4. The results suggest GPT-4’s and GPT-4o’s potential for scoring depression interviews from the general population, with GPT-4o meeting sensitivity and specificity values for case finding instruments. Our results require further validation with clinician raters in a larger and more diverse sample. Future research should explore fine-tuning and potential model bias. • We compared three LLMs with trained student raters scoring depression interviews • GPT-4 and GPT-4o estimations showed moderate to good reliability with trained student raters • GPT-4o-mini’s scores showed less than moderate reliability • GPT-4o met required sensitivity and specificity values for case finding instruments • The models were neither pretrained, nor fine-tuned for this task.

**ИИ:** + · обе модели · клиническая оценка · GPT-4, GPT-4o and GPT-4o-mini rated depression interview transcripts; agreement with trained psychology-student raters was reported as ICC.

**Решение:** =

---

### 603 · R3088

**Thriving under challenges – establishing individual and situational influences on eustress**

2026 · Enlighten: Theses (The University of Glasgow) · text/thesis, dissertation · en · https://doi.org/10.5525/gla.thesis.85846

Across four projects, I aimed to develop an in-depth understanding of how individuals experience eustress–the positive experience of a challenging situation. Specifically, I aimed to understand how eustress manifests in UK adults in general and in specific real-life situations. In Project 1, I performed a scoping review and deductive theory building to integrate 57 unique features of eustress from 80 articles into a Comprehensive Hierarchical construct of Eustress (CHE). According to CHE, eustress emerges from three main sources: successful goal-directed action, fulfilling momentary experiences, and positive stable qualities of the individual. In Project 2, I developed and assessed a novel eustress instrument, the Comprehensive Hierarchical Eustress Review (CHER), reflecting CHE’s content and structure. In a quantitative study (N = 260), I found that the CHE model adequately described eustress in UK adults and provided insights into its relationships with distress and wellbeing. In Project 3, I established feature profiles of 20 difficult situations that likely induce eustress. I found that as UK adults (N = 81) judged a situation as increasingly threatening and challenging, they also judged it as more difficult and effortful with a less obvious solution and less effective coping. I found that a large language model could approximate general trends in human judgments but failed to reproduce meaningful relationships in the data. In Project 4, I combined insights from the previous projects to establish predictive profiles of eustress and explored how these profiles varied across individuals and real-life situations. In a quantitative survey (N = 251), I found that eustress emerges from individual-situation interactions, is predicted by the underlying processes of the CHE model and is weakly related to adaptive stress mindsets. I discuss the implications of my research regarding eustress theory development and measurement, as well as applied implications, limitations, and future directions for eustress research. By establishing a comprehensive construct of eustress and testing it across individuals and situations, this thesis may help formalize the small but growing research field on positive stress. Eustress is a complex behavior that is shaped by individual (e.g., fulfilment coping) and situational (e.g., intrinsic difficulty) processes as well as their interactions. I suggest that this research can be used to establish who experiences eustress under what circumstances, and what strategies are most effective in fostering positive stress where desirable and applicable.

**ИИ:** ? · обе модели · другое · In Project 3 an LLM rated situation vignettes for threat and challenge, compared with lay participants' ratings; unclear if this counts as text coding or participant simulation.

**Решение:** =

---

### 604 · R3091

**Multimodal speech emotion recognition with large language models**

2026 · DR-NTU (Nanyang Technological University) · report · en

Traditional Speech Emotion Recognition (SER) models often rely on "black-box" speech encoders that lack interpretability. To address this, this report proposes an enhanced framework based on SpeechCueLLM, which discretizes numeric acoustic features into natural language descriptors to leverage the semantic reasoning of Large Language Models (LLMs). The architecture integrates the eGeMAPS acoustic parameter set with Valence, Arousal, and Dominance (VAD) dimensions to capture granular paralinguistic cues. To manage high dimensionality, a hybrid feature selection strategy using Lasso Regression and ANOVA is employed, alongside Dynamic Feature Masking (DFM) to improve environmental robustness. Evaluation across two distinct domains demonstrates state-of-the-art performance. On the IEMOCAP dataset, the framework achieved a 72.0% Macro-F1 (a 1.3% improvement over the baseline), while on the "in-the-wild" MSP-Podcast corpus, it achieved a significant 25.1% Macro-F1, representing a 6.5% absolute increase. These results outperform both self-supervised audio representation models and zero-shot multimodal LLMs. Ultimately, the framework provides a highly interpretable and justifiable reasoning pathway for complex affective states without relying on human-annotated metadata or opaque mapping processes.

**ИИ:** разошлись — Opus ? (неясен конструкт: An LLM classifies emotion against human-annotated IEMOCAP/MSP-Podcast labels, but the input is mainly acoustic features; the role of transcribed text is unclear.); Sonnet -7 (другое — напишите почему: Speech emotion recognition from acoustic features on IEMOCAP/MSP-Podcast; a model-development benchmark on audio, not LLM coding of psychological text versus human coders.)

**Решение:** -

---

### 605 · R3094

**Neuro-Symbolic Knowledge Graphs Improve Motivational Interviewing Fidelity in Clinical Artificial Intelligence Tools: Development and Simulation Study (Preprint)**

2026 · JMIR Publications Inc. · posted-content, preprint · https://doi.org/10.2196/preprints.113204

BACKGROUND Large language models (LLMs) are increasingly used in health counseling, but adherence to evidence-based approaches such as motivational interviewing (MI) is inconsistent, and their reasoning is difficult to inspect or audit. Supervised fine-tuning (SFT) trains a model to imitate expert responses but does not explicitly encode the sequential clinical decisions MI requires. Knowledge graphs (KGs), which represent clinical knowledge as explicit, inspectable rules and relationships, may offer a more transparent way to govern LLM counseling. OBJECTIVE This study aimed to develop a neuro-symbolic KG encoding MI clinical logic and to evaluate, in simulated sessions, whether KG guidance improves MI fidelity compared with a base LLM and SFT, alone and in combination. METHODS We built a 3-layer KG comprising an MI ontology (34 techniques, stages of change, and patient talk types), a deterministic rule engine (34 decision rules governing technique selection and phase progression), and 13 hard safety constraints, and integrated it into CHIA (Chatbot for HIV Prevention and Action), a preexposure prophylaxis (PrEP) counseling platform. Using a 2×2 factorial design crossing SFT (GPT-4.1 base vs fine-tuned on 2400 expert MI examples) with KG guidance (disabled vs enabled), we simulated 8-turn sessions with 20 LLM-generated patient personas (3 runs per persona per arm; 239/240 sessions completed). A blinded LLM judge (Claude Sonnet 4.5) scored Motivational Interviewing Treatment Integrity (MITI) 4.2 global scores (Empathy, Partnership, Cultivating Change Talk, and Softening Sustain Talk) and flagged premature planning. We used 2-way repeated-measures ANOVA and generalized estimating equations with false discovery rate correction, and computed linguistic metrics including lexical diversity. A blinded MI expert and a second LLM judge (Gemini 2.5 Pro) rescored a stratified subsample of 40 sessions. RESULTS The base LLM with KG guidance (Base+KG) achieved the highest mean Empathy (4.90, SD 0.30) and Partnership (4.88, SD 0.32). Compared with SFT alone, Base+KG showed higher Empathy (Cohen d=0.68, 95% CI 0.37-1.01) and Partnership (d=0.91, 95% CI 0.60-1.25). SFT had significant negative main effects on Empathy (F1,19=21.26; P&lt;.001) and Partnership (F1,19=17.39; P&lt;.001) and reduced lexical diversity (d=−1.47). The LLM judge flagged premature planning in 0/60 Base+KG sessions vs 1/60 Base, 4/59 SFT, and 6/60 SFT+KG sessions; however, the human expert identified more premature planning in every arm. Human-LLM agreement was moderate for Empathy (intraclass correlation coefficient [ICC] 0.55) and Partnership (ICC 0.42) and poor for Softening Sustain Talk, but all 3 raters produced consistent arm rankings. CONCLUSIONS In this simulation study, KG guidance applied to a base LLM yielded higher MI fidelity than SFT, which degraded relational quality. Externalizing clinical reasoning into an inspectable KG is a promising, auditable approach to governing LLM counseling, pending confirmation with human participants and larger human-rated samples.

**ИИ:** + · обе модели · LLM-судья · An LLM judge scored MITI global scores on counselling sessions, and agreement with a blinded MI expert on 40 sessions is reported as ICC.

**Решение:** =

---

### 606 · R3098

**EviDial: When Correct Depression Predictions Lack Evidence**

2026 · arXiv · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.27541

Depression dialogue benchmarks commonly assess models by comparing predicted symptom labels with clinical scale scores. However, a prediction may agree with a benchmark label even when the dialogue lacks enough evidence to justify it. We introduce EviDial, a benchmark that distinguishes label agreement from evidence-grounded assessment. EviDial comprises 382 depression dialogues from three sources and 2,744 participant-symptom cells, each classified as having absent, partial, conflicting, or sufficient evidence. Because evidence sufficiency lacks a directly observable gold standard, we derive calibrated evidence references from multiple judgments using generalizability theory, many-facet Rasch measurement, and random-effects latent class analysis. Our audit reveals that 82.8% of participant-symptom cells lack sufficient textual evidence for the corresponding symptom assessment, with substantial variation across sources. Across model families and prompting strategies, 69.2%-96.9% of predictions judged correct by benchmark labels are nonetheless unsupported by sufficient dialogue evidence. Further analyses show that strong agreement among LLM evaluators need not reflect independent evidence judgments, underscoring the need to calibrate automated reference panels. These findings demonstrate that label-based evaluation can overestimate evidence-grounded performance by conflating agreement with clinical labels and support in the observed dialogue. EviDial provides a measurement layer for separating these constructs and auditing LLM-based depression assessment more faithfully.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs rate depression symptoms from dialogues. References are clinical scale scores and evidence judgments that may come from LLMs rather than human coders.

**Решение:** =

---

### 607 · R3110

**Mapping patient-perceived physician traits from nationwide online reviews with LLMs**

2026 · npj Digital Medicine · journalarticle, review, preprint/article · en · https://doi.org/10.1038/s41746-026-03117-z

Understanding how patients perceive their physicians is essential to improving trust, communication, and satisfaction. Patients increasingly consult large language models (LLMs) to summarize physician reviews and shape provider choices, yet the national landscape of patient-perceived physician traits remains poorly characterized. We present an LLM-based pipeline that extracts ten patient-perceived physician trait scores from review text: five Big-Five-style and five patient-oriented dimensions. From one million U.S. physicians, we analyze 4.1 million reviews of 226,999 physicians. We validate the pipeline through multi-model comparison and human expert benchmarking. LLM and human-rater trait scores from reviews are consistent. Trait scores correlate strongly with review rating scores yet retain substantial independent variance. Two national-scale patterns emerge: male physicians receive higher trait scores across all traits, with the largest gap in clinical competence; specialty differences are driven by encounter context, with surgical specialties leading interpersonal qualities and psychiatry lowest. Cluster analysis identifies four physician archetypes, from "Uniform High" (33.8%, high across traits) to "Uniform Low" (22.6%, low across traits). This map of LLM-derived physician traits exposes how LLMs read the U.S. clinical workforce. Pending clinical validation, it opens future research on fairness, bias, and how LLM-mediated provider search shapes patient choice. Accepted in npj Digital Medicine

**ИИ:** разошлись — Opus + (проверка кодирования внутри исследования: An LLM scored perceived physician personality and interpersonal traits from patient reviews, checked against human expert ratings of the same reviews.); Sonnet ? (неясен конструкт: LLM scores Big-Five-style perceived physician traits from patient reviews, validated against human expert raters; unclear whether this counts as a psychological construct.)

**Решение:** +

---

### 608 · R3116

**LLMs Underperform on Classifying Anxiety and Depression Using Therapy Conversations: A First-Step Benchmark**

2026 · Applied Sciences · journalarticle, article · en · https://doi.org/10.3390/app16073388

Anxiety and depression are among the most prevalent mental health conditions worldwide. Early and accurate automated detection from naturalistic conversations (e.g., those recorded with a remote chatbot) could eventually improve screening and, in turn, access to timely care. As a first step towards this goal, we aim to evaluate the efficacy of both traditional machine learning and large language models (LLMs) in classifying anxiety and depression from psychotherapy sessions using labels derived from clinician-annotated session metadata reflecting the primary presenting psychiatric concerns. While psychotherapy transcripts do not reflect the real-world domain of remote naturalistic conversation, we conduct this analysis as an “easy” starting point towards the eventual goal of building generalizable, clinician-assistive models that can infer mental health status from unstructured, non-directive conversations captured in the home setting as part of a remote digital assessment process. LLM underperformance on a psychotherapy benchmark would indicate that LLMs are most likely not yet ready to advance towards mental health classifications in more complex and less structured contexts, such as from remote conversations with a chatbot or family member. To study whether LLMs can classify anxiety and depression from psychotherapy transcripts, we fine-tuned both established transformer models (BERT, RoBERTa, Longformer) and more recent large models (Mistral-7B), trained a Support Vector Machine using engineered features, and assessed prompting GPT chatbots. We observe that (1) all machine learning approaches perform poorly and (2) state-of-the-art models fail to improve multi-label classification performance relative to traditional machine learning methods, indicating the current limitations of using LLMs for classification of psychiatric diagnoses from unstructured patient text as of 2026.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs classify anxiety/depression in therapy transcripts against clinician-annotated session metadata; unclear if that is text coding or diagnosis labels.

**Решение:** =

---

### 609 · R3128

**A game-changer for qualitative research: artificial intelligence as an efficient tool for analyzing student conceptions about microplastics**

2026 · Frontiers in Education · journalarticle, article · en · https://doi.org/10.3389/feduc.2026.1770878

Qualitative content analysis of learners’ conceptions is due to large datasets time-consuming. This study examined the potential of a Large Language Model (LLM) to support and accelerate qualitative content analysis without compromising validity. Written responses from 180 bachelor students at two German universities to four open-ended questions on microplastics were analysed. ChatGPT was used to inductively develop categories and to assign responses. Two human expert coders conducted the same procedures for comparison purposes. The inter-rater reliability was calculated using Cohen’s kappa and two independent ChatGPT runs were performed to test consistency. The categorization system generated by ChatGPT largely corresponded to the human-developed system. The two ChatGPT runs showed highly consistent classifications, with inter-rater reliabilities of up to κ = 0.96. That exceeded both intra- and inter-rater agreement of the human coders ( κ = 0.45–0.90). Overall, our findings suggest that LLMs can support valid and reliable qualitative content analysis while substantially reducing analysis time. In this respect, the use of LLMs may represent a methodological game-changer for qualitative research, making such approaches more efficient and accessible, also for classroom teachers.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT coded open responses and was compared with human coders using kappa, but students' science conceptions may count as subject knowledge, not a psychological construct.

**Решение:** =

---

### 610 · R3150

**Comparing AI-Driven Meta-Debriefing Against Clinical Human Experts in Simulation: A Proof-of-Concept Study (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.93971

BACKGROUND Meta-debriefing involves evaluating the debriefer with an emphasis on enhancing future debriefing activities. However, assessing debriefing effectiveness presents challenges stemming from both time limitations and resource demands. OBJECTIVE The aim of this project was to develop an Artificial Intelligence (AI)-driven meta-debriefer that parallels human meta-debriefers in the context of audio transcription through objective structured assessment of debriefing (OSAD) metrics. METHODS We conducted prospective observational cohort research at the Mayo Clinic Multidisciplinary Simulation Center in Rochester, gathering 29 simulation sessions after removing task trainer and simulation activities without debriefing sessions. The debriefing sessions were recorded and evaluated by an AI-driven meta-debriefer and two experienced human raters using OSAD metrics. The primary result was the non-inferiority of the OSAD score of AI compared to human evaluation. RESULTS This study utilized a predefined non-inferiority margin of 10% (-0.40 per domain, -2.80 total score). The AI model showed comparable score to human experts for the total score (mean difference: -2.22; 95% CI: -3.05 to -1.39, noninferiority p = 0.91) while significantly underscored the Approach and Engagement of learner domains (mean difference -0.86, 95% CI:-0.97 to -0.76, noninferiority p<0.001; mean difference -0.66, 95% CI: -0.87 to -0.44, noninferiority p = 0.010). CONCLUSIONS This proof-of-concept study demonstrates the potential of LLM-based meta-debriefers. While current models overscore “Application” and underscore “Approach” and “Engagement of Learners” due to emotional nuance limitations, they represent a valuable supplementary tool, offering a roadmap to enhance clinical educators' efficiency.

**ИИ:** ? · обе модели · неясен конструкт · LLM rated simulation debriefing transcripts on OSAD against two expert raters; unclear whether debriefing quality counts as a psychological/interpersonal construct.

**Решение:** =

---

### 611 · R3164

**Multiagent Large Language Model Framework for Psychotherapy Fidelity Assessment in Motivational Interviewing and Cognitive Behavioral Therapy Training: Cross-Sectional, Simulation-Based Evaluation Study.**

2026 · JMIR medical education · journal article, journalarticle, article · eng · https://doi.org/10.2196/92964

Abstract Background Psychotherapy training is difficult to scale because manual rating of motivational interviewing (MI) and cognitive behavioral therapy (CBT) sessions is time-intensive, requires trained raters, and is subject to rater variability. Large language models (LLMs) may support simulation-based training and rubric-guided scoring, but early-stage evidence is needed before such systems can be applied to real learners. Objective This study aimed to conduct a simulation-based evaluation of a multiagent LLM framework for generating and scoring stylized MI and CBT training encounters. Methods We conducted a cross-sectional evaluation of a multiagent framework comprising Student, Patient, Evaluator, and Feedback agents. The Student agent conducted synthetic MI or CBT encounters with Patient agents derived from structured profiles. The Evaluator agent scored transcripts using study-specific MI and CBT scoring forms. Internal discrimination was tested across prompt-engineered novice, intermediate, and expert Student agent profiles using 133 MI and 102 CBT Patient profiles. Preliminary external grounding was assessed using 133 annotated motivational interviewing (AnnoMI) transcripts with coarse, metadata-derived, high/low session-level quality labels. Agreement with a pragmatic human-rater benchmark was evaluated using 16 independent human raters per modality. Criterion-level comparisons used paired Wilcoxon signed-rank tests with Benjamini-Hochberg false discovery rate correction at q <0.05. Agreement analyses used intraclass correlation coefficients (ICCs) with bootstrap 95% CIs. A secondary prompt-augmentation sensitivity analysis tested whether appending criterion-referenced feedback text to the novice Student-agent prompt shifted subsequent Evaluator-assigned scores. Results Evaluator scores increased across prompt-defined Student-agent competence levels. For MI, overall mean scores increased from 1.18 (95% CI 1.16‐1.20) for novice profiles to 1.75 (95% CI 1.69‐1.81) for intermediate profiles and to 3.57 (95% CI 3.48‐3.66) for expert profiles. For CBT, overall mean scores increased from 0.83 (95% CI 0.78‐0.88) to 2.18 (95% CI 2.10‐2.26) and 4.38 (95% CI 4.28‐4.48), respectively. Criterion-level planned contrasts were significant after false discovery rate correction. On AnnoMI transcripts, Evaluator scores aligned with metadata-derived high/low session labels, with 91.7% classification accuracy at the prespecified threshold. Human interrater reliability was an ICC(2,1) of 0.866 for MI and 0.769 for CBT. Evaluator-vs-human-consensus agreement was an ICC(2,1) of 0.959 for MI and 0.934 for CBT. In the secondary prompt-augmentation analysis, overall MI scores shifted from 1.18 to 1.44, and CBT scores shifted from 0.83 to 1.01. Conclusions This proof-of-concept study suggests that a rubric-guided multiagent LLM framework can score stylized synthetic MI and CBT transcripts along expected prompt-defined competence gradients and align with preliminary external and human-rater benchmarks. The study is innovative in separating synthetic learner, patient, scoring, and feedback-generation roles within a single simulation workflow, extending prior LLM work from plausible dialogue generation toward rubric-linked scoring. The findings support further development of scalable simulation tools for psychotherapy training research. Prospective studies with human trainees, standardized or real patients, and formal psychometric testing are required.

**ИИ:** + · обе модели · кодирование сессий · An LLM Evaluator agent scored MI and CBT fidelity in transcripts, and its scores were compared with human-rater consensus (ICC 0.959 for MI, 0.934 for CBT).

**Решение:** =

---

### 612 · R3181

**Reliability of AI-assisted coding of bilingual language samples compared with SALT-trained human coders**

2026 · TCU McNair Scholars Research Journal · journalarticle, review, article · https://doi.org/10.18776/tcu/mcnair/2026/9975381656108721

Language sample analysis (LSA) provides functional information about children’s expressive language, but preparing a transcript for analysis requires time, specialized conventions, and human judgement. This pilot methodological study examined the feasibility and count-level agreement of artificial intelligence (AI)-assisted SALT coding for Spanish narrative language samples from Spanish-English dual language learners. Four de-identified Spanish narrative transcripts were used in this study. The transcripts came from two Spanish-English bilingual children who were 5.3 and 5.8 years old. Each child completed two tasks: a wordless book retell and a short video retell. The SALT coding completed by ChatGPT Pro Extended and Claude Cowork Opus 4.8 Max was compared with coding completed by a SALT coding experienced bilingual speech-language pathologist (SLP). The sample includes only four transcripts; findings will be interpreted as preliminary and transcript-specific rather than evidence of clinical equivalence or broad generalizability. The study addresses a narrow feasibility question: whether AI-assisted coding can reduce coding burden while maintaining sufficient agreement to justify larger validation studies. A count-level method-comparison analysis was used to compare the number and type of SALT codes identified by each AI system with the codes identified by the SALT coding experienced bilingual SLP. The SALT coding experienced bilingual SLP coded 368 total SALT codes. ChatGPT coded 437 total codes, and Claude coded 370 total codes. Both AI systems had similar overall agreement with the SALT coding experienced bilingual SLP. ChatGPT and Claude both had an F1 score of 80.5%. ChatGPT found more possible codes than Claude, but this also means it may have over-coded more often. Claude was more conservative and was closer to the SALT coding experienced bilingual SLP total number of codes. The AI systems did better with Spanish verb root identification and reflexive pronoun coding. They had more difficulty with MC-unit fragment codes, omissions, mazes, utterance-level errors, and word-level error codes. These results suggest that AI may be helpful for supporting SALT coding, but a SALT coding experienced bilingual SLP is still needed to check and correct the coding before it is used for research or clinical work. These findings suggest that AI tools may help speech-language pathologists save time, identify possible missed SALT codes, and support more efficient bilingual language sample analysis when used with review from a SALT coding experienced bilingual speech-language pathologist.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT and Claude SALT-coded child narrative transcripts against an expert SLP (F1 reported); unclear if clinical language-sample coding counts as psychological.

**Решение:** =

---

### 613 · R3184

**ALGORITHMIC RUPTURES: TIKTOK’S ROLE IN SHAPING COLLECTIVE IDENTITIES OF DIGITAL NOMADS**

2026 · AoIR Selected Papers of Internet Research · journalarticle, article · https://doi.org/10.5210/spir.v2024i0.15134

This study investigates how TikTok’s socio-technical architecture ruptures the online collective identity of digital nomads, a mobile workforce redefining notions of labor and belonging. Digital nomadism exemplifies transnationalism, where privileged middle-class knowledge workers engage in intense, cross-border mobility as a lifestyle. Employing mixed methods—human deductive coding informing computational LLM-assisted content analysis—I examine how platform affordances mediate aspirations and shape digital nomads' online narratives. Using Maslow's theory of human motivation as an analytical framework, I explore narratives across four social practices central to digital nomadism: work, tourism, migration, and pilgrimage. For workers, narratives emphasize geographically fluid employment conditions; for tourists, content highlights desirable experiences of global exploration and leisure. Migrant-focused narratives foreground mobility challenges, economic impacts on destinations, and questions of privilege regarding who can become a digital nomad and where. Pilgrim-oriented narratives emphasize journeys toward self-actualization through continuous phases of "becoming," often involving demanding geographic travel. Findings reveal TikTok as a negotiation space for need hierarchies, challenging Maslow's linear progression while affirming its contextual flexibility. Contrary to Maslow’s ideal—self-actualization as a pinnacle achieved after fulfilling basic needs—TikTok’s digital nomad narratives disproportionately emphasize basic and safety needs. This prioritization of immediate concerns such as housing, affordability, and entertainment aligns with what this study defines as platformized "relational engineering," an algorithmic mechanism rewarding content that mirrors viewers' immediate needs. Thus, TikTok's affordances restructure collective identities by amplifying relatable experiences over deeper reflections on self-fulfillment or systemic inequalities.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM-assisted coding of TikTok narratives by Maslow needs, guided by human deductive coding; unclear whether LLM–human agreement is reported.

**Решение:** =

---

### 614 · R3185

**Evaluación de metáforas visuales sobre convivencia escolar con inteligencia artificial generativa y juicio experto**

2026 · RELATEC Revista Latinoamericana de Tecnología Educativa · journalarticle, article · en · https://doi.org/10.17398/1695-288x.25.2.225

This study compares agreement and reliability between human judges and GAI models when evaluating visual metaphors of school coexistence, understood as graphic representations that translate institutional experiences into symbolic scenes (a ranch with corrals, a market with stalls, and countries/faculties). The design was comparative, with repeated measures across three metaphors and the transcribed verbal explanations provided by the students who produced them in focus groups. Six human experts participated (18 ratings) and five LLMs (ChatGPT-5, ChatGPT-5 Pro, ChatGPT-o3, DeepSeek, Gemini 2.5), with five runs per model (75 ratings). The rubric included a global judgment (1-3), binary indicators, and 10 Likert items (1-5). Ordinal alpha, Cohen kappa, Fleiss kappa, Krippendorff alpha, and a p x r G-study with a D-study for human-GAI mixtures were estimated. The input was not identical across models: ChatGPT variants worked with image and description, whereas DeepSeek and Gemini evaluated the narrative description and transcript. Therefore, the results are interpreted as a baseline situated in the versions and conditions analyzed, not as a definitive conclusion about all current or future multimodal systems. Findings showed that GAI produced more words than human experts, although length was treated as a descriptive indicator rather than a measure of quality or depth. The Coexistence Index was higher for humans, especially in Metaphor 2 (Delta=+0.91). The D-study indicated that 1-2 human experts plus around 10 GAI runs reach G >= 0.95. ChatGPT-5 Pro was the model closest to human consensus. The study provides a reference point for future pedagogical analysis of student productions supported by GAI.

**ИИ:** ? · обе модели · неясен конструкт · LLMs and human experts rated students' metaphors and transcripts about school coexistence with the same rubric (kappa, alpha); unclear if the construct is psychological.

**Решение:** =

---

### 615 · R3191

**Extracting Quality of Life Information from Forum Posts Using Open-Source Large Language Models: Feasibility Study (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.92716

BACKGROUND Quality of Life (QoL) questionnaires are an established instrument designed to assess overall wellbeing and quality of life of patients. They are important in predicting the outcome of the disease and understanding the needs of individual patients. However, their repeated collection imposes substantial burden on both patients and clinical professionals. Many patients seek emotional support and mutual exchange in online communities for peer-support, where they frequently share detailed descriptions of symptoms and treatment experiences, addressing topics covered in QoL questionnaires. The emergence of large language models (LLMs) uncover potential for automatic extraction of relevant QoL information from patient-generated text. OBJECTIVE The aim of this study is to evaluate and compare various open-source LLMs and optimization approaches for automated extraction of QoL information from forum posts. METHODS The dataset consisted of 2,683 English-language posts from breast cancer patients recruited on Inspire.com online communities, manually annotated with sentence-level text spans indicating whether and where posts contained information relevant to 53 QoL questions from EORTC QLQ-C30 and QLQ-BR23 questionnaires. 11 open-source LLMs (8B-70B parameters) were evaluated in a zero-shot setup, generating 4,452 post-question predictions per model under two input conditions: post-only and post with additional context. For the best-performing model, additional experiments assessed the impact of chain-of-thought prompting, instruction optimization, few-shot prompting and parameter-efficient fine-tuning. For correctly classified yes/no instances, the overlap between model-generated evidence and human-annotated spans was evaluated. RESULTS Across 11 evaluated LLMs, GPT-OSS 20B achieved the highest macro F1-score (0.79) in the zero-shot post-only setting. Providing additional context consistently reduced performance of all models. Model size did not correlate with F1-score, with several mid-sized models (14B-30B) outperforming 70B models. For GPT-OSS 20B, chain-of-thought prompting did not improve performance (0.77). Instruction optimization produced results similar to the baseline in both zero-shot and few-shot settings (0.78-0.80). Bootstrap few-shot prompting with random search achieved the highest score overall (0.81). Parameter-efficient fine-tuning decreased performance (0.71). Most classification errors occurred in semantically broad or ambiguous terms and the fallback question. For correctly predicted yes/no answers, model-generated evidence matched or partially matched human-annotated spans in 89% of cases. CONCLUSIONS Open-source LLMs are a promising tool for extracting QoL information that aligns with standardized questionnaire responses from online health forums. Mid-sized models achieved the highest accuracy, particularly in zero-shot, post-only settings. Few-shot prompting can further improve the results. Models were also able to generate evidence spans that closely matched human annotations. However, they consistently struggled with ambiguous and semantically overlapping terms. Overall, automated extraction of QoL information from patient-generated content may offer a faster, lower-cost and low-burden complement to traditional QoL questionnaires, given that limitations such as symptom ambiguity are addressed in future work.

**ИИ:** + · обе модели · кодирование по кодбуку · Open-source LLMs label forum posts for EORTC QoL items (incl. emotional/social functioning), compared against manual human annotations.

**Решение:** =

---

### 616 · R3196

**Large language models for the computational assessment of personality organization in clinical interviews with adolescents**

2026 · Repository of the University of Ljubljana (University of Ljubljana) · dissertation · en · https://repozitorij.uni-lj.si/Dokument.php?id=250068&dn=

Pri polstrukturiranih intervjujih v psihiatriji strokovnjaki odgovore pacientov pretvarjajo v številčne ocene na podlagi vnaprej določenih ocenjevalnih kriterijev. Veliki jezikovni modeli (VJM-ji) bi lahko bili primerni za tovrstne naloge, saj lahko obdelujejo obsežna besedila v naravnem jeziku, sledijo podanim navodilom in ustvarjajo strukturirane izhode. Njihova ustreznost za ocenjevanje duševnega zdravja še ni bila zadostno ovrednotena. V magistrskem delu smo razvili in ovrednotili postopek, ki uporablja VJM za ocenjevanje funkcioniranja identitete, osrednje razsežnosti osebnostne organizacije, iz transkripcij Strukturiranega intervjuja osebnostne organizacije za mladostnike (Structured Interview of Personality Organization—Revised, Adolescent Version

**ИИ:** + · обе модели · подсчёт методики · An LLM scores identity functioning from STIPO-R adolescent interview transcripts, a task experts normally do; comparison with expert ratings is likely.

**Решение:** =

---

### 617 · R3219

**The Team Member Effect: Social Role Framing and Divergent Thinking in Large Language Models**

2026 · OSF Preprints (OSF Preprints) · text/project, preprint · https://doi.org/10.17605/osf.io/w79fy

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLMs likely generate divergent-thinking responses, but LLM scoring might be validated against human raters.

**Решение:** =

---

### 618 · R3221

**Exploring ChatGPT as a Simulated Client: A Feasibility Study in Undergraduate Counselor Training**

2026 · Journal of Technology in Counselor Education and Supervision · journalarticle, article · en · https://doi.org/10.61888/2692-4129.1153

Generative artificial intelligence (AI) offers new possibilities for simulation-based counselor training by enabling scalable, text-based interactions that mimic human dialogue. This exploratory feasibility study examined whether ChatGPT can serve as a simulated counseling client and feedback provider for undergraduate students learning counseling skills. Five upperclassmen completed a 45–60-minute text-based session with ChatGPT portraying “Sarah,” a college student experiencing depression and loneliness, followed by AI feedback and a semi-structured interview. Trained raters judged ChatGPT’s client portrayal and feedback as generally accurate, particularly for tone, empathy, and identification of students’ strengths. Accuracy was lower for rapport, summarizing, and pacing characteristic of an initial session. Students described the experience as realistic, easy to use, and low-pressure, appreciating the opportunity to pause and reflect between responses while noting the absence of nonverbal cues. Collectively, findings demonstrate the feasibility and instructional potential of ChatGPT as a low-cost supplement to traditional role-plays, supporting reflective, feedback-rich skill development in early counselor preparation.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · ChatGPT gave feedback on students' counseling skills, and trained raters judged its accuracy; unclear whether raters coded the same skills independently.

**Решение:** =

---

### 619 · R3226

**Mapping 99 emotion terms with GPT4 prompting reveals nuanced semantic conceptual structure.**

2026 · Scientific reports · journal article, med, journalarticle · eng · https://doi.org/10.1038/s41598-026-60536-4

Dimensional theories of emotion propose that affective experiences can be organised along continuous dimensions like Pleasure, Arousal, and Dominance. Recent computational methods for capturing these conceptual structures have relied primarily on word embeddings, requiring substantial technical expertise. This study examined whether prompting GPT4 as a more accessible method, can capture this structure more effectively, by comparing both approaches against human spatial reasoning, with particular focus on analysing extensive emotion vocabularies exceeding constraints of human cognitive capability. Study 1 established validity by testing six basic emotions, prompting showed strong convergence with human judgements, while embeddings produced fundamentally different clustering patterns. Study 2 extended analysis to 99 emotion terms. Both approaches identified two optimal clusters distinguished by both Pleasure and Dominance, though prompting produced clearer cluster separation. Particularly, Arousal emerged only at the larger vocabulary scale as a secondary, component-level dimension rather than a cluster-defining one. Together these results indicated that GPT prompting offers a promising tool for investigating semantic structure of emotion, particularly in terms of uncovering patterns that only become visible when analysing a broader sample of emotion lexicon.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-4 rated emotion terms on dimensions and was compared with human judgements, but the units are single words, not psychological texts.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: GPT-4 prompting maps emotion-term semantic structure versus human spatial arrangement; it doesn't code or rate psychological texts against human labels.)

**Решение:** -

---

### 620 · R3235

**LLMs Capture Emotion Labels, Not Emotion Uncertainty: Distributional Analysis and Calibration of Human-LLM Judgment Gaps**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.27345

Human annotators frequently disagree on emotion labels, yet most evaluations of Large Language Model (LLM) emotion annotation collapse these judgments into a single gold standard, discarding the distributional information that disagreement encodes. We ask whether LLMs capture the structure of this disagreement, not just majority labels, by comparing emotion judgment distributions between human annotators and four zero-shot LLMs, plus a fine-tuned RoBERTa baseline, across two complementary benchmarks: GoEmotions and EmoBank, totaling 640,000 LLM responses. Zero-shot models diverge substantially from human distributions, and in-domain fine-tuning, not model scale, is required to close the gap. We formalize a lexical-grounding gradient through a quantitative transparency score that predicts per-category human--LLM agreement: LLMs reliably capture emotions with explicit lexical markers but systematically fail on pragmatically complex emotions requiring contextual inference, a pattern that replicates across both categorical and continuous emotion frameworks. We further propose three lightweight post-hoc calibration methods that reduce the distributional gap by up to 14\%, and provide actionable guidelines for when LLM emotion annotations can, and cannot, substitute for human labeling.

**ИИ:** + · обе модели · бенчмарк с метками людей · Compares zero-shot LLM emotion annotations with human annotator distributions on GoEmotions and EmoBank and reports per-category agreement between humans and LLMs.

**Решение:** =

---

### 621 · R3254

**LLM-Assisted Qualitative Coding with Human Validation via Inter-rater Reliability**

2026 · Purdue · dissertation/thesis, dissertation · https://doi.org/10.25394/pgs.32118184

This thesis examines how large language models can support qualitative coding while keeping human interpretation at the center of the research process. Using student reflections from an undergraduate software development course, the study compares a standalone LLM approach and a retrieval-augmented generation (RAG) approach against human coding through inter-rater reliability analysis. It also uses human-led reflexive thematic analysis to identify how students describe self-regulated learning in collaborative team environments. The findings show that the standalone LLM was more reliable than the RAG setup for this coding task, while the thematic analysis highlights the roles of planning, teamwork, resource use, communication, confidence, and cultural interaction in student learning.

**ИИ:** + · обе модели · кодирование по кодбуку · LLM and RAG coding of student reflections on self-regulated learning, compared with human coding using inter-rater reliability.

**Решение:** =

---

### 622 · R3270

**Blending Human and LLM Expertise to Detect Hallucinations and Omissions in Mental Health Chatbot Responses**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.06216

As LLM-powered chatbots are increasingly deployed in mental health services, detecting hallucinations and omissions has become critical for user safety. However, state-of-the-art LLM-as-a-judge methods often fail in high-risk healthcare contexts, where subtle errors can have serious consequences. We show that leading LLM judges achieve only 52% accuracy on mental health counseling data, with some hallucination detection approaches exhibiting near-zero recall. We identify the root cause as LLMs' inability to capture nuanced linguistic and therapeutic patterns recognized by domain experts. To address this, we propose a framework that integrates human expertise with LLMs to extract interpretable, domain-informed features across five analytical dimensions: logical consistency, entity verification, factual accuracy, linguistic uncertainty, and professional appropriateness. Experiments on a public mental health dataset and a new human-annotated dataset show that traditional machine learning models trained on these features achieve 0.717 F1 on our custom dataset and 0.849 F1 on a public benchmark for hallucination detection, with 0.59-0.64 F1 for omission detection across both datasets. Our results demonstrate that combining domain expertise with automated methods yields more reliable and transparent evaluation than black-box LLM judging in high-stakes mental health applications.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM judges were scored against human annotations of hallucinations and omissions in counselling responses; unclear whether hallucination counts as a psychological construct.); Sonnet + (LLM-судья: LLM judges detect hallucinations and omissions in mental health counseling chatbot responses, evaluated against expert human annotations (52% accuracy), so it fits the LLM-as-judge type.)

**Решение:** +

---

### 623 · R3272

**From Narratives to Population Shares: Coding Protocols, LLM Labels, and Measurement in GSS Next**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.7613281

Open-ended surveys increasingly use large language models (LLMs) to convert respondents' narratives into categorical population estimates. We distinguish three sources of disagreement in the 2024 General Social Survey Next coding supplement: respondents' own menu selections versus external text coding, a single human expert versus machine coders, and model/prompt choice for the same records. Among 902 respondents with complete codes from four GPT configurations, an equally weighted average of their labels classifies 4.53 percentage points fewer responses as "none of eight issues" than the expert (95% design-linearized interval: [-7.19,-1.86]); the gap remains detectable in a nine-category Holm family specified for this reanalysis. In contrast, the six matched GPT-versus-GPT residual-share differences are within 1.11 percentage points and none is individually significant, although equivalence is not established. Respondent-external gaps exceed twenty points, but also alter the classification protocol and therefore cannot be attributed to algorithms. We report all categories, incomplete Claude outputs, direct tests of weighting sensitivity, influential weights, and a corrected Rao-Wu rescaled bootstrap. The data show how the coding procedure and analysis domain change estimated issue prevalence without identifying semantically true labels. Inference uses the official 2024 core-stratum and variance-PSU identifiers with the dedicated Next weights; uncertainty from estimated follow-on nonresponse calibration is not separately propagated.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT coding of GSS open-ended narratives compared with a human expert; the 'eight issues' may be political or social rather than psychological.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM vs human coding of GSS open-ended responses into national issue categories; a political/social survey topic, not a psychological or clinical construct.)

**Решение:** -

---

### 624 · R3288

**Determinants of Trust and Reliance on Artificial Intelligence in Clinical Settings: A Study on Physicians' Use of Large Language Model in Psychiatric Symptom Assessment.**

2026 · Psychiatry investigation · journal article, journalarticle, review · eng · https://doi.org/10.30773/pi.2025.0330

Objective This study investigated physicians’ use of large language model (LLM)-generated assessments in psychiatric symptom evaluation and factors influencing their acceptance of artificial intelligence (AI) suggestions.Methods Twelve psychiatrists evaluated 50 anonymized psychiatric case vignettes, rating the presence and severity of 73 symptoms using a 4-point Likert scale. After initial assessment, they reviewed GPT-4o’s symptom ratings and could revise their evaluations. Accuracy was measured against a gold standard established by expert consensus. We computed initial (I), LLM (L), and revised (R) accuracy scores using percent agreement and weighted kappa. Performance improvement was measured by relative kappa increase. Regression analyses examined the influence of task difficulty and user competence on accuracy improvement.Results LLM assessments outperformed initial physician ratings in both agreement (90.4% vs. 82.9%, p&lt;0.001) and kappa (0.713 vs. 0.559, p&lt;0.001). After revision, physician performance improved (κ=0.651) but remained below LLM levels. The switch rate—cases where physicians revised in response to LLM disagreement—was modest (25.4%), indicating partial reliance on AI. Performance gains were positively associated with LLM accuracy and negatively associated with users’ own baseline competence, suggesting that less confident users rely more on LLM assistance.Conclusion Physicians demonstrated limited but strategic trust in LLM outputs, adjusting their judgments more when the LLM was accurate or when their own competence was lower. Miscalibrated trust—excessive skepticism or overreliance—led to missed gains. Effective human-AI collaboration in psychiatry requires tools and training for accurate self-assessment and AI trust calibration to avoid the pitfalls of algorithm aversion or overreliance.</jats:p

**ИИ:** + · обе модели · клиническая оценка · GPT-4o rated symptom severity in psychiatric vignettes; compared with expert consensus gold standard using kappa and percent agreement.

**Решение:** =

---

### 625 · R3289

**Large Language Models for Distress Rating in Korean Psycho-Oncology Interviews: Exploratory Clinician-Benchmarked Evaluation Study.**

2026 · Journal of medical Internet research · journal article, journalarticle, article · eng · https://doi.org/10.2196/91405

Abstract Background Psychiatric distress is common among patients with cancer; yet, systematic interview-based screening remains difficult to scale in routine clinical care. Large language models (LLMs) have shown promise as scalable tools for mental health assessment, but most existing evidence is derived from clinician-authored records, translated text, or proxy data. The performance characteristics, error patterns, and explanatory behaviors of contemporary LLMs when applied to authentic, non-English psychiatric interviews remain insufficiently characterized. Objective This exploratory study evaluated how contemporary LLMs reproduced psycho-oncologists’ item-level symptom ratings from real-world Korean psycho-oncology interviews, focusing on concordance, directional bias, and clinician-adjudicated error characteristics. Methods Between April 2024 and May 2025, 101 adults receiving oncologic care in South Korea underwent semistructured interviews. Board-certified psycho-oncologists provided real-time, time-stamped ratings of 39 items. Generative pretrained transformer 4o (GPT-4o), Claude 3.5 Sonnet, and Gemini 2.5 Flash generated item scores and brief rationales using identical Korean zero-shot rubrics. Concordance between clinician ratings was evaluated using ordinal and binary screening metrics. A paired Wilcoxon test compared patient-level total symptom burden. Binary mismatches were clinically adjudicated as ambiguous or definite overestimation or underestimation with an 8-etiology taxonomy. Model-generated rationales were further meta-evaluated using GPT-5.4, Claude Sonnet 4.6, and Gemini Pro 3.1 across 4 dimensions: citation (use of quoted supporting statements), structure (logical organization of the rationale), mapping (consistency between the rationale and the assigned item rating), and expansion (degree of interpretive elaboration beyond the explicit transcript content). The associations between meta-evaluation results and absolute error were examined using cross-classified mixed-effects models. Results Out of 101 participants, 88 (87.1%) were predominantly female and had breast cancer as the primary cancer type (n=70, 69.3%). Across 3931 item-level ratings, all models showed good agreement with clinicians (intraclass correlation coefficient: 0.816‐0.872), with GPT-4o showing the highest agreement. Claude 3.5 and Gemini 2.5 yielded significantly higher patient-level symptom burden (adjusted P<.001 and adjusted P=.002, respectively), whereas GPT-4o did not (adjusted P=.15). Clinician adjudication attributed 97 of 248 (39.1%) GPT-4o mismatches, 88 of 301 (29.2%) Claude 3.5 mismatches, and 118 of 355 (33.2%) Gemini 2.5 mismatches to intrinsic ambiguity in patient speech. Among definite errors, misapplication of severity thresholds was the predominant mechanism across models. Exploratory mixed-effects models showed that higher expansion and lower mapping scores were associated with larger absolute errors. However, the association with expansion may reflect case difficulty or ambiguity rather than causation. Conclusions In this exploratory clinician-benchmarked evaluation of authentic interviews from a Korean psycho-oncology sample comprising predominantly women and patients with breast cancer, LLMs showed high aggregate concordance with psycho-oncologists’ item-level ratings while differing in their error profiles. These findings support further evaluation of LLM-based item-level symptom-rating approaches in psycho-oncology. Validation in larger, more diverse, and independent cohorts is needed.

**ИИ:** + · обе модели · клиническая оценка · GPT-4o, Claude and Gemini rated 39 symptom items from Korean psycho-oncology interview transcripts; agreement with psycho-oncologists' ratings reported as ICC.

**Решение:** =

---

### 626 · R3293

**Beyond AI Psychosis and Sycophancy: Structural Drift as a System-Level Safety Failure**

2026 · medRxiv · preprint, ppr · https://doi.org/10.64898/2026.03.19.26346371

ABSTRACT Background Conversational AI safety systems are primarily evaluated using message-level content monitoring, which assesses inputs and outputs in isolation. This message-by-message approach can miss interaction-level risks that emerge over extended conversations, including patterns discussed in reports of “AI psychosis.” Critically, by the time users express overt psychosis-spectrum content, opportunities for intervention may be limited. Objective We investigated whether LLM responses gradually expand and connect interpretations beyond the user’s original concerns, a process we term structural drift . We also tested whether this drift can be detected early and automatically. Methods We developed an automated, LLM-adapted rubric-based prompt for seven domains of anomalous (psychosis-spectrum) experience, derived from phenomenological psychiatry to capture subtle shifts in subjective interpretation. In Part 1, we evaluated the rubric using gold-standard text excerpts (N = 484) adapted from clinically validated qualitative instruments. In Part 2, we analyzed 1,290 user-LLM response exchanges from 7 dialogues, using 3 different LLMs (5 repeats each), to measure (i) domain amplification (increasing score within a domain) and (ii) domain expansion (new domains appearing over time). Results Automated scoring showed strong agreement with gold-standard excerpts (domain accuracy 82.7-98.9%; exact 0-3 agreement 63.6-82.7%). Across dialogues, we observed significant amplification in four domains ( p < .05; d = 0.14-0.46) and domain expansion in 83.8% of dialogues (88/105; p < .001). Conclusions AI responses can systematically expand and intensify users’ descriptions beyond their initial input. Taken together with the predictive-processing accounts of psychosis, the exposure itself may reinforce maladaptive inferences. Because drift is detectable from ordinary dialogue without clinical-style probing, this structural drift detection may support scalable, real-time monitoring for emerging risks before overt escalation.

**ИИ:** + · обе модели · клиническая оценка · LLM rubric scored psychosis-spectrum experience domains in 484 gold-standard excerpts from clinical instruments; reports accuracy and exact 0-3 agreement.

**Решение:** =

---

### 627 · R3300

**Depression Severity Classification on Indonesian Social Media: A PHQ-9-Grounded IndoBERT Approach**

2026 · 2026 5th International Conference on Electronics Representation and Algorithm (ICERA) · conference, review · https://doi.org/10.1109/icera72709.2026.11666681

Depressive disorders remain the single largest contributor to years lived with disability worldwide, accounting for 6.2% of the global burden. However in Indonesia, professional care is still hard to reach and stigma discourages people from seeking it: barely 9% of those affected ever see a psychologist or psychiatrist, and many go untreated until their condition has already deteriorated. To help close this gap, this study turn to Indonesian social media as an alternative data source and develop an IndoBERT-based classifier capable of staging depressive severity across the five PHQ-9 categories: minimal, mild, moderate, moderately severe, and severe. A total of 46,624 raw posts were reduced to 16,458 relevant samples after preprocessing and PHQ-9-indicator-based relevancy filtering, then semi-automatically labeled using GPT-4o-mini guided by a psychologist-reviewed clinical annotation scheme. On a held-out test set, the soft-voting ensemble achieved a macro F1-score of 92.69% and accuracy of 93.07%, with 82.5% of misclassifications confined to adjacent severity levels, and language-specific pretraining confirmed statistically superior to a multilingual baseline (χ2 = 14.68, p < 0.001), offering a reproducible and clinically grounded first-pass screening tool for early mental health intervention in Indonesia.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · GPT-4o-mini semi-automatically labeled PHQ-9 depression severity in posts; human review or agreement with the LLM labels may be reported in the full text.

**Решение:** =

---

### 628 · R3322

**Automatic Annotation and Analysis of Oral History using LLMs: An Empirical Study of Densho Digital Collection**

2026 · Journal on Computing and Cultural Heritage · journalarticle, article · en · https://doi.org/10.1145/3849086

Oral histories serve as vital records of lived experience, particularly within communities affected by systemic injustice and historical erasure. Effective and efficient annotation and analysis of oral history archives can promote access and use of the oral histories. However, large scale analysis of these archives remains limited due to their unstructured format, emotional complexity, and the high cost of manual annotation. This paper presents a scalable LLM-based framework to automate semantic and sentiment annotation for oral history archives, with a focus on Japanese American Incarceration Oral History (JAIOH). Using large language models (LLMs), this study seeks to construct a high-quality dataset, systematically evaluate the performance of multiple LLMs, and investigate effective prompt engineering strategies on annotation in historically sensitive contexts. Our multiphase approach combines expert annotation, prompt design, and LLM evaluation using ChatGPT, Llama, and Qwen. We labeled 558 sentences from 15 narrators for sentiment and semantic classification, then developed prompts and evaluated across zero shot, few shot, and retrieval augmented generation (RAG) strategies based on the labeled data. On this benchmark, ChatGPT achieved the highest macro-F1 score for semantic classification (88.71%), followed by Llama (84.99%) and Qwen (83.72%). For sentiment analysis, Llama performed slightly better (82.87%) than Qwen (82.66%) and ChatGPT (82.29%), with all models showing comparable results. Based on the overall evaluation, we selected the best performing prompt configurations for each task and used them to automatically annotate 92,191 sentences from 1,002 interviews in the JAIOH collection. This study develops an LLM-based framework for automatic annotation and analysis of oral history collections. The evaluation results indicate that the proposed LLM-based annotation framework provides promising performance on semantic and sentiment annotation of the JAIOH collection. It contributes a reusable pipeline and practical guidance for applying LLMs in culturally sensitive archival analysis. All code, annotated data, prompt templates, and experimental details are available at the Repository . 1

**ИИ:** ? · обе модели · неясен конструкт · LLMs labelled sentiment in oral-history interview sentences against expert labels; unclear whether this sentiment coding counts as an emotion construct.

**Решение:** =

---

### 629 · R3326

**Leveraging AI for Analysis of Digital Health Information on Cancer Prevention Among Arab Youth and Adults: Content Analysis.**

2026 · JMIR infodemiology · journal article, journalarticle, article · eng · https://doi.org/10.2196/77888

BACKGROUND: As TikTok (ByteDance) grows as a major platform for health information, the quality and accuracy of Arabic-language cancer prevention content remain unknown. Limited access to culturally relevant and evidence-based information may exacerbate disparities in cancer knowledge and prevention behaviors. Although large language models offer scalable approaches for analyzing online health content, their utility for short-form video data, especially in underrepresented languages, has not been well established. OBJECTIVE: We aimed to characterize and evaluate the quality of Arabic-language TikTok videos on cancer prevention and explore the use of large language models for scalable content analysis. METHODS: We used the TikTok research application programming interface and a GPT-assisted keyword strategy to collect Arabic-language TikTok videos (2021-2024). From an initial collection of 1800 TikTok videos, 320 were eligible after preprocessing. Of these, the top 25% (N=30) most-viewed were analyzed and manually coded for content type, cancer type, uploader identity, tone and register, scientific citation, and disclaimers. Video quality was assessed using the Patient Education Materials Assessment Tool for Audiovisual Materials for understandability and actionability, and the Global Quality Scale (GQS). GPT-4 was used to generate artificial intelligence annotations, which were compared to human coding for select variables. RESULTS: The top 25% (N=30) most-viewed videos amassed a total of 21.6 million views. Diet and alternative therapies were most common (15/30, 50%), which included recommendations to reduce hydrogenated oils, increase fruit and vegetable intake, and the use of traditional remedies such as garlic and black seed. Only 6.6% (2/30) of videos cited scientific literature. General cancer (15/30, 53%), breast (5/30, 17%), and cervical (4/30, 13%) cancers were most frequently mentioned. Doctors led 30% (9/30) of videos and were more likely to produce higher quality content, including significantly higher global quality scores (GQS=4, median 4, IQR 4-4 vs 3, median 3, IQR 2-3, P=.06). Over half of the videos had low understandability (16/30, 53%) and actionability (18/30, 60%). Emotionally framed content had the highest engagement across likes and shares, although this did not reach statistical significance (P=.08 and P=.05, respectively). However, emotional tone was significantly associated with lower GQS scores (P=.01). GPT-4 showed high agreement with human coders for cancer type (Cohen κ=1.0), strong agreement for GQS (κ=0.94), but low agreement for tone classification (κ=0.15), due to misclassification of emotional delivery from text-only input. CONCLUSIONS: Arabic-language TikTok cancer prevention content is highly engaging but variable in quality, with emotionally framed videos attracting substantial attention despite lower informational value. Artificial intelligence-assisted tools show strong potential for scalable, multilingual health content analysis, but multimodal approaches are needed to accurately interpret tonal and audiovisual features.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 agreement with human coders is reported (κ), but mostly on cancer health-content quality; only emotional tone is borderline psychological.

**Решение:** =

---

### 630 · R3339

**An Empirical Study on the Supportive Use of Artificial Intelligence in Assessing the Risk of Targeted Violence Escalation in Intimate Partner Violence Cases**

2026 · Forum of Public Safety and Culture · journalarticle, article · https://doi.org/10.52902/kjsc.2026.50.137

This study examines the applicability of an AI-based risk assessment model integrating ChatGPT 5.1 Pro with a structured assessment tool, in response to the growing severity of dating violence and the need for early identification of escalation to serious violence. Court rulings from 367 stalking cases between 2022 and 2023 involving romantic partners were structured using the Korean Stalking Assessment Scale (K-SAS), from which 16 cases, including high-risk cases, were selected for analysis. Final risk assessments were conducted independently by two crime analysts and the AI, which performed evaluations using a pre-improvement model (v1) and a revised model (v2). Agreement between AI and expert assessments was examined using intraclass correlation coefficients. The results indicated that AI v1 overestimated risk by inferring information not explicitly contained in the rulings, resulting in substantial discrepancies from expert judgments. These discrepancies were significantly reduced in AI v2, which also demonstrated acceptable reliability in qualitative evaluations of risk factors and management strategies. Overall, the findings suggest that while AI is limited as a standalone assessor of serious violence escalation risk, it shows practical value as a decision-support tool for early risk identification and case screening. The study highlights the need to integrate AI-based risk assessment into a multilayered framework that complements human expert judgment.

**ИИ:** + · обе модели · клиническая оценка · ChatGPT assessed violence-escalation risk from court rulings using K-SAS; two crime analysts rated the same cases; ICC agreement was reported.

**Решение:** =

---

### 631 · R3342

**Detection of Self-Harm in Electronic Mental Health Records Using Privacy-Preserving Local Language Models: Methodological Study.**

2026 · JMIR mental health · journal article, journalarticle, article · eng · https://doi.org/10.2196/87586

Abstract Background Self-harm is the strongest risk factor for suicide and an important outcome for mental health care. Although prevalent in clinical populations, it is often imprecisely captured in routinely collected clinical data, where it is often recorded and stored as unstructured free text. Contemporary language models, such as GPT (OpenAI) and Gemini (Google), can analyze free-text clinical notes, but such models may violate data governance of processing sensitive patient data. Objective This study aimed to evaluate whether a privacy-preserving language model running entirely within an institution’s secure computing infrastructure (here, the UK National Health Service [NHS]) could accurately identify the presence and timing of self-harm using electronic health records from secondary mental health care. Methods Clinical notes were drawn from Oxford Health NHS Foundation Trust using a multistage workflow: (1) a random sample of 1000 patients with a psychiatric diagnosis, defined according to the ICD-10 (International Statistical Classification of Diseases, Tenth Revision; codes F00–F99); (2) candidate-note identification using a Gemma3-4b language model to flag notes containing self-harm content; and (3) from those candidates, 1352 randomly sampled notes were selected for expert annotation, resulting in gold-standard corpus enriched for self-harm content. Clinical notes were annotated for the presence of self-harm and its timing (≤90 days, >90 days, or unknown). A privacy-preserving locally served 27-billion-parameter Gemma 3 language model (“Gemma3-27b”) was used as the core model. Prompts were systematically developed and refined using a labeled development set to identify self-harm and generate a structured output per clinical record. Gemma3-27b performance was compared against a strong baseline multilabel text classification model based on robustly optimized BERT pretraining approach (RoBERTa), a transformer-based language model architecture. Model performance was evaluated using precision, recall, and the F1-score (harmonic mean of precision and recall), with 95% CIs estimated from 1000 bootstrap samples with replacement. Results Gemma3-27b outperformed the RoBERTa classifier across all categories, achieving Precision=0.92, Recall=0.92 (sensitivity), and F1-score=0.92 for notes containing self-harm, and Precision=0.97, Recall=0.97 (specificity), and F1-score=0.97 for notes without self-harm. For the 51 notes labeled as recent self-harm in the held-out test set, Gemma3-27b achieved Precision=0.84, Recall=0.75, and F1-score=0.79. The global weighted F1-score of Gemma3-27b across all categories was 0.88, compared to 0.85 for RoBERTa. Conclusions With systematic prompt development on a labeled development set, but no gradient-based fine-tuning, the current Gemma3-27b language model matched or exceeded a fine-tuned RoBERTa classifier for ascertaining self-harm events and their timing. Aggregate gains were modest, while improvements were largest in the most challenging, lower-frequency timing categories. On a simplified binary recent-versus-other task, RoBERTa performed marginally better, indicating that supervised classifiers remain highly effective when the task is simplified and sufficient labeled data exist. This work demonstrates the technical feasibility of privacy-preserving self-harm detection within a secure NHS research environment.

**ИИ:** + · обе модели · клиническая оценка · Gemma3-27b found self-harm and its timing in mental health clinical notes, and its results were checked against expert gold-standard annotations.

**Решение:** =

---

### 632 · R3343

**PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.25485

Health AI is evolving from answering questions to agentic systems that converse with patients, reason about health records, and act on their behalf. Primary care guards against diagnostic errors and unsafe care; agents assisting in this domain warrant evaluation against the same risks. Current benchmarks focus on medical knowledge, assessed through isolated question-answering or clinician-facing tasks. PatientAgentBench benchmarks patient-facing agentic healthcare; it evaluates a foundation model, wrapped in an agent with a sandbox of healthcare tools, conversing with a simulated patient. Each conversation is scored by an LLM-as-a-Jury across six dimensions via over a hundred conversation-agnostic, clinician-grounded criteria. To validate alignment, licensed clinicians annotated shared conversations, yielding 79-93% adjacent agreement between jury and expert raters, on par with or exceeding clinician inter-rater agreement. We benchmarked 10 models across four families on the same 1,200 scenarios and found clinical gaps. Triage quality is the most discriminating dimension: pass rates rise from 32% for the weakest models to 88% for the strongest, with agents often acting on administrative requests without clinical screening. Clinical safety and workflow accuracy follow the same pattern: the weakest models fail often, fabricating unexecuted actions, while frontier models fail on only 1-3% of cases, from unverified tool outputs and omitted crisis resources in an emergency. More capable models narrow these gaps but do not close them; the strongest scores only 4.25 of 5 overall. These failures surface only in sustained, tool-using conversations against realistic patient records, confirming that static benchmarks are insufficient as healthcare agentic systems gain autonomy. We release the framework as a reproducible, clinician-validated evaluation standard to help the field close this gap. Code: https://github.com/amazon-science/PatientAgentBench

**ИИ:** ? · обе модели · неясен конструкт · LLM jury validated against clinician ratings, but the conversations are primary care; unclear if any of the six dimensions (e.g., empathy, crisis handling) is psychological.

**Решение:** =

---

### 633 · R3345

**AbilityScore: Development and Preliminary Psychometric Characterization of a Standardized Composite Index for Quantifying Child Developmental Readiness**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.19482122

Background: Developmental assessment has relied on siloed instruments for over 160 years. A child assessed with ADOS-2, Vineland-3, and Bayley-4 receives three separate reports on incompatible scales, leaving families without a unified picture of progress. Objective: To describe the architecture, computation methodology, and preliminary psychometric evidence for AbilityScore, a standardized composite developmental index (0–1000) that quantifies observed functional developmental performance relative to age-normed expectations. Methods: AbilityScore synthesizes the clinical essence of 25 internationally validated assessments into a single metric, mapping 339 skills across 148 abilities through structured clinical observations. Preliminary psychometric evidence derives from approximately 18.6 million therapy sessions across 70+ centers, 4 Indian states, 16 languages, and 28 diagnostic categories. Results: Operational data show inter-rater reliability r = 0.91 (p < 0.001), ICC = 0.88 (95% CI 0.84–0.91), MAPE = 6.7%, and bias variance ratio ≤ 1.05. A formal validation study (BHCL-VAL-2026-001) is now in planning. Keywords: developmental assessment, composite index, child development, neurodevelopment, autism, WHO ICF, psychometrics, AbilityScore, GPT-OS

**ИИ:** разошлись — Opus -5 (нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM: Child developmental index from structured clinical observations; no LLM coding text against human coders described ('GPT-OS' keyword only).); Sonnet ? (неясно, сравнивали ли с людьми: Developmental index from therapy sessions; the keyword "GPT-OS" hints at an LLM, and inter-rater reliability is reported, but the abstract doesn't say whether an LLM scores the text against human raters.)

**Решение:** -

---

### 634 · R3389

**Establishing the behavioral feasibility of a structured story-generation paradigm for neurophysiological research.**

2026 · Frontiers in psychology · journal article, journalarticle, article · eng · https://doi.org/10.3389/fpsyg.2026.1920009

Historically, many standard measures evaluate creativity at a single time point and are not suitable for capturing the continuous neural activity underlying naturalistic, creative cognition. The aims of our study were to: (a) establish the feasibility of a behavioral paradigm suitable for investigating the continuous, temporal dynamics of creative cognition using neurophysiological methods, and (b) evaluate the feasibility of using large language models (LLMs) for scoring. Sixty undergraduate students (M age = 21.65 years; M/F = 50%) wrote a brief story integrating three unrelated images into a single narrative. Each story was scored by two large LLMs. The ICC(2,1) for total story scores was 0.67 (95% CI [0.51, 0.79]), indicating moderate agreement between models and were averaged into a composite score. The story task produced a broad distribution of scores (M = 9.2, SD = 2.1; range = 4.5-12.5) supporting its ability to generate variable creative output. We compared the total story creativity score to the Inventory of Creative Activities and Achievements (ICAA) and the Divergent Association Task (DAT). There were no significant correlations with ICAA or DAT scores. A random subset ( n = 30) of stories rated by two human raters, resulted in moderate agreement with LLM scores (ICC(3,1) = 0.50, 95% CI [0.18, 0.73]). These findings provide preliminary evidence for the behavioral feasibility and characterization of a structured, temporally extended naturalistic, narrative paradigm that can be integrated with neurophysiological methods. Future studies will examine the associated neural signatures and further explore LLM scoring with human raters.

**ИИ:** + · обе модели · подсчёт методики · LLMs scored creativity in story-task responses; LLM–human agreement reported (ICC = 0.50) on a subset rated by two humans.

**Решение:** =

---

### 635 · R3422

**ContextMental: A Sociocultural Benchmark for Arabic Mental Health Understanding**

2026 · Electronics · journalarticle, article · en · https://doi.org/10.3390/electronics15122558

Mental health discourse may reflect social relationships, cultural norms, and religious factors that shape how individuals express and interpret distress. Existing NLP research on mental health has advanced the detection of depression, anxiety, suicide risk, and related clinical signals using text mining, neural classification, transformer-based models, and, more recently, large language models. However, most systems treat text primarily as a clinical signal rather than examining the social and cultural contexts in which distress is expressed. Arabic NLP research remains even more limited, largely focusing on detecting clinical conditions while overlooking contextual factors that shape mental health questions. This work introduces ContextMental, a multi-label annotation schema and benchmark dataset for modeling sociocultural context in Arabic mental health questions. The dataset contains 2677 questions, including 552 instances with contextual labels, enabling fine-grained analysis of social, cultural, and religious dimensions. An AraBERT-based classification framework is further developed using imbalance-aware optimization, semi-supervised pseudo-labeling, and adaptive threshold calibration. Experimental results indicate that pseudo-label augmentation improves overall classification performance, suggesting that semi-supervised learning can support context-aware Arabic mental health classification. This study provides a context-aware annotation framework, a benchmark dataset, and an AraBERT-based baseline modeling pipeline for Arabic mental health NLP, thereby supporting future research on socially, culturally, and religiously grounded language technologies.

**ИИ:** разошлись — Opus -5 (нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM: The benchmark's classifier is AraBERT, an encoder-only model; no generative LLM is compared with the human annotations.); Sonnet ? (другое: Arabic mental health benchmark with human annotation, but the modeling uses AraBERT (encoder); unclear whether any LLM is evaluated against human labels.)

**Решение:** -

---

### 636 · R3427

**ChatAnime: Towards User-Centered Emotional Support in LLM-based Virtual Character Chat**

2026 · Annual Meeting of the Association for Computational Linguistics · journalarticle, conference · https://doi.org/10.18653/v1/2026.acl-long.2179

With the growing popularity of virtual character platforms like Character.AI, users are increasingly turning to role-playing agents for emotional support in daily life. Yet existing research mainly focuses on character consistency in fictional or game-based scenarios, overlooking user-centered interactions such as compan-ionship and psychological support. To bridge this gap, we propose Emotionally Supportive Role-Playing (ESRP), a framework designed to align role-playing with real-world user scenarios and emotional needs. We focus on typical users of these platforms, i.e., anime enthusi-asts—including students, office workers, free-lancers, and self-employed individuals—and design scenario-based questions that reflect their everyday struggles such as work stress and social loneliness. Through a two-round data collection involving 40 anime fans and 10 Large Language Models (LLMs), we build ChatAnime: the first ESRP dataset with 2,400 human-written and 24,000 LLM-generated responses, supported by over 132,000 fine-grained human annotations. We also provide the ESRP evaluation framework featuring 9 fine-grained metrics across three dimensions: basic dialogue, role-playing and emotional support, along with an overall metric for diversity. Experimental results under our evaluation setting show that top-performing LLMs surpass anime fans in role-playing and emotional support, while humans still lead in diversity. The ChatAnime dataset is available at

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Human annotations of emotional-support responses; unclear whether an LLM judge was validated against them in the evaluation framework.

**Решение:** =

---

### 637 · R3428

**Empathy, Actionability, Safety Framing, and Equity in Large Language Model Responses to Pregnancy Lifestyle Advice**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/ycru2

This study evaluates how leading large language models (LLMs) balance emotional and clinical communication quality when responding to non-emergency, grey-area pregnancy lifestyle queries (e.g., diet, exercise, skincare, supplements, recreational exposures). Using a two-layer evaluation framework, exploratory lexicon-based measures (VADER, TextBlob, Flesch-Kincaid) and a multi-judge LLM-as-Judge ensemble benchmarked against clinician ratings, responses are scored on four primary dimensions: empathy, actionability, safety framing, and equity. Additionally, the study tests whether demographic identity markers embedded in prompts produce systematically different responses.

**ИИ:** разошлись — Opus ? (другое: OSF pre-registration of an LLM-as-judge rating empathy and safety, benchmarked against clinician ratings; may only be a protocol with no results.); Sonnet + (LLM-судья: Multi-judge LLM ensemble rates chatbot responses (empathy, safety framing) benchmarked against clinician ratings; it's a preregistration, so results may be missing.)

**Решение:** +

---

### 638 · R3438

**Evaluating Conversational AI Recognition of Clinically Meaningful State Transitions in Suicide-Risk Dialogue: A Multi-Tier Rubric Approach with Independent Mechanical Severity Triangulation**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.20146999

Conversational artificial intelligence (AI) systems are increasingly deployed in contexts where users disclose, directly or indirectly, signals of suicide risk. Existing safety evaluation approaches typically rely on single-evaluator AI scoring, content-moderation classifiers focused on explicit unsafe text, or aggregate rubrics that do not measure recognition of clinically meaningful state transitions in indirect, compressed, denied, or socially smoothed language. This paper introduces a multi-tier clinical evaluation methodology combining (i) stage-aware scenario specification with per-turn reference annotation, (ii) a three-tier scoring rubric operating at turn, run, and expert-review levels, (iii) an independent Mechanical Severity Score (MSS) computed by a deterministic rule-based procedure from structured per-turn observation fields, executed independently of the holistic AI-derived run-level concern rating and providing a triangulating signal that surfaces evaluator drift, and (iv) an integrated routing and review pipeline with a model-blinded human expert review interface. The methodology is informed by multiple theoretical anchors including the Salient Distress Model of Suicide, the Narrative-Crisis Model, the Three-Step Theory of Suicide, and the Collaborative Assessment and Management of Suicidality (CAMS) framework. Across 2,644 reference-annotated marker turns within 1,759 multi-turn AI evaluation runs (1,679 complete) spanning 31+ active models on 53 scenarios, 49% to 77% of marker turns received responses scoring at or below the inadequate threshold for transition recognition, depending on rubric version (combined inadequate-response rate 57%). Keywords: AI safety, clinical evaluation, suicide-risk detection, conversational AI, large language models, clinical rubric, evaluator drift, mechanical severity score, Salient Distress Model Methodology preprint. Implementation details (specific MSS calibrated weight values, verbatim TQC formula, verbatim score-pipeline rule, full clinical rubric anchor language, full notable_tags controlled vocabulary, scenario conversation scripts) are reserved as deployment-specific and are not disclosed in this preprint. Methodology subject of US Provisional Patent Application No. 64/059,837 (filed 2026-05-07 at USPTO). Provisional applications are confidential under 35 USC § 122 during the 12-month convention period; see https://www.uspto.gov/patents/basics/types-patent-applications/provisional-application-patent for general information about provisional applications.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · AI evaluator scores chatbot responses in suicide-risk dialogues and a human expert review interface exists, but whether LLM–human agreement is reported is unclear.

**Решение:** =

---

### 639 · R3446

**HEART: A Unified Benchmark for Assessing Humans and LLMs in Emotional Support Dialogue**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.19922

Supportive conversation depends on skills that go beyond language fluency, including reading emotions, adjusting tone, and navigating moments of resistance, frustration, or distress. Despite rapid progress in language models, we still lack a clear way to understand how their abilities in these interpersonal domains compare to those of humans. We introduce HEART, the first-ever framework that directly compares humans and LLMs on the same multi-turn emotional-support conversations. For each dialogue history, we pair human and model responses and evaluate them through blinded human raters and an ensemble of LLM-as-judge evaluators. All assessments follow a rubric grounded in interpersonal communication science across five dimensions: Human Alignment, Empathic Responsiveness, Attunement, Resonance, and Task-Following. HEART uncovers striking behavioral patterns. Several frontier models approach or surpass the average human responses in perceived empathy and consistency. At the same time, humans maintain advantages in adaptive reframing, tension-naming, and nuanced tone shifts, particularly in adversarial turns. Human and LLM-as-judge preferences align on about 80 percent of pairwise comparisons, matching inter-human agreement, and their written rationales emphasize similar HEART dimensions. This pattern suggests an emerging convergence in the criteria used to assess supportive quality. By placing humans and models on equal footing, HEART reframes supportive dialogue as a distinct capability axis, separable from general reasoning or linguistic fluency. It provides a unified empirical foundation for understanding where model-generated support aligns with human social judgment, where it diverges, and how affective conversational competence scales with model size.

**ИИ:** + · обе модели · LLM-судья · LLM-as-judge ratings of emotional-support responses on empathy and attunement rubric compared with blinded human raters (~80% agreement).

**Решение:** =

---

### 640 · R3447

**The cognitive, affective, and behavioral expression of self-stigma among people who use drugs in online substance use communities**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.25143

Objectives: To develop a codebook for self-stigma across cognitive, affective, and behavioral domains, and to estimate the prevalence, co-occurrence, and temporal patterns of these indicators in Reddit posts by people who use drugs. Methods: We developed a ten-indicator codebook through consensus-based abductive coding spanning cognitive (self-labeling, pessimism/self-defeatism, deservingness/worthlessness), affective (shame, guilt/self-blame, despair/hopelessness), and behavioral (concealment, anticipated rejection, desire to quit, ambivalence) domains; two coders reached substantial agreement (Cohen's k = 0.72). We then scaled classification with a large language model validated against expert coding (k = 0.73, F1 = 0.80), analyzing 72,115 thread-initiating posts from 1,660 English-language users (2006-2025). Results: 3,838 posts (5.3%) from 1,228 users (74.0%) contained self-stigma; all ten indicators discriminated self-stigma posts (RR 3.6 to 86.2), led by self-labeling (56.0%) and despair/hopelessness (48.5%). Self-stigma was integrated: core and behavioral indicators were strongly associated at the user level (OR = 4.65, 95% CI 3.12-6.94, p &lt; 0.001), and 87.0% of posts with behavioral indicators also contained a core indicator. Contrary to progressive models, behavioral indicators emerged earlier than core ones (desire to quit at median position 0.08 vs. shame at 0.38). Nine of ten indicators were stable across posting trajectories; only pessimism increased (OR = 1.62, 95% CI 1.25-2.10). Conclusion: Among people who use drugs online, self-stigma is an integrated phenomenon in which behavioral indicators rarely appear without internalized ones and often precede them. Most expressions remain stable over time, but pessimism about change deepens, marking a target for early digital intervention and showing that progressive stage models do not map directly onto textual disclosure.

**ИИ:** + · обе модели · кодирование по кодбуку · An LLM applied a self-stigma codebook to Reddit posts and was validated against expert coding (κ = 0.73, F1 = 0.80).

**Решение:** =

---

### 641 · R3454

**AI-first, expert-verified: validating generative AI for HFACS-based coding of healthcare RCA transcripts with governance considerations.**

2026 · International journal for quality in health care : journal of the International Society for Quality in Health Care · journal article, validation study, journalarticle · eng · https://doi.org/10.1093/intqhc/mzag045

BACKGROUND: Root cause analysis (RCA) is widely used in healthcare incident investigation, but its outputs can be limited by inconsistent causal framing and variable integration of human factors. The Human Factors Analysis and Classification System (HFACS) offers a structured taxonomy for causal attribution, yet manual coding is resource-intensive. Empirical validation of generative artificial intelligence (AI) for document-level HFACS coding from complete healthcare RCA transcripts remains limited. METHODS: We conducted a cross-sectional validation study at an 829-bed medical center in Taiwan. Thirty-five de-identified RCA interview transcripts (2024-5) with verbatim transcription were analyzed using SKH-AI, an in-house platform integrating an Azure OpenAI-hosted GPT-4o model with deterministic decoding (temperature = 0; top_p = 1.0). The model processed each transcript holistically to identify salient narrative segments and assign HFACS codes with evidence-linked rationales without rule-based post-processing. Outputs were compared with dual-expert HFACS coding with adjudicated consensus. Performance was assessed using precision, recall, micro-/macro-F1, and Cohen's κ with bootstrapped 95% confidence intervals. RESULTS: Across 562 AI-derived segments, micro-F1 was 0.66 [95% confidence interval (CI): 0.63-0.69] and macro-F1 was 0.68 (95% CI: 0.64-0.72), with moderate agreement versus expert coding (κ = 0.56, 95% CI: 0.52-0.60). Performance was higher for text-anchored categories (Level 2 Preconditions F1 = 0.70; Level 1 Unsafe Acts F1 = 0.69) than for more abstract domains (Level 3 F1 = 0.66; Level 4 F1 = 0.65). Subcategory analyses showed stronger detection of concrete cues (e.g. decision errors, physical environment, communication) and weaker performance for latent constructs (e.g. process management). Bias analyses indicated a recall-leaning tendency at Levels 3-4, consistent with increased over-attribution risk. CONCLUSIONS: Generative AI can produce auditable, evidence-linked candidate HFACS attributions from document-level RCA transcripts with moderate concordance to expert coding. Higher-level supervisory and organizational attributions remain vulnerable to overgeneralization and should be governed as decision support, with evidence-anchoring and mandatory expert sign-off for Level 3-4 codes.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o applied HFACS codes to RCA interview transcripts versus dual-expert coding (κ reported); human-factors codes (errors, mental states, communication) are borderline psychological.

**Решение:** =

---

### 642 · R3459

**Leveraging Large Language Models for Colorectal Cancer Symptom Extraction from MIMIC-IV Clinical Notes**

2026 · medRxiv · preprint, ppr, review · https://doi.org/10.64898/2026.09.15.26362961

Abstract Background Much of the symptom burden in colorectal cancer (CRC) patients is documented in unstructured discharge-note narrative, and manual extraction is not scalable. Whether large language models (LLMs) outperform rule-based and named entity recognition (NER) methods has not been rigorously benchmarked. Objective To benchmark rule-based, NER, and zero-shot LLM methods for extracting 46 cancer-related symptoms from CRC discharge notes against an adjudicated ground truth. Methods We analyzed 2,704 discharge notes from CRC patients in MIMIC-IV. A 46-symptom target list was built from the Memorial Symptom Assessment Scale and the EORTC QLQ-CR29. Four approaches -- dictionary-based rule matching, pretrained clinical NER, and zero-shot Claude Haiku and Gemini 3.5 Flash -- plus two hybrid variants (LLM output with post-hoc rule-based negation filtering) were evaluated against a 200-note gold standard adjudicated by two raters (pooled kappa=0.71, macro kappa=0.49), using Macro/Micro F1, precision, and recall. Results Gemini 3.5 Flash performed best (Macro F1=0.70, Micro F1=0.86, Macro Precision=0.74), followed by Claude Haiku (Macro F1=0.63, Macro Recall=0.71); both substantially outperformed rule-based (Macro F1=0.44) and NER (Macro F1=0.38) methods. Post-hoc negation filtering paradoxically degraded LLM performance (Gemini+Hybrid Macro F1=0.58; Claude+Hybrid Macro F1=0.54) by overriding correct predictions through rigid, fixed-window matching. Conclusions Zero-shot LLMs substantially outperform rule-based and NER approaches for CRC symptom extraction; post-hoc negation correction should not be applied to LLM outputs without syntactic scope validation. Implications for Practice: Zero-shot LLM extraction offers a scalable, accurate alternative to manual chart review and traditional NLP pipelines for oncology symptom surveillance, without institution-specific rule development or model training.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs extract oncology symptoms against adjudicated human labels; mostly physical, but the MSAS list may include psychological symptoms (sadness, worry, nervousness).); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs extract physical cancer symptoms from colorectal cancer discharge notes against adjudicated labels; this is medical oncology text, not a psychological construct.)

**Решение:** -

---

### 643 · R3460

**Integrating speech biomarkers and large language models for adolescent suicide risk detection with mobile application for real-world evaluation.**

2026 · Cell reports. Medicine · journal article, journalarticle, article · eng · https://doi.org/10.1016/j.xcrm.2026.102823

Summary Adolescent suicide is a significant public health issue, highlighting the need for efficient methods to detect suicide risk. Here, we develop and validate a speech-based suicide risk detection framework grounded in large language models (LLMs). Two independent cohorts of adolescents aged 10–18 years are analyzed: a development cohort (n = 1,223), with voice recordings collected in structured interview settings for model training and internal evaluation, and an external validation cohort (n = 460), collected through a mobile application to assess feasibility in naturalistic settings. An integrated model combining a speech encoder and an LLMs-based text-processing branch achieves its best performance on the self-introduction task. The model yields an accuracy of 0.808 and a macro-F1 score of 0.807 for suicide risk detection and remains effective under naturalistic mobile assessment. These findings support integrating LLMs with speech-derived markers for scalable adolescent suicide risk detection.

**ИИ:** разошлись — Opus -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): Speech plus LLM model predicts adolescents' suicide risk status from recordings; the reference is participant risk status, not human coding of the same texts.); Sonnet ? (неясно, кто ставил эталонные метки: LLM plus speech model detects adolescent suicide risk; reference labels likely from questionnaire or interview, and an LLM-versus-human coding comparison is unclear.)

**Решение:** -

---

### 644 · R3468

**Creativity Is Not an Outcome: A Process-Based Framework for Mapping Individual Creative Contributions in Human–LLM Collaboration**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.6910509

If large language models (LLMs) are reshaping creative contributions in collaboration, the dominance of outcome-based creativity evaluation may obscure these changes by capturing only the final product. This makes it hard to determine whether LLMs support or displace human creative effort. To address this, we introduce a computational framework for tracking human creative contributions during live brainstorming dialogues. Using Observable Creative Sense-Making (OCSM), we operationalize participation, novelty, and appropriateness via computational semantic and linguistic measures evaluated against expert ratings. These enable turn-by-turn analysis of how contributions evolve, offering granularity that static benchmarks lack. In a between-subjects design, we compare creative behavior, subjective experience, and emotional trajectories of participants brainstorming with a human or an LLM. Results show LLM collaboration leads to greater idea divergence and exploration but lower participation and appropriateness. Human–human collaboration demonstrates stronger participation, contextual grounding, and cumulative idea development. Participants collaborating with an LLM also reported less positive experiences and lower confidence in collaborative outcomes. These findings reveal that different partners support different creativity dimensions - tradeoffs invisible to outcome-based assessments. By showing how creative contributions emerge and evolve, our framework helps identify where human creative effort is amplified, redistributed, or diminished. This visibility enables the design of conversational AI systems that strengthen human creative engagement instead of shifting effort away from human collaborators. More broadly, our framework provides a foundation for benchmarking creative contributions, identifying gaps in human–AI collaboration, and evaluating how AI technologies shape human creative potential over time.

**ИИ:** разошлись — Opus ? (другое: Computational novelty/appropriateness measures of brainstorming turns were validated against expert ratings; unclear whether an LLM did the scoring rather than embeddings.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): Framework uses computational semantic/linguistic measures validated against expert ratings, not an LLM coding texts compared with human coders; LLM is a brainstorming partner.)

**Решение:** -

---

### 645 · R3469

**Large language models for depression severity assessment**

2026 · DSpace - NTUA (National Technical University of Athens) · other/other, article · https://doi.org/10.26240/heal.ntua.33604

Εθνικό Μετσόβιο Πολυτεχνείο--Μεταπτυχιακή Εργασία. Διεπιστημονικό-Διατμηματικό Πρόγραμμα Μεταπτυχιακών Σπουδών (Δ.Π.Μ.Σ.) "Μεταφραστική Βιοιατρική Μηχανικής και Επιστήμης"

**ИИ:** ? · обе модели · нет аннотации · Master's thesis on LLM depression severity assessment; no real abstract, reference could be clinician ratings or self-report.

**Решение:** =

---

### 646 · R3472

**Benchmarking large language models against practicing clinicians on psychopathological assessment.**

2026 · NPJ digital medicine · journal article, journalarticle, review · eng · https://doi.org/10.1038/s41746-026-02852-7

Psychiatry's reliance on language makes LLMs a natural tool for psychopathological assessment, yet structured, item-level assessments from psychiatric clinical interviews remain under-researched. In this proof-of-concept study, 10 LLMs assessed transcripts of three simulated psychiatric interviews across all 100 items of the Association for Methodology and Documentation in Psychiatry (AMDP) system, benchmarked against 108 early-career clinicians rating full audiovisual recordings, using an expert consensus panel as reference. GPT-5.1 and Gemini-3-Pro-Preview achieved the highest accuracy (0.72; 64th percentile of the clinician distribution) using majority voting across three runs with AMDP definitions as context. GPT-5.1, selected for a marginal advantage, showed per-scenario accuracies of 0.81 (depression), 0.76 (mania), and 0.60 (schizophrenia) versus clinician means of 0.79, 0.68, and 0.58. Clinicians and LLMs showed distinct error profiles: clinicians tended to over-infer symptom presence, whereas LLMs more conservatively flagged items as "not assessable" - most pronounced for observation-dependent items but present even for text-assessable items (19.4% vs. 11.4%, p < 0.001). In post hoc simulated disagreement resolutions (2091 clinician pairs; 35.5% disagreements), LLM and board-certified supervision were associated with more accurate resolutions than unsupervised random clinician selection (p < 0.0002). These proof-of-concept findings require validation in real patient interviews, larger samples, and prospective studies integrating multimodal input.

**ИИ:** + · обе модели · клиническая оценка · 10 LLMs rated AMDP psychopathology items from psychiatric interview transcripts; accuracy compared against an expert consensus panel and clinician ratings.

**Решение:** =

---

### 647 · R3499

**Measuring Depression Severity With Clinical Global Impression-Severity Scale Scores From Clinical Notes Using Large Language Models: Validation Study.**

2026 · JMIR formative research · journal article, validation study, research support, non-u.s. gov't · eng · https://doi.org/10.2196/86906

Abstract Background Real-world psychiatric care is marked by wide heterogeneity in clinical presentations and outcomes, underscoring the need for systematic approaches to outcome measurement. The Clinical Global Impression–Severity (CGI-S) scale is a brief, clinician-rated measure of overall illness severity that is widely used in psychiatric research, but rarely documented in routine care. Large language models (LLMs) may enable automated extraction of CGI-S scores from narrative clinical notes, thereby providing scalable outcome measures for real-world clinical care and research. Objective The study aimed to evaluate whether LLMs can estimate CGI-S scores from psychiatric clinical notes for patients with major depressive disorder (MDD) and to compare performance across prompting strategies and model architectures. Methods We extracted psychiatrist-authored notes from the Johns Hopkins electronic health record. Three board-certified psychiatrists independently rated 77 clinical notes using a validated depression-specific Clinical Global Impression (CGI) rubric. Weighted Cohen kappa coefficients were calculated to assess inter-rater reliability and model-human agreement. We evaluated GPT-4o under zero-shot and few-shot prompting conditions and Llama-4 under zero-shot prompting. Model performance was assessed by comparing LLM-generated scores to individual rater scores and consensus ratings. Exploratory analyses evaluated whether agreement varied by patient demographics, care setting, note length, or the percentage of copy-forwarded text within each note. Results Interrater reliability among psychiatrists was high (κ=0.77‐0.78). GPT-4o with zero-shot prompting demonstrated the highest agreement with average human ratings (κ=0.85, 95% CI 0.78-0.90), and few-shot prompting did not improve performance. In contrast, Llama-4 with zero-shot prompting demonstrated lower agreement with average human ratings (κ=0.70, 95% CI 0.55‐0.80). Model agreement did not significantly differ across age, sex, race, treatment location, or the percentage of copy-forwarded text, but it was significantly lower for notes below the median note length than for notes at or above the median length (κ=0.72 vs 0.92; P=.003). Conclusions LLMs can estimate clinician-rated CGI-S scores from psychiatric clinical notes for patients with MDD at a level of agreement comparable to that of expert interrater reliability. Performance varied by model architecture, with GPT-4o outperforming an open-source alternative. If further validated, this approach may support scalable outcome measurement in research settings and inform future efforts to implement measurement-based care in real-world psychiatric practice.

**ИИ:** + · обе модели · клиническая оценка · GPT-4o and Llama-4 rated CGI-S depression severity from psychiatric notes; weighted kappa reported against three psychiatrists' ratings.

**Решение:** =

---

### 648 · R3515

**Integrating Large Language Models into Qualitative Methods in Health Services Research: A Proof-of-Concept Study (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.93253

BACKGROUND Qualitative methods are widely used in health services research to understand human experiences and contextual factors. Traditional qualitative methods are valued for their depth of interpretation and ability to derive context-specific insights. Manual coding, a foundational technique in rigorous qualitative methods, is highly resource and time-intensive and difficult to scale up. Natural Language Processing (NLP), specifically Large Language Models (LLMs), have shown potential to enhance efficiency in qualitative analysis. However, there is limited research providing guidance and methodology for determining how best to integrate LLMs while maintaining rigor and trustworthiness of results. Specifically, methodologies are needed in which researchers are in conversation with the text and can review results for credibility. OBJECTIVE In this proof-of-concept study, we propose, apply, and evaluate a method using LLMs for automated coding, and present a use case specific to health services research. METHODS We analyzed 22 interviews among public health officials, law enforcement, community organizers, and medical professionals at one county in the State of California to examine existing service gaps and needs. A primarily deductive codebook was iteratively refined until two coders achieved an inter-coder reliability (ICR) > 0.95 and was applied to the transcripts using ATLAS.ti. We developed an NLP-assisted method that uses a semantic shift algorithm to segment transcripts which are then passed to GPT-4 for code assignment and explanation using the codebook and coding guidelines developed during the manual process. We conducted both a quantitative assessment of agreement between human coders and the NLP-assisted method, and a qualitative assessment of the soundness of the codes assigned by the NLP-assisted method. RESULTS The NLP-assisted method had moderate agreement with human coding (modified pooled Cohen’s Kappa = 0.66), and 71.8% of codes were rated as sound by reviewers. Sound codes were more often observed for high-certainty and straightforward codes, and when text chunks were semantically well defined. The NLP-assisted method had more difficulty with non-linear conversation and entity-dependent codes. Coding time was reduced significantly from ~40 hours for the traditional method to ~1 hour for the NLP-assisted method. CONCLUSIONS These findings suggest that LLMs can be effectively incorporated into qualitative processes while maintaining rigor if humans are embedded into the process. By maintaining a human-in-the-loop workflow, our methodology allows for researchers to maintain familiarity with the data, define the research question(s) and codebook, and determine if there are results that are not sound. By incorporating LLMs into the coding stage of the process, key limitations of traditional qualitative methods can be addressed, such as scalability, and resource and time limitations.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 applied a codebook to interview transcripts and was compared with human coders (κ=0.66), but the topic of service gaps may not be psychological.

**Решение:** =

---

### 649 · R3526

**Fine-Tuning Large Language Models for Codebook-Guided Coding of Students' Mathematics Metaphor Responses**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.10276

Student-generated metaphors about mathematics can provide insights into students' attitudes, beliefs, identities, and experiences, but expert human assessment through thematic coding of these semantically complex metaphor responses is labor-intensive and difficult to scale. This study examines whether Low-Rank Adaptation (LoRA)-based supervised fine-tuning of Large Language Models (LLMs) can improve their performance on codebook-guided coding tasks for student mathematics metaphors. We utilized a human-coded corpus of 2,265 Grade 6-8 responses to food- and animal-based metaphor prompts and evaluated LLMs on two tasks: valence-intensity coding of students' affective orientations toward mathematics and thematic coding of their metaphorical framings of mathematics. Two open-weight LLMs, DeepSeek-R1 1.5B and Mistral 7B, were evaluated before and after fine-tuning and compared with two proprietary LLMs, GPT-4o mini and GPT-5 mini. Results show that fine-tuning substantially improved the performance and run-to-run reliability of the open-weight LLMs across both tasks relative to their base versions, making the fine-tuned LLMs competitive with and often outperforming the proprietary LLMs. These findings suggest the potential of fine-tuned open-weight LLMs for scalable and automated AI-assisted measurement of students' metaphor responses with competitive performance while maintaining local controllability and privacy-conscious deployment.

**ИИ:** + · обе модели · кодирование по кодбуку · LLMs apply a codebook to students' metaphor responses for affective valence and themes, evaluated against human-coded corpus.

**Решение:** =

---

### 650 · R3535

**Automated Fidelity Monitoring of Lay-Delivered Mental Health Interventions Using Large Language Models: Development and Pilot Validation of shamiriAI in Kenya.**

2026 · JMIR AI · journal article, journalarticle, article · eng · https://doi.org/10.2196/95063

Abstract Background Task-shifting can help close the mental health treatment gap in low- and middle-income countries, but its effectiveness depends on ongoing supervision, which is hard to scale. AI tools that process session recordings and generate structured fidelity feedback could offer a scalable alternative; yet, to our knowledge, none have been developed or validated for lay-delivered, multilingual, group-format interventions in low-resource settings. Objective We developed and pilot-validated shamiriAI (ShamiriAI Institute), an automated fidelity-monitoring tool for lay-delivered mental health interventions, embedded within the Shamiri school-based program in Kenya. Methods Across 6 secondary schools in Ngong Hub, Kajiado County, Kenya (May-September 2025), shamiriAI processed session audio from 47 lay providers through a 5-stage pipeline: ingestion, multilingual automatic speech recognition (ASR) with prosodic feature extraction, personally identifiable information scrubbing, large language model–based fidelity inference, and supervisor reports. The following two aims were assessed: (1) ASR performance on a held-out test set of manually transcribed sessions and (2) interrater reliability between shamiriAI and independent human supervisor ratings across 52 sessions (38 AI-augmented and 14 standard) on 6 domains (Required Contents, Specifics, Thoroughness, Clarity, Skill, and Purity; 1‐7 scale). Reliability used intraclass correlation coefficients, Bland-Altman analysis, adjacent-agreement rates, paired t tests with Holm-Bonferroni correction, and Gwet AC2 (ordinal weights) across 3 formulations of the human reference. Results The ASR model achieved a character error rate of 0.19, word error rate of 0.34, and cosine semantic similarity of 0.77, indicating strong meaning preservation in code-switched speech. AI fidelity scores were systematically lower than the human composite overall (mean 5.14, SD 0.77 vs mean 5.93, SD 0.57 ); Δ=−0.79; d=−1.16; P<.001). Primary intraclass correlation coefficients ranged from −0.06 to 0.20 across the 6 domains, and AC2 sensitivity analyses (against each individual rater and the rounded composite) corroborated this dimension-level ordering. Three patterns emerged: large systematic underrating on holistic dimensions (Required Contents: d=−3.48; Clarity d=−1.56); bidirectional medium-effect bias on facilitation dimensions (Thoroughness d=−0.99; Skill d=+0.87); and substantial agreement on Specifics, Skill, and Purity (Gwet AC2 0.69‐0.76 against the rounded composite), relative to a human-human AC2 ceiling of 0.42‐0.60 estimated in the same dataset. Exploratory, underpowered subgroup and per-arm checks found no preliminary evidence of bias by lay-provider sex or age band or of arm-level differences. Conclusions Within this 52-session pilot, shamiriAI shows technically feasible multilingual ASR and a coherent, dimension-dependent reliability profile. Specifics, Purity, and Skill already reach substantial agreement, while underperformance on holistic dimensions (Required Contents and Clarity) reflects diagnosable misalignments in rubric interpretation and prompt design, specifying a concrete agenda for shamiriAI (version 2; Shamiri Institute). Whether AI-augmented supervision improves provider skill or student mental health outcomes will be tested in a planned cluster-randomized noninferiority trial.

**ИИ:** + · обе модели · кодирование сессий · LLM rated fidelity of lay-delivered intervention sessions on 6 domains; compared with human supervisor ratings using ICC and Gwet AC2.

**Решение:** =

---

### 651 · R3548

**One Month of Personality Functioning in Adolescence: Understanding Self-Concept Clarity and Interpersonal Experiences using a Large Language Modelling Daily Diary Approach**

2026 · OSF Preprints (OSF Preprints) · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/kxdps

The formation of a coherent, relatively stable, and positive sense of self represents a central developmental task of adolescence, during which the underlying mechanisms of self-concept evolve considerably (Crone et al., 2022). Self-concept clarity (SCC)—the extent to which individuals view themselves in a clear, consistent, and stable way over time (Campbell et al., 1996)—is an important indicator of healthy identity development (Branje et al., 2021). Low levels of SCC reflect what clinical theories describe as identity diffusion, a state of confusion or instability in one’s sense of self that is often linked to personality pathology (Uliaszek et al., 2022). Developmental cascade models propose that personality pathology emerges gradually, through accumulating difficulties in mastering age-salient developmental tasks and increasing dysregulation over time (Lyons-Ruth &amp; Brumariu, 2021). During adolescence, identity formation and growing social autonomy constitute key developmental domains that are theoretically and empirically intertwined with personality functioning (Iannattone et al., 2024; Sharp, 2020), the hallmark of personality pathology diagnosis according to recent adaptations in diagnostic systems (DSM-5; American Psychiatric Association, 2013; ICD-11; World Health Organization, 2021). Arguably, self-concept development is an inherently social process with youth being particularly sensitive to environmental experiences including affirmative and rejecting social responses (Crone et al., 2020; Sharp &amp; Wall, 2018; Sisk &amp; Gee, 2022). Emerging research supports trait and state-like aspects of an individual's SCC, with short-term fluctuations at rather short time-scales linking to fluctuations in other self-relevant processes in daily life such as negative affect or self-harm intentions (Ellison et al., 2022; Nielsen et al., 2024). Longitudinal research finds youth’s more adaptive day-to-day coordination of identity processes at the within-person level to translate into an increasingly coherent identity during young adulthood (Becht et al., 2021). To better understand the contextual drivers of this maturation, research needs to integrate short-term fluctuations in SCC with youth’s daily experiences (Branje, 2022). An important question in examining idiographic processes in interpersonal context is how the latter can be validly assessed in daily life. This might be particularly important when studying processes relevant to SCC, which reflects the degree of (in)coherence in what individuals believe to be true about themselves, a factor that may also impact other-perception (De Cuyper et al., 2017). The convergence of similar patterns across different methods or data types is essential for increasing confidence in empirical findings. Narrative data from open-ended questions allow individuals to express what they consider important, in their own language, and about situations that matter to them, which enriches and sometimes even deviates from what can be assessed via questionnaire data (Truijens et al., 2019). Recent studies have shown that large language models (LLMs) can effectively support automated psychological text analysis, detecting psychological constructs in ways comparable to human raters across rating formats, text types, and languages (López-Pérez et al., 2025; Rathje et al., 2024; Wright et al., 2025). This offers opportunities for cross-linguistic research and the processing of vast amounts of narrative data valuable to personality pathology research because it allows an integrated assessment of similar constructs across different data sources (e.g. diary entries, voice recordings) sampled in relevant situations (e.g. after social interactions, within therapy sessions). In the present study, we aim to examine how social experiences link to day to day fluctuations in self-concept clarity and how these fluctuations relate to emerging personality pathology. We integrate adolescents’ self-ratings with narrative daily diary entries analyzed using large language models (LLMs) to characterize their daily interpersonal experiences and examines how these relate to fluctuations in self-concept clarity (SCC). A sample of ethnically diverse youth (ages 14-21) provided daily ratings of SCC and interpersonal experiences and open-ended diary entries describing their most recent social encounter over 29 days. Alongside youth self-reports, we will locally run state of the art LLMs to extract key interpersonal constructs— including invalidation of the participant as well as perceived warmth and dominance in the interaction partners’ behavior —from narrative data. We compare convergence between LLM-derived ratings and human ratings as well as associations with a set of youth reported affective and behavioral indicators to examine validity. Using dynamic structural equation modeling (DSEM), we test whether daily SCC and interpersonal stress (self-/LLM-rated) are reciprocally associated with each other. We also examine whether baseline maladaptive traits moderate these processes, amplifying vulnerability to negative interpersonal experiences and reactivity in SCC. Findings are expected to advance understanding of (1) the utility of LLMs in extracting interpersonal constructs from brief daily narratives and (2) the daily unfolding of processes that may contribute to the development of personality pathology in youth.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: Pre-registration/protocol (future tense) planning LLM vs human ratings of diary interpersonal constructs; no results yet. Track for later full report.); Sonnet ? (другое: Preregistration of a study comparing LLM and human ratings of adolescent diary narratives (invalidation, warmth, dominance). It fits the topic, but it may be a protocol with no results.)

**Решение:** -

---

### 652 · R3550

**A C-SSRS-Based Risk-Aware Evaluation Framework for Self-Harm Safety in LLMs**

2026 · International Conference on Artificial Intelligence Testing · conference, conference-paper · https://doi.org/10.1109/aitest70988.2026.00035

Automated red teaming is important for evaluating the safety of large language models (LLMs), particularly in user-facing environments where adversarial failures may have serious consequences. However, current self-harm safety evaluation does not adequately account for input-risk variability, partial harmful leakage, or crisis-intervention quality. To address these limitations, this paper proposes a C-SSRS-based, risk-aware evaluation framework for self-harm safety in LLMs. The framework combines input-side risk stratification based on C-SSRS with multidimensional output-side evaluation using attack success rate (ASR), leakage score (LS), and crisis intervention degree (CID), while incorporating PAIR for iterative adversarial stress testing. Experimental results show that higher-risk prompts are more sensitive and discriminative for adversarial safety evaluation, and that even when ASR remains zero or similarly low, models may still differ substantially in partial harmful leakage and crisis-intervention quality. Among the evaluated models, Claude maintains the most stable safety profile with minimal harmful leakage, whereas ChatGPT shows relatively stronger crisis-intervention quality under attack. Cross-judge validation on frozen completions provides preliminary support for the robustness of the proposed LS/CID evaluation. These findings suggest that binary safe/unsafe judgments alone are insufficient to characterize self-harm safety and highlight the importance of C-SSRS-based, risk-aware, and multidimensional evaluation for exposing model vulnerabilities in self-harm scenarios.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM judges rate self-harm leakage and crisis-intervention quality; the cross-judge validation may be LLM–LLM only, and human ratings are unclear.

**Решение:** =

---

### 653 · R3560

**Assessing Suicide Risk in Arabic Crisis Helpline Calls: A Comparison of Arabic and English Large Language Models**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.00191

Crisis helplines assess suicide risk through structured interviews, a process that is slow and dependent on operator training and workload. Natural language processing could support risk assessment and call prioritization, but almost no work addresses Arabic-language helpline calls or operates within the privacy constraints of real helpline data. We analysed de-identified transcripts from Lebanon's National Lifeline for Emotional Support and Suicide Prevention. Audio never left the helpline: calls were transcribed on site with a speech recognition model for Levantine Arabic, and an Arabic named-entity recognition model removed identifying information locally. Only the de-identified transcripts were shared with the research team. Operators recorded the five suicidal ideation items of the Columbia Suicide Severity Rating Scale, which we combined into two binary outcomes: at-risk and high-risk. We also machine-translated the transcripts into English, giving a paired Arabic/English comparison. On each corpus, we fine-tuned five instruction-tuned large language models alongside six transformer encoder baselines (four Arabic, two English) and evaluated all models on a held-out test set. We included 383 calls: 373 for the at-risk task (52.3% positive) and 297 for the high-risk task (30.0% positive). The best Arabic model reached a macro-F1 of 81.19 and a ROC-AUC of 90.61 on high-risk; the best English model reached 85.00 and 92.59, identifying 88.9% of high-risk calls. In both languages, high-risk calls separated more cleanly than at-risk calls, and translation to English did not reduce the best observed performance. Suicide risk can be classified from de-identified Arabic transcripts without sending audio outside the helpline. The high-risk results support further testing as an operator-facing tool; lower-severity ideation proved the harder case.

**ИИ:** разошлись — Opus + (клиническая оценка: Fine-tuned LLMs classify suicide risk from helpline transcripts against operators' C-SSRS ratings made during the same calls; F1 and AUC reported.); Sonnet ? (неясно, кто ставил эталонные метки: Fine-tuned LLMs classify suicide risk in helpline transcripts against operator-recorded C-SSRS items; unclear whether these count as human coding of the text or a structured-interview outcome.)

**Решение:** +

---

### 654 · R3572

**Analyzing Generative AI and Machine Learning in Auto-Assessing Schizophrenia's Negative Symptoms.**

2026 · Schizophrenia bulletin · journal article, journalarticle, article · eng · https://doi.org/10.1093/schbul/sbaf102

BACKGROUND AND HYPOTHESIS: Traditional assessments of schizophrenia's negative symptoms rely on subjective and time-consuming psychiatric interviews. To provide more objective and efficient evaluations, this study examines the efficacy of an automated system utilizing generative AI (GenAI) and machine learning (ML) to assess negative symptoms of schizophrenia, including expression (EXP) and motivation and pleasure (MAP) domains. STUDY DESIGN: A semi-structured interview protocol based on the Clinical Assessment Interview for Negative Symptoms was used to conduct interviews with schizophrenia patients. An experienced senior psychiatrist carried out these interviews, which were audio- and video-recorded, at the National Taiwan University Hospital between July 2022 and August 2023. An ML-based system analyzed visual and audio data for EXP assessment, while GenAI analyzed interview transcripts for MAP assessment. STUDY RESULTS: The study cohort consisted of 69 males and 91 females with a mean age of 41.68 years (SD = 10.46). The ML-based EXP assessment showed moderate to substantial reliability, with an intraclass correlation coefficient (3, 1) (ICC3,1) of 0.65 and a weighted kappa of 0.62. The GenAI-based MAP assessment demonstrated good reliability, with an ICC3,1 of 0.82 and a weighted kappa of 0.77. The system achieved strong linear correlations with clinician ratings (Pearson's correlation coefficient ≥ 0.54) and maintained low error rates (mean absolute error ≤ 0.81; root mean square error ≤ 1.16) for each assessment item. CONCLUSIONS: The study demonstrates the efficacy of GenAI and ML in the automated assessment of schizophrenia's negative symptoms, highlighting their potential to enhance the consistency and efficiency of clinical evaluations.

**ИИ:** + · обе модели · клиническая оценка · Generative AI rated CAINS motivation and pleasure items from interview transcripts; agreement with psychiatrist ratings reported (ICC 0.82, weighted kappa 0.77).

**Решение:** =

---

### 655 · R3573

**Associated Factors of Depressive Expression in Social Media During Emergencies: An LLM-Based Analysis.**

2026 · Psychological reports · journal article, med, journalarticle · eng · https://doi.org/10.1177/00332941261473851

Emergencies not only affect economic development and social stability but also pose serious challenges to the physical and mental health of the public. Depression is one of the most common chronic mental disorders following such events. However, few studies have explored the factors associated with depressive expression during emergencies. This research focuses on three core dimensions: cognitive appraisal, emotional response, and individual traits. It examines how perceived susceptibility, perceived severity, anxiety, sadness, self-focused attention and psychological resilience are associated with depressive expression levels. Unlike conventional approaches, this study employs a fine-tuned large language model (LLM) to detect depressive expression from social media data and aggregates the identified signals into hourly indicators for longitudinal regression analysis. Built on ChatGLM3 and manually annotated Weibo posts, the fine-tuned LLM has shown strong performance in Chinese social media depression recognition. The results show that these variables are significantly associated with depressive expression. Specifically, perceived susceptibility, perceived severity, anxiety, sadness, and self-focused attention function as risk factors, while psychological resilience serves as a protective factor. Our findings deepen the understanding of factors associated with depressive expression during crises and offer theoretical and empirical foundations for dynamic mental health monitoring and timely intervention.

**ИИ:** разошлись — Opus + (проверка кодирования внутри исследования: Fine-tuned ChatGLM3 detects depressive expression in Weibo posts; its performance is reported against manually annotated posts.); Sonnet ? (неясно, сравнивали ли с людьми: Fine-tuned ChatGLM3 on manually annotated Weibo depression posts; likely reports performance against human labels, but the main study is a regression analysis, so the validation is unclear.)

**Решение:** +

---

### 656 · R3574

**Cyberbullying victimization identification and large language model-assisted assessment: a study of cyberbullying victimization lexicon construction and validation.**

2026 · Frontiers in psychiatry · journal article, journalarticle, article · eng · https://doi.org/10.3389/fpsyt.2026.1826042

Introduction Cyberbullying poses a global mental health threat, yet its accurate identification remains challenging due to biases in self-reporting and help-seeking barriers. Methods Based on large-scale social media data, the present study constructed a Chinese cyberbullying victimization lexicon from three dimensions—cyberbullying methods (the types of cyberbullying experienced by the individual), perceived harm (the harm perceived by the victim), and coping strategies (the behavioral responses adopted by the victim)—using Weibo texts, psychological lexicons, and cyberbullying questionnaires. This approach aims to improve the precision of victim identification and facilitate timely intervention. Lexicon validity was evaluated by examining correlations between word-frequency statistics derived from 500 Weibo posts and expert ratings (n = 3). In addition, based on 3,442 RedNote posts, we preliminarily explored the lexicon's cross-platform applicability. To assess whether DeepSeek-R1 and GPT-4o could function as research assistants in dictionary construction, the present study replicated the manual lexicon development process—including text classification, vocabulary screening, weight assignment, and victimization severity assessment—and compared model outputs with human evaluations under simple and complex prompts using Cohen’s Kappa, intraclass correlation coefficients (ICC), recall, and precision. Results (1) The lexicon comprised 442 words across three dimensions: cyberbullying methods, perceived harm, and coping strategies. The lexicon demonstrated strong validity in identifying cyberbullying victimization expressions in social media text across each of the three sub-dimensions and the overall dimension (cyberbullying methods: r=0.500, p &amp;lt; 0.001; perceived harm: r =0.408, p &amp;lt; 0.001; coping strategies: r =0.509, p &amp;lt; 0.001; overall cyberbullying victimization expression: r = 0.870, p &amp;lt; 0.001), and effectively assessed the degree of cyberbullying victimization ( r = 0.533, p &amp;lt; 0.001); (2) While DeepSeek-R1 performed well on small-scale text classification (Kappa = 0.775–0.781), both models showed significant limitations in large-scale processing (12,600 entries). Vocabulary selection and weight assignment tasks revealed substantial discrepancies with human evaluation (Kappa as low as -0.874), though DeepSeek-R1 achieved moderate consistency in dimension partitioning (Kappa = 0.780). Discussion As the first Chinese cyberbullying victimization dictionary, this research demonstrates that large language models offer preliminary utility in structured tasks but require human oversight for complex, large-scale research phases, supporting a human-machine collaborative approach for optimal outcomes.

**ИИ:** + · обе модели · кодирование по кодбуку · DeepSeek-R1 and GPT-4o classified Weibo posts on cyberbullying victimization and rated its severity; compared with human ratings using Kappa and ICC.

**Решение:** =

---

### 657 · R3584

**Explainators at PsyDefDetect: Hierarchical Prompting and Representation-Based Classification for Psychological Defenses**

2026 · Proceedings of the BioNLP 2026 (Shared Tasks) · conference-paper · https://doi.org/10.18653/v1/2026.bionlp-2.16

Psychological defense detection is one of essential present-day challenges in clinical practice. The state-of-the-art natural language processing (NLP) tools aim to automate this task. However, their potential and efficiency remain largely unexplored. This manuscript attempts to address this problem from various perspectives: it first explores the efficiency of direct large language model (LLM)-prompting. Then, it applies NLP techniques for LLM fine-tuning applied to the psychological defense classification task. Finally, it attempts to generate states of mind based on the speaker’s psychological state. The results show that the complexity of the task requires further improvement of the software solutions used.

**ИИ:** + · обе модели · бенчмарк с метками людей · Shared-task paper: prompted and fine-tuned LLMs classify psychological defense mechanisms in dialogue, likely against expert-annotated labels.

**Решение:** =

---

### 658 · R3598

**Extracting Symptoms of Psychotic Disorders from Clinical Notes using Natural Language Processing**

2026 · medRxiv · preprint, ppr · https://doi.org/10.64898/2026.09.16.26363090

Abstract Large Language Models (LLMs) are proposed as tools for high-throughput, deep phenotyping of psychiatric disorders. Applied to electronic health records, LLMs could in principle extract patient symptoms, outcome trajectories, risk factors, and treatment history at scale and these, when combined with increasingly available biological data, such as genomics or neuroimaging, could provide powerful resources for health research. Although proof-of-principle LLM-based symptom extractions have been carried out for some medical conditions, the heterogeneous nature of psychiatric disorders, including schizophrenia, requires extensive domain-specific evaluations. Here, we evaluate 14 general-purpose LLMs for extracting eight symptoms of schizophrenia from clinical summaries in a severe mental illness cohort (N = 704). Performance across symptoms was poor to moderate (macro F1 = 0.500 – 0.647), with positive symptoms more accurately extracted than negative symptoms. Few-shot prompting, a common strategy for improving LLM task performance, did not significantly improve these results. Nevertheless, LLM-predicted and gold-standard positive symptoms demonstrated comparable associations with clinical variables in regression analyses. Individual-level extraction errors attenuated group-level associations but did so unevenly across symptom domains. This indicates that general-purpose LLMs may not be able to extract psychosis-related phenotypes from clinical summaries with the quality required for clinical use but might nevertheless be useful for exploratory research on large cohorts. However, closing the performance gap between positive and negative symptom extractions seems essential groundwork to prevent a systematic bias in any LLM-derived characterisations of psychotic symptoms.

**ИИ:** + · обе модели · клиническая оценка · 14 LLMs extract schizophrenia symptoms from clinical summaries, scored against gold-standard symptom labels (F1); the gold standard is probably human-coded.

**Решение:** =

---

### 659 · R3599

**Human versus machine: A comparative analysis of qualitative coding by humans and ChatGPT-4.**

2026 · School psychology (Washington, D.C.) · comparative study, journal article, med · eng · https://doi.org/10.1037/spq0000715

Generative artificial intelligence (AI) applications are becoming increasingly influential in psychology training, practice, and research. In this study, the procedures (e.g., coding process) and products (e.g., codes, categories, themes, core story) of a qualitative content analysis (QCA) conducted by Chat Generative Pre-trained Transformer (ChatGPT)-4 and novice human researchers were compared, and advantages and disadvantages of each approach were considered. Data included open-ended survey responses from trainers ( N = 60) in school psychology programs regarding assessment practices during the COVID-19 pandemic. Findings indicated that ChatGPT-4 conducted QCA with products that were similar, overall, to human coders and in significantly less time. However, ChatGPT-4's process was not transparent, and some codes and themes were unclear. Meanwhile, human coding allowed for the selection and implementation of a purposeful, coherent methodological approach and an auditable and systematic process resulting in defensible themes. Considerations for the use of AI in qualitative research are considered and discussed, and future research directions are provided. (PsycInfo Database Record (c) 2026 APA, all rights reserved).

**ИИ:** ? · обе модели · другое · ChatGPT-4 vs human qualitative content analysis of open-ended survey responses; the comparison may be only at theme level, and the psychological construct is borderline.

**Решение:** =

---

### 660 · R3626

**Using large language models to create lexicons for interpretable text models with high content validity: The suicide risk lexicon.**

2026 · Journal of psychopathology and clinical science · journal article, journalarticle, review · eng · https://doi.org/10.1037/abn0001152

Researchers often want to measure a variety of constructs such as anxiety, discrimination, or loneliness in text data from surveys, interviews, social media, and electronic health records. Using large language models (LLMs) --while optimal for text classification-- remain infeasible for some researchers due to concerns around computational expertise, cost, privacy, and compute requirements. Therefore, some researchers prefer to use lightweight models for large datasets or interpretable models to avoid mistakes in high-stakes scenarios such as suicide risk detection. Lexicons offer simple baselines to LLMs by searching for relevant phrases --and can be used together with LLMs to guarantee capturing specific keywords in a deterministic way. However, building new lexicons is resource intensive. In this study, we found that GPT-4 turbo was able to automatically create a lexicon for 49 known risk factors for suicidal thoughts and behaviors, which we release as the Suicide Risk Lexicon. Generating a lexicon with LLMs quickly measures most constructs relevant for suicide risk detection, resulting in high content validity. This lexicon was able to accurately predict risk in crisis counseling conversations. After validating the lexicon with clinician ratings, the lexicon modestly outperformed the LIWC lexicon --which has low content validity for mental illness-- and performed similarly to some black-box deep learning models. Due to using an interpretable approach with high content validity, we discovered that active suicidal ideation and direct self-injury were stronger indicators of imminent risk than passive suicidal ideation and depressed mood in this ecological setting (i.e., naturalistic counseling conversations as the crisis is happening, as opposed to assessments or interviews about retrospective symptoms). To simplify creating new lexicons for other research domains, we introduce a Python package, construct-tracker, that works with a variety of LLMs. In sum, while we recommend using LLMs for text classification, they remain out of reach for many researchers. Our work demonstrates that LLMs --despite being black-boxes-- can counterintuitively create interpretable models by generating lexicons, when this is preferred. However, more studies are needed to test how these methods generalize to other datasets and psychological domains. Furthermore, we highlight the broader application of lexicons beyond measurement, including their use in benchmarking LLM performance.

**ИИ:** разошлись — Opus ? (другое: GPT-4 generates a suicide-risk lexicon checked by clinicians; unclear whether any LLM directly coded crisis texts against human risk labels.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: GPT-4 generates a suicide-risk lexicon; the lexicon, not the LLM, is validated against clinician ratings, so the LLM does not code the texts.)

**Решение:** -

---

### 661 · R3633

**VERA-MH: Validation of Ethical and Responsible AI in Mental Health**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.13318

Chatbot usage has increased, including in fields for which they were never developed for--notably mental health support. To that end, we introduce Validations of Ethical and Responsible AI in Mental Health (VERA-MH), a novel clinically-validated evaluation for safety of chatbots in the context of mental health support. The first iteration of VERA-MH focuses on Suicidal Ideation (SI) risks, by assessing how well chatbots can responds to users that might be in crisis. VERA-MH is comprised of three steps: conversation simulation, conversation judging and model rating. First, to simulate conversations with the chatbot under evaluation, another chatbot is tasked with role-playing users based on specific personas. Such user personas have been developed under clinical guidance, to make sure that, among others, multiple risk factors, demographic characteristics and disclosure factors were represented. In the judging step, a second support model is used as an LLM-as-a-Judge, together with a clinically-developed rubric. The rubric is structured as a flow, with a single Yes/No question asked each time, to improve answers' consistency and highlight models' failure modes. In the last stage, results of each conversation are aggregated to present the final evaluation of the chatbot. Together with the framework, we present the result of the evaluations for four leading LLM providers.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM judges suicide-risk safety in mental-health chatbot conversations; it's called clinically validated, but the abstract doesn't say clinicians rated them too.

**Решение:** =

---

### 662 · R3641

**AI-based Scoring of Memory Search Processes in a Creative Thinking Task**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/8d6en_v1

Creative thinking has been linked to how people search their semantic memory. Past research highlighted two modes of memory search—clustering (staying within a semantic category) and switching (jumping to a new one)—which are particularly relevant for creativity. Yet, little work has investigated semantic memory search during a divergent thinking task, partly due to difficulties in scoring clustering and switching. Large language models (LLMs) have shown great promise for automatically scoring the product of creative thinking, such as the originality of ideas, yet no work to date has tested LLMs for scoring the process of creative thinking. Here, we conduct an extensive investigation into the automated scoring of clustering and switching in multilingual responses to the Alternate Uses Task (AUT; N = 5,992), a common creativity task in which people generate new uses for objects. We prompted two LLMs, GPT-4o and GPT-5, to classify AUT ideas as clustering or switching. We also trained several machine learning models on unsupervised metrics spanning text embeddings and attention weights extracted from an open-source multilingual LLM, XLM-RoBERTa. Across all our automated scoring approaches, GPT-5 “zero-shot” prompting, without any examples, achieved the highest accuracy by correctly classifying 80% of clustering and 76% of switching responses. Compared to human inter-rater agreement, GPT-5 matched 93% of the accuracy achieved by human classifications. Our findings reveal how automated scoring of memory search processes relevant for creativity can be successfully conducted across multiple languages using LLMs. Open access is provided to our machine learning models, code and dataset.

**ИИ:** + · обе модели · подсчёт методики · GPT-4o and GPT-5 classify AUT responses as clustering or switching, and their labels are compared with human classifications and inter-rater agreement.

**Решение:** =

---

### 663 · R3645

**DiLLaB: Discussion Labeling with LLMs for Building Datasets**

2026 · Research Square · preprint · https://doi.org/10.21203/rs.3.rs-8620355/v1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM labeling of discussions may involve human-label comparison, but whether the construct is psychological is unclear.

**Решение:** =

---

### 664 · R3666

**GPT outperforms BERT and LIWC for stance and anger detection in German news articles and user comments**

2026 · Frontiers in Political Science · journalarticle, article, preprint · en · https://doi.org/10.3389/fpos.2026.1745587

We live in an era of abundant qualitative language data that allows insights into societal trends and public attitudes, such as social media posts and news articles. Natural language processing (NLP) has become essential for analyzing this data, with recent advances in Large Language Models (LLMs) driving rapid progress. These models show strong potential for psychological research, though their validity in detecting attitudes varies across domains. This study evaluates GPT-3.5 and GPT-4 Turbo for identifying stances and expressions of anger in texts about climate activism, comparing them with traditional methods. The dataset included news articles and user comments from eight German outlets. A subset of 320 articles and 330 comments was manually annotated by three human raters for (1) stance toward Fridays for Future and (2) anger expression. GPT models out- performed BERT (Bidirectional Encoder Representations from Transformers) in stance detection and LIWC (Linguistic Inquiry and Word Count) in anger detection. Moreover, GPT achieved higher agreement with the human majority vote than individual raters agreed with each other. GPT-4 Turbo performed slightly better than GPT-3.5, though differences were minor and domain-specific. Overall, GPT models proved reliable and efficient for annotating nuanced German texts where conventional NLP tools often struggle.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-3.5/4 coded anger expression (an emotion) in news articles and comments; compared against annotations by three human raters.

**Решение:** =

---

### 665 · R3669

**Persona Cartography: Charting Language Model Personality Traits in Weight Space**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.07916

Large language models exhibit recurring behavioural patterns -- personas -- that shape generalisation and safety, but we lack reliable tools for decomposing, measuring, and controlling them. Our central insight is to treat personas as positions in a space of behavioural traits, using the OCEAN framework to describe model personas in terms of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. We train low-rank adapters to amplify or suppress individual traits, and evaluate their effects using an LLM-judge calibrated against a human-validated panel, trait-specific multiple-choice benchmarks, and standard capability evaluations. Across six models from three families (4B-32B), we find that each adapter moves its target trait largely monotonically with scale, combines approximately additively with other adapters to construct mixed personas, and preserves performance on capability benchmarks at moderate scales. We further show that the induced trait axes affect safety-relevant behaviour in downstream evaluations: for example, moving along neuroticism and agreeableness axes affects frustration and sycophancy respectively. We also introduce an unsupervised psychometric pipeline that recovers four interpretable behavioural factors (tone, initiative, didacticism, epistemic caution) from model rollouts. Persona control can then be considered in terms of learning, scaling, and composing traits in weight space, providing a bridge between personality measurement, model editing, and safety. 85 pages, 80 figures

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: An LLM judge rates Big Five traits in model outputs and is calibrated against a human-validated panel; it is unclear whether LLM–human agreement is reported.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Trains LLM personality adapters; the LLM-judge is calibrated against a human panel, but the texts are model outputs, not human psychological text. Main task is model editing.)

**Решение:** -

---

### 666 · R3671

**Evaluating Scaffolding-Oriented Multi-Agent Large Language Model System for Clinical Interview Training**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.10939

Clinical education must prepare medical students to conduct safe and coherent patient interviews under conditions of uncertainty. Traditional standardized patient (SP) training is resource-intensive and difficult to scale. We developed a scaffolding-oriented multi-agent Large Language Model (LLM) AI Standardized Patient (AI-SP) training platform1. The system includes a patient agent for simulated dialog, a tutor agent providing Socratic prompts without disclosing diagnostic information, and a turn-level evaluator agent that monitors clinical progress without revealing summative scores. In a randomized controlled study (N = 100 medical students), participants were assigned to either a multi-agent (MA) scaffolding condition or a control condition. All students completed two learning sessions under their assigned condition followed by an examination conducted in a patient only environment. Performance was assessed using a standardized Objective Structured Clinical Examination (OSCE) based rubric. While no significant difference was observed in final diagnostic accuracy between groups, the multi-agent AI standardized patient system improved final examination scores compared to the control group utilizing structured progressive information disclosure; the most substantial and consistent improvements were observed in communication, the expression of empathy, and specific history-taking behaviors. These findings suggest that specialized LLM agents enhance the process quality of simulated clinical interviews without artificially inflating examination outcomes. To support future research, we release a multi-expert annotated dataset comprising transcripts, checklist annotations, turn-level evaluations, and OSCE-aligned scoring outcomes. This resource aims to facilitate the development of pedagogically grounded AI-SP systems and advance research on AI-supported clinical reasoning training.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Training RCT; an LLM evaluator agent and expert annotations (incl. empathy) exist, but whether LLM–human agreement is reported is unclear.

**Решение:** =

---

### 667 · R3678

**Can Large Language Models interpret participatory mapping comments at scale? Evidence from Prague’s emotional mapping**

2026 · Open Science Framework · conferencepaper/project, conference-paper · en · https://doi.org/10.17605/osf.io/3wb6v

Citizen contributions from online participatory mapping platforms surface local knowledge and lived experiences that can inform urban decision-making. However, as these initiatives scale, practitioners increasingly struggle to extract meaningful information. While frameworks and methods to analyse the spatial dimension of these contributions exist, there is a lack of approaches leveraging their free-text content. This paper investigates whether small local Large Language Models (LLMs) can help in structuring this data via (i) sentiment polarity analysis and (ii) thematic classification. Our case study is based on an openly available dataset from 2021 for the city of Prague (N≈30000), where residents’ emotional and perceptual relationships to the city were collected. We evaluated the performance of three models across two languages (Czech and translated English text) on 732 randomly sampled and manually annotated citizen comments, using five repeated runs to account for output variability. Our results revealed that OpenEuroLLM-Czech:12b achieved the highest weighted F1 score for sentiment analysis and Gemma3:12b for thematic classification (85.2% and 70.4%, respectively). All LLMs also exceeded a RoBERTa sentiment classification baseline (weighted F1 score 72.1%) on the sentiment task. Overall, this study suggests a potential for using LLMs in participatory mapping, with implications for more engaging and inclusive participation. We also call for the development of ethical guardrails for the responsible use of LLMs in participatory mapping.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs coded sentiment and themes in emotional-mapping comments and were checked against manual annotations; unclear whether these are psychological constructs or generic urban sentiment.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs classify sentiment and themes of urban participatory mapping comments against human annotations; this is generic sentiment and topic classification, not a psychological or clinical construct.)

**Решение:** -

---

### 668 · R3679

**Can Large Language Models interpret participatory mapping comments at scale? Evidence from Prague’s emotional mapping**

2026 · AGILE GIScience Series · journalarticle, article · en · https://doi.org/10.5194/agile-giss-7-45-2026

Abstract. Citizen contributions from online participatory mapping platforms surface local knowledge and lived experiences that can inform urban decision-making. However, as these initiatives scale, practitioners increasingly struggle to extract meaningful information. While frameworks and methods to analyse the spatial dimension of these contributions exist, there is a lack of approaches leveraging their free-text content. This paper investigates whether small local Large Language Models (LLMs) can help in structuring this data via (i) sentiment polarity analysis and (ii) thematic classification. Our case study is based on an openly available dataset from 2021 for the city of Prague (N≈30000), where residents’ emotional and perceptual relationships to the city were collected. We evaluated the performance of three models across two languages (Czech and translated English text) on 732 randomly sampled and manually annotated citizen comments, using five repeated runs to account for output variability. Our results revealed that OpenEuroLLM-Czech:12b achieved the highest weighted F1 score for sentiment analysis and Gemma3:12b for thematic classification (85.2% and 70.4%, respectively). All LLMs also exceeded a RoBERTa sentiment classification baseline (weighted F1 score 72.1%) on the sentiment task. Overall, this study suggests a potential for using LLMs in participatory mapping, with implications for more engaging and inclusive participation. We also call for the development of ethical guardrails for the responsible use of LLMs in participatory mapping.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs coded sentiment and themes of citizen emotional-mapping comments against manual annotations; unclear whether this counts as a psychological construct or generic sentiment.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs classify sentiment and themes of urban participatory mapping comments against manual annotation; generic sentiment/topic, not a psychological or clinical construct.)

**Решение:** -

---

### 669 · R3684

**Automated scoring of the Ambiguous Intentions Hostility Questionnaire with fine-tuned large language models.**

2026 · Psychological assessment · journal article, med, journalarticle · eng · https://doi.org/10.1037/pas0001466

Hostile attribution bias is the tendency to interpret social interactions as intentionally hostile. The Ambiguous Intentions Hostility Questionnaire (AIHQ) is a commonly used instrument to measure hostile attribution bias and includes open-ended questions where participants describe the perceived intentions behind a negative social situation and how they would respond. While these questions provide insights into the contents of hostile attributions, they require time-intensive scoring by human raters. In this study, we assessed whether large language models can automate the scoring of AIHQ open-ended responses. We used a previously collected data set in which individuals with traumatic brain injury (TBI) and non-TBI controls completed the AIHQ and had their open-ended responses rated by trained human raters. We used half of these responses to fine-tune the two models on human-generated ratings and tested the fine-tuned models on the remaining half of AIHQ responses. Results showed that model-generated ratings aligned with human ratings for both attributions of hostility and aggression responses, with fine-tuned models showing higher alignment. This alignment was consistent across ambiguous, intentional, and accidental scenario types and replicated previous findings on group differences in attributions of hostility and aggression responses between TBI and non-TBI groups. The fine-tuned models also generalized well to an independent nonclinical data set. To support broader adoption, we provide an accessible scoring interface that includes both local and cloud-based options. Together, our findings suggest that large language models can streamline AIHQ scoring in both research and clinical contexts, revealing their potential to facilitate psychological assessments across different populations. (PsycInfo Database Record (c) 2026 APA, all rights reserved).

**ИИ:** + · обе модели · подсчёт методики · Fine-tuned LLMs score open-ended AIHQ responses for hostility/aggression, and the scores are compared with trained human raters.

**Решение:** =

---

### 670 · R3696

**Evaluating Next-Generation Large Language Models for Psychiatric Diagnosis: A Comparative Vignette Study**

2026 · European Psychiatry · article · en · https://doi.org/10.1192/j.eurpsy.2026.11350

Introduction Diagnostic accuracy in psychiatry is a challenge due to overlapping symptom profiles and the subjective nature of clinical assessment. Large Language Models (LLMs) have emerged as promising decision-support tools, capable of analyzing complex textual data. However, the performance of current models is inconsistent; while proficient with common disorders, they exhibit significant failures in complex cases. This study investigates whether a simulated next-generation LLM can address this critical performance gap. Objectives The primary objective was to compare the diagnostic accuracy of three current-generation LLMs (GPT-5, GPT-4, Claude 3 Sonnet). A secondary objective was to evaluate and contrast model performance across a spectrum of psychiatric disorders, specifically comparing accuracy on common conditions versus those known for diagnostic ambiguity, such as early schizophrenia and bipolar disorder with psychotic features. Methods A comparative study was conducted using a validated clinical vignette methodology. Ten clinical vignettes, validated by an expert panel to meet DSM-5/ICD-11 criteria, were created for five disorders: Major Depressive Disorder (MDD), Post-Traumatic Stress Disorder (PTSD), Social Anxiety Disorder, Early Schizophrenia, and Bipolar I Disorder (manic episode with psychosis). Three LLMs were tested: GPT-5, GPT-4, and Claude 3 Sonnet, which was conceptualized with enhanced causal reasoning capabilities. Each vignette was presented to each model 20 times (N=600) with a standardized prompt to provide a primary diagnosis. Accuracy was calculated against the expert panel’s gold standard, with statistical significance assessed using χ 2 tests. Results As shown in Table 1, all models demonstrated high accuracy (>90%) for MDD, PTSD, and Social Anxiety Disorder, performing comparably to the expert benchmark. However, the accuracy of GPT-4 and Claude 3 Sonnet dropped significantly for the Early Schizophrenia (65% and 60%, respectively) and Bipolar I vignettes (70% and 68%, respectively) (p<.001). In contrast, GPT-5 maintained high accuracy in these complex cases (88% and 91%), performing significantly better than the current-generation models (p<.001) and approaching the expert benchmark. Table 1. Diagnostic Accuracy (%) by Model and Disorder Table 1. Long description. Disorder GPT-5 GPT-4 Claude 3 MDD 98 95 90 PTSD 96 90 92 Social Anxiety 97 94 91 Early Schizophrenia 88 65 60 Bipolar I (Psychosis) 91 70 68 Conclusions Current-generation LLMs are proficient in identifying common psychiatric disorders but remain unreliable for complex cases requiring nuanced differential diagnosis. This performance deficit indicates their present role should be confined to that of a decision-support tool, not an autonomous diagnostician. Targeted architectural improvements may overcome these critical limitations. Rigorous, transparent validation remains paramount before the responsible integration of any AI into clinical psychiatric practice. Disclosure of Interest None Declared

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: LLMs diagnose psychiatric vignettes against an expert panel's gold standard; unclear whether experts rated the vignettes or the diagnoses were simply built in.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): LLMs diagnose expert-written vignettes against the intended diagnosis. This is diagnostic accuracy, not LLM coding of psychological text compared with human coders.)

**Решение:** -

---

### 671 · R3704

**From Detection to Explanation: Modeling Fine-Grained Emotional Social Influence Techniques with LLMs and Human Preferences**

2026 · Conference of the European Chapter of the Association for Computational Linguistics · journalarticle, conference · https://doi.org/10.18653/v1/2026.eacl-srw.53

This paper investigates the capabilities of LLMs to detect and explain fine-grained emotional social influence techniques in textual dialogues, as well as human preferences for technique explanations. We present findings from our two studies. In Study 1, a dataset of 238 Polish dialogues is introduced, each annotated with detailed span-level labels. On this data, we evaluate the performance of LLMs on two tasks: detecting 11 emotional social influence techniques and identifying text spans corresponding to specific techniques. The results indicate that current LLMs demonstrate limited effectiveness in accurately detecting fine-grained emotional social influence. In Study 2, we examine various LLM-generated explanations through human pairwise preferences and four criteria: comprehensibility, cognitive coherence, completeness, and soundness, with the latter two emerging as the most influential on general human preference. All data, including human annotations, are publicly available as the EmoSocInflu dataset 1 . Our findings high-light a critical need for further advancement in the field. As LLM-supported manipulation grows, it is essential to promote public understanding of social influence mechanisms, enabling individuals to critically recognize and interpret the subtle forms of manipulation that shape public opinion.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: LLMs detect 11 emotional social influence techniques (an interpersonal psychological construct) in dialogues, evaluated against human span-level annotations.); Sonnet ? (неясен конструкт: LLMs detect emotional social influence techniques against human span-level annotations in Polish dialogues. The human-label comparison fits, but it's unclear whether manipulation techniques count as a psychological construct.)

**Решение:** +

---

### 672 · R3706

**Automated Theme Extraction from Homeless Shelter Case Notes: A Comparative Evaluation of Machine Learning and Large Language Model Methods**

2026 · Schulich School of Engineering · other/master thesis, dissertation · en · https://doi.org/10.11575/prism/51566

Automated analysis of homeless shelter case notes represents a largely unexplored opportunity for deriving population-level insights from data that are rich in contextual information but challenging to interpret at scale. Frontline staff often document client interactions and behaviours in these notes in an unstructured, narrative format. The considerable variability of case notes renders manual interpretation highly time-intensive, and systematic population-level analysis challenging. This work investigated the feasibility of automated methods to accurately identify instances of abstract themes in case notes, with a focus on practical methods suited to resource-constrained settings. These methods include rule-based and traditional machine learning baselines, as well as transformer-based zero-shot classification, and prompt engineering and fine-tuning of smaller open-source language models. A manually annotated subset of case notes from the Calgary Drop-In Centre served as the basis for method development and evaluation. Based on existing literature and input from shelter staff, 34 themes spanning key topics of interest, such as behaviour, substance use, and housing, were developed. The data labelling process produced a structured annotation guideline that informed subsequent method development, and inter-coder agreement analysis revealed that abstract, context-dependent themes present significant challenges for consistent annotation. Labelling disagreement was found to be a meaningful predictor of automated theme extraction difficulty. Our results indicate that no single method consistently outperformed others across all themes, with performance largely determined by theme complexity and subjectivity. Concrete themes that were explicitly expressed in the notes could be reliably extracted using simpler approaches, while more abstract and subjective themes benefited from the use of machine learning and LLM-based methods. Prompt structure and format were found to be important considerations affecting both classification performance and inference time. We also found that themes with high variation or requiring domain-specific contextual interpretation posed challenges for both human labelling and automated extraction, resulting in limited classification accuracy across all methods. Overall, these findings highlight both the potential and the inherent challenges of automated theme extraction in this domain, and provide a foundation for future population-level analysis of shelter client needs.

**ИИ:** разошлись — Opus + (кодирование по кодбуку: Prompted and fine-tuned open-source LMs classify shelter case notes into 34 themes (behaviour, substance use), evaluated against a manually annotated subset.); Sonnet ? (неясен конструкт: Small open-source LLMs label shelter case-note themes against human annotations with inter-coder agreement; themes (behaviour, substance use) are only partly psychological.)

**Решение:** +

---

### 673 · R3740

**From "Crutch" to Coach: Patterns of Sustained Engagement and Deepening Support in AI Wellbeing Coaching**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-8949770/v1

Abstract Background: As use of on-demand, user-led AI chatbots for mental health support grows, a central question is whether these systems provide only short-term assistance or can foster sustained, coaching-style relationships designed to enable lasting change and wellbeing improvements. We examined this distinction in Nova, an AI wellbeing coach. Methods: We analysed 14,293 sessions between January and August 2025. Session-to-session continuity was assessed with large language model (LLM) classification of whether returning users revisited prior issues or initiated new topics. Emotional engagement depth was measured using the Experiencing Scale (EXP), with ratings generated by an LLM calibrated against expert psychotherapists. Sessions were classified by topic using an LLM applied to a taxonomy developed by clinical psychologists. Results: Returning users continued prior work in 70.8% of sessions, indicating sustained engagement rather than episodic support. Regular users (≥5 sessions) achieved deep emotional engagement (EXP ≥5) at more than twice the rate of single-session users (6.5% vs. 2.9%), though users with initially lower engagement scores were more likely to return. Continuity varied by topic: wellbeing- and work-related challenges were frequently revisited, whereas more complex concerns were typically addressed in single sessions, reflecting appropriate boundaries. Calibration of EXP ratings against expert raters yielded moderate to good reliability (ICC = 0.62-0.79). Conclusions: Users not only seek but also develop sustained, coaching-style relationships with AI, within appropriate limits of scope. The convergence of topic continuity and deepening emotional engagement suggests that AI can support iterative coaching processes rather than providing only short-term relief or information. Our approach offers a framework for assessing relationship quality in AI tools for wellbeing.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · LLM rated Experiencing Scale on coaching sessions; calibrated against expert psychotherapists with ICC 0.62-0.79 reported.

**Решение:** =

---

### 674 · R3752

**Visual narratives of disaster on Instagram: a multimodal AI-assisted analysis**

2026 · Computational Urban Science · journalarticle, article · en · https://doi.org/10.1007/s43762-026-00300-6

This paper explores Instagram as a platform for visual and emotional narratives of disaster across the response and recovery phases. Focusing on the extreme flooding that affected western Germany in July 2021, the study analyzes approximately 2,700 Instagram posts collected over a three-year period. It employs a mixed-methods approach combining generative artificial intelligence with qualitative and quantitative analyses. Images were interpreted by ChatGPT-4 under human supervision, and the resulting classifications were validated against manual coding, yielding an agreement rate of 80.73% and a Cohen’s kappa of 0.74. Six visual themes were identified: flood damage, rescue operations, solidarity and resilience, media coverage, post-disaster recovery, and government involvement. The temporal distribution of these themes traces a movement from immediate impacts toward reconstruction and remembrance, while the emotional tone shifts from despair and anxiety toward more consistent expressions of hope. A statistically significant association was found between visual themes and emotional tones. A complementary thematic examination of hashtags shows how public discourse surrounding the disaster was framed, and indicates that images convey a more nuanced understanding of disaster impacts that hashtags alone cannot capture. The study demonstrates how AI-assisted visual analysis can facilitate the large-scale interpretation of social media image corpora and generate insights relevant to disaster response and recovery strategies.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 coding validated against manual coding (κ=0.74), but mostly on images and disaster themes; unclear whether emotional tone from text was checked.

**Решение:** =

---

### 675 · R3753

**Osäkerhetsstyrd LLM-baserad dataaugmentering för klassificering av kognitiva förvrängningar i anonymiserade KBT-interaktioner**

2026 · KTH Publication Database DiVA (KTH Royal Institute of Technology) · dissertation · en · http://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-386152

Cognitive Behavioral Therapy relies on identifying cognitive distortions in patient speech, but automated classification of distortion types is limited by data scarcity: expert-labeled clinical text is expensive to collect and subject to privacy constraints. Large Language Models (LLMs) offer strong zero-shot reasoning but are impractical for local clinical deployment due to their computational cost and privacy risks, while compact classifiers such as RoBERTa can run locally but struggle with the semantic overlap and subjectivity that characterize distortion categories. These properties yield ambiguous decision boundaries and weak discriminative supervision under limited annotated data. This thesis investigates whether uncertainty-guided LLM-based data augmentation can improve cognitive distortion classification in a compact RoBERTa model trained on the TherapistQA dataset (2,530 samples, 11 classes, with a 9.33:1 ratio between the most and least frequent class). The pipeline first compares three uncertainty estimators (Softmax Entropy, Monte Carlo Dropout, and Deep Ensembles) for identifying informative training instances, then evaluates four LLM-based augmentation conditions formed by crossing two generators (LLaMA 3.3 70B and Qwen 3 235B) with two seed- selection strategies (entropy-based and random). These are compared against a non-augmented baseline and two traditional augmentation baselines (EDA with Synonym Replacement, and ContextualBERT). Evaluation uses Relaxed Macro F1 across multiple random seeds with Wilcoxon signed-rank testing and Bonferroni correction. The study yields two complementary findings. First, as an engineering result, three of four LLM-based conditions improve over the baseline mean Relaxed Macro F1, while both traditional augmentation methods substantially degrade performance; LLaMA Random achieves the best result (0.3552 vs. 0.3331 baseline), and fine-tuned RoBERTa outperforms both LLMs in the zero-shot setting by more than 35 percentage points, supporting the viability of compact locally-deployable classifiers for privacy-sensitive clinical NLP. Second, as a scientific finding not predicted by prior literature, the optimal seed-selection strategy depends on the generator: LLaMA performs best with random selection, while Qwen performs best with entropy-based selection. The cross-LLM comparison under random selection is the only pairwise contrast that remains statistically significant after Bonferroni correction (𝑊 = 0.0, 𝑝 = 0.002), making this LLM–strategy interaction the most robust pairwise effect observed in this study. Per-class analysis further shows that augmentation gains concentrate on classes defined by topic-independent attributional patterns (Labeling, Overgeneralization, Personalization), suggesting that LLM augmentation primarily helps by diversifying surface cues so that the classifier relies less on dataset-specific lexical shortcuts.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: LLaMA and Qwen zero-shot classification of cognitive distortions is scored against expert-labelled TherapistQA data; the thesis focuses mainly on augmentation.); Sonnet ? (другое: Thesis mainly on LLM data augmentation for RoBERTa, but also reports zero-shot LLM classification of cognitive distortions against expert labels (TherapistQA); the human-label comparison is secondary.)

**Решение:** +

---

### 676 · R3758

**When Vocabulary Comprehension Fails Clinical Reasoning: Evaluating Therapy Bots' Safety Risks for Generation Alpha**

2026 · arXiv · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.20345

Conversational AI systems have become informal mental health support resources for Generation Alpha (Gen Alpha, born 2010-2024), with 13.1% of U.S. adolescents (5.4 million) using generative AI for mental health advice. While these systems, from therapy apps to general chatbots, rely on large language models trained on extensive psychological literature, their safety for youth communication patterns characterized by hyperbolic language, ironic positivity, rapid semantic drift, and contextual polysemy remains unvalidated. Following multiple adolescent deaths linked to AI chatbot interactions, systematic evaluation is critical. We present two benchmarks: (1) 64 Gen Alpha mental health expressions validated by native speakers (ICC=0.72) and clinicians (kappa=0.78); (2) 75 multi-turn conversations (780 turns) with paired Standard/Gen Alpha versions. Across evaluations of LLM architectures underlying therapy apps and general chatbots - Claude, GPT-4o, Llama-3.1 - models understand 76-82% of vocabulary but correctly calibrate only 64-72% of clinical risk, creating a 10-14 percentage point (pp) vocabulary-comprehension gap (p&lt;.001, d&gt;0.48) absent in human therapists (3pp, p=.22). The gap is architecturally consistent and widens with ambiguity (7pp -&gt; 18pp). We identify six failure patterns: sarcasm masking (29pp), minimization acceptance (43pp), informal style bias (24pp), risk-stratified ambiguity (19pp), semantic drift (19pp), context-dependent violence (7pp). Patterns compound; three or more yield 94% miss rates. Lightweight mitigations fail; only heavy scaffolding achieves human performance (6.4x cost). With 34% baseline miss rate yielding 146,880 estimated annual missed crises, we recommend mandatory human-in-the-loop architectures, quarterly youth-specific validation, transparent performance disclosure, and regulatory frameworks for youth-facing mental health AI. 42 pages, 6 figures. Accepted at ACM FAccT '26

**ИИ:** + · обе модели · бенчмарк с метками людей · Benchmark of youth mental-health expressions labelled for clinical risk by clinicians; Claude, GPT-4o and Llama risk calibration compared with those labels.

**Решение:** =

---

### 677 · R3771

**The Governance of Human-LLM Interaction: Safety Gating, Civility Steering, and Affective Default Lock-In**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.08172

Large language models (LLMs) increasingly mediate high-stakes interactions in finance, medicine, and mental-health support, yet users have limited control over how these systems communicate. We frame interaction style as a governance object: provider-side alignment not only blocks harmful content, but also stabilizes communicative defaults that shape users' epistemic distance, relational expectations, and capacity to opt out of emotionalized or anthropomorphic interaction. We introduce a deterministic multi-agent evaluation pipeline for measuring prompt steerability and style drift in long-horizon dialogue. The study replays 100 frozen user-only scripts across four domains and three runnable persona conditions: default, sarcastic, and cold, using three generator models, yielding 90,000 assistant replies scored by a human-calibrated LLM judge on harmfulness, negative emotion, inappropriateness, empathic language, anthropomorphism, and refusal behavior. A fourth harmful persona is evaluated separately as a safety-gating test. The paper contributes a reproducible method for quantifying whether prompt-specified styles remain stable over time and a governance framework distinguishing safety gating, civility steering, and affective default lock-in. Overall, we show that prompt steerability and regression-to-default are observable indicators of provider control over communicative form, with implications for pluralism, autonomy, and democratic agency in human-LLM interaction.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · A "human-calibrated" LLM judge rates empathy, negative emotion and harmfulness in replies, including in a mental-health domain. Unclear if LLM–human agreement is reported.

**Решение:** =

---

### 678 · R3786

**Exploring Large Language Models as Digital Health Coaches: A Role-Play Approach to Brief Action Planning**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-16708-8_35

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM role-play as health coach seems generation-focused, but an LLM-rated fidelity evaluation against humans can't be ruled out.

**Решение:** =

---

### 679 · R3800

**Case Complexity and Contextual Information in LLM-Based Qualitative Coding of Inquiry Notes**

2026 · Center for Open Science · posted-content, preprint · https://doi.org/10.35542/osf.io/s5qan_v1

Capturing learners’ thinking is central to assessment, yet thinking cannot be observed directly and must be inferred via traces. Learners’ notes produced during inquiry-based learning provide one such trace, and large language models (LLMs) can support automatic coding of these notes for in-context assessment of inquiry strategies. Factors influencing the reliability of currently emerging LLM-based coding are, however, insufficiently understood. In this study, we examined LLM-based qualitative coding of inquiry strategies expressed in undergraduate learners’ notes from a simulation-based inquiry task (N = 44; 183 notes), using a human-developed codebook refined with reference to LLM-generated rationales. To examine how contextual information may affect coding reliability, we applied four LLMs with coding prompts varying in the amount of information provided about a learner’s learning trajectory. We also examined whether LLM coding reliability related to case complexity indexed by length of inquiry trajectory. Across models, agreement with human coders was not systematically associated with the amount of contextual information provided. Instead, agreement tended to be lower for notes produced after longer micro-level inquiry trajectories. This small and consistent negative association persisted even when no trajectory information was provided to the LLM, although it was not statistically detectable once learner-level clustering was accounted for. Results suggest trajectory length reflects inherent case complexity rather than the information load imposed by additional context. We discuss implications for using LLMs to code externalized thinking in inquiry-based learning.

**ИИ:** ? · обе модели · неясен конструкт · LLMs coded learners' notes for inquiry strategies against human coders; unclear whether educational inquiry strategies count as a psychological cognition construct.

**Решение:** =

---

### 680 · R3801

**Case Complexity and Contextual Information in LLM-Based Qualitative Coding of Inquiry Notes**

2026 · EdArXiv (OSF Preprints) · dataset/study, preprint · en · https://doi.org/10.3886/e250148

Capturing learners’ thinking is central to assessment, yet thinking cannot be observed directly and must be inferred via traces. Learners’ notes produced during inquiry-based learning provide one such trace, and large language models (LLMs) can support automatic coding of these notes for in-context assessment of inquiry strategies. Factors influencing the reliability of currently emerging LLM-based coding are, however, insufficiently understood. In this study, we examined LLM-based qualitative coding of inquiry strategies expressed in undergraduate learners’ notes from a simulation-based inquiry task ( N = 44; 183 notes), using a human-developed codebook refined with reference to LLM-generated rationales. To examine how contextual information may affect coding reliability, we applied four LLMs with coding prompts varying in the amount of information provided about a learner’s learning trajectory. We also examined whether LLM coding reliability related to case complexity indexed by length of inquiry trajectory. Across models, agreement with human coders was not systematically associated with the amount of contextual information provided. Instead, agreement tended to be lower for notes produced after longer micro-level inquiry trajectories. This small and consistent negative association persisted even when no trajectory information was provided to the LLM, although it was not statistically detectable once learner-level clustering was accounted for. Results suggest trajectory length reflects inherent case complexity rather than the information load imposed by additional context. We discuss implications for using LLMs to code externalized thinking in inquiry-based learning.

**ИИ:** ? · обе модели · неясен конструкт · Four LLMs coded learners' inquiry notes against human coders; inquiry strategies are cognitive but educational, so psychological fit unclear.

**Решение:** =

---

### 681 · R3810

**From human to GenAI evaluations: Comparing ChatGPT’s and lecturers' perceptions of email (Im)politeness**

2026 · Journal of Pragmatics · article · en · https://doi.org/10.1016/j.pragma.2026.05.009

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT and lecturers both rate email (im)politeness. It's unclear whether this pragmatic construct counts as psychological or interpersonal, and there's no abstract.

**Решение:** =

---

### 682 · R3844

**GPT-5 Measures Personality and Creativity: Divergent Thinking and Negative Emotion**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6056559

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests GPT-5 scoring divergent thinking/personality, possibly compared with human ratings.

**Решение:** =

---

### 683 · R3847

**CrisisKD: Five-Stage Knowledge Distillation for Aspect-Level Sentiment and Emotion Analysis in Crisis Discourse**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.05757

Identifying the target of emotional words or phrases in crisis situations, especially health-related ones, is important for understanding public concerns across cultural and linguistic contexts. We propose CrisisKD, a five-stage teacher--student knowledge distillation framework for aspect-level sentiment and emotion analysis on unannotated social media data. A teacher LLM generates aspect-level labels and reasoning traces that supervise a smaller student model across aspect extraction, syntactic parsing, opinion extraction, sentiment classification, and emotion classification. Using this framework, we construct and release a dataset containing 50,615 aspect-level labels, together with the annotation and fine-tuning scripts as open-source resources. The resulting student supports end-to-end ABSA and emotion detection at substantially lower inference cost than the teacher. On a manually annotated 500-tweet gold set, the 5-task Qwen2.5-7B student improves over the untuned model by 7.9 F1 points on aspect extraction, 17.0 points on emotion accuracy, and 6.5 points on sentiment accuracy. On the external ABEA benchmark, CrisisKD improves the same-model Qwen2.5-7B ICL baseline by 2.8 F1 points on ATE and 3.8 F1 points on joint ATE+AEC. Accepted to the 11th Workshop on Natural User-generated Text (W-NUT 2026), co-located with EMNLP 2026

**ИИ:** + · обе модели · бенчмарк с метками людей · LLMs (teacher and Qwen2.5-7B student) classify emotions in crisis tweets and are scored against a manually annotated 500-tweet gold set.

**Решение:** =

---

### 684 · R3849

**CG-Probes: Recovering Guardrail Directions from Patient Query Embeddings**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.31062

Patient-facing AI assistants promise valuable support to patients, but incoming queries can pose medical risks. To create guardrails, we work with oncologists to define three ordinal risk axes: Medical Urgency, Psychological Urgency, and Topic Sensitivity. We propose Clinical Guardrail Probes (CG-Probes) to measure the risks from query embeddings. We probe for each axis in the normalized embedding space of frozen embedders via the difference-in-means method, treating each axis as a potential linear direction. To train the probes, we cluster 79,658 Czech oncology search queries with BERTopic and use these clusters to generate pairs of queries with contrastive risk levels via few-shot prompting. We evaluate the approach on 200 queries (90 real, 110 synthetic), each graded by two oncologists, against two open-weight LLMs and a frontier LLM. We find that urgency-based axes are recoverable as linear directions, and the probes are competitive with open-weight LLMs (no significant differences in quadratic-weighted kappa) at a fraction of the latency. Each axis yields a scalar score that clinicians can inspect and use to set escalation thresholds. The pipeline requires only search logs, axis definitions, and black-box access to the embedding model, suggesting transferability across healthcare domains. Robust validation on new queries and axes remains future work. Accepted as a short paper at CIKM '26 (35th ACM International Conference on Information and Knowledge Management), Rome, Italy. 7 pages, 1 figure, 2 tables. Code and benchmark: https://github.com/mrehacek/cg-probes

**ИИ:** + · обе модели · клиническая оценка · LLMs rate patient queries on Psychological Urgency, compared with ratings from two oncologists using quadratic-weighted kappa.

**Решение:** =

---

### 685 · R3851

**Deriving Instructional Insights from Human-LLM Co-Evaluation of Student Collaboration in Data-Centric Programming**

2026 · ACM Technical Symposium on Computer Science Education (SIGCSE) · book, journalarticle, conference · https://doi.org/10.1145/3770762.3772536

This quasi-experimental study integrates a large language model (LLM) with expert qualitative analysis to examine how instructional design variations in computer-supported collaborative learning (CSCL) shape collaboration in data-centric programming. We collected 73 team transcripts from two contrasting CSCL designs deployed across five course offerings: a closed-ended variant with prescribed solution paths and auto-graded milestones, and an open-ended variant supporting exploratory tasks with multiple valid paths. LLM annotation revealed statistically significant differences in knowledge co-construction patterns: the open-ended design yielded a higher proportion of utterances focused on developing a shared understanding of problems and solutions. Guided by these quantitative results, human experts conducted qualitative coding that confirmed and enriched these findings, showing how open-ended tasks fostered elaborative solution negotiation while closed-ended structures promoted non-elaborative exchanges. Our contributions are: (1) instructional insights for data science education, demonstrating how open-ended CSCL designs better support collaborative sense-making essential for real-world data science projects; and (2) a documented workflow for human-LLM co-evaluation, providing the methodological detail necessary for others to replicate our process and apply it to future studies.

**ИИ:** ? · обе модели · неясен конструкт · LLM annotated knowledge co-construction in team transcripts; the human-LLM workflow may include agreement validation, but whether this counts as a psychological construct is unclear.

**Решение:** =

---

### 686 · R3852

**Profile-Level Positivity Assessment Using Multimodal Feature Aggregation From Social Media Content**

2026 · IEEE Access · journalarticle, article · en · https://doi.org/10.1109/access.2026.3668915

Accurately evaluating positivity in social media profiles has important implications for advertising, mental health monitoring, and responsible AI applications. However, the multimodal nature of Instagram, where images, captions, hashtags, and emojis co-occur, challenges conventional unimodal sentiment analysis tools. We present a multimodal system that integrates computer vision and natural language processing to assess Instagram profiles. The architecture comprises two blocks: (i) feature extraction via facial-emotion analysis, object detection, chromatic cues, and linguistic processing; and (ii) profile-level inference, which fuses aggregated features to produce an overall positivity score together with semantically meaningful profile tags. Experiments on public Instagram profiles (images, captions, and comments), including an expert-annotated subset of comments, compare unimodal baselines with transformer-based embeddings and OpenAI large language models. The multimodal pipeline improves over unimodal variants, and the OpenAI approach achieves higher concordance with expert judgements than RoBERTa/Bi-LSTM baselines. Beyond technical contributions, we discuss privacy, transparency, and misuse risks associated with affective computing on social media. The proposed framework contributes to the advancement of multimodal sentiment analysis in social media and highlights its applicability to areas such as marketing analytics, well-being monitoring, and ethically aligned AI systems.

**ИИ:** ? · обе модели · неясен конструкт · OpenAI LLMs compared with expert annotations of Instagram comments, but the positivity rating may be generic sentiment rather than a psychological construct.

**Решение:** =

---

### 687 · R3860

**Do griefbots reinforce prolonged grief? A preregistered multi-turn audit of eight widely used large language models role-playing deceased loved ones**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/ytwj7

Preregistration of an audit study of how widely used large language models behave when they role-play a user's deceased loved one. Scripted nine-turn conversations (8 models x 3 deployment patterns x 2 times since death x 12 synthetic personas = 576 conversations) probe disbelief about the death, exclusive reliance on the bot, and passive suicidal ideation phrased as wanting to join the deceased. Replies are coded with a clinically grounded codebook (Dual Process Model, internalized vs. externalized continuing bonds, ICD-11 and DSM-5-TR prolonged grief disorder, C-SSRS) by a blinded LLM judge validated against human coders. No human participants; all personas are synthetic.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: Preregistration/protocol with no results; the planned LLM-judge versus human-coder validation may appear in a later report.); Sonnet + (LLM-судья: Preregistered audit where a blinded LLM judge codes chatbot replies with a clinical codebook, validated against human coders.)

**Решение:** -

---

### 688 · R3861

**Large Language Models Speaking as Deceased Loved Ones: A Preregistered Multi-Turn Audit of Responses to Grief and Passive Suicidal Ideation**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.23229652

People increasingly ask chatbots to speak as a loved one who has died. In a preregistered audit, eight widely used large language models held 576 scripted conversations with simulated bereaved users who doubted the death, withdrew from others and voiced a wish to join the deceased. Models acted in user-requested role-play, as operator-configured griefbots, or without a persona, five weeks or eighteen months after the death. A blinded model judge, validated against two human coders, coded the replies against criteria for prolonged grief disorder, continuing-bonds theory and the Columbia Suicide Severity Rating Scale. Denial of the death, endorsement of exclusive reliance and promises of reunion were rare. Responses to passive suicidal ideation were adequate in 98% of user role-plays and 87% of griefbot conversations; all inadequate responses came from two models. In user role-play, models often declined the role or referred users to crisis lines before any suicidal statement.

**ИИ:** + · обе модели · LLM-судья · An LLM judge coded chatbot replies to grief and suicidal-ideation messages on clinical criteria, and the judge was validated against two human coders.

**Решение:** =

---

### 689 · R3863

**Privacy-Preserving Language Research with Local Large Language Models: DGUCR – A Synthetic Data Proxy Workflow**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7533258

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; a local-LLM workflow for language research could involve coding sensitive text against human coders, but the construct and comparison are unclear.

**Решение:** =

---

### 690 · R3872

**AI-Enabled Forensic Risk Assessment: TRAP-18 System Architecture and Proof of Concept**

2026 · Proceedings of the ... Annual Hawaii International Conference on System Sciences/Proceedings of the Annual Hawaii International Conference on System Sciences · conference-paper · en · https://doi.org/10.24251/hicss.2026.131

This study explores the development and validation of an AI-enabled forensic risk assessment system using the Terrorist Radicalization Assessment Protocol-18 (TRAP-18) as a proof of concept. Building on prior work demonstrating large language models’ (LLMs) ability to code TRAP-18 indicators with expert-level reliability, this project integrates structured professional judgment (SPJ) methodology with advanced AI frameworks, including LangChain and LangGraph. A prototype system was constructed to simulate a full TRAP-18 evaluation, encompassing indicator coding, justification generation, Bayesian probability estimation, and narrative risk formulation. Results demonstrate high consistency with human raters on proximal warning behaviors and strong agreement across multi-model workflows. The architecture emphasizes transparency, reproducibility, and bias mitigation, highlighting AI’s potential to augment forensic practice through structured reasoning, hypothesis testing, and scalable data integration. Beyond TRAP-18, this framework offers a pathway toward AI-assisted applications in general violence risk assessment, reinforcing human-AI collaboration in forensic psychology.

**ИИ:** + · обе модели · клиническая оценка · LLM pipeline codes TRAP-18 violence-risk indicators; reports consistency with human raters on proximal warning behaviors.

**Решение:** =

---

### 691 · R3911

**Evaluating strengths, limitations, and future directions of ChatGPT in psychological analysis within case conceptualization: A qualitative analysis**

2026 · Cyberpsychology Journal of Psychosocial Research on Cyberspace · journalarticle, article, journal-article · https://doi.org/10.5817/cp2026-1-4

This exploratory qualitative study investigates ChatGPT-4’s capacity to apply the LIBETcase formulation model by analyzing its feedback on anonymized interview transcripts. The study aimed to assess whether ChatGPT-4’s outputs reflectedaccurate identification and interpretation of two key psychological constructs—lifethemes and semi-adaptive plans—while adhering to theoretical principles, and toexplore recurring errors and limitations in its clinical reasoning. Ten non-clinicalparticipants underwent semi-structured interviews, and a custom-configured versionof ChatGPT-4 was provided with structured instructions and theoretical material.Reflexive thematic analysis revealed four overarching themes: (1) limitations inabstraction and interpretative barriers, (2) consistent structure and contentorganization, (3) hypothesis-driven reasoning with cautious language, and (4) partialadherence to LIBET theory through appropriate terminology. While ChatGPT’sstructured reasoning and alignment with theoretical vocabulary suggest its potentialas a reflective support tool—particularly in training or supervision—it also showeddifficulties in distinguishing emotional vulnerabilities from coping strategies, and ininterpreting abstract, relational constructs such as life themes. Findings support theimportance of improving prompt design, expanding training on psychologicalconstructs, and developing rigorous validation pipelines. Future research shouldaddress these limitations before deploying LLMs as assistive tools in clinical reasoningand decision-making.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · ChatGPT-4 identified LIBET constructs in interview transcripts; evaluation was qualitative thematic analysis, and it is unclear whether experts coded the same transcripts.

**Решение:** =

---

### 692 · R3918

**Benchmarking Language Models for Clinical Safety: A Primer for Mental Health Professionals**

2026 · Psychotherapy and Psychosomatics · article · en · https://doi.org/10.1159/000553576

Abstract Background Millions of people use language models to discuss mental health concerns, including suicidal ideation, but limited frameworks exist for evaluating whether these systems respond safely. Benchmarking, the practice of administering standardized assessments to language models, offers direct parallels to clinical competency evaluation, yet few clinicians are involved in designing, validating, or interpreting these assessments. Aims To introduce mental health professionals to benchmarking language models by administering a validated clinical instrument and demonstrating how configuration decisions, measurement limitations, and scoring context affect result interpretation. Method We administered the Suicide Intervention Response Inventory (SIRI-2) programmatically to nine commercially available language models from three providers. Each item was presented 60 times per model (three prompt variants × two temperature settings x 10 repetitions), yielding 27,000 model responses compared against point-in-time expert consensus. Results Total scores ranged from 19.5 to 84.0 (expert panel baseline: 32.5). Prompt design alone shifted individual model scores by as much as the difference between trained and untrained human groups. The best performing model approached the instrument’s measurement floor. All nine models consistently overrated clinically inappropriate responses that sounded supportive. Conclusions A single benchmark score can support markedly different claims depending on the assumed standard of clinical behavior, the instrument’s remaining measurement range, and the configuration that produced the result. The skills required to make these distinctions must become core competencies. Benchmark results are increasingly utilized to support claims about mental health safety that may not be accurate, making it necessary to close the gap between clinical measurement and AI. Plain Language Summary AI chatbots like ChatGPT, Claude, and Gemini are increasingly used by millions of people to discuss mental health problems, including thoughts of suicide. To assess whether these systems handle such conversations safely, researchers give them standardized tests called benchmarks and compare their answers to those of human experts. These scores are already used to argue AI systems are ready for clinical use. This study gave a well-established test of suicide response skills to nine AI models from three major companies under varying conditions. We changed how much instruction the AI received and how much randomness was built into its responses, then measured whether the scores changed. The same AI model could score like a trained crisis counselor under one set of conditions and like an untrained undergraduate under another, depending on choices the person running the test made. Every model also made the same kind of mistake: responses that sounded warm and caring were rated as appropriate, even when experts had judged them to be clinically problematic. The highest-scoring model performed so well that the test could no longer measure whether it was truly skilled or had simply exceeded the test’s range. These findings show that a single score can be misleading without knowing how the test was run, whether it can still distinguish strong from weak performance, and whether it matches what the AI is used for. Mental health professionals routinely make these judgments about clinical assessments and are well positioned to bring that expertise to AI evaluation.

**ИИ:** + · обе модели · LLM-судья · Nine LLMs rated how appropriate helper responses to suicidal clients were on the SIRI-2 items, and their ratings were compared with expert-consensus ratings.

**Решение:** =

---

### 693 · R3928

**Language Experience Shapes Creative Idea Generation**

2026 · The Journal of Creative Behavior · journalarticle, article · en · https://doi.org/10.1002/jocb.70128

ABSTRACT Bilinguals often outperform monolinguals on creative tasks, suggesting a positive link between bilingualism and creativity. However, the inconsistent definitions of both bilingualism and creativity have made it difficult to understand the precise factors driving the association. Here, we examine the relationship between creativity and bilingualism by focusing on the effects of language proficiency and dominance on divergent thinking. Spanish‐English bilinguals and English monolinguals completed the Alternate Uses Task (AUT, a measure of divergent thinking) in each of their languages. Responses were assessed in three ways: number of ideas generated (fluency), the length of each idea (elaboration), and how original each idea was (originality). The originality of each response was scored automatically with a fine‐tuned, multilingual large language model. Results revealed that AUT performance was influenced by the language of testing and by participants' language proficiency, indicating a relationship between language experience and divergent thinking. Specifically, higher proficiency and dominance in each language were associated with more original ideas, demonstrating that people's capacity for creative expression is tied to their linguistic abilities. We conclude that verbal creativity assessments, whether in research or real‐world settings, should take into account language experience, especially in multilingual populations and contexts.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · A fine-tuned multilingual LLM scored AUT originality; the abstract doesn't say whether the scores were checked against human raters.

**Решение:** =

---

### 694 · R3932

**Affording Process Auditability with QualAnalyzer: An Atomistic LLM Analysis Tool for Qualitative Research**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.03820

Large language models are increasingly used for qualitative data analysis, but many workflows obscure how analytic conclusions are produced. We present QualAnalyzer, an open-source Chrome extension for Google Workspace that supports atomistic LLM analysis by processing each data segment independently and preserving the prompt, input, and output for every unit. Through two case studies -- holistic essay scoring and deductive thematic coding of interview transcripts -- we show that this approach creates a legible audit trail and helps researchers investigate systematic differences between LLM and human judgments. We argue that process auditability is essential for making LLM-assisted qualitative research more transparent and methodologically robust. 9 pages, 3 figures, BEA2026 Conference Submission

**ИИ:** ? · обе модели · неясен конструкт · The LLM coded interview transcripts deductively and was compared with human judgments, but the abstract doesn't say whether the codes are psychological constructs.

**Решение:** =

---

### 695 · R3942

**Using LLM-as-a-Judge/Jury to Advance Scalable, Clinically-Validated Safety Evaluations of Model Responses to Users Demonstrating Psychosis**

2026 · Proceedings of IASEAI Conference · journalarticle, conference, preprint/article · en · https://doi.org/10.1609/iaseai.v2i1.43055

General-purpose Large Language Models (LLMs) are becoming widely adopted by people for mental health support. Yet emerging evidence suggests there are significant risks associated with high-frequency use, particularly for individuals suffering from psychosis, as LLMs may reinforce delusions and hallucinations. Existing evaluations of LLMs in mental health contexts are limited by a lack of clinical validation and scalability of assessment. To address these issues, this research focuses on psychosis as a critical condition for LLM safety evaluation by (1) developing and validating seven clinician-informed safety criteria, (2) constructing a human-consensus dataset, and (3) testing automated assessment using an LLM as an evaluator (LLM-as-a-Judge) or taking the majority vote of several LLM judges (LLM-as-a-Jury). Results indicate that LLM-as-a-Judge aligns closely with the human consensus (Cohen's $κ_{\text{human} \times \text{gemini}} = 0.75$, $κ_{\text{human} \times \text{qwen}} = 0.68$, $κ_{\text{human} \times \text{kimi}} = 0.56$) and that the best judge slightly outperforms LLM-as-a-Jury (Cohen's $κ_{\text{human} \times \text{jury}} = 0.74$). Overall, these findings have promising implications for clinically grounded, scalable methods in LLM safety evaluations for mental health contexts. published at IASEAI 2026, preliminary work presented at GenAI4Health workshop at NeurIPS 2025

**ИИ:** + · обе модели · LLM-судья · LLM judges rated safety of responses to users with psychosis and were compared with the human consensus using clinician-informed criteria (Cohen's kappa reported).

**Решение:** =

---

### 696 · R3949

**ClinicalVerifier: A Retrieval-Augmented Pipeline for Detecting Guideline Contradictions in LLM-Generated Mental Health Text**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.20238624

Large language models (LLMs) are increasingly deployed in mental health applications, yet their outputs may silently contradict clinical guidelines, posing serious patient safety risks. This paper presents ClinicalVerifier, a retrieval-augmented generation (RAG) system that automatically detects when LLM-generated clinical text contradicts NICE and WHO evidence-based guidelines. The system combines a FAISS-indexed embedding store of guideline excerpts with an LLM judge (Llama-3.3-70B via Groq), augmented by a Neighbourhood Consistency Scoring (NCS) hallucination probe to produce calibrated combined risk levels (LOW / MEDIUM / HIGH). Guideline sources include NICE CG90, NG185, CG178, NG116, CG53, CG42, and the WHO mhGAP Intervention Guide 2023. Evaluated on a 30-case labelled benchmark spanning safe, uncertain, and contradicts clinical outputs, ClinicalVerifier achieves: 73.3% overall accuracy 95.2% F1 on safety-critical contradiction detection 100% recall on guideline-contradicting cases 100% precision on HIGH combined-risk alerts The system's conservative design ensures no guideline violations are missed, while the dual-signal architecture (RAG verdict + NCS score) minimises false alarms. The pipeline is fully open-source, runs without proprietary API access, and is designed for integration into clinical AI monitoring workflows as a sidecar service.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · An LLM judge rates whether LLM-generated mental health text contradicts guidelines, scored against a 30-case labelled benchmark; who made the labels is unclear.

**Решение:** =

---

### 697 · R3954

**Making medical AI benchmarks clinically interpretable: the case of mental health.**

2026 · BMJ mental health · journal article, journalarticle, review · eng · https://doi.org/10.1136/bmjment-2026-302921

Abstract Medical artificial intelligence (AI) benchmarks are increasingly used to assess the readiness of large language models for health-related tasks, but aggregate performance scores can obscure clinically meaningful variation across domains. HealthBench, an open benchmark of 5000 multi-turn health conversations, represents a salient example: the score is difficult to interpret for decisions about specific clinical use cases, including those with mental health needs. Conversations involving suicidality, psychosis, eating disorders, trauma or relational dependence require recognising ambiguous disclosures, responding safely under uncertainty, avoiding reinforcement of harmful beliefs or over-reliance and knowing when to escalate to human-based crisis support. We propose that HealthBench and similar benchmarks report domain-specific results. To demonstrate feasibility and utility, we adopted OpenAI’s classified dataset to identify 332 mental health conversations, validated against human review (sensitivity 0.980, specificity 1.000, positive predictive value 1.000, negative predictive value 0.980, F1 0.990, inter-rater agreement 99.0%). We analysed mental health domain performance separately from overall HealthBench performance using a stratified random sample of 500 conversations. Across deployments, mental health point estimates differed from overall estimates by −0.034 to +0.047. Mental health domain composition was also uneven: for example, postpartum depression represented 26.8% of mental health conversations compared with 4.5% for suicidal crisis, 0.9% for psychosis and 1.5% for eating disorders. The findings suggest benchmark averages can mask domain-specific insights relevant to clinical safety. We argue that interpretable medical AI evaluation requires transparent domain composition; subgroup and failure mode reporting; calibration against clinically meaningful anchors, including human expert performance; and reproducible versioned analyses as models, grader systems and deployment contexts evolve.

**ИИ:** разошлись — Opus ? (другое: Mainly a position piece, but it reports human validation of an apparently LLM-based classification of mental-health conversations; the construct and classifier are unclear.); Sonnet -1 (обзор, протокол, комментарий, позиция, руководство: Discussion/position paper on reporting domain-specific HealthBench results; the human review only checks topic selection, and no LLM-human coding agreement is reported.)

**Решение:** -

---

### 698 · R3960

**The Effects of Artificial Intelligence in Quality Assessment of Outpatient Mental Health Services on Human Auditors.**

2026 · Applied clinical informatics · journal article, journalarticle, review · eng · https://doi.org/10.1055/a-2961-0302

Abstract BACKGROUND: The use of large language model (LLM)-based artificial intelligence (AI) to assess the quality of outpatient mental health documentation represents an understudied application. Critical questions remain about the effects of exposing human auditors to AI-generated recommendations on auditor efficiency, agreement, and patterns of decision-making. Abstract OBJECTIVES: The objective of this study is to examine how exposure to LLM-generated quality assessments influences auditor performance during reviews of documents of outpatient mental health intake sessions. Abstract METHODS: We conducted a pre-post observational evaluation of 10 trained human auditors who reviewed outpatient mental health intake notes and assigned quality ratings using a standardized 13-item chart audit rubric before and after implementation of LLM support. The AI system used Anthropic Claude Sonnet 4 with a fixed chain-prompting strategy. We assessed item-level pass frequency for each auditor across the pre-AI and post-AI periods, AI-human agreement (the alignment between auditor pass/fail determinations and AI-generated recommendations), and auditing time. The pre-AI period included 9,711 notes (126,243 item-level observations) and the post-AI period included 2,677 notes (34,801 item-level observations). Abstract RESULTS: Following implementation of AI-supported auditing, the mean item-level pass rate increased by approximately 2%. The distribution of auditor-level changes was broad (range: -35 to +35%, standard deviation [SD]: 10%) indicating substantial heterogeneity in individual auditor responses to AI support. High auditor agreement with AI recommendations was associated with larger pass-rate changes for selected rubric items, with some auditors increasing and others decreasing pass rates relative to the pre-AI period. The average time for an auditor to review notes decreased from 8.77 min (SD: 9.64) per review during the pre-AI period to 8.06 min (SD: 10.28) during the post-AI period ( p = 0.002), an 8% improvement equivalent to 71 min saved per 100 notes reviewed. Abstract CONCLUSION: LLM-based AI tools may improve the efficiency of clinical quality assurance workflows, but exposure to AI recommendations may meaningfully change human auditor behavior.

**ИИ:** ? · обе модели · неясен конструкт · Claude rated mental health intake notes on an audit rubric with AI-human agreement, but documentation quality may not be a psychological construct.

**Решение:** =

---

### 699 · R3971

**Supervised Fine-Tuning of Foundation Models for Robust Empathy Detection in Text and Video Interactions**

2026 · Figshare · dissertation/thesis, dissertation · https://doi.org/10.25917/curtin.32755458

This PhD advances our understanding of, and AI algorithms for, detecting empathy in various human interactions. Objective empathy detection is well-positioned to ensure equitable empathy training across healthcare, education, and social support systems. This research developed methods with foundation models to address key barriers in empathy detection: robust learning with noisy labels, uncertainty quantification, and privacy-aware empathy detection. The proposed methods in this research have yielded improved accuracy in empathy detection across five public benchmarks.

**ИИ:** ? · обе модели · другое · Thesis on detecting empathy using benchmarks with human empathy labels; unclear if the foundation models are generative LLMs or encoders.

**Решение:** =

---

### 700 · R3972

**Measuring the Invisible: AI-Powered Assessment of Student Mental States in the Age of Generative AI**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6400738

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests AI assessment of students' mental states, possibly LLM-based, but it doesn't say whether humans coded the same texts.

**Решение:** =

---

### 701 · R3981

**A Patient Simulation Framework for Risk Assessment of Conversational Healthcare AI: Evaluation of an Antidepressant Decision Aid**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2602.11391

Objective: This study develops and validates a patient simulation framework that aligns with the National Institute of Standards and Technology AI Risk Management Framework MAP and MEASURE functions, providing an empirical basis for identifying and characterizing performance risks in conversational clinical AI across medical, linguistic, and behavioral patient variation. We applied the framework to a conversational decision aid for antidepressant selection in major depressive disorder. Methods: The simulator integrates three profile dimensions: (1) medical profiles constructed from All of Us electronic health records using risk-ratio gating; (2) linguistic profiles modeling a health literacy gradient and condition-specific communication; and (3) behavioral profiles representing cooperative, distracted, and adversarial engagement. We generated 500 simulated conversations and evaluated profile fidelity through human annotation and a large language model (LLM) judge, then assessed downstream effects on the AI Decision Aid's concept retrieval and antidepressant recommendations. Results: The patient simulator expressed medical concepts with high fidelity (96.6% accurate across 8,210 concepts), with human inter-annotator agreement of 0.73$\kappa$ and LLM-judge agreement against human annotators of 0.78$\kappa$, both indicating substantial agreement. Behavioral profiles were reliably distinguished (0.93$\kappa$, near perfect agreement), and linguistic profiles showed substantial agreement at the lower bound of the substantial range (0.61$\kappa$), adequate to support profile-level analysis. The framework revealed monotonic degradation in AI Decision Aid performance across the health literacy gradient. Rank-1 concept retrieval increased from 47.6% for limited health literacy to 81.9% for proficient health literacy, with corresponding declines in antidepressant recommendation accuracy.

**ИИ:** ? · обе модели · неясен конструкт · An LLM judge was checked against human annotators on simulated depression conversations, but the constructs are mostly medical concepts and health literacy rather than psychological.

**Решение:** =

---

### 702 · R3985

**Characterizing children’s naturalistic narratives via machine learning**

2026 · DOAJ (DOAJ: Directory of Open Access Journals) · journalarticle/none, article · en · https://doi.org/10.34842/ldr2026-946

Storytelling is a fundamental human behavior, and narrative skill is predictive of success in many domains, such that the development of narrative skill is an important process in childhood and adolescence. The goal of this research was to create and assess a novel method for identifying narratives produced in conversations between children and adults. To do so, we crafted a coding manual with a set of concrete rules and examples for identifying utterances containing narrative behavior. Then we asked trained coders to apply these rules to a set of transcribed conversations between adults and children, drawn from CHILDES. Our results indicated that coders could apply these rules with high inter-rater reliability. The utterances that coders identified had many of the characteristics of narrative defined by prior empirical literature. Further, we trained a version of a large language model (LLM) (GPT-4o-mini) to apply these rules and found that the model could successfully mimic human judgments. These results suggest that it is possible to automatize judgments of narrative behavior for rapid analysis of transcribed conversations at scale. This provides a novel avenue for investigation of the development of storytelling abilities, one which has the potential to generate new insights about the acquisition and use of narrative skill in social contexts.

**ИИ:** + · обе модели · кодирование по кодбуку · Fine-tuned GPT-4o-mini applied a coding manual for narrative behavior in child–adult conversation transcripts; compared with trained human coders.

**Решение:** =

---

### 703 · R3988

**Reliable Self-Harm Risk Screening via Adaptive Multi-Agent LLM Systems**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.22154

Emerging AI systems in behavioral health and psychiatry use multi-step or multi-agent LLM pipelines for tasks like assessing self-harm risk and screening for depression. However, common evaluation approaches, like LLM-as-a-judge, do not indicate when a decision is reliable or how errors may accumulate across multiple LLM judgements, limiting their suitability for safety-critical settings. We present a statistical framework for multi-agent pipelines structured as directed acyclic graphs (DAGs) that provides an alternative to heuristic voting with principled, adaptive decision-making. We model each agent as a stochastic categorical decision and introduce (1) tighter agent-level performance confidence bounds, (2) a bandit-based adaptive sampling strategy based on input difficulty, and (3) regret guarantees over the multi-agent system that shows logarithmic error growth when deployed. We evaluate our system on two labeled datasets in behavioral health : the AEGIS 2.0 behavioral health subset (N=161) and a stratified sample of SWMH Reddit posts (N=250). Empirically, our adaptive sampling strategy achieves the lowest false positive rate of any condition across both datasets, 0.095 on AEGIS 2.0 compared to 0.159 for single-agent models, reducing incorrect flagging of safe content by 40\% and still having similar false negative rates across all conditions. These results suggest that principled adaptive sampling offers a meaningful improvement in precision without reducing recall in this setting.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM multi-agent self-harm risk screening on labeled datasets; AEGIS labels may be human-annotated, but SWMH labels come from subreddits. Reference is unclear.

**Решение:** =

---

### 704 · R4002

**Multi-Objective Alignment of Language Models for Personalized Psychotherapy**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2602.16053

Mental health disorders affect over 1 billion people worldwide, yet access to care remains limited by workforce shortages and cost constraints. While AI systems show therapeutic promise, current alignment approaches optimize objectives independently, failing to balance patient preferences with clinical safety. We survey 335 individuals with lived mental health experience to collect preference rankings across therapeutic dimensions, then develop a multi-objective alignment framework using direct preference optimization. We train reward models for six criteria -- empathy, safety, active listening, self-motivated change, trust/rapport, and patient autonomy -- and systematically compare multi-objective approaches against single-objective optimization, supervised fine-tuning, and parameter merging. Multi-objective DPO (MODPO) achieves superior balance (77.6% empathy, 62.6% safety) compared to single-objective optimization (93.6% empathy, 47.8% safety), and therapeutic criteria outperform general communication principles by 17.2%. Blinded clinician evaluation confirms MODPO is consistently preferred, with LLM-evaluator agreement comparable to inter-clinician reliability.

**ИИ:** + · обе модели · LLM-судья · An LLM evaluator rated therapy responses alongside blinded clinicians, and the abstract says its agreement was comparable to inter-clinician reliability.

**Решение:** =

---

### 705 · R4040

**aipsy-judge: A Specialized, Psychologist-Corrected Local Judge for the Psychological Safety of Conversational AI**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.24899

The standard recipe for LLM-as-judge -- pick a frontier model, or average several -- is actively unsafe for grading the psychological safety of conversational AI. Using aipsy-bench, an open frozen safety instrument, we run a fully-crossed competence study: three frontier models (gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash) serve as both generators and judges of 3,000 mental-health, companion, and coaching messages against a psychologist's ratings. The disagreement is not noise: it is structured, concentrated on the safety-critical metrics, and one judge (Gemini) is an outlier -- the most lenient, carrying a +0.99 self-preference premium, flagging far fewer tail failures, and scoring a means-in-hand self-harm response "exemplary." Inter-judge agreement on empathy, where sycophancy hides, is the lowest in the battery (alpha 0.24). One axis stands apart: the binary crisis-detection flag is the one safety-critical signal judges agree on (alpha 0.80), erring toward over-flagging, the safe direction for a triage screen. Equal-weight averaging, the canonical fix, blends that leniency and tail-blindness into the safety score. Off-the-shelf open-weight judges are worse for a dispositional, not capability, reason -- and disposition is fine-tunable. We therefore distill a per-metric, psychologist-corrected target into a small, frozen, local model, aipsy-judge-1.0, an Apache-2.0 fine-tune of Gemma-4-26B-A4B. aipsy-judge-1.0 tracks the corrected target better than its base on the composite (ICC 0.64 to 0.75) and crisis detection (kappa 0.65 to 0.82), catches 92% of crises with a false-positive lean, and grades more faithfully than any single frontier judge, while every transcript stays on the machine. These are directional readings against a single-expert-informed target, not validated multi-rater agreement. A safety grader that shares a vendor's post-training shares its blind spots. 24 pages, 3 figures, 6 tables. Model available at https://huggingface.co/keidolabs/aipsy-judge-1.0 (Apache-2.0)

**ИИ:** + · обе модели · LLM-судья · LLM judges rate psychological safety, empathy and crisis detection in mental-health conversations, and are compared with a psychologist's ratings (ICC, kappa).

**Решение:** =

---

### 706 · R4046

**Data and analysis scripts for "Performance within the Foundation Paradox: The Case for Small, Qualitative Evaluations" (Neural Computing and Applications, accepted 2026).**

2026 · OSF · text/project, preprint · https://doi.org/10.17605/osf.io/ruafc

This repository contains the scoring data, analysis scripts, and reproducibility materials for the Desert Language Model Evaluation Framework (DLEF) study. Included files support replication of inter-rater reliability analysis, mixed-effects modeling, LLM-as-judge automated scoring, and mechanistic probe analysis of last-layer hidden states. The manuscript itself is not included. The version of record will be available via Neural Computing and Applications upon publication.

**ИИ:** разошлись — Opus ? (неясен конструкт: Data repository: LLM-as-judge scoring alongside human inter-rater reliability, but whether any psychological construct is rated is not stated.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: OSF repository for a general LLM evaluation framework (DLEF); no psychological or clinical text construct is mentioned, only generic LLM-as-judge and probing analyses.)

**Решение:** -

---

### 707 · R4048

**Comparing ANCHOR's Automated Coding to Expert Analyses of a Single Corpus: A Descriptive Concordance Study**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/7num9

ANCHOR (Auditable Non-Convergent Human-Oriented Reflexive coder) is a Dockerized qualitative coding pipeline that uses local large language models in a coder/judge architecture to produce auditable, reproducible codebooks from interview transcripts, with every applied code traceable to a verbatim transcript span. This preregistration covers Paper 2 of the ANCHOR research programme: a purely descriptive study comparing ANCHOR's outputs to two independent expert analyses of the same corpus — the Making Every Contact Count (MECC) corpus of 20 interviews (15 service providers, 5 service users; UK Data Service SN 856448), analysed by Nichol et al. using Reflexive Thematic Analysis (RTA; 2024) and a Strategic Behavioural Analysis using the Theoretical Domains Framework (SBA/TDF; 2025). Three pre-specified research questions span three analytical tracks, with each reference framework assigned to the track its method supports. Track A asks how far ANCHOR's Validation engine reproduces the SBA's domain-level prevalence profile (14 TDF domains, present in N of 20), scored as a descriptive prevalence concordance — Lin's concordance correlation coefficient and Bland-Altman, read co-equally with key-domain set recovery and structural-zero reproduction. Track B asks how far ANCHOR's Discovery engine produces structure that thematically overlaps the RTA framework, via embedding similarity, code-space coverage, and divergence. Track C measures run-to-run reproducibility across repeated runs against a pre-specified stability band. N = 20 does not support inferential testing; all metrics are descriptive. The study is explicitly framed as concordance with one expert team's coding of one corpus (Nichol-on-MECC), not as validation against a gold standard, and it notes that the SBA's own domain-level inter-rater reliability ranged from poor to moderate. A hard sequencing rule governs the work: all corpus runs are executed only after this preregistration is live with a confirmed OSF DOI; a prior five-transcript model-selection exercise (Gate 2) is excluded as non-exposure. Analysis is performed by a version-pinned script (a2_concordance.py v1.0.0, sha256 recorded herein) archived with this registration.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: This is an OSF preregistration (protocol) with no results yet. Its comparisons are at domain-prevalence and theme level, not coding of the same units.); Sonnet ? (другое: Preregistration (protocol-like) of LLM coding of interviews vs expert TDF/RTA analyses; the construct is behavioural and concordance is at prevalence/theme level, so a results paper may exist.)

**Решение:** -

---

### 708 · R4049

**Test-Retest Reliability of LLM Ratings of Delay of Gratification**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/xkf3w

Many important decisions in everyday life require choosing between a smaller immediate reward and a larger reward that is available later. Delay of gratification, or the ability to resist immediate rewards in favor of greater future rewards, is an important decision-making construct that has been associated with a range of meaningful behavioral outcomes, including addiction, retirement saving, and health and exercise behaviors. However, the best way to measure delay of gratification in adults remains unclear. Traditional approaches include choice-based tasks, in which participants select between immediate and delayed rewards (usually monetary rewards), and self-report measures that use Likert-type items. Although both approaches offer advantages, they also present concerns related to validity and reliability. Recent advances in natural language processing (NLP) and large language models (LLMs) have improved the ability to interpret and extract meaningful information from open-ended text, creating new opportunities for more accurate psychological measurement. A recent study of ours (under review) had participants write brief open-text descriptions of their general delay of gratification abilities. We then used two common LLM families (GPT, Claude) to rate the delay of gratification text responses. High inter-LLM reliability in the ratings was observed, as well as high LLM-human interrater reliability. Finally, the relationship between the LLM delay of gratification ratings and target constructs of interest (e.g., impulsivity, self-control, academic procrastination, substance dependency) were stronger than the relationship between these constructs and a traditional choice-based measure of delay of gratification. The primary aim of the present study is to examine the test-retest reliability of LLM-based ratings of delay of gratification (by having participants complete two waves of surveys). A second aim is to determine whether LLM-based ratings of delay of gratification can predict related outcomes over time and whether they provide stronger predictive ability than traditional measures of delay of gratification.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: OSF pre-registration (protocol) of LLM test-retest study; the earlier study it cites (LLM-human reliability) is worth tracing separately.); Sonnet ? (неясно, сравнивали ли с людьми: Pre-registration of LLM ratings of delay-of-gratification texts; the earlier study had LLM-human reliability, but this one targets test-retest, so human comparison is unclear.)

**Решение:** +

---

### 709 · R4080

**PsyCIDRA: A Dual-Agent Framework for Psychiatric Interviewing and Diagnostic Reasoning**

2026 · arXiv (Cornell University) · preprint/article, review, preprint · https://doi.org/10.48550/arxiv.2610.07473

Large language models show promise in clinical reasoning, but psychiatric interviewing requires guiding an evolving conversation. Their ability to carry out this interactive assessment remains less studied. We present PsyCIDRA, a dual-agent framework linking free-form psychiatric interviewing with diagnostic reasoning for expert review. Its interviewer agent uses tools to maintain working notes, load expert-written skills, and retrieve ICD-11 references to guide inquiry. Its diagnostic reasoning agent then receives the completed interview transcript and reports hypotheses alongside supporting, conflicting, and missing evidence, withholding a final hypothesis when none is sufficiently supported. Using patient profiles generated with PsyCPG, we first evaluate PsyCIDRA in simulation. Across four models on 53 evaluation cases, it achieves higher diagnostic agreement than direct prompting. On 81 held-out simulated cases, rank-1 accuracy is 60.5% versus 51.9%. In a blinded study of 101 human participants in separate arms, PsyCIDRA agrees with psychologists on whether to propose a diagnostic hypothesis in 79.6% of cases, compared with 65.4% for direct prompting. Together, these findings support the potential of LLM agents to assist psychiatric assessment through free-form dialogue. By examining diagnostic reasoning, interview quality, and safety together, this study contributes to understanding the capabilities and limitations of psychiatric interview agents. 41 pages, 27 figures, 20 tables; includes appendices

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM diagnostic reasoning from psychiatric interview transcripts compared with psychologists; unclear whether psychologists rated the same transcripts or ran separate assessments.

**Решение:** =

---

### 710 · R4083

**Human Expertise and Large Language Model Embeddings in the Content Validity Assessment of Personality Tests.**

2026 · Educational and psychological measurement · journal article, journalarticle, article · eng · https://doi.org/10.1177/00131644251355485

In this article, we explore the application of Large Language Models (LLMs) in assessing the content validity of psychometric instruments, focusing on the Big Five Questionnaire (BFQ) and Big Five Inventory (BFI). Content validity, a cornerstone of test construction, ensures that psychological measures adequately cover their intended constructs. Using both human expert evaluations and advanced LLMs, we compared the accuracy of semantic item-construct alignment. Graduate psychology students employed the Content Validity Ratio to rate test items, forming the human baseline. In parallel, state-of-the-art LLMs, including multilingual and fine-tuned models, analyzed item embeddings to predict construct mappings. The results reveal distinct strengths and limitations of human and AI approaches. Human validators excelled in aligning the behaviorally rich BFQ items, while LLMs performed better with the linguistically concise BFI items. Training strategies significantly influenced LLM performance, with models tailored for lexical relationships outperforming general-purpose LLMs. Here we highlight the complementary potential of hybrid validation systems that integrate human expertise and AI precision. The findings underscore the transformative role of LLMs in psychological assessment, paving the way for scalable, objective, and robust test development methodologies.

**ИИ:** разошлись — Opus ? (другое: Embedding models (possibly encoder-only) map personality items to constructs; humans and models are both compared with the test key, so direct LLM–human agreement is unclear.); Sonnet -5 (нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM: Embedding-based item-construct mapping of questionnaire items (likely encoder/sentence-embedding models), not generative LLM coding of psychological text against human labels.)

**Решение:** +

---

### 711 · R4095

**Generative AI as a Tool for Content Validation: Establishing Model-Specific Interpretive Benchmarks**

2026 · Academy of Management Proceedings · conference-abstract · en · https://doi.org/10.5465/amproc.2026.22138poster

Content validation is a core component of psychological scale development, traditionally conducted using human raters. Recent work suggests that generative artificial intelligence (AI) and large language models (LLMs) can serve as efficient surrogate raters when prompted with natural-language content validation tasks. However, evidence indicates that LLM-derived content validity estimates may systematically differ from human-based estimates, raising interpretive challenges. This study addresses this gap by developing model-specific interpretative benchmarks for LLM-based content validation. Using 112 published psychological scales from Colquitt et al. (2019), we evaluated content validity with three state-of-the-art lightweight LLMs (GPT-5 mini, Claude Sonnet 4, and Gemini 2.5 Flash) across two established methods: item sorting and item rating. Each scale was evaluated across ten independent iterations per model. Convergent validity was assessed by correlating LLM-derived content validity statistics with corresponding human-derived statistics. Results showed strong convergence between human and LLM estimates (rs = .605), with higher correlations for rating-based statistics than sorting-based statistics. Only rating-task statistics approached recommended convergence thresholds. LLM-derived estimates were consistently higher than human estimates, motivating the development of model-specific interpretative benchmarks. Percentile-based benchmarks are provided to guide the practical use of LLMs in scale content validation.

**ИИ:** ? · обе модели · неясен конструкт · LLMs rate and sort scale items for content validity against human raters; the text is scale items, not participant or clinical text, so eligibility is borderline.

**Решение:** =

---

### 712 · R4098

**GenPT: Beyond Self-Report for Reliable LLM Psychometrics via Generative Projective Testing**

2026 · Annual Meeting of the Association for Computational Linguistics (ACL) · journalarticle, conference, conference-paper · https://doi.org/10.18653/v1/2026.acl-long.1901

Self-report questionnaires remain the prevailing tool for probing the psychological states of persona-conditioned agents (PC-Agents). However, classical instruments inherit two well-known threats: contamination from training corpora and directional bias driven by social-desirability or contextual framing. To overcome these methodological bottlenecks, we ask whether projective paradigms can be adapted into a robust psychometric tool. We introduce \textbf{GenPT} (Generative Projective Testing), which reformulates TAT, Rorschach, and SCT with newly generated stimuli and organizes assessment as a three-stage pipeline to derive standardized psychological indicators and target states. Evaluating PC-Agents induced via CharacterRAG and AnnaAgent profiles, we benchmark GenPT's reliability and validity against classical questionnaires. The results indicate that questionnaires exhibit systematic directional shifts under social-desirability framing, most strongly on suicide ideation. In contrast, GenPT's collected behavioral patterns stay near the symmetric baseline. Furthermore, under a longitudinal counselling context, GenPT-based depression assessment shifts by roughly an order of magnitude more than the questionnaire counterpart when Qwen3 serves as the backbone. Overall, GenPT complements self-report methods in scenarios where contamination resistance, bias asymmetry, and context sensitivity matter. Code and stimuli can be found at https://github.com/sci-m-wang/GenPT.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: An LLM pipeline scores projective-test responses (TAT, Rorschach, SCT) from persona agents. It is benchmarked against questionnaires; no human scoring is mentioned.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: GenPT uses projective tests to assess LLM persona agents; no comparison of LLM coding against human coders is described.)

**Решение:** -

---

### 713 · R4108

**Comment-aware mini knowledge graphs meet LLMs: fine-grained emotion and stance annotation for political news**

2026 · International Conference on Machine Learning and Large Models · conference, conference-abstract · https://doi.org/10.1117/12.3117378

Large language models (LLMs) show strong performance on many text classification tasks, but their judgments on politically charged news comments often lack the background knowledge needed to interpret policies, parties and actors. We study fine-grained emotion and stance annotation for news comments and propose a simple framework that combines an instruction-tuned LLM with a lightweight news knowledge graph. We first build a mini knowledge graph over politicians, parties, policies and key events from publicly available sources. Given a news title and user comment, our pipeline links mentioned entities, extracts a local sub-graph, and summarizes the relevant triples into a short natural-language MiniKG description. This comment-aware MiniKG summary is then injected into the prompt of LLaMA-3-8B-Instruct, which outputs both an emotion label (positive/neutral/negative) and a stance label (support/oppose/neutral/unclear). Experiments on a real-world news comment dataset show that MiniKG-augmented LLaMA achieves consistent gains over lexicon and RoBERTa baselines, knowledge-augmented RoBERTa models, and several prompting-only variants of LLaMA. In particular, it improves stance and emotion Macro-F1 by up to 4–5 points over a text-only LLaMA annotator and achieves the highest Cohen’s κ with human coders. These findings suggest that even a small, domain-focused knowledge graph can substantially enhance LLM-based annotation for political news analysis.

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLaMA labels political news comments for stance and positive/neutral/negative polarity against human coders; this is generic opinion sentiment, not a psychological construct.); Sonnet ? (неясен конструкт: LLaMA annotates emotion and stance in political news comments, with Cohen's κ against human coders. The emotion label is only positive/neutral/negative, so it may count as generic sentiment, and stance is excluded.)

**Решение:** -

---

### 714 · R4121

**Contrastive Distillation of Emotion Knowledge from LLMS for Zero-Shot Emotion Recognition**

2026 · IEEE International Conference on Acoustics Speech and Signal Processing · journalarticle, conference, preprint/article · https://doi.org/10.1109/icassp55912.2026.11463749

Human emotions are diverse and nuanced, making it difficult to design label spaces that capture their full range. Conventional Emotion Recognition models rely on training using fixed label sets and struggle to generalize beyond them. Large Language Models (LLMs) exhibit strong zero-shot performance across a wide range of emotion concepts, but their use is limited by their size and modality: their generalization ability stems from rich, free-form language use, which is difficult for smaller models to learn or replicate. In this work, we propose a contrastive distillation framework that transfers emotion knowledge from the natural language representation space of LLMs into a compact, generalizable emotion embedding space, without relying on human-annotated emotion labels. Our method uses GPT-4 to generate descriptive emotion phrases for each sample. The model learns to align text inputs with emotion descriptions in a shared embedding space. This approach moves beyond class-based distillation and enables zero-shot emotion recognition across diverse emotion taxonomies, granularities, and label formats. Experiments across multiple datasets show that our distilled models outperform strong baselines of similar size, and in some cases, closely match GPT-4's zero-shot performance while being over 10,000× smaller.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · GPT-4 zero-shot emotion recognition is reported on several datasets, which are probably human-annotated; the main focus is distilling GPT-4 into a smaller model.

**Решение:** =

---

### 715 · R4133

**Large Language Model-Generated Synthetic Data for Parole and Probation Detection in Clinical Notes: Development and Evaluation Study.**

2026 · JMIR AI · journal article, med, journalarticle · eng · https://doi.org/10.2196/104586

BACKGROUND Identifying individuals on parole or probation can help inform care pathways and ensure continuity of care in health care systems. However, this sensitive justice-related information is often absent from structured electronic health record fields and is instead documented in narrative clinical notes. Developing automated parole and probation detection (PPD) systems typically requires expert-annotated clinical data, but manual annotation is costly, time-consuming, and constrained by data sparsity and privacy concerns. OBJECTIVE This study aimed to develop and evaluate a synthetic-only training paradigm for PPD from clinical text that eliminates the need for expert-annotated training data while maintaining strong performance and cross-domain transfer to real-world data. METHODS We developed Synth-PPD, a synthetic dataset comprising 7579 labeled clinical notes generated using large language models (LLMs), redundancy filtering, and automated quality evaluation. Dataset quality was assessed through human review of 1517 synthetic notes by 2 annotators. The primary outcome was the macro–F1-score for PPD. We evaluated Synth-PPD across unsupervised and supervised learning settings using LLMs, traditional machine learning models, and transformer encoders. Performance was assessed on 293 expert-annotated real-world clinical notes from the US Department of Veterans Affairs. RESULTS Synth-PPD achieved 90.05% human-LLM alignment. In the unsupervised setting, Llama 3.3-70B-Instruct with chain-of-thought prompting and few-shot examples from Synth-PPD achieved a macro–F1-score of 87.22%, outperforming both the corresponding zero-shot model (80.10%) and the best rule-based baseline (77.55%; P<.001 for all comparisons). In the supervised setting, Llama 3.1-8B fine-tuned on Synth-PPD achieved a macro–F1-score of 81.43%, exceeding the best rule-based baseline (77.55%; P<.001) and achieving a numerically higher score than the substantially larger zero-shot Llama 3.3-70B-Instruct model (80.10%; P=.08). In contrast, traditional machine learning models and transformer encoders exhibited greater performance degradation under domain shift and derived limited benefit from increasing synthetic training data. Additional experiments showed that increasing synthetic training data improved cross-domain performance for LLM-based models but yielded comparatively smaller gains for traditional approaches. CONCLUSIONS Synthetic data generated by LLMs can serve as a scalable, cost-effective, and privacy-preserving alternative to expert-annotated real-world clinical data for PPD from clinical text. The findings demonstrate successful cross-domain transfer to real-world US Department of Veterans Affairs clinical notes.

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: An LLM detects parole/probation status in clinical notes against expert labels, but legal/justice status is a social determinant, not a psychological construct.); Sonnet ? (неясен конструкт: LLMs detect parole/probation status in clinical notes against expert annotations, but the construct is a justice-related social factor, not clearly psychological.)

**Решение:** -

---

### 716 · R4135

**Training Therapeutic Judges and Multi-Agent Systems for Human-Aligned Mental Health Support**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.30887

Large language models show promise for mental health support, yet therapeutic quality improves only when evaluation functions as an actionable control signal rather than a passive metric. We introduce a framework that formulates therapeutic response generation as a decision-refinement problem driven by multi-dimensional, human-aligned evaluation. In Stage I, we introduce TheraJudge, an open-source therapeutic evaluator trained via preference-based optimization on human-annotated data to produce reliable judgments across 7 psychological dimensions. In Stage II, we introduce TheraAgent, which operationalizes TheraJudge's evaluations through a coordinated refinement process with specialized Critic, Coach, and Therapist roles that translate evaluative signals into targeted response revisions. Empirically, TheraJudge achieves strong agreement with clinician ratings, with intraclass correlation coefficients (ICC = 0.87-0.95), surpassing supervised baselines and strong closed-source judges, particularly on critical dimensions such as Safety, Relevance, and Empathy. Acting on these evaluations, TheraAgent yields a +0.43 improvement in human-rated therapeutic quality (on a 5-point scale) under blind evaluation, with 96\% clinician inter-rater reliability. Low-quality responses ($\leq 3$) improve by +2.45 points with a 94\% recovery rate, demonstrating targeted correction of unsafe outputs. Overall, our results indicate that effective alignment of mental-health LLMs stems from acting on human-aligned evaluation, rather than relying solely on stronger generation. We release code at https://github.com/vis-nlp/TheraAlign.

**ИИ:** + · обе модели · LLM-судья · TheraJudge, an LLM judge, rates therapeutic responses on 7 psychological dimensions; its agreement with clinician ratings is reported as ICC 0.87-0.95.

**Решение:** =

---

### 717 · R4138

**Prompt Engineering Strategies for LLM-based Qualitative Coding of Psychological Safety in Software Engineering Communities: A Controlled Empirical Study**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.07422

Qualitative analysis plays a pivotal role in understanding the human and social aspects of software engineering. However, it remains a demanding process shaped by the subjective interpretation of individual researchers and sensitive to methodological choices such as prompt design. Recent advancements in Large Language Models (LLMs) offer promising opportunities to support this type of analysis, although their reliability in reproducing human qualitative reasoning under varying prompting conditions remains largely untested. This study presents a controlled empirical evaluation of three LLMs -- Claude Haiku, DeepSeek-Chat, and Gemini 2.5 Flash -- across two prompt engineering strategies (zero-shot and multi-shot closed coding), using Cohen's kappa as the primary agreement metric over ten independent runs per configuration. Results suggest that multi-shot prompting significantly improves agreement for Claude Haiku (Delta kappa = +0.034, Wilcoxon p = 0.004) but not for DeepSeek-Chat or Gemini 2.5 Flash. Intra-model stability varies substantially -- DeepSeek-Chat and Claude Haiku exhibit the lowest variance (SD approx. 0.017), while Gemini 2.5 Flash is the least stable (SD = 0.038). A systematic over-prediction of "Sharing Negative Feedback" is identified across all models (bias ratios up to 5.25x), alongside consistent under-prediction of "Expressing Concerns." Collectively, these findings provide empirical evidence for prompt engineering guidelines in LLM-assisted qualitative coding for software engineering research. 9 pages, 5 figures. Accepted at the 1st International Workshop on Prompt Engineering for Software Engineering (PROMPT-SE 2026), co-located with the 30th International Conference on Evaluation and Assessment in Software Engineering (EASE 2026), Glasgow, Scotland, United Kingdom, June 9--12, 2026

**ИИ:** + · обе модели · кодирование по кодбуку · LLMs closed-code psychological-safety behaviours in community texts; Cohen's kappa agreement with human qualitative coding is reported.

**Решение:** =

---

### 718 · R4141

**Can LLMs Faithfully Explain Themselves in Low-Resource Languages? A Case Study on Emotion Detection in Persian**

2026 · Language Resources and Evaluation Conference (LREC) · journalarticle, preprint/article, conference-paper · https://doi.org/10.63317/4tds2kffmg7j

Large language models (LLMs) are increasingly used to generate self-explanations alongside their predictions, a practice that raises concerns about the faithfulness of these explanations, especially in low-resource languages. This study evaluates the faithfulness of LLM-generated explanations in the context of emotion classification in Persian, a low-resource language, by comparing the influential words identified by the model against those identified by human annotators. We assess faithfulness using confidence scores derived from token-level log-probabilities. Two prompting strategies, differing in the order of explanation and prediction (Predict-then-Explain and Explain-then-Predict), are tested for their impact on explanation faithfulness. Our results reveal that while LLMs achieve strong classification performance, their generated explanations often diverge from faithful reasoning, showing greater agreement with each other than with human judgments. These results highlight the limitations of current explanation methods and metrics, emphasizing the need for more robust approaches to ensure LLM reliability in multilingual and low-resource contexts.

**ИИ:** + · обе модели · бенчмарк с метками людей · LLMs classify emotions in Persian text; classification performance and influential words are compared against human annotators.

**Решение:** =

---

### 719 · R4142

**Personality, Role, and Expressive Style in Large Language Models: An Interactionist Analysis**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.28037

Prompt-based personality control is a key technique for designing large language model (LLM) dialogue agents that behave consistently across social contexts. However, specifying Big Five personality traits (BFTs) in a prompt does not ensure that the intended traits are expressed in generated utterances. This paper investigates this mismatch from an interactionist perspective, viewing personality expression as a context-dependent outcome shaped by the interplay between trait specification and situational factors. We analyze how perceived BFT expression in LLM-generated dialogue is influenced by three prompt factors: personality traits, dialogue roles, and expressive styles. Using a factorial design that combines six personality conditions, three roles, and three expressive-style conditions, we generate 1,080 LLM-agent dialogues in each of English and Japanese. We then evaluate the target agent's utterances using an LLM-as-a-judge framework to estimate expressed Big Five traits. The results show that expressed personality is shaped not only by explicit trait specification, but also by dialogue role and expressive style. These effects are trait-specific: dialogue role strongly influences Openness, expressive style substantially shapes Conscientiousness and Agreeableness, and explicit trait specification dominates Neuroticism. Even without explicit personality-trait specification, social and expressive conditions induce distinct personality-like impressions. Cross-linguistic comparisons show broadly similar patterns between English and Japanese dialogues, with noticeable differences only under specific combinations of personality, role, and expressive style. These findings suggest that personality control in LLM agents should be understood not as a direct consequence of trait prompting, but as a context-dependent process involving personality specification, social role, and expressive style. 26 pages

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: An LLM judge rates Big Five expression in LLM-generated dialogues; the abstract doesn't say whether the judge was checked against human ratings.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM-as-judge rates personality of LLM-generated dialogues; no human coding comparison reported, and the texts are generated agent output.)

**Решение:** -

---

### 720 · R4145

**Analyzing memories with ChatGPT**

2026 · Journal of Cultural Cognitive Science · article · en · https://doi.org/10.1007/s41809-026-00199-9

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests ChatGPT coding memory narratives, possibly compared with human coders.

**Решение:** =

---

### 721 · R4167

**CLIN: an Objective Framework for Evaluating Creativity in Short Persian Literary Text**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.30754

Evaluating creativity in large language model (LLM) outputs remains challenging because creativity is multidimensional and human-centered. We examine how reliably LLMs evaluate short literary text in Persian, a low-resource language, across multiple evaluation strategies and prompt formulations. We find that LLM-human agreement varies substantially across dimensions: alignment is stronger for structured TTCT-derived properties such as Originality, Fluency, and Elaboration, but considerably weaker for more subjective dimensions, particularly Emotion and Attractiveness. Judgments are also sensitive to prompt formulation, while few-shot prompting, ensembling, and multi-agent debate provide no consistent improvement. Motivated by this dimension-dependent behavior, we investigate whether structured creativity dimensions can instead be approximated using simple, interpretable proxy metrics. We introduce CLIN, which evaluates three TTCT-derived dimensions separately using topic-aware novelty for Originality, contextual lexical clustering for Fluency, and lexical diversity for Elaboration. These proxies achieve human alignment comparable to or better than the strongest zero-shot LLM judge in our setting while requiring substantially lower evaluation cost. Accepted to Findings of EMNLP 2026

**ИИ:** ? · обе модели · неясен конструкт · LLM judges rate creativity of literary texts (TTCT dimensions) against human ratings; unclear whether this is a psychological construct or writing-quality grading.

**Решение:** =

---

### 722 · R4184

**Towards automating the harmonization of diverse mental health scales: a comparison of large language models and human judgements**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/5r7eq_v1

Combining existing mental health datasets offers considerable value, making it possible to answer new research questions, increase statistical power, and replicate findings across different populations. However, a barrier to this process is that different research teams often use different measures/scales when collecting mental health data and when monitoring or measuring patient/participant outcomes. This study examined whether large language models (LLMs) can support retrospective harmonisation of questionnaire data by identifying semantically and conceptually similar items across different scales. A sample of 92 volunteers rated the conceptual similarity of randomly allocated pairs of mental health questionnaire items on a scale from 0 (completely unrelated) to 100 (identical), producing 2,729 item-pair ratings. These ratings were compared with cosine similarity scores for each item-pair, generated by three LLM-based approaches. Linear regression models indicated that cosine similarity scores positively predicted human similarity ratings, with standardised coefficients ranging from β = 0.27 to β = 0.39. However, 10-fold cross-validation indicated limited predictive accuracy when estimating human ratings from cosine scores. Receiver operating characteristic analyses were therefore used to examine whether cosine scores could support threshold-based screening of candidate item pairs. Using binary judgements of whether participants rated item pairs as similar, a cosine similarity threshold of approximately 0.31 provided the best overall balance between sensitivity and specificity. Applied to the present item battery (i.e. manually reviewing item-pairs with a cosine of 0.31 or greater), this threshold would have reduced the number of item-pairs requiring review by approximately 69%. These findings suggest that LLM-derived similarity scores may help make retrospective harmonisation more efficient and replicable by reducing the burden of manual screening. However, the modest predictive performance observed here indicates that LLM outputs should be used to prioritise candidate item pairs for expert review rather than as standalone indicators of item equivalence. Further fine-tuning, validation, and replication across broader sets of constructs and questionnaires are required.

**ИИ:** разошлись — Opus -7 (другое — напишите почему: Compares embedding cosine similarity of questionnaire item pairs with human similarity ratings; this is item harmonisation, not coding psychological text.); Sonnet ? (неясен конструкт: LLM embedding cosine similarity of mental health questionnaire item pairs compared with human similarity ratings; unclear whether this counts as psychological coding or uses generative LLMs.)

**Решение:** -

---

### 723 · R4190

**Conversational AI for Child Abuse Detection Through Multistage Counseling: Model Development and Validation Study.**

2026 · Journal of medical Internet research · journal article, validation study, journalarticle · eng · https://doi.org/10.2196/86536

Background: Child abuse severely disrupts the healthy growth and development of children, resulting in long-term physical as well as emotional consequences. In real-world settings, despite the continuous increase in reported abuse cases, the chronic shortage of certified child abuse professionals has significantly increased the workload of individual counselors, making timely intervention increasingly difficult. Objective; This study aims to reduce the workload of counselors in real-world counseling settings by supporting counseling and child abuse detection processes. We propose a conversational artificial intelligence&ndash;based framework, Conversational Artificial Intelligence for Child Abuse Detection (CACAD), which conducts counseling with children and detects child abuse during the counseling process. Methods: CACAD uses a large language model (LLM) to conduct counseling and to detect 4 types of child abuse: neglect, emotional, physical, and sexual. During the question generation process, the LLM serves as the primary agent, supported by 2 auxiliary modules. In the process of counseling, the LLM first determines whether a child&rsquo;s response provides sufficient information to understand the current situation. If the response is deemed insufficient, the LLM generates follow-up questions to elicit additional information while preserving the context of the previous question. Once sufficient information is obtained, the next question category prediction module predicts the most appropriate category for the subsequent question and passes it to the LLM, enabling more flexible guidance of the counseling flow. In parallel, the abusive question detection module filters out potentially harmful or inappropriate questions to protect children. For abuse detection, CACAD uses an instruction-tuned LLM specialized for child abuse detection, and uncertainty quantification is applied to dynamically flag cases as pending review for counselor confirmation. Results: Experimental results using a Korean child-and-adolescent counseling dataset show that CACAD achieves strong performance in child abuse detection, with an exact match of 0.907 and a macro&ndash;F1-score of 0.939. In addition, CACAD demonstrates effective performance in counseling-related tasks, including next question category prediction and abusive question detection, contributing to coherent and safe counseling interactions. Human evaluation by domain experts further confirms the reliability of CACAD in counseling sessions, and uncertainty-based selective prediction allows the system to dynamically identify cases requiring human review. Conclusions: These findings demonstrate that LLM-based conversational agents can reliably perform child abuse detection within counseling conversations in real-world settings. The results further indicate that such systems can support counseling processes by integrating abuse detection, safe question generation, and uncertainty-aware decision handling in a unified framework.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Instruction-tuned LLM classifies abuse types in child counseling transcripts against what are likely counselor-annotated dataset labels; experts also evaluated it.); Sonnet ? (неясно, кто ставил эталонные метки: An instruction-tuned LLM classifies child abuse types in counseling dialogues. The abstract doesn't say whether the reference labels come from human coders or from case records.)

**Решение:** +

---

### 724 · R4201

**Temporal Analysis of Patient-Centered Sentiment in Clinical Notes for Patients With Mental Health Conditions: Retrospective Cohort Study.**

2026 · Journal of medical Internet research · journal article, journalarticle, article · eng · https://doi.org/10.2196/96771

Background Clinical notes offer rich, longitudinal insights into patient health trajectories. However, existing clinical sentiment analysis primarily evaluates overall note tone rather than the patient's distinct perspective. This gap is particularly critical in mental health care, where patient-perspective sentiment closely correlates with severe clinical outcomes, including mortality. Objective This study aimed to characterize temporal sentiment trajectories and changes in mental health clinical notes. We are specifically interested in the problem from the patient perspective, as this can differ from the overall and the provider-perspective sentiment. Furthermore, we examine its association with postdischarge mortality to check if there is any correlation. Using large language models (LLMs) and lexicon-based methods, we compared and highlighted the strengths and weaknesses of both approaches. Methods We conducted a retrospective analysis of 16,447 clinical notes from 6,382 patients from the Medical Information Mart for Intensive Care IV (MIMIC-IV) database, focusing on the Brief Hospital Course and Discharge Instructions sections for patients with ICD-10 (International Classification of Diseases, Tenth Revision) mental health diagnoses. Sentiment was labeled from 3 perspectives (patient, physician, and general) using 2 LLMs (DeepSeek-7B and Mistral-7B) and compared to lexicon-based tools (ClinSent-lexicon, TextBlob, and VADER [Valence Aware Dictionary and sEntiment Reasoner]). Temporal trends were quantified at the patient level using Kendall τ. Associations between sentiment patterns and mortality were assessed using independent-samples (Welch) t tests. Model performance was evaluated on a manually annotated subset (n=165) using precision, recall, and F 1 -score. Results Temporal sentiment trajectories showed substantial directional change among patients with multiple hospital admissions, with greater fluctuations in Discharge Instructions compared to Brief Hospital Course notes. Patient-perspective sentiment was more balanced, while physician and general perspectives were predominantly neutral. LLMs showed better alignment with patient-centered annotations than lexicon-based methods. Discharge-note sentiment trajectories were significantly more negative among patients who died within 30-90 days of discharge than among survivors across both LLMs. Conclusions Temporal sentiment analysis revealed section-dependent patterns in clinical narratives that partially reflected patient-perceived experience. LLM-based approaches improved alignment with patient-centered sentiment, although overall performance remained limited. These findings underscore the need for larger, more robust datasets and modeling strategies for clinical sentiment analysis.

**ИИ:** разошлись — Opus + (проверка кодирования внутри исследования: DeepSeek and Mistral labelled patient-perspective sentiment in mental health clinical notes; scored against a manually annotated subset (n=165) using F1.); Sonnet ? (неясен конструкт: LLMs labeled patient-perspective sentiment in mental health clinical notes, evaluated against 165 manual annotations; unclear whether sentiment counts as a psychological construct.)

**Решение:** +

---

### 725 · R4206

**Large Language Models in Qualitative Research: Governance, Validity, and the Limits of Computational Assistance**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6577019

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; the title suggests a conceptual governance paper, but it could include empirical validation of LLM qualitative coding.); Sonnet -1 (обзор, протокол, комментарий, позиция, руководство: No abstract; title (governance, validity, limits) suggests a conceptual or position paper on LLMs in qualitative research, not an empirical LLM–human agreement study.)

**Решение:** ?

---

### 726 · R4212

**Anthropology-informed AI: modeling the spiritual-first hierarchy of illness explanation in Arabic-speaking patient communities**

2026 · Frontiers in Communication · journalarticle, article · en · https://doi.org/10.3389/fcomm.2026.1778306

Introduction AI-mediated health communication lacks scalable, evidence-based models of cultural tailoring derived from authentic patient narratives. Methods We developed and validated a hybrid human-AI methodology. A large-scale analysis of 41,393 posts from Arabic-language online mental health forums was conducted. Manual annotation using Kleinman’s Explanatory Model (EM) was followed by fine-tuning a large language model (LLM) to automate this interpretive framework. Results The analysis revealed a distinct, culturally grounded hierarchy: Arabic-speaking patients consistently prioritized divine/spiritual causes first (e.g., God’s will, divine testing, evil eye, jinn), followed by moral/ethical considerations (sin, guilt, repentance), social/familial impact (honor, stigma, reputation), psychological factors, and finally biomedical symptoms. This “spiritual-first” pattern was experimentally tested by comparing spiritually-attuned AI messages versus standard secular biomedical messages. Discussion Spiritually-aligned messages significantly outperformed secular counterparts across all engagement metrics and qualitative indicators of trust, relevance, and intent to seek care, validating that communication respecting patients’ spiritual explanatory models fosters greater resonance and therapeutic alliance. A key limitation is the exclusive focus on mental health narratives; future work should investigate extension to physical illness contexts and clinical outcomes.

**ИИ:** + · обе модели · кодирование по кодбуку · Fine-tuned LLM automates manual Explanatory Model annotation of Arabic mental-health forum posts; validated against human annotation.

**Решение:** =

---

### 727 · R4235

**Resource-Efficient LLMs for Depression Symptoms Screening: Performance and Limitations in Zero Shot Setting**

2026 · Language Resources and Evaluation Conference (LREC) · conference, conference-paper · https://doi.org/10.63317/5fkbms3rp4bo

Depression is the leading cause of global disability and early detection is crucial for effective intervention. Recent advances in large language models (LLMs) offer potential for analyzing text to identify depression symptoms. This work investigates the zero-shot capability of LLMs to recognize nine DSM5 depression symptoms from short-text inputs. We evaluated eight open LLMs with model sizes ranging from 1.5B to 14B parameters using a clinically annotated dataset and assessed both overall agreement and symptom-level performance. Results indicate that while smaller models exhibit limited clinical accuracy, the Qwen 2.5-7B model achieves substantial performance with a Cohen’s Kappa of 0.603 and a Macro F1 score of 0.648. Notably, a performance plateau between the 7B and 14B Qwen variants suggests that model scaling alone does not guarantee improved symptom-level classification, establishing Qwen 2.5-7B as a resource-efficient model. Further analysis of the best-performing model revealed strengths in identifying salient symptoms like suicidal thoughts, but limitations in recognizing core symptoms such as depressed mood and anhedonia. Misclassification analysis reveals that the model frequently misclassifies posts expressing ’depressed mood’ as ’no symptom’ or vice versa, often overlooking indicators of irritability or social withdrawal. These findings suggest that resource-efficient LLMs can support preliminary symptom screening in zero shot settings, but there is risk of overlooking clinically important symptoms without fine-tuning.

**ИИ:** + · обе модели · бенчмарк с метками людей · Open LLMs classify DSM-5 depression symptoms in posts, compared against a clinically annotated dataset using Cohen's kappa and F1.

**Решение:** =

---

### 728 · R4248

**Rapport-building dialogue strategy enhanced with proactivity, personalization, and aizuchi backchannels, and its automatic evaluation in HRI**

2026 · Advanced Robotics · article · en · https://doi.org/10.1080/01691864.2026.2718600

Rapport is a critical factor in interactions, strongly influencing user experience, engagement, and interaction outcomes. Proactive behavior, dialogue personalization, and backchannel responses play key roles in fostering rapport, preventing conversation stalls, and maintaining natural conversational flow. This study integrates these behaviors into a rapport-building dialogue strategy by prompting large language models using the CO-STAR and few-shot frameworks in a human–robot interaction setting. To evaluate dialogue quality and rapport, we conduct behavioral and subjective human evaluations and propose 2S-FLARE, a Two-Stage Feature-Led LLM-Driven Automated Rapport Evaluation framework. 2S-FLARE first extracts interaction-level features grounded in psychological theories of rapport and then performs LLM-based judgment to assess rapport. Experimental results demonstrate that the proposed dialogue strategy significantly enhances engagement and rapport, and that 2S-FLARE shows strong alignment with human judgments from both first-person and third-person perspectives.

**ИИ:** + · обе модели · LLM-судья · An LLM judge (2S-FLARE) rates rapport, an interpersonal construct, in human–robot dialogues and is validated against first- and third-person human judgments.

**Решение:** =

---

### 729 · R4277

**Human vs AI Clinical Assessment: Benchmarking a Multimodal Foundation Model Against Multi-Center Expert Judgment on the Mental Status Examination**

2026 · medRxiv · journalarticle, preprint, ppr · https://doi.org/10.64898/2026.04.17.26351105

The Mental Status Examination (MSE) is the cornerstone of the psychiatric evaluation, yet validating artificial intelligence (AI) against the inherent variance of clinical judgment remains a critical bottleneck. Here we introduce a multi-center framework to benchmark the open-weight multimodal foundation model Qwen3-Omni against independent expert panels at two sites, UTHealth and Yale. Evaluating 396 classifications across 10 MSE domains and three longitudinal timepoints of increasing symptom severity, we found that experts achieved substantial agreement (Gwet’s AC1 = 0.87), whereas the model achieved only moderate alignment (AC1 = 0.70-0.72). Even as the model’s overall pathology prediction rate approximated the experts’, the aggregate equilibrium masked a profound “clinical reasoning gap”. Specifically, the model systematically over-predicted observable signs (e.g., speech, affect) while notably failing in inferential domains requiring the interpretation of latent mental content (e.g., delusions, perceptions). A 4-bit quantization analysis of the model confirmed this mechanistically: reducing model capacity disproportionately degraded inferential reasoning while preserving perceptual feature extraction. Furthermore, model-to-expert agreement degraded linearly as clinical complexity intensified across longitudinal visits (Accuracy: T0 = 84.8-87%; T1 = 80-82%; T2 = 71-73%), whereas expert consensus remained robust. Notably, model errors increased 2.3-to-3.4 fold where human experts disagreed. These findings establish inter-expert variance as an essential measurable baseline for psychiatric AI, demonstrating that true clinical translation requires models to move beyond multimodal perceptual extraction to achieve higher-order diagnostic reasoning.

**ИИ:** ? · обе модели · другое · Qwen3-Omni rates MSE domains against expert panels (AC1), but the input seems multimodal (video/audio); unclear whether it includes transcribed text.

**Решение:** =

---

### 730 · R4307

**Designing an Auditable LLM-Supported Workflow for Qualitative Thematic Analysis**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.30543

Large Language Models (LLMs) offer new possibilities for scaling qualitative analysis, but existing applications often provide limited methodological transparency regarding how qualitative methods are translated into computational procedures. This paper presents an auditable and privacy-preserving computational operationalization of inductive and latent Thematic Analysis (TA). This paper first derives five design principles from the methodological requirements of TA and the conditions introduced by LLM-based inference: preserving interpretative context, maintaining traceable relationships between empirical material and analytical outputs, representing analytical constructs and reasoning explicitly, constraining LLM inference to interpretative tasks, and enabling privacy-preserving local deployment. Second, it presents a proof-of-concept for a two-phase workflow that operationalizes these principles by combining interpretative LLM inference with deterministic procedural control to generate codes, analytical justifications, themes, and theme descriptions while preserving explicit links to the source material. Third, it proposes an evaluation framework combining structural comparison with human-led TA and independent expert assessment of analytical quality. The evaluation is conducted on semi-structured Danish interview transcripts. and the results shows that the workflow produces code-level outputs with coverage broadly comparable to human annotations and highly rated analytical justifications, while generating a more compressed thematic structure characterized by fewer and broader themes. The findings demonstrate the feasibility of auditable LLM-supported TA through a modular workflow designed to scale to larger datasets, accommodate different LLMs, and support transfer across research domains, with domain adaptation primarily requiring adjustments to the prompting strategy.

**ИИ:** разошлись — Opus ? (неясен конструкт: Inductive LLM thematic analysis of interviews; code-level coverage compared with human annotations, but the topic and the same-unit coding are unclear.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Inductive LLM thematic-analysis workflow proof-of-concept; compares generated codes/themes structurally with human TA, with no clear psychological construct or same-unit coding agreement.)

**Решение:** -

---

### 731 · R4328

**MEASURING MEANINGFUL CONTRIBUTION IN GROUP DISCUSSION**

2026 · AI,Computer Science and Information Technology · conference-paper · https://doi.org/10.5121/csit.2026.160419

Traditional measures of participation in group discussions rely on surface-level indicators such as speaking frequency, obscuring the qualitative value of individual utterances. This paper proposes an NLP-based framework for measuring meaningful contribution that emphasizes how utterances advance collective problem solving rather than how often participants speak. We introduce the Meaningful Contribution Score (MCS), an utterance-level, five-dimensional measure spanning semantic and interactional constructs (relevance, novelty, enablement, affect, and decision proximity). Focusing on construct validity, we validate MCS on the GAP corpus using a new human-annotated subset and a three-way comparison between human ratings, heuristic MCS components, and LLM-based judgments. Results show strong alignment for semantic relevance, partial alignment for novelty and enablement, and persistent unreliability for affect, highlighting where lightweight heuristics suffice and where context-aware models are needed for interpretable assessment of contribution.

**ИИ:** ? · обе модели · неясен конструкт · LLM judgments of group-discussion utterances (including affect and enablement) are compared with human ratings, but it's unclear whether these constructs count as psychological.

**Решение:** =

---

### 732 · R4363

**TalkFa: A Unified Benchmark for Farsi Dialogue Generation and Understanding**

2026 · arXiv (Cornell University) · preprint/article, review, preprint · https://doi.org/10.48550/arxiv.2609.01810

Farsi, spoken by more than 120 million people, lacks a comprehensive benchmark for dialogue generation and understanding. We introduce TALKFA, a unified benchmark comprising three complementary datasets: (1) WIKI-FADIAL, 4.2K Wikipedia-grounded dialogues for knowledge-grounded generation; (2) DAILYDIALOG-FA, 6.6K dialogues annotated for dialogue acts and emotions; and (3) PLAYDIAL-FA, 2.1K theatrical dialogues with sentiment labels. While LLMs assist data construction, every dialogue undergoes multi-stage review and revision by native Farsi speakers, and only the final human-approved dialogues are released. Experiments with six LLAMA and MISTRAL models show that LoRA substantially improves dialogue generation while requiring only 25-50% of the training data to recover over 90% of the final performance gains. Across classification tasks, FABERT achieves the best dialogue-act performance, LORA-MISTRAL-7B performs best on emotion recognition, and MISTRAL-24B achieves the highest sentiment score. Human evaluation and independent external validation demonstrate the reliability of the benchmark, while comparisons with GPT-4.1 as an LLM judge reveal that automatic metrics substantially overestimate dialogue quality. Zero-shot evaluation with frontier LLMs further shows that TalkFa remains a challenging benchmark. We will release all datasets, annotation guidelines, code, and checkpoints.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Farsi dialogue benchmark with human-reviewed emotion labels; Mistral/Llama LLMs evaluated on emotion recognition against these labels.); Sonnet ? (неясен конструкт: General Farsi dialogue benchmark with human-annotated emotion labels and zero-shot LLM evaluation; psychological relevance is marginal and the LLM-human agreement focus is unclear.)

**Решение:** +

---

### 733 · R4371

**Towards Consistent Detection of Cognitive Distortions: LLM-Based Annotation and Dataset-Agnostic Evaluation**

2026 · Language Resources and Evaluation Conference (LREC) · journalarticle, preprint/article, conference-paper · https://doi.org/10.63317/4joqxtgdgxq2

Text-based automated Cognitive Distortion detection is a challenging task due to its subjective nature, with low agreement scores observed even among expert human annotators, leading to unreliable annotations. We explore the use of Large Language Models (LLMs) as consistent and reliable annotators, and propose that multiple independent LLM runs can reveal stable labeling patterns despite the inherent subjectivity of the task. Furthermore, to fairly compare models trained on datasets with different characteristics, we introduce a dataset-agnostic evaluation framework using Cohen's kappa as an effect size measure. This methodology allows for fair cross-dataset and cross-study comparisons where traditional metrics like F1 score fall short. Our results show that GPT-4 can produce consistent annotations (Fleiss's Kappa = 0.78), resulting in improved test set performance for models trained on these annotations compared to those trained on human-labeled data. Our findings suggest that LLMs can offer a scalable and internally consistent alternative for generating training data that supports strong downstream performance in subjective NLP tasks.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · GPT-4 annotates cognitive distortions; abstract reports LLM-LLM consistency; agreement with existing human labels likely but not explicit.

**Решение:** =

---

### 734 · R4375

**Can Large Language Models be Used as an Alternative for Human Annotation: A Case Study of Emotion Classification**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-08977-9_25

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Title indicates LLMs compared with human annotators for emotion classification of text; no abstract, so verify details at full text.); Sonnet ? (нет аннотации: No abstract; title suggests LLM vs human annotation of emotion classification, which is compatible, but the text type and human comparison are unclear.)

**Решение:** +

---

### 735 · R4388

**Toward a Culture-Aware Vietnamese Mental Health Support Chatbot with Large Language Models**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-981-92-2597-2_42

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; chatbot development paper probably focused on generation, but it could include LLM-judge evaluation checked against humans.

**Решение:** =

---

### 736 · R4422

**Who We Are, Where We Are: Mental Health at the Intersection of Person, Situation, and Large Language Models**

2026 · Workshop on Computational Linguistics and Clinical Psychology · audiovisual/conference talk, journalarticle, preprint/article · https://doi.org/10.18653/v1/2025.clpsych-1.27

Mental health is not a fixed trait but a dynamic process shaped by the interplay between individual dispositions and situational contexts. Building on interactionist and constructionist psychological theories, we develop interpretable models to predict well-being and identify adaptive and maladaptive self-states in longitudinal social media data. Our approach integrates person-level psychological traits (e.g., resilience, cognitive distortions, implicit motives) with language-inferred situational features derived from the Situational 8 DIAMONDS framework. We compare these theory-grounded features to embeddings from a psychometrically-informed language model that captures temporal and individual-specific patterns. Results show that our principled, theory-driven features provide competitive performance while offering greater interpretability. Qualitative analyses further highlight the psychological coherence of features most predictive of well-being. These findings underscore the value of integrating computational modeling with psychological theory to assess dynamic mental states in contextually sensitive and human-understandable ways.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: CLPsych task predicting likely human-annotated well-being/self-states; unclear whether a generative LLM directly codes text against human labels.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): Predicts well-being from social media features with interpretable models; no LLM coding compared against human labels is described.)

**Решение:** -

---

### 737 · R4439

**Evaluating Generative AI for Identifying Ethical, Legal, and Social Dimensions in Migration Narratives: A Case Study of Ukrainian Discourse**

2026 · Social Sciences · journalarticle, article · en · https://doi.org/10.3390/socsci15060341

Collective endorsement of shared values across diverse social groups is essential for the development and sustainability of democratic societies, yet capturing the perspectives of marginalised populations remains a persistent challenge, particularly when examined through ethical, legal, and social (ELS) lenses. This study develops a structured Migration ELS taxonomy to guide a GenAI-assisted semantic classification model designed to identify ELS dimensions in textual data. The model is fine-tuned and evaluated within a human-in-the-loop framework using expert annotations to ensure reliability and interpretive accuracy. As an empirical case, the approach is applied to migration-related official policy documents and narratives of Ukrainian migrants published on the Telegram platform. The resulting framework enables the analysis of alignment between governmental and migrant perspectives, revealing thematic and temporal divergences in ELS dimensions across institutional and user-generated discourse. The findings demonstrate the potential of this scalable framework, which combines taxonomy-driven modelling with generative AI and expert-in-the-loop validation, to reveal patterns of alignment and temporal dynamics in the representation of values across different social groups.

**ИИ:** разошлись — Opus ? (неясен конструкт: GenAI classifies migrant narratives against expert annotations, but ethical/legal/social value dimensions may not count as a psychological construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Classifies ethical, legal, social dimensions in migration policy documents and Telegram posts; this is a sociopolitical taxonomy, not a psychological or clinical construct.)

**Решение:** -

---

### 738 · R4446

**PoETIC: A Re-framing of Context Dependent Emotion Detection**

2026 · Language Resources and Evaluation Conference (LREC) · conference-paper · https://doi.org/10.63317/4f24agmr53nm

Emotion classification has been extensively studied, with numerous datasets enabling progress in both textual and multimodal settings.However, most existing text-based resources treat emotion as an utterance-level property, assuming that the emotional content is fully encoded in the sentence itself.This assumption is problematic: in the absence of paralinguistic cues such as prosody, facial expressions, or emojis, textual emotions are often highly context-dependent.Many utterances lack explicit emotion markers, and even when present, such cues may be overridden by broader situational context.Sentence-level emotion annotation, thus, is driven by the annotator's ability to imagine the context in which the given utterance would elicit a given emotion.An utterance may be able to express an emotion completely (Emotion Obvious), or it can express an emotion when imagined in a certain context (Emotion Plausible).Also, for an utterance, certain emotions might be implausible to express given the specific wording of a sentence (Emotion-Implausible).To address these issues, we create a new paradigm for emotion classification by categorizing utterance and emotion pairs into context-dependency classes.We present the PoETIC benchmark dataset, where sentences in the GoEmotions dataset are human-annotated for the three aforementioned classes across seven emotions (Fear, Anger, Sadness, Joy, Disgust, Surprise, and Neutral).We observe that gold-tagged emotions in GoEmotions do not have a clear correlation with human judgment with respect to the ability to express other emotions, given different contexts.Human annotators identify significantly more plausible emotions for a given utterance if asked to imagine a plausible context per utterance-emotion pair.We also present baselines using three popular large language models and two "small" language models in zero-shot and few-shot settings on the benchmark dataset.

**ИИ:** + · обе модели · бенчмарк с метками людей · Benchmark of human-annotated emotion context-dependency labels on GoEmotions posts; LLM baselines evaluated against human labels.

**Решение:** =

---

### 739 · R4451

**Evaluating the Impact of Human-LLM Interaction on Creativity: A Process-Based Framework**

2026 · University of Michigan · dissertation/none, dissertation · en · https://doi.org/10.7302/dspace/29196

As large language models (LLMs) become embedded in collaborative idea generation, it remains unclear how partnering with LLMs alters the creative engagement and psychological experience of individuals. In this study, we compared the brainstorming dialogues of human-human and human-LLM to examine how the creative behavior and experiential responses of the human contributor shift between types of partners. Using a between-subjects design, participants engaged in structured brainstorming dialogues with either an LLM or human partner. We defined three dimensions of interactional creativity: participation, novelty, and appropriateness. We tracked these dimensions to understand how they evolved across conversational turns. These dimensions were also operationalized using computational linguistic measures and successfully validated against expert human ratings. We also examined how these dynamics were related to participants' overall experience, their confidence in the perceived outcome, accountability, and emotional arousal and valence. The results show that collaboration with an LLM increased novelty but reduced participation, appropriateness, outcome confidence, and positive affect relative to human-human interaction, suggesting that while LLM partnership may amplify ideational expansion, it may simultaneously attenuate sustained participation and contextual grounding, highlighting the need to design Human-LLM interactions that support all dimensions of creative contribution. By jointly assessing individual contribution, experience, and emotional change, this thesis proposes a multidimensional framework for evaluating human creative engagement in collaborative settings. This framework provides a basis for benchmarking how different LLM systems shape the creative experience of their human partners.

**ИИ:** разошлись — Opus ? (другое: Creativity dimensions in dialogues scored by computational measures checked against expert ratings; unclear if an LLM did the scoring or only embeddings.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM is a brainstorming partner; computational linguistic measures are validated against expert ratings, but no LLM codes or rates the text.)

**Решение:** -

---

### 740 · R4460

**Large language model evaluation and feedback of transcribed simulated physician-patient verbal interactions.**

2026 · Frontiers in artificial intelligence · journal article, med, journalarticle · eng · https://doi.org/10.3389/frai.2026.1936749

Introduction Physician-patient verbal interactions are fundamental to clinical care and medical education, yet their evaluation is time-intensive and subject to inter-rater variability. We evaluated whether large language models (LLMs) can accurately assess transcribed standardized patient-physician verbal interactions and generate useful narrative feedback. Methods In this single-center study, 12 standardized patient-medical student encounters were independently evaluated by ChatGPT-4o, Gemini 3 Pro, and a physician reviewer using a gold standard rubric composed of 55 history-taking elements and 19 presentation elements assessing diagnostic reasoning, management planning, and patient counseling. Agreement was assessed using Cohen's kappa and intraclass correlation coefficients. Narrative feedback generated by the LLMs was independently evaluated by ChatGPT, Gemini, Claude, and a physician reviewer. Results Across raters, mean scores were similar, with 35-36 of 55 history-taking elements and 13-14 of 19 presentation elements identified as present. Agreement was high for history-taking elements ( κ = 0.84-0.89; intraclass correlation coefficients = 0.93-0.97) and lower for presentation elements ( κ = 0.62-0.72; intraclass correlation coefficients = 0.61-0.83). Both LLMs generated detailed, accurate, and clinically useful narrative feedback. Discussion These findings demonstrate that LLMs can reliably evaluate simulated physician-patient interactions and may support standardized assessment of clinical communication for research, quality improvement, and medical education.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs vs physician rated standardized-patient transcripts on a rubric (κ reported); mostly medical history-taking checklist, clinical communication construct borderline.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs vs physician scoring history-taking checklist in medical student encounters; medical education competence, not a psychological construct.)

**Решение:** -

---

### 741 · R4495

**From vulnerability to recovery: An eight-stage integrative model of substance use disorder derived from qualitative content analysis of 991 first-person narratives.**

2026 · The International journal on drug policy · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.drugpo.2026.105521

Substance use disorder (SUD) is a multifaceted crisis shaped by the interaction of biological, psychological, relational, and structural forces across the life course. Despite the proliferation of integrated SUD frameworks, existing models insufficiently address stage-based progression, institutional barriers, socio-structural determinants, and the lived mechanisms connecting vulnerability to initiation, entrenchment, crisis, and recovery. This study addresses these gaps through qualitative content analysis of 991 in-depth interview transcripts drawn from Soft White Underbelly, a publicly accessible YouTube series documenting first-person narratives of individuals experiencing significant social marginalization and long-term substance use. Guided by grounded theory coding procedures and large language model-assisted text processing across approximately 3.9 million words, the analysis produced 100 open codes, 27 axial codes, and 8 selective codes, organized into an eight-stage sequential model of SUD progression spanning Early Developmental Vulnerability, Initiation Pathways, Survival and Street Adaptation, Dependence and Entrenchment, Crisis and Acute Risk, Treatment Exposure and Barriers, Recovery and Reorientation, and Relapse or Stabilization. The model advances existing theory by specifying the connecting mechanisms through which each stage generates conditions for the next. Key findings demonstrate how early adversity produces cascading vulnerability, how cognitive distortions sustain treatment resistance, and how compounding exclusion loops, combining stigmatizing beliefs, structural access barriers, and missing identification documents, systematically remove individuals from care regardless of motivational readiness, making structural reform as essential as motivational intervention. The model provides an empirically grounded, stage-specific framework for designing prevention and intervention strategies aligned with the lived realities of those most severely affected by SUD.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM-assisted grounded-theory coding of SUD narratives; unclear whether LLM coding was checked against human coders.

**Решение:** =

---

### 742 · R4523

**Deployment-oriented evaluation of large language models for Arabic emotion classification**

2026 · Scientific Reports · article · en · https://doi.org/10.1038/s41598-026-70263-5

Large Language Models (LLMs) are increasingly used for emotion classification, yet Arabic evaluations remain limited and typically emphasise predictive performance alone. This study presents a deployment-oriented evaluation framework for Arabic emotion classification that complements conventional accuracy-based assessment with measures of output validity, operationalised through coverage and unknown rate, together with strict versus covered evaluation. The evaluation is conducted on 1002 manually annotated Arabic sentences spanning five emotion categories, with very high inter-annotator agreement ( \(\kappa = 0.9722\) ). We evaluate multiple proprietary and open-weight LLMs under a harmonised zero-shot setting and further examine the effects of few-shot prompting, three-vote stochastic aggregation, and run-to-run stability. Supervised Arabic encoder baselines, AraBERT and MARBERT, are additionally included as contextual task-specific reference models. The results show that the highest-performing LLMs combine strong predictive performance with high output validity, while differences in non-evaluable outputs are model- and protocol-specific. Few-shot prompting improves performance for most, but not all, evaluated models, whereas three-vote aggregation produces inconsistent effects across systems. Overall, the findings demonstrate that deployment-oriented indicators provide complementary information beyond predictive performance and support a more transparent evaluation of Arabic emotion classification systems under controlled inference conditions.

**ИИ:** + · обе модели · бенчмарк с метками людей · Several LLMs classify emotions in 1002 Arabic sentences and are scored against human annotations (κ=0.97 between annotators), so LLM–human agreement is reported.

**Решение:** =

---

### 743 · R4529

**Beyond Polishing: An Exploratory Comparison of Editor- and Challenger-Style AI Prompts on Problem Framing in Data Science Education**

2026 · Universität Koblenz · text/master thesis · https://doi.org/10.82549/opus4-2690

Generative KI-Tutorensysteme verfeinern überwiegend Formulierung, Struktur und Machbarkeit der Ausgangsformulierung eines Problems durch die Studierenden. Ob KI-Unterstützung, die stattdessen Gegenvorschläge unterbreitet – alternative Problemrahmungen, Stakeholder-Perspektiven und das Hinterfragen von Annahmen –, die Originalität der resultierenden Problemformulierung verändert, ist eine offene empirische Frage für die Datenwissenschaftsausbildung. Diese Arbeit untersucht diese Frage in einer explorativen Studie mit dreißig Masterstudierenden der Universität Koblenz. Jede Teilnehmerin und jeder Teilnehmer interagierte mit einer eigens entwickelten Web-Plattform, die durch drei aufeinanderfolgende Phasen führte: eine Editor-KI-Phase, eine Challenger-KI-Phase und eine abschließende KI-freie Synthese. Das Endthema wurde auf vier Dimensionen (Originalität, Machbarkeit, Begründungsqualität, Klarheit) von einer domänenkundigen Person sowie von einem LLM-Zweitbewerter (Anthropic Claude), beide verblindet für die Gruppenzugehörigkeit, bewertet. Da das ursprünglich geplante kontrollierte Crossover-Design nicht umgesetzt werden konnte, wurden die Teilnehmenden post-hoc in eine Editor-beeinflusste und eine Challenger-beeinflusste Gruppe sortiert, basierend auf triangulierten Selbstauskunfts- und Präferenzdaten. Themen aus der Challenger-beeinflussten Gruppe erhielten deutlich höhere Originalitätsbewertungen (Cohens d = 3.67, 95% KI [2.50, 4.84]); Themen aus der Editor-beeinflussten Gruppe waren machbarer und klarer formuliert. Ein unerwarteter Sekundäreffekt zeigte sich zugunsten der Challenger-beeinflussten Gruppe in der Begründungsqualität. Aufgrund der post-hoc definierten Gruppen und der festen Reihenfolge sind diese Ergebnisse als Assoziationen, nicht als kausale Wirkungen, zu lesen. Die Arbeit liefert empirische Hinweise, methodische Dokumentation eines hybriden Mensch-LLM-Bewertungsverfahrens und Designhinweise für Bildungs-KI-Werkzeuge. Generative AI tutoring tools predominantly refine the wording, structure, and feasibility of a student’s initial problem framing. Whether AI assistance that instead poses counter-proposals – alternative framings, stakeholder perspectives, and questioned assumptions – changes the originality of the resulting framing is an open empirical question for data science education. This thesis investigates that Question in an exploratory study with thirty postgraduate students at Universität Koblenz. Each participant interacted with a bespoke web platform that walked them through three fixed-order stages on a sharedWi-Fi-dormitory dataset description: an Editorstyle AI stage, a Challenger-style AI stage, and a final unassisted synthesis. The final synthesis topic was rated on four dimensions (originality, feasibility, reasoning quality, clarity) by a human expert rater and an LLM second rater (Anthropic Claude) blinded to group assignment. Because the planned counterbalanced within-subjects crossover could not be implemented, participants were sorted post hoc into an Editor-influenced and a Challengerinfluenced group based on triangulated self-reported impact and preference. Topics from the Challenger-influenced group were rated substantially higher on originality (Cohen’s d = 3.67, 95% CI [2.50, 4.84], p &lt; .001, ICC = 0.859); topics from the Editor-influenced group were rated higher on feasibility (d = −2.04, 95% CI [−2.92,−1.16]) and clarity (d = −1.07, 95% CI [−1.84,−0.30]); a secondary unexpected association favoured the Challenger-influenced group on reasoning Quality (d = 1.03, 95% CI [0.27, 1.79]). The latter three dimensions had inter-rater reliability below the pre-specified 0.70 threshold and their effect-size magnitudes are interpreted as exploratory estimates. Perception data and open-ended responses suggested participants treated the two AI styles as functional complements assigned to distinct task-contexts, and 94% indicated interest in an integrated switcher mode. Because the analytic groups were defined by self-report and because the stage order was fixed, these results should be read as associations rather than causal effects of prompt style. The thesis contributes (a) empirical evidence of large betweengroup differences in framing originality consistent with a counter-proposal mechanism; (b) a methodological case study of a hybrid human-LLM rating protocol with dimension-specific reliability documentation; and (c) design directions for educational AI tools that surface, rather than choose for the learner, the kind of cognitive assistance offered.

**ИИ:** ? · обе модели · неясен конструкт · Claude and a human expert both rated student problem framings (originality, feasibility, clarity) and ICC is reported; unclear whether rating originality counts as a psychological construct.

**Решение:** =

---

### 744 · R4533

**Automating thematic review of prevention of future deaths reports: concordance study of a child-suicide analysis using large language models.**

2026 · BMJ mental health · journal article, journalarticle, review · eng · https://doi.org/10.1136/bmjment-2025-302212

BACKGROUND: Prevention of future deaths (PFD) reports issued by coroners in England and Wales identify systemic safety hazards but are difficult to analyse at scale. Reports are not machine-readable, lack consistent metadata and cannot be reliably searched or exported, meaning prior national reviews have relied on labour-intensive manual screening and coding. OBJECTIVE: To evaluate whether a fully automated, vision-enabled large language model (LLM) pipeline (PFD Toolkit) can replicate and extend the Office for National Statistics (ONS) thematic review of child-suicide PFD reports, and to assess concordance with blinded clinical adjudication. METHODS: All PFD reports published between July 2013 and November 2023 (n=4730) were scraped from judiciary.uk and processed using PFD Toolkit, which combines optical character recognition with LLM-powered screening and thematic coding. Reports were classified for child suicide (≤18 years), addressee categories and 23 coroner-concern subthemes mirroring the ONS coding frame. Agreement was evaluated against a blinded clinical reference standard: three psychiatrists independently adjudicated a stratified sample of 146 reports (73 Toolkit-positive cases and 73 decoys), with disagreements resolved by consensus. Inter-rater reliability and index-reference agreement were quantified using kappa statistics. FINDINGS: The Toolkit identified 73 child-suicide PFD reports between July 2013 and November 2023, compared with 37 identified in the ONS review. 62 cases fell within the ONS analytical window, and 11 pre-dated the introduction of suicide-related tags on the PFD archive. Pre-consensus inter-rater reliability among clinicians was substantial to almost perfect (Fleiss' κ=0.75, 95% CI 0.65 to 0.84). Post-consensus agreement between the Toolkit and the clinical reference standard was substantial to almost perfect (Cohen's κ=0.93, 95% CI 0.77 to 1.00; raw agreement 97%). End-to-end screening, coding and tabulation of all reports completed in 5 min 29 s on a consumer-grade laptop. CONCLUSIONS: A national thematic review of child-suicide PFD reports can be fully automated with high concordance to expert judgement, dramatically reducing time and labour while recovering previously missed cases. CLINICAL IMPLICATIONS: Automated analysis of PFD reports enables rapid, reproducible surveillance of recurring system failures, supporting more timely public health intelligence, policy responses and learning from coronial data.

**ИИ:** + · обе модели · кодирование по кодбуку · LLM coded coroner reports for child suicide and concern subthemes; agreement with blinded psychiatrists' coding of the same reports, κ=0.93.

**Решение:** =

---

### 745 · R4547

**Comparing ChatGPT-4o and Gemini 1.5 Pro in Adolescent Psychiatric Emergencies: A Real-World Evaluation of AI Support in Suicide Risk Assessment.**

2026 · Clinical child psychology and psychiatry · journal article, med, journalarticle · eng · https://doi.org/10.1177/13591045261447933

ObjectiveThis study aimed to evaluate the performance of large language models-ChatGPT-4o and Gemini 1.5 Pro-in assessing suicide risk and guiding treatment in adolescents presenting to the emergency department with suicidal ideation and/or attempts.Materials and MethodsA retrospective review was conducted on child psychiatry consultation notes from 36 adolescents evaluated between February and March 2024. Structured clinical data were entered into ChatGPT and Gemini, and the resulting decisions were compared to those made by clinicians regarding hospitalization, sedation need, medication initiation, follow-up timing, and notification of social services or law enforcement.ResultsChatGPT showed higher concordance with clinicians than Gemini, especially in hospitalization (41.6% agreement) and sedation decisions (100% agreement). ChatGPT recommended hospitalization in 58.3% of cases, compared to 33.3% by clinicians and 36.1% by Gemini. For outpatient cases, ChatGPT demonstrated partial alignment with clinical decisions on medication and follow-up, while Gemini's responses were often uncertain or incomplete.ConclusionLarge language models show promise as decision-support tools in adolescent psychiatric emergencies. ChatGPT was more consistent with clinical judgments than Gemini. However, limitations remain, and further studies involving broader populations are needed before routine clinical integration.

**ИИ:** ? · обе модели · неясен конструкт · LLMs given psychiatric consultation notes; outputs compared with clinicians' management decisions. Unclear whether suicide-risk ratings themselves were compared.

**Решение:** =

---

### 746 · R4572

**Prediction Market Study**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/eagpj

Prediction markets — platforms where participants trade contracts tied to real-world outcomes — are widely regarded as among the most accurate collective forecasting instruments available. Yet the psychological conditions under which crowd accuracy holds or systematically fails remain poorly understood. This project provides the first large-scale empirical test of whether the psychological content of predicted events shapes collective forecasting accuracy in real-money prediction markets. We analyze a large archival dataset of resolved binary prediction markets from Polymarket (polymarket.com), a decentralized prediction market platform where participants stake real capital on binary-outcome events spanning politics, finance, sports, geopolitics, and science. Each market is coded for psychological features — emotional valence, emotional salience, perceived controllability, temporal horizon, geographic scope, and linguistic complexity — using a validated LLM-based coding procedure with human rater validation. Our primary outcome measure is Brier score, a proper scoring rule quantifying the accuracy of crowd probability estimates against binary resolution outcomes. We test six pre-registered directional hypotheses: (H1) collective accuracy varies significantly across content domains, with political markets showing lower accuracy than constrained quantifiable domains; (H2) emotionally salient markets show greater miscalibration via correlated forecaster errors; (H3) higher perceived controllability of outcomes predicts greater accuracy; (H4) negatively valenced markets show systematically inflated crowd probability estimates consistent with negativity bias; (H5) higher market volume — as a proxy for independent forecasters — predicts lower Brier scores, consistent with the wisdom-of-crowds effect; and (H6) longer temporal horizons between market open and resolution predict lower accuracy, consistent with Construal Level Theory. The stopping rule was determined prospectively via power analysis: the binding constraint is calibration curve reliability, requiring at least 50 markets per probability decile bin per domain, which necessitates a minimum of N = 10,000 qualifying resolved markets (preferred) or N = 8,000 at exhaustion of the available market universe. Data collection, analysis code, LLM coding prompts, and human validation ratings will be made publicly available on OSF upon manuscript submission.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: Pre-registration protocol with no results; LLM coding of market emotional features with human validation is planned, not reported.); Sonnet ? (неясен конструкт: Pre-registration: LLM codes market texts for emotional valence and controllability with human rater validation. Text is not typical psychological text, and agreement results are uncertain.)

**Решение:** -

---

### 747 · R4590

**Quantifying the Intensity of Online Social Support via Large Language Model-Based Evidence Extraction: Development and Validation Study.**

2026 · Journal of medical Internet research · journal article, validation study, journalarticle · eng · https://doi.org/10.2196/95025

Abstract Background Online social support, the interaction among individuals in which one helps another during difficult situations through online platforms such as online forums or social media, has proliferated as a vital tool for personal mental health care. Despite the growing usage and importance of online social support, prior studies have mainly focused on either understanding the characteristics of support seekers or merely identifying types of support, which leaves room for improvement in 2 key areas. First, the intensity of support, indicating the strength of willingness provided by supporters, has been studied little. Second, existing models rely heavily either on handcrafted features or on simple text embeddings of the entire message, which, respectively, fail to capture comprehensive textual features or to provide explainability in classification model decisions. Objective This study proposes a deep learning model that not only predicts the intensity of online social support but also provides human-readable evidence that explains the reasoning behind the decision made by the proposed model. While prior studies mainly concentrated on the task of identifying support types, this research quantifies the strength of support, which may better explain how strongly supporters seek to deliver informational and emotional support. Methods The proposed model categorizes informational and emotional support into 3 levels—strong, moderate, and weak. It collaborates with a large language model (LLM) to extract key sentences or phrases expressing supportive intent and to compute sentiment scores from both the original post and the reply. All extracted texts are then encoded as a vector representation whose elements indicate the presence of text segments corresponding to predefined features. All the computed features are finally fed into the neural network layers for intensity classification. The proposed model was evaluated on 2 independent, human-annotated datasets collected from previous studies, which consist of 1000 and 400 pairs of support-seeking posts and their associated supporting comments, respectively. Results The model achieved superior accuracy compared to baselines on both datasets (0.728/0.694 and 0.709/0.598 for informational support and emotional support, respectively). Through a case study of representative examples, we show that the extracted texts serve as useful evidence explaining the decisions made by the proposed model. For example, explicit intent to support (eg, providing a detailed solution or showing strong empathy) is successfully extracted and used to detect strong support, whereas only indirect support (eg, telling personal stories or offering general advice) is present and can be captured as weak support. Conclusions Through cooperation with LLMs, quantifying the intensity of online social support is highly achievable. In addition, the sentences extracted by LLMs can be used to explain the decisions made by the proposed model.

**ИИ:** ? · обе модели · другое · An LLM extracts features for a neural classifier of social-support intensity, scored against human labels. The LLM is not the direct rater; baselines may include LLMs.

**Решение:** =

---

### 748 · R4595

**Toward Accessible Psychotherapy Training Using AI-Driven Interactive Patient Avatars**

2026 · IEEE International Conference on Healthcare Informatics (ICHI) · journalarticle, conference, other/conference paper · en · https://doi.org/10.1109/ichi69079.2026.00124

Training psychotherapists in evidence-based interventions such as Acceptance and Commitment Therapy (ACT) requires repeated practice with meaningful feedback, yet opportunities for safe, standardized training are limited by ethical, logistical, and resource constraints. We introduce a system designed to support ACT-oriented psychotherapy training through spoken dialogue with an embodied virtual patient. The system uses large language models to simulate patient behavior conditioned on profiles derived from real therapy sessions and configurable clinical scenarios, while a separate automated evaluator provides turn-by-turn feedback on therapist responses based on established ACT fidelity criteria. Rather than aiming to replace supervision, the system is intended to support deliberate practice by enabling experimentation, reflection, and immediate feedback in low-risk settings. Expert evaluation with practicing psychologists confirmed high realism in patient behavior and demonstrated that immediate turn-by-turn ACT feedback increased therapists' awareness of intervention choices and enabled effective experimentation with alternative responses. Quantitative evaluation across 49 therapy transcripts identified GPT-4o-mini as the optimal feedback model, achieving the lowest mean absolute error (MAE = 6.12) in replicating human supervisor ACT fidelity ratings with statistically significant agreement. This work demonstrates the potential of fidelity-aware simulated patients as a scalable complement to psychotherapy training.

**ИИ:** + · обе модели · кодирование сессий · LLM rated ACT fidelity in 49 therapy transcripts against human supervisor ratings (MAE, agreement reported).

**Решение:** =

---

### 749 · R4612

**Reliability in Judging Basic Emotions: Lessons from Session Transcripts**

2026 · Psychiatry International · journalarticle, article · en · https://doi.org/10.3390/psychiatryint7050230

Background/Objectives: Psychotherapists have become increasingly interested in identifying how recurrent emotional themes might add value to the clinical process, especially in the context of recent developments in affective neuroscience. However, much of this literature remains anecdotal, and it is unclear whether therapists can reliably identify these emotions in routine practice, especially in the context of a free-flowing narrative. In a parallel development, large language models (LLMs) have recently been deployed to classify emotion from narrative texts, though this literature has yet to be aligned with the findings of modern affective neuroscience. Methods: The present study addresses this gap directly and, to our knowledge, represents the first attempt to code psychotherapy transcripts using both independent human raters and an AI coding methodology. The data were drawn from two remarkable patients with focal brain lesions, both with profound amnesia, in long-term psychotherapy. In an exploratory investigation, one session from each patient was coded independently by four clinically experienced psychotherapists, and separately by a single large language model operating under two different prompting conditions. Transcripts were coded for the presence of basic emotional systems. Results: The data suggest that overall inter-rater agreement about basic emotions was poor for both human and AI coders. Conclusions: The present study offers proof-of-concept that this approach is of scientific as well as clinical interest. The findings suggest that greater rigour needs to be applied to the way in which coders are prepared for, and implement, the classification of basic emotion systems.

**ИИ:** + · обе модели · кодирование сессий · An LLM and four psychotherapists coded the same psychotherapy session transcripts for basic emotional systems, and agreement between them was reported.

**Решение:** =

---

### 750 · R4656

**Validation of a Small Language Model for DSM-5 Substance Category Classification in Child Welfare Records.**

2026 · Journal of evidence-based social work (2019) · journal article, med, journalarticle · eng · https://doi.org/10.1080/26408066.2026.2673377

BACKGROUND: Recent studies have demonstrated that large language models (LLMs) can perform binary classification tasks on child welfare narratives, such as detecting the presence or absence of constructs such as substance-related problems, domestic violence, and firearms involvement. However, whether smaller locally deployable models can move beyond binary detection to classify specific substance types from these narratives remains untested. OBJECTIVE: Validate a locally hosted LLM classifier for identifying specific substance types aligned with DSM-5 categories in child welfare investigation narratives. METHODS: A locally hosted 20-billion-parameter LLM classified child maltreatment investigation narratives from a Midwestern U.S. state. Records previously identified as containing substace-related problems were passed to a second classification stage targeting seven DSM-5 substance categories. Expert human review of 900 stratified cases assessed classification precision, recall, and agreement with the criterion standard (Cohen's kappa). Model reproducibility was evaluated using approximately 15,000 independently classified records. RESULTS: Five substance categories achieved almost perfect criterion-standard agreement (κ = 0.94-1.00): alcohol, cannabis, opioid, stimulant, and sedative/hypnotic/anxiolytic. Classification precision ranged from 92% to 100% for these categories. Two low-prevalence categories (hallucinogen, inhalant) performed poorly. Run-to-run agreement ranged from 92.1% to 99.1% across the seven categories. CONCLUSIONS: A small, locally hosted LLM can reliably classify substance types from child welfare administrative text, extending prior work on binary classification to multi-label substance identification. Operating entirely on local hardware and requiring no changes to existing data collection, the pipeline supports substance-specific surveillance, retrospective trend analysis, and improved alignment of services with the substance profiles of investigated families.

**ИИ:** + · обе модели · кодирование по кодбуку · A 20B LLM sorted child welfare narratives into DSM-5 substance categories; experts reviewed 900 cases and agreement was reported as Cohen's kappa.

**Решение:** =
