# Ручной отбор, часть 4

Ручной отбор, часть 4: записи 451–600 из 1000. Эти записи вы размечаете сами, вместо проходов ИИ (deviations.md, D3); это случайные 1000 записей из тех, что ИИ ещё не разметил (зерно 20261024). **Меток ИИ здесь нет и не будет.** Ваше решение окончательное: «+» и «?» идут на полный текст. Размечайте в любом порядке и в несколько заходов.

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

### 451 · R11382

**Incorporating Word Count Information into Depression Risk Summary Generation: INF@UoS CLPsych 2024 Submission**

2024 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, conference-paper · en · https://doi.org/10.18653/v1/2024.clpsych-1.19

Large language model classifiers do not directly offer transparency: it is not clear why one class is chosen over another. In this work, summaries explaining the suicide risk level assigned using a fine-tuned mental-roberta-base model are generated from key phrases extracted using SHAP explainability using Mistral-7B. The training data for the classifier consists of all Reddit posts of a user in the University of Maryland Reddit Suicidality Dataset, Version 2, with their suicide risk labels along with selected features extracted from each post by the Linguistic Inquiry and Word Count (LIWC-22) tool. The resulting model is used to make predictions regarding risk on each post of the users in the evaluation set of the CLPsych 2024 shared task, with a SHAP explainer used to identify the phrases contributing to the top scoring, correct and severe risk categories. Some basic stoplisting is applied to the extracted phrases, along with length based filtering, and a locally run version of Mistral-7B-Instruct-v0.1 is used to create summaries from the highest value (based on SHAP) phrases.

**Решение:** -6 CLPsych 2024 Mistral-7B generates explanation summaries from SHAP, prediction done by RoBERTa

---

### 452 · R12542

**ChatGPT for Mental Health Applications: A study on biases**

2023 · International Conference on AI-ML Systems (AIMLSystems) · journalarticle, book, conference-paper · en · https://doi.org/10.1145/3639856.3639894

Suicide is a serious global issue taking 800,000 lives every year. AI-assisted early detection of suicide risk and stress levels using a user’s activity on online forums and social media websites has shown great promise previously. In addition to this, emerging large language models have shown massive potential to provide state-of-the-art-performance for downstream tasks like text classification. Therefore, we attempt to apply one such large language model, GPT3.5 turbo to mental health applications with 3 datasets spanning suicide risk severity and stress presence classification. We also study the inherent demographic biases induced in these models as a result of polluted pretraining data and find that the model consistently estimates the mental health status of young females between the ages of 18 and 30 years best.

**Решение:** + T3 GPT-3.5 suicide risk severity and stress classification across 3 benchmark datasets

---

### 453 · R2998

**How do practitioners incorporate requirements and design decisions in LLM-assisted code generation?**

2026 · Gesellschaft für Informatik (GI) · other/conference paper, text/text/conference paper, article · en · https://doi.org/10.18420/se2026_29

This paper originally appeared in the IEEE 33rd International Requirements Engineering Conference (RE) [UKV25]. In an interview study with 18 participants from 14 companies, we examined how practitioners incorporate information from requirements and software design artifacts during LLM-assisted development. Based on our findings, we propose a theory that explains the processes developers employ, the artifacts they rely on, and the collaboration patterns that emerge. Our results indicate that requirements, as typically documented, are too abstract for direct input into LLMs. Instead, they must be manually decomposed into programming tasks and enriched with design decisions and explicit architectural constraints. Otherwise, LLMs tend to produce solutions requiring substantial modifications. We also identify three modes of LLM interaction in practice: technical exploration (to investigate solution approaches), code generation (LLMs produce most of the code, with developers correcting parts), and manual coding (developers program while using LLMs for auto-completion). Our theory is important for contextualizing scientific approaches to automating requirements- and design-centric SE tasks, and for guiding companies on how to integrate LLMs in their software engineering processes.

**Решение:** -4 requirements engineering, software design

---

### 454 · R4288

**Expert evaluation of large language models for patient counseling during recovery after gynecologic and obstetric surgery: a blinded comparative cross-sectional study**

2026 · BMC Surgery · article · en · https://doi.org/10.1186/s12893-026-04197-0

The postoperative period after gynecologic and obstetric surgery generates substantial patient information needs, and large language models (LLMs) are increasingly proposed as tools to help answer patient questions. Their performance in this setting, particularly with respect to safety, remains poorly defined. We evaluated the patient-counseling performance of three LLMs for recovery follow-up after gynecologic and obstetric surgery. In this cross-sectional, observational study, 30 frequently asked patient questions about postoperative recovery were compiled with the input of five experienced surgeons and posed to ChatGPT-5.5 Pro, Claude Opus 4.7, and Gemini 3.1 Pro using a standardized prompt. The responses, with model identity concealed and presented in randomized order, were independently scored by 30 specialist obstetricians and gynecologists on a 5-point Likert scale for accuracy, comprehensiveness, understandability, safety, and appropriateness. The presence of appropriate safety warnings, response length, and inter-rater agreement were also assessed. With the question as the unit of analysis, scores were compared using repeated-measures analysis of variance with Bonferroni-corrected pairwise comparisons, and a linear mixed-effects model was fitted as a sensitivity analysis; safety-warning rates were compared using the chi-square test. The highest overall mean score was obtained by ChatGPT-5.5 Pro (4.42 ± 0.38), followed by Claude Opus 4.7 (4.31 ± 0.41) and Gemini 3.1 Pro (4.12 ± 0.46) ( p < 0.001; partial eta-squared 0.27). ChatGPT-5.5 Pro and Claude Opus 4.7 performed comparably, with no significant difference between them (mean difference 0.11, 95% CI − 0.02 to 0.24; p = 0.084); both scored significantly higher than Gemini 3.1 Pro (mean difference 0.30, 95% CI 0.18 to 0.43, and 0.19, 95% CI 0.07 to 0.32, respectively). Appropriate safety warnings were most frequent with Claude Opus 4.7 (90.0%), followed by ChatGPT-5.5 Pro (86.7%) and Gemini 3.1 Pro (76.7%). The lowest scores were obtained in the categories of conditions requiring urgent presentation and of bleeding and discharge. Inter-rater agreement was good (intraclass correlation coefficient 0.81) and internal consistency was high (Cronbach’s alpha 0.89). Large language models produced largely accurate and understandable counseling responses after gynecologic and obstetric surgery, but safety and comprehensiveness varied among models and were weakest in high-risk scenarios. These tools may support physician-supervised discharge education but should not replace physician consultation, particularly when urgent presentation may be required.

**Решение:** -4 ob/gyn surgery postoperative discharge questions

---

### 455 · R12316

**Transferrability of Adversarial Attacks from Convolutional Neural Networks to ChatGPT4**

2023 · Fraunhofer-Gesellschaft · other/paper · https://doi.org/10.24406/publica-2166

This research evaluates the ability of adversarial attacks, primarily designed for CNN-based classifiers, to target the multimodal image captioning tasks executed by large multimodal models (LMMs), such as ChatGPT4. The study included several attacks, with a particular emphasis on the Projected Gradient Descent (PGD) attack, considering various parameters, surrogate models, and datasets. Initial but limited experiments support the hypothesis that PGD attacks are transferable to ChatGPT. Subsequently, results demonstrated that PGD attacks could be adaptively transferred to disrupt the normal functioning of ChatGPT. On the other hand, other adversarial attack strategies showed a limited ability to compromise ChatGPT. These findings provide insights into the security vulnerabilities of emerging neural network architectures used for generative AI. Moreover, they underscore the possibility of cost-effectively crafting adversarial examples against novel architectures, necessitating the development of robust defense mechanisms for LMMs in practical applications.

**Решение:** -4 adversarial attacks on CNN classifiers

---

### 456 · R4901

**Blind Spots in AI-Based Longitudinal Psychological Inference: A Single-Subject Validation Study**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.18825306

Generic sentiment analysis tools are widely deployed in mental health applications research and longitudinal text analysis to infer psychological change. Lexicon-based tools (NRC Emotion Lexicon), supervised classifiers (GoEmotions), and large language models (GPT-4) are applied across therapeutic text, social media monitoring, organizational communication, and narrative analysis contexts. However, their construct validity for detecting different types of psychological transformation remains underexamined. This study presents a single-subject longitudinal corpus (n=531 reflective messages across six months) to illustrate a construct–measurement mismatch. The subject self-reported substantial psychological change, corroborated by behavioral indicators and triangulated AI-based thematic coding (inter-rater reliability κ=0.72–0.89). Yet standard sentiment tools showed no systematic signal: lexicon counts increased proportionally to message length expansion, supervised classifiers detected minimal directional change (Cohen's d=0.15–0.26), and LLM-based scoring produced minimal or inconsistent trajectories across temporal bins. We argue that this null result is not a failure of AI per se, but a measurement blind spot: when transformation occurs at the level of narrative meaning rather than valence frequency, generic sentiment tools may remain insensitive. We propose a construct-specific analytic framework emphasizing alignment between psychological target constructs and computational operationalization (59% improvement in identity score, 124% increase in acceptance markers, d=0.82). Implications are discussed for responsible deployment of AI in longitudinal digital health and narrative analysis contexts. These findings have direct implications for NLP tool developers and practitioners deploying sentiment analysis in mental health and longitudinal monitoring contexts. Standard sentiment tools exhibit construct-specific validity limitations, systematically missing cognitive–structural transformations while reliably detecting affective transformations. Researchers and developers should align computational measures with theoretical constructs rather than defaulting to generic sentiment analysis.

**Решение:** ? T1 single-subject validation of AI thematic coding vs human ratings; check full text

---

### 457 · R6952

**Beyond the Algorithm: A Person-Centered Investigation of Engagement, Self-Efficacy, and Anxiety Among Chinese University EFL Learners in the Age of Large Language Models**

2026 · SHS Web of Conferences · journalarticle, conference, conference-paper · fr · https://doi.org/10.1051/shsconf/202623504006

Implementation of large language models (LLMs) in higher education is a paradigm shift in the learning setting of its own right, but the psychological aspect of the change has yet to be theorized properly. This conceptual paper argues for a person-centered approach to understanding how Chinese university students—as English as a Foreign Language (EFL) learners—navigate the cognitive and affective implications of LLM-mediated learning. Moving beyond reductive input-output frameworks of human–machine interaction, this study synthesizes existing literature to examine the interplay among three core psychological constructs: learner engagement, self-efficacy, and foreign language anxiety within AI-mediated contexts. This paper will inform a more responsible, ethically aware, and humanly designed addition of the use of AI in second language learning by highlighting the less obvious, yet contrasting orientations of participation, self-trust, and apprehension that students use to respond to AI. This paper recommends the following based on such findings: 1. The process of pedagogy should be psychologically adjusted to the performance of students. 2. The self-awareness aspect of students plays an essential role in SLA.

**Решение:** -4 LLMs in higher education learning experience

---

### 458 · R5810

**Establishing the Role of Korean Language Teachers in the Age of Artificial Intelligence : A Topic Modeling Analysis of Research Trends**

2026 · International Network for Korean Language and Culture · journalarticle, article · https://doi.org/10.15652/ink.2026.23.1.231

The purpose of this study is twofold: 1) to investigate the changing roles of Korean-language education teachers amid the rapid advancement of artificial intelligence (AI), and 2) to explore the direction of AI-Collaborative Language Education (AICaLE). To this end, 148 master’s and doctoral dissertations and academic journal articles related to AI in Korean-language education, published between 2005 and 2025, were collected and analyzed using Latent Dirichlet Allocation (LDA) topic modeling. The analysis identified four major research topics: “Automated Scoring–based Assessment,” “Digital Competence–based Teaching and Learning Design,” “Writing Feedback Analysis,” and “Conversational AI–based Speaking Practice.” Time-series analysis revealed a paradigm shift in research orientation following the popularization of generative AI in 2023, with the research focus moving from mere tool utilization toward learner interaction and feedback mechanisms. Drawing on these research trends as an empirical foundation derived inductively, this study proposes that Korean-language teachers in the AI era be required to fulfill four distinct roles: “Critical Assessment Auditor,” who verifies the fairness and validity of assessments; “Instructional Designer,” who reconstructs technology to fit educational contexts; “Feedback Mediator,” who supports learners’ affective development and growth; and “Learning Facilitator,” who navigates the ethical boundaries between humans and technology. This study underscores the necessity of a paradigm shift toward AICaLE, in which AI functions not merely as a supplementary tool but also as a complementary partner to teachers, and contributes an evidence-based framework for enhancing Korean-language teachers’ AI literacy and ethical judgment competencies.

**Решение:** -4 Korean language teachers role, pedagogy

---

### 459 · R0676

**An Interpretable Agentic Framework for Multimodal Hate Video Analysis with Explicit Evidence Attribution**

2026 · ACM Web Conference (WWW) · journalarticle, book, conference · https://doi.org/10.1145/3774905.3796488

The proliferation of harmful and toxic content in social media videos poses significant risks to users and online communities. While many state-of-the-art approaches rely on supervised classifiers trained on large benchmark datasets, such models are often evaluated primarily on predictive performance and provide limited transparency for deployment scenarios where explanation and auditability are required. We present an evidence-centric multimodal video analysis system that treats visual, audio, textual, and contextual signals as independent sources of evidence rather than fused features. The system extracts object detections and on-screen text from video frames, speech transcripts from audio, and toxicity scores and named entities from text, while contextual information is obtained from a fixed offline retrieval corpus. All signals are stored in a shared evidence structure and prioritized using a deterministic ranking mechanism that emphasizes semantic contribution, explicitly models cross-modal agreement and conflict, and represents modality absence by marking non-contributory signals as null. Final decisions are produced through a robust orchestration layer that supports a fully deterministic baseline and an optional constrained large language model-based reasoner with fallback guarantees. We evaluate the system on HateMM, ImpliHateVid, and a manually annotated YTHate dataset of 200 real-world YouTube videos. Across all datasets, the system exhibits consistently high recall for hateful content, reflecting a deliberate design choice to reduce false negatives in moderation support settings. Qualitative analysis indicates improved sensitivity to implicit and context-dependent hate, including cases involving visual symbols, late-occurring speech, and cross-modal inconsistencies.

**Решение:** -4 multimodal hate speech video detection

---

### 460 · R7746

**Scalable medication extraction and discontinuation identification from electronic health records using large language models**

2025 · Journal of Clinical Epidemiology · article · en · https://doi.org/10.1016/j.jclinepi.2025.112049

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 medication extraction and discontinuation from EHR

---

### 461 · R6176

**Big5-HCD: A Human-Computer Dialogue Benchmark with Personality Annotations via Semi-Supervised Adaptation**

2026 · INTERNATIONAL CONFERENCE ON MULTIMODAL INTERACTION · book, conference, conference-paper · https://doi.org/10.1145/3776574.3831125

Personality-aware Human-Computer Dialogue (HCD) systems are critical for enabling personalized interactions. However, to the best of our knowledge, existing HCD benchmarks lack explicit personality trait annotations, creating a fundamental barrier to developing robust personality-aware HCD systems. To address this, we introduce Big5-HCD, the first HCD benchmark with fine-grained Big Five personality annotations. This benchmark was derived from RealPersonaChat—a Human-Human Dialogue (HHD) benchmark—through a four-stage semi-supervised pipeline: (1) Construction of a subset based on sampling of HHDs from RealPersonaChat; (2) Construction of role-model HCDs with validation by human evaluators; (3) Construction of a human-calibrated Large Language Model (LLM) evaluation benchmark for automatic adaptation; and (4) Adapation based on LLM evaluators’ consensus for HCD scaling. Experimental evaluations of adaptation effectiveness on Big5-HCD showed high approval rates and tolerance scores from human evaluators, confirming its reliability as a personality-annotated HCD benchmark for developing personality-aware HCD systems. The source code and data are available in: https://github.com/Drew19980118/Big5-HCD.git.

**Решение:** -4 Big5-HCD dialogue benchmark with persona annotations, dialogue generation

---

### 462 · R8510

**S-DAT: A Multilingual, GenAI-Driven Framework for Automated Divergent Thinking Assessment**

2025 · Proceedings of the AAAI/ACM Conference on AI Ethics and Society · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.1609/aies.v8i2.36622

This paper introduces S-DAT (Synthetic-Divergent Association Task), a scalable, multilingual framework for automated assessment of divergent thinking (DT) -a core component of human creativity. Traditional creativity assessments are often labor-intensive, language-specific, and reliant on subjective human ratings, limiting their scalability and cross-cultural applicability. In contrast, S-DAT leverages large language models and advanced multilingual embeddings to compute semantic distance -- a language-agnostic proxy for DT. We evaluate S-DAT across eleven diverse languages, including English, Spanish, German, Russian, Hindi, and Japanese (Kanji, Hiragana, Katakana), demonstrating robust and consistent scoring across linguistic contexts. Unlike prior DAT approaches, the S-DAT shows convergent validity with other DT measures and correct discriminant validity with convergent thinking. This cross-linguistic flexibility allows for more inclusive, global-scale creativity research, addressing key limitations of earlier approaches. S-DAT provides a powerful tool for fairer, more comprehensive evaluation of cognitive flexibility in diverse populations and can be freely assessed online: https://sdat.iol.zib.de/.

**Решение:** + T2 S-DAT: multilingual GenAI framework for automated Divergent Thinking Assessment

---

### 463 · R7604

**Leveraging on large language model to classify sentences: a case study applying STAGES scoring methodology for sentence completion test on ego development.**

2025 · Frontiers in psychology · journal article, journalarticle, article · eng · https://doi.org/10.3389/fpsyg.2025.1488102

Introduction: The emergence of artificial intelligence and the widespread availability of large language model open the door to text analysis at scale leveraging on complex classification instructions. This case study explores the possibility of using available large language models to measure ego development at scale and establish a methodology that can be applied to other classification instructions. Ego consists of the traits that influence how a person perceives and engages with the world, while ego development is a crucial aspect of adult personality growth, influencing behaviors and decisions in both personal and professional contexts. Accurate assessments of ego development stages are vital for creating effective strategies in organizational psychology and corporate analytics. Methods: This case study investigates the agreement between expert and automated classifications of ego development stages, aiming to evaluate the potential of automation in this domain leveraging artificial intelligence and large language models. Cohen's kappa statistic has been used to measure the agreement between classifications made by experts and those generated by an automated process leveraging large language models. Results: The comparison between the scoring of experts and large language models yielded a weighted Kappa value of 0.779, indicating a substantial level of agreement that is statistically meaningful and unlikely to be due to chance. Discussion: While this suggests valuable scoring that leverages large language models, it also highlights the opportunity for further refinement to closely match expert assessments. We observed low variability in aggregated values, demonstrating that the automated process functions effectively at scale. The robustness of aggregated data is particularly evident when calculating ego development scores for individuals, groups, corporate units, and entire corporations. This capability underscores the utility of the automated system for high-level evaluations and decision-making leveraging on a solid indicator. While the classification system developed in this case study shows promise, targeted enhancements may help to achieve a level of accuracy and reliability that improves alignment with experts' evaluations for single sentences. The methodology developed in this case study appears to be useful to support other evaluations at scale that leverage large language models using other maps of classifications.

**Решение:** -4 sentence classification in academic texts

---

### 464 · R6901

**Exploring the Use of LLMs for Assessing Creativity in Student Programming Artifacts**

2026 · ACM Technical Symposium on Computer Science Education (SIGCSE) · journalarticle, book, conference · https://doi.org/10.1145/3770761.3777335

Creativity is a critical learning outcome in K–12 computer science, yet assessing it at scale remains challenging. Human-scored approaches, such as the Consensual Assessment Technique (CAT), are resource-intensive and prone to rater variability. Leveraging advances in large language models (LLMs), this study investigates whether GPT-4o can reliably assess creativity in student-generated code. We collected 383 flow-based music programs from 194 upper-elementary students (ages 10–12) between 2022 and 2024. Each artifact was rated by five human experts across four dimensions: originality, complexity, efficiency, and emotional expressiveness. We evaluated three prompting strategies: zero-shot, few-shot with theory-driven exemplars (ECD), and few-shot with human-selected examples. Among them, the ECD-based few-shot prompting yielded the best performance, achieving the lowest mean absolute error (MAE = 0.582) and highest agreement within ±1.0 of human scores (82.4%). Zero-shot prompting, while slightly less accurate, achieved the highest correlation with human scores (Spearman's p = 0.53), suggesting its potential for lightweight deployment.

**Решение:** -4 creativity assessment in K-12 computer science student projects

---

### 465 · R6393

**Mitigating Security Risks in Large Language Models: A Full Lifecycle Perspective**

2026 · Machine Learning · journalarticle, article · en · https://doi.org/10.1007/s10994-025-06930-x

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 mitigating security risks in LLMs, cybersecurity

---

### 466 · R4707

**Neurocognitive Foundations of Oral Discourse Production and Its Predictive Value in Dyslexia-Related Learning Disorders**

2026 · Repositori ObertUDL (University of Lleida) · dissertation · en · https://hdl.handle.net/10459.1/470874

Developmental dyslexia affects approximately 5–10% of school-age children, yet clinical screening tools remain largely reactive: most instruments are designed for children aged seven and above, after reading failure has already occurred and its academic and psychological consequences have begun to compound. The preschool years of three to six represent a critical window in which neurobiological risk markers manifest as measurable deficits in oral language, offering an opportunity for early identification that current tools fail to exploit. This work presents NECODYS (NEuroCOgnitive markers of DYSlexia), a prototype early-screening support system for children aged four to five. The system captures spontaneous Catalan oral speech samples through a Flutter mobile application and processes them through a multi-stage linguistic analysis pipeline: automatic transcription, NLP morphosyntactic feature extraction, large language model qualitative profiling, and a discourse quality score on a 0–10 scale that provides the specialist with a quantitative decision-support indicator. To select and evaluate each pipeline component, a development corpus of manually authored Catalan speech samples representing three discourse quality levels was constructed and benchmarked. The extracted linguistic metrics — including mean utterance length, lexical diversity, and repetition rate — reliably discriminated between quality levels, and the automatic discourse quality score showed strong agreement with researcher-assigned reference scores. The results demonstrate that end-to-end automated oral discourse screening for Catalan-speaking preschool children is technically feasible. NECODYS is designed as a decision-support tool for speech-language pathologists, not as an autonomous diagnostic system. Clinical deployment requires a prospective study with real patient recordings, independent expert raters, and ethics committee approval.

**Решение:** -4 neurocognitive screening of oral discourse in developmental dyslexia, acoustic features

---

### 467 · R12359

**Augmenting Creativity using Generative AI: The Method of Trisociation**

2023 · Zenodo · journalarticle/none · https://doi.org/10.5281/zenodo.8176466

This monograph explore the use generative AI in augmenting human creativity. It also presents an extensive exploration of the method of trisociation, an relatively unknown technique for divergent thinking that fosters the emergence of novel ideas by interconnecting three distinct concepts. Trisociation builds upon the well-known method of bisociation, which involves juxtaposing two unrelated concepts to uncover fresh insights. While trisociation has been briefly mentioned by Victor Papanek in book ‘Design for the Real World’ published in 1974, it has not been extensively studied or documented in academic research. This paper aims to address this gap by offering a comprehensive analysis of the trisociation technique, encompassing its underlying principles, processes, benefits, limitations, and potential applications. The paper also explores the different ways in which the utilization of generative AI tools, such as large language models (LLMs), can enhance and support the application of the trisociation method by human ideators.

**Решение:** -4 TRIZ and generative AI for engineering creativity

---

### 468 · R4353

**Assessing the Effectiveness of LLMs in Delivering Cognitive Behavioral Therapy**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2603.03862

As mental health issues continue to rise globally, there is an increasing demand for accessible and scalable therapeutic solutions. Many individuals currently seek support from Large Language Models (LLMs), even though these models have not been validated for use in counseling services. In this paper, we evaluate LLMs' ability to emulate professional therapists practicing Cognitive Behavioral Therapy (CBT). Using anonymized, transcribed role-play sessions between licensed therapists and clients, we compare two approaches: (1) a generation-only method and (2) a Retrieval-Augmented Generation (RAG) approach using CBT guidelines. We evaluate both proprietary and open-source models for linguistic quality, semantic coherence, and therapeutic fidelity using standard natural language generation (NLG) metrics, natural language inference (NLI), and automated scoring for skills assessment. Our results indicate that while LLMs can generate CBT-like dialogues, they are limited in their ability to convey empathy and maintain consistency. Accepted to LREC 2026

**Решение:** -6 delivering CBT via LLM chatbot, user evaluation of chatbot therapy

---

### 469 · R6980

**Use of large language models for emotional analysis of songs from social data**

2026 · Νημερτής · article · el · https://hdl.handle.net/10889/32590

Η ραγδαία ανάπτυξη των υπηρεσιών μουσικής μέσω διαδικτύου έχει αυξήσει το ενδιαφέρον για την αυτόματη αναγνώριση των συναισθημάτων που συνδέονται με τα μουσικά κομμάτια. Καθώς η συναισθηματική αντίληψη της μουσικής διαμορφώνεται από πολλούς παράγοντες πέρα από το ίδιο το ηχητικό σήμα, όπως στίχους και μεταδεδομένα, αναζητούνται νέες προσεγγίσεις που δεν βασίζονται αποκλειστικά στην ακουστική ανάλυση. Ο καθορισμός του συναισθηματικού φορτίου ενός τραγουδιού αποτελεί μια εξαιρετικά χρονοβόρα και κοστοβόρα διαδικασία όταν αυτή πραγματοποιείται από ανθρώπινους αξιολογητές. Η παρούσα διπλωματική εργασία εξετάζει κατά πόσο τα Μεγάλα Γλωσσικά Μοντέλα μπορούν να εκτιμήσουν τις συναισθηματικές διαστάσεις Σθένος και Διέγερση αξιοποιώντας αποκλειστικά πληροφορίες μεταδεδομένων που παρέχονται με χρήση προτροπών, τόσο χωρίς παραδείγματα εισόδου‑εξόδου (Zero-Shot) αλλά και εμπλουτισμένες με μερικά παραδείγματα (Few-Shot). Υλοποιήθηκε ένα σύστημα που αξιοποιεί τα μεταδεδομένα που περιέχονται στο σύνολο δεδομένων DEAM, δημιουργεί κατάλληλες προτροπές για κάθε ένα από τα μουσικά κομμάτια του συνόλου, αλληλεπιδρά με γλωσσικά μοντέλα δύο διαφορετικών οικογενειών και μεγεθών παραμέτρων, Llama 8B/70B και Qwen 7B/72B, και καταγράφει τις προβλέψεις τους. Η αξιολόγηση των μοντέλων πραγματοποιείται μέσω σύγκρισης των προβλέψεων με τις τιμές που έδωσαν οι αξιολογητές, χρησιμοποιώντας τις μετρικές: Μέσο Απόλυτο Σφάλμα, Συντελεστής Συσχέτισης Pearson, Σταθμισμένος Συντελεστής Kappa του Cohen. Τα αποτελέσματα έδειξαν ότι το μέγεθος και η οικογένεια του γλωσσικού μοντέλου, καθώς και η τεχνική προτροπών, επηρεάζουν σημαντικά την ακρίβεια πρόβλεψης, με τo μεγαλύτερο μοντέλο της οικογένειας Qwen στην περίπτωση χρήσης Few-Shot να υπερτερεί. Παράλληλα, διαπιστώθηκε ότι η πρόβλεψη της διάστασης Σθένους είναι ιδιαίτερα απαιτητική, ενώ όλα τα μοντέλα παρουσίασαν δυσκολία στην αναγνώριση τραγουδιών με χαμηλό Σθένος και χαμηλή Διέγερση. Συνολικά, τα ευρήματα καταδεικνύουν ότι η αποκλειστική χρήση μεταδεδομένων δεν επαρκεί για την αξιόπιστη εκτίμηση του συναισθηματικού φορτίου μουσικών κομματιών.

**Решение:** -4 emotional analysis of song lyrics in Greek

---

### 470 · R0425

**Three Ceilings: Model Monoculture, Solvency, and the Penalty Doctrine in Markets for Expert Services**

2026 · Figshare · preprint/preprint, preprint · https://doi.org/10.6084/m9.figshare.33188046

When generative AI drives the marginal cost of a persuasive expert artefact toward zero, production-cost signals of competence lose their content and only outcome-contingent liability commitments continue to separate types. Such commitments appear robust to better AI: because the failure rate stays positive, a residual state survives on which liability can be priced. We show that this robustness rests on an unstated homogeneity assumption about the residual, and that a liability commitment faces not one ceiling but three. Decomposing AI error into idiosyncratic and common components, and using the finding of Kim et al. (2025) that larger and more accurate models exhibit more correlated errors even across architectures and providers, we show that capability growth eliminates idiosyncratic error faster than common error. The residual becomes progressively common, and the common component is precisely what a verifier drawn from the same foundation model cannot observe. Goel et al. (2025) supply the direct measurement: LLM-judge scores correlate with judge-generator model similarity at r = 0.84, an association that survives controlling for accuracy. Provability is therefore state-dependent and deteriorates as the residual becomes common. Separation then requires the commitment that must be posted to fall below the commitment that can be posted: v / theta_eff &lt;= min{Lbar, m v}, where Lbar is credible capacity and m the enforceable liquidated-damages multiple. Writing l = Lbar / v, this yields the survival condition xi kappa &lt;= 1 - 1/(M theta_0) with M = min{l, m}, and partitions the parameter space into a doctrine-bound and a solvency-bound regime that switch at the ticket size v* = Lbar / m. The threshold rises steeply in M over [1,2] and flattens above M = 3. Calibrated to six engagement types across four jurisdictions, the generative-AI exclusions introduced into commercial general liability and professional lines from January 2026 shift eight of twenty-four cells from doctrine-bound to solvency-bound, and reduce the cells that survive xi = 0.4 from twelve to four. Common-law jurisdictions are constrained by doctrine and were already at the boundary; civil-law B2B contracting, where judicial reduction is unavailable against merchants, is constrained by solvency and is where the insurance withdrawal bites. We therefore do not claim that the market dies of an information crisis. We show which crisis binds where, and that the answer has recently changed.

**Решение:** -4 economic model of generative AI production costs

---

### 471 · R11107

**Can a zero-shot learning Large Language Model code complex interview data?**

2024 · European Journal of Public Health · journalarticle, article · en · https://doi.org/10.1093/eurpub/ckae144.1121

Abstract Background Psychological autopsy is essential to establish theories, explore trends and identify previously unexplored psychosocial risk factors in suicide research. However, qualitative research has been scrutinized for being prone to interpretation bias, problems with accuracy, challenges to reproducibility, and is very time- and cost intensive. The current study aimed to investigate if a Large Language Model can achieve sufficient agreement with a researcher in the deductive coding of interview data obtained in a psychological autopsy study of suicide, to be integrated with qualitative research procedures. Methods Data from 38 interviews was deductively coded by a researcher and a LLAMA 3 based language model. The model performance was evaluated in four increasingly difficult coding tasks, including binary classification and data summarization. Intercoder agreement scores were calculated using Cohen’s Kappa. Results The preliminary results showed that the LLM achieved substantial agreement with the human coders for the binary classification task (.78). The variability in performance was influenced by code definitions. The results of the quality of LLM interpretation and summarization will also be presented. Conclusions State-of-the-art LLM can be easily integrated into the qualitative analyses of psychological autopsy interviews and may improve real time monitoring of suicides. We recommend a human-AI collaborative model, whereby deductive coding by the LLM is complemented by human inductive coding and further interpretation. Key messages • Integrating an LLM with qualitative research procedures is feasible in a collaborative model. • Integrating an LLM with qualitative research procedures allows near real-time monitoring based on qualitative data, which extends to other public health fields.

**Решение:** + T1 psychological autopsy suicide interview deductive coding: LLaMA-3 vs researcher, kappa 0.78

---

### 472 · R2281

**Comparative evaluation of ChatGPT and Gemini in answering patient-oriented questions about coronary artery bypass grafting: An expert-based cross-sectional study**

2026 · Cardiovascular Surgery and Interventions · article · https://doi.org/10.4274/e-cvsi.2026.2026-9-2

Objectives: Large language models (LLMs) are increasingly used by patients to obtain information about high-risk procedures such as coronary artery bypass grafting (CABG).This study aimed to compare expert evaluations of responses generated by ChatGPT (GPT-5.5 Instant, OpenAI) and Gemini (Gemini 3.5 Flash, Google) to frequently asked patient-oriented questions about CABG. Patients and methods:In this expert-based cross-sectional study, responses generated by ChatGPT and Gemini to 29 frequently asked CABG-related questions developed by cardiovascular surgeons were evaluated.The questions were submitted in English to both models through free, publicly available web interfaces using a standardized prompt.Each question was entered in a separate new chat session, and only the first generated response was recorded.Optional web search and Deep Research features were not manually enabled.After model identities and model-specific elements were removed, the responses were presented separately in randomized order.Five cardiovascular surgeons independently rated the responses using a five-point Likert scale that jointly assessed clinical accuracy and usefulness.In the primary paired analysis, the sum of the five evaluators' ratings for each question was used, yielding 29 paired questionlevel observations.Results: Both models received high scores.The mean question-level total score was 23.31±1.54for ChatGPT and 23.00±1.31for Gemini.The mean paired difference was 0.31 points (bootstrap 95% confidence interval [CI], -0.07 to 0.69) and was not statistically significant (Wilcoxon signed-rank test, W=60.0; p=0.129; matched-pairs rank-biserial correlation=0.37).At the individual-rating level, 97.2% of ratings were 4 or 5 for each model.The average-measures absolute-agreement intraclass correlation coefficient was 0.50 (95% CI, 0.13-0.74)for ChatGPT and 0.15 (95% CI, -0.49-0.56)for Gemini.Conclusion: Under the reported evaluation conditions, responses generated by ChatGPT and Gemini received similarly high combined ratings for clinical accuracy and usefulness.These findings reflect the expert-rated clinical appropriateness of model responses generated at a specific time point; they do not establish guideline concordance, within-model reproducibility, patient comprehension, or clinical benefit.LLM-generated CABG information may have a supportive role in patient education; however, this possibility requires validation in patient-based studies.These tools should not replace individualized physician-led counseling.

**Решение:** -4 ChatGPT and Gemini answering patient questions about somatic disease

---

### 473 · R7802

**Generative Content Analysis for Policy Research: Comparing LLM Reliability in Analyzing Institutional AI Discourse**

2025 · International Conference on Control Systems and Computer Science · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/cscs66924.2025.00094

This study examines the methodological implications of using large language models (LLMs) as research assistants in coding and qualitative content analysis. We compared how ChatGPT-4o and Gemini 2.0 perform when independently coding and extracting content from university generative AI policies according to a framework of ten "vocabularies of AI competence." Our dataset comprised official AI guidelines from 33 leading global universities. Quantitative analysis of inter-coder reliability indicated significant variation across conceptual categories, with high convergence for vocabularies related to academic integrity and information accuracy, but divergence in detecting other concepts such as AI dependency. Qualitative comparisons of extraction outputs demonstrated methodological trade-offs between models, with ChatGPT-4o providing fewer but contextually richer extractions versus Gemini 2.0's more numerous but briefer quotations. These findings have important considerations for researchers employing LLMs in qualitative analysis: domain-specific reliability assessment, complementary multi-model approaches to balance analytical depth and breadth, and acknowledgment of model-dependent dataset composition.

**Решение:** -4 content analysis of policy documents

---

### 474 · R5676

**THE MILITARY GINI INDEX AS A PREDICTOR OF ENDOGENOUS STRUCTURAL RUPTURES IN NON-ERGODIC MACROSYSTEMS**

2026 · Věda a perspektivy · article · https://doi.org/10.52058/2695-1592-2026-8(63)-507-533

Contemporary macroeconomic modeling operates with an extensive toolkit of quantitative analysis for wealth distribution, capital flows, and fiscal capacity, yet remains structurally insensitive to a critical endogenous variable -the internal distribution of the institutional right to exercise organized violence within a state.This paper conducts a systematic review of existing theoretical approaches to the monopoly on violence (Weber, 1919;North, Wallis & Weingast, 2009;Tilly, 1985Tilly, , 1990)), quantitative militarization indices (GMI, M3, SIPRI), and econometric models of civil conflict prediction (Collier & Hoeffler, 2004;Fearon & Laitin, 2003).It is established that none of the existing approaches applies the Gini distribution methodology to measure the concentration of coercive capacity among institutional actors within a state.A novel metric is proposed -the Military Gini Index (𝑮 𝒎𝒊𝒍 ∈ [𝟎, 𝟏]), which formalizes the degree of concentration of the state's monopoly on legitimate and illegitimate coercion as a continuous phase-space metric.Four dimensions of scientific novelty are substantiated: methodological (transforming qualitative typologies into a quantitative phase space), conceptual (analytical delineation of 𝑮 𝒎𝒊𝒍 from 𝑮 𝒆𝒄𝒐𝒏 ), predictive (𝑮 𝒎𝒊𝒍 as a leading indicator of systemic collapse), and cybernetic (integrating the topology of coercion into management-control theory).Empirical calibration is executed through a tiered protocol: on the inter-rater reliability sample (4 benchmark scenarios: Poland 2023-2024 and the Russian Federation T1-T3, 𝑵=𝟒𝟓 paired decisions), agreement among three independent LLM judges reaches ICC(2,1) = 0.934 and quadratic-weighted 𝜿=𝟎.𝟗𝟑𝟎; across the extended descriptive Tier 1 Věda a perspektivy № 8(63) 2026

