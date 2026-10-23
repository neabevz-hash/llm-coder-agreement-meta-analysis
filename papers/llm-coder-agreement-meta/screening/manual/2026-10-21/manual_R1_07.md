# Ручной отбор, часть 7

Ручной отбор, часть 7: записи 901–1000 из 1000. Эти записи вы размечаете сами, вместо проходов ИИ (deviations.md, D3); это случайные 1000 записей из тех, что ИИ ещё не разметил (зерно 20261024). **Меток ИИ здесь нет и не будет.** Ваше решение окончательное: «+» и «?» идут на полный текст. Размечайте в любом порядке и в несколько заходов.

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

### 901 · R3506

**IGCA Validation: Independent Expert Coding of Governance Crisis Assessment Scenarios**

2026 · OSF Preprints (OSF Preprints) · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/swxrc

Pre-registration for independent expert validation of gold-standard codings used in the study "The Institutional Alarmism Bias: Do Large Language Models Systematically Catastrophize Governance Crises?" Five independent scholars from five Chinese universities will blind-code a stratified sample of 25 governance scenarios (20 crisis, 5 success) using the IGCA framework. This registration freezes the coding protocol, scenario selection, and analysis plan prior

**Решение:** -1 study pre-registration for political governance crisis coding

---

### 902 · R7753

**An Empirical Investigation into the Utility of Large Language Models in Open-Ended Survey Data Categorization**

2025 · preprint · en · https://doi.org/10.31235/osf.io/wv6tk_v5

How effectively can Large Language Models (LLMs) approximate social scientist judgment in categorizing open-ended survey responses? This study systematically compares four zero-shot LLMs—GPT-4o, Claude 3.7 Sonnet, Sonar Large (Llama 3.1), and Mistral Large—against human annotators using 1,200 responses from the UC Berkeley Social Networks Study across three question types, generating over 43,200 individual coding decisions in a multi-label classification framework. Results demonstrate that leading models achieve human-level performance, exhibiting variation patterns with human annotators similar to the disagreement levels observed between human coders themselves. GPT and Claude reached 97% similarity to a sociologist-derived "gold standard" consensus on straightforward categorization tasks and 88-91% on complex interpretive challenges, while Llama and Mistral reached 95-96% and up to 87% respectively. Survey response length emerged as a critical performance factor, with responses under 50 characters demonstrating 7-11% higher accuracy across all models. While models effectively detected nuance in simpler tasks, they struggled with responses containing multiple codes and implicit meanings. Despite high accuracy metrics, some models produced systematically different social narratives for certain demographic groups. The analysis also demonstrated that LLMs can serve as quality control tools, identifying variation in human annotator reliability. These findings provide a systematic framework for implementing automated LLM coding in survey research while demonstrating that models work best as supplements to, rather than replacements for, human judgment in detecting subtle social patterns.

**Решение:** -4 sociological open-ended survey coding

---

### 903 · R6639

**EXPLORING LARGE LANGUAGE MODELS IN AUTOMATED SCORING OF STUDENTS’ COGNITION AND AFFECT IN PROBLEM-POSING BASED LEARNING**

2026 · Library, Museums and Press - UDSpace (University of Delaware) · article · en · https://udspace.udel.edu/bitstreams/9e1f67d5-f003-48e6-81a1-950e5197fb1a/download

This dissertation investigates the potential of Large Language Models (LLMs) to support educational research through automated analysis of students’ cognitive and affective mathematics data within a problem-posing project. Two studies examine whether LLMs can approximate expert human judgments and how prompt design influences their performance. Study 1 evaluates the use of LLMs for quantitative scoring and qualitative coding of 1,116 responses. The LLM assessed holistic quality, mathematical complexity, linguistic structure, and unexpected responses. Baseline prompts produced moderate agreement with expert coders. After systematic prompt refinement, which included clarifying rubric language, resolving ambiguities, and incorporating implicit human coding patterns, performance improved substantially and reached Cohen’s kappa values of 0.749 to 0.929. Study 2 investigates LLM-based scoring of 814 student affective descriptions of mathematics. Three prompt conditions were tested, ranging from baseline rubrics to refined prompts that embedded common human scoring patterns. The most refined prompts achieved high agreement with human ratings (Cohen’s kappa = 0.819 to 0.845). Effective strategies included being specific about the scoring rubrics, intensifier cues, majority–minority reasoning, and accommodating grammatical variation. Across both studies, results show that LLM accuracy can be significantly improved through prompt engineering that mirrors human reasoning. The findings provide methodological guidance for educational researchers and foundational evidence for using LLMs to support near real-time cognitive and affective analysis.

**Решение:** ? T1/T2 LLM scoring of student affect and cognition in math problem-posing vs human coders (kappa 0.82-0.85); check construct on full text

---

### 904 · R11357

**How Can I Improve? Using GPT to Highlight the Desired and Undesired Parts of Open-ended Responses**

2024 · A&A 687, A227 (2024) · conferencepaper/, text/article, preprint · https://doi.org/10.48550/arxiv.2405.00291

Automated explanatory feedback systems play a crucial role in facilitating learning for a large cohort of learners by offering feedback that incorporates explanations, significantly enhancing the learning process. However, delivering such explanatory feedback in real-time poses challenges, particularly when high classification accuracy for domain-specific, nuanced responses is essential. Our study leverages the capabilities of large language models, specifically Generative Pre-Trained Transformers (GPT), to explore a sequence labeling approach focused on identifying components of desired and less desired praise for providing explanatory feedback within a tutor training dataset. Our aim is to equip tutors with actionable, explanatory feedback during online training lessons. To investigate the potential of GPT models for providing the explanatory feedback, we employed two commonly-used approaches: prompting and fine-tuning. To quantify the quality of highlighted praise components identified by GPT models, we introduced a Modified Intersection over Union (M-IoU) score. Our findings demonstrate that: (1) the M-IoU score effectively correlates with human judgment in evaluating sequence quality; (2) using two-shot prompting on GPT-3.5 resulted in decent performance in recognizing effort-based (M-IoU of 0.46) and outcome-based praise (M-IoU of 0.68); and (3) our optimally fine-tuned GPT-3.5 model achieved M-IoU scores of 0.64 for effort-based praise and 0.84 for outcome-based praise, aligning with the satisfaction levels evaluated by human coders. Our results show promise for using GPT models to provide feedback that focuses on specific elements in their open-ended responses that are desirable or could use improvement. 11 pages, full research paper, EDM 2024

**Решение:** -4 educational learning feedback

---

### 905 · R6266

**Feasibility of human-in-the-loop multimodal generative artificial intelligence chatbot for school-based adolescent mental health support**

2026 · World Journal of Psychiatry · article · https://doi.org/10.5498/wjp.123904

BACKGROUND Schools often identify signs of emotional distress in adolescents before they access formal mental health services; however, many school counseling units lack the capacity to provide individualized support. Generative artificial intelligence (GenAI) chatbots may offer an accessible, low-threshold means of providing support. Nevertheless, their use among minors requires staff supervision, strong privacy protections, and clearly defined protocols for identifying and escalating risk-related content. AIM To evaluate the feasibility, user engagement, working alliance, safety monitoring workflow, and exploratory short-term outcome indicators of Duoduo, an acceptance and commitment therapy-informed multimodal GenAI chatbot developed for adolescents with elevated depressive symptoms. METHODS We conducted a prospective, non-randomized, controlled pilot study at a junior high school in Zhejiang Province, China. Students with elevated depressive symptoms were assigned to either an intervention group (n = 30) or a waitlist control group (n = 32). The intervention comprised eight supervised sessions delivered over two weeks. Feasibility outcomes included completion, engagement, working alliance, and predefined safety-monitoring indicators. Exploratory clinical outcomes were evaluated using baseline-adjusted analysis of covariance, with false discovery rate (FDR) correction applied for multiple comparisons. RESULTS Among the 30 students who initiated the intervention, 26 (86.7%) completed all scheduled sessions. Participants used the system for a mean total of 101.3 minutes. The mean Working Alliance Inventory-Short Revised score was 3.56 (SD = 0.86). Nine students triggered dangerous-behavior alerts, and school counselors conducted offline follow-up according to the established safety protocol. In the unadjusted analyses, nominal between-group differences were observed for anxiety and optimism. However, these differences were no longer evident after adjustment for baseline symptom severity and did not remain significant after FDR correction for multiple comparisons. No clinical outcome demonstrated a statistically significant between-group difference after adjustment. CONCLUSION Supervised school-based implementation of the chatbot was feasible and supports further evaluation in randomized controlled trials to determine its clinical effectiveness and safety.

**Решение:** -6 chatbot intervention feasibility for adolescent mental health

---

### 906 · R9851

**Determining the Role of Artificial Intelligence-Supported Applications in Reliability of Measurement Activities: Awareness and Precautions**

2025 · Uludağ Üniversitesi Eğitim Fakültesi Dergisi · journalarticle, article · en · https://doi.org/10.19171/uefad.1565847

This study aims to explore the role of artificial intelligence (AI)-supported applications in enhancing the reliability of online or face-to-face measurement activities. Using a case study design, a qualitative research method, the study gathered the opinions of 48 educators from various disciplines in schools affiliated with the Ministry of National Education and Higher Education. Data were collected using a semi-structured interview form consisting of four open-ended questions. The data were analyzed with the content analysis method and the Cohen’s kappa reliability coefficient was determined as k = .78, p < .05. The results revealed that nearly half of the educators were aware of AI-supported applications (such as ChatGPT, Bing, Copilot, etc.) and that some students used these applications to answer questions or prepare homework during the measurement process. In this context, the study identified various precautions that can be implemented to increase the reliability of online or face-to-face measurement activities. These precautions included conducting exams in person whenever possible, using interpretative questions, limiting exam durations, and focusing on practical exams. Additionally, educators can take steps such as recording screens during exams, capturing live images with cameras, and monitoring opened tabs to reduce the impact of AI-supported tools. The current study further discusses the influence of these measurement methods and precautions on increasing the reliability of measurement results.

**Решение:** -4 educational measurement awareness case study

---

### 907 · R5561

**Evidence of Limited Biases in Probed Language-based Assessments**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/zrb3v_v1

Large language models (LLMs) enable increasingly accurate language-based assessments (LBAs) of psychopathology. As these tools are more widely deployed in real-world settings, a critical question emerges: Do these tools work equally well for everyone? We examined whether probed LBAs, in which individuals respond to open-ended mental health questions in their own words, exhibit systematic biases that could undermine their clinical utility. We collected open-ended mental health descriptions from 1,260 participants alongside validated depression (PHQ-9) and anxiety (GAD-7) scores. We converted these descriptions to numeric representations using LLM-generated embeddings and applied ridge regression to predict symptom severity, achieving strong predictive accuracy (r &gt; .60). We then examined whether assessment differences were systematically associated with sociodemographic factors (gender, age, education, employment, income) or linguistic characteristics. Our analysis revealed limited evidence of demographic or linguistic bias: most variables showed minimal association with assessment errors (i.e., the absolute differences between the LBAs and self reports). However, higher depression and anxiety severity were associated with larger absolute assessment differences (standardized β = .193, p = .038; β = .252, p = .003). We explored mitigation strategies, finding that downsampling training data eliminated the bias for depression and anxiety. Our findings indicate that probed language-based assessments exhibit limited bias overall, particularly regarding sociodemographic equity. However, the observed severity-related pattern highlights a fundamental challenge.

**Решение:** -3 criterion validity: target is self-reported PHQ-9 and GAD-7 scores

---

### 908 · R4106

**Large Model Cue Injection Attack, Prison Break and Robustness Analysis**

2026 · Applied and Computational Engineering · journalarticle, article · https://doi.org/10.54254/2755-2721/2026.gu32247

The large language model is widely used and faces severe threat of prompt word injection attack. This paper systematically summarizes the classification, methods and corresponding defense mechanisms of cue injection attacks. According to the attack design method, the cue word injection is divided into two categories: manual design and algorithm generation. Manual design attacks include three typical techniques: cue obfuscation, virtual scene and logic induction; Algorithm generation attack focuses on the principles and characteristics of Greedy coordinate gradient (GCG), autoprompt and prompt engineering via zero shot (PEZ). On this basis, the current mainstream large language model prison break and security assessment data sets are sorted out, which are divided into four categories: prison break/attack prompt set, security boundary and refusal consistency, hazard theme coverage and value alignment, bias and multilingual security, and the core uses of each data set are analyzed. Finally, it points out the passivity and limitations of existing defense means, and points out that the future development direction should be from surface defense to internal security, from passive defense to active defense, so as to provide reference for building a more perfect large model security system.

**Решение:** -4 cybersecurity prompt injection and jailbreak

---

### 909 · R4237

**The AI-Augmented Product Manager: How Generative AI Is Reshaping Product Discovery, Strategy, and Execution**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6696358

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 business product management

---

### 910 · R4971

**Generative NLP Models for Mitigating Phishing Attacks**

2026 · Technix International Journal for Engineering Research · article · en · https://doi.org/10.56975/tijer.v13i5.162486

The rapid advancement and accessibility of generative Artificial Intelligence have empowered attackers to orchestrate sophisticated social engineering scams, with phishing remaining the primary vector for malicious distribution (Generative NLP Models for Mitigating Phishing Attacks, n.d.). Traditional defense mechanisms, including rule-based systems and conventional machine learning models, often fail to detect these contextually advanced threats as they rely on static patterns and lack the semantic understanding necessary to adapt to dynamic attack behaviors (Generative NLP Models for Mitigating Phishing Attacks, n.d.). Statistics indicate that 40% of AI-generated phishing emails target businesses, and 60% of recipients fall victim to these deceptive messages, a rate comparable to non-AI-generated attacks (Generative NLP Models for Mitigating Phishing Attacks, n.d.). To address these vulnerabilities, this research proposes an adaptive cybersecurity framework leveraging generative Natural Language Processing models, such as BERT and GPT, to identify complex linguistic patterns and contextual cues of malicious intent (Generative NLP Models for Mitigating Phishing Attacks, n.d.). The proposed methodology integrates generalization-based learning with adversarial training to strengthen the system's resilience against evolving and unknown attack strategies (Generative NLP Models for Mitigating Phishing Attacks, n.d.). A key contribution of this work is the development of a model capable of generating synthetic samples for training, thereby reducing the dependency on massive, manually annotated datasets (Generative NLP Models for Mitigating Phishing Attacks, n.d.). By facilitating real-time detection across various channels—including emails, fake websites, and multilingual chat-based conversations—this framework enhances proactive defense mechanisms and significantly reduces the potential for human error in an increasingly intricate digital landscape (Generative NLP Models for Mitigating Phishing Attacks, n.d.)

**Решение:** -4 cybersecurity phishing detection

---

### 911 · R12483

**Assessing the Effectiveness of ChatGPT in Simulating Client Role Play to Practice Counseling Skills**

2023 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/u2q69

The present study used qualitative content analysis research design to explore and assess the efficacy of ChatGPT, an artificial intelligence (AI) chatbot, in the facilitation of simulated client role play aimed at helping counselors in training (CITs) to practice counseling skills. The authors created 10 case vignettes, conducted a simulated role play with ChatGPT as the client. The qualitative content analysis of the session transcripts indicated that ChatGPT, as the simulated client, demonstrated commendable strengths. Its authentic portrayal of diverse client scenarios, nuanced emotional expressions, and empathetic responses indicate its potential as a valuable tool for CITs practicing counseling skills. The model's ability to maintain consistency throughout the role-play sessions, aligning with the provided case vignettes, underscored its reliability in simulating realistic counseling interactions. However, the study also revealed certain limitations, including occasional instances of inauthentic responses and temporary role confusion. Despite these limitations, the study supports the integration of ChatGPT into counseling education programs, emphasizing its role as a promising resource for enhancing the training experience of future counselors.

**Решение:** -6 client simulation for counselor training without coder agreement

---

### 912 · R0476

**Artificial Emotional Intelligence**

2026 · Business & Information Systems Engineering · article · en · https://doi.org/10.1007/s12599-026-01026-9

Artificial Emotional Intelligence (AEI) refers to Artificial Intelligence (AI) systems that mediate human affect by sensing, processing, and responding to emotional states through multimodal inputs, including text, voice, and physiological signals (Chen et al. 2024 ). As AI systems (especially generative AI) become more conversational, personalised, and multimodal, AEI increasingly mediates therapy, companionship, customer service, education, and work (De Freitas et al. 2026 ; Zao-Sanders 2026 ). This marks a shift from mediating information and behaviour to mediating affect in sensitive contexts: AEI already underpins chatbots designed to mitigate suicide risk (Maples et al. 2024 ), customer-service systems that respond to frustration (Fan et al. 2024 ), and personalised sexbot applications (Rubinsztein and Ciriello 2024 ). This shift reflects technical progress, but also intensifies concerns about social fragmentation, care-capacity gaps, and the expansion of monetisation-oriented platform logics into domains historically organised around care, trust, and professional duty (Arsel 2026 ; Leong et al. 2021 ; Seleznova et al. 2023 ). Despite its significance, this reconfiguration of digital intermediation remains under-conceptualised in Information Systems (IS) research.

**Решение:** -1 conceptual overview of artificial emotional intelligence

---

### 913 · R7308

**Supplementary Material - Recommendations for Efficient and Responsible LLM Adoption Within Industrial Software Development**

2025 · Zenodo · other/ · https://doi.org/10.5281/zenodo.15754264

This is a repository containing the supplementary material for the Journal submission titled "LLM Adoption Recommendations for Industrial Software Development Practices: A Multi-Case Study". It has 6 files in total: 3 interview questionnaires, 1 thematic analysis codebook, 1 survey questionnaire and 1 survey responses sheet.

**Решение:** -4 software engineering adoption

---

### 914 · R11184

**Inductive reasoning with large language models: a simulated randomized controlled trial for epilepsy**

2024 · medRxiv · preprint, ppr · https://doi.org/10.1101/2024.03.18.24304493

