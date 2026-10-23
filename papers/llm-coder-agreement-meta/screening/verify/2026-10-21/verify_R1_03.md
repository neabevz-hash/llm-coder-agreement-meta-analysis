# Проверка с метками ИИ, часть 3

Записи 301–450 из 1304, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

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

### 301 · R11489

**Automatic Annotation of Dream Report’s Emotional Content with Large Language Models**

2024 · Workshop on Computational Linguistics and Clinical Psychology · audiovisual/conference talk · https://doi.org/10.18653/v1/2024.clpsych-1.7

In the field of dream research, the study of dream content typically relies on the analysis of verbal reports provided by dreamers upon awakening from their sleep. This task is classically performed through manual scoring provided by trained annotators, at a great time expense. While a consistent body of work suggests that natural language processing (NLP) tools can support the automatic analysis of dream reports, proposed methods lacked the ability to reason over a report’s full context and required extensive data pre-processing. Furthermore, in most cases, these methods were not validated against standard manual scoring approaches. In this work, we address these limitations by adopting large language models (LLMs) to study and replicate the manual annotation of dream reports, using a mixture of off-the-shelf and bespoke approaches, with a focus on references to reports’ emotions. Our results show that the off-the-shelf method achieves a low performance probably in light of inherent linguistic differences between reports collected in different (groups of) individuals. On the other hand, the proposed bespoke text classification method achieves a high performance, which is robust against potential biases. Overall, these observations indicate that our approach could find application in the analysis of large dream datasets and may favour reproducibility and comparability of results across studies.

**ИИ:** + · обе модели · кодирование по кодбуку · LLMs annotate emotions in dream reports and are validated against manual scoring by trained annotators; need to check that the models are generative rather than encoder-only.

**Решение:** =

---

### 302 · R11490

**Large Language Models Perform on Par with Experts Identifying Mental Health Factors in Adolescent Online Forums**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2404.16461

Mental health in children and adolescents has been steadily deteriorating over the past few years. The recent advent of Large Language Models (LLMs) offers much hope for cost and time efficient scaling of monitoring and intervention, yet despite specifically prevalent issues such as school bullying and eating disorders, previous studies on have not investigated performance in this domain or for open information extraction where the set of answers is not predetermined. We create a new dataset of Reddit posts from adolescents aged 12-19 annotated by expert psychiatrists for the following categories: TRAUMA, PRECARITY, CONDITION, SYMPTOMS, SUICIDALITY and TREATMENT and compare expert labels to annotations from two top performing LLMs (GPT3.5 and GPT4). In addition, we create two synthetic datasets to assess whether LLMs perform better when annotating data as they generate it. We find GPT4 to be on par with human inter-annotator agreement and performance on synthetic data to be substantially higher, however we find the model still occasionally errs on issues of negation and factuality and higher performance on synthetic data is driven by greater complexity of real data rather than inherent advantage.

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT-3.5/4 annotations of adolescent Reddit posts for mental health factors compared with expert psychiatrist labels.

**Решение:** =

---

### 303 · R11494

**Automated Assessment of Creativity in Multilingual Narratives**

2024 · PsyArXiv · preprint, ppr, article · en · https://doi.org/10.31234/osf.io/f4a2g

Researchers and educators interested in creative writing need a reliable and efficient tool to score the creativity of narratives, such as short stories. Typically, human raters manually assess narrative creativity, but such subjective scoring is limited by labor costs and rater disagreement. Large language models (LLMs) have shown remarkable success on creativity tasks, yet they have not been applied to scoring narratives, including multilingual stories. In the present study, we aimed to test whether narrative originality-a component of creativity-could be automatically scored by LLMs, further evaluating whether a single LLM could predict human originality ratings across multiple languages. We trained three different LLMs to predict the originality of short stories written in 11 languages. Our first monolingual model, trained only on English stories, robustly predicted human originality ratings (r = .81). This same model-trained and tested on multilingual stories translated into English-strongly predicted originality ratings of multilingual narratives (r >= .73). Finally, a multilingual model trained on the same stories, in their original language, reliably predicted human originality scores across all languages (r >= .72). We thus demonstrate that LLMs can successfully score narrative creativity in 11 different languages, surpassing the performance of the best previous automated scoring techniques (e.g., semantic distance). This work represents the first effective, accessible, and reliable solution for the automated scoring of creativity in multilingual narratives.

**ИИ:** + · обе модели · подсчёт методики · Fine-tuned LLMs score story originality (creativity) and are correlated with human ratings; check full text that the models are decoder models.

**Решение:** =

---

### 304 · R11508

**Under the (neighbor)hood: Hyperlocal Surveillance on Nextdoor**

2024 · CHI Conference on Human Factors in Computing Systems · book, journalarticle, conference · en · https://doi.org/10.1145/3613904.3641967

This paper examines the tensions between neighborhood gentrification and community surveillance posts on Nextdoor, a hyperlocal social media platform for neighborhoods. We created a privacy-preserving pipeline to gather research data from public Nextdoor posts in Atlanta, Georgia and filtered these to a dataset of 1,537 community surveillance posts. We developed a qualitative codebook to label observed patterns of community surveillance, and deploy a large language model to tag these posts at scale. Ultimately, we present an extensible and empirically-tested typology of the modes of community surveillance that occur on hyperlocal platforms. We find a complex relationship between community surveillance posts and neighborhood gentrification, which indicates that publicly disclosing information about perceived outsiders, especially for petty crimes, is most prevalent in gentrifying neighborhoods. Our empirical evidence inform critical perspectives which posit that community surveillance on platforms like Nextdoor can exclude and marginalize minoritized populations, particularly in gentrifying neighborhoods. Our findings carry broader implications for hyperlocal social platforms and their potential to amplify and exacerbate social tensions and exclusion.

**ИИ:** разошлись — Opus ? (неясен конструкт: An LLM applies a qualitative codebook to Nextdoor posts, probably checked against human coding. It is unclear whether community surveillance counts as a psychological construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM tags Nextdoor posts with a codebook, but the construct is community surveillance and gentrification (sociological), not a psychological or clinical construct.)

**Решение:** -

---

### 305 · R11538

**Close to Human-Level Agreement: Tracing Journeys of Violent Speech in Incel Posts with GPT-4-Enhanced Annotations**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2401.02001

This study investigates the prevalence of violent language on incels.is. It evaluates GPT models (GPT-3.5 and GPT-4) for content analysis in social sciences, focusing on the impact of varying prompts and batch sizes on coding quality for the detection of violent speech. We scraped over 6.9M posts from incels.is and categorized a random sample into non-violent, explicitly violent, and implicitly violent content. Two human coders annotated 3,028 posts, which we used to tune and evaluate GPT-3.5 and GPT-4 models across different prompts and batch sizes regarding coding reliability. The best-performing GPT-4 model annotated an additional 30,000 posts for further analysis. Our findings indicate an overall increase in violent speech overtime on incels.is, both at the community and individual level, particularly among more engaged users. While directed violent language decreases, non-directed violent language increases, and self-harm content shows a decline, especially after 2.5 years of user activity. We find substantial agreement between both human coders (K = .65), while the best GPT-4 model yields good agreement with both human coders (K = 0.54 for Human A and K = 0.62 for Human B). Weighted and macro F1 scores further support this alignment. Overall, this research provides practical means for accurately identifying violent language at a large scale that can aid content moderation and facilitate next-step research into the causal mechanism and potential mitigations of violent expression and radicalization in communities like incels.is.Comment: 10 pages, 2 figures, 3 table

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-4 coded incel posts for violent speech and self-harm (risk constructs); kappa agreement with two human coders reported.

**Решение:** =

---

### 306 · R11551

**AI-Enhanced Cognitive Behavioral Therapy: Deep Learning and Large Language Models for Extracting Cognitive Pathways from Social Media Texts**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2404.11449

Cognitive Behavioral Therapy (CBT) is an effective technique for addressing the irrational thoughts stemming from mental illnesses, but it necessitates precise identification of cognitive pathways to be successfully implemented in patient care. In current society, individuals frequently express negative emotions on social media on specific topics, often exhibiting cognitive distortions, including suicidal behaviors in extreme cases. Yet, there is a notable absence of methodologies for analyzing cognitive pathways that could aid psychotherapists in conducting effective interventions online. In this study, we gathered data from social media and established the task of extracting cognitive pathways, annotating the data based on a cognitive theoretical framework. We initially categorized the task of extracting cognitive pathways as a hierarchical text classification with four main categories and nineteen subcategories. Following this, we structured a text summarization task to help psychotherapists quickly grasp the essential information. Our experiments evaluate the performance of deep learning and large language models (LLMs) on these tasks. The results demonstrate that our deep learning method achieved a micro-F1 score of 62.34% in the hierarchical text classification task. Meanwhile, in the text summarization task, GPT-4 attained a Rouge-1 score of 54.92 and a Rouge-2 score of 30.86, surpassing the experimental deep learning model's performance. However, it may suffer from an issue of hallucination. We have made all models and codes publicly available to support further research in this field.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Social-media posts human-annotated for cognitive pathways/distortions; LLMs (GPT-4) and deep learning models evaluated against these labels.); Sonnet ? (другое: Human-annotated cognitive-pathway dataset from social media; LLMs evaluated on tasks, but unclear whether LLMs did the classification against human labels (GPT-4 reported only for summarization).)

**Решение:** +

---

### 307 · R11553

**Automated Annotation of Academic Emotion Intensity in Online Learning Comment Texts: A BWS Method Based on LLMs**

2024 · International Conference on Education Technology and Computers (ICETC) · book, journalarticle, conference-paper · en · https://doi.org/10.1145/3702163.3702432

Academic emotions significantly impact learning processes and student performance, with a recent trend towards automated measurement for their types and intensity. However, manual annotation methods for large-scale training data required by modeling face issues of time consumption and high cost. The Best Worst Scaling (BWS) methodology enhances the reliability of intensity annotation, while Large Language Models (LLMs) offer advantages in understanding academic emotions across diverse contexts. Combining the BWS and LLMs in academic emotion intensity annotation, this study aims to address the challenge of data annotation in measuring academic emotion intensity in online learning. We choose three widely recognized LLMs to complete the BWS annotation tasks separately, then calculate the consistency and conduct statistical analysis. Results indicate that the consistency of the three LLMS in identifying emotion intensity in nine academic emotions was above 0.750, with a total of 0.865 in 4569 comment texts. The perception of emotion intensity by the LLMs closely resembles that of human cognition and responds to the context of online learning, enabling them to effectively substitute for humans in performing large-scale annotation tasks.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLMs rate academic emotion intensity in comments using BWS; the reported consistency may be between LLMs only, and human comparison is unclear.

**Решение:** =

---

### 308 · R11556

**Evaluating Creative Short Story Generation in Humans and Large Language Models**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2411.02316

Story-writing is a fundamental aspect of human imagination, relying heavily on creativity to produce narratives that are novel, effective, and surprising. While large language models (LLMs) have demonstrated the ability to generate high-quality stories, their creative story-writing capabilities remain under-explored. In this work, we conduct a systematic analysis of creativity in short story generation across 60 LLMs and 60 people using a five-sentence cue-word-based creative story-writing task. We use measures to automatically evaluate model- and human-generated stories across several dimensions of creativity, including novelty, surprise, diversity, and linguistic complexity. We also collect creativity ratings and Turing Test classifications from non-expert and expert human raters and LLMs. Automated metrics show that LLMs generate stylistically complex stories, but tend to fall short in terms of novelty, surprise and diversity when compared to average human writers. Expert ratings generally coincide with automated metrics. However, LLMs and non-experts rate LLM stories to be more creative than human-generated stories. We discuss why and how these differences in ratings occur, and their implications for both human and artificial creativity. Accepted to ICCC 2025

**ИИ:** разошлись — Opus + (подсчёт методики: LLMs and expert/non-expert humans rated the creativity of the same stories from a cue-word story task, so LLM–human agreement can be compared.); Sonnet ? (неясен конструкт: LLMs and humans rate creativity of the same short stories, so agreement is possible. It is unclear whether story creativity counts as a psychological construct or as writing quality.)

**Решение:** +

---

### 309 · R11571

**“Who” Is the Best Creative Thinking Partner? An Experimental Investigation of Human–Human, Human–Internet, and Human– AI Co‐Creation**

2024 · The Journal of Creative Behavior · journalarticle, article · en · https://doi.org/10.1002/jocb.1519

ABSTRACT Recent research suggests that working with generative artificial intelligence (AI), such as ChatGPT, can produce more creative outcomes than humans alone. However, does AI retain its creative edge when humans have access to alternative information sources, such as another human or the internet. We explored this question in a between‐group experiment with 202 German participants across four conditions (human–human dyads, human–Internet, and two human–AI groups with basic or specific instructions) and four creativity tasks (two alternate uses tasks, a consequences task, and a problem‐solving task). Results showed that the human–human condition obtained higher creativity scores in the divergent thinking tasks than the remaining groups. No significant between‐group differences were observed in the problem‐solving task. Moreover, interacting in human dyads made people more creatively confident, an effect not observed in the other groups. In addition, we compared human‐rated outcomes with AI‐based automated scoring (Ocsai). Interestingly, notable discrepancies emerged between the AI assessment and the human‐judged results, raising concerns about AI's susceptibility to “elaboration bias.” These findings highlight the benefits of human collaboration for creativity and call for further studies about the reliability and potential biases of AI in evaluating creative performance.

**ИИ:** + · обе модели · подсчёт методики · Ocsai, a fine-tuned GPT-based scorer, rated divergent thinking responses and was compared with human ratings of the same responses.

**Решение:** =

---

### 310 · R11580

**Empathic Dialog Systems for Patient Intake: Balancing Task-Completion and Emotional Support using RAGs**

2024 · ACM International Conference on Intelligent Virtual Agents (IVA) · journalarticle, book, conference-paper · en · https://doi.org/10.1145/3652988.3673968

Dialogue systems are increasingly recognized as valuable assets in healthcare, aiding in the support of individuals grappling with mental health challenges. In this paper, we develop and evaluate a task-oriented empathic chatbot, EmoBot, in a mental healthcare patient intake scenario. EmoBot employs Retrieval-Augmented Generation (RAG) methods to provide guardrails to Large Language Models (LLMs) in providing targeted empathic support, while ensuring task-completion of administering PHQ-9 intake questionnaire. We evaluate EmoBot’s performance by using a simulated patient model to mimic varying levels of depression severity. Our preliminary results showed high task completion rates and agreement between EmoBot’s depression severity categorization and human raters, demonstrating the promise of RAG-based methods in guiding LLMs to be used for health assessment and support.

**ИИ:** разошлись — Opus + (клиническая оценка: The LLM chatbot sorted depression severity from simulated PHQ-9 intake dialogues into categories, and the abstract reports agreement with human raters on the same dialogues.); Sonnet ? (неясно, сравнивали ли с людьми: Mainly a chatbot-generation study, but the LLM's depression severity categorisation is compared with human raters on simulated patient dialogues; full text is needed to confirm.)

**Решение:** +

---

### 311 · R11581

**Enhancing Patient Intake Process in Mental Health Consultations Using RAG-Driven Chatbot**

2024 · International Conference on Affective Computing and Intelligent Interaction Workshops and Demos (ACIIW) · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/aciiw63320.2024.00053

In this paper, we develop and evaluate an empathic chatbot, called EmoBot, for a mental healthcare patient in-take scenario. EmoBot employs Retrieval-Augmented Generation (RAG) methods with Large Language Models (LLMs), to provide empathic support and advice, while ensuring the intake process is completed. We evaluate EmoBot's performance both by automated metrics using available datasets and through dialogues with a simulated patient model that mimics varying levels of depression severity. Our evaluations showed good agreement between EmoBot's categorization of depression severity levels and human raters. EmoBot's topic classification system achieved 78.48% accuracy on the Primate2022 dataset [1] without fine-tuning. EmoBot's responses showed a 0.93 similarity with patient inputs, proving contextual relevance. These findings highlight the effectiveness of RAG-based methods in guiding and providing safety guardrails for LLMs and their potential as supportive tools for health assessment and support.

**ИИ:** разошлись — Opus + (клиническая оценка: The LLM chatbot's depression-severity ratings are compared with human raters, and its classification is scored for accuracy on the human-annotated PRIMATE dataset.); Sonnet ? (неясно, сравнивали ли с людьми: Chatbot development paper; reports agreement of LLM depression severity categorization with human raters, but unclear whether the same texts were coded; full text needed.)

**Решение:** +

---

### 312 · R11584

**From Text to Emotion: Unveiling the Emotion Annotation Capabilities of LLMs**

2024 · Interspeech (USB) · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.21437/interspeech.2024-2282

Training emotion recognition models has relied heavily on human annotated data, which present diversity, quality, and cost challenges. In this paper, we explore the potential of Large Language Models (LLMs), specifically GPT4, in automating or assisting emotion annotation. We compare GPT4 with supervised models and or humans in three aspects: agreement with human annotations, alignment with human perception, and impact on model training. We find that common metrics that use aggregated human annotations as ground truth can underestimate the performance, of GPT-4 and our human evaluation experiment reveals a consistent preference for GPT-4 annotations over humans across multiple datasets and evaluators. Further, we investigate the impact of using GPT-4 as an annotation filtering process to improve model training. Together, our findings highlight the great potential of LLMs in emotion annotation tasks and underscore the need for refined evaluation methodologies. to be published in Interspeech 2024

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT-4 annotates emotion in text across datasets; its labels are compared with human annotations, so agreement can be reported.

**Решение:** =

---

### 313 · R11585

**The Language of Trauma: Modeling Traumatic Event Descriptions Across Domains with Explainable AI**

2024 · Conference on Empirical Methods in Natural Language Processing · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2024.findings-emnlp.773

Psychological trauma can manifest following various distressing events and is captured in diverse online contexts. However, studies traditionally focus on a single aspect of trauma, often neglecting the transferability of findings across different scenarios. We address this gap by training various language models with progressing complexity on trauma-related datasets, including genocide-related court data, a Reddit dataset on post-traumatic stress disorder (PTSD), counseling conversations, and Incel forum posts. Our results show that the fine-tuned RoBERTa model excels in predicting traumatic events across domains, slightly outperforming large language models like GPT-4. Additionally, SLALOM-feature scores and conceptual explanations effectively differentiate and cluster trauma-related language, highlighting different trauma aspects and identifying sexual abuse and experiences related to death as a common traumatic event across all datasets. This transferability is crucial as it allows for the development of tools to enhance trauma detection and intervention in diverse populations and settings.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · GPT-4 classifies traumatic events in trauma-related texts; unclear whether reference labels come from human annotation or from dataset/subreddit membership.

**Решение:** =

---

### 314 · R11597

**Properties of Person Descriptors in the Natural German Language: A Pre-registered Replication Study Generating and Using a Large, Representative Item Sample**

2024 · preprint · en · https://doi.org/10.31124/advance.171681837.76924086/v1

Understanding language is crucial to psychological research, as it is the basis for almost all psychological measurements. Following previous works, we conducted a pre-registered replication study, analyzing 876 unique terms generated by 187 participants in a free response format. These terms were rated on social desirability, observability, importance, abstractness, base rate, and stability by approximately 15 raters each (n = 456). Key findings were replicated, including a bimodal distribution of social desirability, a greater number of negative vs. positive terms, and a u-shaped relationship between importance and social desirability. Using a Large Language Model (LLM) to derive synthetic social desirability estimates, we observed a moderate correlation (r = .65) with human ratings, but did not replicate all predicted effects. LLM-based item property estimates are not yet entirely equivalent to ratings by human participants but hold much promise for future research.

**ИИ:** ? · обе модели · неясен конструкт · An LLM rated the social desirability of participant-generated person-descriptor terms, correlating r=.65 with human ratings; unclear whether single-word items count as psychological text.

**Решение:** =

---

### 315 · R11607

**Can Machines Resonate with Humans? Evaluating the Emotional and Empathic Comprehension of LMs**

2024 · Conference on Empirical Methods in Natural Language Processing · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48550/arxiv.2406.11250

Empathy plays a pivotal role in fostering prosocial behavior, often triggered by the sharing of personal experiences through narratives. However, modeling empathy using NLP approaches remains challenging due to its deep interconnection with human interaction dynamics. Previous approaches, which involve fine-tuning language models (LMs) on human-annotated empathic datasets, have had limited success. In our pursuit of improving empathy understanding in LMs, we propose several strategies, including contrastive learning with masked LMs and supervised fine-tuning with large language models. While these methods show improvements over previous methods, the overall results remain unsatisfactory. To better understand this trend, we performed an analysis which reveals a low agreement among annotators. This lack of consensus hinders training and highlights the subjective nature of the task. We also explore the cultural impact on annotations. To study this, we meticulously collected story pairs in Urdu language and find that subjectivity in interpreting empathy among annotators appears to be independent of cultural background. Our systematic exploration of LMs' understanding of empathy reveals substantial opportunities for further investigation in both task formulation and modeling. 19 pages

**ИИ:** + · обе модели · бенчмарк с метками людей · Fine-tuned LLMs rate empathic similarity of personal narratives and are evaluated against human-annotated labels, including a new Urdu dataset.

**Решение:** =

---

### 316 · R11609

**Pseudo-Labeling With Large Language Models for Multi-Label Emotion Classification of French Tweets**

2024 · IEEE Access · journalarticle, article · en · https://doi.org/10.1109/access.2024.3354705

This study proposes a novel semi-supervised multi-label emotion classification approach for French tweets based on pseudo-labeling. Human subjectivity in emotional expression makes it difficult for a machine to learn. Therefore, it necessitates training supervised learning models on large datasets annotated by multiple annotators. However, creating such datasets can be costly and time-consuming. Moreover, aggregating annotations from multiple annotators to capture their collective emotional state adds complexity to the task. Semi-supervised learning techniques have shown effectiveness with limited datasets. Furthermore, Large language Models (LLMs), particularly Chat-GPT, have demonstrated superior annotation accuracy compared to annotations obtained from crowdsourcing platforms, when both are evaluated against expert-annotated data. This work introduces a novel approach for multi-label emotion classification of French tweets by leveraging pseudo-labels generated through Chat-GPT, a robust large language model. Using zero-shot, one-shot, and few-shot learning techniques, Chat-GPT annotates the unlabelled part of our dataset. These Chat-GPT-annotated pseudo-labels are then merged with manual annotations, facilitating the training of a multi-label emotion classification model via semi-supervised learning. Furthermore, within the context of our research, we present a new French tweet dataset, containing testimonials from people affected by an urban industrial incident. This dataset features 2,350 tweets, each manually annotated by three human annotators based on 8 pre-identified emotions. Benchmark results are presented for multi-label emotion classification models employing both fully supervised and semi-supervised approaches with pseudo-labeling. Our findings demonstrate the superiority of our approach for multi-label emotion classification over standard pseudo-labeling and an established baseline.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: ChatGPT annotates 8 emotions in French tweets that three humans also annotated; zero/few-shot annotation is likely compared with the human labels.); Sonnet ? (неясно, сравнивали ли с людьми: ChatGPT labels emotions in tweets with a human-annotated dataset available, but the abstract doesn't say whether ChatGPT–human agreement is reported directly.)

**Решение:** +

---

### 317 · R11617

**The Three Stages of Learning to Master a Sensory Augmentation Device: Activation - Acquisition - Integration**

2024 · bioRxiv · preprint, ppr · en · https://doi.org/10.1101/2024.07.17.603884

Abstract By augmenting sensory perception through technology, researchers study how humans use and perceive the novel sensory input provided. Nevertheless, little is known about how learning unfolds over time. To this end, 27 participants trained with an augmentation device (feelSpace belt), which provides tactile feedback about the direction of the cardinal north, over the course of six weeks. During the training phase, we tracked participants’ progress using two different self-report questionnaires containing Likert-scale and open questions. Experts quantified responses to open questions using a previously established category system. As human raters are known to be susceptible to biases, we later reproduced the expert categorization using ChatGPT-4, finding a high congruence between the two classification approaches. The results suggest a three-stage model that best describes the process of acquiring an augmented sense. During the early activation stage, processing the augmented signal requires effort, induces fatigue, and a heightened awareness of the environment. In the knowledge acquisition phase, participants develop a more detailed cognitive spatial representation containing information about objects and places in relation to their current location. The deep integration stage is marked by participants seamlessly integrating the augmented information into existing perceptual processes and automatic use. The results support the supervised use of large language models (LLMs) for the analysis of qualitative data.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-4 used an established category system to code open self-report responses about perceptual and cognitive experience; its codes were compared with expert categorization.

**Решение:** =

---

### 318 · R1163

**Automating Motivational Interviewing Coding in Adolescent Substance Use Prevention: Human-AI Agreement Study.**

2026 · JMIR AI · journal article, journalarticle, review · eng · https://doi.org/10.2196/95964

Abstract Background Motivational interviewing (MI) is widely used in preventive interventions, yet coding MI techniques and monitoring intervention adherence remain resource-intensive due to the reliance on manual transcription and expert review. Large language models (LLMs) offer a promising approach to automate these tasks, but their agreement with human coders in the context of prevention interventions has not been established. Objective This study evaluated the agreement between an AI-based coder (OpenAI’s GPT 4.1) and trained human coders on two tasks: (1) identification of MI techniques (eg, open questions, affirmations, giving information) at the facilitator-message level and (2) completing a 21-item checklist of implementation adherence for a brief MI-based preventive intervention for adolescent substance use. Methods Two certified MI facilitators independently coded 72 facilitator messages from 2 standardized Spanish-language Brief Intervention Based on Motivational Interviewing program (Intervención Breve Basada en Entrevista Motivacional [IBEM]) practice sessions with chatbot-simulated adolescent responses. The facilitators classified MI techniques using the OARS (open questions, affirmations, reflections, and summaries) framework and completed a 21-item implementation-adherence checklist. An AI-based coder (OpenAI’s GPT-4.1, accessed through the API) classified the same facilitator messages and checklist items using a structured prompt derived from the MI coding manual. MI techniques were compared at the facilitator-message level and implementation adherence at the session level. Intercoder agreement in use of MI techniques and implementation adherence was assessed using Cohen κ, Fleiss κ, and Cochran Q tests. Results For use of MI techniques, the AI coder demonstrated moderate-to-substantial agreement with human coders across most techniques, including open questions (κ=0.66-0.69), affirmations (κ=0.66-0.77), and giving information (κ=0.91). No statistically significant differences in percentages of MI technique use were observed among the 3 coders, although agreement was the weakest for higher-inference categories such as complex reflections (κ=0.00). For MI implementation adherence, overall agreement was moderate (Fleiss κ=0.487), and pairwise agreement between the AI coder and 1 human coder was substantial (κ=0.67), exceeding the agreement observed between the 2 human coders (κ=0.53). Conclusions These findings provide support for the feasibility of using LLMs to recognize MI techniques and assess implementation adherence. The results support a human-AI collaborative model in which the AI coder “precodes” facilitator messages and flags sessions for expert review, while human coders retain responsibility for higher-inference judgments and shift their effort from routine coding toward contextual review and coaching feedback. Because the analyses are based on only 2 sessions, these results should be interpreted as early-stage, proof-of-concept evidence rather than a basis for large-scale deployment. Future research should compare different LLMs and evaluate whether AI-assisted coding improves the scalability of routine implementation monitoring.

**ИИ:** + · обе модели · кодирование сессий · GPT-4.1 coded MI techniques and adherence in intervention sessions and was compared with certified human coders using kappa.

**Решение:** =

---

### 319 · R11632

**Leveraging Large Language Model ChatGPT for enhanced understanding of end-user emotions in social media feedbacks**

2024 · Expert Systems with Applications · article · en · https://doi.org/10.1016/j.eswa.2024.125524

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; ChatGPT classifying emotions in user feedback, possibly compared with human annotations, but this is unclear.

**Решение:** =

---

### 320 · R11657

**Assessment of the Capability of Artificial Intelligence for Psychiatric Diagnosis**

2024 · European Psychiatry · journalarticle, article · en · https://doi.org/10.1192/j.eurpsy.2024.1722

Introduction Psychopathological exploration (PPE) involves an assessment of the mental state of patients, where psychological signs and symptoms are analyzed, which collectively form a syndrome. To conduct this assessment, the clinician must utilize their expertise to identify the presence and authenticity of a series of symptoms that, once recognized, allow for a diagnosis (1). The presence of this subjective component could explain why, despite the continuous growth of artificial intelligence (AI), its application in clinical psychiatry practice remains limited. However, the combination of the clinician's work with AI could enhance diagnostic accuracy and our understanding of diseases (2). Objectives The objective of this study is to investigate whether AI can make accurate diagnoses through an initial psychopathological evaluation. Methods A random sample was selected from our medical records of all patients admitted to our acute mental health inpatient unit through the hospital's emergency services in the year 2022. An anonymized database was created, including sociodemographic information, the results of the psychopathological assessment in the emergency department, and the diagnosis at the time of discharge. The psychopathological assessment conducted in the emergency department was provided to the AI chatbot ChatGPT, with a request to establish a diagnosis according to the DSM-5. Diagnoses such as brief psychotic disorder, schizophreniform disorder, and schizophrenia were considered, given their acute symptom similarities, as well as major depressive disorder (unipolar) and bipolar disorder. The level of agreement between both diagnoses was evaluated using the kappa coefficient. Results The sample consisted of 15 patients, of whom 60% were male, with a mean age of 45 years (standard deviation = 15.6). 73.3% of the patients had prior mental health follow-up, and 66.7% had been previously hospitalized. Diagnoses included psychotic disorder in 33.3% of cases, bipolar disorder with manic episode in 26.7%, depressive disorder in 13.3%, delusional disorder in 13.3%, schizoaffective disorder in 6.7%, and borderline personality disorder in 6.7%. A kappa value of 0.561 was obtained, indicating a moderate degree of agreement between the diagnoses. Conclusions Despite the inherent subjectivity in psychopathological assessment, this study suggests that AI, in the form of natural language processing chatbots like ChatGPT, can be a useful tool to assist mental health professionals in the diagnostic process. While AI shows promising potential, it should not entirely replace the experience and clinical judgment of mental health professionals. Instead, the importance of potential collaboration between AI and clinicians for achieving more precise and comprehensive diagnoses is highlighted. Disclosure of Interest None Declared

**ИИ:** разошлись — Opus -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): ChatGPT diagnosis from ED notes compared with discharge diagnosis, not human coding of the same text; criterion validity.); Sonnet ? (неясно, кто ставил эталонные метки: ChatGPT diagnosed from ED psychopathology notes, with kappa against clinician discharge diagnosis. This could count as a clinician rating or as diagnosis prediction, so it needs a full-text check.)

