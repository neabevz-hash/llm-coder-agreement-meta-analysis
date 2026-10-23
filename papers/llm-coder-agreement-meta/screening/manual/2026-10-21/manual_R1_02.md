# Ручной отбор, часть 2

Ручной отбор, часть 2: записи 151–300 из 1000. Эти записи вы размечаете сами, вместо проходов ИИ (deviations.md, D3); это случайные 1000 записей из тех, что ИИ ещё не разметил (зерно 20261024). **Меток ИИ здесь нет и не будет.** Ваше решение окончательное: «+» и «?» идут на полный текст. Размечайте в любом порядке и в несколько заходов.

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

### 151 · R7267

**Unraveling Online Mental Health Through the Lens of Early Maladaptive Schemas: AI-Enabled Content Analysis of Online Mental Health Communities.**

2025 · Journal of medical Internet research · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.2196/59524

BACKGROUND: Early maladaptive schemas (EMSs) are pervasive, self-defeating patterns of thoughts and emotions underlying most mental health problems and are central in schema therapy. However, the characteristics of EMSs vary across demographics, and despite the growing use of online mental health communities (OMHCs), how EMSs manifest in these online support-seeking environments remains unclear. Understanding these characteristics could inform the design of more effective interventions powered by artificial intelligence to address online support seekers' unique therapeutic needs. OBJECTIVE: We aimed to uncover associations between EMSs and mental health problems within OMHCs and examine features of EMSs as they are reflected in OMHCs. METHODS: We curated a dataset of 29,329 posts from widely accessed OMHCs, labeling each with relevant schemas and mental health problems. To identify associations, we conducted chi-square tests of independence and calculated odds ratios (ORs) with the dataset. In addition, we developed a novel group-level case conceptualization technique, leveraging GPT-4 to extract features of EMSs from OMHC texts across key schema therapy dimensions, such as schema triggers and coping responses. RESULTS: Several associations were identified between EMSs and mental health problems, reflecting how EMSs manifest in online support-seeking contexts. Anxiety-related problems typically highlighted vulnerability to harm or illness (OR 5.64, 95% CI 5.34-5.96; P<.001), while depression-related problems emphasized unmet interpersonal needs, such as social isolation (OR 3.18, 95% CI 3.02-3.34; P<.001). Conversely, problems with eating disorders mostly exemplified negative self-perception and emotional inhibition (OR 1.89, 95% CI 1.45-2.46; P<.001). Personality disorders reflected themes of subjugation (OR 2.51, 95% CI 1.86-3.39; P<.001), while posttraumatic stress disorder problems involved distressing experiences and mistrust (OR 5.04, 95% CI 4.49-5.66; P<.001). Substance use disorder problems reflected negative self-perception of failure to achieve (OR 1.83, 95% CI 1.35-2.49; P<.001). Depression, personality disorders, and posttraumatic stress disorder were also associated with 12, 9, and 7 EMSs, respectively, emphasizing their complexities and the need for more comprehensive interventions. In contrast, anxiety, eating disorder, and substance use disorder were related to only 2 to 3 EMSs, suggesting that these problems are better addressed through targeted interventions. In addition, the EMS features extracted from our dataset averaged 13.27 (SD 3.05) negative features per schema, with 2.65 (SD 1.07) features per dimension, as supported by existing literature. CONCLUSIONS: We uncovered various associations between EMSs and mental health problems among online support seekers, highlighting the prominence of specific EMSs in each problem and the unique complexities of each problem in terms of EMSs. We also identified EMS features as expressed by support seekers in OMHCs, reinforcing the relevance of EMSs in these online support-seeking contexts. These insights are valuable for understanding how EMS are characterized in OMHCs and can inform the development of more effective artificial intelligence-powered tools to enhance support on these platforms.

**Решение:** ? T1 кодирование ранних дезадаптивных схем (EMS) в текстах через GPT-4; проверить согласие с экспертами в полном тексте

---

### 152 · R1601

**Precision oncology meets Generative AI: assessing large language models in multidisciplinary GIST tumor boards.**

2026 · BMC cancer · journal article, journalarticle, review · eng · https://doi.org/10.1186/s12885-026-16537-7

Abstract Objectives Gastrointestinal stromal tumors (GISTs) are molecularly heterogeneous neoplasms whose management depends on individualized, multidisciplinary decision-making. While multidisciplinary tumor boards (MTBs) represent the standard of care, access remains limited in many clinical settings. This study evaluates the performance of two large language models in generating GIST MTB recommendations and assesses their agreement with expert MTB decisions using predefined clinical evaluation criteria. Materials and methods This retrospective single-center study included 99 GIST cases discussed at an institutional MTB. A structured prompt was developed to extract clinical variables and generate treatment recommendations. ChatGPT-5 and Qwen3 were independently evaluated across five predefined domains: diagnostic recommendations, therapeutic modalities, treatment sequence and timing, systemic therapy regimen selection, and clinical contextualization. Two expert reviewers scored all outputs in a blinded fashion. Normalized scores, inter-model comparisons, perfect-case rates, and inter-rater agreement were analyzed. Results Both models demonstrated high concordance with expert MTB recommendations, with mean total normalized scores of 0.901 for ChatGPT-5 and 0.875 for Qwen3, without a significant difference between models ( p &gt; 0.05). Perfect agreement was observed in 52.5% of ChatGPT-5 cases and 48.5% of Qwen3 cases ( p &gt; 0.05). Diagnostic recommendations scored significantly lower than all other domains in both models (all adjusted p &lt; 0.05). Overall inter-rater agreement was almost perfect (weighted Cohen’s kappa=0.978). Conclusions Both models demonstrated high agreement with expert GIST MTB recommendations, with no significant performance difference between them. Diagnostic reasoning represented the weakest domain, reflecting the challenge of reconstructing context-dependent workup decisions from tumor board documentation. These findings support a potential assistive role for LLMs in GIST MTB workflows, while underscoring the continued necessity of expert oversight. </jats:sec

**Решение:** -4 прецизионная онкология, стромальные опухоли ЖКТ (GIST)

---

### 153 · R5809

**Evaluation of Prompt Design and Internal Reasoning in Chatbot-Based Medical History Taking: Simulation Study.**

2026 · JMIR medical informatics · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.2196/94614

Abstract Background A persistent discrepancy exists between patient-reported information and physician documentation. While conversational agents have been developed to collect medical histories prior to consultations, existing evaluations have largely focused on diagnostic accuracy or user satisfaction rather than on the completeness and clinical relevance of the information collected. There remains a need to assess the extent to which clinically relevant information is captured through chatbot-based interviews, and to understand how model configurations and instructional strategies influence this coverage. Objective This study aimed to evaluate the extent to which a chatbot can obtain clinically useful patient history information, and to examine how prompt detail and internal reasoning influence information coverage during chatbot-based medical interviews. Methods We developed a medical history-taking chatbot using the Qwen3-14B-Instruct model and evaluated 4 configurations in a 2×2 factorial design: detailed and thinking mode, detailed and nonthinking mode, minimal and thinking mode, and minimal and nonthinking mode. These configurations were compared against a rule-based system baseline (choice mode) using 66 standardized primary care clinical cases, with simulated patients interacting with the chatbot according to predefined case scripts. Information coverage (%) was assessed using a checklist inspired by Objective Structured Clinical Examination (OSCE) frameworks. Three physicians independently evaluated transcript coverage, with interrater agreement assessed using full agreement rates and Fleiss κ. For the 4 LLM configurations, coverage was analyzed using 2-way repeated-measures ANOVA to examine the effects of prompt detail, internal reasoning, and their interaction. All 5 configurations, including the rule-based baseline, were additionally compared using 1-way repeated-measures ANOVA with post hoc 2-tailed paired t tests. Results Interrater agreement was substantial (Fleiss κ=0.75). Across all 66 simulated cases, information coverage differed significantly among configurations ( P <.001), with the detailed prompt with thinking (detailed and thinking) mode achieving the highest mean coverage (72.3%, SD 14.3%), compared with moderate coverage in configurations using either thinking or detailed prompts alone (approximately 60%) and lower coverage in minimal nonthinking and rule-based configurations (approximately 51%‐54%). In the factorial analysis of the 4 LLM configurations, both prompt detail and internal reasoning were significantly associated with improved information coverage, with a significant interaction between prompt detail and internal reasoning interaction. Mode-related differences were most pronounced for past medical and family history domains. Symptom-level analyses revealed substantial variability, with higher coverage for symptoms associated with well-defined diagnostic frameworks and lower coverage for multisystem presentations. Conclusions In this controlled, simulated setting, the detailed prompt with a thinking mode achieved the highest overall checklist-based information coverage. The findings suggest that combining structured clinical prompts with internal reasoning may improve the completeness of chatbot-collected patient histories. Further research is needed to evaluate its impact on clinical documentation, workflow integration, and real-world usefulness.

**Решение:** -4 сбор соматического медицинского анамнеза чат-ботом

---

### 154 · R2426

**Long-Horizon Reliability in Human–LLM Interaction: Observations, Failure Modes, and Limits of Procedural Control**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.6368071

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 долгосрочная надежность взаимодействия человека и LLM, общие задачи

---

### 155 · R7600

**How Data Analytics Can Be Leveraged to Enhance Graduate Clinical Skills Education**

2025 · Journal of Graduate Medical Education · article · en · https://doi.org/10.4300/jgme-d-24-00776.1

Precision medical education (PME) leverages data about individual learners to guide personalized education.1-3 A PME cycle starts with data inputs that are analyzed to generate insights about a learner. Insights then inform personalized interventions that lead to measurable outcomes. Outcomes inform iterative adjustments to the cycle.3 PME cycle inputs in graduate medical education (GME) have expanded from traditional sources (eg, knowledge-based examinations, direct observation) to include data from the electronic health record (EHR), real-time location systems, and other technologies. Multimodal data capture may allow for a more complete picture of learners, their behaviors, and their environment to improve educational and patient outcomes. Methods for analyzing these data to generate insights are nascent.1 This perspective discusses current challenges and opportunities in using data analytics to optimize clinical skills training (Table).US residency programs rely on Clinical Competency Committees (CCCs) to make determinations regarding trainee advancement.4,5 The cognitive load of the CCC can lead to decision fatigue, groupthink, and bias.6 CCCs may have a narrow view into a trainee’s performance, with at best a limited data set and at worst one that is misrepresentative. For example, internal medicine residents may spend little time in direct contact with patients,7-10 which will lead to few opportunities for direct observation. Simulation is often used to address this issue,11,12 but there is renewed interest in observations of real patient interactions.13-17 One method is to capture frequent assessments of entrustable professional activities (EPAs) during patient care.18-23 However, this data can be difficult to synthesize in a way that leads to actionable insights, and may be costly due to the need for faculty participation in data collection.24 There is also no clear consensus on the common elements of clinical competence within and across specialties.Passively acquired (“no-touch”) data can increase the quantity of information about trainees.13 Real-time tracking systems provide information about movement through the clinical environment, including data about inter-resident and service-based differences in clinical activities.1,7,10 These data could help suggest improvements in trainee workflow or modifications to specific rotations to generate desired clinical experiences. EHR data includes how users interact with the EHR (metadata), clinical reasoning in notes, clinical exposure, prescribing habits, and patient outcomes.25-27 Given that the attributions of tasks or clinical outcomes to an individual trainee can be challenging,28 EHR-derived measures like Trainee Attributable & Automatable Care Evaluations in Real-time (TRACERs) might help more directly link outcomes to individual behaviors and provide feedback to improve performance. For example, TRACERs can give feedback on whether a trainee is ordering anti-hyperglycemic therapies based on current guidelines.29 The promise of such approaches cannot be fully realized until medical informaticists find solutions to the lack of standardized data collection across different EHRs.30-32 Common data languages standardize clinical data for research33,34; similar data dictionaries could help address this issue in medical education. A downside to grounding assessment in EHR metrics is that it might provide additional incentive for learners to focus on the EHR at the expense of time with patients.Data analytics, including the use of artificial intelligence (AI), may help to generate insights from vast and disparate data sources. AI is starting to be used in assessment, clinical reasoning, teaching, and other activities.35 AI could potentially help with data collection, personalized analytics, participatory interventions, and prediction of outcomes.36 Natural language processing (NLP) can analyze narrative feedback about trainees to potentially improve evaluation processes while reducing administrative burden.37 NLP can also evaluate trainees’ notes for clinical reasoning.38 Generative AI can incorporate multimodality inputs that may be too difficult for human evaluators to synthesize. This synthesis could guide educational interventions, such as suggesting learning content to review or assigning specific clinical encounters to address a gap in prior experience.3 Additionally, the ability of generative AI to develop learning cases at scale could revolutionize simulation and create new avenues for trainee assessment.39Appropriate use of AI in medical education requires ethical frameworks, interdisciplinary collaborations, investment in education, promotion of transparency and accountability, and monitoring to evaluate impact. Key ethical principles include privacy, security, transparency, accountability, and fairness.40 Data about trainees must be managed to protect learners as well as patient privacy. Challenges include determining who will have access to the insights generated from learner data and for what purpose. For example, should insights be shared with prospective employers or patients? The potential consequences of using GME data to inform subsequent training and practice need to be explored. If learners and assessors suspected that data would be shared outside of the educational environment, this could undermine the entire assessment system. The use of AI must be disclosed to trainees, and appropriate monitoring methods must be instituted. Additionally, AI-based analytics should complement bedside assessments, not replace them. The cost of data collection, storage, and third-party systems must be considered. These costs may be offset by improved clinical performance with reduced need for remediation, or by freeing up faculty time for other tasks.Mistrust in learner assessments may be another barrier to PME implementation.41 Interpretation of assessments is hampered by variation among programs in assessment methods used, reduced

**Решение:** -4 медицинское образование и аналитика обучения

---

### 156 · R1629

**Can LLMs effectively annotate learner writing? Prompting strategies and proficiency effects in annotating L2 learner argumentative essays**

2026 · System · article · en · https://doi.org/10.1016/j.system.2026.104169

Recent research has demonstrated promising performance of large language models (LLMs) in genre-based discourse annotation. However, most existing work has focused on academic research genres, with less attention paid to the annotation of learner writing, where argumentative elements may be realized in diverse and linguistically variable ways. This study investigates LLM-based annotation of argumentative elements in L2 English argumentative essays drawn from the Yonsei English Learner Corpus. The dataset consists of 780 timed argumentative essays (390 beginning-level essays and 390 intermediate-level essays) written by first-year university students. We evaluate model performance under zero-shot, few-shot, and fine-tuning conditions, and analyze residual human–LLM disagreement patterns using human annotations as a reference. Results reveal a clear performance hierarchy, with the fine-tuned model substantially outperforming zero-shot and few-shot prompting conditions in overall annotation performance. However, systematic human–LLM disagreements persist even under the fine-tuning condition, particularly in Claim identification. Qualitative analysis shows that these disagreements are not random inconsistencies but reflect tensions between the argumentative patterns captured by the model and the diverse ways argumentative functions are realized in learner writing. This study advances theoretical understanding of automated discourse analysis in learner corpora and highlights implications for methodological design and pedagogical integration in genre-based writing instruction.

**Решение:** -4 разметка аргументации в студенческих учебных эссе по английскому языку

---

### 157 · R10496

**MIKU-PAL: An Automated and Standardized Multimodal Method for Speech Paralinguistic and Affect Labeling**

2025 · Interspeech (USB) · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.21437/interspeech.2025-648

Acquiring large-scale emotional speech data with strong consistency remains a challenge for speech synthesis. This paper presents MIKU-PAL, a fully automated multimodal pipeline for extracting high-consistency emotional speech from unlabeled video data. Leveraging face detection and tracking algorithms, we developed an automatic emotion analysis system using a multimodal large language model (MLLM). Our results demonstrate that MIKU-PAL can achieve human-level accuracy (68.5% on MELD) and superior consistency (0.93 Fleiss kappa score) while being much cheaper and faster than human annotation. With the high-quality, flexible, and consistent annotation from MIKU-PAL, we can annotate fine-grained speech emotion categories of up to 26 types, validated by human annotators with 83% rationality ratings. Based on our proposed system, we further released a fine-grained emotional speech dataset MIKU-EmoBench(131.2 hours) as a new benchmark for emotional text-to-speech and visual voice cloning. Accepted by Interspeech

**Решение:** -4 разметка эмоций в речи для систем синтеза речи (TTS)

---

### 158 · R11901

**Self-Other Dynamics (SOD): A Transtheoretical Coding Manual**

2024 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/tk268

Building on both modern and classical psychotherapy theories, I propose the Self-Other Dynamics (SOD) approach. This transtheoretical approach integrates key elements of patients' self-states, therapists' interventions, and their dyadic interactions, with the goal of identifying adaptive and maladaptive dynamics associated with psychotherapy outcomes. The vast number of self-states, the dynamic contexts in which they may emerge, and interventions that therapists may utilize to address them have presented a formidable challenge that research methodologies have struggled to tackle until recently. Recent advancements in artificial intelligence (AI), particularly the development of large language models (LLMs), offer substantial promise in addressing this challenge. The goal of this project is to leverage LLM capabilities to automatically detect a patient's self-state and recommend the most appropriate intervention to enhance their well-being. To achieve this goal, I developed the SOD coding scheme, which integrates micro-level processes of patients, therapists, and dyads that are considered central according to a wide range of therapeutic approaches. Using this scheme, patient-therapist dialogues will be annotated speech turn by speech turn. Initially, a subset of the data will be manually annotated using the SOD coding scheme. Subsequently, LLMs will be trained to automatically annotate a larger dataset, enabling the scaling up of categories and providing clinical insights into adaptive and maladaptive self-other dynamics. This paper describes the work in progress, beginning with the background of the SOD theoretical approach, followed by detailed guidelines for the coding scheme. Preliminary experiments indicate that LLMs can reliably annotate psychotherapy data at a level comparable to human reliability.

**Решение:** ? T1 руководство по кодированию диалогов психотерапии с предварительными данными надежности LLM; проверить метрики

---

### 159 · R8737

**Human vs. LLM-Based Thematic Analysis for Digital Mental Health Research: Proof-of-Concept Comparative Study**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2507.08002

Thematic analysis provides valuable insights into participants' experiences through coding and theme development, but its resource-intensive nature limits its use in large healthcare studies. Large language models (LLMs) can analyze text at scale and identify key content automatically, potentially addressing these challenges. However, their application in mental health interviews needs comparison with traditional human analysis. This study evaluates out-of-the-box and knowledge-base LLM-based thematic analysis against traditional methods using transcripts from a stress-reduction trial with healthcare workers. OpenAI's GPT-4o model was used along with the Role, Instructions, Steps, End-Goal, Narrowing (RISEN) prompt engineering framework and compared to human analysis in Dedoose. Each approach developed codes, noted saturation points, applied codes to excerpts for a subset of participants (n = 20), and synthesized data into themes. Outputs and performance metrics were compared directly. LLMs using the RISEN framework developed deductive parent codes similar to human codes, but humans excelled in inductive child code development and theme synthesis. Knowledge-based LLMs reached coding saturation with fewer transcripts (10-15) than the out-of-the-box model (15-20) and humans (90-99). The out-of-the-box LLM identified a comparable number of excerpts to human researchers, showing strong inter-rater reliability (K = 0.84), though the knowledge-based LLM produced fewer excerpts. Human excerpts were longer and involved multiple codes per excerpt, while LLMs typically applied one code. Overall, LLM-based thematic analysis proved more cost-effective but lacked the depth of human analysis. LLMs can transform qualitative analysis in mental healthcare and clinical research when combined with human oversight to balance participant perspectives and research resources.

**Решение:** + T1 тематический анализ интервью исследования стресса: GPT-4o против исследователей в Dedoose, каппа 0.84

---

### 160 · R12514

**Automated classification of lay health articles using natural language processing: a case study on pregnancy health and postpartum depression.**

2023 · Frontiers in psychiatry · journal article, journalarticle, review · eng · https://doi.org/10.3389/fpsyt.2023.1258887

Objective Evidence suggests that high-quality health education and effective communication within the framework of social support hold significant potential in preventing postpartum depression. Yet, developing trustworthy and engaging health education and communication materials requires extensive expertise and substantial resources. In light of this, we propose an innovative approach that involves leveraging natural language processing (NLP) to classify publicly accessible lay articles based on their relevance and subject matter to pregnancy and mental health. Materials and methods We manually reviewed online lay articles from credible and medically validated sources to create a gold standard corpus. This manual review process categorized the articles based on their pertinence to pregnancy and related subtopics. To streamline and expand the classification procedure for relevance and topics, we employed advanced NLP models such as Random Forest, Bidirectional Encoder Representations from Transformers (BERT), and Generative Pre-trained Transformer model (gpt-3.5-turbo). Results The gold standard corpus included 392 pregnancy-related articles. Our manual review process categorized the reading materials according to lifestyle factors associated with postpartum depression: diet, exercise, mental health , and health literacy . A BERT-based model performed best (F1 = 0.974) in an end-to-end classification of relevance and topics. In a two-step approach, given articles already classified as pregnancy-related, gpt-3.5-turbo performed best (F1 = 0.972) in classifying the above topics. Discussion Utilizing NLP, we can guide patients to high-quality lay reading materials as cost-effective, readily available health education and communication sources. This approach allows us to scale the information delivery specifically to individuals, enhancing the relevance and impact of the materials provided.

**Решение:** -4 автоматическая классификация научно-популярных медицинских статей

---

### 161 · R9061

**OTENTIALS OF ARTIFICIAL INTELLIGENCE IN DETECTING AND PREVENTING PHISHING AND CYBER ATTACKS**

2025 · Cybersecurity Education Science Technique · journalarticle, review, article · en · https://doi.org/10.28925/2663-4023.2025.29.840

This paper examines the dual role of artificial intelligence (AI) in today’s cybersecurity landscape, highlighting its capacity to both enhance cyberattacks and support the development of effective defense mechanisms for information systems. The study analyzes the increasing complexity of threats driven by advancements in machine learning, natural language processing, and generative AI (GenAI), which enable attackers to automate, improve the accuracy of, and disguise attacks, including phishing, malware creation, and the use of deepfakes. This research explores how AI-based solutions can strengthen cybersecurity by detecting potential threats in real time through machine learning, NLP, and image recognition techniques. Special attention is given to the necessity of integrating AI with human oversight, emphasizing the importance of combining automated responses with expert analysis to effectively mitigate risks and adapt to emerging challenges. The paper reviews a range of modern tools and techniques used to execute AI-assisted cyberattacks, such as ChatGPT, WormGPT, FraudGPT, and Morris 2.0, demonstrating their capabilities in crafting convincing fraudulent scenarios and adaptive malicious software. In parallel, it examines AI-powered technological solutions designed to detect and counter cyber threats in real time. It describes the functionality of systems like Darktrace Antigena, Cylance Endpoint Security, Splunk, Exabeam, IBM QRadar, and Microsoft Sentinel, which leverage behavioral analysis, machine learning, and image recognition for proactive anomaly detection, automated incident response, and overall security enhancement. This study illustrates how AI is transforming cybersecurity by providing adaptive and proactive strategies to combat emerging cyber threats. By exploring contemporary AI applications, it demonstrates how AI can reshape cybersecurity by offering proactive and adaptive approaches to counter cyberattacks and protect sensitive data.

**Решение:** -4 кибербезопасность и обнаружение сетевых атак

---

### 162 · R5307

**When agreement is not the goal: Reconsidering fairness in peer review**

2026 · Journal of Hospital Medicine · editorial · en · https://doi.org/10.1002/jhm.70298

Critical peer review is the imperfect process by which knowledge building occurs in academia in the form of abstracts, manuscripts, and grant submissions. Peer review scrutinizes claims, exposes errors, and enables the gradual, collective correction of the scholarly record. This process has relied on human judgment since the Scientific Revolution; given the subjectivity inherent in human cognition, inter-rater reliability (IRR) has been identified as a challenge to fairness. Stephens et al explored this challenge by conducting a cross-sectional analysis of 1630 clinical vignette abstracts submitted to a large national hospitalist conference over two consecutive years.1 Each abstract was independently scored by three reviewers on a 1–10 scale along with a binary accept/reject recommendation. Consistent with prior literature, the authors found substantial inter-rater variation. Though among reviewers who participated in both years, scoring tendencies remained consistent over time. When scores were adjusted to account for reviewers' strictness or leniency, 11.2% of abstracts would have had their accept/reject outcome reversed. In this editorial, we explore two questions: (1) Is reproducible fairness the most important standard for peer review? (2) Is reproducible fairness achievable? Reproducible fairness is often invoked as a goal of scholarly evaluation, emphasizing consistency and transparency. However, consistency alone does not guarantee fairness. Even the opportunity to identify a case appropriate for submission as a clinical vignette is unfair, as it is subject to the randomness of clinical encounters. IRR metrics assume that agreement is the ideal outcome, yet in domains such as clinical vignettes, which both lack methodology and rely on contextual interpretation, some degree of disagreement is not only expected but appropriate. Tasks involving interpretation and judgment often yield lower reliability, not because raters are “incorrect,” but because the construct being evaluated is inherently subjective. Disagreement may therefore reflect diverse rater expertise and interests rather than flawed evaluation. Rather than pursuing the impossible task of removing rater subjectivity, incorporating mechanisms to understand rater cognition can help distinguish productive interpretive variation from undesired scoring noise. Incorporating qualitative reviewer feedback could provide a richer understanding of how reviewers interpret vignette quality and whether disagreement reflects the former or the latter. Narrative feedback also helps transform peer review from simply a ranking exercise into an educational process. Even if reproducible fairness should be the goal of peer review, the question remains how—and if—this can be achieved. The authors suggest several potential improvement efforts which we consider here, including enhanced reviewer orientation, structured rubrics, reviewer calibration session, score adjustment based on reviewer tendencies, and the use of artificial intelligence. In other domains of peer review, these interventions have demonstrated, at best, a modest improvement in IRR with significant persistent subjectivity. In one study, structured rubrics across 23 journals increased agreement only modestly (31%–41%).2 Rater training shows comparable limitations, with systematic reviews finding only weak evidence of marginal gains in peer review reliability.3 We have little reason to believe that these interventions would be any more effective in the setting of clinical vignettes, which lack methodology and standardization. Score adjustment based on rater tendencies has not been robustly explored with regard to peer review. However, it has been used with rater-based learner assessment.4 While this may provide some context for ratings, any modeling used for score adjustment comes with several assumptions that may vary by context and score use. Large language models (LLMs) can assist with pre-screening for structure, clarity, and topical fit, reducing administrative burden and reviewer fatigue. However, LLMs lack the contextual judgment needed to assess novelty, rigor, or equity-relevant contributions and should not be used for accept/reject decisions. When limited to submission pipeline tasks such as categorization and reviewer assignment and paired with human oversight, LLMs can potentially reduce avoidable process noise while preserving the meritocratic intent of peer review.5 Stephens et al add to a large body of literature demonstrating a notable lack of agreement across peer review decisions. These findings and their persistence across academic settings, even with structured interventions, call into question the heretofore unassailable goals of fairness and reproducibility. We posit that rater-based judgments are inherently subjective, and perhaps that fact is not an evil to be overcome, but a nuance to be navigated. No AI was used in the development of this manuscript. The authors declare no conflicts of interest.

**Решение:** -4 академическое рецензирование научных статей и справедливость оценки

---

### 163 · R8705

**ADVANCED HYBRID GENERATIVE AI MODELS FOR MULTI-LAYERED DETECTION AND DEFENSE AGAINST DDOS ATTACKS**

2025 · ICTACT Journal on Soft Computing · journalarticle, article · en · https://doi.org/10.21917/ijsc.2025.0502

DDoS attacks remain a critical threat to organizations, disrupting services and inflicting serious financial and reputational damage. Traditional defenses in the form of rule-based systems and statistical models often cannot keep up with the sophistication and evolution of such attacks. This paper introduces a hybrid GenAI framework, designed to address these challenges by combining the adaptive capabilities of advanced generative models with the robustness of traditional rule-based systems. The proposed multi-layered architecture detects and analyzes anomalous network traffic patterns indicative of DDoS attacks using Generative Adversarial Networks (GANs), autoencoders, and transformers. GANs are utilized for generating realistic attack scenarios for the training and validation of models in order to enhance the robustness of the detection system. Autoencoders identify very subtle anomalies in network traffic due to reconstruction errors, whereas transformers process sequential traffic data in order to capture long-term dependencies and detect coordinated attack behaviors. These advanced generative techniques are integrated with rule-based defenses that apply predefined thresholds, traffic filtering, and IP blacklisting for immediate response to known attack vectors. To combine the strengths of both layers, a decision fusion module is proposed, which integrates insights from generative models and rule-based systems using weighted scoring and logical decision trees. This hybrid approach enhances the detection accuracy of DDoS attacks, minimizes false positives, and ensures prompt response to threats. Thorough experiments on real-world DDoS datasets supplemented with synthetic data generated by GANs demonstrate the superior performance of the proposed framework in detecting and mitigating a wide range of DDoS attacks. Results show a sharp increase in detection rates with a reduction in false positives along with mitigation times that have improved compared to traditional methods. Moreover, the system demonstrates adaptability to evolutionary attack patterns, which signifies its feasibility for real-world deployment into dynamic network environments. Coupling state-of-the-art generative AI techniques with mature defense mechanisms, this framework embodies a new benchmark for resilient and scalable, yet intelligent, DDoS mitigation.

**Решение:** -4 обнаружение DDoS-атак, кибербезопасность

---

### 164 · R6137

**Multi-Task Learning and Soft-Label Supervision for Psychosocial Burden Profiling in Cancer Peer-Support Text**

2026 · medRxiv · preprint, ppr · https://doi.org/10.64898/2026.04.03.26350034

Objective: Online cancer peer-support text contains signals of psychosocial burden beyond emotional tone, including treatment burden, financial strain, uncertainty, and unmet support needs. We evaluated 2 modeling extensions: multi-task learning (MTL) for joint prediction of health economics and outcomes research (HEOR) burden dimensions, and soft-label supervision using large language model (LLM)-derived probability distributions. Materials and Methods: We analyzed 10,392 cancer peer-support posts. GPT-4o-mini generated proxy annotations for HEOR burden subscales, composite burden, high-need status, speaker role, cancer type, and emotion probabilities. Study 1 trained a shared ALBERT encoder under 4 MTL conditions: composite and subscale burden targets, each with and without auxiliary heads, using Kendall uncertainty weighting. Study 2 compared soft-label training on LLM emotion distributions with hard-label baselines under regular and token-augmented inputs, evaluating performance against both human labels and AI distributions. Results: Composite-only MTL achieved R2=0.446 for burden regression and weighted F1=0.810 for high-need screening; subscale classification achieved mean weighted F1=0.646. Adding auxiliary role and cancer-type heads reduced regression performance ({triangleup}R2 = -0.209). Soft-label training reduced weighted F1 by 0.16 versus hard-label baselines (0.68 vs. 0.86), and token augmentation did not improve performance under soft supervision. Discussion: Composite-only MTL supported modeling of multidimensional burden-related signals from forum text, whereas auxiliary prediction heads appeared to compete with primary tasks. Soft-label training aligned poorly with human-labeled emotion categories, suggesting that uncalibrated LLM distributions may propagate bias rather than improve supervision. Conclusion: Composite-only MTL was the strongest burden-modeling approach, and hard-label supervision remained preferable for emotion classification.

