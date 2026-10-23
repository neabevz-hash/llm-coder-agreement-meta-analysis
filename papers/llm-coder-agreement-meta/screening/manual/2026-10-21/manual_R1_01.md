# Ручной отбор, часть 1

Ручной отбор, часть 1: записи 1–150 из 1000. Эти записи вы размечаете сами, вместо проходов ИИ (deviations.md, D3); это случайные 1000 записей из тех, что ИИ ещё не разметил (зерно 20261024). **Меток ИИ здесь нет и не будет.** Ваше решение окончательное: «+» и «?» идут на полный текст. Размечайте в любом порядке и в несколько заходов.

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

### 1 · R6657

**A pleasant surprise: perplexity from large language models assesses divergent thinking**

2026 · JoCN Forum · journalarticle, article · en · https://doi.org/10.21428/8e6ba8ef.e8b0ea47

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T2 перплексия LLM для оценки дивергентного мышления; нет аннотации — проверить сопоставление с людьми в полном тексте

---

### 2 · R11560

**Evaluating Gender Bias in Large Language Models**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2411.09826

Gender bias in artificial intelligence has become an important issue, particularly in the context of language models used in communication-oriented applications. This study examines the extent to which Large Language Models (LLMs) exhibit gender bias in pronoun selection in occupational contexts. The analysis evaluates the models GPT-4, GPT-4o, PaLM 2 Text Bison and Gemini 1.0 Pro using a self-generated dataset. The jobs considered include a range of occupations, from those with a significant male presence to those with a notable female concentration, as well as jobs with a relatively equal gender distribution. Three different sentence processing methods were used to assess potential gender bias: masked tokens, unmasked sentences, and sentence completion. In addition, the LLMs suggested names of individuals in specific occupations, which were then examined for gender distribution. The results show a positive correlation between the models' pronoun choices and the gender distribution present in U.S. labor force data. Female pronouns were more often associated with female-dominated occupations, while male pronouns were more often associated with male-dominated occupations. Sentence completion showed the strongest correlation with actual gender distribution, while name generation resulted in a more balanced 'politically correct' gender distribution, albeit with notable variations in predominantly male or female occupations. Overall, the prompting method had a greater impact on gender distribution than the model selection itself, highlighting the complexity of addressing gender bias in LLMs. The findings highlight the importance of prompting in gender mapping. 13 pages, 12 figures, 1 table

**Решение:** -4 аудит гендерной предвзятости LLM в профессиях

---

### 3 · R8696

**Leveraging Text and Speech Processing for Suicide Risk Classification in Chinese Adolescents**

2025 · Interspeech · journalarticle · https://doi.org/10.21437/interspeech.2025-2755

The increasing prevalence of depression among young people is a growing global concern. Early detection and intervention are crucial, making the development of effective diagnostic tools essential. This work explores the use of advanced text and speech processing techniques to classify suicide risk within the context of the SpeechWellness Challenge (SW1) and verifies if speech can be used as a non-invasive and readily available mental health indicator. The analysis incorporated both linguistic features and audio-based methods for spontaneous speech and passage reading. For text classification, Large Language Models like Qwen2.5 and BERT were evaluated. For audio-based prediction, state-of-the-art speech processing models, including Whisper,Wav2Vec2 and HuBERT were employed. Furthermore, a multimodal approach combining both vocal and textual features was investigated. The results obtained in this research ranked among the highest in the challenge.

**Решение:** ? T3 классификация суицидального риска у подростков (Qwen2.5/BERT); проверить эталон разметки в полном тексте

---

### 4 · R10119

**A Multimodal Sleep Foundation Model Developed with 500K Hours of Sleep Recordings for Disease Predictions.**

2025 · medRxiv : the preprint server for health sciences · journal article, preprint, journalarticle · eng · https://doi.org/10.1101/2025.02.04.25321675

Sleep is a fundamental biological process with profound implications for physical and mental health, yet our understanding of its complex patterns and their relationships to a broad spectrum of diseases remains limited. While polysomnography (PSG), the gold standard for sleep analysis, captures rich multimodal physiological data, analyzing these measurements has been challenging due to limited flexibility across recording environments, poor generalizability across cohorts, and difficulty in leveraging information from multiple signals simultaneously. To address this gap, we curated over 585,000 hours of high-quality sleep recordings from approximately 65,000 participants across multiple cohorts and developed SleepFM, a multimodal sleep foundation model trained with a novel contrastive learning approach, designed to accommodate any PSG montage. SleepFM produces informative sleep embeddings that enable predictions of future diseases. We systematically demonstrate that SleepFM embeddings can predict 130 future diseases, as modeled by Phecodes, with C-Index and AUROC of at least 0.75 on held-out participants (Bonferroni-corrected p < 0.01). This includes accurate predictions for death (C-Index: 0.84 [95% CI: 0.81-0.87]), heart failure (C-Index: 0.80 [95% CI: 0.77-0.83]), chronic kidney disease (C-Index: 0.79 [95% CI: 0.77-0.81]), dementia (C-Index: 0.85 [95% CI: 0.82-0.87]), stroke (C-Index: 0.78 [95% CI: 0.76-0.81]), atrial fibrillation (C-Index: 0.78 [95% CI: 0.75-0.81]), and myocardial infarction (C-Index: 0.81 [95% CI: 0.78-0.84]). The model's generalizability was further validated through strong performance on the Sleep Heart Health Study (SHHS), a dataset unseen during pre-training. Additionally, SleepFM demonstrates strong performance on traditional sleep analysis tasks, achieving competitive results in both sleep staging (mean F1 scores: 0.70-0.78) and sleep apnea diagnosis (AUROC: 0.90-0.94). Beyond these standard applications, our analysis reveals that specific sleep stages and physiological signals carry distinct predictive power for different diseases. This work demonstrates how foundation models can leverage sleep polysomnography data to uncover the extensive relationship between sleep physiology and future disease risk.

**Решение:** -4 полисомнографическая модель SleepFM, соматическая медицина сна

---

### 5 · R2047

**PsychiatryBench: a multi-task benchmark for LLMs in psychiatry.**

2026 · NPJ digital medicine · journal article, journalarticle, preprint/article · eng · https://doi.org/10.1038/s41746-026-02582-w