**Решение:** -

---

### 321 · R11661

**Large Language Models for Predicting Empathic Accuracy Between a Designer and a User**

2024 · Journal of Mechanical Design · journalarticle, article · en · https://doi.org/10.1115/1.4067227

Abstract Empathic design research aims to gain deep and accurate user understanding. We can measure the designer's empathic ability as empathic accuracy (EA) in understanding the user's thoughts and feelings during an interview. However, the EA measure currently relies on human rating and is thus time-consuming, making the use of large language models (LLMs) an attractive alternative. It is essential to consider two significant constraints when implementing LLMs as a solution: the choice of LLM and the impact of domain-specific datasets. Datasets of the interactions between the designer and the user are not generally available. We present such a dataset consisting of the EA task employed in user interviews to measure empathic understanding. It consists of over 400 pairs of user thoughts or feelings matched with a designer's guess of the same and the human ratings of the accuracy. We compared the performance of six sentence embedding state-of-the-art LLMs with different pooling techniques on the EA task. We used the LLMs to extract semantic information before and after fine-tuning. We conclude that directly using LLMs based on their reported performance in general language tasks could result in errors when judging a designer's empathic ability. We also found that fine-tuning LLMs on our dataset improved their performance, but the model's ability to fit the EA task and pooling method also determined the LLM's performance. The results will provide insight for other LLM-based similarity analyses in design.

**ИИ:** разошлись — Opus ? (другое: Empathic accuracy scored against human ratings, but the 'sentence embedding LLMs' are likely encoder models; check which models were used.); Sonnet -5 (нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM: Uses sentence-embedding (encoder-type) models for similarity against human empathic accuracy ratings, not generative LLMs prompted to code or rate texts.)

**Решение:** ?

---

### 322 · R11666

**Advancing health coaching: A comparative study of large language model and health coaches.**

2024 · Artificial intelligence in medicine · comparative study, research support, non-u.s. gov't, journal article · eng · https://doi.org/10.1016/j.artmed.2024.103004

OBJECTIVE Recent advances in large language models (LLM) offer opportunities to automate health coaching. With zero-shot learning ability, LLMs could revolutionize health coaching by providing better accessibility, scalability, and customization. The aim of this study is to compare the quality of responses to clients' sleep-related questions provided by health coaches and an LLM. DESIGN, SETTING, AND PARTICIPANTS From a de-identified dataset of coaching conversations from a pilot randomized controlled trial, we extracted 100 question-answer pairs comprising client questions and corresponding health coach responses. These questions were entered into a retrieval-augmented generation (RAG)-enabled open-source LLM (LLaMa-2-7b-chat) to generate LLM responses. Out of 100 question-answer pairs, 90 were taken out and assigned to three groups of evaluators: experts, lay-users, and GPT-4. Each group conducted two evaluation tasks: (Task 1) a single-response quality assessment spanning five criteria-accuracy, readability, helpfulness, empathy, and likelihood of harm-rated on a five-point Likert scale, and (Task 2) a pairwise comparison to choose the superior response between pairs. A suite of inferential statistical methods, including the paired and independent sample t-tests, Pearson correlation, and chi-square tests, were utilized to answer the study objective. Recognizing potential biases in human judgment, the remaining 10 question-answer pairs were used to assess inter-evaluator reliability among the human evaluators, quantified using the interclass correlation coefficient and percentage agreement metrics. RESULTS Upon exclusion of incomplete data, the analysis included 178 single-response evaluations (Task 1) and 83 pairwise comparisons (Task 2). Expert and GPT-4 assessments revealed no discernible disparities in health coach and LLM responses across the five metrics. Contrarily, lay-users deemed LLM responses significantly more helpful than that of human coaches (p < 0.05). LLM responses were preferred in the majority (62.25 %, n = 155) of the aggregate 249 assessments, with all three evaluator groups favoring LLM over health coach inputs. While GPT-4 rated both health coach and LLM responses significantly higher than experts in terms of readability, helpfulness, and empathy, its ratings on accuracy and likelihood of harm aligned with those of experts. Response length positively correlated with accuracy and empathy scores, but negatively affected readability across all evaluator groups. Expert and lay-user evaluators demonstrated moderate to high inter-evaluator reliability. CONCLUSION Our study showed encouraging findings by demonstrating that RAG-enabled LLM has comparable performance to health coaches in the domain tested. Serving as an initial step towards the creation of more sophisticated, adaptive, round-the-clock automated health coaching systems, our findings call for more extensive evaluation which could assist in the development of the model that could in the future lead to potential clinical implementation.

**ИИ:** разошлись — Opus + (LLM-судья: GPT-4 and experts rated the same health-coaching responses on empathy, harm and other criteria, and the two sets of ratings were compared.); Sonnet ? (неясен конструкт: GPT-4 rated health-coach and LLM sleep-coaching responses (including empathy) alongside experts, so LLM–human comparison exists. Whether sleep coaching counts as a psychological construct is unclear.)

**Решение:** +

---

### 323 · R1168

**Theme-Specific Responses to Sustain Talk in AI-Delivered Motivational Interviewing: A Secondary Analysis of Emergency Department Counseling Sessions (Preprint)**

2026 · JMIR Publications Inc. · posted-content, preprint · https://doi.org/10.2196/preprints.111066

BACKGROUND Large language models can generate motivational interviewing-consistent responses, but their responses to client sustain talk require evaluation before clinical use. OBJECTIVE This formative secondary analysis examined whether sustain-talk themes varied by substance and whether an artificial intelligence counseling agent's response patterns varied by sustain-talk theme. METHODS We coded conversational turns from brief counseling sessions with non-treatment-seeking adult emergency department patients focused on alcohol (n=68), cannabis (n=48), or nicotine (n=32). Participant sustain-talk turns were classified into eight themes. Agent responses were coded as discrepancy-only, validation-only, balanced, or neutral-only. Generalized estimating equation models accounted for responses clustered within sessions. Secondary models examined language in the next participant turn. RESULTS Across 477 responses, 50.7% were discrepancy-only, 11.5% validation-only, 8.2% balanced, and 29.6% neutral-only. Relative to therapeutic-coping sustain talk, low-readiness sustain talk was associated with lower odds of discrepancy-only responding (OR, 0.20; 95% CI, 0.08-0.49) and higher odds of validation-only responding (OR, 11.05; 95% CI, 3.87-31.53). In a secondary multinomial model, validation-only responses were associated with a lower relative risk of next-turn sustain talk versus neutral language (RRR, 0.19; 95% CI, 0.09-0.41). CONCLUSIONS This formative evaluation identified theme-specific response patterns and potential gaps for prospective testing AI counseling agents. These observational findings support prospective testing of theme-matched response strategies before large-scale deployment. CLINICALTRIAL NA

**ИИ:** разошлись — Opus -2 (люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает: Researchers coded the AI counselling agent's responses to sustain talk; no LLM coding is compared with human coding.); Sonnet ? (неясно, сравнивали ли с людьми: AI agent's MI responses and sustain-talk themes were coded, but the abstract doesn't say whether an LLM or humans coded them or whether agreement was reported.)

**Решение:** -

---

### 324 · R11698

**Recognizing Emotion Regulation Strategies from Human Behavior with Large Language Models**

2024 · International Conference on Affective Computing and Intelligent Interaction (ACII) · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/acii63134.2024.00029

Human emotions are often not expressed directly, but regulated according to internal processes and social display rules. For affective computing systems, an understanding of how users regulate their emotions can be highly useful, for example to provide feedback in job interview training, or in psychotherapeutic scenarios. However, at present no method to automatically classify different emotion regulation strategies in a cross-user scenario exists. At the same time, recent studies showed that instruction-tuned Large Language Models (LLMs) can reach impressive performance across a variety of affect recognition tasks such as categorical emotion recognition or sentiment analysis. While these results are promising, it remains unclear to what extent the representational power of LLMs can be utilized in the more subtle task of classifying users' internal emotion regulation strategy. To close this gap, we make use of the recently introduced \textsc{Deep} corpus for modeling the social display of the emotion shame, where each point in time is annotated with one of seven different emotion regulation classes. We fine-tune Llama2-7B as well as the recently introduced Gemma model using Low-rank Optimization on prompts generated from different sources of information on the \textsc{Deep} corpus. These include verbal and nonverbal behavior, person factors, as well as the results of an in-depth interview after the interaction. Our results show, that a fine-tuned Llama2-7B LLM is able to classify the utilized emotion regulation strategy with high accuracy (0.84) without needing access to data from post-interaction interviews. This represents a significant improvement over previous approaches based on Bayesian Networks and highlights the importance of modeling verbal behavior in emotion regulation. Accepted to ACII'24

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Fine-tuned Llama2/Gemma classify emotion regulation strategies in DEEP corpus; unclear whether labels come from human coders or participant interviews; multimodal input.

**Решение:** =

---

### 325 · R11703

**Investigating Lasting Effects of Real-Time Feedback on Originality and Evaluation Accuracy**

2024 · Creativity Research Journal · journalarticle, article · en · https://doi.org/10.1080/10400419.2024.2441014

ABSTRACT Previous research has highlighted the benefits of real-time automated feedback in enhancing originality in divergent thinking tasks. In this preregistered study, we sought to replicate these findings, investigating whether improvements in creative ideation persist after feedback is discontinued, and assess the impact on evaluation accuracy. A total of 230 participants were given three divergent thinking tasks (Alternate Uses tests), with or without semantic distance feedback in the first two trials. The third task was always performed without feedback. Participants were then asked to rate the originality of the ideas they produced in this last trial. Their evaluations were compared against originality scores calculated based on semantic distance and Large Language Models (LLM) for converging evidence. The results aligned with previous findings, showing that feedback was effective in improving overall levels of originality across the first two trials. Importantly, this effect carried over to the third trial after feedback was discontinued. However, feedback did not enhance evaluation accuracy, as participants in both conditions achieved relatively high levels of accuracy in rating the originality of their own ideas. We offer possible explanations for this unexpected result and discuss the study’s findings in the broader context of metacognition.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM originality scores for AUT ideas compared with participants' self-ratings; unclear whether trained human raters also scored the ideas.

**Решение:** =

---

### 326 · R1171

**Hybrid Mental Models and Folk Theories of AI: Spanish Adolescents' Conceptions of Generative AI Functioning**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7560998

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract. The record studies adolescents' mental models of AI; nothing shows whether an LLM coded responses or was compared with human coders.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Title concerns adolescents' mental models of generative AI; no sign of an LLM coding psychological text against human labels. No abstract available.)

**Решение:** -

---

### 327 · R11710

**Fine-Tuning Language Models for Ethical Ambiguity: A Comparative Study of Alignment with Human Responses**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2410.07826

Language models often misinterpret human intentions due to their handling of ambiguity, a limitation well-recognized in NLP research. While morally clear scenarios are more discernible to LLMs, greater difficulty is encountered in morally ambiguous contexts. In this investigation, we explored LLM calibration to show that human and LLM judgments are poorly aligned in such scenarios. We used two curated datasets from the Scruples project for evaluation: DILEMMAS, which involves pairs of distinct moral scenarios to assess the model's ability to compare and contrast ethical situations, and ANECDOTES, which presents individual narratives to evaluate the model's skill in drawing out details, interpreting, and analyzing distinct moral scenarios. Model answer probabilities were extracted for all possible choices and compared with human annotations to benchmark the alignment of three models: Llama-3.1-8b, Zephyr-7b-beta, and Mistral-7b. Significant improvements were observed after fine-tuning, with notable enhancements in both cross-entropy and Dirichlet scores, particularly in the latter. Notably, after fine-tuning, the performance of Mistral-7B-Instruct-v0.3 was on par with GPT-4o. However, the experimental models that were examined were all still outperformed by the BERT and RoBERTa models in terms of cross-entropy scores. Our fine-tuning approach, which improves the model's understanding of text distributions in a text-to-text format, effectively enhances performance and alignment in complex decision-making contexts, underscoring the need for further research to refine ethical reasoning techniques and capture human judgment nuances. Accepted to NeurIPS 2024, SoLaR workshop

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs' moral judgments of Scruples narratives compared with crowd annotation distributions; unclear whether moral judgment counts as a psychological construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Moral judgment alignment on Scruples ethical dilemmas; not a psychological or clinical construct coded in text, mainly distribution calibration.)

**Решение:** -

---

### 328 · R11714

**Comparing the Efficacy and Efficiency of Human and Generative AI: Qualitative Thematic Analyses.**

2024 · JMIR AI · journal article, journalarticle, article · eng · https://doi.org/10.2196/54482

BACKGROUND: Qualitative methods are incredibly beneficial to the dissemination and implementation of new digital health interventions; however, these methods can be time intensive and slow down dissemination when timely knowledge from the data sources is needed in ever-changing health systems. Recent advancements in generative artificial intelligence (GenAI) and their underlying large language models (LLMs) may provide a promising opportunity to expedite the qualitative analysis of textual data, but their efficacy and reliability remain unknown. OBJECTIVE: The primary objectives of our study were to evaluate the consistency in themes, reliability of coding, and time needed for inductive and deductive thematic analyses between GenAI (ie, ChatGPT and Bard) and human coders. METHODS: The qualitative data for this study consisted of 40 brief SMS text message reminder prompts used in a digital health intervention for promoting antiretroviral medication adherence among people with HIV who use methamphetamine. Inductive and deductive thematic analyses of these SMS text messages were conducted by 2 independent teams of human coders. An independent human analyst conducted analyses following both approaches using ChatGPT and Bard. The consistency in themes (or the extent to which the themes were the same) and reliability (or agreement in coding of themes) between methods were compared. RESULTS: The themes generated by GenAI (both ChatGPT and Bard) were consistent with 71% (5/7) of the themes identified by human analysts following inductive thematic analysis. The consistency in themes was lower between humans and GenAI following a deductive thematic analysis procedure (ChatGPT: 6/12, 50%; Bard: 7/12, 58%). The percentage agreement (or intercoder reliability) for these congruent themes between human coders and GenAI ranged from fair to moderate (ChatGPT, inductive: 31/66, 47%; ChatGPT, deductive: 22/59, 37%; Bard, inductive: 20/54, 37%; Bard, deductive: 21/58, 36%). In general, ChatGPT and Bard performed similarly to each other across both types of qualitative analyses in terms of consistency of themes (inductive: 6/6, 100%; deductive: 5/6, 83%) and reliability of coding (inductive: 23/62, 37%; deductive: 22/47, 47%). On average, GenAI required significantly less overall time than human coders when conducting qualitative analysis (20, SD 3.5 min vs 567, SD 106.5 min). CONCLUSIONS: The promising consistency in the themes generated by human coders and GenAI suggests that these technologies hold promise in reducing the resource intensiveness of qualitative thematic analysis; however, the relatively lower reliability in coding between them suggests that hybrid approaches are necessary. Human coders appeared to be better than GenAI at identifying nuanced and interpretative themes. Future studies should consider how these powerful technologies can be best used in collaboration with human coders to improve the efficiency of qualitative research in hybrid approaches while also mitigating potential ethical risks that they may pose.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT/Bard and human coders coded the same SMS adherence messages and report percentage agreement; unclear whether the themes are psychological constructs.

**Решение:** =

---

### 329 · R11719

**Assessing dimensions of thought disorder with large language models: The tradeoff of accuracy and consistency.**

2024 · Psychiatry research · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.psychres.2024.116119

Natural Language Processing (NLP) methods have shown promise for the assessment of formal thought disorder, a hallmark feature of schizophrenia in which disturbances to the structure, organization, or coherence of thought can manifest as disordered or incoherent speech. We investigated the suitability of modern Large Language Models (LLMs - e.g., GPT-3.5, GPT-4, and Llama 3) to predict expert-generated ratings for three dimensions of thought disorder (coherence, content, and tangentiality) assigned to speech samples collected from both patients with a diagnosis of schizophrenia (n = 26) and healthy control participants (n = 25). In addition to (1) evaluating the accuracy of LLM-generated ratings relative to human experts, we also (2) investigated the degree to which the LLMs produced consistent ratings across multiple trials, and we (3) sought to understand the factors that impacted the consistency of LLM-generated output. We found that machine-generated ratings of the level of thought disorder in speech matched favorably those of expert humans, and we identified a tradeoff between accuracy and consistency in LLM ratings. Unlike traditional NLP methods, LLMs were not always consistent in their predictions, but these inconsistencies could be mitigated with careful parameter selection and ensemble methods. We discuss implications for NLP-based assessment of thought disorder and provide recommendations of best practices for integrating these methods in the field of psychiatry.

**ИИ:** + · обе модели · клиническая оценка · GPT-3.5/4 and Llama 3 rated thought-disorder dimensions in speech samples and were compared with expert human ratings.

**Решение:** =

---

### 330 · R11737

**DepressionEmo: A novel dataset for multilabel classification of depression emotions.**

2024 · Journal of affective disorders · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.jad.2024.08.013

Emotions are integral to human social interactions, with diverse responses elicited by various situational contexts. Particularly, the prevalence of negative emotional states has been correlated with negative outcomes for mental health, necessitating a comprehensive analysis of their occurrence and impact on individuals. In this paper, we introduce a novel dataset named DepressionEmo designed to detect 8 emotions associated with depression by 6037 examples of long Reddit user posts. This dataset was created through a majority vote over inputs by zero-shot classifications from pre-trained models and validating the quality by annotators and ChatGPT, exhibiting an acceptable level of interrater reliability between annotators. The correlation between emotions, their distribution over time, and linguistic analysis are conducted on DepressionEmo. Besides, we provide several text classification methods classified into two groups: machine learning methods such as SVM, XGBoost, and Light GBM; and deep learning methods such as BERT, GAN-BERT, and BART. The pretrained BART model, bart-base allows us to obtain the highest F1- Macro of 0.76, showing its outperformance compared to other methods evaluated in our analysis. Across all emotions, the highest F1-Macro value is achieved by suicide intent, indicating a certain value of our dataset in identifying emotions in individuals with depression symptoms through text analysis. The curated dataset is publicly available at: https://github.com/abuBakarSiddiqurRahman/DepressionEmo. 18 pages

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · ChatGPT and human annotators both validated depression-emotion labels on Reddit posts; unclear whether ChatGPT–human agreement is reported.

**Решение:** =

---

### 331 · R11743

**LLM-Human Pipeline for Cultural Context Grounding of Conversations**

2024 · arXiv (Cornell University) · journalarticle, conference, preprint/article · en · https://doi.org/10.48550/arxiv.2410.13727

Conversations often adhere to well-understood social norms that vary across cultures. For example, while "addressing parents by name" is commonplace in the West, it is rare in most Asian cultures. Adherence or violation of such norms often dictates the tenor of conversations. Humans are able to navigate social situations requiring cultural awareness quite adeptly. However, it is a hard task for NLP models. In this paper, we tackle this problem by introducing a "Cultural Context Schema" for conversations. It comprises (1) conversational information such as emotions, dialogue acts, etc., and (2) cultural information such as social norms, violations, etc. We generate ~110k social norm and violation descriptions for ~23k conversations from Chinese culture using LLMs. We refine them using automated verification strategies which are evaluated against culturally aware human judgements. We organize these descriptions into meaningful structures we call "Norm Concepts", using an interactive human-in-loop framework. We ground the norm concepts and the descriptions in conversations using symbolic annotation. Finally, we use the obtained dataset for downstream tasks such as emotion, sentiment, and dialogue act detection. We show that it significantly improves the empirical performance. Oral at NAACL 2025 Main conference. Albuquerque, USA. Apr 29 - May 4, 2025. 19 pages, 9 figures, 7 tables

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM verification of social norm/violation descriptions is checked against human judgements; unclear whether social norms count as a psychological construct.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLMs generate social norm descriptions for dialogues; verification vs human judgements concerns generated text, not LLM coding of psychological constructs against human labels.)

**Решение:** -

---

### 332 · R11748

**GPT is an effective tool for multilingual psychological text analysis.**

2024 · Proceedings of the National Academy of Sciences of the United States of America · journal article, research support, n.i.h., extramural, research support, non-u.s. gov't · eng · https://doi.org/10.1073/pnas.2308950121

The social and behavioral sciences have been increasingly using automated text analysis to measure psychological constructs in text. We explore whether GPT, the large-language model (LLM) underlying the AI chatbot ChatGPT, can be used as a tool for automated psychological text analysis in several languages. Across 15 datasets ( n = 47,925 manually annotated tweets and news headlines), we tested whether different versions of GPT (3.5 Turbo, 4, and 4 Turbo) can accurately detect psychological constructs (sentiment, discrete emotions, offensiveness, and moral foundations) across 12 languages. We found that GPT ( r = 0.59 to 0.77) performed much better than English-language dictionary analysis ( r = 0.20 to 0.30) at detecting psychological constructs as judged by manual annotators. GPT performed nearly as well as, and sometimes better than, several top-performing fine-tuned machine learning models. Moreover, GPT's performance improved across successive versions of the model, particularly for lesser-spoken languages, and became less expensive. Overall, GPT may be superior to many existing methods of automated text analysis, since it achieves relatively high accuracy across many languages, requires no training data, and is easy to use with simple prompts (e.g., "is this text negative?") and little coding experience. We provide sample code and a video tutorial for analyzing text with the GPT application programming interface. We argue that GPT and other LLMs help democratize automated text analysis by making advanced natural language processing capabilities more accessible, and may help facilitate more cross-linguistic research with understudied languages.

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT detected discrete emotions, sentiment and moral foundations in tweets and headlines; results compared with manual annotations across 15 datasets.

**Решение:** =

---

### 333 · R1175

**Jeffrey Epstein: anàlisi del discurs de l'autorepresentació i les relacions de poder en els seus correus electrònics (2008-2011)**

2026 · RiuNet (Universitat Politècnica de València) · dissertation · en · https://riunet.upv.es/handle/10251/241962

[EN] This dissertation is situated within the field of Digital Humanities and explores the intersection of Critical Discourse Analysis (CDA), corpus linguistics, and artificial intelligence. It focuses on the use of generative AI to extend CDA from a small, manually analyzed sample to a larger corpus. The study examines emails written by Jeffrey Epstein between 2008 and 2011. Taking into consideration the language of power and the size of the corpus, it presents as an opportunity for both qualitative and quantitative research. The emails are approached from two main perspectives: self-representation and relations of power. These are analyzed through four complementary frameworks: Fairclough’s three-dimensional model, Davies and Harré’s positioning theory, van Leeuwen’s model of legitimation, and van Dijk’s approach to manipulation and social power. Nine emails are first analyzed in detail to develop a codebook, which is then used to guide LLM annotation across larger samples. The main question is whether CDA categories developed through close reading can be applied at a larger scale with the help of an LLM, considering possibilities and limitations during this process. By bringing qualitative and quantitative methods together, the dissertation explores how generative AI can support the expansion of CDA-based analysis while keeping human interpretation at its center.

**ИИ:** ? · обе модели · неясен конструкт · LLM applies CDA codebook (positioning, power, manipulation) to emails; psychological construct borderline, human comparison not explicitly reported.

**Решение:** =

---

### 334 · R11752

**Automated Scoring of Open-Ended Question Complexity: A Large Language Model Approach**

2024 · Research Square · preprint, ppr, posted-content · en · https://doi.org/10.21203/rs.3.rs-3890828/v1

Abstract Question-asking, an essential yet often understudied activity, holds significant implications for learning, creativity, and cognitive development. In particular, the quality and complexity of the questions asked are crucial factors affecting these fields. Previous research has explored open-ended question complexity through frameworks like the Bloom taxonomy of cognitive objectives, but the measurement of complexity remains challenging. Recent advancements in natural language processing have enabled automated scoring of psychological tasks, notably predicting human ratings of creativity. Although some methods have been applied to measure question complexity, there has been scarce research so far on the automatic assessment of open-ended questions. Here, we address this gap by employing a Large Language Model (LLM) to accurately predict human ratings of open-ended question complexity based on the Bloom taxonomy and comparing these predictions to existing baseline measures such as semantic distance and word count. Specifically, this study capitalized on previously collected human-rated responses from a creative question-asking task to train an LLM for scoring questions based on the Bloom taxonomy of complexity. Our results reveal that our LLM-generated Bloom scores correlated strongly with human ratings of complexity ( r = .73), whilst also greatly exceeding tested baseline measures. Our study emphasizes the significance of LLM in automating the assessment of open-ended question complexity, fostering cost-effective, automatic, and reliable measurements in this domain. Our study further highlights the exciting possibilities for the continued usage of LLM in education and psychology and their potential in helping study how we ask creative questions.

**ИИ:** + · обе модели · подсчёт методики · Fine-tuned LLM scores creative question-asking task complexity (Bloom), correlated with human ratings r=.73; verify model is decoder.

**Решение:** =

---

### 335 · R11760

**From Lexicons to Large Language Models: A Holistic Evaluation of Psychometric Text Analysis in Social Science Research**

2024 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.4776480

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title points to an evaluation of LLM psychometric text analysis that may include comparison with human-coded labels.

**Решение:** =

---

### 336 · R11778

**Automated Assessment of Encouragement and Warmth in Classrooms Leveraging Multimodal Emotional Features and ChatGPT**

2024 · International Conference on Artificial Intelligence in Education · journalarticle, conference, text/article · en · https://doi.org/10.1007/978-3-031-64302-6_5

