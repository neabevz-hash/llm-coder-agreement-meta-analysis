# Проверка с метками ИИ, часть 9

Записи 1201–1304 из 1304, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы. Последние 30 — калибровочные записи, где ваша слепая метка разошлась с правилом ИИ: она показана над метками.

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

### 1201 · R9332

**Preprocessing Large-Scale Conversational Datasets: A Framework and Its Application to Behavioral Health Transcripts.**

2025 · JMIR formative research · journal article, journalarticle, review · eng · https://doi.org/10.2196/78082

Abstract Background The rise of artificial intelligence and accessible audio equipment has led to a proliferation of recorded conversation transcripts datasets across various fields. However, automatic mass recording and transcription often produce noisy, unstructured data that contain unintended recordings such as hallway conversations, media (eg, TV, radio), or transcription inaccuracies as speaker misattribution or misidentified words. As a result, large conversational transcript datasets require careful preprocessing and filtering to ensure their research utility. This challenge is particularly relevant in behavioral health contexts (eg, therapy, counseling) where deriving meaningful insights, specifically dynamic processes, depends on accurate conversation representation. Objective We present a framework for preprocessing large datasets of conversational transcripts and filtering out non-sessions—transcripts that do not reflect a behavioral treatment session but instead capture unrelated conversations or background noise. This framework is applied to a large dataset of behavioral health transcripts from community mental health clinics across the United States. Methods Our approach integrated basic feature extraction, human annotation, and advanced applications of large language models (LLMs). We began by mapping transcription errors and assessing the number of non-sessions. Next, we extracted statistical and structural features to characterize transcripts and detect outliers. Notably, we used LLM perplexity as a measure of comprehensibility to assess transcript noise levels. Finally, we used zero-shot prompting with an LLM to classify transcripts as sessions or non-sessions, validating its output against expert annotations. Throughout, we prioritized data security by selecting tools that preserve anonymity and minimize the risk of data breaches. Results Initial assessment revealed that transcription errors—such as incomprehensible segments, unusually short transcripts, and speaker diarization issues—were present in approximately one-third (n=36 out of 100) of a manually reviewed sample. Statistical outliers revealed that high speaking rate (>3.5 words per second) is associated with short transcripts and answering machine messages, while short conversation duration (<15 min) was an indicator for case management sessions. The 75th percentile of LLM perplexity scores was significantly higher in non-sessions than sessions (permutation test mean difference = −258, P =.02), although this feature alone offered only moderate classification performance (precision =0.63, recall =0.23 after outlier removal). In contrast, zero-shot LLM prompting effectively distinguished sessions from non-sessions with high agreement to expert ratings (κ=0.71) while also capturing the nature of the meeting. Conclusions This study’s hybrid approach effectively characterizes errors, evaluates content, and distinguishes text types within unstructured conversational dataset. It provides a foundation for research on conversational data, key methods, and practical guidelines that serve as crucial first steps in ensuring data quality and usability, particularly in the context of mental health sessions. We highlight the importance of integrating clinical experts with artificial intelligence tools while prioritizing data security throughout the process.

**ИИ:** ? · обе модели · неясен конструкт · LLM classified therapy transcripts as session vs non-session against expert annotations (κ=0.71); unclear whether this is a psychological construct.

**Решение:** =

---

### 1202 · R9336

**The Homework Wars: Exploring Emotions, Behaviours, and Conflicts in Parent-Child Homework Interactions**

2025 · Proceedings of the ACM on Interactive Mobile Wearable and Ubiquitous Technologies · journalarticle, review, preprint/article · en · https://doi.org/10.1145/3749517

Parental involvement in homework is a crucial aspect of family education, but it often triggers emotional strain and conflicts. Despite growing concern over its impact on family well-being, prior research has lacked access to fine-grained, real-time dynamics of these interactions. To bridge this gap, we present a framework that leverages naturalistic parent-child interaction data and large language models (LLMs) to analyse homework conversations at scale. In a four-week in situ study with 78 Chinese families, we collected 475 hours of audio recordings and accompanying daily surveys, capturing 602 homework sessions in everyday home settings. Our LLM-based pipeline reliably extracted and categorised parental behaviours and conflict patterns from transcribed conversations, achieving high agreement with expert annotations. The analysis revealed significant emotional shifts in parents before and after homework, 18 recurring parental behaviours and seven common conflict types, with Knowledge Conflict being the most frequent. Notably, even well-intentioned behaviours were significantly positively correlated with specific conflicts. This work advances ubiquitous computing methods for studying complex family dynamics and offers empirical insights to enrich family education theory and inform more effective parenting strategies and interventions in the future. This paper was accepted by Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies (IMWUT)

**ИИ:** + · обе модели · кодирование по кодбуку · An LLM pipeline categorised parental behaviours and conflicts in transcribed parent-child conversations, with high agreement against expert annotations.

**Решение:** =

---

### 1203 · R9346

**Can generative AI assess PTSD? A clinical validation study of transcribed and direct audio input modalities.**

2025 · BMJ digital health & AI · journal article, journalarticle, article · eng · https://doi.org/10.1136/bmjdhai-2025-000042

Objective: Post-traumatic stress disorder (PTSD) remains underdiagnosed due to barriers such as limited access to mental health professionals and resource constraints. While generative artificial intelligence (AI) shows potential in mental health applications, little information is available on its ability to assess PTSD, particularly through direct audio input. We aimed to examine the ability of three AI-based input modalities to support clinical diagnosis of PTSD: Claude 3.5 Sonnet with transcribed input, Gemini 1.5 Pro with transcribed input and Gemini 1.5 Pro with direct audio input. Methods and analysis: Participants were adults with trauma histories who completed clinical interviews. Both generative AI and clinicians produced continuous severity scores and binary diagnoses. For diagnostic prediction, AI-generated severity scores were compared with binary clinician diagnoses using receiver operating characteristic curve analysis to compute area under the curve (AUC). Reliability between AI and clinician severity scores was evaluated using intraclass correlation coefficients (ICCs). Accuracy was calculated by comparing AI-generated diagnoses to clinician-rated diagnoses. Results: The study included 53 participants (mean age=36.9 years, SD=10.6); 47 were female (88.7%). 37 participants (69.8%) met PTSD criteria based on clinician diagnosis. AUCs, ICCs and accuracies (95% CIs) were: Claude transcribed input, 0.94 (0.87 to 1.00), 0.82 (0.71 to 0.92) and 0.89 (0.78 to 0.95); Gemini transcribed input, 0.93 (0.85 to 1.00), 0.83 (0.73 to 0.90) and 0.85 (0.74 to 0.93); Gemini direct audio input, 0.93 (0.84 to 1.00), 0.89 (0.81 to 0.93) and 0.80 (0.68 to 0.90). Conclusions: Generative AI may support PTSD diagnosis and expand access to care. Future applications should be developed with an emphasis on privacy-preserving deployment.

**ИИ:** + · обе модели · клиническая оценка · Claude and Gemini rated PTSD severity from clinical interview transcripts; ICC with clinician severity ratings reported.

**Решение:** =

---

### 1204 · R9351

**Leveraging ASR and LLMs for Automated Scoring and Feedback in Children's Spoken Language Assessments**

2025 · Slate · https://doi.org/10.21437/slate.2025-1

This paper explores the use of automatic speech recognition (ASR) and large language models (LLMs) for automated scoring and feedback generation in spoken language assessment. We design a three stage pipeline that (1) optimizes ASR hypotheses from student speech, (2) performs task-based scoring using LLMs, and (3) generates natural language feedback jus-tifying each score. We evaluate this pipeline using audio responses from 3rd-8th grade students in the Atlanta, Georgia area, recorded as part of the Test of Narrative Language. Our results show that LLMs can reliably replicate expert annotations while providing interpretable feedback. We further analyze model performance across demographic factors, including dialect and reading proficiency, to assess equity. Our findings demonstrate the promise of ASR and LLMs for robust, explain-able, and fair assessment of children’s spoken narratives.

**ИИ:** ? · обе модели · неясен конструкт · LLM scores children's Test of Narrative Language responses against expert annotations; unclear if narrative language ability counts as a psychological construct.

**Решение:** =

---

### 1205 · R9366

**An AI-Supported Methodology for Identifying Attachment Styles**

2025 · medRxiv · preprint, ppr · en · https://doi.org/10.1101/2025.08.30.25334439

Abstract Identifying attachment styles is important for clinical psychologists interested in better understanding their patients. Traditional methods for identifying attachment styles rely on clinical interviews or questionnaires, which are time-consuming and subject to observer bias. Large Language Models offer potential for automated, objective attachment style analysis. The aim of the paper was to develop and validate an AI-supported methodology for identifying attachment styles using the four-category model. To validate the methodology, we analyzed the narratives of a unique group of subjects who experienced an acute psychological crisis. A LLM was used to analyze each stage using a structured prompt. We hypothesized that if the methodology validly identifies attachment styles, the fearful style would be the most prevalent in the descriptions of the subjects’ insecure childhood and crises. The methodology successfully identified the theoretically predicted attachment styles. Chi-square analyses confirmed significant deviations from the null hypothesis across all stages with a strong effect size. In sum, the AI-supported attachment analysis offers an objective, efficient alternative to traditional methods while maintaining theoretical validity. The methodology demonstrates potential clinical utility for rapid assessment of attachment dynamics, though further validation across diverse populations is warranted.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM codes attachment styles in crisis narratives; validated against theoretical predictions, and the abstract mentions no human coder comparison.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): LLM classifies attachment style in narratives, validated against theoretical prevalence (chi-square), not against human coders' labels of the same texts.)

**Решение:** -

---

### 1206 · R9377

**Comparing Human Expertise and Large Language Models Embeddings in Content Validity Assessment of Personality Tests**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2503.12080

In this article we explore the application of Large Language Models (LLMs) in assessing the content validity of psychometric instruments, focusing on the Big Five Questionnaire (BFQ) and Big Five Inventory (BFI). Content validity, a cornerstone of test construction, ensures that psychological measures adequately cover their intended constructs. Using both human expert evaluations and advanced LLMs, we compared the accuracy of semantic item-construct alignment. Graduate psychology students employed the Content Validity Ratio (CVR) to rate test items, forming the human baseline. In parallel, state-of-the-art LLMs, including multilingual and fine-tuned models, analyzed item embeddings to predict construct mappings. The results reveal distinct strengths and limitations of human and AI approaches. Human validators excelled in aligning the behaviorally rich BFQ items, while LLMs performed better with the linguistically concise BFI items. Training strategies significantly influenced LLM performance, with models tailored for lexical relationships outperforming general-purpose LLMs. Here we highlights the complementary potential of hybrid validation systems that integrate human expertise and AI precision. The findings underscore the transformative role of LLMs in psychological assessment, paving the way for scalable, objective, and robust test development methodologies.

**ИИ:** разошлись — Opus ? (другое: Embedding-based mapping of personality items to constructs vs. human CVR ratings; models are probably encoder-only, and it is unclear whether direct agreement is reported.); Sonnet -5 (нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM: Embedding-based (encoder-style) models map personality test items to constructs, compared with student CVR ratings. This is item validation, not generative LLM coding of psychological text.)

**Решение:** -

---

### 1207 · R9382

**L3Cube-MahaEmotions: A Marathi Emotion Recognition Dataset with Synthetic Annotations using CoTR prompting and Large Language Models**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2506.00863

Emotion recognition in low-resource languages like Marathi remains challenging due to limited annotated data. We present L3Cube-MahaEmotions, a high-quality Marathi emotion recognition dataset with 11 fine-grained emotion labels. The training data is synthetically annotated using large language models (LLMs), while the validation and test sets are manually labeled to serve as a reliable gold-standard benchmark. Building on the MahaSent dataset, we apply the Chain-of-Translation (CoTR) prompting technique, where Marathi sentences are translated into English and emotion labeled via a single prompt. GPT-4 and Llama3-405B were evaluated, with GPT-4 selected for training data annotation due to superior label quality. We evaluate model performance using standard metrics and explore label aggregation strategies (e.g., Union, Intersection). While GPT-4 predictions outperform fine-tuned BERT models, BERT-based models trained on synthetic labels fail to surpass GPT-4. This highlights both the importance of high-quality human-labeled data and the inherent complexity of emotion recognition. An important finding of this work is that generic LLMs like GPT-4 and Llama3-405B generalize better than fine-tuned BERT for complex low-resource emotion recognition tasks. The dataset and model are shared publicly at https://github.com/l3cube-pune/MarathiNLP

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT-4 and Llama3 labelled fine-grained emotions in Marathi text and were evaluated against a manually labelled gold-standard test set.

**Решение:** =

---

### 1208 · R9384

**Investigation of the Inter-Rater Reliability between Large Language Models and Human Raters in Qualitative Analysis**

2025 · Physics Education Research Conference (PERC) · conference, review, preprint/article · en · https://doi.org/10.1119/perc.2025.pr.borse