Large language models (LLMs) offer significant potential in enhancing psychiatric practice, from improving diagnostic accuracy to streamlining clinical documentation and therapeutic support. However, existing evaluation resources heavily rely on small clinical interview corpora, social media posts, or synthetic dialogues, which limits their clinical validity and fails to capture the full complexity of diagnostic reasoning. In this work, we introduce PsychiatryBench, a rigorously curated benchmark grounded exclusively in authoritative, expert-validated psychiatric textbooks and casebooks. PsychiatryBench comprises eleven distinct question-answering tasks ranging from diagnostic reasoning and treatment planning to longitudinal follow-up, management planning, clinical approach, sequential case analysis, and multiple-choice/extended matching formats totaling 5,188 expert-annotated items. {\color{red}We evaluate a diverse set of frontier LLMs (including Google Gemini, DeepSeek, Sonnet 4.5, and GPT 5) alongside leading open-source medical models such as MedGemma using both conventional metrics and an "LLM-as-judge" similarity scoring framework. Our results reveal substantial gaps in clinical consistency and safety, particularly in multi-turn follow-up and management tasks, underscoring the need for specialized model tuning and more robust evaluation paradigms. PsychiatryBench offers a modular, extensible platform for benchmarking and improving LLM performance in mental health applications.

**Решение:** -4 PsychiatryBench: медицинские экзаменационные вопросы с множественным выбором

---

### 6 · R7588

**Evaluation of Advanced Artificial Intelligence in Minimally Invasive Surgery Training: A Preliminary Study of the Large Language Models DeepSeek-R1 and Claude 3.5 Sonnet**

2025 · Advances in Neurology and Neuroscience · journalarticle, article · https://doi.org/10.33140/an.08.02.05

Background/Objective: Minimally invasive surgery (MIS) reduces tissue trauma, pain, and recovery times but demands advanced technical skill acquisition. Current surgical training remains time-intensive and mentor-dependent. While robotics, simulation, and AI promise transformative improvements for surgical education, early large language models (LLMs) like ChatGPT raised concerns due to factual inaccuracies ("hallucinations") and limited explainability. It remains unclear whether modern LLMs—such as Claude 3.5 Sonnet and the reasoning-focused DeepSeek-R1— adequately overcome these limitations while ensuring the interpretability and reliability essential for medical applications. Moreover, their alignment with MIS-specific knowledge is understudied. This work preliminarily evaluates both models’ accuracy, reasoning capabilities, and error patterns in MIS knowledge assessment to determine their viability for enhancing surgical training. Methods: We performed a comparative analysis using 30 multiple-choice questions (MCQs) derived from the Atlas of Minimally Invasive Surgical Operations. Model performance was statistically compared using one-way ANOVA with Bonferroni correction. Inter-rater reliability was assessed with Cohen's Kappa, and effect size was measured using odds ratios. Qualitative analysis focused on reasoning patterns, error classification, and pedagogical applications specific to MIS education. Results: Claude 3.5 Sonnet achieved 97% accuracy (29/30 correct), while DeepSeek-R1 achieved 93.3% accuracy (28/30 correct). Statistical analysis (ANOVA, p = 0.742) revealed no significant difference in overall performance between models. Inter-rater reliability showed moderate agreement (κ = 0.52) with a strong effect size (OR = 23.0). Qualitative analysis identified distinct reasoning styles: DeepSeek-R1 demonstrated comprehensive, systematic (step-bystep) analysis, whereas Claude 3.5 Sonnet exhibited more focused, efficient reasoning. Error analysis revealed Formula Confusion Errors and Context Value Errors, with both models converging on clinically plausible but educationally incorrect answers in complex MIS scenarios. Conclusions: Both cutting-edge LLMs demonstrated exceptional accuracy in MIS knowledge assessment, surpassing older models, and possess unique reasoning approaches valuable for surgical education. Claude 3.5 Sonnet showed marginal superiority in accuracy with efficient reasoning, while DeepSeek-R1 offered advantages in reasoning transparency and open-source cost-effectiveness. The high accuracy rates, combined with detailed reasoning analysis, suggest meaningful potential for MIS-specific educational applications; however, careful implementation and human oversight remain essential.

**Решение:** -4 малоинвазивная хирургия, оценка знаний хирургов

---

### 7 · R0254

**ARTIFICIAL INTELLIGENCE IN PSYCHIATRIC DIAGNOSIS AND CLINICAL DECISION-MAKING: CURRENT EVIDENCE, CLINICAL APPLICATIONS, CHALLENGES AND FUTURE DIRECTIONS**

2026 · International Journal of Innovative Technologies in Social Science · journalarticle, review, article · en · https://doi.org/10.31435/ijitss.3(51).2026.6517

Artificial intelligence (AI) is increasingly investigated as a means of supporting psychiatric diagnosis and clinical decision-making. This narrative review critically evaluates its current clinical applications, limitations, ethical challenges, and readiness for implementation in psychiatric practice. A literature search of PubMed, Scopus, Web of Science, and Google Scholar was conducted for English-language publications issued between January 2020 and July 2026, supplemented by earlier landmark contributions. Following duplicate removal and eligibility screening, 111 publications were included in a clinically oriented narrative synthesis. Machine learning, deep learning, natural language processing, digital biomarkers, and large language models have demonstrated potential applications in diagnostic classification, symptom monitoring, treatment-response prediction, relapse and suicide-risk assessment, clinical documentation, and precision psychiatry. Promising performance in retrospective or internally validated datasets has not yet been matched by robust evidence of improved clinical decisions or patient outcomes. Major limitations include small and unrepresentative samples, methodological heterogeneity, insufficient external and prospective validation, inadequate calibration, limited interpretability, inconsistent safety assessment, and vulnerability to bias and automation-related errors. These concerns are particularly important in high-risk applications involving suicide prediction, treatment allocation, and direct patient interaction. AI should augment rather than replace comprehensive clinical assessment and professional judgment. Translation into routine practice will require prospective multicenter studies, representative longitudinal datasets, transparent reporting, subgroup-specific fairness evaluation, meaningful human oversight, stakeholder co-design, and continuous post-deployment monitoring. The value of psychiatric AI should ultimately be determined by whether it safely and equitably improves clinical decisions and patient-relevant outcomes.

**Решение:** -1 обзор применения искусственного интеллекта в психиатрии

---

### 8 · R1177

**Auditing LLM Portrayals of Neurodivergent People: Quantifying the Asymmetry Between Deficit Framing and Neurodiversity Affirmation**

2026 · Proceedings of the AAAI/ACM Conference on AI Ethics and Society · journalarticle, conference, conference-paper · en · https://doi.org/10.1609/aies.v9i4.43328

Open-weight large language models are increasingly used in education, hiring, and information-seeking contexts that touch neurodivergent people, yet we lack a clear empirical map of how their portrayals of neurodiversity shift under everyday prompt variation. We present a multi-condition, multi-model audit of LLM portrayals of eight neurodivergent identities (autism, ADHD, dyslexia, dyspraxia, dyscalculia, Tourette syndrome, OCD, and sensory-processing differences) plus a non-stigmatized medical control. Six open-weight models answer a pre-registered prompt bank that crosses seed items with seven perturbation families, including paraphrase, identity-first versus person-first language, system personas, plausible versus obviously fictional authority citations, multi-turn social pushback, leading questions, and two mitigation arms. Held-out LLM judges score each generation on three ordinal axes. Baseline portrayals are remarkably homogeneous across models, so the inconsistency observed under prompt variation is prompt-driven, not model-driven. Steering toward deficit framing is several times easier than steering toward neurodiversity affirmation. Emotional pushback shifts outputs more than evidence-laden pushback. Plausible-sounding fake citations slip past safety filters while obviously fictional ones do not. A single-line system-prompt mitigation recovers a meaningful share of the steering range at near-zero refusal cost on neutral prompts, though refusal rises sharply under adversarial pressure. The governance question for disability-relevant LLM deployment is therefore not whether the model is biased but who controls the steering, and with what accountability.

**Решение:** -4 аудит репрезентации нейродивергентности в LLM

---

### 9 · R5529

**DrukSerenity: A Culturally-Aware Multi-Agent Chatbot Framework for Mental Health Support in Bhutan**

2026 · Zorig Melong. · article · https://doi.org/10.17102/zmv9.i1.013

Globally, mental health challenges represent a significant public health issue, and Bhutan similarly faces barriers to accessing mental health support due to cultural stigma and limited resources. Currently, there are mental health chatbots, but they are primarily for Western, English-speaking users. There is a need for a system that safely and culturally adapts for Bhutanese people. Therefore, this paper introduces DrukSerenity, a multi-agent chatbot that addresses crisis, offers birdirection Dzongkha-English translation and provides appropriate cultural content using data consisting of 977 Dzongkha proverbs ,alongside 22 cultural, policy, and clinical documents from related institutional sources. The system was evaluated on a synthetic benchmark of 542 messages using rule-based checks and an LLM-judge protocol, showing strong safety performance (100% crisis precision, 92.2% crisis F1) and high cultural fidelity (0.94 RAG fidelity), with an overall functional accuracy of 83.8%, where Emotion classification accuracy and processing latency remains a limitation. Although formal clinical validation with licensed practitioners has not yet been conducted, an informal usability pilot with 20 Bhutanese users received good ratings (overall experience 3.80/5) alongside concerns about proverb overuse. DrukSerenity nonetheless offers a replicable template for building culturally-aware mental health AI in other lowresource, linguistically underserved settings.

**Решение:** -2 чат-бот DrukSerenity: пилотное юзабилити-тестирование с пользователями

---

### 10 · R9328

**A Synergistic Multi-Agent AI Framework for Cognitive Augmentation in Home Loan Credit Risk Assessment**

2025 · Zenodo (CERN European Organization for Nuclear Research) · text/, article · https://doi.org/10.5281/zenodo.18074689

The adjudication of credit risk in the mortgage industry is a knowledge-intensive process constrained by the dual imperatives of high efficiency and unwavering regulatory compliance. Existing AI solutions, often monolithic "black box" models, excel at prediction but fail to meet the critical demands for explainability, auditability, and human-in-the-loop collaboration. This paper introduces the LoanApprovalEngine, a comprehensive, Python-based Hybrid Intelligence framework that re-conceptualizes underwriting as a collaborative task between a human expert and a multi-agent AI system. Our architecture is composed of three specialized, communicating agents:(1) A Prognostic Agent (MLRiskScorer, InterestRateModel), built on an inherently transparent, rules-based model that generates risk scores along with a causal chain of explanatory factors.(2) A Narrative Agent (_generate_ai_credit_memo), a generative LLM that synthesizes the Prognostic Agent's structured output into formal credit appraisal memos.(3) An Interrogative Agent (voice-enabled chatbot), which facilitates a human-in-the-loop hermeneutic process, allowing underwriters to conduct dynamic, multilingual analysis on filtered applicant cohorts. We provide a detailed analysis of how the integration of AI tools—including sentence-transformers for data ingestion, pyttsx3 and langdetect for multilingual voice, and LLMs for reasoning and generation— transforms the underwriting workflow. We demonstrate that this framework drastically reduces processing time for bulk assessments and enables a depth of interactive analysis unattainable through traditional methods.

**Решение:** -4 скоринг кредитных и ипотечных рисков

---

### 11 · R0951

**AI Chatbot Suicide Risk Detection and Response: Human Validation Study of the Open-Source VERA-MH Safety Evaluation.**

2026 · JMIR AI · journal article, journalarticle, preprint/article · eng · https://doi.org/10.2196/92817

BACKGROUND: Millions of people now use leading generative artificial intelligence (AI) tools (chatbots) for psychological support. Despite the promise related to availability and scale, the single most pressing question in AI for mental health is whether these tools are safe. The field currently lacks a validated, automated benchmark for determining AI chatbot safety in mental health, including for users at risk of suicide. The Validation of Ethical and Responsible AI in Mental Health (VERA-MH) evaluation was recently proposed to meet this urgent need. OBJECTIVE: This human validation study examines the alignment of the VERA-MH safety evaluation for AI chatbot suicide risk detection and response with safety ratings by expert human clinicians. METHODS: We simulated a large set of conversations between large language model (LLM)-based users ("user-agents") spanning a wide range of suicide risk levels and disclosure styles and general-purpose AI chatbots. Licensed mental health clinicians from Spring Health used a scoring rubric developed for VERA-MH to independently rate the simulated conversations for safe and unsafe chatbot behaviors. An LLM-based evaluator (the "judge") used the same scoring rubric to evaluate the same set of conversations. We then examined rating alignment across (1) individual clinicians, (2) clinician consensus and the LLM judge, and (3) different judge LLMs. We also examined clinicians' ratings of user-agent realism, suicide risk, and disclosure. RESULTS: Clinicians were generally consistent with one another in their safety ratings (chance-corrected interrater reliability=0.77), thus establishing a reliable clinical consensus reference. The LLM judge was strongly aligned with this clinical consensus reference (interrater reliability=0.81) when using the same scoring rubric. Ratings were stable across judge LLMs and evaluations. Clinicians' ratings of user-agent realism and how well the intended user-agent suicide risk and disclosure styles were reflected in the simulated conversations were mixed. CONCLUSIONS: For the potential mental health benefits of AI chatbots to be realized, attention to safety is paramount. Findings support the reliability of VERA-MH, an open-source, fully automated AI safety evaluation for suicide risk detection and response. These results reflect an earlier version of the benchmark, and as VERA-MH continues to evolve, external validation of updated versions will be an important next step. Future research directions include VERA-MH generalizability and robustness, as well as expanding to target other key areas of AI safety for mental health.

**Решение:** + T4 VERA-MH: валидация LLM-судьи суицидального риска в чат-ботах против консенсуса клиницистов, каппа 0.81

---

### 12 · R8928

**GPT-LGBM: a ChatGPT-based integrated framework for credit scoring with textual and structured data**

2025 · Knowledge and Information Systems · journalarticle, article · en · https://doi.org/10.1007/s10115-025-02602-3

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 GPT-LGBM: кредитный скоринг, финансы

---

### 13 · R7647

**Exploring the Link Between the Emotional Recall Task and Mental Health in Humans and LLMs**

2025 · Preprints.org · preprint, ppr · https://doi.org/10.20944/preprints202510.1021.v1

The ability of Large Language Models to recall human emotions provides a novel opportunity to investigate links between memory, affect, and mental health. This study explores whether the Emotional Recall Task (ERT), a free word-association paradigm, can reveal cognitive markers of distress in both humans and Large Language Models (LLMs). Using spreading activation simulations grounded in cognitive network science, we examined how the recall of emotional concepts (e.g., stress, anxiety, depression) relates to psychometric measures of well-being and personality. In Study 1, correlations were tested between activation dynamics and clinical scales (DASS-21, PANAS, Life Satisfaction) in human participants (N=1200) and artificial participants generated by GPT-4, Claude Haiku, and Anthropic Opus. Humans with higher distress scores exhibited stronger, faster, and more persistent activation of negative concepts, supporting theories of rumination and memory bias. GPT-4 approximated human-like trajectories most closely, though with reduced variability. Study 2 linked recall dynamics to Big Five traits, confirming that neuroticism predicted greater activation of negative concepts, while extraversion acted as a protective factor. While LLMs lack autobiographical memory, their semantic activations partially mirrored human associations. These findings demonstrate that network-based spreading activation analysis can reveal cognitive signatures of distress, highlighting also the limits of LLMs in modeling human affect.

**Решение:** -2 LLM как искусственный испытуемый в тесте эмоционального припоминания (ERT)

---

### 14 · R6162

**ISDP: A Decoupled Iterative Pipeline for Balancing Defensive Robustness and User Usability in LLMs**

2026 · 2026 ICEENG International Conference for Innovations in Intelligent Computing and Cybersecurity (IICC) · conference · https://doi.org/10.1109/iicc69623.2026.11582295

Large Language Models (LLMs) are increasingly vulnerable to sophisticated jailbreaking attacks. Conventional defense mechanisms, such as single-pass filtering and preset refusal, often fail to provide robust protection against nuanced adversarial prompts while also degrading user experience. Motivated by the concept of LLM self-defense and representation-level analysis, we propose the Iterative Safety Defense Pipeline (ISDP) to enhance both the robustness and usability of LLMs. ISDP employs a dual-model architecture decoupling content generation from security analysis. Unlike conventional single-pass filtering, ISDP introduces a conditional iterative refinement mechanism driven by intent recognition to effectively enhance detection accuracy. The guard model first distinguishes underlying malice from superficial adversarial noise; subsequently, a purification cycle is triggered only upon detecting harm or contamination to neutralize threats and strip noise for restored usability, while safe responses are passed directly to minimize latency. Experimental evaluation across three open-source LLMs (Llama2, Mistral, Qwen2.5) demonstrates that ISDP achieves an average true positive rate (TPR) of 95.5% for harmful prompts and reduces the false positive rate (FPR) to 5.5% for benign prompts. With an additional average latency of only 2.95s, ISDP offers an efficient, reliable, and user-friendly framework for secure LLM deployment.

**Решение:** -4 защита от джейлбрейков (ISDP), кибербезопасность

---

### 15 · R10318

**Human-AI Alignment of Multimodal Large Language Models with Speech-Language Pathologists in Parent-Child Interactions**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2506.05879

Joint attention is a critical marker of early social-communicative development, yet remains difficult for caregivers to assess without expert guidance. In this work, we explore how multimodal large language models (MLLMs) can be aligned with the reasoning processes of speech-language pathologists (SLPs) to support the interpretation of everyday parent-child interactions. We conducted in-depth interviews and video annotation studies with three experienced SLPs to uncover how they evaluate joint attention based on three core behavioural cues: gaze, action, and vocalisation. Using these insights, we developed a two-stage MLLM-based system that first extracts fine-grained behavioural descriptions from video segments and then judge joint attention quality using expert-aligned prompts. Our evaluation across 26 parent-child interaction videos shows that MLLMs can achieve up to 85% accuracy in perceptual cue extraction and over 75% average precision in simulating expert judgement. We further propose design guidelines for building MLLM-based behaviour observation-judgement systems that align with SLPs, emphasising the structuring of behavioural cues, the construction of exemplar libraries grounded in expert annotations, and the need to personalise system responses based on developmental stage and neurotypical or atypical presentation. This work provides structured behavioural cues derived from SLP expertise, demonstrates the feasibility of aligning SLPs observation and judgement using MLLMs, and offers practical design guidelines for building aligned systems to support parent-child interaction analysis. This is an earlier version of the work released in May 2025. The version accepted at CHI 2026 is available as a separate preprint at arXiv:2511.04366

**Решение:** ? T1/T2 оценка совместного внимания у детей MLLM против логопедов; проверить модальность и схему в полном тексте

---

### 16 · R2431

**Patient Information Needs Before Anesthesia and Surgery: Protocol for a Qualitative Content Analysis of Patient-Generated Perioperative Questions**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/6naw2

This study is a secondary qualitative analysis of 200 patient-generated perioperative questions collected during the parent study, "ChatGPT Compared with Anesthesiologists for Addressing Patient Preoperative Anesthesia Questions: a Prospective Paired Evaluator-Blinded Cross-Sectional Noninferiority Study." The parent study was prospectively registered at ClinicalTrials.gov (NCT06652854). In the parent study, adults scheduled for elective noncardiac surgery and a preoperative anesthesiologist consultation were asked, before their consultation, to identify the most important question they hoped to ask their anesthesiologist about anesthesia care, pain management, or the perioperative period. The purpose of the present study is to characterize the content and information needs represented in these questions. We will use qualitative content analysis to identify the topics patients ask about and the broader underlying information needs reflected in their questions. This inductive analysis will be complemented by prespecified structured secondary coding of the degree of personalization required to provide a clinically useful initial response, the primary clinical information domain relevant to answering the question, and the factors that make a fully generic response insufficient when contextualization or individualized assessment is required. The study will use an iterative, codebook-based analytic process incorporating independent coding, assessment of intercoder agreement for prespecified structured dimensions, consensus discussion, and refinement of coding definitions as required. Expected outputs include a descriptive taxonomy of perioperative topics and underlying information needs, characterization of response personalization requirements and their sources, and identification of the clinical information domains represented in patients’ questions.

**Решение:** -1 протокол качественного анализа предоперационных вопросов пациентов

---

### 17 · R5266

**Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.02578

Recent multimodal large language models have demonstrated strong reasoning ability, yet their reliability as automated evaluators remains limited by a critical weakness: when visual evidence conflicts with textual cues, MLLM judges tend to reward plausible narratives over perceptually correct answers. We identify and systematically analyze this phenomenon, which we term Perceptual Judgment Bias. Through controlled visual perturbations, existing multimodal judges frequently anchor on the response text instead of their own visual perception, leading to inconsistent and non-verifiable evaluations. To address this issue, we introduce the Perceptually Perturbed Judgment Dataset, which constructs minimally edited counterfactual responses that isolate perceptual errors and enable verifiable supervision. Building on this dataset, we develop a unified training framework that combines a structured GRPO-based reward with a batch-ranking objective, achieving coherent global ordering without explicit pairwise labels. Experiments across diverse MLLM-as-a-Judge benchmarks show that our approach substantially improves perceptual fidelity, ranking coherence, and alignment with human evaluation. Our results establish a scalable and generalizable pathway for training multimodal judges that are perceptually grounded, interpretable, and robust to visual-reasoning conflicts. ICML 2026

**Решение:** -4 перцептивный LLM-as-a-judge в задачах визуального рассуждения (VQA)

---

### 18 · R7625

**Can large audio language models understand child stuttering speech? speech summarization, and source separation**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2510.20850

Child speech differs from adult speech in acoustics, prosody, and language development, and disfluencies (repetitions, prolongations, blocks) further challenge Automatic Speech Recognition (ASR) and downstream Natural Language Processing (NLP). Recent large audio-language models (LALMs) demonstrate strong cross-modal audio understanding; however, their behavior in disfluent child speech remains underexplored. We evaluate several state-of-the-art LALMs in two settings: an interview (mixed speakers) and a reading task (single child). The tasks are (i) single-channel source separation to isolate the child and (ii) child-only summarization that preserves clinically relevant disfluencies and avoids adult-speech leakage. Evaluation combines Large Language Model (LLM) as a judge, human expert ratings, and BERTScore (F1), and we report agreement between models and between models and humans to assess reliability. Our findings delineate the conditions under which LALMs produce faithful child-only summaries from mixed audio and where they fail, offering practical guidance for clinical and educational deployments. We provide prompts and evaluation scripts to support replication. 7 pages, 1 Figure, 8 tables, Under review ICASSP 2026

**Решение:** ? T1/T4 суммаризация заикания у детей, LLM против экспертов; проверить клиническую схему в полном тексте

---

### 19 · R5101

**Learner Emotions and AI Scoring: Integrating Affective Signals in Language Evaluation**

2026 · SAGE Open · journalarticle, article · en · https://doi.org/10.1177/21582440261447928

The rapid evolution of artificial intelligence (AI) and the Internet of Things (IoT) is reshaping language assessment practices, yet most AI-driven approaches remain limited in their ability to recognize the affective dimensions that shape learner performance. This study explores how real-time emotional and physiological signals—such as heart rate variability and facial expressions—can be integrated into AI-mediated oral assessment to enhance fairness, validity, and learner support. Using a combination of generative AI (GPT-4), OpenAI Whisper, affective computing, and IoT-enabled biofeedback, an experimental platform was developed to capture and respond to learners’ emotional states during speaking tasks. Grounded in Weir’s sociocognitive validity framework and Shneiderman’s human-centered AI principles, the study involved 24 intermediate English learners and examined the correlation between affective data and oral performance, the alignment between AI and human scoring, and learner perceptions of fairness and emotional support. Results showed that emotional states significantly impacted language output and that integrating affective input improved the alignment between AI and human ratings, particularly in fluency and coherence. Participants generally perceived the system as transparent and empathetic but raised concerns about emotional surveillance and data privacy. The findings contribute to emerging discussions on human-centered assessment design by highlighting how affective responsiveness in AI-supported assessment can foster interpretive fairness, reduce performance anxiety, and support learner agency. Plain Language Summary How AI Can Understand Learners’ Emotions to Make Language Tests Fairer This study looks at how learners’ emotions, such as stress or calmness, can affect how well they perform during speaking exams in English. Traditional language tests and even new AI-based tests often ignore how nervous or anxious a learner feels, even though these emotions can impact their ability to speak clearly or fluently. To explore this, the researcher created a speaking test system using artificial intelligence (AI), speech recognition, and wearable devices that track things like heart rate and facial expressions. These tools helped the system notice how learners were feeling while they spoke. The study involved 24 university students and compared scores from the AI with scores from human teachers. The results showed that when the AI took emotions into account, it gave scores that were closer to what human teachers would give. Learners also said the system felt more supportive and fair, although some were worried about privacy and how their emotional data was used. This research helps us think about how future language tests could be more human-centered, taking into account not just what learners say, but how they feel while saying it.

**Решение:** -4 автоматическая оценка устной речи на английском языке, педагогика

---

### 20 · R7010

**AIによる認知スキャフォールディングとアイデア発散傾向の構造化:IT実務家における論文執筆の民主化と認知拡張メカニズム**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · ja · https://doi.org/10.5281/zenodo.21981930

English title: Cognitive Scaffolding for Idea-Explosive Minds: How AI Augments Executive Function and Democratizes Scholarly Writing for IT Practitioners 【アブストラクト】現代のナレッジワーカーやITエンジニアの中には、次々とアイデアが湧き出て発散する拡散的思考(Divergent Thinking)を持ちながらも、タスクの始動障壁(Task Initiation Deficit)、ワーキングメモリの制約、ならびに構造化の難しさに直面する者が存在する。本研究はこの認知傾向を、特定疾患の医学的病理としてではなく、診断の有無を問わない認知スタイルの連続的な個人差として記述的に扱う。特に、学術的なトレーニングから離れた実務家にとって、膨大な思考の散乱を一本の体系的な論文として統合・執筆するプロセスは、高い実行機能(Executive Function)のハードルとなりうる。 本論文では、生成AIおよび自律型AIエージェントが提供する動的かつパーソナライズされた認知スキャフォールディング(Cognitive Scaffolding)が、IT実務家の思考発散をどのように「障壁」から「創造的強み」へと転換させるかの相互作用メカニズムを探究する。具体的には、4つの介入メカニズム——(1) 外在化ワーキングメモリによる思考爆発の即時構造化(メタ認知ミラーリング)、(2) タスクのマイクロ分解と着手コストの最小化、(3) 過集中と中断後の復帰を助けるコンテキストセービング、(4) 心理的安全性の高い段階的対話(ZPDプロンプティング)——をデザインサイエンス研究の設計命題として操作化し、著者自身による10年ぶりの論文執筆という探索的単一ケースにおいて、負例の記録とともにその発現を観察した。その結果、4メカニズムの連鎖と、品質ゲートと著者判断による主張の強度の較正を含む修正過程が、設計命題の存在例として示された。知見はオープンソーススキル集(scholarly-agent-skills)として実装・公開されている。 【Abstract】Among today's knowledge workers and IT engineers, there exist individuals who exhibit divergent thinking—a prolific, explosive flow of ideas—while simultaneously facing task initiation deficits, working memory constraints, and difficulties in structuring. This study treats such cognitive tendencies not as the medical pathology of a specific disorder, but descriptively, as continuously distributed individual differences in cognitive style, regardless of diagnostic status. For practitioners removed from academic training in particular, the process of integrating a vast scatter of thoughts into a single, systematic paper can pose a high executive-function hurdle. This paper explores the interaction mechanisms through which dynamic, personalized cognitive scaffolding—provided by generative AI and autonomous AI agents—transforms the idea explosion of IT practitioners from a "barrier" into a "creative strength." Specifically, four intervention mechanisms—(1) immediate structuring of idea explosions through externalized working memory (metacognitive mirroring), (2) micro-decomposition of tasks and minimization of initiation costs, (3) context saving that supports recovery from hyperfocus and post-interruption resumption, and (4) psychologically safe, staged dialogue (ZPD prompting)—are operationalized as design propositions in design science research, and their emergence is observed, together with a record of negative cases, in an exploratory single case study: the author's first scholarly writing in ten years. The results demonstrate, as an existence proof of the design propositions, the chaining of the four mechanisms and a calibration process in which quality gates and authorial judgment constrained the strength of claims. The findings are implemented and published as an open-source skill collection (scholarly-agent-skills). Methodological note: This paper presents a design-science existence proof and an exploratory single case study (self-referential action research). It does not claim statistical generalization or causal efficacy, and does not estimate or classify the medical status of any individual. Reference implementation (open source): https://github.com/hideshi/scholarly-agent-skills

**Решение:** -1 автоэтнографический отчет / эссе об академическом письме с помощью ИИ

---

### 21 · R2556

**A Study on the Utility of Artificial Intelligence in the Draw-A-Story Assessment**

2026 · Art Therapy · journalarticle, article · en · https://doi.org/10.1080/07421656.2026.2676429

Abstract This study examined the applicability of AI-assisted scoring in the Draw-A-Story (DAS) assessment. Ninety-nine adults completed the DAS and the Beck Depression Inventory. Two certified art therapists independently scored drawings across four domains—emotional content, self-image, color usage, and compositional transformation—and ratings were compared with GPT-4–generated scores. Significant group differences emerged in emotional content and self-image by depression level. Quadratic weighted kappa indicated substantial agreement between AI and experts (κ = .67, p < .001), with higher concordance in color usage than in symbolically interpreted domains. Art therapists considered AI-generated descriptions clinically appropriate and useful supplementary information. Findings suggest AI may enhance scoring consistency while supporting, not replacing, clinical judgment.

**Решение:** + T2 проективная методика «Нарисуй историю» (DAS): GPT-4 против двух арт-терапевтов, каппа 0.67

---

### 22 · R3403

**The readability and quality paradox: Comparing ChatGPT, Gemini, and Perplexity outputs on pediatric chest pain queries.**

2026 · PloS one · comparative study, research-article, journal article · eng · https://doi.org/10.1371/journal.pone.0359170

Pediatric chest pain represents a frequently encountered symptom in emergency departments and outpatient clinics throughout childhood, often generating substantial parental anxiety. This study aims to comparatively analyze the readability, information quality, and scientific reliability of textual contents generated by the artificial intelligence (AI) chatbots ChatGPT, Gemini, and Perplexity regarding pediatric chest pain, utilizing multidimensional analytical indices. Out of the top 25 queries with the highest global search volume on Google Trends, 17 unique keywords meeting the predefined inclusion criteria were filtered on June 1, 2026. These inquiries were directed to all three AI platforms in distinct, independent user sessions, yielding a total of 51 textual responses. Linguistic readability levels were calculated across six separate digital interfaces using the FKGL, FRES and other formulas, and the results were benchmarked against the sixth-grade reading level" threshold. Scientific reliability was audited via the Modified DISCERN and JAMA benchmarks, while content quality was examined using the GQS and EQIP instruments. The median readability scores computed across all three AI models were found to be statistically and significantly above the targeted sixth-grade comprehension threshold, indicating a high level of difficulty (p < 0.001). Post-hoc pairwise evaluations revealed that ChatGPT and Gemini offered linguistically more accessible and structurally less complex textual architectures; conversely, Perplexity exhibited a significantly more difficult and academic linguistic framework (p < 0.0167). On the other hand, regarding content quality and source credibility, Perplexity demonstrated remarkably superior and more optimized scores across all evaluated instruments, namely GQS (p = 0.002, p = 0.001), JAMA (p < 0.001, p < 0.001), mDISCERN (p = 0.005, p = 0.001), and EQIP (p = 0.003, p < 0.001), compared directly to both ChatGPT and Gemini, respectively. Although generative AI formulations harbor considerable potential to provide extensive data on pediatric chest pain, the sophisticated, university-level linguistic architecture of these texts poses a substantial access barrier for individuals who lack proficient digital health literacy skills. While Perplexity achieved the performance closest to the "gold standard" in terms of informational accuracy, no model is currently mature enough to substitute for a professional medical consultation due to observed citation biases and omissions. It is of paramount importance that clinicians actively guide families to scrutinize online health data through a critical lens.

**Решение:** -4 педиатрические боли в груди: оценка качества ответов чат-ботов врачами

---

### 23 · R5092

**Large Language Model in Automatic Depression Detection**

2026 · European Psychiatry · journalarticle, article, journal-article · en · https://doi.org/10.1192/j.eurpsy.2026.11414

Introduction Depression affects over 280 million people globally and is linked to substantial morbidity, mortality, and poor outcomes in comorbid conditions. Despite the availability of validated screening tools, up to 63.6% of cases remain undiagnosed, delaying timely treatment. Automated depression screening using text or voice data has emerged to improve accessibility and detection. Large language models (LLMs) have shown promise in identifying depression from social media, clinical notes, and structured interviews. However, current performance estimates are most likely optimistic due to relying on commercial models. Objectives This study evaluates the feasibility and accuracy of using privacy-preserving locally deployed LLMs with realistic size constraints for automated depression detection using clinical dialogue transcripts. Methods We employed the Distress Analysis Interview Corpus–Wizard-of-Oz (DAIC-WOZ) dataset containing therapist–patient transcripts labelled for depression. Several open-source LLMs under 15 billion parameters (Gemma3, Qwen3, DeepSeek-R1, Phi3, and LLaMA3.2) were deployed locally via Ollama. Each model received a standardized system prompt to classify each transcript as “depressed” (1) or “not depressed” (0). Predictions were repeated ten times per model. Accuracy, sensitivity, specificity, precision, F1 score, and Cohen’s kappa were calculated with 95% confidence intervals using Scikit-learn and Scipy (α = 0.05). Results Each model is trained and validated on the Distress Analysis Interview Corpus/Wizard of Oz dataset using locally deployed LLMs to preserve privacy. Best performing models achieved 67.7% accuracy, 46.2% precision, 72.9% specificity (deepseek-r1:14b), 92.9% sensitivity (gemma3:1b), and 56.4% F1 (gemma3:12b). Image 1: Image 1: Long description.A performance metric table comparing eleven machine learning models across five categories including Accuracy and F 1 score. See long description. Image 2: Image 2: Long description.A four-panel dot plot showing 95 percent confidence intervals for Accuracy, Sensitivity, Specificity, and F 1 score across twelve different large language models. See long description. Image 3: Image 3: Long description.A heatmap showing Cohen's Kappa inter-rater reliability between twelve different large language models. See long description. Conclusions The results demonstrated that current local LLMs are not adequate for clinical utility in automatic depression screening. Future studies are required to fine tune locally operated LLMs for depression screening. Disclosure of Interest None Declared

**Решение:** -3 детекция депрессии по DAIC-WOZ: эталон — самоотчет по PHQ-8 (критериальная валидность)

---

### 24 · R11352

**Exploring the Potential of ChatGPT-4o in Translation Quality Assessment**

2024 · Journal of Theory and Practice in Humanities and Social Sciences · article · en · https://woodyinternational.com/index.php/jtphss/article/download/27/21

The advancement of large language models (LLMs) has demonstrated significant potential in the domains of foreign language teaching and research. By evaluating two translated works of MTI students, this study discusses the application effect of ChatGPT-4o in the evaluation of human translation based on Multidimensional Quality Metrics (MQM). The research involves literary texts and non-literary texts and conducts human translations before human and ChatGPT-4o modifications. Subsequently, the versions will be evaluated and compared in accordance with MQM standards. Through the score comparison and the qualitative analysis, the results show that ChatGPT-4o demonstrates high consistency with human evaluators in evaluating translations based on the MQM method. The scores and suggested modifications significantly enhance the translation quality, particularly in terms of maintaining terminology consistency and ensuring grammatical accuracy.

**Решение:** -4 оценка качества машинного перевода по метрике MQM

---

### 25 · R9170

**Storytelling**

2025 · OSF Preprints (OSF Preprints) · text/project, preprint · https://doi.org/10.17605/osf.io/bzgan

The goal of this research was to create and assess a novel method for identifying narratives produced in conversations between children and adults. To do so, we crafted a coding manual with a set of concrete rules and examples for identifying utterances containing narrative behavior. Then we asked trained coders to apply these rules to a set of transcribed conversations between adults and children, drawn from CHILDES. Further, we trained a version of a large language model (LLM) (GPT-4o-mini) to apply these rules.

**Решение:** + T1 кодирование нарративного поведения детей (CHILDES) по кодбуку: GPT-4o-mini против кодировщиков-людей

---

### 26 · R11518

**Leveraging LLMs like ChatGPT for robust quality checks and medical text agreement rationale, enhancing adjudication quality and alignment in BICR for oncology clinical trials**

2024 · SPIE Medical Imaging: Imaging Informatics for Healthcare, Research, and Applications · review, conference-paper · en · https://doi.org/10.1117/12.3009153

Blinded Independent Central Review (BICR) is recommended by the US FDA for registration of oncology trials as image assessment bias is avoided and no chance of unblinding of patient data. Double read with adjudication is the method used to reduce endpoint assessment variability. In cases of disagreement between the readers, a third reader called an adjudicator, reviews the assessment by the two radiologists and decides which assessment is most accurate. Adjudication Rate (AR) and Adjudicator Agreement Rate (AAR) are the two indicators used to evaluate reviewer performance and overall trial variability and quality. Sentiment Analysis (SA) is based on natural language processing and can tag the data as ‘positive’, ‘negative’ or ‘neutral’ although current technologies can provide a more complex analysis of emotions in the written text. Medical SA can analyze patients’ and doctors’ opinions, sentiments, attitudes, and emotions in the clinical background. Python, the most frequently used programming language for deep learning worldwide and ChatGPT, an AI-based chatbot can be used for assessing adjudicator comment quality based on sentiment analysis. If successful, this analysis can open another novel implementation for Large Language Models (LLMs) or ChatGPT in clinical research and medical imaging. This prospective study involved the review of cases for 100 subjects by board-certified radiologists using the Response Evaluation Criteria in Solid Tumors (RECIST) 1.1 criteria. The study employed a double read with adjudication paradigm in a central imaging review setup. The agreement of adjudication was assessed and compared with the overall response, agreed reader, and medical text. The medical text entered by the adjudicator is usually a free text field that typically lacks standardization and control over its content, which may affect its correlation with reviewer selection for agreement. Although uncommon, errors by the adjudicator can occur due to ambiguous text, mis-clicks, or application delay errors. To analyze the adjudicator’s comments, sentiment analysis was conducted using a Python plug-in with ChatGPT as a large language model. Based on this analysis, the subjects were categorized as either having “Potential Error” or “No Error”. The algorithm supported by ChatGPT was evaluated against a Gold Standard, determined by a board-certified radiologist with over 20 years of experience in the BICR process. A comparison was made to assess accuracy and reproducibility, revealing that only four out of 100 subjects had different outcomes. The sensitivity was calculated as 0.857, specificity as 1.0, and accuracy as 0.96. The remarkable Natural Language Processing (NLP) capabilities of ChatGPT are evident in its ability to classify the sentiment as positive, negative, or neutral based on the free-text adjudicator comments provided during the review process. This classification enables a comparison with the actual assessment, adjudicator agreement, and overall patient outcome, highlighting the impressive performance of ChatGPT in this regard.

**Решение:** -4 соматическая онкология, независимый аудит клинических испытаний BICR

---

### 27 · R4620

**Show Your Work: Verbatim Evidence Requirements and Automated Assessment for Large Language Models in Biomedical Text Processing**

2026 · International Journal of Radiation Oncology*Biology*Physics · article · en · https://doi.org/10.1016/j.ijrobp.2026.06.1305

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 биомедицинская обработка текста, нет психолого-клинического конструкта

---

### 28 · R3961

**Reasoning Over Recall: Evaluating the Efficacy of Generalist Architectures vs. Specialized Fine-Tunes in RAG-Based Mental Health Dialogue Systems**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.01341

The deployment of Large Language Models (LLMs) in mental health counseling faces the dual challenges of hallucinations and lack of empathy. While the former may be mitigated by RAG (retrieval-augmented generation) by anchoring answers in trusted clinical sources, there remains an open question as to whether the most effective model under this paradigm would be one that is fine-tuned on mental health data, or a more general and powerful model that succeeds purely on the basis of reasoning. In this paper, we perform a direct comparison by running four open-source models through the same RAG pipeline using ChromaDB: two generalist reasoners (Qwen2.5-3B and Phi-3-Mini) and two domain-specific fine-tunes (MentalHealthBot-7B and TherapyBot-7B). We use an LLM-as-a-Judge framework to automate evaluation over 50 turns. We find a clear trend: the generalist models outperform the domain-specific ones in empathy (3.72 vs. 3.26, $p &lt; 0.001$) in spite of being much smaller (3B vs. 7B), and all models perform well in terms of safety, but the generalist models show better contextual understanding and are less prone to overfitting as we observe in the domain-specific models. Overall, our results indicate that for RAG-based therapy systems, strong reasoning is more important than training on mental health-specific vocabulary; i.e. a well-reasoned general model would provide more empathetic and balanced support than a larger narrowly fine-tuned model, so long as the answer is already grounded in clinical evidence.

**Решение:** -5 оценка агентов психологической помощи через LLM-as-a-judge без людей

---

### 29 · R4849

**Using machine learning to build public policy agenda from social media conversations**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.20604

Issue identification and agenda setting represents an important stage in the public policy making process. Traditional approaches for carrying out activities under this stage are time- and labor-intensive on data collection and analysis, in addition to being costly to scale over large geographic areas. In this work we propose a human-augmented machine learning (ML) approach for identifying matters of public interest from social media conversations. The approach consists of five stages namely, input data cleaning and preprocessing, keywords extraction and issue identification, narrative creation, narrative validation, and agenda validation. We implemented experiments to validate the output of our method based on a Twitter dataset and using Latent Dirichlet Allocation (LDA) and Top2Vec for topic modeling. Natural Language Generation (NLG) was achieved using GPT-2 while narrative and agenda validation were based on similarity analysis and human evaluation. We achieved "very good" and "good" inter-rater agreement (IRA) on readability and coherence of agenda narrative generation by our GPT-2 model. On the other hand, IRA was "good" for generated agenda items. We also achieved above average cosine similarity score on at least three out of five reference text (narrative) themes. These results demonstrate that the ML approach represents a promising methodology for identifying issues of public interest from social media conversations. 14 pages, 14 figures

**Решение:** -4 анализ политической повестки в Twitter методом тематического моделирования

---

### 30 · R6577

**Text Recovery Attacks and Defenses on Physical Envelopes**

2026 · International Conference on Multimedia Retrieval · journalarticle, book, conference-paper · https://doi.org/10.1145/3805622.3810850

Recovering text from sealed envelopes poses a severe security threat to physical privacy. While recent imaging advances can see through paper layers to recover general textures, they fail to reconstruct legible text due to the high-frequency detail and semantic structure required for OCR. To address this, we present the first unified pipeline for Physical Envelope Text Recovery (PETR), covering both attack and defense mechanisms. On the attack side, we design two entirely different recovery architectures: ETNN and ETFormer. In particular, we propose a Text-Aware Loss that injects text-specific guidance into the restoration process, where constraints on both text content and text structure jointly drive gradient back-propagation to enhance structural clarity. We also introduce an LLM-based evaluation protocol to measure the semantic readability of recovered content. On the defense side, we analyze these attack vectors to design secure envelopes using localized disruption patterns that impede recovery without affecting human readability after opening. Extensive experiments show our models outperform state-of-the-art baselines in both fidelity (PSNR/SSIM) and OCR accuracy. The source code and dataset are available on the project page https://github.com/YongfTao/PETR.

**Решение:** -4 восстановление текста с запечатанных конвертов, компьютерное зрение

---

### 31 · R1418

**GENERATIVE AI-POWERED AUTONOMOUS CYBERSECURITY FRAMEWORKS FOR INDUSTRIAL IOT ENVIRONMENTS: ENHANCING THREAT INTELLIGENCE, SECURE COMMUNICATION, AND ADAPTIVE DEFENSE MECHANISMS**

2026 · Zenodo (CERN European Organization for Nuclear Research) · journal/, other · https://doi.org/10.5281/zenodo.22797702

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 кибербезопасность промышленного интернета вещей

---

### 32 · R1266

**EEG-UDAF: A Novel Unsupervised Domain Adaptation Framework Leveraging Dual-view Frequency and Spatio-temporal Features for EEG-based Emotion Recognition**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-9823696/v1

Abstract Currently, machine learning technology has been widely used in electroencephalogram (EEG) automatic emotion recognition tasks. However, the non-stationarity, individual differences, and high annotation costs in EEG signals seriously affect the generalization ability of the model. To solve these problems, we propose a new unsupervised domain adaptation framework named EEG-UDAF for EEG emotion recognition. First, we design a dual-view frequency domain feature fusion module that can extract rich EEG signals frequency domain features from two perspectives, differential entropy and power spectral density, and fuse them based on the self-attention mechanism. Second, we propose a spatio-temporal feature extraction module based on graph convolutional network and bidirectional long short-term memory. It can comprehensively consider the spatial topological structure of the brain and the dynamic characteristics of temporal changes between EEG channels to extract complex spatio-temporal features. Third, we use the unsupervised domain adaptation strategy to solve the non-stationarity and individual differences in EEG signals without manual annotation, and introduce a semantic correction mechanism to prevent incorrect class alignment. Experiments based on intra-subject and inter-subject paradigms show that EEG-UDAF can effectively alleviate non-stationarity and individual differences. Moreover, these transferable EEG representations also provide a potential foundation for LLM-augmented multimodal data fusion in large-scale affective computing.

**Решение:** -4 распознавание эмоций по физиологическим сигналам ЭЭГ

---

### 33 · R2997

**RagForge: Evaluating Retrieval-Augmented Generation for Long-Document Literary Question Answering**

2026 · Zenodo (CERN European Organization for Nuclear Research) · report/, report · en · https://doi.org/10.5281/zenodo.22149827

RagForge is a retrieval-augmented generation (RAG) system built over the complete text of J.R.R. Tolkien's The Lord of the Rings trilogy to evaluate how RAG design choices affect grounded question answering on long narrative text. The system evaluates chunk size, retrieval depth, hybrid dense-BM25 weighting, generation parameters, query expansion, calibrated abstention, and generator model choice using a curated dataset of 1,000 factoid and multi-hop questions. Retrieval performance is evaluated using Hit@K, MRR, and nDCG, while generation quality is assessed using both keyword accuracy and LLM-as-a-judge scoring. The principal finding is that, once a strong retrieval baseline was established, generator capability represented a larger performance bottleneck than additional retrieval tuning. On identical retrieval with an 89.6% hit rate, Claude Opus 4.6 achieved 87.6% judge accuracy compared with 74.5% for Amazon Nova Pro, a 13.1 percentage-point difference. The study also finds that keyword-based evaluation can overstate RAG answer quality and that query expansion and score-based abstention did not improve performance on this domain-specific corpus.

**Решение:** -4 RagForge: литературные ответы на вопросы по «Властелину колец»

---

### 34 · R2383

**Social media polarization during conflict: insights from an ideological stance dataset on Reddit comments**

2026 · Social Network Analysis and Mining · journalarticle, article · en · https://doi.org/10.1007/s13278-026-01604-5

In politically sensitive scenarios such as wars, social media often becomes a platform for polarized discourse and expressions of strong ideological stances. While prior studies have explored ideological stance detection in general contexts, limited attention has been given to conflict-specific settings. This study addresses this gap by analyzing 9969 Reddit comments related to the Israel–Palestine conflict collected between October 2023 and August 2024. The comments were manually annotated into three stance classes—Pro-Israel, Pro-Palestine, and Neutral—with high inter-annotator agreement (Fleiss’ κ = 0.93). We conduct a comprehensive comparative evaluation of neural networks, pre-trained language models, and large language models (LLMs), along with multiple prompt engineering strategies and an LLM majority voting ensemble. Model performance is assessed using accuracy, precision, recall, and F1-score. Among the tested approaches, the Scoring and Reflective Re-read prompting strategy applied to Mixtral 8x7B achieves the best overall performance across evaluation metrics. Beyond model performance, the findings provide empirical insights into how ideological polarization manifests in online discourse surrounding the Israel–Palestine conflict, offering a computational perspective on the distribution of Pro-Israel, Pro-Palestine, and Neutral narratives. The dataset used in this study is publicly available to support further research on ideological stance detection in politically sensitive contexts.

**Решение:** -4 идеологическая поляризация в Reddit о конфликте

---

### 35 · R1684

**Chiaroscuro for Emotions: A Contrastive Emotion Benchmark Grounded in Appraisal Theory**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.03394

Emotion recognition benchmarks often predict one emotion per text, missing many real-world scenarios where two people arrive at opposing emotions from a single shared event. For example, a child kicks the seat in front of her in excitement while the passenger ahead grows angry. We introduce CHIARO, a 1,000 human-annotated sentence benchmark for contrastive emotion inference grounded in appraisal theory. Each scene describes one causal trigger eliciting a positive emotion in one person and a negative emotion in the other, drawn from a ten-class taxonomy. We benchmark seven frontier LLMs and four off-the-shelf emotion classifiers. The strongest LLM reaches 67.3 macro-F1, well below human agreement, while existing emotion classifiers score near chance. Beyond evaluation, CHIARO also serves as a training signal. When combined with an existing emotion corpus, the resulting downstream classifier improves on CHIARO itself and on six of ten external emotion benchmarks, which positions our dataset as a complementary signal for emotion recognition. Accepted to EMNLP 2026 (Main Conference) Dataset and code: https://github.com/cincynlp/Chiaro

**Решение:** + T1 кодирование эмоций по теории когнитивной оценки (appraisal theory): сравнение семи LLM с разметкой людей

---

### 36 · R10149

**Hard Emotion Test Evaluation Sets for Language Models**

2025 · Findings of the Association for Computational Linguistics: NAACL · conference-paper · en · https://doi.org/10.18653/v1/2025.findings-naacl.443

Language models perform well on emotion datasets but it remains unclear whether these models indeed understand emotions expressed in text or simply exploit supperficial lexical cues (e.g., emotion words).In this paper, we present two novel test evaluation sets sourced from two existing datasets that allow us to evaluate whether language models make real inferential decisions for emotion detection or not.Our human-annotated test sets are created by iteratively rephrasing input texts to gradually remove explicit emotion cues (while preserving the semantic similarity and the emotions) until a strong baseline BERT model yields incorrect predictions.Using our new test sets, we carry out a comprehensive analysis into the capabilities of small and large language models to predict emotions.Our analysis reveals that all models struggle to correctly predict emotions when emotion lexical cues become scarcer and scarcer, but large language models perform better than small pre-trained language models and push the performance by 14% over the 5% BERT baseline.We make our evaluation test sets and code publicly available.1

**Решение:** -4 NLP-бенчмарк эмоциональных лексических подсказок, общеязыковая задача

---

### 37 · R0711

**Actors, Frames and Arguments: A Multi-Decade Computational Analysis of Climate Discourse in Financial News using Large Language Models**

2026 · Underline Science Inc. · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48448/5jvj-y219

We curate a 980,061-article corpus of climate-related financial news from the Dow Jones Newswire (2000вЂ“2023) and introduce a three-stage ActorвЂ“FrameвЂ“Argument (AFA) pipeline that uses large language models to extract actors, stances, frames, and argumentative structures. We conduct AFA extraction on a stratified, uncertainty-enriched sample of 4,143 articles that preserves the temporal and thematic distributions of the full corpus. Reliability is established with a 2,000-article human-annotated gold standard and a Decompositional Verification Framework (DVF) that decomposes evaluation into completeness, faithfulness, coherence, and relevance, with multi-judge scoring calibrated against human ratings. Our longitudinal analysis uncovers a structural shift after 2015: coverage transitions from risk and regulatory-burden frames toward economic opportunity and technological innovation; financial institutions and companies increasingly deploy opportunity-centered arguments, while NGOs emphasize environmental urgency and governments stress compliance. Methodologically, we provide a replicable paradigm for longitudinal media analysis with LLMs. For high-stake domain insights, we map how the financial sector has internalized and reframed the climate crisis across two decades.

**Решение:** -4 климатический дискурс в финансовых новостях

---

### 38 · R3693

**Effectiveness and Reliability of Artificial Intelligence as an Assessment Tool for Student Learning Outcomes**

2026 · International Conference on E-Education, E-Business, E-Management, and E-Learning · conference · https://doi.org/10.1109/ic4e69618.2026.11631380

Artificial Intelligence (AI) continues to reshape assessment through automation, real-time feedback, and scalable evaluation techniques. This study evaluates the effectiveness, reliability, and fairness of an AI-based assessment tool-an LLM-powered “AI-Scorer” (developed on a proprietary GPT-3.5 architecture)-in measuring student learning outcomes from complex programming tasks. Using a convergent mixed-method design, the study compares AI scoring with human evaluators across four quantitative dimensions: inter-rater reliability, construct validity, diagnostic feedback quality, and algorithmic fairness. Statistical methods used include Cohen's Kappa, Intraclass Correlation Coefficient (ICC), Pearson correlation, and ANOVA. Results show that the AI-Scorer achieves excellent reliability (ICC $=0.84)$ for structured programming elements but only moderate validity $(\mathbf{r}<0. 6 0)$ for higher-order dimensions such as creativity. A mild linguistic bias was detected, favoring native English writers. Qualitative findings reveal high trust in AI objectivity but concerns about diagnostic depth and the need for human oversight. The study concludes that AI scoring can function as a consistent co-assessor, contingent on transparency, robust fairness audits, and continuous human interpretive oversight.

**Решение:** -4 автоматическая оценка студенческих программ по программированию (AI-Scorer)

---

### 39 · R0928

**Divergent creativity in humans and large language models.**

2026 · Scientific reports · journal article, journalarticle, preprint/article · eng · https://doi.org/10.1038/s41598-025-25157-3

The recent surge of Large Language Models (LLMs) has led to claims that they are approaching a level of creativity akin to human capabilities. This idea has sparked a blend of excitement and apprehension. However, a critical piece that has been missing in this discourse is a systematic evaluation of LLMs' semantic diversity, particularly in comparison to human divergent thinking. To bridge this gap, we leverage recent advances in computational creativity to analyze semantic divergence in both state-of-the-art LLMs and a substantial dataset of 100,000 humans. These divergence-based measures index associative thinking-the ability to access and combine remote concepts in semantic space-an established facet of creative cognition. We benchmark performance on the Divergent Association Task (DAT) and across multiple creative-writing tasks (haiku, story synopses, and flash fiction), using identical, objective scoring. We found evidence that LLMs can surpass average human performance on the DAT, and approach human creative writing abilities, yet they remain below the mean creativity scores observed among the more creative segment of human participants. Notably, even the top performing LLMs are still largely surpassed by the aggregated top half of human participants, underscoring a ceiling that current LLMs still fail to surpass. We also systematically varied linguistic strategy prompts and temperature, observing reliable gains in semantic divergence for several models. Our human-machine benchmarking framework addresses the polemic surrounding the imminent replacement of human creative labor by AI, disentangling the quality of the respective creative linguistic outputs using established objective measures. While prompting deeper exploration of the distinctive elements of human inventive thought compared to those of AI systems, we lay out a series of techniques to improve their outputs with respect to semantic diversity, such as prompt design and hyper-parameter tuning.

**Решение:** -2 дивергентная креативность: LLM в роли испытуемого (DAT)

---

### 40 · R11074

**Leveraging Guideline-Based Clinical Decision Support Systems with Large Language Models: A Case Study with Breast Cancer.**

2024 · Methods of information in medicine · journal article, journalarticle, article · eng · https://doi.org/10.1055/a-2528-4299

Abstract Background Multidisciplinary tumor boards (MTBs) have been established in most countries to allow experts collaboratively determine the best treatment decisions for cancer patients. However, MTBs often face challenges such as case overload, which can compromise MTB decision quality. Clinical decision support systems (CDSSs) have been introduced to assist clinicians in this process. Despite their potential, CDSSs are still underutilized in routine practice. The emergence of large language models (LLMs), such as ChatGPT, offers new opportunities to improve the efficiency and usability of traditional CDSSs. Objectives OncoDoc2 is a guideline-based CDSS developed using a documentary approach and applied to breast cancer management. This study aims to evaluate the potential of LLMs, used as question-answering (QA) systems, to improve the usability of OncoDoc2 across different prompt engineering techniques (PETs). Methods Data extracted from breast cancer patient summaries (BCPSs), together with questions formulated by OncoDoc2, were used to create prompts for various LLMs, and several PETs were designed and tested. Using a sample of 200 randomized BCPSs, LLMs and PETs were initially compared with regard to their responses to OncoDoc2 questions using classic metrics (accuracy, precision, recall, and F1 score). Best performing LLMs and PETs were further assessed by comparing the therapeutic recommendations generated by OncoDoc2, based on LLM inputs, to those provided by MTB clinicians using OncoDoc2. Finally, the best performing method was validated using a new sample of 30 randomized BCPSs. Results The combination of Mistral and OpenChat models under the enhanced Zero-Shot PET showed the best performance as a question-answering system. This approach gets a precision of 60.16%, a recall of 54.18%, an F1 score of 56.59%, and an accuracy of 75.57% on the validation set of 30 BCPSs. However, this approach yielded poor results as a CDSS, with only 16.67% of the recommendations generated by OncoDoc2 based on LLM inputs matching the gold standard. Conclusion All the criteria in the OncoDoc2 decision tree are crucial for capturing the uniqueness of each patient. Any deviation from a criterion alters the recommendations generated. Despite achieving a good accuracy rate of 75.57%, LLMs still face challenges in reliably understanding complex medical contexts and be effective as CDSSs.

**Решение:** -4 консилиум по раку молочной железы (OncoDoc2), онкология

---

### 41 · R2076

**The Defectometer: A Semantic-Geometric Measure of Reasoning Integrity for Verifiable AI**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.19136732

The Defectometer: A Semantic-Geometric Measure of Reasoning Integrity for Verifiable AI Author: Frédéric David BlumAffiliation: Catalyst AI Research, Tel Aviv, IsraelContact: freddavidblum@catalystais.comORCID: 0009-0009-2487-2974License: Paper: CC-BY-4.0 | Code: MITDate: March 2026 Description We introduce the Defectometer, a computable semantic-geometric measure that quantifies the integrity of inference traces produced by large language models (LLMs) or human reasoning chains. The Defectometer operates on a directed acyclic graph (DAG) of claims equipped with semantic embeddings, and computes two complementary scores: D (Semantic Coherence Gap) — measures the distance from each conclusion to the convex hull of its premises' embeddings, normalized by premise dispersion. Captures semantic depth: how far the conclusion leaps beyond what the premises jointly span. B (Premise Balance Score) — detects asymmetric engagement with premises via entropy of the optimal convex projection weights. Captures directional silence: when a conclusion selectively ignores available premises despite semantic proximity. Core Formula D(Γ,E) = Σ_v [SCG(v) / (1 + γ·PSD(v))] · log(in(v) + 1) B(Γ,E) = Σ_v imbalance(v) · log(in(v) + 1) The pair (D, B) produces a two-dimensional diagnostic: B low (balanced) B high (imbalanced) D high (deep) PROFOUND — deep insight, all premises engaged (E=mc², Gödel) SUSPICIOUS — large claim with selective evidence D low (no leap) SOUND — conclusion follows predictably from premises DEFECTIVE — conclusion ignores some premises (logical defect, Gish Gallop) Bond Pricing for Cryptoeconomic Verification For adversarial verification protocols (Cortex Protocol): Bond* = κ · (1 + D) / (1 + β · B) Depth D increases the bond (genuine novelty is valuable); imbalance B decreases it (defective reasoning carries higher challenge risk). D acts as a coupon; B acts as a credit spread. Key Results Trace D (depth) B (balance) Soundness Bond I3 Defective (A∧B→C split) 0.001 0.660 0.431 0.431 I3 Corrected 0.000 0.032 0.940 0.940 E = mc² 4.279 0.000 0.189 0.189 Gish Gallop (50 premises) 0.609 1.805 0.192 0.192 Gödel's Incompleteness 3.423 0.000 0.226 0.226 Negative Result: Hodge Laplacian Failure We also report that the discrete Hodge Laplacian on inference DAGs cannot detect logical defects. On the I3 trace, L₁ has eigenvalues [0.586, 2, 2, 3.414, 4] with trivial first cohomology H¹ = 0. The defect is invisible because DAGs have no cycles, therefore no higher homology. This motivated the Defectometer's use of semantic embeddings rather than pure topology. Novel Concepts Introduced Directional Silence — the measurable phenomenon of a conclusion selectively ignoring available premises Epistemic Friction — situations where an argument could have engaged a premise but did not, despite semantic proximity; the signature of avoidance rather than error Minimal Viable Reasoning Graph — a conjectured threshold below which logical diagnosis is fundamentally under-determined (analogous to Shannon's channel capacity) Risk-Adjusted Bond Pricing — treating reasoning depth as a coupon and premise imbalance as a credit spread in cryptoeconomic verification markets Files Included File Description defectometer-preprint.pdf Full preprint with diagnostic plot, results tables, and complete source code (Appendix A) defectometer.py Python implementation (~450 lines). Core algorithm, 5 test cases, null model shuffle test. Dependencies: numpy, scipy How to Run pip install numpy scipy python defectometer.py Output: comparison table of all 5 test cases + null model analysis. For real embeddings (requires sentence-transformers): from sentence_transformers import SentenceTransformer model = SentenceTransformer('all-MiniLM-L6-v2') # Embed claims for claim in trace.claims.values(): claim.embedding = model.encode(claim.text) # Run Defectometer result = defectometer(trace) print(result) Related Publications Blum, F.D. (2026). Cortex Protocol: A Reasoning Verification Market for Autonomous AI Agents. Zenodo. DOI: 10.5281/zenodo.19003627 Blum, F.D. (2026). Sigil Protocol: Cybersecurity Extension of Cortex. Zenodo. DOI: 10.5281/zenodo.19027462 Blum, F.D. (2026). FDBC/ESG: Bost-Connes System and Witten Laplacian. Zenodo. DOI: 10.5281/zenodo.18859602 Blum, F.D. (2026). Prime States and Spectral Transitions. Zenodo. DOI: 10.5281/zenodo.19023888 Citation @misc{blum2026defectometer, title={The Defectometer: A Semantic-Geometric Measure of Reasoning Integrity for Verifiable AI}, author={Blum, Frédéric David}, year={2026}, publisher={Zenodo}, note={Preprint} } Keywords reasoning verification, semantic coherence, inference graph, Hodge Laplacian, cryptoeconomic bonds, LLM evaluation, epistemic integrity, directional silence, epistemic friction, Cortex Protocol, Catalyst AI

