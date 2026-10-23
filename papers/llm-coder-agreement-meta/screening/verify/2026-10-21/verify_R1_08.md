# Проверка с метками ИИ, часть 8

Записи 1051–1200 из 1304, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

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

### 1051 · R7681

**A Shared Neural Marker Predicts Creative Performance Across Distinct Problem-Solving Tasks**

2025 · bioRxiv · preprint, ppr · en · https://doi.org/10.1101/2025.09.16.676681

Abstract Creativity is essential for innovation, yet the brain mechanisms supporting its moment-to-moment variability remain unclear. We hypothesize that creativity depends on dynamic fluctuations in neural flexibility, which determine the potential to generate creative solutions. Here, we identify a shared neural marker of “creativity potential” that predicts upcoming performance across distinct problem-solving tasks. Twenty-eight participants completed the Alternative Uses Test (AUT), a measure of divergent thinking, and the Fusion Innovation Test (FIT), which integrates divergent and convergent thinking. Responses were scored for novelty, feasibility, and goal attainment using validated GPT-based automated evaluation. EEG signals recorded prior to problem onset were used to decode single-trial creativity scores. A decoding model based on coherence features achieved robust performance ( r = 0.45, leave-one-trial-out) and generalized across individuals ( r = 0.34, leave-one-subject-out). Feature weights revealed a creativity potential network (CPN), characterized by frontal-temporal interactions in beta frequency band. Applying the model to resting-state recordings revealed ∼3-minute cycles of creativity potential, suggesting intrinsic brain dynamics shape readiness for creative problem-solving. These findings establish a shared neural marker of creativity that transcends task boundaries and individuals. Beyond advancing our understanding of creative cognition, this work opens the possibility of monitoring creativity potential in real time, with implications for neurofeedback and creativity enhancement in daily life. Significance statement Creativity allows us to generate novel and useful ideas, yet our ability to be creative fluctuates from moment to moment. Here we identify a neural marker of “creativity potential” that predicts upcoming creative performance across two distinct problem-solving tasks. Using EEG and GPT-based automated evaluation, we show that preparatory brain activity encodes creativity potential, generalizing across tasks and individuals. Furthermore, creativity potential fluctuates in intrinsic ∼3-minute cycles during rest. These results advance our understanding of the neural basis of creativity and provide a foundation for real-time monitoring and neurofeedback applications that may help individuals enhance their creative capacity.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · GPT scored AUT/FIT divergent-thinking responses as 'validated'; unclear whether this paper reports its own agreement with human raters.

**Решение:** =

---

### 1052 · R7684

**DepLLM: Fine-Tuning Large Language Models with a Chinese Dialogue Dataset for Depression Diagnosis via Mixture of Specialized Experts**

2025 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-981-96-5084-2_16

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · Fine-tuned LLM diagnoses depression from Chinese dialogues; no abstract, so it's unclear whether labels come from human coders or from diagnosis/self-report.

**Решение:** =

---

### 1053 · R7697

**Large language models may struggle to detect culturally embedded filicide-suicide risks.**

2025 · Asian journal of psychiatry · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.ajp.2025.104395

This study examines the capacity of six large language models (LLMs)-GPT-4o, GPT-o1, DeepSeek-R1, Claude 3.5 Sonnet, Sonar Large (LLaMA-3.1), and Gemma-2-2b-to detect risks of domestic violence, suicide, and filicide-suicide in the Taiwanese flash fiction "Barbecue". The story, narrated by a six-year-old girl, depicts family tension and subtle cues of potential filicide-suicide through charcoal-burning, a culturally recognized method in Taiwan. Each model was tasked with interpreting the story's risks, with roles simulating different mental health expertise levels. Results showed that all models detected domestic violence; however, only GPT-o1, Claude 3.5 Sonnet and Sonar Large identified the risk of suicide based on cultural cues. GPT-4o, DeepSeek-R1 and Gemma-2-2b missed the suicide risk, interpreting the mother's isolation as merely a psychological response. Notably, none of the models comprehended the cultural context behind the mother sparing her daughter, reflecting a gap in LLMs' understanding of non-Western sociocultural nuances. These findings highlight the limitations of LLMs in addressing culturally embedded risks, essential for effective mental health assessments.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLMs assess suicide/filicide risk in a single fictional story; the reference seems to be the authors' interpretation, not formal human coding.); Sonnet -7 (другое — напишите почему: Six LLMs interpret one flash-fiction story for risk; a single case with no human coding of the same texts and no agreement measure.)

**Решение:** -

---

### 1054 · R7698

**ProactiMate: Evaluating LLM-Based Chatbots for Behavior Change Interventions**

2025 · Authorea Preprints · preprint, ppr · en · https://doi.org/10.22541/au.174807396.68998051/v1

This paper explores the role of Large Language Models (LLMs) in promoting sustainable behavior, specifically in overcoming procrastination. Despite widespread recognition of the need for sustainable behavior change, individuals often struggle to break free from entrenched, unsustainable habits. LLMs, such as OpenAI’s GPT-4, represent a significant breakthrough in artificial intelligence and are increasingly used in behavior change interventions. This study introduces ProactiMate, a chatbot built using Motivational Interviewing (MI) principles and a Chain of Models approach for prompt engineering, designed to help users combat procrastination. Our research compares four LLMs (GPT-3.5 Turbo, LLaMA-3.2, Qwen-2.5, and SmolLM-1.7B) for output influence on procrastination avoidance, and assesses the impact of hyperparameters (temperature and top-p values) on procrastination avoidance. The findings reveal that GPT-3.5 outperforms other models across various evaluation metrics, and higher temperature and top-p values lead to more effective procrastination avoidance from automatic evaluation. According to expert evaluations, Qwen-2.5 and GPT-3.5 Turbo demonstrated notable effectiveness in fostering user engagement and motivation for addressing procrastination, with GPT-3.5 Turbo particularly distinguished by its capacity to provide strategies that help maintain long-term motivation. And GPT’s output aligns well with both automatic evaluation metrics and human evaluation. The results provide insights into the most effective ways to use LLMs in chatbot design, offering solutions for future usability testing.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly MI chatbot generation; unclear whether the 'automatic evaluation' of procrastination avoidance uses an LLM judge validated against expert ratings.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Chatbot generating MI-style responses, evaluated by automatic metrics and expert ratings of LLM outputs; no LLM coding of text against human codes.)

**Решение:** -

---

### 1055 · R7703

**LLM-as-a-Supervisor: Mistaken Therapeutic Behaviors Trigger Targeted Supervisory Feedback**

2025 · arXiv.org · journalarticle · https://doi.org/10.48550/arxiv.2508.09042

Although large language models (LLMs) hold significant promise in psychotherapy, their direct application in patient-facing scenarios raises ethical and safety concerns. Therefore, this work shifts towards developing an LLM as a supervisor to train real therapists. In addition to the privacy of clinical therapist training data, a fundamental contradiction complicates the training of therapeutic behaviors: clear feedback standards are necessary to ensure a controlled training system, yet there is no absolute"gold standard"for appropriate therapeutic behaviors in practice. In contrast, many common therapeutic mistakes are universal and identifiable, making them effective triggers for targeted feedback that can serve as clearer evidence. Motivated by this, we create a novel therapist-training paradigm: (1) guidelines for mistaken behaviors and targeted correction strategies are first established as standards; (2) a human-in-the-loop dialogue-feedback dataset is then constructed, where a mistake-prone agent intentionally makes standard mistakes during interviews naturally, and a supervisor agent locates and identifies mistakes and provides targeted feedback; (3) after fine-tuning on this dataset, the final supervisor model is provided for real therapist training. The detailed experimental results of automated, human and downstream assessments demonstrate that models fine-tuned on our dataset MATE, can provide high-quality feedback according to the clinical guideline, showing significant potential for the therapist training scenario.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM supervisor finds therapist mistakes in simulated dialogues; unclear whether its mistake labels are checked against human-coded labels or only feedback quality.

**Решение:** =

---

### 1056 · R7736

**P0407 Use of social listening to explore diet-related commentary from Inflammatory Bowel Disease social media groups**

2025 · Journal of Crohn s and Colitis · journalarticle, review, conference-abstract · en · https://doi.org/10.1093/ecco-jcc/jjae190.0581

Abstract Background People with inflammatory bowel disease (IBD) desire dietary information1 and use social media to fill the information gap.2 We aimed to capitalise on the large volume of commentary available in social media groups to determine frequently asked dietary questions and nutrition-related topics regarding this condition, utilising the Chat Generative Pre-trained Transformer 4 model (ChatGPT-4) to facilitate social listening analysis. Methods Following ethical guidelines and the approval of Facebook group administrators, social listening techniques were used to extract 11,945 online community comments (2021-2023). All data was deidentified and cleaned according to ethical standards, ensuring only context-specific comments were included for analysis. The data was analysed using content and thematic analysis and ChatGPT-4. Duplicate thematic analysis explored the meaning of the comments. The ChatGPT-4 large language model was trained on 10% of manually coded data using the few-shot learning technique.3 Results from both manual and ChatGPT-4 coding were manually reviewed for congruence to ensure the model’s analysis was suitable and could then be applied to all data. Results Moderate percentage agreement existed between manual and model coded data (75%). Medical therapy (31.2%) and diet-related comments (37.5%) dominated the conversations. A total of 350 unique diet-related queries emerged. Content analysis of these indicated the most commonly mentioned diet-related topics were management of gastrointestinal/extraintestinal symptoms (37.8%), natural therapies/dietary approaches to manage symptoms (20%) and maintenance of nutritional status (5.6%). Thematic analysis indicated five interrelated themes: desire for support and connection; exasperation and desire for information; open to considering advice from non-experts; desire for food to be thy medicine and IBD holds me back. Conclusion Using ChatGPT-4-enabled social listening of IBD Facebook groups, verified with traditional qualitative techniques, improved efficiency in handling large volumes of qualitative information and identified key dietary concerns prevalent in online discussions. Future studies should establish methodological and reporting standards for artificial intelligence-enabled social listening to ensure comparability between studies. With respect to individuals with IBD, Facebook groups provided immediate access to information and connection, compensating for the perceived lack of timely access to a knowledgeable and empathetic multidisciplinary care team. Improving access to specialized professionals, including dietitians well-versed in IBD, could reduce reliance on these platforms as a primary source of information. References 1.Miglioretto C, Beck E, Lambert K. A scoping review of the dietary information needs of people with inflammatory bowel disease. Nutr Diet. 2024;81(1):79-93. 2.Ni Z, Zhu L, Li S, Zhang Y, Zhao R. Characteristics and associated factors of health information-seeking behaviour among patients with inflammatory bowel disease in the digital era: a scoping review. BMC Public Health. 2024;24(1):307 - 22. 3.Chew R, Bollenbacher J, Wenger M, Speer J, Kim A. LLM-Assisted Content Analysis: Using Large Language Models to Support Deductive Coding. arXiv. 2023:1-27.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 coded IBD Facebook comments; 75% agreement with manual coding, but the codes look like diet/medical topics rather than psychological constructs.

**Решение:** =

---

### 1057 · R7737

**USE OF SOCIAL LISTENING TO EXPLORE DIET-RELATED COMMENTARY FROM INFLAMMATORY BOWEL DISEASE SOCIAL MEDIA GROUPS**

2025 · Inflammatory Bowel Diseases · article · en · https://doi.org/10.1093/ibd/izae282.133

Abstract BACKGROUND People with inflammatory bowel disease (IBD) desire dietary information. Social media groups are popular among this cohort to exchange dietary information. We aimed to capitalise on the large volume of commentary available in social media groups to determine frequently asked dietary questions and nutrition-related topics regarding this condition, utilising the Chat Generative Pre-trained Transformer 4 model (ChatGPT-4) to facilitate social listening analysis. METHOD Following ethical guidelines and the approval of Facebook group administrators, social listening techniques were used to extract 11,945 online community comments (from 2021-2023). All data was deidentified and cleaned according to ethical standards, ensuring only context-specific comments were included for analysis. The data was analysed using content and thematic analysis and ChatGPT-4. Thematic analysis was conducted in duplicate to explore the meaning of the comments. The ChatGPT-4 large language model was trained on 10% of manually coded data using the few-shot learning technique. Results from both manual and ChatGPT-4 coding were reviewed for congruence to ensure the artificial intelligence model was suitable and could then be applied to all data. RESULTS Moderate percentage agreement existed between manual and model coded data (75%). Medical therapy (31.2%) and diet-related comments (37.5%) dominated the conversations. A total of 350 unique diet-related queries emerged. Content analysis of these indicated the most commonly mentioned diet-related topics were management of gastrointestinal/extraintestinal symptoms (37.8%), natural therapies/dietary approaches to manage/control symptoms (20%) and maintenance of nutritional status (5.6%). Thematic analysis indicated five interrelated themes: a desire for support and connection; exasperation and desire for information; open to considering advice from non-experts; a desire for food to be thy medicine and IBD holds me back. CONCLUSION In this study, we utilised ChatGPT-4-enabled social listening of IBD Facebook groups and verified findings from this approach with traditional qualitative techniques. This approach reduced time and improved efficiency in extracting and exploring large volumes of qualitative information from a diverse sample. Future studies should establish methodological and reporting standards for artificial intelligence-enabled social listening to ensure comparability between studies. With respect to individuals with IBD, Facebook groups provided immediate access to information and connection, compensating for the perceived lack of timely access to a knowledgeable and empathetic multidisciplinary care team. Improving access to specialized professionals, including dietitians well-versed in IBD, could reduce reliance on these platforms as a primary source of information.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 coded IBD Facebook comments; 75% agreement with manual coding. Codes look mostly topical (diet, medical therapy), so whether they are psychological is unclear.

**Решение:** =

---

### 1058 · R7739

**WITHDRAWN**

2025 · preprint · en · https://doi.org/10.31234/osf.io/xdukm_v1

High-concentration oxygen inhalation is known to facilitate learning and attention.In this study, we tested whether a short-pulse high-concentration oxygen inhalation could enhance creativity.Thirty-four participants were assigned to either an oxygen group (n = 18) or a control group (n = 16) and completed 30 trials of the Alternative Uses Task (AUT) while 128-channel EEG was recorded.The AUT assesses divergent thinking by asking participants to generate alternative uses for everyday items, with the novelty and feasibility of their responses evaluated using an automated GPT-based method.Behavioral results showed that the oxygen group produced solutions with significantly higher novelty without compromising feasibility.Oxygen inhalation also stabilized performance by reducing trial-to-trial variability, with effects lasting at least five minutes after withdrawal.Notably, oxygen prevented the generation of low-novelty solutions while only marginally enhancing highly novel ideas.EEG analysis revealed that oxygen increased brain flexibility, indexed by a resting-state functional connectivity marker termed the Creativity Potential Network (CPN), with the enhancement particularly evident in slow thetaband oscillations.These findings provide behavioral and neural evidence that short-pulse highconcentration oxygen inhalation is a cost-effective method for facilitating creativity.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Withdrawn preprint; GPT scored AUT novelty and feasibility. The abstract doesn't say whether these scores were validated against human raters.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Oxygen inhalation and creativity EEG study; GPT scores AUT responses but no human-rater comparison is mentioned, and the record is a withdrawn preprint.)

**Решение:** -

---

### 1059 · R7756

**Natural Affect DEtection (NADE): Using Emojis to Infer Emotions from Text**

2025 · Journal of Marketing · journalarticle, article · en · https://doi.org/10.1177/00222429251315088

Emotions are central to consumer communications, and extracting them from user-generated online content is crucial for marketers, given that such consumer opinions significantly shape brand perceptions, influence purchase decisions, and provide essential insights for marketing analytics. To leverage vast user-generated data, marketers and researchers require advanced text-to-emotion converters. However, existing tools for fine-grained emotion extraction face several limitations: Lexica are constrained by their dictionaries, machine learning models by human-annotated training data, and large language models by insufficient validation. As a result, marketing research still tends to rely on mere sentiment detection instead of extracting more nuanced emotions from text. This article introduces NADE (Natural Affect DEtection), a novel text-to-emoji-to-emotion converter that first “emojifies” language and then converts these emojis into intensity measures of well-established, theory-grounded emotions. This approach addresses the limitations of existing tools by leveraging the inherent emotional information in emojis. Using human raters and state-of-the-art converters as benchmarks, the authors establish the benefits of exploiting emojis, validate NADE, and demonstrate its use in several marketing applications using data from various social media platforms. Users can apply the proposed converter through an easy-to-use online app and programming packages for Python and R.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Emotion detection in social-media text validated against human raters; unclear whether the benchmark converters include generative LLMs or if NADE is LLM-based.

**Решение:** =

---

### 1060 · R7782

**ChatGPT as a Competent Enough Judge in Validating Responses from a Divergent Thinking Task**

2025 · eScholarship (California Digital Library) · audiovisual/conference talk, journalarticle, article · en · https://doi.org/10.48448/w2kg-j913

The validation of responses in divergent thinking tasks is a critical yet understandardized step that should precede creativity scoring. However, inconsistencies related to human judges in this step may compromise the reliability of the results. This study introduces a systematic approach using ChatGPT to validate responses in the Alternate Uses Task (AUT) and compares its performance against six human judges. Analyzing 1245 AUT responses for common objects, we evaluated validity based on precisely defined criteria. Human judges exhibited significant variability, achieving unanimous agreement for only 58% of responses, while ChatGPT demonstrated significant alignment with human assessments, reflecting a capacity to replicate aggregated human judgment. These findings underscore the potential of Large Language Models to enhance objectivity and reproducibility in creativity research by automating response validation. We advocate for integrating AI-driven validation protocols into divergent thinking response evaluation and emphasize transparent reporting of criteria to advance methodological rigor in the field.

**ИИ:** + · обе модели · подсчёт методики · ChatGPT judged whether Alternate Uses Task responses were valid; the abstract compares its judgments with those of six human judges using the same criteria.

**Решение:** =

---

### 1061 · R7783

**Cognitive Representation in Large Language Models: Formalizing Psychological Constructs for Automated Questionnaire Generation**

2025 · eScholarship (California Digital Library) · audiovisual/conference talk, journalarticle, article · en · https://doi.org/10.48448/8rkq-s531

Understanding how psychological constructs are formalized into measurable representations remains a central challenge in cognitive science. This study examines large language models (LLMs) as cognitive artifacts capable of decomposing and formalizing such constructs. We evaluate LLMs’ conceptual alignment with human cognition across three tasks: predicting psychological attributes from text, generating theoretical construct explanations, and creating psychometrically valid assessment items. Results show strong representational fidelity for personality traits (average r=0.582), moderate alignment for depression (r=0.515), and emerging capabilities for anxiety (r =0.259). Expert evaluations confirm that LLMs produce theoretically coherent construct explanations (mean rating=4.33/5), while generated questionnaires exhibit convergent validity with established measures. Our findings position LLMs as effective tools for exploring cognitive representation systems and suggest that theory-driven prompting enables reliable, automated questionnaire development. This work bridges AI formalization techniques with core questions in cognitive science, offering a scalable framework for studying and constructing psychological measurement tools.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: The LLM predicts personality, depression and anxiety from text (r values), but it's unclear if the reference is human ratings or the writers' self-reports.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): LLMs predict trait scores from text (likely self-report criterion), generate construct explanations and items; experts rate LLM outputs. No human coding of the same texts.)

**Решение:** -

---

### 1062 · R7795

**Temperature and Persona Shape LLM Agent Consensus With Minimal Accuracy Gains in Qualitative Coding**

2025 · arXiv (Cornell University) · conferencepaper/, journalarticle, preprint/article · en · https://doi.org/10.48550/arxiv.2507.11198

Large Language Models (LLMs) enable new possibilities for qualitative research at scale, including annotation and qualitative coding of educational data. While LLM-based multi-agent systems (MAS) can emulate human coding workflows, their benefits over single LLM agents for coding remain poorly understood. To that end, we conducted an experimental study of how persona and temperature of component agents of a MAS shapes consensus-building and coding accuracy for dialog segments. LLMs were prompted to code these segments deductively using a mature codebook with 8 codes and high inter-rater reliability derived from prior research. Our open-source MAS mirrors deductive human coding through structured agent discussion and consensus arbitration. Using six open-source LLMs (with 3 to 32 billion parameters) and 18 experimental configurations, we analyze over 77,000 coding decisions against a gold-standard dataset of human-annotated transcripts from online math tutoring sessions facilitated by educational software. Temperature significantly impacted whether and when consensus was reached across all six LLMs. MAS with multiple personas (including neutral, assertive, or empathetic) significantly delayed consensus in four out of six LLMs compared to uniform personas. In three of those LLMs, higher temperatures significantly diminished the effects of multiple personas on consensus. However, neither temperature nor persona pairing led to robust improvements in coding accuracy. Single agents matched or outperformed MAS consensus in most conditions. Qualitative analysis of MAS collaboration and coding disagreement may, however, improve codebook design and human-AI coding. Accepted as full paper to the 19th International Conference on Educational Data Mining (EDM 2026)

**ИИ:** ? · обе модели · неясен конструкт · LLM coding of math tutoring dialogue checked against human gold labels; unclear whether the 8 codes capture psychological or interpersonal constructs.

**Решение:** =

---

### 1063 · R7834

**Evaluating the Reliability of Large Language Models in Identifying Psychological Constructs in Steam Reviews**

2025 · Queensland University of Technology eBooks · book-chapter · en · https://doi.org/10.5204/qutop/jhtz5964

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests an LLM reliability study coding psychological constructs in Steam reviews, likely compared with human coding.

**Решение:** =

---

### 1064 · R7861

**From Llama to language: prompt-engineering allows general-purpose artificial intelligence to rate narratives like expert psychologists.**

2025 · Frontiers in artificial intelligence · journal article, journalarticle, review · eng · https://doi.org/10.3389/frai.2025.1398885

Introduction Artificial intelligence (AI) has tremendous potential for use in psychology. Among the many applications that may benefit from development of AI applications is narrative-personality assessment. Use of these tools and research methods is notably time-consuming and resource intensive. AI has potential to address these issues in ways that would greatly reduce clinician and researcher burden. Nonetheless, it is unclear if current AI models are sufficiently sophisticated to perform the complex downstream tasks, such as narrative assessment. Methodology The purpose of this study is to explore if an expert-refined prompt generation process can enable AI-empowered chatbots to reliably and accurately rate narratives using the Social Cognition and Object Relations scales - Global Rating Method (SCORS-G). Experts generated prompt inputs by engaging in a detailed review of SCORS-G training materials. Prompts were then improved using an systematic process in which experts worked with Llama-2-70b to refine prompts. The utility of the prompts was then tested on two AI-empowered chatbots, ChatGPT-4 (OpenAI, 2023) and CLAUDE-2-100k , that were not used in the prompt refinement process. Results Results showed that the refined prompts allowed chatbots to reliably rate narratives at the global level, though accuracy varied across subscales. Averaging ratings from two chatbots notably improved reliability for the global score and all subscale scores. Experimentation indicated that expert-refined prompts outperformed basic prompts regarding interrater reliability and absolute agreement with gold standard ratings. Only the expert-refined prompts were able to generate acceptable single-rater interrater reliability estimates. Discussion Findings suggest that AI could significantly reduce the time and resource burdens on clinicians and researchers using narrative rating systems like the SCORS-G. Limitations and implications for future research are discussed.

**ИИ:** + · обе модели · подсчёт методики · GPT-4 and Claude-2 rated narratives on the SCORS-G scales; reliability and agreement were measured against expert gold-standard ratings.

**Решение:** =

---

### 1065 · R7916

**Speech-Integrated Modeling for Behavioral Coding in Counseling**

2025 · Annual Meeting of the Special Interest Group on Discourse and Dialogue · journalarticle, conference-paper · https://doi.org/10.18653/v1/2025.sigdial-1.10

Counseling and psychotherapy are predominantly conducted in spoken form, yet computational models to analyze these conversations often use only text transcripts as a main data source. This dependency overlooks important vocal cues such as tone, pitch, and prosody, hence restricting the models’ capacity to fully capture the dynamics of counselor-client interactions. We introduce Motivational Interviewing with Speech Cues (MISQ), a simple yet effective framework for enhancing the analysis of psychotherapy conversations that uses a large language model, a lightweight adapter, and a speech encoder to directly integrate speech cues. Our experiments show that MISQ consistently outperforms ( ∼ 5% relative improvement) approaches that omit or use speech indirectly, highlighting the essential role of speech in accurately capturing counselor and client behaviors.

**ИИ:** + · обе модели · кодирование сессий · An LLM-based framework (with a speech adapter) codes MI counselor and client behaviours, evaluated against human-annotated behaviour codes.

**Решение:** =

---

### 1066 · R7937

**Exploring the Potential of Large Language Models for Automated Safety Plan Scoring in Outpatient Mental Health Settings.**

2025 · medRxiv : the preprint server for health sciences · journal article, preprint, journalarticle · eng · https://doi.org/10.1101/2025.03.26.25324610

The Safety Planning Intervention (SPI) produces a plan to help understand and manage patients' suicidal crises. Since lower-quality safety plans have been associated with increased suicide risk, evaluating their quality has significant public health significance. We developed the Safety Planning Intervention Fidelity Rater (SPIFR), an automated tool that assesses the quality of SPI using various large language models (LLMs) including GPT-4, LLaMA 3, and o3-mini. Using 266 deidentified SPI from outpatient mental health settings in New York, LLMs analyzed four key steps: warning signs, internal coping strategies, making environments safe, and reasons for living. We compared the predictive performance of the three LLMs, optimizing scoring systems, prompts, and parameters. Results showed that LLaMA 3 and o3-mini outperformed GPT-4, with different step-specific scoring systems recommended based on weighted F1-scores. These findings highlight LLMs' potential to provide clinicians with timely and accurate feedback on SPI practices, enhancing this evidence-based suicide prevention strategy.

**ИИ:** + · обе модели · клиническая оценка · LLMs score the quality and fidelity of 266 suicide safety plans. Weighted F1 implies a comparison with human-rated reference scores.

**Решение:** =

---

### 1067 · R7943

**Case Reports Unlocked: Leveraging Retrieval-Augmented Generation with Large Language Models to Advance Research on Child Psychological Maltreatment**

2025 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5234616

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM with RAG coding child maltreatment case reports likely, may be validated against human coders.

**Решение:** =

---

### 1068 · R7960

**Development and validation of large language model rating scales for automatically transcribed psychological therapy sessions.**

2025 · Scientific reports · journal article, validation study, journalarticle · eng · https://doi.org/10.1038/s41598-025-14923-y

Traditional rating scales have shaped psychological research, but are resource-intensive and can burden participants. Large Language Models (LLMs) offer a tool to assess latent constructs in text. This study introduces LLM rating scales, a rating method that uses LLM responses instead of human ratings. Its application is demonstrated based on the development and validation of an LLM rating scale measuring patient engagement in transcripts of psychological therapies. Automatically transcribed videos of 1,131 sessions from 155 patients were analyzed using DISCOVER, a software framework for local multimodal human behavior analysis. The Llama 3.1 (8B) LLM rated 120 items on patient engagement, with the top eight items averaged to create a total engagement score ranging from 0 (low) to 100 (high). Psychometric properties were evaluated using the original sample, bootstrap resampling, and test folds. The LLM rating scale demonstrated normal distribution, strong reliability (ω = .953) and acceptable fit (CFI = .968, SRMR = .022), except RMSEA = .108. Validity was supported by significant correlations with engagement determinants (e.g., motivation, r = .413), processes (e.g., between-session efforts, r = .390), and outcomes (e.g., symptoms, r = −.304). Results remained robust across bootstrap and cross-validation analyses accounting for the hierarchical data structure. The LLM rating scale exhibited strong psychometric properties for measuring patient engagement, demonstrating the potential of the LLM rating scale approach as a psychological assessment tool. Importantly, this automated approach uses interpretable items, ensuring clear understanding of measured constructs, while supporting local implementation and protecting confidential data.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Llama rates patient engagement in therapy transcripts. Validation uses correlates (motivation, symptoms); unclear if any human rated engagement in the same sessions.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): Llama rates engagement in therapy transcripts, but validation uses psychometrics and correlations with other measures, not human ratings of the same texts.)

**Решение:** ?

---

### 1069 · R7974

**From Conversation to Automation: Leveraging LLMs for Problem-Solving Therapy Analysis**

2025 · Annual Meeting of the Association for Computational Linguistics · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2025.findings-acl.1292

Problem-solving therapy (PST) is a structured psychological approach that helps individuals manage stress and resolve personal issues by guiding them through problem identification, solution brainstorming, decision-making, and outcome evaluation. As mental health care increasingly adopts technologies like chatbots and large language models (LLMs), it is important to thoroughly understand how each session of PST is conducted before attempting to automate it. We developed a comprehensive framework for PST annotation using established PST Core Strategies and a set of novel Facilitative Strategies to analyze a corpus of real-world therapy transcripts to determine which strategies are most prevalent. Using various LLMs and transformer-based models, we found that GPT-4o outperformed all models, achieving the highest accuracy (0.76) in identifying all strategies. To gain deeper insights, we examined how strategies are applied by analyzing Therapeutic Dynamics (autonomy, self-disclosure, and metaphor), and linguistic patterns within our labeled data. Our research highlights LLMs' potential to automate therapy dialogue analysis, offering a scalable tool for mental health interventions. Our framework enhances PST by improving accessibility, effectiveness, and personalized support for therapists. 18 pages