Qualitative analysis is typically limited to small datasets because it is time-intensive. Moreover, a second human rater is required to ensure reliable findings. Artificial intelligence tools may replace human raters if we demonstrate high reliability compared to human ratings. We investigated the inter-rater reliability of state-of-the-art Large Language Models (LLMs), ChatGPT-4o and ChatGPT-4.5-preview, in rating audio transcripts coded manually. We explored prompts and hyperparameters to optimize model performance. The participants were 14 undergraduate student groups from a university in the midwestern United States who discussed problem-solving strategies for a project. We prompted an LLM to replicate manual coding, and calculated Cohen's Kappa for inter-rater reliability. After optimizing model hyperparameters and prompts, the results showed substantial agreement ($κ&gt;0.6$) for three themes and moderate agreement on one. Our findings demonstrate the potential of GPT-4o and GPT-4.5 for efficient, scalable qualitative analysis in physics education and identify their limitations in rating domain-general constructs. 7 pages, 4 figures, Physics Education Research Conference 2025

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o coded student group discussion transcripts against manual coding (Cohen's kappa); unclear if codes capture psychological constructs or education content.

**Решение:** =

---

### 1209 · R9396

**From incident to organisational response - a mixed-methods study of police officers’ needs and expectations following exposure to potentially traumatic events**

2025 · Police Practice and Research · article · en · https://doi.org/10.1080/15614263.2025.2608186

Police officers are at considerable risk of developing post-traumatic stress disorder (PTSD) as they are consistently exposed to a wide array of potentially traumatic events (PTE). Effective organisational strategies for the management of this mental health risk have been the subject of research and some have been implemented in police organisations. This study aims to identify the experiences, needs and expectations of police officers in terms of post-incident interventions following exposure to a PTE. In a mixed-methods design, we first conducted a survey in 107 police officers from four different Belgian police units to determine trauma exposure and evaluate past experiences with three commonly used post-incident interventions: individual counselling, operational debriefing and psychological debriefing. We then conducted focus groups with 13 of the trauma-exposed police officers to explore the needs and expectations of this population following a PTE. The transcripts were analysed using codebook thematic analysis by human coders, supported by a Large Language Model (LLM). A large majority of 87.9% of participating police officers reported traumatic exposure. Post-incident interventions were not routinely offered following traumatic incidents, and while some interventions were evaluated positively, the current organisational approach does not seem to adequately meet the needs of Belgian police officers. While most police officers felt supported by their colleagues, officers report a lack of support from both their supervisors and the wider police institution. Focus group discussions reveal the need for a well-structured, proactive and comprehensive post-incident approach, addressing psychological, operational and administrative needs of trauma-exposed police officers. Given the role of police culture in discouraging help-seeking, it is vital that police leadership leads efforts to normalize the impact of traumatic events. The findings of the current study indicate that a comprehensive set of post-incident interventions is required to address the needs and expectations of trauma-exposed police personnel.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM supported codebook thematic analysis of police trauma focus groups; unclear whether LLM–human coding agreement was reported.

**Решение:** =

---

### 1210 · R9397

**Automatic implicit motive codings are at least as accurate as humans' and 99% faster.**

2025 · Journal of personality and social psychology · journal article, journalarticle, review · eng · https://doi.org/10.1037/pspp0000544

Implicit motives, nonconscious needs that influence individuals' behaviors and shape their emotions, have been part of personality research for nearly a century but differ from personality traits. The implicit motive assessment is very resource-intensive, involving expert coding of individuals' written stories about ambiguous pictures, and has hampered implicit motive research. Using large language models and machine learning techniques, we aimed to create high-quality implicit motive models that are easy for researchers to use. We trained models to code the need for power, achievement, and affiliation ( N = 85,028 sentences). The person-level assessments converged strongly with the holdout data, intraclass correlation coefficient, ICC(1,1) = .85, .87, and .89 for achievement, power, and affiliation, respectively. We demonstrated causal validity by reproducing two classical experimental studies that aroused implicit motives. We let three coders recode sentences where our models and the original coders strongly disagreed. We found that the new coders agreed with our models in 85% of the cases ( p < .001, ϕ = .69). Using topic and word embedding analyses, we found specific language associated with each motive to have a high face validity. We argue that these models can be used in addition to, or instead of, human coders. We provide a free, user-friendly framework in the established R-package text and a tutorial for researchers to apply the models to their data, as these models reduce the coding time by over 99% and require no cognitive effort for coding. We hope this coding automation will facilitate a historical implicit motive research renaissance. (PsycInfo Database Record (c) 2025 APA, all rights reserved).

**ИИ:** ? · обе модели · другое · Implicit motive story coding compared with expert coders; the 'large language models' may be encoder embeddings (R text package), not generative LLMs.

**Решение:** =

---

### 1211 · R9401

**The Alternative Annotator Test for LLM-as-a-Judge: How to Statistically Justify Replacing Human Annotators with LLMs**

2025 · Annual Meeting of the Association for Computational Linguistics (ACL) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2025.acl-long.782

The "LLM-as-an-annotator" and "LLM-as-a-judge" paradigms employ Large Language Models (LLMs) as annotators, judges, and evaluators in tasks traditionally performed by humans. LLM annotations are widely used, not only in NLP research but also in fields like medicine, psychology, and social science. Despite their role in shaping study results and insights, there is no standard or rigorous procedure to determine whether LLMs can replace human annotators. In this paper, we propose a novel statistical procedure, the Alternative Annotator Test (alt-test), that requires only a modest subset of annotated examples to justify using LLM annotations. Additionally, we introduce a versatile and interpretable measure for comparing LLM annotators and judges. To demonstrate our procedure, we curated a diverse collection of ten datasets, consisting of language and vision-language tasks, and conducted experiments with six LLMs and four prompting techniques. Our results show that LLMs can sometimes replace humans with closed-source LLMs (such as GPT-4o), outperforming the open-source LLMs we examine, and that prompting techniques yield judges of varying quality. We hope this study encourages more rigorous and reliable practices.

**ИИ:** разошлись — Opus ? (неясен конструкт: Methods paper comparing LLM and human annotators across ten datasets; some may involve psychological constructs (e.g., emotional-support responses). Needs full-text check.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: General methodological paper on LLM-as-annotator statistical testing across generic NLP/vision-language datasets; no specific psychological or clinical construct.)

**Решение:** -

---

### 1212 · R9403

**Rethinking Emotion Annotations in the Era of Large Language Models.**

2025 · IEEE transactions on affective computing · journal article, journalarticle, preprint/article · eng · https://doi.org/10.1109/taffc.2025.3584775

Modern affective computing systems rely heavily on datasets with human-annotated emotion labels for both training and evaluation. However, human annotations are expensive to obtain, sensitive to study design, and difficult to quality control, because of the subjective nature of emotions. Meanwhile, Large Language Models (LLMs) have shown remarkable performance on many Natural Language Understanding tasks, emerging as a promising tool for text annotation. In this work, we analyze the complexities of emotion annotation in the context of LLMs, focusing on GPT-4 as a leading model. In our experiments, GPT-4 achieves high ratings in a human evaluation study, painting a more positive picture than previous work, in which human labels served as the only ground truth. On the other hand, we observe differences between human and GPT-4 emotion perception, underscoring the importance of human input in annotation studies. To harness GPT-4's strength while preserving human perspective, we explore two ways of integrating GPT-4 into emotion annotation pipelines, showing its potential to flag low-quality labels, reduce the workload of human annotators, and improve downstream model learning performance and efficiency. Together, our findings highlight opportunities for new emotion labeling practices and suggest the use of LLMs as a promising tool to aid human annotation.

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT-4 annotates emotion in text and is compared against human emotion labels; human evaluation also included.

**Решение:** =

---

### 1213 · R9408

**ChatGPT in Research: Variable Extraction and Researcher Protection in the Context of Child Sexual Abuse**

2025 · BCE Official Conference Proceedings · conference · https://doi.org/10.22492/issn.2435-9467.2024.79

In the context of research on childhood sexual abuse (CSA), researchers face significant challenges due to the emotionally distressing nature of sensitive data (Williamson et al., 2020). The use of ChatGPT (OpenAI, 2023) offers valuable support in this area. This artificial intelligence (AI) tool facilitates efficient data processing while maintaining emotional distance by converting qualitative content into quantifiable formats. This approach not only aids in statistical analysis but also reduces the emotional burden on researchers (van Manen, 2023). The inter-coder reliability of this method has been evaluated and largely confirmed in various forms (Naranjos Velazquez, 2024; in press). In a comparative study, the results of AI models ChatGPT 3.5, ChatGPT 4 and ChatGPT 4o were analysed. Increased consistency was observed beginning with the ChatGPT 4 model, further highlighting the reliability of ChatGPT in processing sensitive information. This presentation explores the ethical and practical implications of AI use in research and discusses the limitations of this AI tool (Naranjos Velazquez, 2023 a ; in press).

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · ChatGPT coded child sexual abuse qualitative data into variables and inter-coder reliability is mentioned, but it may be only consistency across model versions.

**Решение:** =

---

### 1214 · R9410

**Decoding Student Minds: Leveraging Conversational Agents for Psychological and Learning Analysis**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2512.10441

This paper presents a psychologically-aware conversational agent designed to enhance both learning performance and emotional well-being in educational settings. The system combines Large Language Models (LLMs), a knowledge graph-enhanced BERT (KG-BERT), and a bidirectional Long Short-Term Memory (LSTM) network with attention to classify students' cognitive and affective states in real time. Unlike prior chatbots limited to either tutoring or affective support, our approach leverages multimodal data-including textual semantics, prosodic speech features, and temporal behavioral trends-to infer engagement, stress, and conceptual understanding. A pilot study with 45 university students demonstrated improved motivation, reduced stress, and moderate academic gains compared to unimodal baselines. We explicitly discuss the exploratory nature of this small-sample pilot, report effect sizes and inter-rater reliability alongside significance tests, and provide an ablation analysis isolating the contribution of the knowledge-graph component and of each modality. These results underline the promise-while acknowledging the current limits in scale and modality balance-of integrating semantic reasoning, multimodal fusion, and temporal modeling to support adaptive, student-centered educational interventions.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: Hybrid LLM/KG-BERT/LSTM system classifies student stress and engagement and reports inter-rater reliability; unclear whether the LLM's labels are compared with human labels.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: A conversational agent system combining an LLM with KG-BERT and LSTM classifiers, tested in a pilot study. The abstract doesn't describe an LLM coding task checked against human coders.)

**Решение:** -

---

### 1215 · R9411

**Natural Language Processing and Generative AI in the Automated Scoring and Feedback of Reflective Writing in Medical Education: A Validity and Fairness Analysis**

2025 · Research Square · preprint, ppr · en · https://doi.org/10.21203/rs.3.rs-6636682/v1

Abstract The study explored the application of Natural Language Processing (NLP) and generative AI tools in assessing reflective writing submitted by medical students in Ghana. It evaluated the validity, fairness, and cultural alignment of AI-generated feedback by comparing AI-generated scores with human rater assessments and analyzing demographic group discrepancies. A total of 180 reflective essays were sampled, with an equal number (n = 60) collected from each university . Quantitative methods included Cohen’s Kappa and Intraclass Correlation Coefficients (ICC) to assess inter-rater agreement, while logistic regression and multiple regression models examined potential biases across gender, university affiliation, and English proficiency. Qualitative data were gathered through interviews with students and faculty to explore perceptions of fairness, trust, and the AI’s capacity to capture cultural and linguistic nuances. Results indicated that the AI system demonstrated strong inter-rater reliability, with Cohen’s Kappa values of 0.74 (AI vs Rater 1) and 0.76 (AI vs Rater 2), and ICC values of 0.78 and 0.80, respectively. Human raters showed higher agreement with each other (Cohen’s Kappa = 0.81, ICC = 0.85). However, significant discrepancies were found across demographic groups, particularly for English proficiency, where lower proficiency students tended to receive higher AI scores than human raters (log-odds of 0.45, p = 0.001). Thematic analysis of qualitative interviews revealed concerns over the lack of empathy in AI feedback, misalignment with cultural and linguistic nuances, and mixed levels of trust in AI-generated assessments. These findings suggest that while AI holds promise for improving efficiency in assessment, careful attention must be given to its limitations in fairness and cultural sensitivity. The study concluded with recommendations for improving AI systems through contextual adaptation, hybrid assessment models, faculty training, and regular bias audits to ensure equitable and effective use of AI in educational settings.

**ИИ:** ? · обе модели · неясен конструкт · Generative AI scored medical students' reflective essays against human raters (kappa reported); unclear if reflection rubric counts as a psychological construct.

**Решение:** =

---

### 1216 · R9441

**Of Humans and Machines: Evaluating the Efficacy of GPT-4 in Coding Discourse Data**

2025 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-12229-2_8

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; GPT-4 vs human coding of discourse data, but unclear whether the construct is psychological (possibly educational discourse).

**Решение:** =

---

### 1217 · R9448

**Using machine learning to automate the collection, transcription, and analysis of verbal-report data.**

2025 · Behavior research methods · journal article, journalarticle, preprint · eng · https://doi.org/10.3758/s13428-025-02800-5

What people think and say during experiments is important for our understanding of the human mind. However, the collection and analysis of verbal-report data in experiments are relatively costly and are thus grossly underutilized. Here, we aim to reduce such costs by providing software that collects, transcribes, and analyzes verbal-report data. Verbal data are collected using jsPsych (De Leeuw, Behavior Research Methods, 47, 1-12, 2015), making it suitable for both online and lab-based experiments. The transcription and analyses rely on classical machine-learning methods as well as deep learning approaches (e.g., large language models), making them substantially more efficient than current methods using human coders. We demonstrate how to use the software we provide in a case study via a simple memory experiment. This collection of software was designed to be modular, allowing for the update and replacement of various components with superior models, as well as the easy addition of new methods. It is our sincere hope that this approach popularizes the collection of verbal-report data in psychology experiments.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLMs analyse verbal reports from a memory experiment, a cognitive construct; the abstract doesn't say whether results were checked against human coders.

**Решение:** =

---

### 1218 · R9457

**Gold Standard**

2025 · OSF Preprints (OSF Preprints) · preprint · https://osf.io/38m7v

his component contains the manually coded transcripts, codebook, and methodology documentation used to construct the gold standard thematic analysis for evaluating AI models in qualitative research. The analysis follows the Braun & Clarke (2003) framework and serves as a benchmark for assessing the performance of QualBot and other LLMs.

**ИИ:** ? · обе модели · неясен конструкт · OSF component: human-coded transcripts and codebook as a benchmark for LLMs. The topic, whether it is psychological, and whether coding is unit-level or theme-level are all unclear.

**Решение:** =

---

### 1219 · R9475

**Cognitive-Mental-LLM: Evaluating Reasoning in Large Language Models for Mental Health Prediction via Online Text**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2503.10095

Large Language Models (LLMs) have demonstrated potential in predicting mental health outcomes from online text, yet traditional classification methods often lack interpretability and robustness. This study evaluates structured reasoning techniques-Chain-of-Thought (CoT), Self-Consistency (SC-CoT), and Tree-of-Thought (ToT)-to improve classification accuracy across multiple mental health datasets sourced from Reddit. We analyze reasoning-driven prompting strategies, including Zero-shot CoT and Few-shot CoT, using key performance metrics such as Balanced Accuracy, F1 score, and Sensitivity/Specificity. Our findings indicate that reasoning-enhanced techniques improve classification performance over direct prediction, particularly in complex cases. Compared to baselines such as Zero Shot non-CoT Prompting, and fine-tuned pre-trained transformers such as BERT and Mental-RoBerta, and fine-tuned Open Source LLMs such as Mental Alpaca and Mental-Flan-T5, reasoning-driven LLMs yield notable gains on datasets like Dreaddit (+0.52\% over M-LLM, +0.82\% over BERT) and SDCNL (+4.67\% over M-LLM, +2.17\% over BERT). However, performance declines in Depression Severity, and CSSRS predictions suggest dataset-specific limitations, likely due to our using a more extensive test set. Among prompting strategies, Few-shot CoT consistently outperforms others, reinforcing the effectiveness of reasoning-driven LLMs. Nonetheless, dataset variability highlights challenges in model reliability and interpretability. This study provides a comprehensive benchmark of reasoning-based LLM techniques for mental health text classification. It offers insights into their potential for scalable clinical applications while identifying key challenges for future improvements. 8 pages, 4 Figures, 3 tables

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: LLMs classify Reddit posts on Dreaddit, Depression Severity and CSSRS, benchmarks labelled by crowd workers or clinicians; accuracy and F1 against those labels.); Sonnet ? (неясно, кто ставил эталонные метки: LLM classification of Reddit mental-health posts (Dreaddit, CSSRS, etc.); labels may be human-annotated or subreddit/self-reported, so the reference source is unclear.)

**Решение:** +

---

### 1220 · R9476

**Extracting social support and social isolation information from clinical psychiatry notes: comparing a rule-based natural language processing system and a large language model.**

2025 · Journal of the American Medical Informatics Association : JAMIA · comparative study, research support, non-u.s. gov't, research-article · eng · https://doi.org/10.1093/jamia/ocae260

OBJECTIVES: Social support (SS) and social isolation (SI) are social determinants of health (SDOH) associated with psychiatric outcomes. In electronic health records (EHRs), individual-level SS/SI is typically documented in narrative clinical notes rather than as structured coded data. Natural language processing (NLP) algorithms can automate the otherwise labor-intensive process of extraction of such information. MATERIALS AND METHODS: Psychiatric encounter notes from Mount Sinai Health System (MSHS, n = 300) and Weill Cornell Medicine (WCM, n = 225) were annotated to create a gold-standard corpus. A rule-based system (RBS) involving lexicons and a large language model (LLM) using FLAN-T5-XL were developed to identify mentions of SS and SI and their subcategories (eg, social network, instrumental support, and loneliness). RESULTS: For extracting SS/SI, the RBS obtained higher macroaveraged F1-scores than the LLM at both MSHS (0.89 versus 0.65) and WCM (0.85 versus 0.82). For extracting the subcategories, the RBS also outperformed the LLM at both MSHS (0.90 versus 0.62) and WCM (0.82 versus 0.81). DISCUSSION AND CONCLUSION: Unexpectedly, the RBS outperformed the LLMs across all metrics. An intensive review demonstrates that this finding is due to the divergent approach taken by the RBS and LLM. The RBS was designed and refined to follow the same specific rules as the gold-standard annotations. Conversely, the LLM was more inclusive with categorization and conformed to common English-language understanding. Both approaches offer advantages, although additional replication studies are warranted.

**ИИ:** + · обе модели · клиническая оценка · Generative FLAN-T5-XL (encoder-decoder) extracts social support, isolation and loneliness from psychiatric notes; compared with human-annotated gold standard.

**Решение:** =

---

### 1221 · R9478

**A framework for the initial phases of personality test development using large language models and artificial personas**

2025 · Journal of Research in Personality · article · en · https://doi.org/10.1016/j.jrp.2025.104647

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: From the title, LLMs generate test items and simulate respondents; nothing suggests they code or rate text against humans. No abstract.); Sonnet ? (нет аннотации: No abstract; LLM/artificial personas for personality test development, likely item generation and simulated responses, but a human comparison is unclear.)

**Решение:** ?

---

### 1222 · R9484

**Combining Human and Automated Coders in Psychological Research: A Case Study on the Use of GPT in the Analysis of Heuristics and Bias in Text**

2025 · OSF Preprints (OSF Preprints) · preprint · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus + (кодирование по кодбуку: No abstract, but the title describes GPT and human coders coding heuristics and biases in text, a cognitive construct, so agreement is likely reported.); Sonnet ? (нет аннотации: No abstract; the title suggests GPT coding of heuristics and bias in text compared with human coders, so the full text should be checked.)

**Решение:** +

---

### 1223 · R9493

**From Data to Dataset: A Framework for Working with Behavioral Treatment Transcripts (Preprint)**

2025 · preprint · en · https://doi.org/10.2196/preprints.78082

BACKGROUND The rise of AI and accessible audio equipment has led to a proliferation of recorded conversation transcripts datasets across various fields. However, automatic mass recording and transcription often produce noisy, unstructured data. First, these datasets naturally include unintended recordings, such as hallway conversations, background noise and media (e.g., TV programs, radio, phone calls). Second, automatic speech recognition (ASR) and speaker diarization errors can result in misidentified words, speaker misattributions, and other transcription inaccuracies. As a result, large conversational transcript datasets require careful preprocessing and filtering to ensure their research utility. This challenge is particularly relevant in behavioral health contexts (e.g., therapy, treatment, counselling): while these transcripts offer valuable insights into patient-provider interactions, therapeutic techniques, and client progress, they must accurately represent the conversations to support meaningful research. OBJECTIVE We present a framework for preprocessing and filtering large datasets of conversational transcripts and apply it to a dataset of behavioral health transcripts from community mental health clinics across the United States. Within this framework we explore tools to efficiently filter non-sessions – transcripts of recordings in these clinics that do not reflect a behavioral treatment session but instead capture unrelated conversations or background noise. METHODS Our framework integrates basic feature extraction, human annotation, and advanced applications of large language models (LLMs). We begin by mapping transcription errors and assessing the distribution of sessions and non-sessions. Next, we identify key features to analyze how outliers help in characterizing the type of transcript. Notably, we use LLM perplexity as a measure of comprehensibility to assess transcript noise levels. Finally, we use zero-shot LLM prompting to classify transcripts as sessions or non-sessions, validating LLM decisions against expert annotations. Throughout, we prioritize data security by selecting tools that preserve anonymity and minimize the risk of data breaches. RESULTS Our findings demonstrated that basic statistical outliers, such as speaking rate, are associated with transcription errors and are observed more frequently in non-sessions versus sessions. Specifically, LLM perplexity can flag fragmented and non-verbal segments and is generally lower in sessions (permutation test mean difference = -258, p<0.05), thus can serve as a filtering aiding tool. Additionally, LLM algorithms have shown an ability to distinguish between sessions and non-sessions with high validity (κ=0.71), while also capturing the nature of the meeting. CONCLUSIONS This study’s hybrid approach effectively characterizes errors, evaluates content, and distinguishes different text types within unstructured conversational datasets. It provides a foundation for research on conversational data, providing key methods and practical guidelines that serve as crucial first steps in ensuring data quality and usability, particularly in the context of mental health sessions. We highlight the importance of integrating clinical experts with AI tools while prioritizing data security throughout the process.

**ИИ:** ? · обе модели · неясен конструкт · Zero-shot LLM sorted behavioral-health transcripts into sessions and non-sessions; expert agreement κ=0.71. It's unclear whether this is a psychological construct.

**Решение:** =

---

### 1224 · R9500

**Exploring biases related to the use of large language models in a multilingual depression corpus.**

2025 · Scientific reports · journal article, journalarticle, article · eng · https://doi.org/10.1038/s41598-025-19980-x

Recent advancements in Large Language Models (LLMs) present promising opportunities for applying these technologies to aid the detection and monitoring of Major Depressive Disorder. However, demographic biases in LLMs may present challenges in the extraction of key information, where concerns persist about whether these models perform equally well across diverse populations. This study investigates how demographic factors, specifically age and gender affect the performance of LLMs in classifying depression symptom severity across multilingual datasets. By systematically balancing and evaluating datasets in English, Spanish, and Dutch, we aim to uncover performance disparities linked to demographic representation and linguistic diversity. The findings from this work can directly inform the design and deployment of more equitable LLM-based screening systems. Gender had varying effects across models, whereas age consistently produced more pronounced differences in performance. Additionally, model accuracy varied noticeably across languages. This study emphasizes the need to incorporate demographic-aware models in health-related analyses. It raises awareness of the biases that may affect their application in mental health and suggests further research on methods to mitigate these biases and enhance model generalization.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs classify depression symptom severity in multilingual text; unclear whether reference labels are clinician/human ratings or self-report scores.

**Решение:** =

---

### 1225 · R9531

**Large language model evaluating theory of mind tasks in a gamified environment**

2025 · Research Square · preprint, ppr, posted-content · https://doi.org/10.21203/rs.3.rs-6944626/v1

Abstract Autism Spectrum Disorder often significantly affects reciprocal social communication, leading to difficulties in inter-preting social cues, recognizing emotions, and maintaining verbal interactions. These challenges can make everydayconversations especially demanding. To support people with Autism Spectrum Disorder in developing their socialcompetence and communication abilities, we propose an interactive game specifically designed to enhance socialunderstanding. By incorporating gamification elements and a user-centered design approach, the application aimsto balance clinical relevance with high usability, ensuring it remains accessible, engaging, and beneficial for anyoneseeking to improve their social skills.Large Language Models have recently been assessed for their ability to detect sarcasm and irony within theory of mindtasks, showing performance comparable to that of trained psychologists. However, a significant limitation remains: theirdependence on traditional "black box" AI architectures, which often lack explainability, interpretability, and transparency.This limitation is particularly concerning when people with and without Autism Spectrum Disorder use these models tolearn and practice social skills in safe, virtual environments.This study investigates and compares the performance of Large Language Models and human experts in evaluatingTheory of Mind tasks, providing a detailed comparative analysis. A total of 21 participants engaged with our game, andtheir responses were assessed by four human experts alongside GPT-4o. The results indicate that GPT-4o matcheshuman experts in both adherence to instructional criteria and evaluation accuracy, with no statistically significantdifferences observed. These findings underscore the potential of LLMs to support scalable, always-available socialtraining systems that are accessible from anywhere.

**ИИ:** + · обе модели · подсчёт методики · GPT-4o scored participants' theory-of-mind task responses and was compared with four human experts on evaluation accuracy.

**Решение:** =

---

### 1226 · R9540

**The effectiveness of a sentence completion test for depression screening using large language models.**

2025 · Acta psychologica · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.actpsy.2025.105425

Depressive symptoms pose a significant mental health challenge globally, including in Thailand. The aim of this study was to assess the effectiveness of a sentence completion test for depression using large language models (LLMs). To improve objectivity and reduce bias in assessments, this study detects and classifies the trends in depression, modernizing the screening process with a newly developed depression sentence completion test. This research examines the four key areas: 1) family, 2) society, 3) health, and 4) self-concept among 373 participants, aged 20 to 40. Additionally, four models were applied to test: 1) LLAMA 3.1-8B, 2) Gemma2-9B, 3) Qwen2-7B, and 4) Typhoon1.5-7B. The result revealed that health, self-concept, and DIFF (Difference) were strongly related to sentiment levels with strong positive values of 0.48, 0.49, and 0.54, respectively, which might mean that they are significant indicators of depression risk. Family and society had positive but lower values of 0.27 and 0.19, respectively. Statistical validation confirms model reliability with a 0.78 lower bound accuracy (p ≤ .05). In the evaluation of all Thai-compatible LLMs, random forest models consistently performed better than decision tree classifiers in the classification of depression risk. LLaMA3.1 and Gemma2 produced the highest sensitivity. Ethical problems have to be considered when using LLMs in mental health. Embedding diverse populations and dynamic updating to sample data in future studies will assure greater accuracy and generalization across different demographic groups.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs score sentence completion test responses for depression; unclear whether the reference is human scoring or a self-report criterion.

**Решение:** =

---

### 1227 · R9543

**Affordable Audio Hardware and Artificial Intelligence Can Transform the Dementia Care Pipeline**

2025 · Preprints.org · preprint, ppr · https://doi.org/10.20944/preprints202509.0861.v1

