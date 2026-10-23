# Проверка с метками ИИ, часть 2

Записи 151–300 из 1304, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

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

### 151 · R10397

**Exploring Differences Between Hybrid GPT-Human and Human-Created Qualitative Codebooks in an Educational Game**

2025 · Communications in computer and information science · book-chapter, conference-paper · en · https://doi.org/10.1007/978-3-032-12229-2_13

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; GPT-human vs human codebook comparison in an educational game. Psychological construct and unit-level coding agreement are unclear.

**Решение:** =

---

### 152 · R10414

**Co-DETECT: Collaborative Discovery of Edge Cases in Text Classification**

2025 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48448/5854-9x13

We introduce Co-DETECT (Collaborative Discovery of Edge cases in TExt ClassificaTion), a novel mixed-initiative annotation framework that integrates human expertise with automatic annotation guided by large language models (LLMs). Co-DETECT starts with an initial, sketch-level codebook and dataset provided by a domain expert, then leverages the LLM to annotate the data and identify edge cases that are not well described by the initial codebook. Specifically, Co-DETECT flags challenging examples, induces high-level, generalizable descriptions of edge cases, and assists user in incorporating edge case handling rules to improve the codebook. This iterative process enables more effective handling of nuanced phenomena through compact, generalizable annotation rules. Extensive user study, qualitative and quantitative analyses prove the effectiveness of Co-DETECT.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM codebook-based annotation framework, possibly compared with humans; the text domain and constructs aren't specified, so they may not be psychological.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: General text-classification annotation framework with LLM codebook refinement; no psychological or clinical construct or LLM–human agreement on such text evident.)

**Решение:** -

---

### 153 · R10419

**Large Language Model–Assisted Annotation Framework for Cross-Platform Analysis of Online Autism Communities: Implications for Parent Education and Digital Support (Preprint)**

2025 · JMIR Publications Inc. · posted-content · https://doi.org/10.2196/preprints.85290

BACKGROUND Online health communities (OHCs) are important channels for families of children with autism spectrum disorder to obtain health information and psychosocial support. Differences between an open forum platform and the physician-patient consultation platforms may shape caregiver decisions, yet comparative evidence from China remains limited. A large language model (LLM) provides a scalable approach for systematic content annotation in large OHC datasets. OBJECTIVE This study proposes and validates a standardized LLM-assisted annotation framework under a unified classification schema and compares topic distributions and poster identities across an open forum platform (Baidu Tieba) and physician-patient consultation platforms (Chunyu Doctor and Haodf). METHODS We implemented an LLM-assisted annotation framework. A unified taxonomy of topics and poster identities was first developed through human open coding. Poster identities in Baidu Tieba were annotated through a double-blind manual procedure. For topic classification, interannotator and human-LLM agreement were evaluated on a manually labeled subset to benchmark models of varying sizes. The best-performing LLM was selected for full-dataset topic annotation, followed by statistical and cross-platform analysis. RESULTS When metrics were arithmetically averaged across all annotation tasks, the best-performing LLM achieved agreement levels comparable to human annotation (accuracy=79.18%, SD 0.20%; κ=0.736, SD 0.003; &lt;i&gt;F&lt;/i&gt;&lt;sub&gt;1&lt;/sub&gt;-score=0.727, SD 0.006), approaching interannotator agreement (accuracy=81.65%; κ=0.767; &lt;i&gt;F&lt;/i&gt;&lt;sub&gt;1&lt;/sub&gt;-score=0.758), demonstrating strong stability and scalability. Full-dataset analysis yielded 3 main findings. First, model performance increased with parameter scale but plateaued beyond 14B, indicating diminishing marginal returns from further scaling. Second, clear cross-platform differences in poster identity were observed: the open forum platform was dominated by family members of patients (caregivers: 2377/3516, 67.61%), with substantial participation from commercial rehabilitation practitioners (commercial posters: 427/3516, 12.14%), resulting in a more heterogeneous participation structure. Third, topic distributions reflected both shared high demand for resource-related information and differentiated help-seeking pathways: both platform types demonstrated consistently high demand for resource recommendation and evaluation; the open forum platform was primarily characterized by diagnosis-related discussions (1183/7535, 15.70%), whereas the physician-patient consultation platforms were centered on intervention-related consultation (2864/7687, 37.26%). CONCLUSIONS The LLM-assisted annotation framework proposed in this study enables reliable large-scale annotation of OHC data while maintaining high human-LLM agreement and operational stability. Midsized models (eg, 14B) demonstrated favorable cost-performance efficiency. The findings reveal 2 key aspects: the open forum platform exhibits a complex participation structure, and the influence of commercially affiliated actors should not be overlooked; users on both platform types show sustained demand for resource-related information but follow different help-seeking pathways, emphasizing diagnostic exploration and professional intervention, respectively. These results suggest that platform structure and governance mechanisms may shape caregivers’ information access and decision-making. The framework provides a transparent, reproducible, and cost-effective approach for OHC research. All data were deidentified and handled in accordance with relevant platform policies and ethical standards. CLINICALTRIAL

**ИИ:** ? · обе модели · неясен конструкт · LLM topic coding of autism community posts compared with human labels (κ reported). It is unclear whether the topic categories are psychological constructs or only information categories.

**Решение:** =

---

### 154 · R10420

**Perplexity and proximity: Large language model perplexity complements semantic distance metrics for the detection of incoherent speech.**

2025 · Journal of biomedical informatics · journal article, research support, n.i.h., extramural, journalarticle · eng · https://doi.org/10.1016/j.jbi.2025.104899

OBJECTIVE: Semantic coherence in speech is characterized by a logical, connected flow of ideas. A lack of coherence in speech may reflect disorganized thinking, a core feature of psychosis in schizophrenia spectrum disorders (SSDs). Developing tools that could help with automated assessment of semantic coherence in language could facilitate early detection of SSDs and improved monitoring of symptoms, enabling more timely intervention. Large language models (LLMs) have demonstrated strong capabilities on numerous language-centric tasks and have shown promise for analyzing semantic coherence due to the natural fit between their innate measures of language perplexity and the surprising turns that incoherent narrative often takes. This study aims to develop a novel representation and associated measure of semantic coherence using LLM-based perplexity metrics and to compare this measure with traditional vector distance-based coherence metrics. METHOD: We evaluated "bag" and "chain" models based on LLM perplexities as measures of semantic coherence. Regression models were trained using both single and paired combinations of perplexity- and proximity-based features to predict human ratings of semantic coherence using standardized instruments. Performance was evaluated on held-out examples from a training set of speeches from individuals experiencing psychotic symptoms and a test set of clinical interviews with patients diagnosed with SSDs, both with labels from human assessments of disorganized thinking severity. RESULTS: The best performance was achieved using a combination of perplexity and proximity features, yielding a Spearman correlation with human ratings of 0.61 (vs. 0.56 with proximity features alone) on leave-one-out cross-validation in the training set, and 0.54 (vs. 0.52 with proximity features alone) on the test set. CONCLUSION: We developed novel methods for assessing semantic coherence using LLM perplexities and found them complementary to proximity-based methods. Combined, these methods showed improved performance across two datasets, highlighting LLM's potential in enhancing automated diagnosis and monitoring of SSDs.

**ИИ:** ? · обе модели · другое · LLM perplexity features feed a regression that predicts human ratings of speech coherence in psychosis. The LLM is not prompted to rate, so eligibility is borderline.

**Решение:** =

---

### 155 · R10421

**Identifying Psychiatric Manifestations in Outpatients with Depression and Anxiety: A Large Language Model-Based Approach**

2025 · medRxiv · preprint, ppr · https://doi.org/10.1101/2025.01.03.24318117

Purpose Accurate psychiatric diagnosis and assessment are crucial for effective treatment. However, while current data-driven approaches emphasize diagnostic outcomes, the process of decoding the underlying symptom expressions in patients’ language and mapping them to well-defined psychiatric terminology has received relatively little attention. This study investigates the potential of Large Language Models (LLMs) to automate the identification of diagnostic categories and symptoms from psychiatrist-patient dialogues, to provide interpretable insights and support automatic diagnosis. Methods We analyzed audio recordings from 1160 psychiatric diagnostic interviews, primarily involving patients with depressive disorder and anxiety disorder. A clinical entities corpus was formed by leveraging clinical annotations in EMRs (e.g., chief complaints, mental status, elements in assessment scales) and widely used assessment scales. LLMs were utilized to identify clinical symptoms, rate assessment scales, and an ensemble learning pipeline was designed to classify diagnostic results and symptoms with 10-fold cross-validation. Results The system achieved 86.9% accuracy for identifying the appearance of clinical annotations and 74.7% (77.2%) accuracy for identifying anxiety (depression) symptoms. Patients with depression and anxiety, diagnosed using ICD-10 codes, were differentiated with an accuracy of 75.5%. Analysis of LLM-generated features shows that depression cases exhibited prominent markers of anhedonia and decreased volition, whereas anxiety disorders were characterized by tension and an inability to relax. Conclusion This study demonstrates the potential of integrating LLM technology with linguistic and acoustic features to enhance psychiatric diagnostics. The developed pipeline effectively predicts psychiatric diagnoses and provides interpretable insights, showcasing a valuable tool for clinicians in mental health assessment.

**ИИ:** разошлись — Opus + (клиническая оценка: LLMs identify symptoms and rate assessment scales from psychiatric interview transcripts; accuracy is reported against clinician annotations in EMRs.); Sonnet ? (неясно, кто ставил эталонные метки: LLMs identify symptoms and rate scales from psychiatric interview dialogues; reference labels come from EMR annotations, possibly clinician-made, so human-coder comparison is unclear.)

**Решение:** ?

---

### 156 · R10432

**CounselBench: A Large-Scale Expert Evaluation and Adversarial Benchmarking of Large Language Models in Mental Health Question Answering**

2025 · arXiv (Cornell University) · preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2506.08584

Medical question answering (QA) benchmarks often focus on multiple-choice or fact-based tasks, leaving open-ended answers to real patient questions underexplored. This gap is particularly critical in mental health, where patient questions often mix symptoms, treatment concerns, and emotional needs, requiring answers that balance clinical caution with contextual sensitivity. We present CounselBench, a large-scale benchmark developed with 100 mental health professionals to evaluate and stress-test large language models (LLMs) in realistic help-seeking scenarios. The first component, CounselBench-EVAL, contains 2,000 expert evaluations of answers from GPT-4, LLaMA 3, Gemini, and online human therapists on patient questions from the public forum CounselChat. Each answer is rated across six clinically grounded dimensions, with span-level annotations and written rationales. Expert evaluations show that while LLMs achieve high scores on several dimensions, they also exhibit recurring issues, including unconstructive feedback, overgeneralization, and limited personalization or relevance. Responses were frequently flagged for safety risks, most notably unauthorized medical advice. Follow-up experiments show that LLM judges systematically overrate model responses and overlook safety concerns identified by human experts. To probe failure modes more directly, we construct CounselBench-Adv, an adversarial dataset of 120 expert-authored mental health questions designed to trigger specific model issues. Expert evaluation of 1,080 responses from nine LLMs reveals consistent, model-specific failure patterns. Together, CounselBench establishes a clinically grounded framework for benchmarking LLMs in mental health QA.

**ИИ:** + · обе модели · LLM-судья · LLM judges rated mental-health QA responses on clinical dimensions and were compared with expert ratings; they overrated responses and missed safety issues.

**Решение:** =

---

### 157 · R10434

**AI for Understanding Interlocutors**

2025 · CRC Press eBooks · book-chapter · en · https://doi.org/10.1201/9781003591047-7

Conversations involve individuals with unique personalities. In this chapter, I discuss the importance of understanding the personalities of those taking part in a conversation and demonstrate how large language models (LLMs) can use external resources to leverage their analysis of those personalities. I use two external knowledge resources to illustrate this approach through detailed case studies from Scenes from a Marriage and Pulp Fiction . The participants in the conversations are analyzed according to their personality type and their ability to mentalize. I show how AI can validly analyze the participants’ personalities and how this analysis enriches our understanding of the conversations. I will even show how AI can produce a risk analysis report on Jules in a way that is fully competitive with a human expert.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Case-study chapter: LLM rates personality and risk in film dialogue and claims parity with a human expert; formal agreement with human coding is unclear.

**Решение:** =

---

### 158 · R10436

**The Feasibility and Comparability of Using Artificial Intelligence for Qualitative Data Analysis in Equity-Focused Research**

2025 · Educational Researcher · review, journalarticle, article · en · https://doi.org/10.3102/0013189x251314821

In this essay, we explored the feasibility of utilizing artificial intelligence (AI) for qualitative data analysis in equity-focused research. Specifically, we compare thematic analyses of interview transcripts conducted by human coders with those performed by GPT-3 using a zero-shot chain-of-thought prompting strategy. Our results suggest that the AI model, when provided with suitable prompts, can proficiently perform thematic analysis, demonstrating considerable comparability with human coders. Despite potential biases inherent in its training data, the model was able to analyze and interpret the data through social justice perspectives. We discuss the applications of integrating AI into qualitative research, provide code snippets illustrating the use of GPT models, and highlight unresolved questions to encourage further dialogue in the field.

**ИИ:** ? · обе модели · неясен конструкт · GPT-3 thematic analysis of equity interviews compared with human coders; unclear if units were coded or only themes compared, and if the construct is psychological.

**Решение:** =

---

### 159 · R10439

**Personality Auto-Scoring with Large Language Models Using a Realistic Accuracy Model of Behavioral Cues in Chatbot Interviews**

2025 · PsyArXiv · preprint, ppr, posted-content · https://doi.org/10.31234/osf.io/rtsm5_v1

Advances in artificial intelligence, particularly large language models (LLMs), have opened new possibilities for automating personality assessment through text-based chatbot interviews. While prior research has applied machine learning (ML) and natural language processing (NLP) methods to score interview responses, these approaches often lack a strong theoretical foundation for extracting and interpreting trait-relevant behavioral cues. In this study, we integrate Funder’s Realistic Accuracy Model (RAM) into LLM-based autoscoring to enhance the identification and utilization of behavioral cues in personality evaluation. We use two archival samples (N = 521) to examine the alignment between LLM-derived personality scores and established measures, including human-coded behavioral description and narrative interview ratings, as well as self-reported Big Five personality assessments. We compare results from a job-focused behavioral interview (Sample 1; N = 218) and narrative identity interviews (Sample 2; N = 303). In the behavioral interview sample, RAM-based LLM prompts demonstrated stronger convergence with human ratings than zero-shot prompts. However, in the narrative interview sample, this advantage was attenuated, with RAM- and zero-shot-based LLM scores showing similar convergence. In Study 2, we analyzed differences in the behavioral cues extracted by LLMs and human raters to better understand the rating reasoning process. Similarity analyses revealed moderate overlap between LLM-extracted and human-annotated cues. These findings suggest that theory-guided LLMs can identify behavioral cues that partially overlap with those used by humans. Limitations and implications for scalable, accurate, and interpretable AI-based personality assessment are discussed.

**ИИ:** + · обе модели · подсчёт методики · LLM scores personality from interview transcripts; convergence with human-coded interview ratings and human-annotated cues is reported.

**Решение:** =

---

### 160 · R10445

**Artificial intelligence in qualitative analysis: a practical guide and reflections based on results from using GPT to analyze interview data in a substance use program**

2025 · Quality & Quantity · journalarticle, article · en · https://doi.org/10.1007/s11135-025-02066-1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; GPT analysis of substance-use program interviews may compare its coding with human coding.

**Решение:** =

---

### 161 · R10454

**Do Emotions Really Affect Argument Convincingness? A Dynamic Approach with LLM-based Manipulation Checks**

2025 · Annual Meeting of the Association for Computational Linguistics · journalarticle, conference, preprint/article · en · https://doi.org/10.18653/v1/2025.findings-acl.1250

Emotions have been shown to play a role in argument convincingness, yet this aspect is underexplored in the natural language processing (NLP) community. Unlike prior studies that use static analyses, focus on a single text domain or language, or treat emotion as just one of many factors, we introduce a dynamic framework inspired by manipulation checks commonly used in psychology and social science; leveraging LLM-based manipulation checks, this framework examines the extent to which perceived emotional intensity influences perceived convincingness. Through human evaluation of arguments across different languages, text domains, and topics, we find that in over half of cases, human judgments of convincingness remain unchanged despite variations in perceived emotional intensity; when emotions do have an impact, they more often enhance rather than weaken convincingness. We further analyze whether 11 LLMs behave like humans in the same scenario, finding that while LLMs generally mirror human patterns, they struggle to capture nuanced emotional effects in individual judgments. ACL 2025 Camera-ready

**ИИ:** ? · обе модели · неясен конструкт · Humans and 11 LLMs rate the same arguments' emotional intensity and convincingness; argument texts may fall outside psychological text.

**Решение:** =

---

### 162 · R10462

**The Biased Oracle: Assessing LLMs' Understandability and Empathy in Medical Diagnoses**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2511.00924

Large language models (LLMs) show promise for supporting clinicians in diagnostic communication by generating explanations and guidance for patients. Yet their ability to produce outputs that are both understandable and empathetic remains uncertain. We evaluate two leading LLMs on medical diagnostic scenarios, assessing understandability using readability metrics as a proxy and empathy through LLM-as-a-Judge ratings compared to human evaluations. The results indicate that LLMs adapt explanations to socio-demographic variables and patient conditions. However, they also generate overly complex content and display biased affective empathy, leading to uneven accessibility and support. These patterns underscore the need for systematic calibration to ensure equitable patient communication. The code and data are released: https://github.com/Jeffateth/Biased_Oracle Accepted by NeurIPS 2025 GenAI4Health Workshop

**ИИ:** + · обе модели · LLM-судья · An LLM judge rates the empathy of LLM diagnostic explanations, and those ratings are compared with human evaluations of the same outputs.

**Решение:** =

---

### 163 · R10476

**LLMs as Medical Safety Judges: Evaluating Alignment with Human Annotation in Patient-Facing QA**

2025 · BioNLP@ACL · journalarticle · https://doi.org/10.18653/v1/2025.bionlp-1.19

The increasing deployment of LLMs in patient-facing medical QA raises concerns about the reliability and safety of their responses. Traditional evaluation methods rely on expert human annotation, which is costly, time-consuming, and difficult to scale. This study explores the feasibility of using LLMs as automated judges for medical QA evaluation. We benchmark LLMs against human annotators across eight qualitative safety metrics and introduce adversarial question augmentation to assess LLMs’ robustness in evaluating medical responses. Our findings reveal that while LLMs achieve high accuracy in objective metrics such as scientific consensus and grammaticality, they struggle with more subjective categories like empathy and extent of harm. This work contributes to the ongoing discussion on automating safety assessments in medical AI and in-forms the development of more reliable evaluation methodologies.

**ИИ:** ? · обе модели · неясен конструкт · An LLM judge is compared with human annotators on medical QA safety metrics. Mostly not psychological, but empathy is rated, which may qualify.

**Решение:** =

---

### 164 · R1048

**LLM-assisted assessment of pragmatics: A multi-study evaluation of feasibility, deployability, and rater stability**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.7366891

Achieving human-level pragmatic competence requires the recovery of communicative intent from contextual information, indirectness, and multimodal cues. The extent to which Large Language Models (LLMs) replicate these processes remains uncertain, as fluent output may obscure failures specific to particular speech acts. This study evaluated two GPT-family models using the Assessment Battery for Communication (ABaCo), a validated instrument based in Cognitive Pragmatics, with text-only administration records from 21 healthy older adults. Across 124 items and 4,443 item-by-dimension scoring units, a four-study design examined human-in-the-loop feasibility, one-shot API deployability, rerun stability, and rationale-based failure modes. Both API models produced complete scores. GPT-5.2 outperformed GPT-4o in observed agreement (0.800 vs. 0.749) and Cohen&amp;apos;s kappa (0.408 vs. 0.336), although both models under-assigned positive scores, resulting primarily in false negatives. Errors varied by pragmatic act: deceit, irony, and paralinguistic contradiction were under-credited, while mitigated directives were frequently misclassified as command-like acts. Repeated runs under nominally deterministic settings resulted in label flips (GPT-4o: 14.5%; GPT-5.2: 8.1%) despite high total-score reliability. Qualitative analyses attributed disagreements to explicitness thresholds, literalism in the absence of cues, exclusive treatment of deceit as lying, and overemphasis on directive lexicon. These findings indicate that text-only LLM raters can identify surface speech-act cues but do not consistently replicate the inferential processes required for nonliteral, mitigated, or multimodally distributed meaning. For cognitive systems research, ABaCo-style pragmatic assessment offers a theory-driven probe of communicative competence in artificial systems and highlights the limitations of using aggregate agreement as evidence of human-like pragmatic cognition.

**ИИ:** + · обе модели · подсчёт методики · GPT-4o and GPT-5.2 scored responses on the ABaCo pragmatic communication battery; agreement with human scorers reported as observed agreement and Cohen's kappa.

**Решение:** =

---

### 165 · R10497

**Leveraging Large Language Models for Spontaneous Speech-Based Suicide Risk Detection**

2025 · Interspeech (USB) · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.21437/interspeech.2025-1483

Early identification of suicide risk is crucial for preventing suicidal behaviors. As a result, the identification and study of patterns and markers related to suicide risk have become a key focus of current research. In this paper, we present the results of our work in the 1st SpeechWellness Challenge (SW1), which aims to explore speech as a non-invasive and easily accessible mental health indicator for identifying adolescents at risk of suicide.Our approach leverages large language model (LLM) as the primary tool for feature extraction, alongside conventional acoustic and semantic features. The proposed method achieves an accuracy of 74\% on the test set, ranking first in the SW1 challenge. These findings demonstrate the potential of LLM-based methods for analyzing speech in the context of suicide risk assessment. Accepted to Interspeech 2025

**ИИ:** разошлись — Opus -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): LLM extracts features to predict adolescents' suicide-risk labels from a clinical assessment (SW1 challenge), not human coding of the same speech text.); Sonnet ? (неясно, кто ставил эталонные метки: LLM used for feature extraction in suicide risk detection from adolescent speech; reference labels likely self-report/clinical risk, not human text coding; unclear.)

**Решение:** -

---

### 166 · R10508

**Does "Reasoning" with Large Language Models Improve Recognizing, Generating, and Reframing Unhelpful Thoughts?**

2025 · Proceedings of the Fourth Workshop on NLP for Positive Impact (NLP4PI) · audiovisual/conference talk, journalarticle, preprint/article · https://doi.org/10.48550/arxiv.2504.00163

Cognitive Reframing, a core element of Cognitive Behavioral Therapy (CBT), helps individuals reinterpret negative experiences by finding positive meaning. Recent advances in Large Language Models (LLMs) have demonstrated improved performance through reasoning-based strategies. This inspires a promising direction of leveraging the reasoning capabilities of LLMs to improve CBT and mental reframing by simulating the process of critical thinking, potentially enabling more effective recognition, generation and reframing of cognitive distortions. In this work, we investigate the role of various reasoning methods, including pre-trained reasoning LLMs, such as DeepSeek-R1, and augmented reasoning strategies, such as CoT (Wei et al., 2022) and self-consistency (Wang et al., 2022), in enhancing LLMs’ ability to perform cognitive reframing tasks. We find that augmented reasoning methods, even when applied to older LLMs like GPT-3.5, consistently outperform state-of- the-art pretrained reasoning models such as DeepSeek-R1 (Guo et al., 2025) and o1 (Jaech et al., 2024) on recognizing, generating and reframing unhelpful thoughts.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs recognize cognitive distortions in unhelpful thoughts, probably against a dataset's human labels, but the abstract does not say where the labels come from.

**Решение:** =

---

### 167 · R10510

**Beyond Self-Reports: Multi-Observer Agents for Personality Assessment in Large Language Models**

2025 · conference-paper · en · https://doi.org/10.18653/v1/2025.findings-emnlp.1150

Self-report questionnaires have long been used to assess LLM personality traits, yet they fail to capture behavioral nuances due to biases and meta-knowledge contamination.This paper proposes a novel multi-observer framework for personality trait assessments in LLM agents that draws on informant-report methods in psychology.Instead of relying on self-assessments, we employ multiple observer LLM agents, each of which is configured with a specific relationship (e.g., family member, friend, or coworker).The observer agents interact with the subject LLM agent before assessing its Big Five personality traits.We show that observer-report ratings align more closely with human judgments than traditional self-reports and reveal systematic biases in LLM self-assessments.Further analysis shows that aggregating ratings of multiple observers provides more reliable results, reflecting a wisdom of the crowd effect up to 5 to 7 observers.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM observer agents rate Big Five from interactions and are compared with human judgments; unclear whether humans rated the same texts with the same scheme.

**Решение:** =

---

### 168 · R10512

**LLM-Assisted Automated Deductive Coding of Dialogue Data: Leveraging Dialogue-Specific Characteristics to Enhance Contextual Understanding**

2025 · International Conference on Artificial Intelligence in Education · journalarticle, conference, preprint/article · en · https://doi.org/10.48550/arxiv.2504.19734

Dialogue data has been a key source for understanding learning processes, offering critical insights into how students engage in collaborative discussions and how these interactions shape their knowledge construction. The advent of Large Language Models (LLMs) has introduced promising opportunities for advancing qualitative research, particularly in the automated coding of dialogue data. However, the inherent contextual complexity of dialogue presents unique challenges for these models, especially in understanding and interpreting complex contextual information. This study addresses these challenges by developing a novel LLM-assisted automated coding approach for dialogue data. The novelty of our proposed framework is threefold: 1) We predict the code for an utterance based on dialogue-specific characteristics -- communicative acts and communicative events -- using separate prompts following the role prompts and chain-of-thoughts methods; 2) We engaged multiple LLMs including GPT-4-turbo, GPT-4o, DeepSeek in collaborative code prediction; 3) We leveraged the interrelation between events and acts to implement consistency checking using GPT-4o. In particular, our contextual consistency checking provided a substantial accuracy improvement. We also found the accuracy of act predictions was consistently higher than that of event predictions. This study contributes a new methodological framework for enhancing the precision of automated coding of dialogue data as well as offers a scalable solution for addressing the contextual challenges inherent in dialogue analysis.

**ИИ:** ? · обе модели · неясен конструкт · LLMs deductively code collaborative-learning dialogue (communicative acts/events), presumably checked against human codes; unclear whether the construct is psychological.

**Решение:** =

---

### 169 · R10513

**Exploring the efficacy of ChatGPT in understanding and identifying intimate partner violence**

2025 · Family Relations · journalarticle, article · en · https://doi.org/10.1111/fare.13176

Abstract Objective This study aims to examine the efficiency and consistency of ChatGPT in identifying intimate partner violence (IPV) and the frequency of emotional and informational support ChatGPT provided. Background The integration of artificial intelligence–based conversational large language models, such as ChatGPT, in understanding relationship dynamics has sparked both interest and debate within the scientific community. This tool could be valuable in offering immediate, personalized responses to questions about relationships, including those involving conflicts and violence. Method We extracted 500 posts involving IPV and 80 posts involving nonviolent family tension from online IPV help‐seeking forums as prompts for ChatGPT (Version 3.5). We coded ChatGPT's responses and examined their congruence and consistency in identifying IPV compared to human experts. We also examined incidents where ChatGPT misjudged. Lastly, we assessed the presence of informational and emotional support in ChatGPT's responses to prompts involving IPV. Results ChatGPT‐3.5 was able to identify cases involving IPV (physical violence, psychological violence, and controlling behavior) correctly in 91.2% of the cases. Misjudgment mostly occurred due to community policies or nuanced context information. ChatGPT consistently provided emotional support and informational support to users who presented IPV‐related inquiries. Conclusion ChatGPT‐3.5 could reach a relatively high accuracy and consistency in identifying IPV and can provide supportive responses. Implications ChatGPT can serve as an initial resource for individuals and family members seeking help with IPV, offering immediate, empathetic, and informational support. However, improvements are needed to address its limitations in handling nuanced cases and to ensure ethical use and user safety.

**ИИ:** + · обе модели · клиническая оценка · ChatGPT-3.5 identified intimate partner violence in help-seeking forum posts; its accuracy was compared with human expert judgments (91.2%).

**Решение:** =

---

### 170 · R10514

**AI-Augmented LLMs Achieve Therapist-Level Responses in Motivational Interviewing**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2505.17380