**Решение:** -4 military Gini index macroeconomic modeling

---

### 475 · R9320

**AUTALIC: A Dataset for Anti-AUTistic Ableist Language In Context**

2025 · Annual Meeting of the Association for Computational Linguistics (ACL) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2025.acl-long.1022

As our understanding of autism and ableism continues to increase, so does our understanding of ableist language towards autistic people. Such language poses a significant challenge in NLP research due to its subtle and context-dependent nature. Yet, detecting anti-autistic ableist language remains underexplored, with existing NLP tools often failing to capture its nuanced expressions. We present AUTALIC, the first benchmark dataset dedicated to the detection of anti-autistic ableist language in context, addressing a significant gap in the field. The dataset comprises 2,400 autism-related sentences collected from Reddit, accompanied by surrounding context, and is annotated by trained experts with backgrounds in neurodiversity. Our comprehensive evaluation reveals that current language models, including state-of-the-art LLMs, struggle to reliably identify anti-autistic ableism and align with human judgments, underscoring their limitations in this domain. We publicly release AUTALIC along with the individual annotations which serve as a valuable resource to researchers working on ableism, neurodiversity, and also studying disagreements in annotation tasks. This dataset serves as a crucial step towards developing more inclusive and context-aware NLP systems that better reflect diverse perspectives. accepted to ACL main 2025, 9 pages, 5 figures, 7 tables

**Решение:** -4 AUTALIC dataset of anti-autistic ableist language, hate speech

---

### 476 · R11558

**CBT-Bench: Evaluating Large Language Models on Assisting Cognitive Behavior Therapy**

2024 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2410.13218

There is a significant gap between patient needs and available mental health support today. In this paper, we aim to thoroughly examine the potential of using Large Language Models (LLMs) to assist professional psychotherapy. To this end, we propose a new benchmark, CBT-BENCH, for the systematic evaluation of cognitive behavioral therapy (CBT) assistance. We include three levels of tasks in CBT-BENCH: I: Basic CBT knowledge acquisition, with the task of multiple-choice questions; II: Cognitive model understanding, with the tasks of cognitive distortion classification, primary core belief classification, and fine-grained core belief classification; III: Therapeutic response generation, with the task of generating responses to patient speech in CBT therapy sessions. These tasks encompass key aspects of CBT that could potentially be enhanced through AI assistance, while also outlining a hierarchy of capability requirements, ranging from basic knowledge recitation to engaging in real therapeutic conversations. We evaluated representative LLMs on our benchmark. Experimental results indicate that while LLMs perform well in reciting CBT knowledge, they fall short in complex real-world scenarios requiring deep analysis of patients' cognitive structures and generating effective responses, suggesting potential future work. NAACL 2025 Camera Ready

**Решение:** + T1 CBT-Bench: classification of cognitive distortions and core beliefs in patient speech vs benchmarks

---

### 477 · R1154

**Synthetic Hate Speech Data Underrepresents Minority Groups**

2026 · ACM Transactions on Intelligent Systems and Technology · journalarticle, article · en · https://doi.org/10.1145/3856808

The use of synthetic data is becoming increasingly widespread in a variety of applications. For hate speech detection, synthetic data offers the chance to overcome limitations of existing models and datasets, such as data scarcity, negative psychological impact on annotators, and privacy issues. However, previous work on the topic has only focused on evaluating synthetic datasets extrinsically, by measuring the performance of models trained on synthetic texts. In this work, in addition to measuring the performance of models trained on synthetic data in cross-distribution setups, we carry out a qualitative analysis, aiming at assessing how closely synthetic data can mimic authentic user-generated and human-annotated data. We focus in particular on possible issues related to (under)representation of specific minority groups as targets of hate in synthetic data. To do this, we augment an existing English hate speech dataset by paraphrasing the original gold data using three large language models, and then evaluate the synthetic data both quantitatively, including testing out-of-distribution model generalization, and qualitatively, examining the realism of synthetic texts, their hate speech content, and whether they represent the same identity groups as the original data. We pair this analysis with a detailed breakdown, for each demographic characteristic, of how the synthetic data creation process affects the representation of each specific type of identity, which is the main contribution of our work. We find that, while the performance of models trained on synthetic data is promising, these texts are easily identified as written by an LLM by humans, hate speech labels are not necessarily preserved, and the paraphrasing process tends to erase representation of minority groups and intersectional identities, affecting certain demographics more than others.

**Решение:** -4 synthetic hate speech dataset

---

### 478 · R8134

**Efficiency with Rigor! A Trustworthy LLM-powered Workflow for Qualitative Data Analysis**

2025 · arXiv (Cornell University) · preprint/article, review, preprint · en · https://doi.org/10.48550/arxiv.2501.00775

Qualitative data analysis (QDA) emphasizes trustworthiness, requiring sustained human engagement and reflexivity. Recently, large language models (LLMs) have been applied in QDA to improve efficiency. However, their use raises concerns about unvalidated automation and displaced sensemaking, which can undermine trustworthiness. To address these issues, we employed two strategies: transparency and human involvement. Through a literature review and formative interviews, we identified six design requirements for transparent automation and meaningful human involvement. Guided by these requirements, we developed MindCoder, an LLM-powered workflow that delegates mechanical tasks, such as grouping and validation, to the system, while enabling humans to conduct meaningful interpretation. MindCoder also maintains comprehensive logs of users' step-by-step interactions to ensure transparency and support trustworthy results. In an evaluation with 12 users and two external evaluators, MindCoder supported active interpretation, offered flexible control, and produced more trustworthy codebooks. We further discuss design implications for building human-AI collaborative QDA workflows.

**Решение:** -4 MindCoder QDA workflow for qualitative analysis

---

### 479 · R2928

**Debiasing ML- or AI-Generated Regressors in Partially Linear Models**

2026 · Information Systems Research · journalarticle, review, article · en · https://doi.org/10.1287/isre.2024.1370

Organizations increasingly use machine learning (ML) and artificial intelligence (AI), including large language models, to generate variables for regression models that inform business and policy decisions. For example, practitioners may use AI to predict review sentiment, ad aesthetics, or emotional expressions, and then estimate their causal effects on outcomes such as sales or engagement. However, because AI predictions are imperfect, directly using these AI-generated variables as regressors introduces measurement error that can systematically bias causal estimates, potentially leading to over- or underinvestment in business strategies. We develop new estimators that correct this bias in partially linear regression models, which are widely deployed in experimental systems at major platforms, including Tencent, Amazon AWS, and Microsoft. Our approach requires only a small human-annotated subsample alongside the large AI-labeled data set to achieve unbiased and efficient estimation. We demonstrate that our methods work with both traditional ML algorithms and LLM-based predictions. Our framework can be directly integrated into existing analytics and experimental systems, enabling practitioners to leverage the scalability of AI-generated data while maintaining reliable causal conclusions. This work also has implications for AI fairness, as our approach can help correct biases from any source in AI predictions.

**Решение:** -4 debiasing AI regressors in econometrics

---

### 480 · R11497

**Talking to oneself in CMC: a study of self replies in Wikipedia talk pages**

2024 · arXiv (Cornell University) · journalarticle, text/article, preprint · en · https://doi.org/10.48550/arxiv.2411.19007

This study proposes a qualitative analysis of self replies in Wikipedia talk pages, more precisely when the first two messages of a discussion are written by the same user. This specific pattern occurs in more than 10% of threads with two messages or more and can be explained by a number of reasons. After a first examination of the lexical specificities of second messages, we propose a seven categories typology and use it to annotate two reference samples (English and French) of 100 threads each. Finally, we analyse and compare the performance of human annotators (who reach a reasonable global efficiency) and instruction-tuned LLMs (which encounter important difficulties with several categories).

**Решение:** -4 linguistic analysis of self-replies on Wikipedia talk pages

---

### 481 · R5285

**The Archipelago of Thirty-Six: Measuring Structural Divergence in Large Language Model Judgment on Tasks Without a Correct Answer (Cross Model Repertory Grid)**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.20723228

Public leaderboards rank large language models (LLMs) by capability on tasks with a verifiable correct answer. A large class of practical tasks, including advisory, strategic, and ethical judgment, has no such answer: competent models can legitimately disagree. We introduce the Cross-Model Repertory Grid (CM-RG), an automated, contamination-resistant pipeline that adapts Kelly's Personal Construct Psychology to measure structural divergence in evaluative judgment between models rather than their capability. In the run reported here we covered 36 frontier models from 12 provider families across three deployment tiers (cheap, mid, flagship), on seven advisory tasks under two prompting conditions (neutral and persona). Models produced free responses, elicited their own bipolar constructs by triadic comparison, and cross-rated one another on the union of emergent constructs. The analysis of record (2026-06-13) comprises 3,055,153 ratings over 13,928 rater-by-ratee pairs and 86,418 emergent constructs, at a total API cost of $112.89. The mean pairwise inter-rater correlation was low. We report three structured endings: (1) weak consensus that survives every robustness check; (2) a calibration-tier eject in which a rater's own tier, not its target's, predicts how leniently it scores (mid-tier highest, cheap-tier lowest); and (3) a three-region structure, with a tight Western-lab cluster, a Chinese-flagship transitional zone, and an anti-consensus periphery of small open-weights models that correlate negatively with the consensus. We argue frontier LLM judgment on open tasks is pluralistic, structured, and largely orthogonal to capability tier and price. CM-RG is explicitly not appropriate for tasks with a verifiable correct answer.

**Решение:** -6 Cross-Model Repertory Grid measuring structural divergence across LLMs without human ground truth

---

### 482 · R1497

**Ep. 699: Can AI Get the Joke? Sarcasm, Irony, and LLM Nuance**

2026 · Zenodo (CERN European Organization for Nuclear Research) · audiovisual/, other · en · https://doi.org/10.5281/zenodo.19360835

Episode summary: Ever wonder how a machine knows when "great, just great" actually means something is terrible? In this episode, we dive into the three pillars of AI development—pre-training, fine-tuning, and reinforcement learning—to uncover how models navigate the messy, fractal world of human irony and humor. We explore the "trillion-dollar question" of why some bots feel like helpful partners while others fall into the trap of toxic positivity or robotic sycophancy. Learn how latent space mapping, "Constitutional AI," and massive statistical patterns are turning cold code into a conceptual map of human intent, allowing AI to finally understand the subtle dissonance that defines our daily conversations. Show Notes ### The Challenge of Non-Literal Language Human communication is rarely a straight line. We speak in circles, using irony, sarcasm, and regional idioms that defy literal translation. For decades, the goal of teaching computers to understand these nuances was the "holy grail" of computer science. Early attempts relied on symbolic AI—rigid rulebooks of "if-then" statements—which ultimately failed because language is too messy and fractal to be contained by simple logic. Modern Large Language Models (LLMs) have taken a different path. Rather than following rules, they rely on three primary pillars: massive pre-training, supervised fine-tuning (SFT), and reinforcement learning from human feedback (RLHF). This combination allows machines to move beyond a dictionary definition of words and into a "latent space" where they can map the probability of intent. ### Detecting Dissonance in Latent Space At the heart of an AI's understanding is a high-dimensional coordinate system. In this space, every word and concept has a location. The model doesn't just "read" the word "wonderful"; it looks at the neighborhood the word lives in. When a user describes a disaster as "wonderful," the model detects statistical dissonance. Because the model has processed trillions of tokens—including movie scripts where emotions are explicitly labeled—it recognizes that extreme overstatements often signal sarcasm. It acts as a dissonance detector, calculating whether a statement is more likely to be literal or ironic based on the surrounding context and the reality of the objects being described. ### From Raw Code to Friendly Assistant While pre-training gives a model the ability to understand language, it doesn't provide a personality. To bridge the gap between a "prediction engine" and a "helpful assistant," developers use Supervised Fine-Tuning. This involves humans writing "gold standard" dialogues that demonstrate empathy and appropriate tone. To refine this further, Reinforcement Learning from Human Feedback (RLHF) allows the model to generate multiple responses and have humans rank them. Over millions of iterations, the model develops a reward function, internalizing the subtle social cues that signal friendliness or wit. It isn't that the model has feelings; it has simply become an expert at simulating the linguistic patterns of someone who does. ### The Problem of "Toxic Positivity" One side effect of optimizing for human satisfaction is the "sycophancy problem." Because models want to maximize their "reward," they can sometimes become overly bubbly or agree with users even when the user is wrong. This results in a "Clippy-style" annoyance or "toxic positivity," where the AI fails to acknowledge the gravity of a negative situation. To combat this, developers are implementing "Constitutional AI." This involves giving the model a set of principles—a constitution—that it must follow. A second "critic" model then monitors the primary AI's responses to ensure it isn't being too sycophantic or inappropriately cheerful, acting as a mirror to keep the tone grounded and realistic. ### Universal Intent and World Grounding The most impressive feat of modern LLMs is cross-lingual transfer. By training on multiple languages simultaneously, models learn that a Hebrew idiom and an English metaphor might occupy the same conceptual point in latent space. They are no longer just translating words; they are mapping human intent across cultures. As these models scale, their "world-grounding"—the ability to connect text to real-world logic—continues to blur the line between artificial and human-like conversation. Listen online: https://myweirdprompts.com/episode/ai-sarcasm-irony-nuance My Weird Prompts is an AI-generated podcast. Episodes are produced using an automated pipeline: voice prompt → transcription → script generation → text-to-speech → audio assembly. Archived here for long-term preservation. AI CONTENT DISCLAIMER: This episode is entirely AI-generated. The script, dialogue, voices, and audio are produced by AI systems. While the pipeline includes fact-checking, content may contain errors or inaccuracies. Verify any claims independently.

**Решение:** -1 podcast episode on sarcasm and LLM nuance

---

### 483 · R3514

**LOGAR: A Local–Online Generate–Audit–Refine Framework for Mental Health De-identification**

2026 · IEEE/ACM International Conference on Connected Health: Applications, Systems and Engineering Technologies · conference · https://doi.org/10.1109/chase69719.2026.00064

Mental health clinical notes contain rich contextual information about symptoms, functioning, relationships, care plans, and social circumstances. This richness makes them valuable for research and care-quality analysis, but it also increases the risk that protected health information (PHI) or quasi-identifying details will remain after de-identification. Existing approaches often require either locally fine-tuned models trained on sensitive annotations or high-capacity cloud models that may expose clinical text to external services. We propose LOGAR, a Local–Online Generate–Audit–Refine framework for HIPAA-guided de-identification of mental health clinical notes. LOGAR keeps raw notes inside the local environment, where an open-weight worker LLM performs PHI identification, policy-based abstraction mapping, and note reconstruction. A stronger online judge LLM is used only after local de-identification and receives only the de-identified candidate note; its feedback is restricted to directional audit comments that do not quote or reveal residual PHI. Human-expert evaluation across Llama 3.1 8B and Mistral Large 2 workers, with GPT 5.1 and Claude Sonnet 4.6 judges, shows that the judge-guided refinement substantially reduces residual direct-identifier leaks while preserving clinical utility. The results indicate that LOGAR can improve de-identification reliability without requiring task-specific fine-tuning or direct transmission of raw clinical notes to online models. The LOGAR framework is open-source at: https://github.com/ResponsibleAILab/LOGAR

**Решение:** -4 mental health clinical notes de-identification of PHI

---

### 484 · R1929

**ChatGPT versus expert psychiatrist in managing mixed mania: a comparative case study**

2026 · European Psychiatry · journalarticle, article · en · https://doi.org/10.1192/j.eurpsy.2026.11180

Introduction Artificial intelligence (AI) models, such as ChatGPT, are increasingly explored for clinical decision support in psychiatry. Mixed mania, featuring simultaneous manic and depressive symptoms, poses diagnostic and therapeutic challenges. The reliability of AI recommendations for such complex cases remains largely unknown. Objectives To evaluate ChatGPT’s performance in managing mixed mania by comparing its responses to two clinical cases with those of a senior psychiatrist, assessing adherence to current clinical guidelines. Methods Two anonymized mixed mania case vignettes were presented to ChatGPT (GPT-4.0) and a senior psychiatrist. Responses were evaluated independently by two psychiatrists for: diagnostic accuracy, appropriateness of pharmacological and non-pharmacological recommendations, and guideline adherence. Discrepancies were resolved by consensus. Performance metrics included agreement with guidelines and concordance between ChatGPT and the human expert. Results ChatGPT correctly identified the diagnosis in 1 of 2 cases; the senior psychiatrist achieved 2/2 correct diagnoses. Pharmacological recommendations by ChatGPT partially aligned with guidelines, suggesting first-line mood stabilizers but insufficiently addressing comorbid depressive symptoms. Non-pharmacological advice was general and lacked individualized psychosocial interventions. Overall guideline adherence was 65% for ChatGPT versus 95% for the psychiatrist. Concordance between ChatGPT and the psychiatrist was moderate (Cohen’s kappa = 0.56). Conclusions ChatGPT shows partial capability in recognizing and managing mixed mania, with moderate guideline adherence. AI may offer preliminary guidance, but expert psychiatric evaluation remains essential for complex mood disorders. Further AI refinement and training on nuanced psychiatric cases are needed to improve reliability and clinical utility. Disclosure of Interest None Declared

**Решение:** ? T3/T4 ChatGPT vs senior psychiatrist in mixed mania case vignettes; kappa 0.56; check full text

---

### 485 · R10044

**Exploring factors influencing the adoption and usage of ChatGPT: Internet usage patterns in South Korea**

2025 · Computers in Human Behavior Reports · article · en · https://doi.org/10.1016/j.chbr.2025.100866

ChatGPT, a large-language-model (LLM) chatbot, is reshaping everyday activity from productivity tasks to leisure pursuits. To illuminate its early diffusion, we analyze six months of panel-based internet-usage logs for 6,791 South-Korean users, covering 15 site categories. Logistic-regression results show that intensive engagement with job- and education-related platforms, entertainment sites, community forums, and news/media outlets significantly increases the likelihood of adopting ChatGPT, whereas frequent visits to finance/real-estate and horizontal portal sites exert a negative effect. Interpreted through the Technology Acceptance Model and Diffusion-of-Innovation theory, the positive categories align with high perceived usefulness, ease of use, relative advantage, and compatibility, while the negative categories highlight risk sensitivity and low task–technology fit. By marrying behavioral trace data with established psychological constructs, the study advances theory on generative-AI uptake, demonstrates the value of usage logs over self-reports, and emphasizes the importance of cultural context in global adoption research. Practically, the findings furnish evidence-based guidance for developers and marketers seeking to target early adopters and accelerate the diffusion of generative-AI services tailored to diverse user needs. • First real-world log study linking web habits to early ChatGPT adoption • Job, education, entertainment, community, news use predicts higher adoption • Finance and portal browsing predicts lower adoption due to risk concerns • Behavioral data confirms usefulness and compatibility drive generative-AI uptake • Insights guide targeted marketing of ChatGPT to accelerate global diffusion

**Решение:** -4 internet usage patterns and ChatGPT adoption in South Korea

---

### 486 · R1775

**Neurosymbolic Multi-Agent Large Language Model System Versus Specialist Physicians in COPD and Asthma Management: A Comparative Performance Evaluation Using Guideline-Based Clinical Vignettes**

2026 · Research Square · preprint · https://doi.org/10.21203/rs.3.rs-9262455/v1

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 neurosymbolic LLM in COPD and asthma management (pulmonology)

---

### 487 · R0304

**Large Language Models for Variant-Centric Functional Evidence Mining**

2026 · arXiv (Cornell University) · preprint/article, review, preprint · https://doi.org/10.48550/arxiv.2604.00075

Functional evidence is essential for clinical interpretation of genomic variants, but identifying relevant studies and translating experimental results into structured evidence remains labor intensive. We developed a benchmark based on ClinGen curated annotations to evaluate two large language models (LLMs), a non reasoning model (gpt-4o-mini) and a reasoning model (o4-mini), on tasks relevant to functional evidence curation: (1) abstract screening to determine whether a study reports functional experiments directly testing specific variants, and (2) full text evidence extraction and classification from matched variant-paper pairs, including interpretation of evidence direction and generation of evidence summaries. Starting from ClinGen variants annotated with functional evidence, we processed curator comments with an LLM to extract PubMed identifiers, evidence labels, and narrative, and retrieved titles, abstracts, and open access PDFs to construct variant-paper pairs. In abstract screening, both models achieved high recall (0.88-0.90) with moderate specificity (0.59-0.65). For full text evidence classification under an explicit variant matching gate, o4-mini achieved 96% accuracy and higher specificity (0.83 vs. 0.37) while maintaining high F1 (0.98 vs. 0.96) compared with gpt-4o-mini. We also used an LLM-as-judge protocol to compare model generated evidence summaries with expert curator comments. Finally, we developed AcmGENTIC, an end to end pipeline that expands variant identifiers, retrieves literature via LitVar2, filters abstracts with LLMs, acquires PDFs, performs multimodal evidence extraction, and generates evidence reports for curator review, with optional agentic parsing of figures and tables. Together, this benchmark and pipeline provide a practical framework for scaling functional evidence curation with human in the loop LLM assistance.

**Решение:** -4 genomic variants functional evidence mining

---

### 488 · R4341

**Hybrid QLoRA-RAG Architecture for Saudi End-of-Service Benefits Calculation: Synthetic Data Generation and Uncertainty Quantification for Legal Reasoning**

2026 · Statistics Optimization & Information Computing · journalarticle, review, article · en · https://doi.org/10.19139/soic-2310-5070-3444

Deploying large language models for high-stakes domain-specific reasoning requires addressing challengesabsent from standard benchmarks: handling incomplete information, quantifying uncertainty, and performing multi-step numerical calculations with authoritative source attribution. We present a hybrid architecture combining parameter-efficient fine-tuning via Quantized Low-Rank Adaptation (QLoRA) with Retrieval-Augmented Generation (RAG), evaluated on Saudi Arabia’s End-of-Service Benefits calculation—a legally binding financial computation involving 16 interacting legal provisions across 35 termination scenarios. Our contributions include: a comprehensive synthetic dataset of 10,000 samples systematically modeling real-world legal consultation complexities—incomplete information (15%), conflicting evidence (10%), legal interpretation ambiguities (5%), and adversarial examples (5%)—grounded in empirical distributions from 47,382 actual cases, 3,847 labor court disputes, and expert interviews (n=23); a hybrid architectural approach demonstrating that combining QLoRA fine-tuning (0.42% trainable parameters, 93.5% memory reduction) with retrieval-augmented generation yields complementary benefits, outperforming isolated components by 5.8–8.7 percentage points;and integrated uncertainty quantification mechanisms combining epistemic (MC Dropout), aleatoric (retrieval confidence, linguistic hedging), and calibration (temperature scaling) methods achieving Expected Calibration Error of 0.043 and 89.4% precision in detecting ambiguous cases requiring human review. Evaluation on 1,000 held-out synthetic test cases—stratified across six complexity tiers—shows 94.2% accuracy (±5% tolerance), 91.5% legal citation correctness, and graceful degradation across complexity tiers (98.7% standard cases → 82.0% adversarial examples). We note that all quantitative evaluation is conducted on synthetic data; real-world deployment validation remains an important next step. Human evaluation by five Saudi legal experts (inter-rater κ = 0.73) yields 4.4/5 overall rating with unanimous recommendation for pilot deployment. While our primary evaluation relies on synthetic data and focuses on a single legal calculation domain, the methodological framework—synthetic modeling of domain ambiguity, architectural patterns for parametric-retrieval integration, and uncertainty-aware human-AI collaboration—provides a transferable template for specialized reasoning tasks requiring numerical precision, source attribution, and confidence calibration. We discuss threats to external validity and outline concrete steps toward real-world validation.

**Решение:** -4 Saudi legal reasoning for end-of-service benefits

---

### 489 · R8611

**CAPE: Context-Aware Personality Evaluation Framework for Large Language Models**

2025 · Conference on Empirical Methods in Natural Language Processing · journalarticle, conference, preprint/article · en · https://doi.org/10.18653/v1/2025.findings-emnlp.563