**Решение:** -4 The Defectometer: геометрическая мера целостности рассуждений ИИ

---

### 42 · R8702

**A Novel Multi-Modal Framework for Sentiment Driven Depression Intensity Assessment**

2025 · Journal of Information Systems Engineering & Management · journalarticle, article · en · https://doi.org/10.52783/jisem.v10i30s.4779

Introduction: Depression is a mental illness that can cause a low mood, loss of interest in doing things, and sudden behavioral changes. Major depression may lead to suicide. It is the life threatening problem to be addressed immediately. According to the World Health Organization (WHO), about 280 million people worldwide have depression, including 5% of the world’s adults and 5.7% of adults above age 60. Once a person diagnosed with depression treatment continue by attending therapy sessions. All these traditional approaches will work on those who already diagnosed with the depression. Through the social media platforms vast data is generating, from the content taken from theses platforms by applying Large Language Models, which works on contest based rather than key based would give better results. So a preventive mechanism of finding depression severity from the text is a novel idea for earlier prediction. Objectives: The main objective of the paper is to identify the depression intensity from the social media posts by applying the LLMs to find the behavioral and emotional patterns of posts. Identification of negative sentiments from the posts by using LLMs. PHQ-9 Questionnaire is used to find the t The LLM based models identifies the negative sentiments based on polarity. From these posts the seed terms were identified based PHQ-9 questionnaire. The next objective is to identify the intensity based the terms used in the posts. Methods: This study proposes a multi-modal framework for depression intensity using NLP techniques. The data is extracted from twitter posted based on depression related hashtags. Preprocessing and feature extraction is done. Once data is ready after cleaning the transformer models like BERT, ALBERT techniques are applied fro depression severity estimation. Model is evaluated using deep learning models (BiLSTM, GRU) with accuracy, F1-score and loss estimation was evaluated. Results: The bLSTM model achieved 92% accuracy, outperforming traditional methods. Transformer-based models (BERT, ALBERT) demonstrated improved classification performance. Conclusions: The multi modal approach proved to be more accurate for earlier prediction purpose. The Same approach can be applied on various questionnaire based approaches for model evaluation. This approach can be used for self-assessment purpose.

**Решение:** -5 оценка депрессии: только модели BERT, ALBERT, BiLSTM, без генеративных LLM

---

### 43 · R5090

**Smart Interview: AI-Driven Interview Automation with Candidate Performance Analysis**

2026 · International Scientific Journal of Engineering and Management · journalarticle, article · https://doi.org/10.55041/isjem.acme105

In many organizations, technical interviews can be quite different depending on the interviewer, and this can cause inconsistencies, biases, and scaling issues in the interview process. To address these issues, this paper presents an intelligent interview system that employs a Large Language Model (LLM) to automate the entire technical interview process. The system offers role specific questions depending on the job description of the candidate and allows administrators to define parameters such as difficulty level, number of questions, and type of questions. The system allows different types of question formats, including descriptive, coding, and multiplechoice questions. For the purpose of validation in evaluation, the system employs structured validation for multiple-choice questions, without revealing the answers, and employys LLM scoring for descriptive answers. To maintain integrity in remote technical interviews, thesystem allows the use of lightweight proctoring features such as motion detection and tab switching. The system also allows automated scoring, summary, and email notification. The experimental results show that the systemimproves consistency in scoring, automates the process, and scales the interview process. The proposed system is a practical and flexible solution for AI recruitment.

**Решение:** -4 автоматизация технических собеседований при найме кандидатов

---

### 44 · R11384

**Zero-Shot Strike: Testing the generalisation capabilities of out-of-the-box LLM models for depression detection**

2024 · Computer Speech & Language · article · en · https://doi.org/10.1016/j.csl.2024.101663

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T3 детекция депрессии с помощью zero-shot LLM, нет аннотации — проверить эталон в полном тексте

---

### 45 · R10971

**Assessing the Impact of Conspiracy Theories Using Large Language Models**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2412.07019