Classroom observation protocols standardize the assessment of teaching effectiveness and facilitate comprehension of classroom interactions. Whereas these protocols offer teachers specific feedback on their teaching practices, the manual coding by human raters is resource-intensive and often unreliable. This has sparked interest in developing AI-driven, cost-effective methods for automating such holistic coding. Our work explores a multimodal approach to automatically estimating encouragement and warmth in classrooms, a key component of the Global Teaching Insights (GTI) study\u27s observation protocol. To this end, we employed facial and speech emotion recognition with sentiment analysis to extract interpretable features from video, audio, and transcript data. The prediction task involved both classification and regression methods. Additionally, in light of recent large language models\u27 remarkable text annotation capabilities, we evaluated ChatGPT\u27s zero-shot performance on this scoring task based on transcripts. We demonstrated our approach on the GTI dataset, comprising 367 16-minute video segments from 92 authentic lesson recordings. The inferences of GPT-4 and the best-trained model yielded correlations of r = .341 and r = .441 with human ratings, respectively. Combining estimates from both models through averaging, an ensemble approach achieved a correlation of r = .513, comparable to human inter-rater reliability. Our model explanation analysis indicated that text sentiment features were the primary contributors to the trained model\u27s decisions. Moreover, GPT-4 could deliver logical and concrete reasoning as potential teacher guidelines. Our findings provide insights into using advanced, multimodal techniques for automated classroom observation, aiming to foster teacher training through frequent and valuable feedback.Accepted as a full paper by the 25th International Conference on Artificial Intelligence in Education (AIED 2024

**ИИ:** разошлись — Opus + (кодирование по кодбуку: GPT-4 zero-shot rated classroom encouragement/warmth (interpersonal construct) from transcripts; correlated with human observation-protocol ratings.); Sonnet ? (неясен конструкт: GPT-4 zero-shot scored classroom transcripts for teacher encouragement/warmth against human ratings (r=.341); construct is educational-interpersonal, so psychological scope is borderline.)

**Решение:** ?

---

### 337 · R11798

**Can AI Relate: Testing Large Language Model Response for Mental Health Support**

2024 · Conference on Empirical Methods in Natural Language Processing · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48550/arxiv.2405.12021

Large language models (LLMs) are already being piloted for clinical use in hospital systems like NYU Langone, Dana-Farber and the NHS. A proposed deployment use case is psychotherapy, where a LLM-powered chatbot can treat a patient undergoing a mental health crisis. Deployment of LLMs for mental health response could hypothetically broaden access to psychotherapy and provide new possibilities for personalizing care. However, recent high-profile failures, like damaging dieting advice offered by the Tessa chatbot to patients with eating disorders, have led to doubt about their reliability in high-stakes and safety-critical settings. In this work, we develop an evaluation framework for determining whether LLM response is a viable and ethical path forward for the automation of mental health treatment. Our framework measures equity in empathy and adherence of LLM responses to motivational interviewing theory. Using human evaluation with trained clinicians and automatic quality-of-care metrics grounded in psychology research, we compare the responses provided by peer-to-peer responders to those provided by a state-of-the-art LLM. We show that LLMs like GPT-4 use implicit and explicit cues to infer patient demographics like race. We then show that there are statistically significant discrepancies between patient subgroups: Responses to Black posters consistently have lower empathy than for any other demographic group (2%-13% lower than the control group). Promisingly, we do find that the manner in which responses are generated significantly impacts the quality of the response. We conclude by proposing safety guidelines for the potential deployment of LLMs for mental health response. EMNLP 2024 Findings

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Clinicians rate empathy/MI adherence of responses; the automatic metrics may be encoder-based, and it is unclear whether an LLM rated the same responses.

**Решение:** =

---

### 338 · R11812

**Using Instruction-Tuned Large Language Models to Identify Indicators of Vulnerability in Police Incident Narratives**

2024 · CrimRxiv · preprint · en · https://doi.org/10.21428/cb6ab371.72ff8f2e

Objectives: Compare qualitative coding of instruction tuned large language models (IT-LLMs) against human coders in classifying the presence or absence of vulnerability in routinely collected unstructured text that describes police-public interactions. Evaluate potential bias in IT-LLM codings. Methods: Analyzing publicly available text narratives of police-public interactions recorded by Boston Police Department, we provide humans and IT-LLMs with qualitative labelling codebooks and compare labels generated by both, seeking to identify situations associated with (i) mental ill health; (ii) substance misuse; (iii) alcohol dependence; and (iv) homelessness. We explore multiple prompting strategies and model sizes, and the variability of labels generated by repeated prompts. Additionally, to explore model bias, we utilize counterfactual methods to assess the impact of two protected characteristics - race and gender - on IT-LLM classification. Results: Results demonstrate that IT-LLMs can effectively support human qualitative coding of police incident narratives. While there is some disagreement between LLM and human generated labels, IT-LLMs are highly effective at screening narratives where no vulnerabilities are present, potentially vastly reducing the requirement for human coding. Counterfactual analyses demonstrate that manipulations to both gender and race of individuals described in narratives have very limited effects on IT-LLM classifications beyond those expected by chance. Conclusions: IT-LLMs offer effective means to augment human qualitative coding in a way that requires much lower levels of resource to analyze large unstructured datasets. Moreover, they encourage specificity in qualitative coding, promote transparency, and provide the opportunity for more standardized, replicable approaches to analyzing large free-text police data sources.

**ИИ:** + · обе модели · кодирование по кодбуку · Instruction-tuned LLMs and human coders applied the same codebook to police narratives to code mental ill health, substance misuse and related vulnerabilities, and their labels were compared.

**Решение:** =

---

### 339 · R11821

**Suicide Ideation and Risk Detection from Social Media Using GPT Models**

2024 · Journal of Computer Science · journalarticle, article · en · https://doi.org/10.3844/jcssp.2024.1349.1356

: As a reason for the sensitiveness of suicide ideation and its considerable impact on people's lives, the demand to treat and prevent the suicide ideation issue has become an obligation. Suicide ideation is a result of a combination of psychological pain and hopelessness. According to the World Health Organization, the task of reducing the global suicide mortality rate is a target, that should be attained. The entire population uses social media platforms to express their feelings, emotions, sentiments, and opinions. Social media platforms are among the most popular sources of datasets related to mental health issues. The process of detecting suicide ideation from social media platforms is based on recent methods of artificial intelligence such as machine learning and deep learning. In this study, we propose fine-tuning large language models to evaluate and find the level of suicide risk in posts published on Reddit. We fine-tuned four GPT-3 models using the UMD Reddit suicidality dataset, which is related to the subreddit of suicidal ideation. Our experimental results illustrate the efficiency of the LLMs in addressing our task. The model attains a high F1-score of 92.3%, an accuracy of 94.8%, and a training loss of 0.050

**ИИ:** + · обе модели · бенчмарк с метками людей · Fine-tuned GPT-3 models rate suicide risk levels in Reddit posts, evaluated against the UMD dataset, whose risk labels come from human annotators.

**Решение:** =

---

### 340 · R11827

**RACER: An LLM-powered Methodology for Scalable Analysis of Semi-structured Mental Health Interviews**

2024 · NLP4SCIENCE · audiovisual/conference talk, journalarticle, preprint/article · en · https://doi.org/10.18653/v1/2024.nlp4science-1.8

Semi-structured interviews (SSIs) are a commonly employed data-collection method in healthcare research, offering in-depth qualitative insights into subject experiences. Despite their value, the manual analysis of SSIs is notoriously time-consuming and labor-intensive, in part due to the difficulty of extracting and categorizing emotional responses, and challenges in scaling human evaluation for large populations. In this study, we develop RACER, a Large Language Model (LLM) based expert-guided automated pipeline that efficiently converts raw interview transcripts into insightful domain-relevant themes and sub-themes. We used RACER to analyze SSIs conducted with 93 healthcare professionals and trainees to assess the broad personal and professional mental health impacts of the COVID-19 crisis. RACER achieves moderately high agreement with two human evaluators (72%), which approaches the human inter-rater agreement (77%). Interestingly, LLMs and humans struggle with similar content involving nuanced emotional, ambivalent/dialectical, and psychological statements. Our study highlights the opportunities and challenges in using LLMs to improve research efficiency and opens new avenues for scalable analysis of SSIs in healthcare research.

**ИИ:** + · обе модели · кодирование по кодбуку · LLM pipeline categorizes interview responses about mental health impacts into themes; agreement with two human evaluators (72%) vs human IRR (77%).

**Решение:** =

---

### 341 · R1183

**An AI-powered research assistant in the lab: A practical guide for text analysis through iterative collaboration with LLMs.**

2026 · Behavior research methods · journal article, journalarticle, review · eng · https://doi.org/10.3758/s13428-026-02966-6

Analyzing texts such as open-ended responses, headlines, or social media posts is a time- and labor-intensive process highly susceptible to bias. However, large language models (LLMs) are promising tools for text analysis, using either a predefined (top-down) or a data-driven (bottom-up) taxonomy, without sacrificing quality. Here, we present a step-by-step tutorial to efficiently develop, test, and apply taxonomies for analyzing unstructured data through an iterative and collaborative process between researchers and an LLM. Using personal goals provided by participants as an example, we demonstrate how we used this method to write prompts to review datasets and generate a taxonomy of life domains, evaluate and refine the taxonomy through prompt and direct modifications, and apply the taxonomy to categorize an entire dataset with high intercoder reliability, while achieving high levels of human-LLM intercoder agreement, reducing analysis time by approximately 87.5%. This test offers a proof of concept, suggesting that with the right procedures LLMs can be used to generate reliable bottom-up categorizations. We discuss the possibilities and limitations of using LLMs for text analysis.

**ИИ:** + · обе модели · кодирование по кодбуку · An LLM sorted participants' personal goals into life-domain categories, and the abstract reports human–LLM intercoder agreement on that coding.

**Решение:** =

---

### 342 · R11834

**ERD: A Framework for Improving LLM Reasoning for Cognitive Distortion Classification**

2024 · Clinical Natural Language Processing Workshop (ClinicalNLP) · audiovisual/conference talk, journalarticle, preprint/article · en · https://doi.org/10.18653/v1/2024.clinicalnlp-1.25

Improving the accessibility of psychotherapy with the aid of Large Language Models (LLMs) is garnering a significant attention in recent years. Recognizing cognitive distortions from the interviewee’s utterances can be an essential part of psychotherapy, especially for cognitive behavioral therapy. In this paper, we propose ERD, which improves LLM-based cognitive distortion classification performance with the aid of additional modules of (1) extracting the parts related to cognitive distortion, and (2) debating the reasoning steps by multiple agents. Our experimental results on a public dataset show that ERD improves the multi-class F1 score as well as binary specificity score. Regarding the latter score, it turns out that our method is effective in debiasing the baseline method which has high false positive rate, especially when the summary of multi-agent debate is provided to LLMs.

**ИИ:** + · обе модели · бенчмарк с метками людей · LLM multi-agent pipeline classifies cognitive distortions in utterances; F1 reported against a public dataset that is probably human-annotated.

**Решение:** =

---

### 343 · R11842

**Psychological Assessments with Large Language Models: A Privacy-Focused and Cost-Effective Approach**

2024 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, journalarticle, preprint/article · en · https://doi.org/10.18653/v1/2024.clpsych-1.18

This study explores the use of Large Language Models (LLMs) to analyze text comments from Reddit users, aiming to achieve two primary objectives: firstly, to pinpoint critical excerpts that support a predefined psychological assessment of suicidal risk; and secondly, to summarize the material to substantiate the preassigned suicidal risk level. The work is circumscribed to the use of "open-source" LLMs that can be run locally, thereby enhancing data privacy. Furthermore, it prioritizes models with low computational requirements, making it accessible to both individuals and institutions operating on limited computing budgets. The implemented strategy only relies on a carefully crafted prompt and a grammar to guide the LLM's text completion. Despite its simplicity, the evaluation metrics show outstanding results, making it a valuable privacy-focused and cost-effective approach. This work is part of the Computational Linguistics and Clinical Psychology (CLPsych) 2024 shared task. Accepted to the Workshop on Computational Linguistics and Clinical Psychology (CLPsych) at EACL 2024

**ИИ:** ? · обе модели · другое · Open-source LLMs extract evidence spans for preassigned suicide risk in Reddit posts; shared-task evaluation against expert highlights may give an agreement measure.

**Решение:** =

---

### 344 · R11846

**WellDunn: On the Robustness and Explainability of Language Models and Large Language Models in Identifying Wellness Dimensions**

2024 · BlackboxNLP Workshop on Analyzing and Interpreting Neural Networks for NLP · journalarticle, text/article, text/text · en · https://doi.org/10.18653/v1/2024.blackboxnlp-1.23

Language Models (LMs) are being proposed for mental health applications where the heightened risk of adverse outcomes means predictive performance may not be a sufficient litmus test of a model's utility in clinical practice. A model that can be trusted for practice should have a correspondence between explanation and clinical determination, yet no prior research has examined the attention fidelity of these models and their effect on ground truth explanations. We introduce an evaluation design that focuses on the robustness and explainability of LMs in identifying Wellness Dimensions (WDs). We focus on two existing mental health and well-being datasets: (a) Multi-label Classification-based MultiWD, and (b) WellXplain for evaluating attention mechanism veracity against expert-labeled explanations. The labels are based on Halbert Dunn's theory of wellness, which gives grounding to our evaluation. We reveal four surprising results about LMs/LLMs: (1) Despite their human-like capabilities, GPT-3.5/4 lag behind RoBERTa, and MedAlpaca, a fine-tuned LLM on WellXplain fails to deliver any remarkable improvements in performance or explanations. (2) Re-examining LMs' predictions based on a confidence-oriented loss function reveals a significant performance drop. (3) Across all LMs/LLMs, the alignment between attention and explanations remains low, with LLMs scoring a dismal 0.0. (4) Most mental health-specific LMs/LLMs overlook domain-specific knowledge and undervalue explanations, causing these discrepancies. This study highlights the need for further research into their consistency and explanations in mental health and well-being. Accepted in BlackboxNLP @ EMNLP 2024

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT-3.5/4 and MedAlpaca classify wellness dimensions in mental-health text against expert-labeled datasets (MultiWD, WellXplain).

**Решение:** =

---

### 345 · R11856

**Generative AI for Thematic Analysis in a Maternal Health Study: Coding Semi-structured Interviews using Large Language Models (LLMs)**

2024 · medRxiv · journalarticle, review · https://doi.org/10.1101/2024.09.16.24313707

Study Objectives: In-depth interviews are one of the most widely used approaches for qualitative studies in public health. The coding of transcripts is a critical step for information extraction and preliminary analysis. However, manual coding is often labor-intensive and time-consuming. The emergence of generative artificial intelligence (GenAI), supported by Large Language Models (LLMs), presents new opportunities to understand human languages, which may significantly facilitate the coding process. This study aims to build a computational coding framework that uses GenAI to automatically detect and extract themes from in-depth interview transcripts. Methods: We conducted an experiment using transcripts of in-depth interviews with maternity care providers in South Carolina. We leveraged ChatGPT to perform two tasks automatically: (1) deductive coding, which involves applying a predefined set of codes to dialogues; and (2) inductive coding, which can generate codes from dialogues without any preconceptions or assumptions. We fine-tuned ChatGPT to understand the content of the interview transcripts, enabling it to detect and summarize codes. We then evaluated the performance of the proposed approach by comparing the codes generated by ChatGPT with those generated manually by human coders, involving human-in-the-loop evaluation. Results: The results demonstrated the potential of GenAI in detecting and summarizing codes from in-depth interview transcripts. ChatGPT could be utilized for both deductive and inductive coding processes. The overall accuracy of GenAI is higher than 80% and the codes it generated showed high positive associations with those generated manually. More impressively, GenAI reduced the time required for coding by 81%, demonstrating its efficiency compared to traditional methods. Discussion: GenAI models like ChatGPT show high generalizability, scalability and efficiency in handling large datasets, and are proficient in multi-level semantic structure identification. They demonstrate promising results in qualitative coding, making it a valuable tool for supporting people in public health research. However, challenges such as inaccuracy, systematic biases, and privacy concerns must be addressed when using them in practice. GenAI-based coding results should be handled with caution and reviewed by human coders to ensure accuracy and reliability.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT did deductive coding of provider interviews and was compared with human coders; unclear whether the codes are psychological or about health services.

**Решение:** =

---

### 346 · R11865

**Detecting the Severity of Depression in Online Forum Data by Leveraging Implicit Semantic Inferences**

2024 · International Journal on Advances in ICT for Emerging Regions (ICTer) · journalarticle, article · en · https://doi.org/10.4038/icter.v17i2.7280

Depression, a prevalent mental health disorder with global implications, exerts a profound negative influence on individuals’ lives. While the prediction of depression (as a binary classification task) is a well-established research area, depression severity detection is a new research direction with limited studies. In the context of detecting the severity of depression through online forum data, this research endeavors to offer two distinct solutions by employing Ada embeddings, GPT 3.5 Turbo, and LIWC as feature engineering techniques, while AutoSklearn serves as the ensemble learning algorithm. Notably, the outcomes of this study significantly outperform existing state-of-the-art models on both depression severity annotated datasets used in this research. The results also showcase the potential reuse nature of the proposed models in diverse data sources due to their high performance in both datasets. Furthermore, as a valuable practical outcome, a software prototype has been developed, capable of providing the depression severity level, along with associated symptoms and keywords, upon inputting an online forum post.

**ИИ:** ? · обе модели · другое · GPT-3.5 provides features for an AutoSklearn severity classifier tested on human-annotated depression datasets; unclear whether the LLM itself rates.

**Решение:** =

---

### 347 · R11866

**Empaths at WASSA 2024 Empathy and Personality Shared Task: Turn-Level Empathy Prediction Using Psychological Indicators**

2024 · Workshop on Computational Approaches to Subjectivity, Sentiment & Social Media Analysis (WASSA) · audiovisual/conference talk, journalarticle, conference-paper · en · https://doi.org/10.18653/v1/2024.wassa-1.35

For the WASSA 2024 Empathy and Personality Prediction Shared Task, we propose a novel turn-level empathy detection method that decomposes empathy into six psychological indicators: Emotional Language, Perspective-Taking, Sympathy and Compassion, Extroversion, Openness, and Agreeableness. A pipeline of text enrichment using a Large Language Model (LLM) followed by DeBERTA fine-tuning demonstrates a significant improvement in the Pearson Correlation Coefficient and F1 scores for empathy detection, highlighting the effectiveness of our approach. Our system officially ranked 7th at the CONV-turn track.

**ИИ:** разошлись — Opus ? (другое: Empathy is predicted against human-annotated turn labels, but a DeBERTa encoder makes the prediction and the LLM only enriches the text.); Sonnet -5 (нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM: Empathy prediction is done by a fine-tuned DeBERTa encoder; the LLM only enriches text, so no LLM–human coding agreement is assessed.)

**Решение:** -

---

### 348 · R11867

**Turn-Level Empathy Prediction Using Psychological Indicators**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2407.08607

For the WASSA 2024 Empathy and Personality Prediction Shared Task, we propose a novel turn-level empathy detection method that decomposes empathy into six psychological indicators: Emotional Language, Perspective-Taking, Sympathy and Compassion, Extroversion, Openness, and Agreeableness. A pipeline of text enrichment using a Large Language Model (LLM) followed by DeBERTA fine-tuning demonstrates a significant improvement in the Pearson Correlation Coefficient and F1 scores for empathy detection, highlighting the effectiveness of our approach. Our system officially ranked 7th at the CONV-turn track.

**ИИ:** ? · обе модели · другое · Human-annotated turn-level empathy, but the final predictor is DeBERTa; the LLM only enriches text. Unclear whether LLM ratings are compared with humans.

**Решение:** =

---

### 349 · R1187

**Can ChatGPT Perform Qualitative Research and Conduct Thematic Analysis in Transplantation?**

2026 · American Journal of Transplantation · article · en · https://doi.org/10.1016/j.ajt.2026.05.983

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. ChatGPT thematic analysis of transplant qualitative data might be compared with human coding, or only at theme level.

**Решение:** =

---

### 350 · R11876

**Integrating Previous Suicide Attempts, Gender, and Age Into Suicide Risk Assessment Using Advanced Artificial Intelligence Models.**

2024 · The Journal of clinical psychiatry · journal article, med, journalarticle · eng · https://doi.org/10.4088/jcp.24m15365

Objective: Suicide is a critical global health concern. Research indicates that generative artificial intelligence (GenAI) and large language models, such as generative pretrained transformer-3 (GPT-3) and GPT-4, can evaluate suicide risk comparably to experts, yet the criteria these models use are unclear. This study explores how variations in prompts, specifically regarding past suicide attempts, gender, and age, influence the risk assessments provided by ChatGPT-3 and ChatGPT-4. Methods: Using a controlled scenario based approach, 8 vignettes were created. Both ChatGPT-3.5 and ChatGPT 4 were used to predict the likelihood of serious suicide attempts, suicide attempts, and suicidal thoughts. A univariate 3-way analysis of variance was conducted to analyze the effects of the independent variables (previous suicide attempts, gender, and age) on the dependent variables (likelihood of serious suicide attempts, suicide attempts, and suicidal thoughts). Results: Both ChatGPT-3.5 and ChatGPT-4 recognized the importance of previous suicide attempts in predicting severe suicide risks and suicidal thoughts. ChatGPT-4 also identified gender differences, associating men with a higher risk, while both models disregarded age as a risk factor. Interaction analysis revealed that ChatGPT-3.5 associated past attempts with a higher likelihood of suicidal thoughts in men, whereas ChatGPT-4 showed an increased risk for women. Conclusions: The study highlights ChatGPT-3.5 and ChatGPT-4's potential in suicide risk evaluation, emphasizing the importance of prior attempts and gender, while noting differences in their handling of interactive effects and the negligible role of age. These findings reflect the complexity of GenAI decision-making. While promising for suicide risk assessment, these models require careful application due to limitations and real-world complexities.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: ChatGPT rates suicide risk in vignettes using a factorial design; the abstract mentions no human ratings, though related studies compared models with professionals.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): ChatGPT predicts suicide risk on manipulated vignettes analyzed by ANOVA; no human coding of the same texts for LLM–human agreement.)

**Решение:** -

---

### 351 · R11880

**Comprehensive Scientific Creativity Assessment (C-SCA): A New Approach for Measuring Scientific Creativity in Secondary School Students**

2024 · International Journal of Science and Mathematics Education · journalarticle, article · en · https://doi.org/10.1007/s10763-024-10469-z

Abstract This study introduces a Comprehensive Scientific Creativity Assessment (C-SCA) instrument and empirically tests its reliability and validity. While existing instruments to measure scientific creativity generally focus on a single dimension, such as divergent thinking, the C-SCA incorporates scientific knowledge, motivation in scientific creativity and thinking styles within its assessment framework. In this study, the three dimensions of C-SCA were measured using modifications of existing instruments. We provide two versions of the test, to allow tests of the effectiveness of educational interventions on scientific creativity. We incorporated ChatGPT into the scientific creativity scoring process to enhance the objectivity of the scores. Looking ahead, technological advancements hold promise for further improvements in scientific creativity assessment.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · ChatGPT scored open-ended scientific creativity/divergent thinking responses; the abstract doesn't say whether it was compared with human scorers.

**Решение:** =

---

### 352 · R11889

**Affect Recognition in Conversations Using Large Language Models**

2024 · Annual Meeting of the Special Interest Group on Discourse and Dialogue · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.18653/v1/2024.sigdial-1.23

Affect recognition, encompassing emotions, moods, and feelings, plays a pivotal role in human communication. In the realm of conversational artificial intelligence, the ability to discern and respond to human affective cues is a critical factor for creating engaging and empathetic interactions. This study investigates the capacity of large language models (LLMs) to recognise human affect in conversations, with a focus on both open-domain chit-chat dialogues and task-oriented dialogues. Leveraging three diverse datasets, namely IEMOCAP (Busso et al., 2008), EmoWOZ (Feng et al., 2022), and DAIC-WOZ (Gratch et al., 2014), covering a spectrum of dialogues from casual conversations to clinical interviews, we evaluate and compare LLMs' performance in affect recognition. Our investigation explores the zero-shot and few-shot capabilities of LLMs through in-context learning as well as their model capacities through task-specific fine-tuning. Additionally, this study takes into account the potential impact of automatic speech recognition errors on LLM predictions. With this work, we aim to shed light on the extent to which LLMs can replicate human-like affect recognition capabilities in conversations. Accepted by SIGDIAL 2024

**ИИ:** + · обе модели · бенчмарк с метками людей · LLMs recognise emotions in IEMOCAP and EmoWOZ dialogues, both labelled by human annotators; DAIC-WOZ depression labels come from self-report.

**Решение:** =

---

### 353 · R11890

**Automating PTSD Diagnostics in Clinical Interviews: Leveraging Large Language Models for Trauma Assessments**

2024 · Annual Meeting of the Special Interest Group on Discourse and Dialogue · journalarticle, text/article, conference-paper · en · https://doi.org/10.18653/v1/2024.sigdial-1.55

The shortage of clinical workforce presents significant challenges in mental healthcare, limiting access to formal diagnostics and services. We aim to tackle this shortage by integrating a customized large language model (LLM) into the workflow, thus promoting equity in mental healthcare for the general population. Although LLMs have showcased their capability in clinical decision-making, their adaptation to severe conditions like Post-traumatic Stress Disorder (PTSD) remains largely unexplored. Therefore, we collect 411 clinician-administered diagnostic interviews and devise a novel approach to obtain high-quality data. Moreover, we build a comprehensive framework to automate PTSD diagnostic assessments based on interview contents by leveraging two state-of-the-art LLMs, GPT-4 and Llama-2, with potential for broader clinical diagnoses. Our results illustrate strong promise for LLMs, tested on our dataset, to aid clinicians in diagnostic validation. To the best of our knowledge, this is the first AI system that fully automates assessments for mental illness based on clinician-administered interviews.

**ИИ:** разошлись — Opus + (клиническая оценка: GPT-4 and Llama-2 run PTSD assessments from clinician-administered interview transcripts; the clinicians' ratings of the same interviews are the likely reference.); Sonnet ? (неясно, кто ставил эталонные метки: LLMs assess PTSD from clinician-administered interview transcripts; unclear whether the reference is clinician coding of the text or the diagnosis/score, so full text is needed.)

**Решение:** ?

---

### 354 · R11904

**Aligning Large Language Models for Enhancing Psychiatric Interviews Through Symptom Delineation and Summarization: Pilot Study.**

2024 · JMIR formative research · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.2196/58418

BACKGROUND: Recent advancements in large language models (LLMs) have accelerated their use across various domains. Psychiatric interviews, which are goal-oriented and structured, represent a significantly underexplored area where LLMs can provide substantial value. In this study, we explore the application of LLMs to enhance psychiatric interviews by analyzing counseling data from North Korean defectors who have experienced traumatic events and mental health issues. OBJECTIVE: This study aims to investigate whether LLMs can (1) delineate parts of the conversation that suggest psychiatric symptoms and identify those symptoms, and (2) summarize stressors and symptoms based on the interview dialogue transcript. METHODS: Given the interview transcripts, we align the LLMs to perform 3 tasks: (1) extracting stressors from the transcripts, (2) delineating symptoms and their indicative sections, and (3) summarizing the patients based on the extracted stressors and symptoms. These 3 tasks address the 2 objectives, where delineating symptoms is based on the output from the second task, and generating the summary of the interview incorporates the outputs from all 3 tasks. In this context, the transcript data were labeled by mental health experts for the training and evaluation of the LLMs. RESULTS: First, we present the performance of LLMs in estimating (1) the transcript sections related to psychiatric symptoms and (2) the names of the corresponding symptoms. In the zero-shot inference setting using the GPT-4 Turbo model, 73 out of 102 transcript segments demonstrated a recall mid-token distance d<20 for estimating the sections associated with the symptoms. For evaluating the names of the corresponding symptoms, the fine-tuning method demonstrates a performance advantage over the zero-shot inference setting of the GPT-4 Turbo model. On average, the fine-tuning method achieves an accuracy of 0.82, a precision of 0.83, a recall of 0.82, and an F1-score of 0.82. Second, the transcripts are used to generate summaries for each interviewee using LLMs. This generative task was evaluated using metrics such as Generative Evaluation (G-Eval) and Bidirectional Encoder Representations from Transformers Score (BERTScore). The summaries generated by the GPT-4 Turbo model, utilizing both symptom and stressor information, achieve high average G-Eval scores: coherence of 4.66, consistency of 4.73, fluency of 2.16, and relevance of 4.67. Furthermore, it is noted that the use of retrieval-augmented generation did not lead to a significant improvement in performance. CONCLUSIONS: LLMs, using either (1) appropriate prompting techniques or (2) fine-tuning methods with data labeled by mental health experts, achieved an accuracy of over 0.8 for the symptom delineation task when measured across all segments in the transcript. Additionally, they attained a G-Eval score of over 4.6 for coherence in the summarization task. This research contributes to the emerging field of applying LLMs in psychiatric interviews and demonstrates their potential effectiveness in assisting mental health practitioners.

**ИИ:** + · обе модели · кодирование сессий · GPT-4 and a fine-tuned LLM identify psychiatric symptoms in interview transcripts, compared against labels from mental health experts.

**Решение:** =

---

### 355 · R11906

**Evaluating the Accuracy and Concordance of the DMIND AI Application with A Renowned Depression Assessment Tool in Thai Adults**

2024 · Chulalongkorn Medical Journal · article · en · https://doi.org/10.56808/2673-060x.5495

Background: In Thailand, the high prevalence of depression, particularly in rural areas with limited mental health services, poses significant challenges. Advanced technologies like digital phenotyping and artificial intelligence (AI), particularly Natural Language Processing (NLP) and Large Language Models (LLMs), offer promising solutions by analyzing digital data to detect early signs of depression. Objective: This study evaluated the performance of the “Detection and Monitoring Intelligence Network of Depression (DMIND)” application, an AI-powered screening tool for detecting depression in Thai adults that analyzes behavioral data from participant responses using machine learning algorithms, such as NLP models and LLMs. The study aimed to determine the agreement of the DMIND AI model and the Thai version of the Hamilton Depression Rating Scale (HDRS-17 Thai) in classifying depression severity. Methods: This cross-sectional study recruited 388 participants from one tertiary care hospital and two psychiatric hospitals. Initially, participants used the DMIND application, where they were asked to answer a series of questions. Their response in the application was recorded and a pre-trained AI model predicted their depression severity. Subsequently, a trained nurse or psychologist then assessed participants using the HDRS-17 Thai to establish a baseline measure of depression severity. Statistical analysis involved comparing the depression severity classifications from the DMIND AI model with the HDRS-17 Thai. Cohen’s kappa coefficient, sensitivity, specificity, and predictive values were used to evaluate the agreement between the two assessments. Results: Our DMIND application demonstrated moderate agreement with the HDRS-17 Thai, indicating substantial consistency in depression severity classification. The tool showed high sensitivity (87.30%) and moderate specificity (59.50%), with strong negative predictive values for detecting depression. Conclusion: The AI-powered DMIND application effectively screens for depression by analyzing digital data from participants’ responses. Its moderate agreement with a traditional clinical assessment and strong diagnostic performance highlights its potential as a scalable, accessible tool for mental health management in Thailand. Integrating AI tools like the DMIND into the public health infrastructure could significantly enhance the accessibility, accuracy, and responsiveness of mental health services, particularly in underserved regions, potentially revolutionizing the management and treatment of depression across the country

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · AI (possibly LLM) rates depression severity from app responses vs clinician HDRS; the clinician interview is separate, and the LLM type is unclear.

**Решение:** =

---

### 356 · R11915

**Assessing Motivational Interviewing Sessions with AI-Generated Patient Simulations**

2024 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · conferenceproceeding/, conference-paper · https://doi.org/10.18653/v1/2024.clpsych-1.1

There is growing interest in utilizing large language models (LLMs) in the field of mental health, and this goes as far as suggesting automated LLM-based therapists. Evaluating such generative models in therapy sessions is essential, yet remains an ongoing and complex challenge. We suggest a novel approach: an LLMbased digital patient platform which generates digital patients that can engage in a text-based conversation with either automated or human therapists. Moreover, we show that LLMs can be used to rate the quality of such sessions by completing questionnaires originally designed for human patients. We demonstrate that the ratings are both statistically reliable and valid, indicating that they are consistent and capable of distinguishing among three levels of therapist expertise. In the present study, we focus on motivational interviewing, but we suggest that this platform can be adapted to facilitate other types of therapies. We plan to publish the digital patient platform and make it available to the research community, with the hope of contributing to the standardization of evaluating automated therapists.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM rates MI session quality; validity shown by therapist expertise levels, and it is unclear whether human ratings of the same sessions were compared.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): LLM digital patients rate MI sessions via questionnaires, validated against therapist expertise levels, not against human coders' ratings of the same texts.)

**Решение:** ?

---

### 357 · R11916

**Shadows of wisdom: Classifying meta-cognitive and morally grounded narrative content via large language models.**

2024 · Behavior research methods · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.3758/s13428-024-02441-0

We investigated large language models' (LLMs) efficacy in classifying complex psychological constructs like intellectual humility, perspective-taking, open-mindedness, and search for a compromise in narratives of 347 Canadian and American adults reflecting on a workplace conflict. Using state-of-the-art models like GPT-4 across few-shot and zero-shot paradigms and RoB-ELoC (RoBERTa -fine-tuned-on-Emotion-with-Logistic-Regression-Classifier), we compared their performance with expert human coders. Results showed robust classification by LLMs, with over 80% agreement and F1 scores above 0.85, and high human-model reliability (Cohen's κ Md across top models = .80). RoB-ELoC and few-shot GPT-4 were standout classifiers, although somewhat less effective in categorizing intellectual humility. We offer example workflows for easy integration into research. Our proof-of-concept findings indicate the viability of both open-source and commercial LLMs in automating the coding of complex constructs, potentially transforming social science research.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-4 coded wise-reasoning constructs in conflict narratives and was compared with expert human coders, reporting Cohen's kappa.