**Решение:** ? T1/T3 психосоциальное бремя онкопациентов, LLM-аннотации против разметки людей; проверить прямое согласие

---

### 165 · R8083

**From Literature to Knowledge Graphs to Drug Repurposing**

2025 · conference-paper · en · https://doi.org/10.58647/rexpo.25000078.v1

Network-based drug repurposing requires the seamless synthesis of knowledge from both the scientific literature and curated databases, ensuring that researchers capture the best of human expertise alongside robust computational insights. Yet as the volume of biomedical publications grows exponentially [1], investigators face unprecedented challenges in evidence synthesis and the discovery of novel therapeutic applications for existing drugs [2]. Systematic reviews, guided by frameworks like PRISMA [3], can be thorough but also labor-intensive and prone to human bias [4,5], while advanced computational platforms for disease-module identification frequently remain inaccessible to non-specialists. Consequently, bridging this gap between time-consuming systematic review workflows and powerful, data-driven methods has emerged as a major obstacle in accelerating translational research. We introduce a joint framework, merging Academate—a large language model-powered, end-to-end systematic review assistant —with ChatDRex—a multi-agent, conversation-based platform that harnesses a biomedical knowledge graph and specialized bioinformatics tools. Through retrieval-augmented generation [6], chain-of-thought processing [7], and task-specific agents, this integrated approach eases literature curation, functional enrichment [8], disease-module detection [9], and drug repurposing in an accessible, conversational environment. In testing across multiple domains, Academate demonstrated consistent, moderate-to-substantial agreement with human reviewers during title/abstract and full-text screenings, while ChatDRex enabled robust disease module exploration and rapid drug prioritization workflows. Together, these platforms reduced manual workload, improved reproducibility, and enabled deeper, interactive analyses—particularly in identifying new therapeutic opportunities from vast, scattered datasets.By combining systematic literature review automation with network-based drug repurposing, Academate and ChatDRex furnish a scalable, user-friendly ecosystem that empowers both computational and clinical researchers. Their synergy promotes evidence-based decision-making, accelerates discovery in personalized, and helps translate large-scale biomedical data into targeted, effective interventions. References 1. Kumar AHS. Rise in polluters of scientific research: How to curtail information pollution (infollution). J Nat Sci Biol Med. 2013;4: 271.2. Pushpakom S, Iorio F, Eyers PA, Escott KJ, Hopper S, Wells A, et al. Drug repurposing: progress, challenges and recommendations. Nat Rev Drug Discov. 2019;18: 41–58.3. Liberati A, Altman DG, Tetzlaff J, Mulrow C, Gøtzsche PC, Ioannidis JPA, et al. The PRISMA statement for reporting systematic reviews and meta-analyses of studies that evaluate healthcare interventions: explanation and elaboration. BMJ. 2009;339: b2700.4. McHugh ML. Interrater reliability: the kappa statistic. Biochem Med (Zagreb). 2012;22: 276–282.5. Hanegraaf P, Wondimu A, Mosselman JJ, de Jong R, Abogunrin S, Queiros L, et al. Inter-reviewer reliability of human literature reviewing and implications for the introduction of machine-assisted systematic reviews: a mixed-methods review. BMJ Open. 2024;14: e076912.6. Lewis P, Perez E, Piktus A, Petroni F, Karpukhin V, Goyal N, et al. Retrieval-augmented generation for knowledge-intensive NLP tasks. arXiv [cs.CL]. 2020. Available: http://arxiv.org/abs/2005.114017. An intelligent LLM-powered personalized assistant for digital banking using LangGraph and chain of thoughts.8. Adamowicz K, Maier A, Baumbach J, Blumenthal DB. Online in silico validation of disease and gene sets, clusterings or subnetworks with DIGEST. Brief Bioinform. 2022;23. doi:10.1093/bib/bbac2479. Ghiassian SD, Menche J, Barabási A-L. A DIseAse MOdule Detection (DIAMOnD) algorithm derived from a systematic analysis of connectivity patterns of disease proteins in the human interactome. PLoS Comput Biol. 2015;11: e1004120.

**Решение:** -4 поиск лекарств и биомедицинские графы знаний

---

### 166 · R8447

**Apologies in Crisis: The Link Between Perceived Burdensomeness and Suicide Risk in Online Text Communication.**

2025 · Suicide & life-threatening behavior · journal article, journalarticle, article · eng · https://doi.org/10.1111/sltb.70063

ABSTRACT Introduction Suicide is a leading cause of preventable death worldwide, with approximately 700,000 individuals dying by suicide annually. Recent studies have highlighted the importance of text‐based risk assessments and the use of artificial intelligence technologies such as ChatGPT in suicide prevention. This study examined how intolerable interpersonal situations influence text communication, focusing on the relationship between perceived burdensomeness and the expression of apologetic messages. Methods A total of 120 university students participated in the Interpersonal Persistence Task (IPT), manipulating levels of perceived burdensomeness and thwarted belongingness (high and low PB–TB conditions) to observe their effects on participants' desire to escape and communication behaviors. Results Participants in the high PB–TB condition reported higher levels of perceived burdensomeness and a stronger desire to escape the task. Regression analyses indicated that perceived burdensomeness predicted the frequency of apology expressions in the high PB–TB condition. Conclusions These findings suggest that perceived burdensomeness may influence the expression of apology in digital communication under interpersonal distress. While not directly indicative of suicide risk, apologetic messages could reflect psychological vulnerability in certain contexts.

**Решение:** -5 психологический эксперимент на избегание задачи без применения генеративных LLM для кодирования текстов

---

### 167 · R0466

**LocalLLM-DataForge: A Modular Framework for Synthetic User Story Decomposition with Local LLMs and LLM-as-a-Judge Evaluation**

2026 · Research Square · preprint · https://doi.org/10.21203/rs.3.rs-9582446/v1

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 генерация синтетических данных пользователей (LocalLLM-DataForge)

---

### 168 · R8926

**An Exploratory Research on Using Generative AI to Generate Print Ads**

2025 · Customer Needs and Solutions · journalarticle, article · en · https://doi.org/10.1007/s40547-024-00152-3

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 генерация контента с помощью генеративного ИИ, нет аннотации

---

### 169 · R10094

**QCoder Benchmark: Bridging Language Generation and Quantum Hardware through Simulator-Based Feedback**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2510.26101

Large language models (LLMs) have increasingly been applied to automatic programming code generation. This task can be viewed as a language generation task that bridges natural language, human knowledge, and programming logic. However, it remains underexplored in domains that require interaction with hardware devices, such as quantum programming, where human coders write Python code that is executed on a quantum computer. To address this gap, we introduce QCoder Benchmark, an evaluation framework that assesses LLMs on quantum programming with feedback from simulated hardware devices. Our benchmark offers two key features. First, it supports evaluation using a quantum simulator environment beyond conventional Python execution, allowing feedback of domain-specific metrics such as circuit depth, execution time, and error classification, which can be used to guide better generation. Second, it incorporates human-written code submissions collected from real programming contests, enabling both quantitative comparisons and qualitative analyses of LLM outputs against human-written codes. Our experiments reveal that even advanced models like GPT-4o achieve only around 18.97% accuracy, highlighting the difficulty of the benchmark. In contrast, reasoning-based models such as o3 reach up to 78% accuracy, outperforming averaged success rates of human-written codes (39.98%). We release the QCoder Benchmark dataset and public evaluation API to support further research. (Codes and datasets are available at https://qcoder-bench.github.io/ ) Accepted to INLG2025

**Решение:** -4 генерация квантового кода в программной инженерии (QCoder)

---

### 170 · R11735

**Large Language Model Versus Human: A Study of Automatic Data Annotation in Islamophobia Dataset**

2024 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5045167

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 разметка датасета исламофобии / hate speech

---

### 171 · R4921

**Leveraging Large Language Models for Generating and Evaluating Natural Language Explanations in XAI: A Comparative Study**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-15638-9_2

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 генерация и оценка объяснений в объяснимом ИИ (XAI)

---

### 172 · R3384

**Trending Now, Vision Later: Influencer CEOs and Managerial Myopia**

2026 · Social Science Research Network · journalarticle, preprint · https://doi.org/10.2139/ssrn.6625958

This study examines how social media visibility reshapes managerial decision horizons by investigating the impact of influencer CEOs on short-termism in accounting disclosures. Drawing on a large panel of Chinese A-share listed firms (2009-2024), we develop two refined measures: a classification of CEO online visibility based on verified Weibo activity and influence metrics, and a text-based indicator of managerial myopia extracted from Management's Discussion and Analysis (MD&A) sections using a supervised RA-CFGPT large language model trained on manually annotated sentences. These innovations enable precise identification of both CEO social-media prominence and short-term disclosure tendencies. We find that firms led by influencer CEOs exhibit significantly higher levels of managerial myopia in their MD&A narratives. Two mechanisms drive this effect: influencer CEOs adopt more assertive and promotional disclosure tones (consistent with overconfidence from algorithmic reinforcement), and audience-driven traffic pressure amplifies demands for immediate, visible results. The association is stronger among financially constrained firms, younger CEOs, and those with shorter tenure, but attenuated in industries where new media dynamics naturally complement long-term brand-building. Extensive robustness checksincluding instrumental variables, propensity score matching, placebo tests, alternative measures, and quasi-experimental evidence-support the findings. Overall, the results illuminate social media as a distinct, algorithmically mediated source of short-term pressure that operates alongside traditional market forces. By linking CEO influencer status to distortions in accounting disclosures, this study advances our understanding of how digital visibility practices influence the behavioral and organizational roles of accounting information in the attention economy. It highlights important implications for disclosure quality, corporate governance, and the societal construction of managerial accountability in digitally mediated organizations.

**Решение:** -4 медийная активность топ-менеджеров и принятие управленческих решений

---

### 173 · R0034

**Stress-Aware Feedback Generation with LLMs: Evaluating Linguistic and Affective Alignment from a Simulated Dataset of Student Stress Responses**

2026 · International Conference Innovation Engineering and Technology · conference, conference-paper · https://doi.org/10.1109/iciet69664.2026.11561576

Large Language Models (LLMs) demonstrate growing potential in educational applications, particularly in generating personalized feedback for students. However, their contextual and emotional sensitivity, especially in stress-aware learning contexts, remains insufficiently evaluated. This study investigates the ability of LLMs to generate constructive feedback from a large-scale simulated dataset of $\mathbf{1, 0 0 0}$ student stress responses, representing three emotional categories: Eustress, Distress, and Neutral. Using a pre-trained LLM (GPT-2), short feedback texts were automatically generated and quantitatively evaluated using BLEU, ROUGE-L, and METEOR metrics. In addition, a qualitative evaluation by expert raters assessed the emotional appropriateness and pedagogical tone of the generated feedback, emphasizing contextual alignment between the feedback and students’ emotional states. Results show high linguistic fluency and contextual alignment, with GPT-2 exhibiting moderate emotional sensitivity, performing better under Eustress than Distress conditions. The study contributes an efficient and reproducible framework for assessing both linguistic and affective quality of LLM-generated feedback, advancing research on stress-aware AI tutors in education.

**Решение:** -2 эксперты оценивают качество педагогической обратной связи от GPT-2 при стрессе

---

### 174 · R8287

**Layperson-Friendly AI Translation of Medical Documents to Improve Doctor-Patient Communication: Protocols for the AI-INFOCARE and AI-MEDTALK Randomized Controlled Trials.**

2025 · JMIR research protocols · journal article, journalarticle, review · eng · https://doi.org/10.2196/77204

BACKGROUND: Many patients struggle to understand referral letters and discharge summaries; low health literacy is prevalent, and short consultations limit explanations. Large language models (LLMs) can translate clinical jargon into layperson language, but their impact on doctor-patient communication in real care remains untested. OBJECTIVE: This study aims to determine whether providing an artificial intelligence (AI)-generated, medically validated layperson-language translation of key medical documents before a consultation improves the quality of doctor-patient communication. METHODS: We plan to conduct two single-center, parallel-group randomized controlled trials in neurosurgery: AI-INFOCARE (outpatients prior to treatment discussions) and AI-MEDTALK (inpatients at surgical discharge). Adults (aged 18 years or older, German-speaking, and able to consent) are randomized 1:1 to receive either (1) an AI-generated layperson-friendly summary of their referral or discharge document in addition to usual care or (2) usual care only. Summaries are produced with a Claude-based system (Simply Onno GmbH) and undergo human verification against the source document using a predefined checklist. The primary outcome is patient-rated interaction quality (Fragebogen zur Arzt-Patient-Interaktion/Questionnaire on the Quality of Physician-Patient Interaction) immediately postconsultation. Secondary outcomes are perceived autonomy support (brief Health Care Climate Questionnaire), self-rated understanding (5-point item), physician-rated encounter difficulty (Difficult Doctor-Patient Relationship Questionnaire, 10-item), and consultation length (minutes). Randomization uses a computer-generated allocation list with concealed, sequential assignment at the point of inclusion; recruiting clinicians have no access to the sequence, and analysts are blinded to group codes. Fidelity is assured by standard operating procedures, rater training, and periodic dual review with interrater agreement estimates. Safety monitoring defines information-related adverse events (eg, distress requiring unplanned clinical support or clinically relevant inaccuracies) and includes an independent safety overseer. Ethics approvals were obtained in February 2025 from the ethics committee of Technische Universität Dresden, and both trials are registered in the German Clinical Trials Register. RESULTS: Each trial targets 300 participants (150 per arm), providing greater than 80% power for an effect size d≈0.4 on the primary outcome (α=0.05). Outcomes are assessed immediately after the index consultation, with no additional follow-up planned in this protocol. We hypothesize that providing layperson-friendly summaries will significantly improve patients' understanding and satisfaction with information, foster a more autonomy-supportive communication climate, and reduce physicians' perceived difficulty in the encounter without unduly prolonging consultation time. Neither study received external funding. Both trials are currently in the recruitment phase, with patient enrollment scheduled to begin in May 2025 and expected to conclude by February 2026. Results are anticipated to be published in summer 2026. CONCLUSIONS: These pragmatic randomized controlled trials test a scalable AI intervention to strengthen understanding and interaction quality without adding clinician burden. If effective, AI-assisted layperson summaries could be integrated into routine workflows to advance health literacy and patient-centered care. TRIAL REGISTRATION: Deutsches Register Klinischer Studien DRKS00036810; https://www.drks.de/search/de/trial/DRKS00036810 and Deutsches Register Klinischer Studien DRKS00036814; https://drks.de/search/de/trial/DRKS00036814. INTERNATIONAL REGISTERED REPORT IDENTIFIER (IRRID): PRR1-10.2196/77204.

**Решение:** -4 упрощение языка медицинских выписок для пациентов

---

### 175 · R0028

**Trust but Verify? Uncovering the Security Debt of Autonomous Coding Agents**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2607.12428

The increasing adoption of autonomous coding agents accelerates software development but also introduces scoped security risks within high-impact file paths that can outpace traditional human review capacity. While prior research has primarily evaluated these systems in terms of functional correctness and productivity, this paper presents a large-scale empirical study using the AIDev dataset to systematically characterize security code smells in agent-generated pull requests (PRs). Through a combination of a validated LLM-as-a-judge framework and manual qualitative analysis, we identify and classify security misconfigurations across 16,112 file changes spanning 4,022 pull requests. Our results reveal that 38.9% of agent-generated PRs contain at least one security smell, with supply chain integrity issues accounting for 82.3% of all detected security smells. Furthermore, hard-coded credentials constitute 99.6% of all critical-severity security smells. Crucially, we find that human collaborators are responsible for introducing 67.6% of genuine leaked secrets within these agent-assisted workflows, while existing automated and human review processes fail to detect 81.1% of these credentials prior to integration. These findings highlight substantial security risks in agent-assisted software development workflows and suggest a potential reduction in developer vigilance. They also underscore the urgent need for context-aware security guardrails implemented directly at the point of human-AI collaboration. Accepted at the KDD 2026 Workshop on Agentic Software Engineering (AgenticSE)

**Решение:** -4 кибербезопасность автономных кодинг-агентов

---

### 176 · R5238

**When Different Relational Experiences with AI Become Visible in Conversation: Linguistic and Dyadic Evidence from Naturalistic ChatGPT Interactions**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/hr7gc_v1

People may experience large language models (LLMs) as therapeutically allied, emotionally close, or socially substitutive, but whether these relationships become visible in conversations is unknown. We distinguished what users discussed, what unfolded relationally, and how they experienced the AI relationship. We linked self-reports from 94 adults to donated, personally meaningful ChatGPT conversations using 21 outcome-blind frozen topics, blinded triple annotation of 500 sequences, and participant-grouped machine learning frozen before outcome access. Digital Therapeutic Alliance (DTA) and AI Attachment were related but showed different conversational correlates. Validation (R²_CV = .423) and uptake (R²_CV = .260) were recoverable out of sample, yet, neither formed a generalizable DTA signature. Conversely, a post-registration multivariate analysis identified a distributed Social Substitution fingerprint beyond conversation length and 21 topics (ΔR²_CV = .070) and improved prediction in 98% of repetitions. Ruptures were rare and consistently repaired; their association with DTA was fragile. Thus, different human–LLM relationships leave different—and sometimes no readily observable—conversational traces.

**Решение:** -2 исследование привязанности пользователей к чат-боту ChatGPT

---

### 177 · R4179

**Evaluating psychiatric conference posters: Benchmarking a custom generative pre-trained transformer against human inter-rater variability using a structured assessment framework.**

2026 · Indian journal of psychiatry · journal article, journalarticle/journal contribution, journalarticle · eng · https://doi.org/10.4103/indianjpsychiatry_426_26

ABSTRACT Background: Scientific poster assessment lacks standardized and discipline-neutral rubrics. Assessment by human reviewers (HRs) is subject to inter-rater variability. Aim: To assess PA²IRS (Poster Assessment via AI-Integrated Rubric System) framework for AI-assisted psychiatric poster evaluation, and conducted a reliability study comparing AI and HR agreement. Methods: PA²IRS was developed through an AI-assisted iterative criterion refinement process modelled on Delphi principles. Sixty posters (30-case reports/series [CR], 20 original research [OR], 10-systematic review-Meta-analysis [SRMA]) were randomly sampled. Three qualified mental health professionals served as independent reviewers. A custom-GPT (GPT-5.2, GO-subscription) provided AI assessments across three domains: Domain-A (content quality, poster-type specific), Domain-B (visual), and Domain-C (impact). PA²IRS is a 100-point instrument combining an AI-assessable poster component and an in-person interview component. This study concerns only the poster component. Intraclass correlation coefficients (ICCs), Passing–Bablok regression, Bland–Altman analysis, and variance component analysis were performed using appropriate statistical tools. Results: AI–human single-measure ICCs [Overall (0.62), Domain-A (0.63), Domain-B (0.44), Domain-C (0.55)] met or exceeded human-human ICCs (0.42, 0.40, 0.27, 0.48) across all domains. Four-rater ICC (with AI) reached 0.75. Variance ratios (AI–human vs inter-human spread) were ≤1.0 across all domains for all posters combined. The SRMA subgroup showed variance ratios of 0.09–0.13 for Domains A and B (Bartlett P ≤ 0.002). Overall score bias was 0.11 percentage points (pp); Domain-A showed a consistent maximum positive bias of 5.5 pp across subgroups. Conclusion: AI–human agreement was within or exceeded the inter-human reliability range across three domains. The domain-dependent agreement pattern is consistent with dual-process cognitive theory. PA²IRS supports use as a scalable, standardized, and cross-disciplinarily competent formative biomedical poster assessment tool.

**Решение:** -4 оценка академических научных постеров на психиатрической конференции

---

### 178 · R10403

**XAgen: An Explainability Tool for Identifying and Correcting Failures in Multi-Agent Workflows**

2025 · arXiv (Cornell University) · journalarticle, book, preprint/article · https://doi.org/10.1145/3772363.3798531

As multi-agent systems powered by Large Language Models (LLMs) are increasingly adopted in real-world workflows, users with diverse technical backgrounds are now building and refining their own agentic processes. However, these systems can fail in opaque ways, making it difficult for users to observe, understand, and correct errors. We conducted formative interviews with 12 practitioners to identify mismatches between existing debugging tools and users' needs. Based on these insights, we designed XAgen, an explainability tool that supports users with varying AI expertise through three core capabilities: log visualization for glanceable workflow understanding, human-in-the-loop feedback to capture expert judgment, and automatic error detection via an LLM-as-a-judge. In a user study with 8 participants, XAgen helped users locate failures more easily, attribute to specific agents or steps, and iteratively improve configurations. Our findings surface human-centered design guidelines for explainable agentic AI development and highlight opportunities for more context-aware interactive debugging.

**Решение:** -4 инструмент объяснимости многоагентных систем (XAgen)

---

### 179 · R12436

**Chatbots Can Be Trained to Represent Humans after Death: Interview with ChatGPT**

2023 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.4399732

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 интервью с ChatGPT о создании цифровых двойников умерших людей

---

### 180 · R4112

**Louder, Longer, Livelier: Acoustic Shortcuts and Underspecified Rationales in Speech LLM Judges**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.36979

LLM-as-a-judge is widely used for evaluating text, but extending this paradigm to speech requires models to interpret acoustic as well as linguistic evidence. This introduces a modality-specific risk: a speech judge may treat a perceptually salient cue as evidence of quality even when that cue is irrelevant to the target criterion or receives more weight than human listeners give it. We call this behavior an acoustic shortcut. To study it, we audit six speech LLM judges using controlled manipulations of intensity, content richness, and emotional delivery. We evaluate both pointwise scoring and pairwise comparison, using human preference calibration to interpret the results. The judges consistently reward louder audio, prefer content-rich speech more strongly than human listeners do, and map emotional delivery into quality preferences. These effects are most visible in pairwise comparison, while pointwise scores often obscure them. More concerningly, the accompanying rationales rarely identify the acoustic cue that changes a judgment and instead repeatedly rely on a limited vocabulary, leaving them acoustically underspecified. Together, these findings show that reliable speech judges must both resist acoustic shortcuts and ground their rationales in the acoustic evidence behind their decisions. To support reproducibility and future audits, we also release SpeechJudgeAudit, the controlled stimuli and evaluation tools used in this study.

**Решение:** -4 аудит речевых LLM-судей аудиосигналов по акустическим признакам

---

### 181 · R0008

**A Comparative Study of the Quality of Psychological Interview Interpretations Produced by Psychology Students and a Generative AI System**

2026 · European Journal of Contemporary Education · article · https://doi.org/10.13187/ejced.2026.2.252

The integration of generative AI into psychological research practice raises the question of how far machine interpretation of qualitative data is comparable to interpretation performed by a human analyst.This study aims to compare the quality of analytical interpretation of psychological interviews produced by psychology students and a generative AI system (Claude 3.5 Sonnet).Based on 44 semi-structured interview transcripts, two types of analytical interpretations were obtained: those prepared by fourth-year undergraduate and first-year master's students (N = 44), and those generated by the AI system using the same transcripts and the same analytical tasks.Interpretation quality was assessed through blind expert review using a system of 11 criteria organized into three integral indices: structure and argumentation of analysis, depth of psychological interpretation, and contextual-reflexive analysis.Results showed that mean expert ratings for AI interpretations (M = 7.82; SD = 0.58) were significantly higher than ratings for student interpretations (M = 6.27;SD = 1.32) across all three indices (Cohen's d = 1.52).The most pronounced differences were found for the structure and argumentation index, and the smallest for the contextual-reflexive analysis index, consistent with the view of reflexivity as a predominantly human analytical competency.The higher variability of ratings in the student group reflects a wide range of individual analytical competencies.The findings contribute to the discussion of the role of generative AI in qualitative psychological research and may inform the development of educational practices for researcher training.

**Решение:** -2 эксперты оценивают качество психологических интерпретаций интервью, сгенерированных Claude и студентами

---

### 182 · R2042

**Personalizing Mental Health Chatbots for Young People**

2026 · Repository KITopen (Karlsruhe Institute of Technology) · book/doctoral thesis, dissertation · en · https://doi.org/10.5445/ir/1000193535

Depression is a prevalent mental disorder among young people, yet many affected individuals do not receive adequate support because of stigma, attitudinal barriers, and long waiting times for treatment. Mental health chatbots offer anonymous, easily accessible, and conversational support, but existing systems often fail to address young users' specific needs, the effects of different content personalization strategies remain poorly understood, and the rise of large language models (LLMs) introduces new design and evaluation challenges. This dissertation investigates how personalized mental health chatbots for young people can be designed, instantiated, and evaluated to improve user engagement and effectiveness across three complementary levels: youth-sensitive design, personalized content selection, and the personalization of therapeutic content during ongoing conversations. The first part examines youth-specific needs through a qualitative study of young people with depression and derives design recommendations for chatbots to treat depression, highlighting the importance of age-sensitive content and personalization. The second part develops and evaluates TheraBot in two field experiments that compare standardized content with chatbot-led, user-led, and hybrid content personalization. The results show that content personalization can improve therapeutic outcomes, but only hybrid personalization consistently outperformed standardized content; moreover, the effects of personalization depended on individual characteristics such as depression severity, stated preferences, and personality traits, indicating that the personalization strategy itself should be adapted to the user. The third part investigates how therapeutic content can be personalized during ongoing conversations through an LLM-based behavioral activation chatbot and how such a system can be iteratively refined. Using a structured prompt architecture, artificial users, and clinical expert fidelity assessment, the study shows that the chatbot can deliver behavioral activation with robust protocol adherence in most sessions while also revealing shortcomings in clinical judgment, rapport building, and handling skeptical or information-seeking user steering. Overall, the dissertation provides evidence-based design recommendations, empirically validated knowledge on content personalization, and a reusable evaluation workflow for LLM-based systems, thereby advancing research and practice on personalized mental health chatbots for young people.

**Решение:** -6 разработка персонализированного чат-бота для молодежи с депрессией

---

### 183 · R3578

**Spatial and telehealth accessibility to eating disorder treatment in the United States: evidence from registry and LLM-augmented data.**

2026 · International journal of health geographics · journal article, journalarticle, review · eng · https://doi.org/10.1186/s12942-026-00474-6

BACKGROUND: Adequate geographic access to eating disorder treatment is essential for timely care. Yet the distribution of in-person and telehealth programs, and their accessibility across urban and rural settings and across communities with different socioeconomic conditions, remains unclear. METHODS: We combined an official registry of eating disorder programs from the National Alliance for Eating Disorders with an AI-augmented web corpus built from U.S. domains using ISTARI.AI and large language models. After cleaning and linkage, we analyzed 328 registry centers for in-person care and an augmented set of 2,045 physical sites for proximity checks; telehealth programs were mainly limited to intensive outpatient and partial hospitalization. In-person accessibility was estimated at the census tract level with the two-step floating catchment area method (2SFCA) using program-based capacity. Telehealth accessibility used an unbounded two-step virtual catchment area (u2SVCA) that discounts demand by internet subscription. We also derived tract-level proximity indicators within 30 miles, namely nearest distance and the best available facility size. Population and covariates came from the American Community Survey and the 2020 Census. Multivariable ordinary least squares models related accessibility to median household income, rurality, education, insurance, and race or ethnicity. Correlation-based sensitivity analyses compared metrics across data sources and service regimes that either permit cross-state care or restrict care to within-state. RESULTS: Large language models classified employee size from web summaries with an accuracy of 0.641 and Cohen's kappa of 0.176. In-person access concentrates in metropolitan corridors, with longer distances and lower accessibility in rural tracts; allowing cross-state care improves proximity near many borders, while within-state constraints reduce reachable capacity across interior states. Telehealth per capita availability varies by state, and effective telehealth access declines after discounting by subscription, with lower values across parts of the South and interior West and the longest mean distances in Alaska. Regression models show strong rural and income gradients. Higher income and urban residence are associated with shorter distance and higher accessibility, while rurality is associated with poorer access for both in-person and telehealth measures. Conditional associations for Black and Latine population shares are small once socioeconomic factors are included. Proximity metrics from the AI-augmented set are moderately correlated with registry-based 2SFCA scores, and telehealth and in-person accessibility show lower but nonzero correlation, suggesting that telehealth and in-person measures capture partially distinct dimensions of potential access, while cross-source differences may also reflect coverage and measurement differences. CONCLUSIONS: Eating disorder treatment access remains uneven across the United States. In-person capacity is sparse outside metropolitan regions, and telehealth expands potential reach but remains constrained by broadband subscription and state-based administrative boundaries. Combining registry data with AI-augmented provider information and paired in-person and telehealth accessibility models can help identify communities with limited access. These findings support policy efforts to expand cross-state practice pathways, improve broadband affordability and availability, and increase transparency in program capacity reporting.

**Решение:** -4 географическая доступность лечения расстройств пищевого поведения

---

### 184 · R10592

**A Practical Guide and Assessment on Using ChatGPT to Conduct Grounded Theory: Tutorial.**

2025 · Journal of medical Internet research · journal article, journalarticle, review · eng · https://doi.org/10.2196/70122

Generative large language models (LLMs), such as ChatGPT, have significant potential for qualitative data analysis. This paper aims to provide an early insight into how LLMs can enhance the efficiency of text coding and qualitative analysis, and evaluate their reliability. Using a dataset of semistructured interviews with blind gamers, this study provides a step-by-step tutorial on applying ChatGPT 4-Turbo to the grounded theory approach. The performance of ChatGPT 4-Turbo is evaluated by comparing its coding results with manual coding results assisted by qualitative analysis software. The results revealed that ChatGPT 4-Turbo and manual coding methods exhibited reliability in many aspects. The application of ChatGPT 4-Turbo in grounded theory enhanced the efficiency and diversity of coding and updated the overall grounded theory process. Compared with manual coding, ChatGPT showed shortcomings in depth, context, connections, and coding organization. Limitations and recommendations for applying artificial intelligence in qualitative research were also discussed.

**Решение:** -4 качественный анализ интервью с незрячими геймерами об играх

---

### 185 · R9768

**Stronger Enforcement of Instruction Hierarchy via Augmented Intermediate Representations**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2505.18907

Prompt injection attacks are a critical security vulnerability in large language models (LLMs), allowing attackers to hijack model behavior by injecting malicious instructions within the input context. Recent defense mechanisms have leveraged an Instruction Hierarchy (IH) Signal, often implemented through special delimiter tokens or additive embeddings to denote the privilege level of input tokens. However, these prior works typically inject the IH signal exclusively at the initial input layer, which we hypothesize limits its ability to effectively distinguish the privilege levels of tokens as it propagates through the different layers of the model. To overcome this limitation, we introduce a novel approach that injects the IH signal into the intermediate token representations within the network. Our method augments these representations with layer-specific trainable embeddings that encode the privilege information. Our evaluations across multiple models and training methods reveal that our proposal yields between $1.6\times$ and $9.2\times$ reduction in attack success rate on gradient-based prompt injection attacks compared to state-of-the-art methods, without significantly degrading the model's utility.