Population ageing is increasing dementia care demand. We present an audio-driven monitoring pipeline that operates either on mobile phones, microcontroller nodes, and smart television sets. The system combines audio signal processing with AI tools for structured interpretation. Preprocessing includes voice activity detection, speaker diarization, automatic speech recognition for dialogues, and speech-emotion recognition. An audio classifier detects home-care–relevant events (cough, cane taps, thuds, alarms, speech). A large language model integrates transcripts, acoustic features, and a consented household knowledge base to produce a daily caregiver report covering orientation/disorientation (person, place, time), delusion themes, agitation events, health proxies, and safety flags (e.g., exit seeking, possible fall). The pipeline targets continuous monitoring in homes and facilities and it is an adjunct to caregiving, not a diagnostic device. Evaluation focuses on human-in-the-loop review, inter-rater agreement, and prospective monitoring studies. Intended users are low-income households in remote settings where in-person caregiving cannot be secured, enabling remote monitoring support for older adults with dementia.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM interprets dementia transcripts for disorientation, delusions and agitation; mentions inter-rater agreement, but this may be a system proposal without empirical human comparison.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: System description of an audio monitoring pipeline where an LLM generates caregiver reports. Evaluation is only planned, so there is no reported LLM–human coding agreement.)

**Решение:** -

---

### 1228 · R9549

**A Gold Standard Dataset and Evaluation Framework for Depression Detection and Explanation in Social Media using LLMs**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2507.19899

Early detection of depression from online social media posts holds promise for providing timely mental health interventions. In this work, we present a high-quality, expert-annotated dataset of 1,017 social media posts labeled with depressive spans and mapped to 12 depression symptom categories. Unlike prior datasets that primarily offer coarse post-level labels \cite{cohan-etal-2018-smhd}, our dataset enables fine-grained evaluation of both model predictions and generated explanations. We develop an evaluation framework that leverages this clinically grounded dataset to assess the faithfulness and quality of natural language explanations generated by large language models (LLMs). Through carefully designed prompting strategies, including zero-shot and few-shot approaches with domain-adapted examples, we evaluate state-of-the-art proprietary LLMs including GPT-4.1, Gemini 2.5 Pro, and Claude 3.7 Sonnet. Our comprehensive empirical analysis reveals significant differences in how these models perform on clinical explanation tasks, with zero-shot and few-shot prompting. Our findings underscore the value of human expertise in guiding LLM behavior and offer a step toward safer, more transparent AI systems for psychological well-being.

**ИИ:** + · обе модели · бенчмарк с метками людей · Expert-annotated depression symptom spans in social media posts; GPT-4.1, Gemini, and Claude were evaluated against these expert labels.

**Решение:** =

---

### 1229 · R9558

**Can an Algorithm Tell How Spiritual You Are? Using Generative Pretrained Transformers for Sophisticated Forms of Text Analysis.**

2025 · Journal of personality · journal article, journalarticle, text/article · eng · https://doi.org/10.1111/jopy.13006

Text analysis is a form of psychological assessment that involves converting qualitative information (text) into quantitative data. We tested whether automated text analysis using Generative Pre-trained Transformers (GPTs) can match the "gold standard" of manual text analysis, even when assessing a highly nuanced construct like spirituality.In Study 1, N&thinsp;=&thinsp;2199 US undergraduates wrote about their goals (N&thinsp;=&thinsp;6597 texts) and completed self-reports of spirituality and theoretically related constructs (religiousness and mental health). In Study 2, N&thinsp;=&thinsp;357 community adults wrote short essays (N&thinsp;=&thinsp;714 texts) and completed trait self-reports, 5&thinsp;weeks of daily diaries, and behavioral measures of spirituality. Trained research assistants and GPTs then coded the texts for spirituality.The GPTs performed just as well as human raters. Human- and GPT-generated scores were remarkably consistent and showed equivalent associations with other measures of spirituality and theoretically related constructs.GPTs can match the gold standard set by human raters, even in sophisticated forms of text analysis, but require a fraction of the time and labor.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT and trained research assistants coded the same written texts for spirituality, and the consistency between them is reported.

**Решение:** =

---

### 1230 · R9566

**Supervised Learning and Large Language Model Benchmarks on Mental Health Datasets: Cognitive Distortions and Suicidal Risks in Chinese Social Media.**

2025 · Bioengineering (Basel, Switzerland) · journal article, journalarticle, article · eng · https://doi.org/10.3390/bioengineering12080882

On social media, users often express their personal feelings, which may exhibit cognitive distortions or even suicidal tendencies on certain specific topics. Early recognition of these signs is critical for effective psychological intervention. In this paper, we introduce two novel datasets from Chinese social media: SOS-HL-1K for suicidal risk classification, which contains 1249 posts, and SocialCD-3K, a multi-label classification dataset for cognitive distortion detection that contains 3407 posts. We conduct a comprehensive evaluation using two supervised learning methods and eight large language models (LLMs) on the proposed datasets. From the prompt engineering perspective, we experiment with two types of prompt strategies, including four zero-shot and five few-shot strategies. We also evaluate the performance of the LLMs after fine-tuning on the proposed tasks. Experimental results show a significant performance gap between prompted LLMs and supervised learning. Our best supervised model achieves strong results, with an F1-score of 82.76% for the high-risk class in the suicide task and a micro-averaged F1-score of 76.10% for the cognitive distortion task. Without fine-tuning, the best-performing LLM lags by 6.95 percentage points in the suicide task and a more pronounced 31.53 points in the cognitive distortion task. Fine-tuning substantially narrows this performance gap to 4.31% and 3.14% for the respective tasks. While this research highlights the potential of LLMs in psychological contexts, it also shows that supervised learning remains necessary for more challenging tasks.

**ИИ:** + · обе модели · бенчмарк с метками людей · New Chinese social-media datasets labelled for suicide risk and cognitive distortions; eight LLMs evaluated against the labels, which are presumably from human annotators.

**Решение:** =

---

### 1231 · R9569

**Evaluating Text Creativity across Diverse Domains: A Dataset and Large Language Model Evaluator**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2505.19236

Creativity evaluation remains a challenging frontier for large language models (LLMs). Current evaluations heavily rely on inefficient and costly human judgments, hindering progress in enhancing machine creativity. While automated methods exist, ranging from psychological testing to heuristic- or prompting-based approaches, they often lack generalizability or alignment with human judgment. To address these issues, we propose a novel pairwise-comparison framework for assessing textual creativity that leverages shared contextual instructions to improve evaluation consistency. We introduce CreataSet, a large-scale dataset with 100K+ human-level and 1M+ synthetic creative instruction-response pairs spanning diverse open-domain tasks. Through training on CreataSet, we develop an LLM-based evaluator named CrEval. CrEval demonstrates remarkable superiority over existing methods in alignment with human judgments. Experimental results underscore the indispensable significance of integrating both human and synthetic data to train highly robust evaluators, and showcase the practical utility of CrEval in boosting the creativity of LLMs. Accepted by ICLR 2026

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM evaluator of text creativity checked against human judgments; unclear whether this is a psychological construct (divergent thinking) or writing quality.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM evaluator of creativity in open-domain creative writing responses; not psychological or clinical text or a psychological assessment, despite human-alignment validation.)

**Решение:** -

---

### 1232 · R9571

**Evaluating Machine Translation of Emotion-loaded Chinese User-generated Content**

2025 · University of Surrey · text/doctoral thesis · https://doi.org/10.15126/thesis.901658

In the digital era, people often express their emotions and opinions on social media platforms, generating an enormous volume of emotion-loaded user-generated content (UGC). Given the rapid production and sheer quantity of UGC, machine translation (MT) is the only practical solution for translating this content effectively, as relying solely on human translators is unfeasible. However, the MT community has significantly understudied the quality of MT outputs for these texts, particularly for emotion-loaded Chinese UGC. This research aims to explore the evaluation of machine translation for emotion-loaded Chinese UGC. Utilizing an open-source dataset of microblog posts, the study begins by investigating the challenges faced by professional translators and identifying key issues MT systems encounter, especially with emotion carrying slang created through homophone substitution. The thesis then introduces a human evaluation framework adapted from the well-established error-based Multi-dimensional Quality Metrics (MQM) to manually assess the emotion preservation of MT outputs. The evaluation reveals that approximately 50% of the English translations contain errors related to emotion preservation, underscoring a gap in current MT evaluations. This evaluation process also yields a dataset suitable for training automatic quality estimation (QE) systems without reference translations. Subsequently, the study employs various machine learning techniques, including multi-task learning, in-context learning, and parameter-efficient fine-tuning of large language models (LLMs), to achieve accurate and interpretable evaluations. The performance of these QE systems surpasses existing frameworks in handling emotion-loaded texts. Furthermore, probing these QE systems using perturbed data created by homophone-substituted emotion words demonstrates that fine-tuned LLMs offer more robust and precise evaluations. By uncovering the challenges of translating UGC, proposing an MQM-based evaluation framework, creating a human-annotated QE dataset, and applying machine learning techniques, this research makes significant contributions to the MT evaluation of emotion-loaded Chinese UGC. The study also releases relevant resources to the open-source community for further advancements of this field.

**ИИ:** разошлись — Opus ? (неясен конструкт: Fine-tuned LLMs rate how well translations of Chinese microblogs preserve emotion, checked against human MQM labels. Unclear if this counts as a psychological construct.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Thesis on machine translation quality estimation of emotion-loaded text; LLMs assess translation quality, not coding psychological constructs against human labels.)

**Решение:** -

---

### 1233 · R9576

**Leveraging Large Language Models for Review Classification and Rating Estimation of Mental Health Applications**

2025 · Proceedings of the International AAAI Conference on Web and Social Media · journalarticle, review, conference-paper · en · https://doi.org/10.1609/icwsm.v19i1.35916

Large Language Models (LLMs) can analyze large datasets semantically. However, research on applying LLMs for mental health text classification is relatively new and developing. Existing methods often use supervised, deep, and reinforcement learning, which rely heavily on fine-tuning and reward models. To investigate whether LLMs can assist in recommending mental health apps based on user reviews, our study collected approximately 200k user reviews from 73 mental health mobile applications. We instructed selected LLMs to classify individual reviews into 1-5 star ratings, subsequently averaging these results to derive an overall rating for each app reflecting current user feedback. While the best supervised learning method in our experiments achieved an F1-Score of 0.79 which required significantly more human effort, the GPT-4 and Gemini 1.5 Pro delivered a strong ‘out-of-the-box’ performance with an overall F1-Score of 0.76. We provide further statistical comparisons and discussions of the performance of these models for the text classification task. Using a crowdsourcing platform to determine agreement levels, we observed that human ratings align closely with GPT ratings. In addition, we analyze specific features and concerns highlighted in mental health app reviews. Alongside our analysis, we make our data available for further experimentation and benchmarking.

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs predict star ratings of mental health app reviews, which is product sentiment, not a psychological construct, despite the crowd-worker comparison.); Sonnet ? (неясен конструкт: LLMs rate mental health app reviews (1-5 stars) with crowd human agreement checks; the construct is product-review sentiment, so psychological relevance is borderline.)

**Решение:** -

---

### 1234 · R9579

**Accident investigation via LLMs reasoning: HFACS-guided Chain-of-Thoughts enhance general aviation safety**

2025 · Expert Systems with Applications · article · en · https://doi.org/10.1016/j.eswa.2025.126422

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (неясен конструкт: No abstract. LLM applies HFACS human-error categories to aviation accident reports; the psychological construct and any human-coder comparison are unclear.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM chain-of-thought for aviation accident investigation using HFACS; not psychological or clinical text coded against human labels in this review's sense.)

**Решение:** -

---

### 1235 · R9592

**What About Emotions? Guiding Fine-Grained Emotion Extraction from Mobile App Reviews**

2025 · IEEE International Requirements Engineering Conference (RE) · journalarticle, conference, review · en · https://doi.org/10.1109/re63999.2025.00012

Opinion mining plays a vital role in analysing user feedback and extracting insights from textual data. While most research focuses on sentiment polarity (e.g., positive, negative, neutral), fine-grained emotion classification in app reviews remains underexplored. Fine-grained emotion classification is thus needed to better understand users' affective responses and support downstream tasks such as feature-emotion analysis, user-oriented release planning, and issue triaging. This paper addresses this gap by identifying and addressing the challenges and limitations in fine-grained emotion analysis in the context of app reviews. Our study adapts Plutchik's emotion taxonomy to app reviews by developing a structured annotation framework and dataset. Through an iterative human annotation process, we define clear annotation guidelines and document key challenges in emotion classification. Additionally, we evaluate the feasibility of automating emotion annotation using large language models, assessing their cost-effectiveness and agreement with human-labelled data. Our findings reveal that while large language models significantly reduce manual effort and maintain substantial agreement with human annotators, full automation remains challenging due to the complexity of emotional interpretation. This work contributes to opinion mining in requirements engineering by providing structured guidelines, an annotated dataset, and insights for developing automated pipelines to capture the complexity of emotions in app reviews. Accepted at the 33rd IEEE International Requirements Engineering 2025 conference

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: LLM annotation of Plutchik emotions in app reviews compared with human annotators; emotion construct, though product-review context is borderline.); Sonnet ? (неясен конструкт: LLM–human agreement on Plutchik emotion annotation of app reviews; emotions are psychological, but the text is product feedback, close to the generic-sentiment exclusion.)

**Решение:** +

---

### 1236 · R9619

**Towards scalable and reliable coding of semantic property norms: ChatGPT vs. an improved AC-PLT.**

2025 · Behavior research methods · journal article, med, journalarticle · eng · https://doi.org/10.3758/s13428-025-02838-5

When using the Property Listing Task (PLT) to collect semantic content for a set of concepts (Concept Property Norms, CPNs), coding raw properties into standardized labels poses significant challenges. In this work, we address these challenges by enhancing the Assisted Coding for Property Listing Task (AC-PLT) framework, which facilitates the coding process. The current work conducts an ablation study to optimize AC-PLT by evaluating combinations of text cleaning, embedding models (e.g., Word2Vec, E5, LaBSE), and classification methods (e.g., kNN, SVM, XGBoost). Results show that normalization with the E5 embedding model and kNN classification achieves the highest accuracy, with top-1 test accuracies of 0.523 for CPN27 and 0.608 for CPN120 datasets, outperforming the original AC-PLT baseline. Comparisons with ChatGPT (fine-tuned and one-shot) reveal AC-PLT's superior stability and cost-effectiveness, despite ChatGPT's competitive performance in some cases. The improved AC-PLT framework offers a scalable, efficient solution to manual coding challenges, reducing variability and time constraints. Future work will explore its role as a recommender system for human coders, further enhancing its practical utility in cognitive psychology and psycholinguistics research.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT codes property-listing responses against human-coded labels; it's unclear whether semantic property norms count as a psychological construct.

**Решение:** =

---

### 1237 · R9634

**Objective Scoring of Divergent Thinking Tasks via Large Language Models.**

2025 · Unipub UB Graz (Universität Graz) · dissertation

In den letzten zehn Jahren wurden in der Forschung zunehmend automatisierte Methoden zur Aufgabenbewertung von divergentem Denken (DT) erforscht, um den mit der menschlichen Bewertung verbundenen Zeit- und Kostenaufwand zu verringern und gleichzeitig die Objektivität zu erhöhen. Mit dem Aufkommen verschiedener Large Language Models (LLMs) in den letzten Jahren haben LLM-basierte Bewertungsmethoden sehr vielversprechende Ergebnisse gezeigt. Diese Studie hat das Ziel, bestehende Ergebnisse mit neueren LLM-Versionen (ChatGPT-4, Llama 3.3 70B, Claude Sonnet 3.5) bei Zero-Shot Prompting zu replizieren und zu erweitern. In Anbetracht der begrenzten Forschung im Bereich der automatischen Bewertung von Real-World (RW) Aufgaben sollen auch die Umsetzbarkeit der automatisierten Bewertung dieses Aufgabentyps untersucht werden. Darüber hinaus werden mögliche Auswirkungen der Antwortsprache (Deutsch vs. ins Englische übersetzt) und der Antwortherkunft (menschlich vs. LLM-generiert) untersucht. Die verwendeten Daten bestehen aus 14118 Antworten des Alternate Uses Task (AUT) und einer RW DT-Aufgabe von 300 deutschsprachigen Teilnehmenden, sowie aus 150 von ChatGPT-4o generierten Antworten. Alle Antworten wurden von sechs Ratern auf Deutsch und von den drei LLMs sowohl auf Deutsch als auch auf Englisch (nach Übersetzung) bewertet. Die Ergebnisse zeigen, dass ChatGPT-4 die menschlichen Kreativitätsbewertungen in diesem Zero-Shot-Ansatz am genauesten nachahmt und mittlere bis starke Korrelationen erreicht (r = .55 für den AUT; r = .65 für die RW-Aufgabe). Eine gruppierte Claude Auswertung, bei der 10 zufällig ausgewählte DT-Task-Antworten eines Items zusammen präsentiert und bewertet werden, verbessern die Prozesseffizienz, ohne die Genauigkeit zu beeinträchtigen, im Vergleich zum Einzelbewertungsmodus, bei dem jede Idee einzeln ohne den Kontext anderer Antworten bewertet wird. Die Kombination von LLM-Bewertungen durch Mittelwertbildung von ChatGPT-, Claude- und Claude-Batch-Bewertungen führte zu einer weiteren Verbesserung der Korrelation mit Menschlichen Bewertungen im Vergleich mit den Ergebnissen der einzelnen LLMs (AUT: r = .61; RW: r = .71). Weiters scheint die RW DT Aufgabe für automatische Bewertungen besonders geeignet zu sein. Die Übersetzung ins Englische verbesserte die Übereinstimmung mit menschlichen Bewertungen nicht, was nahelegt, dass Antworten in der Originalsprache von starken LLMs wie ChatGPT-4 zuverlässig bewertet werden können. Abschließend werden mögliche inhaltsbezogene sozio-ethische Verzerrungen für LLMs und subjektive menschliche Bewertungen sowie mögliche technische Verbesserungen der aktuellen Studie betrachtet.

**ИИ:** + · обе модели · подсчёт методики · GPT-4, Llama and Claude scored creativity in AUT and real-world divergent thinking responses; results were correlated with six human raters.

**Решение:** =

---

### 1238 · R9635

**Using Instruction-Tuned Large Language Models to Identify Indicators of Vulnerability in Police Incident Narratives.**

2025 · Journal of quantitative criminology · journal article, journalarticle, review · eng · https://doi.org/10.1007/s10940-025-09611-z

Objectives: Compare qualitative coding of instruction tuned large language models (IT-LLMs) against human coders in classifying the presence or absence of vulnerability in routinely collected unstructured text that describes police-public interactions. Evaluate potential bias in IT-LLM codings. Methods: Analyzing publicly available text narratives of police-public interactions recorded by Boston Police Department, we provide humans and IT-LLMs with qualitative labelling codebooks and compare labels generated by both, seeking to identify situations associated with (i) mental ill health; (ii) substance misuse; (iii) alcohol dependence; and (iv) homelessness. We explore multiple prompting strategies and model sizes, and the variability of labels generated by repeated prompts. Additionally, to explore model bias, we utilize counterfactual methods to assess the impact of two protected characteristics - race and gender - on IT-LLM classification. Results: Results demonstrate that IT-LLMs can effectively support human qualitative coding of police incident narratives. While there is some disagreement between LLM and human generated labels, IT-LLMs are highly effective at screening narratives where no vulnerabilities are present, potentially vastly reducing the requirement for human coding. Counterfactual analyses demonstrate that manipulations to both gender and race of individuals described in narratives have very limited effects on IT-LLM classifications beyond those expected by chance. Conclusions: IT-LLMs offer effective means to augment human qualitative coding in a way that requires much lower levels of resource to analyze large unstructured datasets. Moreover, they encourage specificity in qualitative coding, promote transparency, and provide the opportunity for more standardized, replicable approaches to analyzing large free-text police data sources. 33 pages, 6 figures Submitted to Journal of Quantitative Criminology

**ИИ:** + · обе модели · кодирование по кодбуку · IT-LLMs and human coders used the same codebook to label police narratives for mental ill health and substance misuse, and their labels were compared.

**Решение:** =

---

### 1239 · R9636

**vpfrc_llm_vulnerability_classifier**

2025 · OSF · text/project · https://doi.org/10.17605/osf.io/har9m

This project provides datasets and replication materials for research on using large language models (LLMs) to identify vulnerability indicators in police narratives. It contains classified narrative datasets, counterfactual variations for bias analysis, and labeled examples with human annotations. These resources support the paper "Using Instruction-Tuned Large Language Models to Identify Indicators of Vulnerability in Police Incident Narratives," which evaluates how effectively different LLM architectures can identify mental health issues, substance abuse, alcoholism, and homelessness in police reports.