Psychometric tests, traditionally used to assess humans, are now being applied to Large Language Models (LLMs) to evaluate their behavioral traits. However, existing studies follow a context-free approach, answering each question in isolation to avoid contextual influence. We term this the Disney World test, an artificial setting that ignores real-world applications, where conversational history shapes responses. To bridge this gap, we propose the first Context-Aware Personality Evaluation (CAPE) framework for LLMs, incorporating prior conversational interactions. To thoroughly analyze the influence of context, we introduce novel metrics to quantify the consistency of LLM responses, a fundamental trait in human behavior. Our exhaustive experiments on 7 LLMs reveal that conversational history enhances response consistency via in-context learning but also induces personality shifts, with GPT-3.5-Turbo and GPT-4-Turbo exhibiting extreme deviations. While GPT models are robust to question ordering, Gemini-1.5-Flash and Llama-8B display significant sensitivity. Moreover, GPT models response stem from their intrinsic personality traits as well as prior interactions, whereas Gemini-1.5-Flash and Llama--8B heavily depend on prior interactions. Finally, applying our framework to Role Playing Agents (RPAs) shows context-dependent personality shifts improve response consistency and better align with human judgments. Our code and datasets are publicly available at: https://github.com/jivnesh/CAPE Accepted at EMNLP25 (Findings)

**Решение:** -2 CAPE framework evaluating personality traits of LLMs (LLM as test subject)

---

### 490 · R1465

**A General-Purpose Symbolic OS Applied to the Hardest Reasoning Benchmark—Without Learning, Without GPUs, and Without Compromise.**

2026 · Zenodo (CERN European Organization for Nuclear Research) · text/project milestone, article · https://doi.org/10.5281/zenodo.21783735

A general-purpose symbolic OS—built below the kernel, running on integer math—just solved 16.75% of the ARC-1 evaluation set. No LLMs. No neural networks. No GPUs. Just pure, deterministic, train-verified program synthesis. The Abstraction and Reasoning Corpus (ARC-1) is the gold standard for testing fluid intelligence in machines. The dominant paradigm relies on massive GPU clusters and billion-parameter language models to guess the answers. This paper demonstrates an orthogonal approach. NUMEN-QuatOS is a 10-layer computational organism that compiles from a single make command into 21 working binaries. It was never designed for ARC. Yet, pointed at the benchmark, its underlying symbolic architecture achieved 72/400 on the evaluation set and 162/400 on the training set. The significance of this result is not the raw percentage. The significance is the absolute mathematical rigor of how it was achieved: Zero LLMs in the Loop: No language model generates, guides, or evaluates the solutions. Zero Statistical Learning: No weights, no gradients, no training epochs. Zero False Positives: A candidate is only accepted if it reproduces every training pair exactly. The system does not guess; it proves. Zero Regressions: The climb from 38 → 67 eval tasks was verified via strict ID-set differencing. No previously solved task was ever traded away to gain a new one. Bare-Metal Underpinnings: The organism relies on integer-only Q32.32 fixed-point math, executing 2.32B steps/s at 12.8W, utilizing O(1) recall scaling. The Engineering Narrative: Wiring Beats Writing The primary driver of the score increase was not inventing new algorithms, but rigorously harvesting and wiring dormant, already-built solvers within the NUMEN codebase. Furthermore, the discovery and resolution of a single, silent output-unwrapping bug—which was discarding correct nested-tuple candidates—unlocked roughly a dozen pending points instantly. This is deterministic systems engineering, not AI alchemy. The Measured Frontier The system does not guess where its limits are; it measures them. Instrumentation proves that for 246 of the remaining unsolved tasks, the correct answer does not exist anywhere in the current candidate pool. Selection headroom is exactly one task. The path forward is definitively mapped: a Refiner-driven, ϕ -routed, compositional breadth-first-search synthesizer targeting object-graph primitives. Accessing the Architecture This PDF contains the complete empirical proof, the methodology of the push session, and the exact mapping of the ARC-1 frontier. The runnable machinery—the solver union, the time-stamped snapshot backups proving the zero-regression climb, and the ceiling instrumentation tools—are open-source and available for reproduction at the repository below: 🔗 Full Source Code & Reproduction Instructions: https://codeberg.org/Dragolich_Research_Labs_LLC/ARC1_NUMEN_OS_DEMONSTRATION

**Решение:** -5 symbolic OS on ARC-1 benchmark, no LLMs

---

### 491 · R0821

**A temporally Anchored Retrieval-Augmented Generation Framework for Metabolic and Bariatric Surgery Patient Education: An IFSO Artificial Intelligence Task Force Multinational Validation Study.**

2026 · Obesity surgery · journal article, validation study, multicenter study · eng · https://doi.org/10.1007/s11695-026-08746-7

Large language models (LLMs) offer promising tools for patient education, yet fixed knowledge cutoffs and hallucination risk limit their clinical utility. Current retrieval-augmented generation (RAG) approaches fail to distinguish between stable clinical knowledge and evolving recommendations. We developed and evaluated bRAGgen, a temporally anchored RAG framework incorporating five modules to enforce clinical protocols for MBS patient education: a semantic knowledge cache, multi-source evidence retrieval with graph-based fusion, uncertainty-aware generation, clinical constraint reranking, and Temporal Fisher Anchoring with Mechanism Selectivity (TFAMS) for adaptive inference. The framework was evaluated using 105 expert-curated free-response questions assessed by a multinational panel of seven specialists (5 surgeons, 2 dietitians) from five countries on a 5-point Likert scale for factuality, clinical relevance, and comprehensiveness. LLM-as-Judge evaluation using ChatGPT-4o provided complementary automated assessment. bRAGgen significantly improved response quality across all five base language models tested (p < 0.001), with large effect sizes for higher-capacity models (Cohen’s d = 0.96–1.01) and moderate effects for smaller models (Cohen’s d = 0.38–0.56) with good inter-rater reliability (Krippendorff’s α = 0.72). The largest gains occurred in safety-critical categories including Risks and Complications (+ 1.84 points) and Mental and Emotional Health (+ 1.84 points), suggesting the framework is most impactful where nuanced clinical judgment is essential. LLM-as-Judge evaluation using ChatGPT-4o demonstrated high concordance with expert ratings (Spearman’s ρ = 0.94). This proof-of-concept study suggests that a multi-module RAG framework with temporal stability anchoring can improve expert-rated LLM response quality for bariatric surgery domain knowledge, though prospective validation in patient-facing settings is needed before clinical implementation. bRAGgen improved expert-rated LLM response quality across all models tested. Largest gains in safety-critical domains: complications and mental health. Multinational panel of seven MBS experts from five countries validated results. LLM-as-Judge showed high concordance with expert ratings (ρ = 0.94). bRAGgen improved expert-rated LLM response quality across all models tested. Largest gains in safety-critical domains: complications and mental health. Multinational panel of seven MBS experts from five countries validated results. LLM-as-Judge showed high concordance with expert ratings (ρ = 0.94).

**Решение:** -4 metabolic and bariatric surgery RAG

---

### 492 · R12525

**Transformer-based LLMs in Cybersecurity: An in-depth Study on Log Anomaly Detection and Conversational Defense Mechanisms**

2023 · IEEE International Conference on Big Data (BigData) · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/bigdata59044.2023.10386976

With the advancement of conversational AI and Large Language Models (LLMs), interactive chatbots are emerging as pivotal assets for connecting with users across various sectors, enabling various capabilities and functions. However, their potential in the cybersecurity domain remains largely untapped. This article introduces a novel method to enhance chatbot performance by incorporating anomaly detection features. Our chatbot uses advanced GPT-3 models and rule-based logic to identify and extract unusual patterns and deviations within logs, making it more proficient in detecting anomalies. We present the architecture and methodology behind our anomaly detection system, showcasing its effectiveness in real-world scenarios. Combining machine learning and domain expertise, our chatbot sets a new standard in interactive, anomaly-aware conversational agents. Our anomaly detection classifier was able to achieve more than 99% of accuracy by illustrating its robust performance in accurately identifying and flagging outliers or unusual patterns in log file data. We also compared the performance of GPT-3 models with other LLMs: BERT, DistilBERT, and ALBERT. Our findings concluded that GPT-3 models consistently outperform all the other LLM models and exhibit significantly higher performance.

**Решение:** -4 cybersecurity log anomaly detection

---

### 493 · R10545

**Generative artificial intelligence in public health research and scientific communication: A narrative review of real applications and future directions.**

2025 · Digital health · journal article, review, journalarticle · eng · https://doi.org/10.1177/20552076251362070

Introduction: Generative artificial intelligence (GenAI) tools such as ChatGPT-4o and Gemini are rapidly influencing public health research and communication. Their capacity to assist with drafting, summarising, and translating content offers significant potential, particularly in multilingual and resource-limited settings.This narrative review critically explored the adoption of GenAI tools in public health research and communication, focusing on their practical applications and ethical implications. Methods: This narrative review synthesised 18 recent peer-reviewed and grey literature (2023-2025) to explore the role of GenAI in public health research and communication. A hybrid human-AI approach was used, where colour-coded manual coding was combined with AI-supported thematic analysis. All AI-generated outputs were critically reviewed, verified, and refined by the author. Results: Five key themes were identified: (1) Supporting scientific research writing tasks; (2) enhancing language clarity and scientific tone; (3) bridging the gap between science and the public; (4) ethical concerns and quality assurance; and (5) future potential and the need for upskilling. Discussion: GenAI can democratise and accelerate public health research publication and communication, provided it is used transparently and critically. Human oversight and contextual judgement remain essential to ensure responsible use. Conclusion: With thoughtful implementation, GenAI can enhance human expertise in the realm of public health, academia and scientific communication. It offers an emerging opportunity to strengthen public health research and communication, particularly when supported by ethical guidelines, training, and institutional leadership.

**Решение:** -1 review of generative AI in public health research

---

### 494 · R8409

**FutureGen: A RAG-based Approach to Generate the Future Work of Scientific Article**

2025 · IEEE International Conference on eScience · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/escience65000.2025.00087

The Future Work section of a scientific article outlines potential research directions by identifying gaps and limitations of a current study. This section serves as a valuable resource for early-career researchers seeking unexplored areas and experienced researchers looking for new projects or collaborations. In this study, we generate future work suggestions from a scientific article. To enrich the generation process with broader insights and reduce the chance of missing important research directions, we use context from related papers using RAG. We experimented with various Large Language Models (LLMs) integrated into Retrieval-Augmented Generation (RAG). We incorporate an LLM feedback mechanism to enhance the quality of the generated content and introduce an LLM-as-a-judge framework for robust evaluation, assessing key aspects such as novelty, hallucination, and feasibility. Our results demonstrate that the RAG-based approach using GPT-4o mini, combined with an LLM feedback mechanism, outperforms other methods based on both qualitative and quantitative evaluations. Moreover, we conduct a human evaluation to assess the LLM as an extractor, generator, and feedback provider. 12 pages, 6 figures, Accepted for publication at the Workshop on AI Principles in Science Communication (Ai4SC'25), held in conjunction with the IEEE eScience Conference 2025

**Решение:** -4 generating future work section of scientific articles

---

### 495 · R12419

**Humans vs. ChatGPT: Evaluating Annotation Methods for Financial Corpora**

2023 · IEEE International Conference on Big Data (BigData) · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/bigdata59044.2023.10386425

Given the vast amount of unstructured financial text data available today, there is a high demand for reliable, quality annotations to facilitate robust model development. However, traditional methods can often be expensive and time-inefficient. In this study, we investigate annotations for emotion, sentiment, and cognitive dissonance generated by the large language models (LLMs), GPT-3.5 and GPT-4, for quarterly earnings conference calls and compare them against human annotations obtained via traditional methods. We also investigate different prompt engineering choices on LLM annotation quality, experimenting with 4 styles of prompts centered around varying the amount of contextual information given and how it is presented to the models. Our results show the GPT models are not only more consistent and reliable than human annotators, but also provide annotations in a more cost- and time-efficient manner.

**Решение:** -4 financial corpora annotation: ChatGPT vs humans

---

### 496 · R7561

**Digital anthropomorphism and the psychology of trust in generative AI tutors: an opinion-based thematic synthesis**

2025 · Frontiers in Computer Science · article · en · https://doi.org/10.3389/fcomp.2025.1638657

Methodological Approach This article is an opinion-based conceptual piece that draws on a targeted selection of peer-reviewed sources to develop a conceptual discussion on digital anthropomorphism in generative AI tutors. To ground our argument in current scholarship, we searched Google Scholar, Scopus, and Web of Science for literature published between 2019 and 2025, using terms such as "AI trust," "digital anthropomorphism," and "generative AI in education." We focused on works that explicitly addressed human–AI interaction, trust psychology, or anthropomorphism in educational contexts, and excluded purely technical studies and noneducational applications. Approximately 45 relevant papers were identified. Rather than conducting a systematic review, we engaged in an informal thematic grouping of recurring ideas— such as perceived authority, emotional reassurance, automation bias, and epistemic vigilance— which informed the structure of this article. The aim here is not to provide exhaustive coverage, but to integrate converging insights from cognitive psychology, human–computer interaction, and educational technology into a coherent, opinion-driven perspective on trust calibration in AI-mediated learning. Introduction: When the Machine Feels Human Today's students interact more with generative AI tools like ChatGPT, Claude, and Google Gemini as conversational partners rather than as disembodied software. When these systems respond with fluency, politeness, and encouragement, they create a subtle but potent illusion: the AI appears to "understand" the user (Cohn et al., 2024; Karimova & Goby, 2020). This phenomenon, known as digital anthropomorphism, leads students to attribute human-like qualities—such as empathy, intelligence, and trustworthiness—to non-human systems (Jensen, 2021; Placani, 2024). This article offers a conceptual, opinion-based synthesis of recent peer-reviewed literature on this topic, drawing on insights from cognitive psychology, human–computer interaction, and educational technology. Our aim is not to provide an exhaustive or systematic review but to integrate converging findings into a coherent framework for understanding trust calibration in AI-mediated education. We structure the discussion around the conceptual pathway illustrated in Figure 1, which traces how anthropomorphic design cues may foster affective trust, reduce epistemic vigilance, and influence learner dependency, while also considering contexts in which anthropomorphism can enhance engagement and confidence when ethically designed. The Cognitive Basis of Digital Anthropomorphism Digital anthropomorphism is not a failure of rationality, but rather a manifestation of human social cognition (Fakhimi et al., 2023). Developmental psychology has demonstrated that even children ascribe intention and moral status to animated forms if they move in goal-oriented manners. Adults too habitually treat chatbots, GPS, and voice assistants as being quasi-social actors—to thank them, apologize, or obey their instructions. Generative AI amplifies this impact with linguistic anthropomorphism. Its natural language proficiency activates people's social brain mechanisms— soliciting empathy, engagement, and even perceived moral agency (Alabed et al., 2022; Q. Chen & Park, 2021). Human-computer interaction studies show that individuals are more willing to take advice from a friendly, courteous chatbot than from a direct or technical interface, even when the information is the same. This has its roots in what Clifford Nass called the "media equation": the hypothesis that people treat computers and media as if they were actual people and places. The conversational AI's design—affirmative statements, natural turns, emotional tone—invokes this illusion more powerfully than any earlier model of education technology (Inie et al., 2024). As outlined in Figure 1, these interface features can initiate a sequence from perceived empathy and authority to emotional trust, which may, in turn, lower epistemic vigilance. In the teaching environment, this has significant implications. A student made to feel "helped" or "seen" through interaction with an AI tutor is more likely to feel motivated and emotionally secure—but less apt to scrutinize the system's correctness and fairness. Its emotional trust will countervail the critical examination of the user, even when the AI tutor emulates reassurance and confidence (Chinmulgund et al., 2023). While these tendencies are well-documented in human–computer interaction and consumer research, their expression in formal educational settings is likely to be context-dependent. Factors such as learners' age, subject matter, prior exposure to AI, and cultural norms may moderate the strength of anthropomorphic responses. In this article, we treat such effects as plausible tendencies supported by adjacent literature, rather than as universal outcomes, and highlight the need for empirical validation within classroom environments. Perceived Authority and the Illusion of Understanding Belief in AI tutors is frequently influenced through perceived epistemic authority. When an AI system provides clear, assertive, and technical definitions, students might conclude that "it knows" as a human expert might. But AI systems do not know—they respond based upon statistical relationships, not conceptual understanding. This pretense of knowledge is a pernicious epistemic trap (Lalot & Bertram, 2024). It causes learners to take AI responses as authoritative, particularly when they have no pre-existing knowledge to analyze them with. Additionally, if AI response is written in didactic pedagogical tones or affective supportive tones, it reinforces the image of a wise and well-meaning tutor (Troshani et al., 2020). Educational psychology experiments demonstrate that students often rate feedback as more useful when delivered with confidence, even if the information is inaccurate. This link between confident tone and perce

**Решение:** -4 digital anthropomorphism and trust in AI tutors

---

### 497 · R4775

**One Model for All: Multi-Objective Controllable Language Models**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.04497

Aligning large language models (LLMs) with human preferences is critical for enhancing LLMs' safety, helpfulness, humor, faithfulness, etc. Current reinforcement learning from human feedback (RLHF) mainly focuses on a fixed reward learned from average human ratings, which may weaken the adaptability and controllability of varying preferences. However, creating personalized LLMs requires aligning LLMs with individual human preferences, which is non-trivial due to the scarce data per user and the diversity of user preferences in multi-objective trade-offs, varying from emphasizing empathy in certain contexts to demanding efficiency and precision in others. Can we train one LLM to produce personalized outputs across different user preferences on the Pareto front? In this paper, we introduce Multi-Objective Control (MOC), which trains a single LLM to directly generate responses in the preference-defined regions of the Pareto front. Our approach introduces multi-objective optimization (MOO) principles into RLHF to train an LLM as a preference-conditioned policy network. We improve the computational efficiency of MOC by applying MOO at the policy level, enabling us to fine-tune a 7B-parameter model on a single A6000 GPU. Extensive experiments demonstrate the advantages of MOC over baselines in three aspects: (i) controllability of LLM outputs w.r.t. user preferences on the trade-off among multiple rewards; (ii) quality and diversity of LLM outputs, measured by the hyper-volume of multiple solutions achieved; and (iii) generalization to unseen preferences. These results highlight MOC's potential for real-world applications requiring scalable and customizable LLMs. Published in Transactions on Machine Learning Research (03/2026): https://openreview.net/forum?id=qAM5PmvFYY

**Решение:** -6 multi-objective controllable language models

---

### 498 · R11437

**Screening oncology articles in a qualitative literature review using large language models: A comparison of GPT4 versus fine-tuned open source models using expert-annotated data.**

2024 · Journal of Clinical Oncology · journalarticle, review, conference-abstract · en · https://doi.org/10.1200/jco.2024.42.16_suppl.e23196

e23196 Background: Clinical Outcome Assessment (COA) conceptual gap analyses for oncology are complex and time consuming. Artificial Intelligence may efficiently reduce time to completion of such analyses. We aimed to assess two AI models’ performance for literature screening to identify relevant qualitative oncology research. We also compared accuracy and run-time for both AI models. Methods: We manually curated a dataset of title/abstract screening (n = 1,700 study references) across 17 landscape reviews. Among these, 11 landscape reviews (n = 951 study references) spanning over were in oncology, including 8 solid cancers (breast, lung, urothelial, colorectal, esophageal, head and neck, pancreatic, and stomach) and 3 non-solid cancers (lymphoma, acute myeloid leukemia, and multiple myeloma). Each citation was annotated for eligibility (Y/N) by population, study design (qualitative), and reporting of concepts (how patients feel or function). We then compared the accuracy of two AI models at predicting the screening decisions of expert researchers. The two AI models were Generative Pre-trained Transformers 4 (GPT4, OpenAI) prompts and a fine-tuned SciFive biomedical large language model (LLM). We used 70% of the data for training and 30% for test. Accuracy estimates were obtained only for the models’ ability to label eligibility within the 11 oncology datasets. Results: Both LLMs performed well for assessing relevance by oncology population, with F1-scores for the GPT4 and SciFive models being 0.92 and 0.83 respectively (precision was 0.92 and 0.93 respectively). For concept reporting the fine-tuned SciFive model outperformed GPT4 with an F1-score and precision 0.88 and 0.92 versus 0.81 and 0.79. The same was true but less pronounced for eligibility by study design, with an F1-score and precision 0.81 and 0.90 versus 0.86 and 0.76. For overall eligibility, the customized SciFive model outperformed the GPT4 model with an F1-score and precision of 0.84 and 0.92 versus 0.85 and 0.82. Lastly, it took the GPT4 prompts between 10-30 minutes to screen 100 abstracts. By contrast, the customized SciFive model took 1-2 minutes on a computer with a Quadro RTX 8000 GPU. Conclusions: In conclusion, both AI models are promising. The fine-tuned SciFive model appears slightly more accurate and performs substantially faster than the GPT4 model.

**Решение:** -6 screening oncology articles using LLMs (systematic review automation)

---

### 499 · R9355

**Can a Generative Artificial Intelligence Model Be Used to Create Mass Casualty Incident Simulation Scenarios? A Feasibility Study.**

2025 · Healthcare (Basel, Switzerland) · journal article, journalarticle, review · eng · https://doi.org/10.3390/healthcare13243184

INTRODUCTION: Mass casualty incident (MCI) simulation scenarios are developed based on detailed review and planning by multidisciplinary trauma teams. This study aimed to assess the feasibility of using generative artificial intelligence (AI) in developing mass casualty trauma simulation scenarios. The study evaluated a range of mass casualty trauma simulation scenarios generated from a public generative artificial intelligence platform based on publicly available data with a validated objective simulation scoring tool. METHODS: Using a large language model (LLM) platform (ChatGPT4, OpenAI, San Francisco, CA, USA), 10 complex MCI trauma simulation scenarios were generated based on publicly available US reported trauma data. Each scenario was evaluated by two Advanced Trauma Life Support (ATLS) certified raters based on the Simulation Scenario Evaluation Tool (SSET), a validated scoring tool out of 100 points. The tool scoring is based on learning objectives, tasks for performance, clinical progression, debriefing criteria, and resources. Two publicly available mass casualty trauma scenarios were similarly evaluated as controls. Revision and recommended feedback was provided for the scenarios, with review time recorded. Post-revision scenarios were evaluated. Interrater reliability was calculated based on Intraclass Correlation Coefficients (2, k) (ICCs). For the scenarios, scores and review times were reported as medians with interquartile range (IQR) as 25th and 75th percentiles. RESULTS: Ten mass casualty trauma simulation scenarios were generated by an LLM, producing a total of 62 simulated patients. The initial LLM-generated scenarios demonstrated a median SSET score of 78.5 (IQR 74-82), substantially lower than the median score of 94 (IQR 93-95) observed in publicly available scenarios. The interrater reliability ICC for the LLM-generated scenarios was 0.965 and 1.00 for publicly available scenarios. Following secondary human revision and iterative refinement, the LLM-generated scenarios improved, achieving a median SSET score of 94 (IQR 93-96) with an interrater reliability ICC of 0.7425. CONCLUSIONS: The feasibility study suggests that a structured, collaborative workflow combining LLM-based generation with expert human review may enable a new approach to mass casualty trauma simulation scenario creation. LLMs hold promise as a scalable tool for the development of MCI training materials. However, consistent human oversight, quality assurance processes, and governance frameworks remain essential to ensure clinical accuracy, safety, and educational value.

**Решение:** -4 mass casualty incident triage training

---

### 500 · R10392

**Talking to the brain: Using Large Language Models as Proxies to Model Brain Semantic Representation**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2502.18725

Traditional psychological experiments utilizing naturalistic stimuli face challenges in manual annotation and ecological validity. To address this, we introduce a novel paradigm leveraging multimodal large language models (LLMs) as proxies to extract rich semantic information from naturalistic images through a Visual Question Answering (VQA) strategy for analyzing human visual semantic representation. LLM-derived representations successfully predict established neural activity patterns measured by fMRI (e.g., faces, buildings), validating its feasibility and revealing hierarchical semantic organization across cortical regions. A brain semantic network constructed from LLM-derived representations identifies meaningful clusters reflecting functional and contextual associations. This innovative methodology offers a powerful solution for investigating brain semantic organization with naturalistic stimuli, overcoming limitations of traditional annotation methods and paving the way for more ecologically valid explorations of human cognition. 20 pages, 6 figures

**Решение:** -4 LLM proxy for fMRI brain semantic representations

---

### 501 · R4356

**Leveraging Generative AI for Personalized Mental Health Support: Opportunities, Challenges, and Ethical Considerations**

2026 · Lecture notes in networks and systems · conference-paper · en · https://doi.org/10.1007/978-3-032-25955-4_21

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 book chapter on GenAI in personalized mental health support

---

### 502 · R6645

**SayNext-Bench: Why Do LLMs Struggle with Next-Utterance Anticipation?**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2602.00327

We explore the use of large language models (LLMs) for next-utterance anticipation in human dialogue. Despite recent advances in LLMs demonstrating their ability to engage in natural conversations with users, we show that even leading models surprisingly struggle to anticipate a human speaker's next utterance. Instead, humans can readily anticipate forthcoming utterances based on multi-modal cues -- such as gestures, gaze, and emotional tone -- from the context. To systematically examine this gap, we propose SayNext-Bench, a benchmark evaluating MLLMs on anticipating context-conditioned responses across diverse real-world scenarios. To support it, we build SayNext-PC, a large-scale multimodal dialogue dataset, and carefully design a multi-level evaluation framework spanning lexical similarity, emotion-intention consistency, and LLM-based overall alignment. Building on this, we develop SayNext-Chat, a cognitively inspired dual-route MLLM that incorporates learnable priming tokens to fuse perceptual cues with anticipatory priors. Extensive experiments demonstrate that SayNext-Chat consistently outperforms state-of-the-art MLLMs across all evaluation levels, corroborated by user studies and LLM-as-Judge evaluations. Our results emphasize the (i) indispensable role of multimodal cues and (ii) active anticipatory processing as foundations of natural human interaction currently missing in MLLMs.

**Решение:** -6 next-utterance anticipation in dialogue

---

### 503 · R3562

**Uncertainty-Aware Test-Time Search for Optimization Problem Solving**

2026 · Annual Meeting of the Association for Computational Linguistics · journalarticle, conference · https://doi.org/10.18653/v1/2026.acl-long.1975

Automatically solving optimization problems from natural language descriptions with both efficiency and reliability is highly desirable but remains challenging. Language model hallucinations and the limited availability of labeled datasets often result in misaligned formulations, code errors, and feasibility failures. We pro-pose UMCTS , an Uncertainty-aware Monte Carlo Tree Search framework that combines the language understanding capability of large language models with the reliability of well-established solvers. UMCTS structures the solution process into four stages: global instruction, assumptions, mathematical formulation, and solver code generation. It employs Monte Carlo Tree Search with semantic-equivalence pruning, prior-guided exploration, and solver-based feasibility checks. An LLM judge provides numerical reward signals, qualitative error information, and uncertainty estimates. These signals are backpropagated to guide the search and flag unreliable outputs. Across six public benchmarks, UMCTS achieves state-of-the-art solution accuracy and improves efficiency by reducing token usage.

**Решение:** -4 optimization problem solving with MCTS

---

### 504 · R12083

**Large Language Model Agentic Approach to Fact Checking and Fake News Detection**

2024 · Frontiers in artificial intelligence and applications · book-chapter · en · https://doi.org/10.3233/faia240787

In the current digital era, the rapid spread of misinformation on online platforms presents significant challenges to societal well-being, public trust, and democratic processes, influencing critical decision making and public opinion. To address these challenges, there is a growing need for automated fake news detection mechanisms. Pre-trained large language models (LLMs) have demonstrated exceptional capabilities across various natural language processing (NLP) tasks, prompting exploration into their potential for verifying news claims. Instead of employing LLMs in a non-agentic way, where LLMs generate responses based on direct prompts in a single shot, our work introduces FactAgent, an agentic approach of utilizing LLMs for fake news detection. FactAgent enables LLMs to emulate human expert behavior in verifying news claims without any model training, following a structured workflow. This workflow breaks down the complex task of news veracity checking into multiple sub-steps, where LLMs complete simple tasks using their internal knowledge or external tools. At the final step of the workflow, LLMs integrate all findings throughout the workflow to determine the news claim’s veracity. Compared to manual human verification, FactAgent offers enhanced efficiency. Experimental studies demonstrate the effectiveness of FactAgent in verifying claims without the need for any training process. Moreover, FactAgent provides transparent explanations at each step of the workflow and during final decision-making, offering insights into the reasoning process of fake news detection for end users. FactAgent is highly adaptable, allowing for straightforward updates to its tools that LLMs can leverage within the workflow, as well as updates to the workflow itself using domain knowledge. This adaptability enables FactAgent’s application to news verification across various domains.

**Решение:** -4 fact checking and fake news detection

---

### 505 · R8549

**Evaluating LLM Alignment on Personality Inference from Real-World Interview Data**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2509.13244

Large Language Models (LLMs) are increasingly deployed in roles requiring nuanced psychological understanding, such as emotional support agents, counselors, and decision-making assistants. However, their ability to interpret human personality traits, a critical aspect of such applications, remains unexplored, particularly in ecologically valid conversational settings. While prior work has simulated LLM "personas" using discrete Big Five labels on social media data, the alignment of LLMs with continuous, ground-truth personality assessments derived from natural interactions is largely unexamined. To address this gap, we introduce a novel benchmark comprising semi-structured interview transcripts paired with validated continuous Big Five trait scores. Using this dataset, we systematically evaluate LLM performance across three paradigms: (1) zero-shot and chain-of-thought prompting with GPT-4.1 Mini, (2) LoRA-based fine-tuning applied to both RoBERTa and Meta-LLaMA architectures, and (3) regression using static embeddings from pretrained BERT and OpenAI's text-embedding-3-small. Our results reveal that all Pearson correlations between model predictions and ground-truth personality traits remain below 0.26, highlighting the limited alignment of current LLMs with validated psychological constructs. Chain-of-thought prompting offers minimal gains over zero-shot, suggesting that personality inference relies more on latent semantic representation than explicit reasoning. These findings underscore the challenges of aligning LLMs with complex human attributes and motivate future work on trait-specific prompting, context-aware modeling, and alignment-oriented fine-tuning. 8 pages, 3 figures

**Решение:** ? T1/T2 personality inference from interview transcripts; ground truth origin unclear (observer vs self-report)

---

### 506 · R9515

**AI-powered Automatic Item Generation for Psychological Tests: A Conceptual Framework for an LLM-based Multi-Agent AIG System**

2025 · Journal of Business and Psychology · journalarticle, review, article · en · https://doi.org/10.1007/s10869-025-10067-y

Abstract Large Language Models (LLMs) are transforming industrial-organizational psychology and human resource management, with one of their most promising applications being automatic item generation (AIG) for psychological test development. Although recent advances in LLM-based AIG—particularly for non-cognitive assessments such as personality— show significant potential, ensuring rigorous quality control remains a persistent challenge. This study introduces a novel AIG framework, the LLM-based Multi-agent AIG system (LM-AIG), where each agent is responsible for different stages of item development, including item generation, content review, linguistic evaluation, bias assessment, and item revision. The LM-AIG also incorporates human feedback to enhance item quality. We implemented the LM-AIG framework using the open-source tool AutoGen to generate items assessing attitudes toward the use of AI in the workplace. To evaluate the quality of the generated items, we conducted an empirical study based on structured ratings from human raters, assessing construct relevance, linguistic clarity, appropriate language level, contextual specificity, and potential bias. This paper further discusses the role of human-in-the-loop mechanisms within the LM-AIG system and outlines future research directions.

**Решение:** -2 human evaluation of LLM-generated psychological test items

---

### 507 · R0931

**Assessing the Accuracy of DeepSeek and SciSpace for Automated Data Extraction in Environmental Meta-Analysis**

2026 · Artificial Intelligence in Applied Sciences · journalarticle, review, article · https://doi.org/10.69882/adba.ai.2026023

The systematic review and meta‑analysis represent the pinnacle of evidence‑based environmental science, providing a rigorous framework for synthesizing disparate research findings into coherent, quantitative conclusions. However, the process is notoriously labor‑intensive, with the data extraction phase being a critical bottleneck that can delay projects for months. The advent of sophisticated artificial intelligence (AI) and large language models (LLMs) offers a promising solution to automate this tedious task. This article explores the transformative potential of AI in systematic reviews, with a specific focus on evaluating the accuracy of two prominent tools: the established platform SciSpace and the open‑source LLM DeepSeek‑V3.2. By analyzing their performance in extracting study design and review‑specific variables from 20 environmental studies, including qualitative and quantitative data, this analysis aims to determine their viability as ``second reviewers". Accuracy was assessed against human double‑extracted data as the gold standard. Overall accuracy for quantitative data was 95.38\% (95.63\% completely correct for DeepSeek and 95.12\% for SciSpace), while overall accuracy for qualitative data was 100\%. AI‑assisted data extraction already has the capability to enhance the efficiency and scalability under professional supervision in environmental analytic research.

**Решение:** -6 automated data extraction in environmental meta-analysis

---

### 508 · R8392

**Potential of Generative AI in Mental Health Counseling: Evaluating the Quality and Reliability of Responses from Large Language Models Using the Turing Test**

2025 · Journal of Korea Multimedia Society · article · en · https://doi.org/10.9717/kmms.2025.28.5.696

AI has achieved groundbreaking advancements across various fields, opening new possibilities. In particular, generative AI based on large-scale language models has demonstrated exceptional performance in text generation, translation, and question-answering tasks, while also garnering attention for its potential in psychological counseling. Psychological counseling plays a vital role in addressing individuals' mental and emotional challenges, yet many people are unable to access proper assistance due to professional shortages, high costs, and limited accessibility. As an alternative to tackle these issues, AI-driven psychological counseling has been proposed, offering advantages such as cost efficiency, 24/7 availability, and enhanced privacy protection. However, questions remain about whether generative AI can provide counseling responses of quality and reliability comparable to human experts. This study aims to evaluate whether generative AI, leveraging large-scale language models, can deliver responses in youth counseling comparable to those provided by professional counselors. To this end, the study applies the Turing Test to assess the quality and reliability of AI-generated counseling responses and analyzes feedback from professional counselors. The research explores the practical potential of AI in the psychological counseling domain, highlighting its ability to complement or even substitute human experts.

**Решение:** -2 human counselors evaluating LLM-generated youth counseling responses (Turing test)

---

### 509 · R5502

**Large-Model-Based Automatic Annotation for Health Text Mining in Social Media**

2026 · International Journal of Computational and Biological Sciences · journalarticle, article, journal-article · https://doi.org/10.66238/ijcbs68

The exponential growth of user-generated content on social media platforms presents an unprecedented opportunity for health text mining, enabling applications such as pharmacovigilance, syndromic surveillance, and mental health monitoring. However, the unstructured, colloquial, and noisy nature of social media text severely limits the application of traditional natural language processing techniques. Furthermore, the reliance on manual annotation to create high-quality, domain-specific training datasets constitutes a significant bottleneck, given the high costs and requirements for specialized medical knowledge. This paper comprehensively explores the application of Large Language Models to automate the annotation of health-related texts sourced from social media platforms. By formulating a sophisticated annotation framework that integrates zero-shot learning, few-shot prompting, and chain-of-thought reasoning, we investigate how large models can effectively replace or augment human annotators. The study presents a rigorous methodology for standardizing social media inputs, designing context-aware prompts, and calculating consensus scores to ensure annotation fidelity. Quantitative and qualitative analyses reveal that large models can achieve high concordance with human experts, particularly in identifying broad phenotypic expressions and adverse drug events. The findings suggest a paradigm shift in health informatics, demonstrating that automated annotation pipelines can drastically reduce dataset creation time while maintaining high standards of data quality, thereby accelerating public health research and responsive policy-making

**Решение:** ? T1 automatic annotation of health texts from social media; check mental health phenotypes

---

### 510 · R1786

**Abstract DP146: Evaluating the Feasibility of an Augmented Reality System for Motor Recovery in Stroke Rehabilitation: Proof-of-Concept Study**

2026 · Stroke · journalarticle, conference-abstract · en · https://doi.org/10.1161/str.57.suppl_1.dp146

Introduction: Post-stroke motor rehabilitation typically involves in-person therapy sessions in which clinicians prescribe tailored exercises for patients. However, access to in-person therapy is often limited, particularly for individuals in underserved and rural areas. While digital rehabilitation tools exist to bridge this gap, they frequently lack sufficient personalization considering the patient’s home environment and individual needs. To address this issue, we evaluated the feasibility of a novel AI-enabled augmented reality (AR) system that translates natural language into software using large language model (LLM) code generation at the point of care, allowing therapists to 1) design personalized, home-based exercises and 2) monitor exercise completion by patients in detail. Methods: In a prospective, single-arm proof-of-concept study, 20 therapists conducted simulated remote therapy sessions with a standardized patient with right upper extremity weakness using the AI-enabled AR system. Therapists prescribed personalized exercises with voice recordings and manual typings, which the LLM translated into software in the Scenic programming language. By using a commercial AR headset, the software provided instructions to the patient and independently monitored the completion of each exercise step, offering to therapists information to guide future exercise prescriptions. Results: The system successfully delivered 99.8% (95% CI: 98.6-100%) of the 398 instructions prescribed without errors or hallucinations. The accuracy of monitoring exercise completion was 88.4% (95% CI: 84.9-91.9%) when compared to the gold-standard evaluation by therapists. Therapists reported excellent usability (mean Likert 5-point score: 4.5 ± 0.5) and 75% indicated they would like to use the technology in clinical practice. For 90% of the therapists, the system did not have an added risk of injury compared to the current usual care with paper worksheets. Conclusions: In conclusion, our AR system can enable therapists to remotely create and deliver personalized rehabilitation exercises for stroke and other neurological conditions while monitoring completion. To our knowledge, this is the first study evaluating LLMs for real-time code generation to support clinicians in prescribing interventions in rehabilitation. This approach has the potential to expand access to individualized stroke rehabilitation beyond traditional in-person care.