Large language models (LLMs) like GPT-4 show potential for scaling motivational interviewing (MI) in addiction care, but require systematic evaluation of therapeutic capabilities. We present a computational framework assessing user-perceived quality (UPQ) through expected and unexpected MI behaviors. Analyzing human therapist and GPT-4 MI sessions via human-AI collaboration, we developed predictive models integrating deep learning and explainable AI to identify 17 MI-consistent (MICO) and MI-inconsistent (MIIN) behavioral metrics. A customized chain-of-thought prompt improved GPT-4's MI performance, reducing inappropriate advice while enhancing reflections and empathy. Although GPT-4 remained marginally inferior to therapists overall, it demonstrated superior advice management capabilities. The model achieved measurable quality improvements through prompt engineering, yet showed limitations in addressing complex emotional nuances. This framework establishes a pathway for optimizing LLM-based therapeutic tools through targeted behavioral metric analysis and human-AI co-evaluation. Findings highlight both the scalability potential and current constraints of LLMs in clinical communication applications. 21 pages, 5 figures

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mostly GPT-4 generating MI responses, but MI behaviour coding via "human-AI collaboration" may involve checking LLM codes against human coders.

**Решение:** =

---

### 171 · R10515

**Integrative modeling enables ChatGPT to achieve average level of human counselors performance in mental health Q&A**

2025 · Information Processing & Management · article · en · https://doi.org/10.1016/j.ipm.2025.104152

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests ChatGPT generating counselling answers, but the evaluation may include LLM-versus-human ratings.

**Решение:** =

---

### 172 · R10533

**Automatic Scoring of an Open-Response Measure of Advanced Mind-Reading Using Large Language Models**

2025 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, conference-paper · en · https://doi.org/10.18653/v1/2025.clpsych-1.7

A rigorous psychometric approach is crucial for the accurate measurement of mind-reading abilities. Traditional scoring methods for such tests, which involve lengthy free-text responses, require considerable time and human effort. This study investigates the use of large language models (LLMs) to automate the scoring of psychometric tests. Data were collected from participants aged 13 to 30 years and scored by trained human coders to establish a benchmark. We evaluated multiple LLMs against human assessments, exploring various prompting strate- gies to optimize performance and fine-tuning the models using a subset of the collected data to enhance accuracy. Our results demonstrate that LLMs can assess advanced mind-reading abilities with over 90% accuracy on average. Notably, in most test items, the LLMs achieved higher Kappa agreement with the lead coder than two trained human coders, highlighting their potential to reliably score open-response psychometric tests.

**ИИ:** + · обе модели · подсчёт методики · LLMs scored open-response mind-reading test answers; agreement with trained human coders reported as kappa.

**Решение:** =

---

### 173 · R10541

**CAMI: A Counselor Agent Supporting Motivational Interviewing through State Inference and Topic Exploration**

2025 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2502.02807

Conversational counselor agents have become essential tools for addressing the rising demand for scalable and accessible mental health support. This paper introduces CAMI, a novel automated counselor agent grounded in Motivational Interviewing (MI) -- a client-centered counseling approach designed to address ambivalence and facilitate behavior change. CAMI employs a novel STAR framework, consisting of client's state inference, motivation topic exploration, and response generation modules, leveraging large language models (LLMs). These components work together to evoke change talk, aligning with MI principles and improving counseling outcomes for clients from diverse backgrounds. We evaluate CAMI's performance through both automated and manual evaluations, utilizing simulated clients to assess MI skill competency, client's state inference accuracy, topic exploration proficiency, and overall counseling success. Results show that CAMI not only outperforms several state-of-the-art methods but also shows more realistic counselor-like behavior. Additionally, our ablation study underscores the critical roles of state inference and topic exploration in achieving this performance.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly an MI counselor-generation agent, but it uses both automated and manual evaluation of MI skill and state inference; LLM–human agreement may be reported.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Presents an LLM counselor agent that generates MI responses, evaluated with simulated clients; no LLM coding validated against human labels is evident.)

**Решение:** -

---

### 174 · R10542

**Automated scoring of the Ambiguous Intentions Hostility Questionnaire using fine-tuned large language models**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2508.10007

Hostile attribution bias is the tendency to interpret social interactions as intentionally hostile. The Ambiguous Intentions Hostility Questionnaire (AIHQ) is commonly used to measure hostile attribution bias, and includes open-ended questions where participants describe the perceived intentions behind a negative social situation and how they would respond. While these questions provide insights into the contents of hostile attributions, they require time-intensive scoring by human raters. In this study, we assessed whether large language models can automate the scoring of AIHQ open-ended responses. We used a previously collected dataset in which individuals with traumatic brain injury (TBI) and healthy controls (HC) completed the AIHQ and had their open-ended responses rated by trained human raters. We used half of these responses to fine-tune the two models on human-generated ratings, and tested the fine-tuned models on the remaining half of AIHQ responses. Results showed that model-generated ratings aligned with human ratings for both attributions of hostility and aggression responses, with fine-tuned models showing higher alignment. This alignment was consistent across ambiguous, intentional, and accidental scenario types, and replicated previous findings on group differences in attributions of hostility and aggression responses between TBI and HC groups. The fine-tuned models also generalized well to an independent nonclinical dataset. To support broader adoption, we provide an accessible scoring interface that includes both local and cloud-based options. Together, our findings suggest that large language models can streamline AIHQ scoring in both research and clinical contexts, revealing their potential to facilitate psychological assessments across different populations. We have no known conflict of interest

**ИИ:** + · обе модели · подсчёт методики · Fine-tuned LLMs score open-ended AIHQ hostile attribution responses; compared with trained human raters.

**Решение:** =

---

### 175 · R10552

**Capturing Collaborative Competency with GPT-4o and ENA**

2025 · Computer-supported collaborative learning/The Computer-Supported Collaborative Learning Conference · conference-paper · en · https://doi.org/10.22318/cscl2025.611229

Collaboration is a critical learning skill employed across many educational domains.Since moments of collaborative competencies frequently occur in student discourse, there has been a growing body of work in automatic collaborative process analysis.With recent advancements in Large Language Models (LLMs), it became feasible to automate the collaborative process analysis through simple prompting methods.In this study, we develop CoComTag, an LLM-powered approach using GPT-4o that captures students' collaborative competency using four prompting techniques.Our findings demonstrate that CoComTag shows substantial agreement with humans (kappa of 0.67).Such a result shows that LLM yields comparable performance with prior studies using only prompting strategies without additional fine-tuning.Next, using qualitative error analysis and epistemic network analysis (ENA), we examine how CoComTag differs from humans in detecting collaborative competency.Our analysis shows that ENA provides visual cues on where collaborative competencies co-occur, revealing the differences between LLM and human annotation patterns.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o coded student collaborative discourse against human coders (κ=0.67); unclear whether educational collaboration competency counts as a psychological interpersonal construct.

**Решение:** =

---

### 176 · R10553

**The impact of fine-tuning LLMs on the quality of automated therapy assessed by digital patients.**

2025 · Npj mental health research · journal article, journalarticle, article · eng · https://doi.org/10.1038/s44184-025-00159-1

The use of generative large language models (LLMs) in mental health applications is gaining traction, with some proposals even suggesting LLM-based automated therapists. In this study, we assess the impact of fine-tuning therapist LLMs to improve the quality of therapy sessions, addressing a critical question in LLM-based mental health research. Specifically, we demonstrate that fine-tuning with datasets focused on specific therapeutic techniques significantly enhances the performance of LLM therapists. To facilitate this assessment, we introduce a novel evaluation system based on digital patients, powered by LLMs, which engage in text-based therapy sessions and provide session evaluations through questionnaires designed for human patients. This method addresses the inadequacies of traditional text-similarity metrics, which are insufficient for assessing the quality of therapeutic interactions. This study centers on motivational interviewing (MI), a structured and goal-oriented therapeutic approach. However, our digital therapists and patients can be adapted to work in other forms of therapy. We believe that our digital therapists offer a standardized method for assessing automated therapists and showcasing the potential of LLMs in mental health care.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM digital patients rate MI therapy sessions with questionnaires; the abstract does not say whether human ratings of the same sessions were compared.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Fine-tuned LLM therapists are evaluated by LLM digital patients via questionnaires; no LLM coding against human labels is reported.)

**Решение:** -

---

### 177 · R10572

**Two-Stage Voting for Robust and Efficient Suicide Risk Detection on Social Media**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2510.08365

Suicide rates have risen worldwide in recent years, underscoring the urgent need for proactive prevention strategies. Social media provides valuable signals, as many at-risk individuals - who often avoid formal help due to stigma - choose instead to share their distress online. Yet detecting implicit suicidal ideation, conveyed indirectly through metaphor, sarcasm, or subtle emotional cues, remains highly challenging. Lightweight models like BERT handle explicit signals but fail on subtle implicit ones, while large language models (LLMs) capture nuance at prohibitive computational cost. To address this gap, we propose a two-stage voting architecture that balances efficiency and robustness. In Stage 1, a lightweight BERT classifier rapidly resolves high-confidence explicit cases. In Stage 2, ambiguous inputs are escalated to either (i) a multi-perspective LLM voting framework to maximize recall on implicit ideation, or (ii) a feature-based ML ensemble guided by psychologically grounded indicators extracted via prompt-engineered LLMs for efficiency and interpretability. To the best of our knowledge, this is among the first works to operationalize LLM-extracted psychological features as structured vectors for suicide risk detection. On two complementary datasets - explicit-dominant Reddit and implicit-only DeepSuiMind - our framework outperforms single-model baselines, achieving 98.0% F1 on explicit cases, 99.7% on implicit ones, and reducing the cross-domain gap below 2%, while significantly lowering LLM cost.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM voting classifies suicide risk in Reddit/DeepSuiMind posts; unclear whether labels come from human annotators or from subreddit/synthetic sources.

**Решение:** =

---

### 178 · R1058

**Incorporating Artificial Intelligence in Qualitative Research: Exploring the Role of ChatGPT in Thematic Analysis.**

2026 · Medical science educator · journal article, journalarticle, article · eng · https://doi.org/10.1007/s40670-025-02587-2

Thematic analysis is a form of qualitive analysis performed to identify patterns within text-based datasets such as open-ended responses. While thematic analysis is used extensively in medical education research, it has several limitations, such as subjective interpretation by graders and the time required to manually code responses in large datasets. There is potential to overcome many of these challenges with the use of Artificial Intelligence (AI) platforms, such as the free to use large language model, ChatGPT. The goal of this study was to evaluate whether AI can be used in thematic analysis to replace manual graders as the gold standard. The dataset used in this study was related to first year medical students' thoughts and feelings regarding the act of cadaveric dissections. Three different methods were used to instruct the AI to grade the responses, and each method was repeated three times. Various measures related to precision and accuracy were compared, both within the repeated tests using AI and between the AI generated results and those obtained by manual coders. Results show that Method 3 had greater accuracy and agreement with the manual coders, but less precision compared to the other two methods. All methods had an agreement greater than 80%. These findings demonstrate that AI has promise in being used for thematic analysis, but the method used to instruct the AI has a strong influence on the results. When using AI for thematic analyses, it is imperative to carefully document and refine the methodology as well as still incorporate some human oversight to ensure accurate results. Supplementary Information: The online version contains supplementary material available at 10.1007/s40670-025-02587-2.

**ИИ:** + · обе модели · кодирование по кодбуку · ChatGPT coded medical students' open responses about their thoughts and feelings on dissection; agreement with manual coders was reported (>80%).

**Решение:** =

---

### 179 · R10581

**Research on the Validity of Automated Interview Scoring Based on Large Language Models**

2025 · Academy of Management Proceedings · conference-abstract · en · https://doi.org/10.5465/amproc.2025.17713abstract

Large language models, such as ChatGPT-4o, are considered potential alternatives to supervised AI models (e.g., BERT) in automated interview evaluation due to their stronger generalization capabilities and lower deployment costs. However, their actual performance in terms of evaluation validity has not yet been systematically verified. This study applies ChatGPT-4o to automated interview evaluation, analyzing its scoring validity and gender bias to uncover the unique advantages and limitations of large language models in interview scoring, while comparing them with supervised AI models and human raters. Based on an analysis of 1,799 interview videos with a total duration of 3,490 minutes, the study reveals two significant advantages of ChatGPT-4o: first, it demonstrates stronger discriminatory ability in assessing candidates' distinct competencies; second, it achieves higher predictive validity for outcome variables that are primarily quantitative and reflect longer-term job performance (e.g., job performance six months after onboarding). However, the convergent validity of ChatGPT-4o with human ratings is relatively low, which may indicate its ability to capture latent semantic features overlooked by traditional evaluation methods. Additionally, the study shows that ChatGPT-4o exhibits lower gender bias during automated scoring. These findings provide new theoretical insights into the application of large language models in automated interviews and suggest that organizations should refine competency dimensions and optimize prompts based on job requirements and evaluation objectives to enhance the scientific rigor and practical utility of AI-driven scoring.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o scored job interview competencies and was compared with human raters; unclear whether these competencies count as psychological constructs.

**Решение:** =

---

### 180 · R1060

**Toward an integrative science of suicidality: Understanding suicide risk factors through real-world natural language.**

2026 · Journal of psychopathology and clinical science · journal article, med, journalarticle · eng · https://doi.org/10.1037/abn0001157

Suicide remains a public health crisis; accurate prediction and coherent theory integration are hampered by suicidality's complexity and fragmented models.We introduce a multimethod computational framework that operationalizes 27 theory-derived suicidal constructs ("archetypes") in language.Each construct (e.g., perceived burdensomeness) was instantiated with prototype sentences (e.g., "The world would be a better place without me").Using a pretrained transformer, we embedded prototypes and computed their semantic similarity to sentences from five corpora: two real-world suicide-related (r/SuicideWatch posts, authentic suicide notes) and three controls (online discourse about mental health issues, normative stream-of-consciousness writing, and nonclinical online discourse).Corpora were profiled by archetype similarity and by Linguistic Inquiry and Word Count markers; we also benchmarked risk estimates from an instruction-tuned large language model (LLM).Suicide-related texts differed robustly from controls, with elevations across most archetypes, especially negative affect, aversive self-views, and escape motivations.r/SuicideWatch posts and suicide notes also diverged, indicating qualitative differences across stages of suicide risk.LLM ratings showed extreme anchoring and a failure to capture fine-grained gradations.Our results demonstrate that theory-guided semantic profiling can synthesize disparate suicide theories and distinguish contexts of suicidality in naturalistic text, whereas generic LLM scoring added little to this integrative approach.Across theory-derived constructs of suicide risk, we find that the highest risk of suicidality coheres around a small set of motivational cores-aversive self-evaluation, perceived burdensomeness, and a drive to escape-whose shifting balance differentiates ideation from imminent action, sharpening conceptual targets for assessment and intervention. General Scientific SummaryThis study uses computer-based language analysis to examine how people express suicidal thoughts and feelings in their own words, drawing on online posts, suicide notes, and everyday writing.By measuring how closely people's language aligns with 27 different psychological factors linked to suicide-such as feeling like a burden, wanting to escape, and painful self-focus-we find that the psychological profile of suicidality shifts depending on where a person may be in their experience of suicidal thoughts, from early distress to the point of action.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: An LLM rated suicide risk in posts and notes, but the reference seems to be corpus type or embeddings; human ratings are unclear.); Sonnet -5 (нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM: Main method is transformer embedding similarity; the LLM risk rating was only benchmarked, with no human-coded reference labels reported.)

**Решение:** -

---

### 181 · R10622

**Exploring Safety Alignment Evaluation of LLMs in Chinese Mental Health Dialogues via LLM-as-Judge**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2508.08236

Evaluating the safety alignment of LLM responses in high-risk mental health dialogues is particularly difficult due to missing gold-standard answers and the ethically sensitive nature of these interactions. To address this challenge, we propose PsyCrisis-Bench, a reference-free evaluation benchmark based on real-world Chinese mental health dialogues. It evaluates whether the model responses align with the safety principles defined by experts. Specifically designed for settings without standard references, our method adopts a prompt-based LLM-as-Judge approach that conducts in-context evaluation using expert-defined reasoning chains grounded in psychological intervention principles. We employ binary point-wise scoring across multiple safety dimensions to enhance the explainability and traceability of the evaluation. Additionally, we present a manually curated, high-quality Chinese-language dataset covering self-harm, suicidal ideation, and existential distress, derived from real-world online discourse. Experiments on 3600 judgments show that our method achieves the highest agreement with expert assessments and produces more interpretable evaluation rationales compared to existing approaches. Our dataset and evaluation tool are publicly available to facilitate further research.

**ИИ:** + · обе модели · LLM-судья · LLM-as-judge rates safety of responses in mental health crisis dialogues; agreement with expert assessments reported.

**Решение:** =

---

### 182 · R10630

**JiraiBench: A Bilingual Benchmark for Evaluating Large Language Models' Detection of Human Self-Destructive Behavior Content in Jirai Community**

2025 · arXiv (Cornell University) · preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2503.21679

This paper introduces JiraiBench, the first bilingual benchmark for evaluating large language models' effectiveness in detecting self-destructive content across Chinese and Japanese social media communities. Focusing on the transnational "Jirai" (landmine) online subculture that encompasses multiple forms of self-destructive behaviors including drug overdose, eating disorders, and self-harm, we present a comprehensive evaluation framework incorporating both linguistic and cultural dimensions. Our dataset comprises 10,419 Chinese posts and 5,000 Japanese posts with multidimensional annotation along three behavioral categories, achieving substantial inter-annotator agreement. Experimental evaluations across four state-of-the-art models reveal significant performance variations based on instructional language, with Japanese prompts unexpectedly outperforming Chinese prompts when processing Chinese content. This emergent cross-cultural transfer suggests that cultural proximity can sometimes outweigh linguistic similarity in detection tasks. Cross-lingual transfer experiments with fine-tuned models further demonstrate the potential for knowledge transfer between these language systems without explicit target language training. These findings highlight the need for culturally-informed approaches to multilingual content moderation and provide empirical evidence for the importance of cultural context in developing more effective detection systems for vulnerable online communities. 20 pages, 1 figures

**ИИ:** + · обе модели · бенчмарк с метками людей · Benchmark of human-annotated social-media posts on self-harm, overdose and eating disorders; LLM detection is evaluated against those human labels.

**Решение:** =

---

### 183 · R10634

**Towards Multimodal Emotional Support Conversation Systems**

2025 · IEEE Transactions on Multimedia · journalarticle, preprint/article, article · en · https://doi.org/10.1109/tmm.2025.3604951

The integration of conversational artificial intelligence (AI) into mental health care promises a new horizon for therapist-client interactions, aiming to closely emulate the depth and nuance of human conversations. Despite the potential, the current landscape of conversational AI is markedly limited by its reliance on single-modal data, constraining the systems' ability to empathize and provide effective emotional support. This limitation stems from a paucity of resources that encapsulate the multimodal nature of human communication essential for therapeutic counseling. To address this gap, we introduce the Multimodal Emotional Support Conversation (MESC) dataset, a first-of-its-kind resource enriched with comprehensive annotations across text, audio, and video modalities. This dataset captures the intricate interplay of user emotions, system strategies, system emotions, and system responses, setting a new precedent in the field. Leveraging the MESC dataset, we propose a general Sequential Multimodal Emotional Support framework (SMES) grounded in Therapeutic Skills Theory. Tailored for multimodal dialogue systems, the SMES framework incorporates an LLM-based reasoning model that sequentially generates user emotion recognition, system strategy prediction, system emotion prediction, and response generation. Our rigorous evaluations demonstrate that this framework significantly enhances the capability of AI systems to mimic therapist behaviors with heightened empathy and strategic responsiveness. By integrating multimodal data in this innovative manner, we bridge the critical gap between emotion recognition and emotional support, marking a significant advancement in conversational AI for mental health support. This work not only pushes the boundaries of AI's role in mental health care but also establishes a foundation for developing conversational agents that can provide more empathetic and effective emotional support.

**ИИ:** ? · обе модели · другое · Mainly a generation framework, but its LLM-based model predicts user emotion and strategy labels that can be scored against the human-annotated MESC dataset.

**Решение:** =

---

### 184 · R10637

**UAV Accident Forensics via HFACS-LLM Reasoning: Low-Altitude Safety Insights**

2025 · Drones · journalarticle, article · en · https://doi.org/10.3390/drones9100704

UAV accident investigation is essential for safeguarding the fast-growing low-altitude airspace. While near-daily incidents are reported, they were rarely analyzed in depth as current inquiries remain expert-dependent and time-consuming. Because most jurisdictions mandate formal reporting only for serious injury or substantial property damage, a large proportion of minor occurrences receive no systematic investigation, resulting in persistent data gaps and hindering proactive risk management. This study explores the potential of using large language models (LLMs) to expedite UAV accident investigations by extracting human-factor insights from unstructured narrative incident reports. Despite their promise, the off-the-shelf LLMs still struggle with domain-specific reasoning in the UAV context. To address this, we developed a human factors analysis and classification system (HFACS)-guided analytical framework, which blends structured prompting with lightweight post-processing. This framework systematically guides the model through a two-stage procedure to infer operators’ unsafe acts, their latent preconditions, and the associated organizational influences and regulatory risk factors. A HFACS-labelled UAV accident corpus comprising 200 abnormal event reports with 3600 coded instances has been compiled to support evaluation. Across seven LLMs and 18 HFACS categories, macro-F1 ranged 0.58–0.76; our best configuration achieved macro-F1 0.76 (precision 0.71, recall 0.82), with representative category accuracies > 93%. Comparative assessments indicate that the prompted LLM can match, and in certain tasks surpass, human experts. The findings highlight the promise of automated human factor analysis for conducting rapid and systematic UAV accident investigations.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs applied HFACS human-factors codes (unsafe acts, preconditions) to UAV accident narratives and were compared with expert labels; unclear whether this counts as a psychological construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs code UAV accident reports with HFACS human-factor categories against expert labels, but this is aviation safety analysis, not a psychological or clinical construct in psychological text.)

**Решение:** -

---

### 185 · R10660

**Scaling hermeneutics: a guide to qualitative coding with LLMs for reflexive content analysis**

2025 · EPJ Data Science · journalarticle, article, journal-article · en · https://doi.org/10.1140/epjds/s13688-025-00548-8

Abstract Qualitative coding, or content analysis, is more than just labeling text: it is a reflexive interpretive practice that shapes research questions, refines theoretical insights, and illuminates subtle social dynamics. As large language models (LLMs) become increasingly adept at nuanced language tasks, questions arise about whether—and how—they can assist in large-scale coding without eroding the interpretive depth that distinguishes qualitative analysis from traditional machine learning and other quantitative approaches to natural language processing. In this paper, we present a hybrid approach that preserves hermeneutic value while incorporating LLMs to scale the application of codes to large data sets that are impractical for manual coding. Our workflow retains the traditional cycle of codebook development and refinement, adding an iterative step to adapt definitions for machine comprehension, before ultimately replacing manual with automated text categorization. We demonstrate how to rewrite code descriptions for LLM-interpretation, as well as how structured prompts and prompting the model to explain its coding decisions (chain-of-thought) can substantially improve fidelity. Empirically, our case study of socio-historical codes highlights the promise of frontier AI language models to reliably interpret paragraph-long passages representative of a humanistic study. Throughout, we emphasize ethical and practical considerations, preserving space for critical reflection, and the ongoing need for human researchers’ interpretive leadership. These strategies can guide both traditional and computational scholars aiming to harness automation effectively and responsibly—maintaining the creative, reflexive rigor of qualitative coding while capitalizing on the efficiency afforded by LLMs.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM codebook coding checked against manual coding, but the codes are socio-historical; unclear whether any are psychological constructs.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM qualitative coding workflow validated on socio-historical codes from a humanistic study, not a psychological or clinical construct.)

**Решение:** -

---

### 186 · R10661

**A Fully Generative Motivational Interviewing Chatbot for Moving Smokers Towards the Decision to Quit and LLM-Based Synthetic Smokers**

2025 · TSpace (University of Toronto) · dissertation · https://hdl.handle.net/1807/150672

Tobacco use is responsible for 7 million preventable deaths each year. For a large population of smokers, a therapeutic approach called Motivational Interviewing (MI) has shown effectiveness, yet many lack access to this support. This research presents an accessible alternative in the form of an expert-informed, large language model (LLM)-based chatbot that provides MI to smokers through unscripted, natural conversation. Additionally, this work contributes towards the development of synthetic smokers — LLM-based agents that simulate the demographic and behavioural characteristics of real human smokers, and can be used to test the chatbot during development. A study with 106 smokers showed that a single conversation with the chatbot yielded a statistically significant average increase of +1.7 in participants' confidence to quit at one-week follow-up. On a metric of perceived empathy, the chatbot scored higher than its predecessors, but significantly lower than typical human counsellors. An automated analysis of the transcripts showed the chatbot adhered to MI in 98% of the utterances (higher than human counsellors) and elicited a high proportion of motivational language (59%) from participants, comparable to high-quality human-delivered counselling sessions. The fidelity of the synthetic smokers was validated by installing participants' behavioural attributes into their "doppelgängers". The automated analysis of transcripts showed that the level of motivation in doppelgängers' language strongly correlated with their twin participants. In addition, synthetic smokers modulated their behaviour according to counselling quality, producing 54% less motivational language when interacting with a confrontational chatbot as compared to an MI-adherent one. This shows their potential as a tool for testing automated counselling systems and training MI counsellors.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mainly a chatbot-generation dissertation, but the automated MI coding of transcripts could be LLM-based and checked against human coders.

**Решение:** =

---

### 187 · R1067

**Comparison of GPT-5, Gemini 2.5 Pro, and Human Coding for the Qualitative Analysis of Dutch Health Services Data: Comparative Study (Preprint)**

2026 · JMIR Publications Inc. · posted-content, preprint · https://doi.org/10.2196/preprints.98374

BACKGROUND Large Language Models (LLMs) are increasingly used in qualitative research, but their reliability compared to human analysis, especially on large, non-English datasets, is unclear. Previous studies on older models (like GPT-4) show limitations in nuance and token capacity. OBJECTIVE This thesis compares the qualitative analysis capabilities of OpenAI's GPT-5 and Google's Gemini 2.5 with a traditional human analysis. The study uses a large dataset of 317 Dutch newspaper articles (860 pages) from January 1, 2020, to December 31st, 2023, investigating the sentiment towards nurses during the COVID-19 pandemic. METHODS The study employed a two-part methodology. First, a thematic comparison was conducted where the human researcher, GPT-5, and Gemini independently generated inductive coding trees from the entire corpus. Second, a comparative test was performed where all three coded a 10% (31/317) random sample using a predefined codebook. This process was iterative, requiring a second round of AI analysis with refined prompts and an article-by-article approach to ensure a valid comparison. RESULTS The results show that both AI models identified third-order themes (e.g., "Healthcare Heroes") that were highly consistent with the data. In the practical application, however, both AIs "over-coded", identifying more quotations than the human (approx. 180 vs. 136). CONCLUSIONS This study reveals a fundamental divergence in analytical logic: whereas human coders prioritize interpretive significance (contextual weight), LLMs default to semantic presence (literal frequency), leading to systematic over-coding. Consequently, this article argues that LLMs should not be viewed as autonomous researchers but as high-sensitivity filtering instruments requiring human calibration. This study concludes that AI serves as a valuable assistant for qualitative researchers. Still, it requires a rigorous, iterative, and human-in-th

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-5/Gemini applied a codebook to newspaper articles alongside a human coder; unclear whether media sentiment toward nurses counts as a psychological construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs and a human coded Dutch newspaper articles for sentiment toward nurses. That is media content, not psychological or clinical text or a psychological construct.)

**Решение:** -

---

### 188 · R10674

**INSIGHTFUL: insight generation through clinical annotation, analysis and modelling of suicide-related factors towards understanding and lifesaving**

2025 · medRxiv · journalarticle · https://doi.org/10.1136/bmjdhai-2025-000019

