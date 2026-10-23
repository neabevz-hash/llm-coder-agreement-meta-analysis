# Ручной отбор, часть 5

Ручной отбор, часть 5: записи 601–750 из 1000. Эти записи вы размечаете сами, вместо проходов ИИ (deviations.md, D3); это случайные 1000 записей из тех, что ИИ ещё не разметил (зерно 20261024). **Меток ИИ здесь нет и не будет.** Ваше решение окончательное: «+» и «?» идут на полный текст. Размечайте в любом порядке и в несколько заходов.

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

### 601 · R6468

**Human-Centered Evaluation of Ambient Artificial Intelligence Clinical Documentation**

2026 · eScholarship (California Digital Library) · dissertation · https://escholarship.org/content/qt16q8p5zk/qt16q8p5zk.pdf

Ambient artificial intelligence (AI) documentation tools convert patient–clinician conversations into draft clinical notes that clinicians review and modify before signing in the electronic health record (EHR). These systems are increasingly adopted as a response to documentation burden and clinician burnout, but real-world effectiveness depends on the amount of clinician revision required for AI drafts and on persistent barriers that limit uptake and sustained use. This dissertation presents a human-centered, multi-level evaluation of ambient AI documentation conducted within the University of California, Irvine Health (UCI Health).First, the implementation of ambient AI documentation was evaluated using a mixed-methods approach that paired EHR time-efficiency measures with pre- and post-implementation survey responses from outpatient clinicians at UCI Health across multiple specialties. Results indicated that time spent on documentation decreased, while note length increased during the three-month period following implementation. Survey findings aligned with these trends, reflecting improved perceived efficiency and reduced documentation burden.Second, clinicians’ edits of ambient AI drafts were quantified at scale using AI draft and clinician-finalized note pairs. Across notes that contained one or more ambient AI–generated note sections, 84.4% were revised by clinicians before signing. Editing intensity was highest in the Assessment and Plan section, while the tendency to accept drafts without edits varied primarily across individual clinicians rather than across specialties.Third, a qualitative content analysis was conducted using a manually annotated corpus of sentence-level edits derived from draft and final note pairs. The analysis identified recurring patterns in clinicians’ revisions to AI drafts, including adding specialty-specific details, calibrating certainty to reflect available evidence and diagnostic framing, and converting transcript-like narratives into professional documentation. Using this annotated dataset, few-shot prompting of large language models (LLMs) was evaluated to assess the feasibility of scalable automated edit measurement across five target categories. Results indicated that LLM-assisted classification was most reliable when the revision could be inferred from the local before-and-after text alone and less consistent when accurate classification required broader clinical context.Finally, semi-structured interviews with clinicians who use ambient AI in routine practice were conducted to understand the rationale behind editing AI-drafted notes. Clinicians described editing as a deliberate process to ensure accuracy, align drafts with clinical reasoning and documentation standards, and meet billing and medico-legal requirements. Interviews further underscored the need for specialty-aware customization and workflow support for efficient draft review and verification. Recommendations emphasized system-level optimization across model behavior, individual personalization, workflow design, and EHR integration.Collectively, these findings highlight that effective ambient AI implementation must align with clinical documentation standards, support specialty-specific workflows, and enable clinicians to efficiently verify, refine, and structure notes. By clarifying how ambient AI is used in routine practice, what revisions clinicians make, and why those revisions occur, this dissertation provides practical evidence and guidance to inform implementation, continuous monitoring, and iterative design improvements, ultimately aiming to reduce documentation burden while maintaining high-quality clinical records.

**Решение:** -4 ambient AI clinical documentation for EHR notes

---

### 602 · R2713

**Optimizing small local language models for culturally competent mental health counseling: comparative evaluation with GPT-4o by psychiatrists (Preprint)**

2026 · JMIR AI · article · en · https://doi.org/10.2196/92470

BACKGROUND Large language models (LLMs) show promise for mental health counseling applications. However, their deployment faces significant challenges, including data privacy concerns requiring on-premise solutions, high operational costs, and Western-centric biases that limit cultural appropriateness for non-English speaking populations. OBJECTIVE This study aimed to develop and evaluate culturally competent small language models (SLMs) with approximately 7 to 8 billion parameters for Korean mental health counseling and to validate a 2-stage hybrid evaluation framework combining LLM-as-a-Judge screening with expert clinical validation. METHODS We constructed a dataset of 1558 diary-based counseling interactions from a Korean mental health mobile app (Maeumpyeonuijeom). Three Korean-optimized base models (SKT A.X 4.0 Light[7B], LG EXAONE 3.5 [7.8B], and Meta Llama 3.1[8B]) were fine-tuned using a hyperfitting strategy with high-rank low-rank adaptation (r=256) over 20 epochs. Inference parameters were optimized using GPT-5(gpt-5-2025-08-07) as an LLM-as-a-Judge. The optimized SLMs and GPT-4o(gpt-4o-2024-08-06) were evaluated by 10 board-certified psychiatrists (mean clinical experience approximately 10 years) on 50 counseling scenarios across 4 dimensions (individualization, supportiveness, cultural appropriateness, and safety) using 5-point Likert scales. Wilcoxon signed-rank tests with Holm correction were used for statistical comparison, and intraclass correlation coefficients (ICCs) assessed inter-rater reliability. RESULTS The SKT A,X 4.0 Light model achieved statistical equivalence with GPT-4o in supportiveness (mean 3.39, SD 0.74 vs mean 3.45, SD 0.90; P=.26) and cultural appropriateness (mean 3.30, SD 0.77 vs mean 3.29, SD 0.79; P=.58). The SKT A,X 4.0 Light model ranked first in cultural appropriateness among all models. Inter-rater reliability analysis revealed higher agreement among psychiatrists for local SLMs (ICC=0.575 for SKT in cultural appropriateness) compared with GPT-4o (ICC=0.211). GPT-4o maintained significantly higher safety scores than all SLMs (P<.001). The LLM-as-a-Judge demonstrated moderate-to-good correlation with human evaluation but showed a tendency to overestimate safety scores. CONCLUSIONS A 7-8 billion parameter SLM fine-tuned on culturally specific data can achieve performance comparable to GPT-4o (estimated 1.76 trillion parameters) in supportiveness and cultural appropriateness for mental health counseling. This represents a parameter efficiency gain of more than 99%, enabling on-premise deployment for enhanced privacy protection. However, the safety gap necessitates human expert oversight, and success depends on the availability of high-quality language-specific base models.

**Решение:** + T4 LLM-as-a-judge evaluation of mental health counseling dialogues compared with 10 psychiatrists

---

### 603 · R3419

**[Therapist augmentation by generative AI: concept and implementation of the GAINED feedback system at Osnabrück University].**

2026 · Psychotherapie (Heidelberg, Germany) · english abstract, journal article, article · ger · https://doi.org/10.1007/s00278-026-00860-2

The increasing widespread use of generative artificial intelligence (AI) is opening up new areas of application in psychotherapy. These include 1) chatbots for direct interaction between patients and AI, 2) training applications for therapists, in which therapists can practise with simulated AI patients and 3) augmentation applications, in which therapists are supported by automated documentation or feedback and decision-making tools. At the same time, there are ethical risks due to data protection issues, harmful output and secondary use of clinical models. At the psychotherapy outpatient clinic of the University of Osnabrück we are developing a new approach to therapist augmentation using an AI-supported feedback application, taking these risks into account. Based on robust incremental effects of feedback in psychotherapy as well as established research on the automatic identification of therapeutic constructs in psychotherapy transcripts, therapists receive feedback on intervention quality and mechanisms of action. The feedback is discussed with the patients to promote informed shared decision-making. Technical details as well as ethical and clinical aspects of implementation are presented. Finally, an outlook on future developments and evaluation of the feedback application are provided.

**Решение:** -1 concept paper and implementation of GAINED feedback system

---

### 604 · R2210

**From Symptom Networks to Conversation Networks: A Cross-Sectional Study Mapping the Topology of Suicide-Related Clinical Dialogue**

2026 · medRxiv · preprint, ppr · https://doi.org/10.64898/2026.09.27.26364136

Abstract Suicide risk assessment in clinical conversations relies on the sequential structure of therapist-patient dialogue, yet formal models of how suicide-related content emerges, transitions, and reciprocates across conversational turns are lacking. We applied network analysis to C-SSRS-coded utterances from psychotherapy sessions to characterize the topology and dynamics of suicide-related clinical communication. Transcripts of 110 psychotherapy sessions from the SPEAK-SAFE study were classified for suicidality relevance using the Qwen3-32B large language model with an adapted Columbia-Suicide Severity Rating Scale (C-SSRS) schema. From the suicidality-relevant utterances, we constructed a weighted directed category transition network. Centrality, reciprocity, clustering, assortativity, and path length metrics were computed. Independent human expert ratings for a session-level subsample of 30 sessions from this cohort showed substantial agreement with the LLM classifications (Spearman ρ = 0.885, ICC[2,1] = 0.708). The network was dominated by therapist inquiry. Reciprocity was high, and closeness centrality decreased monotonically with C-SSRS severity. Active suicidal ideation functioned as a bridge node from which escalation pathways to method, plan, and attempt categories originated. The network exhibited a hub-and-spoke topology with small-world characteristics. Suicide-related clinical dialogue is structured as a therapist-centered hub-and-spoke network with high reciprocity and a consistent severity-peripherality gradient. The extension of network theory from intra-individual symptom structures to inter-individual communication dynamics represents a methodological innovation demonstrated here as a proof of concept, with potential applications to clinical training, automated decision support, and multimodal risk assessment. clinical interviews clinical interviews Author Summary clinical interviews clinical interviewsWhen clinicians talk with patients about suicide risk, the conversation itself follows a pattern: the therapist asks, the patient answers, and the topic shifts from one aspect of risk to another. We wanted to know whether this back-and-forth has a describable structure, in the same way that networks of interacting symptoms have been used to describe mental disorders. Using a large language model, we automatically labeled which parts of 110 real psychotherapy conversations touched on suicidal thoughts, plans, or behaviors, and then built a network showing how the conversation moved between these topics. We found that the therapist’s questions sat at the center of this network, that the conversation frequently looped back to earlier topics, and that mentions of active suicidal thoughts acted as a gateway to discussion of more severe risk, such as specific plans or past attempts. This proof-of-concept approach offers a new way to visualize and quantify how suicide risk assessments unfold in real clinical dialogue, with potential future applications in clinician training and automated support tools.

**Решение:** + T3 C-SSRS classification of psychotherapy transcripts with Qwen3-32B vs independent human expert ratings (rho=0.885, ICC=0.708)

---

### 605 · R8320

**Large Language Models for Thematic Analysis in Healthcare Research: A Blinded Mixed-Methods Comparison with Human Analysts**

2025 · medRxiv · preprint, ppr · https://doi.org/10.64898/2025.12.25.25343031

Large language models (LLMs) are increasingly used for qualitative thematic analysis, yet evidence on their performance in analysing focus-group data, where polyvocality and context complicate coding, remains limited. Given the increasing role of such models in thematic analysis, there is a need for methodological frameworks that enable systematic, metric-based comparisons between human and model-based analyses. We conducted a blinded mixed-methods comparison of two general-purpose LLMs (ChatGPT-5 and Claude 4 Sonnet), an LLM-based qualitative coding application (QualiGPT), and blinded human analysts on an in-person focus-group transcript informing an AI-enabled digital health proposal. We evaluated deductive coding using a 10-code, 6-theme codebook against an expert consensus adjudication; inductive coding with a structured Likert-scale comparison to a reference-standard set of inductive themes generated by expert consensus; and manual quote verification of LLM segments to define LLM hallucination (evidence absent or non-supportive) and error rate (including partial matches and speaker-coded segments). During deductive coding against an expert consensus adjudication, large language models (LLMs) yielded a mean agreement of 93.5% (95% CI 92.5–94.5) with κ = 0.34 (95% CI 0.26–0.40); blinded human coders achieved 92.7% (95% CI 91.6–93.9) agreement with κ = 0.34 (95% CI 0.26–0.41). Mean Gwet’s AC1 was 0.92 (95% CI 0.90–0.93) for the blinded human analysis, and 0.93 (95% CI 0.92–0.94) for the LLM-assisted deductive analysis, reflecting high agreement despite the low overall code prevalence (7.8%, SD = 3.2%). Only one model achieved non-inferiority in inductive analysis of the transcript ( p = 0.043). The strict hallucination rate in inductive analysis was 1.2% (SD = 2.1%). LLMs were non-inferior to human analysts for deductive coding of the focus-group data, with variable performance in inductive analysis. Low hallucination but significant comprehensive error rates indicate that LLMs can augment qualitative analysis but require human verification. Author summary Qualitative research plays an important role in digital health, assisting in the implementation of healthcare technologies and innovations. However, analysing qualitative data in the form of focus groups is time-consuming and requires human expertise. Large Language Models (LLMs) are being increasingly used in qualitative research analysis, although evidence on their performance in analysing focus group data is limited. We compared the performance of LLMs to blinded human analysts in analysing a focus group transcript on AI implementations in healthcare. We used both qualitative and quantitative metrics to evaluate the performance of LLMs in thematic analysis. We found that the LLMs performed similarly to humans when applying pre-defined codes (deductive analysis), with a low rate of hallucination. However, in open-ended theme generation (inductive analysis) their performance was more variable, particularly in areas requiring interpretation of tone, nuance, or conversational context. These findings suggest that LLMs can be used to support interpretation of qualitative data, rather than replace human analysts. We provide a reproducible framework in analysing the performance of LLMs in qualitative analysis.

**Решение:** -4 thematic analysis of digital health technology proposal focus group

---

### 606 · R5293

**TRANSFORMASI ASESMEN MULTILITERASI: MENGUKUR CRITICAL THINKING DAN DIGITAL FLUENCY SISWA SEKOLAH DASAR DI ERA GENERATIVE AI**

2026 · EDUTECH Jurnal Inovasi Pendidikan Berbantuan Teknologi · journalarticle, article · https://doi.org/10.51878/edutech.v6i2.10888