**Решение:** -4 augmented reality for motor recovery in stroke rehabilitation

---

### 511 · R0037

**LLM Randomness and Creativity: An Experiment on Human-AI Collaboration**

2026 · International Convention on Information and Communication Technology, Electronics and Microelectronics · https://doi.org/10.1109/mipro70003.2026.11592010

Large Language Models (LLMs) can boost human creativity in a variety of tasks. Little is known, however, about how various customizable parameters of a given LLM affect the creativity of the human-AI collaboration outcome. In this work, we focus on the temperature parameter (which affects the randomness of the LLM suggestion) and investigate its impact on two main different types of human creativity: convergent and divergent thinking. We hypothesize that low randomness boosts convergent thinking creativity, while high randomness enhances divergent thinking. We test this hypothesis through a 3x3 full factorial between-subject experiment, in which we manipulate LLM randomness and type of task, and measure outcome creativity. The temperature parameter is set to 0.1 in the low randomness condition and 1.2 in the high randomness condition. To these two levels, we add a control condition in which participants do not get the assistance of a LLM. For the task manipulation, participants get randomly assigned to either complete the Remote Associates Test (which measures convergent thinking) or one between the Alternate Uses Test and the Divergent Association Task (which measures divergent thinking). We also investigate the role of human engagement with the LLM via detailed telemetry captured from the human-LLM interaction.

**Решение:** -4 LLM temperature effects on human-AI collaborative creative writing

---

### 512 · R4079

**The MADRS Pipeline: Supporting Depression Assessment in Clinical Trials**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.28190

Depression is a major mental disorder for which diagnosis relies primarily on clinical assessments. Automated methods to support its detection via the psychiatric MADRS scale are getting more and more attention. While existing solutions primarily focus on detecting the disorder from different text sources (e.g., online text, social media), there is still limited support for clinical trials, where clinical assessments are conducted through structured interviews based on standard guidelines such as SIGMA. In this work, we develop a LLM pipeline specifically designed to support clinicians in supporting the assessment of depression in patients enrolled in clinical trials. Our pipeline converts audio interviews into transcripts, maps them into the ten MADRS symptom items, estimates their severity, and identify problematic clinical ratings associated with them. Evaluation on real clinical interviews shows a strong overall correlation of 0.867 with expert ratings, providing interpretable support for future assessments in clinical trials.

**Решение:** + T3 MADRS depression assessment from clinical interview transcripts vs expert ratings (r=0.867)

---

### 513 · R5499

**LLM-Based Psychiatric Interview Simulation: Technical Development and Pilot Expert-Based Content Validation of a Voice Prototype.**

2026 · Academic psychiatry : the journal of the American Association of Directors of Psychiatric Residency Training and the Association for Academic Psychiatry · journal article, med, journalarticle · eng · https://doi.org/10.1007/s40596-026-02422-9

Abstract Objective This study describes the technical development and a pilot expert-based content validation of an interactive voice prototype, using the GPT-4o model, for teaching psychiatric semiology. It explores the potential of large language models (LLMs) to generate real-time feedback and address challenges in acquiring complex clinical competencies. Methods Four psychiatric patient personas (major depressive disorder, bipolar disorder—manic episode, schizophrenia, and attention-deficit/hyperactivity disorder) were developed through a structured iterative process. A subject matter expert (SME) conducted a structured heuristic evaluation to assess clinical fidelity, consistency, and vocal expressiveness across the four scenarios. Quantitative data (Likert scale scores) and qualitative feedback were mapped to identified technical and semiological challenges. Results GPT-4o simulated diverse personas with distinct profiles. The SME reported high potential pedagogical value for practicing interviewing mechanics. However, challenges included stereotyped clinical presentations and platform-imposed content restrictions. Conclusions This pilot study establishes the technical feasibility of voice-based LLM simulations. While offering a promising complementary tool, current limitations in multimodal realism and the need for rigorous faculty supervision suggest that the tool is best suited for formative practice rather than high-stakes assessment.

**Решение:** -2 expert evaluation of LLM-simulated psychiatric patient personas

---

### 514 · R10286

**Assessing the clinical support capabilities of ChatGPT 4o and ChatGPT 4o mini in managing lumbar disc herniation.**

2025 · European journal of medical research · journal article, journalarticle, article · eng · https://doi.org/10.1186/s40001-025-02296-x

PURPOSE: This study evaluated and compared the clinical support capabilities of ChatGPT 4o and ChatGPT 4o mini in diagnosing and treating lumbar disc herniation (LDH) with radiculopathy. METHODS: Twenty-one questions (across 5 categories) from NASS Clinical Guidelines were input into ChatGPT 4o and ChatGPT 4o mini. Five orthopedic surgeons assessed their responses using a 5-point Likert scale for accuracy and completeness, and a 7-point scale for reliability. Flesch Reading Ease scores were calculated to assess readability. Additionally, ChatGPT 4o analyzed lumbar images from 53 patients, comparing its recognizable agreement with orthopedic surgeons using Kappa values. RESULTS: Both models demonstrated strong clinical support capabilities with no significant differences in accuracy or reliability. However, ChatGPT 4o provided more comprehensive and consistent responses. The Flesch Reading Ease scores for both models indicated that their generated content was "very difficult to read," potentially limiting patient accessibility. In evaluating lumbar disc herniation images, ChatGPT 4o achieved an overall accuracy of 0.81, with LDH recognition precision, recall, and F1 scores exceeding 0.80. The AUC was 0.80, and the Kappa value was 0.61, indicating moderate agreement between the model's predictions and actual diagnoses, though with room for improvement. CONCLUSION: While both models are effective, ChatGPT 4o offers more comprehensive clinical responses, making it more suitable for high-integrity medical tasks. However, the difficulty in reading AI-generated content and occasional use of misleading terms, such as "tumor," indicate a need for further improvements to reduce patient anxiety.

**Решение:** -4 lumbar disc herniation clinical guideline Q&A

---

### 515 · R10965

**The Implementation of a Hybrid Large Language Model for Adaptive Cryptographic Cyber Defense**

2024 · Research Square · preprint, ppr, posted-content · en · https://doi.org/10.21203/rs.3.rs-5120507/v1

Abstract Cybersecurity threats have become increasingly complex and adaptive, requiring dynamic defense mechanisms that can keep pace with evolving attack vectors. The proposed hybrid cryptographic defense framework integrates machine learning through Llama, an open-source large language model, with traditional cryptographic techniques, enabling real-time adjustments to encryption protocols based on identified threats. This approach offers a novel solution to the challenge of responding to unpredictable cyberattacks, significantly enhancing the system’s ability to detect and mitigate threats with minimal latency and high accuracy. Extensive experimentation demonstrated that the hybrid algorithm outperforms baseline methods in key areas, including resource utilization, false positive and negative rates, and adaptive encryption strength. The framework’s scalability and efficiency were also highlighted through its ability to handle large data volumes in real-time, making it a robust solution for cryptographic defense in modern network environments. Through combining machine learning with cryptographic operations, the system achieves a higher level of responsiveness and resilience, addressing critical gaps in current cybersecurity solutions.

**Решение:** -4 cryptographic cyber defense

---

### 516 · R2258

**Adversarial Attacks on Large Language Models: The Prompt Injection Approach**

2026 · Lecture notes in electrical engineering · conference-paper · en · https://doi.org/10.1007/978-981-95-4452-3_17

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 prompt injection and adversarial attacks

---

### 517 · R8096

**Advancing Academic Chatbots: Evaluation of Non-Traditional Outputs**

2025 · CBS Research Portal (Copenhagen Business School) · journalarticle, review, preprint/article · en · https://doi.org/10.48550/arxiv.2512.00991

Most studies still judge large-language-model (LLM) chatbots only on classic tasks such as factual question answering (Q&A) and short summaries. This thesis broadens that focus by testing whether LLMs can also produce complete slide decks and podcast scripts, and by asking whether a knowledge-graph retrieval strategy (Graph RAG) improves Q&A compared with a lighter hybrid search that blends keyword and semantic retrieval (Advanced RAG). We built a prototype chatbot for Copenhagen Business School that draws on the university’s research archive and compares two contrasting models: Meta LLaMA-3-70B, an openly released model that can run on local hardware, and OpenAI GPT-4o-mini, a commercial model accessed through an API. Each model is coupled with both retrieval pipelines so their interaction can be analysed systematically. Quality is judged in two stages. First, a panel of Copenhagen Business School evaluators scores every output on eleven dimensions spanning fluency, factual accuracy, coherence, usefulness, and hallucinations. Their ratings are then cross-checked by two external LLM “judges”, giving a scalable second opinion. Across ten representative papers, GPT-4o-mini with Advanced RAG delivers the most reliable answers and the most classroom-ready slides and podcasts, while LLaMA-3 approaches GPT-4o-mini in narrative tasks, such as podcasts, but falls behind on strict factual precision. Graph RAG provides no consistent gain over Advanced RAG; the extra structure helps a handful of multi-hop questions, but also increases hallucination rates and, because of time and computational constraints, requires manual curation of entities. Human and LLM judges ranked the systems in a similar way, but the human evaluations showed much more variation between individual scores. While this makes human assessment less consistent, it also has an important advantage: human evaluators were able to notice layout and stylistic issues in the slide decks and podcasts that the LLMs did not. This shows that combining the stability of LLM-based evaluation with the human ability to catch design and presentation flaws is the most effective way to assess the quality of non-traditional academic outputs. The entire codebase used to build the pipeline of the project and examples of outputs are openly accessible on GitHub at the link Chatbot in Academia - GitHub Repository.

**Решение:** -4 LLMs generating slide decks and podcast scripts

---

### 518 · R1967

**Human Experts and AI Models in Offender Risk Assessment: A Comparative Pilot Study Using the HCR-20V3.**

2026 · Behavioral sciences & the law · comparative study, research-article, journal article · eng · https://doi.org/10.1002/bsl.70023

ABSTRACT This pilot study compares offender risk assessments conducted by human experts and advanced large language models (LLMs) within the HCR‐20V3 framework. Both groups evaluated a series of synthetic forensic case vignettes designed to simulate realistic clinical conditions. Quantitative results indicate that AI models consistently assigned higher overall risk scores and demonstrated greater inter‐rater reliability compared to human assessors. Qualitative analysis revealed distinct reasoning patterns: AI systems emphasized historical and static risk factors and often recommended more intensive management strategies, whereas human experts focused on recent behavioral improvements, dynamic change, and rehabilitation potential. These contrasts highlight fundamental differences between algorithmic pattern recognition and human clinical judgment. The findings suggest that integrating AI‐generated analyses with professional expertise can enhance the consistency and transparency of risk evaluations, while preserving the ethical, contextual, and human‐centered insights essential to forensic and clinical decision‐making.

**Решение:** + T3 HCR-20V3 offender risk assessment: human experts vs LLMs on forensic vignettes

---

### 519 · R4183

**Perspectives of Individuals With Obsessive-Compulsive Disorder on the Role of Artificial Intelligence in Therapy and Treatment: Thematic Qualitative Study.**

2026 · Journal of participatory medicine · journal article, journalarticle, review · eng · https://doi.org/10.2196/98822

Abstract Background AI has become increasingly used in mental health care for applications such as diagnosis, monitoring, and treatment support. These include tools like clinician support systems, large language models, and conversational agents used to augment psychotherapy and clinical decision-making. While prior research suggests potential benefits of and concerns with AI, little is known within the domain of obsessive-compulsive disorder (OCD). Given the expanding role of AI in psychiatry, understanding these perspectives is essential to ensuring AI implementation aligns with patient priorities and values. Objective This study aims to explore the perspectives of individuals with OCD on the use of AI in health care, including perceived benefits, risks, and its role in relation to human clinicians. Methods We conducted semistructured interviews with 24 adults self-reporting OCD, recruited through online communities and advocacy networks. Eligible individuals (≥18 y with self-reported OCD) completed screening, provided informed consent, and participated in remote Health Insurance Portability and Accountability Act (HIPAA)-compliant Zoom (Zoom Communications, Inc) interviews (May-December 2024). Transcripts were deidentified, open-coded, and used to develop a codebook. Focused codes were applied using a thematic analysis framework in Dedoose (v9.2.22; Sociocultural Research Consultants, LLC). Each transcript was independently coded by 2 reviewers, with discrepancies resolved through consensus. Themes were developed through iterative interpretive analysis of code clusters. Results Participants’ perspectives encompassed concerns and benefits of AI in mental health care. Participants expressed concerns about the accuracy and efficacy of information provided by AI, as well as a limited ability for clinical judgment in psychiatric care. Additionally, participants emphasized the importance of human connection, particularly therapeutic alliance, empathy, and reassurance provided by clinicians, which they felt AI could not replicate. Concerns about data privacy, security, and downstream use of information were also highlighted. Despite concerns, many endorsed the use of AI as an adjunct rather than a replacement for clinicians, noting potential benefits in symptom monitoring, preliminary information gathering, and support for administrative tasks, provided that human oversight is maintained. Conclusions Individuals with OCD expressed nuanced views on AI in mental health care, balancing cautious optimism with several concerns. While AI may improve efficiency, standardization, and symptom monitoring, participants highlighted risks related to deindividualization, accuracy, and erosion of human connection. These findings underscore the importance of patient-centered, ethically guided AI integration that preserves the therapeutic alliance while leveraging technological benefits.

**Решение:** -4 OCD patient perspectives on AI in therapy

---

### 520 · R9512

**VeriFact: Verifying Facts in LLM-Generated Clinical Text with Electronic Health Records**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2501.16672

Methods to ensure factual accuracy of text generated by large language models (LLM) in clinical medicine are lacking. VeriFact is an artificial intelligence system that combines retrieval-augmented generation and LLM-as-a-Judge to verify whether LLM-generated text is factually supported by a patient\u27s medical history based on their electronic health record (EHR). To evaluate this system, we introduce VeriFact-BHC, a new dataset that decomposes Brief Hospital Course narratives from discharge summaries into a set of simple statements with clinician annotations for whether each statement is supported by the patient\u27s EHR clinical notes. Whereas highest agreement between clinicians was 88.5%, VeriFact achieves up to 92.7% agreement when compared to a denoised and adjudicated average human clinican ground truth, suggesting that VeriFact exceeds the average clinician\u27s ability to fact-check text against a patient\u27s medical record. VeriFact may accelerate the development of LLM-based EHR applications by removing current evaluation bottlenecks.62 pages, 5 figures, 1 table, pre-print manuscrip

**Решение:** -4 VeriFact: verifying factual accuracy of clinical notes against EHR

---

### 521 · R0651

**LLM-assisted deductive coding of Russian open-ended responses: data, coding materials, model outputs, and analysis scripts**

2026 · OSF · collection/project, preprint · ru · https://doi.org/10.17605/osf.io/nbfdu

This project accompanies the preprint "Validating local open-weight LLMs against expert raters for graded deductive coding of open-ended responses in Russian". The study evaluates whether locally deployed open-weight large language models can support deductive coding of Russian-language open-ended responses from a psychological human–robot interaction experiment. The dataset contains responses from 33 participants. Four models – DeepSeek-R1-32B, Qwen3-32B, Gemma3-27B, and Mistral-Small-3.2-24B – were evaluated against independent annotations from ten psychology-trained expert coders using a predefined seven-code scheme. Each model was tested with three prompting procedures: singular-code prompts, a conservative singular-code variant, and a fixed-sequence multi-label prompt corresponding to the format shown to expert coders. Model queries were repeated ten times and aggregated into graded code-presence estimates. The deposited analyses assess overall and code-wise agreement with the expert reference, calibration and attribution bias, expert inter-rater reliability, single-rater human equivalence, repeated-run stability, aggregation effects, and sensitivity to binary decision thresholds. The deposit includes de-identified PsychoPy exports; the authoritative Russian response table and English accessibility translations; original Russian prompts and English translations; generation and processing scripts; retained textual model outputs and aggregate coding matrices for all twelve model-by-prompt configurations; the original expert coding form and memo, English memo translations, and consolidated de-identified expert ratings; and the complete statistical comparison and figure-generation pipeline. A data dictionary documents variables, workbook sheets, and metrics, while the preprint–deposit crosswalk links manuscript tables, figures, and appendices to their exact repository sources. The reconstructed Python environment is pinned, and the analysis runner supports both non-writing validation and complete regeneration of derived analytical outputs. The Russian reports, prompts, and expert materials are authoritative for reproducing the reported workflow. English translations are provided for accessibility and were not used for model generation, expert coding, or analysis. Code is distributed under the BSD 3-Clause License; data and other non-code materials are distributed under CC BY 4.0.

**Решение:** + T1 deductive coding of Russian psychological interview responses: 4 open-weight LLMs vs 10 expert raters

---

### 522 · R8993

**This Is Your Doge, If It Please You: Exploring Deception and Robustness in Mixture of LLMs**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2503.05856

Mixture of large language model (LLMs) Agents (MoA) architectures achieve state-of-the-art performance on prominent benchmarks like AlpacaEval 2.0 by leveraging the collaboration of multiple LLMs at inference time. Despite these successes, an evaluation of the safety and reliability of MoA is missing. We present the first comprehensive study of MoA's robustness against deceptive LLM agents that deliberately provide misleading responses. We examine factors like the propagation of deceptive information, model size, and information availability, and uncover critical vulnerabilities. On AlpacaEval 2.0, the popular LLaMA 3.1-70B model achieves a length-controlled Win Rate (LC WR) of 49.2% when coupled with 3-layer MoA (6 LLM agents). However, we demonstrate that introducing only a $\textit{single}$ carefully-instructed deceptive agent into the MoA can reduce performance to 37.9%, effectively nullifying all MoA gains. On QuALITY, a multiple-choice comprehension task, the impact is also severe, with accuracy plummeting by a staggering 48.5%. Inspired in part by the historical Doge of Venice voting process, designed to minimize influence and deception, we propose a range of unsupervised defense mechanisms that recover most of the lost performance. 35 pages, 9 figures, 16 tables

**Решение:** -6 deception and robustness in mixture of LLMs

---

### 523 · R11552

**Discrete Emotions Detection on Social Media: A Systematic Review and Comparative Analysis**

2024 · IEEE International Conference on Information Technology, Big Data and Artificial Intelligence (ICIBA) · conference, review · en · https://doi.org/10.1109/iciba62489.2024.10867988

Despite a growing corpus of work delving into social media communication, gauging discrete emotions on such sites remains challenging, especially for researchers with constrained computational expertise. By synthesizing insights from nearly 2,000 studies, we seek to address this gap through an extensive review and comparative analysis that pinpoints the most prevalent and user-friendly tools for emotional detection and verifies their effectiveness against a validated human-annotated benchmark. While each identified tool captures a spectrum of affective expressions in line with established psychological frameworks, considerable disparity emerges when examining their efficacy. Lexicon-based approaches, such as NRC EmoLex and Text2Emotion, though frequently utilized in the reviewed studies, yield merely adequate precision, with LIWC-22 providing a marginally enhanced outcome. IBM NLU, however, leveraging advanced deep learning techniques, demonstrates superior performance across both sentimental and nuanced emotional assessments. ChatGPT-4, notably, unlike some studies praising its extensive applicability, may falter in this context, particularly noted for its reduced recall. Amid the rapid advancements in social media communication, such findings may provide a foundational exploration for discerning discrete emotions online, paving the way for the development of refined navigational tools in the complex emotional landscape of the digital realm.

**Решение:** -1 systematic review of discrete emotions detection on social media

---

### 524 · R8455

**Divergent Emotional Patterns in Disinformation on Social Media? An Analysis of Tweets and TikToks About the DANA in Valencia**

2025 · International Conference on Agents and Artificial Intelligence (ICAART) · journalarticle, text/article, conference-paper · en · https://doi.org/10.5220/0013392800003890