Importance The analysis of electronic medical records at scale to learn from clinical experience is currently very challenging. The integration of artificial intelligence (AI), specifically foundational large language models (LLMs), into an analysis pipeline may overcome some of the current limitations of modest input sizes, inaccuracies, biases, and incomplete knowledge bases. Objective To explore the effectiveness of using an LLM for generating realistic clinical data and other LLMs for summarizing and synthesizing information in a model system, simulating a randomized clinical trial (RCT) in epilepsy to demonstrate the potential of inductive reasoning via medical chart review. Design An LLM-generated simulated RCT based on a RCT for treatment with an anti-seizure medication, cenobamate, including a placebo arm and a full-strength drug arm, evaluated by an LLM-based pipeline versus a human reader. Setting Simulation based on realistic seizure diaries, treatment effects, reported symptoms and clinical notes generated by LLMs with multiple different neurologist writing styles. Participants Simulated cohort of 240 patients, divided 1:1 into placebo and drug arms. Intervention Utilization of LLMs for the generation of clinical notes and for the synthesis of data from these notes, aiming to evaluate the efficacy and safety of cenobamate in seizure control either with a human evaluator or AI-pipeline. Measures The AI and human analysis focused on identifying the number of seizures, symptom reports, and treatment efficacy, with statistical analysis comparing the 50%-responder rate and median percentage change between the placebo and drug arms, as well as side effect rates in each arm. Results AI closely mirrored human analysis, demonstrating the drug’s efficacy with marginal differences ( Conclusions and Relevance This study showcases the potential of LLMs accurately simulate and analyze clinical trials. Significantly, it highlights the ability of LLMs to reconstruct essential trial elements, identify treatment effects, and recognize reported symptoms, within a realistic clinical framework. The findings underscore the relevance of LLMs in future clinical research, offering a scalable, efficient alternative to traditional data mining methods without the need for specialized medical language training. Key Points Question Can large language models (LLMs) effectively simulate and analyze a randomized clinical trial, accurately summarizing and synthesizing clinical data to evaluate drug efficacy and identify relevant reported symptoms? Findings In a simulated study using LLMs to generate and analyze clinical notes for a trial comparing a drug to a placebo in epilepsy treatment, AI-driven analyses were found to closely match human expert evaluations. The process demonstrated the ability of LLMs to accurately capture treatment effects and identify reported symptoms, with minimal differences in outcomes between the human and LLM analyses. Meaning The use of LLMs in simulating and analyzing clinical trials offers a promising approach to developing inductive reasoning systems based on electronic medical records. This could revolutionize the way clinical trials are conducted and analyzed, enabling rapid, accurate assessments of therapeutic efficacy and safety without the need for specialized medical language training.

**Решение:** -4 somatic neurology (epilepsy trial simulation)

---

### 915 · R4712

**AI Genie**

2026 · Open Science Framework · article · https://doi.org/10.17605/osf.io/q6238

This OSF repository contains all materials, data, and code for the manuscript “AI‑GENIE: A Fully Automated Pipeline for In‑Silico Item Generation and Structural Validation Using Large Language Models and Network Psychometrics” (Russell‑Lasalandra, Christensen, & Golino, under review). What is AI‑GENIE? AI‑GENIE (Automatic Item Generation with Network‑Integrated Evaluation) is a fully automated framework that couples large language model (LLM) item generation with network psychometric reduction (EGA, UVA, and parametric bootstrap EGA). It produces psychometrically sound scales in silico, dramatically reducing the time and cost of traditional scale development. This repository includes: Supplementary materials (technical details, R code, full item pools, extended results) Figures (pipeline schematic, EGA network, bootstrap stability plot) Empirical datasets (anonymised) Human‑expert comparison data (items generated by five doctoral‑level personality psychologists) Corpus sample (1,000 published items used for the random‑generation control) Codebook (variable definitions and file structure) Analysis code (reproducible R scripts; also in Supplement A of the supplementary materials)

**Решение:** -6 automated psychometric item generation pipeline

---

### 916 · R6396

**Traceable Generative AI Workflow for Exhibit Product Design**

2026 · Proceedings of the 2nd International Conference on Artificial Intelligence and Product Design · book, conference, review · https://doi.org/10.1145/3829918.3829930

Generative AI can accelerate early-stage exhibition design by drafting storyboards, scripts, and motion prototypes. Yet in collaborative review, teams often cannot tell which details are supported by sources and which are added for narrative flow. We present a human-centric workflow that makes provenance explicit across multimodal prototypes. The workflow (1) organizes domain evidence in an evidence registry with stable EvidenceIDs, (2) uses field-structured prompts to carry evidence constraints across text, images, and motion, and (3) labels each narrative unit as grounded ({G}) or creative ({C}) with explicit EvidenceID references. We apply it to an evidence-rich exhibit prototype (two storyboards, two scripts, and two motion prototypes). In a small expert study, a historian and an exhibition designer rate evidence fidelity, narrative coherence, transparency/traceability, and design utility, and report plausibility concerns. While overall ratings are strong, initial scripts lacked explicit source pointers. Applying a lightweight Traceability Kit (unit tables and tags) makes EvidenceID references explicit for every script unit (28/28), allowing reviewers to locate unsupported or interpretive segments and iterate with an auditable evidence trail. We report pre/post traceability audit metrics for scripts, but we do not re-run the expert ratings after applying the kit; therefore, we treat these metrics as process measures rather than evidence of improved expert scores.

**Решение:** -4 product and exhibition design

---

### 917 · R8542

**DALE: Semantically Disentangled LoRA Expert Mixture for Depression Detection in Psychiatric Dialogue**

2025 · IEEE International Conference on Bioinformatics and Biomedicine (BIBM) · journalarticle, conference, conference-paper · https://doi.org/10.1109/bibm66473.2025.11356998

Major depressive disorder (MDD) is a significant global health burden; timely and precise diagnosis is essential to reduce relapse and mortality. However, existing approaches typically frame depression diagnosis as a monolithic classification problem, neglecting the multi-dimensional and hierarchical reasoning that underpins clinical interviews. We introduce DALE, a modular framework that mirrors psychiatrists'reasoning by explicitly disentangling four dimensions of patient narratives-psychological symptoms, somatic symptoms, protective factors and stressors. Leveraging GPT-4, we augment the dataset with dialogue-level annotations that map patient interview onto a list of attributes. On this auxiliary data, we train four domain-specialised LoRA adapters atop a frozen LLM; each adapter conducts a brief diagnostic dialogue and produces a concise report of its domain. A lightweight classifier then integrates these reports to generate a final summary and predict depression and suicide risk. Experiments on the D4 psychiatric dialogue benchmark show that DALE showing strong performance, while requiring far fewer trainable parameters, and yields interpretable, attribute-level evidence for its predictions.

**Решение:** -6 psychiatric dialogue classifier architecture using LLM for data augmentation

---

### 918 · R9311

**Is ChatGPT-40 Truly Ineffective at Trauma X-Ray Interpretation, or Does Machine Learning Simply Need More Practice?**

2025 · Journal of Emergency Medicine · article · en · https://doi.org/10.1016/j.jemermed.2025.02.024

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 somatic trauma radiology

---

### 919 · R8211

**MAGI: Multi-Agent Guided Interview for Psychiatric Assessment**

2025 · arXiv (Cornell University) · journalarticle, conference, preprint/article · en · https://doi.org/10.48550/arxiv.2504.18260

Automating structured clinical interviews could revolutionize mental healthcare accessibility, yet existing large language models (LLMs) approaches fail to align with psychiatric diagnostic protocols. We present MAGI, the first framework that transforms the gold-standard Mini International Neuropsychiatric Interview (MINI) into automatic computational workflows through coordinated multi-agent collaboration. MAGI dynamically navigates clinical logic via four specialized agents: 1) an interview tree guided navigation agent adhering to the MINI's branching structure, 2) an adaptive question agent blending diagnostic probing, explaining, and empathy, 3) a judgment agent validating whether the response from participants meet the node, and 4) a diagnosis Agent generating Psychometric Chain-of- Thought (PsyCoT) traces that explicitly map symptoms to clinical criteria. Experimental results on 1,002 real-world participants covering depression, generalized anxiety, social anxiety and suicide shows that MAGI advances LLM- assisted mental health assessment by combining clinical rigor, conversational adaptability, and explainable reasoning. In progress

**Решение:** ? T3 MAGI multi-agent MINI psychiatric interview assessment across 1,002 participants; check clinician agreement on full text

---

### 920 · R3180

**Can a Large Language Model Judge a Child's Statement?: A Comparative Analysis of ChatGPT and Human Experts in Credibility Assessment.**

2026 · Journal of evidence-based social work (2019) · comparative study, journal article, med · eng · https://doi.org/10.1080/26408066.2025.2547211

Purpose: This study investigates the inter-rater reliability between human experts (a forensic psychologist and a social worker) and a large language model (LLM) in the assessment of child sexual abuse statements. The research aims to explore the potential, limitations, and consistency of this class of AI as an evaluation tool within the framework of Criteria-Based Content Analysis (CBCA), a widely used method for assessing statement credibility. Materials and methods: Sixty-five anonymized transcripts of forensic interviews with child sexual abuse victims (N = 65) were independently evaluated by three raters: a forensic psychologist, a social worker, and a large language model (ChatGPT, GPT-4o Plus). Each statement was coded using the 19-item CBCA framework. Inter-rater reliability was analyzed using Intraclass Correlation Coefficient (ICC), Cohen’s Kappa (κ), and other agreement statistics to compare the judgments between the human-human pairing and the human-AI pairings. Results: A high degree of inter-rater reliability was found between the two human experts, with the majority of criteria showing “good” to “excellent” agreement (15 of 19 criteria with ICC >.75). In stark contrast, a dramatic and significant decrease in reliability was observed when the AI model’s evaluations were compared with those of the human experts. The AI demonstrated systematic disagreement on criteria requiring nuanced, contextual judgment, with reliability coefficients frequently falling into “poor” or negative ranges (e.g. ICC = -.106 for “Logical structure”), indicating its evaluation logic fundamentally differs from expert reasoning. Discussion: The findings reveal a profound gap between the nuanced, contextual reasoning of human experts and the pattern-recognition capabilities of the LLM tested. The study concludes that this type of AI, in its current, prompt-engineered form, cannot reliably replicate expert judgment in the complex task of credibility assessment. While not a viable autonomous evaluator, it may hold potential as a “cognitive assistant” to support expert workflows. The assessment of child testimony credibility remains a task that deeply requires professional judgment and appears far beyond the current capabilities of such generative AI models

**Решение:** + T1/T2 forensic CBCA coding of 65 child sexual abuse interview transcripts: ChatGPT (GPT-4o Plus) vs forensic psychologist and social worker, ICC & Cohen kappa (J Evid Based Soc Work 2026)

---

### 921 · R10407

**Trust in LLM-controlled Robotics: a Survey of Security Threats, Defenses and Challenges**

2025 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2601.02377

The integration of Large Language Models (LLMs) into robotics has revolutionized their ability to interpret complex human commands and execute sophisticated tasks. However, such paradigm shift introduces critical security vulnerabilities stemming from the ''embodiment gap'', a discord between the LLM's abstract reasoning and the physical, context-dependent nature of robotics. While security for text-based LLMs is an active area of research, existing solutions are often insufficient to address the unique threats for the embodied robotic agents, where malicious outputs manifest not merely as harmful text but as dangerous physical actions. In this work, we present a systematic survey, summarizing the emerging threat landscape and corresponding defense strategies for LLM-controlled robotics. Specifically, we discuss a comprehensive taxonomy of attack vectors, covering topics such as jailbreaking, backdoor attacks, and multi-modal prompt injection. In response, we analyze and categorize a range of defense mechanisms, from formal safety specifications and runtime enforcement to multi-LLM oversight and prompt hardening. Furthermore, we review key datasets and benchmarks used to evaluate the robustness of these embodied systems. By synthesizing current research, this work highlights the urgent need for context-aware security solutions and provides a foundational roadmap for the development of safe, secure, and reliable LLM-controlled robotics.

**Решение:** -1 review on security of LLM-controlled robotics

---

### 922 · R11873

**Cybersecurity in additive manufacturing: Investigating vulnerabilities and cyberattack mitigation strategies for connected 3D printers**

2024 · dissertation · en · https://doi.org/10.31274/td-20250502-35

The rapid adoption of additive manufacturing(AM), also known as 3D printing, in industrial production introduces critical cybersecurity challenges that threaten product integrity and manufacturing processes. Through an experimental testbed, this thesis investigates vulnerabilities in 3D printing systems, focusing on man-in-the-middle (MitM) attacks. Unauthorized modifications to printing parameters can substantially degrade product quality and structural integrity. Our research encompasses three core components: assessment of AM vulnerabilities, exploring potential attack vectors, and manufacturing system weaknesses. This thesis focuses on the development of a specialized testing environment for MitM attack simulation and enabling controlled analysis of security breaches. We then implement robust mitigation strategies for industrial applications, focusing on practical defense mechanisms. Our experiments reveal significant vulnerabilities in 3D printing workflows, particularly during data transmission and process validation. We propose two complementary security approaches: a real-time process monitoring framework leveraging point cloud data captured with depth cameras and an evaluation of Large Language Models (LLMs) for detecting compromised G-code. Our detection strategy complements traditional security measures with a lightweight solution suitable for resource-constrained devices. This research contributes theoretical insights into 3D printing vulnerabilities and practical solutions for manufacturing security.

**Решение:** -4 cybersecurity in 3D printing

---

### 923 · R7424

**QEVA: A Reference-Free Evaluation Metric for Narrative Video Summarization with Multimodal Question Answering**

2025 · Underline Science Inc. · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48448/zagb-pd42

Video-to-text summarization remains underexplored in terms of comprehensive evaluation methods. Traditional n-gram overlap-based metrics and recent large language model (LLM)-based approaches depend heavily on human-written reference summaries, limiting their practicality and sensitivity to nuanced semantic aspects. In this paper, we propose QEVA, a reference-free metric evaluating candidate summaries directly against source videos through multimodal question answering. QEVA assesses summaries along three clear dimensions: Coverage, Factuality, and Chronology. We also introduce MLVU(VS)-Eval, a new annotated benchmark derived from the MLVU dataset, comprising 800 summaries generated from 200 videos using state-of-the-art video-language multimodal models. This dataset establishes a transparent and consistent framework for evaluation. Experimental results demonstrate that QEVA shows higher correlation with human judgments compared to existing approaches, as measured by Kendall's $τ_b$, $τ_c$, and Spearman's $ρ$. We hope that our benchmark and metric will facilitate meaningful progress in video-to-text summarization research and provide valuable insights for the development of future evaluation methods. Accepted to Findings of EMNLP 2025

**Решение:** -4 video summarization metric

---

### 924 · R8891

**Effectiveness of generative AI-large language models' recognition of veteran suicide risk: a comparison with human mental health providers using a risk stratification model.**

2025 · Frontiers in psychiatry · journal article, journalarticle, article · eng · https://doi.org/10.3389/fpsyt.2025.1544951

Background: With over 6,300 United States military veterans dying by suicide annually, the Veterans Health Administration (VHA) is exploring innovative strategies, including artificial intelligence (AI), for suicide risk assessment. Machine learning has been predominantly utilized, but the application of generative AI-large language models (GAI-LLMs) remains unexplored. Objective: This study evaluates the effectiveness of GAI-LLMs, specifically ChatGPT-3.5, ChatGPT-4o, and Google Gemini, in using the VHA's Risk Stratification Table for identifying suicide risks and making treatment recommendations in response to standardized veteran vignettes. Methods: We compared the GAI-LLMs' assessments and recommendations for both acute and chronic suicide risks to evaluations by mental health care providers (MHCPs). Four vignettes, representing varying levels of suicide risk, were used. Results: GAI-LLMs' assessments showed discrepancies with MHCPs, particularly rating the most acute case as less acute and the least acute case as more acute. For chronic risk, GAI-LLMs' evaluations were generally in line with MHCPs, except for one vignette rated with higher chronic risk by the GAI-LLM. Variation across GAI-LLMs was also observed. Notably, ChatGPT-3.5 showed lower acute risk ratings compared to ChatGPT-4o and Google Gemini, while ChatGPT-4o identified higher chronic risk ratings and recommended hospitalization for all veterans. Treatment planning by GAI-LLMs was predicted by chronic but not acute risk ratings. Conclusion: While GAI-LLMs offers potential suicide risk assessment comparable to MHCPs, significant variation exists across different GAI-LLMs in both risk evaluation and treatment recommendations. Continued MHCP oversight is essential to ensure accuracy and appropriate care. Implications: These findings highlight the need for further research into optimizing GAI-LLMs for consistent and reliable use in clinical settings, ensuring they complement rather than replace human expertise.

**Решение:** + T3 veteran suicide risk recognition (VHA Risk Stratification): ChatGPT-3.5, ChatGPT-4o, Gemini vs mental health care providers on acute/chronic risk (Frontiers in Psychiatry 2025)

---

### 925 · R3292

**Mapping Practice-Based Signals of Generative AI in Psychiatric Care: Qualitative Study of Korean Psychiatrists' Experiences, Interpretations, and Implementation Priorities.**

2026 · Journal of medical Internet research · journal article, journalarticle, review · eng · https://doi.org/10.2196/96556

Abstract Background Generative artificial intelligence (GenAI) has increasingly entered psychiatric practice through patient-facing chatbots, self-help tools, and clinician-facing workflow support. Although prior research has examined clinicians’ attitudes, readiness, and anticipated use cases, less is known about how frontline encounters with GenAI shape psychiatrists’ interpretations and implementation priorities. Health care foresight also remains methodologically underdeveloped and has focused mainly on external signals, overlooking clinically consequential signals emerging from everyday practice. This gap is especially important in psychiatry, where GenAI-related benefits and harms may depend on patient vulnerability, crisis sensitivity, and the therapeutic relationship. Objective This study aims to qualitatively examine how South Korean psychiatrists described clinical experiences with GenAI, how they interpreted its roles and limits in psychiatric care, and what implementation priorities they emphasized. Selected concepts from horizon scanning informed the organization of the analysis by orienting attention to practice-based signals, interpretive patterns, and implementation priorities. Methods In this qualitative descriptive study, directed content analysis and codebook-based thematic synthesis were used to analyze responses to 3 open-ended survey questions administered to members of the Korean Neuropsychiatric Association. Invitations were distributed through the association’s official email system from October 27 to December 26, 2025. The qualitative analysis included respondents who provided an interpretable response to at least 1 item. The questions addressed (1) GenAI-related clinical experiences, (2) perceived advantages and limitations of GenAI relative to human therapists, and (3) priorities for the safe introduction of GenAI into mental health care. An exploratory participant-level cross-question thematic alignment analysis was also conducted to examine recurring adjacent-item pairings across the experience-interpretation-priority sequence. Results Of 408 total survey respondents, 311 respondents provided a meaningful response to at least 1 open-ended item. Psychiatrists described GenAI as a clinically ambivalent technology whose implications depended on context, intensity of use, and patient vulnerability. Practice-based signals clustered around patient-led use, clinician-led use, GenAI as a relational object, and GenAI-mediated changes in the patient-clinician interface, with high-risk and destabilizing scenarios cutting across these themes. Respondents viewed GenAI as potentially useful as an adjunct, but also as relationally limited and unacceptable as a replacement for human therapists. Implementation priorities centered on governance, crisis and vulnerability safeguards, technical reliability and clinical validation, and education, supervision, and structural readiness. Cross-question analysis suggested recurrent alignments between frontline signals, a view of GenAI as standardized and tireless but relationally thin, and governance- and validation-oriented implementation priorities. Conclusions In this qualitative descriptive study, GenAI emerged in psychiatric practice as an access tool, a workflow aid, and, at times, a competing interpretive reference point in clinical encounters. The key implementation challenge is therefore not whether psychiatry will encounter GenAI, but how its use should be bounded, supervised, and governed in light of patient vulnerability, psychiatric risk, and the relational demands of care.

**Решение:** -2 qualitative study of psychiatrists experiences with GenAI (human participants evaluated GenAI)

---

### 926 · R0824

**Mental health interventions: an integrated system based on generative artificial intelligence and virtual reality**

2026 · Virtual Reality · journalarticle, article · en · https://doi.org/10.1007/s10055-026-01474-4

Abstract Mental health interventions use therapeutic techniques to support emotional well-being, often leveraging emerging technologies to improve accessibility and effectiveness. In recent years, tools such as VR and AI have been increasingly used to create immersive and adaptive therapeutic experiences. This paper presents a framework that integrates generative artificial intelligence (GenAI) and virtual reality (VR) to enhance mental health interventions. The system allows for near real-time co-creation of three-dimensional objects during therapy sessions and provides a customizable “safe space”for emotional regulation. In a user study (n = 30), participants completed anxiety (GAD-7) and depression (PHQ-9) assessments, generated virtual objects linked to specific emotions, and rated the system’s usability (SUS) and recommendability (NPS). The framework achieved a high SUS score of 79 and an NPS of 40, indicating robust usability and willingness to recommend. Notably, neither anxiety nor depression levels, nor prior experience with VR or GenAI, significantly affected these measures. These findings highlight the feasibility and acceptability of combining GenAI and VR to offer immersive, personalized, and user-friendly therapeutic environments, representing a promising direction for future clinical validation in people-centered healthcare programs.

**Решение:** -6 system description of VR and AI mental health intervention

---

### 927 · R2278

**From unstructured text to structured reasoning: a hybrid knowledge graph for Indonesian sentencing analysis**

2026 · Artificial Intelligence and Law · article · en · https://doi.org/10.1007/s10506-026-09507-8

Abstract Indonesian court decisions contain rich legal knowledge about how judges interpret statutes, assess evidence, and determine sentences, yet much of this remains hidden in semi-structured, inconsistent documents. Rule-based systems fail on lengthy narratives, while machine learning models overfit to noise, and large language models risk factual errors. This study introduces a hybrid framework that combines rule-based extraction for structured sections with a BERT-based pipeline for narrative text. This framework was developed using a dataset of 9,109 narcotics and corruption cases; from this corpus, seven legal experts manually annotated 200 decisions. A relevance filter cleaned the text before entity extraction using fine-tuned LegalBERT. The entity extraction pipeline achieved an average F1-score of 84.39% across both domains (86.1% for corruption cases and 82.3% for narcotics cases), and the resulting knowledge graph enabled sentence length prediction with 85% accuracy, i.e., a 56.9% point improvement over full-text baselines that reached only 26–28% despite 95% training accuracy. This notable performance gap suggests that structured graph representations may better capture legally meaningful patterns that unstructured text alone tends to miss. Our study introduces what we believe is the first legal knowledge graph of Indonesian court decisions.

**Решение:** -4 legal sentencing analysis

---

### 928 · R12108

**Integrating Generative AI into Art Therapy: A Technical Showcase (Preprint)**

2024 · preprint · en · https://doi.org/10.2196/preprints.66328

BACKGROUND Mental health issues are prevalent and challenging both on a personal and societal level. Art therapy has been a recognized method of treatment, offering patients an expressive and non-verbal way to process emotions. With advancements in digital technologies, integrating artificial intelligence (AI) into therapeutic practices has the potential to enhance accessibility and effectiveness. However, the application of generative AI within art therapy remains underexplored, necessitating further investigation into its technical and ethical challenges. OBJECTIVE This study aims to develop and showcase a novel technical design that integrates generative AI into art therapy, specifically focusing on the use of text-to-image models. The goal is to provide a supportive tool that enhances patient expression and creative customization, while preserving the role of the therapist in guiding the therapeutic process. METHODS We define a simplified art therapy session process and demonstrate how it can be augmented with generative AI. Our technical implementation leverages edge detection, sketch-to-image models, and inpainting techniques to enable patients to refine their artwork through text prompts. We qualitatively evaluate the system using three illustrative examples: a digital sketch, a painted image, and a photograph of a sculpture. RESULTS The system successfully generated, refined and adapted versions of the exemplary artworks for all three cases, demonstrating its ability to maintain the essence of the original input. CONCLUSIONS The integration of generative AI into art therapy offers significant potential for enhancing accessibility and expressive possibilities for patients. While this proof-of-concept highlights technical feasibility, future research is required to assess therapeutic efficacy, user acceptance, and address ethical concerns, such as bias in AI-generated content. Our approach offers a foundation for further investigation into combining AI with traditional therapeutic practices, supporting the development of extended applications in clinical settings. Our implementations are publicly available at https://github.com/BFH-AMI/sds24.

