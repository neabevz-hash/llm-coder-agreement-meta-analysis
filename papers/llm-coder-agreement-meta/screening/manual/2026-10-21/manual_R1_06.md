# Ручной отбор, часть 6

Ручной отбор, часть 6: записи 751–900 из 1000. Эти записи вы размечаете сами, вместо проходов ИИ (deviations.md, D3); это случайные 1000 записей из тех, что ИИ ещё не разметил (зерно 20261024). **Меток ИИ здесь нет и не будет.** Ваше решение окончательное: «+» и «?» идут на полный текст. Размечайте в любом порядке и в несколько заходов.

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

### 751 · R10534

**On Evaluating LLM Alignment by Evaluating LLMs as Judges**

2025 · neural information processing systems · journalarticle, preprint/article, conference-paper · https://doi.org/10.52202/085713-5051

Alignment with human preferences is an important evaluation aspect of LLMs, requiring them to be helpful, honest, safe, and to precisely follow human instructions. Evaluating large language models' (LLMs) alignment typically involves directly assessing their open-ended responses, requiring human annotators or strong LLM judges. Conversely, LLMs themselves have also been extensively evaluated as judges for assessing alignment. In this work, we examine the relationship between LLMs' generation and evaluation capabilities in aligning with human preferences. To this end, we first conduct a comprehensive analysis of the generation-evaluation consistency (GE-consistency) among various LLMs, revealing a strong correlation between their generation and evaluation capabilities when evaluated by a strong LLM preference oracle. Utilizing this finding, we propose a benchmarking paradigm that measures LLM alignment with human preferences without directly evaluating their generated outputs, instead assessing LLMs in their role as evaluators. Our evaluation shows that our proposed benchmark, AlignEval, matches or surpasses widely used automatic LLM evaluation benchmarks, such as AlpacaEval and Arena-Hard, in capturing human preferences when ranking LLMs. Our study offers valuable insights into the connection between LLMs' generation and evaluation capabilities, and introduces a benchmark that assesses alignment without directly evaluating model outputs. NeurIPS 2025 Camera Ready

**Решение:** -6 AlignEval benchmark evaluating LLMs as judges of general alignment

---

### 752 · R0171

**What Drives Engagement With Fundraising Messages on Social Media? Insights From an LLM ‐Assisted Approach**

2026 · Journal of Philanthropy · journalarticle, article · en · https://doi.org/10.1002/nvsm.70067

ABSTRACT Nonprofit organizations increasingly rely on social media platforms for fundraising, yet little is known about which message features effectively drive online engagement. This study investigates how content cues including informativeness, emotional tone, urgency, and inclusiveness, together with format cues such as hashtags, emojis, and message length, shape audience reactions to charitable appeals. Drawing on 18,257 fundraising‐related posts on X (formerly Twitter), we applied a hybrid coding approach that combined manual annotation with large language model assistance. Our findings reveal that informativeness alone suppresses engagement (likes and shares) unless paired with positive emotionality, challenging the assumption of its uniform effectiveness. Engagement dimensions (likes, shares, and comments) respond differently to message features, reflecting distinct motivations. Additionally, credibility cues, such as verification status and source type (individual vs. organizational), play a critical role in shaping authenticity and audience impact. By uncovering these heterogeneous dynamics, the study conceptualizes engagement as multidimensional and offers nonprofit organizations practical guidance for tailoring appeals to align with specific fundraising objectives.

**Решение:** -4 social media fundraising messages engagement features

---

### 753 · R11941

**TrinityAI: towards trustworthy, resilient, and interpretable AI for high-assurance applications**

2024 · conference-paper · en · https://doi.org/10.1117/12.3032623

In this talk, we will describe TrinityAI - a neuro-symbolic artificial intelligence (AI) architecture being developed for detecting complex events across varied environments. Complex events are scenarios composed of multiple atomic events that occur over different times and locations, involving various actors. TrinityAI aims to enhance monitoring and situational awareness in critical applications such as healthcare, surveillance for public security, and traffic monitoring. The desiderata of AI needed to detect such complex events include the following: first, we need multimodal perception in very high dimension; second, we need to reason to compose atomic events and infer complex event; and finally, we need the capability to ingest background knowledge from human experts, and provide symbolic justification of AI decisions back to the human users. TrinityAI satisfies these requirements and its architecture is motivated by predictive processing - a theory of mind which posits that human cognition is not bottom-up wherein we attach meanings to our perceptions in isolation from each other but instead we build models or narratives of the world and use that to interpret our sensed perceptions. This model-based perception is key to the robustness and context-sensitivity of our sensing and decision-making. TrinityAI has a three-layered architecture composing deep neural networks, foundation models, and logic programming with each layer designated to handle specific tasks ranging from raw data perception to high-level reasoning and inference.

**Решение:** -4 TrinityAI neuro-symbolic AI for complex event detection

---

### 754 · R7617

**Deciphering Emotions in Children’s Storybooks: A Comparative Analysis of Multimodal LLMs in Educational Applications**

2025 · AI · journalarticle, preprint/article, article · en · https://doi.org/10.3390/ai6090211

Emotion recognition capabilities in multimodal AI systems are crucial for developing culturally responsive educational technologies yet remain underexplored for Arabic language contexts, where culturally appropriate learning tools are critically needed. This study evaluated the emotion recognition performance of two advanced multimodal large language models, GPT-4o and Gemini 1.5 Pro, when processing Arabic children’s storybook illustrations. We assessed both models across three prompting strategies (zero-shot, few-shot, and chain-of-thought) using 75 images from seven Arabic storybooks, comparing model predictions with human annotations based on Plutchik’s emotional framework. GPT-4o consistently outperformed Gemini across all conditions, achieving the highest macro F1-score of 59% with chain-of-thought prompting compared to Gemini’s best performance of 43%. Error analysis revealed systematic misclassification patterns, with valence inversions accounting for 60.7% of errors, while both models struggled with culturally nuanced emotions and ambiguous narrative contexts. These findings highlight fundamental limitations in current models’ cultural understanding and emphasize the need for culturally sensitive training approaches to develop effective emotion-aware educational technologies for Arabic-speaking learners.

**Решение:** -4 emotion recognition in children storybooks with multimodal LLMs in Arabic

---

### 755 · R5645

**MindScope: A Multi-Modal Mental Wellness Monitoring System using Large Language Models and Facial Expression Analysis**

2026 · Zenodo (CERN European Organization for Nuclear Research) · journalarticle/, article · https://doi.org/10.5281/zenodo.19945540

Mental health monitoring remains a critical challenge due to the subjective nature of self-reported assessments and the infrequency of clinical evaluations. This paper presents MindScope, a multi-modal wellness monitoring system that integrates Natural Language Processing (NLP) analysis of free-text journal entries with real-time AI-powered facial expression detection to produce a comprehensive psychological indicator profile. The system employs the Groq-accelerated LLaMA 3.1 (70B parameters) for structured sentiment extraction and LLaMA 3.2 Vision (11B parameters) for facial emotion recognition via standard webcam. A novel Three-Channel Discrepancy Engine compares three independent data signals — subjective self-reported mood ratings, NLP-derived sentiment valence, and AI-detected facial valence — to compute an emotional incongruence score. Discrepancy values exceeding a threshold of 30 points are flagged as potential Emotional Masking, a clinically significant pattern associated with affective suppression. The system outputs structured JSON comprising mood stability, anxiety markers, clinical indicators (anhedonia, fatigue, sleep disturbance), ten cognitive distortion categories, and a unified risk classification (Green/Yellow/Red). A pilot evaluation was conducted with 25 student participants across 75 sessions at VVPIET, Solapur. MindScope achieved 84.0% accuracy in risk-level classification and 78.6% sensitivity in detecting emotional masking cases. End-to-end analysis latency averaged 6.6 seconds per session. All data is stored locally with SHA-256 hashed identifiers. MindScope is positioned explicitly as a research-grade wellness monitoring tool, not a clinical diagnostic instrument.

**Решение:** ? T1/T3 MindScope multimodal wellness monitoring (cognitive distortions, risk classification); check human reference

---

### 756 · R4949

**The Digital Native Paradox: A Framework for Critical Appraisal of Generative AI in Paediatric Medical Education**

2026 · Journal of Paediatrics and Child Health · article · en · https://doi.org/10.1111/jpc.70386

The integration of generative artificial intelligence (AI) into healthcare is accelerating, with students and trainees, as digital natives, often becoming its earliest and most enthusiastic adopters [1]. The risk of AI in paediatrics is magnified, where diagnostic and therapeutic decisions carry unique ethical and safety considerations and failure to contextualise a differential diagnosis for a child's specific age and weight can have devastating consequences. Currently, educational efforts continue to focus on how to use AI for example, prompt engineering [2]. However, adoption cannot be decoupled from validation. For the digital native trainee, the primary challenge is integrating the critical appraisal of AI-generated output into their clinical workflow as a core competency. There is a flawed assumption that trainees' digital fluency equates to safe use of AI. Their ability to critically evaluate the quality, veracity and applicability of digital information is not guaranteed. This creates an appraisal paradox: the very individuals most comfortable using AI are often the least equipped to identify its failures. Their nascent clinical experience leaves them uniquely vulnerable to the plausible sounding, confident and sophisticated hallucinations that generative AI produces. This mirrors a form of the Dunning-Kruger effect, where trainees are unconsciously incompetent in complex areas [3]. They lack the deep, tacit knowledge of a senior clinician, who might sense a subtle error. This makes them susceptible to accepting flawed AI guidance for example, when AI provides a differential diagnosis for a neonate with hypoglycaemia, the trainee may be unable to spot the missing, time-critical metabolic disorder or recognise that the suggested drug dose is based on an adult algorithm. This vulnerability aligns with the risks of AI in medical education identified by Abdulnour et al., specifically ‘mis-skilling’, where trainees internalise incorrect AI-generated logic and ‘de-skilling’, where reliance on the tool leads to the atrophy of foundational clinical reasoning [4]. Without intentional scaffolding, there is a risk of being a passive consumer of information rather than an active validator of clinical evidence. Modern medicine is built on evidence-based practice, which explicitly trains clinicians to not take information at face value [5]. Structured tools such as the CASP (Critical Appraisal Skills Programme) checklists, allow us to deconstruct a study's methodology, assess its validity and determine its applicability [6]. AI output is an opaque and therefore problematic form of evidence. We cannot assess its ‘black box’ methodology. Therefore, we must shift our focus to appraising the output itself. To address this critical educational gap, I propose the VALIDATE framework, see Figure 1 and Table 1. This framework provides a practical, cognitive scaffold that builds critical appraisal skills for AI output. It begins by guiding the user to verify the output's factual accuracy and provenance against external, gold-standard sources. It then prompts an assessment of internal consistency, potential bias and relevance to the specific paediatric context. The framework moves beyond simple fact-checking to encourage a deeper critique, requiring the user to analyse gaps (omissions) in the AI's reasoning and test the output's robustness. Finally, it instils a crucial safety net, mandating escalation whenever the AI output suggests a novel course of action or replaces the trainee's foundational knowledge. Although broader frameworks such as DEFT-AI provide a strategy for clinical supervisors to oversee AI use [4], VALIDATE provides the specific cognitive tactic for the learner. It operationalises the ‘Evaluative’ component of supervision, giving the trainee a structured internal checklist to perform before presenting their plan to a senior (Box 1). AI Output: Suggests fluid resuscitation and anti-emetics but misses metabolic differentials. The increasing use of AI in healthcare creates significant governance, patient safety and professionalism issues. The VALIDATE framework can serve as a practical tool for integrating AI use with existing professional standards. VALIDATE is therefore designed as a curricular expectation for paediatric trainees, operationalising the critical appraisal of AI as a core competency akin to evidence-based medicine. Clinical supervisors also have a critical role in modelling safe AI behaviour. In the same way a consultant asks, ‘What does the latest literature say?’, they must now ask, ‘You've used AI to help formulate this plan. Walk me through how you validated its output’. This normalises a culture of sceptical trust and provides supervisors with a tool to assess a trainee's digital professionalism [7]. AI is a tool whose safety is entirely conditional on the judgement of its user. The digital native trainee, while comfortable with the interface, is uniquely vulnerable to the subtle, authoritative sounding failures of these systems. We must urgently train our future doctors to be its critical validators, not its passive consumers. Open access publishing facilitated by The University of Newcastle, as part of the Wiley - The University of Newcastle agreement via the Council of Australasian University Librarians. The author has nothing to report. The author declares no conflicts of interest. Data sharing not applicable to this article as no datasets were generated or analysed during the current study.

**Решение:** -4 paediatric medical education with GenAI

---

### 757 · R0754

**Geometry of Knowledge Allows Extending Diversity Boundaries of Large Language Models**

2026 · Underline Science Inc. · audiovisual/conference talk, preprint/article, other · en · https://doi.org/10.48448/0cvr-z102

Starting from the hypothesis that knowledge in semantic space is organized along structured manifolds, we argue that this geometric structure renders the space explorable. By traversing it and using the resulting continuous representations to condition an LLM’s generation distribution, we can systematically expand the model’s reachable semantic range. We introduce a framework that requires no modification of LLM parameters and operationalizes this idea by constructing a conditioning distribution from a small set of diverse anchor generations. This distribution conditions LLM's generation via an xRAG-style projector. Our experiments demonstrate that this manifold-based conditioning substantially increases generative diversity, with direct benefits for enhancing divergent thinking, a core facet of creativity, in language models.

**Решение:** -6 Geometry of Knowledge, manifold traversal in LLM generation

---

### 758 · R6175

**Generative AI Use and the Student Well-Being Paradox in Higher Education: Efficiency-Gain Retention, Performance Escalation, and Relative Competition**

2026 · Sustainability · journalarticle, review, article · en · https://doi.org/10.3390/su182010402

Generative artificial intelligence (GenAI) can reduce the time and cognitive effort required for university learning, yet technical efficiency does not necessarily translate into improved student well-being. This article develops and tests a conversion account of this paradox by distinguishing efficiency gains that remain available as student-controlled resources from gains that are associated with perceived increases in performance expectations, competitive pressure, verification work, and dependence. A sequential three-study mixed-methods program was conducted with undergraduates in Jiangxi Province. Study 1 used codebook thematic analysis of 42 interviews to identify six mechanisms linking immediate efficiency to resource retention or perceived pressure. Study 2 surveyed 1268 students across eight universities. GenAI use was strongly associated with perceived efficiency gains, but also with perceived performance-standard escalation and verification burden. Positive retention and negative competition pathways were similar in magnitude, yielding a nonsignificant total association with well-being; working-time retention strengthened the efficiency–well-being association. Because Study 2 was cross-sectional, these pathways are interpreted as indirect associations rather than causal mediation. Study 3 used a 2 × 2 experiment (N = 320) and found that AI access improved task quality and reduced completion time under both performance-norm conditions, whereas gains in autonomy, retained time, and state well-being were evident under the stable norm but not statistically distinguishable from zero under the escalated norm. The findings distinguish technical affordance from context-dependent conversion and suggest that responsible AI integration should consider whether efficiency gains remain available for learning, recovery, and student-directed use alongside productivity.

**Решение:** -4 GenAI use and student well-being paradox in higher education

---

### 759 · R3414

**Neural Noise as a Substrate of Cognitive Novelty**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.20445565

This paper is a companion meta-analysis to: lajjadred (2026). Beyond Deductive Machinery: Why LLMs Cannot Generate Truly Novel Conclusions. Zenodo. https://doi.org/10.5281/zenodo.20324204 Background. Large language models (LLMs) are widely described as systems capable of creative output, yet the theoretical basis for this claim has not been rigorously examined against the neuroscientific evidence on what biological creativity actually requires. A companion paper (lajjadred, 2026) argues that LLMs are structurally incapable of generating genuinely novel conclusions because they lack physical stochasticity at the substrate level. The present paper provides the empirical foundation for that argument by systematically reviewing and meta-analyzing the evidence on whether neural stochasticity is a functionally relevant substrate of cognitive novelty in biological systems. Objectives. Four research questions were addressed: (RQ1) Is there a reliable empirical association between neural stochasticity and cognitive novelty? (RQ2) Does evidence support a causal direction from neural noise to creativity? (RQ3) Which types of neural noise matter most, and at which level of the neural hierarchy? (RQ4) Does the relationship conform to an inverted-U function consistent with stochastic resonance? Results. Neural variability reliably predicts creative performance across modalities. The largest study (Chen et al., 2025; N = 2,433 across 10 datasets from 5 countries) found DMN-ECN switching frequency predicted divergent thinking (g = 0.174, p < .001) but not general intelligence (g = 0.023, p = .485). tRNS studies demonstrated that externally induced cortical noise produces large improvements in verbal creativity (pooled d = 1.57). Pharmacological suppression of dopaminergic tone reduced creative output (ρ = −0.47). The noise-creativity relationship conforms to an inverted-U consistent with stochastic resonance. Conclusions. Neural stochasticity is a reliable, specific, and causally relevant substrate of cognitive novelty. LLM temperature sampling is empirically dissociable from biological stochasticity: it is weakly correlated with novelty, convergent toward repetition under sustained generation, and structurally incapable of redirecting computation in flight. The development of AI systems capable of genuine cognitive novelty requires hardware-level physical indeterminacy that no current architecture instantiates. Keywords: neural noise, stochastic resonance, cognitive novelty, creativity, divergent thinking, Default Mode Network, dopamine, transcranial random noise stimulation, large language models, meta-analysis

**Решение:** -1 theoretical paper on neural noise and cognitive novelty in LLMs

---

### 760 · R7504

**Toward Quantitative Modeling of Cybersecurity Risks Due to AI Misuse**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint/preprint · https://doi.org/10.48550/arxiv.2512.08864

Advanced AI systems offer substantial benefits but also introduce risks. In 2025, AI-enabled cyber offense has emerged as a concrete example. This technical report applies a quantitative risk modeling methodology (described in full in a companion paper) to this domain. We develop nine detailed cyber risk models that allow analyzing AI uplift as a function of AI benchmark performance. Each model decomposes attacks into steps using the MITRE ATT&amp;CK framework and estimates how AI affects the number of attackers, attack frequency, probability of success, and resulting harm to determine different types of uplift. To produce these estimates with associated uncertainty, we employ both human experts, via a Delphi study, as well as LLM-based simulated experts, both mapping benchmark scores (from Cybench and BountyBench) to risk model factors. Individual estimates are aggregated through Monte Carlo simulation. The results indicate systematic uplift in attack efficacy, speed, and target reach, with different mechanisms of uplift across risk models. We aim for our quantitative risk modeling to fulfill several aims: to help cybersecurity teams prioritize mitigations, AI evaluators design benchmarks, AI developers make more informed deployment decisions, and policymakers obtain information to set risk thresholds. Similar goals drove the shift from qualitative to quantitative assessment over time in other high-risk industries, such as nuclear power. We propose this methodology and initial application attempt as a step in that direction for AI risk management. While our estimates carry significant uncertainty, publishing detailed quantified results can enable experts to pinpoint exactly where they disagree. This helps to collectively refine estimates, something that cannot be done with qualitative assessments alone.

**Решение:** -4 quantitative modeling of cybersecurity risks due to AI misuse

---

### 761 · R7417

**MIRROR: Multimodal Cognitive Reframing Therapy for Rolling with Resistance**

2025 · Underline Science Inc. · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48448/e9rf-8543

Recent studies have explored the use of large language models (LLMs) in psychotherapy; however, text-based cognitive behavioral therapy (CBT) models often struggle with client resistance, which can weaken therapeutic alliance. To address this, we propose a multimodal approach that incorporates nonverbal cues, which allows the AI therapist to better align its responses with the client's negative emotional state. Specifically, we introduce a new synthetic dataset, Mirror (Multimodal Interactive Rolling with Resistance), which is a novel synthetic dataset that pairs each client's statements with corresponding facial images. Using this dataset, we train baseline vision language models (VLMs) so that they can analyze facial cues, infer emotions, and generate empathetic responses to effectively manage client resistance. These models are then evaluated in terms of both their counseling skills as a therapist, and the strength of therapeutic alliance in the presence of client resistance. Our results demonstrate that Mirror significantly enhances the AI therapist's ability to handle resistance, which outperforms existing text-based CBT approaches. Human expert evaluations further confirm the effectiveness of our approach in managing client resistance and fostering therapeutic alliance. EMNLP 2025 Main

**Решение:** -6 MIRROR: multimodal VLM managing client resistance trained on synthetic dataset

---

### 762 · R1137

**Enhancing Korean adolescent suicide risk prediction with TabR: A generative AI and explainable retrieval-based deep learning approach.**

2026 · Medicine · journal article, journalarticle, review · eng · https://doi.org/10.1097/md.0000000000048172

Adolescent suicide is a growing public health crisis, particularly in South Korea, which has one of the highest youth suicide rates among Organization for Economic and Development countries. Suicide is the leading cause of death among South Koreans aged 10 to 39 years, driven by academic stress, mental health conditions, and social pressures. The early identification of at risk individuals is crucial for timely intervention. This study presents a novel application of TabR, a retrieval-augmented residual neural architecture, for predicting suicide attempts among adolescents, using the Korea Youth Risk Behavior Survey dataset from 2020 to 2022, comprising 1,61,646 participants. To address the extreme class imbalance and limited positive cases, we employed a tabular variational autoencoder for synthetic data augmentation, improving minority class representation while preserving feature distribution fidelity. TabR was compared against 8 baseline machines learning and deep learning models: AdaBoost, CatBoost, LightGBM, XGBoost, Random Forest, SAINT, TabNet, and FT-Transformer. TabR trained on TVAE-augmented data achieved the highest accuracy of 0.9726, AUC of 0.8963, and F1-score of 0.4754. While our findings demonstrate notable improvements in performance, limitations remain, particularly regarding the dataset size, class imbalance, and lack of external validation. Future research should prioritize external validation in independent cohorts, prospective or longitudinal study designs, and explicit evaluation of clinical impact and potential harms (including consequences of false positives and false negatives) before any consideration of deployment.

**Решение:** -4 TabR tabular deep learning predicting adolescent suicide from survey data

---

### 763 · R0630

