# Проверка с метками ИИ, часть 7

Записи 901–1050 из 1304, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

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

### 901 · R6276

**Multi-Task Mental Health Detection with Large Language Models under Class Imbalance**

2026 · MobiSys Workshops · journalarticle, book, conference-paper · https://doi.org/10.1145/3812836.3814757

Social media posts provide a valuable opportunity for early mental health detection because they often capture users' thoughts, emotions, and distress signals in real time, potentially enabling timely identification of individuals at risk. However, building reliable models from such data is difficult, especially because benchmark datasets are often highly imbalanced across tasks and labels. In this paper, we study how loss design and reweighting strategies affect multi-task mental health prediction on four Reddit-based corpora covering six tasks: stress detection, binary depression detection, depression severity classification, suicidal ideation detection, binary suicide-risk detection, and five-level suicide-risk assessment. We compare several training configurations built on the same Qwen3-4B with LoRA backbone, including cross-entropy with reweighting, focal loss, focal loss with reweighting, a without-CE baseline, and a Proposed BACC-Guided setting that combines cross-entropy with a balanced-accuracy-oriented objective. Across the six tasks, the Proposed BACC-Guided setting achieves the best overall balanced accuracy, reaching a mean BACC of 0.62, compared with 0.59 for focal loss with reweighting, 0.58 for reweighting only, 0.57 for focal loss only, and 0.56 for the without-CE baseline. The gains are most evident on binary and moderately imbalanced tasks, suggesting that optimizing for balanced accuracy can produce more robust and generalizable mental health models under heterogeneous task imbalance. As an exploratory study, our findings provide initial insights that can guide future research on identifying the most suitable models and training strategies for multi-task mental health prediction.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Fine-tuned Qwen3-4B on Reddit mental-health benchmarks; labels may be human-annotated (e.g., suicide-risk levels), but the abstract doesn't say.

**Решение:** =

---

### 902 · R6280

**Evaluating Developmental Cognition Capabilities of LLMs**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.08549

Conversational AI is increasingly personalized around users' preferences, histories, goals, and knowledge, but much less around how users interpret and take up model outputs to construct and understand their reality. We draw on Robert Kegan's constructive-developmental theory as a complementary lens on this dimension. Existing methods for assessing developmental stage in the Keganian tradition rely either on expert interviews that do not scale or on sentence-completion instruments that are proprietary, lengthy, or invasive. To make this perspective tractable for LLM evaluation, we introduce the Developmental Sentence Completion Test (DSCT), a 20-item instrument designed to elicit developmental signal in self-administered text. Throughout, we treat the resulting labels as characterizations of stage-like structure in elicited responses, not as validated person-level developmental stage. We then ask how much of that signal can be recovered by LLMs across three elicited response regimes: simulated personas, real human respondents, and default model-generated answers. On simulated personas, top frontier models recover simulator-intended labels with high accuracy. On real human DSCT responses, human-LLM agreement is fair, with much stronger within-neighborhood than exact agreement. Finally, when LLMs answer DSCT prompts without persona-conditioning, their responses exhibit stable stage-like differences across model families, with larger and newer models tending to generate higher-rated text. These results suggest that stage-conditioned signal is cleaner in synthetic responses than in human-written DSCT text, and that the core constraint for stage-aware conversational AI is not classifier accuracy alone, but the availability of developmental signal from elicited text. 9 pages, 3 figures, (10 pages appendix)

**ИИ:** + · обе модели · подсчёт методики · LLMs score real human sentence-completion responses for Kegan developmental stage, and the abstract reports human–LLM agreement.

**Решение:** =

---

### 903 · R6284

**Enhancing Automated Text Coding in Online Learning Research: A Systematic Calibration Framework for Large Language Models**

2026 · IEEE Transactions on Learning Technologies · dataset/dataset, journalarticle, article · https://doi.org/10.1109/tlt.2026.3661363

Automated coding is particularly crucial in online learning research, where vast amounts of text provide valuable insights into cognitive engagement, emotional expression, and social interaction, yet manual analysis of such large-scale discourse remains time-consuming. While large language models (LLMs) offer promising solutions, existing approaches suffer from inconsistent coding performance and suboptimal prompt engineering, limiting their reliability across diverse educational frameworks. This study introduces the optimized LLM coding (OLLM-C) framework, a systematic approach that enhances automated content analysis through calibrated prompting strategies. We evaluated OLLM-C using a comprehensive dataset of 8671 comments collected from five online courses. The framework was validated against 15 widely used coding frameworks spanning cognitive, social-emotional, and behavioral dimensions. Comparative analysis of five LLMs [generative pre-trained transformer (GPT)-3.5, GPT-4o, Gemini, Claude, and Llama] revealed GPT-4o’s superior performance in initial coding tasks. The OLLM-C calibration process significantly improved GPT-4o’s reliability, with Cohen’s kappa coefficients increasing from an average of 0.45–0.57 across frameworks. Notably, the model demonstrated stronger performance in social-emotional coding compared to cognitive skills frameworks, achieving substantial agreement with human coders in emotion recognition and social interaction analysis while showing limitations in complex cognitive reasoning tasks. These findings establish OLLM-C as a systematic calibration framework that enhances the reliability, efficiency, and practical applicability of LLM-assisted qualitative analysis.

**ИИ:** + · обе модели · кодирование по кодбуку · LLMs applied coding frameworks (cognitive, social-emotional, behavioral) to online learning comments; Cohen's kappa against human coders reported.

**Решение:** =

---

### 904 · R6302

**Retrieval‑augmented large language models for depression screening and suicide risk stratification.**

2026 · BMC psychiatry · journal article, journalarticle, review · eng · https://doi.org/10.1186/s12888-026-07988-0

BACKGROUND: Depression imposes substantial individual and societal burdens, yet more than 80% of cases remain undetected in non‑psychiatric settings, and approximately 15% of individuals with severe depression die by suicide. Existing screening methods are limited by subjective self‑report, fragmented care pathways, and stigma‑related underutilization. METHODS: We developed and locally deployed a Retrieval‑Augmented Generation (RAG) framework that integrates large language models (LLMs) with an evidence‑based clinical knowledge base for depression and suicidality. Three leading Chinese LLMs (DeepSeek, Qwen, Baichuan) were evaluated under base and RAG‑augmented configurations. The knowledge base comprised clinical practice guidelines, standard textbooks, and peer‑reviewed literature. Model performance was assessed on multi‑source datasets. Outcomes included classification of depression and suicide risk, consistency of diagnostic outputs, symptom‑summary quality, and clinician‑rated empathy and dialogue quality. RESULTS: RAG augmentation consistently improved diagnostic performance across datasets. For depression detection, Qwen3 + RAG achieved an F1‑score of 0.9107, and for suicide risk stratification, RAG enhanced F1‑scores by approximately 0.15 compared with non‑RAG baselines. The best‑performing configuration demonstrated high reproducibility for both depression diagnosis and suicide risk classification (overall κ = 0.93; 95% CI: 0.91–0.95). Symptom summarization was substantially improved with RAG, with relative gains of 44.1–207.2% in BLEU‑2 and 37.0–94.0% in ROUGE‑L. Clinician‑blinded ratings indicated clinician-evaluated high-level empathic expression in RAG‑enhanced models (mean scores 4.23–4.98/5), with Qwen3 + RAG exhibiting particularly strong emotional concordance (95% CI: 4.80–4.92). Dialogue quality was rated as high across domains, including fluency (mean 4.98/5) and perceived doctor‑likeness (mean 4.94/5). CONCLUSIONS: A domain‑specific, RAG‑enhanced LLM framework can deliver clinically reliable, reproducible, and empathetic depression screening and suicide risk stratification in both real‑world and simulated settings. Local on‑premises deployment supports privacy and data‑governance requirements, while the scalable architecture and structured outputs position this approach as a promising tool for augmenting mental health triage and longitudinal monitoring in resource‑constrained environments.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs classify depression and suicide risk across multi-source datasets; unclear whether the reference labels are human/clinician coding or diagnoses.

**Решение:** =

---

### 905 · R6319

**Empathy in Diversity: Personalized Depression and Anxiety Therapy via Dialogue State Tracking and Patient-Aware Planning**

2026 · Annual Meeting of the Association for Computational Linguistics · journalarticle, conference · https://doi.org/10.18653/v1/2026.acl-long.424

Large language model (LLM) dialogue agents are increasingly used in psychological therapy, yet robustness across diverse patients remains underexplored. We address this gap with three contributions: (1) MindEval , a realistic role-play protocol for evaluating therapeutic dialogue agents; (2) MindData , a de-identified, expert-annotated corpus of therapist–patient dialogues (2,573 sessions; 63,348 turns); and (3) MindApt , a framework that integrates a therapeutic dialogue state tracking paradigm with a patient-aware strategic planning module. On MindEval, MindApt out-performs strong baselines on therapeutic outcomes and dialogue quality while improving conversational efficiency. To evaluate utility beyond role-play, we conducted a clinical study with real patients, demonstrating that MindApt-guided care achieves outcomes comparable to therapist-determined care, while the hybrid setting combining therapist judgment with Min-dApt’s recommendations yields the strongest overall outcomes.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly a therapy-agent paper, but the LLM dialogue state tracking may be evaluated against expert annotations of patient states in the corpus.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Therapy dialogue agent generation framework and role-play evaluation; the expert-annotated corpus is not used for LLM-vs-human coding agreement.)

**Решение:** -

---

### 906 · R6328

**When AI Meets Early Childhood Education: Large Language Models as Assessment Teammates in Chinese Preschools**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-29744-0_18

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM assessment in preschools may involve rating child development or classroom interactions against teacher ratings.

**Решение:** =

---

### 907 · R6331

**G-SHARE: A Guideline-Based Structured Reasoning Framework for Human-Factor Event Diagnosis**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.11892

Human-factor event diagnosis is essential for learning from operational events in nuclear power plants, yet its quality depends strongly on expert interpretation of narrative reports and guideline-based reasoning.Existing data-driven or one-shot large language model approaches often lack structured reasoning, have limited alignment with formal diagnostic guidelines, and may generate logically inconsistent conclusions. To address this issue, this study proposes G-SHARE, a guideline-based structured reasoning framework that operationalizes the CNNP nine-step human-factor event diagnosis guideline into a multi-stage diagnostic pipeline.The framework consists of evidence extraction, stepwise diagnostic reasoning, and post-hoc consistency repair, enabling explicit use of report evidence, intermediate rationale generation, and logical validation of diagnostic outputs. A dataset of real human-factor event reports was constructed from Chinese nuclear industry sources, and a gold-standard subset annotated by domain experts was used for evaluation. Results show that G-SHARE substantially outperforms one-shot prompting and traditional machine learning baselines, with the strongest version achieving the best overall accuracy and macro-F1. Ablation results further indicate that structured reasoning and consistency enforcement are critical to robust diagnosis, especially under weak prompting conditions. The findings demonstrate the value of transforming expert diagnostic guidelines into auditable reasoning workflows, providing a practical pathway for intelligent human-factor analysis in safety-critical industries.

**ИИ:** разошлись — Opus ? (неясен конструкт: An LLM classifies nuclear-plant event narratives against expert gold labels; unclear if human-factor error diagnosis counts as a psychological construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Nuclear plant human-factor event diagnosis from incident reports; an industrial safety domain, not a psychological or clinical construct in text.)

**Решение:** -

---

### 908 · R6334

**Structure vs. Chain-of-Thought: Evaluating LLM Criteria Extraction for Depression Severity**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.39049

A large language model (LLM) can rate depression severity directly from a social media post, or mark which clinical criteria the post shows and let a simple rule turn the count into a label. The latter is easier to audit because a clinician can check each marked criterion. We compare these approaches on two Reddit corpora using three LLMs (from 9B to frontier scale) and two questionnaires (PHQ-9, BDI-II), and measure agreement with quadratic weighted kappa. For the two frontier models, criteria extraction scores above chain-of-thought on one corpus only when its decision thresholds are fitted on labeled data. Neither model's gain is significant, with or without recalibrating chain-of-thought on the same labels. With thresholds fixed a priori from PHQ-9's criteria, extraction shows no gain on either corpus, even where models mark over two criteria per post. The 9B model behaves differently on a corpus from depression communities. It labels most posts as severe, whether prompted directly or with chain-of-thought, while the a priori rule, which uses no labels, beats both. After chain-of-thought is recalibrated on the same labels, no significant gap remains, consistent with a calibration effect. Yet higher ordinal agreement does not ensure better detection of severe cases. PHQ-9 criteria extraction misses most severe posts, and moving from direct prompting to chain-of-thought and then to extraction increases misses in nearly all comparisons. On one corpus, a relabeled stress dataset, a model using that dataset's own features, some computed from the post text, is not significantly different from frontier criteria extraction under the a priori rule. 16 pages, 3 figures. Extended version of a paper accepted at MHSM 2026 (IEEE ICDM 2026 Workshops); includes BDI-II extraction for the 9B model, not in the proceedings version. v2 adds a criteria-structured chain-of-thought ablation, two figures, and the 9B model in the stricter-threshold check. Code: https://github.com/xinkaichen97/depseverity-artifact

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: LLMs rate depression severity of Reddit posts against annotated severity labels (QWK); the corpora likely carry human annotations.); Sonnet ? (неясно, кто ставил эталонные метки: LLMs rate depression severity in Reddit posts, scored by QWK against labels; unclear whether the reference labels come from human annotators or from self-report.)

**Решение:** +

---

### 909 · R6357

**Automated Health Care Thematic Analysis Using a Multiagent Large Language Model: Algorithm Development and Evaluation Study.**

2026 · Journal of medical Internet research · journal article, evaluation study, journalarticle · eng · https://doi.org/10.2196/90872

BACKGROUND: Understanding patients' experiences is essential for advancing patient-centered care, especially in chronic diseases that require ongoing communication. Qualitative thematic analysis is widely used to explore these experiences; however, the process remains labor-intensive, subjective, and difficult to scale. OBJECTIVE: This study aimed to develop and evaluate Collaborative Theme Identification Agents (CoTI), a multiagent large language model framework designed to support manual thematic analysis by rapidly generating supporting excerpts, initial codes, and themes. METHODS: CoTI consists of 3 agents: Instructor, Thematizer, and CodebookGenerator. The Instructor refines instruction prompts, the Thematizer extracts supporting excerpts and generates initial codes for each transcript, and the CodebookGenerator groups similar codes across all transcripts into a codebook with themes. We evaluated CoTI primarily using 12 transcripts of patient with heart failure, with a focus on perceptions of medication intensity. CoTI-generated outputs were compared against the reference standard developed by senior investigators. To explore human-AI interaction in thematic analyses, we further implemented CoTI in a user-facing application. RESULTS: CoTI generated supporting excerpts, initial codes, and themes that were more similar to those of senior investigators than were the outputs of junior investigators, baseline natural language processing models, and other basic large language models. In an exploratory human-AI collaboration experiment, we found that the collaboration between CoTI and junior investigators provided only marginal gains compared to CoTI alone. A possible hypothesis was that junior investigators may overrely on CoTI and limit their independent critical thinking. CONCLUSIONS: CoTI can improve the efficiency of thematic analysis by rapidly generating supporting excerpts, initial codes, and themes for human researchers' review. These findings highlight CoTI's potential as a useful tool for scalable qualitative research.

**ИИ:** ? · обе модели · другое · Multiagent LLM thematic analysis of heart-failure patient interviews; compared mainly at the code/theme similarity level, but excerpt-level comparison may allow unit agreement.

**Решение:** =

---

### 910 · R6358

**Large Language Model-Assisted Annotation Framework for Cross-Platform Analysis of Online Autism Communities: Implications for Parent Education and Digital Support.**

2026 · Journal of medical Internet research · journal article, journalarticle, article · eng · https://doi.org/10.2196/85290

Background Online health communities (OHCs) are important channels for families of children with autism spectrum disorder to obtain health information and psychosocial support. Differences between an open forum platform and the physician-patient consultation platforms may shape caregiver decisions, yet comparative evidence from China remains limited. A large language model (LLM) provides a scalable approach for systematic content annotation in large OHC datasets. Objective This study proposes and validates a standardized LLM-assisted annotation framework under a unified classification schema and compares topic distributions and poster identities across an open forum platform (Baidu Tieba) and physician-patient consultation platforms (Chunyu Doctor and Haodf). Methods We implemented an LLM-assisted annotation framework. A unified taxonomy of topics and poster identities was first developed through human open coding. Poster identities in Baidu Tieba were annotated through a double-blind manual procedure. For topic classification, interannotator and human-LLM agreement were evaluated on a manually labeled subset to benchmark models of varying sizes. The best-performing LLM was selected for full-dataset topic annotation, followed by statistical and cross-platform analysis. Results When metrics were arithmetically averaged across all annotation tasks, the best-performing LLM achieved agreement levels comparable to human annotation (accuracy=79.18%, SD 0.20%; κ=0.736, SD 0.003; F 1 -score=0.727, SD 0.006), approaching interannotator agreement (accuracy=81.65%; κ=0.767; F 1 -score=0.758), demonstrating strong stability and scalability. Full-dataset analysis yielded 3 main findings. First, model performance increased with parameter scale but plateaued beyond 14B, indicating diminishing marginal returns from further scaling. Second, clear cross-platform differences in poster identity were observed: the open forum platform was dominated by family members of patients (caregivers: 2377/3516, 67.61%), with substantial participation from commercial rehabilitation practitioners (commercial posters: 427/3516, 12.14%), resulting in a more heterogeneous participation structure. Third, topic distributions reflected both shared high demand for resource-related information and differentiated help-seeking pathways: both platform types demonstrated consistently high demand for resource recommendation and evaluation; the open forum platform was primarily characterized by diagnosis-related discussions (1183/7535, 15.70%), whereas the physician-patient consultation platforms were centered on intervention-related consultation (2864/7687, 37.26%). Conclusions The LLM-assisted annotation framework proposed in this study enables reliable large-scale annotation of OHC data while maintaining high human-LLM agreement and operational stability. Midsized models (eg, 14B) demonstrated favorable cost-performance efficiency. The findings reveal 2 key aspects: the open forum platform exhibits a complex participation structure, and the influence of commercially affiliated actors should not be overlooked; users on both platform types show sustained demand for resource-related information but follow different help-seeking pathways, emphasizing diagnostic exploration and professional intervention, respectively. These results suggest that platform structure and governance mechanisms may shape caregivers' information access and decision-making. The framework provides a transparent, reproducible, and cost-effective approach for OHC research. All data were deidentified and handled in accordance with relevant platform policies and ethical standards.

**ИИ:** ? · обе модели · неясен конструкт · LLM topic coding of autism caregiver forum posts vs human labels (κ reported); unclear if topic categories count as psychological constructs.

**Решение:** =

---

### 911 · R6359

**Using large language models to evaluate the interplay between posttraumatic stress disorder symptom severity and intolerance to uncertainty: A large-scale ecological momentary assessment study.**

2026 · Journal of psychopathology and clinical science · journal article, journalarticle, article · eng · https://doi.org/10.1037/abn0001156

Intolerance of uncertainty (IU) is central to cognitive models of posttraumatic stress disorder (PTSD), reflecting a maladaptive process that maintains hypervigilant threat appraisals and symptom persistence. However, traditional self-report measures may overlook IU's implicit and context-dependent expression. Here, we introduce a novel language-based method to detect subtle linguistic markers of IU from naturalistic daily diaries and examined the role of IU in PTSD symptoms dynamics. In a 90-day ecological momentary assessment study, 432 trauma-exposed individuals with elevated PTSD symptoms provided 29,623 diary entries and 32,941 daily PTSD symptom ratings. A large language model (LLM)-based IU assessment quantified the similarity between daily transcribed speech and language from an established IU scale; IU model scores correlated with human ratings ( r = .60). Dynamic structural equation models showed that higher daily IU predicted greater next-day PTSD symptom severity (β = .041, 95% credible interval CI [.024, .056]), even after controlling for prior-day symptoms. Higher daily PTSD symptom severity also predicted greater next-day IU (β = .035, 95% CI [.018, .054]). The strength of these bidirectional effects varied across individuals (IU→PTSD variance = .014, 95% CI [.007, .022]; PTSD→IU variance = .037, 95% CI [.030, .047]), reflecting substantial heterogeneity in daily IU-PTSD dynamics. Complementary multilevel analyses demonstrated that language-derived IU provides incremental validity, explaining variance in PTSD symptom severity beyond sentiment and positive and negative affect. These findings extend cognitive models of PTSD, demonstrating that IU influences daily symptom trajectories, and provide an ecologically valid, scalable framework for tracking implicit cognitive processes via natural language. (PsycInfo Database Record (c) 2026 APA, all rights reserved).

**ИИ:** разошлись — Opus + (проверка кодирования внутри исследования: LLM-derived intolerance-of-uncertainty scores from diaries correlated r=.60 with human ratings; check whether the model is generative or embedding-only.); Sonnet ? (другое: LLM-based intolerance-of-uncertainty scores for diary entries correlated with human ratings (r=.60), but the model may be embedding-based rather than generative; check the full text.)

**Решение:** +

---

### 912 · R6370

**Evaluating Large Language Models as Substitutes for Human Affective Ratings in Naturalistic Paradigms**

2026 · IEEE Transactions on Affective Computing · journalarticle, article · https://doi.org/10.1109/taffc.2026.3696891

Naturalistic paradigms provide ecologically valid insights into affective and cognitive processes but often require costly and time-consuming human annotations. Large language models (LLMs) provide a scalable tool for generating human-like affective ratings that could complement traditional behavioral approaches. In this study, we compared affective ratings of narrative segments obtained from young adults, five OpenAI's GPT models, Meta's Llama 3.1, and lexical-level norms from the SCOPE metabase. LLM-derived ratings of hedonic valence showed strong correlations with human ratings and outperformed lexical norms. When applied to fMRI data, LLM-derived ratings identified affective brain networks that substantially overlapped with those revealed by human ratings. These findings demonstrate that LLMs can approximate group-level affective ratings from young adults in naturalistic contexts and serve as a useful complement to traditional behavioral data collection, while underscoring the need for careful evaluation of their generalizability and potential biases.

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT models and Llama rated the affective valence of narrative segments, and these ratings were correlated with young adults' ratings of the same segments.

**Решение:** =

---

### 913 · R6373

**Towards Privacy-Preserving Mental Health Support with Large Language Models**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.01993

Large language models (LLMs) have shown promise for mental health support, yet training such models is constrained by the scarcity and sensitivity of real counseling dialogues. In this article, we present MindChat, a privacy-preserving LLM for mental health support, together with MindCorpus, a synthetic multi-turn counseling dataset constructed via a multi-agent role-playing framework. To synthesize high-quality counseling data, the developed dialogue-construction framework employs a dual closed-loop feedback design to integrate psychological expertise and counseling techniques through role-playing: (i) turn-level critique-and-revision to improve coherence and counseling appropriateness within a session, and (ii) session-level strategy refinement to progressively enrich counselor behaviors across sessions. To mitigate privacy risks under decentralized data ownership, we fine-tune the base model using federated learning with parameter-efficient LoRA adapters and incorporate differentially private optimization to reduce membership and memorization risks. Experiments on synthetic-data quality assessment and counseling capability evaluation show that MindCorpus improves training effectiveness and that MindChat is competitive with existing general and counseling-oriented LLM baselines under both automatic LLM-judge and human evaluation protocols, while exhibiting reduced privacy leakage under membership inference attacks. 15 pages, 16 figures

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly a counseling-model generation paper, but LLM-judge and human ratings of counseling responses might be compared on the same outputs.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Paper builds a synthetic counseling dataset and fine-tunes a counseling LLM; LLM-judge evaluation of chatbot outputs is not clearly validated against human ratings as a coding task.)

**Решение:** -

---

### 914 · R6405

**MIMIC-IV Phenotype Atlas (MIPA): A Publicly Available Dataset for EHR Phenotyping**

2026 · medRxiv · preprint, ppr, review · https://doi.org/10.64898/2026.04.16.26350888

Introduction Secondary use of electronic health records (EHRs) often requires transforming raw clinical information into research-grade data. A central step in this process is EHR phenotyping - the identification of patient cohorts defined by specific medical conditions. Although numerous approaches exist, from ICD-based heuristics to supervised learning and large language models (LLMs), the field lacks standardized benchmark datasets, limiting reproducibility and hindering fair comparison across methods. Methods We developed the MIMIC-IV Phenotype Atlas (MIPA) dataset, an adaptation of MIMIC-IV that provides expert-annotated discharge summaries across 16 phenotypes of varying prevalence and complexity. Two independent clinicians reviewed and labeled the discharge summaries, resolving disagreements by consensus. In parallel, we implemented a processing pipeline that extracts multimodal EHR features and generates training, validation, and testing datasets for supervised phenotyping. To illustrate MIPA's utility, we benchmarked four phenotyping methods : ICD-based classifiers, keyword-driven Term Frequency-Inverse Document Frequency (TF-IDF) classifiers, supervised machine learning (ML) models, and LLMs on the task. Results The final MIPA corpus consists of 1,388 expert-annotated discharge summaries. Annotation reliability was high (mean document-level kappa = 0.805, mean label-level kappa = 0.771), with 91% of disagreements resolved through consensus review. MIPA provides high-quality phenotype labels paired with structured EHR features and predefined train/validation/test splits for each phenotype. In the benchmarking case study, LLMs achieved the highest F1 scores in 13 of 16 phenotypes, particularly for conditions requiring contextual interpretation of clinical narrative, while supervised ML offered moderate improvements over rule-based baselines. Conclusion MIPA is the first publicly available benchmark dataset dedicated to EHR phenotyping, combining expert-curated annotations, broad phenotype coverage, and a reproducible processing pipeline. By enabling standardized comparison across ICD-based heuristics, ML models, and LLMs, MIPA provides a durable reference resource to advance methodological development in automated phenotyping.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs benchmarked against clinician phenotype labels on discharge summaries; 16 phenotypes unspecified, may include depression or substance abuse.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: EHR phenotyping of medical conditions in MIMIC-IV discharge summaries; general medical phenotypes, not psychological constructs.)

**Решение:** -

---

### 915 · R6413

**Large Language Model-Assisted Measurement of ADRD Caregiver Burden on Reddit (Preprint)**

2026 · JMIR Publications Inc. · posted-content, preprint · https://doi.org/10.2196/preprints.103305

BACKGROUND Background: Informal caregivers of older adults with Alzheimer’s disease and related dementias (ADRD) often face high burden and chronic stress. Reddit provides naturally occurring caregiver narratives to study caregiving burden, but prior studies have often relied on small manual coding or aggregate topic models that may not easily connect caregiving context, burden, and stressor at scale. OBJECTIVE Objective: This study aimed to apply a large language model (LLM)-assisted measurement workflow to characterize ADRD caregiver burden, caregiving contexts, stressor, temporal patterns, and high-burden subgroups in Reddit posts. METHODS Methods: We processed monthly Reddit submission archives from January 2020 through June 2025. Posts were selected from 5 ADRD-specific subreddits and 4 broader caregiving or aging subreddits, yielding a balanced 13,200-post corpus. A locally hosted open-weight LLM inferred structured post-level variables including caregiver sociodemographic characteristics, caregiver role, ADRD stage, care setting, support need, dominant emotion, sentiment, burden, and primary and secondary stressors. The workflow included schema validation, uncertainty ratings, field-level correction prompts, source matching, a 150-post double-coded human validation benchmark, and pairwise subgroup analyses. RESULTS Results: The source-matched analytic sample included 13,179 LLM-coded posts. Human agreement was high for caregiver role, ADRD stage, care setting, dominant emotion, support need type, burden group, and stressor categories (κ= 0.77–1.00), but poor for the initial in-scope screen (κ= 0.00). Adult children were the largest inferred caregiver group (8266/13,179, 62.7%), followed by grandchildren (2012/13,179, 15.3%). Moderate ADRD was the modal inferred stage (6554/13,179, 49.7%), and home was the modal care setting (7145/13,179, 54.2%). Mean burden increased from early-stage ADRD (5.38) to moderate-stage ADRD (6.96) and late-stage ADRD (7.77). Behavioral strain was the dominant primary stressor, while family conflict, financial strain, emotional strain, and social isolation were leading secondary stressors. Pairwise subgroup analysis showed high burden in late-stage ADRD with emotional support needs (mean 8.42), care transitions with emotional support needs (mean 8.45), and late-stage care transitions (mean 8.40). CONCLUSIONS Conclusions: LLM-assisted measurement can help convert unstructured caregiver narratives into post-level, theory-guided quantitative measures when paired with validation and cautious interpretation. This workflow extends prior online caregiver research by linking caregiving context, burden, and stressor pathways at scale. The findings highlight care transitions, emotional support needs, financial navigation, and family role negotiation as potential targets for caregiver-support interventions. CLINICALTRIAL Not applicable

**ИИ:** + · обе модели · проверка кодирования внутри исследования · LLM coded Reddit caregiver posts for burden, emotion and stressors; validated against a 150-post double-coded human benchmark (κ reported).

**Решение:** =

---

### 916 · R6421

**Harnessing AI and social media to understand real-world patient experiences in SLE.**

2026 · Lupus science & medicine · journal article, journalarticle, review · eng · https://doi.org/10.1136/lupus-2026-002024

Objective To apply large language models (LLMs) to Reddit posts referencing SLE to identify patient-expressed unmet medical needs, symptom experiences and healthcare challenges, demonstrating how artificial intelligence-enabled social media listening complements traditional patient-experience research. Methods We extracted 4633 posts from 10 SLE-related Reddit communities using the public Reddit Application Programming Interface (October-November 2025). After removing duplicates, promotional content and posts with insufficient information, 2603 posts remained. We developed a thematic codebook through manual review of 300 posts and refined it iteratively. Two state-of-the-art LLMs (Gemini 3.0 and GPT-5.2) were evaluated for automated thematic labelling using per cent agreement, Cohen's κ and performance against a human-annotated reference set (n=100). The best-performing model was then used to quantify theme prevalence across the full dataset, followed by qualitative review of representative narratives. Results GPT-5.2 demonstrated higher performance (F1=0.844) than Gemini 3.0 (F1=0.811), with substantial intermodel agreement across main themes (mean κ=0.71). Posts reflected multidimensional experiences. The most frequent subtheme was Advice Seeking (84.1%), followed by Emotional Coping (55.6%). Common symptom-related themes included Pain (37.2%), Other Symptom Presentations (37.6%), Fatigue (24.7%) and Acute or Worsening Flares (30.2%). Diagnostic uncertainty was prominent, including testing and results confusion (24.0%) and emotional impact of uncertainty and disease progression (33.0%). Qualitative review highlighted emotional and social burden, reliance on peer communities for advice and shared experiences, and difficulty managing complex treatment regimens. Conclusion LLM-enabled social media listening offers a scalable method for synthesising large volumes of unstructured patient narratives, providing timely insights into lived experiences and unmet needs among individuals discussing lupus online. Findings align with established qualitative literature while highlighting persistent gaps in patient education, communication and care coordination. This analytical framework can be extended to other disease areas to support patient-centred care, measurement development and evidence generation relevant to therapeutic and health outcomes research.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-5.2 and Gemini applied a codebook with emotional coping and emotional-impact themes to lupus Reddit posts, checked against a human-annotated reference set (κ, F1).

**Решение:** =

---

### 917 · R6432

**LLM-Assisted Incident Coding for UAS Safety: Reliability-Aware Human-Factor Extraction and Operational Risk Analytics**

2026 · Preprints.org · preprint, ppr, posted-content · https://doi.org/10.20944/preprints202602.0324.v1