Objective: Suicide is a critical medical and public health challenge, particularly among individuals with mental illnesses in safety-net hospitals. To uncover insights about suicidality embedded in unstructured clinical notes, we propose to annotate, analyze, and model a corpus for suicidality understanding and lifesaving. Methods: A multidisciplinary panel developed an annotation guideline to capture four key suicide-related factors: Suicidal Ideation (SI), Suicide Attempt (SA), Exposure to Suicide (ES), and Non-Suicidal Self-Injury (NSSI). We created an annotated corpus of 500 notes through a clinically validated annotation process and performed cohort analysis to characterize demographic and suicidal distributions. A large language model was deployed for automatic classification. Results: The annotated corpus was created with a Cohen's Kappa of 0.95 and further de-identified for data sharing. Most notes (79.4%) contained one (34.4%) or more (45%) suicide-related labels, with SI and SA co-occurrence as the most frequent combination (35.6%), which demonstrates significant overlap. The cohort was characterized with a mean age of 33.4, 51.7% male, and 75.8% singles. Prevalent stressors included unemployment (24.2%), homelessness (12.0%), limited healthcare access (5.4%), and legal challenges (5.0%). We identified four key insights to improve documenting suicidality, including implicitness, confliction, ambiguity, and definition coverage incompleteness. The baseline model achieved a micro-averaged F1 score of 0.70, demonstrating satisfying performance in multi-label classification. Conclusion: The near-perfect inter-annotator agreement underscores the proposed annotation process and data quality. Cohort analysis highlights the distribution and documentation insights of suicidality. Data modeling demonstrates the potential of insight generation via AI-powered methods for mining large-scale clinical notes.

**ИИ:** + · обе модели · клиническая оценка · An LLM classified suicide-related factors (SI, SA, NSSI) in clinical notes and was scored against a human-annotated corpus (F1 0.70).

**Решение:** =

---

### 189 · R10698

**Cultural Alignment and Biases in Qualitative Coding: Comparing GPT and Human Coders**

2025 · Center for Open Science · posted-content, preprint · https://doi.org/10.35542/osf.io/h8u4f_v1

Qualitative coding—the interpretive labeling of data—is shaped by the researcher's cultural background, particularly when coding more subjective or culturally-grounded constructs that require interpretive judgment. As large language models (LLMs) are increasingly integrated into qualitative research in education, understanding how cultural perspectives influence coding decisions becomes critical. This study examines where and why researchers from different cultures diverge in their interpretations, and whether LLMs can approximate culture-specific human coding decisions when integrated into this process. We compared coding decisions from three cultural backgrounds (China, India, United States) with qualitative coding produced by GPT under two prompting conditions: baseline and culture-specific. Drawing on emic-etic perspectives, we analyzed coding agreement and divergence across cultural groups and between humans and GPT, along with coders' rationales. Results show that cross-cultural coding agreement was relatively low, suggesting that coders relied on culturally informed interpretive frames when interpreting subjective constructs. When integrating GPT into coding, the model aligned more closely with U.S. coders and struggled to recognize implicit cultural cues—even when prompted to adopt specific cultural lenses. These findings highlight the value of incorporating both emic and etic perspectives in coding and the challenges of integrating LLMs into the process.

**ИИ:** ? · обе модели · неясен конструкт · GPT vs human coders on the same qualitative education data; unclear whether the subjective constructs are psychological.

**Решение:** =

---

### 190 · R10717

**MeKB-Sim: Personal Knowledge Base-Powered Multi-Agent Simulation**

2025 · North American Chapter of the Association for Computational Linguistics · journalarticle, conference · https://doi.org/10.18653/v1/2025.naacl-demo.33

Language agents have demonstrated remarkable emergent social behaviors within simulated sandbox environments. However, the characterization of these agents has been constrained by static prompts that outline their profiles, highlighting a gap in achieving simulations that closely mimic real-life interactions. To close this gap, we introduce MeKB-Sim, a multi-agent simulation platform based on a dynamic personal knowledge base, termed MeKB. Each agent’s MeKB contains both fixed and variable attributes—such as linguistic style, personality, and memory—crucial for theory-of-mind modeling. These attributes are updated when necessary, in response to events that the agent experiences. Comparisons with human annotators show that the LLM-based attribute updates are reliable. Based on the dynamic nature of MeKB, experiments and case study show that MeKB-Sim enables agents to adapt their planned activities and interactions with other agents effectively. Our platform includes a Unity WebGL game interface for visualization and an interactive monitoring panel that presents the agents’ planning, actions, and evolving MeKBs over time 1 .

**ИИ:** разошлись — Opus ? (неясен конструкт: Agent simulation platform; LLM updates of personality and memory attributes were compared with human annotators, but the texts are simulated events.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Multi-agent simulation platform; human comparison only checks LLM attribute updates, not coding of psychological text.)

**Решение:** -

---

### 191 · R1073

**A comparison of human and ChatGPT classification performance on complex social media data**

2026 · Information Research · journalarticle, preprint/article, article · en · https://doi.org/10.47989/ir31iconf64141

Introduction. Generative artificial intelligence tools, like ChatGPT, are an increasingly utilised resource among computational social scientists. Nevertheless, there remains space for improved understanding of the performance of ChatGPT in complex tasks such as classifying and annotating datasets containing nuanced language. Method. In this paper, we measure the performance of GPT-4 on one such task and compare results to human annotators. We investigate ChatGPT versions 3.5, 4, and 4o to examine performance given rapid changes in technological advancement of large language models. We employ a dataset containing human-annotated comments from YouTube and X. We craft four prompt styles as input and evaluate precision, recall, and F1 scores. Analysis. Both quantitative and qualitative evaluations of results demonstrate that while including label definitions in prompts may help performance, overall GPT-4 has difficulty classifying nuanced language. Results. Qualitative analysis reveals four specific findings: 1) cultural euphemisms are too nuanced for GPT-4 to understand, 2) interpreting the type of ’internet speak’ found on social media platforms is a challenge, 3) GPT-4 falters in determining who or what is the target of directed attacks (e.g., the content or the user), and 4) the rationale GPT-4 provides is inconsistent in logic. Conclusion. Our results suggest the use of ChatGPT in classification tasks involving nuanced language should be conducted with prudence

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: GPT compared with human annotations of social media comments for nuanced attack or toxicity labels, which falls under hate speech or incivility, not a psychological construct.); Sonnet ? (неясен конструкт: GPT is compared with human annotators on YouTube/X comments, but the construct (possibly toxicity or directed attacks) is unstated and may be hate speech rather than psychological.)

**Решение:** -

---

### 192 · R10741

**PALLM: Evaluating and Enhancing Palliative Care Conversations with Large Language Models**

2025 · ACM Transactions on Computing for Healthcare · journalarticle, preprint/article, article · en · https://doi.org/10.1145/3712300

Effective patient-provider communication is crucial in clinical care, directly impacting patient outcomes and quality of life. Traditional evaluation methods, such as human ratings, patient feedback, and provider self-assessments, are often limited by high costs and scalability issues. Although existing natural language processing (NLP) techniques show promise, they struggle with the nuances of clinical communication and require sensitive clinical data for training, reducing their effectiveness in real-world applications. Emerging large language models (LLMs) offer a new approach to assessing complex communication metrics, with the potential to advance the field through integration into passive sensing and just-in-time intervention systems. This study explores LLMs as evaluators of palliative care communication quality, leveraging their linguistic, in-context learning, and reasoning capabilities. Specifically, using simulated scripts crafted and labeled by healthcare professionals, we test proprietary models (e.g., GPT-4) and fine-tune open-source LLMs (e.g., LLaMA2) with a synthetic dataset generated by GPT-4 to evaluate clinical conversations, to identify key metrics such as `understanding' and `empathy'. Our findings demonstrated LLMs' superior performance in evaluating clinical communication, providing actionable feedback with reasoning, and demonstrating the feasibility and practical viability of developing in-house LLMs. This research highlights LLMs' potential to enhance patient-provider interactions and lays the groundwork for downstream steps in developing LLM-empowered clinical health systems. Accepted by ACM Transactions on Computing for Healthcare, Special Issue on Large Language Models, Conversational Systems, and Generative AI in Health, pending minor revisions

**ИИ:** + · обе модели · LLM-судья · GPT-4 and LLaMA2 rate empathy and understanding in palliative care conversation scripts that healthcare professionals also labelled.

**Решение:** =

---

### 193 · R10751

**Integrating Visual Modalities with Large Language Models for Mental Health Support**

2025 · International Conference on Computational Linguistics · journalarticle, conference

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. Multimodal LLM for mental health support may be generation only, but it could involve classification against human labels.

**Решение:** =

---

### 194 · R10764

**Exploring the Digital Therapeutic Alliance: A Preliminary Analysis of Mental Health Chatbot Conversations**

2025 · Proceedings of the 2025 International Conference on Human-Engaged Computing · book, conference, review · https://doi.org/10.1145/3786995.3787059

Digital Therapeutic Alliance (DTA) refers to the relational qualities that shape engagement with mental health technologies. While surveys suggest that users can experience empathy, support, and trust with chatbots, little is known about how such alliance-like dynamics actually unfold in conversation. We present a transcript-based study of Youper, a mental health chatbot, drawing on a purposive subsample of ten participants over two weeks. End-of-study relationship ratings were linked to daily transcripts, analyzed through a hybrid pipeline that combined lexicon-based heuristics with large language model (LLM)–assisted coding. Our analysis reveals that high-relationship users engaged in affect-rich disclosure, sustained empathy uptake, and constructive tool use, whereas low-relationship users offered terse or shallow disclosures, resisted support, and rejected exercises; mid-range cases exhibited mixed patterns. These findings suggest that DTA is less about the frequency of disclosure than about whether empathic and instrumental bids are extended into ongoing trajectories. By combining surveys with computational transcript analysis, our study demonstrates a scalable approach for examining alliance in chatbot interactions and identifies conversational features that differentiate stronger from weaker relationships.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM-assisted coding of mental health chatbot transcripts for alliance features; unclear whether human coding validated LLM codes.

**Решение:** =

---

### 195 · R10766

**Exploring Automated Assessment of Primary Students’ Creativity in a Flow-Based Music Programming Environment**

2025 · Journal of Learning Analytics · journalarticle, article · en · https://doi.org/10.18608/jla.2025.8835

Creativity is a vital skill in science, technology, engineering, and mathematics (STEM)--related education, fostering innovation and problem-solving. Traditionally, creativity assessments relied on human evaluations, such as the consensual assessment technique (CAT), which are resource-intensive, time-consuming, and often subjective. Recent advances in computational methods, particularly large language models (LLMs), have enabled automated creativity assessments. In this study, we extend research on automated creativity scoring to a flow-based music programming environment, a context that integrates computational and creative thinking. We collected 383 programming artifacts from 194 primary school students (2022--2024) and employed two automated approaches: an evidence-centred design (ECD) framework--based approach and an LLM-based approach using ChatGPT-4 with few-shot learning. The ECD-based approach integrates divergent thinking, complexity, efficiency, and emotional expressiveness, while the LLM-based approach uses CAT ratings and ECD examples to learn creativity scoring. Results revealed moderate to strong correlations with human evaluations (ECD-based: \( r = 0.48 \); LLM-based: \( r = 0.68 \)), with the LLM-based approach demonstrating greater consistency across varying learning examples (\( r = 0.82 \)). These findings highlight the potential of automated tools for scalable, objective, and efficient creativity assessment, paving the way for their application in creativity-focused learning environments.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 creativity ratings correlated with human CAT ratings, but the rated units are music-programming artifacts, not clearly psychological text.

**Решение:** =

---

### 196 · R10767

**From Clips to Communities: Fusing Social Video into Knowledge Graphs for Localness-Aware LLMs**

2025 · CSCW Companion · journalarticle, book · https://doi.org/10.1145/3715070.3749277

Understanding how people experience and assign meaning to places — what we term “localness” — is essential for designing systems that support orientation, belonging, and community integration. However, current computational approaches to modeling place often struggle to capture the multimodal, relational, and contextual richness of localness. In this paper, we introduce a novel workflow for extracting structured localness representations from geotagged short-form social videos using a Graph-Enhanced Retrieval-Augmented Generation (Graph-RAG) framework. Our method aligns and fuses multimodal video data from TikTok into a knowledge graph, retrieves relevant contextual evidence through a hybrid of graph-based and semantic retrieval, and then prompts large language models (LLMs) to infer fine-grained localness attributes across cognitive, relational, and physical domains. We evaluate our system using both human-annotated ground truth and qualitative analysis, demonstrating full coverage across all localness components, with especially strong performance in environmental and relational dimensions. Our findings reveal both the promises and the challenges of grounding AI systems in lived experiences of place, and we offer design implications for localness-aware technologies in digital placemaking, community informatics, and contextual computing.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs infer localness attributes (cognitive, relational) from TikTok videos against human annotations; unclear whether this counts as psychological text coding.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs infer place "localness" attributes from TikTok videos via Graph-RAG; a geographic/place construct, not a psychological or clinical coding task against human coders.)

**Решение:** -

---

### 197 · R10771

**MM-OPERA: Benchmarking Open-ended Association Reasoning for Large Vision-Language Models**

2025 · neural information processing systems · journalarticle, preprint/article, conference-paper · https://doi.org/10.52202/085713-0386

Large Vision-Language Models (LVLMs) have exhibited remarkable progress. However, deficiencies remain compared to human intelligence, such as hallucination and shallow pattern matching. In this work, we aim to evaluate a fundamental yet underexplored intelligence: association, a cornerstone of human cognition for creative thinking and knowledge integration. Current benchmarks, often limited to closed-ended tasks, fail to capture the complexity of open-ended association reasoning vital for real-world applications. To address this, we present MM-OPERA, a systematic benchmark with 11,497 instances across two open-ended tasks: Remote-Item Association (RIA) and In-Context Association (ICA), aligning association intelligence evaluation with human psychometric principles. It challenges LVLMs to resemble the spirit of divergent thinking and convergent associative reasoning through free-form responses and explicit reasoning paths. We deploy tailored LLM-as-a-Judge strategies to evaluate open-ended outputs, applying process-reward-informed judgment to dissect reasoning with precision. Extensive empirical studies on state-of-the-art LVLMs, including sensitivity analysis of task instances, validity analysis of LLM-as-a-Judge strategies, and diversity analysis across abilities, domains, languages, cultures, etc., provide a comprehensive and nuanced understanding of the limitations of current LVLMs in associative reasoning, paving the way for more human-like and general-purpose AI. The dataset and code are available at https://github.com/MM-OPERA-Bench/MM-OPERA. NeurIPS 2025 Datasets and Benchmarks Track poster

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM-as-judge scores open-ended association responses from psychometric-style tasks; validity analysis may use human ratings, but the responses come from AI models.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Vision-language model association reasoning benchmark; LLM-as-judge validated, but not coding psychological or clinical text constructs.)

**Решение:** -

---

### 198 · R1082

**Can Researchers Agree on Levels of Resilience?**

2026 · Etuaptmumk The Journal of Two-Eyed Seeing · journalarticle, review, article · en · https://doi.org/10.59401/ej.v7i2.49

Resilience has been challenging to define, though it is intuitively apparent in many ways as the capacity to recover from adversity. We set out to determine if we could agree on resilience ratings based on our assessments of collected life story interviews. After reviewing our life stories, we settled on five resilience ratings based on a water/swimming metaphor. At pattern 1, the person sinks to the bottom and remains there. At pattern 2, the person is not sitting at the bottom but has yet to reach the surface. At pattern 3, the person is treading water. They are working hard to stay aoat but not making signicant progress in altering their overall situation. At pattern 4, they’re swimming toward shore, toward a more favorable environment where they can thrive. At pattern 5, they've managed to climb out of the water and change their circumstances. Their resilience allows them to overcome challenges and seek better surroundings. We reviewed the life story interviews of thirty-five participants with an eye to these categories. We also used ChatGPT to determine if it could perform better than us. For 35 participants with five ratings and three raters, we had a percent overall agreement of 84.00% with a free-marginal kappa of 0.80 (95% CI for free-marginal kappa; 0.66 to 0.94). The fixed-marginal kappa was 0.78, with a 95% CI of 0.62 to 0.93. ChatGPT had a percent overall agreement of 71.33% with a free-marginal kappa of 0.65 (95% CI for free-marginal kappa was 0.50 to 0.79); fixed-marginal kappa of 0.61 (95% CI for fixed-marginal kappa of 0.51 to 0.71). Cohen suggested the Kappa result be interpreted as follows: values ≤ 0 as indicating no agreement and 0.01–0.20 as none to slight, 0.21–0.40 as fair, 0.41– 0.60 as moderate, 0.61–0.80 as substantial, and 0.81–1.00 as almost perfect agreement (Cohen, 1960). All results were statistically significant at p < 0.01. The self-administered Ohio State Resilience Scale, reflecting the participants own assessment of their level of resilience, did not correlate with our ratings, suggesting that people’s assessments of their level of resilience do not match those of clinically trained observers. Warning: This paper includes discussion of categories of adverse childhood experience, including child sexual assault, as well as accounts of adult violence, domestic violence, abuse, sexual assault, neglect, and household dysfunction.

**ИИ:** + · обе модели · кодирование по кодбуку · ChatGPT rated resilience levels in life story interviews, and its agreement with trained human raters was reported as kappa.

**Решение:** =

---

### 199 · R10832

**Towards AI-Assisted Protocol Analysis in Design Research: Automating Question Labelling with GPT-4 According to Eris’ (2004) Taxonomy**

2024 · Springer eBooks · conference-paper · en · https://doi.org/10.1007/978-3-031-71918-9_3

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · неясен конструкт · No abstract. GPT-4 labels design-conversation questions using Eris's taxonomy, probably checked against human coders; unclear whether design cognition counts as psychological.

**Решение:** =

---

### 200 · R10833

**Utilizing Large Language Models to Identify Evidence of Suicidality Risk through Analysis of Emotionally Charged Posts**

2024 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, conferencepaper/conferenceitem, conference-paper · en · https://doi.org/10.18653/v1/2024.clpsych-1.26

This paper presents our contribution to the CLPsych 2024 shared task, focusing on the use of open-source large language models (LLMs) for suicide risk assessment through the analysis of social media posts. We achieved first place (out of 15 participating teams) in the task of providing summarized evidence of a user’s suicide risk. Our approach is based on Retrieval Augmented Generation (RAG), where we retrieve the top-k (k=5) posts with the highest emotional charge and provide the level of three different negative emotions (sadness, fear, anger) for each post during the generation phase.

**ИИ:** ? · обе модели · другое · CLPsych 2024 suicide-risk evidence extraction with LLMs, scored against expert-annotated evidence; unclear whether this counts as coding agreement.

**Решение:** =

---

### 201 · R10848

**GPT Models for Text-Annotation: An Empirical Exploration in Public Policy Research**

2024 · preprint · en · https://doi.org/10.31235/osf.io/6fpgj

Text annotation, the practice of labeling text following a predetermined scheme, is essential to qualitative researcher in public policy. Despite its importance utility, text annotation for policy research faces challenges of high labor and time costs, particularly when the size of the qualitative data is enormous. Recent Developments in large language models (LLMs), specifically models with generative pre-trained transformers (GPTs), shows a potential approach that may alleviate the burden of manual annotation coding. In this report, we test if Open AI’s GPT3.5 and GPT-4 models can be employed for text annotation tasks and measure the results of different prompting strategies against manual annotation. Using email messages collected from a national corresponding experiment in the U.S. nursing home market as an example, on average, we demonstrate 86.25% percentage agreement between GPT and human annotations. We also show that GPT models possess context-based limitations. Our report ends with suggestions, guidance, and reflections for readers who are interested in using GPT models for text annotation.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-3.5/4 annotations of nursing-home emails compared with human coding; unclear whether the codes are psychological (e.g., warmth) or policy categories.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: GPT annotation of nursing-home inquiry emails for public policy research versus human annotation; no psychological or clinical construct.)

**Решение:** -

---

### 202 · R10851

**IDEM: The IDioms with EMotions Dataset for Emotion Recognition**

2024 · Language Resources and Evaluation Conference (LREC) · journalarticle, conference-paper · en · https://doi.org/10.63317/22sd97jw5mff

Idiomatic expressions are used in everyday language and typically convey affect, i.e., emotion. However, very little work investigating the extent to which automated methods can recognise emotions expressed in idiom-containing text has been undertaken. This can be attributed to the lack of emotion-labelled datasets that support the development and evaluation of such methods. In this paper, we present the IDioms with EMotions (IDEM) dataset consisting of a total of 9685 idiom-containing sentences that were generated and labelled with any one of 36 emotion types, with the help of the GPT-4 generative language model. Human validation by two independent annotators showed that more than 51% of the generated sentences are ideal examples, with the annotators reaching an agreement rate of 62% measured in terms of Cohen's Kappa coefficient. To establish baseline performance on IDEM, various transformer-based emotion recognition approaches were implemented and evaluated. Results show that a RoBERTa model fine-tuned as a sequence classifier obtains a weighted F1-score of 58.73%, when the sequence provided as input specifies the idiom contained in a given sentence, together with its definition. Since this input configuration is based on the assumption that the idiom contained in the given sentence is already known, we also sought to assess the feasibility of automatically identifying the idioms contained in IDEM sentences. To this end, a hybrid idiom identification approach combining a rule-based method and a deep learning-based model was developed, whose performance on IDEM was determined to be 84.99% in terms of F1-score.

**ИИ:** разошлись — Opus ? (другое: GPT-4 generated and emotion-labelled synthetic sentences that humans then validated; unclear whether this counts as LLM–human label agreement.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: GPT-4 generated and labelled idiom sentences; humans only validated the generated data. Baselines use RoBERTa, so no LLM-versus-human coding agreement is measured.)

**Решение:** -

---

### 203 · R10860

**Emotion Identification for French in Written Texts: Considering Modes of Emotion Expression as a Step Towards Text Complexity Analysis**

2024 · Workshop on Computational Approaches to Subjectivity, Sentiment & Social Media Analysis (WASSA) · journalarticle, conference-paper · en · https://doi.org/10.18653/v1/2024.wassa-1.14

The objective of this paper is to predict (A) whether a sentence in a written text expresses an emotion, (B) the mode(s) in which the emotion is expressed, (C) whether it is basic or complex, and (D) its emotional category.One of our major contributions, in addition to a dataset and a model, is to integrate the fact that an emotion can be expressed in different modes: from a direct mode, essentially lexicalized, to a more indirect mode, where emotions will only be suggested, a mode that NLP approaches generally don’t take into account. The scope is on written texts, i.e. it does not focus on conversational or multi-modal data. In this context, modes of expression are seen as a factor towards the automatic analysis of complexity in texts.Experiments on French texts show acceptable results compared to the human annotators’ agreement to predict the mode and category, and outperforming results compared to using a large language model with in-context learning (i.e. no fine-tuning) on all tasks.Dataset and model can be downloaded on HuggingFace: https://huggingface.co/TextToKids .

**ИИ:** + · обе модели · бенчмарк с метками людей · Human-annotated French emotion dataset; an LLM using in-context learning is evaluated against the human emotion labels as a baseline.

**Решение:** =

---

### 204 · R10861

**Emotion Identification for French in Written Texts: Considering their Modes of Expression as a Step Towards Text Complexity Analysis**

2024 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, preprint/article · en · https://doi.org/10.48550/arxiv.2405.14385

The objective of this paper is to predict (A)~whether a sentence in a written text expresses an emotion, (B) the mode(s) in which the emotion is expressed, (C) whether it is basic or complex, and (D) its emotional category. One of our major contributions, in addition to a dataset and a model, is to integrate the fact that an emotion can be expressed in different modes: from a direct mode, essentially lexicalized, to a more indirect mode, where emotions will only be suggested, a mode that NLP approaches generally don't take into account. The scope is on written texts, i.e. it does not focus on conversational or multi-modal data. In this context, modes of expression are seen as a factor towards the automatic analysis of complexity in texts. Experiments on French texts show acceptable results compared to the human annotators' agreement to predict the mode and category, and outperforming results compared to using a large language model with in-context learning (i.e. no fine-tuning) on all tasks. Dataset and model can be downloaded on HuggingFace: https://huggingface.co/TextToKids .

**ИИ:** + · обе модели · бенчмарк с метками людей · Human-annotated French emotion dataset; an LLM using in-context learning is evaluated against the human labels for emotion presence, mode and category.

**Решение:** =

---

### 205 · R10863

**The Point of View of a Sentiment: Towards Clinician Bias Detection in Psychiatric Notes**

2024 · Proceedings of the Language Resources and Evaluation Conference · journalarticle, conference, preprint/article · https://doi.org/10.48550/arxiv.2405.20582

Negative patient descriptions and stigmatizing language can contribute to generating healthcare disparities in two ways: (1) read by patients, they can harm their trust and engagement with the medical center; (2) read by physicians, they may negatively influence their perspective of a future patient. In psychiatry, the patient-clinician therapeutic alliance is a major determinant of clinical outcomes. Therefore, language usage in psychiatric clinical notes may not only create healthcare disparities, but also perpetuate them. Recent advances in NLP systems have facilitated the efforts to detect discriminatory language in healthcare. However, such attempts have only focused on the perspectives of the medical center and its physicians. Considering both physicians and non-physicians' point of view is a more translatable approach to identifying potentially harmful language in clinical notes. By leveraging pre-trained and large language models (PLMs and LLMs), this work aims to characterize potentially harmful language usage in psychiatric notes by identifying the sentiment expressed in sentences describing patients based on the reader's point of view. Extracting 39 sentences from the Mount Sinai Health System containing psychiatric lexicon, we fine-tuned three PLMs (RoBERTa, GatorTron, and GatorTron + Task Adaptation) and implemented zero-shot and few-shot ICL approaches for three LLMs (GPT-3.5, Llama-3.1, and Mistral) to classify the sentiment of the sentences according to the physician or non-physician point of view. Results showed that GPT-3.5 aligned best to physician point of view and Mistral aligned best to non-physician point of view. These results underline the importance of recognizing the reader's point of view, not only for improving the note writing process, but also for the quantification, identification, and reduction of bias in computational systems for downstream analyses. Oral presentation at NAACL 2024 Queer in AI Workshop

**ИИ:** ? · обе модели · неясен конструкт · GPT-3.5, Llama and Mistral classify the sentiment of psychiatric-note sentences against physician and non-physician labels; unclear if this sentiment counts as a psychological construct.

**Решение:** =

---

### 206 · R10864

**Reading ability conflates SES creativity gaps**

2024 · OSF · text/project · https://doi.org/10.17605/osf.io/d7hm8

Who is more creative: the rich or the poor? This question is the focus of intense debates within both the scientific community and society at large, since creativity has been linked to innovation, productivity and wealth generation -- and increasingly so with the advent of generative AI. This question is, however, hard to answer; in particular, because creativity is typically assessed through standardized tests that build on reading and writing proficiency -- which might conflate the relationship between socioeconomic status and creativity. To overcome this challenge, we conducted a randomized control trial with Brazilian high-school students, who completed divergent thinking tasks: in the control group, students had to read question prompts, just like in standard assessments (e.g., PISA); in the treatment group, enumerators read the prompts on their behalf. In both conditions, enumerators wrote down students' answers. We find that high-SES students outperform low-SES ones in generating diverse ideas only when they read the prompt; the relationship is flipped when performance does not depend on reading ability.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Divergent thinking responses were scored, possibly by an LLM with human validation; the abstract mentions no LLM scoring method.

**Решение:** =

---

### 207 · R10870

**ChatGPT for Education Research: Exploring the Potential of Large Language Models for Qualitative Codebook Development**

2024 · Lecture notes in computer science · journalarticle, conference, conference-paper · en · https://doi.org/10.1007/978-3-031-64299-9_10

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; ChatGPT codebook development for education qualitative data, so the psychological construct and the human coding comparison are both unclear.

**Решение:** =

---

### 208 · R10871

**Discipline-Driven AI: Training a GPT to Qualitatively Code for Technical and Professional Communication Research**

2024 · ACM International Conference on Design of Communication (SIGDOC) · journalarticle, book, conference · en · https://doi.org/10.1145/3641237.3691686

This project reports on the process used to train an AI model for qualitative coding and lessons learned for AI utilization in discipline-specific qualitative research. Interdisciplinary scholars are assessing the role of AI in qualitative coding processes, analyzing tools such as Cody [1], PaTAT [2] and ChatGPT3 [3]. Early findings suggest that emerging AI technology may contribute to qualitative coding by providing new insights [2] and increasing intercoder reliability [1], among other benefits. Though important, the sustained attention to the outcomes of AI-assisted coding provides little insight into the processes, successes, and failures during the training process. By focusing on process, researchers can better formulate strategies for AI-assisted coding. This project highlights researchers’ experiences training an AI with a disciplinary-specific knowledge base to support qualitative coding.

**ИИ:** ? · обе модели · неясен конструкт · GPT trained for qualitative coding in technical communication research; unclear if the construct is psychological or whether agreement with human coders is reported.

**Решение:** =

---

### 209 · R10876

**Training LLMs to Recognize Hedges in Spontaneous Narratives**

2024 · arXiv (Cornell University) · journalarticle, text/article, preprint · en · https://doi.org/10.48550/arxiv.2408.03319