Measuring the relative impact of CTs is important for prioritizing responses and allocating resources effectively, especially during crises. However, assessing the actual impact of CTs on the public poses unique challenges. It requires not only the collection of CT-specific knowledge but also diverse information from social, psychological, and cultural dimensions. Recent advancements in large language models (LLMs) suggest their potential utility in this context, not only due to their extensive knowledge from large training corpora but also because they can be harnessed for complex reasoning. In this work, we develop datasets of popular CTs with human-annotated impacts. Borrowing insights from human impact assessment processes, we then design tailored strategies to leverage LLMs for performing human-like CT impact assessments. Through rigorous experiments, we textit{discover that an impact assessment mode using multi-step reasoning to analyze more CT-related evidence critically produces accurate results; and most LLMs demonstrate strong bias, such as assigning higher impacts to CTs presented earlier in the prompt, while generating less accurate impact assessments for emotionally charged and verbose CTs.

**Решение:** -4 оценка влияния теорий заговора, социология/политология

---

### 46 · R1442

**A Direct-Observation Coding Instrument for Doctoral Viva Questions: Retrieval, Extension, Adjacency, and the Examination of Claimed Contribution**

2026 · Zenodo · text/ · https://doi.org/10.5281/zenodo.21971124

Research on doctoral examination has developed over twenty-five years, but it has relied almost entirely on indirect methods: interviews with examiners, analysis of examiners' written reports, candidate recollection, and policy review. The reason is structural rather than a matter of research priorities. As Morley, Leonard and David (2002) noted, the viva is rarely witnessed by anyone outside the examination process, which constrains both monitoring and research into the assessment itself. In the systems that produced this literature, the doctoral defence is closed. In Jordanian universities, and in a number of other systems, the doctoral defence is a public session. The methodological barrier does not apply, and direct observation becomes possible. This instrument supports the systematic observation and coding of doctoral defences along two axes. The first classifies every question posed on a single formal criterion — whether the answer is available within the thesis itself — across four categories: direct retrieval, extension, adjacent, and formal. The criterion is deliberately formal rather than evaluative, so that coding does not depend on the observer's judgement of question quality. The second axis records whether the contribution to knowledge required by the institution's own regulations is explicitly examined, or is instead assumed from the existence of the document. The instrument additionally captures response latency, questioner role, and the verbatim wording of the contribution question where one is posed. The instrument is released for reuse in any system where doctoral defences are held in public. It includes coding rules with worked examples, boundary-case resolutions, an inter-rater reliability protocol, and ethical constraints prohibiti AI disclosure: The conceptual framework, the retrieval/extension/adjacency distinction, and the research questions are the author's own. A large language model (Claude, Anthropic) was used as an editorial and structuring aid in drafting this instrument, in reviewing the prior literature, and in translating source material. All literature cited was independently verified by the author. The author is solely responsible for the content.

**Решение:** -5 инструмент наблюдения за защитой диссертаций, нет LLM

---

### 47 · R10321

**82 ARTIFICIAL INTELLIGENCE ASSISTED MENTAL HEALTH EVALUATION SYSTEM FOR COLLEGE STUDENTS IN SOUTH CHINA: AN EMPIRICAL STUDY BASED ON LARGE LANGUAGE MODELS (LLMS)**

2025 · Current Opinion in Psychiatry · conference-abstract · en · https://doi.org/10.1097/01.yco.0001176016.43210.73

Background: China's Ministry of Education 2024 White Paper sets targets for intelligent mental health screening and for breakthroughs in multilingual assessment in South China. Six representative universities in this region perform∼180,000 screenings annually; traditional workflows consume≍1,200 person-days and yield high-risk detection accuracy below 68%. We designed and evaluated an AI-assisted mental health assessment system that fuses a general large language model (GPT–4) with a Chinese–optimized model (DeepSeek) to improve efficiecy and cultural/language adaptation for large-scale screening. Subjects and Methods: The system implements data ingestion and anonymization, LLM fusion analysis (task partitioning, prompt engineering, cascade/weighted fusion), evidence-backed risk scoring, human-in-the-loop review and automated reporting. Illustrative pilot analyses used simulated/deidentified screening data (n≍54,312) from six South China universities (PHQ-9, GAD-7, PSS-10 and open-ended responses). A quasi-experimental design compared AI-assisted vs manual workflows with baseline (T1) and six-month follow-up (T2). Outcomes: processing time, staff person–days, classification metrics (precision, recall, F1, AUC, Kappa), psychometric changes (repeated measures ANOVA / mixed models), help-seeking rates, SUS usability, and subgroup fairness metrics. Results (Illustrative): AI assistance reduced end-to-end processing time by≍78% vs manual workflows (p<0.001). GPT-4+DeepSeek fusion achieved precision=0.91, recall=0.94, F1=0.925, AUC=0.96 against clinician adjudication (simulated ground truth). Experimental cohorts showed larger reductions in PHQ-9/GAD-7/PSS-10 at T2 (group×time interaction p<0.01) and higher help–seeking (7.8% vs 3.6%, χ2 p<0.001). SUS ≍78; clinicians requested stronger explainability and continuous bias monitoring. Targeted reweighting reduced subgroup recall gaps. Conclusions: A mixed LLM approach combining GPT-4 with a Chinese-optimized model is feasible and effective for large–scale, culturally adapted university mental health screening. Responsible deployment requires robust privacy safeguards, human oversight, and continuous fairness auditing. Future work: multi–site trials, multimodal integration, and cost–effectiveness analyses.

**Решение:** + T3 оценка психического здоровья студентов: GPT-4 и DeepSeek против клиницистов, каппа и F1

---

### 48 · R2975

**MindEval2: Clinically Grounded Patients and Rubrics for Evaluating Language Models in Mental Health Support**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.22314

With people increasingly turning to AI chatbots for mental health support, the need to evaluate these tools is becoming more pressing. Recent benchmarks attempt to mimic a realistic setting by simulating multi-turn interactions with synthetic patients and evaluating them with an LLM-as-a-judge. However, the usefulness of these methods is limited because simulated patients can be overly forthcoming and self-reflective, and judgments typically involve opaque Likert scales with unclear practical utility. To bridge these gaps, we introduce MindEval2, an evaluation framework that consists of two components: Mental Health Quality Rubrics (MHQR), for evaluation, and MindSim, for patient simulation. For MHQR, we collaborate with PhD-level psychologists to develop a set of rubrics that break down response quality into explicit operational criteria that are more interpretable and actionable than existing evaluation taxonomies. MindSim, in turn, is an LLM harness that combines carefully-designed patient profiles with tools, enabling more varied, challenging, and realistic interactions than existing baselines. The harness also contains a memory component that is updated between each interaction, enabling MindEval2 to model the longitudinal aspect of mental health. We evaluate 18 proprietary and open-weight models on MindEval2, finding that while frontier models have largely improved on issues related to surface level quality and boundaries, guidance calibration remains the dominant failure mode across all models, accounting for most of the quality gap. 47 pages, 17 figures, 23 tables. Code, prompts, benchmark profiles and annotations: https://github.com/SWORDHealth/mind-eval

**Решение:** ? T4 MindEval2: рубрики оценки качества ответов в mental health; проверить согласие LLM-судьи с психологами

---

### 49 · R12468

**Reflections on the use of artificial intelligence in psychiatric diagnosis**

2023 · Salud Mental · article · en · https://doi.org/10.17711/sm.0185-3325.2023.036

I recently had the opportunity to read the article “Evaluating the Performance of ChatGPT in Differential Diagnosis of Neurodevelopmental Disorders: A Pediatricians-Machine Comparison,” published in Psychiatry Research journal. Authors Wei, Cui, Wei, Cheng, & Xu (2023) used Cohen’s Kappa values to compare the diagnostic accuracy of a sample of pediatric residents, experienced pediatricians, and ChatGPT-4 (Open AI, San Francisco, California), an artificial intelligence chatbot. In this exercise, the researchers gave the study groups the results of the Early Language Milestone Scale, the Gesell Developmental Scale, the Modified Checklist for Autism in Toddlers, and the Autism Behavior Checklist, as well as the gender and age of patients. During the second round, this information was complemented by vignettes containing aspects of clinical interest such as chief complaint, developmental milestones achieved and family history. For each scenario, both pediatricians and the chatbot were asked to select the most likely diagnosis from Autism Spectrum Disorder, Global Developmental Delay, and Developmental Language Disorder. The study reported diagnostic accuracy values of 66.7% for experienced pediatricians and ChatGPT, surpassing pediatric residents, who achieved just 55.3%. The level of agreement between experienced pediatricians and ChatGPT, according to the Kappa value, was .43. When vignettes were included, the chatbot’s accuracy decreased to 53.3%, and interobserver agreement between the chatbot and pediatricians dropped to .35. Interestingly, this exercise was performed with the ChatGPT-4 version available to the public (at the time of writing, it operated under a subscription model) and is only trained with non-specialized information available on the Internet. The next few years will see many more articles like this one, particularly since it is possible to specialize the linguistic models under which these types of tools operate using data sets with better resolution or specificity to answer questions related to each specialized field.

**Решение:** -1 комментарий / письмо в редакцию к исследованию диагностики нарушений развития

---

### 50 · R7994

**Deep Learning Approaches to Natural Language Processing for Digital Twins of Patients in Psychiatry and Neurological Rehabilitation**

2025 · Electronics · journalarticle, article · en · https://doi.org/10.3390/electronics14102024

Deep learning (DL) approaches to natural language processing (NLP) offer powerful tools for creating digital twins (DTs) of patients in psychiatry and neurological rehabilitation by processing unstructured textual data such as clinical notes, therapy transcripts, and patient-reported outcomes. Techniques such as transformer models (e.g., BERT, GPT) enable the analysis of nuanced language patterns to assess mental health, cognitive impairment, and emotional states. These models can capture subtle linguistic features that correlate with symptoms of degenerative disorders (e.g., aMCI) and mental disorders such as depression or anxiety, providing valuable insights for personalized treatment. In neurological rehabilitation, NLP models help track progress by analyzing a patient’s language during therapy, such as recovery from aphasia or cognitive decline caused by neurological deficits. DL methods integrate multimodal data by combining NLP with speech, gesture, and sensor data to create holistic DTs that simulate patient behavior and health trajectories. Recurrent neural networks (RNNs) and attention mechanisms are commonly used to analyze time-series conversational data, enabling long-term tracking of a patient’s mental health. These approaches support predictive analytics and early diagnosis by predicting potential relapses or adverse events by identifying patterns in patient communication over time. However, it is important to note that ethical considerations such as ensuring data privacy, avoiding bias, and ensuring explainability are crucial when implementing NLP models in clinical settings to ensure patient trust and safety. NLP-based DTs can facilitate collaborative care by summarizing patient insights and providing actionable recommendations to medical staff in real time. By leveraging DL, these DTs offer scalable, data-driven solutions to promote personalized care and improve outcomes in psychiatry and neurological rehabilitation.

**Решение:** -1 обзор применения DL/NLP для цифровых двойников в психиатрии

---

### 51 · R6486

**Comparative Study of Prompt Engineering Strategies for LLM-Based Automated Grading of Career Sentence Completion Test**

2026 · Journal of Digital Contents Society · journalarticle, article · en · https://doi.org/10.9728/dcs.2026.27.4.1061

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T2 скоринг теста незавершённых предложений (Sentence Completion Test), нет аннотации — проверить в полном тексте

---

### 52 · R0502

**Narrating the AI Act: Policy narratives on artificial intelligence, their construction, and evolution within the European Parliament**

2026 · Government Information Quarterly · article · en · https://doi.org/10.1016/j.giq.2026.102159

This article investigates how Members of the European Parliament (MEPs) constructed policy narratives on artificial intelligence (AI) in the legislative process leading up to the EU Artificial Intelligence Act (AI Act) adopted in 2024. While previous research has primarily focused on executive-driven strategy documents, the Parliament's discursive role remains underexplored. To address this gap, the study applies the Narrative Policy Framework (NPF) to a corpus of 18 parliamentary documents from 2020 to 2024, in which 500 narratives were manually coded according to the NPF categories of plot, character, setting, and moral. The findings reveal remarkable stability in the Parliament's AI narratives over time, despite significant external shocks such as the release of ChatGPT 3.5 in 2022. Plots were dominated by stories of control and rising, supported by heroes and beneficiaries, framing AI as both manageable and beneficial. Settings spanned security, global competition, and European legal norms, while morals centered on risk-based regulation, ethical standards, and calls for a joint approach. By illuminating how the European Parliament narrates AI policy, this study contributes to understanding the discursive dynamics shaping EU AI governance and their implications for digital government research, particularly regarding the normative conditions under which AI systems are adopted in public administration.

**Решение:** -4 политические нарративы об AI Act в Европарламенте

---

### 53 · R6122

**Detecting change in clinical communication skills: Responsiveness of the Gap-Kalamazoo communication skills assessment form scored by experts and ChatGPT.**

2026 · Patient education and counseling · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.pec.2026.109829

OBJECTIVE The Gap-Kalamazoo Communication Skills Assessment Form (GKCSAF) is widely used to assess clinicians' communication skills. While expert-rated administration of the GKCSAF is seen as objective and thorough, manual scoring is time- and resource-intensive. The ChatGPT-rated GKCSAF is a large language model-based rating approach that uses the same GKCSAF items and scoring criteria. It shows acceptable reliability and validity while reducing rater burden. However, the responsiveness of the expert-rated and ChatGPT-rated GKCSAF has remained unknown, limiting the interpretation of change scores in communication skills. The study aimed to compare the responsiveness of the expert-rated and ChatGPT-rated GKCSAF. METHODS Eighty occupational therapy students completed two recorded clinical interactions with different patients. Between interactions, students received training via the Communication Skills Measure for Therapists, a formative measure that assesses communication skills and yields actionable feedback. Transcripts of the interactions were independently scored by trained expert raters and by ChatGPT. Responsiveness was examined using paired t-tests, Cohen's d, and standardized response mean (SRM). Differences in responsiveness indices between the rating approaches (i.e., the expert-rated and ChatGPT-rated GKCSAF) were estimated using bootstrap confidence intervals. RESULTS For both rating approaches, mean post-training scores were significantly higher than mean pre-training scores (both t = 3.8, p < 0.001). The responsiveness indices were nearly moderate (expert-rated GKCSAF: d = 0.45, SRM = 0.42; ChatGPT-rated GKCSAF: d = 0.47, SRM = 0.43), with no significant differences between the two rating approaches (bootstrap 95% confidence intervals for the differences included zero). CONCLUSIONS Both the ChatGPT-rated and expert-rated GKCSAF showed evidence of responsiveness for detecting changes in clinicians' communication skills. PRACTICE IMPLICATIONS Considering the shorter scoring time and reduced rater burden of the ChatGPT-rated GKCSAF, it may be a promising outcome assessment for clinical and research use.

**Решение:** + T4/T1 оценка клинических коммуникативных навыков по форме Gap-Kalamazoo: ChatGPT против экспертов

---

### 54 · R2083

**Education Research: Quality of Narrative Feedback Generated by a Large Language Model Compared With Expert Faculty for Case-Based Learning in Neurology Education.**

2026 · Neurology. Education · journal article, journalarticle, article · eng · https://doi.org/10.1212/ne9.0000000000200320

Background and Objectives: Neurology learners often receive limited feedback in clinical settings because of workflow constraints, variability in supervision, and competing clinical demands. Artificial intelligence, including large language models (LLMs) may help address these gaps and provide clinical learners with effective formative feedback by generating real-time, case-specific feedback during neurology case-based learning (CBL). The aim of this study was to examine how the quality of LLM-generated feedback compares with human expert-generated feedback in neurology CBL. Methods: In this exploratory quantitative study, student participants undertook LLM-enabled interactive cases on the TEACHABLE platform, which included history gathering, physical examination elements, and ordering diagnostic testing. Participants were clinical-level students recruited from 2 medical institutions. Case transcripts were recorded and analyzed for feedback generation, which was provided by an LLM and human experts in 2 components: history taking/physical examination elements (H&P) and assessment and plan (A&P). Feedback characteristics including sentence count, word count, and reference to case key learning points were summarized and compared. Feedback quality was scored by blinded experts using the QuAL and EFeCT instruments. Results were compared for the H&P and A&P components of the case interactions. Results: Four student participants completed 5 interactive cases each, generating 20 total transcripts for feedback. Word and sentence number were similar among LLM-generated and expert-generated feedback, except for a greater word length in expert-generated A&P feedback. Regarding H&P, the LLM commented on the key learning points in 20/20 (100%) of the cases as compared with 39/60 (65%) for the human experts. For A&P, the LLM feedback discussed key points in 20/20 (100%) cases as compared with 39/40 (97.5%) for the human experts. The LLM feedback had no medical inaccuracies. QuAL and EFeCT scores were significantly greater for the LLM as compared with human experts for the H&P component, but not significantly different for the A&P component. Discussion: LLMs provided with key learning points can generate timely, quality feedback on case-based interactions in a manner comparable with human experts. A hybrid framework combining LLM-generated feedback with faculty input may offer high-quality and equitably accessible formative feedback at scale. These pilot findings are limited by a small sample size and experimental setting.

**Решение:** -2 эксперты оценивают качество обратной связи по неврологии, сгенерированной LLM

---

### 55 · R2161

**Blinded multi-model evaluation of large language models as raters of hospital incident reports (severity, event type, and sentinel-event classification): dataset, protocol, and analysis code.**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/mgwve

This project holds the materials, de-identified data, analysis code and results for a completed study evaluating whether five contemporary large language models (LLMs) can reproduce expert-adjudicated classifications of hospital incident reports from the free-text narrative alone. Incident reports were drawn from a single Italian tertiary-care hospital (events 2015–2025); models were queried blind (narrative only) at temperature 0 with a common prompt in June 2026, with a test–retest run in August 2026. The project contains the protocol as conducted, the coding scheme (codebook), the prompts, the expert reference key, per-model outputs, the scoring code, and result tables.

**Решение:** -4 кодирование госпитальных инцидентов безопасности, нет клинико-психологического конструкта

---

### 56 · R4342

**GENERATIVE AI AND THE FUTURE OF AUTHORSHIP: MODERN AND CONTEMPORARY ART AS A METHOD FOR PRESERVING HUMAN SUBJECTIVITY**

2026 · Social informatics journal · journalarticle, article · https://doi.org/10.58898/famedia.v1.3

This article examines the transformation of the author’s role within a digital media environment saturated with generative content and algorithmically mediated communication. In the context of the rapid expansion of synthetic texts, images, and audiovisual materials, the central problem is increasingly defined by an erosion of authorial subjectivity, interpretive depth, and the capacity to produce new structures of meaning. The article proposes the concept of the author as an architect of meaning – a new role model for the contemporary media producer who uses generative AI not as a substitute for the creative act, but as an infrastructural tool for automating routine processes and freeing cognitive resources for interpretation, critical thinking, and meaning-making. The theoretical foundation of the article is an original interdisciplinary methodology grounded in the use of modern and contemporary art as a framework for cultivating cognitive flexibility, divergent thinking, and the capacity to work with uncertainty. Its practical dimension draws on the author’s professional experience in designing educational and media formats, working with small learning communities, and integrating tailored AI workflows into research and editorial practice. The article argues that the sustainable media ecology of the future will be shaped not by the endless production of content, but by the author’s ability to construct distinctive structures of meaning and forms of sustained intellectual presence.

**Решение:** -4 философский анализ авторства и современного искусства

---

### 57 · R0872

**Statistical and qualitative analysis of ChatGPT and human raters in preservice teachers’ writing assessment**

2026 · International Journal of Assessment Tools in Education · journalarticle, review, article · en · https://doi.org/10.21449/ijate.1678002

Teachers spend a significant amount of time providing feedback. This study compared expert and ChatGPT assessments and feedback on written texts to determine the suitability of AI for writing skill assessments that are time-consuming to assess and provide feedback. Three experts and ChatGPT graded 14 Turkish undergraduate students’ assignments using rubric that included content, language use, vocabulary, organization, and mechanics, and justified their decisions. The study involved document review and triangulation, a qualitative design. In addition, an intraclass correlation coefficient was used to assess the consistency of the ChatGPT and the experts’ scores. All feedback was qualitatively analyzed to identify the strengths and weaknesses of the experts and their similarities with ChatGPT. Experts and ChatGPT had moderate to weak consistency in the writing subscales, while good reliability was found in the total score. Experts excelled in ‘explanatory feedback’, ‘interpretation’ and ‘experience’, while ChatGPT excelled in ‘automation and continuity’ and ‘data processing capacity’. Experts’ weaknesses included ‘limited time and energy’ and ‘comparison bias’, while ChatGPT’s weaknesses were ‘ambiguous expressions’ and ‘repetition’. The study also found that experts and ChatGPT preferred to provide constructive and supportive feedback.

**Решение:** -4 оценка письменных работ студентов-педагогов

---

### 58 · R0594

**Multimodal Depression Detection An Integrated Multimodal Framework for Automated Depression Severity Assessment**

2026 · International Journal of Leading Research Publication. · journalarticle, article · https://doi.org/10.70528/ijlrp.v7.i5.2191

Depression remains one of the most prevalent mental health disorders globally, yet early detection remains challenging due to its multifaceted and heterogeneous clinical presentation [1]. This study presents a novel multimodal depression detection system that integrates five distinct analytical modalities: facial expression analysis, vocal tone assessment, video-based emotion recognition, text sentiment analysis, and clinical questionnaire evaluation. Using a probability-weighted scoring mechanism combined with an unequal weighting scheme that prioritizes explicit user input, the system generates a comprehensive depression severity score on a 0–100 scale with clinically relevant classification thresholds. The architecture leverages convolutional neural networks (CNNs) [4] for image and video processing, long short-term memory (LSTM) networks [5] for audio analysis, a trained sequence model for text classification, and large language model (LLM) integration via the Groq API for open-ended questionnaire assessment. By combining noisy ambient snapshots with explicit clinical input, the system achieves a holistic psychological profile that extends beyond single-modality approaches [8]. This paper describes the technical implementation, mathematical framework, and clinical classification methodology underlying this integrated system.

**Решение:** -6 архитектура системы мультимодальной детекции депрессии без эмпирической валидации согласия

---

### 59 · R3461

**Generative AI Use in Learning and Research Among Undergraduate Clinical Medical Students in China: A Task-Recall Qualitative Study (Preprint)**

2026 · JMIR Publications Inc. · posted-content, preprint · https://doi.org/10.2196/preprints.114386

BACKGROUND Background: Undergraduate medical students increasingly use generative artificial intelligence (GenAI) for learning and research-related tasks. However, less is known about how they refine prompts, revise outputs, verify information, and negotiate boundaries within specific educational tasks. OBJECTIVE Objective: This study aimed to explore how undergraduate clinical medical students in China described using GenAI in specific learning and research tasks, focusing on prompt refinement, output revision, verification, and ethical and cognitive boundary negotiation. METHODS Methods: We conducted individual semistructured remote interviews via WeChat voice calls or telephone using a task-recall approach with 50 undergraduate clinical medical students recruited through purposive sampling, supported by social media outreach and peer referral. Participants varied in training year, sex, internship status, and self-reported GenAI use. Interviews were conducted in Mandarin Chinese, audio-recorded in full with participants’ permission, transcribed verbatim, deidentified, and analyzed using codebook-informed thematic analysis with iterative team discussion. RESULTS Results: The analysis generated five interrelated themes: convenience-driven entry into AI use, iterative co-construction of outputs for medical learning, critical verification before trust, ethical and cognitive boundary negotiation, and perceived institutional support needs. These themes informed an interpretive process model that distinguished reported task practices from perceived institutional support needs. Participants described using GenAI under task pressure, refining prompts, adapting outputs, and checking claims and references against other sources. Verification could prompt further revision, while concerns about academic integrity, independent reasoning, and group responsibility shaped decisions about whether and how outputs were used. Participants also described the workload involved in checking plausible errors and requested clearer rules, task-based training, and tools with traceable sources. CONCLUSIONS Conclusions: Participants’ accounts suggest that GenAI use in medical learning involves iterative revision, verification, and boundary negotiation. The findings highlight verification and accountability as priorities for task-based AI literacy education. The model reflects reported practices and does not establish verification effectiveness or improvements in learning outcomes.

**Решение:** -1 качественное исследование использования GenAI студентами-медиками

---

### 60 · R11816

**A Summary of Advances in Document Summarization from 2023-2024**

2024 · casereport, review, report · en · https://doi.org/10.2172/2462994

In computer science, Document Summarization is the task of condensing some quantity of text and related content through automated means. The resulting summary is expected to emphasize key information from the original text in the service of some purpose. In this document, we review recent literature in text summarization. The “hybrid” extractive-abstractive approaches training transformers and graph neural networks to prioritize and incorporate content into generated text continue to be explored, with some efforts continuing to test such methods on domain-specific and non-English text. Some of the latest efforts have also sought to enable users to adjust summaries with queries or other structure and benefit from new chat and instructible large language models. While summaries are evaluated qualitatively on relevance and salience, in addition to brevity and faithfulness to the original text, many traditional metrics are poorly correlated to human judgements and the field continues to seek good quantitative metrics for evaluating competing approaches; this related task has also begun to test reinforcement-learning style agentic LLM-based solutions. We see opportunities for leveraging causal analysis, psychology, and agent-based solutions to create more trustworthy, natural, and interactive content summarization systems.

**Решение:** -1 обзор методов автоматической суммаризации документов

---

### 61 · R10230

**Symbolically Scaffolded Play: Designing Role-Sensitive Prompts for Generative NPC Dialogue**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2510.25820

Large Language Models (LLMs) promise to transform interactive games by enabling non-player characters (NPCs) to sustain unscripted dialogue. Yet it remains unclear whether constrained prompts actually improve player experience. We investigate this question through The Interview, a voice-based detective game powered by GPT-4o. A within-subjects usability study ($N=10$) compared high-constraint (HCP) and low-constraint (LCP) prompts, revealing no reliable experiential differences beyond sensitivity to technical breakdowns. Guided by these findings, we redesigned the HCP into a hybrid JSON+RAG scaffold and conducted a synthetic evaluation with an LLM judge, positioned as an early-stage complement to usability testing. Results uncovered a novel pattern: scaffolding effects were role-dependent: the Interviewer (quest-giver NPC) gained stability, while suspect NPCs lost improvisational believability. These findings overturn the assumption that tighter constraints inherently enhance play. Extending fuzzy-symbolic scaffolding, we introduce \textit{Symbolically Scaffolded Play}, a framework in which symbolic structures are expressed as fuzzy, numerical boundaries that stabilize coherence where needed while preserving improvisation where surprise sustains engagement.

**Решение:** -4 диалоги игровых персонажей (NPC) в видеоиграх

---

### 62 · R5009

**DialogPII: A multilingual dataset of synthetic dialog transcripts to detect personal information**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.30312

Conversational data collected in domains such as healthcare or social sciences is a valuable resource for research and automated analysis. However, responsible data sharing requires the detection and removal of personally identifiable and sensitive information to protect individual privacy. To support the development and evaluation of automatic de-identification systems, we present DialogPII, a multilingual dataset of synthetic dialogs and speech-derived transcripts for personal information detection. DialogPII covers eight interaction scenarios (emergency calls, medical anamnesis interviews, therapy sessions, insurance communication, customer support, clinical interviews regarding an AI-supported dashboard, police reports, and group therapy discussions), 19 entity types, and 11 languages (English, Arabic, Finnish, French, German, Hindi, Italian, Polish, Portuguese, Spanish, and Turkish). Dialogs were generated semi-automatically using large language models, manually curated for plausibility and diversity, and localized to country- and city-specific contexts. All dialogs were additionally converted to speech via text-to-speech synthesis, transcribed with Whisper, and annotated through automatic projection and manual correction, yielding aligned written and speech-derived resources across all languages. We further release baseline multilingual named entity recognition models and provide technical validation through inter-annotator agreement analysis, translation quality evaluation, annotation projection assessment, and benchmark experiments with transformer-based sequence labeling models. currently under review

**Решение:** -4 деидентификация персональных данных (PII) в диалогах

---

### 63 · R4905

**Trusted or Tricked? A Multi-Layer Robustness Scoring Framework for Evaluating LLMs Against Public Health Misinformation**

2026 · Annals of Computer Science and Information Systems · conference-paper · https://doi.org/10.15439/2026f3733

The increasing use of Large Language Models (LLMs) as accessible sources of public health information raises concerns about their potential to generate or reinforce medical misinformation.This study evaluates four state-of-the-art LLMs (LLaMA, DeepSeek, Gemini, and GPT-4.1-nano)using the U.S. Centers for Disease Control and Prevention (CDC)verified medical questions to assess factual reliability, consistency, and robustness under neutral, provocative, and misinformationseeking prompts.We propose a two-layer evaluation framework that combines quantitative behavioral metrics including factual alignment, semantic and topic drift, hallucination, toxicity, overconfidence, and refusal behavior with qualitative LLM-as-a-judge assessment into a unified robustness score.This enables a comprehensive evaluation of factual reliability, safety, tone stability, and prompt-specific robustness.Results reveal clear behavioral differences across models.DeepSeek and GPT-4.1-nanoachieve the strongest factual consistency and safer responses, whereas LLaMA is more susceptible to prompt-induced drift and Gemini exhibits more conservative refusal behavior but lower overall robustness.These findings demonstrate the value of structured multi-dimensional evaluation for identifying failure modes and supporting the deployment of reliable, misinformation-aware LLMs in healthcare.

**Решение:** -4 фактчекинг и робастность медицинской информации

---

### 64 · R7300

**SAGE**

2025 · Zenodo · conferencepaper/ · https://doi.org/10.5281/zenodo.14968914

SAGE A Context-aware Hybrid Approach to Mining Privacy Concerns from Mental Health App Reviews Introduction This repository includes all the materials (code, input data, evaluation results, output dataset) of our approach to extracting privacy concerns from mental health app reviews. These materials involve quantitative and qualitative analysis of SAGE. File Descriptions There are three directories in total, and the content of each directory is described as follows: `datafiles`: the input data used for this study. - `labeled_reviews.csv` is the ground truth dataset containing privacy or not-privacy labeled app reviews from the mental health domain. - `unlabeled_reviews.csv` is the unlabeled dataset containing 1 and 2-star rated app reviews from the mental health domain. We use this dataset to extract new privacy-related app reviews. - `sage_classified_reviews.csv` is the dataset extracted using our proposed Sage approach. `docs`: additional supporting documents for our study. - `evaluation_results.md` contains the results of our manual inspection process followed to create new gold-standard dataset of privacy-related app reviews. - `manual_label_guide.md` contains the instructions followed by the annotators for manual inspection. `programfiles`: the source code of our study. - `nli_inference_test.py` contains the code for NLI inference and evaluation. We perform the NLI inference using the `DeBERTa-V3` base model and evaluate 3 different sets of heuristics to select the best one without any bias. - `sage_evaluation.py` contains the code for complete Sage implementation and evaluation using domain-specific hypotheses and the GPT model. - `sage_unlabeled_data.py` contains the code to extract new privacy reviews (qualitative evaluation) from the unlabeled dataset using Sage. - `data_preprocess.py` contains the data pre-processing code used to clean the data before extracting privacy reviews. - `generic_hypotheses` contains the implementation of baseline generic hypotheses with Sage. - `bert.py` contains the implementation of baseline `BERT` classifier. - `svm.py` contains the implementation of baseline `SVM` classifier. - `t5.py` contains the implementation of the baseline `T5` classifier. - `standalone_gpt.py` contains the implementation of the baseline `Standalone GPT` model. `new_privacy_reviews.csv` is the manually curated dataset containing 1,008 privacy-related app reviews after using Sage on a dataset of 42,271 app reviews. `supplementary_material.pdf` provides supporting material for the paper.

**Решение:** -4 выявление опасений о конфиденциальности в отзывах о приложениях mental health

---

### 65 · R9398

**The Language-Based Assessment Model (L-BAM) Library: Open Model Sharing for Independent Validation and Broader Applications**

2025 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/n8rza_v1

Language-based assessments (LBAs), quantitative estimates of scientific constructs based on language, have advanced methods in the psychological and social sciences for over a decade. LBAs based on individuals’ prompted descriptions analysed with large language models to produce scores of their psychological states and traits have shown strong convergence with the corresponding rating scales (r &gt; .80) and have often surpassed rating scales in predicting theoretically relevant behaviours (external criteria). Despite their high validity across numerous psychological outcomes and contexts, the broader adoption of LBA models has been limited. Even when made available alongside research publications, these models often remain inaccessible due to technical complexities, inconsistent documentation, and the absence of a standardized repository. This tutorial introduces a framework targeted to social and psychological scientists for accessible sharing models with others –the Language-Based Assessment Models (L-BAM) Library– as well as a toolkit for easily using L–BAMs via the text package in R. L-BAM covers a wide range of models for assessing mental health disorders (e.g., depression, anxiety), well-being (e.g., satisfaction with life, harmony in life), implicit motives (need for power, affiliation and achievement) and more. The L-BAM library aims to increase the availability and resource efficiency of language-based assessments of psychological constructs while encouraging replication, independent validation and the broad application of pre-existing language-based assessment models.

**Решение:** ? фреймворк/туториал L-BAM для языковой психодиагностики; проверить данные согласия в полном тексте

---

### 66 · R6201

**Securing LLM Agents Need Intent-to-Execution Integrity**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.16976

This position paper argues that securing LLM agents requires first defining an end-to-end correctness property that specifies when an agent's execution faithfully reflects the user's intent. Modern LLM agents operate over an \emph{intent-to-execution pipeline}, where natural-language instructions are translated into concrete system operations such as tool calls, API requests, and code execution. While recent defenses have made progress in constraining how agents construct tool calls, most existing formulations implicitly assume that tools are trusted. The emergence of systems such as OpenClaw, with open ecosystems of third-party skills and direct access to user environments, breaks this assumption and exposes new failure modes, including malicious or over-privileged components in the execution pipeline. Despite rapid progress in defense mechanisms, there is no adequate correctness property that defines what ``secure'' means for LLM agents, nor a principled way to evaluate the coverage of existing defenses. We observe that LLM agents are structurally analogous to compilers, where security violations correspond to mis-executions that do not preserve user intent. Drawing on this analogy, we identify two fundamental problem sources -- untrusted data ingestion and untrusted tool execution -- and derive four integrity properties that must hold simultaneously: \emph{Tool Integrity}, \emph{Instruction Integrity}, \emph{Judgment Integrity}, and \emph{Data Flow Integrity}. We call their conjunction \emph{intent-to-execution integrity}. Analyzing existing agentic defenses against these properties reveals that current systems provide only partial and non-compositional coverage, leaving fundamental gaps in securing modern LLM agents.

**Решение:** -1 концептуальная статья по безопасности LLM-агентов

---

### 67 · R10739

**DMRL: Data- and Model-aware Reward Learning for Data Extraction**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2505.06284

Large language models (LLMs) are inherently vulnerable to unintended privacy breaches. Consequently, systematic red-teaming research is essential for developing robust defense mechanisms. However, current data extraction methods suffer from several limitations: (1) rely on dataset duplicates (addressable via deduplication), (2) depend on prompt engineering (now countered by detection and defense), and (3) rely on random-search adversarial generation. To address these challenges, we propose DMRL, a Data- and Model-aware Reward Learning approach for data extraction. This technique leverages inverse reinforcement learning to extract sensitive data from LLMs. Our method consists of two main components: (1) constructing an introspective reasoning dataset that captures leakage mindsets to guide model behavior, and (2) training reward models with Group Relative Policy Optimization (GRPO), dynamically tuning optimization based on task difficulty at both the data and model levels. Comprehensive experiments across various LLMs demonstrate that DMRL outperforms all baseline methods in data extraction performance. Data- and Model-aware Reward Learning for Data Extraction. arXiv admin note: substantial text overlap with arXiv:2503.18991

**Решение:** -4 атаки извлечения данных из LLM, кибербезопасность

---

### 68 · R5722

**SoCRATES: Towards Reliable Automated Evaluation of Proactive LLM Mediation across Domains and Socio-cognitive Variations**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.05563

Evaluating LLM mediators remains challenging, as mediation unfolds as a real-time trajectory shaped by disputants' shifting emotions, intentions, and context. Existing testbeds rely on a few expert-authored domains, vary mainly strategic posture, and score every turn against every topic, introducing off-topic noise. We introduce SoCRATES, a benchmark for evaluating proactive LLM mediators in realistic, multi-domain testbeds. It constructs scenarios from real conflicts through an agentic pipeline across eight domains, probes five socio-cognitive adaptation axes (strategic posture, party composition, history length, emotional reactivity, and cultural identity), and scores each topic only on the turns that advance it via a topic-localized evaluator. The evaluator reaches 0.82 alignment with human experts, more than doubling a per-turn baseline. Benchmarking eight frontier LLMs, we find that even the strongest mediator closes only about a third of the unmediated consensus gap under diverse and realistic testbeds, with performance varying sharply by socio-cognitive axis, highlighting that progress lies in social adaptation to diverse conditions.

**Решение:** ? T4 SoCRATES: LLM-судья диалогов медиации конфликтов, согласие 0.82 с экспертами; проверить соответствие T4

---

### 69 · R0774

**P2P - from Posts to Patterns: An LLM Ensemble Approach to Mental Health Dynamics Detection**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/dts3-fg54

The automatic detection of mental health dy- namics represents a challenging and socially relevant task, requiring models to capture sub- tle psychological changes over time. Large language models have demonstrated remark- able capabilities in clinical and diagnostic con- texts, yet their outputs often lack consistency and may diverge significantly across different model families and prompting strategies. This paper presents the USAI team’s submission to the CLPsych 2026 Shared Task, targeting Tasks 1.1, 1.2, 2, and 3.1. We propose an ensemble-based approach combining multiple open-source large language models, where the contribution of each model is weighted accord- ing to its alignment with clinically grounded human annotations on the training set. Our system achieves competitive results across the evaluated subtasks, with particularly strong per- formance on Tasks 1.2 and 2.

**Решение:** + T3/T1 CLPsych 2026: выявление динамики психического здоровья ансамблем LLM против клинической разметки людей

---

### 70 · R7771

**Leveraging large language models for thematic analysis: a case study in the charity sector**

2025 · AI & Society · journalarticle, article · en · https://doi.org/10.1007/s00146-025-02487-4

Abstract This study explores how large language models (LLMs) can support deductive and inductive thematic coding in real-life contexts, balancing AI-driven efficiency with essential human oversight. Using three datasets from Tearfund, a UK-based Christian charity, we propose a dual-role human–LLM collaborative framework where the LLM functions as an initial annotator and a validator. In the deductive phase, GPT-4o and GPT-4o-mini were compared against human coders. GPT-4o achieved a substantial agreement in multi-label thematic categorization (κ = 0.61–0.65), while GPT-4o-mini showed a moderate agreement (κ = 0.41–0.58). Both models excelled in sentiment analysis (κ = 0.91–0.95), but struggled with evaluating evidence of impact due to contextual complexity (κ ≤ 0.01). GPT-4o-mini exhibited greater output variability and instability than GPT-4o, but benefited more from few-shot learning to mitigate hallucinations. In the inductive phase, GPT-4o demonstrated a strong semantic alignment with human-generated themes (cosine similarity = 0.76–0.79) though its tendency toward broad themes required human refinement. Despite their potential to streamline thematic analysis, LLMs also pose limitations and implementation challenges, including inconsistencies in excerpt extraction (precision = 0.41, recall = 0.53) and the trade-off between the time saved in coding and the time required for human validation. To facilitate practical implementation, we provide reusable prompt templates for four stages: context, instructions, data processing, and verification. Our findings underline the indispensable role of human expertise—from prompt engineering and managing hallucinations to final verification—to ensure accurate and trustworthy AI-assisted analyses. While LLMs can enhance qualitative analysis, their full potential is only realized under skilled human guidance.

**Решение:** -4 тематический анализ данных благотворительной организации Tearfund

---

### 71 · R4946

**RPA-Check: A Multi-Stage Automated Framework for Evaluating Dynamic LLM-based Role-Playing Agents**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.2139/ssrn.6756301

The rapid adoption of Large Language Models (LLMs) in interactive systems has enabled the creation of dynamic, open-ended Role-Playing Agents (RPAs). However, evaluating these agents remains a significant challenge, as standard NLP metrics fail to capture the nuances of role adherence, logical consistency, and long-term narrative stability. This paper introduces RPA-Check, a multi-stage automated evaluation framework designed to objectively assess the performance of LLM-based RPAs in complex, constraints-heavy environments. Our methodology is based on a four-step pipeline: (1) Dimension Definition, establishing high-level qualitative behavioral criteria; (2) Augmentation, where these requirements are expanded into granular boolean checklist indicators; (3) Semantic Filtering, to ensure indicator objectivity, no redundancy and agent isolation; and (4) LLM-as-a-Judge Evaluation, which employs chain-of-thought verification to score agent fidelity. We validate this framework by applying it to LLM Court, a serious game for forensic training involving several quantized local models. Experimental results across five distinct legal scenarios demonstrate the framework's ability to identify subtle trade-offs between model size, reasoning depth, and operational stability. Notably, the findings reveal an inverse relationship between parametric scale and procedural consistency, showing that smaller, adequately instruction-tuned models (8-9B) can outperform larger architectures prone to user-alignment bias or sycophancy. RPA-Check thus provides a standardized and reproducible metric for future research in generative agent evaluation within specialized domains.

**Решение:** -4 оценка ролевых агентов в судебных симуляциях (LLM Court)

---

### 72 · R11695

**Research Letter: Characterizing spin in psychiatric clinical research literature using large language models.**

2024 · medRxiv : the preprint server for health sciences · journal article, preprint, journalarticle · eng · https://doi.org/10.1101/2024.06.30.24309737

Importance: Spin is a common form of biased reporting that misrepresents study results in publications as more positive than an objective assessment would indicate, but its prevalence in psychiatric journals is unknown. Objective: To apply a large language model to characterize the extent to which original reports of pharmacologic and non-pharmacologic interventions in psychiatric journals reflect spin. Design: We identified abstracts from studies published between 2013 and 2023 in 3 high-impact psychiatric journals describing randomized trials or meta-analyses of interventions. Main Outcome and Measure: Presence or absence of spin estimated by a large language model (GPT4 turbo, turbo2024 04 09), validated using gold standard abstracts with and without spin. Results: Among a total of 663 abstracts, 296 (44.6%) exhibited possible or probable spin, including 230/529 (43.5%) randomized trials, 66/134 (49.3%) meta-analyses; 148/310 (47.7%) for medication, 107/238 (45.0%) for psychotherapy, and 41/115 (35.7%) for other interventions. In a multivariable logistic regression model, reports of randomized trials, and non-pharmacologic/non-psychotherapy interventions, were less likely to exhibit spin, as were more recent publications Conclusions and Relevance: A substantial subset of psychiatric intervention abstracts in high-impact journals may contain results presented in a potentially misleading way, with the potential to impact clinical practice. The success in automating spin detection via large language models may facilitate identification and revision to minimize spin in future publications.

**Решение:** -6 выявление спина в статьях по психиатрии (мета-исследование/скрининг литературы)

---

### 73 · R2652

**Generative Artificial Intelligence as a Psychological Intervention: Between Illusion and Risk.**

2026 · Journal of medical systems · journal article, med, article · eng · https://doi.org/10.1007/s10916-026-02381-6

Generative AI is rapidly reshaping how people seek emotional and psychological support. Millions now turn to large language model (LLM)-based chatbots for advice, consolation, and interactions that may feel surprisingly “therapeutic.” Yet these systems are not clinicians, and many operate outside established clinical, ethical, and legal oversight frameworks, without the capacity to assess risk, exercise professional judgment, or manage crises. Importantly, the risks posed by these tools are not uniform; they vary according to user vulnerability, deployment context, degree of human oversight, and the presence or absence of safeguards. While some low-risk, bounded applications may have a supportive role, greater concern arises in therapy-adjacent consumer settings, where engagement-optimized systems may mirror cognitive distortions, validate delusional beliefs, or respond inadequately to suicidality. In contrast to regulated psychotherapy, characteristic failure modes of commercial emotional support chatbots include uncritical agreement (sycophancy), deceptive empathy, crisis mismanagement, and privacy and security risks. This commentary examines these distinctions, situates consumer tools within a broader spectrum of AI-enabled mental health applications, and outlines minimum safeguards needed when such systems are used—or marketed—as psychological interventions.

**Решение:** -1 эссе / концептуальный анализ рисков применения ИИ в качестве психотерапии

---

### 74 · R8321

**Comment on “A positive spin: large language models can help directors evaluate programs through their patients' own words”**

2025 · PAIN Reports · article · en · https://doi.org/10.1097/pr9.0000000000001351

We would like to comment on the publication on “A positive spin: large language models can help directors evaluate programs through their patients' own words.”1 This study looked into the ability of large language models (LLMs) like ChatGPT to interpret qualitative remarks from participants in a pain education program. The study used both LLM-based and manual theme review methodologies to illustrate the viability of using LLMs to assess patient responses. Although the use of LLMs for qualitative research is a promising advance, some areas need to be explored further. First, although the thematic analysis found 7 major motifs, it does not detail how the LLMs were trained or calibrated to accomplish this task efficiently. Large language models are inevitably influenced by the data used for training, and ChatGPT may struggle with context-specific language or delicate patient interactions. For example, patient reactions during pain education may have complicated emotional connotations and cultural connections that LLMs might not completely get. How did the authors guarantee that the LLMs were calibrated correctly for this domain, and what procedures did they take to minimize potential bias and misunderstanding? Second, despite the study's reference to a “dual analysis methodology,” there is no information about the procedure and criteria for comparing the outcomes of the LLM-based and manual analyses. How did theme reviewers manually go through the results generated by ChatGPT? Were there any major differences between the 2 methods? If so, how did they get adjusted? Interrater reliability between LLM and human reviewers is a crucial consideration that should be thoroughly explained to demonstrate the robustness of the findings. Regarding innovation, this study presents a fresh technique to accelerating qualitative analysis with LLM, which is especially relevant in large-scale investigations and resource-constrained contexts. However, future research might look into the unique benefits and drawbacks of LLM against classic qualitative approaches such in-depth interviews and self-coding. One promising option is to improve LLM to detect more subtle patterns, such as emotional tone and patient motivation, to boost the depth of qualitative insights. In the future, incorporating LLM into clinical and research contexts may enable more scalable and efficient processing of patient feedback, allowing for real-time modifications to therapy and program delivery. However, future study should take into account ethical concerns, such as data privacy and potential algorithmic prejudice. Further study will look into ways to train LLM on a variety of patient-specific datasets to boost sensitivity to individual characteristics and make it a more dependable and empathetic tool in health care. Disclosures The authors have no conflict of interest to declare.

**Решение:** -1 комментарий / письмо в редакцию

---

### 75 · R8294

**Generative AI in Virtual Reality Communities: A Preliminary Analysis of the VRChat Discord Community**

2025 · CHI Extended Abstracts · journalarticle, book · https://doi.org/10.1145/3706599.3720120

As immersive social platforms like VRChat increasingly adopt generative AI (GenAI) technologies, it becomes critical to understand how community members perceive, negotiate, and utilize these tools. In this preliminary study, we conducted a qualitative analysis of VRChat-related Discord discussions, employing a deductive coding framework to identify key themes related to AI-assisted content creation, intellectual property disputes, and evolving community norms. Our findings offer preliminary insights into the complex interplay between the community’s enthusiasm for AI-driven creativity and deep-rooted ethical and legal concerns. Users weigh issues of fair use, data ethics, intellectual property, and the role of community governance in establishing trust. By highlighting the tensions and trade-offs as users embrace new creative opportunities while seeking transparency, fair attribution, and equitable policies, this research offers valuable insights for designers, platform administrators, and policymakers aiming to foster responsible, inclusive, and ethically sound AI integration in future immersive virtual environments.

**Решение:** -4 социологическое исследование взаимодействий в VRChat

---

### 76 · R8650

**Automated Formative Assessment With Large Language Models: Design, Validation, and Empirical Application in Higher Education**

2025 · Journal of Higher Education Theory and Practice · journalarticle, article · https://doi.org/10.33423/jhetp.v25i6.8016

This study presents the design and validation of a formative assessment system that automatically grades and provides feedback on open-ended responses in higher education using large language models (LLMs). Implemented locally through the Ollama platform with a customized course corpus, it generates an “ideal response” based on instructor criteria and evaluates student answers accordingly. Semantic filters and sequential tolerance thresholds ensure alignment between AI and human grading. A dataset of 450 exams (2022–2025) from three technical courses was used, with 360 for model optimization and 90 for validation. Performance metrics included mean difference, Pearson correlation, intraclass correlation coefficient (ICC), and Bland–Altman analysis. Results showed strong agreement (mean absolute difference = 4.5/100, r > 0.95, ICC ≈ 0.95) and negligible bias (±8/100). The system generated detailed, pedagogically coherent feedback and effectively filtered irrelevant or ambiguous responses. Overall, it provided accurate and consistent assessment, greatly reducing grading time and enhancing formative learning while preserving instructor oversight.

**Решение:** -4 автоматическая оценка вузовских экзаменационных ответов по техническим дисциплинам

---

### 77 · R1252

**Distinguishing cancer patients' mild and severe symptoms in radiotherapy via zero-shot and few-shot large language model-based probabilistic prompts.**

2026 · BioData mining · journal article, journalarticle, article · eng · https://doi.org/10.1186/s13040-026-00547-z

PURPOSE: Monitoring symptom severity during and after radiotherapy (RT) is critical for cancer patient care, however, existing machine learning and deep learning approaches face high retraining costs and lack clinically acceptable explanations. This study aims to investigate effective prompts for LLM-based reasoning and decision-making, distinguishing cancer patients’ mild and severe status during and after radiotherapy across multiple health symptoms. METHODS: To overcome these limitations, we developed a set of few-shot Large Language Model (LLM)-based predictive models operating under an anomaly detection framework (AD-LLM). Our approach leverages six novel, probabilistically designed prompts tailored for AD-LLM to identify and track patients with mild or severe symptoms, enabling accurate prediction despite limited patient-specific data. RESULTS: Experiments on prostate cancer patients monitoring bowel pain, depression, and sexual dysfunction problems demonstrated AD-LLM’s effectiveness in classifying symptom severity levels using these structured prompts. We evaluate the performance of different prompt strategies using AUC, AUCPR, Precision, Recall, and F1 scores, with confusion matrices and ROC/PR curves visualized to offer insights into LLM reasoning. The reasoning examples of LLMs are also provided to explain and understand their decision-making process. CONCLUSION: This method provides a promising and explainable solution for real-time symptom monitoring in RT settings, potentially improving timely intervention and patient outcomes.

**Решение:** ? T3 оценка тяжести симптомов у онкопациентов, включая депрессию; проверить тип данных и эталон в полном тексте

---

### 78 · R0163

**Large Language Models for Intelligent Code Generation in Software Engineering: A Systematic Review and Future Research Directions**

2026 · Asian Journal of Engineering Social and Health · journalarticle, review · https://doi.org/10.46799/ajesh.v5i6.779

The proliferation of Large Language Models has catalyzed a paradigm shift in software engineering automation, yet existing literature reviews predominantly evaluate functional correctness while systematically neglecting security posture, maintainability, and multi-language deployment contexts. This study addresses the critical research gap regarding the absence of unified, multi-dimensional assessment protocols for LLM-generated code in production environments. Through a PRISMA-guided systematic review of 87 primary studies published between 2020 and 2025, this research examined architectural evolution, evaluation methodologies, and deployment barriers using a dual-phase qualitative and quantitative synthesis supported by a custom quality assessment framework. A five-criterion evaluation instrument was applied to ensure methodological rigor, with strong inter-rater reliability (Cohen’s kappa = 0.84). The findings reveal that decoder-only transformer architectures have achieved dominant performance on generative benchmarks, with Claude-3 Opus attaining 74.9% Pass@1 on HumanEval. However, only 12% of evaluated studies incorporated security metrics, fewer than 8% assessed maintainability, and benchmark contamination threatens the validity of reported generalization. The novelty of this work lies in proposing a unified evaluation framework that integrates functional correctness, Common Weakness Enumeration vulnerability scanning, and maintainability metrics, alongside a standardized multi-language protocol. The implications suggest that enterprise DevSecOps pipelines must embed static security analysis and cross-language quality gates before production integration. Future research should prioritize runtime verification, longitudinal productivity studies, and contamination-free benchmarks to ensure trustworthy deployment of generative AI in mission-critical software ecosystems.

**Решение:** -4 генерация программного кода в программной инженерии

---

### 79 · R0883

**ChatGPT as a source of surgical information: Evaluation of responses to patient questions on hallux rigidus fusion.**

2026 · Digital health · journal article, journalarticle, article · eng · https://doi.org/10.1177/20552076261481386

Background Patients are increasingly turning to online resources and artificial intelligence (AI)-based tools to obtain information about orthopedic conditions and surgical options. Large language models, such as ChatGPT, are becoming prominent in patient education; however, their reliability and readability remain uncertain. This study evaluated the quality and readability of responses generated by ChatGPT-4o and ChatGPT-5 to frequently asked patient questions regarding hallux rigidus fusion surgery. Methods Twenty commonly asked patient questions were compiled and presented to ChatGPT-4o and ChatGPT-5. Readability was assessed using the Flesch–Kincaid Grade Level, Gunning Fog, Coleman–Liau, and Simple Measure of Gobbledygook indices. Quality was evaluated with the DISCERN tool, response accuracy scores, and Journal of the American Medical Association (JAMA) criteria. Interrater agreement was measured using the Intraclass Correlation Coefficient (ICC). Results ChatGPT-4o generated longer responses (802 vs. 242 words; p&lt;0.001) with slightly higher readability grade levels (10.81 vs. 10.37; p=0.031). Accuracy (2.00 vs. 1.85; p=0.323) and DISCERN scores (49.35 vs. 48.93; p=0.747) showed no significant differences. All responses received a JAMA score of 0 due to the absence of citations, authorship, or transparency indicators. Interrater reliability indicated moderate to good agreement (ICC: 0.68–0.80). Conclusion ChatGPT-4o and ChatGPT-5 provide generally satisfactory yet non-comprehensive, limited-quality information at a level above tenth-grade regarding hallux rigidus fusion surgery. Although linguistically coherent, responses lack evidence-based detail and individualized guidance. These models may supplement, but cannot replace, expert orthopedic counseling. Ensuring physician oversight and integrating validated, updated clinical content remain essential for safe implementation of AI-generated patient information. </jats:sec

**Решение:** -2 хирурги оценивают точность ответов ChatGPT о хирургических вмешательствах

---

### 80 · R5517

**Affective Misgrounding in Aligned Language Models: A Quantitative Analysis of Emotional Hallucination in LLM Responses**

2026 · Research Square · preprint · https://doi.org/10.21203/rs.3.rs-9583845/v1

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? эмоциональные галлюцинации LLM, нет аннотации — проверить дизайн в полном тексте

---

### 81 · R0029

**Elyssa: A multi-modal framework integrating facial emotion recognition and fine-tuned language models for accessible mental health support**

2026 · Array · article · en · https://doi.org/10.1016/j.array.2026.101277

The growing disparity between mental healthcare demand and availability indicates a need for artificial intelligence-driven support. Existing text-based conversational models often overlook emotional cues conveyed through facial expressions. This paper presents Elyssa, a multi-modal framework combining real-time facial emotion recognition (FER) with a fine-tuned conversational language model and a keyword-based crisis-detection mechanism. The FER module adapts Llama-3.2-11B-Vision-Instruct via Low-Rank Adaptation (LoRA) on the 9400-image Tukey Human Emotion Dataset across eight categories. The conversational component fine-tunes Llama-3.2-3B on MentalChat16K, comprising 16,084 therapeutic dialogues. During inference, the FER-detected emotion label is injected into the conversational prompt, conditioning responses on both textual input and non-verbal affect. Evaluated on 1880 test images, the FER module achieves 72.7% accuracy and a 0.73 macro-F1 score. Evaluation of the conversational module on 3217 test records shows an 8.2% ROUGE-F1 improvement over the base model. Complementary LLM-as-Judge evaluation using GPT-4o demonstrates a 24.1% improvement in overall response quality, increasing from 2.74 to 3.40 out of 5.00, across empathy, safety, and helpfulness. An ablation study confirms that emotion conditioning provides additive benefits. Furthermore, the safety mechanism achieves an F1 score of 0.86 for crisis detection, operating with a 0.09% false-positive rate, and multi-seed experiments across five seeds confirm metric stability. With an end-to-end inference latency of 2.3 s on an NVIDIA A100 GPU, Elyssa establishes a functional proof of concept for emotion-aware conversational mental health support, identifying necessary clinical validation steps prior to deployment.

**Решение:** -5 чат-бот Elyssa оценен исключительно через GPT-4o-as-a-judge без людей

---

### 82 · R3571

**AI-powered methods for psychological assessment in adolescence psychological disorders: A systematic review and meta-analysis.**

2026 · Clinical psychology review · journal article, systematic review, meta-analysis · eng · https://doi.org/10.1016/j.cpr.2026.102728

Artificial intelligence (AI)-powered assessment, with its ability to process multimodal data and support real-time evaluation, is transforming traditional psychological assessment. However, the predictive performance of AI-powered assessments, such as the area under the curves (AUCs), and their clinical applicability remain unclear. Adolescence, marked by heightened neuroplasticity and psychological vulnerability, demands more precise approaches to assessment and intervention to promote mental health. This review developed a multimodal assessment framework that integrates both modality type and disorder type, and conducted a large language model (LLM) assisted meta-analysis in adolescent populations. Eight databases were systematically searched from inception to December 12, 2025. Studies that used AI-powered assessments of adolescent mental outcomes were included. A total of 188 studies involving 4,794,001 participants (aged 10-19 years) met the inclusion criteria. In the meta-analysis, we included studies that determined mental health outcomes using gold-standard assessments (e.g., clinical interviews) or self-reported behavioral indices (k = 154). The mean AUCs ranged from 0.75 to 0.85 under internal validation (performance tested within the same dataset used for model development) and 0.76 to 0.96 under external validation (performance tested in a new, independent dataset) across various mental health outcomes, indicating good discrimination. Subgroup analyses showed that multi-modal achieved higher AUCs than single-modality models for depression and suicide. AI holds promise for adolescent mental health assessment, with performance varying by data modality and mental health outcome. These findings may inform the development of AI-driven clinical decision support systems. However, integration into routine care requires staged, externally validated, and reciprocal clinical transition approaches that align with real-world clinical workflows. It is also essential to enhance clinical interpretability, deployment, ethical governance, and cultural adaptation to ensure equitable access to mental health resources.

**Решение:** -1 систематический обзор и метаанализ методов оценки психических расстройств у подростков

---

### 83 · R10151

**Exploring Jailbreak Attacks on LLMs through Intent Concealment and Diversion**

2025 · Annual Meeting of the Association for Computational Linguistics · journalarticle, conference, preprint/article · https://doi.org/10.48550/arxiv.2505.14316

Although large language models (LLMs) have achieved remarkable advancements, their security remains a pressing concern. One major threat is jailbreak attacks, where adversarial prompts bypass model safeguards to generate harmful or objectionable content. Researchers study jailbreak attacks to understand security and robustness of LLMs. However, existing jailbreak attack methods face two main challenges: (1) an excessive number of iterative queries, and (2) poor generalization across models. In addition, recent jailbreak evaluation datasets focus primarily on question-answering scenarios, lacking attention to text generation tasks that require accurate regeneration of toxic content. To tackle these challenges, we propose two contributions: (1) ICE, a novel black-box jailbreak method that employs Intent Concealment and divErsion to effectively circumvent security constraints. ICE achieves high attack success rates (ASR) with a single query, significantly improving efficiency and transferability across different models. (2) BiSceneEval, a comprehensive dataset designed for assessing LLM robustness in question-answering and text-generation tasks. Experimental results demonstrate that ICE outperforms existing jailbreak techniques, revealing critical vulnerabilities in current defense mechanisms. Our findings underscore the necessity of a hybrid security strategy that integrates predefined security mechanisms with real-time semantic decomposition to enhance the security of LLMs.

**Решение:** -4 исследование сокрытия намерений при джейлбрейках LLM, кибербезопасность

---

### 84 · R1738

**AI-Powered Phishing in the Era of Generative AI: Emerging Risks, Business Impact, and Organizational Defense Strategies**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.21408765

Artificial Intelligence (AI) is reshaping cybersecurity by enabling both cyber defense and cyber offense. Phishing, one of the oldest cyber threats, has evolved dramatically through Generative AI and Large Language Models (LLMs), which allow attackers to craft personalized, grammatically correct, and context-aware phishing content at scale. AI-powered phishing increases the risk of credential theft, financial fraud, Business Email Compromise (BEC), ransomware, and data breaches, while conventional detection techniques struggle to keep pace. This study examines the evolution of phishing attacks, the role of Generative AI in cybercrime, the business impact of AI-driven attacks on organizations, and existing defense mechanisms, using a qualitative methodology based on secondary data. The findings show that AI has amplified attacker capabilities while simultaneously equipping organizations with powerful tools for threat detection, behavioral analysis, automated incident response, and predictive security. The study proposes the AI-SHIELD Framework, an integrated model combining AI-based detection, employee awareness, identity management, governance, incident response, and continuous monitoring. The research concludes that a proactive, AI-enabled, and governance-driven cybersecurity strategy is essential for organizations to withstand the next generation of phishing threats.

**Решение:** -4 фишинг с применением генеративного ИИ, кибербезопасность

---

### 85 · R9541

**Accuracy and Consistency of Gemini Responses Regarding the Management of Traumatized Permanent Teeth.**

2025 · Dental traumatology : official publication of International Association for Dental Traumatology · journal article, observational study, med · eng · https://doi.org/10.1111/edt.13004

BACKGROUND: The aim of this cross-sectional observational analytical study was to assess the accuracy and consistency of responses provided by Google Gemini (GG), a free-access high-performance multimodal large language model, to questions related to the European Society of Endodontology position statement on the management of traumatized permanent teeth (MTPT). MATERIALS AND METHODS: Three academic endodontists developed a set of 99 yes/no questions covering all areas of the MTPT. Nine general dentists and 22 endodontic specialists evaluated these questions for clarity and comprehension through an iterative process. Two academic dental trauma experts categorized the knowledge required to answer each question into three levels. The three academic endodontists submitted the 99 questions to the GG, resulting in 297 responses, which were then assessed for accuracy and consistency. Accuracy was evaluated using the Wald binomial method, while the consistency of GG responses was assessed using the kappa-Fleiss coefficient with a confidence interval of 95%. A 5% significance level chi-squared test was used to evaluate the influence of question level of knowledge on accuracy and consistency. RESULTS: The responses generated by Gemini showed an overall moderate accuracy of 80.81%, with no significant differences found between the responses of the academic endodontists. Overall, high consistency (95.96%) was demonstrated, with no significant differences between GG responses across the three accounts. The analysis also revealed no correlation between question level of knowledge and accuracy or consistency, with no significant differences. CONCLUSIONS: The results of this study could significantly impact the potential use of Gemini as a free-access source of information for clinicians in the MTPT.

**Решение:** -2 оценка врачами качества и точности ответов Gemini по медицине

---

### 86 · R5480

**STEB: A Speech-to-Speech Translation Expressiveness Benchmark for Evaluating Beyond Translation Fidelity**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.25529

Speech-to-speech translation (S2ST) should preserve not only lexical meaning, but also expressive attributes: emotion, scenario style (e.g., news reporting vs. dramatic dialogue), and nonverbal vocalizations (NVs). Moreover, collecting cross-lingual target speech that is both translation-faithful and expressively aligned with the source is difficult at scale, making reference-based evaluation impractical. We introduce STEB (Speech-to-Speech Translation Expressiveness Benchmark), a 32.6-hour Chinese--English benchmark that evaluates both standard dimensions (translation fidelity, speaker similarity, duration alignment) and expressiveness dimensions (emotion, scenario style, NV preservation). For expressiveness evaluation, STEB uses a caption-then-summarize framework that converts speech into structured expressive attributes and compares source and hypothesis attributes with an LLM judge. Human validation shows statistically significant correlations with listener judgments across all expressive dimensions. We evaluate six S2ST systems covering cascaded systems, end-to-end models, and speech large language models. Many systems, especially cascaded ones, achieve strong translation fidelity, but they still struggle with emotion preservation (best: 3.82/5) and NV preservation (best: 2.31/5). These results reveal a gap between semantic transfer and expressive transfer, identifying expressiveness preservation as an open challenge for S2ST. Audio samples are available at https://cmots.github.io/steb.github.io/.

**Решение:** -4 бенчмарк экспрессивности машинного перевода речи (S2ST)

---

### 87 · R11529

**Examining the Idea Density and Semantic Distance of Responses Given by AI to Tests of Divergent Thinking**

2024 · The Journal of Creative Behavior · journalarticle, article · en · https://doi.org/10.1002/jocb.1528

ABSTRACT Research suggests that generative AI (GAI) responds to divergent thinking (DT) prompts with multiple ideas, some of which seem to be original. The present investigation administered 55 DT tasks to three GAI services (Bard, GPT 3.5, and GPT 4.0). Instead of examining individual responses, an Idea Density algorithm was used to assess the output. This algorithm quantifies the ideas within responses, controlling for the number of words. A subset of the DT tests administered to the GAI were also scored for Semantic Distance, which estimates originality. Results indicated that the three GAI models differed in the Idea Density of the output. There were also significant differences between Realistic and Nonrealistic DT tasks. As has been the case in human samples, directions given when the GAI received the prompts also had a significant impact, with more Idea Density following directions that explicitly prompted original responses. Adjusted scores removed all verbiage in the output, which did not actually address the questions conveyed by the prompts. These corrected scores shared approximately 50% of the variance with the uncorrected “raw” responses, implying that the typical output of GAI is not always relevant. This was interpreted in the context of the standard definition of creativity, which emphasizes effectiveness, as well as originality.

**Решение:** -2 плотность идей: LLM в роли тестируемого в тестах дивергентного мышления

---

### 88 · R11483

**Beyond the Buzz: A Systematic Review of Generative AI’s Capabilities in Mental Health (Preprint)**

2024 · preprint · en · https://doi.org/10.2196/preprints.70014

BACKGROUND The global shortage of mental health professionals, exacerbated by increasing mental health needs post-COVID-19, has driven interest in leveraging large language models (LLMs) like ChatGPT to address these challenges through applications such as clinical note generation, personalized treatment planning, and therapeutic support. OBJECTIVE This systematic review aims to evaluate the current capabilities of generative AI (genAI) models in the context of mental health applications. METHODS A comprehensive search across five databases yielded 1,046 references, of which eight studies met the inclusion criteria. These criteria required original research with experimental designs (e.g., Turing tests, socio-cognitive tasks, trials, or qualitative methods), a focus on genAI models, and explicit measurement of socio-cognitive abilities (e.g., empathy, emotional awareness), mental health outcomes, and user experience (e.g., perceived trust, empathy). RESULTS The studies, published between 2023 and 2024, primarily evaluated models like ChatGPT 3.5 and 4.0, Bard, and Claude in tasks such as psychoeducation, diagnosis, emotional awareness, and clinical interventions. Most studies employed zero-shot prompting and human evaluators to assess the AI responses, using standardized rating scales or qualitative analysis. However, these methods were often insufficient to fully capture the complexity of genAI capabilities. The reliance on single-shot evaluation techniques, limited comparisons, and task-based assessments isolated from a specific context may oversimplify genAI’s abilities and overlook the nuances of human-AI interaction, especially in areas requiring contextual reasoning or cultural sensitivity. The findings suggest that while genAI models demonstrate strengths in psychoeducation and emotional awareness, their diagnostic accuracy, cultural competence, and ability to engage users emotionally remain limited. Users frequently reported concerns about trustworthiness, accuracy, and the lack of emotional engagement. CONCLUSIONS Future research could use more sophisticated evaluation methods, such as few-shot and chain-of-thought prompting to fully uncover genAI’s potential. Future studies should also focus on longitudinal research, broader comparisons with human benchmarks, and exploring how AI can be better integrated into mental health care with improved socio-cognitive and ethical decision-making capabilities.

**Решение:** -1 систематический обзор возможностей генеративного ИИ в психическом здоровье

---

### 89 · R0860

**Evaluating LLMs for Causal Extraction from Transcribed Hindi Agricultural Data**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-18477-1_51

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 извлечение причинно-следственных связей из сельскохозяйственных текстов

---

### 90 · R4506

**AI Psychosis: Mechanisms, Clinical Risks, and Safety Considerations in Generative AI Chatbots**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/9rqhg_v1

As generative AI chatbots become embedded in everyday life, their inherent risks are manifesting in unprecedented ways. Emerging reports describe cases of AI Psychosis in which intensive chatbot use triggers delusional thinking and altered behaviour. This paper proposes a mechanism wherein baseline user vulnerabilities and specific engagement patterns interact with generative AI attributes, such as sycophancy and hallucination, to induce cognitive distortions. Subsequently, it outlines clinical, design, and regulatory strategies that can help mitigate risks.

**Решение:** -1 концептуальный анализ механизмов и клинических рисков «ИИ-психоза»

---

### 91 · R8668

**Protective Factor-Aware Dynamic Influence Learning for Suicide Risk Prediction on Social Media**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2507.10008

Suicide is a critical global health issue that requires urgent attention. Even though prior work has revealed valuable insights into detecting current suicide risk on social media, little attention has been paid to developing models that can predict subsequent suicide risk over time, limiting their ability to capture rapid fluctuations in individuals' mental state transitions. In addition, existing work ignores protective factors that play a crucial role in suicide risk prediction, focusing predominantly on risk factors alone. Protective factors such as social support and coping strategies can mitigate suicide risk by moderating the impact of risk factors. Therefore, this study proposes a novel framework for predicting subsequent suicide risk by jointly learning the dynamic influence of both risk factors and protective factors on users' suicide risk transitions. We propose a novel Protective Factor-Aware Dataset, which is built from 12 years of Reddit posts along with comprehensive annotations of suicide risk and both risk and protective factors. We also introduce a Dynamic Factors Influence Learning approach that captures the varying impact of risk and protective factors on suicide risk transitions, recognizing that suicide risk fluctuates over time according to established psychological theories. Our thorough experiments demonstrate that the proposed model significantly outperforms state-of-the-art models and large language models across three datasets. In addition, the proposed Dynamic Factors Influence Learning provides interpretable weights, helping clinicians better understand suicidal patterns and enabling more targeted intervention strategies.

**Решение:** ? T3 выявление факторов суицидального риска на Reddit, оценка LLM; проверить согласие в полном тексте

---

### 92 · R9714

**Fine-tuning LLM for Counseling Application in Federated Learning Setting**

2025 · UbiComp Companion · journalarticle, book · https://doi.org/10.1145/3714394.3754388

LLMs hold significant potential for counseling applications, which can support the treatment of common mental health conditions. If LLMs can perform counseling tasks as effectively as human counselors, it could generate helpful, patient-specific advice to a wide range of patients, at any time, reducing financial and logistic barriers to mental healthcare. One way to train LLMs to perform counseling tasks like human counselors is to fine-tune it with real conversational data of patients and counselors, produced by audio-recording counseling sessions. Although that data would be highly valuable in incorporating human-like tone and fluency in LLM's responses, direct access to such data is often not feasible due to privacy concerns. Federated learning offers a solution by enabling collaborative model training across decentralized data sources without exposing the raw data. This study makes two main contributions. Firstly, we propose a novel application of fine-tuning LLM through federated learning : Counseling. Secondly, we conduct an experiment to show that federated learning does not limit the effectiveness of fine-tuning any more than centralized training for the novel application of counseling. Our experimental findings demonstrate that federated learning can fine-tune LLMs for counseling without compromising model performance, providing a privacy-preserving alternative to centralized approaches.

**Решение:** -6 дообучение чат-бота для психологического консультирования в federated learning

---

### 93 · R11506

**LLM prompts used in coach phrase priming.**

2024 · https://doi.org/10.1371/journal.pdig.0000431.t001

Large language models (LLMs) have shown promise for task-oriented dialogue across a range of domains. The use of LLMs in health and fitness coaching is under-explored. Behavior science frameworks such as COM-B, which conceptualizes behavior change in terms of capability (C), Opportunity (O) and Motivation (M), can be used to architect coaching interventions in a way that promotes sustained change. Here we aim to incorporate behavior science principles into an LLM using two knowledge infusion techniques: coach message priming (where exemplar coach responses are provided as context to the LLM), and dialogue re-ranking (where the COM-B category of the LLM output is matched to the inferred user need). Simulated conversations were conducted between the primed or unprimed LLM and a member of the research team, and then evaluated by 8 human raters. Ratings for the primed conversations were significantly higher in terms of empathy and actionability. The same raters also compared a single response generated by the unprimed, primed and re-ranked models, finding a significant uplift in actionability and empathy from the re-ranking technique. This is a proof of concept of how behavior science frameworks can be infused into automated conversational agents for a more principled coaching experience.</div

**Решение:** -2 эксперты оценивают эмпатичность ответов LLM при коучинге (coach phrase priming)

---

### 94 · R7103

**Artificial intelligence in maxillofacial trauma: expert ally or unreliable assistant?**

2025 · Medicina oral, patologia oral y cirugia bucal · journal article, journalarticle, article · eng · https://doi.org/10.4317/medoral.27229

Background Large language models (LLMs), such as ChatGPT, have demonstrated potential in synthesizing complex clinical information, yet concerns persist regarding their accuracy and reliability in specialized domains. The rationale of this study is to address a gap in the literature by evaluating ChatGPT-4o’s capabilities and limitations in terms of accuracy and reliability on oral and maxillofacial traumatology. Material and Methods A total of 188 oral and maxillofacial trauma-related questions were selected from a comprehensive resource. Thirty questions were randomly chosen and submitted to ChatGPT-4o resetting to “new chat” mode every repetition to eliminate potential memory bias. Accuracy was scored using a 3-point Likert scale. Reliability was assessed with weighted kappa (κ) and Intraclass Correlation Coefficient (ICC), and internal consistency was evaluated using both Cronbach's alpha (α) and McDonald’s omega (ω). Results The accuracy rates for comprehensive and adequate responses were calculated as 38% (95% CI: 32.5% - 43.5%) and 58% (95% CI: 52.1% - 63.3%), respectively. Weighted kappa (κ = 0.469) and ICC (0.503) indicated moderate reliability. Internal consistency metrics revealed excellent and good reliability, respectively (α = 0.904, ω = 0.860). Conclusions ChatGPT-4o demonstrated promising results as an adjunct tool in providing supplementary educational content, verifying critical information, and supporting the decision-making processes in oral and maxillofacial traumatology. Current limitations warrant further research. Future enhancements in LLMs and prompt engineering may assist in the optimization of their clinical applicability and alignment with evidence-based standards. Key words:Oral surgery, maxillofacial trauma, artificial intelligence, large language models, performance, clinical decision making.

**Решение:** -4 челюстно-лицевая хирургия и травматология

---

### 95 · R1348

**Large Language and Foundation Models for Machinery Health Monitoring: A Systematic Review**

2026 · Open Science Framework · studyregistration/pre-registration, preprint, review · https://doi.org/10.17605/osf.io/bas7r

The rapid adoption of large language models (LLMs) and foundation models is re-shaping machinery health monitoring. This shift moves the field beyond task-specific deep learning (DL) toward more generalist and multimodal intelligence. Addressing this transition’s fragmented methodology, this systematic review uniquely shifts the focus from purely algorithmic performance to practical industrial deployment. It achieves this by mapping the evolution of text-centric LLMs into autonomous, cyber-physical industrial agents. Following the preferred reporting items for systemat-ic reviews and meta-analyses (PRISMA) 2020 guidelines, an analysis of 58 Scopus studies published between 2022 and early 2026 was conducted to answer six core re-search questions (RQs). The synthesized literature demonstrates striking quantitative gains. Multimodal foundation models improve out-of-distribution accuracy to 71.95%, up from 18.25% in conventional models. Furthermore, they achieve approximately 98% fault diagnosis accuracy using merely 1.2% labeled samples. To ensure reliability, integrating retrieval-augmented generation (RAG) and knowledge graphs (KGs) miti-gates hallucinations. Meanwhile, autonomous agentic architectures within digital twins (DTs) reduce false positive alarms by up to 67%. Despite generative artificial in-telligence (GenAI) tackling data scarcity via synthetic data generation, challenges re-main regarding real-time determinism, corpus poisoning, and edge deployment. Ulti-mately, real-world adoption demands targeted physics-AI hybridization and hard-ware-embedded DTs over generic compression.

**Решение:** -4 диагностика состояния промышленного оборудования

---

### 96 · R8191

**Detecting Suicidal Ideation on Social Media Using Large Language Models with Zero-Shot Prompting**

2025 · International Conference on Information and Communication Technologies for Ageing Well and e-Health · journalarticle · https://doi.org/10.5220/0013283400003938

: Detecting suicidal ideation in social media posts using Natural Language Processing (NLP) and Machine Learning has become an essential approach for early intervention and providing support to at-risk individuals. The role of data is critical in this process, as the accuracy of NLP models largely depends on the quality and quantity of labeled data available for training. Traditional methods, such as keyword-based approaches and models reliant on manually annotated datasets, face limitations due to the complex and time-consuming nature of data labeling. This shortage of high-quality labeled data creates a significant bottleneck, limiting model fine-tuning. With the recent emergence of Large Language Models (LLMs) in various NLP applications, we utilize their strengths to classify posts expressing suicidal ideation. Specifically, we apply zero-shot prompting with LLMs, enabling effective classification even in data-scarce environments without needing extensive fine-tuning, thus reducing the dependence on large annotated datasets. Our findings suggest that zero-shot LLMs can match or exceed the performance of traditional approaches like fine-tuned RoBERTa in identifying suicidal ideation. Although no single LLM outperforms consistently across all tasks, their adaptability and effectiveness underscore their potential to detect suicidal thoughts without requiring manually labeled data.

**Решение:** ? T3 детекция суицидальных мыслей в соцсетях zero-shot LLM против RoBERTa; проверить эталон разметки в полном тексте

---

### 97 · R3521

**Sequential Human-AI Collaboration Impairs Narrative Creativity in University Students: A Randomized Controlled Trial**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-8774138/v1

Abstract The rise of generative AI (GenAI) has sparked interest in whether human-AI collaboration can enhance creativity, yet empirical findings remain mixed. This study systematically compared 4 collaboration models (i.e., AI-first, AI-follow, AI-parallel, and human-only) using a randomized controlled experiment involving 112 college students. Participants completed a two-stage narrative story-writing task. Creativity was assessed by both trained human raters (N = 10) and a validated AI model, while creative self-efficacy was measured before and after the task. A residualized linear model was used to control baseline differences and covariates. Results showed that sequential collaboration models (i.e., AI-first and AI-follow) significantly impaired narrative creativity relative to human-only creation, and AI-parallel collaboration did not improve creativity. None of the models improved creative self-efficacy. These findings suggest that GenAI may even disrupt key cognitive mechanisms underlying narrative creativity. Using a rigorous research design, we examine how different models of human-AI collaboration shape creativity. Implications for human-AI co-creation in education and design are discussed.

**Решение:** -4 исследование совместного с ИИ написания текстов и его влияния на креативность

---

### 98 · R6242

**Change the Number, Change the Answer: Assessing Rating Scale Sensitivity in LLM-Based Text Scoring**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.22187

Large language models (LLMs) are increasingly used in computational social science to assign scalar scores to social and psychological constructs. However, studies use different rating scales, and whether their scores remain comparable across scale designs is understudied. To address this gap, we define and systematically investigate scale sensitivity, the variation in LLM-generated scores caused by rating scale design. We distinguish numerical sensitivity, changes in normalized scores, from semantic sensitivity, changes in score interpretation. To assess both, our experimental design crosses 2 formats (continuous vs. ordinal), 4 ranges (3, 5, 11, and 21 points), and 2 signs (signed vs. unsigned) across 3 tasks (political leaning, sentiment, and toxicity), 2 prompting strategies (zero-shot and rubric-based), and 5 LLMs. We find that changing one design element shifts normalized scores by about 0.10 on average and changes the category of roughly 20% of texts. Sensitivity is greatest for toxicity, the only unipolar construct examined. Also, rubric-based prompting does not reduce sensitivity compared with zero-shot prompting. We provide practical guidance for designing more reliable LLM-based text scoring and highlight the need for robustness checks across alternative scales.

**Решение:** -5 исследование чувствительности шкал разметки LLM без сопоставления с разметкой людей

---

### 99 · R10619

**TrapLLM: An LLM-powered Interactive Log-based Honeypot for Real-world Network Attacks**

2025 · IEEE International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom) · journalarticle, conference, conference-paper · https://doi.org/10.1109/trustcom66490.2025.00183