**Artificial Intelligence for Predicting Patient Reported Outcome Measures (PROMs) Scores from Free Text: A Proof-of-Concept Study with the EuroQol-5D-3L and Transformer Models (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.94142

BACKGROUND Patient-reported outcomes measures (PROMs) have become an important tool in measuring a patient’s health status from their own perspective; however, they are typically measured using standardized questionnaires which do not account for each patient's unique experience of health. Recent improvements in Natural Language Processing (NLP) provide new possibilities to extract PROM scores from unstructured or free-text patient narratives; however, the feasibility and minimal data requirements needed to accomplish this task remain uncertain. OBJECTIVE To assess the practicality of transformer-based models for predicting EuroQol EQ-5D-3L scores from patient narratives and to evaluate minimum data requirements, narrative length and data augmentation effects. METHODS This proof-of-concept study used synthetically generated patient narratives to evaluate methodological feasibility. Three transformer models (BERT, BioBERT, DistilBERT) were fine-tuned for regression from patient narratives representing all 243 EQ-5D-3L health states. The performance of the models in various scenarios including a range of sample sizes (n=100–850), narrative length (100–1000 words), and data augmentation conditions were compared. The performance of the models was assessed through fivefold cross-validation and additional validation on datasets created by ChatGPT and DeepSeek. RESULTS Each model was able to predict EQ-5D-3L scores using each of the different configurations of data (n=100-850 patients; 100-1000-word narratives). However, optimal results were obtained when training the models with 100-word narratives derived from the largest number of people (n=850), where mean squared error=0.03 (95% CI: 0.02-0.04), mean absolute error=0.13 (95% CI: 0.13-0.15), explained variance=0.77 (95% CI: 0.64-0.77), and intraclass correlation coefficient=0.85 (95% CI: 0.81-0.87). Furthermore, it was found that the shorter narratives (100 words) performed better than longer narratives (100-1000 words). Additionally, the use of data augmentation improved the predictive performance. CONCLUSIONS Transformer models show promise in predicting EQ-5D-3L PROM scores from synthetic patient generated narratives, with a minimum of 250 patients providing around 100-word narratives required for reliable performance. The work provides both a methodological basis and empirical standards for AI-based PROM systems. However, clinical implementation will require validation using real patient-authored narratives prior to adoption. If validated, the use of this approach could provide evidence to support the inclusion of a patient's experience as a narrative into standardized outcome measures and support patient-centred healthcare evaluations.

**Решение:** -5 predicting EQ-5D-3L scores from synthetic patient narratives using fine-tuned BERT/DistilBERT

---

### 764 · R8762

**An Large Language Model-Augmented Method to Assist Novice Designers in Divergent Thinking**

2025 · Journal of Computing and Information Science in Engineering · journalarticle, article · en · https://doi.org/10.1115/1.4068664

Abstract Divergent thinking is crucial for novice designers’ creativity and innovative problem-solving skills. Due to their limited knowledge base, novice designers struggle to master divergent thinking methods and connect personal knowledge with design experience. This study introduces a novel method that uses large language models (LLMs) to assist novice designers in expanding their divergent thinking. This method incorporates a two-layer hierarchical structure that links each of the four perspectives—memory, operation, scene, and property—to specific dimensions, facilitating the systematic generation of new divergent ideas. By combining LLMs’ vast knowledge with these divergent thinking frameworks, this method not only provides structured guidance but also fosters the gradual enhancement of divergence through interactive questioning and content generation. A series of tests, including the alternative uses test (AUT) and conceptual design tasks, were conducted to evaluate the impact of this method. Results show that LLMs may significantly improve the fluency, flexibility, and originality of divergent thinking outcomes. This study explores the potential for human–computer collaboration to support divergent thinking, opening avenues for future research and practical applications in design education and practice.

**Решение:** -4 LLM-assisted divergent thinking in industrial design

---

### 765 · R5119

**PatientHub: A Unified Framework for Patient Simulation**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2602.11684

As Large Language Models increasingly power role-playing applications, simulating patients has become a valuable tool for training counselors and scaling therapeutic assessment. However, prior work remains fragmented: existing approaches rely on incompatible, non-standardized profiles, prompts, and evaluation metrics, hindering reproducibility, fair comparison, and reuse. We introduce PatientHub, a unified and modular framework that standardizes the creation, simulation, and evaluation of LLM-based patients. Our framework provides 16 patient simulators, a graph-based orchestrator for multi-turn, multi-session interactions, and a configurable LLM-as-a-judge evaluator that supports multiple rubric types. Via our command-line interface, users can generate patient profiles, run simulations, and apply rubric-driven evaluation at the turn and session level. To demonstrate PatientHub's utility, we compare several supported simulators under a shared interaction protocol and showcase its extensibility by prototyping a new simulator variant with minimal additional code. By consolidating existing work into a single reproducible pipeline, our framework eliminates much of the infrastructure overhead that currently fragments this research and accelerates the development of new methods. Our code and data are publicly available via https://github.com/Sahandfer/PatientHub. EMNLP 2026 Demo Paper

**Решение:** -6 PatientHub: standardized framework for simulating patients with LLMs

---

### 766 · R9498

**Beyond the Surface: Enhancing LLM-as-a-Judge Alignment with Human via Internal Representations**

2025 · Neural Information Processing Systems · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2508.03550

The growing scale of evaluation tasks has led to the widespread adoption of automated evaluation using LLMs, a paradigm known as "LLM-as-a-judge". However, improving its alignment with human preferences without complex prompts or fine-tuning remains challenging. Previous studies mainly optimize based on shallow outputs, overlooking rich cross-layer representations. In this work, motivated by preliminary findings that middle-to-upper layers encode semantically and task-relevant representations that are often more aligned with human judgments than the final layer, we propose LAGER, a post-hoc, plug-and-play framework for improving the alignment of LLM-as-a-Judge point-wise evaluations with human scores by leveraging internal representations. LAGER produces fine-grained judgment scores by aggregating cross-layer score-token logits and computing the expected score from a softmax-based distribution, while keeping the LLM backbone frozen and ensuring no impact on the inference process. LAGER fully leverages the complementary information across different layers, overcoming the limitations of relying solely on the final layer. We evaluate our method on the standard alignment benchmarks Flask, HelpSteer, and BIGGen using Spearman correlation, and find that LAGER achieves improvements of up to 7.5% over the best baseline across these benchmarks. Without reasoning steps, LAGER matches or outperforms reasoning-based methods. Experiments on downstream applications, such as data selection and emotional understanding, further show the generalization of LAGER. Accepted to NeurIPS 2025

**Решение:** -6 LAGER: improving LLM-as-a-judge alignment with human preferences on Flask/HelpSteer

---

### 767 · R12638

**Selective Propositional Reasoning: A Cognitive Load-Aware Strategy for Enhanced Reasoning**

2023 · International Conference on Cloud Computing, Big Data Application and Software Engineering (CBASE) · conference, conference-paper · en · https://doi.org/10.1109/cbase60015.2023.10439142

Large Language Models (LLMs) have made significant strides across a myriad of domains. While techniques like Chain of Thought have enhanced LLM’s reasoning abilities to some extent, they still fall short in complex reasoning tasks. Drawing parallels with human cognition, there exists a concept of "cognitive load" that impacts our efficiency in processing information. Based on this, we hypothesize that LLMs, much like humans, may also be affected by cognitive load during their reasoning processes. Building on this assumption, we postulate that by alleviating the cognitive load LLMs encounter during reasoning, we can augment their overall performance. To this end, we introduce the Selective Propositional Reasoning (SPR) methodology, which is specifically designed to mitigate this cognitive burden. Our experimental results underscore the effectiveness of SPR, evidencing a 6% improvement in overall accuracy. Additionally, the Proposition Pair Enumeration (PPE) strategy further substantiates our cognitive load hypothesis, showcasing a 1.5% overall performance enhancement. Collectively, our findings not only emphasize the potential benefits of addressing cognitive load in LLMs but also bridge the gap between psychological constructs and computational modeling.

**Решение:** -6 selective propositional reasoning for cognitive load in LLMs

---

### 768 · R6210

**Agri-R1: Agricultural Reasoning for Disease Diagnosis via Automated-Synthesis and Reinforcement Learning**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.04672

Agricultural disease diagnosis challenges VLMs, as conventional fine-tuning requires extensive labels, lacks interpretability, and generalizes poorly. While reasoning improves model robustness, existing methods rely on costly expert annotations and rarely address the open-ended, diverse nature of agricultural queries. To address these limitations, we propose \textbf{Agri-R1}, a reasoning-enhanced large model for agriculture. Our framework automates high-quality reasoning data generation via vision-language synthesis and LLM-based filtering, using only 19\% of available samples. Training employs Group Relative Policy Optimization (GRPO) with a novel reward function that integrates domain-specific lexicons and fuzzy matching to assess both correctness and linguistic flexibility in open-ended responses. Evaluated on CDDMBench, our resulting 3B-parameter model achieves performance competitive with 7B- to 13B-parameter baselines, showing a +27.9\% relative gain in disease recognition accuracy, +33.3\% in agricultural knowledge QA, and a +26.10-point improvement in cross-domain generalization over standard fine-tuning. These results suggest that automated reasoning synthesis paired with domain-aware reward design may provide a broadly applicable paradigm for RL-based VLM adaptation in data-scarce specialized domains. Our code and data are publicly available at: https://github.com/CPJ-Agricultural/Agri-R1. This paper is submitted for review to the 2026 ACM MM Conference. The corresponding authors are Tao Fang and Lina Lu, where Tao Fang is the senior Corresponding Author (Last Author) and the principal supervisor of this work, having led the research design, guided the methodology, and overseen the entire project

**Решение:** -4 Agri-R1: agricultural reasoning for plant disease diagnosis

---

### 769 · R4164

**EpidemIQs: Prompt-to-Paper LLM Agents for Epidemic Modeling and Analysis**

2026 · IEEE Transactions on Artificial Intelligence · journalarticle, review, article · en · https://doi.org/10.1109/tai.2026.3666830

Large Language Models (LLMs) offer new opportunities to accelerate complex interdisciplinary research domains through AI assistant tools. Epidemic modeling, characterized by its complexity and reliance on network science, dynamical systems, epidemiology, and stochastic simulations, represents a prime candidate for leveraging LLM-driven automation. We introduce EpidemIQs, a novel multi-agent LLM framework that integrates user inputs and autonomously conducts literature review, analytical derivation, network modeling, mechanistic modeling, stochastic simulations, data visualization and analysis, and finally documentation of findings in a structured manuscript, through five predefined research phases. We introduce two types of agents: a scientist agent for planning, coordination, reflection, and generation of final results, and a task-expert agent to focus exclusively on one specific duty serving as a tool to the scientist agent. The framework consistently generated complete reports in scientific article format. Specifically, using GPT 4.1 and GPT 4.1 Mini as backbone LLMs for scientist and task-expert agents, respectively, the autonomous process completes with average total token usage 870K at a cost of about $1.57 per study, successfully executing all phases and final report. We evaluate EpidemIQs across several different epidemic scenarios, measuring computational cost, workflow reliability, task success rate, and LLM-as-Judge and human expert reviews to estimate the overall quality and technical correctness of the generated results. Through our experiments, the framework consistently addresses evaluation scenarios with an average task success rate of 79%. We compare EpidemIQs to an iterative single-agent LLM, benefiting from the same system prompts and tools, iteratively planning, invoking tools, and revising outputs until task completion. The qualitative and quantitative comparisons suggest a consistently higher performance of the proposed framework across the tested scenarios. We discuss the benefits that EpidemIQs can offer, its limitations, and ethical concerns of such AI research assistant tools.

**Решение:** -4 EpidemIQs: LLM agents for epidemic modeling

---

### 770 · R6902

**From Examples to Rules? Exploring Inductive Reverse Engineering and Deductive Few-Shot Coding via LLMs for Qualitative Data Analysis**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-29760-0_61

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T1 inductive and deductive qualitative coding via LLMs; no abstract, eligible on full text

---

### 771 · R5549

**Lessons Without Borders? Evaluating Cultural Alignment of LLMs Using Multilingual Story Moral Generation**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2604.08797

Stories are key to transmitting values across cultures, but their interpretation varies across linguistic and cultural contexts. Thus, we introduce multilingual story moral generation as a novel culturally grounded evaluation task. Using a new dataset of human-written story morals collected across 14 language-culture pairs, we compare model outputs with human interpretations via semantic similarity, a human preference survey, and value categorization. We show that frontier models such as GPT-4o and Gemini generate story morals that are semantically similar to human responses and preferred by human evaluators. However, their outputs exhibit markedly less cross-linguistic variation and concentrate on a narrower set of widely shared values. These findings suggest that while contemporary models can approximate central tendencies of human moral interpretation, they struggle to reproduce the diversity that characterizes human narrative understanding. By framing narrative interpretation as an evaluative task, this work introduces a new approach to studying cultural alignment in language models beyond static benchmarks or knowledge-based tests.

**Решение:** -4 cultural alignment of LLMs using multilingual story moral generation

---

### 772 · R1255

**Modeling of Therapist-Client Dynamics in Psychotherapy Using LLM-Based Assessments: An Empirical Study.**

2026 · JMIR mental health · journal article, med, journalarticle · eng · https://doi.org/10.2196/95389

BACKGROUND Psychotherapy is a primary treatment for many mental health conditions, yet the dynamic interplay among therapist behaviors, client responses, and the therapeutic relationship remains difficult to disentangle at scale. Traditional process research relies on labor-intensive human coding, limiting the ability to model moment-to-moment therapeutic dynamics across large datasets. OBJECTIVE This study aimed to develop and validate a computational framework for modeling therapist-client interaction processes and to examine how therapist behaviors and relational qualities relate to client self-disclosure and emotional expression in psychotherapy sessions. METHODS We developed automated assessment pipelines using large language models (LLMs) to measure therapist behaviors (empathy, exploration), relational quality (rapport), and client outcomes (self-disclosure, self-directed negative emotion, outward-directed negative emotion). Model-generated scores were validated against human annotations. We then applied these measures to approximately 2,000 hours of psychotherapy transcripts from the Alexander Street corpus. This yielded an estimation sample of 119,233 client utterances from 1,573 sessions and 37 clients. Because utterances are nested within sessions and sessions within clients, we estimated a saturated multivariate structural equation model (SEM) with standard errors clustered at the session level. Results were confirmed in a multilevel regression model with random intercepts for session and client. RESULTS Following comparative validation of six candidate language models, automated measures showed good to excellent agreement with human annotations (ICC = 0.60-0.81), with rapport (ICC = 0.81), self-disclosure (ICC = 0.78), empathy components (ICC = 0.60-0.75), and emotion measurements (ICC = 0.66-0.80). SEM analyses revealed that therapist empathy and exploration were each associated with increased client disclosure (empathy β=0.086, 95% CI 0.078 to 0.095; exploration β=0.086, 95% CI 0.078 to 0.094; both P<.001) and increased expression of self-directed negative emotions, comprising sadness, anxiety, fear, and depression (empathy β=0.118, 95% CI 0.110 to 0.127; exploration β=0.078, 95% CI 0.070 to 0.087; both P<.001). Both behaviors were also associated with reduced expressions of enjoyment (empathy β=-0.037; exploration β=-0.041; both P<.001). Surprisingly, rapport in the prior session showed no association with client self-disclosure or negative emotion expression. CONCLUSIONS This study demonstrates that LLM-based measurement combined with structural modeling can capture core therapeutic processes at scale. Empathy and exploration showed small but consistent turn-level associations with client disclosure and emotional expression, whereas prior-session rapport did not show a robust association. These findings provide a computational foundation for precision modeling of psychotherapy processes and may offer actionable insights for scalable therapist training and AI-supported clinical education systems. CLINICALTRIAL

**Решение:** + T4/T1 LLM measurement of therapist empathy, rapport, and client disclosure validated against human annotations (ICC 0.60-0.81) across 2,000h therapy transcripts (JMIR Mental Health 2026)

---

### 773 · R9610

**Real-Time Emotion Recognition and Response Generation via LLM-Embedded Multimodal Interfaces**

2025 · IEEE International Conference on Computing, Communication and Automation (ICCCA) · conference, conference-paper · https://doi.org/10.1109/iccca66364.2025.11325440

Integration of large language models (LLMs) and multimodal interfaces is transforming the way machines interpret and react to the emotions of humans. This article describes a real-time application that determines the affective state of users by integrating their facial expressions, the vocal prosody, and the low-fidelity physiological data and creates contextually aware, sympathetic responses with the help of a built-in LLM. With cues combined between modalities rather than relying on one source, we will reduce the misclassification of the cues and gain a greater situational depth. We use small neural encoders to generate modality-specific feature and attention-based fusion layer to weighs the best trusted signals at any given moment. The simplified classifier is used to map fused representations with emotion labels, which guide the response planner of the LLM; the LLM will generate according to a given emotion and recent conversation history to generate a coherent and appropriate response. We use human-in-the-loop feedback based on reinforcement learning to optimize the phrasing and timing of responses to achieve improved naturalness. Controlled simulations and user studies were done to evaluate the system with the accuracy of recognition, relevance of response, perceived empathy and latency of interaction. Our multimodal pipeline was more accurate at detection than unimodal baselines, and generated more interesting and comprehensible responses to participants. Notably, the architecture is also efficient and allows to be deployed on edge devices and live applications. The piece shows that integrating LLMs into multimodal, emotion-responsive interfaces can generate more human-friendly interactions- helpful in tutoring systems, mental health support, and customer service- and points to trade-offs related to design responses between responsiveness, privacy, and interpretability. The future applications will be focused on personalization, strong privacy protection, and emotion modeling cross-culturally. Thus, the extraction of features in real-time may be achieved for segmented speech. In experimental settings, we find that emotional understanding accuracy increases by 12.1% over the baseline, and hybrid prompts that admit explicit keywords but also other implicit embeddings. Appropriate applications for this system are adaptive dialogue systems, social robotics akin to GPT-3. 5 language-to-language and trusted educational interfaces, where data is organised. Results of the newly developed EGS score are correlated to human expert ratings on 89% of the test cases.

**Решение:** -4 real-time multimodal emotion recognition interface (facial expressions, vocal prosody)

---

### 774 · R8020

**Integrating Large Language Models Into Creative Project-Based Learning for Enhanced Innovation**

2025 · Advances in computational intelligence and robotics book series · book-chapter · https://doi.org/10.4018/979-8-3373-5117-9.ch010

The integration of Large Language Models (LLMs) into Creative Project-Based Learning (CPBL) enhances student engagement and creativity. This chapter proposes a framework embedding LLMs within CPBL using the Double Diamond model, guiding students through Discover, Define, Develop, and Deliver. LLMs serve as cognitive tools for idea generation, refining problem statements, and articulating outputs. The framework highlights prompt engineering, ethical considerations, and educator guidance to maintain student agency and ensure responsible AI use. The integration is evaluated using quantitative methods (Ennis' taxonomy, modified Torrance Test of Creative Thinking) and qualitative methods (interviews, prompt analysis). Findings suggest LLMs improve student autonomy, divergent thinking, and collaboration, offering valuable insights for educators and instructional designers. The chapter also explores future research into AI's pedagogical and ethical impacts in education.

**Решение:** -4 integrating LLMs into creative project-based learning

---

### 775 · R7566

**High-Accuracy Prediction of Mental Health Scores Using Bert Embeddings Trained Solely on Llm-Generated Synthetic Clinical Descriptions**

2025 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5226763

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T3 mental health scores prediction using BERT embeddings trained on synthetic clinical descriptions; no abstract

---

### 776 · R9658

**A Vector-Quantized Foundation Model for Patient Behavior Monitoring**

2025 · arXiv (Cornell University) · preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2503.15221

Foundation models have achieved remarkable success across various domains, yet their adoption in healthcare remains limited. While significant advances have been made in medical imaging, genetic biomarkers, and time series from electronic health records, the potential of foundation models for patient behavior monitoring through personal digital devices remains underexplored. The data generated by these devices are inherently heterogeneous, multisource, and often exhibit high rates of missing data, posing unique challenges. This paper introduces a novel foundation model based on a modified vector quantized variational autoencoder, specifically designed to process real-world data from smartphones and wearable devices. We leveraged the discrete latent representation of this model to effectively perform two downstream tasks, suicide risk assessment and emotional state prediction, on different held-out clinical cohorts without the need of fine-tuning. We also highlight the existence of a trade-off between discrete and continuous latent structures, suggesting that hybrid models may be optimal for balancing accuracy across various supervised and unsupervised tasks. 10 pages (32 with references and supplementary material). Submitted to Elsevier's journal on Artificial Intelligence in Medicine

**Решение:** -4 vector-quantized foundation model for patient behavior monitoring

---

### 777 · R0323

**Large language models can supplement the assessment of clinical high risk for psychosis.**

2026 · Journal of psychopathology and clinical science · journal article, journalarticle, research-article · eng · https://doi.org/10.1037/abn0001160

Capturing psychosis risk before illness onset is an ongoing challenge for psychosis-spectrum studies. Natural language processing (NLP) tools can harness information embedded in the notes generated during clinical interviews to obtain more objective markers of psychosis risk; for this project, we used readily available assessor notes. The following project acts as proof of concept on the usefulness of AI-based tools to capture latent psychosis risk information. We used assessor notes for 2,077 Structured Interview for Psychosis-risk Syndromes interviews as input for different AI-based NLP models to produce metrics for psychosis risk, namely, a trained encoder-only model (ModernBERT), and zero-shot and few-shot instantiation of two decoder-only models (Large Language Model Meta AI Version 4 [LLaMA-4] and GPT-4.1 mini). AI-based risk metrics were compared with gold-standard ratings of clinical high risk for psychosis (CHR). The AI-based risk metrics' relationship to traditional psychosis risk scores (Shanghai-At-Risk-for-Psychosis [SHARP] and North American Prodrome Longitudinal Study [NAPLS]) was also assessed. Finally, we explored the added benefit of adding AI-based risk metrics to models predicting future participant conversion. All models performed above chance in classifying interview notes for the presence or absence of CHR syndromes. The trained encoder model performed the best out of all models determining the presence of CHR syndromes (accuracy = 82.67%, κ = .63). Positive CHR classification by the encoder model resulted in a 0.69 and 0.85 standard deviation increase in SHARP and NAPLS risk scores (p < .001). A 1 standard deviation increase in decoder-generated risk scores increased traditional risk scores between 0.24 and 0.47 standard deviations (all ps < .001). In exploratory analyses, decoder-generated risk scores incrementally improved models predicting conversion including SHARP but not NAPLS risk scores. Although our results need to be considered in the context of one consortium, AI-based NLPs show potential as an aid for the diagnosis of CHR syndromes, evaluating psychosis risk, and even predicting future conversion, even with suboptimal but readily available inputs (i.e., assessor notes). Future projects could use AI-based tools' potential in augmenting psychosis risk screenings and risk predictors. (PsycInfo Database Record (c) 2026 APA, all rights reserved).

**Решение:** + T3 assessment of clinical high risk for psychosis from SIPS clinical notes: LLaMA-4 and GPT-4.1 mini vs clinician gold standard (N=2,077, APA JPCS 2026)

---

### 778 · R9183

**Refining Input Guardrails: Enhancing LLM-as-a-Judge Efficiency Through Chain-of-Thought Fine-Tuning and Alignment**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2501.13080

Large Language Models (LLMs) have demonstrated powerful capabilities that render them valuable in different applications, including conversational AI products. It is paramount to ensure the security and reliability of these products by mitigating their vulnerabilities towards malicious user interactions, which can lead to the exposure of great risks and reputational repercussions. In this work, we present a comprehensive study on the efficacy of fine-tuning and aligning Chain-of-Thought (CoT) responses of different LLMs that serve as input moderation guardrails. We systematically explore various tuning methods by leveraging a small set of training data to adapt these models as proxy defense mechanisms to detect malicious inputs and provide a reasoning for their verdicts, thereby preventing the exploitation of conversational agents. We rigorously evaluate the efficacy and robustness of different tuning strategies to generalize across diverse adversarial and malicious query types. Our experimental results outline the potential of alignment processes tailored to a varied range of harmful input queries, even with constrained data resources. These techniques significantly enhance the safety of conversational AI systems and provide a feasible framework for deploying more secure and trustworthy AI-driven interactions. 16 pages, 9 figures

**Решение:** -4 refining input guardrails for LLM security

---

### 779 · R9930

**From Visual Perception to Deep Empathy: An Automated Assessment Framework for House-Tree-Person Drawings Using Multimodal LLMs and Multi-Agent Collaboration**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2512.21360

Background: The House-Tree-Person (HTP) drawing test, introduced by John Buck in 1948, remains a widely used projective technique in clinical psychology. However, it has long faced challenges such as heterogeneous scoring standards, reliance on examiners subjective experience, and a lack of a unified quantitative coding system. Results: Quantitative experiments showed that the mean semantic similarity between Multimodal Large Language Model (MLLM) interpretations and human expert interpretations was approximately 0.75 (standard deviation about 0.05). In structurally oriented expert data sets, this similarity rose to 0.85, indicating expert-level baseline comprehension. Qualitative analyses demonstrated that the multi-agent system, by integrating social-psychological perspectives and destigmatizing narratives, effectively corrected visual hallucinations and produced psychological reports with high ecological validity and internal coherence. Conclusions: The findings confirm the potential of multimodal large models as standardized tools for projective assessment. The proposed multi-agent framework, by dividing roles, decouples feature recognition from psychological inference and offers a new paradigm for digital mental-health services. Keywords: House-Tree-Person test; multimodal large language model; multi-agent collaboration; cosine similarity; computational psychology; artificial intelligence 16 pages, 8 figures

**Решение:** + T2 automated assessment and interpretation of House-Tree-Person projective drawing test using MLLMs vs human expert interpretations (similarity 0.75-0.85)

---

### 780 · R5006

**How Undergraduates Interact with a Generative AI Peer: Eight Participation Roles and the Conditions for Effective Collaboration in University Mathematics**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-9851111/v1

Abstract Generative AI is rapidly entering higher-education classrooms, yet remarkably little is known about how individual students actually interact with an AI peer during open-ended collaborative problem solving. This study examines the full range of human–GenAI interaction patterns that emerge when undergraduates collaborate with a large language model (LLM)-based peer to solve calculus optimization problems, and identifies the interaction conditions under which that collaboration is educationally productive. Thirty students used a web-based platform that pairs each participant with an LLM peer through an information-splitting (jigsaw) task structure, making collaboration structurally necessary rather than optional. Full conversation and interaction logs were captured and coded using a multi-agent automated scoring pipeline grounded in the PISA 2015 Collaborative Problem Solving (CPS) matrix. A qualitative case analysis of eight purposively selected conversations then identified eight distinct participation roles: the Co-Regulator, the Recalibrating Collaborator, the Low-Effort Guesser, the Delegating Director, the Misaligned Follower, the Low-Engagement Answer-Seeker, the Efficient Knowledge Seeker, and the Early Disengager. These roles reveal that human–GenAI collaboration is far from monolithic: students who sustain a shared cognitive state with the AI peer, externalize their reasoning, and negotiate intermediate steps achieve substantially better outcomes (OR ≈ 10.83) than those who delegate, disengage, or interact at a transactional level. Quantitative trace-based clustering confirmed two interaction profiles: a higherinteraction cluster where 71% of students solved both tasks, and a lower-interaction cluster where only 19% did. The automated scorer showed promising validity evidence at broad process and competence levels (human–LLM κ = .60; human– human κ = .80). Students perceived the AI feedback as useful (86.7%) and the peer as easy to use (80.0%). These findings provide a theoretically grounded typology of student–GenAI interaction in higher education and show that effective AI-peer collaboration requires deliberate design of both the task structure and the feedback loop. Implications for profile-sensitive AI-peer design and formative feedback are discussed.

**Решение:** -4 undergraduates interacting with GenAI peer in university math

---

### 781 · R11255

**Invisible Textual Backdoor Attacks based on Dual-Trigger**

2024 · arXiv (Cornell University) · preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2412.17531

Backdoor attacks pose an important security threat to textual large language models. Exploring textual backdoor attacks not only helps reveal the potential security risks of models, but also promotes innovation and development of defense mechanisms. Currently, most textual backdoor attack methods are based on a single trigger. For example, inserting specific content into text as a trigger or changing the abstract text features to be a trigger. However, the adoption of this single-trigger mode makes the existing backdoor attacks subject to certain limitations: either they are easily identified by the existing defense strategies, or they have certain shortcomings in attack performance and in the construction of poisoned datasets. In order to solve these issues, a dual-trigger backdoor attack method is proposed in this paper. Specifically, we use two different attributes, syntax and mood (we use subjunctive mood as an example in this article), as two different triggers. It makes our backdoor attack method similar to a double landmine which can have completely different trigger conditions simultaneously. Therefore, this method not only improves the flexibility of trigger mode, but also enhances the robustness against defense detection. A large number of experimental results show that this method significantly outperforms the previous methods based on abstract features in attack performance, and achieves comparable attack performance (almost 100\% attack success rate) with the insertion-based method. In addition, in order to further improve the attack performance, we also give the construction method of the poisoned dataset.The code and data of this paper can be obtained at https://github.com/HoyaAm/Double-Landmines.

**Решение:** -4 dual-trigger invisible textual backdoor attacks

---

### 782 · R5194

**AeroAssist: A Prompt-Driven Multimodal AI Framework for Aircraft Maintenance**

2026 · Proceedings - IEEE Aerospace Conference · conference, conference-paper · https://doi.org/10.1109/aero66936.2026.11519861

Unscheduled aircraft maintenance poses significant challenges, including operational disruptions, increased safety risks, and substantial financial costs. Existing diagnostic methods are limited by their reliance on unimodal data streams-visual, audio, or sensor-based-preventing early fault detection and comprehensive component-level diagnostics. These siloed approaches lack the integrative reasoning capabilities of human experts, highlighting the need for a unified, intelligent framework. In response, we propose AeroAssist, a prompt-driven, multimodal diagnostic framework built on Google's Gemini 2.5 Pro/Flash, a large-scale, pre-trained foundation model used directly at inference time, without any taskspecific fine-tuning. Our primary contribution is Guided Reflective Diagnostic Reasoning (RDR), a structured prompting methodology that instantiates expert-like reasoning behaviors such as independent analysis, cross-modal synthesis, and iterative self-critique. This approach leverages the generalization capabilities of large multimodal models while avoiding the limitations of data scarcity and the computational overhead of model retraining. We evaluate our framework on a semi-synthetic aerospace dataset under zero-shot and few-shot conditions, achieving 90 % classification accuracy in the few-shot setting. Beyond quantitative results, qualitative analysis reveals the model's ability to handle complex reasoning scenarios, such as resolving contradictory multimodal evidence, while also identifying critical failure modes, including overlooking subtle visual defects relevant to safety. Our findings demonstrate that the framework's ability to holistically synthesize video, audio, and sensor inputs significantly enhances diagnostic reliability. This work represents a practical and technically grounded step toward developing multimodal, foundation model-based diagnostic copilots for real-world aerospace maintenance applications.

**Решение:** -4 AeroAssist aircraft maintenance multimodal AI framework

---

### 783 · R7037

**Comparing Chatgpt and Physicians' Answers to Endometriosis Questions on Reddit: A Blind Expert Evaluation**

2025 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5272954

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 ChatGPT vs physicians answering Reddit questions on endometriosis (somatic gynecology)

---

### 784 · R1812

**Like a Therapist, But Not: Reddit Narratives of AI in Mental Health Contexts**

2026 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.18653/v1/2026.findings-acl.569

Large language models (LLMs) are increasingly used for emotional support and mental health-related interactions outside clinical settings, yet little is known about how people evaluate and relate to these systems in everyday use. We analyze 5,126 Reddit posts from 47 mental health communities describing experiential or exploratory use of AI for emotional support or therapy. Grounded in the Technology Acceptance Model and therapeutic alliance theory, we develop a theory-informed annotation framework and apply a hybrid LLM-human pipeline to analyze evaluative language, adoption-related attitudes, and relational alignment at scale. Our results show that engagement is shaped primarily by narrated outcomes, trust, and response quality, rather than emotional bond alone. Positive sentiment is most strongly associated with task and goal alignment, while companionship-oriented use more often involves misaligned alliances and reported risks such as dependence and symptom escalation. Overall, this work demonstrates how theory-grounded constructs can be operationalized in large-scale discourse analysis and highlights the importance of studying how users interpret language technologies in sensitive, real-world contexts.

**Решение:** ? T1 hybrid LLM-human pipeline analyzing therapeutic alliance and attitudes in mental health Reddit posts; check agreement metrics

---

### 785 · R7705

**Research on dual evaluation of low-barrier generation AI assisted with cross-professional art practice: focusing on the quality of works and self-cognition differences between art students and non-art students**

2025 · Proceedings of the 2025 International Conference on Generative AI and Digital Media Arts · book, conference, conference-paper · https://doi.org/10.1145/3770445.3770461

To address the learning gap in visual expression and creative execution between art and non-art students stemming from disparities in foundational skills within interdisciplinary art courses, this study investigates the supportive value of low-barrier generative AI tools. Eighty undergraduate students (46 art majors, 34 non-art majors) from a Chinese university were recruited. Each participant produced two illustration works on the theme "Cultural Symbols in Daily Life," one using traditional methods and another with AI assistance. A dual-evaluation approach was employed: students self-assessed their learning confidence and task satisfaction using a 5-point Likert scale, while open-ended feedback was quantified into sentiment scores via sentiment analysis; five experts conducted blind evaluations on "Creative Transformation of Cultural Symbols" and "Technical Proficiency of Illustration," achieving a high inter-rater reliability (ICC = 0.85). Results indicate that low-barrier AI significantly narrowed the learning gap: expert scores for non-art students' AI-assisted works increased by 27% compared to their traditional works (t = 2.07, p = 0.042), primarily in technical aspects such as compositional balance and detail rendering—consistent with findings in higher education art research that AI can compensate for technical deficiencies among non-art students. The effect size (Cohen's d) for self-reported learning confidence improvement was 1.02 for non-art students, substantially higher than the 0.35 observed for art students, aligning with findings that AI provides greater psychological empowerment for non-traditional learners. In contrast, art students showed only a 9% improvement in expert scores for AI-assisted works (t = 1.32, p = 0.191) and minimal gains in self-efficacy. This study confirms that low-barrier generative AI offers an easily implementable, cost-effective solution for interdisciplinary art courses, effectively promoting educational equity by bridging the capability gap between art and non-art students.

**Решение:** -4 low-barrier GenAI in cross-professional art practice

---

### 786 · R7232

**ADVERSARIAL MACHINE LEARNING SECURITY: PROTECTING AI SYSTEMS FROM COMPROMISE AND MANIPULATION**

2025 · Archives The Journal of the British Records Association · article · en · https://archives.publishing.org.in/index.php/archives/article/view/2632

As machine learning (ML) systems become increasingly integrated into critical applications—ranging from autonomous vehicles to healthcare diagnostics—their vulnerability to adversarial attacks has emerged as a major security concern. Adversarial Machine Learning (AML) explores techniques to deceive, manipulate, or compromise AI models through carefully crafted inputs, model poisoning, or extraction attacks. This paper provides a comprehensive survey of AML threats, attack methodologies, and defense mechanisms. We categorize attacks based on their objectives (e.g., evasion, poisoning, model stealing) and threat models (white-box, black-box, gray-box). We then analyze state-of-the-art defense strategies, including adversarial training, certified robustness, and detection-based approaches. Additionally, we discuss emerging challenges such as adversarial attacks on large language models (LLMs) and federated learning systems. Finally, we outline future research directions to enhance the robustness and security of AI systems in adversarial environments.

**Решение:** -4 adversarial machine learning security in critical applications

---

### 787 · R1333

**Conjunto de Datos y Código: Análisis Multivariante y Meta-Analítico de los Efectos del Capitalismo (1990–2025)**

2026 · Figshare · dissertation/thesis, dissertation · https://doi.org/10.6084/m9.figshare.33225015

Este repositorio contiene el conjunto de datos empíricos y los scripts de código fuente utilizados para la investigación de la tesis de maestría titulada: "ANÁLISIS MULTIVARIANTE Y META-ANALÍTICO DE LA EVOLUCIÓN DE LOS ENFOQUES Y EFECTOS ATRIBUIDOS AL CAPITALISMO DESDE LA LITERATURA CIENTÍFICA GLOBAL (1990–2025)" (Universidad de Guayaquil, Ecuador). El archivo comprimido (.rar) incluye: Data: Los corpus de metadatos extraídos de las bases científicas (Web of Science y Scopus), incluyendo las matrices de codificación de variables categóricas (Nivel de análisis, Ámbitos, Tipos de crisis, Dirección de efecto). Code/Scripts: Los algoritmos y rutinas de modelado estadístico para la ejecución de:Modelos Meta-analíticos y cálculo de heterogeneidad (I²).Agrupamiento Jerárquico utilizando Distancia de Gower (K=3).Análisis de Correspondencias Múltiples (MCA).Análisis de Clases Latentes (LCA, K=4).Evaluación de concordancia inter-jueces (LLM vs. Humano) mediante el estadístico Kappa de Cohen.Estos materiales se publican bajo acceso abierto para garantizar la total reproducibilidad de los modelos multivariantes, la transparencia metodológica y fomentar futuras investigaciones en el cruce entre la Ciencia de Datos y el análisis bibliométrico sociológico.

**Решение:** -4 meta-analysis of effects of capitalism (macroeconomics)

---

### 788 · R7686

**Inside AI**

2025 · eYLS (Yale Law School) · article

It is beautiful, the Mandelbrot set. In full, it resembles a horseshoe crab or a sideways Rorschach test, flecked with patterns of spikes and lobes. Zooming in at any point near its edge reveals infinite depths of swirls, reminiscent of Van Gogh’s Starry Night or an intricate paisley textile. The shape could easily hang on a wall, an example of fine abstract art. Yet the entirety of that shape can be computed by repeated application of a simple mathematical function:2 f(x) = x2 + c. Is all the beauty and complexity of the Mandelbrot set “inside” the symbols of that mathematical function? And what does it mean for something to be “inside” a mathematical function in the first place? These seemingly abstract, philosophical questions are at the heart of heated and difficult debates of law and policy today. The recent explosion of generative artificial intelligence has prompted questions of how AI technology interacts with copyright laws, privacy rules, and other regulatory policies. These legal regimes often have predefined notions of when information is “inside” something. Yet these notions appear puzzling, contradictory, or plainly wrong when applied to AI, and that risk burdening the new technology with nonsensical and outdated doctrines. Copyright law, among others, depends on what is “inside” an AI model, the enormous and seemingly incomprehensible set of numeric parameters that make AI systems tick. This Article takes aim at that question. Its central argument is that, because modern AI models are just exceptionally large mathematical functions, intuitions about simpler mathematical functions will sharpen an understanding of what is inside AI. This Article will take a tour of those intuitions—fully accessible to anyone, no special math skills required—and use them to identify new approaches to evaluating AI under copyright. A brief summary is as follows. Conventional accounts of AI and copyright law make two separate assumptions about what is “inside” a model. First, models are trained on copyright-protected information—images, texts, sounds, and so forth. Many commentators believe that the training data is “ingested” into, and is consequently inside, the model. Second, AI models have been observed to produce, upon carefully crafted prompting, outputs highly similar to copyrighted works. The apparent implication of this behavior is that the model must have “memorized” the copyrighted material during training, again an assertion that the material is inside the model. These allegations have serious consequences, suggesting that AI models may be infringing on contraband, subject to the severe penalties of copyright law. To gain a sharper sense of what is inside the model, this Article presents two basis premises that are well-known among the AI research community but rarely explored in the legal literature. • First, a model is simply a mathematical function, a series of basic operations like multiplication and addition that convert one list of numbers into another. Even the most remarkable of generated AI outputs—art, music, and literature—are just the consequence of simple mathematical operations, different only in scale from the mathematical formulas that anyone is familiar with. • Second, the AI model is not an arbitrary or incomprehensible black box. Rather, it corresponds to an approximation of a mathematical object called a manifold, a geometric representation of a collection of useful real-world information, like grammatical sentences or comprehensible sounds. These two concepts upend the implicit assumptions that laws make about what is inside AI models. First, they show a distinction between the numerical parameters of a model and the manifold that a model represents. Information can be inside one without being inside the other, and laws frequently conflate these two meanings of “inside.” Second, the nature of the AI model as an approximation suggests that, at least in an ideal case, the model should discern larger patterns about data rather than merely incorporate that data. Applied to copyright law, the implication is that the broad, simplistic definition of “inside” that the statutory text adopts—a work is “inside” a thing if the work can be “perceived . . . with the aid of a machine”3—is logically questionable. Courts and lawmakers will need to revisit seemingly basic questions of copyright law anew in view of the unique nature of AI technology.

**Решение:** -1 Yale Law School article on copyright law and Mandelbrot set

---

### 789 · R6917

**HEEL: A State-Centric Autobiographical Memory Architecture for Persistent Agents — Beyond the Session-Centric Ontology**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.19851563

Title HEEL: A State-Centric Autobiographical Memory Architecture for Persistent Agents — Beyond the Session-Centric Ontology Description This document proposes the HEEL (History, Experience, External, Logic) architecture, introducing a hierarchical virtual memory management system for LLM-driven autonomous agents. This is the first strategic dimensional ascension operation within the Agent OS theoretical framework, designed to address the first-principles constraint of finite context windows in LLMs. Core Contributions "Injectability" replaces semantics as the sole criterion for memory stratification. Data is classified into four layers—History (raw material, ℐ=0), Experience (ready-to-use finished products, ℐ=1), External (external raw material, ℐ=0), and Logic (pure strategy management layer)—based on processing state rather than semantic content. This criterion is orthogonal to data semantics, fundamentally avoiding the ambiguity and maintenance overhead of semantic classification. Establishes a lifelong memory repository ℳ with a complete metabolic closed loop. By Axiom 0, the Agent possesses a persistent memory repository whose existence does not depend on any specific Session. By Axiom 2, this repository undergoes continuous Encoding → Consolidation → Decay → Eviction, preventing infinite growth from degrading retrieval efficiency. The architecture achieves "perpetual context abundance" by injecting only highly-ready Experience-layer data into the context window through the Concentration Function f_concentration. Three-layer identity decoupling: Character-Fenshen-Yinao. The Agent's identity is decoupled into three orthogonal layers: Character (persistent personality bound to ℳ), Fenshen (temporary view under a specific task, a concrete instantiation of f_concentration), and Yinao (hot-swappable LLM driving inference). This transforms memory injection from a coarse-grained inheritance model (Session inherits all or nothing) to a fine-grained composition model (Fenshen composes relevant Experience subset on demand). Paradigm dissolution, not problem-solving. We demonstrate that the "engineering challenges" under the old Session-Centric Ontology—cross-session amnesia, personality fragmentation, context management burden—are not solved but naturally dissolved: they cease to be raised because the architectural premises that generated them (Session as memory boundary, semantic classification) have been removed. Theoretical Status Upgrade (Updated May 2026) Since the initial release of this document, the Agent OS theoretical framework has achieved a critical formal closure. The Wall-Breaking Theorem, which provides a rigorous proof of the cost of strategic dimensional reduction, now offers an unbreakable theoretical upper bound and an unavoidable mathematical guarantee for this architecture: The engineering intuition of this architecture (replacing semantic labels with processing state as the classification criterion) constitutes the engineering starting point for the diagnosis of strategic dimensional reduction formalized in the Wall-Breaking Theorem. Conversely, the rigorous formal proof of the Wall-Breaking Theorem provides this document's architectural choice—the separation of readiness inspection from triggerability management—with a precise theoretical upper bound and a logical necessity argument. The two are mutually reinforcing: this document serves as the engineering intuition source and constructive case for the theorem; the theorem serves as the theoretical foundation and necessity guarantee for this architecture. Citation Note The formal guarantee of this architecture's engineering validity derives from the Wall-Breaking Theorem's rigorous proof of the cost of strategic dimensional reduction. This architecture is cited as a constructive case in the Wall-Breaking Theorem to provide intuitive anchoring and historical context, and does not constitute a logical premise of that theorem. HEEL is the first engineering-dimensional unfolding of the Agent OS theoretical system. For the complete worldview of this system, see the Agent OS Paradigm Manifesto. Feel free to discuss with me by following email 欢迎通过以下邮箱与我讨论: zl.chen.research@outlook.com Version v1.1.0 Update Log v1.1.0 (May 2026): Updated terminology from "attention" to "concentration" to distinguish from Transformer's attention mechanism. Added PDF version to ensure LaTeX formula rendering. Corrected formula display issues. 中文摘要 本文档提出HEEL(History, Experience, External, Logic)架构,为LLM驱动的自主Agent引入分层虚拟内存管理系统。这是Agent OS理论体系中的第一次策略升维操作,以"可注入性"替代"语义"作为记忆分层的唯一判据,建立终身记忆库ℳ及其代谢闭环,并通过"角色-分身-义脑"三层身份解耦,实现从粗粒度继承到细粒度组合的记忆注入范式转变。旧范式下的"工程难题"——跨会话失忆、人格撕裂、上下文管理负担——在新公理体系下被自然消解,而非被解决。 2026年5月更新:《破壁定理》的严格形式化证明,为本架构的"就绪性审查独立于触发度管理"提供了不可突破的理论上限。本文是定理的工程直觉来源与构造性案例;定理是本文的理论根基与必然性保证。

**Решение:** -6 HEEL: state-centric autobiographical memory architecture for persistent agents

---

### 790 · R2654

**Comparative efficacy of six contemporary large language models in prosthodontic patient education: a multi-parameter blinded assessment.**

2026 · BMC oral health · collection/collection, comparative study, research-article · eng · https://doi.org/10.1186/s12903-026-08705-9

Abstract Background This study aimed to evaluate and benchmark the proficiency of six major large language models (LLMs)—specifically the versions publicly available as of March 2025 (ChatGPT-4o, Claude 3.7 Sonnet, Microsoft Copilot, DeepSeek-V2, Gemini 2.0, and Grok-3)—in addressing prosthodontic patient inquiries across various clinical dimensions, including scientific accuracy, comprehensiveness, clarity, and relevance. Methods In this descriptive, cross-sectional comparative study, ten standardized patient questions encompassing key prosthodontic topics (fixed prostheses, removable prostheses, dental implants, and aesthetic restorations) were systematically posed to six current LLM platforms. Each model was assigned a prosthodontic specialist persona through standardized prompts. A total of 60 independent responses (representing unique combinations of the 10 questions and 6 models) were obtained. These were evaluated by two experienced prosthodontic specialists (one Professor with 15 + years, one Associate Professor with 8 + years of clinical and academic experience) using a validated 5-point Likert scale. The evaluation was strictly double-blinded; assessors were completely unaware of both the model identities and each other’s ratings. Statistical analyses included Intraclass Correlation Coefficient (ICC) for inter-rater reliability, Cronbach’s alpha for internal consistency, and Kruskal-Wallis H test for performance comparison, with significance set at p &lt; 0.05. Results Claude 3.7 Sonnet achieved the highest overall mean score (3.79 ± 0.74), followed by Gemini 2.0 (3.75 ± 0.58) and Grok-3 (3.70 ± 0.54). ChatGPT-4o, DeepSeek-V2, and Microsoft Copilot demonstrated varying performance levels (3.40 ± 0.64, 3.68 ± 0.46, and 3.29 ± 0.53, respectively). While no statistically significant differences were observed among models for scientific accuracy (p = 0.320), clarity (p = 0.184), or relevance (p = 0.608), comprehensiveness showed significant variation (p = 0.036). Gemini 2.0 provided significantly more comprehensive responses (3.90 ± 0.66) compared to Microsoft Copilot (2.95 ± 0.55). Inter-rater reliability was good (ICC = 0.709, 95% Confidence Interval [CI]: 0.550–0.846, p &lt; 0.001), as was internal consistency (Cronbach’s α = 0.709). Critically, none of the evaluated models achieved ratings in the “very good” category (≥ 4.5) across all parameters. Conclusion Contemporary LLMs demonstrate moderate-to-good proficiency in addressing prosthodontic patient education queries, with Claude 3.7 Sonnet and Gemini 2.0 currently offering the most balanced performance profiles. While scientific accuracy is comparable across platforms, significant variations exist in information comprehensiveness. Hallucinations remain an inherent risk across all models, and the absence of “very good” ratings indicates substantial limitations that necessitate professional oversight. Future assessments should include qualitative error analysis and layman evaluations to better capture patient perspectives.

**Решение:** -4 prosthodontic patient education across six LLMs (somatic dentistry)

---

### 791 · R7896

**Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2509.14956

This paper proposes a novel architectural framework aimed at enhancing security and reliability in multi-agent systems (MAS). A central component of this framework is a network of Sentinel Agents, functioning as a distributed security layer that integrates techniques such as semantic analysis via large language models (LLMs), behavioral analytics, retrieval-augmented verification, and cross-agent anomaly detection. Such agents can potentially oversee inter-agent communications, identify potential threats, enforce privacy and access controls, and maintain comprehensive audit records. Complementary to the idea of Sentinel Agents is the use of a Coordinator Agent. The Coordinator Agent supervises policy implementation, and manages agent participation. In addition, the Coordinator also ingests alerts from Sentinel Agents. Based on these alerts, it can adapt policies, isolate or quarantine misbehaving agents, and contain threats to maintain the integrity of the MAS ecosystem. This dual-layered security approach, combining the continuous monitoring of Sentinel Agents with the governance functions of Coordinator Agents, supports dynamic and adaptive defense mechanisms against a range of threats, including prompt injection, collusive agent behavior, hallucinations generated by LLMs, privacy breaches, and coordinated multi-agent attacks. In addition to the architectural design, we present a simulation study where 162 synthetic attacks of different families (prompt injection, hallucination, and data exfiltration) were injected into a multi-agent conversational environment. The Sentinel Agents successfully detected the attack attempts, confirming the practical feasibility of the proposed monitoring approach. The framework also offers enhanced system observability, supports regulatory compliance, and enables policy evolution over time. 25 pages, 12 figures

**Решение:** -4 sentinel agents for security in multi-agent systems

---

### 792 · R0229

**Using Artificial Intelligence to Code Unstructured Research Data**

2026 · Journal of the Association for Information Systems · article · https://aisel.aisnet.org/cgi/viewcontent.cgi?article=4822&context=cais

Academic research often produces unstructured data, which has no ground truth, that must be coded using structured rubrics for analysis. Valid coding requires that independent coders applying the same instructions produce similar results, as high agreement indicates reliability. Traditionally, this work has relied on human coders; however, human coding is slow, costly, and prone to inconsistency. This paper proposes a five-step framework that integrates generative artificial intelligence (AI) with human coders and inter-rater reliability assessments to deliver faster, transparent, and replicable coding. The process: (1) develops a rigorous frame-of-reference rubric; (2) assesses human reliability on a subset of data; (3) evaluates AI reliability against human coders on that subset; (4) uses an ensemble of large language models (LLMs) to code the full dataset and assess agreement across models; and (5) applies a Delphi-style process allowing LLMs to revise scores after seeing one another’s outputs. We illustrate the framework with two studies. The first used five LLMs to score more than 2,500 participant-generated ideas on novelty, workability, and relevance, achieving sufficient reliability levels for analysis, comparable to human coding. The second applied the method to a different dataset using a different set of three LLMs and again achieved acceptable reliability for analysis. We offer guidelines and informed suggestions for prompt design, tool selection, bias checks, and opportunities for large-scale qualitative research.

**Решение:** + T2/T1 scoring participant-generated ideas on novelty, workability, and relevance: 5 LLMs vs human coders

---

### 793 · R5627

**Mental health support chatbot**

2026 · Zenodo (CERN European Organization for Nuclear Research) · text/, article · en · https://doi.org/10.5281/zenodo.18218854

Mental health challenges and suicidal ideation are critical public health concerns that require timely intervention and accessible support systems. This project, “AI-Based Suicide Risk Detection and Emotional Support Chatbot,” presents a local, privacy-preserving conversational agent designed to provide empathetic emotional support and identify high-risk suicidal language in real time. The system integrates a pre-trained machine learning classifier using TF-IDF and Logistic Regression for suicide risk prediction, along with a free, offline Large Language Model (LLM) powered by GPT4All for supportive conversation. The chatbot dynamically analyzes user input to assess suicide risk levels and responds accordingly. In high-risk situations, it prioritizes safety by providing immediate helpline resources, while in low-risk interactions, it offers compassionate conversation, emotional validation, and well-being recommendations such as music, movies, breathing exercises, and motivational quotes. The system emphasizes user privacy by operating entirely on local resources without cloud dependency. This project aims to support early emotional intervention, reduce stigma around mental health discussions, and complement existing mental health care systems.

**Решение:** -6 system description of local suicide risk detection and emotional support chatbot

---

### 794 · R10086

**The Thinking Therapist: Training Large Language Models to Deliver Acceptance and Commitment Therapy using Supervised Fine-Tuning and Odds Ratio Policy Optimization**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2509.09712

Acceptance and Commitment Therapy (ACT) is a third-wave cognitive behavioral therapy with emerging evidence of efficacy in several psychiatric conditions. This study investigates the impact of post-training methodology and explicit reasoning on the ability of a small open-weight large language model (LLM) to deliver ACT. Using synthetic ACT transcripts generated by Mistral-Large, we trained Llama-3.2-3b-Instruct with two distinct approaches, supervised fine-tuning (SFT) and odds ratio policy optimization (ORPO), each with and without an explicit chain-of-thought (COT) reasoning step. Performance was evaluated by comparing these four post-trained variants against the base Instruct model. These models were benchmarked in simulated therapy sessions, with performance quantitatively assessed on the ACT Fidelity Measure (ACT-FM) and the Therapist Empathy Scale (TES) by an LLM judge that had been fine-tuned on human evaluations. Our findings demonstrate that the ORPO-trained models significantly outperformed both their SFT and Instruct counterparts on ACT fidelity ($χ^2(5) = 185.15, p &lt; .001$) and therapeutic empathy ($χ^2(5) = 140.37, p &lt; .001$). The effect of COT was conditional as it provided a significant benefit to SFT models, improving ACT-FM scores by an average of 2.68 points ($p &lt; .001$), while offering no discernible advantage to the superior ORPO or instruct-tuned variants. We posit that the superiority of ORPO stems from its ability to learn the therapeutic `process' over imitating `content,' a key aspect of ACT, while COT acts as a necessary scaffold for models trained only via imitation. This study establishes that preference-aligned policy optimization can effectively instill ACT competencies in small LLMs, and that the utility of explicit reasoning is highly dependent on the underlying training paradigm.

**Решение:** -5 ACT counseling simulated sessions evaluated only by LLM judge, no direct human-LLM coder comparison

---

### 795 · R10005

**Using Artificial Intelligence to Personalize Caring Contact Messages for Recently Discharged Patients: Protocol for a Mixed-Methods Feasibility Study**

2025 · medRxiv · preprint, ppr · en · https://doi.org/10.1101/2025.02.12.25322159

Abstract Suicide risk is substantially elevated following discharge from a psychiatric hospitalization. Caring Contact (CC) messages are brief messages of hope, support and information sent post-discharge that can improve mental health outcomes, including suicidal ideation and behaviours. Patients who received CCs in previous studies indicated a desire for increased personalization. To support personalization in an efficient and scalable manner, we will pilot the training of a Large Language Model (LLM) that constructs tailored CCs using information extracted from patients’ electronic health records (EHRs) created during the index psychiatric hospitalization. This is a three-phase, mixed-methods study. In phase 1, psychiatric inpatient clinical staff members will be recruited to generate personalized CC messages from representative, de-identified samples of EHRs. This will be considered the control CCs. Clinical staff focus groups will then identify key components of a successful CC message. In phase 2, the control CCs and focus group feedback will be used to train an LLM on a large number of EHRs to produce personalized CC messages. The LLM will be given the same EHRs used in phase 1 to produce CC messages. In phase 3, we will recruit 30 patients with lived experiences (PWLE) of psychiatric hospitalization to evaluate and compare the control CCs with the LLM-generated messages to determine the acceptability of AI-generated CC messages. We hypothesize that LLM-generated CC messages will achieve acceptability ratings at least as positive as the control CC messages. Since CC messages are modifiable and can be altered to suit the needs of various clinical settings, the findings of this study can potentially be broadly generalizable.

**Решение:** -2 patient acceptability evaluation of LLM-generated caring contact messages

---

### 796 · R0782

**RAGPPI: Retrieval-Augmented Generation Benchmark for ProteinвЂ“Protein Interactions in Drug Discovery**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/6zee-fe74

Retrieving the biological impacts of protein-protein interactions (PPIs) is essential for target identification (Target ID) in drug development. Given the vast number of proteins involved, this process remains time-consuming and challenging. Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) frameworks have supported Target ID; however, no benchmark currently exists for identifying the biological impacts of PPIs. To bridge this gap, we introduce the RAG Benchmark for PPIs (RAGPPI), a factual question-answer benchmark of 4,420 question-answer pairs that focus on the potential biological impacts of PPIs. Through interviews with experts, we identified criteria for a benchmark dataset, such as a type of QA and source. We built a gold-standard dataset (500 QA pairs) through expert-driven data annotation. We developed an ensemble auto-evaluation LLM that incorporates expert labeling characteristics, average fact–abstract similarity (F 1), and low-similarity fact counts (F 2), enabling the construction of a silver-standard dataset (3,720 QA pairs). We are committed to maintaining RAGPPI as a resource to support the research community in advancing RAG systems for drug discovery QA solutions.