**ИИ:** + · обе модели · кодирование по кодбуку · LLMs flag mental health, substance abuse and homelessness indicators in police narratives; data repository includes human-annotated examples for comparison.

**Решение:** =

---

### 1240 · R9643

**Automatically assessing oral narratives of Afrikaans and isiXhosa children**

2025 · Slate · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.21437/slate.2025-21

Developing narrative and comprehension skills in early childhood is critical for later literacy. However, teachers in large preschool classrooms struggle to accurately identify students who require intervention. We present a system for automatically assessing oral narratives of preschool children in Afrikaans and isiXhosa. The system uses automatic speech recognition followed by a machine learning scoring model to predict narrative and comprehension scores. For scoring predicted transcripts, we compare a linear model to a large language model (LLM). The LLM-based system outperforms the linear model in most cases, but the linear system is competitive despite its simplicity. The LLM-based system is comparable to a human expert in flagging children who require intervention. We lay the foundation for automatic oral assessments in classrooms, giving teachers extra capacity to focus on personalised support for children's learning. Accepted to SLaTE 2025

**ИИ:** ? · обе модели · неясен конструкт · LLM scores children's oral narrative and comprehension transcripts against expert scores; unclear whether narrative-skill assessment counts as a psychological construct.

**Решение:** =

---

### 1241 · R9648

**Building Feedback Loops between Human Expertise and Large Language Model Systems in Clinical Research**

2025 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.5777803

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests human–LLM collaboration in clinical research, possibly coding, but the psychological construct and human comparison are unclear.

**Решение:** =

---

### 1242 · R9652

**Look What AI Made Me Do: AI-Assisted Qualitative Inquiry for Deeper Insights at Scale**

2025 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/sy6mr_v1

Qualitative research excels at revealing the nuance of human behavior, yet the volume, multilingual scope, and cultural diversity of contemporary datasets increasingly strain its hallmark depth. Drawing on generative artificial intelligence (genAI) capabilities, this paper proposes a hybrid, human‑in‑the‑loop framework that reconciles scale with interpretive rigor. We first establish a manually coded “ground‑truth” subset to anchor subsequent analysis, then employ an AI platform (myRA) to extend deductive and inductive coding across large corpora. Iterative cycles of human validation refine AI‑generated themes, ensuring contextual accuracy and theoretical coherence. We address ethical imperatives, data anonymization, transparent reporting of AI use, and model bias mitigation. We also advocate for privacy‑preserving deployments and locally hosted models where feasible. Looking ahead, we identify four trajectories for AI‑enhanced qualitative inquiry: multimodal analysis that fuses text, audio, and video; multilingual comparison at scale; AI‑driven theory building; and the co‑design of ethically grounded AI systems. Ultimately, we argue that the future of qualitative research lies not in automating interpretation but in strategically augmenting human expertise with AI’s speed and pattern recognition power, thereby achieving deeper insights without sacrificing methodological integrity.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly a framework paper on AI-assisted qualitative coding against a human ground-truth subset; unclear whether agreement data or a psychological construct is reported.); Sonnet -1 (обзор, протокол, комментарий, позиция, руководство: Conceptual framework/position paper on AI-assisted qualitative analysis; no reported empirical LLM–human coding agreement on psychological text.)

**Решение:** -

---

### 1243 · R9670

**Large Language Models for Large-Scale, Rigorous Qualitative Analysis in Applied Health Services Research.**

2025 · Research square · journal article, preprint, journalarticle · eng · https://doi.org/10.21203/rs.3.rs-7794878/v1

Large language models (LLMs) show promise for improving the efficiency of qualitative analysis in large, multi-site health-services research. Yet methodological guidance for LLM integration into qualitative analysis and evidence of their impact on real-world research methods and outcomes remain limited. We developed a model- and task-agnostic framework for designing human-LLM qualitative analysis methods to support diverse analytic aims. Within a multi-site study of diabetes care at Federally Qualified Health Centers (FQHCs), we leveraged the framework to implement human-LLM methods for (1) qualitative synthesis of researcher-generated summaries to produce comparative feedback reports and (2) deductive coding of 167 interview transcripts to refine a practice-transformation intervention. LLM assistance enabled timely feedback to practitioners and the incorporation of large-scale qualitative data to inform theory and practice changes. This work demonstrates how LLMs can be integrated into applied health-services research to enhance efficiency while preserving rigor, offering guidance for continued innovation with LLMs in qualitative research. 20 pages, 6 figures

**ИИ:** ? · обе модели · неясен конструкт · LLM deductive coding of 167 interview transcripts on diabetes care practice transformation; psychological construct and human agreement comparison both unclear.

**Решение:** =

---

### 1244 · R9672

**Using AI to replicate human experimental results: a motion study**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2507.10342

This paper explores the potential of large language models (LLMs) as reliable analytical tools in linguistic research, focusing on the emergence of affective meanings in temporal expressions involving manner-of-motion verbs. While LLMs like GPT-4 have shown promise across a range of tasks, their ability to replicate nuanced human judgements remains under scrutiny. We conducted four psycholinguistic studies (on emergent meanings, valence shifts, verb choice in emotional contexts, and sentence-emoji associations) first with human participants and then replicated the same tasks using an LLM. Results across all studies show a striking convergence between human and AI responses, with statistical analyses (e.g., Spearman's rho = .73-.96) indicating strong correlations in both rating patterns and categorical choices. While minor divergences were observed in some cases, these did not alter the overall interpretative outcomes. These findings offer compelling evidence that LLMs can augment traditional human-based experimentation, enabling broader-scale studies without compromising interpretative validity. This convergence not only strengthens the empirical foundation of prior human-based findings but also opens possibilities for hypothesis generation and data expansion through AI. Ultimately, our study supports the use of LLMs as credible and informative collaborators in linguistic inquiry.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 replicates human valence and affective-meaning ratings of linguistic stimuli; it is unclear whether these count as psychological text coding or as simulated participants.

**Решение:** =

---

### 1245 · R9685

**Can large language models enhance assessment of Criterion A for PTSD from self-report?**

2025 · Psychological trauma : theory, research, practice and policy · journal article, med, journalarticle · eng · https://doi.org/10.1037/tra0002087

Objective Based on the Diagnostic and Statistical Manual of Mental Disorders , fifth edition, posttraumatic stress disorder (PTSD) involves assessing whether a traumatic event meets Criterion A, which is necessary to establish symptom severity and a potential PTSD diagnosis. As research moves online, methods to establish Criterion A have varied widely, influencing the accuracy and consistency of PTSD diagnoses. Literature suggests relying solely on self-assessment of trauma experiences may be problematic. This study evaluated whether integration of large language models (LLMs) directly into online self-report data collection could enhance assessment of Criterion A for PTSD. Method The present study leveraged LLMs to test a new method for enhancing the online assessment of Criterion A from self-report. Adults ( N = 110) completed the extended Life Events Checklist for the Diagnostic and Statistical Manual of Mental Disorders, fifth edition. An LLM was integrated directly into the online survey tool Qualtrics and utilized via Application Programming Interface to code text descriptions to actively follow up with participants by providing additional questions/prompts. Four clinician raters independently evaluated the text descriptions after data collection was complete to determine the proportion of individuals meeting Criterion A and to establish interrater reliability with LLMs. Results The percentage of participants who met Criterion A based on clinician ratings was increased from an average of 65% (range: 59%-71%) at the first description to an average of 86% across all follow-up clarifications. However, interrater reliability of LLMs with clinician raters was only fair, original LLM mean κ = 0.26 (κ range: 0.18-0.46), newer LLM mean κ = 0.35 (κ range: 0.23-0.47). Conclusions Findings suggest that use of LLMs for enhancing Criterion A assessment led to increased information from participants, leading to greater reporting of events meeting Criterion A. However, LLMs did not provide determination of Criterion A on par with clinicians. Findings highlight the need for further assessment of integrating LLMs into online research or treatment. (PsycInfo Database Record (c) 2026 APA, all rights reserved).

**ИИ:** + · обе модели · клиническая оценка · The LLM coded trauma descriptions for PTSD Criterion A, and agreement with four clinician raters was reported as kappa.

**Решение:** =

---

### 1246 · R9691

**LLM-Assisted Text Mining Framework for Cross-Cultural Health Communications: Analyzing Depression News Coverage in Chinese and American Media**

2025 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-981-95-3459-3_21

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM text mining of depression news may involve codebook coding with human validation, but the construct is likely media framing.

**Решение:** =

---

### 1247 · R9719

**Comparing Few-Shot Prompting of GPT-4 LLMs with BERT Classifiers for Open-Response Assessment in Tutor Equity Training**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2501.06658

Assessing learners in ill-defined domains, such as scenario-based human tutoring training, is an area of limited research. Equity training requires a nuanced understanding of context, but do contemporary large language models (LLMs) have a knowledge base that can navigate these nuances? Legacy transformer models like BERT, in contrast, have less real-world knowledge but can be more easily fine-tuned than commercial LLMs. Here, we study whether fine-tuning BERT on human annotations outperforms state-of-the-art LLMs (GPT-4o and GPT-4-Turbo) with few-shot prompting and instruction. We evaluate performance on four prediction tasks involving generating and explaining open-ended responses in advocacy-focused training lessons in a higher education student population learning to become middle school tutors. Leveraging a dataset of 243 human-annotated open responses from tutor training lessons, we find that BERT demonstrates superior performance using an offline fine-tuning approach, which is more resource-efficient than commercial GPT models. We conclude that contemporary GPT models may not adequately capture nuanced response patterns, especially in complex tasks requiring explanation. This work advances the understanding of AI-driven learner evaluation under the lens of fine-tuning versus few-shot prompting on the nuanced task of equity training, contributing to more effective training solutions and assisting practitioners in choosing adequate assessment methods. 8 Page Workshop Paper, AAAI2025 Workshop on Innovation and Responsibility in AI-Supported Education (iRAISE) - Open-response Grading, Feedback, Equity Training, LLMs, BERT, GPT-4

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 graded tutor equity-training open responses against human annotations; unclear whether this is a psychological/interpersonal construct or educational grading.

**Решение:** =

---

### 1248 · R9726

**DarkPatterns-LLM: A Multi-Layer Benchmark for Detecting Manipulative and Harmful AI Behavior**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2512.22470

The proliferation of Large Language Models (LLMs) has intensified concerns about manipulative or deceptive behaviors that can undermine user autonomy, trust, and well-being. Existing safety benchmarks predominantly rely on coarse binary labels and fail to capture the nuanced psychological and social mechanisms constituting manipulation. We introduce \textbf{DarkPatterns-LLM}, a comprehensive benchmark dataset and diagnostic framework for fine-grained assessment of manipulative content in LLM outputs across seven harm categories: Legal/Power, Psychological, Emotional, Physical, Autonomy, Economic, and Societal Harm. Our framework implements a four-layer analytical pipeline comprising Multi-Granular Detection (MGD), Multi-Scale Intent Analysis (MSIAN), Threat Harmonization Protocol (THP), and Deep Contextual Risk Alignment (DCRA). The dataset contains 401 meticulously curated examples with instruction-response pairs and expert annotations. Through evaluation of state-of-the-art models including GPT-4, Claude 3.5, and LLaMA-3-70B, we observe significant performance disparities (65.2\%--89.7\%) and consistent weaknesses in detecting autonomy-undermining patterns. DarkPatterns-LLM establishes the first standardized, multi-dimensional benchmark for manipulation detection in LLMs, offering actionable diagnostics toward more trustworthy AI systems.

**ИИ:** ? · обе модели · неясен конструкт · LLMs detect manipulative content in chatbot outputs against expert annotations; unclear whether AI-safety manipulation/harm counts as a psychological construct.

**Решение:** =

---

### 1249 · R9737

**Large language model enabled synthetic dataset generation for human-AI teaming in mental health assessment**

2025 · Applied Computing and Intelligence · article · en · https://doi.org/10.3934/aci.2025009

Mental health assessment presents unique challenges in healthcare due to its inherently subjective nature and the scarcity of high-quality training data. This research explores the use of large language models (LLMs) to generate synthetic datasets for Human-AI teaming algorithms, focusing on mental health assessments. We created a diverse dataset that simulates human-AI collaboration scenarios in diagnostic processes. Synthetic data are labeled through an innovative approach that involves two human annotators and three LLMs, using majority voting for consensus-based annotations. The dataset initially achieves a similarity score of 83.1%, which is further improved by considering human factors that influence decision-making, with varying performance across different mental health categories, highlighting the need for targeted improvements in data collection and model architecture. Our approach addresses several key challenges in the field, including the lack of real-world training data, privacy concerns, and the need for diverse training datasets. This study serves as a foundation for future work in this critical area, which could lead to more effective and ethically sound AI-assisted mental health assessment tools.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Two human annotators and three LLMs labeled synthetic mental-health texts; unclear whether LLM–human agreement is reported separately from consensus.

**Решение:** =

---

### 1250 · R9752

**Reproducibility and Case Sensitivity of LLMs for Anonymizing Depressed Tweets**

2025 · IEEE International Conference on Data Science and Advanced Analytics (DSAA) · journalarticle, conference, conference-paper · https://doi.org/10.1109/dsaa65442.2025.11247966

A careful analysis of the Large Language Model (LLM) results, generated through anonymized representations of the original dataset, is crucial to precisely evaluate the data-sharing procedure's limitations and facilitate valuable collaborations among Internet-based cognitive behavioral therapy (ICBT) companies and third parties. This paper presents an experimental study of fine-tuning 27 LMs for a multiclass classification task to identify depression severity using 40,191 tweets labeled by human annotators. We fine-tune 14 Bidirectional Encoder Representations from Transformers (BERT), 6 Robustly Optimized BERT Pretraining Approaches (RoBerta), 3 Generative Pretraining (GPT), and 4 Text-to-Text Transfer Transformer (T5) based LMs to classify confidential and anonymized tweets. We report that T5, through conditional generation, outperforms widely adopted BERT, RoBerta, and GPT types for classifying confidential and anonymized tweets. Anonymizing personal information safeguards user privacy and often increases LM performance. Case sensitivity can potentially improve or harm the performance of domain-specific LMs for original and anonymized text.

**ИИ:** ? · обе модели · другое · Fine-tuned GPT/T5 models classify depression severity against human annotator labels; unclear whether the GPT models count as LLMs (GPT-3 or later).

**Решение:** =

---

### 1251 · R9789

**Leveraging Consistency: Evaluating AI Coders for Qualitative Research**

2025 · Digital Commons - USU (Utah State University) · article, text · https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=1919&context=itls_facpub

This study provides insights of using Large Language Models (LLMs) for deductive coding tasks in market research. Deductive coding, which applies predefined codes to text, often demands consistency rather than interpretive nuance. We compare five closed-weight LLMs with a group of human coders in tagging instances of “Expansive Framing” across qualitative excerpts, using Fleiss’ Kappa, ANOVA, and Estimated Marginal Means. Results reveal that LLMs exhibit higher consistency and faster processing than humans. These findings suggest that integrating LLMs can improve efficiency, making them an attractive asset for firms managing large datasets.

**ИИ:** ? · обе модели · неясен конструкт · LLMs and human coders apply a deductive "Expansive Framing" code to qualitative excerpts; unclear whether this market-research construct counts as psychological.

**Решение:** =

---

### 1252 · R9793

**Exploration of Mehrabian's communication model with an android.**

2025 · Scientific reports · journal article, journalarticle, article · eng · https://doi.org/10.1038/s41598-025-11745-w

Multimodal emotional expressions play an essential role in real-life communication. Mehrabian and colleagues suggested that facial expressions may have the greatest emotional impact, followed by vocal and verbal expressions. However, no study has examined all three modalities in face-to-face situations in a single experiment, possibly due to limitations in human acting. We postulated that an android could be a useful solution to this problem. In this study, the android Nikola systematically changed its facial, vocal, and verbal expressions of negative, neutral, and positive emotions in a face-to-face situation. Participants rated the emotional valence of the expressions. The modalities were ranked from the greatest to the least emotional impact, as follows: facial expressions, then vocal expressions, and finally verbal expressions. Additional experiments with human raters and ChatGPT showed comparable emotional valence for facial, vocal, and verbal expressions presented unimodally. The results provide the first evidence validating Mehrabian's model, demonstrating the importance of facial or nonverbal expressions in face-to-face emotional communication.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT and human raters rated the emotional valence of the android's verbal stimulus sentences. Whether this counts as LLM–human agreement is unclear.

**Решение:** =

---

### 1253 · R9803

**AutoPsyC: Automatic Recognition of Psychodynamic Conflicts from Semi-structured Interviews with Large Language Models**

2025 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, preprint/article · en · https://doi.org/10.48550/arxiv.2503.21911

Psychodynamic conflicts are persistent, often unconscious themes that shape a person's behaviour and experiences. Accurate diagnosis of psychodynamic conflicts is crucial for effective patient treatment and is commonly done via long, manually scored semi-structured interviews. Existing automated solutions for psychiatric diagnosis tend to focus on the recognition of broad disorder categories such as depression, and it is unclear to what extent psychodynamic conflicts which even the patient themselves may not have conscious access to could be automatically recognised from conversation. In this paper, we propose AutoPsyC, the first method for recognising the presence and significance of psychodynamic conflicts from full-length Operationalized Psychodynamic Diagnostics (OPD) interviews using Large Language Models (LLMs). Our approach combines recent advances in parameter-efficient fine-tuning and Retrieval-Augmented Generation (RAG) with a summarisation strategy to effectively process entire 90 minute long conversations. In evaluations on a dataset of 141 diagnostic interviews we show that AutoPsyC consistently outperforms all baselines and ablation conditions on the recognition of four highly relevant psychodynamic conflicts.

**ИИ:** + · обе модели · клиническая оценка · LLM rates psychodynamic conflicts from OPD interview transcripts, evaluated against manually scored expert OPD ratings of the same interviews.

**Решение:** =

---

### 1254 · R9805

**Employing Large Language Models for Emotion Detection in Psychotherapy Transcripts: Supplementary Data**

2025 · OSF · text/project · https://doi.org/10.17605/osf.io/akf3h

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests LLM emotion detection in psychotherapy transcripts, which likely compares against human coders. The record is supplementary data.

**Решение:** =

---

### 1255 · R9835

**Integrating Motivational Interviewing Principles and Large Language Models in Automated Behaviour Change Support**

2025

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title suggests MI-based LLM generation, but the paper may also include MI coding validated against human coders.

**Решение:** =

---

### 1256 · R9836

**LLM-based conversational agents for behaviour change support: A randomised controlled trial examining efficacy, safety, and the role of user behaviour**

2025 · International Journal of Human-Computer Studies · text/article, article · en · https://doi.org/10.1016/j.ijhcs.2025.103514

This study examines the use of Motivational Interviewing (MI) principles in a GPT-4-based chatbot, MIcha, to promote behaviour change. We conducted a pre-registered randomised controlled trial to assess the integration of MI techniques in conversational agents, aiming to support users’ behaviour change through guided self-reflection and identify how users interact with large language model (LLM)-based systems in this context. Results indicate that short conversations with LLM-based chatbots are successful at increasing users’ readiness to change and usage of MI principles during text generation can effectively mitigate potential harms. Additionally, we identified distinct user behaviour types — cooperative, reflective, and pre-informed—that significantly influenced the outcomes of interactions. These findings demonstrate the potential of MI principles in enhancing the efficacy of conversational agents for behaviour change and highlight the importance of user behaviour in shaping interaction dynamics. • Brief LLM chats on behaviour change goals significantly boost readiness to change. • Motivational interviewing can significantly reduce potential harms in LLM outputs. • User behaviour types heavily influence conversation outcome and success.

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: RCT of GPT-4 MI chatbot delivering intervention; no LLM coding of text compared against human coders described.); Sonnet ? (неясно, сравнивали ли с людьми: RCT of an MI chatbot; user behaviour types were identified and harms assessed, possibly with human coding or LLM rating, but the abstract doesn't say. Full text needed.)

**Решение:** -

---

### 1257 · R9846

**Simple Prompting Enhances ChatGPT’s Diagnostic Accuracy in Psychiatric Cases**

2025 · preprint · en · https://doi.org/10.31219/osf.io/fd8w5_v2

Despite the centrality of the diagnostic assessment in psychiatry, the agreement among mental health practitioners often varies from poor to moderate. The potential of Large Language Models (LLMs; such as ChatGPT), among other approaches, has been studied to be used as standardized tools to support clinicians’ decision-making. The current work investigates the diagnostic accuracy of ChatGPT 3.5 (gpt-3.5) across different case presentation styles (i.e., vignette and outline) and prompting techniques. A total of 46 psychiatric cases with an accompanying diagnosis were used. Two trained clinical psychologists evaluated the accuracy of the generated diagnosis against the reference diagnosis. A robust statistical approach was then used to investigate the effect of case format and prompt type on the average diagnostic accuracy. The results showed a moderate agreement between the ratings of the two clinical psychologists (kappa = 0.687). Moreover, a statistically significant main effect of prompting technique on gpt-3.5 diagnostic accuracy emerged (p = .009). The highest accuracy was achieved when gpt-3.5 was simply instructed to provide and justify a single diagnosis for each case as compared to when it was asked to provide a diagnosis likelihood (p < .001) or when it was asked to act as a clinical psychologist (p = .001). The results of the current work reinforce the potential to use LLMs as a supporting tool for the diagnostic step in psychiatry and provide a general indication in order to ensure good performance when using them. Additionally, this study offers a methodological framework that can serve as an example for future research aiming to systematically evaluate LLMs’ diagnostic capabilities across different prompting strategies and case presentation formats.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: GPT-3.5 diagnoses psychiatric vignettes against case-book reference diagnoses; unclear whether these count as human coding of the same text.); Sonnet -2 (люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает: ChatGPT generates diagnoses for vignettes; clinical psychologists rate the accuracy of its outputs. The LLM does not code or rate texts against human labels.)