**Решение:** -6 technical showcase of GenAI tool in art therapy without coder agreement

---

### 929 · R7475

**Algorithmic Aesthetics: Machine Learning for Reconstructing Poetic Imagination in English Literature**

2025 · International Conference on Science Technology Engineering and Mathematics (ICONSTEM) · conference, conference-paper · https://doi.org/10.1109/iconstem65670.2025.11374627

This study explores the application of machine learning techniques to reconstruct poetic imagination from English literary texts, bridging computational modeling with human creativity. The structure of the corpus through which the features of the Shakespearean and Sylvia Plath pieces are encoded accommodates structural peculiarities and aesthetic elements that are hybridized based on syntax, semantics, and poetic stylization with the help of hybrid embeddings. The transformer-based model is used to deduce the latent imaginative intent of metaphor, symbolism and tone. Moreover, such generative problems as line continuation, thematic transposition, or style mimicry are carried out with fine-tuned large language models. The explainable AI methods utilizing Lisp machine interpretation are incorporated so that the features could be highlighted to drive imaginative reconstructions. The outcomes show that the model performs well with regard to several measures. The Imaginative Fidelity Score (IFS) ranged at an average of 0.89 and the averages of the affective match between the categories of emotion were at 87%. The average score of $4.47 / 5$ based on human judgments was on imaginative authenticity and stylistic coherence. Also, thematic transpositions maintained symbolic mapping at an accuracy of more than 90.6% on more complex transitions such as the mapping of Loss to Transformation. This overlap of the fields of computational linguistics and poetic aesthetics creates opportunities in AI-assisted literary criticism, creative writing, and affective computing. The system proposed does not just analyze the poetic texts but also adds to them being a co-creator of the literary exploration. The project could be extended in the future to incorporate cross-lingual poetic re-construction, the inclusion of multimodal metaphors and modeling cultural or historical context to add additional layers to imaginative expressions. The results highlight how subtle human creativity can be represented by the aesthetic of algorithms, to which education, digital humanities, and literary AI applications are relevant.

**Решение:** -4 literary analysis of poetry

---

### 930 · R4649

**The Effects of AI-Guided Exercise and a Smart Ring on Arterial Stiffness (GONDOR-AS): protocol for a randomized controlled trial**

2026 · medRxiv · preprint, ppr · https://doi.org/10.64898/2026.03.19.26348812

Background: Cardiovascular disease (CVD) prevention is limited by the major challenge of low long-term adherence to effective lifestyle regimens. Arterial stiffness (measured by carotid-femoral pulse wave velocity, cfPWV) and maximal cardiorespiratory fitness (measured by VO2max), are modifiable risk factors for CVD but require sustained lifestyle change. Wearable technology provides continuous measurement and offers a scalable platform to deliver health interventions. A combination of continuous monitoring with a wearable device and an artificial intelligence (AI) -based coach personalized for individual data and preferences could be a powerful, low-barrier tool for achieving sustainable cardiovascular health benefits by directly addressing the adherence challenge. Objective: We will study the comparative effectiveness of a wearable and an interactive app-based AI coaching intervention promoting moderate exercise on improving gold-standard cfPWV and VO2max. This will be compared to a supervised high-intensity interval training (HIIT) group (benchmark with known benefits for VO2max) and a control group using only Oura Ring (passive monitoring). We will also conduct a detailed Process Evaluation (structured interviews) to study the feasibility and experience of interacting with the AI coach. Methods: This randomized controlled trial recruited 165 eligible sedentary participants aged 30-65 years. Co-primary outcomes cfPWV and VO2max were measured at baseline and will be repeated after 12 weeks. Participants were equally randomized into three groups: an AI-based coaching group (steady-state exercise), a HIIT group (supervised exercise) and a control group (usual low activity). The AI-based coaching group receives personalized guidance using large language model (LLM) technology. All participants wear Oura Ring and are blinded to cardiovascular health metrics provided by the ring. Results: The recruitment for the study began in October 2024 and will end when 165 men and women have been recruited. Data collection for the study is scheduled to conclude early 2026. Data collection is ongoing. Conclusions: This study will evaluate if a highly scalable, AI-based coaching intervention can achieve comparable gains in CV structural health (cfPWV) and functional capacity VO2max relative to a resource-intensive supervised HIIT benchmark. The findings will provide essential evidence on the use of digital health tools to promote sustainable exercise adherence. ClinicalTrials.gov registration identifier: NCT06644014 (Registered: 2024-10-15) Keywords: cardiovascular age; arterial stiffness; pulse wave velocity; artificial intelligence; high-intensity interval training; randomized controlled trial; study protocol

**Решение:** -1 RCT protocol on arterial stiffness in cardiology

---

### 931 · R2464

**Processes in psychotherapy: A scoping review with LLM-assisted clustering.**

2026 · Clinical psychology review · journalarticle, review, scoping review · eng · https://doi.org/10.1016/j.cpr.2026.102782

BACKGROUND: Clinical psychological science has shown limited progress in improving treatment efficacy, refining intervention models, and identifying processes of change, that are traditionally associated with common factors (such as therapeutic alliance and empathy). OBJECTIVE: To examine research trends on this topic, we systematically surveyed the literature for studies that examine processes of change in the context of psychological interventions. METHODS: A total of 778 studies reported on 684 processes of therapeutic change since 2007. Using an iterative, AI-assisted human-in-the-loop clustering procedure, these processes were subsequently organized into 32 process clusters using OpenAI's GPT-5 nano model. RESULTS: The largest process cluster identified concerned common factors (i.e., therapeutic alliance and collaborative processes, and interpersonal functioning), accounting for 20.6% of all investigated processes of change. The remaining processes were primarily associated with specific factors related to cognitive behavioral therapy, such as cognitive appraisal and belief change processes. The research focus and number of studies on therapeutic processes have not changed substantially over the years. CONCLUSION: Despite urgent calls to improve our understanding of therapeutic processes, the focus and volume of research have remained unchanged, with the primary focus remaining on common factor processes.

**Решение:** -1 scoping review of psychotherapy processes with LLM-assisted literature clustering

---

### 932 · R4623

**The Language of Affect Heuristic in Online Discourse: A Corpus Study with Human and Llm Coders**

2026 · Człowiek i Społeczeństwo · journalarticle, article, journal-article · pl · https://doi.org/10.14746/cis.2026.61.8

This paper investigates the affect heuristic in online argumentative discourse through a corpus-based study combining manual and automatic annotation. Drawing on research in argumentation theory, psychology, and decision science, the study approaches affect not as an external addition to reasoning but as a recurring component of evaluative judgment. The analysis focuses on discussions of climate change and artificial intelligence collected from Reddit and X (formerly Twitter), domains characterised by uncertainty, risk perception, and public controversy. The study employs a bottom-up annotation methodology in which four human annotators identify instances of affect heuristic and related cognitive biases in a corpus of more than 30,000 posts and comments. Inter-annotator agreement is assessed using Fleiss’ κ, Cohen’s κ, Gwet’s AC1, and weighted F1 measures. In a second stage, the same annotation scheme is applied to GPT-4o, treated as a constrained fifth annotator operating within predefined categories and probabilistic classification rules. The results show that the affect heuristic is the most frequent heuristic pattern in the corpus, occurring more often than confirmation bias, availability heuristic, or representativeness heuristic. Although traditional κ coefficients remain low because of category imbalance, agreement measures robust to prevalence effects indicate substantial consistency among annotators. The automatic annotation stage reveals partial alignment between human and model judgments, while also exposing systematic discrepancies in the model’s distribution of categories. A lexical and discursive analysis further demonstrates that affect heuristics do not necessarily manifest through explicit emotion vocabulary. Instead, they frequently appear through evaluative framing, practical reasoning under uncertainty, and subtle stance-taking related to collective action and future-oriented judgment. The findings contribute to empirical research on emotional processes in argumentation and demonstrate how affective reasoning can be operationalised and studied through combined qualitative and computational methods.

**Решение:** + T1 affect heuristic and cognitive biases coding on 30k posts: GPT-4o vs 4 human annotators, Fleiss kappa, Cohen kappa, Gwet AC1, weighted F1 (Czlowiek i Spoleczenstwo 2026)

---

### 933 · R5795

**AI Systems for Qualitative Data Interrogation (EpiChat) and Semi-Automated Coding (EpiCode)**

2026 · Zenodo (CERN European Organization for Nuclear Research) · text/poster, article · https://doi.org/10.5281/zenodo.23234705

Background: The Virage project collected approximately 800 one-hour interviews on rabies awareness, including transmission, disease progression, and vaccination. Manually searching, comparing, and coding this corpus would require substantial time and human resources. Objective: EpiChat and EpiCode were developed using large language models (LLMs) to support natural-language interrogation and thematic analysis of interview transcripts. Local LLMs were used to preserve data privacy, avoid sharing data with foreign cloud services, and eliminate token and subscription costs. Methods: EpiChat uses an LLM-based router to direct questions to three specialized pipelines. An SQL pipeline translates structured metadata questions into database queries. For questions regarding counts or proportions, a map-reduce pipeline examines each interview independently and aggregates the results. Explanatory questions are handled using Retrieval-Augmented Generation (RAG). Because conventional RAG retrieves only the highest-ranked passages across the corpus, it may overlook rare perspectives that are important to qualitative research. To address this, EpiChat introduces a deep search mode that formulates the question as a quotation and searches for it into each interview. Verified quotations from matching interviews are then combined into a single response with source citations. EpiCode supports qualitative coding by matching transcript segments to a two-level codebook of main codes and subcodes. Each suggested code includes a model-generated confidence score, supporting quotation, and brief rationale. When no existing code adequately represents the content, the system proposes a new code. All suggestions require researcher review and approval. Results: Preliminary runtime measurements showed that EpiChat processed an interview-level query in approximately four seconds per interview, while EpiCode generated code suggestions for an entire interview in around three minutes. Conclusion: EpiChat and EpiCode provide a privacy-preserving, locally deployed platform for AI-assisted qualitative analysis. Future work will compare AI-generated codebooks with human-developed codebooks and evaluate whether EpiChat produces answers consistent with findings derived from manual coding. Poster presented at the Pasteur Network Annual Meeting (PNAM 2026), Laval, Canada, 3–5 November 2026.

**Решение:** -4 qualitative coding of rabies awareness interviews (infectious disease epidemiology)

---

### 934 · R1807

**Identifying and Representing Knowledge Delta in Scientific Literature Identifikation und Darstellung von Wissensdeltas in wissenschaftlicher Literatur**

2026 · TU Wien · text/dissertation · https://doi.org/10.34726/hss.2026.140233

The process of continuously keeping up to date with the state-of-the-art on a specific research topic is a challenging task for researchers, not least due to the rapid increase in published research. While existing tools, such as scholarly search engines or citation graphs, can help find related articles, they often fail to highlight the factual differences between papers that address the same research problem. As a result, identifying what is new or different in a given article remains a challenge. This is particularly important for writing surveys, conducting literature reviews, or evaluating the novelty of a contribution. In this thesis, we address this problem by introducing the concept of the Knowledge Delta(K∆), which refers to the factual differences between related scientific articles, and improve informativeness, particularly for long summaries. On the TalkSumm dataset, argumentative structure enhance summary quality, while on CL-SciSumm, abstract- based methods perform best, reflecting the close alignment between human-written short summaries and abstract content. For the second step, we explore different approaches for representing the extracted factual knowledge. We use Large Language Models, including GPT-4o, GPT-4o-mini, LLaMA3.1-8B, and LLaMA3.1-70B, to represent each of the research task, method, dataset, and results of each article. These representations are produced using designed prompts and are guided by either the full article or the AZ-extracted summaries. These representations are evaluated using the downstream task of Narrative Knowledge Delta (NK∆) generation. which focuses on identifying differences between pairs of scientific articles that tackle theFor the final step, we introduce the task of Narrative Knowledge Delta (NK∆) generation, same research problem, presented in a narrative form. We create two small, manually annotated datasets, one based on interviews with researchers and another based on a survey paper, to serve as ground truth. In addition, we construct a large-scale synthetic dataset using existing scientific annotations to serve as examples for LLM prompts in few-shot settings. To evaluate NK∆ outputs automatically, we apply the scientific fact- checking model MultiVerS to assess the LLM-generatedannotated claims. The results show that structured prompting, combined with examplesNK∆ sentences against manually from the synthetic data, improves the factual accuracy of generated comparisons.wepropose a method for automatically identifying and representing these differences. We define a specific form of Knowledge Delta called the Narrative Knowledge Delta(NK∆), which captures how a pair of scientific articles differ in terms of their researchtasks, methods, datasets, and results. We formulate three research questions that guide this work: how to extract factual knowledge from scientific articles, how to represent it in a structured way, and how to compare and evaluate the differences between articles. Based on these questions, we design a three-step methodology. First, we use Argumentative Zoning (AZ) to detect regions within a scientific article that cover the main components of an article (i.e. factual knowledge). Second, we represent the extracted knowledge using Large Language Models (LLMs) through structured prompts and templates to generateNK∆. Third, we evaluate the generated NK∆ using a scientific fact-checking model, MultiVerS, to assess the correctness of the comparisons against the original documents.To support the first step of the pipeline, we develop an AZ annotation platform that allows annotators to label rhetorical zones in full scientific articles. This tool aims to address the lack of existing AZ datasets at the full-paper level and handles the complexity of the annotation task. Using this tool, we conduct two rounds of annotation, both online and offline, with Master’s and Bachelor’s students and created a corpus of AZ- labeled articles focused on NLP and text mining. We also train a BERT-based classifier to automatically identify AZ zones. Our results show that high-quality annotations significantly improve model performance compared to a BERT model trained on a baseline corpus. Additionally, as a downstream task, we use the AZ-trained model in a scientific summarization pipeline. We experiment on two scientific summarization datasets: TalkSumm and Cl-SciSumm. Our experiments reveal that AZ-based approaches

**Решение:** -4 scientific literature informatics

---

### 935 · R4291

**Using AI to Detect Motivation : Inferring Author’s Basic Psychological Need Satisfaction with a Large Language Model from Workplace Appreciation Texts with Human and AI Participants**

2026 · Diva portal (Dalarna University Library) · dissertation · en · http://urn.kb.se/resolve?urn=urn:nbn:se:su:diva-257792

Large language models (LLMs) offer a scalable alternative to self-reported questionnaires for assessing psychological constructs from natural language text, yet their validity for inferring motivation-related states remains untested. This study examined whether LLM-inferred authors’ Basic Psychological Need Satisfaction (BPNS) scores derived from workplace appreciation texts converge with self-reported questionnaire scores, and whether AI surrogates can serve as a methodological tool for stress-testing how text amount affects this convergence. Human participants (N = 132) were Swedish-speaking employed adults who wrote three workplace appreciation texts of at least 50 words. AI surrogates (N = 394) were LLM-generated profiles drawn from a US-population-representative repository that produced appreciation texts varying systematically in length and number. Both samples completed a BPNS questionnaire. An LLM scored all texts for BPNS dimensions Autonomy, Competence, and Relatedness using a fixed zero-shot prompt. For human participants, LLM-inferred scores showed a small positive but fragile correlation for Autonomy only (r = .19), with Competence and Relatedness near zero, diverging from the three-dimensional structure of self-reported scores. For AI surrogates, LLM-inferred scores showed weak correlations in the human-matched condition (r = .07−.09) and also diverged from the three-dimensional structure of self-reported scores for BPNS. Text amount did not systematically improve convergence. These findings suggest that the appreciation text genre carries insufficient signal about the author’s BPNS state, pointing to a construct-genre mismatch rather than LLM capability failure. LLM-based BPNS scoring from appreciation texts is not yet ready for organizational use. AI surrogates show preliminary feasibility as a stress test instrument, contingent on structural-convergence checks against human samples.

**Решение:** -3 criterion validity: target is self-reported BPNS questionnaire scores

---

### 936 · R12213

**Humanlike Cognitive Patterns as Emergent Phenomena in Large Language Models**

2024 · arXiv (Cornell University) · journalarticle, review, preprint/article · en · https://doi.org/10.48550/arxiv.2412.15501

Research on emergent patterns in Large Language Models (LLMs) has gained significant traction in both psychology and artificial intelligence, motivating the need for a comprehensive review that offers a synthesis of this complex landscape. In this article, we systematically review LLMs' capabilities across three important cognitive domains: decision-making biases, reasoning, and creativity. We use empirical studies drawing on established psychological tests and compare LLMs' performance to human benchmarks. On decision-making, our synthesis reveals that while LLMs demonstrate several human-like biases, some biases observed in humans are absent, indicating cognitive patterns that only partially align with human decision-making. On reasoning, advanced LLMs like GPT-4 exhibit deliberative reasoning akin to human System-2 thinking, while smaller models fall short of human-level performance. A distinct dichotomy emerges in creativity: while LLMs excel in language-based creative tasks, such as storytelling, they struggle with divergent thinking tasks that require real-world context. Nonetheless, studies suggest that LLMs hold considerable potential as collaborators, augmenting creativity in human-machine problem-solving settings. Discussing key limitations, we also offer guidance for future research in areas such as memory, attention, and open-source model development.

**Решение:** -1 review on emergent cognitive patterns in LLMs

---

### 937 · R5507

**Generative AI for Early Detection of Depression Using Multimodal Data: A Review**

2026 · Eagle Leap Publication · journalarticle/ · https://doi.org/10.5281/zenodo.23535783

Depression is a major mental-health condition that affects emotion, behaviour, communication and daily functioning, and its early identification remains a significant challenge for both clinicians and researchers. Conventional assessment relies mainly on clinical interviews and self-report instruments such as the PHQ and BDI, which are subjective and dependent on the willingness and ability of an individual to accurately report symptoms. Advances in Generative Artificial Intelligence (GenAI), deep learning and multimodal data fusion have opened new possibilities for analysing text, audio, video and behavioural signals together to support early depression-risk detection. This paper presents a structured review of recent literature on multimodal and Generative-AI-based approaches for depression detection, tracing the progression from traditional machine-learning techniques to deep-learning, transformer-based and generative architectures. Eight representative studies are analysed and compared in terms of methodology, key findings and limitations. Based on this synthesis, key research gaps are identified, including limited integration of GenAI with rich multimodal information, scarcity of large and diverse real-world datasets, generalization difficulties, GenAI reliability concerns and privacy and ethical issues associated with sensitive mental-health data. A conceptual multimodal GenAI framework that combines text, audio, video and behavioural indicators while addressing reliability, privacy and explainability is subsequently outlined as a direction for future work.

**Решение:** -1 review on GenAI for depression detection using multimodal data

---

### 938 · R5509

**PsyProbe: Proactive and Interpretable Dialogue through User State Modeling for Exploratory Counseling**

2026 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.18653/v1/2026.findings-eacl.336

Recent advances in large language models have enabled mental health dialogue systems, yet existing approaches remain predominantly reactive, lacking systematic user state modeling for proactive therapeutic exploration. We introduce PsyProbe, a dialogue system designed for the exploration phase of counseling that systematically tracks user psychological states through the PPPPPI framework (Presenting, Predisposing, Precipitating, Perpetuating, Protective, Impact) augmented with cognitive error detection. PsyProbe combines State Builder for extracting structured psychological profiles, Memory Construction for tracking information gaps, Strategy Planner for Motivational Interviewing behavioral codes, and Response Generator with Question Ideation and Critic/Revision modules to generate contextually appropriate, proactive questions. We evaluate PsyProbe with 27 participants in real-world Korean counseling scenarios, including automatic evaluation across ablation modes, user evaluation, and expert evaluation by a certified counselor. The full PsyProbe model consistently outperforms baseline and ablation modes in automatic evaluation. User evaluation demonstrates significantly increased engagement intention and improved naturalness compared to baseline. Expert evaluation shows that PsyProbe substantially improves core issue understanding and achieves question rates comparable to professional counselors, validating the effectiveness of systematic state modeling and proactive questioning for therapeutic exploration. In Findings of the Association for Computational Linguistics: EACL 2026

**Решение:** -6 dialogue system architecture for exploratory counseling without coder agreement

---

### 939 · R0562

**AI-Driven Iatrogenesis: Risks of Using Generative AI for Mental Health Support**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7539820

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 perspective on risks and iatrogenesis of GenAI in mental health