**Решение:** =

---

### 358 · R11925

**Exploring the Capabilities of Prompted Large Language Models in Educational and Assessment Applications**

2024 · arXiv (Cornell University) · conferencepaper/, journalarticle, preprint/article · en · https://doi.org/10.48550/arxiv.2405.11579

In the era of generative artificial intelligence (AI), the fusion of large language models (LLMs) offers unprecedented opportunities for innovation in the field of modern education. We embark on an exploration of prompted LLMs within the context of educational and assessment applications to uncover their potential. Through a series of carefully crafted research questions, we investigate the effectiveness of prompt-based techniques in generating open-ended questions from school-level textbooks, assess their efficiency in generating open-ended questions from undergraduate-level technical textbooks, and explore the feasibility of employing a chain-of-thought inspired multi-stage prompting approach for language-agnostic multiple-choice question (MCQ) generation. Additionally, we evaluate the ability of prompted LLMs for language learning, exemplified through a case study in the low-resource Indian language Bengali, to explain Bengali grammatical errors. We also evaluate the potential of prompted LLMs to assess human resource (HR) spoken interview transcripts. By juxtaposing the capabilities of LLMs with those of human experts across various educational tasks and domains, our aim is to shed light on the potential and limitations of LLMs in reshaping educational practices. Accepted at EDM 2024

**ИИ:** ? · обе модели · неясен конструкт · Mostly educational question generation, but LLM assessment of HR interview transcripts against human experts might involve behavioural or interpersonal constructs.

**Решение:** =

---

### 359 · R11928

**Counseling Responses for Mental Health Forum Questions with Early Maladaptive Schema Prediction**

2024 · Frontiers in artificial intelligence and applications · journalarticle, conference, book-chapter · en · https://doi.org/10.3233/faia240785

State-of-the-art Large Language Models (LLMs) have shown remarkable capabilities for general Question Answering (QA) tasks. However, their practical use for answering mental health questions has been limited due to the missing link between LLM-generated answer responses and well-established theories and guiding principles from Psychology and Counseling. We present a first step in this direction with STeer, an AI-based method that supports Schema Therapy-enabled responses for mental health questions on community QA forums. STeer uses Early Maladaptive Schemas (EMSs), a fundamental concept from Schema Therapy that characterizes “self-defeating, unhealthy patterns of thought and behavior” in individuals, to effectively prompt state-of-the-art LLMs to generate specific, theoretically-grounded, empathetic counseling responses to mental health questions. We present EMSRank, a novel method based on the Personalized PageRank algorithm, to automatically predict the EMSs from mental health forum question texts. We show that EMSRank is computationally scalable and can be further combined with textual entailment to obtain high precision, explainable EMS labels for mental health forum questions. To address the current lack of annotated datasets, we also leveraged on EMSRank to create a first-of-its-kind, large dataset of about 23K EMS-annotated mental health questions from three diverse, currently operating, peer-support community forums for mental health. With the global rise in mental health issues, our work is a timely step towards enabling the use of AI-based assistive tools for counseling support on mental health community forums.

**ИИ:** разошлись — Opus ? (другое: LLMs generate responses; schema labels come from PageRank/entailment. Unclear whether LLM schema labeling is compared against human annotations.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLMs generate counseling responses; EMS prediction uses a non-LLM PageRank method, so there is no LLM coding compared with human labels.)

**Решение:** -

---

### 360 · R11938

**(121) Utilizing ChatGPT for Urology Trainee Simulation of Peyronie’s Disease Counseling**

2024 · The Journal of Sexual Medicine · journalarticle, article · en · https://doi.org/10.1093/jsxmed/qdae001.115

Abstract Introduction Peyronie’s disease is a medical issue with significant psychological overtones. However, trainee exposure to initial counseling and management can be limited and therefore understanding both the disease state and its psychological effects can be difficult to master. Institutions have incorporated simulation-based education to augment resident skills and knowledge in topics such as transgender health and SICU patient management. The gold standard of assessing trainees in simulated clinical interaction has been objective structured clinical examinations (OSCE). However, novel AI-based technologies like ChatGPT offer a promising alternative for resident education and assessment. ChatGPT, developed by OpenAI, utilizes natural language processing technology to provide human-like responses to open-ended questions posed by users. Preliminary reports have already described its use in training emergency medicine residents in delivering bad news. Objective To simulate a realistic clinical scenario utilizing ChatGPT to improve resident and student confidence in Peyronie’s disease evaluation and treatment, and to assess ChatGPT’s ability to deliver actionable feedback to trainees on both knowledge base and patient interaction compared to evaluation by a sexual medicine specialist. Methods ChatGPT Plus was utilized to roleplay the patient in an initial consultation for Peyronie’s disease. A detailed input was composed to establish the rules of the simulation (Figure 1). ChatGPT was prompted to conduct a final assessment of trainee performance with standardized scales in accuracy, comprehensiveness, and empathy (A, C, E). ChatGPT was prompted to use the 2015 AUA Peyronie’s Disease Diagnosis and Treatment Guidelines when formulating its assessment and feedback. Three trainees with different experience levels performed the simulation. At completion, a fellowship-trained sexual medicine specialist separately graded each trainee’s performance using the same scale. Cohen’s kappa was calculated to assess inter-rater reliability. Results Three urology trainees performed the simulation: a 3rd year medical student, a PGY2 resident, and a PGY4 resident. Trainee performance scores are shown in Table 1. Mean ChatGPT ratings were 8.7, 8.0, and 9.0 (A, C, E), while andrologists ratings were 7.0, 4.7, and 6.3 (A, C, E). Progressive improvement was demonstrated as trainee experience increased. ChatGPT generally rated trainees at higher competency levels than andrologists. Cohen’s kappa was calculated to be -0.125, -0.125, and 0.0 (A, C, E), indicating an overall low level of agreement between ChatGPT and andrologists assessment of trainees. Conclusions Our findings demonstrate that ChatGPT has potential to be a successful tool for urology resident and medical student education on Peyronie’s disease counseling. However, there was disagreement in trainee ratings between ChatGPT and the sexual medicine specialist. ChatGPT provided trainees constructive, actionable feedback referencing current guidelines (Figure 2). When given defined parameters for a clinical scenario, ChatGPT can be effective in designing a realistic standardized patient simulation. However, ChatGPT has not appeared to master the competency and accuracy of that expected from a sexual medicine specialist. Tweaking the initial input can allow for testing competency in various alternative clinical vignettes. Further collection of real-world data is needed to better assess ChatGPT’s rating of the learner’s performance, ideally in conjunction with national/international guidelines. Disclosure Any of the authors act as a consultant, employee or shareholder of an industry for: Fellow, Posterity Health, Coloplast, Hims, Genentech.

**ИИ:** разошлись — Opus + (LLM-судья: ChatGPT and a sexual medicine specialist rated trainee counselling transcripts on the same scale, including empathy; Cohen's kappa reported.); Sonnet ? (неясен конструкт: ChatGPT rated trainee counseling performance (accuracy, comprehensiveness, empathy) against a specialist with Cohen's kappa. Empathy fits the review, but the setting is medical education and the other scales are knowledge-based.)

**Решение:** +

---

### 361 · R11942

**Cactus: Towards Psychological Counseling Conversations using Cognitive Behavioral Theory**

2024 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2407.03103

Recently, the demand for psychological counseling has significantly increased as more individuals express concerns about their mental health. This surge has accelerated efforts to improve the accessibility of counseling by using large language models (LLMs) as counselors. To ensure client privacy, training open-source LLMs faces a key challenge: the absence of realistic counseling datasets. To address this, we introduce Cactus, a multi-turn dialogue dataset that emulates real-life interactions using the goal-oriented and structured approach of Cognitive Behavioral Therapy (CBT). We create a diverse and realistic dataset by designing clients with varied, specific personas, and having counselors systematically apply CBT techniques in their interactions. To assess the quality of our data, we benchmark against established psychological criteria used to evaluate real counseling sessions, ensuring alignment with expert evaluations. Experimental results demonstrate that Camel, a model trained with Cactus, outperforms other models in counseling skills, highlighting its effectiveness and potential as a counseling agent. We make our data, model, and code publicly available. Published at EMNLP 2024 Findings

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mainly a dataset-generation paper, but its LLM-based CTRS counseling evaluation is said to align with expert evaluations; LLM–human agreement may be reported.

**Решение:** =

---

### 362 · R11961

**Decoding depression: Analyzing social network insights for depression severity assessment with transformers and explainable AI**

2024 · Natural Language Processing Journal · article · en · https://doi.org/10.1016/j.nlp.2024.100079

Depression is a mental state characterized by recurrent feelings of melancholy, hopelessness, and disinterest in activities, having a significant negative influence on everyday functioning and general well-being. Millions of users express their thoughts and emotions on social media platforms, which can be used as a rich source of data for early detection of depression. In this connection, this work leverages an ensemble of transformer-based architectures for quantifying the severity of depression from social media posts into four categories- non-depressed, mild, moderate, and severe. At first, a diverse range of preprocessing techniques is employed to enhance the quality and relevance of the input. Then, the preprocessed samples are passed through three variants of transformer-based models, namely vanilla BERT, BERTweet, and ALBERT, for generating predictions, which are combined using a weighted soft-voting approach. We conduct a comprehensive explainability analysis to gain deeper insights into the decision-making process, examining both local and global perspectives. Furthermore, to the best of our knowledge, we are the first ones to explore the extent to which a Large Language Model (LLM) like ‘ChatGPT’ can perform this task. Evaluation of the model on the publicly available ‘DEPTWEET’ dataset produces state-of-the-art performance with 13.5% improvement in AUC-ROC score.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: ChatGPT rates depression severity in tweets from DEPTWEET, a human-annotated dataset; transformer ensemble is the main focus.); Sonnet ? (неясно, кто ставил эталонные метки: Mainly BERT ensembles, but ChatGPT is also tested on DEPTWEET depression severity. The abstract doesn't say whether the labels are human annotations, so check the full text.)

**Решение:** +

---

### 363 · R11972

**Chinchunmei at WASSA 2024 Empathy and Personality Shared Task: Boosting LLM’s Prediction with Role-play Augmentation and Contrastive Reasoning Calibration**

2024 · Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis · journalarticle · https://doi.org/10.18653/v1/2024.wassa-1.32

This paper presents the Chinchunmei team’s contributions to the WASSA2024 Shared-Task 1: Empathy Detection and Emotion Classification. We participated in Tracks 1, 2, and 3 to predict empathetic scores based on dialogue, article, and essay content. We choose Llama3-8b-instruct as our base model. We developed three supervised fine-tuning schemes: standard prediction, role-play, and contrastive prediction, along with an innovative scoring calibration method called Contrastive Reasoning Calibration during inference. Pearson Correlation was used as the evaluation metric across all tracks. For Track 1, we achieved 0.43 on the devset and 0.17 on the testset. For Track 2 emotion, empathy, and polarity labels, we obtained 0.64, 0.66, and 0.79 on the devset and 0.61, 0.68, and 0.58 on the testset. For Track 3 empathy and distress labels, we got 0.64 and 0.56 on the devset and 0.33 and 0.35 on the testset.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Fine-tuned Llama3 predicts empathy/emotion scores; WASSA Track 2 turn-level labels come from human annotators (Track 3 labels are self-reports).); Sonnet ? (неясно, кто ставил эталонные метки: Fine-tuned Llama3 predicts empathy, emotion and distress scores in WASSA data. Some labels are likely third-party human annotations and some are writer self-reports, so the reference is unclear.)

**Решение:** +

---

### 364 · R11974

**Enhancing the Analysis of Interdisciplinary Learning Quality with GPT Models: Fine-Tuning and Knowledge-Empowered Approaches**

2024 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-031-64312-5_19

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (неясен конструкт: No abstract; GPT likely codes student texts for interdisciplinary learning quality, but whether it's a psychological/cognitive construct with a human-coded reference is unclear.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Interdisciplinary learning quality analysis with GPT is educational, not a psychological or clinical construct; no abstract available.)

**Решение:** ?

---

### 365 · R11975

**Can Generic LLMs Help Analyze Child-adult Interactions Involving Children with Autism in Clinical Observation?**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2411.10761

Large Language Models (LLMs) have shown significant potential in understanding human communication and interaction. However, their performance in the domain of child-inclusive interactions, including in clinical settings, remains less explored. In this work, we evaluate generic LLMs' ability to analyze child-adult dyadic interactions in a clinically relevant context involving children with ASD. Specifically, we explore LLMs in performing four tasks: classifying child-adult utterances, predicting engaged activities, recognizing language skills and understanding traits that are clinically relevant. Our evaluation shows that generic LLMs are highly capable of analyzing long and complex conversations in clinical observation sessions, often surpassing the performance of non-expert human evaluators. The results show their potential to segment interactions of interest, assist in language skills evaluation, identify engaged activities, and offer clinical-relevant context for assessments. GenAI for Health Workshop, NeurIPS 2024

**ИИ:** + · обе модели · кодирование сессий · LLMs classify utterances and rate clinically relevant ASD traits and language skills in clinical observation transcripts, compared with human annotations and evaluators.

**Решение:** =

---

### 366 · R11977

**Evaluation of OpenAI o1: Opportunities and Challenges of AGI**

2024 · arXiv (Cornell University) · journalarticle, review, preprint/article · en · https://doi.org/10.48550/arxiv.2409.18486

This comprehensive study evaluates the performance of OpenAI's o1-preview large language model across a diverse array of complex reasoning tasks, spanning multiple domains, including computer science, mathematics, natural sciences, medicine, linguistics, and social sciences. Through rigorous testing, o1-preview demonstrated remarkable capabilities, often achieving human-level or superior performance in areas ranging from coding challenges to scientific reasoning and from language processing to creative problem-solving. Key findings include: -83.3% success rate in solving complex competitive programming problems, surpassing many human experts. -Superior ability in generating coherent and accurate radiology reports, outperforming other evaluated models. -100% accuracy in high school-level mathematical reasoning tasks, providing detailed step-by-step solutions. -Advanced natural language inference capabilities across general and specialized domains like medicine. -Impressive performance in chip design tasks, outperforming specialized models in areas such as EDA script generation and bug analysis. -Remarkable proficiency in anthropology and geology, demonstrating deep understanding and reasoning in these specialized fields. -Strong capabilities in quantitative investing. O1 has comprehensive financial knowledge and statistical modeling skills. -Effective performance in social media analysis, including sentiment analysis and emotion recognition. The model excelled particularly in tasks requiring intricate reasoning and knowledge integration across various fields. While some limitations were observed, including occasional errors on simpler problems and challenges with certain highly specialized concepts, the overall results indicate significant progress towards artificial general intelligence.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: Broad o1 evaluation that includes emotion recognition on social media, probably against human-labelled benchmarks; needs full-text check.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: General multi-domain evaluation of o1-preview; only a minor social media sentiment/emotion component, not a focused psychological coding study against human labels.)

**Решение:** -

---

### 367 · R11978

**Can Large Language Models Assess Personality From Asynchronous Video Interviews? A Comprehensive Evaluation of Validity, Reliability, Fairness, and Rating Patterns**

2024 · IEEE Transactions on Affective Computing · journalarticle, article · en · https://doi.org/10.1109/taffc.2024.3374875

The advent of Artificial Intelligence (AI) technologies has precipitated the rise of asynchronous video interviews (AVIs) as an alternative to conventional job interviews. These one-way video interviews are conducted online and can be analyzed using AI algorithms to automate and speed up the selection procedure. In particular, the swift advancement of Large Language Models (LLMs) has significantly decreased the cost and technical barrier to developing AI systems for automatic personality and interview performance evaluation. However, the generative and task-unspecific nature of LLMs might pose potential risks and biases when evaluating humans based on their AVI responses. In this study, we conducted a comprehensive evaluation of the validity, reliability, fairness, and rating patterns of two widely-used LLMs, GPT-3.5 and GPT-4, in assessing personality and interview performance from an AVI. We compared the personality and interview performance ratings of the LLMs with the ratings from a task-specific AI model and human annotators using simulated AVI responses of 685 participants. The results show that LLMs can achieve similar or even better zero-shot validity compared with the task-specific AI model when predicting personality traits. The verbal explanations for predicting personality traits generated by LLMs are interpretable by the personality items that are designed according to psychological theories. However, LLMs also suffered from uneven performance across different traits, insufficient test-retest reliability, and the emergence of certain biases. Thus, it is necessary to exercise caution when applying LLMs for human-related application scenarios, especially for significant decisions such as employment.</p

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT-3.5/GPT-4 rated personality from interview responses and were compared with human annotators' ratings of the same responses; validity may also use self-report.

**Решение:** =

---

### 368 · R1198

**Strategic Competence in Sustainability Education: Conceptual Patterns Identified Through AI-Assisted Qualitative Analysis**

2026 · Sustainability · journalarticle, article · en · https://doi.org/10.3390/su18073643

This study investigates how participants conceptualise sustainability and sustainability citizenship, as well as how these conceptualisations relate to perceived agency. Drawing on two open-ended prompts, it analyses participants’ visions of a sustainable future and the roles they would like to play within it. The dataset was based on 1714 coded response segments from 164 participants. Methodologically, the study combines qualitative content analysis, independent human-AI double coding, manual validation, inter-rater reliability assessment, and residual-based co-occurrence analysis within a qualitatively grounded mixed-methods design. The results show that sustainability is predominantly framed in civic, symbolic, and ecological terms, whereas strategic competence and professionally articulated agency remain less visible. Sustainability meanings and role conceptions also vary systematically across disciplinary contexts. In addition, the analyses reveal patterned gaps between participants’ future visions and their self-attributed roles in sustainability transformations. The study contributes empirical insights into sustainability meaning-making and perceived agency and shows how LLM-assisted coding can be embedded in a transparent mixed-methods workflow. For sustainability education, the findings underline the importance of strengthening strategic and systemic dimensions of competence and linking civic engagement more closely to professional pathways of action.

**ИИ:** ? · обе модели · неясен конструкт · Human–AI double coding of open responses with an IRR check; unclear whether sustainability conceptions and perceived agency count as psychological constructs.

**Решение:** =

---

### 369 · R12011

**How Can Client Motivational Language Inform Psychotherapy Agents?**

2024 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, conference-paper · https://doi.org/10.18653/v1/2024.clpsych-1.3

Within Motivational Interviewing (MI), client utterances are coded as for or against a certain behaviour change, along with commitment strength; this is essential to ensure therapists soften rather than persisting goal-related actions in the face of resistance. Prior works in MI agents have been scripted or semi-scripted, limiting users’ natural language expressions. With the aim of automating the MI interactions, we propose and explore the task of automated identification of client motivational language. Employing Large Language Models (LLMs), we compare in-context learning (ICL) and instruction fine-tuning (IFT) with varying training sizes for this identification task. Our experiments show that both approaches can learn under low-resourced settings. Our results demonstrate that IFT, though cheaper, is more stable to prompt choice, and yields better performance with more data. Given the detected motivation, we further present an approach to the analysis of therapists’ strategies for balancing building rapport with clients with advancing the treatment plan. A framework of MI agents is developed using insights from the data and the psychotherapy literature.

**ИИ:** + · обе модели · кодирование сессий · LLMs (ICL and instruction fine-tuning) identify client motivational language (change/sustain talk) in MI transcripts, evaluated against human-coded labels.

**Решение:** =

---

### 370 · R12026

**Unlocking LLMs: Addressing Scarce Data and Bias Challenges in Mental Health**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2412.12981

Large language models (LLMs) have shown promising capabilities in healthcare analysis but face several challenges like hallucinations, parroting, and bias manifestation. These challenges are exacerbated in complex, sensitive, and low-resource domains. Therefore, in this work we introduce IC-AnnoMI, an expert-annotated motivational interviewing (MI) dataset built upon AnnoMI by generating in-context conversational dialogues leveraging LLMs, particularly ChatGPT. IC-AnnoMI employs targeted prompts accurately engineered through cues and tailored information, taking into account therapy style (empathy, reflection), contextual relevance, and false semantic change. Subsequently, the dialogues are annotated by experts, strictly adhering to the Motivational Interviewing Skills Code (MISC), focusing on both the psychological and linguistic dimensions of MI dialogues. We comprehensively evaluate the IC-AnnoMI dataset and ChatGPT's emotional reasoning ability and understanding of domain intricacies by modeling novel classification tasks employing several classical machine learning and current state-of-the-art transformer approaches. Finally, we discuss the effects of progressive prompting strategies and the impact of augmented data in mitigating the biases manifested in IC-AnnoM. Our contributions provide the MI community with not only a comprehensive dataset but also valuable insights for using LLMs in empathetic text generation for conversational therapy in supervised settings. International Conference on Natural Language Processing and Artificial Intelligence for Cyber Security (NLPAICS) 2024

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · ChatGPT generates MI dialogues that experts annotate with MISC; the classifiers seem to be classical/transformer models, and it's unclear whether an LLM also labels them.

**Решение:** =

---

### 371 · R12027

**MoralBERT: A Fine-Tuned Language Model for Capturing Moral Values in Social Discussions**

2024 · Conference on Information Technology for Social Good · book, journalarticle, text/article · en · https://doi.org/10.1145/3677525.3678694

Moral values play a fundamental role in how we evaluate information, make decisions, and form judgements around important social issues. Controversial topics, including vaccination, abortion, racism, and sexual orientation, often elicit opinions and attitudes that are not solely based on evidence but rather reflect moral worldviews. Recent advances in Natural Language Processing (NLP) show that moral values can be gauged in human-generated textual content. Building on the Moral Foundations Theory (MFT), this paper introduces MoralBERT, a range of language representation models fine-tuned to capture moral sentiment in social discourse. We describe a framework for both aggregated and domain-adversarial training on multiple heterogeneous MFT human-annotated datasets sourced from Twitter (now X), Reddit, and Facebook that broaden textual content diversity in terms of social media audience interests, content presentation and style, and spreading patterns. We show that the proposed framework achieves an average F1 score that is between 11% and 32% higher than lexicon-based approaches, Word2Vec embeddings, and zero-shot classification with large language models such as GPT-4 for in-domain inference. Domain-adversarial training yields better out-of domain predictions than aggregate training while achieving comparable performance to zero-shot learning. Our approach contributes to annotation-free and effective morality learning, and provides useful insights towards a more comprehensive understanding of moral narratives in controversial social debates using NLP.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Zero-shot GPT-4 classification of moral foundations in social-media posts, evaluated against human-annotated MFT datasets; moral values are a psychological construct.); Sonnet ? (неясен конструкт: Main model is BERT, but GPT-4 zero-shot is a baseline scored against human-annotated Moral Foundations labels on social media posts; moral values may count as a psychological construct.)

**Решение:** +

---

### 372 · R12029

**Team ISM at CLPsych 2024: Extracting Evidence of Suicide Risk from Reddit Posts with Knowledge Self-Generation and Output Refinement using A Large Language Model**

2024 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, conference-paper, proceedings-article · https://doi.org/10.18653/v1/2024.clpsych-1.16

This paper presents our approach to the CLPsych 2024 shared task: utilizing large language models (LLMs) for finding supporting evidence about an individual's suicide risk level in Reddit posts. Our framework is constructed around an LLM with knowledge self-generation and output refinement. The knowledge self-generation process produces task-related knowledge which is generated by the LLM and leads to accurate risk predictions. The output refinement process, later, with the selected best set of LLM-generated knowledge, refines the outputs by prompting the LLM repeatedly with different knowledge instances interchangeably. We achieved highly competitive results comparing to the top-performance participants with our official recall of 93.5%, recall--precision harmonic-mean of 92.3%, and mean consistency of 96.1%.

**ИИ:** + · обе модели · бенчмарк с метками людей · LLM extracts suicide-risk evidence from Reddit posts in the CLPsych 2024 shared task; output is scored for recall and precision against expert-annotated evidence.

**Решение:** =

---

### 373 · R12034

**Evaluating the Effectiveness of a Large Language Model in the Psychological Assessment of Potential Liver Transplant Candidates: A Feasibility Study**

2024 · Saudi Journal of Medical and Pharmaceutical Sciences · journalarticle, article, journal-article · en · https://doi.org/10.36348/sjmps.2024.v10i10.006

Introduction: The use of artificial intelligence (AI) in medical settings has shown promise in various domains including diagnostics, treatment recommendation, and patient management. Recent advances have explored the potential of AI in pre-surgical assessments, but its application in transplant psychology remains unexplored. The objective of this study is to assess the effectiveness of AI in the context of screening potential liver transplant donors and recipients. To assess the feasibility of using ChatGPT-4 to screen potential liver transplant donors and recipients. Methods: This study utilizes a cross-sectional research design to evaluate the feasibility of using ChatGPT-4 in the preliminary screening of living liver donors and liver transplant candidates. The study aims to determine the accuracy and reliability of ChatGPT-4 in assessing hypothetical scenarios involving potential donors and recipients. Results: The analysis showed no found no significant differences between ChatGPT-4 and the expert panel in assessing liver transplant candidates, demonstrating an overall accuracy of 83.58%, sensitivity of 56.10%, and specificity of 80.49%. Additionally, the Cohen’s Kappa statistic of 0.68 (95% CI: 0.52-0.83) indicated substantial agreement between ChatGPT-4 and the psychologists’ evaluations. The absence of false positives (0%) and a low false negative rate (8%) emphasize ChatGPT-4's cautious and accurate decision-making capabilities. Conclusion: The findings of this study demonstrate that ChatGPT-4 has the potential to serve as an effective screening tool for liver transplant candidates, complementing the work of human experts and enhancing the overall efficiency of the transplant process. While challenges remain, the integration of AI into the liver transplantation workflow could lead to significant improvements in candidate evaluation and patient outcomes, paving the way for the broader application of AI in clinical practice.