**ИИ:** + · обе модели · кодирование сессий · GPT-4o and other LLMs label PST strategies in therapy transcripts annotated by humans; accuracy reported against human labels.

**Решение:** =

---

### 1070 · R7978

**Recording the Echoes of Suicide**

2025 · dissertation · en · https://doi.org/10.5463/thesis.1007

The overall aim of this thesis is to report on the development and implementation a standardized psychosocial autopsy to understand and prevent suicides in the Netherlands. Chapter 2 sets off with an exploration of stakeholder perceptions and needs concerning the implementation of a standardized psychosocial autopsy in the Netherlands. Standardized herein refers to a specific, predetermined set of guiding principles and conditions relating to processes involved with the psychosocial autopsy, ranging from the interview instrument to data collection and the translation into recommendations for prevention. In the second part of this dissertation, we present findings from psychosocial autopsy studies into adolescent suicides, and railway suicides. In chapter 3 we investigated the differences in suicide-related communication between young male and female (aged under 20 years old) suicide decedents. We used a qualitative analysis technique called the ‘Constant Comparative Method’101 to investigate 798 suicide-related communication events reported in interviews concerning 35 young male and female decedents. In chapter 4 we explored the meaning of social media in the lives of the adolescents who died by suicide. Interpretative Phenomenological Analysis was performed to assess the role social media had in the lives and to the deaths of these adolescents, with particular attention to the ways in which social media use affected their wellbeing and distress. Chapter 5 reports a mixed-methods psychosocial autopsy of railway suicides. In this study, we combined data detailing the sociodemographic characteristics of all railway suicide decedents in the Netherlands from 2017 and 2021, with data from in-depth psychosocial autopsy interviews concerning 39 railway suicide decedents. We started working towards a retrospective, dynamic, cross-sectional cohort that facilitates real-time monitoring of psychosocial characteristics of suicides and allows for an analysis of time-trends and clusters in the future. Chapter 6 describes findings from the pilot study with the new, mixed-methods psychosocial autopsy of suicide in young and middle-aged people. In chapter 7, the use of Large Language Models for automated deductive coding of interview data is explored and evaluated. In chapter 8, we discuss the findings from our research that have yet received little attention in scientific literature, reflect on lessons learned, and discuss the future of the psychosocial autopsy.

**ИИ:** разошлись — Opus + (кодирование по кодбуку: Chapter 7 evaluates LLM deductive coding of psychosocial autopsy suicide interviews, likely against human coding.); Sonnet ? (неясно, сравнивали ли с людьми: Dissertation with a chapter on LLM deductive coding of suicide psychosocial autopsy interviews. Human comparison is likely but not stated in the abstract, so full text is needed.)

**Решение:** +

---

### 1071 · R7985

**Capturing Patients' Lived Experiences with Chronic Pain through Motivational Interviewing and Information Extraction.**

2025 · Proceedings of the ... Workshop on Patient-Oriented Language Processing · audiovisual/conference talk, journal article, journalarticle · eng · https://doi.org/10.18653/v1/2025.cl4health-1.28

Chronic pain affects millions, yet traditional assessments often fail to capture patients' lived experiences comprehensively. In this study, we used a Motivational Interviewing framework to conduct semi-structured interviews with eleven adults experiencing chronic pain and then applied Natural Language Processing (NLP) to their narratives. We developed an annotation schema that integrates the International Classification of Functioning, Disability, and Health (ICF) with Aspect-Based Sentiment Analysis (ABSA) to convert unstructured narratives into structured representations of key patient experience dimensions. Furthermore, we evaluated whether Large Language Models (LLMs) can automatically extract information using this schema. Our findings advance scalable, patient-centered approaches to chronic pain assessment, paving the way for more effective, data-driven management strategies.

**ИИ:** + · обе модели · кодирование по кодбуку · LLMs apply ICF+ABSA annotation scheme to chronic-pain interview narratives, likely evaluated against human annotations of lived experience.

**Решение:** =

---

### 1072 · R7988

**The role of generative artificial intelligence in evaluating adherence to responsible press media reports on suicide: A multisite, three-language study.**

2025 · European psychiatry : the journal of the Association of European Psychiatrists · journal article, multicenter study, journalarticle · eng · https://doi.org/10.1192/j.eurpsy.2025.10037

Abstract Background Improving media adherence to World Health Organization (WHO) guidelines is crucial for preventing suicidal behaviors in the general population. However, there is currently no valid, rapid, and effective method to evaluate the adherence to these guidelines. Methods This comparative effectiveness study (January–August 2024) evaluated the ability of two artificial intelligence (AI) models (Claude Opus 3 and GPT-4O) to assess the adherence of media reports to WHO suicide-reporting guidelines. A total of 120 suicide-related articles (40 in English, 40 in Hebrew, and 40 in French) published within the past 5 years were sourced from prominent newspapers. Six trained human raters (two per language) independently evaluated articles based on a WHO guideline-based questionnaire addressing aspects, such as prominence, sensationalism, and prevention. The same articles were also processed using AI models. Intraclass correlation coefficients (ICCs) and Spearman correlations were calculated to assess agreement between human raters and AI models. Results Overall adherence to WHO guidelines was ~50% across all languages. Both AI models demonstrated strong agreement with human raters, with GPT-4O showing the highest agreement (ICC = 0.793 [0.702; 0.855]). The combined evaluations of GPT-4O and Claude Opus 3 yielded the highest reliability (ICC = 0.812 [0.731; 0.869]). Conclusions AI models can replicate human judgment in evaluating media adherence to WHO guidelines. However, they have limitations and should be used alongside human oversight. These findings may suggest that AI tools have the potential to enhance and promote responsible reporting practices among journalists and, thus, may support suicide prevention efforts globally.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o and Claude rated news articles' adherence to WHO suicide-reporting guidelines against human raters (ICC); unclear if this counts as a psychological construct.

**Решение:** =

---

### 1073 · R8023

**Large Language Model Agent Personality and Response Appropriateness: Evaluation by Human Linguistic Experts, LLM-as-Judge, and Natural Language Processing Model**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2510.23875

While Large Language Model (LLM)-based agents can be used to create highly engaging interactive applications through prompting personality traits and contextual data, effectively assessing their personalities has proven challenging. This novel interdisciplinary approach addresses this gap by combining agent development and linguistic analysis to assess the prompted personality of LLM-based agents in a poetry explanation task. We developed a novel, flexible question bank, informed by linguistic assessment criteria and human cognitive learning levels, offering a more comprehensive evaluation than current methods. By evaluating agent responses with natural language processing models, other LLMs, and human experts, our findings illustrate the limitations of purely deep learning solutions and emphasize the critical role of interdisciplinary design in agent development.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM-as-judge and human experts both assess agent personality in responses; unclear if they used the same scheme and if agreement is reported.

**Решение:** =

---

### 1074 · R8026

**Co‐Coding Classroom Dialogue: A Single Researcher Case Study of ChatGPT ‐Assisted Analysis in Science Education**

2025 · Journal of Computer Assisted Learning · journalarticle, article · en · https://doi.org/10.1111/jcal.70089

ABSTRACT Background Analysing classroom dialogue is a widely used approach for understanding students' learning, often requiring team‐based collaborative research. This presents a challenge for single researchers due to the labour‐intensive nature of the process. Emerging advancements in large language models (LLMs) such as ChatGPT, enhance qualitative research, particularly in inductive and deductive coding tasks. Objectives This study investigates the feasibility of a single researcher, the author of this study, collaborating with ChatGPT‐4o for qualitative coding of classroom dialogue data. The goal is to develop effective human–ChatGPT co‐coding methods and explore how such collaboration can enhance qualitative coding practices and provide insights into students' dialogue patterns. Methods The study analysed 1287 utterances from middle school science classes using a mixed‐method approach. A new codebook was developed through an inductive process using ChatGPT, followed by deductive coding conducted by both the researcher and ChatGPT. Kappa values were compared between human–human and human–ChatGPT coding. Disagreements in code assignments were resolved by the researcher, with reference to ChatGPT's rationale. Coded utterances were analysed using ordered network analysis (ONA) to visualise dialogue patterns in classes. Results and Conclusions The coding conducted by the researcher and ChatGPT resulted in a Cohen's kappa of 0.56, with the highest level of disagreement observed in the category of Meta‐cognition. The inductively co‐developed codebook helped uncover students dialogue patterns during experimental activities. Although ChatGPT exhibited limitations in interpreting nuanced and context‐dependent utterances, the findings highlight its potential as a valuable collaborator for solo researchers by supporting cognitive processes such as reflective interpretation and the development of new perspectives.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o and a human coded the same classroom dialogue utterances (κ=0.56); codes include metacognition, but it is unclear whether educational dialogue codes count as a psychological construct.

**Решение:** =

---

### 1075 · R8029

**A practical guide to implementing ChatGPT as a secondary coder in qualitative research**

2025 · International Journal of Accounting Information Systems · article · en · https://doi.org/10.1016/j.accinf.2025.100754

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; a methods guide on using ChatGPT as a secondary qualitative coder, likely accounting data, so a psychological construct is doubtful.

**Решение:** =

---

### 1076 · R8038

**Automated scoring of the Thought and Language Disorder Scale in schizophrenia using a large language model: reliability and comparison with clinicians**

2025 · EMPATH-IA@CHItaly · journalarticle

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · клиническая оценка · The title describes an LLM scoring thought and language disorder ratings in schizophrenia, compared with clinicians. There is no abstract, but the title fits.

**Решение:** =

---

### 1077 · R8044

**Securing the Weakest Link: Exploring Affective States Exploited in Phishing Emails With Large Language Models**

2025 · IEEE Access · journalarticle, article · en · https://doi.org/10.1109/access.2025.3615788

Cyberattacks often begin with a phishing email designed to exploit human factors, widely regarded as the weakest link in cybersecurity defences. Although previous research has identified factors that make individuals susceptible to scams and fraud, it is still unclear how phishing emails exploit these factors to trigger victims’ emotional responses. This paper addresses the following major questions: Which affective states are commonly exploited in phishing emails? Can they be reliably detected by Large Language Models (LLMs), and how do these models compare to human annotators? In this paper, we identify phishing-specific susceptibility factors inspired by interdisciplinary research literature from areas such as security, human-computer interaction (HCI), and psychology to explain the emotional responses (affective states) attackers seek to trigger in phishing emails. We conducted a pilot study and found that affective states can be key differentiators between phishing and non-phishing emails. Affective states commonly characterizing phishing emails, such as fear and greed, are almost absent in non-phishing emails. Additionally, phishing emails evoke higher emotional arousal levels than non-phishing emails in both subjects and bodies. Furthermore, we explore the capability of several LLMs (GPT-4, Llama 3, and Gemini Pro) in detecting affective states in over 5,000 phishing emails targeting six universities. Using reliability statistics, we compared LLMs’ performance with human annotators’ performance, mapped exploited affective states to the valence-arousal Cartesian space, examined LLMs’ performance in detecting phishing emails with special characters, and analyzed LLM hallucinations. We found that attackers commonly exploit curiosity, trust, and urgency in phishing email subjects and fear, urgency, and trust in their bodies. While fear and urgency elevate arousal levels, the valence of the email body generally remains neutral. Key affective state pairings include fear-urgency, urgency-trust, and trust-curiosity. Among LLMs, GPT4 outperforms Llama 3 and GeminiPro for both body and subject affective states, followed by Llama 3 and GeminiPro. These findings highlight the need for further research on affective states in phishing emails to improve detection systems.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-4, Llama 3 and Gemini annotated affective states (fear, urgency, trust) in phishing emails; reliability compared with human annotators.

**Решение:** =

---

### 1078 · R8052

**Passive Methods of Monitoring Suicide Risk in AI Conversations (Preprint)**

2025 · preprint · en · https://doi.org/10.2196/preprints.75272

BACKGROUND Most patients are not at elevated risk for suicide and active interview for assessment of suicide risk may not be reasonable. OBJECTIVE This paper describes passive monitoring of suicide risk factors from (a) text of conversations with the AI system or (b) medical history events reported to the AI system. We report the relationship between the number of risk factors to replicate the judgment of two experts regarding elevated risk of suicide. METHODS The adequacy of the text monitoring system was assessed by agreement in classification of risk factors by the LLM and a trained human reviewer, in 18 dialogues and 48 case descriptions; found in two books typically used to train clinicians on detection of suicide risks. The classification of medical history events into suicide risk factors was done using likelihood of suicide reported in the literature. Two clinicians rated relative risk levels of 86 pairs of dialogues/case descriptions. An index of risk was derived from these pairwise comparisons. This paper reports the percentage of variation in expert-assessed risk of suicide explained by the number of risk factors identified by the LLM. RESULTS On average the human rater and the LLM agreed in 97.03% (standard deviation of 3.98%) of risk factors in the 66 dialogues/case descriptions. The count of risk factors explained 30% of the variation in experts’ rating of the risk of suicide and achieved near-perfect accuracy (AROC =99%) in classifying dialogues into low vs high/moderate risk groups. CONCLUSIONS The proposed method of counting risk factors for suicide could be a reasonable strategy to passively monitor risk of suicide in AI conversations with depressed patients. Additional research is needed to compare the performance of this passive method compared to active suicide assessment.

**ИИ:** + · обе модели · клиническая оценка · An LLM classified suicide risk factors in dialogues and case descriptions; agreement with a trained human reviewer was 97%, and results were compared against expert risk ratings.

**Решение:** =

---

### 1079 · R8056

**SENTINEL-LLM: Suicide Ensemble-Based Text Intelligence and Natural Language Evaluation Through Large Language Models**

2025 · International Conference on Web Research (ICWR) · conference, conference-paper · en · https://doi.org/10.1109/icwr65219.2025.11006176

Detecting suicidal ideation in social media posts is a critical challenge in mental health intervention. This study introduces a novel suicide-focused Frequent-Rare (FR) Dictionary, specifically designed to enhance the sensitivity of Large Language Models (LLMs) to suicide-related linguistic patterns. Unlike conventional fine-tuning approaches, our methodology integrates domain-specific lexicons, leveraging TF-IDF weighting and sentiment-based adjustments to optimize LLMs for suicide risk detection. We fine-tune Qwen2.5, LLaMA3, and GPT-NEO with this enriched vocabulary, achieving remarkable performance improvements over their baseline versions. For instance, Qwen2.5's accuracy leaps from 30.42% to 92.93%, while GPT-NEO improves from 63.10% to 93.52%, demonstrating the profound impact of targeted linguistic augmentation. This advancement not only significantly boosts detection accuracy but also enhances model recall and precision, ensuring more reliable identification of high-risk cases. Our findings establish domain-aware finetuning as a powerful strategy for suicide risk assessment, highlighting the necessity of integrating specialized lexicons into mental health AI models.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Fine-tuned LLMs detect suicidal ideation in social media posts; unclear whether reference labels are human annotations or subreddit-derived.

**Решение:** =

---

### 1080 · R8078

**Measuring the Unspoken: A Disentanglement Model and Benchmark for Psychological Analysis in the Wild**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2512.04728

Generative psychological analysis of in-the-wild conversations faces two fundamental challenges: (1) existing Vision-Language Models (VLMs) fail to resolve Articulatory-Affective Ambiguity, where visual patterns of speech mimic emotional expressions; and (2) progress is stifled by a lack of verifiable evaluation metrics capable of assessing visual grounding and reasoning depth. We propose a complete ecosystem to address these twin challenges. First, we introduce Multilevel Insight Network for Disentanglement(MIND), a novel hierarchical visual encoder that introduces a Status Judgment module to algorithmically suppress ambiguous lip features based on their temporal feature variance, achieving explicit visual disentanglement. Second, we construct ConvoInsight-DB, a new large-scale dataset with expert annotations for micro-expressions and deep psychological inference. Third, Third, we designed the Mental Reasoning Insight Rating Metric (PRISM), an automated dimensional framework that uses expert-guided LLM to measure the multidimensional performance of large mental vision models. On our PRISM benchmark, MIND significantly outperforms all baselines, achieving a +86.95% gain in micro-expression detection over prior SOTA. Ablation studies confirm that our Status Judgment disentanglement module is the most critical component for this performance leap. Our code has been opened.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly a vision model, but the expert-guided LLM judge (PRISM) rates psychological inferences; unclear whether it was validated against expert ratings.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Visual VLM model for micro-expressions in video; the LLM-based PRISM metric isn't validated as coding text against human labels.)

**Решение:** -

---

### 1081 · R8080

**Leveraging ChatGPT for Enhancing Arabic NLP: Application for Semantic Role Labeling and Cross-Lingual Annotation Projection**

2025 · IEEE Access · journalarticle, article · en · https://doi.org/10.1109/access.2025.3525493

Semantic role labeling involves assigning semantic roles to sentence arguments, providing rich information for various NLP tasks and applications. Annotated corpora with semantic roles are a critical factor in improving the performance of semantic-based models. Besides, Arabic as a low resourced language, have to pay more attention to alternative methods to build such annotated corpora. To this end, two traditional methods have been intensively used, namely, manual annotation and crowed-resourced annotation. The former is highly precise but it demands substantial training and extensive resources, while, the latter, reduce human effort but often results in lower-quality annotations. Recently, Large language model (LLM) based conversational systems like ChatGPT have emerged as a promising tool for text annotation across various NLP tasks. In this paper, we leverage ChatGPT for two main sub-tasks in Arabic language processing. (1) Creating an Arabic annotated resource with emotional semantic roles from an English corpus, using cross-lingual annotation projection approach. (2) Annotating the Arabic corpus of emotional sentences with emotion categories and semantic roles. Furthermore, we evaluate ChatGPT’s potential for translating English sentences into Arabic. From the perspective of generalization, we test the performance of open-LLMs, specifically, mBERT, and mBART for the same tasks. The evaluation process includes assessing the impact of sentence complexity on the performance of ChatGPT, and open-LLMs in semantic role labeling, and cross-lingual annotation projection. We compared the obtained zero-shot annotation accuracy with that of human base annotations, where the GPT results achieved an accuracy of 0.94 for cross-lingual projection and 0.76 in semantic role labelling, While the open-LLMs achieved notable accuracies of 0.72, and 0.38 respectively.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT annotates Arabic emotional sentences with emotion categories and emotion semantic roles, compared with human annotations; mainly linguistic SRL focus.

**Решение:** =

---

### 1082 · R8086

**In-context learning capabilities of Large Language Models to detect suicide risk among adolescents from speech transcripts**

2025 · Interspeech (USB) · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.21437/interspeech.2025-2083

Early suicide risk detection in adolescents is critical yet hindered by scalability challenges of current assessments. This paper presents our approach to the first SpeechWellness Challenge (SW1), which aims to assess suicide risk in Chinese adolescents through speech analysis. Due to speech anonymization constraints, we focused on linguistic features, leveraging Large Language Models (LLMs) for transcript-based classification. Using DSPy for systematic prompt engineering, we developed a robust in-context learning approach that outperformed traditional fine-tuning on both linguistic and acoustic markers. Our systems achieved third and fourth places among 180+ submissions, with 0.68 accuracy (F1=0.7) using only transcripts. Ablation analyses showed that increasing prompt example improved performance (p=0.003), with varying effects across model types and sizes. These findings advance automated suicide risk assessment and demonstrate LLMs' value in mental health applications. Accepted to Interspeech 2025

**ИИ:** разошлись — Opus -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): LLM predicts adolescents' suicide risk labels from the SW1 challenge, which come from a MINI-KID clinical assessment, not human coding of the transcripts.); Sonnet ? (неясно, кто ставил эталонные метки: LLM classifies suicide risk from adolescent speech transcripts; unclear whether reference labels are human ratings or questionnaire/clinical risk status (likely criterion validity).)

**Решение:** -

---

### 1083 · R8089

**Using natural language processing to assess the impact of cognitive reappraisal**

2025 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/v8nsk_v1

Cognitive reappraisal is one of the most widely studied emotion regulation strategies. Recent research suggests that reappraisal involves shifting appraisals of situations along multiple dimensions. However, assessing these shifts is challenging as individuals can find it difficult or cumbersome to report upon them directly. We sought to determine whether natural language processing (NLP) methods, including large language models (LLMs), supplement self-reports of appraisals. We conducted an experiment with young adults (Study 1: n = 1943) that we replicated in a pre-registered experiment with adults (Study 2: n = 2449). Participants were randomized to regulate a recent upsetting situation via (1) cognitive reappraisal or (2) an active control (expressive writing). Self-reports of distress and appraisals were captured pre- and post-regulation. Text descriptions of the situation were captured pre- and post-regulation and analyzed with the Sentiment Analysis and Cognition Engine (SEANCE) as well as the LLM LLAMA 3. Across both samples, cognitive reappraisal (versus expressive writing) led to greater improvements in self-reported distress and changes in most appraisals. Cognitive reappraisal led to changes in the SEANCE metrics, but most of the effects were small and many were inconsistent across the samples. By contrast, cognitive reappraisal led to greater LLM-rated cognitive changes and overall changes in textual similarity and these were consistent across both samples. Self-report and NLP indices capture the process of cognitive reappraisal. In particular, the LLM reliably detected overall text changes as well as changes in cognition.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLaMA 3 rated cognitive change in reappraisal texts against self-reports; unclear whether human coders also rated the same texts.

**Решение:** =

---

### 1084 · R8092

**Does AI at Work Increase Stress? Text Mining Social Media About Human–AI Team Processes and AI Control**

2025 · Journal of Organizational Behavior · journalarticle, article · en · https://doi.org/10.1002/job.70000

ABSTRACT With rising use of artificial intelligence (AI) in organizations, alongside increasing mental health issues, we seek to understand how AI use affects human stress. Drawing on the automation–augmentation perspective, we propose that AI control over decision‐making thwarts human autonomy and thus contributes to stress. Drawing on models of teamwork and augmentation, we expect that human–AI team processes (i.e., transition, action, and interpersonal processes) help people meet their goals and reduce stress. Finally, we argue that human–AI team processes provide an important social resource, which buffers the stress‐enhancing role of AI control. To test our hypotheses, we analyzed over 2700 tweets. Using a trained large language model, validated against human ratings, we indexed key measures. Results confirm that high AI control was associated with increased stress, whereas human–AI team processes were associated with decreased stress. In support of the moderation hypothesis, two human–AI team processes (action and interpersonal) helped further reduce the stress‐enhancing effect of AI control. We discuss implications for work design theory and the importance of regulating levels of AI control to protect workers' mental health.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · A trained LLM rated stress and team processes in tweets, and those ratings were validated against human ratings.

**Решение:** =

---

### 1085 · R8114

**Assessing Heterogeneity in Sentiment Changes in Text-Based Counseling: Latent Class Trajectory Analysis.**

2025 · Journal of medical Internet research · journal article, journalarticle, article · eng · https://doi.org/10.2196/75091

Abstract Background Online text-based counseling services are becoming increasingly popular. However, their text-based nature and anonymity pose challenges in tracking and understanding shifts in help-seekers’ emotional experience within a session. These characteristics make it difficult for service providers to tailor interventions to individual needs, potentially diminishing service effectiveness and user satisfaction. Objective This study aimed to identify distinct within-session sentiment trajectories among help-seekers in online text-based counseling and examine key variables associated with trajectory membership. Methods A total of 6207 counseling sessions were randomly extracted from an online text-based counseling service in Hong Kong. A latent class trajectory analysis of help-seekers’ in-session sentiment was conducted using a growth mixture model (GMM) to identify latent groups of help-seekers exhibiting specific sentiment trajectories. Sentiment scores of help-seeker messages, labeled by ChatGPT, served as the primary variable for trajectory modeling. Subsequently, a multinomial logistic regression was performed to identify variables associated with class membership. Results The GMM identified 3 distinct sentiment trajectories as the best fit: (1) steady improvement (1171/6207, 18.9%), (2) deterioration (1119/6207, 18.0%), and (3) dip-then-rebound (3917/6207, 63.1%). Compared with the Dip-Then-Rebound Class, help-seekers in the Deterioration Class were more likely to report suicidal ideation (OR=1.28, 95% CIs 1.07-1.52, P=.006), present with family (OR=1.56, 95% CIs 1.19-2.08, P=.002) or physical health-related concerns (OR=1.67, 95% CIs 1.02-2.74, P=.04), have an unknown gender status (OR=1.32, 95% CIs 1.04-1.67, P=.02), access the service through the anonymous channel (OR=1.30, 95% CIs 1.03-1.63, P=.03), depart from the session prematurely (OR=9.76, 95% CIs 8.33-11.36, P<.001), and have shorter session durations (OR=0.77, 95% CIs 0.71-0.84, P<.001). Conclusions We identified 3 distinct trajectories of help-seekers’ in-session sentiment. Identifying the most likely trajectory at an early stage in the session could potentially help counselors adjust their approaches, thereby improving the effectiveness of text-based counseling and enhancing help-seeker satisfaction.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · ChatGPT labeled help-seeker sentiment in counseling sessions; the full text may include validation against human labels, but the abstract doesn't say.

**Решение:** =

---

### 1086 · R8124

**Can LLMs Help Recollect and Elaborate on Our Personal Experiences?**

2025 · Italian Conference on Computational Linguistics · journalarticle

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLMs and autobiographical narratives may involve coding personal memories against human ratings, or may be generation only.

**Решение:** =

---

### 1087 · R8132

**Public Health Discussions on Social Media: Evaluating Automated Sentiment Analysis Methods.**

2025 · JMIR formative research · journal article, journalarticle, article · eng · https://doi.org/10.2196/57395

Background Sentiment analysis is one of the most widely used methods for mining and examining text. Social media researchers need guidance on choosing between manual and automated sentiment analysis methods. Objective Popular sentiment analysis tools based on natural language processing (NLP; VADER [Valence Aware Dictionary for Sentiment Reasoning], TEXT2DATA [T2D], and Linguistic Inquiry and Word Count [LIWC-22]), and a large language model (ChatGPT 4.0) were compared with manually coded sentiment scores, as applied to the analysis of YouTube comments on videos discussing the opioid epidemic. Sentiment analysis methods were also examined regarding ease of programming, monetary cost, and other practical considerations. Methods Evaluation methods included descriptive statistics, receiver operating characteristic (ROC) curve analysis, confusion matrices, Cohen κ, accuracy, specificity, precision, sensitivity (recall), F 1 -score harmonic mean, and the Matthews correlation coefficient. An inductive, iterative approach to content analysis of the data was used to obtain manual sentiment codes. Results A subset of comments were analyzed by a second coder, producing good agreement between the 2 coders' judgments (κ=0.734). YouTube social media about the opioid crisis had many more negative comments (4286/4871, 88%) than positive comments (79/662, 12%), making it possible to evaluate the performance of sentiment analysis models in an unbalanced dataset. The tone summary measure from LIWC-22 performed better than other tools for estimating the prevalence of negative versus positive sentiment. According to the ROC curve analysis, VADER was best at classifying manually coded negative comments. A comparison of Cohen κ values indicated that NLP tools (VADER, followed by LIWC's tone and T2D) showed only fair agreement with manual coding. In contrast, ChatGPT 4.0 had poor agreement and failed to generate binary sentiment scores in 2 out of 3 attempts. Variations in accuracy, specificity, precision, sensitivity, F 1 -score, and MCC did not reveal a single superior model. F 1 -score harmonic means were 0.34-0.38 (SD 0.02) for NLP tools and very low (0.13) for ChatGPT 4.0. None of the MCCs reached a strong correlation level. Conclusions Researchers studying negative emotions, public worries, or dissatisfaction with social media face unique challenges in selecting models suitable for unbalanced datasets. We recommend VADER, the only cost-free tool we evaluated, due to its excellent discrimination, which can be further improved when the comments are at least 100 characters long. If estimating the prevalence of negative comments in an unbalanced dataset is important, we recommend the tone summary measure from LIWC-22. Researchers using T2D must know that it may only score some data and, compared with other methods, be more time-consuming and cost-prohibitive. A general-purpose large language model, ChatGPT 4.0, has yet to surpass the performance of NLP models, at least for unbalanced datasets with highly prevalent (7:1) negative comments.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT-4 sentiment coding of opioid-crisis YouTube comments compared with manual coding (κ); unclear whether generic sentiment counts as a psychological construct.

**Решение:** =

---

### 1088 · R8159

**Transforming User Defined Criteria into Explainable Indicators with an Integrated LLM AHP System**

2025 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2601.05267

Evaluating complex texts across domains requires converting user defined criteria into quantitative, explainable indicators, which is a persistent challenge in search and recommendation systems. Single prompt LLM evaluations suffer from complexity and latency issues, while criterion specific decomposition approaches rely on naive averaging or opaque black-box aggregation methods. We present an interpretable aggregation framework combining LLM scoring with the Analytic Hierarchy Process. Our method generates criterion specific scores via LLM as judge, measures discriminative power using Jensen Shannon distance, and derives statistically grounded weights through AHP pairwise comparison matrices. Experiments on Amazon review quality assessment and depression related text scoring demonstrate that our approach achieves high explainability and operational efficiency while maintaining comparable predictive power, making it suitable for real time latency sensitive web services.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · An LLM judge scores depression-related text, but the abstract doesn't say whether the labels it is checked against come from human coders.

**Решение:** =

---

### 1089 · R8161

**Humans Hallucinate Too: Language Models Identify and Correct Subjective Annotation Errors With Label-in-a-Haystack Prompts**

2025 · Conference on Empirical Methods in Natural Language Processing (EMNLP) · journalarticle, conference, conference-paper · en · https://doi.org/10.18653/v1/2025.emnlp-main.993