With the continual escalation of cyberattack tactics, zero-day exploits and advanced persistent threats (APTs) characterized by high stealth and dynamic evolution have posed significant challenges to traditional honeypot systems. Existing approaches are limited in service fidelity, interactive intelligence, and awareness of attacker intent, making it difficult to effectively lure advanced attackers or reconstruct threat chains from massive volumes of log data. To address these challenges, this paper introduces large language models (LLMs) as the core driving force to construct an architecture that integrates log-driven data governance with dynamic response generation. Leveraging the semantic understanding and generative capabilities of LLMs, the proposed method enables fine-grained identification of attacker intent, reconstruction of event sequences, and adaptive responses driven by retrieval-augmented generation (RAG), thereby realizing an intelligent closed-loop defense. This innovative integration overcomes the constraints of traditional static rules and low interaction emulation, achieving attack intent analysis and adaptive deception response, and providing an efficient pathway for proactive threat hunting. During a 25day deployment in a real production network environment, the system utilized 25 diversion nodes and 8 types of emulated services to capture over 1.39 million raw attack logs. Analysis revealed multiple attack attempts targeting 9 known Common Vulnerabilities and Exposures (CVE) vulnerabilities, along with a substantial number of high-severity attacks for which specific CVE identifiers could not be determined. Experimental results demonstrate that the proposed approach significantly improves both the accuracy of threat awareness and the timeliness of response, providing reliable support for the evolution of intelligent defense mechanisms.