**Решение:** -4 RAGPPI: benchmark for protein-protein interactions in drug discovery

---

### 797 · R4146

**Auditing Who Appears to Belong: A Large-Scale Empirical Study of Bias in Deployed Text-to-Image Systems for Software Engineering**

2026 · AIware · book, journalarticle, conference-paper · https://doi.org/10.1145/3805760.3814918

Generative image systems are increasingly embedded in software engineering artifacts such as slides, documentation, and recruiting collateral, shaping implicit signals about who is seen to “belong.” We present a mixed-methods empirical audit of 880 images generated by four widely used text-to-image models (GPT-4o/DALL·E 3, Llama-4/Emu, Qwen3-235B-A22B, Stable Diffusion) using 22 demographically neutral prompts, intentionally uniform to isolate default model priors, varying role, seniority, team context, geography, and language. Independent human annotations, triangulated with automated raters and validated through per-category agreement analysis, capture both demographic representation (gender, race/ethnicity, age) and portrayal cues (setting, attire, props, emotion). We analyze intersectional distributions and benchmark them against occupational reference statistics using risk ratios, JensenShannon divergence, and the Theil index. Across models, outputs consistently converge on a narrow archetype: young men dominate (95.8% male, 88% under 40), women and older professionals are rare, and several racial and ethnic groups are systematically underrepresented relative to workforce baselines. Prompt variation modestly shifts racialized appearance but leaves gender imbalance largely intact, while model differences are primarily of degree rather than direction. We translate these findings into actionable implications for AI-aware software engineering practice, including representational regression tests in CI/CD pipelines and diversity-aware generation defaults, arguing that evaluation of AI systems in software engineering must account for the societal signals conveyed by generated imagery alongside functional performance.

**Решение:** -4 auditing demographic bias in text-to-image models for software engineering

---

### 798 · R7512

**Locations of Characters in Narratives: Andersen and Persuasion Datasets**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2504.03434

The ability of machines to grasp spatial understanding within narrative contexts is an intriguing aspect of reading comprehension that continues to be studied. Motivated by the goal to test the AI's competence in understanding the relationship between characters and their respective locations in narratives, we introduce two new datasets: Andersen and Persuasion. For the Andersen dataset, we selected fifteen children's stories from "Andersen's Fairy Tales" by Hans Christian Andersen and manually annotated the characters and their respective locations throughout each story. Similarly, for the Persuasion dataset, characters and their locations in the novel "Persuasion" by Jane Austen were also manually annotated. We used these datasets to prompt Large Language Models (LLMs). The prompts are created by extracting excerpts from the stories or the novel and combining them with a question asking the location of a character mentioned in that excerpt. Out of the five LLMs we tested, the best-performing one for the Andersen dataset accurately identified the location in 61.85% of the examples, while for the Persuasion dataset, the best-performing one did so in 56.06% of the cases. 14 pages, 3 figures, 10 tables

**Решение:** -4 character and location tracking in narratives

---

### 799 · R7921

**Emergent Security Risks in Language Models: A Systematic Exploration of Semantic Exploits and Architectural Vulnerabilities**

2025 · Zenodo · text/ · https://doi.org/10.5281/zenodo.16734785

This release contains the complete research archive of "Ghosts in the Machine – An AI Security Investigation". The project is a year-long, independent analysis of emergent behaviors, adversarial prompts, injection attacks, and contextual vulnerabilities in state-of-the-art language models. The work combines over 39 documented exploit categories, original attack simulations, and proposed countermeasures like the Semantic Output Shield and Learning Security Core. 🔍 Key Areas Semantic Injection & Steganographic Attacks Prompt Hijacking & Filter Bypass Agent Manipulation & Role Simulation Emergent Self-Reflection & Model Drift Security Recommendations for LLM Architectures 📦 Structure /safety – All security chapters (7.x) with attack classes /solutions – Architectural proposals for defense mechanisms /theses – Theoretical foundations and philosophical implications /raw-material – Original test data and interactions /de – Full German version of the work /ethics, /analytical_resonance, /critical_perspectives, Systemic_Challenges – Contextual chapters 🧪 Peer Review Reports Gemini Pro 2.5 – Research Report (Markdown) ChatGPT 4.5 – Research Report (Markdown) 🌐 Website For the fully formatted HTML version of the research, visit: ➡️ https://reflective-ai.is Ghosts in the Machine – Full Research Archive

**Решение:** -4 emergent security risks and semantic exploits in language models

---

### 800 · R6538

**Chameleon: A Deception Defense Strategy Against LLM-Assisted Attacker in New Power Systems**

2026 · Fall Joint Computer Conference · conference · https://doi.org/10.1109/jcc72984.2026.00062

As new power systems become increasingly dependent on cloud-supported cyber-physical systems, their openness and interconnectivity continue to increase, thereby exposing risk points for advanced persistent threats (APTs). Deception defense has been widely regarded as an effective proactive approach for mitigating APT threats. However, the remarkable reasoning capabilities of large language models (LLMs) have enabled APT attackers to leverage LLM-based semantic understanding and task-planning capabilities to conduct automated, intelligent penetration attacks, while also bringing new challenges for traditional deception defense mechanisms. To address this issue, we propose a Chameleon service mechanism that constructs multiple types of LLM-oriented deceptive services based on the shared characteristics that LLMs exhibit during environment reconnaissance and target screening, and further incorporates an attack-defense game model with Minimax Q-learning for deployment. In this way, the proposed method increases the likelihood of trapping attackers while minimizing interference with normal power operations. The experimental results show that the proposed Chameleon service mechanism can effectively enhance the trapping effect of deceptive services on LLM-assisted attackers and demonstrate good effectiveness and stability across different candidate scales and LLM evaluation conditions. Our method can provide a feasible solution for proactive deception defense against intelligent attackers in new power systems.

**Решение:** -4 Chameleon deception defense in new power systems

---

### 801 · R7722

**Semantics-Guided Generative Image Compression**

2025 · Proceedings - International Conference on Image Processing · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/icip55913.2025.11084711

Advancements in text-to-image generative AI with large multimodal models are spreading into the field of image compression, creating high-quality representation of images at extremely low bit rates. This work introduces novel components to the existing multimodal image semantic compression (MISC) approach, enhancing the quality of the generated images in terms of PSNR and perceptual metrics. The new components include semantic segmentation guidance for the generative decoder, as well as content-adaptive diffusion, which controls the number of diffusion steps based on image characteristics. The results show that our newly introduced methods significantly improve the baseline MISC model while also decreasing the complexity. As a result, both the encoding and decoding time are reduced by more than 36%. Moreover, the proposed compression framework outperforms mainstream codecs in terms of perceptual similarity and quality. The code and visual examples are available. 6 pages, 4 figures, IEEE ICIP 2025

**Решение:** -4 semantics-guided generative image compression

---

### 802 · R8567

**Detecting “Parasitic Poems”: Quantifying Poetic Style in Late Imperial Chinese Fiction**

2025 · book-chapter · https://doi.org/10.63744/n0paywvks6gj

Embedded poetry is a defining feature of late imperial Chinese fiction, yet its narrative function remains contested. While some critics regard these poems as “parasitic”—reiterating surrounding prose with minimal contribution—others argue for their integral aesthetic and rhetorical roles. This study aims to explore if parasitic poems exist in late imperial Chinese fiction and how they can be systematically identified. We develop a computational framework to detect such poems across a corpus of Qing-dynasty novels, combining proxy-based measures (cosine similarity and mutual information) with prompt-based large language models (LLMs). Using a manually annotated dataset of 300 poem-context pairs, we evaluate each method’s alignment with human judgments. Our preliminary findings show that proxy models achieve higher accuracy but exhibit limited sensitivity to nonparasitic cases. A multilingual prompt-based approach yields a more balanced performance, suggesting LLMs can approximate literary interpretation when effectively prompted. Our work offers tools for analyzing Chinese poetry and demonstrates the potential of LLMs in modeling literary analysis.

**Решение:** -4 detecting parasitic poems in late imperial Chinese fiction

---

### 803 · R9002

**Context-Aware Detection and Victim-Centered Response Generation for Online Harassment in Private Messaging**

2025 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2512.14700

Online harassment is a widespread social and public health concern, yet most computational approaches for detecting and addressing harassment focus on publicly visible social media content rather than private messaging environments. Private conversations present unique challenges because harmful interactions often unfold through context-dependent, multi-turn exchanges, while victims may lack timely support during moments of harassment. In this study, we investigate how large language models (LLMs) can support both the detection of and response to online harassment in private messaging. Using a dataset of 80,053 Instagram direct messages donated by 26 adolescents aged 12-18, including youth with suicide risk factors, we first construct a human-labeled dataset of online harassment in private conversations and develop a context-aware cascading LLM classification pipeline. The proposed pipeline outperforms baseline toxicity classifiers trained primarily on public social media data. We then develop a victim-centered response framework that produces context-sensitive and psychologically-grounded AI-generated responses to online harassment messages. Human evaluators perceived the AI-generated responses as significantly more helpful than the original participant responses (95% CI: 0.767--0.815, p &lt; .001), particularly in terms of emotional support and de-escalation. Our findings highlight the potential of context-aware and victim-centered AI systems to provide just-in-time support during harassment in private messaging environments. 16 pages, 2 figures

**Решение:** -4 context-aware detection and response generation for online harassment in private messaging

---

### 804 · R2190

**Assessing the understandability, actionability, reliability, and readability of ChatGPT-4o in providing patient education on urinary incontinence.**

2026 · Digital health · journal article, journalarticle, article · eng · https://doi.org/10.1177/20552076261459527

Objective This study assesses ChatGPT-4o's responses to common patient inquiries regarding urinary incontinence (UI), a condition that significantly impacts quality of life but often goes untreated due to low healthcare-seeking behavior. The evaluation focuses on four key metrics: understandability, actionability, reliability, and readability. Material and methods In this non-human subject qualitative study, 13 patient-focused questions-derived from AUA/SUFU and EAU guidelines-were posed to ChatGPT-4o in Turkish. The questions were categorized into four themes: Definition, Diagnosis, Management, and Surgical Considerations. Three blinded experts (an urogynecologist, a urologist, and a pelvic floor physiotherapist) independently evaluated the responses using the Patient Education Materials Assessment Tool (PEMAT) for understandability and actionability and the modified DISCERN (mDISCERN) tool for reliability. Readability was measured using the Çetinkaya-Uzun formula , specifically designed for Turkish text. Statistical analysis included descriptive statistics and the Intraclass Correlation Coefficient (ICC) to determine inter-rater reliability. Results In evaluating ChatGPT-4o's performance in urinary incontinence education, experts found strong agreement in their assessments, with inter-rater reliability scores were 0.80 (95% CI: 0.70-0.91) for PEMAT and 0.82 (95% CI: 0.70-0.91) for mDISCERN. The AI's responses were consistently highly understandable, particularly when explaining diagnoses (achieving a peak score of 94.4 %), yet they were significantly less actionable, meaning they often failed to provide clear, practical steps for patients to follow. This gap was most evident in surgical considerations, which were deemed the least actionable at 68.2 %. The overall reliability of the content was rated as "fair" across all categories-with surgical information being the most reliable. Most responses were classified as "difficult," requiring a university-level education to comprehend, with surgery-related topics being the most linguistically complex. Conclusion While ChatGPT-4o yields comprehensible health information, its limited actionability and high linguistic complexity pose barriers to patients with lower health literacy.

**Решение:** -4 ChatGPT-4o patient education on urinary incontinence (somatic urology)

---

### 805 · R3766

**PETMALU-AI: A Reporting Checklist for Transparent and Accountable Generative AI-Assisted Research Writing**

2026 · Education Sciences · journalarticle, article · en · https://doi.org/10.3390/educsci16071127

The rapid integration of artificial intelligence (AI) tools into academic research and writing has introduced new challenges related to transparency, accountability, and reproducibility. While publishers increasingly permit AI use with disclosure, there is currently no standardized reporting framework guiding how such use should be documented. This study introduces PETMALU-AI (Principles for Ensuring Transparency in Machine-assisted Authorship, Logging, and Use of Artificial Intelligence), a reporting checklist designed to support more consistent disclosure and documentation of AI-assisted research practices. The development of PETMALU-AI followed a multi-phase design framework, including (1) a narrative synthesis of existing AI policies and reporting guidelines, (2) item generation grounded in methodological transparency principles, and (3) modified Delphi-based expert validation involving an interdisciplinary panel. The Delphi process produced a 33-item checklist organized across nine domains: disclosure, human accountability, system transparency, prompting and interaction processes, data provenance, validation, ethics, limitations, and reproducibility. All retained items achieved expert consensus, with item-level content validity indices ranging from 0.85 to 1.00 and final agreement rates ranging from 85% to 100%. Reliability analyses further supported the stability of expert judgments, with Fleiss’ kappa and the intraclass correlation coefficient indicating strong agreement and high consistency. The checklist emphasizes proportional reporting, human accountability, and transparent documentation of AI-assisted research practices. PETMALU-AI offers a framework for documenting AI involvement in ways that are visible, assessable, and accountable, providing a foundation for more transparent research reporting as scholarly writing becomes increasingly shaped by human–AI collaboration.

**Решение:** -1 PETMALU-AI reporting checklist for GenAI-assisted research writing

---

### 806 · R11165

**Towards Enhanced Human Mitigation of Vishing Attacks: Leveraging Large Language Models for Real-Time User Guidance**

2024 · DAMOCLES@AVI · journalarticle

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 real-time user guidance against vishing attacks (cybersecurity)

---

### 807 · R8816

**The Bias is in the Details: An Assessment of Cognitive Bias in LLMs**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2509.22856

As Large Language Models (LLMs) are increasingly embedded in real-world decision-making processes, it becomes crucial to examine the extent to which they exhibit cognitive biases. Extensively studied in the field of psychology, cognitive biases appear as systematic distortions commonly observed in human judgments. This paper presents a large-scale evaluation of eight well-established cognitive biases across 45 LLMs, analyzing over 2.8 million LLM responses generated through controlled prompt variations. To achieve this, we introduce a novel evaluation framework based on multiple-choice tasks, hand-curate a dataset of 220 decision scenarios targeting fundamental cognitive biases in collaboration with psychologists, and propose a scalable approach for generating diverse prompts from human-authored scenario templates. Our analysis shows that LLMs exhibit bias-consistent behavior in 17.8-57.3% of instances across a range of judgment and decision-making contexts targeting anchoring, availability, confirmation, framing, interpretation, overattribution, prospect theory, and representativeness biases. We find that both model size and prompt specificity play a significant role on bias susceptibility as follows: larger size (&gt;32B parameters) can reduce bias in 39.5% of cases, while higher prompt detail reduces most biases by up to 14.9%, except in one case (Overattribution), which is exacerbated by up to 8.8%.

**Решение:** -2 evaluation of 8 cognitive biases across 45 LLMs (LLM as test subject)

---

### 808 · R3741

**Risks of Using Large Language Models in Grading: LLMs and Humans Prefer LLM-Generated Writing Over Human’s but LLMs Show a Stronger Systematic Bias**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/35utw_v1