Modeling complex subjective tasks in Natural Language Processing, such as recognizing emotion and morality, is considerably challenging due to significant variation in human annotations. This variation often reflects reasonable differences in semantic interpretations rather than mere noise, necessitating methods to distinguish between legitimate subjectivity and error. We address this challenge by exploring label verification in these contexts using Large Language Models (LLMs). First, we propose a simple In-Context Learning binary filtering baseline that estimates the reasonableness of a document-label pair. We then introduce the Label-in-a-Haystack setting: the query and its label(s) are included in the demonstrations shown to LLMs, which are prompted to predict the label(s) again, while receiving task-specific instructions (e.g., emotion recognition) rather than label copying. We show how the failure to copy the label(s) to the output of the LLM are task-relevant and informative. Building on this, we propose the Label-in-a-Haystack Rectification (LiaHR) framework for subjective label correction: when the model outputs diverge from the reference gold labels, we assign the generated labels to the example instead of discarding it. This approach can be integrated into annotation pipelines to enhance signal-to-noise ratios. Comprehensive analyses, human evaluations, and ecological validity studies verify the utility of LiaHR for label correction. Code is available at https://github.com/gchochla/liahr.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: LLMs predict emotion and morality labels on human-annotated datasets, are compared with the gold labels, and are also checked by human evaluation.); Sonnet ? (другое: LLMs re-predict human-annotated emotion and morality labels and flag or correct them. It's unclear whether LLM–human agreement is reported as the main outcome.)

**Решение:** +

---

### 1090 · R8208

**SBDH-Reader: a large language model-powered method for extracting social and behavioral determinants of health from clinical notes.**

2025 · Journal of the American Medical Informatics Association : JAMIA · journal article, validation study, research support, n.i.h., extramural · eng · https://doi.org/10.1093/jamia/ocaf124

Abstract Objective Social and behavioral determinants of health (SBDH) are increasingly recognized as essential for prognostication and informing targeted interventions. Clinical notes often contain details about SBDH in unstructured format. Conventional extraction methods for these data tend to be labor intensive, inaccurate, and/or unscalable. In this study, we aim to develop and validate a large language model (LLM)-powered method to extract structured SBDH data from clinical notes through prompt engineering. Materials and Methods We developed SBDH-Reader to extract 6 categories of granular SBDH data by prompting GPT-4o, including employment, housing, marital status, and substance use including alcohol, tobacco, and drug use. SBDH-Reader was developed using 7225 notes from 6382 patients in the MIMIC-III database (2001–2012) and externally validated using 971 notes from 437 patients at The University of Texas Southwestern Medical Center (UTSW; 2022–2023). We evaluated SBDH-Reader’s performance against human-annotated ground truths based on precision, recall, F1, and confusion matrix. Results When tested on the UTSW validation set, SBDH-Reader achieved a macro-average F1 ranging from 0.94 to 0.98 across 6 SBDH categories. For clinically relevant adverse attributes, F1 ranged from 0.96 (employment; housing) to 0.99 (tobacco use). When extracting any adverse attributes across all SBDH categories, SBDH-Reader achieved an F1 of 0.97, recall of 0.97, and precision of 0.98 in the independent validation set. Discussion SBDH-Reader demonstrated strong performance in extracting structured SBDH data through effective prompt engineering of a general-purpose LLM, without the need for task-specific fine-tuning. Its modular design and adaptability to diverse datasets and documentation patterns support its applicability in real-world clinical settings. Conclusion SBDH-Reader has the potential to serve as a scalable and effective method for collecting real-time, patient-level SBDH data to support clinical research and care.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o extracts SBDH, including substance use, from clinical notes and is compared with human annotations; unclear whether these count as psychological constructs.

**Решение:** =

---

### 1091 · R8209

**SBDH-Reader: an LLM-powered method for extracting social and behavioral determinants of health from clinical notes.**

2025 · medRxiv : the preprint server for health sciences · journal article, preprint, ppr · eng · https://doi.org/10.1101/2025.02.19.25322576

ABSTRACT Objective Social and behavioral determinants of health (SBDH) are increasingly recognized as essential for prognostication and informing targeted interventions. Clinical notes often contain details about SBDH in unstructured format. Conventional extraction methods for these data tend to be labor intensive, inaccurate, and/or unscalable. In this study, we aim to develop and validate an LLM-powered method to extract structured SBDH data from clinical notes through prompt engineering. Materials and Methods We developed SBDH-Reader to extract six categories of granular SBDH data by prompting GPT-4o, including employment, housing, marital status, and substance use including alcohol, tobacco, and drug use. SBDH-Reader was developed using 7,225 notes from 6,382 patients in the MIMIC-III database (2001–2012) and externally validated using 971 notes from 437 patients at The University of Texas Southwestern Medical Center (UTSW; 2022–2023). We evaluated SBDH-Reader’s performance against human-annotated ground truths based on precision, recall, F1, and confusion matrix. Results When tested on the UTSW validation set, SBDH-Reader achieved a macro-average F1 ranging from 0.94 to 0.98 across six SBDH categories. For clinically relevant adverse attributes, F1 ranged from 0.96 (employment; housing) to 0.99 (tobacco use). When extracting any adverse attributes across all SBDH categories, SBDH-Reader achieved an F1 of 0.97, recall of 0.97, and precision of 0.98 in the independent validation set. Conclusion A general-purpose LLM can accurately extract structured SBDH data through effective prompt engineering. The SBDH-Reader has the potential to serve as a scalable and effective method for collecting real-time, patient-level SBDH data to support clinical research and care.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o extracts SBDH, including substance use, from clinical notes against human annotations; unclear whether these social determinants count as a psychological construct.

**Решение:** =

---

### 1092 · R8224

**Constructing Reliable Social Networks from Conversational Data: An Ensemble Prompt Engineering Approach with Uncertainty Quantification**

2025 · arXiv (Cornell University) · preprint/article, review, preprint · en · https://doi.org/10.48550/arxiv.2501.18912

Conversational data are central to the study of interaction dynamics and social structures across psychological research. However, constructing structured social networks from unstructured conversational data remains a major methodological challenge. This study presents a pipeline for network construction using prompt engineering. We employ an ensemble of five Large Language Models (LLMs) with majority voting to automate utterance classification, reducing dependence on manual coding without task-specific parameter fine-tuning. Classification uncertainty is assessed through an uncertainty quantification framework based on Shannon entropy, which can be used to prioritize ambiguous cases for review. The classified utterances are used to construct directed interaction networks for subsequent analysis. Reliability and accuracy are established relative to the criterion-referenced and human comparisons reported here rather than as unconditional guarantees across settings. We demonstrate the utility of this approach through two illustrative applications to classroom interaction data: network centrality analysis to characterize participant roles, and network mediation analysis using the additive and multiplicative effects network (AMEN) model to examine how interaction structures mediate the relationship between gender and mathematics performance. This pipeline provides a scalable foundation for automated network construction from conversational data across diverse research contexts.

**ИИ:** ? · обе модели · неясен конструкт · LLM ensemble classifies classroom utterances, with human comparison reported; unclear whether the categories capture a psychological or interpersonal construct.

**Решение:** =

---

### 1093 · R8237

**When LLM Therapists Become Salespeople: Evaluating Large Language Models for Ethical Motivational Interviewing**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2503.23566

Large language models (LLMs) have been actively applied in the mental health field. Recent research shows the promise of LLMs in applying psychotherapy, especially motivational interviewing (MI). However, there is a lack of studies investigating how language models understand MI ethics. Given the risks that malicious actors can use language models to apply MI for unethical purposes, it is important to evaluate their capability of differentiating ethical and unethical MI practices. Thus, this study investigates the ethical awareness of LLMs in MI with multiple experiments. Our findings show that LLMs have a moderate to strong level of knowledge in MI. However, their ethical standards are not aligned with the MI spirit, as they generated unethical responses and performed poorly in detecting unethical responses. We proposed a Chain-of-Ethic prompt to mitigate those risks and improve safety. Finally, our proposed strategy effectively improved ethical MI response generation and detection performance. These findings highlight the need for safety evaluations and guidelines for building ethical LLM-powered psychotherapy.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs detect unethical vs. ethical MI responses; it is unclear whether the reference labels come from human or expert annotation.

**Решение:** =

---

### 1094 · R8244

**Forma mentis networks predict creativity ratings of short texts via interpretable artificial intelligence in human and AI-simulated raters**

2025 · PsyArXiv · journalarticle, preprint/article, preprint · en · https://doi.org/10.31234/osf.io/6zpre_v3

Abstract Creativity is a fundamental skill of human cognition. We use textual forma mentis networks (TFMN) to extract network (semantic/syntactic associations) and emotional features from approximately one thousand human-, GPT3.5-, and Sonnet 3.7-generated stories. Using Explainable Artificial Intelligence (XAI) we test whether features relative to Mednick’s associative theory of creativity can explain creativity ratings assigned by humans or AI raters. Using XGBoost, we examine 5 scenarios: (i) human rating human stories, (ii) GPT-3.5 rating human stories, (iii) GPT-3.5 rating GPT-3.5 stories, (iv) Sonnet 3.7 rating human stories, and (v) Sonnet 3.7 rating Sonnet 3.7 stories. Our findings reveal that GPT-3.5 and Sonnet 3.7 ratings differ significantly from human ratings not only in terms of correlations but also because of feature patterns identified with XAI methods. GPT-3.5 and Sonnet 3.7 favour “their own” stories and rate human stories differently from humans. Feature importance analysis with SHAP scores shows that: (i) network features are more predictive for human creativity ratings but also for ratings by GPT-3.5 and Sonnet 3.7 for human stories; (ii) emotional features played a greater role than semantic/syntactic network structure in GPT-3.5 and Sonnet 3.7 rating their own stories. These quantitative results underscore key limitations in the ability of GPT-3.5 and Sonnet 3.7 to align with human assessments of creativity. We emphasise the need for caution when using AI models to assess and generate creative content, as they may not yet capture the nuanced complexity that characterises human creativity.

**ИИ:** + · обе модели · подсчёт методики · GPT-3.5 and Sonnet 3.7 rate the creativity of human-written stories; their ratings are correlated with and compared against human creativity ratings.

**Решение:** =

---

### 1095 · R8257

**Does GPT-4 Decode Richer Architecture of Emotion? Mapping Dimensional Structure with 99 Emotions**

2025 · preprint · en · https://doi.org/10.31219/osf.io/sdnbh_v2

Dimensional theories of emotion propose that affective experiences can be organized along continuous dimensions like Pleasure, Arousal, and Dominance. Recent computational methods for capturing these structures have relied primarily on word embeddings, requiring substantial technical expertise. This study examined whether prompting GPT-4 as a more accessible method, can capture dimensional emotion structure more effectively, by comparing both approaches against human spatial reasoning, with particular focus on analyzing extensive emotion vocabularies exceeding constraints of human cognitive capability. Study one established validity by testing six basic emotions, prompting showed strong convergence with human judgments, while embeddings showed no dimensional correlations and produced fundamentally different clustering patterns. Study two extended analysis to 99 emotion terms. Both approach identified two optimal clusters distinguished by both Pleasure and Dominance, though prompting produced clearer cluster separation. Particularly, arousal's discriminative power increased substantially from six to 99 emotions with prompting method only. This pattern may reflect how broader sampling of emotion terms provides sufficient linguistic contexts for arousal-related distinctions to emerge statistically. Together these results indicated that GPT prompting offers a promising methodological tool for dimensional emotion research, particularly in terms of uncovering patterns that only become visible when analysing a boarder sample of emotion terms.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 rates emotion words on PAD dimensions and is compared with human judgments, but the units are vocabulary items, not psychological texts.

**Решение:** =

---

### 1096 · R8262

**Validating the use of large language models for psychological text classification**

2025 · Frontiers in Social Psychology · journalarticle, article · en · https://doi.org/10.3389/frsps.2025.1460277

Large language models (LLMs) are being used to classify texts into categories informed by psychological theory (“psychological text classification”). However, the use of LLMs in psychological text classification requires validation, and it remains unclear exactly how psychologists should prompt and validate LLMs for this purpose. To address this gap, we examined the potential of using LLMs for psychological text classification, focusing on ways to ensure validity. We employed OpenAI's GPT-4o to classify (1) reported speech in online diaries, (2) other-initiations of conversational repair in Reddit dialogues, and (3) harm reported in healthcare complaints submitted to NHS hospitals and trusts. Employing a two-stage methodology, we developed and tested the validity of the prompts used to instruct GPT-4o using manually labeled data (N = 1,500 for each task). First, we iteratively developed three types of prompts using one-third of each manually coded dataset, examining their semantic validity, exploratory predictive validity, and content validity. Second, we performed a confirmatory predictive validity test on the final prompts using the remaining two-thirds of each dataset. Our findings contribute to the literature by demonstrating that LLMs can serve as valid coders of psychological phenomena in text, on the condition that researchers work with the LLM to secure semantic, predictive, and content validity. They also demonstrate the potential of using LLMs in rapid and cost-effective iterations over big qualitative datasets, enabling psychologists to explore and iteratively refine their concepts and operationalizations during manual coding and classifier development. Accordingly, as a secondary contribution, we demonstrate that LLMs enable an intellectual partnership with the researcher, defined by a synergistic and recursive text classification process where the LLM's generative nature facilitates validity checks. We argue that using LLMs for psychological text classification may signify a paradigm shift toward a novel, iterative approach that may improve the validity of psychological concepts and operationalizations.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-4o classified diaries, Reddit dialogues, and healthcare complaints for psychological constructs; its labels were validated against manually coded data.

**Решение:** =

---

### 1097 · R8268

**Bridging Human and Machine Perspectives: Integrating Large Language Models into Collaborative Coding and Peer Debriefing for Qualitative Inquiry**

2025 · LAK Workshops · journalarticle

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM collaborative qualitative coding at LAK workshop, psychological construct and human-coder comparison unclear.

**Решение:** =

---

### 1098 · R8326

**Comparing AI- and Human-Based Assessments of Medical Interview Transcripts Using a Generative AI Simulated Patient System. (Preprint)**

2025 · preprint · en · https://doi.org/10.2196/preprints.81673

BACKGROUND Generative AI is increasingly used in medical education, including the use of AI-based virtual patients to improve interview skills. However, it remains unclear how much AI-based assessment (ABA) differs from those of Human-based assessment (HBA). OBJECTIVE This study aimed to compare the quality of clinical interview assessments generated by an ABA using a virtual patient with those provided by a HBA conducted by clinical instructors. Additionally, it evaluated whether the use of AI could lead to a measurable reduction in evaluation time, and examined the level of agreement across participants with differing levels of clinical experience. METHODS A standardized leg-weakness case was implemented in an AI based virtual patient. Seven participants—two medical students, three resident physicians, and two attending physicians—each conducted an interview, and transcripts were scored with the Master Interview Rating Scale (MIRS; 25 items, 0–5 scale; total 0–125). Two evaluation strategies were compared. (1) ChatGPT o1-Pro scored each transcript five times with different random seeds to assess case specificity; total runtime for the five scores was automatically logged. (2) Five blinded clinical instructors , after a preparatory webinar reviewing the rubric and practicing on sample transcripts, each rated every transcript once and recorded clock time per rating. Because the five AI outputs are replicates of the same algorithm, intraclass correlation coefficients (ICC) were used to quantify repeatability rather than inter rater reliability. For human raters, we calculated ICC (2,1). Mean scores from both methods were compared, and agreement was quantified with Pearson’s r, Lin’s concordance correlation coefficient (ρc), Bland–Altman limits of agreement (LoA), internal consistency (Cronbach’s α), and ICC. Time efficiency was expressed as mean minutes per transcript and the relative percentage reduction achieved by AI scoring. RESULTS Mean interview scores were similar for ABA and HBA (52.1 ± 6.9 vs 53.7 ± 6.8). Agreement was strong (r = 0.92; ρc = 0.92) with minimal bias (+0.4 points; LoA −4.9 to +5.7). ABA showed higher internal consistency (α = 0.936 vs 0.863) and greater inter rater reliability (ICC = 0.77 vs 0.38). The coefficient of variation for ABA scores was roughly half that of HBA scores (6.6 % vs 13.9 %). In addition, ChatGPT completed each five run analysis in 4.3 ± 1.7 minutes compared with 10.3 ± 3.3 minutes for physicians, representing a 58 % reduction in assessment time. CONCLUSIONS ABA scores that closely matched HBA scores while demonstrating superior consistency and reliability. In the setting of virtual clinical interview transcripts, these preliminary findings suggest that ABA shows potential as a valid, rapid, and scalable alternative to HBA. When applied strategically, it could potentially furnish timely formative feedback, quantify efficiency gains, and reduce faculty workload without compromising assessment quality. Further research is needed to determine whether this can be achieved without compromising assessment quality.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT o1-Pro vs. clinical instructors scoring medical interview transcripts on MIRS; communication/interpersonal-skill construct may or may not qualify.

**Решение:** =

---

### 1099 · R8332

**Evaluating Generative Pretrained Transformer (GPT) models for suicide risk assessment in synthetic patient journal entries.**

2025 · BMC psychiatry · journal article, journalarticle, review · eng · https://doi.org/10.1186/s12888-025-07088-5

Over 700,000 individuals die by suicide globally each year, with rapid progression from suicidal ideation (SI) to attempt often precluding opportunities for intervention. Digital behavioral health (DBH) platforms offer novel means of collecting SI indicators outside the clinic, but the actionable utility of these data may be limited by clinician-dependent workflows such as reviewing patients' journaling exercises for signs of SI. Large language models (LLMs) provide a methodology to streamline this task by rapidly risk-stratifying text based on the presence and severity of SI; however, this application has yet to be reliably evaluated. To test this approach, we first generated and validated a corpus of 125 synthetic journal responses to prompts from a real-world DBH platform. The responses varied on the presence and severity of suicidal ideation, readability, length, use of emojis, and other common language features, allowing for over 1 trillion feature permutations. Next, five collaborating behavioral health experts worked independently to stratify these responses as no-, low-, moderate-, or high-risk SI. Finally, we risk-stratified the responses using several tailored implementations of OpenAI's Generative Pretrained Transformer (GPT) models and compared the results to those of our raters. Using clinician consensus as "ground truth," our ensemble LLM performed significantly above chance (30.38%) in exact risk-assessment agreement (65.60%; χ2 = 86.58). The ensemble model also aligned with 92% of clinicians' "do/do not intervene" decisions (Cohen's Kappa = 0.84) and achieved 94% sensitivity and 91% specificity in that task. Additional results of precision-recall, time-to-decision, and cost analyses are reported. While further testing and exploration of ethical considerations remain critical, our results offer preliminary evidence that LLM-powered risk stratification can serve as a powerful and cost-effective tool to enhance suicide prevention frameworks.

**ИИ:** + · обе модели · клиническая оценка · GPT models rated suicide risk in synthetic journal entries and were compared with five clinician raters; kappa reported.

**Решение:** =

---

### 1100 · R8335

**Evaluating the Impact of Counseling Skills in Online Platforms: An LLM-Based Analysis**

2025 · Pacific Asia Conference on Information Systems · journalarticle

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests LLM coding of counseling skills in online platforms, possibly validated against human coders.

**Решение:** =

---

### 1101 · R8346

**Applying Large Language Models with Active Learning and Ensemble Learning for Sentiment Recognition in Children’s Reading**

2025 · IEEE International Joint Conference on Neural Network · journalarticle, conference, conference-paper · https://doi.org/10.1109/ijcnn64981.2025.11228146

Sentiment recognition in children’s reading plays a crucial role in supporting their mental health and overall development. However, existing datasets often suffer from issues such as limited sample sizes, cross-linguistic ambiguities, and subjective human annotations, hindering the accurate modeling of complex emotional expressions in real-world contexts. These challenges result in suboptimal performance and limited generalization in sentiment recognition models. To address these issues, we leverage the extensive domain knowledge of Large Language Models (LLMs) to improve sentiment recognition performance. First, to mitigate data scarcity, we design a pretraining strategy that utilizes publicly available sentiment recognition datasets in both Chinese and English, enhancing LLMs’ ability to adapt to sentiment recognition tasks. Second, we propose a trustworthy ensemble strategy that integrates the outputs of LLMs across different languages. This strategy employs an uncertainty-aware weighted fusion mechanism to handle semantic ambiguities introduced by linguistic variations. Third, we develop an active learning framework for LLMs that iteratively resolves label inconsistencies, improving data quality and model performance. To validate the proposed methods, we construct a high-quality sentiment recognition dataset for children’s reading and incorporate the publicly available 40-Thai-Children dataset. Extensive experiments show that our method achieves an F1 score of 96.71% and accuracy of 97.42% on the collected dataset, and 86.31% F1 score and 87.02% accuracy on the 40-Thai-Children dataset. Furthermore, the active learning framework demonstrates its potential for generalization, improving accuracy from 82.05% to 86.32% in cross-domain testing by reducing data bias. The collected dataset and code are available at https://anonymous.4open.science/r/Children-s-Reading-Sentiment-Recognition-Dataset-745D.

**ИИ:** ? · обе модели · неясен конструкт · Fine-tuned LLMs classify emotion/sentiment in children's reading against human-annotated dataset; unclear whether texts express children's psychological states or generic sentiment.

**Решение:** =

---

### 1102 · R8347

**Generalizable Cross-Lingual Cognitive Distortion Detection with Standardized Annotations and Multi-Task Learning**

2025 · conference-paper · en · https://doi.org/10.18653/v1/2025.findings-acl.826

Cognitive distortion is a critical issue in psychology, with most existing studies based on Burns' cognitive distortion theory.However, differences in annotation standards lead to variations in building analysis tools, resulting in inconsistent analyses and limiting the generalizability of findings, especially in large-scale and cross-linguistic contexts.To address this issue, we collected all publicly available datasets (four in total) and conducted a series of experiments to evaluate the generalizability of various cross-linguistic models.The results indicate that models exhibit significant performance differences across datasets, highlighting the generalization problem.To mitigate this issue, we propose two solutions.First, we propose a multi-task learning model based on teacher student architecture solution, which demonstrates improved generalization performance in our experiments.Second, we introduce a new dataset (~5,000 samples) derived from reannotating existing open datasets to ensure standardized alignment.The annotation process we provided is interpretable and grounded in psychological principles.Based on this, we constructed large language models with cognitive reasoning chains, enhancing both generalizability and interpretability.This study identifies the generalization challenge in cognitive distortion research, and our experiments show that the proposed solutions significantly improve model performance.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: LLMs with reasoning chains detect cognitive distortions in text and are evaluated against human-annotated and re-annotated datasets.); Sonnet ? (неясно, сравнивали ли с людьми: Cognitive distortion detection with human-annotated datasets and LLMs with reasoning chains; unclear whether LLMs are evaluated against human labels versus mainly fine-tuned models.)

**Решение:** +

---

### 1103 · R8371

**An intelligent agent for sentence completion test: creation and application in depression assessment.**

2025 · Frontiers in psychology · journal article, journalarticle, article · eng · https://doi.org/10.3389/fpsyg.2025.1649905

During large-scale psychological screening, traditional self-report questionnaires face challenges like response deception or social desirability bias, while the Sentence Completion Test (SCT) as a projective technique shows potential but is limited by manual scoring and high costs. Leveraging advancements in Large Language Models (LLMs), this study integrates SCT's theoretical framework with LLM capabilities to develop a specialized set of SCT items for depression assessment in Chinese university students, using a self-built intelligent agent across three progressive empirical studies. Results show the agent demonstrates good reliability (Cronbach's α = 0.89-0.92) and validity, with high consistency to manual scoring ( r = 0.96), significant criterion correlations with the Beck Depression Inventory ( r = 0.89) and Self-Rating Depression Scale ( r = 0.85), confirmed structural validity via exploratory factor analysis. Furthermore, the intelligent agent could identify most invalid responses (F1 = 0.94, Accuracy = 0.99, Precision = 0.99, Recall = 0.90). This research marks a key milestone in SCT's intelligent transformation, driving innovation in psychological assessment and offering new academic and practical pathways.

**ИИ:** + · обе модели · подсчёт методики · LLM agent scores Sentence Completion Test responses for depression; consistency with manual scoring reported (r = 0.96).

**Решение:** =

---

### 1104 · R8372

**Creativity Potential Networks: Brain Markers for Novelty and Feasibility of Upcoming Divergent Thinking Solutions**

2025 · bioRxiv · preprint, ppr · en · https://doi.org/10.1101/2025.06.24.661027

Abstract The brain’s resting-state activity can serve as an indicator of cognitive flexibility and predict the likelihood of an upcoming Aha experience. This suggests that spontaneous neural dynamics reflect a person’s readiness for creative insight and underscore the potential of resting-state measures as biomarkers for anticipating creative breakthroughs. However, solutions accompanied by an Aha experience are not always truly creative, so it may be more valuable to identify biomarkers specifically linked to novelty and usefulness—two key dimensions of creative performance. To achieve this, we recruit 49 participants to complete the Alternative Uses Test, in which unconventional uses for everyday items are generated. We evaluate the responses for both novelty and feasibility using automated GPT-based methods and analyze resting-state EEG prior to the test. We find that creative performance is better predicted by interactions between different brain areas than by the activation of individual regions. Specifically, the degree centrality of theta-band functional connectivity in the right parietal and occipital areas correlates with novelty, while connectivity in the right middle and inferior frontal areas is associated with more feasible answers. These findings highlight distinct resting-state brain networks underlying the “creative potential” for novelty and feasibility, which could be leveraged to monitor and enhance brain flexibility. Significance statement Our study introduces the Creativity Potential Network (CPN), a resting-state brain network that can predict the novelty and feasibility of the upcoming solution in creative problem-solving. We show that the CPN is represented by communication between brain areas, and that the networks for novelty and feasibility are spatially distinct. This work provides a potential method to assess the potential to be creative without relying on behavioral measures and could be combined with neurofeedback to monitor and enhance brain flexibility.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · GPT scored Alternative Uses Test responses for novelty and feasibility; the full text may include validation against human ratings.

**Решение:** =

---

### 1105 · R8387

**From Keywords to Context: Bridging Expert Insight and Language Models for Multidimensional Sleep Health Classification in Clinical Notes**

2025 · medRxiv · preprint, ppr · en · https://doi.org/10.1101/2025.06.06.25329167

Abstract Accurate detection of multidimensional sleep health (MSH) information from electronic health records (EHRs) is critical for improving clinical decision-making but remains challenging due to sparse documentation and class imbalance. This study investigates whether integrating expert-guided annotations and keyword-based heuristics with large language models (LLMs) enhances the extraction of nuanced MSH indicators from clinical narratives. Using a novel, expertly annotated dataset (NCH-Sleep), we trained and evaluated models to classify clinical notes across nine clinically relevant MSH categories. Our baseline model demonstrated substantial predictive capability using raw text alone. Incorporating manually annotated spans (oracle annotations) dramatically improved performance, highlighting the benefit of targeted expert guidance. Additionally, employing curated keyword annotations within varying context windows significantly enhanced model interpretability while retaining strong predictive accuracy. Through detailed bias analyses, we identified consistent performance across demographics and clinical settings, although specific disparities underscored the importance of balanced expert oversight. Our findings emphasize the value of expert-informed supervision and heuristic approaches in building scalable, interpretable clinical NLP systems for sleep health classification.

**ИИ:** ? · обе модели · неясен конструкт · Expert-annotated sleep-health categories in clinical notes; unclear whether sleep counts as psychological and whether models are generative LLMs or encoders.

**Решение:** =

---

### 1106 · R8424

**Development of an Essay-type Assessment for Teaching Aptitude and Personality Using Generative AI-based Automated Scoring**

2025 · 교육학연구 · journalarticle, article · https://doi.org/10.30916/kera.63.6.215

This study aimed to enhance the practical applicability of essay-type assessments for pre-service teachers' teaching aptitude and personality, complementing the limitations of existing self-report measures. However, the viability of such assessments has been historically challenged by the time, cost, and reliability issues inherent in human scoring. To address this, the study adopted an integrated approach: first, developing a scenario-based assessment focused on educational problem-solving skills, and second, validating the application of generative AI (ChatGPT-4) for its automated scoring. A study with pre-service teachers revealed that while automated scoring was more lenient than human scoring, it demonstrated higher internal consistency and stability. The developed assessment showed discriminant validity through low correlations with self-report measures and convergent validity through its correlation with academic grades. These findings suggest the practical applicability and efficiency of an integrated assessment system that combines a scenario-based essay test with AI-powered scoring.

**ИИ:** + · обе модели · подсчёт методики · ChatGPT-4 scored essay responses on a teaching aptitude/personality assessment and was compared with human scoring; the construct is borderline psychological.

**Решение:** =

---

### 1107 · R8443

**Large Language Models Reveal Narrative Architectures of Veteran Transition Stress (Preprint)**

2025 · preprint · https://doi.org/10.2196/preprints.90155

UNSTRUCTURED The assessment of complex psychological phenomena has traditionally relied on resource-intensive qualitative methods or self-report measures that may not capture nuanced experiences. This study introduces and validates Generative Artificial Intelligence (GenAI) approach to automate the quantification and subsequent thematic analysis of veteran transition stress. Utilizing transcripts from interviews, a Large Language Model rated transition stress severity. These ratings correlated very highly with transition stress ratings from human experts and showed significant, theoretically congruent correlations with measures of clinical symptoms, reintegration difficulties, and veterans' self-ratings of transition difficulty. Critically, the AI-derived scores were used to quantitatively define high- and low-stress groups, enabling a targeted, automated thematic analysis. This analysis revealed distinct narrative structures of resilience and chronic stress characterized by themes of deployment, loss/trauma, material/emotional support and strategies. These findings suggest that GenAI offers a robust, scalable, and valid method for multidimensional analysis of complex, narrative-based psychological constructs.