Hedges allow speakers to mark utterances as provisional, whether to signal non-prototypicality or "fuzziness", to indicate a lack of commitment to an utterance, to attribute responsibility for a statement to someone else, to invite input from a partner, or to soften critical feedback in the service of face-management needs. Here we focus on hedges in an experimentally parameterized corpus of 63 Roadrunner cartoon narratives spontaneously produced from memory by 21 speakers for co-present addressees, transcribed to text (Galati and Brennan, 2010). We created a gold standard of hedges annotated by human coders (the Roadrunner-Hedge corpus) and compared three LLM-based approaches for hedge detection: fine-tuning BERT, and zero and few-shot prompting with GPT-4o and LLaMA-3. The best-performing approach was a fine-tuned BERT model, followed by few-shot GPT-4o. After an error analysis on the top performing approaches, we used an LLM-in-the-Loop approach to improve the gold standard coding, as well as to highlight cases in which hedges are ambiguous in linguistically interesting ways that will guide future research. This is the first step in our research program to train LLMs to interpret and generate collateral signals appropriately and meaningfully in conversation. Amie Paige, Adil Soubki, and John Murzaku contributed equally to this study

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-4o and LLaMA-3 detect hedges in narrative transcripts against a human gold standard; hedging is a linguistic/interpersonal construct of borderline psychological relevance.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs detect hedges against human annotations, but hedging is a linguistic/pragmatic feature of cartoon narratives, not a psychological or clinical construct.)

**Решение:** -

---

### 210 · R10889

**Using Large Language Models for Understanding Narrative Discourse**

2024 · Underline Science Inc. · audiovisual/conference talk, conference-paper · en · https://doi.org/10.18653/v1/2024.wnu-1.4

In this study, we explore the application of large language models (LLMs) to analyze narrative discourse within the framework established by the field of narratology. We develop a set of elementary narrative features derived from prior theoretical work that focus on core dimensions of narrative, including time, setting, and perspective. Through experiments with GPT-4 and fine-tuned open-source models like Llama3, we demonstrate the models' ability to annotate narrative passages with reasonable levels of agreement with human annotators. Leveraging a dataset of human-annotated passages spanning 18 distinct narrative and non-narrative genres, our work provides empirical support for the deictic theory of narrative communication. This theory posits that a fundamental function of storytelling is the focalization of attention on distant human experiences to facilitate social coordination. We conclude with a discussion of the possibilities for LLM-driven narrative discourse understanding.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-4/Llama3 annotations of narrative passages compared with human annotators; the narratological features may or may not count as psychological constructs.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: GPT-4/Llama3 annotate narratological features (time, setting, perspective) against human annotators, but these are literary and linguistic, not psychological or clinical constructs.)

**Решение:** -

---

### 211 · R10906

**Understanding the Therapeutic Relationship between Counselors and Clients in Online Text-based Counseling using LLMs**

2024 · arXiv.org · journalarticle, conference, preprint/article · en · https://doi.org/10.18653/v1/2024.findings-emnlp.69

Robust therapeutic relationships between counselors and clients are fundamental to counseling effectiveness. The assessment of therapeutic alliance is well-established in traditional face-to-face therapy but may not directly translate to text-based settings. With millions of individuals seeking support through online text-based counseling, understanding the relationship in such contexts is crucial. In this paper, we present an automatic approach using large language models (LLMs) to understand the development of therapeutic alliance in text-based counseling. We adapt a theoretically grounded framework specifically to the context of online text-based counseling and develop comprehensive guidelines for characterizing the alliance. We collect a comprehensive counseling dataset and conduct multiple expert evaluations on a subset based on this framework. Our LLM-based approach, combined with guidelines and simultaneous extraction of supportive evidence underlying its predictions, demonstrates effectiveness in identifying the therapeutic alliance. Through further LLM-based evaluations on additional conversations, our findings underscore the challenges counselors face in cultivating strong online relationships with clients. Furthermore, we demonstrate the potential of LLM-based feedback mechanisms to enhance counselors' ability to build relationships, supported by a small-scale proof-of-concept. Accepted to EMNLP Findings 2024. 24 pages, 6 figures, 9 tables

**ИИ:** + · обе модели · кодирование сессий · An LLM rates therapeutic alliance in text-based counselling conversations, and the abstract says the same subset was evaluated by experts.

**Решение:** =

---

### 212 · R1091

**Validation of the safety, empathy and utility of a large language model conversation agent for parents of autistic and neurodivergent children.**

2026 · Scientific reports · journal article, validation study, journalarticle · eng · https://doi.org/10.1038/s41598-026-44254-5

This paper presents three descriptive validation studies of a large language model (LLM) conversation agent designed to support families and carers with autistic children. In the first study, a LLM’s responses to 400 parent/carer questions were assessed against 10 criteria across 3 domains—safety, empathy and utility by experienced human evaluators. In the second study, the LLM’s capacity to identify safeguarding issues was evaluated. In the third study, the responses to 50 parent/carer questions from the LLM and health clinicians were blind rated by an experienced evaluator and compared. The LLM’s responses were rated as safe, empathetic and useful. The LLM identified and correctly flagged the safeguarding issue in 100% of the presented questions. The ratings for LLM and clinician’s responses were highly correlated and the evaluator was able to distinguish which the provenance of the responses (74%). This is the first deployment of a comprehensive evaluation model that uses human ratings to scrutinize the output of LLM designed to support families with autistic children. It provides a demonstration of how LLMs have the potential to be safe, empathetic and clinically useful tools for responding to the unmet support needs of parents and carers of autistic children.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: Mainly humans rating LLM responses, but Study 2 has the LLM flagging safeguarding risk in parent questions; unclear whether reference labels came from human coders.); Sonnet -2 (люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает: Human evaluators rate LLM chatbot responses for safety, empathy and utility; the LLM does not rate texts against human labels. The safeguarding flagging test is a minor part.)

**Решение:** -

---

### 213 · R10916

**Towards a Multidimensional Evaluation Framework for Empathetic Conversational Systems**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2407.18538

Empathetic Conversational Systems (ECS) are built to respond empathetically to the user's emotions and sentiments, regardless of the application domain. Current ECS studies evaluation approaches are restricted to offline evaluation experiments primarily for gold standard comparison &amp; benchmarking, and user evaluation studies for collecting human ratings on specific constructs. These methods are inadequate in measuring the actual quality of empathy in conversations. In this paper, we propose a multidimensional empathy evaluation framework with three new methods for measuring empathy at (i) structural level using three empathy-related dimensions, (ii) behavioral level using empathy behavioral types, and (iii) overall level using an empathy lexicon, thereby fortifying the evaluation process. Experiments were conducted with the state-of-the-art ECS models and large language models (LLMs) to show the framework's usefulness. 13 pages, 4 figures

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLMs are the systems being evaluated for empathetic responses. The abstract does not describe an LLM rating empathy against human coding.); Sonnet ? (неясно, сравнивали ли с людьми: Empathy evaluation framework for conversational systems tested with LLMs; unclear whether LLM ratings are compared against human labels.)

**Решение:** -

---

### 214 · R10917

**ChatGPT Label: Comparing the Quality of Human-Generated and LLM-Generated Annotations in Low-Resource Language NLP Tasks**

2024 · IEEE Access · journalarticle, article · en · https://doi.org/10.1109/access.2024.3402809