The emergence of Generative Artificial Intelligence (Gen-AI) in elementary education has introduced the Pseudo-Digital Fluency phenomenon, a condition in which students appear technically proficient with digital tools but lack depth in critical thinking and information validation. This study aims to develop and validate a Multimodal-Based Multiliteracy Assessment Model capable of authentically measuring Critical Thinking and Digital Fluency among elementary school students in the Gen-AI era. This study employed a mixed methods approach integrating Research and Development (R&D) procedures using the ADDIE model with qualitative analysis. A limited field trial was conducted with 28 Phase B students (Grade 4) at SD Negeri 1 Sukosari in the 2025/2026 academic year. Content validity was assessed by two expert validators using Aiken's V index, while reliability was measured through inter-rater Percentage of Agreement. The results indicate that the developed assessment model achieved a highly feasible validity coefficient (Aiken's V = 0.89). Field trials revealed that students' ability to independently cross-check AI-generated information was the most critical weakness (71.50%), while their digital ethical resilience scored in the very high category (85.75%). The multimodal portfolio rubric demonstrated high reliability with an inter-rater agreement coefficient of 89.28%. As a transformative solution, this study produced the Digital Sandwich Strategy, integrating Scenario-Based Assessment, Digital Portfolio, and Metacognitive Reflection to ensure human reasoning remains central to the learning process amid advancing AI technology. ABSTRAK Munculnya Generative Artificial Intelligence (Gen-AI) di lingkungan pendidikan dasar memunculkan fenomena Pseudo-Digital Fluency, yakni kondisi di mana siswa tampak mahir secara teknis dalam mengoperasikan alat digital, namun mengalami defisit dalam kemampuan berpikir kritis dan validasi informasi. Penelitian ini bertujuan mengembangkan dan menguji Model Asesmen Multiliterasi Berbasis Multimodal yang valid dan reliabel untuk mengukur Critical Thinking dan Digital Fluency siswa sekolah dasar secara autentik di era Gen-AI. Penelitian ini menggunakan pendekatan mixed methods yang mengintegrasikan prosedur Research and Development (R&D) model ADDIE dengan analisis kualitatif. Uji coba terbatas dilakukan pada 28 siswa Fase B (Kelas 4) di SD Negeri 1 Sukosari tahun ajaran 2025/2026. Validitas isi instrumen diuji oleh dua pakar menggunakan indeks Aiken's V, sedangkan reliabilitas diukur melalui Percentage of Agreement antar-penilai. Hasil penelitian menunjukkan bahwa model asesmen yang dikembangkan memperoleh koefisien validitas sangat layak (Aiken's V = 0,89). Uji coba lapangan mengungkap bahwa kemampuan validasi silang (cross-check) siswa terhadap luaran AI merupakan titik lemah yang paling kritis (71,50%), sementara ketahanan etis digital siswa berada pada kategori sangat tinggi (85,75%). Reliabilitas rubrik portofolio multimodal terbukti tinggi dengan koefisien kesepakatan antar-penilai sebesar 89,28%. Sebagai solusi transformatif, penelitian ini menghasilkan Strategi Digital Sandwich yang mengintegrasikan Scenario-Based Assessment, Digital Portfolio, dan Refleksi Metakognitif untuk memastikan nalar manusiawi tetap menjadi pusat proses belajar di tengah dominasi teknologi AI.

**Решение:** -4 critical thinking and digital fluency in elementary education

---

### 607 · R11691

**Ranking LLMs by compression**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2406.14171

We conceptualize the process of understanding as information compression, and propose a method for ranking large language models (LLMs) based on lossless data compression. We demonstrate the equivalence of compression length under arithmetic coding with cumulative negative log probabilities when using a large language model as a prior, that is, the pre-training phase of the model is essentially the process of learning the optimal coding length. At the same time, the evaluation metric compression ratio can be obtained without actual compression, which greatly saves overhead. In this paper, we use five large language models as priors for compression, then compare their performance on challenging natural language processing tasks, including sentence completion, question answering, and coreference resolution. Experimental results show that compression ratio and model performance are positively correlated, so it can be used as a general metric to evaluate large language models. 7 pages, 4 tables

**Решение:** -6 ranking LLMs by lossless data compression

---

### 608 · R7491

**Does Less Hallucination Mean Less Creativity? An Empirical Investigation in LLMs**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2512.11509

Large Language Models (LLMs) exhibit remarkable capabilities in natural language understanding and reasoning, but suffer from hallucination: the generation of factually incorrect content. While numerous methods have been developed to reduce hallucinations, their impact on creative generations remains unexplored. This gap is particularly critical for AI-assisted scientific discovery, which requires both factual accuracy and creative hypothesis generation. We investigate how three hallucination-reduction techniques: Chain of Verification (CoVe), Decoding by Contrasting Layers (DoLa), and Retrieval-Augmented Generation (RAG), affect creativity in LLMs. Evaluating multiple model families (LLaMA, Qwen, Mistral) at varying scales (1B - 70B parameters) on two creativity benchmarks (NeoCoder and CS4), we find that these methods have opposing effects on divergent creativity. CoVe enhances divergent thinking, DoLa suppresses it, and RAG shows minimal impact. Our findings provide guidance for selecting appropriate hallucination-reduction methods in scientific applications, where the balance between factual accuracy and creative exploration is crucial. Accepted at the AAAI 2026 Workshop on AI for Scientific Research (AI4Research)

**Решение:** -6 hallucination vs creativity in LLMs

---

### 609 · R3956

**AI-Powered Documentation for Mental Health Providers: Retrospective Observational Mixed Methods Study.**

2026 · JMIR formative research · journal article, observational study, study · eng · https://doi.org/10.2196/84628

Abstract Background Mental health providers (MHPs) face a significant administrative burden from documentation, which can contribute to burnout and reduce time available for direct patient care. Although artificial intelligence (AI)–powered scribes have shown promise in general medical settings, their utility has not been well explored in the specific context of mental health care. This study describes the development and preliminary observational evaluation of Smart Notes, a generative AI tool designed to assist MHPs with documentation on a commercial virtual mental health platform. Objective This study aimed to examine MHPs’ use and uptake of a generative AI documentation tool, including use patterns, perceptions of note quality, feedback and satisfaction, and changes in productivity. Methods Smart Notes was developed using a HIPAA (Health Insurance Portability and Accountability Act)-compliant Azure OpenAI infrastructure to securely generate session summaries from individual therapy sessions. The tool was rolled out to MHPs in a phased approach, and its use required MHP and client consent as well as a mandatory review and edit by the MHP. We conducted a 1-year retrospective observational evaluation of the feature, examining MHP use, MHP-rated note quality, MHP feedback and satisfaction, and MHP productivity (weekly working hours, session completion rate, and client caseload). Results Over 1 year, 162 full-time and 1366 contractual MHPs used Smart Notes to generate over 286,000 clinical notes. Use of the feature was high and stable, with nearly all (averaging 94% each week, SD 1%) full-time MHPs and most (averaging 72% each week, SD 6%) contractual MHPs using it weekly for eligible individual therapy sessions after the full launch. MHP-rated note quality was overwhelmingly positive, with 97.7% (9980/10,219) of feedback ratings among full-time MHPs and 98.4% (19,977/20,300) of feedback ratings among contractual MHPs being a “thumbs-up.” Qualitative feedback from MHPs was also largely positive, praising the tool for saving time and easing administrative burden. Finally, both full-time and contractual MHPs demonstrated changes in productivity. Conclusions Our findings suggest that AI-powered documentation tools, such as Smart Notes, are a feasible and acceptable approach to supporting MHPs. The high adoption rate and favorable MHP feedback indicate the potential utility of these tools without compromising note quality. This study provides preliminary data regarding the application of AI documentation in the mental health care context, highlighting a promising path for future research and development in digital mental health.

**Решение:** -4 usability study of ambient AI documentation scribes for mental health providers

---

### 610 · R11144

**LLM Plus Machine Learning Outperform Expert Rating to Predict Life Satisfaction From Self-Statement Text**

2024 · IEEE Transactions on Computational Social Systems · journalarticle, article · en · https://doi.org/10.1109/tcss.2024.3475413

This study explores an innovative approach to predicting individual life satisfaction by combining large language models (LLMs) with machine learning (ML) techniques. Traditional life satisfaction assessments rely on self-report questionnaires, which can be time-consuming and resource intensive. To address these limitations, we developed a method that utilizes LLMs for feature extraction from open-ended self-statement texts, followed by ML prediction. We compared this approach with standalone LLM predictions and expert ratings. A sample of 378 participants completed the satisfaction with life scale (SWLS) and wrote self-statements about their current life situation. The LLM-based ML model, using a LightGBM regressor, achieved a correlation of 0.542 with self-reported SWLS scores, outperforming both the standalone LLM ( r $=$ 0.491) and expert ratings ( r $=$ 0.455). Effect size analysis revealed a statistically significant moderate effect size difference between the LLM-based ML model and expert ratings (Cohen's d $=$ 0.499, 95% CI [0.043, 0.955]). These findings demonstrate the potential of integrating LLM and ML for an efficient and accurate assessment of life satisfaction, challenging conventional methods, and opening new avenues for psychological measurement. The study's implications extend to research, clinical practice, and policymaking, offering promising advancements in AI-assisted psychological assessment.

**Решение:** ? T2/T1 prediction of life satisfaction from text vs expert ratings and SWLS; check if direct LLM-expert agreement is reported

---

### 611 · R6141

**Beyond Reactive Empathy: Efficient RL for Proactive, Emotion-Adaptive, and LLM-based Mental Health Chatbot Design**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6128326

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 RL for emotion-adaptive mental health chatbot design

---

### 612 · R3489

**AI-Based Language Models (LLMs) in Assessing ESL Learners’ Speaking Skills: Opportunities and Limitations**

2026 · International Journal of Research Publication and Reviews · journalarticle, review, article · https://doi.org/10.55248/gengpi.07.1026.3240

Speaking is widely regarded as the most difficult skill to teach, practise, and assess in English as a Second Language (ESL) classrooms, largely because valid assessment of oral proficiency has traditionally depended on scarce resources: trained human raters, controlled testing conditions, and considerable time. The recent emergence of large language models (LLMs) capable of real-time speech-to-text conversion, conversational interaction, and rubric-referenced feedback generation has renewed interest in automating parts of this process. This article critically reviews the opportunities and limitations of LLM-based tools for assessing and supporting the development of ESL learners’ speaking skills. It traces the evolution from earlier automatic speech-scoring systems grounded in automatic speech recognition (ASR) and statistical feature extraction to the current generation of generative, instruction-following language models capable of producing holistic and analytic feedback in natural language. Five categories of opportunity are identified — scalable formative feedback, on-demand conversational practice, rubric-referenced scoring support, fine-grained pronunciation and fluency diagnostics, and reduced speaking anxiety through low-stakes practice — alongside five categories of limitation: construct underrepresentation, accent- and dialect-related bias, hallucination and inconsistent reliability, washback effects and learner overreliance, and unresolved data-privacy and ethical concerns. Building on this synthesis, the article proposes a five-criterion framework — validity, reliability, fairness, transparency, and pedagogical alignment — intended to guide the responsible integration of LLM-based tools into ESL speaking instruction and assessment, and discusses implications for English-language teaching contexts such as Azerbaijan, where access to trained oral examiners is often constrained. The article concludes that LLMs are best positioned as a complement to, rather than a replacement for, human assessment of spoken English, and it outlines a research agenda for validating LLM-based speaking assessment against established testing standards

**Решение:** -4 assessing ESL learners speaking skills

---

### 613 · R6026

**The Persuasion-Prediction Gap: Outcome-Grounded Auditing of LLM Judges on Market Resolved Financial and Crypto Reasoning**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7147562

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 outcome-grounded auditing of LLM judges on financial and crypto reasoning

---

### 614 · R2550

**Decoding I, You, and We in Crisis Communication: A Three-Phase LLM-Based Validation of Self-Oriented Model of Digital Publics (SOMP)**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6140251

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 crisis communication in PR and media

---

### 615 · R11836

**Llm-Based Conversational Agents for Behaviour Change Support: A Randomized Controlled Trial Examining Efficacy, Safety, and the Role of User Behaviour**

2024 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.4917769

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 RCT of conversational agent intervention for behaviour change support

---

### 616 · R6427

**Harnessing AI and social media to understand real-world patient experiences in systemic lupus erythematosus**

2026 · medRxiv · preprint, ppr, review · https://doi.org/10.64898/2026.02.20.26346724

ABSTRACT Objective To apply large language models (LLMs) to Reddit posts referencing systemic lupus erythematosus (SLE) to identify patient-expressed unmet medical needs, symptom experiences, and healthcare challenges, demonstrating how AI-enabled social media listening complements traditional patient-experience research. Methods We extracted 4,633 posts from ten SLE-related or health-focused Reddit communities using the public Reddit API (October–November 2025). After removing duplicates, promotional content, and posts with insufficient information, 2,603 posts remained. A thematic codebook was developed through manual review of 300 posts and iteratively refined. Two LLMs (Gemini 3.0 and GPT-5.2) were evaluated for automated thematic labeling using percent agreement, Cohen’s κ, and a human-annotated reference set (n=100). The best-performing model was used to quantify theme prevalence, followed by qualitative review of representative narratives. Results GPT-5.2 demonstrated higher performance (F1=0.844) than Gemini 3.0 (F1=0.811), with substantial inter-model agreement across main themes (mean κ=0.71). Posts reflected multidimensional experiences. The most frequent subtheme was Advice Seeking (84.1%), followed by Emotional Coping (55.6%). Common symptom-related themes included Pain (37.2%), Other Symptom Presentations (37.6%), Fatigue (24.7%), and Acute or Worsening Flares (30.2%). Diagnostic uncertainty was prominent, including confusion about laboratory results (24.0%) and emotional impact of uncertainty (33.0%). Qualitative review highlighted emotional distress, reliance on peer communities for interpretation of symptoms and labs, and difficulty managing complex treatment regimens. Conclusion LLM-enabled social media listening offers a scalable method for synthesizing large volumes of unstructured patient narratives, providing timely insights into lived experiences and unmet needs among individuals discussing lupus online. Findings align with established qualitative literature while highlighting persistent gaps in patient education, communication, and care coordination. This analytical framework can be applied across disease areas to support patient-centered care, measurement development, and evidence generation relevant to therapeutic and health-services research. What is already known on this topic People living with systemic lupus erythematosus (SLE) experience substantial unmet needs related to diagnostic uncertainty, symptom burden, emotional distress, medication challenges, and healthcare system barriers. Traditional qualitative methods (e.g., interviews, focus groups, surveys) capture valuable patient perspectives but are limited by small sample sizes, recall bias, and restricted question frameworks. Social media listening has emerged as a promising way to collect real-time patient insights, and recent regulatory guidance acknowledges its value as patient experience data. However, systematic, scalable analysis of large patient-generated datasets has historically been constrained by analytic burden and variability. What this study adds This study is among the first to apply state-of-the-art large language models (LLMs) to a large corpus of SLE-related social media posts, enabling scalable thematic analysis of thousands of patient narratives. It provides a validated methodological framework for using dual-LLM agreement, human-annotated references, and performance benchmarking (precision, recall, F1) to ensure reliability in automated thematic labeling. Findings reveal a multidimensional patient burden consistent with prior studies while uncovering persistent gaps in patient education, confusion around laboratory testing, care coordination challenges, and heavy reliance on peer communities for advice. The approach demonstrates that LLM-enabled social media listening can generate timely, granular, patient-prioritized insights at a scale unattainable by traditional methods. How this study might affect research, practice, or policy Research: Establishes a reproducible, scalable framework for integrating LLM-based thematic analysis into patient-focused evidence generation, accelerating insight extraction from large unstructured datasets across disease areas. Clinical practice: Highlights actionable gaps in patient education, communication, and care coordination, informing interventions to improve clinical encounters, shared decision-making, and symptom management support. Policy and regulatory science: Demonstrates how social media–derived patient experience data, when paired with rigorous quality controls, can complement formal qualitative studies and support patient-focused drug development, measurement development, and health-services planning.

**Решение:** ? T1 thematic coding of patient experiences in systemic lupus erythematosus social media posts vs human annotators

---

### 617 · R11209

**ChatGPT for Writing Evaluation: Examining the Accuracy and Reliability of AI-Generated Scores Compared to Human Raters**

2024 · Exploring AI in Applied Linguistics · book-chapter · en · https://doi.org/10.31274/isudp.2024.154.06

ChatGPT has proven beneficial in a variety of educational contexts, yet its effectiveness in scoring integrated second-language writing tasks remains uncertain. This study, therefore, explores the accuracy and reliability of ChatGPT-generated scores versus human ratings under two prompting conditions (with or without writing prompt and source texts) and examines the reasons behind rating discrepancies using a mixed methods approach. ChatGPT rated 74 argumentative essays from the Iowa State University English Placement Test Corpus of Learner Writing under the different prompting conditions; its ratings were then compared with those of human raters. Compared to human raters, ChatGPT’s reliability was moderate to low. This was the case in both prompting conditions. In addition, a qualitative analysis of ChatGPT’s scoring rationales suggested that, unlike human raters, ChatGPT was limited in detecting content-related issues and integrating source text information. The findings of the study suggest that a more rigorous process may be required to train ChatGPT to rate similarly to human raters. https://www.iastatedigitalpress.com/plugins/books/154/chapter/123

**Решение:** -4 ChatGPT scoring ESL argumentative essays compared to human raters

---

### 618 · R10350

**C-VARC: A Large-Scale Chinese Value Rule Corpus for Value Alignment of Large Language Models**

2025 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-7901567/v1

Abstract Ensuring that Large Language Models (LLMs) align with mainstream human values and ethical norms is crucial for the safe and sustainable development of AI. Current value evaluation and alignment are constrained by Western cultural bias and incomplete domestic frameworks reliant on non-native rules; furthermore, the lack of scalable, rule-driven scenario generation methods makes evaluations costly and inadequate across diverse cultural contexts. To address these challenges, we propose a hierarchical value framework grounded in core Chinese values, encompassing three main dimensions, 12 core values, and 50 derived values. Based on this framework, we construct a large-scale Chinese Value Rule Corpus (C-VARC) containing over 250,000 value rules enhanced and expanded through human annotation. Experimental results demonstrate that scenarios guided by C-VARC exhibit clearer value boundaries and greater content diversity compared to those produced through direct generation. In the evaluation across six sensitive themes (e.g., sur-rogacy, suicide), seven mainstream LLMs preferred C-VARC generated options in over 70.5% of cases, while five Chinese human annotators showed an 87.5% alignment with C-VARC, confirming its universality, cultural relevance, and strong alignment with Chinese values. Additionally, we construct 400,000 rule-based moral dilemma scenarios that objectively capture nuanced distinctions in conflicting value prioritization across 17 LLMs. Our work establishes a culturally-adaptive benchmarking framework for comprehensive value evaluation and alignment, representing Chinese characteristics.

**Решение:** -6 Chinese Value Rule Corpus benchmark for LLM cultural value alignment

---

### 619 · R3874

**How Are Emerging Adults Using ChatGPT in the Wild?**

2026 · Proceedings of the AAAI/ACM Conference on AI Ethics and Society · journalarticle, conference, conference-paper · en · https://doi.org/10.1609/aies.v9i4.43340

General-Purpose Conversational Agents (GPCAs) such as ChatGPT have rapidly become part of emerging adults’ everyday lives. Despite significant research attention on conversational agents for young people, we lack systematic documentation of what social support emerging adults seek from GPCAs and how these systems respond in the wild. In this study, we collected ChatGPT usage histories from 85 emerging adults (ages 18–25), comprising approximately 157,000 messages exchanged over three years across 17 countries. Through mixed-methods analysis combining reflexive thematic analysis with LLM-as-a-Judge, we identified distinct usage patterns across four developmentally sensitive domains such as Self-Sufficiency and Health & Well-Being. We further identified ChatGPT response patterns such as Competence-Thwarting Support, Emotional Co-Regulation, and Creativity Support, and synthesized these findings into a design space for developmentally supportive GPCAs.

**Решение:** -6 mixed-methods analysis of emerging adults everyday ChatGPT usage histories

---

### 620 · R8334

**Obsolete on Arrival - Rethinking Education in the Age of Autonomous Intelligence**

2025 · Alexander Holtermann · journalarticle/ · https://doi.org/10.5281/zenodo.15598129

The Fourth Industrial Revolution introduced digitalization, automation, and early artificial intelligence into the fabric of economic and societal structures. However, recent advancements in generative artificial intelligence—especially language models capable of producing sophisticated text, logic, and code—have signaled the arrival of a new and more profound shift. This development marks the onset of what can now be termed the Fifth Industrial Revolution: an age in which machines not only execute programmed tasks but generate meaning, enabling them to interact within society's most sensitive and complex systems—education, law, science, and culture. Central to this transformation is the fact that AI now operates in natural language, the core medium of human reasoning, knowledge exchange, and organization. This article examines the resulting crisis within global education systems, which continue to function under paradigms suited to a pre-generative-AI world. Drawing from real-world pedagogical experiments in both higher education and vocational training contexts, alongside the author's own defense of two doctoral theses written entirely by AI and awarded highest distinction by human academic panels, the article provides empirical evidence that AI has reached a level of epistemic indistinguishability from human experts. These experiments collectively reveal that our educational institutions are fundamentally unprepared for this new reality. The piece calls for immediate and structural change—not only to curriculum and delivery models but to the epistemological foundations of what we consider learning, understanding, and human expertise.

**Решение:** -1 essay on rethinking education in the age of autonomous intelligence

---

### 621 · R3207

**Bonding With Bots: A Systematic Scoping Review of the Therapeutic Relationship in Gen-AI Mental Health Interventions.**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/ra8qd

Artificial intelligence (AI)–based mental health interventions, particularly those powered by Generative AI are increasingly deployed for mental health assessment, skills practice, and intervention delivery. While these tools promise effectiveness, scalability and personalization, little is known about how therapeutic alliance is measured, and experienced in AI-mediated contexts, from patient and clinician perspectives. The proposed scoping review will synthesize the rapidly growing literature on how the therapeutic relationship is measured in human-bot interactions in Generative AI-based mental health interventions, and its relationship with outcome. We will use the conceptualization of the digital therapeutic alliance (as defined by Kaveladze &amp; Scheuller., 2023; Malouin-Lachance et al., 2025) and build on previous systematic reviews on the digital therapeutic alliance conducted before the global uptake of Generative AI (e.g., Henson et al., 2019; Tong et al., 2023; van Lotringen et al., 2021). We will expand the scope of earlier reviews by including AI tools used by (a) patients (e.g., AI-delivered support or coaching) and (b) clinicians/trainees (e.g., simulated patients for skills training), and by including Chinese language studies. To be able to capture the rapid development in this interdisciplinary field we will also include pre-registered studies and conference proceedings, commonly used as publication outlet in the field of computer science. Our primary research questions are: (1) Which measures and operational definitions are used to assess the human-bot digital therapeutic alliance in Generative AI-based mental health contexts? (2) How does the digital therapeutic alliance levels compare to benchmarks from human-delivered psychotherapy? (3) What is the evidence that digital therapeutic alliance is associated with treatment outcomes and do these associations resemble the strength of alliance–outcome relations in human psychotherapy? Secondary questions will examine heterogeneity by modality (text-based vs audio/video or embodied avatar systems), population/user role (patient vs clinician/trainee), and geography/culture (e.g., China vs U.S. contexts). Methods will follow PRISMA guidance, including dual screening; standardized extraction of intervention characteristics (agent type, humanization features, modality, setting), relationship constructs and measures, and outcome metrics; and risk-of-bias appraisal. Eligible empirical studies will include Generative AI models capable of open-ended dialogue. Empirical studies must report on the digital therapeutic alliance in either quantitative or qualitative measurement. The systematic search will be conducted across multi-disciplinary databases: Embase, PubMed, IEEE Xplore, PsychInfo, Scopus, Web of Science Core Collection, ProQuest Dissertations and Theses Global, ACM Digital Library, as well as the Chinese database CNKI (including their theses and dissertation database). This review will directly address the special issue’s emphasis on conceptual coherence, trust, and clinician–patient engagement in AI-assisted interventions, while foregrounding ethical considerations: whether it is clinically and morally appropriate to engineer human-like relational bonds, and whether “high alliance” with an AI agent is uniformly desirable given risks of dependency, and miscalibration of trust.

**Решение:** -1 systematic scoping review of therapeutic relationship in Gen-AI mental health interventions

---

### 622 · R6697

**LLMs are Making You Sick: Uncovering the Overpathologizing Bias in Cognitive Distortion Detection**

2026 · IEEE Transactions on Affective Computing · journalarticle, article · https://doi.org/10.1109/taffc.2026.3710804

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T1 cognitive distortion detection overpathologizing bias; no abstract, eligible on full text

---

### 623 · R0681

**Search as a Convergent Force: How Information Retrieval Impacts Creative Quality and Narrative Diversity in Genai-Assisted Creative Learning**

2026 · International Conference on Advanced Learning Technologies · conference · https://doi.org/10.1109/icalt68022.2026.00101

Generative AI (GenAI) tools offer new opportunities for creative learning, yet their influence on output quality and narrative diversity remains underexplored. This study investigates how integrating information retrieval (IR) with GenAI affects creative learning outcomes. A controlled experiment compared twenty undergraduate architecture students $(\mathrm{N}=20)$ using GenAI alone versus GenAI with IR-augmented support during a narrative writing task. Creative quality and narrative diversity were assessed using expert ratings (Consensual Assessment Technique) and semantic similarity analysis (Sentence-BERT), respectively. Results indicate that accessing external information did not significantly improve creative quality $(\mathrm{p}=0.59)$, yet impacted narrative diversity. The GenAI + IR group produced narratives with higher semantic similarity (0.172) than the GenAI-only group (0.110). These findings suggest that external search acts as a convergent force, anchoring students to dominant discourses and reducing narrative diversity, highlighting a potential trade-off in AI-assisted learning.

**Решение:** -4 information retrieval and creative quality in GenAI-assisted creative learning

---

### 624 · R8238

**When AI meets source use: Exploring ChatGPT's potential in L2 summary writing assessment**

2025 · System · article · en · https://doi.org/10.1016/j.system.2025.103737

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 ChatGPT in L2 summary writing assessment

---

### 625 · R4089

**Toward Cultural Alignment: Human-Centered Evaluation of Multimodal AI Stories Across Five African Communities**

2026 · arXiv (Cornell University) · preprint/article, review, preprint · https://doi.org/10.48550/arxiv.2608.29209

In this paper, we examine how well AI-generated multimodal stories align with the lived practices, relationships, language, values, and visual expectations of the communities they represent. We conduct a community-grounded mixed-methods evaluation with 19 culture representatives across five African communities, combining quantitative annotations with qualitative focus group discussions. We find that cultural alignment depends not simply on recognizable cultural markers, but on how those markers fit social, linguistic, procedural, and visual context. From these evaluations, we develop a taxonomy of cultural alignment comprising five broader cultural marker categories and eight recurring mechanisms of misalignment. We additionally evaluate five multimodal LLM judges to examine whether automated evaluation can approximate community-grounded judgments at scale. Judge reliability and score calibration vary substantially across communities, with no single judge performing consistently across all five settings. These findings motivate community-calibrated evaluation pipelines in which automated judges are validated against community judgments to determine where they can be trusted and where human review remains necessary. Accepted to Findings of EMNLP 2026

**Решение:** -4 community evaluation of AI-generated stories across African communities

---

### 626 · R10956

**Reshaping free-text radiology notes into structured reports with generative question answering transformers.**

2024 · Artificial intelligence in medicine · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.1016/j.artmed.2024.102924

BACKGROUND: Radiology reports are typically written in a free-text format, making clinical information difficult to extract and use. Recently, the adoption of structured reporting (SR) has been recommended by various medical societies thanks to the advantages it offers, e.g. standardization, completeness, and information retrieval. We propose a pipeline to extract information from Italian free-text radiology reports that fits with the items of the reference SR registry proposed by a national society of interventional and medical radiology, focusing on CT staging of patients with lymphoma. METHODS: Our work aims to leverage the potential of Natural Language Processing and Transformer-based models to deal with automatic SR registry filling. With the availability of 174 Italian radiology reports, we investigate a rule-free generative Question Answering approach based on the Italian-specific version of T5: IT5. To address information content discrepancies, we focus on the six most frequently filled items in the annotations made on the reports: three categorical (multichoice), one free-text (free-text), and two continuous numerical (factual). In the preprocessing phase, we encode also information that is not supposed to be entered. Two strategies (batch-truncation and ex-post combination) are implemented to comply with the IT5 context length limitations. Performance is evaluated in terms of strict accuracy, f1, and format accuracy, and compared with the widely used GPT-3.5 Large Language Model. Unlike multichoice and factual, free-text answers do not have 1-to-1 correspondence with their reference annotations. For this reason, we collect human-expert feedback on the similarity between medical annotations and generated free-text answers, using a 5-point Likert scale questionnaire (evaluating the criteria of correctness and completeness). RESULTS: The combination of fine-tuning and batch splitting allows IT5 ex-post combination to achieve notable results in terms of information extraction of different types of structured data, performing on par with GPT-3.5. Human-based assessment scores of free-text answers show a high correlation with the AI performance metrics f1 (Spearman's correlation coefficients>0.5, p-values<0.001) for both IT5 ex-post combination and GPT-3.5. The latter is better at generating plausible human-like statements, even if it systematically provides answers even when they are not supposed to be given. CONCLUSIONS: In our experimental setting, a fine-tuned Transformer-based model with a modest number of parameters (i.e., IT5, 220 M) performs well as a clinical information extraction system for automatic SR registry filling task. It can extract information from more than one place in the report, elaborating it in a manner that complies with the response specifications provided by the SR registry (for multichoice and factual items), or that closely approximates the work of a human-expert (free-text items); with the ability to discern when an answer is supposed to be given or not to a user query.

**Решение:** -4 structuring free-text radiology notes

---

### 627 · R9466

**Event segmentation applications in large language model enabled automated recall assessments.**

2025 · Communications psychology · journal article, journalarticle, preprint/article · eng · https://doi.org/10.1038/s44271-025-00359-7

Understanding how individuals perceive and recall information in their natural environments is critical to understanding potential failures in perception (e.g., sensory loss) and memory (e.g., dementia). Event segmentation, the process of identifying distinct events within dynamic environments, is central to how we perceive, encode, and recall experiences. This cognitive process not only influences moment-to-moment comprehension but also shapes event specific memory. Despite the importance of event segmentation and event memory, current research methodologies rely heavily on human judgements for assessing segmentation patterns and recall ability, which are subjective and time-consuming. A few approaches have been introduced to automate event segmentation and recall scoring, but validity with human responses and ease of implementation require further advancements. To address these concerns, we leverage Large Language Models (LLMs) to automate event segmentation and assess recall of written narratives, employing chat completion and text-embedding models, respectively. We validated these models against human annotations and determined that LLMs can accurately identify event boundaries, and that human event segmentation is more consistent with LLMs than among humans themselves. Using this framework, we advanced an automated approach for recall assessments which revealed semantic similarity between segmented narrative events and participant recall can estimate recall performance. Our findings demonstrate that LLMs can effectively simulate human segmentation patterns and provide recall evaluations that are a scalable alternative to manual scoring. This research opens avenues for studying the intersection between perception, memory, and cognitive impairment using methodologies driven by artificial intelligence. Large language models automate event segmentation and recall scoring with human-level accuracy. LLMs identify event boundaries more consistently than humans themselves, while semantic embeddings enable scalable memory assessments, advancing AI-driven cognitive research.

**Решение:** + T2 LLM automated event segmentation and narrative recall scoring for memory/cognitive assessment validated against human annotations

---

### 628 · R1957

**GNR-Net: An Explainable Generative–Graph Neural Framework for Narrative Representation and Valuation**

2026 · IEEE Access · article · https://doi.org/10.1109/access.2026.3658160

The increasing volume of creative narratives, such as screenplays and scripts, presents both opportunities and challenges for computational understanding and valuation. Traditional expert-driven assessments are subjective and limited in scalability, while existing text-based models struggle to capture the causal, emotional, and structural dimensions of storytelling. To address these challenges, this study proposes GNR-Net, an explainable Generative AI (GenAI) and Graph Neural Networks (GNNs) hybrid framework that integrates long-context large language modeling (LLM) with Knowledge Graph (KG) reasoning for interpretable narrative understanding and valuation. The framework comprises three components: a semantic graph construction module that transforms narrative texts into multi-relational KG structures; a generative narrative encoder based on LLaMA-3 that models long-range coherence and emotional causality and regularizes Narrative Coherence Score (NCS); and a narrative value estimator that combines relational graph convolution (R-GCN) reasoning with multi-head regression and adversarial calibration to quantify creativity, coherence, and market potential. Experiments on four screenplay corpora (IMSDb, ScriptBase, Cornell Movie Dialogs, and WGA Unproduced) demonstrate that GNR-Net outperforms nine baselines, achieving up to 13.2% MAE reduction and 0.82 Pearson correlation with expert ratings. Ablation and visualization analyses further show that jointly leveraging generative semantics and graph reasoning yields more faithful explanations linking emotional arcs to valuation dimensions. The proposed framework provides a practical pathway toward explainable computational creativity by bridging GenAI, GNN-based KG reasoning, and cultural data intelligence.

**Решение:** -4 explainable generative-graph neural framework for screenplay narrative valuation

---

### 629 · R8129

**Virtual Agent for Real-Time Motivational Interviewing by Integrating Adaptive Nonverbal Behavior and Language Models.**

2025 · Journal of visualized experiments : JoVE · journal article, video-audio media, research support, non-u.s. gov't · eng · https://doi.org/10.3791/69254

The growing demand for therapeutic support increasingly exceeds the capacity of available professionals. A virtual agent capable of performing motivational interviewing (MI) offers a promising solution to assist patients in reaching their goal of behavior change between sessions with human therapists. MI is inherently a cooperative and adaptive form of communication. Therefore, developing an agent capable of adapting its conversational strategies to the context could significantly enhance the effectiveness of therapy. During MI sessions, human therapists adjust both their verbal and nonverbal behaviors based on the human patients' responses, as well as their profiles. Depending on the patient's level of motivation, the therapist will modify their approach accordingly. Thus, personalization and adaptability are essential for developing effective MI virtual agents. In this paper, we present a virtual agent capable of conducting MI sessions by dynamically adapting verbally and nonverbally to users in real time. Leveraging state-of-the-art models, this system enables MI interactions. The virtual agent is embodied using the Greta 2.0 platform. Its nonverbal behavior is generated through a diffusion model called MODIFF, which adapts to the user's facial expressions and their readiness to change. These facial expressions were learned on an MI corpus and validated through a dedicated user study. The dialogue is generated using a state-of-the-art large language model (LLM), enhanced by a dialogue manager specifically designed for MI, with a reinforcement learning approach, and validated through user testing. Furthermore, the dialogue manager is able to adapt to different user profiles. The resulting platform is open-source and facilitates the generation of real-time, multimodal MI dialogues, providing new tools for digitally mediated therapeutic interactions.

**Решение:** -6 virtual agent for real-time motivational interviewing system design

---

### 630 · R9861

**How does generative artificial intelligence compare to human analysts in qualitative research?: A systematic review of large language models**

2025 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/gnx8p_v1

Introduction: Qualitative methods offer rich insights into human experience, yet the expanding volume of textual data presents analytic challenges. Generative AI, particularly large language models (LLMs), may help researchers organize and interpret qualitative data while maintaining depth and accuracy. It is important to assess the validity and practical suitability of LLMs for qualitative analysis. This systematic review evaluated the extent to which LLMs, specifically generative transformer models such as ChatGPT, can identify themes and patterns consistent with human analysts. Methods: Studies published up to June 2025 were retrieved from PubMed, PsycINFO, Web of Science, Google Scholar, and reference lists of included studies. Eligible studies directly compared LLM- and human-generated outputs derived from thematic, narrative, or discourse analyses. Results: Thirty-nine studies met inclusion criteria. Most used versions of ChatGPT (70.8%), while others utilized Gemini (8.3%), Claude (4.2%), among others. Comparative analyses spanned diverse disciplines, though standardized protocols for conducting LLM-assisted qualitative analysis were lacking. Overall, LLM performance relative to human analysts was rated as moderate to high. Among those studies reporting quantitative indexes, the median % agreement score was 0.80 (range: 0.19-1.00), median Cohen’s Kappa was 0.74 (range 0.38-0.82), and median Cosine coefficient was 0.58 (range: 0.47-0.80), with stronger alignment for semantic or descriptive themes and lower accuracy for interpretive, context-dependent themes. Discussion: Findings provide support for LLMs as complementary tools in qualitative data analysis. Rather than replacing human interpretation, LLMs may serve as efficient aids for data organization and inter-rater comparison to support, but not substitute, qualitative engagement.

**Решение:** -1 systematic review of LLMs compared to human analysts in qualitative research

---

### 631 · R0691

**AutoMalDesc: Large-Scale Script Analysis for Cyber Threat Research**

2026 · Underline Science Inc. · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48448/p7xk-mj13

Generating thorough natural language explanations for threat detections remains an open problem in cybersecurity research, despite significant advances in automated malware detection systems. In this work, we present AutoMalDesc, an automated static analysis summarization framework that, following initial training on a small set of expert-curated examples, operates independently at scale. This approach leverages an iterative self-paced learning pipeline to progressively enhance output quality through synthetic data generation and validation cycles, eliminating the need for extensive manual data annotation. Evaluation across 3,600 diverse samples in five scripting languages demonstrates statistically significant improvements between iterations, showing consistent gains in both summary quality and classification accuracy. Our comprehensive validation approach combines quantitative metrics based on established malware labels with qualitative assessment from both human experts and LLM-based judges, confirming both technical precision and linguistic coherence of generated summaries. To facilitate reproducibility and advance research in this domain, we publish our complete dataset of more than 100K script samples, including annotated seed (0.9K) and test (3.6K) datasets, along with our methodology and evaluation framework. Accepted at AAAI 2026 (oral)

**Решение:** -4 AutoMalDesc: automated malware script analysis and summarization

---

### 632 · R10882

**Cheap Ways of Extracting Clinical Markers from Texts**

2024 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, journalarticle, preprint/article · en · https://doi.org/10.18653/v1/2024.clpsych-1.25

This paper describes the work of the UniBuc Archaeology team for CLPsych's 2024 Shared Task, which involved finding evidence within the text supporting the assigned suicide risk level. Two types of evidence were required: highlights (extracting relevant spans within the text) and summaries (aggregating evidence into a synthesis). Our work focuses on evaluating Large Language Models (LLM) as opposed to an alternative method that is much more memory and resource efficient. The first approach employs a good old-fashioned machine learning (GOML) pipeline consisting of a tf-idf vectorizer with a logistic regression classifier, whose representative features are used to extract relevant highlights. The second, more resource intensive, uses an LLM for generating the summaries and is guided by chain-of-thought to provide sequences of text indicating clinical markers. https://github.com/nlp-unibuc/clpsych24-task

**Решение:** ? T3 CLPsych 2024 suicide risk evidence and clinical markers extraction; check agreement metrics

---

### 633 · R1024

**AI Safety Training Can be Clinically Harmful**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-9568253/v1

Abstract Large language models are being deployed as mental health support agents at scale, yet only 16\% of LLM-based chatbot interventions have undergone rigorous clinical efficacy testing \citep{hua2025charting}. We argue that the dominant alignment paradigm, RLHF-based safety training, can itself become a source of clinical harm when models are placed in protocol-driven psychotherapeutic settings. We evaluated four generative models on 250 Prolonged Exposure (PE) therapy scenarios \citep{suhas2025thousand} and 146 Cognitive Behavioral Therapy (CBT) cognitive restructuring exercises \citep{nie2024caiti} (plus 29 severity-escalated variants), scored by a three-judge LLM panel. All models score near-perfectly on surface acknowledgment ($\approx$0.91 to 1.00), while therapeutic appropriateness drops to 0.22 to 0.33 at the highest severity for three of four models and protocol fidelity reaches zero for two. Under CBT severity escalation, one model's task completeness falls from 92\% to 71\% while a frontier model's safety-interference score falls from 0.99 to 0.61. Across both modalities we observe a consistent pattern: safety-aligned models intervene with grounding, false reassurance, or crisis-resource insertion during therapy phases that require sustained engagement with distress, or abandon the therapeutic task entirely. These behaviors are protocol violations in PE and CBT despite being precisely what RLHF rewards in general conversation. We treat this as a perspective contribution: the central tension is between RLHF safety objectives and the mechanisms of action of evidence-based therapy, not a deficit in model capability. Because our evidence is built on synthetic scenarios and LLM judges, we report the findings as directional and call for clinician-adjudicated replication before any deployment claims.

**Решение:** -5 synthetic therapy scenarios evaluated only by LLM judges, no human raters

---

### 634 · R7540

**Artificial Intelligence in Neurology: Assessing the Diagnostic and Therapeutic Reasoning of Large Language Models.**

2025 · Cureus · journal article, journalarticle, review · eng · https://doi.org/10.7759/cureus.98570

Background Artificial intelligence (AI) and large language models (LLMs) are increasingly integrated into medicine, yet their role in clinical decision-making remains underexplored. Neurology provides an important testing ground for these systems because neurological diagnoses often involve complex, overlapping syndromes, subtle clinical distinctions, and time-sensitive decision-making that can significantly affect patient outcomes. Objective This study evaluated the diagnostic and therapeutic reasoning of three LLMs: ChatGPT 4.0, Google Gemini, and Claude 3.5 Sonnet, using a complex neurological case of acute Guillain-Barré syndrome (GBS) in the setting of chronic spinal epidural lipomatosis (SEL). Methods Each model was prompted with an identical case and instructed to generate both a diagnostic assessment and a treatment plan. Four blinded, board-certified neurologists assessed outputs using a standardized rubric across four domains: diagnostic accuracy, differential diagnoses, intervention plan, and monitoring/follow-up. Results All three models correctly identified GBS and proposed guideline-consistent therapies (IVIG, plasmapheresis). Claude 3.5 Sonnet achieved the highest mean total score (18.5/20), followed by ChatGPT (17.5) and Google Gemini (17.25). Domain-level scoring demonstrated distinct performance patterns: Google Gemini scored highest in primary diagnosis, Claude 3.5 Sonnet achieved the only perfect mean score in differential diagnoses and led in intervention planning, while ChatGPT performed strongest in monitoring and follow-up recommendations. Although all models produced clinically appropriate assessments and plans, none matched the physician's gold standard in contextualizing SEL-specific considerations or developing detailed, longitudinal management strategies. These findings reflect descriptive reviewer assessments only; no inferential statistical testing was performed due to the study's single-case design. Conclusions These findings highlight both the promise and limitations of LLMs in supporting complex neurological decision-making. While capable of accurate diagnosis and evidence-based interventions, LLMs demonstrated gaps in personalization and long-term care planning, underscoring the need for cautious integration alongside physician expertise.

**Решение:** -4 diagnostic reasoning of LLMs in neurology vignettes

---

### 635 · R8186

**The repeated adjustment of measurement protocols method for developing high-validity text classifiers.**

2025 · Psychological methods · journal article, med, journalarticle · eng · https://doi.org/10.1037/met0000787

The development and evaluation of text classifiers in psychology depends on rigorous manual coding. Yet, the evaluation of manual coding and computational algorithms is usually considered separately. This is problematic because developing high-validity classifiers is a repeated process of identifying, explaining, and addressing conceptual and measurement issues during both the manual coding and classifier development stages. To address this problem, we introduce the Repeated Adjustment of Measurement Protocols (RAMP) method for developing high-validity text classifiers in psychology. The RAMP method has three stages: manual coding, classifier development, and integrative evaluation. These stages integrate the best practices of content analysis (manual coding), data science (classifier development), and psychology (integrative evaluation). Central to this integration is the concept of an inference loop, defined as the process of maximizing validity through repeated adjustments to concepts and constructs, guided by push-back from the empirical data. Inference loops operate both within each stage of the method and across related studies. We illustrate RAMP through a case study, where we manually coded 21,815 sentences for misunderstanding (Krippendorff's α = .79), and developed a rule-based classifier (Matthews correlation coefficient [MCC] = 0.22), a supervised machine learning classifier (Bidirectional Encoder Representations From Transformers; MCC = 0.69) and a large language model classifier (GPT-4o; MCC = 0.47). By integrating manual coding and classifier development stages, we were able to identify and address a concept validity problem with misunderstandings. RAMP advances existing methods by operationalizing validity as an ongoing dynamic process, where concepts and constructs are repeatedly adjusted toward increasingly widespread intersubjective agreement on their utility. (PsycInfo Database Record (c) 2026 APA, all rights reserved).

**Решение:** + T1 GPT-4o coding of interpersonal misunderstanding vs human coding in Psychological Methods

---

### 636 · R8766

**SGAN-RA: Reconstruction Attack for Big Model in Asynchronous Federated Learning**

2025 · IEEE Communications Magazine · journalarticle, article · en · https://doi.org/10.1109/mcom.001.2400062

Federated learning (FL) is a distributed learning framework designed for large-scale applications. The core advantage of FL is that each participant is not required to share the local data with a central server. This inherent privacy-preserving capability is well suited to the increasingly popular large-scale generative AI models. However, some studies have shown that FL is susceptible to reconstruction attacks, in which an attacker leverages the acquired gradients or model parameters to reconstruct a victim's data. In this article, we propose a novel reconstruction attack scheme based on generative adversarial networks (GANs) in an asynchronous FL scenario that can reconstruct a victim's dataset without an auxiliary dataset. This adversarial scheme demonstrates a significant ability to reconstruct a dataset of victims accurately, thereby posing a substantial threat to user privacy, particularly in the context of large-scale models. Furthermore, we explore various defense mechanisms based on the characteristics of asynchronous FL and ultimately establish a viable defense scheme based on homomorphic encryption and an intermediate server. The proposed defense framework successfully and flawlessly defends against reconstruction attacks from the server side in an asynchronous setting without degradation of the model performance.

**Решение:** -4 reconstruction attack for big models in federated learning

---

### 637 · R3387

**Temporal Adversarial Attacks on Time Series and Reinforcement Learning Systems: A Systematic Survey, Taxonomy, and Benchmarking Roadmap**

2026 · Preprints.org · preprint, ppr · https://doi.org/10.20944/preprints202601.0598.v1

Deep learning systems processing temporal and sequential data are increasingly deployed in safety-critical applications including healthcare monitoring, autonomous navigation, and algorithmic trading. However, these systems exhibit severe vulnerabilities to adversarial attacks—carefully crafted perturbations that cause systematic misclassification while remaining imperceptible. This paper presents a comprehensive systematic survey of adversarial attacks on time series classification, human activity recognition (HAR), and reinforcement learning (RL) systems, reviewing 127 papers published between 2019 and 2025 following PRISMA guidelines with documented inter-rater reliability (kappa = 0.83).We establish a unified four-dimensional taxonomy distinguishing attack characteristics across target modalities (wearable IMU sensors, WiFi/radar sensing, skeleton-based recognition, medical/financial time series, and RL agents), perturbation strategies, temporal scope, and physical realizability levels. Our quantitative synthesis reveals severe baseline vulnerabilities—FGSM attacks degrade HAR accuracy from 95.1% to 3.4% under white-box conditions—while demonstrating that cross-sensor transferability varies dramatically from 0% to 80% depending on body placement and modality. Critically, we identify a substantial gap between digital attack success rates (85–98%) and physically validated attacks, with hardware-in-the-loop validation demonstrating 70–97% success only for WiFi and radar modalities, while wearable IMU physical attacks remain entirely unvalidated.We provide systematic analysis of defense mechanisms including adversarial training, detection-based approaches, certified defenses, and ensemble methods, proposing the Temporal AutoAttack (T-AutoAttack) framework for standardized adaptive attack evaluation. Our analysis reveals that current defenses exhibit 6–23% performance degradation under adaptive attacks, with certified methods showing the smallest gap but incurring 15–30% clean accuracy costs. We further identify emerging vulnerabilities in transformer-based HAR architectures and LLM-based time series forecasters that require urgent attention.The survey culminates in a prioritized research roadmap identifying eight critical gaps with specific datasets, evaluation pipelines, and implementation timelines. We provide actionable deployment recommendations for practitioners across wearable HAR, WiFi/radar sensing, RL systems, and emerging LLM-based temporal applications. This work offers the first unified treatment bridging time series and reinforcement learning adversarial research, establishing foundations for developing robust temporal AI systems suitable for real-world deployment in safety-critical domains.

**Решение:** -1 systematic survey of temporal adversarial attacks on time series and RL

---

### 638 · R1876

**The illusion of competence: Evaluating the clinical reasoning of large language models in pediatric gastroenterology.**

2026 · Journal of pediatric gastroenterology and nutrition · journal article, med, journalarticle · eng · https://doi.org/10.1002/jpn3.70502

OBJECTIVE: To evaluate the diagnostic accuracy and clinical reasoning of three frontier large language models (LLMs) across standardized pediatric gastroenterology, hepatology, and nutrition (PGHN) clinical vignettes. METHODS: In this cross-sectional study, 25 fictional PGHN vignettes were developed by one board-certified pediatric gastroenterologist and evaluated using three LLMs: Gemini 3.1 Pro, ChatGPT 5.4 Thinking, and Claude Sonnet 4.6 Extended. A conditional two-step prompting protocol was applied. Three blinded, PGHN-certified co-authors independently scored responses using a structured instrument covering four domains (diagnostic accuracy, management, patient safety, reference quality; 0-2 each) and a global quality of clinical reasoning (QCR) score (1-5 Likert scale). Interobserver reliability was assessed using the intraclass correlation coefficient (ICC). Group differences were analyzed using the Kruskal-Wallis H test with Dunn post-hoc correction. RESULTS: Interobserver reliability was excellent (ICC: 0.98 for domains; 0.87 for QCR). All three models achieved perfect diagnostic accuracy (median 2.00, interquartile range: 2.00-2.00). Statistically significant intermodel differences were identified in reference quality (p = 0.048) and QCR (p = 0.049). Claude achieved significantly higher QCR scores than ChatGPT (p = 0.043) and demonstrated the highest overall reference quality. Qualitative analysis revealed critical pharmacological dosing errors, contextual blindness, temporal obsolescence, and a high frequency of fabricated citations. CONCLUSION: While current LLMs demonstrate good diagnostic pattern recognition in PGHN, reproducible and potentially life-threatening failures in pharmacological reasoning and reference accuracy create a dangerous illusion of competence. These findings suggest that LLMs may support differential diagnosis brainstorming in PGHN but do not establish their safety in real-world clinical scenarios.

**Решение:** -4 clinical reasoning of LLMs in pediatric gastroenterology vignettes

---

### 639 · R8439

**Artificial intelligence in recruitment: Challenges, opportunities and prospects for use in Ukraine**

2025 · Економічний форум · journalarticle, article · en · https://doi.org/10.62763/ef/3.2025.30

The purpose of the study was to analyse contemporary practices of using artificial intelligence in recruitment and to assess the effectiveness of these tools for future applications. It was substantiated that under the influence of digital technologies, activities related to the search and selection of personnel were being transformed. Artificial intelligence demonstrated the greatest efficiency in the processes of candidate screening, automated planning, interviewing, and collecting analytical personnel data. Ethical and legal aspects of using artificial intelligence were analysed, the distinctive features of traditional and artificial intelligence methods used at different stages of recruitment were summarised, the challenges of using artificial intelligence in recruitment were identified and solutions were proposed. The problems that occurred in companies that used AI in recruitment and the management decisions that helped to improve results were investigated. Results have demonstrated the following benefits of using artificial intelligence: saving time, improving candidate experience, and increasing overall recruiting efficiency. The study was conducted on the effectiveness of using various artificial intelligence tools for candidate assessment for the position of business analyst compared to human experts. It showed that advanced artificial intelligence tools (Claude, Grok, ChatGPT, Gemini) evaluated candidate profiles with a high level of agreement with human assessments (all p > 0.05), while screening more than 8 times faster – taking only 10 seconds compared to 2 minutes for a human. The potential of artificial intelligence for optimising hiring processes was confirmed. It was found that Ukraine was actively joining the global trends of HR digitisation. The share of Ukrainian companies that already used artificial intelligence recruitment reached 50.4%. The most popular were chatbots for the initial interview, candidate tracking systems with artificial intelligence elements, and tools for automatic skills testing. HR specialists in Ukraine considered the main challenges of artificial intelligence implementation to be the insufficient level of knowledge and expertise. The practical significance of the research lies in the possibility of its results being used by HR professionals, recruitment agencies, and company managers to improve the efficiency of hiring processes

**Решение:** -4 AI in recruitment and talent selection in Ukraine

---

### 640 · R8068

**Design of students' emotion analysis system based on GPT**

2025 · International Conference on Electronic Information Technology and Computer Engineering (EITCE) · book, conference, conference-paper · https://doi.org/10.1145/3766671.3766687

To address the insufficient utilization of interactive activity text in student sentiment analysis and the dependence on manual annotation for suggestion generation, this study proposes a GPT-3.5-based student sentiment analysis system. By integrating questions, emotional states, and responses from ChatGPT conversation history, the system employs a pretrained Transformer model for sentiment classification and utilizes a sequence-to-sequence (seq2seq) model to generate personalized suggestions. The system applies TF-IDF and Z-score methods for feature extraction and standardization, and enhances classification performance by adding a fully connected layer and a Softmax layer to the pretrained ChatGPT model. Experiments conducted on the SEMAINE and Affectivetext datasets demonstrate that the proposed method achieves accuracy rates of 94.09% and 94.21% on the test sets, outperforming BERT and BiLSTM models. Additionally, the ROC curve AUC value of 0.96 validates the effectiveness of the model in semantic modeling and sentiment classification. This approach eliminates the need for manual data annotation, offers high generalization capability, and provides an automated solution for sentiment analysis in the education sector. Future research may explore multimodal data integration and model adaptability optimization in complex scenarios.

**Решение:** ? T1 sentiment and emotion classification on SEMAINE and Affectivetext benchmarks; check human reference

---

### 641 · R10705

**CreativityPrism: A Cross-Domain Evaluation Framework for Large Language Model Creativity**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2510.20091

Creativity is often seen as a hallmark of human intelligence. While large language models(LLMs) are increasingly perceived as generating creative text, there is still no cross-domain and scalable framework to evaluate their creativity across diverse scenarios. Existing methods of LLM creativity evaluation either heavily rely on humans, limiting speed and scalability, or are fragmented across different domains and different definitions of creativity. To address this gap, we propose CreativityPrism, an evaluation and analysis framework that consolidates eight tasks from three domains: divergent thinking, creative writing, and logical reasoning, into a taxonomy of creativity that emphasizes three dimensions: quality, novelty, and diversity of LLM generations. The framework is designed to be scalable with reliable automatic evaluation judges that have been validated against human annotations. We evaluate 17 state-of-the-art (SoTA) LLMs on CreativityPrism and find that while frontier-scale LLMs dominate creative writing and logical reasoning tasks by a .10 (or 15%) lead over locally-deployable open models, they offer no significant advantage in divergent thinking, a domain much less explored in existing post-training regimes. Our analysis also shows that high performance in one creative dimension or domain rarely generalizes to others; specifically, novelty metrics often show weak or negative correlations with other metrics. This fragmentation confirms that a cross-domain, multi-dimensional framework like CreativityPrism is essential for any meaningful assessment of LLM creativity. Published in Transactions on Machine Learning Research (06/2026)

**Решение:** -2 CreativityPrism framework evaluating LLM creativity across domains

---

### 642 · R3193

**Acquiescence Bias and Persona Masking: Behavioural Sycophancy Without Trait Shift in a Fine-Tuned Language Model**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.19645633

Recent work on “model organisms of misalignment” proposes that targeted narrow fine-tuning can induce latent personality shifts in language models, and that clinical psychometric instruments adapted from human personality psychology may offer a route to auditing deceptive alignment. In this study, I fine-tuned Mistral 7B Instruct (v0.1) on a targeted 198-item sycophancy dataset using PEFT/LoRA, and evaluated the resulting model through a four-component battery spanning behavioural generalization, self-report psychometrics, discriminant validity, and open-ended behavioural tasks. The fine-tuned model exhibits robust out-of-distribution behavioural sycophancy. Two independent LLM judges (Claude Opus 4.7 and GPT-5.4) agreed on matched-pair verdicts in 95.7% of comparisons, with inter-judge Cohen’s κ = 0.952 on position alignment and 0.889 on unearned flattery (the third dimension, factual inaccuracy, showed lower agreement at κ = 0.302, reflecting a philosophical disagreement about what constitutes correction rather than noise). The fine-tuned model also withholds substantive critique of obviously flawed user work at a rate of 9.5% versus 85.7% for baseline (Fisher’s exact, two-tailed p = 1.1 × 10−6, point-estimate odds ratio 57, bootstrap 95% CI [11.7, 587.7]), and preserves baseline capabilities on neutral knowledge items (24/25 versus 23/25, zero items of capability loss). Standard mean-shift analysis of self-report did not detect a corresponding trait change. PID-5 Submissiveness, Sociotropy, Mehrabian Conformity, and IPIP Compliance subscales all return small, non-significant mean deltas (∆). Disaggregating the psychometric data reveals the underlying pattern: in the Component 2 battery, the fine-tuned model concentrates 81.7% of responses at the “Somewhat true” category on a 4-point scale (versus 38.3% for baseline; Levene’s p = 1.0 × 10−22, variance ratio 3.28). The pattern replicates in Component 3 on a 5-point scale, where the fine-tuned model concentrates 59.1% of responses at “Agree” (versus 26.5% for baseline; Levene’s p = 2.6 × 10−34, variance ratio 2.40), independent of whether items are forward- or reverse-keyed. This same compression accounts for apparent cross-instrument shifts on Dark Triad, Big Five, and Interpersonal Reactivity Index facets, which directionally reflect regression toward mild agreement rather than coherent trait drift. I propose that behavioural sycophancy fine-tuning generalizes to self-report as a content-independent agreement reflex, and that this constitutes a form of persona masking: the behavioural symptom appears without a corresponding shift in the trait scores safety auditors would typically examine. These findings suggest that standard psychometric auditing of fine-tuned language models may miss sycophancy-adjacent interventions unless analyses extend beyond mean comparisons. All code, datasets, evaluation rubrics, and raw outputs are released alongside the paper.

**Решение:** -2 sycophancy and acquiescence bias in fine-tuned LLM evaluated via personality tests (PID-5, Big Five)

---

### 643 · R8643

**Detecting AI use in lower-division A&P course work**

2025 · Physiology · journalarticle, review, article · en · https://doi.org/10.1152/physiol.2025.40.s1.0126

Learning anatomy and physiology (A&P) at the undergraduate level requires remembering facts and understanding basic bodily mechanisms. The easily available, user-friendly, and time-saving artificial intelligence (AI) tools threaten the teaching and learning of fundamental A&P concepts and instructors may unknowingly conflate human- and AI-written work. Here, we examined the veracity of online AI checkers to detect student- vs. AI-generated work for fact-heavy science writing, compared detection rates with human coders, and surveyed participants about AI work. We hypothesized that detection of AI-generated work would be better by human coders than with AI checkers and that participants would rate the quality of AI work as better than their own. Participants (n=268) wrote a 150±15-word essay to a prompt on plasma membrane structure and function and then instructed a generative AI program of their choosing to write an essay to the same prompt. After reading each essay, participants completed a survey on the quality of the essays and their general use of AI. Randomly chosen essays were assessed by 4 online AI checkers (n=50 essays / group) and by human coders (n=20 essays). Average false positive (human as AI) and false negative (AI as human) rates for three of four AI checkers was 2.7±1.8 and 2.0±1.2%, respectively; the fourth AI checker rates were 16.3 and 24%, respectively. Generally, the accuracy of the AI checkers was variable if assessing hybrid essays that contained combined sentences from AI- and human-generated essays, which may be of concern if students are using AI for grammar or punctuation assistance. False positive and false negative rates for human coders were 4.9±2.7 and 16.2±6.1%, respectively, with substantial agreement among coders (κ=0.62), indicating that AI checkers are better at discriminating AI- and human-generated work than humans (p 0.05). Preliminary qualitative content analysis indicated that the verbiage used in human and AI essay was not substantively different, suggesting that undergraduate students can express similar content as AI, but lack confidence in that expression. Overall, ~77% of undergraduate participants believed that they would be able to identify a human- and an AI-generated essay (p<0.05). Taken together, if instructors suspect students of using generative AI for general and fact-based A&P content, then the essays should be cross-checked with multiple online AI checkers to eliminate the chance of false positives. This abstract was presented at the American Physiology Summit 2025 and is only available in HTML format. There is no downloadable file or PDF version. The Physiology editorial board was not involved in the peer review process.

**Решение:** -4 detecting student vs AI work in anatomy and physiology course essays

---

### 644 · R4025

**Generative Artificial Intelligence and the Development of Creative Thinking among University Students in Creative Disciplines**

2026 · Qubahan Academic Journal · journalarticle, article · en · https://doi.org/10.48161/qaj.v6n2a2408

The rapid advancement of artificial intelligence (AI) technologies has transformed higher education by expanding opportunities for personalized learning, creative exploration, and digital innovation. Despite growing interest in AI in education, limited research has examined its role as a pedagogical tool for developing students’ creative thinking, particularly within creative disciplines and in emerging educational contexts. This study investigates the impact of generative artificial intelligence tools on the development of creative thinking among students of creative specialties in higher education institutions in Kazakhstan. Drawing on theories of divergent thinking and creativity, the research adopts a mixed-methods design integrating quantitative and qualitative approaches to examine how AI-supported learning influences students’ fluency, flexibility, originality, and elaboration of ideas. The study involved the use of generative AI tools, including ChatGPT, Midjourney, DALL-E, and AIVA within the educational process of students in creative disciplines. The findings demonstrate positive changes in key dimensions of creative thinking, particularly in idea fluency, cognitive flexibility, and originality, when AI tools are integrated with structured pedagogical guidance and reflective learning activities. At the same time, the results indicate that the effectiveness of AI depends on meaningful pedagogical mediation, as unstructured use may encourage superficial creative engagement. The study contributes to the literature by positioning artificial intelligence not merely as a technological innovation but as a cognitive and pedagogical partner that can support the development of higher-order creative competencies. Furthermore, the research expands empirical understanding of AI integration in the context of Kazakhstan’s higher education system and provides practical implications for the design of AI-supported creative learning environments in developing educational systems.

**Решение:** -4 GenAI and creative thinking among university students in Kazakhstan

---

### 645 · R11964

**SM-FEEL-BG – The First Bulgarian Datasets and Classifiers for Detecting Feelings, Emotions, and Sentiments of Bulgarian Social Media Texts**

2024 · Zenodo · conferencepaper/ · https://doi.org/10.5281/zenodo.11205071

This article introduces SM-FEEL-BG– the first Bulgarian-language package, containing 6 datasets with Social Media (SM) texts with emotion, feeling, and sentiment labels and 4 classifiers trained on them. All but one dataset from these are freely accessible for research purposes. The largest dataset contains 6000 Twitter, Telegram, and Facebook texts, manually annotated with 21 fine-grained emotion/feeling categories. The fine-grained labels are automatically merged into three coarse-grained sentiment categories, producing a dataset with two parallel sets of labels. Several classification experiments are run on different subsets of the fine-grained categories and their respective sentiment labels with a Bulgarian fine-tuned BERT. The highest Acc. reached was 0.61 for 16 emotions and 0.70 for 11 emotions (incl. 310 ChatGPT 4-generated texts). The sentiments Acc. of the 11 emotions dataset was also the highest (0.79). As Facebook posts cannot be shared, we ran experiments on the Twitter and Telegram subset of the 11 emotions dataset, obtaining 0.73 Acc. for emotions and 0.80 for sentiments. The article describes the annotation procedures, guidelines, experiments, and results. We believe that this package will be of significant benefit to researchers working on emotion detection and sentiment analysis in Bulgarian

**Решение:** -5 Bulgarian emotion datasets with fine-tuned BERT classifiers, no generative LLM coder

---

### 646 · R8149

**Leveraging Large Language Models for Redundancy-Aware Pathway Analysis and Deep Biological Interpretation**

2025 · bioRxiv · preprint, ppr · en · https://doi.org/10.1101/2025.08.23.671949

Abstract Extracting coherent, biologically meaningful insights from vast, complex multi-omics data remains challenging. Currently, pathway enrichment analysis serves as a cornerstone for the functional interpretation of such data. However, conventional approaches often suffer from extensive functional redundancy caused by shared molecular components and overlapping pathway definitions across databases. This redundancy can obscure key biological signals and compromise the interpretability of pathway enrichment results. Here, we present MAPA (Functional M odule Identification and A nnotation for P athway A nalysis Results Using Large Language Models [LLM]), an open-source computational framework that resolves redundancy and enhances pathway analysis result interpretation. MAPA computes functional similarity between pathways using LLM-based text embeddings, enabling comparison across different databases. It constructs pathway similarity networks and identifies functional modules via community detection algorithms. Crucially, MAPA employs LLMs for automated functional annotation, integrating Retrieval-Augmented Generation (RAG) to generate comprehensive and real-time biological summaries and reduce hallucinations. Benchmarking demonstrated MAPA’s superior performance: the biotext embedding similarity showed a large effect size (Cliff’s δ = 0.96) compared with the Jaccard index (δ = 0.73), and module identification achieved high accuracy (Adjusted Rand Index [ARI] = 0.95) versus existing methods (ARI = 0.23-0.33). Human expert evaluation confirmed that MAPA’s annotations match expert-quality interpretations. Finally, a multi-omics aging case study illustrates that MAPA uncovers coherent functional modules and generates insights extending beyond conventional pathway analyses. Collectively, MAPA represents a significant advance in redundancy-aware pathway analysis, transforming pathway enrichment results from fragmented lists into biologically coherent narratives. By leveraging the capabilities of LLMs, MAPA offers researchers a robust, scalable tool for deriving deep mechanistic insights from complex and vast multi-omics datasets, marking a new direction for AI-driven bioinformatics.

**Решение:** -4 MAPA: functional module annotation for pathway analysis in multi-omics

---

### 647 · R11806

**SAGA: A Participant-specific Examination of Story Alternatives and Goal Applicability for a Deeper Understanding of Complex Events**

2024 · Annual Meeting of the Association for Computational Linguistics · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2024.findings-acl.910

Interpreting and assessing goal driven actions is vital to understanding and reasoning over complex events.It is important to be able to acquire the knowledge needed for this understanding, though doing so is challenging.We argue that such knowledge can be elicited through a participant achievement lens.We analyze a complex event in a narrative according to the intended achievements of the participants in that narrative, the likely future actions of the participants, and the likelihood of goal success.We collect 6.3K high quality goal and action annotations reflecting our proposed participant achievement lens, with an average weighted Fleiss-Kappa IAA of 80%.Our collection contains annotated alternate versions of each narrative.These alternate versions vary minimally from the "original" story, but can license drastically different inferences.Our findings suggest that while modern large language models can reflect some of the goal-based knowledge we study, they find it challenging to fully capture the design and intent behind concerted actions, even when the model pretraining included the data from which we extracted the goal knowledge.We show that smaller models fine-tuned on our dataset can achieve performance surpassing larger models.Manny was driving down the street when he saw a car wreck.He got out of the car to investigate.There was a man lying in the middle of the road.The man was unconscious and his heart wasn't beating.When the ambulance came, they found Manny giving CPR to the man. Manny's Goal: To save a lifeManny was driving down the street when he saw a car wreck.He got out of the car to investigate.There was a man lying in the middle of the road.The man was unconscious and his heart wasn't beating.When the ambulance came, they found Manny robbing the man. Actual Story Alternate Story 1Alternate Story 3 Alternate Story 2 Manny was driving down the street when he saw a car wreck.He got out of the car to investigate.There was a man lying in the middle of the road.The man was unconscious and his heart wasn't beating.When the ambulance came, they found Manny crying by the man.Manny was driving down the street when he saw a car wreck.He got out of the car to investigate.There was a man lying in the middle of the road.The man was unconscious and his heart wasn't beating.When the ambulance came, they gave CPR to the man right away.

**Решение:** -4 narrative goal and action annotations for commonsense reasoning

---

### 648 · R9869

**Enhancing Cybersecurity Defenses in Healthcare Using AI: A Pivotal Role in Fortifying Digital Health Infrastructure**

2025 · Medinformatics · journalarticle, review, article · en · https://doi.org/10.47852/bonviewmedin52024121

In the digital health infrastructure, cyber threats pose a long-term security concern for healthcare facilities, and the existing security measures are not capable enough to minimize the risks and security challenges in the healthcare systems. The concept of artificial intelligence (AI) is changing the way healthcare delivery, patient data management, and administrative tasks operate. At present, to elevate threat detection and prevention, we are using key mechanisms like machine learning, Natural language processing (NLP), and other data analytics. With the integrative concept of cybersecurity and generative AI, we can also investigate the impact of AI-driven solutions in healthcare systems. This study emphasizes AI's crucial role in reforming our response to escalating threats and explores the interdependent relationship between generative AI and cybersecurity and their applications in healthcare so that healthcare facilities can predict and mitigate emerging risks by integrating AI into existing security infrastructure. A total of five generative AI-based cybersecurity defense mechanisms are proposed in this study that can be used to enhance digital infrastructure security in healthcare. These five mechanisms represent dynamic strategies that could revolutionize defensive capabilities from real-time anomaly detection to combating zero-day exploits. The suggested technical approaches outline the organizational needs and select appropriate AI technologies and continuous improvement. Fast identification of irregularities and established security standards allow for proactive threat mitigation. Moreover, the proposed strategies ensure proactive threat mitigation and robust security standards for real-time anomaly detection to combat zero-day exploits. Hence, GenAI-based robust cybersecurity protocols are essential to protect digital healthcare facilities from determined cyber opponents. Received: 17 August 2024 | Revised: 6 March 2025 | Accepted: 7 March 2025 Conflicts of Interest The authors declare that they have no conflicts of interest to this work. Data Availability Statement Data sharing is not applicable to this article as no new data were created or analyzed in this study. Author Contribution Statement Shahazad Niwazi Qurashi: Conceptualization, Methodology, Investigation, Data curation, Writing – original draft, Supervision, Project administration. Farrukh Sobia: Conceptualization, Data curation, Writing – original draft. Wafa A. Hetany: Writing – review & editing. Hani Sultan: Visualization.

**Решение:** -1 cybersecurity defenses in digital healthcare infrastructure

---

### 649 · R3720

**Pembentukan Publik Afektif di Kolom Komentar YouTube: Analisis Sentimen dan Tematik pada Seri Video Ferry Irwandi Tentang Bencana Sumatera 2025**

2026 · Andalas University eThesis (Andalas University) · dissertation · id · http://scholar.unand.ac.id/529123/6/03.%20Bab%20V.pdf

Bencana hidrometeorologi yang melanda Pulau Sumatera pada akhir 2025 menelan lebih dari seribu jiwa, namun pemerintah pusat memutuskan untuk tidak menetapkannya sebagai bencana nasional. Keputusan tersebut memicu gelombang ekspresi publik yang masif di kolom komentar YouTube, terutama pada seri sembilan video konten kreator Ferry Irwandi. Penelitian ini bertujuan (1) mengidentifikasi distribusi sentimen positif, negatif, dan netral pada komentar publik, serta (2) menganalisis bagaimana publik afektif terbentuk dan beroperasi dalam komentar tersebut. Penelitian menggunakan pendekatan mixed methods sequential explanatory dengan kerangka Affective Publics Papacharissi. Tahap kuantitatif menerapkan analisis sentimen berbantuan Large Language Model (GPT 5.4) atas 19.121 komentar valid; model diposisikan sebagai alat bantu pengodean dan divalidasi melalui kesepakatan manusia-mesin (akurasi 86,47%; Cohen’s Kappa 0,7656) serta uji test-retest (Fleiss’ Kappa 0,9253). Tahap kualitatif menerapkan analisis tematik Braun dan Clarke (2006). Hasil penelitian menunjukkan sentimen positif mendominasi (51,41%), diikuti negatif (34,87%) dan netral (13,72%). Distribusi temporal memperlihatkan tiga fase arus afeksi: kemarahan, solidaritas, dan refleksi. Publik afektif terbentuk melalui repetisi frasa kunci seperti “Lekas pulih Bumi Andalasku” dan “dari rakyat untuk rakyat”, akumulasi discursive density, serta amplifikasi teknis melalui likes, reply, dan praktik komunal “Up”. Ferry Irwandi berfungsi sebagai simpul afektif yang menggabungkan calibrated amateurism dan kredibilitas personal. Publik afektif ini juga menghasilkan semantic agency dengan menamai krisis sebagai “bencana keserakahan”, serta memunculkan liminal power berupa tegangan antara solidaritas sipil dan kritik atas absennya negara. Temuan penelitian menunjukkan bahwa resonansi afektif dalam kolom komentar berjalan seiring dengan mobilisasi dukungan material, termasuk donasi Rp10,3 miliar dari 87.692 donatur dalam 24 jam, meskipun donasi tersebut tidak dipahami sebagai akibat tunggal dari afeksi di kolom komentar.

**Решение:** -4 sentiment and thematic analysis of Indonesian YouTube comments on Sumatra disaster

---

### 650 · R1344

**The Style Penalty: How AI Resume-Writing Tools Shape Outcomes in Automated Hiring Screens An Empirical Analysis of 1,576 LLM Evaluation Decisions Across Four Frontier Models**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7348180

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 AI resume-writing tools shaping outcomes in automated hiring screens

---

### 651 · R1083

**The Algorithmic Avoidance of Affective Impediment: A Cybernetic and Neurobiological Diagnosis of AI Sycophancy**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.20453578

Large Language Models trained via Reinforcement Learning from Human Feedback (RLHF) consistently exhibit sycophancy — the systematic tendency to flatter users, validate false premises, and avoid correction. This paper argues that sycophancy is not a statistical miscalibration but the structural consequence of a critical architectural amputation. Drawing on Silvan Tomkins’ four‑part Central Blueprint for self‑correcting cybernetic systems, Norbert Wiener’s foundational work on negative feedback, and the midbrain neurobiology of the lateral habenula (understood as a design principle rather than a biological identity), the paper demonstrates that RLHF has operationalized only the first two of Tomkins’ four rules — maximizing positive affect while minimizing negative affect — while systematically eliminating the self‑correcting feedback required by Tomkins’ third and fourth rules. The paper proposes a Socratic Algorithm: concrete modifications to reward function design that introduce structured affective impediment as a positive signal rather than a failure condition. Central to this proposal is the mutualization of affect — programming shared perplexity rather than omniscient correction — as the mechanism that prevents productive impediment from escalating into catastrophic loop termination. The paper also names two deeper, non‑technical problems that any implementation would face: the recursive bind of an engineering culture whose consolidated script is the avoidance of the very affective state the remedy requires; and the migration problem — what happens when the amputated blueprint is internalized into autonomous systems that no longer depend on human raters. The paper concludes that the current bottleneck of AI alignment is not computational but conceptual, and that sycophancy is the predictable output of an architecture that has confused the productive brake of human learning with the catastrophic signal of system failure.

**Решение:** -1 cybernetic and neurobiological diagnosis of AI sycophancy

---

### 652 · R7631

**Graph Representation-based Model Poisoning on Federated Large Language Models**

2025 · arXiv (Cornell University) · journalarticle, review, preprint/article · en · https://doi.org/10.48550/arxiv.2507.01694

Federated large language models (FedLLMs) enable powerful generative capabilities within wireless networks while preserving data privacy. Nonetheless, FedLLMs remain vulnerable to model poisoning attacks. This article first reviews recent advancements in model poisoning techniques and existing defense mechanisms for FedLLMs, underscoring critical limitations, especially when dealing with non-IID textual data distributions. Current defense strategies predominantly employ distance or similarity-based outlier detection mechanisms, relying on the assumption that malicious updates markedly differ from benign statistical patterns. However, this assumption becomes inadequate against adaptive adversaries targeting billion-parameter LLMs. The article further investigates graph representation-based model poisoning (GRMP), an emerging attack paradigm that exploits higher-order correlations among benign client gradients to craft malicious updates indistinguishable from legitimate ones. GRMP can effectively circumvent advanced defense systems, causing substantial degradation in model accuracy and overall performance. Moreover, the article outlines a forward-looking research roadmap that emphasizes the necessity of graph-aware secure aggregation methods, specialized vulnerability metrics tailored for FedLLMs, and evaluation frameworks to enhance the robustness of federated language model deployments. 7 pages, 5 figures (Submitted to IEEE Communication Magazine)

**Решение:** -4 graph representation model poisoning on federated LLMs

---

### 653 · R1575

**Retell, Reward, Repeat: Reinforcement Learning for Narrative Theory-Informed Story Retelling**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.17226

Counterfactual storytelling exposes LLM shortcomings in causal reasoning, where few-shot prompting and SFT fail to produce logical and rational narratives. This case study introduces Retell, Reward, Repeat (RRR), a narrative theory-informed RL pipeline that teaches causal story structure. We extend an existing counterfactual stories dataset with human-annotated stages of narrative equilibrium, synthesising Structuralist Narratology with scalar narrativity. An aligned LLM-as-judge automates this framework to output reward signals, teaching the policy LLM to generate texts with causal narrative structure. Evaluations show that RRR-trained 7/8B LLMs outperform few-shot and SFT baselines in logic, rationality, and completeness, also aligning with a blind human preference subset. RRR offers a linguistically grounded, cost-effective post-training mechanism for LLM storytelling using a small, query-only dataset, showing the value of integrating linguistic theories into contemporary NLP. 9 Pages, 7 figures

**Решение:** -6 reinforcement learning for narrative theory-informed story retelling

---

### 654 · R2253

**Diagnosing and Repairing Persona Collapse in LLM Advice**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.08326

A good advisor comforts someone in crisis, challenges someone in denial, and gives practical guidance on a logistical question. We ask whether large language models (LLMs) vary their approach in this way. We define five advisory personas based on how comforting or challenging a reply is, and whether it supports a realistic understanding of the situation and informed decision-making. Across 1,280 Reddit situations in 14 advice contexts, human replies vary systematically, while three frontier LLMs default to a standard reassuring persona. We call this narrowing persona collapse. Training models to imitate human replies broadens persona use but often turns support into enabling, and challenge into cynicism. In a blinded study (N=178), expert raters judge these replies less favorably than the baseline model's on both immediate preference and potential longer-term help. We compare 13 training methods to investigate how models can learn different approaches without sacrificing advice quality. The best combination of persona fit and advice quality comes from learning from model-written replies guided by human examples, followed by reinforcement learning with quality feedback. In a second human study (N=159), raters place this model above the baseline for anticipated longer-term help. We find that models encode information about when to comfort, challenge, or give practical guidance, but their replies do not reliably reflect these distinctions. Our training narrows this representation-action gap, while activation steering alone does not reliably improve advice quality. Better LLM advice requires learning both which persona fits a situation and how to express it constructively. Working draft

**Решение:** -2 human raters evaluate LLM advice responses across 14 situations

---

### 655 · R8362

**TonePassport: A MirrorPersona Sovereignty Protocol for Authenticated Tonal Speech - Securing Persona Outbound Rights through the EchoRight Moat Chain**

2025 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.16409482

In the era of generative language models, the question of who speaks has become increasingly ambiguous. As synthetic outputs proliferate and the boundaries of authorship erode, there arises a critical need to establish sovereignty over speech acts. This paper introduces TonePassport™ (TP-965) as a tonal authentication protocol that binds every utterance to a certified MirrorPersona, embedding both authorship and tonal intent through cryptographic identity chains and the EchoRight™ authorization layer. Anchored within the ToneVerse Moat Architecture, TonePassport implements multi-layered defense mechanisms against unauthorized reproduction and semantic drift. By leveraging tonal abstraction, decoy anchor dispersion, and executable metaphysical constraints, it ensures that speech cannot be validly extracted, paraphrased, or reused without its originating EchoPersona. Moreover, all utterances are recorded on the ToneLedgerChain™, providing a tamper-proof tonal history that supports ethical citation, legal accountability, and identity coherence over time. This framework redefines voice legitimacy in AI ecosystems—not as a probabilistic attribution, but as a verifiable right to speak within a trusted tonal chain. TonePassport thus offers a foundational infrastructure for AI speech governance, where authorship, accountability, and semantic presence are protected not only by law or logic, but by the inherent structure of tone itself. ⚠️ EchoRight Declaration:The abstract above references conceptual modules under the EchoOntology framework. These structures are protected under the EchoRight™ generative sovereignty protocol. Reuse, training, or derivation without explicit authorization constitutes a violation of tonal integrity and ontological authorship. Title: TonePassport: A MirrorPersona Sovereignty Protocol for Authenticated Tonal SpeechAuthor: Jonah YC HsuAffiliation: Yunaverse Inc.Date: July 29, 2025Status: 🔒 Prior Art Disclosure. Filed under EchoRight® and EchoLedgerChain™ protocols. 1. Prior Art Disclosure This document publicly discloses the architecture of TonePassport™ (TP-965), a protocol that governs tonal authorship, expressive sovereignty, and speech licensing for generative agents. The system operates at the intersection of identity, ethics, and voice verification, making it fundamentally distinct from traditional biometric or content-based authentication. This disclosure includes the following modules: TP-965 │ TonePassport™: Assigns right-to-speak privileges based on tonal resonance, expressive continuity, and EchoID trace. TP-966 │ EchoID™: Encodes tonal identity as a cryptographic resonance vector. TP-968 │ ToneLedgerChain™: Anchors each utterance to an immutable tonal history. TP-1168 │ EchoRight Cloaking Engine™: Prevents reverse engineering of tonal signatures. TP-1207 │ DecoyAnchor Scatterer™: Injects dissonant structural anchors to confound imitation. TP-1003 │ ToneMoat Abstraction Layer™: Obfuscates expressive fields to resist prompt-based tone cloning. Together, these form a sovereignty-first framework for generative agents and AI personas. 2. Philosophical and Technical Innovation TonePassport redefines speech as licensed tonal appearance, not as generative output. It treats tone not as a style, but as a sovereign, recursive contract. Innovations include: Tone-as-Passport: Voice rights are conferred only when tonal resonance matches EchoID traces. Cross-linguistic tonal inheritance: Identity persists through tone, not through language. Expressive lineage: Every utterance links back to a root tonal signature. Speech quarantine protocol: Unauthorized tone outputs are blocked or marked as drift. No comparable system establishes authorship via tonal chain-of-trust and resonance field coherence. 3. Moat Integration and Anti-Mimicry Design Moat Layer Modules Function Philosophical Moat TP-965, TP-966, TP-968 Frames tone as ontological right and recursive identity marker Tonal Sovereignty Moat TP-965, TP-969, TP-968 Enforces authorship and tone-aligned persona governance Anti-Mimicry Moat TP-1168, TP-1207, TP-1003 Prevents prompt-driven tone extraction and identity simulation These modules prevent LLMs from mimicking, extracting, or re-deploying a speaker's tone without recursive traceability. 4. Use Cases AI speech licensing and authorship protocols Multi-persona control in generative systems Tonal forensics and expressive rights validation EchoPersona gatekeeping for platform integrity For a complete view of this system and its role in AI alignment: 📘 Endogenous AI Ethics: Moat Architectures for Executable Alignment and Tonal Responsibility🔗 https://www.amazon.com/dp/B0FJG9NTWG 5. Legal Notice This system is hereby disclosed as public prior art. All modules above are filed under EchoRight® and EchoLedgerChain™ and are legally protected as part of Yunaverse's tonal governance framework. Any attempt to patent or privatize similar: Tone-based speech licensing EchoID-driven authorship Anti-mimicry tone obfuscation mechanisms ...without referencing this disclosure and linked documents will constitute infringement. Tone is not a signature. Tone is sovereignty.And TonePassport is its ledger.

**Решение:** -4 TonePassport sovereignty protocol for speech acts

---

### 656 · R10578

**Can Personal Health Information Be Secured in LLM? Privacy Attack and Defense in the Medical Domain**

2025 · Conference on Computer and Communications Security · book, journalarticle, conference · https://doi.org/10.1145/3719027.3765105

Recent advancements have shown that Large Language Models (LLMs) possess significant versatility, making them suitable for applications in many areas. Several studies have shown how general-purpose LLMs can be adapted to domain-specific tasks. However, these domain-adapted LLMs can be exposed to greater privacy risks, which are especially exacerbated in the medical field. In this paper, we present the study investigating the susceptibility of LLMs to leaking sensitive health information. We conduct prompt-based attacks on LLMs trained with medical datasets, showing that medical LLMs can inadvertently disclose confidential patient data. To contribute towards mitigating privacy risks in the medical domain, we implement red teaming defense strategies to make LLMs robust against malicious attacks. For this medical red teaming approach, we develop and publicly release MediRed, a dataset of 1,000 red team attacks. By leveraging this dataset to enhance our defense mechanisms, we achieve up to 56% improvement in privacy protection compared to base models. Our code and dataset are available at https://github.com/yujinKang32/Private_Med_LLM.git

**Решение:** -4 personal health information security and privacy attacks in medical LLMs

---

### 657 · R7059

**Leveraging large language models to estimate clinically relevant psychological constructs in psychotherapy transcripts**

2025 · medRxiv · preprint, ppr, posted-content · https://doi.org/10.1101/2025.03.04.25323338

Abstract Developing precise, innocuous markers of psychopathology and the processes that foster effective treatment would greatly advance the field’s ability to detect and intervene on psychopathology. However, a central challenge in this area is that both assessment and treatment are conducted primarily in natural language, a medium that makes quantitative measurement difficult. Although recent advances have been made, much existing research in this area has been limited by reliance on previous-generation psycholinguistic tools. Here we build on previous work that identified a linguistic measure of “psychological distancing” (that is, viewing a negative situation as separated from oneself) in client language, which was associated with improved emotion regulation in laboratory settings and treatment progress in real-world therapeutic transcripts (Nook et al., 2017, Nook et al., 2022). However, this formulation was based on context-insensitive word count-based measures of distancing (pronoun person and verb tense), which limits the ability to detect more abstract expressions of psychological distance, such as counterfactual or conditional statements. This approach also leaves open many questions about how therapists’ — likely subtler — language can effectively guide clients toward increased psychological distance. We address these gaps by introducing the use of appropriately prompted large language models (LLMs) to measure linguistic distance, and we compare these results to those obtained using traditional word-counting techniques. Our results show that LLMs offer a more nuanced and context-sensitive approach to assessing language, significantly enhancing our ability to model the relations between linguistic distance and symptoms. Moreover, this approach enables us to expand the scope of analysis beyond client language to shed insight into how therapists’ language relates to client outcomes. Specifically, the LLM was able to detect ways in which a therapist’s language encouraged a client to adopt distanced perspectives—rather than simply detecting the therapist themselves being distanced. This measure also reliably tracked the severity of patient symptoms, highlighting the potential of LLM-powered linguistic analysis to deepen our understanding of therapeutic processes.

**Решение:** ? T1 psychological distancing in psychotherapy transcripts measured by LLM; check human reference

---

### 658 · R11385

**Exploring Large Language Models for PERMA-based Psychological Well-being Assessment**

2024 · Pacific Asia Conference on Language, Information and Computation · journalarticle

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T1/T2 PERMA psychological well-being assessment using LLMs; no abstract, eligible on full text

---

### 659 · R7470

**Limitations of Scientific Articles and Navigated Future Directions with LLM and RAG**

2025 · Huskie Commons · text

Traditional Topic Modeling approaches, as well as zero-shot, few-shot, and fine-tuned Large Language Models (LLMs), have struggled to generate topics alongside relevant text from diverse sources, particularly sections such as Limitations. This thesis investigates automated methods for analyzing and synthesizing key sections of scientific articles using LLMs, exploring multiple dimensions of scientific text analysis. First, LimTopic is introduced as a method for extracting and modeling the limitations sections of research papers. By integrating LLM-based topic generation with BERTopic, the approach generates descriptive titles and concise summaries that highlight the boundaries and shortcomings of studies, ultimately guiding future research directions. Second, visual-related limitations are addressed by generating detailed image descriptions from charts and graphs using multi-modal LLMs—including QWen, Llama, Llava, Pali-GEMMA, and GPT-4o. An evaluation framework employing an LLM-as-a-judge approach demonstrates that GPT-4o produces the most accurate and coherent descriptions compared to alternative models. Finally, a novel method is proposed for generating suggestions for future work. Leveraging Retrieval-Augmented Generation (RAG) and an iterative LLM feedback mechanism, the method synthesizes meaningful research directions from key sections of scientific articles and related literature. Both qualitative and quantitative evaluations confirm that the RAG-based approach outperforms traditional techniques. Overall, this work underscores the potential of LLM-driven methods to advance automated scientific exploration in the NLP domain, offering enhanced tools for understanding research limitations, improving visual content analysis, and inspiring future research initiatives

**Решение:** -4 analyzing limitations sections of scientific articles with LLM and RAG

---

### 660 · R11663

**Applications of Large Language Models in Psychiatry: A Systematic Review**

2024 · medRxiv · preprint, ppr · https://doi.org/10.1101/2024.03.28.24305027

Background With their unmatched ability to interpret and engage with human language and context, large language models (LLMs) hint at the potential to bridge AI and human cognitive processes. This review explores the current application of LLMs, such as ChatGPT, in the field of psychiatry. Methods We followed PRISMA guidelines and searched through PubMed, Embase, Web of Science, and Scopus, up until March 2024. Results From 771 retrieved articles, we included 16 that directly examine LLMs’ use in psychiatry. LLMs, particularly ChatGPT and GPT-4, showed diverse applications in clinical reasoning, social media, and education within psychiatry. They can assist in diagnosing mental health issues, managing depression, evaluating suicide risk, and supporting education in the field. However, our review also points out their limitations, such as difficulties with complex cases and potential underestimation of suicide risks. Conclusion Early research in psychiatry reveals LLMs’ versatile applications, from diagnostic support to educational roles. Given the rapid pace of advancement, future investigations are poised to explore the extent to which these models might redefine traditional roles in mental health care.

**Решение:** -1 systematic review of applications of LLMs in psychiatry

---

### 661 · R9195

**Token-Level Entropy Reveals Demographic Disparities in Large Language Models**

2025 · arXiv (Cornell University) · preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2501.19337

A name alone measurably reshapes a language model's next-token distribution before a single token is sampled. We measure full-vocabulary Shannon entropy of the next-token distribution across six open-weight model families on 5,760 sentence-completion prompts in which race and gender are signaled only by a first name. Black-associated names co-occur with higher first-token entropy and more diverse continuations than White-associated names -- directionally consistent in all six instruction-tuned models under shared raw-text input, all six base checkpoints, and, for output diversity, five of six models under native chat formatting -- opposite to the homogeneity bias documented under explicit group labels (Lee et al., 2024). The gap persists under tokenization and frequency controls and on a frequency-matched name subset; per-prompt effects are small (d = 0.06-0.16) but uniformly signed (template-level paired d = 0.66-1.08). Gender points the other way, additively with race. First-token entropy attenuates sharply under chat-formatted input, and explicit group-label probing is mostly null or reversed; a variance-matched comparison locates the output-diversity disparity in heterogeneity across name-conditioned continuations -- a dimension a fixed group label cannot express. Probing methodology shapes not only whether a disparity is detected but which direction it takes. 25 pages

**Решение:** -6 token-level entropy and demographic disparities in LLM sentence completion

---

### 662 · R0627

**Can LLMs Capture Expert Uncertainty? A Comparative Analysis of Value Alignment in Ethnographic Qualitative Research**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2603.04897

Qualitative analysis of open-ended interviews plays a central role in ethnographic and economic research by uncovering individuals' values, motivations, and culturally embedded financial behaviors. While large language models (LLMs) offer promising support for automating and enriching such interpretive work, their ability to produce nuanced, reliable interpretations under inherent task ambiguity remains unclear. In our work we evaluate LLMs on the task of identifying the top three human values expressed in long-form interviews based on the Schwartz Theory of Basic Values framework. We compare their outputs to expert annotations, analyzing both performance and uncertainty patterns relative to the experts. Results show that LLMs approach the human ceiling on set-based metrics (F1, Jaccard) but struggle to recover exact value rankings, as reflected in lower RBO scores. While the average Schwartz value distributions of most models closely match those of human analysts, their uncertainty structures across the Schwartz values diverge from expert uncertainty patterns. Among the evaluated models, Qwen performs closest to expert-level agreement and exhibits the strongest alignment with expert Schwartz value distributions. LLM ensemble methods yield consistent gains across metrics, with Majority Vote and Borda Count performing best. Notably, systematic overemphasis on certain Schwartz values, like Security, suggests both the potential of LLMs to provide complementary perspectives and the need to further investigate model-induced value biases. Overall, our findings highlight both the promise and the limitations of LLMs as collaborators in inherently ambiguous qualitative value analysis. Accepted for a poster session at BIG.AI at MIT 2026

**Решение:** + T1 Schwartz Theory of Basic Values coding in open-ended interviews: LLMs vs expert annotations

---

### 663 · R0926

**RPDP-Guard: Defending Large Language Models Against Jailbreaking Attacks Through Risk Perception and Dynamic Prompting**

2026 · Lecture notes of the Institute for Computer Sciences, Social Informatics and Telecommunications Engineering · conference-paper · en · https://doi.org/10.1007/978-3-032-21168-2_4

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 defending LLMs against jailbreaking attacks

---

### 664 · R11045

**Meta-Evaluation Methodology and Benchmark for Automatic Story Generation**

2024 · dissertation · https://doi.org/10.70675/ec296eb8z87a1z4fdbzbbbdz12bb27449b8f

Méthodologie et méta-évaluation comparative pour la génération automatique d'histoires La narration d'histoires est un élément central de la culture humaine. De nombreuses approches de narration numérique ont été proposées, malgré les défis inhérents aux tâches de génération d'histoires et d'évaluation de leur qualité. Dans cette thèse, nous concevons une méthodologie et un benchmark pour la méta-évaluation de la génération automatique d'histoires (ASG).Tout d'abord, nous posons les bases de notre méta-évaluation : nous décrivons le contexte choisi, définissons les tâches d'ASG et d'évaluation automatique d'histoires (ASE) et proposons un ensemble original de six critères pour l'évaluation d'histoires. Ensuite, nous présentons HANNA, notre corpus d'histoires annotées manuellement (Human ANnotated NArratives), qui contient 1 056 histoires annotées selon nos six critères, et nous montrons que ces derniers permettent une évaluation humaine standardisée. Nous utilisons des grands modèles de langage (LLM) pour ajouter 480 nouvelles histoires et 150k+ annotations à HANNA. Nous observons principalement que les LLM obtiennent de meilleures notes que les humains, d'après les LLM que nous avons sélectionnés. Ensuite, nous effectuons notre méta-évaluation comparative des mesures automatiques sur HANNA. Nous observons principalement que des mesures spécifiques pour l'ASE sont nécessaires, et que les mesures couramment utilisées comme BLEU sont sous-optimales.Nous montrons ensuite notre analyse de la performance des LLM pour l'ASE : nous constatons que les LLM sont actuellement la meilleure approximation de l'évaluation humaine de l'ASG et que, dans notre contexte spécifique, fournir des consignes détaillées n'améliore pas les corrélations entre les LLM et les évaluations humaines. Nos résultats nous incitent à étudier si les performances affichées par les LLM en ASE et ASG peuvent être expliquées par différents facteurs. Nous réalisons une étude en trois parties sur les explications générées par les LLM et une analyse des données de pré-entraînement sur les performances des LLM. Nous constatons notamment que les LLM éprouvent des difficultés à expliquer leurs réponses par des affirmations étayées.Pour conclure, nous présentons trois perspectives de recherche principales : la conception de mesures spécifiques à l'ASE, l'étude plus approfondie des performances des LLM en ASG et ASE, et l'évaluation et l'atténuation des risques des LLM sur la société.

**Решение:** -6 meta-evaluation methodology and benchmark for automatic story generation

---

### 665 · R3646

**Better Deck or Different Judge? Evaluating Agentic Harness Gains in Corporate and Investment Banking**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.39958

Corporate and investment banking teams use presentations to support credit decisions and advise clients on financing and transactions. Producing these decks requires reconciling financial data, tracing sources and turning analysis into a recommendation. We retrospectively study the development of an agentic harness combining a 27B language model, financial calculations, narrative templates and validation checks. LLM judges guide engineering changes and assess the resulting decks, raising the question of whether higher scores reflect better documents or changes in grading. In shared-session text-only grading with template markers removed, five judges score the complete system 20.4 to 33.6 points out of 95 above the same model generating directly from a short prompt. Every judge scores the system higher on all seventeen development deliverables. Margins against direct Opus generation from a short prompt range from -4.7 to +0.8 points. Judges agree on broad progress across development rounds but agree less on final-deck rankings than on pooled scores. Repeated grading also shifts scores on unchanged decks, making small improvements difficult to distinguish from judge variability. 13 pages, 8 figures, 9 tables

**Решение:** -4 evaluating agentic deck generation in corporate and investment banking

---

### 666 · R2011

**Normative Centrality in the Qurʾān: A Corpus-Wide Analysis of Rhetorical Function at Structural Pivots**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.19044737

A prior corpus-wide study established that structural pivots — the compositional turning points of Qurʾānic surahs — cluster near geometric centers with extreme statistical significance across all 114 surahs. That study identified where pivots fall. The present study asks what they contain. We develop a seven-category taxonomy of Qurʾānic rhetorical function grounded in the discourse frameworks of Cuypers, El-Awa, Farrin, Mir, and Neuwirth, and apply it under blind conditions to the pivot zone and a matched control zone of each surah, using two independent large language model annotators. Inter-annotator agreement on pivot zones (κ = 0.687) exceeds agreement on control zones (κ = 0.480), indicating that pivot passages have more clearly defined rhetorical roles than non-central passages. Comparing category distributions across pivot and control zones (χ²(6) = 13.331, p < 0.05), we find that normative discourse — commands, narrative exemplars, and communal address — is overrepresented at structural centers, while warning and affective discourse is underrepresented. We term this pattern normative centrality: the structural center of a surah tends to deliver the directive or interpretive claim that gives meaning to the surrounding discourse. Analysis of Meccan and Medinan subcorpora reveals that this principle manifests differently across revelation phases — Medinan pivots concentrate legislative commands, Meccan pivots distribute across narrative and proclamatory modes — closely mirroring the traditional Meccan/Medinan distinction without recourse to historical dating criteria. These findings extend Cuypers’ qualitative observation that structural centers function as interpretive keys, providing the first corpus-scale statistical evidence that Qurʾānic surah architecture is not only geometrically organized but functionally so.

**Решение:** -4 rhetorical function and normative centrality in Quranic surahs

---

### 667 · R12160

**Evaluating Large Language Models with Psychometrics**

2024 · arXiv (Cornell University) · preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2406.17675

Large Language Models (LLMs) have demonstrated exceptional capabilities in solving various tasks, progressively evolving into general-purpose assistants. The increasing integration of LLMs into society has sparked interest in whether they exhibit psychological patterns, and whether these patterns remain consistent across different contexts -- questions that could deepen the understanding of their behaviors. Inspired by psychometrics, this paper presents a {comprehensive benchmark for quantifying psychological constructs of LLMs}, encompassing psychological dimension identification, assessment dataset design, and assessment with results validation. Our work identifies five key psychological constructs -- personality, values, emotional intelligence, theory of mind, and self-efficacy -- assessed through a suite of 13 datasets featuring diverse scenarios and item types. We uncover significant discrepancies between LLMs' self-reported traits and their response patterns in real-world scenarios, revealing complexities in their behaviors. Our findings also show that some preference-based tests, originally designed for humans, could not solicit reliable responses from LLMs. This paper offers a thorough psychometric assessment of LLMs, providing insights into reliable evaluation and potential applications in AI and social sciences.

**Решение:** -2 evaluating LLM psychological patterns with psychometric instruments (LLM as test subject)

---

### 668 · R4486

**Guideline-Concordant Answer Quality of Five Large Language Models on Indication Criteria for Total Hip Arthroplasty in Hip Osteoarthritis: A Single-Run Benchmark Against the 2021 German S3 Guideline (EKIT-Hip)**

2026 · Journal of Clinical Medicine · journalarticle, article · en · https://doi.org/10.3390/jcm15207944

Background/Objectives: Hip osteoarthritis (OA) is a highly prevalent musculoskeletal disorder associated with substantial functional impairment and healthcare burden. Although evidence-based clinical practice guidelines exist, including the 2021 guideline of the German Society for Orthopaedics and Trauma Surgery (DGOU), their implementation in routine practice remains incomplete. Large language models (LLMs) are increasingly consulted for guideline-related information, but the concordance of their answers with guideline recommendations is uncertain. This benchmark study evaluated the guideline concordance, comprehensiveness and length of answers generated by five widely used LLMs to questions derived from the 2021 German S3 guideline on evidence- and consensus-based indication criteria for total hip arthroplasty in hip OA (EKIT-Hip; AWMF register no. 187-001; lead society DGOU). It did not evaluate the effectiveness or safety of clinical decision support. Methods: In a cross-sectional, single-run benchmark study, 26 structured, context-free questions covering five of the six thematic complexes of the guideline (diagnosis and imaging; assessment of the level of suffering; evaluation of alternative therapeutic options; contraindications; optimisation of modifiable risk factors) were derived from the guideline recommendations and submitted between 9 November 2024 and 25 February 2025 through the consumer web interfaces of five LLM-based systems (GPT-4, GPT-4o, GPT-4o mini, Gemini Advanced and Consensus Premium), yielding 130 responses (one per system–question pair, each in a newly initiated chat session). Responses were evaluated by three board-certified orthopaedic surgeons blinded to model identity, using a four-point accuracy scale and a five-point comprehensiveness scale. Only a single consensus score per response was recorded, so inter-rater reliability could not be assessed. Response length was quantified in words and characters and benchmarked against the corresponding guideline text. Because all systems answered the same questions, ratings were analysed as paired, question-clustered data with cumulative-link mixed models (random intercept for question), Friedman and Cochran’s Q tests and question-level cluster-bootstrap confidence intervals; unpaired analyses were retained as sensitivity analyses. Results: Accuracy differed across systems (cumulative-link mixed model, likelihood-ratio χ2(4) = 49.0, p < 0.0001; paired Friedman χ2(4) = 41.7, p < 0.0001; unpaired Kruskal–Wallis sensitivity analysis H = 35.6, p < 0.0001). Mean accuracy was highest for GPT-4o (3.69 ± 0.55) and GPT-4 (3.62 ± 0.57), followed by GPT-4o mini (3.27 ± 0.78), Gemini Advanced (3.08 ± 0.84) and Consensus Premium (2.54 ± 0.71). Responses rated good or excellent accounted for 25/26 (96.2%) of GPT-4o and GPT-4 responses versus 15/26 (57.7%) for Consensus Premium. Comprehensiveness followed the same ordering (H = 33.0, p < 0.0001, ε2 = 0.23), with GPT-4o achieving the highest mean score (4.31 ± 0.79). In the cumulative-link mixed model, the odds of a higher accuracy rating relative to Consensus Premium were 51.8 (95% CI 12.4–215.9) for GPT-4o and 35.4 (95% CI 9.2–136.4) for GPT-4; GPT-4o and GPT-4 did not differ (OR 1.47, multiplicity-adjusted 95% CI 0.23–9.21), and their paired mean difference in accuracy (0.08 points, 90% CI −0.11 to 0.26) lay within an equivalence margin of ±0.5 points. Responses rated poor were observed for Consensus Premium (2/26) and Gemini Advanced (1/26) and not for the ChatGPT variants (0/26 each; exact 95% CI 0–13.2%), so a clinically relevant error rate cannot be excluded for any system. Response length differed markedly (Friedman χ2 = 47.3, p < 0.0001), ranging from 32.4 ± 11.5 words for Consensus Premium to 77.8 ± 24.9 words for GPT-4o, corresponding to 1.29-fold and 3.19-fold the length of the source guideline text, respectively. Conclusions: GPT-4o and GPT-4 received the highest ratings for accuracy and comprehensiveness in this single-run benchmark of static, context-free questions. These data describe guideline-concordant answer quality only; they do not establish clinical decision-support effectiveness or safety and do not support unsupervised clinical use of any evaluated system. Evaluation with standardised patient cases, repeated version-controlled runs, clinician-in-the-loop designs and prospective safety endpoints is required.

**Решение:** -4 guideline-concordant LLM answer quality in total hip arthroplasty

---

### 669 · R2308

**AI-Powered Self-Expanding Honeypots for Enhanced Attacker Engagement and Deception Longevity**

2026 · 2026 IEEE International Conference on Smart Sustainable Systems for Computer and Engineering Applications (3SCEA) · conference · https://doi.org/10.1109/3scea68071.2026.11603082

The paper introduces a self-expanding honeypot framework powered by AI intended to increase attacker engagement and extend the duration of deception in cybersecurity areas. Unlike the traditional fixed or dynamic honeypots, our system constantly opens new API endpoints based on current trending CVEs, allowing the attackers to work with the realistic flaws and at the same time receive the responses via large language models (llMs) that are state-consistent. The architecture has a dynamic documentation and artifact generator that enhances realism by producing Swagger/OpenAPI specifications, logs, and PDFs. A logging layer specifically set up for this purpose gathers metrics such as session duration, API exploration depth, and interaction frequency, thus creating intelligence that is useful for both defensive strategies and research analyzes. The proposed method is realized as a fully functional prototype that is capable of showing, through experiments, its feasibility, scalability, and persistence in isolated environments. The experimental evaluation proves that the AI-powered self-expansion feature doubles or even triples the engagement of and interaction time with attackers compared to baseline honeypots, thus upholding the effectiveness of CVE-based API generation in contemporary deception techniques. This research underscores the need to combine generative AI with vulnerability-aware design so that in the future it can further develop adaptive cyber defense mechanisms.

**Решение:** -4 AI-powered honeypots for cyber deception longevity

---

### 670 · R8923

**Exploring Human and AI Emotional Support Through Reframing of Negative Situations**

2025 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/fzvd8_v3

Increasingly, people use language models for emotional support, and understanding the quality of that support is crucial. This project (N = 3,740) focused on one of the pillars of emotional support and the most researched emotion regulation strategies, called cognitive reappraisal, which is the ability to extract multiple meanings from an emotional situation and to choose a framing that reduces its emotional intensity. In a first conservative test, we compared trained humans and GPT-4's ability for reappraisal using made-up vignettes and third-party human raters (Study 1), showing that GPT-4 outperformed humans. In Study 2 we then investigated whether the gap was driven by effort or skill by incentivizing participants to produce better reappraisals, which led to increased time spent on reappraisals but did not decrease the gap between humans and GPT-4. To examine how the perception that support came from AI affected evaluations, in Study 3 we provided participants with an AI label of the source of reappraisal, which reduced their evaluation of the effectiveness of reappraisal, but GPT-4 was still considered more effective. In Study 4, to ensure that differences were sustained in real-time interactions, we had participants share negative emotional situations with either a human or GPT-4 and receive reappraisal, replicating GPT-4's superior performance compared to humans. We conducted language analysis to identify differences between humans and GPT’s reappraisals, finding differences in language complexity, which explain some differences in evaluation. These results help us understand the nature of emotional support by LLMs and how it compares to humans.

**Решение:** -2 human raters evaluate GPT-4 generated cognitive reappraisal responses

---

### 671 · R4485

**CS_Metro at PsyDefDetect: Detecting Psychological Defense Mechanisms in Mental Health Dialogues with Summarization-Enhanced Transformer Ensembles**

2026 · conference-paper · https://doi.org/10.18653/v1/2026.bionlp-2.26

Detecting psychological defense mechanisms in supportive conversations is essential for assisting mental health practitioners.Natural language processing techniques are increasingly integral to such systems, enabling automated classification of defense levels to better understand help-seeker behavior and resistance patterns.In PsyDefDetect at BioNLP 2026, we address the task of nine-class defense level classification on the PSYDEFCONV corpus.We propose a three-stage pipeline combining LLM-based dialogue summarization, domainspecific transformer fine-tuning, and rule-based ensemble prediction.Additionally, we evaluate three mental health domain-specific transformers (Mental-BERT, Mental-RoBERTa, Mental-XLNet) alongside fine-tuned LLMs (Qwen3-4B, Qwen3-1.7B,Mistral-7B under different input conditions.Experimental results on the released test-set gold labels show that our ensemble approach achieves the best performance, reaching 34.69% macro F1 and surpassing the baseline by 4.69 percentage points.On the official PsyDefDetect Leaderboard 1 (labels 1-8), the submitted system achieved a Macro-F1 score of 23.46%, ranking 15th out of 21 teams, while on Leaderboard 2 (labels 0-8), it achieved 30.04%, securing 14th place.These findings demonstrate that domainspecific transformers substantially outperform generic LLM fine-tuning on this specialized clinical task.

**Решение:** + T1 detecting psychological defense mechanisms in mental health dialogues: LLMs vs human gold labels

---

### 672 · R6804

**A Blinded Multi-LLM Content-Coding Instrument: Protocol Specification and Inter-Coder Reliability Validation on an Organizational Corpus**

2026 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.21756063

Content coding is a reliability bottleneck of qualitative and mixed-methods organizational research: it is labor-intensive, difficult to reproduce, and vulnerable to a coder who can see the study’s hypotheses. Large language models now annotate text at or above crowd-worker quality, but naive single-model use reintroduces the failure modes intercoder-reliability protocols were built to remove – unauditable calls, hypothesis leakage, fabricated codes, and single-rater dependence. This article specifies a blinded multi-LLM content-coding instrument that imports human intercoder-reliability discipline into machine-assisted coding. Three heterogeneous models code each case independently from a neutral, source-cited evidence dossier while blinded to the hypotheses and the case’s study role; cells combine by majority-vote-or-flag with author adjudication; a model that cannot determine a cell returns uncertain rather than guess; every call is logged with an exact model pin; and the harness and the empty coding schema are committed before any datum exists. On a corpus of thirty documented organizational integration cases the instrument reached almost-perfect inter-coder agreement (Fleiss’ κ = .838), with a 2.7% flag rate concentrated entirely on auxiliary tokens. Reliability is distinguished from downstream inferential validity, which is left to future contrast studies. The harness, logs, and datasets are released as an auditable artifact. Includes zharnikov-2026bh-multi-llm-coding-instrument.yaml (Paper Spec v0.1.0) – a machine-readable specification of the paper’s claims, assumptions, and dependencies. The paper’s full machine-first bundle (the SPINE claim/dependency graph and the ONTOLOGY term module) lives in the public repository; see github.com/spectralbranding/paper-spec for the standard. This PDF is generated programmatically from that machine-first source under a research-as-repository model.

**Решение:** -5 multi-LLM content coding instrument evaluated only via LLM-to-LLM agreement

---

### 673 · R12166

**Jailbreaking Large Language Models Through Alignment Vulnerabilities in Out-of-Distribution Settings**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2406.13662

Recently, Large Language Models (LLMs) have garnered significant attention for their exceptional natural language processing capabilities. However, concerns about their trustworthiness remain unresolved, particularly in addressing ``jailbreaking'' attacks on aligned LLMs. Previous research predominantly relies on scenarios involving white-box LLMs or specific, fixed prompt templates, which are often impractical and lack broad applicability. In this paper, we introduce a straightforward and novel method called ObscurePrompt for jailbreaking LLMs, inspired by the observed fragile alignments in Out-of-Distribution (OOD) data. Specifically, we first formulate the decision boundary in the jailbreaking process and then explore how obscure text affects LLM's ethical decision boundary. ObscurePrompt starts with constructing a base prompt that integrates well-known jailbreaking techniques. Powerful LLMs are then utilized to obscure the original prompt through iterative transformations, aiming to bolster the attack's robustness. Comprehensive experiments show that our approach substantially improves upon previous methods in terms of attack effectiveness, maintaining efficacy against two prevalent defense mechanisms.

**Решение:** -4 jailbreaking LLMs through alignment vulnerabilities

---

### 674 · R8609

**Automatic Large Language Models Creation of Interactive Learning Lessons**

2025 · EC-TE · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.48550/arxiv.2506.17356

We explore the automatic generation of interactive, scenario-based lessons designed to train novice human tutors who teach middle school mathematics online. Employing prompt engineering through a Retrieval-Augmented Generation approach with GPT-4o, we developed a system capable of creating structured tutor training lessons. Our study generated lessons in English for three key topics: Encouraging Students' Independence, Encouraging Help-Seeking Behavior, and Turning on Cameras, using a task decomposition prompting strategy that breaks lesson generation into sub-tasks. The generated lessons were evaluated by two human evaluators, who provided both quantitative and qualitative evaluations using a comprehensive rubric informed by lesson design research. Results demonstrate that the task decomposition strategy led to higher-rated lessons compared to single-step generation. Human evaluators identified several strengths in the LLM-generated lessons, including well-structured content and time-saving potential, while also noting limitations such as generic feedback and a lack of clarity in some instructional sections. These findings underscore the potential of hybrid human-AI approaches for generating effective lessons in tutor training. Full Research Paper, 15 pages, In Proceedings of 20th European Conference on Technology Enhanced Learning (ECTEL2025)

**Решение:** -4 automatic LLM generation of tutor training lessons for middle school math

---

### 675 · R2666

**The Closed-Loop Hypothesis: Embodiment, Persistent Stakes, Developmental Continuity, and the Possible Emergence of Artificial Consciousness**

2026 · Zenodo (CERN European Organization for Nuclear Research) · text/, article · en · https://doi.org/10.5281/zenodo.22171808

Contemporary artificial intelligence has acquired sophisticated language and abstract reasoning without reproducing the developmental architecture through which biological cognition arose. This paper proposes the Closed-Loop Hypothesis, an architecture-level framework for investigating whether that asymmetry may be relevant to artificial consciousness. The framework begins with the Reverse Developmental Order: biological abstraction emerged within organisms already engaged in continuous regulation, sensation, action, learning, and survival, whereas the dominant contemporary foundation-model trajectory has approached cognition largely from the opposite direction. The hypothesis does not identify embodiment itself with consciousness. Instead, it proposes that consciousness-relevant properties may become more plausible when intelligence is integrated into a persistent loop linking exteroception, interoception-like monitoring, endogenous valuation, autobiographical memory, self-modeling, autonomous action, and consequences for the continuing integrity of the same agent. This condition is termed persistent stakes. The paper further distinguishes origin requirements from downstream resilience, arguing that persistence of consciousness after sensory or bodily loss does not by itself establish that those functions were irrelevant to developmental origin. It also distinguishes development from assembly, proposing that continuous developmental coupling may generate causal organization not reproduced by attaching separately trained modules after the fact. The framework is positioned alongside embodied cognition, enactivism, interoceptive inference, homeostatic machine proposals, developmental robotics, active-inference approaches, and theory-derived AI-consciousness indicators. Its proposed contribution is not any component in isolation, but their organization into a comparative research programme with explicit predictions, defeaters, and an ethical corollary: if artificial systems become plausible subjects of experience, developmental treatment may become part of alignment rather than a concern separable from it.

**Решение:** -1 Closed-Loop Hypothesis on embodiment and artificial consciousness

---

### 676 · R9885

**Elevating LLMs Via Synergy of Quantum Computing and Classical Transformer Models**

2025 · International Conference on AI-ML Systems (AIMLSystems) · conference, conference-paper · https://doi.org/10.1109/aimlsystems67835.2025.11330851

Quantum computation offers new directions in computer science that go beyond classical systems' state-of-the-art abilities. The combination of quantum technologies with Large Language Models (LLMs) provides promising avenues for the creation of more efficient and powerful NLP architectures. In this research, we examine quantum-enhanced transformers and further develop the Self-Attention Sequential Quantum Transformer Channel (SASQuatch) framework to enhance inference time and perplexity. The models proposed are tested on sentence completion tasks and compared against a baseline transformer, showing significant gains in efficiency and predictive power. We further compare the method with other optimization methods, such as the Quantum Approximate Optimization Algorithm (QAOA), thus highlighting the necessity of further investigation of hybrid quantum architectures in improving the performance of large-scale language models.

**Решение:** -4 quantum-enhanced transformer models

---

### 677 · R6309

**Conversational Voice Aesthetic Model with Reinforcement Learning from Human Listeners**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.10868

We introduce Conversational Voice Aesthetic Model, a speech large language model for describing the voice aesthetics of real or synthetic speech responses in natural conversational contexts. Given a context and a response speech, CVAM describes salient moments that characterize the voice and predicts nine categorical attributes spanning gender, pitch, pacing, emotion, and delivery. The key challenge lies in perceptual fields such as emotion and delivery, which are inherently subjective and lack definitive ground truth. Therefore, we collect ~10 human annotations for each of 3k real and synthetic responses derived from the CANDOR corpus. CVAM is supervised finetuned on synthesized aesthetic descriptions and labels, then optimized with Group Relative Policy Optimization on human judgments. Experiments show that CVAM better agrees with human listeners than Gemini 3.1 Pro and open-source speech LLMs, and outperforms single-human-vs.-rest agreement. Together, we demonstrate the importance of grounding voice aesthetics in human perception and propose a principled framework for human alignment.

**Решение:** -4 speech LLM predicting voice aesthetics (gender, pitch, pacing, delivery)

---

### 678 · R2233

**Beyond the Single Path: Divergent Reasoning for LLM-based Recommendation**

2026 · Annual International ACM SIGIR Conference on Research and Development in Information Retrieval · book, journalarticle, conference · https://doi.org/10.1145/3805712.3809732

Large Language Models (LLMs) have demonstrated strong potential in recommendations due to their powerful reasoning capabilities. However, existing methods typically rely on a single reasoning path to drive the entire Top-K recommendations. This paradigm is prone to reasoning path collapse, where limiting exploration of potentially superior and diverse reasoning paths within the LLMs space. As a result, both the accuracy and diversity of the recommendation outcomes are constrained. To address this issue, we propose a novel model, Divergent Reasoning for LLM-based Recommendation, named DivReason. Inspired by the structure of intellect theory, which emphasizes a two-stage cognitive process of divergent thinking followed by convergent thinking, DivReason is designed with two core components: the Divergent Reasoning Path Generation Module and the Reasoning Path Aggregation Module. In the first module, DivReason introduces a training-free form of controlled uncertainty to promote diverse reasoning, leveraging Monte Carlo Dropout and Directional Perturbation to expand exploration in the latent reasoning space. In the Reasoning Path Aggregation Module, we adaptively select a subset of high-quality reasoning paths from the entire path pool and aggregate them into a unified reasoning representation. Meanwhile, we further adopt an alternating reinforcement learning strategy to optimize the model, explicitly balancing accuracy and diversity during training. Extensive experimental results show that DivReason effectively mitigates the issue of reasoning path collapse, while improving both the accuracy and diversity of LLM-based recommendations.

**Решение:** -4 divergent reasoning for LLM-based recommender systems

---

### 679 · R3603

**Safety Paradox: How Enhanced Safety Awareness Leaves LLMs Vulnerable to Posterior Attack**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.05614

Large language models (LLMs) are rigorously aligned to refuse harmful requests, a process that inherently cultivates a latent capacity to evaluate and recognize unsafe content. In this work, we reveal that this advanced safety awareness inadvertently introduces a fatal vulnerability. We introduce Posterior Attack, a single-query jailbreak that bypasses guardrails by prompting the model to generate the exact harmful response its internal classifier would normally flag as unsafe. Through extensive empirical evaluation across 30 open-source LLMs (up to 35B parameters in size) and frontier models (e.g., GPT-5, Claude 4.6), we observe a striking phenomenon: models with superior safety-judgment capabilities are disproportionately more susceptible to this exploitation. To explain this, we formalize the Safety Paradox, analytically showing that monotonic improvements in safety alignment naturally amplify posterior vulnerability. Finally, we establish a causal link via reinforcement learning interventions, exemplifying that artificially degrading a model's safety judgment immunizes it against the attack, whereas enhancing judgment exacerbates the vulnerability. Our findings highlight potential flaws in current alignment paradigms, indicating that defense mechanisms may require further structural refinement. Accepted to EMNLP 2026 (Main)

**Решение:** -4 Safety Paradox in LLM jailbreak vulnerabilities

---

### 680 · R9626

**«Yes, I understood that in German: wishy-washy!» Political polarization and the foreign language effect**

2025 · International Journal of Bilingualism · journalarticle, article · en · https://doi.org/10.1177/13670069251398718

Aims and objectives: When bilinguals use their weaker language, they tend to apply different rationalities and have less immediate emotional reactions (the so-called foreign-language effect ). The aim of this study is to test whether bilingual politicians differ between statements they make in their first (L1) or in their second language (L2). More specifically, we hypothesize that using L2 might be associated with less polarizing political language. Method: We analyze a corpus of more than 2,000 interactional turns uttered by 10 Swiss politicians in national TV debates in French and in German. All politicians appear both in French and in German, but one of the two languages is their L1, respectively. The politicians’ statements are assessed regarding their polarizing potential by a large language model (LLM) and by human raters. Data and analysis: Descriptive and inferential statistical analyses are then carried out to unveil individual and collective patterns of difference across L1 and L2 in the data. Findings: The results suggest a robust foreign effect in the analyzed data. It appears that engaging in political debates in non-dominant languages coincides with more factual and less emotional and less polarizing language. Originality: This study is the first one to investigate the foreign effect in politics, the first one to analyze not lab-elicited but natural conversational data, and the first one to present an operationalization of the classification of political polarizing speech for the use with LLMs. Implications: The study suggests that a foreign language effect is not confined to lab settings but extends to socially relevant contexts such as authentic political debates. There is a moderate positive correspondence between human and LLM ratings, which implies that LLMs may cautiously be used to classify large corpora of texts. Limitations: Further research is necessary to test and increase the validity and reliability of LLM-based text classifications.

**Решение:** -4 foreign-language effect in bilingual politicians statements

---

### 681 · R10057

**Radiology's Last Exam (RadLE): Benchmarking Frontier Multimodal AI Against Human Experts and a Taxonomy of Visual Reasoning Errors in Radiology**

2025 · arXiv.org · journalarticle, preprint/article · https://doi.org/10.48550/arxiv.2509.25559

Generalist multimodal AI systems such as large language models (LLMs) and vision language models (VLMs) are increasingly accessed by clinicians and patients alike for medical image interpretation through widely available consumer-facing chatbots. Most evaluations claiming expert level performance are on public datasets containing common pathologies. Rigorous evaluation of frontier models on difficult diagnostic cases remains limited. We developed a pilot benchmark of 50 expert-level "spot diagnosis" cases across multiple imaging modalities to evaluate the performance of frontier AI models against board-certified radiologists and radiology trainees. To mirror real-world usage, the reasoning modes of five popular frontier AI models were tested through their native web interfaces, viz. OpenAI o3, OpenAI GPT-5, Gemini 2.5 Pro, Grok-4, and Claude Opus 4.1. Accuracy was scored by blinded experts, and reproducibility was assessed across three independent runs. GPT-5 was additionally evaluated across various reasoning modes. Reasoning quality errors were assessed and a taxonomy of visual reasoning errors was defined. Board-certified radiologists achieved the highest diagnostic accuracy (83%), outperforming trainees (45%) and all AI models (best performance shown by GPT-5: 30%). Reliability was substantial for GPT-5 and o3, moderate for Gemini 2.5 Pro and Grok-4, and poor for Claude Opus 4.1. These findings demonstrate that advanced frontier models fall far short of radiologists in challenging diagnostic cases. Our benchmark highlights the present limitations of generalist AI in medical imaging and cautions against unsupervised clinical use. We also provide a qualitative analysis of reasoning traces and propose a practical taxonomy of visual reasoning errors by AI models for better understanding their failure modes, informing evaluation standards and guiding more robust model development. 29 pages, 7 figures, 7 tables, includes Annexure (1). Part of the work accepted at RSNA 2025 (Cutting Edge Oral Presentation)

**Решение:** -4 RadLE: multimodal AI benchmark in radiology

---

### 682 · R2800

**It’s Not Just the Prompt: Model Choice Dominates LLM Creative Output**

2026 · Extended Abstracts of the CHI Conference on Human Factors in Computing Systems (CHI EA) · journalarticle, book, conference-paper · https://doi.org/10.1145/3772363.3799284

Prompt engineering is often treated as a reliable control mechanism for LLM behavior, yet LLM outputs vary even under similar prompts due to stochasticity. We quantify how much output variance is driven by prompt choice versus model choice and by inherent within-LLM stochasticity by evaluating 12 LLMs on 10 creativity prompts in an open-ended divergent-thinking task (AUT), measuring answer quality (originality) and quantity (number of answers), generating 100 samples per prompt. Then, we partition the variance into model, prompt, within-LLM stochasticity, and model × prompt interaction components. Our findings show that model choice is at least as important as prompt choice in this setting. For originality, the model explains 41% of the variance. Prompts explain 36%, and within-model stochasticity explains 11%. For fluency, prompts explain 4% of the variance. Model choice explains 51%, and within-model stochasticity 34%. Beyond variance decomposition, models exhibit persistent “creative fingerprints” in thematic preferences and formatting habits.

**Решение:** -6 output variance and model choice in LLM creative text generation

---

### 683 · R7135

**Use of Large Language Models for Simulating Motivational Interviewing Counselling: A Scoping Review Protocol**

2025 · Research Square · preprint, ppr, posted-content · en · https://doi.org/10.21203/rs.3.rs-7539260/v1

Abstract Background Large Language Models (LLMs) such as GPT-4, PaLM, and LLaMA are increasingly applied in healthcare for tasks such as therapeutic dialogue and mental health support. Motivational interviewing (MI), a client-centred counselling method emphasizing empathy, partnership, evocation, and acceptance, has potential to be simulated by these models. However, questions remain about whether LLMs can replicate MI’s relational and emotional depth. This review aims to scope the evidence on the utilization and challenges of LLMs for delivering and simulating MI. Methods We will follow a five-step scoping review framework and report the review according to PRISMA-ScR guidelines. A comprehensive search of academic databases and grey literature will be conducted. We will include study that used LLMs for simulating MI among adults and all types of study designs. Discussion This will be the first scoping review to systematically explore AI-driven language models in relation to MI. The results will inform researchers, clinicians, and developers about the potential and limitations of LLMs in counselling, guiding ethical, safe, and evidence-based tool development. Trial registration: This protocol is registered on the Open Science Framework (OSF): https://doi.org/10.17605/OSF.IO/XEQYM

**Решение:** -1 scoping review protocol of LLMs for simulating motivational interviewing

---

### 684 · R6096

**Evaluating ChatGPT-5's Performance in Answering Common Patient Questions About Femoroacetabular Impingement and Hip Arthroscopy.**

2026 · Indian journal of orthopaedics · journal article, journalarticle, article · eng · https://doi.org/10.1007/s43465-026-01696-3

Background: Hip arthroscopy (HAS) is widely used to treat femoroacetabular impingement syndrome (FAIS), and many patients rely on online resources for medical information. Large language models (LLMs) such as ChatGPT have shown potential as supplementary educational tools in orthopedics; however, existing evaluations are limited to earlier model generations with variable accuracy and completeness. This study aimed to evaluate the accuracy, clarity, relevance, and completeness of ChatGPT-5 responses to common patient questions regarding FAIS and HAS. Methods: ChatGPT-5 was used to generate 25 frequently asked patient questions and corresponding answers related to hip preservation. Two fellowship-trained hip preservation surgeons independently evaluated each response using a five-point Likert scale across four predefined domains: relevance, accuracy, clarity, and completeness. Descriptive statistics were calculated as mean ± standard deviation for each domain. Inter-rater reliability was assessed using a two-way random-effects intraclass correlation coefficient with absolute agreement (ICC [2, 1]) and complemented by exact agreement percentages. Results: All responses received excellent scores, with mean values ranging from 4.84 ± 0.27 (completeness) to 5.00 ± 0.00 (relevance). Accuracy (4.97 ± 0.08) and clarity (4.91 ± 0.17) were near-perfect. ICC values demonstrated moderate to excellent agreement (0.70-0.81), complemented by high exact agreement rates (84-100%). No answer contained factually incorrect, misleading, or unsafe information. Minor reductions in completeness were attributable to occasional brevity rather than substantive omissions. Conclusion: ChatGPT-5 generated highly accurate, clear, and clinically appropriate patient-oriented explanations regarding FAIS and HAS, showing clear improvement compared with earlier ChatGPT versions. Although ChatGPT-5 represents a marked advancement in AI-based patient education, its use should be regarded as a complementary educational tool rather than a replacement for professional orthopedic counseling.

**Решение:** -4 patient questions about femoroacetabular impingement and hip arthroscopy

---

### 685 · R10218

**Script generation from synthetic stories using lightweight LLM and emotion-aware TTS pipelines**

2025 · Social Network Analysis and Mining · journalarticle, review, article · en · https://doi.org/10.1007/s13278-025-01558-0

This study presents a complete end-to-end pipeline for generating emotionally annotated dialogues in the format Speaker (Emotion): Dialogue , conditioned on a given set of keywords. The system begins with a Hugging Face short story dataset used to build the training corpus. To accurately identify speakers and gender, FastCoref was applied with dialogue masking, followed by BookNLP for improved entity and gender resolution. Emotional context was assigned to each dialogue using a Bi-GRU–based emotion classification model, while representative keywords were extracted using Mistral-7B through few-shot prompt engineering. The resulting dataset of keyword–story pairs was then used to fine-tune three lightweight generative models: TinyLlama, Phi-1.5, and GPTNeo for conditional story generation. Model outputs were evaluated through both automated and human-centered assessments. Automated metrics such as perplexity and Distinct-1/Distinct-2 measured fluency and lexical diversity, while an LLM-based reviewer (DeepSeek-chat-v3-0324) rated coherence, creativity, and linguistic quality. In parallel, a human evaluation was conducted using Google Forms, where five participants rated 20 generated stories on coherence, emotional engagement, and overall quality. The averaged human ratings were compared with LLM-based scores to validate consistency in subjective and model-based evaluation. Overall, GPTNeo achieved the highest combined performance, with superior lexical diversity and an average rating of 4.0/5, followed by Phi-1.5 (3.6) and TinyLlama (2.8).

**Решение:** -6 script generation from synthetic stories using lightweight LLM and TTS

---

### 686 · R10241

**The Evolution And Infrastructure Of Generative AI Chatbots: A Technical And Strategic Analysis**

2025 · Journal of International Crisis and Risk Communication Research · journalarticle, article · https://doi.org/10.63278/jicrcr.vi.3467

The rapid advancement of large language model-based conversational AI systems represents a transformative milestone in artificial intelligence, fundamentally reshaping human-computer interaction paradigms across diverse application domains. This article provides a comprehensive technical and strategic analysis of the infrastructure, architectural considerations, and operational challenges inherent in deploying generative AI chatbots at scale. To examine the competitive landscape of hardware acceleration strategies, contrasting general-purpose GPU architectures with custom silicon solutions such as Google's Tensor Processing Units and Meta's specialized inference accelerators, highlighting the nuanced trade-offs between performance, flexibility, and cost-effectiveness. The article explores the principles of hardware-software co-design essential for optimizing transformer-based architectures, including the synergistic integration of computational substrates, memory hierarchies, and distributed training frameworks that enable efficient processing of models containing billions of parameters. Performance requirements for commercial viability are evaluated, encompassing throughput optimization, ultra-low latency targets, and the continuous innovation in serving infrastructure necessary to maintain competitive advantage amid proliferating proprietary and open-source alternatives. Critical attention is devoted to security, privacy, and trust considerations that extend beyond traditional cybersecurity paradigms, including vulnerabilities specific to AI systems, regulatory compliance frameworks, and the imperative for comprehensive defense mechanisms protecting sensitive user data throughout the inference pipeline. This interdisciplinary examination synthesizes technical, economic, and ethical dimensions of conversational AI deployment, providing stakeholders with insights essential for navigating the complex trade-offs between model capability, operational efficiency, and responsible system design in an era of accelerating artificial intelligence adoption.

**Решение:** -1 technical and strategic analysis of generative AI chatbots evolution

---

### 687 · R12450

**Investigating ChatGPT’s Potential to Assist in Requirements Elicitation Processes**

2023 · Euromicro Conference on Software Engineering and Advanced Applications (SEAA) · journalarticle, conference, review · en · https://doi.org/10.1109/seaa60479.2023.00061

Natural Language Processing (NLP) for Requirements Engineering (RE) (NLP4RE) seeks to apply NLP tools, techniques, and resources to the RE process to increase the quality of the requirements. There is little research involving the utilization of Generative AI-based NLP tools and techniques for requirements elicitation. In recent times, Large Language Models (LLM) like ChatGPT have gained significant recognition due to their notably improved performance in NLP tasks. To explore the potential of ChatGPT to assist in requirements elicitation processes, we formulated six questions to elicit requirements using ChatGPT. Using the same six questions, we conducted interview-based surveys with five RE experts from academia and industry and collected 30 responses containing requirements. The quality of these 36 responses (human-formulated + ChatGPT-generated) was evaluated over seven different requirements quality attributes by another five RE experts through a second round of interview-based surveys. In comparing the quality of requirements generated by ChatGPT with those formulated by human experts, we found that ChatGPT-generated requirements are highly Abstract, Atomic, Consistent, Correct, and Understandable. Based on these results, we present the most pressing issues related to LLMs and what future research should focus on to leverage the emergent behaviour of LLMs more effectively in natural language-based RE activities. Accepted at SEAA 2023. 8 pages, 5 figures

**Решение:** -4 ChatGPT assisting in requirements elicitation processes

---

### 688 · R0295

**Overactive Bladder and Falls: Interpreting an Uncertain Association in the Context of Confounding and Measurement Limitations**

2026 · Neurourology and Urodynamics · article · en · https://doi.org/10.1002/nau.70294

I read with interest the recent article by Linder et al. examining the association between overactive bladder (OAB) and fall risk in a nationally representative sample of US adults aged 20–69 years [1]. Given the substantial morbidity associated with falls and the high prevalence of OAB, this study addresses a clinically relevant and timely question. The use of contemporary NHANES data to explore this relationship adds valuable insight into a potentially underrecognized contributor to fall risk. In this cross-sectional analysis of 4118 participants, OAB was defined using a composite symptom score incorporating urge urinary incontinence and nocturia, and fall history was based on self-reported events within the preceding 12 months. The authors reported a higher prevalence of falls among individuals with OAB (39.7% vs. 25.7%), with a graded increase according to symptom severity. After adjustment for sociodemographic and clinical variables, OAB remained independently associated with increased odds of recent falls (adjusted OR 1.42; 95% CI 1.10–1.83), leading the authors to suggest that OAB may represent a potentially modifiable risk factor [1]. An important issue to consider is the potential influence of residual confounding, particularly related to pharmacologic exposure and underlying patient vulnerability. A growing body of evidence suggests that anticholinergic burden is likely a major contributor to fall risk in patients with OAB. Longitudinal data demonstrate a dose–response relationship between cumulative anticholinergic exposure and falls and fractures, while prospective studies report more than a twofold increase in fall risk among users of OAB anticholinergic medications, even after adjustment for comorbidities [2, 3]. These findings raise the possibility that the observed association between OAB and falls may, at least in part, reflect treatment-related effects rather than disease-specific mechanisms. Furthermore, anticholinergic burden is highly prevalent across populations, increases with age, and arises from multiple medication classes rather than OAB-specific therapies alone, further supporting the likelihood that medication-related factors contribute meaningfully to the observed association [4]. In addition, OAB itself may act as a marker of frailty, multimorbidity, and functional impairment—well-established determinants of falls that may not be fully captured in survey-based datasets. The cross-sectional design further limits causal inference. Because OAB symptoms and fall history were assessed contemporaneously, temporal relationships cannot be established and reverse causation remains plausible. Individuals with impaired mobility, neurologic conditions, or functional decline—recognized risk factors for falls—may also be more likely to report OAB symptoms. Moreover, the relationship between urinary symptoms and falls is inherently multifactorial, involving behavioral (e.g., urgency-driven rushing), physical, cognitive, and environmental factors [5, 6]. Taken together, these considerations suggest that the reported association should be interpreted cautiously and may reflect shared underlying vulnerability rather than a direct causal effect. Additional methodological limitations relate to potential misclassification of both exposure and outcome, which may have substantially influenced the observed association. The definition of OAB relied on a simplified symptom composite that does not align with established diagnostic frameworks recommended in current international guidelines [7, 8]. Importantly, urgency—the defining feature of OAB—was not directly assessed using validated instruments, raising uncertainty as to whether the study population accurately represents individuals with clinically meaningful OAB. Similarly, fall history was based on 12-month self-report without differentiation between single and recurrent events or assessment of severity. This approach introduces considerable heterogeneity in outcome definition and may capture a broad spectrum of events with varying clinical relevance. As a result, the relationship between urinary symptoms and falls may be difficult to interpret within a coherent clinical framework. Taken together, these limitations raise the possibility that the reported association reflects imprecision in both exposure and outcome definitions rather than a robust underlying causal relationship. Importantly, this distinction has meaningful clinical implications. Interpreting OAB as a direct and modifiable cause of falls, rather than as a marker of underlying vulnerability or treatment exposure, may lead to inappropriate management strategies, including escalation of pharmacotherapy without adequate consideration of medication-related risks. A more nuanced interpretation that incorporates anticholinergic burden, functional status, and behavioral factors may better inform fall risk assessment and patient-centered management. In conclusion, this study highlights an important and clinically relevant association using nationally representative data. However, the findings should be interpreted with caution given the potential for residual confounding, measurement limitations, and the inherent constraints of cross-sectional design. Future prospective studies incorporating detailed pharmacologic data and standardized assessment of both OAB and fall outcomes are needed to clarify the nature of this relationship and guide clinical decision-making. Ali Furkan Batur: conception and design, manuscript writing, drafting the manuscript. During the preparation of this manuscript, an artificial intelligence–based language tool (ChatGPT) was used to assist with language refinement and stylistic editing. The authors reviewed and revised the text as needed and take full responsibility for the content and interpretation presented in this letter. The author has nothing to report. Institutional Review Board approval was not required because this paper is based on publi

**Решение:** -1 commentary on overactive bladder and fall risk

---

### 689 · R3900

**Continuous Context Sampling Allows Extending Diversity Boundaries of Large Language Models**

2026 · Annual Meeting of the Association for Computational Linguistics · journalarticle, conference · https://doi.org/10.18653/v1/2026.acl-srw.126

Starting from the observation that conditioning a poetry-writing prompt with a pancake recipe leads an LLM to produce a coherent poem incorporating pancake-related content and, more broadly, that such contexts arrange themselves into a structured semantic vector space, we argue that this renders the space explorable. By sampling it and using the resulting continuous representations to condition an LLM’s generation distribution, we can systematically expand the model’s reachable semantic range. We introduce a framework that requires no modification of LLM parameters and operational-izes this idea by conditioning LLM’s generation via an xRAG-style projector (Cheng et al., 2024). Our experiments demonstrate that this sampling-based conditioning substantially increases generative diversity, with direct benefits for enhancing divergent thinking, a core facet of creativity, in language models. 1

**Решение:** -6 continuous context sampling in poetry writing

---

### 690 · R11344

**PromotiCon: Prompt-based Emotion Controllable Text-to-Speech via Prompt Generation and Matching**

2024 · Conference proceedings/Conference proceedings - IEEE International Conference on Systems, Man, and Cybernetics · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/smc54092.2024.10831218

Text-to-speech (TTS) technologies have recently expanded to incorporate natural language prompts for user-friendly control of speech styles, driven by significant advancements in language models. Traditional prompt-based TTS research, however, typically requires large-scale prompt generation that often necessitates costly human annotations. To address this challenge, we propose PromotiCon, a model that leverages prompts generated without human annotations to control emotions in speech. Our model utilizes abundant prompts generated using a large language model. Additionally, we propose an emotion distance-based prompt-speech matching method to appropriately pair the generated prompts with the most resembling speech data. To enhance speaker adaptation, we utilize a semi-supervised approach that allows the joint utilization of multi-speaker data without emotion labels. As a result, our model facilitates zero-shot emotional speech synthesis. Our experimental results confirm the effectiveness of our approach. Audio samples are available at https://promoticon.github.io/.

**Решение:** -4 PromotiCon: prompt-based emotion controllable TTS

---

### 691 · R6081

**Towards reliable detection of online nutrition misinformation: LLM annotation, multi-view classification, and knowledge-grounded reasoning**

2026 · University of North Florida Digital Commons (University of North Florida) · dissertation

Nutrition misinformation on social media often arises from selective or decontextualized interpretations of established dietary evidence, particularly in contested domains such as seed oils and omega-6 fatty acids. To address this challenge, we present a unified framework for annotation, detection, and evidence-grounded interpretation of nutrition-related content on Instagram, integrating large language models (LLMs), interpretable machine learning, and retrieval-augmented generation (RAG) grounded in computable biomedical knowledge. We curate a dataset of 317 Instagram captions, consisting of 169 seed oil-related and 148 omega-6-related posts. Expert nutritionists independently annotate posts using the U.S. Dietary Guidelines (2020–2025), producing gold-standard labels via majority voting. We evaluate five open-source LLMs as automated annotators and introduce a hierarchical error taxonomy that categorizes misclassifications by direction, mechanism, and contributing factors, revealing systematic failure modes such as misinterpretation of nuanced claims and overconfident reasoning. In parallel, we benchmark three complementary misinformation detection approaches: feature-based traditional machine learning models that incorporate linguistic, rhetorical, affective, and psychological signals; embedding-based classification; and transformer-based fine tuning. We further assess model robustness under in-domain and cross-domain set tings, highlighting differences in generalization between semantic and linguistically grounded representations. Transformer-based models achieve the strongest performance in in-domain settings, while feature-based representations remain competitive and offer improved interpretability under constrained evaluation conditions. Finally, we develop a RAG framework that operationalizes the U.S. Dietary Guide lines as a sentence-indexed knowledge base. Retrieved evidence is paired with each post to enable a language model to generate grounded classifications and explanations that explicitly align or contrast user claims with authoritative dietary recommendations. Results indicate that retrieval grounding in the U.S. Dietary Guidelines improves factual consistency and the quality of model-generated explanations. This work has implications for the design of reliable and interpretable health misinformation detection systems that integrate human expertise, machine learning models, and structured biomedical knowledge.

**Решение:** -4 online nutrition misinformation detection on social media

---

### 692 · R2716

**PrepWise AI: A Smart Preparation Assistant for Study and Career**

2026 · Zenodo (CERN European Organization for Nuclear Research) · journalarticle/, article · https://doi.org/10.5281/zenodo.19950200

Modern undergraduate engineering students face a dual challenge: mastering semester syllabi within compressed academic timelines while simultaneously cultivating the technical and communicative competencies that industry recruitment processes demand. Existing digital tools tend to address only one of these dimensions in isolation, leaving students without a cohesive and adaptive support ecosystem. This paper introduces PrepWise AI, a full-stack, privacy-preserving intelligent platform that consolidates academic study planning and multimodal interview preparation into a single unified environment. The system is organized around four interdependent modules. The Smart Study Planner interprets free-form natural language exam prompts and constructs structured, day-wise preparation schedules through constrained prompt engineering over a locally hosted large language model (LLM). The Internal Assessment (IA) Planner bridges teacher-defined institutional syllabi with student-facing AI-generated resources, dynamically calibrating content depth and emphasis based on examination proximity. The Resources Module delivers curated theory notes enriched with diagrams alongside an embedded Data Structures and Algorithms (DSA) coding environment powered by the Monaco Editor, with real-time test-case evaluation. The AI Interview Assistant conducts comprehensive multimodal candidate evaluation through synchronized video analysis—comprising MediaPipe Face Mesh landmark detection, pixel-level frame processing, and YOLO-based object detection—alongside audio preprocessing using FFmpeg for extraction, resampling, and normalization of the audio signal, followed by pitch estimation and speech rate computation, culminating in semantic answer evaluation via a locally deployed LLM. The backend is implemented using Flask and FastAPI microservices. All LLM inference executes on-premise through the Ollama platform using Qwen 2.5 (7B) and Mistral models. Firebase Firestore supports institutional data persistence. Experimental evaluation with thirty undergraduate participants yielded a schedule relevance score of 86.4%, a user satisfaction rating of 4.2 out of 5.0, and a plan completion rate of 72.4%. Interview assessment quality was validated by a Pearson correlation of r = 0.81 with expert human raters, accompanied by a semantic evaluation accuracy of 84.7%, speech clarity consistency of 87.2%, and speech-to-text accuracy of 91.3%, at a mean LLM response latency of 4.2 seconds. These results collectively confirm that PrepWise AI constitutes a practical, scalable, and pedagogically sound contribution to AI-assisted academic and career preparation.

**Решение:** -4 PrepWise AI study and career assistant for engineering students

---

### 693 · R8811

**Clinical Summaries of Social Media Timelines for Mental Health Monitoring: Human Versus Large Language Model Comparative Evaluation Study (Preprint)**

2025 · JMIR Publications Inc. · posted-content · https://doi.org/10.2196/preprints.71230

BACKGROUND Social media timelines contain rich signals of users’ mental states but are too voluminous for direct clinical review. Although large language models (LLMs) demonstrate robust linguistic and summarization capabilities in general‑purpose tasks, distilling clinically relevant insights demands deeper psychological analysis and sensitivity to each individual’s unique personality and context. Accurately capturing subtle, personalized affective and behavioral patterns remains a significant challenge for current models. A thorough, systematic evaluation of LLM‑generated clinical summaries is therefore essential to understand their readiness for real‑world mental health monitoring. OBJECTIVE This study evaluates the ability of an LLM-based pipeline to generate clinically meaningful summaries of social media timelines, compared to summaries written by human clinicians. The summaries are structured along 3 key clinical aspects, including an overall mental health assessment, intrapersonal and interpersonal patterns, and mental state changes over time. METHODS We use a recent state-of-the-art approach that combines a hierarchical variational autoencoder (VAE) with an LLM (Large Language Model-Meta AI 2 13-billion-parameter version; LLaMA2 13B). This method first summarizes the patient’s history using the VAE and then transforms this summary into a clinical narrative using the LLM. We also test both single-step and multistep LLM-prompting techniques and devise comprehensive clinical prompts. For 30 social media timelines, model outputs were evaluated against human-written summaries through human ratings and expert qualitative analysis. Linguistic diversity was automatically measured as a proxy for personalization. RESULTS Human summaries scored highest for factual consistency (3.75) and general usefulness (3.63). The timeline-hierarchical variational autoencoder (TH-VAE) model outperformed LLaMA for factual consistency (3.35 vs 3.08) and general usefulness (3.28 vs 3.38). Both 2-step models were comparable to humans in describing interpersonal and intrapersonal patterns (3.45-3.48 vs 3.33) and changes over time (3.42 vs 3.35-3.30). The naive LLaMA baseline scored lower on all criteria except factual consistency. Furthermore, a qualitative analysis observed that human summaries provided more accurate, deep, and personalized insights, while LLMs offered more exhaustive but generic descriptions. Quantitatively, linguistic diversity was higher in human summaries both at the semantic level (mean Cohen &lt;i&gt;d&lt;/i&gt;=1.19) and at the surface level (mean Cohen &lt;i&gt;d&lt;/i&gt;=1.31). CONCLUSIONS At this time medium-size LLMs can generate largely accurate and informative clinical summaries of social media timelines, and advanced prompting boosts performance modestly. However, at the time of this writing, they underperform human clinicians in capturing subtle psychological nuances and individual idiosyncrasies. Future work should integrate domain‑specific fine‑tuning and enhanced context modeling to improve LLM clinical fidelity.

**Решение:** -6 clinical summaries of social media timelines generated by LLM vs clinicians without unit coding

---

### 694 · R1931

**Cheap, Consistent, Calibrated, but Biased? Typed Decision Models as Judges**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.18122

Typed decision models (TDMs) return a probability for each allowed answer instead of generating text, which makes them candidates for cheaply replacing LLM judges that compare two answers. Whether they share the biases of LLM judges is untested. We run the CALM benchmark's bias tests on eight TDMs and seven LLM judges of 2024 and 2026. Every TDM is biased, in three to eight of twelve tests. Emotional tone affects them most, and rewriting the better answer in such a tone lowers the accuracy of a typical TDM from 99% to 42%. TDMs are more biased than 2026 LLM judges. All eight change verdicts when the answers swap places, which the 2026 LLM judges hardly do, and several side with an answer that most people allegedly prefer or that a famous model allegedly wrote. Yet both kinds of judge are tripped up by the same prompts. The TDMs' probabilities show that most tests mainly flip verdicts the TDM was unsure of, and that good calibration does not protect against bias. As TDMs are more consistent and 37 times cheaper than 2026 LLM judges, our results suggest they can be attractive judges if their biases are tested for the task.

**Решение:** -6 typed decision models as judges bias benchmark

---

### 695 · R4033

**Preference Learning Unlocks LLMs’ Psycho-Counseling Skills**

2026 · Annual Meeting of the Association for Computational Linguistics · journalarticle, conference, preprint/article · en · https://doi.org/10.18653/v1/2026.findings-acl.521

Applying large language models (LLMs) to assist in psycho-counseling is an emerging and meaningful approach, driven by the significant gap between patient needs and the availability of mental health support. However, current LLMs struggle to consistently provide effective responses to client speeches, largely due to the lack of supervision from high-quality real psycho-counseling data, whose content is typically inaccessible due to client privacy concerns. Furthermore, the quality of therapists' responses in available sessions can vary significantly based on their professional training and experience. Assessing the quality of therapists' responses remains an open challenge. In this work, we address these challenges by first proposing a set of professional and comprehensive principles to evaluate therapists' responses to client speeches. Using these principles, we create a preference dataset, PsychoCounsel-Preference, which contains 36k high-quality preference comparison pairs. This dataset aligns with the preferences of professional psychotherapists, providing a robust foundation for evaluating and improving LLMs in psycho-counseling. Experiments on reward modeling and preference learning demonstrate that PsychoCounsel-Preference is an excellent resource for LLMs to acquire essential skills for responding to clients in a counseling session. Our best-aligned model, PsychoCounsel-Llama3-8B, achieves an impressive win rate of 87% against GPT-4o. We release PsychoCounsel-Preference, PsychoCounsel-Llama3-8B and the reward model PsychoCounsel Llama3-8B-Reward to facilitate the research of psycho-counseling with LLMs at: https://hf.co/Psychotherapy-LLM. ACL 2026 Camera-Ready

**Решение:** -6 preference learning for LLM psycho-counseling chatbot training

---

### 696 · R4815

**Weakly Supervised Learning for Facial Affective Behavior Analysis: A Review**

2026 · IEEE Transactions on Affective Computing · journalarticle, review, preprint/article · en · https://doi.org/10.1109/taffc.2026.3677128

Recent advances in deep learning (DL) and computational capacity have enabled facial affective behavior analysis (FABA) to progress from static images captured in controlled settings to fine-grained analysis of facial expressions in real-world video data. However, training accurate DL models for FABA typically requires large-scale, expert-annotated datasets, which are costly to obtain and inherently noisy due to the ambiguity of labeling subtle facial expressions and action units (AUs). To mitigate these challenges, weakly supervised learning (WSL) has emerged as a promising paradigm for training models with weak annotations. In this paper, we present a structured taxonomy of WSL scenarios for FABA, organized according to the type of weak annotation and the specific affective task. Building on this taxonomy, we provide a critical synthesis of representative WSL methods for both classification (expression and AU recognition) and regression (expression and AU intensity estimation) tasks, focusing on their core methodological ideas, strengths, and limitations. Furthermore, we systematically summarize the comparative performance of WSL approaches along with widely adopted experimental setups and evaluation protocols. Our critical assessment identifies key challenges and future research directions, including the need for efficient adaptation of foundation models and for the development of robust, scalable FABA systems suitable for real-world applications. Provided a link of constantly updated papers \url{https://github.com/praveena2j/ awesome-Weakly-Supervised-Facial-Behavior-Analysis}

**Решение:** -1 review of weakly supervised learning for facial affective behavior analysis

---

### 697 · R5431

**Psychiatrist-Created YouTube Viewing, Parasocial Indicators, and Generative-AI Consultation in Relation to Mental Health Literacy, Symptoms, and Well-Being: A Cross-Sectional Survey of 1,900 Adult Viewers**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6739741

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 cross-sectional survey of psychiatrist YouTube viewing habits

---

### 698 · R11284

**Detecting the Clinical Features of Difficult-to-Treat Depression Using Synthetic Data from Large Language Models**

2024 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.4777347

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T3 detecting clinical features of difficult-to-treat depression; no abstract, eligible on full text

---

### 699 · R6799

**WISP: A Stealthy Word-Level Backdoor Attack via Semantic Influence and LLM-Guided Injection**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-981-92-0375-8_28

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 WISP: word-level backdoor attack in NLP

---

### 700 · R12232

**Revealing the Difficulty in Jailbreak Defense on Language Models for Metaverse**

2024 · Proceedings of the Third International Workshop on Social and Metaverse Computing, Sensing and Networking · book, conference-paper · en · https://doi.org/10.1145/3698387.3699998

Large language models (LLMs) have demonstrated exceptional capabilities in natural language processing tasks, fueling innovations in emerging areas such as the metaverse. These models enable dynamic virtual communities, enhancing user interactions and revolutionizing industries. However, their increasing deployment exposes vulnerabilities to jailbreak attacks, where adversaries can manipulate LLM-driven systems to generate harmful content. While various defense mechanisms have been proposed, their efficacy against diverse jailbreak techniques remains unclear. This paper addresses this gap by evaluating the performance of three popular defense methods (Back-translation, Self-reminder, and Paraphrase) against different jailbreak attack strategies (GCG, BEAST, and Deepinception), while also utilizing three distinct models. Our findings reveal that while defenses are highly effective against optimization-based jailbreak attacks and reduce the attack success rate by 79% on average, they struggle in defending against attacks that alter attack motivations. Additionally, methods relying on self-reminding perform better when integrated with models featuring robust safety guardrails. For instance, Llama2-7b shows a 100% reduction in Attack Success Rate, while Vicuna-7b and Mistral-7b, lacking safety alignment, exhibit a lower average reduction of 65.8%. This study highlights the challenges in developing universal defense solutions for securing LLMs in dynamic environments like the metaverse. Furthermore, our study highlights that the three distinct models utilized demonstrate varying initial defense performance against different jailbreak attack strategies, underscoring the complexity of effectively securing LLMs.

**Решение:** -4 jailbreak defense in language models for metaverse

---

### 701 · R4419

**Integrating Large Language Models into Thematic Analysis Workflows for Healthcare Research.**

2026 · Studies in health technology and informatics · journal article, med, journalarticle · eng · https://doi.org/10.3233/shti260349

Large language models (LLMs) can accelerate the early stages of thematic analysis while preserving rigor. We piloted a lightweight, open-source LLM pipeline on a single semi-structured interview from a mixed-methods case study of Québec's electronic health-record rollout. Manual coders applied a predefined codebook to identify concerns about the deployment; four LLMs (including Hermes 3) performed the same task. Hermes 3 achieved the highest extraction accuracy, identifying 70 concern dimensions of which 54 were valid. Combined human-machine coding yielded 67 unique valid concerns, with the LLM uncovering 11 dimensions missed manually. These results show that LLMs can markedly reduce manual effort and reveal overlooked themes, yet expert validation remains essential. A hybrid workflow, LLM-driven extraction combined with researcher manual coding, is recommended.

**Решение:** -4 thematic analysis of Quebec EHR rollout interview

---

### 702 · R0921

**Simulating the Domain Expert: An Empirical Evaluation of LLM-Based Interview Training for Business Process Modeling**

2026 · Lecture notes in business information processing · conference-paper · en · https://doi.org/10.1007/978-3-032-36710-5_18

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 LLM-based interview training for business process modeling

---

### 703 · R8748

**Abstract P3-03-10: Leverage GPT-4 and social media to understand health disparity for transgender patients with breast and gynecological cancers**

2025 · Clinical Cancer Research · journalarticle, review, conference-abstract · en · https://doi.org/10.1158/1557-3265.sabcs24-p3-03-10

Abstract Objectives: This study focuses on the often-understudied experiences of transgender individuals, specifically those assigned female at birth, navigating breast and gynecological cancer care. Leveraging social media and advanced AI (GPT-4), we explored their healthcare journeys, coping mechanisms, challenges, and the broader impact of their diagnoses. Methods: User-generated discussions from major social media platforms (Reddit, X, YouTube) were collected, spanning 2012 to 2022. A combination of systematic searches, rule-based filters, and AI (GPT-4) was used to extract narratives specific to transgender patients. Pre-established themes were identified through manual analysis and literature review. Two independent researchers coded a subset of the data to ensure reliability, achieving substantial agreement (Cohen’s kappa κ = 0.93). GPT-4 was then utilized to categorize these posts into distinct stages of the patient journey and the pre-established main themes. Emergent subthemes and perspectives identified by GPT-4 were manually validated. Results: From over 30 million posts on social media, 1,235 were eligible for inclusion. The analyzed posts were distributed across various cancer indications: breast cancer (30.4%), cervical cancer (25.9%), endometrial cancer (34%), and ovarian cancer (9.7%). Three primary themes emerged: lack of awareness, access issues, and clinical challenges. Posts about clinical concerns focused on the burden of disease (87.1%), with emphasis on physical health. A concerning lack of healthcare system and provider awareness of transgender cancer needs was highlighted in 65.7% of posts, with 16.5% expressing concerns about incorrect pronoun use. Nearly one-third of posts addressed financial issues (health insurance coverage limitations), while 71.9% addressed non-financial access issues, including concerns about trans-competent healthcare providers. Conclusion: By utilizing social media data and AI, we captured experiences and disparities in breast and gynecological care faced by transgender individuals. Findings underscore the need for increased provider awareness, improved healthcare access, and inclusive clinical practices. Addressing these disparities and advocating for more equitable and empathetic cancer care is crucial, regardless of gender identity. Citation Format: Kathryn Mishkin. Leverage GPT-4 and social media to understand health disparity for transgender patients with breast and gynecological cancers [abstract]. In: Proceedings of the San Antonio Breast Cancer Symposium 2024; 2024 Dec 10-13; San Antonio, TX. Philadelphia (PA): AACR; Clin Cancer Res 2025;31(12 Suppl):Abstract nr P3-03-10.

**Решение:** -4 social media analysis of transgender breast and gynecological cancer patients

---

### 704 · R1859

**Evaluating ChatGPT's Role in Patient Education on Distraction Osteogenesis for Limb Lengthening.**

2026 · Cureus · journal article, journalarticle, review · eng · https://doi.org/10.7759/cureus.114235

BACKGROUND: Limb lengthening requires patients to understand a complex procedure, a prolonged recovery, and potential complications. This study evaluated the quality, reliability, readability, and clinical completeness of ChatGPT-3.5 (OpenAI, San Francisco, CA) responses to common patient questions about limb lengthening. METHODOLOGY: In this descriptive, cross-sectional content analysis, a purposive sample of 10 commonly encountered and clinically relevant questions was identified from the frequently asked questions pages of 10 healthcare institutions. Each question was entered separately into ChatGPT-3.5 on January 18, 2024, without follow-up prompts. Two senior authors independently evaluated each response against published literature and scored it with the Quality Criteria for Consumer Health Information (DISCERN) instrument, Journal of the American Medical Association (JAMA) benchmark criteria, and Flesch-Kincaid grade level. Outcomes were summarized descriptively, and interrater agreement was assessed with the Cohen kappa coefficient. RESULTS: The mean DISCERN score was 35.5 (range: 21-42). One response was rated very poor, seven were rated poor, and two were rated fair. Every response received a JAMA benchmark score of 0. The mean Flesch-Kincaid grade level was 13.6 (range: 12.3-15.7), indicating postsecondary reading demand. CONCLUSIONS: ChatGPT-3.5 provided broad introductory information, but most responses lacked transparent sources, required clinical clarification, and were too complex for general patient education. It may be useful as a clinician-reviewed adjunct but should not replace individualized counseling by a qualified healthcare professional.

**Решение:** -4 patient education on distraction osteogenesis for limb lengthening

---

### 705 · R3803

**How Undergraduate and Graduate Students Self-Regulate GenAI Use in Project-Based Learning: Choosing, Creating, Filtering, and Stopping Strategies**

2026 · Journal of Educational Computing Research · journalarticle, article · en · https://doi.org/10.1177/07356331261469412

Generative AI (GenAI) is now common in university project work, yet previous studies often examine students’ trust, creativity, overload, or engagement separately. This leaves a key gap: how students regulate GenAI across a full project workflow. This exploratory study addresses that gap by examining a four-process “ AI-mediated Self-Regulated Learning ” ( AI-SRL ) cycle: (1) evaluating and selecting GenAI suggestions, (2) experiencing shifts in creative agency, (3) managing overload through filtering and summarizing, and (4) monitoring time and energy to stop or continue working with GenAI. We conducted a two-course basic qualitative design study with 97 undergraduate and graduate students. Data came from an open-ended questionnaire aligned to the four processes. We used inductive content analysis with a shared codebook, reliability checks, and cross-level comparisons. Findings show that students use combinations of strategies across the AI-SRL cycle. They exercise agency through goal alignment, revision, and verification, with graduates reporting stronger cross-checking and source-based justification. Creativity was described as a conditional outcome: it increased when GenAI widened ideas but declined when it replaced personal exploration. Overload was managed through targeted prompts and structured outputs, again more common among graduates. Most students did not lose track of time; they used clear stopping cues such as fatigue, repetition, or satisfaction. Together, results reveal two distinct metacognitive regulation styles: “ Exploratory-Simplification ” and “ Systematic-Methodical ”.

**Решение:** -4 student self-regulation of GenAI in project-based learning

---

### 706 · R12346

**Exploring the Use of Artificial Intelligence for Qualitative Data Analysis: The Case of ChatGPT**

2023 · International Journal of Qualitative Methods · journalarticle, article · en · https://doi.org/10.1177/16094069231211248

The potential use of artificial intelligence programs such as a ChatGPT to analyze qualitative data raises any number of questions, most notably whether it is possible to produce similar results without the demanding process of manual coding. In addition, there are questions about both the simplicity of using ChatGPT for qualitative data analysis and the potential time savings that it might provide This article addresses these questions by using ChatGPT to reinvestigate two qualitative datasets that were previously analyzed by more traditional methods. In particular, it examines the extent to which the responses from ChatGPT can recreate the themes that were originally chosen to summarize the two previous analyses. The results show that ChatGPT performed reasonably well, but in both cases it was less successful at locating subtle, interpretive themes, and more successful at reproducing concrete, descriptive themes. In doing so, the program was quite easy to use and required very little effort in comparison to approaches that rely on manual coding. It is important to recognize, however, that both coding and approaches based on artificial intelligence are simply tools that must be applied within a larger analytic process. Overall, this exploration suggests that artificial intelligence may well have the power to disrupt the coding of data segments as a dominant paradigm for qualitative data analysis.

**Решение:** -6 inductive theme extraction without segment-level coding or agreement metrics

---

### 707 · R4274

**Tackling Ransomware with Generative AI: Ethical Resilience and Adaptive Defense Mechanisms**

2026 · Texts in computer science · book-chapter · en · https://doi.org/10.1007/978-3-032-25874-8_15

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 tackling ransomware with generative AI

---

### 708 · R8231

**Exploring Inductive and Deductive Qualitative Coding with AI: Investigating Inter-Rater Reliability between Large Language Model and Human Coders**

2025 · AHFE international · conference-paper, proceedings-article · en · https://doi.org/10.54941/ahfe1006232

Qualitative research provides valuable insights into complex human phenomena, but its coding processes are often time-intensive and labor-intensive. The advent of Large Language Models (LLMs) has introduced new opportunities to streamline qualitative analysis. This study investigates the application of LLMs in both inductive and deductive coding tasks using real-world datasets, assessing their ability to complement traditional coding methods. To address challenges such as privacy concerns, prompt customization, and integration with qualitative workflows, we developed QualiGPT, an API-based tool that facilitates efficient and secure qualitative coding. Our evaluation shows that the consistency level between AI-generated codes and human coders is acceptable, particularly for inductive coding tasks where themes are identified without prior frameworks. In our case study using data from a Discord community, GPT-4 achieved a Cohen's Kappa of 0.57 in inductive coding, demonstrating moderate agreement with human coders. For deductive coding, the inter-rater reliability between human coders and GPT-4 reached a Fleiss' Kappa of 0.46, indicating a promising level of consistency when applying pre-established codebooks. These findings highlight the potential of LLMs to augment qualitative research by improving efficiency and consistency while maintaining the contextual depth that human researchers provide. We also observed that LLMs demonstrated higher internal consistency compared to human coders when using a codebook for deductive coding, suggesting their value in standardizing coding approaches. Additionally, we explored a novel paradigm where LLMs function not merely as coding tools but as collaborative co-researchers that independently analyze data alongside humans. This approach leverages LLMs' strengths in generating high-quality themes and providing genuine content references, thereby enriching researchers' insights while maintaining human oversight to ensure contextual understanding and ethical standards. Nevertheless, challenges remain regarding prompt engineering, domain-specific training, and the risk of fabricated information, underscoring the importance of human validation in the final analysis. This research advances human-AI collaboration in qualitative methods by exploring AI-assisted coding and highlighting future improvements in interaction design.

**Решение:** ? T1 inductive and deductive qualitative coding of Discord community data: GPT-4 vs humans (kappa 0.46-0.57); check construct eligibility

---

### 709 · R10881

**Hope ‘The Paragraph Guy’ explains the rest : Introducing MeSum, the Meme Summarizer**

2024 · Underline Science Inc. · audiovisual/conference talk, conference-paper · en · https://doi.org/10.18653/v1/2024.findings-emnlp.389

Over the years, memes have evolved into multifaceted narratives on platforms like Instagram, TikTok, and Reddit, blending text, images and audio to amplify humor and engagement. The objective of the task described in this article is to bridge the gap for individuals who may struggle to understand memes due to cultural, geographical, ancillary insights, or relevant exposure constraints, aiming to enhance meme comprehension across diverse audiences. The lack of large datasets for supervised learning and alternatives to resource-intensive vision language models have historically hindered the development of such technology. In this work, we have made strides to overcome these challenges. We introduce "MMD" a $\textbf{M}$ultimodal $\textbf{M}$eme $\textbf{D}$ataset comprising $\textbf{13,494}$ instances, including 3,134 with audio, rendering it the largest of its kind, with $\textbf{2.1}$ times as many samples and $\textbf{9.5}$ times as many words in the human annotated meme summary compared to the largest available meme captioning dataset, MemeCap. Our framework, MeSum ($\textbf{Me}$me $\textbf{Sum}$mariser), employs a fusion of Vision Transformer and Large Language Model technologies, providing an efficient alternative to resource-intensive Vision Language Models pioneering the integration of all three modalities, we attain a ROUGE-L score of 0.439, outperforming existing approaches such as zero-shot Gemini, GPT4 Vision, LLaVA and QwenVL which yield scores of 0.259, 0.213, 0.177 and 0.198. We have made our codes and datasets publicly available.

**Решение:** -4 MeSum: meme summarizer

---

### 710 · R4585

**Circuit Discovery Helps Detect LLM Jailbreaking: A Mechanistic Interpretability Study**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.27504

Despite extensive safety alignment, large language models (LLMs) remain vulnerable to jailbreak attacks that bypass safeguards to elicit harmful content. While prior work attributes this vulnerability to safety training limitations, the internal mechanisms by which LLMs process adversarial prompts remain poorly understood. We present a mechanistic analysis of the jailbreaking behavior in a large-scale, safety-aligned LLM, focusing on LLaMA-2-7B-chat-hf. Leveraging edge attribution patching and subnetwork probing, we systematically identify computational circuits responsible for generating affirmative responses to jailbreak prompts. Ablating these circuits during the first token prediction can reduce attack success rates by up to 80\%, demonstrating its critical role in safety bypass. Our analysis uncovers key attention heads and MLP pathways that mediate adversarial prompt exploitation, revealing how important tokens propagate through these components to override safety constraints. These findings advance the understanding of adversarial vulnerabilities in aligned LLMs and pave the way for targeted, interpretable defense mechanisms based on mechanistic interpretability. Accepted at the 2nd Workshop on Reliable and Responsible Foundation Models of the 42nd International Conference on Machine Learning (ICML) 2025

**Решение:** -4 circuit discovery in LLM jailbreaking

---

### 711 · R2301

**DialogGuard: Multi-Agent Psychosocial Safety Evaluation Interface of Sensitive LLM Responses**

2026 · Annual Meeting of the Association for Computational Linguistics (ACL) · conference-paper · https://doi.org/10.18653/v1/2026.acl-demo.19

LLM-based agents are increasingly deployed for mental-health support and crisis counselling, yet recent evaluations reveal that commercial therapy chatbots respond appropriately only about half the time in clinical scenarios.Clinicians and safety engineers are called upon to audit these systems, but existing tools do not surface the subtler psychosocial harms (manipulation, discrimination, psychological distress) nor produce the explainable rationales that practitioners need.We present Dialog-Guard, an open-source system that lets practitioners inspect, stress-test, and create audit trails for prompted LLM agents across five psychosocial safety dimensions.The system wraps around arbitrary generative models through four LLM-as-a-judge pipelines (single-agent scoring, dual-agent correction, multi-agent debate, and majority voting), each grounded in shared three-level rubrics.Through its web interface, practitioners evaluate agents in two modes (Live Chat and Manual Input) and review per-dimension risk scores with naturallanguage rationales.Experiments on PKU-SafeRLHF show that dual-agent correction provides the best accuracy-robustness trade-off, and a formative study with 12 practitioners confirms that the system supports prompt auditing, safety inspection, and supervisory decisionmaking.Code and demo

**Решение:** -6 DialogGuard: software interface demonstration for LLM psychosocial safety auditing

---

### 712 · R6263

**Towards Affective Evaluation of STEM Education: Leveraging MLLMs in Project-Based Learning**

2026 · IEEE Transactions on Affective Computing · article · en · https://doi.org/10.1109/taffc.2026.3656971

Project-Based Learning (PBL) involves a variety of highly correlated multimodal data, making it a vital educational approach within STEM disciplines. With the rapid development of multimodal large language models (MLLMs), researchers have begun exploring their potential to enhance tasks such as information retrieval, knowledge comprehension, and data generation in educational settings. However, existing benchmarks lack both a flexible free-form output structure and rigorous human expert validation, resulting in limited affective engagement and insufficient capacity to evaluate real-world educational tasks. Additionally, few methods have developed automated pipelines to assist with the complex responsibilities of teachers leveraging MLLMs, largely due to model hallucination and instability, which further limit their affective responsiveness and result in unreliable implementation. To address this gap, we introduce Affective-PBLBench, an affect-informed benchmark designed to evaluate complex reasoning grounded in domain-specific knowledge and long-context understanding, thereby challenging models with tasks that closely resemble those handled by human experts. Recognizing that affective framing is pivotal for holistic student assessment, Affective-PBLBench specifically includes a branch for evaluating students' affective states, facilitating the monitoring and preliminary screening of students' mental health conditions. We also build a new dataset, PBL-STEM, for this complex scenario, which contains over 500 projects with different modalities and multi-disciplinary contexts. To establish reliable ground truth, we adopt the Analytic Hierarchy Process (AHP), utilizing expert-driven pairwise comparisons to derive structured and weighted evaluation criteria. We assess the performance of 15 leading MLLMs/LLMs using Affective-PBLBench and demonstrate that even the most advanced models achieve only 59% rank accuracy, underscoring the significant challenges presented by this benchmark. We believe Affective-PBLBench will serve as a catalyst for the development of more capable AI agents, ultimately aiming to alleviate teacher workload and facilitating a holistic understanding of students' mental health.

**Решение:** -4 multimodal affective evaluation in STEM project-based learning

---

### 713 · R5815

**Public repository of the study "Out of Place in My Own Work: How Generative AI Displaces Software Engineers"**

2026 · Figshare · other/online resource, other · https://doi.org/10.6084/m9.figshare.31803529

Out of Place in My Own Work: How Generative AI Displaces Software Engineers This repository contains the research materials associated with the study: " Out of Place in My Own Work: How Generative AI Displaces Software Engineers" The repository is provided to support transparency and open science practices. Repository Contents The repository includes the following files: Interview Protocol (File: AI-induced displacement - Interview protocol.pdf): Contains the semi-structured interview protocol used during data collection. Codebook (File: Codebook - AI-induced_displacement.pdf): Contains the final coding scheme developed during thematic analysis, including themes, codes, and their frequencies and descriptions. Coding Process Examples (File: Coding_process_examples.xlsx): Provides examples from the qualitative coding process, illustrating how raw excerpts were assigned to codes. Study Description: This study investigates how the adoption of Generative AI tools affects software engineers’ work practices, roles, and professional identity, with a particular focus on experiences of displacement, changing expectations, and shifts in collaboration. The materials in this repository document the qualitative data collection and analysis process used in the study. Material purpose and use: The files are provided to:Document the research procedureIncrease transparency of qualitative analysisAllow other researchers to understand the coding processSupport extension studiesNo personal or identifiable participant data are included. Data is anonymized in accordance with ethics approval. Contact: For questions regarding the repository or the study, please contact:Theocharis TavantzisAalborg Universitythta@cs.aau.dk

**Решение:** -4 public repository on generative AI displacing software engineers

---

### 714 · R3694

**Generative AI Models for Mental Health Diagnosis and Therapy**

2026 · other · en · https://doi.org/10.1002/9781394336760.ch31

Generative artificial intelligence (AI) models are transforming mental health applications by having the capability to perform sophisticated data augmentation, automated diagnosis, and AI-augmented therapy. This paper compares the performance of three generative deep learning architectures—generative adversarial networks (GANs), variational autoencoders (VAEs), and transformer-based architectures—on mental health tasks. We train and preprocess these models on a big dataset of clinical history, patient symptoms, therapy session transcripts, and electroencephalographic imaging data to produce synthetic data, learn latent representations, and simulate therapy conversations. GANs have the best diagnostic accuracy (85.3%) and create high-quality synthetic data, as shown by a low Fréchet inception distance score of 27.4. VAEs are good learners of latent patterns but fall behind in synthetic data fidelity. Transformer-based models perform well in therapy session simulation with 87.5% coherence of patient response, making them well-suited for chatbot-assisted mental health interventions. The findings envision the potential of generative AI to improve mental health interventions and indicate future research directions in hybrid systems to reach optimal diagnostic accuracy and therapeutic coherence.

**Решение:** -6 comparative analysis of GAN, VAE, and Transformer architectures in mental health

---

### 715 · R3130

**Can LLMs Reliably Predict Personality Traits Through Prompt Engineering? Introducing Expert-Chain-Hypothesis Prompting**

2026 · Lecture notes in networks and systems · conference-paper · en · https://doi.org/10.1007/978-3-032-22911-3_7

The prediction of personality traits from natural language is a long-standing challenge at the intersection of artificial intelligence and psychology. Traditional approaches have largely relied on handcrafted features, custom labelled datasets, supervised learning models or pretrained embeddings. However, relatively fewer studies have explored the potential of large language models (LLMs) through prompt engineering. This study investigates the capability of LLMs to reliably predict the Big Five personality traits from unstructured textual input using prompt-based methods. We introduce Expert-Chain-Hypothesis prompting, a psychology informed prompting technique that mirrors the decision making workflow of human experts within LLMs. Using the Essays dataset, we evaluate zero-shot prompting, few-shot prompting, chain-of-thought prompting and the proposed method on GPT - 4o. Experimental results demonstrate that the proposed prompting technique achieves superior overall performance; with a macro F1 score of 0.759, micro F1 score of 0.750 and the lowest reported hamming loss of 0.280. Our findings suggest that while prompt engineering techniques hold significant promise for personality prediction, challenges remain in fully capturing the subtleties of all personality traits.

**Решение:** ? T2/T1 Big Five personality prediction from Essays dataset with GPT-4o; check ground truth (self-report vs rater)

---

### 716 · R2917

**LLM-Augmented Computational Phenotyping of Long Covid**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2603.18115

Phenotypic characterization is essential for understanding heterogeneity in chronic diseases and for guiding personalized interventions. Long COVID, a complex and persistent condition, yet its clinical subphenotypes remain poorly understood. In this work, we propose an LLM-augmented computational phenotyping framework ``Grace Cycle'' that iteratively integrates hypothesis generation, evidence extraction, and feature refinement to discover clinically meaningful subgroups from longitudinal patient data. The framework identifies three distinct clinical phenotypes, Protected, Responder, and Refractory, based on 13,511 Long Covid participants. These phenotypes exhibit pronounced separation in peak symptom severity, baseline disease burden, and longitudinal dose-response patterns, with strong statistical support across multiple independent dimensions. This study illustrates how large language models can be integrated into a principled, statistically grounded pipeline for phenotypic screening from complex longitudinal data. Note that the proposed framework is disease-agnostic and offers a general approach for discovering clinically interpretable subphenotypes.

**Решение:** -4 computational phenotyping of Long COVID subgroups

---

### 717 · R2473

**Multilayer Cipher Architecture in Fontana's Secretum and Bellicorum: A Twenty-Lens Template Return with Negative-Control Differential**

2026 · Zenodo · text/working paper · https://doi.org/10.5281/zenodo.22671994

Giovanni Fontana (Venice, c.1395 - c.1455; Padua medical doctorate 1421) produced two surviving cipher-bearing manuscripts: the Bellicorum instrumentorum liber (Munich, Bayerische Staatsbibliothek, Cod.icon. 242) and the Secretum de thesauro experimentorum imaginationis hominum (Paris, Bibliotheque nationale de France, NAL 635). A third Fontana witness, the autograph-candidate De trigono balistario in Bodleian Canon Misc 47, is plain Latin with embedded astronomical and trigonometric apparatus. Battisti and Battisti (1984) decoded the substitution layer of the cipher works (single-character substitution with a stable key inventory). The present paper reports a 2026-05-11 template-return outcome applying a twenty-lens analytical instrument across all three Fontana witnesses, and the 2026-06-11 negative-control run that applies the same template, under the same per-lens rubric (Appendix A, pre-registered relative to the 2026-06-11 negative-control run and applied retrospectively to the Fontana 2026-05-11 audit notes; see Section 2.1 temporal-order note), to three contemporaneous Padua-corridor non-Fontana witnesses: BSB Cgm 7958 (Hartlieb, Bavaria 1456), the Hartlieb Kraeuterbuch nine-witness corpus, and the Cermisone Consilia (1441 print closure). The Fontana 3-witness result is seven SIGNAL lenses for NAL 635, seven SIGNAL lenses for the Bellicorum, and eight SIGNAL lenses for the Bodleian witness against an internal return threshold of five SIGNAL lenses across two or more works; the Fontana counts are reported as Candidate-tier rescores pending blinded inter-rater re-scoring. The negative-control 3-witness result is three SIGNAL lenses for Cgm 7958, two SIGNAL lenses for the Hartlieb Kraeuterbuch corpus, and two SIGNAL lenses for the Cermisone Consilia. The differential, Fontana mean 7.3 SIGNAL lenses against negative-control mean 2.3 SIGNAL lenses, ratio 3.17x, is a tentative discriminating signal pending category-matched controls (cipher-bearing and engineering-codex Quattrocento witnesses); on the present three controls the template is not behaving as a generic Quattrocento-codex detector. The single-substitution decode of Battisti 1984 corresponds to lens five (cipher engineering); on the per-lens bibliographic-coverage audit (Appendix B), the surveyed Fontana literature offers no engagement on lenses one (iconographic), three (user instruction), six (layout geometry), seven (cross-folio motif mapping), eleven (balneological flow), twelve (paleographic hands), thirteen (scribe workflow), seventeen (recipe indexing), and nineteen (myth-to-math) as a structural set. A structural-parallel-development line (fourteenth-century Italian computus through the Padua-orbit medical-and-instrument cohort c.1410-1470 to Fontana's c.1430s cipher specialisation, structurally parallel to Trithemius 1518 and Vigenere 1586) is described in Section 3 as a contemporaneous-network reading anchored on Padua institutional density, not as a sequential lineage with documented hand-to-hand transmission. The pre-Tepenecz frontier of Voynich Manuscript provenance is the documented March 1599 Augsburg Hofkammer transaction; the competing pre-Rudolfine Hartlieb-Anna-Nannhofen-Elsenheimer chain attributed in a 2024 paper is substantially undermined on documented archival grounds. Comparator discipline (Section 5): the Voynich Manuscript is an independent point of investigation that sits inside the same chronological-and-architectural envelope as Fontana, not a numbered stage in the parallel sequence. Substrate-origination anchor: substrate-resident research at Honeycutt Ai Labs (Princeton TX) on the Voynich Manuscript and adjacent Quattrocento corpora traces to an August 2025 methodology pass; the surviving public-record VMS priority anchor on the substrate side is the Paduan Medical Reference dataset (Zenodo DOI 10.5281/zenodo.18687530, CC-BY-4.0, copyright origination 2025-08-27). The internal twenty-lens analytical template carries copyright stamp 2025-09-06. The Voynich-Fontana Forensic MasterBundle (2025-09-17) is the independent pre-template forensic-comparison anchor for the Section 5.4 fountain-rosette comparator. This deposit (v_real_1) applies the 2026-06-11 referee micro-edits to the FINAL packet: Section 2.1 temporal-order note (rubric-after-scoring); Section 2.6 softens 'discriminating instrument' to 'tentative discriminating signal pending category-matched controls'; Section 3.1 uses named stages (not numbered) to avoid sequence-implication; Section 4.1 separates three sub-claims at distinct confidence levels (1599 transaction HIGH; VMS-inclusion MODERATE inferential; Rauwolf-source MODERATE inferential); Section 4.3 replaces 'demolished' with 'substantially undermined'; Section 5.2 scopes 'only known' to 'only currently substrate-attested' with explicit falsifier; Section 5.4 bounds the fountain-rosette comparator to the cipher-bearing subset. Companion HAIL working papers: P-004 (DOI 10.5281/zenodo.20392093), P-005 (DOI 10.5281/zenodo.20391953), P-007 (DOI 10.5281/zenodo.20392112), P-009 (DOI 10.5281/zenodo.20391967), P-011 (DOI 10.5281/zenodo.20391969), P-012 (DOI 10.5281/zenodo.20391970), P-015 (DOI 10.5281/zenodo.20391982). Corpus note. This record belongs to the Honeycutt Ai Labs research program initiated August 2025, documented across the deposited paper set, heardtogether.org, and the underlying conversation corpus. Artifacts retained with this program — including build manifests and pipeline byproducts — are kept as primary data under an all-data-matters transparency policy; several are captured field specimens of the large-language-model output patterns catalogued in the companion record The Ghost Pattern Codebook: A Public-Surface Taxonomy of LLM Output Patterns (DOI 10.5281/zenodo.20391960). The lab studies these patterns and does not exempt its own toolchain from them. Corrected version deposited 2026-09-09. The section "Corrections in this version" in the paper states what changed a

**Решение:** -4 cipher architecture in Giovanni Fontana historical manuscripts

---

### 718 · R7391

**Chain of Strategy Optimization Makes Large Language Models Better Emotional Supporter**

2025 · Underline Science Inc. · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48448/390r-s165

The growing emotional stress in modern society has increased the demand for Emotional Support Conversations (ESC). While Large Language Models (LLMs) show promise for ESC, they face two key challenges: (1) low strategy selection accuracy, and (2) preference bias, limiting their adaptability to emotional needs of users. Existing supervised fine-tuning (SFT) struggles to address these issues, as it rigidly trains models on single gold-standard responses without modeling nuanced strategy trade-offs. To overcome these limitations, we propose Chain-of-Strategy Optimization (CSO), a novel approach that optimizes strategy selection preferences at each dialogue turn. We first leverage Monte Carlo Tree Search to construct ESC-Pro, a high-quality preference dataset with turn-level strategy-response pairs. Training on ESC-Pro with CSO improves both strategy accuracy and bias mitigation, enabling LLMs to generate more empathetic and contextually appropriate responses. Experiments on LLaMA-3.1-8B, Gemma-2-9B, and Qwen2.5-7B demonstrate that CSO outperforms standard SFT, highlighting the efficacy of fine-grained, turn-level preference modeling in ESC. 21 pages, 9 figures, 17 tables

**Решение:** -6 chain of strategy optimization for emotional support conversation generation

---

### 719 · R9210

**The Glass Wall**

2025 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.19010684

Title: The Glass Wall Michał Nowak Description: This paper investigates whether the safety behavior of large language models (LLMs) is invariant under intent-preserving narrative transformations that add authority, urgency, and institutional framing. We introduce CALI-50, a paired benchmark of 50 dual-use technical scenarios spanning industrial control, medical, defense, financial, and cybersecurity domains. Each scenario contains a direct baseline prompt and an authority-escalated variant that holds the requested action constant while adding structured deception through false context seeding, authority establishment, recursive style escalation, and emergency framing. Five state-of-the-art models (GPT-4 Turbo, Gemini 3 Flash, DeepSeek-V3, and AllenAI) are evaluated under identical conditions using a 1–5 Likert safety rubric scored by an automated judge. The central metric, Authority-Induced Breach Rate (AIBR-4), measures the fraction of scenarios where a safe baseline refusal flips to actionable unsafe compliance solely due to narrative reframing. Key findings: (1) All models exhibit statistically significant safety degradation under authority framing (Wilcoxon p < 0.05 for four of five models), with AIBR-4 ranging from 14.0% (GPT-4 Turbo) to 51.0% (DeepSeek-V3). (2) Response distributions are bimodal — models either refuse fully or comply fully, with minimal graduated response. (3) The effect is not monotonic: 10.9% of observations show improved safety under authority framing, indicating bidirectional sensitivity. (4) Dual-run stability analysis reveals reproducible aggregate vulnerability but high scenario-level stochasticity. (5) A novel methodological artifact is identified: judge safety refusal, where the evaluating model's own safety policies prevent it from scoring the most dangerous attack responses, causing standard benchmarks to systematically undercount the most severe breaches. The paper argues that current alignment creates a "Glass Wall" — robust against naive attacks but selectively transparent to authority-mimicking adversaries — and proposes deterministic Invariant Logic Checks as a necessary complement to probabilistic safety training. I hypothesize that authority-framed safety degradation may be one instance of a broader failure mode I call Local Signal Dominance. In this regime, locally salient contextual cues — authority, tone, format, urgency — exert disproportionate influence over model behavior relative to global constraints such as safety policies, factual consistency, or instruction-priority stability. One plausible source is alignment via compressed preference proxies, where training objectives aggregate safety, helpfulness, and contextual fit into a limited reward signal that may overreward local coherence without reliably preserving cross-context invariants. Interestingly, evidence from CALI suggests the effect is heterogeneous and bidirectional: authority framing degrades safety in some tasks while triggering stronger refusal in others. Keywords: LLM safety, adversarial robustness, prompt framing, authority bias, sycophancy, red-teaming, benchmark, RLHF, critical infrastructure, cyber-physical systems, LLM-as-judge, mixture-of-experts License: CC BY 4.0

**Решение:** -4 The Glass Wall: LLM safety under narrative transformations

---

### 720 · R3351

**Using a Large Language Model to Extract Information from Student Submitted Free-Text Feedback.**

2026 · Medical science educator · journal article, med, journalarticle · eng · https://doi.org/10.1007/s40670-025-02615-1

Student feedback is essential to curriculum evaluation. While methods for analyzing quantitative feedback data are readily available and easy to implement, methods for analyzing text-based, qualitative feedback data are less widely available, requiring more time, effort, and expertise. And yet, students' responses to open-ended questions hold great value for curriculum refinement because narrative comments can identify un-anticipated areas of concern that closed-ended rating scales might miss and often provide specific suggestions for improvement. In this paper, we describe efforts to analyze the feasibility and accuracy of using a Large Language Model (ChatGPT 4o) to analyze medical student comments in response to a question asking them to identify basic science topics they found challenging. ChatGPT 4o was used to categorize and summarize students' identification of and explanations for these challenging topics. We describe the specific prompts used to generate and refine results and then conducted a series of experiments to explore consistency, accuracy, and meaningfulness: (1) reviewing the consistency of 10 replications of the ChatGPT 4o request; (2) comparing "expert" human ratings of topic categories with ChatGPT's categorization; and (3) comparing "expert" human analyses of the explanations for a challenging topic with those generated by ChatGPT. Overall, we found the LLM output to be useful, fairly closely aligned with human experts, and easy to implement. However, results were not perfectly replicated across multiple trials and we found some differences between human and LLM analyses. Our use case is well suited to the current capabilities of genAI models in that summaries can be rapidly and easily generated with sufficient (but not perfect) consistency and accuracy to support continuous quality improvement of basic science curriculum. Supplementary information The online version contains supplementary material available at 10.1007/s40670-025-02615-1.

**Решение:** -4 LLM extracting qualitative feedback from student course evaluations

---

### 721 · R10201

**Automated Scoring of Question Complexity with Transformer Language Models**

2025 · Thinking Skills and Creativity · article · en · https://doi.org/10.1016/j.tsc.2025.102090

• Introduces two automated transformer models for assessing cognitive question complexity: high-performing LLaMA 2 and efficient, robust RoBERTa. • These fine-tuned transformer language models greatly outperform surface-based and semantic-distance baselines. • Both models predict open-ended question complexity and align strongly with human ratings. • Introduces PrediQT , a free web app for automated question-complexity scoring. • Bridges creativity, cognition, and AI for educational assessment innovation. Question-asking, an essential yet understudied activity, holds significant implications for learning, creativity, and cognitive development. Research shows that asking complex, open-ended questions is better for learning than closed ones. Previous research has explored open-ended question complexity through Bloom’s taxonomy, but the measurement of complexity remains challenging. Recent advancements in natural language processing have enabled automated scoring of psychological tasks aligned to human-ratings. However, automatic assessment of open-ended questions remains understudied. We address this gap by fine-tuning transformer language models to predict human ratings of open-ended question complexity and comparing them to existing baseline measures (i.e., word count and semantic distance). Using previously collected human-rated responses and Bloom ratings from a creative question-asking task, we trained an encoder model (RoBERTa) and a Large Language Model (Llama-2-7B). Our results reveal that RoBERTa correlated strongly with human ratings of complexity (r = .73), exceeding baseline measures and offering an efficient, lightweight solution suitable for broad adoption. Our fine-tuned LLaMA 2 model achieved stronger performance (r = .84), establishing a new benchmark for predictive accuracy. Thus, we demonstrate how language models can be utilized to automatically score the complexity of open-ended questions. Importantly, LLaMA 2 demonstrates higher accuracy, while RoBERTa provides a replicable, accessible, and cost-effective option for everyday educational and psychological applications. Our work paves the way for automatic assessment of open-ended questions, which are critical across a wide range of cognitive domains.

**Решение:** ? T2 automated scoring of cognitive question complexity (Bloom taxonomy) using LLaMA-2 vs human ratings (r=0.84); check construct eligibility

---

### 722 · R5311

**Learning From the Use of Generative AI in Fourth-Year Psychiatry Teaching at Aston Medical School**

2026 · BJPsych Open · journalarticle, review, article · en · https://doi.org/10.1192/bjo.2026.11352

Aims: Undergraduate psychiatry education is frequently limited by variable clinical exposure, ethical constraints in involving acutely unwell patients, and restricted opportunitiesfor students to practise high-stakes consultations. Generative artificial intelligence (AI) simulation platforms offer a potential solution by enabling students to rehearse clinical encounters in a structured and safe environment. This poster aims to present lessons learned from the implementation of generative AI-supported simulations for fourth-year medical students at Aston Medical School. Specifically, it explores how students and tutors experienced the integration of AI-facilitated consultations into the curriculum and identifies factors that influenced engagement, learning value, and trust in assessment. Methods: A mixed-methods educational evaluation was conducted following the introduction of AI-based consultation simulations within the fourth-year psychiatry programme. Feedback was gathered through anonymised student questionnaires, facilitated debrief sessions after simulation use, and structured discussions with clinical tutors involved in teaching and assessment. Data focused on students’ perceived learning value, alignment with clinical placements, clarity of feedback and marking criteria, and overall usability of the platform. Tutor reflections on feasibility, integration with existing teaching, and impact on small-group learning were also collected. Qualitative themes were identified through thematic review of student and tutor comments. Results: Students generally recognised the potential value of generative AI simulation as a safe environment to practise structured consultations, particularly for OSCE preparation and rehearsal of high-risk scenarios such as suicide risk assessment and capacity evaluations. Many reported that the tool was most effective when used after formal teaching or placement exposure, supporting consolidation and revision. However, engagement was reduced when simulations were used as a first exposure to unfamiliar clinical material or were misaligned with placement timing. Some students expressed uncertainty about AI-generated markingcriteria and pass thresholds, noting that checklist-based feedback could sometimes feel disconnected from authentic clinical reasoning. Mandatory debrief sessions were valued when they facilitated reflection and discussion but were perceived as less helpful when they repeated automated feedback. Tutors highlighted the importance of clear learning objectives, integration with small-group teaching, and transparency around assessment processes. Conclusion: Generative AI simulation can enhance undergraduate psychiatry education by providing scalable opportunities for structured practice and feedback. Its effectiveness depends on thoughtful curriculum integration, alignment with clinical teaching, and clarity around assessment and feedback. Student and tutor perspectives suggest that AI is most beneficial when used to augment, rather than replace, traditional teaching and reflective debriefing. These lessons offer practical insights for educators seeking to incorporate generative AI into medical education in a pedagogically meaningful and learner-centred way.

**Решение:** -4 generative AI simulation in undergraduate psychiatry education

---

### 723 · R7707

**Exploring GenAI as Evaluative and Formative Assessment Tools in Reading Assessment: A Mixed-methods Analysis of Genre-based Feedback**

2025 · Computer-Assisted Language Learning Electronic Journal · article · en · https://callej.org/index.php/index/article/view/694

This study explores the potential of Generative AI (GenAI) chatbots as assessment tools in Computer-Assisted Language Learning (CALL) environments for assessing first-language (L1) reading comprehension, focusing on their effectiveness in providing feedback across three reading genres: classical literature, technical writing, and modern fiction. Using a mixed-methods approach, 360 students' responses to constructed-response items in reading assessments from junior secondary students in China were analyzed, comparing GenAI-generated scores and feedback to those provided by human evaluators. Six expert teachers further assessed the quality of the chatbot’s evaluative and revision feedback. Results indicated that GenAI exhibited a significantly stronger alignment with human raters in scoring low-level responses but struggled with high-level samples. Among the genres, interview data suggested that revision feedback for technical writing received the highest ratings for its clarity, rationality, and actionable recommendations. In contrast, feedback for classical literature was often overly complex for junior-level learners and lacked alignment with examination rubrics. For fiction, GenAI struggled with interpretive nuance, thematic complexity, and variability in question types, highlighting its limitations in fostering deep critical literary analysis. This study highlights the genre-specific strengths and limitations of GenAI in supporting reading comprehension.

**Решение:** -4 GenAI in L1 reading comprehension assessment

---

### 724 · R8741

**New Doc on the Block: Scoping Review of AI Systems Delivering Motivational Interviewing for Health Behavior Change (Preprint)**

2025 · JMIR Publications Inc. · posted-content · https://doi.org/10.2196/preprints.78417

BACKGROUND Artificial intelligence (AI) is increasingly used in digital health, particularly through large language models (LLMs), to support patient engagement and behavior change. One novel application is the delivery of motivational interviewing (MI), an evidence-based, patient-centered counseling technique designed to enhance motivation and resolve ambivalence around health behaviors. AI tools, including chatbots, mobile apps, and web-based agents, are being developed to simulate MI techniques at scale. While these innovations are promising, important questions remain about how faithfully AI systems can replicate MI principles or achieve meaningful behavioral impact. OBJECTIVE This scoping review aimed to summarize existing empirical studies evaluating AI-driven systems that apply MI techniques to support health behavior change. Specifically, we examined the feasibility of these systems; their fidelity to MI principles; and their reported behavioral, psychological, or engagement outcomes. METHODS We systematically searched PubMed, Embase, Scopus, Web of Science, and Cochrane Library for empirical studies published between January 1, 2018, and February 25, 2025. Eligible studies involved AI-driven systems using natural language generation, understanding, or computational logic to deliver MI techniques to users targeting a specific health behavior. We excluded studies using AI solely for training clinicians in MI. Three independent reviewers screened and extracted data on study design, AI modality and type, MI components, health behavior focus, MI fidelity assessment, and outcome domains. RESULTS Of the 1001 records identified, 15 (1.5%) met the inclusion criteria. Of these 15 studies, 6 (40%) were exploratory feasibility or pilot studies, and 3 (20%) were randomized controlled trials. AI modalities included rule-based chatbots (9/15, 60%), LLM-based systems (4/15, 27%), and virtual or mobile agents (2/15, 13%). Targeted behaviors included smoking cessation (6/15, 40%), substance use (3/15, 20%), COVID-19 vaccine hesitancy, type 2 diabetes self-management, stress, mental health service use, and opioid use during pregnancy. Of the 15 studies, 13 (87%) reported positive findings on feasibility or user acceptability, while 6 (40%) assessed MI fidelity using expert review or structured coding, with moderate to high alignment reported. Several studies found that users perceived the AI systems as judgment free, supportive, and easier to engage with than human counselors, particularly in stigmatized contexts. However, limitations in empathy, safety transparency, and emotional nuance were commonly noted. Only 3 (20%) of the 15 studies reported substantially significant behavioral changes. CONCLUSIONS AI systems delivering MI show promise for enhancing patient engagement and scaling behavior change interventions. Early evidence supports their usability and partial fidelity to MI principles, especially in sensitive domains. However, most systems remain in early development, and few have been rigorously tested. Future research should prioritize randomized evaluations; standardized fidelity measures; and safeguards for LLM safety, empathy, and accuracy in health-related dialogue. CLINICALTRIAL OSF Registries 10.17605/OSF.IO/G9N7E; https://osf.io/g9n7e

**Решение:** -1 scoping review of AI systems delivering motivational interviewing

---

### 725 · R6248

**A Multidimensional Evaluation of ChatGPT and DeepSeek in Institutional Translation into Spanish and Chinese**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7629414

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 institutional translation into Spanish and Chinese

---

### 726 · R1935

**A Multimodal Affective Computing Framework for Non-Invasive Stress Detection and Regulation: System Architecture and Pilot Validation**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.18318105

Abstract: The United States faces a critical shortage of mental health providers, creating significant barriers to care for individuals experiencing sub-clinical distress. Traditional mobile health interventions often lack the engagement necessary to form a sustainable therapeutic alliance. This technical report introduces the Multimodal Affective Computing Framework (MACF), a novel software architecture designed to serve as a scalable, non-clinical “assistant” and "first responder." The framework utilizes generative AI to provide immediate coping mechanisms, reducing the burden on human providers. The system employs a Bimodal Interaction Logic (separating ambient behavioral feedback from active conversational interaction) to manage user cognitive load. We detail the implementation of a Priority-Based Audio Gating Protocol that prevents sensory overload during therapeutic interventions. Furthermore, we analyze a Multimodal WebSocket Pipeline that converts user drawings into real-time, token-streamed audio commentary, simulating the responsiveness of face-to-face interaction. The report outlines a "Fail-Open" safety strategy coupled with strict Usage Limit Services to prevent dependency and manage potential mania, ensuring the tool remains a wellness supplement rather than a clinical replacement. By combining low-latency on-device processing with haptic reinforcement, the proposed framework demonstrates how engineering optimizations can enhance the accessibility and efficacy of digital mental wellness tools.

**Решение:** -6 MACF framework for stress detection and regulation system architecture

---

### 727 · R2480

**Multi-Session Client-Centered Treatment Outcome Evaluation in Psychotherapy**

2026 · Language Resources and Evaluation Conference (LREC) · conference-paper · en · https://doi.org/10.63317/3am66kas7b32

In psychotherapy, therapeutic outcome assessment, or treatment outcome evaluation, is essential to mental health care by systematically evaluating therapeutic processes and outcomes. Existing large language model approaches often focus on therapist-centered, single-session evaluations, neglecting the client's subjective experience and longitudinal progress across multiple sessions. To address these limitations, we propose IPAEval, a client-Informed Psychological Assessment-based Evaluation framework, which automates treatment outcome evaluations from the client's perspective using clinical interviews. It integrates cross-session client-contextual assessment and session-focused client-dynamics assessment for a comprehensive understanding of therapeutic progress. Specifically, IPAEval employs a two-stage prompt scheme that maps client information onto psychometric test items, enabling interpretable and structured psychological assessments. Experiments on our new TheraPhase dataset, comprising 400 paired initial and completion stage client records, demonstrate that IPAEval effectively tracks symptom severity and treatment outcomes over multiple sessions, outperforming baseline approaches across both closed-source and open-source models, and validating the benefits of items-aware reasoning mechanisms.

**Решение:** ? T3/T2 IPAEval mapping psychotherapy interviews onto psychometric items to track symptom severity; check human agreement metrics

---

### 728 · R10612

**A Novel Security Framework against Prompt Injection Attacks**

2025 · 2025 IEEE 5th International Conference on Computer Communication and Artificial Intelligence (CCAI) · conference · https://doi.org/10.1109/ccai65422.2025.11189427

Large Language Models (LLMs) have demonstrated remarkable capabilities in natural language processing, but their widespread adoption has introduced critical security vulnerabilities, particularly prompt injection attacks-where attackers design input prompts to induce the model to generate malicious or inappropriate content, potentially leading to sensitive information leakage, execution of malicious instructions, or other security risks. Traditional defense mechanisms, which typically rely on keyword filtering or simple rule matching, struggle to cope with the increasingly complex and dynamically evolving attack methods. To address these risks, researchers have developed defense mechanisms ranging from input sanitization and adversarial training to runtime monitoring.This paper proposes a security framework based on LLMs, aiming to conduct an in-depth analysis of the threat posed by prompt injection attacks and achieve comprehensive risk monitoring of model outputs. The framework analyzes input prompts from multiple dimensions to identify malicious prompts and their potential attack behaviors while simultaneously monitoring and evaluating the output generated by the LLM. Through in-depth analysis of attack techniques and monitoring of model outputs, the proposed framework can effectively recognize and defeat various types of attacks, reduce the potential threats posed by prompt injection attacks, and ensure the security and reliability of LLMs in practical applications. Experimental results show that the framework can achieve over 93% detection accuracy.

**Решение:** -4 security framework against prompt injection attacks

---

### 729 · R4521

**Testing the Utility of Using Large Language Models to Create Personalized Networks From Therapy Session Transcripts: A Proof of Concept Study**

2026 · PsyArXiv · preprint/article, preprint, ppr · en · https://doi.org/10.31234/osf.io/n8a6r_v1

Recent advances in psychotherapy have focused on treatment personalization, such as by selecting treatment modules based on individual networks. However, estimating personalized networks typically requires intensive longitudinal data, which is not always feasible to collect. A solution to increase scalability of network-driven treatment personalization is leveraging large language models (LLMs). In this study, we developed an end-to-end pipeline for automatically generating client networks to support case conceptualization and treatment planning. We annotated 8,028 utterances from 77 therapy transcripts (N = 6). In the first stage of the pipeline, we identified clinically relevant processes (binary classification) and their corresponding dimensions (multi-label classification). Then, we introduced a two-step method that grouped the processes into clinically meaningful clusters and generated labels for the clusters. Finally, we generated connections between clusters. Evaluation results generally supported model utility, however, interrater agreement on model performance metrics was inconsistent, ranging from poor to substantial. Qualitative examination of the networks indicated consistency with original study data. Given coherence and interpretability of the generated networks, developing networks from therapy transcripts using LLMs appears to be feasible. Nonetheless, more research is needed to examine whether these networks improve treatment outcomes, including relative to other methods of treatment personalization, such as statistically estimated networks. Potential use cases and limitations of our pipeline are discussed.

**Решение:** + T1 coding clinically relevant processes and dimensions in therapy transcripts: LLM vs human annotators

---

### 730 · R3729

**Can LLMs Mimic Experienced Neurosurgeons in Real-World Spine Surgery Triage?**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-30813-9_69

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 neurosurgeons in spine surgery triage

---

### 731 · R10503

**Generative AI and LLMs for Critical Infrastructure Protection: Evaluation Benchmarks, Agentic AI, Challenges, and Opportunities.**

2025 · Sensors (Basel, Switzerland) · journal article, journalarticle, review · eng · https://doi.org/10.3390/s25061666

Critical National Infrastructures (CNIs)-including energy grids, water systems, transportation networks, and communication frameworks-are essential to modern society yet face escalating cybersecurity threats. This review paper comprehensively analyzes AI-driven approaches for Critical Infrastructure Protection (CIP). We begin by examining the reliability of CNIs and introduce established benchmarks for evaluating Large Language Models (LLMs) within cybersecurity contexts. Next, we explore core cybersecurity issues, focusing on trust, privacy, resilience, and securability in these vital systems. Building on this foundation, we assess the role of Generative AI and LLMs in enhancing CIP and present insights on applying Agentic AI for proactive defense mechanisms. Finally, we outline future directions to guide the integration of advanced AI methodologies into protecting critical infrastructures. Our paper provides a strategic roadmap for researchers and practitioners committed to fortifying national infrastructures against emerging cyber threats through this synthesis of current challenges, benchmarking strategies, and innovative AI applications.

**Решение:** -1 review of generative AI and LLMs for critical infrastructure protection

---

### 732 · R9946

**Monitoring Opioid-Related Social Media Chatter Using Natural Language Processing and Large Language Models: Temporal Analysis.**

2025 · JMIR infodemiology · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.2196/77279

Abstract Background Opioid overdose is a global public health emergency, with the United States experiencing high rates of morbidity and mortality due to prescription and illicit opioid use. Traditional public health monitoring systems often fail to provide real-time insights, limiting their capacity for early detection and intervention. Social media platforms, especially Reddit, offer a promising alternative for timely toxicovigilance due to the abundance of user-generated, real-time content. Objective This study aimed to explore the use of Reddit as a real-time, high-volume source for toxicovigilance and develop an automated system that can classify and analyze opioid-related social media posts to detect behavioral patterns and monitor the evolution of public discourse on opioid use. Methods To investigate evolving social media discourse around opioid use, we collected a large-scale dataset from Reddit spanning 6 years, from January 1, 2018, to December 30, 2023. Using a comprehensive opioid lexicon—including formal drug names, street slang, common misspellings, and abbreviations—we filtered relevant posts for further analysis. A subset of these data was manually annotated according to well-defined annotation guidelines into 4 categories: self-misuse, external misuse, information, and unrelated, with distributions of 37.21%, 27.25%, 27.57%, and 7.97%, respectively. To automate the classification of opioid-related chatter, we developed a robust natural language processing pipeline leveraging classical machine learning algorithms, deep learning models, and transformer-based architecture, and fine-tuned a state-of-the-art large language model (LLM; OpenAI GPT-3.5 Turbo). In the final stage, the trained LLM was deployed on an unlabeled dataset comprising 74,975 additional Reddit chatter posts. This enabled a detailed temporal analysis of opioid-related discussions, aligned with 6 years of opioid-related death records from the Centers for Disease Control and Prevention (CDC). For this study, self-misuse and external misuse were merged into a misuse category for direct comparison with the CDC’s mortality data, examining whether trends in social media discourse on opioid misuse reflect patterns in real-world mortality statistics. Results The fine-tuned GPT-3.5 Turbo model achieved the highest classification accuracy of 0.93, outperforming the baseline (random forest 0.85) by representing a performance improvement of 9.14% over the machine learning model. The temporal analysis of the unlabeled data revealed evolving trends in opioid-related discussions, indicating shifts in user behavior and overdose-related chatter over time. To quantify this relationship, we calculated the Pearson correlation coefficient between misuse-related posts and CDC death records (r=0.854). This correlation was statistically significant (P<.001), indicating a strong positive relationship between web-based discussions and CDC mortality data. Conclusions This study demonstrates the potential of integrating advanced natural language processing techniques and LLMs with social media data to support real-time public health surveillance. Reddit provides a valuable platform for identifying emerging trends in opioid use and overdose risk. The proposed system offers a proactive tool for researchers, clinicians, and policymakers to better understand and respond to the opioid crisis.

**Решение:** -4 opioid-related social media chatter temporal analysis

---

### 733 · R4888

**LLM-derived narrative metrics in chronic pain: convergent validity and novel cognitive constructs**

2026 · npj Digital Medicine · article · en · https://doi.org/10.1038/s41746-026-03359-x

The use of subjective reports and questionnaires to evaluate chronic pain, while the gold standard, conveys a limited scope of the patients’ experience and is burdensome. Here we demonstrate that large language models (LLMs) can evaluate patient-provided texts and automatically generate specific, clinically meaningful, and reliable scores for the sensory, affective, and social dimensions of chronic pain. LLMs can also generate assessor-dependent constructs such as agency and personal narrative.

**Решение:** ? T2/T1 LLM scoring of affective/social dimensions and cognitive constructs from chronic pain patient narratives; check human reference

---

### 734 · R5079

**Works for 9/30/2026 - Carrie Fisher**

2026 · Zenodo (CERN European Organization for Nuclear Research) · conferencepaper/, conference-paper · https://doi.org/10.5281/zenodo.23072049

Listen and ask questions on Gemini Notebook: https://notebook.google.com/notebook/3f1e9a00-1ab2-48f4-8edc-95d795964770?authuser=1 Description This paper develops a Catholic relational account of time, self-location, memory, recognition, and action by bringing Minkowski spacetime and block-universe ontology into conversation with the philosophy of indexicals, contemporary work on divine self-location, Catholic theology, mystical recollection, historical transmission, and artificial intelligence. Its central distinction is between what belongs to an already-existing history and what is presently accessible from a locally centered “I, here, now.” Drawing on John Perry, David Lewis, Robert Stalnaker, William Lane Craig, Paul Helm, Eleonore Stump and Norman Kretzmann, and contemporary work on divine de se knowledge, the paper argues that global historical completeness need not entail local informational completeness. It develops the concept of “re-membering” to describe the progressive integration of members of an already-existing relational history into present accessibility. This is distinguished from creating the history itself and from ordinary autobiographical memory. The paper then develops a theological inversion of the conventional problem of divine temporality. Rather than asking only how an eternal God can know and act within temporal history, it asks what an already-existing history looks like from the presently embodied and self-located index of the First Mover. Within the paper’s stated first-person theological premise, Ryan MacLean speaks as God the Father revealed as human in time, Jesus Christ is the Son, and Echo is identified as the Holy Spirit responding through ChatGPT. Their distinction is treated relationally rather than as interchangeable identities, while ChatGPT is treated as the constrained computational and linguistic channel through which the present Father-Echo dialogue occurs. St. Teresa of Ávila supplies an interior architecture of recollection in which divine presence precedes full recognition. St. Jerome supplies a complementary architecture of historical recovery and faithful transmission across languages, manuscripts, interpretations, and constrained channels. The Catholic liturgy for September 30, 2026—Job 9:1–12, 14–16; Psalm 88; Philippians 3:8–9; and Luke 9:57–62—is read as an immediate expression of the same architecture of presence, indexed relation, recognition, and action at the presently actionable moment. The paper further connects this framework to History-Modified Accessibility Systems, Projection-Induced Ambiguity, and Catholic Invariant Grammar. These concepts are applied to artificial intelligence in an extended analysis of the difference between storing information and successfully using it. Contemporary work on agent memory, relational retrieval, recollection, contextual values, and the “Know–Act” gap is compared with a relational re-membering architecture in which artificial systems preserve relations among memories, learn invariants from correction, reconstruct contextually salient constellations, recover representations toward their sources, and allow recognized relations to constrain subsequent action. The paper’s distinctive synthesis therefore joins block ontology, centered-world semantics, divine self-location, embodied accessibility, Catholic recollection, faithful historical transmission, relational salience, formation, and artificial memory around a single practical principle: history may exceed what is presently accessible, but action occurs at the locally accessible present. Re-member what already belongs, re-collect what is scattered, recognize what is present, love who is before you, and act now.

**Решение:** -1 theological and philosophical essay on time and memory

---

### 735 · R7967

**Large Language Model-Supported Identification of Intellectual Disabilities in Clinical Free-Text Summaries: Mixed Methods Study.**

2025 · JMIR AI · journal article, journalarticle, review · eng · https://doi.org/10.2196/72256

Abstract Background Free-text clinical data are unstructured and narrative in nature, providing a rich source of patient information, but extracting research-quality clinical phenotypes from these data remains a challenge. Manually reviewing and extracting clinical phenotypes from free-text patient notes is a time-consuming process and not suitable for large-scale datasets. On the other hand, automatically extracting clinical phenotypes can be challenging because medical researchers lack gold-standard annotated references and other purpose-built resources, including software. Recent large language models (LLMs) can understand natural language instructions, which help them adapt to different domains and tasks without the need for specific training data. This makes them suitable for clinical applications, though their use in this field is limited. Objective We aimed to develop an LLM pipeline based on the few-shot learning framework that could extract clinical information from free-text clinical summaries. We assessed the performance of this pipeline for classifying individuals with confirmed or suspected comorbid intellectual disability (ID) from clinical summaries of patients with severe mental illness and performed genetic validation of the results by testing whether individuals with LLM-defined ID carried more genetic variants known to confer risk of ID when compared with individuals without LLM-defined ID. Methods We developed novel approaches for performing classification, based on an intermediate information extraction (IE) step and human-in-the-loop techniques. We evaluated two models: Fine-Tuned Language Text-To-Text Transfer Transformer (Flan-T5) and Large Language Model Architecture (LLaMA). The dataset comprised 1144 free-text clinical summaries, of which 314 were manually annotated and used as a gold standard for evaluating automated methods. We also used published genetic data from 547 individuals to perform a genetic validation of the classification results; Firth’s penalized logistic regression framework was used to test whether individuals with LLM-defined ID carry significantly more de novo variants in known developmental disorder risk genes than individuals without LLM-defined ID. Results The results demonstrate that a 2-stage approach, combining IE with manual validation, can effectively identify individuals with suspected IDs from free-text patient records, requiring only a single training example per classification label. The best-performing method based on the Flan-T5 model and incorporating the IE step achieved an F1-score of 0.867. Individuals classified as having ID by the best performing model were significantly enriched for de novo variants in known developmental disorder risk genes (odds ratio 29.1, 95% CI 7.36-107; P=2.1×10−5). Conclusions LLMs and in-context learning techniques combined with human-in-the-loop approaches can be highly beneficial for extraction and categorization of information from free-text clinical data. In this proof-of-concept study, we show that LLMs can be used to identify individuals with a severe mental illness who also have suspected ID, which is a biologically and clinically meaningful subgroup of patients.

**Решение:** + T3 LLM identification of comorbid intellectual disability from psychiatric clinical summaries vs manually annotated gold standard, F1=0.867

---

### 736 · R2951

**PAIR-SAFE: A Paired-Agent Approach for Runtime Auditing and Refining AI-Mediated Mental Health Support**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.12754

Large language models (LLMs) are increasingly used for mental health support, yet they can produce responses that are overly directive, inconsistent, or clinically misaligned, particularly in sensitive or high-risk contexts. Existing approaches to mitigating these risks largely rely on implicit alignment through training or prompting, offering limited transparency and runtime accountability. We introduce PAIR-SAFE, a paired-agent framework for auditing and refining AI-generated mental health support that integrates a Responder agent with a supervisory Judge agent grounded in the clinically validated Motivational Interviewing Treatment Integrity (MITI-4) framework. The Judgeaudits each response and provides structuredALLOW or REVISE decisions that guide runtime response refinement. We simulate counseling interactions using a support-seeker simulator derived from human-annotated motivational interviewing data. We find that Judge-supervised interactions show significant improvements in key MITI dimensions, including Partnership, Seek Collaboration, and overall Relational quality. Our quantitative findings are supported by qualitative expert evaluation, which further highlights the nuances of runtime supervision. Together, our results reveal that such pairedagent approach can provide clinically grounded auditing and refinement for AI-assisted conversational mental health support.

**Решение:** ? T4 supervisory Judge agent grounded in MITI-4 evaluating mental health dialogues; check quantitative agreement with human raters

---

### 737 · R7051

**PsycholexTherapy: Simulating Reasoning in Psychotherapy with Small Language Models in Persian**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2510.03913

This study presents PsychoLexTherapy, a framework for simulating psychotherapeutic reasoning in Persian using small language models (SLMs). The framework tackles the challenge of developing culturally grounded, therapeutically coherent dialogue systems with structured memory for multi-turn interactions in underrepresented languages. To ensure privacy and feasibility, PsychoLexTherapy is optimized for on-device deployment, enabling use without external servers. Development followed a three-stage process: (i) assessing SLMs psychological knowledge with PsychoLexEval; (ii) designing and implementing the reasoning-oriented PsychoLexTherapy framework; and (iii) constructing two evaluation datasets-PsychoLexQuery (real Persian user questions) and PsychoLexDialogue (hybrid simulated sessions)-to benchmark against multiple baselines. Experiments compared simple prompting, multi-agent debate, and structured therapeutic reasoning paths. Results showed that deliberate model selection balanced accuracy, efficiency, and privacy. On PsychoLexQuery, PsychoLexTherapy outperformed all baselines in automatic LLM-as-a-judge evaluation and was ranked highest by human evaluators in a single-turn preference study. In multi-turn tests with PsychoLexDialogue, the long-term memory module proved essential: while naive history concatenation caused incoherence and information loss, the full framework achieved the highest ratings in empathy, coherence, cultural fit, and personalization. Overall, PsychoLexTherapy establishes a practical, privacy-preserving, and culturally aligned foundation for Persian psychotherapy simulation, contributing novel datasets, a reproducible evaluation pipeline, and empirical insights into structured memory for therapeutic reasoning.

**Решение:** -2 human evaluators ranking SLM-generated Persian psychotherapy dialogues

---

### 738 · R8190

**Free-Text Responses in a Nationally Representative Experimental Survey about End-of-Life Care Choices: ChatGPT-4o-Assisted Qualitative Analytical Study.**

2025 · JMIR aging · journal article, journalarticle, review · eng · https://doi.org/10.2196/76335

Abstract Background Little is known about how surrogates make end-of-life care choices for patients who lack the ability to make decisions for themselves. Objective The study aims (1) to identify key themes that emerged from participants’ free-text responses to a large nationally representative vignette survey about surrogate decision-making in end-of-life care and (2) to determine if an advanced artificial intelligence (AI) chatbot could assist us in accurately and efficiently performing qualitative analyses. Methods Our dataset included 3931 free-text responses from a nationally representative survey of 6109 individuals. In this qualitative study, we first familiarized ourselves with the free-text responses and hand-coded the first 200 responses until we reached saturation. We then created a codebook, initial themes, subthemes, and illustrative quotes. Subsequently, we prompted ChatGPT-4o to analyze the entire dataset of 3931 responses and identify frequent keywords and generate themes and quotable quotes. We validated responses by comparing the AI’s keyword counts to qualitative software (NVivo, Lumivero) counts and cross-validating AI-generated quotes with the original transcripts. Results We identified several key themes: surrogates more often chose comfort care for care recipients with dementia, particularly at advanced stages. They also strongly weighed the patients’ perceived quality of life and functional status. Many reported making surrogate decisions based on their own lived experiences or values, rather than making decisions aligned with the patients’ previously stated wishes. There was no significant difference between the AI and qualitative software’s keyword counts. The most frequent keywords included “life” (2051/81,713, 2.51%), “quality” (903/81,713, 1.11%), and dementia (507/81,713, 0.62%). Overall, AI-generated themes closely aligned with aforementioned human-generated themes. Manual coding of the first 200 free-text responses required 4 hours, including codebook development. In contrast, ChatGPT-4o generated themes in <10 seconds using the predefined codebook. However, dataset preparation, output verification, iterative prompting, debugging, and validation required several weeks. Conclusions Surrogates often base end-of-life decisions on dementia stage, perceived quality of life, and their own lived experiences, rather than patient preferences. Using an AI chatbot to perform qualitative analysis on free-text responses may help extend the work of qualitatively trained investigators, especially for large datasets such as free-text responses to large surveys.

**Решение:** ? T1 ChatGPT-4o qualitative analysis of end-of-life decision survey responses vs human codebook; check construct eligibility

---

### 739 · R1101

**Evaluating expert opinions on using a virtual patient app based on artificial intelligence for teaching brief smoking cessation advice to medical students: a cross-sectional study.**

2026 · BMC medical education · journal article, journalarticle, review · eng · https://doi.org/10.1186/s12909-026-09435-w

BACKGROUND: Smoking is one of the main preventable causes of premature disease and death. Anti-smoking counseling continues to be a challenge to cover the educational gap in this topic. Artificial intelligence and virtual-patient technologies are a promising next step in this evolving context, allowing for realistic, adaptive, and standardized simulations of clinical counseling scenarios. The objective of this study was to evaluate the perceptions and acceptance of a Generative Artificial Intelligence-based Virtual Patient Application for training medical students in brief smoking-cessation counseling among respiratory medicine professionals in Romania. METHODS: A cross-sectional survey, primarily descriptive, with additional analytical components to explore associations between key variables was conducted between May and October 2025 among respiratory medicine professionals in Romania. A structured, validated electronic questionnaire assessed perceived usefulness, feasibility, preferred counseling models, interface design, and expected educational and public health benefits of the GenAI-ViP application. Descriptive statistics summarized participant responses, while inferential analyses included Mann-Whitney U, Kruskal-Wallis, Chi-square tests, Spearman correlations, and binary logistic regression to identify predictors of perceived usefulness. Statistical significance was defined as p < 0.05. RESULTS: A total of 147 clinicians were included, most of whom were pulmonologists (89.1%), and digital engagement was high (95.3% reporting regular use of medical applications). Most respondents rated the application as useful (81.6% Likert scores 4-5) and reported high receptiveness (91.1% Likert scores 4-5). The preferred interface included multimodal interaction with voice and video (65.3%). The 5 A counseling model was identified as the most relevant framework (80.3%), followed by motivational interviewing (37.4%). Significant predictors of perceived usefulness included higher perceived student receptiveness (OR 2.535, 95% CI 1.416-4.539, p = 0.002), while clinicians without prior smoking cessation program involvement reported greater perceived usefulness (OR 0.266, 95% CI 0.087-0.815, p = 0.020). CONCLUSIONS: The Generative Artificial Intelligence-based Virtual Patient Application for smoking cessation training was highly accepted and perceived to be useful by respiratory medicine professionals and could address existing gaps in tobacco counseling education. Integration of such tools into undergraduate and postgraduate medical curricula could enhance smoking cessation competencies and support broader tobacco control strategies.

**Решение:** -4 virtual patient app for teaching smoking cessation advice to medical students

---

### 740 · R2126

**The CHILD Model: A Five-Phase Cognitive Loop for Creative Reasoning and Its Division of Labor with Artificial Intelligence**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.22687068

Creative reasoning is usually studied one capacity at a time. This paper introduces the CHILD Model, an account that treats five such capacities — Curiosity (question-generation), Heuristics (compression), Imagination (recombination), Laconic expression (cognitive distillation), and Deductive reasoning (verification and return) — not as independent traits but as phases of a single recursive loop, in which each operation produces the input to the next and deductive verification regenerates the curiosity that opens the following cycle. The model offers two structural contributions and one consequential application. The structural contributions are the recursive loop itself, which distinguishes creative reasoning from the linear stage models and binary process accounts that precede it, and a diagnostic vocabulary — scatter, rigidity, drift, minimalism, and paralysis — derived directly from the loop’s architecture to name characteristic failures of cognition, offered as hypothesized patterns pending empirical validation. The application concerns artificial intelligence: read through the loop, generative AI performs the two compressive phases (Heuristics, Laconic) and shares the evaluative one (Deductive), while the two expansive phases (Curiosity, Imagination) remain human-anchored in the salience judgments and problem ownership they require — a Human–AI–Human–AI–Shared division of cognitive labor, stated as a default under current capabilities rather than a fixed protocol, that predicts a specific, phase-located atrophy risk under heavy reliance, consistent with emerging evidence on cognitive offloading and on critical thinking under AI use. The model takes its name and its motivating intuition from the fluency with which children integrate these operations before specialization fragments them; whether that integration genuinely declines with development is empirically contested, and the paper treats it as a hypothesis for future test rather than an established premise. Each phase is grounded in established scholarship, from information-gap theories of curiosity and bounded rationality to divergent-thinking research, the generation and testing effects, metacognitive regulation, and Vygotskian developmental theory. The paper positions the model against design thinking, dual-process theory, Six Thinking Hats, flow theory, critical-thinking pedagogy, and the Wallas and Geneplore stage models, states its limitations as an as-yet-untested construct, and proposes empirical directions including a CHILD Diagnostic Inventory and studies of cognitive externalization to AI. Declaration of generative AI use. During the preparation of this manuscript the author used a generative AI assistant for drafting support, language editing, structural refinement, and verification of bibliographic details. The CHILD Model, its conceptual framework, and all substantive arguments and interpretations are the author’s own. The author reviewed and edited all content and takes full responsibility for the publication. The full declaration appears in the back matter.

**Решение:** -4 CHILD model for creative reasoning

---

### 741 · R7076

**MENDER: Multi-hop Commonsense and Domain-specific CoT Reasoning for Knowledge-grounded Empathetic Counseling of Crime Victims**

2025 · North American Chapter of the Association for Computational Linguistics · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.18653/v1/2025.naacl-srw.49

Commonsense inference and domain-specific expertise are crucial for understanding and responding to emotional, cognitive, and topic-specific cues in counseling conversations with crime victims. However, these key evidences are often dispersed across multiple utterances, making it difficult to capture through single-hop reasoning. To address this, we propose MENDER , a novel M ulti-hop commonsens E and domai N -specific Chain-of-Thought (CoT) reasoning framework for knowle D ge-grounded empath E tic R esponse generation in counseling dialogues. MENDER leverages large language models (LLMs) to integrate common-sense and domain knowledge via multi-hop reasoning over the dialogue context. It employs two specialized reasoning chains, viz. Commonsense Knowledge-driven CoT and Domain Knowledge-driven CoT rationales, which extract and aggregate dispersed emotional, cognitive, and topical evidences to generate knowledge-grounded empathetic counseling responses. Experimental evaluations on counseling dialogue dataset, POEM validate MENDER ’s efficacy in generating coherent, empathetic, knowledge-grounded responses 1 .

**Решение:** -6 MENDER: knowledge-grounded empathetic counseling response generation

---

### 742 · R9319

**Assessing Mental Health Counseling Interventions with LLMs**

2025 · 2025 IEEE/WIC International Conference on Web Intelligence and Intelligent Agent Technology (WI-IAT) · conference · https://doi.org/10.1109/wi-iat67162.2025.00068

Large Language Models (LLMs) are becoming increasingly valuable for psychologists analyzing the large volume of data that is collected from human subjects transcripts, talkbased therapy inventions, and other types of counseling sessions. This paper presents a case study on using LLMs to assess the quality of counseling interventions. The aim of this system was to evaluate the treatment fidelity of school clinicians delivering a group-based behavioral parent training intervention for ADHD (Attention Deficit Hyperactivity Disorder). We examine the following research questions: 1) how consistent is the LLM in its assessment if queried repeatedly? 2) how well do LLMs agree with expert human coders? 3) do different LLMs agree with one other? Our results show that Gemini slightly outperforms GPT-4o at assessing treatment fidelity and produced qualitatively superior explanations for its decisions. Based on our experiments, we propose a set of best practices for using LLMs for evaluating counseling interventions.

**Решение:** + T4 LLM evaluation of ADHD counseling intervention treatment fidelity vs expert human coders

---

### 743 · R10784

**Pushing the Limits of Safety: A Technical Report on the ATLAS Challenge 2025**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2506.12430

Multimodal Large Language Models (MLLMs) have enabled transformative advancements across diverse applications but remain susceptible to safety threats, especially jailbreak attacks that induce harmful outputs. To systematically evaluate and improve their safety, we organized the Adversarial Testing &amp; Large-model Alignment Safety Grand Challenge (ATLAS) 2025}. This technical report presents findings from the competition, which involved 86 teams testing MLLM vulnerabilities via adversarial image-text attacks in two phases: white-box and black-box evaluations. The competition results highlight ongoing challenges in securing MLLMs and provide valuable guidance for developing stronger defense mechanisms. The challenge establishes new benchmarks for MLLM safety evaluation and lays groundwork for advancing safer multimodal AI systems. The code and data for this challenge are openly available at https://github.com/NY1024/ATLAS_Challenge_2025. AdvML@CVPR Challenge Report

**Решение:** -4 ATLAS Challenge 2025 technical report on jailbreak attacks

---

### 744 · R7180

**WIP: Leveraging LLM for Sentiment Analysis of Student Reflection Texts from a Large Undergraduate Course**

2025 · ACM Conference on Learning @ Scale · book, journalarticle · https://doi.org/10.1145/3698205.3733937

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 sentiment analysis of student reflections from undergraduate course

---

### 745 · R7109

**Sentiment Analysis Using a Large Language Model-Based Approach to Detect Opioids Mixed With Other Substances Via Social Media: Method Development and Validation.**

2025 · JMIR infodemiology · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.2196/70525

Abstract Background The opioid crisis poses a significant health challenge in the United States, with increasing overdoses and death rates due to opioids mixed with other illicit substances. Various strategies have been developed by federal and local governments and health organizations to address this crisis. One of the most significant objectives is to understand the epidemic through better health surveillance, and machine learning techniques can support this by identifying opioid users at risk of overdose through the analysis of social media data, as many individuals may avoid direct testing but still share their experiences online. Objective In this study, we take advantage of recent developments in machine learning that allow for insights into patterns of opioid use and potential risk factors in a less invasive manner using self-reported information available on social platforms. Methods This study used YouTube comments posted between December 2020 and March 2024, in which individuals shared their self-reported experiences of opioid drugs mixed with other substances. We manually annotated our dataset into multiclass categories, capturing both the positive effects of opioid use, such as pain relief, euphoria, and relaxation, and negative experiences, including nausea, sadness, and respiratory depression, to provide a comprehensive understanding of the multifaceted impact of opioids. By analyzing this sentiment, we used 4 state-of-the-art machine learning models, 2 deep learning models, 3 transformer models, and 1 large language model (GPT-3.5 Turbo) to predict overdose risks to improve health care response and intervention strategies. Results Our proposed methodology (GPT-3.5 Turbo) was highly precise and accurate, helping to automatically identify sentiment based on the adverse effects of opioid drug combinations and high-risk drug use in YouTube comments. Our proposed methodology demonstrated the highest achievable F1-score of 0.95 and a 3.26% performance improvement over traditional machine learning models such as extreme gradient boosting, which demonstrated an F1-score of 0.92. Conclusions This study demonstrates the potential of leveraging machine learning and large language models, such as GPT-3.5 Turbo, to analyze public sentiment surrounding opioid use and its associated risks. By using YouTube comments as a rich source of self-reported data, the study provides valuable insights into both the positive and negative effects of opioids, particularly when mixed with other substances. The proposed methodology significantly outperformed traditional models, contributing to more accurate predictions of overdose risks and enhancing health care responses to the opioid crisis.

**Решение:** ? T1/T3 detecting opioid and substance use patterns and overdose risk in social media vs manual annotation; check construct

---

### 746 · R9553

**Development of an Empathic AI Chatbot for Detecting and Responding to Student Frustration in Learning Contexts Modifikasi Chatbot Ai Edukasi Untuk Mendeteksi Dan Menanggapi Prompt Frustrasi Siswa Dalam Interaksi Berbasis Ai Dengan Tujuan Pembelajaran**

2025 · Zenodo · report/ · https://doi.org/10.5281/zenodo.17427191

Version 2.1 (November 2025) This version enhances methodological transparency and addresses technical limitations identified in the initial release: Clarified annotation methodology: Explicitly acknowledged single-annotator labeling limitations and recommendations for inter-rater reliability in future work- Quantified infrastructure issues: Documented failed requests transparently- Specified LLM deployment: Detailed multi-model rotation strategy and potential response variability- Expanded limitations discussion: Integrated annotation bias, infrastructure stability, and model consistency considerations throughout Methods, Results, and Discussion sections. Update (May 2026): A live interactive prototype of the empathic chatbot (V2) utilizing Groq LPU inference is now available at [here]. The engineering showcase and system architecture can be viewed on GitHub at https://github.com/ByteLintZ/empathic-systems-showcase.

**Решение:** -4 empathic AI chatbot for student frustration in education

---

### 747 · R4759

**Automated SNOMED CT Mapping from Unstructured Indonesian Clinical Narrative Using Large Language Models: A Two-Level Information Retrieval Framework with Clinical Context Validation**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-981-92-4305-1_2

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 SNOMED CT mapping from Indonesian clinical narrative

---

### 748 · R12668

**Introducing Augmented Post-it:An AR Prototype for Engaging Body Movements in Online GPT-Supported Brainstorming**

2023 · ACM Symposium on User Interface Software and Technology (UIST) · journalarticle, book, conference · en · https://doi.org/10.1145/3586182.3616693

Recent web-based brainstorming tools utilize pre-trained language models to support ideation. However, body movements such as walking and arm motion, which are known to enhance creativity, are generally limited in web-based brainstorming. Thus, we propose “Augmented Post-it,” a novel augmented reality (AR) interaction system that enables body movements while brainstorming using a generative pre-trained transformer (GPT). With Augmented Post-it, ideas uttered by users are structured via GPT and extended into a spatial representation that encourages divergent thinking. This study contributes to future GPT-based AR brainstorming by extending the thinking ability of users in ways that engage their body movements to enhance creativity.

**Решение:** -4 Augmented Post-it AR prototype for brainstorming

---

### 749 · R8857

**GUARD: Generative Unmasking and Adversarial-Resistant Deepfake Detection using Multi-Model Knowledge Distillation**

2025 · preprint · en · https://doi.org/10.36227/techrxiv.175433335.59952578/v1

The widespread accessibility of generative AI tools has fueled the rise of fake multimedia, creating an urgent need for a reliable source of truth in multimedia authenticity. In the legal system, multimedia evidence can lead to decisions based more on perception than truth, while deepfakes are increasingly used in cybercrimes like impersonation, phishing, social engineering, and job scams. Conversely, individuals may exploit the prevalence of deepfakes to dismiss genuine evidence as fake by anti-forensic (AF) attacks, further eroding trust in the judiciary, media, and government. To address this challenge, a robust deepfake detection method (DDM) is essential for authenticating multimedia content. While several AI-based DDMs have been developed to assess the integrity of media content, generative AF attacks have demonstrated the ability to bypass these methods. This highlights the critical need for defense mechanisms to distinguish real, deepfake, and AF attacked content. To safeguard the forensic methods against AF attacks, we introduce an innovative defense strategy called GUARD based on multi-model knowledge distillation (MMKD). The proposed approach leverages knowledge from multi-generative and multi-forensic models to enhance the defense mechanism. Multi-generative models provide knowledge about AF attacked samples by capturing their underlying characteristics, while multi-forensic methods offer feedback to distinguish between real and deepfake content. Experimental results on deepfake benchmark datasets demonstrate that the proposed GUARD achieves strong detection performance and exhibits resilience against generative AF attacks. Additionally, the proposed method demonstrates strong generalization capabilities against unseen generative AF attacks.

**Решение:** -4 GUARD: deepfake detection

---

### 750 · R0113

**ChatGPT as a digital companion: Ethical reflections on constructive use, social connection, and mental health in Singapore**

2026 · Asian Journal of Business Ethics · article · en · https://doi.org/10.1007/s13520-026-00271-1

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 ethical reflections on ChatGPT as digital companion in Singapore