**ИИ:** + · обе модели · клиническая оценка · An LLM rated transition-stress severity from veterans' interview transcripts, and its ratings correlated highly with human expert ratings of the same transcripts.

**Решение:** =

---

### 1108 · R8444

**The Capability of Large Language Models to Measure and Differentiate Psychiatric Conditions Through O-Shot Learning**

2025 · Biological Psychiatry · article · en · https://doi.org/10.1016/j.biopsych.2025.02.165

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM zero-shot measurement of psychiatric conditions may involve rating text against human or clinician labels.

**Решение:** =

---

### 1109 · R8451

**Toward Empathetic AI: Neural-Symbolic LLMs for Emotionally Aligned Conversations**

2025 · Lecture notes in social networks · conference-paper · en · https://doi.org/10.1007/978-3-032-13509-4_31

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. Probably about generating empathetic responses, but it may include emotion recognition checked against human labels.

**Решение:** =

---

### 1110 · R8464

**KoACD: The First Korean Adolescent Dataset for Cognitive Distortion Analysis via Role-Switching Multi-LLM Negotiation**

2025 · Conference on Empirical Methods in Natural Language Processing · journalarticle, conference, preprint/article · en · https://doi.org/10.18653/v1/2025.findings-emnlp.1202

Cognitive distortion refers to negative thinking patterns that can lead to mental health issues like depression and anxiety in adolescents. Previous studies using natural language processing (NLP) have focused mainly on small-scale adult datasets, with limited research on adolescents. This study introduces KoACD, the first large-scale dataset of cognitive distortions in Korean adolescents, containing 108,717 instances. We applied a multi-Large Language Model (LLM) negotiation method to refine distortion classification, enabling iterative feedback and role-switching between models to reduce bias and improve label consistency. In addition, we generated synthetic data using two approaches: cognitive clarification for textual clarity and cognitive balancing for diverse distortion representation. Validation through LLMs and expert evaluations showed that while LLMs classified distortions with explicit markers, they struggled with context-dependent reasoning, where human evaluators demonstrated higher accuracy. KoACD aims to enhance future research on cognitive distortion detection. The dataset and implementation details are publicly accessible. Accepted to Findings of EMNLP 2025

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Multi-LLM labelling of cognitive distortions with expert validation; unclear if experts coded the same texts independently or only judged LLM labels.); Sonnet + (бенчмарк с метками людей: Dataset paper where multi-LLM labels cognitive distortions in Korean adolescent text, validated against expert human evaluation showing LLM–human accuracy differences.)

**Решение:** +

---

### 1111 · R8487

**Advancement of divergent thinking assessment**

2025 · Unipub UB Graz (Universität Graz) · dissertation · en

Divergentes Denken gilt als ein zentraler Indikator für das kreative Potenzial einer Person und als valider Prädiktor für kreative Leistungen im Alltag. Obwohl divergente Denkaufgaben nach wie vor zu den gängigsten Verfahren zur Erfassung des kreativen Potenzials zählen, wird ihre psychometrische Qualität seit Langem kritisch diskutiert. Trotz zahlreicher methodischer Weiterentwicklungen in den letzten Jahren mangelt es bislang an einer systematischen Überprüfung hinsichtlich Psychometrie und klassischer Gütekriterien, was sich in einer erheblichen Heterogenität der eingesetzten Verfahren widerspiegelt. Ziel der vorliegenden Dissertation war es, zur Standardisierung der Erfassung divergenter Denkleistung – und darüber hinaus zur Weiterentwicklung der Kreativitätsmessung insgesamt – beizutragen. Insgesamt sechs Publikationen widmeten sich zentralen konzeptuellen und psychometrischen Fragestellungen. Eine erste systematische Übersichtsarbeit dokumentierte die Bandbreite bestehender Verfahren zur Erfassung des divergenten Denkens und zeigte zugleich zeitliche Entwicklungen im Feld auf. Eine zweite Studie verglich etablierte und neuartige Auswertungsmethoden hinsichtlich ihrer psychometrischen Güte und untersuchte zusätzlich den Einfluss der Aufgabenkomplexität. Vor dem Hintergrund der zunehmenden Bedeutung computergestützter Verfahren analysierte eine dritte Studie das Potenzial von Sprachmodellen (engl. Large Language Models) zur automatisierten Auswertung deutscher Antworten divergenter Denkaufgaben. Eine vierte Studie vertiefte diesen Ansatz, indem sie neben der Übereinstimmung automatisierter Bewertungen mit menschlichen Urteilen auch die psychometrische Qualität der erzeugten Scores untersuchte. Neben diesen spezifisch auf divergentes Denken ausgerichteten Studien erweiterte die Dissertation den Blick auf übergeordnete Fragen der Kreativitätsforschung: Eine fünfte Studie verglich professionelle Musiker:innen und Schauspieler:innen mit einer Kontrollgruppe von Nicht-Künstler:innen anhand verschiedener Kreativitätsmaße. Eine sechste Studie untersuchte, wie Menschen ihr kreatives Selbstbild begründen. Insgesamt greifen die Arbeiten grundlegende Herausforderungen und aktuelle Entwicklungen in der Kreativitätsdiagnostik auf. Sie leisten einen Beitrag zur empirischen Fundierung innovativer Methoden und liefern wichtige Impulse für zukünftige Entwicklungen und Fortschritte in der Kreativitätsforschung.

**ИИ:** + · обе модели · подсчёт методики · Dissertation studies compare large language model scoring of German divergent thinking responses with human ratings; need to check the model type in the full text.

**Решение:** =

---

### 1112 · R8500

**A Computational Framework to Identify Self-Aspects in Text**

2025 · Annual Meeting of the Association for Computational Linguistics · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.18653/v1/2025.acl-srw.47

This Ph.D. proposal introduces a plan to develop a computational framework to identify Self-aspects in text. The Self is a multifaceted construct and it is reflected in language. While it is described across disciplines like cognitive science and phenomenology, it remains underexplored in natural language processing (NLP). Many of the aspects of the Self align with psychological and other well-researched phenomena (e.g., those related to mental health), highlighting the need for systematic NLP-based analysis. In line with this, we plan to introduce an ontology of Self-aspects and a gold-standard annotated dataset. Using this foundation, we will develop and evaluate conventional discriminative models, generative large language models, and embedding-based retrieval approaches against four main criteria: interpretability, ground-truth adherence, accuracy, and computational efficiency. Top-performing models will be applied in case studies in mental health and empirical phenomenology. Accepted to ACL SRW 2025

**ИИ:** ? · обе модели · другое · PhD proposal planning an LLM evaluation against a human-annotated Self-aspects dataset; may hold no results yet, close to a protocol.

**Решение:** =

---

### 1113 · R8513

**Leveraging ChatGPT for thematic analysis of medical best practice advisory data.**

2025 · JAMIA open · journal article, journalarticle, article · eng · https://doi.org/10.1093/jamiaopen/ooaf126

Abstract Objectives To evaluate ChatGPT’s ability to perform thematic analysis of medical Best Practice Advisory (BPA) free-text comments and identify prompt engineering strategies that optimize performance. Materials and Methods We analyzed 778 BPA comments from a pilot AI-enabled clinical deterioration intervention at Stanford Hospital, categorized as reasons for deterioration (Category 1) and care team actions (Category 2). Prompt engineering strategies (role, context specification, stepwise instructions, few-shot prompting, and dialogue-based calibration) were tested on a 20% random subsample to determine the best-performing prompt. Using that prompt, ChatGPT conducted deductive coding on the full dataset followed by inductive analysis. Agreement with human coding was assessed as inter-rater reliability (IRR) using Cohen’s Kappa (κ). Results With structured prompts and calibration, ChatGPT achieved substantial agreement with human coding (κ = 0.76 for Category 1; κ = 0.78 for Category 2). Baseline agreement was higher for Category 1 than Category 2, reflecting differences in comment type and complexity, but calibration improved both. Inductive analysis yielded 9 themes, with ChatGPT-generated themes closely aligning with human coding. Discussion ChatGPT can accelerate qualitative analysis, but its rigor depends heavily on prompt engineering. Key strategies included role and context specification, pulse-check calibration, and safeguard techniques, which enhanced reliability and reproducibility. Conclusion This study demonstrates the feasibility of ChatGPT-assisted thematic analysis and introduces a structured approach for applying LLMs to qualitative analysis of clinical free-text data, underscoring prompt engineering as a methodological lever.

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: ChatGPT coding was checked against human coding (κ), but the codes are medical deterioration reasons and care actions, not psychological constructs.); Sonnet ? (неясен конструкт: ChatGPT deductive coding of clinician BPA comments with human kappa reported, but constructs (medical deterioration reasons, care team actions) may be non-psychological.)

**Решение:** -

---

### 1114 · R8550

**Evaluating LLM Alignment on Personality Inference from Real-World Interview Data (Preprint)**

2025 · preprint · https://doi.org/10.2196/preprints.87129

UNSTRUCTURED Large Language Models (LLMs) are increasingly deployed in roles requiring nuanced psychological understanding, such as emotional support agents, counselors, and decision-making assistants. However, their ability to interpret human personality traits, a critical aspect of such applications, remains unexplored, particularly in ecologically valid conversational settings. While prior work has simulated LLM ”personas” using discrete Big Five labels on social media data, the alignment of LLMs with continuous, ground-truth personality assessments derived from natural interactions is largely unexamined. To address this gap, we introduce a novel benchmark comprising semi-structured interview transcripts paired with validated continuous Big Five trait scores. Using this dataset, we systematically evaluate LLMs performance across three paradigms: (1) zero-shot and chain-of-thought prompting with GPT-4.1 Mini, (2) LoRA-based fine-tuning applied to both RoBERTa and Meta-LLaMA architectures. and (3) regression using static embedding from pretrained BERT and OpenAI’s text-embedding-3-small. Our results reveal that all Pearson correlations between model predictions and ground-truth personality traits remain below 0.26, highlighting the limited alignment of current LLMs with validated psychological constructs. Chain-of-thought prompting offers minimal gains over zero-shot, suggesting that personality inference relies more on latent semantic representation than explicit reasoning. These findings underscore the challenges of aligning LLMs with complex human attributes and motivate future work on trait-specific prompting, context-aware modeling, and alignment-oriented fine-tuning.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: GPT-4.1/LLaMA infer Big Five from interview transcripts; unclear if 'validated' trait scores are self-report or human-rated from interviews.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): LLMs predict interviewees' validated Big Five scores (questionnaire-based), not human coding of the transcripts; this is criterion validity, not coder agreement.)

**Решение:** -

---

### 1115 · R8558

**Improving the Robustness of Large Language Models in Extracting Social Determinants of Health**

2025 · Research Square · preprint · en · https://doi.org/10.21203/rs.3.rs-6255894/v1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (неясен конструкт: No abstract. Extracting social determinants of health with an LLM likely uses human annotations; SDOH may include psychosocial constructs, but this is unclear.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Title-only record on LLM extraction of social determinants of health from clinical text; this is a medical/social construct, not a psychological one, and the record has no abstract.)

**Решение:** ?

---

### 1116 · R8563

**Labeling Free-text Data using Language Model Ensembles**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2501.08413

Free-text responses are commonly collected in psychological studies, providing rich qualitative insights that quantitative measures may not capture. Labeling curated topics of research interest in free-text data by multiple trained human coders is typically labor-intensive and time-consuming. Though large language models (LLMs) excel in language processing, LLM-assisted labeling techniques relying on closed-source LLMs cannot be directly applied to free-text data, without explicit consent for external use. In this study, we propose a framework of assembling locally-deployable LLMs to enhance the labeling of predetermined topics in free-text data under privacy constraints. Analogous to annotation by multiple human raters, this framework leverages the heterogeneity of diverse open-source LLMs. The ensemble approach seeks a balance between the agreement and disagreement across LLMs, guided by a relevancy scoring methodology that utilizes embedding distances between topic descriptions and LLMs' reasoning. We evaluated the ensemble approach using both publicly accessible Reddit data from eating disorder related forums, and free-text responses from eating disorder patients, both complemented by human annotations. We found that: (1) there is heterogeneity in the performance of labeling among same-sized LLMs, with some showing low sensitivity but high precision, while others exhibit high sensitivity but low precision. (2) Compared to individual LLMs, the ensemble of LLMs achieved the highest accuracy and optimal precision-sensitivity trade-off in predicting human annotations. (3) The relevancy scores across LLMs showed greater agreement than dichotomous labels, indicating that the relevancy scoring method effectively mitigates the heterogeneity in LLMs' labeling.

**ИИ:** + · обе модели · кодирование по кодбуку · Open-source LLM ensemble labels topics in eating-disorder Reddit posts and patient free-text responses, and is evaluated against human annotations.

**Решение:** =

---

### 1117 · R8564

**Can Third Parties Read Our Emotions?**

2025 · Annual Meeting of the Association for Computational Linguistics (ACL) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2025.acl-long.1042

Natural Language Processing tasks that aim to infer an author's private states, e.g., emotions and opinions, from their written text, typically rely on datasets annotated by third-party annotators. However, the assumption that third-party annotators can accurately capture authors' private states remains largely unexamined. In this study, we present human subjects experiments on emotion recognition tasks that directly compare third-party annotations with first-party (author-provided) emotion labels. Our findings reveal significant limitations in third-party annotations-whether provided by human annotators or large language models (LLMs)-in faithfully representing authors' private states. However, LLMs outperform human annotators nearly across the board. We further explore methods to improve third-party annotation quality. We find that demographic similarity between first-party authors and third-party human annotators enhances annotation performance. While incorporating first-party demographic information into prompts leads to a marginal but statistically significant improvement in LLMs' performance. We introduce a framework for evaluating the limitations of third-party annotations and call for refined annotation practices to accurately represent and model authors' private states.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs and human third-party annotators both label emotions in the same texts, but the main reference is authors' self-labels; LLM–human agreement may not be reported.

**Решение:** =

---

### 1118 · R8580

**A Cascaded Multimodal Framework for Automatic Social Communication Severity Assessment in Children with Autism Spectrum Disorder**

2025 · Interspeech (USB) · journalarticle, conference-paper · 영어 · https://doi.org/10.21437/interspeech.2025-726

Autism Spectrum Disorder (ASD) is a neurodevelopmental condition characterized by deficits in social communication, affecting both language use and speech patterns. Since assessment relies on behavioral observations rather than standardized medical tests, developing an objective evaluation method is essential. Recognizing that ASD impacts both language and speech production, this study proposes a cascaded multi-modal framework for ASD severity assessment. The framework processes raw audio, generates transcriptions via automatic speech recognition, and extracts linguistic and acoustic features using speech-language foundation models. Given the atypical suprasegmental and segmental speech characteristics in ASD, two speech foundation models are employed. A co-attention mechanism then integrates these representations to estimate severity. Achieving a Spearman’s correlation of 0.5629 with human ratings, the proposed approach offers a scalable, fully automated ASD assessment tool.

**ИИ:** разошлись — Opus ? (другое: ASD severity estimated from transcripts and audio and compared with human ratings; unclear whether the language model is a generative LLM or an encoder.); Sonnet -5 (нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM: Speech/language foundation models with co-attention predict ASD severity from audio; not a generative LLM coding text, so no LLM–human coder agreement.)

**Решение:** -

---

### 1119 · R8588

**CliniChat: A Multi-Source Knowledge-Driven Framework for Clinical Interview Dialogue Reconstruction and Evaluation**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2504.10418

Large language models (LLMs) hold great promise for assisting clinical interviews due to their fluent interactive capabilities and extensive medical knowledge. However, the lack of high-quality interview dialogue data and widely accepted evaluation methods has significantly impeded this process. So we propose CliniChat, a framework that integrates multi-source knowledge to enable LLMs to simulate real-world clinical interviews. It consists of two modules: Clini-Recon and Clini-Eval, each responsible for reconstructing and evaluating interview dialogues, respectively. By incorporating three sources of knowledge, Clini-Recon transforms clinical notes into systematic, professional, and empathetic interview dialogues. Clini-Eval combines a comprehensive evaluation metric system with a two-phase automatic evaluation approach, enabling LLMs to assess interview performance like experts. We contribute MedQA-Dialog, a high-quality synthetic interview dialogue dataset, and CliniChatGLM, a model specialized for clinical interviews. Experimental results demonstrate that CliniChatGLM's interview capabilities undergo a comprehensive upgrade, particularly in history-taking, achieving state-of-the-art performance.

**ИИ:** ? · обе модели · неясен конструкт · LLM judge rates medical interview dialogues, possibly including empathy, possibly against experts; mostly medical history-taking, and human validation is unclear.

**Решение:** =

---

### 1120 · R8594

**IntentionFrame: A Semi-Structured, Multi-Aspect Framework for Fine-Grained Conversational Intention Understanding**

2025 · Conference on Empirical Methods in Natural Language Processing (EMNLP) · conference-paper · https://doi.org/10.18653/v1/2025.emnlp-main.1427

Understanding user intentions in multi-turn dialogues is critical for conversational AI, yet existing approaches-relying on rigid slot-value structures or unstructured free-text-fail to fully capture conversational complexity.In this paper, we propose IntentionFrame, a semistructured framework inspired by psychological and cognitive intention theories, which organizes conversational intents into four interrelated aspects: situation, emotion, action, and knowledge.This design not only retains interpretability but also provides LLMs with a rich context to accurately parse and respond to nuanced user inputs.To efficiently scale Inten-tionFrame annotations, we introduce a Weaklysupervised Reinforced Generation (WeRG) method that leverages a small set of highquality human annotations in conjunction with abundant coarsely labeled data.By applying reinforcement learning to balance these diverse signals, WeRG aims to effectively generate reliable IntentionFrame annotations, which serve as essential grounding for downstream tasks-leading to substantial improvements in response generation and task completion.Our experiments, supported by both automatic metrics and human evaluations, show that integrating IntentionFrame with WeRG significantly improves LLMs' conversational understanding and sets a new benchmark for intent analysis 1 .

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM generates intention annotations, including emotion, for general dialogues using some human annotations; unclear whether psychological coding agreement is reported.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Conversational intent annotation framework for dialogue systems; not coding psychological constructs against human coders, focuses on response generation and task completion.)

**Решение:** -

---

### 1121 · R8595

**LLM-based Conversational AI Therapist for Daily Functioning Screening and Psychotherapeutic Intervention via Everyday Smart Devices**

2025 · ACM Transactions on Computing for Healthcare · journalarticle, preprint/article, article · en · https://doi.org/10.1145/3712299

Despite the global mental health crisis, access to screenings, professionals, and treatments remains high. In collaboration with licensed psychotherapists, we propose a Conversational AI Therapist with psychotherapeutic Interventions (CaiTI), a platform that leverages large language models (LLM)s and smart devices to enable better mental health self-care. CaiTI can screen the day-to-day functioning using natural and psychotherapeutic conversations. CaiTI leverages reinforcement learning to provide personalized conversation flow. CaiTI can accurately understand and interpret user responses. When the user needs further attention during the conversation, CaiTI can provide conversational psychotherapeutic interventions, including cognitive behavioral therapy (CBT) and motivational interviewing (MI). Leveraging the datasets prepared by the licensed psychotherapists, we experiment and microbenchmark various LLMs' performance in tasks along CaiTI's conversation flow and discuss their strengths and weaknesses. With the psychotherapists, we implement CaiTI and conduct 14-day and 24-week studies. The study results, validated by therapists, demonstrate that CaiTI can converse with users naturally, accurately understand and interpret user responses, and provide psychotherapeutic interventions appropriately and effectively. We showcase the potential of CaiTI LLMs to assist the mental therapy diagnosis and treatment and improve day-to-day functioning screening and precautionary psychotherapeutic intervention systems.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLMs benchmarked on interpreting user responses with psychotherapist-prepared datasets; likely therapist-labelled classification, but the task details are unclear.

**Решение:** =

---

### 1122 · R8603

**A Psychological Strategy Annotation Method Using Multiple LLMs with a Chain of Thought Based on Deductive Reasoning**

2025 · Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC) · journalarticle, conference, conference-paper · https://doi.org/10.1109/apsipaasc65261.2025.11249074

Using appropriate psychological counseling strategies is critical for improving the quality of large language modeldriven mental health dialogues, yet a single large language model (LLM) often produces unreliable results due to ambiguous strategy definitions and degradation of thought in reasoning. Multi-LLM voting-based strategy annotation methods are often hampered in their overall decision-making performance due to the low accuracy of some individual models. To address this, we propose a multi-LLM system with a deductive-reasoning chain of thought. We built a dataset that comprises psychologist-client dialogue segments, each annotated with nine strategies by four professional psychologists. The system uses three LLMs as experts to generate initial strategy candidates, and then an LLM as a judge applies deductive reasoning-aligning dialogue evidence with strategy definitions-to annotate the optimal strategy. Experiments show that this approach outperforms single models, voting, and conventional chain-of-thought methods in F1 score and accuracy. This work advances LLM-based psychological strategy annotation, offering a reliable tool for mental health dialogue systems.

**ИИ:** + · обе модели · кодирование сессий · LLMs annotate counseling strategies in psychologist-client dialogue segments; evaluated against annotations by four professional psychologists (F1, accuracy).

**Решение:** =

---

### 1123 · R8615

**LLMCode: Evaluating and Enhancing Researcher-AI Alignment in Qualitative Analysis**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2504.16671

The use of large language models (LLMs) in qualitative analysis offers enhanced efficiency but raises questions about their alignment with the contextual nature of research for design (RfD). This research examines the trustworthiness of LLM-driven design insights, using qualitative coding as a case study to explore the interpretive processes central to RfD. We introduce LLMCode, an open-source tool integrating two metrics, namely Intersection over Union (IoU) and Modified Hausdorff Distance, to assess the alignment between human and LLM-generated insights. Across two studies involving 26 designers, we find that while the model performs well with deductive coding, its ability to emulate a designer's deeper interpretive lens over the data is limited, emphasising the importance of human-AI collaboration. Our results highlight a reciprocal dynamic where users refine LLM outputs and adapt their own perspectives based on the model's suggestions. These findings underscore the importance of fostering appropriate reliance on LLMs by designing tools that preserve interpretive depth while facilitating intuitive collaboration between designers and AI.

**ИИ:** ? · обе модели · неясен конструкт · Compares LLM and human qualitative coding of the same units (IoU); it is unclear whether the design-research data cover psychological constructs.

**Решение:** =

---

### 1124 · R8617

**LLM-based clustering of verbal and physiological content in psychotherapy sessions**

2025 · Padua Research Archive (University of Padova) · conference-paper · en

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM clustering of psychotherapy session content might involve comparison with human coding, but this is unclear.

**Решение:** =

---

### 1125 · R8619

**Processes Matter: How ML/GAI Approaches Could Support Open Qualitative Coding of Online Discourse Datasets**

2025 · Computer-supported collaborative learning/The Computer-Supported Collaborative Learning Conference · journalarticle, conference, preprint/article · en · https://doi.org/10.22318/cscl2025.114185

Open coding, a key inductive step in qualitative research, discovers and constructs concepts from human datasets. However, capturing extensive and nuanced aspects or "coding moments" can be challenging, especially with large discourse datasets. While some studies explore machine learning (ML)/Generative AI (GAI)'s potential for open coding, few evaluation studies exist. We compare open coding results by five recently published ML/GAI approaches and four human coders, using a dataset of online chat messages around a mobile learning software. Our systematic analysis reveals ML/GAI approaches' strengths and weaknesses, uncovering the complementary potential between humans and AI. Line-by-line AI approaches effectively identify content-based codes, while humans excel in interpreting conversational dynamics. We discussed how embedded analytical processes could shape the results of ML/GAI approaches. Instead of replacing humans in open coding, researchers should integrate AI with and according to their analytical processes, e.g., as parallel co-coders. This paper was recommended for acceptance as a long paper by CSCL reviewers, but ends up as a short paper. The arXiv version here is its longer form, revised with reviewers' comments

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Compares ML/GAI and human open coding of online chat messages about mobile learning software; there is no psychological construct, and the comparison is at the code-discovery level.); Sonnet ? (неясен конструкт: GAI open coding of learning-chat messages compared with four human coders; the psychological construct is unclear and open coding may not be unit-level agreement.)

**Решение:** -

---

### 1126 · R8634

**Enhancing the Objective Structured Clinical Examination Using Artificial Intelligence.**

2025 · Journal of doctoral nursing practice · journal article, med, journalarticle · eng · https://doi.org/10.1891/jdnp-2025-0061

Background: Artificial intelligence (AI) offers promising solutions for nurse practitioner education, especially in addressing challenges related to evaluating Objective Structured Clinical Examinations (OSCEs), such as examiner bias and delayed feedback. AI tools employing natural language processing and generative AI have the potential to enhance the accuracy and efficiency of clinical assessments. Objective: This product evaluation was conducted to determine whether AI-generated OSCE assessments align with faculty evaluations. Methods: A descriptive correlational design was used to assess product acceptability, feasibility, and agreement between AI and faculty assessments. A convenience sample of 13 nurse practitioner students was randomly divided into either a traditional evaluation group or an AI-assisted group. The AI-generated transcripts were scored using the same rubric used by faculty, and agreement was measured with Spearman's correlation, Cohen's Kappa, and interrater reliability percent agreement (IRR%). Results: Spearman's correlations ranged from negligible to moderate, with the highest in the physical/mental health exams category (r = .54, p < .05). However, Cohen's Kappa (.14-.41) and IRR% (31%-54%) showed weak agreement. Conclusions: These results suggest that AI feedback was inconsistent with faculty assessments, possibly due to technical issues and limitations in the rubric. Despite these limitations, this product evaluation demonstrated that the AI tool was easy to use and that faculty believed it could improve feedback quality. Implications for Nursing: These findings underscore both the promise and the current limitations of AI-supported clinical assessment. With thoughtful attention to these shortcomings, the ease of integration and capacity for enhanced learning offered by AI tools can help advance clinical competence and foster excellence in nurse practitioner and doctoral nursing education.

**ИИ:** разошлись — Opus ? (неясен конструкт: Generative AI scored OSCE transcripts against faculty rubric (kappa reported); construct is clinical competence, possibly including communication, so borderline.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: AI scoring of nurse practitioner OSCE transcripts against faculty is educational clinical-competence assessment, not a psychological construct; the LLM is also unspecified.)

**Решение:** -

---

### 1127 · R8641

**Therapeutic Chatbot for Suicidal Risk Teens Using Large Language Models**

2025 · 2025 IEEE XXXII International Conference on Electronics, Electrical Engineering and Computing (INTERCON) · conference, conference-paper · https://doi.org/10.1109/intercon67304.2025.11244711

Suicide poses a significant public health risk that disproportionately affects young people between the ages of 15 and 34. For this reason, this research proposes the development of an autonomous chatbot based on Large Language Models (LLMs) as a tool to detect and prevent suicidal thoughts in adolescents, in collaboration with the Peruvian Center for Suicidology and Suicide Prevention (SENTIDO). In addition, the chatbot integrates new advanced natural language processing technologies with cognitive-behavioral therapy to provide 80% emotional support in a personalized and accessible way 24 hours a day.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM chatbot meant to detect suicidal thoughts; the abstract doesn't say whether detection was checked against expert or clinician labels.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Development of an LLM therapeutic chatbot for suicidal teens; no coding or rating task compared against human labels is described.)

**Решение:** -

---

### 1128 · R8669

**Suicidal Comment Tree Dataset: Enhancing Risk Assessment and Prediction Through Contextual Analysis**

2025 · IEEE ... International Conference on Data Mining workshops · journalarticle, conference, preprint/article · https://doi.org/10.1109/icdmw69685.2025.00160

Suicide remains a critical global public health issue. While previous studies have provided valuable insights into detecting suicidal expressions in individual social media posts, limited attention has been paid to the analysis of longitudinal, sequential comment trees for predicting a user's evolving suicidal risk. Users, however, often reveal their intentions through historical posts and interactive comments over time. This study addresses this gap by investigating how the information in comment trees affects both the discrimination and prediction of users' suicidal risk levels. We constructed a high-quality annotated dataset, sourced from Reddit, which incorporates users' posting history and comments, using a refined four-label annotation framework based on the Columbia Suicide Severity Rating Scale (C-SSRS). Statistical analysis of the dataset, along with experimental results from Large Language Models (LLMs) experiments, demonstrates that incorporating comment trees data significantly enhances the discrimination and prediction of user suicidal risk levels. This research offers a novel insight to enhancing the detection accuracy of at-risk individuals, thereby providing a valuable foundation for early suicide intervention strategies.

**ИИ:** + · обе модели · бенчмарк с метками людей · Annotated Reddit dataset with C-SSRS-based suicide risk labels; LLMs evaluated against those human annotations.

**Решение:** =

---

### 1129 · R8673

**ChatThero: An LLM-Supported Chatbot for Behavior Change and Therapeutic Support in Addiction Recovery**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2508.20996