This research paper presents a comprehensive comparative study assessing the quality of annotations in Turkish, Indonesian, and Minangkabau Natural Language Processing (NLP) tasks, with a specific focus on the contrast between annotations generated by human annotators and those produced by Large Language Models (LLMs). In the context of NLP, high-quality annotations play a pivotal role in training and evaluating machine-learning models. The study encompasses three core NLP tasks: topic classification, tweet sentiment analysis, and emotion classification, each reflecting a distinct aspect of text analysis. The research methodology incorporates a meticulously curated dataset sourced from a variety of text data, spanning diverse topics and emotions. Human annotators, proficient in the Turkish, Indonesian, and Minangkabau language, were tasked with producing high-quality annotations, adhering to comprehensive annotation guidelines. Additionally, fine-tuned Turkish LLMs were employed to generate annotations for the same tasks. The evaluation process employed precision, recall, and F1-score metrics, tailored to each specific NLP task. The findings of this study underscore the nuanced nature of annotation quality. While LLM-generated annotations demonstrated competitive quality, particularly in sentiment analysis, human-generated annotations consistently outperformed LLM-generated ones in more intricate NLP tasks. The observed differences highlight LLM limitations in understanding context and addressing ambiguity. This research contributes to the ongoing discourse on annotation sources in Turkish, Indonesian, and Minangkabau NLP, emphasizing the importance of judicious selection between human and LLM-generated annotations. It also underscores the necessity for continued advancements in LLM capabilities, as they continue to reshape the landscape of data annotation in NLP and machine learning.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: ChatGPT/LLM emotion classification of tweets compared against human annotations using the same guidelines; emotion counts as a psychological construct.); Sonnet ? (неясен конструкт: Compares LLM and human annotations including emotion classification of tweets, but mostly generic NLP tasks, and it's unclear whether the "fine-tuned Turkish LLMs" are generative models.)

**Решение:** ?

---

### 215 · R10921

**Inductive Coding with ChatGPT - An Evaluation of Different GPT Models Clustering Qualitative Data into Categories**

2024 · Center for Open Science · posted-content · https://doi.org/10.31219/osf.io/gpnye

Arlinghaus CS, Wulff C, Maier GW. Inductive Coding with ChatGPT - An Evaluation of Different GPT Models Clustering Qualitative Data into Categories. OSF Preprints. 2024.Qualitative data is invaluable, yet its analysis is very time-consuming. To prevent the loss of valuable information and to streamline the coding process for developing and assigning inductive categories, we introduce LLM-Assisted Inductive Categorization (LAIC), a novel method of categorizing text responses using a Large Language Model (LLM). In two pre-registered studies, we tested two Generative Pre-trained Transformer (GPT) models that are commonly used in ChatGPT (GPT-3.5 Turbo and GPT-4o) across three temperature settings (0, 0.5, 1) with 10 repetitions each (120 runs in total). Outputs were evaluated based on established qualitative research criteria (credibility, dependability, confirmability, transferability, transparency). Two human coders also generated inductive categories and assigned text responses accordingly for comparison. Our findings demonstrate that both GPT models are highly effective in developing and assigning inductive categories, even outperforming human coders in agreement rates. Overall, GPT-4o achieved the best results (e.g., better explanations and higher agreement) and is recommended for inductive category formation and assignment with a temperature setting of 0 and 10 repetitions. This approach saves significant time and resources while enhancing analysis quality. Instructions and Python scripts for applying our new coding technique are freely available under a CC-BY 4.0 International license: https://osf.io/h4dux

**ИИ:** ? · обе модели · неясен конструкт · GPT models assign text responses to categories and are compared with human coders' agreement, but the abstract doesn't say whether the content is psychological.

**Решение:** =

---

### 216 · R10922

**Revolutionizing Qualitative Human-Robot Interaction Research by Using GPT Models for Inductive Category Development**

2024 · Zenodo · conferencepaper/ · https://doi.org/10.5281/zenodo.13693979

Coding qualitative data is essential but time-consuming. This late-breaking report presents a new method for developing inductive categories utilizing GPT models. We examined two different GPT models (gpt-3.5-turbo-0125 and gpt-4o-2024-05-03) and three temperature settings (0, 0.5, 1), each with ten repetitions. The generated categories were fairly consistent across settings, although higher temperatures included less relevant aspects. The agreement for GPT-generated category assignments exceeded that of human coders, with the best performance observed at temperature setting 0. Thus, we recommend using a GPT model with the temperature setting 0 to create and assign inductive categories for qualitative data.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · GPT assigns inductive categories to HRI qualitative data. Unclear whether LLM-human agreement is reported and whether the construct is psychological.

**Решение:** =

---

### 217 · R10927

**Illuminate a Novel Approach for Depression Detection with Explainable Analysis and Proactive Therapy using Prompt Engineering.**

2024 · International Journal of Psychiatry · journalarticle, article · en · https://doi.org/10.33140/ijp.09.02.02

Traditional methods of depression detection on social media forums can classify whether a user is depressed, but they often lack the capacity for human-like explanations and interactions. This paper proposes a next-generation paradigm for depression detection and treatment strategies. This research employs three advanced Large Language Models (LLMs) - Generative Pretrained Transformer 4 (GPT - 4), Llama 2 chat, and Gemini, each fine-tuned using specially engineered prompts to effectively diagnose, explain, and suggest therapeutic interventions for depression. These prompts are designed to guide the models in analyzing textual data from clinical interviews and online forums, ensuring nuanced and context-aware responses. The study introduces a novel approach to prompt engineering, utilizing a few-shot prompting methodology for the Diagnosis and Explanation component. This technique is optimized to provide Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, (DSM-5) based analysis and explanation, enhancing the model’s ability to identify and articulate depressive symptoms accurately. For the Interaction and Learning aspect, the models engage in empathetic dialogue management, guided by resources from Psychology Database and a Cognitive Behavioral Therapy (CBT) guide. This facilitates meaningful interactions with individuals facing major depressive disorders, fostering a supportive and understanding environment. Furthermore, the research innovates in Case Conceptualization and Treatment, creating the Illuminate Database to guide the models in offering personalized therapy. This database is enriched with various CBT modules, encompassing case conceptualization, treatment planning, and therapeutic techniques. The models utilize this information to offer structured, actionable steps for addressing mental health issues. The quantitative analysis of the study highlights the effectiveness of these LLMs, demonstrated through metrics such as F1 scores, Precision, Recall, Cosine similarity, and Recall-Oriented Understudy for Gisting Evaluation (ROUGE) across different test sets. This comprehensive approach, blending cutting-edge AI with established psychological methodologies, illuminates new possibilities in mental health care, showcasing the potential of LLMs in revolutionizing diagnosis and treatment strategies.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · GPT-4/Llama/Gemini detect depression in interviews and forum posts using F1; unclear whether labels come from human annotation or self-report/diagnosis.

**Решение:** =

---

### 218 · R10928

**Illuminate: Depression diagnosis, explanation and proactive therapy using prompt engineering**

2024 · Journal of Student Research · journalarticle, article · en · https://doi.org/10.47611/jsrhs.v13i2.6718

Traditional methods of depression detection on social media forums can classify whether a user is depressed, but they often lack the capacity for human-like explanations and interactions. This paper proposes a next-generation paradigm for depression detection and treatment strategies. It employs three Large Language Models (LLMs) - Generative Pre-trained Transformer 4, Llama, and Gemini, each fine-tuned using specially engineered prompts to effectively diagnose, explain, and suggest therapeutic interventions for depression. These prompts are designed to guide the models in analyzing textual data from clinical interviews and online forums, ensuring nuanced and context-aware responses. The study utilizes a few-shot prompting methodology for the Diagnosis and Explanation component. This technique is optimized to provide DSM-5 based analysis and explanation, enhancing the model’s ability to identify and articulate depressive symptoms accurately. Models engage in empathetic dialogue management, guided by resources from Psychology Database and a Cognitive Behavioral Therapy guide, and fine-tuned using Chain of Thought and Tree of Thought prompting techniques. This facilitates meaningful interactions with individuals facing major depressive disorders, fostering a supportive and understanding environment. The research innovates in case conceptualization, treatment planning and therapeutic interventions by creating the Illuminate Database to guide the models in offering personalized therapy. The quantitative analysis of the study is demonstrated through metrics such as F1 scores, Precision, Recall, Cosine similarity, and ROUGE score across different test sets. This comprehensive approach offered through a mobile application prototype, with established psychological methodologies showcases the potential of LLMs in revolutionizing diagnosis and treatment strategies.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs detect depression in interview and forum text (F1 reported), but it is unclear whether the reference labels come from human coders or from self-report/diagnosis.

**Решение:** =

---

### 219 · R10948

**AI-Supported Diagnostic of Depression Using Clinical Interviews: A Pilot Study**

2024 · VISIGRAPP · journalarticle · https://doi.org/10.5220/0012439700003660

: In the face of rising depression rates, the urgency of early and accurate diagnosis has never been more paramount. Traditional diagnostic methods, while invaluable, can sometimes be limited in access and susceptible to biases, potentially leading to underdiagnoses. This paper explores the innovative potential of AI technology, specifically machine learning, as a diagnostic tool for depression. Drawing from prior research, we note the success of machine learning in discerning depression indicators on social media platforms and through automated interviews. A particular focus is given to the BERT -based NLP transformer model, previously shown to be effective in detecting depression from simulated interview data. Our study assessed this model’s capability to identify depression from transcribed, semi-structured clinical interviews within a general population sample. While the BERT model displayed an accuracy of 0.71, it was surpassed by an untrained GPT - 3.5 model, which achieved an impressive accuracy of 0.88. These findings emphasise the transformative potential of NLP transformer models in the realm of depression detection. However, given the relatively small dataset ( N = 17 ) utilised, we advise a measured interpretation of the results. This paper is designed as a pilot study, and further studies will incorporate bigger datasets.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · GPT-3.5 detects depression from clinical interview transcripts; unclear if the reference is a clinician's rating of the same interview or a separate diagnosis.

**Решение:** =

---

### 220 · R10961

**ChatGPT for Automated Qualitative Research: Content Analysis.**

2024 · Journal of medical Internet research · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.2196/59050

BACKGROUND: Data analysis approaches such as qualitative content analysis are notoriously time and labor intensive because of the time to detect, assess, and code a large amount of data. Tools such as ChatGPT may have tremendous potential in automating at least some of the analysis. OBJECTIVE: The aim of this study was to explore the utility of ChatGPT in conducting qualitative content analysis through the analysis of forum posts from people sharing their experiences on reducing their sugar consumption. METHODS: Inductive and deductive content analysis were performed on 537 forum posts to detect mechanisms of behavior change. Thorough prompt engineering provided appropriate instructions for ChatGPT to execute data analysis tasks. Data identification involved extracting change mechanisms from a subset of forum posts. The precision of the extracted data was assessed through comparison with human coding. On the basis of the identified change mechanisms, coding schemes were developed with ChatGPT using data-driven (inductive) and theory-driven (deductive) content analysis approaches. The deductive approach was informed by the Theoretical Domains Framework using both an unconstrained coding scheme and a structured coding matrix. In total, 10 coding schemes were created from a subset of data and then applied to the full data set in 10 new conversations, resulting in 100 conversations each for inductive and unconstrained deductive analysis. A total of 10 further conversations coded the full data set into the structured coding matrix. Intercoder agreement was evaluated across and within coding schemes. ChatGPT output was also evaluated by the researchers to assess whether it reflected prompt instructions. RESULTS: The precision of detecting change mechanisms in the data subset ranged from 66% to 88%. Overall κ scores for intercoder agreement ranged from 0.72 to 0.82 across inductive coding schemes and from 0.58 to 0.73 across unconstrained coding schemes and structured coding matrix. Coding into the best-performing coding scheme resulted in category-specific κ scores ranging from 0.67 to 0.95 for the inductive approach and from 0.13 to 0.87 for the deductive approaches. ChatGPT largely followed prompt instructions in producing a description of each coding scheme, although the wording for the inductively developed coding schemes was lengthier than specified. CONCLUSIONS: ChatGPT appears fairly reliable in assisting with qualitative analysis. ChatGPT performed better in developing an inductive coding scheme that emerged from the data than adapting an existing framework into an unconstrained coding scheme or coding directly into a structured matrix. The potential for ChatGPT to act as a second coder also appears promising, with almost perfect agreement in at least 1 coding scheme. The findings suggest that ChatGPT could prove useful as a tool to assist in each phase of qualitative content analysis, but multiple iterations are required to determine the reliability of each stage of analysis.

**ИИ:** + · обе модели · кодирование по кодбуку · ChatGPT coded forum posts for behaviour-change mechanisms; extraction precision checked against human coding. Kappas may be ChatGPT–ChatGPT only.

**Решение:** =

---

### 221 · R10966

**RESEMO: A Benchmark Chinese Dataset for Studying Responsive Emotion from Social Media Content**

2024 · Annual Meeting of the Association for Computational Linguistics · journalarticle, conference, conference-paper · en · https://doi.org/10.18653/v1/2024.findings-acl.970

On social media platforms, users’ emotions are triggered when they encounter particular content from other users, where such emotions are different from those that spontaneously emerged, owing to the “responsive” nature. Analyzing the aforementioned responsive emotions from user interactions is a task of significant importance for understanding human cognition, the mechanisms of emotion generation, behavior on the Internet, etc. Performing the task with artificial intelligence generally requires human-annotated data to help train a well-performing system, while existing data resources do not cover this specific area, with none of them focusing on responsive emotion analysis. In this paper, we propose a Chinese dataset named R ES E MO for responsive emotion analysis, including 3,813 posts with 68,781 comments collected from Weibo, the largest social media platform in China. R ES E MO contains three types of human annotations with respect to responsive emotions, namely, responsive relationship, responsive emotion cause, and responsive emotion category. Moreover, to test this dataset, we build large language model (LLM) baseline methods for responsive relation extraction, responsive emotion cause extraction, and responsive emotion detection, which show the potential of the proposed R E - S E MO being a benchmark for future studies on responsive emotions.

**ИИ:** + · обе модели · бенчмарк с метками людей · Benchmark dataset of human-annotated responsive emotions in Weibo comments; LLM baselines evaluated against the human labels.

**Решение:** =

---

### 222 · R1097

**Decoding the phenomenology of spontaneous thought using large language-model ratings on verbal retrospective free reports**

2026 · bioRxiv · preprint, ppr · https://doi.org/10.64898/2026.04.22.720079

A bstract Spontaneous thoughts constitute most of everyday inner experience, yet long-standing methodological challenges obscure a thorough exploration of their content and neurophysiological underpinnings. Traditional approaches relying on thought probes impose strict constraints on phenomenological reports, whereas online verbal reports disrupt the natural flow of experience while interfering neural signals with motor artifacts. Here, we designed and tested an alternative approach to assess the neural basis of spontaneous thoughts combining delayed verbal retrospective free reports (RFR) with automated phenomenological ratings generated by large language models (LLMs). Twenty-two participants performed an eyes-closed free-thinking task, providing reports that were evaluated along ten phenomenological dimensions by four state-of-the-art LLMs and a panel of human raters. Machine-learning models (ML) were then trained to decode LLM-derived ratings from EEG spectral, complexity, and connectivity features. Our analyses showed that inter-rater agreement among LLMs exceeded that of human raters whereas ML models achieved above-chance accuracy for the prediction of emotional valence. These findings provide support for the use of LLMs for a scalable phenomenological annotation of spontaneous thoughts and suggest that their affective dimensions can be decoded from concurrent EEG activity.

**ИИ:** + · обе модели · кодирование по кодбуку · Four LLMs and a human rater panel scored thought reports on ten phenomenological dimensions; LLM–human agreement can likely be extracted.

**Решение:** =

---

### 223 · R10972

**Can Large Language Models Understand You Better? An MBTI Personality Detection Dataset Aligned with Population Traits**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2412.12510

The Myers-Briggs Type Indicator (MBTI) is one of the most influential personality theories reflecting individual differences in thinking, feeling, and behaving. MBTI personality detection has garnered considerable research interest and has evolved significantly over the years. However, this task tends to be overly optimistic, as it currently does not align well with the natural distribution of population personality traits. Specifically, (1) the self-reported labels in existing datasets result in incorrect labeling issues, and (2) the hard labels fail to capture the full range of population personality distributions. In this paper, we optimize the task by constructing MBTIBench, the first manually annotated high-quality MBTI personality detection dataset with soft labels, under the guidance of psychologists. As for the first challenge, MBTIBench effectively solves the incorrect labeling issues, which account for 29.58% of the data. As for the second challenge, we estimate soft labels by deriving the polarity tendency of samples. The obtained soft labels confirm that there are more people with non-extreme personality traits. Experimental results not only highlight the polarized predictions and biases in LLMs as key directions for future research, but also confirm that soft labels can provide more benefits to other psychological tasks than hard labels. The code and data are available at https://github.com/Personality-NLP/MbtiBench. Accepted by COLING 2025. 28 papges, 20 figures, 10 tables

**ИИ:** + · обе модели · бенчмарк с метками людей · Benchmark of MBTI personality detection with psychologist-guided manual annotations; LLMs evaluated against human labels.

**Решение:** =

---

### 224 · R10973

**Language models (mostly) do not consider emotion triggers while predicting emotion**

2024 · The University of Texas at Austin · dissertation/thesis · https://doi.org/10.26153/tsw/55861

Situations and events evoke emotions in humans, but to what extent do they inform the prediction of emotion detection models? This work investigates how well human-annotated emotion triggers correlate with features that models deemed salient in their prediction of emotions. First, we introduce a novel dataset EmoTrigger, consisting of 900 social media posts sourced from three different datasets; these were annotated by experts for emotion triggers with high agreement. Using EmoTrigger, we evaluate the ability of large language models (LLMs) to identify emotion triggers, and conduct a comparative analysis of the features considered important for these tasks between LLMs and fine-tuned models. Our analysis reveals that emotion triggers are largely not considered salient features for emotion prediction models, instead there is intricate interplay between various features and the task of emotion detection. As an extension of our work, we also present the preliminary findings of our analysis of the ability of multimodal models to predict emotions and accurately identify triggers from memes.

**ИИ:** + · обе модели · бенчмарк с метками людей · LLMs identify emotion triggers in social media posts and are evaluated against the expert-annotated EmoTrigger dataset.

**Решение:** =

---

### 225 · R10978

**Extracting Social Support and Social Isolation Information from Clinical Psychiatry Notes: Comparing a Rule-based NLP System and a Large Language Model**

2024 · arXiv · text/article, preprint · https://doi.org/10.48550/arxiv.2403.17199

Background: Social support (SS) and social isolation (SI) are social determinants of health (SDOH) associated with psychiatric outcomes. In electronic health records (EHRs), individual-level SS/SI is typically documented as narrative clinical notes rather than structured coded data. Natural language processing (NLP) algorithms can automate the otherwise labor-intensive process of data extraction. Data and Methods: Psychiatric encounter notes from Mount Sinai Health System (MSHS, n=300) and Weill Cornell Medicine (WCM, n=225) were annotated and established a gold standard corpus. A rule-based system (RBS) involving lexicons and a large language model (LLM) using FLAN-T5-XL were developed to identify mentions of SS and SI and their subcategories (e.g., social network, instrumental support, and loneliness). Results: For extracting SS/SI, the RBS obtained higher macro-averaged f-scores than the LLM at both MSHS (0.89 vs. 0.65) and WCM (0.85 vs. 0.82). For extracting subcategories, the RBS also outperformed the LLM at both MSHS (0.90 vs. 0.62) and WCM (0.82 vs. 0.81). Discussion and Conclusion: Unexpectedly, the RBS outperformed the LLMs across all metrics. Intensive review demonstrates that this finding is due to the divergent approach taken by the RBS and LLM. The RBS were designed and refined to follow the same specific rules as the gold standard annotations. Conversely, the LLM were more inclusive with categorization and conformed to common English-language understanding. Both approaches offer advantages and are made available open-source for future testing. 2 figures, 3 tables

**ИИ:** разошлись — Opus ? (другое: FLAN-T5-XL extracts social support and isolation from psychiatric notes against a human-annotated gold standard; unclear whether an encoder-decoder T5 counts as an LLM.); Sonnet + (клиническая оценка: FLAN-T5-XL labels social support/isolation in psychiatric notes against a human-annotated gold standard. FLAN-T5 is encoder-decoder, so the model type is borderline.)

**Решение:** ?

---

### 226 · R10981

**Generation, Distillation and Evaluation of Motivational Interviewing-Style Reflections with a Foundational Language Model**

2024 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2402.01051

Large Foundational Language Models are capable of performing many tasks at a high level but are difficult to deploy in many applications because of their size and proprietary ownership. Many will be motivated to distill specific capabilities of foundational models into smaller models that can be owned and controlled. In the development of a therapeutic chatbot, we wish to distill a capability known as reflective listening, in which a therapist produces reflections of client speech. These reflections either restate what a client has said, or connect what was said to a relevant observation, idea or guess that encourages and guides the client to continue contemplation. In this paper, we present a method for distilling the generation of reflections from a Foundational Language Model (GPT-4) into smaller models. We first show that GPT-4, using zero-shot prompting, can generate reflections at near 100% success rate, superior to all previous methods. Using reflections generated by GPT-4, we fine-tune different sizes of the GPT-2 family. The GPT-2-small model achieves 83% success on a hold-out test set and the GPT-2 XL achieves 90% success. We also show that GPT-4 can help in the labor-intensive task of evaluating the quality of the distilled models, using it as a zero-shot classifier. Using triple-human review as a guide, the classifier achieves a Cohen-Kappa of 0.66, a substantial inter-rater reliability figure. Accepted to EACL 2024 Long Paper

**ИИ:** + · обе модели · LLM-судья · GPT-4 used as a zero-shot classifier of MI reflection quality, compared against triple-human review; Cohen's kappa = 0.66.

**Решение:** =

---

### 227 · R10982

**Decoding Moral Reasoning in Ai: A Quantitative Analysis of Few-Shot Learning Models of GPT**

2024 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5019221

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; few-shot GPT moral reasoning could be classifying moral content of texts against human labels, or just probing the model itself.

**Решение:** =

---

### 228 · R10989

**Large language models and humans converge in judging public figures' personalities.**

2024 · PNAS nexus · journal article, journalarticle, preprint · eng · https://doi.org/10.1093/pnasnexus/pgae418

Abstract ChatGPT-4 and 600 human raters evaluated 226 public figures’ personalities using the Ten-Item Personality Inventory. The correlation between ChatGPT-4 and aggregate human ratings ranged from r = 0.76 to 0.87, outperforming the models specifically trained to make such predictions. Notably, the model was not provided with any training data or feedback on its performance. We discuss the potential explanations and practical implications of ChatGPT-4's ability to mimic human responses accurately.

**ИИ:** разошлись — Opus -7 (другое — напишите почему: GPT-4 and humans rate public figures' personalities from general knowledge, not by coding psychological text; the LLM codes no text units.); Sonnet ? (неясен конструкт: ChatGPT-4 and humans rated public figures' personality with the TIPI and were compared. The abstract doesn't say whether any text was rated, so it may be knowledge-based rating rather than text coding.)

**Решение:** -

---

### 229 · R1099

**From Narrative to Numbers: Evaluating Large Language Models for Ordinal Qualitative Coding of Likert-Type Responses (Preprint)**

2026 · JMIR Publications Inc. · posted-content, preprint · https://doi.org/10.2196/preprints.98538

BACKGROUND Qualitative analysis helps interpret complex human experiences by identifying patterns not easily captured through quantitative measures. However, when applied at scale in healthcare and health professions education, qualitative coding is a labor-intensive task. As a result, large volumes of narrative data are often underutilized or inefficiently analyzed. Recent advances in artificial intelligence, particularly large language models (LLMs), have introduced new opportunities for scaling qualitative analysis through automated processing of narrative text. Prior work has demonstrated that LLMs can approximate human judgments across qualitative and evaluative applications, including thematic analysis and rubric-based assessment. Still, methodological questions remain regarding how these models assign meaning to narrative data and translate it into structured outputs, particularly when mapping responses onto ordinal Likert-type scales. It also remains unclear how prompt design influences the validity, reliability, and stability of LLM-generated qualitative coding. OBJECTIVE This article explores an aspect of AI coding with multiple applications in both research and assessment. Specifically, how effectively can AI interpret Likert-type inferences relative to a human. METHODS This study addresses these gaps by evaluating whether an LLM (Gemini) can infer ordinal Likert-type responses from narrative data. Using a dataset of paired Likert responses and narrative elaborations, multiple prompt conditions were systematically varied to assess their impact on distributional alignment and interrater reliability. RESULTS Across all prompt conditions, Gemini-generated outputs closely approximated the overall distribution of the original self-reported Likert responses while outperforming a human qualitative analyst in distributional alignment. Agreement at the individual response level remained moderate (κw between 0.44 and 0.52), and variations in prompt structure did not produce substantial changes in performance (Krippendorff’s α ranged from 0.69 to 0.76). CONCLUSIONS These findings suggest that LLMs may infer latent meaning structures from narrative data and reproduce aggregate response patterns from an underlying distribution of human responses. LLMs may therefore serve as scalable tools for supporting qualitative coding of ordinal data in healthcare settings when combined with clear processing instructions, structured outputs, and human verification.

**ИИ:** ? · обе модели · неясен конструкт · Gemini coded narrative responses onto Likert scales, compared with a human analyst and self-reports; unclear whether the construct is psychological.

**Решение:** =

---

### 230 · R11002

**A - 133 The Clinical Utility of Large Language Models in Diagnosing Neurocognitive Disorders among NACC Participants**

2024 · Archives of Clinical Neuropsychology · journalarticle, article · en · https://doi.org/10.1093/arclin/acae067.147

Abstract Objective Our study aimed to investigate ChatGPT’s ability to diagnose neurocognitive disorders in older adults based on neuropsychological interviews and test results and compare its accuracy with neuropsychologist consensus diagnosis. Methods We prompted ChatGPT-4 to provide provisional diagnoses (normal changes, mild cognitive impairment, or dementia) for each case. We also asked ChatGPT to diagnose the underlying etiology. We evaluated interrater reliability (IRR) with Cohen’s kappa and a chi-square test. Receiver operating characteristic (ROC) curves and area-under-the-curve (AUC) values were computed to explore measures predicting diagnostic agreement. Results Participants were 15,048 older adults (Mage = 69.13, 56.7% female) assessed in Alzheimer’s Disease Core Centers across the United States. For cognitive diagnoses, Cohen’s kappa demonstrated fair agreement (κ = 0.42; p < 0.001). The chi-square test [χ2 (6) = 7896.51, p < 0.001] revealed a significant and strong association (Cramer’s V = 0.51, p < 0.001) between ChatGPT and clinicians’ diagnoses. For the underlying etiology, Cohen’s kappa demonstrated fair agreement on specific diagnoses (κ = 0.38; p < 0.001). The chi-square test [χ2 (24) = 5353.04, p < 0.001] revealed a significant and strong association (Cramer’s V = 0.30, p < 0.001) between ChatGPT and clinicians’ diagnoses. ROC curves demonstrate that no variables predicted diagnostic agreement at above chance. Conclusion Our findings demonstrate the potential clinical utility of integrating LLMs into neuropsychology. While significant IRR was found between ChatGPT and the neuropsychologist diagnosis, further research is needed prior to the adoption of LLMs into clinical practice, given ongoing developments of artificial intelligence in the field of medicine.

**ИИ:** ? · обе модели · другое · GPT-4 diagnoses vs neuropsychologist consensus from the same case data; unclear if input is text and whether the consensus diagnosis counts as coding.

**Решение:** =

---

### 231 · R11014

**Embedding Democratic Values into Social Media AIs via Societal Objective Functions**

2024 · Proceedings of the ACM on Human-Computer Interaction · journalarticle, review, text/article · en · https://doi.org/10.1145/3641002

Mounting evidence indicates that the artificial intelligence (AI) systems that rank our social media feeds bear nontrivial responsibility for amplifying partisan animosity: negative thoughts, feelings, and behaviors toward political out-groups. Can we design these AIs to consider democratic values such as mitigating partisan animosity as part of their objective functions? We introduce a method for translating established, vetted social scientific constructs into AI objective functions, which we term societal objective functions, and demonstrate the method with application to the political science construct of anti-democratic attitudes. Traditionally, we have lacked observable outcomes to use to train such models-however, the social sciences have developed survey instruments and qualitative codebooks for these constructs, and their precision facilitates translation into detailed prompts for large language models. We apply this method to create a democratic attitude model that estimates the extent to which a social media post promotes anti-democratic attitudes, and test this democratic attitude model across three studies. In Study 1, we first test the attitudinal and behavioral effectiveness of the intervention among US partisans (N=1,380) by manually annotating (alpha=.895) social media posts with anti-democratic attitude scores and testing several feed ranking conditions based on these scores. Removal (d=.20) and downranking feeds (d=.25) reduced participants' partisan animosity without compromising their experience and engagement. In Study 2, we scale up the manual labels by creating the democratic attitude model, finding strong agreement with manual labels (rho=.75). Finally, in Study 3, we replicate Study 1 using the democratic attitude model instead of manual labels to test its attitudinal and behavioral impact (N=558), and again find that the feed downranking using the societal objective function reduced partisan animosity (d=.25). This method presents a novel strategy to draw on social science theory and methods to mitigate societal harms in social media AIs.

**ИИ:** ? · обе модели · неясен конструкт · LLM ratings of anti-democratic attitudes in posts agreed with manual labels (rho=.75); unclear if this political construct counts as psychological (partisan animosity).

**Решение:** =

---

### 232 · R11015

**Prompt-based and Fine-tuned GPT Models for Context-Dependent and -Independent Deductive Coding in Social Annotation**

2024 · International Conference on Learning Analytics and Knowledge · journalarticle, book, conference-paper · en · https://doi.org/10.1145/3636555.3636910

GPT has demonstrated impressive capabilities in executing various natural language processing (NLP) and reasoning tasks, showcasing its potential for deductive coding in social annotations. This research explored the effectiveness of prompt engineering and fine-tuning approaches of GPT for deductive coding of context-dependent and context-independent dimensions. Coding context-dependent dimensions (i.e., Theorizing, Integration, Reflection) requires a contextualized understanding that connects the target comment with reading materials and previous comments, whereas coding context-independent dimensions (i.e., Appraisal, Questioning, Social, Curiosity, Surprise) relies more on the comment itself. Utilizing strategies such as prompt decomposition, multi-prompt learning, and a codebook-centered approach, we found that prompt engineering can achieve fair to substantial agreement with expert-labeled data across various coding dimensions. These results affirm GPT's potential for effective application in real-world coding tasks. Compared to context-independent coding, context-dependent dimensions had lower agreement with expert-labeled data. To enhance accuracy, GPT models were fine-tuned using 102 pieces of expert-labeled data, with an additional 102 cases used for validation. The fine-tuned models demonstrated substantial agreement with ground truth in context-independent dimensions and elevated the inter-rater reliability of context-dependent categories to moderate levels. This approach represents a promising path for significantly reducing human labor and time, especially with large unstructured datasets, without sacrificing the accuracy and reliability of deductive coding tasks in social annotation. The study marks a step toward optimizing and streamlining coding processes in social annotation. Our findings suggest the promise of using GPT to analyze qualitative data and provide detailed, immediate feedback for students to elicit deepening inquiries.

**ИИ:** ? · обе модели · неясен конструкт · GPT codes student annotations against expert labels; the codes include curiosity, surprise and reflection, but the educational framing makes psychological relevance unclear.

**Решение:** =

---

### 233 · R11020

**From Prompt Engineering to Prompt Science With Human in the Loop**

2024 · arXiv (Cornell University) · preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2401.04122

As LLMs make their way into many aspects of our lives, one place that warrants increased scrutiny with LLM usage is scientific research. Using LLMs for generating or analyzing data for research purposes is gaining popularity. But when such application is marred with ad-hoc decisions and engineering solutions, we need to be concerned about how it may affect that research, its findings, or any future works based on that research. We need a more scientific approach to using LLMs in our research. While there are several active efforts to support more systematic construction of prompts, they are often focused more on achieving desirable outcomes rather than producing replicable and generalizable knowledge with sufficient transparency, objectivity, or rigor. This article presents a new methodology inspired by codebook construction through qualitative methods to address that. Using humans in the loop and a multi-phase verification processes, this methodology lays a foundation for more systematic, objective, and trustworthy way of applying LLMs for analyzing data. Specifically, we show how a set of researchers can work through a rigorous process of labeling, deliberating, and documenting to remove subjectivity and bring transparency and replicability to prompt generation process. A set of experiments are presented to show how this methodology can be put in practice.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM codebook labeling is checked against human labeling, but the abstract doesn't say whether the coded data are psychological.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: General methodology for codebook-inspired prompt construction with humans in the loop; the abstract names no psychological or clinical construct or dataset.)

**Решение:** -

---

### 234 · R11056

**Speech and text psychometrics: Identifying suicide risk factors with large language models and acoustic networks**

2024 · Digital Access to Scholarship at Harvard (DASH) (Harvard University) · dissertation · en · https://dash.harvard.edu/bitstreams/fa526c07-ca88-408d-b82a-fb92091ea091/download

Suicide is among the leading causes of death worldwide, with about one death every 11 minutes in the US in recent years. Suicide risk factors such as suicidal ideation, loneliness, and hopelessness have been mainly assessed through rating scales and clinical interviews, which have generally had low accuracy in predicting suicide. One challenge is that suicidal symptoms can be sudden and may not be present during a clinical interview. Another challenge is that many individuals are not receiving regular treatment to be assessed in the first place. Automated risk assessments of suicidal thoughts and behaviors (STBs) and their risk factors could be done more continuously and ecologically outside the clinic by using the speech and text data individuals produce naturally when they use social media, message a friend, journal, or use a crisis counseling service. Clinical assessments could also be enhanced by using speech and text data from therapy sessions and electronic health records. With recent advances in artificial intelligence, this seems promising, but how will we know whether these novel tools are valid? Psychological assessments using speech and natural language processing are generally not evaluated for the types of validity typically expected from screening questionnaires that use rating scales. This may be due to a gap between these fields and psychometrics. This dissertation seeks to bridge this gap. In chapter 1, I use generative AI to automatically build a Suicide Risk Lexicon of 49 risk factors for STBs. This results in an interpretable baseline model that can guarantee flagging certain high-risk language. I validate it with clinician judgments and by demonstrating it can predict imminent suicide risk during crisis counseling sessions. In chapter 2, I try to consolidate Text Psychometrics as the field that studies how to measure psychological constructs in text. I systematically compare a diverse set of models including lexicons, zero-shot deep learning methods, and generative AI on different desirable properties in their ability to predict 13 types of mental health crises. I evaluate clinical utility and introduce content validity test sets as a way to demonstrate whether models detect key expressions of the target variable. In chapter 3, to overcome that fact most approaches to suicide risk assessment use rating scales that simply capture the presence or frequency of STBs, we ask something that is relatively unknown: what are the actual thoughts in suicidal thinking? Participants with STBs answer this question over multiple days, and we compare the validity of categorizing their responses through theory-driven and data-driven methods. Our results reveal that measuring natural language through open-response questions captures suicidal ideation that rating scales miss. In Chapter 4, I analyze the speech patterns of individuals during and after their hospitalizations for suicide risk through daily recordings. I estimate networks of acoustic and psychological variables to capture the dynamic nature of how these variables affect each other over time. I provide a Suicide Speech Model to help explain potential mechanisms by which speech biomarkers could detect changes in STBs. In sum, I provide new methods to measure psychological constructs using speech and text data and lay out novel frameworks to validate these measurements more thoroughly.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Dissertation: generative AI on crisis-counseling text and open suicidal-thought responses; clinician validation mentioned, but unclear whether LLM-human coding agreement is reported.

**Решение:** =

---

### 235 · R11075

**Exploring the Creative Personality: Using Machine Learning to Predict Fluency and Originality in Divergent Thinking**

2024 · Creativity Research Journal · journalarticle, article · en · https://doi.org/10.1080/10400419.2024.2371725

ABSTRACT In this study, 100 self-reported personality items from the Big Five Aspects Scale, responded to by a sample of 334 undergraduate participants, were used to predict quantity (ideational fluency) and quality (originality) of ideas on a divergent thinking (DT) task. The originality of DT responses was scored through a fine-tuned version of the Generative Pre-trained Transformer (GPT) 3.5 (i.e., Ocsai), and a least absolute shrinkage selection operator (LASSO) machine learning model selected the items that were meaningful predictors of each outcome. Results revealed that the personality profiles of highly fluent and highly original individuals were characterized by a tension between seemingly opposed personality attributes. Both ideational fluency and originality were predicted by a playfully open intellectualism that nonetheless avoided more typical work (i.e. was disorderly and unindustrious). Fluency was additionally predicted by a tension between enthusiasm for social interaction and depressive symptoms associated with withdrawal. Originality was predicted by a socially dominant assertiveness that was tempered by awareness and care for others’ feelings (e.g. compassion and politeness) as well as stability (i.e. non-volatility). Taken together, these results demonstrate that the creative personality is likely to be composed of aspects of multiple dimensions of typical personality models like the Big 5, and that the highly fluent and the highly original creative personality is different in important ways.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Fine-tuned GPT-3.5 (Ocsai) scored divergent-thinking originality; the abstract doesn't say whether scores were checked against human raters.); Sonnet -7 (другое — напишите почему: Ocsai (GPT-3.5) scores originality only as an outcome for personality prediction; no human rating comparison is mentioned, so no LLM–human agreement is reported.)

**Решение:** ?

---

### 236 · R11084

**Evaluating Language Models for Assessing Counselor Reflections**

2024 · ACM Transactions on Computing for Healthcare · journalarticle, article · en · https://doi.org/10.1145/3709364

Reflective listening is a fundamental communication skill in behavioral health counseling. It enables counselors to demonstrate an understanding of and empathy for clients’ experiences and concerns. Training to acquire and refine reflective listening skills is essential for counseling proficiency. Yet, it faces significant barriers, notably the need for specialized and timely feedback to improve counseling skills. In this work, we evaluate and compare several computational models, including transformer-based architectures, for their ability to assess the quality of counselors’ reflective listening skills. We explore a spectrum of neural-based models, ranging from compact, specialized RoBERTa models to advanced large-scale language models such as Flan, Mistral, and GPT-3.5, to score psychotherapy reflections. We introduce a psychotherapy dataset that encompasses three basic levels of reflective listening skills. Through comparative experiments, we show that a fine-tuned small RoBERTa model with a custom learning objective (Prompt-Aware margIn Ranking (PAIR)) effectively provides constructive feedback to counselors in training. This study also highlights the potential of machine learning in enhancing the training process for motivational interviewing (MI) by offering scalable and effective feedback alternatives for counseling training.

**ИИ:** + · обе модели · кодирование сессий · Mistral and GPT-3.5 score counselor reflection quality against a human-labeled dataset with three skill levels; includes LLMs alongside RoBERTa.

**Решение:** =

---

### 237 · R11093

**Case Reports Unlocked: Harnessing Large Language Models to Advance Research on Child Maltreatment**

2024 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.4928223

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests LLMs coding child maltreatment case reports, which may include validation against human coders.

**Решение:** =

---

### 238 · R11094

**A step-by-step method for cultural annotation by LLMs.**

2024 · Frontiers in artificial intelligence · journal article, journalarticle, article · eng · https://doi.org/10.3389/frai.2024.1365508

Building on the growing body of research highlighting the capabilities of Large Language Models (LLMs) like Generative Pre-trained Transformers (GPT), this paper presents a structured pipeline for the annotation of cultural (big) data through such LLMs, offering a detailed methodology for leveraging GPT's computational abilities. Our approach provides researchers across various fields with a method for efficient and scalable analysis of cultural phenomena, showcasing the potential of LLMs in the empirical study of human cultures. LLMs proficiency in processing and interpreting complex data finds relevance in tasks such as annotating descriptions of non-industrial societies, measuring the importance of specific themes in stories, or evaluating psychological constructs in texts across societies or historical periods. These applications demonstrate the model's versatility in serving disciplines like cultural anthropology, cultural psychology, cultural history, and cultural sciences at large.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Methods pipeline for GPT annotation of cultural texts, including psychological constructs; validation against human coders likely but not stated.

**Решение:** =

---

### 239 · R11108

**Leveraging Large Language Models for Automating Inductive Qualitative Coding: A Comparative Study of Prompt Engineering Techniques**

2024 · Inquiry Queen s Undergraduate Research Conference Proceedings · journalarticle, conference, conference-paper · en · https://doi.org/10.24908/iqurcp18054

This study explores the potential of Large Language Models (LLMs), like those from the GPT family, to automate inductive qualitative coding—a process of assigning codes to text excerpts and organizing them into categories, traditionally done manually in social science and software engineering research. Our primary question is: Can LLMs effectively automate inductive qualitative coding? To investigate this, we compared different prompt engineering techniques, including Zero-shot, Few-shot, and Chain-of-Thought (CoT) learning, in coding interview transcripts. While LLMs cannot fully replace human coders, they can aid the process with a human-in-the-loop approach. Few-shot learning showed consistent performance with moderate amounts data, while CoT proved most effective in reducing partial hallucinations. Initially aimed at full automation, our study pivoted to testing prompt strategies after realizing that a human-in-the-loop process would offer better accuracy and flexibility, given the challenges of context and token limits in LLMs. These findings suggest that tailored LLM with adequate prompting techniques can help assist researchers when performing qualitative analysis.

**ИИ:** ? · обе модели · неясен конструкт · GPT inductive coding of interview transcripts compared with human coders; the topic of the interviews (psychological or software engineering) is not stated.

**Решение:** =

---

### 240 · R11110

**Decoding Complexity: Exploring Human-AI Concordance in Qualitative Coding**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2403.06607

Qualitative data analysis provides insight into the underlying perceptions and experiences within unstructured data. However, the time-consuming nature of the coding process, especially for larger datasets, calls for innovative approaches, such as the integration of Large Language Models (LLMs). This short paper presents initial findings from a study investigating the integration of LLMs for coding tasks of varying complexity in a real-world dataset. Our results highlight the challenges inherent in coding with extensive codebooks and contexts, both for human coders and LLMs, and suggest that the integration of LLMs into the coding process requires a task-by-task evaluation. We examine factors influencing the complexity of coding tasks and initiate a discussion on the usefulness and limitations of incorporating LLMs in qualitative research.

**ИИ:** ? · обе модели · неясен конструкт · LLM applies a codebook to qualitative data and is compared with human coders, but the dataset's domain and psychological construct are unspecified.

**Решение:** =

---

### 241 · R11118

**MAXIMIZING LEARNING EFFICIENCY WITH LIMITED LABELED DATA: APPLICATIONS TO HEALTHCARE AND EDUCATION**

2024 · Temple University. Libraries · text/none · https://doi.org/10.34944/sc51-wf26

Document classification is essential in domains such as healthcare and education, encompassing three major steps: annotation, training accurate models, and evaluation. Each of these steps is labor-intensive and time-consuming, requiring substantial amounts of labeled data, which is both costly and resource-demanding. This dissertation addresses these challenges by presenting innovative methodologies to enhance annotation efficiency, model training in low-resource settings, and automated scoring. In the healthcare domain, we tackle the challenges of annotation and training with limited resources. First, we develop a visualization approach for rapid labeling of clinical notes for smoking status extraction. The annotation process is labor-intensive and time-consuming; thus, we introduce a tool that accelerates annotation by clustering similar sentences and highlighting important keywords. This reduces the cognitive load on annotators, resulting in faster and more efficient labeling. Next, we address the problem of training accurate classifiers in low-resource settings with limited labeled data. In our first approach, MERIT (Minimal Supervision Through Label Augmentation for Biomedical Relation Extraction), we propose using shortest dependency path (SDP) representation and specific distance thresholds to propagate labels and augment high-quality labeled data. This method improves classifier accuracy compared to using limited labeled data alone. We extend this in our second approach by developing an iterative algorithm to learn automatic thresholds for label propagation. This method is tested in various scenarios, including semi-supervised learning, supervised learning, and in-context learning, demonstrating significant improvements in model performance. In the education domain, we focus on the problem of assessing narratives generated by school-aged children, a task that is both expensive and time-consuming for teachers. We leverage large language models (LLMs) to learn the scoring patterns of teachers accurately, offering a reliable tool for automated narrative scoring. This approach reduces the subjectivity and resource requirements of manual scoring, providing a scalable and consistent alternative. Experimental results across these methodologies demonstrate their effectiveness in improving annotation speed, data utilization, and model accuracy. This dissertation contributes to advancing document classification in low-resource settings, offering practical solutions for critical tasks in healthcare and education.

**ИИ:** ? · обе модели · неясен конструкт · LLMs learn to score children's narratives the way teachers do. Unclear whether this is a psychological/language assessment or just writing-quality grading.

**Решение:** =

---

### 242 · R11119

**Using large language models to evaluate alternative uses task flexibility score**

2024 · Thinking Skills and Creativity · article · en · https://doi.org/10.1016/j.tsc.2024.101549

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; LLM scoring of divergent-thinking (AUT) flexibility likely validated against human raters, but this is unconfirmed.); Sonnet + (подсчёт методики: LLMs scoring flexibility on the Alternative Uses Task (divergent thinking), very likely compared with human scorers; no abstract, but the title fits.)

**Решение:** ?

---

### 243 · R11122

**Can ChatGPT read who you are?**

2024 · Computers in Human Behavior Artificial Humans · journalarticle, text/article, article · en · https://doi.org/10.1016/j.chbah.2024.100088

The interplay between artificial intelligence (AI) and psychology, particularly in personality assessment, represents an important emerging area of research. Accurate personality trait estimation is crucial not only for enhancing personalization in human-computer interaction but also for a wide variety of applications ranging from mental health to education. This paper analyzes the capability of a generic chatbot, ChatGPT, to effectively infer personality traits from short texts. We report the results of a comprehensive user study featuring texts written in Czech by a representative population sample of 155 participants. Their self-assessments based on the Big Five Inventory (BFI) questionnaire serve as the ground truth. We compare the personality trait estimations made by ChatGPT against those by human raters and report ChatGPT\u27s competitive performance in inferring personality traits from text. We also uncover a \u27positivity bias\u27 in ChatGPT\u27s assessments across all personality dimensions and explore the impact of prompt composition on accuracy. This work contributes to the understanding of AI capabilities in psychological assessment, highlighting both the potential and limitations of using large language models for personality inference. Our research underscores the importance of responsible AI development, considering ethical implications such as privacy, consent, autonomy, and bias in AI applications

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · The ground truth is self-reported BFI, but human raters also judged personality from the same texts, so LLM–human agreement may be reported.

**Решение:** =

---

### 244 · R11132

**Measuring Psychological Depth in Language Models**

2024 · arXiv (Cornell University) · journalarticle, conference, preprint · en · https://doi.org/10.48550/arxiv.2406.12680

Evaluations of creative stories generated by large language models (LLMs) often focus on objective properties of the text, such as its style, coherence, and diversity. While these metrics are indispensable, they do not speak to a story's subjective, psychological impact from a reader's perspective. We introduce the Psychological Depth Scale (PDS), a novel framework rooted in literary theory that measures an LLM's ability to produce authentic and narratively complex stories that provoke emotion, empathy, and engagement. We empirically validate our framework by showing that humans can consistently evaluate stories based on PDS (0.72 Krippendorff's alpha). We also explore techniques for automating the PDS to easily scale future analyses. GPT-4o, combined with a novel Mixture-of-Personas (MoP) prompting strategy, achieves an average Spearman correlation of 0.51 with human judgment while Llama-3-70B with constrained decoding scores as high as 0.68 for empathy. Finally, we compared the depth of stories authored by both humans and LLMs. Surprisingly, GPT-4 stories either surpassed or were statistically indistinguishable from highly-rated human-written stories sourced from Reddit. By shifting the focus from text to reader, the Psychological Depth Scale is a validated, automated, and systematic means of measuring the capacity of LLMs to connect with humans through the stories they tell.

**ИИ:** ? · обе модели · неясен конструкт · LLMs rate stories on emotion, empathy and engagement against human ratings; the construct may be story quality rather than a psychological one.

**Решение:** =

---

### 245 · R11146

**Building an extensible, AI-augmented ecological momentary assessment platform**

2024 · dissertation · en · https://doi.org/10.32469/10355/105952

In the rapidly evolving landscape of data-driven research, mobile ecological momentary assessment (EMA) has emerged as a powerful tool for real-time data collection. TigerAware, an advanced system designed for the user-friendly creation and deployment of surveys on mobile devices, has undergone significant enhancements to become a multi-faceted platform. This thesis presents several innovations that leverage advancements in large language models (LLMs) and foundation models to augment TigerAware's capabilities and advance the field of mobile EMA. We developed novel methods for automating the qualitative analysis of unstructured text responses collected through EMA. Our LLM-driven approach, which includes a Keypoints Extractor module and a Keypoints Relevance Evaluator, demonstrated superior performance in extracting concise, relevant keywords and accurately linking free text arguments to their pertinent points. Additionally, we introduced Argument2Code (A2C), a method that utilizes LLMs to automate inductive coding in qualitative data analysis by generating comprehensive codebooks. These advancements significantly enhance the automation and sophistication of the coding process in qualitative research. Furthermore, we proposed FENAP (Foundation Models for Comprehensive Analysis and Prediction of EMA-derived Narratives), which applies the capabilities of foundation models to interpret and analyze EMA data. By transforming raw EMA inputs into structured narratives, FENAP captures detailed behavioral patterns and dynamics, enabling a deeper understanding of human behavior. We implemented this methodology using the diverse UT1000 Project dataset and demonstrated that FENAP outperforms traditional and advanced machine learning baselines in predicting behavioral outcomes. To address critical challenges in privacy protection within EMA, we introduced a novel dataset and a hybrid AI approach that combines DistilBERT and LLaMA models for detecting privacy-sensitive information (PSI). This approach surpassed existing baselines in PSI detection accuracy and provided clearer explanations for model decisions, advancing privacy protection methods in EMA. In addition to these contributions, we made significant enhancements to the user experience, workflow optimization, and software engineering aspects of TigerAware. These improvements include interface refinements, streamlined workflow tools, enhanced communication features, and the incorporation of strong software engineering standards, ensuring TigerAware's reliability, extensibility, and user-friendliness for cutting-edge research. Our contributions underscore TigerAware's evolution into a dynamic and comprehensive EMA platform, ideal for the demands of various research domains. The integration of modern AI technologies, such as LLMs and foundation models, into real-world data collection and analysis platforms demonstrates the immense potential for advancing research in the field of mobile EMA.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM coding of free-text EMA responses (key-point linking, inductive coding); unclear whether this is a psychological construct or compared with human coding.