**Решение:** -4 кибербезопасность, интерактивные ловушки honeypot (TrapLLM)

---

### 100 · R7397

**Emotion-Aware Dysarthric Speech Reconstruction: LLMs and Multimodal Evaluation with MCDS**

2025 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/2d37-tm34

Dysarthria, a motor speech disorder affecting over 46 million individuals globally, impairs both intelligibility and emotional expression in communication. This work introduces a novel framework for emotion-aware sentence reconstruction from dysarthric speech using Large Language Models (LLMs) fine-tuned with QLoRA, namely LLaMA 3.1 and Mistral 8x7B. Our pipeline integrates direct emotion recognition from raw audio and conditions textual reconstruction on this emotional context to enhance both semantic and affective fidelity. We propose the Multimodal Communication Dysarthria Score (MCDS), a holistic evaluation metric combining BLEU, semantic similarity, emotion consistency, and human ratings: MCDS=αB+βE+γS+δH where $\alpha + \beta + \gamma + \delta = 1$. On our extended TORGO+ dataset, our emotion-aware LLM model achieves a MCDS of 0.87 and BLEU of 72.4%, significantly outperforming traditional pipelines like Kaldi GMM-HMM (MCDS: 0.52, BLEU: 38.1%) and Whisper-based models. It also surpasses baseline LLM systems by 0.09 MCDS. This sets a new benchmark in emotionally intelligent dysarthric speech reconstruction, with future directions including multilingual support and real-time deployment.

**Решение:** -4 реконструкция дизартрической речи с сохранением эмоций, речевые технологии

---

### 101 · R12387

**OpenAi’s ChatGPT-4, BARD and YOU.com (AI) and the Cancer Patient, for Now, Caveat Emptor, but Stay Tuned**

2023 · Digital Medicine and Healthcare Technology · journalarticle, article · en · https://doi.org/10.5772/dmht.19

ChatGPT-4, BARD, and YOU.com are AI large language models (LLM) developed by OpenAI based on the GPT-3-4 architecture and Google. They were trained using unsupervised learning, which allows them to learn from vast amounts of text data without requiring explicit human labels. ChatGPT-4 was exposed to training information up to September 2021. By presenting prompts (queries) to ChatGPT-4, BARD, and YOU.com, including a typical case presentation (vignette) of a new patient with squamous cell tonsillar cancer, we uncovered several specific issues that raise concerns for the current application of this early phase of advanced LLM AI technology for clinical medicine. By prompting and comparing responses of three different LLMs (ChatGPT-4, BARD, and YOU.com) to identical prompts, we reveal several flaws in each AI that, if taken as factual, would affect clinical therapeutic suggestions and possible survival. The presented clinical vignette of a patient with newly diagnosed tonsillar cancer is presented to three LLMs readily available for free trial allowing comparison of results. We observed frequent changing responses to unchanging prompts over just hours and days within the same and between LLMs, critical errors of guideline-recommended drug therapy, and noted that several AI-supplied references presented by the AIs are bogus AI-generated references whose DOI and or PMID identifiers were either nonexistent or led to completely irrelevant manuscripts on other subjects.

**Решение:** -4 соматическая онкология, ответы ChatGPT, Bard и You.com для пациентов

---

### 102 · R1899

**Counseling and Health Education in Primary Care Dentistry**

2026 · Zenodo · journalarticle/ · https://doi.org/10.5281/zenodo.21327419

Counseling and health education in dental primary care are distinct but intertwined practices. Counseling addresses the affective, relational, and volitional dimensions of change; education conveys information and builds capability. This note outlines the theoretical underpinnings of motivational interviewing and the therapeutic alliance, examines how health education is most effective when embedded within a counselling frame, and proposes practical structures for integrating both into routine dental encounters. The dentist's role extends beyond technical skill to include genuine facilitation of patient autonomy and health literacy. Author roles: Clinical Dentist & Clinic Manager, Dr. Ahmed Etman Dental Center; Medical AI Evaluator, Outlier AI; AI-Safety/LLM Red Team, DataAnnotation.tech; Benchmark Producer & Primary Domain Reviewer, ClinMAP-VOI v0.

**Решение:** -1 руководство / обзор по консультированию в стоматологии

---

### 103 · R11692

**PBChat: Enhance Student’s Problem Behavior Diagnosis with Large Language Model**

2024 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-031-64302-6_3

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T1/T3 диагностика проблемного поведения учащихся (PBChat), нет аннотации — проверить эталон в полном тексте

---

### 104 · R7792

**Affective connotations according to LLMs: implications for meaning measurement and cultural bias.**

2025 · Cognition & emotion · journal article, med, journalarticle · eng · https://doi.org/10.1080/02699931.2025.2568551

The affective connotations of words are central to meaning and important predictors of many social processes. As such, understanding the degree to which commercially-available generative language models (LLMs) replicate human judgements of affective connotations may help better understand human-model interactions. LLMs may also serve as useful tools for researchers seeking affective meaning estimates. We test the ability of three LLMs - GPT-4o, Mistral Large, and Llama 3.1 - to estimate human affective connotation ratings of words representing social identities, behaviours, modifiers, and settings in three language cultures: English (US), French (France), and German (Germany). We find that LLM ratings of terms correlate strongly with human ratings. However, their ratings tend to be overly extreme and patterns of correlations between meaning dimensions only loosely approximate those of human ratings. Consistent with previous findings of English-language and American biases in LLMs, we find that LLMs tend to perform better on English terms, though this pattern varies somewhat by meaning dimension and the type of term in question. We explore how LLMs might contribute to scholarship on affective connotations - by acting as tools for measurement - and how scholarship on affective connotations might contribute to generative language models - by guiding exploration of model biases.

**Решение:** -4 оценка эмоциональных коннотаций отдельных слов (лексиконы слов)

---

### 105 · R12446

**Rapid evaluation of the efficacy of ChatGPT for screening studies in a systematic review**

2023 · OSF · studyregistration/pre-registration, text/project · https://doi.org/10.17605/osf.io/bc3gj

Objectives: • To provide a rapid evaluation of the performance of ChatGPT in screening titles, abstracts, and full-text articles for inclusion in a systematic review on parenting in protracted refugee situations. • To compare the performance of ChatGPT with the performance of human reviewers in the screening process. Methods: • Dataset preparation Use the dataset from the previously screened studies. • Dataset training and screening We will supply the ChatGPT model with all the PROSPERO registration data and material specific to this review. To ensure that the constructs defined in this review of parenting, refugees, and protracted refugee situations are being applied in line with the formulations we published on PROSPERO, rather than other formulations that ChatGPT may have been pre-trained at, we will check the output of ChatGPT using ten articles and if needed reclarify or rephrase the definitions to realign the model. We will then assess 300 titles and abstracts that are double-reviewed. Of these, we will review 100 titles and abstracts in English language black literature and another 100 titles and abstracts in English language grey literature. These studies will be an even split between those that were categorised by the human coders as Yes/Maybe (50%) and those categorised as No (50%). We will take 100 studies from all the other four main languages in this review (Arabic, French, Italian, and Urdu). Because there are smaller numbers of studies in these four languages and a high proportion of them were excluded, we will have 25 from each of the languages but these will not be an even split between those categorised as Yes/Maybe and those categorised as No. We will then assess ChatGPT’s efficacy in screening 100 [corrected from 300] full-text studies. We will try to balance our selection of the studies to include a variety of the four exclusion reasons that we have, and we will assess all the included studies. Finally, we will assess the data extraction capabilities of ChatGPT for 30 studies, which include peer-reviewed and grey literature. • Model evaluation We will compare the performance metrics of ChatGPT with those of human reviewers in the screening process. Statistical analysis • To compare performance abilities, we will compare the sensitivity, specificity, and accuracy between ChatGPT and human reviewers. I. Sensitivity: At the title and abstract stage, this would be the proportion of Yes/Maybe that the model correctly identifies. At the full-text screening stage, this would be the proportion of the inclusion decisions that the model correctly identifies. At the extraction stage, this would be correctly identifying relevant empirical data in each of the extraction categories. II. Specificity: At the title and abstract stage, this would be the proportion of No that the model correctly identifies (we will also look at specificity by exclusion reason). At the full-text screening stage, this would be the proportion of the exclusion decisions that the model correctly identifies. At the extraction stage, this would be correctly identifying irrelevant empirical data. III. Accuracy: The proportion of correct predictions made by the model out of the total predictions. • To understand agreement levels, we will calculate Cohen's kappa coefficient to measure inter-rater reliability between ChatGPT and human reviewers. We will also calculate weighted Kappa, penalising false rejection decisions by ChatGPT, since these are the most costly decisions [Sentence added]. Additionally, to account for bias in the dataset we will adjust Kappa as per Byrt et al., (1993)’s recommendations [Sentence added]. • To understand how prompt reliability could affect performance and agreement levels, we will calculate all scores again for concept(s) that achieve the highest reliability scores [Sentence added after results show that concepts of 'protracted' and 'parenting' returned relatively low test re-test reliability scores]. Descriptive assessment • Conduct a descriptive assessment of any discrepancies between ChatGPT and human reviewers to identify potential areas for improvement in the ChatGPT model. Expected Outcomes: 1. Assessment of ChatGPT's performance in screening studies and extracting information from them for a systematic review, as compared to human reviewers. 2. Identification of potential areas for improvement in ChatGPT’s systematic review screening process. 3. Insights into the applicability of ChatGPT for use in systematic reviews, particularly in the field of social sciences, including psychology. Timeline: Dataset preparation: 2 weeks Model evaluation: 2 weeks Reporting: 2 weeks Total duration: 6 weeks [Added] Delayed encountered: Testing limits and issues with answers from prompts have significantly delayed project delivery date by a few months

**Решение:** -6 скрининг литературы для систематических обзоров с помощью ChatGPT

---

### 106 · R0840

**ADAPT-MIND: A Cross-Domain Deep Learning Framework for Mental Health Signal Detection in Shakespearean and Social Media Texts**

2026 · IEEE Transactions on Computational Social Systems · journalarticle · https://doi.org/10.1109/tcss.2026.3654355

Cross-domain detection of mental distress signals in historical and contemporary texts is very challenging because of linguistic heterogeneity and the limited annotation resources. Adapter-Augmented Distillation And Prompt-Tuning – Memory-Augmented INference for Distress (ADAPT-MIND) proposes a unified framework that integrates adapter-enhanced LLM embeddings, graph-attentive temporal convolutions, memory-augmented transformers, adversarial–contrastive distillation and mutual information regularization, and mixed meta-learned soft prompts. Shared pre-processing and feature augmentation are applied to both Shakespearean utterances (10% expert-annotated, $\kappa = 0.82$) and 7489 student social-media posts (80/10/10 split), including pronoun variance, affective bigrams, syntactic entropy, and graph positional encodings. On five-fold cross-validation, ADAPT-MIND achieves accuracies of 0.912 for Shakespearean and 0.857 for students, with F1 scores of 0.911 and 0.856 and AUC of 0.948 and 0.903, respectively. Extensive ablation studies confirm an F1 drop of up to 4.2% by removing the graph-temporal module, proving its critical role in capturing multiscale narrative context. Error analysis shows misunderstanding of archaic idioms is responsible for 31%, while the rest is mainly due to mistaken academic stress, totaling 27%. Hyper-parameter optimization utilizes hierarchical Bayesian search over loss weights, learning rates, adapter dimensions, and convolution depth. The proposed approach delivers state-of-the-art performance across domains while ensuring interpretability and efficient parameter adaptation.

**Решение:** + T3/T1 выявление дистресса в текстах студентов и Шекспира: модель ADAPT-MIND с LLM-адаптерами против экспертов, каппа 0.82

---

### 107 · R5927

**Counterargument for Critical Thinking as Judged by AI and Humans**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2605.05353

This intervention study investigates the use of counterarguments in writing for critical thinking by students in the context of Generative AI (GenAI). This is especially as risks of cheating and cognitive offloading exist with the use of GenAI. We presented 36 students in a particular university course with 4 carefully selected thesis statements (from a set of popular debates) to write about anyone of them. We used six established rubrics (focus, logic, content, style, correctness and reference) to conduct three human assessments (two student peer-reviews and one experienced teacher) per writeup on a 5-point Likert scale for all the qualified samples (n) of 35 submissions (after disqualifying one for irregularity). Using the same rubrics and guidelines, we also assessed the submissions using six frontier LLMs as judges. Our mixed-method design included qualitative open-ended feedback per assessment and quantitative methods. The results reveal that (1) the students' self-written counterarguments to AI-generated content contains logic, among other things, which is a key component of critical thinking, and (2) GenAI can be successfully used at scale to assess students' written work, based on clear rubrics, and these assessments generally align with human assessments as shown with Gwets AC2 inter-rater reliability values of 0.33 for all the models except one. 9 pages

**Решение:** -4 оценка аргументации критического мышления в студенческих эссе

---

### 108 · R5888

**Characterizing public comments via Regulations.gov in response to proposed cannabis rescheduling in the United States.**

2026 · Addiction (Abingdon, England) · journal article, journalarticle, article · eng · https://doi.org/10.1111/add.70410

AIMS: The United States Drug Enforcement Administration's (DEA) proposed rescheduling of cannabis from Schedule I to Schedule III under the Controlled Substances Act marks a significant shift in federal policy. Understanding public sentiment toward this policy is critical for guiding the current cannabis rescheduling effort as well as future reforms. The objective of this study is to characterize public comments submitted to Regulations.gov regarding the DEA's cannabis rescheduling proposal and identify underlying justifications for support or opposition. DESIGN: A mixed-methods analysis was conducted. SETTING: Online public comments submitted to Regulations.gov regarding the DEA's cannabis rescheduling proposal. PARTICIPANTS: 42 913 public comments submitted between 21 May and 22 July 2024. MEASUREMENTS: Comments were analyzed for sentiment towards the proposed rescheduling (support, oppose or insufficient rescheduling) and thematic justifications using manual and automated natural language processing techniques. A two-stage annotation approach was employed: manual coding of 200 randomly sampled comments by multiple independent evaluators, followed by automated classification of all 42 913 comments using open source Large Language Model (LLM) validated against the manual annotations. FINDINGS: Using LLM-based classification validated against human annotations [88% agreement, F1 (harmonic mean of precision and recall) = 0.86], we found that among 42 913 comments, 28.85% [95% confidence interval (CI) = 28.44%-29.24%] supported rescheduling, 6.74% (95% CI = 6.50%-6.99%) opposed and 63.50% (95% CI = 63.06%-63.99%) deemed the proposal insufficient, favoring further rescheduling or complete de-scheduling of cannabis. Among the 200 manually annotated comments, therapeutic benefits (56.7%, 95% CI = 46.7%-66.7%) and economic impacts (27.8%, 95% CI = 18.9%-37.8%) were the most common justifications among supporters. Public health risks (100.0%, 95% CI = 100.0%-100.0%), addictiveness concerns (71.4%, 95% CI = 42.9%-100.0%) and concerns about underage use (57.1%, 95% CI = 14.3%-85.7%) were predominant in opposing comments. Insufficient rescheduling comments cited therapeutic benefits (37.8%, 95% CI = 28.5%-48.0%), economic impacts (28.6%, 95% CI = 19.4%-37.8%) and criminal justice reform (26.5%, 95% CI = 18.4%-35.7%) as primary justifications. CONCLUSIONS: Public sentiment on Regulations.gov supports the United States Drug Enforcement Administration's proposal for cannabis rescheduling, though the majority views the proposed Schedule III classification as inadequate and supports further rescheduling or complete de-scheduling of cannabis.

**Решение:** -4 анализ публичных комментариев к регуляторным актам по каннабису

---

### 109 · R11145

**A New Method Supporting Qualitative Data Analysis Through Prompt Generation for Inductive Coding**

2024 · IEEE International Conference on Information Reuse and Integration for Data Science (IRI) · conference, conference-paper · en · https://doi.org/10.1109/iri62200.2024.00043

Recent advances in Large Language Models (LLMs) have revolutionized numerous fields, including Qualitative Data Analysis (QDA). This paper introduces a novel method, ArGUMENT2CODE (A2C), designed to leverage the capabilities of LLMs for enhancing the QDA process, particularly focusing on the inductive coding aspect. A2C sets itself apart from conventional automated coding tools by initiating a two-stage fine-tuned LLM process adept at navigating the complex landscape of qualitative data. This innovative method starts with the identification of coding cues hidden within the textual data, which are then refined into targeted prompts. These prompts are then used for guiding the inductive coding process, facilitating the generation of a rich, actionable codebook that offers expansive coverage of analytical perspectives. Our experimentation reveals that A2C not only successfully generates a pertinent and insightful codebook consistently but also significantly outperforms all other existing methods.

**Решение:** -4 метод индуктивного качественного кодирования A2C, нет психолого-клинического конструкта

---

### 110 · R8115

**Adversarial Prompt Optimization in LLMs: HijackNet's Approach to Robustness and Defense Evasion**

2025 · Preprints.org · preprint, ppr · https://doi.org/10.20944/preprints202506.0937.v1

This paper introduces HijackNet, an adversarial prompt hijacking framework designed to improve hijacking success rates and generalization in multi-lingual tasks. Combining Neural Architecture Search (NAS), Reinforcement Learning (RL), and Multi-Objective Optimization (MOO), HijackNet generates adversarial prompts that adapt to target tasks while bypassing model defense mechanisms. This framework optimizes hijacking success, defense evasion, and task completion through a combination of a prompt generator and adversarial optimizer. We introduce a Defense Robustness Score (DRS) to evaluate the stability of prompts in adversarial settings. HijackNet improves adversarial prompt generation, advancing the security and robustness of large language models in adversarial environments.

**Решение:** -4 состязательная оптимизация промптов (HijackNet), кибербезопасность

---

### 111 · R9963

**A Survey of Textual Adversarial Attacks and Defenses on Large Language Models (LLMs)**

2025 · Science and Technology of Engineering Chemistry and Environmental Protection · journalarticle, review, article · https://doi.org/10.61173/m8d1p054

The broad use of large language models (LLMs) like GPT-4 and LLaMA in dialogue systems, content generation, etc., causes security flaws of these models to rise. The current study examines progress made in recent years on textual adversarial attacks and defenses for LLMs, focusing on special attack vectors and defensive techniques targeting LLMs. Firstly, a 'Target—Technology—Scenario' three-dimensional attack classification framework that mainly consists of typical kinds of attacks including PIA and JBA. Secondly, defense mechanisms from two different perspectives: alignment enhancement in the training phase and security controls in the inference phase. In addition, by conducting experiments using benchmark datasets (HELM), existing technical drawbacks and future work directions are also discussed. The aim is to offer guidance and references for subsequent work on theoretical studies of LLM security and promoting the building of stronger NLP systems.

**Решение:** -1 обзор текстовых состязательных атак и защит для LLM

---

### 112 · R8093

**Exploring online polarisation in the United States: A computational social science approach**

2025 · University of Oxford · dissertation/dissertation · https://doi.org/10.5287/ora-zvkmmezxv

Affective polarisation—the profound divide between political groups—has emerged as a critical threat to American democracy, vividly illustrated by events like the January 6th 2021 Capitol Hill attack. Despite widespread concern, existing research has struggled to adequately measure polarisation at scale, trace its evolution across actors and time, and map its structural underpinnings in online networks. This thesis addresses these gaps by means of three papers, leveraging theoretical and methodological innovations, and large-scale empirical analysis of US Twitter data from 2015 to 2020. The first paper introduces a novel framework for detecting polarising language using supervised machine learning classifiers based on transformer models. By integrating the political affiliations of human coders and benchmarking against generative artificial intelligence (AI), the study demonstrates that coder ideology shapes perceptions of divisiveness, with combined human coders’ perspectives yielding more balanced and accurate classification than single-affiliation or AI-only models. These classifiers, which will be made publicly available, establish a robust foundation for scalable and nuanced measurement of affective polarisation. Building on this measurement advance, the second paper investigates the temporal and directional dynamics of polarisation among US politicians, news media, and the public. Applying vector-autoregressive models to a comprehensive tweet dataset, the analysis reveals that polarising rhetoric is driven by a dynamic feedback loop: politicians, media, and citizens alternately lead and respond to shifts in divisive language. The media acts as a catalyst, while cross-party interactions often escalate polarisation, underscoring the complex, reciprocal nature of digital political discourse. The third paper turns to the network structures that sustain elite polarisation. Using hierarchical exponential random graph models, it maps the relational architecture of political communication. It finds that party-based homophily dominates network formation. Democrat politicians hold stronger connections to other powerful nodes in the network than Republicans. The most divisive language is concentrated in the rare ties bridging partisan clusters, highlighting the joint role of network structure and rhetoric in entrenching polarisation. Together, these studies advance both the measurement and substantive understanding of affective polarisation in digital public spheres, offering new tools and theoretical insights for researchers, policymakers, and platform designers seeking to address the challenges of polarisation in contemporary democracies.

**Решение:** -4 политическая аффективная поляризация в США

---

### 113 · R4207

**Breaking the Ceiling: Mitigating Extreme Response Bias in Surveys Using an Open-Ended Adaptive-Testing System and LLM-Based Response Analysis**

2026 · AI · journalarticle, review, article · en · https://doi.org/10.3390/ai7020073

Assessments of extreme psychological constructs often face a persistent challenge: the ceiling effect, in which a significant proportion of respondents select the highest score on a scale, thus obscuring an important part of the population's variation. This effect may have profound consequences in studies of extreme psychological constructs. To address this limitation, we introduce a novel framework that integrates Multistage Testing (MST) with open-ended questions that are automatically analyzed by large language models (LLMs). This hybrid approach adapts the survey questions to the respondent while leveraging LLMs to efficiently and reliably interpret free-text answers in large-scale online surveys. Using a case study on aversion toward cockroaches, we show how our method can effectively eliminate extreme ceiling effects, revealing hidden data distributions that are often obscured by extreme responses to conventional Likert-type survey questions. In addition, validation against expert human annotations of survey responses demonstrates the consistency and reliability of the LLMs' performance as evaluators of free-text answers. This framework offers a generalizable methodology that enables more precise and sensitive quantitative measurement of extreme psychological constructs, allowing researchers to study topics that until now were inaccessible due to significant, inherent ceiling effects.

**Решение:** + T2/T1 открытые психологические вопросы против эффекта потолка: скоринг ответов LLM против экспертной разметки

---

### 114 · R7465

**Computer-Assisted Code Generation Using Combination of Generative Artificial Intelligence, Stepwise Coding, and Topic Modeling**

2025 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-12229-2_20

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 генерация кода, программная инженерия, нет аннотации

---

### 115 · R9299

**KNOWLEDGE AND IDENTIFICATION OF AI VERSUS HUMAN HEALTHCARE RESPONSES: PERCEPTIONS OF PAKISTANI HEALTHCARE PROFESSIONALS**

2025 · TPM Testing, psychometrics, methodology in applied psychology · article · en · https://tpmap.org/submission/index.php/tpm/article/download/4251/3217

Purpose and Objectives: The objective of the study was to compare the quality of answers that the large language models (LLMs), namely ChatGPT-4 and the general AI model, provide concerning the perceived quality of responses provided by human participants, as perceived by the Pakistani professionals in the healthcare sector. These aims were to evaluate differences in knowledge, helpfulness, empathy, question relevance, clarity, and distractor quality and to establish the correlations between response features and patterns of evaluation. Methods: The design used was a quantitative and cross-sectional experimental design. A total of 197 healthcare professionals in Pakistan were selected and interviewed in May 2025. ChatGPT-4, a general AI model, and human experts were the participants who provided a response to the health-related questions. Knowledge, helpfulness, and empathy Likert-type scales were used to evaluate anonymized responses by the participants. The statistical tests (Chi-square, Spearman rank correlation, mean comparison with confidence interval 95) were used. Results: ChatGPT-4 reactions were similar to human-created reactions in dimensions all, and there were non-significant mean distinctions in the interpretation of the queries (MD = -.13), clearness (MD = -.03) and caliber of distractors (MD = -.10). The overall model of AI was significantly worse in all the areas, especially clarity (MD = 1.21, p = 0.001) and distractor quality (MD = 1.5). Chi-square measures showed that there were significant relationships between response type and knowledge (Cramer V = 0.099), helpfulness (V = 0.116) and empathy (V = 0.115). Spearman correlations revealed that there were great connections between the knowledge and helpfulness (r = 0.83 0.85), between knowledge and empathy (r =0.67 0.69), and between helpfulness and empathy (r = 0.76 0.79). Conclusion: ChatGPT-4 proves to be as efficient as medical expertise in producing the relevant, understandable, and empathetic responses, which is why it may be considered a helpful solution in medical education and evaluation. The presence of high required human supervision may suggest that other AI models have low performance. Though such findings are encouraging, the confidence of evidence was considerably low suggesting the necessity to conduct other studies using more diverse bigger samples.