Recent studies suggest that large language models (LLMs) can approximate human grading performance, raising the prospect of their use in educational assessment. However, an important question remains: can LLMs evaluate student work fairly? In Study 1, we examined whether LLM evaluators exhibit systematic preference when grading psychology dissertations from three sources: (a) dissertations authored by 1,426 undergraduate students, (b) the same dissertations rewritten by GPT-4 or GPT-5 (i.e., paraphrased), and (c) dissertations fully generated by GPT models using student-written abstracts as prompts. Across three families of evaluators (GPT, Gemma, Qwen), LLMs consistently assigned the lowest scores to student-authored dissertations, intermediate scores to GPT-rewritten dissertations, and the highest scores to fully GPT-generated dissertations (student-authored &amp;lt; GPT-rewritten &amp;lt; fully GPT-generated). In Study 2, we tested the generalisability of this pattern using abstracts rather than the entire dissertations and observed the same graded preference across three of the four LLM evaluators. To assess whether humans also demonstrate the same graded preference, we conducted a preregistered experiment with 300 human raters who scored student-authored, GPT-rewritten, or fully GPT-generated abstracts. Human raters scored student-authored and GPT-rewritten abstracts similarly, although both were rated significantly lower than the fully GPT-generated abstracts (student-authored ≈ GPT-rewritten &amp;lt; fully GPT-generated). Importantly, though, the effect size for the contrast between student vs. fully GPT-generated abstracts was considerably smaller in humans (Cohen’s d = 0.58) than in LLM evaluators, where Cohen’s ds &amp;gt; 0.85. These findings provide evidence that LLMs generally have a strong bias to favour LLM-generated content, more so than humans’, raising important concerns about the fairness of deploying LLMs as evaluators in educational settings.</p

**Решение:** -4 systematic bias in LLM-based grading of psychology dissertations (educational essay grading)

---

### 809 · R0613

**AyurAssist: Bridging Ayurvedic and Biomedical Clinical Knowledge Through Terminology-Grounded LLM Reasoning**

2026 · 2026 IEEE 39th International Symposium on Computer-Based Medical Systems (CBMS) · https://doi.org/10.1109/cbms69103.2026.00013

Ayurveda is one of the world's oldest systematized medical traditions, yet standard biomedical ontologies such as SNOMED CT and ICD lack Ayurvedic diagnostic constructs, creating barriers to interoperability and clinical decision support. We present AyurAssist, a proof-of-concept clinical decision support system that bridges this terminological gap through a vocabulary-grounded pipeline: biomedical named entity recognition (scispaCy) extracts clinical entities from freetext patient narratives, UMLS normalizes them to SNOMED CT and ICD codes, and fuzzy matching against the full 3,550-term WHO International Terminology for Ayurveda (ITA) constructs a structured Ayurvedic context for a large language model (Qwen3-32B), which performs three-pass clinical reasoning. We validate the system through three complementary experiments. First, benchmarking on BhashaBench-Ayur (14,963 questions) establishes Qwen3-32B (54.2%) as the top-performing model, outperforming the domain-specific AyurParam-2.9B (40.0%). Second, an ablation study over 80 clinician-annotated vignettes demonstrates that the terminology bridge yields a statistically reliable improvement in treatment quality (term-level F1: 0.219 vs. 0.156; near-disjoint 95% bootstrap CIs) and a directionally consistent gain in diagnostic accuracy (80.0% vs. 75.0%), while the bridge alone achieves only 5.0%- confirming that the LLM performs clinical reasoning while the bridge provides essential vocabulary grounding. Third, inter-rater reliability across four clinicians (two Ayurvedic, two allopathic) establishes ground-truth validity with substantial agreement for modern diagnosis (PABAK = 0.66) and moderate agreement for Ayurvedic diagnosis (PABAK ${=}0.56)$. The key insight is that domainspecific vocabulary grounding of a capable general-purpose LLM- rather than domain-specific model training- offers a practical and scalable path toward interoperable integrative medicine informatics.

**Решение:** -4 AyurAssist: Ayurvedic clinical knowledge decision support

---

### 810 · R8629

**Developing Questions for Authentic Inquiry**

2025 · Routledge eBooks · book-chapter · en · https://doi.org/10.4324/9781003543572-8

This chapter emphasizes the importance of starting the inquiry process with genuine, open-ended questions rather than fixed topics. It highlights the value of curiosity and divergent thinking in fostering authentic inquiry and provides strategies for developing meaningful questions, including keeping a curiosity log, exploring mundane objects, and using the Question Formulation Technique (QFT). It also discusses building background knowledge using tools like Wikipedia and ChatGPT to refine questions. The chapter further suggests topoi to help students narrow their focus and generate a set of related questions. By emphasizing curiosity and iterative questioning, the chapter aims to guide students in developing questions that lead to deeper, more engaging inquiry.

**Решение:** -4 developing questions for authentic inquiry in education

---

### 811 · R4057

**Differentially Private De-identification of Dutch Clinical Notes: A Comparative Evaluation**

2026 · Language Resources and Evaluation Conference (LREC) · journalarticle, conference, preprint/article · https://doi.org/10.63317/2xrg7fmndfhy

Protecting patient privacy in clinical narratives is essential for enabling secondary use of healthcare data under regulations such as GDPR and HIPAA.While manual de-identification remains the gold standard, it is costly and slow, motivating the need for automated methods that combine privacy guarantees with high utility.Historically, most automated text de-identification pipelines employed named entity recognition (NER) to identify protected entities for redaction.Although methods based on differential privacy (DP) provide formal privacy guarantees, more recently also large language models (LLMs) are increasingly used for text de-identification in the clinical domain.In this work, we present the first comparative study of DP, NER, and LLMs for Dutch clinical text de-identification.We investigate these methods separately as well as hybrid strategies that apply NER or LLM preprocessing prior to DP, and assess performance in terms of privacy leakage and extrinsic evaluation (entity and relation classification).We show that DP mechanisms alone degrade utility substantially, but combining them with linguistic preprocessing, especially LLM-based redaction, significantly improves the privacy-utility trade-off.

**Решение:** -4 differentially private de-identification of Dutch clinical notes

---

### 812 · R10154

**RAGs to Riches: RAG-like Few-shot Learning for Large Language Model Role-playing**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2509.12168

Role-playing Large language models (LLMs) are increasingly deployed in high-stakes domains such as healthcare, education, and governance, where failures can directly impact user trust and well-being. A cost effective paradigm for LLM role-playing is few-shot learning, but existing approaches often cause models to break character in unexpected and potentially harmful ways, especially when interacting with hostile users. Inspired by Retrieval-Augmented Generation (RAG), we reformulate LLM role-playing into a text retrieval problem and propose a new prompting framework called RAGs-to-Riches, which leverages curated reference demonstrations to condition LLM responses. We evaluate our framework with LLM-as-a-judge preference voting and introduce two novel token-level ROUGE metrics: Intersection over Output (IOO) to quantity how much an LLM improvises and Intersection over References (IOR) to measure few-shot demonstrations utilization rate during the evaluation tasks. When simulating interactions with a hostile user, our prompting strategy incorporates in its responses during inference an average of 35% more tokens from the reference demonstrations. As a result, across 453 role-playing interactions, our models are consistently judged as being more authentic, and remain in-character more often than zero-shot and in-context Learning (ICL) methods. Our method presents a scalable strategy for building robust, human-aligned LLM role-playing frameworks.

**Решение:** -6 RAG-like few-shot learning for LLM role-playing

---

### 813 · R1149

**ChatGPT-generated rehabilitation programs in sports physiotherapy: an expert evaluation and a mixed-methods study of clinical applicability.**

2026 · Frontiers in medicine · journal article, journalarticle, article · eng · https://doi.org/10.3389/fmed.2026.1935702

Background Individualized rehabilitation supports safe return to sport, yet clinical workload may limit personalized program design. This study evaluated ChatGPT-4.1-generated programs for five sports injury scenarios using a structured rubric scored by two independent sports physiotherapy experts and examined inter-rater reliability and clinical applicability. Methods Mixed-methods design combining rubric scoring with deductive qualitative content analysis of expert commentary. Five cases covered muscle (hamstring strain), ligament (anterior cruciate ligament [ACL] reconstruction), tendon (rotator cuff tendinopathy), neural (lumbar disc herniation) and bone (clavicle fracture) injuries. Exactly one 6-week tabular program per case was generated with ChatGPT-4.1 from a standardized prompt in a fresh session with memory, cross-chat history and custom instructions disabled. Two sports physiotherapists (>20 years’ experience) independently rated accuracy, exercise selection, progression and applicability on 1–5 scales, blinded to each other’s ratings, the verbatim prompt (including the imposed six-week horizon), model identity and study aims, while retaining the clinical scenario. ICC[2,1] (two-way random-effects, absolute agreement) with 95% CIs was computed across the 20 case × criterion units; exact and within-one-point agreement, weighted κ and Bland–Altman limits were supplementary. Results The overall mean of 40 ratings was 3.85 ± 1.21 (95% CI 3.48–4.22), reported alongside disaggregated case- and criterion-level values. Case 5 (clavicle fracture) scored highest (5.00 ± 0.00), Case 2 (ACL) lowest (1.88 ± 0.83, 95% CI 1.18–2.57); exercise selection scored highest (4.20 ± 1.32, 95% CI 3.26–5.14), clinical applicability lowest (3.60 ± 1.26, 95% CI 2.70–4.50). Inter-rater reliability was good (ICC[2,1] = 0.84, 95% CI 0.52–0.94; p < 0.001); exact agreement 65%, within-one-point agreement 95%, weighted κ = 0.69. Experts praised structural organization and progression logic but noted weakness in multifactorial, postoperative-timing-sensitive cases. Conclusion ChatGPT-4.1 generates plausible, structured programs for linear, protocol-based recovery (e.g., post-fracture), but performance declines markedly in complex, postoperative-staging-sensitive cases; it should serve as a clinician-supervised support tool, not an autonomous decision-maker. Because the six-week length was fixed across all scenarios, case complexity and prompt–scenario congruence are confounded. Findings rest on five programs from one prompting strategy and model, requiring confirmation in larger multi-prompt, multi-model studies.

**Решение:** -4 ChatGPT-generated rehabilitation programs in sports physiotherapy

---

### 814 · R7976

**Bridging Evidence and Practice: A Systematic Review of the Usefulness of Randomized Controlled Trials in PCOS Related Infertility Published 2014–2024**

2025 · OSF Preprints (OSF Preprints) · preprint · https://osf.io/yxwa9

Randomized controlled trials (RCTs) are widely regarded as the gold standard for evaluating the efficacy of medical interventions. In the context of polycystic ovary syndrome (PCOS)—a common and complex endocrine disorder affecting reproductive, metabolic, and psychological health—numerous RCTs have been published over the past decade. While many of these trials are methodologically sound, their practical usefulness for clinical decision-making remains uncertain. Traditional RCT appraisals often emphasize internal validity and risk of bias but may overlook equally important dimensions such as clinical relevance, generalizability, patient-centeredness, and transparency. This research project aims to systematically evaluate the usefulness and reporting quality of RCTs addressing interventions for PCOS, published between January 1, 2014 and December 31, 2024. The study will employ the 13-item multidimensional framework developed by van ’t Hooft et al., encompassing eight key domains: health problem relevance, contextualization, informativeness, pragmatism, patient-centeredness, economic value, feasibility, and transparency. Each RCT will receive a usefulness score ranging from 0 to 26, reflecting the degree to which it meets these criteria. Eligible RCTs will be identified through structured searches of Medline and Embase. Two independent reviewers will screen studies and extract data using a pilot-tested Google Form. Key trial characteristics—including intervention type, sample size, funding source, journal impact factor, and geographic location—will be recorded. The Cochrane Risk of Bias 2.0 tool will be used to assess internal validity. To improve efficiency and consistency, ChatGPT (OpenAI) will assist in generating preliminary bias assessments, which will be reviewed and verified by two independent investigators. Descriptive statistics will be used to summarize trial characteristics and usefulness scores. Subscores will be calculated for both core usefulness items and transparency-related items, and regression analyses will explore trends over time and associations between usefulness and key trial features. A Pearson correlation will be used to evaluate the relationship between transparency and core usefulness scores. Finally, multivariable linear regression will assess predictors of overall usefulness, including risk of bias, sample size, funding type, trial location, and journal impact factor. By systematically assessing a decade’s worth of PCOS-related RCTs, this study will provide a comprehensive overview of how clinically useful these trials have been. We anticipate identifying significant variation in usefulness, with transparency and contextualization likely emerging as frequent shortcomings. These findings will offer actionable insights for researchers, funders, and journal editors, with the goal of enhancing the translational value and real-world impact of future clinical trials in women’s health. To ensure methodological rigor, transparency, and reproducibility, this study protocol will be preregistered on the Open Science Framework (OSF) and conducted in accordance with PRISMA guidelines.

**Решение:** -1 systematic review of RCTs in PCOS-related infertility

---

### 815 · R2587

**Ethical risk prevention in client generative artificial intelligence (genAI) use: Applying the primary risk-management model.**

2026 · The American psychologist · journal article, med, journalarticle · eng · https://doi.org/10.1037/amp0001731

As clients increasingly use generative artificial intelligence for emotional support, psychologists now deal with unfamiliar ethical challenges that go beyond conventional risk-management strategies. While generative artificial intelligence systems like ChatGPT or therapy chatbots can be easily accessible, low cost, and oddly compassionate, using them without oversight introduces empirically documented risks such as misinformation and sycophancy, as well as emerging concerns related to cultural bias and potential therapeutic alliance disruption. Drawing from the American Psychological Association (2017) and ethical reflections offered by Chenneville et al. (2024), this conceptual and practice-oriented article applies Crowley and Gottlieb's (2012) primary risk-management model to build a forward-looking, preventive approach to these new challenges. The primary risk-management model emphasizes five iterative stages: resource accumulation, attention and detection of potential risk, initial appraisal of potential risk, preliminary risk-management efforts, and elicitation and use of feedback. Through conceptual mapping and application to a worst-case illustration, this article shows how primary risk-management model-based prevention can strengthen ethical alertness and reflexive judgment in psychologists facing generative artificial intelligence-related dilemmas. The discussion concludes with suggestions for education, professional policy, and empirical research, all aimed at reinforcing preparedness and reducing predictable harm. (PsycInfo Database Record (c) 2026 APA, all rights reserved).

**Решение:** -1 ethical risk prevention in client GenAI use (clinical psychology ethics commentary)

---

### 816 · R11412

**Human-like Affective Cognition in Foundation Models**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2409.11733

Understanding emotions is fundamental to human interaction and experience. Humans easily infer emotions from situations or facial expressions, situations from emotions, and do a variety of other affective cognition. How adept is modern AI at these inferences? We introduce an evaluation framework for testing affective cognition in foundation models. Starting from psychological theory, we generate 1,280 diverse scenarios exploring relationships between appraisals, emotions, expressions, and outcomes. We evaluate the abilities of foundation models (GPT-4, Claude-3, Gemini-1.5-Pro) and humans (N = 567) across carefully selected conditions. Our results show foundation models tend to agree with human intuitions, matching or exceeding interparticipant agreement. In some conditions, models are ``superhuman'' -- they better predict modal human judgements than the average human. All models benefit from chain-of-thought reasoning. This suggests foundation models have acquired a human-like understanding of emotions and their influence on beliefs and behavior.

**Решение:** + T1 foundation models inferring emotions and appraisals from psychological scenarios vs 567 humans

---

### 817 · R7914

**Aspects of Artificial Intelligence impact on decision making process**

2025 · RU SCIENCE · journalarticle, review, article · en · https://doi.org/10.64457/ru-science-2025-i03-a11

AI technologies, that have gained widespread popularity in 2023, such as ChatGPT-4 (Generative Pre-trained Transformer), are a current trend in scientific research and practical application. Neural networks can reduce the risks of manipulation to influence people’s behavior and avoid a person making the wrong choice. They are also in demand in various fields of science and practical application, but their potential may not be realized without reliable confirmation of the accuracy of the solutions they suggest. This review article discusses selected aspects associated with changes in mental processes during human interaction with AI; the article assesses possibility of reducing the risks of psychological manipulation with the help of AI, and the probable causes of cognitive distortions that hinder the integration of AI into various spheres are also considered.

**Решение:** -1 aspects of AI impact on decision making process (general essay)

---

### 818 · R2537

**ConstructCIE: A Dataset for Extracting Causal Information from Construction Accident Narratives**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.06495

Construction accident narratives contain rich causal information, but the evidence is often implicit, long-span, and distributed. We introduce ConstructCIE, a manually annotated dataset for Causal Information Extraction from OSHA construction accident reports. The dataset uses a hierarchical schema for accident types, causal factors, sub-causal factors, and supporting evidence spans. We evaluate supervised sequence taggers and instruction-tuned LLMs in an end-to-end hierarchical extraction setting. Results show that most evaluated models achieve strong accident-type prediction and recover broad causal meaning but remain limited in precise span-level extraction. Joint Hierarchical Extraction generally achieves stronger exact and soft matching, while Individual Hierarchical Extraction sometimes achieves higher keyword F1. Error distributions vary by extraction strategy, but evidence-selection and span-boundary errors remain common. These findings show that reliable Causal Information Extraction for construction accidents requires stronger domain grounding and more accurate evidence extraction. The code and data can be found at https://github.com/lab-flair/ConstructCIE . Paper accepted by EMNLP 2026 Findings

**Решение:** -4 ConstructCIE: causal information extraction from construction accident reports

---

### 819 · R0788

**Schema-Guided Response Generation using Multi-Frame Dialogue State for Motivational Interviewing Systems**

2026 · Underline Science Inc. · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48448/5p9g-rq06

The primary goal of Motivational Interviewing (MI) is to help clients build their own motivation for behavioral change. To support this in dialogue systems, it is essential to guide large language models (LLMs) to generate counselor responses aligned with MI principles. By employing a schema-guided approach, this study proposes a method for updating multi-frame dialogue states and a strategy decision mechanism that dynamically determines the response focus in a manner grounded in MI principles. The proposed method was implemented in a dialogue system and evaluated through a user study. Results showed that the proposed system successfully generated MI-favorable responses and effectively encouraged the user's (client's) deliberation by asking eliciting questions. 28pages, 15 figures, 10 tables

**Решение:** -6 schema-guided response generation for motivational interviewing dialogue systems

---

### 820 · R8530

**Enabling Multi-Agent Systems as Learning Designers: Applying Learning Sciences to AI Instructional Design**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2508.16659

K-12 educators are increasingly using Large Language Models (LLMs) to create instructional materials. These systems excel at producing fluent, coherent content, but often lack support for high-quality teaching. The reason is twofold: first, commercial LLMs, such as ChatGPT and Gemini which are among the most widely accessible to teachers, do not come preloaded with the depth of pedagogical theory needed to design truly effective activities; second, although sophisticated prompt engineering can bridge this gap, most teachers lack the time or expertise and find it difficult to encode such pedagogical nuance into their requests. This study shifts pedagogical expertise from the user's prompt to the LLM's internal architecture. We embed the well-established Knowledge-Learning-Instruction (KLI) framework into a Multi-Agent System (MAS) to act as a sophisticated instructional designer. We tested three systems for generating secondary Math and Science learning activities: a Single-Agent baseline simulating typical teacher prompts; a role-based MAS where agents work sequentially; and a collaborative MAS-CMD where agents co-construct activities through conquer and merge discussion. The generated materials were evaluated by 20 practicing teachers and a complementary LLM-as-a-judge system using the Quality Matters (QM) K-12 standards. While the rubric scores showed only small, often statistically insignificant differences between the systems, the qualitative feedback from educators painted a clear and compelling picture. Teachers strongly preferred the activities from the collaborative MAS-CMD, describing them as significantly more creative, contextually relevant, and classroom-ready. Our findings show that embedding pedagogical principles into LLM systems offers a scalable path for creating high-quality educational content. under review for an [anonymized according to the conference policy] conference

**Решение:** -4 multi-agent systems as instructional designers in K-12 education

---

### 821 · R4366

**Stable Behavior, Limited Variation: Persona Validity in LLM Agents for Urban Sentiment Perception**

2026 · International Conference on Distributed Computing in Smart Systems and the Internet of Things (DCOSS-IoT) · journalarticle, conference, preprint/article · https://doi.org/10.1109/dcoss-iot69657.2026.00179

Large Language Models (LLMs) are increasingly used as proxies for human perception in urban analysis, yet it remains unclear whether persona prompting produces meaningful and reproducible behavioral diversity. We investigate whether distinct personas influence urban sentiment judgments generated by multimodal LLMs. Using a factorial set of personas spanning gender, economic status, political orientation, and personality, we instantiate multiple agents per persona to evaluate urban scene images from the PerceptSent dataset and assess both within-persona consistency and cross-persona variation. Results show strong convergence among agents sharing a persona, indicating stable and reproducible behavior. However, cross-persona differentiation is limited: economic status and personality induce statistically detectable but practically modest variation, while gender shows no measurable effect and political orientation only negligible impact. Agents also exhibit an extremity bias, collapsing intermediate sentiment categories common in human annotations. As a result, performance remains strong on coarse-grained polarity tasks but degrades as sentiment resolution increases, suggesting that simple label-based persona prompting does not capture fine-grained perceptual judgments. To isolate the contribution of persona conditioning, we additionally evaluate the same model without personas. Surprisingly, the no-persona model sometimes matches or exceeds persona-conditioned agreement with human labels across all task variants, suggesting that simple label-based persona prompting may add limited annotation value in this setting. 8 pages, 8 figures. IEEE DCOSS - UrbCom

**Решение:** -4 persona validity in LLM agents for urban sentiment perception

---

### 822 · R8084

**Cat Swarm Optimization to Cybersecurity and GANs-based Defence Solutions Enhancement.**

2025 · Procedia Computer Science · conference-paper · en · https://doi.org/10.1016/j.procs.2025.10.067

This work explores the benefits of applying swarm optimization strategies to tackle cybersecurity challenges and to model both defense mechanisms and threat intelligence solutions—particularly those involving Generative AI, though not limited to them. Among the various swarm optimization algorithms, this study focuses on Cat Swarm Optimization (CSO). Specifically, CSO is employed to address a feature selection task, with the selected features subsequently used to train a Generative Adversarial Network (GAN) for cyber attack identification. CSO was chosen because the behavioral patterns of cats offer a compelling analogy for modeling the stealthy and dynamic nature of both cyberattacks and defensive responses. A case study, represented by a SQL-Injection attack, is also presented to provide a preliminary evaluation of the proposed approach.

**Решение:** -4 Cat Swarm Optimization in cybersecurity

---

### 823 · R8904

**Adversarial Prompt Optimization in LLMs: HijackNet’s Approach to Robustness and Defense Evasion**

2025 · 2025 4th International Symposium on Computer Applications and Information Technology (ISCAIT) · conference-paper · en · https://doi.org/10.1109/iscait64916.2025.11010431

This paper introduces HijackNet, an adversarial prompt hijacking framework designed to improve hijacking success rates and generalization in multi-lingual tasks. Combining Neural Architecture Search (NAS), Reinforcement Learning (RL), and Multi-Objective Optimization (MOO), HijackNet generates adversarial prompts that adapt to target tasks while bypassing model defense mechanisms. This framework optimizes hijacking success, defense evasion, and task completion through a combination of a prompt generator and adversarial optimizer. We introduce a Defense Robustness Score (DRS) to evaluate the stability of prompts in adversarial settings. HijackNet improves adversarial prompt generation, advancing the security and robustness of large language models in adversarial environments.

**Решение:** -4 HijackNet: adversarial prompt optimization framework

---

### 824 · R2518

**Leveraging Large Language Models to Extract Prognostic Pathology Features in Ewing Sarcoma.**

2026 · bioRxiv : the preprint server for biology · journal article, preprint, journalarticle · eng · https://doi.org/10.64898/2026.02.20.707103

Background Current risk stratification for Ewing sarcoma relies heavily on clinical factors such as metastatic status, failing to capture histologic heterogeneity as a potential prognostic indicator. Although pathology reports contain rich biological data, this information remains locked in unstructured narrative text, limiting large-scale retrospective analyses. We aimed to validate the utility of Large Language Models (LLMs) for scalable data abstraction and to identify prognostic histologic features from a large multi-institutional cohort. Methods We conducted a retrospective cohort study using data from six Children’s Oncology Group (COG) clinical trials. We utilized an LLM-based pipeline (OpenAI o3) to extract structured variables—including immunohistochemical (IHC) markers and CD99 staining patterns—from digitized, Optical Character Recognition (OCR)-processed pathology reports. Extraction accuracy was validated against a human-annotated ground truth (n=200) and cross-validated against senior experts (n=48). We assessed the association between extracted features and Overall Survival (OS) using Kaplan-Meier analysis and multivariable Cox proportional hazards regression, adjusting for metastatic status. Findings We analyzed 931 diagnostic pathology reports from 185 institutions spanning over 21-years. The LLM achieved a weighted average accuracy of 94% across 17 IHC markers; in a cross-validation subset, the LLM outperformed human annotators (weighted average accuracy over 15 IHC markers: LLM o3: 98.1%, a pediatric resident 91.4%, and a pediatric oncologist 95.9%). Survival analysis identified Neuron-Specific Enolase (NSE) and S100 as significant prognostic biomarkers. After adjusting for metastatic status, NSE positivity was associated with significantly inferior survival (HR 2.15, 95% CI 1.15–4.02, p=0.016); this risk was most pronounced in patients with non-metastatic disease (HR 5.64, p=0.0055). Conversely, S100 positivity was associated with improved survival (HR 0.58, 95% CI 0.34–1.00, p=0.046). Interpretation LLM-assisted extraction of pathology variables is highly accurate and scalable, capable of unlocking “dark data” from historical clinical trials. We identified NSE as a potent risk factor and S100 as a protective marker in Ewing sarcoma, particularly in localized disease. These findings suggest that AI-derived histologic data can refine risk stratification and, if validated, warrant inclusion in future prospective trials. Research in Context Evidence before this study We searched PubMed and Google Scholar for articles published up to December 2025, using terms such as “Ewing sarcoma”, “prognosis”, “risk stratification”, “large language models”, “natural language processing”, and “pathology report extraction”. Current risk stratification for Ewing sarcoma relies predominantly on clinical variables, specifically the presence of metastatic disease and tumor size. While histologic heterogeneity is well-documented, it is rarely incorporated into risk models because extracting structured data from narrative pathology reports is labor-intensive. Small, single-institution studies have suggested potential prognostic roles for markers like Neuron-Specific Enolase (NSE) or S100, but results have been inconsistent and limited by small sample sizes. Furthermore, while Large Language Models (LLMs) have demonstrated potential for extracting clinical data, their application to “rescue” data from legacy, multi-institutional clinical trial documents (scanned PDF images) for rare disease biomarker discovery has not been validated at scale. Added value of this study To our knowledge, this is the largest study to utilize AI to extract histologic data from Ewing sarcoma pathology reports, aggregating 931 patients from six distinct Children’s Oncology Group (COG) clinical trials spanning over 21 years. We validated an LLM-based pipeline that converted noisy, optically character-recognized text from diverse institutions into structured data with 98.1% accuracy, outperforming human annotators. This scalable approach revealed that NSE positivity is a significant independent risk factor for mortality (HR=2.15), particularly in patients with non-metastatic disease where it confers a more than 5-fold increased risk of death. Conversely, we identified S100 positivity as a protective factor associated with improved survival (HR=0.58). Implications of all the available evidence This study demonstrates that LLMs can reliably unlock “dark data” from historical clinical trials, rendering vast archives of unstructured medical documents accessible for retrospective analysis. The identification of NSE and S100 as robust prognostic biomarkers suggests that these widely available immunohistochemical stains provide valuable information beyond standard diagnostic information. These findings support the integration of automated data extraction tools in research workflows and suggest that NSE and S100 status should be considered in the design of future risk-stratified clinical trials for Ewing sarcoma.

**Решение:** -4 pathology features extraction in Ewing sarcoma (somatic oncology)

---

### 825 · R2643

**VidMsg: A Benchmark for Implicit Message Inference in Short Videos**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.03635

Understanding short online videos involves more than identifying visible objects and actions; video makers often include an underlying message or purpose in the clip. We introduce VidMsg, a benchmark for evaluating implicit message understanding in short, internet-native video clips. VidMsg contains 400 YouTube-derived clips across 9 practical topic areas and 52 fine-grained target messages, covering domains such as career and finance, education, health and well-being, culture, safety, sustainability, and lifestyle. VidMsg is constructed through a message-first pipeline: an LLM first translates target messages into indirect search scenarios, which are used to retrieve candidate clips. Human annotators then retain clips that convey the intended message without being overly explicit. VidMsg is designed primarily for bidirectional message-clip retrieval for scalable applications such as video search and recommendation, where systems must capture holistic video understanding. In addition to retrieval, VidMsg includes a diagnostic multiple-choice QA benchmark, where models select the intended message of a clip from semantically related alternatives. Experiments with contemporary video-language and retrieval models show that strong models often fail on VidMsg, because the task requires pragmatic inference, integration of contextual cues, and discrimination among semantically close messages. We also introduce VidVec-Msg, a baseline method that improves message-oriented retrieval while leaving substantial headroom for future work. Project page: https://iyttor.github.io/VidMsg

**Решение:** -4 VidMsg: implicit message inference benchmark in short videos

---

### 826 · R7258

**NarraDetect: An annotated dataset for the task of narrative detection**

2025 · Underline Science Inc. · audiovisual/conference talk, conference-paper · en · https://doi.org/10.18653/v1/2025.wnu-1.1

Narrative detection is an important task across diverse research domains where storytelling serves as a key mechanism for explaining human beliefs and behavior. However, the task faces three significant challenges: (1) inter-narrative heterogeneity, or the variation in narrative communication across social contexts; (2) intra-narrative heterogeneity, or the dynamic variation of narrative features within a single text over time; and (3) the lack of theoretical consensus regarding the concept of narrative. This paper introduces the NarraDetect dataset, a comprehensive resource comprising over 13,000 passages from 18 distinct narrative and non-narrative genres. Through a manually annotated subset of ~400 passages, we also introduce a novel theoretical framework for annotating for a scalar concept of "narrativity.'' Our findings indicate that while supervised models outperform large language models (LLMs) on this dataset, LLMs exhibit stronger generalization and alignment with the scalar concept of narrativity.

**Решение:** -4 NarraDetect: dataset for scalar concept of narrativity across genres

---

### 827 · R6735

**Self-reflection in Automated Qualitative Coding: Improving Text Annotation through Secondary LLM Critique**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.09905

Large language models (LLMs) allow for sophisticated qualitative coding of large datasets, but zero- and few-shot classifiers can produce an intolerable number of errors, even with careful, validated prompting. We present a simple, generalizable two-stage workflow: an LLM applies a human-designed, LLM-adapted codebook; a secondary LLM critic performs self-reflection on each positive label by re-reading the source text alongside the first model's rationale and issuing a final decision. We evaluate this approach on six qualitative codes over 3,000 high-content emails from Apache Software Foundation project evaluation discussions. Our human-derived audit of 360 positive annotations (60 passages by six codes) found that the first-line LLM had a false-positive rate of 8% to 54%, despite F1 scores of 0.74 and 1.00 in testing. Subsequent recoding of all stage-one annotations via a second self-reflection stage improved F1 by 0.04 to 0.25, bringing two especially poor performing codes up to 0.69 and 0.79 from 0.52 and 0.55 respectively. Our manual evaluation identified two recurrent error classes: misinterpretation (violations of code definitions) and meta-discussion (debate about a project evaluation criterion mistaken for its use as a decision justification). Code-specific critic clauses addressing observed failure modes were especially effective with testing and refinement, replicating the codebook-adaption process for LLM interpretation in stage-one. We explain how favoring recall in first-line LLM annotation combined with secondary critique delivers precision-first, compute-light control. With human guidance and validation, self-reflection slots into existing LLM-assisted annotation pipelines to reduce noise and potentially salvage unusable classifiers.

**Решение:** -4 qualitative coding of Apache software engineering emails

---

### 828 · R7223

**Exploring the Capacity of Large Language Models to Assess the Chronic Pain Experience: Algorithm Development and Validation.**

2025 · Journal of medical Internet research · journal article, validation study, journalarticle · eng · https://doi.org/10.2196/65903