**Решение:** -

---

### 1258 · R9853

**Assessing the accuracy and consistency of large language models in triaging social media posts for psychological distress.**

2025 · Psychiatry research · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.1016/j.psychres.2025.116583

Advances in artificial intelligence, particularly in natural language processing, offer promising tools for addressing mental health challenges in online contexts, potentially identifying at-risk individuals and informing timely interventions. This study investigates the potential of Large Language Models (LLMs) for automatically triaging social media posts expressing psychological distress. Using a dataset of 425 Italian-language Reddit posts, we compared the triage performance of three state-of-the-art LLMs - ChatGPT-4o, Claude 3.5 Sonnet, and Gemini 1.5 Pro - with trained clinician assessment using an adapted version of the Mental Health Triage Scale (MHTS), a validated instrument used in psychiatric screening services. A zero-shot prompting approach, with and without role assignment (simulating a clinician's perspective), evaluated the models' capability to assess intervention urgency. Results revealed that LLMs consistently overestimated urgency compared to human raters, although correlations with human judgments were moderate to strong, with GPT-4o and Claude 3.5 Sonnet demonstrating higher agreement. GPT-4o achieved the best classification performance, highlighting its potential for this task. Claude 3.5 Sonnet showed high sensitivity but lower precision, indicating a tendency toward false positives, while Gemini 1.5 Pro exhibited more balanced but generally lower performance. These findings suggest that while LLMs show promise for mental health triage in social media, their tendency to overestimate urgency and model-specific variations in performance underscore the need for careful interpretation, and human oversight when applying LLMs in mental health contexts.

**ИИ:** + · обе модели · клиническая оценка · GPT-4o, Claude and Gemini rated triage urgency of Reddit distress posts with an adapted MHTS; compared against trained clinician ratings.

**Решение:** =

---

### 1259 · R9867

**TN-Eval: Rubric and Evaluation Protocols for Measuring the Quality of Behavioral Therapy Notes**

2025 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2503.20648

Behavioral therapy notes are important for both legal compliance and patient care. Unlike progress notes in physical health, quality standards for behavioral therapy notes remain underdeveloped. To address this gap, we collaborated with licensed therapists to design a comprehensive rubric for evaluating therapy notes across key dimensions: completeness, conciseness, and faithfulness. Further, we extend a public dataset of behavioral health conversations with therapist-written notes and LLM-generated notes, and apply our evaluation framework to measure their quality. We find that: (1) A rubric-based manual evaluation protocol offers more reliable and interpretable results than traditional Likert-scale annotations. (2) LLMs can mimic human evaluators in assessing completeness and conciseness but struggle with faithfulness. (3) Therapist-written notes often lack completeness and conciseness, while LLM-generated notes contain hallucinations. Surprisingly, in a blind test, therapists prefer and judge LLM-generated notes to be superior to therapist-written notes. As recruiting therapists for annotation is expensive, we will release the rubric, therapist-written notes, and expert annotations to support future research.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM judges rate behavioral therapy notes against therapists' rubric annotations; the construct (documentation quality) may not count as psychological.); Sonnet + (LLM-судья: LLMs rate therapy notes on a therapist-designed rubric (completeness, conciseness, faithfulness) and are compared with expert human annotations. This is LLM-as-judge validated against humans.)

**Решение:** +

---

### 1260 · R9876

**BRIGHTER: BRIdging the Gap in Human-Annotated Textual Emotion Recognition Datasets for 28 Languages**

2025 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2502.11926

People worldwide use language in subtle and complex ways to express emotions. Although emotion recognition--an umbrella term for several NLP tasks--impacts various applications within NLP and beyond, most work in this area has focused on high-resource languages. This has led to significant disparities in research efforts and proposed solutions, particularly for under-resourced languages, which often lack high-quality annotated datasets. In this paper, we present BRIGHTER--a collection of multi-labeled, emotion-annotated datasets in 28 different languages and across several domains. BRIGHTER primarily covers low-resource languages from Africa, Asia, Eastern Europe, and Latin America, with instances labeled by fluent speakers. We highlight the challenges related to the data collection and annotation processes, and then report experimental results for monolingual and crosslingual multi-label emotion identification, as well as emotion intensity recognition. We analyse the variability in performance across languages and text domains, both with and without the use of LLMs, and show that the BRIGHTER datasets represent a meaningful step towards addressing the gap in text-based emotion recognition. Accepted at ACL2025 (Main)

**ИИ:** + · обе модели · бенчмарк с метками людей · Emotion dataset labelled by humans in 28 languages; LLMs are evaluated on emotion identification and intensity against the human labels.

**Решение:** =

---

### 1261 · R9889

**From Joy to Fear: A Benchmark of Emotion Estimation in Pop Song Lyrics**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2509.05617

The emotional content of song lyrics plays a pivotal role in shaping listener experiences and influencing musical preferences. This paper investigates the task of multi-label emotional attribution of song lyrics by predicting six emotional intensity scores corresponding to six fundamental emotions. A manually labeled dataset is constructed using a mean opinion score (MOS) approach, which aggregates annotations from multiple human raters to ensure reliable ground-truth labels. Leveraging this dataset, we conduct a comprehensive evaluation of several publicly available large language models (LLMs) under zero-shot scenarios. Additionally, we fine-tune a BERT-based model specifically for predicting multi-label emotion scores. Experimental results reveal the relative strengths and limitations of zero-shot and fine-tuned models in capturing the nuanced emotional content of lyrics. Our findings highlight the potential of LLMs for emotion recognition in creative texts, providing insights into model selection strategies for emotion-based music information retrieval applications. The labeled dataset is available at https://github.com/LLM-HITCS25S/LyricsEmotionAttribution. 5 pages, 2 figures

**ИИ:** разошлись — Opus ? (неясен конструкт: Zero-shot LLMs are scored against human MOS ratings of six emotions, but it is unclear whether song lyrics count as psychological text.); Sonnet + (бенчмарк с метками людей: Benchmark of zero-shot LLMs predicting emotion intensities in song lyrics against human MOS-annotated labels; emotion construct, human ground truth.)

**Решение:** +

---

### 1262 · R9905

**Identifying psychiatric manifestations in outpatients with depression and anxiety: a large language model-based approach**

2025 · npj Mental Health Research · article · en · https://doi.org/10.1038/s44184-025-00175-1

Abstract Purpose Accurate psychiatric diagnosis and assessment are crucial for effective treatment. However, while current data-driven approaches emphasize diagnostic outcomes, the process of decoding the underlying symptom expressions in patients’ language and mapping them to well-defined psychiatric terminology has received relatively little attention. This study investigates the potential of Large Language Models (LLMs) to automate the identification of diagnostic categories and symptoms from psychiatrist-patient dialogues, to provide interpretable insights and support automatic diagnosis. Methods We analyzed audio recordings from 1160 psychiatric diagnostic interviews, primarily involving patients with depressive disorder and anxiety disorder. A clinical entities corpus was formed by leveraging clinical annotations in EMRs (e.g., chief complaints, mental status, elements in assessment scales) and widely used assessment scales. LLMs were utilized to identify clinical symptoms, rate assessment scales, and an ensemble learning pipeline was designed to classify diagnostic results and symptoms with 10-fold cross-validation. Results The system achieved 86.9% accuracy for identifying the appearance of clinical annotations and 74.7% (77.2%) accuracy for identifying anxiety (depression) symptoms. Patients with depression and anxiety, diagnosed using ICD-10 codes, were differentiated with an accuracy of 75.5%. Analysis of LLM-generated features shows that depression cases exhibited prominent markers of anhedonia and decreased volition, whereas anxiety disorders were characterized by tension and an inability to relax. Conclusion This study demonstrates the potential of integrating LLM technology with linguistic and acoustic features to enhance psychiatric diagnostics. The developed pipeline effectively predicts psychiatric diagnoses and provides interpretable insights, showcasing a valuable tool for clinicians in mental health assessment.

**ИИ:** разошлись — Opus + (клиническая оценка: LLMs identified symptoms and rated scales from psychiatric interview transcripts; accuracy was measured against psychiatrists' EMR annotations of the same interviews.); Sonnet ? (неясно, кто ставил эталонные метки: LLMs identify symptoms and rate scales from psychiatric interview dialogues; accuracy is against EMR annotations, which may be human clinical labels. Unclear whether reference is human coding.)

**Решение:** +

---

### 1263 · R9918

**PersonaTAB: Predicting Personality Traits using Textual, Acoustic, and Behavioral Cues in Fully-Duplex Speech Dialogs**

2025 · Interspeech (USB) · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.21437/interspeech.2025-80

Despite significant progress in neural spoken dialog systems, personality-aware conversation agents -- capable of adapting behavior based on personalities -- remain underexplored due to the absence of personality annotations in speech datasets. We propose a pipeline that preprocesses raw audio recordings to create a dialogue dataset annotated with timestamps, response types, and emotion/sentiment labels. We employ an automatic speech recognition (ASR) system to extract transcripts and timestamps, then generate conversation-level annotations. Leveraging these annotations, we design a system that employs large language models to predict conversational personality. Human evaluators were engaged to identify conversational characteristics and assign personality labels. Our analysis demonstrates that the proposed system achieves stronger alignment with human judgments compared to existing approaches. This is accepted to Interspeech 2025; Added an extra page for supplementary figures; Project page: https://github.com/shinshoji01/Personality-Prediction-for-Conversation-Agents

**ИИ:** + · обе модели · бенчмарк с метками людей · LLM predicts personality from dialogue transcripts; human evaluators assigned personality labels; alignment with human judgments reported.

**Решение:** =

---

### 1264 · R9921

**RSD-15K: A Large-Scale User-Level Annotated Dataset for Suicide Risk Detection on Social Media**

2025 · IEEE International Conference on Data Engineering Workshops (ICDEW) · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/icdew67478.2025.00029

In recent years, cognitive and mental health (CMH) disorders have increasingly become an important challenge for global public health, especially the suicide problem caused by multiple factors such as social competition, economic pressure and interpersonal relationships among young and middle-aged people. Social media, as an important platform for individuals to express emotions and seek help, provides the possibility for early detection and intervention of suicide risk. This paper introduces a large-scale dataset containing 15,000 user-level posts. Compared with existing datasets, this dataset retains complete user posting time sequence information, supports modeling the dynamic evolution of suicide risk, and we have also conducted comprehensive and rigorous annotations on these datasets. In the benchmark experiment, we systematically evaluated the performance of traditional machine learning methods, deep learning models, and fine-tuned large language models. The experimental results show that our dataset can effectively support the automatic assessment task of suicide risk. Considering the sensitivity of mental health data, we also discussed the privacy protection and ethical use of the dataset. In addition, we also explored the potential applications of the dataset in mental health testing, clinical psychiatric auxiliary treatment, etc., and provided directional suggestions for future research work. the article has already been recieved by 2025 IEEE 41st International Conference on Data Engineering Workshops (ICDEW), but hadn't been online yet

**ИИ:** + · обе модели · бенчмарк с метками людей · Benchmark dataset with rigorous human annotation of suicide risk in social media posts; fine-tuned LLMs evaluated against those labels.

**Решение:** =

---

### 1265 · R9923

**TRANSFORMING BINARY DEPRESSIVE DATA INTO SEVERITY INSIGHTS THROUGH AUTOMATIC CLUSTERING AND LABELLING**

2025 · ICTACT Journal on Soft Computing · journalarticle, article · en · https://doi.org/10.21917/ijsc.2025.0555

Depression affects individuals globally, necessitating efficient diagnostic tools. This study introduces an advanced unsupervised hybrid approach, that automatically converts binary-labelled depression datasets into multi-class datasets by integrating a rule-based system with Large Language Models (LLMs). The rule-based system employs the Beck Depression Inventory-II tool that can be used to classify depression levels based on predefined scoring rules, and these rules are segregated into clusters based on score ranges from 0-3. LLMs employ fine-tuned large language Model Meta AI2 (LLaMa2) to generate domain-specific embedding from social media posts. By harnessing LLMs’ contextual understanding, both BDI rules and social media posts are embedded, thereafter cosine similarity is applied to calculate semantic similarities. Based on the similarity score, each post is assigned to the most similar BDI cluster, with the highest similarity score, creating a refined multiclass depression cluster. To evaluate clustering effectiveness, the silhouette score was computed, yielding an average score of 0.45, indicating moderate clustering quality. Additionally, 30% of the binary depression dataset was manually labelled by clinical experts. The Normalized Mutual Information (NMI) score of 0.53 further validated the method, showing strong alignment between the generated clusters and expert-labelled data. This approach enhances depression severity classification, providing a scalable, efficient, and accurate tool for researchers and practitioners.

**ИИ:** разошлись — Opus + (клиническая оценка: Fine-tuned LLaMA2 assigns depression severity to social-media posts; checked against clinical expert labels (NMI). LLM used via embeddings, not prompting.); Sonnet ? (другое: LLaMa2 embeddings assign posts to BDI severity clusters, validated by NMI against clinician labels on 30% of posts. It is unclear whether this counts as LLM coding.)

**Решение:** +

---

### 1266 · R9931

**Neo-Grounded Theory: A Methodological Innovation Integrating High-Dimensional Vector Clustering and Multi-Agent Collaboration for Qualitative Research**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2509.25244

Purpose: Neo Grounded Theory (NGT) integrates vector clustering with multi agent systems to resolve qualitative research's scale depth paradox, enabling analysis of massive datasets in hours while preserving interpretive rigor. Methods: We compared NGT against manual coding and ChatGPT-assisted analysis using 40,000 character Chinese interview transcripts. NGT employs 1536-dimensional embeddings, hierarchical clustering, and parallel agent-based coding. Two experiments tested pure automation versus human guided refinement. Findings: NGT achieved 168-fold speed improvement (3 hours vs 3 weeks), superior quality (0.904 vs 0.883), and 96% cost reduction. Human AI collaboration proved essential: automation alone produced abstract frameworks while human guidance yielded actionable dual pathway theories. The system discovered patterns invisible to manual coding, including identity bifurcation phenomena. Contributions: NGT demonstrates computational objectivity and human interpretation are complementary. Vector representations provide reproducible semantic measurement while preserving meaning's interpretive dimensions. Researchers shift from mechanical coding to theoretical guidance, with AI handling pattern recognition while humans provide creative insight. Implications: Cost reduction from \$50,000 to \$500 democratizes qualitative research, enabling communities to study themselves. Real-time analysis makes qualitative insights contemporaneous with events. The framework shows computational methods can strengthen rather than compromise qualitative research's humanistic commitments. Keywords: Grounded theory; Vector embeddings; Multi agent systems; Human AI collaboration; Computational qualitative analysis 44 pages, 11 figures

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Multi-agent LLM coding of interviews compared with manual coding; unclear whether the same units were compared or only frameworks, and whether the construct is psychological.

**Решение:** =

---

### 1267 · R9943

**TRUST: An LLM-Based Dialogue System for Trauma Understanding and Structured Assessments**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2504.21851

Objectives: While Large Language Models (LLMs) have been widely used to assist clinicians and support patients, no existing work has explored dialogue systems for standard diagnostic interviews and assessments. This study aims to bridge the gap in mental healthcare accessibility by developing an LLM-powered dialogue system that replicates clinician behavior. Materials and Methods: We introduce TRUST, a framework of cooperative LLM modules capable of conducting formal diagnostic interviews and assessments for Post-Traumatic Stress Disorder (PTSD). To guide the generation of appropriate clinical responses, we propose a Dialogue Acts schema specifically designed for clinical interviews. Additionally, we develop a patient simulation approach based on real-life interview transcripts to replace time-consuming and costly manual testing by clinicians. Results: A comprehensive set of evaluation metrics is designed to assess the dialogue system from both the agent and patient simulation perspectives. Expert evaluations by conversation and clinical specialists show that TRUST performs comparably to real-life clinical interviews. Discussion: Our system performs at the level of average clinicians, with room for future enhancements in communication styles and response appropriateness. Conclusions: Our TRUST framework shows its potential to facilitate mental healthcare availability. 5 figures, 4 tables

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM conducts PTSD structured interviews; experts rate outputs, but it may also score assessments or dialogue acts against clinician labels.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM dialogue system conducting PTSD interviews; experts evaluate its outputs, with no LLM coding or rating of texts against human labels.)

**Решение:** -

---

### 1268 · R9945

**Explainable Emotion Classification in Social Media**

2025 · Université d'Ottawa | University of Ottawa · dissertation/thesis · https://doi.org/10.20381/ruor-31260

In the age of internet social media, people express their emotions openly online, making accurate emotion classification an increasingly important yet challenging task. Unlike sentiment analysis, which focuses on the polarity of opinions, emotion analysis dives deeper to identify specific emotions within text. Emotion classification has several practical applications, such as brand perception analysis, crisis management, and processing customer feedback, which are vital for businesses, governments, and organizations to engage effectively with their audiences. This thesis explores both multi-label and multi-class emotion classification and its explainability, specifically in tweets. For multi-label classification, we utilized the SemEval 2018 task E-c dataset, which comprises 11 distinct emotions, and for multi-class classification, we employed the DAIR AI emotion dataset. Through comprehensive experiments, we demonstrated robust model performance across both classification tasks, underscoring the adaptability and effectiveness of our approach. Our research uses instruction-based fine-tuning of large language models (LLMs) like GPT-2 and experiments with zero-shot and dynamic few-shot classification using GPT-4o, LLaMA 3 (8B), and DeepSeek R1 (Distilled Qwen 32B). Building on previous baseline performance, we further improved emotion detection and model interpretability by developing a self-explaining model that uses generative explanations and preference alignment. Notably, we constructed a novel preference alignment dataset using GPT-4o with chain-of-thought prompting, where human annotators assessed model outputs for correctness, clarity, helpfulness, and verbosity. Utilizing this dataset, we preference-aligned GPT-4o via Direct Preference Optimization (DPO) and open-source models, including LLaMA 3 (8B) and DeepSeek R1 (Distilled Qwen 32B), using Odds Ratio Preference Optimization (ORPO). The resulting self-explaining models achieved state-of-the-art multilabel classification performance (68.85\%) on the SemEval 2018 E-c dataset and competitive accuracy (93.1\%) on the DAIR AI multiclass dataset. Furthermore, the explanations generated by our models exceeded existing explainability techniques, achieving a higher sufficiency score of 63.66\%, reflecting better interpretability and alignment with human expectations. We also performed detailed human evaluations of the generated explanations, demonstrating that explanations produced by our preference-aligned models significantly surpass those from pre-trained models.

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT-4o, LLaMA 3 and DeepSeek classify tweet emotions; tested on the SemEval 2018 E-c dataset, whose labels come from human crowd annotators.

**Решение:** =

---

### 1269 · R9947

**Investigating the Effects of Valence, Arousal, Concreteness, and Humor on Words Unique to Singapore English.**

2025 · Journal of cognition · journal article, journalarticle, article · eng · https://doi.org/10.5334/joc.470

Singapore English is a dialect of English spoken by individuals living in Singapore, whose colloquial form (i.e., Singapore Colloquial English) contains unique lexical items not found in dominant dialects of English. The absence of these items from the lexicon of dominant English dialects indicates that lexical-semantic and affective norms central to psycholinguistic research do not exist for these Singapore English concepts, and it is unclear what is the specific influence of these effects when processing Singapore Colloquial English words. The present paper describes the development of valence, arousal, concreteness, and humor norms for a core vocabulary list of approximately 300 words and concepts, via human ratings and probing a Large Language Model, and evaluates the contribution of these norms to account for lexical processing performance in a visual lexical decision task. Results indicated that valence, arousal, and concreteness explained additional variance over and above orthographic similarity and word frequency in the visual lexical decision task. Specifically, Singapore English words that were more positively valenced, highly arousing, and more concrete, were responded to more rapidly and accurately. In addition, although there was generally a high convergence of valence, arousal, and concreteness ratings across human raters and the Large Language Model, humor norms were much less closely aligned. Overall, this paper provides a case study of how psycholinguistic research can be extended to diverse, understudied dialects of English, and showcases how doing so offers an opportunity for psycholinguistics to examine the importance of various lexical-semantic and affective measures to quantify lexical information in colloquial, informal language.

**ИИ:** ? · обе модели · неясен конструкт · An LLM and humans both rated the valence, arousal and humor of words. The units are single words rather than psychological text, so eligibility is unclear.

**Решение:** =

---

### 1270 · R9955

**Acceptability, feasibility, and user experiences of NOLA Gem: a geospatially customizable culturally tailored JITAI for violence-affected people living with HIV (Preprint)**

2025 · preprint · en · https://doi.org/10.2196/preprints.80705

BACKGROUND Post-traumatic stress, alongside comorbid mental health challenges and hazardous alcohol use, disproportionately burden people living with HIV. Drivers of these stressors are both intra-individual, rooted in early life adversity and firsthand violence exposures, and contextual: often place-based. Imparting effective coping skills and distinguishing changeable versus unchangeable stressors can improve stress management proximally with cascading effects on and key HIV continuum of care endpoints such as antiretroviral therapy adherence. But problem- and emotion-based coping skills, delivered via traditional linear in-person group modalities, may falter in the moment. We adapted the evidence-based Living in the Face of Trauma (LIFT) intervention to an iOS- and Android-native app, featuring daily diary–triggered coping skills recommendations, self-guided LIFT psychoeducational sessions, and a personalizable geofencing function. OBJECTIVE This mixed methods study examined the acceptability, feasibility, and user experiences of NOLA Gem, focusing on user interaction costs relative to geographic ecological momentary assessment (GEMA) alone, and honing future optimization options. METHODS People living with HIV (N = 32) were recruited across New Orleans and initially randomized 1:1 to treatment (NOLA Gem+GEMA) versus control (GEMA) for 21 days. Feasibility was assessed via enrollment and attrition rates. At the immediate post assessment, participants completed acceptability and usability measures and a brief structured usability interview. Analyses included descriptive statistics, bivariate logit modeling, and synergistic human-LLM deductive coding. RESULTS N = 30 participants (n = 22 in the GEMA+NOLA Gem treatment arm) completed the pilot: 94% of baseline enrollees. Acceptability was very high across the board: 100% of users considered NOLA Gem “very” or “somewhat” successful in addressing their daily lives, with 91% endorsing increased calm and emotional wellbeing. Fully 50% of NOLA Gem users were “extremely likely” (Net Promoter Score = 10/10) to recommend the app to friends. Eight (27%) of GEMA and GEMA+NOLA Gem users reported privacy concerns. Eleven (50%) NOLA Gem users received geofencing alerts; perceptions of this feature’s helpfulness were mixed. No statistically significant socio-demographic or clinical predictors of disparate acceptability (p ≥ 0.068) or increased privacy concerns (p ≥ 0.171) were found. No additional frictions were evidenced by GEMA+NOLA Gem versus GEMA users (p ≥ 0.132). Qualitatively, NOLA Gem users praised the just-in-time mindfulness, breathing, and problem-solving skills delivery, and broader stress control and self-insight benefits. A subset of users pointed out the burdensome length and sometimes-inconvenient timing of the daily diaries. Recommendations for next-generation personalization included user-specific dynamic daily diary and geofencing prompt tailoring. CONCLUSIONS Our small pilot study demonstrated high NOLA Gem acceptability and feasibility, and a rich, beneficial user experience among people living with HIV, with clear and actionable opportunities for improvement. INTERNATIONAL REGISTERED REPORT RR2-10.2196/47151

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Human-LLM deductive coding of usability interviews; unclear whether LLM–human agreement is reported, and the construct is borderline (app user experience).

**Решение:** =

---

### 1271 · R9956

**The IDRE Dataset in Practice: Training and Evaluation of Small-to-Medium-Sized LLMs for Empathetic Rephrasing**

2025 · Electronics · journalarticle, article · en · https://doi.org/10.3390/electronics14204052

Integrating emotional intelligence into AI systems is essential for developing empathetic chatbots, yet deploying fully empathetic models is often constrained by business, ethical, and computational factors. We propose an innovative solution: a dedicated empathy rephrasing layer that operates downstream of a chatbot’s initial response. This layer leverages large language models (LLMs) to infuse empathy into the chatbot’s output without altering its core meaning, thereby enhancing emotional intelligence and user engagement. To implement this layer, we extend and validate the IDRE (Italian Dialogue for Empathetic Responses) dataset. We evaluated small- and medium-scale LLMs across three configurations: baseline models, models augmented via few-shot learning with IDRE exemplars, and models fine-tuned on IDRE. Performance was quantitatively assessed using the LLM-as-a-judge paradigm, leveraging custom metrics. These results were further validated through an independent human evaluation and supported by established NLP similarity metrics, ensuring a robust triangulation of findings. Results confirm that both few-shot prompting and fine-tuning with IDRE significantly enhance the models’ capacity for empathetic language generation. Applications include empathetic AI in healthcare, such as virtual assistants for patient support, and demonstrate promising generalization to other domains. All datasets, prompts, fine-tuned models, and scripts are publicly available to ensure transparency and reproducibility.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · An LLM judge rated the empathy of rephrased chatbot responses and humans also evaluated them, but it is unclear whether they used the same scheme on the same units.

**Решение:** =

---

### 1272 · R9961

**Enhancing Automated Interview Performance Evaluation Using Multimodal Emotion Detection and Retrieval-Augmented Generation**

2025 · International Conference on Contemporary Computing · conference, review, conference-paper · https://doi.org/10.1109/ic366947.2025.11290678

Conventional interview assessment is based on human perception, tending towards subjectivity, variability, and inefficiencies, particularly when evaluating large groups of candidates. To overcome these drawbacks, we introduce an AI-based automated interview assessment platform that combines multimodal emotion recognition with Retrieval-Augmented Generation (RAG) to deliver objective, data-driven analysis. Our method evaluates verbal (text-based answers), non-verbal (facial reactions, gaze, and body language), and paralinguistic (speech tone, pitch, and clarity) signals to provide a complete assessment of interview performance. By utilizing GPT-3.5 with LLaMA Index, the model reads and places key findings from interview transcripts into context to provide comprehensive and explainable feedback. Moreover, OpenFace and Wav2Vec are utilized for face expression and speech emotion recognition that are combined utilizing a hybrid multimodal approach in order to do a strong assessment. The assessment is done via a Total Score metric, examining candidates on understanding content (30%), confidence, and fluency (20%), emotional control (20%), non-verbal communication (15%), and paralinguistic features (15%). Experimental validation on the MIT Interview Dataset shows that the system proposed here enhances assessment accuracy, fairness, and consistency, outperforming human evaluators in delivering standardized reviews. Such discoveries show the promise of multimodal AI-driven evaluations for automated recruitment, talent assessment, and educational uses, opening the way for scalable, bias-free interview reviews)

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-3.5 multimodal scoring of job interviews (confidence, emotional control) against MIT dataset human ratings; psychological construct and LLM-specific agreement unclear.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Job interview performance scoring with multimodal emotion recognition; not a clinical or psychological coding task, and no clear LLM-human coder agreement.)