**ИИ:** + · обе модели · клиническая оценка · GPT-4 rated psychological suitability in transplant-candidate scenarios against psychologists' evaluations; Cohen's kappa 0.68 is reported.

**Решение:** =

---

### 374 · R12045

**Detection of suicidality from medical text using privacy-preserving large language models.**

2024 · The British journal of psychiatry : the journal of mental science · journal article, review, journalarticle · eng · https://doi.org/10.1192/bjp.2024.134

BACKGROUND: Attempts to use artificial intelligence (AI) in psychiatric disorders show moderate success, highlighting the potential of incorporating information from clinical assessments to improve the models. This study focuses on using large language models (LLMs) to detect suicide risk from medical text in psychiatric care. AIMS: To extract information about suicidality status from the admission notes in electronic health records (EHRs) using privacy-sensitive, locally hosted LLMs, specifically evaluating the efficacy of Llama-2 models. METHOD: We compared the performance of several variants of the open source LLM Llama-2 in extracting suicidality status from 100 psychiatric reports against a ground truth defined by human experts, assessing accuracy, sensitivity, specificity and F1 score across different prompting strategies. RESULTS: A German fine-tuned Llama-2 model showed the highest accuracy (87.5%), sensitivity (83.0%) and specificity (91.8%) in identifying suicidality, with significant improvements in sensitivity and specificity across various prompt designs. CONCLUSIONS: The study demonstrates the capability of LLMs, particularly Llama-2, in accurately extracting information on suicidality from psychiatric records while preserving data privacy. This suggests their application in surveillance systems for psychiatric emergencies and improving the clinical management of suicidality by improving systematic quality control and research.

**ИИ:** + · обе модели · клиническая оценка · Llama-2 variants extracted suicidality status from psychiatric admission notes and were compared with a ground truth set by human experts.

**Решение:** =

---

### 375 · R12046

**Detection of Suicidality Through Privacy-Preserving Large Language Models**

2024 · medRxiv · preprint, ppr · en · https://doi.org/10.1101/2024.03.06.24303763

Abstract Importance Attempts to use Artificial Intelligence (AI) in psychiatric disorders show moderate success, high-lighting the potential of incorporating information from clinical assessments to improve the models. The study focuses on using Large Language Models (LLMs) to manage unstructured medical text, particularly for suicide risk detection in psychiatric care. Objective The study aims to extract information about suicidality status from the admission notes of electronic health records (EHR) using privacy-sensitive, locally hosted LLMs, specifically evaluating the efficacy of Llama-2 models. Main Outcomes and Measures The study compares the performance of several variants of the open source LLM Llama-2 in extracting suicidality status from psychiatric reports against a ground truth defined by human experts, assessing accuracy, sensitivity, specificity, and F1 score across different prompting strategies. Results A German fine-tuned Llama-2 model showed the highest accuracy (87.5%), sensitivity (83%) and specificity (91.8%) in identifying suicidality, with significant improvements in sensitivity and specificity across various prompt designs. Conclusions and Relevance The study demonstrates the capability of LLMs, particularly Llama-2, in accurately extracting the information on suicidality from psychiatric records while preserving data-privacy. This suggests their application in surveillance systems for psychiatric emergencies and improving the clinical management of suicidality by improving systematic quality control and research. Key Points Question Can large language models (LLMs) accurately extract information on suicidality from electronic health records (EHR)? Findings In this analysis of 100 psychiatric admission notes using Llama-2 models, the German fine-tuned model (Emgerman) demonstrated the highest accuracy (87.5%), sensitivity (83%) and specificity (91.8%) in identifying suicidality, indicating the models’ effectiveness in on-site processing of clinical documentation for suicide risk detection. Meaning The study highlights the effectiveness of LLMs, particularly Llama-2, in accurately extracting the information on suicidality from psychiatric records, while preserving data privacy. It recommends further evaluating these models to integrate them into clinical management systems to improve detection of psychiatric emergencies and enhance systematic quality control and research in mental health care.

**ИИ:** + · обе модели · клиническая оценка · Llama-2 pulls suicidality status out of psychiatric admission notes and is scored against ground truth labelled by human experts.

**Решение:** =

---

### 376 · R12048

**Theme-Driven Keyphrase Extraction to Analyze Social Media Discourse**

2024 · Proceedings of the International AAAI Conference on Web and Social Media · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.1609/icwsm.v18i1.31391

Social media platforms are vital resources for sharing self-reported health experiences, offering rich data on various health topics. Despite advancements in Natural Language Processing (NLP) enabling large-scale social media data analysis, a gap remains in applying keyphrase extraction to health-related content. Keyphrase extraction is used to identify salient concepts in social media discourse without being constrained by predefined entity classes. This paper introduces a theme-driven keyphrase extraction framework tailored for social media, a pioneering approach designed to capture clinically relevant keyphrases from user-generated health texts. Themes are defined as broad categories determined by the objectives of the extraction task. We formulate this novel task of theme-driven keyphrase extraction and demonstrate its potential for efficiently mining social media text for the use case of treatment for opioid use disorder. This paper leverages qualitative and quantitative analysis to demonstrate the feasibility of extracting actionable insights from social media data and efficiently extracting keyphrases using minimally supervised NLP models. Our contributions include the development of a novel data collection and curation framework for theme-driven keyphrase extraction and the creation of MOUD-Keyphrase, the first dataset of its kind comprising human-annotated keyphrases from a Reddit community. We also identify the scope of minimally supervised NLP models to extract keyphrases from social media data efficiently. Lastly, we found that a large language model (ChatGPT) outperforms unsupervised keyphrase extraction models, and we evaluate its efficacy in this task. 11 pages, 2 figures, submitted to ICWSM. This version represents a substantial expansion and refocus of the previous manuscript, including new experiments, expanded data analysis, and comprehensive discussions

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT keyphrase extraction from Reddit OUD-treatment posts was compared with human annotations; unclear whether the themes are psychological or just medical entities.

**Решение:** =

---

### 377 · R12074

**Eliciting Motivational Interviewing Skill Codes in Psychotherapy with LLMs: A Bilingual Dataset and Analytical Study**

2024 · International Conference on Language Resources and Evaluation · conferenceproceeding/, journalarticle, text/preprint · https://doi.org/10.63317/3u2cyg9q5d6c

Behavioral coding (BC) in motivational interviewing (MI) holds great potential for enhancing the efficacy of MI counseling. However, manual coding is labor-intensive, and automation efforts are hindered by the lack of data due to the privacy of psychotherapy. To address these challenges, we introduce BiMISC, a bilingual dataset of MI conversations in English and Dutch, sourced from real counseling sessions. Expert annotations in BiMISC adhere strictly to the motivational interviewing skills code (MISC) scheme, offering a pivotal resource for MI research. Additionally, we present a novel approach to elicit the MISC expertise from Large language models (LLMs) for MI coding. Through the in-depth analysis of BiMISC and the evaluation of our proposed approach, we demonstrate that the LLM-based approach yields results closely aligned with expert annotations and maintains consistent performance across different languages. Our contributions not only furnish the MI community with a valuable bilingual dataset but also spotlight the potential of LLMs in MI coding, laying the foundation for future MI research.

**ИИ:** + · обе модели · кодирование сессий · LLMs apply MISC codes to real MI counseling transcripts; results are compared with expert annotations in a bilingual dataset.

**Решение:** =

---

### 378 · R12075

**Rethinking the Alignment of Psychotherapy Dialogue Generation with Motivational Interviewing Strategies**

2024 · International Conference on Computational Linguistics · conferenceproceeding/, journalarticle, conference · https://doi.org/10.48550/arxiv.2408.06527

Recent advancements in large language models (LLMs) have shown promise in generating psychotherapeutic dialogues, particularly in the context of motivational interviewing (MI). However, the inherent lack of transparency in LLM outputs presents significant challenges given the sensitive nature of psychotherapy. Applying MI strategies, a set of MI skills, to generate more controllable therapeutic-adherent conversations with explainability provides a possible solution. In this work, we explore the alignment of LLMs with MI strategies by first prompting the LLMs to predict the appropriate strategies as reasoning and then utilizing these strategies to guide the subsequent dialogue generation. We seek to investigate whether such alignment leads to more controllable and explainable generations. Multiple experiments including automatic and human evaluations are conducted to validate the effectiveness of MI strategies in aligning psychotherapy dialogue generation. Our findings demonstrate the potential of LLMs in producing strategically aligned dialogues and suggest directions for practical applications in psychotherapeutic settings.

**ИИ:** ? · обе модели · другое · Mainly MI dialogue generation, but the LLM's MI-strategy predictions may be scored against human-annotated MI codes; needs full-text check.

**Решение:** =

---

### 379 · R12076

**Assessing the Potential and Limits of Large Language Models in Qualitative Coding**

2024 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-031-76335-9_7

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests LLM qualitative coding likely compared with humans, but psychological construct unclear.

**Решение:** =

---

### 380 · R12104

**Embracing naturalistic paradigms: substituting GPT predictions for human judgments**

2024 · bioRxiv · preprint, ppr, posted-content · en · https://doi.org/10.1101/2024.06.17.599327

Abstract Naturalistic paradigms can assure ecological validity and yield novel insights in psychology and neuroscience. However, using behavioral experiments to obtain the human ratings necessary to analyze data collected with these paradigms is usually costly and time-consuming. Large language models like GPT have great potential for predicting human-like behavioral judgments. The current study evaluates the performance of GPT as a substitute for human judgments for affective dynamics in narratives. Our results revealed that GPT’s inference of hedonic valence dynamics is highly correlated with human affective perception. Moreover, the inferred neural activity based on GPT-derived valence ratings is similar to inferred neural activity based on human judgments, suggesting the potential of using GPT’s prediction as a reliable substitute for human judgments.

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT rated the emotional valence of narrative text, and these ratings were correlated with human affective ratings of the same narratives.

**Решение:** =

---

### 381 · R12110

**Reddit-Impacts: A Named Entity Recognition Dataset for Analyzing Clinical and Social Effects of Substance Use Derived from Social Media**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2405.06145

Substance use disorders (SUDs) are a growing concern globally, necessitating enhanced understanding of the problem and its trends through data-driven research. Social media are unique and important sources of information about SUDs, particularly since the data in such sources are often generated by people with lived experiences. In this paper, we introduce Reddit-Impacts, a challenging Named Entity Recognition (NER) dataset curated from subreddits dedicated to discussions on prescription and illicit opioids, as well as medications for opioid use disorder. The dataset specifically concentrates on the lesser-studied, yet critically important, aspects of substance use--its clinical and social impacts. We collected data from chosen subreddits using the publicly available Application Programming Interface for Reddit. We manually annotated text spans representing clinical and social impacts reported by people who also reported personal nonmedical use of substances including but not limited to opioids, stimulants and benzodiazepines. Our objective is to create a resource that can enable the development of systems that can automatically detect clinical and social impacts of substance use from text-based social media data. The successful development of such systems may enable us to better understand how nonmedical use of substances affects individual health and societal dynamics, aiding the development of effective public health strategies. In addition to creating the annotated data set, we applied several machine learning models to establish baseline performances. Specifically, we experimented with transformer models like BERT, and RoBERTa, one few-shot learning model DANN by leveraging the full training dataset, and GPT-3.5 by using one-shot learning, for automatic NER of clinical and social impacts. The dataset has been made available through the 2024 SMM4H shared tasks. 7 pages, 1 figure, 4 tables

**ИИ:** + · обе модели · бенчмарк с метками людей · Human-annotated Reddit dataset of clinical and social impacts of substance use; GPT-3.5 one-shot evaluated against human labels.

**Решение:** =

---

### 382 · R12120

**Leveraging Social Media for Real-Time Interpretable and Amendable Suicide Risk Prediction With Human-in-The-Loop**

2024 · IEEE Transactions on Affective Computing · journalarticle, article · en · https://doi.org/10.1109/taffc.2024.3494860

Suicide presents a global health challenge, prompting the development of diverse prevention strategies. Among them, timely identification of individuals at risk of suicide remains challenging. Although social media offers potential for tracking users’ mental status, harnessing collaboration between AI and human experts for real-time prediction of suicide risk is inadequately explored. This study presents a human-in-the-loop framework for real-time suicide risk prediction based on social media. Once a user made a new post on social media, the AI model assesses user’s suicide risk within the next month with explanation based on the historic and new posts plus domain knowledge. Human experts on the other side look into the explanation to confirm/clarify uncertain information as feedback, enabling consistent evolution of the model. Experiments on the constructed dataset, containing 66 suicidal users and 66 non-suicidal users, show that our method achieved 82.58% prediction accuracy, outperforming competitive baselines by 6.57%. Leveraging human feedback improved prediction accuracy by 4.12%. Consultation with 18 experts (including 6 medical staff and 12 psychologists) was conducted to examine the validity of our method. Ethics considerations, as well as potential and limitations of large language models in mental condition prediction, are also discussed at the end of the paper.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Possibly LLM-based suicide risk prediction from posts; labels may be future-outcome criteria rather than human coding, and LLM use is unclear.

**Решение:** =

---

### 383 · R12149

**Using LLMs to score Hierarchical Organization of Narrative Recall**

2024 · Digital Repository at the University of Maryland · text/presentation · https://doi.org/10.13016/u7me-ectv

Research has suggested that the ability to comprehend narratives relies on hierarchical organization of memory. Disorders like dementia can be detected by measures of narrative recall, however these often rely on human graders. Here we explored how LLMs can be leveraged to measure hierarchical organization of narrative recall (HONR). We had participants (n=4) recall two, 45-50 sentence stories. We then submitted the recalls (n=8) to a two-part process where we first asked chatGPT to connect the sentences in the recall to the sentences in the actual stories. Next we took the output from ChatGPT and devised two measures of HONR: Event Bunching and Linearity as proxies for Local and Global Coherence, respectively. We compared a sample of human scored responses to those semi-automated responses and found a high interrater reliability, suggesting LLMs can reliably answer questions about narrative structure.

**ИИ:** + · обе модели · подсчёт методики · ChatGPT scored narrative recall (memory assessment); compared with human scorers, reporting interrater reliability.

**Решение:** =

---

### 384 · R12151

**Towards Understanding Counseling Conversations: Domain Knowledge and Large Language Models**

2024 · Findings of the Association for Computational Linguistics: EACL · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.18653/v1/2024.findings-eacl.137

Understanding the dynamics of counseling conversations is an important task, yet it is a challenging NLP problem regardless of the recent advance of Transformer-based pre-trained language models. This paper proposes a systematic approach to examine the efficacy of domain knowledge and large language models (LLMs) in better representing conversations between a crisis counselor and a help seeker. We empirically show that state-of-the-art language models such as Transformer-based models and GPT models fail to predict the conversation outcome. To provide richer context to conversations, we incorporate human-annotated domain knowledge and LLM-generated features; simple integration of domain knowledge and LLM features improves the model performance by approximately 15%. We argue that both domain knowledge and LLM-generated features can be exploited to better characterize counseling conversations when they are used as an additional context to conversations. Findings of EACL 2024, 10 pages

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mainly predicts crisis-counseling outcomes (criterion), but LLM-generated features may mirror human-annotated domain knowledge; comparison unclear from abstract.

**Решение:** =

---

### 385 · R12155

**A Computational Framework for Behavioral Assessment of LLM Therapists**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2401.00820

The emergence of large language models (LLMs) like ChatGPT has increased interest in their use as therapists to address mental health challenges and the widespread lack of access to care. However, experts have emphasized the critical need for systematic evaluation of LLM-based mental health interventions to accurately assess their capabilities and limitations. Here, we propose BOLT, a proof-of-concept computational framework to systematically assess the conversational behavior of LLM therapists. We quantitatively measure LLM behavior across 13 psychotherapeutic approaches with in-context learning methods. Then, we compare the behavior of LLMs against high- and low-quality human therapy. Our analysis based on Motivational Interviewing therapy reveals that LLMs often resemble behaviors more commonly exhibited in low-quality therapy rather than high-quality therapy, such as offering a higher degree of problem-solving advice when clients share emotions. However, unlike low-quality therapy, LLMs reflect significantly more upon clients' needs and strengths. Our findings caution that LLM therapists still require further research for consistent, high-quality care.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · In-context-learning LLMs code psychotherapy behaviours in therapy conversations; the abstract does not say whether the classifier was validated against human annotations.

**Решение:** =

---

### 386 · R12170

**Do LLMs Agree with Humans on Emotional Associations to Nonsense Words?**

2024 · Workshop on Cognitive Modeling and Computational Linguistics (CMCL) · audiovisual/conference talk, conference-paper · en · https://doi.org/10.18653/v1/2024.cmcl-1.7

Understanding human perception of nonsense words is helpful to devise product and character names that match their characteristics.Previous studies have suggested the usefulness of Large Language Models (LLMs) for estimating such human perception, but they did not focus on its emotional aspects.Hence, this study aims to elucidate the relationship of emotions evoked by nonsense words between humans and LLMs.Using a representative LLM, GPT-4, we reproduce the procedure of an existing study to analyze evoked emotions of humans for nonsense words.A positive correlation of 0.40 was found between the emotion intensity scores reproduced by GPT-4 and those manually annotated by humans.Although the correlation is not very high, this demonstrates that GPT-4 may agree with humans on emotional associations to nonsense words.Considering that the previous study reported that the correlation among human annotators was about 0.68 on average and that between a regression model trained on the annotations for real words and humans was 0.17, GPT-4's agreement with humans is notably strong.入力 未知語 [alse, roice, dw "joy"に最も関連している 最も関連していないもの 回答

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 emotion-intensity ratings correlated with human annotations, but the units are nonsense-word stimuli rather than psychological or clinical text.

**Решение:** =

---

### 387 · R12171

**Coding Open-Ended Responses using Pseudo Response Generation by Large Language Models**

2024 · North American Chapter of the Association for Computational Linguistics · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.18653/v1/2024.naacl-srw.26

Survey research using open-ended responses is an important method that contributes to the discovery of unknown issues and new needs. However, survey research generally requires time and cost-consuming manual data processing, indicating that it is difficult to analyze large dataset. To address this issue, we propose an LLM-based method to automate parts of the grounded theory approach (GTA), a representative approach of the qualitative data analysis. We generated and annotated pseudo open-ended responses, and used them as the training data for the coding procedures of GTA. Through evaluations, we showed that the models trained with pseudo open-ended responses are quite effective compared with those trained with manually annotated open-ended responses. We also demonstrate that the LLM-based approach is highly efficient and cost-saving compared to human-based approach.

**ИИ:** ? · обе модели · неясен конструкт · LLM-generated training data for coding open-ended survey responses, evaluated against manual codes; survey topic and whether the coding model is an LLM are unclear.

**Решение:** =

---

### 388 · R12179

**Surveying the Dead Minds: Historical-Psychological Text Analysis with Contextualized Construct Representation (CCR) for Classical Chinese**

2024 · Conference on Empirical Methods in Natural Language Processing (EMNLP) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2024.emnlp-main.151

In this work, we develop a pipeline for historical-psychological text analysis in classical Chinese. Humans have produced texts in various languages for thousands of years; however, most of the computational literature is focused on contemporary languages and corpora. The emerging field of historical psychology relies on computational techniques to extract aspects of psychology from historical corpora using new methods developed in natural language processing (NLP). The present pipeline, called Contextualized Construct Representations (CCR), combines expert knowledge in psychometrics (i.e., psychological surveys) with text representations generated via transformer-based language models to measure psychological constructs such as traditionalism, norm strength, and collectivism in classical Chinese corpora. Considering the scarcity of available data, we propose an indirect supervised contrastive learning approach and build the first Chinese historical psychology corpus (C-HI-PSY) to fine-tune pre-trained models. We evaluate the pipeline to demonstrate its superior performance compared with other approaches. The CCR method outperforms word-embedding-based approaches across all of our tasks and exceeds prompting with GPT-4 in most tasks. Finally, we benchmark the pipeline against objective, external data to further verify its validity.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: GPT-4 prompting is compared on psychological constructs in classical Chinese texts; unclear whether the evaluation labels are human annotations.); Sonnet -5 (нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM: CCR uses fine-tuned transformer encoders for measuring constructs in classical Chinese; GPT-4 is only a prompting baseline, with no clear human-coder agreement design.)

**Решение:** ?

---

### 389 · R1218

**A Cautious Integration With AI in the Clinic: A Standardized-Patient Pilot Study of ChatGPT's Reliability in Hamilton Depression Rating Scale Scoring.**

2026 · Alpha psychiatry · journal article, journalarticle, review · eng · https://doi.org/10.31083/ap51483

Background: Artificial intelligence (AI) integration offers significant potential to improve mental healthcare, however, the reliability of large language models (LLMs) in performing nuanced clinical tasks remains an important and largely unanswered question. This study aimed to evaluate ChatGPT’s performance in scoring the Hamilton Depression Rating Scale (HAMD-21) compared with expert raters using standardized patients (SPs). Methods: Three senior mental health experts created and portrayed scenarios for ten SPs representing diverse depressive symptom profiles. Recorded interviews were transcribed and used as input for ChatGPT-4o. HAMD-21 scores generated by ChatGPT were compared with those assigned by expert raters and with predefined script-based reference scores. Inter-rater reliability was assessed using intraclass correlation coefficient (ICC), and differences between raters were evaluated using Steiger’s tests. Results: ChatGPT and the expert raters achieved good-to-excellent reliability for total HAMD-21 scores (experts: ICC = 0.9921; ChatGPT: ICC = 0.9739). However, expert raters achieved perfect ICCs on 11 individual items, whereas ChatGPT achieved perfect agreement on only 2 items. Steiger’s test demonstrated that experts significantly outperformed ChatGPT on 10 individual items as well as on total scores (Z = 1.931, p = 0.0268). Qualitative review revealed that ChatGPT tended to overestimate scores on items related to insomnia and somatic symptoms (items 4–6 and 13) and frequently miscalculated total scores. Conclusions: ChatGPT demonstrated excellent agreement on total HAMD-21 scores in structured, text-based depression assessments, supporting the potential role of LLMs as adjunctive tools for standardized depression severity evaluation. However, item-level discrepancies and systematic scoring errors indicate that human oversight remains essential for clinically nuanced interpretation.

**ИИ:** + · обе модели · клиническая оценка · ChatGPT-4o scored HAMD-21 from interview transcripts and was compared with expert raters using ICC.

**Решение:** =

---

### 390 · R12192

**Scalable Qualitative Coding with LLMs: Chain-of-Thought Reasoning Matches Human Performance in Some Hermeneutic Tasks**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2401.15170

Qualitative coding, or content analysis, extracts meaning from text to discern quantitative patterns across a corpus of texts. Recently, advances in the interpretive abilities of large language models (LLMs) offer potential for automating the coding process (applying category labels to texts), thereby enabling human researchers to concentrate on more creative research aspects, while delegating these interpretive tasks to AI. Our case study comprises a set of socio-historical codes on dense, paragraph-long passages representative of a humanistic study. We show that GPT-4 is capable of human-equivalent interpretations, whereas GPT-3.5 is not. Compared to our human-derived gold standard, GPT-4 delivers excellent intercoder reliability (Cohen's $\kappa \geq 0.79$) for 3 of 9 codes, and substantial reliability ($\kappa \geq 0.6$) for 8 of 9 codes. In contrast, GPT-3.5 greatly underperforms for all codes ($mean(\kappa) = 0.34$; $max(\kappa) = 0.55$). Importantly, we find that coding fidelity improves considerably when the LLM is prompted to give rationale justifying its coding decisions (chain-of-thought reasoning). We present these and other findings along with a set of best practices for adapting traditional codebooks for LLMs. Our results indicate that for certain codebooks, state-of-the-art LLMs are already adept at large-scale content analysis. Furthermore, they suggest the next generation of models will likely render AI coding a viable option for a majority of codebooks.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-4 codebook coding compared with a human gold standard (kappa), but the socio-historical codes may not be psychological constructs.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: GPT-4 vs human qualitative coding agreement, but codes are socio-historical categories on humanistic passages, not a psychological or clinical construct.)

**Решение:** ?

---

### 391 · R12193

**Enhancing Emotional Generation Capability of Large Language Models via Emotional Chain-of-Thought**

2024 · arXiv (Cornell University) · preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2401.06836

Large Language Models (LLMs) have shown remarkable performance in various emotion recognition tasks, thereby piquing the research community's curiosity for exploring their potential in emotional intelligence. However, several issues in the field of emotional generation tasks remain unresolved, including human preference alignment and emotional generation assessment. In this paper, we propose the Emotional Chain-of-Thought (ECoT), a plug-and-play prompting method that enhances the performance of LLMs on various emotional generation tasks by aligning with human emotional intelligence guidelines. To assess the reliability of ECoT, we propose an automated model-based evaluation method called Emotional Generation Score (EGS). EGS incorporates Goleman's Emotional Intelligence Theory as a consensus of human experts, providing a new perspective on the evaluation of emotional generation tasks. Extensive experimental results demonstrate the effectiveness of ECoT and EGS. Further, we discuss the promise of LLMs in the field of emotional intelligence and present key insights into the LLMs with the ECoT in emotional generation tasks.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mainly a generation method, but it proposes an LLM-based scoring of emotional responses (EGS); unclear if it is checked against human ratings.

**Решение:** =

---

### 392 · R12196

**Utilizing Large Language Models for Psychological Assessment: Enhancing Suicide Risk Detection Through Social Media Analysis**

2024 · 2024 6th International Conference on Frontier Technologies of Information and Computer (ICFTIC) · conference, conference-paper, proceedings-article · en · https://doi.org/10.1109/icftic64248.2024.10913098

Mental health issues are increasingly prevalent due to the fast-paced lifestyle and rising work stress. Traditional psychological assessments face limitations due to resource scarcity and inefficiency. This paper presents a novel system using large language models (LLMs) to detect suicidal tendencies through social media analysis. Our system integrates prompt engineering and Retrieval-Augmented Generation (RAG) techniques to enhance detection accuracy. The architecture includes a knowledge retrieval-enhanced component and a judgment component, utilizing a fine-tuned LLM. Experiments with a Kaggle dataset demonstrate high performance, with consistent accuracy, precision, recall, and F1-Score across multiple runs. This system offers a promising solution to improve early psychological assessment and intervention, addressing the mental health resource gap. Future work aims to optimize the model and explore broader applications in psychological research.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · A fine-tuned LLM detects suicide risk on a Kaggle social-media dataset; unclear if labels are human-annotated or subreddit-derived.

**Решение:** =

---

### 393 · R12198

**Human-LLM Collaborative Construction of a Cantonese Emotion Lexicon**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2410.11526

Large Language Models (LLMs) have demonstrated remarkable capabilities in language understanding and generation. Advanced utilization of the knowledge embedded in LLMs for automated annotation has consistently been explored. This study proposed to develop an emotion lexicon for Cantonese, a low-resource language, through collaborative efforts between LLM and human annotators. By integrating emotion labels provided by LLM and human annotators, the study leveraged existing linguistic resources including lexicons in other languages and local forums to construct a Cantonese emotion lexicon enriched with colloquial expressions. The consistency of the proposed emotion lexicon in emotion extraction was assessed through modification and utilization of three distinct emotion text datasets. This study not only validates the efficacy of the constructed lexicon but also emphasizes that collaborative annotation between human and artificial intelligence can significantly enhance the quality of emotion labels, highlighting the potential of such partnerships in facilitating natural language processing tasks for low-resource languages. 13 pages

**ИИ:** ? · обе модели · другое · LLM and human annotators both label emotions for lexicon entries. LLM–human agreement may be reported, but the units are words, not psychological texts.

**Решение:** =

---

### 394 · R12208

**Enhancing Suicide Risk Detection with a Multisource Data Filtering and Fusion Optimization Framework (MDF-FOF)**

2024 · IEEE International Conference on Big Data (BigData) · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/bigdata62323.2024.10825363

Recently, with the popularity of social media platforms, the increase in suicide-related content has triggered great attention on automated suicide risk detection systems. This research proposes a natural language processing model based on RoBERTa, which aims to identify and classify suicide risks in social media posts. Our team propose a "Multisource data filtering and fusion optimization framework"(MDF-FOF), which effectively solves the problem of data imbalance by combining a large language model (LLM) with manual annotation to generate a balanced training sample set. In terms of model construction, we proposed a framework MDF-FOF that utilizes pre-trained RoBERTa for feature extraction and combines it with a self-built EmoBERT for soft label classification. Experimental results show that the recall rate of the proposed framework on the validation set is stable above 0.75, which is better than the existing methods and baseline models. It shows good robustness and excellent performance in tests on datasets from different sources. This study provides a reliable basic framework for multi-feature extraction of user posts in the future.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Main classifier is RoBERTa, but an LLM plus manual annotation labels suicide-risk posts; LLM–human labeling agreement may be reported.); Sonnet -5 (нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM: RoBERTa-based classifier for suicide risk; LLM only used for data augmentation/balancing, no LLM–human agreement evaluation.)