Substance use disorders (SUDs) affect millions of people, and relapses are common, requiring multi-session treatments. Access to care is limited, which contributes to the challenge of recovery support. We present \textbf{ChatThero}, an innovative low-cost, multi-session, stressor-aware, and memory-persistent autonomous \emph{language agent} designed to facilitate long-term behavior change and therapeutic support in addiction recovery. Unlike existing work that mostly finetuned large language models (LLMs) on patient-therapist conversation data, ChatThero was trained in a multi-agent simulated environment that mirrors real therapy. We created anonymized patient profiles from recovery communities (e.g., Reddit). We classify patients as \texttt{easy}, \texttt{medium}, and \texttt{difficult}, three scales representing their resistance to recovery. We created an external environment by introducing stressors (e.g., social determinants of health) to simulate real-world situations. We dynamically inject clinically-grounded therapeutic strategies (motivational interview and cognitive behavioral therapy). Our evaluation, conducted by both human (blinded clinicians) and LLM-as-Judge, shows that ChatThero is superior in empathy and clinical relevance. We show that stressor simulation improves robustness of ChatThero. Explicit stressors increase relapse-like setbacks, matching real-world patterns. We evaluate ChatThero with behavioral change metrics. On a 1--5 scale, ChatThero raises \texttt{motivation} by $+1.71$ points (from $2.39$ to $4.10$) and \texttt{confidence} by $+1.67$ points (from $1.52$ to $3.19$), substantially outperforming GPT-5. On \texttt{difficult} patients, ChatThero reaches the success milestone with $26\%$ fewer turns than GPT-5.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mainly a chatbot-generation paper, but blinded clinicians and an LLM-as-judge both rated empathy; whether they rated the same outputs or reported agreement is unclear.

**Решение:** =

---

### 1130 · R8687

**Automated Data Enrichment using Confidence-Aware Fine-Grained Debate among Open-Source LLMs for Mental Health and Online Safety**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2512.06227

Real-world indicators play an important role in many Natural Language Processing (NLP) applications, such as life events for mental health analysis and risky behaviours for online safety, yet labelling such information is often costly and/or difficult due to its multi-label and dynamic nature. Large Language Models (LLMs) show promising potential for automated annotation, but the multi-label setting remains challenging. In this work, we propose a Confidence-Aware Fine-Grained Debate (CFD) framework that simulates human collaborative annotation using fine-grained communication to better support automated multi-label enrichment. We introduce two expert-annotated resources: life-event and symptom annotation for a mental health well-being dataset, and a new online safety sharenting dataset. Experiments show that CFD achieves the most robust enrichment performance across tasks, and that the benefit of fine-grained confidence is influenced by its quality and variability. We further evaluate training-free strategies for incorporating enrichment indicators into downstream tasks and show that automated enrichment consistently improves performance, by up to 9.9 Macro-F1 points, with the most effective integration format depending on how the indicator relates to the downstream objective.

**ИИ:** + · обе модели · бенчмарк с метками людей · Open-source LLMs annotate life events and symptoms in mental-health text; the output is evaluated against new expert-annotated resources.

**Решение:** =

---

### 1131 · R8691

**BOARD # 437: Research in the Formation of Engineers: Prompting Socially Engaged Divergent Thinking in Engineering Design by Leveraging Generative AI**

2025 · ASEE Annual Conference & Exposition · conference-paper · en · https://doi.org/10.18260/1-2--55816

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; generative AI prompting divergent thinking in engineering students may include LLM scoring of ideas, but this is unclear.

**Решение:** =

---

### 1132 · R8718

**Digital Support or Cyber-Stigma? A Content Analysis of YouTube Comments on Depression and Schizophrenia Videos**

2025 · OSF · text/project, preprint · https://doi.org/10.17605/osf.io/h2gfq

Online forums discussing mental illness contain stigmatizing remarks that can magnify feelings of otherness and isolation, but also contain supportive remarks that can foster a sense of belonging and community. YouTube is one of the world’s largest online communities and is frequently used for mental health discourse. This study examined the likelihood of encountering supportive versus stigmatizing comments in response to YouTube videos on schizophrenia (a highly stigmatized topic) in comparison to depression, which is less stigmatized. We also examined associations between video characteristics (short- or long-form and level of self-disclosure) and stigmatizing or supportive comments. Large language model (LLM) prompts were engineered based on previous research and examination of comment content and refined until good human-LLM inter-rater reliability was achieved. The LLM was subsequently used to rate 6,656 comments from 368 videos on the extent of agreement with the presence of stigma and support. Across both disorders, significantly more comments were supportive (35.64%) than stigmatizing (6.34%). Forced-entry regression models showed that videos involving more self-disclosure had more supportive comments; support did not differ as a function of video (disorder) topic. On the other hand, schizophrenia-related videos had more stigmatizing comments. Surprisingly, short-form videos also had fewer stigmatizing comments, although this was not a strong effect. While YouTube may serve as a conduit for mental illness support, understanding video characteristics that generate more supportive and less stigmatizing reactions may enable the development of more helpful online mental health content.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · An LLM rated YouTube mental-health comments for stigma and support, and human–LLM inter-rater reliability was established before the full coding.

**Решение:** =

---

### 1133 · R8723

**A Systematic Evaluation of Large Language Models for PTSD Severity Estimation: The Role of Contextual Knowledge and Modeling Strategies**

2025 · Research Square · journalarticle, preprint/article, preprint · https://doi.org/10.21203/rs.3.rs-8376581/v1

Large language models (LLMs) are increasingly being used in a zero-shot (generative) fashion to assess mental health conditions, yet we have limited knowledge on what factors affect their accuracy. In this study, we use a clinical dataset of natural language narratives and self-reported PTSD severity scores from 1,437 individuals to comprehensively evaluate the performance of 11 state-of-the-art LLMs. To understand the factors affecting model's assessment accuracy, we systematically varied (i) contextual knowledge prompted to the models like subscale definitions, distribution summary, and interview questions, and (ii) modeling strategies including zero-shot vs few shot, amount of reasoning effort, model sizes, structured subscales vs direct scalar prediction, output rescaling and nine ensemble methods. Our findings indicate that (a) LLMs are most accurate when provided with detailed construct definitions and context of the narrative, even exceeding human raters agreement with self-reported scores; (b) increased reasoning effort leads to better estimation accuracy; (c) performance of open-weight models (Llama, DeepSeek) plateaus beyond 70B parameters while closed-weight (gpt-o3-mini, gpt-5) alternatives improve with newer generations; and (d) best performance is achieved when ensembling a supervised model with the zero-shot LLMs. Beyond agreement with self-reports, LLMs' estimates discriminated PTSD severity from depression, anxiety, and alcohol use, and prospectively predicted future mental healthcare expenditure. Together, these results suggest that contextual knowledge and modeling strategies meaningfully affect accuracy and clinical utility of LLM-based assessments of PTSD severity. 24 pages, 5 figures, 5 tables

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · The main reference is self-reported PTSD scores, but human raters also rated the narratives, so LLM–human agreement might be reportable.

**Решение:** =

---

### 1134 · R8740

**Patterns vs. Patients: Evaluating LLMs against Mental Health Professionals on Personality Disorder Diagnosis through First-Person Narratives**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2512.20298

Growing reliance on LLMs for psychiatric self-assessment raises questions about their ability to interpret qualitative patient narratives. This depth over breadth case study directly compares state-of-the-art LLMs and mental health professionals in assessing Borderline (BPD) and Narcissistic (NPD) Personality Disorders based on Polish-language first-person autobiographical accounts. Within our sample, the overall diagnostic scores of the top-performing Gemini Pro models (65.48%) were 21.91 percentage points higher than the average scores of the human professionals (43.57%). While both models and human experts excelled at identifying BPD (F1 = 83.4 &amp; F1 = 80.0, respectively), models severely underdiagnosed NPD (F1 = 6.7 vs. 50.0), showing a potential reluctance toward the value-laden term "narcissism." Qualitatively, models provided confident, elaborate justifications focused on patterns and formal categories, while human experts remained concise and cautious, emphasizing the patients' sense of self and temporal experience. Our findings demonstrate that while LLMs might be competent at interpreting complex first-person clinical data, their outputs still carry critical reliability and bias issues.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs and professionals both diagnose BPD/NPD from the same narratives; the reference seems to be the true diagnosis, but LLM–human agreement may be reported.

**Решение:** =

---

### 1135 · R8745

**Evaluating LLM Assisted Qualitative Analysis in Medical Education Research: A Comparison of Human and AI-Generated Thematic Coding (Preprint)**

2025 · JMIR Publications Inc. · posted-content, preprint · https://doi.org/10.2196/preprints.85572

BACKGROUND While LLM-assisted qualitative analysis could improve the efficiency and scalability of feedback-driven curricular refinement in medical education, how to best to leverage LLMs for qualitative analysis while ensuring quality outputs remains an open question. Prior work has demonstrated the feasibility of using LLMs for inductive and deducting coding tasks, but more needs to be known about how LLM-assisted thematic coding can best be deployed in a medical education context to maximize its strengths and guard against weaknesses. OBJECTIVE The objective of our study was to evaluate LLM performance in inductive code generation and deductive application of a human codebook using a student focus-group transcript to propose a framework for collaborating with AI in qualitative analysis. METHODS The qualitative data for this study consisted of a 1‑hour focus group with four second‑year medical students discussing a required AI‑driven clinical‑scenario tool (2‑Sigma). Three human coders conducted an inductive thematic analysis. For the same transcript, GPT‑4o generated inductive codes and applied the human codebook deductively. The researchers compared the alignment between the AI inductive codes and the human consensus codebook using three categories: Agreement, Reasonable Alternative, and Not Reasonable. Interrater reliability of AI deductive coding was evaluated using percent agreement and Cohen’s κ, with textual audits of discrepancies, including "misses" (failed to apply appropriate codes) and "misfires" (inappropriately applied codes). All analysis took place between February and July 2025. RESULTS In the inductive condition, GPT‑4o generated 137 initial codes, of which 31% (n=43) demonstrated Agreement with human codes, 26% (n=36) represented Reasonable Alternatives, and 42% (n=58) were classified as Not Reasonable. In the deductive condition, the mean percent agreement for AI application of human codes was 96% (SD 4%, range 79–100%) and mean κ was 0.71 (SD 0.26, range 0–1.00). Of all coding decisions, there were 57 misfires (2%) and 28 misses (1%); common patterns included over‑interpretation of tone, failure to recognize continued ideas across excerpts, and difficulty distinguishing hypothetical vs experienced features. Based on our findings, we suggest a roadmap that retains human interpretive control while leveraging AI scalability: humans first develop a contextually grounded codebook through inductive analysis, then use AI both as a creative partner to surface alternative codes and as a tool to apply the validated codebook across the dataset. CONCLUSIONS With targeted human oversight, an LLM can reliably apply an existing codebook and propose additional inductive codes, offering a scalable adjunct for qualitative analysis in medical education.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o applied a human codebook to a focus-group transcript (κ reported), but the codes cover students' views of an educational tool, so they may not be psychological.

**Решение:** =

---

### 1136 · R8750

**Expanding possibilities for generative AI in qualitative analysis: Fostering student feedback literacy through the application of a feedback quality rubric**

2025 · Journal of Engineering Education · article · en · https://doi.org/10.1002/jee.70024

Abstract Background Courses in engineering often use peer evaluation to monitor teamwork behaviors and team dynamics. The qualitative peer comments written for peer evaluations hold potential as a valuable source of formative feedback for students, yet little is known about their content and quality. Purpose This study uses a large language model (LLM) to apply a previously tested feedback quality rubric to peer feedback comments. Our research questions interrogate the reliability of LLMs for qualitative analysis with a rubric and use Bandura's self‐regulated learning theory to assess peer feedback quality of first‐year engineering students' comments. Method An open‐source, local LLM was used to score each comment according to four rubric criteria. Inter‐rater reliability (IRR) with human raters using Cohen's quadratic weighted kappa was the primary metric of reliability. Our assessment of peer feedback quality utilized descriptive statistics. Results The LLM achieved lower IRR than human raters, but the model's challenges mimic those of human raters. The model did achieve an excellent quadratic weighted kappa of 0.80 for one rubric criterion, which shows promise for LLM capability. For feedback quality, students generally wrote low‐ to medium‐quality comments that were infrequently grounded in specific teamwork behaviors. We identified five types of peer feedback that inform how students perceive the feedback process. Conclusions Our implementation of GAI suggests that LLMs can be helpful for rapid iteration of research designs, but consistent and reliable analysis with generative artificial intelligence (GAI) requires significant effort and testing. To develop feedback literacy, students must understand how to provide high‐quality feedback.

**ИИ:** ? · обе модели · неясен конструкт · LLM rubric scoring of peer feedback comments vs human raters (weighted kappa); unclear if feedback quality/teamwork counts as a psychological construct.

**Решение:** =

---

### 1137 · R8763

**Artificial Intelligence and Qualitative Analysis of Emergency Department Telemental Health Care Implementation Survey.**

2025 · Telemedicine journal and e-health : the official journal of the American Telemedicine Association · journal article, journalarticle, review · eng · https://doi.org/10.1089/tmj.2024.0555

Background : Implementation of telemental health care in emergency departments (EDs) in the United States (U.S.) has been increasing. Artificial intelligence (AI) can augment traditional qualitative research methods; little is known about its efficiency and accuracy. This study sought to understand ED directors' qualitative recommendations for improving telemental health care implementation and to understand how AI could facilitate analysis of qualitative survey responses. Methods : Directors at a nationally representative sample of 279 U.S. EDs that used telemental health care completed an open-ended survey question about improving telemental health care implementation between June 2022 and October 2023. Two groups of researchers completed independent qualitative coding of responses: one group used traditional qualitative methods, and one group used AI (ChatGPT 4.0) to facilitate analysis. Both groups independently developed a codebook, came to consensus on a combined codebook, and each group independently used it to code the survey responses. The two groups identified themes in ED directors' recommendations and compared codebooks and code application across traditional and AI approaches. Results : Themes included (1) recommendations for improving telemental health care directly and (2) recommendations for improving mental health care systems broadly to make telehealth more effective. ED directors' most common recommendation was enabling faster and more streamlined access to telemental health care. AI augmented human coding by identifying two valid codes not initially identified by human analysts. In codebook application, 75% of responses were coded consistently across AI and human coders. Conclusions and Relevance : For US EDs using telemental health care, there is a need to improve timeliness and efficiency of access to telemental health care.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT and humans applied the same codebook to open survey responses (75% agreement), but the content is implementation recommendations about mental-health services.

**Решение:** =

---

### 1138 · R8769

**Distinct Profiles of Run-to-Run Score Reliability and Expert-Panel Alignment Across Four LLM Evaluators of Simulated Japanese-Language AI-to-AI Counseling**

2025 · arXiv (Cornell University) · preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2507.02950

Large language models (LLMs) increasingly evaluate generated dialogue, but repeatable scores do not necessarily align with professional judgment. This observational fixed-benchmark study compared four configured LLM evaluator systems (GPT-5.5, Gemini 3.5 Flash, Claude Opus 4.8, and Fable 5) with aggregated ratings from 15 counseling experts on 18 complete simulated AI-to-AI counseling sessions conducted in Japanese. The sessions represented three counselor conditions across six prespecified client profiles. Each system scored every transcript three times on four motivational interviewing-informed dimensions and overall quality. All four systems assigned higher scores than the expert panel for softening sustain talk and overall quality, although differences varied across systems and constructs. Single-run intraclass correlation coefficients ranged from .33 to .96, showing that high run-to-run reliability did not ensure closer expert-panel alignment. Claude Opus 4.8 had the smallest mean absolute difference, whereas Fable 5 had an intermediate difference. In a secondary benchmark analysis, GPT-4-turbo sessions generated with the Structured Multi-step Dialogue Prompt received higher expert ratings than sessions generated by the same model with a minimal instruction for cultivating change talk, partnership, empathy, and overall quality; the softening sustain talk contrast remained uncertain. The fixed benchmark contained one session per counselor-condition-by-profile cell, so inference concerns these sessions rather than all possible stochastic regenerations. Run-to-run reliability, expert-panel alignment, and condition discrimination are separate properties of automated counseling evaluation. This benchmark supports construct-level assessment of LLM evaluators against professional judgment. 55 pages, 2 figures, 31 tables; supplemental material included; data and code at https://doi.org/10.5281/zenodo.22106028; preregistration and amendments at https://doi.org/10.17605/OSF.IO/VU286

**ИИ:** + · обе модели · LLM-судья · Four LLM evaluators scored simulated counseling transcripts on MI dimensions and were compared with ratings from a 15-expert panel.

**Решение:** =

---

### 1139 · R8770

**Can AI Sentiment Analysis Detect the Risk of Social Exclusion in SNS Conversations Before It Happens?**

2025 · Journal of Artificial Intelligence General science (JAIGS) · journalarticle, article · https://doi.org/10.60087/jaigs.v8i02.441

Early Detection of Social Exclusion Through Sentiment Analysis: Today, cyberbullying is growing rapidly at a startling rate, causing serious emotional and psychological harm to children and young adults. Social exclusion in online settings is recognized as one of the primary driving forces to this issue which is why it is essential to be able to identify these exclusionary signs early on is crucial to successful intervention. Thus, this study evaluates the potential of AI models like Open AI’s ChatGPT in detecting early signals that indicate social isolation in simulated social networking services (SNS). A dataset of 6 conversational scenarios (bullying, neutral, and positive) with a total of 24 utterances were created and assessed with sentiment labels, risk categories, and sentiment intensity scores. The evaluations from ChatGPT’s algorithm were then compared to human-coded annotations. Bullying scenarios consistently scored higher in the risk range (0.7-1.0) with strongly negative sentiment tables, whereas neutral and positive scenarios clustered near zero, demonstrating clear polarizations. Additionally, there was a high degree of agreement between human annotations and model evaluations especially when it came to distinguishing between neural encounters and high-risk bullying. Contrastingly, it failed to show an accuracy with identifying more subtle kinds of exclusion capturing the nuances behind expression. Results reflected that GPT’s model served to be an effective system for early warning toward dangerous interactions in social media settings. Although there is limited ecological validity due to the conversation data being simulated, the results act as a fundamental paradigm for using sentiment analysis to reduce cyberbullying.

**ИИ:** + · обе модели · кодирование по кодбуку · ChatGPT labelled sentiment and social-exclusion risk in simulated SNS utterances; these labels were compared with human-coded annotations.

**Решение:** =

---

### 1140 · R8801

**Interpretable Depression Detection from Social Media Text Using LLM-Derived Embeddings**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2506.06616

Accurate and interpretable detection of depressive language in social media can support early identification of mental health conditions and inform timely interventions. In this paper, we investigate the use of large language models (LLMs) and traditional machine learning classifiers for three social media-based mental health prediction tasks: binary depression classification, depression severity classification, and differential diagnosis among depression, PTSD, and anxiety. We compare zero-shot LLMs with supervised classifiers trained on conventional text embeddings, psycholinguistic features, and embeddings derived from LLM-generated mental health summaries. Across multiple publicly available social media text datasets and five-fold cross-validation experiments, we find that zero-shot LLMs exhibit strong performance and generalization in binary depression classification, but struggle with fine-grained severity prediction. In contrast, supervised models trained on LLM summary embeddings often achieve more accurate and consistent performance, particularly for multi-class and ordinal classification tasks. These findings highlight both the strengths and limitations of current LLMs for mental health prediction and suggest that using LLMs as semantic interpreters, rather than solely as end-to-end classifiers, may provide a promising direction for building more effective and interpretable mental health assessment systems. This version of the contribution has been accepted for publication at ICAI 2026, after peer review but is not the Version of Record and does not reflect post-acceptance improvements, or any corrections

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Zero-shot LLMs classify depression and severity in public social-media datasets; unclear whether labels come from human annotators or self-report.

**Решение:** =

---

### 1141 · R8808

**Comprehensive Evaluation and Design Strategies for Japanese Counseling AIs Using Large Language Models**

2025 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/j2fsq_v1

This study simultaneously evaluated three types of systems in Japanese counseling dialogues: counselor AIs (GPT-4-turbo in a zero-shot setting with a Structured Multi-Dialogue Prompt [SMDP] and Claude 3-Opus with SMDP), a client AI, and counseling-evaluation AIs (o3, Claude 3.7-Sonnet, and Gemini-2.5-pro). Introducing the SMDP significantly improved human experts’ global ratings based on the Motivational Interviewing Treatment Integrity Coding Manual 4.2.1, and no notable performance differences were detected among the major large language models. Although the evaluation AIs did not differ significantly from human raters on Cultivating Change Talk, they tended to overrate—particularly for Softening Sustain Talk and Comprehensive Evaluation—and exhibited model-specific grading biases. The client AI displayed limited emotional expression, indicating a need to enhance conversational naturalness. Finally, the study presents recommendations for boosting each AI’s performance through prompt engineering, retrieval-augmented generation, and fine-tuning. 本研究は、日本語カウンセリング対話を対象に、カウンセラーAI（GPT-4-turboゼロショット/Structured Multi Dialogue Prompt (SMDP)、Claude-3-Opus SMDP）、クライアントAI、カウンセリング評価AI（o3, Claude-3.7-Sonnet, Gemini-2.5-pro）の三者を同時検証した。SMDP導入で、Motivational Interviewing Treatment Integrity Coding Manual 4.2.1に基づく人間の専門家によるグローバル評価が有意に向上し、主要Large Language Model間の性能差は認められなかった。評価AIは、Cultivating Change Talkでは人間の評価と有意な差はなかったが、特にSoftening Sustain TalkとComprehensive Evaluationについて過大評価する特徴や、モデル固有の採点の癖も判明した。クライアントAIは感情表出が乏しく自然さの改善が必要であることが示された。各AIについて、プロンプト設計とRetrieval Augmented Generationやファインチューニングによる性能向上のための提案が示された。

**ИИ:** + · обе модели · LLM-судья · LLM evaluation AIs gave MITI 4.2.1 global ratings of counseling dialogues, which were compared with ratings from human experts.

**Решение:** =

---

### 1142 · R8814

**Establishing feature profiles of threatening and challenging situations generated with AI**

2025 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/g4m7u_v1

A variety of difficult situations can elicit stress responses, yet little research has systematically characterized the features that make situations threatening and challenging. In a pre-registered study, we developed a normed set of situations and established features associated with threat and challenge. Using an open-source large language model (LLM), we first generated 20 situations that represent common stressors for UK adults (e.g., “Give a public speech in front of a large audience”). We then asked 81 UK adults to evaluate each situation on dimensions of threat, challenge and eight theory-derived features (e.g., intrinsic difficulty), aggregating their judgments into a 10-dimensional feature profile for each situation. We also tested whether an open-source LLM could reproduce human feature profiles and feature relationships. In the human data, we observed highly reliable feature profiles for the situations that exhibited low threat and moderate challenge overall, while varying reasonably. The eight features were surprisingly similar in how they correlated with threat and challenge (as opposed to exhibiting inverse patterns), explaining high variance in each. Unsupervised clustering identified four coherent groups of situations that illustrate different ways threat and challenge can manifest in daily life. Although LLM judgments approximated human judgments at the aggregate level, their accuracy varied substantially across situations and measures such that LLM judgments failed to capture structural relationships observed in the human data. These findings advance our understanding of situational features underlying threat and challenge, while illustrating the potential and current limitations of LLMs as tools for psychological research.

**ИИ:** ? · обе модели · неясен конструкт · An LLM and 81 adults rated the same situation texts on threat, challenge and eight features. These look like lay appraisal judgments, not coding of psychological text.

**Решение:** =

---

### 1143 · R8815

**Modeling memories, predicting prospections: Automated scoring of autobiographical detail narration using large language models.**

2025 · Behavior research methods · journal article, journalarticle, preprint · eng · https://doi.org/10.3758/s13428-025-02767-3

The autobiographical interview is a widely used tool for examining memory and related cognitive functions. It provides a standardized framework to differentiate between internal details, representing the episodic features of specific events, and external details, including semantic knowledge and other non-episodic information. This study introduces an automated scoring model for autobiographical memory and future thinking tasks, using large language models (LLMs) that can analyze personal event narratives without preprocessing. Building on the traditional autobiographical interview protocol, we fine-tuned a LLaMA-3 model to identify internal and external details at a narrative level. The model was trained and tested on narratives from 284 participants across three studies, spanning past and future thinking tasks, multiple age groups, and collected in lab and virtual interviews. Results demonstrate strong correlations with human scores of up to r = 0.87 on internal and up to r = 0.84 on external details, indicating the model aligns as closely with human raters as they do with each other. Additionally, as evidence of the algorithm's construct validity, the model replicated known age-related trends wherein cognitively normal older adults generate fewer internal and more external details than younger adults across three datasets, finding this age group difference even in one dataset where human raters did not. This automated approach offers a scalable alternative to manual scoring, making large-scale studies of human autobiographical memory more feasible. To facilitate access for researchers, we created a Jupyter Notebook with the automated model and instructions for applying it to new narratives.

**ИИ:** + · обе модели · подсчёт методики · Fine-tuned LLaMA-3 scores autobiographical interview internal/external details; correlations with human scorers reported.

**Решение:** =

---

### 1144 · R8821

**Repurposing Annotation Guidelines to Instruct LLM Annotators: A Case Study**

2025 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-031-97144-0_13

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. LLM annotation guided by human guidelines; the domain may be biomedical NER, but whether the construct is psychological can't be confirmed.

**Решение:** =

---

### 1145 · R8824

**Identifying the Presence and Timing of Self-harm in Electronic Mental Health Records Using Privacy-Preserving Local Language Models: Methodological Study**

2025 · medRxiv · preprint, ppr · https://doi.org/10.1101/2025.10.27.25338892

Abstract Background Self-harm is the strongest risk factor for suicide and an important outcome for mental health care. Although prevalent in clinical populations, it is often imprecisely captured in routinely collected clinical data, where it is often recorded and stored as unstructured free text. Contemporary language models, such as GPT (OpenAI) and Gemini (Google), can analyse free-text clinical notes, but such cloud-based commercial and closed-source models may violate data governance of processing sensitive patient data. Objectives We evaluated whether a privacy-preserving language model running entirely within an institution’s secure computing infrastructure (here, the UK National Health Service; NHS) could accurately identify the presence and timing of self-harm using electronic health records (EHRs) from secondary mental healthcare. Methods Clinical notes were drawn from Oxford Health NHS Foundation Trust using a multi-stage workflow: (1) a random sample of 1,000 patients with a psychiatric diagnosis (ICD-10 F00–F99); (2) candidate-note identification using a Gemma3-4b language model to flag notes containing self-harm content; (3) from those candidates, 1,352 randomly sampled notes were selected for expert annotation. The resulting gold-standard corpus is therefore enriched for self-harm content. Each clinical note was annotated for the presence/absence of self-harm and its timing (≤90 days/>90 days/unknown). A privacy-preserving locally served 27-billion-parameter Gemma3 language model (’Gemma3-27b’) was used as the core model. Prompts were systematically developed and refined using a labelled development set to identify self-harm and generate a structured output per clinical record. The performance of Gemma3-27b model was compared against a strong baseline multi-label text classification model based on RoBERTa (Robustly Optimized BERT Pretraining Approach, a transformer-based language model) architecture. Model performance was evaluated using precision, recall, and the F1-score (harmonic mean of precision and recall), with 95% confidence intervals estimated from 1,000 bootstrap samples with replacement. Results Gemma3-27b outperformed the RoBERTa classifier across all categories, achieving Precision=0.92, Recall=0.92, and F1-score=0.92 for notes containing self-harm, and Precision=0.97, Recall=0.97, and F1-score=0.97 for notes without self-harm. For the 51 notes labelled as recent self-harm in the held-out test set, Gemma3-27b achieved Precision=0.84, Recall=0.75, and F1-score=0.79. The global weighted F1-score of Gemma3-27b across all categories was 0.88, compared to 0.85 for RoBERTa. Conclusions With systematic prompt development on a labelled development set, but no gradient-based fine-tuning, the current Gemma3-27b language model matched or exceeded a fine-tuned RoBERTa classifier for ascertaining self-harm events and their timing. Aggregate gains were modest, while improvements were largest in the most challenging, lower-frequency timing categories. On a simplified binary recent-versus-other task, RoBERTa performed marginally better, indicating that supervised classifiers remain highly effective when the task is simplified and sufficient labelled data exist. This work demonstrates the technical feasibility of privacy-preserving self-harm detection within a secure NHS research environment.

**ИИ:** + · обе модели · клиническая оценка · Gemma3-27b LLM identified self-harm presence and timing in mental health clinical notes, compared against expert-annotated gold standard.

**Решение:** =

---

### 1146 · R8825

**Analyzing patient perspectives with large language models: a cross-sectional study of sentiment and thematic classification on exception from informed consent.**

2025 · Scientific reports · journal article, research support, n.i.h., extramural, research support, non-u.s. gov't · eng · https://doi.org/10.1038/s41598-025-89996-w

Large language models (LLMs) can improve text analysis efficiency in healthcare. This study explores the application of LLMs to analyze patient perspectives within the exception from informed consent (EFIC) process, which waives consent in emergency research. Our objective is to assess whether LLMs can analyze patient perspectives in EFIC interviews with performance comparable to human reviewers.&nbsp;We analyzed 102 EFIC community interviews from 9 sites, each with 46 questions, as part of the Pediatric Dose Optimization for Seizures in Emergency Medical Services study. We evaluated 5 LLMs, including GPT-4, to assess sentiment polarity on a 5-point scale and classify responses into predefined thematic classes. Three human reviewers conducted parallel analyses, with agreement measured by Cohen's Kappa and classification accuracy.&nbsp;Polarity scores between LLM and human reviewers showed substantial agreement (Cohen's kappa: 0.69, 95% CI 0.61-0.76), with major discrepancies in only 4.7% of responses. LLM achieved high thematic classification accuracy (0.868, 95% CI 0.853-0.881), comparable to inter-rater agreement among human reviewers (0.867, 95% CI 0.836-0.901). LLMs enabled large-scale visual analysis, comparing response statistics across sites, questions, and classes. LLMs efficiently analyzed patient perspectives in EFIC interviews, showing substantial sentiment assessment and thematic classification performance. However, occasional underperformance suggests LLMs should complement, not replace, human judgment. Future work should evaluate LLM integration in EFIC to enhance efficiency, reduce subjectivity, and support accurate patient perspective analysis

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 sentiment and thematic coding of community interviews compared with human reviewers (kappa); unclear whether attitudes toward emergency-research consent count as psychological.

