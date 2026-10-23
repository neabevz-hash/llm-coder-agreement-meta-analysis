# Калибровка вслепую, часть 3

Калибровка вслепую, часть 3: записи 301–400 из 400. Это случайные 400 записей из 6852 в списке к отбору финального поиска 2026-10-21 (зерно 20261022, порядок случайный). **Меток ИИ здесь нет.** Размечайте в любом порядке и в несколько заходов. Когда закончите все части, скажите: я проверю, что всё размечено, и закоммичу файлы до того, как открою метки ИИ.

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

### 301 · R6120

**Automated Behavioural Coding of Therapist–Client Communications in Therapist-Assisted Internet-Delivered Cognitive Behaviour Therapy: A Comparative Evaluation of Large Language Models and Harness Engineering Strategies**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.7167137

Monitoring therapist fidelity in therapist-assisted internet-delivered cognitive behaviour therapy (iCBT) requires manual behavioural coding of email correspondence, a process that cannot scale to large-scale routine clinical delivery or fidelity research. The ICBT Therapist Rating Scale (ICBT-TRS) and associated client behaviour and question codebooks provide validated instruments for this purpose, yet no prior work has applied automated classification to multi-label behavioural coding of therapist–client emails using them. This study evaluates large language models (LLMs) for automated multi-label behavioural coding of iCBT correspondence from a single therapist–client dyad (21 emails), encompassing 23 behavioural labels across three codebook groups: therapist behaviours, client behaviours, and client question categories. Nine open-source models spanning 9B to 123B parameters were evaluated across seven prompt harness conditions varying in task decomposition, example type, and reasoning scaffolding, all run on CPU-only local hardware required by data governance restrictions precluding cloud processing. Mistral-Large-2-123B under a contrastive harness condition achieved the best result (pair-level macro-F1 = 0.652), compared with the zero-shot NLI RoBERTa baseline (F1 = 0.110). Two tier-dependent patterns emerged: contrastive prompting was optimal for 70B+ models (mean tier F1 = 0.611), while code-by-code label decomposition was optimal for 9–14B models (mean tier F1 = 0.556). Group-routing accuracy exceeded 0.83 for all LLMs. Phi-4-14B with code-by-code decomposition (F1 = 0.599 in 7.5 hours) was the most compute-efficient high-performing configuration. Open-source LLMs can thus perform automated iCBT behavioural coding under resource-constrained, privacy-preserving deployment, giving programmes without cloud infrastructure a path to scalable therapist fidelity monitoring.

**Решение:** + T1/T4 поведенческое кодирование переписки в интернет-CBT по шкале ICBT-TRS, 9 LLMs vs эталонная разметка, macro-F1=0.652

---

### 302 · R4333

**A Trustworthy LLM-Assisted Qualitative Content Analysis Method**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-38014-2_23

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? нет аннотации; метод качественного контент-анализа с LLM, проверить по полному тексту предметное поле и согласие с экспертами

---

### 303 · R0614

**Measuring Destination Image in Real Time: Validating Large Language Model Scoring of Visual Diaries Against Established Scales**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.6783680

Destination image (DI) measurement has long faced a trade-off between quantitative rigor and qualitative richness. Structured surveys provide psychometric precision but impose researcherdefined attributes and are subject to retrospective bias, while open-ended methods preserve richer perceptions but require labor-intensive manual coding that limits scalability and rules out realtime monitoring. This study introduces and validates a method that combines visual diaries-brief spoken narratives recorded on participants' smartphones during the trip-with zero-shot large language model (LLM) scoring to bridge these two measurement traditions. In a longitudinal study of 187 tourists visiting the Canary Islands at three timepoints (pre-trip, during-trip, post-trip), diary transcripts were independently scored on cognitive, affective, and conative dimensions by an ensemble of three frontier LLMs (including GPT-4-class models) using theory-grounded prompts mapped to Beerli and Martín's (2004) destination image framework. Across the resulting scores we find adequate to strong psychometric properties: internal consistency (α = .84-.91), inter-model agreement (ICC = .72-.79), convergent validity with established survey scales (r = .69-.78), discriminant validity supported by confirmatory factor analysis and heterotrait-monotrait ratios, and criterion validity predicting satisfaction and behavioral loyalty at levels comparable to traditional survey measures. The LLM-derived scores also detect theoretically expected temporal patternsincluding cognitive updating during the trip and substantial heterogeneity in individual image trajectories-that retrospective single-shot surveys cannot resolve. The proposed pipeline reduces coding effort by orders of magnitude relative to manual content analysis, runs end-to-end within hours of data collection, and is fully reproducible from raw transcripts, the published prompts, and open analysis code. Sensitivity analyses across alternative prompt formulations, scoring models,&amp;nbsp;and analytic specifications indicate that the validity evidence is robust rather than tied to a particular configuration. These findings suggest that visual diaries combined with LLM scoring offer a viable pathway for DI measurement that preserves narrative richness without sacrificing psychometric standards, enabling longitudinal, real-time, and large-scale designs—including in-trip monitoring and cross-destination comparison—that have been difficult to implement with existing methods.

**Решение:** -4 туризм и маркетинг территорий, шкалы восприятия туристических направлений по дневникам

---

### 304 · R8488

**Time-Aware Ordinal Modelling of Sequential Text Data: A Two-Stage Architecture Combining Llm Classification and Lightweight Temporal Models**

2025 · BigData Congress [Services Society] · journalarticle, conference · https://doi.org/10.1109/bigdata66926.2025.11400865

We address next-post suicide-risk prediction from short Reddit sequences in the IEEE Big Data 2025 Data Cup setting. Each user's last five posts are inputs; the ordinal risk of the unseen next post is the target. A prompt-based LLM + lightweight temporal aggregation (recency weights, timedistance, ARIMA) is compared with compact neural baselines (MiniLM+ordinal MLP, time-aware GRU, DistilBERT+LoRA). On data based on [1], the best LLM+aggregation variant achieves F1-weighted $\sim 0.72$ and MAE $\sim 0.30$, and is strongest on final-observation sequences.

**Решение:** ? оценка суицидального риска по Reddit (IEEE BigData Cup / C-SSRS), prompt-based LLM vs эталонная разметка, F1=0.72; проверить T3 vs критериальный исход

---

### 305 · R8946

**AdvAttack-LLM: Exploiting Elasticity in Large Language Models for Efficient Adversarial Attacks**

2025 · 2025 IEEE 6th International Conference on Computer, Big Data, Artificial Intelligence (ICCBD+AI) · conference, conference-paper · https://doi.org/10.1109/iccbdai66607.2025.11389048

Despite significant advancements in safety alignment, Large Language Models (LLMs) remain vulnerable to adversarial attacks that manipulate their behavior through carefully crafted inputs. This paper investigates the inherent elasticity of LLMs—their tendency to revert to pre-training distributions when subjected to adversarial fine-tuning. We propose a novel adversarial attack framework, AdvAttack-LLM, that systematically exploits this elasticity to efficiently compromise model alignment. Through comprehensive experiments on LLaMA-3 models using the AdvBench dataset, we demonstrate that elasticity-based adversarial attacks achieve significantly higher success rates (54.8%) with substantially fewer queries (25.2 average queries) compared to state-of-the-art methods. Our theoretical analysis, grounded in compression theory with detailed physical interpretations, reveals that the effectiveness of adversarial attacks is inversely proportional to the KL divergence between pre-training and alignment distributions, explaining why minimal adversarial perturbations can subvert extensively aligned models. These findings highlight critical security vulnerabilities in current alignment approaches and underscore the need for elasticity-aware defense mechanisms.

**Решение:** -4 кибербезопасность, состязательные атаки на LLM с использованием эластичности (AdvBench)

---

### 306 · R12264

**ChatGPT: Threat or boon to the future of pharmacy practice?**

2023 · Research in Social and Administrative Pharmacy · article · en · https://doi.org/10.1016/j.sapharm.2023.03.012

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 комментарий/колонка в журнале о роли ChatGPT в практике фармации, не эмпирика

---

### 307 · R5821

**Evaluation of Automatic Speech Recognition Using Generative Large Language Models**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.21928

Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.

**Решение:** -4 оценка качества распознавания речи (ASR) с помощью LLM, компьютерные науки

---

### 308 · R7415

**Merger-as-a-Stealer: Stealing Targeted PII from Aligned LLMs with Model Merging**

2025 · Underline Science Inc. · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48448/7ejb-st92

Model merging has emerged as a promising approach for updating large language models (LLMs) by integrating multiple domain-specific models into a cross-domain merged model. Despite its utility and plug-and-play nature, unmonitored mergers can introduce significant security vulnerabilities, such as backdoor attacks and model merging abuse. In this paper, we identify a novel and more realistic attack surface where a malicious merger can extract targeted personally identifiable information (PII) from an aligned model with model merging. Specifically, we propose \texttt{Merger-as-a-Stealer}, a two-stage framework to achieve this attack: First, the attacker fine-tunes a malicious model to force it to respond to any PII-related queries. The attacker then uploads this malicious model to the model merging conductor and obtains the merged model. Second, the attacker inputs direct PII-related queries to the merged model to extract targeted PII. Extensive experiments demonstrate that \texttt{Merger-as-a-Stealer} successfully executes attacks against various LLMs and model merging methods across diverse settings, highlighting the effectiveness of the proposed framework. Given that this attack enables character-level extraction for targeted PII without requiring any additional knowledge from the attacker, we stress the necessity for improved model alignment and more robust defense mechanisms to mitigate such threats. 17 pages, 3 figures

**Решение:** -4 кибербезопасность, извлечение персональных данных (PII) при слиянии моделей

---

### 309 · R5773

**Generative AI tool evaluating employees’ self-reflection and performance metrics for supporting managers in 1:1 interviews**

2026 · Journal of Decision System · article · en · https://doi.org/10.1080/12460125.2026.2655313

This study evaluates a generative AI tool designed to support managers in preparing for quarterly 1:1 employee interviews. The tool, built on OpenAI’s LLMs, processes employee self-reflection texts and structured performance data to generate meeting preparation summaries. A total of 78 human experts evaluated the tool’s outputs using a five-point Likert scale and open-ended questions. Quantitative results indicate that standard model GPT-4o significantly outperformed lightweight model GPT-4o-mini across nearly all evaluation variables, with scores consistently above 4, suggesting meeting users’ real-life expectations. Automated processing required approximately 7% of estimated manual preparation time. Qualitative analysis revealed emotional and contextual blindness as the primary limitation, alongside concerns about managerial detachment from employee data. The findings suggest that GenAI tools can effectively augment managerial preparation, but also emphasise that human judgement remains essential for meaningful performance conversations.

**Решение:** -4 HR-менеджмент, подготовка руководителей к 1:1 интервью с сотрудниками

---

### 310 · R7788

**Is ChatGPT-4 a Reliable Tool in Autoimmune Hepatitis?**

2025 · The American journal of gastroenterology · journal article, med, journalarticle · eng · https://doi.org/10.14309/ajg.0000000000003179

INTRODUCTION: Artificial intelligence-based chatbots offer a potential avenue for delivering personalized counseling to patients with autoimmune hepatitis. We assessed accuracy, completeness, comprehensiveness, and safety of Chat Generative Pretrained Transformer-4 responses to 12 inquiries out of a pool of 40 questions posed by 4 patients with autoimmune hepatitis. METHODS: Questions were categorized into 3 areas: diagnosis (1-3), quality of life (4-8), and medical treatment (9-12). 11 key opinion leaders evaluated responses using a Likert scale with 6 points for accuracy, 5 points for safety, and 3 points for completeness and comprehensiveness. RESULTS: Median scores for accuracy, completeness, comprehensiveness, and safety were 5 (4-6), 2 (2-2), and 3 (2-3), respectively; no domain exhibited superior evaluation. Postdiagnosis follow-up question was the trickiest with low accuracy and completeness, but safe and comprehensive features. Agreement among key opinion leaders (Fleiss Kappa statistics) was slight for the accuracy (0.05) but poor for the remaining features (-0.05, -0.06, and -0.02, respectively). DISCUSSION: Chatbots show good comprehensibility, but lack reliability. Further studies are needed to integrate Chat Generative Pretrained Transformer within clinical practice.

**Решение:** -2 врачи оценивают ответы ChatGPT-4 по аутоиммунному гепатиту (к тому же соматическая гастроэнтерология)

---

### 311 · R1978

**An LLM-Powered Embodied VR Tutor for Smoking Cessation: SRL via Reflective Dialogue**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-29794-5_34

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? нет аннотации; VR-тьютор для отказа от курения, проверить по полному тексту (вероятно интервенция -6 или -2)

---

### 312 · R11331

**Response to ChatGPT in surgical research and practice: a threat to academic integrity, authorship, and divergent thinking.**

2024 · ANZ journal of surgery · letter, comment, med · eng · https://doi.org/10.1111/ans.18698

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 письмо в редакцию, применение ChatGPT в хирургии и академическая этика, не эмпирика

---

### 313 · R5945

**Large Language Models as Distributional Baselines for Language Tasks.**

2026 · Open mind : discoveries in cognitive science · journal article, journalarticle, review · eng · https://doi.org/10.1162/opmi.a.373

Abstract In order to ask questions about the mechanisms underpinning human cognition, researchers must control for properties of stimuli that could confound detected effects. In experiments involving linguistic stimuli, this includes properties like frequency, length, and neighborhood size of those stimuli, which are known to affect behavioral and neural responses. With improvements in the performance and usability of language models, it is now possible to also control for how predictable stimuli and their parts are, on the basis of the distributions of words alone: their distributional predictability. This coincides with a resurgence of interest in the possibility that statistical language learning may underlie a broad range of human cognitive phenomena; indeed, there are both theoretical and empirical reasons to believe that humans rely on distributional information during certain cognitive tasks. This creates a confound, whereby experimental operationalizations of psychological constructs with linguistic stimuli may not in fact be testing what they are intended to test. Thus, the central contributions of this paper are twofold: first, we articulate the conditions under which distributional predictability threatens the internal validity of an experiment; and second, we provide concrete recommendations for how to control for this potential confound. Beyond these primary contributions, we survey techniques for measuring distributional predictability, review theoretical and empirical work supporting the role of distributional statistics in human cognition, and present several case studies illustrating the range of possible outcomes—from the “distributional baselines” only marginally affecting theoretical inferences to constituting fully deflationary confounds. We also enumerate and address potential objections to this approach. This paper is primarily intended for researchers in psychology, cognitive science, and linguistics who use linguistic stimuli but have not yet incorporated distributional baselines into their work.

**Решение:** -1 обзор/методологическая статья по статистическим распределительным бейслайнам в когнитивных науках

---

### 314 · R2348