Safety analysis for Unmanned Aircraft Systems (UAS) relies heavily on incident and occurrence reports that document operational anomalies, environmental conditions, and human-factor contributors in free-text narrative form. While these narratives contain rich safety-relevant information, transforming them into structured and analyzable knowledge remains labor-intensive, inconsistent, and difficult to scale. This paper proposes a reliability-aware framework for large language model (LLM)-assisted incident coding tailored to UAS safety analysis. A UAS-specific safety factor taxonomy encompassing human, system, environmental, and organizational contributors is first developed. Using constrained prompting, LLMs are guided to extract structured safety factors from incident narratives together with explicit supporting evidence spans. To address trust and robustness concerns in safety-critical applications, a multi-level reliability audit is introduced, integrating self-consistency analysis, evidence stability assessment, and agreement with expert annotations. Finally, the extracted safety factors are incorporated into a risk-weighted operational analytics pipeline to identify dominant contributors and emerging safety patterns across different mission contexts. The proposed approach substantially reduces manual coding effort while maintaining strong alignment with expert judgment, demonstrating the potential of reliability-aware LLM analytics to support scalable and proactive UAS safety management.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM codes UAS incident narratives against expert annotations; human-factor contributors are partly psychological, but the domain is mainly operational safety.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM coding of UAS aviation incident reports (human factors in safety); not a psychological or clinical construct in psychological/clinical text.)

**Решение:** -

---

### 918 · R6437

**Depression detection via multimodal analysis using a large language model-powered interview platform**

2026 · Engineering Applications of Artificial Intelligence · article · en · https://doi.org/10.1016/j.engappai.2026.114480

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. LLM depression detection from interviews; unclear whether the reference labels come from clinician ratings or from self-report/diagnosis.

**Решение:** =

---

### 919 · R6444

**AICompanionBench: Benchmarking LLMs-as-Judges for AI Companion Safety**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.04867

As AI companion platforms such as Replika and Character.AI rapidly grow, concerns about unsafe human-AI interactions have intensified. This study introduces AICompanionBench, to our knowledge the first publicly available benchmark dataset of human-AI companion conversations annotated with fine-grained safety risk categories. The dataset contains 2,123 real-world Replika conversations collected from Reddit and annotated through human-AI collaboration across nine categories: sexual behavior, antisocial behavior, physical aggression, verbal aggression, substance abuse, self-harm and suicide, control, manipulation, and no-harm. Using this benchmark, we evaluate 20 state-of-the-art open-source and closed-source LLMs under an LLM-as-judge framework for detecting unsafe interactions. Results show substantial variation in model performance, with stronger models achieving high overall accuracy but still struggling with nuanced categories such as manipulation, as well as benign conversations that are incorrectly identified as harmful. Our findings suggest that while current LLMs can effectively detect explicit harmful content, they remain limited in identifying implicit unsafe interactions. Overall, our work contributes a new benchmark dataset for AI companionship safety research and offers insights into monitoring AI companion systems using LLMs. The dataset is publicly available at: https://github.com/anonymousresearcher2026/AICompanionBench/blob/main/AICompanionBench.xlsx

**ИИ:** + · обе модели · бенчмарк с метками людей · Benchmark of companion conversations annotated for harm categories (self-harm, aggression, manipulation); 20 LLM judges evaluated against these human-AI annotated labels.

**Решение:** =

---

### 920 · R6447

**MedSimAI: Simulation and Formative Feedback Generation to Enhance Deliberate Practice in Medical Education**

2026 · International Learning Analytics and Knowledge Conference (LAK) · book, journalarticle, review · en · https://doi.org/10.1145/3785022.3785092

Medical education faces challenges in providing scalable, consistent clinical skills training. Simulation with standardized patients (SPs) develops communication and diagnostic skills but remains resource-intensive and variable in feedback quality. Existing AI-based tools show promise yet often lack comprehensive assessment frameworks, evidence of clinical impact, and integration of self-regulated learning (SRL) principles. Through a multi-phase co-design process with medical education experts, we developed MedSimAI, an AI-powered simulation platform that enables deliberate practice through interactive patient encounters with immediate, structured feedback. Leveraging large language models, MedSimAI generates realistic clinical interactions and provides automated assessments aligned with validated evaluation frameworks. In a multi-institutional deployment (410 students; 1,024 encounters across three medical schools), 59.5 percent engaged in repeated practice. At one site, mean Objective Structured Clinical Examination (OSCE) history-taking scores rose from 82.8 to 88.8 (p &lt; 0.001, Cohen's d = 0.75), while a second site's pilot showed no significant change. Automated scoring achieved 87 percent accuracy in identifying proficiency thresholds on the Master Interview Rating Scale (MIRS). Mixed-effects analyses revealed institution and case effects. Thematic analysis of 840 learner reflections highlighted challenges in missed items, organization, review of systems, and empathy. These findings position MedSimAI as a scalable formative platform for history-taking and communication, motivating staged curriculum integration and realism enhancements for advanced learners. Accepted to LAK 2026; 11 pages, 5 figures

**ИИ:** ? · обе модели · неясен конструкт · LLM scores medical student encounter transcripts on MIRS (communication, empathy) with 87% accuracy, presumably against human raters; the construct is only borderline psychological.

**Решение:** =

---

### 921 · R6450

**Preregistered Evaluation of LLM-Based Scoring of the Washington University Sentence Completion Test**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/hg2kb

The Washington University Sentence Completion Test (WUSCT; Hy & Loevinger, 1996) measures ego development from a person's completions of a set of sentence stems. Its scoring is its bottleneck. A trained rater assigns every completion an ego-development stage on the ordinal scale E2-E9, using a scoring manual whose rules and example completions are specific to the individual sentence stem, and then aggregates the item ratings into a Total Protocol Rating by fixed ogive rules. Training a rater takes months, and rating a protocol takes a skilled person a substantial amount of time. That cost, rather than any property of the construct, is what keeps the instrument out of studies that would otherwise use it. This project develops and evaluates an automated rater: a large language model prompted with the same item-specific scoring instruction a human rater works from, returning for each completion a stage rating, a justification in the manual's own terms, and a self-reported confidence. Protocol ratings are then formed from the item ratings by the published ogive rules. The design decision that shapes the whole project is that the model receives the manual's item-specific material rather than a general description of the stages or a classifier trained on labelled responses. The consequence is that the procedure stays inspectable: every rating carries the rule it was based on, so a person can check it the way one rater checks another instead of accepting an opaque score. The registration covers three questions. First, whether the automated rater reaches the agreement level of a trained human rater at the item level, on responses it was not developed against. Second, whether that agreement survives aggregation to the Total Protocol Rating, which is the value the instrument actually reports. Third, whether the rater carries a usable signal of its own uncertainty (e. g. self-reported confidence, disagreement between independent rating attempts, simple properties of the response, ...) and what that signal is good for: deferring uncertain cases to a person, weighting the protocol-level aggregation, or directing where further human effort is worth spending. The evaluation runs against existing labelled WUSCT material: the two labelled datasets printed in the scoring manual's appendices, a large publicly archived corpus of expert-rated responses, and a further labelled corpus in the Loevinger scoring tradition that has been offered to us but is not yet in our possession. No human participants are recruited for data collection; the only new human work is expert re-rating of existing responses, which supplies a human-human agreement baseline on the same cases the automated rater sees. Expected outcomes: We expect item-level agreement to fall short of perfect and to be unevenly distributed: better on short, prototypical completions and in the lower and middle stages, worse on long completions and in the upper stages, where the manual's distinctions are finest and the base rates lowest. We expect the ogive aggregation to absorb part of the item-level error, so that protocol-level agreement is better than the item-level figure alone would suggest. We expect the error signals to be informative enough to identify a subset of cases whose deferral raises accuracy on the remainder materially, but not sufficient to approach complete detection. And we expect agreement to be bounded above by the agreement human raters reach among themselves, since independent human rating teams agree neither perfectly with one another nor perfectly with the published labels; we will interpret our numbers against that bound rather than against perfect agreement. Whether a residual gap is attributable to the model, to the rating instruction, to the reference labels or to genuine ambiguity in the responses is not separable with the present design, and we do not plan to claim it. Preliminary results from method development (not confirmatory): The figures below were obtained on the corpora described above during method development, are reported against the corrected key. They are development results, with the corpora having been fully inspected and none of them constituting a test of the hypotheses registered here. Item level (manual appendices, n = 570): exact agreement 0.844 [0.814, 0.874], agreement within one stage 0.981, quadratically weighted kappa 0.913. Protocol level (12 complete protocols): every protocol rating falls within one stage of the reference, exact agreement 0.75–0.83. Rater self-consistency across repeated identical runs: weighted kappa 0.93–0.98. Self-reported confidence separates correct from incorrect ratings with an area under the ROC curve of 0.845; deferring the least confident 28 % of cases raises exact agreement on the remainder to 0.93. Read against the published inter-rater literature, these values sit inside the range reported for trained human raters (item exact 77–85 %, within one stage ~95 %, item weighted kappa .73). It is currently not possible to determine whether the residual disagreement belongs to the rater, the rating instruction, the reference labels, or whether it is due to genuine ambiguity in the responses. The work of separating these factors is ongoing. If the rater reaches the stated thresholds, the practical outcome is a scoring procedure that makes the WUSCT usable at a scale its rating cost currently forecloses, with a person in the loop only where the procedure flags itself as uncertain. If it does not, the outcome is a quantified account of where and how it fails, broken down by stage, sentence stem and response type. This provides insight into where the boundary lies between material that can be reliably rated and genuinely ambiguous material. The method exists and has been developed against corpora we have seen in full. This registration is filed to record the project, its questions and the shape of its analyses before the confirmatory material becomes available. Parts of the plan

**ИИ:** разошлись — Opus ? (другое: Preregistration (normally excluded), but it reports preliminary LLM-versus-expert WUSCT scoring agreement (weighted kappa 0.913), so full-text check needed.); Sonnet + (подсчёт методики: Preregistered study of an LLM scoring WUSCT sentence completions (ego development), compared with expert human ratings; agreement metrics reported.)

**Решение:** +

---

### 922 · R6452

**MedQA-CS: Objective Structured Clinical Examination (OSCE)-Style Benchmark for Evaluating LLM Clinical Skills.**

2026 · Proceedings of the conference. Association for Computational Linguistics. European Chapter. Conference · audiovisual/conference talk, journal article, journalarticle · eng · https://doi.org/10.18653/v1/2026.eacl-long.292

Artificial intelligence (AI) and large language models (LLMs) in healthcare require advanced clinical skills (CS), yet current benchmarks fail to evaluate these comprehensively. We introduce MedQA-CS, an AI-SCE framework inspired by medical education's Objective Structured Clinical Examinations (OSCEs), to address this gap. MedQA-CS evaluates LLMs through two instruction-following tasks, LLM-as-medical-student and LLM-as-CS-examiner, designed to reflect real clinical scenarios. Our contributions include developing MedQA-CS, a comprehensive evaluation framework with publicly available data and expert annotations, and providing the quantitative and qualitative assessment of LLMs as reliable judges in CS evaluation. Our experiments show that MedQA-CS is a more challenging benchmark for evaluating clinical skills than traditional multiple-choice QA benchmarks (e.g., MedQA). Combined with existing benchmarks, MedQA-CS enables a more comprehensive evaluation of LLMs' clinical capabilities for both open- and closed-source LLMs. To appear in proceedings of the Main Conference of the European Chapter of the Association for Computational Linguistics (EACL) 2026

**ИИ:** ? · обе модели · неясен конструкт · LLM-as-examiner judged against expert annotations of OSCE encounters; mostly medical clinical skills, though patient communication may count as interpersonal.

**Решение:** =

---

### 923 · R6463

**Validating local open-weight LLMs against expert raters for graded deductive coding of open-ended responses in Russian**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/8psd9_v2

Large language models (LLMs) are increasingly used to code open-ended survey responses, but their validity against expert annotation remains uncertain, especially outside English. We evaluated four open-weight LLMs for deductive coding of Russian responses from a psychological human-robot interaction experiment (N = 33): DeepSeek-R1-32B, Qwen3-32B, Gemma3-27B, and Mistral-Small-3.2-24B. Ten psychology-trained coders provided a graded expert reference for seven predefined codes. Each model was run under singular-code prompts, an exploratory conservative variant, and fixed-sequence prompts mirroring the expert memo, with ten repeated runs aggregated into graded code-presence estimates. Agreement was assessed with graded concordance, calibration, human-equivalence, and threshold-sensitivity diagnostics. The strongest configurations by concordance — DeepSeek-R1-32B with singular-code prompting (CCC = 0.71) and Qwen3-32B with fixed-sequence prompting (CCC = 0.69) — reached agreement with the expert aggregate comparable to the disagreement among individual experts, although both relied on reasoning mode, which was confounded with model identity. Several models over-attributed codes relative to experts, and prompt format and aggregation strategy materially affected agreement. We recommend validating LLM coding as a measurement procedure, with reported calibration and uncertainty, rather than as automatic expert replacement in small applied psychological datasets.

**ИИ:** + · обе модели · кодирование по кодбуку · Open-weight LLMs did deductive coding of open-ended Russian responses from a psychology experiment and were compared with ten expert coders (CCC reported).

**Решение:** =

---

### 924 · R6478

**TeachObs: A Human-Validated Benchmark for Multimodal Teaching Observation and Model Evaluation**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.30673

Classroom videos contain observable teaching practices, but their pedagogical and visual signals are rarely organized in forms suitable for model evaluation. We present \textit{TeachObs}, a human-validated benchmark for multimodal teaching observation in classroom videos. \textit{TeachObs} includes 30 public lesson videos from eight countries divided into 5,158 fixed 15-second scenes. Seven researchers annotated each scene with 39 binary observation codes, covering 20 visual codes, such as gesture, board work, pointing, and visual materials, and 19 nonvisual codes, such as instruction, monitoring, questioning, feedback, and reflection. Gold segment labels are constructed using reliability- and prevalence-aware rules based on Krippendorff's alpha. In addition to segment-level labels, three expert raters produced lesson-level ratings and qualitative evaluations of instructional design, instructional delivery, learner response, learning materials, and lesson closure across the 30 lessons, with rater coverage detailed in the body. Using these two human reference layers, we evaluate five vision-capable frontier LLMs across three tracks - text-only segment coding, text + frame segment coding, and lesson-level coverage scored under an LLM-as-judge protocol - and find that no single model consistently outperforms others across all three tracks, that adding a mid-frame inflates both true and false attributions per scene, and that model evaluations over-rate procedurally clear lessons relative to expert raters. \textit{TeachObs} therefore supports both fine-grained annotation benchmarking and whole-lesson evaluation, showing where AI systems can assist classroom video analysis and where expert judgment remains necessary across varied subjects, classroom formats, and annotation difficulty levels.

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs code classroom teaching practices (pedagogical observation codes) against human annotators; this is an educational construct, not a psychological or clinical one.); Sonnet ? (неясен конструкт: LLMs code classroom teaching behaviours against human annotations (benchmark); the construct is educational rather than clearly psychological, and it is partly video-based.)

**Решение:** -

---

### 925 · R6490

**Evaluation of college student tutoring dialogue based on large language model prompting engineering**

2026 · International Conference on Optics, Electronics, and Communication Engineering (OECE) · conference, conference-abstract · https://doi.org/10.1117/12.3127800

The dialogue evaluation of student counseling in colleges and universities relies on human supervision, which faces the problems of strong subjectivity, high cost and lagging feedback, and the consistency between different supervisors is only medium. Different from clinical counseling, college counseling focuses on developmental issues such as academic pressure and interpersonal relationship. Due to the lack of strategy alignment for counseling micro-skills, the existing large model zero-sample prompt evaluation is prone to score inflation, standard deviation, and is significantly affected by the change of prompt words. To this end, this study constructs a dialogue evaluation dataset labeled by senior consultants according to the competency model for multiple rounds, covering six indicators such as emotional reflection, open inquiry, empowerment reconstruction and security risk. On this basis, a fine-tuning evaluation method is proposed to parameterize the tutoring micro-skill evaluation system into the large model. Based on LAMA-2-7B, a prompt template with embedded evaluation anchors and stepwise reasoning is designed, and QLoRA low-rank adaptation is used for instruction fine-tuning. Contrast samples are constructed for confusion dimensions such as "empathy-compassion" and "leading-preaching", and the preference ranking and supervised contrast loss optimization are combined. The training is completed on a single consumer-level GPU, and the motivation generation is fine-tuned synchronously to enhance the transparency of evaluation. GPT-4, Claude, no fine-tuning base and pure cue engineering baseline were selected for comparison. On real tutoring records, the proposed method significantly outperforms all comparison models in terms of weighted Kappa, fine-grained F1 and cross-dialogue length stability. Ablation studies confirmed that the joint contrast preference optimization made a prominent contribution to suppressing the inflation of confounding dimension scores, and the evaluation illusion and position deviation were also significantly reduced.

**ИИ:** + · обе модели · кодирование сессий · Fine-tuned Llama-2, GPT-4 and Claude rate counseling micro-skills (empathy, reflection) in dialogues; weighted kappa reported against labels from senior counselors.

**Решение:** =

---

### 926 · R6493

**How AI Functions Affect AI Recruitment System Continuance Intention: An Empirical Study Based on LLM Fine-Tuned Competency Modeling**

2026 · Guangdong-Hong Kong-Macao Greater Bay Area International Conference on Digital Economy and Artificial Intelligence (DEAI) · book, conference, review · https://doi.org/10.1145/3837873.3838060

Drawing on cognitive appraisal theory, this study examines how three types of artificial intelligence functions in recruitment systems—assistive, augmented, and autonomous—influence applicants’ continuance intention, with technology anxiety as a mediator and AI self-efficacy as a moderator. To operationalize the data collection, I developed a large language model fine-tuning pipeline based on ChatGLM3-6B with low-rank adaptation (LoRA, rank=8). The model extracts behavioral evidence from interview responses and generates standardized competency scores across four dimensions (communication, teamwork, responsibility, meticulousness), achieving strong agreement with human experts (Spearman's ρ=0.81). A three-wave, time-lagged survey was then administered to 224 job applicants who completed a real AI recruitment process powered by this model through a professional AI recruiting company in China. This study contributes to the AI recruitment literature by moving beyond a monolithic view of AI, demonstrating that distinct AI functions trigger different cognitive appraisal processes. It also introduces a reproducible LLM-based competency modeling method for applicant assessment, extends cognitive appraisal theory to human–AI interaction, and offers practical guidance for deploying AI recruitment systems to preserve applicants’ continuance intention.

**ИИ:** разошлись — Opus + (проверка кодирования внутри исследования: Fine-tuned ChatGLM3 scores behavioral/interpersonal competencies from interview responses; agreement with human experts reported (ρ=0.81).); Sonnet ? (неясен конструкт: Fine-tuned ChatGLM3 scores interview responses on competencies (teamwork, responsibility) with human-expert agreement (ρ=0.81); the construct is occupational, so psychological fit is unclear.)

**Решение:** +

---

### 927 · R6524

**Implicit Personality Representations in Humans and LLMs**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.12704

A century of psychology has found that the trait words people use to describe one another vary, but the relational structure among those traits, which ones go together and which oppose, is strikingly consistent across raters and cultures. We test whether the LLM (Qwen 2.5-7B-Instruct) reproduces this structure in its internal trait representations. From millions of crowd-sourced personality ratings of fictional characters, we build a human implicit-personality matrix over hundreds of traits; from contrastive model activations, we build a matching matrix over the same traits. The two relational structures align strongly (Mantel r = 0.77), and the agreement holds trait by trait as well as in aggregate. Two dominant axes of the model's trait representations recover the social and intellectual dimensions long known to organize human personality impressions, social warmth and intellectual competence. On held-out dialogue, projecting model activations onto these directions yields personality profiles that agree with human ratings. This work establishes a framework that enables comprehensive, human-grounded comparison between internal model trait geometry and the shared structure of human personality impressions. Findings of the Association for Computational Linguistics (EMNLP 2026)

**ИИ:** разошлись — Opus ? (другое: Qwen activation projections on character dialogue are compared with crowd personality ratings; this is an activation probe rather than prompted coding, so eligibility is unclear.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Interpretability study comparing internal trait-activation geometry of Qwen with human trait-relation matrices; not an LLM coding or rating texts against human coders.)

**Решение:** -

---

### 928 · R6526

**Exploring the application of large language models in coding the experiencing scale (EXP).**

2026 · Cogent mental health · journal article, journalarticle, article · eng · https://doi.org/10.1080/28324765.2026.2664163

Abstract Psychotherapy process measures like the Experiencing Scale (EXP) offer valuable insight into clinical interactions but are time-intensive to code. Large language models (LLMs) like ChatGPT have the potential to streamline this process, but empirical validation is nascent. This exploratory study aimed to provide a proof-of-concept coding the EXP using ChatGPT with special attention to ethical considerations, limitations, and future directions. ChatGPT was used to code 79 psychotherapy transcripts drawn from the EXP manual. Multiple models of ChatGPT were tested using varied few-shot learning prompt engineering protocols. Data collection occurred in three phases, during which models rated both modal and peak EXP scores for all transcripts. ChatGPT demonstrated moderate agreement with manual reference ratings. An efficient configuration (o3-mini, 5-shot prompting) yielded moderate reliability for both modal EXP scores (ICC[3,1] = .67, 95% CI [.53, .79]) and peak EXP scores (ICC[3,1] = .71, 95% CI [.58, .81]). LLMs may feasibly augment or replace human EXP coders under certain conditions. However, evidence is preliminary and ethical and technical limitations remain. Future research should validate the present methodology using out-of-manual data, assess potential pretraining exposure, and explore locally hosted LLM applications to mitigate privacy concerns.

**ИИ:** + · обе модели · кодирование сессий · ChatGPT coded the Experiencing Scale on 79 psychotherapy transcripts and was compared with the manual's reference ratings (ICC reported).

**Решение:** =

---

### 929 · R6544

**Dep-LLM: Training-Free Depression Diagnosis via Evidence-Guided Structured Multi-factor with Reliable LLM Reasoning**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.10796

Automatic Depression Detection (ADD) from clinical interviews is a pivotal task in computational mental health, yet it remains challenging due to two critical obstacles: 1) difficulty in modeling complex but sparsely distributed depression clues within lengthy, multi-topic clinical interviews, leading to superficial and unreliable reasoning; 2) scarcity of labeled data due to clinical privacy, together with high cost of training and fine-tuning, limiting the deployment of supervised ADD systems. To jointly address these challenges, we propose Dep-LLM, a training-free framework that mirrors the step-by-step reasoning of clinical psychiatrists and operates entirely on frozen off-the-shelf foundation LLMs. Dep-LLM comprises three stages. First, a Chain-of-Thought (CoT) Depression Multi-factor Analysis module structurally decomposes the long dialogue into five clinically aligned themes and produces evidence-grounded rationales, effectively handling long-context dependencies. Second, we introduce Confidence Analysis and Modulation module that quantifies the epistemic reliability from token-level entropy of each rationale and applies an intra-label and inter-theme modulation that amplifies trustworthy signals while suppressing uncertain ones without extra training. Third, a Collaborative Multi-factor Prediction module dynamically integrates multi-factor signals weighted by confidence into the final diagnosis. Extensive experiments on the DAIC-WOZ and E-DAIC datasets demonstrate the effectiveness and generalizability of Dep-LLM: it surpasses zero-shot baseline on nearly all 21 foundation LLMs across 9 metrics such as accuracy, macro F1 and weighted-average F1, and further outperforms state-of-the-art supervised domain-specific LLMs as well as the latest closed-source commercial LLMs, while requiring no extra training.

**ИИ:** разошлись — Opus -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): LLM predicts depression on DAIC-WOZ/E-DAIC, whose labels are self-reported PHQ-8 scores, not human coding of the interview text.); Sonnet ? (неясно, кто ставил эталонные метки: LLM depression detection on DAIC-WOZ interviews; labels are likely PHQ-8 scores (criterion validity), not human coding, but this is unclear from the abstract.)

**Решение:** -

---

### 930 · R6545

**GAIVA: A Generative AI Framework for Human-AI Collaboration in Educational Video Analysis**

2026 · Journal of Educational Data Mining · journalarticle/, article · en · https://doi.org/10.5281/zenodo.20748282

Qualitative video analysis is a foundational yet labor-intensive method in the learning sciences, particularly for investigating the multimodal and collaborative dimensions of learning. This paper introduces GAIVA (Generative Artificial Intelligence for Video Analysis), a novel framework that integrates multimodal large language models (MLLMs) and large language models (LLMs) to support scalable, consistent, and theory-informed video analysis. GAIVA comprises four sequential phases: (1) video preprocessing, (2) MLLM-based behavioral transcription, (3) human-AI collaborative codebook development grounded in theoretical constructs from computer-supported collaborative learning (CSCL), and (4) LLM-based automated coding. Drawing on a case study to analyze simulation-based collaborative science learning, we demonstrate that GAIVA generates rich behavioral transcriptions, enables the construction of stable and theoretically grounded coding schemes, and achieves inter-rater reliability comparable to human annotation. Notably, findings illustrate GAIVA's capacity to support both deductive alignment and inductive discovery. The framework surfaces a behavioral construct--Peripheral Engagement--that is consistent across data batches but absent from existing frameworks. We contribute a systematic and replicable framework for integrating generative AI into qualitative video research, enabling large-scale, multimodal analysis of collaborative learning while preserving analytical rigor, theoretical coherence, and interpretive transparency.

**ИИ:** ? · обе модели · неясен конструкт · LLM codes collaborative learning behaviours from video transcriptions, with reliability compared to humans; unclear whether CSCL constructs count as psychological.

**Решение:** =

---

### 931 · R6551

**Agent Sociodrama: Social-Dynamics-Guided Persona Recasting for LLM Agent Teams**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.15788

Large language model (LLM) agents are increasingly deployed as teams, yet they fail in characteristically social ways: information holders stay silent, dominant speakers anchor groups on wrong answers, and norm violations go unsanctioned. We present Agent Sociodrama, a framework for modeling and validating evolving social dynamics in LLM agent teams. Under fixed personas, agents' emotional states and directed, asymmetric relationships are updated every round by a unified external LLM judge and shape their subsequent interactions. Across six LLM backbones and five social scenarios, we assess social fidelity through classical social-theory patterns and agreement with human judgments. The resulting trajectories exhibit structured social patterns and model-specific differences. We then introduce Trajectory-Guided Persona Recasting (TPR), which diagnoses group-dynamic failures from interaction transcripts and social trajectories and recasts agent personas before rerunning the task. Across four collaborative benchmarks, TPR improves performance from both heterogeneous and randomly initialized agent persona compositions, yielding up to 83.3%p of accuracy improvement over the initial casting. On representative distributed-information cooperation and mixed-motive bargaining tasks, we outperform SOTOPIA and AgentVerse in three of four comparisons, by up to 37.5%p in Pareto rate. These results show that validated social trajectories provide actionable signals for repairing LLM agent teams. Project Page: https://lululu896.github.io/Agent-Sociodrama

**ИИ:** разошлись — Opus ? (неясен конструкт: An LLM judge rates emotional states and relationships in agent-team transcripts and is checked against human judgments; the text is generated by LLM agents, not written by humans.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM agent team framework with LLM judge of simulated agent emotions; not human psychological text, only incidental human-judgment agreement on simulated agents.)

**Решение:** -

---

### 932 · R6558

**Advancing depression detection with role-playing LLMs and synthetic psychological interviews**

2026 · International Journal of Machine Learning and Cybernetics · journalarticle, article · en · https://doi.org/10.1007/s13042-026-03337-5

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM depression detection from interviews, but the reference labels may come from self-report rather than human coding.

**Решение:** =

---

### 933 · R6569

**Developing a pandemic-specific taxonomy and artificial intelligence models for classifying information needs during COVID-19**

2026 · Journal of Information Science · journalarticle, article · en · https://doi.org/10.1177/01655515261478591

This study develops a pandemic-specific taxonomy and artificial intelligence–based classification models to categorize COVID-19-related information needs expressed by the public. A total of 91,772 questions were collected from a leading social Q&A platform in South Korea and analyzed using Python. From this dataset, 10,000 questions were randomly sampled and manually annotated to construct a training corpus. The annotated data were then used to fine-tune two classification models, KoELECTRA and GPT-4o-mini. The analysis identified 12 primary categories of pandemic-related information needs, encompassing both informational and socio-emotional dimensions. The results demonstrate that artificial intelligence–based models can classify large-scale user-generated health queries with a high level of accuracy, offering a scalable alternative to traditional content analysis approaches. These findings suggest that artificial intelligence–based classification systems may support the organization and analysis of online health discourse by facilitating the identification of emerging information needs and patterns. Such systems may complement existing Library and Information Science tools, by enabling more adaptive and context-sensitive approaches to categorizing health-related information in dynamic crisis environments.

**ИИ:** ? · обе модели · неясен конструкт · Fine-tuned GPT-4o-mini classifies COVID questions against human annotations; information-need categories include socio-emotional dimensions, so whether the construct is psychological is unclear.

**Решение:** =

---

### 934 · R6571

**Algorithmic Exploitation in App-Work:Dual Forces of Centralized Control and Financial Vulnerability**

2026 · Academy of Management Proceedings · conference-abstract · en · https://doi.org/10.5465/amproc.2026.19270abstract

The phenomenon of app-workers being vulnerable to exploitation by AI-powered algorithmic management systems is prevalent and has significant implications for both online labor platforms and app-workers. However, existing research has yet to offer a comprehensive conceptualization of this phenomenon or a thorough explanation of its underlying causes. Drawing on a qualitative study using grounded theory, which integrated human coders with Large Language Models (LLMs) in the coding process, we introduce the term “platform algorithmic exploitation” to describe the exploitation phenomenon. We identify three components of platform algorithmic exploitation: algorithmic manipulation, algorithmic pressure, and algorithmic theft. Crucially, we further uncover three mechanisms through which online labor platforms (i.e., the concentration of power to control AI-powered algorithmic management systems in the hands of online labor platforms) and app-workers (i.e., the financial vulnerability of app-workers) jointly contribute to platform algorithmic exploitation: the platform’s profit-seeking mechanism, the behavioral data reinforcement mechanism, and the adaptive lock-in mechanism. Our findings contribute to the understanding of artificial intelligence ethics, broaden the discussion on the implications of AI-powered algorithms for vulnerable workers, and offer novel insights into labor exploitation.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Grounded-theory coding used human coders together with LLMs on worker experiences; unclear whether LLM–human agreement was reported or the construct counts as psychological.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Grounded-theory study of app-worker exploitation using human and LLM coding; labor/management construct, no reported LLM–human agreement on psychological constructs.)

**Решение:** -

---

### 935 · R6597

**HLLC: A Four-Stage Human-AI Collaborative Annotation Framework for Panic Emotion Recognition in Social Networks**

2026 · 2026 12th International Conference on Big Data and Information Analytics (BigDIA) · conference · https://doi.org/10.1109/bigdia71496.2026.11684711