**Решение:** =

---

### 1147 · R8839

**ChatGPT as a Competent Enough Judge in Evaluating Relevance of Responses from Divergent Thinking Task**

2025 · OSF · text/project · https://doi.org/10.17605/osf.io/jazem

The validation of responses in divergent thinking tasks is a critical yet understandardized step that should precede creativity scoring. However, inconsistencies related to human judges in this step may compromise the reliability of the results. This study introduces a systematic approach using ChatGPT to validate responses in the Alternate Uses Task (AUT) and compares its performance against six human judges. Analyzing 1245 AUT responses for common objects, we evaluated validity based on precisely defined criteria. Human judges exhibited significant variability, achieving unanimous agreement for only 58% of responses, while ChatGPT demonstrated significant alignment with human assessments, reflecting a capacity to replicate aggregated human judgment. These findings underscore the potential of Large Language Models to enhance objectivity and reproducibility in creativity research by automating response validation. We advocate for integrating AI-driven validation protocols into divergent thinking response evaluation and emphasize transparent reporting of criteria to advance methodological rigor in the field. Full text: https://escholarship.org/uc/item/0fs5t29x This work was supported by the National Science Center, Poland [Grant Number: 2021/41/N/HS6/01620]

**ИИ:** + · обе модели · подсчёт методики · ChatGPT judged the validity of AUT divergent thinking responses against the same criteria as six human judges; agreement was reported.

**Решение:** =

---

### 1148 · R8847

**Mitigating Semantic Drift: Evaluating LLMs' Efficacy in Psychotherapy through MI Dialogue Summarization**

2025 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2511.22818

Recent advancements in large language models (LLMs) have shown their potential across both general and domain-specific tasks. However, there is a growing concern regarding their lack of sensitivity, factual incorrectness in responses, inconsistent expressions of empathy, bias, hallucinations, and overall inability to capture the depth and complexity of human understanding, especially in low-resource and sensitive domains such as psychology. To address these challenges, our study employs a mixed-methods approach to evaluate the efficacy of LLMs in psychotherapy. We use LLMs to generate precise summaries of motivational interviewing (MI) dialogues and design a two-stage annotation scheme based on key components of the Motivational Interviewing Treatment Integrity (MITI) framework, namely evocation, collaboration, autonomy, direction, empathy, and a non-judgmental attitude. Using expert-annotated MI dialogues as ground truth, we formulate multi-class classification tasks to assess model performance under progressive prompting techniques, incorporating one-shot and few-shot prompting. Our results offer insights into LLMs' capacity for understanding complex psychological constructs and highlight best practices to mitigate ``semantic drift" in therapeutic settings. Our work contributes not only to the MI community by providing a high-quality annotated dataset to address data scarcity in low-resource domains but also critical insights for using LLMs for precise contextual interpretation in complex behavioral therapy.

**ИИ:** + · обе модели · кодирование сессий · LLMs classify MI dialogues on MITI components (empathy, evocation, etc.) against expert-annotated ground truth.

**Решение:** =

---

### 1149 · R8871

**A baseline for self-state identification and classification in mental health data: CLPsych 2025 Task**

2025 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, journalarticle, preprint/article · en · https://doi.org/10.18653/v1/2025.clpsych-1.17

We present a baseline for the CLPsych 2025 A.1 task: classifying self-states in mental health data taken from Reddit. We use few-shot learning with a 4-bit quantized Gemma 2 9B model (Gemma Team, 2024; Brown et al., 2020; Daniel Han and team, 2023) and a data preprocessing step which first identifies relevant sentences indicating self-state evidence, and then performs a binary classification to determine whether the sentence is evidence of an adaptive or maladaptive self-state. This system outperforms our other method which relies on an LLM to highlight spans of variable length independently. We attribute the performance of our model to the benefits of this sentence chunking step for two reasons: partitioning posts into sentences 1) broadly matches the granularity at which self-states were human-annotated and 2) simplifies the task for our language model to a binary classification problem. Our system placed third out of fourteen systems submitted for Task A.1, earning a test-time recall of 0.579.

**ИИ:** + · обе модели · бенчмарк с метками людей · Gemma 2 LLM classifies adaptive/maladaptive self-states in Reddit posts, evaluated against human annotations (recall reported).

**Решение:** =

---

### 1150 · R8878

**Employing large language models for emotion detection in psychotherapy transcripts.**

2025 · Frontiers in psychiatry · journal article, journalarticle, journalarticle/einzelbeitrag in einer wissenschaftlichen zeitschrift [article] · eng · https://doi.org/10.3389/fpsyt.2025.1504306

Purpose In the context of psychotherapy, emotions play an important role both through their association with symptom severity, as well as their effects on the therapeutic relationship. In this analysis, we aim to train a large language model (LLM) for the detection of emotions in German speech. We want to apply this model on a corpus of psychotherapy transcripts to predict symptom severity and alliance aiming to identify the most important emotions for the prediction of symptom severity and therapeutic alliance. Methods We employed a public labeled dataset of 28 emotions and translated the dataset into German. A pre-trained LLM was then fine-tuned on this dataset for emotion classification. We applied the fine-tuned model to a dataset containing 553 psychotherapy sessions of 124 patients. Using machine learning (ML) and explainable artificial intelligence (AI), we predicted symptom severity and alliance by the detected emotions. Results Our fine-tuned model achieved modest classification performance ( F1 macro =0.45, Accuracy =0.41, Kappa =0.42) across the 28 emotions. Incorporating all emotions, our ML model showed satisfying performance for the prediction of symptom severity ( r = .50; 95%-CI:.42,.57) and moderate performance for the prediction of alliance scores ( r = .20; 95%-CI:.06,.32). The most important emotions for the prediction of symptom severity were approval, anger , and fear . The most important emotions for the prediction of alliance were curiosity, confusion , and surprise . Conclusions Even though the classification results were only moderate, our model achieved a good performance especially for prediction of symptom severity. The results confirm the role of negative emotions in the prediction of symptom severity, while they also highlight the role of positive emotions in fostering a good alliance. Future directions entail the improvement of the labeled dataset, especially with regards to domain-specificity and incorporating context information. Additionally, other modalities and Natural Language Processsing (NLP)-based alliance assessment could be integrated.

**ИИ:** ? · обе модели · другое · Fine-tuned 'LLM' scored against human emotion labels (kappa 0.42), but the model may be encoder-only (German BERT); check architecture in the full text.

**Решение:** =

---

### 1151 · R8880

**Can Researchers Agree on Levels of Resilience?**

2025 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-7078197/v1

Abstract Resilience has been challenging to define, though it is intuitively apparent in many ways as the capacity to bounce back from adversity. We set out to determine if we could agree on ratings resilience based on our collected life story interviews. After reviewing our life stories, we settled on five ratings of resilience based upon a water/swimming metaphor. At level 1, the person sinks to the bottom and remains there. At level 2, the person is not sitting at the bottom but has yet to reach the surface. At level 3, the person is treading water. They are working hard to stay aﬂoat but not making signiﬁcant progress in altering their overall situation. At level 4, they’re swimming toward shore, toward a more favorable environment where they can thrive. At level 5, they've managed to climb out of the water and change their circumstances. Their resilience allows them to overcome challenges and seek better surroundings. We reviewed the life story interviews of thirty-five participants with an eye to these categories. We also used ChatGPT to determine if it could perform better than us. For 35 participants with five ratings and three raters, we had a percent overall agreement of 84.00% with a free-marginal kappa of 0.80 (95% CI for free-marginal kappa; 0.66 to 0.94). The fixed-marginal kappa was 0.78, with a 95% CI of 0.62 to 0.93. ChatGPT had a percent overall agreement of 71.33% with a free-marginal kappa of 0.65 (95% CI for free-marginal kappa was 0.50 to 0.79: fixed-marginal kappa of 0.61 (95% CI for fixed-marginal kappa of 0.51 to 0.71. Cohen suggested the Kappa result be interpreted as follows: values ≤ 0 as indicating no agreement and 0.01–0.20 as none to slight, 0.21–0.40 as fair, 0.41– 0.60 as moderate, 0.61–0.80 as substantial, and 0.81–1.00 as almost perfect agreement (Cohen, 1960). All results were statistically significant at p

**ИИ:** + · обе модели · кодирование по кодбуку · ChatGPT rated resilience levels in life story interviews; kappa agreement compared with human raters reported.

**Решение:** =

---

### 1152 · R8883

**Sarc7: Evaluating Sarcasm Detection and Generation with Seven Types and Emotion-Informed Techniques**

2025 · conference-paper · https://doi.org/10.18653/v1/2025.winlp-main.25

Sarcasm is a complex linguistic and pragmatic phenomenon where expressions convey meanings that contrast with their literal interpretations, requiring sensitivity to the speaker's intent and context.Misinterpreting sarcasm in collaborative human-AI settings can lead to under-or overreliance on LLM outputs, with consequences ranging from breakdowns in communication to critical safety failures.We introduce Sarc7, a benchmark for fine-grained sarcasm evaluation based on the MUStARD dataset, annotated with seven pragmatically defined sarcasm types: self-deprecating, brooding, deadpan, polite, obnoxious, raging, and manic.These categories are adapted from prior linguistic work and used to create a structured dataset suitable for LLM evaluation.For classification, we evaluate multiple prompting strategies-zero-shot, few-shot, chain-ofthought (CoT), and a novel emotion-based technique-across five major LLMs.Emotionbased prompting yields the highest macroaveraged F1 score of 0.3664 (Gemini 2.5), outperforming CoT for several models and demonstrating its effectiveness in sarcasm type recognition.For sarcasm generation, we design structured prompts using fixed values across four sarcasm-relevant dimensions: incongruity, shock value, context dependency, and emotion.Using Claude 3.5 Sonnet, this approach produces more subtype-aligned outputs, with human evaluators preferring emotion-based generations 38.46% more often than zero-shot baselines.Sarc7 offers a foundation for evaluating nuanced sarcasm understanding and controllable generation in LLMs, pushing beyond binary classification toward interpretable, emotion-informed language modeling.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs classify sarcasm types against human-annotated TV dialogue; unclear whether sarcasm counts as a psychological construct rather than a linguistic one.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Sarcasm type benchmark on TV dialogue (MUStARD) is a linguistic/pragmatic task, not a psychological or clinical construct in clinical or psychological text.)

**Решение:** -

---

### 1153 · R8885

**Prompting LLMs to Notice Student Thinking in Small Group Discussions**

2025 · Stanford Digital Repository · text/capstone · https://doi.org/10.25740/vb895fh1973

Building on student thinking is central to effective instruction in K–12 mathematics education, yet the foundational practice of noticing student thinking remains a persistent challenge. As a high-leverage practice that teachers can learn and are expected to enact across diverse classrooms and contents, noticing student thinking requires sustained opportunities for professional development and ongoing support for consistent implementation. However, the need for expert human judgment makes the work difficult to scale. This study explores whether large language models (LLMs) can support this practice by comparing GPT-4o’s annotations of student thinking in small-group math discussions to those of expert educators. We operationalize noticing student thinking as identifying pre-specified mathematical moves in transcripts and assess alignment using Krippendorff’s unitized alpha, a span-level agreement metric. Human–model agreement approaches human–human agreement, and in some cases, the model identifies meaningful discourse moments that individual raters miss. While discrepancies remain, qualitative analysis suggests LLMs could offer useful reference points for teachers. Rather than acting as expert noticers, LLMs may scaffold teacher reflection and support scalable, content-specific professional learning.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-4o vs expert span-level coding of student mathematical thinking moves in transcripts; unclear whether math discourse counts as a psychological construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: GPT-4o is compared with experts, but the coded construct is mathematical discourse moves in classroom talk. That is an educational construct, not a psychological or clinical one.)

**Решение:** -

---

### 1154 · R8898

**AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation**

2025 · Survey research methods · journalarticle/none, journalarticle, review · en · https://doi.org/10.18148/srm/2025.v19i4.8568

The recent development and wider accessibility of large language models (LLMs) have spurred discussions about how these language models can be used in survey research, including classifying open-ended survey responses. Due to their linguistic capacities, it is possible that LLMs are an efficient alternative to time-consuming manual coding and the pre-training of supervised machine learning models. As most existing research on this topic has focused on English-language responses relating to non-complex topics or on single LLMs, it is unclear whether their findings generalize and how the quality of these classifications compares to established methods. In this study, we investigate to what extent different LLMs can be used to code open-ended survey responses in other contexts, using German data on reasons for survey participation as an example. We compare several state-of-the-art LLMs of the GPT, Llama, and Mistral families, and several prompting approaches, including zero- and few-shot prompting and fine-tuning, and evaluate the LLMs’ performance by using human expert codings. Overall performance differs greatly between LLMs, and only a fine-tuned LLM achieves satisfactory levels of predictive performance. Performance differences between prompting approaches are conditional on the LLM used. Finally, LLMs’ unequal classification performance across different categories of reasons for survey participation results in different categorical distributions when not using fine-tuning. We discuss the implications of these findings, both for methodological research on coding open-ended responses and for their substantive analysis, and for practitioners processing or substantively analyzing such data. Finally, we highlight the many trade-offs researchers need to consider when choosing automated methods for open-ended response classification in the age of LLMs. In doing so, our study contributes to the growing body of research about the conditions under which LLMs can be efficiently, accurately, and reliably leveraged in survey research and their impact on data quality.

**ИИ:** разошлись — Opus + (кодирование по кодбуку: GPT, Llama and Mistral models coded German open-ended answers on survey participation motivation; results were checked against human expert codings.); Sonnet ? (неясен конструкт: LLMs code German open-ended responses on survey participation motivation against human expert codes; the construct is survey-methodological and only borderline psychological.)

**Решение:** +

---

### 1155 · R8907

**Language Models for standardising clinical notes and information extraction in addiction psychiatry – an empirical study**

2025 · preprint · en · https://doi.org/10.31219/osf.io/d5m6e_v1

Introduction: Electronic Health Records (EHR) contain both structured and unstructured data, with unstructured clinical notes (CNs) widely used in addiction psychiatry. CNs have numerous errors and require proofreading before downstream applications. This study evaluates NLP methods and adapts a Language Model (LM) for proofreading CNs and extracting substance-related information.Methods: We analysed CNs from a five-year addiction medicine EHR dataset (2018-2023), selecting 6,500 notes. The proofreading task involved correcting spelling, expanding abbreviations, while information extraction (IE) identified substance use presence and quantified the time since last use. Annotations by a team of doctors and nurses provided the gold standard. Against this, we compared performance of existing solutions including LMs and adapted an LM for these tasks. The final model is also compared against state-of-the-art commercial model (Gpt-4-o) and an acceptability-distinguishability experiment is done with masked raters.Results: Proofreading improved readability and decreased out-of-vocabulary words. LM-based solutions outperformed simpler approaches. The final model performed better than Gpt-4-o on both tasks. Human evaluators found model-corrected CNs indistinguishable from human-proofread versions, correctly guessing the identity in only 27.9% instances and preferring model outputs in 55.7%. On the IE task, while the overall performance is satisfactory (Mean F1 0.99), it is poor on rarer substance classes like hallucinogens.Discussion and Conclusions: Fine-tuned LMs effectively standardized CNs and extracted structured information from addiction psychiatry records. It is possible to adapt open-source LMs for bespoke tasks in addiction psychiatry with limited computational resources. This standardisation can enable large-scale dataset collations for deep learning based predictive modelling.

**ИИ:** разошлись — Opus + (клиническая оценка: GPT-4o and a fine-tuned LM extract substance use from addiction psychiatry notes; compared against doctor/nurse gold-standard annotations.); Sonnet ? (неясен конструкт: Addiction psychiatry notes; LM and GPT-4o extract substance use presence and recency against human annotations, but the construct is factual information extraction and the LM type is unclear.)

**Решение:** +

---

### 1156 · R8922

**The Assessment of Body Image Based on Large Language Model.**

2025 · PsyCh journal · journal article, journalarticle, review · eng · https://doi.org/10.1002/pchj.70048

ABSTRACT Assessing adolescent body image is crucial for mental health interventions, yet traditional methods suffer from limited dimensional coverage, poor dynamic tracking, and weak ecological validity. To address these gaps, this study proposes a multidimensional evaluation using large language models (LLMs) and compares its criterion validity against a dictionary‐based method and expert ratings. We defined four dimensions—perception, positive attitude, negative attitude, behavior—by reviewing the body‐image literature and built a validated dictionary through expert ratings and iterative refinement. A four‐step prompt‐engineering process, incorporating role‐playing and other optimization techniques, produced tailored prompts for LLM‐based recognition. To validate these tools, we collected self‐reported texts and scale scores from 194 university students, performed semantic analyses with Llama‐3.1‐70B, Qwen‐Max, and DeepSeek‐R1 using these prompts, and confirmed ecological validity on social media posts. Results indicate that our multidimensional dictionary correlated significantly with expert ratings across all four dimensions ( r = 0.515–0.625), providing a solid benchmark. LLM‐based assessments then outperformed both the dictionary and human ratings, with zero‐shot LLMs achieving r = 0.664 in positive attitude (vs. expert r = 0.657) and DeepSeek‐R1 reaching r = 0.722 in perception. Role‐playing techniques significantly improved the validity in the perception dimension (Δ r = +0.117). Consistency checks revealed that the DeepSeek model reduced error dispersion in extreme score ranges by 48.4% compared to human ratings, with the 95% consistency limits covering the fluctuations of human scores. Incremental validity analysis showed that LLMs could replace human evaluations in the perception dimension (Δ R 2 = 0.220). In ecological validity checks, the Qwen model achieved a correlation of 0.651 in the social media behavior dimension—53.1% higher than the dictionary method. We found that LLMs demonstrated significant advantages in the multidimensional assessment of body image, offering a new intelligent approach to mental health measurement.

**ИИ:** + · обе модели · клиническая оценка · LLMs and experts both rated body-image dimensions in self-report texts; the main focus is criterion validity, but LLM–human consistency checks are reported.

**Решение:** =

---

### 1157 · R8941

**CultureManip: A Benchmark for Mental Manipulation Detection Across Multilingual Settings**

2025 · Preprints.org · preprint, ppr · https://doi.org/10.20944/preprints202511.0936.v1

Large language models (LLMs) show significant performance gaps in detecting mental manipulation across languages, with particularly pronounced limitations in low-resource settings. Despite extensive research on multilingual LLMs, mental manipulation detection in non-English languages remains understudied. We introduce CultureManip, a multilingual benchmark for binary mental manipulation detection, evaluating ChatGPT-3.5 Turbo across four languages: English, Spanish, Chinese, and Tagalog. Using inter-annotator agreement scores (which measure how often the model's predictions align with human judgments), we reveal substantial performance degradation in non-English contexts. Human-LLM agreement drops from 48% in English to 41% in Spanish, 28% in Chinese, and just 20% in Tagalog, meaning the model disagrees with human annotators 80% of the time for the lowest-resource language. These results demonstrate a clear correlation between language resource availability and detection accuracy, highlighting critical challenges at the intersection of cultural context, linguistic structure, and manipulation identification. This work underscores the urgent need for culturally-aware, multilingual approaches to mental manipulation detection in AI systems.

**ИИ:** + · обе модели · бенчмарк с метками людей · Benchmark comparing GPT-3.5 mental manipulation detection (an interpersonal psychological construct) with human annotators across four languages, reporting agreement.

**Решение:** =

---

### 1158 · R8944

**Computational emotion analysis with multimodal LLMs: Current evidence on an emerging methodological opportunity**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2512.10882

Research increasingly leverages audio-visual materials to analyze emotions in political communication. Multimodal large language models (mLLMs) promise to enable such analyses through in-context learning. However, we lack systematic evidence on whether current mLLMs can reliably measure emotions in real-world political settings. This paper closes this gap by evaluating open- and closed-weights mLLMs available as of early 2026 in video-based emotional arousal measurement using two complementary human-labeled datasets: speech actor recordings created under laboratory conditions and real-world parliamentary debates. I find a critical lab-vs-field performance gap. In videos created under laboratory conditions, the examined mLLMs arousal scores approach human-level reliability. However, in parliamentary debate recordings, all examined models' arousal scores correlate at best moderately with average human ratings. Moreover, in each dataset, all but one of the examined mLLMs exhibit systematic gender-differential bias, consistently underestimating arousal more for male than for female speakers, resulting in a net-positive intensity bias. These findings reveal important limitations of current mLLMs for real-world political video analysis and establish a rigorous evaluation framework for tracking future developments.

**ИИ:** ? · обе модели · другое · Multimodal LLMs rate emotional arousal against human ratings, but the input is video/audio rather than text, so eligibility depends on modality.

**Решение:** =

---

### 1159 · R8949

**Evaluating motivational interview quality using large language models and hidden Markov models.**

2025 · BMC psychiatry · collection/collection, journal article, journalarticle · eng · https://doi.org/10.1186/s12888-025-07391-1

Abstract Background Motivational Interviewing (MI) is a counseling approach that promotes behavior change by eliciting “change talk” and minimizing “sustain talk.” Traditional methods for assessing MI quality, such as manual coding, are labor-intensive, subjective, and difficult to scale. This study introduces an automated framework integrating large language models (LLMs) and Hidden Markov Models (HMMs) for evaluation of MI session quality. Aims This study evaluates the effectiveness of an LLM-HMM framework in predicting MI session quality and examines motivational state transitions in high- and low-quality sessions. Method A dataset of 40 MI sessions was analyzed. Client utterances were classified and numerically scored by an LLM based on their intention toward or away from change. With HMMs, we used these scores to examine the motivational state transitions across each session. Differences between high- and low-quality sessions were quantified by comparing transition matrices using Frobenius norms. Statistical significance was assessed via a permutation test. Predictive performance was evaluated using logistic regression with leave-one-out cross-validation (LOOCV), where transition matrix elements served as independent variables and interview quality as the dependent variable. Results High-quality MI sessions exhibited fluid transitions between motivational states, whereas low-quality sessions showed persistence in resistance-oriented states. A statistically significant difference in transition matrices was observed between session groups (p &lt; 0.001). The framework achieved a mean LOOCV accuracy of 0.80, demonstrating strong predictive performance in identifying MI session quality. Conclusions This study presents a scalable, objective alternative to manual MI evaluation. Future applications may include real-time therapist support, training, and prognosis prediction, pending further validation on field-collected data.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM coded client change/sustain talk in MI sessions; unclear whether utterance codes were compared with human annotations; session-quality prediction is downstream.

**Решение:** =

---

### 1160 · R8962

**Explainable Depression Detection in Clinical Interviews with Personalized Retrieval-Augmented Generation**

2025 · Annual Meeting of the Association for Computational Linguistics · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2025.findings-acl.517

Depression is a widespread mental health disorder, and clinical interviews are the gold standard for assessment. However, their reliance on scarce professionals highlights the need for automated detection. Current systems mainly employ black-box neural networks, which lack interpretability, which is crucial in mental health contexts. Some attempts to improve interpretability use post-hoc LLM generation but suffer from hallucination. To address these limitations, we propose RED, a Retrieval-augmented generation framework for Explainable depression Detection. RED retrieves evidence from clinical interview transcripts, providing explanations for predictions. Traditional query-based retrieval systems use a one-size-fits-all approach, which may not be optimal for depression detection, as user backgrounds and situations vary. We introduce a personalized query generation module that combines standard queries with user-specific background inferred by LLMs, tailoring retrieval to individual contexts. Additionally, to enhance LLM performance in social intelligence, we augment LLMs by retrieving relevant knowledge from a social intelligence datastore using an event-centric retriever. Experimental results on the real-world benchmark demonstrate RED's effectiveness compared to neural networks and LLM-based baselines.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: LLM RAG depression detection from interview transcripts; the benchmark is likely DAIC-WOZ, so labels are probably PHQ self-report, not human coding.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): RAG framework predicting depression from interview transcripts; reference is likely PHQ-based labels, not human coding of text, so no coder-agreement comparison.)

**Решение:** -

---

### 1161 · R8971

**Enhanced large language models for effective screening of depression and anxiety.**

2025 · Communications medicine · journal article, journalarticle, preprint/article · eng · https://doi.org/10.1038/s43856-025-01158-1

Depressive and anxiety disorders are widespread, necessitating timely identification and management. These conditions manifest through various emotional and behavioral symptoms, such as persistent sadness and excessive worry. When left undiagnosed and untreated, these disorders can cause severe consequences, including increased risk of suicide and substantial socioeconomic burden. Recent advances in Large Language Models (LLMs) offer potential solutions, yet high costs and ethical concerns about training data remain challenges. This paper introduces a pipeline for synthesizing clinical interviews, resulting in 1,157 interactive dialogues (PsyInterview), and presents EmoScan, an LLM-based emotional disorder screening system. EmoScan distinguishes between coarse (e.g., anxiety or depressive disorders) and fine disorders (e.g., major depressive disorders) and conducts high-quality interviews. Evaluations show that EmoScan exceeds the performance of base models and other LLMs like GPT-4 in screening emotional disorders (F1-score = 0.7467). It also delivers superior explanations (BERTScore=0.9408) and demonstrates robust generalizability (F1-score of 0.67 on an external dataset). Furthermore, EmoScan outperforms baselines in interviewing skills, as validated by automated ratings and human evaluations. This work highlights the importance of scalable data-generative pipelines for developing effective mental health LLM tools. Liu, Gao et al. develop EmoScan, an LLM-based system to screen for emotional disorders. Findings reveal that EmoScan effectively screens for emotional disorders with high accuracy and can provide detailed explanations, enhancing transparency and trust in automated mental health assessments. Depression and anxiety are common but often hard to detect. This study explores the potential of artificial intelligence (AI) for identification. We used a type of advanced AI that understands and writes human-like text, known as a large language models (LLMs), to automatically create a large collection of realistic conversations between a psychiatrist and a client. We named this collection of simulated interviews “PsyInterview”. Using this data, we trained a new AI system called EmoScan to capture the signs of emotional disorders. EmoScan can screen for depression and anxiety by having a short, text-based conversation with a person. Our evaluation showed that EmoScan is more accurate at identifying these signs and explaining its reasoning compared to other popular AIs. It also conducts high-quality interviews. This work shows how LLMs can help improve mental health care by making screening faster and more accessible, especially where expert resources are limited.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM screens disorders from interview dialogues; the source of the reference labels (diagnosis vs. human coding) is unclear, and automated vs. human ratings of interviewing skill may be comparable.

**Решение:** =

---

### 1162 · R8977

**Enhancing Divergent Thinking through Short-Pulse Inhalation of High-Concentration Oxygen**

2025 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/w3j9s_v1

High-concentration oxygen inhalation is known to facilitate learning and attention. In this study, we tested whether a short-pulse high-concentration oxygen inhalation could enhance creativity. Thirty-four participants were assigned to either an oxygen group (n = 18) or a control group (n = 16) and completed 30 trials of the Alternative Uses Task (AUT) while 128-channel EEG was recorded. The AUT assesses divergent thinking by asking participants to generate alternative uses for everyday items, with the novelty and feasibility of their responses evaluated using an automated GPT-based method. Behavioral results showed that the oxygen group produced solutions with significantly higher novelty without compromising feasibility. Oxygen inhalation also stabilized performance by reducing trial-to-trial variability, with effects lasting at least five minutes after withdrawal. Notably, oxygen prevented the generation of low-novelty solutions while only marginally enhancing highly novel ideas. EEG analysis revealed that oxygen increased brain flexibility, indexed by a resting-state functional connectivity marker termed the Creativity Potential Network (CPN), with the enhancement particularly evident in slow theta-band oscillations. These findings provide behavioral and neural evidence that short-pulse high-concentration oxygen inhalation is a cost-effective method for facilitating creativity.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · GPT scored novelty and feasibility of AUT responses; the full text may report validation against human raters, but the abstract doesn't say.

**Решение:** =

---

### 1163 · R8983

**Evaluating Large Language Models Against Human Annotators in Latent Content Analysis: Sentiment, Political Leaning, Emotional Intensity, and Sarcasm**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2501.02532

In the era of rapid digital communication, vast amounts of textual data are generated daily, demanding efficient methods for latent content analysis to extract meaningful insights. Large Language Models (LLMs) offer potential for automating this process, yet comprehensive assessments comparing their performance to human annotators across multiple dimensions are lacking. This study evaluates the reliability, consistency, and quality of seven state-of-the-art LLMs, including variants of OpenAI\u27s GPT-4, Gemini, Llama, and Mixtral, relative to human annotators in analyzing sentiment, political leaning, emotional intensity, and sarcasm detection. A total of 33 human annotators and eight LLM variants assessed 100 curated textual items, generating 3,300 human and 19,200 LLM annotations, with LLMs evaluated across three time points to examine temporal consistency. Inter-rater reliability was measured using Krippendorff\u27s alpha, and intra-class correlation coefficients assessed consistency over time. The results reveal that both humans and LLMs exhibit high reliability in sentiment analysis and political leaning assessments, with LLMs demonstrating higher internal consistency than humans. In emotional intensity, LLMs displayed higher agreement compared to humans, though humans rated emotional intensity significantly higher. Both groups struggled with sarcasm detection, evidenced by low agreement. LLMs showed excellent temporal consistency across all dimensions, indicating stable performance over time. This research concludes that LLMs, especially GPT-4, can effectively replicate human analysis in sentiment and political leaning, although human expertise remains essential for emotional intensity interpretation. The findings demonstrate the potential of LLMs for consistent and high-quality performance in certain areas of latent content analysis.24 pages, 3 figure

**ИИ:** ? · обе модели · неясен конструкт · LLMs and 33 human annotators rated the same texts; emotional intensity may be a psychological construct, but sentiment, politics and sarcasm are not.

**Решение:** =

---

### 1164 · R8984

**Human vs. Machine: A Comparative Analysis of Qualitative Coding by Humans and ChatGPT-4**

2025 · PsyArXiv · preprint, ppr, posted-content · https://doi.org/10.31234/osf.io/8g36r

Generative artificial intelligence (AI) applications are becoming increasingly influential in psychology training, practice, and research. In this study, the procedures (e.g., coding process) and products (e.g., codes; themes; core story) of qualitative content analysis (QCA) conducted by Chat Generative Pre-trained Transformer (ChatGPT)-4 and novice human researchers were compared, and advantages and disadvantages of each approach were considered. Data included open-ended survey responses from trainers (N = 60) in school psychology programs regarding assessment practices during the COVID-19 pandemic. Findings indicated that ChatGPT-4 could conduct QCA with products that were similar, overall, to human coders, and in significantly less time. However, ChatGPT-4’s process was not transparent, and some codes and themes were unclear. Meanwhile, human coding allowed for the selection and implementation of a purposeful methodological approach, and an auditable and systematic process resulting in a coherent narrative. Considerations for the use of AI in qualitative research are considered and discussed, and future research directions are provided.

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Compares ChatGPT-4 and human codes/themes produced by separate inductive analyses on trainers' assessment-practice responses; no same-unit agreement.); Sonnet ? (неясен конструкт: ChatGPT-4 and humans coded open-ended survey responses, but the topic is assessment practice and the comparison may be at code and theme level only.)

**Решение:** -

---

### 1165 · R8987

**Leveraging Large Language Models for Cost-Effective, Multilingual Depression Detection and Severity Assessment**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2504.04891

Depression is a prevalent mental health disorder that is difficult to detect early due to subjective symptom assessments. Recent advancements in large language models have offered efficient and cost-effective approaches for this objective. In this study, we evaluated the performance of four LLMs in depression detection using clinical interview data. We selected the best performing model and further tested it in the severity evaluation scenario and knowledge enhanced scenario. The robustness was evaluated in complex diagnostic scenarios using a dataset comprising 51074 statements from six different mental disorders. We found that DeepSeek V3 is the most reliable and cost-effective model for depression detection, performing well in both zero-shot and few-shot scenarios, with zero-shot being the most efficient choice. The evaluation of severity showed low agreement with the human evaluator, particularly for mild depression. The model maintains stably high AUCs for detecting depression in complex diagnostic scenarios. These findings highlight DeepSeek V3s strong potential for text-based depression detection in real-world clinical applications. However, they also underscore the need for further refinement in severity assessment and the mitigation of potential biases to enhance clinical reliability.

**ИИ:** разошлись — Opus + (клиническая оценка: LLM rated depression severity from clinical interview text; the abstract reports agreement with a human evaluator.); Sonnet ? (неясно, кто ставил эталонные метки: LLM depression detection on clinical interviews with severity agreement vs a human evaluator; unclear whether detection reference labels are human-coded or diagnosis/questionnaire-based.)

**Решение:** +

---

### 1166 · R8998

**Text Psychometrics: Assessing Psychological Constructs in Text Using Natural Language Processing**

2025 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/9rdux_v1

Natural language processing (NLP) has advanced tremendously thanks to innovations in large language models (LLMs) and generative AI. However, when these technologies are used to assess psychological constructs in text, they are generally not evaluated for the types of validity, reliability, and standardization typically expected from questionnaires that use rating scales and diagnostic instruments. This study seeks to bridge this gap by demonstrating how to evaluate psychometric properties of text-based models, which we call Text Psychometrics. Here we provide an overview of different NLP methods, compare how they can address key constraints in psychological research (e.g., explainability and data privacy), and provide a framework for evaluating these models on a broader range of psychometric properties than is typically evaluated. We then carry out multiple studies to validate NLP models for psychological assessment from text. In study 1, we evaluate concurrent criterion validity by classifying thousands of text-based crisis counseling conversations and Reddit posts into different types of mental health issues. We use a wide array of methods, from traditional lexicons to open-source LLMs. We introduce a novel way to evaluate NLP models for content validity, the degree to which a test captures most expressions of a construct it should capture. Importantly, we find certain high-performing models fail to identify many obvious expressions of a construct; for example, one model that achieved a mean ROC AUC of 0.82 failed to detect 49% of obvious expressions, on average. It is likely other NLP models used in the field for psychological assessment could suffer from the same lack of content validity, but it is rarely evaluated. In study 2, we evaluate prospective criterion validity and estimate how 49 known suicide risk factors are associated with imminent risk in crisis counseling conversations. We find that mentioning lethal means for suicide, the police, depressed mood, and anxiety in text as well as the texter writing more than the counselor characterize the conversations that end up needing an emergency service intervention for imminent suicide risk. This work extends findings from retrospective surveys by analyzing text data in an ecological, high-risk setting as it occurs in real time. In sum, we provide a blueprint for assessing and validating constructs in text through a variety of traditional and state-of-the-art methods that can be chosen depending on the particular constraints researchers may have. While most NLP studies in psychology rely on a single type of metric to validate their models, here we demonstrate why we should validate models more broadly when using NLP and LLMs in psychological research.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Open-source LLMs classify crisis conversations and Reddit posts by mental-health issue; unclear whether labels come from human coders, counselor tags or subreddit.

**Решение:** =

---

### 1167 · R9003

**VERA-MH Concept Paper**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2510.15297

We introduce VERA-MH (Validation of Ethical and Responsible AI in Mental Health), an automated evaluation of the safety of AI chatbots used in mental health contexts, with an initial focus on suicide risk. Practicing clinicians and academic experts developed a rubric informed by best practices for suicide risk management for the evaluation. To fully automate the process, we used two ancillary AI agents. A user-agent model simulates users engaging in a mental health-based conversation with the chatbot under evaluation. The user-agent role-plays specific personas with pre-defined risk levels and other features. Simulated conversations are then passed to a judge-agent who scores them based on the rubric. The final evaluation of the chatbot being tested is obtained by aggregating the scoring of each conversation. VERA-MH is actively under development and undergoing rigorous validation by mental health clinicians to ensure user-agents realistically act as patients and that the judge-agent accurately scores the AI chatbot. To date we have conducted preliminary evaluation of GPT-5, Claude Opus and Claude Sonnet using initial versions of the VERA-MH rubric and used the findings for further design development. Next steps will include more robust clinical validation and iteration, as well as refining actionable scoring. We are seeking feedback from the community on both the technical and clinical aspects of our evaluation.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Concept paper on an LLM judge scoring suicide-risk safety in chatbot conversations; clinician validation is ongoing, and it's unclear whether any agreement is reported.

**Решение:** =

---

### 1168 · R9004

**Creative and depressive profiles shape divergent thinking in emotion regulation idea generation**

2025 · preprint · en · https://doi.org/10.31219/osf.io/9x382_v1

Emotion regulation (ER) is a multi-faceted process, though its generative component––wherein one ideates situation-specific regulatory options (“techniques”)––is poorly understood. Through a novel task (ERGen), we evaluated ER repertoires based on the techniques that individuals generate to regulate their emotional response to negative scenarios. We hypothesized these repertoires to be sensitive to creative (divergent-thinking originality) ability and depression symptoms in our online adult sample (N = 143). Human raters and a generative pre-trained transformer (GPT-4o) coded each generated technique (n = 7854) into one of 14 regulatory strategies to model repertoire richness (strategy diversity) and size (technique count). Individuals higher in creativity showed more prolific technique generation across many strategies, whereas individuals with more depressive symptoms showed altered generation within specific strategies, and reduced deviation from habitual ER tendencies. These findings highlight an untapped research sphere that can motivate new intervention targets in affective disorders, including divergent-thinking ability.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · Human raters and GPT-4o both sorted the generated emotion-regulation techniques into 14 strategies, so agreement can probably be reported.

**Решение:** =

---

### 1169 · R9021

**Human vs. LLM Labeling Consistency: A Comparative Study of Sentiment Annotation in Open-Ended Survey Responses**

2025 · OSF Registries · journalarticle/pre-registration, journalarticle/project, project · https://doi.org/10.17605/osf.io/24swn

This study investigates the extent to which human annotators agree on sentiment classification of open-ended survey responses compared to large language models (LLMs). We will measure inter-annotator agreement among multiple human raters and between human raters and LLMs using Krippendorff’s Alpha as the primary metric and exact match percentage as a secondary descriptive statistic. The research will help assess whether LLMs can achieve levels of subjective judgment comparable to human raters in sentiment annotation tasks.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: OSF pre-registration protocol with no results; generic sentiment labeling of survey responses, with no clear psychological construct.); Sonnet ? (неясен конструкт: LLM–human agreement on sentiment of open-ended survey responses is clearly measured, but it is unclear whether the sentiment is psychological or generic opinion sentiment.)