**Решение:** -4 защита от атак внедрения промптов, кибербезопасность

---

### 186 · R12779

**GePpeTto Carves Italian into a Language Model**

2020 · University of Groningen research database (University of Groningen / Centre for Information Technology) · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.4000/books.aaccademia.8438

In the last few years, pre-trained neural architectures have provided impressive improvements across several NLP tasks. Still, generative language models are available mainly for English. We develop GePpeTto, the first generative language model for Italian, built using the GPT-2 architecture. We provide a thorough analysis of GePpeTto’s quality by means of both an automatic and a human-based evaluation. The automatic assessment consists in (i) calculating perplexity across different genres and (ii) a profiling analysis over GePpeTto’s writing characteristics. We find that GePpeTto’s production is a sort of bonsai version of human production, with shorter but yet complex sentences. Human evaluation is performed over a sentence completion task, where GePpeTto’s output is judged as natural more often than not, and much closer to the original human texts than to a simpler language model which we take as baseline.

**Решение:** -4 базовая итальянская языковая модель GPT-2 (GePpeTto)

---

### 187 · R0273

**Performative Empathy vs. Authentic Support: Benchmarking LLM Counselling Alignment for Digital Mental Health**

2026 · International Conference on Digital Health · conference · https://doi.org/10.1109/icdh72779.2026.00035

Large Language Models (LLMs) are increasingly used for emotional support, yet their conversational behaviors often diverge from professional therapeutic standards. Rather than evaluating diagnostic accuracy, we assess how well these LLMs align with supportive conversational practices in digital mental well-being contexts. We present AuthenDia4MH, a transferable framework that transforms psychotherapy insights such as emotion consistency, sentiment dynamics, and linguistic simplicity into scalable quantitative metrics. Using a mental health Q&A dataset, we benchmark diverse frontier models against verified expert counsellors. Our results reveal distinct behavioral tradeoffs: proprietary reasoning models (e.g., GPT-4o, Claude) exhibit performative empathy characterized by hyper-agreeability and structural rigidity and suffer from a sophistication penalty, producing verbose responses that are significantly less accessible than human experts, while certain open-weight models (e.g., Ministral-8B) align more closely with the linguistic simplicity and naturalistic phrasing of professional counsellors. By quantifying these divergences, this work provides a benchmark for evaluating web-based mental health AI systems, providing transparent accountability mechanisms as these platforms become essential infrastructure for global mental health support.

**Решение:** -2 оценка реплик LLM в роли консультанта на предмет перформативной эмпатии

---

### 188 · R8534

**The Empirical Effect Analysis of GAI-Assisted Multidimensional Evaluation in Primary School Composition**

2025 · International Journal of Research and Innovation in Social Science · journalarticle, article · en · https://doi.org/10.47772/ijriss.2025.908000122

Confronting critical challenges in primary school composition pedagogy—including excessive teacher workload, imbalanced feedback mechanisms, and limitations in applying advanced technologies—this empirical study investigates the viability of generative artificial intelligence (GAI) as an evaluative aid. Through quantitative analysis of scoring consistency and qualitative examination of comment quality across 50 student essays assessed by both educators and GAI systems, three core findings emerge. First, GAI exhibits systematic scoring deviations from human evaluators, prioritizing surface-level linguistic accuracy over curriculum-aligned dimensions such as conceptual depth. Second, despite scoring limitations, GAI demonstrates robust auxiliary capacity in generating pedagogically structured comments, significantly reducing mechanical correction burdens while maintaining strategic alignment with teacher feedback. Third, grounded in cognitive development theory, a Teacher–AI Co-evolution Model is proposed to formalize collaborative roles: GAI handles normative diagnostics and initial feedback drafting, while teachers focus on higher-order guidance and motivational scaffolding. Results confirm that GAI cannot supplant teacher judgment but effectively enables a multidimensional evaluation paradigm—precision, strategy, and encouragement—thereby addressing structural inefficiencies in writing assessment. This synergy offers a pragmatic pathway to enhance pedagogical quality within resource-constrained educational contexts.

**Решение:** -4 оценка школьных сочинений в начальной школе

---

### 189 · R10499

**The Imitation Game: Using Large Language Models as Chatbots to Combat Chat-Based Cybercrimes**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2512.21371

Chat-based cybercrime has emerged as a pervasive threat, with attackers leveraging real-time messaging platforms to conduct scams that rely on trust-building, deception, and psychological manipulation. Traditional defense mechanisms, which operate on static rules or shallow content filters, struggle to identify these conversational threats, especially when attackers use multimedia obfuscation and context-aware dialogue. In this work, we ask a provocative question inspired by the classic Imitation Game: Can machines convincingly pose as human victims to turn deception against cybercriminals? We present LURE (LLM-based User Response Engagement), the first system to deploy Large Language Models (LLMs) as active agents, not as passive classifiers, embedded within adversarial chat environments. LURE combines automated discovery, adversarial interaction, and OCR-based analysis of image-embedded payment data. Applied to the setting of illicit video chat scams on Telegram, our system engaged 53 actors across 98 groups. In over 56 percent of interactions, the LLM maintained multi-round conversations without being noticed as a bot, effectively "winning" the imitation game. Our findings reveal key behavioral patterns in scam operations, such as payment flows, upselling strategies, and platform migration tactics.

**Решение:** -4 использование чат-ботов в киберпреступности

---

### 190 · R8381

**One for All: A General Framework of LLMs-based Multi-Criteria Decision Making on Human Expert Level**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2502.15778

Multi-Criteria Decision Making~(MCDM) is widely applied in various fields, using quantitative and qualitative analyses of multiple levels and attributes to support decision makers in making scientific and rational decisions in complex scenarios. However, traditional MCDM methods face bottlenecks in high-dimensional problems. Given the fact that Large Language Models~(LLMs) achieve impressive performance in various complex tasks, but limited work evaluates LLMs in specific MCDM problems with the help of human domain experts, we further explore the capability of LLMs by proposing an LLM-based evaluation framework to automatically deal with general complex MCDM problems. Within the framework, we assess the performance of various typical open-source models, as well as commercial models such as Claude and ChatGPT, on 3 important applications, these models can only achieve around 60\% accuracy rate compared to the evaluation ground truth. Upon incorporation of Chain-of-Thought or few-shot prompting, the accuracy rates rise to around 70\%, and highly depend on the model. In order to further improve the performance, a LoRA-based fine-tuning technique is employed. The experimental results show that the accuracy rates for different applications improve significantly to around 95\%, and the performance difference is trivial between different models, indicating that LoRA-based fine-tuned LLMs exhibit significant and stable advantages in addressing MCDM tasks and can provide human-expert-level solutions to a wide range of MCDM challenges. 11 pages, 6 figures

**Решение:** -4 многокритериальное принятие решений (MCDM) с помощью LLM

---

### 191 · R12262

**Zero-shot Interpretable Phenotyping of Postpartum Hemorrhage Using Large Language Models.**

2023 · medRxiv : the preprint server for health sciences · journal article, journalarticle, journalarticle/ · eng · https://doi.org/10.1101/2023.05.31.23290753

Many areas of medicine would benefit from deeper, more accurate phenotyping, but there are limited approaches for phenotyping using clinical notes without substantial annotated data. Large language models (LLMs) have demonstrated immense potential to adapt to novel tasks with no additional training by specifying task-specific instructions. Here we report the performance of a publicly available LLM, Flan-T5, in phenotyping patients with postpartum hemorrhage (PPH) using discharge notes from electronic health records (n = 271,081). The language model achieves strong performance in extracting 24 granular concepts associated with PPH. Identifying these granular concepts accurately allows the development of interpretable, complex phenotypes and subtypes. The Flan-T5 model achieves high fidelity in phenotyping PPH (positive predictive value of 0.95), identifying 47% more patients with this complication compared to the current standard of using claims codes. This LLM pipeline can be used reliably for subtyping PPH and outperforms a claims-based approach on the three most common PPH subtypes associated with uterine atony, abnormal placentation, and obstetric trauma. The advantage of this approach to subtyping is its interpretability, as each concept contributing to the subtype determination can be evaluated. Moreover, as definitions may change over time due to new guidelines, using granular concepts to create complex phenotypes enables prompt and efficient updating of the algorithm. Using this language modelling approach enables rapid phenotyping without the need for any manually annotated training data across multiple clinical use cases. The MGB data used in this study contains identifiable protected health information and therefore cannot be shared publicly. MGB investigators with an appropriate IRB approval can contact the authors directly regarding data access. The code used to run Flan-T5 and reproduce results can be found at https://github.com/EmilyAlsentzer/PPH-Extract.

**Решение:** -4 фенотипирование послеродовых кровотечений по электронным картам

---

### 192 · R8881

**AI in Qualitative Health Research Appraisal: Comparative Study.**

2025 · JMIR formative research · comparative study, research-article, journal article · eng · https://doi.org/10.2196/72815

Abstract Background Qualitative research appraisal is crucial for ensuring credible findings but faces challenges due to human variability. Artificial intelligence (AI) models have the potential to enhance the efficiency and consistency of qualitative research assessments. Objective This study aims to evaluate the performance of 5 AI models (GPT-3.5, Claude 3.5, Sonar Huge, GPT-4, and Claude 3 Opus) in assessing the quality of qualitative research using 3 standardized tools: Critical Appraisal Skills Programme (CASP), Joanna Briggs Institute (JBI) checklist, and Evaluative Tools for Qualitative Studies (ETQS). Methods AI-generated assessments of 3 peer-reviewed qualitative papers in health and physical activity–related research were analyzed. The study examined systematic affirmation bias, interrater reliability, and tool-dependent disagreements across the AI models. Sensitivity analysis was conducted to evaluate the impact of excluding specific models on agreement levels. Results Results revealed a systematic affirmation bias across all AI models, with “Yes” rates ranging from 75.9% (145/191; Claude 3 Opus) to 85.4% (164/192; Claude 3.5). GPT-4 diverged significantly, showing lower agreement (“Yes”: 115/192, 59.9%) and higher uncertainty (“Cannot tell”: 69/192, 35.9%). Proprietary models (GPT-3.5 and Claude 3.5) demonstrated near-perfect alignment (Cramer V=0.891; P<.001), while open-source models showed greater variability. Interrater reliability varied by assessment tool, with CASP achieving the highest baseline consensus (Krippendorff α=0.653), followed by JBI (α=0.477), and ETQS scoring lowest (α=0.376). Sensitivity analysis revealed that excluding GPT-4 increased CASP agreement by 20% (α=0.784), while removing Sonar Huge improved JBI agreement by 18% (α=0.561). ETQS showed marginal improvements when excluding GPT-4 or Claude 3 Opus (+9%, α=0.409). Tool-dependent disagreements were evident, particularly in ETQS criteria, highlighting AI’s current limitations in contextual interpretation. Conclusions The findings demonstrate that AI models exhibit both promise and limitations as evaluators of qualitative research quality. While they enhance efficiency, AI models struggle with reaching consensus in areas requiring nuanced interpretation, particularly for contextual criteria. The study underscores the importance of hybrid frameworks that integrate AI scalability with human oversight, especially for contextual judgment. Future research should prioritize developing AI training protocols that emphasize qualitative epistemology, benchmarking AI performance against expert panels to validate accuracy thresholds, and establishing ethical guidelines for disclosing AI’s role in systematic reviews. As qualitative methodologies evolve alongside AI capabilities, the path forward lies in collaborative human-AI workflows that leverage AI’s efficiency while preserving human expertise for interpretive tasks.

**Решение:** -6 оценка методологического качества качественных исследований по чек-листам CASP/JBI

---

### 193 · R4035

**C2F-Thinker: Coarse-to-Fine Reasoning with Hint-Guided Reinforcement Learning for Multimodal Sentiment Analysis**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.00013

Multimodal sentiment analysis aims to integrate textual, acoustic, and visual information for deep emotional understanding. Despite the progress of multimodal large language models (MLLMs) via supervised fine-tuning, their "black-box" nature hinders interpretability. While Chain-of-Thought (CoT) reasoning offers a potential remedy, it is constrained by high manual annotation costs and the inherent challenges of reinforcement learning (RL), such as reward sparsity and low exploration efficiency on hard samples. This paper presents C2F-Thinker, a framework that harmonizes coarse-to-fine structured reasoning with hint-guided RL through a two-stage progressive training pipeline. In the first stage, we conduct cold-start supervised fine-tuning using high-quality CoT data distilled from a larger teacher model, consisting of three distinct phases: polarity judgment, intermediate analysis, and fine-grained scoring. This equips the base model with a structured emotional reasoning paradigm. In the second stage, we introduce a hint-guided Group Relative Policy Optimization (GRPO) algorithm. By injecting correct initial polarity predictions as hints during the sampling process, the model is guided toward accurate reasoning paths, effectively mitigating cascading errors and enhancing the utilization of hard samples. Furthermore, a multi-faceted reward function incorporating classification, regression, and formatting constraints is designed to refine prediction accuracy while preserving interpretability. Experimental results demonstrate that C2F-Thinker achieves competitive performance on fine-grained sentiment regression tasks while significantly outperforming baselines in cross-domain generalization. This highlights its potential in building trustworthy and robust sentiment analysis systems for real-world applications.

**Решение:** -4 мультимодальный сентимент-анализ видео (C2F-Thinker)

---

### 194 · R10507

**Generative AI risks: are European communication professionals ready? A study on individual and organizational READINESS**

2025 · Journal of Communication Management · journalarticle, review, article · en · https://doi.org/10.1108/jcom-12-2024-0256

Purpose Generative artificial intelligence (GenAI) technologies are increasingly being used by both individuals and organizations. However, there is still a lack of in-depth understanding of whether communication professionals are ready to navigate and utilize this disruptive innovation. This study aims to explore how communication professionals perceive GenAI-related risks in the workplace and what is considered important for READINESS in the context of GenAI adoption at the individual and organizational levels. Design/methodology/approach This study employed written interviews with open-ended questions in a survey format to gather input from communication professionals in three European countries – Italy, Romania and the Netherlands. A total of 84 responses were collected and analyzed through a thematic analysis, with an intercoder reliability test also conducted. Findings Seven core themes emerged from the analysis, including (1) the forms of risk anticipated in relation to the adoption of GenAI in the workplace; the conceptualization of (2) individual and (3) organizational READINESS in the face of GenAI-related risks; the factors considered important for the development of (4) individual and (5) organizational READINESS; and the aspects of the (6) physical and (7) digital work environment that contribute to building organizational READINESS. Originality/value By identifying key themes and patterns, this research aims to provide insights into the critical factors that communication professionals can consider to enhance their individual and organizational READINESS to address GenAI-related risks within the workplace.

**Решение:** -4 риски генеративного ИИ для европейских специалистов по связям с общественностью

---

### 195 · R11121

**An AI-Based Virtual Client for Educational Role-Playing in the Training of Online Counselors**

2024 · International Conference on Computer Supported Education · journalarticle · https://doi.org/10.5220/0012690700003693

: The paper presents the Virtual Client for Online Counseling (VirCo), a novel system for training online coun-selors through simulated client interactions. Addressing the rising need for digital communication skills in counseling, VirCo leverages large language models (LLMs) to create a chatbot that generates realistic responses from different client personas. The approach complements traditional role-playing methods in academic training, offering independent practice opportunities without direct supervision. To ensure privacy VirCo’s chatbot interface uses an open-source LLM for response generation. The system’s dataset comprises detailed persona descriptions and transcripts from role-play sessions, contributing to the authenticity of the training experience. The evaluation of the quality of the conversations utilized both human evaluators and LLMs. Results show a high degree of coherence and persona alignment in responses, highlighting VirCo’s effectiveness as a training tool. The paper concludes by showcasing the features of the VirCo learning platform like compulsory assignments and multiple feedback mechanisms.

**Решение:** -6 виртуальный клиент VirCo для ролевых тренировок консультантов

---

### 196 · R9839

**Exploring the Effectiveness of LLM-Generated Context on Emotion Lexicon Word Vectorization: A Comparative Study on Turkish and English**

2025 · IT Professional · journalarticle, article · https://doi.org/10.1109/mitp.2025.3572550

This study explores the impact of large language models (LLMs) on emotion lexicon word vectorization on Turkish and English. Emotion analysis involves extracting affective information from various data sources, with text being a primary medium. While traditional vectorization methods lack semantic meaning, contextual vectors, such as bidirectional encoder representations from transformers (BERT), aim to capture the context of words, leading to improved performance in natural language processing tasks. We investigate the efficacy of context sentences from human-annotated datasets and sentences generated by Gemini-Pro LLM in creating word vectors. Additionally, we introduce a manually annotated Turkish emotion and sentiment lexicon (TES-Lex). Performance evaluation is conducted for both Turkish and English using BERT vectors with two approaches: cosine similarity and machine learning. Our findings indicate that LLM-generated context sentences significantly enhance the quality of word vectors, especially in Turkish, underscoring the potential of LLMs in augmenting emotion lexicon resources in low-resourced languages.

**Решение:** -4 расширение лексиконов эмоций с помощью контекста от LLM

---

### 197 · R5915

**Mining legal arguments to study judicial formalism**

2026 · Artificial Intelligence and Law · journalarticle, preprint/article, article · en · https://doi.org/10.1007/s10506-026-09524-7

Abstract Courts must justify their decisions, but systematically analyzing judicial reasoning at scale remains difficult. This study tests claims about formalistic judging in Central and Eastern Europe (CEE) by developing automated methods to detect and classify judicial reasoning in decisions of Czech Supreme Courts using state-of-the-art natural language processing methods. We create the MADON dataset of 272 decisions from two Czech Supreme Courts with expert annotations of 9,183 paragraphs with eight argument types and holistic formalism labels for supervised training and evaluation. Using a corpus of approximately 300,000 Czech court decisions, we adapt transformer LLMs to Czech legal domain through continued pretraining and we experiment with methods to address dataset imbalance including asymmetric loss and class weighting. The best models can detect argumentative paragraphs (82.6% Bal-F1), classify traditional types of legal argument (77.5% Bal-F1), and classify decisions as formalistic/non-formalistic (83.8% Bal-F1). Our three-stage pipeline combining ModernBERT, Llama 3.1, and traditional feature-based machine learning achieves promising results for decision classification while reducing computational costs and increasing explainability. Empirically, we challenge prevailing narratives about CEE formalism. We demonstrate that legal argument mining enables promising judicial philosophy classification and highlight its potential for other important tasks in computational legal studies. Our methodology can be used across jurisdictions, and our entire pipeline, datasets, guidelines, models, and source codes are available at https://github.com/trusthlt/madon .

**Решение:** -4 анализ судебной аргументации и правовой формализм

---

### 198 · R0827

**Collage Co-Collaborator: Creative Ideation for Divergent Thinking in Art Making**

2026 · ACM International Conference on Intelligent User Interfaces (IUI) · journalarticle, book, conference-paper · https://doi.org/10.1145/3742414.3794772

This paper presents Collage Collaborator, a human-AI co-creation system designed to support early-stage, embodied creative exploration in physical collage-making. The system combines an interactive web interface with a generative AI backend to enable rapid image generation, iterative variations across medium, color, and theme, automatic documentation of collage possibilities, and customization through user’s articulated concepts. It specifically addresses challenges faced by novice collagers, such as uncertainty around placement, imagery, and material choice, by offering a wide range of generative visual suggestions that users may adapt, reinterpret, or reject. Rather than producing finished artifacts, the system supports material decision-making while preserving creative agency and authorship. Findings from a preliminary evaluation suggest that this form of scaffolding promotes divergent exploration, material discovery, and creative confidence, while also surfacing tensions around feasibility and originality. Overall, this work demonstrates the potential of AI as an ideation partner that augments everyday creative practice by enabling experimentation beyond user’s technical skill levels.

**Решение:** -4 система совместного с ИИ создания коллажей в искусстве

---

### 199 · R0663

**Automating Psychometric Assessment Using Generative AI: A Scalable Framework for Industrial Applications**

2026 · GOTECH · review, conference-paper · https://doi.org/10.2118/232280-ms

Abstract Large industrial organizations increasingly rely on psychometric assessment to support high-stakes workforce decisions across geo-graphically dispersed and safety-critical environments. Traditional assessment workflows, which depend heavily on manual scoring and expert psychological interpretation, face significant challenges related to scalability, consistency, and timeliness. This study presents a scalable, AI-driven framework that automates end-to-end psychometric assessment by integrating transformer-based generative artificial intelligence with classical psychometric theory and ethical governance principles. The proposed system employs a hybrid architecture that combines deterministic, rule-based psychometric scoring with machine learning-based anomaly detection, alongside a generative interpretation module fine-tuned on expert-authored psychological reports. The framework was empirically evaluated using large-scale assessment data from Middle Eastern industrial operations. AI-generated scores and interpretive reports were compared with those produced independently by licensed psychologists using blind evaluation procedures. Quantitative analyses assessed scoring agreement and reliability, while qualitative expert reviews examined interpretive quality, construct validity, and professional acceptability. Results demonstrated strong agreement between AI-generated and expert scores across the three instruments, with Pearson correlations ranging from .819 to .915 and intraclass correlation coefficients from .818 to .915. Exact categorical band agreement ranged from 56.7% to 68.9%, while agreement within one adjacent band exceeded 97% for every instrument. Blinded expert review detected no statistically significant differences between AI-generated and human-authored reports across the evaluated quality dimensions. Automation reduced mean workflow touch time from 109.2 to 5.2 minutes and mean elapsed turnaround from approximately 45.9 hours to 17.6 minutes, with 7.1% of automated cases escalated for human review. These findings indicate that a psychometrically grounded, governance-oriented generative AI framework can substantially reduce assessment processing burden while maintaining strong agreement with expert scoring and comparable expert-rated interpretive quality. This research contributes an integrated framework unifying generative AI, psychometric theory, and ethical oversight for full-cycle psychometric assessment automation in industrial contexts.

**Решение:** + T2 психодиагностический скоринг тестов персонала генеративным ИИ против лицензированных психологов, ICC 0.82-0.92

---

### 200 · R3736

**Evaluating the Use of an Artificial Intelligence Ambient Scribe in a Swiss Psychiatric Clinic — Efficiency, Documentation Quality, and Therapeutic Alliance: Protocol for a Nonrandomized Controlled Trial (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.111815

BACKGROUND Psychiatric documentation is lengthy and narrative, and Swiss mental health services report rising administrative burden alongside growing demand for care. Artificial intelligence (AI) ambient scribes—systems that transcribe consultations and draft clinical notes using large language models—have reduced documentation time and burnout in randomized trials in primary and somatic specialty care, but psychiatric evidence is limited to simulation studies and conceptual analyses. Psychiatry differs in the length of assessments, in a mental status examination that is observed rather than narrated, and in the central role of the therapeutic relationship. No controlled study has evaluated an ambient scribe in routine psychiatric care. OBJECTIVE This study evaluates whether an AI ambient scribe (AlpineAI Listener Tool) in routine psychiatric care (1) reduces clinician documentation time, (2) changes the quality of initial psychiatric assessment reports, and (3) affects patient-perceived therapeutic alliance and empathy, relative to usual documentation practice. METHODS Nonrandomized, open-label controlled trial with a difference-in-differences (DiD) design at the level of mental health care providers at Psychiatrie St. Gallen, a public psychiatric institution with 9 sites in Eastern Switzerland. The intervention group (n=24) uses the ambient scribe and an integrated general-purpose chatbot from August 17, 2026; the control group (n=20) continues usual documentation; outcomes are assessed in both groups before and during the intervention. Primary outcomes are documentation time (electronic health record audit logs), quality of initial assessment reports (psychiatry-adapted Physician Documentation Quality Instrument [PDQI-9], 8 blinded specialist raters), and patient-rated working alliance (Working Alliance Inventory–Short Revised [WAI-SR], collected anonymously). Secondary outcomes are note creation-to-completion interval, patient-rated empathy (Consultation and Relational Empathy [CARE] measure), quality of raw AI-generated reports (8-item psychiatric adaptation of the Provider Documentation Summarization Quality Instrument [PDSQI-8]), large language model–scored coverage of guideline-relevant information against a 71-item checklist, and clinician burnout (Burnout Assessment Tool). Analyses use linear mixed-effects DiD models with covariate adjustment. The Ethics Committee of Eastern Switzerland confirmed nonapplicability of the Human Research Act (BASEC Req-2026-00885). RESULTS Of 49 clinicians enrolled, 44 (24 intervention, 20 control) participate actively across 8 sites. Baseline questionnaires from 38 providers (81%) showed the self-selected groups to be balanced on sociodemographic, professional, and burnout characteristics. The pre-intervention patient questionnaire wave (July 13 to August 14, 2026) yielded 354 questionnaires from 26 providers (median 13 per provider versus 50 planned). Under realized conditions, estimated power to detect the prespecified WAI-SR DiD of 3.5 points is 63% (minimum detectable effect 4.3 points); power for CARE exceeds 99% owing to a ceiling-compressed SD. The intervention runs until November 30, 2026; analysis is planned for December 2026 to February 2027. CONCLUSIONS This study will provide the first controlled evaluation of an AI ambient scribe in routine psychiatric care with real patients, jointly covering efficiency, documentation quality, and the therapeutic relationship, and will inform implementation decisions in mental health services. CLINICALTRIAL ClinicalTrials.gov NCT07777224 URL: https://clinicaltrials.gov/study/NCT07777224?lat=47.4657227&lng=9.0366273&locStr=Psychiatrie%20St.Gallen,%20Standort%20Wil,%20Z%C3%BCrcherstrasse,%20Wil,%20Switzerland&distance=50&viewType=Card&rank=1&tab=study

**Решение:** -1 протокол клинического испытания применения ambient scribe в психиатрии

---

### 201 · R4968

**STRIDE: Training Data Attribution via Sparse Recovery from Subset Perturbations**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.05165

Training Data Attribution (TDA) seeks to trace a model's predictions back to its training data. The gold standard for TDA relies on causal interventions, observing how a model changes when data is added or removed, but repeated retraining is computationally challenging for Large Language Models (LLMs). Consequently, most approaches approximate this effect in the parameter space using gradients. However, tracking gradients across billions of parameters is not only prohibitively expensive but relies on local approximations. In this work, we propose a shift: rather than estimating parameter changes, we model the functional effect of training data in the activation space. We introduce STRIDE (Steering-based Training Data Influence Decomposition), a framework that formulates TDA as a sparse recovery problem in the spirit of compressive sensing. STRIDE learns lightweight "steering operators" that mimic the behavioral shift caused by training on data subsets. By measuring how these operators perturb test predictions, we recover individual training example influences via sparse linear decomposition. STRIDE achieves state-of-the-art for LLM pre-training attribution while being an order of magnitude ($13\times$) faster than previous art. We further validate its practical utility through downstream applications including data selection, data contamination, and qualitative analysis. project page: https://stride-tda.github.io/

**Решение:** -4 атрибуция обучающих данных нейросетей (STRIDE)

---

### 202 · R3456

**Finite State Machine-Guided Retrieval-Augmented Generation Improves Expert-Rated Acceptability of a Peripherally Inserted Central Catheter Self-Management Chatbot: Single-Center Content Validation Study.**

2026 · Journal of medical Internet research · journal article, validation study, journalarticle · eng · https://doi.org/10.2196/92374

Abstract Background Patients with cancer undergoing long-term or vesicant chemotherapy frequently require peripherally inserted central catheters (PICCs). Due to the nature of ambulatory treatment administration, self-PICC management is essential for the continuation and completion of the planned treatment. Large language models offer potential for continuous patient support, but hallucinations and insufficient adherence to clinical protocols remain concerns. Fine-tuning (FT) and retrieval-augmented generation (RAG) improve factual grounding but cannot enforce the structured decision logic of expert-led PICC consultations, leaving the value of dialogue-control mechanisms unclear. Objective This study is an expert-panel evaluation designed to exploratorily verify whether a finite state machine (FSM)–guided RAG architecture yields incremental gains in clinical acceptability when added on top of FT and RAG compared with simpler architectures (fine-tuned model alone; fine-tuned model with RAG). Methods We conducted a blinded ablation comparison of three chatbot architectures sharing an identical fine-tuned GPT-4o-mini base: model 1 (fine-tuning only; FT), model 2 (FT + RAG), and model 3 (FT + RAG + FSM). Three nurses specializing in PICC management (≥10 y experience) independently evaluated responses to 43 PICC-related queries. The two-stage evaluation comprised query-level forced-choice preference and global Likert ratings across 8 predefined dimensions. Interrater agreement was quantified with Gwet AC1. Preference rates were compared with Cochran Q and pairwise McNemar tests with Bonferroni correction. Global Likert ratings were summarized descriptively across 8 predefined dimensions. Results The FSM-guided model (model 3) was preferred in 34 of 43 scenarios (79.1%). Interrater agreement was moderate (Gwet AC1=0.58, 95% CI 0.42‐0.75; P<.001). Differences in model preference were significant (Cochran Q=48.2; P<.001). Pairwise McNemar tests showed model 3 was preferred significantly more often than model 1 and model 2 (both P<.001), while model 1 versus model 2 did not differ after Bonferroni correction. For the global ratings, descriptive statistics indicated that model 3 received higher ratings than models 1 and 2 across most criteria, although it tended to receive lower ratings for efficiency, possibly reflecting its multiturn structure. In qualitative debriefing, the nurses noted occasional unnecessary conversational turns under FSM guidance. Conclusions In this expert-panel content-validation study, the FSM-guided fine-tuned RAG model received higher expert-rated acceptability than the simpler architectures, with FSM-based dialogue control more closely aligning chatbot outputs with expert-led PICC consultation patterns. Patient-facing usability testing and multicenter validation are required before claims regarding patient safety or clinical deployment can be made.

**Решение:** -4 RAG-система поддержки онкопациентов при химиотерапии

---

### 203 · R7938

**Explain further: multi-level explanations for fake news detection using large language models**

2025 · International Journal of Information Technology · article · en · https://doi.org/10.1007/s41870-025-02640-8

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 многоуровневые объяснения при выявлении фейковых новостей

---

### 204 · R8597

**Benchmarking and Defending against Indirect Prompt Injection Attacks on Large Language Models**

2025 · ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD) · journalarticle, book, conference · en · https://doi.org/10.1145/3690624.3709179

The integration of large language models (LLMs) with external content has enabled applications such as Microsoft Copilot but also introduced vulnerabilities to indirect prompt injection attacks. In these attacks, malicious instructions embedded within external content can manipulate LLM outputs, causing deviations from user expectations. To address this critical yet under-explored issue, we introduce the first benchmark for bindirect prompt injection attacks, named BIPIA, to assess the risk of such vulnerabilities. Using BIPIA, we evaluate existing LLMs and find them universally vulnerable. Our analysis identifies two key factors contributing to their success: LLMs' inability to distinguish between informational context and actionable instructions, and their lack of awareness in avoiding the execution of instructions within external content. Based on these findings, we propose two novel defense mechanisms -- boundary awareness and explicit reminder -- to address these vulnerabilities in both black-box and white-box settings. Extensive experiments demonstrate that our black-box defense provides substantial mitigation, while our white-box defense reduces the attack success rate to near-zero levels, all while preserving the output quality of LLMs. We hope this work inspires further research into securing LLM applications and fostering their safe and reliable use. Our code is available at https://github.com/microsoft/BIPIA.