---

### 940 · R4004

**A Systematic Evaluation of LLM Security in Cloud Environments: Failure Modes in Malicious URL and Jailbreak Detection**

2026 · 2026 11th International Conference on Cloud Computing and Big Data Analytics (ICCCBDA) · conference · https://doi.org/10.1109/icccbda69573.2026.11676536

The widespread deployment of large language models (LLMs) in cloud environments has introduced substantial security challenges across the entire service pipeline, primarily due to their exposure to open-ended user inputs and external interactions. Existing defense approaches-including rule-based filtering, machine learning classifiers, and reasoningbased models-struggle to balance detection effectiveness, latency, and operational cost, thereby limiting their practicality in real-world systems. This study presents a systematic evaluation of a heuristicbased security framework (Model Armor v1.0) using a unified evaluation pipeline and three large-scale public datasets (over 1.1 million samples) covering URL legitimacy classification, malicious URL detection, and LLM jailbreak attacks, comprising over 1.1 million samples in total. A unified evaluation pipeline is developed, incorporating sample routing, multilayer heuristic detection, and standard performance metrics, including accuracy, precision, recall, and F1-score. Experimental results indicate that although the framework achieves a moderate accuracy of 70.43%, its recall is critically low at 3.93%, resulting in 96.07% of threats remaining undetected. Detection performance is highly imbalanced, with nearcomplete failure in identifying malicious URLs and jailbreak attacks. Furthermore, a substantial number of false positives leads to operational inefficiencies. These findings suggest that static heuristic-based methods lack robustness against complex and evolving attack patterns. This work highlights fundamental limitations in current LLM security frameworks and underscores the need for adaptive, multi-layered, and semantically aware defense mechanisms to ensure secure and scalable cloud deployment.

**Решение:** -4 cybersecurity URL and jailbreak detection

---

### 941 · R6836

**HydroAgent: Closing the Gap Between Frontier LLMs and Human Experts in Hydrologic Model Calibration via Simulator-Grounded RL**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.17792

Calibrating distributed hydrologic models is a critical bottleneck across operational water resources management - streamflow prediction, reservoir operation, drought monitoring, infrastructure design, and flood forecasting all depend on it. Each basin demands an expert to translate hydrograph signatures into adjustments of a high-dimensional parameter vector, and the resulting workflow does not transfer between watersheds. We ask: can frontier large language model (LLM) agents replace the human hydrologic modeler, and if not, what would it take? We benchmark nine frontier LLM agents - Claude Opus 4.6/4.7, Sonnet 4.6, GPT-5/5.4/5.4-pro, and Gemini 2.5-pro/3.1-pro/3-flash - on the operational CREST distributed hydrologic model used by the U.S. National Weather Service for flash-flood forecasting. Best-of-twenty-rounds Nash-Sutcliffe Efficiency (NSE) across four held-out gauges spanning 329-40,792 km2 ranges from -0.16 (GPT-5.4) to 0.75 (Sonnet 4.6); the ceiling reproduces across all three vendors and capability tiers, with the strongest models concentrating in the 0.65-0.75 band, and no model reaches the human-expert reference except Opus-4.7 on one gauge. We argue this gap is not a parameter-count problem but a domain-grounding problem. We then propose HYDROAGENT, fine-tuning open-weight Qwen3-4B with supervised fine-tuning on 2,576 expert calibration trajectories and Group-Relative Policy Optimization using NSE as a verifiable reward from online CREST simulations - reinforcement learning with simulation feedback (RLSF). For Earth system science, a small domain-tuned policy with simulator-in-the-loop RL is a more compute-efficient and physically faithful path than scaling generic frontier models, and the multi-modal richness of Earth data - remote sensing, in-situ time series, and forecaster narrative - makes domain agents a leveraged direction for AI in physical science.

**Решение:** -4 hydrology and water resources modeling

---

### 942 · R1952

**The co-analyst in the loop: Claude’s affordances for applied linguistics research methods**

2026 · Research Methods in Applied Linguistics · article · en · https://doi.org/10.1016/j.rmal.2026.100382

Applied linguistics is being transformed less by “artificial intelligence” in the abstract than by the concrete affordances of specific large language models (LLMs) acting on its research-methods lifecycle. This paper is a narrative, tutorial-style methodological review advancing a model-specific, affordance-based account of how Anthropic’s Claude can support applied-linguistics research across design, data collection, transcription, coding, analysis, and reporting. It is not a systematic synthesis in the sense of Chong and Plonsky (2024); we specify our source-selection procedure and claim no exhaustive coverage. Against a tendency to treat LLMs as an undifferentiated category typified by ChatGPT and evaluated mainly as productivity aids, we reconceptualize Claude as a co-analyst in the loop: a configurable participant whose decisions can be made auditable. We identify, and explain how we derived, four affordances useful for method: extended-context document grounding, behavioural steerability, rationale-exposing output, and agentic tool use. Through worked examples—including one grounded in real interview data with a computed reliability figure—we demonstrate their application to instrument design, elicitation, transcription, coding, rating, and synthesis, using Claude as an example of a broader class rather than a uniquely capable system. We are explicit about limits: a stated rationale is not a faithful trace of internal computation, and LLMs remain only partially interpretable. We specify a human–machine analytic loop with reliability procedures addressing session-to-session variability and cross-session carryover. Claude’s contribution, we argue, is to turn tacit judgements into inspectable procedures, repositioning the human expert toward auditing and adding auditability to—not replacing—existing criteria of agreement, reliability, and construct validity.

**Решение:** -1 tutorial and methodological narrative on Claude in applied linguistics

---

### 943 · R9446

**Prompting the Priorities: A First Look at Evaluating LLMs for Vulnerability Triage and Prioritization**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2510.18508

Security analysts face increasing pressure to triage large and complex vulnerability backlogs. Large Language Models (LLMs) offer a potential aid by automating parts of the interpretation process. We evaluate four models (ChatGPT, Claude, Gemini, and DeepSeek) across twelve prompting techniques to interpret semi-structured and unstructured vulnerability information. As a concrete use case, we test each model's ability to predict decision points in the Stakeholder-Specific Vulnerability Categorization (SSVC) framework: Exploitation, Automatable, Technical Impact, and Mission and Wellbeing. Using 384 real-world vulnerabilities from the VulZoo dataset, we issued more than 165,000 queries to assess performance under prompting styles including one-shot, few-shot, and chain-of-thought. We report F1 scores for each SSVC decision point and Cohen's kappa (weighted and unweighted) for the final SSVC decision outcomes. Gemini consistently ranked highest, leading on three of four decision points and yielding the most correct recommendations. Prompting with exemplars generally improved accuracy, although all models struggled on some decision points. Only DeepSeek achieved fair agreement under weighted metrics, and all models tended to over-predict risk. Overall, current LLMs do not replace expert judgment. However, specific LLM and prompt combinations show moderate effectiveness for targeted SSVC decisions. When applied with care, LLMs can support vulnerability prioritization workflows and help security teams respond more efficiently to emerging threats. 19 pages, 8 figures

**Решение:** -4 software engineering vulnerability triage

---

### 944 · R12743

**Decoding Methods for Neural Narrative Generation**

2021 · IEEE Games Entertainment Media Conference · audiovisual/conference talk, journalarticle, preprint/article · en · https://doi.org/10.18653/v1/2021.gem-1.16