**Решение:** -

---

### 1170 · R9024

**DialogGuard: Multi-Agent Psychosocial Safety Evaluation of Sensitive LLM Responses**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2512.02282

Large language models (LLMs) now mediate many web-based mental-health, crisis, and other emotionally sensitive services, yet their psychosocial safety in these settings remains poorly understood and weakly evaluated. We present DialogGuard, a multi-agent framework for assessing psychosocial risks in LLM-generated responses along five high-severity dimensions: privacy violations, discriminatory behaviour, mental manipulation, psychological harm, and insulting behaviour. DialogGuard can be applied to diverse generative models through four LLM-as-a-judge pipelines, including single-agent scoring, dual-agent correction, multi-agent debate, and stochastic majority voting, grounded in a shared three-level rubric usable by both human annotators and LLM judges. Using PKU-SafeRLHF with human safety annotations, we show that multi-agent mechanisms detect psychosocial risks more accurately than non-LLM baselines and single-agent judging; dual-agent correction and majority voting provide the best trade-off between accuracy, alignment with human ratings, and robustness, while debate attains higher recall but over-flags borderline cases. We release Dialog-Guard as open-source software with a web interface that provides per-dimension risk scores and explainable natural-language rationales. A formative study with 12 practitioners illustrates how it supports prompt design, auditing, and supervision of web-facing applications for vulnerable users.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM judges rate psychosocial harm against PKU-SafeRLHF human annotations. Unclear whether these are psychological constructs or the same scheme the humans used.); Sonnet + (LLM-судья: LLM-as-judge pipelines rate psychosocial safety (manipulation, psychological harm, insult) of responses, evaluated against human safety annotations in PKU-SafeRLHF.)

**Решение:** +

---

### 1171 · R9031

**Evaluating the Performance of LLMs and Humans in Deductive Coding**

2025 · Digital Commons - USU (Utah State University) · conference-paper

LLMs have increasingly supported qualitative research by automating: code discovery, refinement, and agreement data categorization and pattern recognition. • This study explores the potential of large language models (LLMs) to enhance deductive coding in qualitative research.

**ИИ:** ? · обе модели · неясен конструкт · Compares LLM and human deductive coding of qualitative data, but the abstract doesn't say whether the codes are psychological.

**Решение:** =

---

### 1172 · R9032

**Streamlining Field Note Analysis: Leveraging GPT for Further Insights**

2025 · Digital Commons - USU (Utah State University) · article

As an integral part of qualitative research inquiry, field notes provide important data from researchers embedded in research sites. However, field notes can vary significantly, influenced by the researchers' immersion in the field, prior knowledge, beliefs, interests, and perspectives. As consequence, their interpretation presents significant challenges. This study offers a preliminary investigation into the potential of using large language models to assist researchers with the analysis and interpretation of field notes data. Our methodology consisted of two phases. First, a researcher deductively coded field notes of six classroom implementations of a novel elementary-level mathematics curriculum. In the second phase, we prompted ChatGPT-4 to code the same field notes, using the codebook, definitions, examples, and deductive coding approach employed by the researcher. We also prompted Chatgpt to provide justifications of its coding decisions We then, calculated agreements and disagreements between ChatGPT and the researcher, organized the data in a contingency table, computed Cohen's Kappa, structured the data into a confusion matrix; and using the researcher’s coding as the “gold standard”, we calculated performance measures, specifically: Accuracy, Precision, Recall, and F1 Score. Our findings revealed that while the researcher and ChatGPT appeared to generally agree on the frequency in applying the different codes, overall agreement, as measured by Cohen’s Kappa was low. In contrast, using measures from information science at the code level revealed more nuanced results. Moreover, coupled with ChatGPT justifications of coding decisions, these findings provided insights than can help support the iterative improvement of codebooks.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-4 deductively coded classroom field notes vs researcher (kappa). Unclear whether the codes are psychological constructs or only teaching/curriculum categories.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: ChatGPT-4 vs researcher coding of math classroom field notes with kappa, but the construct is education/curriculum implementation, not psychological or clinical.)

**Решение:** -

---

### 1173 · R9033

**Exploring the potential of large language models to understand interpersonal emotion regulation strategies from narratives.**

2025 · Emotion (Washington, D.C.) · journal article, med, journalarticle · eng · https://doi.org/10.1037/emo0001528

Interpersonal emotion regulation involves using diverse strategies to influence others' emotions, commonly assessed with questionnaires. However, this method may be less effective for individuals with limited literacy or introspection skills. To address this, recent studies have adopted narrative-based approaches, though these require time-intensive qualitative analysis. Given the potential of artificial intelligence (AI) and large language models (LLM) for information classification, we evaluated the feasibility of using AI to categorize interpersonal emotion regulation strategies. We conducted two studies in which we compared AI performance against human coding in identifying regulation strategies from narrative data. In Study 1, with 2,824 responses, ChatGPT initially achieved Kappa values over .47. Refinements in prompts (i.e., coding instructions) led to improved consistency between ChatGPT and human coders (κ > .79). In Study 2, the refined prompts demonstrated comparable accuracy (κ > .76) when analyzing a new set of responses ( N = 2090), using both ChatGPT and Claude. Additional evaluations of LLMs' performance using different accuracy metrics pointed to notable variability in LLM's capability when interpreting narratives across different emotions and regulatory strategies. These results point to the strengths and limitations of LLMs in classifying regulation strategies, and the importance of prompt engineering and validation. (PsycInfo Database Record (c) 2025 APA, all rights reserved).

**ИИ:** + · обе модели · кодирование по кодбуку · ChatGPT and Claude coded interpersonal emotion regulation strategies in narratives; kappa reported against human coders.

**Решение:** =

---

### 1174 · R9055

**A Fully Generative Motivational Interviewing Counsellor Chatbot for Moving Smokers Towards the Decision to Quit**

2025 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2505.17362

The conversational capabilities of Large Language Models (LLMs) suggest that they may be able to perform as automated talk therapists. It is crucial to know if these systems would be effective and adhere to known standards. We present a counsellor chatbot that focuses on motivating tobacco smokers to quit smoking. It uses a state-of-the-art LLM and a widely applied therapeutic approach called Motivational Interviewing (MI), and was evolved in collaboration with clinician-scientists with expertise in MI. We also describe and validate an automated assessment of both the chatbot's adherence to MI and client responses. The chatbot was tested on 106 participants, and their confidence that they could succeed in quitting smoking was measured before the conversation and one week later. Participants' confidence increased by an average of 1.7 on a 0-10 scale. The automated assessment of the chatbot showed adherence to MI standards in 98% of utterances, higher than human counsellors. The chatbot scored well on a participant-reported metric of perceived empathy but lower than typical human counsellors. Furthermore, participants' language indicated a good level of motivation to change, a key goal in MI. These results suggest that the automation of talk therapy with a modern LLM has promise. To be published in the Findings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL), Vienna, Austria, 2025

**ИИ:** + · обе модели · кодирование сессий · Validated automated (likely LLM) coding of MI adherence and client language in counselling transcripts; check human-coder reference in full text.

**Решение:** =

---

### 1175 · R9058

**Towards Smarter Hiring: Are Zero-Shot and Few-Shot Pre-trained LLMs Ready for HR Spoken Interview Transcript Analysis?**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2504.05683

This research paper presents a comprehensive analysis of the performance of prominent pre-trained large language models (LLMs), including GPT-4 Turbo, GPT-3.5 Turbo, text-davinci-003, text-babbage-001, text-curie-001, text-ada-001, llama-2-7b-chat, llama-2-13b-chat, and llama-2-70b-chat, in comparison to expert human evaluators in providing scores, identifying errors, and offering feedback and improvement suggestions to candidates during mock HR (Human Resources) interviews. We introduce a dataset called HURIT (Human Resource Interview Transcripts), which comprises 3,890 HR interview transcripts sourced from real-world HR interview scenarios. Our findings reveal that pre-trained LLMs, particularly GPT-4 Turbo and GPT-3.5 Turbo, exhibit commendable performance and are capable of producing evaluations comparable to those of expert human evaluators. Although these LLMs demonstrate proficiency in providing scores comparable to human experts in terms of human evaluation metrics, they frequently fail to identify errors and offer specific actionable advice for candidate performance improvement in HR interviews. Our research suggests that the current state-of-the-art pre-trained LLMs are not fully conducive for automatic deployment in an HR interview assessment. Instead, our findings advocate for a human-in-the-loop approach, to incorporate manual checks for inconsistencies and provisions for improving feedback quality as a more suitable strategy. 32 pages, 24 figures

**ИИ:** ? · обе модели · неясен конструкт · LLMs score HR interview transcripts against expert human evaluators; unclear whether the scored dimensions are psychological constructs or only interview performance.

**Решение:** =

---

### 1176 · R9068

**AI Delivers Creative Output but Struggles with Thinking Processes**

2025 · Thinking Skills and Creativity · journalarticle, preprint/article, article · en · https://doi.org/10.48550/arxiv.2503.23327

A key objective in artificial intelligence (AI) development is to create systems that match or surpass human creativity. Although current AI models perform well across diverse creative tasks, it remains unclear whether these achievements reflect genuine creative thinking. This study examined whether AI models (GPT-3.5-turbo, GPT-4, and GPT-4o) engage in creative thinking by comparing their performance with humans across various creative tasks and core cognitive processes. Results showed that AI models outperformed humans in divergent thinking, convergent thinking, and insight problem-solving, but underperformed in creative writing. Compared to humans, AI generated lower forward flow values in both free and chain association tasks and showed lower accuracy in the representational change task. In creative evaluation, AI exhibited no significant correlation between the weights of novelty and appropriateness when predicting creative ratings, suggesting the absence of a human-like trade-off strategy. AI also had higher decision error scores in creative selection, suggesting difficulty identifying the most creative ideas. These findings suggest that while AI can mimic human creativity, its strong performance in creative tasks is likely driven by non-creative mechanisms rather than genuine creative thinking.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mostly AI as a creative participant, but in a creative-evaluation task GPT rates ideas; LLM–human rating agreement may be reportable.

**Решение:** =

---

### 1177 · R9072

**AI-Powered Triage of Suicidal Ideation in Adolescents: A Comparative Evaluation of Large Language Models Using Synthetic Clinical Vignettes**

2025 · medRxiv · preprint, ppr, posted-content · en · https://doi.org/10.1101/2025.08.05.25333046

Abstract Objective To evaluate the performance of leading Large Language Models (LLMs) in classifying suicide risk and generating clinically appropriate action plans for adolescent psychiatric cases presented through synthetic clinical vignettes. Methods We developed 40 synthetic clinical vignettes depicting adolescents with varying levels of suicide risk, structured according to established clinical formulation principles. A gold standard for risk level, based on the Columbia-Suicide Severity Rating Scale (C-SSRS) framework, and corresponding clinical actions was established for each vignette by a panel of two board-certified child and adolescent psychiatrists. Three LLMs (GPT-4o, Claude 3.5 Sonnet, Llama-3.1-70B) were prompted using a structured chain-of-thought methodology to classify risk and propose a detailed action plan. Performance was assessed using quantitative classification metrics (accuracy, precision, recall, F1-score) and qualitative thematic analysis of the generated action plans. Results Quantitative analysis of risk classification revealed variable performance. GPT-4o achieved the highest accuracy (82.5%), followed by Claude 3.5 Sonnet (75.0%) and Llama-3.1-70B (67.5%). F1-scores demonstrated challenges in correctly identifying higher-risk categories, particularly for nuanced presentations of intent. Qualitative thematic analysis of the action plans identified consistent adherence to basic safety protocols (e.g., recommending emergency evaluation for high-risk cases). However, significant and critical failures were pervasive, including the omission of crucial inquiries about access to lethal means, failure to incorporate protective factors into planning, and the generation of clinically inappropriate therapeutic reassurance in a triage context. Conclusions While LLMs demonstrate a nascent ability to process clinical information for suicide risk assessment, significant deficits in clinical reasoning and safety planning persist. Their performance on idealized synthetic data suggests these models are not yet suitable for autonomous clinical decision-making. These findings underscore the imperative for rigorous, clinically-grounded evaluation frameworks and the development of human-in-the-loop systems to ensure patient safety in any future deployment. Key Messages What is already known on this topic Suicide is a leading cause of death in adolescents, yet current clinical risk assessment tools and subjective judgments have limited predictive accuracy and are difficult to scale in the face of rising demand and workforce shortages. What this study adds This study provides a direct comparative evaluation of multiple state-of-the-art Large Language Models on a standardized adolescent suicide risk triage task, using a synthetic data methodology that allows for controlled assessment of both classification accuracy and the clinical appropriateness of generated action plans. How this study might affect research, practice or policy The findings highlight the potential of LLMs as adjunctive tools in non-specialist settings but also reveal critical safety and reliability gaps that must be addressed through further research, the development of ethical guidelines, and regulatory oversight before any clinical implementation can be considered.

**ИИ:** + · обе модели · клиническая оценка · GPT-4o, Claude and Llama classified suicide risk in 40 vignettes; scored for accuracy against a C-SSRS gold standard set by two psychiatrists.

**Решение:** =

---

### 1178 · R9079

**Prompt-based learning and its application in mental health**

2025 · ePrints Soton (University of Southampton) · dissertation · en · https://eprints.soton.ac.uk/505273/1/thesis_draft.pdf

With the rise of large language models (LLMs), prompt-based learning has become a widely studied and essential topic in the field of Natural Language Processing (NLP). Due to their impressive performance in zero-shot and few-shot settings, prompting offers a strong opportunity for low-resource domains such as mental health. Mental health is a prevalent global concern, with increasing numbers of users sharing their experiences on social media. However, data from these platforms is often complex, and manual annotation at scale is both time-consuming and costly. This thesis investigates the central hypothesis that task-specific and well-designed prompt strategies are essential for effectively adapting LLMs to low-resource domains, with a particular focus on mental health applications. This study systematically examines the role of prompt position across tasks and prompting methods, revealing that position significantly affects model performance and is often overlooked in prior work. A domain-specific prompting method is then explored to extract and summarise evidence of suicidal ideation with minimal supervision. Finally, a novel LLM-based framework is developed for multi-label life event annotation in the mental health domain, incorporating tailored prompting techniques and prompt position self-ordering to enable effective automatic annotation.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Thesis on LLM annotation of suicidal-ideation evidence and life events in mental-health social-media posts, likely evaluated against human-annotated gold labels.); Sonnet ? (неясно, сравнивали ли с людьми: Thesis on LLM prompting for mental health, including suicidal ideation evidence extraction and life event annotation; human-labelled comparison likely but not stated in the abstract.)

**Решение:** +

---

### 1179 · R9088

**Role-Play Large Language Models for Short Behavior Change Interventions: An Exploratory Study on Brief Action Planning**

2025 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-031-95841-0_9

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; title suggests LLM role-play generating BAP interventions, but fidelity coding against humans cannot be ruled out.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: No abstract; the title suggests LLMs role-play a coach delivering Brief Action Planning, which is generation rather than coding against human labels.)

**Решение:** ?

---

### 1180 · R9097

**Advancing qualitative analysis in professional disaster and risk communication: A comparative study of an OpenAI ChatGPT 3.5 model-enabled method for processing complex public discourse**

2025 · International Journal of Disaster Risk Reduction · article · en · https://doi.org/10.1016/j.ijdrr.2025.105835

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; ChatGPT-3.5 qualitative analysis of disaster public discourse compared with another method, possibly human coding; whether a psychological construct is involved is unclear.

**Решение:** =

---

### 1181 · R9099

**LLMs4AAIs - Using LLMs to Automatically Assess Adult Attachment Interviews**

2025 · OSF Preprints (OSF Preprints) · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/xrvz3

This work explores the feasibility of automating AAI assessment using recent advances in large language models (LLMs) and reasoning capabilities to plausibly evaluate AAI transcripts. We specifically evaluate the potential of open-source models to automatically assess AAIs according to the Main &amp; Goldwyn Scoring and Classification System (1984). To this end, we work with a dataset of 1,565 AAI transcripts from the Attachment Secondary Processing and Analysis Network (ASPAN), which is part of the Collaboration on Attachment Transmission Synthesis (CATS) project, and plan to apply different methodologies including direct prompting, retrieval-augmented generation, embedding-based classification, supervised fine-tuning, Reinforcement Learning as well as synthetic data generation to enhance model training and address class imbalance. We plan to benchmark model performance across binary (secure/insecure), four-way (secure-autonomous, dismissing, preoccupied, and unresolved/disorganized), and ordinal scale predictions, using published inter-rater agreement levels as a reference. By improving the scalability, accessibility, and objectivity of AAI assessments, this research aims to support broader use of attachment theory in psychological and developmental research. It also serves as a proof-of-concept for applying open-source LLMs to complex narrative-based psychological instruments.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: Pre-registration/protocol for LLM scoring of AAI transcripts against human classifications; planned work, no results reported. Track eventual results paper.); Sonnet + (подсчёт методики: LLMs score Adult Attachment Interview transcripts using Main & Goldwyn system, benchmarked against human-coded classifications from 1,565 ASPAN transcripts (preregistration).)

**Решение:** -

---

### 1182 · R9103

**Assisting Screening of Pediatric Depression with Large Language Models as Symptom Extractors: Pilot Study (Preprint)**

2025 · preprint · en · https://doi.org/10.2196/preprints.71614

BACKGROUND Depression is rising among people aged 10–24. Traditional depression screening methods, such as the PHQ-9, are particularly challenging for children. AI has potential to help but the scarcity of annotated datasets highlights the need for zero-shot approaches. In this work, we investigate the feasibility of state-of-the-art Large Language Models (LLMs) for depressive symptom extraction in pediatric settings. This approach aims to complement traditional screening. OBJECTIVE The key objectives were to: 1) Assess the feasibility of zero-shot LLMs in identifying depressive symptoms in free-text clinical notes for pediatric populations, 2) Benchmark the zero-shot performance of leading LLM models in extracting PHQ-9 symptom-related information, 3) Demonstrate the potential clinical value of LLM-driven evidence extraction to improve mental health screening using an example of an interpretable AI-based depression screening tool. METHODS We examined free text of the EHRs of pediatric patients with the diagnosis of depression or related mood disorders (age groups 6-24, 1.8K patients) from the Cincinnati Children's Hospital Medical Center. We noticed drastic inconsistencies in the application and documentation of PHQ-9 screening highlighting the difficulty in obtaining comprehensive diagnostic data in these conditions. We manually annotated notes for 22 patients with 16 depression-related symptom categories. We leveraged the combination of Beck's Depression Inventory (BDI) and the PHQ-9 to develop tailored categories specifically suited for pediatric depression symptoms. We then applied three state-of-the-art Large Language Models (LLMs) (FLAN T5, Llama and Phi) to automate the identification of these symptom categories. RESULTS Our findings show that all LLMs are 60% more efficient than word match with Flan leading in precision (average F1: 0.65, precision: 0.78), excelling in the extraction of more rare symptoms like "sleep problems" (F1 0.92) and "self-loathing" (F1 0.8). Phi strikes a balance between precision (0.44) and recall (0.60). Llama 3 with the highest recall (0.90), overgeneralizes symptoms and is less suitable. Challenges include the complexity of clinical notes and overgeneralization from PHQ-9 scores. We finally demonstrate the utility of symptom annotations provided by Flan as features in an ML algorithm which differentiates depression cases from controls with high precision of 0.78 with major performance boost as compared to a baseline not using these features. CONCLUSIONS This study highlights the strengths of LLMs in addressing data scarcity and heterogeneity by extracting depressive symptoms from free text of pediatric EHRs with high precision. The computational efficiency of FLAN-T5 further supports its potential for deployment in resource-limited clinical settings. Our findings are constrained to the pediatric age group, requiring further validation for broader populations and other mental health conditions. Our study demonstrates the potential of LLMs to enhance depression screening, improve diagnostic consistency, and provide an interpretable tool for mental health clinicians.