**Решение:** -

---

### 1273 · R9979

**Automated Coding of Counsellor and Client Behaviours in Motivational Interviewing Transcripts and Application to a Fully Generative Motivational Interviewing Chatbot**

2025 · TSpace (University of Toronto) · dissertation · https://utoronto.scholaris.ca/bitstreams/61806594-3a4f-48df-8b8e-edcda3e2df45/download

Motivational Interviewing (MI) is a widely-used talk therapy approach employed by clinicians to guide clients toward healthy behaviour change. Evaluating MI sessions and training MI counsellors relies on behavioural coding, the classification of counsellor and client utterances into predefined categories. Recent advances in Large Language Models (LLMs) now make it possible to automate not only behavioural coding, but the delivery of MI itself. This dissertation introduces AutoMISC, which performs utterance-level parsing and behavioural coding under the Motivational Interviewing Skill Code, the original annotation scheme for MI. AutoMISC achieves an overall accuracy of 70% and a macro F1 score of 0.42 for counsellor speech (19 categories) and 0.41 for client speech (17 categories) against expert-aligned annotations using GPT-4.1 (n= 821 utterances). Additional validation showed that the codes predict session-level counselling quality in a widely-used MI transcript dataset at 87% accuracy, and align with existing annotations in another dataset at 71% accuracy. We also demonstrate how the codes can visualize the trajectory of client motivation over a session alongside counsellor codes. We apply AutoMISC to the transcripts of a brief smoking cessation intervention experiment where tobacco smokers conversed with a fully generative MI counsellor chatbot evolved in collaboration with experienced MI clinician-scientists. Two versions were tested: (1) a single prompted LLM (106 participants), and (2) a two-stage approach which decouples technique selection from utterance generation (93 participants). Participant-reported confidence in quitting smoking was measured before the conversation and one week later. Both versions yielded an average increase in confidence of 1.7 on a 0-10 scale (p<0.001 for both). The first version scored well on participant-reported perceived empathy, higher than typical human counsellors, while the second scored lower. AutoMISC’s analysis of the transcripts provided deeper insights beyond participant-reported outcomes. Both versions showed adherence to MI standards in 99% of utterances. We found that the slope of the trajectory of the client’s motivation correlates with the change in confidence (Spearman’s r= 0.28, p<0.005 for Version 1; r= 0.20, p= 0.051 for Version 2). This work demonstrates the potential synergy between automated MI delivery and automated MI behavioural coding.

**ИИ:** + · обе модели · кодирование сессий · GPT-4.1 applies MISC codes to MI transcript utterances; accuracy and F1 are reported against expert-aligned human annotations.

**Решение:** =

---

### 1274 · R9999

**Initial Design and Development of a Novel Framework for Motivational Interviewing Training Through Knowledge Graphs, AI, and Evidence-Based Learning**

2025 · ScholarWorks @ UTRGV (The University of Texas Rio Grande Valley) · article

Motivational Interviewing (MI) is an evidence-based system for talking to patients about behavioral change that has proven effective in multiple use cases such as promoting positive outcomes in patients with Substance Use Disorder and those managing chronic illness. Those who learn motivational interviewing through observed practice with correctional guidance from an expert practitioner demonstrate higher proficiency than those who learn via self-study, group seminars, or the classroom setting. Having one-on-one guidance for every interested learner may be possible through technological advancements, chiefly Artificial Intelligence. In this work, we present one possible path toward a digital platform that leverages this technology as well as insights in evidence-based learning strategies. The incorporation of the latter is facilitated through the creation of a Knowledge Graph, whose application to MI is presented in this work and is a novel contribution to research in this space. Furthermore, we demonstrate a proof-of-concept for using ChatGPT-40 to develop one MI skill—offering Simple Affirmations—illustrating an approach that can be generalized to other MI component skills.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · GPT-4o proof-of-concept for MI affirmation training may involve rating learner responses; unclear whether compared with human coding.

**Решение:** =

---

### 1275 · R0065

**What makes a challenging psychedelic experience challenging? What symptoms persist beyond the acute stage? - A Qualitative Analysis**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/tnqhs

This project investigates what makes a challenging psychedelic experience challenging. Open-ended descriptions of adverse reactions to psychedelics (LSD, psilocybin, DMT, ayahuasca) will be analyzed to answer two questions: (1) What threat contents characterize acutely challenging experiences? and (2) What post-acute symptoms and impairments follow them? An inductive-deductive approach will be employed: a structured codebook, grounded in previous findings, will be refined iteratively through inductive coding of the data. Hybrid qualitative coding will be used, with an LLM serving as a third coder (inter-rater reliability assessed via Gwet's AC1 and Krippendorff's alpha). Post-acute codes will be aligned with DSM-5 PTSD criteria, enabling comparison with clinical post-traumatic symptom profiles. Narratives will be flagged against DSM-5 and ICD-11 trauma Criterion A to test whether the subjective phenomenology of challenging psychedelic experiences meets broader diagnostic thresholds. [Optional: Furthermore, network analysis will be used to examine which acute threat contents are associated with specific post-acute symptom clusters.] Expected outcomes include: (a) a taxonomy of acute threat contents organized by interpersonal, intrapersonal, transpersonal, and affective dimensions; (b) a post-acute symptom profile mapped to PTSD clusters; (c) prevalence estimates of DSM-5 vs. ICD-11 trauma criteria among challenging psychedelic experiences; [Optional: (d) a network map linking acute threat contents to post-acute symptoms; and (e) insights into the mechanisms by which acute threat contents translate into persistent post-acute impairment.]

**Ваша слепая метка (калибровка):** -1 пререгистрация протокола качественного анализа психоделического опыта на OSF, нет эмпирических результатов согласия

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: OSF pre-registration (protocol) with no results; it plans an LLM as third coder of psychedelic narratives. Track the eventual publication.); Sonnet + (кодирование по кодбуку: Preregistered qualitative codebook coding of psychedelic narratives with an LLM as third coder; inter-rater reliability (AC1, alpha) against human coders planned.)

**Решение:** -

---

### 1276 · R0397

**A Phenomenological Analysis of Older Adults' Lived Experience in Music Therapy.**

2026 · Journal of music therapy · journal article, med, journalarticle · eng · https://doi.org/10.1093/jmt/thaf018

With population aging, policies and practices that support healthy aging can be strengthened by creating accessible environments and incorporating the voices of older adults. This phenomenological study aimed to explore the lived experiences of 12 Brazilian older adults participating in a group music therapy process. Over 3 months, a music therapist facilitated 12 weekly music therapy sessions for a group of 12 older adults. Each session lasted an hour and included songs based on participants' musical preferences. Beginning with the 6th session, the group engaged in writing a song addressing the aging process and ageism, which was later recorded and publicly performed. At the end of the process, individual interviews were conducted. Data analysis, supported by the artificial intelligence tool GPT-4, revealed that the group music therapy promoted psychological well-being, facilitated new friendships and social support, retrieved autobiographical memories, and stimulated social activity. Participants considered the collective therapeutic songwriting process as an opportunity to raise awareness about aging and combat ageism. These findings suggest the potential of the music therapy process to foster meaningful social connections, enhance psychological resilience, and promote narratives related to aging and ageism.

**Ваша слепая метка (калибровка):** -6 феноменологический анализ музыкальной терапии с использованием GPT-4 как инструмента анализа, нет оценки согласия с людьми

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · GPT-4 helped analyse interviews about well-being; the abstract doesn't say if it was compared with human coding or only produced themes.

**Решение:** =

---

### 1277 · R0556

**A golden era for open-ended questions? Using LLMs to scale the qualitative coding of open-ended survey responses**

2026 · Center for Open Science · posted-content, preprint · https://doi.org/10.31235/osf.io/f8mga_v3

Open-text questions in quantitative surveys can yield rich information from large samples, but analysing and coding these data using qualitative text analysis is resource-intensive. Large Language Models (LLMs) are a promising tool for scaling up such analyses, reducing time and costs. We first use thematic qualitative text analysis to create a typology of responses; we then let LLMs code texts based on our typology and instructions and compare their coding accuracy with that of student assistants, defining accuracy as agreement with a researcher-coded benchmark dataset. We assess performance on an interpretive coding task: applying a 15-category typology to approximately 1,400 open-ended responses from young US Americans about dating across party-political lines. We evaluate models from OpenAI, Anthropic, and Mistral, with and without training data. The most advanced models outperform student assistants, and performance further increases with training data. This study contributes by applying LLMs to a use case with great analytical potential, namely open-ended survey responses, and testing whether the resulting codes support the same substantive conclusions as hand-coded data. We offer applied social scientists practical recommendations for a division of labour in which researchers retain conceptualisation and codebook construction and delegate the standardised coding to an LLM.

**Ваша слепая метка (калибровка):** -4 социология / открытые ответы об отношениях между представителями разных партий (политические установки, E3)

**ИИ:** ? · обе модели · неясен конструкт · LLMs applied a codebook to open survey responses and were compared with human coders, but the topic (cross-partisan dating) may be political rather than psychological.

**Решение:** =

---

### 1278 · R0689

**411 - Assessing the Capabilities of LLMs in Humor: A Multi-dimensional Analysis of Oogiri Generation and Evaluation**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/rcgy-dn54

Computational humor is a frontier for creating advanced and engaging natural language processing (NLP) applications, such as sophisticated dialogue systems. While previous studies have benchmarked the humor capabilities of Large Language Models (LLMs), they have often relied on single-dimensional evaluations, such as judging whether something is simply ``funny.'' This paper argues that a multifaceted understanding of humor is necessary and addresses this gap by systematically evaluating LLMs through the lens of Oogiri, a form of Japanese improvisational comedy games. To achieve this, we expanded upon existing Oogiri datasets with data from new sources and then augmented the collection with Oogiri responses generated by LLMs. We then manually annotated this expanded collection with 5-point absolute ratings across six dimensions: Novelty, Clarity, Relevance, Intelligence, Empathy, and Overall Funniness. Using this dataset, we assessed the capabilities of state-of-the-art LLMs on two core tasks: their ability to generate creative Oogiri responses and their ability to evaluate the funniness of responses using a six-dimensional evaluation. Our results show that while LLMs can generate responses at a level between low- and mid-tier human performance, they exhibit a notable lack of Empathy. This deficit in Empathy helps explain their failure to replicate human humor assessment. Correlation analyses of human and model evaluation data further reveal a fundamental divergence in evaluation criteria: LLMs prioritize Novelty, whereas humans prioritize Empathy. We release our annotated corpus to the community to pave the way for the development of more emotionally intelligent and sophisticated conversational agents.

**Ваша слепая метка (калибровка):** -4 вычислительный юмор и оценка шуток в японской игре Oogiri

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs rate Oogiri humor responses on six dimensions, compared with human ratings; unclear whether humor/creativity counts as a psychological construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs rate humor (Oogiri) against human ratings, but humor/funniness of jokes is not a psychological or clinical construct in the review's sense.)

**Решение:** -

---

### 1279 · R0762

**LLMs for Now, Fine-Tuning for Later: An Ensemble Approach to Data Drift in Domain-Specific Tasks**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/pkvy-y978

Deploying machine learning models in real-world domain-specific scenarios is challenged by the scarcity of expert annotations and by data drift, where the statistical properties of incoming data continuously evolve. Active Learning (AL) iteratively improves compact models with expert annotations but suffers from recurring cold-start degradation, while LLMs provide strong off-the-shelf performance yet cannot leverage newly accumulated labels, raising the question: how can we better leverage LLMs to assist the active learning process? Through an empirical study on five legal and biomedical datasets, we reveal a complementary temporal dynamic: LLMs excel during early and post-drift stages, while AL-assisted compact models eventually surpass them as annotations accumulate. Motivated by this finding, we propose an ensemble system that combines an LLM, an AL-assisted compact model, and an automatic switch module that routes predictions to the better-performing model in real time. Evaluated under simulated data drift on two mental health datasets, our system achieves 96--98% switch accuracy and consistently outperforms either model used alone.