**Решение:** -

---

### 395 · R1221

**A Large-Scale Analysis of Student Behavior with Pedagogically Constrained LLM Tutors**

2026 · ACM Conference on Learning @ Scale · journalarticle, book · https://doi.org/10.1145/3774398.3811593

Large language models (LLMs) are increasingly being integrated into higher education as digital tutors, yet our understanding of how students actually behave when interacting with these systems remains limited. We present a large-scale empirical study of student behavioral patterns when interacting with an LLM-based educational system deployed across three computer science courses of varying difficulty levels. Our system uses prompt engineering and retrieval-augmented generation (RAG) to align LLM capabilities with educational goals, including a homework-detection mechanism that provides hints rather than direct answers. We collected over 12,000 conversations containing more than 20,000 student messages from 589 students and developed an LLM-based annotation framework validated with human agreement that evaluates student behaviors along four dimensions: self-regulated learning, help-seeking behaviors, cognitive engagement (grounded in the ICAP framework), and affective-motivational signals. Our analysis of 1,500 sampled conversations reveals that the majority of interactions exhibit low engagement quality (56.1%), with students rarely presenting prior work (30.0%), seldom reflecting on their learning states (8.2%), and frequently ignoring tutor hints (28.0%). We find statistically significant differences across course levels in self-regulated learning, help-seeking orientation, and cognitive engagement: entry-level students show more procedural focus and higher self-correction rates, while advanced students demonstrate greater conceptual depth but lower overall engagement with the tutoring system. These findings highlight gaps in students' ability to productively interact with LLM-based tutors, as well as the need for tutoring systems that better scaffold metacognition, adapt hint delivery, and maintain response reliability.

**ИИ:** разошлись — Opus + (проверка кодирования внутри исследования: LLM annotation of student messages for self-regulation, engagement and affective-motivational signals, checked against human annotation.); Sonnet ? (неясен конструкт: LLM annotates student tutor messages for self-regulation, engagement and affect, validated with human agreement; educational-psychology constructs, so it is unclear whether they count as psychological.)

**Решение:** +

---

### 396 · R12216

**Few-shot Dialogue Strategy Learning for Motivational Interviewing via Inductive Reasoning**

2024 · Annual Meeting of the Association for Computational Linguistics · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2024.findings-acl.782

We consider the task of building a dialogue system that can motivate users to adopt positive lifestyle changes: Motivational Interviewing.Addressing such a task requires a system that can infer how to motivate a user effectively.We propose DIIR (Dialogue Strategy Learning via Inductive Reasoning), a framework that is capable of learning and applying conversation strategies in the form of natural language inductive rules from expert demonstrations.Automatic and human evaluation on instruction-following large language models show natural language strategy descriptions discovered by DIIR can improve active listening skills, reduce unsolicited advice, and promote more collaborative and less authoritative responses, outperforming various demonstration utilization methods.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly MI response generation, but automatic MI-behaviour coding may use LLMs alongside human evaluation; LLM–human agreement possible.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM dialogue system learns MI strategies to generate responses; evaluation is of generation, not LLM coding against human labels.)

**Решение:** -

---

### 397 · R12224

**Adapting Mental Health Prediction Tasks for Cross-lingual Learning via Meta-Training and In-context Learning with Large Language Model**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2404.09045

Timely identification is essential for the efficient handling of mental health illnesses such as depression. However, the current research fails to adequately address the prediction of mental health conditions from social media data in low-resource African languages like Swahili. This study introduces two distinct approaches utilising model-agnostic meta-learning and leveraging large language models (LLMs) to address this gap. Experiments are conducted on three datasets translated to low-resource language and applied to four mental health tasks, which include stress, depression, depression severity and suicidal ideation prediction. we first apply a meta-learning model with self-supervision, which results in improved model initialisation for rapid adaptation and cross-lingual transfer. The results show that our meta-trained model performs significantly better than standard fine-tuning methods, outperforming the baseline fine-tuning in macro F1 score with 18\% and 0.8\% over XLM-R and mBERT. In parallel, we use LLMs' in-context learning capabilities to assess their performance accuracy across the Swahili mental health prediction tasks by analysing different cross-lingual prompting approaches. Our analysis showed that Swahili prompts performed better than cross-lingual prompts but less than English prompts. Our findings show that in-context learning can be achieved through cross-lingual transfer through carefully crafted prompt templates with examples and instructions.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM in-context classification of stress, depression and suicidal ideation in social-media posts; unclear whether dataset labels come from human annotators.

**Решение:** =

---

### 398 · R12230

**Spontaneous Speech-Based Suicide Risk Detection Using Whisper and Large Language Models**

2024 · Interspeech (USB) · journalarticle, text/article, conference-paper · en · https://doi.org/10.21437/interspeech.2024-1895

The early detection of suicide risk is important since it enables the intervention to prevent potential suicide attempts. This paper studies the automatic detection of suicide risk based on spontaneous speech from adolescents, and collects a Mandarin dataset with 15 hours of suicide speech from more than a thousand adolescents aged from ten to eighteen for our experiments. To leverage the diverse acoustic and linguistic features embedded in spontaneous speech, both the Whisper speech model and textual large language models (LLMs) are used for suicide risk detection. Both all-parameter finetuning and parameter-efficient finetuning approaches are used to adapt the pre-trained models for suicide risk detection, and multiple audio-text fusion approaches are evaluated to combine the representations of Whisper and the LLM. The proposed system achieves a detection accuracy of 0.807 and an F1-score of 0.846 on the test set with 119 subjects, indicating promising potential for real suicide risk detection applications. Accepted by Interspeech 2024

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Fine-tuned LLM detects adolescent suicide risk from speech transcripts; source of labels (self-report scale vs clinician rating) not stated.

**Решение:** =

---

### 399 · R12237

**Beyond words: a survey of online conversation metrics Πέρα από τις λέξεις: μια έρευνα για την αξιολόγηση συζητήσεων στο διαδίκτυο**

2024 · Athens University of Economics and Business · other/text · https://doi.org/10.26219/heal.aueb.4936

Η παρούσα διπλωματική εργασία εξετάζει τον τρόπο με τον οποίο αξιολογούνται οι διαδικτυακές συζητήσεις μέσω δύο προσεγγίσεων: μια συστηματική έρευνα των μετρικών αξιολόγησης και μια πειραματική σύγκριση μεταξύ ανθρώπων - αξιολογητών και Μεγάλων Γλωσσικών Μοντέλων (ΜΓΜ). Η βιβλιογραφική επισκόπηση εντοπίζει 22 διακριτές μετρικές, οι οποίες κατηγοριοποιούνται σε ομάδες Δομής και Λογικής, Κοινωνικής Δυναμικής, Συναισθηματικής και Συμπεριφορικής, και Δέσμευσης και Περιεχομένου. Ενώ οι μετρικές που βασίζονται στη δομή επιχειρημάτων και στην πραγματολογία αναδεικνύονται ως οι πιο συχνά μελετημένες, η ανάλυση αποκαλύπτει μια αυξανόμενη εστίαση στα κοινωνικά και συγκυριακά στοιχεία στην αξιολόγηση συνομιλιών στην πρόσφατη βιβλιογραφία.Η πειραματική μελέτη συγκρίνει τον τρόπο με τον οποίο οι άνθρωποι και τα ΜΓΜ αξιολογούν τις ίδιες διαδικτυακές συζητήσεις, αποκαλύπτοντας βασικές διαφορές στα πρότυπα αξιολόγησής τους. Οι ανθρώπινοι αξιολογητές επιδεικνύουν μεγαλύτερη ευαισθησία στην κοινωνική δυναμική, ιδίως στον εντοπισμό αρνητικών συμπεριφορών όπως η αγένεια και η κυριαρχία, ενώ τα ΜΓΜ υπερέχουν στον εντοπισμό δομικών στοιχείων αλλά συχνά παραβλέπουν αυτές τις λεπτές κοινωνικές ενδείξεις. Τα ευρήματα αναδεικνύουν ένα σημαντικό χάσμα μεταξύ υπολογιστικών και ανθρώπινων προσεγγίσεων στην αξιολόγηση συνομιλιών, γεγονός που υποδηλώνει ότι τα αποτελεσματικά πλαίσια αξιολόγησης πρέπει να εξισορροπούν και τις δύο οπτικές γωνίες για να αποτυπώσουν την πλήρη πολυπλοκότητα των διαδικτυακών συζητήσεων.Η παρούσα έρευνα συμβάλλει στην κατανόηση της αξιολόγησης των διαδικτυακών συνομιλιών με τη συστηματική χαρτογράφηση των υφιστάμενων μετρικών και την επίδειξη του τρόπου με τον οποίο οι διαισθητικές αξιολογήσεις των καθημερινών αναγνωστών διαφέρουν από τις υπολογιστικές προσεγγίσεις. Οι γνώσεις αυτές έχουν πρακτικές επιπτώσεις για την ανάπτυξη αποτελεσματικότερων εργαλείων αξιολόγησης συνομιλιών και τη βελτίωση των συστημάτων συντονισμού διαδικτυακών κοινοτήτων. This thesis examines how online discussions are evaluated through two approaches: a systematic survey of evaluation metrics and an experimental comparison between human evaluators and Large Language Models (LLMs). The literature review identifies 22 distinct metrics, categorized into Structure and Logic, Social Dynamics, Emotional and Behavioral, and Engagement and Content groups. While Argument Structure and Pragmatic-based metrics emerge as the most frequently studied, the analysis reveals an increasing focus on social and contextual elements in conversation evaluation across recent literature.The experimental study compares how humans and LLMs assess the same online discussions, revealing key differences in their evaluation patterns. Human evaluators demonstrate greater sensitivity to social dynamics, particularly in detecting negative behaviors like rudeness and dominance, while LLMs excel at identifying structural elements but often overlook these subtle social cues. The findings highlight a significant gap between computational and human approaches to conversation assessment, suggesting that effective evaluation frameworks must balance both perspectives to capture the full complexity of online discussions.This research contributes to our understanding of online conversation evaluation by systematically mapping existing metrics and demonstrating how everyday readers' intuitive assessments differ from computational approaches. These insights have practical implications for developing more effective conversation assessment tools and improving online community moderation systems.

**ИИ:** ? · обе модели · неясен конструкт · Humans and LLMs rate the same online discussions on metrics such as rudeness, dominance and emotion. Unclear if these count as psychological constructs.

**Решение:** =

---

### 400 · R12260

**Lost in translation? Not for Large Language Models: Automated divergent thinking scoring performance translates to non-English contexts**

2023 · Thinking Skills and Creativity · journalarticle, article, journal-article · en · https://doi.org/10.1016/j.tsc.2023.101414

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** + · обе модели · подсчёт методики · LLM automated scoring of divergent thinking responses in non-English languages, likely validated against human originality ratings.

**Решение:** =

---

### 401 · R12271

**Deployment and Evaluation of a Motivational-Interviewing Chatbot for Moving Smokers Towards the Decision to Quit and Distillation of Large Foundational Language Models for Generating MI Reflections**

2023 · TSpace (University of Toronto) · dissertation · https://utoronto.scholaris.ca/bitstreams/d6838dcb-ae23-4621-b319-eb65c6e9b871/download

Motivational Interviewing (MI) is a validated therapeutic approach that has been shown to help ambivalent people struggling with addiction move toward change. MI has been applied to many behaviours, including smoking cessation. If conversational agents could effectively apply MI, they may provide a scalable way to help more people access this therapy. Previous attempts to provide MI therapy through text-based conversational agents have typically employ scripted responses to client statements, but such non-specific responses have been shown to reduce effectiveness. A key technique in MI is to ask open-ended questions and then provide a reflection of the response to evoke contemplation in the client. Recent advances in Natural Language Processing provide a new way to create responses that are specific to client's statements, using a Transformer-based Language Model. We present the design, evolution and impact assessment of a chatbot that makes use of generated reflections, whose goal is to guide ambivalent smokers toward the decision to quit. Through four trials of 349 participants, we show that the chatbot significantly increases participants' confidence to quit smoking one week after the conversation compared to before the conversation (\textit{P}=.001). As a key part of the chatbot is the language model that produces reflection, and it is difficult and sometimes impractical to run a clinical bot with a corporation's proprietary model, we explore methods of model distillation to train smaller, more practical language models to generate MI-adherent reflections. We present a method for distilling the specific tasks of generating MI reflections from a Large Foundational Language Model (GPT-4) into smaller models. We show that GPT-4 can generate MI-adherent reflections near 100\% success and use output generated from that model to fine-tune the much smaller GPT-2 family as form of knowledge distillation. We also use GPT-4 as a zero-shot evaluator to classify the quality distilled student model outputs and validate that classifier with a triple human-review. We show that the GPT-2 small achieves an 83\% success rate on a hold-out test set and the GPT-2 XL achieves 90\% success. In addition, our GPT-4 zero-shot prompt evaluator achieves significantly high inter-rater reliability (.61 Cohen-Kappa) with triple-human review.

**ИИ:** + · обе модели · LLM-судья · GPT-4 zero-shot rated MI-adherence of reflections, validated against triple human review (Cohen's kappa .61).

**Решение:** =

---

### 402 · R12278

**DepreSym: A Depression Symptom Annotated Corpus and the Role of LLMs as Assessors of Psychological Markers**

2023 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2308.10758

Computational methods for depression detection aim to mine traces of depression from online publications posted by Internet users. However, solutions trained on existing collections exhibit limited generalisation and interpretability. To tackle these issues, recent studies have shown that identifying depressive symptoms can lead to more robust models. The eRisk initiative fosters research on this area and has recently proposed a new ranking task focused on developing search methods to find sentences related to depressive symptoms. This search challenge relies on the symptoms specified by the Beck Depression Inventory-II (BDI-II), a questionnaire widely used in clinical practice. Based on the participant systems' results, we present the DepreSym dataset, consisting of 21580 sentences annotated according to their relevance to the 21 BDI-II symptoms. The labelled sentences come from a pool of diverse ranking methods, and the final dataset serves as a valuable resource for advancing the development of models that incorporate depressive markers such as clinical symptoms. Due to the complex nature of this relevance annotation, we designed a robust assessment methodology carried out by three expert assessors (including an expert psychologist). Additionally, we explore here the feasibility of employing recent Large Language Models (ChatGPT and GPT4) as potential assessors in this complex task. We undertake a comprehensive examination of their performance, determine their main limitations and analyze their role as a complement or replacement for human annotators.

**ИИ:** + · обе модели · бенчмарк с метками людей · Benchmark of sentences annotated by experts for BDI-II symptom relevance; ChatGPT and GPT-4 tested as assessors against the human annotations.

**Решение:** =

---

### 403 · R12294

**CLARIN-Emo: Training Emotion Recognition Models Using Human Annotation and ChatGPT**

2023 · Lecture notes in computer science · journalarticle, conference-paper · en · https://doi.org/10.1007/978-3-031-35995-8_26

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests ChatGPT and human annotation of emotions on the same texts, so agreement may be reported.

**Решение:** =

---

### 404 · R12297

**Automatic Scoring of Dream Reports' Emotional Content with Large Language Models**

2023 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2302.14828

In the field of dream research, the study of dream content typically relies on the analysis of verbal reports provided by dreamers upon awakening from their sleep. This task is classically performed through manual scoring provided by trained annotators, at a great time expense. While a consistent body of work suggests that natural language processing (NLP) tools can support the automatic analysis of dream reports, proposed methods lacked the ability to reason over a report's full context and required extensive data pre-processing. Furthermore, in most cases, these methods were not validated against standard manual scoring approaches. In this work, we address these limitations by adopting large language models (LLMs) to study and replicate the manual annotation of dream reports, using a mixture of off-the-shelf and bespoke approaches, with a focus on references to reports' emotions. Our results show that the off-the-shelf method achieves a low performance probably in light of inherent linguistic differences between reports collected in different (groups of) individuals. On the other hand, the proposed bespoke text classification method achieves a high performance, which is robust against potential biases. Overall, these observations indicate that our approach could find application in the analysis of large dream datasets and may favour reproducibility and comparability of results across studies.

**ИИ:** разошлись — Opus ? (другое: Scores dream-report emotions against trained human annotators, but the "LLMs" used may be encoder models (e.g., RoBERTa); full text needed to check.); Sonnet + (кодирование по кодбуку: LLMs replicate manual annotation of emotions in dream reports, validated against trained human annotators' scoring.)

**Решение:** +

---

### 405 · R12321

**Procedures for training a ChatGPT-based classification for mental health screening in a college population**

2023 · Zenodo (CERN European Organization for Nuclear Research) · conferencepaper/none, conference-paper · en · https://doi.org/10.5281/zenodo.7955508

Providing mental health remains one of the greatest challenges in world health care. For proper screening standardized instruments are unavoidable, but expert clinical interviews are even more critical. However, this remains inaccessible to large human groups. Recent developments in artificial intelligence [1] can help to help close this gap, especially for college students for it is easier to access their needs, language and mores, and because young people tend to be less reluctant to interact with chat Apps in their mobile devices. What is lacking, and however offered here, is a the-oretically grounded framework for dealing with the relationship between human spontaneous re-sponses (explanations to personal challenges which include their cognitions and feelings) to ap-propriate, expert-guided inquiries, and the potentially diagnostic information contained in these utterances. Following Weiner's [2] 3-dimensional approach to extracting causal attributions from natural language (which have been shown in the scientific literature to be associated with depression and anxiety [3], optimism, and self-efficacy), here we describe procedures we used for 1) collecting these attributions in a sample of college alumni from a large university in central Mexico, 2) recog-nition of sociocognitive meaningful patterns on these utterances [4], 3) to classify them (with the help of mental health experts) into 10 fuzzy sets (8+2) and to estimate their associated statistical and computational criteria, and 4) to check the diagnostic potential of these cut-points and classifications for rapid automated mental health screening. We show some exemplars of the iterative process using chatGPT-3 to obtain stable and acceptable network parameters. The ultimate aim is to validate the model and apply this classifier on-the-fly (in a voluntary and automated way through chatGTP-4), during the admission process of about 40,000 freshmen by 2023, in order to propose and provide a theoretically grounded, and almost personalized, institutional support in mental health prevention.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · ChatGPT classifies students' causal-attribution utterances, with experts also classifying them; unclear if LLM–expert agreement is reported.

**Решение:** =

---

### 406 · R12333

**The Mechanical Psychologist: How Computational Techniques Can Aid Social Researchers in the Analysis of High-Stakes Conversation**

2023 · University of Liverpool Repository · text/thesis · https://doi.org/10.17638/03170404

Qualitative coding is an essential observational tool for describing behaviour in the social sciences. However, it traditionally relies on manual, time-consuming, and error-prone methods performed by humans. To overcome these issues, cross-disciplinary researchers are increasingly exploring computational methods such as Natural Language Processing (NLP) and Machine Learning (ML) to annotate behaviour automatically. Automated methods offer scalability, error reduction, and the discovery of increasingly subtle patterns in data compared to human effort alone (N. C. Chen et al., 2018). Despite promising advancements, concerns regarding generalisability, mistrust of automation, and value alignment between humans and machines persist (Friedberg et al., 2012; Grimmer et al., 2021; Jiang et al., 2021; R. Levitan &amp; Hirschberg, 2011; Mills, 2019; Nenkova et al., 2008; Rahimi et al., 2017; Yarkoni et al., 2021). This thesis investigates the potential of computational techniques, such as social signal processing, text mining, and machine learning, to streamline qualitative coding in the social sciences, focusing on two high-stakes conversational case studies. The first case study analyses political interviewing using a corpus of 691 interview transcripts from US news networks. Psychological behaviours associated with effective interviewing are measured and used to predict conversational quality through supervised machine learning. Feature engineering employs a Social Signal Processing (SSP) approach to extract latent behaviours from low-level social signals (Vinciarelli, Salamin, et al., 2009). Conversational quality, calculated from desired characteristics of interviewee speech, is validated by a human-rater study. The findings support the potential of computational approaches in qualitative coding while acknowledging challenges in interpreting low-level social signals. The second case study investigates the ability of machines to learn expert-defined behaviours from human annotation, specifically in detecting predatory behaviour in known cases of online child grooming. In this section, the author utilises 623 chat logs obtained from a US-based online watchdog, with expert annotators labelling a subset of these chat logs to train a large language model. The goal was to investigate the machine’s ability to detect eleven predatory behaviours based on expert annotations. The results show that the machine could detect several behaviours with as few as fifty labelled instances, but rare behaviours were frequently over-predicted. The author next implemented a collaborative human-AI approach to investigate the trade-off between human accuracy and machine efficiency. The results suggested that a human-in-the-loop approach could improve human efficiency and machine accuracy, achieving near-human performance on several behaviours approximately fifteen times faster than human effort alone. The conclusion emphasises the value of increased automation in social sciences while recognising the importance of social scientific expertise in cross-disciplinary re- search, especially when addressing real-world problems. It advocates for technology that augments and enhances human effort and expertise without replacing it entirely. This thesis acknowledges the challenges in interpreting computational signals and the importance of preserving human insight in qualitative coding. The thesis also highlights potential avenues for future research, such as refining computational methods for qualitative coding and exploring collaborative human-AI approaches to address the limitations of automated methods.

**ИИ:** разошлись — Opus ? (другое: A "large language model" was trained on expert labels of predatory behaviours in grooming chats; unclear whether it is generative or encoder-only.); Sonnet + (кодирование по кодбуку: Thesis case study trains a large language model on expert-annotated child-grooming chat logs to detect eleven predatory behaviours, evaluated against expert labels.)

**Решение:** +

---

### 407 · R12335

**Collecting Qualitative Data at Scale with Large Language Models: A Case Study**

2023 · arXiv (Cornell University) · preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2309.10187

Chatbots have shown promise as tools to scale qualitative data collection. Recent advances in Large Language Models (LLMs) could accelerate this process by allowing researchers to easily deploy sophisticated interviewing chatbots. We test this assumption by conducting a large-scale user study (n=399) evaluating 3 different chatbots, two of which are LLM-based and a baseline which employs hard-coded questions. We evaluate the results with respect to participant engagement and experience, established metrics of chatbot quality grounded in theories of effective communication, and a novel scale evaluating "richness" or the extent to which responses capture the complexity and specificity of the social context under study. We find that, while the chatbots were able to elicit high-quality responses based on established evaluation metrics, the responses rarely capture participants' specific motives or personalized examples, and thus perform poorly with respect to richness. We further find low inter-rater reliability between LLMs and humans in the assessment of both quality and richness metrics. Our study offers a cautionary tale for scaling and evaluating qualitative research with LLMs. 27 pages, 6 figures

**ИИ:** ? · обе модели · неясен конструкт · Reports LLM–human inter-rater reliability on interview response quality and richness; unclear whether these count as psychological constructs.

**Решение:** =

---

### 408 · R12351

**Application of Artificial Intelligence in Mental Healthcare: Generative Pre-trained Transformer 3 (GPT-3) and Cognitive Distortions**

2023 · Lecture notes in networks and systems · conference-paper · en · https://doi.org/10.1007/978-3-031-47454-5_16

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests GPT-3 detecting cognitive distortions in text, possibly compared against human labels.

**Решение:** =

---

### 409 · R12365

**Beyond human expertise: the promise and limitations of ChatGPT in suicide risk assessment.**

2023 · Frontiers in psychiatry · journal article, journalarticle, article · eng · https://doi.org/10.3389/fpsyt.2023.1213141

ChatGPT, an artificial intelligence language model developed by OpenAI, holds the potential for contributing to the field of mental health. Nevertheless, although ChatGPT theoretically shows promise, its clinical abilities in suicide prevention, a significant mental health concern, have yet to be demonstrated. To address this knowledge gap, this study aims to compare ChatGPT's assessments of mental health indicators to those of mental health professionals in a hypothetical case study that focuses on suicide risk assessment. Specifically, ChatGPT was asked to evaluate a text vignette describing a hypothetical patient with varying levels of perceived burdensomeness and thwarted belongingness. The ChatGPT assessments were compared to the norms of mental health professionals. The results indicated that ChatGPT rated the risk of suicide attempts lower than did the mental health professionals in all conditions. Furthermore, ChatGPT rated mental resilience lower than the norms in most conditions. These results imply that gatekeepers, patients or even mental health professionals who rely on ChatGPT for evaluating suicidal risk or as a complementary tool to improve decision-making may receive an inaccurate assessment that underestimates the actual suicide risk.

**ИИ:** + · обе модели · клиническая оценка · ChatGPT rated suicide risk and resilience in clinical vignettes; compared with mental health professionals' ratings of the same vignettes.

**Решение:** =

---

### 410 · R12379

**Evaluating the Efficacy of Supervised Learning vs. Large Language Models for Identifying Cognitive Distortions and Suicidal Risks in Chinese Social Media**

2023 · Research Square · journalarticle, preprint/article, preprint · en · https://doi.org/10.21203/rs.3.rs-3355484/v1

Abstract Large language models, particularly those akin to the rapidly progressing GPT series, are gaining traction for their expansive influence. While there is keen interest in their applicability within medical domains such as psychology, tangible explorations on real-world data remain scant. Concurrently, users on social media platforms are increasingly vocalizing personal sentiments; under specific thematic umbrellas, these sentiments often manifest as negative emotions, sometimes escalating to suicidal inclinations. Timely discernment of such cognitive distortions and suicidal risks is crucial to effectively intervene and potentially avert dire circumstances. Our study ventured into this realm by experimenting on two pivotal tasks: suicidal risk and cognitive distortion identification on Chinese social media platforms. Using supervised learning as a baseline, we examined and contrasted the efficacy of large language models via three distinct strategies: zero-shot, few-shot, and fine-tuning. Our findings revealed a discernible performance gap between the large language models and traditional supervised learning approaches, primarily attributed to the models' inability to fully grasp subtle categories. Notably, while GPT-4 outperforms its counterparts in multiple scenarios, GPT-3.5 shows significant enhancement in suicide risk classification after fine-tuning. To our knowledge, this investigation stands as the maiden attempt at gauging large language models on Chinese social media tasks. This study underscores the forward-looking and transformative implications of using large language models in the field of psychology. It lays the groundwork for future applications in psychological research and practice.

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT-3.5/GPT-4 classify cognitive distortions and suicide risk in Chinese social-media posts; the labels are presumably human-annotated.

**Решение:** =

---

### 411 · R12397

**ChatGPT for Suicide Risk Assessment on Social Media: Quantitative Evaluation of Model Performance, Potentials and Limitations**

2023 · Workshop on Computational Approaches to Subjectivity, Sentiment & Social Media Analysis (WASSA) · audiovisual/conference talk, journalarticle, preprint/article · en · https://doi.org/10.18653/v1/2023.wassa-1.16

This paper presents a novel framework for quantitatively evaluating the interactive ChatGPT model in the context of suicidality assessment from social media posts, utilizing the University of Maryland Reddit suicidality dataset. We conduct a technical evaluation of ChatGPT’s performance on this task using Zero-Shot and Few-Shot experiments and compare its results with those of two fine-tuned transformer-based models. Additionally, we investigate the impact of different temperature parameters on ChatGPT’s response generation and discuss the optimal temperature based on the inconclusiveness rate of ChatGPT. Our results indicate that while ChatGPT attains considerable accuracy in this task, transformer-based models fine-tuned on human-annotated datasets exhibit superior performance. Moreover, our analysis sheds light on how adjusting the ChatGPT’s hyperparameters can improve its ability to assist mental health professionals in this critical task.

**ИИ:** + · обе модели · клиническая оценка · ChatGPT rates suicide risk in Reddit posts from the UMD dataset, which has expert/crowd human annotations; compared against human labels.

**Решение:** =

---

### 412 · R12409

**The Capability of Large Language Models to Measure Psychiatric Functioning**

2023 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2308.01834

The current work investigates the capability of Large language models (LLMs) that are explicitly trained on large corpuses of medical knowledge (Med-PaLM 2) to predict psychiatric functioning from patient interviews and clinical descriptions without being trained to do so. To assess this, n = 145 depression and n =115 PTSD assessments and n = 46 clinical case studies across high prevalence/high comorbidity disorders (Depressive, Anxiety, Psychotic, trauma and stress, Addictive disorders) were analyzed using prompts to extract estimated clinical scores and diagnoses. Results demonstrate that Med-PaLM 2 is capable of assessing psychiatric functioning across a range of psychiatric conditions with the strongest performance being the prediction of depression scores based on standardized assessments (Accuracy range= 0.80 - 0.84) which were statistically indistinguishable from human clinical raters t(1,144) = 1.20; p = 0.23. Results show the potential for general clinical language models to flexibly predict psychiatric risk based on free descriptions of functioning from both patients and clinicians.

**ИИ:** + · обе модели · клиническая оценка · Med-PaLM 2 estimated depression/PTSD scores from interview transcripts, compared against scores from human clinical raters.

**Решение:** =

---

### 413 · R1241

**Can Large Language Models Assess Corporate Leaders’ Personalities from Their Video Interviews?**

2026 · Academy of Management Proceedings · conference-abstract · en · https://doi.org/10.5465/amproc.2026.16440abstract

Research in upper echelons theory faces a persistent trade-off between sample scalability and validity in measuring corporate leaders’ personalities. Recent advances in large language models offer a promising solution, yet conventional accuracy-based metrics are ill-suited for evaluating such latent psychological constructs. Drawing on psychometric practices, we assess LLM-based personality measures derived from video interview materials of 602 leaders in Chinese listed firms using test–retest reliability, validity, and an empirical criterion-validation framework. Our results show that LLM-based measures demonstrate acceptable reliability, convergent and discriminant validity, and relate to firm risk taking and performance. Overall, this study introduces a complementary and unobtrusive tool for large-scale measurement of leader personality.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM rates leader personality from interview material; unclear whether convergent validity uses human-coded ratings of the same interviews or other measures.

**Решение:** =

---

### 414 · R12434

**ChatCounselor: A Large Language Models for Mental Health Support**

2023 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2309.15461

This paper presents ChatCounselor, a large language model (LLM) solution designed to provide mental health support. Unlike generic chatbots, ChatCounselor is distinguished by its foundation in real conversations between consulting clients and professional psychologists, enabling it to possess specialized knowledge and counseling skills in the field of psychology. The training dataset, Psych8k, was constructed from 260 in-depth interviews, each spanning an hour. To assess the quality of counseling responses, the counseling Bench was devised. Leveraging GPT-4 and meticulously crafted prompts based on seven metrics of psychological counseling assessment, the model underwent evaluation using a set of real-world counseling questions. Impressively, ChatCounselor surpasses existing open-source models in the counseling Bench and approaches the performance level of ChatGPT, showcasing the remarkable enhancement in model capability attained through high-quality domain-specific data.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mainly a generation model, but GPT-4 judges counseling responses on seven metrics; unclear whether the judge was validated against human ratings.

**Решение:** =

---

### 415 · R12459

**Suicide Risk Assessments Through the Eyes of ChatGPT-3.5 Versus ChatGPT-4: Vignette Study (Preprint)**

2023 · JMIR Publications Inc. · posted-content · https://doi.org/10.2196/preprints.51232

BACKGROUND ChatGPT, a linguistic artificial intelligence (AI) model engineered by OpenAI, offers prospective contributions to mental health professionals. Although having significant theoretical implications, ChatGPT’s practical capabilities, particularly regarding suicide prevention, have not yet been substantiated. OBJECTIVE The study’s aim was to evaluate ChatGPT’s ability to assess suicide risk, taking into consideration 2 discernable factors—perceived burdensomeness and thwarted belongingness—over a 2-month period. In addition, we evaluated whether ChatGPT-4 more accurately evaluated suicide risk than did ChatGPT-3.5. METHODS ChatGPT was tasked with assessing a vignette that depicted a hypothetical patient exhibiting differing degrees of perceived burdensomeness and thwarted belongingness. The assessments generated by ChatGPT were subsequently contrasted with standard evaluations rendered by mental health professionals. Using both ChatGPT-3.5 and ChatGPT-4 (May 24, 2023), we executed 3 evaluative procedures in June and July 2023. Our intent was to scrutinize ChatGPT-4’s proficiency in assessing various facets of suicide risk in relation to the evaluative abilities of both mental health professionals and an earlier version of ChatGPT-3.5 (March 14 version). RESULTS During the period of June and July 2023, we found that the likelihood of suicide attempts as evaluated by ChatGPT-4 was similar to the norms of mental health professionals (n=379) under all conditions (average &lt;i&gt;Z&lt;/i&gt; score of 0.01). Nonetheless, a pronounced discrepancy was observed regarding the assessments performed by ChatGPT-3.5 (May version), which markedly underestimated the potential for suicide attempts, in comparison to the assessments carried out by the mental health professionals (average &lt;i&gt;Z&lt;/i&gt; score of –0.83). The empirical evidence suggests that ChatGPT-4’s evaluation of the incidence of suicidal ideation and psychache was higher than that of the mental health professionals (average &lt;i&gt;Z&lt;/i&gt; score of 0.47 and 1.00, respectively). Conversely, the level of resilience as assessed by both ChatGPT-4 and ChatGPT-3.5 (both versions) was observed to be lower in comparison to the assessments offered by mental health professionals (average &lt;i&gt;Z&lt;/i&gt; score of –0.89 and –0.90, respectively). CONCLUSIONS The findings suggest that ChatGPT-4 estimates the likelihood of suicide attempts in a manner akin to evaluations provided by professionals. In terms of recognizing suicidal ideation, ChatGPT-4 appears to be more precise. However, regarding psychache, there was an observed overestimation by ChatGPT-4, indicating a need for further research. These results have implications regarding ChatGPT-4’s potential to support gatekeepers, patients, and even mental health professionals’ decision-making. Despite the clinical potential, intensive follow-up studies are necessary to establish the use of ChatGPT-4’s capabilities in clinical practice. The finding that ChatGPT-3.5 frequently underestimates suicide risk, especially in severe cases, is particularly troubling. It indicates that ChatGPT may downplay one’s actual suicide risk level.

**ИИ:** + · обе модели · клиническая оценка · ChatGPT-3.5/4 rated suicide risk in clinical vignettes; compared with ratings from mental health professionals (n=379) on the same vignettes and scales.

**Решение:** =

---

### 416 · R12460

**Suicide Risk Assessments Through the Eyes of ChatGPT-3.5 Versus ChatGPT-4: Vignette Study.**

2023 · JMIR mental health · journal article, journalarticle, article · eng · https://doi.org/10.2196/51232

BACKGROUND: ChatGPT, a linguistic artificial intelligence (AI) model engineered by OpenAI, offers prospective contributions to mental health professionals. Although having significant theoretical implications, ChatGPT's practical capabilities, particularly regarding suicide prevention, have not yet been substantiated. OBJECTIVE: The study's aim was to evaluate ChatGPT's ability to assess suicide risk, taking into consideration 2 discernable factors-perceived burdensomeness and thwarted belongingness-over a 2-month period. In addition, we evaluated whether ChatGPT-4 more accurately evaluated suicide risk than did ChatGPT-3.5. METHODS: ChatGPT was tasked with assessing a vignette that depicted a hypothetical patient exhibiting differing degrees of perceived burdensomeness and thwarted belongingness. The assessments generated by ChatGPT were subsequently contrasted with standard evaluations rendered by mental health professionals. Using both ChatGPT-3.5 and ChatGPT-4 (May 24, 2023), we executed 3 evaluative procedures in June and July 2023. Our intent was to scrutinize ChatGPT-4's proficiency in assessing various facets of suicide risk in relation to the evaluative abilities of both mental health professionals and an earlier version of ChatGPT-3.5 (March 14 version). RESULTS: During the period of June and July 2023, we found that the likelihood of suicide attempts as evaluated by ChatGPT-4 was similar to the norms of mental health professionals (n=379) under all conditions (average Z score of 0.01). Nonetheless, a pronounced discrepancy was observed regarding the assessments performed by ChatGPT-3.5 (May version), which markedly underestimated the potential for suicide attempts, in comparison to the assessments carried out by the mental health professionals (average Z score of -0.83). The empirical evidence suggests that ChatGPT-4's evaluation of the incidence of suicidal ideation and psychache was higher than that of the mental health professionals (average Z score of 0.47 and 1.00, respectively). Conversely, the level of resilience as assessed by both ChatGPT-4 and ChatGPT-3.5 (both versions) was observed to be lower in comparison to the assessments offered by mental health professionals (average Z score of -0.89 and -0.90, respectively). CONCLUSIONS: The findings suggest that ChatGPT-4 estimates the likelihood of suicide attempts in a manner akin to evaluations provided by professionals. In terms of recognizing suicidal ideation, ChatGPT-4 appears to be more precise. However, regarding psychache, there was an observed overestimation by ChatGPT-4, indicating a need for further research. These results have implications regarding ChatGPT-4's potential to support gatekeepers, patients, and even mental health professionals' decision-making. Despite the clinical potential, intensive follow-up studies are necessary to establish the use of ChatGPT-4's capabilities in clinical practice. The finding that ChatGPT-3.5 frequently underestimates suicide risk, especially in severe cases, is particularly troubling. It indicates that ChatGPT may downplay one's actual suicide risk level.

**ИИ:** + · обе модели · клиническая оценка · ChatGPT rated suicide risk in clinical vignettes using the same scales as mental health professionals (n=379), and the two were compared.

**Решение:** =

---

### 417 · R12467

**Automatic Scoring of Creative Problem-Solving with Large Language Models: A Comparison of Originality and Quality Ratings**

2023 · PsyArXiv · preprint, ppr, posted-content · en · https://doi.org/10.31234/osf.io/g5qvf

Creative problem-solving is a naturalistic form of creative thinking involving the generation of solutions that are not only original but also of high quality (i.e., plausible and effective). Naturalistic tasks that evaluate both originality and quality are vital for the promotion of creativity in real-world settings—yet scoring such tasks remains challenging, due to costly human labor required to manually rate task responses. Past work has shown that large language models (LLMs) can be trained to predict human originality ratings of responses to tests of divergent thinking. In the present research, we extend this work to creative problem-solving, examining whether both originality and quality can be automatically scored for a naturalistic creativity task. We gathered data from 10 studies, amounting to 3,235 participants who completed a creative problem-solving task (CPST). We then fine-tuned two open-source LLMs, RoBERTa and GPT-2, to predict human ratings of originality and quality on the CPST, and compared their performance to two other scoring methods: elaboration (i.e., word count) and semantic distance. We found that RoBERTa and GPT-2 models predict solution quality (RoBERTa, r = .83; GPT-2, r = .83) better than solution originality (RoBERTa, r = .79; GPT-2, r = .80). Moreover, we found that both models outperformed elaboration and semantic distance methods and generalized to new CPST items not present in their training set. We therefore show for the first time that naturalistic creativity tasks can be automatically scored for both originality and quality. Open access is provided to the models and training data.

**ИИ:** ? · обе модели · другое · Fine-tuned GPT-2 and RoBERTa were compared with human creativity ratings, but GPT-2 is older than the review's GPT-3 cutoff for LLMs.

**Решение:** =

---

### 418 · R1248

**A Matter of Perspective: Contrasting User and Subject-Matter Experts’ Sensemaking of LLM Feedback on Instructional Discourse**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-29770-9_63

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -2 (люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает: No abstract; title suggests humans interpreting LLM feedback on classroom teaching discourse, which is educational and not human-LLM coding agreement.); Sonnet ? (нет аннотации: No abstract; LLM feedback on instructional discourse is educational, not clearly psychological, and may involve humans rating LLM feedback rather than coding.)

**Решение:** ?

---

### 419 · R12486

**Mental State-Based Dialogue System for Mental Health Care by Using GPT-3**

2023 · Lecture notes in networks and systems · conference-paper · en · https://doi.org/10.1007/978-981-99-3043-2_74

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; GPT-3 dialogue system may estimate users' mental states, possibly compared with human labels, but could be generation-only.

**Решение:** =

---

### 420 · R12488

**Advancing Mental Health Diagnostics: GPT-Based Method for Depression Detection**

2023 · Annual Conference of the Society of Instrument and Control Engineers (SICE) · journalarticle, conference, conference-paper · en · https://doi.org/10.23919/sice59929.2023.10354236

In this paper, we present a novel artificial intelligence (AI) application for depression detection, using advanced transformer networks to analyse clinical interviews. By incorporating simulated data to enhance traditional datasets, we overcome limitations in data protection and privacy, consequently improving the model’s performance. Our methodology employs BERT-based models, GPT-3.5, and ChatGPT-4, demonstrating state-of-the-art results in detecting depression from linguistic patterns and contextual information that significantly outperform previous approaches. Utilising the DAIC-WOZ and Extended-DAIC datasets, our study showcases the potential of the proposed application in revolutionising mental health care through early depression detection and intervention. Empirical results from various experiments highlight the efficacy of our approach and its suitability for real-world implementation. Furthermore, we acknowledge the ethical, legal, and social implications of AI in mental health diagnostics. Ultimately, our study underscores the transformative potential of AI in mental health diagnostics, paving the way for innovative solutions that can facilitate early intervention and improve patient outcomes.

**ИИ:** разошлись — Opus -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): GPT models detect depression in DAIC-WOZ interviews; the labels are PHQ-8 self-report scores, not human coding of the text.); Sonnet ? (неясно, кто ставил эталонные метки: GPT-3.5/GPT-4 depression detection on DAIC-WOZ; labels are likely PHQ-8 scores (criterion validity), but human coding reference is unclear.)