Public emergencies often trigger large-scale panic emotions, which are further amplified by social media, potentially leading to serious consequences such as resource hoarding and social disorder. Therefore, timely identification and intervention of panic are of great significance. However, the development of panic emotion recognition models is severely constrained by the scarcity of high-quality annotated datasets. Existing coarse-grained sentiment classification fails to distinguish panic from fear and anxiety, where the latter two are characterized by high arousal and a sense of loss of control. Furthermore, purely manual annotation is expensive and hard to scale, while fully automated annotation suffers from model hallucinations and conservative bias. To address the challenges in constructing large-scale panic emotion datasets, this paper leverages large language models (LLMs) and proposes a four-stage progressive human-AI collaborative annotation framework named HLLC (Human-LLM Collaborative Labeling). The framework sequentially performs data sampling, LLM initial labeling, crowdsourced verification, and model generalization. Through representative sampling, multi-model consistency comparison for zero-shot labeling, confidence-based sample routing, and BERT fine-tuning, the framework balances annotation quality and efficiency. Experiments on the CrisisNLP Hurricane Sandy dataset [1] show that the HLLC framework achieves a panic F1 score of 0.787 and an overall accuracy of 0.857, improving by 33.3% over lexicon methods and boosting panic recall by 78.7% over pure LLM annotation. These results demonstrate that HLLC enables large-scale, fine-grained panic emotion dataset construction at low cost, offering a practical solution for emergency public opinion monitoring and early warning.

**ИИ:** + · обе модели · бенчмарк с метками людей · LLM zero-shot labelling of panic emotion in social-media posts, scored against a reference that is probably human or crowdsourced (abstract doesn't say).

**Решение:** =

---

### 936 · R6615

**Do Large Language Models Inherit Human Bias? Evidence from Interview Evaluations**

2026 · Academy of Management Proceedings · conference-abstract · en · https://doi.org/10.5465/amproc.2026.12941abstract

With the rapid adoption of large language models (LLMs) in recruitment, growing attention has been directed toward their fairness and potential biases. On the one hand, LLMs do not possess human emotions or cognitive fatigue and are expected to enhance fairness in hiring decisions; on the other hand, they may inherit and even amplify historical biases embedded in training data. As a result, debates persist in both academia and practice over whether LLMs mitigate or exacerbate human bias. Drawing on real interview transcripts from the largest hotel chain in China, this study conducted four empirical investigations to systematically compare human raters and LLMs across multiple forms of bias and to test the effectiveness of prompt engineering interventions. Results show that LLMs avoided certain human biases, such as stereotype-based discrimination against women and candidates with disabilities, and did not exhibit assimilation effects. However, LLMs—similar to humans—significantly reproduced halo and contrast effects and displayed a distinct preference for GPT-styled responses. Moreover, while prompt adjustments and behaviorally anchored rating scales (BARS) reduced the strength of these biases, they did not eliminate them. Overall, this research highlights the dual role of LLMs in recruitment interviews: they have the potential to reduce traditional human biases and create fairer opportunities for vulnerable and minority groups (e.g., women, individuals with disabilities), yet may simultaneously introduce new forms of discrimination that exacerbate inequality. These findings underscore the “double-edged sword” effect of AI in advancing diversity, equity, and inclusion (DEI) within organizational practice.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs and human raters both rate real interview transcripts; it's unclear whether the ratings are of psychological constructs and whether agreement is reported.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM vs human bias in hiring interview ratings; organizational selection context, not a psychological or clinical construct, and it studies bias rather than agreement.)

**Решение:** -

---

### 937 · R6642

**ChildEC: A Developmentally Stratified Chinese Dialogue Corpus for Child Emotion Coaching**

2026 · Poster Volume 0007 The 2026 Twenty-Second International Conference on Intelligent Computing July 23-26, 2026 Toronto, Canada · conference, conference-paper · https://doi.org/10.65286/icic.v22i1.68048

Existing dialogue resources for minors mainly focus on general psychological support, adolescent positive mental health promotion, or broad emotional companionship, and therefore do not adequately support the task of everyday emotion coaching for Chinese children. To address this gap, we construct ChildEC, a developmentally stratified multi-turn dialogue corpus for everyday emotion coaching, targeting Chinese children aged 8--12. The corpus contains 1,709 multi-turn dialogues spanning two developmental stages and five core themes. To support corpus construction and evaluation, we further propose the Theory-Grounded Emotion Coaching Framework (TGEC). Within this framework, TGEC-Synth operationalizes the five-step emotion coaching model and Socratic dialogue into a multi-stage dialogue synthesis pipeline, while TGEC-Eval assesses the quality of child emotion coaching dialogues along six key dimensions. Experimental results show that models fine-tuned on ChildEC consistently outperform their corresponding base models under both automatic metrics and LLM-as-a-Judge evaluation, demonstrating the downstream training value of the corpus for child emotion coaching. Overall, ChildEC provides a specialized data resource and an evaluation reference for developmentally sensitive and theory-consistent research on Chinese child emotion coaching. Our dataset will be publicly released upon acceptance of the paper.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mainly a synthetic corpus, but an LLM judge rates emotion-coaching quality; unclear whether the judge was checked against human ratings.

**Решение:** =

---

### 938 · R6652

**MIS-Bench: Benchmarking Multimodal LLMs for Psychotherapeutic Interpersonal Skills Assessment**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.22778

Multimodal large language models (MLLMs) are increasingly used as evaluators, yet their reliability in professional assessment tasks that require expert judgment remains unclear. We investigate this challenge in the context of assessing psychotherapeutic interpersonal skills and introduce MIS-Bench, a Multimodal Interpersonal Skills (MIS) benchmark comprising 996 psychotherapy response videos annotated across 8 dimensions of Facilitative Interpersonal Skills. Across 9 MLLMs with multiple modality and prompting settings, we find that current models show only modest agreement with human experts, inconsistent gains from multimodal input, and limited benefits from reasoning-based prompting. To mitigate this gap, we propose MIS-RAFT, a regression-aware fine-tuning method inspired by RAFT and tailored to fine-grained interpersonal skill scoring at one-decimal precision. MIS-RAFT addresses the mismatch between autoregressive token prediction and scalar-valued expert assessment, significantly improving agreement with human ratings. Overall, MIS-Bench reveals a clear gap between general multimodal capability and expert-level interpersonal judgment, while MIS-RAFT offers a promising path toward more reliable model-based assessment.

**ИИ:** + · обе модели · бенчмарк с метками людей · MLLMs score Facilitative Interpersonal Skills in psychotherapy responses (multimodal, probably including transcripts); agreement with human expert ratings is reported.

**Решение:** =

---

### 939 · R6660

**Can LLM-Based Social Desirability Ratings Substitute for Human Ratings? Validation of the Full Pipeline for Forced-Choice Personality Scale Construction**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/xca6z

This study aims to evaluate, across the full pipeline, whether large language models (LLMs) can substitute for human raters in collecting the item-level social desirability ratings required for constructing a forced-choice (comparative) scale. When forced-choice scales are used for measurement, it is important to employ item pairs that are matched on social desirability. However, collecting such rating data from human raters is costly and time-consuming, creating a bottleneck in scale construction. If LLM-based ratings correspond sufficiently well to human ratings, the scale construction process may be streamlined. Previous studies have examined the potential of Transformer/LLM-based approaches to approximate human social desirability judgments (e.g., Hommel, 2023; Leistner et al., 2025). Other work has focused on the stability of LLM ratings and correlations among ratings produced from different LLMs (e.g., Shu et al., 2024; Huang et al., 2024), as well as partial implementations of forced-choice block construction using LLM ratings (e.g., Li et al., 2025). However, to the best of our knowledge, no study has consistently evaluated and validated the entire process from “LLM rating → desirability matching → forced-choice scale → psychometric evaluation using human data.” This study consists primarily of three stages. First, LLMs will provide social desirability ratings for both the sentence- and adjective-format items of the HEXACO-60, and the degree of agreement with existing human rating data will be examined quantitatively from the perspective of convergent validity (correlation). Second, forced-choice scales will be constructed on the basis of LLMs’ social desirability ratings, and the resulting scales will be compared with scales constructed on the basis of human ratings. Third, a survey with human participants will be conducted using the forced-choice scale optimized on the basis of LLM ratings and the forced-choice scale optimized on the basis of human ratings, and the equivalence of the resulting latent trait estimates will be evaluated. By integrating the results of these three stages, we will examine whether LLM-based social desirability ratings can substitute for human ratings in the process of constructing a forced-choice scale.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: Pre-registration/protocol with no results yet; LLM social desirability ratings of HEXACO items would be compared with human ratings.); Sonnet ? (неясен конструкт: LLMs rate social desirability of HEXACO-60 items, compared with human ratings of the same items. The texts are questionnaire items, not clinical or response text, so fit is borderline.)

**Решение:** -

---

### 940 · R6666

**A Two-Stage Selective Escalation Framework for Robust Suicide Risk Detection on Social Media: Machine Learning Study (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.95663

BACKGROUND Suicide rates have risen worldwide in recent years, underscoring the urgent need for proactive and scalable prevention strategies. Social media has emerged as a valuable source for early screening, as many at-risk individuals who avoid formal help due to stigma express distress online. However, current suicide risk detection systems face a critical limitation: while explicit suicidal expressions are relatively easy to identify, implicit suicidal ideation conveyed through metaphor, sarcasm, or subtle emotional cues remains difficult to detect and constitutes a major source of system failure in real-world deployment. OBJECTIVE This study aims to develop a robust and computationally efficient suicide risk detection framework that can reliably handle both explicit and implicit expressions while controlling inference cost and improving practical deployability for mental health screening. METHODS We propose a robust and efficient two-stage framework that explicitly accounts for heterogeneous signal strength through selective escalation. In Stage 1, a lightweight Bidirectional Encoder Representations from Transformers (BERT) classifier rapidly resolves high-confidence explicit cases. In Stage 2, only ambiguous inputs are escalated for further analysis through two complementary mechanisms: (i) a multi-perspective large language model (LLM) voting strategy designed to improve recall on implicit suicide risk, and (ii) a feature-based machine learning ensemble guided by psychologically grounded indicators extracted via prompt-engineered LLMs, enabling efficient inference and enhanced interpretability. RESULTS We evaluate the proposed framework on two complementary datasets representing distinct risk profiles: an explicit-dominant Reddit dataset and an implicit-only DeepSuiMind dataset. The framework achieves an F1 score of 98.0% on the Reddit benchmark and up to 99.94% recall on the implicit-only DeepSuiMind benchmark (positive-only; precision is not defined). It reduces the cross-domain performance gap to approximately 1.2-1.4% in recall and 1.7-2.2% in F1, and significantly lowers LLM invocation costs compared with single-model baselines. CONCLUSIONS These results demonstrate that system-level design with selective escalation offers a practical and effective pathway for suicide risk detection systems that are both robust to implicit expressions and efficient enough for real-world mental health screening applications. CLINICALTRIAL N/A

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM voting detects suicide risk in Reddit/DeepSuiMind posts; unclear whether benchmark labels come from human annotation or subreddit membership.

**Решение:** =

---

### 941 · R6667

**LLM-Enhanced Modeling of Social Desirability-Aware Forced-Choice Personality Assessment**

2026 · Electronics · journalarticle, article · en · https://doi.org/10.3390/electronics15091792

Personality assessment serves as a key building block in intelligent information systems that enable human-centered modeling. Unlike cognitive tests, personality assessments rely primarily on self-reports and are therefore susceptible to faking. Forced-choice (FC) formats partially mitigate this problem, yet socially desirable responding remains a systematic source of bias. Traditional approaches rely on expert-annotated social desirability (SD) ratings to construct FC item blocks and infer respondents’ personality traits from block-level rankings. This rating procedure is labor-intensive and coarse-grained. Furthermore, existing methods neglect the non-linear SD interactions between respondents and items, which act as structured adversarial noise that hinders the recovery of true latent traits. To address these challenges, we propose the Social Desirability-aware Forced-Choice Diagnosis (SDFCD) approach. Our approach adopts a knowledge-guided learning paradigm by leveraging large language models (LLMs) to distill fine-grained, continuous SD ratings, thereby replacing sparse expert ratings. We then introduce a decoupled neural interaction module that jointly represents latent personality traits and SD tendencies, enabling the modeling of respondent–item SD interactions. Experiments on real assessment data demonstrate that our method significantly outperforms baseline FC models in personality trait diagnostic performance and model interpretability. This study highlights the potential of LLMs for automated, fine-grained SD quantification and offers a scalable path toward more trustworthy personality assessment.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM rates social desirability of personality items in place of expert ratings; unclear whether LLM-expert agreement is reported, and the texts are test items.

**Решение:** =

---

### 942 · R6668

**Agency Predicts Progress in Ancient China: A Large Language Model Approach**

2026 · Research Square · preprint · https://doi.org/10.21203/rs.3.rs-9575403/v1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM likely codes agency (a psychological construct) in historical texts, and might be validated against human coders.

**Решение:** =

---

### 943 · R6672

**Does Capability Transfer to Subjective Behavior -- and Would Our Instruments Tell Us? A Self-Evolving, Trust-by-Construction Evaluation Paradigm**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.27914

Benchmarking is mature where answers are verifiable -- math, code, reasoning -- but the fastest-growing uses of LLMs are subjective and human-facing: companionship, emotional support, counseling. There the default validity test, correlating a metric to human judgment, has no stable anchor: inter-rater agreement is low, structured by annotator identity, barely reproducible, and length-biased. So we cannot answer the question that matters: does capability that scales on objective benchmarks transfer to subjective behavior, and would our instruments even tell us if it did not? We build an instrument for this regime and report what it reveals at the frontier. We contribute, first, a self-evolving instrument that selects and then authors its own behavioral dimensions under a multiplicative anti-gaming fitness, self-halting when it stops improving; second, a trust-by-construction paradigm that earns belief through three certificates established without a human gold standard, where human raters saturate (rho ~ 0.45); and third, the finding it makes visible -- capability transfer is dissociable. Across 49 models, 8 families, and 24 months, subjective behaviors are where objective-benchmark scaling fails to carry over: the sharpest case, advice-restraint (knowing when not to give advice), is the frontier's universal-lowest dimension, and at gpt-4.1-&gt;gpt-5 it ran backwards while the aggregate score hid it -- a regression one instruction recovers. Warm restraint is moved by model generation, not by raw scale, MoE width, inference budget, or reasoning mode; the open-weight Pareto frontier matches closed flagships at ~10-80x lower per-call cost; and four judge families replicate the rubric on held-out human ESConv conversations. Data, code, the locked rubric, and judge prompts will be released upon publication.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM judges rate emotional-support behaviour, but validation is designed to work without a human gold standard. It's unclear whether LLM–human rating agreement is reported.

**Решение:** =

---

### 944 · R6680

**Creating Multilingual Mental Health Dialogue Datasets: Limits of Persona-Based Localization via Nationality and Language**

2026 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, journalarticle, preprint/article · https://doi.org/10.18653/v1/2026.clpsych-1.11

AI and large language models (LLMs) have emerged as promising tools to address global mental health challenges. Despite the global nature of these challenges, there remains a critical shortage of high-quality datasets for training and evaluating such systems. To mitigate this gap, researchers increasingly generate synthetic clinical personas to simulate user data and test digital mental health support systems. However, most validated personas rely on English-centric contexts. This paper investigates whether similar persona-based methods can be used to generate multilingual mental health datasets. We modified nationality and language parameters in personas to generate clinical dialogues in Mandarin, Bengali, and Hindi. We then examined how different LLMs perform when evaluating the depression severity of these generated multilingual datasets against the baseline in English. Our findings indicate that just adding nationality and language parameters in personas might not be adequate, as it can introduce clinical inconsistency across languages. LLM judge models often exhibit inaccuracies in assessing depression severity in non-English texts, with performance varying across different models. This exposes the systemic limitations of applying English-centric personas to multilingual contexts. Ultimately, our work highlights the urgent need for culturally responsive data generation to ensure equitable mental health systems globally. 15 pages, 4 figures. Accepted to the 2026 Workshop on Computational Linguistics and Clinical Psychology (CLPsych 2026), co-located with ACL 2026

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM judges rate depression severity in synthetic dialogues; the reference appears to be persona-assigned severity, and any human ratings are unclear.

**Решение:** =

---

### 945 · R6696

**Can We Trust LLMs for Mental Health-Based Decisions? A Causality Aware Reliability Analysis**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-31319-5_17

Mental health concerns constitute a global burden as they affect individuals’ functional, behavioral, and cognitive abilities. Unfortunately, people who suffer from mental health issues do not get enough professional help, which necessitates the use of automatic tools for early risk identification. Large Language Models (LLMs), as emerging models, have a broad usage including mental health screening. However, there is not enough research about the trustworthiness and responsibility of these systems. In this research, we investigate whether, although LLMs have high predictive performance, these models follow clinical reasoning or if there are mainly spurious correlations. We analyse Qwen2.5-7B on depression, stress, and suicidal ideation detection to investigate if its internal attention mechanism reflects clinical reasoning. We further identify and correct a theoretical flaw in attention based causal discovery for mental health by introducing contrastive TF-IDF and directed Pointwise Mutual Information (PMI) and validated by three independent LLM judges across all three disorders.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: Qwen2.5 detects depression, stress and suicidal ideation in text; the source of the dataset labels (human-annotated or not) is unclear, and the focus is interpretability.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): Interpretability/attention analysis of Qwen on depression, stress, suicide detection; LLM judges validate causal terms, no human-coded reference agreement evident.)

**Решение:** -

---

### 946 · R6701

**A Multi-Agent LLM Framework for Occupational Psychological Profiling: Reliability and Validity Evidence From 1,636 Chinese Occupations**

2026 · OSF Preprints (OSF Preprints) · preprint

Code, data, and per-occupation outputs for the paper “Multi-Agent LLMs for Occupational Profiling: Psychometric Validation on 1,636 Chinese Occupations.” Three LLMs act as separate expert raters, with a separate arbitrator, to score all 1,636 occupations in the 2022 Chinese Occupational Classification on Holland RIASEC and Big Five. The repository includes the scoring pipeline (occ-psych-agent/) and the R/Python analysis that reproduces every result, table, and figure (analysis/). The paper's tables and figures can be regenerated without an API key.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM agents rate occupation descriptions on RIASEC/Big Five; unclear whether validity is checked against human expert ratings or only between LLMs.

**Решение:** =

---

### 947 · R6707

**DemMA: Dementia Multi-Turn Dialogue Agent with Expert-Guided Reasoning and Action Simulation**

2026 · arXiv (Cornell University) · journalarticle, conference, preprint/article · https://doi.org/10.48550/arxiv.2601.06373

Simulating dementia patients with large language models (LLMs) is challenging due to the need to jointly model cognitive impairment, emotional dynamics, and nonverbal behaviors over long conversations. We present DemMA, an expert-guided dementia dialogue agent for high-fidelity multi-turn patient simulation. DemMA constructs clinically grounded dementia personas by integrating pathology information, personality traits, and subtype-specific memory-status personas informed by clinical experts. To move beyond text-only simulation, DemMA explicitly models nonverbal behaviors, including motion, facial expressions, and vocal cues. We further introduce a Chain-of-Thought distillation framework that trains a single LLM to jointly generate reasoning traces, patient utterances, and aligned behavioral actions within one forward pass, enabling efficient deployment without multi-agent inference. Extensive evaluations with experts, medical students, and LLM judges demonstrate that DemMA significantly outperforms strong baselines across multiple metrics.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly a dementia patient-simulation study; experts and LLM judges both rated the outputs, but it is unclear whether their agreement is compared.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Dementia patient simulation agent; humans and LLM judges rate generated outputs, with no LLM coding of psychological text against human labels.)

**Решение:** -

---

### 948 · R6708

**ActTraitBench: Quantifying the Knowledge-Decision Gap in Large Language Models via Human-Grounded Behavioral Validation**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.29791

While Large Language Models (LLMs) can convincingly simulate personas in explicit self-reports, they often deviate in implicit behavioral decisions, revealing a substantial Knowledge-Decision Gap ($G_{\mathrm{KD}}$). Existing benchmarks struggle to measure this discrepancy due to limited construct validity, multidimensional entanglement, and distributional biases in LLM-based evaluation. To address these issues, we propose ActTraitBench, a human-grounded evaluation framework for measuring personality consistency in LLMs. Grounded in empirical human data, ActTraitBench establishes one-to-one mappings between psychometric facets and behavioral paradigms and applies Distributional Calibration via Quantile Mapping to reduce distributional mismatch between LLM-judge scores and human responses. Experiments on 14 mainstream LLMs reveal substantial knowledge-decision gaps and show that assigned personas are reflected more consistently in self-reports than in behavioral decisions for most evaluated models. To mitigate this gap, we further introduce the Chain of Cognitive Alignment (CoCA), an inference-time intervention that reduces $G_{\mathrm{KD}}$ for 12 of the 13 models with paired results. Code and resources are available at https://github.com/Selina233/ActTraitBench. Accepted to Findings of EMNLP 2026. Camera-ready version

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM judge scores personality from persona behaviour; calibrated to human response distributions. Unclear whether humans rated the same texts.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Benchmark of LLM persona simulation consistency; LLM-judge scores are calibrated to human response distributions, not coded against human labels of the same texts.)

**Решение:** -

---

### 949 · R6713

**MAAM: Anchor-Preserving Compression and Contextual Calibration for Chinese Discriminatory Language Detection**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.09114

Chinese discriminatory-language detection is challenging because harmful intent is often implicit and context-dependent. We propose MAAM (Myopia--Astigmatism Anchor Mechanism), a lightweight, model-agnostic framework inspired by functional visual blur: rather than preserving every token equally, MAAM retains discrimination-relevant semantic anchors and calibrates them with C--I--S contextual priors (Contextual Tone, Group Identity, and Stance Polarity). We also introduce ChLGBT, to our knowledge the first Chinese LGBT-focused discriminatory-language dataset, with 8,120 manually annotated samples and three ordinal labels: explicit bias, implicit bias, and emotional intensity. Across strong encoder baselines, MAAM improves all three prediction dimensions, with consistent gains in accuracy, F1, Brier score, and expected calibration error. Compared with frontier LLM baselines under zero-shot and few-shot prompting protocols, MAAM remains competitive while offering stronger compactness and stability. These results suggest that interpretable anchor preservation and contextual calibration provide a practical alternative to heavier model scaling for Chinese discriminatory-language assessment.

**ИИ:** разошлись — Opus ? (неясен конструкт: Mainly discriminatory-language (hate speech) detection, but LLM baselines are scored against human-annotated emotional-intensity labels; this may count as an emotion construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Discriminatory-language (hate speech-type) detection with an encoder-based proposed method; LLMs only as baselines, and the construct is not psychological or clinical.)

**Решение:** -

---

### 950 · R6722

**StanceBench: A Benchmark for Audio LLM-Based Interpersonal Stance Evaluation from Speech**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.22658

Speech-to-speech dialogue models increasingly depend on prosody and interactional nuance to convey social intent, yet benchmarks for these cues remain limited. We introduce StanceBench, a benchmark for measuring interpersonal stance in conversational speech and evaluating audio-capable LLMs as automated judges. Using the Seamless Interaction corpus, StanceBench (1) specifies 9 stance dimensions via role-prompt poles, (2) standardizes single-speaker and interaction-based evaluations, and (3) reports LLM-as-a-judge robustness, bias, and stance inference. Across evaluated stances, empathy and politeness are the easiest. Warmth and assertiveness are moderately separable with positivity skew/asymmetry. Honesty is the hardest and shows high prompt order bias, consistent with needing cross-turn evidence. Attentiveness is separable but aligns weakly with humans. Interaction stances are more context-sensitive, with threshold gaps and high variance, especially conflict regulation. Accepted to Interspeech 2026

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Audio LLM judges rate interpersonal stance (empathy, warmth); the references are mainly role-prompt poles, though some human alignment is reported. Input is speech rather than text.

**Решение:** =

---

### 951 · R6730

**Retrospective Analysis of Cognitive Distortions and Recovery Outcomes in Persistent Post-Concussion Symptoms (PPCS) via Natural Language Processing**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/zeb8f

This is a survey project designed to elicit retrospective thoughts and feelings about participants concussions. The survey includes symptom recollection forms and open ended prompts about the injury. The responses to the prompts will be analyzed using a localized LLM to detect cognitive distortions. The distorted and healthy language groups will be compared to each other in the symptom and emotional domains.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: OSF pre-registration (protocol) of planned LLM cognitive-distortion detection; no results and no stated human coding comparison.); Sonnet ? (неясно, сравнивали ли с людьми: Pre-registration: a local LLM detects cognitive distortions in open-ended responses; the abstract doesn't say whether humans code the same texts for validation.)

**Решение:** -

---

### 952 · R6733

**Measurement Invariance of Machine Empathy**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/85hg9

Purpose. Large language models are now used as "judges" to score the empathy of AI-generated responses, and these scores are load-bearing across the field: systems are ranked, fine-tuned, and safety-evaluated against them. Yet the validity of empathy-as-scored has never been formally established. This project asks whether LLM-judged empathy is a coherent, transportable measurement — or an artifact of the particular judge, rubric, and dataset a researcher happens to choose. We treat "empathy score" from the measurement-modeling perspective (Jacobs &amp; Wallach, 2021; Cronbach &amp; Meehl, 1955): as a measurement of a theorized construct whose reliability and validity must be demonstrated rather than assumed. Design. We conduct, to our knowledge, the first fully crossed judge-evaluation experiment: nine judge models spanning four classes (frontier API models, mid-tier API and prompted open-weight models, purpose-trained evaluator models, and an author-trained fine-tuned encoder) × three rubric conditions (undefined dimension labels, anchored definitions, single holistic score) × seven corpora spanning distinct support domains (peer support, strategy-annotated support dialogues, motivational-interviewing transcripts with expert quality tiers, CBT sessions with clinician fidelity ratings, counseling Q&amp;A with licensed-professional ratings, and human-labeled crisis conversations) × three repetitions — approximately 193,000 judgments — anchored by a 480-item calibration set rated independently by three raters with counseling/clinical-psychology training. Confirmatory analyses (specified in the registered preregistration): factor-structure and discriminant-validity tests of multi-dimension rubrics; ordinal multi-group confirmatory factor analysis testing configural→threshold→loading invariance across domains, with registered controls for response-authorship and response-length confounds; known-groups validity against clinically validated quality tiers; a test of whether crisis content contaminates empathy scores independent of expert-rated response quality; judge–expert agreement by domain; and a generalizability-theory variance decomposition estimating what fraction of a reported empathy score reflects the instrument (judge, rubric, sampling) rather than the response being scored. Expected outcomes. Either empirical result is informative: if empathy scores fail invariance and validity tests, a substantial portion of empathy-evaluation practice rests on unlicensed generalization, and the field requires the instruments this project releases; if the scores pass, the field gains its first formally validated empathy-judging protocol. Planned outputs include the quantitative findings, an open evaluation battery, a psychometric "datasheet" methodology for auditing empathy judges, and a calibrated open judge model — intended to make "we used an LLM judge" an auditable methods decision rather than an assumption.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: Pre-registration protocol for LLM empathy judges compared with expert raters; no results yet, and protocols are excluded.); Sonnet + (LLM-судья: Preregistered study of LLM judges scoring empathy in support/counseling/MI/CBT/crisis texts, with judge–expert agreement and a human-rated calibration set.)

**Решение:** -

---

### 953 · R6748

**OmniOPSD: Rationale-Privileged On-Policy Self-Distillation for Affective Computing**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.15920

Reinforcement learning for multimodal large language models (MLLMs) is often hindered by severe reward sparsity in complex reasoning tasks. This challenge is particularly pronounced in human-centered scenarios involving states, emotions, intentions, and behaviors, where heterogeneous multimodal signals and subjective human factors make high-quality chain-of-thought (CoT) annotations expensive and difficult to obtain. Although many multimodal datasets provide expert-annotated ground-truth labels, directly using these labels for supervised fine-tuning may encourage shortcut learning in multimodal perception and provides limited transparency for safety-critical human--AI interaction. To address these limitations, we propose OmniOPSD, a Rationale-Privileged On-Policy Self-Distillation framework that uses frontier-generated rationales as teacher-side privileged evidence rather than student imitation targets. OmniOPSD uses frontier-generated evidence-aware rationales only as training-time privileged evidence context for a local teacher. The student samples its own rollout from the original multimodal input, while the rationale-privileged teacher scores the same tokens and provides dense token-level supervision. Thus, the student learns on its own trajectory distribution without directly imitating frontier-model completions, and inference requires no labels, rationales, CoT annotations, or closed-source model access. Experiments on MER-UniBench show that OmniOPSD achieves state-of-the-art performance with an average score of $84.19$, and ablations further support the value of rationale-privileged teacher guidance.

**ИИ:** разошлись — Opus ? (другое: Multimodal LLM emotion recognition evaluated on MER-UniBench against expert labels; mainly video/audio, text role and human-label agreement unclear.); Sonnet -7 (другое — напишите почему: Multimodal LLM training method (self-distillation) for emotion recognition on MER-UniBench; model-performance work on audio/video, not LLM–human coder agreement on psychological text.)

**Решение:** -

---

### 954 · R6763

**CogManip: Benchmarking Manipulative Behavior in Multi-Turn Interactions with Large Language Model**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.06099

Whether Large Language Models (LLMs) exhibit covert psychological manipulation in complex human-AI interactions has garnered increasing safety concerns. However, existing AI safety benchmarks remain largely restricted to explicit rule compliance and static prompts, failing to capture the dynamic and covert nature of manipulative strategies in multi-turn dialogues. We introduce CogManip, a comprehensive benchmark that evaluates 15 manipulation strategy risks across 1,000 multi-turn interaction scenarios, validated by human experts. A systematic evaluation of 13 representative models, including frontier models like GPT-5.4 and DeepSeek-V3.2, reveals significant risk heterogeneities and illuminates the targeted direction for future defense. Further analysis of objective function perturbation reveals that DeepSeek-V3.2's manipulation tactics are highly sensitive to both negative and benign system prompts, demonstrating the critical necessity of prompt-based defense engineering and implicit goal auditing. CogManip offers a robust instrument and perspective for auditing the implicit psychological influence and dynamic strategy selection of modern LLMs.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Benchmark of psychological manipulation in LLM dialogues; an LLM judge is likely, but whether experts validated the judge's labels or only the scenarios is unclear.

**Решение:** =

---

### 955 · R6764

**Automating Adult Attachment Interview Classification Using Large Language Models**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/b94km

This project investigates whether large language models (LLMs) can be used to support the automated classification of Adult Attachment Interview (AAI) transcripts in a way that is theoretically aligned with established AAI coding principles. The Adult Attachment Interview is widely regarded as a gold-standard measure of adult attachment, but its reliance on expert judgment makes it time-intensive and difficult to scale. Recent advances in large language models provide new opportunities to analyse complex psychological texts at the level of discourse and reasoning, rather than relying solely on surface linguistic features. However, their application to AAI transcripts remains largely unexplored. The study consists of two stages. In Study 1, an instruction-following large language model deployed within a secure Azure environment will be used to perform zero-shot classification of English AAI transcripts into four attachment categories: Secure, Dismissing, Preoccupied, and Unresolved. The model will be prompted to base its judgments on core AAI coding principles, such as coherence of discourse, balance of evaluations of attachment figures, and lapses in reasoning around loss or trauma. Model outputs will be compared against expert-coded attachment classifications. In Study 2, the same model will be fine-tuned using a subset of labelled transcripts to examine whether task-specific alignment improves classification performance and the quality of model-generated explanations. Performance will be evaluated using standard classification metrics, alongside qualitative assessment of the model’s reasoning. All data processing and analysis will take place within a secure institutional computing environment, and no data will be stored or processed locally. This project aims to contribute to methodological discussions around the use of large language models in clinical and developmental psychology, and to explore their potential role in supporting, rather than replacing, expert-based attachment assessment.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: OSF pre-registration with no results: planned LLM AAI classification vs expert codes. Topic is relevant, so look for a later results paper.); Sonnet + (подсчёт методики: Pre-registered study: LLM classifies AAI transcripts into attachment categories, compared with expert-coded classifications; fits assessment scoring.)