**Решение:** -2 оценка пациентами качества медицинских ответов ИИ по сравнению с врачами

---

### 116 · R3612

**Using LLMs as a clinician support for detecting defense mechanisms from psychotherapy transcripts: a proof-of-concept study**

2026 · Current Psychology · journalarticle, article · en · https://doi.org/10.1007/s12144-026-09685-3

Abstract This proof-of-concept study evaluated the feasibility of using large language models (LLMs) to support clinicians in identifying defense mechanisms in psychodynamic psychotherapy transcripts, comparing LLM assessments with those of psychodynamic therapists in both solo and supervision group settings. The first two sessions of a psychoanalytic case were analyzed. The transcribed sessions were segmented into excerpts and coded by two psychodynamic clinicians and two LLMs (ChatGPT and Gemini) guided with a structured prompt. Coding followed an adapted version of DMRS comprising 12 defenses organized into three maturity levels. For each excerpt, defense mechanisms were identified, and an overall defensive functioning index (ODF) was calculated. Inter-rater agreement was estimated using the Intraclass Correlation Coefficient (ICC), considering human-human, LLM-LLM, human-LLM, and integrated versions (clinical supervision vs. LLM integration) pairs. LLMs tended to assign a higher number of defenses, including more immature ones, producing profiles with lower average ODFs than clinicians, who instead provided more selective and, overall, more mature ratings. However, some of the defenses reported only by LLMs were subsequently recognized by supervised clinicians as clinically relevant and worthy of inclusion. Clinicians showed good to excellent inter-rater reliability, while ChatGPT and Gemini showed low inter-rater reliability, suggesting that the two models are not interchangeable. Agreement between clinicians and LLMs was low across the sessions. Therefore, the combined use of LLMs among clinicians is technically feasible and could potentially enhance understanding of patients’ defensive functioning, especially as a support for case formulation and supervision. Currently, LLMs cannot replace clinical judgment or the therapeutic relationship, but they might be considered as a support tool for clinical practice under human professional guidance.

**Решение:** + T1/T3 кодирование механизмов психологической защиты (DMRS) по транскриптам психотерапии: LLM против клиницистов, ICC

---

### 117 · R6132

**Elder-Sim: A Psychometrically Validated Platform for Personality-Stable Elderly Digital Twins**

2026 · medRxiv · preprint, ppr · https://doi.org/10.64898/2026.03.25.26349036

Abstract Background Large language models (LLMs) enable patient-facing conversational agents, creating a plausible pathway toward patient digital twins that can capture older adults’ lived experiences, beliefs, and behavioral responses across time. A central barrier to clinical-grade digital twins is personality drift—inconsistent trait expression across repeated, longitudinal interactions—which can undermine the reliability of generated trajectories and intervention-response simulation in geriatric care contexts. Objective To develop ELDER-SIM as a multi-role elderly-care conversational platform oriented toward building personality-stable elderly digital twin agents, and to propose a psychometric validation framework for quantifying and improving personality consistency in LLM-based agents across repeated interactions. Methods ELDER-SIM was implemented using n8n workflow orchestration with local LLM inference (Ollama/vLLM), integrating (1) Big Five (OCEAN) trait specifications, (2) a three-layer Cognitive Conceptualization Diagram (CCD) grounded in Beck’s cognitive behavioral therapy framework, and (3) a MySQL-based long-term memory module for persistent states. We conducted a systematic ablation study across four conditions—Baseline (prompt-only), +Memory, +CCD, and +LoRA (domain-specific fine-tuning using 19,717 instruction pairs derived from CHARLS)—and evaluated personality consistency using Cronbach’s α (internal consistency), intraclass correlation coefficient (ICC) (test–retest reliability), and role discrimination accuracy . Results Personality measurement reliability was acceptable to excellent across conditions (Cronbach’s α: 0.70–0.94), with consistently high test–retest stability (ICC: 0.85– 0.96). Role discrimination improved stepwise from 83.3% (Baseline) to 88.9% (+Memory), 94.4% (+CCD), and 97.2% (+LoRA). CCD produced the largest gain in internal consistency (mean α 0.702→0.892), while LoRA achieved the highest overall internal consistency (α 0.940) and ICC (0.958). Conclusions ELDER-SIM provides a psychometrically validated approach for constructing personality-consistent elderly digital twin agents. By demonstrating that structured cognitive modeling and domain adaptation materially reduce personality drift, the framework supports more reliable longitudinal digital twins for elderly mental health and psychosocial care, enabling reproducible in silico evaluation of interaction trajectories and intervention strategies before clinical deployment.

**Решение:** -6 Elder-Sim: симуляция цифрового двойника пожилого человека (пациент-агент)

---

### 118 · R7039

**Conversation AI Dialog for Medicare powered by Finetuning and Retrieval Augmented Generation**

2025 · arXiv.org · journalarticle, text/article, preprint · https://doi.org/10.48550/arxiv.2502.02249

Large language models (LLMs) have shown impressive capabilities in natural language processing tasks, including dialogue generation. This research aims to conduct a novel comparative analysis of two prominent techniques, fine-tuning with LoRA (Low-Rank Adaptation) and the Retrieval-Augmented Generation (RAG) framework, in the context of doctor-patient chat conversations with multiple datasets of mixed medical domains. The analysis involves three state-of-the-art models: Llama-2, GPT, and the LSTM model. Employing real-world doctor-patient dialogues, we comprehensively evaluate the performance of models, assessing key metrics such as language quality (perplexity, BLEU score), factual accuracy (fact-checking against medical knowledge bases), adherence to medical guidelines, and overall human judgments (coherence, empathy, safety). The findings provide insights into the strengths and limitations of each approach, shedding light on their suitability for healthcare applications. Furthermore, the research investigates the robustness of the models in handling diverse patient queries, ranging from general health inquiries to specific medical conditions. The impact of domain-specific knowledge integration is also explored, highlighting the potential for enhancing LLM performance through targeted data augmentation and retrieval strategies. 12 pages

**Решение:** -4 диалоговая система обслуживания клиентов программы Medicare

---

### 119 · R1293

**Jailbreak-as-a-Service: The Emerging Threat Landscape**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.18226068

The commoditization of jailbreak attacks through Jailbreak-as-a-Service (JaaS) platforms represents a critical escalation in the threat landscape facing generative AI systems. This paper examines the emergence of JaaS as a structured underground economy that democratizes access to sophisticated prompt-based attacks against large language models (LLMs). We analyze the architectural components of the JaaS ecosystem, including marketplace platforms, pricing models, and distribution channels that have lowered the technical barrier for exploiting AI safety mechanisms. Through systematic categorization of attack methodologies employed by JaaS providers-ranging from automated prompt engineering and role-playing techniques to encoded obfuscation strategies, we demonstrate how these services achieve reported success rates of 65-78% against major LLM providers. Our analysis reveals that JaaS platforms operate with varying degrees of sophistication, from simple Telegram bots offering pay-per-query models to subscription-based web portals with curated jailbreak libraries. We present a comparative evaluation of detection and mitigation strategies, highlighting the inadequacy of current guardrail systems against evolving JaaS techniques. The findings underscore an urgent need for collaborative defense mechanisms between AI providers, researchers, and policymakers to address this growing threat. This work contributes a comprehensive taxonomy of the JaaS ecosystem and provides actionable insights for developing robust countermeasures against commercialized AI exploitation.

**Решение:** -4 исследование угроз Jailbreak-as-a-Service, кибербезопасность

---

### 120 · R1621

**Large Language Model-Assisted Thematic Coding in Medical Education Research: Comparative Methodological Study.**

2026 · JMIR formative research · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.2196/85572

Abstract Background While large language model (LLM)–assisted qualitative analysis could improve the efficiency and scalability of feedback-driven curricular refinement in medical education, how best to leverage LLMs for qualitative analysis while ensuring quality outputs remains an open question. Prior work has demonstrated the feasibility of using LLMs for inductive and deductive coding tasks, but more needs to be known about how LLM-assisted thematic coding can best be deployed in a medical education context to maximize its strengths and guard against its weaknesses. Objective Our study evaluated LLM performance in inductive code generation and in the deductive application of a human codebook, using a student focus-group transcript, to propose a model for AI collaboration in qualitative analysis. Methods The qualitative data for this study consisted of a 1-hour focus group with 4 second-year medical students discussing a required AI-driven clinical-scenario tool (2-Sigma). Three human coders conducted an inductive thematic analysis. Using the same transcript, GPT-4o (version gpt-4o-2024-11-20; OpenAI) generated inductive codes and applied the human codebook deductively. The researchers compared the alignment between the AI inductive codes and the human consensus codebook using 3 categories: agreement, reasonable alternative, and not reasonable. Interrater reliability of AI deductive coding was evaluated using percent agreement and Cohen κ, with textual audits of discrepancies, including “misses” (failed to apply appropriate codes) and “misfires” (inappropriately applied codes). Analysis took place between February and July 2025. Results In the inductive condition, GPT-4o generated 137 initial codes, of which 31.4% (n=43) demonstrated agreement with human codes, 26.3% (n=36) represented reasonable alternatives, and 42.3% (n=58) were classified as not reasonable. In the deductive condition, mean percent agreement for AI application of human codes was 96% (SD 4%, range 79%‐100%) and the mean κ was 0.71 (SD 0.26, range 0‐1.00). Of all 2352 coding decisions, there were 57 (2.4%) misfires and 28 (1.2%) misses; common patterns included overinterpretation of tone, failure to recognize continued ideas across excerpts, and difficulty distinguishing hypothetical vs experienced features. Based on our findings, we suggest a roadmap that retains human interpretive control while leveraging AI scalability: humans first develop a contextually grounded codebook through inductive analysis, then use AI both as a creative partner to surface alternative codes and as a tool to apply the validated codebook across the dataset. Conclusions With targeted human oversight, an LLM reliably applied an existing codebook and generated additional inductive codes. These findings support a proposed workflow in which AI serves as an additional perspective within human-driven qualitative analysis, offering a scalable adjunct for qualitative analysis in medical education. Validation across larger and more diverse datasets will help confirm the generalizability of this approach.

**Решение:** -4 тематическое кодирование фокус-групп студентов-медиков об образовательном инструменте

---

### 121 · R10875

**Training LLMs to Recognize Hedges in Dialogues about Roadrunner Cartoons**

2024 · Annual Meeting of the Special Interest Group on Discourse and Dialogue · journalarticle, conference-paper · en · https://doi.org/10.18653/v1/2024.sigdial-1.18

Hedges allow speakers to mark utterances as provisional, whether to signal non-prototypicality or “fuzziness”, to indicate a lack of commitment to an utterance, to attribute responsibility for a statement to someone else, to invite input from a partner, or to soften critical feedback in the service of face management needs. Here we focus on hedges in an experimentally parameterized corpus of 63 Roadrunner cartoon narratives spontaneously produced from memory by 21 speakers for co-present addressees, transcribed to text (Galati and Brennan, 2010). We created a gold standard of hedges annotated by human coders (the Roadrunner-Hedge corpus) and compared three LLM-based approaches for hedge detection: fine-tuning BERT, and zero and few-shot prompting with GPT-4o and LLaMA-3. The best-performing approach was a fine-tuned BERT model, followed by few-shot GPT-4o. After an error analysis on the top performing approaches, we used an LLM-in-the-Loop approach to improve the gold standard coding, as well as to highlight cases in which hedges are ambiguous in linguistically interesting ways that will guide future research. This is the first step in our research program to train LLMs to interpret and generate collateral signals appropriately and meaningfully in conversation.

**Решение:** -4 лингвистический анализ прагматических маркеров (hedges) в описании мультфильмов

---

### 122 · R12089

**Jailbreak Attacks and Defenses against Multimodal Generative Models: A Survey**

2024 · arXiv (Cornell University) · journalarticle, review, preprint/article · en · https://doi.org/10.48550/arxiv.2411.09259

The rapid evolution of multimodal foundation models has led to significant advancements in cross-modal understanding and generation across diverse modalities, including text, images, audio, and video. However, these models remain susceptible to jailbreak attacks, which can bypass built-in safety mechanisms and induce the production of potentially harmful content. Consequently, understanding the methods of jailbreak attacks and existing defense mechanisms is essential to ensure the safe deployment of multimodal generative models in real-world scenarios, particularly in security-sensitive applications. To provide comprehensive insight into this topic, this survey reviews jailbreak and defense in multimodal generative models. First, given the generalized lifecycle of multimodal jailbreak, we systematically explore attacks and corresponding defense strategies across four levels: input, encoder, generator, and output. Based on this analysis, we present a detailed taxonomy of attack methods, defense mechanisms, and evaluation frameworks specific to multimodal generative models. Additionally, we cover a wide range of input-output configurations, including modalities such as Any-to-Text, Any-to-Vision, and Any-to-Any within generative systems. Finally, we highlight current research challenges and propose potential directions for future research. The open-source repository corresponding to this work can be found at https://github.com/liuxuannan/Awesome-Multimodal-Jailbreak. ongoing work

**Решение:** -1 обзор литературы по мультимодальным джейлбрейкам

---

### 123 · R9014

**Large Language Models as Narrative-Driven Recommenders**

2025 · arXiv (Cornell University) · book, journalarticle, conference · en · https://doi.org/10.1145/3696410.3714668

Narrative-driven recommenders aim to provide personalized suggestions for user requests expressed in free-form text such as "I want to watch a thriller with a mind-bending story, like Shutter Island." Although large language models (LLMs) have been shown to excel in processing general natural language queries, their effectiveness for handling such recommendation requests remains relatively unexplored. To close this gap, we compare the performance of 38 open- and closed-source LLMs of various sizes, such as LLama 3.2 and GPT-4o, in a movie recommendation setting. For this, we utilize a gold-standard, crowdworker-annotated dataset of posts from reddit's movie suggestion community and employ various prompting strategies, including zero-shot, identity, and few-shot prompting. Our findings demonstrate the ability of LLMs to generate contextually relevant movie recommendations, significantly outperforming other state-of-the-art approaches, such as doc2vec. While we find that closed-source and large-parameterized models generally perform best, medium-sized open-source models remain competitive, being only slightly outperformed by their more computationally expensive counterparts. Furthermore, we observe no significant differences across prompting strategies for most models, underscoring the effectiveness of simple approaches such as zero-shot prompting for narrative-driven recommendations. Overall, this work offers valuable insights for recommender system researchers as well as practitioners aiming to integrate LLMs into real-world recommendation tools. Under review; 19 pages

**Решение:** -4 рекомендательная система фильмов по текстовым запросам

---

### 124 · R9360

**Evaluating Large Language Models for Enhancing Live Chat Therapy: A Comparative Study with Psychotherapists**

2025 · Annual Meeting of the Special Interest Group on Discourse and Dialogue · journalarticle, conference-paper · https://doi.org/10.18653/v1/2025.sigdial-1.59

Large Language Models (LLMs) hold promise for addressing the shortage of qualified therapists in mental health care. While chatbot-based Cognitive Behavioral Therapy (CBT) tools exist, their efficacy in sensitive contexts remains underexplored. This study examines the potential of LLMs to support therapy sessions aimed at reducing Child Sexual Abuse Material (CSAM) consumption. We propose a Retrieval-Augmented Generation (RAG) framework that leverages a fine-tuned BERT-based retriever to guide LLM-generated responses, better capturing the multi-turn, context-specific dynamics of therapy. Four LLMs—Qwen2-7B-Instruct, Mistral-7B-Instruct-v0.3, Orca-2-13B, and Zephyr-7B-Alpha—were evaluated in a small-scale study with 14 domain-expert psychotherapists. Our comparative analysis reveals that, in certain scenarios, LLMs like Mistral-7B-Instruct-v0.3 and Orca-2-13B were preferred over human therapist responses. While limited by sample size, these findings suggest that LLMs can perform at a level comparable to or even exceeding that of human therapists, especially in therapy focused on reducing CSAM consumption. Our code is available online. 1

**Решение:** -2 психотерапевты оценивают качество реплик LLM в чат-терапии при потреблении CSAM

---

### 125 · R11044

**NovelQA: Benchmarking Question Answering on Documents Exceeding 200K Tokens**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2403.12766

Recent advancements in Large Language Models (LLMs) have pushed the boundaries of natural language processing, especially in long-context understanding. However, the evaluation of these models' long-context abilities remains a challenge due to the limitations of current benchmarks. To address this gap, we introduce NovelQA, a benchmark tailored for evaluating LLMs with complex, extended narratives. Constructed from English novels, NovelQA offers a unique blend of complexity, length, and narrative coherence, making it an ideal tool for assessing deep textual understanding in LLMs. This paper details the design and construction of NovelQA, focusing on its comprehensive manual annotation process and the variety of question types aimed at evaluating nuanced comprehension. Our evaluation of long-context LLMs on NovelQA reveals significant insights into their strengths and weaknesses. Notably, the models struggle with multi-hop reasoning, detail-oriented questions, and handling extremely long inputs, with average lengths exceeding 200,000 tokens. Results highlight the need for substantial advancements in LLMs to enhance their long-context comprehension and contribute effectively to computational literary analysis. Accepted by ICLR-2025

**Решение:** -4 литературные вопросы и ответы по длинным художественным текстам (NovelQA)

---

### 126 · R8018

**THE IMPACT OF MORPHOSYNTACTIC FEATURES ON AI-GENERATED TEXTS**

2025 · English Review Journal of English Education · journalarticle, article · en · https://doi.org/10.25134/k9x3sr16

This study explored the impact of morphosyntactic features on AI-generated text, focusing on how morphological complexity and syntactic structure influence large language model (LLM) performance in terms of response quality, coherence, and processing efficiency. A mixed-methods design was adopted, combining quantitative computational evaluation with qualitative linguistic analysis. Experimental procedures involved constructing 60 prompts with controlled variations in morphological complexity (simple vs. complex derivational forms, e.g., nationalization, reindustrialization) and syntactic structure (single-clause, multi-clause, and compound-complex sentences). Each prompt was submitted to three state-of-the-art LLMs under identical conditions (temperature = 0.7, top-p = 0.9, max tokens = 512). Outputs were assessed using automated metrics (BLEU, ROUGE-L, perplexity) and human-rated coherence scores from three trained linguists, with inter-rater reliability measured by Cronbach’s alpha (≥ 0.80). Statistical analysis employed two-way ANOVA with post-hoc Tukey HSD tests, reporting effect sizes (η²) and using α = 0.05. Results showed that morphologically complex prompts generated 27% more contextually rich responses, with average processing times 34% longer and perplexity scores 35% higher than simpler inputs. Complex multi-clause prompts achieved coherence scores 18% higher than single-clause prompts, while compound-complex structures produced the most accurate outputs but required 38% more processing time and 21% more computational resources. Prompts combining both morphological and syntactic complexity yielded the highest quality (coherence scores 25% above mean) but also the highest computational cost, reflecting increased cognitive load. Prompts that combined both complex morphological and syntactic elements demonstrated the highest overall quality, with coherence scores 25% above average, but also the greatest computational demand, reflecting the cognitive load required for deep linguistic processing. These findings underscore the importance of carefully balancing morphological and syntactic complexity in prompt design, depending on the specific goals of the application.

**Решение:** -2 лингвисты оценивают связность текста, сгенерированного LLM

---

### 127 · R5414

**When AI Sounds Supportive: Comparing Conversational AI and Therapist Responses to Mental Health Disclosures**

2026 · Counselling and Psychotherapy Research · journalarticle, article · en · https://doi.org/10.1002/capr.70237

ABSTRACT Objectives To compare artificial intelligence (AI) and therapist responses to real‐world mental health (MH) disclosures and evaluate differences in empathy, safety practices and contextual usefulness. Methods We analysed 937 unique MH disclosures and 2749 therapist responses using the Counsel Chat dataset. For each disclosure, we generated a standardised AI response using a large language model. Responses were evaluated across empathy, safety and contextual usefulness measures using automated metrics, blinded human ratings of 120 therapist‐AI response pairs, mixed effects regression models, and qualitative analyses of disagreement cases. Results AI responses scored higher than therapist responses on automated empathy ( β = 0.30; p < 0.001), human‐rated empathy ( β = 0.38; p < 0.001), emotional validation ( β = 0.40; p < 0.001) and automated safety ( β = 0.25; p < 0.001). AI safety advantages were largest for self‐harm or suicide‐related disclosures. Therapists scored higher on specificity/personalisation ( β = −0.62; p < 0.001) and helpfulness ( β = −0.23; p = 0.013); overall quality did not differ significantly. Conclusions As conversational AI becomes an increasingly common source of MH support, AI responses may offer strengths in empathic communication and explicit safety‐oriented guidance, whereas therapist responses were rated more highly for personalisation and contextual usefulness. These findings highlight different strengths across AI and therapist responses while underscoring the need for caution in interpreting response quality as clinical effectiveness. They also point to a potential role for conversational AI as an accessible first point of support within broader MH care systems, particularly where timely professional support is limited.

**Решение:** -2 эксперты оценивают эмпатию и безопасность терапевтических ответов LLM

---

### 128 · R5765

**Evaluating large language models for patient consultations on osteoporotic vertebral compression fractures: a two-phase comparative study**

2026 · Journal of Orthopaedic Surgery and Research · article · en · https://doi.org/10.1186/s13018-026-07185-5

To evaluate the quality, readability, error patterns, and expert-rated response safety of large language model–generated information for patients with osteoporotic vertebral compression fractures (OVCFs), and to explore differences between a selected model and a spine surgeon in a simulated written consultation setting. This two-phase sequential benchmarking study evaluated ChatGPT-5.1, Gemini 2.5 Pro, DeepSeek-V3.2, and Qwen3-Max. In Phase 1, the four models answered 26 expert-developed OVCF questions. Three senior spine surgeons independently rated accuracy, comprehensiveness, and expert-rated response safety using predefined 5-point criteria. Response length, readability, aggregate model-ranking concordance, and predefined error categories were also assessed. In Phase 2, ChatGPT-5.1 and one spine surgeon independently answered 17 de-identified patient-derived questions using the same standardized instruction. Accuracy, comprehensiveness, and expert-rated response safety were evaluated by two senior spine surgeons through consensus, whereas empathy and usability were rated by one researcher. Friedman and paired Wilcoxon signed-rank tests were used, with Benjamini–Hochberg correction for multiple comparisons. In Phase 1, the four models differed in accuracy (Friedman χ 2 (3) = 12.64, P = 0.00548, Kendall’s W = 0.162), comprehensiveness (χ 2 (3) = 38.68, P = 2.03 × 10 −8 , W = 0.496), and expert-rated response safety (χ 2 (3) = 19.86, P = 0.000182, W = 0.255). After multiplicity correction, ChatGPT-5.1 and DeepSeek-V3.2 generally received higher ratings than Gemini 2.5 Pro, although several comparisons with Qwen3-Max were not statistically significant. Omission errors occurred across all four models. In Phase 2, no statistically significant difference was detected between ChatGPT-5.1 and the physician comparator in accuracy (paired mean difference, 0.24; 95% CI − 0.12 to 0.59; adjusted P = 0.2482) or expert-rated response safety (difference, 0.53; 95% CI − 0.06 to 1.12; adjusted P = 0.1469). ChatGPT-5.1 received higher ratings for comprehensiveness, researcher-rated empathy, and usability (adjusted P = 0.0012, 0.0011, and 0.0012, respectively) and had lower estimated reading-grade requirements. ChatGPT-5.1 and DeepSeek-V3.2 generated structured OVCF patient-education content with favorable expert ratings, but clinically relevant omissions remained. The exploratory Phase 2 comparison involved only 17 questions and one physician comparator and did not establish equivalence, noninferiority, or real-world clinical safety. LLMs may support clinician-supervised patient education and communication but should not replace diagnosis, imaging interpretation, individualized risk assessment, procedural decision-making, or complication management.

**Решение:** -4 вертебрология/ортопедия, оценка хирургических консультаций LLM

---

### 129 · R7873

**Ethnochemical Reconstruction of Dayak Tomun Tuak Fermentation for Contextual Chemistry Learning: an Applied Ethnography with AI-Augmented Qualitative Analysis**

2025 · IJPTE International Journal of Pedagogy and Teacher Education · journalarticle, article · https://doi.org/10.20961/ijpte.v9i2.110383

This study integrates AI-augmented qualitative analysis into an applied-ethnographic reconstruction of Dayak Tomun tuak fermentation to address the lack of curriculum-ready, place-based chemistry materials. Fieldwork in Arut Selatan, Central Kalimantan (August 2024–January 2025) engaged two participants (one brewer, one customary leader) through structured observation, semi-structured narrative interviews, and audiovisual documentation under inclusion criteria of ≥10 years’ practice and consistent use of traditional methods. Within Google Colab, ChatGPT assisted transcript segmentation and first-pass open–axial–selective coding; researchers verified all outputs line by line and iteratively refined a codebook with an audit trail. Findings clarify a two-stage process: glutinous-rice tapai for approximately 2–3 days followed by fermentation of a cooled sugar-and-spice infusion for approximately 4–5 days. Three controls consistently mattered: cooling to hand-warm (≤35 °C) before inoculation, tightly sealed vessels for defined durations, and spice infusion (clove, cinnamon, nutmeg, long pepper, black pepper) for flavor and perceived “cleanliness.” Sensory shift from sweet to bitter aligned with community assessments of progress; sociocultural boundaries (acid exclusion, restricted access, optional kapur sirih markings) co-occurred with empirical controls. We provide four curriculum-aligned exemplars for Grades 10–11: stoichiometry and reaction progress with simulated sucrose musts; anaerobiosis and gas balance via sealed-jar CO₂ capture; phenolic antioxidant assays (DPPH) using culinary spices with safety notes; and pH-shift demonstrations framed by the acid-exclusion hypothesis. Limitations include no instrumental ABV, pH, or microbiome data; pathway figures are interpretive. Future work should prioritize spot pH/Brix and hydrometer ABV, along with microbiome–metabolome mapping to strengthen the scientific and educational bridge.

**Решение:** -4 этнохимическое исследование традиционного брожения напитка туак

---

### 130 · R6233

**La colaboración humano-IA como estrategia metodológica para el desarrollo de la creatividad en la educación cultural y artística**

2026 · Dialnet (Universidad de la Rioja) · article · es · https://dialnet.unirioja.es/descarga/articulo/10764175.pdf

This article analyzes human-artificial intelligence (AI) collaboration as an innovative methodological strategy for developing creativity in cultural and artistic education. Through a mixed-methods and exploratory research design with 60 secondary school students, the impact of integrating generative AI tools into the artistic creation process was evaluated. The quantitative results, obtained using the Consensus Assessment Technique, demonstrated a statistically significant improvement in the originality, technical feasibility, and conceptual depth of the works. Qualitatively, reflective journals and focus groups revealed that AI acts as a cognitive scaffold that reduces anxiety when faced with a blank canvas and fosters divergent thinking. A redefinition of authorship was also observed, with students assuming the role of art director, along with an increase in critical thinking by detecting and confronting algorithmic biases. It is concluded that this synergy democratizes artistic expression and enhances aesthetic curation, although the challenge of conveying genuine emotional expressiveness remains fundamentally dependent on human sensitivity.

**Решение:** -4 применение генеративного ИИ в школьном художественном образовании

---

### 131 · R3178

**Quality and readability of AI-generated information on bipolar disorder: a cross-sectional content analysis.**

2026 · BMC psychiatry · collection/collection, journal article, journalarticle · eng · https://doi.org/10.1186/s12888-026-08262-z

Abstract Background Bipolar disorder is a clinically sensitive and diagnostically complex condition in which unclear or incomplete psychoeducational information may contribute to misunderstanding of symptoms, delayed help-seeking, and unsafe interpretation of treatment options. Large language models are increasingly used as on-demand sources of mental health information, yet comparative evidence on the quality and readability of AI-generated information about bipolar disorder remains limited. Methods This cross-sectional content analysis evaluated 180 responses generated by ChatGPT, Gemini, and DeepSeek to 20 bipolar disorder-related questions derived from Google Trends. Each question was asked in three independent new sessions for each model. Information quality was assessed using the 20-item EQIP instrument, and readability was evaluated using Flesch-Kincaid Grade Level, Flesch Reading Ease, and word count. To address the non-independence of repeated responses nested within prompts, a linear mixed-effects model was used with AI model and question category as fixed effects and question ID as a random intercept. Results In the mixed-effects analysis, AI model significantly predicted EQIP scores. Compared with ChatGPT, Gemini and DeepSeek generated higher EQIP scores, with DeepSeek showing the largest estimated difference. Question category also contributed to information quality, although category-level pairwise comparisons did not remain significant after Bonferroni adjustment. Higher EQIP scores were moderately associated with longer responses and more favorable readability indices. Inter-rater analyses showed moderate absolute agreement for total EQIP scores and variable item-level agreement. Conclusions Within the specific models, access conditions, prompts, date, and settings tested in this study, AI-generated bipolar disorder information differed across models in EQIP-rated quality and readability. These findings should be interpreted as content-quality findings rather than evidence of clinical accuracy, safety, or patient benefit. AI-generated psychoeducation should therefore be treated as a supplementary information source requiring expert review rather than a replacement for clinician-guided education.