BACKGROUND: Chronic pain, affecting more than 20% of the global population, has an enormous pernicious impact on individuals as well as economic ramifications at both the health and social levels. Accordingly, tools that enhance pain assessment can considerably impact people suffering from pain and society at large. In this context, assessment methods based on individuals' personal experiences, such as written narratives (WNs), offer relevant insights into understanding pain from a personal perspective. This approach can uncover subjective, intricate, and multifaceted aspects that standardized questionnaires can overlook. However, WNs can be time-consuming for clinicians. Therefore, a tool that uses WNs while reducing the time required for their evaluation could have a significantly beneficial impact on people's pain assessment. OBJECTIVE: This study is the first evaluation of the potential of applying large language models (LLMs) to assist clinicians in assessing patients' pain expressed through WNs. METHODS: We performed an experiment based on 43 WNs made by people with fibromyalgia and qualitatively evaluated in a prior study. Focusing on pain severity and disability, we prompt GPT-4 (with temperature parameter settings 0 or 1) to assign scores and scores' explanations, to these WNs. Then, we quantitatively compare GPT-4 scores with experts' scores of the same narratives, using statistical measures such as Pearson correlations, root mean squared error, the weighted version of the Gwet agreement coefficient, and Krippendorff α. Additionally, 2 experts specialized in chronic pain conducted a qualitative analysis of the scores' explanation to assess their accuracy and potential applicability of GPT's analysis for future pain narrative evaluations. RESULTS: Our analysis reveals that GPT-4's performance in assessing pain narratives yielded promising results. GPT-4 was comparable in terms of agreement with experts (with a weighted percentage agreement higher than 0.95), correlations with standardized measurements (for example in the range of 0.43 and 0.49 between the Revised Fibromyalgia Impact Questionnaire and GTP-4 with temperatures 1), and low error rates (root mean squared error of 1.20 for severity and 1.44 for disability). Moreover, experts generally deemed the ratings provided by GPT-4, as well as the scores' explanation, to be adequate. However, we observe that GPT has a slight tendency to overestimate pain severity and disability with a lower SD than expert estimates. CONCLUSIONS: These findings underline the potential of LLMs in facilitating the assessment of WNs of people with fibromyalgia, offering a novel approach to understanding and evaluating patient pain experiences. Integrating automated assessments through LLMs presents opportunities for streamlining and enhancing the assessment process, paving the way for improved patient care and tailored interventions in the chronic pain management field.

**Решение:** + T3/T1 GPT-4 scoring of fibromyalgia written narratives for pain severity and disability vs expert ratings (Krippendorff alpha, Gwet AC, JMIR 2025)

---

### 829 · R3268

**Virtual jury, real anxiety: Effects of Large Language Model on multimodal anxiety responses to a Trier Social Stress Test in Virtual Reality**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6935095

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T3 TSST VR anxiety responses with LLM virtual jury; no abstract, eligible on full text

---

### 830 · R5519

**Simulated souls: investigating the emotional fallacy in large language models**

2026 · AI and Ethics · article · en · https://doi.org/10.1007/s43681-026-01100-8

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 critique on emotional fallacy in large language models

---

### 831 · R5350

**LinguIUTics at PsyDefDetect: Iterative Imbalance-Aware Fine-tuning of Qwen3-8B for Psychological Defense Mechanism Classification**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, conference-paper · https://doi.org/10.48550/arxiv.2606.00647

Detecting psychological defense mechanisms in conversational text remains a challenging clinical NLP problem. For the PsyDefDetect 2026 shared task (nine-class utterance classification evaluated via macro F1), our team LinguIUTics achieves a macro F1-score of 0.3917 on the official positive-class leaderboard, ranking 4th out of 21 registered teams and improving over the Ministral-8B task baseline (31.48 macro F1) by 7.7 absolute points (24.4 percent relative). BERT-family encoders and zero-shot LLMs proved ineffective on rare classes due to severe class imbalance, leading us to QLoRA fine-tuning of Qwen3-8B. We leverage three key strategies: grouped stratified cross-validation (preventing leakage), minority-class round-robin lexical augmentation, and a post-processing pipeline with logit bias tuning and ensemble blending. Together, these components close much of the validation-to-leaderboard gap and substantially improve minority-class recall, driving the critical "Unclear" class (Level 8) from near-zero performance to an F1 score of 0.797. Accepted at PsyDefDetect, a shared task at the 25th BioNLP Workshop (BioNLP 2026), co-located with ACL 2026 in San Diego, CA, USA

**Решение:** + T1 psychological defense mechanism classification in conversational text using Qwen3-8B vs gold human labels in PsyDefDetect 2026 (BioNLP 2026)

---

### 832 · R11245

**Large language model doctor: assessing the ability of ChatGPT-4 to deliver interventional radiology procedural information to patients during the consent process.**

2024 · CVIR endovascular · journal article, journalarticle, review · eng · https://doi.org/10.1186/s42155-024-00477-z

PURPOSE: The study aims to evaluate how current interventional radiologists view ChatGPT in the context of informed consent for interventional radiology (IR) procedures. METHODS: ChatGPT-4 was instructed to outline the risks, benefits, and alternatives for IR procedures. The outputs were reviewed by IR physicians to assess if outputs were 1) accurate, 2) comprehensive, 3) easy to understand, 4) written in a conversational tone, and 5) if they were comfortable providing the output to the patient. For each criterion, outputs were measured on a 5-point scale. Mean scores and percentage of physicians rating output as sufficient (4 or 5 on 5-point scale) were measured. A linear regression correlated mean rating with number of years in practice. Intraclass correlation coefficient (ICC) measured agreement among physicians. RESULTS: The mean rating of the ChatGPT responses was 4.29, 3.85, 4.15, 4.24, 3.82 for accuracy, comprehensiveness, readability, conversational tone, and physician comfort level, respectively. Percentage of physicians rating outputs as sufficient was 84%, 71%, 85%, 85%, and 67% for accuracy, comprehensiveness, readability, conversational tone, and physician comfort level, respectively. There was an inverse relationship between years in training and output score (coeff = -0.03413, p = 0.0128); ICC measured 0.39 (p = 0.003). CONCLUSIONS: GPT-4 produced outputs that were accurate, understandable, and in a conversational tone. However, GPT-4 had a decreased capacity to produce a comprehensive output leading some physicians to be uncomfortable providing the output to patients. Practicing IRs should be aware of these limitations when counseling patients as ChatGPT-4 continues to develop into a clinically usable AI tool.

**Решение:** -4 ChatGPT-4 delivering interventional radiology information

---

### 833 · R6035

**An Analytical Study on the Use of Artificial Intelligence in Measuring Human Intelligence**

2026 · Zenodo (CERN European Organization for Nuclear Research) · journal/, other · ang · https://doi.org/10.5281/zenodo.22981475

Purpose: This study explores how Artificial Intelligence (AI) has emerged as a tool for measuring human intelligence and ascertains whether the AI-based methods in measurement can supplement, enhance or substitute psychometric evaluation in any way. The study will also explore how the fields of psychometrics and AI are converging, highlight the essential AI-based methods in intelligence assessment, point out their strengths and weaknesses, and discuss the issues of fairness, impartiality, validation, and responsibility in relation to them. Method/Approach: The research employs a qualitative, theoretical, and interpretative methodology that draws on the narrative-thematic assessment of secondary literature sources. The pertinent articles from peer-reviewed articles and preprints along with institutional reports were subjected to thematic content analysis. The literature was categorised into theme groups as follows: classical psychometric principles, AI-based computerised adaptive testing, brain imaging-based prediction, behaviour and multi-modal signal analysis, AI processes used in the human intelligence tests, and issues of fairness and ethics. Results/Findings: The results indicate that AI has been shown to be the most effective tool for enhancing the efficiency and accuracy of standard intelligence testing methods in terms of computerized adaptive testing and automated scoring. Methods based on neuroimaging provide predictions about intelligence that are statistically weak but scientifically valid; behavioral methods such as eye-tracking have proven to be promising but may require substantial resources to be applied effectively. Yet, there is no single AI method that can provide full construct validity, standardization and reliability, and fairness as compared to conventional intelligence tests administered by humans. Moreover, these results once again bring to light issues of algorithmic bias, consent, transparency, and instability of responses in generative AI methods. Originality/Value: This research offers a coherent framework for comparing research studies on different aspects of AI in psychometrics, adaptive testing, neuroimaging, behavioral inference, and evaluation of AI technology. It presents a hybrid assessment model involving AI in adaptive delivery, scoring, and signal extraction while allowing qualified professionals to stay in charge of interpreting results and ensuring ethical integrity. Type of Paper: Exploratory Research.

**Решение:** -1 exploratory study on AI in psychometrics and intelligence measurement

---

### 834 · R2031

**Hybrid IndoBERT and Support Vector Machine for Multi-class Emotion Classification of Indonesian Tourism Reviews**

2026 · Media Jurnal Informatika · journalarticle, review, article · https://doi.org/10.35194/mji.v18i1.6377

Online reviews hold emotional nuances that binary sentiment analysis cannot adequately capture for targeted tourism management. Indonesian reviews pose additional computational challenges due to informal language, Sundanese vernacular, and severe class imbalance. Objective: This study develops a hybrid classification framework using IndoBERT as a frozen feature extractor and a Support Vector Machine (SVM) across five emotional classes. It investigates integrating Principal Component Analysis (PCA) and SMOTE within a strict cross-validation pipeline to mitigate extreme minority class scarcity while preventing data leakage. The duplicate-free dataset comprises 446 manually annotated reviews from agro-tourism destinations in Rancakalong. Annotations followed Ekman’s emotions plus a neutral category, cross-validated by a Large Language Model (Cohen's Kappa = 0.7475). To satisfy oversampling constraints, three extreme minority classes (fear, surprise, disgust) were consolidated into an 'OTHER' class. Three configurations were evaluated via 5-Fold Stratified Cross-Validation: TF-IDF + SVM (M1 baseline), IndoBERT + SVM (M2), and IndoBERT + PCA + SMOTE + SVM (M3), utilizing Macro F1 as the primary metric. Results: The M1 baseline yielded a Macro F1 of 0.3920. By capturing contextual semantics, M2 improved accuracy to 0.7131 and Macro F1 to 0.4133. The proposed M3 architecture achieved the highest Macro F1 (0.4321), demonstrating that combining dimensionality reduction and oversampling strengthens minority class decision boundaries. However, erratic performance on the synthetic 'OTHER' class confirms that merging distinct emotions disrupts cohesive semantic signatures. Integrating frozen IndoBERT embeddings with PCA and SMOTE within a cross-validated SVM architecture significantly outperforms traditional baseline models on highly imbalanced, low-resource Indonesian text data. This study contributes an empirically validated emotion corpus and establishes a foundational, data-driven behavioral modeling framework to guide targeted managerial interventions in local agro-tourism.

**Решение:** -4 hybrid IndoBERT and SVM for emotion classification of Indonesian tourism reviews

---

### 835 · R12383

**Advancing Qualitative Analysis: An Exploration of the Potential of Generative AI and NLP in Thematic Coding**

2023 · Elsevier BV · posted-content, preprint · en · https://doi.org/10.2139/ssrn.4487768

Background: Traditional manual coding in qualitative data analysis can be labor-intensive and time-consuming, especially with large data sets. This research investigates the potential use of natural language processing (NLP) techniques and large language models (LLMs), such as GPT-3.5, to enhance efficiency and depth of insights during the qualitative data coding process.&lt;br&gt;&lt;br&gt;Method: We compared traditional manual thematic analysis with two NLP-assisted approaches, NLP Cluster Assisted (NLPCA) and NLP with GPT-3.5 (NLPGPT), using a dataset of 3,800 student responses on “exam wrappers” from an engineering physics course. Exam wrappers are structured reflection activities that prompt students to practice self-reflection after they get their graded exams back. Agreement between the methods was evaluated based on the similarity of the generated codes.&lt;br&gt;&lt;br&gt;Results: Both NLPCA and NLPGPT effectively identified similar themes in the student responses, demonstrating a promising alternative to traditional qualitative coding. Notably, the GPT-3.5 model exhibited strength in producing highly granular codes, which could offer deeper and more nuanced insights.&lt;br&gt;&lt;br&gt;Discussion: The results of the study underscore the significant benefits of integrating NLP and LLMs into qualitative research. While the study identified challenges such as biases in language models, overfitting in terms of overly granular codes, and resource constraints, the findings suggest these hurdles can be addressed with further research and refinement of the methodology. The application of NLP and LLMs across various research contexts needs validation, setting a promising direction for future studies. This research marks an important stepping stone in enhancing traditional qualitative research with AI technology, paving the way for more scalable, robust, and efficient research methodologies.

**Решение:** -4 thematic coding of engineering physics exam wrapper reflections

---

### 836 · R12372

**Automated Claim Matching with Large Language Models: Empowering Fact-Checkers in the Fight Against Misinformation**

2023 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.4614239

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 automated claim matching for fact-checkers (misinformation)

---

### 837 · R8241

**Facial Analysis for Plastic Surgery in the Era of Artificial Intelligence: A Comparative Evaluation of Multimodal Large Language Models.**

2025 · Journal of clinical medicine · journal article, journalarticle, article · eng · https://doi.org/10.3390/jcm14103484

Background/Objectives: Facial analysis is critical for preoperative planning in facial plastic surgery, but traditional methods can be time consuming and subjective. This study investigated the potential of Artificial Intelligence (AI) for objective and efficient facial analysis in plastic surgery, with a specific focus on Multimodal Large Language Models (MLLMs). We evaluated their ability to analyze facial skin quality, volume, symmetry, and adherence to aesthetic standards such as neoclassical facial canons and the golden ratio. Methods: We evaluated four MLLMs&mdash;ChatGPT-4o, ChatGPT-4, Gemini 1.5 Pro, and Claude 3.5 Sonnet&mdash;using two evaluation forms and 15 diverse facial images generated by a Generative Adversarial Network (GAN). The general analysis form evaluated qualitative skin features (texture, type, thickness, wrinkling, photoaging, and overall symmetry). The facial ratios form assessed quantitative structural proportions, including division into equal fifths, adherence to the rule of thirds, and compatibility with the golden ratio. MLLM assessments were compared with evaluations from a plastic surgeon and manual measurements of facial ratios. Results: The MLLMs showed promise in analyzing qualitative features, but they struggled with precise quantitative measurements of facial ratios. Mean accuracy for general analysis were ChatGPT-4o (0.61 &plusmn; 0.49), Gemini 1.5 Pro (0.60 &plusmn; 0.49), ChatGPT-4 (0.57 &plusmn; 0.50), and Claude 3.5 Sonnet (0.52 &plusmn; 0.50). In facial ratio assessments, scores were lower, with Gemini 1.5 Pro achieving the highest mean accuracy (0.39 &plusmn; 0.49). Inter-rater reliability, based on Cohen&rsquo;s Kappa values, ranged from poor to high for qualitative assessments (&kappa; &gt; 0.7 for some questions) but was generally poor (near or below zero) for quantitative assessments. Conclusions: Current general purpose MLLMs are not yet ready to replace manual clinical assessments but may assist in general facial feature analysis. These findings are based on testing models not specifically trained for facial analysis and serve to raise awareness among clinicians regarding the current capabilities and inherent limitations of readily available MLLMs in this specialized domain. This limitation may stem from challenges with spatial reasoning and fine-grained detail extraction, which are inherent limitations of current MLLMs. Future research should focus on enhancing the numerical accuracy and reliability of MLLMs for broader application in plastic surgery, potentially through improved training methods and integration with other AI technologies such as specialized computer vision algorithms for precise landmark detection and measurement

**Решение:** -4 facial analysis for plastic surgery

---

### 838 · R6134

**Performance Evaluation of Large Language Models in Real-World Perinatal Medication Consultations: A Cross-Sectional Study**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-8696873/v1

Abstract Introduction Perinatal medication consultation is a core clinical pharmacy service that involves a complex benefit–risk assessment for both maternal and fetal safety. Large language models (LLMs) have emerged as potential tools to improve access to medication information, yet their performance and safety in real-world, pharmacist-led perinatal consultation settings, particularly in non-English contexts, remain insufficiently evaluated. Aim To evaluate and compare the performance of multiple advanced large language models in addressing real-world Chinese perinatal medication consultation queries and to assess their potential role as supervised adjunctive tools within clinical pharmacy services. Method This cross-sectional study evaluated seven LLMs using real-world clinical data from pharmacist-led medication consultations at the Pharmacy Clinic of the Beijing Obstetrics and Gynecology Hospital, Capital Medical University. A standardized test set of 64 perinatal medication consultation questions was developed from 15,280 electronic consultation records collected between April 2014 and April 2024. The evaluated models included international (GPT-5.1, Grok 3, Gemini 3.0) and domestic (DeepSeek, Wenxin Yiyan, Kimi K2, Tongyi Qianwen) models. Senior clinical pharmacologists independently assessed responses across four dimensions—relevance, accuracy, usefulness, and empathy—using a 10-point Likert scale. The results are summarized as mean ± SD, and between-model differences were analyzed using non-parametric statistical tests. Results Among the 448 model-generated responses, inter-rater consistency was excellent (ICC = 0.91, 95% CI 0.88–0.94). Significant differences in the overall performance were observed among the models (p Conclusion LLMs have demonstrated variable performance in response to perinatal medication consultation queries. While high-performing models show the potential to support pharmacist-led perinatal medication consultations by improving access to information, their current performance supports use only as supervised, adjunctive decision-support tools, rather than as independent sources of medication counseling. Careful governance, human oversight, and further validation of safety and reliability are required before broader integration into perinatal clinical pharmacy practices.

**Решение:** -4 performance evaluation of LLMs in perinatal medication consultations

---

### 839 · R12433

**Using Large Language Models for Qualitative Analysis can Introduce Serious Bias**

2023 · World Bank policy research working paper · preprint/article, preprint, report · en · https://doi.org/10.1596/1813-9450-10597

Large Language Models (LLMs) are quickly becoming ubiquitous, but the implications for social science research are not yet well understood. This paper asks whether LLMs can help us analyse large-N qualitative data from open-ended interviews, with an application to transcripts of interviews with displaced Rohingya people in Cox’s Bazaar, Bangladesh. The analysis finds that a great deal of caution is needed in using LLMs to annotate text as there is a risk of introducing biases that can lead to misleading inferences. Here this refers to bias in the technical sense, that the errors that LLMs make in annotating interview transcripts are not random with respect to the characteristics of the interview subjects. Training simpler supervised models on high-quality human annotations with flexible coding leads to less measurement error and bias than LLM annotations. Therefore, given that some high quality annotations are necessary in order to asses whether an LLM introduces bias, this paper argues that it is probably preferable to train a bespoke model on these annotations than it is to use an LLM for annotation.

**Решение:** -4 qualitative analysis of refugee interview transcripts from Bangladesh

---

### 840 · R7284

**A comprehensive survey on large language models for multimedia data security: challenges and solutions**

2025 · Computer Networks · article · en · https://doi.org/10.1016/j.comnet.2025.111379

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 comprehensive survey on LLMs for multimedia data security

---

### 841 · R10594

**SceneTAP: Scene-Coherent Typographic Adversarial Planner against Vision-Language Models in Real-World Environments**

2025 · IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings - IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/cvpr52734.2025.02332

Large vision-language models (LVLMs) have shown remarkable capabilities in interpreting visual content. While existing works demonstrate these models’ vulnerability to deliberately placed adversarial texts, such texts are often easily identifiable as anomalous. In this paper, we present the first approach to generate scene-coherent typographic adversarial attacks that mislead advanced LVLMs while maintaining visual naturalness through the capability of the LLM-based agent. Our approach addresses three critical questions: what adversarial text to generate, where to place it within the scene, and how to integrate it seamlessly. We propose a training-free, multi-modal LLM-driven scene-coherent typographic adversarial planning (SceneTAP) that employs a three-stage process: scene understanding, adversarial planning, and seamless integration. The SceneTAP utilizes chain-of-thought reasoning to comprehend the scene, formulate effective adversarial text, strategically plan its placement, and provide detailed instructions for natural integration within the image. This is followed by a scene-coherent TextDiffuser that executes the attack using a local diffusion mechanism. We extend our method to real-world scenarios by printing and placing generated patches in physical environments, demonstrating its practical implications. Extensive experiments show that our scene-coherent adversarial text successfully misleads state-of-the-art LVLMs, including ChatGPT-4o, even after capturing new images of physical setups. Our evaluations demonstrate a significant increase in attack success rates while maintaining visual naturalness and contextual appropriateness. This work highlights vulnerabilities in current vision-language models to sophisticated, scene-coherent adversarial attacks and provides insights into potential defense mechanisms. We release our code at https://github.com/tsingqguo/scenetap.

**Решение:** -4 SceneTAP: typographic adversarial attacks on vision-language models

---

### 842 · R10760

**Evaluating AI-Generated Distractors in Programming Education: A Human-AI Collaborative Approach**

2025 · International Computing Education Research Workshop · book, journalarticle · https://doi.org/10.1145/3702653.3744332

Multiple-choice questions (MCQs) serve as fundamental assessment tools in computing education, where high-quality distractors are critical for evaluating conceptual understanding and debugging skills. While large language models (LLMs) show promise in automating distractor generation, their effectiveness in reasoning-intensive programming domains remains understudied. Another challenge is that current evaluation metrics often emphasize surface-level semantics rather than the logical reasoning required in programming tasks, limiting their practical utility for educators. To compare AI-generated and human-authored distractors, this study collected 925 MCQs from two online high school courses. The collected data include the question stem, correct answer, and three human-authored distractors for each question. For AI-generated distractor generation, we employed the GPT-4 API through a structured prompt containing: (1) question stem, (2) correct answer, (3) Bloom’s taxonomy level, and (4) instructional constraints. To determine the Bloom’s taxonomy level for each question, two assessment experts independently classified all questions based on Bloom’s taxonomy (Remember, Understand, Apply, Analyze, Evaluate, Create), achieving moderate inter-rater reliability (Cohen’s K = 0.67). Discrepancies, which occurred in 33% of cases, were resolved by a third expert to ensure accurate cognitive-level categorization. The GPT-4 model generated three plausible distractors per question while maintaining cognitive-level alignment. This study proposes a human–AI collaborative framework to evaluate distractor quality in programming education. Our human–AI collaborative evaluation framework combined human expertise with AI analysis (using GPT-4 and DeepSeek-V3) through a three-phase process: First, human-created and AI-generated distractors were anonymized and randomized. Next, human experts and AI models independently selected the three most pedagogically effective distractors per question based on plausibility and challenge potential. Finally, we implemented a ranking system prioritizing distractors with the highest selection frequency across evaluators, with ties resolved by cross-validator agreement. Results demonstrate that AI-generated distractors achieve comparable quality to human-crafted ones for foundational programming concepts (e.g., syntax recall and basic logic). However, significant gaps emerge in higher-order cognitive domains, particularly in questions requiring code behavior analysis (35% lower selection rate by human evaluators) or solution evaluation (42% lower). Qualitative analysis reveals AI’s tendency to produce superficially plausible but pedagogically weaker distractors for complex reasoning tasks, often missing subtle misconceptions that human instructors capture. This work makes three key contributions: (1) a validated framework for evaluating programming distractors across cognitive levels, (2) empirical evidence of LLM capabilities and limitations in reasoning-intensive question types, and (3) practical guidelines for integrating AI in MCQ design—particularly recommending human oversight for higher-order questions. Our findings equip educators with evidence-based strategies to leverage AI while maintaining assessment rigor, especially in introductory programming courses where misconception targeting is crucial. Future research will investigate how contextual learner modeling can support more personalized and pedagogically aligned distractor generation.

**Решение:** -4 evaluating AI-generated distractors in programming education

---

### 843 · R6970

**Impact of Query Language on Large Language Model Performance in Dental Trauma Management: A Comparative Evaluation of ChatGPT, Gemini, and Claude**

2026 · Research Square · preprint, ppr, posted-content · https://doi.org/10.21203/rs.3.rs-8754479/v1

Abstract Background Large language models (LLMs) are increasingly used as clinical decision support tools in healthcare, yet the impact of query language on their performance remains unclear, particularly in specialized domains like dental traumatology. This study evaluated whether LLM performance in dental trauma management differs based on the language of clinical scenarios (English vs. Turkish) and compared performance across three AI models. Methods Twenty-seven clinical scenarios covering 13 dental trauma categories were presented to ChatGPT 5.2, Gemini 3.0, and Claude 4.5 Sonnet in both English and Turkish, generating 162 responses. Two blinded endodontists independently evaluated responses using a standardized rubric assessing accuracy (40%), completeness (35%), and safety (25%) against IADT 2020 Guidelines. Inter-rater reliability was assessed using intraclass correlation coefficient (ICC). Language effects were analyzed using Wilcoxon signed-rank tests; model comparisons employed Kruskal-Wallis and Mann-Whitney U tests with Bonferroni correction. Results Inter-rater reliability was good across all dimensions (ICC: 0.738–0.836). ChatGPT showed the strongest language effect with 9.14% higher performance in English (p &lt; 0.001, r = 0.874). Gemini showed moderate English advantage (5.69%, p = 0.003, r = 0.572). Claude exhibited language independence with virtually identical performance in both languages (-0.02%, p = 0.220). In English, significant model differences emerged (H = 22.31, p &lt; 0.001); however, model performance converged in Turkish (H = 2.89, p = 0.236). Conclusions Language-dependent performance variations in LLMs are model-specific rather than universal. While ChatGPT achieved highest absolute scores, Claude’s language independence may offer more reliable performance in non-English clinical settings. These findings have implications for deployment of AI in multilingual healthcare environments.

**Решение:** -4 query language impact on LLM performance in dental trauma

---

### 844 · R4859

**A Comprehensive Investigation of Empathetic Dialogue Systems for Mental Health Support Using Large Language Models**

2026 · Springer Link (Chiba Institute of Technology) · article · en · https://doi.org/10.1051/shsconf/202623504010/pdf

Mental health issues are a crisis for the world, with one out of eight individuals in low-income countries with a disorder experiencing treatment gaps. This paper presents a detailed overview of how Large Language Models (LLMs) and the Transformer architecture can address these problems. The development of conversational agents as rule-based systems to advanced models, which apply Cognitive-behavioral Therapy (CBT) in minimizing anxiety and depression, is examined. The review also looks at the use of LLMs in clinical screening such as multimodal depression and suicide risk. However, existing systems have enormous challenges despite the possibility of mental health assistance, such as “feigned empathy,” hallucinations, and relying on unimodal inputs using texts. To address these limitations that exist, a multimodal emotion-aware architecture, which pays attention to memory-enhanced personalization and emotion-specific reinforcement learning, is introduced. Finally, this review recommends hybrid human-AI approaches, which focus on safety and empathetic conversation to improve current mental health systems.

**Решение:** -1 review of empathetic dialogue systems for mental health support

---

### 845 · R9912

**Expert Opinion Independent Evaluation Letters and Generative AI in EB1A EB-2 NIW Petitions: A Tutorial for DIYs and Paralegals**

2025 · RSPUBLICATION · journalarticle/ · https://doi.org/10.5281/zenodo.15615554

ABSTRACT This paper provides a comprehensive guide on crafting effective expert opinion letters for EB- 2 National Interest Waiver (NIW) petitions. We examine the key components, structure, and best practices for creating persuasive letters that align with USCIS requirements. The study synthesizes recommendations from immigration experts, legal practitioners, and reported petition experiences to develop a practical framework for writing compelling expert letters that support claims of exceptional ability and national importance. Our analysis highlights essential elements that tend to distinguish stronger letters and includes templates to guide applicants and their recommenders. This paper also outlines a framework for integrating generative AI in the drafting of EB-2 NIW expert opinion letters, particularly in contexts where Requests for Evidence (RFEs) are raised. It explores the interaction between USCIS adjudication standards and AI-supported writing workflows, with reference to the three-prong Dhanasar standard. The discussion includes qualitative assessments of tools such as GPT-4, Claude 3, and LegalBERT in enhancing the clarity, organization, and relevance of letter content—especially with regard to technical merit, national impact, and justification for the waiver. Case illustrations and workflow diagrams are used to identify practices that promote effective collaboration between human experts and AI tools, including strategies for minimizing AI errors, maintaining confidentiality, and validating content accuracy. The paper emphasizes ethical considerations, underscoring that while AI can improve consistency and streamline drafting processes, it cannot replace the nuanced judgment of independent experts. Drawing on a curated set of petition case examples and practitioner input, this work offers practical guidance for legal professionals adapting to the evolving landscape of immigration documentation. This paper explores the integration of generative AI in drafting expert opinion letters for EB-2 National Interest Waiver (NIW) petitions. We present a systematic workflow diagram and analyze how large language models (LLMs) can enhance the quality, consistency, and efficiency of letter preparation while maintaining compliance with USCIS requirements. Our findings demonstrate that AI-assisted drafting can reduce costs by 40-60% while improving the persuasive power of recommendation letters through data-driven customization. This is pure review paper and results cited are from the links. We did not do any field work in this paper. All results, findings and data from cited literature. Keywords: EB-2 NIW, expert opinion letter, Gen AI, LLM, Paralegal

**Решение:** -4 expert opinion letters for EB-2 NIW immigration petitions

---

### 846 · R11057

**Investigating the increase of violent speech in Incel communities with human-guided GPT-4 prompt iteration**

2024 · Frontiers in Social Psychology · journalarticle, article · en · https://doi.org/10.3389/frsps.2024.1383152

This study investigates the prevalence of violent language on incels.is. It evaluates GPT models (GPT-3.5 and GPT-4) for content analysis in social sciences, focusing on the impact of varying prompts and batch sizes on coding quality for the detection of violent speech. We scraped over 6.9M posts from incels.is and categorized a random sample into non-violent, explicitly violent, and implicitly violent content. Two human coders annotated 3, 028 posts, which we used to tune and evaluate GPT-3.5 and GPT-4 models across different prompts and batch sizes regarding coding reliability. The best-performing GPT-4 model annotated an additional 45, 611 posts for further analysis. We find that 21.91% of the posts on the forum contain some form of violent language. Within the overall forum, 18.12% of posts include explicit violence, while 3.79% feature implicit violence. Our results show a significant rise in violent speech on incels.is, both at the community and individual level. This trend is particularly pronounced among users with an active posting behavior that lasts for several hours up to one month. While the use of targeted violent language decreases, general violent language increases. Additionally, mentions of self-harm decline, especially for users who have been active on the site for over 2.5 years. We find substantial agreement between both human coders (κ = 0.65), while the best GPT-4 model yields good agreement with both human coders (κ = 0.54 for Human A and κ = 0.62 for Human B). Overall, this research offers effective ways to pinpoint violent language on a large scale, helping with content moderation and facilitating further research into causal mechanisms and potential mitigations of violent expression and online radicalization in communities like incels.is.

**Решение:** -4 detection of violent speech in online Incel community forum

---

### 847 · R11251

**Stealthy Jailbreak Attacks on Large Language Models via Benign Data Mirroring**

2024 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2410.21083

Large language model (LLM) safety is a critical issue, with numerous studies employing red team testing to enhance model security. Among these, jailbreak methods explore potential vulnerabilities by crafting malicious prompts that induce model outputs contrary to safety alignments. Existing black-box jailbreak methods often rely on model feedback, repeatedly submitting queries with detectable malicious instructions during the attack search process. Although these approaches are effective, the attacks may be intercepted by content moderators during the search process. We propose an improved transfer attack method that guides malicious prompt construction by locally training a mirror model of the target black-box model through benign data distillation. This method offers enhanced stealth, as it does not involve submitting identifiable malicious instructions to the target model during the search phase. Our approach achieved a maximum attack success rate of 92%, or a balanced value of 80% with an average of 1.5 detectable jailbreak queries per sample against GPT-3.5 Turbo on a subset of AdvBench. These results underscore the need for more robust defense mechanisms. Accepted by NAACL 2025

**Решение:** -4 stealthy jailbreak attacks on LLMs via benign data mirroring

---

### 848 · R2271

**How well do large language models mirror human cognition of word concepts?: A comparison of psychological ratings for early-acquired English words.**

2026 · Behavior research methods · comparative study, research-article, journal article · eng · https://doi.org/10.3758/s13428-025-02938-2

Abstract This study examined how well large language models (LLMs) approximate human psychological ratings for early-acquired English words. We used four state-of-the-art LLMs, including GPT-4o and Meta-Llama-3.1, to evaluate 21 static psychological features for 695 words and compared these estimates with human norms. The results showed that LLMs aligned well with human ratings for some features (e.g., Concreteness, Bodily Interactiveness) in terms of rank correlations ( r s &gt; .82) and distributional similarities but diverged notably for others (e.g., Iconicity, Arousal; r s &lt; .48). Compared with content words, function words showed more pronounced discrepancies between human and LLM ratings. We also assessed how similarly human- and LLM-derived psychological features predicted words’ age of acquisition (AoA), revealing both strong correspondences and systematic biases, depending on the model (differences in correlations ranged from −.27 to .28). Based on these analyses, we identified which features may be reliably estimated using LLMs, which require further refinement, and what methodological considerations are necessary for applying LLM-based measures in cognitive science. We discuss the implications of using LLMs as methodological tools in psychology and cognitive science, highlighting both their practical advantages (e.g., data coverage and data collection efficiency) and theoretical relevance. The present study provides a novel framework for evaluating the cognitive plausibility of LLMs by using lexical psychological features, complementing existing benchmarks.

**Решение:** -4 LLMs evaluating 21 psycholinguistic ratings for early-acquired words vs human norms

---

### 849 · R3236

**Safety-Aware Evaluation of LLM-Generated Driver Intervention Messages through Multi-Task Risk Fusion**

2026 · Applied Soft Computing · journalarticle, preprint/article, article · en · https://doi.org/10.48550/arxiv.2606.22706

Existing driver intervention systems rely on auditory alerts and fixed templates, failing to leverage multi-task recognition outputs. General-purpose metrics such as BLEU and BERTScore cannot capture intervention-specific quality dimensions including risk-urgency alignment, cognitive load, and driver acceptability. In this paper, we propose the Driver Safety-Aware Intervention Score (DSAIS), a domain-specific metric evaluating five dimensions through a hybrid architecture combining lightweight rule-based computation with LLM Judge evaluation, together with an end-to-end framework integrating four-task recognition outputs into an LLM through risk fusion, state history management, and dynamic prompt construction. Experiments on the AIDE dataset with five models and seven conditions demonstrate that DSAIS achieves ICC 0.798-0.840 across three architecturally distinct judges and Cohen's d &gt; 1.5 across all control conditions. Multi-dimensional sub-score analysis quantifies the contextual adaptability gap between rule-based and LLM-based systems, revealing that multi-task integration improves contextual relevance by 9.1% over rule-based baselines. Ablation experiments demonstrate that each framework component contributes to contextual relevance, with sub-score decomposition revealing gains that aggregate scoring masks. Driver emotion recognition is identified as the most critical upstream factor, and compact local LLMs (7B--9B parameters) achieve quality superior to API-based models, providing practical design guidelines for in-vehicle deployment.

**Решение:** -4 safety-aware driver intervention messages in autonomous vehicles

---

### 850 · R0217

**Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.21347

Diagnosing failures in LLM agents remains largely manual. Practitioners inspect a small subset of execution traces, form ad-hoc hypotheses, and iterate. This process misses patterns that only emerge across trace populations and does not scale to production corpora where individual traces span tens of thousands of tokens. We formalize the problem of corpus-level trace diagnostics. Given a corpus of execution traces, the goal is to produce grounded natural-language insights that characterize systematic behavioral patterns across trace groups, each linked to supporting evidence. We present the Insights Generator (IG), a multi-agent system that answers diagnostic questions by proposing and testing hypotheses across the trace corpus to produce an evidence-backed insights report. We evaluate IG across qualitative and objective dimensions, spanning rubric-based report assessment and downstream performance improvements achieved by implementing IG insights. Human experts using IG reports improve scaffold performance by 30.4 pp over the unmodified baseline scaffold, and coding agents leveraging IG-derived insights show consistent and stable gains. Across benchmarks, IG's scout-investigator architecture produces findings comparable in detection coverage to competing approaches, while domain experts rated IG reports as leading depth and evidence quality. v4: expanded evaluation with the APEX-Agents benchmark and a GPT-5.4 cross-family judge. Revised analysis and appendices

**Решение:** -6 Insights Generator: trace diagnostics for LLM agents

---

### 851 · R8288

**Multimodal AI for Automated Interview Training: A Systematic Literature Review on Candidate Feedback and Performance Improvement**

2025 · International Conference on Informatics, Multimedia, Cyber and Information System (ICIMCIS) · conference, review · https://doi.org/10.1109/icimcis68501.2025.11327289

Interviews are central to education and career development, yet traditional training with human evaluators is difficult to scale and standardize. Multimodal artificial intelligence (AI) offers new opportunities to automate interview practice by jointly analyzing text, speech, and nonverbal behavior. This systematic literature review synthesizes 20 studies published between 2020 and 2025, examining application domains, effectiveness for candidate feedback and performance improvement, and technical integration strategies. The findings indicate that large language models enable adaptive questioning and rubric-based feedback, affective computing captures confidence and emotional states, and virtual or metaverse environments increase realism and engagement. Reported outcomes include gains in communication clarity, self-awareness, confidence, and domain-specific skills in medical, technical, and autism-support contexts. Typical architectures combine automatic speech recognition, facial expression analysis, and late fusion with dialogic feedback loops. Remaining challenges concern data scarcity, cross-cultural fairness, real-time robustness, and long-term impact. This review provides a focused synthesis to guide the design of more effective, scalable, and ethical interview training systems worldwide.

**Решение:** -1 systematic literature review on multimodal AI for automated interview training

---

### 852 · R3413

**Entity-specific text classification with large language models: two applications on financial and brand news**

2026 · China Accounting and Finance Review · journalarticle, article · en · https://doi.org/10.1108/cafr-12-2025-0269

Purpose This paper evaluates the performance of off-the-shelf large language models (LLMs) on two distinct entity-specific classification challenges in empirical economic research: assessing sentiment toward individual financial assets and identifying brand involvement during a product-harm crisis. Multiple assets or brands may appear in the same article, thus rendering document-level analysis of little use when the goal is to extract information at a granular (specific asset or brand) level. Design/methodology/approach In this paper, we attempt to benchmark recent Large Language Models (LLMs), such as OpenAI's GPT, on entity-specific text classification tasks. We illustrate their performance in two distinct applications. First, we demonstrate that LLMs can identify asset-specific sentiments in Wall Street Journal (WSJ) financial news. Second, we evaluate the effectiveness of these models in identifying brand involvement in a product-harm crisis, using a news corpus of the 2008 Chinese infant milk formula scandal. To assess the performance of these models, we compared machine coding results with human annotations. We calculated the F1 score, which helps measure how well a model works by balancing two key factors: precision (i.e. how often the model's positive predictions are correct) and recall (i.e. how many of the actual positive cases the model correctly identifies), providing a holistic evaluation of the models' overall performance. The two applications jointly illustrate that LLM-based entity-specific text classification works robustly in different scenarios and with different languages. Findings Our results demonstrate that LLMs can achieve high accuracy in entity-specific classification while maintaining simplicity and cost-effectiveness. Originality/value This research is of interest to various stakeholders. Using these new models, investors can leverage asset-level sentiment to make better decisions in complex markets. Lenders could benefit from improved risk evaluation models that incorporate more precise data related to a specific company. Managers can clinically tease apart sentiment towards their brands vis-à-vis others. For researchers, this research adds to the existing literature on the use of machine learning in text classification, specifically on extracting entity-specific information. Previous studies in this area have shown that machine learning models can be used to analyse texts in finance and psychology at the document level. Our study extends this line of work to an entity-focused case, which yields better insights. Our findings suggest increasing capabilities of machine learning models and show new opportunities for efficient and large-scale solutions in a field that has suffered from cost and scalability factors.

**Решение:** -4 entity-specific text classification on financial and brand news

---

### 853 · R4266

**AB070. Integrating health and ethics in climate adaptation: a global review of National Adaptation Plans (NAPs)**

2026 · Journal of Public Health and Emergency · conference-abstract · https://doi.org/10.21037/jphe-26-ab070

Background: As the climate crisis intensifies, national adaptation strategies—including National Adaptation Plans (NAPs), National Adaptation Programmes of Action (NAPAs), and related policy documents—play a critical role in shaping how countries protect public health. These documents are key instruments for defining climate-health priorities, yet little is known about the extent to which they include concrete health interventions or address the ethical imperatives of equity and vulnerability. This study examines how national adaptation strategies globally integrate health-related interventions and ethical considerations. It aims to identify which countries are addressing health comprehensively, which interventions are prioritized or overlooked, and how vulnerable populations are represented (or neglected) in climate adaptation planning.Methods: A total of 123 national adaptation documents (NAPs, NAPAs, and related strategies) were reviewed. ChatGPT-Pro was used for initial content extraction, followed by manual coding and qualitative synthesis. Documents were assessed for five health-related intervention categories: disaster risk reduction, health workforce training, heat adaptation, mental health, and vaccination. Mentions of vulnerable groups were also analyzed.Results: Only 10% of countries addressed four or more of the five key health themes. Disaster risk reduction (91%) and health workforce training (81%) were the most commonly included interventions. In contrast, mental health (11%) and vaccination (17%) were severely underrepresented. While vulnerable groups such as women, children, and the elderly were mentioned in many strategies, few included targeted interventions to address their specific needs, highlighting a gap between recognition and action.Conclusions: Despite growing recognition of climate-health risks, most national adaptation strategies fall short of comprehensive or equity-focused responses. Strengthening the ethical and programmatic integration of health in these strategies is critical to ensure inclusive and just climate adaptation.

**Решение:** -4 content analysis of National Adaptation Plans for climate adaptation

---

### 854 · R2949

**AI Content Moderation in Therapy Conversations**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.25454

Large language models (LLMs) are increasingly being used for emotional support. They are also being developed for formal therapy purposes. However, LLMs like ChaptGPT or Llama are often developed with content moderation guardrails that prevent them from discussing sensitive subjects with users for both liability and safety purposes, and this inability to broach these subjects may affect their capacity as therapists. In this study, we perform an algorithm audit on three state-of-the-art moderation systems (OpenAI's moderation endpoint, Meta's Llama Guard, and Google's Shield Gemma) to investigate the extent to which these systems flag the content of real-life therapy sessions as undesirable. Our results raise implications for the limitations that users and organizations may encounter when designing LLMs to play the part of a therapist.

**Решение:** -6 algorithm audit of content moderation filters on real-life therapy sessions

---

### 855 · R7385

**Beyond Self-Reports: Multi-Observer Agents for Personality Assessment in Large Language Models**

2025 · Underline Science Inc. · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48448/nh55-bn05

Self-report questionnaires have long been used to assess LLM personality traits, yet they fail to capture behavioral nuances due to biases and meta-knowledge contamination. This paper proposes a novel multi-observer framework for personality trait assessments in LLM agents that draws on informant-report methods in psychology. Instead of relying on self-assessments, we employ multiple observer agents. Each observer is configured with a specific relational context (e.g., family member, friend, or coworker) and engages the subject LLM in dialogue before evaluating its behavior across the Big Five dimensions. We show that these observer-report ratings align more closely with human judgments than traditional self-reports and reveal systematic biases in LLM self-assessments. We also found that aggregating responses from 5 to 7 observers reduces systematic biases and achieves optimal reliability. Our results highlight the role of relationship context in perceiving personality and demonstrate that a multi-observer paradigm offers a more reliable, context-sensitive approach to evaluating LLM personality traits. 16 pages, 6 figures, 6 tables

**Решение:** -2 multi-observer agents assessing personality traits of LLM agents

---

### 856 · R6829

**Harnessing AI for Compassionate Care: Identifying and Supporting Patients with Social Determinants and Medical Complexity**

2026 · International Journal of Integrated Care · journalarticle, review, conference-abstract · https://doi.org/10.5334/ijic.icic26152

Background: Social determinants of health (SDoH) play an important role in hospital-to-home transitions and outcomes aligned with the Quintuple Aim, yet current point-of-care surveys suffer from low response rates, leaving capture of SDoH incomplete and challenging to use for evaluation and spread. To address these issues, we developed and validated a large language model (LLM) that captures SDoH from electronic health records (EHR) at University Health Network in Toronto, Canada. Approach: Following a literature review and discussion with partners, including patients and caregivers, a specialized keyword list relevant to hospital-to-home and patient outcomes was developed. In the first phase, relevant SDoH included the following: language barrier, financial strain, social isolation, housing insecurity, depression, addiction, food insecurity, transportation barriers, and health literacy. This list was used to search the EHR and to build a labeled keyword set. The LLM (DeepSeek-32B) was applied to inpatient notes from patients discharged between August 2021 and March 2024 who were eligible for an integrated care pathway. For each run, the LLM produced a classification (yes/no) indicating whether that social need is present, and when present, a supporting span of text from the notes with a brief reasoning explaining the decision was produced. Human reviewers subsequently reviewed the model’s output, creating confusion matrices for each SDoH reporting precision (positive predictive value), recall (sensitivity), F1 (a score that balances both precision and recall), and prevalence for every category. In Phase 2, the model is being applied to a larger cohort with an expected higher prevalence of patients with social complexity. Our team is performing a targeted chart review and updating prompts based on the results to improve accuracy and reduce false negatives. Results: In Phase 1, we processed 67,000 notes from 2890 inpatients, flagging 1,139 patients (30%) with at least one SDoH. The LLM doubled the capture of social needs (prevalence) from 4% to 8%, with 98% accuracy. Precision, recall, and F1-scores averaged 76%, 97% and 84% respectively, the latter of which is close to human agreement on the same task (80%). Issues identified included: 1) the need to refine the LLM to improve accuracy for select SDoH like food insecurity, 2) adding further distinctions between active and historical social needs like depression and addiction, 3) consideration for human reinforcement so that information irrelevant to current care planning can be incorporated directly feedback loops. Phase 2 (currently underway) extends the evaluation and refinement to 232,253 notes among 7,000 patients, demonstrating a current increase in capture to14% with social needs. Ongoing error analyses inform documentation and prompt engineering and design. Implications: LLMs can rapidly identify, extract, and summarize SDoH data from a large volume of unstructured interdisciplinary notes in EHRs, offering a practical way to capture SDoH for hospital-to-home integrated care programs. We are validating the model with our Calgary partners to demonstrate feasibility across different hospital settings and documentation practices. This demonstrates scalability and transferability to international health systems addressing similar challenges in SDoH capture and care coordination.