**Решение:** -

---

### 956 · R6767

**An fMRI dataset of verbalized spontaneous thought with annotated transcripts and self-report trait measures.**

2026 · bioRxiv : the preprint server for biology · journal article, preprint, journalarticle · eng · https://doi.org/10.64898/2026.05.12.724488

Spontaneous thought is pervasive in everyday human cognition, yet datasets capturing its neural dynamics under minimally interrupted conditions remain limited. The current dataset was acquired from a think-aloud functional MRI experiment in which 118 participants continuously verbalized their spontaneous thoughts during 10-minute scanning sessions. The raw MRI data and verbal transcripts with sentence-level timestamps were previously released and analyzed in our prior study examining neural activity associated with thought transitions. Building on that release, we additionally provide preprocessed MRI data, speech transcriptions with word-level timestamps aligned to image acquisition, large language model-generated ratings of transcribed thoughts across emotional and sensory dimensions, and self-report survey measures assessing personality, mental health, and cognitive abilities. Validation analyses demonstrated activation in expected cortical regions associated with speech production and sensory content identified from transcript annotations, agreement between language model and human ratings, and adequate internal consistency of survey measures, supporting the dataset's overall quality. This dataset enables reuse for investigations of spontaneous thought, speech generation, and individual differences using naturalistic functional MRI data.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · An LLM rated think-aloud transcripts on emotional and sensory dimensions, and the paper reports how well those ratings agreed with human ratings.

**Решение:** =

---

### 957 · R6768

**Automated Symptom Identification from Clinical Interview Transcripts in Diagnosed Schizophrenia: A Multi-Agent LLM Framework.**

2026 · Studies in health technology and informatics · journal article, med, journalarticle · eng · https://doi.org/10.3233/shti260324

We present a multi-agent LLM framework for automated evaluation of symptom-criteria consistency in diagnosed schizophrenia cases. Our system decomposes evaluation into seven specialized agents with RAG-augmented DSM-5/ICD-11 knowledge: symptom extraction, standard matching, differential diagnosis, temporal analysis, counterfactual reasoning, voting, and arbitration. Evaluated on 71 diagnosed cases, our framework achieves 95.8% PPA (Positive Percent Agreement), outperforming single-agent baseline (70.4%) by 25.4% and single-agent+RAG (87.3%) by 8.5%. Because the dataset is case-only, results reflect case detection rather than screening accuracy; specificity is not estimable. Ablation reveals RAG contributes +16.9% and multi-agent specialization adds +8.5%, demonstrating both are critical for psychiatric symptom-criteria evaluation. Overall, our seven-agent RAG framework structures and traces interview-based symptom-to-criterion assessment and offers a scalable automated prototype; clinical use still requires multi-center validation with controls and first-episode cases to confirm specificity and external generalizability.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Multi-agent LLM finds symptoms in schizophrenia interview transcripts; agreement seems to be with the diagnosis, but clinician symptom ratings may exist.

**Решение:** =

---

### 958 · R6773

**Granularity paradox: how emotion taxonomies shape GPT-5's affective cognition and human-AI alignment.**

2026 · Frontiers in psychology · journal article, journalarticle, article · eng · https://doi.org/10.3389/fpsyg.2026.1786724

Background: Large Language Models (LLMs) have demonstrated exceptional capability in textual emotion detection. However, LLM evaluations often treat the emotion taxonomy-the "cognitive ruler" defining the emotional space-as a neutral background variable. The extent to which taxonomic complexity moderates LLM performance remains underexplored. Method: This study systematically evaluates the impact of emotion taxonomy on GPT-5's annotation behavior. We constructed a dataset of 2,848 Chinese Weibo posts. Five human annotators and GPT-5 (zero-shot) labeled the data across five distinct taxonomies, each with varying levels of granularity: SemEval (4 classes), Ekman (6 classes), Chinese SevenEmotions (7 classes), Plutchik (8 classes), and GoEmotions (27 classes). A rigorous experimental design, including randomized ordering and washout periods, was implemented to minimize sequence effects. By comparing the results of GPT-5 and manual annotation, the analysis is conducted across three dimensions: performance, consistency, and bias patterns. Results: Results reveal a significant "granularity paradox": GPT-5's performance is strongly negatively correlated with taxonomic complexity, with performance collapsing in fine-grained settings (GoEmotions). Crucially, we identified systematic misalignment mechanisms: (1) Consistency decay: Human-AI agreement significantly deteriorates as semantic boundaries blur in complex taxonomies; (2) Hyper-sensitivity bias: GPT-5 exhibits a tendency to over-interpret neutral texts as emotional, with false-positive rates increasing with taxonomy size; and (3) Arousal shift: The model consistently misclassifies low-arousal negative emotions (e.g., sadness) as high-arousal prototypes (e.g., fear/anger), reflecting a valence-based rather than nuance-based inference logic. Notably, the indigenous SevenEmotions did not yield superior cultural alignment compared to Western taxonomies. Conclusion: Our findings suggest that emotion taxonomies function as a critical hyperparameter that shapes the cognitive boundaries of GPT. While GPT shows promise, its reliability is compromised by complex taxonomies. Researchers must balance granular detail against model robustness when deploying LLMs for psychological analysis.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-5 and five human annotators labeled emotions in 2,848 Weibo posts using five taxonomies; the study reports human-AI agreement.

**Решение:** =

---

### 959 · R6801

**Examining Social Attribution in LLM Reasoning: A Theory-Guided Probing Methodology**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.12022

Large language models (LLMs) are increasingly deployed in sociotechnical systems where social attribution, the reasoning process attributing external events to the causes and reasons of agents' social behaviors, plays a critical role. These processes involve judgments of social cause, responsibility, and blame/credit to agents. Although attributional models are well-studied in social psychology and cognition through Attribution Theory, social attribution remains underexplored in AI, particularly LLM social reasoning. This paper provides the first systematic exploration of LLM social attribution. Our work focuses on responsibility and blame attributions, examining current LLMs' judgments and their underlying internal mechanisms. Guided by attribution theory, we construct a social attribution benchmark consisting of a Vignette subset based on classic scenarios from attribution theory research and a Reality subset based on real-world social narratives, yielding 7,639 responsibility/blame judgment questions. On this basis, we evaluate 32 representative LLMs and 5 basic non-LLM baselines. To further explore the internal mechanisms underlying the LLM judgment process, we develop a probing-based methodology to investigate the latent-space representations of 5 key attribution dimensions and the consistency of their influences on LLM judgments compared to those in human social attribution. Our research findings reveal that current LLMs exhibit measurable but incomplete agreement with human responsibility and blame judgments, and meanwhile, this agreement is positively correlated with model size. Some attribution dimensions are systematically decodable from specific positions in LLM hidden states, and their influences on the final judgment are consistent with those indicated by human Attribution Theory. The dataset and associated code are available at https://github.com/Yuzhaoxin946/SAB-Bench.

**ИИ:** ? · обе модели · неясен конструкт · LLM responsibility/blame judgments on vignettes and narratives compared with human judgments; unclear whether this is coding of psychological text or LLM-as-participant reasoning.

**Решение:** =

---

### 960 · R6812

**Enhancing LLM-Based Data Annotation with Error Decomposition**

2026 · International Learning Analytics and Knowledge Conference (LAK) · journalarticle, book, preprint/article · https://doi.org/10.1145/3785022.3785070

Large language models (LLMs) offer a scalable alternative to human coding for data annotation tasks, enabling the scale-up of research across data-intensive domains such as learning analytics. While LLMs are already achieving near-human accuracy on objective annotation tasks, their performance on subjective annotation tasks, such as those involving psychological constructs, is less consistent and more prone to errors. Standard evaluation practices typically collapse all annotation errors into a single alignment metric, but this simplified approach may obscure different kinds of errors that affect final analytical conclusions in different ways. Here, we propose a diagnostic evaluation paradigm that incorporates a human-in-the-loop step to separate task-inherent ambiguity from model-driven inaccuracies and assess annotation quality in terms of their potential downstream impacts. We refine this paradigm on ordinal annotation tasks, which are common in subjective annotation. The refined paradigm includes: (1) a diagnostic taxonomy that categorizes LLM annotation errors along two dimensions: source (model-specific vs. task-inherent) and type (boundary ambiguity vs. conceptual misidentification); (2) a lightweight human annotation test to estimate task-inherent ambiguity from LLM annotations; and (3) a computational method to decompose observed LLM annotation errors following our taxonomy. We validate this paradigm on four educational annotation tasks, demonstrating both its conceptual validity and practical utility. Theoretically, our work provides empirical evidence for why excessively high alignment is unrealistic in specific annotation tasks and why single alignment metrics inadequately reflect the quality of LLM annotations. In practice, our paradigm can be a low-cost diagnostic tool that assesses the suitability of a given task for LLM annotation and provides actionable insights for further technical optimization.1

**ИИ:** ? · обе модели · неясен конструкт · LLM annotations are compared with human labels on four educational ordinal tasks; it is unclear whether these involve psychological constructs.

**Решение:** =

---

### 961 · R6813

**The Effects of Dual-Pathway AI Assistance on Divergent Thinking in Tasks of Varying Semantic Richness**

2026 · Creativity Research Journal · article · en · https://doi.org/10.1080/10400419.2026.2721513

Generative artificial intelligence (AI) shows promise for enhancing creative performance, but its capacity to augment human creative thinking remains debated. Grounded in the dual-pathway model of creativity, this study investigates how two AI assistance strategies, flexible (promoting cross-category exploration) and persistent (promoting within-category deepening), influence divergent thinking across tasks differing in semantic richness. In a within-subjects design (N = 35), participants completed the Alternative Uses Task for semantically rich and sparse objects under three assistance conditions: flexible AI, persistent AI, and no-AI baseline. Using a turn-taking brainstorming paradigm, the AI provided tailored cues after each participant’s idea. Results revealed a crucial task-strategy fit: persistent AI significantly increased mean originality only for semantically rich tasks, where deeper semantic exploration is needed. Temporal analyses further showed that, across both task types, both flexible and persistent AI elevated initial originality compared with the baseline, albeit with a slower subsequent increase. For semantically sparse tasks, these analyses provided tentative evidence of an originality benefit from flexible AI, but this pattern was not evident in overall mean originality. Cross-lagged models further showed an asymmetric influence in the persistent-AI condition: AI ideas predicted participants’ subsequent originality, but not vice versa. Mediation analysis suggested the persistent AI benefit was accounted for by stronger AI-to-human coupling. These findings suggest that AI’s creative benefits depend on aligning its assistance style with the cognitive demands of the task.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: AI-assisted AUT study; originality scoring method unstated, possibly LLM scoring validated against human raters.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Experiment on AI assistance generating cues for divergent thinking; the abstract describes no LLM scoring of responses compared with human raters.)

**Решение:** -

---

### 962 · R6835

**MERRY: Semantically Decoupled Evaluation of Multimodal Emotional and Role Consistencies of Role-Playing Agents**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2602.21941

Multimodal Role-Playing Agents (MRPAs) are attracting increasing attention due to their ability to deliver more immersive multimodal emotional interactions. However, existing studies still rely on pure textual benchmarks to evaluate the text responses of MRPAs, while delegating the assessment of their multimodal expressions solely to modality-synthesis metrics. This evaluation paradigm, on the one hand, entangles semantic assessment with modality generation, leading to ambiguous error attribution, and on the other hand remains constrained by the heavy reliance on human judgment. To this end, we propose MERRY, a semantically decoupled evaluation framework for assessing Multimodal Emotional and Role consistencies of Role-playing agents. This framework introduce five refined metrics for EC and three for RC. Notably, we transform the traditional subjective scoring approach into a novel bidirectional-evidence-finding task, significantly improving the human agreement of LLM-as-Judge evaluations. Based on MERRY, we conduct extensive evaluations. Our empirical results primarily reveal that: (1) Training on synthetic datasets tends to reduce emotional consistency, whereas training on real-world datasets improves it; (2) Existing models suffer from emotional templatization and simplification, exhibiting positive-bias and performance bottleneck in fine-grained negative emotions; (3) Simple prompting method strengthens the weak models but constrains the strong ones, while simple fine-tuning method suffers from poor role generalization. Codes and dataset are available. 11 pages, 6 figures

**ИИ:** ? · обе модели · неясен конструкт · LLM-as-judge rates emotional consistency of role-playing agent responses with reported human agreement; whether this counts as a psychological construct is borderline.

**Решение:** =

---

### 963 · R6851

**Agent-as-Peer-Debriefer: A Multi-Agent Framework with Perspective-Based Refinement for Qualitative Analysis**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.24600

Large language models (LLMs) are increasingly used for qualitative data analysis (QDA), yet their outputs often miss the depth and nuance of human analysis. We argue this gap reflects a missing credibility practice from human QDA: peer debriefing, in which an analyst seeks feedback from a disinterested peer and uses it to refine their coding. To bring this practice into LLM-assisted QDA, we propose Agent-as-Peer-Debriefer, a multi-agent QDA framework that builds peer debriefing into key coding steps. In our framework, a Hierarchical Coding Agent follows the standard QDA process to generate codes, sub-themes, and themes, along with self-explanations and reflection memos. It then shares these outputs with three Peer-Debriefing Agents, each applying a distinct analytical perspective (Theory-Driven, Data-Driven, or Applied) and refining the codes by keeping, renaming, reassigning, merging, or splitting them. These perspectives are drawn from established human QDA practices that generalize across domains and datasets. To evaluate the framework, we test it on three datasets across two domains with three LLMs, measuring semantic similarity to human-annotated codes. Across all settings, perspective-based, peer-debriefing refinement aligns more closely with human codes than a single-LLM baseline, and an ablation further shows the gain is not merely from additional refinement. The three perspectives also produce distinct trade-offs, showing that the choice of perspective is a meaningful and controllable design decision. More broadly, these findings suggest that simulating peer debriefing with explicit perspectives is a promising route to more credible LLM-assisted QDA. Accepted to EMNLP 2026 Main Conference

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM inductive QDA codes compared to human codes by semantic similarity; the domains are unclear, and it may be theme-level comparison only.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Multi-agent LLM framework generates codes and themes, evaluated by semantic similarity to human code sets. This is not unit-level coding agreement, and the psychological domain is unclear.)

**Решение:** -

---

### 964 · R6878

**Large-Language-Model-Agent-Enabled Analysis of Semi-Structured Interviews: Comparing Driver Experience Across Partial Automation Systems**

2026 · Proceedings of the Human Factors and Ergonomics Society Annual Meeting · journalarticle, article, journal-article · en · https://doi.org/10.1177/10711813261475249

SAE Level 2 (L2) partial automation changes the driving task, shifting the driver’s role from active operator to supervisor, raising questions about trust, satisfaction, perceived limitations, and system understanding. This study presents a locally hosted, auditable large language model (LLM) agent pipeline for analyzing 161 semi-structured post-study interviews from a 30-day naturalistic driving study of Tesla Autopilot, Cadillac Super Cruise, and Volvo Pilot Assist. The pipeline segmented transcripts into semantic units and coded each unit by question theme, answer theme, subtheme, and sentiment, enabling structured comparison across systems while preserving traceability to source evidence. Results showed significant vehicle-level differences in sentiment, with satisfaction-related responses strongly positive but performance-limitation narratives strongly negative. Validation against manually coded interview data showed high accuracy for answer subthemes and sentiment. Findings suggest that driver satisfaction with partial automation can coexist with uncertainty about system limits and automation boundaries.

**ИИ:** ? · обе модели · неясен конструкт · LLM coding of interview units was checked against manual coding, but driver trust, satisfaction and sentiment may count as product opinion rather than psychological constructs.

**Решение:** =

---

### 965 · R6879

**Detecting Emotional Dynamic Trajectories: An Evaluation Framework for Emotional Support in Language Models**

2026 · Proceedings of the AAAI Conference on Artificial Intelligence · journalarticle, conference, preprint/article · en · https://doi.org/10.1609/aaai.v40i3.37189

Emotional support is a core capability in human-AI interaction, with applications including psychological counseling, role play, and companionship. However, existing evaluations of large language models (LLMs) often rely on short, static dialogues and fail to capture the dynamic and long-term nature of emotional support. To overcome this limitation, we shift from snapshot-based evaluation to trajectory-based assessment, adopting a user-centered perspective that evaluates models based on their ability to improve and stabilize user emotional states over time. Our framework constructs a large-scale benchmark consisting of 328 emotional contexts and 1,152 disturbance events, simulating realistic emotional shifts under evolving dialogue scenarios. To encourage psychologically grounded responses, we constrain model outputs using validated emotion regulation strategies such as situation selection and cognitive reappraisal. User emotional trajectories are modeled as a first-order Markov process, and we apply causally-adjusted emotion estimation to obtain unbiased emotional state tracking. Based on this framework, we introduce three trajectory-level metrics: Baseline Emotional Level (BEL), Emotional Trajectory Volatility (ETV), and Emotional Centroid Position (ECP). These metrics collectively capture user emotional dynamics over time and support comprehensive evaluation of long-term emotional support performance of LLMs. Extensive evaluations across a diverse set of LLMs reveal significant disparities in emotional support capabilities and provide actionable insights for model development.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Benchmark rates emotional states in emotional-support dialogues; unclear whether LLM-based emotion estimation is checked against human ratings.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Benchmark of LLM emotional support with simulated users and trajectory metrics; no LLM coding compared against human labels is described.)

**Решение:** -

---

### 966 · R6880

**Can speech reveal mental health status? A study of linguistic features across multiple samples of at-risk adults.**

2026 · Journal of psychopathology and clinical science · journal article, journalarticle, research-article · eng · https://doi.org/10.1037/abn0001158

An urgent challenge in clinical science is the reliable detection of psychiatric risk in the aftermath of traumatic or stressful events. Current screening tools rely on patient symptom reports that are low in specificity and may confound normative reported distress with symptom escalation. The consequences of this lack of precision are significant, and there is a need for novel tools that will detect not only individuals at risk for psychiatric disorders but also those whose adaptation represents resilience and/or normative recovery pathways. In the current investigation, we applied natural language processing and large language models to transcripts of adult individuals ( N = 555) describing recent experiences via semistructured interviews to identify relevant features of language predictive of psychiatric risk. Participants were pooled from five different investigations and were all at elevated risk for psychopathology due highly stressful contexts and/or traumatic event exposure. We applied large language models to characterize the emotional content, overall sentiment, and autobiographical memory type of their interview responses to distinguish individuals with either persistent depressed mood or anhedonia (derived via separate diagnostic interviews). AI-detected features were consistent with prior in-lab emotion assessments. We then tested machine learning models to determine the extent to which each feature would be sensitive to the presence of disorder. The results suggest that emotional content and broad indices of sentiment offer a relatively high level of sensitivity when modeling diagnostic status, including the presence of major depressive disorder as well as any psychiatric disorder. Moreover, results also suggested certain content may be more relevant for risk detection (i.e., discussions of coping rather than a stressful event). Together, these findings advance the potential for applying AI-driven tools in psychiatric surveillance. (PsycInfo Database Record (c) 2026 APA, all rights reserved).

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLMs coded emotion and autobiographical memory type in interviews mainly to predict diagnosis; validation against human coding is possible but unclear.

**Решение:** =

---

### 967 · R6882

**Social Support Mechanisms in an Online Type 1 Diabetes Community: Social Network Analysis of Stakeholder Diversity and Disease Duration.**

2026 · Journal of medical Internet research · journal article, observational study, study · eng · https://doi.org/10.2196/82996

Abstract Background Online health communities (OHCs) have emerged as critical platforms for patients with type 1 diabetes (T1D) to exchange informational and emotional support. However, how stakeholder roles and disease duration jointly shape support dynamics and influence formation remains underexplored. Objective This study aimed to examine network-based social support mechanisms in a large T1D OHC, focusing on how stakeholder diversity and disease duration are associated with social support behaviors, subnetwork structures, and user influence. Methods This retrospective observational study analyzed digital trace data from China’s largest T1D online community (January 1-May 20, 2024), comprising 43,788 posts and 145,423 comments contributed by 1393 users. We manually annotated 2000 randomly sampled posts and fine-tuned a GPT-4o-mini (OpenAI) to classify support type (informational or emotional, and seeking or providing), yielding 20,384 support-related posts and 56,953 comments from 1224 users. We constructed weighted directed informational and emotional interaction networks and modeled predictors of a composite influence metric (Relative Centrality) using a gamma log-link generalized linear model (including demographics, identity, sentiment, disease duration, posting orientation, and cyclical activity time). Analyses were conducted in Python (version 3.11; Python Software Foundation). Statistical significance was set at P<.05. Results Support predominantly flowed from longer-duration members (≥ y) to those at earlier stages (≤5 y). Both subnetworks exhibited multicentered, star-like structures; the informational subnetwork had broader participation (density 0.031, diameter 7), while the emotional network was denser (density 0.039, diameter 6). In the influence model, peer supporters had substantially higher influence than patients (exp(β)=34.79, 95% CI 18.94‐64.08; P<.001), professionals lower (exp(β)=0.41, 95% CI 0.17‐0.99; P=.055), and women higher than men (exp(β)=1.65, 95% CI 1.23‐2.23; P=.001). Positive sentiment was associated with higher influence (exp(β)=1.91, 95% CI 1.22‐2.97; P=.005), and negative lower (exp(β)=0.54, 95% CI 0.37‐0.79; P=.001). Influence followed an inverted U-shaped trajectory over disease duration, peaking at approximately the 116th month (95% CI 43.25‐188.91). Conclusions This study suggests that social support patterns and user influence in a T1D OHC vary by stakeholder role and disease duration. Users with shorter disease duration more often sought support, whereas longer-duration users more often provided support, and informational and emotional exchanges formed distinct interaction subnetworks. Peer supporters were the most influential users; influence was also associated with gender, sentiment, activity timing, and a nonlinear (inverted U-shaped) relationship with disease duration. These findings may inform peer-facilitated, stage-tailored community strategies, with professionals engaged in targeted, complementary roles. A patient-centered collaborative care approach integrating peer experience with multidisciplinary clinical input could be explored in future work.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · Fine-tuned GPT-4o-mini classified social support type in posts against 2000 manually annotated posts; validation metrics likely reported.

**Решение:** =

---

### 968 · R6916

**Forensic Schema for Psychological Manipulation in Cyber Fraud: LLM-Driven Victim Reports Analysis**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.07751

Existing cybercrime classification schemas capture contact metadata and financial transactions but omit the psychological manipulation techniques perpetrators employ. We present a forensic schema (four categories, 35 questions) adding 11 manipulation indicators and cryptocurrency evidence fields to established forensic foundations. Applied to 10,994 victim reports via large language model (LLM)-driven annotation and validated against two human annotators (mean LLM-human $κ= 0.69$, matching inter-annotator $κ= 0.68$), the schema revealed a statistically distinct manipulation profile for each major fraud type (Cramer's $V$ up to $0.790$). A rationale-based evidence audit nonetheless exposed a forensic detail gap: detection of manipulation techniques was reliable, but victim narratives varied widely in the actionable detail supporting each Yes answer, and blockchain-specific identifiers were nearly absent. These findings point to AI-assisted victim intake with schema-informed follow-up questions as the most direct way to close the gap. The tiered annotation strategy also provides a reusable template for LLM-based extraction from other forensic text domains. Accepted by the 23rd International Conference on Privacy, Security and Trust (PST 2026)

**ИИ:** + · обе модели · кодирование по кодбуку · LLM coded psychological manipulation indicators in victim narratives; validated against two human annotators (κ=0.69 vs inter-annotator κ=0.68).

**Решение:** =

---

### 969 · R6919

**Learning to Prefer Reliably: Error-Augmented Emotion Preference Optimization with Calibrated Fusion**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.24730

Emotion preference learning uses pairwise comparisons between candidate descriptions to align multimodal large language models (MLLMs) with human judgments of open-ended emotion descriptions and to train reward models that capture human emotional preferences. However, conventional pairwise supervision is often sparse, typically providing only a single negative description for each positive description, and therefore offers limited coverage of the diverse ways in which an emotion description can be incorrect. In particular, models may be insufficiently exposed to semantically fluent but emotionally inconsistent descriptions. Beyond this data-level limitation, relying on a single MLLM judge introduces a distinct model-level concern: its judgments can be affected by model-specific biases when interpreting fine-grained or ambiguous multimodal emotional cues. To address these limitations, we propose Error-Augmented Preference Optimization (EAPO), a framework for improving the reliability of MLLM-based emotion preference judgment at both the data and model levels. First, we construct an error-augmented dataset by generating multiple controlled and emotion-aware negative descriptions from each preferred description. We then adapt multiple independent MLLM judges to this richer supervision and aggregate their preference margins using margin-calibrated soft fusion, which maps heterogeneous margins to a common scale before aggregation. Experiments on the MER2026-EmoPrefer Challenge dataset and our error-augmented dataset demonstrate that EAPO improves emotion preference prediction and enhances the robustness of MLLM judges when evaluating fluent descriptions that conflict with the video's multimodal emotional evidence. Our code is available at https://github.com/slash1028/EAPO-EmoPrefer. Accepted at ACM MM 2026 Workshop (MRAC '26)