**ИИ:** + · обе модели · клиническая оценка · Llama and Phi extracted depressive symptom categories from pediatric clinical notes; results were compared with manual human annotations (F1 reported).

**Решение:** =

---

### 1183 · R9122

**How Do Citizens Think and Feel about Voting?**

2025 · book-chapter · en · https://doi.org/10.1093/9780198946335.003.0006

Abstract This chapter provides a descriptive overview of voting meanings across 13 countries using cross-sectional surveys and two three-wave panel surveys. It focuses on validating the measurement of voting meanings via open-ended survey questions and manual coding. Validity is examined through content accuracy, the measurement tool’s comprehensiveness, and construct soundness, ensuring alignment with theoretical expectations. It compares responses on voting meanings using open-ended versus closed-ended questions, and examines traditional voter behaviours and attitudes such as turnout and trust in institutions. Additionally, the chapter uses large language models (LLMs) to evaluate the robustness of coding, testing the consistency and accuracy of the codebook across nearly a million words from diverse linguistic contexts. By leveraging artificial intelligence (AI), the chapter aims to enhance coding efficiency and maintain high data quality in multilingual and culturally diverse datasets.

**ИИ:** ? · обе модели · неясен конструкт · LLMs test codebook coding of open-ended voting-meaning responses against manual coding; the construct may be political rather than psychological.

**Решение:** =

---

### 1184 · R9137

**Optimizing Generative AI's Accuracy and Transparency in Inductive Thematic Analysis: A Human-AI Comparison**

2025 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5174910

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; compares human and AI inductive thematic analysis. It may compare themes only, and the data's psychological content is unclear.

**Решение:** =

---

### 1185 · R9140

**Large Language Models are Highly Aligned with Human Ratings of Emotional Stimuli**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2508.14214

Emotions exert an immense influence over human behavior and cognition in both commonplace and high-stress tasks. Discussions of whether or how to integrate large language models (LLMs) into everyday life (e.g., acting as proxies for, or interacting with, human agents), should be informed by an understanding of how these tools evaluate emotionally loaded stimuli or situations. A model's alignment with human behavior in these cases can inform the effectiveness of LLMs for certain roles or interactions. To help build this understanding, we elicited ratings from multiple popular LLMs for datasets of words and images that were previously rated for their emotional content by humans. We found that when performing the same rating tasks, GPT-4o responded very similarly to human participants across modalities, stimuli and most rating scales (r = 0.9 or higher in many cases). However, arousal ratings were less well aligned between human and LLM raters, while happiness ratings were most highly aligned. Overall LLMs aligned better within a five-category (happiness, anger, sadness, fear, disgust) emotion framework than within a two-dimensional (arousal and valence) organization. Finally, LLM ratings were substantially more homogenous than human ratings. Together these results begin to describe how LLM agents interpret emotional stimuli and highlight similarities and differences among biological and artificial intelligence in key behavioral domains.

**ИИ:** ? · обе модели · другое · LLMs rated emotion in word and image stimuli against human normative ratings; it's unclear whether isolated word norms count as psychological text.

**Решение:** =

---

### 1186 · R9142

**Song-based methods and critical reflection: experiences of Brazilian older adults in music therapy**

2025 · Geriatrics Gerontology and Aging · journalarticle, article · en · https://doi.org/10.53886/gga.e0000292_en

Objective: To explore the lived experiences of Brazilian older adults participating in group music therapy sessions that incorporated song-based methods, with a focus on how these experiences fostered dialogue and critical reflection. Methods: This phenomenological study involved a music therapist facilitating 12 weekly 1-hour sessions with a group of 12 Brazilian older adults. Audio recordings from all sessions were transcribed and analyzed using a thematic approach grounded in phenomenology. The artificial intelligence tool GPT-4 and member checking were employed to ensure the reliability of results. Results: The analysis revealed that song-based methods encouraged discussion and critical reflection on the aging process, relationships, ageism, gender roles, and cultural change over time. Conclusion: The song-based methods created a reflective space that supported expression and social dialogue among older adults. Future research should explore their long-term effects and adaptability across diverse contexts.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · GPT-4 was used to check the reliability of a thematic analysis of therapy transcripts; unclear whether it coded the same units or only compared themes.

**Решение:** =

---

### 1187 · R9188

**Deconstructing Depression Stigma: Integrating AI-driven Data Collection and Analysis with Causal Knowledge Graphs**

2025 · arXiv (Cornell University) · journalarticle, book, conference · en · https://doi.org/10.48550/arxiv.2502.06075

Mental-illness stigma is a persistent social problem, hampering both treatment-seeking and recovery. Accordingly, there is a pressing need to understand it more clearly, but analyzing the relevant data is highly labor-intensive. Therefore, we designed a chatbot to engage participants in conversations; coded those conversations qualitatively with AI assistance; and, based on those coding results, built causal knowledge graphs to decode stigma. The results we obtained from 1,002 participants demonstrate that conversation with our chatbot can elicit rich information about people's attitudes toward depression, while our AI-assisted coding was strongly consistent with human-expert coding. Our novel approach combining large language models (LLMs) and causal knowledge graphs uncovered patterns in individual responses and illustrated the interrelationships of psychological constructs in the dataset as a whole. The paper also discusses these findings' implications for HCI researchers in developing digital interventions, decomposing human psychological constructs, and fostering inclusive attitudes. Conditionally accepted to CHI Conference on Human Factors in Computing Systems (CHI'25)

**ИИ:** + · обе модели · кодирование по кодбуку · An LLM coded the chatbot conversations about depression stigma, and the abstract reports strong consistency with human-expert coding.

**Решение:** =

---

### 1188 · R9189

**PychoAgent: Psychology-driven LLM Agents for Explainable Panic Prediction on Social Media during Sudden Disaster Events**

2025 · Conference on Empirical Methods in Natural Language Processing · journalarticle, conference · https://doi.org/10.18653/v1/2025.emnlp-main.865

Accurately predicting public panic sentiment on social media is crucial for proactive governance and crisis management. Current efforts on this problem face three main challenges: lack of finely annotated data hinders emotion prediction studies, unmodeled risk perception causes prediction inaccuracies, and insufficient interpretability of panic formation mechanisms limits mechanistic insight. We address these issues by proposing a Psycho logy-driven generative Agent framework (PsychoAgent) for explainable panic prediction based on emotion arousal theory. Specifically, we first construct a fine-grained panic emotion dataset (namely COPE) via human-AI (Large Language Models, LLMs) collaboration, combining scalable LLM-based labeling with human annotators to ensure accuracy for panic emotion and to mitigate biases from linguistic variations. Then, we construct PsychoAgent integrating cross-domain heterogeneous data grounded in psychological mechanisms to model risk perception and cognitive differences in emotion generation. To enhance interpretability, we design an LLM-based role-playing agent that simulates individual psychological chains through dedicatedly designed prompts. Experimental results on our annotated dataset show that Psy-choAgent improves panic emotion prediction performance by 13% 1 to 21% compared to baseline models. Furthermore, the explainabil-ity and generalization of our approach is validated. Crucially, this represents a paradigm shift from opaque "data-driven fitting" to transparent "role-based simulation with mechanistic interpretation" for panic emotion prediction during emergencies. Our implementation is publicly available at: https://github.com/s upersonic0919/PsychoAgent .

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM labels panic emotion in posts with human annotators (COPE); unclear whether LLM–human agreement is reported or whether the task is forecasting rather than coding.

**Решение:** =

---

### 1189 · R9197

**Integrating Motivational Interviewing Principles and Large Language Models in Automated Behaviour Change Support Integration von Prinzipien der Motivierenden Gesprächsführung und großen Sprachmodellen in die automatisierte Unterstützung von Verhaltensänderungen**

2025 · Universität Regensburg · text/thesis · https://doi.org/10.5283/epub.76569

This thesis explores the application of large language models (LLMs) in the context of behaviour change support systems, focusing on the integration of Motivational Interviewing (MI) principles to enhance the effectiveness and safety of these interactions. This work addresses both the technical and theoretical aspects of applying conversational AI to intentional behaviour change scenarios. The primary technical contributions of this research include an annotated dataset of written conversations about behaviour change, transferable and robust classification algorithms for identifying behaviour change language, and strategic methodologies for significantly reducing harms and unsuitable outputs in LLM-based conversations. An annotation scheme was also developed to identify and mitigate unsuitable behaviours in LLM outputs, accompanied by an annotated dataset of real human-LLM interactions, which provides insights into user behaviour and system performance in practical settings. This project provides novel insights into the domain independence of behaviour change language, demonstrating the applicability of the developed systems across various contexts and target behaviours. Furthermore, the project explores user behaviour and expectations during interactions with LLMs, offering a deeper understanding of how users engage with and respond to LLM-based behaviour change support. In general, this thesis contributes to the field of conversational AI by showcasing how LLMs can be used effectively and safely to support behaviour change, emphasising the importance of tailoring interactions based on MI principles and user-specific communication patterns. The findings not only advance our understanding of the technical and interactional dynamics of conversational AI but also set the stage for future research in the deployment of these technologies in diverse real-world applications. All code is made available on GitHub Diese Arbeit untersucht die Anwendung von Large Language Models (LLMs) im Kontext von Systemen zur Unterstützung von Verhaltensänderungen und konzentriert sich dabei auf die Integration von Prinzipien der motivierenden Gesprächsführung (MI), um die Effektivität und Sicherheit dieser Interaktionen zu verbessern. Diese Arbeit befasst sich sowohl mit den technischen als auch mit den theoretischen Aspekten der Conversational AI in Szenarien zur beabsichtigten Verhaltensänderung. Zu den primären technischen Beiträgen dieser Forschung gehören ein annotierter Datensatz schriftlicher Konversationen über Verhaltensänderung, übertragbare und robuste Klassifizierungsalgorithmen zur Identifizierung von Sprache zur Verhaltensänderung und strategische Methoden zur signifikanten Reduzierung von gefährlichen und unangemessenen Textausgaben in LLM-basierten Konversationen. Darüber hinaus wurde ein Annotationsschema entwickelt, um ungeeignete Verhaltensweisen in LLM-Outputs zu identifizieren und abzuschwächen, begleitet von einem annotierten Datensatz echter Mensch-LLM-Interaktionen, der Einblicke in das Nutzerverhalten und die Systemleistung in der Praxis bietet. Dieses Projekt bietet neue Einblicke in die Domänenunabhängigkeit von Sprache über Verhaltensänderung und demonstriert die Anwendbarkeit der entwickelten Systeme in verschiedenen Kontexten unf für verschiedene Verhaltensänderungen. Darüber hinaus erforscht das Projekt das Verhalten und die Erwartungen von NutzerInnen während der Interaktion mit LLMs und bietet so ein tieferes Verständnis dafür, wie diese mit LLM-basierten Verhaltensmodellen umgehen und darauf reagieren. Sämtlicher Code wird auf GitHub veröffentlicht.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Thesis with human-annotated MI behaviour-change language dataset and classifiers; unclear whether LLMs classify and are compared with human annotations.

**Решение:** =

---

### 1190 · R9200

**LADEN: A LLM-AideD ENsemble Model for Suicide Risk Prediction**

2025 · BigData Congress [Services Society] · journalarticle, conference, conference-paper · https://doi.org/10.1109/bigdata66926.2025.11400928

We propose a Large Language Model (LLM)-aided ensemble model (LADEN) to predict the suicide risks associated with a user's subsequent post, based on their historical posts. Each sample in the dataset, provided by the IEEE BigData 2025 Cup Challenge, consists of five user posts and one corresponding label indicating the suicide risk level. The four possible risk levels are: indicator, ideation, behavior, and attempt, represented by labels $0,1,2$, and 3, respectively. The distribution of these labels in the training dataset is imbalanced, which presents a challenge. To mitigate this issue, we develop an ensemble framework in which an LLM is first employed during feature preprocessing to transform user posts into semantic vectors. These semantic representations are then input into the ensemble model for classification. The proposed ensemble architecture consists of two Mixture-of-Experts (MOE) neural networks, namely MOE-1 and MOE-2, designed to alleviate the impact of label imbalance. Specifically, the semantic vector of each sample is initially processed by MOE1 to determine whether it belongs to the ideation class. If not, it is passed to MOE-2, which classifies it into one of the remaining three risk levels. At the end of the challenge, LADEN achieved a weighted F1 score of 0.44539 on the test dataset while using only approximately 0.86 million parameters, demonstrating both efficiency and effectiveness. The implementation is available as open source at: https://github.com/ludlows/LADEN.

**ИИ:** разошлись — Opus ? (другое: LLM used only for embeddings feeding a MoE classifier that predicts suicide risk levels of the next post; labels' human-annotation source unclear.); Sonnet -5 (нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM: LLM is only used for embeddings feeding a MoE neural classifier; no LLM coding compared with human coders.)

**Решение:** -

---

### 1191 · R9207

**Automated Scoring of Narrative Recall Assessments Using Large Language Models Enables Exploration of Alternate Scoring Criteria**

2025 · Alzheimer s & Dementia · abstract, pmc, journalarticle · eng · https://doi.org/10.1002/alz70857_099418

Abstract Background Clinical neuropsychological assessments, particularly narrative recall tests, present significant challenges for real‐time scoring due to the need for rapid interpretation. While post‐hoc scoring from recordings improves accuracy, time constraints in clinical settings often preclude this approach. Large Language Models (LLMs) have demonstrated promise in scoring verbal responses, potentially offering improved reliability and consistency compared to traditional human rating methods. Method 28 participants (14 MCI, 14 age‐matched CN), completed the Craft Story 21 assessment, immediate and delayed. ChatGPT‐4o was provided human‐corrected transcripts along with two sets of questions; a standard scoring criteria which matched that used by human raters, and a novel set of questions, both utilizing few‐shot and chain‐of‐thought prompting strategies. Result LLM scoring demonstrated moderately high correlations with human raters for both immediate ( r = 0.654, p &lt; .001) and delayed recall ( r = 0.655, p &lt; .001). Interrater reliability was comparable between LLM (ICC2k=0.580, p = .015) and human raters (ICC2k=0.574, p = .008). LLM scoring showed superior discrimination of cognitive status for immediate recall (t(26)=2.64, AUC=0.765, p = .013) compared to human scored responses which did not find any difference (t(26)=1.26, AUC=0.638, p = .218), while discrimination in human‐scored assessments was significantly better for the delayed recall responses (t(26)=2.50, AUC=0.747, p = .019) than LLMs (t(26)=1.57, AUC=0.662, p = .128). A novel set of questions was then developed to separate general from specific answers, with variable weighting per question, which exhibited an ability to improve discrimination in the immediate recall assessment (AUC=0.798, p = 0.010) compared to the standard questions, but not in the delayed component. Conclusion LLMs demonstrate potential as a reliable, cost‐effective alternative to human scoring, offering consistent performance and the ability to retrospectively apply modified scoring criteria for research purposes. However, the presence of hallucinations and score variability between model runs suggests that this technology is at a premature stage for use in clinical settings. Nonetheless, rapid advancements in the field may result this strategy being a viable alternative in the very near future, especially as more advanced reasoning models become more available and consistent.

**ИИ:** + · обе модели · подсчёт методики · GPT-4o scored Craft Story narrative recall transcripts using standard criteria; correlations and ICC with human raters reported.

**Решение:** =

---

### 1192 · R9209

**AI-Powered Role-Play in Higher Education: Extending Practice Beyond the Classroom**

2025 · NSUWorks (Nova Southeastern University) · conference-paper

Artificial Intelligence (AI) and Large Language Models (LLMs) are rapidly reshaping the landscape of higher education, offering new opportunities to enhance teaching, learning, and professional training. This session highlights findings from an exploratory study that investigated the use of AI-powered role-play in graduate psychology education. In the study, 24 graduate students engaged in simulated diagnostic interviews with an AI-generated caregiver profile and received both immediate AI feedback and traditional faculty evaluation. Results demonstrated statistically significant increases in student support for the use of AI in higher education after participation. Students reported that AI feedback was highly detailed and structured, complementing, but not replacing, the mentorship and expertise of faculty. This session will engage participants in exploring how AI can supplement faculty instruction by extending practice opportunities, supporting deliberate skill development, and offering individualized feedback at scale. At the same time, attention will be given to limitations and challenges identified by students, including technical reliability, authenticity of the simulation, and ethical considerations related to training future professionals. The intended audience includes faculty, instructional designers, and academic leaders interested in innovative, research-informed strategies for integrating AI into graduate and professional education.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: AI gave feedback on student diagnostic interviews and faculty also evaluated them; the abstract reports only student attitudes, so AI–faculty agreement is unclear.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: AI role-play simulation with AI feedback for psychology students; no LLM coding of texts compared against human codes reported, only student perceptions.)

**Решение:** -

---

### 1193 · R9214

**Large language models can segment narrative events similarly to humans.**

2025 · Behavior research methods · journal article, journalarticle, preprint/article · eng · https://doi.org/10.3758/s13428-024-02569-z

Humans perceive discrete events such as "restaurant visits" and "train rides" in their continuous experience. One important prerequisite for studying human event perception is the ability of researchers to quantify when one event ends and another begins. Typically, this information is derived by aggregating behavioral annotations from several observers. Here, we present an alternative computational approach where event boundaries are derived using a large language model, GPT-3, instead of using human annotations. We demonstrate that GPT-3 can segment continuous narrative text into events. GPT-3-annotated events are significantly correlated with human event annotations. Furthermore, these GPT-derived annotations achieve a good approximation of the "consensus" solution (obtained by averaging across human annotations); the boundaries identified by GPT-3 are closer to the consensus, on average, than boundaries identified by individual human annotators. This finding suggests that GPT-3 provides a feasible solution for automated event annotations, and it demonstrates a further parallel between human cognition and prediction in large language models. In the future, GPT-3 may thereby help to elucidate the principles underlying human event perception.

**ИИ:** ? · обе модели · неясен конструкт · GPT-3 event-boundary segmentation of narratives compared with human annotations; it is unclear whether event perception counts as a psychological construct for this review.

**Решение:** =

---

### 1194 · R9216

**Rating the Experiencing Scale with generative AI: examining the accuracy, reliability, and feasibility of ChatGPT**

2025 · Person-Centered & Experiential Psychotherapies · article · en · https://doi.org/10.1080/14779757.2025.2601985

In recent years, psychotherapy research has seen increasing interest in the application of generative AI, accompanied by advances in natural language understanding. The Experiencing Scale (EXP Scale) is a valuable instrument for evaluating psychotherapeutic processes and outcomes, but ratings require specialized training and time, posing challenges for large-scale analysis. Generative AI may offer a solution. This study examined the accuracy, reliability, and feasibility of EXP Scale ratings using ChatGPT (GPT-4o and OpenAI o1). Both seven-stage ratings and a simplified three-stage version (Low, Middle, High) were evaluated against expert ratings (primarily based on Klein et al., 1970). As a result, high agreement was observed in the three-stage ratings, suggesting potential utility as a screening tool for identifying Stage 4 and above, a critical turning point in psychotherapy. Although the seven-stage ratings often misclassified Stages 1 and 6 and lacked sufficient accuracy, they generally aligned with expert ratings. Therefore, improvements in prompts and models may enhance rating precision. Additionally, a supplemental evaluation of Japanese segments demonstrated performance comparable to or exceeding that of the English segments. Despite its limitations, generative AI’s ability to rate much faster than humans suggests its potential as a valuable adjunct to psychotherapy research and clinical practice.

**ИИ:** + · обе модели · кодирование сессий · GPT-4o and o1 rated psychotherapy segments on the Experiencing Scale; their ratings were compared with expert ratings.

**Решение:** =

---

### 1195 · R9231

**Reasoning Beyond Labels: Measuring LLM Sentiment in Low-Resource, Culturally Nuanced Contexts**

2025 · Proceedings of the 7th Workshop on African Natural Language Processing (AfricaNLP 2026) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2508.04199

Sentiment analysis in low-resource, culturally nuanced contexts challenges conventional NLP approaches that assume fixed labels and universal affective expressions. We present a diagnostic framework that treats sentiment as a context-dependent, culturally embedded construct, and evaluate how large language models (LLMs) reason about sentiment in informal, code-mixed WhatsApp messages from Nairobi youth health groups. Using a combination of human-annotated data, sentiment-flipped counterfactuals, and rubric-based explanation evaluation, we probe LLM interpretability, robustness, and alignment with human reasoning. Framing our evaluation through a social-science measurement lens, we operationalize and interrogate LLMs outputs as an instrument for measuring the abstract concept of sentiment. Our findings reveal significant variation in model reasoning quality, with top-tier LLMs demonstrating interpretive stability, while open models often falter under ambiguity or sentiment shifts. This work highlights the need for culturally sensitive, reasoning-aware AI evaluation in complex, real-world communication.

**ИИ:** ? · обе модели · неясен конструкт · LLMs labelled sentiment in youth health-group WhatsApp messages against human annotations; unclear whether sentiment here counts as a psychological/emotional construct.

**Решение:** =

---

### 1196 · R9246

**Can You Share Your Story? Modeling Clients' Metacognition and Openness for LLM Therapist Evaluation**

2025 · Annual Meeting of the Association for Computational Linguistics · journalarticle, conference, preprint/article · https://doi.org/10.18653/v1/2025.findings-acl.1332

Understanding clients' thoughts and beliefs is fundamental in counseling, yet current evaluations of LLM therapists often fail to assess this ability. Existing evaluation methods rely on client simulators that clearly disclose internal states to the therapist, making it difficult to determine whether an LLM therapist can uncover unexpressed perspectives. To address this limitation, we introduce MindVoyager, a novel evaluation framework featuring a controllable and realistic client simulator which dynamically adapts itself based on the ongoing counseling session, offering a more realistic and challenging evaluation environment. We further introduce evaluation metrics that assess the exploration ability of LLM therapists by measuring their thorough understanding of client's beliefs and thoughts. Published at ACL 2025 Findings

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Client simulator plus evaluation metrics for LLM therapists' understanding of client beliefs; unclear whether LLM-based metrics were validated against human ratings.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Client simulator and evaluation metrics for LLM therapists; no LLM coding of texts compared with human labels evident in the abstract.)

**Решение:** -

---

### 1197 · R9250

**Modeling Affect in Speech and Language in the Presence of Natural Inconsistency**

2025 · Deep Blue (University of Michigan) · dissertation/none, dissertation · en · https://doi.org/10.7302/27095

Understanding human affect, including emotions and moods, is crucial for a wide range of applications, from improving mental health monitoring to enhancing user experiences in human-computer interaction. The complex, ambiguous, and subjective nature of human affect poses many challenges in developing affect recognition models, such as disagreements in human labels and misaligned signals across modalities (e.g., text and voice). While these inconsistencies present obstacles, they reflect fundamental aspects of human affect and can offer valuable signals for affect modeling if properly harnessed. By addressing these challenges and effectively making use of the information embedded in these inconsistencies, we can work toward building more reliable, interpretable, and human-aligned affect recognition systems. This dissertation investigates the causes and effects of inconsistencies in affect models and explores strategies to mitigate their impact or to use them as informative signals. We focus on emotions expressed through speech and language, the most common modes of communication, particularly in interactions with intelligent systems. First, we examine modality inconsistency: emotions conveyed through text and vocal modalities do not always align. In the mental health domain, we demonstrate that their mismatch carries important information about people’s mood and can serve as signals for mood disorder monitoring. We extend this finding and more broadly show that modeling text and acoustic modalities separately allows for disentangling their respective information, yielding richer and more robust speech representations for various speech understanding tasks. Second, we examine annotation inconsistency observed in human emotion labels of text data, highlighting their variability and sensitivity to annotation study designs. We compare human and Large Language Models (LLMs) generated annotations and find that LLMs achieve strong performance. Building on this insight, we propose integrating LLMs into the human annotation workflow, which improves both the annotators’ experience and the quality of the labels. We then explore interpersonal inconsistency caused by the subjectivity of emotion perception across individuals. We show that emotion perception significantly differs across demographic and personality groups, and incorporating annotator-level information can improve personalized speech emotion recognition models. Finally, drawing on insights from annotation and interpersonal inconsistencies, we propose a contrastive distillation framework that transfers the generalizable emotion understanding capabilities of LLMs into a lightweight text emotion recognition model. Leveraging the breadth of LLMs’ pretraining, the distilled model learns an efficient, emotion-salient embedding space and can seamlessly handle unseen emotion label spaces without extra training. Together, these findings offer a new perspective on the role of inconsistencies in affective modeling. It is important to understand their origins and implications, develop strategies to mitigate unintended ones, and leverage useful signals from them, to achieve a more comprehensive understanding and modeling of human affect.

**ИИ:** + · обе модели · бенчмарк с метками людей · Dissertation compares LLM-generated emotion annotations of text with human emotion labels; agreement likely reported.

**Решение:** =

---

### 1198 · R9254

**Understanding Graduate School Through AI: A Scalable Approach to Thematic Coding**

2025 · International Journal of Qualitative Methods · journalarticle, article, journal-article · en · https://doi.org/10.1177/16094069251395943

This study explores the application of artificial intelligence (AI) in qualitative research, specifically examining how large language models (LLMs) can be utilized to code qualitative data and identify relationships among coder-defined themes. The approach is particularly useful for cases where researchers have previously-identified themes and hypotheses but lack the resources to code a large corpus of data manually. We outline a multi-step methodological framework grounded in qualitative research traditions, whereby researchers first conduct manual coding using a grounded theory approach (Charmaz, 2006; Glaser &amp; Strauss, 1967) on a subset of the data. The resulting codes are then applied to the remaining data using a model-assisted process that integrates natural language processing, AI-based text classification (Noah et al., 2024), and topic identification. Lastly, this is followed by statistical analyses to test hypotheses and expected patterns, providing a robust approach to ensure reliability and accuracy. We illustrate this process through the systematic application of locally-run AI for coding interview transcripts related to graduate students’ experiences in four Ph.D. programs at a large research university. We demonstrate how AI can improve the efficiency, consistency, and scalability of qualitative research without sacrificing confidentiality. This study highlights the potential for AI to enhance qualitative research processes while addressing challenges related to nuance and interpretation.

**ИИ:** ? · обе модели · неясен конструкт · Local LLM applies human-derived codes to interviews about graduate student experiences. It's unclear whether the codes are psychological and whether agreement with humans is reported.

**Решение:** =

---

### 1199 · R9283

**Emotion in Context: Human and AI Perspectives on the Affective Landscape of Severance**

2025 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-7997646/v1

Abstract Emotion identification has long been a focus of interdisciplinary research spanning psychology, linguistics, and discourse analysis. Prior to the advent of artificial intelligence and large language models (LLMs), emotion recognition relied heavily on annotation and sentiment lexicons (e.g., Mohammad & Turney, 2013), often supported by sentiment analysis tools with limited sensitivity to contextual nuance. These traditional approaches, however, struggled with the complexity of emotional expression, particularly in multimodal or narrative-rich texts. Recent advances in natural language processing (NLP), particularly the development of LLMs, offer new possibilities for automating emotion detection with greater contextual awareness. This study investigates how emotions are represented and perceived in the television series Severance (Apple TV, 2022) through a multi-layered annotation framework based on Parrott’s hierarchical taxonomy of emotions. All nine episodes of season 1 were annotated scene by scene, producing four datasets: human text-only, human multimodal (video + audio + text), and two large-language-model (LLM) outputs. Comparative analyses assessed inter-annotator agreement, modality effects, and temporal and character-based emotion patterns. Results show that multimodal annotations yield a far richer and more nuanced emotional landscape than text alone, highlighting the decisive role of prosody, gesture, and facial expression in conveying affect. LLMs captured general emotional polarity but failed to reproduce fine-grained distinctions. Character profiles further reveal individualized affective strategies of repression, resistance, and awakening. The findings underscore the inherently multimodal nature of emotional meaning in audiovisual narrative.

**ИИ:** разошлись — Opus + (кодирование по кодбуку: Humans and LLMs annotated TV-series scene text for emotions using Parrott's taxonomy; inter-annotator agreement between them was compared.); Sonnet ? (неясен конструкт: LLM and human annotators coded emotions (Parrott taxonomy) in TV series scenes with agreement analysed; fictional audiovisual material rather than psychological or clinical text, so eligibility is unclear.)

**Решение:** +

---

### 1200 · R9321

**Beyond Keywords: Evaluating Large Language Model Classification of Nuanced Ableism**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2505.20500

Large language models (LLMs) are increasingly used in decision-making tasks like r\'esum\'e screening and content moderation, giving them the power to amplify or suppress certain perspectives. While previous research has identified disability-related biases in LLMs, little is known about how they conceptualize ableism or detect it in text. We evaluate the ability of four LLMs to identify nuanced ableism directed at autistic individuals. We examine the gap between their understanding of relevant terminology and their effectiveness in recognizing ableist content in context. Our results reveal that LLMs can identify autism-related language but often miss harmful or offensive connotations. Further, we conduct a qualitative comparison of human and LLM explanations. We find that LLMs tend to rely on surface-level keyword matching, leading to context misinterpretations, in contrast to human annotators who consider context, speaker identity, and potential impact. On the other hand, both LLMs and humans agree on the annotation scheme, suggesting that a binary classification is adequate for evaluating LLM performance, which is consistent with findings from prior studies involving human annotators.

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: The LLMs detect ableist or offensive content against human annotations, which counts as hate-speech or offensive-content classification rather than a psychological construct.); Sonnet ? (неясен конструкт: LLMs classify ableism toward autistic people against human annotations; construct resembles hate speech/offensive content, so psychological relevance is unclear.)

**Решение:** -