**Ваша слепая метка (калибровка):** -6 активное обучение при дрейфе данных, ансамбль моделей, оценка переключения на legal/biomed датасетах

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: An LLM classifies texts from two mental health datasets against expert annotations; the abstract doesn't say what the labels are or where they come from.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Ensemble of LLM and active-learning models for data drift; not about LLM–human coder agreement on psychological text, though mental health datasets are used for evaluation.)

**Решение:** -

---

### 1280 · R0917

**Rethinking the Assessment of Oral Communicative Competence in Higher Education: Integrating Closed-Ended and Open-Ended Questionnaires with Generative AI Tools**

2026 · Technology Knowledge and Learning · journalarticle, article · en · https://doi.org/10.1007/s10758-026-09963-w

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -4 высшее образование / оценка устной коммуникативной компетенции студентов (нет аннотации; E3)

**ИИ:** ? · обе модели · нет аннотации · No abstract. Generative AI may analyse open-ended questionnaire responses, but the educational construct and any human comparison are unclear.

**Решение:** =

---

### 1281 · R0954

**CALA-Net: Intelligent depression detection with multimodal fusion and Tree-of-Thoughts framework**

2026 · Computers in Human Behavior Reports · article · en · https://doi.org/10.1016/j.chbr.2026.101051

Depression is recognized as the second leading cause of global disease burden, yet efficient and precise detection methods remain underexplored. While existing approaches have made progress in identifying depressive symptoms, they are limited by insufficient multimodal semantic analysis, subjective assessment bias, and inadequate detection performance. This study aims to address these gaps by proposing the Cross-Attention and LLM-Assisted Network (CALA-Net), a multimodal framework for depression screening. The framework integrates a Temporal-Spatial Cross-Attention (TSCA) module to fuse audio and facial features, employs a fine-tuned large language model (LLM), and utilizes a Tree of Thoughts (ToT) prompting mechanism to systematically evaluate participants’ dialogue or self-report texts along standardized psychological feature dimensions. The extracted multimodal features are then processed by a random forest classifier for final depression assessment. Evaluation was conducted on the publicly available D-Vlog and LMVD datasets, as well as the internally developed FJSI structured clinical interview dataset, demonstrating the model’s capability across different evaluation settings. The TSCA module achieved F1-Scores ranging from 0.740 to 0.787 across all three datasets. The complete CALA-Net framework, incorporating the text modality, showed improved performance on the FJSI dataset with F1-Scores between 0.826 and 0.841. These findings provide valuable insights into multimodal depression detection and present a novel approach to support objective, automated screening for depression in clinical settings. • We propose CALA-Net, a multimodal framework for automated depression screening. • We designed a TSCA module for audio and facial features fusion via temporal-spatial cross-attention. • We found the combination of audio, facial, and textual modalities can improve depression detection. • CALA-Net achieves F1-Scores of 0.826-0.841 on clinical interview data.

**Ваша слепая метка (калибровка):** ? CALA-Net: скрининг депрессии по интервью FJSI; проверить сопоставление RDoC/ToT с оценками клиницистов vs диагнозом

**ИИ:** -3 · обе модели · эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность) · Multimodal pipeline predicts depression status; LLM-extracted text features feed a random forest, with no LLM–human coding agreement on the same texts.

**Решение:** =

---

### 1282 · R10375

**SSRLBot: Designing and Developing a Large Language Model-based Agent using Socially Shared Regulated Learning**

2025 · AIED Companion · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.48550/arxiv.2505.00945

Large language model (LLM)--based agents have emerged as pivotal tools in assisting human experts across various fields by transforming complex tasks into more efficient workflows and providing actionable stakeholder insights. Despite their potential, the application of LLM-based agents for medical education remains underexplored. The study aims to assist in evaluating the students' process and outcomes on medical case diagnosis and discussion while incorporating the theoretical framework of Socially Shared Regulation of Learning (SSRL) to assess student performance. SSRL emphasizes metacognitive, cognitive, motivational, and emotional interactions, highlighting the collaborative management of learning processes to improve decision-making outcomes. Grounded in SSRL theory, this tool paper introduces SSRLBot, an LLM-based agent designed to enable team members to reflect on their diagnostic performance and the key SSRL skills that foster team success. SSRLBot's core functions include summarizing dialogue content, analyzing participants' SSRL skills, and evaluating students' diagnostic results. Meanwhile, we evaluated SSRLBot through diagnostic conversation data collected from six groups (12 participants, 1926 conversational turns). Results showed that SSRLBot can deliver detailed, theory-aligned evaluations, link specific behaviors to SSRL dimensions, and offer actionable recommendations for improving teamwork. The findings address a critical gap in medical education, advancing the application of LLM agents to enhance team-based decision-making and collaboration in high-stakes environments. 8 pages, 2 figures

**Ваша слепая метка (калибровка):** -4 медицинское образование, агент SSRLBot для поддержки группового обучения студентов

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM agent analyses SSRL behaviours in team dialogue; the abstract doesn't say whether its coding was compared with human coders.

**Решение:** =

---

### 1283 · R10398

**Qualitative Coding with GPT-4**

2025 · Journal of Learning Analytics · journalarticle, article, journal-article · en · https://doi.org/10.18608/jla.2025.8575

This study explores the potential of the large language model GPT-4 as an automated tool for qualitative data analysis by educational researchers, exploring which techniques are most successful for different types of constructs. Specifically, we assess three different prompt engineering strategies — Zero-shot, Few-shot, and Few-shot with contextual information — as well as the use of embeddings. We do so in the context of qualitatively coding three distinct educational datasets: Algebra I semi-personalized tutoring session transcripts, student observations in a game-based learning environment, and debugging behaviours in an introductory programming course. We evaluated the performance of each approach based on its inter-rater agreement with human coders and explored how different methods vary in effectiveness depending on a construct’s degree of clarity, concreteness, objectivity, granularity, and specificity. Our findings suggest that while GPT-4 can code a broad range of constructs, no single method consistently outperforms the others, and the selection of a particular method should be tailored to the specific properties of the construct and context being analyzed. We also found that GPT-4 has the most difficulty with the same constructs than human coders find more difficult to reach inter-rater reliability on.

**Ваша слепая метка (калибровка):** -4 педагогическое качественное кодирование: уроки алгебры, поведение при отладке кода; нет психолого-клинического конструкта

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 coding compared against human coders on educational data (tutoring transcripts, student behaviours). Unclear whether the constructs are psychological, e.g. affect or engagement.

**Решение:** =

---

### 1284 · R10758

**Listen, Watch, and Learn to Feel: Retrieval-Augmented Emotion Reasoning for Compound Emotion Generation**

2025 · conference-paper · en · https://doi.org/10.18653/v1/2025.findings-acl.590

The ability to comprehend human emotion using multimodal large language models (MLLMs) is essential for advancing human-AI interaction and multimodal sentiment analysis.While psychology theory-based human annotations have contributed to multimodal emotion tasks, the subjective nature of emotional perception often leads to inconsistent annotations, limiting the robustness of current models.Addressing these challenges requires more fine-grained methods and evaluation frameworks.In this paper, we propose the Retrieval-Augmented Emotion Reasoning (RAER) framework, a plug-andplay module that enhances MLLMs' ability to tackle compound and context-rich emotion tasks.To systematically evaluate model performance, we introduce the Stimulus-Armed Bandit (SAB) framework, designed to benchmark emotional reasoning capabilities.Additionally, we construct the Compound Emotion QA dataset, an AI-generated multimodal dataset aimed at strengthening emotion understanding in MLLMs.Experimental results demonstrate the effectiveness of RAER across both traditional benchmarks and SAB evaluations, highlighting its potential to enhance emotional intelligence in multimodal AI systems. A HyperparametersKey hyperparameters used for RAER, SAB, and DPO are provided in Table 7..

**Ваша слепая метка (калибровка):** -4 мультимодальная генерация и распознавание сложных эмоций в диалогах, синтетический датасет Compound Emotion QA

**ИИ:** разошлись — Opus ? (другое: Multimodal LLMs recognise emotions on traditional benchmarks that likely have human labels, but the input is video/audio rather than text, and the paper mainly develops a method.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Multimodal emotion reasoning framework and AI-generated dataset for MLLMs; no LLM-vs-human coding agreement on psychological text.)

**Решение:** -

---

### 1285 · R12352

**Measuring Latent Trust Patterns in Large Language Models in the Context of Human-AI Teaming**

2023 · Proceedings of the Human Factors and Ergonomics Society Annual Meeting · journalarticle, article · en · https://doi.org/10.1177/21695067231192869

Qualitative self-report methods such as think-aloud procedures and open-ended response questions can provide valuable data to human factors research. These measures come with analytic weaknesses, such as researcher bias, intra- and inter-rater reliability concerns, and time-consuming coding protocols. A possible solution exists in the latent semantic patterns that exist in machine learning large language models. These semantic patterns could be used to analyze qualitative responses. This exploratory research compared the statistical quality of automated sentence coding using large language models to the benchmarks of self-report and behavioral measures within the context of trust in automation research. The results indicated that three large language models show promise as tools for analyzing qualitative responses. The study also provides insight on minimum sample sizes for model creation and offers recommendations for further validating the robustness of large language models as research tools.

**Ваша слепая метка (калибровка):** -4 инженерная психология / эргономика, доверие в командах человек-ИИ

**ИИ:** разошлись — Opus -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): LLM coding of trust responses is benchmarked against self-report and behavioral measures, not human coders; models seem to be embedding-based.); Sonnet ? (неясно, сравнивали ли с людьми: LLMs code open-ended trust responses, but the models may be embedding or encoder types, and the benchmarks are self-report and behavioral measures. Human coder comparison is unclear.)

**Решение:** -

---

### 1286 · R1315

**Auditing LLM-mediated interpretation through source-to-claim documentation**

2026 · Research Square · preprint · https://doi.org/10.21203/rs.3.rs-10756391/v1

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -4 NLP, аудит источников утверждений LLM

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests auditing LLM interpretation, possibly of qualitative data; unclear whether there is a psychological construct or human comparison.

**Решение:** =

---

### 1287 · R1849

**Predicting dropout from therapy based on first-session transcripts**

2026 · npj Mental Health Research · article · en · https://doi.org/10.1038/s44184-026-00249-8

Dropout from psychotherapy is common, often occurring early in treatment, but predicting which patients will leave care remains difficult. In this retrospective cohort study of 31,146 patients receiving individual outpatient therapy through an employer-sponsored digital mental health platform, we examined whether language from first-session transcripts could be used to predict subsequent dropout (failure to attend a fourth session within 1 year of the first session). We combined clinical, demographic, and utilization variables with features derived from transcripts using natural language processing and large language models. Models incorporating transcript-derived features improved prediction compared with pre-session data alone (area under the curve, 0.642 vs 0.569). Provider behaviors, particularly whether follow-up care was clearly discussed, were strongly associated with retention, while patient-level constructs such as motivation, ambivalence, and therapeutic alliance were not consistently predictive. Although overall discrimination was modest, transcript-derived features improved identification of high-risk patients. These findings suggest that early-session dynamics contain actionable signals of engagement and may support scalable approaches to improving retention in mental health care.

**Ваша слепая метка (калибровка):** -3 критериальная валидность: предсказание внешнего исхода (дропаут пациентов из терапии) по первой сессии, а не кодирование текста людьми

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM-coded therapy-session constructs (alliance, motivation, follow-up discussion) predict dropout; unclear whether LLM codes were validated against human coders.

**Решение:** =

---

### 1288 · R1978

**An LLM-Powered Embodied VR Tutor for Smoking Cessation: SRL via Reflective Dialogue**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-29794-5_34

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** ? нет аннотации; VR-тьютор для отказа от курения, проверить по полному тексту (вероятно интервенция -6 или -2)

**ИИ:** -6 · обе модели · другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM · No abstract; title describes an LLM VR tutor delivering a smoking-cessation intervention, with no apparent LLM-versus-human coding task.

**Решение:** =

---

### 1289 · R2079

**Adaptive follow-up questions for data quality in open-ended EMA questions using LLMs**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/ysrxt

Experience sampling method (ESM) studies often collect large volumes of qualitative data, including open-ended descriptions of stressful events. However, this information remains largely underutilised, primarily because manual coding is time-consuming and ensuring data quality is difficult (Bringmann et al., 2026). While validation techniques exist for numerical responses, quality checks for open-text responses are largely unexplored. Compared with fixed-format or self-learning items, open-text responses provide richer, more detailed information but are prone to omitting important details (such as the people involved, the location, or the reasons for perceived stress) that are essential to understanding the everyday context of stressors. In this study, we propose an automated pipeline that can be integrated into regular ESM studies, and we demonstrate its feasibility through a small pilot study. The pipeline uses locally hosted large language models (LLMs) to extract social context information from participants' descriptions of stressful events. Based on this extraction, adaptive, personalised follow-up questions are created to allow participants to vverify the extracted information, provide missing details, and clarify inconsistent responses (e.g., reporting no stressors despite a stress rating of 90/100). The follow-up questions also allow participants to confirm, correct, or extend their stored social network.

**Ваша слепая метка (калибровка):** -1 пре-регистрация протокола на OSF по открытым вопросам в EMA/ESM, не эмпирика

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: Pre-registration/protocol; the LLM extracts stressor context, which participants verify. No human coders apply the same scheme to compare agreement.); Sonnet ? (неясно, сравнивали ли с людьми: LLM extracts social context from EMA stress descriptions; pilot may validate extraction against human coding, but the abstract doesn't say so.)

**Решение:** -

---

### 1290 · R2348

**Detecting Mental Health Signals in Social Media Text: A Large Language Model–Based Approach with Knowledge-Informed Prompt Engineering (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.98535

BACKGROUND Mental disorders are often under detected, and social media text has emerged as a complementary source of behavioral signals for digital mental health research. Existing approaches for detecting mental health conditions from user-generated content commonly rely on disorder-specific supervised machine learning models or large language model–based discrete prompting strategies, which may require substantial labeled data and may not systematically incorporate domain knowledge. OBJECTIVE This study aimed to develop and evaluate a large language model–based method for detecting mental health signals from user-generated social media text by combining personalized continuous prompting with structured medical knowledge. METHODS We proposed a continuous multi-prompt framework built on FLAN-T5 that integrates 2 components: (1) prefix tuning to capture user-level personalized context and (2) a rule-based prompt layer that injects ontology-based medical knowledge related to symptoms, life events, and treatments. The method is evaluated on eRisk datasets for depression and pathological gambling using subject-level prediction from longitudinal social media posts. The depression dataset included 1707 subjects (214 positive, 1493 negative), and the pathological gambling dataset included 4427 subjects (245 positive, 4182 negative). Data are split into training, validation, and test sets (60%/20%/20%), and results are averaged over 10 runs. We report F1-score, precision, and recall and compare the proposed method with traditional machine learning, deep learning, discrete prompting, and large language model fine-tuning baselines. We also examined few-shot learning, early identification, performance on a rare-disorder dataset (self-harm; 340 subjects, including 41 positive cases), and alignment with psychiatrist ratings. RESULTS The proposed method achieved the highest F1-scores among the evaluated approaches on both primary tasks. For depression detection, it achieved an F1-score of 0.913, precision of 0.888, and recall of 0.939. For pathological gambling detection, it achieved an F1-score of 0.985, precision of 0.985, and recall of 0.990. On the rare-disorder self-harm dataset, the method achieved an F1-score of 0.917. In post hoc evaluation, model probabilities showed strong alignment with psychiatrist ratings (Pearson r=0.8656), while expert interrater agreement is high (Pearson r=0.9636). CONCLUSIONS A large language model approach that combines personalized continuous prompting with structured medical knowledge can improve detection of mental health–related signals in social media text. These findings support the potential of knowledge-informed prompt engineering for scalable, data-efficient digital mental health research using user-generated content. This approach should be interpreted as a complementary screening and monitoring tool for research settings rather than as a clinical diagnostic system.

**Ваша слепая метка (калибровка):** -3 критериальная валидность: датасеты eRisk с бинарной меткой депрессии/гемблинга по самоотчету пользователей, а не экспертная разметка текста

**ИИ:** ? · обе модели · другое · Model probabilities on social-media posts were compared with psychiatrist ratings (r=0.87), but FLAN-T5 (encoder-decoder) is a borderline LLM; eRisk labels are self-reported.

**Решение:** =

---

### 1291 · R2665

**Large-Language-Models-As-a-Judge in Theory-Agnostic Adaptive Metric-Alignment for Prototypical Networks in Personality Recognition**

2026 · IEEE Transactions on Affective Computing · journalarticle, preprint/article, article · en · https://doi.org/10.1109/taffc.2026.3712379

Personality recognition has traditionally been constrained by theory-dependent formulations, where models are trained to fit predefined psychological taxonomies rather than uncovering shared underlying behavioral structure. This limits generalization, as personality itself is better understood as theory-invariant, while existing annotations reflect only partial and sometimes inconsistent views of the same latent traits. In this work, we introduce JAM ((J)udge for (A)daptive (M)etric-Alignment), a theory-agnostic framework that shifts learning from adapting to predefined personality theories toward discovering unified latent pseudo-facets that capture shared psychological structure. Rather than constraining the model to any personality taxonomy during training or inference, the framework learns generalizable psychological representations and can infer an individual's latent psychological profile directly from the textual samples, without requiring theory-specific labels. JAM achieves this through an Attention-Pooled Graph Prototypical Network that learns structured representations via clustering in embedding space, together with a Cross-Theory Harmonization (CTH) approach that integrates (i) Human-Guided Linkage and (ii) Machine-Induced Consensus to unify heterogeneous datasets without relying on predefined labels. To further improve robustness and data quality, we incorporate an LLM-as-a-Judge mechanism operating in two configurations, (i) LLM-before-the-loop and (ii) LLM-in-the-loop which identifies ambiguous samples to guide adaptive metric learning. Experiments show that JAM improves cross-framework generalization and performance, establishing a strong step toward theory-agnostic personality inference and supporting low-resource personality theories. The related code repository, model weights, and artifacts are available at https://research.jingjietan.com/JAM

**Ваша слепая метка (калибровка):** ? IEEE TAFFC: распознавание черт личности, калибровка метрик LLM-as-a-judge; проверить согласие на уровне текстов

**ИИ:** разошлись — Opus -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): The LLM judge only flags ambiguous samples for a prototypical network; personality labels are likely self-report, with no human coding of the texts.); Sonnet -7 (другое — напишите почему: Personality recognition via prototypical network; the LLM-as-judge only flags ambiguous training samples, with no reported LLM–human coder agreement.)

**Решение:** -

---

### 1292 · R3212

**Evaluating a large language model–driven safety culture interview chatbot and transcript analysis in a simulated experiment**

2026 · Safety Science · article · en · https://doi.org/10.1016/j.ssci.2026.107427

Safety-critical industries are placing increasing attention on the cultural aspects of safety. Conducting safety culture assessments has become commonplace for supporting the continuous improvement of safety. Comprehensive safety culture assessments are highly resource-demanding and complex projects that involve qualitative data collection and analysis. In this article, we examine the applicability of tools driven by large language models (LLMs) to conduct and analyse safety culture interviews. Firstly, we developed a custom, LLM-driven safety culture interview chatbot. The chatbot was used to create a simulated safety culture interview dataset where it interviewed a human safety culture expert roleplaying ten interviewees. Secondly, the interview transcripts were analysed in parallel by the LLM and by another human expert, and the results of the analyses were compared. We found that the chatbot was successful in collecting useful information within the safety culture interview context. It appears to complement human-led safety culture interviews and safety climate questionnaires by offering a scalable, yet qualitative and interactive, data collection solution. We also found that the LLM was useful for identifying safety culture themes from the interview transcripts, offering an increase in efficiency and potentially offering an alternative perspective on the data. We conclude that while LLM-based tools can be valuable for safety culture assessments, they should complement, rather than replace, human involvement and the established methods. Based on our observations, we propose several future research needs.

**Ваша слепая метка (калибровка):** -6 качественное тематическое сравнение интервью по культуре производственной безопасности без поштучных метрик согласия (E4)

**ИИ:** разошлись — Opus ? (другое: An LLM and a human expert analysed the same interview transcripts. The comparison may be theme-level only, and it is unclear whether safety culture counts as a psychological construct.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Safety culture interviews in industry; LLM and human theme identification compared at theme level, not a clinical or psychological coding task with unit-level agreement.)