**Решение:** ?

---

### 421 · R12495

**ChatGPT vs. Human Annotators: A Comprehensive Analysis of ChatGPT for Text Annotation**

2023 · International Conference on Machine Learning and Applications · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/icmla58977.2023.00089

In recent years, the field of Natural Language Processing (NLP) has witnessed a groundbreaking transformation with the emergence of large language models (LLMs). ChatGPT stands out as an example among these LLM models captivating considerable public interest due to its impressive language generation capabilities. Researchers have been exploring the potential of using ChatGPT for data annotation tasks, aiming to discover more timesaving and cost-effective approaches. In this paper, we present a comprehensive evaluation of ChatGPT's data annotation capabilities across ten diverse datasets covering various subject areas and varied number of classes. To ensure the quality of our evaluation, we leveraged datasets that were previously annotated by human experts, providing a reliable benchmark for comparison. Through rigorous experimentation, we assessed the impact of different prompt strategies and model configurations on the annotation performance. Our findings emphasize the capability of ChatGPT in handling most data annotation tasks achieving average accuracy of 78.2% across various tasks. The banking queries dataset stands out with an impressive 95.9% accuracy, while emotions classification presents challenges, yielding an accuracy of 57.5%. Our evaluation also highlights the impact of prompt strategies on annotation performance and reveals significant performance differences between GPT models, with “gpt-4” achieving higher accuracy 79.2% on average compared to “gpt-3.5” of 74.6%. Our research provides valuable insights into the capabilities and limitations of ChatGPT in automating data annotation tasks.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: ChatGPT/GPT-4 annotation compared with human-expert labels across ten datasets, including emotion classification, a psychological construct.); Sonnet ? (неясен конструкт: General ChatGPT annotation across ten datasets vs human labels; includes an emotion classification dataset, but most tasks are non-psychological.)

**Решение:** +

---

### 422 · R12501

**Evaluating ChatGPT in Information Extraction: A Case Study of Extracting Cognitive Exam Dates and Scores**

2023 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.4520434

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · неясен конструкт · No abstract. ChatGPT pulls cognitive exam scores from clinical notes, likely checked against human annotation, but it may be information extraction, not construct rating.

**Решение:** =

---

### 423 · R12513

**A systematic review of social connection inventories**

2023 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/6ueyd

Social connection is vital to health and longevity. To date, a plethora of instruments exists to measure social connection, assessing a variety of aspects of social connection like loneliness, social isolation, or social support. For comparability and consistency of the published literature and for policy recommendations, consolidation and evaluation of the quality of measures is crucial. To answer the call for comparability, in Study 1a, we conducted a systematic review to create a database of social connection measures (N=xx) for its structure (N=xx), function (N=xx), and quality components (N=xx), spanning [YEAR] to [YEAR]; after which, in Study 1b, we assessed the heterogeneity of these existing measures through an item-content analysis relying both on human coders, as well as ChatGPT. We identified a total of XX item categories (XX for structure, XX for function, and XX for quality components) with a Jaccard index of XX for structure, XX for function, and XX for quality components. To answer the call for quality assessment, in Study 2a, we conducted a second systematic review on the measures found in Study 1a, creating a database documenting overall validity evidence. In Study 2b, we then evaluated the measurement properties using the COnsensus-based Standards for the Selection of health Measurement Instruments. We found the measurement properties to be [sufficient / insufficient / inconsistent / indeterminate], [sufficient / insufficient / inconsistent / indeterminate], and [sufficient / insufficient / inconsistent / indeterminate]; with [high/moderate/low/very low], [high/moderate/low/very low], and [high/moderate/low/very low] quality of evidence for the structure, function, and quality components, respectively. Finally, we identified the country of origin of the measures and the population groups with which they were developed, using data from Study 1a. Most of the measures were developed in [country name] (XX%) and for [add population characteristics] (XX%). [Overall conclusion].

**ИИ:** ? · обе модели · неясен конструкт · Systematic review of measures, but Study 1b has ChatGPT and human coders categorise social-connection questionnaire items; whether item text counts is unclear.

**Решение:** =

---

### 424 · R12527

**Comparing the Efficacy and Efficiency of Human and Generative AI: Qualitative Thematic Analyses (Preprint)**

2023 · JMIR Publications Inc. · posted-content · https://doi.org/10.2196/preprints.54482

BACKGROUND Qualitative methods are incredibly beneficial to the dissemination and implementation of new digital health interventions; however, these methods can be time intensive and slow down dissemination when timely knowledge from the data sources is needed in ever-changing health systems. Recent advancements in generative artificial intelligence (GenAI) and their underlying large language models (LLMs) may provide a promising opportunity to expedite the qualitative analysis of textual data, but their efficacy and reliability remain unknown. OBJECTIVE The primary objectives of our study were to evaluate the consistency in themes, reliability of coding, and time needed for inductive and deductive thematic analyses between GenAI (ie, ChatGPT and Bard) and human coders. METHODS The qualitative data for this study consisted of 40 brief SMS text message reminder prompts used in a digital health intervention for promoting antiretroviral medication adherence among people with HIV who use methamphetamine. Inductive and deductive thematic analyses of these SMS text messages were conducted by 2 independent teams of human coders. An independent human analyst conducted analyses following both approaches using ChatGPT and Bard. The consistency in themes (or the extent to which the themes were the same) and reliability (or agreement in coding of themes) between methods were compared. RESULTS The themes generated by GenAI (both ChatGPT and Bard) were consistent with 71% (5/7) of the themes identified by human analysts following inductive thematic analysis. The consistency in themes was lower between humans and GenAI following a deductive thematic analysis procedure (ChatGPT: 6/12, 50%; Bard: 7/12, 58%). The percentage agreement (or intercoder reliability) for these congruent themes between human coders and GenAI ranged from fair to moderate (ChatGPT, inductive: 31/66, 47%; ChatGPT, deductive: 22/59, 37%; Bard, inductive: 20/54, 37%; Bard, deductive: 21/58, 36%). In general, ChatGPT and Bard performed similarly to each other across both types of qualitative analyses in terms of consistency of themes (inductive: 6/6, 100%; deductive: 5/6, 83%) and reliability of coding (inductive: 23/62, 37%; deductive: 22/47, 47%). On average, GenAI required significantly less overall time than human coders when conducting qualitative analysis (20, SD 3.5 min vs 567, SD 106.5 min). CONCLUSIONS The promising consistency in the themes generated by human coders and GenAI suggests that these technologies hold promise in reducing the resource intensiveness of qualitative thematic analysis; however, the relatively lower reliability in coding between them suggests that hybrid approaches are necessary. Human coders appeared to be better than GenAI at identifying nuanced and interpretative themes. Future studies should consider how these powerful technologies can be best used in collaboration with human coders to improve the efficiency of qualitative research in hybrid approaches while also mitigating potential ethical risks that they may pose.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT/Bard coded the same SMS units as human coders and agreement was reported, but unclear whether intervention-message themes are psychological constructs.

**Решение:** =

---

### 425 · R12528

**Can an algorithm tell how spiritual you are? Measuring spirituality from text using Generative Pre-trained Transformers**

2023 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/bqnmk

Text analysis is a form of psychological assessment that involves converting qualitative information (text) into quantitative data. We tested whether automated text analysis using Generative Pre-trained Transformers (GPTs) can match the “gold standard” of manual text analysis, even when assessing a highly nuanced construct like spirituality. In Study 1, N = 2,199 US undergraduates wrote about their goals (N = 6,597 texts) and completed self-reports of spirituality and theoretically related constructs (religiousness and mental health). In Study 2, N = 357 community adults wrote short essays (N = 714 texts) and completed trait self-reports, five weeks of daily diaries, and behavioral measures of spirituality. Trained research assistants and GPTs then coded the texts for spirituality. The GPTs performed just as well as human raters. Human- and GPT-generated scores were remarkably consistent and showed equivalent associations with other measures of spirituality and theoretically related constructs. GPTs can match the gold standard set by human raters, even in sophisticated forms of text analysis, but require a fraction of the time and labor.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT and trained research assistants coded spirituality in the same participant texts, and the abstract reports how consistent their scores were.

**Решение:** =

---

### 426 · R12530

**Evaluating the performance of ChatGPT in differential diagnosis of neurodevelopmental disorders: A pediatricians-machine comparison**

2023 · Psychiatry Research · article · en · https://doi.org/10.1016/j.psychres.2023.115351

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; ChatGPT vs pediatricians diagnosing neurodevelopmental cases, possibly from vignettes; unclear if this counts as human-coded text agreement.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): ChatGPT diagnosing neurodevelopmental disorders from clinical cases, compared with pediatricians; this is diagnostic accuracy, not coding or rating of text against human labels.)

**Решение:** ?

---

### 427 · R12544

**LLM-Assisted Content Analysis: Using Large Language Models to Support Deductive Coding**

2023 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2306.14924

Deductive coding is a widely used qualitative research method for determining the prevalence of themes across documents. While useful, deductive coding is often burdensome and time consuming since it requires researchers to read, interpret, and reliably categorize a large body of unstructured text documents. Large language models (LLMs), like ChatGPT, are a class of quickly evolving AI tools that can perform a range of natural language processing and reasoning tasks. In this study, we explore the use of LLMs to reduce the time it takes for deductive coding while retaining the flexibility of a traditional content analysis. We outline the proposed approach, called LLM-assisted content analysis (LACA), along with an in-depth case study using GPT-3.5 for LACA on a publicly available deductive coding data set. Additionally, we conduct an empirical benchmark using LACA on 4 publicly available data sets to assess the broader question of how well GPT-3.5 performs across a range of deductive coding tasks. Overall, we find that GPT-3.5 can often perform deductive coding at levels of agreement comparable to human coders. Additionally, we demonstrate that LACA can help refine prompts for deductive coding, identify codes for which an LLM is randomly guessing, and help assess when to use LLMs vs. human coders for deductive coding. We conclude with several implications for future practice of deductive coding and related research methods.

**ИИ:** ? · обе модели · неясен конструкт · GPT-3.5 deductive coding compared with human coders on four public datasets; unclear whether any of the coded constructs are psychological.

**Решение:** =

---

### 428 · R12549

**SIGHT: A Large Annotated Dataset on Student Insights Gathered from Higher Education Transcripts**

2023 · Workshop on Innovative Use of NLP for Building Educational Applications · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.18653/v1/2023.bea-1.27

Lectures are a learning experience for both students and teachers. Students learn from teachers about the subject material, while teachers learn from students about how to refine their instruction. However, online student feedback is unstructured and abundant, making it challenging for teachers to learn and improve. We take a step towards tackling this challenge. First, we contribute a dataset for studying this problem: SIGHT is a large dataset of 288 math lecture transcripts and 15,784 comments collected from the Massachusetts Institute of Technology OpenCourseWare (MIT OCW) YouTube channel. Second, we develop a rubric for categorizing feedback types using qualitative analysis. Qualitative analysis methods are powerful in uncovering domain-specific insights, however they are costly to apply to large data sources. To overcome this challenge, we propose a set of best practices for using large language models (LLMs) to cheaply classify the comments at scale. We observe a striking correlation between the model's and humans' annotation: Categories with consistent human annotations (&gt;$0.9$ inter-rater reliability, IRR) also display higher human-model agreement (&gt;$0.7$), while categories with less consistent human annotations ($0.7$-$0.8$ IRR) correspondingly demonstrate lower human-model agreement ($0.3$-$0.5$). These techniques uncover useful student feedback from thousands of comments, costing around $\$0.002$ per comment. We conclude by discussing exciting future directions on using online student feedback and improving automated annotation techniques for qualitative research. First two authors contributed equally. In the Proceedings of Innovative Use of NLP for Building Educational Applications 2023. The code and data are open-sourced here: https://github.com/rosewang2008/sight

**ИИ:** разошлись — Opus ? (неясен конструкт: An LLM applies a qualitative rubric to student comments and is compared with human coders, but the feedback categories are educational and only partly psychological (e.g., confusion).); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM–human agreement is reported, but the task is categorizing YouTube lecture comments into educational feedback types, not a psychological or clinical construct.)

**Решение:** ?

---

### 429 · R1256

**Two-Stage Extraction of Clinical Course Information From Psychiatric Discharge Summaries Using Fine-Tuned Large Language Models: Cross-Validation Study.**

2026 · JMIR formative research · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.2196/94454

Abstract Background Clinical course information, including disease onset, episode recurrence, and hospitalization history, is essential for psychiatric care and research. However, these data are embedded in unstructured clinical narratives with substantial linguistic variability, making manual extraction labor-intensive and rule-based extraction difficult to scale. Fine-tuned large language models (LLMs) may flexibly extract such information from privacy-sensitive psychiatric records. Objective This study aimed to evaluate the performance of LLMs for automatically extracting temporal and clinical course information from psychiatric discharge summaries. Methods We analyzed 500 psychiatric discharge summaries from the Integrated Medical Database of National Taiwan University Hospital. A psychiatrist and a natural language processing researcher manually annotated clinical events and temporal information. Four open-source LLMs (LLaMA, MentaLLaMA, OpenBioLLM, and Mistral) were fine-tuned using low-rank adaptation and evaluated using 10-fold cross-validation. A 2-stage framework was developed in which sentence-level extraction of clinical events and temporal information was followed by chart-level prediction of 4 clinical course features: first-episode onset time, episode count, number of psychiatric hospitalizations, and most recent hospitalization. Performance was assessed using precision, recall, F1-score, accuracy, mean absolute error (MAE), and bootstrap significance testing. Results A total of 12,947 sentences were extracted from 500 discharge summaries, yielding 7177 clinical event annotations and 4842 temporal annotations. At the sentence level, Mistral achieved the highest F1-scores for clinical event extraction, including symptom/episode detection (0.925, 95% CI 0.920‐0.930), hospitalization detection (0.944, 95% CI 0.934‐0.952), and remission/response detection (0.867, 95% CI 0.851‐0.883). Mistral also achieved the highest F1-scores for most temporal information categories, including age expressions (0.983, 95% CI 0.973‐0.993), relative time expressions (0.953, 95% CI 0.944‐0.963), duration expressions (0.976, 95% CI 0.962‐0.987), and vague temporal expressions (0.888, 95% CI 0.871‐0.905). At the chart level, the proposed 2-stage framework showed the clearest benefit for first-episode onset prediction. Using the 2-stage framework, Mistral achieved the highest point estimate for onset accuracy (0.772), although its performance did not significantly differ from that of LLaMA using the same framework (0.744; bootstrap P=.26). For onset prediction, the 2-stage framework significantly outperformed the direct and joint extraction approaches across all evaluated models (all bootstrap P≤.002). For other chart-level features, the best-performing approach varied: using the 2-stage framework, Mistral achieved the highest episode count accuracy (0.624; MAE=0.428); using the direct approach, LLaMA achieved the highest hospitalization count accuracy (0.692; MAE=0.379); and using the 2-stage framework, OpenBioLLM achieved the highest most recent hospitalization accuracy (0.868; F1-score=0.617). Conclusions Fine-tuned, locally deployable, open-source LLMs can extract temporal and longitudinal disease course information from psychiatric discharge summaries. The 2-stage framework was most beneficial for first-episode onset prediction and performed competitively across other chart-level features, supporting the use of LLMs to transform heterogeneous psychiatric narratives into structured data for research and decision support.

**ИИ:** ? · обе модели · неясен конструкт · LLMs extract psychiatric symptom/episode and course events from discharge summaries against psychiatrist annotations; may be information extraction rather than psychological coding.

**Решение:** =

---

### 430 · R1257

**Using Large Language Models to Measure Symptom Severity Scores in Patients At-Risk for Schizophrenia.**

2026 · Schizophrenia bulletin · journal article, journalarticle, article · eng · https://doi.org/10.1093/schbul/sbag084

Abstract Background and Hypothesis Patients who are at clinical high risk (CHR) for schizophrenia need close monitoring of their symptoms to inform appropriate treatments. The Brief Psychiatric Rating Scale (BPRS) is a validated, commonly used research tool for measuring symptoms in patients with schizophrenia and other psychotic disorders; however, it is not commonly used in clinical practice as it requires a lengthy structured interview. We hypothesized we could utilize large language models (LLMs) to predict BPRS scores from clinical interview transcripts. Study Design We used LLMs to predict BPRS scores from transcripts in 409 CHR patients from the Accelerating Medicines Partnership Schizophrenia cohort. Study Results Despite the interviews not being specifically structured to measure the BPRS, the zero-shot performance of the LLM predictions compared to the true assessment (median concordance: 0.84, Intraclass Correlation Coefficient [ICC]: 0.73) approaches human inter- and intra-rater reliability. We further demonstrate that LLMs have expansive potential to improve and standardize the assessment of CHR patients via their accuracy in assessing the BPRS in foreign languages (median concordance: 0.88, ICC: 0.70), and integrating longitudinal information as one-shot or few-shot learning. Conclusions LLMs may present a promising pathway to extract symptom severity scores from clinical interviews for improved monitoring of CHR patients.