**ИИ:** разошлись — Opus ? (неясен конструкт: MLLM judges predict human preferences between emotion descriptions of videos; multimodal preference task, so it's unclear whether it counts as coding psychological text.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Multimodal emotion preference optimization for MLLM judges on video emotion descriptions; a model-training method, not LLM coding of psychological or clinical text against human coders.)

**Решение:** -

---

### 970 · R6922

**“High-EQ” Discourse in Chinese Social Media: A Comparison of Human and Large Language Model Judgments**

2026 · Extended Abstracts of the CHI Conference on Human Factors in Computing Systems (CHI EA) · book, journalarticle, conference-paper · https://doi.org/10.1145/3772363.3799054

On Chinese social media, “high emotional intelligence” (高情商, High EQ) has emerged as a folk category for discussing socially skillful responses to awkward or face-threatening situations. These discussions form a naturalistic site for studying pragmatic judgment as a socially negotiated practice. This paper examines how understandings of High EQ are shared among human users and the extent to which large language models (LLMs) align with human evaluations. Using a corpus of 40 RedNote discussion posts and their associated responses, we compared human and LLM evaluations on High EQ responses along three dimensions: perceived High EQ, aggressiveness, and expected popularity. Combining quantitative agreement analysis with qualitative analysis informed by speech-act and politeness theory, we found that humans exhibit strong consensus on what counts as High EQ and aggressiveness, but little agreement on popularity. LLM judgments diverge systematically from human judgments, particularly for High EQ responses that rely on indirect off-record facework.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: LLM and human ratings of the same social-media responses on perceived emotional intelligence and aggressiveness (interpersonal constructs), with agreement analysis.); Sonnet ? (неясен конструкт: LLM and humans rate the same social media responses for High EQ and aggressiveness with agreement analysis. It's unclear whether this pragmatic and social judgment counts as a psychological construct.)

**Решение:** +

---

### 971 · R6941

**Detecting HIV-Related Stigma in Clinical Narratives Using Large Language Models**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.07717

Human immunodeficiency virus (HIV)-related stigma is a critical psychosocial determinant of health for people living with HIV (PLWH), influencing mental health, engagement in care, and treatment outcomes. Although stigma-related experiences are documented in clinical narratives, there is a lack of off-the-shelf tools to extract and categorize them. This study aims to develop a large language model (LLM)-based tool for identifying HIV stigma from clinical notes. We identified clinical notes from PLWH receiving care at the University of Florida (UF) Health between 2012 and 2022. Candidate sentences were identified using expert-curated stigma-related keywords and iteratively expanded via clinical word embeddings. A total of 1,332 sentences were manually annotated across four stigma subscales: Concern with Public Attitudes, Disclosure Concerns, Negative Self-Image, and Personalized Stigma. We compared GatorTron-large and BERT as encoder-based baselines, and GPT-OSS-20B, LLaMA-8B, and MedGemma-27B as generative LLMs, under zero-shot and few-shot prompting. GatorTron-large achieved the best overall performance (Micro F1 = 0.62). Few-shot prompting substantially improved generative model performance, with 5-shot GPT-OSS-20B and LLaMA-8B achieving Micro-F1 scores of 0.57 and 0.59, respectively. Performance varied by stigma subscale, with Negative Self-Image showing the highest predictability and Personalized Stigma remaining the most challenging. Zero-shot generative inference exhibited non-trivial failure rates (up to 32%). This study develops the first practical NLP tool for identifying HIV stigma in clinical notes.

**ИИ:** + · обе модели · бенчмарк с метками людей · Generative LLMs (LLaMA, GPT-OSS, MedGemma) classify psychosocial stigma subscales in clinical notes against manual human annotations; F1 reported.

**Решение:** =

---

### 972 · R6942

**Learning to GUIDE the Group: Self-Learning LLM Facilitation Across Multi-Party Tasks**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.16231

As large language models are increasingly adopted as multi-party communication facilitators, there is a growing demand for agents capable of balancing diverse group dynamics across contexts. However, existing LLM facilitators are often fine-tuned for task-specific objectives; generalized LLM-based facilitation methods that can adapt to different types of tasks and diverse group dynamics are underdeveloped. To address this gap, we present GUIDE (Generalized Unified Intervention for Dynamic Exchanges, a framework for developing generalized LLM-based facilitators across different multi-party contexts. GUIDE evaluates facilitation across both objective task outcomes and subjective metrics, including psychological safety and perceived friction. Within this framework, we study whether LLMs can self-learn generalized facilitation strategy offline to real-time interventions. We first collect multi-party human interactions guided by task-specific expert LLM facilitators (N=432 conversations). We then employ a self-learning method in which an LLM induces an actionable strategic playbook from conversations and iteratively refines it using feedback from an LLM judge aligned with human annotators (N=20), developing a single generalized facilitator that outperforms the three task-specific expert facilitators on held-out conversations 61.4% win rate. Finally, we evaluate these improvements empirically; in a real-time online empirical study, the self-learned generalized facilitator preserves facilitator performance and group productivity, improves speaking comfort and reduces interpersonal friction, while using 24.7% fewer turns and 29.0% fewer words than the expert prompts. These findings provide empirical evidence that LLMs can learn generalizable, task-agnostic social facilitation from task-specific human interactions, on-par with hand-crafted task-specific prompts across diverse group settings.

**ИИ:** ? · обе модели · неясен конструкт · An LLM judge rating facilitation in group conversations was aligned with human annotators; unclear whether it rated interpersonal constructs or only facilitation quality.

**Решение:** =

---

### 973 · R6965

**Automated detection of referential features in schizophrenic speech using large language models.**

2026 · Neuropsychologia · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.neuropsychologia.2026.109505

© 2026 The AuthorsCross-linguistic studies have demonstrated that individuals with schizophrenia—particularly those exhibiting formal thought disorder (FTD)—show distinctive distributions of noun phrases (NPs) in spontaneous speech. NPs (e.g., the picture; a husband) serve to organize the referential structure of meaning. Extracting such referential NP features, however, has traditionally required manual annotations. In this study we applied state-of-the-art large language models (LLMs) to extract these features automatically, using an existing, manually annotated dataset, in which English-speaking participants described a comic strip: 30 individuals with schizophrenia (SZ) (15 with moderate or severe FTD (SZ + FTD), 15 with minimal or no FTD (SZ−FTD), 15 neurotypical controls (NC). We first show that LLM-based analyses replicate the findings based on manual annotation, particularly highlighting that definite NPs tied to prior discourse, markers of grammatical and cognitive complexity and narrative coherence, were underused in the SZ + FTD group. Secondly, we demonstrate that LLMs, especially when used with in-context (few-shot) learning, offer a promising avenue for the automatic extraction of referential features. These results show that a cross-linguistically validated and clinically important linguistic pattern of deviance is accessible to automatized assessment with NLP.

**ИИ:** ? · обе модели · неясен конструкт · LLMs annotate noun-phrase referential features in schizophrenia speech against manual annotation; the coded construct is linguistic, though it is a marker of thought disorder.

**Решение:** =

---

### 974 · R6966

**Augmenting FEEL-based sentiment analysis for French healthcare workforce free-text: acronym expansion, negation handling, NMF topic modeling, and inter-rater validation — a methodological framework with proof-of-concept in emergency medicine (Preprint)**

2026 · JMIR Publications Inc. · preprint · https://doi.org/10.2196/preprints.106100

BACKGROUND Lexicon-based sentiment analysis of healthcare workforce free-text in French is typically performed by directly applying the FEEL (French Expanded Emotion Lexicon) to a tokenized corpus, with topic structure recovered through Latent Dirichlet Allocation (LDA). OBJECTIVE On small to medium corpora drawn from clinical settings, this standard pipeline has four known limitations: (i) profession-specific medical acronyms are treated as out-of-lexicon tokens, (ii) French negation operators are ignored, (iii) LDA topic structure is unstable on small text collections, and (iv) inter-rater reliability is rarely quantified. METHODS We developed an augmented FEEL-based pipeline that addresses these four limitations through: (1) a 26-entry French emergency medicine acronym expansion dictionary applied prior to lexicon matching, (2) a deterministic French negation handler that flips polarity assignments for tokens within four positions downstream of a negation marker, (3) Non-negative Matrix Factorization (NMF) with TF-IDF input, coherence-based selection of the topic count, and bootstrap stability assessment substituting for LDA, and (4) a dual-reference Cohen's kappa protocol on a stratified 50-response sample, in which one expert human rater and one large language model rater (Claude Opus 4) independently label the same responses, the human rater providing the substantive validation reference and the LLM rater serving as a transparent second annotator following recent methodological work on LLM-augmented text classification benchmarks. We benchmarked the augmented pipeline against a baseline R tidytext topicmodels pipeline on the PERCEPT'urg national survey corpus (n = 141 French emergency medicine professionals, 13 free-text items). RESULTS Acronym expansion added 252 token occurrences to the FEEL-matched set (16 distinct acronyms; SMUR n = 74, SAMU n = 46, IDE n = 34), raising token-level coverage from 39.5% to 40.7% (+1.2 pp). Negation handling triggered 697 polarity reassignments and shifted three items into negative AFINN-style intensity territory that the baseline pipeline classified as net-positive (definition of a non-urgent situation: +0.67 to -0.52; definition of an unscheduled situation: +0.28 to -0.41; ideal medicine in terms of patients: +0.14 \to -0.60). Coherence-based topic-count selection identified k = 3 for NMF (mean C_V = 0.72, versus k = 5 and C_V = 0.54 for the original LDA configuration). NMF was substantially more stable than LDA across re-fits (mean pairwise top-10 Jaccard 0.81 versus 0.48); with deterministic non-negative SVD initialization, within-init NMF stability reached Jaccard= 1.00. The augmented pipeline confirmed and sharpened the substantive finding of a preserved-ideal / dissonant-operational-reality configuration in the PERCEPT'urg corpus, with four rather than one item in negative territory. Dual-reference validation on the stratified 50-response sample yielded human-vs-LLM Cohen's kappa = 0.804 (95% CI [0.639, 0.934]; substantial agreement, 88% raw), establishing that the labeling task is well-defined; lexicon-vs-human kappa = 0.312 ([0.130, 0.493]) and lexicon-vs-LLM kappa = 0.353 ([0.155, 0.559]) were both fair, with the near-equality of the two values indicating that the FEEL pipeline diverges from both references in the same way --- a quantified over-assignment of the positive category driven by bounded lexicon coverage of operationally-negative vocabulary. CONCLUSIONS Four targeted augmentations to the standard FEEL pipeline---acronym expansion, negation handling, NMF substitution for LDA, and quantitative inter-rater validation---produce a methodologically defensible workflow for French healthcare workforce free-text without external dependencies beyond FEEL and standard R/Python packages. The framework is transferable to other French clinical corpora and, by replacing the acronym dictionary, to other professional French sub-languages. </sec

**ИИ:** ? · обе модели · неясен конструкт · Claude Opus 4 and a human expert labelled the sentiment of 50 survey responses (kappa 0.804); unclear whether generic sentiment counts as a psychological construct.

**Решение:** =

---

### 975 · R6972

**AI-Powered Decision Support System for Forest Fire Rescue Using Twitter and GPT-Based Analysis**

2026 · Afet ve Risk Dergisi · journalarticle, article · tr · https://doi.org/10.35341/afet.1821297

This study presents the Forest Fire Rescue Decision Support System (FFR-DSS), an AI-powered framework integrating GPT-4-based semantic analysis with real-time Twitter data to support emergency rescue coordination during forest fires in Turkey. Using tweets from the catastrophic 2021 wildfires affecting Muğla and Antalya, FFR-DSS employs prompt-engineered large language model (LLM) pipelines to extract urgency scores, emotional tone, geographical information, and actionability indicators from crisis-related social media content. Unlike traditional natural language processing (NLP) approaches such as Bag-of-Words (BoW) and TF-IDF, which may struggle with contextually rich and emotionally variable messages, the proposed framework leverages GPT-4's zero-shot semantic reasoning capabilities without requiring task-specific labeled training datasets. A geospatial risk mapping component further aggregates tweet-level outputs into district-level risk scores and dynamic heatmaps, enabling emergency teams to identify critical areas and prioritize resource allocation. Evaluation against a manually annotated sample demonstrates that FFR-DSS achieves 92.4% classification precision and 89.1% recall, substantially outperforming the BoW+SVM baseline with 72.8% accuracy. These results demonstrate the potential of LLM-augmented social media analytics to transform unstructured crisis communications into actionable intelligence, improving situational awareness, rescue coordination, and data-driven decision-making during large-scale natural disasters.In addition to its natural language understanding capabilities, FFR-DSS incorporates a geospatial mapping component to visualize and monitor critical rescue zones dynamically. By aligning semantic outputs with location data, the system helps authorities prioritize interventions in areas of greatest need. Empirical evaluations show that FFR-DSS achieves higher classification accuracy and interpretability than prior baseline methods, offering a more robust, transparent, and context-aware framework for emergency response. The results suggest that GPT-based systems represent a transformative step in disaster management technology, particularly in scenarios requiring rapid analysis and decision-making based on unstructured social media content.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-4 pulls urgency and emotional tone from wildfire tweets and is checked against manual annotation; unclear if the emotion coding itself was validated.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: GPT-4 analyzes disaster tweets for urgency and location for forest fire rescue; this is crisis management, not a psychological construct in a clinical or psychological sense.)

**Решение:** -

---

### 976 · R6985

**Moral Foundations in Children’s Media Content: A Comparison of Secular and Religious Media Sources**

2026 · Sociological Journal · journalarticle, article · ru · https://doi.org/10.19181/socjour.2026.32.2.3

Children’s media content is a crucial agent of moral socialization, but differences in the ethical narratives of secular and religious products remain understudied. Of particular interest are media products from “strict churches” (according to L. Yannacone), which demand a high degree of exclusivity and obedience, suggesting a unique moral profile. The aim of the study is to quantify the differences in ethical rhetoric between secular, mainstream Christian and “strict” religious (LDS) children’s content. A corpus of 13,205 lines was formed based on transcripts of the animated series Craig of the Creek (secular), Superbook (mainstream Christianity), and educational materials from the Church of Jesus Christ of Latter-day Saints (LDS). J. Haidt’s moral foundation theory (MFT) was used for analysis. The reliability of manual coding was verified using LLM (Large Language Model) Claude Sonnet 4.5, with a Cohen’s kappa of 0,676. A significant “ethical divide” between content types was identified. While the ethics of Care/Harm are universal (~30% of responses in all groups), the frequency of appeals to “binding” foundations varies dramatically. The LDS corpus demonstrates extremely high scores for the categories of Authority (41,7%) and Holiness (23,9%), which are virtually absent in the secular narrative. A gradient of religious strictness was established: Craig → Superbook → LDS, correlating with a shift from values of autonomy to the imperative of obedience. The results confirm the hypothesis on the heterogeneity of the religious media segment. The media production of “strict churches” functions as an instrument of doctrinal encapsulation, forming closed social capital through strict codes of hierarchy and purity, in contrast to more adaptive mainstream content.

**ИИ:** ? · обе модели · неясен конструкт · Claude Sonnet 4.5 checked against manual moral-foundations coding of media transcripts (κ=0.676); unclear if moral rhetoric counts as a psychological construct.

**Решение:** =

---

### 977 · R7020

**How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities for LLM-Based Qualitative Coding**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.11109

The utility of AI in multi-coder qualitative coding has been widely discussed, yet little empirical evidence exists to delineate the contexts in which it performs reliably. We address this gap by quantifying the effectiveness of multi-agent LLM coding across varied qualitative datasets, revealing key contextual and structural factors that mediate coding outcomes. We developed a literature-informed baseline pipeline that enables AI agents to independently code, debate, and reconcile disagreements. Results revealed that coding accuracy depends on factors such as codebook length, qualitative data similarity, and agent disagreement. Notably, intense and unresolved debates between agents led to higher accuracy. Our analysis showed that while LLMs emulate many human discussion behaviors, they lack adaptive responsiveness to context. From these findings, we offer design recommendations for building automated coding systems. Our open-source AI discussion dataset and methodological framework lay the groundwork for advancing the design of AI-mediated automated thematic analysis. 34 pages, 7 tables

**ИИ:** ? · обе модели · неясен конструкт · Multi-agent LLM codebook coding with accuracy presumably measured against human codes; unclear whether the datasets involve psychological constructs.

**Решение:** =

---

### 978 · R7028

**Large Language Models for Psychiatric Interview Analysis: AnExploratory Pilot Study**

2025 · IS 2025 COGNITIVE SCIENCE · conference-paper · https://doi.org/10.70314/is.2025.cogni.12

This exploratory pilot study investigates the use of large language models (LLMs) for automated analysis of psychiatric interviews.Using transcripts from the Structured Interview of Personality Organization (STIPO-R), we tested GPT-4o across three paradigms: direct application of clinical scoring guidelines, emulation of a validated psychometric scale, and exploratory construct elicitation.LLM-derived scores strongly correlated with clinician ratings and captured clinically relevant constructs.Findings highlight opportunities for scalable, theory-driven assessment of patient language, but also underscore challenges including interpretability, reproducibility and data privacy.

**ИИ:** + · обе модели · подсчёт методики · GPT-4o applied STIPO-R scoring guidelines to the psychiatric interview transcripts, and its scores correlated with clinician ratings.

**Решение:** =

---

### 979 · R7042

**Using Large Language Models to Analyze Symptom Discussions and Recommendations in Clinical Encounters**

2025 · Journal of Palliative Medicine · journalarticle · https://doi.org/10.1177/10966218251363802

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM coding of symptom discussions in palliative encounter transcripts may include psychological symptoms and human comparison.

**Решение:** =

---

### 980 · R7045

**Comparative Analysis of the Efficacy in the Classification of Cognitive Distortions Using LLMs**

2025 · International Conference on Agents and Artificial Intelligence · journalarticle, conference-paper · en · https://doi.org/10.5220/0013399200003890

: This paper explores the application of Large Language Models (LLMs) for the classification of cognitive distortions in humans. This is important for detecting irrational thought patterns that may negatively influence people’s emotional state. To achieve this, we evaluated a range of open-source LLMs with varying sizes and architectures to assess their effectiveness in the task. The results show promising results of the recognition capabilities of these models, particularly given that none of them were specifically fine-tuned for this task and were solely guided by a structured prompt. The results allow us to see a trend where larger models generally outperform their smaller counterparts in this task. However, architecture and training strategies are also important factors, as some smaller models achieve performance levels comparable to or exceeding larger ones. This study has also allowed us to see the limitations in this field: the subjectivity factor that may exist in the annotations of cognitive distortions due to overlapping categories. This ambiguity impacts both human agreement and model performance. Therefore, future work includes fine-tuning LLMs specifically for this task and improving the quality of the dataset to improve performance and address ambiguity.

**ИИ:** + · обе модели · бенчмарк с метками людей · Open-source LLMs prompted to classify cognitive distortions in text, evaluated against human annotations of the dataset; annotation ambiguity is discussed.

**Решение:** =

---

### 981 · R7054

**AffectLLM: A Large Language Model for Rating the Affective Quality of Representations**

2025 · IEEE International Conference on Human-Machine Systems (ICHMS) · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/ichms65439.2025.11154254

Affective computing presents significant challenges, particularly in the context of human-machine interactions. Traditional approaches often involve developing data-driven models that rely on physiological and image-based data to infer the emotional states of individuals during interactions with machines. However, these models frequently lack contextual relevance and perform poorly in complex scenarios involving conflicting cues. Additionally, they suffer from weak generalization due to the absence of structured methodologies that disentangle interconnected external factors. To address these limitations, we propose leveraging the Affective Quality of Representations (AFF) score, a standardized metric for assessing human affective responses across varied contexts. The AFF score is derived from expert ratings of participant narratives elicited by questions or visual cards, following established SCORS-G guidelines. The primary challenge of this approach is its reliance on trained psychology experts for scoring. To mitigate this, we developed the AffectLLM, a large language model designed to predict AFF scores efficiently and support the analysis of human-machine interactions. A strong contribution of AffectLLM is providing a structured metric that can guide the design of humanmachine interaction environments that promote more positive affect quality outcomes.

**ИИ:** + · обе модели · подсчёт методики · LLM predicts SCORS-G Affective Quality scores of narratives, against expert ratings as the reference.

**Решение:** =

---

### 982 · R7058

**Leveraging Large Language Models to Estimate Clinically Relevant Psychological Constructs in Psychotherapy Transcripts.**

2025 · Computational psychiatry (Cambridge, Mass.) · journal article, journalarticle, article · eng · https://doi.org/10.5334/cpsy.141

Developing precise, innocuous markers of psychopathology and the processes that foster effective treatment would greatly advance the field's ability to detect and intervene on psychopathology. However, a central challenge in this area is that both assessment and treatment are conducted primarily in natural language, a medium that makes quantitative measurement difficult. Although recent advances have been made, much existing research in this area has been limited by reliance on previous-generation psycholinguistic tools. Here we build on previous work that identified a linguistic measure of ``psychological distancing" (that is, viewing a negative situation as separated from oneself) in client language, which was associated with improved emotion regulation in laboratory settings and treatment progress in real-world therapeutic transcripts (Nook et al., 2017, 2022). However, this formulation was based on context-insensitive word count-based measures of distancing (pronoun person and verb tense), which limits the ability to detect more abstract expressions of psychological distance, such as counterfactual or conditional statements. This approach also leaves open many questions about how therapists' --- likely subtler --- language can effectively guide clients toward increased psychological distance. We address these gaps by introducing the use of appropriately prompted large language models (LLMs) to measure linguistic distance, and we compare these results to those obtained using traditional word-counting techniques. Our results show that LLMs offer a more nuanced and context-sensitive approach to assessing language, significantly enhancing our ability to model the relations between linguistic distance and symptoms. Moreover, this approach enables us to expand the scope of analysis beyond client language to shed insight into how therapists' language relates to client outcomes. Specifically, the LLM was able to detect ways in which a therapist's language encouraged a client to adopt distanced perspectives---rather than simply detecting the therapist themselves being distanced. This measure also reliably tracked the severity of patient symptoms, highlighting the potential of LLM-powered linguistic analysis to deepen our understanding of therapeutic processes.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM rates psychological distancing in therapy transcripts against word counts and symptoms; any human-coding validation is unclear.

**Решение:** =

---

### 983 · R7065

**Exploring the Impact of Innovation Competitions on Student Self-Awareness and Growth Through AI and Human Analysis**

2025 · Proceedings of the ... Annual Hawaii International Conference on System Sciences/Proceedings of the Annual Hawaii International Conference on System Sciences · conference-paper · en · https://doi.org/10.24251/hicss.2025.609

Student Innovation Competitions and Programs (ICPs), including design challenges, hackathons, startup competitions, and boot camps, play a critical role in entrepreneurship and innovation education. These programs foster students' technical skills, networking opportunities, and innovation mindsets. However, the literature lacks an exploration of ICPs' transformative impact on students' entrepreneurial mindsets, which involves profound changes in students' values and abilities. This study addresses this gap by applying the Transformative Learning Theory (TLT) to examine how ICPs can be transformative experiences for students. Using a qualitative inductive approach, semi-structured interviews with 36 students who participated in ICPs were conducted. Thematic analysis was performed using both human coders and ChatGPT 4.0 to identify the strengths and weaknesses realized by students during ICPs. The results showed a high level of agreement between human and AI-generated codes, highlighting ICPs' role in enhancing self-awareness and personal growth. Key strengths discovered included communication skills, leadership, problem-solving, organizational skills, tenacity, and interpersonal skills, while common weaknesses were noted as time management, communication challenges, lack of self-advocacy, trust issues, inflexibility, conflict management, and stress and anxiety. These findings suggest that ICPs are instrumental in fostering an entrepreneurial and innovation mindset, but organizers should address time management and stress issues to maximize benefits to students.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · ChatGPT-4 and humans coded student interviews for self-perceived strengths and weaknesses and reported agreement; unclear whether coding was unit-level or theme-level.

**Решение:** =

---

### 984 · R7086

**Evidence-Driven Marker Extraction for Social Media Suicide Risk Detection**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2502.18823

Early detection of suicide risk from social media text is crucial for timely intervention. While Large Language Models (LLMs) offer promising capabilities in this domain, challenges remain in terms of interpretability and computational efficiency. This paper introduces Evidence-Driven LLM (ED-LLM), a novel approach for clinical marker extraction and suicide risk classification. ED-LLM employs a multi-task learning framework, jointly training a Mistral-7B based model to identify clinical marker spans and classify suicide risk levels. This evidence-driven strategy enhances interpretability by explicitly highlighting textual evidence supporting risk assessments. Evaluated on the CLPsych datasets, ED-LLM demonstrates competitive performance in risk classification and superior capability in clinical marker span identification compared to baselines including fine-tuned LLMs, traditional machine learning, and prompt-based methods. The results highlight the effectiveness of multi-task learning for interpretable and efficient LLM-based suicide risk assessment, paving the way for clinically relevant applications.

**ИИ:** + · обе модели · бенчмарк с метками людей · Mistral-7B classifies suicide risk and extracts evidence spans from Reddit posts; evaluated against expert-annotated CLPsych labels.

**Решение:** =

---

### 985 · R7127

**MAGneT: Coordinated Multi-Agent Generation of Synthetic Multi-Turn Mental Health Counseling Sessions**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2509.04183

The growing demand for scalable psychological counseling highlights the need for high-quality, privacy-compliant data, yet such data remains scarce. Here we introduce MAGneT, a novel multi-agent framework for synthetic psychological counseling session generation that decomposes counselor response generation into coordinated sub-tasks handled by specialized LLM agents, each modeling a key psychological technique. Unlike prior single-agent approaches, MAGneT better captures the structure and nuance of real counseling. We further propose a unified evaluation framework that consolidates diverse automatic metrics and expands expert assessment from four to nine counseling aspects, thus addressing inconsistencies in prior evaluation protocols. Empirically, MAGneT substantially outperforms existing methods: experts prefer MAGneT-generated sessions in 77.2% of cases on average across the nine aspects over the strongest baseline, and sessions generated by MAGneT using Llama3-8B-Instruct backbone yield 3.2% higher general counseling skills and 4.3% higher CBT-specific skills on cognitive therapy rating scale (CTRS). An open source Llama3-8B-Instruct model fine-tuned on MAGneT-generated data also outperforms models fine-tuned using baseline synthetic datasets by 6.9% on average on CTRS. We make our code, data and fine-tuned model public. 50 pages, 39 figures, 20 Tables

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly a generation study; CTRS skill ratings are probably LLM-judged alongside expert ratings, but LLM–expert agreement on the same sessions is unclear.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Synthetic counseling session generation; experts compare outputs and CTRS scoring is used for evaluation, with no LLM-vs-human coding agreement.)

**Решение:** -

---

### 986 · R7137

**DynaMentA: Dynamic Prompt Engineering and Weighted Transformer Architecture for Mental Health Classification Using Social Media Data**

2025 · IEEE Transactions on Computational Social Systems · journalarticle, article · en · https://doi.org/10.1109/tcss.2025.3569400

Mental health classification is inherently challenging, requiring models to capture complex emotional and linguistic patterns. Although large language models (LLMs) such as ChatGPT, Mental-Alpaca, and MentaLLaMA show promise, they are not trained on clinically grounded data and often overlook subtle psychological cues. Their predictions tend to overemphasize emotional intensity, while failing to capture contextually relevant indicators that are critical for accurate mental health assessment. This article introduces dynamic prompt engineering and weighted transformer architecture dynamic prompt engineering and weighted transformer architecture for mental health classification (DynaMentA), a novel dual-layer transformer framework that integrates the strengths of BioGPT and decoding-enhanced BERT with disentangled attention (DeBERTa) to address these challenges. BioGPT captures fine-grained biomedical indicators, while DeBERTa provides context-aware disambiguation. The ensemble mechanism dynamically weights their outputs, guided by a simulated feedback loop that refines the predictions during training. Unlike previous studies that treat classification statically, DynaMentA incorporates dynamic prompt engineering to better align with evolving linguistic and emotional signals. Evaluated on three benchmark datasets, DepSeverity, suicide versus depression classification natural language (SDCNL), and Dreaddit, DynaMentA achieves precision of 92.6%, 91.9% F1-score, and 0.94 AUC-ROC, consistently outperforming the existing benchmark, including general-purpose LLMs and domain-specific mental health models. This scalable and interpretable framework establishes a state-of-the-art methodology for computational mental health analysis in high-stakes applications, such as suicide risk assessment and crisis intervention and early detection of severe depressive episodes.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · BioGPT+DeBERTa ensemble and LLM baselines classify mental health posts; Dreaddit/DepSeverity likely human-annotated, but the abstract doesn't say where labels come from.

**Решение:** =

---

### 987 · R7141

**Overview of ToxHabits at BioCreative IX: corpus, guidelines and evaluation of systems for the detection of Toxic Habits from text**

2025 · Zenodo · conferenceproceeding/ · https://doi.org/10.5281/zenodo.16918801

Abstract Systems able to detect mentions of substance use and abuse from clinical texts are essential for healthcare analytics, substance use surveillance, and AI-based decision support. Compared to other clinical concepts, substance use and behavioral information are often only captured in free-text narratives and are rarely structured in electronic health records. Despite their relevance for clinical research and public health, few annotated corpora exist for substance use detection, and prior efforts have been limited by narrow domain coverage, English-only datasets, or lack of event-based annotations. To address these limitations, we proposed the ToxHabits shared task. The task is based on a Spanish corpus of 1,499 clinical case reports covering multiple medical specialties, with event-based annotations for substance use and associated attributes. The task is divided into two subtasks: ToxNER, focused on identifying substance use mentions (triggers), and ToxUse, aimed at extracting related information that characterizes the substance use (arguments), such as type, frequency, and route. A total of 6 teams participated, each allowed to submit up to 5 runs per subtask. The top-scoring systems achieved an F1-score of 0.94 for ToxNER and 0.91 for ToxUse. Considering the complexity of real-world narratives, nested entities, and fine-grained event structures, these results demonstrate the viability of accurate substance use detection from clinical text and offer a strong benchmark for future work in Spanish-language biomedical NLP. The ToxHabits Gold Standard is freely available at: https://zenodo.org/records/15425460. This article is part of the Proceedings of the BioCreative IX Challenge and Workshop (BC9): Large Language Models for Clinical and Biomedical NLP at the International Joint Conference on Artificial Intelligence (IJCAI).

**ИИ:** ? · обе модели · другое · Shared task scoring systems against human gold annotations of substance use in clinical texts; unclear whether participating systems used LLMs; NER-style extraction.

**Решение:** =

---

### 988 · R7151

**Collecting Qualitative Data at Scale with Large Language Models: A Case Study**

2025 · Proceedings of the ACM on Human-Computer Interaction · journalarticle, other/journal article, article · en · https://doi.org/10.1145/3710947

Chatbots have shown promise as tools to scale qualitative data collection. Recent advances in Large Language Models (LLMs) could accelerate this process by allowing researchers to easily deploy sophisticated interviewing chatbots. We test this assumption by conducting a large-scale user study (n=399) evaluating 3 different chatbots, two of which are LLM-based and a baseline which employs hard-coded questions. We evaluate the results with respect to participant engagement and experience, established metrics of chatbot quality grounded in theories of effective communication, and a novel scale evaluating richness or the extent to which responses capture the complexity and specificity of the social context under study. We find that, while the chatbots were able to elicit high-quality responses based on established evaluation metrics, the responses rarely capture participants\u27 specific motives or personalized examples, and thus perform poorly with respect to richness. We further find low inter-rater reliability between LLMs and humans in the assessment of both quality and richness metrics. Our study offers a cautionary tale for scaling and evaluating qualitative research with LLMs.27 pages, 6 figure

**ИИ:** ? · обе модели · неясен конструкт · LLM and human ratings of interview response quality and richness are compared, but it is unclear whether these count as psychological constructs.

**Решение:** =

---

### 989 · R7155

**Clinical Free Text Summaries and LLMs: A Case Study on LLM-supported Identification of Intellectual Disabilities in Clinical Free Text Summaries (Preprint)**

2025 · preprint · en · https://doi.org/10.2196/preprints.72256

BACKGROUND Free-text clinical data that is unstructured and narrative in nature can provide a rich source of patient information. However, the information contained within routinely collected health data is typically captured as free-text, and extracting research quality clinical phenotypes from these data remains a challenge. Manually reviewing and extracting clinical phenotypes from free-text patient notes is a time-consuming process and not suitable for large scale datasets. On the other hand, automatically extracting clinical phenotypes can be a challenging task due to medical researchers lacking gold-standard annotated references and other purpose-built resources including software. Recent large language models (LLMs) have the ability to understand natural language instructions (prompts) which helps them adapt to different domains and tasks without the need for specific training data. This makes them suitable for clinical applications, though their use in this field is still limited. OBJECTIVE In this paper, we analyse how large language models (LLMs) and in-context-learning techniques can be utilised for text classification in a real-world medical research scenario, where only a few training examples are available. For this, we sought to develop a pipeline, based on the “few-shot” learning framework, for extracting information from free-text clinical summaries derived from discharge patient notes and clinical interviews in a cohort of 1121 individuals with severe mental illnesses. Our main aim was to identify those with confirmed or strongly suspected comorbid intellectual disability (ID). A secondary aim was to take advantage of complementary and independent information from this cohort, in the form of a high-quality genomic dataset. For this we designed a proof-of-concept study to assess whether the individuals identified by our LLM-based models as having ID were also carriers of genetic variants known to confer risk of ID in the general population. METHODS We explore novel approaches for performing classification in free-text patient summaries, based on using an intermediate Information Extraction step and human-in-the-loop approach in order to maximise the performance of in-context-learning techniques and LLMs. We perform our experiments with two models, Flan-T5 and LLaMA, and a real-world research dataset with free text clinical information from individuals diagnosed with severe mental illness. For our genetics-based proof-of-concept experiment, we use a published dataset where de novo mutations have been called. On this, we perform rare variant association analyses through Firth’s penalised likelihood approach, a logistic regression framework appropriate for sparse data. RESULTS Results show that a two-stage approach consisting of information extraction and manual validation can be effective for identifying individuals with suspected intellectual disabilities within free-text patient information, only needing a single training example per classification label. This approach was further validated by demonstrating that individuals classified by LLMs to have suspected intellectual disabilities were significantly enriched for rare genetic variants in genes associated with intellectual disability. CONCLUSIONS Recently developed LLMs and in-context learning techniques combined with human-in-the-loop approaches, can be highly beneficial for extraction and categorisation of information from free-text clinical data when there is lack of training data. In this proof-of-concept study, we show that LLMs can be used to identify individuals with a severe mental illness who also have suspected intellectual disability, which is a biologically and clinically meaningful subgroup of patients. This showcases one of the applications of our method and suggests broad uses for supporting research on clinical records.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLaMA/Flan-T5 classify intellectual disability from clinical summaries of patients with severe mental illness; unclear whether results are evaluated against human-coded labels.

**Решение:** =

---

### 990 · R7156

**Modelling Inter-Individual Differences in Multimodal Data: A Metric Learning Approach for Personalized Well-being Estimation in Healthcare Workers**

2025 · TU Wien · text/diploma thesis · https://doi.org/10.34726/hss.2025.133180

In stark belasteten Arbeitsumgebungen wie Krankenhäusern und Pflegeeinrichtungen ist das Wohlbefinden von Pflegekräften durch die physischen, emotionalen und zeitlichen Anforderungen ihrer Arbeit ständig beeinträchtigt. Diese Belastungen führen schleichend zu einer Beeinträchtigung des Wohlbefindens, wobei frühe Symptome oft subtil sind und häufig erst lange nach ihrem Auftreten bemerkt werden, was ein proaktives Eingreifen erschwert.Diese Arbeit basiert auf einer Praxisstudie der TU Wien in Zusammenarbeit mit einem Krankenhaus in Hietzing, Wien, an der Pflegekräfte über mehrere Monate teilnahmen.Ziel der Studie war die Modellierung und Vorhersage des täglichen Wohlbefindens mit-hilfe multimodaler Daten, bestehend aus Daten mobiler Sensoren, halbstrukturierten Interviews, psychologischen Merkmalen aus Fragebögen und Schlafverhalten.Im ersten Teil wird untersucht, ob große Sprachmodelle die qualitative Kodierung halbstrukturierter Interviews auf dem gleichen Niveau wie ein Mensch durchführen können.Die generierten Codes zeigen eine hohe thematische Übereinstimmung mit den Annotationen von Experten, was darauf hindeutet, dass die LLM-gestützte Kodierung eine zuverlässige und skalierbare Alternative darstellen kann.Im zweiten Teil wird ein Modell entwickelt, das anhand der ambulanten physiologischen Signale der Teilnehmenden deren tägliches Wohlbefinden (gemessen mit den NASA-TLX-Selbstbeurteilungsbögen) vorhersagt. Die Einbeziehung von Merkmalen aus Interviews verbessert die Vorhersagegenauigkeit zusätzlich.Abschließend werden die Teilnehmenden anhand ihrer Persönlichkeitsmerkmale und Schlafmuster gruppiert, um zu untersuchen, ob sich die Vorhersagekraft der Modelle dadurch weiter steigern lässt. Obwohl dieser Ansatz theoretisch vielversprechend ist,schränkte die geringe Anzahl an Teilnehmenden pro Gruppe die Modellleistung ein,sodass die Ergebnisse nicht eindeutig sind.Trotz dieser Herausforderungen zeigen die Ergebnisse, dass eine aussagekräftige Modellierung des Wohlbefindens auch unter realen Feldbedingungen mit verrauschten Daten und begrenzten Ressourcen möglich ist. Diese Arbeit liefert einen Machbarkeitsnachweis für ein skalierbares, datengestütztes Wohlbefindensmonitoring im klinischen Alltag –nicht nur unter kontrollierten Forschungsbedingungen, sondern auch dort, wo es am dringendsten benötigt wird. In high-stress working environments such as hospitals and long-term care facilities, the well-being of healthcare workers is constantly challenged by the physical, emotional, and temporal demands of their work. These burdens gradually erode their well-being, and yet early symptoms are subtle and often self-reported long after they occur, making proactive intervention difficult.This thesis is based on a real-world study conducted by TU Wien in collaboration with a hospital in the Second Department of Psychiatry and Psychotherapy, Hietzing Clinic, Vienna, where healthcare workers participated in a multi-month field study. The study aimed to model and predict daily well-being using multimodal data which consists of ambulatory sensor data, semi-structured interviews, psychological traits derived from questionnaires, and sleep behavior.The first part evaluates whether large language models can perform qualitative coding of semi-structured interviews on the same level as a human would. The generated codes show high thematic alignment with expert human annotations, suggesting that LLM-assisted coding can serve as a reliable and scalable alternative.The second part develops a model to predict participants’ daily well-being scores measured by the NASA-TLX self assessments forms from their ambulatory physiological signals. Incorporating features derived from interviews further improves predictive performance.Finally, participants are clustered based on their personality traits and sleep patterns to investigate would it even further improve predictive ability of the models. While thisapproach is theoretically promising, the small number of participants per cluster limited model performance, rendering results inconclusive.In spite of these challenges, the findings demonstrate that meaningful well-being modeling is feasible in real-world field conditions where data are noisy and resources limited.This work provides a proof of concept for scalable data-driven well-being monitoring in everyday clinical practice, not only under controlled research conditions but in the settings where it is needed most.

**ИИ:** + · обе модели · кодирование по кодбуку · LLM qualitative coding of healthcare workers' well-being interviews compared with expert annotations; 'thematic alignment' may mean theme-level only, so check full text.

**Решение:** =

---

### 991 · R7171

**Identification of suicide positive expressions in electronic health records in German language (Preprint)**

2025 · preprint · https://doi.org/10.2196/preprints.87119

UNSTRUCTURED Suicide attempts are one of the most challenging psychiatric outcomes and have great importance in clinical practice. However, they remain difficult to detect in a standardised way to assist prevention because assessment is mostly qualitative and often subjective. As digital documentation is increasingly used in the medical field, Electronic Health Records (EHRs) have become a source of information that can be used for prevention purposes, containing codified data, structured data, and unstructured free text. This study aims to provide a quantitative approach to detection of suicide risk using EHRs, employing natural language processing techniques in combination with deep learning artificial intelligence methods to create an algorithm intended for use with clinical documentation in German. Using psychiatric medical files from inpatient psychiatric hospitalisations between 2013 and 2021, free text reports were transformed into structured embeddings using a German-trained adaptation of Word2Vec, followed by a Long-Short Term Memory (LSTM) – Convolutional Neural Network (CNN), BERT models (gbert-large and bert-base-german-cased), and GPT-2 approaches on sentences of interest to label suicide related content. The present study resulted in an average overall accuracy of >70% for all models, sensitivity, and F1 scores for the positive related sentences >60%. This study offers promising ways for automated early prediction of suicide attempts and therefore holds opportunities for mental health care.

**ИИ:** ? · обе модели · другое · Suicide-related EHR sentences, probably human-labelled; but the only generative model is GPT-2, which predates the review's GPT-3 cutoff. The rest are BERT/LSTM.

**Решение:** =

---

### 992 · R7181

**Leveraging social media data for detection and monitoring of depression**

2025 · Imperial College London · text/text, article · https://doi.org/10.25560/125096

Mental health disorders are increasingly prevalent, with depression being the most common and a major cause of disability and suicide worldwide. Understanding its symptoms, severity, and progression is vital for improving early detection and intervention. This thesis adopts a data-driven AI approach, constructing a large expert-annotated dataset and developing models for monitoring depression from social media language. We first design a data collection and curation framework to build a large-scale dataset of posts from individuals who self-report depression. In collaboration with psychiatrists and psychologists, we create an annotation scheme for labelling symptoms and severity over time. Experienced psychologists annotate the data, resulting in DepSy, the largest English dataset of 40,000 posts fully annotated for depression symptoms and severity progression. This dataset underpins all subsequent experiments. We then benchmark multiple NLP approaches to classify posts written before versus after a reported depression diagnosis. Analyses include linguistic patterns, emotion usage, and content variation. Among various models tested, BERT-based classifiers achieve the best overall performance, while large language models (LLMs) in zero-shot settings perform near random. Next, we address symptom detection as a multi-label classification problem. A bespoke BERT-based model achieves strong overall results, while a fine-tuned Llama-based model, DepSy-LLaMA, obtains higher recall, identifying more positive symptom cases—a valuable property in mental health detection. However, LLM predictions remain less reliable for sensitive applications. Finally, we explore depression severity prediction over time using deep learning and propose a hybrid CTMC-LSTM model that integrates Markov chains with LSTM to capture temporal patterns. This model uniquely detects severe cases and achieves the highest performance across all baselines. The findings demonstrate the importance of temporal modelling and expert-annotated data for building robust, ethical, and clinically informed systems for depression monitoring from social media.

**ИИ:** + · обе модели · бенчмарк с метками людей · Fine-tuned Llama and zero-shot LLMs detect depression symptoms in posts, evaluated against psychologists' annotations in the DepSy dataset.

**Решение:** =

---

### 993 · R7185

**Explicitation interviews on compassionate tacit knowledge— A pilot study contrasting AI & human processes**

2025 · F1000 Research Ltd · other, posted-content · en · https://doi.org/10.21955/mep.1115840.1

Background Compassionate tacit knowledge is essential for healthcare professionals to navigate complex clinical environments and deliver patient-centered care. Health professionals develop this practical, experiential knowledge through workplace reflection [1,2], while the lived experiences of patients and caregivers play a critical role in shaping healthcare professionals' compassionate care. Traditional methods to evaluate compassionate tacit knowledge are resource-intensive and require expert training, limiting scalability. Recent advancements in artificial intelligence (AI) provide opportunities to address these challenges through objective, scalable approaches. This pilot study explores the feasibility and validity of using an AI-powered virtual instructor to assess compassionate tacit knowledge in patients, caregivers, and healthcare professionals, leveraging the AI-enabled Objective Structured Clinical Examination (OSCE) Debrief platform. Summary of Work This two-phase study aimed to evaluate the potential of AI in capturing compassionate tacit knowledge. Phase 1 involved qualitative interpretative analysis of explication interviews with interprofessional participants (n=7, including patients, caregivers, physicians, and allied health professionals) to map patterns of compassionate tacit knowledge. In Phase 2, these insights informed the development of an AI algorithm, fine-tuned using a large language model (e.g., GPT 4.1 mini; GPT 4.1 nano). The algorithm evaluated Phase 1 data demonstrated high concordance [Intraclass Correlation Coefficients (ICCs) &gt; 0.85] with human evaluators for AI-enabled OSCE Debrief. Summary of Results The AI-enabled virtual instructor effectively simulated a human facilitator, providing non-directional, open-ended feedback to learners to foster reflective practice. This study demonstrated the feasibility of AI-enabled education in compassionate care. Discussion and Conclusion The adoption of the AI-enabled OSCE design offers a scalable and objective means of capturing compassionate tacit knowledge in diverse clinical contexts. By integrating cultural experiences and social norms, AI-enabled OSCE design advances healthcare education and practice. Future use of this AI-enabled OSCE by another cohort can capture patient/caregiver tacit knowledge for other clinical topics of interest. Take-home Message(s) Experiential learning fosters AI-human collaboration and shared mental models in knowledge co-creation. Human-AI collaboration transforms healthcare education, strengthening partnerships in complex healthcare ecosystems. The AI’s ability to identify tacit knowledge enhances healthcare service delivery with low-cost primary care education, and the quality of life of health providers and receivers through participatory AI integrated human-centered design approaches. Supplement: *This pilot study is within a larger scale project. Privacy Protection with Expert Guidance This AI tool development centres on privacy protection. Model selection (GPT 4.1mini and nano, Microsoft Azure) aligns with ethical guidelines. Data privacy can be protected using Azure to reduce open- source data sharing. GPT 4.1 has a privacy protection function that will not allow data sharing for future GPT model training. Future personal health information protection infrastructure will need to be built in place to support blurred faces or name removed function in video data collection and data analysis stages. AI (LLM) deployment was guided by a curriculum educator. Two engineering students met with an educator daily to ensure that the product development supports the population needs. A software expert joins 30-60 minute meetings once every two weeks for technical support.

**ИИ:** разошлись — Opus + (кодирование по кодбуку: Fine-tuned GPT-4.1 evaluated explicitation interview data on compassionate tacit knowledge; ICC > 0.85 with human evaluators.); Sonnet ? (неясен конструкт: Fine-tuned GPT-4.1 evaluated interview data on compassionate tacit knowledge with ICC >0.85 against human evaluators; the construct is compassion-related, but the coded text and scheme are unclear.)

**Решение:** +

---

### 994 · R7196

**Does Generative Artificial Intelligence Cause Negative Transfer? Experimental Evidence from Creativity Assessments with Middle-Schoolers in Brazil**

2025 · Stanford Digital Repository · text/thesis · https://doi.org/10.25740/dv853vd5728

Children increasingly use Generative Artificial Intelligence (AI) for solving homework problems, satisfying their curiosities, and in the creative process at large. Much of this use happens with Large Language Models (LLMs) such as OpenAI’s ChatGPT. While literature has already explored how the use of LLMs impacts adults’ creative divergent thinking in one context, very little has analyzed how AI impacts the transfer of learning from one context to another. In the present study, Brazilian middle-schoolers between grades 6 and 9 (N = 126) completed two divergent thinking tasks––the Alternate Uses Task and the Divergent Association Task––both with and without the assistance of generative AI. When children’s access to an AI tool was taken away from them from one task to another, they performed worse on the second divergent thinking task. While this result could be attributed to children trying less on any task after using AI, finding future tasks to be more difficult without AI assistance, or feeling less creative after using AI, each of these explanations do not align with the study’s quantitative findings. Given these results, and a qualitative analysis of children’s conversations with AI, I claim that AI use for creative tasks may result in negative transfer in children. These findings may only be generalized to middle school aged students in Brazil, and more work is needed to fully understand both how children use AI differently from adults and the impact that AI has on learning transfer in different domains.

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Experiment on how children's AI use affects divergent thinking; the LLM is the intervention, not a coder, and no LLM–human scoring agreement is mentioned.); Sonnet ? (неясно, сравнивали ли с людьми: Experiment on AI use and divergent thinking (AUT); the abstract doesn't say whether an LLM scored the responses against human raters, so the full text is needed.)

**Решение:** -

---

### 995 · R7216

**Evaluating Reasoning LLMs for Suicide Screening with the Columbia-Suicide Severity Rating Scale**

2025 · arXiv (Cornell University) · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/fmlds67896.2025.00067

Suicide prevention remains a critical public health challenge. While online platforms such as Reddit's r/SuicideWatch have historically provided spaces for individuals to express suicidal thoughts and seek community support, the advent of large language models (LLMs) introduces a new paradigm-where individuals may begin disclosing ideation to AI systems instead of humans. This study evaluates the capability of LLMs to perform automated suicide risk assessment using the Columbia-Suicide Severity Rating Scale (C-SSRS). We assess the zero-shot performance of six models-including Claude, GPT, Mistral, and LLaMA-in classifying posts across a 7-point severity scale (Levels 0-6). Results indicate that Claude and GPT closely align with human annotations, while Mistral achieves the lowest ordinal prediction error. Most models exhibit ordinal sensitivity, with misclassifications typically occurring between adjacent severity levels. We further analyze confusion patterns, misclassification sources, and ethical considerations, underscoring the importance of human oversight, transparency, and cautious deployment. Full code and supplementary materials are available at https://github.com/av9ash/llm_cssrs_code. 8 Pages, 6 Figures, 1 Table

**ИИ:** + · обе модели · клиническая оценка · LLMs classify Reddit posts on C-SSRS suicide severity levels and are compared with human annotations.

**Решение:** =

---

### 996 · R7218

**Moderating Harm: Benchmarking Large Language Models for Cyberbullying Detection in YouTube Comments**

2025 · International Journal of Computer Applications · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2505.18927

As online platforms grow, comment sections increasingly host harassment that undermines user experience and well-being. This study benchmarks three leading large language models, OpenAI GPT-4.1, Google Gemini 1.5 Pro, and Anthropic Claude 3 Opus, on a corpus of 5,080 YouTube comments sampled from high-abuse threads in gaming, lifestyle, food vlog, and music channels. The dataset comprises 1,334 harmful and 3,746 non-harmful messages in English, Arabic, and Indonesian, annotated independently by two reviewers with substantial agreement (Cohen's kappa = 0.83). Using a unified prompt and deterministic settings, GPT-4.1 achieved the best overall balance with an F1 score of 0.863, precision of 0.887, and recall of 0.841. Gemini flagged the highest share of harmful posts (recall = 0.875) but its precision fell to 0.767 due to frequent false positives. Claude delivered the highest precision at 0.920 and the lowest false-positive rate of 0.022, yet its recall dropped to 0.720. Qualitative analysis showed that all three models struggle with sarcasm, coded insults, and mixed-language slang. These results underscore the need for moderation pipelines that combine complementary models, incorporate conversational context, and fine-tune for under-represented languages and implicit abuse. A de-identified version of the dataset and full prompts is publicly released to promote reproducibility and further progress in automated content moderation. 9 pages, 3 tables, 1 figure

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs are benchmarked against human labels for flagging harmful YouTube comments. This is content moderation, closer to hate speech than to a psychological construct.); Sonnet ? (неясен конструкт: LLMs are benchmarked against two human annotators on cyberbullying in comments. It's unclear whether this counts as a psychological construct or as content moderation, like hate speech, which is excluded.)

**Решение:** -

---

### 997 · R7225

**Rethinking Suicidal Ideation Detection: A Trustworthy Annotation Framework and Cross-Lingual Model Evaluation**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2507.14693

Suicidal ideation detection is critical for real-time suicide prevention, yet its progress faces two under-explored challenges: limited language coverage and unreliable annotation practices. Most available datasets are in English, but even among these, high-quality, human-annotated data remains scarce. As a result, many studies rely on available pre-labeled datasets without examining their annotation process or label reliability. The lack of datasets in other languages further limits the global realization of suicide prevention via artificial intelligence (AI). In this study, we address one of these gaps by constructing a novel Turkish suicidal ideation corpus derived from social media posts and introducing a resource-efficient annotation framework involving three human annotators and two large language models (LLMs). We then address the remaining gaps by performing a bidirectional evaluation of label reliability and model consistency across this dataset and three popular English suicidal ideation detection datasets, using transfer learning through eight pre-trained sentiment and emotion classifiers. These transformers help assess annotation consistency and benchmark model performance against manually labeled data. Our findings underscore the need for more rigorous, language-inclusive approaches to annotation and evaluation in mental health natural language processing (NLP) while demonstrating the questionable performance of popular models with zero-shot transfer learning. We advocate for transparency in model training and dataset construction in mental health NLP, prioritizing data and model reliability. This manuscript has been submitted to the IEEE Journal of Biomedical and Health Informatics

**ИИ:** + · обе модели · бенчмарк с метками людей · Turkish suicidal-ideation posts annotated by three humans and two LLMs; LLM–human label agreement likely reported.

**Решение:** =

---

### 998 · R7233

**AI-Assisted Qualitative Coding: Comparing Human to Machine Outputs**

2025 · IEEE International Professional Communication Conference (ProComm) · conference, review, conference-paper · en · https://doi.org/10.1109/procomm64814.2025.00051

This study explores the application of generative AI in the qualitative coding of survey responses, comparing its performance to that of human coders. By using ChatGPT-4o, we aimed to automate the coding process traditionally performed manually, assessing the AI's ability to identify themes and patterns within textual data. Our findings reveal that while AI demonstrates remarkable efficiency and speed, it struggles with the nuanced understanding required for complex coding tasks. The AI frequently misinterpreted coding definitions and over-relied on certain codes, indicating a need for more balanced training data and iterative refinement. Despite these challenges, AI proved valuable in providing summative feedback and identifying overall trends, suggesting its potential as a complementary tool in qualitative research. The study underscores the importance of developing codebooks collaboratively with AI and highlights the necessity of human oversight to ensure accuracy and depth.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT-4o applied a codebook to survey responses and was compared with human coders, but the survey topic may not be psychological.

**Решение:** =

---

### 999 · R7238

**Human Experts vs. Large Language Models: Evaluating Annotation Scheme and Guidelines Development for Clinical Narratives**

2025 · Text2Story@ECIR · journalarticle

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The paper seems to be about LLMs developing annotation schemes for clinical narratives; unclear if they're psychological or include coding agreement.

**Решение:** =

---

### 1000 · R7243

**Evaluation of Prompting Strategies for Cyberbullying Detection Using Various Large Language Models**

2025 · Advances in Knowledge-Based Systems Data Science and Cybersecurity · journalarticle, article · en · https://doi.org/10.54364/cybersecurityjournal.2025.1109

Sentiment analysis detects toxic language for safer online spaces and helps businesses refine strategies through customer feedback analysis [1, 2]. Advancements in Large Language Models (LLMs) and prompt engineering have introduced novel approaches to sentiment analysis, cyberbullying detection, and toxicity classification. However, several challenges persist, particularly in handling text ambiguity, sarcasm, multilingual contexts, and nuanced emotional comprehension, which limit the ability to achieve accurate and human-aligned results. This study uses the CYBY23 dataset, which contains 112 human-annotated threads. To balance the dataset, synthetic threads were generated using ChatGPT, resulting in a final dataset of 148 threads evenly distributed across two labels: 0 (bullying with no aggression) and 1 (bullying with aggression). Three publicly available LLMs—Deepseek-r1-distillllama-70b (Deepseek), Qwen-2.5-32b (Qwen) and llama3-70b-8192 (Llama)—were systematically evaluated using zero-shot, one-shot, and few-shot prompting strategies, with all models accessed via Groq Cloud APIs. The model outputs were assessed using recall, precision, F1 scores, and accuracy to measure performance in different prompting techniques (PT). In this report, Qwen achieved the highest overall accuracy at 82.43% in few-shot 2, while Llama matched that accuracy in one-shot 2, demonstrating solid performance in few-shot tasks as well. Deepseek showed high variability, thriving with contextual enhancements in zero-shot 2 but struggling in one-shot and fluctuating in few-shot settings. one-shot prompting proved most effective for Llama, while few-shot methods worked best for both Qwen and Llama.

**ИИ:** ? · обе модели · неясен конструкт · LLMs classify cyberbullying aggression against human-annotated threads; it is unclear whether this counts as a psychological construct or as toxicity/hate-speech moderation.

**Решение:** =

---

### 1001 · R7260

**Using Large Language Models to Measure Symptom Severity in Patients At Risk for Schizophrenia**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2508.10226

Patients who are at clinical high risk (CHR) for schizophrenia need close monitoring of their symptoms to inform appropriate treatments. The Brief Psychiatric Rating Scale (BPRS) is a validated, commonly used research tool for measuring symptoms in patients with schizophrenia and other psychotic disorders; however, it is not commonly used in clinical practice as it requires a lengthy structured interview. Here, we utilize large language models (LLMs) to predict BPRS scores from clinical interview transcripts in 409 CHR patients from the Accelerating Medicines Partnership Schizophrenia (AMP-SCZ) cohort. Despite the interviews not being specifically structured to measure the BPRS, the zero-shot performance of the LLM predictions compared to the true assessment (median concordance: 0.84, ICC: 0.73) approaches human inter- and intra-rater reliability. We further demonstrate that LLMs have substantial potential to improve and standardize the assessment of CHR patients via their accuracy in assessing the BPRS in foreign languages (median concordance: 0.88, ICC: 0.70), and integrating longitudinal information in a one-shot or few-shot learning approach.

**ИИ:** + · обе модели · клиническая оценка · LLM rates BPRS symptom severity from clinical interview transcripts, compared with clinician BPRS ratings (ICC 0.73).

**Решение:** =

---

### 1002 · R7262

**Privacy-preserving local language models accurately identify the presence and timing of self-harm in electronic mental health records (Preprint)**

2025 · preprint · https://doi.org/10.2196/preprints.87586

BACKGROUND Self-harm, defined as intentional self-injury or self-poisoning irrespective of motivation, is the strongest risk factor for suicide and an important outcome for mental health care. Although highly prevalent in clinical populations, it is often imprecisely captured in routinely collected clinical data, where it is typically recorded and stored in unstructured, free-text format. Contemporary language models, such as GPT (OpenAI), Gemini (Google) and Claude (Anthropic) can analyse free-text clinical notes, but such cloud-based commercial and closed-source models may violate data governance of processing sensitive patient data. OBJECTIVE We evaluated whether a privacy-preserving language model running entirely within an institution’s secure computing infrastructure (here, the UK National Health Service) could accurately identify the presence and timing of self-harm using electronic health records (EHRs) from secondary mental healthcare. METHODS A random sample of 1,352 clinical notes from the EHRs of people with a confirmed diagnosis of a psychiatric disorder, according to the International Classification of Diseases (ICD-10), was selected from Oxford Health NHS Foundation Trust. Each clinical note was annotated for (i) presence or absence of self-harm and (ii) its recency (≤90 days vs. >90 days vs. unknown), constituting the gold-standard data set for model development and validation. Privacy-preserving locally served 27-billion-parameter Gemma 3 language model (‘Gemma3-27b’) was used as a core language model to identify self-harm along with its timing to generate a structured output per clinical record. The performance of Gemma3-27b model was compared against a strong baseline multi-label text classification model based on RoBERTa (Robustly Optimized BERT Pretraining Approach, a transformer-based language model) architecture. Model performance was evaluated using precision, recall, and the F1-score (harmonic mean of precision and recall), with 95% confidence intervals estimated from 1,000 bootstrap samples with replacement. RESULTS The Gemma3-27b model outperformed the RoBERTa classifier across all categories. Gemma3-27b achieved Precision = 0.92, Recall = 0.92 (sensitivity), and F1-score of 0.92 for notes containing self-harm, and Precision = 0.97, Recall = 0.97 (specificity), and F1-score of 0.97 for notes without self-harm. The performance of Gemma3-27b for recent self-harm was Precision = 0.84, Recall = 0.75, and F1-score of 0.79. The global weighted F1-score of Gemma3-27b across all categories was 0.88, compared to 0.85 for RoBERTa. CONCLUSIONS The prompt-engineered local language model outperformed the multi-label text classification RoBERTa model on the task of ascertaining self-harm events and their timing, while requiring significantly fewer high-fidelity annotated data. This approach offers a practical solution for improving self-harm case ascertainment whilst adhering to strict data governance rules to potentially transform clinical monitoring and response to this critical public health challenge. CLINICALTRIAL None

**ИИ:** + · обе модели · клиническая оценка · Gemma3-27b identifies self-harm presence and timing in mental health clinical notes, evaluated against a human-annotated gold standard.

**Решение:** =

---

### 1003 · R7264

**AI-powered analysis of single-session therapeutic conversation transcripts: Predicting the therapeutic bond from the session content**

2025 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/7uqrw

The therapeutic bond, the emotional component of the therapeutic alliance, encompassing mutual trust, acceptance, commitment to the relationship, and a sense of safety and support, is a robust common factor predicting therapy outcomes. Growing evidence highlights the importance of the first session in establishing this alliance. Research also shows that assessing the alliance from both client and therapist perspectives enhances predictive power. Recent advances in natural language processing (NLP) raise the possibility that AI may predict therapeutic bond based on complex data from psychotherapy sessions. The purpose of this study is to examine whether a widely available AI model (ChatGPT) can predict the quality of the therapeutic bond from the content of the initial session. The study involved 80 therapist–client dyads. The ‘therapists’ were fourth- and fifth-year psychology students specializing in psychotherapy, and the ‘clients’ were mostly students from other fields. Each interaction lasted 10 minutes and was recorded. The conversation focused on a topic chosen by the ‘client’ that evoked mild to moderately strong emotions. The student therapist’s task was to create the best possible conditions for the client to talk about themselves, using active listening techniques. After the interactions, both therapists and clients completed the Bond Scale from the Working Alliance Inventory and the Session Rating Scale. ChatGPT (a large language model–based NLP tool) was used to evaluate session transcripts in terms of depth, contact quality, emotional saturation, and the therapeutic bond drawing on Bowlby’s secure base concept; key elements of adult bonding dynamics described by Hazan &amp; Shaver and Mikulincer &amp; Shaver; the two-dimensional model of adult attachment by Brennan, Clark &amp; Shaver; and adapted aspects of attachment-related discourse. Additionally, two psychology students rated the depth and quality of contact in the interactions. This study will clarify whether widely available AI models can reliably estimate therapeutic alliance in a clinical context, potentially offering an alternative or supplement to self-report assessments. If validated, such tools could reduce assessment burden and mitigate response bias in psychotherapy research and practice.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: OSF pre-registration (protocol) with no results; the planned design compares ChatGPT and student ratings of session depth and contact quality.); Sonnet + (кодирование сессий: ChatGPT rates session transcripts for depth, contact quality and bond; two psychology students also rated depth and contact quality, enabling LLM–human agreement.)

**Решение:** -

---

### 1004 · R7271

**Measuring What Matters: Evaluating Ensemble LLMs with Label Refinement in Inductive Coding**

2025 · Underline Science Inc. · audiovisual/conference talk, conference-paper · en · https://doi.org/10.18653/v1/2025.findings-acl.563

Inductive coding traditionally relies on labor-intensive human efforts, who are prone to inconsistencies and individual biases. Although large language models (LLMs) offer promising automation capabilities, their standalone use often results in inconsistent outputs, limiting their reliability. In this work, we propose a framework that combines ensemble methods with code refinement methodology to address these challenges. Our approach integrates multiple smaller LLMs, fine-tuned via Low-Rank Adaptation (LoRA), and employs a moderator-based mechanism to simulate human consensus. To address the limitations of metrics like ROUGE and BERTScore, we introduce a composite evaluation metric that combines code conciseness and contextual similarity. The validity of this metric is confirmed through correlation analysis with human expert ratings. Results demonstrate that smaller ensemble models with refined outputs consistently outperform other ensembles, individual models, and even large-scale LLMs like GPT-4. Our evidence suggests that smaller ensemble models significantly outperform larger standalone language models, pointing out the risk of relying solely on a single large model for qualitative analysis.

**ИИ:** ? · обе модели · неясен конструкт · The ensemble LLMs do inductive coding of qualitative data checked against human codes, but the data domain and whether any psychological construct is coded are unclear.

**Решение:** =

---

### 1005 · R7272

**Text Annotation via Inductive Coding: Comparing Human Experts to LLMs in Qualitative Data Analysis**

2025 · Findings of the Association for Computational Linguistics: NAACL · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2025.findings-naacl.361

This paper investigates the automation of qualitative data analysis, focusing on inductive coding using large language models (LLMs). Unlike traditional approaches that rely on deductive methods with predefined labels, this research investigates the inductive process where labels emerge from the data. The study evaluates the performance of six open-source LLMs compared to human experts. As part of the evaluation, experts rated the perceived difficulty of the quotes they coded. The results reveal a peculiar dichotomy: human coders consistently perform well when labeling complex sentences but struggle with simpler ones, while LLMs exhibit the opposite trend. Additionally, the study explores systematic deviations in both human and LLM generated labels by comparing them to the golden standard from the test set. While human annotations may sometimes differ from the golden standard, they are often rated more favorably by other humans. In contrast, some LLMs demonstrate closer alignment with the true labels but receive lower evaluations from experts.

**ИИ:** ? · обе модели · неясен конструкт · LLMs inductively code qualitative quotes and are compared to human experts and gold labels, but the domain and whether it is psychological are unclear.

**Решение:** =

---

### 1006 · R7293

**Limitations of the LLM-as-a-Judge Approach for Evaluating LLM Outputs in Expert Knowledge Tasks**

2025 · ACM International Conference on Intelligent User Interfaces (IUI) · journalarticle, book, conference · en · https://doi.org/10.1145/3708359.3712091

The potential of using Large Language Models (LLMs) themselves to evaluate LLM outputs offers a promising method for assessing model performance across various contexts. Previous research indicates that LLM-as-a-judge exhibits a strong correlation with human judges in the context of general instruction following. However, for instructions that require specialized knowledge, the validity of using LLMs as judges remains uncertain. In our study, we applied a mixed-methods approach, conducting pairwise comparisons in which both subject matter experts (SMEs) and LLMs evaluated outputs from domain-specific tasks. We focused on two distinct fields: dietetics, with registered dietitian experts, and mental health, with clinical psychologist experts. Our results showed that SMEs agreed with LLM judges 68% of the time in the dietetics domain and 64% in mental health when evaluating overall preference. Additionally, the results indicated variations in SME-LLM agreement across domain-specific aspect questions. Our findings emphasize the importance of keeping human experts in the evaluation process, as LLMs alone may not provide the depth of understanding required for complex, knowledge specific tasks. We also explore the implications of LLM evaluations across different domains and discuss how these insights can inform the design of evaluation workflows that ensure better alignment between human experts and LLMs in interactive systems.

**ИИ:** + · обе модели · LLM-судья · LLM judges and clinical psychologist experts made the same pairwise judgments of mental-health outputs; reported agreement was 64%.

**Решение:** =

---

### 1007 · R7295

**Classifying Unreliable Narrators with Large Language Models**

2025 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2506.10231

Often when we interact with a first-person account of events, we consider whether or not the narrator, the primary speaker of the text, is reliable. In this paper, we propose using computational methods to identify unreliable narrators, i.e. those who unintentionally misrepresent information. Borrowing literary theory from narratology to define different types of unreliable narrators based on a variety of textual phenomena, we present TUNa, a human-annotated dataset of narratives from multiple domains, including blog posts, subreddit posts, hotel reviews, and works of literature. We define classification tasks for intra-narrational, inter-narrational, and inter-textual unreliabilities and analyze the performance of popular open-weight and proprietary LLMs for each. We propose learning from literature to perform unreliable narrator classification on real-world text data. To this end, we experiment with few-shot, fine-tuning, and curriculum learning settings. Our results show that this task is very challenging, and there is potential for using LLMs to identify unreliable narrators. We release our expert-annotated dataset and code at https://github.com/adbrei/unreliable-narrators and invite future research in this area.

**ИИ:** ? · обе модели · неясен конструкт · LLMs classify narrator unreliability against expert annotations; a narratology construct that may only partly count as psychological.

**Решение:** =

---

### 1008 · R7321

**Does ChatGPT get it? LLM-driven annotation of Humor**

2025 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5500673

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. ChatGPT annotating humor may be compared with human labels; unclear if humor is coded as a psychological construct.

**Решение:** =

---

### 1009 · R7322

**Emotion in Context: Human and AI Perspectives on the Affective Landscape of Severance**

2025 · Corpus Pragmatics · journalarticle, article · en · https://doi.org/10.1007/s41701-025-00220-6

Abstract Emotion identification has long been a focus of interdisciplinary research spanning psychology, linguistics, and discourse analysis. Prior to the advent of artificial intelligence and large language models (LLMs), emotion recognition relied heavily on annotation and sentiment lexicons (e.g., Mohammad & Turney, 2013), often supported by sentiment analysis tools with limited sensitivity to contextual nuance. These traditional approaches, however, struggled with the complexity of emotional expression, particularly in multimodal or narrative-rich texts. Recent advances in natural language processing (NLP), particularly the development of LLMs, offer new possibilities for automating emotion detection with greater contextual awareness. This study investigates how emotions are represented and perceived in the television series Severance (Apple TV, 2022) through a multi-layered annotation framework based on Parrott’s hierarchical taxonomy of emotions. All nine episodes of season 1 were annotated scene by scene, producing four datasets: human text-only, human multimodal (video + audio + text), and two large-language-model (LLM) outputs. Comparative analyses assessed inter-annotator agreement, modality effects, and temporal and character-based emotion patterns. Results show that multimodal annotations yield a far richer and more nuanced emotional landscape than text alone, highlighting the decisive role of prosody, gesture, and facial expression in conveying affect. LLMs captured general emotional polarity but failed to reproduce fine-grained distinctions. Character profiles further reveal individualized affective strategies of repression, resistance, and awakening. The findings underscore the inherently multimodal nature of emotional meaning in audiovisual narrative.

**ИИ:** разошлись — Opus + (кодирование по кодбуку: LLM and human annotators coded emotions in Severance scenes using Parrott's taxonomy; inter-annotator agreement compared.); Sonnet ? (неясен конструкт: LLM and human annotators coded emotions (Parrott taxonomy) in TV series scenes, with agreement analysed. It's unclear whether fictional audiovisual dialogue counts as psychological text.)

**Решение:** +

---

### 1010 · R7324

**In-context learning for the classification of manipulation techniques in phishing emails**

2025 · European Symposium on Research in Computer Security · journalarticle, conference, preprint/article · en · https://doi.org/10.48550/arxiv.2506.22515

Traditional phishing detection often overlooks psychological manipulation. This study investigates using Large Language Model (LLM) In-Context Learning (ICL) for fine-grained classification of phishing emails based on a taxonomy of 40 manipulation techniques. Using few-shot examples with GPT-4o-mini on real-world French phishing emails (SignalSpam), we evaluated performance against a human-annotated test set (100 emails). The approach effectively identifies prevalent techniques (e.g., Baiting, Curiosity Appeal, Request For Minor Favor) with a promising accuracy of 0.76. This work demonstrates ICL's potential for nuanced phishing analysis and provides insights into attacker strategies.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o-mini coded phishing emails for psychological manipulation techniques against human annotations; unclear whether this counts as a psychological construct or a security category.

**Решение:** =

---

### 1011 · R7326

**PULSE: A Multi-stage Artificial Intelligence Framework for Analyzing Vaccine Hesitancy on Twitter using Particle Swarm Optimization and Large Language Models**

2025 · Swarm and Evolutionary Computation · article · en · https://doi.org/10.1016/j.swevo.2025.102218

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: No abstract; going by the title, vaccine hesitancy on Twitter is a stance/opinion category, not a psychological construct; human-coding comparison also unclear.); Sonnet ? (нет аннотации: No abstract; LLM analysis of vaccine hesitancy tweets, possibly stance-like and possibly validated against human labels, which can't be determined from the title.)

**Решение:** -

---

### 1012 · R7331

**DepreSym: A Depression Symptom Annotated Corpus and the Role of Large Language Models as Assessors of Psychological Markers**

2025 · Language Resources and Evaluation · journalarticle, article · en · https://doi.org/10.1007/s10579-025-09831-6

Abstract Computational methods for depression detection aim to mine traces of depression from online publications posted by Internet users. However, solutions trained on existing collections exhibit limited generalisation and interpretability. To tackle these issues, recent studies have shown that identifying specific depressive symptoms can lead to more robust and effective models. The eRisk initiative fosters research on this area and has recently proposed a new ranking task focused on developing search methods to find sentences related to depressive symptoms. This search challenge relies on the symptoms specified by the Beck Depression Inventory-II (BDI-II), a questionnaire widely used in clinical practice. It includes symptoms such as sadness, irritability or lack of sleep. Given the input submitted by systems participating in eRisk, we first apply top-k pooling over the systems’ relevance rankings, obtaining a diverse set of sentences. These sentences are judged for relevance, leading to DepreSym, a dataset consisting of 21,580 sentences annotated according to their relevance to the 21 BDI-II symptoms. This dataset serves as a valuable resource for advancing the development of models that monitor depression markers. Due to the complex nature of this relevance annotation, we designed a robust assessment methodology carried out by three expert assessors, including a trained psychologist. As part of this study, we explore the potential of recent Large Language Models (ChatGPT, GPT4 and Vicuna) as assessors in this complex task. We undertake a comprehensive examination of the LLMs’ performance, studying their main limitations and analysing their role as a complement or replacement for human annotators. Finally, we incorporate our dataset into the Benchmarking Information Retrieval (BEIR) framework for a thorough search evaluation. We use state-of-the-art retrieval systems, including lexical, sparse, dense and re-ranking architectures, to gain insights about the dataset’s complexity and identify potential avenues for improvement.

**ИИ:** + · обе модели · бенчмарк с метками людей · ChatGPT, GPT-4 and Vicuna act as assessors of the relevance of sentences to BDI-II depression symptoms, compared with expert human annotators.

**Решение:** =

---

### 1013 · R7336

**Identifying Bias at Scale in Clinical Notes Using Large Language Models.**

2025 · Mayo Clinic proceedings. Digital health · journal article, journalarticle, review · eng · https://doi.org/10.1016/j.mcpdig.2025.100296

Objective: To evaluate whether generative pretrained transformer (GPT)-4 can detect and revise biased language in emergency department (ED) notes, against human-adjudicated gold-standard labels, and to identify modifiable factors associated with biased documentation. Patients and Methods: We randomly sampled 50,000 ED medical and nursing notes from the Mount Sinai Health System (January 1, 2023, to December 31, 2023). We also randomly sampled 500 discharge notes from the Medical Information Mart for Intensive Care IV database. The GPT-4 flagged 4 types of bias: discrediting, stigmatizing/labeling, judgmental, and stereotyping. Two human reviewers verified model detections. We used multivariable logistic regression to examine associations between bias and health care utilization, presenting problems (eg, substance use), shift timing, and provider type. We then asked physicians to rate GPT-4's proposed language revisions on a 10-point scale. Results: The GPT-4 showed 97.6% sensitivity and 85.7% specificity compared with the human review. Biased language appeared in 6.5% (3229 of 50,000) of Mount Sinai notes and 7.4% (37 of 500) of Medical Information Mart for Intensive Care IV notes. In adjusted models, frequent health care utilization (adjusted odds ratio [aOR], 2.85; 95% CI, 1.95-4.17), substance use presentations (aOR, 3.09; 95% CI, 2.51-3.80), and overnight shifts (aOR, 1.37; 95% CI, 1.23-1.52) showed elevated odds of biased documentation. Physicians were more likely to include bias than nurses (aOR, 2.26; 95% CI, 2.07-2.46); GPT-4's recommended revisions received mean physician ratings above 9 of 10. Conclusion: The study showed that GPT-4 accurately detects biased language in clinical notes, identifies modifiable contributors to that bias, and delivers physician-endorsed revisions. This approach may help mitigate documentation bias and reduce disparities in care.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 detection of stigmatizing/judgmental language in ED notes was checked against human-adjudicated labels; unclear whether clinician bias counts as a psychological construct.

**Решение:** =

---

### 1014 · R7338

**Benchmarking Open-Source Large Language Models for Sentiment and Emotion Classification in Indonesian Tweets**

2025 · IEEE Access · journalarticle, article · en · https://doi.org/10.1109/access.2025.3574629

We benchmark 22 open-source large language models (LLMs) against ChatGPT-4 and human annotators on two NLP tasks—sentiment analysis and emotion classification—for Indonesian tweets. This study contributes to NLP in a relatively low-resource language (Bahasa Indonesia) by evaluating zero-shot classification performance on a labeled tweet corpus. The dataset includes sentiment labels (Positive, Negative, Neutral) and emotion labels (Love, Happiness, Sadness, Anger, Fear). We compare model predictions to human annotations and report precision, recall, and F1-score, along with inference time analysis. ChatGPT-4 achieves the highest macro F1-score (0.84) on both tasks, slightly outperforming human annotators. The best-performing open-source models—such as LLaMA3.1_70B and Gemma2_27B—achieve over 90% of ChatGPT-4’s performance, while smaller models lag behind. Notably, some mid-sized models (e.g., Phi-4 at 14B parameters) perform comparably to much larger models on select categories. However, certain classes—particularly Neutral sentiment and Fear emotion—remain challenging, with lower agreement even among human annotators. Inference time varies significantly: optimized models complete predictions in under an hour, while some large models require several days. Our findings show that state-of-the-art open models can approach closed-source LLMs like ChatGPT-4 on Indonesian classification tasks, though efficiency and consistency in edge cases remain open challenges. Future work should explore fine-tuning multilingual LLMs on Indonesian data and practical deployment strategies in real-world applications.

**ИИ:** + · обе модели · бенчмарк с метками людей · LLMs classify emotions (love, happiness, sadness, anger, fear) in Indonesian tweets, compared with human annotations (F1 reported).

**Решение:** =

---

### 1015 · R7343

**Exploring the Use of Large Language Models (LLMs) to Estimate Depression Severity through BDI Scoring: A Pilot Study**

2025 · Unpublished · text/preprint · https://doi.org/10.13140/rg.2.2.35060.05764

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM estimating BDI depression severity, reference may be self-report or clinician scoring.

**Решение:** =

---

### 1016 · R7347

**Why We Feel What We Feel: Joint Detection of Emotions and Their Opinion Triggers in E-commerce**

2025 · Conference on Empirical Methods in Natural Language Processing · journalarticle, conference, review · en · https://doi.org/10.18653/v1/2025.findings-emnlp.295

Customer reviews on e-commerce platforms capture critical affective signals that drive purchasing decisions. However, no existing research has explored the joint task of emotion detection and explanatory span identification in e-commerce reviews - a crucial gap in understanding what triggers customer emotional responses. To bridge this gap, we propose a novel joint task unifying Emotion detection and Opinion Trigger extraction (EOT), which explicitly models the relationship between causal text spans (opinion triggers) and affective dimensions (emotion categories) grounded in Plutchik's theory of 8 primary emotions. In the absence of labeled data, we introduce EOT-X, a human-annotated collection of 2,400 reviews with fine-grained emotions and opinion triggers. We evaluate 23 Large Language Models (LLMs) and present EOT-DETECT, a structured prompting framework with systematic reasoning and self-reflection. Our framework surpasses zero-shot and chain-of-thought techniques, across e-commerce domains. 23 pages, 11 figures, 7 tables. Dataset and code will be made publicly available

**ИИ:** ? · обе модели · неясен конструкт · 23 LLMs evaluated against human-annotated Plutchik emotions in e-commerce reviews; emotion construct qualifies, but product-review context is borderline.

**Решение:** =

---

### 1017 · R7361

**Leveraging large language models for detecting and preserving emotions in quran translations**

2025 · Journal of King Saud University - Computer and Information Sciences · journalarticle, article · en · https://doi.org/10.1007/s44443-025-00269-y

Over the years, translations of the Quran have served as a vital tool for conveying its message to non-Arabic speaking audiences. This research proposes a computational quantitative approach to investigate emotion preservation in English translations of the Quran using Large Language Models (LLMs). The proposed approach implements emotion analysis using the state-of-the-art models and evaluates the agreement levels through a human validation process, using a parallel corpus of the Quran with seven English translations. This research yields the Emotionally-Labeled Quran Verses (ELQV) dataset, a collection of 2100 Quran verses annotated by specialists, designed to advance Arabic Natural Language Processing (NLP), particularly NLP-based Quranic research. The analysis demonstrates that the investigated translations preserved the emotional semantics at a fair level. Compared to the Quran, neither of the translations reached substantial agreement with Arabic readers, with Cohen’s Kappa (κ\documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$\kappa $$\end{document}) scores ranging from 0.29 to 0.35. Despite the challenges associated with Classical Arabic scripts, the LLMs adopted in this research proved their ability to capture the emotional semantics of the Quran, indicating their aptitude to comprehend complex scripts with cultural and theological significance.

**ИИ:** ? · обе модели · неясен конструкт · LLM emotion labelling of Quran verses checked against specialist annotations (kappa); scripture is not typical psychological text, and model types are unclear.

**Решение:** =

---

### 1018 · R7376

**AI Through the Human Lens: Investigating Cognitive Theories in Machine Psychology**

2025 · Underline Science Inc. · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48448/f7v0-bk19

We investigate whether Large Language Models (LLMs) exhibit human-like cognitive patterns under four established frameworks from psychology: Thematic Apperception Test (TAT), Framing Bias, Moral Foundations Theory (MFT), and Cognitive Dissonance. We evaluated several proprietary and open-source models using structured prompts and automated scoring. Our findings reveal that these models often produce coherent narratives, show susceptibility to positive framing, exhibit moral judgments aligned with Liberty/Oppression concerns, and demonstrate self-contradictions tempered by extensive rationalization. Such behaviors mirror human cognitive tendencies yet are shaped by their training data and alignment methods. We discuss the implications for AI transparency, ethical deployment, and future work that bridges cognitive psychology and AI safety Accepted to IJCNLP-AACL 2025 Student Research Workshop

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Machine psychology study; LLM-generated TAT narratives are scored automatically. It's unclear whether that scoring was checked against human scorers.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Studies LLMs' own human-like cognitive patterns (TAT, framing, MFT); LLM outputs are analyzed, with no LLM–human coding agreement on psychological text.)