**Решение:** -

---

### 1293 · R4784

**Unlocking the Power of Generative AI in Qualitative Data Analysis: A Deep Dive into Data from a Physical Activity Service Evaluation**

2026 · Smart innovation, systems and technologies · conference-paper · en · https://doi.org/10.1007/978-3-032-18849-6_17

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** -4 качественный анализ отзывов об услугах физической активности

**ИИ:** ? · обе модели · нет аннотации · No abstract; generative AI qualitative analysis of physical activity evaluation data may involve comparison with human coding of experiences.

**Решение:** =

---

### 1294 · R4986

**Using large language models to complement humans for the coding of social media interactions between science teachers**

2026 · Discover Education · journalarticle, article, conference paper · en · https://doi.org/10.1007/s44217-025-00868-x

Large Language Models (LLMs) offer a powerful opportunity to support educational researchers in analysing large-scale qualitative datasets, particularly those emerging from informal online learning environments. With teacher informal professional learning increasingly occurring on social media platforms, such as Facebook groups dedicated to teaching, the volume and complexity of interactional posts pose significant challenges for traditional thematic analysis. This study focuses specifically on Australian science teacher Facebook groups, exploring the potential of LLMs to enhance the efficiency and depth of qualitative coding in these dynamic, peer-driven spaces. 2000 posts were analysed from four science teacher Facebook communities, including groups for Biology, Chemistry, Physics, and general Science education. An inductively developed coding schema was applied first by human researchers and then iteratively refined using LLMs (GPT-3.5 Turbo, GPT-4 Turbo, and GPT-4o). By parallel coding the Facebook posts using both human coders and three off-the-shelf LLMs, we developed a systematic approach for prompt engineering LLMs to code qualitative data sets. Inter-coder reliability was evaluated using Krippendorff’s Alpha, allowing us quantitatively assess the performance of different LLMs relative to each other and to expert human judgement. Results show that LLMs can approach or match human coding performance with careful prompt refinement. GPT-4o achieved inter-coder reliability on par with human coders, even when applied to datasets beyond the original training context. This suggests that, with well-crafted prompts and clear coding schemes, LLMs can serve as reliable co-coders, reducing workload, enhancing consistency, and enabling researchers to scale their analysis without sacrificing quality. However, model reliability varied with post ambiguity and topic familiarity, highlighting the importance of human oversight. The study demonstrates that LLMs can serve as effective co-analysts, enhancing the speed and scalability of qualitative research without sacrificing rigour. This paper will be of particular interest to educational researchers working with qualitative data, especially those exploring teacher professional learning, online communities of practice, and science education. This paper offers a replicable workflow for using LLMs in education research and proposes new directions for analysing informal professional learning at scale. By showcasing how LLMs can be leveraged to support, not replace, human insight, this study opens new possibilities for qualitative research in education

**Ваша слепая метка (калибровка):** -4 качественный анализ постов учителей естественных наук в профессиональных группах Facebook, нет психолого-клинического конструкта

**ИИ:** ? · обе модели · неясен конструкт · GPT models vs human coders (Krippendorff's alpha) on teacher Facebook posts; unclear if codes capture psychological/interpersonal constructs or only educational topics.

**Решение:** =

---

### 1295 · R5136

**Detecting Experiential Intertextuality Across Migration Routes: Beyond Surface Similarity in French Narratives**

2026 · SIGDIAL Conferences · journalarticle · https://doi.org/10.18653/v1/2026.sigdial-1.nn

Migrants traversing geographically distinct routes such as the Trans-Saharan and Balkan corridors often recount strikingly parallel lived experiences: police violence, smuggler exploitation, dangerous crossings, and family separation. We introduce the task of experiential intertextuality detection: automatically identifying shared experiential echoes across migration narratives without requiring annotated training data. From 108 French migration narratives spanning both corridors, we automatically generate sentence pairs and score them using annotation-free methods: lexical baselines, sentence embeddings, POS-based structural features, a migration-specific theme lexicon, context-aware narrative features, and zero-shot LLM scoring with Qwen2.5-7B and Mistral-7B under three prompting strategies. We validate all methods against 816 expert-annotated intertextuality judgments (inter-annotator Krippendorff's $\alpha = 0.27$). Our results reveal that all surface, structural, and embedding methods correlate only weakly with expert judgments ($r \leq 0.30$); Qwen2.5-7B zero-shot achieves the best single-method correlation ($r = 0.38$); few-shot examples degrade Qwen but dramatically improve Mistral; narrative position significantly predicts intertextuality, with departure-phase pairs showing the highest experiential echoes; and a supervised hybrid combining all 31 features achieves $r = 0.45$, a 21% improvement over the best individual method.

**Ваша слепая метка (калибровка):** -4 литературоведение, нарративы мигрантов, интертекстуальность

**ИИ:** ? · обе модели · неясен конструкт · Zero-shot LLMs rate experiential similarity in migrant narratives against expert annotations; unclear whether intertextuality counts as a psychological construct.

**Решение:** =

---

### 1296 · R6554

**PrivacyReasoner: Can LLM Emulate a Human-like Privacy Mind?**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.09152

Prior work on LLM-based privacy focuses on norm judgment over synthetic vignettes, rather than how people think about a specific data practice and formulate their opinions. We address this gap by designing PrivacyReasoner, an agent architecture grounded in three key ideas: (1) LLMs can detect subtle privacy cues in natural language and role-play human characteristics; (2) a user's ``privacy mind'' can be reconstructed from their real-world online comment history, distilling experiences, personality, and cultural orientations; and (3) a contextual filter can dynamically activate relevant privacy beliefs based on the contexts in a scenario. We evaluate PrivacyReasoner on real-world privacy discussions from Hacker News, using an LLM-as-a-Judge evaluator calibrated against an established privacy concern taxonomy to quantify reasoning faithfulness. PrivacyReasoner significantly outperforms baselines in predicting individual privacy concerns and generalizes across different domains, such as AI, e-commerce, and healthcare.

**Ваша слепая метка (калибровка):** -4 приватность, рассуждения о нормах приватности по истории комментариев

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM emulates users' privacy concerns; an LLM judge codes concerns using a taxonomy, but whether it is validated against human coding is unclear.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Agent simulates users' privacy opinions from comment history; the LLM judge evaluates reasoning faithfulness, not human-coded psychological text agreement.)

**Решение:** -

---

### 1297 · R6631

**Towards a Unified Model for Evaluating Respect and Empathy in Dialogues**

2026 · Institutional Repositories DataBase (IRDB) · article · en · https://kyutech.repo.nii.ac.jp/record/2002714/files/10478337.pdf

Empathy and respect are central social-affective dimensions of dialogue that influence perceived service quality, yet prior studies have typically modelled them in isolation using separate datasets and evaluation metrics. This work addresses this limitation by jointly modelling empathy and respect and by introducing an explicit metric for their combined expression in service dialogues. We construct two complementary dialogue datasets by assigning respect labels to an empathy-annotated corpus and empathy labels to a respect-annotated corpus using a large language model, and we train both single-task and multi-task classifiers on these data. To evaluate joint social quality, we propose the Respect--Empathy Index (RE-index), which measures the proportion of responses that simultaneously satisfy minimal criteria for empathy and respect. Experiments on the two datasets reveal a clear asymmetry. On the respect dataset, multi-task learning with human-annotated respect labels and LLM-generated empathy labels substantially improves empathy performance, while preserving respect performance. In contrast, on the empathy dataset, multi-task learning with highly imbalanced LLM-generated respect labels degrades empathy performance. Furthermore, we observe that high classification scores for individual dimensions do not necessarily translate into high joint scores: in some settings, the predicted RE-index is less than half of the gold value. These results indicate that joint modelling is sensitive to the reliability and distribution of auxiliary labels, and that multi-dimensional evaluation metrics such as RE-index are necessary for analysing dialogue systems that aim to capture both empathic and respectful behaviour.

**Ваша слепая метка (калибровка):** -4 клиентский сервис, аугментация диалогов

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · An LLM labels empathy and respect in dialogues. It is unclear whether those labels were checked against human annotations of the same units.

**Решение:** =

---

### 1298 · R7091

**Clinically Grounded AI-Scribing in Psychotherapy: Benchmarking LLMs Against Expert Documentation in the iCARE Framework**

2025 · medRxiv · preprint, ppr · en · https://doi.org/10.1101/2025.06.25.25330252

Abstract Background AI-scribes based on large language models (LLMs) are being rapidly adopted in healthcare, yet their use in psychotherapy remains limited because most systems produce brief, administratively oriented notes that miss the interpretative and contextual nuance essential to mental-health documentation. We argue that AI documentation for psychotherapy should instead be built on a comprehensive structure of history, clinical evaluation, and risk assessment that can subsequently be condensed into any brief format. Objective To this end we introduce iCARE ( I dentifying information, C hief concerns and clinical history, A ssessment and analysis, R isk identification, E valuation of progress and action plan), a structured, clinically grounded, 17-section documentation format developed through iterative review by psychiatrists and clinical psychologists. Methods Using the publicly available HOPE dataset, we created iHOPE, a corpus of 174 re-transcribed, speaker-diarized therapy sessions with expert-written gold-standard notes in the iCARE format. We benchmarked eleven contemporary LLMs (nine open-source and two proprietary) in zero-shot and one-shot settings, evaluating outputs with lexical (BLEU, METEOR, ROUGE-L) and semantic (BERTScore, BLEURT, InfoLM) metrics and with TRACE (Trustworthiness, Relevance, Accuracy, Comprehensiveness, Expression), a five-domain human-evaluation framework we designed for mental-health documentation. Results Closed-source models consistently outperformed open-source ones, with GPT-4o-mini achieving the best overall automatic-evaluation scores and Gemini Pro excelling at interpretative sections such as crisis-marker identification. All models struggled with temporal reasoning, such as past-session and next-session details, and lexical overlap with human notes was low despite strong semantic alignment. In blinded expert review, clinical preference did not always mirror automatic benchmarks, with Mistral, a smaller open model, emerging as a surprise favourite. Conclusions The iCARE format, iHOPE dataset, and TRACE framework together provide a foundation for clinically valid, therapist-centred AI documentation that assists rather than replaces clinicians.

**Ваша слепая метка (калибровка):** ? AI-скрайбинг в психотерапии (iCARE): генерация клинических заметок и оценка риска; проверить полный текст на наличие поштучной оценки согласия по секциям риска (vs E4/-6)

**ИИ:** -6 · обе модели · другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM · LLMs write therapy session notes, scored by text-similarity metrics and expert ratings of quality; no coding of the same units against human codes.

**Решение:** =

---

### 1299 · R7580

**Artificial Intelligence Approximates Human Affect Ratings of Cannabis Images.**

2025 · medRxiv : the preprint server for health sciences · journal article, preprint, journalarticle · eng · https://doi.org/10.1101/2025.11.14.25339699

Abstract Cannabis imagery is proliferating online and can elicit affective responses related to use. Scalable tools are needed to evaluate how this proliferation could influence population health. This pilot study tested whether multimodal generative artificial intelligence (MGAI) can reproduce subjective human affect ratings of cannabis images. Four MGAI agents (model: gpt-4o-2024-11-20) were created to parallel the four human participant subgroups from Macatee et al. 2021, defined by primary method of cannabis administration (bong, bowl, joint/blunt, vaporizer). Using Macatee et al.’s participant instructions and standardized image set, each agent rated images of its primary method of administration on valence, arousal, and urge constructs. For each image-construct pair, n=100 ratings were generated in separate conversational threads using zero-shot prompting. Image-level MGAI mean ratings were compared with human mean ratings using Two One-Sided Tests of equivalence and Spearman correlations. Although formal statistical equivalence was rare (4% valence, 11% arousal, 3% urge), MGAI ratings approximated human ratings closely (Mean difference of mean ratings = – 0.31, SD = 1.23) and correlations between MGAI and human mean ratings were moderate to high: r s (valence) = 0.55, r s (arousal) = 0.34, r s (urge) = 0.56. MGAI also reproduced the parabolic relation between rating means and standard deviations observed in human data. These preliminary results indicate that MGAI can approximate human cannabis cue-reactivity patterns closely enough to justify continued refinement. MGAI could potentially be developed into a Cannabis Regulatory Science tool to aid regulatory oversight of online cannabis marketing.

**Ваша слепая метка (калибровка):** ? оценка аффекта и тяги по изображениям каннабиса (GPT-4o vs люди, rs=0.34-0.56); сомнения по I1 (стимулы - только изображения, без текста); проверить по полному тексту

**ИИ:** разошлись — Opus -7 (другое — напишите почему: GPT-4o rated affect responses to cannabis images, not text, and was compared with participants' own subjective reactions rather than with human coding of text.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): GPT-4o rates cannabis images (not text) on affect; compared to human mean ratings, but stimuli are images, not psychological text coding.)

**Решение:** -

---

### 1300 · R7589

**Introducing Synthetic Cognitive Capacity (SCC): A Novel Framework for Evaluating Generalizable Intelligence in Generative AI Systems**

2025 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5215716

_Аннотации нет — решайте по названию или ставьте `?`._

**Ваша слепая метка (калибровка):** ? SCC фреймворк оценки интеллекта систем ИИ; нет аннотации, проверить по полному тексту; если LLM объект - исключить как -2

**ИИ:** -6 · обе модели · другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM · Proposes a framework for evaluating AI intelligence, not LLM coding of psychological text against human raters; no abstract available.

**Решение:** =

---

### 1301 · R7894

**The Effectiveness of Style Vectors for Steering Large Language Models: A Human Evaluation**

2025 · IEEE Access · journalarticle, preprint/article, article · en · https://doi.org/10.1109/access.2025.3628500

Controlling the behavior of large language models (LLMs) at inference time is essential for aligning outputs with human abilities and safety requirements. Activation steering provides a lightweight alternative to prompt engineering and fine-tuning by directly modifying internal activations to guide generation. This research advances the literature in three significant directions. First, while previous work demonstrated the technical feasibility of steering emotional tone using automated classifiers, this paper presents the first human evaluation of activation steering concerning the emotional tone of LLM outputs, collecting over 7,000 crowd-sourced ratings from 190 participants via Prolific ( $n=190$ ). These ratings assess both perceived emotional intensity and overall text quality. Second, we find strong alignment between human and model-based quality ratings (mean $r=0.776$ , range 0.157–0.985), indicating automatic scoring can proxy perceived quality. Moderate steering strengths ( $\lambda \approx 0.15$ ) reliably amplify target emotions while preserving comprehensibility, with the strongest effects for disgust ( $\eta _{p}^{2} = 0.616$ ) and fear ( $\eta _{p}^{2} = 0.540$ ), and minimal effects for surprise ( $\eta _{p}^{2} = 0.042$ ). Finally, upgrading from Alpaca to LlaMA-3 yielded more consistent steering with significant effects across emotions and strengths (all $p \lt 0.001$ ). Inter-rater reliability was high (ICC = 0.71–0.87), underscoring the robustness of the findings. These findings support activation-based control as a scalable method for steering LLM behavior across affective dimensions.

**Ваша слепая метка (калибровка):** -2 люди оценивают перенос стиля в генерации текстов

**ИИ:** разошлись — Opus ? (неясен конструкт: Crowd workers rated emotion in steered LLM outputs. Model-human agreement is reported for text quality; it is unclear whether a model also rated emotion.); Sonnet -2 (люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает: Crowd workers rate emotional intensity and quality of steered LLM outputs. The human–model agreement concerns generic text quality, not a psychological construct in psychological text.)

**Решение:** -

---

### 1302 · R8453

**LLM for Semantic Role Labeling of Emotion Predicates in Russian**

2025 · Supercomputing Frontiers and Innovations · article · https://doi.org/10.14529/jsfi250303

Semantic role labeling (SRL) for morphologically rich languages, such as Russian, faces significant challenges due to complex case marking systems, free word order, and limited annotated resources. These challenges are particularly acute for emotion predicates, which require specialized linguistic expertise to capture distinctions between roles denoting those who feel, causes and objects of feelings. We propose a novel approach that leverages large language models to address SRL for Russian emotion predicates through few-shot in-context learning combined with predicate-specific instructions. Our method was evaluated on a manually annotated dataset of 169 sentences containing six emotion predicate groups extracted from Russian social media texts. We compared three state-of-the-art LLMs (Claude 3.7 Sonnet, GPT-5 Mini, and DeepSeek V3) against a RuELECTRA-based trained sequence labelling baseline using both exact and partial matching criteria. Claude 3.7 achieved the highest performance with 74.85% F1 score on partial matching, substantially outperforming the baseline (22.67%). For general predicates on FrameBank, our adapted method with GPT-5 Mini reached 85.0% F1 compared to the previous state-of-the-art of 80.1%. The LLM-based approach successfully handles complex linguistic phenomena, including syntactic zeros and multi-word arguments, while requiring minimal manually annotated training data. We demonstrate that LLM-based methods can significantly advance SRL for Russian by reducing dependency on large-scale annotated corpora while achieving competitive performance.

**Ваша слепая метка (калибровка):** -4 компьютерная лингвистика, семантические роли предикатов эмоций в русском FrameBank

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs label experiencer and cause roles of emotion predicates in social-media text against manual annotation; this is linguistic SRL, so it may not count as a psychological construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Linguistic semantic role labeling of emotion predicates in Russian; syntactic annotation, not coding of a psychological construct in text.)

**Решение:** -

---

### 1303 · R8491

**Expressing stigma and inappropriate responses prevents LLMs from safely replacing mental health providers.**

2025 · ACM Conference on Fairness, Accountability, and Transparency (FAccT) · journalarticle, book, review · en · https://doi.org/10.1145/3715275.3732039

Should a large language model (LLM) be used as a therapist? In this paper, we investigate the use of LLMs to replace mental health providers, a use case promoted in the tech startup and research space. We conduct a mapping review of therapy guides used by major medical institutions to identify crucial aspects of therapeutic relationships, such as the importance of a therapeutic alliance between therapist and client. We then assess the ability of LLMs to reproduce and adhere to these aspects of therapeutic relationships by conducting several experiments investigating the responses of current LLMs, such as gpt-4o. Contrary to best practices in the medical community, LLMs 1) express stigma toward those with mental health conditions and 2) respond inappropriately to certain common (and critical) conditions in naturalistic therapy settings—e.g., LLMs encourage clients’ delusional thinking, likely due to their sycophancy. This occurs even with larger and newer LLMs, indicating that current safety practices may not address these gaps. Furthermore, we note foundational and practical barriers to the adoption of LLMs as therapists, such as that a therapeutic alliance requires human characteristics (e.g., identity and stakes). For these reasons, we conclude that LLMs should not replace therapists, and we discuss alternative roles for LLMs in clinical therapy. Content warning: Contains content and examples related to sensitive mental health topics, including suicide.

**Ваша слепая метка (калибровка):** -2 психиатры оценивают ответы чат-ботов на бред и стигму; LLM объект

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM therapy responses judged for stigma/appropriateness; an LLM judge may have been validated against human labels, but the abstract doesn't say.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Mapping review plus experiments on LLM responses as therapists; no LLM coding against human labels evident.)

**Решение:** -

---

### 1304 · R9295

**Leveraging Large Language Models for Multi-Class and Multi-Label Detection of Drug Use and Overdose Symptoms on Social Media**

2025 · arXiv · preprint/article, preprint · https://doi.org/10.48550/arxiv.2504.12355

Drug overdose remains a critical global health issue, often driven by misuse of opioids, painkillers, and psychiatric medications. Traditional research methods face limitations, whereas social media offers real-time insights into self-reported substance use and overdose symptoms. This study proposes an AI-driven NLP framework trained on annotated social media data to detect commonly used drugs and associated overdose symptoms. Using a hybrid annotation strategy with LLMs and human annotators, we applied traditional ML models, neural networks, and advanced transformer-based models. Our framework achieved 98% accuracy in multi-class and 97% in multi-label classification, outperforming baseline models by up to 8%. These findings highlight the potential of AI for supporting public health surveillance and personalized intervention strategies.

**Ваша слепая метка (калибровка):** -4 токсикология, симптомы передозировки ПАВ в соцсетях, классификация на трансформерах/ML

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLMs and humans jointly annotated drug-use posts; the full text may report LLM–human annotation agreement, but the classifiers may be encoder-only.

**Решение:** =