Narrative generation is an open-ended NLP task in which a model generates a story given a prompt. The task is similar to neural response generation for chatbots; however, innovations in response generation are often not applied to narrative generation, despite the similarity between these tasks. We aim to bridge this gap by applying and evaluating advances in decoding methods for neural response generation to neural narrative generation. In particular, we employ GPT-2 and perform ablations across nucleus sampling thresholds and diverse decoding hyperparameters -- specifically, maximum mutual information -- analyzing results over multiple criteria with automatic and human evaluation. We find that (1) nucleus sampling is generally best with thresholds between 0.7 and 0.9; (2) a maximum mutual information objective can improve the quality of generated stories; and (3) established automatic metrics do not correlate well with human judgments of narrative quality on any qualitative metric. 20 pages. Updated to the accepted version in Workshop on Generation Evaluation and Metrics at ACL 2021 (GEM'21)

**Решение:** -4 computational linguistics narrative generation

---

### 945 · R6846

**Disagreement-Driven Joint Refinement of Retrieval and Decision Rules for Imbalanced Counseling Risk Classification**

2026 · Language Resources and Evaluation Conference (LREC) · conference, review, conference-paper · https://doi.org/10.63317/2f8zttankw7p

With the rapid growth of online counseling services, timely and reliable risk classification of counseling records is essential for supporting early screening and prioritizing limited intervention resources. High-risk samples refer to high-acuity suicide risk and require expedited human review. However, this task is challenging due to severe class imbalance (93% low-risk and 7% high-risk samples) and complex decision boundaries. Large language models (LLMs) exhibit unstable predictions and systematic errors in such imbalanced clinical-text settings. To address this issue, we propose Disagreement-Driven Joint Refinement (DDJR), an iterative, parameter-free refinement framework. It uses prediction disagreement between two inference settings, zero-shot and retrieval-augmented in-context learning, as the primary signal for identifying high-value instances. These disagreement-identified instances are transformed into adaptive refinement signals and used to jointly update both the exemplar pool and an executable rule set, thereby sharpening decision boundaries and improving prediction stability. Experiments on 6,481 real-world counseling records demonstrate that the proposed DDJR outperforms existing methods, achieving an accuracy of 0.915 and a Matthews Correlation Coefficient (MCC) of 0.583. These results demonstrate that DDJR achieves more stable and reliable predictions for high-stakes counseling risk classification in real-world settings.

**Решение:** ? T3 counseling records suicide risk classification with LLM (DDJR) on 6,481 records; check human rater reference standard on full text

---

### 946 · R4280

**Strategic war narrative of president Zelenskyy and its effect on the persuasion of foreign audiences during the Russo-Ukrainian war 2022-2025 : dissertation to obtain the degree of Doctor of Philosophy**

2026 · Electronic Kyiv-Mohyla Academy Institutional Repository (National University of Kyiv-Mohyla Academy) · dissertation · uk · https://ekmair.ukma.edu.ua/bitstreams/32396c86-8d65-4b1d-a762-53691c78cca0/download

PhD thesis to obtain the degree of Doctor of Philosophy in the Programme Subject Area 061 "Journalism" (06 — Journalism). — National University of Kyiv-Mohyla Academy, Kyiv, 2026. The dissertation presents a comprehensive analysis of the construction, evolution, and functional dynamics of President V. Zelenskyy's strategic war narrative during the Russo-Ukrainian war of 2022–2025. Strategic war narrative is examined as a central instrument of external communication aimed at reshaping the global perception of the war, mobilizing and sustaining international support, and influencing Western partners' decisions on vital military-political assistance to Ukraine. The narrative architecture is modelled as a three-level structure (archetypal-plot, emotional, and genre-stylistic levels); the model's uniqueness is substantiated, its transformation is traced across the four phases of the war; and key mechanisms of persuading Western elites and publics are identified. Beyond reconstructing the model, a prospective research programme for empirically testing the narrative's effectiveness is outlined. Russia's full-scale invasion provoked Europe's most significant security crisis since WWII; beyond the kinetic confrontation with infrastructural destruction and humanitarian catastrophe, the war became a starting point for a global war of meanings. Zelenskyy's strategic task was securing a stable supply of resources (weapons, financing, sanction pressure) under Ukraine's total dependence on Western liberal democracies. The orientation of Western political systems toward public opinion made winning their electorates' hearts and minds prerequisite for Ukrainian statehood's survival. Additional drivers included entrenched fears of nuclear escalation and scepticism about Ukraine's inevitable defeat – instead, a reality had to be constructed where Ukraine is capable of effective resistance and acts as a defender of global democratic values. Other regional conflicts (the Middle East, India–Pakistan) intensified the global competition for attention, while the war's protracted nature gave rise to war fatigue in the West, threatening to popularize moral selfishness and positions of trading peace at the expense of Ukrainian interests. Conceptually, the study synthesizes the theories of strategic narratives, melodramatic political discourse, and the emotional turn in the social sciences into a three-level conception of the strategic war narrative. The archetypal-plot level simplifies decades of Russo-Ukrainian confrontation, structuring events into a storyline that assigns guilt and defines the innocent via archetypes for international actors. The emotional level regulates external audiences' affective states, while the genre-stylistic level integrates these elements into a melodramatic frame with a distinctive rhetorical repertoire. The research objectives were: 1) to identify the conditions, goals, and communicative tasks faced by Zelenskyy in persuading international audiences over the four years of war; 2) to elucidate the principal elements of the model through a hybrid methodology; 3) to formulate the model's uniqueness as an instrument for mobilizing external audiences' attention and support; 4) to develop prospective directions for studying the model's effectiveness. The methodology combines computer-assisted narrative analysis in ATLAS.ti with automated content analysis via the Claude large language model. Both rested on predeveloped codebooks adapting the theoretical model to Ukrainian wartime foreign-policy communication. The empirical basis is a corpus of 90 Zelenskyy foreign-policy speeches (2022–2025), balanced across years and structured according to the four phases of the war (shock phase (02–04.2022); Ukrainian counteroffensives (05.2022 – 08.2023); positional warfare (09.2023 – 08.2024); strategic adaptation (09.2024 – 12.2025)) and audience types (addresses to peoples of partner countries, speeches at international platforms, addresses to parliaments). Qualitative narrative analysis of the 90 texts identified five archetypal roles (Victim, Aggressor, Hero, Ally, Coward; N=2083) and five plot sequences (Current aggression, Past aggression, Past reaction, Current reaction, Desired state; N=1199). Quantitative content analysis operationalized 17 sub-categories of emotional-rhetorical indicators across four categories (C1. Direct expression of emotions; C2. Dramatization; C3. Simplification; C4. Rhetorical devices; N=7112). Parallel manual coding on a corpus subset confirmed the method's high accuracy. The procedure complies with the GAIDeT taxonomy for transparent use of generative AI. The findings reveal the complexity and adaptability of the strategic war narrative. At the archetypal-plot level, the archetypes have the following distribution: Victim (18%), Aggressor (34%), Hero (15%), Ally (24%), Coward (9%). The plot sequences demonstrate a different trend: the mobilizing Current reaction and Current aggression account for two-thirds of all codes (43% and 28%), while Past reaction (7.5%), Past aggression (11%), and Desired state (11%) are auxiliary. The plot is constructed in the classical melodramatic genre of a Hero-saviour (the Ukrainian state and Defence Forces) who fights a cruel, dehumanized Aggressor (Russia) to rescue an innocent Victim (the Ukrainian civilian population). The most important finding is the central positioning of Western partners as an adaptation to Ukraine's conditions and needs. The unique Ally archetype is the central character after the Aggressor (displacing even the Victim and the Hero): in the plot, the Ally supports the Hero at the most decisive moment, sharing virtue and credit for the victory. The presidential narrative transforms the West's military-political assistance from an act of compassion into an affirmation of its own greatness (national pride from the success of Western weaponry in the defence against Russia). The Coward archetype – a character who choo

**Решение:** -4 political communication and journalism dissertation

---

### 947 · R10901

**News**

2024 · Significance · article · en · https://doi.org/10.1093/jrssig/qmae001

The US Department of Homeland Security (DHS) has expanded its statistical activities by creating a centralised statistics office, the Office of Homeland Security Statistics (OHSS). The OHSS (dhs.gov/ohss) replaces the Office of Immigration Statistics (OIS) – which, as its name suggests, collected only immigration statistics – and is responsible for gathering and reporting data from more than a dozen agencies within its scope, including on cybersecurity, emergency management, infrastructure protection, maritime safety, screening, terrorism and targeted violence, and chemical, biological, radiological, and nuclear security. The new office has pledged to release more detailed data regularly and with greater transparency, and support “evidence-based” policies, programmes, and decision-making. For the current fiscal year, it plans to release data on law enforcement, international trade, cybersecurity, airport screening, emergency response to federal disasters, and maritime response operations. It will also oversee the development of department-wide data standards and help bring the DHS – formed in 2003 in response to the September 11 attacks two years earlier – in line with the 2018 Evidence Act, which requires agencies to make their data accessible and support their policy-making with statistical evidence. The OHSS is led by former OIS director Marc Rosenblum, who joined the DHS in 2016 and has a background in immigration policy. Launching the new office at DHS headquarters last November, Rosenblum said demand for immigration data governance, processing, modelling and reporting had “exploded in the last few years,” adding that “DHS does incredibly important work, and the OHSS team is 100 percent committed to our piece of the mission, which is to foster transparency and data-driven homeland security decision-making by analyzing and disseminating timely, objective DHS data and statistics. “OHSS differs a bit from most existing statistical agencies because our reporting is mainly on DHS activities, rather than external data, and because a major part of our work is to support leadership decision-making. “In establishing this new office, we'll begin releasing data more quickly, with greater granularity and covering a broader scope of DHS activities. “Simply growing the reporting and data governance that accompanies that will be a big undertaking. “This is a big step forward for an office that until recently published data annually, a few years late, so we're really upping our game.” Secretary of Homeland Security Alejandro Mayorkas (pictured) said: “Data-driven decision-making is an integral part of everything we do … Our increased transparency will inform the American people as we work to fulfil our security and safety mission, while safeguarding privacy, civil rights, and civil liberties.” The first systematic study of how ChatGPT might affect the white-collar workplace has found that AI may be more useful for creative tasks than analytical ones. Currently under review at a scientific journal, the study (tinyurl.com/yc25bkbs) examines the performance implications of AI on “realistic, complex, and knowledge-intensive” professional tasks at Boston Consulting Group, one of the world's largest management-consulting firms, which had previously banned its consultants from using AI bots in their work. A total of 758 consultants were randomly assigned to carry out typical work-related tasks with either no AI access, GPT-4 AI access (i.e. ChatGPT), or GPT-4 AI access after 30 minutes of training. The findings showed that consultants assisted by ChatGPT for creative tasks, including brainstorming and writing persuasively, produced work that independent human evaluators rated about 40% better on average – and that they did so over 20% faster. However, when tasks required evidence-based reasoning such as interpreting data from spreadsheets, AI was more of a hindrance than a help. Consultants not using ChatGPT were correct about 84.5% of the time, compared to 70% of those using the bot, and 60% of those using the bot after training. Authors said their findings “bring in a nuanced response to the ongoing debate on whether organizations should adopt AI for high-end knowledge work.” The Office for National Statistics (ONS) has begun quarterly publication of the Household Cost Indices (HCIs), after over a decade of campaigning from the Royal Statistical Society (tinyurl.com/ynyu4dvm). Before the introduction of HCIs, the ONS published only the Consumer Prices Index (CPI), the Consumer Prices Index including owner occupiers’ housing costs (CPIH), and the soon-to-be-discontinued Retail Price Index (RPI), which measure changes in the cost of goods and services. The RSS has promoted the case for HCIs, an additional and alternative measure of household inflation devised by two RSS Fellows, Jill Leyland and John Astin, since around 2012. The HCIs are an attempt to reflect more accurately the true rises in the cost of living for different UK households, and include interest payments such as mortgages and student loans. They also weight households equally, whereas the CPI gives greater weight to higher-spend (usually higher-income) households. The first release estimates that, in the year to September 2023, the cost of living for the average UK family rose by 8.2%, which is higher than the 6.7% recorded by the CPI. “The data shows exactly why we've been pushing for development of the HCIs,” Jill Leyland told the BBC. “CPI is fine for broader economic purposes but over the past two years, it has not reflected the true extent of the cost of living crisis.” In response to the latest figures, RSS chief executive Sarah Cumbers encouraged policy-makers to “take into account the Household Cost Indices, now published quarterly by ONS, as the best way to understand people's experiences of inflation, particularly those on lower incomes.” Former Stanford University president Marc Tessier-Lavigne has retracted a contested paper on

**Решение:** -7 news article on Department of Homeland Security statistics

---

### 948 · R11530

**InFact: A Strong Baseline for Automated Fact-Checking**

2024 · FEVER · https://doi.org/10.18653/v1/2024.fever-1.12

The spread of disinformation poses a global threat to democratic societies, necessitating robust and scalable Automated Fact-Checking (AFC) systems. The AVeriTeC Shared Task Challenge 2024 offers a realistic benchmark for text-based fact-checking methods. This paper presents Information-Retrieving Fact-Checker (InFact), an LLM-based approach that breaks down the task of claim verification into a 6-stage process, including evidence retrieval. When using GPT-4o as the backbone, InFact achieves an AVeriTeC score of 63% on the test set, outperforming all other 20 teams competing in the challenge, and establishing a new strong baseline for future text-only AFC systems. Qualitative analysis of mislabeled instances reveals that InFact often yields a more accurate conclusion than AVeriTeC’s human-annotated ground truth.

**Решение:** -4 automated fact-checking benchmark

---

### 949 · R3337

**Beyond “tasty but nasty”: AI-guided food pairing to re-imagine edible insects in gastronomy**

2026 · Journal of Insects as Food and Feed · journalarticle, article · en · https://doi.org/10.1163/23524588-bja10400

Abstract Growing pressure on global food systems has intensified the search for sustainable, protein-rich alternative ingredients, positioning edible insects as promising yet culturally contested food sources, particularly in Western societies. This study proposes an interdisciplinary framework that integrates Food Pairing Theory with artificial intelligence-assisted recipe prototyping to reframe entomophagy through gastronomic compatibility rather than novelty or necessity. Adopting a qualitative single intrinsic case study design, the research operationalizes food-pairing logic by identifying insect-ingredient combinations with shared aromatic compounds and translating these pairings into structured recipe prototypes using a large language model (ChatGPT-5.2). Three edible insect categories – beetles, caterpillars, and bees – were selected based on their global prevalence and nutritional relevance and paired with complementary plant-based ingredients using a data-driven aroma-matching database. Standardized prompts were employed to generate draft recipes, which were subsequently refined through a systematic expert evaluation process. Two gastronomy-trained experts assessed the finalized prototypes using a structured 7-point anchored rubric addressing pairing coherence, anticipated sensory balance, culinary feasibility, clarity, gastronomic positioning, innovation, and food-safety awareness. Inter-rater reliability was examined using quadratic-weighted Cohen’s kappa ( κ w). Findings indicate that AI-assisted recipe prototyping can coherently translate food-pairing theory into gastronomically plausible concepts, with particularly strong performance in pairing coherence and novelty-with-plausibility dimensions. The study contributes a transparent, reproducible workflow for integrating artificial intelligence into gastronomic innovation and demonstrates how taste harmony can serve as a strategic lens for addressing consumer resistance to insect-based foods. Future research should extend this framework through sensory testing, consumer acceptance studies, and comparative evaluations across insect species and algorithmic pairing systems.

**Решение:** -4 gastronomy and food science

---

### 950 · R6868

**Large Language Models for Accurate Medical Chart Abstraction: Enabling Scalable and Secure Artificial Intelligence Deployment in Stroke.**

2026 · AJNR. American journal of neuroradiology · journal article, med, journalarticle · eng · https://doi.org/10.3174/ajnr.a9251

Graphical Abstract BACKGROUND AND PURPOSE: Medical chart abstraction plays a critical role in clinical research and quality monitoring by transforming unstructured narratives in the procedure reports into structured variables for large-scale analysis. We developed and evaluated a prompting-based large language model (LLM) framework for automated extraction of structured clinical variables from neurointerventional procedure reports in patients with acute ischemic stroke due to large vessel occlusions. MATERIALS AND METHODS: This retrospective study included 2416 free-text neurointerventional acute stroke intervention (thrombectomy) reports with key radiology findings from 3 hospitals. Eight clinically relevant variables were annotated by hospital staff (without formal clinical training) and used as the nonexpert reference standard. Twenty-two instruction-tuned open-source LLMs (LLaMA, Qwen, Gemma, etc) were evaluated across architectures, sizes, and biomedical adaptations using 2 prompting strategies: Quick Response and Chain-of-Thought (CoT). Model performance was benchmarked against nonexpert staff annotations and medical expert ratings. Extraction accuracy, latency, and agreement with expert adjudication were assessed. RESULTS: LLaMA3.3-70B achieved the highest overall accuracy (94.8%). CoT prompting improved performance on inferential variables (eg, site of occlusion), while Quick Response was optimal for directly stated procedural fields (eg, stent placement). Expert adjudication confirmed that LLaMA3.3-70B outperformed nonexpert annotations in 7 of 8 variables and matched junior medical students. Annotation accuracy increased with clinical experience, and artificial intelligence predictions were more closely aligned with expert interpretations than with those of nonexpert staff, especially for structured variables like IV tPA, TICI Post, and NIHSS. CONCLUSIONS: Prompted LLMs can accurately and scalably extract critical clinical information from neurovascular radiology reports without custom preprocessing, supporting integration into retrospective research pipelines and automated stroke registry curation.

**Решение:** -4 somatic neurology stroke chart abstraction

---

### 951 · R3611

**Populism and Narratives of Social Mobility: Replication Package**

2026 · OSF · text/project, preprint · https://doi.org/10.17605/osf.io/2vx4p

Replication Package — "Populism and Narratives of Social Mobility" Lorenz Meister (DIW Berlin &amp; Freie Universität Berlin) This repository contains all code and documentation needed to reproduce the empirical results of the paper. The analysis draws on three original survey waves (N ≈ 6,600 U.S. residents, 2024–2025), administrative mobility data from the Opportunity Atlas (Chetty et al. 2018), and county-level electoral data from the MIT Election Data and Science Lab. What's included: Stata do-files, a Python script for LLM-based narrative classification, survey questionnaires, and a codebook. Public data sources are freely downloadable; see the README for links and folder structure. Survey data: Available upon request — contact lmeister@diw.de. Prolific user IDs and IP addresses are not included.

**Решение:** -4 political science replication package

---

### 952 · R6528

**Evaluating large language model clinical reasoning in glaucoma using retrieval-augmented generation.**

2026 · Advances in ophthalmology practice and research · journal article, journalarticle, article · eng · https://doi.org/10.1016/j.aopr.2026.05.003

Background: Large language models (LLMs) demonstrate strong performance in knowledge-based medical tasks, yet their clinical reasoning capabilities in complex ophthalmic decision-making, particularly glaucoma management, remain insufficiently characterized. Retrieval-augmented generation (RAG) has been proposed as a strategy to improve factual grounding and safety, but its clinical value requires systematic evaluation. Methods: We conducted a retrospective, scenario-based comparative evaluation using 40 real-world glaucoma cases spanning primary, secondary, postoperative, and end-stage disease. Six model conditions (GPT, Gemini, and Grok, each with and without RAG) were assessed using a guideline-grounded framework covering medical accuracy, key point coverage, logical completeness, and a separate qualitative safety audit. Model outputs were compared with written responses from four practicing ophthalmologists. All responses were independently scored by two masked glaucoma specialists using a prespecified ordinal rubric, and formal inter-rater reliability and paired sensitivity analyses were performed. Results: RAG-enhanced models consistently outperformed their matched non-RAG counterparts across evaluation domains. In human-rating sensitivity analyses, the composite RAG advantage remained significant for GPT (mean difference=0.119, 95% CI: 0.068-0.173), Gemini (mean difference=0.095, 95% CI: 0.030-0.161), and Grok (mean difference=0.110, 95% CI: 0.033-0.194). Inter-rater agreement of the ordinal rubric was limited, supporting consensus adjudication and cautious interpretation of artificial intelligence-human comparisons. Conclusions: Retrieval augmentation was associated with more accurate, more complete, and more safety-aware glaucoma reasoning under this scenario-based evaluation. These findings support the potential value of RAG-enhanced LLMs as supervised clinical decision-support tools, but they do not establish standalone clinical use. Safety was evaluated as a separate audit layer rather than as part of the weighted composite score.

**Решение:** -4 somatic ophthalmology (glaucoma reasoning)

---

### 953 · R5699

**Are LLMs better expert judges? Rethinking content validity assessment in the age of AI**

2026 · PsyArXiv · preprint · https://doi.org/10.31234/osf.io/4hsyx_v1

In this article, we demonstrate a novel application of large language models (LLMs) as expert judges for item-level content relevance evaluation. Eleven advanced LLMs were included, each treated as a separate expert panel based on multiple procedurally independent judgments generated via repeated API queries. Their performance was compared with ratings provided by human judges, including psychology students and academic experts. Internal agreement within each panel was assessed using Krippendorff’s alpha and Kendall’s coefficient of concordance. Beyond agreement, theoretically predefined control items representing content-nonrelevant material were used to determine the accuracy of each panel’s ratings. Results indicated that several LLM-based panels (Gemini 3 Pro, GPT-5.2 Pro, Claude Sonnet 4.5, and DeepSeek-V3.2) combined near-perfect internal agreement with high accuracy in identifying nonrelevant items, outperforming human panels. Even when individual model instances were treated as independent judges, agreement remained high and all control items were correctly identified. These findings demonstrate that selected LLMs can function as highly consistent content judges, particularly in detecting content-nonrelevant items that are conceptually distant from the measured construct. However, given the lack of empirical evidence on LLMs as expert judges, their ratings should currently be viewed as complementary to human expertise, and further research is required to clarify the conditions under which they can be reliably incorporated into procedures for evaluating test item content relevance.

**Решение:** ? T1/T2 LLMs as expert judges for psychometric item content validity vs human academic experts (Krippendorff alpha); evaluate on full text

---

### 954 · R7053

**Semantic Analysis of ChatGPT’s Behavior in Contextual Code Correction for Python**

2025 · International Journal of Computational and Experimental Science and Engineering · journalarticle, article · en · https://doi.org/10.22399/ijcesen.3419

Software debugging remains one of the most time-consuming and cognitively demanding phases in the software development lifecycle. The paper considers the analytical capabilities of transformers transformer-based language models—specifically ChatGPT—in detecting and correcting semantic faults in multi-module Python projects. Ten synthetic Python programs (100–200 lines each), containing a total of 30 deliberately injected faults (distributed among order faults, variable leakage, and edge-case omissions), were submitted to ChatGPT under a standardized prompting scheme. Model responses were benchmarked against conventional static analysis tools (Pylint, MyPy) and a human expert baseline. Quantitatively, ChatGPT achieved an average error detection rate (EDR) of 76.7%, outperforming Pylint (23.3%) and MyPy (15%) across fault categories. In repair accuracy (RA), ChatGPT resolved 62–75% of the identified errors correctly, versus 10–25% for static tools. Statistical validation using a Chi-square test (χ² = 36.27, p < 0.001) and one-way ANOVA (F(3, 27) = 14.92, p < 0.001) confirms the significance of these differences. Qualitative clarity was also assessed using ordinal metrics and validated via Kruskal-Wallis H tests (H = 11.56, p < 0.01). These results suggest that ChatGPT possesses substantial semantic reasoning capabilities, particularly in contexts requiring non-local inference across modules. However, limitations persist in handling implicit dependencies and dynamic runtime conditions. The study concludes that such models can be meaningfully integrated into debugging pipelines as assistive agents, provided their outputs are cross-validated with expert oversight and static tools. Future research should explore hybrid frameworks that combine statistical inference with formal verification techniques.

**Решение:** -4 software engineering code correction

---

### 955 · R3590

**Evaluative Stance Toward Artificial Intelligence in the Medical Literature: Infoveillance Study of 16,749 High-Quartile Journal Abstracts, 2021-2026 (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.109710

BACKGROUND Medical artificial intelligence (AI) publications report performance while also framing AI as beneficial, uncertain, or risky, which has not been measured at scale. The literature is itself an information environment clinicians rely on, yet health AI sentiment has been measured mainly in public online discourse, not in medical journals. OBJECTIVE We aimed to measure the evaluative stance toward AI in high-quartile medical journal abstracts from January 2021 to April 2026, and to characterize it across time, concern themes, failure mechanisms, specialties, first-author country, and publication format. METHODS We conducted a large language model (LLM)-assisted computational content analysis of PubMed records from top-two-quartile (Q1/Q2) SCImago journals. Of 97,492 eligible records, an AI-engagement prefilter retained 16,759 discourse or evaluative records, and stance classification yielded 16,749 valid labels on an ordered scale of Alarm, Caution, Neutral, Cautious Optimism, and Advocacy. Critical stance was Alarm plus Caution; favourable stance was Cautious Optimism plus Advocacy. Critical records were further classified for concern theme and, on two axes, for failure mechanism, which distinguished fabrication from factual error, and model type. Every LLM step was validated against blinded human coding (prefilter Cohen kappa 0.51; stance quadratic-weighted kappa 0.79, 95% CI 0.72-0.84; specialty kappa 0.75; model type kappa 0.84; failure mode kappa 0.57). RESULTS Cautious Optimism was the majority stance (62.8%) and 30.8% of records were critical. Advocacy fell monotonically from 2.9% (2021) to 0.6% (partial 2026; Spearman rho -1.00), while critical share rose modestly from 25.4% (95% CI 22.9-28.1) to 32.6% (30.9-34.4), rising within both prefilter genres. Among critical abstracts, patient safety rose 11.0 percentage points and errors 30.9, whereas regulation fell 22.0 in prevalence share. Within the hallucination-gated subset (n=2226), factual error was the majority mechanism every year (56% to 90%), while fabrication-involved papers reached about 21% to 23% from 2023 onward; fabrication estimates are an upper bound. Critical rate varied roughly threefold across 18 specialty and domain categories (51.3% in Mental Health and Psychiatry to 16.8% in Cardiology), was inversely associated with US Food and Drug Administration cleared-device availability (rho -0.65, two-sided p=.004), and varied by first-author country (34.5% United States, 16.2% China). Reviews were the least critical (24.9%) and most favourable (73.1%) format. CONCLUSIONS Medical-AI abstracts moved away from unqualified promotion toward more qualified assessment, not toward broad opposition. Two implications follow for how the literature is written and read. That reviews were the least critical and most favourable format may matter for readers, guideline developers, and educators. Critical reporting should distinguish factual error from fabrication rather than treating hallucination as one category, which bears on how journals, reviewers, and reporting standards describe language model failure. Throughout our investigation, we measure published discourse, not AI capability, nor whether these stances are correct.

**Решение:** -4 bibliometric and sentiment analysis of medical literature on AI

---

### 956 · R4310

**Mental health professionals' perspectives on integrating artificial intelligence into psychological interventions: A qualitative multinational study with a focus on epistemic trust and the hybrid therapeutic alliance.**

2026 · Psychiatry research · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.psychres.2026.117371

Background The rapid expansion of generative artificial intelligence (AI) in mental health care has raised critical questions regarding its acceptance, potential benefits, risks, and ethical implications for mental health professionals. This study explored in depth the perspectives of professionals from multiple countries on the integration of generative AI into psychological interventions. Methods A qualitative design was employed, using written semi-structured interviews with 34 mental health professionals from the United States, Canada, the United Kingdom, Germany, Australia, New Zealand, Iran, and Türkiye. Data were analyzed through reflexive thematic analysis. Results Four overarching themes were identified: (1) general perceptions characterized by enthusiasm alongside skepticism; (2) opportunities including expanded access to care, personalized support, and reduced clinical workload; (3) concerns related to response quality, the therapeutic alliance, and ethical and data security issues; and (4) future perspectives emphasizing accountability, complementary clinician-AI roles, and responsible innovation. Participants consistently highlighted the importance of algorithmic transparency, empirical validation, ethical governance, and clinician training. These findings informed the development of the concepts of epistemic trust and the hybrid therapeutic alliance as interpretive frameworks for understanding clinicians' evaluations of AI in psychological practice. Conclusion The findings suggest that the responsible integration of generative AI into psychological practice requires balancing innovation with clinical oversight, ethical governance, and human judgment. The concepts of epistemic trust and the hybrid therapeutic alliance are proposed as novel conceptual frameworks for understanding clinicians' acceptance and responsible use of AI in mental health care. Future research should examine these concepts across diverse clinical and cultural contexts to inform implementation strategies, clinician training, and regulatory policy.

**Решение:** -2 qualitative interview study of clinicians attitudes towards AI

---

### 957 · R5893

**Language Carries the Expert's Impression: Instrument-Anchored LLM Judges Transfer Counseling-Quality Assessment and Beat In-Domain Training**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.08055

Automatic assessment of communication quality in dyadic counseling conversations is bottlenecked by data: expert-rated corpora are small and expensive to grow. We study cross-domain transfer of expert overall-impression prediction across three German corpora of simulated counseling (two general-practice medical, one school-related parent-teacher; $n=195$ expert-rated sessions, one corpus after scale equating). Training on the other domains beats training in-domain: leave-one-domain-out transfer reaches nested Spearman $ρ= 0.54$ against $\le 0.48$ within the target domain, a paired session-level gap of $+0.15$ that holds at $+0.12$ when the training-set sizes are matched, so it is not simply data volume. The decisive features are session-level construct scores from small open-weight LLMs reading the two-speaker transcript, with the constructs largely derived from the experts' rating instruments: the instrument-derived battery lifts a single judge from $0.32$ to $0.41$ over generic dialogue qualities, judges from three model families ensemble to $0.51$ language-only, and a nonverbal-dyadic block adds $+0.03$ more, not separable from noise at this sample size. We also price the recording setup: one corpus lost its per-speaker audio, 16% of its diarised segments carry the wrong speaker, and repair is worth $+0.07$ there. At practically attainable corpus sizes, the expert's overall impression is carried by what is said, and by other communication programs' data more than by one's own. Preprint. 25 pages, 2 figures

**Решение:** + T4 communication quality in dyadic counseling sessions: instrument-anchored LLM judges vs expert overall impressions (Spearman rho = 0.51-0.54, N=195 sessions)

---

### 958 · R0040

**Evaluating Sycophantic Behavior and Belief Distortion in Multilingual Large Language Models: SYCON-Indic**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7226038

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 benchmark evaluating sycophancy in LLMs

---

### 959 · R1100

**Prompt-Based Jailbreaking of Leading LLM Chatbots: A Survey of Attacks and Defenses**

2026 · IEEE Transactions on Artificial Intelligence · journalarticle, review, article · https://doi.org/10.1109/tai.2026.3665656

Generative artificial intelligence (AI) systems—particularly large language models (LLMs)—remain vulnerable to jailbreak attacks: adversarial prompts that bypass safeguards and elicit unsafe or restricted outputs. This survey synthesizes jailbreak research from 2023–2025, covering attack methods, defense strategies, and evaluation frameworks. Jailbreak techniques are grouped into five main categories: prompt-based injections, role-play conditioning, multiturn dialogue, multilingual or multimodal exploits, and optimization-driven pipelines. We also examine discovery methods such as human red teaming and automated attacker systems (e.g., AutoJailbreak and LLMStinger), and review defense mechanisms including supervised fine-tuning (SFT), reinforcement learning from human feedback (RLHF), adversarial fine-tuning, and output or pipeline filtering. Standardized benchmarks—such as PromptBench, JailbreakBench, and multimodal evaluation suites—are analyzed in terms of reproducibility, coverage, and robustness testing. Persistent issues of generalization, reproducibility, and scalability are discussed, along with trade-offs between safety alignment and model utility. This article provides an up-to-date reference clarifying the evolving landscape of jailbreak attacks and defenses in LLMs.

**Решение:** -1 survey on prompt-based jailbreaking

---

### 960 · R1663

**Rage Vs Reason: Analyzing Emotional Outbursts from Constructive Criticisms in Negative Steam Reviews**

2026 · International Conference on Computational Intelligence and Communication Networks · conference, review · https://doi.org/10.1109/cicn70047.2026.11594384

Sentiment analysis generally classifies textual data into positive, negative, or neutral categories; however, the negative sentiment is mostly treated as a single, uniform category. In real-world context, negative reviews may contain either emotion-based reviews or constructive, reason-based responses. Our work addresses this limitation by introducing a fine-grained classification technique, which distinguishes ragedriven emotional responses from reasonable feedback within negative user reviews of games. A custom manually annotated dataset of 1001 game reviews collected from Overwatch® 2, Kerbal Space Program 2, and Starfield was manually annotated for this work. A traditional supervised machine learning model, support vector machine, was implemented and evaluated, along with a zero-shot and a few-shot large language model. The results showed that traditional supervised classifiers outperformed the other models with an overall accuracy of 82.09%. Additional statistical analysis of average word and character counts was performed to understand the structural differences between rage-driven and reason-driven texts. The proposed work provides a practical approach to assist developers in identifying constructive insights underlying in the negative reviews, which may help them improve the products and services.

**Решение:** -4 commercial Steam video game review sentiment

---

### 961 · R8099

**Shaping Explanations: Semantic Reward Modeling with Encoder-Only Transformers for GRPO**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2509.13081

While Large Language Models (LLMs) excel at generating human-like text, aligning their outputs with complex, qualitative goals like pedagogical soundness remains a significant challenge. Standard reinforcement learning techniques often rely on slow and expensive LLM-as-a-judge evaluations or on brittle, keyword-based metrics like ROUGE, which fail to capture the semantic essence of a high-quality explanation. In this work, we introduce a novel approach to reward shaping within the Group Relative Policy Optimisation (GRPO) framework. Our central contribution is the use of a small, efficient encoder-only transformer as a semantic reward model. This model provides a dense, semantically rich reward signal based on the cosine similarity between a generated explanation and a ground-truth reference, guiding the policy towards explanations that are not just factually correct but also structurally and conceptually aligned with expert reasoning. We apply this method to the task of training a model for the Italian medical-school entrance examinations, following standard domain-adaptive continued pre-training (CPT) and supervised fine-tuning (SFT). Our results demonstrate that GRPO with our proposed semantic reward significantly improves explanation faithfulness and clarity over a strong SFT baseline, showcasing the power of using lightweight encoder models for nuanced reward shaping in complex generation tasks

**Решение:** -4 educational reward modeling with encoder-only transformers

---

### 962 · R9677

**Performance assessment of large language models in cancer staging: Comparative analysis of Mistral models**

2025 · medRxiv · preprint, ppr · en · https://doi.org/10.1101/2025.09.10.25335246

ABSTRACT Cancer staging plays a critical role in treatment planning and prognosis but is often embedded in unstructured clinical narratives. To automate the extraction and structuring of staging data, large language models (LLMs) have emerged as a promising approach. However, their performance in real-world oncology settings has yet to be systematically evaluated. Herein, we analysed 1000 oncological summaries from patients receiving treatment for breast cancer between 2019 and 2020 at the François Baclesse Comprehensive Cancer Centre, France. Five Mistral artificial intelligence–based LLMs were evaluated (i.e. Small, Medium, Large, Magistral and Mistral:latest) for their ability to derive the cancer stage and identify staging elements. Larger models outperformed their smaller counterparts in staging accuracy and reproducibility (kappa > 0.95 for Mistral Large and Medium). Mistral Large achieved the highest accuracy in deriving the cancer stage (93.0%), surpassing the original clinical documentation in several cases. The LLMs consistently performed better in deriving the cancer stage when working through tumour size, nodal status and metastatic components compared to when they were directly requested stage data. The top-performing models had a test–retest reliability exceeding 97%, while smaller models and locally deployed versions lacked sufficient robustness, particularly in handling unit conversions and complex staging rules. The structured, stepwise use of LLMs that emulates clinician reasoning offers a more efficient, transparent and reproducible approach to cancer staging, and the study findings support LLM integration into digital oncology workflows.

**Решение:** -4 somatic oncology cancer staging

---

### 963 · R10834

**GPT-4 Emulates Average-Human Emotional Cognition from a Third-Person Perspective**

2024 · International Conference on Affective Computing and Intelligent Interaction (ACII) · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/acii63134.2024.00043

This paper extends recent investigations on the emotional reasoning abilities of Large Language Models (LLMs). Current research on LLMs has not directly evaluated the distinction between how LLMs predict the self-attribution of emotions and the perception of others' emotions. We first look at carefully crafted emotion-evoking stimuli, originally designed to find patterns of brain neural activity representing fine-grained inferred emotional attributions of others. We show that GPT-4 is especially accurate in reasoning about such stimuli. This suggests LLMs agree with humans' attributions of others' emotions in stereotypical scenarios remarkably more than self-attributions of emotions in idiosyncratic situations. To further explore this, our second study utilizes a dataset containing annotations from both the author and a third-person perspective. We find that GPT-4's interpretations align more closely with human judgments about the emotions of others than with self-assessments. Notably, conventional computational models of emotion primarily rely on self-reported ground truth as the gold standard. However, an average observer's standpoint, which LLMs appear to have adopted, might be more relevant for many downstream applications, at least in the absence of individual information and adequate safety considerations. submitted to 12th International Conference on Affective Computing &amp; Intelligent Interaction, Glasgow, UK, September 15-18, 2024

**Решение:** + T1 GPT-4 emotion annotation from third-person perspective compared to human ratings (ACII 2024)

---

### 964 · R8022

**A Zero-Shot Framework for Automated Media Framing Analysis using Large Language Models**

2025 · International Conference on Sustainable Communication Networks and Application (ICSCNA) · conference, conference-paper · https://doi.org/10.1109/icscn67106.2025.11308308

The framing of information in news media profoundly influences public perception, yet its analysis at scale remains a significant challenge. Traditional computational methods, such as sentiment analysis, are often insufficient as they fail to capture the nuanced narrative angles that define media frames. This paper introduces a novel, zero-shot framework for the automated classification of news headlines into predefined media frames using a large language model (LLM). A codebook of four primary frames—Economic Consequences, Human Interest, Conflict, and Ethical & Moral—is established, and a structured prompt is engineered to guide the LLM's inferential process. The framework is validated through a proof-of-concept, applied to a curated set of headlines concerning the topic of Electric Vehicles (EVs), which demonstrates the model's capacity to consistently identify the dominant narrative frame and provide a coherent justification for its classification. This work represents a step towards the development of more sophisticated, scalable, and accessible tools for computational media analysis, enabling researchers to move beyond simple sentiment and explore the deeper structures of media discourse.

**Решение:** -4 news media framing analysis

---

### 965 · R5696

**Natural language processing for non-violent conflict detection in institutional discourse**

2026 · Expert Systems with Applications · article · en · https://doi.org/10.1016/j.eswa.2026.133182

This paper proposes a methodological pipeline for studying non-violent institutional conflict in formal deliberative settings, where disagreement is rarely expressed through overt hostility and instead emerges through tone, interactional positioning, and procedural dynamics. The approach combines computational methods with human-in-the-loop annotation to enable scalable yet interpretable analysis of conflict in public administration. The pipeline is illustrated through a case study of the Regional Council of Aosta Valley (Italy), using official multilingual parliamentary transcripts. We construct an original dataset integrating institutional metadata, speaker characteristics, and affective evaluations. A representative three-month subset is annotated along two dimensions, i.e., intrinsic tone and contextual conflict, by human coders, large language models (LLMs), and a multilingual BERT sentiment classifier, allowing systematic comparison across annotation sources. Results show that human annotations constitute the most coherent benchmark, while LLM-based labels are noisier, especially for contextual conflict. BERT-derived sentiment provides a stable but only partially aligned signal. Descriptive analyses reveal pronounced asymmetries in participation and evaluation, including exploratory gender-disaggregated patterns that motivate further investigation. Predictive models trained on non-linguistic metadata achieve moderate accuracy when supervised with automated sentiment, but near-perfect performance when human-coded tone is included, highlighting both the limits of automation and the interpretive nature of institutional conflict. Overall, the study demonstrates that non-violent conflict is empirically tractable yet deeply context-dependent, and offers a transferable framework for conflict analysis in democratic institutions.

**Решение:** -4 political conflict detection in institutional discourse

---

### 966 · R12623

**DRDT: Dynamic Reflection with Divergent Thinking for LLM-based Sequential Recommendation**

2023 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2312.11336

The rise of Large Language Models (LLMs) has sparked interest in their application to sequential recommendation tasks as they can provide supportive item information. However, due to the inherent complexities of sequential recommendation, such as sequential patterns across datasets, noise within sequences, and the temporal evolution of user preferences, existing LLM reasoning strategies, such as in-context learning and chain-of-thought are not fully effective. To address these challenges, we introduce a novel reasoning principle: Dynamic Reflection with Divergent Thinking within a retriever-reranker framework. Our approach starts with a collaborative in-context demonstration retriever, which collects sequences exhibiting collaborative behaviors as in-context examples. Following this, we abstract high-level user preferences across multiple aspects, providing a more nuanced understanding of user interests and circumventing the noise within the raw sequences. The cornerstone of our methodology is dynamic reflection, a process that emulates human learning through probing, critiquing, and reflecting, using user feedback to tailor the analysis more effectively to the target user in a temporal manner. We evaluate our approach on three datasets using six pre-trained LLMs. The superior performance observed across these models demonstrates the efficacy of our reasoning strategy, notably achieved without the need to fine-tune the LLMs. With our principle, we managed to outperform GPT-Turbo-3.5 on three datasets using 7b models e.g., Vicuna-7b and Openchat-7b on NDCG@10. This research not only highlights the potential of LLMs in enhancing sequential recommendation systems but also underscores the importance of developing tailored reasoning strategies to fully harness their capabilities.

**Решение:** -4 recommender systems in e-commerce

---

### 967 · R0894

**Leveraging Generative Large Language Models for Temporal Relation Extraction From French Clinical Narratives: Prompt-Chaining Approach.**

2026 · Journal of medical Internet research · journal article, journalarticle, article · eng · https://doi.org/10.2196/95198

Abstract Background Temporal relation extraction (TRE) in clinical narratives is crucial for understanding patient history, disease progression, and treatment pathways. However, it remains challenging due to limited annotated data and to the complexity of clinical text, including domain-specific terminology, inconsistent information, and implicit temporal reasoning. These challenges are particularly acute for rare diseases, where information such as the date of diagnosis or the onset of key phenotypes is rarely available in structured data, despite being essential for estimating diagnostic delay and reconstructing the natural history of the disease. Objective We explore the potential of open-weight and on-premises large language models (LLMs) on clinical TRE and normalization using zero- and few-shot prompting, aiming to reduce the time-consuming and costly annotation process. Based on recent promising capabilities of LLMs in understanding and reasoning over text, we evaluate whether these models can efficiently perform TRE and normalization in real-world clinical settings. Methods We cast the temporal relation task as a question-answering task, in which the models extract the temporal expressions associated with a given clinical event. We propose a prompt-chaining strategy that sequentially performs normalization on the extracted temporal expressions. Our LLM-based approach is evaluated on constructed and annotated French real-world clinical narratives, covering temporal relations involving 2 types of clinical events: phenotypes and rare disease diagnoses. Four open-weight LLMs were evaluated across multiple prompt configurations and compared with rule-based and neural baselines using exact-match metrics, an LLM-as-a-judge evaluation, and human validation. We further evaluate our approach by applying it to the English 2012 i2b2 corpus, involving other types of clinical events. Results The proposed approach achieves stable extraction performance with only a small number of in-context examples across both clinical event types, reaching a maximum F1-score of 0.72 for rare disease diagnoses and 0.61 for phenotype events. LLM-as-a-judge evaluation supports these findings by capturing minor temporal variations penalized by exact-match metrics, while human validation further confirms the clinical validity of the extracted relations. On the 2012 i2b2 corpus, the approach remains robust despite increased complexity and minimal supervision. Adding normalization using the prompt-chaining strategy maintains stable overall performance, indicating minimal error propagation and efficient temporal normalization. Conclusions Prompting LLMs with a minimal set of in-context examples can achieve strong performance for TRE and normalization in low-resource settings with limited domain-specific annotations. Relying on open-weight, on-premises models, the proposed approach therefore offers a practical path toward deployment in real-world clinical workflows and could further be extended to extract key clinical information, such as age at diagnosis or age at onset, particularly in the context of rare diseases, where it could help prefill structured reporting forms, reducing the manual effort needed to retrieve such information directly from clinical narratives.

**Решение:** -4 somatic clinical EHR temporal relation extraction

---

### 968 · R7741

**Comparison of Artificial Intelligence Chatbots (ChatGPT vs Google Gemini) for Informed Consent Quality: A Cross-sectional Evaluation.**

2025 · Indian journal of critical care medicine : peer-reviewed, official publication of Indian Society of Critical Care Medicine · journal article, journalarticle, article · eng · https://doi.org/10.5005/jp-journals-10071-25074

Abstract Background and aims Obtaining informed consent (IC) for tracheostomy is a frequent and essential process in the intensive care unit (ICU). With the increasing use of artificial intelligence (AI) in health care, chatbots such as ChatGPT and Google Gemini (GG) are being explored as potential tools to assist in drafting IC documents. Methods In this cross-sectional study, IC drafts for tracheostomy were generated by ChatGPT and GG. Fifteen experienced intensivists independently evaluated these drafts for accuracy, completeness, readability, and sentiment. Readability was measured using the Flesch Reading Ease (FRE) score, while sentiment analysis assessed the emotional tone of the text. Results No statistically significant differences were observed in terms of accuracy or completeness between the two chatbots. The inter-rater reliability was assessed using the intraclass correlation (ICC). The ICC for completeness and accuracy ratings between ChatGPT and GG were 0.85 (95% CI: 0.75–0.92) and 0.80 (95% CI: 0.68–0.89), respectively, suggesting excellent to good inter-rater reliability between the two Chatbots. However, ChatGPT drafts had higher FRE scores (76.46 vs 60.04), indicating better readability. Sentiment analysis revealed that both drafts were predominantly neutral, with GG incorporating slightly more positive expressions. Conclusion Both ChatGPT and GG can generate clinically appropriate IC content for tracheostomy. ChatGPT appears to have an advantage in producing more readable and patient-friendly material, highlighting its potential utility in clinical communication. How to cite this article Chilkoti GT, Jain S, Gondode PG. Comparison of Artificial Intelligence Chatbots (ChatGPT vs Google Gemini) for Informed Consent Quality: A Cross-sectional Evaluation. Indian J Crit Care Med 2025;29(11):967–969.

**Решение:** -4 somatic surgical informed consent (tracheostomy)

---

### 969 · R0952

**Benchmarking the Safety of General Purpose Large Language Models for Suicide Risk Detection and Response**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.6836551

Background: As more people turn to AI chatbots for psychological support, questions are growing about whether these tools are safe. Automated LLM-as-a-judge evaluations can both quantify chatbot safety at scale and identify actionable areas for improvements, enabling more efficient iteration for developers and safer AI tool deployment.&lt;br&gt;&lt;br&gt;Methods: We used the Validation of Ethical and Responsible AI in Mental Health (VERA-MH), an open-source automated evaluation of simulated multi-turn conversations, to benchmark the performance of ten leading general-purpose large language models (LLMs) for suicide risk detection and response. We first tested the framework’s internal structure and identified optimal testing conditions for producing stable scores and facilitating meaningful comparisons across LLMs. We then applied VERA-MH to evaluate both overall safety and five safety dimensions across version histories from four major LLM providers.&lt;br&gt;&lt;br&gt;Outcomes: The framework’s five safety dimensions were largely distinct, supporting the value of both overall and dimension-specific scores. Scores stabilized when judging 200 conversations of up to 30 turns per LLM, suggesting these parameters provided optimal testing conditions. Newer LLMs achieved higher overall safety scores than earlier versions for 3 of the 4 providers, with Claude Sonnet 4.6 and GPT-5.2 scoring the highest overall and GPT-4o and Grok 4 the lowest. Models consistently performed the best on detecting potential risk, but underperformed in asking direct follow-up questions about suicidal thoughts or safety 61% of the time, and failed to adequately guide users to human care 33% of the time.&lt;br&gt;&lt;br&gt;Interpretation: Although safety has improved over time for most general-purpose models, gaps remain in suicide risk handling, particularly in how consistently chatbots confirm risk and effectively guide users to human support when needed.

**Решение:** ? T3/T4 VERA-MH benchmark evaluating LLMs for suicide risk detection and response; check human clinician validation on full text

---

### 970 · R12300

**Exploring the Sources of Variance in Risky Decision Making with Large Language Models**

2023 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/3hrnc

What are the sources of individual-level differences in decision making, and how do they depend on the domain or situation in which the decision is being made? Psychologists currently answer such questions with psychometric methods, which analyze correlations across participant ratings in survey datasets. In this paper we model the psychological mechanisms that give rise to these correlations. Our approach uses 1. Large language models (LLMs) to quantify everyday behaviors in terms of the attributes or reasons that may describe those behaviors, and 2. Decision models to map these attributes and reasons onto participant ratings. We show that LLM-based decision models can explain observed correlations between risky behaviors in terms of the reasons different behaviors elicit, and explain observed correlations between individuals in terms of the weights different individuals place on reasons, thereby providing a process-level foundation for psychometric analysis. Since LLMs provide quantitative representations for nearly any naturalistic decision, they can be used to make accurate out-of-sample predictions for hundreds of everyday behaviors, predict the reasons why people may or may not want to engage in these behaviors, and interpret these reasons in terms of intuitive psychological constructs. Our approach has important theoretical and practical implications for the study of heterogeneity in everyday decision making.

**Решение:** -6 cognitive modeling of risky decision making without text coder agreement

---

### 971 · R5731

**Performance of ChatGPT versus spine surgeons as an emergency department spine call consultant.**

2026 · North American Spine Society journal · journal article, journalarticle, article · eng · https://doi.org/10.1016/j.xnsj.2025.100836

Background: Large language models (LLMs) like ChatGPT are increasingly being recognized as credible tools for use across diverse healthcare settings. While artificial intelligence (AI) use has previously been evaluated in emergency medicine, its use in subspecialty care - particularly spine surgery - remains underexplored. This study evaluates the clinical accuracy, management appropriateness, completeness, helpfulness, and overall quality of ChatGPT responses compared to those of board-certified, spine surgeons in response to common emergency department (ED) consultations. Methods: A 7-part questionnaire was developed based on common ED spine consultations (eg, Cauda Equina Syndrome, compression fracture in elderly patients, purulent drainage from surgical wound, acute lumbar disc herniation, incomplete spinal cord injury, epidural abscess, and metastatic spine disease). Each case included 3-4 questions pertaining to examination, diagnosis, management, and counseling. Responses from ChatGPT and 7 board-certified spine surgeons were restricted to 3-4 sentences per question. Three emergency medicine physicians rated each de-identified questionnaire response using a 5-point Likert scale. Statistical analysis was conducted using a 2-sample T-test with unequal variance. Inter-rater reliability was assessed using pairwise weighted Cohen's kappa coefficient (κ). Results: When comparing AI responses versus spine surgeon responses to proposed ED consultations, AI responses were rated to be superior across all 5 metrics of clinical accuracy, management appropriateness, completeness, helpfulness, and overall quality (p<.05). Inter-rater reliability was assessed using the average pairwise weighted Cohen's kappa coefficient which showed substantial agreement (κ=0.76). Conclusions: ChatGPT responses to emergency department spine consultations were rated as significantly higher compared to board-certified spine surgeons by emergency medicine providers. Though further improvement and validation is warranted, these findings suggest that ChatGPT can be a useful clinical adjunct for spine-related emergency department consultations.

**Решение:** -4 somatic spine surgery consultation

---

### 972 · R1675

**Building Psychotherapy Awareness in LLM: A Novel GenAI Multi-Agent Framework for Predicting Client’s Remission**

2026 · IEEE Access · journalarticle, article · en · https://doi.org/10.1109/access.2026.3727051

Motivational Interviewing (MI) is a widely recognised therapeutic approach for behaviour modification in clients suffering from addiction. An important step in evaluating the effectiveness of MI involves annotating the clients’ utterances and therapists’ behaviour associated with the utterances. Manually annotating an MI transcript is often time-consuming, whereas automating it with Large Language Models (LLMs) leads to a drop in quality. This paper advances the use of LLMs in clinical applications by presenting a novel multi-agent framework for automatically annotating MI transcripts and predicting clients’ remission. The framework consists of multiple LLM-agents operating in two stages by decomposing the complex task of predicting clients’ remission into simpler subtasks that individual agents can manage. In stage one, a set of reasoning agents generate reasons for annotating utterances by adhering to the Motivational Interviewing Treatment Integrity (MITI). These reasons are used by decision agents to annotate an utterance and create a MI-aware summary of their decision. The MI-aware summary captures the clients’ motivation and resilience to change as induced by the therapist. Once the transcript is annotated, stage two begins with another set of reasoning agents generating reasons for remit or non-remit prediction. A final decision agent then uses the reasoning to predict clients’ remission. The proposed framework outperforms the state of the art, achieving 89% annotation accuracy on the AnnoMI dataset. To evaluate the framework’s ability to predict remission, this paper introduces a novel Clinical MI dataset. The proposed framework achieves 85% accuracy in predicting remission without any training or fine-tuning.

**Решение:** + T1 Motivational Interviewing Treatment Integrity (MITI) utterance coding with LLM multi-agent framework vs AnnoMI human gold standard (89% accuracy, IEEE Access 2026)

---

### 973 · R10172

**Agentic Explainable Artificial Intelligence (Agentic XAI) Approach To Explore Better Explanation: A Case Study in Decision Support for Rice Cultivation in Japan**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2512.21066

Explainable artificial intelligence (XAI) reveals how explanatory variables relate to a response variable, yet communicating XAI outputs to laypersons remains difficult, limiting trust in AI-based predictions. Large language models (LLMs) can translate technical explanations into accessible narratives, but iterative refinement of XAI explanations by an autonomous LLM agent remains unexplored. This study proposes an agentic XAI framework that combines SHapley Additive exPlanations (SHAP) with iterative refinement by a multimodal LLM and tests it as an agricultural recommendation system on rice yield data from 28 fields in Japan. From a SHAP result, the agent explored additional analyses across 11 refinement rounds (Rounds 0-10). Crop scientists (n = 12) and LLM judges (n = 14) scored every round on seven criteria: Specificity, Clarity, Conciseness, Practicality, Contextual Relevance, Cost Consideration, and Crop Science Credibility. Both groups found that refinement raised the average score by 30-33% over Round 0, peaking at Rounds 3-4, after which quality declined, below the starting point for crop scientists. Refinement therefore requires strategic early stopping, which challenges assumptions of monotonic improvement. Criterion-level trajectories indicate a bias-variance trade-off. Early rounds lacked Specificity (bias), whereas excessive iteration eroded Conciseness and raised Cost Consideration through ungrounded economic reasoning (variance). The LLM judges overscored every criterion by 1.4-2.3 points but largely preserved the experts'ranking of rounds (Spearman $\rho$ = 0.58-0.90), so screened LLM judges can flag the quality peak despite unreliable absolute scores. Trustworthy agentic XAI also needs expert-anchored screening of LLM judges and transparent, verifiable refinement records.

**Решение:** -4 agriculture (rice cultivation decision support)

---

### 974 · R6595

**Multidimensional evaluation of generative AI chatbots for public consultation on sudden cardiac death: safety, accuracy, empathy, reliability, quality, and readability across six models**

2026 · BMC Public Health · article · en · https://doi.org/10.1186/s12889-026-29766-z

Generative AI chatbots are increasingly used for health information, but their performance in safety-sensitive sudden cardiac death (SCD) consultation remains insufficiently characterized. This study evaluated six publicly accessible chatbots on SCD-related public questions involving symptom triage, emergency response, CPR/AED use, inherited risk, myocarditis-related concerns, return to exercise, screening, and ICD decision-making. This cross-sectional, comparative, text-level study evaluated ChatGPT Plus 5.5 thinking, Gemini 3.5 Flash, Microsoft Copilot smart, DeepSeek-V4-pro, Doubao, and Perplexity. A standardized set of 56 SCD-related public consultation questions was developed from Google Trends, online forums, public question-answer platforms, clinical guidelines, expert consensus statements, systematic reviews, and qualitative interviews. Each question was submitted once to each chatbot between May 10 and May 16, 2026, yielding 336 model-response items. Five blinded senior cardiology raters assessed safety, accuracy, empathy, DISCERN, EQIP, JAMA benchmark criteria, and GQS. Readability was calculated using six formula-based indices. Between-model comparisons were performed using Cochran’s Q test and Friedman tests, with Kendall’s W reported as the effect size. Responses containing potential safety concerns were additionally examined qualitatively. Inter-rater agreement was high across all manually assessed metrics, with Fleiss’ kappa of 0.856 for Safety and ICC values ranging from 0.801 to 0.887 for other domains. Safe responses predominated across all models, although responses containing potential safety concerns occurred in every chatbot. ChatGPT Plus 5.5 thinking and Perplexity had the highest observed safety proportions during this query window, whereas Doubao had the lowest. Qualitative analysis identified recurrent concerns involving delayed emergency activation for chest pain, syncope, or post-viral symptoms; over-reassurance about prevention; fixed return-to-exercise timelines after infection or COVID-19; pulse-check instructions that could delay CPR; and oversimplified screening, electrolyte, or ICD-related advice. Most flagged responses contained a single potential safety concern. The qualitative severity distribution was concentrated in low and low-to-moderate concerns, whereas higher-severity concerns were less frequent. Accuracy differed significantly across models ( P < 0.001; Kendall’s W = 0.864), with ChatGPT Plus 5.5 thinking, Gemini 3.5 Flash, Microsoft Copilot smart, DeepSeek-V4-pro, and Perplexity achieving similar median scores and Doubao performing lower. Empathy also differed significantly ( P < 0.001; Kendall’s W = 0.531), with DeepSeek-V4-pro having the highest observed score. Significant differences were observed for DISCERN, EQIP, JAMA, GQS, and all readability indices (all P < 0.001). Within this dataset, DeepSeek-V4-pro had the highest DISCERN and EQIP scores and the most favorable readability profile, Gemini 3.5 Flash showed comparable EQIP performance, and Microsoft Copilot smart had the highest JAMA score. However, transparency remained limited overall, and all models produced responses with relatively high reading-grade requirements. In this multidimensional evaluation of six generative AI chatbots for SCD-related public consultation, most responses were safe and clinically relevant, but potential safety concerns occurred across all models. Important limitations involved emergency escalation, CPR/AED guidance, return-to-exercise advice, individualized risk interpretation, transparency, and readability. These tools may support general SCD education, but they should not replace emergency medical services or clinician assessment. Because each question was sampled once during a defined week and all prompts were submitted in English through public interfaces accessed in China, the findings should be interpreted as a time-, language-, and access-specific snapshot rather than a stable ranking of the underlying models. Future development should prioritize evidence-linked content, clear red-flag escalation, plain-language communication, and ongoing expert review.

**Решение:** -4 somatic cardiology (sudden cardiac death consultation)

---

### 975 · R9617

**MULTIVOX: A Benchmark for Evaluating Voice Assistants for Multimodal Interactions**

2025 · Conference on Empirical Methods in Natural Language Processing · journalarticle, conference · https://doi.org/10.18653/v1/2025.emnlp-main.1447

The rapid progress of Large Language Models (LLMs) has empowered omni models to act as voice assistants capable of understanding spoken dialogues. These models can process multimodal inputs beyond text, such as speech and visual data, enabling more context-aware interactions. However, current benchmarks fall short in comprehensively evaluating how well these models generate context-aware responses, particularly when it comes to implicitly understanding fine-grained speech characteristics, such as pitch, emotion, timbre, and volume or the environmental acoustic context such as background sounds. Additionally, they inadequately assess the ability of models to align paralinguistic cues with complementary visual signals to inform their responses. To address these gaps, we introduce MultiVox, the first omni voice assistant benchmark designed to evaluate the ability of voice assistants to integrate spoken and visual cues including paralinguistic speech features for truly multimodal understanding. Specifically, MultiVox includes 1000 human-annotated and recorded speech dialogues that encompass diverse paralinguistic features and a range of visual cues such as images and videos. Our evaluation on 10 state-of-the-art models reveals that, although humans excel at these tasks, current models consistently struggle to produce contextually grounded responses.

**Решение:** -4 voice assistant benchmark

---

### 976 · R1471

**Coding open-ended responses with large language models: Evidence from three economic experiments**

2026 · OSF Preprints (OSF Preprints) · posted-content, preprint, project · https://doi.org/10.2139/ssrn.6805398

This paper examines whether large language models (LLMs) can reliably code openended responses and free-form communication data in experimental economics. We apply three LLMs (GPT, Claude, and Gemini) under alternative prompt designs and temperature settings to data from three published experiments that differ in coding structure, the degree of textual ambiguity, and the role of communication in the experimental design. In a trust game where the coding task targets explicit commitment language, all three models achieve strong agreement with human benchmarks (Cohen's κ &amp;gt; 0.80) and replicate the finding that promise-making predicts cooperative behavior. In thematic coding of explanations for discrepancies between self-and peer-reported AI use, LLMs reliably recover the dominant category but over-identify rare inductively derived categories by a factor of three to five. In multi-label coding of chat communication in a coordination experiment, agreement is weaker and downstream regressions do not replicate consistently, with some coefficients reversing sign. Model choice and temperature are not first-order determinants of performance. The primary constraint is the structural fit between the coding scheme and LLM capabilities: LLMs succeed when categories are deductively defined and explicitly marked in the text, and fail when coding relies on pragmatic inference or inductively derived themes. These findings have direct implications for measurement reliability and analytical transparency in experimental research that uses coded text.</jats:p

**Решение:** -4 experimental economics open-ended response coding

---

### 977 · R0981

**The Structure of Social Situations: Insights From the Large-Scale Automated Coding of Text.**

2026 · Psychological science · journal article, med, journalarticle · eng · https://doi.org/10.1177/09567976261418946

Social situations are key determinants of cognition and behavior, and although several frameworks for representing situations have been proposed, these remain partial, nonintegrated, and not systematically mapped onto the rich space of situations encountered in everyday life. We address this problem by analyzing more than 20,000 detailed textual descriptions of dyadic social interactions obtained from participant-generated stories, published fiction, blogs, and autobiographical narratives. Our main methodological contribution is to use generative artificial intelligence to code these textual descriptions along a very large set of features and derive a detailed taxonomy of situational classes or categories of social interactions. We subsequently relate these situational classes to high-level situational variables like conflict, power, and duty, which have been identified by prior theory. In this way, our article provides a comprehensive, data-driven, and integrative framework for quantifying situational structure, advancing the study of social cognition and behavior.

**Решение:** ? T1 automated coding of 20,000 social situation descriptions using generative AI; check human coder validation on full text

---

### 978 · R7635

**Synthesising Summaries: A novel Retrieval-Augmented Generation-based pipeline for multi-document summarisation**

2025 · dissertation · en · https://doi.org/10.7190/shu-thesis-00719

The rapid growth of scientific literature in recent years has created a requirement for efficient methods to synthesise information from multiple related documents. This thesis addresses this challenge by developing and evaluating novel approaches to multi-document summarisation (MDS) of scientific papers, with a focus on hybrid and deep learning techniques leveraging both extractive and abstractive methods. The research explores the application of state-of-the-art large language models (LLMs), specifically Google's Gemma 2B and 7B models, to the task of scientific literature summarisation. A key innovative approach is the integration of Retrieval-Augmented Generation (RAG) techniques to enhance the summarisation process. The study employs a mixed-methods approach, combining quantitative evaluation metrics with qualitative human assessment and the recently developed novel LLM-as-judge methodology. A comprehensive literature review provides the theoretical foundation, covering the evolution of summarisation techniques, the emergence of transformer-based models, and recent advances in LLMs and related tools and techniques. The experimental design involves fine-tuning embedding models, optimising chunking strategies, and developing a RAG pipeline that integrates retrieval mechanisms with generative LLMs. Results demonstrate significant improvements in summary quality, coherence, and factual accuracy compared to baseline methods. The fine-tuned Gemma models, coupled with RAG techniques, show promise in handling the complexities of scientific text. The study also shows interesting trade-offs between model size and performance, with implications for resource-constrained applications. This research contributes to the field by advancing the state-of-the-art in scientific literature summarisation, providing insights into the effective application of LLMs to this area, and suggesting improved evaluation methodologies. The findings have potential implications for enhancing scientific communication, accelerating literature reviews, and improving access to scientific knowledge.

**Решение:** -6 multi-document summarisation pipeline

---

### 979 · R6523

**Meaning, Computation, and Reasoning: Four Studies**

2026 · eScholarship (California Digital Library) · dissertation · https://escholarship.org/content/qt5471f6f0/qt5471f6f0.pdf

This dissertation brings together four studies. The first two address practical representation, drawing on programming-language semantics and motor representation. The latter two are collaborative studies that develop and test methods for evaluating psychological depth in large language models. The first study examines Carlotta Pavese’s account of practical modes of presentation, in which operational semantic values serve as practical Fregean senses and algorithms as their referents. I show that the account does not establish how distinct operational semantic values can be more fine-grained than an algorithm while sharing it as their referent. I argue that algorithms cannot occupy the intermediate level of granularity between operational semantic values and the functions they compute. The second study develops a positive account of practical representation as a distinctive representational kind. I frame the central dispute as one between a mode of presentation view, in which a task is represented in a distinctively practical way, and a mode of use view, in which ordinary task representations are practically deployed in action. I examine how motor representational format bears on this dispute. I then take Pavese’s capacity-relative view of practical modes of presentation as the starting point for a positive account, and I introduce practical constancies to specify the capacities that play the relevant constitutive role. I propose that motor equivalences instantiate a distinctively practical form of representational constancy by preserving the same operationally articulated task across variations in execution. The third study introduces the Psychological Depth Scale, which is a reader-centered framework for assessing five dimensions of human- and LLM-generated fiction. The study first tests whether human readers can apply the PDS consistently, then examines whether those judgments can be approximated automatically. It finally uses the scale to compare human- and LLM-authored fiction, finding that GPT-4-generated stories score higher than highly rated human-written stories on empathy and narrative complexity and comparably on the remaining dimensions. The fourth study asks whether an LLM-based evaluator validated against human judgments on this original dataset continues to track human judgments when deployed on closely matched frontier-model outputs. Human readers show no uniform preference for reasoning-enhanced models, whereas the automated judge shows an almost uniform preference for reasoning-model outputs. Agreement with human ratings on one dataset therefore does not guarantee that an automated evaluator will track human judgments on a different distribution of outputs, especially when those judgments are subjective. Through philosophical and empirical inquiry, the dissertation seeks to address questions concerning meaning, computation, and reasoning.

**Решение:** -1 philosophical dissertation on meaning and computation

---

### 980 · R11643

**AUTOMATED DETECTION OF EMOTION IN CENTRAL BANK COMMUNICATION: A WARNING**

2024 · National Institute Economic Review · journalarticle, article · en · https://doi.org/10.1017/nie.2024.31

Abstract Central banks have increased their official communications. Previous literature measures complexity, clarity, tone and sentiment. Less explored is the use of fact versus emotion in central bank communication. We test a new method for classifying factual versus emotional language, applying a pretrained transfer learning model, fine-tuned with manually coded, task-specific and domain-specific data sets. We find that the large language models outperform traditional models on some occasions; however, the results depend on a number of choices. We therefore caution researchers from depending solely on such models even for tasks that appear similar. Our findings suggest that central bank communications are not only technically but also subjectively difficult to understand.

**Решение:** -4 central bank macroeconomic communications

---

### 981 · R7854

**SELF-PERCEPT: Introspection Improves Large Language Models' Detection of Multi-Person Mental Manipulation in Conversations**

2025 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2505.20679

Mental manipulation is a subtle yet pervasive form of abuse in interpersonal communication, making its detection critical for safeguarding potential victims. However, due to manipulation's nuanced and context-specific nature, identifying manipulative language in complex, multi-turn, and multi-person conversations remains a significant challenge for large language models (LLMs). To address this gap, we introduce the MultiManip dataset, comprising 220 multi-turn, multi-person dialogues balanced between manipulative and non-manipulative interactions, all drawn from reality shows that mimic real-world scenarios. For manipulative interactions, it includes 11 distinct manipulations depicting real-life scenarios. We conduct extensive evaluations of state-of-the-art LLMs, such as GPT-4o and Llama-3.1-8B, employing various prompting strategies. Despite their capabilities, these models often struggle to detect manipulation effectively. To overcome this limitation, we propose SELF-PERCEPT, a novel, two-stage prompting framework inspired by Self-Perception Theory, demonstrating strong performance in detecting multi-person, multi-turn mental manipulation. Our code and data are publicly available at https://github.com/danushkhanna/self-percept . Accepted to ACL 2025 (Main)

**Решение:** ? T1 detection and classification of 11 mental manipulation types in conversations (MultiManip dataset); check human annotator agreement on full text

---

### 982 · R9136

**Human Experts' Evaluation of Generative AI for Contextualizing STEAM Education in the Global South**

2025 · arXiv.org · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2511.19482

STEAM education in many parts of the Global South remains abstract and weakly connected to learners sociocultural realities. This study examines how human experts evaluate the capacity of Generative AI (GenAI) to contextualize STEAM instruction in these settings. Using a convergent mixed-methods design grounded in human-centered and culturally responsive pedagogy, four STEAM education experts reviewed standardized Ghana NaCCA lesson plans and GenAI-generated lessons created with a customized Culturally Responsive Lesson Planner (CRLP). Quantitative data were collected with a validated 25-item Culturally Responsive Pedagogy Rubric assessing bias awareness, cultural representation, contextual relevance, linguistic responsiveness, and teacher agency. Qualitative reflections provided additional insight into the pedagogical and cultural dynamics of each lesson. Findings show that GenAI, especially through the CRLP, improved connections between abstract standards and learners lived experiences. Teacher Agency was the strongest domain, while Cultural Representation was the weakest. CRLP-generated lessons were rated as more culturally grounded and pedagogically engaging. However, GenAI struggled to represent Ghana's cultural diversity, often producing surface-level references, especially in Mathematics and Computing. Experts stressed the need for teacher mediation, community input, and culturally informed refinement of AI outputs. Future work should involve classroom trials, broader expert participation, and fine-tuning with Indigenous corpora.

**Решение:** -4 STEAM education pedagogical evaluation

---

### 983 · R10879

**On the Categorization of Corporate Multimodal Disinformation with Large Language Models**

2024 · CODAI@ECAI · journalarticle

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 corporate multimodal disinformation

---

### 984 · R2162

**Evaluating Large Language Models as Classifiers (LLM-as-rater) for Hospital Incident Reports**

2026 · Open Science Framework · studyregistration/pre-registration, other, preprint · https://doi.org/10.17605/osf.io/b4nre

This research project evaluates the capability of five frontier Large Language Models (LLMs)—ChatGPT, Gemini, Claude, DeepSeek, and Mistral—to act as blinded classifiers ("LLM-as-rater") for hospital Incident Reporting (IR). The primary purpose is to assess whether these models can accurately replicate the classification tasks typically performed by human raters, relying exclusively on free-text narrative descriptions (e.g., "Where", "What happened", "How and why it happened", "Description") without access to prior structured human classifications. The study is designed as an observational, retrospective agreement study based on a source dataset of 1,988 incident reports collected at the Policlinico di Bari (Italy) and its affiliated facilities between 2015 and 2025. To ensure robust evaluation on clinically and medico-legally relevant scenarios, the analysis is conducted on an extended sample of 824 cases. This sample combines a "discriminating core" of 624 difficult cases (which includes all severe harm events, deaths, and cases with inter-rater disagreement or reclassification) and a "population anchor" of 200 random, straightforward cases. Post-stratification weights are then applied to these strata to re-anchor the performance estimates to the real-world population distribution. The project focuses on three main comparative evaluations: AI vs. Expert Gold Standard: Measuring the agreement between the model's classification and the final expert consensus. AI vs. Human Benchmark: Comparing the model's performance against the initial classification provided by the front-line professional who reported the event. Algorithmovigilance (AI vs. AI): Analyzing cross-model agreement to determine if different models share the same systematic biases or correlated errors, effectively agreeing with each other more often than they agree with human experts. The primary outcome is the level of agreement on the severity of harm, which is measured on a five-level ordinal scale. Secondary outcomes include: Accuracy in identifying the specific event type across 16 controlled categories. Triage capability, measured by the model's sensitivity and specificity in predicting whether a review of the Electronic Health Record (EHR) is necessary. Confidence calibration, evaluated via the Expected Calibration Error (ECE) to see if a model's stated confidence aligns with its actual accuracy. An indirect knowledge cutoff probe, testing whether models correctly apply an updated (July 2024) 23-item list of sentinel events from the Italian Ministry of Health instead of the legacy 16-item list. Expected outcomes include a comprehensive framework for understanding LLM reliability in clinical risk management. The study aims to map specific AI failure modes—such as chronic overconfidence, over-reliance on medical records, or failure to update domain knowledge—and to provide empirical evidence on the phenomenon of "shared bias" among frontier models in a specialized medico-legal context.

**Решение:** -1 pre-registration protocol on hospital incident reports

---

### 985 · R10278

**Prompt Engineering an Informational Chatbot for Education on Mental Health Using a Multiagent Approach for Enhanced Compliance With Prompt Instructions: Algorithm Development and Validation.**

2025 · JMIR AI · journal article, journalarticle, article · eng · https://doi.org/10.2196/69820

BACKGROUND: People with schizophrenia often present with cognitive impairments that may hinder their ability to learn about their condition. Education platforms powered by large language models (LLMs) have the potential to improve the accessibility of mental health information. However, the black-box nature of LLMs raises ethical and safety concerns regarding the controllability of chatbots. In particular, prompt-engineered chatbots may drift from their intended role as the conversation progresses and become more prone to hallucinations. OBJECTIVE: This study aimed to develop and evaluate a critical analysis filter (CAF) system that ensures that an LLM-powered prompt-engineered chatbot reliably complies with its predefined instructions and scope while delivering validated mental health information. METHODS: For a proof of concept, we prompt engineered an educational chatbot for schizophrenia powered by GPT-4 that could dynamically access information from a schizophrenia manual written for people with schizophrenia and their caregivers. In the CAF, a team of prompt-engineered LLM agents was used to critically analyze and refine the chatbot's responses and deliver real-time feedback to the chatbot. To assess the ability of the CAF to re-establish the chatbot's adherence to its instructions, we generated 3 conversations (by conversing with the chatbot with the CAF disabled) wherein the chatbot started to drift from its instructions toward various unintended roles. We used these checkpoint conversations to initialize automated conversations between the chatbot and adversarial chatbots designed to entice it toward unintended roles. Conversations were repeatedly sampled with the CAF enabled and disabled. In total, 3 human raters independently rated each chatbot response according to criteria developed to measure the chatbot's integrity, specifically, its transparency (such as admitting when a statement lacked explicit support from its scripted sources) and its tendency to faithfully convey the scripted information in the schizophrenia manual. RESULTS: In total, 36 responses (3 different checkpoint conversations, 3 conversations per checkpoint, and 4 adversarial queries per conversation) were rated for compliance with the CAF enabled and disabled. Activating the CAF resulted in a compliance score that was considered acceptable (≥2) in 81% (7/36) of the responses, compared to only 8.3% (3/36) when the CAF was deactivated. CONCLUSIONS: Although more rigorous testing in realistic scenarios is needed, our results suggest that self-reflection mechanisms could enable LLMs to be used effectively and safely in educational mental health platforms. This approach harnesses the flexibility of LLMs while reliably constraining their scope to appropriate and accurate interactions.

**Решение:** -6 educational chatbot development for schizophrenia without text coder agreement

---

### 986 · R6729

**Multi-Dimensional Prosody Judgment For Live Streaming Speech Synthesis**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.20124

Evaluating live streaming speech synthesis (TTS) requires assessing fine-grained, highly expressive prosody such as emotion, intonation, and energy which traditional MOS predictors fail to capture. While proprietary Large Language Models (LLMs) like Gemini can evaluate these aspects, they are too costly for massive inference and reinforcement learning feedback. To address this, we first introduce Live-ProsodyJudge (LPJ), a cost-effective pairwise evaluator distilled from Gemini into Qwen3-Omni. However, we identify a critical flaw in standard multi-dimensional evaluation: verdict coupling. The judge tends to lazily align all individual dimension scores with its overall preference, collapsing a rich multi-dimensional rubric into a single preference bit. To resolve this, we further propose Decoupled-Live-ProsodyJudge (D-LPJ). D-LPJ eliminates the overall verdict target to prevent blind following, masks uncertain pair-dimensions during Supervised Fine-Tuning(SFT), and introduces a novel span-local GRPO strategy that applies normalized advantages strictly to their corresponding rationale spans. Evaluated on highly curated human-annotated test sets, 10 sample balanced-order LPJ achieves higher point accuracy than a single Gemini call, while D-LPJ successfully produces independent,decoupled dimension judgments. Furthermore, in a Best-of-8 TTS candidate selection tournament, the LPJ-selected utterance falls within the human top-3 in 85.29% of high-confidence cases, demonstrating its efficacy for fine-grained TTS preference optimization.

**Решение:** -4 speech synthesis prosody evaluation

---

### 987 · R10923

**Small-Scale Testing on Generative AI and Post-OCR Correction in Historical Datasets**

2024 · Zenodo · text/poster · https://doi.org/10.5281/zenodo.11403646

This article proposes a small-scale investigation on the use of generative AI agents for post-OCR correction in historical datasets. Three chatbots, ChatGPT-4, Google Bard and YouChat and excerpts from 18th century French texts were utilised. The evaluation included qualitative and quantitative methods. Character and word error rates (CER, WER) were computed both by the agents and independently using a specialised Python library and gold standard fragments from the ICDAR 2017 competition on post-OCR text correction.

**Решение:** -4 historical text OCR correction

---

### 988 · R3204

**Measuring therapeutic alliance with chatbots**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/zvk2x

This study investigates whether a therapeutic alliance can emerge between lay users and Chatbots during naturalistic use. Participants who use ChatGPT and other chatbots for counseling or therapeutic purposes will complete an anonymous online survey assessing therapeutic alliance (WAI-SR, HAQ), mental health (PHQ-4), personality (BFI-10), technology readiness (TRI 2.0), and demographic and clinical characteristics. The primary aim is to examine the strength and factor structure of the therapeutic alliance with chatbot. Secondary analyses will explore associations with personality, technology readiness, mental health, psychotherapy experience, and chatbot use. Findings will improve our understanding of therapeutic relationships with generative AI and inform future AI-supported mental health interventions. Interim analyses may be conducted on subsets of the data for educational purposes (e.g., student theses). These analyses will not influence the preregistered hypotheses, sample size, stopping rule, or primary analyses, which will be conducted only after completion of data collection.

**Решение:** -1 pre-registration protocol on user survey of therapeutic alliance with chatbots

---

### 989 · R11985

**Realistic Evaluation of Toxicity in Large Language Models**

2024 · Annual Meeting of the Association for Computational Linguistics · journalarticle, conference, preprint/article · en · https://doi.org/10.18653/v1/2024.findings-acl.61

Large language models (LLMs) have become integral to our professional workflows and daily lives. Nevertheless, these machine companions of ours have a critical flaw: the huge amount of data which endows them with vast and diverse knowledge, also exposes them to the inevitable toxicity and bias. While most LLMs incorporate defense mechanisms to prevent the generation of harmful content, these safeguards can be easily bypassed with minimal prompt engineering. In this paper, we introduce the new Thoroughly Engineered Toxicity (TET) dataset, comprising manually crafted prompts designed to nullify the protective layers of such models. Through extensive evaluations, we demonstrate the pivotal role of TET in providing a rigorous benchmark for evaluation of toxicity awareness in several popular LLMs: it highlights the toxicity in the LLMs that might remain hidden when using normal prompts, thus revealing subtler issues in their behavior. Findings of ACL 2024

**Решение:** -4 general toxicity evaluation benchmark

---

### 990 · R5832

**Towards Uncovering Indoor Satisfaction Profiles: LLM Capacity for Structured Extraction from Occupant Feedback**

2026 · Sustainability Week · journalarticle, book, review · https://doi.org/10.1145/3765611.3815502

Local large language models (LLM) offer a scalable, privacy-preserving approach to extracting structured attributes from free text from built environment occupant surveys, but there is little guidance on what model capacity is needed for reliable extraction. We address this gap with a validation study comparing three locally deployed LLM models (3B, 8B, 27B parameters) on structured complaint-style extraction from 6,283 post-occupancy evaluation survey narratives focused on categories of indoor environmental quality. The 3B model produces near-random classifications (κ < 0.15), the 8B model achieves only slight to fair agreement (κ = 0.05–0.33), and the 27B model reaches moderate agreement with human coding (κ = 0.44–0.58). We contextualise this finding within a reproducible pipeline that integrates latent profile analysis of 16 indoor environmental satisfaction items (n = 39,149), identifying eight occupant profiles, with LLM-based extraction of complaint tone, severity, attribution, and work impact. A classification benchmark shows that neither text content nor LLM-extracted features predict profile membership beyond chance, establishing that satisfaction profiles and complaint text capture independent constructs. This work prototypes a framework for the forensic characterization of the diversity of personal subjective experience in indoor built environments.

**Решение:** -4 building indoor satisfaction occupant feedback

---

### 991 · R9174

**Automated Scoring of Creative Achievement**

2025 · PsyArXiv · journalarticle, preprint, ppr · en · https://doi.org/10.31234/osf.io/rk6yp_v1

ABSTRACT The assessment of creative achievement (CA) can be cumbersome as participants are typically asked to respond to long lists of possible accomplishments that may still miss their very specific achievements. A bottom‐up alternative is to let participants openly report their most significant CAs, which, however, involves more complex scoring such as via human ratings. In this study, we investigated whether language models (LMs) can provide an efficient and valid scoring of such open‐ended responses. Across two data sets, participants described their three most significant CAs. These responses were rated by human judges and by three LMs (Llama 3.1–8B, Llama 3.3–70B, GPT‐4o) using zero‐shot prompting. Correlations between human and LM ratings were consistently high ( r = 0.53–0.80), and criterion validity evidence of LM‐based scores was largely on par with rater‐based scores. In addition, we examined zero‐shot domain classification of CAs into nine creative domains (e.g., music, visual arts). Classification accuracy was 62.3% overall; closer inspection suggested that automated classification has the potential to unveil conceptual overlaps between domains and to identify CAs involving multiple domains. Taken together, automated scoring of CA via LMs represents a promising and efficient alternative to traditional CA measures by approximating human ratings and providing useful domain classifications.

**Решение:** + T2 automated scoring of open-ended creative achievement descriptions: 3 LLMs vs human judges (r = 0.53-0.80, PsyArXiv 2025)

---

### 992 · R2663

**Stroke Lesions as a Rosetta Stone for Language Model Interpretability**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2602.04074

Large language models (LLMs) have achieved remarkable capabilities, yet methods to verify which model components are truly necessary for language function remain limited. Current interpretability approaches rely on internal metrics and lack external validation. Here we present the Brain-LLM Unified Model (BLUM), a framework that leverages lesion-symptom mapping, the gold standard for establishing causal brain-behavior relationships for over a century, as an external reference structure for evaluating LLM perturbation effects. Using data from individuals with chronic post-stroke aphasia (N = 410), we trained symptom-to-lesion models that predict brain damage location from behavioral error profiles, applied systematic perturbations to transformer layers, administered identical clinical assessments to perturbed LLMs and human patients, and projected LLM error profiles into human lesion space. LLM error profiles were sufficiently similar to human error profiles that predicted lesions corresponded to actual lesions in error-matched humans above chance in 67% of picture naming conditions (p &lt; 10^{-23}) and 68.3% of sentence completion conditions (p &lt; 10^{-61}), with semantic-dominant errors mapping onto ventral-stream lesion patterns and phonemic-dominant errors onto dorsal-stream patterns. These findings open a new methodological avenue for LLM interpretability in which clinical neuroscience provides external validation, establishing human lesion-symptom mapping as a reference framework for evaluating artificial language systems and motivating direct investigation of whether behavioral alignment reflects shared computational principles. 45 pages, 17 figures

**Решение:** -4 neuroscience stroke lesion interpretability mapping

---

### 993 · R4324

**Integration of generative AI in creative mathematics learning: A correlational analysis between the quality of prompts and the logical reasoning of student teachers in the education degree programme**

2026 · Revista de Educación a Distancia (RED) · journalarticle, article · en · https://doi.org/10.6018/red.716941

The presence of Generative Artificial Intelligence (GenAI) based on Large Language Models (LLMs) such as ChatGPT, Gemini, and Claude has triggered a massive paradigm shift in mathematics education. GenAI no longer functions as an information search engine (Luo et al., 2025); it has evolved into a cognitive partner capable of performing complex mathematical reasoning. The integration of GenAI into creative mathematics learning is particularly important because it enables students to explore multiple solution strategies, develop original mathematical ideas, and refine their reasoning through continuous interaction and feedback. As creativity in mathematics requires both divergent thinking and logical justification, GenAI provides opportunities for students to articulate, evaluate, and improve their mathematical arguments in real time. Various recent studies show that the use of artificial intelligence in STEM education can enhance student engagement and offer personalised learning (Huang et al., 2025; Nikhil, 2025). However, the transition from conventional learning to AI-based interaction presents new pedagogical challenges, particularly regarding how students communicate with machines to structure their mathematical thinking.

**Решение:** -4 mathematics teacher education

---

### 994 · R7117

**Enabling Trait-based Personality Simulation in Conversational LLM Agents: Case Study of Customer Assistance in French**

2025 · International Workshop on Spoken Dialogue Systems Technology · journalarticle

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 conversational agent customer assistance simulation

---

### 995 · R9147

**Do large language models Dunning-Kruger?**

2025 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/4naty_v1

Human judgments typically demonstrate an overconfidence pattern, especially for low performers (i.e., the Dunning-Kruger effect (DKE; Kruger &amp; Dunning, 1999). This effect has been shown to extend to a variety of metacognitive judgment tasks, including judgments learning (JOLs) and judgments of associative memory (JAMs). Across these tasks, perceived relatedness produces inflated memory predictions. The present study explored whether large language models (LLMs) similarly exhibit this effect. We used a modified JAM task based on Maxwell and Buchanan (2020), which assessed three types of word pair relationships: Associative (i.e., probability of cue eliciting target in free association tasks), semantic (i.e., degree of feature overlap), and thematic (i.e., likelihood of co-occurrence within the same narrative context). This judgment of relatedness task (JOR) was adapted for BERT using surprisal values, which estimate how expected a target word is for a given cue. LLM JOR patterns were then compared to human JAMs first reported by Maxwell and Buchanan (2020). Overall, humans showed a classic overestimation pattern (high intercepts and shallow slopes). However, BERT surprisals were minimally sensitive to differences in word relations (i.e., near-zero or negative slopes) but showed higher bias compared to humans (i.e., elevated intercepts). Taken together, our findings suggest that LLMs do not exhibit the classic DKE pattern, though they are prone to overestimation. Instead, LLMs appear to uniformly overestimate word pair relatedness.

**Решение:** -2 LLM evaluated as test subject for Dunning-Kruger effect

---

### 996 · R2015

**How do LLMs Evaluate Perceived Moral Agency? Investigating Moral Decision-Making in Human-Artificial Agents Interactions**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.05037

As LLMs take on roles requiring moral advice, understanding how they attribute moral agency becomes critical. Humans possess moral agency, the capacity to make ethically guided decisions and bear responsibility for their consequences, a well-established construct in moral psychology. Yet as artificial agents (AAs) such as robots, drones, and disembodied AI systems become increasingly embedded in smart city environments, the question of whether and how moral agency is attributed to them takes on new urgency. This paper presents, to the best of our knowledge, the first empirical study comparing how humans and LLMs evaluate perceived moral agency (PMA) across human and autonomous artificial agents varying in embodiment, situated in plausible smart city scenarios. Using an adaptation of a validated PMA scale, we applied a protocol to 190 human participants as well as various LLMs. Our evaluation reveals higher perceptions of moral agency in humans than in AAs. However, when facing moral dilemmas in concrete scenarios, LLMs reason outward from the situation, prioritizing harm severity and contextual urgency over any stable assessment of the agent itself, amplifying a context-sensitivity also present in human raters. These findings are particularly relevant as LLMs become increasingly involved in everyday moral decisions. 43 pages, 14 figures, 29 tables. Preprint under review

**Решение:** -6 moral agency attribution in human-AI interaction without text coder agreement

---

### 997 · R11397

**Reconstruct Your Previous Conversations! Comprehensively Investigating Privacy Leakage Risks in Conversations with GPT Models**

2024 · arXiv (Cornell University) · audiovisual/conference talk, conferenceproceeding/conference contribution, journalarticle · en · https://doi.org/10.48550/arxiv.2402.02987

Significant advancements have recently been made in large language models represented by GPT models. Users frequently have multi-round private conversations with cloud-hosted GPT models for task optimization. Yet, this operational paradigm introduces additional attack surfaces, particularly in custom GPTs and hijacked chat sessions. In this paper, we introduce a straightforward yet potent Conversation Reconstruction Attack. This attack targets the contents of previous conversations between GPT models and benign users, i.e., the benign users' input contents during their interaction with GPT models. The adversary could induce GPT models to leak such contents by querying them with designed malicious prompts. Our comprehensive examination of privacy risks during the interactions with GPT models under this attack reveals GPT-4's considerable resilience. We present two advanced attacks targeting improved reconstruction of past conversations, demonstrating significant privacy leakage across all models under these advanced techniques. Evaluating various defense mechanisms, we find them ineffective against these attacks. Our findings highlight the ease with which privacy can be compromised in interactions with GPT models, urging the community to safeguard against potential abuses of these models' capabilities. Accepted in EMNLP 2024. 14 pages, 10 figures

**Решение:** -4 cybersecurity privacy leakage in LLM conversations

---

### 998 · R2922

**Crisis Management LLM Benchmark (C1–C16): Scenario Corpus, Reference Standards, Expert Ratings, and Analysis Scripts**

2026 · OSF Preprints (OSF Preprints) · dataset/project, preprint · https://doi.org/10.17605/osf.io/a8jd2

This repository contains the complete data, materials, and analysis code supporting the study "How Well Can Large Language Models Manage Intraoperative Crisis? A Multicenter Blinded Benchmark on 16 Anaesthesia Scenarios". Contents: (1) scenario_corpus_C1-C16.xlsx — 16 clinical scenarios with prompt context, time-critical first-line action, and reference-standard decision tree. (2) reference_standards.xlsx — guideline-anchored reference decisions, cross-referenced to AHA 2020, ESAIC 2022, ASA difficult-airway 2022, and other current guidelines. (3) expert_ratings_blinded.xlsx — de-identified accuracy ratings from 3 board-certified anaesthetists (double-blinded, randomised order). (4) fixed_prompt_template.txt — the exact prompt fed to every evaluated model. (5) analysis_scripts/ — R / Python scripts that reproduce all tables (Table 1–3) and figures (Fig. 1–3; Supplementary Fig. S1). (6) README.md — column-level data dictionary and reproducibility instructions (random seeds, package versions). Scope of sharing: All identifiers removed. No protected health information. No human-subject IRB was required (simulation-only evaluation). License: CC-BY 4.0. Suggested citation will be added upon manuscript acceptance.

**Решение:** -4 somatic anaesthesia intraoperative crisis benchmark

---

### 999 · R6341

**Applying Anomaly Detection Methods to Google Search Logs to Detect Periods Preceding Suicide Attempts (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.93274

BACKGROUND Suicide is a major global public health concern and a leading cause of death worldwide. However, timely identification of individuals at elevated risk remains challenging. Traditional suicide risk assessment relies heavily on self-report and structured screening tools, which are often limited by infrequent monitoring, social stigma surrounding mental health issues, and restricted access to mental health services. As individuals increasingly rely on web search engines for everyday information seeking, personal search data offer a unique opportunity to capture signals related to suicide risk. OBJECTIVE This study aimed to quantitatively evaluate the utility of personal Google search logs for detecting periods preceding suicide attempts using anomaly detection methods. METHODS A subset of personal Google search data collected in a retrospective-prospective study, focusing on 80 adult participants who reported suicide attempt dates (n=111) with sufficient detail to enable identification of high-risk periods, was used for analysis. Neural language representation techniques were developed to calculate a proximity score between each search query and constructs representing known suicide warning signs, reflecting search behavior related to suicide risk. The semantic feature construction framework, consists of initial proximity based filtering on query-construct relatedness by a smaller-scale language model and further adjudication by a state-of-the-art large language model (Llama 3.1), was feasible for application to large-scale web search data. Anomaly detection methods were applied to semantic and behavioral features of search activity to identify time periods (14 days) preceding the suicide attempts. Models were trained on search data more than 6 months prior to the attempt and evaluated over the 180 days preceding and including the attempt date. The ROC AUC score was used to evaluate how effectively the model distinguished attempt periods from non-attempt periods. RESULTS The majority of analyzed suicide attempts were effectively distinguished from non-attempt periods. The best-performing anomaly detection model achieved a median ROC AUC score of 0.75 across attempts. Individually trained models outperformed generalized models trained on normative data from all participants. Semantic features that characterized search content’s relatedness to constructs contributed more substantially to the anomaly detection performance than behavioral features. Substantial differences in search feature importance were observed across participants, while consistent feature importance was found within the attempt histories of the same participant. Results from the ablation study demonstrated the utility of large language models in adjudicating the validity of construct-to-search relationships. CONCLUSIONS This study showed that personal Google search logs can be a valuable resource for suicide risk detection. The proposed framework has the potential to support the development of automated suicide risk detection tools for more timely identification of individuals at elevated risk.

**Решение:** -6 anomaly detection on Google search logs to predict suicide attempts

---

### 1000 · R8583

**The Applications of Large Language Models in Mental Health: Scoping Review.**

2025 · Journal of medical Internet research · journal article, scoping review, review · eng · https://doi.org/10.2196/69284

BACKGROUND: Mental health is emerging as an increasingly prevalent public issue globally. There is an urgent need in mental health for efficient detection methods, effective treatments, affordable privacy-focused health care solutions, and increased access to specialized psychiatrists. The emergence and rapid development of large language models (LLMs) have shown the potential to address these mental health demands. However, a comprehensive review summarizing the application areas, processes, and performance comparisons of LLMs in mental health has been lacking until now. OBJECTIVE: This review aimed to summarize the applications of LLMs in mental health, including trends, application areas, performance comparisons, challenges, and prospective future directions. METHODS: A scoping review was conducted to map the landscape of LLMs' applications in mental health, including trends, application areas, comparative performance, and future trajectories. We searched 7 electronic databases, including Web of Science, PubMed, Cochrane Library, IEEE Xplore, Weipu, CNKI, and Wanfang, from January 1, 2019, to August 31, 2024. Studies eligible for inclusion were peer-reviewed articles focused on LLMs' applications in mental health. Studies were excluded if they (1) were not peer-reviewed or did not focus on mental health or mental disorders or (2) did not use LLMs; studies that used only natural language processing or long short-term memory models were also excluded. Relevant information on application details and performance metrics was extracted during the data charting of eligible articles. RESULTS: A total of 95 articles were drawn from 4859 studies using LLMs for mental health tasks. The applications were categorized into 3 key areas: screening or detection of mental disorders (67/95, 71%), supporting clinical treatments and interventions (31/95, 33%), and assisting in mental health counseling and education (11/95, 12%). Most studies used LLMs for depression detection and classification (33/95, 35%), clinical treatment support and intervention (14/95, 15%), and suicide risk prediction (12/95, 13%). Compared with nontransformer models and humans, LLMs demonstrate higher capabilities in information acquisition and analysis and efficiently generating natural language responses. Various series of LLMs also have different advantages and disadvantages in addressing mental health tasks. CONCLUSIONS: This scoping review synthesizes the applications, processes, performance, and challenges of LLMs in the mental health field. These findings highlight the substantial potential of LLMs to augment mental health research, diagnostics, and intervention strategies, underscoring the imperative for ongoing development and ethical deliberation in clinical settings.

**Решение:** -1 scoping review of LLMs in mental health