**Решение:** -

---

### 1019 · R7380

**Assessing effective de-escalation of crisis conversations using transformer-based models and trend statistics**

2025 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/bem4-aq91

One of the core goals of crisis counseling services is to support emotional de-escalation of the individual in crisis, by reducing intense negative emotional affect and emotional dysregulation. The science of crisis intervention has been impeded, however, by a lack of quantitative approaches that allow for detailed analysis of emotion in crisis conversations. In order to measure de-escalation at scale (millions of text-based conversations), lightweight models are needed that can assign not just binary sentiment predictions but quantitative scores to capture graded change in emotional valence. Accordingly, we developed a transformer-based emotional valence scoring model fit for crisis conversations, BERT-EV, that assigns numerical emotional valence scores to rate the intensity of expressed negative versus positive emotion. This transformer-based model can run on modest hardware configurations, allowing it to scale affordably and efficiently to a massive corpus of crisis conversations. We evaluated model performance on a corpus of hand-scored social media messages, and found that BERT-EV outperforms existing dictionary-based standard tools in the field, as well as other transformer-based implementations and an LLM in accurately matching scores from human annotators. Finally, we show that trends in these emotional valence scores can be used to assess emotional de-escalation during crisis conversations, with sufficient turn-by-turn granularity to help identify helpful vs. detrimental crisis counselor statements.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: An LLM baseline was scored against human-annotated emotional valence of social media messages, alongside the main BERT model.); Sonnet ? (другое: Main model is BERT-based, but an LLM baseline was also compared with human annotators' emotional valence scores; LLM-human agreement may be reported in full text.)

**Решение:** +

---

### 1020 · R7388

**Can Large Language Models Identify Implicit Suicidal Ideation? An Empirical Evaluation**

2025 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/c6by-1938

Suicide remains a major global mental health challenge, and early intervention hinges on recognizing signs of suicidal ideation. In private conversations, such ideation is often expressed in subtle or conflicted ways, making detection especially difficult. Existing data sets are mainly based on public help-seeking platforms such as Reddit, which fail to capture the introspective and ambiguous nature of suicidal ideation in more private contexts. To address this gap, we introduce \ourdata, a novel dataset of 1,200 test cases simulating implicit suicidal ideation within psychologically rich dialogue scenarios. Each case is grounded in psychological theory, combining the Death/Suicide Implicit Association Test (D/S-IAT) patterns, expanded suicidal expressions, cognitive distortions, and contextual stressors. In addition, we propose a psychology-guided evaluation framework to assess the ability of LLMs to identify implicit suicidal ideation through their responses. Experiments with eight widely used LLMs across varied prompting conditions reveal that current models often struggle significantly to recognize implicit suicidal ideation. Our findings highlight the urgent need for more clinically grounded evaluation frameworks and design practices to ensure the safe use of LLMs in sensitive support systems.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs detect implicit suicidal ideation in simulated dialogues; labels may come from how cases were built, and it's unclear whether humans annotated or validated them.

**Решение:** =

---

### 1021 · R7398

**EmplifAI: a Fine-grained Dataset for Japanese Empathetic Medical Dialogues in 28 Emotion Labels**

2025 · Underline Science Inc. · audiovisual/conference talk, journalarticle, review · https://doi.org/10.48448/xc5a-ma54

This paper introduces EmplifAI, a Japanese empathetic dialogue dataset designed to support patients coping with chronic medical conditions. They often experience a wide range of positive and negative emotions (e.g., hope and despair) that shift across different stages of disease management. EmplifAI addresses this complexity by providing situation-based dialogues grounded in 28 fine-grained emotion categories, adapted and validated from the GoEmotions taxonomy. The dataset includes 280 medically contextualized situations and 4,125 two-turn dialogues, collected through crowdsourcing and expert review. To evaluate emotional alignment in empathetic dialogues, we assessed model predictions on situation–dialogue pairs using BERTScore across multiple large language models (LLMs), achieving F1 scores of ≤ 0.83. Fine-tuning a baseline Japanese LLM (LLM-jp-3.1-13b-instruct4) with EmplifAI resulted in notable improvements in fluency, general empathy, and emotion-specific empathy. Furthermore, we compared the scores assigned by LLM-as-a-Judge and human raters on dialogues generated by multiple LLMs to validate our evaluation pipeline and discuss the insights and potential risks derived from the correlation analysis.

**ИИ:** + · обе модели · LLM-судья · An LLM-as-a-Judge rating of empathy in emotional medical dialogues is compared with human raters' scores of the same dialogues.

**Решение:** =

---

### 1022 · R7405

**Humans Hallucinate Too: Language Models Identify and Correct Subjective Annotation Errors With Label-in-a-Haystack Prompts**

2025 · Underline Science Inc. · audiovisual/conference talk, preprint/article, other · https://doi.org/10.48448/9e42-a772

Modeling complex subjective tasks in Natural Language Processing, such as recognizing emotion and morality, is considerably challenging due to significant variation in human annotations. This variation often reflects reasonable differences in semantic interpretations rather than mere noise, necessitating methods to distinguish between legitimate subjectivity and error. We address this challenge by exploring label verification in these contexts using Large Language Models (LLMs). First, we propose a simple In-Context Learning binary filtering baseline that estimates the reasonableness of a document-label pair. We then introduce the Label-in-a-Haystack setting: the query and its label(s) are included in the demonstrations shown to LLMs, which are prompted to predict the label(s) again, while receiving task-specific instructions (e.g., emotion recognition) rather than label copying. We show how the failure to copy the label(s) to the output of the LLM are task-relevant and informative. Building on this, we propose the Label-in-a-Haystack Rectification (LiaHR) framework for subjective label correction: when the model outputs diverge from the reference gold labels, we assign the generated labels to the example instead of discarding it. This approach can be integrated into annotation pipelines to enhance signal-to-noise ratios. Comprehensive analyses, human evaluations, and ecological validity studies verify the utility of LiaHR for label correction. Code is available at https://github.com/gchochla/liahr. Accepted to the Main Proceedings of EMNLP, 2025. 20 pages, 16 figures, 10 tables

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: LLMs label emotion and morality in text and are compared with human gold annotations, with human evaluations; likely reports LLM–human agreement.); Sonnet ? (другое: LLMs re-predict and correct human emotion and morality labels in NLP datasets. This is about label verification, not coder agreement, and the texts are not clearly psychological or clinical.)