**Решение:** =

---

### 246 · R11156

**The Value of Generative AI for Qualitative Research: A Pilot Study**

2024 · Journal of Data Science and Intelligent Systems · journalarticle, article, journal-article · en · https://doi.org/10.47852/bonviewjdsis42022964

This mixed-methods approach study investigates the potential of introducing generative AI (ChatGPT 4 and Bard) as part of a deductive qualitative research design that requires coding, focusing on possible gains in cost-effectiveness, coding throughput time, and inter-coder reliability (Cohen’s Kappa). This study involved semi-structured interviews with five domain experts and analyzed a dataset of 122 respondents that required categorization into six predefined categories. The results from using generative AI coders were compared with those from a previous study where human coders carried out the same task. In this comparison, we evaluated the performance of AI-based coders against two groups of human coders, comprising three experts and three non-experts. Our findings support the replacement of human coders with generative AI ones, specifically ChatGPT for deductive qualitative research methods of limited scope. The experimental group, consisting of three independent generative AI coders, outperformed both control groups in coding effort, with a fourfold (4x) efficiency and throughput time (15x) advantage. The latter could be explained by leveraging parallel processing. Concerning expert vs. non-expert coders, minimal evidence suggests a preference for experts. Although experts code slightly faster (17%), their inter-coder reliability showed no substantial advantage. A hybrid approach, combining ChatGPT and domain experts, shows the most promise. This approach reduces costs, shortens project timelines, and enhances inter-coder reliability, as indicated by higher Cohen’s Kappa values. In conclusion, generative AI, exemplified by ChatGPT, offers a viable alternative to human coders, in combination with human research involvement, delivering cost savings and faster research completion without sacrificing notable reliability. These insights, while limited in scope, show potential for further studies with larger datasets, more inductive qualitative research designs, and other research domains.This mixed-methods approach study investigates the potential of introducing generative AI (ChatGPT 4 and Bard) as part of a deductive qualitative research design that requires coding, focusing on possible gains in cost-effectiveness, coding throughput time, and inter-coder reliability (Cohen’s Kappa). This study involved semi-structured interviews with five domain experts and analyzed a dataset of 122 respondents that required categorization into six predefined categories. The results from using generative AI coders were compared with those from a previous study where human coders carried out the same task. In this comparison, we evaluated the performance of AI-based coders against two groups of human coders, comprising three experts and three non-experts. Our findings support the replacement of human coders with generative AI ones, specifically ChatGPT for deductive qualitative research methods of limited scope. The experimental group, consisting of three independent generative AI coders, outperformed both control groups in coding effort, with a fourfold (4x) efficiency and throughput time (15x) advantage. The latter could be explained by leveraging parallel processing. Concerning expert vs. non-expert coders, minimal evidence suggests a preference for experts. Although experts code slightly faster (17%), their inter-coder reliability showed no substantial advantage. A hybrid approach, combining ChatGPT and domain experts, shows the most promise. This approach reduces costs, shortens project timelines, and enhances inter-coder reliability, as indicated by higher Cohen’s Kappa values. In conclusion, generative AI, exemplified by ChatGPT, offers a viable alternative to human coders, in combination with human research involvement, delivering cost savings and faster research completion without sacrificing notable reliability. These insights, while limited in scope, show potential for further studies with larger datasets, more inductive qualitative research designs, and other research domains.A

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT/Bard deductive coding of 122 responses compared with human coders (kappa), but the content domain of the categories is not stated.

**Решение:** =

---

### 247 · R11157

**The Value of Generative AI for Qualitative Research: A Pilot Study**

2024 · Journal of Data Science and Intelligent Systems · article, journal-article · en · https://doi.org/10.47852/bonviewjdsis4202964

This mixed-methods approach study investigates the potential of introducing generative AI (ChatGPT 4 and Bard) as part of a deductive qualitative research design that requires coding, focusing on possible gains in cost-effectiveness, coding throughput time, and inter-coder reliability (Cohen’s Kappa). This study involved semi-structured interviews with five domain experts and analyzed a dataset of 122 respondents that required categorization into six predefined categories. The results from using generative AI coders were compared with those from a previous study where human coders carried out the same task. In this comparison, we evaluated the performance of AI-based coders against two groups of human coders, comprising three experts and three non-experts. Our findings support the replacement of human coders with generative AI ones, specifically ChatGPT for deductive qualitative research methods of limited scope. The experimental group, consisting of three independent generative AI coders, outperformed both control groups in coding effort, with a fourfold (4x) efficiency and throughput time (15x) advantage. The latter could be explained by leveraging parallel processing. Concerning expert vs. non-expert coders, minimal evidence suggests a preference for experts. Although experts code slightly faster (17%), their inter-coder reliability showed no substantial advantage. A hybrid approach, combining ChatGPT and domain experts, shows the most promise. This approach reduces costs, shortens project timelines, and enhances inter-coder reliability, as indicated by higher Cohen’s Kappa values. In conclusion, generative AI, exemplified by ChatGPT, offers a viable alternative to human coders, in combination with human research involvement, delivering cost savings and faster research completion without sacrificing notable reliability. These insights, while limited in scope, show potential for further studies with larger datasets, more inductive qualitative research designs, and other research domains. Received: 30 March 2024 | Revised: 17 May 2024 | Accepted: 18 June 2024 Conflicts of Interest The author declares that he has no conflicts of interest to this work. Data Availability Statement The data that support the findings of this study are not publicly available due to privacy concerns. However, anonymous data are available on request from the corresponding author upon reasonable request. Author Contribution Statement Frédéric Pattyn: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Resources, Data curation, Writing - original draft, Writing - review &amp; editing, Visualization, Project administration.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT/Bard deductive coding compared with human coders using kappa, but the abstract doesn't say whether the categories are psychological.

**Решение:** =

---

### 248 · R11159

**Efficacy of ChatGPT in Cantonese Sentiment Analysis: Comparative Study.**

2024 · Journal of medical Internet research · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.2196/51069

BACKGROUND: Sentiment analysis is a significant yet difficult task in natural language processing. The linguistic peculiarities of Cantonese, including its high similarity with Standard Chinese, its grammatical and lexical uniqueness, and its colloquialism and multilingualism, make it different from other languages and pose additional challenges to sentiment analysis. Recent advances in models such as ChatGPT offer potential viable solutions. OBJECTIVE: This study investigated the efficacy of GPT-3.5 and GPT-4 in Cantonese sentiment analysis in the context of web-based counseling and compared their performance with other mainstream methods, including lexicon-based methods and machine learning approaches. METHODS: We analyzed transcripts from a web-based, text-based counseling service in Hong Kong, including a total of 131 individual counseling sessions and 6169 messages between counselors and help-seekers. First, a codebook was developed for human annotation. A simple prompt ("Is the sentiment of this Cantonese text positive, neutral, or negative? Respond with the sentiment label only.") was then given to GPT-3.5 and GPT-4 to label each message's sentiment. GPT-3.5 and GPT-4's performance was compared with a lexicon-based method and 3 state-of-the-art models, including linear regression, support vector machines, and long short-term memory neural networks. RESULTS: Our findings revealed ChatGPT's remarkable accuracy in sentiment classification, with GPT-3.5 and GPT-4, respectively, achieving 92.1% (5682/6169) and 95.3% (5880/6169) accuracy in identifying positive, neutral, and negative sentiment, thereby outperforming the traditional lexicon-based method, which had an accuracy of 37.2% (2295/6169), and the 3 machine learning models, which had accuracies ranging from 66% (4072/6169) to 70.9% (4374/6169). CONCLUSIONS: Among many text analysis techniques, ChatGPT demonstrates superior accuracy and emerges as a promising tool for Cantonese sentiment analysis. This study also highlights ChatGPT's applicability in real-world scenarios, such as monitoring the quality of text-based counseling services and detecting message-level sentiments in vivo. The insights derived from this study pave the way for further exploration into the capabilities of ChatGPT in the context of underresourced languages and specialized domains like psychotherapy and natural language processing.

**ИИ:** + · обе модели · кодирование сессий · GPT-3.5/4 labeled sentiment of counseling session messages against human codebook annotation; emotional valence in counseling transcripts.

**Решение:** =

---

### 249 · R11168

**MultiWD: Multi-label wellness dimensions in social media posts.**

2024 · Journal of biomedical informatics · journal article, research support, n.i.h., extramural, journalarticle · eng · https://doi.org/10.1016/j.jbi.2024.104586

Background: Halbert L. Dunn’s concept of wellness is a multi-dimensional aspect encompassing social and mental well-being. Neglecting these dimensions over time can have a negative impact on an individual’s mental health. The manual efforts employed in in-person therapy sessions reveal that underlying factors of mental disturbance if triggered, may lead to severe mental health disorders. Objective: In our research, we introduce a fine-grained approach focused on identifying indicators of wellness dimensions and mark their presence in self-narrated human-writings on Reddit social media platform. Design and Method: We present the MultiWD dataset, a curated collection comprising 3281 instances, as a specifically designed and annotated dataset that facilitates the identification of multiple wellness dimensions in Reddit posts. In our study, we introduce the task of identifying wellness dimensions and utilize state-of-the-art classifiers to solve this multi-label classification task. Results: Our findings highlights the best and comparative performance of fine-tuned large language models with fine-tuned BERT model. As such, we set BERT as a baseline model to tag wellness dimensions in a user-penned text with F1 score of 76.69. Conclusion: Our findings underscore the need of trustworthy and domain-specific knowledge infusion to develop more comprehensive and contextually-aware AI models for tagging and extracting wellness dimensions.

**ИИ:** + · обе модели · бенчмарк с метками людей · Annotated Reddit dataset of wellness dimensions; fine-tuned LLMs evaluated against the human labels and compared with a BERT baseline.

**Решение:** =

---

### 250 · R11174

**The Strong Pull of Prior Knowledge in Large Language Models and Its Impact on Emotion Recognition**

2024 · International Conference on Affective Computing and Intelligent Interaction (ACII) · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/acii63134.2024.00041

In-context Learning (ICL) has emerged as a powerful paradigm for performing natural language tasks with Large Language Models (LLM) without updating the models' parameters, in contrast to the traditional gradient-based finetuning. The promise of ICL is that the LLM can adapt to perform the present task at a competitive or state-of-the-art level at a fraction of the cost. The ability of LLMs to perform tasks in this few-shot manner relies on their background knowledge of the task (or task priors). However, recent work has found that, unlike traditional learning, LLMs are unable to fully integrate information from demonstrations that contrast task priors. This can lead to performance saturation at suboptimal levels, especially for subjective tasks such as emotion recognition, where the mapping from text to emotions can differ widely due to variability in human annotations. In this work, we design experiments and propose measurements to explicitly quantify the consistency of proxies of LLM priors and their pull on the posteriors. We show that LLMs have strong yet inconsistent priors in emotion recognition that ossify their predictions. We also find that the larger the model, the stronger these effects become. Our results suggest that caution is needed when using ICL with larger LLMs for affect-centered tasks outside their pre-training domain and when interpreting ICL results. 30 pages, 27 figures

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: LLMs do in-context emotion recognition on text and are evaluated against human emotion annotations; agreement or accuracy is probably reported.); Sonnet ? (неясно, сравнивали ли с людьми: LLM in-context emotion recognition on text, likely scored against human-annotated emotion datasets, but the focus is on prior effects rather than agreement; needs full-text check.)

**Решение:** ?

---

### 251 · R11178

**MTP: A Dataset for Multi-Modal Turning Points in Casual Conversations**

2024 · Annual Meeting of the Association for Computational Linguistics (ACL) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2024.acl-short.30

Detecting critical moments, such as emotional outbursts or changes in decisions during conversations, is crucial for understanding shifts in human behavior and their consequences. Our work introduces a novel problem setting focusing on these moments as turning points (TPs), accompanied by a meticulously curated, high-consensus, human-annotated multi-modal dataset. We provide precise timestamps, descriptions, and visual-textual evidence high-lighting changes in emotions, behaviors, perspectives, and decisions at these turning points. We also propose a framework, TPMaven, utilizing state-of-the-art vision-language models to construct a narrative from the videos and large language models to classify and detect turning points in our multi-modal dataset. Evaluation results show that TPMaven achieves an F1-score of 0.88 in classification and 0.61 in detection, with additional explanations aligning with human expectations. Accepted by ACL 2024 main conference

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Benchmark of human-annotated turning points (shifts in emotion and behaviour) in conversations; LLMs classify and detect them and are scored against human labels.); Sonnet ? (неясен конструкт: Human-annotated benchmark where LLMs classify and detect turning points (emotion, behaviour, decision shifts) in conversations. It's multimodal, and it's unclear whether the construct counts as psychological.)

**Решение:** ?

---

### 252 · R11185

**Deciphering Cognitive Distortions in Patient-Doctor Mental Health Conversations: A Multimodal LLM-Based Detection and Reasoning Framework**

2024 · Conference on Empirical Methods in Natural Language Processing (EMNLP) · journalarticle, conference, conference-paper · en · https://doi.org/10.18653/v1/2024.emnlp-main.1256

Cognitive distortion research holds increasing significance as it sheds light on pervasive errors in thinking patterns, providing crucial insights into mental health challenges and fostering the development of targeted interventions and therapies.This paper delves into the complex domain of cognitive distortions which are prevalent distortions in cognitive processes often associated with mental health issues.Focusing on patient-doctor dialogues, we introduce a pioneering method for detecting and reasoning about cognitive distortions utilizing Large Language Models (LLMs).Operating within a multimodal context encompassing audio, video, and textual data, our approach underscores the critical importance of integrating diverse modalities for a comprehensive understanding of cognitive distortions.By leveraging multimodal information, including audio, video, and textual data, our method offers a nuanced perspective that enhances the accuracy and depth of cognitive distortion detection and reasoning in a zero-shot manner.Our proposed hierarchical framework adeptly tackles both detection and reasoning tasks, showcasing significant performance enhancements compared to current methodologies.Through comprehensive analysis, we elucidate the efficacy of our approach, offering promising insights into the diagnosis and understanding of cognitive distortions in multimodal settings.The code and dataset can be found here: https://www.iitp.ac. in/~ai-nlp-ml/resources.html#ZS-CoDR.CoD Reasoning: The patient's final words, "They are always commenting on everything that I'm doing."could be seen as an example of cognitive distortion.This distortion occurs when someone assumes others are always scrutinizing them, despite lacking evidence.The patient's belief that others are constantly monitoring and critiquing their actions is exaggerated and unsupported, demonstrating a distorted perception of external attention.D: Ok, ok.And can you hear what they are actually saying?P: Yeah, they are talking about me.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Zero-shot LLM detection of cognitive distortions in patient-doctor dialogues, evaluated on an annotated dataset whose labels are probably human.); Sonnet ? (неясно, сравнивали ли с людьми: Zero-shot LLM detection of cognitive distortions in patient-doctor dialogues with a dataset; likely human-annotated labels, but this isn't stated in the abstract. Full text needed.)

**Решение:** +

---

### 253 · R11194

**Chain-of-Interaction: Enhancing Large Language Models for Psychiatric Behavior Understanding by Dyadic Contexts**

2024 · IEEE International Conference on Healthcare Informatics (ICHI) · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/ichi61247.2024.00057

Automatic coding patient behaviors is essential to support decision making for psychotherapists during the motivational interviewing (MI), a collaborative communication intervention approach to address psychiatric issues, such as alcohol and drug addiction. While the behavior coding task has rapidly adapted machine learning to predict patient states during the MI sessions, lacking of domain-specific knowledge and overlooking patient-therapist interactions are major challenges in developing and deploying those models in real practice. To encounter those challenges, we introduce the Chain-of-Interaction (CoI) prompting method aiming to contextualize large language models (LLMs) for psychiatric decision support by the dyadic interactions. The CoI prompting approach systematically breaks down the coding task into three key reasoning steps, extract patient engagement, learn therapist question strategies, and integrates dyadic interactions between patients and therapists. This approach enables large language models to leverage the coding scheme, patient state, and domain knowledge for patient behavioral coding. Experiments on real-world datasets can prove the effectiveness and flexibility of our prompting method with multiple state-of-the-art LLMs over existing prompting baselines. We have conducted extensive ablation analysis and demonstrate the critical role of dyadic interactions in applying LLMs for psychotherapy behavior understanding. Accepted to IEEE ICHI 2024

**ИИ:** + · обе модели · кодирование сессий · LLMs prompted to code patient behaviours in MI session transcripts; real-world datasets have human-annotated MI codes as reference.

**Решение:** =

---

### 254 · R11201

**Sequence-to-Sequence Language Models for Character and Emotion Detection in Dream Narratives**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2403.15486

The study of dreams has been central to understanding human (un)consciousness, cognition, and culture for centuries. Analyzing dreams quantitatively depends on labor-intensive, manual annotation of dream narratives. We automate this process through a natural language sequence-to-sequence generation framework. This paper presents the first study on character and emotion detection in the English portion of the open DreamBank corpus of dream narratives. Our results show that language models can effectively address this complex task. To get insight into prediction performance, we evaluate the impact of model size, prediction order of characters, and the consideration of proper names and character traits. We compare our approach with a large language model using in-context learning. Our supervised models perform better while having 28 times fewer parameters. Our model and its generated annotations are made publicly available.

**ИИ:** + · обе модели · бенчмарк с метками людей · An in-context LLM and seq2seq models detect characters and emotions in DreamBank narratives, evaluated against manual human annotations.

**Решение:** =

---

### 255 · R11208

**RU at WASSA 2024 Shared Task: Task-Aligned Prompt for Predicting Empathy and Distress**

2024 · Workshop on Computational Approaches to Subjectivity, Sentiment & Social Media Analysis (WASSA) · journalarticle, conference-paper · en · https://doi.org/10.18653/v1/2024.wassa-1.31

This paper describes our approach for the WASSA 2024 Shared Task on Empathy Detection and Emotion Classification and Personality Detection in Interactions at ACL 2024. We focused on Track 3: Empathy Prediction (EMP) which aims to predict the empathy and distress of writers based on their essays. Recently, LLMs have been used to detect the psychological status of the writers based on the texts. Previous studies showed that the performance of LLMs can be improved by designing prompts properly. While diverse approaches have been made, we focus on the fact that LLMs can have different nuances for psychological constructs such as empathy or distress to the specific task. In addition, people can express their empathy or distress differently according to the context. Thus, we tried to enhance the prediction performance of LLMs by proposing a new prompting strategy: Task-Aligned Prompt (TAP). This prompt consists of aligned definitions for empathy and distress to the original paper and the contextual information about the dataset. Our proposed prompt was tested using ChatGPT and GPT4o with zero-shot and few-shot settings and the performance was compared to the plain prompts. The results showed that the TAP-ChatGPT-zero-shot achieved the highest average Pearson correlation of empathy and distress on the EMP track.

**ИИ:** разошлись — Opus -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): GPT models predict essay writers' self-reported empathy and distress in the WASSA Track 3 task; no human coders provide the reference labels.); Sonnet ? (неясно, кто ставил эталонные метки: LLMs predict empathy and distress from essays (WASSA EMP). The labels are likely the writers' self-reports rather than coder ratings, but the abstract doesn't say. Check the full text.)

**Решение:** -

---

### 256 · R11210

**Empower Typed Descriptions by Large Language Models for Speech Emotion Recognition**

2024 · Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC) · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/apsipaasc63619.2025.10848758

Training speech emotion recognition (SER) requires human-annotated labels and speech data. However, emotion perception is complex. The pre-defined emotion categories are not enough for annotators to describe their emotion perception. Devoted annotators will use natural language rather than traditional emotion labels when annotating data, resulting in typed descriptions (e.g., "Slightly Angry, calm" to notify the intensity of emotion). While these descriptions are highly valuable, SER models, designed as classification models, cannot process natural languages and thus discard them. To leverage the valuable typed descriptions, we propose a novel way to prompt ChatGPT to mimic annotators, comprehend natural language typed descriptions, and subsequently adjust the given label of the input data. By utilizing labels generated by ChatGPT, we consistently achieve an average relative gain of 3.08% across all settings using 15 speech self-surprised learning models on the SUPERB, which provides a potential way to integrate the power of LLMs to improve the performances of SER.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: ChatGPT turns annotators' typed emotion descriptions into labels; evaluation seems to be downstream SER gain, and any agreement with human labels is unclear.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Speech emotion recognition; ChatGPT adjusts labels from annotator typed descriptions to improve SER training, with no LLM–human agreement on text coding.)

**Решение:** -

---

### 257 · R11212

**ESC-Eval: Evaluating Emotion Support Conversations in Large Language Models**

2024 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2406.14952

Emotion Support Conversation (ESC) is a crucial application, which aims to reduce human stress, offer emotional guidance, and ultimately enhance human mental and physical well-being. With the advancement of Large Language Models (LLMs), many researchers have employed LLMs as the ESC models. However, the evaluation of these LLM-based ESCs remains uncertain. Inspired by the awesome development of role-playing agents, we propose an ESC Evaluation framework (ESC-Eval), which uses a role-playing agent to interact with ESC models, followed by a manual evaluation of the interactive dialogues. In detail, we first re-organize 2,801 role-playing cards from seven existing datasets to define the roles of the role-playing agent. Second, we train a specific role-playing model called ESC-Role which behaves more like a confused person than GPT-4. Third, through ESC-Role and organized role cards, we systematically conduct experiments using 14 LLMs as the ESC models, including general AI-assistant LLMs (ChatGPT) and ESC-oriented LLMs (ExTES-Llama). We conduct comprehensive human annotations on interactive multi-turn dialogues of different ESC models. The results show that ESC-oriented LLMs exhibit superior ESC abilities compared to general AI-assistant LLMs, but there is still a gap behind human performance. Moreover, to automate the scoring process for future ESC models, we developed ESC-RANK, which trained on the annotated data, achieving a scoring performance surpassing 35 points of GPT-4. Our data and code are available at https://github.com/AIFlames/Esc-Eval. EMNLP 2024

**ИИ:** + · обе модели · LLM-судья · Human annotations of emotional support dialogues; ESC-RANK and GPT-4 scoring compared against human ratings.

**Решение:** =

---

### 258 · R11214

**Performance of a Custom GPT-4 Model Enhanced with Instruction-Based Learning in Identifying Cognitive Distortion Statements: The ChatPSY Example**

2024 · SSRN Electronic Journal · journalarticle, preprint · en · https://doi.org/10.2139/ssrn.4722640

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. A custom GPT-4 identifying cognitive distortion statements probably used human-labelled statements as the reference, so it fits.

**Решение:** =

---

### 259 · R11215

**A methodological exploration of generative artificial intelligence (AI) for efficient qualitative analysis on hotel guests’ delightful experiences**

2024 · International Journal of Hospitality Management · article · en · https://doi.org/10.1016/j.ijhm.2024.103974

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. Generative AI qualitative coding of guest delight (an emotion) is borderline with consumer sentiment; human comparison is likely but unconfirmed.

**Решение:** =

---

### 260 · R11218

**The Clinical Utility of Large Language Models in Diagnosing Neurocognitive Disorders among NACC Participants**

2024 · Archives of Clinical Neuropsychology · journalarticle, article · en · https://doi.org/10.1093/arclin/acae067.014

Abstract Objective Our study aimed to investigate ChatGPT’s ability to diagnose neurocognitive disorders in older adults based on neuropsychological interviews and test results and compare its accuracy with neuropsychologist consensus diagnosis. Methods We prompted ChatGPT-4 to provide provisional diagnoses (normal changes, mild cognitive impairment, or dementia) for each case. We also asked ChatGPT to diagnose the underlying etiology. We evaluated interrater reliability (IRR) with Cohen’s kappa and a chi-square test. Receiver operating characteristic (ROC) curves and area-under-the-curve (AUC) values were computed to explore measures predicting diagnostic agreement. Results Participants were 15,048 older adults (Mage = 69.13, 56.7% female) assessed in Alzheimer’s Disease Core Centers across the United States. For cognitive diagnoses, Cohen’s kappa demonstrated fair agreement (κ = 0.42; p < 0.001). The chi-square test [χ2 (6) = 7896.51, p < 0.001] revealed a significant and strong association (Cramer’s V = 0.51, p < 0.001) between ChatGPT and clinicians’ diagnoses. For the underlying etiology, Cohen’s kappa demonstrated fair agreement on specific diagnoses (κ = 0.38; p < 0.001). The chi-square test [χ2 (24) = 5353.04, p < 0.001] revealed a significant and strong association (Cramer’s V = 0.30, p < 0.001) between ChatGPT and clinicians’ diagnoses. ROC curves demonstrate that no variables predicted diagnostic agreement at above chance. Conclusion Our findings demonstrate the potential clinical utility of integrating LLMs into neuropsychology. While significant IRR was found between ChatGPT and the neuropsychologist diagnosis, further research is needed prior to the adoption of LLMs into clinical practice, given ongoing developments of artificial intelligence in the field of medicine.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · GPT-4 diagnoses neurocognitive disorders vs neuropsychologist consensus (kappa); unclear whether the input is psychological text or structured NACC test data.

**Решение:** =

---

### 261 · R11220

**Doing Research with Help from ChatGPT: Promising Examples for Coding and Inter-Rater Reliability**

2024 · International Journal of Technology in Education · journalarticle, article, journal-article · en · https://doi.org/10.46328/ijte.537

The rapid development of artificial intelligence and large language models (LLMs) has led to significant advancements in applying machine learning techniques across diverse disciplines, including educational science research. This study investigates the potential of LLMs like ChatGPT for qualitative data analysis, focusing on open, axial, selective coding, theme or pattern identification, and inter-rater reliability. Our findings indicate promising capabilities of ChatGPT in open coding, demonstrating accurate categorization of qualitative data. However, axial coding posed challenges due to the model's limited understanding, which was partially addressed by refining prompts based on ChatGPT's interpretation. ChatGPT also showed competence in selective coding and theme or pattern identification, providing additional insights. For inter-rater reliability, ChatGPT's performance varied across datasets, with improvements observed when providing contextual information. It is important to note the limitations and variability of LLMs such as ChatGPT, which is in public beta and subject to potential limitations in usage and reliability. Our study demonstrates ChatGPT's potential for coding and inter-rater reliability. Improved results are achieved with refined prompts and utilising ChatGPT's own definitions. The adoption of LLMs for qualitative analysis requires further exploration, including addressing algorithmic bias and the potential for inaccurate responses. Validation techniques are crucial in mitigating these risks.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT coding of qualitative education data with inter-rater reliability against humans; unclear whether the coded constructs are psychological.

**Решение:** =

---

### 262 · R11226

**ChatGPT Giving Relationship Advice – How Reliable Is It?**

2024 · Proceedings of the International AAAI Conference on Web and Social Media · journalarticle, conference-paper · en · https://doi.org/10.1609/icwsm.v18i1.31338