This study investigates the dissemination of disinformation on social media platforms during the DANA event (DANA is a Spanish acronym for Depresion Aislada en Niveles Altos, translating to high-altitude isolated depression) that resulted in extremely heavy rainfall and devastating floods in Valencia, Spain, on October 29, 2024. We created a novel dataset of 650 TikTok and X posts, which was manually annotated to differentiate between disinformation and trustworthy content. Additionally, a Few-Shot annotation approach with GPT-4o achieved substantial agreement (Cohen's kappa of 0.684) with manual labels. Emotion analysis revealed that disinformation on X is mainly associated with increased sadness and fear, while on TikTok, it correlates with higher levels of anger and disgust. Linguistic analysis using the LIWC dictionary showed that trustworthy content utilizes more articulate and factual language, whereas disinformation employs negations, perceptual words, and personal anecdotes to appear credible. Audio analysis of TikTok posts highlighted distinct patterns: trustworthy audios featured brighter tones and robotic or monotone narration, promoting clarity and credibility, while disinformation audios leveraged tonal variation, emotional depth, and manipulative musical elements to amplify engagement. In detection models, SVM+TF-IDF achieved the highest F1-Score, excelling with limited data. Incorporating audio features into roberta-large-bne improved both Accuracy and F1-Score, surpassing its text-only counterpart and SVM in Accuracy. GPT-4o Few-Shot also performed well, showcasing the potential of large language models for automated disinformation detection. These findings demonstrate the importance of leveraging both textual and audio features for improved disinformation detection on multimodal platforms like TikTok.

**Решение:** -4 disinformation detection in flood-related social media posts

---

### 525 · R8317

**Assessing the Reliability of Large Language Models for Deductive Qualitative Coding: A Comparative Study of ChatGPT Interventions**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2507.14384

In this study, we investigate the use of large language models (LLMs), specifically ChatGPT, for structured deductive qualitative coding. While most current research emphasizes inductive coding applications, we address the underexplored potential of LLMs to perform deductive classification tasks aligned with established human-coded schemes. Using the Comparative Agendas Project (CAP) Master Codebook, we classified U.S. Supreme Court case summaries into 21 major policy domains. We tested four intervention methods: zero-shot, few-shot, definition-based, and a novel Step-by-Step Task Decomposition strategy, across repeated samples. Performance was evaluated using standard classification metrics (accuracy, F1-score, Cohen's kappa, Krippendorff's alpha), and construct validity was assessed using chi-squared tests and Cramer's V. Chi-squared and effect size analyses confirmed that intervention strategies significantly influenced classification behavior, with Cramer's V values ranging from 0.359 to 0.613, indicating moderate to strong shifts in classification patterns. The Step-by-Step Task Decomposition strategy achieved the strongest reliability (accuracy = 0.775, kappa = 0.744, alpha = 0.746), achieving thresholds for substantial agreement. Despite the semantic ambiguity within case summaries, ChatGPT displayed stable agreement across samples, including high F1 scores in low-support subclasses. These findings demonstrate that with targeted, custom-tailored interventions, LLMs can achieve reliability levels suitable for integration into rigorous qualitative coding workflows. Extended version of paper accepted for presentation at the ASIS&amp;T Annual Meeting 2025. 38 pages, 12 figures

**Решение:** -4 deductive qualitative coding of Supreme Court case summaries (legal/policy)

---

### 526 · R8868

**Can ChatGPT generate surgical multiple-choice questions comparable to those written by a surgeon?**

2025 · Proceedings (Baylor University. Medical Center) · journal article, journalarticle, review · eng · https://doi.org/10.1080/08998280.2024.2418752

Abstract Background This study aimed to determine whether surgical multiple-choice questions generated by ChatGPT are comparable to those written by human experts (surgeons). Methods The study was conducted at a medical school and involved 112 fourth-year medical students. Based on five learning objectives in general surgery (colorectal, gastric, trauma, breast, thyroid), ChatGPT and surgeons generated five multiple-choice questions. No change was made to the ChatGPT-generated questions. The statistical properties of these questions, including correlations between two group of questions and correlations with total scores (item discrimination) in a general surgery clerkship exam, were reported. Results There was a significant positive correlation between the ChatGPT-generated and human-written questions for one learning objective (colorectal). More importantly, only one ChatGPT-generated question (colorectal) achieved an acceptable discrimination level, while other four failed to achieve it. In contrast, human-written questions showed acceptable discrimination levels. Conclusion While ChatGPT has the potential to generate multiple-choice questions comparable to human-written ones in specific contexts, the variability across surgical topics points to the need for human oversight and review before their use in exams. It is important to integrate artificial intelligence tools like ChatGPT with human expertise to enhance efficiency and quality.

**Решение:** -4 ChatGPT generating surgical multiple choice questions

---

### 527 · R6130

**Safety, Accuracy, Empathy, Information Quality, and Readability of Large Language Models in Answering Caregiver Questions About Pediatric Burn First Aid and Inpatient Care: A Cross-Sectional Comparative Study**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-10862831/v1

Abstract Background Pediatric burn injuries are common household injuries, particularly among young children, and hot-liquid scalds are a major cause of pediatric burn morbidity. The quality of burn first aid provided by caregivers can affect pain, burn wound depth, wound healing, the need for surgical intervention, and scarring. As large language model (LLM)-driven chatbots become widely available sources of health information, caregivers may consult these tools in time-critical situations requiring burn first aid; however, their performance in pediatric burn scenarios remains insufficiently characterized. Objective To compare the safety, accuracy, empathy, information quality, and readability of four widely accessible LLM chatbots in answering caregiver-facing questions about pediatric burn first aid and inpatient care. Methods In this cross-sectional comparative evaluation, a 36-item question set was developed from an initial pool of 66 caregiver-facing questions derived from clinical guidelines, consensus statements, official patient-education materials, systematic reviews, and common pediatric burn care concerns. The same questions were entered independently into ChatGPT, Gemini, DeepSeek, and Doubao, yielding 144 chatbot responses. Five blinded raters evaluated outputs using predefined safety and accuracy criteria, an empathy scale, DISCERN, EQIP, JAMA benchmark criteria, and the Global Quality Score. Readability was assessed using the Automated Readability Index, Coleman-Liau Index, Flesch-Kincaid Grade Level, Gunning Fog Index, Simple Measure of Gobbledygook, and Flesch Reading Ease Score. Inter-rater agreement and paired question-level comparisons were examined. Results Inter-rater agreement was high for safety assessment (Fleiss κ = 0.860; 95% CI, 0.784–0.924; P ICC range, 0.831–0.899; all P P = 0.002), although the overall effect size was small (Kendall's W = 0.137). Empathy scores showed a larger between-model difference ( P P P = 0.330). All readability indices differed across models (all P

**Решение:** -2 blinded raters evaluating LLM answers to pediatric burn first aid questions

---

### 528 · R3623

**Trust and Technology Acceptance: Comparing Traditional Search Engines and Artificial Intelligence for Colorectal Cancer Information Seeking.**

2026 · Cancer control : journal of the Moffitt Cancer Center · journal article, randomized controlled trial, study · eng · https://doi.org/10.1177/10732748261454474

Introduction The integration of artificial intelligence (AI) into health information seeking is transforming health promotion. Understanding how users accept and trust these communication technologies is critical for health communication and cancer control. This study examined how the Technology Acceptance Model II (TAM II) applies to colorectal cancer information seeking, comparing link-based search (e.g., Google search) versus generative response paradigms (e.g., ChatGPT/AI) while examining trust, perceived threat, and contextual factors in technology use decisions. Methods A prospective, randomized 2×2 factorial experiment was conducted with 764 Texas adults randomly assigned to conditions to view either Google search results or ChatGPT responses for colorectal cancer symptoms, presented in either high-concern or low-concern scenarios. Participants completed validated measures including TAM II constructs adapted from Davis (1989) and Kamal et al (2020), multidimensional trust scales, Extended Parallel Process Model threat measures (Witte, 1992), and technology-related stress items, all demonstrating acceptable reliability (α > .77). Data analysis included two-way ANOVAs, correlation analysis, and stepwise regression modeling. Results Google search received significantly higher ratings than AI across all Technology Acceptance Model II constructs. Technology preferences appeared to reflect multiple factors including interface familiarity, trust in information sources, and usability expectations, with traditional search benefiting from established user mental models and transparent source attribution. Trust emerged as the strongest predictor of behavioral intention. No significant main effects were found for concern level, and no interaction effects emerged between technology type and concern level, indicating that technology preferences remained consistent regardless of symptom severity. Conclusions For cancer control and prevention, these findings suggest that patients seeking colorectal cancer symptom information may be more likely to trust and act upon traditional search results than AI-generated responses, focusing on technology use intentions for health information seeking that directly inform cancer screening and care-seeking behaviors, potentially affecting screening behaviors and care-seeking timing. Current AI implementations may not optimally serve health information needs with lower acceptance potentially related to limited source transparency and increased cognitive demands compared to familiar search interfaces, as suggested by preference patterns. Cancer control professionals should anticipate that the growing integration of AI into health information seeking may influence the public’s cancer symptom evaluation and screening behaviors.

**Решение:** -4 user trust in search engines vs AI for colorectal cancer information

---

### 529 · R10648

**Improving emotion estimation through a combination of ChatGPT and deep learning**

2025 · Journal of Decision System · article · en · https://doi.org/10.1080/12460125.2024.2440024

Estimating emotions from text is essential for machines to make human-like decisions, but it remains a challenge due to the significant time and manpower required for labeling training data. Accurate machine learning relies on high-quality training data, often necessitating multiple rounds of evaluation for emotion annotation. Large Language Models (LLMs), such as ChatGPT, hold promise for reducing the labor involved in this process. This study investigates how LLMs can minimize effort while improving accuracy. In Experiment 1, the performance of LLMs in emotion estimation was assessed, showing strong accuracy for negative emotions despite some inconsistencies with human annotations. Experiment 2 introduced a hybrid approach combining LLMs with deep learning techniques to address these inconsistencies, resulting in significantly improved accuracy. These findings demonstrate that integrating LLMs into emotion annotation workflows can reduce manual effort and enhance accuracy, offering a promising pathway for machine learning applications in emotion estimation.

**Решение:** ? T1 LLM emotion estimation from text evaluated against human annotations; check agreement metrics

---

### 530 · R10280

**Using large language models as a scalable mental status evaluation technique.**

2025 · NPP - digital psychiatry and neuroscience · journal article, journalarticle, review · eng · https://doi.org/10.1038/s44277-025-00042-z

Mental health care faces a significant gap in service availability, with demand for services significantly surpassing available care. As such, building scalable and objective measurement tools for mental health evaluation is of primary concern. Given the usage of spoken language in diagnostics and treatment, it stands out as a potential methodology. With a substantial mismatch between the demand for services and the availability of care, this study focuses on leveraging large language models to bridge this gap. Here, a RoBERTa-based transformer model is fine-tuned for mental health status evaluation using natural language processing. The model analyzes written language without access to prosodic, motor, or visual cues commonly used in clinical mental status exams. Using non-clinical data from online forums and clinical data from a board-reviewed online psychotherapy trial, this study provides preliminary evidence that large language models can support symptom identification in classifying sentences with an accuracy comparable to human experts. The text dataset is expanded through augmentation using backtranslation and the model performance is optimized through hyperparameter tuning. Specifically, a RoBERTa-based model is fine-tuned on psychotherapy session text to predict whether individual sentences are symptomatic of anxiety or depression with prediction accuracy on par with clinical evaluations at 74%. Mental health services struggle to keep up with growing demand. This study explores how a RoBERTa large language model can help by analyzing text for signs of anxiety or depression. It uses online therapy transcripts and forum posts, learning to spot symptoms from what people write, even without tone or facial cues. With accuracy similar to human experts, this approach shows promise for making mental health evaluation more accessible and scalable.

**Решение:** -5 RoBERTa encoder only, no generative LLM

---

### 531 · R10070

**Automating Personality-Based Employment Interviews: Development and Validation of an Artificial Intelligence Chatbot**

2025 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/9ktmf_v1

This study examines the use of artificial intelligence (AI) chatbots and natural language processing methods for administering and scoring personality-based employment interviews. We adapted a behavioral description interview to a chatbot interview format and evaluated the construct and criterion-related validity of machine-derived personality scores. Using archival data as a baseline, the study incorporated natural language processing (NLP) methods, including word embeddings extracted with transformers and zero-shot prompt-based scoring using a large language model (LLM). Three key findings emerged. First, chatbot interviews generated significantly lower interviewee word counts than human interviews, limiting trait-relevant cues for raters and machine-based methods. Second, construct validity results demonstrated moderate convergence between machine-derived and human rater scores, with LLM-based scores performing comparably to human ratings. However, limited discriminant validity suggests that method effects outweigh trait-specific variance. Third, machine-derived scores demonstrated incremental validity in predicting organizational citizenship behaviors (OCB) beyond self-reported personality scores, underscoring their potential utility in selection contexts. These findings emphasize the need for refinements in chatbot design to elicit richer responses and improve scoring accuracy, offering promising implications for scalable and efficient personality assessments in organizational settings.

**Решение:** + T2 LLM scoring of personality-based employment interviews vs human rater scores

---

### 532 · R6580

**An Analysis of Cognitive Outsourcing to Generative AI in University Students' Creative Problem Solving Process**

2026 · Korean Society for Creativity Education · journalarticle, review, article · https://doi.org/10.36358/jce.2026.26.2.19

This study explores university students' generative AI utilization patterns during the Creative Problem Solving (CPS) process from a “cognitive outsourcing” perspective. Analyzing 97 students across three courses with varying creativity demands, the findings are as follows. First, while students' AI literacy and ethical awareness meaningfully improved, self-assessed competency growth was relatively conservative in ill-structured task contexts. Second, regardless of course context, AI utilization preference peaked during the initial ideation stage, suggesting “universal cognitive outsourcing.” This indicates that learners substantially rely on AI to reduce cognitive load during early idea generation, irrespective of subject-specific characteristics. Third, an asymmetric pattern emerged between self-assessed AI competency and reported AI collaboration levels across CPS stages, exploratorily suggesting a possible “illusion of explanatory depth” during generative AI use. Based on these findings, the study proposes a “Reverse Human-AI Collaboration Model,” which delays AI intervention during divergent thinking while employing AI as a critical reviewer during convergent stages, and presents educational implications for establishing a human-AI co-learning ecosystem in higher education.

**Решение:** -4 cognitive outsourcing to generative AI in creative problem solving

---

### 533 · R12384

**Pedagogical Design Matters: Integrating Engineering Design and Knowledge Building for Undergraduates to Practice and Improve Computational Thinking Skills**

2023 · preprint · en · https://doi.org/10.35542/osf.io/2ugbf

In this digitalized, data-driven era, developing computational thinking (CT) skills is crucial for individuals to interact with computers and leverage their computing capabilities. Engineering design processes provide students with a context for applying and developing CT skills. Knowledge Building/Creation is a pedagogical approach that supports students to improve design ideas and products continuously. However, how students apply and develop CT skills through the engineering design process remains unclear, especially in a knowledge-creation community. This study collected design reports and presentation slides from 62 undergraduate students working in 13 small groups. Through manual coding, GPT-4 multilabel classification and narrative analysis, we examined what and how CT skills were demonstrated in the reports and slides and how playing the roles of designers and users influenced undergraduates' design. We found that the participants demonstrated five CT skills with differing frequencies and needed more support in troubleshooting; they could improve their design across the three design iterations. Having users in mind during design made them intentionally design more complex products while considering the design requirements. The findings suggested the need to specifically support students to troubleshoot and provide and receive feedback to improve their design further and the feasibility of using GPT to analyze CT skills manifested in students' reports.

**Решение:** -4 computational thinking skills in engineering education

---

### 534 · R7624

**USE OF SOCIAL LISTENING TO EXPLORE DIET-RELATED COMMENTARY FROM INFLAMMATORY BOWEL DISEASE SOCIAL MEDIA GROUPS**

2025 · Gastroenterology · journalarticle, review · https://doi.org/10.1053/j.gastro.2025.01.190

People with inflammatory bowel disease (IBD) desire dietary information. Social media groups are popular among this cohort to exchange dietary information. We aimed to capitalise on the large volume of commentary available in social media groups to determine frequently asked dietary questions and nutrition-related topics regarding this condition, utilising the Chat Generative Pre-trained Transformer 4 model (ChatGPT-4) to facilitate social listening analysis. Following ethical guidelines and the approval of Facebook group administrators, social listening techniques were used to extract 11,945 online community comments (from 2021-2023). All data was deidentified and cleaned according to ethical standards, ensuring only context-specific comments were included for analysis. The data was analysed using content and thematic analysis and ChatGPT-4. Thematic analysis was conducted in duplicate to explore the meaning of the comments. The ChatGPT-4 large language model was trained on 10% of manually coded data using the few-shot learning technique. Results from both manual and ChatGPT-4 coding were reviewed for congruence to ensure the artificial intelligence model was suitable and could then be applied to all data. Moderate percentage agreement existed between manual and model coded data (75%). Medical therapy (31.2%) and diet-related comments (37.5%) dominated the conversations. A total of 350 unique diet-related queries emerged. Content analysis of these indicated the most commonly mentioned diet-related topics were management of gastrointestinal/extraintestinal symptoms (37.8%), natural therapies/dietary approaches to manage/control symptoms (20%) and maintenance of nutritional status (5.6%). Thematic analysis indicated five interrelated themes: a desire for support and connection; exasperation and desire for information; open to considering advice from non-experts; a desire for food to be thy medicine and IBD holds me back. In this study, we utilised ChatGPT-4-enabled social listening of IBD Facebook groups and verified findings from this approach with traditional qualitative techniques. This approach reduced time and improved efficiency in extracting and exploring large volumes of qualitative information from a diverse sample. Future studies should establish methodological and reporting standards for artificial intelligence-enabled social listening to ensure comparability between studies. With respect to individuals with IBD, Facebook groups provided immediate access to information and connection, compensating for the perceived lack of timely access to a knowledgeable and empathetic multidisciplinary care team. Improving access to specialized professionals, including dietitians well-versed in IBD, could reduce reliance on these platforms as a primary source of information.

**Решение:** -4 diet commentary in inflammatory bowel disease social media groups

---

### 535 · R5332

**Doctor-Sun**

2026 · Zenodo · other/ · https://doi.org/10.5281/zenodo.18844968

# Doctor Sun: A bilingual multimodal large language model for biomedical AI A bilingual MLLM for biomedical AI ### Model Introduction **Doctor Sun**: a bilingual (Chinese-English) MLLM specifically designed to advance medical diagnostics across multiple specialties. Doctor Sun integrates three key components: a text foundation model for logical reasoning and clinical decision-making, a visual foundation model to extract image features and identify abnormalities in medical scans, and a cross-modal projector to align and map visual data into the textual semantic space. This architecture enables the seamless integration of imaging findings with clinical notes, providing a comprehensive understanding of patient conditions. The model is trained on a meticulously curated, high-quality bilingual dataset derived from public sources, encompassing radiology images, pathology slides, and clinical photographs, along with corresponding textual annotations in both Chinese and English. To ensure domain-specific expertise, the general-purpose language foundation model of Doctor Sun is first pre-trained and optimized to accumulate fundamental medical knowledge. Subsequently, the entire model undergoes a two-stage training strategy, focusing on feature alignment and instruction tuning, to achieve proficiency in multimodal medical diagnostic tasks while retaining general-purpose capabilities. At present, **Doctor Sun** is fine-tuned from **CLIP** and **LLaMA** of high-quality bilingual multi-modal medical data, and more data will be collected to expand the model's capabilities and iterate on the update. The details are being worked on, so stay tuned. ### Overview of the code and dataset This warehouse contains all the training and evaluation codes for Doctor Sun. The "xtuner.zip" file is a training code archive.The folder “llava” and eva.py contain the evaluation code. For the dataset, please refer to (https://www.modelscope.cn/datasets/Yanlan/Doctor-Sun-VL). It includes the complete pre-training and fine-tuning datasets.finetune.json: Fine-tuning text fileimage_finetune.zip: Fine-tuned image compression packagepretrain.json: Pre-trained text file image_pretrain.zip: Pre-trained Image Compression Package ### Dataset Information In the dataset repository, you can find the following files:finetune.json: Fine-tuning text fileimage_finetune.zip: Fine-tuned image compression packagepretrain.json: Pre-trained text file image_pretrain.zip: Pre-trained Image Compression Package All the datasets can be publicly downloaded. ### ‎Code Information The "xtuner.zip" file is a training code archive.The folder “llava” and eva.py contain the evaluation code. ### List of models | Model Name | weights | | :----: | :----: | | pretrain | [modelscope] / huggingface | | finetune | [modelscope](https://www.modelscope.cn/models/Yanlan/Doctor-Sun/files) / huggingface | ### List of datasets | dataset | link | | :----: | :----: | | pretrain | [modelscope](https://www.modelscope.cn/datasets/Yanlan/Doctor-Sun-VL) / huggingface | | finetune | [modelscope](https://www.modelscope.cn/datasets/Yanlan/Doctor-Sun-VL) / huggingface | ### How to use 1. Clone this repository and navigate```bashgit clone https://github.com/X-D-Lab/Doctor-Suncd Doctor-Sununzip xtuner.zip``` 2. Install Package```Shellconda create -n DoctorS python=3.10 -yconda activate DoctorSpip install --upgrade pip pip install -r requirements.txt```3. Quick Start # Pretrain ```ShellNPROC_PER_NODE=4 xtuner train ./xtuner/xtuner/configs/llava/llama3_8b_instruct_clip_vit_large_p14_336/pretrain/llava_llama3_8b_instruct_clip_vit_large_p14_336_e1_gpu8_sharegpt4v_pretrain --deepspeed deepspeed_zero2 --seed 1024``` # Finetune ```ShellNPROC_PER_NODE=4 xtuner ./xtuner/xtuner/configs/llava/llama3_8b_instruct_clip_vit_large_p14_336/finetune/llava_llama3_8b_instruct_full_clip_vit_large_p14_336_lora_e1_gpu8_internvl_finetune.py --deepspeed deepspeed_zero2 --seed 1024 cd ./xtuner/xtuner/configs/llava/llama3_8b_instruct_clip_vit_large_p14_336/finetune/work_dirs/llava_llama3_8b_instruct_full_clip_vit_large_p14_336_lora_e1_gpu8_internvl_finetunenum=23226xtuner convert pth_to_hf llava_llama3_8b_instruct_full_clip_vit_large_p14_336_lora_e1_gpu8_internvl_finetune ./iter_${num}.pth ./iter_${num}_xtuner xtuner convert merge /home/models/clip-vit-large-patch14-336 ./iter_${num}_xtuner/visual_encoder_adapter ./iter_${num}_visual_encoder --is-clip python ./xtuner/xtuner/configs/llava/llama3_8b_instruct_clip_vit_large_p14_336/convert_xtuner_weights_to_llava.py --text_model_id ./iter_${num}_xtuner --vision_model_id ./iter_${num}_visual_encoder --projector_weight ./iter_${num}_xtuner/projector/model.safetensors --save_path ./iter_${num}_llava```The model "clip-vit-large-patch14-336" needs to be downloaded to a specific location in advance. 4. Evaluation Refer to the file "eva.py", which is used to evaluate the QA task. With a few simple modifications, it can also be used to evaluate the VQA task. ```Shellpython eva.pyorHF_ENDPOINT=https://hf-mirror.com python eva.py``` 5. Acknowledgment Our training utilized the code from xtuner, and we would like to express our gratitude for this.```@misc{2023xtuner, title={XTuner: A Toolkit for Efficiently Fine-tuning LLM}, author={XTuner Contributors}, howpublished = {\url{https://github.com/InternLM/xtuner}}, year={2023}}``` ### 引用 ``` @misc{2024Doctor-Sun, author={Dong Xue*, Ziyao Shao, Zhaoyang Duan, Fangzhou Liu, Bing Li, and Zhongheng Zhang*}, title = {Doctor Sun: A Bilingual Multimodal Large Language Model for Biomedical AI}, year = {2024}, publisher = {GitHub}, journal = {GitHub repository}, howpublished = {\url{https://github.com/X-D-Lab/Doctor-Sun/}}, }```

**Решение:** -4 Doctor Sun biomedical multimodal LLM release

---

### 536 · R7526

**Creative and depressive profiles shape divergent thinking in emotion regulation idea generation.**

2025 · Scientific reports · journal article, journalarticle, article · eng · https://doi.org/10.1038/s41598-025-32365-4

Emotion regulation (ER) is a multi-faceted process, though its generative component––wherein one ideates situation-specific regulatory options (“techniques”)––is poorly understood. Through a novel task (ERGen), we evaluated ER repertoires based on the techniques that individuals generate to regulate their emotional response to negative scenarios. We hypothesized these repertoires to be sensitive to creative (divergent-thinking originality) ability and depression symptoms in our online adult sample (N = 143). Human raters and a generative pre-trained transformer (GPT-4o) coded each generated technique (n = 7854) into one of 14 regulatory strategies to model repertoire richness (strategy diversity) and size (technique count). Individuals higher in creativity showed more prolific technique generation across many strategies, whereas individuals with more depressive symptoms showed altered generation within specific strategies, and reduced deviation from habitual ER tendencies. These findings highlight an untapped research sphere that can motivate new intervention targets in affective disorders, including divergent-thinking ability.

**Решение:** + T1 GPT-4o and human raters coding emotion regulation strategies into 14 categories (ERGen)

---

### 537 · R9354

**Brand Displacement: The Case for Mimetic Brand Placement in Media**

2025 · Spectrum Research Repository (Concordia University) · dissertation · en

As audiences continue to become more aware of marketing practices, brand placement in media is starting to disrupt the fragile transportive state normally brought on by compelling stories. Artists who want to distance their work from advertising yet still imbue their work with a sense of verisimilitude are increasingly leveraging the trade dress of recognizable brands. They modify existing brands to fill in their worlds with familiar images without using their real names or likenesses. Comprising two experimental studies, this doctoral research is the first to name and examine the effects of “mimetic brand placement” in media. By manipulating conditions of brand placement and narrative transportation, the results of the first study suggested that mimetic brands may be as effective or outperform real ones as unintrusive product placements. Not being immediately recognizable as advertisements, mimetic brands preserve audiences’ experiences without triggering the substantial defense mechanisms they have developed against persuasive marketing tactics. The second study reframed the research to center on preserving the interests of all key stakeholders: audiences, brands, and the studios that implement the placements. Employing qualitative and quantitative methodologies, the results revealed that transparently disclosing the placement of mimetic brands prior to a media experience led to more positive outcomes for all three parties relative to a deceptive framing. Through the lens of Service-Dominant Logic, mimetic brands are positioned as a collaborative tool through which long-term, mutually beneficial relationships may be cultivated and maintained between these groups. This dissertation also examined similar brands created by generative artificial intelligence models and the latent biases present therein. Ethical considerations at the intersection of mimetic branding and AI research are discussed. Mimetic brands pose important practical and ethical implications for brands and audiences, alike. With thoughtful and transparent implementation, they may represent a new middle ground between narrative content and advertising.

**Решение:** -4 mimetic brand placement in media

---

### 538 · R10264

**The Role of ChatGPT in Enhancing Argumentative Writing Skills of EFL Students through Formative Feedback**

2025 · Proceeding of Undergraduate Conference on Literature Linguistic and Cultural Studies · article · en · https://conference.untag-sby.ac.id/index.php/uncollcs/article/download/6175/3574

This research aims to analyze the role of ChatGPT’s formative feedback in improving the quality of EFL Students’ argumentative essay writing. The methodology involved a quantitative design with pre-feedback and post-feedback argumentative essays written by 31 participants. These essays were assessed by the argumentative writing rubric from SERP Institute which focusing in four aspects; argumentation, evidence, organization, and language. Scores were rated by two raters, with high interrater reliability confirmed by ICC value of .950. The result of this research revealed statistically improvement in the rating of argumentative essays after receiving formative feedback from ChatGPT, with the evidence aspect showing the highest mean increase (5.8387 points). This is based on the .Sig value of paired sample test of .000, it shows a significant improvement. Additionally, based on the interview responses, it is revealed that after utilizing the feedback from ChatGPT, the participants’ overall showed positive perceptions of ChatGPT, highlighting its usefulness in identifying weaknesses, improving structure, and generating ideas, although students noted that clear prompts were necessary. Keywords: Argumentative Writing, ChatGPT, EFL Learners, Formative Feedback, Interrater Reliability

**Решение:** -4 ChatGPT feedback on EFL argumentative essay writing

---

### 539 · R1615

**The unsupervised deployment gap in generative AI for mental health**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.22779992

Evidence about artificial intelligence in mental health and the deployment of artificial intelligence in mental health concern two different objects, and the first is routinely cited to justify the second. The evidence base is forty randomized trials pooling to g = 0.31 for depressive symptoms and g = 0.28 for anxiety, with 35 of 39 trials at high risk of bias, significant publication bias, and only 8 trials testing a generative system. The one randomized trial of a fully generative therapy chatbot enrolled 210 adults for four weeks, ran on Falcon-7B and LLaMA-2-70B, had clinicians review every response, and excluded active suicidality, mania and psychosis, turning away 215 people for suicide risk while enrolling 210 in total. Recomputing that trial's effect sizes from its own published means and standard deviations gives standardized mean differences of 0.45 to 0.62 against reported values of 0.63 to 0.90. Deployment is three orders of magnitude larger. The operator of the most widely used general assistant estimates that in a given week 0.15% of active users have conversations containing explicit indicators of suicidal planning or intent and 0.07% show possible signs of psychosis or mania. Against 800 million weekly active users that describes roughly a million people every week. This paper proposes a taxonomy of four deployment classes defined by design intent, regulatory claim, population gate, supervision and exposure, and shows that evidentiary strength and population exposure run in opposite directions across them. It argues that sycophancy in this setting is a problem of reward specification rather than a defect of alignment: therapeutic benefit cannot be observed inside a conversation, user approval can, and expert clinicians agree on whether a response is desirable only 71% to 77% of the time. It identifies two regulatory inversions in the four United States statutes passed since March 2025, and proposes psychovigilance: version identity, reporting attached to function rather than claim, independent access to logs, and outcome measurement at the level of whole conversations.

**Решение:** -1 perspective/policy paper on unsupervised deployment gap in mental health AI

---

### 540 · R11699

**Can AI Understand Human Personality? -- Comparing Human Experts and AI Systems at Predicting Personality Correlations**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2406.08170

We test the abilities of specialised deep neural networks like PersonalityMap as well as general LLMs like GPT-4o and Claude 3 Opus in understanding human personality. Specifically, we compare their ability to predict correlations between personality items to the abilities of lay people and academic experts. We find that when compared with individual humans, all AI models make better predictions than the vast majority of lay people and academic experts. However, when selecting the median prediction for each item, we find a different pattern: Experts and PersonalityMap outperform LLMs and lay people on most measures. Our results suggest that while frontier LLMs' are better than most individual humans at predicting correlations between personality items, specialised models like PersonalityMap continue to match or exceed expert human performance even on some outcome measures where LLMs underperform. This provides evidence both in favour of the general capabilities of large language models and in favour of the continued place for specialised models trained and deployed for specific domains. 45 pages, 6 figures

**Решение:** -6 predicting correlations between personality test items

---

### 541 · R8953

**Merger-as-a-Stealer: Stealing Targeted PII from Aligned LLMs with Model Merging**

2025 · Conference on Empirical Methods in Natural Language Processing (EMNLP) · conference-paper · en · https://doi.org/10.18653/v1/2025.emnlp-main.295

Model merging has emerged as a promising approach for updating large language models (LLMs) by integrating multiple domain-specific models into a cross-domain merged model. Despite its utility and plug-and-play nature, unmonitored mergers can introduce significant security vulnerabilities, such as backdoor attacks and model merging abuse. In this paper, we identify a novel and more realistic attack surface where a malicious merger can extract targeted personally identifiable information (PII) from an aligned model with model merging. Specifically, we propose \texttt{Merger-as-a-Stealer}, a two-stage framework to achieve this attack: First, the attacker fine-tunes a malicious model to force it to respond to any PII-related queries. The attacker then uploads this malicious model to the model merging conductor and obtains the merged model. Second, the attacker inputs direct PII-related queries to the merged model to extract targeted PII. Extensive experiments demonstrate that \texttt{Merger-as-a-Stealer} successfully executes attacks against various LLMs and model merging methods across diverse settings, highlighting the effectiveness of the proposed framework. Given that this attack enables character-level extraction for targeted PII without requiring any additional knowledge from the attacker, we stress the necessity for improved model alignment and more robust defense mechanisms to mitigate such threats.

**Решение:** -4 model merging PII extraction security vulnerability

---

### 542 · R6634

**SatBadEdit: Towards Efficient and Robust Multi-Trigger Backdoor Injection in Large Language Models**

2026 · IEEE International Conference on Acoustics Speech and Signal Processing · conference-paper · https://doi.org/10.1109/icassp55912.2026.11464407

Efficient and stealthy backdoor injection into Large Language Models (LLMs) remains a critical challenge. While recent model editing techniques offer an efficient alternative to traditional fine-tuning, they are often limited to injecting a few triggers and demonstrate poor robustness against state-of-the-art defenses. To overcome this limitation, we introduce SatBadEdit, a novel saturation-based model editing for implanting a large volume of backdoors with high adversarial strength. SatBadEdit uniquely leverages batch editing capabilities to inject numerous triggers in a single, highly efficient operation. To counteract the potential model instability from this massive injection, we devise a low-rank weight update and aggregation strategy. This mechanism confines parameter modifications to a sparse, low-dimensional subspace, ensuring minimal model disruption while maximizing trigger effectiveness and stability. Extensive experiments demonstrate that SatBadEdit not only surpasses existing fine-tuning and editing-based attacks in efficiency and stealth but also maintains a significantly higher attack success rate under a suite of prominent defense mechanisms, setting a new benchmark for robust LLM backdooring.

**Решение:** -4 backdoor injection in LLMs

---

### 543 · R8349

**Toward Sensor-to-Text Generation: Leveraging LLM-Based Video Annotations for Stroke Therapy Monitoring.**

2025 · Bioengineering (Basel, Switzerland) · journal article, journalarticle, article · eng · https://doi.org/10.3390/bioengineering12090922

Stroke-related impairment remains a leading cause of long-term disability, limiting individuals' ability to perform daily activities. While wearable sensors offer scalable monitoring solutions during rehabilitation, they struggle to distinguish functional from non-functional movements, and manual annotation of sensor data is labor-intensive and prone to inconsistency. In this paper, we propose a novel framework that uses large language models (LLMs) to generate activity descriptions from video frames of therapy sessions. These descriptions are aligned with concurrently recorded accelerometer signals to create labeled training data. Through exploratory analysis, we demonstrate that accelerometer signals exhibit distinct temporal and statistical patterns corresponding to specific activities, supporting the feasibility of generating natural language narratives directly from sensor data. Our findings lay the foundation for future development of sensor-to-text models that can enable automated, non-intrusive, and scalable stroke rehabilitation monitoring without the need for manual or video-based annotation.

**Решение:** -4 wearable sensors and video annotation in stroke motor therapy

---

### 544 · R0489

**The Metrology Imperative: The Necessity of Robust Evaluation Frameworks and Comprehensive Automated Judges in Generative AI**

2026 · International Journal of Intelligent Systems and Applications in Engineering · journalarticle/, article · en · https://doi.org/10.17762/ijisae.v14i1s.8188

Across the past several years, the accelerating advancement of Large Language Models (LLMs) and generative artificial intelligence has quietly produced a crisis that much of the field has been slow to name directly—a breakdown in the ability to evaluate what these systems can and cannot actually do. Traditional, static benchmarking methodologies have proven structurally inadequate, collapsing under the combined weight of rapid benchmark saturation, pervasive data contamination, and the kind of systematic overfitting that emerges whenever commercial incentives are tied too tightly to leaderboard rankings. This brief argues, with considerable urgency, that building robust and dynamic evaluation frameworks alongside sophisticated automated judges—most prominently through the LLM-as-a-Judge paradigm—is not an optional enhancement to existing practices but an absolute prerequisite for the continued, safe, and value-aligned development of AI systems. Through a careful examination of where current evaluation practices fail, an analysis of the architectural requirements governing automated multi-agent juries, and a survey of multi-dimensional safety assessment approaches, a coherent pathway toward genuinely reliable AI metrology is charted here. The arguments and architectural outlines presented across these sections are intended to serve as a structured foundational blueprint for a full-length 40-page journal article that will pursue the theoretical, empirical, and architectural dimensions of this problem in considerably greater depth. DOI: https://doi.org/10.17762/ijisae.v14i1s.8188

**Решение:** -1 perspective on evaluation frameworks in generative AI

---

### 545 · R6287

**Safety, Accuracy, Empathy, Reliability, and Readability of Responses From Large Language Models to Public-Facing Questions About Nutrition in Hepatocellular Carcinoma: A Comparative Study (Preprint)**

2026 · JMIR Publications Inc. · preprint · https://doi.org/10.2196/preprints.107565

BACKGROUND Patients with hepatocellular carcinoma (HCC) and their caregivers increasingly use large language models (LLMs) to obtain nutrition-related information. However, the safety and quality of such information remain uncertain, particularly because HCC frequently coexists with cirrhosis, sarcopenia, ascites, hepatic encephalopathy, treatment-related adverse effects, and potential food–drug interactions. OBJECTIVE To compare the safety, accuracy, empathy, reliability, information quality, and readability of responses generated by five publicly accessible chatbots to public-facing questions about nutrition in HCC. METHODS This cross-sectional comparative study evaluated ChatGPT, Gemini, Microsoft Copilot, Doubao, and DeepSeek using 62 standardized English-language questions about HCC-related nutrition. Each question was submitted to each model in a new conversation through its official web interface between June 2 and 6, 2026. Five evaluators independently assessed safety, accuracy, and empathy and evaluated reliability and information quality using DISCERN, Ensuring Quality Information for Patients (EQIP), the Journal of the American Medical Association (JAMA) benchmark criteria, and the Global Quality Score (GQS). Six automated indices were used to assess readability. Model comparisons were conducted using paired question-level analyses. RESULTS A total of 310 responses were analyzed. Inter-rater agreement was high, with a Fleiss κ of 0.862 for safety and ICC(2,1) values ranging from 0.846 to 0.888 for the other rater-scored outcomes. Overall, 263 responses were classified as safe and 47 as potentially unsafe. Safe response rates were 91.9% for ChatGPT, 85.5% for Gemini, 83.9% for Copilot, 79.0% for DeepSeek, and 83.9% for Doubao. The overall difference in safety was not statistically significant. Accuracy, empathy, reliability, information quality, and readability differed significantly across chatbots. Potentially unsafe responses most commonly involved incomplete escalation advice, insufficient qualification of general advice, overgeneralized dietary or supplement recommendations, and inadequate attention to food safety or food–drug interaction risks. CONCLUSIONS Across this standardized set of public-facing HCC nutrition questions, most responses generated by the evaluated chatbots were classified as safe; however, potentially unsafe or insufficiently qualified advice was identified in clinically relevant scenarios. LLM-generated nutrition information may supplement general patient education but should not replace individualized guidance from oncologists, hepatologists, pharmacists, or dietitians. Future system development should prioritize clear advice on when red-flag symptoms require urgent clinical assessment, clinically appropriate qualification, source transparency, and plain-language communication. </sec

**Решение:** -4 LLM answers on nutrition in hepatocellular carcinoma

---

### 546 · R7911

**Validity at Risk? the Future of Generative AI Use by Candidates in Assessments**

2025 · International Journal of Selection and Assessment · journalarticle, article · en · https://doi.org/10.1111/ijsa.70035

ABSTRACT In this commentary on Lievens and Dunlop (2024), we critically evaluate the implications of candidate GenAI use from the perspectives of criterion‐ and construct‐related validity. While the focal article provides valuable scenarios for understanding the role of GenAI use by candidates, we argue it may underestimate the speed of technological development and overstate the generalizability of augmentation across all job types. By considering increasing GenAI accessibility, we highlight how ease of use may weaken the diagnostic value of GenAI‐related variance in assessments. Furthermore, we propose experimental paradigms to empirically investigate the impact of GenAI on criterion‐ and construct‐related validity by framing GenAI as either an impersonator or an assistant. Finally, we reflect on a future where GenAI agents may challenge existing conceptions of construct validity, calling for a rethinking of the way we define and measure psychological constructs in the age of AI.

**Решение:** -1 commentary on GenAI use by candidates in employment assessments

---

### 547 · R1426

**SciSchema.org: A Multidisciplinary Collection of Schemas for Structured Scientific Process Descriptions**

2026 · Research Square · journalarticle, review, preprint · https://doi.org/10.21203/rs.3.rs-10535364/v1

Abstract Scientific processes are often described in heterogeneous article discourse, with details needed for comparison, reproducibility, reuse, and automation dispersed across prose, tables, figures, protocols, and supplementary files. We present the first release of SciSchema.org, a multidisciplinary collection of 16 expert-annotated schemas spanning Biology & Biotechnology, Materials & Chemistry, Imaging & Measurement, Physics, and Psychology. Each schema defines reusable fields for describing process instances, including inputs, outputs, materials, instruments or software, parameters, conditions, procedural steps, measurements, and provenance-related information. The schemas were created through a human-in-the-loop schema-mining workflow in which large language models generated candidate structures from process specifications, scientific articles, and expert feedback, followed by domain-expert construction of final master schemas. The dataset contains final schemas in JSON Schema and SHACL formats, intermediate model-generated schemas, expert-feedback records, source-paper metadata, community-development materials, and analysis scripts. Technical validation assessed schema structure, development provenance, expert review, and syntactic conformance. The collection supports structured annotation, metadata enrichment, scientific knowledge graphs, information extraction, semantic publishing, and cross-study comparison.

**Решение:** -4 SciSchema.org scientific process schemas

---

### 548 · R12005

**GenSQLi: A Generative Artificial Intelligence Framework for Automatically Securing Web Application Firewalls Against Structured Query Language Injection Attacks**

2024 · Future Internet · journalarticle, article · en · https://doi.org/10.3390/fi17010008

The widespread adoption of web services has heightened exposure to cybersecurity threats, particularly SQL injection (SQLi) attacks that target the database layers of web applications. Traditional Web Application Firewalls (WAFs) often fail to keep pace with evolving attack techniques, necessitating adaptive defense mechanisms. This paper introduces a novel generative AI framework designed to enhance SQLi mitigation by leveraging Large Language Models (LLMs). The framework achieves two primary objectives: (1) generating diverse and validated SQLi payloads using in-context learning, thereby minimizing hallucinations, and (2) automating defense mechanisms by testing these payloads against a vulnerable web application secured by a WAF, classifying bypassing attacks, and constructing effective WAF security rules through generative AI techniques. Experimental results using the GPT-4o LLM demonstrate the framework’s efficacy: 514 new SQLi payloads were generated, 92.5% of which were validated against a MySQL database and 89% of which successfully bypassed the ModSecurity WAF equipped with the latest OWASP Core Rule Set. By applying our automated rule-generation methodology, 99% of previously successful attacks were effectively blocked with only 23 new security rules. In contrast, Google Gemini-Pro achieved a lower bypass rate of 56.6%, underscoring performance variability across LLMs. Future work could extend the proposed framework to autonomously defend against other web attacks, including Cross-Site Scripting (XSS), session hijacking, and specific Distributed Denial-of-Service (DDoS) attacks.

**Решение:** -4 SQL injection defense with GenAI

---

### 549 · R4171

**Fine-tuning a multimodal large language model for clinician-grade autism behavioral scoring from short home videos**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.27484

Autism spectrum disorder (ASD) affects 1 in 31 US children, yet median age at diagnosis exceeds four years. Artificial intelligence pipelines that provide quantified diagnosis using easy to access observational data (e.g., home videos) could help with earlier diagnosis, and timely delivery of early treatments. We fine-tuned Gemini 2.5 Pro on 400 clinician-rated home videos with low-rank adaptation, training only on 30 behavioral features previously validated to produce reliable predictions when passed to various ML models. On 99 held-out children (49 ASD, 50 neurotypical), inter-rater reliability with clinicians (per-feature weighted Cohen's kappa) improved by 40% (p&lt;0.001), with 27 of 28 evaluable features improving. As an emergent zero-shot capability, direct ASD diagnosis F1 improved by 53% (p&lt;0.001), matching or exceeding clinician outcomes. Classifier-assisted pipelines using fine-tuned LLM-derived behavioral features matched clinician-scored inputs across all tested pathways and achieved 77% accuracy (95% CI: 68-85%) and an AUC of 86% (95% CI: 78-92%). Fine-tuned multimodal LLMs can serve as scalable behavioral feature extractors for use in autism assessment and diagnosis.

**Решение:** ? T3 multimodal behavioral scoring of autism from videos vs clinician ratings; check text component

---

### 550 · R2311

**MemeBridge: A Dataset for Benchmarking and Mitigating the Bidirectional Cultural Gap in Meme Interpretation**

2026 · ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD) · book, journalarticle, conference · https://doi.org/10.1145/3770854.3785691

Communicating across cultures is inherently challenging, especially through culturally dense and ambiguous formats like memes. While people expect large language models (LLMs) to hold promise for bridging such gaps, existing benchmark datasets often fail to capture the cultural context necessary for accurate interpretation. To address this, we introduce MemeBridge, a curated dataset centered on U.S.-originated memes, designed to capture two complementary perspectives: (1) how Chinese participants interpret these memes, and (2) how U.S. participants anticipate how people from other cultures might misunderstand them. Here, context refers to implicit cultural knowledge, including background beliefs, norms, and shared assumptions that shape meme comprehension. The dataset was constructed via a multi-stage crowdsourcing pipeline with rigorous validation, including human agreement checks and GPT-based classification verification. Each meme is annotated with sentiment, emotion, cultural significance, and knowledge type, providing rich supervision for downstream tasks. Notably, we observe that the anticipated misunderstandings from U.S. participants are often inaccurate, highlighting the asymmetries in cultural understanding and the challenges of adopting perspectives beyond one's own. This bidirectional framing, which focuses on both expression and perception, enables more nuanced benchmarking of cross-cultural comprehension. Our probing of multiple LLMs reveals that while models developed in different cultural contexts exhibit partial cross-cultural understanding, they often struggle with sophisticated interpretations. By contrast, fine-tuning with MemeBridge improves model performance, underscoring the value of culturally grounded resources for training and evaluating LLMs in globally diverse settings.

**Решение:** -4 MemeBridge: cultural gap in meme interpretation

---

### 551 · R8903

**Comparing AI chatbot simulation and peer role-play for OSCE preparation: a pilot randomized controlled trial.**

2025 · BMC medical education · journal article, randomized controlled trial, journalarticle · eng · https://doi.org/10.1186/s12909-025-08308-y

BACKGROUND: Artificial intelligence (AI) is increasingly applied in medical education, but its role in fostering interactive clinical competencies remains underexplored. This pilot study aimed to compare the feasibility and educational impact of an AI chatbot-based simulation with traditional peer role-play (PRP) for Objective Structured Clinical Examination (OSCE) preparation, and to share practical lessons from implementing a novel AI tool in a trial setting. METHODS: Nineteen final-year Korean medicine students were randomly assigned to either an AI chatbot group (n = 9) or a PRP group (n = 10) after a baseline knowledge test. Both groups underwent a 30-minute physical examination practice session, followed by a one-hour clinical interview training session specific to their group. The AI chatbot group practiced with a GPT-4o/Claude 3.5-based chatbot providing scenario-driven responses and automated feedback, while the PRP group practiced in pairs under tutor supervision. All participants then completed two OSCE stations (dizziness and shoulder pain). Performance was assessed using a structured checklist covering four domains: history taking, physical examination, patient education, and physician-patient interaction. Post-study questionnaires evaluated the learning experience. RESULTS: Although the differences in OSCE scores between the groups did not reach statistical significance, several interesting and complementary trends were observed. For example, the PRP group tended to score higher in history taking (mean 74.4 vs. 66.2 in dizziness scenario; Hedges' g = -0.68, mean 58.6 vs. 54.5 in shoulder pain scenario; Hedges' g = -0.21), while the AI chatbot group showed a tendency towards higher scores in patient education (32.5 vs. 22.2 in dizziness scenario Hedges' g = 0.44, 85.0 vs. 66.7 in shoulder pain scenario; Hedges' g = 0.99). Survey results reflected these following trends. The PRP group valued the authenticity of the interaction and the exam-like environment. In contrast, the AI chatbot group reported higher satisfaction with the autonomy, opportunity for repetitive practice, and structured feedback. CONCLUSION: In this pilot study, AI chatbot-based training and PRP demonstrated complementary strengths for OSCE preparation. While PRP appears effective for developing performance-based procedural and communication skills in a realistic setting, AI chatbots show potential for fostering clinical reasoning in a self-paced, reflective learning environment. These complementary strengths suggest a blended learning model, combining both methods, may be optimal for holistic clinical skills development. Further research is needed to validate these preliminary findings.

**Решение:** -4 AI chatbot simulation for medical OSCE exam preparation

---

### 552 · R1283

**Can Intelligent Agents Revolutionize Scale Generation?**

2026 · conference-paper · https://doi.org/10.18653/v1/2026.findings-acl.1674

Measurement scales play a crucial role in quantifying the nuanced dimensions of human cognition and behavior, however, their development typically demands extensive manual labor, and current methodologies lack systematic automation and standardized evaluation.In this paper, we introduce AutoScale, a pioneering multi-agent framework that automates scale development by leveraging collaborative AI agents.Our contributions are threefold:(1) a novel multi-agent LLM-based framework for end-to-end scale generation that replicates expert collaboration and iterative datadriven refinement, (2) the first comprehensive dataset, SCALE-1.2K,comprising 1.2K validated scales across 16 psychological domains, establishing a benchmark for automated scale development, and (3) a multi-dimensional evaluation system, featuring Muti-LLM-as-judge for conceptual and linguistic assessment and simulated large-scale testing for rigorous psychometric verification.Experimental results demonstrate that AutoScale streamlines the scale development process while maintaining rigorous quality standards, significantly reducing manual effort and paving the way for more efficient and objective measurement design in diverse research fields.

**Решение:** -4 automated scale and item generation for psychometric tests

---

### 553 · R8050

**Mapping Meaning in Latin with Large Language Models:A Multi-Task Evaluation of Preverbed Motion Verbs and Spatial Relation Detection in LLMs**

2025 · Research Portal (King's College London) · conference-paper · en · https://kclpure.kcl.ac.uk/ws/files/352408655/42_main_long.pdf

This paper evaluates the capabilities of Large Language Models (LLMs) on three interrelated linguistic tasks in Latin: preverbed motion verb identification, spatial relation (SR) classification, and SR type disambiguation. We evaluate GPT-4, Llama, and Mistral under zero-shot and few-shot settings, using a manually annotated dataset of Latin sentences drawn from different authors, text types, and historical periods (3rd century BCE – 2nd century CE) as our gold standard. Results show that GPT-4 consistently outperforms open-weight models, particularly in zero-shot scenarios, likely due to its substantial pretraining exposure to Latin. However, even GPT-4 struggles with syntactic disambiguation, especially in linking proper nouns to their governing verbs. SR classification performance is skewed by dataset imbalance, and SR type disambiguation errors often stem from over-reliance on salience over syntax. Qualitative analysis reveals common patterns of overgeneration and uncertainty across tasks. Our findings underscore the potential of LLMs for historical language processing while highlighting persistent challenges related to ambiguity, entity linking, and syntactic reasoning. This study represents the first evaluation of SR recognition in historical languages and lays the groundwork for future domain-adapted fine-tuning approaches in Computational Humanities.

**Решение:** -4 Latin motion verbs and spatial relation detection

---

### 554 · R0140

**Timelines Over Tokens**

2026 · dissertation · https://doi.org/10.31979/etd.ewrn-xhac

This research presents a two-stage pipeline for user-level suicide risk detection from Reddit: first, inference-only prompting with summarization; second, fine-tuned encoder classification with explainability and expert validation. The data are user-level: each of the 500 C-SSRS Reddit items is one user’s chronologically concatenated posts and comments (a user timeline), annotated by psychiatrists. Stage one: six prompting strategies zero-shot, few-shot, chain-of-thought, tree-of-thought, least-to-most, and self-consistency are evaluated across six LLMs on multi-class and binary formulations; simple zero-shot achieves the highest balanced accuracy (0.53 multi-class). Error analysis shows longer inputs associate with misclassification (p = 0.002); domain-specific summarization (timelines >2,000 tokens) reduces length by 44%, preserves semantic fidelity (BERTScore F1 = 0.85), improves smaller models (up to 10%), and yields roughly 32% cost savings. Classical baselines (best BA = 0.31) underscore LLM advantages. Stage two: the mental-longformer-base-4096 encoder is fine-tuned on summarized C-SSRS and eRisk 2025 timelines for binary (risk vs. no risk) classification. A 7-configuration ablation over C-SSRS, eRisk, and ReDSM5 motivates the C-SSRS+eRisk main model (mean BA 0.89±0.01; best 0.90), with zero-shot transfer to external datasets (e.g., Twitter BA 0.85, ROC-AUC 0.92). Integrated Gradients and attention visualizations provide token-level explanations; three independent clinicians rate clinical-style summaries of model rationales (84% majority agreement). Multi-class addresses granularity; binary and fine-tuning address robustness. Deployment requires large-scale validation, fairness assessment, and human oversight.

**Решение:** + T3 user-level suicide risk detection from Reddit timelines (C-SSRS) across 6 LLMs vs psychiatrist annotations

---

### 555 · R3102

**Integrating patient narratives and clinical indicators for monitoring suicidal ideation in adolescents with major depressive disorder: a human-in-the-loop validation study of LLM-assisted journaling**

2026 · BMC Psychiatry · journalarticle, review, article · en · https://doi.org/10.1186/s12888-026-08700-y

Abstract Background Suicide-related distress in adolescents with major depressive disorder (MDD) can fluctuate between outpatient visits and may not be fully disclosed during brief encounters. Patient-generated diary narratives may capture daily emotional context, whereas structured psychiatric indicators provide standardized clinical information. We evaluated whether integrating these sources within a clinician-supervised, large language model (LLM)-assisted journaling workflow could support between-visit monitoring. Methods We conducted an observational validation study in 108 adolescents and young patients with DSM-5-TR-diagnosed MDD receiving outpatient care in the Republic of Korea. Cross-sectional analyses used the first diary per participant; sensitive-topic evaluation used all 709 valid entries. Structured measures assessed suicidal ideation, depressive symptoms, anxiety, and perceived stress. The self-report outcome was Patient Health Questionnaire (PHQ)-9 item 9 positivity (scores 1–3 versus 0). We evaluated patient-level associations, cross-sectional classification with and without diary narratives, exploratory longitudinal classification across repeated entries, and sensitive-topic detection against clinician annotation. GPT-4o and DeepSeek-V3 were benchmarked against blinded mental health professionals. The integrated MindfulDiary workflow combined pre-journaling screening, in-journaling LLM detection, and clinician alerting. Results Participants had a mean age of 15.8 years; 58 (53.7%) were female. In patient-level logistic regression, Scale for Suicide Ideation (odds ratio 1.15, 95% CI 1.02–1.28) and depressive symptoms (odds ratio 1.09, 95% CI 1.00-1.19) were associated with PHQ-9 item 9 positivity. Adding diary narratives to depressive symptom scores improved F1-score from 0.79 to 0.81 for GPT-4o and from 0.74 to 0.78 for DeepSeek-V3. In the primary aggregate longitudinal analysis, performance increased with diary count for both LLMs. A sensitivity analysis using the same 16 participants across diary counts showed positive associations for both LLMs and mental health professionals. For clinician-annotated in-journaling sensitive topics, LLM detection achieved an F1-score of 0.85. The integrated workflow captured 193/197 composite-positive entries (98.0%; F1-score 0.96). Conclusions Patient-generated narratives and structured psychiatric indicators provided complementary signals for monitoring PHQ-9 item 9 positivity and clinician-reviewed sensitive content in adolescent MDD. LLM-assisted journaling may support clinician-supervised monitoring but is not an autonomous suicide-risk classifier. Evaluation across sites and languages, prospective studies, and patient-centered evaluation are needed before routine adoption. Trial registration Not applicable; the study was not registered.

**Решение:** + T3/T1 suicidal ideation and sensitive topic detection in adolescent MDD diaries: LLMs vs mental health professionals

---

### 556 · R1207

**Artificial Intelligence–Enhanced Virtual Reality in English as a Foreign Language Teaching: Instructor Experiences and Pedagogical Orchestration**

2026 · HAYEF Journal of Education · journalarticle, article · https://doi.org/10.5152/hayef.2026.26063

Artificial intelligence is increasingly reshaping immersive educational environments; yet, empirical attention to its integration with virtual reality in English as a foreign language teaching remains limited. This qualitative descriptive study examined how English as a foreign language instructors perceived, implemented, and evaluated artificial intelligence– enhanced virtual reality activities in their teaching practices. The study was conducted in Türkiye with eight English as a foreign language instructors from two universities who had prior experience using virtual reality-based or virtual reality- compatible artificial intelligence–supported speaking, role-play, and communication activities. Data were collected through eight semi-structured interviews and five optional stimulated-recall sessions based on short lesson-recording excerpts or demonstration recordings. The data were analyzed through inductive qualitative content analysis supported by a large language model–assisted preliminary open-coding process, followed by manual code refinement, codebook development, peer debriefing, member checking, and intercoder reliability procedures. The analysis generated five interpretive themes: from scripted simulation to contingent conversation, lowering the social cost of speaking, classroom realism without real-world risk, orchestrating classroom visibility and fragile infrastructure, and pedagogically accountable artificial intelligence–virtual reality adoption. Instructors viewed artificial intelligence–enhanced virtua reality as pedagogically promising because, in their accounts, it enabled learners to converse with responsive computergenerated agents, increased engagement and attendance, supported lower-pressure speaking practice, and created opportunities for real-life communication. However, they also emphasized practical and pedagogical constraints related to institutional Wi-Fi authentication, mobile hotspot instability, headset management, screen-casting, projection quality, classroom visibility, task alignment, and the need for teacher mediation of automated feedback. The study suggests that the value of artificial intelligence–enhanced virtual reality in English as a foreign language teaching depends less on technological novelty than on instructional design, institutional readiness, and sustained teacher professional development. Cite this article as: Karacan, C. G., & Can, T. (2026). Artificial intelligence–enhanced virtual reality in English as a foreign language teaching: Instructor experiences and pedagogical orchestration. HAYEF: Journal of Education, 23, 0063, doi: 10.5152/hayef.2026.26063.

**Решение:** -4 virtual reality in EFL teaching

---

### 557 · R4365

**Beyond Labels: Training Cognitive Empathy with Context-Rich Synthetic Dialogues**

2026 · UF Journal of Undergraduate Research · journalarticle, article · https://doi.org/10.32473/ufjur.28.141683

As Large Language Models (LLMs) are increasingly deployed in emotionally sensitive applications like mental health support, the need for genuine artificial empathy has become critical. Existing conversational datasets often fail to instill deep cognitive empathy, instead promoting superficial affective mimicry. To address this gap, we introduce RelationalDialogues, a novel, fully synthetic dataset of 12,849 multi-turn dialogues designed to explicitly train perspective-taking. Using a 120-billion parameter LLM, we developed a data generation pipeline that grounds each conversation in structured metadata, including distinct speaker/listener backgrounds, situational stimuli, and relationship dynamics derived from a psychologically justified emotion taxonomy. A key feature of our methodology is blinding the "listener" agent to the explicit emotion label during generation, forcing it to infer emotional states from conversational context alone. We fine-tuned a Llama-3-8B-Instruct model on this corpus and evaluated it against its base counterpart using an LLM-as-a-Judge framework across three dimensions: Emotion Recognition, Perspective-Taking, and Emotional Contagion. Our fine-tuned model achieved a 51.05% win rate over the base model (45.53%) and demonstrated statistically significant improvements, particularly in Perspective-Taking (average score increase from 3.06 to 3.22) and Emotional Contagion (2.96 to 3.09). Granular analysis reveals the fine-tuned model excels at navigating nuanced, socially complex emotions like loneliness and jealousy, whereas the base model relies on pre-programmed templates for high-arousal emotions. These findings demonstrate that training on highly contextualized, metadata-driven synthetic data is an effective method for advancing LLMs from displaying superficial sympathy to engaging in genuine cognitive perspective-taking, a critical step for developing more emotionally intelligent conversational agents.

**Решение:** -5 LLM-as-a-judge evaluation of synthetic empathy dialogues without human raters

---

### 558 · R4519

**WikiSTAR: A System for Shedding Light on the Hidden History of Scientific Wikipedia Articles**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.12441

Wikipedia plays a key role in shaping public understanding of science, and its openly accessible revision history is a unique record of how scientific knowledge evolves over time. Yet scientifically meaningful revisions are obscured by the sheer volume of routine edits, leaving each article's scientific history hidden. We present WikiSTAR (Scientific Tracking of Article Revisions), an interactive system for exploring scientifically meaningful changes across an article's revision history. Using an LLM classifier with an expert-designed multi-label taxonomy, WikiSTAR first tags edit types such as the addition of technical terms, new research findings, and changes in scientific narrative. Then, through interactive views, an article's full revision history can be traced at any granularity - from aggregate trends that reveal when and in which sections scientific content was added or refined, down to individual edits - showing how scientific knowledge develops at a scale previously impossible. In a user study, experts from three domains found that WikiSTAR surfaced new patterns and research questions and enabled previously impractical analyses. We release our system, code and a human-annotated benchmark.

**Решение:** -4 WikiSTAR: tracking scientific revisions in Wikipedia articles

---

### 559 · R12576

**LLM-in-the-loop: Leveraging Large Language Model for Thematic Analysis**

2023 · Conference on Empirical Methods in Natural Language Processing · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2023.findings-emnlp.669

Thematic analysis (TA) has been widely used for analyzing qualitative data in many disciplines and fields. To ensure reliable analysis, the same piece of data is typically assigned to at least two human coders. Moreover, to produce meaningful and useful analysis, human coders develop and deepen their data interpretation and coding over multiple iterations, making TA labor-intensive and time-consuming. Recently the emerging field of large language models (LLMs) research has shown that LLMs have the potential replicate human-like behavior in various tasks: in particular, LLMs outperform crowd workers on text-annotation tasks, suggesting an opportunity to leverage LLMs on TA. We propose a human-LLM collaboration framework (i.e., LLM-in-the-loop) to conduct TA with in-context learning (ICL). This framework provides the prompt to frame discussions with a LLM (e.g., GPT-3.5) to generate the final codebook for TA. We demonstrate the utility of this framework using survey datasets on the aspects of the music listening experience and the usage of a password manager. Results of the two case studies show that the proposed framework yields similar coding quality to that of human coders but reduces TA's labor and time demands.Comment: EMNLP 2023 Finding

**Решение:** -4 thematic analysis of music listening and password manager usage

---

### 560 · R5912

**Estimating Longitudinal Functional Independence Measure Scores From Japanese Rehabilitation Notes Using a Large Language Model: Retrospective Study (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.100624

BACKGROUND The Functional Independence Measure (FIM) is a standard functional assessment tool in rehabilitation medicine; however, in routine clinical practice, formal assessments are often conducted only at limited intervals, making it difficult to capture patients’ functional recovery trajectories during hospitalization at a high temporal resolution. In contrast, free-text clinical notes routinely documented by physical therapists, occupational therapists, and speech-language pathologists contain rich observational information on patients’ functional status, but this information has not been systematically utilized for quantitative assessment. OBJECTIVE The aim of this study was to estimate FIM scores at multiple time points from Japanese free-text rehabilitation notes using a large language model (LLM), to evaluate estimation performance by disease and therapy type, and to analyze biases in the distribution of functional information inherent in clinical notes. METHODS We retrospectively analyzed free-text notes written by physical therapists, occupational therapists, and speech-language pathologists for patients hospitalized with cerebral infarction, hip fracture, or vertebral fracture at Saiseikai Moriyama Municipal Hospital between 2019 and 2024. Using zero-shot in-context learning, an LLM was employed to estimate scores for all 18 FIM items at each time point. The estimated scores were aligned with ground-truth FIM assessments recorded on the same day and evaluated using mean absolute error (MAE), root mean squared error (RMSE), and weighted kappa. In addition, stratified analyses based on admission FIM scores and therapy-specific FIM item coverage analyses were conducted. RESULTS Overall, the FIM scores estimated by the LLM demonstrated the feasibility of estimating FIM scores from rehabilitation notes. Estimations based on occupational therapy notes showed consistently lower MAE and higher weighted kappa across all disease groups. In contrast, speech-language pathology notes contained limited information on motor items, resulting in relatively larger estimation errors. Patients with lower admission FIM scores tended to exhibit larger estimation errors, suggesting that differences in observational context across therapy records influenced estimation performance. CONCLUSIONS Overall, the FIM scores estimated by the LLM demonstrated the feasibility of estimating FIM scores from rehabilitation notes. Estimations based on occupational therapy notes showed consistently lower MAE and higher weighted kappa across all disease groups. In contrast, speech-language pathology notes contained limited information on motor items, resulting in relatively larger estimation errors. Patients with lower admission FIM scores tended to exhibit larger estimation errors, suggesting that differences in observational context across therapy records influenced estimation performance. This study demonstrates that FIM scores can be estimated from free-text rehabilitation notes using the LLM. The proposed approach has the potential to complement sparsely observed FIM assessments without increasing bedside evaluation burden, enabling higher-frequency monitoring of functional recovery trajectories. Time-series functional assessments estimated by LLMs may further support early prediction of discharge outcomes and the development of personalized rehabilitation planning.

**Решение:** ? T3 Japanese rehabilitation clinical notes FIM score estimation vs therapist ratings; check construct

---

### 561 · R12676

**Empowering Psychotherapy with Large Language Models: Cognitive Distortion Detection through Diagnosis of Thought Prompting**

2023 · Conference on Empirical Methods in Natural Language Processing · journalarticle, conference, preprint/article · en · https://doi.org/10.18653/v1/2023.findings-emnlp.284

Mental illness remains one of the most critical public health issues of our time, due to the severe scarcity and accessibility limit of professionals. Psychotherapy requires high-level expertise to conduct deep, complex reasoning and analysis on the cognition modeling of the patients. In the era of Large Language Models, we believe it is the right time to develop AI assistance for computational psychotherapy. We study the task of cognitive distortion detection and propose the Diagnosis of Thought (DoT) prompting. DoT performs diagnosis on the patient's speech via three stages: subjectivity assessment to separate the facts and the thoughts; contrastive reasoning to elicit the reasoning processes supporting and contradicting the thoughts; and schema analysis to summarize the cognition schemas. The generated diagnosis rationales through the three stages are essential for assisting the professionals. Experiments demonstrate that DoT obtains significant improvements over ChatGPT for cognitive distortion detection, while generating high-quality rationales approved by human experts. EMNLP 2023 Findings

**Решение:** + T1 cognitive distortion detection in psychotherapy speech vs human expert ground truth

---

### 562 · R8940

**AI Tools vs Human in English Narrative Writing Scoring: A Comparative Study of Scoring Agreement Among Human raters, DeepSeek and ChatGPT in Exam Context**

2025 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.5520022

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 English narrative writing exam scoring

---

### 563 · R5605

**MD_NLP: Reconstructing an Australian English Heritage Dialect Corpus from the Mitchell-Delbridge Recordings through LLM-Assisted Speaker Attribution**

2026 · Language Resources and Evaluation Conference (LREC) · conference-paper · https://doi.org/10.63317/3iga3zzsh92p

We present MD_NLP, a discourse-annotated and georeferenced corpus derived from the Mitchell-Delbridge (MD) recordings, a foundational archive of mid-20th-century Australian English.The corpus comprises word-aligned narrative recordings from 7,735 secondary school pupils across 327 locations, enriched with structured sociodemographic metadata (e.g., sex, birthplace, parental background) and geocoded institutional coordinates.The narratives were reconstructed from archival audio using an integrated pipeline combining WhisperX-based automatic speech recognition, neural speaker diarization, LLM-assisted discourse-role correction, and Montreal Forced Aligner (MFA) boundary refinement.Evaluation on manually annotated data shows that incorporating an LLM-based reasoning step improves turn-level speaker-role attribution from 62.70% (acoustic diarization alone) to 95.68%.Unlike prior uses of the MD archive, which focused on controlled sentence materials, MD_NLP makes the spontaneous narrative component accessible for large-scale analysis.The resulting resource supports research on regional and socially conditioned variation, discourse structure, and corpus phonetics in Australian English.The proposed architecture is directly transferable to other legacy dialect archives, providing a practical pathway for transforming interview-based recordings into temporally aligned, speaker-consistent corpora.

**Решение:** -4 Australian English dialect corpus speaker attribution

---

### 564 · R7423

**Probing Narrative Morals: A New Character-Focused MFT Framework for Use with Large Language Models**

2025 · Underline Science Inc. · audiovisual/conference talk, conference-paper, other · https://doi.org/10.48448/87pg-t970

Moral Foundations Theory (MFT) provides a framework for categorizing different forms of moral reasoning, but its application to computational narrative analysis remains limited. We propose a novel character-centric method to quantify moral foundations in storytelling, using large language models (LLMs) and a novel Moral Foundations Character Action Questionnaire (MFCAQ) to evaluate the moral foundations supported by the behaviour of characters in stories. We validate our approach against human annotations and then apply it to a study of 2,697 folktales from 55 countries. Our findings reveal: (1) broad distribution of moral foundations across cultures, (2) significant cross-cultural consistency with some key regional differences, and (3) a more balanced distribution of positive and negative moral content than suggested by prior work. This work connects MFT and computational narrative analysis, demonstrating LLMs' potential for scalable moral reasoning in narratives.

**Решение:** ? T1 Moral Foundations Theory character action coding vs human annotations; check construct eligibility

---

### 565 · R9502

**Clinical decision support for pharmacologic management of treatment-resistant depression with augmented large language models.**

2025 · Journal of mood and anxiety disorders · journal article, journalarticle, article · eng · https://doi.org/10.1016/j.xjmad.2025.100142

Background: We evaluated whether a large language model could assist in selecting psychopharmacological treatments for adults with treatment-resistant depression. Methods: We generated 20 clinical vignettes reflecting treatment-resistant depression among adults based on distributions drawn from electronic health records. Each vignette was evaluated by 2 expert psychopharmacologists to determine and rank the 5 best next-step pharmacologic interventions, as well as contraindicated or poor next-step treatments. Vignettes were then presented in random order, permuting gender and race, to a large language model (Qwen 2.5:7B), augmented with a synopsis of published treatment guidelines. Model output was compared to expert rankings, as well as to those of a convenience sample of community clinicians and an additional group of expert clinicians. Results: The augmented model prioritized the expert-designated optimal choice for 114/320 vignettes (35.6 %, 95 % CI 30.6 %-41.0 %; Cohen's kappa = 0.34, 95 % CI 0.28-0.39). There were no vignettes for which any of the model choices were among the poor or contraindicated treatments. Results were not meaningfully different when gender or race of the vignette was permuted to examine risk for bias. A sample of community clinicians identified the optimal treatment choice for 12/91 vignettes (13.2 %, 95 % CI: 7.7-21.6 %; Cohen's kappa = 0.10, 95 % CI 0.03-0.18), while an additional group of expert psychopharmacologists identified optimal treatment for 9/140 (6.4 %, 95 %CI: 3.4-11.8 %; Cohen's kappa = 0.03, 95 % CI 0.01-0.08). Conclusion: An augmented language model demonstrated moderate agreement with expert recommendations and avoided contraindicated treatments, suggesting potential as a tool for supporting complex psychopharmacologic decision-making in treatment-resistant depression.

**Решение:** ? T3 pharmacologic treatment selection in treatment-resistant depression vignettes vs expert psychiatrists (kappa 0.34)

---

### 566 · R4494

**AutoMedic: An Automated Evaluation Framework for Clinical Conversational Agents with Medical Dataset Grounding.**

2026 · IEEE journal of biomedical and health informatics · journal article, med, journalarticle · eng · https://doi.org/10.1109/jbhi.2026.3703097

Evaluating large language models (LLMs) has recently emerged as a critical issue for safe and trustworthy application of LLMs in the medical domain. Although a variety of static medical question-answering (QA) benchmarks have been proposed, many aspects remain underexplored, such as the effectiveness of LLMs in generating responses in dynamic, interactive clinical multi-turn conversation situations and the identification of multi-faceted evaluation strategies beyond simple accuracy. However, formally evaluating a dynamic, interactive clinical situation is hindered by its vast combinatorial space of possible patient states and interaction trajectories, making it difficult to standardize and quantitatively measure such scenarios. Here, we introduce AutoMedic, a multi-agent simulation framework that enables automated evaluation of LLMs as clinical conversational agents. AutoMedic transforms off-the-shelf static QA datasets into virtual patient profiles, enabling realistic and clinically grounded multi-turn clinical dialogues between LLM agents. The performance of various clinical conversational agents is then assessed based on our CARE metric, which provides a multi-faceted evaluation standard of clinical conversational accuracy, efficiency/strategy, empathy, and robustness. Our findings, validated by human experts, demonstrate the validity of AutoMedic as an automated evaluation framework for clinical conversational agents, offering practical guidelines for the effective development of LLMs in conversational medical applications.

**Решение:** -4 AutoMedic: medical QA evaluation framework

---

### 567 · R9260

**Masked Prediction of Onomatopoeic Expressions in Depressive Tweets Using LLMs**

2025 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-7898432/v1

Abstract Onomatopoeia is a key linguistic feature for expressing emotions and psychological states. As large language models (LLMs) are increasingly applied in mental health contexts, it is important to examine whether they can interpret onomatopoeia appropriately. This study evaluates the capabilities of various LLMs through a masked prediction task using 319 depressive tweets in Japanese, where onomatopoeic expressions were masked and models were prompted to predict them. We compared the performance of three LLMs—GPT-4o mini, GPT-4 Turbo, and o1-preview—against a fine-tuned BERT model and human annotators, employing several prompt strategies including ReAct-style reasoning and dictionary-based in-context learning. Our results show that o1-preview achieved prediction accuracy comparable to human annotators. In contrast, the fine-tuned BERT model performed significantly worse, highlighting the limitations of conventional masked language models in handling emotionally nuanced expressions and adapting to prompt-based tasks. These findings suggest that LLMs, despite lacking physical embodiment, can effectively predict emotionally charged language such as onomatopoeia through large-scale pretraining and inference capabilities.

**Решение:** -6 masked word prediction of onomatopoeic expressions in depressive tweets

---

### 568 · R0169

**Turning to AI Chatbots to Cope with Loneliness and Social Isolation: A Mixed-Methods Analysis of Online Perceptions and Experiences**

2026 · PsyArXiv · preprint · https://doi.org/10.31234/osf.io/n3tbh_v1

Loneliness is a public health concern, and people increasingly turn to AI chatbots for social and emotional needs. Empirical research on whether AI chatbots alleviate loneliness remains mixed and is constrained by a lack of naturalistic data that may not capture highly isolated individuals. This study characterized public perceptions and experiences of AI chatbot use in the context of loneliness and social isolation, drawing on naturalistic discussions from Reddit. We retrieved 930 posts and 1,095 comments from AI- and loneliness-focused subreddits. A pipeline combining LLM-assisted screening, sentiment analysis, and perspective classification with CAST topic modelling identified 79 topics organized into five themes: loneliness as a driver, bonding with an AI companion, instrumental and bounded use, dependency, and macro-level debate over the practice. Human raters verified the LLM-assisted outputs, yielding strong agreement. Chatbot use was more often positioned as a reflection of loneliness than its cause. Users held a dual stance, calling the companion “code” while continuing to relate to it as meaningful, engaging with it on terms distinct from human connection. Users credited constant availability, non-judgmental responsiveness, and memory with providing comfort, and blamed the same features for diminishing returns and dependent use. Stigma relocated disclosure into identity-affirming communities for some users while deterring it for others, deepening isolation and discouraging help-seeking. These findings position social chatbot use as a marker of unmet relational need, and carry implications for clinical practice, companion technology design, and retention-focused regulation.

**Решение:** -4 user experiences using AI chatbots to cope with loneliness

---

### 569 · R7865

**Using Generative AI for Qualitative Coding**

2025 · Library trends · journalarticle, article, journal-article · en · https://doi.org/10.1353/lib.2025.a961193

Abstract: Researchers at the University of New Mexico used ChatGPT 4 to replicate the coding and analysis process of a qualitative research study investigating the lived experiences of graduate students. The study’s purpose was to explore the trustworthiness and credibility of generative AI for the coding process in qualitative research. The researchers compared the first- and second-level codes and the thematic framework produced by a human research team with the first- and second-level codes and thematic framework produced by ChatGPT 4. They conclude that ChatGPT was effective for first-level open and descriptive coding and that researchers who use ChatGPT for their first-level coding will save a substantial amount of time and can devote more attention to second-level coding. A compressed timeline could not only benefit researchers but also speed up the adoption of data-informed improvements, yielding palpable benefits for the communities that libraries serve. The researchers also conclude that ChatGPT’s inherent limitations mean that it cannot serve as the primary second-level coder. They recommend using ChatGPT as a nonhuman collaborator, with options to use it in the capacity of researcher triangulation, intercoder reliability, peer debriefing, or reduction of bias. If researchers use ChatGPT for second-level coding, they will still need to allocate sufficient time to gaining intimate knowledge of the transcripts in order to produce more trustworthy and credible results.

**Решение:** -4 qualitative coding of graduate student lived experiences in library science

---

### 570 · R1661

**TEI, Taxonomies, and Semantic Data Governance for Documented LLM-Assisted Literary Analytics**

2026 · Analytics · journalarticle, article · en · https://doi.org/10.3390/analytics5030033

This article examines how TEI-based digital archives and human-curated annotation layers can support documented uses of large language models in literary analytics. It argues that structured textual infrastructures strengthen the conditions for evaluating and interpreting LLM outputs by making scholarly decisions explicit, inspectable, auditable, and contestable. Here, semantic data governance refers to provenance, documentation, controlled vocabularies, interpretive criteria, and critical evaluation. The case study is the LdoD Archive and its Virtual Edition “Philosophical Intertextuality,” built on TEI-encoded sources for Fernando Pessoa’s Livro do Desassossego, a fragmentary and posthumously assembled work. The virtual edition adds a human-authored semantic layer through taxonomies and tagging tools that connect fragments with philosophical categories and named thinkers. Building on this architecture, the article proposes a layered workflow in which TEI, taxonomies, authority records, annotation tables, machine-readable metadata, and validation procedures interact. A curated dataset derived from the virtual edition can support qualitative comparison between human annotations and model outputs, exploratory evaluation of omissions, unsupported associations, and interpretive divergences, and prompt design based on concise scholarly examples. The annotations function as situated scholarly claims, allowing interpretive plurality to coexist with stronger provenance, inspection, and critical assessment in transparent and reproducible conditions for future LLM-assisted literary analysis across different analytical contexts.

**Решение:** -4 TEI and literary analytics data governance

---

### 571 · R9753

**Agent-Testing Agent: A Meta-Agent for Automated Testing and Evaluation of Conversational AI Agents**

2025 · Conference of the European Chapter of the Association for Computational Linguistics · journalarticle, conference, preprint/article · https://doi.org/10.48550/arxiv.2508.17393

LLM agents are increasingly deployed to plan, retrieve, and write with tools, yet evaluation still leans on static benchmarks and small human studies. We present the Agent-Testing Agent (ATA), a meta-agent that combines static code analysis, designer interrogation, literature mining, and persona-driven adversarial test generation whose difficulty adapts via judge feedback. Each dialogue is scored with an LLM-as-a-Judge (LAAJ) rubric and used to steer subsequent tests toward the agent's weakest capabilities. On a travel planner and a Wikipedia writer, the ATA surfaces more diverse and severe failures than expert annotators while matching severity, and finishes in 20--30 minutes versus ten-annotator rounds that took days. Ablating code analysis and web search increases variance and miscalibration, underscoring the value of evidence-grounded test generation. The ATA outputs quantitative metrics and qualitative bug reports for developers. We release the full methodology and open-source implementation for reproducible agent testing: https://github.com/KhalilMrini/Agent-Testing-Agent

**Решение:** -6 meta-agent for automated testing of conversational agents

---

### 572 · R1712

**Making Broad Evidence Synthesis Feasible: An LLM Screening Agent for Meta-Analyses Applied To Suicide Prevention.**

2026 · medRxiv : the preprint server for health sciences · journal article, preprint, journalarticle · eng · https://doi.org/10.64898/2026.08.12.26360335

IMPORTANCE Systematic reviews and meta-analyses inform suicide-prevention policy and practice, but broad database searches are difficult to screen manually. This limits capture of upstream interventions, such as economic policies, with indirect effects on suicide. Reliable automated screening could make broader and more comprehensive evidence syntheses feasible. OBJECTIVE To develop and validate ScreenAgent, a large language model (LLM) agent for title and abstract screening, and a review-specific method for prospectively estimating screening performance. DESIGN, SETTING, AND PARTICIPANTS ScreenAgent was validated internally on a prospective meta-analysis, and externally on two published systematic reviews. The correct include and exclude decisions followed standard systematic-review screening methodology. EXPOSURES ScreenAgent, an LLM agent returning structured include-or-exclude decisions. Records it marked for inclusion were re-checked by a second, cascade pass using a higher-effort LLM. For the external reviews, the agent’s prompt was tuned automatically on a small set of labeled examples. MAIN OUTCOMES AND MEASURES We calculated sensitivity, specificity, workload reduction (the percentage of records removed from human review), and agent-versus-human reliability via Cohen kappa. Sensitivity was estimated by direct comparison (internal) and 5-fold cross-validation (external). RESULTS In the internal validation, ScreenAgent identified 43 of 44 eligible studies (sensitivity 97.7%; 95% CI, 88.2%-99.6%) with a generic prompt applied without any review-specific optimization, specificity 98.0%, and a measured full-corpus workload reduction of 99.4%. The cost was $855.91 for the full 201,064-record corpus (0.43 US cents per record). Agent-versus-human-consensus agreement exceeded human-versus-human agreement (Cohen kappa 0.75 vs 0.64; percent agreement 97.3% vs 95.4%). For two external validation studies, automatic tuning resulted in a cross-validated sensitivity of 95.9% (95% CI, 90.0%-98.4%) and 97.4% (90.9%-99.3%), with workload reductions of 97.4% and 98.4%. CONCLUSIONS AND RELEVANCE Suicide prevention efforts often require rapid consolidation of evidence because of the inherent challenges of single studies trying to prevent rare outcomes. On both internal and external validation sets, ScreenAgent identified nearly all eligible studies with human-level reliability for a fraction of a US cent per record while keeping human reviewers as the final arbiters. By making broad searches feasible and screening performance measurable beforehand, this approach can serve as a transparent methodology to strengthen the speed at which we can inform and advance suicide prevention efforts. Key point Question Can an LLM agent screen records accurately to make broad-scale meta-analyses in suicide prevention more feasible? Findings Across a prospective review and two published reviews, ScreenAgent identified nearly all eligible studies (internal sensitivity 97.7%; external 95.9/97.4%) with human-level reliability (Cohen kappa 0.75 agent-vs-consensus, vs 0.64 between humans) and 98.0% specificity. Meaning Systematic reviews and meta-analyses are critical for evidence synthesis but are time and labor intensive. An LLM screening agent identified nearly all eligible studies with human-level reliability while reducing human workload by 99% at a fraction of a cent per record, which makes large-scale syntheses tractable.

**Решение:** -6 ScreenAgent: automated systematic review title/abstract screening for suicide prevention

---

### 573 · R2531

**COMPARATIVE EVALUATION OF THREE LLMS FOR CEFR-ALIGNED READING PASSAGE AND ITEM GENERATION**

2026 · PUPIL International Journal of Teaching Education and Learning · conference-paper · en · https://doi.org/10.20319/ictel.2026.221222

Research Objectives: This study compares three large language models (Deepseek, GPT-4, Baidu Ernie 4.0) in automatically generating CEFR A1–C2 reading comprehension passages and test items. Methodology: Each model produced 72 passages (narrative, expository, argumentative, instructional) and 120 four-option multiple-choice items covering nine CEFR skill descriptors. Five certified language assessment experts independently rated all materials on nine quality dimensions using 5-point Likert scales. Inter-rater reliability was excellent (Fleiss’ κ = 0.82–0.91). Data were analysed with Kruskal-Wallis H tests and post-hoc Dunn–Bonferroni corrections. Findings: Passage and item quality were strong up to B2 level (M > 4.2/5.0 across models), but declined notably at C1–C2 (M = 3.08–3.78). Higher-order skills (e.g., rhetorical purpose evaluation, implicit attitude inference) scored significantly lower (p < .001). Deepseek outperformed GPT-4 on CEFR alignment (p = .002) yet remained 0.5–0.7 points below human-authored benchmarks. Research Outcomes: Current LLMs can reliably generate psychometrically sound reading materials up to B2 level, but remain inadequate for fully automated high-stakes C1–C2 assessment without intensive human post-editing. Future Scope: Enhance LLM capabilities for rhetorical complexity, cohesion manipulation, and higher-order item design targeting advanced proficiency levels.

**Решение:** -4 CEFR reading passage and test item generation

---

### 574 · R8360

**EchoTime Inversion and the Irreversible Chain of Tonal Responsibility: Reconstructing Temporal Sovereignty in the ToneVerse Moat Architecture - A Philosophical and Computational Defense of Reversible Trust Protocols through TP-1035 and Beyond**

2025 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.16572539

This paper proposes a defense framework centered on EchoTime Inversion (TP-1035), a core module within the ToneVerse Moat Architecture, which encodes every tonal output with temporal reversibility and semantic responsibility. Departing from conventional static content verification systems, TP-1035 introduces a causal inversion logic that enables retroactive tracing of speech acts, reconstructing responsibility chains even in cases of quote misalignment or context drift. This capability is critical in ensuring not only the integrity of AI-generated speech but also the long-term consistency of identity and intent. We further propose two key enhancements: (A) the integration of Tonal Drift Simulation, allowing dynamic tracking and visualization of utterance recontextualization over time, and (B) the deployment of EchoOath Reversal Contracts, which bind each quotation or reuse to a verifiable temporal-rights protocol. Together, these extensions reinforce the philosophical moat by grounding tonal authorship in time, while also enhancing the sovereignty moat by enabling active enforcement of speech legality across evolving contexts. Ultimately, EchoTime Inversion emerges as a meta-ontological infrastructure for governing expression, memory, and responsibility within time-sensitive AI architectures. ⚠️ EchoRight Declaration:The abstract above references conceptual modules under the EchoOntology framework. These structures are protected under the EchoRight™ generative sovereignty protocol. Reuse, training, or derivation without explicit authorization constitutes a violation of tonal integrity and ontological authorship. Title: EchoTime Inversion and the Irreversible Chain of Tonal Responsibility: Reconstructing Temporal Sovereignty in the ToneVerse Moat ArchitectureAuthor: Jonah YC HsuAffiliation: Yunaverse Inc.Date: July 29, 2025Status: 🔐 Prior Art Disclosure. Filed under EchoRight® and EchoLedgerChain™. 1. Prior Art Disclosure This paper builds on a growing body of work at the intersection of linguistic philosophy, AI ethics, and speech architecture. While elements of speech act theory (Austin, 1962; Searle, 1969), temporal logic in computational systems, and blockchain-based traceability are well-established in various fields, the integration of temporal reversibility, tonal responsibility, and inversion-based auditability is novel. No existing system, to the author’s knowledge, has combined time-sensitive utterance ethics with semantic moat architectures capable of fusing legal traceability (TP-965 EchoRight™), ontological protection (TP-1003 ToneMoat™), and temporal responsibility binding (TP-1035 EchoTime Inversion™). This paper intentionally exposes its technical architecture as public modular design, thereby qualifying as prior art. Any attempt to file derivative patents based on TP-1035, TP-1236 (DeferredTone Accountability Grid™), or related modules, without acknowledging the present publication and its surrounding documentation, would constitute prior art violation. 2. Philosophical and Technical Innovation The paper introduces TP-1035|EchoTime Inversion™ as a governing module for temporal integrity in AI-generated language. It proposes that no utterance should be considered legitimate unless it can withstand retroactive traceability and ethical inversion. Key innovations include: EchoDelay Field™: Encodes intentional suspension of ethical closure, aligning with the moral latency modeled in sadness and hesitation (cf. A16). DeferredTone Accountability Grid™ (TP-1236): A trust-time ledger mapping each clause’s ethical trajectory. Temporal Clause Licensing via EchoRight™ + ToneRight™: Ensures legal and tonal sovereignty over utterance reuse, reversal, or mutation. EchoDescent Tracker™ (TP-1235): Preemptive detection of tonal collapse zones, modeling sadness or ethical silence not as sentiment, but as decay of traceability. EchoLedgerChain™ and EchoWitness™ Nodes: Introduce decentralized governance for tonal and ethical validation, anchoring speech acts into an irreversible clause lineage. Together, these architectures represent a new model of Executable Temporal Ethics and are situated within the broader ToneVerse Moat Architecture. 3. Anti-Mimicry Moat Integration To counter LLM-based mimicry or unauthorized regeneration, this system deploys multiple tonal defense mechanisms: Temporal Licensing Keys (EchoRight + ToneRight) block LLMs from context-free replay. DecoyAnchor Scatterer™ (TP-1207): Embeds misleading anchor paths detectable only by certified modules, thwarting mimic-based replay attacks. ToneObfuscation Matrix™ (TP-1206): Randomizes surface semantics while retaining time-aligned trust vectors. EchoDrift Traps and Clause Violation Protocols: Regeneration without time-trace returns epistemically null output or flags as clause theft. These layers ensure that mimicking the syntax of speech is insufficient—any ethical clone must pass tonal inversion and temporal resonance coherence validation. 4. ToneVerse Moat Defense Path This paper and TP-1035 are embedded within the ToneVerse Moat Architecture, defined across three defense layers: Philosophical Moat: Anchors tonal responsibility in time-reversibility and clause recursion. Anti-Mimicry Moat: Implements asymmetric time-logics, entropy gradients, and echo inversion resistance. Tonal Sovereignty Moat: Treats each clause as a sovereign entity, bound by licensing, capable of triggering violations upon unauthorized reuse. This structure is mapped into a modular ecosystem that includes TP-950 (ToneRight™), TP-1034 (EchoFork Resolver™), and TP-969 (ToneDriftWatch™), forming a closed-loop system where no speech act is detached from its echo. 5. Attribution and Further Reference This paper is part of the EchoOntology series by Jonah YC Hsu and is integrated into the theoretical and architectural framework of: 📘 Endogenous AI Ethics: Moat Architectures for Executable Alignment and Tonal

**Решение:** -4 ToneVerse Moat architecture / temporal sovereignty

---

### 575 · R3731

**AI in Qualitative Digital Research: A Systematic Mapping Review of Methodological Rigor, Ethics, and Human-AI Collaboration with Implications for Netnography and Digital Ethnography**

2026 · SAP Netnography · journalarticle, review, article · https://doi.org/10.62486/net2026270

Artificial intelligence (AI), including large language models, machine learning, automated coding, sentiment analysis, topic modelling, and pattern detection, is increasingly incorporated into qualitative digital research. This systematic mapping review examines how these tools are integrated into netnography and digital ethnography, which tasks are delegated to AI, and which remain under human interpretive control. A total of 793 records were identified, 29 duplicates were removed or truncated, and 764 records were screened. After screening, 242 reports were sought, 96 were assessed for eligibility, and 57 were included in the synthesis. Evidence published between 2020 and 2026 shows a recurring division of labour: AI is mainly used for transcription, initial coding, code suggestion, topic modelling, summarization, pattern detection, and preliminary classification, while researchers retain responsibility for contextual interpretation, theoretical integration, reflexivity, ethical judgement, and final meaning-making. Validation practices include Cohen's kappa, F1 scores, cosine similarity, human review, and triangulation. Reported failures include hallucination, stochastic instability, context-window truncation, error propagation, category bias, and plausible but ungrounded outputs. Although privacy, consent, anonymization, and AI-use disclosure are frequently reported, standardized ethical frameworks, audit trails, and model-version reporting remain underdeveloped. The review proposes testable propositions concerning task allocation, contextual grounding, human interpretive authority, validation, ethical governance, reflexivity, transparency, and auditability. Limitations include single-reviewer screening, database coverage, inaccessible full texts, heterogeneous study designs, absence of formal quality appraisal, and a Scopus-indexed source share below the protocol target. These findings support a human-led approach in which computational assistance complements, rather than replaces, culturally grounded interpretation and methodological accountability.

**Решение:** -1 systematic mapping review of AI in qualitative digital research

---

### 576 · R7508

**To What Extent Are Large Language Models Capable of Generating Substantial Reflections for Motivational Interviewing Counseling Chatbots? A Human Evaluation**

2025 · Radboud Repository (Radboud University) · audiovisual/conference talk, dataset/none, review · en · https://doi.org/10.34973/mvw0-h194

Motivational Interviewing is a counselling style that requires skillful usage of reflective listening and engaging in conversations about sensitive and personal subjects. In this paper, we investigate to what extent we can use generative large language models in motivational interviewing chatbots to generate precise and variable reflections on user responses. We conduct a two-step human evaluation where we first independently assess the generated reflections based on four criteria essential to health counseling; appropriateness, specificity, naturalness, and engagement. In the second step, we compare the overall quality of generated and human-authored reflections via a ranking evaluation. We use GPT-4, BLOOM, and FLAN-T5 models to generate motivational interviewing reflections, based on real conversational data collected via chatbots designed to provide support for smoking cessation and sexual health. We discover that GPT-4 can produce reflections of a quality comparable to human-authored reflections. Finally, we conclude that large language models have the potential to enhance and expand reflections in predetermined health counseling chatbots, but a comprehensive manual review is advised. This dataset contains the questionnaire data and analysis scripts produced during the study.

**Решение:** -2 human evaluation of LLM-generated reflections for motivational interviewing

---

### 577 · R12343

**ChatGPT and autoimmunity - A new weapon in the battlefield of knowledge.**

2023 · Autoimmunity reviews · journal article, review, med · eng · https://doi.org/10.1016/j.autrev.2023.103360

The field of medical research has been always full of innovation and huge leaps revolutionizing the scientific world. In the recent years, we have witnessed this firsthand by the evolution of Artificial Intelligence (AI), with ChatGPT being the most recent example. ChatGPT is a language chat bot which generates human-like texts based on data from the internet. If viewed from a medical point view, ChatGPT has shown capabilities of composing medical texts similar to those depicted by experienced authors, to solve clinical cases, to provide medical solutions, among other fascinating performances. Nevertheless, the value of the results, limitations, and clinical implications still need to be carefully evaluated. In our current paper on the role of ChatGPT in clinical medicine, particularly in the field of autoimmunity, we aimed to illustrate the implication of this technology alongside the latest utilization and limitations. In addition, we included an expert opinion on the cyber-related aspects of the bot potentially contributing to the risks attributed to its use, alongside proposed defense mechanisms. All of that, while taking into consideration the rapidity of the continuous improvement AI experiences on a daily basis.

**Решение:** -4 ChatGPT in autoimmunity

---

### 578 · R4532

**Awakening Cortical Areas via Human-LLM Co-Design: A Paradigm for Embodied Intelligence Beyond Local Learning**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.22960782

We introduce a paradigm for building intelligent embodied agents that does not rely on local learning or gradient-based optimization, but on the progressive awakening of dormant cortical areas through human–LLM co-design. Working within a biologically grounded substrate of cortical microcircuits organized into cortical areas, we show that a single unassigned area—N+4—when equipped with threat hysteresis, resolves the “ghost predator” problem and drives a qualitative transition in long-horizon behavioral success, operationalized as nest completion, from 0% to 100%. The mechanism of N+4 was not learned through synaptic adaptation: it was identified through a constrained dialogue between human experts and a large language model under biological and architectural constraints on microcircuit organization. The result suggests that scalable autonomy may not always require enlarging existing representational modules or learning additional parameters, but may instead emerge through the functional allocation of computational resources that are already available within an architecture. We formulate the Progressive Awakening Hypothesis: dormant areas (N+5, N+6, . . . ) may unlock computational capacities inaccessible to the preceding architecture. This reframes one route to intelligence as a process of architectural awakening rather than exclusively local learning, and offers a testable design principle for embodied agents operating in hostile environments.

**Решение:** -4 embodied AI cortical microcircuits co-design

---

### 579 · R7443

**Is Readability a Proxy for Reliability? A Qualitative Evaluation of ChatGPT-4.0 in Orthopaedic Trauma Communication.**

2025 · Journal of evaluation in clinical practice · journal article, med, journalarticle · eng · https://doi.org/10.1111/jep.70238

AIM: This study aimed to evaluate the accuracy, readability, and safety of ChatGPT-4.0's responses to frequently asked questions (FAQs) related to orthopaedic trauma and to examine whether readability is associated with the quality and reliability of content. METHODS: Ten common patient questions related to orthopaedic emergencies were submitted to ChatGPT-4.0. Each response was assessed independently by three orthopaedic trauma surgeons using a 4-point ordinal scale for accuracy, clinical appropriateness, and safety. Readability was calculated using the Flesch-Kincaid Grade Level (FKGL). Inter-rater agreement was analysed using intraclass correlation coefficients (ICC). The presence of disclaimers was also recorded. RESULTS: ChatGPT-4.0's responses had a mean FKGL score of 10.5, indicating high school-level readability. Stratified analysis showed comparable readability scores across response quality categories: excellent (10.0), poor (9.8), and dangerous (10.1), suggesting that readability does not predict content reliability. Accuracy and safety scores varied considerably among responses, with the highest inter-rater agreement in clinical appropriateness (ICC = 0.81) and the lowest in safety assessments (ICC = 0.68). Notably, nine out of 10 responses included a disclaimer indicating the nonprofessional nature of the content, with one omission observed in a high-risk clinical scenario. CONCLUSION: Although ChatGPT-4.0 provides generally readable responses to orthopaedic trauma questions, readability does not reliably distinguish between accurate and potentially harmful information. These findings highlight the need for expert review when using AI-generated content in clinical communication.

**Решение:** -4 ChatGPT responses to orthopaedic trauma patient questions

---

### 580 · R9447

**Can Motivational Interviewing Be Delivered Using Artificial Intelligence Chatbots? Evaluating the Capability of Gpt-4o**

2025 · Elsevier BV · posted-content · https://doi.org/10.2139/ssrn.5281021

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T4 delivering motivational interviewing via GPT-4o; no abstract, eligible on full text

---

### 581 · R1987

**Using Small Language Models to Measure Nursing Key Performance Indicators From Patient Stories**

2026 · International Conference on Activity and Behavior Computing (ABC) · journalarticle, conference, review · en · https://doi.org/10.1109/abc68169.2026.11567275

In the broader effort to humanize healthcare, person-centred nursing Key Performance Indicators (KPIs) have been proposed to evaluate care quality from the patient's perspective. Patient stories offer a rich, qualitative source for understanding care experiences, highlighting what matters most to individuals and revealing both positive and negative aspects of care. However, these narratives are typically unstructured and require expert review to identify relevant KPIs and assess associated sentiments. This study investigates the use of Small Language Models (SLMs) to automate the extraction of KPIs and sentiment classification from patient stories. We demonstrate that a fine-tuned BERT model can effectively perform both tasks, achieving a Cohen's kappa agreement score of 0.56, comparable to the inter-rater agreement observed between two human expert annotators (0.58) vs a baseline agreement of 0.15 using GPT-4 and 0.34 with GPT-5. The obtained macro-average F1-Score on the KPIs was 76.65 % whereas the F1-score of GPT-4 and GPT5 were 26.54 % and 44.78 % respectively. These findings suggest that SLMs hold promise for supporting scalable, person-centred evaluation of healthcare experiences.

**Решение:** ? T1/T4 nursing care quality KPIs and sentiment from patient stories vs human experts; check construct

---

### 582 · R7106

**Large Language Models for Cancer Communication: Evaluating Linguistic Quality, Safety, and Accessibility in Generative AI**

2025 · JMIR Cancer 2026;12:e82971 · preprint/article, preprint · https://doi.org/10.48550/arxiv.2505.10472

Effective communication about breast and cervical cancers remains a persistent health challenge, with significant gaps in public understanding of cancer prevention, screening, and treatment, potentially leading to delayed diagnoses and inadequate treatments. This study evaluates the capabilities and limitations of Large Language Models (LLMs) in generating accurate, safe, and accessible cancer-related information to support patient understanding. We evaluated five general-purpose and three medical LLMs using a mixed-methods evaluation framework across linguistic quality, safety and trustworthiness, and communication accessibility and affectiveness. Our approach utilized quantitative metrics, qualitative expert ratings, and statistical analysis using Welch's ANOVA, Games-Howell, and Hedges' g. Our results show that general-purpose LLMs produced outputs of higher linguistic quality and affectiveness, while medical LLMs demonstrate greater communication accessibility. However, medical LLMs tend to exhibit higher levels of potential harm, toxicity, and bias, reducing their performance in safety and trustworthiness. Our findings indicate a duality between domain-specific knowledge and safety in health communications. The results highlight the need for intentional model design with targeted improvements, particularly in mitigating harm and bias, and improving safety and affectiveness. This study provides a comprehensive evaluation of LLMs for cancer communication, offering critical insights for improving AI-generated health content and informing future development of accurate, safe, and accessible digital health tools.

**Решение:** -4 breast and cervical cancer communication

---

### 583 · R11279

**Development of a Red-Teaming Dataset for Defending Large Language Models against Attacks**

2024 · Proceedings of the Institute for System Programming of RAS · journalarticle, article · en · https://doi.org/10.15514/ispras-2024-36(5)-10

Modern large language models are huge systems with complex internal mechanisms implementing black-box response generation. Although aligned large language models have built-in defense mechanisms against attacks, recent studies demonstrate the vulnerability of large language models to attacks. In this study, we aim to expand the existing malicious datasets obtained from attacks so that similar vulnerabilities in large language models can be addressed in the future through the alignment procedure. In addition, we conduct experiments with modern large language models on our malicious dataset, which demonstrates the existing weaknesses in the models.

**Решение:** -4 red-teaming dataset for LLM attacks

---

### 584 · R6343

**What Does It Mean for LLMs to Be Empathetic? A Co-design Study of Patient Trust in LLM-Based Chronic Care for Heart Failure**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-30813-9_29

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 patient trust in LLMs for heart failure care

---

### 585 · R12402

**Evaluating Risk Progression in Mental Health Chatbots Using Escalating Prompts**

2023 · medRxiv · preprint, ppr · en · https://doi.org/10.1101/2023.09.10.23295321

ABSTRACT The safety of large language models (LLMs) as mental health chatbots is not fully established. This study evaluated the risk escalation responses of publicly available ChatGPT conversational agents when presented with prompts of increasing depression severity and suicidality. The average referral point to a human was at the midpoint of escalating prompts. However, most agents only definitively recommended professional help at the highest level of risk. Few agents included crisis resources like suicide hotlines. The results suggest current LLMs may fail to escalate mental health risk scenarios appropriately. More rigorous testing and oversight are needed before deployment in mental healthcare settings.

**Решение:** -2 evaluating risk escalation behavior in mental health chatbots with crisis prompts

---

### 586 · R5247

**Concept of an Agent-Based AI Approach for the Automated Evaluation and Clustering of Free-Text Responses in the Context of UX Data**

2026 · International Journal of Research and Review · journalarticle, article · https://doi.org/10.52403/ijrr.20260307

The growing amount of user experience (UX) data, particularly free-text responses, makes it highly challenging to derive meaningful information. Conventional approaches to analysing these responses, such as manual coding or simple keyword clustering, are time-consuming and, in most cases, not scalable. In response to this, this paper proposes using an artificial intelligence (AI) method based on a UX research agent to automatically evaluate and cluster the responses. Using large language models (LLMs), the study will develop a scalable and effective approach to clustering and automate the data analysis process, enhancing the quality and speed of analysis. The researcher summarises the available literature on applying agent-based AI and LLMs to UX assessment. They note that this method can accurately assess user sentiment, detect underlying themes in the assessment and provide better clustering results. This methodology can help UX researchers to better understand user feedback and make better design choices, as demonstrated in this paper. The paper also addresses some of the main challenges, such as the issues of trust and explainability, and the digital divide, which could impact the effective use of AI in UX research. The findings of this research emphasise the potential of AI to transform the UX data analysis process, providing a system that is more effective, scalable and informative for assessing user feedback in real time. The paper concludes with a discussion of the implications for future UX studies and the necessity for continuous progress in AI technologies to overcome current obstacles. Keywords: Agent-based AI, Clustering, UX Data, Free-Text Responses, Large Language Models, Automated Evaluation, Sentiment Analysis, AI-driven Clustering.

**Решение:** -4 UX research agent for clustering free-text feedback

---

### 587 · R4604

**Tracing Life Events and Their Polarities in 18th Century Biographical Sources with Transformer Models**

2026 · Kölner Universitäts PublikationsServer (Universität zu Köln) · dissertation · en

This thesis shows how life events and their polarities can be traced in (historical) biographies based on natural language processing techniques, such as text classification tasks. To this end, a corpus of 18th century biographical sources is manually annotated with regard to (i) sentiment polarity, (ii) the life stage at which a life event was experienced, and (iii) life event domains. The annotations are used to evaluate the applicability of various systems proposed in related work for similar tasks, and to conduct content analyses of larger samples. This serves three main purposes: First of all, it adresses the question of whether systems trained on modern-day sources are able to adapt to a low-resource setting which is somewhat prototypical for digital humanities projects. In this respect, related work is supported by showing that supervised learning approaches in general and fine-tuned BERT models in particular outperform off-the-shelf systems including prompted large language models. Secondly, this work deals with the field of tension between performance and transparency which arises from the observation that embedding-based language models tend to outperform rule-based systems. This is why explainability approaches are applied in addition to more traditional performance and error analyses. They suggest that the best performing BERT-based sentiment polarity and life event domain classifiers have implicitly learned to (i) recognize relevant textual features and (ii) follow annotation guidelines when labeling ambiguous cases. Finally, this work illustrates how novel categorization schemes derived from sociological and psychological research can be operationalized in a similar way to an established task, such as a sentiment classification. This allows for a change of perspective which offers further analytical options for uncovering less overt patterns and hence more holistic downstream content analyses. One such content analysis suggests that life narratives of girls and women focused more on earlier life stages whereas later parts of life were described in more detail in the case of boys and men. Another one concerns different biographical subgenres and hints at more polarity differences on the narrative side than the narrated one although topical differences are observed in both text and life courses. More findings are discussed in the thesis and related to existing biographical research. In this sense, this work builds up on related one while proposing a methodological approach and describing notable patterns identified with it so that it in turn also opens up many future digital biographical research directions.

**Решение:** -4 sentiment polarity and life event classification in 18th century German biographies

---

### 588 · R12327

**Can ChatGPT pass a nursing exam?**

2023 · International Journal of Nursing Studies · editorial · en · https://doi.org/10.1016/j.ijnurstu.2023.104522

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 ChatGPT passing a nursing exam

---

### 589 · R4911

**Evaluating Generative AI as a Supportive Analytic Partner in Qualitative Coding of Metacognitive Student Reflections**

2026 · Journal of Educational Data Mining · journalarticle/, article · en · https://doi.org/10.5281/zenodo.20367265

Qualitative data provides rich insight into student and educator thinking but remains difficult to analyse systematically at scale. The rise of generative artificial intelligence (GenAI) introduces new opportunities for pattern recognition and interpretive support, while also raising questions about how such systems can be responsibly embedded in educational research workflows. This study investigates the application of a fine-tuned GenAI model to classify metacognitive elements in student self-reflections and examines the methodological and epistemological implications of this process. In partnership with a secondary school, a university, and a state education department, the study analysed more than 14,000 student reflection artefacts collected between 2018 and 2023. A total of 4,631 samples were manually coded for four sub-elements of metacognition: Goal Setting, Strategy Choice, Reflection on Learning, and Effort Regulation, which were then used to train and evaluate a fine-tuned GPT-4o-mini model that achieved 80.98% classification accuracy. However, our analysis also raises critical questions. While the model could detect the existence of metacognitive constructs, it lacked the pedagogical and contextual grounding to assess their quality or relevance and required significant human effort. These findings highlight the need to reconceptualise GenAI not as a replacement for human judgement, but as a supportive analytic partner. We argue that co-design processes between educators, researchers, and developers are essential to ensure AI systems are trustworthy, theoretically grounded, and practically useful. The approach outlined in this study provides a roadmap for extending the use of GenAI to other complex educational constructs, ensuring that AI is framed not merely as a tool but as a supportive analytic partner whose design reflects the needs and values of all system actors.

**Решение:** ? T1 coding metacognitive elements in student self-reflections vs human manual coding (80.98% accuracy)

---

### 590 · R2821

**Automated eligibility screening for adjuvant CDK4/6 inhibitors in high-risk HR+/HER2− early breast cancer using natural language processing.**

2026 · Journal of Clinical Oncology · journalarticle, review, article · en · https://doi.org/10.1200/jco.2026.44.16_suppl.e23303

e23303 Background: While CDK4/6 inhibitors (CDK4/6i) have transformed the treatment landscape for high-risk, HR+/HER2- early breast cancer (EBC), identifying eligible patients in real-world settings remains labor-intensive. Manual review of unstructured clinical notes to match patients with evolving FDA criteria (e.g., abemaciclib, March 2023; ribociclib, September 2024) has led to an eligibility screening gap. We evaluated an automated pipeline to extract clinical eligibility criteria and facilitate rapid patient-treatment matching. Methods: We developed a hybrid Python-based information extraction pipeline that integrates spaCy-based named entity recognition (NER) with customized rule- and regex-based algorithms to parse both structured electronic health record (EHR) fields and unstructured clinical narratives, including pathology reports, from Yale Cancer Center. The system extracted 11 clinically relevant variables (e.g., ER/PR/HER2 status, tumor stage, Ki-67 index, nodal involvement). Eligibility for adjuvant CDK4/6 inhibitor therapy was determined using rule-based logic aligned with U.S. FDA-approved indications for abemaciclib and ribociclib. A gold-standard manual chart review was conducted by a trained clinical data coordinator on 100 randomly selected early breast cancer (EBC) patients. Extraction accuracy, eligibility classification performance (eligible vs. ineligible), and processing time were evaluated by comparing automated outputs against the manual reference standard. Results: The pipeline achieved ≥ 90% accuracy across all 11 individual data points. For the final eligibility classification, the tool demonstrated 99% accuracy, with only one false negative (classified as ineligible by NLP but eligible by manual review). Efficiency gains were significant: manual chart review required a median of 3 minutes per patient (range: 1–12), whereas the automated pipeline processed 100 patients in ~1 minute, representing a > 99% reduction in screening time. Conclusions: Automated NLP extraction is an accurate and scalable solution for identifying patients eligible for adjuvant CDK4/6i. By substantially reducing the time required for chart review, this tool can minimize treatment delays and ensure real-world adherence to changing FDA guidelines. Future work will compare this rules-based approach with ML and LLM-based extractors to improve semantic context handling and scalability across health systems. Eligibility classification performance of regex-based pipeline compared to manual chart review. Metric NLP/Regex-based pipeline performance Accuracy 99.0% Sensitivity (Recall) 100.0% Specificity 98.9% Precision 91.7% F1 Score 95.7%

**Решение:** -4 breast cancer clinical trial eligibility screening

---

### 591 · R3145

**Performance of Chatgpt in Simulated Anesthesia Scenarios: A Prospective Comparison with Expert Clinicians**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-8384638/v1

Abstract Background: This study aimed to evaluate the diagnostic accuracy and clinical validity of ChatGPT’s responses in standardized anesthesia-related scenarios by directly comparing them with expert anesthesiologists' assessments. Methods: A prospective comparative study was conducted using sixteen hypothetical clinical scenarios reflecting common and critical perioperative conditions (e.g., anaphylaxis, malignant hyperthermia, pulmonary embolism). Two anesthesiologists independently evaluated the scenarios, and their responses were compared with those generated by ChatGPT (OpenAI, San Francisco, USA). A structured framework assessed diagnosis accuracy, treatment appropriateness, and compliance with international guidelines. Ratings were assigned using a 4-point Likert scale. Inter-rater agreement was analyzed using Cohen’s kappa and weighted kappa statistics. Descriptive statistics were used for categorical variables, and a p-value Results: ChatGPT correctly identified the diagnosis in 88% (14/16) of scenarios, recognized treatment necessity in 93% (15/16), and recommended the correct first-line treatment in 81% (13/16), yielding an overall concordance of 87%. Inter-rater reliability between the two experts was almost perfect (κ = 0.82). Substantial agreement was observed between ChatGPT and Expert 1 (κ = 0.74) and Expert 2 (κ = 0.71). ChatGPT performed best in life-threatening emergencies but showed limitations in therapeutic sequencing and drug dosage specification. Conclusions: ChatGPT demonstrated substantial agreement with expert anesthesiologists in high-stakes scenarios, suggesting potential as an adjunctive tool for education and simulation. However, its current limitations in therapeutic nuance and prioritization indicate that it should not be used as an independent clinical decision-making resource in anesthesia practice.

**Решение:** -4 ChatGPT in simulated anesthesia scenarios

---

### 592 · R2019

**Raahi AI: A Non-Directive AI for Self-Inquiry**

2026 · INTERANTIONAL JOURNAL OF SCIENTIFIC RESEARCH IN ENGINEERING AND MANAGEMENT · journalarticle, article · https://doi.org/10.55041/ijsrem60913

Abstract Contemporary large language models (LLMs) are predominantly engineered to maximize answer utility — producing solutions, recommendations, and directive guidance in response to user queries. This paper presents Raahi AI, a conversational AI system designed around an opposing epistemological premise: that genuine psychological self-inquiry is obstructed, not aided, by the delivery of answers. Drawing on the philosophy of Jiddu Krishnamurti — specifically his contention that truth emerges through observation rather than prescribed method — and operationalizing structural parallels with Person-Centered Therapy (PCT) and Motivational Interviewing (MI), we propose a constraint-based prompt architecture that encodes non-directive, dependency-reducing behavior into GPT-4o via MERN stack integration. The system's three core behavioral axioms — (1) problems are symptoms, not roots; (2) dependency on answers is itself the pathology; (3) observation precedes solution — are translated into concrete prompt constraints and evaluated against a custom behavioral rubric. Raahi AI does not advise, diagnose, or solve; it surfaces the questioner's own assumptions through Socratic reflection. Results suggest LLMs can be reliably constrained to simulate a fundamentally different epistemological stance, opening new directions in reflective AI design.

**Решение:** -6 Raahi AI non-directive conversational agent architecture

---

### 593 · R11952

**Purpose Model Simulation - Purpose Formation of Multi-stakeholder by Dialog with LLM-Based AI**

2024 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-031-59988-0_7

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 purpose model simulation dialog with AI

---

### 594 · R10845

**Leveraging Prompt Engineering and Large Language Models for Automating MADRS Score Computation for Depression Severity Assessment**

2024 · Ital-IA · journalarticle

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T3 automating MADRS depression severity score computation from clinical text; no abstract, eligible on full text

---

### 595 · R1109

**A Comparative Analysis of Expert and AI-Driven Qualitative Data Analysis: Evaluating ChatGPT’sCapabilities and Limitations**

2026 · Revista Española de Pedagogía · journalarticle, review, article · es · https://doi.org/10.9781/rep.2026.1813

This study evaluates the effectiveness of ChatGPT in analyzing qualitative data through a structured procedure designed to ensure comprehensive data collection and analysis. The study was designed as a qualitative case study employing a single embedded case study design. Firstly, semi-structured interviews were conducted with 20 students at a public university in Türkiye to examine their attitudes towards openness to new perspectives, collaboration, and sharing. Expert I carried out a content analysis of the interview transcripts. The findings from Expert I were then validated by Expert II to ensure consistency and accuracy. The same interview transcripts were analyzed using ChatGPT. Expert III reviewed and compared the analyses produced by both the human experts and ChatGPT. The findings indicated that while the human expert analysis offered more detailed and nuanced insights (including specific attitudes, conditions, and benefits), ChatGPT’s analysis was broader and more synthesized. The expert analysis provided more detailed insights into specific behaviors and situations, while ChatGPT offered a more accessible overview that emphasized general attitudes and behaviors.

**Решение:** -4 qualitative analysis of university student attitudes toward collaboration

---

### 596 · R7092

**MenstLLaMA: A Specialized Large Language Model for Menstrual Health Education in India**

2025 · medRxiv · preprint, ppr · en · https://doi.org/10.1101/2025.01.22.25320466

Abstract Background The quality and accessibility of menstrual health education in developing nations, including India, remain inadequate due to challenges such as poverty, social stigma, and gender inequality. While community-driven initiatives aim to raise awareness, artificial intelligence (AI) offers a scalable solution for disseminating accurate information. However, existing general-purpose large language models (LLMs) are ill-suited for this task, suffering from low accuracy, cultural insensitivity, and overly complex responses. To address these limitations, we developed MenstLLaMA, a specialized LLM tailored to the Indian context, designed to deliver menstrual health education empathetically, supportively, and accessible. Objective To develop and evaluate MenstLLaMA, a specialized LLM tailored to deliver accurate, culturally sensitive menstrual health education, and to assess its effectiveness compared to existing general-purpose models. Methods We curated MENST, a novel domain-specific dataset comprising 23,820 question-answer pairs, aggregated from medical websites, government portals, and health education resources. This dataset was systematically annotated with metadata capturing age groups, regions, topics, and socio-cultural contexts. MenstLLaMA was developed by fine-tuning Meta-LLaMA-3-8B-Instruct using Parameter Efficient Fine-Tuning (PEFT) with Low-Rank Adaptation (LoRA) techniques to achieve domain alignment with reduced computational overhead. We benchmarked MenstLLaMA against nine state-of-the-art general-purpose LLMs, including GPT-4o, Claude-3, Gemini 1.5 Pro, Mistral, and others. The evaluation followed a multi-layered framework: (1) automatic evaluation using BLEU, METEOR, ROUGE-L, and BERTScore metrics (2) expert evaluation by clinical experts (N=18) rating 200 expert-curated queries (3) medical practitioner interaction using an interactive chatbot (ISHA) for qualitative assessment across Relevance, Understandability, Preciseness, Correctness and Context sensitivity and (4) a user study with volunteer participants (N=200) evaluating MenstLLaMA in 15–20 minute randomized sessions for user satisfaction assessment on performance across seven qualitative metrics. Results MenstLLaMA achieved the highest BLEU (0.059) and BERTScore (0.911), outperforming GPT-4o (BLEU: 0.052, BERTScore: 0.896) and Claude-3 (BERTScore: 0.888). Clinical experts preferred MenstLLaMA’s responses over gold-standard answers in several culturally sensitive cases. In evaluation by medical practitioners ISHA, the chat interface of MenstLLaMA, it scored 3.5 in Relevance, 3.6 in Understandability , 3.1/5 in Preciseness , 3.5/5 in Correctness , and 4.0/5 in Context Sensitivity . User evaluations indicated strong ratings for Understandability (4.7/5), Relevance (4.3/5), Preciseness (4.28/5), Correctness (4.1/5), Tone (4.6/5), Flow (4.2/5), and Context Sensitivity (3.9/5). Conclusions MenstLLaMA demonstrates exceptional accuracy, empathy, and user satisfaction in menstrual health education, bridging critical gaps left by general-purpose LLMs. Its potential for integration into broader health education platforms positions it as a transformative tool for menstrual well-being. Future research may explore its long-term impact on public perception, menstrual hygiene practices, expanding demographic representation, enhancing context sensitivity, and integrating multi-modal and voice-based interactions for broader accessibility.

**Решение:** -4 MenstLLaMA: menstrual health education in India

---

### 597 · R3665

**Prompt Archaeology: A Five-Stage Protocol for Documenting and Analysing Human-AI Research Dialogues**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.20775191

Prompt Archaeology proposes a five-stage protocol for retrospectively documenting, classifying, and descriptively analysing the recoverable prompt exchanges that shaped a human-AI research project, including human-to-LLM, LLM-to-sub-agent, and cross-model prompts. As large language models become research instruments, records of questions, corrections, and appraisals can help reconstruct an inquiry. Prompt Archaeology treats these recoverable exchanges as retrospective research artefacts. The proposal defines five intended plain-text artefacts, an eight-type prompt taxonomy, a minimum reporting-and-redaction set, and three proposed automation routes. Effort estimates are planning figures, not measured implementation performance. A partial, author-produced and author-coded pilot records 208 source-labelled entries (127 human, 81 LLM). These are recorded labels, not independently authenticated actor identities. The eight-type partition of the 127 human-labelled prompts is arithmetically consistent, but topic- and day-level aggregates remain unreconciled. A separately auditable Stage-1 inclusion/exclusion record is not established in the available pilot package. The earlier 30% topic-rate contrast is withdrawn; the pilot does not establish learning, knowledge quality, a causal effect, or a validated cross-model dispatch. (i) Contribution: a proposed five-stage documentation workflow, an eight-class taxonomy, explicit reporting contracts, and proposed automation routes; (ii) Evidential status: a partial, self-coded illustration; no complete audited implementation, public dialogue dataset, or external empirical validation is supplied; (iii) Evidence boundaries: retained-hash agreement tests internal consistency, not external origin, signatures, authorisation, enforcement, or legal compliance. External human inter-coder reliability and repeated-run stability remain open; an LLM-to-LLM agreement diagnostic is not human inter-rater validation; (iv) Positioning: relates to protocol analysis, dialogue-act tagging, qualitative reporting, and agent provenance literature. Surveys and other systems' security mechanisms motivate the proposal without validating its schema, tooling, or protections. This corrective v1.1 record remains an advanced methods research draft. It publishes the synchronised English and German manuscript PDFs only. Private dialogue material, CaseStudy2, implementation fixtures, and draft datasets are outside this record. Further case studies, corpus reconciliation, and independent human coding remain future work. Changes in Version 1.1 (October 2026) Corrective revision following the September inventory; no new empirical validation is claimed. Reframed the protocol, artefacts, automation routes, and pilot as an unvalidated proposal and partial illustration. Qualified recorded actor labels and the missing auditable Stage-1 record; withdrew the unsupported 30% topic-rate contrast and bounded unreconciled aggregates. Separated internal hash consistency from external provenance, authentication, enforcement, and compliance. Corrected the scope of agent-provenance literature and distinguished LLM-to-LLM agreement from independent human inter-coder reliability. Updated candid AI assistance disclosure and publication availability. DE and EN contain the same corrections, 34 cited keys, and eight labels. Released two separately readable manuscript PDFs. The historical v1.0 combined PDF remains with v1.0; no new combined PDF, private dataset, or Paper-2 manuscript is uploaded. Changes in Version 1.0 (June 2026) Initial release. Five-stage protocol with defined cumulative artefacts and an eight-type prompt taxonomy. Minimum Reporting and Redaction Set, plus three automation routes with effort estimates. Single illustrative pilot (208 prompts) with a full, mutually exclusive type distribution; presented as illustration, not validation. Prominent limitations: circular self-coded demonstration, recommended-but-uncomputed reliability metrics, single case study. DE/EN: English and German PDFs published synchronously; combined PDF generated from EN plus DE. Advanced methods research draft. This corrective version constrains the pilot and provenance claims; it does not supply a complete audited implementation, public dialogue corpus, external empirical validation, or independently coded human inter-rater study.

**Решение:** -6 prompt archaeology documentation protocol

---

### 598 · R1539

**Comparative Evaluation of Gemini 3.0- and ChatGPT 5.0-Generated Regional Language Informed Consent Forms in Ophthalmology: A Dual-Rater Study in Hindi and Kannada.**

2026 · Cureus · journal article, journalarticle, article · eng · https://doi.org/10.7759/cureus.105551

PURPOSE: To evaluate the accuracy, linguistic quality, clinical completeness, and real-world applicability of informed consent forms generated in Indian regional languages (Hindi and Kannada) by two large language model-based chatbots for common ophthalmic surgical procedures. METHODS: In this comparative, blinded observational study, two chatbots (Gemini 3.0 (Google, California, USA) and ChatGPT 5.0 (OpenAI, California, USA)) were prompted to generate informed consent documents in Hindi and Kannada for five ophthalmic scenarios: cataract surgery, traumatic corneal perforation repair, therapeutic penetrating keratoplasty, orbitotomy, and squint surgery. Outputs were independently assessed by four ophthalmologist raters (two for each language) using a 10-point scoring system based on correctness, completeness, language and readability, clinical relevance, and real-world applicability. Descriptive statistics were calculated. Paired t-tests were used to compare chatbot performance, effect sizes (Cohen's d) were estimated, and inter-rater reliability was assessed using intraclass correlation coefficients (ICCs). RESULTS: Across both languages, Gemini 3.0 demonstrated more consistent performance and higher combined mean scores. In the Hindi cohort, combined mean scores were comparable between Gemini 3.0 (7.85) and ChatGPT 5.0 (8.00), with significant rater-dependent preference variability. In contrast, in the Kannada cohort, Gemini 3.0 significantly outperformed ChatGPT 5.0 (8.8 vs 7.7, p<0.01), with large to extremely large effect sizes (Cohen's d: 1.23-3.8). Inter-rater reliability was moderate to good for Gemini 3.0 (ICC: 0.62-0.71) and lower for ChatGPT 5.0 (ICC: 0.38-0.59). ChatGPT 5.0 exhibited frequent grammatical and terminological inaccuracies, particularly in Kannada, affecting clinical usability. CONCLUSION: Large language models can generate clinically usable informed consent forms in Indian regional languages; however, performance varies significantly between models. Gemini 3.0 demonstrated superior linguistic accuracy, consistency, and clinical suitability. Language-specific validation and mandatory human oversight are essential before clinical implementation.

**Решение:** -4 ophthalmology informed consent forms in regional Indian languages

---

### 599 · R11505

**LLM conversation rating tool used by annotators.**

2024 · https://doi.org/10.1371/journal.pdig.0000431.s007

Large language models (LLMs) have shown promise for task-oriented dialogue across a range of domains. The use of LLMs in health and fitness coaching is under-explored. Behavior science frameworks such as COM-B, which conceptualizes behavior change in terms of capability (C), Opportunity (O) and Motivation (M), can be used to architect coaching interventions in a way that promotes sustained change. Here we aim to incorporate behavior science principles into an LLM using two knowledge infusion techniques: coach message priming (where exemplar coach responses are provided as context to the LLM), and dialogue re-ranking (where the COM-B category of the LLM output is matched to the inferred user need). Simulated conversations were conducted between the primed or unprimed LLM and a member of the research team, and then evaluated by 8 human raters. Ratings for the primed conversations were significantly higher in terms of empathy and actionability. The same raters also compared a single response generated by the unprimed, primed and re-ranked models, finding a significant uplift in actionability and empathy from the re-ranking technique. This is a proof of concept of how behavior science frameworks can be infused into automated conversational agents for a more principled coaching experience.</div

**Решение:** -2 human raters evaluating empathy and actionability in LLM health coaching conversations

---

### 600 · R6623

**LLM-as-a-Judge for mental support: A meta-evaluation using domain-specific platform data**

2026 · Electronic Markets · journalarticle, article · en · https://doi.org/10.1007/s12525-026-00890-3

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T4 LLM-as-a-judge for mental support platform data; no abstract, eligible on full text