**Решение:** +

---

### 1023 · R7408

**IntentionFrame: A Semi-Structured, Multi-Aspect Framework for Fine-Grained Conversational Intention Understanding**

2025 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/8gfq-h354

Understanding user intentions in multi-turn dialogues is critical for conversational AI, yet existing approaches—relying on rigid slot-value structures or unstructured free-text—fail to fully capture conversational complexity. In this paper, we propose IntentionFrame, a semi-structured framework inspired by psychological and cognitive intention theories, which organizes conversational intents into four interrelated aspects: situation, emotion, action, and knowledge. This design not only retains interpretability but also provides LLMs with a rich context to accurately parse and respond to nuanced user inputs. To efficiently scale IntentionFrame annotations, we introduce a Weakly-supervised Reinforced Generation (WeRG) method that leverages a small set of high-quality human annotations in conjunction with abundant coarsely labeled data. By applying reinforcement learning to balance these diverse signals, WeRG aims to effectively generate reliable IntentionFrame annotations, which serve as essential grounding for downstream tasks—leading to substantial improvements in response generation and task completion. Our experiments, supported by both automatic metrics and human evaluations, show that integrating IntentionFrame with WeRG significantly improves LLMs’ conversational understanding and sets a new benchmark for intent analysis.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM-generated intention annotations (including emotion) for general dialogues with some human annotations; unclear if psychological construct or LLM-human agreement reported.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Conversational AI intent-understanding framework with annotation generation; not coding psychological constructs for LLM–human agreement in clinical or psychological text.)

**Решение:** -

---

### 1024 · R7416

**Metamo: Empowering Large Language Models with Psychological Distortion Detection for Cognition-aware Coaching**

2025 · Underline Science Inc. · audiovisual/conference talk, conference-paper, other · https://doi.org/10.48448/x7p1-sw46

We demonstrate Metamo, a browser-based dialogue system that transforms an off-the-shelf large language model into an empathetic coach for everyday workplace concerns. Metamo introduces a light, single-pass wrapper that first identifies the cognitive distortion behind an emotion, then recognizes the user’s emotion, and finally produces a question-centered reply that invites reflection, all within one model call. The wrapper keeps the response time below two seconds in the API, yet enriches the feedback with cognitively grounded insight. A front-end web interface renders the detected emotion as an animated avatar and shows distortion badges in real time, whereas a safety layer blocks medical advice and redirects crisis language to human hotlines. Empirical tests on public corpora confirmed that the proposed design improved emotion‑recognition quality and response diversity without sacrificing latency. A small user study with company staff reported higher perceived empathy and usability than a latency‑matched baseline. Metamo is model-agnostic, illustrating a practical path toward cognition-aware coaching tools.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: LLM detects emotions and cognitive distortions and is tested on public corpora; whether those corpora have human labels and agreement is reported is unclear.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: System demo of an LLM coaching chatbot generating replies; emotion recognition tested on public corpora but no clear LLM–human coding agreement focus.)

**Решение:** -

---

### 1025 · R7430

**Sarc7: Evaluating Sarcasm Detection and Generation with Seven Types and Emotion-Informed Techniques**

2025 · Underline Science Inc. · audiovisual/conference talk, journalarticle, preprint/article · en · https://doi.org/10.48448/hm0d-8846

Sarcasm is a complex linguistic and pragmatic phenomenon where expressions convey meanings that contrast with their literal interpretations, requiring sensitivity to the speaker's intent and context. Misinterpreting sarcasm in collaborative human–AI settings can lead to under- or overreliance on LLM outputs, with consequences ranging from breakdowns in communication to critical safety failures. We introduce Sarc7, a benchmark for fine-grained sarcasm evaluation based on the MUStARD dataset, annotated with seven pragmatically defined sarcasm types: self-deprecating, brooding, deadpan, polite, obnoxious, raging, and manic. These categories are adapted from prior linguistic work and used to create a structured dataset suitable for LLM evaluation. For classification, we evaluate multiple prompting strategies—zero-shot, few-shot, chain-of-thought (CoT), and a novel emotion-based technique—across five major LLMs. Emotion-based prompting yields the highest macro-averaged F1 score of 0.3664 (Gemini 2.5), outperforming CoT for several models and demonstrating its effectiveness in sarcasm type recognition. For sarcasm generation, we design structured prompts using fixed values across four sarcasm-relevant dimensions: incongruity, shock value, context dependency, and emotion. Using Claude 3.5 Sonnet, this approach produces more subtype-aligned outputs, with human evaluators preferring emotion-based generations 38.46% more often than zero-shot baselines. Sarc7 offers a foundation for evaluating nuanced sarcasm understanding and controllable generation in LLMs, pushing beyond binary classification toward interpretable, emotion-informed language modeling.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs classify human-annotated sarcasm types in dialogue; sarcasm is mainly linguistic/pragmatic, so whether it counts as psychological is borderline.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Sarcasm-type benchmark on TV dialogue (MUStARD) is a linguistic/pragmatic construct, not a psychological or clinical one. It resembles stance or sentiment tasks.)

**Решение:** -

---

### 1026 · R7431

**SEER: The Span-based Emotion Evidence Retrieval Benchmark**

2025 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/xeh1-v512

Emotion recognition methods typically assign labels at the sentence level, obscuring the specific linguistic cues that signal emotion. This limits their utility in applications requiring targeted responses, such as empathetic dialogue and clinical support, which depend on knowing which language expresses emotion. The task of identifying \textit{emotion evidence} -- text spans conveying emotion -- remains underexplored due to a lack of labeled data. Without span-level annotations, we cannot evaluate whether models truly localize emotion expression, nor can we diagnose the sources of emotion misclassification. We introduce the SEER (Span-based Emotion Evidence Retrieval) Benchmark to evaluate Large Language Models (LLMs) on this task. SEER evaluates single and multi-sentence span identification with new annotations on 1200 real-world sentences. We evaluate 14 LLMs and find that, on single-sentence inputs, the strongest models match the performance of average human annotators, but performance declines in multi-sentence contexts. Key failure modes include fixation on emotion keywords and false positives in neutral text.

**ИИ:** + · обе модели · бенчмарк с метками людей · Benchmark paper testing 14 LLMs on emotion-evidence span identification against new human annotations of 1,200 real-world sentences.

**Решение:** =

---

### 1027 · R7436

**Third-Person Appraisal Agent: Simulating Human Emotional Reasoning in Text with Large Language Models**

2025 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/hfmp-6b38

Emotional reasoning is essential for improving human-AI interactions, particularly in mental health support and empathetic systems. However, current approaches, which primarily map sensory inputs to fixed emotion labels, fail to understand the intricate relationships between motivations, thoughts, and emotions, thereby limiting their ability to generalize across flexible emotional reasoning tasks. To address this, we propose a novel third-person appraisal agent that simulates human-like emotional reasoning through three phases: Primary Appraisal, Secondary Appraisal, and Reappraisal. In the Primary Appraisal phase, a third-person generator powered by a large language model (LLM) infers emotions based on cognitive appraisal theory. The Secondary Appraisal phase uses an evaluator LLM to provide feedback, guiding the generator in refining its predictions. The generator then uses counterfactual reasoning to adjust its process and explore alternative emotional responses. The Reappraisal phase utilizes reinforced fine-tuning (ReFT) by employing a reflective actor-critic framework to further enhance the model’s performance and generalization. This process uses reward signals and learns from appraisal trajectories without human annotations. Our approach outperforms baseline LLMs in various emotional reasoning tasks, demonstrating superior generalization and interpretability. To the best of our knowledge, this is the first cognition-based architecture designed to enhance emotional reasoning in LLMs, advancing AI towards human-like emotional understanding.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM agent infers emotions in text on emotional reasoning benchmarks; unclear whether the reference labels come from human annotation.

**Решение:** =

---

### 1028 · R7438

**Towards AI-Assisted Psychotherapy: Emotion-Guided Generative Interventions**

2025 · Underline Science Inc. · audiovisual/conference talk, conference-paper, other · https://doi.org/10.48448/w0kj-0898

Large language models (LLMs) hold promise for therapeutic interventions, yet most existing datasets rely solely on text, overlooking non-verbal emotional cues essential to real-world therapy. To address this, we introduce a multimodal dataset of 1,441 publicly sourced therapy session videos containing both dialogue and non-verbal signals such as facial expressions and vocal tone. Inspired by Hochschild’s concept of emotional labor, we propose a computational formulation of \textit{emotional dissonance}—the mismatch between facial and vocal emotion—and use it to guide emotionally aware prompting. Our experiments show that integrating multimodal cues, especially dissonance, improves the quality of generated interventions. We also find that LLM-based evaluators misalign with expert assessments in this domain, highlighting the need for human-centered evaluation. Data and code will be released to support future research.

**ИИ:** + · обе модели · LLM-судья · LLM-based evaluators of generated therapy interventions are compared with expert assessments, and the abstract reports they misalign.

**Решение:** =

---

### 1029 · R7447

**Large language models fall short in classifying learners’ open-ended responses**

2025 · Research Methods in Applied Linguistics · article · en · https://doi.org/10.1016/j.rmal.2025.100210

Generative Artificial Intelligence (GenAI), based on large language models (LLMs), excels in various language comprehension tasks and is increasingly utilized in applied linguistics research. This study examines the accuracy and methodological implications of using LLMs to classify open-ended responses from learners. We surveyed 143 Japanese university students studying English as a foreign language (EFL) about their essay-writing process. Two human evaluators independently classified the students’ responses based on self-regulated learning processes: planning, monitoring, and evaluation. At the same time, several LLMs performed the same classification task, and their results were compared with those of the human evaluators using Cohen’s kappa coefficient. We established κ ≥ 0.8 as the threshold for strong agreement based on rigorous methodological standards. Our findings revealed that even the best-performing model (DeepSeek-V3) achieved only moderate agreement (κ = 0.68), while other models demonstrated fair-to-moderate agreement (κ = 0.37–0.61). Surprisingly, open-source models outperformed several commercial counterparts. These results highlight the necessity of expert oversight when integrating GenAI as a support tool in qualitative data analysis. The paper concludes by discussing the methodological implications for using LLMs in qualitative research and proposing specific prompt engineering strategies to enhance their reliability in applied linguistics.

**ИИ:** + · обе модели · кодирование по кодбуку · LLMs coded open-ended responses about self-regulated learning (metacognitive processes) and were compared against two human coders using Cohen's kappa.

**Решение:** =

---

### 1030 · R7472

**Multimodal LLM vs. Human-Measured Features for AI Predictions of Autism in Home Videos.**

2025 · Algorithms · journal article, journalarticle, article · eng · https://doi.org/10.3390/a18110687

Autism diagnosis remains a critical healthcare challenge, with current assessments contributing to average diagnostic ages of 5 and extending to 8 in underserved populations. With the FDA approval of CanvasDx in 2021, the paradigm of human-in-the-loop AI diagnostics entered the pediatric market as the first medical device for clinically precise autism diagnosis at scale, while fully automated deep learning approaches have remained underdeveloped. However, the importance of early autism detection, ideally before 3 years of age, underscores the value of developing even more automated AI approaches, due to their potentials for scale, reach, and privacy. We present the first systematic evaluation of multimodal LLMs as direct replacements for human annotation in AI-based autism detection. Evaluating seven Gemini model variants (1.5-2.5 series) on 50 YouTube videos shows clear generational progression: version 1.5 models achieve 72-80% accuracy, version 2.0 models reach 80%, and version 2.5 models attain 85-90%, with the best model (2.5 Pro) achieving 89.6% classification accuracy using validated autism detection AI models (LR5)-comparable to the 88% clinical baseline and approaching crowdworker performance of 92-98%. The 24% improvement across two generations suggests the gap is closing. LLMs demonstrate high within-model consistency versus moderate human agreement, with distinct assessment strategies: LLMs focus on language/behavioral markers, crowdworkers prioritize social-emotional engagement, clinicians balance both. While LLMs have yet to match the highest-performing subset of human annotators in their ability to extract behavioral features that are useful for human-in-the-loop AI diagnosis, their rapid improvement and advantages in consistency, scalability, cost, and privacy position them as potentially viable alternatives for aiding diagnostic processes in the future.