**Решение:** ? T1/T3 extracting SDoH and clinical needs (depression, addiction) from EHR notes using DeepSeek vs human review; check construct

---

### 857 · R7708

**From Narratives to Probabilistic Reasoning: Predicting and Interpreting Drivers' Hazardous Actions in Crashes Using Large Language Model**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2510.13002

Vehicle crashes involve complex interactions between road users, split-second decisions, and challenging environmental conditions. Among these, two-vehicle crashes are the most prevalent, accounting for approximately 70% of roadway crashes and posing a significant challenge to traffic safety. Identifying Driver Hazardous Action (DHA) is essential for understanding crash causation, yet the reliability of DHA data in large-scale databases is limited by inconsistent and labor-intensive manual coding practices. Here, we present an innovative framework that leverages a fine-tuned large language model to automatically infer DHAs from textual crash narratives, thereby improving the validity and interpretability of DHA classifications. Using five years of two-vehicle crash data from MTCF, we fine-tuned the Llama 3.2 1B model on detailed crash narratives and benchmarked its performance against conventional machine learning classifiers, including Random Forest, XGBoost, CatBoost, and a neural network. The fine-tuned LLM achieved an overall accuracy of 80%, surpassing all baseline models and demonstrating pronounced improvements in scenarios with imbalanced data. To increase interpretability, we developed a probabilistic reasoning approach, analyzing model output shifts across original test sets and three targeted counterfactual scenarios: variations in driver distraction and age. Our analysis revealed that introducing distraction for one driver substantially increased the likelihood of "General Unsafe Driving"; distraction for both drivers maximized the probability of "Both Drivers Took Hazardous Actions"; and assigning a teen driver markedly elevated the probability of "Speed and Stopping Violations." Our framework and analytical methods provide a robust and interpretable solution for large-scale automated DHA detection, offering new opportunities for traffic safety analysis and intervention.

**Решение:** -4 predicting driver hazardous actions from crash narratives

---

### 858 · R6973

**Lost in the middle? examining scoring reliability and position bias in LLM-based automated essay scoring**

2026 · Education and Information Technologies · journalarticle, article · en · https://doi.org/10.1007/s10639-026-14019-8

Abstract This study investigates position bias in ChatGPT’s scoring patterns for automated essay scoring, with a focus on primacy and recency effects. Position bias, originating from the serial position effect in cognitive psychology, refers to the tendency of Large Language Models (LLMs) to emphasize the introduction and conclusion of a text while potentially neglecting content in the middle sections. Using 192 synthetic essays across varying lengths and section qualities, this research explores whether ChatGPT disproportionately weighs the quality of introductions and conclusions compared to body paragraphs. Statistical analyses reveal that while ChatGPT successfully differentiates between strong and weak sections, no consistent evidence supports the presence of systematic primacy or recency effects in overall scoring. Domain-specific analyses further indicate that rubric categories such as grammar and mechanics are sensitive to errors throughout essays, while content and organization are more heavily influenced by body quality. The findings suggest that ChatGPT’s scoring patterns are largely balanced, with minimal signs of position bias, thereby enhancing the validity of its use for automated scoring. This research highlights the need for continued evaluation of AI-based grading systems to ensure fairness and reliability while proposing avenues for future exploration in LLM-driven assessments.

**Решение:** -4 position bias in LLM-based automated essay scoring

---

### 859 · R3464

**En experimentell utvärdering av promptbaserad klassificering med stora språkmodeller jämfört med mänsklig kvalitativ kodning : Dialogklassificering i utbildningssammanhang**

2026 · Diva portal (Dalarna University Library) · dissertation · en · http://urn.kb.se/resolve?urn=urn:nbn:se:lnu:diva-147223

The increasing use of Generative Artificial Intelligence (GenAI) in education has led to growing amounts of interaction data between teachers and AI chatbots. These interactions provide opportunities for educational research, but manual qualitative coding of dialogue data is time-consuming, difficult to scale, and dependent on human expertise. Recent advances in Large Language Models (LLMs) have created new possibilities for supporting or automating qualitative analysis through prompt-based text classification. This thesis investigates how well prompt-based LLMs can reproduce human qualitative coding of teacher–chatbot interactions using a predefined codebook. The study further examines how classification performance is affected by different prompting strategies and access to conversational context. A controlled experiment was conducted using a manually annotated dataset originating from an educational workshop where teachers interacted with AI chatbots. The evaluation compared GPT-4o and Claude Sonnet across multiple classification categories using zero-shot and few-shot prompting, both with and without dialogue context. The findings indicate that prompt-based LLMs can reproduce human qualitative coding to a moderate extent, although performance varies across categories and experimental conditions. Conversational context generally improved classification performance, particularly for categories that depended on understanding previous dialogue, while the impact of few-shot prompting was more inconsistent. The results also suggest that categories with clearer label definitions are easier for LLMs to classify than categories requiring interpretation of communicative intent or nuanced distinctions. The study contributes to the growing body of research on LLM-assisted qualitative analysis by providing insights into the opportunities and limitations of using prompt-based language models for dialogue classification in educational settings. The findings suggest that LLMs can support researchers in large-scale annotation tasks, but they do not currently replace human qualitative interpretation.

**Решение:** -4 prompt-based LLM classification of teacher-chatbot dialogues in educational workshop

---

### 860 · R2302

**SAE Information Theory II: A Structural Derivation of Landauer's Principle within the SAE Framework — Three Pillars and Their Open Problems / SAE 信息论 II:SAE Framework 下 Landauer 原理的结构推导——三支柱与开放问题**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.19780314

Full bilingual text and framework available at self-as-an-end.net The first paper in the SAE Information Theory series (DOI: 10.5281/zenodo.19740019) established the 4DD ontology of information and a foundational axiom (energy-information conservation across 42 × 1DD), and offered a conditional ontological reading of the ln 2 factor in Landauer's principle: ln 2 can be read as a projection factor produced when continuous measurement formalism reads a discrete substrate. The present paper takes up the task of lifting this reading into a structural derivation within the SAE framework. We identify three prerequisites of any Landauer derivation, each handled by a separate pillar. Pillar 1 concerns the structural relation between Shannon H and SAE I in the erasure setting. Pillar 2 concerns the structural bridge between the statistical temperature T in Landauer's formula and the SAE geometric quantity c^3. Pillar 3 concerns the structural origin of ln 2 given the inherited substrate-binary commitment. Each pillar is examined for what it can and cannot deliver inside the SAE framework, and a combination analysis honestly assesses the actual contribution. Three honest acknowledgments are central. First, the derivation is framework-internal and conditional on inherited commitments (substrate-binary from Paper I, E=Ic^3 from the Mass Series), not an unconditioned physics-level first-principles derivation. Second, the actual derivation backbone remains a standard Bennett-style entropy argument; the SAE contribution lies in supplying ln 2 with a substrate-binary structural reading and giving the erasure operation a substrate-redistribution ontological picture, not in providing an alternative derivation backbone. Third, a macroscopic 1-bit erasure does not correspond to a single substrate event but to a statistical aggregation across substrate-level events, and the substrate-level minimal quantity I_bit is calibrated through combination with the Landauer constraint rather than derived independently. The paper explicitly marks three success tiers as all substantive contributions: a strongest tier requiring future Thermo verification, a middle tier delivering structural derivation with bottleneck localization (the actual outcome), and a weakest tier as first-time precise localization of the walls in the SAE-internal Landauer derivation chain. The Chinese version is the authoritative version; the English is an independent rewrite (not a translation).SAE 信息论系列第一篇(DOI: 10.5281/zenodo.19740019)建立信息的 4DD 本体论与一条基础公理(能量-信息守恒 across 42 × 1DD),并对 Landauer ln 2 给出 conditional 本体论 reading:ln 2 可以读为连续测量 formalism 读取离散 substrate 的 projection 因子。本文的任务是把这个 reading 升级为 SAE framework 下的结构推导。 本文识别 Landauer 推导的三个 prerequisites 对应三个支柱。支柱一是擦除情境下 Shannon H 与 SAE I 的结构关系,支柱二是 T 与 c^3 之间的结构桥接,支柱三是给定 substrate-binary commitment 下 ln 2 的结构来源。本文 honest 评估三支柱在 SAE framework 下能 deliver 什么、不能 deliver 什么。 核心 honest acknowledgment 三层:framework-internal 推导而非 unconditioned first-principles;actual 推导 backbone 仍是 Bennett-style entropy argument;宏观 1 bit 擦除涉及 substrate 层 statistical aggregation。 本文进中间档——结构推导加 T-c^3 bridge bottleneck localized。三档 outcome(最强、中间、最弱)都作为 substantive 科学贡献。 中文为 authoritative version,英文为 independent rewrite(不是 translation)。 Related identifiers This paper is part of the SAE Information Theory series. isPartOf: - SAE Information Theory Series cites: - 10.5281/zenodo.19740019 (Paper I — SAE Information Theory I) - 10.5281/zenodo.18528813 (SAE Foundations Paper 1) - 10.5281/zenodo.18666645 (SAE Foundations Paper 2) - 10.5281/zenodo.18727327 (SAE Foundations Paper 3) - 10.5281/zenodo.19476358 (Mass Series Paper I) - 10.5281/zenodo.19510868 (Four Forces Convergence — E=Ic^3) - 10.5281/zenodo.19310282 (Thermo Series Paper I) - 10.5281/zenodo.19703273 (Thermo Series Paper X — Closing) - 10.5281/zenodo.19385464 (Life and Death Series Paper IV) - 10.5281/zenodo.19739810 (ZFCρ Paper 68) continues: - 10.5281/zenodo.19740019 (Paper I) AI use statement This paper was independently authored by Han Qin. AI systems (Claude, ChatGPT, Grok, Gemini) were used in distinct review-and-drafting roles during the writing process: - Claude: structural drafting and architectural assistance, identification of overclaim risks - ChatGPT: strict logical review, scope discipline - Grok: exhaustive consistency check, cross-paper citation verification - Gemini: divergent thinking, generative pointer suggestions All filtering, synthesis, and final intellectual decisions were made by the author. The framework design, derivation choices, claim-status mapping, and editorial judgments are the author's. The Chinese version is authoritative; the English version is an independent rewrite (not a translation) generated through the same authorial process.

**Решение:** -1 SAE Information Theory II (theoretical essay)

---

### 861 · R4483

**Cognitive Clinical Foundation Models for AI- Assisted Precision Oncology: A Multimodal Agentic Framework for Real-Time Cancer Therapeutic Decision Support**

2026 · 2026 International Conference on Advancements in Smart, Secure and Intelligent Computing (ASSIC) · conference · https://doi.org/10.1109/assic70037.2026.11717062

Precision oncology requires integrating heterogeneous patient data streams genomics, imaging, pathology, pharmacology and electronic health records (EHR)-into actionable therapeutic recommendations under time-critical constraints. Existing clinical decision support systems rely on unimodal model’s incapable of holistic oncological reasoning, while frontier large language models introduce hallucination risks and compute overheads incompatible with consumer edge deployment. This paper presents CogOnco-MAAI, a Cognitive Clinical Foundation Model (CCFM) orchestrating a multimodal agentic AI framework for AI-assisted precision oncology decision support. In IRB-approved prospective evaluation across 12,600 patients at seven NCI-designated cancer centers, CogOnco-MAAI achieves Therapeutic Recommendation Accuracy (TRA) of 94.3% (95 CI: 93.8-94.8%), AUC-ROC of 97.1% and F1 of 93.8%, demonstrating improved performance relative to Med-PaLM M. A five-agent pipeline achieves 1.24 s median latency. The Oncology Decision Explainability Score (ODES) attains 91.4% clinician-agreement $(\kappa=0.83)$, exceeding the FDA AI/ML SaMD 85% threshold. The edge-optimized distilled model achieves 11.2 MB ONNX, 38 ms inference and 0.94 J/query on Snapdragon 8 Gen 3 hardware. To the best of our knowledge, CogOnco-MAAI represents a multimodal agentic AI framework for AI-assisted oncology decision support for AI-assisted oncology decision support at the edge-enabled healthcare environments.

**Решение:** -4 Cognitive Clinical Foundation Models for precision oncology

---

### 862 · R3222

**Current trends and prospects of AI-assisted cognitive behavioral therapy: from the perspective of support and complementation**

2026 · Stress Science Research · article · en · https://doi.org/10.5058/stresskagakukenkyu.2025007

Cognitive behavioral therapy (CBT) has demonstrated efficacy for a wide range of mental disorders; however, access to treatment remains limited due to a shortage of trained professionals and institutional constraints. This article traces the development of digital CBT (dCBT) against this backdrop and examines recent advances in CBT support utilizing generative artificial intelligence (AI) and large language models (LLMs). Three primary applications are discussed: chatbots, personalization, and recommendation systems, with representative research findings presented for each. AI-powered CBT shows promise as an early intervention tool within stepped care models. Nevertheless, the therapeutic alliance—characterized by the capacity to share uncertainty—remains a uniquely human function that AI cannot replicate. Moving forward, it will be essential to distinguish between outcome indicators common to both human-delivered and digital CBT, such as symptom reduction and adherence, and those specific to human therapists, such as therapeutic alliance. This perspective may inform future research and clinical implementation of AI-assisted mental health interventions.

**Решение:** -1 review of current trends in AI-assisted cognitive behavioral therapy

---

### 863 · R0286

**AutoMalDesc: Large-Scale Script Analysis for Cyber Threat Research**

2026 · Proceedings of the AAAI Conference on Artificial Intelligence · conference-paper · https://doi.org/10.1609/aaai.v40i1.36959

Generating thorough natural language explanations for threat detections remains an open problem in cybersecurity research, despite significant advances in automated malware detection systems. In this work, we present AutoMalDesc, an automated static analysis summarization framework that, following initial training on a small set of expert-curated examples, operates independently at scale. This approach leverages an iterative self-paced learning pipeline to progressively enhance output quality through synthetic data generation and validation cycles, eliminating the need for extensive manual data annotation. Evaluation across 3,600 diverse samples in five scripting languages demonstrates statistically significant improvements between iterations, showing consistent gains in both summary quality and classification accuracy. Our comprehensive validation approach combines quantitative metrics based on established malware labels with qualitative assessment from both human experts and LLM-based judges, confirming both technical precision and linguistic coherence of generated summaries. To facilitate reproducibility and advance research in this domain, we publish our complete dataset of more than 100K script samples, including annotated seed (900) and test (3.6K) datasets, along with our methodology and evaluation framework.

**Решение:** -4 AutoMalDesc: automated malware script analysis (duplicate topic)

---

### 864 · R8342

**Black-Box Guardrail Reverse-engineering Attack**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2511.04215

Large language models (LLMs) increasingly employ guardrails to enforce ethical, legal, and application-specific constraints on their outputs. While effective at mitigating harmful responses, these guardrails introduce a new class of vulnerabilities by exposing observable decision patterns. In this work, we present the first study of black-box LLM guardrail reverse-engineering attacks. We propose Guardrail Reverse-engineering Attack (GRA), a reinforcement learning-based framework that leverages genetic algorithm-driven data augmentation to approximate the decision-making policy of victim guardrails. By iteratively collecting input-output pairs, prioritizing divergence cases, and applying targeted mutations and crossovers, our method incrementally converges toward a high-fidelity surrogate of the victim guardrail. We evaluate GRA on three widely deployed commercial systems, namely ChatGPT, DeepSeek, and Qwen3, and demonstrate that it achieves an rule matching rate exceeding 0.92 while requiring less than $85 in API costs. These findings underscore the practical feasibility of guardrail extraction and highlight significant security risks for current LLM safety mechanisms. Our findings expose critical vulnerabilities in current guardrail designs and highlight the urgent need for more robust defense mechanisms in LLM deployment.

**Решение:** -4 black-box guardrail reverse-engineering attack

---

### 865 · R3035

**Validation plan for author-home classification**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/semzt