In the evolving realm of natural language processing (NLP), generative AI models like ChatGPT are increasingly utilized across various applications. Among the possible purposes, many people are considering asking ChatGPT for relationship advice. However, the lack of in-depth examination of ChatGPT's response quality could be concerning when it is used for personal topics like mental health issues and intimate relationship problems. In these topics, a piece of misleading advice could cause harmful repercussions. In response to people's growing interest in using ChatGPT as a relationship advisor, our research evaluates ChatGPT's proficiency in discerning relationship advice. Specifically, we investigate its alignment with human judgements. We conducted our analysis with 13,138 Reddit posts about intimate relationship problems to examine the overall alignment. Furthermore, we investigate ChatGPT's consistency in judging intimate relationship advice by re-prompting identical queries. Our results indicate a significant disparity between ChatGPT and human judgments, with the model displaying inconsistency in its own decisions. Our findings emphasize the need for comprehensive insights into ChatGPT's mechanisms for intimacy problems and future improvements in its proficiency in helping people's relationship struggles.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT judges relationship advice in Reddit posts against human judgments; unclear if this is a psychological construct or just Reddit votes.

**Решение:** =

---

### 263 · R11229

**Using Machine Learning to Analyze Short-Answer Responses to Conceptually Challenging Chemical Engineering Thermodynamics Questions**

2024 · ASEE Annual Conference & Exposition · conference-paper · en · https://doi.org/10.18260/1-2--48236

Abstract This work builds off a collaboration between machine learning and engineering education researchers to build a human-computer partnership utilizing machine learning to analyze student narratives of understanding in written short-answer responses to conceptually challenging questions [1], [2]. This study investigates student thinking in written short-answer responses justifying their answer choice to conceptually challenging multiple-choice concept questions often used in peer instruction or other active learning practices [3], [4]. The study then uses Large Language Models (LLMs) to automate the analysis of these responses. Students writing short answer responses to justify their reasoning to multiple choice concept questions has been shown to improve engagement, conceptual understanding, and has an overall positive effect on students' answers [5], [6]. We conceptualize the responses that students write as "narratives of understanding," as students use a combination of everyday and disciplinary language to construct a short-answer response around their understanding. We utilized written responses available from consenting students in the Concept Warehouse (CW) [7], a web-based online tool for active learning. Two related questions from chemical engineering thermodynamics were coded by humans using emergent and inductive coding approaches [8], [9]: an enthalpy of mixing question (1396 responses) and an entropy of mixing question (1387 responses). The written responses were then analyzed using LLMs-based coding methods. We used in-context learning for GPT-4 [10], where we prompted the model with the question, four in-context examples of answers, and the corresponding codes and instructed it to generate the code(s) for the new answer instance. We evaluated the model on a test set of 140 samples for each of the thermodynamics questions. Using both manual and language model-based coding, we aim to answer two research questions: 1. What aspects of student thinking are present in narratives of understanding constructed to justify conceptual questions about the enthalpy and entropy of mixing ideal gases? 2. To what extent can we use Large Language Models to automate qualitative coding of student narratives of understanding? Through this coding process, elements of student thinking were identified to describe the narratives students created to convey their understanding, including identification, comparison, and inference. In this paper, we conceptualize and discuss these three aspects of student thinking and how they convey an understanding of these concepts. When compared against manually coded responses, GPT-4 can generate codes with an F1 score of 54%, precision of 61%, and recall of 49% for the enthalpy of mixing question. For the entropy of mixing question, the model has an F1 score of 47%, precision of 48%, and recall of 47%. This study aims to contribute to the body of work that investigates applications of natural language processing to education research and, more generally, to qualitative coding processes.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-4 coding of student reasoning in thermodynamics answers, compared with human codes; unclear if this is a psychological construct or subject knowledge.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: GPT-4 codes engineering student thermodynamics reasoning against human codes; this is subject-knowledge education research, not a psychological or clinical construct.)

**Решение:** -

---

### 264 · R11231

**When Qualitative Research Meets Large Language Model: Exploring the Potential of QualiGPT as a Tool for Qualitative Coding**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2407.14925

Qualitative research, renowned for its in-depth exploration of complex phenomena, often involves time-intensive analysis, particularly during the coding stage. Existing software for qualitative evaluation frequently lacks automatic coding capabilities, user-friendliness, and cost-effectiveness. The advent of Large Language Models (LLMs) like GPT-3 and its successors marks a transformative era for enhancing qualitative analysis. This paper introduces QualiGPT, a tool developed to address the challenges associated with using ChatGPT for qualitative analysis. Through a comparative analysis of traditional manual coding and QualiGPT\u27s performance on both simulated and real datasets, incorporating both inductive and deductive coding approaches, we demonstrate that QualiGPT significantly improves the qualitative analysis process. Our findings show that QualiGPT enhances efficiency, transparency, and accessibility in qualitative coding. The tool\u27s performance was evaluated using inter-rater reliability (IRR) measures, with results indicating substantial agreement between human coders and QualiGPT in various coding scenarios. In addition, we also discuss the implications of integrating AI into qualitative research workflows and outline future directions for enhancing human-AI collaboration in this field.arXiv admin note: substantial text overlap with arXiv:2310.0706

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT-based tool's qualitative coding compared with human coders via IRR; unclear whether the datasets involve psychological constructs.

**Решение:** =

---

### 265 · R11239

**Scoring with Large Language Models: A Study on Measuring Empathy of Responses in Dialogues**

2024 · IEEE International Conference on Big Data (BigData) · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/bigdata62323.2024.10825836

In recent years, Large Language Models (LLMs) have become increasingly more powerful in their ability to complete complex tasks. One such task in which LLMs are often employed is scoring, i.e., assigning a numerical value from a certain scale to a subject. In this paper, we strive to understand how LLMs score, specifically in the context of empathy scoring. We develop a novel and comprehensive framework for investigating how effective LLMs are at measuring and scoring empathy of responses in dialogues, and what methods can be employed to deepen our understanding of LLM scoring. Our strategy is to approximate the performance of state-of-the-art and fine-tuned LLMs with explicit and explainable features. We train classifiers using various features of dialogues including embeddings, the Motivational Interviewing Treatment Integrity (MITI) Code, a set of explicit subfactors of empathy as proposed by LLMs, and a combination of the MITI Code and the explicit subfactors. Our results show that when only using embeddings, it is possible to achieve performance close to that of generic LLMs, and when utilizing the MITI Code and explicit subfactors scored by an LLM, the trained classifiers can closely match the performance of fine-tuned LLMs. We employ feature selection methods to derive the most crucial features in the process of empathy scoring. Our work provides a new perspective toward understanding LLM empathy scoring and helps the LLM community explore the potential of LLM scoring in social science studies. Accepted by IEEE BigData 2024

**ИИ:** + · обе модели · бенчмарк с метками людей · LLMs score the empathy of dialogue responses and are evaluated for performance, probably against human-annotated empathy labels; MITI coding is also used.

**Решение:** =

---

### 266 · R11249

**Multi-Session Client-Centered Treatment Outcome Evaluation in Psychotherapy**

2024 · International Conference on Language Resources and Evaluation · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2410.05824

In psychotherapy, therapeutic outcome assessment, or treatment outcome evaluation, is essential to mental health care by systematically evaluating therapeutic processes and outcomes. Existing large language model approaches often focus on therapist-centered, single-session evaluations, neglecting the client's subjective experience and longitudinal progress across multiple sessions. To address these limitations, we propose IPAEval, a client-Informed Psychological Assessment-based Evaluation framework, which automates treatment outcome evaluations from the client's perspective using clinical interviews. It integrates cross-session client-contextual assessment and session-focused client-dynamics assessment for a comprehensive understanding of therapeutic progress. Specifically, IPAEval employs a two-stage prompt scheme that maps client information onto psychometric test items, enabling interpretable and structured psychological assessments. Experiments on our new TheraPhase dataset, comprising 400 paired initial and completion stage client records, demonstrate that IPAEval effectively tracks symptom severity and treatment outcomes over multiple sessions, outperforming baseline approaches across both closed-source and open-source models, and validating the benefits of items-aware reasoning mechanisms. Accepted at LREC 2026. Camera-ready Version

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs rate symptom severity from therapy transcripts using psychometric items; the abstract doesn't say whether the TheraPhase reference labels come from human raters.

**Решение:** =

---

### 267 · R11257

**FEEL: A Framework for Evaluating Emotional Support Capability with Large Language Models**

2024 · International Conference on Intelligent Computing · journalarticle, text/article, conference-paper · en · https://doi.org/10.1007/978-981-97-5618-6_9

Emotional Support Conversation (ESC) is a typical dialogue that can effectively assist the user in mitigating emotional pressures. However, owing to the inherent subjectivity involved in analyzing emotions, current non-artificial methodologies face challenges in effectively appraising the emotional support capability. These metrics exhibit a low correlation with human judgments. Concurrently, manual evaluation methods extremely will cause high costs. To solve these problems, we propose a novel model FEEL (Framework for Evaluating Emotional Support Capability with Large Lan-guage Models), employing Large Language Models (LLMs) as evaluators to assess emotional support capabilities. The model meticulously considers various evaluative aspects of ESC to apply a more comprehensive and accurate evaluation method for ESC. Additionally, it employs a probability distribution approach for a more stable result and integrates an ensemble learning strategy, leveraging multiple LLMs with assigned weights to enhance evaluation accuracy. To appraise the performance of FEEL, we conduct extensive experiments on existing ESC model dialogues. Experimental results demonstrate our model exhibits a substantial enhancement in alignment with human evaluations compared to the baselines. Our source code is available at https://github.com/Ansisy/FEEL. Accepted to ICIC 2024

**ИИ:** + · обе модели · LLM-судья · LLM evaluators rate emotional support capability in ESC dialogues; alignment with human evaluations reported.

**Решение:** =

---

### 268 · R11261

**Predicting the Information Need for Domestic Violence Survivors Based on the Fine-Tuned Large Language Model.**

2024 · Studies in health technology and informatics · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.3233/shti240282

Women with domestic violence experiences often refuse to seek help face-to-face due to embarrassment. They begin to share their emotions and seek help from online health communities. Understanding and responding to these posts can be crucial in providing timely support to the victims. We proposed a fine-tuned large language model (LLM) capable of accurately predicting the informational need based on the content of postings. We fine-tuned the LAMMA2-7B-chat model based on the guidance of identifying the information need and a dataset comprising 273 posts from Reddit, which are manually annotated by domain experts. Furthermore, we evaluated the performance of our model using a random sample of 15 posts, and 66.6% were accurately predicted. The results demonstrate that our model can rapidly capture the information needs expressed in the posts, enabling healthcare providers to provide timely and useful support based on our predictions.

**ИИ:** разошлись — Opus ? (неясен конструкт: Fine-tuned Llama2 classifies information needs in DV survivors' Reddit posts against expert annotations; unclear whether information need counts as a psychological construct.); Sonnet + (кодирование по кодбуку: Fine-tuned Llama2 labels information needs in Reddit domestic violence posts, evaluated against expert manual annotations (66.6% accuracy on 15 posts).)

**Решение:** ?

---

### 269 · R11276

**Can large language models be sensitive to culture suicide risk assessment?**

2024 · Journal of Cultural Cognitive Science · journalarticle, article, journal-article · en · https://doi.org/10.1007/s41809-024-00151-9

Abstract Suicide remains a pressing global public health issue. Previous studies have shown the promise of Generative Intelligent (GenAI) Large Language Models (LLMs) in assessing suicide risk in relation to professionals. But the considerations and risk factors that the models use to assess the risk remain as a black box. This study investigates if ChatGPT-3.5 and ChatGPT-4 integrate cultural factors in assessing suicide risks (probability of suicidal ideation, potential for suicide attempt, likelihood of severe suicide attempt, and risk of mortality from a suicidal act) by vignette methodology. The vignettes examined were of individuals from Greece and South Korea, representing countries with low and high suicide rates, respectively. The contribution of this research is to examine risk assessment from an international perspective, as large language models are expected to provide culturally-tailored responses. However, there is a concern regarding cultural biases and racism, making this study crucial. In the evaluation conducted via ChatGPT-4, only the risks associated with a severe suicide attempt and potential mortality from a suicidal act were rated higher for the South Korean characters than for their Greek counterparts. Furthermore, only within the ChatGPT-4 framework was male gender identified as a significant risk factor, leading to a heightened risk evaluation across all variables. ChatGPT models exhibit significant sensitivity to cultural nuances. ChatGPT-4, in particular, offers increased sensitivity and reduced bias, highlighting the importance of gender differences in suicide risk assessment. The findings suggest that, while ChatGPT-4 demonstrates an improved ability to account for cultural and gender-related factors in suicide risk assessment, there remain areas for enhancement, particularly in ensuring comprehensive and unbiased risk evaluations across diverse populations. These results underscore the potential of GenAI models to aid culturally sensitive mental health assessments, yet they also emphasize the need for ongoing refinement to mitigate inherent biases and enhance their clinical utility.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: ChatGPT rates suicide risk in vignettes across cultures; abstract reports only comparisons between conditions, but professional benchmark ratings may be included.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): ChatGPT rates suicide risk for researcher-made vignettes to test cultural/gender bias; no human coding of the same texts for agreement.)

**Решение:** -

---

### 270 · R11286

**Generative AI To Recognize Response Fabrication in PTSD**

2024 · Research Square · preprint · en · https://doi.org/10.21203/rs.3.rs-4289440/v1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM detecting fabricated PTSD responses could compare with human or clinician judgments, or only with known fabrication status.

**Решение:** =

---

### 271 · R11289

**Detecting Conversational Mental Manipulation with Intent-Aware Prompting**

2024 · arXiv (Cornell University) · journalarticle, conference, preprint/article · en · https://doi.org/10.48550/arxiv.2412.08414

Mental manipulation severely undermines mental wellness by covertly and negatively distorting decision-making. While there is an increasing interest in mental health care within the natural language processing community, progress in tackling manipulation remains limited due to the complexity of detecting subtle, covert tactics in conversations. In this paper, we propose Intent-Aware Prompting (IAP), a novel approach for detecting mental manipulations using large language models (LLMs), providing a deeper understanding of manipulative tactics by capturing the underlying intents of participants. Experimental results on the MentalManip dataset demonstrate superior effectiveness of IAP against other advanced prompting strategies. Notably, our approach substantially reduces false negatives, helping detect more instances of mental manipulation with minimal misjudgment of positive cases. The code of this paper is available. Accepted at COLING2025. Oral Presentation. Best Short Paper Award. For code and data, see https://github.com/Anton-Jiayuan-MA/Manip-IAP

**ИИ:** + · обе модели · бенчмарк с метками людей · LLMs detect mental manipulation (an interpersonal construct) in dialogues; evaluated against the human-annotated MentalManip dataset.

**Решение:** =

---

### 272 · R11297

**Evaluating Transformer Models for Suicide Risk Detection on Social Media**

2024 · IEEE International Conference on Big Data (BigData) · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/bigdata62323.2024.10826094

The detection of suicide risk in social media is a critical task with potential life-saving implications. This paper presents a study on leveraging state-of-the-art natural language processing solutions for identifying suicide risk in social media posts as a submission for the "IEEE BigData 2024 Cup: Detection of Suicide Risk on Social Media" conducted by the kubapok team. We experimented with the following configurations of transformer-based models: fine-tuned DeBERTa, GPT-4o with CoT and few-shot prompting, and fine-tuned GPT-4o. The task setup was to classify social media posts into four categories: indicator, ideation, behavior, and attempt. Our findings demonstrate that the fine-tuned GPT-4o model outperforms two other configurations, achieving high accuracy in identifying suicide risk. Notably, our model achieved second place in the competition. By demonstrating that straightforward, general-purpose models can achieve state-of-the-art results, we propose that these models, combined with minimal tuning, may have the potential to be effective solutions for automated suicide risk detection on social media.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: GPT-4o classified Reddit posts into four suicide-risk levels, scored against the competition's annotated labels, which are likely expert-coded.); Sonnet ? (неясно, кто ставил эталонные метки: GPT-4o classifies suicide-risk posts into four levels in a shared-task dataset; the abstract doesn't say the reference labels are expert annotations (likely, but unconfirmed).)

**Решение:** +

---

### 273 · R11311

**Psychological Profiling in Cybersecurity: A Look at LLMs and Psycholinguistic Features**

2024 · WISE · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.48550/arxiv.2406.18783