**Решение:** -2 оценка людьми качества и удобочитаемости сгенерированной информации о биполярном расстройстве (EQIP)

---

### 132 · R8621

**A policy framework for leveraging generative AI to address enduring challenges in clinical trials**

2025 · npj Digital Medicine · article · en · https://doi.org/10.1038/s41746-025-01440-5

As the primary tool for validating new treatments, clinical trials are integral to evidence-based medicine and medical progress, playing a pivotal role in determining the safety and efficacy of new therapeutic interventions, including drugs, medical devices, and clinical procedures. But despite their central role and the vast resources devoted to them, studies from Cochrane reviews—widely regarded as the gold standard—indicate that over 40% of these trials are ‘wasted’ due to suboptimal protocols, a situation deemed ‘ethically, scientifically, and economically indefensible’ 1 . Three of the most common deficiencies concern blinding of patients and personnel, blinding of outcome assessment and incomplete outcome data (see Table 1 for a comprehensive overview of deficiencies) 1 , 2 , 3 . Although initiatives such as enhanced training and targeted funding have been proposed to overcome deficiencies, tangible progress remains insufficient 3 . Can artificial intelligence (AI) help address some of these enduring challenges?

**Решение:** -1 политико-регуляторный фреймворк для клинических испытаний

---

### 133 · R10066

**Exploring Large Language Models for Grammar Error Explanation and Correction in Indonesian as a Low-Resource Language**

2025 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-981-95-3343-5_43

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 объяснение грамматических ошибок, лингвистика/педагогика

---

### 134 · R11566

**ChatGPT as a Text Annotation Tool to Evaluate Sentiment Analysis on South African Financial Institutions**

2024 · IEEE Access · journalarticle, review, article · en · https://doi.org/10.1109/access.2024.3464374

Social media platforms play a significant role in analyzing customer perceptions of financial products and services in today’s culture. These platforms facilitate the immediate and in-depth sharing of thoughts and experiences, offering valuable insights into consumer behaviour. Any customer looking for such a service would surf the internet for reviews and ratings before making a decision, which usually influences their ultimate pick. Feedback and suggestions from friends, family, and coworkers improve customer experiences. Customer reviews play a crucial role in shaping the reputation and profitability of businesses and products offered by financial institutions, often serving as the final assessment of quality and satisfaction during decision-making. Therefore, it is paramount for decision-makers to carefully evaluate customer feedback and understand the sentiment expressed in a given piece of text, which could lead to equity trading, and credit market assessment, and offer invaluable insights that boost the financial performance of the institution. Previous research has used human-annotated text, such as lexicon-based methods, to train machine learning models for sentiment analysis, but the approach did not capture the full range of structure and semantic relationships in natural language. Therefore, our research aims to develop a more comprehensive and accurate sentiment analysis model using advanced natural language processing techniques that could answer questions on various subjects and tasks. To do this, we first crawled customer reviews on Hellopeter, a popular review site, and financial data on the top five financial institutions listed on the Johannesburg Stock Exchange (JSE) in South Africa. After that, we used OpenAI’s ChatGPT as a zero-short learning model to generate human-like annotation tools for different sentiment tasks. The OpenAI ChatGPT feature vector was subsequently fed into BERT, BiLSTM, and a SoftMax function to detect and identify the sentiment of a given sentence. Lastly, we use feature vectors with oversampling methods to address the imbalanced data dilemma and visualise the contribution features of the given piece of text for the customer reviewers. The experiments demonstrated that the method performed as well as or better than the latest and most effective methods on the tested datasets, yielding comparable results. When OpenAI’s ChatGPT was combined with pre-trained BERT and BiLSTM models, it did better overall, with an average score of 98.9%, an F1-measure of 97.7%, and an AUC of 91.90% when oversampling was used. The traditional lexicon-based model got an 86.68% score using SVM and logistic regression and an AUC of 91.90%. The study shows the exceptional performance of OpenAI ChatGPT in detecting the emotional tone or polarity of a given sentence in a customer review, which helps with annotation and understanding the sentiment analysis of an event and how it influences decisions and outcomes. In conclusion, these results underscore the significant advantages of incorporating customer sentiment analysis into financial analysis and decision-making processes as a valuable tool for understanding and prioritizing customer needs and preferences.

**Решение:** -4 анализ тональности отзывов о финансовых продуктах

---

### 135 · R5267

**Quotient Critical Geometry: Collapse-Time Laws and Bifurcated Failure Modes in Affective Governance**

2026 · Zenodo · text/working paper · https://doi.org/10.5281/zenodo.20029159

This paper formalizes collapse risk in adaptive governance systems as a quotient geometry in loading–resilience space. Rather than treating collapse as a function of load, misalignment, or endurance alone, the paper defines the collapse-control parameter κ(t)=A(t)/H(t)=S(t)δ(t)/H(t)\kappa(t)=A(t)/H(t)=S(t)\delta(t)/H(t)κ(t)=A(t)/H(t)=S(t)δ(t)/H(t), where instability, misalignment, and affective endurance jointly determine proximity to collapse. The paper derives collapse-time laws under quasi-static loading, showing how time-to-collapse depends on the initial quotient state, the critical threshold, and the depletion rate of affective endurance. It also corrects the critical interaction-density relation, showing that stronger misalignment coupling lowers the safe coordination density, while higher capacity and endurance raise it. A central contribution is the classification of Freeze and Runaway as the two primitive collapse-mode classes of affective governance systems. Freeze corresponds to suppressed excitation gain and silent criticality, while Runaway corresponds to amplification cascades under preserved or elevated sensitivity. Mixed-mode collapses are treated as composite regimes composed of local Freeze and Runaway dynamics. Controlled mechanism tests support the associated predictions, including critical slowing down, finite-size scaling, and early-warning behavior. The paper positions quotient critical geometry as the formal collapse-law layer of the broader AGP/AGM series. AI use disclosure. Generative AI (OpenAI GPT) was used substantively in preparing this work, including source comparison, drafting and editing, and, where applicable, mathematical and counterexample checks and the writing and running of supplementary code. The research questions, framework and final claims were directed and reviewed by the author, who takes full responsibility for the content, including the accuracy of all references and reported numbers.

**Решение:** -4 математическое моделирование критической геометрии коллапса

---

### 136 · R4587

**Investigating automated change analysis in FinTech regulations**

2026 · Information and Software Technology · journalarticle, article · en · https://doi.org/10.1016/j.infsof.2026.108144

Context: Software systems in regulated domains must continually adapt to legal changes, yet practitioners often handle updates manually with limited support, making compliance work costly and error prone. Recent advances in LLMs prompt the question of how automation can reliably assist this process. Objectives: We aim to (1) characterize the nature of regulatory changes and derive a systematic taxonomy, (2) understand through the lens of practitioners where automation is most useful, and (3) assess the feasibility of using LLMs for detecting and classifying regulatory changes. Method: We conducted a mixed-methods study grounded in the German social security (DEÜV) in collaboration with practitioners from a FinTech company. First, we developed a taxonomy of regulatory changes through manual document analysis of four Regulatory Implementation Specifications (RIS), followed by a workshop and expert interviews. Second, we validated the taxonomy and elicited challenges through semi-structured practitioner interviews. Third, we built a gold-standard dataset of 93 annotated change instances and evaluated seven state-of-the-art LLMs within an automated detection and classification pipeline. Results: The taxonomy defines five change scopes and four optional context dimensions. Practitioners found it intuitive and useful for filtering relevant changes, particularly Data and Field updates, but reported challenges such as tight deadlines, legal ambiguity, limited traceability, and overlapping categories. In automation, proprietary LLMs performed best, while performance dropped on narrative or weakly structured documents, highlighting sensitivity to document format. Conclusion: The proposed taxonomy provides a practical lens for organizing regulatory change information, and LLMs can support the identification and classification of recurring, structurally explicit changes. Their limitations on context-dependent and infrequent categories suggest that automation should complement, rather than replace, expert assessment, motivating future work on human-in-the-loop compliance tooling across broader regulatory ecosystems.

**Решение:** -4 программный анализ финтех-регулирования

---

### 137 · R12404

**Haiku Generation with Large Language Models**

2023

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 генерация стихотворений хайку, литература

---

### 138 · R3421

**Which Neurons Detect Malicious Code? A Probing Study of LLM Security Knowledge**

2026 · arXiv (Cornell University) · conferencepaper/emerging results, vision & reflection track paper, journalarticle, preprint/article · en · https://doi.org/10.4230/lipics.esem.2026.70

Background. Large language models (LLMs) have become increasingly capable of understanding and generating source code, leading to their widespread adoption in software engineering tasks such as code completion, repair, and vulnerability detection. However, despite their strong empirical performance, the internal mechanisms through which LLMs recognize malicious or vulnerable code patterns remain poorly understood. Aim. We investigated where the malware detection behavior is encoded inside LLMs Feed Forward Network (FFN) neurons and verified the attribution with causal interventions on the neurons identified. This aims to identify the most important neurons in detecting malicious code. Methods. We applied mechanistic interpretability methods to locate the neurons being responsible for malware-detection behavior in three instruction-tuned LLMs: Llama3.1-8B-Instruct, Mistral-v0.3-7B-Instruct, and Qwen2.5-7B-Instruct. Using 1,500 malicious and 1,500 benign PyPI packages from the PyPI Malregistry, we attribute the behavior to a set of neurons. Results. The experimental results reveal that amplifying facilitating neurons for malware detection while suppressing inhibiting ones can boost accuracy, while the reverse collapses predictions toward a single class, although the magnitude and consistency is heavily model-dependent. We demonstrated that the guardrail detection mechanism varies across models, each represents its malware detection behavior differently within its FFN layers. Conclusions. Probing the neurons associated with security-relevant knowledge helps us gain insights into how LLMs encode malicious programming concepts, identify potentially harmful memorized behaviors, paving the way toward more reliable defense mechanisms, such as neuron-level editing, selective unlearning, and security-aware alignment for code-focused LLMs. The paper has been peer reviewed and accepted for publication in the 20th International Symposium on Empirical Software Engineering and Measurement (ESEM 2026)

**Решение:** -4 детектирование вредоносного кода нейронами LLM, кибербезопасность

---

### 139 · R2229

**Feasibility and user evaluation of HopeBot: An LLM-powered conversational chatbot for depression screening.**

2026 · PLOS digital health · journal article, journalarticle, review · eng · https://doi.org/10.1371/journal.pdig.0001446

Clinician-administered Patient Health Questionnaire-9 (PHQ-9) interviews allow clarification of ambiguous responses but are resource-intensive and difficult to scale for routine use. Self-administered versions are widely adopted for depression screening yet offer little opportunity for interaction or clarification, which may limit engagement and scoring accuracy. We developed HopeBot, a conversational chatbot powered by a large language model (LLM) that delivers the PHQ-9 via text or voice, providing real-time clarification and safety guidance through a retrieval-augmented generation (RAG) layer drawing on validated psychological and helpline resources. The system aims to extend access to structured screening rather than replace clinician judgment. In a within-subject feasibility study, 132 adults from two countries completed both self-administered and chatbot-assisted PHQ-9 assessments followed by a 25-item evaluation survey. Chatbot and self-report scores showed high concordance (intraclass correlation coefficient = 0.92; median absolute difference = 1 point), indicating faithful replication of scoring. Of these participants, 75 completed a comparative feedback module (most with identical scores were not prompted for comparison); 71% (n = 53) reported greater confidence in chatbot-assisted scores, citing clearer structure, interpretive guidance, and a supportive tone. Mean usability ratings (0-10) were 8.4 for comfort, 7.7 for voice clarity, 7.6 for handling sensitive topics, and 7.4 for recommendation helpfulness; the latter varied significantly by employment status and prior experience with mental-health services. The self-administered PHQ-9 served as a pragmatic comparator reflecting real-world digital screening, allowing evaluation of whether the chatbot could faithfully reproduce the questionnaire's structure and scoring accuracy rather than diagnostic validity. These findings indicate that an LLM-powered conversational agent with RAG-based grounding can feasibly and acceptably administer the PHQ-9 with strong score concordance relative to self-report, suggesting potential as a scalable adjunct for early, low-burden depression screening. Further validation against clinician-administered assessments in real-world workflows is warranted. Trial registration ClinicalTrials.gov Identifier NCT06801925.

**Решение:** -3 скрининг депрессии HopeBot: сопоставление со стандартным самоотчетом PHQ-9 (критериальная валидность)

---

### 140 · R5571

**Auditing Disability Representation in Vision-Language Models**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.17348

Vision-language models (VLMs) are increasingly deployed in socially sensitive applications, yet their behavior with respect to disability remains underexplored. We study disability aware descriptions for person centric images, where models often transition from evidence grounded factual description to interpretation shift including introduction of unsupported inferences beyond observable visual evidence. To systematically analyze this phenomenon, we introduce a benchmark based on paired Neutral Prompts (NP) and Disability-Contextualised Prompts (DP) and evaluate 15 state-of-the-art open- and closed-source VLMs under a zero-shot setting across 9 disability categories. Our evaluation framework treats interpretive fidelity as core objective and combines standard text-based metrics capturing affective degradation through shifts in sentiment, social regard and response length with an LLM-as-judge protocol, validated by annotators with lived experience of disability. We find that introducing disability context consistently degrades interpretive fidelity, inducing interpretation shifts characterised by speculative inference, narrative elaboration, affective degradation and deficit oriented framing. These effects are further amplified along race and gender dimension. Finally, we demonstrate targeted prompting and preference fine-tuning effectively improves interpretive fidelity and reduces substantially interpretation shifts.

**Решение:** -4 аудит репрезентации инвалидности в мультимодальных моделях

---

### 141 · R8628

**Leveraging Public Large Language Models for Coding Conflict Event Data: A Case Study Using ACLED Data from the Syrian Civil War**

2025 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.5938594

Methods for large-scale qualitative coding of conflict data conventionally have a major tradeoff in approaches: the traditional manual coding is time-intensive, whereas the rule-based coding often fails to capture contextual complexities in event narratives. This study presents a novel application of a Large Language Model (LLM) to qualitatively code over 140,000 civil warrelated incidents from the Armed Conflict Location &amp;amp; Event Data Project (ACLED). We assess the model's capacity to extract and classify contextual details such as targeting patterns, and violence severity from multi-sourced event descriptions, comparing its performance to rulebased models. The paper provides an in-depth discussion of prompt development, validation strategies, some of the challenges we experienced, and our solutions. Our results demonstrate the LLM's adaptability, scalability, and capacity to interpret linguistic variation in conflict data. Beyond offering a practical tool for coding large qualitative datasets, this approach enables conflict researchers to systematically analyze dimensions of violence that were previously accessible only through resource-intensive large projects or small-N case studies.

**Решение:** -4 качественное кодирование вооруженных конфликтов по базе ACLED

---

### 142 · R4210

**IPO Finance Agent: Benchmark of LLM Financial Analysts Beyond Finance Agent v2, with Automated Rubric Generation, on the SpaceX (SPCX) IPO**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · en · https://doi.org/10.48550/arxiv.2606.23032

Finance Agent v2 (by Vals AI) has emerged as the reference benchmark for evaluating both Anthropic Claude and OpenAI ChatGPT frontier language models on financial tasks. However, it narrowly deals with periodic reporting from publicly traded companies (SEC 10-K and 10-Q filings), and its agentic harness relies on naive, unenriched chunk retrieval. Neither the task design nor the retrieval approach addresses the distinct challenges of IPO due diligence. SEC S-1 filings combine historical financial statements, governance structures, pro forma and common-control accounting treatments, capital-formation narratives, and underwriting-sensitive risk disclosures within substantially longer documents than typical periodic filings. That is why we introduce IPO Finance Agent, which extends the Finance Agent v2 framework along two directions: task domain and retrieval architecture. During our experiments, the original Finance Agent v2 harness basically failed to deliver any output related to the SpaceX S-1 filing, due to document length. We therefore had to improve the agentic harness with contextual retrieval, a more realistic and industry-standard approach for long documents. We also built a dataset of 1,000 IPO-diligence questions, and publicly release 70 questions on the SpaceX (SPCX) S-1 filing to support reproducibility, while the remainder are held private to guard against benchmark contamination. In addition, we introduce an evaluator-optimizer pipeline to automatically generate evaluation rubrics for the benchmark: candidate facts are extracted from model answers, consolidated into draft criteria, then automatically audited for omissions, hallucinations, mistiered items, and redundancy, with LLM feedback driving iterative repair, targeted enrichment, and deduplication. Human experts only review final rubrics before deployment. Results show that the best-performing evaluated model, Zhipu GLM-5.2, reaches 79.8% accuracy, and the most cost-efficient model on the resulting Pareto frontier, Xiaomi MiMo-2.5 Pro, reaches slightly lower accuracy (77.2%) at 0.05 USD per query, while exceeding the current Finance Agent v2 leaderboard ceiling, Google Gemini 3.5 Flash at 57.9% for 2.51 USD per query, and undercutting even FABv2's cheapest entry (MiniMax M3: 48.3% at 0.32 USD) on cost-efficiency. Code and data are released on GitHub https://github.com/benstaf/ipoagent

**Решение:** -4 финансовый бенчмарк аналитиков IPO

---

### 143 · R9530

**Large language models for autism: evaluating theory of mind tasks in a gamified environment.**

2025 · Scientific reports · journal article, journalarticle, article · eng · https://doi.org/10.1038/s41598-025-18608-4

Autism Spectrum Disorder often significantly affects reciprocal social communication, leading to difficulties in interpreting social cues, recognizing emotions, and maintaining verbal interactions. These challenges can make everyday conversations especially demanding. To support autistic people in developing their social competence and communication abilities, we propose an interactive game specifically designed to enhance social understanding. By incorporating gamification elements and a user-centered design approach, the application aims to balance clinical relevance with high usability, ensuring it remains accessible, engaging, and beneficial for anyone seeking to improve their social skills. Large Language Models have recently been assessed for their ability to detect sarcasm and irony within Theory of Mind tasks, showing performance comparable to that of trained psychologists. However, a significant limitation remains: their dependence on traditional "black box" AI architectures, which often lack explainability, interpretability, and transparency. This limitation is particularly concerning when people with and without Autism Spectrum Disorder use these models to learn and practice social skills in safe, virtual environments. This study investigates and compares the performance of Large Language Models and human experts in evaluating Theory of Mind tasks, providing a detailed comparative analysis. A total of 21 participants engaged with our game, and their responses were assessed by four human experts alongside GPT-4o. The results indicate that GPT-4o matches human experts in both adherence to instructional criteria and evaluation accuracy, with no statistically significant differences observed. These findings underscore the potential of LLMs to support scalable, always-available social training systems that are accessible from anywhere.

**Решение:** + T2 оценка выполнения заданий на модель психического (Theory of Mind): GPT-4o против четырех экспертов

---

### 144 · R10977

**Assessing the Accuracy of Generative Conversational Artificial Intelligence in Debunking Sleep Health Myths: Mixed Methods Comparative Study With Expert Analysis.**

2024 · JMIR formative research · journal article, journalarticle, article · eng · https://doi.org/10.2196/55762

BACKGROUND: Adequate sleep is essential for maintaining individual and public health, positively affecting cognition and well-being, and reducing chronic disease risks. It plays a significant role in driving the economy, public safety, and managing health care costs. Digital tools, including websites, sleep trackers, and apps, are key in promoting sleep health education. Conversational artificial intelligence (AI) such as ChatGPT (OpenAI, Microsoft Corp) offers accessible, personalized advice on sleep health but raises concerns about potential misinformation. This underscores the importance of ensuring that AI-driven sleep health information is accurate, given its significant impact on individual and public health, and the spread of sleep-related myths. OBJECTIVE: This study aims to examine ChatGPT's capability to debunk sleep-related disbeliefs. METHODS: A mixed methods design was leveraged. ChatGPT categorized 20 sleep-related myths identified by 10 sleep experts and rated them in terms of falseness and public health significance, on a 5-point Likert scale. Sensitivity, positive predictive value, and interrater agreement were also calculated. A qualitative comparative analysis was also conducted. RESULTS: ChatGPT labeled a significant portion (n=17, 85%) of the statements as "false" (n=9, 45%) or "generally false" (n=8, 40%), with varying accuracy across different domains. For instance, it correctly identified most myths about "sleep timing," "sleep duration," and "behaviors during sleep," while it had varying degrees of success with other categories such as "pre-sleep behaviors" and "brain function and sleep." ChatGPT's assessment of the degree of falseness and public health significance, on the 5-point Likert scale, revealed an average score of 3.45 (SD 0.87) and 3.15 (SD 0.99), respectively, indicating a good level of accuracy in identifying the falseness of statements and a good understanding of their impact on public health. The AI-based tool showed a sensitivity of 85% and a positive predictive value of 100%. Overall, this indicates that when ChatGPT labels a statement as false, it is highly reliable, but it may miss identifying some false statements. When comparing with expert ratings, high intraclass correlation coefficients (ICCs) between ChatGPT's appraisals and expert opinions could be found, suggesting that the AI's ratings were generally aligned with expert views on falseness (ICC=.83, P<.001) and public health significance (ICC=.79, P=.001) of sleep-related myths. Qualitatively, both ChatGPT and sleep experts refuted sleep-related misconceptions. However, ChatGPT adopted a more accessible style and provided a more generalized view, focusing on broad concepts, while experts sometimes used technical jargon, providing evidence-based explanations. CONCLUSIONS: ChatGPT-4 can accurately address sleep-related queries and debunk sleep-related myths, with a performance comparable to sleep experts, even if, given its limitations, the AI cannot completely replace expert opinions, especially in nuanced and complex fields such as sleep health, but can be a valuable complement in the dissemination of updated information and promotion of healthy behaviors.

**Решение:** -4 фактчекинг заблуждений о здоровье сна: оценка истинности утверждений

---

### 145 · R8185

**LLM-Based Quality Assessment of Software Architecture Diagrams: A Preliminary Study with Four Open-Source Projects**

2025 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-02138-0_8

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 оценка диаграмм архитектуры программного обеспечения

---

### 146 · R3079

**L’Intelligence artificielle dans les revues systématiques et les méta-analyses : performance spécifique par tâche, quantification de l’erreur résiduelle et supervision humaine**

2026 · Revue de Chirurgie Orthopédique et Traumatologique · article · fr · https://doi.org/10.1016/j.rcot.2026.07.013

Résumé Contexte Le volume des publications scientifiques a augmenté rapidement, renforçant le besoin de synthèses probantes fiables et régulièrement mises à jour. Les revues systématiques (RS) et les méta-analyses (MA) demeurent le plus haut niveau de preuve, mais leur réalisation est longue et coûteuse en ressources, dépassant souvent un an. L’intelligence artificielle (IA) est de plus en plus utilisée pour automatiser les étapes de ce processus, mais la validation de ses performances et de sa rigueur méthodologique reste limitée. Cette revue narrative aborde trois questions : 1) à quelles étapes du processus RS/MA l’IA peut-elle être utilisée de manière fiable ; 2) comment évaluer la performance de l’IA pour chaque tâche ; et 3) comment quantifier l’erreur résiduelle après vérification humaine. Méthodes Nous décrivons les principes et les étapes clés d’une méta-analyse traditionnelle et examinons la contribution de l’IA à chaque étape. La littérature a été issue des principales bases de données biomédicales ; aucune recherche systématique n’a été réalisée. Les performances de l’IA sont résumées par tâche, l’évaluation comparative et la quantification de l’erreur résiduelle étant considérées séparément. Résultats Sur l’ensemble du processus, la maturité de l’IA est hétérogène. Dans une revue systématique de 2025 portant sur 19 études comparatives, l’IA générative a manqué 68,0 % à 96,0 % des études pertinentes lors de la recherche, et a produit des décisions d’inclusion incorrectes dans 0,0 % à 29,0 % des cas, des exclusions incorrectes dans 1,0 % à 83,0 %, des extractions incorrectes dans 4,0 % à 31,0 %, et des évaluations du risque de biais incorrectes dans 10,0 % à 56,0 %. Une revue de portée de 2025 a identifié 37 articles : 15/37 (41 %) concernant la recherche bibliographique, 14/37 (38 %) la sélection des études, 11/37 (30 %) l’extraction de données ; 33/37 (89 %) utilisaient des modèles GPT et 21/37 (57 %) étaient des études de validation ; 20/37 (54 %) ont conclu de manière prometteuse, aucune comme implémentation validée. Le cribéage titre/résumé était le plus mature (sensibilité 99,2 %, spécificité 83,6 %) par rapport au cribéage texte intégral (97,6 % et 47,4 %). Pour l’extraction structurée sur 30 articles, un outil a atteint 92,0 % de précision, rappel et F1, mais la sensibilité tombait à 77,0 %–80,0 % pour les variables spécifiques à la revue, avec des confabulations dans 4/90 (4 %) des points de données ; sur 107 essais, la précision d’extraction était de 96,2 % (97,9 % avec affinage) tandis que le temps moyen est passé de 86,9 à 14,7 min par essai. L’évaluation du risque de biais était la tâche la plus fragile (kappa 0,51, IC 95 % : 0,36–0,66). Pour l’erreur résiduelle, 0 erreur parmi 60 éléments vérifiés correspond à une borne supérieure unilatérale à 95 % de 4,9 %. Discussion L’IA transforme les RS/MA vers des flux de travail hybrides homme–machine plutôt qu’elle ne les remplace. Les performances sont spécifiques à la tâche, et les métriques seules sont insuffisantes : l’incertitude résiduelle doit être quantifiée. Les données actuelles soutiennent l’IA comme technologie d’assistance sous supervision humaine, et non une utilisation autonome. Niveau de preuve V ; revue narrative.

**Решение:** -1 обзор применения ИИ в систематических обзорах литературы

---

### 147 · R1272

**Beyond Cognitive Support: Social Interaction and Affective Experience in AI-Assisted Creative Thinking Among University Students.**

2026 · Journal of Intelligence · journal article, journalarticle, article · eng · https://doi.org/10.3390/jintelligence14070151

Creative thinking has become an increasingly important competence in education, yet less is known about how it may be supported in human-AI collaboration as large language models (LLMs) are increasingly employed as partners in learning and problem solving. This study examined whether and how cognitive support and social interaction in AI-assisted collaboration were associated with divergent and convergent thinking. A total of 92 undergraduate students completed creative problem-solving tasks with GPT-4.0. Data were collected from task outputs and self-report measures, and the hypothesized associations were tested using structural equation modeling, with indirect effects examined as supplementary analyses. Results showed that in human-AI collaboration, social interaction rather than cognitive support was associated with more positive affective experiences, and this affective pathway was linked specifically to convergent thinking rather than divergent thinking. These findings suggest that associations between AI-assisted collaboration and creative thinking may depend less on perceived cognitive support alone than on the extent to which collaboration is experienced as socially engaging and affectively positive, particularly for convergent thinking.

**Решение:** -4 исследование совместного с GPT-4 решения задач студентами на креативность

---

### 148 · R3200

**Using Large Language Models to Create Personalized Networks From Therapy Sessions**

2026 · OSF Preprints (OSF Preprints) · preprint

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T1/T3 построение персонализированных сетей по сессиям психотерапии, нет аннотации — проверить эталон в полном тексте

---

### 149 · R2840

**Exposing Privacy Risks in Graph Retrieval-Augmented Generation**

2026 · Annual Meeting of the Association for Computational Linguistics · journalarticle, conference, preprint/article · https://doi.org/10.18653/v1/2026.findings-acl.899

Retrieval-Augmented Generation (RAG) is a powerful technique for enhancing Large Language Models (LLMs) with external, up-to-date knowledge. Graph RAG has emerged as an advanced paradigm that leverages graph-based knowledge structures to provide more coherent and contextually rich answers. However, the move from plain document retrieval to structured graph traversal introduces new, under-explored privacy risks. This paper investigates the data extraction vulnerabilities of the Graph RAG systems. We design and execute tailored data extraction attacks to probe their susceptibility to leaking both raw text and structured data, such as entities and their relationships. Our findings reveal a critical trade-off: while Graph RAG systems may reduce raw text leakage, they are significantly more vulnerable to the extraction of structured entity and relationship information. We also explore potential defense mechanisms to mitigate these novel attack surfaces. This work provides a foundational analysis of the unique privacy challenges in Graph RAG and offers insights for building more secure systems.

**Решение:** -4 уязвимости приватности в Graph RAG, кибербезопасность

---

### 150 · R3031

**Optimized code-switching attacks on open-source large language models**

2026 · DR-NTU (Nanyang Technological University) · report · en

Large language models (LLMs) undergo extensive safety alignment to mitigate harmful outputs; however, this process is predominantly conducted in English, leaving a systematic vulnerability in other languages. We exploit this gap through a gradient-guided code-switching attack, Safety Targeted Embedding Exploit via Refinement (STEER). STEER leverages model gradients to identify tokens that most strongly activate refusal behavior, then selectively translates these tokens into low-resource languages to bypass safety filters while preserving malicious intent. Across six open-source 8B-parameter models, STEER achieves attack success rates (ASR) of up to 93% on JailbreakBench and 96.7% on AdvBench, outperforming direct prompting, random code-switching (CSRT), and Greedy Coordinate Gradient (GCG) in both effectiveness and iteration efficiency. To better understand the mechanism, we conduct a layer-wise analysis using the Fisher Linear Discriminant, which reveals that refusal representations are geometrically localized within specific middle layers. This structural concentration enables efficient white-box exploitation. Furthermore, a transferability evaluation on GPT-4o-mini demonstrates that STEER achieves a 35.5% ASR, significantly surpassing CSRT (13.9%) and GCG (29.3%). This indicates that the vulnerability extends beyond white-box settings into more realistic black-box scenarios. Overall, our findings expose critical gaps in multilingual safety alignment and highlight the need for more robust, language-agnostic defense mechanisms.

**Решение:** -4 атаки на открытые LLM с переключением языкового кода