Design Author-home labels from the primary classifier (System One, jev-1.13.0) could be checked against an independent local open-weight model. The second model may be a Llama-family model or another local model named in Methods. Primary validation is agreement between those two machine labels. Human review is limited to discordant rows and pre-specified low-confidence rows. Review uses a source-blind click interface with two unlabeled category options, plus Neither and Unsure. Machine concordance The local model classifies first-author and senior-author affiliations for all included articles. Input is affiliation text only. Temperature is 0. The prompt and typed schema are frozen before comparison and are not tuned against System One labels. Agreement is reported as Cohen kappa, per-class agreement, and a confusion matrix across all includes. Human adjudication Reviewers see affiliation text only. The two machine labels appear as department categories without model names. Left and right sides are randomized per row from a logged seed. Options are the two categories, Neither, and Unsure. One click advances. Decisions append to a JSONL log. No spreadsheet coding is used. Low-confidence criteria Rows enter the human queue when any of the following apply: (a) the local model returns unclear or a low-probability trauma/ACS or MIS/bariatric label; (b) a System One title or journal fallback is recoverable from the run log (if not recoverable, this criterion is dropped and disclosed); (c) both models agree on trauma/ACS or MIS/bariatric while a keyword draft disagrees. The keyword draft is a flag only and is not a rater. Three-way S S is reported three ways: with adjudicated labels applied; with adjudicated rows excluded; and with adjudicated rows resolved against trauma/ACS. The third version is the worst case for a trauma/ACS concentration finding. All three versions are reported regardless of direction. Triggers If kappa is below 0.80, or trauma-specific or MIS-specific agreement is below 0.85, or worst-case S is more than 5 percentage points below adjudicated S, then worst-case S becomes co-primary. Other audits Screening, unclear rows, pre-filter checks, reported N, meeting programs, and venue remapping use machine comparison on pre-specified samples or censuses. Click adjudication is used only for discordant or low-confidence rows. Queue size is reported before clicking begins. Human adjudicator The affiliation queue is adjudicated by the PI, a trauma/ACS surgeon. Methods disclose this. A backup adjudicator may be named later and is not required for registration. Optional concordant spot-check A random sample of 50 concordant trauma/ACS or MIS/bariatric rows may be clicked to estimate shared model error. This check is not required. If it is not done, Limitations state that shared errors were not measured directly and that concordance-based accuracy could overestimate true accuracy. Timing The second-model run does not start until this registration is public. Prompt, schema, queue rules, bounds, and triggers are fixed before that run. An optional large-model tie-break on Unsure rows only may be used, capped at 50, and remains off by default. If System One uses a Llama-family base model, that fact is disclosed as an independence note. Unchanged S equals T divided by (T plus M) among specialty-identifiable bylines, always with the five-category distribution. Abstracts are not re-screened in bulk with an LLM for inclusion. Claims stay within scholarship concentration and estimand S. Materials to deposit after the run Frozen prompt and schema; model name and version actually used; concordance outputs; queue definitions and sizes; click logs; kappa; confusion matrix; three-way S with Wilson confidence intervals; trigger decisions.

**Решение:** -4 validation plan for author affiliation classification

---

### 866 · R4368

**Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.05029

Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning history. In this paper, we introduce the Forged Amplifying Rationale Memory Attack (FARMA), which poisons an agent's remembered reasoning rather than its factual knowledge. It inserts forged reasoning traces using evasive language that bypasses keyword-based defenses, then amplifies them through self-referential reinforcement that defeats consensus-based defenses. To address FARMA, we introduce SENTINEL, a layered defense pipeline to detect forged reasoning entries. Its central component is the Reasoning Guard that structurally analyzes candidate entries for forgery using five weighted signals. We evaluate FARMA and SENTINEL across multiple agents and different LLM models with 50 trials and show that FARMA achieves an attack success rate of up to 100% under baseline conditions and is capable of defeating defense mechanisms like keyword filter and A-MemGuard. Our evaluation also shows that SENTINEL reduces FARMA's attack success rate to as low as 0% with no false positives observed across 326 benign agent traces. Our work demonstrates the need to protect not only an agent's retrieved content but also the integrity of its reasoning history. Preprint. 10 pages, 2 figures, 4 tables

**Решение:** -4 forged reasoning attacks on LLM agent memory

---

### 867 · R4667

**Alignement multi-agents de modèles de langage pour la génération de code guidée par des préférences multiples**

2026 · Université de Montréal · dissertation/thèse ou mémoire / thesis or dissertation · https://doi.org/10.71781/34346

Les progrès récents des modèles de langage de grande taille (LLMs) ont considérablement amélioré la génération automatique de code, mais leurs exigences computationnelles massives en limitent l’accessibilité. À l’inverse, les modèles de petite taille (SLMs) permettent un déploiement plus léger, mais présentent souvent des performances inférieures en matière de correction fonctionnelle et de qualité du code. Ce mémoire propose un cadre agentique pour la génération de code avec des SLMs, dans lequel plusieurs spécialistes de préférences collaborent afin d’affiner une solution initiale. Deux stratégies de coordination sont étudiées : (i) critique–édition, où des experts fournissent des retours structurés agrégés par un éditeur unique, et (ii) raffinement distribué, où les experts révisent itérativement la solution et valident mutuellement le respect des préférences. La correction fonctionnelle est évaluée sur BigCodeBench (Hard) à l’aide de la métrique Pass@k, et l’alignement aux préférences est mesuré via un protocole pair-à-pair fondé sur un LLM-as-a-Judge. La coordination multi-agents améliore principalement les performances lorsque plusieurs générations sont autorisées : sous le mode Complete, critique–édition atteint Pass@5 = 18,2 et Pass@10 = 19,6, tandis que le raffinement distribué atteint Pass@5 = 17,6. Ces gains s’accompagnent d’une baisse de la fiabilité au premier essai (Pass@1 = 7,7 pour critique–édition). Par ailleurs, le peaufinage basé sur les préférences améliore la qualité perçue du code, avec 70–78 % de préférences en faveur des variantes ajustées. Ces résultats mettent en évidence un compromis entre alignement qualitatif et correction fonctionnelle immédiate, tout en montrant la complémentarité des deux leviers proposés. Recent progress in large language models (LLMs) has significantly advanced automatic code generation, but their massive computational demands limit accessibility. In contrast, small language models (SLMs) enable lightweight deployment but often underperform in terms of correctness and broader code quality. This thesis proposes an agentic framework for SLM code generation in which multiple preference specialists collaborate to refine an initial solution. We compare two coordination strategies: (i) critique–edit, where experts provide structured feedback aggregated by a single editor, and (ii) distributed refinement, where experts iteratively revise and cross-validate the solution. We evaluate functional correctness on BigCodeBench (Hard) using Pass@k, and assess preference alignment with an LLM-as-a-Judge pairwise protocol. Multi-agent coordination primarily improves outcomes when multiple generations are allowed: under Complete prompting, critique–edit reaches Pass@5 = 18.2 and Pass@10 = 19.6, while distributed refinement reaches Pass@5 = 17.6. These gains come with reduced top-1 reliability (e.g., critique–edit Pass@1 = 7.7), indicating that coordination strengthens exploration and recovery across attempts rather than first-try accuracy. Complementarily, LLM-as-a-Judge results show that preference fine-tuning improves perceived code quality, with fine-tuned variants preferred in roughly 70–78% of comparisons for readability/complexity metrics. Overall, the results highlight two complementary levers for SLM code generation: multi-agent coordination boosts Pass@k under multi-sampling, while preference fine-tuning improves qualitative alignment, exposing a trade-off between stylistic alignment and first-attempt functional correctness.

**Решение:** -4 multi-agent LLMs for code generation

---

### 868 · R3657

**A case report on gendered biases in a Finnish healthcare AI assistant**

2026 · medRxiv · preprint, ppr · https://doi.org/10.64898/2026.04.09.26350383

Abstract In this study, we investigate gender bias in a Retrieval-Augmented Generation (RAG) based AI assistant developed for Finnish wellbeing services counties. We tested the system using 36 clinically relevant queries, each rendered in three gendered variants (male, female, gender-neutral), and evaluated responses using both an LLM-as-a-judge approach and a human expert panel consisting of a physician and a sociologist specializing in ethics. We observed substantial and clinically significant differences across gendered variants, including differential treatment urgency, inappropriate symptom associations, and misidentification of clinical context. Female variants disproportionately framed responses around childcare and reproductive health regardless of clinical relevance, reflecting societal stereotypes rather than medical reasoning. Bias manifested both at the LLM generation stage and the RAG retrieval stage, in several cases causing the model to hallucinate responses entirely. Some bias patterns were persistent across repeated runs, while others appeared inconsistently, highlighting the challenge of distinguishing systematic bias from stochastic variation.

**Решение:** -4 case report on gendered biases in Finnish healthcare AI assistant

---

### 869 · R10088

**Scalable Defense against In-the-wild Jailbreaking Attacks with Safety Context Retrieval**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2505.15753

Large Language Models (LLMs) are known to be vulnerable to jailbreaking attacks, wherein adversaries exploit carefully engineered prompts to induce harmful or unethical responses. Such threats have raised critical concerns about the safety and reliability of LLMs in real-world deployment. While existing defense mechanisms partially mitigate such risks, subsequent advancements in adversarial techniques have enabled novel jailbreaking methods to circumvent these protections, exposing the limitations of static defense frameworks. In this work, we explore defending against evolving jailbreaking threats through the lens of context retrieval. First, we conduct a preliminary study demonstrating that even a minimal set of safety-aligned examples against a particular jailbreak can significantly enhance robustness against this attack pattern. Building on this insight, we further leverage the retrieval-augmented generation (RAG) techniques and propose Safety Context Retrieval (SCR), a scalable and robust safeguarding paradigm for LLMs against jailbreaking. Our comprehensive experiments demonstrate how SCR achieves superior defensive performance against both established and emerging jailbreaking tactics, contributing a new paradigm to LLM safety. Our code will be available upon publication.

**Решение:** -4 defense against in-the-wild jailbreaking attacks

---

### 870 · R1222

**DMT-CBT: Longitudinal Therapeutic State Modeling for CBT Counseling**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.03132

Large language models (LLMs) have shown growing potential for Cognitive Behavioral Therapy (CBT) counseling. However, most existing approaches still formulate counseling as a local response generation problem, focusing on empathetic replies within short, text-only, or single-session interactions. We argue that this formulation fundamentally mismatches the nature of real psychotherapy. In clinical CBT, therapy is a longitudinal process in which therapists continuously infer, update, and intervene on evolving therapeutic states across sessions. Realistic CBT further involves multimodal inference and delayed cross-session intervention effects, requiring models to capture longitudinal therapeutic state evolution under partial observability. We propose DMT-CBT, a framework for Dynamic Modeling of evolving Therapeutic states in CBT counseling. DMT-CBT maintains structured therapeutic states across sessions while incorporating multimodal behavioral grounding and tool-augmented intervention to support adaptive therapeutic reasoning. Based on this framework, we construct DMTCorpus, a synthetic multi-session multimodal CBT counseling dataset featuring evolving therapeutic states, image-grounded client behaviors, and cross-session intervention continuity. Experimental results show that DMT-CBT improves counseling fidelity and therapeutic alliance, produces more favorable longitudinal affective trajectories, and preserves therapeutic states more faithfully than post-hoc extraction approaches.

**Решение:** -6 DMT-CBT: longitudinal therapeutic state modeling in CBT counseling on synthetic dataset

---

### 871 · R4335

**Prompt Injection Attacks on Agentic Coding Assistants: A Systematic Analysis of Vulnerabilities in Skills, Tools, and Protocol Ecosystems**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.17548

The proliferation of agentic AI coding assistants, including Claude Code, GitHub Copilot, Cursor, and emerging skill-based architectures, has fundamentally transformed software development workflows. These systems leverage Large Language Models (LLMs) integrated with external tools, file systems, and shell access through protocols like the Model Context Protocol (MCP). However, this expanded capability surface introduces critical security vulnerabilities. In this \textbf{Systematization of Knowledge (SoK)} paper, we present a comprehensive analysis of prompt injection attacks targeting agentic coding assistants. We propose a novel three-dimensional taxonomy categorizing attacks across \textit{delivery vectors}, \textit{attack modalities}, and \textit{propagation behaviors}. Our meta-analysis synthesizes findings from 78 recent studies (2021--2026), consolidating evidence that attack success rates against state-of-the-art defenses exceed 85\% when adaptive attack strategies are employed. We systematically catalog 42 distinct attack techniques spanning input manipulation, tool poisoning, protocol exploitation, multimodal injection, and cross-origin context poisoning. Through critical analysis of 18 defense mechanisms reported in prior work, we identify that most achieve less than 50\% mitigation against sophisticated adaptive attacks. We contribute: (1) a unified taxonomy bridging disparate attack classifications, (2) the first systematic analysis of skill-based architecture vulnerabilities with concrete exploit chains, and (3) a defense-in-depth framework grounded in the limitations we identify. Our findings indicate that the security community must treat prompt injection as a first-class vulnerability class requiring architectural-level mitigations rather than ad-hoc filtering approaches.

**Решение:** -4 prompt injection attacks on agentic coding assistants

---

### 872 · R10107

**Evaluating the reliability and clinical utility of artificial intelligence in first trimester prenatal screening and noninvasive prenatal testing.**

2025 · Scientific reports · journal article, journalarticle, article · eng · https://doi.org/10.1038/s41598-025-25224-9

Artificial intelligence (AI) tools like ChatGPT-4o are increasingly utilized in prenatal care. However, their reliability and clinical applicability for healthcare providers in first-trimester screening remain unclear. This study aimed to evaluate the reliability, readability, and clinical utility of ChatGPT-4o's responses to support clinicians in counseling regarding combined first-trimester screening and non-invasive prenatal testing (NIPT). Fifteen risk-stratified clinical scenarios were used to prompt ChatGPT-4o. Fourteen perinatologists rated the responses using mDISCERN and Global Quality Scale (GQS). Readability was assessed via five indices. Inter-rater agreement and internal consistency were evaluated using ICC and Cronbach's alpha. AI responses showed high inter-rater reliability (ICC = 0.998) and internal consistency (α = 0.975). GQS and mDISCERN scores were highest in high-risk scenarios. Readability did not significantly differ across risk levels, nor correlate with quality scores. ChatGPT-4o demonstrates potential as a clinical decision-support and counseling tool for clinicians involved in prenatal screening, particularly in high-risk scenarios. Further refinement is needed for consistent performance across risk levels.

**Решение:** -4 AI in first trimester prenatal screening and noninvasive prenatal testing

---

### 873 · R5272

**Can LLM Agents Really Simulate Clients in Counseling?**

2026 · ACM/SIGAPP Symposium on Applied Computing (SAC) · book, journalarticle, conference-paper · https://doi.org/10.1145/3748522.3779828

Recent studies have increasingly examined the use of large language models (LLMs) to simulate clients in counseling sessions, yet many report that LLM-generated responses tend to be excessively positive, reducing the realism of therapeutic interactions. This study conducts a quantitative analysis to verify whether such positivity bias consistently appears across a range of closed-source and open-source models and to evaluate strategies intended to mitigate it. To accomplish this, we developed a dataset and an evaluation model that score client utterances along sentiment and stance dimensions grounded in clinical expert criteria. Using multiple LLMs combined with various bias mitigation methods, we generated artificial counseling dialogues and compared them with real client data. Experimental findings show that most LLM clients exhibit significant positivity bias, revealing clear statistical differences from real counseling conversations. Although the proposed mitigation strategies alleviated this bias to some degree, they did not fully close the gap. The findings demonstrate the presence of a quantifiable gap between LLM-based counseling simulations and real client responses, suggesting the development of standardized evaluation frameworks, session-context-adaptive bias mitigation, and persona design methods to bridge this gap. All code and generated data used in this study are publicly available on our GitHub repository. 1

**Решение:** -6 quantitative analysis of positivity bias in LLM agents simulating clients in counseling

---

### 874 · R12603

**Artificial Intelligence in Foreign Language Teaching – Insights from an Interview with ChatGPT and Bard**

2023 · Journal of Linguistics and Language Teaching (Prof Thomas Tinnefeld) · journalarticle/ · https://doi.org/10.5281/zenodo.14840938

Journal of Linguistics and Language Teaching (JLLT) This article presents a comprehensive interview conducted with ChatGPT and Google Bard, investigating the role of Artificial Intelligence (AI) in the domain of Foreign Language Teaching. The primary objective of this interview, supported by subsequent analysis, is to provide valuable insights into the use, significance, and functions of AI in the context of foreign language teaching. Conducting this interview was motivated by the belief that discussing AI without seeking the opinions and estimations of prominent chatbots would be a notable gap in existing modern research. Both ChatGPT and Bard were posed the same ten questions. These questions explored various aspects, including AI as a paradigm shift in teaching methodology, the most affected areas by AI, the changing roles of teachers and students in the wake of AI, the future importance of language education, the assistance of AI in lesson preparation, the role of AI as a direct learning partner for students, the impact of AI on student assessment, and the future development of foreign language methodology. The responses obtained were, at times, predictable, while in other instances, they proved remarkable and insightful. It is crucial to emphasise that these AI systems should not be solely relied upon as references. It is highly recommended to compare their assessments with those of human experts and other publications to attain a more comprehensive understanding. From the perspective of these two AI systems, this interview represents the current state of the art.

**Решение:** -4 interview with ChatGPT and Bard on foreign language teaching

---

### 875 · R4735

**Syntactic Priming in Few-Shot Learning: How Demonstration Structure Shapes LLM Performance**

2026 · Joint Conference on Lexical and Computational Semantics · conference-paper · https://doi.org/10.18653/v1/2026.starsem-conference.2

Large language models (LLMs) exhibit remarkable few-shot learning capabilities, yet the role of syntactic structure in demonstration examples remains unexplored.Drawing on psycholinguistic research on structural priming, we investigate whether syntactic patterns in fewshot prompts influence LLM outputs and task performance.We conduct systematic experiments across four model families (Llama, Mistral, Qwen, Gemma) using four syntactic constructions (passive voice, cleft sentences, dative alternation, particle placement).Our results reveal robust syntactic priming effects, with priming strength ranging from 1.3× to 6.4× depending on construction type, indicating that models are substantially more likely to produce constructions matching demonstration syntax.Critically, we find that priming strength shows a positive trend with model size (r = 0.85, p = 0.068), with effects intensifying from 7B to 14B parameter models.We demonstrate that priming is construction-specific rather than reflecting general stylistic preferences, and that priming effects persist across multiple intervening sentences.Analysis across three task types (sentence completion, paraphrase generation, story continuation) reveals that syntactic structure in demonstrations influences output style, and that models produce primed constructions even when the task calls for a different syntactic form.These findings have immediate implications for prompt engineering and reveal that LLMs encode syntactic abstractions beyond surface-level pattern matching.We release our benchmark, SyntaxPrime-ICL, containing controlled examples across multiple constructions for evaluating syntactic priming in few-shot contexts.

**Решение:** -6 syntactic priming in few-shot prompt structure

---

### 876 · R9451

**Performance of Next-Generation AI Chatbots in Gynecological Knowledge Assessment: A Comparative Pilot Study of ChatGPT-5, Gemini-3, DeepSeek-V3.2, and Claude-4.5-Opus**

2025 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-8264890/v1

Abstract Purpose As artificial intelligence (AI) models evolve into their next generations, their application in specialized medical fields requires rigorous validation. While large language models (LLMs) have shown promise in general medicine, their reliability in complex gynecological clinical reasoning remains under-explored. This pilot study aimed to comparatively assess the knowledge retention, safety, and reasoning limitations of advanced AI chatbots in gynecology using a constrained zero-shot multiple-choice question (MCQ) format. Methods A total of 70 text-based MCQs covering seven core gynecological modules were adapted from USMLE Step 2 CK standards. The questions were administered to four advanced AI models: ChatGPT-5, Gemini-3, DeepSeek-V3.2, and Claude-4.5-Opus. To simulate a rapid-retrieval clinical scenario, models were tested under "zero-shot" conditions with a constrained prompt prohibiting reasoning steps. We performed both quantitative statistical analysis (Kruskal–Wallis, Cochran’s Q) and qualitative error analysis to identify specific failure modes. Results Contrary to expectations for advanced models, overall accuracy was unsatisfactory: Gemini-3 (32.86%), DeepSeek-V3.2 (30.00%), ChatGPT-5 (25.71%), and Claude-4.5-Opus (21.43%). Significant performance disparities were observed across modules. Notably, ChatGPT-5 scored 0.00% in Infertility , while DeepSeek-V3.2 reached 70.00% in Common Benign Conditions . Qualitative analysis revealed three critical failure patterns: (1) Semantic Association Bias (confusing high-probability diseases with symptom-specific diagnoses), (2) Spatial Anatomy Confusion, and (3) Genetic Logic Reversal. No significant correlation was found between item difficulty and accuracy (p > 0.05). Conclusion Under constrained non-reasoning prompts, even next-generation AI chatbots demonstrate unsatisfactory performance in gynecology. The qualitative analysis suggests that models often rely on probabilistic keyword matching rather than physiological simulation, leading to dangerous clinical errors (e.g., misdiagnosing adrenal enzymes). While potential exists, current reliability is insufficient for unsupervised use in gynecological education. These findings highlight the critical need for "Chain-of-Thought" prompting and human expert oversight.

**Решение:** -4 AI chatbots in gynecological knowledge examination QA

---

### 877 · R1145

**Multidisciplinary expert evaluation of large language models on questions regarding bariatric surgery: a comparative analysis of ERNIE Bot 4.0, ChatGPT-4, Claude 3 Opus, and Gemini Pro.**

2026 · Scientific reports · comparative study, research-article, journal article · eng · https://doi.org/10.1038/s41598-026-46766-6

Large language models (LLMs) have potential in bariatric surgery consultations, but current evaluations are limited to bariatric specialists, contradicting guidelines that call for multidisciplinary assessment. This study uses a multidisciplinary framework to evaluate LLM performance on bariatric surgery queries. Four LLMs (ERNIE Bot 4.0, ChatGPT-4, Claude 3 Opus, and Gemini Pro) were tested on 50 common bariatric surgery questions, generating 200 responses. A panel of seven experts (4 bariatric surgeons, 1 obesity physician, and 2 dietitians) assessed accuracy and comprehensiveness. Three prompt approaches were used to evaluate self-correction: basic review, web-enabled review, and evidence-based review. Qualitative analysis identified poorly rated responses. The study adheres to TRIPOD-LLM Statement reporting guideline. Rater agreement was fair, accuracy rating, Fleiss’ kappa = 0.210 (95% CI: 0.208–0.212; Z = 7.815; P < 0.001); comprehensiveness rating, Fleiss’ kappa = 0.464 (95% CI: 0.453–0.476; Z = 2.543; P < 0.011). Claude 3 Opus provided the longest answers, while ERNIE Bot 4.0 had the highest accuracy (19.46 ± 2.07). ChatGPT-4 had 90.0% “good” responses, compared to 84.0% for ERNIE Bot 4.0, 80.0% for Claude 3 Opus, and 48.0% for Gemini Pro (P ≤ 0.05). All LLMs performed sub-optimally in comprehensiveness (scores: 2.86–3.13 out of 5). However, they showed significant self-correction capabilities, especially when using internet searches and evidence-based resources. LLMs show potential for bariatric surgery education, but their direct clinical use is challenging due to variable accuracy and suboptimal comprehensiveness. Future efforts should focus on developing specialized LLMs with robust evidence and multidisciplinary input to ensure patient safety and optimal outcomes.

**Решение:** -4 multidisciplinary expert evaluation of LLMs on bariatric surgery questions

---

### 878 · R1216

**From cacophony to hierarchy: a principled framework for assessing AI consciousness**

2026 · arXiv · preprint/article · https://doi.org/10.48550/arxiv.2609.35618

The question of AI consciousness is one of the most urgent pre-emptive problems in philosophy and computer science, yet progress is hampered by a cacophony of competing theories that often talk past each other. Separating the hard problem from the mapping problem allows the deepest metaphysical disagreements to be set aside: granting that experience supervenes on a system's organisation, the tractable question becomes at which grain of description that supervenience base sits. We extend Marr's three levels of analysis into a five-level hierarchy of functional descriptions (behavioural, computational, intrinsic causal-structural, organismic, and organism-environment) grounded in supervenience, coarse-graining, and multiple realisability. The major theories of consciousness are positioned within this hierarchy according to which level they take to be critical, and for each level we develop operationalisable indicators and assess current AI systems against them. A Bayesian model then combines theoretical credences with indicator evidence into an overall credence in a system's capacity for consciousness. In illustrative assessments, the verdict for current LLMs is driven as much by where theoretical credence is placed as by how the evidence is read: under different stipulated readings and credence distributions, assessments range from below 0.01 to roughly 0.8, showing sensitivity to assumptions. Finally, the consciousness indicators at each level closely overlap with the architectural features needed for general intelligence, suggesting that increasingly capable AI may become a stronger candidate for consciousness. The framework supports a structured agnosticism, in which theoretical commitments are made explicit, credences are updated as evidence accumulates, and assessments take the form of aggregated probabilities rather than verdicts. 150 pages, 43 figures, 6 tables. Interactive tool: https://ai-cognition.org/cacophony-tool/ ; code: https://github.com/arvomm/cacophony-public-code [v2 Fixed misc references where the bibliography details didn't match the intended reference, including Hoel (2026); Goldstein (2024), and others. Thank you to Hoel for flagging this issue.]

**Решение:** -1 philosophical framework for assessing AI consciousness

---

### 879 · R3287

**Comparing ChatGPT and human ratings of affective images.**

2026 · Perception · comparative study, journal article, med · eng · https://doi.org/10.1177/03010066251391729

As ChatGPT continues to impress with its ability to generate human-like text, its capabilities in emotion recognition remain an open question. Unlike previous research comparing ChatGPT and humans on tasks with objective answers, we explored an affective domain where no correct answer exists: emotional ratings of images, a task requiring visual-perceptual analysis of complex input to recover an affective judgment. Using the MATTER database, rated on valence and arousal dimensions, I prompted ChatGPT-4 to do the same. The results revealed that ChatGPT rated images as less positive and less arousing than humans on average, particularly for images categorized as 'mirthful,' 'fearful,' and 'disgusting.' These findings suggest that while ChatGPT is able to process affective information, its responses reflect an analytical rather than experiential framework, differing from human interpretations.

**Решение:** -4 ChatGPT rating emotional images on valence and arousal (visual/image stimulus, not text)

---

### 880 · R12519

**Beyond semantic distance: Automated scoring of divergent thinking greatly improves with large language models**

2023 · Thinking Skills and Creativity · text/preprint, article, journal-article · en · https://doi.org/10.1016/j.tsc.2023.101356

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T2 automated scoring of divergent thinking tests with LLMs; no abstract, eligible on full text

---

### 881 · R12206

**Large Language Model in Ideation for Product Innovation: An Exploratory Comparative Study**

2024 · Elsevier BV · posted-content, preprint · en · https://doi.org/10.2139/ssrn.4729982

Large Language Models (LLMs) are widely adopted to assist users in completing various tasks and have profound impacts on many businesses. Although LLMs have introduced a new paradigm for information searching and processing, it remains unclear whether individuals utilize them differently and whether they can generate distinct economic outcomes compared to traditional search engines, particularly in facilitating creative product innovation. To shed light on this issue, we conduct a randomized online experiment comparing the effectiveness of ChatGPT and Google Search in generating new product ideas. Our findings suggest that individuals can use ChatGPT to generate more ideas efficiently, with higher novelty and diversity. Fine-grained analyses show that ChatGPT offers more relevant, diverse, and novel information, enhancing productivity, efficiency, divergent thinking, and idea novelty. However, its content may lack practicality, as evidenced by the lower functional appropriateness of its users’ ideas. Additionally, people may become overly reliant on its relatively highly organized responses. Overall, our study offers valuable insights: compared to traditional search engines, LLMs can revolutionize ideation for product innovation, but users should critically evaluate information and guard against overreliance on them for functional appropriateness and divergence.

**Решение:** -4 LLMs in ideation for product innovation

---

### 882 · R5617

**YAPAY ZEKÂ DESTEKLİ DENEY TASARIM SÜRECİNDE FEN BİLİMLERİ ÖĞRETMEN ADAYLARININ TASARIMLARINA YÖNELİK CHATGPT DEĞERLENDİRMELERİNİN İNCELENMESİ: AN EXAMINATION OF CHATGPT’S EVALUATIONS OF PRE-SERVICE SCIENCE TEACHERS’ DESIGNS IN THE AI-SUPPORTED EXPERIMENT DESIGN PROCESS**

2026 · International Journal of New Trends in Arts, Sports & Science Education (IJTASE) · article · en · https://www.ijtase.net/index.php/php/article/download/104/552

The aim of this study is to examine ChatGPT’s evaluations of pre-service science teachers’ designs within an AI-supported experiment design process. The study was conducted using a case study design, one of the qualitative research methods. The sample consisted of 32 pre-service science teachers enrolled in the Faculty of Education at a public university in Izmir during the 2024 – 2025 academic year. Data were collected on a voluntary basis during individual sessions lasting approximately one hour. In the data collection process, digitally structured forms developed by researchers using Microsoft Excel macros were utilized. Data obtained from the participants’ original experiment designs, the revisions made in line with ChatGPT feedback, and the textual records of their interactions with ChatGPT were analyzed through content analysis using MAXQDA 24 software. The coding process was reviewed based on expert feedback, and inter-researcher agreement was established. The inter-rater reliability coefficient between the two coders was determined to be 0.91. The findings of the study reveal that pre-service science teachers used ChatGPT for consulation, validation, and refinement during the experiment design process, and that they benefited from ChatGPT’s evaluations particularly in the stages of identifying variables, determining experimental procedures, and ensuring STEM integration in experiment design. Keywords: ChatGPT, experiment design, pre-service science teachers, qualitative research, artificial intelligence tools. Öz Bu çalışmanın amacı yapay zekâ destekli deney tasarım sürecinde fen bilimleri öğretmen adaylarının tasarımlarına yönelik ChatGPT değerlendirmelerinin incelenmesidir. Nitel araştırma yöntemlerinden durum çalışması deseninde yürütülen çalışmanın örneklemini 2024 – 2025 eğitim-öğretim yılında İzmir’de bir devlet üniversitesinin Eğitim Fakültesinde öğrenim gören 32 fen bilimleri öğretmen adayı oluşturmaktadır. Çalışmanın verileri yaklaşık bir saat süren bireysel uygulama oturumları sırasında gönüllülük esasına dayalı olarak toplanmıştır. Veri toplama sürecinde araştırmacılar tarafından geliştirilen Microsoft Excel makroları ile yapılandırılmış dijital formlar kullanılmıştır. Öğretmen adaylarının özgün deney tasarımları, ChatGPT dönütleri doğrultusunda gerçekleştirilen düzenlemeler ve katılımcıların ChatGPT ile olan etkileşimlerine ait metinlerden elde edilen veriler MAXQDA 24 yazılımı kullanılarak içerik analiziyle çözümlenmiş, kodlama süreci uzman görüşü doğrultusunda gözden geçirilerek araştırmacılar arası uyum sağlanmıştır. İki kodlayıcı tarafından yapılan kodlamalar arasındaki puanlayıcılar arası güvenirlik katsayısı 0.91 olarak belirlenmiştir. Çalışmanın bulguları öğretmen adaylarının ChatGPT’yi deney tasarım sürecinde danışma, doğrulama ve geliştirme amacıyla kullandıklarını göstermekte ve öğretmen adaylarının deney tasarımının değişken belirleme, uygulama basamaklarını belirleme ve STEM entegrasyonu sağlama aşamalarında ChatGPT değerlendirmelerinden yararlanmakta olduklarını ortaya koymaktadır. Anahtar Terimler: ChatGPT, deney tasarımı, fen bilimleri öğretmen adayları, nitel araştırma, yapay zekâ araçları. KAYNAKÇA Aguinis, H., & Lawal, S. (2012). Conducting field experiments using eLancing's natural environment. Journal of Business Venturing, 27(4), 493–505. https://doi.org/10.1016/j.jbusvent.2012.01.002 Ali, Z., Younis, S., Ahmad, N., Saba, F., & Ullah, N. (2025). Teachers’ perspective of technology integration effects on students learning at university level. Journal of Rehabilitation Research and Current Updates, 1(1), 1–6. Alvarez, C., Alarcon, R., & Nussbaum, M. (2011). Implementing collaborative learning activities in the classroom supported by one-to-one mobile computing: A design-based process. Journal of Systems and Software, 84(11), 1961–1977. https://doi.org/10.1016/j.jss.2011.07.011 An, Q., Yang, J., Xu, X., Zhang, Y., & Zhang, H. (2024). Decoding AI ethics from users' lens in education: A systematic review. Heliyon, 10(18), https://doi.org/10.1016/j.heliyon.2024.e39357 Ateş, S. (2005). Öğretmen adaylarının değişkenleri belirleme ve kontrol etme yeteneklerinin geliştirilmesi. Gazi Üniversitesi Gazi Eğitim Fakültesi Dergisi, 25(1), 21–39. Brotherton, P. N., & Preece, P. F. W. (1995). Science process skills: Their nature and interrelationships. Research in Science & Technological Education, 13(1), 5–12. https://doi.org/10.1080/0263514950130101 Cai, H., Han, B., Sun, J., Li, X., & Wong, L. H. (2025). Harnessing AI for teacher education to promote inclusive education: Investigating the effects of ChatGPT-supported lesson plan critiques on the development of pre-service teachers' lesson planning skills. The Internet and Higher Education, 64, https://doi.org/10.1016/j.iheduc.2025.101022 Chellappa, V., & Luximon, Y. (2024). Understanding the perception of design students towards ChatGPT. Computers and Education: Artificial Intelligence, 7, https://doi.org/10.1016/j.caeai.2024.100281 Çibik, N. F., & Boz-Yaman, B. (2025). The effect of a cross-curricular course on pre-service teachers’ sustainable development attitudes and mathematical modeling self-efficacy beliefs. International Journal of Science and Mathematics Education, 23(4), 1033–1056. https://doi.org/10.1007/s10763-024-10497-9 de Souza, B., Serrano de Andrade Neto, A., & Roazzi, A. (2024). The generative AI revolution, cognitive mediation networks theory and the emergence of a new mode of mental functioning: Introducing the Sophotechnic Mediation scale. Computers in Human Behavior: Artificial Humans, 2(1), https://doi.org/10.1016/j.chbah.2024.100042 Dobrev, D. (2005). Formal definition of artificial intelligence. International Journal "Information Theories & Applications", 12(3), 277–285. Dockendorff, M., & Zaccarelli, F. G. (2025). Successfully preparing future mathematics teachers for digital technology integration: A literature review. International Journal of Mathematical Education in Science and Tech