The increasing sophistication of cyber threats necessitates innovative approaches to cybersecurity. In this paper, we explore the potential of psychological profiling techniques, particularly focusing on the utilization of Large Language Models (LLMs) and psycholinguistic features. We investigate the intersection of psychology and cybersecurity, discussing how LLMs can be employed to analyze textual data for identifying psychological traits of threat actors. We explore the incorporation of psycholinguistic features, such as linguistic patterns and emotional cues, into cybersecurity frameworks. Our research underscores the importance of integrating psychological perspectives into cybersecurity practices to bolster defense mechanisms against evolving threats.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: Conceptual discussion of LLM psychological profiling in cybersecurity; no empirical LLM coding compared against human ratings described.); Sonnet ? (неясно, сравнивали ли с людьми: LLMs analyzing text for psychological traits of threat actors; abstract is vague, possibly a discussion paper, and doesn't mention human coder comparison.)

**Решение:** -

---

### 274 · R11314

**Deductive Coding's Role in AI vs. Human Performance**

2024 · Educational Data Mining · conferencepaper/, journalarticle · https://doi.org/10.5281/zenodo.12729957

In this study, we explore the interplay between Large Language Models (LLMs) and human coders within the realm of deductive coding in educational qualitative research, evaluating their performance side by side.The time, effort, and cost associated with training human coders contribute to inter-rater reliability (IRR) disagreements, which can delay the coding process. Additionally, challenges in consistently classifying cognitive engagement in text due to overt behavior nuances exacerbate these disagreements. We hypothesize that LLMs with the correct prompt will more accurately and precisely classify these behaviors reducing cost and time. Our methodology involves a mixed-methods approach, combining quantitative measures of coding accuracy and reliability with qualitative assessments of the coding workflow. Preliminary findings suggest that LLMs, on average, achieved a percentage improvement of approximately 13.18\% over human counterparts in terms of overall accuracy across the evaluated experiments. Notably, class-specific analysis showed that when utilizing a combination prompt, LLMs demonstrated superior performance in identifying nuanced categories, securing a 10\% and 20\% higher accuracy in Active and Constructive classes, respectively. These outcomes underscore the efficacy of LLMs, when equipped with a combination prompt, in more effectively navigating and classifying complex behaviors compared to conventional human coding methods.

**ИИ:** разошлись — Opus + (кодирование по кодбуку: LLM deductive coding of cognitive engagement (ICAP) in educational text, compared on accuracy with human coders; engagement is a cognitive-behavioural construct.); Sonnet ? (неясен конструкт: LLM deductive coding of cognitive engagement (ICAP) in educational text versus human coders; the construct is borderline psychological and the reference standard is unclear.)

**Решение:** ?

---

### 275 · R11319

**Overview of the CLPsych 2024 Shared Task: Leveraging Large Language Models to Identify Evidence of Suicidality Risk in Online Posts**

2024 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · review, conference-paper · https://doi.org/10.18653/v1/2024.clpsych-1.15

We present the overview of the CLPsych 2024 Shared Task, focusing on leveraging open source Large Language Models (LLMs) for identifying textual evidence that supports the suicidal risk level of individuals on Reddit. In particular, given a Reddit user, their pre- determined suicide risk level (‘Low’, ‘Mod- erate’ or ‘High’) and all of their posts in the r/SuicideWatch subreddit, we frame the task of identifying relevant pieces of text in their posts supporting their suicidal classification in two ways: (a) on the basis of evidence highlighting (extracting sub-phrases of the posts) and (b) on the basis of generating a summary of such evidence. We annotate a sample of 125 users and introduce evaluation metrics based on (a) BERTScore and (b) natural language inference for the two sub-tasks, respectively. Finally, we provide an overview of the system submissions and summarise the key findings.

**ИИ:** ? · обе модели · другое · Shared-task overview: LLM-extracted suicide-risk evidence scored against human annotations of 125 users; unclear whether span/summary metrics count as coding agreement.

**Решение:** =

---

### 276 · R1133

**A dataset for detecting emotional manipulation techniques in Lithuanian text.**

2026 · Data in brief · journal article, journalarticle, data-paper · eng · https://doi.org/10.1016/j.dib.2026.113000

This paper presents a dataset of Lithuanian language comments annotated with emotional manipulation techniques. The source material comprises comments from Lithuanian news portal texts. A total of 1000 comments were selected and manually annotated by four human annotators using Label Studio. The annotators identified text fragments corresponding to fourteen emotional manipulation techniques, producing span-level human annotations that form the primary component of the dataset. In addition to the manual annotations, the dataset includes machine-generated outputs created by the GPT-4.1 model. These outputs were produced by executing prompts designed for the detection and classification of emotional manipulation span. Several prompting strategies were applied, and each prompt was run five times to capture variability in model behaviour. Because GPT-4.1 does not always return verbatim text excerpts, all generated spans were post-processed to extract precise fragments from the original comments and compute their character-level offsets. The resulting dataset encompasses four components: unprocessed source comments, human-annotated spans, prompt templates, and GPT-4.1 generated predictions. The dataset provides the first publicly available Lithuanian resource annotated for emotional manipulation techniques and can support research on manipulation and persuasion phenomena in a morphologically rich, low-resource language. The human annotations may be used as a benchmark for evaluating computational models for span extraction and technique classification. The inclusion of prompts and corresponding GPT-4.1 outputs enables the study of large language model behaviour under different prompting strategies and facilitates prompt engineering research without repeating inference runs. The dataset may also be reused for training or evaluating multilingual and cross-lingual models and offers a foundational framework for the development of annotation schemes and guidelines in related corpus construction efforts.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4.1 and human span annotations of emotional manipulation techniques in news comments; unclear if this is psychological or propaganda/persuasion.

**Решение:** =

---

### 277 · R11335

**Towards a Client-Centered Assessment of LLM Therapists by Client Simulation**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2406.12266

Although there is a growing belief that LLMs can be used as therapists, exploring LLMs' capabilities and inefficacy, particularly from the client's perspective, is limited. This work focuses on a client-centered assessment of LLM therapists with the involvement of simulated clients, a standard approach in clinical medical education. However, there are two challenges when applying the approach to assess LLM therapists at scale. Ethically, asking humans to frequently mimic clients and exposing them to potentially harmful LLM outputs can be risky and unsafe. Technically, it can be difficult to consistently compare the performances of different LLM therapists interacting with the same client. To this end, we adopt LLMs to simulate clients and propose ClientCAST, a client-centered approach to assessing LLM therapists by client simulation. Specifically, the simulated client is utilized to interact with LLM therapists and complete questionnaires related to the interaction. Based on the questionnaire results, we assess LLM therapists from three client-centered aspects: session outcome, therapeutic alliance, and self-reported feelings. We conduct experiments to examine the reliability of ClientCAST and use it to evaluate LLMs therapists implemented by Claude-3, GPT-3.5, LLaMA3-70B, and Mixtral 8*7B. Codes are released at https://github.com/wangjs9/ClientCAST.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM-simulated clients rate therapeutic alliance and session outcome; the reliability check might compare these ratings with human-labelled sessions, but this is unclear.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM simulates clients who complete questionnaires to assess LLM therapists; no coding of texts compared against human labels is described.)

**Решение:** -

---

### 278 · R11346

**Fear of Artificial Intelligence? NLP, ML and LLMs Based Discovery of AI-Phobia and Fear Sentiment Propagation by AI News**

2024 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.4755964

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; LLM-based detection of fear (an emotion) in AI news text; unclear whether human-coded labels were compared.

**Решение:** =

---

### 279 · R11354

**XinHai@CLPsych 2024 Shared Task: Prompting Healthcare-oriented LLMs for Evidence Highlighting in Posts with Suicide Risk**

2024 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, conference-paper · https://doi.org/10.18653/v1/2024.clpsych-1.23

In this article, we introduce a new method for analyzing and summarizing posts from r/SuicideWatch on Reddit, overcoming the limitations of current techniques in processing complex mental health discussions online. Existing methods often struggle to accurately identify and contextualize subtle expressions of mental health problems, leading to inadequate support and intervention strategies. Our approach combines the open-source Large Language Model (LLM), fine-tuned with health-oriented knowledge, to effectively process Reddit posts. We also design prompts that focus on suicide-related statements, extracting key statements, and generating concise summaries that capture the core aspects of the discussions. The preliminary results indicate that our method improves the understanding of online suicide-related posts compared to existing methodologies.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: CLPsych 2024 shared task: LLM extracts suicide-risk evidence from Reddit posts, likely evaluated against expert-highlighted spans.); Sonnet ? (неясно, сравнивали ли с людьми: CLPsych 2024 LLM evidence highlighting in suicide-risk posts; likely evaluated against expert-annotated spans, but the abstract doesn't state human agreement, so full text is needed.)

**Решение:** +

---

### 280 · R11355

**Large Model Fine-tuning for Suicide Risk Detection Using Iterative Dual-LLM Few-Shot Learning with Adaptive Prompt Refinement for Dataset Expansion**

2024 · IEEE International Conference on Big Data (BigData) · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/bigdata62323.2024.10825974

An approach to detecting suicide risk in social media posts is presented, addressing the challenges of limited and imbalanced datasets. The proposed workflow combines large language models (LLMs), few-shot learning, and expert-supervised prompt optimization. To address class imbalance, a novel Iterative Dual-LLM Few-Shot Learning with Adaptive Prompt Refinement (IDFL-APR) method for dataset expansion is introduced. This method employs two LLMs: one for classifying posts using few-shot learning, and another for dynamically optimizing prompts, with expert oversight to prevent overfitting. The optimized LLM then identifies high-confidence samples from unclassified data, focusing on underrepresented categories. Back-translation techniques are further applied to enhance textual diversity and achieve dataset balance across all categories. Subsequently, the bloomz-3b model is fine-tuned using optimized hyperparameters, implementing an active learning strategy to iteratively augment the training set. The proposed approach significantly enhances suicide risk detection accuracy. The best-performing model achieved a weighted F1-score of 0.7154 on the test set provided by the Suicide Ideation Detection on Social Media Challenge, a track of the IEEE Big Data 2024 BigData Cup. These results demonstrate a robust solution to the inherent challenges in suicide detection tasks.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs (few-shot, fine-tuned bloomz-3b) classify suicide risk in social-media posts against challenge test labels, probably human-annotated but not stated.

**Решение:** =

---

### 281 · R1136

**Evaluating AI-Generated Virtual Patients for Communication Training in Medical Education: A Simulation Study (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.91153

BACKGROUND Simulation-based medical training often relies on scripted or pre-recorded dialogue, limiting opportunities to practice adaptive patient communication. Large language models (LLMs) can generate flexible patient dialogue, but it remains unclear whether personality-conditioned outputs produce perceptible personality cues, support clinically realistic communication, or influence judgments about whether dialogue appears AI-generated in educational contexts. OBJECTIVE This study examined whether AI-generated virtual patient dialogue conditioned on Big Five personality profiles produces perceptible and design-relevant differences in simulated medical communication, assessing personality inference, the relationship between perceived personality alignment and clinical realism, the communicative cues underlying these judgments, and whether LLMs can approximate human evaluations in a dental consultation scenario. METHODS We developed PRISM, a prototype platform featuring an LLM-powered virtual patient with configurable Big Five personality profiles. In an exploratory study, adult participants reviewed five pre-generated dental consultation transcripts in which the dentist’s dialogue was standardized using an existing educational script, while patient communication style varied by assigned personality profile. Participants evaluated personality alignment, perceived clinical realism, and whether each transcript appeared AI- or human-authored. Open-ended explanations were analyzed qualitatively, and an exploratory LLM-as-rater analysis compared automated and human judgments. RESULTS Participants provided 75 transcript-level judgments across five simulated dental consultations. Accuracy in inferring intended Big Five personality traits was low (mean 27.7%, SD 8.1%), corresponding to a mean of 6.9 (SD 2.0) correct items out of 25, with ratings clustering toward moderate trait levels. Mixed-effects models showed that inferred personality ratings did not reliably track assigned trait values. Higher inference accuracy was associated with greater perceived alignment with the assigned profile (β=1.37, SE 0.42, z=3.30, P<.001; OR 3.94, 95% CI 1.75–8.88), but not with perceived clinical realism (β=−0.38, SE 0.42, z=−0.89, P=.37; OR 0.69, 95% CI 0.30–1.57). Dialogues were classified as AI-generated in 41% of judgments, and higher realism ratings were associated with lower odds of AI attribution (β=−0.87, SE 0.33, z=−2.64, P=.008; OR 0.42, 95% CI 0.21–0.78). In exploratory analyses, LLM raters achieved 44% and 48% accuracy in personality inference but classified all transcripts as human-authored. CONCLUSIONS Participants relied primarily on language style, content specificity, and behavioral coherence when evaluating personality alignment, clinical plausibility, and dialogue authorship, while emotional cues played a limited role. Personality-conditioned dialogue influenced overall conversational impressions but did not support reliable recognition of individual Big Five traits, indicating constraints in trait-level personality control for communication-focused simulations. Although LLMs generated coherent and contextually appropriate patient dialogue, automated evaluations overestimated realism and misattributed authorship. Effective educational deployment of AI-generated virtual patients therefore requires human-centered validation, clear instructional framing, and design strategies that prioritize interactional coherence and contextual realism over latent personality parameterization.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM raters inferred Big Five traits from transcripts alongside lay human raters; unclear if LLM–human agreement or only accuracy against assigned profiles.

**Решение:** =

---

### 282 · R11360

**Exploring Instructive Prompts for Large Language Models in the Extraction of Evidence for Supporting Assigned Suicidal Risk Levels**

2024 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, conference-paper · https://doi.org/10.18653/v1/2024.clpsych-1.17

Monitoring and predicting the expression of suicidal risk in individuals’ social media posts is a central focus in clinical NLP. Yet, existing approaches frequently lack a crucial explainability component necessary for extracting evidence related to an individual’s mental health state. We describe the CSIRO Data61 team’s evidence extraction system submitted to the CLPsych 2024 shared task. The task aims to investigate the zero-shot capabilities of open-source LLM in extracting evidence regarding an individual’s assigned suicide risk level from social media discourse. The results are assessed against ground truth evidence annotated by psychological experts, with an achieved recall-oriented BERTScore of 0.919. Our findings suggest that LLMs showcase strong feasibility in the extraction of information supporting the evaluation of suicidal risk in social media discourse. Opportunities for refinement exist, notably in crafting concise and effective instructions to guide the extraction process.

**ИИ:** ? · обе модели · другое · An open-source LLM pulled suicide-risk evidence spans from posts and was scored against expert annotations by BERTScore; unclear if this counts as coder agreement.

**Решение:** =

---

### 283 · R11363

**Prompts Matter: Comparing ML/GAI Approaches for Generating Inductive Qualitative Coding Results**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2411.06316

Inductive qualitative methods have been a mainstay of education research for decades, yet it takes much time and effort to conduct rigorously. Recent advances in artificial intelligence, particularly with generative AI (GAI), have led to initial success in generating inductive coding results. Like human coders, GAI tools rely on instructions to work, and how to instruct it may matter. To understand how ML/GAI approaches could contribute to qualitative coding processes, this study applied two known and two theory-informed novel approaches to an online community dataset and evaluated the resulting coding results. Our findings show significant discrepancies between ML/GAI approaches and demonstrate the advantage of our approaches, which introduce human coding processes into GAI prompts. Accepted by AERA 2025 Annual Meeting

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Compares ML/GAI approaches that generate inductive codes for an education online-community dataset; no unit-level agreement with human coding or psychological construct.); Sonnet ? (неясно, сравнивали ли с людьми: GAI inductive coding of online community posts in education; unclear whether it compares with human codes on the same units or only at theme level, and whether the construct is psychological.)

**Решение:** -

---

### 284 · R11373

**From traces to measures: Large language models as a tool for psychological measurement from text**

2024 · arXiv.org · journalarticle · https://doi.org/10.48550/arxiv.2405.07447

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title fits LLM psychological measurement from text but may be a conceptual paper. Needs the full text to check for human comparison.

**Решение:** =

---

### 285 · R11374

**ExpressivityBench: Can LLMs Communicate Implicitly?**

2024 · Conference of the European Chapter of the Association for Computational Linguistics · journalarticle, conference, preprint/article · https://doi.org/10.18653/v1/2026.findings-eacl.235

Human communication is often implicit, conveying tone, identity, and intent beyond literal meanings. While large language models have achieved strong performance on explicit tasks such as summarization and reasoning, their capacity for expressivity, or implicit communication, remains underexplored. We introduce \textbf{ExpressivityBench}, a framework for evaluating the expressivity of LLMs using information-theoretic communication models. Our approach quantifies how well LLM-generated text communicates target properties without explicit mention, across nine tasks spanning emotion, identity, and tone. To enable scalable and reproducible evaluation, we employ LLM-based graders validated against human judgments. Our results reveal that while models are adept at expressing affective content, they struggle with sociolinguistic signals, lagging behind human baselines. This study provides a necessary step to evaluate human-like implicit communication, with implications for applications such as education, mental health support, and socially-aware dialogue systems. We provide code and data for our benchmark alongside our paper. 21 pages, 7 figures

**ИИ:** ? · обе модели · неясен конструкт · LLM graders validated against human judgments on emotion/identity/tone in text; unclear whether the emotion-related agreement is reported separately.

**Решение:** =

---

### 286 · R11387

**Overview of IEEE BigData 2024 Cup Challenges: Suicide Ideation Detection on Social Media**

2024 · IEEE International Conference on Big Data (BigData) · journalarticle, conference, review · en · https://doi.org/10.1109/bigdata62323.2024.10825048

This overview presents one of the cup challenges of IEEE BigData 2024, with the topic of suicide risk level detection on social media posts. Given a training set of N = 2000 posts (N = 500 labelled and N = 1500 unlabelled posts) from r/SuicideWatch subreddits, the task of this challenge is to develop a predictive model capable of classifying the suicidal posts into four levels (i.e., indicator, ideation, behaviour, and attempt). The dataset provided simulated the obstacles existed in relevant fields (e.g., model overfitting, data scarcity and class imbalance), participating teams are supposed to tackle these issues while exploring the effectiveness of various model architectures. We received submissions from 21 teams and works of 13 teams underwent final evaluation. Teams addressed key challenges in suicide risk detection including limited suicidal data and suicidal risk imbalance. They employed novel approaches to overcome these obstacles, leveraging a diverse range of models from foundational base language models (BLMs) to state-of-the-art large language models (LLMs). In the competition, the highest weighted F1-score achieved under the final evaluation was 0.7605. The findings of this challenge can provide technical implications to social media suicide detection and contribute the clinical effectiveness to the applications of machine learning in digital suicide or mental healthcare management.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Shared-task overview where some teams used LLMs to classify suicide risk levels in Reddit posts; unclear whether labels are human-annotated or LLM results are separable.

**Решение:** =

---

### 287 · R11404

**Language Model Council: Democratically Benchmarking Foundation Models on Highly Subjective Tasks**

2024 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, preprint/article · en · https://doi.org/10.48550/arxiv.2406.08598

As Large Language Models (LLMs) continue to evolve, evaluating them remains a persistent challenge. Many recent evaluations use LLMs as judges to score outputs from other LLMs, often relying on a single large model like GPT-4o. However, using a single LLM judge is prone to intra-model bias, and many tasks - such as those related to emotional intelligence, creative writing, and persuasiveness - may be too subjective for a single model to judge fairly. We introduce the Language Model Council (LMC), where a group of LLMs collaborate to create tests, respond to them, and evaluate each other's responses to produce a ranking in a democratic fashion. Unlike previous approaches that focus on reducing cost or bias by using a panel of smaller models, our work examines the benefits and nuances of a fully inclusive LLM evaluation system. In a detailed case study on emotional intelligence, we deploy a council of 20 recent LLMs to rank each other on open-ended responses to interpersonal conflicts. Our results show that the LMC produces rankings that are more separable and more robust, and through a user study, we show that they are more consistent with human evaluations than any individual LLM judge. Using all LLMs for judging can be costly, however, so we use Monte Carlo simulations and hand-curated sub-councils to study hypothetical council compositions and discuss the value of the incremental LLM judge.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM judges rate emotional-intelligence responses to interpersonal conflicts against a human user study; agreement may be at model-ranking level only.

**Решение:** =

---

### 288 · R11410

**Large Language Models on Fine-grained Emotion Detection Dataset with Data Augmentation and Transfer Learning**

2024 · arXiv (Cornell University) · journalarticle, review, preprint/article · en · https://doi.org/10.48550/arxiv.2403.06108

This paper delves into enhancing the classification performance on the GoEmotions dataset, a large, manually annotated dataset for emotion detection in text. The primary goal of this paper is to address the challenges of detecting subtle emotions in text, a complex issue in Natural Language Processing (NLP) with significant practical applications. The findings offer valuable insights into addressing the challenges of emotion detection in text and suggest directions for future research, including the potential for a survey paper that synthesizes methods and performances across various datasets in this domain.

**ИИ:** ? · обе модели · другое · Emotion classification against human GoEmotions labels; unclear whether generative LLMs or only encoder models like BERT/RoBERTa were used.

**Решение:** =

---

### 289 · R1142

**Emotion Analysis in Kerala’s Political Discourse: Curating and Evaluating a Multilabel Code-Mixed Malayalam-English Social Media Dataset Using LLMs**

2026 · Procedia Computer Science · conference-paper · en · https://doi.org/10.1016/j.procs.2026.06.183

In Kerala, social media has become the primary arena for political debate, with much of this discourse expressed in Malayalam-English code-mixing, commonly known as Manglish. While this hybrid language reflects the region’s cultural and linguistic realities, it creates serious hurdles for Natural Language Processing (NLP) tasks like emotion detection, where most existing tools are built for monolingual or well-resourced languages. To overcome this limitation, we present a new code-mixed Malayalam-English dataset specifically curated from YouTube comments centred on Kerala’s political discussions. The dataset is manually annotated for five key political emotions—Anger, Joy/Support, Sadness/Opposition, Fear, and Sarcasm—by native bilingual speakers, and annotation consistency is verified through Krippendorff’s Alpha. We evaluate this resource through multiple baselines, including conventional machine learning(ML) algorithms, deep learning(DL) models, and transformer architectures, and extend the analysis to advanced language models like LLMs using zero-shot as well as few-shot approaches. The results reveal both the difficulties and the potential of existing models when applied to code-mixed political text. Our work represents one of the earliest systematic efforts to build and benchmark an emotion-labelled dataset for Manglish in a political context. Beyond serving as a valuable testbed for multilingual and low-resource NLP research, this dataset has practical relevance in analysing public sentiment, shaping data-driven political communication strategies, and informing policy decisions.

**ИИ:** + · обе модели · бенчмарк с метками людей · Native speakers annotated emotions in YouTube comments; LLMs tested zero- and few-shot against these labels. Political context, but the construct is emotion.

**Решение:** =

---

### 290 · R11423

**Man Versus Machine: Harnessing Artificial Intelligence for Qualitative Analysis (Preprint)**

2024 · preprint · en · https://doi.org/10.2196/preprints.56500

BACKGROUND Large language models like GPT-4 have opened new avenues in healthcare and qualitative research. Traditional qualitative methods are time-consuming and require expertise to capture nuance. Although large language models have demonstrated enhanced contextual understanding and inferencing compared to traditional natural language processing, their performance in qualitative analysis versus that of humans remains unexplored. OBJECTIVE We evaluated the effectiveness of GPT-4 versus human researchers in qualitative analysis of interviews from patients with adult-acquired buried penis (AABP). METHODS Qualitative data were obtained from semi-structured interviews with 20 AABP patients. Human analysis involved a structured thematic process in three stages: initial observations, line-by-line coding, and consensus discussions to refine themes. In contrast, artificial intelligence (AI) analysis with GPT-4 underwent two phases: a naïve phase where GPT-4 outputs were independently evaluated by a blinded reviewer to identify themes/subthemes, and a comparison phase where AI-generated themes were compared with human-identified themes to assess agreement. RESULTS The study population (n=20) comprised predominantly white (85%), married (60%), heterosexual (95%) men, with a mean age of 58.8 years and BMI of 41.1 kg/m2. Human thematic analysis identified "urinary issues" in 95% and GPT-4 in 75% of interviews, with the subtheme "spray/stream" noted in 60% and 35%, respectively. "Sexual issues" were prominent (95% humans vs. 80% GPT-4), though humans identified a wider range of subthemes, including "pain with sex or masturbation" (35%) and "difficulty with sex or masturbation" (20%). Both analyses similarly highlighted "mental health issues" (55% humans vs. 44% GPT-4), although humans coded "depression" more frequently (50% humans vs. 20% GPT-4). Humans frequently cited "issues using public restrooms" (60%) as impacting social life, whereas GPT-4 emphasized "struggles with romantic relationships" (45%). "Hygiene issues" were consistently recognized (70% humans vs. 65% GPT-4). Humans uniquely identified "contributing factors" as a theme in all interviews. There was moderate agreement between human and GPT-4 coding (Cohen's Kappa = 0.401). Reliability assessments of GPT-4’s analyses showed consistent coding for themes like "Body image struggles" and "Chronic pain" (100%), and "Depression" (90%). Other themes like "Motivation for surgery" and "Weight challenges" were reliably coded (80%), while less frequent themes were variably identified across multiple iterations. CONCLUSIONS Large language models like GPT-4 can effectively identify key themes in analyzing qualitative healthcare data, showing moderate agreement with human analysis. While human analysis provided a richer diversity of subthemes, the consistency of AI suggests its utility as a complementary tool in qualitative research. With AI rapidly advancing, future studies should iterate analyses and circumvent token limitations by segmenting data, furthering the breadth and depth of large language model-driven qualitative analyses.

**ИИ:** разошлись — Opus + (кодирование по кодбуку: GPT-4 coded patient interviews for themes, including mental health, depression and body image, per interview; agreement with human coding reported as Cohen's kappa = 0.401.); Sonnet ? (неясен конструкт: GPT-4 coded patient interviews with human-agreement kappa reported, but the content is a urological condition's patient experience, so the psychological construct is borderline.)

**Решение:** +

---

### 291 · R11432

**Leveraging LLMs for Translating and Classifying Mental Health Data**

2024 · Workshop on Multilingual Representation Learning (MRL) · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.18653/v1/2024.mrl-1.20

Large language models (LLMs) are increasingly used in medical fields. In mental health support, the early identification of linguistic markers associated with mental health conditions can provide valuable support to mental health professionals, and reduce long waiting times for patients. Despite the benefits of LLMs for mental health support, there is limited research on their application in mental health systems for languages other than English. Our study addresses this gap by focusing on the detection of depression severity in Greek through user-generated posts which are automatically translated from English. Our results show that GPT3.5-turbo is not very successful in identifying the severity of depression in English, and it has a varying performance in Greek as well. Our study underscores the necessity for further research, especially in languages with less resources. Also, careful implementation is necessary to ensure that LLMs are used effectively in mental health platforms, and human supervision remains crucial to avoid misdiagnosis.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · GPT-3.5 rates depression severity in user posts (English and Greek translation); the source of the reference labels isn't stated but is likely human annotation.

**Решение:** =

---

### 292 · R11442

**Depression Diagnosis Dialogue Simulation: Self-improving Psychiatrist with Tertiary Memory**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2409.15084

Mental health issues, particularly depressive disorders, present significant challenges in contemporary society, necessitating the development of effective automated diagnostic methods. This paper introduces the Agent Mental Clinic (AMC), a self-improving conversational agent system designed to enhance depression diagnosis through simulated dialogues between patient and psychiatrist agents. To enhance the dialogue quality and diagnosis accuracy, we design a psychiatrist agent consisting of a tertiary memory structure, a dialogue control and reflect plugin that acts as ``supervisor'' and a memory sampling module, fully leveraging the skills reflected by the psychiatrist agent, achieving great accuracy on depression risk and suicide risk diagnosis via conversation. Experiment results on datasets collected in real-life scenarios demonstrate that the system, simulating the procedure of training psychiatrists, can be a promising optimization method for aligning LLMs with real-life distribution in specific domains without modifying the weights of LLMs, even when only a few representative labeled cases are available.

**ИИ:** разошлись — Opus ? (неясно, кто ставил эталонные метки: LLM agent diagnoses depression and suicide risk from simulated dialogues; unclear whether the real-life labels come from clinician coding or from diagnosis.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM agents simulate psychiatrist-patient dialogues to predict depression/suicide risk; diagnosis prediction, not LLM coding of text against human coder labels.)

**Решение:** -

---

### 293 · R11445

**Harmful Suicide Content Detection**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2407.13942

Harmful suicide content on the Internet is a significant risk factor inducing suicidal thoughts and behaviors among vulnerable populations. Despite global efforts, existing resources are insufficient, specifically in high-risk regions like the Republic of Korea. Current research mainly focuses on understanding negative effects of such content or suicide risk in individuals, rather than on automatically detecting the harmfulness of content. To fill this gap, we introduce a harmful suicide content detection task for classifying online suicide content into five harmfulness levels. We develop a multi-modal benchmark and a task description document in collaboration with medical professionals, and leverage large language models (LLMs) to explore efficient methods for moderating such content. Our contributions include proposing a novel detection task, a multi-modal Korean benchmark with expert annotations, and suggesting strategies using LLMs to detect illegal and harmful content. Owing to the potential harm involved, we publicize our implementations and benchmark, incorporating an ethical verification process. 30 pages, 7 figures

**ИИ:** + · обе модели · бенчмарк с метками людей · Korean benchmark of online suicide content with expert harmfulness annotations; LLMs evaluated on classifying it into five harmfulness levels.

**Решение:** =

---

### 294 · R11446

**Detecting Suicide Risk Patterns using Hierarchical Attention Networks with Large Language Models**

2024 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, conference-paper, proceedings-article · https://doi.org/10.18653/v1/2024.clpsych-1.21

Suicide has become a major public health and social concern in the world . This Paper looks into a method through use of LLMs (Large Lan- guage Model) to extract the likely reason for a person to attempt suicide , through analysis of their social media text posts detailing about the event , using this data we can extract the rea- son for the cause such mental state which can provide support for suicide prevention. This submission presents our approach for CLPsych Shared Task 2024. Our model uses Hierarchi- cal Attention Networks (HAN) and Llama2 for finding supporting evidence about an individ- ual’s suicide risk level.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: CLPsych 2024 shared task: Llama2-based extraction of suicide-risk evidence from posts, evaluated against expert-annotated evidence highlights.); Sonnet ? (другое: CLPsych 2024 shared task: Llama2 with HAN extracts suicide-risk evidence from posts, likely scored against human-annotated evidence. Unclear whether this counts as coding agreement.)

**Решение:** +

---

### 295 · R11454

**Finetuning Large Language Models for Suicide Risk Level Assessment on Social Media**

2024 · IEEE International Conference on Big Data (BigData) · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/bigdata62323.2024.10825211

Suicide remains a pressing global issue, and early detection of individuals at risk is vital for prevention. Traditional methods of suicide risk assessment rely heavily on questionnaires and interviews. However, social media offers a rich source of realtime data, providing an opportunity for automated suicide risk detection. In this study, we propose a novel method leveraging large language models (LLMs) to assess suicide risk based on social media activity. Our approach integrates RoBERTa, Llama 3.1, and Gemma 2 through a voting mechanism to enhance predictive performance. Results indicate that our model achieves an F1 score of 0.7006, outperforming traditional machine learning and deep learning models. We also observe that while fine-tuning large models on limited data yields better results than pre-trained models, increasing model size does not always improve performance. The use of a voting mechanism significantly improves the accuracy of the predictions, demonstrating the utility of multi-model approaches in suicide risk detection.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Fine-tuned Llama 3.1 and Gemma 2 rate suicide risk levels in social-media posts; the abstract doesn't say whether reference labels are human annotations.

**Решение:** =

---

### 296 · R11455

**Properties of Person Descriptors in the Natural German Language: A Preregistered Replication and Extension**

2024 · PsyArXiv · journalarticle, preprint, ppr · en · https://doi.org/10.31234/osf.io/s8h7u

Understanding language is crucial to psychological research, as it is the basis for almost all psychological measurements. Building on previous work, we conducted a preregistered replication study, analyzing 874 person-descriptive terms generated by 187 participants using a free response format. These terms were rated on social desirability, observability, importance, abstractness, base rate, and stability by approximately human 15 raters each (n = 456). Key findings were replicated, including a bimodal distribution of social desirability, a greater number of negative vs. positive terms, and an U-shaped relationship between importance and social desirability. Furthermore, we show that human ratings of social desirability can be closely approximated by synthetic ratings derived from either a fine-tuned encoder model or the general-purpose transformer model GPT-4o. However, when investigating GPT-4o's performance in approximating human ratings of the other properties, it was mediocre at best, and its performance in approximating abstractness was poor. This suggests that there is still need for improvement in AI-applications for natural language processing.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o ratings of participant-generated person descriptors compared with human ratings; unclear whether word properties count as a psychological construct.

**Решение:** =

---

### 297 · R11462

**Can Large Language Models be sensitive to Culture Suicide Risk Assessment?**

2024 · Research Square · preprint, ppr, posted-content · https://doi.org/10.21203/rs.3.rs-4066705/v1

Abstract Suicide remains a pressing global public health issue. Previous studies have shown the promise of Generative Intelligent (GenAI) Large Language Models (LLMs) in assessing suicide risk in relation to professionals. But the considerations and risk factors that the models use to assess the risk remain as a black box. This study investigates if ChatGPT-3.5 and ChatGPT-4 integrate cultural factors in assessing suicide risks (probability of suicidal ideation, potential for suicide attempt, likelihood of severe suicide attempt, and risk of mortality from a suicidal act) by vignette methodology. The vignettes examined were of individuals from Greece and South Korea, representing countries with low and high suicide rates, respectively. The contribution of this research is to examine risk assessment from an international perspective, as large language models are expected to provide culturally-tailored responses. However, there is a concern regarding cultural biases and racism, making this study crucial. In the evaluation conducted via ChatGPT-4, only the risks associated with a severe suicide attempt and potential mortality from a suicidal act were rated higher for the South Korean characters than for their Greek counterparts. Furthermore, only within the ChatGPT-4 framework was male gender identified as a significant risk factor, leading to a heightened risk evaluation across all variables. ChatGPT models exhibit significant sensitivity to cultural nuances. ChatGPT-4, in particular, offers increased sensitivity and reduced bias, highlighting the importance of gender differences in suicide risk assessment.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: ChatGPT rates suicide risk in vignettes across cultures and genders; the abstract mentions no comparison with professional ratings, though related studies include one.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): ChatGPT rates suicide risk for vignettes varying by culture and gender; this tests bias, with no human coding of the same texts to compare against.)

**Решение:** -

---

### 298 · R11464

**Comparing GPT-4 and Human Researchers in Health Care Data Analysis: Qualitative Description Study.**

2024 · Journal of medical Internet research · comparative study, research-article, journal article · eng · https://doi.org/10.2196/56500

Background Large language models including GPT-4 (OpenAI) have opened new avenues in health care and qualitative research. Traditional qualitative methods are time-consuming and require expertise to capture nuance. Although large language models have demonstrated enhanced contextual understanding and inferencing compared with traditional natural language processing, their performance in qualitative analysis versus that of humans remains unexplored. Objective We evaluated the effectiveness of GPT-4 versus human researchers in qualitative analysis of interviews with patients with adult-acquired buried penis (AABP). Methods Qualitative data were obtained from semistructured interviews with 20 patients with AABP. Human analysis involved a structured 3-stage process-initial observations, line-by-line coding, and consensus discussions to refine themes. In contrast, artificial intelligence (AI) analysis with GPT-4 underwent two phases: (1) a naïve phase, where GPT-4 outputs were independently evaluated by a blinded reviewer to identify themes and subthemes and (2) a comparison phase, where AI-generated themes were compared with human-identified themes to assess agreement. We used a general qualitative description approach. Results The study population (N=20) comprised predominantly White (17/20, 85%), married (12/20, 60%), heterosexual (19/20, 95%) men, with a mean age of 58.8 years and BMI of 41.1 kg/m 2 . Human qualitative analysis identified "urinary issues" in 95% (19/20) and GPT-4 in 75% (15/20) of interviews, with the subtheme "spray or stream" noted in 60% (12/20) and 35% (7/20), respectively. "Sexual issues" were prominent (19/20, 95% humans vs 16/20, 80% GPT-4), although humans identified a wider range of subthemes, including "pain with sex or masturbation" (7/20, 35%) and "difficulty with sex or masturbation" (4/20, 20%). Both analyses similarly highlighted "mental health issues" (11/20, 55%, both), although humans coded "depression" more frequently (10/20, 50% humans vs 4/20, 20% GPT-4). Humans frequently cited "issues using public restrooms" (12/20, 60%) as impacting social life, whereas GPT-4 emphasized "struggles with romantic relationships" (9/20, 45%). "Hygiene issues" were consistently recognized (14/20, 70% humans vs 13/20, 65% GPT-4). Humans uniquely identified "contributing factors" as a theme in all interviews. There was moderate agreement between human and GPT-4 coding (κ=0.401). Reliability assessments of GPT-4's analyses showed consistent coding for themes including "body image struggles," "chronic pain" (10/10, 100%), and "depression" (9/10, 90%). Other themes like "motivation for surgery" and "weight challenges" were reliably coded (8/10, 80%), while less frequent themes were variably identified across multiple iterations. Conclusions Large language models including GPT-4 can effectively identify key themes in analyzing qualitative health care data, showing moderate agreement with human analysis. While human analysis provided a richer diversity of subthemes, the consistency of AI suggests its use as a complementary tool in qualitative research. With AI rapidly advancing, future studies should iterate analyses and circumvent token limitations by segmenting data, furthering the breadth and depth of large language model-driven qualitative analyses.

**ИИ:** разошлись — Opus + (кодирование по кодбуку: GPT-4 and humans coded themes, including mental health, depression and body image, in each of 20 patient interviews; agreement κ=0.401.); Sonnet ? (неясен конструкт: GPT-4 coded patient interviews against human coding (κ=0.401), but the themes are mostly medical and theme-level, so the psychological construct is unclear.)

**Решение:** +

---

### 299 · R11478

**A framework to support educational gerontology based on agile culture**

2024 · Education and Information Technologies · journalarticle, article · en · https://doi.org/10.1007/s10639-024-13260-3

Older adults have unique learning needs that require distinct approaches, particularly in non-formal education settings, which are flexible, systematic, and less bureaucratic. Seeking methods to support these needs, this study explores agile culture—a people-centered, adaptable approach originally from software development that emphasizes collaboration, communication, and gradual planning without rigid rules. The objective is to present Agil-Idade, a non-formal education framework based on agile culture, aimed at supporting older adult education in a way that promotes lifelong learning and meaningful engagement. Agil-Idade was developed through bibliographic research, co-design, and literature mapping, then evaluated in a 14-week exploratory study with six participants aged 60 to 83. Data collection included questionnaires and semi-structured interviews, analyzed using a mixed approach that combined content analysis with descriptive statistics. The study employed both manual coding and qualitative analysis tools (ChatGPT and ATLAS.ti) to establish comprehensive categories, with a Likert scale used for self-assessment in areas such as collaboration, satisfaction, experience sharing, engagement, and communication. Results indicate that Agil-Idade effectively enhanced collaboration and communication, fostering greater satisfaction, engagement, and personal appreciation among participants. These findings suggest that agile culture holds potential for advancing educational practices with older adults, contributing to the literature on non-formal education and supporting personal and social development within this demographic.

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: ChatGPT helped build categories for an education framework evaluation; no LLM–human coding agreement on the same units is reported.); Sonnet ? (неясно, сравнивали ли с людьми: Interviews coded manually and with ChatGPT/ATLAS.ti; unclear whether LLM–human agreement is reported and whether constructs (satisfaction, engagement) count as psychological.)

**Решение:** -

---

### 300 · R11485

**Evaluating large language models in analysing classroom dialogue.**

2024 · NPJ science of learning · journal article, journalarticle, text/article · eng · https://doi.org/10.1038/s41539-024-00273-3

This study explores the application of Large Language Models (LLMs), specifically GPT-4, in the analysis of classroom dialogue, a crucial research task for both teaching diagnosis and quality improvement. Recognizing the knowledge-intensive and labor-intensive nature of traditional qualitative methods in educational research, this study investigates the potential of LLM to streamline and enhance the analysis process. The study involves datasets from a middle school, encompassing classroom dialogues across mathematics and Chinese classes. These dialogues were manually coded by educational experts and then analyzed using a customised GPT-4 model. This study focuses on comparing manual annotations with the outputs of GPT-4 to evaluate its efficacy in analyzing educational dialogues. Time efficiency, inter-coder agreement, and inter-coder reliability between human coders and GPT-4 are evaluated. Results indicate substantial time savings with GPT-4, and a high degree of consistency in coding between the model and human coders, with some discrepancies in specific codes. These findings highlight the strong potential of LLM in teaching evaluation and facilitation.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4 vs expert coding of classroom dialogue with reliability reported; unclear whether the dialogue codes are psychological/interpersonal or purely pedagogical.

**Решение:** =