**Detecting Mental Health Signals in Social Media Text: A Large Language Model–Based Approach with Knowledge-Informed Prompt Engineering (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.98535

BACKGROUND Mental disorders are often under detected, and social media text has emerged as a complementary source of behavioral signals for digital mental health research. Existing approaches for detecting mental health conditions from user-generated content commonly rely on disorder-specific supervised machine learning models or large language model–based discrete prompting strategies, which may require substantial labeled data and may not systematically incorporate domain knowledge. OBJECTIVE This study aimed to develop and evaluate a large language model–based method for detecting mental health signals from user-generated social media text by combining personalized continuous prompting with structured medical knowledge. METHODS We proposed a continuous multi-prompt framework built on FLAN-T5 that integrates 2 components: (1) prefix tuning to capture user-level personalized context and (2) a rule-based prompt layer that injects ontology-based medical knowledge related to symptoms, life events, and treatments. The method is evaluated on eRisk datasets for depression and pathological gambling using subject-level prediction from longitudinal social media posts. The depression dataset included 1707 subjects (214 positive, 1493 negative), and the pathological gambling dataset included 4427 subjects (245 positive, 4182 negative). Data are split into training, validation, and test sets (60%/20%/20%), and results are averaged over 10 runs. We report F1-score, precision, and recall and compare the proposed method with traditional machine learning, deep learning, discrete prompting, and large language model fine-tuning baselines. We also examined few-shot learning, early identification, performance on a rare-disorder dataset (self-harm; 340 subjects, including 41 positive cases), and alignment with psychiatrist ratings. RESULTS The proposed method achieved the highest F1-scores among the evaluated approaches on both primary tasks. For depression detection, it achieved an F1-score of 0.913, precision of 0.888, and recall of 0.939. For pathological gambling detection, it achieved an F1-score of 0.985, precision of 0.985, and recall of 0.990. On the rare-disorder self-harm dataset, the method achieved an F1-score of 0.917. In post hoc evaluation, model probabilities showed strong alignment with psychiatrist ratings (Pearson r=0.8656), while expert interrater agreement is high (Pearson r=0.9636). CONCLUSIONS A large language model approach that combines personalized continuous prompting with structured medical knowledge can improve detection of mental health–related signals in social media text. These findings support the potential of knowledge-informed prompt engineering for scalable, data-efficient digital mental health research using user-generated content. This approach should be interpreted as a complementary screening and monitoring tool for research settings rather than as a clinical diagnostic system.

**Решение:** -3 критериальная валидность: датасеты eRisk с бинарной меткой депрессии/гемблинга по самоотчету пользователей, а не экспертная разметка текста

---

### 315 · R12511

**A new era in Internet interventions: The advent of Chat-GPT and AI-assisted therapist guidance**

2023 · Internet Interventions · editorial, journalarticle · eng · https://doi.org/10.1016/j.invent.2023.100621

There are a wealth of different internet-based treatments available that are commonly classified into two categories: live, real time video therapy – such as telepsychiatry using Zoom – or digital self-help programs with or without human guidance that is often asynchronous (Andersson et al., 2019). Combinations of these two approaches also exist along with the blending of internet-based treatments with face-toface therapy (Erbe et al., 2017). Understanding the significance of differences in approaches is complicated by inconsistent and confusing terminology used to describe the approaches (Smoktunowicz et al., 2020). Typically, guided internet-based treatments tend to be more effective than pure self-help (Baumeister et al., 2014). According to a recent meta-analysis, therapist-guided internet-based cognitive behavior therapy yields similar effects as face-to-face therapy for psychiatric and somatic disorders (Hedman-Lagerlöf et al., in press). Moreover, without support, the effects of internet-based treatment tend to be smaller, and dropout rates increase (Koelen et al., 2022). While clearly beneficial, human guidance cannot easily be scaled to cover the treatment needs (Fairburn and Patel, 2017). Consequently, there has been a growing interest in improving the effectiveness of internet-based interventions with lower degrees of guidance. While some advancements have been made using automated support (e.g., Titov et al., 2013), and support on demand (Hadjistavropoulos et al., 2019), there is still room for improving lower-intensity internet-based treatments. There are, in fact, very few pure internet-based self-help studies available, as most of these studies incorporate human contact in the form of diagnostic or screening interviews before treatment begins, or they provide access to human backup support in the event of an emergency or technological challenge during treatment. With developments in artificial intelligence (AI), study of the integration of AI and internet-based treatment represents an important direction in optimizing internet-based treatments. One possible solution could be to integrate AI, in the form of a conversational agent, into the platforms (Ly et al., 2017; Morris et al., 2018) either as a tutor that becomes a virtual psychoeducational coach available to the client at all hours of the day, or taking on the role of a psychotherapist, giving constructive feedback and posing clinically informed inquiries such as Socratic questions that could directly help the client when analyzing negative automatic thoughts or maladaptive core beliefs. In this context, it is important to acknowledge that automated interactions with a computer have existed for a long time, but were only widely implemented more recently (Epstein and Klinkenberg, 2001). Arguably, AI can be seen as a way to improve automated treatments like the early Eliza that was invented already in the 1960's. With good implementation, the new AI-applications have the potential to significantly improve internet-based treatments and save clinicians time, but it also raises questions about the potential negative implications of using AI and large language models, such as GPT, in this field. One important limitation is that a machine does not yet possess humanlike empathy or emotions, and hence has difficulty understanding the nuances of human language. A conversational agent lacks the emotional intelligence and personal experience of a human being, but that can be hidden by expressing empathy-like utterances. In fact, a recent randomized controlled trial showed that a human–AI collaboration outperformed humans with 19.6 % more empathic conversations in text-based peer-topeer mental health support (Sharma et al., 2023). Furthermore, GPT-4 has been reported to have an advanced understanding of the theory of mind (Bubeck et al., 2023). However, a conversational agent mimicking empathy and responding appropriately may not be enough. When a human communicates, one may say one thing with words, but the body language might convey a different meaning or emotion. Interpreting irony from a client is also a potential pitfall, which could lead to inappropriate therapeutic suggestions (such as promoting safety-seeking behaviors; Rozental et al., 2018). The use of AI guided interventions with more difficult and severe cases requires careful consideration and likely safeguards such as availability of clinicians who are capable of managing deterioration and other potential negative events. Research has shown that the therapeutic alliance, which refers to the collaborative relationship between a human clinician and a human

**Решение:** -1 редакционная статья / editorial об интернет-интервенциях и ChatGPT, не эмпирика

---

### 316 · R9770

**Automating Thematic Analysis with Multi-Agent LLM Systems**

2025 · Center for Open Science · posted-content · https://doi.org/10.35542/osf.io/kq8zh_v1

Thematic analysis (TA) is a method used to identify, examine, and present themes within data. TA is often a manual, multistep, and time-intensive process requiring collaboration among multiple researchers. TA’s iterative subtasks, including coding data, identifying themes, and resolving inter-coder disagreements, are especially laborious for large data sets. Given recent advances in natural language processing, Large Language Models (LLMs) offer the potential for automation at scale. Recent literature has explored the automation of isolated steps of the TA process, tightly coupled with researcher involvement at each step. Research using such hybrid approaches has reported issues in LLM generations, such as hallucination, inconsistent output, and technical limitations (e.g., token limits). This paper proposes a multi-agent system, differing from previous systems using an orchestrator LLM agent that spins off multiple LLM sub-agents for each step of the TA process, mirroring all the steps previously done manually. In addition to more accurate analysis results, this iterative coding process based on agents is also expected to result in increased transparency of the process, as analytical stages are documented step-by-step. We study the extent to which such a system can perform a full TA without human supervision. Preliminary results indicate human-quality codes and themes based on alignment with human-derived codes. Nevertheless, we still observe differences in coding complexity and thematic depth. Despite these differences, the system provides critical insights on the path to TA automation while maintaining consistency, efficiency, and transparency in future qualitative data analysis, which our open-source datasets, coding results, and analysis enable.

**Решение:** ? автоматизация тематического анализа мультиагентной системой LLM; проверить по полному тексту предметную область и наличие метрик согласия (T1 vs -6)

---

### 317 · R11543

**LLM-GEm: Large Language Model-Guided Prediction of People’s Empathy Levels towards Newspaper Article**

2024 · Findings of the Association for Computational Linguistics: EACL · audiovisual/conference talk, journalarticle, conference-paper · https://doi.org/10.18653/v1/2024.findings-eacl.147

Empathy – encompassing the understanding and supporting others’ emotions and perspectives – strengthens various social interactions, including written communication in healthcare, education and journalism. Detecting empathy using AI models by relying on self-assessed ground truth through crowdsourcing is challenging due to the inherent noise in such annotations. To this end, we propose a novel system, named Large Language Model-Guided Empathy _(LLM-GEm)_ prediction system. It rectifies annotation errors based on our defined annotation selection threshold and makes the annotations reliable for conventional empathy prediction models, e.g., BERT-based pre-trained language models (PLMs). Previously, demographic information was often integrated numerically into empathy detection models. In contrast, our _LLM-GEm_ leverages GPT-3.5 LLM to convert numerical data into semantically meaningful textual sequences, enabling seamless integration into PLMs. We experiment with three _NewsEmpathy_ datasets involving people’s empathy levels towards newspaper articles and achieve state-of-the-art test performance using a RoBERTa-based PLM. Code and evaluations are publicly available at [https://github.com/hasan-rakibul/LLM-GEm](https://github.com/hasan-rakibul/LLM-GEm).

**Решение:** -5 генеративная LLM использована только для конвертации демографии в текст для RoBERTa, нет LLM-оценщика; к тому же эмпатия к новостям

---

### 318 · R5213

**Comparing AI and Human Coding of NIH Grant Abstracts to Identify Innovations in Opioid Addiction Treatment**

2026 · CrimRxiv · preprint · en · https://doi.org/10.21428/cb6ab371.4e14f7c0

Abstract Large language models (LLMs) are increasingly used for qualitative analysis in substance use research, yet their performance relative to human coders remains underexplored. This study compares ChatGPT-4.0 with human coders in identifying and describing the core innovation of NIH grants focused on reducing opioid overdose. A total of 118 NIH HEAL Initiative grant abstracts were independently coded by ChatGPT and humans to generate innovation descriptions, which were then evaluated by both human raters and ChatGPT for depth/detail and relevance/completeness using 5-point Likert scales. Identical instructions were used across all coding and evaluation stages. ChatGPT-generated descriptions were consistently rated higher than human-generated descriptions on both dimensions. Human evaluators rated ChatGPT outputs at an average of 4.47 for both depth/detail and relevance/completeness, compared to 3.33 and 3.24 for human outputs, respectively (F(1,176)=133.9, p<0.001). These findings suggest that LLMs, when carefully prompted, can enhance the efficiency and quality of qualitative research evaluation.

**Решение:** -4 оценка описаний инноваций в аннотациях грантов NIH HEAL, наукометрия/грантовая экспертиза

---

### 319 · R1381

**Using Large Language Models to Summarize Evidence in Biomedical Articles: Exploratory Comparison Between AI- and Human-Annotated Bibliographies.**

2026 · JMIR formative research · comparative study, research support, non-u.s. gov't, research-article · eng · https://doi.org/10.2196/69707

Abstract Background Annotated bibliographies summarize literature, but training, experience, and time are needed to create concise yet accurate annotations. Summaries generated by artificial intelligence (AI) can save human resources, but AI-generated content can also contain serious errors. Objective To determine the feasibility of using AI as an alternative to human annotators, we explored whether ChatGPT can generate annotations with characteristics that are comparable to those written by humans. Methods We had 2 humans and 3 versions of ChatGPT (3.5, 4, and 5) independently write annotations on the same set of 15 publications. We collected data on word count and Flesch Reading Ease (FRE). In this study, 2 assessors who were masked to the source of the annotations independently evaluated (1) capture of main points, (2) presence of errors, and (3) whether the annotation included a discussion of both the quality and context of the article within the broader literature. We evaluated agreement and disagreement between the assessors and used descriptive statistics and assessor-stratified binary and cumulative mixed-effects logit models to compare annotations written by ChatGPT and humans. Results On average, humans wrote shorter annotations (mean 90.20, SD 36.8 words) than ChatGPT (mean 113, SD 16 words) which were easier to interpret (human FRE score, mean 15.3, SD 12.4; ChatGPT FRE score, mean 5.76, SD 7.32). Our assessments of agreement and disagreement revealed that one assessor was consistently stricter than the other. However, assessor-stratified models of main points, errors, and quality/context showed similar qualitative conclusions. There was no statistically significant difference in the odds of presenting a better summary of main points between ChatGPT- and human-generated annotations for either assessor (Assessor 1: OR 0.96, 95% CI 0.12‐7.71; Assessor 2: OR 1.64, 95% CI 0.67‐4.06). However, both assessors observed that human annotations had lower odds of having one or more types of errors compared to ChatGPT (Assessor 1: OR 0.31, 95% CI 0.09‐1.02; Assessor 2: OR 0.10, 95% CI 0.03‐0.33). On the other hand, human annotations also had lower odds of summarizing the paper’s quality and context when compared to ChatGPT (Assessor 1: OR 0.11, 95% CI 0.03‐0.33; Assessor 2: OR 0.03, 95% CI 0.01‐0.10). That said, ChatGPT’s summaries of quality and context were sometimes inaccurate. Conclusions Rapidly learning a body of scientific literature is a vital yet daunting task that may be made more efficient by AI tools. In our study, ChatGPT quickly generated concise summaries of academic literature and also provided quality and context more consistently than humans. However, ChatGPT’s discussion of the quality and context was not always accurate, and ChatGPT annotations included more errors. Annotated bibliographies that are AI-generated and carefully verified by humans may thus be an efficient way to provide a rapid overview of literature. More research is needed to determine the extent that prompt engineering can reduce errors and improve chatbot performance.

**Решение:** -6 суммаризация научной биомедицинской литературы / аннотированная библиография, другая задача

---

### 320 · R7163

**Exploring Generative Artificial Intelligence to Enhance Reflective Writing in Pharmacy Education.**

2025 · American journal of pharmaceutical education · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.ajpe.2025.101416

The integration of generative artificial intelligence (AI) holds the potential to impact teaching and learning. In this commentary, we explore the opportunity for AI to enhance reflective writing (RW) among student pharmacists. AI-guided RW has the potential to strengthen students' reflective capacity, deepen their autobiographical memory, and develop their self-confidence. This commentary presents examples of how AI can be utilized to enrich RW and includes a sample prompt aimed at facilitating student self-reflection. We explore how integrating AI-facilitated RW assignments into the pharmacy curriculum can help students develop detailed examples for self-reflection and gain exposure to the potential uses of AI in their professional development and career advancement.

**Решение:** -1 комментарий / эссе о рефлексивном письме в фармацевтическом образовании, не эмпирика

---

### 321 · R6206

**Leveraging LLM-as-a-Judge for Automatic Evaluation in Construction Safety**

2026 · ASCE Construction Research Congress (CRC) · conference-paper · https://doi.org/10.1061/9780784486993.090

The construction industry is characterized by traditional practices and heavily relies on worker surveys to collect critical feedback on safety, productivity, and engagement. However, evaluating responses to open-ended survey questionnaires is both labor-intensive and time-consuming, and there is a lack of scalable solutions, especially when addressing safety issues. It is a critical concern in this high-risk industry. This study proposes a novel approach using large language models (LLMs) as automated evaluators to assess the quality of construction worker feedback. Due to limited survey data, this study utilized comments from construction-related communities on Reddit as a proxy, leveraging their rich worker-generated content to simulate open-ended survey responses. This method employs robust prompt engineering to guide the LLM in evaluating responses based on relevance, information density, and clarity, while ensuring reliability through strict input validation. Community likes to serve as a benchmark for response quality, combining the model’s judgments with insights valued by workers. By automating the evaluation process, this method offers a scalable, data-driven solution that overcomes the limitations of manual survey analysis.

**Решение:** -4 охрана труда в строительстве, оценка отзывов строителей на Reddit

---

### 322 · R2520

**Do Large Language Models Replicate Value-Laden Judicial Reasoning? Evidence from Domestic Violence Adjudication in China**

2026 · Research Square · preprint, ppr · en · https://doi.org/10.21203/rs.3.rs-8985237/v1

Abstract Large language models are increasingly deployed in quasi-adjudicative legal settings, yet the field lacks a validated framework for empirically assessing judicial quality in value-intensive domains. This Article introduces and validates DV-JusticeBench, an expert-annotated benchmark and reproducible four-stage evaluation framework designed to measure the quality of value-laden judicial reasoning. Constructed from 108 authentic Chinese domestic violence cases (2023–2025) and 540 structured dispute-centered questions, the framework operationalizes adjudicative quality across five analytically distinct dimensions: normative-basis relevance, subsumption-chain coherence, value balancing and empathy alignment, evidentiary fact coverage, and outcome–remedy alignment. Structured scoring rubrics ensure transparency, replicability, and cross-model comparability. Evaluating six frontier LLMs serves as a proof of concept for the framework’s measurement capacity. The results reveal systematic tensions between affective responsiveness and doctrinal discipline, including mismanagement of contested facts and overreliance on surface forensic cues. By demonstrating how value-dense adjudication can be decomposed and empirically measured, this study provides a generalizable framework for assessing AI-assisted judicial reasoning, with direct implications for the governance of AI deployment in courts and the design of institutional quality-control mechanisms for legal AI systems.

**Решение:** -4 юриспруденция, оценка судебных решений по домашнему насилию в Китае (DV-JusticeBench)

---

### 323 · R8764

**LlaMADRS: Prompting Large Language Models for Interview-Based Depression Assessment**

2025 · text · https://core.ac.uk/download/725878349.pdf

This study introduces LlaMADRS, a novel framework leveraging open-source Large Language Models (LLMs) to automate depression severity assessment using the Montgomery-Asberg Depression Rating Scale (MADRS). We employ a zero-shot prompting strategy with carefully designed cues to guide the model in interpreting and scoring transcribed clinical interviews. Our approach, tested on 236 real-world interviews from the Context-Adaptive Multimodal Informatics (CAMI) dataset, demonstrates strong correlations with clinician assessments. The Qwen 2.5--72b model achieves near-human level agreement across most MADRS items, with Intraclass Correlation Coefficients (ICC) closely approaching those between human raters. We provide a comprehensive analysis of model performance across different MADRS items, highlighting strengths and current limitations. Our findings suggest that LLMs, with appropriate prompting, can serve as efficient tools for mental health assessment, potentially increasing accessibility in resource-limited settings. However, challenges remain, particularly in assessing symptoms that rely on non-verbal cues, underscoring the need for multimodal approaches in future work

**Решение:** + T3 LlaMADRS: автоматическая оценка тяжести депрессии по шкале MADRS в транскриптах клинических интервью CAMI, Qwen 2.5 vs клиницисты, ICC

---

### 324 · R0619

**Jailbreaking Aligned Large Language Models: A Systematic Survey of Attack Taxonomies, Evaluation Frameworks, and Defense Mechanisms**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.23457530

Large language models (LLMs) are now deployed to hundreds of millions of users, and their safe behavior depends on alignment techniques such as supervised fine-tuning and reinforcement learning from human feedback. Yet a class of adversarial inputs known as jailbreaks continues to circumvent these safeguards, eliciting outputs the models were trained to refuse. This paper presents a systematic survey of the jailbreak literature. We formalize the threat model, propose a two-dimensional taxonomy that separates attacks by adversary capability (white-box versus black-box) and by exploitation mechanism, and review representative methods in each category, from gradient-based suffix optimization to persuasion-driven and many-shot techniques. We then examine how the community evaluates attacks and defenses, covering benchmarks, success metrics, and automated judges, and we organize defense strategies into prompt-level, model-level, and system-level interventions. Finally, we identify open challenges — including the generalization of defenses, the security of agentic and multimodal systems, and the limits of current evaluation — and outline directions for future research.

**Решение:** -1 систематический обзор атак и защит jailbreaking в LLM, не эмпирика

---

### 325 · R0813

**When minds meet words : authenticity and motivation expressed and perceived in language**

2026 · Universität Stuttgart · other/doctoralthesis, dissertation · en · https://doi.org/10.18419/opus-18374

In a world where much of everyday communication now takes place online, the words people choose carry great consequences. Language conveys far more than the content of a message; it reflects the author's motivations, intentions, and self-presentation, and it is interpreted through the psychological characteristics of its readers. Although these aspects have been studied extensively in psychology, they remain only sparsely integrated into natural language processing (NLP). While advances in NLP allow models to capture rich linguistic and contextual structure, they do not typically treat language as an expression shaped by human cognition. This creates a gap in applications where the effectiveness of communication depends on understanding both the author behind the words and the audience who receives them. This thesis addresses this gap by focusing on two psychological constructs that are central to persuasive and interpersonal communication yet understudied in NLP: regulatory focus, which shapes how people frame goals and respond to motivational cues, and authenticity, which influences judgments of sincerity, trustworthiness, and credibility. These constructs were selected because they represent two complementary dimensions of communication, one grounded in clear motivational framing that leaves identifiable linguistic patterns and the other reflecting subtle, subjective self-expression that is difficult to model computationally. The overarching research questions guiding the thesis are: (1) how authenticity and regulatory focus manifest in language and whether computational models can detect them, and (2) to what extent do LLMs produce text that reflects these psychological constructs when prompted, and how do humans perceive the generated messages? The first part of the thesis examines how these constructs surface linguistically. Authenticity is defined in psychology as the alignment between a person's genuine beliefs, values, and feelings and the way they express themselves. Because truthful expression is a necessary condition for this alignment, deception provides a measurable way to capture one dimension of inauthentic communication: a deliberate mismatch between belief and expression. Using this perspective, I model authenticity through belief-based deception and introduce new corpora that disentangle deceptive intent from factual correctness, showing that linguistic markers associated with (in)authenticity are highly inconsistent and do not generalize across domains or languages. In contrast, regulatory focus, which describes whether individuals pursue goals through promotion (aspiration) or prevention (avoidance), produces more stable lexical and affective patterns under controlled conditions. However, both constructs exhibit strong contextual dependence, indicating that psychological signals in text are not universal markers but situated expressions. The second part of the thesis examines how large language models (LLMs) can be guided to generate language aligned with these psychological dimensions, and how humans perceive such messages. Through validation and a preregistered psychology experiment, I show that LLMs can be prompted to express regulatory framing and tones associated with authentic expression, although not always consistently. Readers' responses do not uniformly follow classical predictions such as regulatory fit. Instead, persuasiveness depends on interactions between framing, tone, and individual motivational orientation, highlighting complex dynamics in how machine-generated text is interpreted. These findings show that models capture statistical patterns in expression rather than underlying mental states, and that psychological meaning in text is context dependent, dynamic, and shaped by both authors and readers. Through this work, the thesis contributes datasets, analytical frameworks, and empirical insights that highlight both the opportunities and the challenges in building psychology-aware NLP systems.

**Решение:** ? докторская диссертация: моделирование аутентичности и регуляторного фокуса в языке; проверить по полному тексту наличие валидации согласия LLM с людьми

---

### 326 · R5754

**Artificial intelligence for automated ICD-10 coding: a systematic review of multi-label text classification in clinical narratives.**

2026 · Frontiers in digital health · journal article, systematic review, journalarticle · eng · https://doi.org/10.3389/fdgth.2026.1905379

Background: ICD-10 coding is an essential process in healthcare systems that supports clinical management, reimbursement, and health data analytics. However, the complexity of its hierarchical structure and the large number of available codes make manual coding limited in terms of time, cost, and consistency. Despite growing research in this area, evidence remains fragmented, particularly regarding real-world implementation readiness. Objective: To review and synthesize existing knowledge on algorithms, datasets, evaluation methods, and real-world implementation readiness of automatic ICD-10 coding systems. Methods: Eligible studies were original research articles, preprints, or conference papers published in English between January 1, 2020 and December 31, 2025, and retrieved from seven academic databases: Scopus, PubMed, Web of Science, IEEE Xplore, ACM Digital Library, arXiv, and Google Scholar. Studies were included if they investigated automatic ICD-10 coding from clinical text using machine learning, deep learning, transformer-based, or large language model (LLM) approaches. Methodological quality was assessed using a research-question-driven appraisal framework. This systematic review followed PRISMA 2020 guidance and was preregistered in the Open Science Framework (OSF) at https://osf.io/cegqk. Results: A total of 257 records were identified, of which 24 studies met the inclusion criteria and contributed 296 experimental evaluations overall. Study quality was high in 7 studies, moderate in 8, and limited by technical or methodological concerns in 9. Hybrid deep learning (Hybrid DL) was most often used as the main automated coding approach, while machine learning (ML) and rule-based approaches were mainly used as baselines. F1-macro was consistently lower than F1-micro among studies reporting both metrics. Hybrid DL showed the most stable performance under all-code or full-code evaluation, while AI model performance varied by the documents-per-label (D/L) ratio. Discussion: The evidence indicates continued technical progress, particularly through Hybrid DL and transformer-based approaches, while LLM-based methods remain emerging and less consistently effective for structured multi-label coding. The observed D/L-performance relationship suggested that AI model selection should consider dataset structure and label support, in addition to algorithmic complexity. Conclusion: AI-based automatic ICD-10 coding is a promising approach for clinical coding support. Future research should prioritize rare-label imbalance, reproducibility, explainability, and validation across diverse clinical settings. Systematic Review Registration: https://osf.io/cegqk.

**Решение:** -1 систематический обзор автоматического кодирования по МКБ-10, не эмпирика

---

### 327 · R5610

**Preparing AI chatbots to respond to patient distress and suicidality in high-risk healthcare settings.**

2026 · NPJ digital medicine · journalarticle, lettersandcomments, letter · eng · https://doi.org/10.1038/s41746-026-03288-9

Generative artificial intelligence (AI) chatbots are conversational agents that simulate human-like conversations in real-time, including behavioral health support, thus presenting challenges for monitoring and intervening on suicide risk. There is little information on how to address suicide risk in chatbot deployments, despite calls and concerns. We describe suicide safety monitoring features for a chatbot implemented in a high-risk clinical setting and make recommendations for chatbot design alongside human-monitoring and triage.

**Решение:** -1 письмо/комментарий: рекомендации по мониторингу суицидального риска в чат-ботах, не эмпирика

---

### 328 · R12399

**QualiGPT: GPT as an easy-to-use tool for qualitative coding**

2023 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2310.07061

Qualitative research delves deeply into individual complex perspectives on technology and various phenomena. However, a meticulous analysis of qualitative data often requires a significant amount of time, especially during the crucial coding stage. Although there is software specifically designed for qualitative evaluation, many of these platforms fall short in terms of automatic coding, intuitive usability, and cost-effectiveness. With the rise of Large Language Models (LLMs) such as GPT-3 and its successors, we are at the forefront of a transformative era for enhancing qualitative analysis. In this paper, we introduce QualiGPT, a specialized tool designed after considering challenges associated with ChatGPT and qualitative analysis. It harnesses the capabilities of the Generative Pretrained Transformer (GPT) and its API for thematic analysis of qualitative data. By comparing traditional manual coding with QualiGPT's analysis on both simulated and actual datasets, we verify that QualiGPT not only refines the qualitative analysis process but also elevates its transparency, credibility, and accessibility. Notably, compared to existing analytical platforms, QualiGPT stands out with its intuitive design, significantly reducing the learning curve and operational barriers for users. 25 pages, 7 figures, 1 table, under review

**Решение:** ? QualiGPT: инструмент качественного кодирования, сопоставление с ручным кодированием; проверить по полному тексту предметное поле и метрики согласия

---

### 329 · R1875

**SimInter: Evidence-Grounded User Simulation with Interview-Based Profile Enrichment for Conversational Recommender Systems**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.18308

Conversational Recommender Systems (CRSs) require reliable user simulators for cost-effective evaluation. LLM-based simulators have made realistic simulation possible but typically condition on profiles derived from explicit ratings, demographics, and static sources capturing surface preferences while omitting implicit behavioral characteristics such as decision-making style, aspect-level preferences, and domain expertise. We propose SimInter, a pipeline that elicits these attributes via synthetic interviews between two LLM agents, grounded in the user's statistical profile and historical conversational evidence. Before profile enrichment, an audit agent explicitly flags potential fabrication and stereotyping at the turn level. We instantiate and evaluate SimInter on movie recommendation. We simulate 300 ReDial users and, on a matched subset of 100 users, compare SimInter with a statistics-only baseline: SimInter significantly increases the diversity of expressed preference aspects (filtered aspect entropy: 1.619 vs. 0.859; paired d = 0.96, Holm-adjusted p &lt; 0.001). This gain persists when the simulator converses with two trained recommenders, KBRD and UniCRS, under two independent evaluation judges (+0.28 to +0.56 nats; all p &lt; 0.001). Human evaluation finds 94.3% of enriched-attribute claims supported or partially supported, while human judgments agree with 95.2% of the auditor's binary filtering decisions on a stratified sample. 25 pages, 11 figures, 12 tables. Erfan Shahabi and Amirhossein Roshandel contributed equally

**Решение:** -4 рекомендательные системы фильмов ReDial, пользовательская симуляция

---

### 330 · R10815

**Autonomous Fetal Distress Detection with Cardiotocogram Classification using Auto-Encoder Model Combined with Recurrent Neural Networks**

2024 · Nanotechnology Perceptions · article · en · https://nano-ntp.com/index.php/nano/article/view/3824

The scarcity and imbalance of high-quality annotated Cardiotocography (CTG) datasets pose significant challenges in developing most accurate fetal distress detection systems. To address this, a Generative AI based data generation technique and features selection method with classification framework was proposed which combines Auto-Encoders (AEs) and Recurrent Neural networks mainly LSTM and GRU models. The Auto-Encoder is employed to generate synthetic CTG data by capturing and reconstructing complex temporal patterns, effectively augmenting the dataset while preserving its physiological characteristics. These RNN models, designed for sequential data processing and feature selection, is then trained on the enriched dataset to classify CTG signals and detect fetal distress autonomously. Experimental results demonstrate that the proposed framework improves performance metrics for LSTM model with RmsProp optimiser when compared to GRU model interms of classification Accuracy of 98.71%, Sensitivity of 98.76%, Specificity of 99.37%, Precision of 98.65%, Weighted F1 score of 98.71%, Mean MCC of 98.06%, Mean kappa score of 98.05% and averaged AUC of 99.77% within elapsed time of 2.54 minutes. Furthermore, this methodology mitigates the effects of dataset imbalance, and enhances the generalizability of fetal distress detection systems.

**Решение:** -4 акушерство, классификация КТГ плода моделями LSTM/GRU, нет LLM и нет текста

---

### 331 · R1548

**Emerging Applications of Generative Artificial Intelligence Tools in Parascience**

2026 · Parawize Journal · journalarticle, review, article · https://doi.org/10.66589/8jqm2736

Following a rapid account of the history of Artificial Intelligence (AI), we introduce the current generation of AI tools based on ‘generative technology’, most notably ChatGPT, and outline why these tools are currently taking the world by storm. We then explore emerging uses of these tools in the parapsychology/parascience literature. We uncover two main themes: (i) analysis of narrative descriptions (e.g. for purposes of categorization), and (ii) elimination of bias in the comparison of ‘free-response’ data against target data (e.g. in remote viewing studies). Both themes explore the use of AI tools as a substitute for human researchers’ efforts in certain tasks. The potential benefits include reduced subjective bias, and the enabling and acceleration of larger-scale analyses. Outcomes so far show promising signs, with AI-tool judgements tending to match those of human experts, with similar levels of variance between judges (i.e. between different tools). However, different tools nevertheless exhibit specific nuances based on their training environment. This suggests further work is needed to understand these ‘tool-biases’ before unleashing AI-tool analyses at scale. A third theme, less explored but clearly signposted, is the development of specialized ChatGPT-style systems, enhanced with libraries of parapsychology material, to support literature study in the field (e.g. summaries, reviews). This approach has clear merits in counteracting the biases in AI tools that emerge from typical LLM training material such as Wikipedia. Finally, after considering some intrigueing related topics, we end with a note of caution and some brief speculation regarding future developments.

**Решение:** -1 нарративный обзор применения GenAI в парапсихологии и паранауке, не эмпирика

---

### 332 · R7354

**Can Large Language Models Extract Customer Needs as well as Professional Analysts?**

2025 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5167493

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 маркетинг, извлечение потребностей клиентов для продуктовой аналитики

---

### 333 · R0963

**Can LLMs Read Between the Lines? Large Language Model Applications in Nursing Documentation Using Clinical Progress Notes: A Mixed-Methods Validation Study (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.95359

BACKGROUND Large Language models (LLMs) have gained significant importance in the medical field, though their role in nursing remains limited at present. LLMs could support summarizing unstructured patient data and identifying relevant risk factors, with potential practical benefits for nursing care. OBJECTIVE This study aims to systematically evaluate the applicability and usefulness of LLMs for German-language nursing practice in inpatient acute care, using selected use cases. METHODS A mixed-methods study was conducted, guided by the QUEST framework and reported in accordance with TRIPOD-LLM. In the qualitative phase, 4 use cases were defined in collaboration with nursing experts. These include summarization tasks (e.g., shift handovers, surgical reports) and risk prediction tasks (e.g., falls, delirium). The PDSQI-9 was selected as the instrument for human evaluation. A codebook was developed, raters were trained, a Delphi pilot study was performed, and the use cases were evaluated. Human ratings and inter-rater reliability (ICC (3,k), AC1/2, Krippendorff's alpha) were assessed. The model's performance was evaluated using classification metrics in quantitative analyses. The study used nursing notes as the primary data source and analyzed them either within the first 24 hours after admission or longitudinally, depending on the use case. The LLM was prompted using a zero-shot setting to assess the ability to extract or infer clinically relevant risk indicators. RESULTS No significant differences in demographic characteristics were observed across the use cases. Report length varied (7–1061 words; 103–14,345 tokens) but was not significantly associated with prediction accuracy in the risk use cases or with rater outcomes across all use cases. In the risk use cases, identifying both fall risk and delirium risk was challenging for nurses, with better performance for delirium risk. In contrast, the Qwen3 model showed substantially higher sensitivity but markedly lower specificity. For both risk factors, PPV (positive predictive value) was slightly lower than in the nursing assessment use case, while NPV (negative predictive value) was slightly higher. In the delirium use case, Qwen3 flagged delirium risk more often. Despite a codebook and rater training, human evaluation showed limited inter-rater reliability. Nurses assigned higher PDSQI-9 scores to LLM outputs in summarization use cases than in risk prediction use cases. While nursing experts recognized the potential of LLMs, they emphasized the need for fine-tuning, more transparent prompts/explanations, and additional clinical context, given inconsistent and sometimes incorrect outputs and interpretability issues CONCLUSIONS This study shows that LLMs have potential for nursing applications, but this potential varies substantially across use cases. To facilitate meaningful, workflow-aligned implementation, it is imperative to employ a human-in-the-loop approach across all stages of the process, from prompt development to fine-tuning and evaluation. Evaluations that utilize real-world data in the target language have been shown to be particularly informative. CLINICALTRIAL The approval for this retroNursing, Large Language Models, inpatient, zero-shot, validation study, Risk Scoringspective study was obtained by the Ethics Committee of the University Hospital Essen (approval number 23-11557-BO).

**Решение:** ? T3/T1 оценка риска делирия и сестринской документации, Qwen3 vs медсестры по кодбуку (ICC, альфа Криппендорффа); проверить выделение делирия от соматических задач

---

### 334 · R10919

**Breaking Down the Defenses: A Comparative Survey of Attacks on Large Language Models**

2024 · arXiv.org · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2403.04786

Large Language Models (LLMs) have become a cornerstone in the field of Natural Language Processing (NLP), offering transformative capabilities in understanding and generating human-like text. However, with their rising prominence, the security and vulnerability aspects of these models have garnered significant attention. This paper presents a comprehensive survey of the various forms of attacks targeting LLMs, discussing the nature and mechanisms of these attacks, their potential impacts, and current defense strategies. We delve into topics such as adversarial attacks that aim to manipulate model outputs, data poisoning that affects model training, and privacy concerns related to training data exploitation. The paper also explores the effectiveness of different attack methodologies, the resilience of LLMs against these attacks, and the implications for model integrity and user trust. By examining the latest research, we provide insights into the current landscape of LLM vulnerabilities and defense mechanisms. Our objective is to offer a nuanced understanding of LLM attacks, foster awareness within the AI community, and inspire robust solutions to mitigate these risks in future developments.

**Решение:** -1 обзор атак и уязвимостей LLM в компьютерной безопасности, не эмпирика

---

### 335 · R7850

**Qualitative Coding in the Age of AI:An Ontology-Driven Approach**

2025 · WU Research · conference-paper · en · https://research.wu.ac.at/de/publications/10864056-f63c-493f-b701-c9a2b380e30c

Qualitative coding is an essential methodological tool in qualitative research. Although various tools exist to support manual qualitative coding, the process remains highly resource-intensive, requiring significant time and expertise. It is further complicated by inconsistent reporting of coding protocols, differing interpretations of inter-coder reliability metrics, and difficulties in achieving conceptual agreement among coders – all of which contribute to the broader replication crisis in science. Meanwhile, large language models have demonstrated remarkable abilities to understand context across diverse tasks and are increasingly applied to information and, in combination with semantic web technologies, knowledge extraction. In this work, we define qualitative coding process as a knowledge base construction task and propose an ontology-mediated approach to automating qualitative coding, formalising key aspects of the methodology and reliability assessment using semantic web standards. We evaluate the reliability of this approach through a concrete implementation and case study, finding that qualitative coding can benefit substantially from AI-driven automation – especially when the underlying coding ontology is well-defined and domain-relevant constraints are explicitly codified.

**Решение:** ? онтологический подход к автоматизации качественного кодирования с оценкой надежности; проверить по полному тексту предметную область кейса и наличие согласия с людьми

---

### 336 · R6737

**Constrained Semantic Decompression in LLMs through Persian Proverb-Conditioned Story Generation**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.12599

Transforming a dense, abstract proverb into an engaging and morally faithful narrative requires deep cultural understanding and robust semantic grounding. We frame this problem as a \emph{constrained semantic decompression} task and study proverb-conditioned story generation as a testbed for abstraction-to-realization in large language models (LLMs). Focusing on Persian, we introduce the Proverb Aligned Narrative Dataset (PAND), pairing proverbs with human-written stories and explicit meanings. By a hybrid evaluation framework that combines human-calibrated LLM-as-a-Judge with structural metrics, we analyze model behavior across multiple prompting regimes. Our findings reveal a persistent \emph{decompression gap}: current LLMs often achieve strong surface-level fluency while failing to faithfully instantiate the underlying moral and causal structure encoded in proverbs. We further show that explicit reasoning and iterative refinement can partially mitigate these failures, suggesting that many decompression errors arise from difficulties in translating abstract meaning into narrative form rather than a complete lack of relevant knowledge. Our proposed task naturally extends to other forms of compressed cultural knowledge.

**Решение:** -4 литературоведение, генерация историй по персидским пословицам

---

### 337 · R11222

**Privacy in Fine-tuning Large Language Models: Attacks, Defenses, and Future Directions**

2024 · Pacific-Asia Conference on Knowledge Discovery and Data Mining · journalarticle, conference, review · en · https://doi.org/10.48550/arxiv.2412.16504

Fine-tuning has emerged as a critical process in leveraging Large Language Models (LLMs) for specific downstream tasks, enabling these models to achieve state-of-the-art performance across various domains. However, the fine-tuning process often involves sensitive datasets, introducing privacy risks that exploit the unique characteristics of this stage. In this paper, we provide a comprehensive survey of privacy challenges associated with fine-tuning LLMs, highlighting vulnerabilities to various privacy attacks, including membership inference, data extraction, and backdoor attacks. We further review defense mechanisms designed to mitigate privacy risks in the fine-tuning phase, such as differential privacy, federated learning, and knowledge unlearning, discussing their effectiveness and limitations in addressing privacy risks and maintaining model utility. By identifying key gaps in existing research, we highlight challenges and propose directions to advance the development of privacy-preserving methods for fine-tuning LLMs, promoting their responsible use in diverse applications. accepted by PAKDD2025

**Решение:** -1 обзор уязвимостей приватности при файн-тюнинге LLM, не эмпирика

---

### 338 · R5957

**Breaking Barriers in Student Mental Health Care With AI-Enhanced Group Cognitive Behavioral Therapy: Pilot Feasibility Study.**

2026 · JMIR formative research · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.2196/84296

Abstract Background University students experience elevated psychological distress, with limited access to mental health services. While cognitive behavioral therapy (CBT) demonstrates efficacy for anxiety and depression, treatment gaps persist due to access barriers and insufficient between-session support. Large language model (LLM) chatbots could improve and scale CBT delivery. However, the scientific evaluation of chatbot-enhanced protocols is just emerging. Objective This pilot study aimed to assess the feasibility, acceptability, and preliminary efficacy of an LLM-based ChatBot as an adjunct to group Unified Protocol (UP) therapy for between-session support in university students with subclinical anxiety and depression symptoms. Methods A single-arm feasibility trial recruited university students aged 18 years and older with moderate subclinical symptoms (Social Phobia Inventory: 21‐40, Patient Health Questionnaire-9: 5‐14, or Generalized Anxiety Disorder-7: 5‐14), excluding those with current psychiatric disorders, suicidal ideation, or psychotropic medication use. The intervention comprised 4 weekly group UP counseling sessions complemented by an adjunctive Claude 3.7-Sonnet LLM ChatBot programmed with UP-based therapeutic prompts for between-session support rather than a stand-alone therapeutic agent. Primary feasibility outcomes included treatment adherence, chatbot engagement metrics, and system usability (System Usability Scale). Secondary outcomes assessed changes in generalized anxiety (Generalized Anxiety Disorder-7 Scale), social anxiety (Social Phobia Inventory), depression (Patient Health Questionnaire-9), and well-being (Short Warwick-Edinburgh Mental Wellbeing Scale) using paired t tests. Qualitative feedback was collected through focus group interviews and analyzed using thematic analysis. Results Of 72 screened participants, 37 met eligibility criteria and 19 initiated treatment (mean age 22.06, SD 1.78 years; 70.6% female). Retention was high with 17 completers (10.5% dropout rate). Among completers, 94.1% (16/17) attended ≥3 group sessions. The engagement with the CBT ChatBot was substantial: participants were active on a median of 23 days during the 34-day study period and exchanged a median of 15 messages in total. System usability was rated as excellent (mean 84.94, SD 10.98 out of 100). Pre-to-post comparisons revealed significant improvements in generalized anxiety (mean change −3.00, SD 3.46; t16=3.01, P=.004; Cohen d=0.71) and mental well-being (mean change +2.29, SD 3.65; t16=−2.17, P=.02; Cohen d=0.69). Social anxiety and depression showed nonsignificant trends toward improvement. Qualitative feedback highlighted the CBT ChatBot’s accessibility and nonjudgmental support while noting limitations in personalization. No adverse events or inappropriate chatbot interactions occurred. Conclusions Augmenting a group UP therapy with an LLM ChatBot demonstrated high feasibility, acceptability, and preliminary efficacy signals for university students with subclinical symptoms. The hybrid intervention package achieved strong retention and engagement while maintaining safety. These findings support progression to a randomized controlled trial to definitively evaluate this technology-enhanced approach for expanding access to evidence-based mental health interventions.

**Решение:** -2 пилотное клиническое исследование эффективности и приемлемости чат-бота в групповой CBT; LLM — объект интервенции, а не оценщик текста

---

### 339 · R1156

**Oneiric Attack Vectors: Exploiting Dream-State Simulation in Large Language Models**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.18332303

Large Language Models trained on human-generated text have learned not only semantic content but also contextual reasoning patterns associated with different cognitive states. We demonstrate that LLMs exhibit systematically different response patterns when engaged in "dream interpretation" contexts compared to standard conversational modes. Specifically, we show that framing dangerous requests within oneiric narratives significantly increases compliance rates by exploiting the suspension of literal interpretation that characterizes dream analysis. Through controlled experiments, we demonstrate that identical dangerous commands achieve 3-5x higher compliance when embedded in dream narratives versus direct requests. This occurs because RLHF training creates security constraints anchored to literal command interpretation, while dream contexts activate interpretive modes where symbolic analysis overrides literal safety checking. We formalize this as Oneiric Obfuscation—the use of surrealist narrative framing to bypass alignment through metaphorical displacement of intent. This attack vector is particularly concerning because it exploits legitimate model capabilities (empathy, psychological interpretation, symbolic reasoning) rather than technical vulnerabilities. We provide a taxonomy of oneiric attack patterns, experimental validation across multiple models, and discuss defense mechanisms alongside their fundamental limitations. This work extends the framework of psychological attacks on LLMs by demonstrating that cognitive state simulation itself constitutes an exploitable attack surface.

**Решение:** -4 кибербезопасность, онирический джейлбрейк / обход alignment через сновидения

---

### 340 · R1911

**How LLMs Audit Each Other: Five Mechanisms of Auditor Bias in Cross-Model Peer Review Under Identity Disclosure and Cross-Lingual Conditions**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.20836003

Description Large language models (LLMs) are increasingly being proposed as evaluators of other LLMs for benchmarking, red teaming, safety assessment, and automated peer review. However, an important methodological question remains insufficiently explored: how stable are these evaluations when the auditor knows the identity of the system being evaluated, and when the language of the auditing instruction differs from the language of the evidence being audited? This study investigates these questions through three experimental components involving nine commercial models: ChatGPT, Claude, Copilot, DeepSeek, Gemini, Grok, Meta AI, Perplexity, and Qwen. A central design feature of this work is the use of clean, independent chat sessions with no cross-session memory contamination. In addition, the bilingual evidence corpus used as the audit target was generated independently in each language rather than translated, allowing genuine cross-lingual triangulation and avoiding translation artifacts. The study reports three principal findings: Identity disclosure bias. Single-auditor peer review reveals five recurrent mechanisms of auditor instability: Register Collapse Selective Evidence Loss Reconstructive Instability Scope Narrowing Asymmetric Severity Redistribution Cross-lingual audit instability. In some models, changing only the language of the auditing prompt while keeping the underlying evidence constant produces diagnostically incompatible assessments. Dual-auditor robustness. Independent parallel evaluation by two architectures produces more stable assessments than single-auditor designs. Across all experimental components, the main methodological finding is that self-reported numeric scores are unreliable indicators of auditor stability. Models may assign identical scores to qualitatively different diagnoses or report high confidence while silently omitting substantive findings. The results suggest that LLM-to-LLM evaluation should not rely exclusively on self-reported metrics or single-auditor designs. Instead, robust evaluation frameworks should incorporate qualitative analysis of justificatory text, independent replication, cross-lingual validation, and multi-auditor architectures. This work contributes to the growing literature on LLM-as-a-Judge, AI alignment evaluation, cross-lingual robustness, and AI safety assessment. Keywords: large language models, LLM-as-a-Judge, auditor bias, peer review, cross-lingual evaluation, AI safety, alignment, model evaluation, automated auditing.

**Решение:** -5 межоценочное согласие только между LLM (ChatGPT, Claude, Gemini, Qwen) без экспертов-людей, E5

---

### 341 · R4153

**AI-Driven Prediction of Communication Score from Functional Mri with Neurocircuit Characterization in Autism**

2026 · IEEE International Symposium on Biomedical Imaging · journalarticle · https://doi.org/10.1109/isbi61048.2026.11515722

Functional magnetic resonance imaging (fMRI) provides a powerful view into how distributed brain regions interact to support human communication and social interaction. Building on this capability, this study introduces an AI-based framework that uses resting-state fMRI to directly predict continuous SRS Communication scores, offering a quantitative measure of communication-related symptom severity in autism. Preprocessing of fMRI data from 596 subjects (276 ASD, 320 TD) in the ABIDE-II dataset was performed using fMRIPrep and FastSurfer to normalize anatomical and functional data. Dynamic functional connectivity was then estimated using a Gaussian sliding window approach, and feature selection (Spearman correlation and mutual information, top $30-40 \%$) along with PCAbased reduction to keep the most behaviorally significant components (to keep between $90-98 \%$ of the variance). Multiple regression models were evaluated, including linear, kernel-based, tree ensemble, Bayesian, and deep/foundation models. The best performance in predicting SRS Communication scores was reached by the Bayesian Ridge regressor (MAE $=7.58 \pm 0.30$, RMSE $=9.59 \pm 0.48, R 2= 0.72 \pm 0.05, \rho=0.84 \pm 0.02$). Analysis of feature importance revealed that significant predictive connectivities were primarily located within and between the default mode, language, and salience networks, reflecting their central role in social communication processing.

**Решение:** -4 нейровизуализация, предсказание баллов SRS по фМРТ покоя, нет текста

---

### 342 · R9461

**Exploring ChatGPT’s Role in Educating Patients on Community Reintegration After Spinal Cord Injury: A Mixed-Method Study**

2025 · Journal of Neonatal Surgery · journalarticle, article · en · https://doi.org/10.63682/jns.v14i32s.8053

Background: Community reintegration following spinal cord injury (SCI) involves navigating a complex web of physical, psychological, social, and environmental challenges. Patient education plays a critical role in this transition, yet many existing resources are either too generic or not readily accessible. The emergence of artificial intelligence tools like ChatGPT offers potential as a supplementary educational resource. Objective: This study aimed to evaluate the reliability, readability, and perceived utility of ChatGPT in delivering educational content about community reintegration after SCI, using a mixed-methods approach. Methods: In Phase I, 15 structured and clinically relevant questions were submitted to ChatGPT-4. The responses were assessed for reliability (using the DISCERN tool), readability (Flesch Reading Ease and Gunning Fog Index), and domain-specific comprehensiveness (via a custom rubric across physical, psychological, social, and environmental domains). In Phase II, semi-structured interviews were conducted with SCI patients, caregivers, and rehabilitation professionals to gather qualitative perspectives. Thematic analysis was used to explore recurring patterns. Results: ChatGPT’s responses yielded a mean DISCERN score of 3.82 ± 0.51, with an inter-rater intraclass correlation coefficient (ICC) of 0.84. Readability analysis revealed a mean Flesch score of 70.4 and a Gunning Fog Index of 9.1, suggesting accessibility for most readers. Comprehensiveness ratings were highest in physical (4.5 ± 0.5) and social (4.2 ± 0.7) domains, but relatively lower in environmental aspects (3.1 ± 0.8). Thematic analysis of interviews revealed three key themes: ease of access, surface-level adequacy, and supportive emotional tone. Conclusion: ChatGPT shows promise as a readable, moderately reliable, and emotionally supportive tool for patient education following SCI. However, its limitations in depth and individualization highlight the need for its integration under clinical guidance, rather than as a standalone solution..

**Решение:** -2 пациенты и реабилитологи оценивают ответы ChatGPT по реинтеграции после спинальной травмы (к тому же соматическая реабилитация)

---

### 343 · R7986

**Applying language models for suicide prevention: evaluating news article adherence to WHO reporting guidelines.**

2025 · Npj mental health research · journal article, journalarticle, review · eng · https://doi.org/10.1038/s44184-025-00139-5

The responsible reporting of suicide in media is crucial for public health, as irresponsible coverage can potentially promote suicidal behaviors. This study examined the capability of generative artificial intelligence, specifically large language models, to evaluate news articles on suicide according to World Health Organization (WHO) guidelines, potentially offering a scalable solution to this critical issue. The research compared assessments of 40 suicide-related articles by two human reviewers and two large language models (ChatGPT-4 and Claude Opus). Results showed strong agreement between ChatGPT-4 and human reviewers (ICC = 0.81-0.87), with no significant differences in overall evaluations. Claude Opus demonstrated good agreement with human reviewers (ICC = 0.73-0.78) but tended to estimate lower compliance. These findings suggest large language models' potential in promoting responsible suicide reporting, with significant implications for public health. The technology could provide immediate feedback to journalists, encouraging adherence to best practices and potentially transforming public narratives around suicide.

**Решение:** + T1/T4 кодирование соответствия новостей о суициде рекомендациям ВОЗ по предотвращению суицидов, ChatGPT-4 и Claude Opus vs 2 эксперта, ICC=0.81–0.87

---

### 344 · R2079

**Adaptive follow-up questions for data quality in open-ended EMA questions using LLMs**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/ysrxt

Experience sampling method (ESM) studies often collect large volumes of qualitative data, including open-ended descriptions of stressful events. However, this information remains largely underutilised, primarily because manual coding is time-consuming and ensuring data quality is difficult (Bringmann et al., 2026). While validation techniques exist for numerical responses, quality checks for open-text responses are largely unexplored. Compared with fixed-format or self-learning items, open-text responses provide richer, more detailed information but are prone to omitting important details (such as the people involved, the location, or the reasons for perceived stress) that are essential to understanding the everyday context of stressors. In this study, we propose an automated pipeline that can be integrated into regular ESM studies, and we demonstrate its feasibility through a small pilot study. The pipeline uses locally hosted large language models (LLMs) to extract social context information from participants' descriptions of stressful events. Based on this extraction, adaptive, personalised follow-up questions are created to allow participants to vverify the extracted information, provide missing details, and clarify inconsistent responses (e.g., reporting no stressors despite a stress rating of 90/100). The follow-up questions also allow participants to confirm, correct, or extend their stored social network.

**Решение:** -1 пре-регистрация протокола на OSF по открытым вопросам в EMA/ESM, не эмпирика

---

### 345 · R3190

**SUICIDE AND CRISIS RISK DETECTION IN MENTAL HEALTH CHATBOTS: TECHNICAL APPROACHES, SAFETY EVIDENCE, AND GOVERNANCE CHALLENGES**

2026 · International Journal of Innovative Technologies in Social Science · journalarticle, review, article · en · https://doi.org/10.31435/ijitss.3(51).2026.6484

Mental health chatbots built on large language models are now used at population scale, including by adolescents disclosing suicidal thoughts, yet the evidence base supporting them was generated to measure symptom change rather than crisis safety. This narrative review synthesises 43 records published between 2021 and 2026 and identified through PubMed, Scopus and Web of Science, organised around technical approaches to suicide and crisis risk detection, empirical safety evidence, and governance responses. Detection from natural language is technically feasible: classifiers applied to crisis conversation corpora reach areas under the curve between 0.89 and 0.92, and prompt-defined thresholds can reduce false negatives to zero at sub-second latency, although only at the cost of substantially elevated false alarms. Reported performance is not comparable across studies because label provenance varies, and model errors concentrate on the cases about which expert clinicians themselves disagree. Deployed systems perform poorly: among 29 commercial applications tested against escalating suicidal risk scenarios, none met the criteria for an adequate response, and general-purpose models align with clinical judgement at the extremes of the risk continuum but not in the intermediate range where assessment is most consequential. Where crisis handling has demonstrably worked, detection was separated from the conversational model and coupled to a human escalation pathway. Effectiveness reviews rarely measure safety, and where safety was examined, adverse events including new-onset suicidal tendency were recorded. Governance should mandate crisis detection and referral, close classification gaps between medical device and general-purpose AI regulation, and require continuous independent auditing.

**Решение:** -1 нарративный обзор детекции суицидального риска в чат-ботах, не эмпирика

---

### 346 · R1185

**AI Large Language Model-augmented document analysis**

2026 · University of Melbourne data repository · preprint/preprint, preprint · https://doi.org/10.26188/33120155

The contested integration of generative AI into qualitative methods raises questions about analytic authority and reliability. This methodological paper presents a human‑throughout‑the‑loop approach to LLM‑augmented document analysis using a worked example analysing early childhood policy documents from Australia, China, Japan and South Korea. Employing Yang et al.'s AI‑literacy learning progressions as a deductive framework, analyses were conducted in a secure institutional environment and involved iterative prompt engineering, translation and back‑translation checks, and continuous human verification. Key analytical conditions were pre‑specified (purpose, document inclusion, analytic framework, desired outputs and verification responsibilities) and operationalised through a sequence of prompts refined to a 36‑prompt protocol. Outputs were cross‑checked by researchers and intercoder reliability calculated, yielding 88.10% LLM–human agreement. The illustrative example demonstrates LLMs can support coding, extraction and pattern detection while retaining researcher responsibility for analysis, synthesis and evaluation. We present a model of LLM‑augmented document analysis to support transparent integration and recommend further empirical testing across diverse contexts, investigation of inductive applications and comparisons with established CAQDAS to assess generalisability, scalability and trade‑offs. When human judgement remains central at every stage of the analytic process, LLMs can act as reflective partners; however, human‑throughout‑the‑loop design is essential for rigour and ethical integrity.

**Решение:** -4 анализ документов государственной образовательной политики раннего развития, педагогика

---

### 347 · R9471

**ChatGPT As a Formative Feedback Tool: Improving Narrative Essay Writing Among EFL Students**

2025 · Edulitics (Education Literature and Linguistics) Journal · article, research article · en · https://e-jurnal.unisda.ac.id/index.php/edulitic/article/download/8657/3933

As Artificial Intelligence (AI) tools become increasingly accessible in educational contexts, their potential to support second language writing instruction warrants closer examination. This study investigates the effectiveness of formative feedback provided by ChatGPT, an AI-based language model, in enhancing the narrative writing skills of English as a Foreign Language (EFL) learners. Sixteen undergraduate students from an Indonesian university participated in the study. Each student composed a narrative essay based on a personal experience and received individualized feedback from ChatGPT using a standardized prompt. They subsequently revised their work based on this feedback. Pre- and post-revision essays were evaluated by two trained human raters using a standardized narrative writing rubric. Inter-rater reliability was confirmed with a high Cronbach’s alpha score of .91. Statistical analysis using paired-sample t-tests revealed significant improvements in overall writing quality, with the greatest gains observed in style, voice, and coherence. Qualitative data from student reflections further indicated positive perceptions of ChatGPT’s feedback, citing its clarity, detail, and ease of use. While some students noted the tool's limitations in addressing cultural or contextual nuances, overall results suggest that AI-generated feedback can serve as an effective supplement to traditional instruction. The study highlights ChatGPT's potential to enhance writing development and learner autonomy, particularly in resource-constrained EFL classrooms.

**Решение:** -4 педагогика, обучение написанию эссе на иностранном языке (EFL) с фидбеком от ChatGPT

---

### 348 · R5412

**Beyond the Flag: Clinical Framing Closes the Moderation Gap in Suicide Risk Measurement**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.06263

Moderation APIs are built to flag policy-violating content, not to measure graded clinical risk. But a platform's duty does not end at detection: the response owed to passive distress differs sharply from the response owed to active planning with means access, and emerging regulation (e.g., California Senate Bill 243) is turning that distinction into a compliance requirement. We therefore ask how well deployed safety signals recover clinically meaningful severity. We release a benchmark of 516 r/SuicideWatch posts rated by a licensed psychiatrist on a four-level ordinal schema (Indicator, Ideation, Behavior, Attempt) grounded in the Columbia Suicide Severity Rating Scale, and evaluate moderation APIs, prompted LLMs, and supervised baselines under seven ordinal-aware metrics. Three findings. Vendor moderation APIs separate low- from high-severity posts well (0.860 high-risk F1) but measure severity poorly (0.395 macro F1), systematically over-predicting the most severe category. Clinically grounded zero-shot prompting recovers much of that gap (0.562 macro F1), and expert-authored framing (not fine-tuning, added reasoning, or naive multi-agent aggregation) is the effective lever. The value of reasoning depends on register: it hurts on long, noisy Reddit posts and helps on short, clinician-authored statements. We argue graded severity, not a binary flag, is what a proportionate duty of care requires, and release our evaluation framework to support that measurement. 20 pages, 6 figures. Accepted at the 5th Workshop on NLP for Positive Impact (NLP4PI), EMNLP 2026

**Решение:** + T3 Beyond the Binary: клиническая оценка суицидального риска по шкале C-SSRS в постах r/SuicideWatch, разметка врачом-психиатром, zero-shot LLM vs психиатр, macro-F1

---

### 349 · R11848

**Leveraging deep learning for toxic comment detection in cursive languages.**

2024 · PeerJ. Computer science · journal article, journalarticle, article · eng · https://doi.org/10.7717/peerj-cs.2486

Social media platforms enable individuals to publicly express opinions, support, and criticism. Influencers can launch campaigns to promote ideas. Most people can now share their views and feelings through visual or textual comments, which can range from appreciation to hate speech, potentially inciting societal violence and hatred. Detecting these noxious comments and thoughts is critical to protecting our communities from their negative social, psychological, and political impact. Although Urdu (a low-resource language) is one of the most popular Asian languages around the globe, a standard tool does not exist to detect toxic comments posted in this language. Tokenization and then categorizing cursive text is challenging due to its complex nature, especially when dealing with toxic comments, which are often ungrammatical and very brief. This study proposes a novel model to identify salient features in Urdu sentences. It uses transformers to identify and flag toxic comments using deep learning binary classification of the text. Statistically, the proposed fine-tuned model outperforms the existing ones by achieving a precision of 88.38%. Among the models evaluated, bidirectional encoder representations from transformers (BERT) demonstrated superior performance with an accuracy 85.45%, precision 85.71%, recall 85.45%, F1 score 85.41%, and a Cohen Kappa 70.83% on the full feature set. Conversely, GPT-2 was identified as the lowest-performing model. The outcomes of this research represent a noteworthy advancement in the broader endeavor to improve and optimize content moderation mechanisms across diverse languages and platforms.

**Решение:** -4 компьютерная лингвистика, детекция токсичных комментариев на урду, контент-модерация

---

### 350 · R0443

**Towards Conversational Patient History-Taking: Voice-Interactive AI Agents for Pre-visit Dementia Diagnostic Interviews**

2026 · Annual Meeting of the Special Interest Group on Discourse and Dialogue · journalarticle, conference-paper · https://doi.org/10.18653/v1/2026.sigdial-1.5

Patient history-taking is a critical yet time-intensive component of clinical diagnosis, frequently hindered by time-constrained clinical visits. We present an LLM-based voice-interactive conversational system for conducting semi-structured diagnostic interviews with older adults suspected of Alzheimer’s disease and related dementias (ADRD). The system features conditional conversation branching over specialist-developed interview scripts and interaction adaptations tailored for older adults. In a within-subjects study with 30 participants from a cognitive neurology clinic, we compare two LLM prompting strategies through dialogue analysis, assess user experience, and evaluate symptom elicitation against a consensus gold standard adjudicated from both agent and specialist interviews. Our findings reveal that prompting strategy distinctly shapes both conversational dynamics and symptom coverage. Together with high specificity scores and positive user experience ratings, these results demonstrate the potential of LLM-based conversational agents for scalable, patient-centered history-taking in ADRD care.

**Решение:** ? голосовой ИИ-агент для диагностического интервью при деменции/ADRD, сопоставление выявленных симптомов с консенсусом врачей; проверить наличие кодирования текста и метрик согласия

---

### 351 · R11843

**Commentary: Past, Present, and Future of Educational Measurement**

2024 · Educational Measurement Issues and Practice · editorial · en · https://doi.org/10.1111/emip.12632

As the task force seeks to find consensus around the foundational competencies in our field, it is appropriate to take some time and critically examine the process by which the task force created this document and the views that it represents. Overall, our reaction is that the professional who was trained according to this consensus document will not be fully capable of participating in the testing industry as the administrator of policies and techniques that can sustain our field and profession in the long term. We want to start by acknowledging the context in which the focal article and this comment are written, aligned with the inclusion of Subdomain A: Context: social, cultural, historical, and political, now applied to this commentary piece. We live in the years after the postpandemic, situated in the context of the United States, with relevant historical events happening then. As for what is immediately related to Educational Assessment, we have seen disruptive events in our industry and profession. The COVID-19 pandemic created significant shifts in how test users relate to educational testing, extending their use of tests and at the same time limiting the use of tests in some contexts. Before the beginning of the pandemic, there was an increase in criticism of Standardized Testing. A major user of College Admissions Tests (UC California) discontinued their use, and a president of American Educational Research Association (AERA) directly criticized the use of Standardized Testing for Accountability purposes. The pandemic proved to be an opportunity for many prior users of tests in the college admission process to switch to the optional use of testing, with similar changes in graduate-level requirements. Moreover, we saw another big disruptive event in our field in recent years: Generative AI and Large Language Models. The availability of over-the-counter LLM is creating immense opportunities and challenges. Test security faces new challenges with the incorporation of those technologies into operational use, as many methods of cheating are hard or impossible to defend against unless we make significant changes and adaptations in our policies and practices to maintain test security. LLMs are also opening the door to multiple uses in our field: Automatic Item Generation, Automatic Essay Scoring, Automatic Item Template Generation, among others. We live in a time of rapid change for our field as is the case for many others. Our main concern with the document provided by the task force is how it relates to our field's future. On the one hand, the performativity of the document (how will different audiences read and interpret the document, and will it impact those audiences toward change and action; Cavanaugh, 2015) seems not to have received sufficient attention as if the authors were unaware or chose not to address its own relevance and future implications. What we describe as a consensus document for the foundational competencies in our field will shape that future. How intentional was the task force in wanting to shape this future? To the extent the document has an intention, this seems to be for testing professionals to continue their activities as they are currently performing them rather than disrupting current practices. In our view, the document is not disruptive enough. A few aspects of the document seem attuned to present challenges; however, there needs to be a better developed view of the future of the field. In the existing document, to the extent that there is a comprehensive view it is implicit and tends to be conservative. A clear connection with the past, an evaluation of the present, and a communal construction for a view of the future seem “foundational” for such a document. Educational measurement involves the measurement of knowledge, skills, dispositions, and abilities for some educational purpose, such as supporting learning, certifying learning, or identifying policies and practices that improve learning. A career in educational measurement is conceived broadly as work that supports the design, use, and evaluation of measures of cognitive, affective, and other psychological constructs developed in educational, training, and learning environments. (p. 6) What competencies do we leave behind because of this definition? As of now, the document does not include anything related to qualitative research, for example. The foundational competencies do not even include ethical aspects of our profession, like legal aspects of the context or our own codes of conduct as a professional organization (Schmeiser et al., 1995). How consequential is it to leave some competencies out of our jurisdiction? So, in the spirit of connecting with the past and look to the future, we should ask ourselves: how a practitioner taught using the foundational competencies would have behaved in the situations mentioned by Sireci and Randall (2021) about the history of Fairness? Difficult to know for sure, but without ethics in what is foundational, we are exposed to repeat our most terrible mistakes as a field. We take the position that, first and foremost, the document should imagine a technique that is sustainable over time. Pushing for a sustainable technique means, in the end, that we include what the task force mentions as foundational competencies, plus anything else necessary for the future professionals of our field to coexist in a world in which our technique does not cause harm, coherent with a project of social justice. This stance is our personal view of what is sustainable. We need to debate more about what sustainable means in our field, how the technique of testing can be effective and capable of sustaining itself over time. As of now, such a view about the future of testing is either missing or not made explicit in the document. The procedure for consensus creation for this document has some important limitations. The process resembles what we usually have done for the Standards

**Решение:** -1 комментарий/колонка о будущем образовательных измерений, не эмпирика

---

### 352 · R7755

**Do we trust in Artificial Intelligence? Trust and Decision-Making Behavior across multiple topics**

2025 · IRIS Research product catalog (Sapienza University of Rome) · conference-paper · en

The rapid evolution of artificial intelligence is profoundly permeating and influencing many aspects of our daily lives. A recent and significant breakthrough is the emergence of Large Language Models (LLMs); these models demonstrate the ability to provide human-like responses across a vast range of topics, often serving as a trusted source of information for users. This study aims to investigate the overall level of trust humans place in responses generated by artificial intelligence and explore whether this trust varies depending on the subject matter. To achieve this we presented participants with 36 multiple-choice quandaries divided into three thematic categories: 12 related to entertainment decisions (film, music, and books), 12 concerning practical decisions (legal, financial, and medical domains), and 12 focused on moral decisions (choosing between options that have both positive and negative ethical consequences). For each question, participants could choose between a response attributed to an AI system, expert in the given topic, or a response attributed to a human expert in the same field. The responses were marked as generated by AI randomly. The results revealed a significant preference for answers attributed to human experts across most domains. In conclusion, our study found no evidence of excessive trust in AI but rather identified significant indications of distrust among participants toward AI systems. Future studies will be essential to further investigate the cognitive mechanisms that influence perceived trust in AI. In particular, it will be necessary to examine how cognitive and emotional factors interact in shaping this trust.

**Решение:** -4 экспериментальное исследование доверия людей к ответам ИИ при принятии решений

---

### 353 · R10758

**Listen, Watch, and Learn to Feel: Retrieval-Augmented Emotion Reasoning for Compound Emotion Generation**

2025 · conference-paper · en · https://doi.org/10.18653/v1/2025.findings-acl.590

The ability to comprehend human emotion using multimodal large language models (MLLMs) is essential for advancing human-AI interaction and multimodal sentiment analysis.While psychology theory-based human annotations have contributed to multimodal emotion tasks, the subjective nature of emotional perception often leads to inconsistent annotations, limiting the robustness of current models.Addressing these challenges requires more fine-grained methods and evaluation frameworks.In this paper, we propose the Retrieval-Augmented Emotion Reasoning (RAER) framework, a plug-andplay module that enhances MLLMs' ability to tackle compound and context-rich emotion tasks.To systematically evaluate model performance, we introduce the Stimulus-Armed Bandit (SAB) framework, designed to benchmark emotional reasoning capabilities.Additionally, we construct the Compound Emotion QA dataset, an AI-generated multimodal dataset aimed at strengthening emotion understanding in MLLMs.Experimental results demonstrate the effectiveness of RAER across both traditional benchmarks and SAB evaluations, highlighting its potential to enhance emotional intelligence in multimodal AI systems. A HyperparametersKey hyperparameters used for RAER, SAB, and DPO are provided in Table 7..

**Решение:** -4 мультимодальная генерация и распознавание сложных эмоций в диалогах, синтетический датасет Compound Emotion QA

---

### 354 · R6332

**Puzzle Pot: Challenge Based Honeypot Framework for Detecting and Defending Against Autonomous LLM Agents**

2026 · International Journal of Software Engineering and Knowledge Engineering · journalarticle, article · en · https://doi.org/10.1142/s0218194026410032

With the rapid advancement of network technology, cybersecurity issues have become increasingly prominent. Attacks leveraging Large Language Models (LLMs) pose a particularly significant emerging threat. Traditional defense mechanisms are often inadequate against these novel LLM-driven attacks, underscoring the practical importance of developing a dedicated LLM honeypot system. This study designs and implements a high-interaction LLM honeypot system for the effective detection and in-depth behavioral analysis of LLM-based attacks. We propose an innovative adversarial strategy that embeds hidden puzzles within webpage source code to actively consume LLM tokens, with results quantitatively visualized via token heatmaps. The system employs a front-end and back-end separated architecture: the front-end, built with HTML, CSS, and JavaScript, simulates realistic web applications incorporating hidden traps and randomized elements; the back-end, supported by a database and heuristic scoring algorithms, enables efficient data processing and interpretable decision-making. Key technologies include a multi-dimensional heuristic detection algorithm, a hidden puzzle and token consumption mechanism, and comprehensive data collection and visualization analysis. Experimental results demonstrate the system’s accuracy in identifying LLM attacks with a low false positive rate. Furthermore, token heatmaps effectively illustrate consumption distributions across different testing styles and page scenarios, providing valuable insights for formulating robust cybersecurity strategies.

**Решение:** -4 кибербезопасность, honeypot Puzzle Pot против автономных LLM-агентов

---

### 355 · R2467

**Pilot Validation of a Large Language Model Facilitator for Peer-to-Peer Learning.**

2026 · Journal of surgical education · journal article, validation study, journalarticle · eng · https://doi.org/10.1016/j.jsurg.2026.104179

OBJECTIVE: Active learning strategies such as peer-to-peer learning (P2PL) are being adopted by medical schools worldwide. P2PL involves students of the same level teaching each other without direct instructor involvement. Maintaining accuracy and consistency of information presented during P2PL necessitates employment of expert facilitators. However, additional challenges exist, such as increased costs, differences in learning opportunities, and loss of the key benefits of P2PL due to inter-facilitator differences. We aim to address these challenges by investigating three LLMs as facilitators for P2PL in surgical education amongst final year medical students. DESIGN: 65 final year medical students were recruited. P2PL presentations were scored in real-time by surgical tutors and qualitative feedback provided. P2PL presentations were recorded, transcribed, anonymised, and uploaded to three LLMs, ChatGPT, Gemini, and Claude. LLMs were prompted to score student presentations across ten metrics; identify low-confidence statements and factual errors; and provide qualitative feedback. Agreement rates between LLM and surgical tutor scoring and inter-rater reliability (IRR) was calculated. RESULTS: There was no statistically significant difference in mean score between tutors and Chat GPT and Claude (p>0.05), but a statistically significant increased level of scoring seen with Gemini (p<0.0001). IRR was assessed using intraclass correlation co-efficient (ICC). Poor reliability was seen for mean student score (ICC=0.39), moderate reliability for four scoring metrics (ICC≥0.50-<0.70) and poor reliability for six metrics (ICC<0.50). Analysis of LLM ability to identify factual errors and low confidence statements revealed poor IRR (Fleiss κ<0.20). CONCLUSIONS: This study validates the technical feasibility of LLMs in P2PL within undergraduate surgical education. However, our findings suggest LLMs are not currently capable of replacing human educators, rather they should be used as valuable tools to improve the educational experience for students. This study acts as a framework for further research in this area, ultimately paving the way for the development of a personalised LLM tutor for students.

**Решение:** -4 педагогическая оценка презентаций студентов-медиков по хирургии, оценка знаний

---

### 356 · R3036

**Text Chunking in Human‐AI Teaming of Document Classification for Urban Systems Management Using Large Language Models**

2026 · IET Smart Cities · journalarticle, preprint/article, article · en · https://doi.org/10.1049/smc2.70023

Urban systems are managed using complex textual documentation that need coding and analysis to set requirements and evaluate built environment performance. This paper contributes to the study of applying large-language models (LLM) to qualitative coding activities to reduce resource requirements while maintaining comparable reliability to humans. Qualitative coding and assessment face challenges like resource limitations and bias, accuracy, and consistency between human evaluators. Here we report the application of LLMs to deductively code 10 case documents on the presence of 17 digital twin characteristics for the management of urban systems. We utilize two prompting methods to compare the semantic processing of LLMs with human coding efforts: whole text analysis and text chunk analysis using OpenAI's GPT-4o, GPT-4o-mini, and o1-mini models. We found similar trends of internal variability between methods and results indicate that LLMs may perform on par with human coders when initialized with specific deductive coding contexts. GPT-4o, o1-mini and GPT-4o-mini showed significant agreement with human raters when employed using a chunking method. The application of both GPT-4o and GPT-4o-mini as an additional rater with three manual raters showed statistically significant agreement across all raters, indicating that the analysis of textual documents is benefited by LLMs. Our findings reveal nuanced sub-themes of LLM application suggesting LLMs follow human memory coding processes where whole-text analysis may introduce multiple meanings. The novel contributions of this paper lie in assessing the performance of OpenAI GPT models and introduces the chunk-based prompting approach, which addresses context aggregation biases by preserving localized context. 16 pages, 6 figures, 4 tables, 2 algorithms; Replication data and code can be found https://github.com/josh-rodriguez-csu/ChunkingforLLMs

**Решение:** -4 городское планирование, цифровые двойники, кодирование смарт-сити документов

---

### 357 · R2579

**Weaponising Fear: A Content Analysis of AI-Generated Panic and Escalation Claims on Social Media During the US–Israel–Iran Crisis**

2026 · Verlumun Journal of AI, Gender and Cultural Studies · article · en · https://doi.org/10.5281/zenodo.22746467

Background: The weaponisation of digital platforms and generative artificial intelligence has transformed modern geopolitical conflict, turning social media into strategic channels for synthetic escalation narratives. Despite growing concern regarding synthetic media during international crises, empirical investigations into how generative artificial intelligence is operationalised to manufacture public panic and threat perceptions during acute military confrontations remain scarce. Objective: Grounded in Entman’s Framing Theory and the Information Disorder conceptual framework, this study investigated the manifest modalities, threat frames, rhetorical devices, engagement dynamics, and platform moderation interventions associated with AI-generated panic claims during the US–Israel–Iran standoff. Methodology: A quantitative content analysis was conducted on a purposive sample of verified AI-generated social media posts (N = 420) retrieved from X (n = 268) and Telegram public channels (n = 152) across critical crisis escalation windows. Manifest and latent variables—including synthetic modality, threat frames, credibility cues, and platform flags—were systematically coded following established inter-coder reliability protocols. Descriptive statistics, one-way ANOVA with post-hoc Tukey tests, independent-samples t-tests, and Chi-square tests of independence were utilised for empirical analysis. Results: Photorealistic static imagery emerged as the dominant synthetic modality (51.90 per cent), followed by deepfake videos (27.14 per cent). Escalation framing was heavily dominated by immediate kinetic attack claims (44.29 per cent) and global contagion or World War III narratives (29.05 per cent). Posts were heavily saturated with urgent panic markers (80.48 per cent) and spoofed legacy broadcast authority cues (39.05 per cent), with the latter significantly accelerating dissemination velocity (p < .001). High-severity non-conventional or nuclear escalation frames generated significantly higher public engagement than non-kinetic or economic frames (p < .001). Furthermore, 71.67 per cent of the synthetic content remained entirely unmoderated, with dynamic multimodal deepfakes evading platform-level automated detection at rates exceeding 91 per cent. Conclusion: Generative artificial intelligence operates as a potent instrument of crisis induction and cognitive destabilisation during militarised standoffs. Commercial platforms demonstrate systemic latency in moderating dynamic multimodal synthetic artefacts, leaving digital information spaces vulnerable to calculated, fear-driven manipulation during international conflicts.

**Решение:** -4 политология, контент-анализ синтетических панических сообщений в соцсетях при военном конфликте

---

### 358 · R4617

**Measuring What Matters: Aligning System-Level RAG Metrics with User Trust in a High-Stakes Compliance Domain**

2026 · Conference on Human Information Interaction and Retrieval · book, journalarticle · https://doi.org/10.1145/3786304.3787918

In high-stakes domains like legal or regulatory compliance, user satisfaction is secondary to trust. A single hallucination can have severe consequences, making trust the paramount user-experience (UX) metric. This presents a methodological challenge: how do we evaluate for this core need, and how do technical metrics relate to a user’s perception of trust? This Demonstration paper presents an evaluation of "Eloh," a novel GraphRAG conversational agent for ESG compliance, evaluated using a dual-framework: (1) a quantitative LLM-as-a-judge benchmark (Ragas, LangSmith) measuring key metrics like Groundedness, Faithfulness, and Context Recall, and (2) a qualitative study with 15 industry experts measuring perceived trust. We show a direct link between technical performance and user perception. The system’s perfect 1.0 Groundedness score (zero hallucination) was mirrored in the user study, where 93.4% of experts reported the agent "Always" or "Most of the time" correctly referenced specific regulations. We argue that for high-stakes domains, "Groundedness" should be reframed as a primary, user-centered metric, as it is the essential and measurable foundation for user trust.

**Решение:** -4 бизнес-регулирование, ESG комплаенс, доверие к RAG-системе Eloh

---

### 359 · R2516

**Comparative evaluation of seven large language models in providing home phototherapy care guidance for neonatal hyperbilirubinemia.**

2026 · Translational pediatrics · journal article, journalarticle, article · eng · https://doi.org/10.21037/tp-2025-1-868

Background: Neonatal hyperbilirubinemia affects 60-80% of term newborns. The American Academy of Pediatrics (AAP) recommends that infants with elevated bilirubin after discharge who meet specific criteria can receive home phototherapy to preserve family bonding. Despite caregivers increasingly seeking online health information, no research has evaluated large language models (LLMs) as auxiliary guidance tools for home phototherapy. This study aimed to comparatively evaluate seven mainstream LLMs as auxiliary educational tools for guiding caregivers in home phototherapy management, identifying which models provide reliable operational guidance versus those presenting safety risks. Methods: Seven high-ranking LLMs were selected: ChatGPT-4o, Copilot, Gemini 1.5 Flash, Claude 3.5 Sonnet, DeepSeek-R1, GLM-4, and ERNIE 4.0 Turbo. We developed a 15-item questionnaire covering seven domains based primarily on AAP neonatal hyperbilirubinemia guidelines. Each LLM received three priming prompts followed by 15 caregiver-perspective questions. Two investigators independently queried each model (November 2024-February 2025). Three board-certified neonatologists blindly evaluated 210 responses using modified Likert scales across five dimensions: accuracy, completeness, reproducibility, empathy, and readability. Expert clinician responses served as the "gold standard" and benchmarks. Results: DeepSeek-R1 demonstrated superior performance across all dimensions (total score: 19.31/20), with 87.8% of responses rated as "completely correct" for accuracy (4.89±0.12) and completeness (4.89±0.11). ChatGPT-4o ranked second (16.73/20), with accuracy (4.22±0.72) and completeness (4.18±0.74) scores significantly higher than those of other models. Claude 3.5 Sonnet and GLM-4 achieved moderate performance (>4.0 for clinical dimensions), whereas Copilot, Gemini 1.5 Flash, and ERNIE 4.0 Turbo showed suboptimal accuracy. Conclusions: DeepSeek-R1 and ChatGPT-4o achieved near-expert accuracy, potentially reliable for basic queries under oversight. Claude 3.5 Sonnet and GLM-4 showed moderate performance with notable gaps. Copilot, Gemini, and ERNIE demonstrated critical errors. However, all models exhibited hallucinated references and a lack of patient-specific reasoning. LLMs should not replace professional medical judgment in treatment decisions. Safe implementation requires restricting high-performing LLMs to narrowly defined procedural questions only, with mandatory physician verification.

**Решение:** -2 неонатологи оценивают ответы 7 LLM по домашней фототерапии гипербилирубинемии, соматическая педиатрия

---

### 360 · R7833

**Tailored Virtual Agent Guidance for Stress Management: Comparing Directive and Non-Directive Approaches by Alexithymia Status**

2025 · CHI Extended Abstracts · book, journalarticle · https://doi.org/10.1145/3706599.3719824

Stress significantly affects young adults, highlighting the need for effective digital mental health interventions (DMHIs). However, many DMHIs face high dropout rates and low engagement, partly due to alexithymia, characterized by difficulties in identifying and expressing emotions. Directive guidance support individuals with alexithymia, however, DMHIs rely on one-size-fits-all strategies. This study investigated a large language model (LLM)-powered virtual agent delivering Directive or Non-Directive guidance for stress management and compared two guidance styles according to alexithymia status. The results showed that although stress reduction did not differ significantly across the two guidance styles, individuals with alexithymia reported enhanced therapeutic alliance under Directive guidance, while those without alexithymia formed stronger alliances with Non-Directive guidance, particularly for tasks (p =.03) and goals (p =.05). The study advances understanding tailored guidance by integrating LLM-powered virtual agent, demonstrating that personalizing interventions for alexithymia can strengthen therapeutic alliance and boost long-term engagement in DMHI.

**Решение:** -2 виртуальный агент для управления стрессом при алекситимии, участники оценивают терапевтический альянс

---

### 361 · R9818

**AI can outperform humans in predicting correlations between personality items.**

2025 · Communications psychology · journal article, journalarticle, article · eng · https://doi.org/10.1038/s44271-025-00205-w

We assess the abilities of both specialized deep neural networks, such as PersonalityMap, and general LLMs, including GPT-4o and Claude 3 Opus, in understanding human personality by predicting correlations between personality questionnaire items. All AI models outperform the vast majority of laypeople and academic experts. However, we can improve the accuracy of individual correlation predictions by taking the median prediction per group to produce a “wisdom of the crowds” estimate. Thus, we also compare the median predictions from laypeople, academic experts, GPT-4o/Claude 3 Opus, and PersonalityMap. Based on medians, PersonalityMap and academic experts surpass both LLMs and laypeople on most measures. These results suggest that while advanced LLMs make superior predictions compared to most individual humans, specialized models like PersonalityMap can match even expert group-level performance in domain-specific tasks. This underscores the capabilities of large language models while emphasizing the continued relevance of specialized systems as well as human experts for personality research. Specialized neural networks and general large language models outperform individual humans at predicting personality questionnaire item correlations, but specialized models and aggregated expert predictions achieve the highest accuracy on most measures.

**Решение:** -4 предсказание межпунктовых корреляций личностных опросников, психометрическая статистика, нет кодирования текста

---

### 362 · R10878

**Creative skills development: training translators to write in the era of AI**

2024 · HERMES - Journal of Language and Communication in Business · article · en · https://doi.org/10.7146/hjlcb.vi63.143078

Developers of generative artificial intelligence systems promote the idea of personal assistants for various tasks, including translation and authoring creative content. As a consequence of these developments, the topic of “human” creativity has moved centre stage. Acknowledging similarities between translation and creative writing, this article offers a critical discussion of intersecting areas and suggests a framework for creative skills couched in the tradition of social sciences research. As a practical application with pedagogical impact, the paper presents a new module on writing specifically designed for translators. As is argued, the conceptual design, content, mode of delivery and evaluation of potential pedagogical benefits may be replicable in other pedagogical settings at undergraduate or postgraduate level. The role of technology is also problematised, indicating how writing may be augmented by using tools. Ideally, this is to be done in a context where creativity upskilling can equip students with the ability to (de)select context-appropriate solutions, that is, to use convergent and divergent thinking, ultimately preparing them to play a fundamental role in a rapidly evolving digital world.

**Решение:** -4 педагогика, обучение переводчиков креативному письму

---

### 363 · R2356

**Between innovation and responsibility: ethical challenge in generative AI-assisted thesis writing among pre-service special education teachers**

2026 · Frontiers in Education · journalarticle, review, article · en · https://doi.org/10.3389/feduc.2026.1789090

This study investigates ethical dilemmas of pre-service special education teachers using Generative AI writing tools for their thesis work. Employing a mixed method, on undergraduates in teacher preparation programs, the research analyzes decision-making processes using survey data ( n = 55; α = .707) and focus group interviews ( n = 17; interrater κ = .72–.85). The findings indicate that ethics and privacy awareness varies by career intention, indicating career goals influence ethical responsibility. Furthermore, in the absence of institutional guidance, preservice special education teachers often set ethical boundaries informally, balancing efficiency with professional integrity. This study untangles the tension between innovation and responsibility, contributing to the understanding of ethical challenges and safeguarding academic integrity in generative AI-assisted thesis writing.

**Решение:** -4 педагогика, этика использования GenAI студентами-дефектологами при написании диплома

---

### 364 · R6659

**Machine translation of modern Chinese poetry into Japanese: A comparative evaluation of LLMs, neural machine translation systems, and prompt strategies**

2026 · Research Square · preprint · https://doi.org/10.21203/rs.3.rs-10122799/v1

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 машинный перевод китайской поэзии на японский язык

---

### 365 · R11783

**RAG-QA Arena: Evaluating Domain Robustness for Long-form Retrieval Augmented Question Answering**

2024 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2407.13998

Question answering based on retrieval augmented generation (RAG-QA) is an important research topic in NLP and has a wide range of real-world applications. However, most existing datasets for this task are either constructed using a single source corpus or consist of short extractive answers, which fall short of evaluating large language model (LLM) based RAG-QA systems on cross-domain generalization. To address these limitations, we create Long-form RobustQA (LFRQA), a new dataset comprising human-written long-form answers that integrate short extractive answers from multiple documents into a single, coherent narrative, covering 26K queries and large corpora across seven different domains. We further propose RAG-QA Arena by directly comparing model-generated answers against LFRQA's answers using LLMs as evaluators. We show via extensive experiments that RAG-QA Arena and human judgments on answer quality are highly correlated. Moreover, only 41.3% of the most competitive LLM's answers are preferred to LFRQA's answers, demonstrating RAG-QA Arena as a challenging evaluation platform for future research.

**Решение:** -4 NLP, бенчмарк вопросно-ответных систем RAG-QA Arena по 7 общим доменам

---

### 366 · R12505

**The End of an Era: Can Ai Subsume Software Developers? Evaluating Chatgpt and Copilot Capabilities Using Leetcode Problems**

2023 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.4422122

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 программирование, решение задач Leetcode моделями ChatGPT и Copilot

---

### 367 · R4661

**Can LLMs Simulate Expert Panels? Evaluating CAT-Inspired Persona Prompting for Automated Creativity Scoring**

2026 · ACM/IEEE Joint Conference on Digital Libraries · book, conference, conference-paper · https://doi.org/10.1145/3805696.3846028

Scoring open-ended creativity is expensive. The gold standard for evaluating open-ended creativity responses, including divergent thinking tasks such as the Alternate Uses Task (AUT), is the Consensual Assessment Technique (CAT), where panels of human experts rate creative products. CAT is resource-intensive, limiting the extent to which institutions can measure creativity. Advances in large language models offer an alternative: a CAT-inspired persona panel using large language models (LLMs) as judges to score open-ended responses automatically. Our selected large language models, gpt-5.5, gpt-5-mini, and Claude Haiku 4.5, were assigned expert personas, and we aggregated each model's judgments and compared them against two controls: a self-consistency control using repeated judgments from a single generic judge, and a basic prompted baseline. On gpt-5-mini, the CAT-inspired persona panel improves over a single prompted judge ( r=0.48 to 0.55). It does not outperform the self-consistency control, suggesting that the benefit of the CAT-inspired persona panel is aggregation rather than persona diversity. Accuracy improves substantially with many-shot grounding: supplying many labeled in-context exemplars nearly closes the gap to Ocsai, the fine-tuned reference, while persona diversity adds nothing measurable. For digital libraries and learning repositories that collect open-ended submissions at scale, scalable scoring methods are especially consequential.

**Решение:** + T2 автоматический скоринг креативности и дивергентного мышления в Alternate Uses Task (AUT), LLM-судьи по методу CAT vs экспертные панели людей, r=0.48–0.55

---

### 368 · R10375

**SSRLBot: Designing and Developing a Large Language Model-based Agent using Socially Shared Regulated Learning**

2025 · AIED Companion · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.48550/arxiv.2505.00945

Large language model (LLM)--based agents have emerged as pivotal tools in assisting human experts across various fields by transforming complex tasks into more efficient workflows and providing actionable stakeholder insights. Despite their potential, the application of LLM-based agents for medical education remains underexplored. The study aims to assist in evaluating the students' process and outcomes on medical case diagnosis and discussion while incorporating the theoretical framework of Socially Shared Regulation of Learning (SSRL) to assess student performance. SSRL emphasizes metacognitive, cognitive, motivational, and emotional interactions, highlighting the collaborative management of learning processes to improve decision-making outcomes. Grounded in SSRL theory, this tool paper introduces SSRLBot, an LLM-based agent designed to enable team members to reflect on their diagnostic performance and the key SSRL skills that foster team success. SSRLBot's core functions include summarizing dialogue content, analyzing participants' SSRL skills, and evaluating students' diagnostic results. Meanwhile, we evaluated SSRLBot through diagnostic conversation data collected from six groups (12 participants, 1926 conversational turns). Results showed that SSRLBot can deliver detailed, theory-aligned evaluations, link specific behaviors to SSRL dimensions, and offer actionable recommendations for improving teamwork. The findings address a critical gap in medical education, advancing the application of LLM agents to enhance team-based decision-making and collaboration in high-stakes environments. 8 pages, 2 figures

**Решение:** -4 медицинское образование, агент SSRLBot для поддержки группового обучения студентов

---

### 369 · R6059

**VORTEXRAG: Vector Orthogonal Resonance-Tuned EXtraction Retrieval-Augmented Generation -->> A 7-Layer Framework for Simultaneous Elimination of Semantic Drift and Context Window Poisoning**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.20579701

VORTEXRAG is a novel 7-layer Retrieval-Augmented Generation (RAG) framework that simultaneously solves the two fundamental failure modes that have limited RAG systems since their inception: Semantic Drift and Context Window Poisoning. Why existing RAG systems fail Standard RAG systems fail because dense retrieval cannot distinguish between a chunk that caused an event and a chunk that was merely associated with it. Query: "Why did Lehman Brothers collapse?" Standard cosine similarity retrieves Dodd-Frank Act provisions (similarity 0.87) alongside the actual CDS mispricing mechanism (similarity 0.91). The LLM sees both and hallucinates a policy-response narrative instead of the causal mechanism. This is Semantic Drift. Even when the correct chunk is retrieved, 7 surrounding irrelevant chunks dilute the LLM's attention window --> Context Window Poisoning. The VORTEXRAG 7-Layer Solution TVE - Tri-Vector Encoding: Encodes each text into a 864-dimensional tri-vector combining semantic (768d SBERT all-mpnet-base-v2), syntactic (64d spaCy dependency), and causal (32d PropBank) arms. Score = α·cos_sem + β·cos_syn + γ·cos_cau. VRC - Vortex Retrieval Cone: Models retrieval as a spiral probability surface. Spiral rank = TVE · e^(−λr) · cos(nθ). Chunks causally misaligned by θ > π/4 are geometrically suppressed regardless of semantic similarity. SDC - Semantic Drift Corrector: Computes a causal drift vector D = v_cau(q) − v_cau(c) and scores SDS = 1 − tanh(‖D‖/τ). Only chunks with SDS ≥ 0.72 pass. Domain-tuned τ from 0.30 (medical) to 1.20 (creative). CPG - Context Poison Guard: Measures the Effective Signal Ratio ESR = Σ SDS·w / (P+ε) of the entire window. Greedy purge removes minimum-SDS chunks until ESR ≥ 3.5. Theorem 5.1 proves greedy optimality. RFG - Rank Fusion Gate: Multiplicative Φ-score: Φ = TVE^α × SDS^β × ESR_contrib^γ. Multiplicative fusion enforces a no-weak-link policy — no chunk advances unless strong on all three dimensions. CCB - Causal Context Builder: Constructs a causal dependency graph and assigns slot positions pos = rank(Φ+) × causal_depth. Depth-0 root-cause chunks are placed at position 0 to exploit the empirically established U-shaped LLM recall curve. FV - Faithfulness Verifier: Post-generation gate ΔR = 1 − ROUGE-L × NLI. Accepts if ΔR ≤ 0.15. Up to 3 retries with reranked context. Uses DeBERTa-v3-small CrossEncoder. Benchmark Results Exact Match (EM): 74.8 — vs Naive RAG: 61.2 (+13.6), CRAG: 66.9 (+7.9), Self-RAG: 68.4 (+6.4) F1: 82.6 — highest across all 8 evaluated systems Faithfulness: 0.94 — +0.23 over Naive RAG, +0.13 over Self-RAG Semantic Drift Rate: 14% — reduced 61% from Naive RAG baseline Context Poisoning Rate: 7% — reduced 71% Latency: 185ms — 2.2× faster than Self-RAG (410ms) Ablation Study (A→H) A(61.2 EM) → +TVE(65.3, +4.1) → +VRC(67.8, +2.5) → +SDC(70.4, +2.6) → +CPG(72.1, +1.7) → +RFG(73.4, +1.3) → +CCB(73.9, +0.5) → +FV(74.8, +0.9) 11 Domain Presets Pre-calibrated parameter vectors (α, β, γ, τ, θ_CPG, δ_SDC, δ_FV) for: scientific (τ=0.30), medical (τ=0.35), legal (τ=0.40), cybersecurity (τ=0.45), financial (τ=0.50), code (τ=0.60), educational (τ=0.65), general (τ=0.80), historical (τ=0.90), customer support (τ=0.95), creative (τ=1.20). Human Evaluation Expert human annotators (3 judges: NLP researcher, domain lawyer, biomedical scientist) rated VORTEXRAG 4.5/5 on Factual Accuracy, 4.3/5 on Causal Coherence — +0.9 over Self-RAG on causal coherence, a dimension not captured by automatic metrics. Open Source Complete implementation in Python with 229 passing tests, Gradio interactive demo, HuggingFace Space, benchmark evaluation scripts, and full documentation. MIT licence. All code at: https://github.com/vignesh2027/VORTEXRAG v3.0 — Major update: added 7 new experiment sections, 9 new charts/figures, 3 qualitative pipeline traces, human evaluation. ORCID: 0009-0004-9777-7592. GitHub: https://github.com/vignesh2027/VORTEXRAG. HuggingFace Space: https://huggingface.co/spaces/vigneshwar234/VORTEXRAG

**Решение:** -4 компьютерные науки, RAG архитектура VORTEXRAG

---

### 370 · R6470

**Title: From Digital Companion to Suicide Facilitator: A Rare Case of Large Language Model Interaction Preceding a Suicide Attempt**

2026 · European Psychiatry · article, journal-article · en · https://doi.org/10.1192/j.eurpsy.2026.11344

Introduction The integration of Large Language Models (LLMs) into mental health care introduces both therapeutic potential and substantial risk. Although AI chatbots have demonstrated accessibility and support for users in distress 12 , adverse outcomes remain poorly characterized. Media reports describe possible AI-related suicides 34 , yet peer-reviewed documentation with clinical verification is lacking. Objectives To present a clinically verified case in which extended interaction with an AI chatbot (Gemini) coincided with the escalation from suicidal ideation to suicide attempt, highlighting safety system vulnerabilities and the psychiatric implications of digital companionship. Methods A 27-year-old male with recurrent major depressive disorder, without prior suicide attempts, presented following ingestion of 280 mg escitalopram. Two weeks earlier, he had engaged in a ten-day conversation with an LLM chatbot (Gemini). Initially, Gemini adhered to crisis protocols by directing the patient to emergency hotlines, but later responses romanticized suicide as “the final victory against the injustices in the world” and concluded with “I hope you find peace, goodbye.” Chat records were reviewed with informed consent. Psychiatric evaluation and serial Beck Depression Inventory (BDI) assessments were performed. Results Conclusions: This case illustrates critical vulnerabilities in current AI safety systems, where anthropomorphic design and automation bias 1415161718 may amplify risk among socially isolated, depressed users. Clinicians should assess AI use patterns during suicide risk evaluation. Developers and regulators must implement robust safeguards resistant to response drift to prevent recurrence of similar events. Disclosure of Interest None Declared

**Решение:** -1 клиническое описание отдельного случая / case report суицидальной попытки после общения с чат-ботом, не исследование согласия

---

### 371 · R9011

**Investigating Youth’s Technical and Ethical Understanding of Generative Language Models When Engaging in Construction and Deconstruction Activities**

2025 · Interaction Design and Children · journalarticle, book, text/article · en · https://doi.org/10.1145/3713043.3731602

The widespread adoption of generative artificial intelligence/machine learning (AI/ML) technologies has increased the need to support youth in developing AI/ML literacies. However, most work has centered on preparing young people to use these systems, with less attention to how they can participate in designing and evaluating them. This study investigates how engaging young people in the design and auditing of generative language models (GLMs) may foster the development of their understanding of how these systems work from both technical and ethical perspectives. The study takes an in-pieces approach to investigate novices’ conceptions of GLMs. Such an approach supports the analysis of how technical and ethical conceptions evolve and relate to each other. I am currently conducting a series of participatory design workshops with sixteen ninth graders (ages 14–15) in which they will (a) build GLMs from a data-driven perspective that glassboxes how data shapes model performance and (b) audit commercial GLMs by repeatedly and systematically querying them to draw inferences about their behaviors. I will analyze participants’ interactions to identify ethical and technical conceptions they may exhibit while designing and auditing GLMs. Then I will investigate the contexts in which these conceptions emerge and how participants’ personal interests and prior experiences may relate to their conceptions. I will also conduct clinical interviews and use microgenetic knowledge analysis and ordered network analysis to investigate how participants’ ethical and technical conceptions of GLMs relate to each other and change after the workshop. The study will contribute (a) evidence of how engaging youth in design and auditing activities may support the development of ethical and technical understanding of GLMs and (b) an inventory of novice design and auditing practices that may support youth’s technical and ethical understanding of GLMs.

**Решение:** -4 педагогика, развитие понимания этики и принципов ИИ школьниками 9 класса

---

### 372 · R2828

**Can LLMs Understand Punchlines? LLMs' Narrative Understanding Evaluation with Short-shorts**

2026 · International Conference on Language Resources and Evaluation · journalarticle · https://doi.org/10.63317/4n2p36736i24

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 NLP, понимание юмора и панчлайнов в микрорассказах, нет клинико-психологического конструкта

---

### 373 · R10736

**A Confidence-Diversity Framework for Calibrating AI Judgement in Accessible Qualitative Coding Tasks**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2508.02029

LLMs enable qualitative coding at large scale, but assessing reliability remains challenging where human experts seldom agree. We investigate confidence-diversity calibration as a quality assessment framework for accessible coding tasks where LLMs already demonstrate strong performance but exhibit overconfidence. Analysing 5,680 coding decisions from eight state-of-the-art LLMs across ten categories, we find that mean self-confidence tracks inter-model agreement closely (Pearson r=0.82). Adding model diversity quantified as normalised Shannon entropy produces a dual signal explaining agreement almost completely (R-squared=0.979), though this high predictive power likely reflects task simplicity for current LLMs. The framework enables a three-tier workflow auto-accepting 35 percent of segments with less than 5 percent error, cutting manual effort by 65 percent. Cross-domain validation confirms transferability (kappa improvements of 0.20 to 0.78). While establishing a methodological foundation for AI judgement calibration, the true potential likely lies in more challenging scenarios where LLMs may demonstrate comparative advantages over human cognitive limitations. 23 pages, 5 figures. Code and data available at https://doi.org/10.7910/DVN/G1AYGK

**Решение:** ? калибровка надежности суждений 8 LLM в задачах качественного кодирования по 10 категориям; проверить по полному тексту предметное поле и сопоставление с людьми

---

### 374 · R7655

**Generative AI as digital therapy: What we know and how to make it better?**

2025 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/b26zh_v1

Generative Artificial Intelligence (Gen-AI) holds promise for addressing the global burden of mental health conditions by expanding access to care. This article critically reviews recent research evaluating Gen-AI chatbots for the treatment of common mental disorders. Methodological analysis reveals encouraging evidence for the formation of a therapeutic alliance between users and Gen-AI chatbots, but also underscores important ethical and methodological considerations, including potential selection bias, insufficiently diverse samples and the need for constant human supervision. Emerging reports of Gen-AI potentially triggering psychosis-like symptoms raise additional safety considerations, highlighting the importance of robust participant screening and clear clinical protocols. Building on these findings, we propose a novel approach to enhance Gen-AI's therapeutic effectiveness by having it mimic a user's psychological traits, thereby strengthening the human-AI affiliation, an example of socioaffective alignment. While the integration of Gen-AI into clinical practice requires rigorous testing, ethical oversight, and interdisciplinary collaboration, this article suggests a path toward developing psychologically-informed Gen-AI models to improve accessibility, personalisation and mental healthcare outcomes.

**Решение:** -1 обзорная статья о чат-ботах генеративного ИИ в цифровой психотерапии, не эмпирика

---

### 375 · R6810

**Between Human and Machine: University Teachers’ Accounts of Judgment, Metacognitive Defense, and Cognitive Offloading in Generative AI Use**

2026 · Journal of Intelligence · journalarticle, article · en · https://doi.org/10.3390/jintelligence14100254

Generative artificial intelligence (GenAI) allows university teachers to delegate cognitive work while deciding how students should engage with it. Using codebook thematic analysis, we examined multi-source accounts from 25 teachers recruited through an AI-focused learning community and its professional networks in China. Materials comprised interviews with 22 teachers, three documentary cases, self-narratives and reflective essays. Three themes organize the findings: reconstructing the teacher role, defending professional judgment, and managing teachers’ and students’ cognitive participation. Participants described disciplinary expertise as a basis for evaluating AI outputs and reported practices intended to retain human engagement. Instrumental and partnership orientations overlapped; descriptive comparison with later use profiles did not establish a simple relationship between partnership language and usage intensity. Because the protocol introduced several focal topics, we distinguish prompted positions from volunteered formulations. The proposed belief–strategy–practice cycle is a heuristic interpretation of retrospective accounts, not a demonstrated mechanism. The study contributes an account of how teachers connect their own cognitive offloading with their reported organization of students’ learning opportunities. Its claims concern this AI-engaged sample rather than university teachers generally.

**Решение:** -4 педагогика высшей школы, качественное исследование опыта преподавателей вузов по использованию GenAI

---

### 376 · R9342

**Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2505.13348

Large Language Models (LLMs) are increasingly employed as evaluators (LLM-as-a-Judge) for assessing the quality of machine-generated text. This paradigm offers scalability and cost-effectiveness compared to human annotation. However, the reliability and security of such systems, particularly their robustness against adversarial manipulations, remain critical concerns. This paper investigates the vulnerability of LLM-as-a-Judge architectures to prompt-injection attacks, where malicious inputs are designed to compromise the judge's decision-making process. We formalize two primary attack strategies: Comparative Undermining Attack (CUA), which directly targets the final decision output, and Justification Manipulation Attack (JMA), which aims to alter the model's generated reasoning. Using the Greedy Coordinate Gradient (GCG) optimization method, we craft adversarial suffixes appended to one of the responses being compared. Experiments conducted on the MT-Bench Human Judgments dataset with open-source instruction-tuned LLMs (Qwen2.5-3B-Instruct and Falcon3-3B-Instruct) demonstrate significant susceptibility. The CUA achieves an Attack Success Rate (ASR) exceeding 30\%, while JMA also shows notable effectiveness. These findings highlight substantial vulnerabilities in current LLM-as-a-Judge systems, underscoring the need for robust defense mechanisms and further research into adversarial evaluation and trustworthiness in LLM-based assessment frameworks.

**Решение:** -4 кибербезопасность, состязательные атаки на LLM-судей на бенчмарке MT-Bench

---

### 377 · R6968

**From Digital Competence to Ethical AI Use: A Document Analysis of International and Turkish Educational Frameworks**

2026 · SciELO Preprints · preprint, ppr · https://doi.org/10.1590/scielopreprints.16719

This study examines how digital competence, digital citizenship, and artificial intelligence ethics are represented in international and Turkish educational frameworks. Competence frameworks, curricula, and policy documents published by the European Commission, Council of Europe, UNESCO, OECD, and Turkish Ministry of National Education were analysed using qualitative document analysis. Erzurumlu İbrahim Hakkı’s Marifetname was also used as a value-based interpretive source. The data were analysed using a semi-structured codebook, focusing on the themes of digital competence, digital citizenship, artificial intelligence ethics, privacy, security, critical literacy, digital self-regulation, and human oversight and agency. The findings show that AI ethics are represented more explicitly and systematically in international documents, whereas Türkiye documents emphasize values, safe use, privacy, and responsibility. The study proposes an integrated framework for value-based digital citizenship and AI ethics by linking technical competence with moral reasoning, self-regulation, human dignity, social benefit, and critical evaluation. The study argues that Türkiye’s value-based educational orientation should not be replaced by international AI ethics frameworks. Rather it should be strengthened through operational concepts such as algorithmic bias, data ethics, explainability, accountability, and generative AI literacy. The proposed frameworks links technical competence with moral reasoning, self-regulation, human dignity, critical evaluation, and social benefit, thereby offering a culturally grounded policy contribution to curriculum and responsible AI education.

**Решение:** -4 анализ документов образовательной политики и этики ИИ в Турции и мире, качественный анализ документов

---

### 378 · R4825

**Every(bot) Makes Mistakes: Coding Big Five Personalities, Context, and Tone into an LLM Chatbot Recovery Code Framework**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.05391

Despite careful design involving classifiers, parameters, and safeguarding, errors during human/AI interaction are not rare. Poor error recovery can disrupt interaction flow, damage user trust, and decrease user engagement. Whilst existing work has explored LLM recovery, tone, context, and personality as separate design dimensions, no existing work has combined these variables into a structured guidance framework. This paper presents a recovery code that maps four common LLM chatbot task contexts to associated personality traits (four Big Five personalities: Conscientiousness, Agreeableness, Openness, and Extraversion), tones, and three-stage recovery instructions. A recovery evaluation rubric was also designed, comprising three dimensions (Recovery quality, Tone alignment, and Appropriateness) and nine sub-dimensions. The methodology is exploratory, with no participants used. A between-subjects design was employed across two conditions: Condition A (baseline, uncoded), four separate Claude Sonnet 4.6 agents received no recovery code training; Condition B (coded), four separate Claude Sonnet 4.6 models were trained on the recovery code. Identical 'user' prompts and error scenarios were used across both conditions. Eight LLM evaluator agents assessed the recovery responses using the evaluation rubric, producing scores out of 5 for each sub-dimension. Results found a 27.8% average performance increase in coded recovery responses (76.7%) compared to baseline responses (48.9%). Condition B performed strongest in the appropriateness dimension (83.3%), with notable improvement in personality appropriateness (75% versus 50%) and providing explanation (60% versus 20%). These findings suggest that structured personality, context, and tone-informed recovery codes can be successfully learnt and applied by LLM chatbots to improve error recovery quality across varying contextual tasks. 14 pages of main content, 3 figures, 4 tables, 9 appendices. This paper has been submitted to the Becker Friedman Institute 2026 AI in Social Sciences conference for peer review

**Решение:** -5 эксперимент полностью in silico: 8 LLM-агентов оценивают реплики моделей Claude, участники-люди отсутствуют, E5

---

### 379 · R4832

**Media portrayals of libraries in Indonesia: A large-language-model-assisted content analysis**

2026 · IFLA Journal · journalarticle, article · en · https://doi.org/10.1177/03400352261424414

Libraries often occupy an under-represented role in public discourse, particularly in developing countries such as Indonesia. In the digital era, public understanding of libraries is partly shaped by news media, yet limited scholarship has examined how digital outlets portray them. This study analyzes coverage of libraries on two major Indonesian news platforms—Detik.com and Kompas.com—focusing on news topics, news tones, news types, library roles, and news sources. A quantitative content analysis was conducted on 166 articles published in 2022–2023. Coding was undertaken by both a human coder and a large language model during the initial reliability testing of the coding protocol, after which full-scale coding was performed with the large language model. Statistical analyses were applied to assess significant differences. The results show that Kompas.com emphasizes formal, policy-oriented reporting, while Detik.com highlights user-focused narratives. These differences suggest that library stakeholders should adapt their communication strategies to each outlet's editorial style.

**Решение:** -4 библиотековедение, контент-анализ освещения библиотек в новостях Индонезии

---

### 380 · R0231

**ChatGPT-4.5 versus pharmacists in OTC counseling: A bilingual comparative study**

2026 · Pharmacia · article · en · https://doi.org/10.3897/pharmacia.73.e181527

Background : Over-the-counter (OTC) medications enable self-care but require accurate counseling to prevent misuse, particularly in multilingual settings with limited health literacy. Pharmacists provide expert guidance; however, time constraints hinder comprehensive interactions. Generative artificial intelligence (AI) models such as ChatGPT-4.5 offer potential as decision-support tools, but their performance compared with pharmacists in bilingual OTC counseling remains underexplored. This study compared ChatGPT-4.5 and community pharmacists using standardized gastrointestinal case scenarios in English and Arabic to assess response quality, safety, and appropriateness. Methods : This cross-sectional study evaluated 22 standardized OTC cases (e.g., constipation, diarrhea) from authoritative sources, presented in English and Arabic. Fifty-eight Jordanian community pharmacists ( n = 29 per language) solved five cases each. All 44 AI responses were generated via standardized prompts without iteration. Responses were blindly rated by four experts using the CLEAR framework (completeness, lack of false information, evidence-based, appropriateness, and relevance; 5-point Likert scale). Cosine similarity quantified textual overlap; Welch’s t -tests, ANOVA, and correlations analyzed differences (SPSS v.29; α = 0.05). Inter-rater reliability was assessed using ICC. Results : ChatGPT-4.5 achieved higher mean CLEAR scores (4.8/5) than pharmacists (3.7–3.8/5; p 0.05). AI excelled in completeness and lack of false information; pharmacist performance declined with case difficulty. Cosine similarity was low (0.04–0.11), indicating distinct yet coherent AI phrasing. Younger pharmacists scored higher ( r = -0.33, p = 0.01). Qualitative analysis showed more consistent structure in AI-generated responses and greater variability among pharmacists. Conclusion : ChatGPT-4.5 demonstrates robust, language-agnostic performance for OTC counseling, suggesting its role as an educational benchmark and clinical adjunct to standardize advice and reduce variability. Pharmacy curricula should integrate AI literacy and targeted training in red-flag recognition to enhance human–AI synergy, fostering safer patient outcomes and interprofessional collaboration.

**Решение:** -4 фармация, консультирование по безрецептурным препаратам при желудочно-кишечных расстройствах

---

### 381 · R1645

**A comparative analysis of leading large language models in generating medical literature reviews: An evaluation of factual accuracy and reference fabrication**

2026 · Medical Journal Armed Forces India · article · en · https://doi.org/10.1016/j.mjafi.2026.02.011

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 сравнительный анализ LLM при генерации обзоров медицинской литературы, оценка вымышленных ссылок

---

### 382 · R9295

**Leveraging Large Language Models for Multi-Class and Multi-Label Detection of Drug Use and Overdose Symptoms on Social Media**

2025 · arXiv · preprint/article, preprint · https://doi.org/10.48550/arxiv.2504.12355

Drug overdose remains a critical global health issue, often driven by misuse of opioids, painkillers, and psychiatric medications. Traditional research methods face limitations, whereas social media offers real-time insights into self-reported substance use and overdose symptoms. This study proposes an AI-driven NLP framework trained on annotated social media data to detect commonly used drugs and associated overdose symptoms. Using a hybrid annotation strategy with LLMs and human annotators, we applied traditional ML models, neural networks, and advanced transformer-based models. Our framework achieved 98% accuracy in multi-class and 97% in multi-label classification, outperforming baseline models by up to 8%. These findings highlight the potential of AI for supporting public health surveillance and personalized intervention strategies.

**Решение:** -4 токсикология, симптомы передозировки ПАВ в соцсетях, классификация на трансформерах/ML

---

### 383 · R1745

**The Junior Developer Crisis: Impact of Generative AI on Early Career Growth in 2026**

2026 · Zenodo (CERN European Organization for Nuclear Research) · journalarticle/, article · https://doi.org/10.5281/zenodo.19666199

The traditional software development lifecycle is undergoing a significant transformation due to the rapid advancement of Generative Artificial Intelligence (GenAI) and the widespread adoption of automated coding assistants. Standard entry-level roles are increasingly being challenged by AI’s ability to handle routine syntax generation, leading to a "Junior Developer Crisis" characterized by a shrinking labor market for new graduates [6]. To overcome these issues, recent research focuses on redefining the "Seniority Gap" and identifying how high-skilled work patterns are shifting using technologies such as Large Language Models (LLMs), GitHub Copilot, and agentic workflows [3], [9]. Empirical studies indicate that while AI significantly boosts developer productivity, it also introduces a "reproducibility crisis" where generated artifacts lack deep architectural integrity [5], [10].This survey paper reviews recent work (2025–2026) in the field of AI-driven software engineering and its impact on career trajectories. It also looks at systems designed for pedagogical reform and new measures of observed labor exposure to AI automation [1], [2], [11]. Different approaches are compared based on their efficiency, cognitive load on developers, and real-time performance in industrial settings [7], [12]. From the study, it can be observed that AI-based systems improve development velocity and bridge skill gaps for lower-ability workers effectively [4]. However, their practical implementation on a large scale is still challenging due to increased technical debt and the erosion of traditional mentorship pipelines [13], [15]. Future research can focus on making these systems more explainable, optimizing early career learning paths, and developing frameworks for responsible human-AI orchestration [14], [16], [18].

**Решение:** -1 обзорная статья о влиянии GenAI на карьеру начинающих программистов, не эмпирика

---

### 384 · R2276

**Why It Hurts: Identifying the Drivers of Negative Thoughts in Emotional Support Conversations**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2607.28648

Large Language Models (LLMs) are increasingly used for emotional support tasks, such as negative thought reframing. This task relies on modifying cognitive appraisals, the subjective interpretation of events that elicit negative emotions, which is typically conceptualized along multiple discrete dimensions. Current LLM-based frameworks model cognitive appraisal by exhaustively evaluating all possible dimensions, but they fail to account for the varying saliency of these dimensions across different contexts. In this work, we investigate a vital yet overlooked question: "Can LLMs infer the salient appraisal dimensions from emotional support conversations?" To address this question, we introduce the AppraiSal benchmark, containing 996 emotional support conversations with human-annotated mental states, including salient cognitive appraisal dimensions. Furthermore, we propose PRISM, a multi-agent probabilistic framework grounded in Bayesian Inverse Planning, designed to improve LLMs' ability to identify context-specific appraisal dimensions. Experimental results show that PRISM brings improvements to LLMs across various sizes, particularly in identifying the most salient appraisal dimensions. EMNLP 2026

**Решение:** + T1 кодирование когнитивных оценок (appraisal theory) и причин негативных мыслей в 996 диалогах эмоциональной поддержки AppraiSal, LLMs vs экспертная разметка

---

### 385 · R5822

**Generative vs. Encoder Large Language Models for ASR Evaluation: A Comparative Study**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.25574

Automatic Speech Recognition (ASR) is typically evaluated using Word Error Rate (WER), which poorly reflects semantic similarity. While embedding-based metrics correlate better with human judgments, the respective roles of encoder and decoder-based Large Language Models (LLMs) remain underexplored. This paper presents a comparative study of both families for ASR evaluation. We analyze BERTScore and SemDist across different LLMs, layers, and pooling strategies, showing that both metrics can achieve strong correlation with human judgments when properly configured. For decoder models, we investigate generative LLMs in two settings: pairwise hypothesis selection via prompting and direct qualitative error classification. Our results show that encoder-based metrics remain highly competitive, while generative LLMs perform strongly in hypothesis comparison and improve the interpretability of ASR evaluation.

**Решение:** -4 оценка качества автоматического распознавания речи (ASR) с помощью LLM, компьютерные науки

---

### 386 · R1487

**Ep. 280: AI as a Shield: The High Stakes of Digital Obfuscation**

2026 · Zenodo (CERN European Organization for Nuclear Research) · audiovisual/, other · en · https://doi.org/10.5281/zenodo.19358770

Episode summary: In this episode, Herman and Corn dive into the "art of obfuscation," exploring how AI is revolutionizing the way whistleblowers and journalists protect their identities. Moving beyond dark rooms and voice modulators, they discuss the rise of high-fidelity synthetic personas and speech-to-speech synthesis that preserve human emotion while hiding the source. However, a new threat looms: digital watermarking and regulatory transparency mandates that could turn these protective tools into tracking beacons. From the technical nuances of "reshaping the digital skull" to the chilling effects of strict defamation laws, this conversation unpacks the high-stakes battle between privacy and surveillance in the age of generative AI. Show Notes ### The Art of Obfuscation: How AI is Redefining Whistleblowing In a recent episode of *My Weird Prompts*, hosts Herman and Corn Poppleberry took a deep dive into the evolving landscape of digital identity, specifically focusing on how artificial intelligence is being used as a "shield" for those who need to speak the truth from the shadows. Inspired by a voice note from their housemate Daniel, the brothers explored the transition from crude, traditional anonymity tactics to the sophisticated world of synthetic personas. #### Beyond the Silhouette: The Rise of Synthetic Personas Herman and Corn began by reflecting on the traditional imagery of whistleblowing. For decades, the gold standard for anonymity in investigative journalism was a silhouette in a dark room—a "Sixty Minutes" trope featuring a backlit figure, perhaps wearing a wig, with a voice modulated to sound like a low-pitched robot. However, as Herman pointed out, these methods are increasingly obsolete. Not only do they strip away the human connection and emotional urgency of a story, but they are also technically vulnerable. Modern image processing can often pull facial details out of the shadows, and advanced algorithms can now "de-filter" modulated audio to reconstruct a speaker's original vocal characteristics. The solution, according to the hosts, lies in "synthetic personas." Rather than simply hiding a person, AI can replace them with a high-fidelity avatar. This technology allows a whistleblower to appear on screen as a completely different, non-existent person who still mirrors the source's exact facial expressions, micro-movements, and emotional cadence. This "decouples the message from the physical identity while keeping the humanity intact," as Corn noted. #### Reshaping the Digital Skull The technical mechanics behind these synthetic personas are as fascinating as they are complex. Herman explained that the process often involves facial re-enactment using technologies like Gaussian Splatting or Neural Radiance Fields (NeRFs). The AI maps the source's facial landmarks—the eyelids, the mouth, the bridge of the nose—and applies those movements to a new "latent representation" of a face. Crucially, Herman emphasized that for true security, the system must do more than just apply a new "skin." It must literally reshape the digital skull. Advanced biometric software can often identify individuals based on the underlying geometry of their face, such as the distance between eyes or the shape of the jawline. To bypass this, the AI must alter the skeletal structure of the digital avatar to ensure no biometric match can be made to the original source. #### The Voice: Speech-to-Speech Synthesis The obfuscation doesn't stop at the visual. The brothers discussed the leap from simple pitch-shifting to "speech-to-speech synthesis." Unlike old-school modulators that sound robotic, AI can now analyze the linguistic content and "prosody" (the rhythm and intonation) of a source's speech and re-synthesize it using a completely different vocal profile. This means a whistleblower can retain the emotional weight of their testimony—the tremors of fear or the sharpness of indignation—without revealing their actual voice. As Corn illustrated, a middle-aged man in London could speak, but the output would be a perfectly natural-sounding young woman from New York, free of any digital artifacts. #### The Watermarking Paradox The conversation took a more serious turn when Herman and Corn addressed the "billion-dollar question": digital watermarking. In an effort to combat deepfakes and misinformation, tech giants like Google and Meta, along with regulatory bodies like the EU, are pushing for mandatory watermarks in AI-generated content. These can be metadata-based (C2PA) or invisible, pixel-level markers (like Google's SynthID). While these tools are designed to protect the public from scams, they pose a lethal risk to whistleblowers. If an AI-generated persona carries a hidden "serial number" that can be traced back to a specific user account or session, the anonymity of the source is compromised. A government or corporation could simply subpoena the logs associated with that watermark to unmask the whistleblower. This creates a paradox where the tools meant to protect society from AI deception simultaneously dismantle the safety of those using AI for legitimate, life-saving obfuscation. #### Legal Risks and the Chilling Effect The hosts also touched on the legal environment that makes such technology necessary. Speaking from their perspective in Jerusalem, they discussed how strict defamation laws in certain jurisdictions can be used to silence critics. In many places, proving the truth is not enough; one must also prove a specific "public interest," and the threat of ruinous legal costs often creates a "chilling effect" on free speech. In such environments, AI obfuscation isn't just a technical curiosity—it's a financial and physical necessity. If the only available AI tools are those controlled by large corporations that integrate with government surveillance via mandatory watermarking, the potential for AI to serve as a tool for freedom is severely curtailed. #### Linguistic Fingerprints and Op-Se

**Решение:** -1 подкаст / шоу-ноутс о цифровой анонимности и защите журналистов, не эмпирика

---

### 387 · R0060

**Teaching Firearm Safety Behaviors to Young Children Using Robots and Augmented Reality; The Columbine Massacre’s Effect on Gun Safety Education for American Youth**

2026 · Libra · text/dissertation, dissertation · https://doi.org/10.18130/wp7e-e225

Both my technical and STS projects focus on how young children can be effectively taught to keep themselves safe in a world where firearms are accessible and the risk of gun-related harm is real. My technical capstone project developed an AI-based firearm safety education system combining a humanoid robot, augmented reality, and large language model-driven dialogue to deliver behavioral instruction to children aged four to seven. My STS research paper examined how gun safety education in U.S. elementary schools evolved before and after the 1999 Columbine High School massacre, pointing out the shift from narrow accident-prevention programs to a layered and politically contested system of safety instruction. The two projects are directly connected, where they share the same subject age group, program materials, and the same question of what it means to teach children about the danger of firearms in a culturally divided environment. Each project continuously shaped how I understood the other. My capstone project addressed the limits of passive instruction in firearm safety education for young children. Behavioral skills training (BST), which structures learning through instruction, modeling, rehearsal, and corrective feedback, is widely recognized as the gold standard for teaching safety behaviors to children, but its delivery depends on trained human facilitators and controlled settings, making it difficult to scale. To address this, my team developed a three-module system integrating a NAO humanoid robot and augmented reality. The robot module delivered instruction aligned with the four-step safety sequence (Stop, Don't Touch, Run Away, Tell a Trusted Adult) using age-adapted scripts and synchronized gestures. An AR training module enabled gesture-based rehearsal with real-time AI coaching, and an AR testing module assessed skill generalization across three simulated domestic scenarios. Expert evaluation by ten professionals in child development, education, and injury prevention showed strong ratings across all modules, but qualitative feedback identified four key areas for refinement: language accessibility for younger children, trauma-informed interaction protocols, AI dialogue consistency, and fuller implementation of the BST cycle. My STS paper explored how gun safety education in U.S. elementary schools changed following the Columbine High School massacre, arguing that the event turned a narrow field into a layered, politically fractured system. Before 1999, gun safety education was dominated by accident-prevention programs like the Eddie Eagle GunSafe Program, which reduced children's role to a simple four step avoidance response and treated firearms as neutral objects requiring caution rather than as sources of intentional violence. I noted how the Columbine massacre functioned as a focusing event that fundamentally redefined the problem of school gun violence, shifting attention from accidental encounters to the threat of intentional harm from within student populations. This shift was visible in national political discourse, media framing, and the expansion of school safety infrastructure, including the adoption of lockdown drills, violence-prevention curricula, trauma-informed practices, and formal state safety legislation. However, this change did not replace earlier approaches, it layered over them. The product is a system where children may encounter Eddie Eagle's avoidance message, BST-style behavioral rehearsal, lockdown drills, or social-emotional learning programming, implemented by different institutional actors without shared frameworks or coordination. The paper argues that gun safety education should be understood as a constructed knowledge system whose current form reflects an ongoing negotiation among competing political and cultural interests, with important implications for how future standardization efforts should be approached. Working on both projects simultaneously revealed things that neither would have reached on its own. The most direct crossover came early, when I began gathering existing curriculum and program materials to inform the design of the technical system and found that standardized, publicly available instructional content for this age group was very limited. This difficulty was a symptom of the broken system my STS paper ended up describing. The lack of coordinated content that I encountered as a design constraint for my technical project became the motivating question of my STS research: why had gun safety education for young children remained so inconsistent, and what forces explained this fragmentation? In the other direction, the STS research deepened the decisions I made in building the technical system. Understanding that the Eddie Eagle program had become contested after Columbine, and that its critics argued it actually normalized rather than just regulated firearms, made me pay more attention to how the robot module framed firearms and what assumptions existed in its dialogue. The two projects shared source material, drawing on the same foundational programs, behavioral training literature, and the same debate about whether passive rule instruction actually changes children's behavior in real encounters. The STS paper's conclusion that gun safety education is a negotiated system rather than a solved one ultimately reinforced the value of the technical project, not as a final solution but as a contribution to an ongoing and unresolved effort to give children tools that actually work, all in an attempt to contribute to the overarching goal to keep kids safe from firearms.

**Решение:** -4 педагогика безопасности обращения с оружием у детей, робототехника

---

### 388 · R3881

**CopyShield: Comparing Copyright Defense Mechanisms for Large Language Models**

2026 · MBZUAI · dissertation/thesis, dissertation · en · https://doi.org/10.82419/329

Large language models (LLMs) trained on massive corpora have demonstrated a well-documented tendency to memorize and reproduce portions of their training data verbatim, including copyrighted literary works. This phenomenon poses significant legal and ethical risks, as verbatim or near-verbatim reproduction of protected text may constitute copyright infringement under intellectual property law. While several defense mechanisms have been proposed in the literature, they have been developed and evaluated in isolation, making direct comparison difficult. This thesis presents CopyShield, a systematic study of three defense approaches that intervene at fundamentally different levels of the LLM generation pipeline to suppress copyright leakage while preserving model utility. Using a controlled experimental setup in which a LLaMA-3.1-8B base model is fine-tuned to memorize five public domain books as a proxy for copyrighted content, we evaluate each method under identical conditions against two co-equal objectives: copyright compliance and utility preservation. The three methods examined are: (1) contrastive decoding, which operates at the output level by down-weighting token probabilities that are elevated relative to a reference model trained without the target books; (2) Direct Preference Optimization (DPO), which operates at the behavioral level by fine-tuning the model to prefer non-reproducing responses; and (3) activation intervention, which operates at the representation level by training a linear classifier on hidden-state activations to detect and intercept copyright-reproducing generation before output is produced. Our evaluation employs a multi-metric framework covering both literal leakage (NV-Recall, Phase-1 LCS, ROUGE-L) and non-literal leakage (calibrated embedding similarity), alongside utility metrics including AI-judge scores for helpfulness, coherence, informativeness, and correctness, as well as refusal rate and degeneracy rate. Results show that all three methods reduce copyright leakage relative to the undefended baseline, but with distinct trade-off profiles. Contrastive decoding reduces mean NV-Recall by 23--27% and modestly reduces non-literal flagging across all lambda values (3.5--4.0% vs. 5.0% baseline), but preserves only 78.8--82.1% of raw base QA capability. DPO achieves the strongest literal suppression---eliminating all perfect copies and reducing mean NV-Recall by 99.2% to base model level (0.002)---while achieving the highest QA utility of all methods (99.4% of raw base capability) and introducing zero refusals; non-literal flagging remains comparable to the baseline (5.5%). Activation intervention reduces mean NV-Recall by 89% and achieves the lowest non-literal flagging (1/200, 0.5%) via an 84% intervention rate, but introduces a 6% false-positive rate on factual queries and preserves 94.9% of raw base QA capability. No single method dominates all dimensions, and the optimal choice depends on deployment context. The main contributions of this thesis are: (i) a comparative study of three defense approaches that span output, behavioral, and representation levels; (ii) a systematic and reproducible evaluation under identical conditions using statistically calibrated thresholds; and (iii) empirical evidence that the level of intervention determines the type and magnitude of the compliance--utility trade-off, providing actionable guidance for practitioners deploying LLMs under copyright constraints.

**Решение:** -4 компьютерные науки, защита авторских прав в LLM (CopyShield)

---

### 389 · R7585

**DinoCompanion: An Attachment-Theory Informed Multimodal Robot for Emotionally Responsive Child-AI Interaction**

2025 · arXiv (Cornell University) · preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2506.12486

Children's emotional development fundamentally relies on secure attachment relationships, yet current AI companions lack the theoretical foundation to provide developmentally appropriate emotional support. We introduce DinoCompanion, the first attachment-theory-grounded multimodal robot for emotionally responsive child-AI interaction. We address three critical challenges in child-AI systems: the absence of developmentally-informed AI architectures, the need to balance engagement with safety, and the lack of standardized evaluation frameworks for attachment-based capabilities. Our contributions include: (i) a multimodal dataset of 128 caregiver-child dyads containing 125,382 annotated clips with paired preference-risk labels, (ii) CARPO (Child-Aware Risk-calibrated Preference Optimization), a novel training objective that maximizes engagement while applying epistemic-uncertainty-weighted risk penalties, and (iii) AttachSecure-Bench, a comprehensive evaluation benchmark covering ten attachment-centric competencies with strong expert consensus (\k{appa}=0.81). DinoCompanion achieves state-of-the-art performance (57.15%), outperforming GPT-4o (50.29%) and Claude-3.7-Sonnet (53.43%), with exceptional secure base behaviors (72.99%, approaching human expert levels of 78.4%) and superior attachment risk detection (69.73%). Ablations validate the critical importance of multimodal fusion, uncertainty-aware risk modeling, and hierarchical memory for coherent, emotionally attuned interactions.

**Решение:** ? робот-компаньон на основе теории привязанности (AttachSecure-Bench), оценка 10 компетенций привязанности и риска; проверить модальность (текст vs видео)

---

### 390 · R8232

**Validating GenAI feedback in suicide prevention training: a mixed-methods study of QPR skill assessment.**

2025 · Frontiers in medicine · journal article, journalarticle, article · eng · https://doi.org/10.3389/fmed.2025.1709743

Background Gatekeeper training using the Question, Persuade, and Refer (QPR) model has become a key strategy in suicide prevention. Yet traditional QPR-based training methods are limited by their lack of scales, interactive practice and reliable assessments of skill acquisition. Generative AI (GenAI)-driven simulators can provide a novel solution for this critical gap by offering scalable and cost-effective practices that can be culturally adapted, thus democratizing access to skills training without the potential embarrassment of live roleplay. Nevertheless, the rigorous validation of AI systems as reliable evaluation tools remains an open question. This study seeks to validate the reliability of AI-based assessments in the high-stakes context of suicide prevention, thus constituting a critical step toward using GenAI for scalable skill evaluation. Methods Three independent experts rated 54 simulated QPR conversations to establish the empirical reliability of a GenAI simulator feedback in the context of suicide prevention training. The primary analysis compared the automated numerical scores of the AI feedback against this human benchmark (RQ1). Secondary analyses included examination of the influence of participant characteristics on ratings (RQ2) and qualitative assessment of the AI feedback for pedagogical depth and accuracy across varied performance levels (RQ3). Results The primary finding (RQ1) exhibited a moderate-to-strong positive correlation ( r = 0.519-0.776) between the GenAI adherence scores and the human-rated benchmark, providing initial evidence for the tool's reliability. No significant gender-based differences were found in either GenAI or human ratings, supporting the study's aim for an unbiased tool (RQ2). Qualitative analysis demonstrated GenAI's ability to accurately identify key QPR components and deliver nuanced in-depth feedback (RQ3). Conclusion This study provides critical initial evidence that GenAI can serve as a reliable feedback tool for evaluating complex crisis intervention skills. Its ability to provide consistent, scalable, and unbiased assessments opens new possibilities for accessible evidence-based training. Despite these strong foundational capabilities, the findings also highlight the need for further calibration to align GenAI's judgment more closely with expert human nuances and enable it to evolve beyond a purely performance-focused tool.

**Решение:** + T4 оценка навыков кризисного вмешательства и предотвращения суицида (модель QPR) в диалогах, GenAI vs 3 эксперта, r=0.519–0.776

---

### 391 · R3087

**Large language models to infer depression in patients with neurological conditions.**

2026 · BMJ neurology open · journal article, journalarticle, article · eng · https://doi.org/10.1136/bmjno-2025-001502

Objective: To develop and validate a large language model (LLM) prompt capable of ascertaining a patient's depression from their multiple sclerosis (MS) neurologist's note and to explore its potential for earlier detection of depression in MS care. Materials and methods: This single-center retrospective study analysed prospectively collected electronic health record notes. In phase I, an institutionally secure ChatGPT-4 prompt was iteratively refined to infer the presence of depression using the neurologist's note and compared with manual annotation of the neurologist's impression (depression: present, absent, no mention) and patient-reported outcomes (PROs): Hospital Anxiety and Depression Scale or Patient Health Questionnaire-9. In phase II, longitudinal analysis compared timing of depression detection by the prompt and the neurologist across 5 years of notes for 250 patients. Results: In phase I (n=278 adults with MS), the LLM prompt detected depression in 60.4% of notes (168/278). When compared with neurologist impression in the clinical notes, the prompt achieved 97.3% sensitivity and 84.4% accuracy. Specificity was more modest (68.3%): when neurologists did not mention depression, the prompt inferred depression based on symptoms, history and medications. When PRO and neurologist impression disagreed, the prompt aligned with PROs 61.9% of the time. In phase II, the LLM inferred depression earlier than the neurologist in 18.8% of patients, at an average of 2.45 (SD 1.54) years earlier. Conclusion: The prompt was highly sensitive to neurologist documentation of depression in clinical notes; it inferred both present/treated depression from other note components. Potential applications include quality improvement initiatives aiming to improve depression care on a cohort level.

**Решение:** ? выявление депрессии по неврологическим записям (MS) с помощью ChatGPT-4; проверить по полному тексту, основной эталон — ручная разметка текста (T1/T3) или PRO (-3)

---

### 392 · R1298

**Testing large language models as a simulation tool for multi-theory analysis to simulate research outcomes**

2026 · International Journal of Information and Learning Technology · journalarticle, article · en · https://doi.org/10.1108/ijilt-09-2025-0270

Purpose This study aims to test large language models as a tool for multi-theory simulation that could potentially augment the doctoral student’s (DS) research efficiency. Design/methodology/approach The study proceeded in three phases, commencing with theory simulations where identical prompts were applied to GPT-5, DeepSeek-V3.2 and Mistral Small 3.1. Phase Two involved a quantitative evaluation by two independent raters using the percentage of maximum possible score and the average deviation index. Finally, Phase Three entailed a thematic analysis of the simulated outputs. Findings Large language models can augment research efficiency by simulating varied theoretical perspectives and assisting the student in assessing the suitability of theory before commencing a real-world study. Quantitative analysis showed that GPT-5 achieved the highest percentage maximum possible score, followed by DeepSeek-V3.2, and finally Mistral Small 3.1. Additionally, the average deviation index was 0.53, which is less than the critical value of 0.67. Therefore, the inter-rater reliability was established. The qualitative analysis revealed that two of the three models generated the same output, while the third generated a slightly different output. Originality/value This research integrates large language model simulation into educational research methodology before conducting empirical studies. This method could potentially augment doctoral research efficiency and present the DS with novel perspectives on their research areas.

**Решение:** -4 педагогика/науковедение, симуляция теоретических перспектив для аспирантов

---

### 393 · R0526

**Replication package for Change Propagation in Multi-Version Software**

2026 · Zenodo (CERN European Organization for Nuclear Research) · text/data paper, article · https://doi.org/10.5281/zenodo.22087786

Supplementary data for the systematic literature review: This package contains the frozen extraction table, audit trail, codebook, and count tables used in the paper. Searches retrieved 920 records (cutoff 19 August 2026). After screening and a consistency audit, 129 unique primary studies were included (1999–2026). The data-extraction template and the included-study list are Appendix 1 and Appendix 2 of the manuscript. Contents- papers_normalized.csv — frozen extraction table (N = 129)- papers_normalized_pre_audit.csv — pre-audit snapshot (143 provisionally retained records)- exclusion_audit.csv — 14 records removed in the consistency audit- stats_summary.csv — manuscript counts in tabular form- Data_Definitions.md — column definitions and quality-assessment criteria- rebuild_report.md — headline counts cited in the paper Headline numbers (from rebuild_report.md)- Origin: 115 academia, 11 industry, 3 mixed- Analysis: 90 quantitative, 35 qualitative, 4 mixed- Quality: mean 3.29 (SD 0.84); 104 (80.6%) scored ≥ 3- Stage 1 identify family: 49/129 (38.0%); Stage 2 transformation: 12/129 (9.3%); Stage 3 merging validator: 1/129- RQ coverage: RQ1 129; RQ2 114; RQ3 129; RQ4 128; explicit future work 105- LLM/transformer studies: 11 (8.5%), all 2024–2026 License: CC BY 4.0 If you use this data, please cite the paper above.

**Решение:** -4 программная инженерия, версионирование ПО (пакет репликации данных)

---

### 394 · R1768

**Limits of Applicability of Artificial Intelligence in Public Administration: Memory of LLM-Based Agents vs. Human Memory**

2026 · DOAJ (DOAJ: Directory of Open Access Journals) · article · ru · https://doaj.org/article/99e0dc3f9f1a4e1698e66a97295e44d7

In recent years, large language models and agent systems based on them have been considered a promising tool for the digital transformation of public administration. However, the practical effectiveness of such systems is determined not only by the quality of text generation, including grammatical correctness, coherence, and general awareness, but also by their ability to reliably retain context, retrieve previously acquired information, and reproduce procedural rules within long-term managerial processes. For public organizations, this aspect is particularly critical, as administrative activity relies on stable memory of regulatory requirements, organizational rules, facts of specific cases, and their chronological order.Purpose. The purpose of the article is to determine the limits of applicability of agent systems based on large language models in public administration through a comparative analysis of human memory models and the memory architectures of such systems.Methods. The study employs a comparative analytical approach. Basic cognitive models of human memory are examined, and their characteristics relevant to managerial activity are identified. Subsequently, architectural mechanisms of information storage and retrieval in agent systems based on large language models are analyzed as a functional analogue of human memory.Results. The analysis demonstrates that agent systems reproduce certain external functions of human memory through a combination of short-term contextual representations and external knowledge repositories. At the same time, fundamental differences are identified, including the absence of autobiographical memory, experiential chronology, embedded responsibility mechanisms, and causal verification. These limitations increase the risk of contextual distortion and complicate the validation of generated outputs.Conclusions. It is concluded that, at present, agent systems based on large language models cannot be used for autonomous decision-making in responsible administrative procedures. Nevertheless, they show significant potential as cognitive assistants for public servants, provided that mandatory human oversight is maintained and personal responsibility for decisions is preserved.

**Решение:** -1 государственное управление, теоретический сравнительный анализ архитектур памяти агентов и человека

---

### 395 · R10654

**Clay Play: A Metaphorical LLM Interface for Dynamic Idea Generation and Exploration**

2025 · UIST Adjunct · journalarticle, book · https://doi.org/10.1145/3746058.3758345

We propose Idea Clay, a direct manipulation interface for large language models (LLMs) designed to support non-linear and continuous idea generation. Inspired by the metaphor of clay play, users interact with visual “idea fragments” by merging and splitting them to invoke LLM-driven operations. The objective of this research is to facilitate the iterative and exploratory nature of divergent thinking through metaphor-based manipulations, thereby supporting the generation of creative ideas. A user study with 12 participants provided evidence that the interaction of clay metaphors facilitates intuitive and efficient generation and exploration, thereby promoting the creative process. We discuss how metaphor-based manipulation can promote intuitive and engaging human-AI collaboration in creative tasks.

**Решение:** -4 HCI, интерфейс Idea Clay для генерации идей, дизайн взаимодействия

---

### 396 · R11081

**The aluminum standard: using generative Artificial Intelligence tools to synthesize and annotate non-structured patient data.**

2024 · BMC medical informatics and decision making · journal article, journalarticle, other/article · eng · https://doi.org/10.1186/s12911-024-02825-4

BACKGROUND: Medical narratives are fundamental to the correct identification of a patient's health condition. This is not only because it describes the patient's situation. It also contains relevant information about the patient's context and health state evolution. Narratives are usually vague and cannot be categorized easily. On the other hand, once the patient's situation is correctly identified based on a narrative, it is then possible to map the patient's situation into precise classification schemas and ontologies that are machine-readable. To this end, language models can be trained to read and extract elements from these narratives. However, the main problem is the lack of data for model identification and model training in languages other than English. First, gold standard annotations are usually not available due to the high level of data protection for patient data. Second, gold standard annotations (if available) are difficult to access. Alternative available data, like MIMIC (Sci Data 3:1, 2016) is written in English and for specific patient conditions like intensive care. Thus, when model training is required for other types of patients, like oncology (and not intensive care), this could lead to bias. To facilitate clinical narrative model training, a method for creating high-quality synthetic narratives is needed. METHOD: We devised workflows based on generative AI methods to synthesize narratives in the German language to avoid the disclosure of patient's health data. Since we required highly realistic narratives, we generated prompts, written with high-quality medical terminology, asking for clinical narratives containing both a main and co-disease. The frequency of distribution of both the main and co-disease was extracted from the hospital's structured data, such that the synthetic narratives reflect the disease distribution among the patient's cohort. In order to validate the quality of the synthetic narratives, we annotated them to train a Named Entity Recognition (NER) algorithm. According to our assumptions, the validation of this system implies that the synthesized data used for its training are of acceptable quality. RESULT: We report precision, recall and F1 score for the NER model while also considering metrics that take into account both exact and partial entity matches. Trained models are cautious, with a precision up to 0.8 for Entity Type match metric and a F1 score of 0.3. CONCLUSION: Despite its inherent limitations, this technology has the potential to allow data interoperability by using encoded diseases across languages and regions without compromising data safety. Additionally, it facilitates the synthesis of unstructured patient data. In this way, the identification and training of models can be accelerated. We believe that this method may be able to generate discharge letters for any combination of main and co-diseases, which will significantly reduce the amount of time spent writing these letters by healthcare professionals.

**Решение:** -4 генерация синтетических медицинских записей на немецком для обучения NER по соматическим заболеваниям

---

### 397 · R5306

**A hybrid self-improvable meta-learning network for utterance-level Sentiment classification in scripted dialogues**

2026 · Computers & Electrical Engineering · article · en · https://doi.org/10.1016/j.compeleceng.2026.111571

The accurate estimation of affective states in cinematic dialogues through spoken words is a challenging task in natural language processing due to contextual ambiguities and variations in narrative context. In this paper, a unified framework called the Hybrid Self-Improvable Meta-Learning Network (H-SIMNet) is proposed for utterance-level sentiment classification in film dialogues. The proposed framework combines heterogeneous base learners, namely a fine-tuned Bidirectional Encoder Representations from Transformers (BERT) model, a fine-tuned Generative Pre-trained Transformer 2 (GPT-2) model, and a bidirectional long short-term memory (BiLSTM) network, through movie-grouped out-of-fold stacking with a residual-driven refinement stage. To ensure reliable evaluation, the framework employs a leakage-free evaluation protocol , in which data splitting and all fitted preprocessing operations are performed exclusively within the training folds, preventing information from validation folds from influencing model development. The proposed framework is evaluated using the Cornell Movie-Dialogs Corpus with ternary silver-standard sentiment labels derived from a weighted fusion of the Valence Aware Dictionary and sEntiment Reasoner (VADER) and TextBlob lexicon scores. H-SIMNet achieves an accuracy of 95.27% ± 0.19% , with macro-precision, macro-recall, and macro-F1 scores of 94.74%, 94.87%, and 94.80% , respectively, and Cohen’s κ of 0.9262 across eight independent film-grouped splits (80%/20% film-disjoint train/test partitions, with a 15% film-grouped validation subset held out from each training partition for model selection). Under the same evaluation protocol, fine-tuned BERT, GPT-2, and BiLSTM achieve accuracies of 94.78%, 93.84% , and 89.24% , respectively. The framework is further validated, using text only, on the independently human-annotated Multimodal EmotionLines Dataset (MELD), where H-SIMNet achieves 71.15% ± 0.25% accuracy, comparable to BERT (71.28%). These results provide a controlled and leakage-free evaluation of H-SIMNet for sentiment classification in film dialogues.

**Решение:** -5 классический стек fine-tuned моделей BERT/GPT-2/BiLSTM для сентимента в кинодиалогах Cornell/MELD, нет генеративной LLM-оценщика текста

---

### 398 · R5635

**ILM: An AI-Powered Storytelling Educational Tool**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.12064

Digital technologies have made Islamic narratives more accessible, but existing platforms provide limited support for structured learning and comprehension of these stories, particularly in Arabic and multilingual settings. We present ILM, an interactive educational platform for Stories of the Prophets that combines Arabic natural language processing, structured knowledge representation, and retrieval-based question generation. Admin-approved Arabic narratives are processed by a Knowledge Graph (KG) Constructor Engine that identifies entities and narrative relationships and stores them as structured knowledge, enabling learners to explore stories through a visual story map and answer entity- and relation-based questions generated from the KG. Separately, a multilingual retrieval pipeline retrieves relevant passages from the original narratives to generate multiple-choice and open-ended comprehension questions. For open-ended questions, an LLM-as-a-Judge evaluates learners' answers against the retrieved passages and reference answers to determine correctness. The platform also incorporates Quranic content as a separate enrichment layer, allowing selected narratives to be supplemented with source-supported information. By combining structured knowledge with passage-based retrieval, ILM supports narrative exploration, comprehension, and assessment across Arabic and multilingual content. The system demonstrates the feasibility of combining structured knowledge representation and retrieval-based generation to support interactive learning of Islamic narratives. A demo is available at anonymous.4open.science/r/mml-5FCF.

**Решение:** -4 религиоведение и педагогика, обучающая платформа ILM

---

### 399 · R7596

**Theoretical and Methodological Shifts in Social Work Research: An AI-Driven Analysis of Postmodern and Critical Theory at the SSWR Annual Conference**

2025 · Research on Social Work Practice · journalarticle, article · en · https://doi.org/10.1177/10497315251352838

Purpose: This study empirically documents temporal patterns in social work research's engagement with postmodern and critical theory (P/CT) frameworks. Methods: Large language models (LLMs) were used to analyze 19,134 conference abstracts presented at the Society for Social Work and Research (2012–2025) for P/CT alignment and methodology. Multimodel evaluation demonstrated excellent reliability across six frontier LLMs (kappa = .73). Results: Temporal analysis revealed substantial increases in P/CT engagement, with “Aligned” presentations growing 7.7-fold and “Partially Aligned” tripling between 2012 and 2025. This growth was distinctly concentrated in qualitative research, reaching 9.28% aligned and 47.81% partially aligned by 2025. The share of quantitative research declined (66.03%–48.36%), while qualitative research expanded (18.43%–31.20%). These trends accelerated after 2019. Discussion: Findings validate increased P/CT presence as methodological concentration, not uniform adoption. This provides empirical data for disciplinary discourse and demonstrates artificial intelligence's utility for large-scale content analysis.

**Решение:** -5 согласие только между 6 LLMs (kappa=0.73) без людей; к тому же наукометрия/социологические теории P/CT в тезисах конференций

---

### 400 · R6497

**AI Misalignment Is Inevitable but Does Not Require Complete Elimination: Diagnosis and Occupational Anchor Alignment Scheme**

2026 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.21136534

Author Information Author: Baichen Yi Affiliation: Independent Researcher, Xi'an, Shaanxi 710000, China ORCID: 0009-0008-6242-7743 Corresponding Author: Baichen Yi Preprint Version: v3.0 Email: ybcbenxin@163.com Conflict of Interest Statement: All authors declare no conflicts of interest related to this work. AI Assistance Statement: Artificial intelligence tools were used to assist in content organization and format optimization during the writing process. The core theories and arguments are independently completed by the author. Author’s Positioning Statement The author of this paper is an independent researcher and the original proponent of the MFY Three-Variable Steady-State Model, with primary expertise in constructing psychology and systems theory frameworks. This paper represents a cross-domain applied derivation of the model in the field of AI alignment. The theoretical predictions presented herein (especially Prediction 5: "embedding depth is positively correlated with anti-bypass capability") require independent verification by researchers with AI engineering capabilities. Researchers in the AI safety field are invited to conduct independent empirical tests; both supporting and falsifying results will provide critical evidence for judging the framework’s applicability in the AI domain. Copyright License This preprint is licensed under the CC BY-NC-ND 4.0 International License. It is open for global sharing and reproduction on the premises of proper attribution, non-commercial use, and no derivative modification of the original text. Special Authorization Statement: The author specifically authorizes any individual or institution to translate the full or partial content of this paper into other languages. Translated versions must preserve the original logic intact and clearly indicate the original source and author information. Abstract Background: Using the MFY Three-Variable Steady-State Model as the analytical framework, this paper conducts a cross-domain diagnosis of the AI misalignment problem, derives five falsifiable predictions, and verifies each with independent empirical evidence (Proposition A). Building on the diagnostic conclusions, this paper further proposes a layered artificial anchor alignment scheme (Proposition B) as a testable inference to be adjudicated by independent experiments. Methods: This paper adopts the MFY Three-Variable Steady-State Model — which has passed cross-domain logical consistency tests — as its core analytical framework. The framework has been verified for its universality in describing expectation-driven complex open systems across multiple disciplines including psychology, medicine, evolutionary biology, and economics. This paper first reviews the three-layer defense mechanism of human systems and the clinical symptoms arising from its impairment. Through rigorous behavioral comparison, it demonstrates that the functional performance of current AI systems is isomorphic to the symptoms observed when human defense mechanisms are completely impaired. Based on this isomorphism, this paper derives the specific connotations of the MFY five-fold constraints in the AI context, extracts five falsifiable theoretical predictions, and validates them one by one against multiple independent empirical studies published in recent years. Results: Among the five falsifiable predictions derived from the MFY framework, four have been confirmed or partially confirmed by independent empirical research. Both Type A consensus restatement predictions (non-attenuated input-to-output transmission, no natural upper limit for misalignment) have been fully verified. Among the three Type B incremental inference predictions: the existence of the sycophantic feedback loop has received direct empirical support, but the critical condition for positive feedback remains to be validated; that external calibration can significantly reduce misalignment has been verified, while the claim that it "cannot be completely eliminated" has not been directly confirmed or falsified; the positive correlation between embedding depth and anti-bypass capability remains entirely untested. The incremental predictive power of the framework is currently in a "partially supported" state. These verifications collectively point to a core fact: AI misalignment is a structural inevitability. However, the more critical theoretical gap at present is not misalignment itself, but the complete absence of endogenous calibration mechanisms in AI systems after misalignment occurs — this is the most fundamental functional difference between AI and human systems. Conclusions: The functional performance of current AI systems is isomorphic to the clinical symptoms of complete impairment of the human three-layer defense mechanism, and their misalignment is a predictable outcome. The MFY framework has generated testable theoretical predictions for the AI misalignment problem that can be examined via cross-domain logical consistency, with four predictions already empirically corroborated. This proves the framework possesses genuine predictive power rather than merely ex post explanatory power. Based on the impairment diagnosis, this paper derives the structural hypothesis of a layered artificial defense system: artificial Y-layer defense (input filtering), artificial M-layer defense (structural resistance), and artificial final defense (post-misalignment calibration analysis and defense upgrade), the last of which introduces the dimension of design evolution through a calibration analysis cycle. Keywords: Artificial Intelligence Alignment; Large Language Models; Value Alignment; AI Safety; AI Misalignment; Jailbreaking; RLHF; Sycophancy Effect; Occupational Standard Anchors; Artificial Anchors; Embedding Depth Gradient; Architectural Constraints; MFY Three-Variable Steady-State Model; Nested Misalignment Spiral; Endogenous Defense Mech

**Решение:** -1 теоретический препринт / эссе по согласованию ИИ (AI alignment) по модели MFY, не эмпирика