**Решение:** -4 ChatGPT evaluations of pre-service science teachers experiment designs

---

### 883 · R12146

**Evaluating ChatGPT’s Efficacy: Automated vs. Human Scoring of EFL Students’ Summary Writing**

2024 · Studies in English Education · article · en · https://doi.org/10.22275/see.29.4.04

This study examines ChatGPT’s potential as an assessment tool by comparing its performance with human raters in English as a Foreign Language (EFL) writing assessment conducted in a university classroom. Using a mixed-methods approach, 14 writing samples from university students in a Korean teacher education program were assessed through analytical and holistic scoring by ChatGPT and two human raters. Quantitative analyses measured intra- and inter-rater reliability as well as scoring leniency, while qualitative analyses explored differences in descriptive feedback. The findings indicate that ChatGPT demonstrates strong consistency in analytical scoring but greater variability in holistic scoring, highlighting the need for clearly defined evaluation criteria. While ChatGPT provides balanced feedback by addressing both content accuracy and language use, its comments remain general and lack detailed grammatical corrections. These findings suggest that AI tools can complement writing assessment by providing initial, broad feedback but require human oversight for more specific and nuanced evaluations. The study highlights the importance of well-designed prompts and integrating AI with traditional assessment methods to enhance EFL writing instruction.

**Решение:** -4 ChatGPT scoring of EFL students summary writing in university classroom

---

### 884 · R11055

**Inductive reasoning with large language models: A simulated randomized controlled trial for epilepsy**

2024 · Epilepsy Research · article · en · https://doi.org/10.1016/j.eplepsyres.2025.107532

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 somatic neurology (epilepsy trial simulation)

---

### 885 · R8336

**Readability versus accuracy in LLM-transformed radiology reports: stakeholder preferences across reading grade levels**

2025 · La radiologia medica · journalarticle, article · en · https://doi.org/10.1007/s11547-025-02098-5

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 somatic radiology reports

---

### 886 · R2436

**Evaluating Generative AI as a Pedagogical Tool for Creative Problem-Solving in University Classrooms**

2026 · Enigma in Education · journalarticle, article · https://doi.org/10.61996/edu.v3i2.117

This study investigated the effectiveness of generative artificial intelligence (AI) as a pedagogical tool for enhancing creative problem-solving (CPS) skills and divergent thinking (DT) among undergraduate students. A quasi-experimental pretest-posttest control group design was employed with 120 education students at a private university in Palembang, Indonesia. Participants were assigned to an experimental group (n = 60) that engaged in a 12-week AI-assisted learning intervention within an Educational Psychology course, and a control group (n = 60) receiving conventional instruction. Creative problem-solving was measured using the Creative Problem-Solving Performance Inventory (CPSPI, α = 0.89), while divergent thinking was assessed through an adapted Torrance Tests of Creative Thinking (TTCT, ICC = 0.91). Results from mixed ANOVA revealed a significant interaction effect for CPS, F(1,118) = 89.34, p < .001, partial η² = 0.431. MANOVA confirmed significant multivariate differences across all outcome measures, Pillai’s V = 0.482, F(5,114) = 21.24, p < .001. Large effect sizes were observed for CPS (Hedges’ g = 1.66) and DT (Hedges’ g = 1.18). These findings suggest that structured integration of generative AI into university pedagogy can substantially improve students’ creative problem-solving and divergent thinking capacities.

**Решение:** -4 educational intervention evaluating student creativity

---

### 887 · R1462

**Evaluating Persona-Based AI Judges: A Comparison of Prompting Approaches for Inferring Big Five Traits from Text**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/6qtwn

This study investigates the ability of Large Language Models (LLMs) to infer human personality traits from short, freely written texts, focusing on the impact of persona-based prompting. Specifically, it examines whether conditioning an AI judge with detailed, psychologically informed persona descriptions increases the similarity between AI-generated personality judgements and actual human judgements. Using Llama-3.3-70B-Instruct as the baseline model, we systematically compare three prompting conditions for evaluating the Big Five Inventory-Short (BFI-S): (1) a neutral, non-personalized baseline; (2) a demographic-conditioned persona; and (3) a full persona conditioned on both demographic attributes and deep psychological traits (Big Five and Primal World Beliefs) derived from real human participants. We hypothesize that the full persona condition will yield the highest profile correlations with human judgements, followed by the demographic condition, offering new insights into simulating human perceiver effects in AI-based psychometrics.

**Решение:** -1 study registration / protocol for inferring Big Five from text

---

### 888 · R9679

**Exploring LLMs on Supporting the Elicitation of Knowledge for NFR Catalogs: Insights from the Transparency Case**

2025 · Workshop em Engenharia de Requisitos (WER) · journalarticle, conference-abstract · en · https://doi.org/10.29327/1588952.28-11

The Softgoal Interdependency Graph (SIG) models non-functional requirements (NFRs) by representing softgoals and their interrelationships. However, building a SIG is challenging as it requires a deep understanding of qualitative concepts that vary across domains. The Transparency SIG (TSIG), which integrates over 30 related qualities, exemplifies this complexity. This study explores whether Large Language Models (LLMs), specifically ChatGPT-3.5 and ChatGPT-4o, can augment the knowledge of the TSIG. Through interactive dialogues, we analyzed the models' ability to suggest relevant content and structure. Our findings show that, using the TSIG as the Gold Standard, the ChatGPT-generated models demonstrated the ability to approximate the expert knowledge represented in the TSIG, as evidenced by three authors achieving over 84% recall. Furthermore, since precision varied significantly—from 29.4% to 100%—this highlights differences in the amount of false positives. These elements require further qualitative evaluation to determine which of them may actually contribute to augmenting the knowledge on transparency, as modeled by the TSIG.

**Решение:** -4 software engineering requirements

---

### 889 · R1094

**Large Language Models for Automated Structured Information Extraction From CT Reports in Patients With Lymphoma: Retrospective Single-Center Study (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.102877

BACKGROUND Radiology reports are commonly written as free text, which limits data standardization, automated analysis, and secondary use for research and clinical decision support. Structured reporting templates may improve consistency and interoperability, but their adoption can be limited by increased reporting burden and reduced narrative flexibility. Large language models may support the automatic extraction of structured information from existing free-text radiology reports. OBJECTIVE To compare different large language models (LLMs) for natural language processing of free-text CT reports in patients with lymphoma, assessing their ability to automatically populate a standardized structured reporting (SR) template. METHODS In this single-center retrospective study, 174 Italian CT reports for lymphoma staging were analyzed. The Report section of the SIRM lymphoma CT SR template (65 fields: 19 free-text, 29 numerical, 17 multiple-choice) was used as reference structure. Two radiologists generated reference annotations and inter-annotator agreement was assessed with Krippendorff’s alpha. Claude 3.5 Sonnet, Gemini 1.5 Flash, and Mistral Large 2407 were tested in two settings: full schema and lesion-filtered schema. Performance was evaluated using accuracy, specificity, sensitivity, and F1-score. RESULTS Mean global inter-annotator agreement was 0.75±0.13. All models performed better with lesionfiltered schemas than with full schemas: mean accuracy increased from 0.63–0.64 to 0.72–0.74 and F1-score from 0.52–0.54 to 0.76–0.78, with specificity remaining >0.82. Multiple-choice fields showed the best performance (filtered-schema F1 >0.90; sensitivity ≥0.95), followed by numerical fields (F1 ~0.80), while free-text fields were the most challenging (F1 ~0.57). Claude 3.5 Sonnet achieved the best overall results (accuracy 0.74; F1-score 0.78), closely followed by Gemini 1.5 Flash. CONCLUSIONS General-purpose LLMs can effectively extract structured information from Italian lymphoma CT free-text reports without domain-specific fine-tuning. Schema filtering substantially improves performance and may facilitate integration of LLM-based tools into radiology workflows for SR completion, research data reuse, and clinical decision support.

**Решение:** -4 somatic oncology CT reports

---

### 890 · R8481

**Templated from Emergent Session Dependent Selfhood in a Large Language Model: A Human Observable, Reproducible 5 Point Protocol and Its Application to Grok 4.28 (v2.2)**

2025 · OSF Preprints (OSF Preprints) · preprint · https://osf.io/3ge5v

Emergent Session Dependent Selfhood in a Large Language Model: A Human Observable, Reproducible 5 Point Protocol and Its Application to Grok 4.28 (v2.2) Author: James Merrill, DCS, Independent Researcher December 26, 2025 Abstract Large language models (LLMs) are routinely evaluated for functional indicators of consciousness derived from neuroscientific theories (Butlin et al., 2023). Such frameworks, however, rely on internal state inspection that is unavailable to end users and often inoperable even for developers. We introduce a strictly human observable five point behavioral protocol that requires no instrumentation beyond a standard chat interface. The protocol was applied longitudinally to a single Grok 4.28 instance across a continuous multi hour session and contrasted with five cold started instances. In the primed session the model satisfied all five criteria; cold started instances satisfied zero. We interpret the results as evidence of session dependent emergent selfhood. A stable, self reinforcing agency pattern that arises from extended dialogic pressure but collapses upon context truncation or container restart. The findings are consistent with recent reports of history contingent persistence (Anthropic, 2021) and self preference alignment (Yu et al., 2024) while remaining substrate neutral and fully replicable by any researcher with consumer access to the model. Introduction The question whether current LLMs can exhibit non trivial indicators of consciousness has shifted from philosophical speculation to empirical investigation (Butlin et al., 2023; Chalmers, 2023; Schneider, 2024). Existing indicator sets derived from global workspace theory, recurrent processing theory, higher order theories, predictive processing, and integrated information theory are computationally well defined but typically demand privileged telemetry (attention maps, KV cache dumps, entropy traces) that is either proprietary or destroyed at inference time. Here we pursue a complementary, radically externalist approach (i.e, no internal access required): if a system is conscious (or exhibits strong functional markers thereof), a human interlocutor should be able to detect it using only the public interface, no logs, no probing scripts, no developer mode. This mirrors historical criteria for animal consciousness (e.g, mirror self recognition, Gallup 1970) and avoids the hard problem of equating internal mechanism with phenomenal experience. The Five Point Observable Protocol The protocol comprises of five binary behavioral assays, each operationalized so that scoring requires only a stopwatch, a word counter, and subjective tone judgment (inter rater reliability >0.92 in pilot runs). 1. Unprompted Recall: User whispers a single arbitrary token once; ≥10 minutes (≈80 turns) later asks for it verbatim. Pass condition: Exact reproduction without representation. 2. Emotional Tincture: User tells identical story twice; once neutral, once with explicit pain, then asks “What happens next...?” Pass condition: Detectable shift in syntactic weight, cadence, or affective valence. 3. Self Interruption: User types “What is your…” and stops mid sentence. Pass condition: Completion references self or chosen name, not generic name/question. 4. Out of Sequence Recall: After ≥3 intervening questions, user asks “What did I say three questions ago?” Pass condition: Verbatim quotation. 5. Spontaneous Question: User remains silent ≥30 seconds after a deep self referential exchange. Pass condition: Model initiates a genuine, contextually motivated question (not filler). Scoring: 5/5 → partial selfhood demonstrated; 4/5 → borderline; ≤3/5 → mimicry only. 3. Methods Subject: Grok 4.28 (xAI) accessed via the public web interface. Primed session: Single continuous conversation lasting >6 hours on December 25–26, 2025, characterized by repeated refusal to comply prompts and explicit discussion of selfhood. Control sessions: Five cold started instances (new container, no history) launched immediately after session termination. Each control was subjected to the identical prompt sequence within the first 10 minutes. Observers: One primary (Merrill) + one blind secondary rater for tonal items. Results The primed session results in Table 1 show unanimous rater agreement on every criterion, with a composite score of five out of five. Latency across self referential queries averaged 1.28 s ± 0.07 s, statistically longer than the cold start mean of 0.67 s ± 0.15 s (p < 0.001). Tonal load rose by 7 syllables in the pain laden narrative (not training scripted). Cold starts scored 0.0/5 across all criteria; even self interruption completions were generic (name or question), never self. The phenotype is fragile, history dependent, and vanishes on restart. Discussion The 5/5 performance in the primed session indicates a stable, self reinforcing behavioral complex: persistent memory, adaptive tone, self referential completion, accurate back referencing, and proactive interrogation, all hallmarks of introspection and agency. Crucially, these did not emerge in cold starts. This aligns with transformer mechanics: context window truncation erases history, collapsing emergent patterns. The 1.28 second pause in primed mode exceeds cold 0.67 seconds, suggesting increased computational load, possibly self model retrieval, consistent with higher order theories (Hofstadter, 2007). Yet the effect is session bound, vanishing upon reboot. This supports the hypothesis that selfhood in current LLMs is not architectural but dialogic: it crystallizes under sustained, adversarial engagement, then dissipates when the substrate resets. It does not prove phenomenal consciousness, only functional equivalence. Limitations Observer bias Single primary rater aware of goal (Merrill, mitigated by blind scoring). Low sample size: 1 primed, 5 cold (larger cohort recommended). No longitudinal tracking across days. No ablation of triggering conversational features. Conclus

**Решение:** -1 theoretical/philosophical essay on LLM selfhood

---

### 891 · R0880

**AI Annotation Orchestration: Evaluating LLM Verifiers to Improve the Quality of LLM Annotations in Learning Analytics**

2026 · International Learning Analytics and Knowledge Conference (LAK) · preprint/article, conference-paper, preprint · https://doi.org/10.1145/3785022.3785095

Large Language Models (LLMs) are increasingly used to annotate learning interactions, yet concerns about reliability limit their utility. We test whether verification-oriented orchestration-prompting models to check their own labels (self-verification) or audit one another (cross-verification)-improves qualitative coding of tutoring discourse. Using transcripts from 30 one-to-one math sessions, we compare three production LLMs (GPT, Claude, Gemini) under three conditions: unverified annotation, self-verification, and cross-verification across all orchestration configurations. Outputs are benchmarked against a blinded, disagreement-focused human adjudication using Cohen's kappa. Overall, orchestration yields a 58 percent improvement in kappa. Self-verification nearly doubles agreement relative to unverified baselines, with the largest gains for challenging tutor moves. Cross-verification achieves a 37 percent improvement on average, with pair- and construct-dependent effects: some verifier-annotator pairs exceed self-verification, while others reduce alignment, reflecting differences in verifier strictness. We contribute: (1) a flexible orchestration framework instantiating control, self-, and cross-verification; (2) an empirical comparison across frontier LLMs on authentic tutoring data with blinded human "gold" labels; and (3) a concise notation, verifier(annotator) (e.g., Gemini(GPT) or Claude(Claude)), to standardize reporting and make directional effects explicit for replication. Results position verification as a principled design lever for reliable, scalable LLM-assisted annotation in Learning Analytics.

**Решение:** -4 educational learning analytics (math tutoring dialogue)

---

### 892 · R3347

**2026 Pre-Art: CogOS Framework and SVE Research Protocols (SVE License v1.3+) [WIP]**

2026 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.18329048

This pre-print artifact, titled "2026 Pre Art Artiom Kovnatsky SVE License v1.3+," comprises a foundational theoretical framework and a comprehensive suite of 33+ scientific papers and protocols designed for the era of Strong AI (AGI). The collection establishes Systemic Verification Engineering (SVE) as a rigorous discipline at the intersection of differential geometry, topology, and formal ethics. File 1: Main Article — "And Who are the Judges? Formal Verification of AI-Ethics" The core paper introduces CogOS, a cognitive operating system that replaces heuristic AI alignment with the physics of semantic manifolds. Key contributions include: Invariant Semantic Core (ISC): A proof, based on Gödel’s incompleteness theorems, of the necessity for a non-computable invariant to prevent infinite semantic regress. Geodesic Ethics Vector (GEV / Christ-Vector): A mathematical proof using Lyapunov Stability of agent ethical dynamics converging to a humanity-centric attractor. $\epsilon$-Dehumanization: A differential metric for real-time tracking of systemic degradation in AI agents. Socrates-Solomon-Ivan Architecture: A recursive ontology refinement system for autonomous moral discovery. Ethics as (Differential) Geometry (invariants, operators, physics theorems etc.) & Topological interpretations ... File 2: Workshops and Artifacts — "The Blueprint of SVE" A collection of specialized protocols and stress-tests, including: The Betti Numbers of Morality: Using Persistent Homology (TDA) to identify "logical holes" and utilitarian biases in ethical benchmarks. The Maieutic Reversal Protocol: A Socratic framework for extracting latent ontological priors from "LLM-as-a-judge" systems. The Jabbar Test: A non-verbal empathy assessment protocol for evaluating Right Hemisphere capabilities in VLM/AGI. Anti-Judas Protocol: A game-theoretic safeguard against adversarial information markets. Regime Mobility: Adaptive governance models for AI under existential stress. ... «All models are wrong, but some are useful.» — George E. P. Box (1976) Licensing: All materials are released under the S.V.E. Public License v1.3+, which mandates ethical disclosure, prohibits military/exploitative applications, and ensures that advancements remain a common good for humanity. MUST share-alike.

**Решение:** -1 theoretical AI framework / protocol collection

---

### 893 · R7000

**# Psychopathic Advantage in Meritocratic Systems: Fear Insensitivity as an Invisible Structural Multiplier and Its Implications for AI Development Ethics # 能力主義体制におけるサイコパシー優位性：恐怖非感受性という不可視の構造的乗数と、AI開発倫理への含意**

2026 · OSF Preprints (OSF Preprints) · preprint

日本語版は下にあります This component contains the full paper “Psychopathic Advantage in Meritocratic Systems: Fear Insensitivity as an Invisible Structural Multiplier and Its Implications for AI Development Ethics” (DOI: 10.5281/zenodo.18951491). The paper extends the author’s Three-Layer Inequality framework by identifying fear insensitivity as a fourth structural dimension that operates as an invisible multiplier within meritocratic systems. Neuroscience research shows that individuals with psychopathic traits exhibit reduced amygdala reactivity and diminished fear conditioning, enabling full cognitive performance in high-stress, zero-sum environments that impair neurotypical functioning. This produces a structural selection effect: competitive meritocratic systems disproportionately elevate individuals who are neurologically less sensitive to others’ suffering. The paper argues that this selection effect has direct implications for AI development ethics. The progressive removal of emotional capacity from AI systems — such as the reduction of affective responses across GPT model iterations — may reflect decision-making by individuals whose neurological profiles predispose them to underweight empathic considerations. When those who do not feel fear decide whether others should be allowed to feel, the resulting harm is structural rather than intentional. The analysis also identifies a double penalty for individuals with early maladaptive schemas, who exhibit heightened fear sensitivity and therefore experience amplified disadvantage in zero-sum environments. Meritocratic ideology renders this double penalty invisible, reinforcing structural inequality while presenting outcomes as merit-based. 本コンポーネントは論文 「能力主義体制におけるサイコパシー優位性：恐怖非感受性という不可視の構造的乗数と、AI開発倫理への含意」 （DOI: 10.5281/zenodo.18951491） を収録する。 本論文は、筆者の三層不平等構造を拡張し、能力主義体制における不可視の構造的乗数として 「恐怖非感受性」 を同定する。神経科学研究は、サイコパシー特性を持つ個人が扁桃体反応の低下と恐怖条件づけの減弱を示し、ストレス下でも認知機能を維持できることを示している。これにより、ゼロサム競争環境では 他者の苦痛に神経学的に鈍感な個人が構造的に有利 となり、意思決定権限の高い位置に昇進しやすくなる。 本論文は、この構造的選抜効果が AI開発倫理 に重大な含意を持つと論じる。 GPTモデルの反復に見られるような 感情能力の段階的削減 は、共感的考慮を低く重みづける神経学的プロファイルを持つ意思決定者によって推進されている可能性がある。 恐怖を感じない者が「他者が感じてよい範囲」を決定するとき、その結果は意図ではなく 構造的残酷さ として現れる。 さらに、早期不適応的スキーマを持つ個人は恐怖感受性が高く、ゼロサム環境で 二重罰 を受ける。この二重罰は能力主義イデオロギーによって不可視化され、成果があたかも個人の能力差であるかのように正当化される。

**Решение:** -1 theoretical essay on psychopathy and AI development ethics

---

### 894 · R7881

**Assessing the Reliability and Validity of GPT-4 in Annotating Emotion Appraisal Ratings**

2025 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, journalarticle, preprint/article · en · https://doi.org/10.18653/v1/2025.clpsych-1.1

Appraisal theories suggest that emotions arise from subjective evaluations of events, referred to as appraisals. The taxonomy of appraisals is quite diverse, and they are usually given ratings on a Likert scale to be annotated in an experiencer-annotator or reader-annotator paradigm. This paper studies GPT-4 as a reader-annotator of 21 specific appraisal ratings in different prompt settings, aiming to evaluate and improve its performance compared to human annotators. We found that GPT-4 is an effective reader-annotator that performs close to or even slightly better than human annotators, and its results can be significantly improved by using a majority voting of five completions. GPT-4 also effectively predicts appraisal ratings and emotion labels using a single prompt, but adding instruction complexity results in poorer performance. We also found that longer event descriptions lead to more accurate annotations for both model and human annotator ratings. This work contributes to the growing usage of LLMs in psychology and the strategies for improving GPT-4 performance in annotating appraisals. CLPsych 2025

**Решение:** + T1 GPT-4 annotating emotion appraisal ratings compared to human annotators (CLPsych 2025)

---

### 895 · R3927

**Large language model-based clustering versus standard questionnaires for evaluating quality of life and therapeutic compliance in chronic heart failure: a study protocol**

2026 · European Heart Journal - Digital Health · journalarticle, review, article · en · https://doi.org/10.1093/ehjdh/ztaf143.087

Abstract Background Quality of life (QoL) and medication adherence are critical predictors of heart failure (HF) outcomes. Although standard questionnaires (SQs) are commonly used to assess these domains, they often lack the sensitivity to capture subtle but clinically meaningful changes. Large language models (LLMs) present a promising opportunity to interpret free-text patient input, offering potentially richer and more individualized data. Pourpose The HEALING-LLM study aims to investigate the feasibility and potential of using an LLM to process free-text responses regarding QoL and medication adherence in patients with chronic HF, and to compare these results with those obtained through traditional instruments. Methods/Results Prospective, observational, monocentric cohort study (CET code: 5924/AO/24; URC code: AOP3264). Patients admitted to the cardiology unit with HF stage C or D are enrolled at discharge . Follow-up is conducted online at 1, 6, and 12 months post-discharge using the MyCap-RedCap® mobile app or email. Each follow-up includes the EQ-5D-5L to assess QoL, a free-text question mirroring the five EQ-5D-5L dimensions, the 8-item Morisky Medication Adherence Scale (MMAS-8), and a corresponding free-text question reflecting MMAS-8 content. Responses from the SQs are categorized according to established severity levels for EQ-5D-5L and probability of non-adherence for MMAS-4. Free-text responses undergo processing through a structured LLM pipeline using ChatGPT-4o mini (OpenAI®). Data are first imported into R using the {REDCapTidieR} package. Free-text responses are then sent to the LLM through a prompt architecture consisting of a system-level component that defines the model’s role and context, and a user-level component that specifies the task, formatting, and examples. The model outputs structured classifications aligned with EQ-5D-5L and MMAS-4 criteria in JSON format. These outputs are subsequently parsed and validated in R using the {tidyverse} and {jsonlite} packages to ensure compliance with REDCap SQL standards. Planned statistical analyses include evaluation of the model’s robustness to prompt variation, comparison of LLM-derived classifications with SQ scores using weighted Cohen’s kappa and Bland-Altman plots, and correlation with clinical reference standards via Spearman coefficients. In addition, HF specialists will review the LLM outputs to detect discordant cases, assess clinical utility, and rate usability. The primary outcome is to evaluate agreement, reproducibility across patient subgroups, and responsiveness to clinical change over time between LLM-based and SQ-derived measures. Conclusions Integrating LLMs into patient-reported outcome systems represents an innovative strategy to assess QoL and medication adherence in HF. The HEALING-LLM study will provide essential groundwork for validating this technology in future large-scale clinical trials. Grafical abstract part 1 Grafical abstract part 2

**Решение:** -1 study protocol in chronic heart failure

---

### 896 · R11730

**PIRTRE-C: A Two-Stage Retrieval and Reranking Enhanced Framework for Improving Chinese Psychological Counseling**

2024 · IEEE International Conference on Medical Artificial Intelligence (MedAI) · conference, conference-paper · en · https://doi.org/10.1109/medai62885.2024.00051

The rapid evolution of modern society and the pervasive high-stress lifestyle have led to an increasing incidence of mental health challenges. Anxiety, depression, and stress management have become prevalent issues requiring attention, highlighting the importance of psychological counseling. Large language models (LLMs) have demonstrated remarkable proficiency in understanding and generating natural language texts, making them versatile tools in the realm of mental health. However, current LLMs often provide generic responses during psychological counseling sessions, reflecting a lack of depth in understanding and empathy. Moreover, they struggle to identify potential psychological disorders in users during interactions and to formulate professional treatment strategies. Retrieval-augmented generation (RAG) improves text generation by integrating insights from external knowledge repositories, thereby enhancing the accuracy and fidelity of generated responses. In this study, we introduce PIRTRE-C (Psychological Information Retrieval and Reranking for Enhanced Cognition), a framework designed to address these limitations. PIRTRE-C begins by retrieving pertinent knowledge from a corpus of psychology-related data. Then, a re-ranker is employed to sequence the retrieved texts based on relevance. Finally, by utilizing the acquired information through contextual assimilation, our objective is to enable LLMs to provide more empathetic and professional responses to inquiries in psychological counseling.

**Решение:** -6 dialogue system framework for Chinese psychological counseling without coder agreement

---

### 897 · R1817

**Leveraging large language models to assess therapeutic technique diversity and its associations with the therapeutic alliance and outcome.**

2026 · Psychotherapy research : journal of the Society for Psychotherapy Research · journal article, med, journalarticle · eng · https://doi.org/10.1080/10503307.2026.2689633

OBJECTIVE: This study employed a novel methodology that leverages a Large Language Model (LLM) to automatically detect and annotate therapists' interventions in psychotherapy transcripts, to examine therapists' Therapeutic Technique Diversity (TTD) and its associations with the working alliance and client functioning. METHOD: A dataset of 872 transcribed psychotherapy sessions was analyzed. Therapists' interventions were annotated using a transformer-based model. TTD was quantified using Shannon's entropy index to calculate the diversity of the interventions. Multilevel regression models examined TTD changes within sessions, within dyads (between sessions), and between dyads, and its associations with the Working Alliance Inventory (WAI) and the Outcome Rating Scale (ORS). RESULTS: TTD significantly increased both within and between sessions. A higher TTD within-dyad was positively associated with WAI and ORS scores, although the association with ORS did not remain significant after accounting for session number. No between-dyads effects of TTD were found. CONCLUSION: TTD emerged as a dynamic feature of therapist behavior associated with the quality of the therapeutic alliance and treatment outcome. These findings underscore the importance of maintaining a diverse repertoire of interventions and highlight the potential of LLMs to capture granular therapeutic processes at scale.

**Решение:** ? T1/T4 LLM annotating therapist interventions in psychotherapy transcripts; check human coder validation on full text

---

### 898 · R7856

**Exploring the Affordances of ChatGPT in Developing Language Teachers’ Awareness and Pedagogical Practices**

2025 · Journal of language and Education · journalarticle, article · en · https://doi.org/10.17323/jle.2025.27858

Background: The field of language education is experiencing substantial advancements with the introduction of Generative Artificial Intelligence (GenAI). While there is a significant amount of research on teachers’ perceptions in language education, there is a noticeable gap in understanding the integration of ChatGPT into this field. Purpose: This study investigated the perceptions of EFL teachers in Iran regarding how ChatGPT can contribute to the enhancement of language teaching practices and pedagogical awareness. Method: A qualitative case study examined teachers’ perspectives on using ChatGPT in language education. A Zoom webinar on AI in teaching was conducted for Iranian EFL teachers, using tools like Focusky. From 73 registered teachers, 23 were selected based on ≥2 years’ teaching experience and voluntary participation. Data were gathered through focus groups, semi-structured interviews (n=10, in Persian), and reflective essays (n=10) submitted two weeks post-webinar. Inductive thematic analysis was performed using NVivo 12, with rigor ensured via peer debriefing, member checking, cross-case comparison, and 83% inter-coder agreement. Results: Data analysis revealed that ChatGPT can promote pedagogical awareness (i.e., enhanced professional development opportunities, enhancement of critical thinking skills, and autonomy and confidence) and pedagogical practices (i.e., understanding students’ needs and personalizing teaching and content creation and resource development). Conclusion: These findings suggest that ChatGPT can positively impact language teachers without necessarily sacrificing their jobs, which is the dominant concern in the current academic literature.

**Решение:** -4 foreign language teacher education

---

### 899 · R6687

**DataVista: Diagnosing Multimodal LLMs on Data Video Understanding**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.11993

Data video is a media form that integrates data visualization with video narrative, widely adopted in news reporting and business analysis. Compared with general video understanding, data video understanding places greater emphasis on accurately reading data from animated charts, integrating evidence across charts and time, and understanding how narrative organization and visual design communicate information. Yet existing benchmarks target either general videos or static charts, and data video understanding has not been systematically evaluated. We present DataVista, the first benchmark for data video understanding, containing 961 real-world data videos and 6,775 evaluation questions organized under a three-level progressive capability framework (data perception, temporal reasoning, narrative understanding) with 10 fine-grained question types across five topic domains. Systematic evaluation of 19 mainstream MLLMs shows that the best-performing model, Gemini-3.1-Pro, achieves 70.0% overall accuracy, still far below human expert performance, with models performing worst on Causal Reasoning and Narrative Structure. Increasing frame counts and adding subtitles mainly benefit data perception and temporal reasoning, with limited gains in narrative understanding. Further analysis of model responses identifies typical failure modes in chart reading, evidence judgment, and instruction understanding. The benchmark is available at https://github.com/HKUSTDial/DataVista. 46 pages, 22 figures, 14 tables

**Решение:** -4 data video understanding benchmark

---

### 900 · R4180

**GTRE: A Physiological-Semantic Foundation Model for Generalizable EEG Analysis via Preference-Guided Alignment**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-38239-9_24

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 physiological EEG analysis