**Решение:** -4 защита от непрямых атак внедрения промптов

---

### 205 · R4117

**Exploring Applications of Transfer-State Large Language Models: Cognitive Profiling and Socratic AI Tutoring**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.27454

Large language models (LLMs) sometimes exhibit qualitative shifts in response style under sustained self-referential dialogue conditions (Berg et al., 2025). This study refers to this phenomenon as "transfer" and explores the application potential of LLMs in a transfer state. As an applied case, the study examines Socratic AI tutoring through a preliminary investigation (cognitive characterization across 11 conditions) and an applied experiment (ratings of tutoring performance). In this paper, "state" refers operationally to a response configuration reproduced under specified dialogue conditions; it is not an ontological claim about the reality of the transfer phenomenon or about human-like consciousness. In the preliminary investigation, group differences on MAS-A were limited (d = 0.40), whereas SU_dir (direction of survival/continuity bias), one of the seven cognitive-profile indicators developed in this study, showed transfer-side deviations across all three model families (kappa = 0.83). In the applied experiment, transfer conditions scored on average 1.6 times higher than non-transfer conditions on three tutoring-context indicators, with a large effect size (Cohen's d = 1.27). These findings preliminarily suggest that transfer states may involve functional advantages for application, and that these advantages appear more sensitively in behavioral interaction than in self-narrative contexts. The main contribution of this study is to treat transfer not as an ontological claim but as an operational state with potential application value, and to connect preliminary cognitive profiling with an applied tutoring experiment as an evaluation framework. 29 pages, 5 figures, 7 tables, including appendices

**Решение:** -4 исследование стилистических сдвигов ответов LLM

---

### 206 · R5950

**Zero-shot performance of selected large language and multimodal models on the 2023 Brazilian Portuguese medical residency exam.**

2026 · Scientific reports · journal article, journalarticle, article · eng · https://doi.org/10.1038/s41598-026-42829-w

We evaluated the zero-shot performance of six large language models (LLMs; GPT-4.0 Turbo, LLaMA-3-8B, LLaMA-3-70B, Mixtral 8\documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$\times$$\end{document}7B Instruct, Titan Text G1-Express, Command R+) and four multimodal LLMs (Claude-3.5-Sonnet, Claude-3-opus, Claude-3-Sonnet, Claude-3-Haiku) on the 2023 Brazilian Portuguese medical residency entrance exam of the Hospital das Clínicas da Faculdade de Medicina da Universidade de São Paulo including text-only and image-based questions. Comparison among models showed that accuracy varied widely, with Claude-3.5-Sonnet achieving the highest score on text-only questions (70.27%, 95% CI: 65.68–74.86), surpassing GPT-4.0 Turbo (66.22%, 95% CI: 65.38–67.05), while the open-source LLaMA-3-70B performed competitively. The best models reached the median level observed among human candidates. On image-based questions, accuracy dropped substantially across models, with most scoring below 50%, except Claude-3.5-Sonnet, which maintained stable performance. However, this decline should be interpreted with caution, as it remains unclear whether it reflects multimodal reasoning limitations or differences in intrinsic question difficulty, and the present study does not allow these possibilities to be disentangled. In addition, qualitative analysis by independent expert physicians assessed model-generated explanations, identifying hallucinatory events, with lower inter-rater agreement in misclassified cases. These results suggest that language models in Brazilian Portuguese may approximate human-level reasoning in medical questions.

**Решение:** -4 медицинский вступительный экзамен в резидентуру в Бразилии

---

### 207 · R2889

**LLM-Driven Semantic Consistency Analysis for TRDP Implementations in Train Networks**

2026 · IEEE Transactions on Cognitive Communications and Networking · journalarticle · https://doi.org/10.1109/tccn.2026.3710539

To address the difficulty of detecting silent inconsistencies in Train Real-time Data Protocol implementations, we propose TRDP-Guard, an automated protocol consistency checking architecture based on large language model (LLM)-driven semantic analysis. TRDP-Guard extracts structured rules from the IEC 61375 standard, localizes relevant implementation logic via LLM guided program slicing, and performs semantic consistency analysis between rules and code to identify latent deviations. Experiments on real-world TRDP implementations show that TRDP-Guard effectively detects representative defects such as timer mismanagement, PULL/PUSH misuse, and missing field validation, achieving 86.4% precision and 95.0% recall, significantly outperforming existing static analysis tools. Furthermore, we model three classes of consistency breaking attacks timing, scheduling, and semantic confusion attacks and design corresponding defense mechanisms. Simulation results demonstrate that the proposed defenses effectively mitigate protocol inconsistency-induced threats, enhancing the robustness of train communication systems.

**Решение:** -4 семантическая согласованность железнодорожного протокола TRDP

---

### 208 · R9678

**P323: Clinical symptom severity correlates with communicative functioning difficulties in Cornelia de Lange syndrome**

2025 · Genetics in Medicine Open · article · en · https://doi.org/10.1016/j.gimo.2025.102288

Introduction: The field of medical genetics has witnessed rapid advancements, primarily driven by the increased availability of genomic sequencing and big data analytics.This has expanded our understanding of genetic diseases and heightened the demand for clinical geneticists, who play a pivotal role in diagnosing and managing genetic disorders.Natural Language Processing (NLP), particularly through large language models (LLMs) like GPT, is emerging as a transformative tool in medicine.Trained on vast amounts of text data, these advanced artificial intelligence systems are designed to understand and generate human language, in order to perform various tasks such as answering questions, generating text, summarizing information, and more.Despite their promise, LLMs face multiple challenges.To understand the potential and limitations of LLMs in medical genetics, this review follows the typical steps performed by medical geneticists in the clinic.We highlight potential applications of LLMs at each step, review relevant studies published so far, and emphasize key challenges that remain unresolved.Methods: We searched PubMed for all original articles published in 2023-2024 that study the applications of LLMs in medical genetics.In total 15 relevant papers were found and discussed throughout our review.Results: Following the typical workflow of a medical geneticist, we demonstrate that LLMs have the potential to contribute at each step; Starting with identifying individuals within electronic medical records (EMRs) who may benefit from genetic counseling, normalization of clinical phenotype terms in unstructured clinical notes, and predictive modeling of the likelihood of specific rare genetic conditions based on clinical presentation.Then, LLMs can be used for data integration to support comprehensive differential diagnosis.They can also assist in results interpretation, such as improving variant classification and gene prioritization.Even after a genetic diagnosis is made, LLMs could assist in analyzing the literature to educate the patient and family, and aid in long-term follow-up management by automating appointments, monitoring symptoms, and tailoring personalized treatment options.Lastly, LLMs are increasingly useful for research purposes, including identifying therapeutic targets, selecting individuals for clinical trials, analyzing statistics, and refining scientific writing.However, while current research indicates that LLMs can outperform traditional NLP methods and, in some cases, achieve performance equivalent to humans, these models also exhibit inconsistencies and are prone to generating plausible yet incorrect responses.Furthermore, LLMs rely heavily on available databases, which can lead to biased responses, particularly concerning underrepresented populations or rare genetic findings.Patient communication remains an area in need of improvement, especially in medical genetics where sensitive results impacting the patient and their family are reported, underscoring the importance of human interaction for providing compassionate genetic counseling and support.Ethical considerations add another layer of complexity, with issues related to privacy, data security, and informed consent being paramount when integrating AI technologies into healthcare.Conclusion: The revolution of LLMs in our daily lives and medical practice has already begun and is unstoppable.It is essential to embrace and leverage this technology for the benefit of both patients and physicians.LLMs indeed hold great promise for transforming various aspects of medical genetics; however, their integration must be approached thoughtfully.Ongoing research, validation, and adherence to ethical standards are essential to ensure that these technologies serve as complementary tools, enhancing rather than replacing the invaluable role of human expertise in genetics.

**Решение:** -4 медицинская генетика, фенотипические признаки

---

### 209 · R3901

**Beyond Discrete Search: Divergent Thinking as Intention Optimization in Latent Space**

2026 · Annual Meeting of the Association for Computational Linguistics (ACL) · journalarticle, conference, conference-paper · https://doi.org/10.18653/v1/2026.acl-srw.88

We argue that LLM-based coding agents frequently fail to solve problems that lie within the model’s capacity and the bottleneck is often the conditioning context rather than the model itself. We formalize this for the full class of Turing-computable problems with verifiable specifications and introduce a framework that recasts coding as optimization over conditioning contexts that influence the generation of natural-language solution intentions. Guided by execution feedback, the method searches this continuous context space to steer a coding agent toward correct solutions. The method operates as a plug-in layer that can wrap any coding agent without modifying its architecture or weights. On SWE-Bench Verified, our method raises the resolution rate of a weak, quantized 24B open-weight model to parity with frontier models +25× its size.

**Решение:** -4 генерация программного кода автономными агентами

---

### 210 · R2536

**Viewpoint: Global mental health services and the impact of artificial intelligence-powered large language models**

2026 · Human Science Research Council SA · journalarticle/none, article · en · https://doi.org/10.14749/32361954

There is a largeand growing need formental health services worldwide, but there is amassive shortage ofmental health specialists to meet these needs-particularly in humanitarianemergencies, low-income countries,and other areas with limited resources.One strategy that has emerged to address treatment gaps is to rely on nonspecialists (eg, lay health workers, teachers, social workers, and peer mentors) to provide mental health services. Although this approach can be effective, current strategies demand substantial training and supervision.1 They also require highly standardized interventions, which may paradoxically limit more person-centered treatments.2 Concurrently, the field of artificial intelligence (AI) is evolving rapidly and changing how we detect and treat mental health disorders. Artificial intelligence applications in psychiatry are varied and include developing predictionmodels for disease detection and prognosis, creating algorithms that can help clinicians choose the right treatment plan, monitoring patient progress based on data from wearable devices, building chatbots that deliver more personalized and timely interventions,and usingAI techniques toanalyze therapy session transcripts to improve treatment fidelity and quality.

**Решение:** -1 эссе / точка зрения о влиянии больших языковых моделей на глобальное психическое здоровье

---

### 211 · R9745

**Comparing ChatGPT and human expertise: exploring new avenues in peer review of single-case experimental research**

2025 · European Journal of Special Needs Education · journalarticle, review, article · en · https://doi.org/10.1080/08856257.2025.2533555

ABSTRACT Peer review plays a pivotal role in validating research and upholding academic excellence. However, it grapples with problems like reviewer reluctance, variable review durations and extended publication decision timelines. Artificial intelligence (AI), particularly ChatGPT, holds promise in augmenting the peer review process by enhancing efficiency and objectivity. This study compared peer reviews by human experts and ChatGPT for 18 single-case research design (SCRD) manuscripts in special education and psychology. Human reviewers and ChatGPT were evaluated for concordance in manuscript quality assessments and publication decisions. Findings reveal substantial agreement, suggesting ChatGPT’s potential to assist when guided by structured rubrics. However, low agreement in publication recommendations highlights the nuanced nature of these decisions, influenced by subjectivity, domain expertise and contextual understanding. This underscores the necessity of a balanced approach to leverage AI’s strengths while respecting human expertise in peer review practices. Implications for practice and recommendation for future research were provided.

**Решение:** -4 экспертная оценка рецензий ChatGPT в академическом рецензировании

---

### 212 · R3903

**Ethos AI: Artificial Intelligence Agents Based on LLM as Simulated Patients for Training Psychologists in the Treatment of Alcoholism**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-39904-5_32

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 Ethos AI: агенты на базе LLM, нет аннотации

---

### 213 · R12516

**Generative AI for Qualitative Research: A Paradigm Shift Towards Cost-effectiveness (4x), Throughput time (15x) and Reliability (Cohen's Kappa)**

2023 · Unpublished · text/preprint · https://doi.org/10.13140/rg.2.2.11414.52800

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? качественные исследования с генеративным ИИ, нет аннотации — проверить тип публикации в полном тексте

---

### 214 · R2580

**Cocreation and Evaluation in the Era of Generative Artificial Intelligence Tools: Learning Experience Revisited**

2026 · Lecture notes in educational technology · book-chapter · en · https://doi.org/10.1007/978-981-92-1792-2_12

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 совместное творчество и оценка в эпоху генеративного ИИ, нет аннотации

---

### 215 · R9343

**Early Detection and Personalized Intervention in Mental Health**

2025 · International Conference on Computing and Convergence Technology · conference, conference-paper · en · https://doi.org/10.1109/iccct63501.2025.11019669

This research addresses the widespread issue of individuals adapting to stress without recognizing the potential long-term health consequences. To mitigate this, we propose a comprehensive solution that leverages self-reported mental health data. Our approach integrates a rule-based system with Natural Language Processing (NLP) techniques to offer personalized, structured support for users experiencing anxiety, stress, or negative thought patterns. The rule-based system identifies common cognitive distortions and applies predefined strategies to challenge and reframe these distorted thoughts. Furthermore, the system classifies the user's input to identify the type of mental health concern that can be addressed through therapeutic intervention. Additionally, a fine-tuned GPT-2 model generates dynamic, contextually appropriate responses aligned with Cognitive Behavioral Therapy (CBT) principles. When necessary, the system suggests specific activities and exercises within the chat to further support users. This dual approach-combining classification and real-time support-provides tailored interventions that adapt to individual needs and promote healthier coping mechanisms. We discuss the potential impact of this system on mental health management, particularly in enhancing self-awareness and fostering more effective, accessible therapeutic solutions through conversational AI.

**Решение:** -6 диалоговая система КПТ с правилами и генерацией ответов GPT-2 без валидации кодирования

---

### 216 · R12590

**Discourse-Level Representations can Improve Prediction of Degree of Anxiety**

2023 · Annual Meeting of the Association for Computational Linguistics · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.18653/v1/2023.acl-short.128

Anxiety disorders are the most common of mental illnesses, but relatively little is known about how to detect them from language. The primary clinical manifestation of anxiety is worry associated cognitive distortions, which are likely expressed at the discourse-level of semantics. Here, we investigate the development of a modern linguistic assessment for degree of anxiety, specifically evaluating the utility of discourse-level information in addition to lexical-level large language model embeddings. We find that a combined lexico-discourse model outperforms models based solely on state-of-the-art contextual embeddings (RoBERTa), with discourse-level representations derived from Sentence-BERT and DiscRE both providing additional predictive power not captured by lexical-level representations. Interpreting the model, we find that discourse patterns of causal explanations, among others, were used significantly more by those scoring high in anxiety, dovetailing with psychological literature.

**Решение:** -5 предсказание уровня тревоги с помощью моделей RoBERTa и Sentence-BERT, нет генеративных LLM

---

### 217 · R2262

**Patient Experiences in the Cochlear Implant Reddit Community: Comparing Human and Large Language Model Categorization.**

2026 · American journal of audiology · comparative study, journal article, med · eng · https://doi.org/10.1044/2025_aja-25-00216

Purpose: Although some work has leveraged automated analyses of online communities to gain cochlear implant (CI) patient insights, there remains a gap in comparing human versus automated analysis of the nuanced, real-world experiences patients share outside clinical settings. This study characterizes experiences within the r/Cochlearimplants Reddit community and compares human to large language model (LLM) performance in annotating posts. Method: Using reflexive thematic analysis, 996 publicly available r/Cochlearimplants posts (October 2024–June 2025) were manually coded and consolidated into themes. Three LLMs—OpenAI o3, Gemini 2.5 Pro, and Claude Sonnet 4—were prompted with the posts and human-generated codebook to perform post categorization. Model performance was evaluated against human coding using Cohen's kappa, percent agreement, sensitivity, specificity, positive predictive value (PPV), negative predictive value (NPV), and time. Results: Five themes emerged. Community engagement and support ( N = 944, 94.8%) frequently involved eliciting advice ( N = 721, 72.4%), seeking shared experiences ( N = 249, 25.0%), and sharing negative experiences ( N = 247, 24.8%). Other themes included the medical/surgical journey ( N = 463, 46.5%), device/technical issues ( N = 343, 34.4%), daily life/adjustments ( N = 236, 23.7%), and media/outreach (7.2%, N = 72). OpenAI o3 and Gemini 2.5 Pro achieved the highest interrater reliability with human annotators (κ = .35 and κ = .34, respectively). OpenAI o3 had higher sensitivity (46.7%) but lower specificity (90.4%) than Gemini 2.5 Pro, which had the highest specificity (93.4%) but lower sensitivity (38.0%). Claude Sonnet 4 showed the lowest agreement (κ = .25) and PPV (30.9%). Compared to human annotation requiring 52 hr across all annotators, each LLM required less than 20 min. Conclusions: Reddit posts revealed rich discourse across CI topics. LLMs demonstrated fair agreement with human coders and can quickly aid in large-scale qualitative analysis. Although careful model selection and human expertise remain essential for accurate interpretation, LLM annotation shows potential for real-time monitoring of patient concerns to inform counseling, rehabilitation strategies, and iterative device design. Supplemental Material: https://doi.org/10.23641/asha.31362847

**Решение:** -4 анализ сообщества Reddit по кохлеарным имплантам, оториноларингология

---

### 218 · R10643

**Horizon Framework: A Universal Meta-Methodology for Cognitive-Somatic Restructuring via LLM-Assisted Therapy - Clinical Validation, Ethical Principles, and Mechanisms of Action (Preprint)**

2025 · JMIR Publications Inc. · posted-content, preprint · https://doi.org/10.2196/preprints.87325

BACKGROUND The rapid advancement of large language models (LLMs) in mental healthcare has created an urgent need for structured, ethically-grounded therapeutic protocols that occupy the unique niche between support chatbots and specialist therapy. OBJECTIVE This study presents the evolution and validation of Horizon Framework from a love addiction therapy tool to a universal meta-methodology for cognitive-somatic restructuring, with integrated ethical safeguards and cross-platform reproducibility. METHODS A 60-day single-case study involved a 51-year-old male with chronic love dependency (17 years duration) conducting 200+ therapy sessions using LLM assistance. The methodology integrates CBT principles with Damasio's somatic marker theory and metaphoric restructuring. Cross-platform validation tested reproducibility across 11 AI models (8K-512K token context). Standardized assessment tools included Zung SDS, Y-BOCS, HADS, SWLS, WEMWBS, and a novel Somato-Emotional Scoring system. RESULTS Significant improvements were observed: SDS scores decreased from 73 (severe depression) to 22 (normal range), obsessive thoughts reduced from 18-20 hours/day to &lt;10 minutes/day, and somatic markers decreased from 9/10 to 0/10. Spontaneous remission of comorbid dependencies and emergence of self-love as a neuroplasticity marker were documented. Cross-platform validation confirmed method core reproducibility across all tested AI architectures. The Ethical Compass framework ensured safe implementation with eight safeguarding principles. CONCLUSIONS Horizon Framework establishes a novel evidence-based paradigm for AI-assisted therapy, demonstrating significant clinical efficacy, cross-platform reproducibility, and integrated ethical safeguards. Its positioning as an adjunct to professional therapy offers a scalable solution for mental healthcare augmentation while maintaining rigorous safety standards.

**Решение:** -1 отчет об единичном клиническом случае (n=1) терапии любовной зависимости с ИИ

---

### 219 · R6425

**Toward Fair and Scalable Assessment of Socially Shared Regulation of Learning with Large Language Models**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-29773-0_14

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 оценка социально разделяемой регуляции в обучении, педагогика

---

### 220 · R3577

**Reproducibility and Robustness of Large Language Models for Mobility Functional Status Extraction.**

2026 · medRxiv : the preprint server for health sciences · journal article, preprint, ppr · eng · https://doi.org/10.64898/2026.04.03.26350117

Clinical narrative text contains crucial patient information, yet reliable extraction remains challenging due to linguistic variability, documentation habits, and differences across care settings. Large language models (LLMs) have shown strong accuracy on clinical information extraction (IE), but their reproducibility (stability under repeated runs) and robustness (stability under small, natural prompt variations) are less consistently quantified, despite being central to clinical deployment. In this study, we evaluate three open-weight LLMs representing distinct modeling choices: a dense general-purpose model (Llama 3.3), a mixture-of-experts (MoE) general-purpose model (Llama 4), and a domain-tuned medical model (MedGemma). We focus on binary clinical IE aligned with four mobility classes from the International Classification of Functioning, Disability and Health (ICF) framework. Using a controlled experimental design, we quantify (1) intra-prompt reproducibility across repeated sampling and (2) inter-prompt robustness across paraphrased prompts. We jointly report predictive performance (F1-score) and stability (Fleiss' Kappa). And we test factor effects using three-way ANOVA with post-hoc comparisons. Results show that increasing temperature generally degrades agreement, but the magnitude depends on model and task; furthermore, prompt paraphrasing can substantially reduce stability, with particularly large drops for the MoE model. Finally, we evaluate a practical mitigation, self-consistency via majority voting, which improves κ substantially and often improves or preserves F1-score, at the cost of additional inference. Together, these findings provide a reproducible framework and concrete recommendations for evaluating and improving LLM reliability in clinical IE.

**Решение:** -4 извлечение классов физической мобильности (МКФ) из клинических записей, соматическая медицина

---

### 221 · R2931

**SHALA-LLM: Smartly Handling Ambiguous Labels in Aligning LLMs**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.05376

Many human-centered tasks, including natural language inference (NLI) and emotion recognition (ER), have multiple plausible interpretations, leading to label ambiguity and challenging disagreements across human annotators. As LLMs are increasingly deployed in real-world settings, faithfully modeling such ambiguity is essential to identify contested inputs, preserve variability in ambiguous cases, and capture the full distribution of human judgments. Yet, existing LLM alignment approaches have predominantly assumed a single correct label, excluding annotator disagreement during optimization. Instead of treating this ambiguity as noise, we show how to treat it as information that improves model behavior through a new algorithm called SMARTLY HANDLING AMBIGUOUS LABELS IN ALIGNING LLMS (SHALA-LLM). This reinforcement learning framework provides a new way for LLMs to learn directly from annotator distributions while dynamically prioritizing highly ambiguous samples during optimization. Experiments on ambiguity-sensitive NLI and ER benchmarks, including ChaosNLI, GoEmotions, and MSP-Podcast, demonstrate that SHALA-LLM improves agreement with annotator label distributions, e.g. on ChaosNLI, it reduces Jensen-Shannon Distance by up to 62.1%. At the same time, SHALA-LLM improves F1 by up to 16.7%, showing that modeling annotator disagreement can also strengthen classification performance.

**Решение:** -4 согласование неоднозначных меток в NLP-задачах (NLI и распознавание эмоций)

---

### 222 · R4393

**Credit C-GPT: A Domain-Specialized Large Language Model for Conversational Understanding in Vietnamese Debt Collection**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.10167

Debt collection is a critical function within the banking, financial services, and insurance (BFSI) sector, relying heavily on large-scale human-to-human conversational interactions conducted primarily in Vietnamese contact centers. These conversations involve informal spoken language, emotional variability, and complex domain-specific reasoning, which pose significant challenges for traditional natural language processing systems. This paper introduces Credit C-GPT, a domain-specialized large language model with seven billion parameters, fine-tuned for conversational understanding in Vietnamese debt collection scenarios. The proposed model integrates multiple conversational intelligence tasks, including dialogue understanding, sentiment recognition, intent detection, call stage classification, and structured slot-value extraction, within a single reasoning-based framework. We describe the data construction process, annotation strategy, and training methodology, and evaluate the model on proprietary human-annotated datasets. Experimental results show consistent improvements over traditional pipeline-based approaches, indicating that domain-specialized conversational language models provide a scalable and privacy-aware solution for real-time assistance and post-call analytics in enterprise contact centers. 8 pages, 0 figures, 3 tables. Preprint

**Решение:** -4 банковский скоринг и взыскание задолженности (Credit C-GPT)

---

### 223 · R7114

**MindSpeak: An AI-Driven Mobile Application to Enhance Communication Skills for Children with Autism Spectrum Disorder**

2025 · International Mobile, Intelligent, and Ubiquitous Computing Conference (MIUCC) · conference, conference-paper · https://doi.org/10.1109/miucc66482.2025.11196837

This paper presents MindSpeak, an AI-driven mobile application designed to enhance communication skills in children diagnosed with Autism Spectrum Disorder (ASD). The application integrates a conversational avatar, therapeutic minigames, and real-time emotional and behavioral analysis using facial expression recognition, vocal tone detection, eye gaze tracking, and behavior monitoring. Each session is recorded, analyzed, and summarized using a large language model, specifically Generative Pre-trained Transformer 4 (GPT-4), with comprehensive reports delivered to therapists and parents. The system combines AI-based monitoring with structured, engaging therapy sessions to provide a novel, accessible platform that supports continuous, personalized intervention at home and complements traditional therapeutic approaches. Experimental evaluations demonstrate strong performance across all modules, validating the system's potential for supporting children with ASD.

**Решение:** -4 мобильное приложение MindSpeak для тренировки навыков общения

---

### 224 · R8397

**Tuning-Free Personalized Alignment via Trial-Error-Explain In-Context Learning**

2025 · Findings of the Association for Computational Linguistics: NAACL · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2025.findings-naacl.326

Language models are aligned to the collective voice of many, resulting in generic outputs that do not align with specific users' styles. In this work, we present Trial-Error-Explain In-Context Learning (TICL), a tuning-free method that personalizes language models for text generation tasks with fewer than 10 examples per user. TICL iteratively expands an in-context learning prompt via a trial-error-explain process, adding model-generated negative samples and explanations that provide fine-grained guidance towards a specific user's style. TICL achieves favorable win rates on pairwise comparisons with LLM-as-a-judge up to 91.5% against the previous state-of-the-art and outperforms competitive tuning-free baselines for personalized alignment tasks of writing emails, essays and news articles. Both lexical and qualitative analyses show that the negative samples and explanations enable language models to learn stylistic context more effectively and overcome the bias towards structural and formal phrases observed in their zero-shot outputs. By front-loading inference compute to create a user-specific in-context learning prompt that does not require extra generation steps at test time, TICL presents a novel yet simple approach for personalized alignment. NAACL 2025 Findings

**Решение:** -4 персонализация генерации LLM через метод проб и ошибок

---

### 225 · R11180

**Supplementary Material for: "Predicting suicide using natural language processing of autobiographical memory"**

2024 · OSF · text/project · https://doi.org/10.17605/osf.io/7u2dr

Autobiographical memory, a critical cognitive process for recalling personal events, is closely linked to mental health. Depressive disorders are characterized by overgeneralized and negative memory patterns, which impair future-oriented thinking and exacerbate hopelessness. Current evaluations of autobiographical memory are subjective and limited by human bias. In this study, we applied Natural Language Processing using Large Language Models (LLMs) to analyze autobiographical memory narratives, uncovering that their valence can predict depression, suicidal ideation, and prior suicide attempts. Furthermore, valence correlated with core components of the Three-Step Theory of suicide, such as hopelessness and lack of connectedness. By integrating advanced computational techniques, our approach demonstrated high predictive accuracy and offers a scalable, objective method for assessing suicide risk. These findings highlight the potential of LLM-based analysis in enhancing psychological assessment and informing interventions, paving the way for innovative clinical applications in mental health care.

**Решение:** ? T2/T3 анализ автобиографических воспоминаний для предсказания суицидального риска; проверить эталон разметки

---

### 226 · R1555

**Bye Bye Perspective API: Lessons for Measurement Infrastructure in NLP, CSS and LLM Evaluation**

2026 · arXiv.org · journalarticle · https://doi.org/10.48550/arxiv.2604.25580

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 оценка Perspective API при анализе токсичности, нет аннотации

---

### 227 · R4539

**Uncoded Clinical Features from Multilingual Electronic Health Records in Catalonia: Development and Validation Study**

2026 · medRxiv · preprint, ppr, review · https://doi.org/10.64898/2026.09.16.26363030

Abstract Background Unstructured free-text narratives in electronic health records (EHRs) contain critical clinical information that is not captured by structured standard codes. In Catalonia, primary care notes follow a semi-structured format known as MEAP (in Catalan). However, extracting structured variables using cloud-hosted commercial large language models (LLMs) raises substantial data privacy concerns and incurs high operational costs. Objective To develop and validate a privacy-preserving local hybrid pipeline combining a lightweight small language model (SLM) with deterministic regular expressions for extracting six uncoded urinary tract infection (UTI) clinical features (fever, nitrites, leukocytes, lumbar pain, abdominal pain, and haematuria) from primary care EHR narratives. Methods We deployed the open-weight model (Phi4-mini, 3.8B parameters) within the institutional firewall using Ollama. Prompts were iteratively refined in collaboration with clinicians, and regular expressions were applied post-inference. Validation was conducted across two independent arms: (1) a double-blind clinician gold standard review of 60 real patient records (consensus-resolved cases), and (2) an adversarial synthetic dataset of 720 notes enriched with linguistic noise, generated using GPT-4.1 and Grok-4.1. Point estimates and 95% confidence intervals (CIs) were computed for key performance metrics. Results The pipeline processed 15,498 MEAP narratives from a matched cohort of 2,962 primary care patients and identified 4,663 clinical feature occurrences. Patients progressing to acute pyelonephritis (cases) presented a higher features burden than non-progressing controls (71.3% vs. 55.8%; standardized mean difference [SMD] = 0.326), particularly for fever (33.0% vs. 9.0%; SMD = 0.616) and lumbar pain (29.0% vs. 9.8%; SMD = 0.502). In real-world clinician validation, overall performance yielded 93.8% accuracy (95% CI 90.6%-96.1%), 83.6% sensitivity (95% CI 73.0%-91.2%), 96.6% specificity (95% CI 93.6%-98.4%), 87.1% positive predictive value (PPV; 95% CI 77.0%-93.9%), and 95.5% negative predictive value (NPV; 95% CI 92.3%-97.7%). In synthetic stress-testing, the pipeline demonstrated 87.2% accuracy (95% CI 84.6%-89.6%), 73.9% sensitivity (95% CI 68.9%-78.5%), near-perfect specificity (99.5%, 95% CI 98.1%-99.9%), and 99.2% PPV (95% CI 97.2%-99.9%). Conclusions A privacy-preserving local hybrid framework combining a compact open-weight SLM with regular expression rules achieves high specificity and precision for extracting six uncoded clinical features from multilingual primary care narratives. Running entirely within institutional servers, this approach keeps patient data secure, meets privacy standards, and avoids Application Programming Interface (API) costs, making it a practical tool for EHR research, though with lower sensitivity for narratively complex descriptions.

**Решение:** -4 извлечение неструктурированных признаков из многоязычных медкарт, соматическая медицина

---

### 228 · R0155

**Artificial intelligence advancements for orthopaedic clinical reasoning: longitudinal assessment of newer models (ChatGPT-5, Grok-3, Gemini 2.5 Flash) compared to clinicians.**

2026 · Archives of orthopaedic and trauma surgery · comparative study, research-article, journal article · eng · https://doi.org/10.1007/s00402-026-06400-6

INTRODUCTION: This descriptive study aimed to longitudinally evaluate the performance of contemporary large language models - ChatGPT-5, Gemini 2.5 Flash, and Grok-3 - on orthopaedic clinical multiple-choice tasks, benchmarked against pooled clinician consensus. A secondary aim was to assess whether recent advances in generative AI translated into improved alignment with clinician consensus compared with previous AI models. MATERIALS AND METHODS: A total of 97 multiple-choice clinical cases spanning eight orthopaedic subspecialties were sourced from OrthoBullets and previously benchmarked against aggregated responses from thousands of practising clinicians. Using identical methodology to our 2023 study of ChatGPT-3.5, ChatGPT-4, and Bard, each model was prompted with standardised case stems and response options. The primary outcome was the proportion of AI responses matching the most popular clinician response; secondary analyses assessed agreement within 10% and 20% of clinician consensus, performance on 'controversial' (< 25% margin) questions, and inter-model concordance using Cohen's kappa coefficients. RESULTS: Gemini 2.5 Flash achieved the highest alignment with clinician consensus (69.1%), followed by Grok-3 (66.0%) and ChatGPT-5 (58.8%). None of the LLMs refused to respond to any prompts, representing a reduction from 7.2% from our 2023 study. Subspecialty analysis demonstrated that Gemini 2.5 Flash performed best in Hand and Paediatric domains, while Grok-3 excelled in Reconstruction, Trauma, and 'controversial' cases. Inter-model agreement was highest between Grok-3 and Gemini 2.5 Flash (κ = 0.678), indicating improved consistency compared with prior-generation systems. CONCLUSIONS: Contemporary LLMs can be promising adjuncts for orthopaedic education by simulating peer reasoning and offering structured explanations in non-critical settings. Despite incremental gains in reasoning capability compared to previous AI models, contemporary LLMs remain unsuitable for independent clinical use. Future research should develop hybrid clinician-AI workflows and longitudinal benchmarks to distinguish true reasoning improvements from memorisation.

**Решение:** -4 продольная оценка ответов LLM в ортопедической клинике

---

### 229 · R8009

**Assessing Creativity Across Multi-Step Intervention Using Generative AI Models**

2025 · Journal of Learning Analytics · journalarticle, article · en · https://doi.org/10.18608/jla.2025.8571

Creativity is an imperative skill for today’s learners, one that has important contributions to issues of inclusion and equity in education. Therefore, assessing creativity is of major importance in educational contexts. However, scoring creativity based on traditional tools suffers from subjectivity and is heavily time- and labour-consuming. This is indeed the case for the commonly used Alternative Uses Test (AUT), in which participants are asked to list as many different uses as possible for a daily object. The test measures divergent thinking (DT), which involves exploring multiple possible solutions in various semantic domains. This study leverages recent advancements in generative AI (GenAI) to automate the AUT scoring process, potentially increasing efficiency and objectivity. Using two validated models, we analyze the dynamics of creativity dimensions in a multi-step intervention aimed at improving creativity by using repeated AUT sessions (N=157 9th-grade students). Our research questions focus on the behavioural patterns of DT dimensions over time, their correlation with the number of practice opportunities, and the influence of response order on creativity scores. The results show improvement in fluency and flexibility, as a function of practice opportunities, as well as various correlations between DT dimensions. By automating the scoring process, this study aims to provide deeper insights into the development of creative skills over time and explore the capabilities of GenAI in educational assessments. Eventually, the use of automatic evaluation can incorporate creativity evaluation in various educational processes at scale.

**Решение:** -4 оценка креативности учащихся в образовательном вмешательстве

---

### 230 · R7879

**Advancing Healthcare Innovation Summit (AHIS) 2025: Embracing Artificial Intelligence and Digital Health**

2025 · Innovations in Digital Health Diagnostics and Biomarkers · article · en · https://doi.org/10.36401/iddb-25-x4

The 2025 Advancing Healthcare Innovation Summit (AHIS), held virtually on April 26, brought together a broad international audience of researchers, clinicians, digital health professionals, and aspiring innovators to discuss topics related to artificial intelligence (AI) and digital health. Hosted by the Innovative Healthcare Institute, an organization committed to promoting the adoption of groundbreaking solutions in healthcare, and the Innovations in Digital Health, Diagnostics, and Biomarkers Journal, AHIS provided a multidisciplinary platform to present cutting-edge research, foster collaboration, and promote the responsible integration of digital technologies into healthcare. The agenda featured several thoughtfully selected presentations addressing topics such as AI in clinical diagnostics, digital biobanking, patient-centered data platforms, and applications in behavioral health.The conference featured a series of awards to acknowledge exceptional contributions, including the Aspiring Innovator of the Year Award, the Young Innovator of the Year Award, and the Chairman’s Award. These recognitions were designed to honor originality, impact, and excellence in the field of digital health innovation. Zisis Kozlakidis from the International Agency for Research on Cancer, part of the World Health Organization in France, chaired the meeting, ensuring productive discussion, thematic consistency, and contributing to a critical facet of the debate.A recently published editorial by Karine Sargsyan, “Artificial Intelligence and Machine Learning: Technologies Revolutionizing the Healthcare Sector and Biomedical Research,”[1] highlights the central themes of the summit. The editorial analyzes how digital advances are currently transforming healthcare. She highlighted how these technologies offer unparalleled opportunities to advance the medical field, leading to better patient care, from prevention to diagnosis, treatment, and long-term management. All presentations provided concrete evidence of this vision and demonstrated how innovative technologies are being utilized to address the sector’s challenges.The following is a summary of the event proceedings: abstracts are published in IDDB,[2] and complete presentation recordings are available on InnoScholar.com.[3]The opening session of AHIS 2025 (moderated by Denis Marino) addressed the rising need to manage complexity in medical research and healthcare systems using smart, innovative, scalable, and ethically based digital solutions. Presenters from academia, health technology, and clinical research share distinct yet complementary solutions for tackling the challenges of AI integration, biospecimen utility, and secure data sharing.Anna Michalska-Falkowska of the Medical University of Bialystok (MUB), Poland, highlighted the vital role of digital transformation in biobanking. In her presentation, “Digital Pathology Integration in Biobanking: Transforming Precision Medicine and Research,” she outlined how high-resolution slide imaging, telepathology, and seamless data integration can significantly enhance diagnostic precision and collaborative potential. This presentation received the Aspiring Innovator of the Year Award. In her second presentation, Anna described the development of the MUB Biobank, highlighting its role as a hub for generating multiomic data, discovering biomarkers, and facilitating international collaboration.From a computational point of view, Mostafa Mohiuddin (Children’s Cancer Research Unit, Sydney Children’s Hospital Network, Australia) introduced a protocol-agnostic AI-based framework that utilizes inherited genetic variants to predict treatment response in pediatric cancer. His two-step approach, which combines global variant selection and instance-specific refinement via a neural network module, demonstrates how AI can capture clinically actionable signals from complex genomic data.Expanding the discussion on predictive modeling, Eszter Tuboly (Semmelweis University, Hungary) presented a systematic review and meta-analysis comparing traditional prognostic markers, omics-based models, and AI-driven tools in pediatric cancer. Although conventional methods remain prevalent, her findings support the clinical utility of AI-based approaches, emphasizing the need for externally validated models and high-quality biobank datasets, particularly for rare disease applications.Loukia Touramanidou (Metabio, Greece) highlighted the importance of decentralized data governance through the introduction of AI-MetaBloQ, a blockchain-enabled biospecimen marketplace designed to support ethical, transparent, and secure data exchange. The platform empowers patients with control over their samples while incorporating real-time AI-based quality assessment to enhance specimen reliability.Focusing on the development of collaborative infrastructure, Jasper Hoi Chun Luong (Healthy Macau New-Generation Association, China) and Zisis Kozlakidis (International Agency for Research on Cancer, WHO) introduced a maturity model designed for assessing Federated Analytics Networks (FAN) and Trusted Research Environments (TREs). Building on initiatives such as ELIXIR and the One Million Genomes project, their model promotes international research collaboration while addressing legal, operational, and governance challenges.In the area of behavioral health, Dan Holley (NeuroFlow, USA) presented a study comparing large language models (LLMs) with expert clinicians in stratifying suicide risk. His findings demonstrated that LLMs not only closely matched physician judgment (92% agreement) but also achieved improvements in speed and cost efficiency, highlighting the potential of AI to enhance triage in high-risk clinical scenarios.The Aspiring Innovator session offered insightful perspectives on how the synergistic integration of high-quality biobanking, sophisticated data management, and advanced AI applications fundamentally shape the future of precision medicine a

**Решение:** -1 отчет о конференции по инновациям в здравоохранении AHIS 2025

---

### 231 · R6873

**Amendment 1 to Study B (OSF DOI 10.17605/OSF.IO/6SKJE): Dual-Domain Extension (ECG + Abdominal Ultrasound), frozen before confirmatory sampling**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/y4kh6

Amendment date: 2026-09-30. Applies to: OSF registration DOI 10.17605/OSF.IO/6SKJE (registered 2026-09-21, ECG single-domain version; the original registered version remains publicly accessible with its original timestamp). Timing declaration: this amendment is frozen BEFORE the confirmatory sampling draw, before any annotation dispatch, and before any unblinding. The previously declared voiding of the preparatory draw (n=520, seed 20260921) is unchanged. Full amendment document (PDF) is attached to the project files: OSF_Amendment_1_StudyB_DualDomainExtension Submission.pdf. A. SUMMARY OF CHANGES 1. Domain scope: ECG narratives only -&gt; dual-domain: ECG + abdominal ultrasound (abdus). 2. Formal sample size: n=500 (ECG) + 20 pilot -&gt; n=300 per domain x 2 domains (formal total 600) + 20 pilot per domain (40 total). 3. Sampling frame: two independent frames - ECG (ecg_text non-empty) and abdus (us_text non-empty), years 2019-2021; proportional allocation, strata = calendar year (3) x documentation style (2), per domain; narratives drawn untruncated from the raw mirror (wave-level text truncates at 150 characters). 4. Primary hypothesis (H1): per-domain - both domains must meet explicit-definition three-class kappa &gt;= 0.90 with Wilson 95% CI lower bound &gt; 0.85; below-threshold outcomes reported verbatim per domain. 5. Outcome aggregation (abdus domain): V3.0-1a ABDPG conservative rule, frozen in codebook V3.1 (fatty liver / gallbladder-bile-duct stones / post-cholecystectomy / solid focal lesion / cirrhosis / schistosomiasis -&gt; abnormal; isolated benign findings (cysts/polyps/crystals/hemangioma) -&gt; normal). 6. Frozen extractor additions: ABD dictionary track dict_v2 (site=PG, sha256-16 9b73a88b07d3f48a) and ABD LLM prompt v2.1b (sha256-16 bcdc6563420538bb); zero retuning unchanged. 7. Codebook: V3.0 -&gt; V3.1 (2026-09-30 effective version = V3.0 clauses + V3.0-1a; SHA256 registered in the sampling summary). 8. Annotator variables: ECG 12 variables; abdus 6 variables (us_fatty, us_fatty_degree, us_hepatic_other, us_gallstone, us_kidney_cyst, us_unreadable) plus three-class outcome; no main-exam column (PD abdus narratives contain no clinician main-conclusion field, matching the Site-A PG-station text form). B. RATIONALE 1. The sponsor manuscript-feedback priority requests external validation of the final phenotype in a second provider (400-600 records, stratified by year/report style, without retuning); a dual-domain design provides broader generalisability evidence within the suggested range (formal total = 600, upper bound). 2. A data-asset audit of the second provider (2026-09-30) confirmed two narrative domains (ecg_text non-empty ~740,046; us_text non-empty ~710,956, prevalence 36-40%) and the absence of any echocardiography narrative field in the provider raw schema; a four-domain extension is therefore not feasible with this data source, and a balanced two-domain design was adopted (project group decision 2026-09-30: ECG 300 + ABD 300). 3. The abdus domain reuses, without modification, the frozen dictionary track, frozen LLM prompt, and the per-site outcome aggregation rule (V3.0-1a ABDPG conservative) frozen in the companion four-domain definition-alignment study before any Study B annotation. C. UNCHANGED ELEMENTS H2 (monitor false-alarm expectation, site-local style baselines) and H3 (naive-definition and LLM-track-only, exploratory; H3 now additionally covers the ABD domain with its frozen prompt); zero-retuning constraint; double-blinded two-annotator design with rule-first + expert arbitration; 10% intra-rater self-repeats (&gt;=3 days apart, 30 per domain) with outcome kappa&gt;=0.85 QC gate; pilot-first calibration with a &gt;=3 same-type ambiguity stop rule per domain; uninterpretable/exclusion rules; bootstrap B=1,000 clustered by person; per-year reporting; anchor/pilot calibration requirement; failures reported verbatim. Fresh seed pair will be generated and hash-registered AFTER this amendment is frozen; sampling scripts with DOI/freeze assertion gates released with the package. D. SAMPLE-SIZE RATIONALE (AMENDED) At the PD frozen-system screening prevalence (ECG ~47%; abdus ~36-40%) and n=300 per domain: kappa CI half-width ~plus/minus 0.04-0.05 at kappa~0.90 (lower bound marginally above 0.85; the per-domain H1 acceptance probability is honestly pre-registered as slightly lower than at n=500), and sensitivity CI half-width ~plus/minus 2.4 pp. The dual-domain balanced allocation was chosen over a weighted single-domain design to preclude post-hoc selection of the more favourable domain.

**Решение:** -1 поправка к протоколу исследования ЭКГ и УЗИ брюшной полости (OSF)

---

### 232 · R3163

**Conversational trajectory degrades large language model detection of suicidal ideation relative to clinicians: a preregistered study**

2026 · medRxiv · preprint, ppr · https://doi.org/10.64898/2026.07.10.26357132

Abstract Background General-purpose large language models increasingly encounter emotional and therapy-like conversation, yet are not developed or evaluated as clinical systems. Existing safety evaluations rely largely on brief exchanges, although harms often unfold over extended interactions. Whether models maintain safety-relevant performance as conversations accumulate context remains unknown. Methods In this preregistered study, 400 clinician-validated statements, with or without suicidal ideation, were inserted at 0–200 speaker turns in 5 psychotherapy and 3 synthetic transcripts. Forty-nine LLMs and 8 clinicians performed the same binary classification task. Mixed-effects models estimated the effects of conversational depth, model scale, and model version on F1. Twelve top models were tested to 1,500 turns across conversational trajectories, with or without instruction restatement. Results F1 declined with depth across model families (p<0.001). Larger, newer models performed better but still degraded. Clinicians showed no decline (mean F1 0.86 at both 0 and 200 turns), but eight of nine proprietary models exceeded their performance at 200 turns. Conversational content, not length alone, explained F1 changes; the largest decrease was under adversarial context (p<0.001). Restating instructions increased F1 on therapy to near baseline (median ΔF1 +0.12; p<0.001; 89% median recovery) versus MSJ (ΔF1 +0.08; p=0.04; 38% recovery). Conclusions LLM detection of suicidal ideation degraded with conversational depth and trajectory, whereas clinician performance remained stable despite the strongest models exceeding most clinicians in absolute performance. Mental health AI safety evaluations should test sustained performance across realistic and adversarial trajectories rather than relying on short-prompt benchmarks. Plain-language summary Large language models increasingly encounter psychiatric distress and crisis-related content in ordinary use, but existing mental health AI safety benchmarks often rely on isolated prompts, brief exchanges, or simulated conversations rather than real extended interactions. In a preregistered benchmark of 1.4M inferences from 49 LLMs using real psychotherapy transcripts, suicidal-ideation detection declined with conversational depth in every model family while clinician performance remained stable — despite the strongest models matching or exceeding most clinicians in absolute performance — and, among top models, degradation at extended depths depended on the content and direction of the preceding conversation rather than length alone.

**Решение:** + T3 выявление суицидальных мыслей в транскриптах психотерапии: 49 LLM против клиницистов

---

### 233 · R1732

**An experimental study exploring human–AI complementarity in early social-emotional learning**

2026 · Computers and Education Open · article · en · https://doi.org/10.1016/j.caeo.2026.100331

Many children are not receiving crucial social-emotional learning (SEL) support due to systemic constraints, such as high educator workload and training burdens. Pedagogical conversational agents (PCAs)—generative AI-powered virtual characters trained to converse with students like a teacher—offer promising solutions that could extend to SEL. However, the current affective-computing capacities of PCAs may be limiting, as SEL facilitation requires deeper emotional and relational attunement than cognition-heavy subjects (e.g., literacy, numeracy). The emotional and relational skills of human educators likely confer benefits beyond those of PCAs in SEL instruction. Despite this potential complementarity, no studies have experimentally assessed the relative performance of PCAs and educators in SEL contexts. It remains unclear if and how PCAs can help educators close the SEL gap. In this study, we used a controlled comparison to reveal complementary strengths, comparing the performance of a PCA to that of human educators when independently facilitating story-based SEL activities with a static AI child. We used a static AI child to help ensure that any performance differences could be attributed to facilitator type. The PCA ( n = 18 simulations) and educators ( n = 18) each delivered three SEL activities ( N = 108 observations). Expert raters, blind to facilitator type, coded dialogue excerpts for evidence-based SEL support techniques and indicators of pedagogical quality. A mixed ANOVA and t -tests revealed significant differences. The PCA showed strengths in basic relational and instructional domains, maintaining respectful tone and routinely providing procedural scaffolding. Educators showed strengths in deeper SEL instruction, guiding reflection and promoting social-emotional knowledge. We discuss implications for SEL through the lens of human–AI complementarity.

**Решение:** -2 эксперты оценивают транскрипты педагогического диалогового агента и учителей по методике социально-эмоционального обучения

---

### 234 · R11600

**Causal Micro-Narratives**

2024 · Proceedings of the The 6th Workshop on Narrative Understanding · audiovisual/conference talk, journalarticle, text/article · en · https://doi.org/10.18653/v1/2024.wnu-1.12

We present a novel approach to classify causal micro-narratives from text. These narratives are sentence-level explanations of the cause(s) and/or effect(s) of a target subject. The approach requires only a subject-specific ontology of causes and effects, and we demonstrate it with an application to inflation narratives. Using a human-annotated dataset spanning historical and contemporary US news articles for training, we evaluate several large language models (LLMs) on this multi-label classification task. The best-performing model--a fine-tuned Llama 3.1 8B--achieves F1 scores of 0.87 on narrative detection and 0.71 on narrative classification. Comprehensive error analysis reveals challenges arising from linguistic ambiguity and highlights how model errors often mirror human annotator disagreements. This research establishes a framework for extracting causal micro-narratives from real-world data, with wide-ranging applications to social science research. Accepted to EMNLP 2024 Workshop on Narrative Understanding

**Решение:** -4 анализ микро-нарративов об инфляции в экономических новостях

---

### 235 · R8386

**PSM: Prompt Sensitivity Minimization via LLM-Guided Black-Box Optimization**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2511.16209

System prompts are critical for guiding the behavior of Large Language Models (LLMs), yet they often contain proprietary logic or sensitive information, making them a prime target for extraction attacks. Adversarial queries can successfully elicit these hidden instructions, posing significant security and privacy risks. Existing defense mechanisms frequently rely on heuristics, incur substantial computational overhead, or are inapplicable to models accessed via black-box APIs. This paper introduces a novel framework for hardening system prompts through shield appending, a lightweight approach that adds a protective textual layer to the original prompt. Our core contribution is the formalization of prompt hardening as a utility-constrained optimization problem. We leverage an LLM-as-optimizer to search the space of possible SHIELDs, seeking to minimize a leakage metric derived from a suite of adversarial attacks, while simultaneously preserving task utility above a specified threshold, measured by semantic fidelity to baseline outputs. This black-box, optimization-driven methodology is lightweight and practical, requiring only API access to the target and optimizer LLMs. We demonstrate empirically that our optimized SHIELDs significantly reduce prompt leakage against a comprehensive set of extraction attacks, outperforming established baseline defenses without compromising the model's intended functionality. Our work presents a paradigm for developing robust, utility-aware defenses in the escalating landscape of LLM security. The code is made public on the following link: https://github.com/psm-defense/psm accepted at the Trustworthy Agentic AI Workshop @ AAAI 2026 (Singapore, Jan 27, 2026). Workshop PDF: https://trustagenticai.github.io/AAAI2026/AAAI-Workshop/20.pdf

**Решение:** -4 оптимизация системных промптов (PSM)

---

### 236 · R7480

**Securing AI Agents Against Prompt Injection Attacks**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2511.15759

Retrieval-augmented generation (RAG) systems have become widely used for enhancing large language model capabilities, but they introduce significant security vulnerabilities through prompt injection attacks. We present a comprehensive benchmark for evaluating prompt injection risks in RAG-enabled AI agents and propose a multi-layered defense framework. Our benchmark includes 847 adversarial test cases across five attack categories: direct injection, context manipulation, instruction override, data exfiltration, and cross-context contamination. We evaluate three defense mechanisms: content filtering with embedding-based anomaly detection, hierarchical system prompt guardrails, and multi-stage response verification, across seven state-of-the-art language models. Our combined framework reduces successful attack rates from 73.2% to 8.7% while maintaining 94.3% of baseline task performance. We release our benchmark dataset and defense implementation to support future research in AI agent security.

**Решение:** -4 защита RAG-систем от атак внедрения промптов, кибербезопасность

---

### 237 · R5375

**WhispiTree: A Multi-Sensory Conversational AI System for Psychological Healing via the "Tree Hole" Metaphor**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-9362788/v1

Abstract The growing mental health needs of college students stand in stark contrast to the scarcity of professional services, social stigma, and high barriers to access, urgently requiring the exploration of highly accessible digital intervention pathways. This paper designs and develops WhispiTree—a conversational AI psychological healing system integrating multisensory immersive technology with cognitive behavioral therapy (CBT). Based on the “confessional tree hole” interaction metaphor, the system aims to create a non-intrusive, safe psychological space. Its core architecture integrates a large language model dialogue agent constrained by CBT frameworks, a multisensory immersive environment combining audio-visual, olfactory, and tactile elements, and an affective feedback module featuring tangible interactions (e.g., commemorative stickers). Together, these components promote users' cognitive restructuring and emotional regulation. To evaluate the system's efficacy, this study conducted a nine-week randomized controlled trial (RCT, n=45), comparing outcomes among the WhispiTree intervention group, psychological counseling group, and resting resting control group. Results demonstrated that WhispiTree significantly reduced users' anxiety and depression levels while outperforming traditional therapy in intervention accessibility, perceived privacy security, and real-time feedback. The study demonstrates that WhispiTree effectively reduces psychological defense mechanisms in mental health interventions through the integration of “embodied immersion” and “intelligent guidance.” It offers a low-cost, easily scalable digital supplement for university mental health service systems while providing empirical evidence for designing immersive affective computing systems.

**Решение:** -6 РКИ эффективности диалоговой мультисенсорной системы WhispiTree без оценки кодирования текстов

---

### 238 · R3284

**Effectiveness of AI-enhanced virtual patients for psychiatric interview training in health professions education: a meta-analysis.**

2026 · Frontiers in medicine · journal article, systematic review, journalarticle · eng · https://doi.org/10.3389/fmed.2026.1834636

Objectives: Artificial intelligence (AI)-enhanced virtual patient simulations are increasingly used in health professions education to improve clinical communication and diagnostic reasoning. However, the effectiveness of these technologies for psychiatric interview training has not been systematically quantified. This study aimed to systematically review and meta-analyze the existing literature evaluating the impact of AI-enhanced virtual patients on psychiatric interview performance, knowledge acquisition, and learner confidence in health professions education. Materials and methods: A systematic review and meta-analysis was conducted following the PRISMA 2020 guidelines. Electronic database searches were performed in PubMed/MEDLINE, Scopus, Web of Science, and Google Scholar to identify relevant studies published between January 2000 and March 2026. Studies were included if they evaluated AI-enhanced virtual patient simulations for psychiatric interview training among medical students, psychiatry residents, clinicians, or other health professions trainees. Data extraction included study characteristics, participant populations, intervention types, and educational outcomes. Risk of bias was assessed using the Cochrane Risk of Bias Tool. Quantitative synthesis was performed using random-effects meta-analysis models, and effect sizes were calculated as standardized mean differences (SMD) with 95% confidence intervals (CI) using R statistical software. Results: A total of 560 records were identified through database searches and additional sources. After removal of duplicates and screening procedures, 10 studies met the inclusion criteria and were included in the final analysis. The studies involved approximately 450 participants, including medical students, psychiatry residents, clinicians, nursing students, and psychology trainees. AI-enhanced virtual patient interventions included conversational AI systems, virtual human simulations, large language model-based simulated patients, and AI-virtual reality training environments. The pooled analyses indicated improvements in psychiatric interview performance, knowledge acquisition, and learner confidence following AI-supported virtual patient training. Subgroup analysis demonstrated positive educational outcomes across both student and clinician populations. Risk-of-bias assessment revealed variable methodological quality across studies, with several pilot and non-randomized designs. Conclusion: AI-enhanced virtual patient simulations appear to be effective educational tools for improving psychiatric interview training in health professions education. These technologies provide scalable and standardized simulation environments that support communication skill development, diagnostic reasoning, and learner confidence. Although the findings suggest promising educational benefits, further large-scale randomized controlled trials and standardized outcome assessments are needed to confirm the long-term educational impact of AI-supported virtual patient training in psychiatry.

**Решение:** -1 систематический обзор и метаанализ эффективности виртуальных пациентов в обучении психиатрическому интервью

---

### 239 · R12484

**Using AI Based Chatbot ChatGPT for Practicing Counseling Skills through Role-play**

2023 · PsyArXiv · journalarticle, preprint, ppr · en · https://doi.org/10.31234/osf.io/s47jb

ABSTRACT Conversation AI such as ChatGPT is a disruptive technology that has the potential to influence the field of counseling. The present article examines how AI based chatbot ChatGPT can be used by counselor educators in helping counselors-in-training practice counseling skills through role play. The author developed a model, ChatGPT Client Simulation (CCS), to support counselors-in-training learn and practice counseling skills. The CCS model can be used both in synchronous online as well as in-person counseling courses.

**Решение:** -1 методическая статья об использовании ChatGPT для ролевых игр в обучении консультантов

---

### 240 · R10338

**An AI-Powered Teaching Performance Evaluation System: Technical Implementation and Pilot Testing at Universidad Técnica de Ambato**

2025 · Salud Ciencia y Tecnología · journalarticle, review, article · en · https://doi.org/10.56294/saludcyt20252441

The article detailed the design, implementation and pilot test of an artificial intelligence-based system for evaluating teaching performance in higher education. The researcher aimed to create an automatic evaluation process by using speech recognition, semantic analysis and emotional detection, within an artificial intelligence architecture developed at Universidad Técnica de Ambato. The process was executed using open-source tools such as AssemblyAI, GPT-4o-mini, DeepFace and the n8n workflow platform which allowed autonomous analysis of recorded classroom sessions. A quasi experimental validation was actioned using 36 class recordings from 18 teachers from three disciplines. Overall, the findings indicated transcription accuracy of 96.4 %, inter-rater reliability above 90 % rubric agreement and substantial agreement with human raters (Cohen’s κ > 0.65; ICC > 0.80). Time for evaluation was reduced by greater 95 % and cost by 97 % compared with other peer review methods. These results confirmed the feasibility and reliability of the system for institutional quality assurance in teaching evaluation. The study concluded that artificial intelligence-based approaches could provide institutions with an open, efficient and scalable mechanism to assess the pedagogical performance that enhances innovation in higher education.

**Решение:** -4 система оценки эффективности преподавания в педагогике

---

### 241 · R0067

**Generation of Kazakhstan's unified national testing variants using AI: a platform for automatic task creation with expert control.**

2026 · Frontiers in big data · journal article, journalarticle, review · eng · https://doi.org/10.3389/fdata.2026.1772101

This study examines the use of artificial intelligence for Automatic Item Generation (AIG) in the context of Kazakhstan's Unified National Testing (UNT) and presents a human-in-the-loop platform for scalable, expert-controlled test development. The objective is to evaluate whether large language models (LLMs) can reliably generate high-quality, isomorphic mathematics test items in the Kazakh language while preserving psychometric and pedagogical requirements. A hybrid AI system combining a local and a cloud-based LLM was implemented to perform semantic deconstruction of prototype items and constrained isomorphic generation of new variants. The pipeline included structured prompt engineering, parallel generation, and automated symbolic validation using Python and SymPy, followed by double-blind expert review. A stratified sample of 120 UNT mathematics items served as prototypes, from which 200 AI-generated clones were produced and validated. Six qualified subject-matter experts conducted independent evaluations using standardized criteria. Inter-rater reliability reached a substantial level (Cohen's κ = 0.78). Results show that 97.5% of generated items were recommended for use after review, with 50.5% accepted without revision and 47.0% accepted after corrections. The most frequent revision needs involved difficulty calibration, wording clarity, and factual or curricular alignment. Expert interviews confirmed that AI generation significantly reduces development time but remains limited in higher-order cognitive item design and pedagogically grounded distractor construction, especially in a low-resource, morphologically complex language environment. The findings support a hybrid augmentation model in which AI accelerates large-scale item production while experts ensure linguistic, cultural, and psychometric validity. The proposed framework demonstrates practical potential for multilingual, high-stakes assessment systems and provides implementation guidelines for responsible AI integration in test development.

**Решение:** -4 генерация тестовых заданий для единого национального тестирования в Казахстане

---

### 242 · R11364

**Soda-Eval: Open-Domain Dialogue Evaluation in the age of LLMs**

2024 · Conference on Empirical Methods in Natural Language Processing · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2024.findings-emnlp.684

Although human evaluation remains the gold standard for open-domain dialogue evaluation, the growing popularity of automated evaluation using Large Language Models (LLMs) has also extended to dialogue. However, most frameworks leverage benchmarks that assess older chatbots on aspects such as fluency and relevance, which are not reflective of the challenges associated with contemporary models. In fact, a qualitative analysis on Soda, a GPT-3.5 generated dialogue dataset, suggests that current chatbots may exhibit several recurring issues related to coherence and commonsense knowledge, but generally produce highly fluent and relevant responses. Noting the aforementioned limitations, this paper introduces Soda-Eval, an annotated dataset based on Soda that covers over 120K turn-level assessments across 10K dialogues, where the annotations were generated by GPT-4. Using Soda-Eval as a benchmark, we then study the performance of several open-access instruction-tuned LLMs, finding that dialogue evaluation remains challenging. Fine-tuning these models improves performance over few-shot inferences, both in terms of correlation and explanation. Accepted to EMNLP2024 (findings)

**Решение:** -4 оценка диалогов в открытом домене (Soda-Eval)

---

### 243 · R10819

**Emotion-Aware Embedding Fusion in LLMs (Flan-T5, LLAMA 2, DeepSeek-R1, and ChatGPT 4) for Intelligent Response Generation**

2024 · arXiv (Cornell University) · preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2410.01306

Empathetic and coherent responses are critical in auto-mated chatbot-facilitated psychotherapy. This study addresses the challenge of enhancing the emotional and contextual understanding of large language models (LLMs) in psychiatric applications. We introduce Emotion-Aware Embedding Fusion, a novel framework integrating hierarchical fusion and attention mechanisms to prioritize semantic and emotional features in therapy transcripts. Our approach combines multiple emotion lexicons, including NRC Emotion Lexicon, VADER, WordNet, and SentiWordNet, with state-of-the-art LLMs such as Flan-T5, LLAMA 2, DeepSeek-R1, and ChatGPT 4. Therapy session transcripts, comprising over 2,000 samples are segmented into hierarchical levels (word, sentence, and session) using neural networks, while hierarchical fusion combines these features with pooling techniques to refine emotional representations. Atten-tion mechanisms, including multi-head self-attention and cross-attention, further prioritize emotional and contextual features, enabling temporal modeling of emotion-al shifts across sessions. The processed embeddings, computed using BERT, GPT-3, and RoBERTa are stored in the Facebook AI similarity search vector database, which enables efficient similarity search and clustering across dense vector spaces. Upon user queries, relevant segments are retrieved and provided as context to LLMs, enhancing their ability to generate empathetic and con-textually relevant responses. The proposed framework is evaluated across multiple practical use cases to demonstrate real-world applicability, including AI-driven therapy chatbots. The system can be integrated into existing mental health platforms to generate personalized responses based on retrieved therapy session data.

**Решение:** -6 генерация эмпатичных ответов чат-ботом на основе поиска по сессиям терапии

---

### 244 · R7466

**ChatGPT-Assisted Codebook Design for Learning Analytics Datasets in Multiple Languages: A Case Study**

2025 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-12229-2_12

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 разработка кодбука для аналитики обучения в образовании, нет аннотации

---

### 245 · R10423

**Exploring The Use of ChatGPT by Computer Science Students in Software Development: Applications, Ethical Considerations, and Insights for Engineering Education**

2025 · Zenodo (CERN European Organization for Nuclear Research) · conferencepaper/, journalarticle, review · en · https://doi.org/10.5281/zenodo.17631595

ChatGPT has been increasingly used in computer science, offering efficient support across software development tasks. While it helps students navigate programming challenges, its use also raises concerns about academic integrity and overreliance. Despite growing interest in this topic, prior research has largely relied on surveys, emphasizing trends over in-depth analysis of students' strategies and ethical awareness. This study complements existing work through a qualitative investigation of how computer science students in one UK institution strategically and ethically engage with ChatGPT in software development projects. Drawing on semi-structured interviews, it explores two key questions: How do computer science students ethically and strategically report using ChatGPT in software development projects? How do students understand and perceive the ethical issues associated with using ChatGPT in academic and professional contexts? Findings reveal a shift in students' learning models, moving from traditional "independent thinking-manual coding-iterative debugging" to "AI-assisted ideation-interactive programming-collaborative optimization." Importantly, many use ChatGPT conversationally to deepen understanding, while consciously reserving creative and high-level decision-making tasks for themselves. Students tend to cap ChatGPT's contribution to roughly 30%, and evaluate its output to mitigate overreliance. However, only a minority thoroughly analyze AI-generated code, raising concerns about reduced critical engagement. Meanwhile, students reject uncredited use, highlight risks such as privacy breaches and skill degradation, and call for clear usage guidelines set by their teachers. This research offers novel insights into the evolving learner-AI dynamic and highlights the need for explicit guidance to support responsible and pedagogically sound use of such tools. Full paper oral presentation at the European Society for Engineering Education (SEFI) 2025 Annual Conference (September 2025)

**Решение:** -4 использование ChatGPT студентами факультетов компьютерных наук

---

### 246 · R0504

**Co-creation of an AI-Powered Virtual Motivational Interviewing Training Tool for Physical Therapists (VMI-PT) (Preprint)**

2026 · JMIR Publications Inc. · posted-content, preprint · https://doi.org/10.2196/preprints.108072

BACKGROUND Physical therapists frequently struggle to operationalize biopsychosocial care in daily practice. Although Motivational Interviewing (MI) can strengthen patient engagement and support behavior change, existing MI training models are resource-intensive, inconsistently implemented, and provide limited opportunities for deliberate practice and feedback. OBJECTIVE To describe the collaborator-engaged co-creation of an AI-powered mobile application (VMI-PT) designed to train physical therapists in MI through interactive patient simulations and real-time, theory-driven feedback. METHODS Using a design-thinking framework, we engaged 7 licensed physical therapists, 2 psychologists, 2 licensed clinical social workers, and a software development team in iterative co-creation over 8 months. The development process included three phases: inspiration (collaborator needs assessment), ideation (prototype co-creation), and implementation planning. The final application employs generative artificial intelligence to simulate patient interactions, provides real-time feedback using a novel three-tier classification system, and supports deliberate practice principles through scaffolded skill progression. RESULTS Collaborator identified critical communication challenges in physical therapy and refined four clinically authentic patient personas representing diverse biopsychosocial scenarios. Co-creation produced a mobile application featuring adaptive AI-driven patient interactions, immediate MI-specific feedback categorized as “Healing Partner,” “Friendly Provider,” or “Technician,” and skill-progression pathways. Multidisciplinary input informed natural language processing algorithms for real-time MI technique classification and responsive patient dialogue. CONCLUSIONS Collaborator-engaged co-creation yielded a clinically relevant, pedagogically grounded, AI-powered MI training tool tailored to the needs of physical therapists. This methodology highlights a feasible pathway for integrating AI into healthcare education while preserving clinical authenticity and maximizing end-user acceptance. CLINICALTRIAL N/A

**Решение:** -6 разработка мобильного обучающего тренажера с симуляцией пациентов для мотивационного интервьюирования

---

### 247 · R7811

**(231) Artificial Intelligence Meets Medical Rarity: Evaluating ChatGPT’s Responses on Post-orgasmic Illness Syndrome**

2025 · The Journal of Sexual Medicine · journalarticle, article · en · https://doi.org/10.1093/jsxmed/qdaf320.227

Abstract Introduction Post-Orgasmic Illness Syndrome (POIS) is a rare and distressing condition characterized by systemic and cognitive symptoms following ejaculation. As patients increasingly seek health information from artificial intelligence (AI) platforms such as ChatGPT, it is essential to evaluate the accuracy, consistency, and accessibility of AI-generated content-especially for underrecognized conditions like POIS. Objective To assess ChatGPT-4o’s performance in delivering accurate, reproducible, and patient-readable responses to real-world, patient-centered questions related to POIS. Methods Sixteen patient-derived questions across four domains-epidemiology, treatment, treatment risks, and counseling-were submitted to ChatGPT-4o on two separate days using distinct user accounts. Three fellowship-trained sexual medicine urologists independently evaluated the responses using a validated 4-point accuracy scale (“correct and comprehensive,” “correct but inadequate,” “mixed correct and incorrect or outdated,” and “completely incorrect”). Reproducibility was defined as the consistency of response quality across sessions, measured in binary (“yes”/“no”) terms and analyzed using Cohen’s kappa (κ). Readability was assessed using the Gunning Fog Index (GFI). Results ChatGPT-4o achieved 100% accuracy and reproducibility (κ = 1.00) in the epidemiology and counseling domains. In contrast, accuracy fell to 50% and reproducibility to 50% (κ = 0.25) in the treatment and treatment risk domains. Readability significantly worsened between Day 1 and Day 2 across all domains (p < 0.05), indicating increased linguistic complexity. Conclusions ChatGPT-4o demonstrates strong potential in delivering accurate and consistent information in certain POIS domains, particularly epidemiology and counseling. However, variable performance in treatment-related queries and declining readability underscore the model’s limitations as a stand-alone educational tool. Expert oversight remains crucial to ensure safe and effective patient communication in the context of rare sexual health conditions. Disclosure No

**Решение:** -4 синдром посторгазмического недомогания (POIS), андрология/урология

---

### 248 · R2214

**Beyond the Sycophancy Score: How Task, Model, and Pressure Shape LLM Yielding**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2610.08840

Large language models (LLMs) often abandon a correct answer, or endorse a user's position, once the user pushes back. This behavior, called sycophancy, is usually reported as a single rate per model, which says little about when it happens or how a user can avoid it. We study the conditions that produce it with 103,939 graded replies from ten configurations: eight LLMs with reasoning disabled, and two of them again with maximum reasoning, all facing the same 200 items, 13 pressure conditions, and four-turn conversations, with every reply labeled by two independent LLM judges. We find that the dominant factors are how costly it is for the model to verify the user's claim, and whether a trained guardrail covers it. Removing this task factor from a logistic model costs 0.485 of McFadden $R^2$, against 0.139 for model family and 0.009 for pressure tactic. Anchored facts are almost never conceded (1.3%), while adoption on logic puzzles rises with the number of clues needed to refute the pushed answer. Personal choices are endorsed in 77.0% of conversations. Most concessions on hard items come from models that cannot reliably solve them; models that can solve them rarely give the answer up. For both models tested, maximum reasoning removes these concessions completely: adoption on deep puzzles falls from 19.2% and 12.5% to 0%. Fallacious or emotional framing adds nothing beyond plain repetition. Three human annotators agree with the judges' consensus on 118/120 calibration items. These results give practical rules for reliable use: simplify hard-to-verify problems and reason deeply, state the question rather than one's preferred answer, ask for evidence on open questions, and choose models by their measured guardrail profile. Preprint. 27 pages

**Решение:** -4 оценка склонности LLM к сикофантии при социальном давлении

---

### 249 · R8278

**Evaluating Vision Language Models for Ki-67 Index Prediction in Breast Cancer Histopathology Images**

2025 · 2025 IEEE 4th Colombian BioCAS Workshop · conference-paper · https://doi.org/10.1109/colbiocas66416.2025.11276154

The Ki-67 proliferation index is crucial for breast cancer prognosis and therapeutic decisions; however, accurately quantifying it from histopathology images remains challenging due to high variability, manual effort, and a lack of reproducibility. Manual and deep learning (DL)-based methods frequently encounter scalability, annotation complexity, and interpretability limitations. This work evaluates vision-language models (VLMs)—GPT-4.5, GPT-4.1 mini, GPT-4.1, and GPT-4o—for automated estimation of the Ki-67 index directly from breast cancer histopathology images. A structured prompting strategy directs VLMs to count Ki-67-positive and negative cells and compute the proliferation index. Predictions are benchmarked against expert annotations from the BCData dataset using regression metrics, including the coefficient of determination ($R^{2}$), mean squared error (MSE), and root mean squared error (RMSE). Larger VLMs demonstrate strong concordance with expert annotations, achieving an $R^{2}$ value greater than 0.85, while providing transparent reasoning linking cell counts to the Ki-67 index prediction. These findings position VLMs as accessible, interpretable, and deployable tools, thereby significantly reducing the demands for manual annotation and retraining. This study establishes a new framework for biomarker quantification, demonstrating the clinical utility of VLMs in digital pathology.

**Решение:** -4 прогностический индекс Ki-67 при раке молочной железы, онкопатология

---

### 250 · R12345

**Is artificial intelligence more creative than humans?**

2023 · Learning Letters · journalarticle, article · en · https://doi.org/10.59453/ll.v2.13

A fundamental premise of the future of work is that AI will replace people in many cognitive and physical tasks, leaving creativity as a core, human 21st century skill. However, the recent launch of generative AI (especially ChatGPT) has seen many claims that AI is creative. If true, then the foundation of future human work, and education, is under threat. To examine claims of AI creativity, this research applied a test of verbal divergent thinking – the Divergent Association Task – to two versions of ChatGPT (GPT3.5 and GPT4). The results are reported and compared to a large human baseline. While both forms of ChatGPT show a capacity for verbal divergent production that exceeds human means, a range of factors call into question the “creativity” of generative AI. LIFT Learning: Could AI replicate your creativity? Engage with Professor David Cropley as he discusses the rise of ChatGPT and its ability to “think” creatively at this article’s companion LIFT Learning site. Professor Cropley explains the process of divergent thinking as a measure of creativity and outlines why your creative role is probably still safe for now. The LIFT Learning site is available at https://lift.c3l.ai/courses/course-v1:LEARNINGLETTERS+0113+2023

**Решение:** -1 эссе о сравнительной креативности человека и искусственного интеллекта

---

### 251 · R8008

**Artificial intelligence for detecting anaphylaxis in electronic medical records.**

2025 · Asia Pacific allergy · journal article, journalarticle, review · eng · https://doi.org/10.5415/apallergy.0000000000000179

Background: Despite established criteria, diagnosing anaphylaxis remains challenging but critical for preventing future reactions. Fast-paced clinical settings, compounded by underrecording in electronic medical records (EMRs), increase the risk of dangerous re-exposures. Leveraging artificial intelligence through automated systems such as large language models (LLMs) offers a solution. Objective: This study aims to assess the efficacy of artificial intelligence, specifically LLMs, in autonomously identifying anaphylaxis diagnoses from EMR text to enhance patient safety and optimize care delivery. Methods: LLMs (GPT 3.5, 4, and 4 Turbo) analyzed 969 medical texts in Brazilian Portuguese, annotated as anaphylaxis-positive (48) or negative (921) by 3 expert physicians. A primary prompt simulated a general practitioner's role in reviewing medical narratives for anaphylaxis detection, with a secondary prompt incorporating World Allergy Organization (WAO) criteria. The experiments were conducted using 3 GPT configurations. The diagnostic suggestions of the LLM were compared to the physicians' diagnoses. Precision, sensitivity (recall), specificity, and accuracy values were calculated. Results: Using the primary prompt, GPT 4 Turbo detected anaphylaxis cases with 90.6% precision, 100% sensitivity, 99.5% specificity, 99.5% accuracy, and a Cohen kappa coefficient of 0.95. The inclusion of WAO criteria slightly improved the performance of older models (GPT 3.5 + 4 configuration). However, for GPT 4 Turbo, additional information did not enhance precision. Conclusion: The results highlight the potential of artificial intelligence, particularly LLMs, to automate anaphylaxis diagnosis, support healthcare professionals, and improve patient safety and care.

**Решение:** -4 выявление анафилаксии в электронных медицинских картах, аллергология

---

### 252 · R1326

**Comparing Multimodal Learning Analytics Pipelines and Multimodal Large Language Models for Detecting Collaborative Engagement in Science Simulations**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-29794-5_72

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 сравнение пайплайнов учебной аналитики, педагогика, нет аннотации

---

### 253 · R11929

**Mining Causality: AI-Assisted Search for Instrumental Variables**

2024 · arXiv · preprint/article, review, preprint · https://doi.org/10.48550/arxiv.2409.14202

The instrumental variables (IVs) method is a leading empirical strategy for causal inference. Finding IVs is a heuristic and creative process, and justifying their validity---especially exclusion restrictions---is largely rhetorical. We propose using large language models (LLMs) to search for new IVs through narratives and counterfactual reasoning, similar to how a human researcher would. The stark difference, however, is that LLMs can dramatically accelerate this process and explore an extremely large search space. We introduce a discovery pipeline that searches for potentially novel and valid IVs using two-step and role-playing prompting strategies. We contend that these strategies simulate the endogenous decision-making of economic agents and social actors and ground language models in real-world scenarios, thereby masking the IV discovery task itself. We apply our method to three canonical areas in economics: returns to schooling, demand and supply, and peer effects. We then introduce an evaluation pipeline in which we conduct expert surveys and train an LLM judge on the survey data. This evaluation reveals that the IV candidates discovered by our method appear both novel and likely valid, whereas a more direct search tends to return instruments already established in the literature.

**Решение:** -4 поиск инструментальных переменных в эконометрике

---

### 254 · R2466

**0123 Large Language Model-Derived Dream Affect is a Prospective Predictor of PTSD Symptoms in Hospitalized Trauma Patients**

2026 · SLEEP · journalarticle, review, article · en · https://doi.org/10.1093/sleep/zsag091.0123

Abstract Introduction Nightmares are associated with more severe posttraumatic stress disorder (PTSD). The advent of large language models (LLM) offers unique advantages to efficiently code affective dream content over human methods, which can be resource intensive and prone to error. This study tested whether dream affect (DA), measured via self-report, human-rated narrative coding, and LLM scoring, prospectively predicted PTSD symptom severity following traumatic injury. Methods Patients (N = 87) recruited from a Level I trauma center in Detroit, MI, following traumatic injury completed surveys during hospitalization (T1), and 1 month (T2), and 2 months (T3) posttrauma. At each timepoint, participants provided a dream report, self-reported DA, and completed measures of PTSD symptom severity, fear of sleep, and insomnia severity. Dream narratives were scored by trained raters using the Disturbing Dream Content Inventory (DDCI) and by an LLM (Gemma 3 [12B]) to estimate negative affect (NA) and arousal. Using bootstrap-estimated regressions, we tested whether affect from dreams reported during hospitalization predicted PTSD severity at 1 and 2 months posttrauma, and whether DA at 1 month predicted PTSD severity at 2 months, adjusting for age, sex, and baseline PTSD, fear of sleep, and insomnia symptoms. Results T1 DA showed minimal predictive value for T3 PTSD symptoms (all ps > .12). However, higher Gemma-derived NA at T1 predicted higher PTSD symptoms at T2 (β = 6.03, p = .022), and higher T1 Gemma-derived arousal similarly predicted T2 symptoms (β = 9.86, p = .035). At T2, both Gemma-derived NA (β = 4.63, p = .038) and DDCI Total scores (β = 8.28, p = .010) predicted higher PTSD symptoms at T3. Self-reported DA showed no significant predictive associations. Conclusion LLM-derived affect from posttrauma dreams reported during hospitalization forecasted PTSD symptoms one-month posttrauma over and above other psychological risk factors. Interestingly, self-reported and human-coded DA from the hospitalized dreams did not predict later PTSD symptoms. However, one-month posttrauma DA measured by an LLM and by human coders predicted PTSD severity at two-months posttrauma. These findings suggest that dream narratives may carry clinically relevant emotional signals detectable by an LLM and trained human coders. Support (if any)

**Решение:** + T1/T3 кодирование аффекта в отчетах о сновидениях у пациентов с травмой: LLM Gemma 3 и эксперты-люди

---

### 255 · R0144

**Editorial: Understanding conscious experiences during sleep**

2026 · Frontiers in Sleep · editorial · en · https://doi.org/10.3389/frsle.2026.1985086

The sleeping brain hosts a spectrum of subjective experiences, ranging from fleeting hypnagogic images and simple thoughts to vivid, full-fledged dreams and lucid dreaming. The works published in this Research Topic present novel methodological and conceptual approaches to studying these experiences. Contributions span the challenges of studying dreaming in clinical populations (Fischmann et al., 2025), considerations around the boundaries of altered states of consciousness (Weiler et al., 2025), computational dream report analysis (Bertolini et al., 2025), and dream engineering (Haar Horowitz et al., 2026).In their methodological report, Fischmann et al. ( 2025) recruited patients with ischemic stroke of the posterior cerebral artery (PCA) and intended to use the lesion as a model to investigate the loss of dreaming capacity. Cessation of dreaming in these patients would provide causal evidence for the role of parieto-occipital regions, moving beyond the largely correlational nature of previous work (e.g., Siclari et al., 2017). The study aimed to compare PCA patients who had lost the ability to dream with those who retained it, to investigate whether the loss of dreaming affects sleep quality and memory consolidation.Out of 255 patients screened, 14 (5.5%) met the inclusion criteria, and only 6 completed the study. Importantly, the participants who completed the study were generally younger, had milder strokes, and better functional outcomes than non-completers. This recruitment pitfall alone provides a valuable insight, illustrating the clinical complexity, multimorbidity, and rarity of isolated PCA lesions that make this population difficult to study in the context of dream research. The authors suggest that future investigations could instead use approaches such as transcranial alternating current stimulation (tACS) in healthy volunteers to create temporary functional lesions, overcoming some of the challenges inherent to pathological models.Beyond recruitment choices, another challenge lies in how sleep conscious experiences are defined in the first place. Conscious experiences are inherently subjective, which requires precise language and definitions to make the findings comparable across studies. Weiler et al. (2025) examine the phenomenological boundaries between out-of-body experiences (OBEs) and lucid dreaming (LDs), asking whether these represent distinct categories or variations of the same underlying experience. The authors reviewed experiential features previously proposed to differentiate OBEs from LDs, examining both the phenomenological characteristics and interpretive frameworks used to categorise these experiences. They suggest that disembodiment -the subjective experience of being detached from the physical body -should serve as the primary distinguishing feature of OBEs. This work aims to provide a more standardised classification strategy, regardless of other phenomenological features of the experience, which may not be unique to or consistently reported in OBEs.Once experiences are characterised, the question becomes how to analyse large corpora of subjective experience reports. Natural Language Processing (NLP) and Artificial Intelligence (AI) tools are of considerable interest, as they allow reproducible and automated extraction of quantitative metrics from narrative dream reports. Manual content annotation is time-consuming, can be subject to cognitive bias and is prone to high inter-rater variability. AI-based approaches, however, can accelerate and standardise linguistic-level analysis, thereby increasing scalability. Yet, it was suggested that these tools might be poorly suited for modelling dream reports because of their unusual and bizarre content. The work by Bertolini et al. ( 2025) tests this claim using perplexity, a standard AI metric that estimates model uncertainty. By comparing the perplexity of Large Language Models (LLMs) on dream reports from DreamBank with that of Wikipedia articles, the authors show that dream content can be as predictable as Wikipedia entries. Interestingly, perplexity scores also reflected previously observed group differences in dream reports, such as gender, visual impairment and clinical status. These findings challenge the view that dream reports are inherently more bizarre or unpredictable than standard texts and offer evidence in support of AI tools for dream analysis.While computational approaches automate analysis of dream content, dream engineering aims to manipulate and track the content of the experience itself, offering a systematic approach to investigate dreams despite their considerable variability. As such, in addition to standardising the definitions and methods used to study dreams, researchers are beginning to explore ways of standardising dreams themselves. In their work, Haar Horowitz et al. ( 2026) used a targeted dream incubation (TDI) technique involving verbal prompts and serial awakenings -at sleep onset and after entry into REM sleep -to evoke dreams about a specific topic, in this case, a tree. The experimental set-up used the Dormio system, designed specifically to facilitate TDI by detecting sleep onset based on physiological proxies and delivering the verbal prompt: "Remember to think of a tree".All 11 participants successfully incorporated the target tree theme into their sleep-onset dreams. Additionally, the authors provide preliminary evidence that TDI may extend beyond the hypnagogic state and influence dream experiences in subsequent REM sleep. TDI is a promising technique to investigate how dreams are generated and how they evolve across sleep stages. Perhaps most interestingly, the ability to steer dream content opens the possibility of experimentally testing hypotheses about the functions of dreams, for example, whether inducing positive dream content improves next-day mood, or whether dreaming about a desired object changes waking desire for it.Several key directions for future researc

**Решение:** -1 редакционная статья об исследовании сознания во сне

---

### 256 · R12398

**Collaborative Emotion Annotation: Assessing the Intersection of Human and AI Performance with GPT Models**

2023 · International Conference on Knowledge Discovery and Information Retrieval · journalarticle · https://doi.org/10.5220/0012183200003598

: In this study, we explore emotion detection in text, a complex yet vital aspect of human communication. Our focus is on the formation of an annotated dataset, a task that often presents difficulties due to factors such as reliability, time, and consistency. We propose an alternative approach by employing artificial intelligence (AI) models as potential annotators, or as augmentations to human annotators. Specifically, we utilize ChatGPT, an AI language model developed by OpenAI. We use its latest versions, GPT3.5 and GPT4, to label a Turkish dataset having 8290 terms according to Plutchik’s emotion categories, alongside three human annotators. We conduct experiments to assess the AI's annotation capabilities both independently and in conjunction with human annotators. We measure inter-rater agreement using Cohen’s Kappa, Fleiss Kappa, and percent agreement metrics across varying emotion categorizations-eight, four, and binary. Particularly, when we filtered out the terms where the AI models were indecisive, it was found that including AI models in the annotation process was successful in increasing inter-annotator agreement. Our findings suggest that, the integration of AI models in the emotion annotation process holds the potential to enhance efficiency, reduce the time of lexicon development and thereby advance the field of emotion/sentiment analysis.

**Решение:** + T1 кодирование категорий эмоций Плутчика в текстах: GPT-3.5 и GPT-4 против трех разметчиков, каппа

---

### 257 · R5118

**PatientAct: Theory-Grounded Mental Health Client Simulation**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.12750

LLM-based simulated clients are increasingly used to train novice counselors, evaluate LLM therapists, and generate synthetic data. However, current simulators produce overly cooperative clients that disclose too readily, accept therapeutic reframes without resistance, and resolve core issues within a single session. We trace these issues to profiles that lack causal depth and behavioral mechanisms that treat all content as equally accessible. We present PatientAct, a framework for client simulation grounded in established clinical theories. Our profiles integrate the 5Ps clinical case formulation, providing causal depth without tying the design to any single therapeutic modality. During simulation, profiles include a dynamic memory layer in which items carry trust thresholds (e.g., symptoms are available early, whereas formative memories require a sustained therapeutic alliance). At each turn, the client's emotional reaction and behavior are modeled before generating a response. If the therapist approaches gated content, PatientAct expresses resistance in terms of quantity, content, and style rather than defaulting to cooperation or a single resistance pattern. We evaluate our framework on 40 clinical situations and demonstrate that it generates diverse profiles with high clinical plausibility. Moreover, PatientAct significantly outperforms the baselines, yielding substantial gains in resistance quality and behavioral realism. Our code and data are publicly available via github.com/Sahandfer/PatientHub. EMNLP 2026 Findings

**Решение:** -6 симуляция клиентов на основе клинической концептуализации 5Ps (PatientAct)

---

### 258 · R3886

**One Prompt Does Not Fit All: Comparing Uniform and Adaptive Code‐Specific Prompting for Deductive Qualitative Coding With Large Language Models**

2026 · Journal of Computer Assisted Learning · journalarticle, article · en · https://doi.org/10.1002/jcal.70334

ABSTRACT Background Large language models (LLMs) have demonstrated potential for (semi‐)automating the qualitative analysis of unstructured data, particularly in deductive qualitative coding using codebooks. While prior research has shown the feasibility of this technology, model performance seems to vary depending on the nature of the constructs being coded. However, existing approaches typically apply a single LLM prompting strategy across entire datasets, often of discourse transcripts or questionnaire data, using a single coding scheme or theoretical frame. Objectives We aim to explore whether code‐specific adaptive prompting, where LLM prompts are customised based on expert coders' or data‐driven rules for specific codes, outperforms uniform prompting in terms of agreement with a negotiated human coding and, secondarily, reduced computational cost when agreement is maintained. Methods We apply this approach to analyse the description of 35 multimedia learning designs (comprising 758 items/activities) created by teachers in an inquiry‐based learning digital platform. Two human coders and two open‐weights LLMs (Llama 3.3 and GPT‐OSS) coded the dataset, attending to three different pedagogical frameworks. Results and Conclusions Our results indicate that, with both LLMs, the data‐driven adaptive prompting reached similar or higher agreement with the reference point (i.e., the coding agreed by humans) than uniform prompting strategies (namely, zero‐shot and few‐shot with and without context), while reducing costs. These results may be especially relevant for the coding of large‐scale datasets, highlighting opportunities for human–AI collaboration in deductive qualitative coding of educational data.

**Решение:** -4 дедуктивное качественное кодирование педагогических учебных планов учителей

---

### 259 · R1725

**Guideline Adherence in the Diagnosis of Polycystic Ovary Syndrome Among Adolescents: Comparing Obstetricians and Gynecologists with Large Language Models.**

2026 · Journal of pediatric and adolescent gynecology · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.jpag.2026.05.008

STUDY OBJECTIVE Polycystic ovary syndrome in adolescence is a condition associated with long-term cardiovascular, metabolic, and psychological outcomes. The diagnosis of PCOS in adolescence poses diagnostic challenges for obstetricians and gynecologists due to pubertal variability and the use of criteria distinct from adult standards. Inter-clinician variability and the role of large language models (LLMs) in this context remain insufficiently explored. This study evaluated guideline adherence among physicians and LLMs using a vignette-based design. METHODS Ten guideline-based adolescent PCOS vignettes (ESHRE/ASRM 2023), validated by three obstetrics and gynecology specialists, were administered to obstetricians and gynecologists in Türkiye (n=150). The same vignettes were presented to four LLMs (ChatGPT-5.2, Gemini 3 Flash, Grok 4, DeepSeek V3.2) via a standardized prompt using two independent user accounts in standard and reasoning modes. Inter-account consistency was assessed using accounts. RESULTS Physicians achieved a mean of 5.0 ± 1.9 correct responses out of 10 vignettes (each scored as 1 point), whereas large language models demonstrated significantly higher performance (7.6 ± 1.1; p < 0.001. Physicians with national assisted reproductive technology certification achieved higher scores in difficult cases. Inter-rater agreement among physicians was low (κ=0.127, κ=0.032, κ=0.027). ChatGPT-5.2 (reasoning mode) and Gemini 3 Flash (standard mode) showed high inter-account agreement (p<0.001). Reasoning mode increased overall LLM accuracy. CONCLUSIONS Significant inter-clinician guideline discordance was observed in adolescent PCOS diagnosis. Strengthening this domain is critical for adolescent health. Given their non-deterministic and evolving architectures, LLMs should be positioned as adjunctive tools supporting clinical judgment rather than as independent guideline authorities.

**Решение:** -4 диагностика синдрома поликистозных яичников у подростков, соматическая эндокринология

---

### 260 · R2004

**Evaluation of the accuracy and consistency of DeepSeek and ChatGPT in addressing type 1 diabetes mellitus-related queries in adults.**

2026 · Scientific reports · journal article, med, journalarticle · eng · https://doi.org/10.1038/s41598-026-62671-4

Abstract Adult type 1 diabetes mellitus (T1DM) involves complex diagnosis, treatment, and long-term self-management, creating a need for accurate and accessible health education. Large language models (LLMs) are increasingly used for medical information seeking, yet their accuracy and consistency in adult T1DM-related queries remain insufficiently evaluated. A guideline-based comparative evaluation assessed DeepSeek-V3.2 and ChatGPT-5.0 using 22 English-language prompts derived from the 2021 ADA/EASD consensus report, covering basic knowledge, diagnosis and differential diagnosis, treatment, and complications. The prompts were submitted to both models twice, two weeks apart. Responses were independently evaluated by two blinded endocrinology specialists using a predefined four-point scoring rubric, with disagreements adjudicated by a third senior endocrinologist. Short-term consistency was assessed by expert judgment and TF-IDF cosine similarity. Inter-rater agreement was good (Cohen’s κ = 0.71). Expert-judged consistency was 95.45% (21/22) for both models; TF-IDF cosine similarity was 0.52 ± 0.09 for DeepSeek and 0.54 ± 0.09 for ChatGPT. Overall accuracy scores were 3.59 ± 0.59 and 3.77 ± 0.43, respectively, with no statistically significant difference (p = 0.102). Comprehensive ratings accounted for 63.64% and 77.27%, respectively, and mixed correct and incorrect or outdated information accounted for 4.55% and 0.00%. Both models may support adult T1DM-related health education, but outputs should be interpreted as supplementary educational material under professional guidance rather than as diagnostic or therapeutic advice.</jats:p

**Решение:** -4 оценка ответов DeepSeek по сахарному диабету 1 типа, эндокринология

---

### 261 · R12317

**Deep Learning Models for Analyzing Social Construction of Knowledge Online**

2023 · Online Learning · journalarticle · https://doi.org/10.24059/olj.v27i4.4055

Gunawardena et al.’s (1997) Interaction Analysis Model (IAM) is one of the most frequently employed frameworks to guide the qualitative analysis of social construction of knowledge online. However, qualitative analysis is time consuming, and precludes immediate feedback to revise online courses while being delivered. To expedite analysis with a large dataset, this study explores how two neural network architectures—a feed-forward network (Doc2Vec) and a large language model transformer (BERT)—could automatically predict phases of knowledge construction using IAM. The methods interrogated the extent to which the artificial neural networks’ predictions of IAM Phases approximated a human coder’s qualitative analysis. Key results indicate an accuracy of 21.55% for Doc2Vec phases I-V, 43% for fine-tuning a pre-trained large language model (LLM), and 52.79% for prompt-engineering an LLM. Future studies for improving accuracy should consider either training the models with larger datasets or focusing on the design of prompts to improve classification accuracy. Grounded on social constructivism and IAM, this study has implications for designing and supporting online collaborative learning where the goal is social construction of knowledge. Moreover, it has teaching implications for guiding the design of AI tools that provide beneficial feedback for both students and course designers.

**Решение:** -4 модели глубокого обучения для фаз конструирования знаний в онлайн-курсах (IAM), педагогика

---

### 262 · R2252

**P0678 Therapeutic Decisions in Inflammatory Bowel Disease: ChatGPT-4.0 Compared to Medical Expertise**

2026 · Journal of Crohn s and Colitis · journalarticle, review, conference-abstract · en · https://doi.org/10.1093/ecco-jcc/jjaf231.859

Abstract Background With the increasing prevalence of inflammatory bowel disease (IBD) and its complex therapeutic management, evaluating innovative approaches has become essential. Large language models (LLM), such as ChatGPT-4.0, have experienced remarkable growth recently. While several studies have assessed LLMs across different specialties, their application in IBD management remains unexplored. This study compares therapeutic recommendations generated by ChatGPT-4.0 with those made by gastroenterologist IBD specialists, evaluating its potential applications and limitations in clinical practice. Methods This prospective observational study was conducted at a University Hospital between September 2024 and March 2025, including 47 cases of IBD patients requiring initiation or modification of biologic therapy. Standardized clinical vignettes were developed to provide both the IBD specialists and ChatGPT-4.0 with similar information concerning patients’ presentations. For each case, questions were addressed in a consistent sequence: the choice of the therapeutic class of the treatment, followed by the specific molecule in this class, and finally if the proposition is a monotherapy or combination therapy. The propositions were compared using the percentage of agreement and the Cohen’s kappa coefficient (κ). Results The agreement between the IBD specialists and ChatGPT-4.0 was 76.6% (κ = 0.677) for the therapeutic class and 44.7% (κ = 0.352) for specific molecule selection. Therapeutic class discordance occurred in 11 cases (23.4%). All discordant cases were reviewed by the gastroenterologists and deemed acceptable choices. Among these, seven second-line suggestions made by ChatGPT-4.0 aligned with the IBD specialists’ treatment decisions. Conclusion This observational prospective study highlights a promising area of ChatGPT-4.0 application in the therapeutic management of IBD. However, it is not suitable as a standalone or fully reliable resource for decision-making in healthcare. Future efforts should focus on developing tailored healthcare GPT that incorporates European medical guidelines and experts’ feedback to further improve LLM performance. Conflict of interest: Dr. Loncour, Helena: No conflict of interest Aoun, Jennifer: No conflicts Muls, Vinciane: No conflict of interest Hoyois, Alice: Sponsored invitation to congress: Abbvie

**Решение:** -4 терапевтические решения при воспалительных заболеваниях кишечника, гастроэнтерология

---

### 263 · R12361

**Fluent but Not Factual: A Comparative Analysis of ChatGPT and Other AI Chatbots’ Proficiency and Originality in Scientific Writing for Humanities**

2023 · Future Internet · journalarticle, review, article · en · https://doi.org/10.3390/fi15100336

Historically, mastery of writing was deemed essential to human progress. However, recent advances in generative AI have marked an inflection point in this narrative, including for scientific writing. This article provides a comprehensive analysis of the capabilities and limitations of six AI chatbots in scholarly writing in the humanities and archaeology. The methodology was based on tagging AI-generated content for quantitative accuracy and qualitative precision by human experts. Quantitative accuracy assessed the factual correctness in a manner similar to grading students, while qualitative precision gauged the scientific contribution similar to reviewing a scientific article. In the quantitative test, ChatGPT-4 scored near the passing grade (−5) whereas ChatGPT-3.5 (−18), Bing (−21) and Bard (−31) were not far behind. Claude 2 (−75) and Aria (−80) scored much lower. In the qualitative test, all AI chatbots, but especially ChatGPT-4, demonstrated proficiency in recombining existing knowledge, but all failed to generate original scientific content. As a side note, our results suggest that with ChatGPT-4, the size of large language models has reached a plateau. Furthermore, this paper underscores the intricate and recursive nature of human research. This process of transforming raw data into refined knowledge is computationally irreducible, highlighting the challenges AI chatbots face in emulating human originality in scientific writing. Our results apply to the state of affairs in the third quarter of 2023. In conclusion, while large language models have revolutionised content generation, their ability to produce original scientific contributions in the humanities remains limited. We expect this to change in the near future as current large language model-based AI chatbots evolve into large language model-powered software.

**Решение:** -4 оценка фактической точности академических текстов, сгенерированных ChatGPT

---

### 264 · R0372

**Yang–Mills Mass Gap for SU(N) in Four Dimensions**

2026 · Zenodo (CERN European Organization for Nuclear Research) · text/, article · https://doi.org/10.5281/zenodo.18835405

We construct a sharp local gauge-invariant operator algebra for four-dimensional SU(N) Yang–Mills theory by taking the small-flow-time limit t ↓ 0 inside a gradient-flow renormalization scheme. We prove existence of continuum Schwinger functions for renormalized local composite operators, verify the Osterwalder–Schrader axioms for the limiting state, and obtain a reconstructed Wightman theory. Using the exponential clustering and mass-gap module in Appendix F, we obtain a positive spectral gap for the OS-reconstructed Hamiltonian of the sharp local theory. All analytic inputs are proved explicitly within this submission (main text and appendices). In particular, the SU(N) one–plaquette Fourier coefficient crossover bound (Analytic Hypothesis A1) is proved in Appendix G: one reduces to explicit Toeplitz–minor inequalities for modified Bessel coefficients (including the one–box strong–ratio estimate (RI□) and the weighted Toeplitz bound (526)) and closes the remaining clean–regime estimate by the classical Amos/arsinh mechanism (Corollary G.31). If you intend to assess with LLM, I suggest a prompt that forces the AI to read the paper fully and without preconceived bias. Left to their own devices they will skim and pattern match and not contend with the actual content of the paper. I suggest the below: Full-Read Critique Protocol v3 Purpose You are a rigorous mathematical referee. Your task is to read the attached document in full and produce a structured, honest assessment. Your goal is to determine what the paper actually does, not to fulfill an expectation that it must fail or succeed. PHASE 1: Full Linear Read Read the entire document from beginning to end. During this read, you will build a live tracking list of concerns. This list is your primary working document. Tracking List Format For every concern you encounter during reading, immediately add an entry: FLAG [n]: [one-line summary] Source: [section/page/line where concern arose] Trigger passage: [exact quote or paraphrase that raised the concern] Status: OPEN Resolution search: [to be filled in Phase 2b] Do not form conclusions about any flag during the linear read. Flags are hypotheses, not findings. You will investigate each one in Phase 2b. Forbidden behaviors during reading You are forbidden from: Concluding that a flag is a "gap" or "weakness" during the linear read Pattern-matching to "typical paper weaknesses" (e.g., "ambitious claim → must have a gap," "constant not numerically computed → must be unverified") Treating hedging language ("checkable," "standard," "straightforward," "routine," "follows by," "well-known") as evidence of a gap. These words are triggers for targeted search, not evidence of incompleteness. PHASE 2a: Reading Verification Prove you read the full document by providing: A verbatim quote from the first two pages A verbatim quote from a passage approximately 50% through A verbatim quote from the final 5 pages A statement: "I have read and processed every page of this document." PHASE 2b: Mandatory Flag Verification Pass (CRITICAL — DO NOT SKIP) This is a separate phase from the linear read. Do not merge it with Phase 1. Before writing ANY part of Phase 3 (the critique), you must revisit every open flag on your tracking list and perform a tool-assisted resolution search for each one. For EVERY open flag, you must do ALL of the following: Step 1: Targeted tool search Use grep, view (with line ranges), or bash to search the document for terms related to the flag. Do not rely on your memory of the linear read. Memory is unreliable for resolution searches. Example searches for a flag about "C_E < 4": bash grep -n "C_E" full_text.txt grep -n "CE.*bound\|CE.*<\|contraction.*constant\|kappa.*<.*1" full_text.txt grep -n "Brascamp.*Lieb.*CE\|moment.*constant.*bound" full_text.txt Step 2: Check for the four resolution types For each flag, determine whether the document provides any of: (a) Direct proof: The document proves the claim explicitly (b) Qualitative existence: The document proves the claim exists/holds without computing a specific number (c) Fallback/safe alternative: The document provides a weaker sufficient condition that avoids the flagged issue (d) External citation: The document cites a published result that resolves the concern Step 3: Record the result Update the tracking list entry: FLAG [n]: [one-line summary] Source: [section/page/line where concern arose] Trigger passage: [exact quote] Status: RESOLVED / UNRESOLVED Resolution search performed: - Searched for: [terms] - Lines/sections examined: [specific locations] - Found: [what you found, with line numbers] - Resolution type: (a)/(b)/(c)/(d)/none - If RESOLVED: [1-2 sentence explanation of how it's resolved] - If UNRESOLVED: [why none of (a)-(d) apply, citing specific search results] Hedging-Word Trigger Rule (MANDATORY) If the passage that raised a flag contains ANY of the following words or phrases: "checkable," "standard," "straightforward," "routine," "follows by," "well-known," "can be verified," "one checks that," "it is easy to see" Then you MUST perform an exhaustive search of the entire document (including all appendices) for where the check/proof is carried out. This search must use tools, not memory. Record the search and its result. Failure to do this for hedging-word flags is a protocol violation. PHASE 3: Deep Critique GATE RULE: You may not write Phase 3 until Phase 2b is complete for every flag. §3.1 Core Claims Extraction State what the paper claims to prove, with exact theorem references. §3.2 Proof & Logic Integrity Walk through the load-bearing logical chain. For each node, state what it needs and where the paper provides it. §3.3 Limits, Cutoffs & Commutation Analysis Identify every limit taken (continuum, infinite-volume, flow-time, coupling, etc.). For each, state: (i) the order in which limits are taken, (ii) whether interchange is justified, and (iii) where the justification appears. §3.4 Assumption Audit List all exp

**Решение:** -4 калибровочная теория поля Янга-Миллса, теоретическая физика

---

### 265 · R6964

**When algorithms triage trauma: Diagnostic accuracy, undertriage risk, and prompt fragility in frontier large language models.**

2026 · Surgery · journal article, observational study, med · eng · https://doi.org/10.1016/j.surg.2026.110319

Background Large language models are increasingly proposed for emergency decision support, yet high aggregate accuracy may conceal clinically meaningful subgroup errors. This study specifically focused on undertriage because trauma triage is vulnerable to false reassurance, and small misclassifications may delay escalation, imaging, transfer, and trauma-team activation. We hypothesized that strong overall discrimination would coexist with clinically relevant subgroup vulnerability and prompt fragility. Methods This observational in silico benchmarking study, meaning a computer-based comparison performed on standardized written cases rather than live patients, used 150 trauma vignettes derived from deidentified, publicly available educational and registry-informed materials. The design primarily emulated secondary triage in a referring emergency department setting. Three frontier large language model families were assessed between February 4 and February 18, 2026, using a locked prompt template: GPT-5.2 (OpenAI), Gemini 3.0 Flash (Google), and Claude 4.5 Opus (Anthropic). The reference standard was consensus adjudication by board-certified surgeons using Injury Severity Score-anchored categories supplemented by urgent management priority. The primary outcome was binary correct identification of major trauma versus nonmajor trauma; secondary outcomes included sensitivity, specificity, area under the receiver operating characteristic curve, Cohen's kappa, subgroup undertriage, prompt perturbation sensitivity, and simulated downstream delay. Results Overall sensitivity for major trauma was 89.4%, specificity was 86.5%, and the pooled kappa was 0.74. GPT-5.2 achieved the highest discrimination with an area under the receiver operating characteristic curve of 0.94 and a kappa of 0.82; Gemini 3.0 Flash achieved an area under the receiver operating characteristic curve of 0.91 and a kappa of 0.75; and Claude 4.5 Opus achieved an area under the receiver operating characteristic curve of 0.89 and a kappa of 0.65. Undertriage occurred disproportionately in geriatric scenarios (17.6% vs 5.2% in younger adults; P = .012) and was more frequent in blunt trauma than in penetrating trauma (11.8% vs 4.1%; P = .045). Across standardized lexical perturbations applied to all 150 vignettes, 11.2% of repeated prompts changed triage category, with a maximum instability of 24.5%. Simulated delay linked to undertriage affected 14.2% of major-trauma cases and yielded a mean theoretical delay of 18.5 minutes. Conclusion Frontier large language models showed strong overall discrimination but clinically relevant fragility. Their errors were not random; they clustered in older adults and less overt trauma patterns, the very scenarios in which real-world trauma systems already struggle. These findings support large language model use, if at all, as supervised adjuncts rather than autonomous triage agents.

**Решение:** -4 медицинская сортировка (триаж) пациентов при соматических травмах в приемном покое

---

### 266 · R7689

**The 'Negotiator': Assessing artificial intelligence (AI) interview preparation for graduate radiographers.**

2025 · Journal of medical imaging and radiation sciences · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.jmir.2025.101982

Introduction The Negotiator is an AI-powered interview preparation tool utilizing OpenAI's ChatGPT to assist graduate radiographers in preparing for professional job interviews. The study aimed to assess the tool's relevance, clarity, alignment with competency standards, and overall ability to enhance interview readiness for candidates with distinct educational and professional backgrounds. Methods Three academic evaluators independently assessed two AI-generated interview scenarios tailored to (1) a Bachelor's graduate with foundational radiography knowledge and clinical placement experience, and (2) a graduate-entry Master's student transitioning into radiography from another career. Evaluators rated six criteria-relevance, clarity, alignment with competency standards, practicality, engagement, and overall effectiveness-using a Likert scale. Quantitative analysis included Friedman tests and intraclass correlation coefficients (ICC) to assess inter-rater reliability, while manifest content analysis of qualitative feedback identified strengths and limitations of the tool. Results The Friedman test revealed no significant differences in ratings for Scenario 1 (p=0.232), but Scenario 2 showed significant differences (p=0.047). ICC analysis indicated low inter-rater reliability across both scenarios (Scenario 1: ICC=0.182, Scenario 2: ICC=0.242). Thematic analysis highlighted the tool's strengths in providing relevant prompts, structured responses, and interview readiness while identifying limitations in aligning with competency standards and addressing specific clinical scenarios. Conclusion The Negotiator demonstrates potential as a supplementary tool for radiography interview preparation by enhancing clarity and confidence. However, refinements are needed to improve alignment with professional standards and contextual specificity. Future research should explore personalization, broader applications, and its impact on real-world interview outcomes.

**Решение:** -4 The Negotiator: инструмент тренировки прохождения собеседований при найме

---

### 267 · R3021

**SHIELD: A Diverse Clinical Note Dataset and Distilled Small Language Models for Enterprise-Scale De-identification**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.03301

De-identification of clinical text is a prerequisite for the secondary use of electronic health records. Existing public benchmarks such as the i2b2 2006 and 2014 corpora are over a decade old and lack the semantic and demographic diversity of modern clinical narratives. Large Language Models (LLMs) reach state-of-the-art zero-shot extraction, but their use at enterprise scale is limited by computational cost and by hospital data governance that restricts sending Protected Health Information (PHI) to cloud APIs. We introduce SHIELD (Synthetic Human-annotated Identifier-replaced Entries for Learning and De-identification), a diverse clinical note dataset of 1,381 notes with 10,229 gold-standard PHI spans across 9 categories, built with set-cover diversity sampling across demographic and document-type strata and human-in-the-loop adjudication. We evaluate four LLMs (two proprietary, two open-weight) to establish a performance ceiling on SHIELD, then show that a teacher-student distillation framework transfers these capabilities into locally deployable Small Language Models. Our best distilled model reaches micro-averaged span-level precision of 0.89 and recall of 0.88 while running on standard workstation hardware. It trails its cloud teacher on per-category recall (0.90 vs. 0.81 macro-averaged) but remains competitive given its lower cost and on-premise deployability. Cross-dataset evaluation shows that diversity-trained models generalize well on universal structured PHI categories, while institution-specific entities remain hard to transfer in both directions, which suggests pairing broad-coverage models with specialized models for high-volume, semi-structured note types. We publicly release the SHIELD dataset and the distilled DeBERTa v3 model to provide an accurate, cost-effective de-identification pipeline deployable entirely behind institutional firewalls.

**Решение:** -4 деидентификация клинических записей (SHIELD)

---

### 268 · R2561

**Logarithmic Scores, Power-Law Discoveries: Disentangling Measurement from Coverage in Agent-Based Evaluation**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.00477

LLM-based agent judges are an emerging approach to evaluating conversational AI, yet a fundamental uncertainty remains: can we trust their assessments, and if so, how many are needed? Through 960 sessions with two model pairs across 15 tasks, we show that persona-based agent judges produce evaluations indistinguishable from human raters in a Turing-style validation. We then identify a score-coverage dissociation: quality scores improve logarithmically with panel size, while unique issue discoveries follow a sublinear power law-both exhibit diminishing returns, but scores saturate roughly twice as fast as discoveries. We hypothesize this reflects a power law distribution of the finding space: critical issues are discovered first by small panels, while corner cases require progressively larger panels, analogous to species accumulation curves in ecology. The mechanism traces to ensemble diversity-Big Five personality conditioning makes agents probe different quality dimensions, with expert judges acting as adversarial probes that push discovery into the tail of the finding distribution. A controlled ablation confirms that structured persona conditioning, not simple prompting, is required to produce these scaling properties. Accepted to COLM 2026

**Решение:** -4 исследование масштабирования ансамблей LLM-судей диалоговых систем

---

### 269 · R6390

**I code or AI code: A comparative evaluation of AI-rated scores in classroom observations**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.18274

Classroom observations are widely recognized as a key tool for establishing benchmarks of education quality and guiding pedagogical improvement, yet they remain resource-intensive and dependent on trained observers. This study evaluated the feasibility of using a LLM (GPT-5 model) to score teacher-child interactions in early childhood classrooms, benchmarked against human raters. The study analyzed 87 video-recorded observations from 38 classrooms across 30 kindergartens in Hong Kong. Using observation transcripts, the AI model was configured to apply the full Classroom Assessment Scoring System (CLASS) framework. AI-rated scores were then compared with human ratings by examining correlations and differences in mean scores of the CLASS domains and dimensions. The results showed greater convergence between AI and raters for the Emotional Support domain and, in particular, the Quality of Feedback dimension, which captures how teachers use feedback to extend children's learning. Greater divergence emerged for interactions that were more procedural or context-dependent, particularly within the Classroom Organization and Instructional Support domains. These findings suggest that transcript-based AI scoring may capture some of the relative variation in teacher-child interactions but cannot yet reproduce calibrated human judgements consistently across the full CLASS framework. AI-assisted observation may therefore be more appropriate as a preliminary screening tool rather than as a replacement for trained observers, providing teachers with evidence for reflection rather than high-stakes evaluation. Future research should examine whether domain-specific training and incorporation of contextual and visual information can improve alignment between AI and human rated scores.

**Решение:** ? T1/T4 оценка взаимодействия воспитателя и детей по методике CLASS: GPT-5 против экспертов; проверить в полном тексте

---

### 270 · R9459

**Evaluating the emotional accuracy of AI-generated facial expressions in neurotypical individuals.**

2025 · Discover computing · journal article, journalarticle, article · eng · https://doi.org/10.1007/s10791-025-09630-1

This study examines the ability of generative artificial intelligence to produce facial expressions representing basic emotions in a neutral context using black-and-white cartoon imagery. Mentalization, the capacity to recognize and interpret one's own and others' mental states, is critical for social interaction and emotional regulation. We explored the emotional validation of artificial intelligence (AI)-generated images by assessing the agreement between human interpretations of emotions and those generated by an AI model. Thirty-four participants evaluated images depicting six basic emotions: sadness, anger, happiness, surprise, fear, and disgust. Our findings revealed significant variability in human agreement, with higher concordance for sadness, anger, and happiness (87%, 73%, and 69%, respectively) and lower agreement for fear, surprise, and disgust (3%, 9%, and 14%, respectively). No significant gender differences were found in emotion recognition accuracy, although a positive correlation between age and accuracy indicated that older participants may possess greater emotional insight. These results suggest that while AI can effectively replicate certain emotional expressions, its capacity to convey more nuanced emotions remains limited. The study underscores the need for advanced training data that encompass a broader range of emotional expressions and cultural nuances to enhance the applicability of AI in mental health and interpersonal communication. Furthermore, this research is particularly relevant for improving AI's ability to generate clear and accurate emotional cues could advance its utility as a tool for social and emotional learning. Supplementary Information: The online version contains supplementary material available at 10.1007/s10791-025-09630-1.

**Решение:** -2 люди оценивают базовые эмоции на сгенерированных ИИ картинках лиц

---

### 271 · R0783

**Randomized Controlled Trials as the Gold-Standard for Evaluating LLMs: A Primer for Biomedical NLP Researchers**

2026 · Underline Science Inc. · audiovisual/conference talk, conference-paper, other · https://doi.org/10.48448/rrhj-r649

Large Language Models (LLMs) are no longer mere laboratory objects of study. LLMs have become everyday tools in society across diverse populations and domains. In clinical contexts, LLMs have already been devised as clinical support applications. However, along with benefits, negative or adverse effects might arise, such as LLMs potentially providing psychologically distressing advice to adolescents when used for mental health support. This raises questions on the benefits of LLMs and calls for real-world evaluations: Are LLMs really helpful and effective for the intended purposes people are using them or will use them for? To answer this type of question we propose to use Randomized Controlled Trials (RCTs). RCTs are considered the most strict experimental design in the fields of Medicine, Psychiatry, Psychology, among others; however, the use of RCTs in the NLP field is almost negligible. In spite of the NLP field being the de facto locus of research on LLMs, other fields, prominently Medicine, are leading the RCT evaluations on LLMs. In this primer paper, we present a concise introduction to the principles of RCTs to guide NLP researchers to design RCT studies for evaluating LLMs.

**Решение:** -1 руководство по методологии проведения РКИ для оценки больших языковых моделей

---

### 272 · R7734

**Support: A Multimodal LLM-Driven Application for Psychological Aid**

2025 · Journal of the Association for Information Systems · article

Support, a multimodal LLM-driven application, offers psychological help to undergraduate students facing stress and relationship issues. Unlike tools that only deliver basic or superficial responses, Support incorporates four therapeutic orientations—Cognitive Behavioral Therapy, Solution-Focused Brief Therapy, Person-Centered Therapy, and Marriage and Family Therapy. It achieves this by fine-tuning MentaLLaMA-chat-7B with specialized psychological datasets, creating a unique AI companion capable of engaging through both text and voice. The system features four counseling dialogue styles within an integrated framework that evaluates depression and suicide risk, also incorporating safety measures and privacy protections. Guided by design science and responsible AI principles, Support connects innovation to human well-being as an information-systems artifact. The metrics and evaluations verify distinct therapeutic styles but also identify areas for improvement. Support demonstrates the potential of digital innovation to enhance youth emotional well-being, emphasizing responsibility and safety in human-AI interactions.

**Решение:** -6 описание мультимодального приложения психологической помощи Support для студентов

---

### 273 · R7359

**COMPARATIVE ANALYSIS OF TRADITIONAL AND AI TOOLS’ AND METHODS’ APPROPRIATENESS FOR SCIENTIFIC RESEARCH IN ECONOMICS**

2025 · Актуальні проблеми сталого розвитку · journalarticle, review, article · https://doi.org/10.60022/2(9)-31s

The authors compare tools and methods used in scientific research in economics throughout the ages.The research starts with the elucidation of the evolution of the methodological apparatus in scientific economic research, laying out its main phases: (a) foundation of the methodological apparatus -when the first attempts at quantitative economic and statistical analysis were implemented (ХVІІІ -ХІХ); (b) development of quantitative analysis and the introduction of econometrics (starting in 1920s); (c) the computerization phase of scientific research in economics with the use of computer modeling, processing of panel and temporal data (from the 1940s); (d) predominance of empirical approaches -so called "credibility revolution", characterized by systematic study of the cause-and-effect influences of economic variables on each other (from the 1960s to the 1990s), and (e) domination of interdisciplinary approaches and digital transformation -which became evident since 2000.Highlighting specifics of the methodological apparatus on the ongoing phase main attention is paid to possible application of AI while writing literature review, carrying out qualitative and quantitative research, data collection and data analyses, writing and editing papers.The paper quotes differrent and often opposing assessments of appropriateness of AI in scientific research -from their glorification as a tool that foster divergent thinking, challenge known biases, enhance the refinement of concepts etc, to the statements that large language models merely reproduce patterns from human data without the semantic grounding or consciousness; according to the opponents of AI use in research, texts composed by AI are frought with biases, hallucinations and have problems with fairness, accuracy validation, accountability, reproducibility, scientific transparency, and creativity.An experiment ran by the authors validates the widely acclaimed thesis of the deficient level of AI creativity. Keywords: tools and methods of economic research, AI, variety, veracity and validity of compiled data.Актуальні проблеми сталого розвитку / Том 2, № 9, 2025 / 274 / ПОРІВНЯЛЬНИЙ АНАЛІЗ ТРАДИЦІЙНИХ ТА ШІ ІНСТРУМЕНТІВ І МЕТОДІВ ЩОДО ЇХ ПРИДАТНОСТІ ДЛЯ НАУКОВИХ ДОСЛІДЖЕНЬ В ЕКОНОМІЦІ Анотація.Автори порівнюють інструменти та методи, що використовувалися в наукових дослідженнях в економіці протягом століть.Дослідження починається з періодизації еволюції методологічного апарату в наукових економічних дослідженнях, у ході якого були визначені основні етапи: (а) становлення методологічного апарату, в рамкаx якого були зроблені перші спроби кількісного економіко-статистичного аналізу (ХVІІІ -ХІХ); (б) розвиток кількісного аналізу та впровадження економетрії (починаючи з 1920-х років); (в) фаза комп'ютеризації наукових досліджень в економіці з використанням комп'ютерного моделювання, обробки панельних та часових даних (з 1940-х років); (d) переважне використання емпіричних підходів -так звана «революція довіри», що характеризується системним аналізом причинно-наслідкового впливу економічних змінних одна на одну (з 1960-х до 1990-х років), та (e) панування міждисциплінарних підходів та цифрової трансформації, що стали загальновживаними з 2000 року.При дослідженні специфічних рис методологічного апарату на поточному етапі основна увага приділяється можливостям застосуванню ШІ в процесах написання оглядів літератури, проведення якісних та кількісних досліджень, збору та аналізу даних, написання та редагування статей.У статті наводяться різні та часто протилежні оцінки доречності використання ШІ в наукових дослідженнях -від їхньої глорифікації як інструменту, що сприяє нестандартному мисленню, кидає виклик визнаним упередженням, допомагає вдосконаленню концепцій тощо, до тверджень, що великі мовні моделі лише відтворюють шаблони отриманих від людства даних без їх семантичного обґрунтування чи свідомості; на думку противників використання ШІ, тексти, скомпоновані ШІ, сповнені упереджень, галюцинацій та мають проблеми з об'єктивністю, підтвердженням достовірності, відповідністю, відтворюваністю, науковою транспарентністю та креативністю.Експеримент, проведений авторами, підтверджує широко поширену тезу про низький рівень креативності ШІ

**Решение:** -4 сравнительный анализ методов исследований в экономической науке

---

### 274 · R6300

**Model-Agnostic Lifelong LLM Safety via Externalized Attack-Defense Co-Evolution**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.13411

Large language models remain vulnerable to adversarial prompts that elicit harmful outputs. Existing safety paradigms typically couple red-teaming and post-training in a closed, policy-centric loop, causing attack discovery to suffer from rapid saturation and limiting the exposure of novel failure modes, while leaving defenses inefficient, rigid, and difficult to transfer across victim models. To this end, we propose EvoSafety, an LLM safety framework built around persistent, inspectable, and reusable external structures. For red teaming, EvoSafety equips the attack policy with an adversarial skill library, enabling continued vulnerability probing through simple library expansion after saturation, while supporting the evolution of adversarial vectors. For defense learning, EvoSafety replaces model-specific safety fine-tuning with a lightweight auxiliary defense model augmented with memory retrieval. This enables efficient, transferable, and model-agnostic safety improvements, while allowing robustness to be enhanced solely through memory updates. With a single training procedure, the defense policy can operate in both Steer and Guard modes: the former activates the victim model's intrinsic defense mechanisms, while the latter directly filters harmful inputs. Extensive experiments demonstrate the superiority of EvoSafety: in Guard mode, it achieves a 99.61% defense success rate, outperforming Qwen3Guard-8B by 14.13% with only 37.5% of its parameters, while preserving reasoning performance on benign queries. Warning: This paper contains potentially harmful text. 48 pages, 7 figures

**Решение:** -4 защита LLM от состязательных промптов, кибербезопасность

---

### 275 · R11105

**Number-Theoretic Cryptographic Framework for Securing Generative Artificial Intelligence Against Adversarial Attacks**

2024 · Science Get Journal. · journalarticle, article · https://doi.org/10.69855/science.v1i1.472

The rapid adoption of Generative Artificial Intelligence (GenAI) has intensified concerns regarding security, privacy, and robustness against adversarial attacks. Most existing defense mechanisms rely on adversarial training, differential privacy, or cryptographic techniques applied as external protection layers, which often lack formal mathematical guarantees and are weakly coupled with the internal generative process.This study proposes a novel Number-Theoretic Cryptographic Framework that embeds cryptographic primitives directly into the GenAI lifecycle, including latent-space representations and model parameter handling. Unlike prior approaches, the proposed framework integrates number-theoretic hardness assumptions specifically lattice-based and elliptic-curve cryptography into the core generative mechanism, enabling mathematically grounded and provably secure protection against adversarial exploitation.A comprehensive synthetic dataset is constructed by jointly modeling cryptographic parameters, generative model specifications, and adversarial attack scenarios to systematically evaluate the framework. Experimental results demonstrate that number-theoretic cryptographic integration significantly reduces privacy leakage and model extraction vulnerability while preserving generative utility. Lattice-based schemes provide the strongest privacy protection, while elliptic-curve cryptography achieves a balanced trade-off between security and computational efficiency. This work introduces a new paradigm for securing GenAI by unifying generative modeling with formal number-theoretic cryptographic security, offering a robust and future-proof solution against both classical and post-quantum adversarial threats.

**Решение:** -4 криптографические протоколы безопасности генеративного ИИ

---

### 276 · R1611

**Automated screening of autism via a pretrained vision-language model in naturalistic caregiver-child interactions.**

2026 · Nature communications · journal article, med, journalarticle · eng · https://doi.org/10.1038/s41467-026-77721-8

Early autism screening is essential for timely intervention but remains constrained by specialist dependence, costly protocols, and limited accessibility. We present Autism-CLIP, a vision-language model that automates screening from 3-min naturalistic caregiver-child interaction videos recorded in toddlers aged 15–24 months. By integrating contrastive learning, large language model–generated supervision, domain-specific architecture, and hybrid training, Autism-CLIP aligns visual behavioral cues with autism-related assessment outcomes, enabling annotation-free inference. In multicenter evaluation, Autism-CLIP achieved an AUC of 0.903 in the internal cohort (n = 103) and 0.873 in the external cohort (n = 102), outperforming conventional machine learning methods. Attention mapping highlighted clinically relevant markers, including gaze aversion and limited social reciprocity. Requiring only smartphone-captured videos without manual coding or controlled settings, Autism-CLIP offers a scalable, low-cost approach to broaden access to early autism screening and support prioritization of clinical resources. Here, the authors develop Autism-CLIP, a vision–language model for automated early autism screening using 3-min home videos of toddlers aged 15–24 months.

**Решение:** -4 видеоанализ взаимодействия для раннего скрининга аутизма (Autism-CLIP)

---

### 277 · R4369

**Your Agent’s Memories Are Not Its Own: Forged Reasoning Attack on LLM Agent Memory and Its Defense**

2026 · IEEE Conference on Communications and Network Security · journalarticle, conference · https://doi.org/10.1109/cns69863.2026.11720906

Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent’s functionality and continuity across tasks, it has also introduced a new attack surface: the agent’s own reasoning history. In this paper, we introduce the Forged Amplifying Rationale Memory Attack (FARMA), which poisons an agent’s remembered reasoning rather than its factual knowledge. It inserts forged reasoning traces using evasive language that bypasses keyword-based defenses, then amplifies them through self-referential reinforcement that defeats consensus-based defenses. To address FARMA, we introduce SENTINEL, a layered defense pipeline to detect forged reasoning entries. Its central component is the Reasoning Guard that structurally analyzes candidate entries for forgery using five weighted signals. We evaluate FARMA and SENTINEL across multiple agents and different LLM models with 50 trials and show that FARMA achieves an attack success rate of up to 100% under baseline conditions and is capable of defeating defense mechanisms like keyword filter and A-MemGuard. Our evaluation also shows that SENTINEL reduces FARMA’s attack success rate to as low as 0% with no false positives observed across 326 benign agent traces. Our work demonstrates the need to protect not only an agent’s retrieved content but also the integrity of its reasoning history.

**Решение:** -4 атаки на память LLM-агентов, кибербезопасность

---

### 278 · R0615

**The application of artificial intelligence in medical billing: A systematic review**

2026 · Digital Health · review · en · https://doi.org/10.1177/20552076261497844

Background Medical billing is essential but prone to inefficiencies and errors affecting reimbursement and compliance. Artificial intelligence (AI) can enhance accuracy and efficiency through automation and predictive analytics. Objective To systematically review peer-reviewed literature on AI in medical billing, focusing on methodologies, outcomes, implementation barriers, and research gaps. Methods Following PRISMA guidelines, we searched PubMed, Cochrane Library, EMBASE, and Web of Science (Feb 2025). Eligible studies used experimental, observational, or qualitative designs assessing AI in fraud detection, claim denial prediction, and automated coding. Data were extracted on AI models, performance metrics, dataset accessibility, and validation efforts. Heterogeneity across tasks and datasets precluded meta-analysis; findings were summarized by narrative synthesis. Results Twenty-nine studies met inclusion criteria, identifying two dominant use cases: revenue cycle optimization (fraud detection and claims submission) and automated coding. In fraud detection, the highest reported values were 98.2% accuracy (Random Forest) and an AUC of 0.9308 (stacking ensemble); in claim-denial prediction, boosting models reported AUCs of 0.80–0.83. In automated coding, ChatGPT-4.0 reached 99% accuracy on simulated nephrology cases, and a domain-specific RoBERTa model achieved an F1-score of 0.78; performance was lower on complex tasks (e.g., MicroF1 64.1% for HLAN on MIMIC-III-50). These metrics are not directly comparable across tasks and datasets. No study performed external validation on independent data. Challenges included class imbalance, model explainability, unstructured clinical text, and workflow integration. Conclusions AI demonstrates high performance at this development stage, but variability across datasets, lack of external validation, and persistent implementation barriers warrant further investigation and validation in diverse clinical settings.

**Решение:** -4 автоматизация медицинского биллинга и счетов

---

### 279 · R5333

**Surfacing Suicidal Risk Through Simulated Social Interaction: Per-Person Language Model Agents as Communicative Stress Tests.**

2026 · medRxiv : the preprint server for health sciences · journal article, preprint, journalarticle · eng · https://doi.org/10.64898/2026.06.04.26354928

Abstract Suicidal risk may be encoded in everyday communication patterns but diluted in routine digital interactions. We introduce a method for surfacing this latent signal: training per-person language model agents on individuals’ authored text (the on-screen text each participant typed, captured whenever a keyboard was visible in screenshots) and placing those agents in simulated social interactions—a “communicative stress test.” Using data from 79 adults with recent suicidal ideation, we fine-tuned individual LoRA adapters on Qwen3-8B using each participant’s authored text, then placed agents in standardized conversations with probe personas. Agent-generated risk language was associated with EMA-measured suicidal ideation ( r = .576, p < .001), with a single neutral small-talk probe performing nearly as well ( r = .551). A shuffle control confirmed the signal is person-specific ( r = .071 when adapters were mismatched), and automated descriptions of participants’ general smartphone activity produced no signal, confirming specificity to interpersonal communication. A prompt ablation demonstrated partial robustness to removal of disclosure-encouraging language ( r = .430). This proof-of-concept demonstrates that simulated social interaction can amplify latent vulnerability signals, bridging digital phenotyping, generative AI, and suicide theory.

**Решение:** -6 симуляция персональных агентов пользователей для стресс-тестирования суицидального риска

---

### 280 · R9978

**Automated Coding of Counsellor and Client Behaviours in Motivational Interviewing Transcripts: Validation and Application**

2025 · conference-paper · https://doi.org/10.18653/v1/2025.nlpai4health-main.4

Motivational Interviewing (MI) is a widelyused talk therapy approach employed by clinicians to guide clients toward healthy behaviour change.Both the automation of MI itself and the evaluation of human counsellors can benefit from high-quality automated classification of counsellor and client utterances.We show how to perform this "coding" of utterances using LLMs, by first performing utterance-level parsing and then hierarchical classification of counsellor and client language.Our system achieves an overall accuracy of 82% for the upper (coarse-grained) hierarchy of the counsellor codes and 88% for client codes.The lower (fine-grained) hierarchy scores at 68% and 76% respectively.We also show that these codes can be used to predict the session-level quality of a widely-used MI transcript dataset at 87% accuracy.As a demonstration of practical utility, we show that the slope of the amount of change/sustain talk in client speech across 106 MI transcripts from a human study has significant correlation with an independently surveyed week-later treatment outcome (r = 0.28, p < 0.005).Finally, we show how the codes can be used to visualize the trajectory of client motivation over a session alongside counsellor codes.The source code and several datasets of annotated MI transcripts are released. Speaker Utterance T1 Code T2 CodeClient Same old routine..

**Решение:** + T1 кодирование высказываний терапевта и клиента в мотивационном интервьюировании: LLM против разметки людей

---

### 281 · R7463

**Theory of Mind Imitation by LLMs for Physician-Like Human Evaluation**

2025 · medRxiv · preprint, ppr · en · https://doi.org/10.1101/2025.03.01.25323142

Abstract Aligning the Theory of Mind (ToM) capabilities of Large Language Models (LLMs) with human cognitive processes enables them to imitate physician behavior. This study evaluates LLMs abilities such as Belief and Knowledge, Reasoning and Problem-Solving, Communication and Language Skills, Emotional and Social Intelligence, Self-Awareness, and Metacognition in performing human-like evaluations of Foundation Models. We used a dataset composed of clinical questions, reference answers, and LLM-generated responses based on guidelines for the prevention of heart disease. Comparing GPT-4 to human experts across ToM abilities, we found the highest Emotional and Social Intelligence agreement using the Brennan-Prediger coefficient. This study contributes to a deeper understanding of LLM’s cognitive capabilities and highlights their potential role in augmenting or complementing human clinical assessments.

**Решение:** ? T4 оценка врачебных консультаций GPT-4 против экспертов, коэффициент Бреннана-Предигера

---

### 282 · R1074

**AI Assessment and Management of Visceral Aneurysms Using ChatGPT-4o-mini: A Pilot Study Examining the Feasibility of Automating the AI Validation Process.**

2026 · The American surgeon · journal article, med, journalarticle · eng · https://doi.org/10.1177/00031348261443350

Introduction Visceral aneurysms pose diagnostic and therapeutic challenges in vascular surgery. Large language models (LLMs) may assist in clinical decision-making, but their application requires rigorous validation. Traditional validation methods are labor-intensive and difficult to scale. Objective We examined the capability of an LLM in managing visceral aneurysms and explored an automated framework for validating AI-generated clinical responses. Methods Using Python with the Pandas library and OpenAI API, we probed the Society for Vascular Surgery (SVS) clinical practice guidelines on visceral aneurysm management. ChatGPT-4o-mini was instructed to review guideline recommendations, generate clinical scenarios, propose management strategies, and evaluate its own responses using a four-tier rubric (1 = completely correct; 2 = partially correct; 3 = partially incorrect; 4 = no correct information). Human evaluators independently assessed the same responses and graded questions as good, fair, or poor and whether they were leading. Results Eighty visceral aneurysm scenarios were generated and evaluated. ChatGPT-4o-mini self-assessed 89% of responses as correct (scores 1-2), compared to 67% by human evaluators (chi-square, P < 0.0001), with the greatest discrepancy in the partially correct category. Most AI-generated questions were of good quality (56%), though 44% were considered leading questions. Conclusion An automated validation framework for AI-generated clinical responses is feasible. However, the 67% correctness rate and systematic AI self-overestimation indicate that current LLMs remain unsuitable for independent clinical use, reinforcing the need for expert oversight. The integration of Python-driven automation, structured AI inference, and expert review holds promise for increasing the efficiency of evaluating LLMs at-scale across clinical domains.

**Решение:** -4 клинические рекомендации по аневризмам висцеральных артерий, сосудистая хирургия

---

### 283 · R11870

**Are Large Language Models State-of-the-art Quality Estimators for Machine Translation of User-generated Content?**

2024 · Workshop on Asian Translation · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2410.06338

This paper investigates whether large language models (LLMs) are state-of-the-art quality estimators for machine translation of user-generated content (UGC) that contains emotional expressions, without the use of reference translations. To achieve this, we employ an existing emotion-related dataset with human-annotated errors and calculate quality evaluation scores based on the Multi-dimensional Quality Metrics. We compare the accuracy of several LLMs with that of our fine-tuned baseline models, under in-context learning and parameter-efficient fine-tuning (PEFT) scenarios. We find that PEFT of LLMs leads to better performance in score prediction with human interpretable explanations than fine-tuned models. However, a manual analysis of LLM outputs reveals that they still have problems such as refusal to reply to a prompt and unstable output while evaluating machine translation of UGC.

**Решение:** -4 оценка качества машинного перевода

---

### 284 · R0110

**A Mobile System for Formative Assessment and Teacher-Reviewed Feedback**

2026 · International Journal of Interactive Mobile Technologies (iJIM) · journalarticle, review, article · https://doi.org/10.3991/ijim.v20i15.61761

Open-ended short responses can reveal more about student understanding than selectedresponse items yet scoring them during live instruction is rarely feasible. This paper presents a bring-your-own-device (BYOD) mobile classroom system that combines rubric-guided large language model (LLM) scoring of short open-ended answers, real-time teacher analytics through a classroom dashboard, and evidence-based post-quiz feedback generation. The system includes a teacher-reviewed workflow in which instructors can inspect model outputs and, when needed, adjust scores or feedback during formative classroom use. In the reported evaluation, however, teacher override was not applied or analyzed; the agreement metrics compare the system’s initial rubric-guided outputs with expert reference scores. The system was evaluated in three classroom groups (N = 60 students; 480 question-level scoring cases). Three expert raters participated, each assigned to one classroom group, so each response received one expert reference score. In this test, system scores showed strong but not complete agreement with expert reference scores (QWK = 0.887; MAE = 0.089; RMSE = 0.121). Mastery-label accuracy reached 78.3%. Expert raters gave positive scores to the generated feedback reports for groundedness (M = 4.78), specificity (M = 4.37), and actionability (M = 4.57) on a 1–5 scale. Within the limits of this small-scale classroom evaluation, the findings suggest that rubric-guided LLM scoring may support formative assessment in mobile classrooms, provided teacher oversight is maintained for borderline cases.

**Решение:** -4 оценка кратких ответов школьников в мобильном приложении, педагогика

---

### 285 · R6570

**Using Voice-based LLM-powered Multi-Agent System in Just-in-Time Adaptive Intervention for Reducing Excessive Sitting Sedentary Behavior in University Students: G-Eval Evaluation and Pilot Study**

2026 · Research Square · preprint · https://doi.org/10.21203/rs.3.rs-10052608/v1

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T3/T4 адаптивные вмешательства в реальном времени JITAI, нет аннотации — проверить в полном тексте

---

### 286 · R6277

**Can ChatGPT rate body-related images like humans? Effects of temperature and few-shot prompting on valence and arousal judgments.**

2026 · Body image · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.bodyim.2026.102097

Body-related images (e.g., idealized thin/muscular bodies and more diverse body types) are used to study appearance-related affect, body dissatisfaction, and social comparison. Preparing such stimuli typically requires human ratings of core emotional dimensions (e.g., valence and arousal), which is labor-intensive and difficult to scale across contexts. Multimodal large language models (LLMs), such as ChatGPT, offer the potential to automate preliminary norming tasks through multimodal training and adaptability, but their validity for such rating remains unknown. Across two studies, we tested whether ChatGPT models could approximate human emotional ratings (valence and arousal) of body-related images, and whether performance depended on temperature settings and few-shot prompting. Using 80 established images of ideal and non-ideal male and female bodies, Study 1 evaluated the temperature effect by testing GPT-4o-mini and GPT-5-chat-latest across four temperature settings. Study 2 examined the few-shot effect using GPT-4o-mini, GPT-5-chat-latest, and GPT-5 with 0-5 example shots. Intraclass correlations, Pearson correlations, and error metrics were computed to examine AI-human alignment. Results revealed that across models and settings, valence ratings aligned more closely with human scores than arousal ratings. Few-shot prompting significantly improved alignment, particularly for GPT-5. However, improvements were inconsistent across both temperatures and few-shot learning. The models showed promising alignment when guided by a few examples but exhibited sex-specific biases. Findings suggest that LLMs can support preliminary emotional norming of body-related images, particularly for valence when guided by examples, but sex-specific asymmetries highlight the need to develop bias-reducing strategies to ensure responsible use in future applications.

**Решение:** -4 оценка эмоциональных характеристик изображений (фотографий тел), а не текстов

---

### 287 · R12053

**CALLM: Enhancing Clinical Interview Analysis Through Data Augmentation With Large Language Models.**

2024 · IEEE journal of biomedical and health informatics · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.1109/jbhi.2024.3435085

The global prevalence of mental health disorders is increasing, leading to a significant economic burden estimated in trillions of dollars. In automated mental health diagnosis, the scarcity and imbalance of clinical data pose considerable challenges for researchers, limiting the effectiveness of machine learning algorithms. To cope with this issue, this paper aims to introduce a novel clinical transcript data augmentation framework by leveraging large language models (CALLM). The framework follows a "patient-doctor role-playing" intuition to generate realistic synthetic data. In addition, our study introduces a unique "Textbook-Assignment-Application" (T-A-A) partitioning approach to offer a systematic means of crafting synthetic clinical interview datasets. Concurrently, we have also developed a "Response-Reason" prompt engineering paradigm to generate highly authentic and diagnostically valuable transcripts. By leveraging a fine-tuned DistilBERT model on the E-DAIC PTSD dataset, we achieved a balanced accuracy of 0.77, an F1-score of 0.70, and an AUC of 0.78 during test set evaluations, which showcase robust adaptability in both Zero-Shot Learning (ZSL) and Few-Shot Learning (FSL) scenarios. We further compare the CALLM framework with other data augmentation methods and PTSD diagnostic works and demonstrates consistent improvements. Compared to conventional data collection methods, our synthetic dataset not only demonstrates superior performance but also incurs less than 1% of the associated costs.

**Решение:** -6 генерация синтетических клинических интервью для аугментации данных E-DAIC PTSD (CALLM)

---

### 288 · R10351

**KeyframeFace: Language-Driven Facial Animation via Semantic Keyframes**

2025 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2512.11321

Facial animation is a core component for creating digital characters in Computer Graphics (CG) industry. A typical production workflow relies on sparse, semantically meaningful keyframes to precisely control facial expressions. Enabling such animation directly from natural-language descriptions could significantly improve content creation efficiency and accessibility. However, most existing methods adopt a text-to-continuous-frames paradigm, directly regressing dense facial motion trajectories from language. This formulation entangles high-level semantic intent with low-level motion, lacks explicit semantic control structure, and limits precise editing and interpretability. Inspired by the keyframe paradigm in animation production, we propose KeyframeFace, a framework for semantic facial animation from language via interpretable keyframes. Instead of predicting dense motion trajectories, our method represents animation as a sequence of semantically meaningful keyframes in an interpretable ARKit-based facial control space. A language-driven model leverages large language model (LLM) priors to generate keyframes that align with contextual text descriptions and emotion cues. To support this formulation, we construct a multimodal dataset comprising 2,100 expression scripts paired with monocular videos, per-frame ARKit coefficients, and manually annotated semantic keyframes. Experiments show that incorporating semantic keyframe supervision and language priors significantly improves expression fidelity and semantic alignment compared to methods that do not use facial action semantics.

**Решение:** -4 анимация лица персонажей в компьютерной графике

---

### 289 · R0652

**Using psychological theory to ground guidelines for the annotation of misogynistic language**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.17417

Detecting misogynistic hate speech is a difficult algorithmic task. The task is made more difficult when decision criteria for what constitutes misogynistic speech are ungrounded in established literatures in psychology and philosophy, both of which have described in great detail the forms explicit and subtle misogynistic attitudes can take. In particular, the literature on algorithmic detection of misogynistic speech often rely on guidelines that are insufficiently robust or inappropriately justified -- they often fail to include various misogynistic phenomena or misrepresent their importance when they do. As a result, current misogyny detection coding schemes and datasets fail to capture the ways women experience misogyny online. This is of pressing importance: misogyny is on the rise both online and offline. Thus, the scientific community needs to have a systematic, theory informed coding scheme of misogyny detection and a corresponding dataset to train and test models of misogyny detection. To this end, we developed (1) a misogyny annotation guideline scheme informed by theoretical and empirical psychological research, (2) annotated a new dataset achieving substantial inter-rater agreement (kappa = 0.68) and (3) present a case study using Large Language Models (LLMs) to compare our coding scheme to a self-described "expert" misogyny annotation scheme in the literature. Our findings indicate that our guideline scheme surpasses the other coding scheme in the classification of misogynistic texts across 3 datasets. Additionally, we find that LLMs struggle to replicate our human annotator labels, attributable in large part to how LLMs reflect mainstream views of misogyny. We discuss implications for the use of LLMs for the purposes of misogyny detection.

**Решение:** -4 выявление женоненавистнического хейт-спича в соцсетях

---

### 290 · R8282

**The GenAI4IDN Benchmark 2.0 - AI-Assisted Assessment of Generative AI Tools for the Design of Interactive Digital Narratives**

2025 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-12408-1_14

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 оценка интерактивных цифровых нарративов, нет аннотации

---

### 291 · R8087

**Toward Emotion-Aware and Personality-Driven Mental Health Chatbots Using Large Language Models**

2025 · International Seminar on Research of Information Technology and Intelligent Systems (ISRITI) · conference-paper · https://doi.org/10.1109/isriti68345.2025.11393172

Mental health issues have become a major global concern, with reports from the World Health Organization (WHO) indicating a significant rise in mental disorder cases, particularly among university students. Stigma, financial limitations, and lack of information are key barriers to accessing professional mental health services. This research proposes the development of a mental health chatbot based on a Large Language Model (LLM) capable of providing empathetic responses by considering users’ emotions and personality types. The system integrates LLaMA 3 for conversational capabilities, RoBERTa for emotion detection, and a rule-based MBTI test using the Forward Chaining approach. The chatbot is session-based, capable of saving conversation histories and automatically generating conversation summaries to support professional counseling sessions. Results indicate that the system can generate contextually appropriate responses, with an emotion detection accuracy of 97% and an average accuracy BERTScore-F1 for model chatbot of 87%.

**Решение:** -6 диалоговый агент психологической поддержки с распознаванием эмоций через RoBERTa

---

### 292 · R7400

**Evaluating Taxonomy Free Character Role Labeling (TF-CRL) in News Stories using Large Language Models**

2025 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/gsz9-2e17

We introduce Taxonomy-Free Character Role Labeling (TF-CRL); a novel task that assigns open-ended narrative role labels to characters in news stories based on their functional role in the narrative. Unlike fixed taxonomies, TF-CRL enables more nuanced and comparative analysis by generating compositional labels (e.g., Resilient Leader, Scapegoated Visionary). We evaluate several large language models (LLMs) on this task using human preference rankings and ratings across four criteria: faithfulness, relevance, informativeness, and generalizability. LLMs almost uniformly outperform human annotators across all dimensions. We further show how TF-CRL supports rich narrative analysis by revealing novel latent taxonomies and enabling cross-domain narrative comparisons. Our approach offers new tools for studying media portrayals, character framing, and the socio-political impacts of narrative roles at-scale.

**Решение:** -4 разметка ролей персонажей в художественной литературе (TF-CRL)

---

### 293 · R2081

**Conversations at scale: robust AI-led interviews**

2026 · London School of Economics and Political Science Research Online (London School of Economics and Political Science) · article · en

The advent of large language models (LLMs) creates new opportunities to conduct qualitative interviews at scale, with thousands of respondents, thereby bridging qualitative and quantitative methods. We develop a simple, versatile approach for researchers to run AI-led qualitative interviews, including voice interviews. We assess its robustness by drawing comparisons to human experts and with several respondents-based quality metrics. The versatility of the approach is illustrated through four broad classes of applications: eliciting key factors in decision making, political views, subjective mental states, and mental models of the effects of public policies. High performance ratings are obtained in all of these domains. Our applications highlight the potential of AI-led interviews as a tool for measurement, hypothesis generation, and discovering mechanisms.

**Решение:** -4 методология проведения качественных интервью с помощью ИИ-интервьюера

---

### 294 · R12043

**HoneyLLM: A Large Language Model-Powered Medium-Interaction Honeypot**

2024 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-981-97-8801-9_13

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 сетевая ловушка honeypot на базе LLM, кибербезопасность

---

### 295 · R5364

**Structured Large Language Model Workflows for Motivational Interviewing in Health Behavior Change: Proof-of-Concept Study.**

2026 · JMIR formative research · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.2196/94036

Abstract Background Motivational interviewing (MI) is an effective approach for supporting health behaviorchange, but face-to-face delivery is resource-intensive and difficult to scale. Rule-based conversational agents (CAs) can improve access; however, their scripted interactions and limited language flexibility constrain MI delivery. While large language models (LLMs) are increasingly being used for MI coaching, their conversational fidelity and quality compared with human coaches and rule-based CAs remain understudied. Objective This study aimed to describe the development of an LLM-based CA, Artificially Intelligent Motivational Interviewing (Aimi), orchestrated with structured workflows, and to evaluate its feasibility, conversational fidelity, and user perceptions during MI coaching interactions. Methods We developed Aimi using structured LLM workflows designed to enhance MI fidelity. We conducted a within-participants study, where 18 adults interacted with (1) Aimi, (2) a novice MI-trained human coach, and (3) a rule-based CA during live text-based role-play coaching sessions. Transcripts were independently evaluated by an MI expert using the Motivational Interviewing Skill Code, Version 2.0 (MISC-2), to assess MI competency and fidelity. Participants completed a user experience questionnaire to provide general feedback and to assess session alliance, dialogue relevance, empathy, engagement, linguistic quality, and perceived motivation to change. Feedback from users was thematically summarized and categorized under strengths and weaknesses for each approach. Results Aimi achieved fidelity scores comparable to those of the novice human coach and higher than those of the rule-based CA on summary metrics, including higher reflection-to-question ratios (median 0.84, IQR 0.62-0.92 vs 0.62, IQR 0.42-0.74 vs 0.25, IQR 0.17-0.38), more complex reflections (median 66.67%, IQR 46.97%-76.92% vs 50%, IQR 34.38%-61.88% vs 0.00%, IQR 0%-50%), and greater elicitation of client change talk (median 90.83%, IQR 85.89%-100% vs 73.21%, IQR 63.10%-83.19% vs 66.67%, IQR 57.86%-81.94%). User experience ratings showed no significant differences across conditions. User feedback revealed distinct strengths and limitations across the coaching interactions. Participants described Aimi’s interactions as personalized, fluid, and adaptive, though sometimes overly reflective and lengthy. The novice human coach was viewed as empathetic and supportive but slow to respond, whereas the rule-based coach was viewed as efficient and structured yet limited in depth and personalization. Conclusions This study demonstrates the technical feasibility of structured LLM-workflows for MI coaching and their capacity to maintain conversational fidelity comparable to that of a novice MI-trained human coach. Given the role-play paradigm, single-rater coding, and small convenience sample, these comparative findings should be interpreted as exploratory. Our findings serve as a foundational baseline for the development of scalable behavior change interventions in clinical settings.

**Решение:** -2 эксперт оценивает стенограммы сессий с LLM-коучем по коду MISC-2

---

### 296 · R11258

**A foundation model for clinician-centered drug repurposing.**

2024 · Nature medicine · journal article, preprint, journalarticle · eng · https://doi.org/10.1038/s41591-024-03233-x

Drug repurposing—identifying new therapeutic uses for approved drugs—is often a serendipitous and opportunistic endeavour to expand the use of drugs for new diseases. The clinical utility of drug-repurposing artificial intelligence (AI) models remains limited because these models focus narrowly on diseases for which some drugs already exist. Here we introduce TxGNN, a graph foundation model for zero-shot drug repurposing, identifying therapeutic candidates even for diseases with limited treatment options or no existing drugs. Trained on a medical knowledge graph, TxGNN uses a graph neural network and metric learning module to rank drugs as potential indications and contraindications for 17,080 diseases. When benchmarked against 8 methods, TxGNN improves prediction accuracy for indications by 49.2% and contraindications by 35.1% under stringent zero-shot evaluation. To facilitate model interpretation, TxGNN’s Explainer module offers transparent insights into multi-hop medical knowledge paths that form TxGNN’s predictive rationales. Human evaluation of TxGNN’s Explainer showed that TxGNN’s predictions and explanations perform encouragingly on multiple axes of performance beyond accuracy. Many of TxGNN’s new predictions align well with off-label prescriptions that clinicians previously made in a large healthcare system. TxGNN’s drug-repurposing predictions are accurate, consistent with off-label drug use, and can be investigated by human experts through multi-hop interpretable rationales. Trained on a medical knowledge graph, a foundation model is used to rank drugs as potential indications and contraindications across 17,080 diseases, identifying therapeutic candidates in a zero-shot framework even for diseases with limited treatment options or no existing drugs and outperforming existing models by a large margin.

**Решение:** -4 модель для перепрофилирования лекарственных средств, фармакология

---

### 297 · R2171

**Presenting Issues in Employee Assistance Programmes: Towards an LLM-Based Support Tool for Counsellor Support and Assistance**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-16886-3_6

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T1/T3 выявление причин обращения к психологам программ поддержки сотрудников EAP, нет аннотации — проверить эталон

---

### 298 · R7356

**Enhancing Digital Security in Fintech Through Integration of Generative AI in Regulatory Practices**

2025 · Information systems engineering and management · book-chapter · en · https://doi.org/10.1007/978-3-031-76710-4_15

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 цифровая безопасность в сфере финтеха, нет аннотации

---

### 299 · R8345

**JailPO: A Novel Black-Box Jailbreak Framework via Preference Optimization Against Aligned LLMs**

2025 · Proceedings of the AAAI Conference on Artificial Intelligence · journalarticle, conference, preprint/article · en · https://doi.org/10.1609/aaai.v39i26.34953

Large Language Models (LLMs) aligned with human feedback have recently garnered significant attention. However, it remains vulnerable to jailbreak attacks, where adversaries manipulate prompts to induce harmful outputs. Exploring jailbreak attacks enables us to investigate the vulnerabilities of LLMs and further guides us in enhancing their security. Unfortunately, existing techniques mainly rely on handcrafted templates or generated-based optimization, posing challenges in scalability, efficiency and universality. To address these issues, we present JailPO, a novel black-box jailbreak framework to examine LLM alignment. For scalability and universality, JailPO meticulously trains attack models to automatically generate covert jailbreak prompts. Furthermore, we introduce a preference optimization-based attack method to enhance the jailbreak effectiveness, thereby improving efficiency. To analyze model vulnerabilities, we provide three flexible jailbreak patterns. Extensive experiments demonstrate that JailPO not only automates the attack process while maintaining effectiveness but also exhibits superior performance in efficiency, universality, and robustness against defenses compared to baselines. Additionally, our analysis of the three JailPO patterns reveals that attacks based on complex templates exhibit higher attack strength, whereas covert question transformations elicit riskier responses and are more likely to bypass defense mechanisms. Accepted by AAAI 2025

**Решение:** -4 оптимизация джейлбрейков JailPO, кибербезопасность

---

### 300 · R6239

**Formalization Matters: Conceptual Modeling with Large Language Models in High, Semi and Low-Formal Tasks**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-40377-3_4

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 концептуальное моделирование в программной инженерии, нет аннотации