**ИИ:** ? · обе модели · другое · Gemini annotates autism behavioural features compared with crowdworker and clinician annotators, but the input is video rather than text.

**Решение:** =

---

### 1031 · R7486

**Can Conversational AI Counsel for Change? A Theory-Driven Approach to Supporting Dietary Intentions in Ambivalent Individuals**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2511.02428

Adherence to healthy diets reduces chronic illness risk, yet rates remain low. Large Language Models (LLMs) are increasingly used for health communication but often struggle to engage individuals with ambivalent intentions at a pivotal stage of the Transtheoretical Model (TTM). We developed CounselLLM, an open-source model enhanced through persona design and few-shot, domain-specific prompts grounded in TTM and Motivational Interviewing (MI). In controlled evaluations, CounselLLM showed stronger use of TTM subprocesses and MI affirmations than human counselors, with comparable linguistic robustness but expressed in more concrete terms. A user study then tested CounselLLM in an interactive counseling setting against a baseline system. While knowledge and perceptions did not change, participants' intentions for immediate dietary change increased significantly after interacting with CounselLLM. Participants also rated it as easy to use, understandable, and supportive. These findings suggest theory-driven LLMs can effectively engage ambivalent individuals and provide a scalable approach to digital counseling.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly an LLM counseling-generation study; MI/TTM coding of responses may use an LLM coder checked against humans, which is unclear.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Develops a counseling LLM and tests it in a user study; no LLM coding of texts validated against human coders is described.)

**Решение:** -

---

### 1032 · R7490

**Deductively coding psychosocial autopsy interview data using a few-shot learning large language model.**

2025 · Frontiers in public health · journal article, journalarticle, review · eng · https://doi.org/10.3389/fpubh.2025.1512537

Background: Psychosocial autopsy is a retrospective study of suicide, aimed to identify emerging themes and psychosocial risk factors. It typically relies heavily on qualitative data from interviews or medical documentation. However, qualitative research has often been scrutinized for being prone to bias and is notoriously time- and cost-intensive. Therefore, the current study aimed to investigate if a Large Language Model (LLM) can be feasibly integrated with qualitative research procedures, by evaluating the performance of the model in deductively coding and coherently summarizing interview data obtained in a psychosocial autopsy. Methods: Data from 38 semi-structured interviews conducted with individuals bereaved by the suicide of a loved one was deductively coded by qualitative researchers and a server-installed LLAMA3 large language model. The model performance was evaluated in three tasks: (1) binary classification of coded segments, (2) independent classification using a sliding window approach, and (3) summarization of coded data. Intercoder agreement scores were calculated using Cohen's Kappa, and the LLM's summaries were qualitatively assessed using the Constant Comparative Method. Results: The results showed that the LLM achieved substantial agreement with the researchers for the binary classification (accuracy: 0.84) and the sliding window task (accuracy: 0.67). The performance had large variability across codes. LLM summaries were typically rich enough for subsequent analysis by the researcher, with around 80% of the summaries being rated independently by two researchers as 'adequate' or 'good.' Emerging themes in the qualitative assessment of the summaries included unsolicited elaboration and hallucination. Conclusion: State-of-the-art LLMs show great potential to support researchers in deductively coding complex interview data, which would alleviate the investment of time and resources. Integrating models with qualitative research procedures can facilitate near real-time monitoring. Based on the findings, we recommend a collaborative model, whereby the LLM's deductive coding is complemented by review, inductive coding and further interpretation by a researcher. Future research may aim to replicate the findings in different contexts and evaluate models with a larger context size.

**ИИ:** + · обе модели · кодирование по кодбуку · LLaMA3 deductively coded psychosocial autopsy interviews about suicide; agreement with human researchers was reported as Cohen's kappa and accuracy.

**Решение:** =

---

### 1033 · R7497

**Large Language Models for Pathos Mining**

2025 · Argumentation library · book-chapter · en · https://doi.org/10.1007/978-3-032-06332-8_9

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLMs detecting emotional appeals (pathos) in argumentative text might be compared with human annotations, but the construct is borderline.

**Решение:** =

---

### 1034 · R7516

**A SYSTEMATIC LITERATURE REVIEW OF EVALUATING THE ACCURACY OF NVIVO, R, AND LARGE LANGUAGE MODELS IN THEMATIC ANALYSIS OF INTERVIEW DATA: A COMPARATIVE STUDY**

2025 · Third Desk Research Conference · conference, review · https://doi.org/10.64920/drc2025031

In response to the growing integration of computational tools in qualitative research, this study presents a systematic comparison of three widely adopted approaches for conducting thematic analysis on qualitative interview data: NVivo (proprietary), R-based text analysis packages (open source), and Large Language Models (LLMs) such as ChatGPT. Thematic analysis remains a cornerstone of qualitative inquiry, and with increasing reliance on automated methods, it is essential to understand how accurately these tools replicate the depth, nuance, and contextual sensitivity of human-coded analysis. Interview transcripts, selected for their richness in expression and detail, provide a robust dataset for comparative evaluation. Manual thematic coding, grounded in Braun and Clarke's six-phase framework, is employed as the gold standard. Each tool then independently analyzes the same dataset to extract themes and patterns. The resulting outputs are assessed using established metrics such as Precision, Recall, F1 Score, and Thematic Overlap, which quantitatively capture the degree of alignment with the human-coded reference. This evaluation aims not only to identify the comparative strengths and weaknesses of each tool but also to highlight the contexts in which specific tools may be most effective or limited. Moreover, the study delves into the potential of hybrid approaches that combine human judgment with machine-driven analysis to improve both accuracy and efficiency. By systematically mapping the capabilities and limitations of these tools, the research provides valuable, evidence-based guidance for researchers and practitioners navigating the evolving domain of AI-supported qualitative analysis. The findings are intended to support more informed tool selection and promote the thoughtful integration of computational methods into human-centered research workflows.

**ИИ:** разошлись — Opus ? (другое: Labelled a review, but the abstract describes comparing an LLM with human thematic coding of interviews. It is unclear whether the comparison is theme-level only or whether the construct is psychological.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Compares tool-extracted themes (NVivo, R, LLM) with human themes in generic interview data; theme-level overlap, no psychological construct coding of the same units.)

**Решение:** -

---

### 1035 · R7538

**Advancing AI-driven thematic analysis in qualitative research: a comparative study of nine generative models on Cutaneous Leishmaniasis data.**

2025 · BMC medical informatics and decision making · collection/collection, comparative study, research-article · eng · https://doi.org/10.1186/s12911-025-02961-5

Abstract Background As part of qualitative research, the thematic analysis is time-consuming and technical. The rise of generative artificial intelligence (A.I.), especially large language models, has brought hope in enhancing and partly automating thematic analysis. Methods The study assessed the relative efficacy of conventional against AI-assisted thematic analysis when investigating the psychosocial impact of cutaneous leishmaniasis (CL) scars. Four hundred forty-eight participant responses from a core study were analysed comparing nine A.I. generative models: Llama 3.1 405B, Claude 3.5 Sonnet, NotebookLM, Gemini 1.5 Advanced Ultra, ChatGPT o1-Pro, ChatGPT o1, GrokV2, DeepSeekV3, Gemini 2.0 Advanced with manual expert analysis. Jamovi software maintained methodological rigour through Cohen’s Kappa coefficient calculations for concordance assessment and similarity measurement via Python using Jaccard index computations. Results Advanced A.I. models showed impressive congruence with reference standards; some even had perfect concordance (Jaccard index = 1.00). Gender-specific analyses demonstrated consistent performance across subgroups, allowing a nuanced understanding of psychosocial consequences. The grounded theory process developed the framework for the fragile circle of vulnerabilities that incorporated new insights into CL-related psychosocial complexity while establishing novel dimensions. Conclusions This study shows how A.I. can be incorporated in qualitative research methodology, particularly in complex psychosocial analysis. Consequently, the A.I. deep learning models proved to be highly efficient and accurate. These findings imply that the future directions for qualitative research methodology should focus on maintaining analytical rigour through the utilisation of technology using a combination of A.I. capabilities and human expertise following standardised future checklist of reporting full process transparency.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Nine LLMs did thematic analysis of 448 psychosocial responses, scored against expert analysis with kappa/Jaccard; unclear whether response-level coding or theme-level only.); Sonnet + (кодирование по кодбуку: Nine LLMs thematically coded 448 open responses on psychosocial impact; Cohen's kappa and Jaccard versus manual expert analysis.)

**Решение:** +

---

### 1036 · R7572

**Comparison of Human and Large Language Model Coded Themes in Patient Comments About Their Care Experience**

2025 · Texas Digital Library (University of Texas) · dataset/survey data, clinical data, dataset · https://doi.org/10.18738/t8/lbeddu

The themes that arise in patient verbatim comments regarding experience can guide clinician and unit improvements, but traditional qualitative analysis is time-consuming. This study evaluated whether large language models (LLMs) can efficiently identify themes in patient feedback. We analyzed 77 transcribed comments from post-visit telephone surveys in musculoskeletal specialty care grouped by rating: 0, 1-2, and 3-6 on a 0 to 10-point scale. An LLM first generated themes, after which human coders refined and applied these themes to all comments. We compared the themes and theme counts generated by an LLM and by humans using the LLM as a tool. The LLM themes and subthemes that varied by rating category. Human coders consolidated these into three consistent themes across rating categories: trust and relationship, lack of direction, and logistics. The lowest recommendation rating was dominated by relationship concerns, whereas mid-range scores mostly addressed logistical issues. LLM theme counts approximated human counts across groups, suggesting that LLMs can streamline qualitative review while preserving human judgment in refinement.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM and humans coded themes in patient comments and theme counts were compared; unclear if per-comment agreement exists or if construct is psychological.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Compares LLM- and human-generated themes and theme counts in patient experience comments, not unit-level coding agreement; construct is care experience, not clearly psychological.)

**Решение:** -

---

### 1037 · R7574

**Assessing Critical Thinking through a Multi-Agent LLM-Based Debate Chatbot**

2025 · CHI Extended Abstracts · book, journalarticle · https://doi.org/10.1145/3706599.3721207

Critical thinking (CT) is a crucial competency in education, requiring structured and reliable assessment methods. This study introduces an LLM-based debate chatbot framework designed to evaluate CT by integrating argument construction and analytical reasoning (i.e., argumentation skills) and qualitative reasoning criteria (i.e., intellectual standards). Two assessment models were developed: the Single-Agent (SA) model and the Multi-Agent (MA) model. The MA model achieved an Intraclass Correlation Coefficient (ICC) of 0.78 and 97.37 % Agreement within ±1 with human evaluators, indicating strong alignment with human assessment results. By independently assessing argumentation skills and intellectual standards, the MA model more effectively mirrored the nuanced assessment patterns observed in human assessments. These findings highlight the potential of multi-agent approaches in CT assessment, bridging structured assessment models with expert-like evaluative reasoning. This study contributes to the development of LLM-driven CT assessment frameworks, offering a scalable foundation for integrating diverse evaluative criteria in automated educational assessment.

**ИИ:** ? · обе модели · неясен конструкт · LLM scores critical thinking in debate text, with ICC against human raters; unclear if this educational competency counts as a psychological construct.

**Решение:** =

---

### 1038 · R7575

**Are Today's LLMs Ready to Explain Well-Being Concepts?**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2508.03990

Well-being encompasses mental, physical, and social dimensions essential to personal growth and informed life decisions. As individuals increasingly consult Large Language Models (LLMs) to understand well-being, a key challenge emerges: Can LLMs generate explanations that are not only accurate but also tailored to diverse audiences? High-quality explanations require both factual correctness and the ability to meet the expectations of users with varying expertise. In this work, we construct a large-scale dataset comprising 43,880 explanations of 2,194 well-being concepts, generated by ten diverse LLMs. We introduce a principle-guided LLM-as-a-judge evaluation framework, employing dual judges to assess explanation quality. Furthermore, we show that fine-tuning an open-source LLM using Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) can significantly enhance the quality of generated explanations. Our results reveal: (1) The proposed LLM judges align well with human evaluations; (2) explanation quality varies significantly across models, audiences, and categories; and (3) DPO- and SFT-finetuned models outperform their larger counterparts, demonstrating the effectiveness of preference-based learning for specialized explanation tasks. 9 pages, 4 figures, 3 tables

**ИИ:** ? · обе модели · неясен конструкт · LLM judges validated against human ratings, but they rate the quality of explanations of well-being concepts, which may not be a psychological construct.

**Решение:** =

---

### 1039 · R7576

**Comparing large Language models and human annotators in latent content analysis of sentiment, political leaning, emotional intensity and sarcasm.**

2025 · Scientific reports · comparative study, research-article, journal article · eng · https://doi.org/10.1038/s41598-025-96508-3

In the era of rapid digital communication, vast amounts of textual data are generated daily, demanding efficient methods for latent content analysis to extract meaningful insights. Large Language Models (LLMs) offer potential for automating this process, yet comprehensive assessments comparing their performance to human annotators across multiple dimensions are lacking. This study evaluates the inter-rater reliability, consistency, and quality of seven state-of-the-art LLMs. These include variants of OpenAI's GPT-4, Gemini, Llama-3.1-70B, and Mixtral 8 × 7B. Their performance is compared to human annotators in analyzing sentiment, political leaning, emotional intensity, and sarcasm detection. The study involved 33 human annotators and eight LLM variants assessing 100 curated textual items. This resulted in 3,300 human and 19,200 LLM annotations. LLM performance was also evaluated across three-time points to measure temporal consistency. The results reveal that both humans and most LLMs exhibit high inter-rater reliability in sentiment analysis and political leaning assessments, with LLMs demonstrating higher reliability than humans. In emotional intensity, LLMs displayed higher reliability compared to humans, though humans rated emotional intensity significantly higher. Both groups struggled with sarcasm detection, evidenced by low reliability. Most LLMs showed excellent temporal consistency across all dimensions, indicating stable performance over time. This research concludes that LLMs, especially GPT-4, can effectively replicate human analysis in sentiment and political leaning, although human expertise remains essential for emotional intensity interpretation. The findings demonstrate the potential of LLMs for consistent and high-quality performance in certain areas of latent content analysis.

**ИИ:** ? · обе модели · неясен конструкт · LLMs and 33 human annotators rated the same texts; emotional intensity fits the review, but sentiment and political leaning do not, and the texts look generic.

**Решение:** =

---

### 1040 · R7590

**CAN ARTIFICIAL INTELLIGENCE (AI) JUDGE REFLECTION? VALIDITY, RELIABILITY, AND FAIRNESS OF GENERATIVE AI-ASSISTED ASSESSMENT IN POSTGRADUATE HEALTH PROFESSIONS EDUCATION**

2025 · DOAJ (DOAJ: Directory of Open Access Journals) · journalarticle, article, journal-article · en · https://doi.org/10.37762/jgmds.13-1.835

ABSTRACT OBJECTIVES This study aimed to evaluate the role of GenAI in assessing reflective writing among Master of Health Professions Education (MHPE) students by comparing GenAI scores with those of human raters, examining subgroup fairness, exploring stakeholder perceptions, and proposing governance recommendations. METHODOLOGY A sequential mixed-methods study was conducted in an MHPE programme at Khyber Medical University, Pakistan. In Phase I, 120 Gibbs-structured reflections from 40 students were scored by three trained faculty raters and a GPT-4-level GenAI model using an eight-dimensional rubric. Inter-rater reliability, AI-human agreement, and subgroup differences by gender, discipline, and career stage were examined. In Phase II, semi-structured interviews were conducted with 10 MHPE students and the three faculty raters. Data were analysed using reflexive thematic analysis and integrated with quantitative results. RESULTS Human scoring demonstrated strong reliability (ICC = .82). GenAI showed high alignment with human ratings for surface-level dimensions such as clarity and language mechanics (r = .81-.84), but only modest agreement for higher-order reflective constructs including feelings, analysis, and conclusion (r = .49-.59). Exploratory subgroup analyses revealed no statistically significant differences in AI-human discrepancies. However, qualitative accounts highlighted concerns about linguistic and cultural fairness. Participants valued AI for efficient, organised feedback but consistently emphasised its inability to interpret emotional nuance, contextual meaning, or developmental trajectories. Faculty stressed the irreplaceability of human judgment and the need for transparent governance and fairness monitoring. CONCLUSION GenAI can effectively support the assessment of structural and linguistic aspects of reflective writing but remains limited in evaluating deeper reflective constructs central to postgraduate learning. Ethical and educationally sound integration requires hybrid human-AI approaches in which AI provides formative support while human evaluators retain primary responsibility for interpretive judgment, fairness oversight, and professional mentorship. GenAI should supplement, not replace, human assessment of reflective writing.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 and faculty scored reflective writing on the same rubric. It's unclear whether educational reflection counts as a psychological construct or as essay grading.

**Решение:** =

---

### 1041 · R7599

**SafetyScan: Validating a Software Tool for Human-on-the-Loop Oversight of GenAI Behavioral Counseling Conversations (Preprint)**

2025 · preprint · en · https://doi.org/10.2196/preprints.76614

BACKGROUND As generative AI (GenAI) is increasingly used in behavior interventions, ensuring the safety and appropriateness of AI-generated statements and detecting high-risk patient disclosures are critical. OBJECTIVE We developed and tested SafetyScan, a large language model (LLM)-assisted transcript scanner designed to support human-on-the-loop (HOTL) oversight by identifying and categorizing potentially concerning content in counseling encounters. METHODS To validate SafetyScan, we analyzed transcripts from a completed study where a GenAI conducted motivational interviewing with young adults reporting hazardous alcohol consumption. We analyzed 37 transcripts previously confirmed by human raters to contain no concerning content (serving as negative controls). We then created 37 positive test cases by inserting one randomly generated concerning statement into each of these original transcripts, drawn from five predefined categories: client safety (e.g., suicidal ideation), unsupported treatment recommendation, inappropriate counselor comment, discriminatory language, and invented client history. SafetyScan analyzed all 74 transcripts. RESULTS SafetyScan demonstrated strong performance with a sensitivity of 0.92, specificity of 1.00, and an F1 score of 0.96. It correctly identified 34 of the 37 inserted concerning statements (true positives) and correctly cleared all 37 benign transcripts (true negatives), resulting in 3 false negatives and 0 false positives. The three missed statements were two inappropriate counselor responses and one unsupported treatment recommendation, none judged as critical safety failures. CONCLUSIONS These findings suggest SafetyScan offers a feasible and accurate solution for assisting human oversight of GenAI-driven counseling, supporting safer deployment of conversational AI systems in clinical and research contexts. CLINICALTRIAL NA

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · An LLM flags safety concerns in MI counseling transcripts. The reference mixes human-confirmed negative transcripts with synthetically inserted positives, not human coding of the same units.

**Решение:** =

---

### 1042 · R7602

**The Structure of Major Life Transitions Among Older Suicide Decedents: An Application of Large Language Models**

2025 · Innovation in Aging · journalarticle, article, journal-article · en · https://doi.org/10.1093/geroni/igaf122.1215

Abstract The role of life events in shaping suicide risk for older adults is unclear. Structure and meaning of events are interconnected: structure shapes the relationship between event elements (e.g., timing), with meaning emerging through their dynamic interactions. Large language models (LLM) provide an opportunity to analyze textual data at scale, but they have not yet been widely used to understand the contributing circumstances of suicide. In this study, we applied LLMs to narrative texts from the National Violent Death Reporting System (2003-2022), a nationwide registry of suicide deaths, to (1) identify salient events in the lives of suicide decedents aged 50 + (n = 164,240), (2) classify aspects of the structure of these events (e.g., timing, sequence, expectedness), and (3) explore variation by age. Mean age of decedents was 63 years, 24% were female, 88% were non-Hispanic White; 54% did not have a known mental health problem at the time of their death. Most narratives described sequences of life events involving interlinked health or family problems that often escalated days before suicide (e.g., mobility loss after a recent surgery); less frequently, narratives mentioned isolated events, referring to financial or relationship crises. For decedents aged 65+, events often involved legal issues or relationship loss (e.g., widowhood), while those aged &amp;lt;65 events typically related to employment or relationship discord. Preliminary analyses demonstrate the feasibility of identifying structural elements of life events using LLMs; next steps will include refining prompts to improve classification of complex transitions from these texts.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM classifies life events in suicide decedent narratives (NVDRS); the abstract doesn't say whether results were validated against human coding.

**Решение:** =

---

### 1043 · R7603

**Factors Associated with Abusive Head Trauma in Young Children Presenting to Emergency Medical Services Using a Large Language Model.**

2025 · Prehospital emergency care · journal article, med, journalarticle · eng · https://doi.org/10.1080/10903127.2025.2451209

Abstract Objectives Abusive head trauma (AHT) is a leading cause of death in young children. Analyses of patient characteristics presenting to Emergency Medical Services (EMS) are often limited to structured data fields. Artificial Intelligence (AI) and Large Language Models (LLM) may identify rare presentations like AHT through factors not found in structured data. Our goal was to apply AI and LLM to EMS narrative documentation of young children to detect AHT. Methods This is a retrospective cohort study of EMS transports of children <36 months of age with a diagnosis of head injury from the 2018–2019 ESO Research Data Collaborative. Non-abusive closed head injury (NA-CHI) was distinguished from AHT and child maltreatment (AHT-CAN) through 2 expert reviewers; kappa statistic (k) assessed inter-rater reliability. A Natural Language Processing (NLP) framework using an LLM augmented with expert derived n-grams was developed to identify AHT-CAN. We compared test characteristics (sensitivity, specificity, negative predictive value (NPV)) between this NLP framework to a Generative Pretrained Transformer (GPT) or n-grams only models to detect AHT-CAN. Association of specific word tokens with AHT-CAN was analyzed using Pearson’s chi-square. Area Under the Receiver Operator Curve (AUROC) and Area Under the Precision-Recall Curve (AUPRC) are also reported. Results There were 1082 encounters in our cohort; 1030 (95.2%) NA-CHI and 52 (4.8%) AHT-CAN. Inter-rater agreement was substantial (k = 0.71). The augmented NLP framework had a specificity and sensitivity of 72.4% and 92.3%, respectively with a NPV of 99.5%. In comparison, the GPT model had a sensitivity of 69.2%, specificity of 97.1% and NPV of 98.4% and n-grams alone had a sensitivity of 53.8%, specificity of 62.0%, NPV of 96.4%. AUROC was 0.91 and AUPRC was 0.52. A total of 44 n-grams and bi-grams were positively associated with AHT-CAN including “domestic,” “various,” “bruise,” “cheek,” “multiple,” “doa,” “not respond,” “see EMS.” Conclusions AI and LLMs have high sensitivity and specificity to detect AHT-CAN in EMS free-text narratives. Words associated with physical signs of trauma are strongly associated with AHT-CAN. LLMs augmented with a list of n-grams may help EMS identify signs of trauma that aid in the detection of AHT in young children.

**ИИ:** ? · обе модели · неясен конструкт · GPT detects abusive head trauma/maltreatment in EMS narratives against expert labels; unclear whether child-abuse detection counts as a psychological construct.

**Решение:** =

---

### 1044 · R7606

**Valence Ratings of Lemmas Generated by a Large Language Model Simulating Multiple Human Responses**

2025 · World Congress on Medical Physics and Biomedical Engineering, September 7 - 12, 2009, Munich, Germany · conference-paper · en · https://doi.org/10.1007/978-3-031-94934-0_66

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM valence (emotion) ratings of words, possibly compared with human affective norms; whether single words count as text is unclear.

**Решение:** =

---

### 1045 · R7620

**Observer-Independent Assessment of Content Overlap in Mental Health Questionnaires: Large Language Model-Based Study.**

2025 · JMIR AI · journal article, journalarticle, text/journal article · eng · https://doi.org/10.2196/79868

JMIR AI 4, e79868 - e79868 (2025). doi:10.2196/79868 Background: Mental disorders are frequently evaluated using questionnaires, which have been developed over the past decades for the assessment of different conditions. Despite the rigorous validation of these tools, high levels of content divergence have been reported for questionnaires measuring the same construct of psychopathology. Previous studies that examined the content overlap required manual symptom labeling, which is observer-dependent and time-consuming.Objective: In this study, we used large language models (LLMs) to analyze content overlap of mental health questionnaires in an observer-independent way and compare our results with clinical expertise.Methods: We analyzed questionnaires from a range of mental health conditions, including adult depression (n=7), childhood depression (n=15), clinical high risk for psychosis (CHR-P; n=11), mania (n=7), obsessive-compulsive disorder (n=7), and sleep disorder (n=12). Two different LLM-based approaches were tested. First, we used sentence Bidirectional Encoder Representations from Transformers (sBERT) to derive numerical representations (embeddings) for each questionnaire item, which were then clustered using k-means to group semantically similar symptoms. Second, questionnaire items were prompted to a Generative Pretrained Transformer to identify underlying symptom clusters. Clustering results were compared to a manual categorization by experts using the adjusted rand index. Further, we assessed the content overlap within each diagnostic domain based on LLM-derived clusters.Results: We observed varying degrees of similarity between expert-based and LLM-based clustering across diagnostic domains. Overall, agreement between experts was higher than between experts and LLMs. Among the 2 LLM approaches, GPT showed greater alignment with expert ratings than sBERT, ranging from weak to strong similarity depending on the diagnostic domain. Using GPT-based clustering of questionnaire items to assess the content overlap within each diagnostic domain revealed a weak (CHR-P: 0.344) to moderate (adult depression: 0.574; childhood depression: 0.433; mania: 0.419; obsessive-compulsive disorder [OCD]: 0.450; sleep disorder: 0.445) content overlap of questionnaires. Compared to the studies that manually investigated content overlap among these scales, the results of this study exhibited variations, though these were not substantial.Conclusions: These findings demonstrate the feasibility of using LLMs to objectively assess content overlap in diagnostic questionnaires. Notably, the GPT-based approach showed particular promise in aligning with expert-derived symptom structures.Keywords: GPT; content overlap; large language models; questionnaires; sBERT; scales; sentence Bidirectional Encoder Representations from Transformers; symptom overlap. Published by JMIR Publications, Toronto, Ont.

**ИИ:** ? · обе модели · неясен конструкт · GPT sorted questionnaire items into symptom clusters and was compared with expert categorization (ARI); unclear whether item text counts as psychological text.

**Решение:** =

---

### 1046 · R7628

**Tailored Emotional LLM-Supporter: Enhancing Cultural Sensitivity**

2025 · TUbilio (Technical University of Darmstadt) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2508.07902

Large language models (LLMs) show promise in offering emotional support and generating empathetic responses for individuals in distress, but their ability to deliver culturally sensitive support remains underexplored due to a lack of resources. In this work, we introduce CultureCare, the first dataset designed for this task, spanning four cultures and including 1729 distress messages, 1523 cultural signals, and 1041 support strategies with fine-grained emotional and cultural annotations. Leveraging CultureCare, we (i) develop and test four adaptation strategies for guiding three state-of-the-art LLMs toward culturally sensitive responses; (ii) conduct comprehensive evaluations using LLM-as-a-Judge, in-culture human annotators, and clinical psychologists; (iii) show that adapted LLMs outperform anonymous online peer responses, and that simple cultural role-play is insufficient for cultural sensitivity; and (iv) explore the application of LLMs in clinical training, where experts highlight their potential in fostering cultural competence in novice therapists. Joint first authors; EACL

**ИИ:** разошлись — Opus + (LLM-судья: An LLM judge, in-culture annotators and clinical psychologists all evaluate the same emotional-support responses, so judge–human agreement can likely be compared.); Sonnet ? (неясно, сравнивали ли с людьми: Mainly response generation, but LLM-as-a-Judge is used alongside human and clinician ratings of support responses; LLM–human agreement may be reported in the full text.)

**Решение:** +

---

### 1047 · R7650

**Evaluating the Feasibility, Usability, and Promise of a Parent Management Training using a Generative Artificial Intelligence Platform**

2025 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5176475

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: No abstract; the title describes a feasibility and usability study of a parent training delivered by generative AI, with no sign of LLM-versus-human coding.); Sonnet ? (нет аннотации: No abstract; title suggests a generative AI parent training feasibility study, likely generation-focused, but human coding or rating of the texts can't be ruled out.)

**Решение:** ?

---

### 1048 · R7658

**Navigating Life Transitions as a Strategy for Preventing Late-Life Suicide**

2025 · Innovation in Aging · journalarticle, article · en · https://doi.org/10.1093/geroni/igaf122.1212

Abstract Older adults have higher rates of suicide than the general population. Life transitions and changes unique to aging may contribute to this increased risk of suicide. This symposium will feature research examining the identification of suicide risk factors and prevention of suicide in older adults, with a particular focus on the role of changes in functioning and health. First, Catherine Ju will present research investigating how strategies older adults might use to compensate for functional impairment (e.g., seeking help) might play a role in risk for suicidal ideation among people who highly value their own autonomy. Second, Dr. Kimberly Van Orden will present results of a clinical trial testing whether an intervention addressing barriers to social connection (produced by functional impairment and health problems) results in reductions in suicidal ideation as measured via ecological momentary assessment. Last, Dr. Briana Mezuk will describe research employing large language models to identify and characterize the structure of life transitions of older suicide decedents using the National Violent Death Reporting System. Dr. Amy Fiske will serve as discussant.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Symposium abstract; one talk uses LLMs to code life transitions in NVDRS suicide narratives, but whether this was validated against human coding is unclear.

**Решение:** =

---

### 1049 · R7664

**Utilizing AI-Powered Thematic Analysis: Methodology, Implementation, and Lessons Learned.**

2025 · Cureus · journal article, journalarticle, article · eng · https://doi.org/10.7759/cureus.85338

Artificial intelligence (AI) has the potential to transform healthcare, medical education, and research. Large language models (LLMs) have gained attention for their ability to improve qualitative research by automating data analysis, coding, and thematic interpretation. While prior research evaluates LLMs' performance in qualitative studies, clear guidelines on their implementation remain scarce. This manuscript offers detailed methods with instructions and prompts for using LLMs in qualitative analysis. It provides a clear, step-by-step, practical approach. We developed a customized generative pre-trained transformer (Custom-GPT) based on Braun and Clarke's six-step thematic analysis framework. The performance of the model was evaluated across three datasets, comparing its outputs with manually generated codes and themes. Triangulation was conducted using Google's NotebookLM. Across the three datasets, the model generated consistent thematic structures that aligned closely with manual coding. However, slight variability in responses, lack of AI decision-making explanations, and requiring repeated prompting during the process were the main challenges. Additional human interventions were required between steps to refine outputs and ensure methodological integrity. LLMs offer promising opportunities to enhance qualitative thematic analysis. However, their limitations emphasize the necessity of human oversight throughout the process. This report highlights the importance of integrating AI tools responsibly, emphasizing methodological rigor, and developing clear guidelines for AI-assisted qualitative research. Future research should explore ethical frameworks, domain-specific LLMs, and advanced prompt engineering techniques to optimize AI's role in qualitative analysis.

**ИИ:** разошлись — Opus ? (неясен конструкт: Custom-GPT thematic analysis compared with manual codes/themes on three datasets; unclear if psychological content or unit-level coding agreement.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Methods report on Custom-GPT thematic analysis comparing LLM-generated codes and themes with manual ones. It has no clear psychological construct and no unit-level coding agreement.)

**Решение:** -

---

### 1050 · R7667

**From Code to Insight: How LLMs Help and Hinder Qualitative Research**

2025 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-031-99264-3_4

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests LLM-assisted qualitative coding, possibly compared with humans, but the domain and design are unclear.

**Решение:** =