**ИИ:** + · обе модели · клиническая оценка · The LLM rated BPRS symptom severity from clinical interview transcripts and was compared with clinician-rated BPRS scores (ICC 0.73).

**Решение:** =

---

### 431 · R12582

**Language Models (Mostly) Do Not Consider Emotion Triggers When Predicting Emotion**

2023 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2311.09602

Situations and events evoke emotions in humans, but to what extent do they inform the prediction of emotion detection models? This work investigates how well human-annotated emotion triggers correlate with features that models deemed salient in their prediction of emotions. First, we introduce a novel dataset EmoTrigger, consisting of 900 social media posts sourced from three different datasets; these were annotated by experts for emotion triggers with high agreement. Using EmoTrigger, we evaluate the ability of large language models (LLMs) to identify emotion triggers, and conduct a comparative analysis of the features considered important for these tasks between LLMs and fine-tuned models. Our analysis reveals that emotion triggers are largely not considered salient features for emotion prediction models, instead there is intricate interplay between various features and the task of emotion detection. NAACL 2024 Camera Ready

**ИИ:** + · обе модели · бенчмарк с метками людей · Experts annotated emotion triggers in 900 social media posts, and LLMs were evaluated against those labels on identifying emotion triggers.

**Решение:** =

---

### 432 · R12587

**Identifying Early Maladaptive Schemas from Mental Health Question Texts**

2023 · Conference on Empirical Methods in Natural Language Processing · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2023.findings-emnlp.792

In Psychotherapy, {maladaptive schemas}-- negative perceptions that {an individual has of the self, others, or the world that endure despite objective reality}-- often lead to resistance to treatments and relapse of mental health issues such as depression, anxiety, panic attacks etc. Identification of early maladaptive schemas (EMS) is thus a crucial step during Schema Therapy-based counseling sessions, where patients go through a detailed and lengthy EMS questionnaire. However, such an approach is not practical in "offline" counseling scenarios, such as community QA forums which are gaining popularity for people seeking mental health support. In this paper, we investigate both LLM (Large Language Models) and non-LLM approaches for identifying EMS labels using resources from Schema Therapy. Our evaluation indicates that recent LLMs can be effective for identifying EMS but their predictions lack explainability and are too sensitive to precise `prompts'. Both LLM and non-LLM methods are unable to reliably address the {null} cases, i.e. cases with no EMS labels. However, we posit that the two approaches show complementary properties and together, they can be used to further devise techniques for EMS identification.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: LLMs label early maladaptive schemas in mental-health forum questions; the evaluation implies human-annotated EMS labels as the reference.); Sonnet ? (неясно, кто ставил эталонные метки: LLMs identify early maladaptive schemas in mental health QA posts; the abstract doesn't say whether the reference labels come from human annotators, so check the full text.)

**Решение:** +

---

### 433 · R12606

**Harnessing AI to Optimize Thought Records and Facilitate Cognitive Restructuring in Smartphone CBT: An Exploratory Study**

2023 · Cognitive Therapy and Research · journalarticle, article · en · https://doi.org/10.1007/s10608-023-10411-7

Abstract Background Effective cognitive restructuring (CR) requires identification of automatic thoughts that underlie experienced emotions. However, accurate recording of thoughts and emotions is challenging when CR is provided in internet cognitive-behavior therapy (iCBT). This study investigated the potential use of the artificial intelligence (AI) including the natural language processing (NLP) to facilitate CR offered in iCBT. Methods We applied the Japanese Text-to-Text Transfer Transformer (T5), one of the most advanced Large Language Models for the NLP,to records of thought-feeling pairs provided by participants in two randomized controlled trials of iCBT. We conducted threefold cross-validated prediction of self-reported feelings based on recorded thoughts. We examined the validity of the predictions by checking them against the human expert judgments and by the efficacy when the thought records were subjected to CR. Results 1626 participants provided 4369 though-feeling records. The overall prediction accuracy was 73.5%. The self-reported feelings matched the human expert judgments more frequently when they were correctly predicted by the T5 than not (90% vs 37.5%, 95%CI of difference: 34.8 to 70.2%). When subjected to CR, the correctly predicted thought-feeling pairs led to greater reductions in negative feelings than the incorrectly predicted pairs (− 1.54 vs − 1.43 on a scale of 0 to 5, 95%CI of difference: 0.03 to 0.19). Conclusions A new CR module of an iCBT application can incorporate this model and advise the users to revisit and revise their automatic thoughts to reflect their feelings more accurately. Whether such an iCBT application can ultimately lead to greater reductions in depression is to be examined in a future randomized trial.

**ИИ:** ? · обе модели · другое · Fine-tuned Japanese T5 (encoder-decoder, borderline LLM) predicts feelings mainly against self-report, but expert judgments were also compared.

**Решение:** =

---

### 434 · R1261

**HPSU: A Benchmark for Human-Level Perception in Real-World Spoken Speech Understanding**

2026 · Proceedings of the AAAI Conference on Artificial Intelligence · journalarticle, conference, preprint/article · en · https://doi.org/10.1609/aaai.v40i37.40419

Recent advances in Speech Large Language Models (Speech LLMs) have led to great progress in speech understanding tasks such as Automatic Speech Recognition (ASR) and Speech Emotion Recognition (SER). However, whether these models can achieve human-level auditory perception, particularly in terms of their ability to comprehend latent intentions and implicit emotions in real-world spoken language, remains underexplored. To this end, we introduce the Human-level Perception in Spoken Speech Understanding (HPSU), a new benchmark for fully evaluating the human-level perceptual and understanding capabilities of Speech LLMs. HPSU comprises over 20,000 expert-validated spoken language understanding samples in English and Chinese. It establishes a comprehensive evaluation framework by encompassing a spectrum of tasks, ranging from basic speaker attribute recognition to complex inference of latent intentions and implicit emotions. To address the issues of data scarcity and high cost of manual annotation in real-world scenarios, we developed a semi-automatic annotation process. This process fuses audio, textual, and visual information to enable precise speech understanding and labeling, thus enhancing both annotation efficiency and quality. We systematically evaluate various open-source and proprietary Speech LLMs. The results demonstrate that even top-performing models still fall considerably short of human capabilities in understanding genuine spoken interactions. Consequently, HPSU will be useful for guiding the development of Speech LLMs toward human-level perception and cognition. Accepted by AAAI 2026

**ИИ:** разошлись — Opus ? (другое: Benchmark tests Speech LLMs on implicit emotion/intent against expert-validated labels, but input is audio and labels are semi-automatic.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Speech LLM benchmark of audio understanding (speaker attributes, intent, emotion); audio-based general perception, not coding of psychological or clinical text against human coders.)

**Решение:** -

---

### 435 · R12613

**Contextual Emotion Estimation from Image Captions**

2023 · International Conference on Affective Computing and Intelligent Interaction (ACII) · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/acii59096.2023.10388198

Emotion estimation in images is a challenging task, typically using computer vision methods to directly estimate people's emotions using face, body pose and contextual cues. In this paper, we explore whether Large Language Models (LLMs) can support the contextual emotion estimation task, by first captioning images, then using an LLM for inference. First, we must understand: how well do LLMs perceive human emotions? And which parts of the information enable them to determine emotions? One initial challenge is to construct a caption that describes a person within a scene with information relevant for emotion perception. Towards this goal, we propose a set of natural language descriptors for faces, bodies, interactions, and environments. We use them to manually generate captions and emotion annotations for a subset of 331 images from the EMOTIC dataset. These captions offer an interpretable representation for emotion estimation, towards understanding how elements of a scene affect emotion perception in LLMs and beyond. Secondly, we test the capability of a large language model to infer an emotion from the resulting image captions. We find that GPT-3.5, specifically the text-davinci-003 model, provides surprisingly reasonable emotion predictions consistent with human annotations, but accuracy can depend on the emotion concept. Overall, the results suggest promise in the image captioning and LLM approach. Accepted to ACII 2023. Project page: http://rosielab.github.io/emotion-captions/

**ИИ:** ? · обе модели · неясен конструкт · GPT-3.5 infers emotions from image captions and is compared with human emotion annotations; unclear whether captions count as psychological text.

**Решение:** =

---

### 436 · R1262

**Beyond human agreement: Validating large language model ratings of psychological concern from narratives**

2026 · OSF Preprints (OSF Preprints) · preprint

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests LLM ratings of psychological concern in narratives, possibly compared with human raters, but the validation approach is unclear.

**Решение:** =

---

### 437 · R12642

**Multiple Regression Analysis on the Factors of Onset and Treatment Initiation of Restrictive-type Anorexia Nervosa: Using YouTube comments and ChatGPT**

2023 · Korean Association For Learner-Centered Curriculum And Instruction · journalarticle, article · en · https://doi.org/10.22251/jlcci.2023.23.18.815

Objectives This study aimed to predict the onset of Restrictive Anorexia Nervosa (AN-R) and identify influential symptom variables for treatment initiation. Methods We collected 333 comments from Korean YouTube videos related to eating disorders, focusing on AN-R. Through ChatGPT assessment, we extracted 1,210 symptomatic pieces of evidence, categorizing them into psychological, physical, behavioral, and social symptoms. Regression analysis at α=0.5 revealed a negative correlation between psychological and physical symptoms. Results Psychological symptoms were highest at the early onset of AN-R, gradually decreasing as physical symptoms emerged. Self-perception of symptom severity was primarily influenced by physical and social symptoms, especially appearance changes. Treatment initiation showed a positive correlation with appearance changes and a negative correlation with psychological symptoms. Conclusions Our findings confirm that AN-R onset can be predicted when physical symptoms appear after progressing psychological symptoms, highlighting the dominant influence of psychological symptoms in treatment initiation.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · ChatGPT coded anorexia symptoms in YouTube comments; abstract doesn't say whether its coding was checked against human coders.

**Решение:** =

---

### 438 · R12675

**Conversational Breakdown Detector for a Motivational Interviewing Conversational Agent**

2023 · The iJournal Student Journal of the Faculty of Information · journalarticle, article, journal-article · en · https://doi.org/10.33137/ijournal.v9i1.42237

A conversational breakdown in human-chatbot interaction refers to a disruption or failure in the communicative flow between the human user and the chatbot. To recover a disrupted conversation, the first step is to detect the breakdown. Researchers have proposed methods using supervised learning and semi-supervised learning in dialogue systems to achieve the goal of detecting conversational breakdown. However, few studies have focused on detecting breakdowns in automated therapeutic conversations, especially conversations led by motivational interviewing chatbots. The presence of conversational breakdowns has negative impacts on the human-chatbot interaction, such as frustration, dissatisfaction, or loss of trust. This gap suggests a need to build a robust and efficient conversational breakdown detector that recognizes interruptions during the conversation. Conversational breakdown detection paves the way for further action to recover conversations. In this paper, I develop a novel, unifying framework called “CIMIC” for characterizing the conversational breakdowns of “MIBot,” a motivational interviewing conversational agent for smoking cessation. I collect 200 pieces of conversational data through Prolific and annotate them using the CIMIC framework with a group of four trained annotators. The annotated dataset is then applied as the training set to fine-tune GPT-3 models to build a conversational breakdown detector for the MIBot.

**ИИ:** ? · обе модели · неясен конструкт · Fine-tuned GPT-3 detects breakdowns in MI chatbot dialogues using human annotations; unclear whether breakdown counts as a psychotherapy-process construct.

**Решение:** =

---

### 439 · R12679

**Supporting Qualitative Analysis with Large Language Models: Combining Codebook with GPT-3 for Deductive Coding**

2023 · ACM International Conference on Intelligent User Interfaces (IUI) · journalarticle, book, text/article · en · https://doi.org/10.1145/3581754.3584136

Qualitative analysis of textual contents unpacks rich and valuable information by assigning labels to the data. However, this process is often labor-intensive, particularly when working with large datasets. While recent AI-based tools demonstrate utility, researchers may not have readily available AI resources and expertise, let alone be challenged by the limited generalizability of those task-specific models. In this study, we explored the use of large language models (LLMs) in supporting deductive coding, a major category of qualitative analysis where researchers use pre-determined codebooks to label the data into a fixed set of codes. Instead of training task-specific models, a pre-trained LLM could be used directly for various tasks without fine-tuning through prompt learning. Using a curiosity-driven questions coding task as a case study, we found, by combining GPT-3 with expert-drafted codebooks, our proposed approach achieved fair to substantial agreements with expert-coded results. We lay out challenges and opportunities in using LLMs to support qualitative coding and beyond. 28th International Conference on Intelligent User Interfaces (IUI '23 Companion), March 27--31, 2023, Sydney, NSW, Australia

**ИИ:** ? · обе модели · неясен конструкт · GPT-3 applies an expert codebook to curiosity-driven questions and is compared with expert coding; unclear whether the codes reflect a psychological construct.

**Решение:** =

---

### 440 · R12684

**Towards Effective Automatic Evaluation of Generated Reflections for Motivational Interviewing**

2023 · ICMI Companion · journalarticle, book, conference-paper · en · https://doi.org/10.1145/3610661.3616127

Reflection is an essential counselling skill where the therapist communicates their understanding of the client’s words to the client. Recent studies have explored language-model-based reflection generation, but automatic quality evaluation of generated reflections remains under-explored. In this work, we investigate automatic evaluation on one fundamental quality aspect: coherence and context-consistency. We test a range of automatic evaluators/metrics and examine their correlations with expert judgement. We find that large language models (LLMs) as zero-shot evaluators achieve the best performance, while other metrics correlate poorly with expert judgement. We also demonstrate that diverse LLM-as-evaluator configurations need to be explored to find the best setup.

**ИИ:** + · обе модели · LLM-судья · LLMs used as zero-shot evaluators of the coherence of MI reflections, correlated with expert judgement of the same reflections.

**Решение:** =

---

### 441 · R12685

**ความเชอมนและความเทยงตรงของปญญาประดษฐ Application DMIND สำหรบคนหาภาวะซมเศราในประชากรไทย**

2023 · dissertation · https://doi.org/10.58837/chula.the.2023.1474

ประเทศไทยและทั่วโลกมีประชากรประสบภาวะซึมเศร้าเพิ่มขึ้นทุกปี มีจำนวนมากที่ไม่สามารถเข้าถึงบริการสาธารณสุขได้จึงเริ่มมีการนำเทคโนโลยีปัญญาประดิษฐ์มาช่วยค้นหาภาวะซึมเศร้าพร้อมแยกระดับความรุนแรง การศึกษานี้มีวัตถุประสงค์เพื่อพัฒนาเทคโนโลยีปัญญาประดิษฐ์ Application DMIND ประเมินความเชื่อมั่น ความเที่ยงตรง และความถูกต้องในการคัดกรองภาวะซึมเศร้าในประชากรไทย เป็นการศึกษาแบบ Cross-sectional เป็น Research and development โดย มี 2 ระยะ คือ ระยะที่ 1 เป็น การพัฒนา DMIND Questionnaire ที่เตรียมนำเข้าไปใช้กับแอพลิเคชั่น มีการศึกษาความเชื่อมั่น ความเที่ยงตรงและความถูกต้องของแบบสอบถาม ระยะที่ 2 เป็นการศึกษาความเที่ยงตรงและความถูกต้องของ Application DMIND เทียบกับ HDRS-17 Thai ระยะที่ 1: ผู้เข้าการศึกษาทั้ง 81คน ถูกประเมินด้วยแบบสอบถาม DMIND ตามด้วยแบบประเมินภาวะซึมเศร้า Hamilton Depression Rating Scale (HDRS-17 Thai) ผลการศึกษาพบว่า แบบสอบถาม DMIND แสดงให้เห็นถึงคะแนนความถูกต้องของเนื้อหาสูง โดยมี I-CVI และ S-CVI ที่ 1.0 เครื่องมือยังแสดงให้เห็นถึงความสอดคล้องภายในที่สูง Cronbach's alpha coefficient = 0.96 การวิเคราะห์ ROC แสดง AUC = 0.88 ซึ่งบ่งบอกถึงความแม่นยำสูงในการคัดกรองภาวะซึมเศร้า คะแนนตัดที่เหมาะสมที่ 11.5 ระยะที่ 2: เป็นการศึกษาความถูกต้องและเที่ยงตรงของ Application DMIND เทียบกับ HDRS-17 Thai โดยมีผู้เข้าร่วมงานวิจัย ที่มีคุณสมบัติตามเกณฑ์ จำนวน 388 ราย ใช้แอปพลิเคชัน DMIND แล้วถูกประเมินต่อด้วย HDRS-17 Thai ผลการศึกษาพบว่า แอปพลิเคชัน DMIND มีระดับความสอดคล้องกับ HDRS-17 Thai สูง 87.53 มีค่า Cohen Kappa 0.45 ในระดับปานกลาง และประสิทธิภาพเครื่องมือนี้มีความถูกต้องโดยมีค่าความไวสูง (87.30%) และความจำเพาะพอใช้ได้ (59.50%) และค่าความถูกต้องที่ปานกลาง (68.0%) สรุป : การศึกษานี้แสดงให้เห็นว่า แอพลิเคชั่น DMIND ที่ใช้เทคโนโลยีปัญญาประดิษฐ์มีโมเดลการทำงานของ Machine learning, Natural language processing และ Large language model ที่ สามารถคัดกรองภาวะซึมเศร้าได้อย่างมีประสิทธิภาพนำมาปรับให้เข้าถึงและให้การตอบสนองของบริการสุขภาพจิตได้ดี ในอนาคตควรนำนวัตกรรมนี้ไปใช้ในกลุ่มเป้าหมายอื่น ๆ และศึกษาการประเมินผลในระยะยาวต่อไป

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · An AI app (ML/NLP/LLM) screens for depression and is compared with clinician HDRS-17 ratings. It is unclear whether an LLM rates text that clinicians also rated.

**Решение:** =

---

### 442 · R12690

**A Systematic Evaluation of Text Mining Methods for Short Texts: Mapping Individuals’ Internal States from Online Posts**

2022 · preprint · en · https://doi.org/10.31235/osf.io/cerzs

Short texts generated by individuals in online environments can provide social and behavioral scientists with rich insights into these individuals’ internal states. Trained manual coders can reliably interpret expressions of such internal states in text. However, manual coding imposes restrictions on the number of texts that can be analyzed, limiting our ability to extract insights from large-scale textual data. We evaluate the performance of several automatic text analysis methods in approximating trained human coders’ evaluations across four coding tasks encompassing expressions of motives, norms, emotions, and stances. Our findings suggest that commonly used dictionaries, although performing well in identifying infrequent categories, generate false positives too frequently compared to other methods. We show that large language models trained on manually coded data yield the highest performance across all case studies. However, there are also instances where simpler methods show almost equal performance. Additionally, we evaluate the effectiveness of cutting-edge generative language models like GPT-4 in coding texts for internal states with the help of short instructions (so-called zero-shot classification). While promising, these models fall short of the performance of models trained on manually analyzed data. We discuss the strengths and weaknesses of various models and explore the trade-offs between model complexity and performance in different applications. Our work informs social and behavioral scientists of the challenges associated with text mining of large textual datasets while providing best-practice recommendations.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-4 zero-shot coding of online posts for motives, norms and emotions, compared against trained human coders.

**Решение:** =

---

### 443 · R12705

**Automatic Generation and Detection of Motivational Interviewing-style Reflections for Smoking Cessation Therapeutic Conversations using Transformer-based Language Models**

2022 · TSpace (University of Toronto) · dissertation · https://utoronto.scholaris.ca/bitstreams/2b1a4df9-ea48-42ec-8939-05d3d055dec5/download

If conversational agents can take on a therapeutic role, they may provide a scalable way to help many more people suffering from addictions. Motivational Interviewing (MI) is a validated therapy for behaviour change that has been used to help smokers to quit. A key MI skill is to produce reflections on a patient’s statements about a behaviour. Reflections are simple restatements or complex inferences drawing on conversation history or general experience. This thesis presents a method of generating reflections using GPT-2 and GPT-3 language models. These models produce promising reflections; however, some generated reflections are poor quality. To address this, we train a classifier on samples labeled by an MI expert to act as a filter. Its sensitivity is 90%, and specificity 71%. GPT-2 produces reflections 54% of the time with few-shot priming which GPT-3 improves to 89%. With fine-tuning and filtering, GPT-2 generation hit-rate improves to 81%.

**ИИ:** ? · обе модели · другое · Mostly about generation, but a transformer classifier detects MI reflections against expert labels; unclear whether the classifier is a generative LLM.

**Решение:** =

---

### 444 · R12710

**Generation and Classification of Motivational-Interviewing-Style Reflections for Smoking Behaviour Change Using Few-Shot Learning with Transformers**

2022 · Institute of Electrical and Electronics Engineers (IEEE) · posted-content, preprint · en · https://doi.org/10.36227/techrxiv.20029880

&lt;p&gt;If conversational agents can take on a therapeutic role, they may provide a scalable way to help many people suffering from addictions. Motivational Interviewing (MI) is a validated therapy for behaviour change that can be applied to addiction, including smoking cessation. A core technique in MI (and many other kinds of talk therapy) is to pose an open-ended question concerning a negative behaviour, and then to provide a reflection of the response. Reflections can be a simple restatement of the response, or a more complex inference from prior statements or general knowledge, and they help someone contemplate the behaviour more deeply. We describe a method to generate reflections that uses few-shot priming of the GPT-2 and GPT-3 language models. These produce very promising simple and complex reflections, but also some that are off-topic or irrelevant. To filter these, we train a classifier to detect poor reflections, employing samples labeled by an MI expert. Its accuracy is 81%, sensitivity 90% and specificity 71%. We show that GPT-2 can generate acceptable reflections at a 54% success rate, and when combined with the classifier/filter produces acceptable reflections 73% of the time. The GPT-3 model has a native success rate of 89%. &lt;/p&gt; &lt;p&gt;&lt;br&gt;&lt;/p&gt;

**ИИ:** разошлись — Opus ? (другое: A classifier rates MI reflection quality against MI expert labels, but it may be an encoder or GPT-2 model rather than an eligible LLM.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: GPT-2/3 generate MI reflections; the quality filter is a separately trained classifier on expert labels, not an LLM coding texts against human coders.)

**Решение:** -

---

### 445 · R12719

**Human vs. GPT-3: The challenges of extracting emotions from child responses**

2022 · International Conference on Quality of Multimedia Experience (QoMEX) · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/qomex55416.2022.9900885

Conducting interviews with abused children requires a specific skill set that is obtained by undergoing special training. In addition to acquiring the interview training skills, these also have to be constantly refreshed to keep a high level of quality. Technology, such as synthetic video generation and natural language processing, is in a stage that could allow the construction of a system that can make this task easier. Thus, we aim to design a training system aided by machine learning that can support the interview training with an interactive child avatar capable of meaningful interactions with the trainees. In these interviews, emotions play an important role, so we conduct three different user studies in a remote study setting with the aim of analyzing child emotions in these interviews. In these user studies, the participants had to classify different transcripts excerpts as one of the possible predefined emotions. These human annotations are used to measure the performance of sentiment analysis using GPT-3. We investigate different approaches to obtain the correct classifications by changing the amount of context the participants and the model get to see. Our experiments show that humans have a hard time agreeing when choosing between seven different emotions. This improves when we reduce the set of emotions to four. In addition, we found that context is needed to make a motivated choice, but too much context can make it vague, reducing the judgment's quality.

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT-3 classified emotions in child interview transcript excerpts, and its output was compared with human annotations under the same emotion categories.

**Решение:** =

---

### 446 · R12722

**Experiment Maker: A Tool to Create Experiments with GPT-3 Easily**

2022 · International Conference Knowledge Engineering and Knowledge Management · journalarticle

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Software-tool paper for running GPT-3 experiments in knowledge engineering; title suggests no psychological text coding or human comparison.); Sonnet ? (нет аннотации: No abstract; title suggests a GPT-3 experiment tool, likely generic and not psychological coding, but the content is unclear.)

**Решение:** ?

---

### 447 · R12738

**Does GPT-3 Generate Empathetic Dialogues? A Novel In-Context Example Selection Method and Automatic Evaluation Metric for Empathetic Dialogue Generation**

2022 · International Conference on Computational Linguistics · journalarticle, conference

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: Mainly empathetic dialogue generation, but the proposed automatic empathy metric may involve GPT-3 rating and correlation with human ratings.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Focuses on GPT-3 generating empathetic dialogue with in-context example selection; no LLM coding of text against human labels is evident.)

**Решение:** ?

---

### 448 · R12741

**Μεγάλα γλωσσικά μοντέλα στην υποστήριξη της ψυχικής υγείας: μελέτη, πειραματική αξιολόγηση και εφαρμογή**

2022 · University of Thessaly Institutional Repository (University of Thessaly) · dissertation · en · http://ir.lib.uth.gr/xmlui/bitstream/11615/88829/4/33808.pdf

This thesis explores the use of Large Language Models (LLMs) for mental health support, with a focus on detecting the depression severity and suicide risk from text.Motivated by the growing number of mental health phenoms, this work aims to contribute a tool that can assist psychologists in identifying high-risk cases early and reliably.To achieve this, MentaLLaMA was fine-tuned using instruction-based datasets for two classification tasks, the depression severity estimation and suicide risk detection.Because of the limited data in high-risk scenarios, a synthetic dataset was created to help with the model's performance.The training pipeline for fine-tuning the models was designed with LoRA and QLoRA.Also a focal loss function was implemented to deal with class imbalance and a hard negative mining technique to help the model train more on challenging examples.Finally, a user interface was designed to provide an environment for the individuals to express their thoughts.This user interface was implemented with Flutter.A crucial feature of this implementation is the response protocol when a crisis is detected.In such case the system triggers an immediate intervention mechanism, that directs the user to profesional emergency responses.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Fine-tuned MentaLLaMA classifies depression severity and suicide risk from text; unclear whether the reference labels are human annotations.

**Решение:** =

---

### 449 · R12749

**Support for Interview Preparation with Deep Learning Based Language Model**

2021 · International Conference on Emerging Techniques in Computational Intelligence (ICETCI) · conference, conference-paper · en · https://doi.org/10.1109/icetci51973.2021.9574063

Deep-learning based language models (LMs) have significantly enhanced services relating to language generation and classification. Our focus in this paper is on the Multiple Mini Interview (MMI) which is commonly used internationally by medical schools to screen applicants based on their ability to answer short questions in a considerate, professional manner. In this paper we establish the ability of LMs, specifically GPT-3, to generate MMI questions, simulate responses, and rate answers. We compare these simulated questions with their human generated counterparts and, after identifying the optimal hyperparameters, find that 92% of generated responses are capable of fooling humans. We also find that after identifying the optimal hyperparameters for question-answering, LMs are capable producing high quality simulated MMI responses, with an average human rating of 3.5 out of 5. Finally, GPT-3 is shown to have some agreement with human ratings, although it tends to overestimate the quality of the response. Conditional text generation by LMs alone seems to be able to significantly support MMI preparation.

**ИИ:** ? · обе модели · неясен конструкт · GPT-3 rated MMI answers and was compared with human ratings; unclear whether answer quality counts as a psychological/interpersonal construct.

**Решение:** =

---

### 450 · R1278

**An Auditable Standard for Transcript-Visible Crisis Interview Conduct**

2026 · International Journal of Human-Computer Interaction · journalarticle/journal contribution, article · en · https://doi.org/10.1080/10447318.2026.2696959

Semi-structured interviews in crisis contexts generate perishable data that is difficult to collect at scale, and the growing interest in Large Language Models (LLMs) as interviewers or auditors raises the question of how to evaluate interviewer conduct on comparable terms across human and machine. We propose a bounded, auditable standard for transcript-visible crisis interview conduct, operationalized as a 10-item rubric across four domains: Question Effectiveness, Interviewer Engagement, Contextual Understanding, and Respect/Ethical Conduct. Using transcripts from disaster-resilience and COVID-19 studies, we provide initial reliability evidence from two trained coders (pooled Cohen’s κ = 0.86 across categorical items) and a benchmark of two LLMs (OpenAI o4-mini, Google gemini-2.5-flash) against these human reference labels. Under one controlled prompt design, LLMs approximate human judgments on structural criteria but remain weaker on relational ones, supporting a bounded, human-in-the-loop auditing role.

**ИИ:** + · обе модели · кодирование сессий · o4-mini and Gemini rated interviewer conduct (engagement, respect, relational skills) in crisis interview transcripts against human reference labels from two trained coders.

**Решение:** =
