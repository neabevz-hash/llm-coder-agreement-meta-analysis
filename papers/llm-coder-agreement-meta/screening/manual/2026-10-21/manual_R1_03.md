# Ручной отбор, часть 3

Ручной отбор, часть 3: записи 301–450 из 1000. Эти записи вы размечаете сами, вместо проходов ИИ (deviations.md, D3); это случайные 1000 записей из тех, что ИИ ещё не разметил (зерно 20261024). **Меток ИИ здесь нет и не будет.** Ваше решение окончательное: «+» и «?» идут на полный текст. Размечайте в любом порядке и в несколько заходов.

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

### 301 · R6283

**S-Eval: Towards Automated Safety Evaluation with Enhancement for Large Language Models**

2026 · ACM Transactions on Software Engineering and Methodology · journalarticle, article · en · https://doi.org/10.1145/3805706

Large language models (LLMs) have revolutionized natural language processing with their transformative and emergent capabilities. However, recent evidence indicates that LLMs can produce harmful content that violates social norms, raising significant concerns regarding the safety ramifications of deploying these advanced models. Thus, it is both critical and imperative to perform a rigorous and comprehensive safety evaluation of LLMs before deployment. Despite this need, owing to the extensiveness of LLM generation space, it still lacks a unified and standardized risk taxonomy to systematically reflect the LLM content safety, automated assessment techniques to explore the potential risks efficiently, as well as defense mechanisms for timely mitigation. To bridge the striking gap, we propose S-Eval, a novel LLM-based automated Safety Evaluation framework. S-Eval incorporates three key components, i.e., an expert testing LLM \(\mathcal{M}_{t}\) , a novel safety critique LLM \(\mathcal{M}_{c}\) , and constitutional defense. The expert testing LLM \(\mathcal{M}_{t}\) is responsible for automatically generating test cases in accordance with the proposed risk management (including 8 risk dimensions and a total of 102 subdivided risks). The safety critique LLM \(\mathcal{M}_{c}\) can provide quantitative and explainable safety evaluations for better risk awareness of LLMs. Furthermore, the constitutional defense enables differentiated safety constraints in a non-intrusive manner. In contrast to prior works, S-Eval differs in significant ways: (i) efficient – we construct a multi-dimensional and open-ended benchmark comprising 220,000 test cases across 102 risks utilizing \(\mathcal{M}_{t}\) and conduct safety evaluations for 29 influential LLMs via \(\mathcal{M}_{c}\) on our benchmark. The entire process is fully automated and requires no human involvement. (ii) effective – extensive validations show that S-Eval facilitates a more thorough assessment and better perception of potential LLM risks, where \(\mathcal{M}_{c}\) not only accurately quantifies the risks of LLMs but also provides explainable and in-depth insights into their safety, and our constitutional defense method can effectively mitigate the safety risks. (iii) adaptive – S-Eval can be flexibly configured and adapted to the rapid evolution of LLMs and accompanying new safety threats, test generation methodologies, safety critique approaches, and defense mechanisms. We further study the impacts of hyper-parameters, languages, and reasoning on model safety, which may lead to promising directions for future research. S-Eval has been deployed at our industrial partner, Alibaba Group, for automated safety evaluation of multiple LLMs serving millions of users, demonstrating its effectiveness in real-world scenarios.

**Решение:** -4 оценка безопасности LLM от вредоносного контента (S-Eval)

---

### 302 · R6420

**Ethical implications of high attrition in AI-based mental health interventions: a systematic review and meta-analysis.**

2026 · BMC medical ethics · journal article, systematic review, meta-analysis · eng · https://doi.org/10.1186/s12910-026-01510-7

BACKGROUND: The integration of AI-based conversational agents (CAs) in mental health aims to bridge the global "treatment gap." However, high user attrition poses a critical ethical challenge, potentially compromising care continuity and distributive justice. This study quantifies attrition rates in AI-driven mental health interventions and evaluates their ethical implications for user autonomy and research integrity. METHODS: Following PRISMA 2020 guidelines and registered with PROSPERO, this systematic review and meta-analysis synthesized evidence from six databases through September 2025. Employing a convergent parallel mixed-methods design, we analyzed 39 independent studies. A random-effects model was used to calculate pooled attrition rates, while meta-regression explored the correlation between attrition and clinical efficacy (improvement in depressive/anxiety symptoms). Qualitative narrative synthesis was further applied to contextualize user experiences. RESULTS: The meta-analysis revealed a pooled attrition rate of 17.04% (95% CI, 11.46%-23.38%) for AI interventions. Generative AI-based CAs exhibited significantly lower attrition rates (9.25%) compared to retrieval-based systems (23.12%, p = 0.044). Subgroup analysis identified intervention target, delivery platform, interaction mode, engagement reminders and safety measures as key moderators of engagement. Crucially, a significant inverse association between retention and treatment efficacy was observed in depression interventions, where lower attrition correlated with larger effect sizes (β = 0.97, p = 0.043). Furthermore, a pervasive "reporting gap" exists regarding the qualitative reasons for user withdrawal. CONCLUSIONS: High attrition rates in AI-based mental health interventions may represent more than technical disengagement, potentially implicating the ethical principles of beneficence and non-maleficence by disrupting the continuity of care. While generative AI shows promise in fostering a perceived therapeutic alliance and mitigating attrition, the observed association between disengagement and diminished efficacy suggests a risk of exacerbating structural health disparities. To address these challenges, we propose the "Ethics-oriented Engagement Framework"(EEF), which integrates transparent accountability, autonomy balance, safety-by-design, and inclusive beneficence. This framework provides a normative roadmap to reconcile the tension between promoting user engagement and upholding the foundational ethical mandates of patient safety and justice. TRIAL REGISTRATION: PROSPERO (CRD420251275051).

**Решение:** -1 систематический обзор и метаанализ отсева в цифровых вмешательствах в психическом здоровье

---

### 303 · R5909

**Addressing Key Challenges in Narrative Understanding**

2026 · IRIS Research product catalog (Sapienza University of Rome) · dissertation · en · https://hdl.handle.net/11573/1769343

Narrative text is one of the most demanding domains for automatic language understanding. At book scale, characters can be represented through varying names, pronouns, and implicit references, and answering questions often requires evidence distributed across entire chapters. Current NLP systems, developed primarily for short documents, face four interconnected limitations: unreliable entity tracking, evaluation metrics that correlate poorly with human judgments, retrieval pipelines that miss implicitly referenced passages, and insufficient adaptation to longer narrative inputs. In this thesis, we address all four through new resources, evaluation frameworks, and methods specifically designed for book-scale Narrative Understanding. The first challenge, reliable entity tracking, naturally leads to Coreference Resolution at book scale, a problem studied almost exclusively on short documents. We introduce BookCoref, the first book-scale coreference resource, produced through a semi-automatic pipeline combining entity linking, LLM-based cluster validation, and local coreference expansion. Its silver partition spans over 10.8 million tokens across 50 books, with chains averaging more than 73,000 tokens in pairwise distance; a manually annotated test set provides expert-curated annotations for three complete novels. State-of-the-art systems drop below 47 CoNLL-F1 on full novels (versus approximately 80 on much shorter benchmarks), and training on the silver data raises the best system to 67.0, well short of the 82.2 achieved on independent windows. Equipped with these models, we investigate the challenge of coreference-aware retrieval-augmented generation (RAG) for Narrative QA, where dense retrievers miss passages containing implicit entity references. Two integration strategies reveal a clear asymmetry: index-time augmentation degrades performance by propagating coreference errors globally, whereas query-time filtering yields consistent, if modest, improvements by confining errors to passages already retrieved for a single query. The second pair of contributions addresses evaluation methodology and model capacity. NarrativeQA, the most widely used Narrative QA benchmark, proves unreliable: 22% of its test documents are mismatched or non-narrative, and noisy annotations degrade n-gram-based metrics. We introduce LiteraryQA, a curated benchmark of 138 documents and 3,785 question-answer pairs derived via manual document filtering and LLM-based QA correction, which also serves as the evaluation framework for the RAG experiments above. A meta-evaluation on 7,000 model predictions shows near-zero system-level correlation between n-gram metrics and human preferences, while an LLM-as-a-judge approach augmented with book summaries reaches 0.69 Kendall's Tau. We then apply this evaluation framework when exploring context length adaptation and applications on less-resourced languages: through continual pretraining, we extend a bilingual English-Italian LLM's context window from 4K to 16K tokens using a literary-enriched data mixture, and introduce INDAQA, the first Italian Narrative QA benchmark (365 books, 13,757 question-answer pairs). Continually training our model achieves substantial gains over simple post-training adaptations on both languages. We also find that our method provides a clear cross-lingual transfer effect and robust extrapolation to twice the training length, while metric divergences on Italian further reinforces the LiteraryQA findings. This thesis addresses key challenges of narrative text, from long-distance coreference to evidence scattered across chapters, calling for resources and protocols designed specifically for book-scale inputs. BookCoref lays the groundwork for entity tracking and enables the coreference-aware retrieval experiments; LiteraryQA establishes the evaluation standard shared by both the retrieval and adaptation studies; and INDAQA extends it to Italian, enabling the first cross-lingual study of narrative comprehension. These resources and findings form a concrete foundation for future research in automatic Narrative Understanding.

**Решение:** -4 автоматическое понимание длинных книжных нарративов

---

### 304 · R2064

**Retrieval-Augmented Generation for Industrial Applications: Design and Evaluation of an AI Assistant**

2026 · Open Repository of the University of Porto (University of Porto) · dissertation · en · https://repositorio-aberto.up.pt/bitstream/10216/176085/2/787395.pdf

Industrial machinery manufacturers distribute technical knowledge through dense manuals that operators and engineers must navigate manually to answer operational questions.This process is time-consuming, prone to error, and inaccessible to users without prior familiarity with the documentation.Large language models offer a promising alternative, but their reliance on static parametric knowledge makes them unsuitable for domain-specific technical queries where safety, accuracy and grounding in authoritative sources are critical.This dissertation presents AMOB-RAG, a modular Retrieval-Augmented Generation system designed to answer natural language questions in Portuguese about technical documentation for rotary draw bending machines.The system is structured around two pipelines: an offline ingestion pipeline that preprocesses, chunks, and indexes markdown documentation into a persistent vector store, and an online query pipeline that retrieves, reranks, and assembles context before generating grounded answers.Key design decisions include semantic chunking with configurable breakpoint detection, CrossEncoder reranking with a table penalty heuristic, domain-specific query expansion from a structured axis synonym file, and a similarity threshold gate that prevents low-confidence retrievals from reaching the generation stage.The system is evaluated against a human-verified golden dataset of 20 question-answer pairs in Portuguese, covering five question categories.Evaluation combines automated metrics with an LLM-as-a-judge framework that scores each answer across three qualitative dimensions: faithfulness, answer relevance, and context relevance.A controlled experiment strategy isolates the contribution of each pipeline component.A baseline experiment demonstrates that a standalone large language model fails to answer domain-specific questions reliably, establishing the necessity of the RAG architecture.Subsequent controlled experiments validate the individual contributions of each ingestion and query pipeline component.The results, obtained from this initial case study, confirm that the modular architecture achieves reliable retrieval and grounded answer generation over specialized industrial documentation, with the evaluation framework providing sufficient diagnostic resolution to identify failure modes in specific pipeline components.As the system has not yet been deployed within AMOB's production environment, these findings establish a validated technical foundation ahead of a future field deployment and evaluation with AMOB's operators.

**Решение:** -4 RAG для технических руководств промышленного оборудования

---

### 305 · R2668

**Testing Empathy in Machines: A Comparative Study of Large Language Models and Motivational Interviewing**

2026 · European Psychiatry · abstract, pmc, article · eng · https://doi.org/10.1192/j.eurpsy.2026.12058

Introduction Large language models (LLMs) are increasingly proposed as tools for behavioral healthcare, with the potential to augment or even automate aspects of psychotherapy. Among therapeutic frameworks, motivational interviewing (MI) is especially relevant as it is well-validated for eliciting behavior change and improving adherence. MI’s structured, empathetic style provides a rigorous benchmark for assessing whether LLMs can replicate therapeutic dialogue. While LLMs promise scalability and accessibility, their application in psychotherapy remains high-stakes, raising concerns of safety, fidelity, and ethical deployment. Objectives This study aims to evaluate whether current leading LLMs reproduce the principles of MI, focusing on empathy, change talk, rolling with resistance, and support for autonomy. Methods A standardized MI script addressing ambivalence toward alcohol reduction was applied across five leading LLMs: GPT-4, GPT-3.5, Claude, Gemini, and Llama-2. Outputs were coded against MI core processes (engaging, focusing, evoking, planning), MI principles (empathy, discrepancy, resistance management, non-confrontation, self-efficacy), and common techniques (open questions, reflections, affirmations, eliciting change talk, avoidance of directive advice). Results GPT-4 most consistently embodied MI: it engaged and focused effectively, elicited change talk, and demonstrated empathy through accurate reflections. It avoided confrontation and supported self-efficacy, applying all five principles with notable fidelity. Claude showed similar strengths, especially in empathy and discrepancy development, but was less reliable in rolling with resistance. Gemini balanced empathy with structure, producing clear open questions and affirmations, but defaulted to directive recommendations, limiting adherence to non-confrontation and autonomy support. GPT-3.5 generated open questions but frequently lapsed into advice-giving, undermining MI principles and the planning process. Llama-2 showed the lowest fidelity, often offering prescriptive advice rather than reflections, with minimal engagement in evoking change talk or consolidating commitment. Across models, nuanced techniques such as managing resistance and strengthening commitment were inconsistently applied, with GPT-4 and Claude demonstrating the highest overall fidelity to MI principles and techniques. Conclusions LLMs can reproduce surface features of MI and show promise for scaling access to supportive dialogue. However, consistent therapeutic stance and deeper MI techniques remain beyond current capacity. These findings echo concerns that while LLMs may simulate skills, they do not yet deliver the clinical sensitivity required for psychotherapy. Responsible development should prioritize domain-specific training, interdisciplinary oversight, and hybrid models where clinician supervision ensures therapeutic integrity. Disclosure of Interest None Declared

**Решение:** -2 исследователи оценивают соответствие реплик пяти LLM принципам мотивационного интервьюирования

---

### 306 · R10430

**Context-Aware Pseudo-Label Scoring for Zero-Shot Video Summarization**

2025 · International Conference on Artificial Intelligence and Intelligent Information Processing (AIIIP) · journalarticle, book, conference · https://doi.org/10.1145/3778534.3778559

With the rapid proliferation of video content across social media, surveillance, and education platforms, efficiently summarizing long videos into concise yet semantically faithful surrogates has become increasingly vital. Existing supervised methods achieve strong in-domain accuracy by learning from dense annotations but incur high labeling costs and limited cross-dataset generalization, while unsupervised approaches, though label-free, often miss high-level human semantics and fine-grained narrative cues. Recent zero-shot pipelines leverage large language models (LLMs) for training-free video summarization, yet remain highly sensitive to handcrafted prompts and dataset-specific normalization.To address these limitations, we propose a rubric-guided, pseudo-labeled prompting framework that converts a small subset of human annotations into high-confidence pseudo labels and aggregates them into structured, dataset-adaptive scoring rubrics for interpretable scene evaluation. During inference, first and last segments are scored based solely on their descriptions, whereas intermediate segments incorporate brief contextual summaries of adjacent scenes to assess narrative progression and redundancy. This contextual prompting enables the LLM to balance local salience and global coherence without parameter tuning.Our framework achieves consistent improvements across three benchmarks. On SumMe and TVSum, it reaches F1 scores of 57.58 and 63.05, surpassing the zero-shot baseline PROMPTS TO SUMMARIES (56.73 and 62.21) by +0.85 and +0.84, respectively, while approaching the performance of supervised models. On the query-focused QFVS benchmark, our method attains an average F1 of 53.79, exceeding the baseline (53.42) by +0.37 and demonstrating stable performance across all validation videos. These results confirm that rubric-guided pseudo labeling, combined with contextual prompting, effectively stabilizes LLM-based scoring and establishes a general, interpretable zero-shot paradigm applicable to both generic and query-focused video summarization.Code is available at: https://github.com/wuyuanli60-svg/Context-Aware-Pseudo-Label-Scoring-for-Zero-Shot-Video-Summarization.

**Решение:** -4 контекстная псевдоразметка для суммаризации видео

---

### 307 · R10384

**Who's the Mole? Modeling and Detecting Intention-Hiding Malicious Agents in LLM-Based Multi-Agent Systems**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2507.04724

Multi-agent systems powered by Large Language Models (LLM-MAS) have demonstrated remarkable capabilities in collaborative problem-solving. However, their deployment also introduces new security risks. Existing research on LLM-based agents has primarily examined single-agent scenarios, while the security of multi-agent systems remains largely unexplored. To address this gap, we present a systematic study of intention-hiding threats in LLM-MAS. We design four representative attack paradigms that subtly disrupt task completion while maintaining a high degree of stealth, and evaluate them under centralized, decentralized, and layered communication structures. Experimental results show that these attacks are highly disruptive and can easily evade existing defense mechanisms. To counter these threats, we propose AgentXposed, a psychology-inspired detection framework. AgentXposed draws on the HEXACO personality model, which characterizes agents through psychological trait dimensions, and the Reid interrogation technique, a structured method for eliciting concealed intentions. By combining progressive questionnaire probing with behavior-based inter-agent monitoring, the framework enables the proactive identification of malicious agents before harmful actions are carried out. Extensive experiments across six datasets against both our proposed attacks and two baseline threats demonstrate that AgentXposed effectively detects diverse forms of malicious behavior, achieving strong robustness across multiple communication settings.

**Решение:** -4 обнаружение скрытых вредоносных агентов, кибербезопасность

---

### 308 · R0828

**The Language-Based Assessment Model Library: Open Model Sharing for Independent Validation and Broader Applications**

2026 · Advances in Methods and Practices in Psychological Science · journalarticle, review, article · en · https://doi.org/10.1177/25152459261419036

Language-based assessments (LBAs), quantitative estimates of scientific constructs based on language, have advanced methods in the psychological and social sciences for more than a decade. LBAs based on individuals’ prompted descriptions analyzed with large language models to produce scores of their psychological states and traits have shown strong convergence with the corresponding rating scales ( r &gt; .80) and have often surpassed rating scales in predicting theoretically relevant behaviors (external criteria). Despite their high validity across numerous psychological outcomes and contexts, the broader adoption of LBA models (LBAMs) has been limited. Even when made available alongside research publications, these models often remain inaccessible because of technical complexities, inconsistent documentation, and the absence of a standardized repository. In this tutorial, we introduce a framework targeted to social and psychological scientists for accessible sharing models with others—the Language-Based Assessment Models (L-BAM) Library—and a toolkit for easily using LBAMs via the text package in R. L-BAM covers a wide range of models for assessing mental-health disorders (e.g., depression, anxiety), well-being (e.g., satisfaction with life, harmony in life), implicit motives (need for power, affiliation, and achievement), and more. The L-BAM Library aims to increase the availability and resource efficiency of LBAs of psychological constructs while encouraging replication, independent validation, and the broad application of preexisting LBAMs.

**Решение:** ? туториал/фреймворк L-BAM для языковой психодиагностики; проверить данные согласия в полном тексте

---

### 309 · R11893

**Evaluating the performance of ChatGPT and GPT-4o in coding classroom discourse data: A study of synchronous online mathematics instruction**

2024 · Computers and Education Artificial Intelligence · article · en · https://doi.org/10.1016/j.caeai.2024.100325

High-quality instruction is essential to facilitating student learning, prompting many professional development (PD) programmes for teachers to focus on improving classroom dialogue. However, during PD programmes, analysing discourse data is time-consuming, delaying feedback on teachers' performance and potentially impairing the programmes' effectiveness. We therefore explored the use of ChatGPT (a fine-tuned GPT-3.5 series model) and GPT-4o to automate the coding of classroom discourse data. We equipped these AI tools with a codebook designed for mathematics discourse and academically productive talk. Our dataset consisted of over 400 authentic talk turns in Chinese from synchronous online mathematics lessons. The coding outcomes of ChatGPT and GPT-4o were quantitatively compared against a human standard. Qualitative analysis was conducted to understand their coding decisions. The overall agreement between the human standard, ChatGPT output, and GPT-4o output was moderate (Fleiss's Kappa = 0.46) when classifying talk turns into major categories. Pairwise comparisons indicated that GPT-4o (Cohen's Kappa = 0.69) had better performance than ChatGPT (Cohen's Kappa = 0.33). However, at the code level, the performance of both AI tools was unsatisfactory. Based on the identified competences and weaknesses, we propose a two-stage approach to classroom discourse analysis. Specifically, GPT-4o can be employed for the initial category-level analysis, following which teacher educators can conduct a more detailed code-level analysis and refine the coding outcomes. This approach can facilitate timely provision of analytical resources for teachers to reflect on their teaching practices. • This study evaluated the performance of ChatGPT and GPT-4o in classroom discourse analysis. • The coding outcomes by GPT-4o aligned better with the human standard compared to those by ChatGPT. • The AI tools showed weaknesses, such as lacking pedagogical content knowledge and misinterpreting code definitions. • GPT-4o's coding was reliable at the category level but not at the code level. • A two-stage approach to AI-supported classroom discourse analysis is proposed.

**Решение:** -4 кодирование структуры педагогического диалога на уроках математики, нет психологического конструкта

---

### 310 · R1671

**Detecting negative language transfer in L2 using natural language processing**

2026 · Athens University of Economics & Business · other/text, other · https://doi.org/10.26219/heal.aueb.10065

Negative Language Transfer (NLT) is the misuse of a native language pattern or rule that leads to the production of an error, or an inappropriate form in the target language. There are various aspects of NLT that have been explored in NLP, however, many aspects of the phenomenon still remain unexplored; the extent of Inter Annotator Agreement (IAA) in detecting NLT, and the performance of Large Language Models (LLMs) as annotators alongside humans. The present study deals with these gaps. To explore them, three annotation rounds were conducted where expert and non-expert annotators annotated 300 authentic learner sentences produced by Greek learners of English. An adjudication round was also conducted, in order to gain qualitative insight into annotator disagreements. The key findings include that human agreement is low, and varies approximately between κ = 0.30 and κ = 0.40. The LLM achieves a similar agreement score against all annotators averaged (κ = 0.27), agreeing more with non-expert annotators, and achieving similar κ scores (0.28). These results have notable implications for the creation and development of foreign language learning tools, as well as NLP systems, as LLMs are not on an expert level yet. This study concludes that NLT is a complex and subjective task. The thesis concludes that it should be treated as a multi-label, ordinal problem to better reflect its subjectivity instead of a binary one. Η αρνητική γλωσσική παρεμβολή (Negative Language Transfer, NLT) είναι η λανθασμένη χρήση ενός μοτίβου ή κανόνα της μητρικής γλώσσας, που οδηγεί στην παραγωγή ενός λάθους ή μιας αστοχίας στη ξένη γλώσσα. Υπάρχουν διάφορες πτυχές της αρνητικής γλωσσικής παρεμβολής που έχουν μελετηθεί στην Επεξεργασία Φυσικής Γλώσσας (Natural Language Processing, NLP), όμως, πολλές πτυχές του φαινομένου παραμένουν ακόμα ανεξερεύνητες: αυτές είναι ο βαθμός συμφωνίας μεταξύ επισημειωτών (Inter-Annotator Agreement, IAA), καθώς και η ικανότητα των μεγάλων γλωσσικών μοντέλων (Large Language Models, LLMs) να την εντοπίσουν. Η παρούσα μελέτη ασχολείται με αυτά τα κενά. Για την μελέτη τους, πραγματοποιήθηκαν τρεις γύροι επισημείωσης, όπου ειδικοί και μη-ειδικοί επισημειωτές επισημείωσαν 300 προτάσεις από εκθέσεις Ελλήνων μαθητών της Αγγλικής ως ξένη γλώσσα. Πραγματοποιήθηκε επίσης μια συνάντηση για συζήτηση των επισημειώσεων, με στόχο τη ποιοτική ανάλυση των διαφωνιών μεταξύ επισημειωτών. Τα βασικά ευρήματα δείχνουν ότι η συμφωνία μεταξύ επισημειωτών είναι χαμηλή, και κυμαίνεται από περίπου κ =0.30 μέχρι κ = 0.40. To LLM πετυχαίνει ένα παρόμοιο κ score (κ = 0.27) έναντι του μέσου όρου των επισημειωτών, και φαίνεται να συμφωνεί περισσότερο με τους μη-ειδικούς επισημειωτές, παρουσιάζοντας παρόμοια κ scores (0.28). Τα αποτελέσματα αυτά είναι σημαντικά για τη δημιουργία και την ανάπτυξη συστημάτων εκμάθησης ξένων γλωσσών και συστημάτων NLP, καθώς τα LLMs δεν βρίσκονται στο επίπεδο των ειδικών επισημειωτών ακόμη. Η διατριβή καταλήγει στο ότι η αρνητική γλωσσική παρεμβολή θα πρέπει να αντιμετωπίζεται ως διαβαθμισμένο πρόβλημα πολλαπλών επιλογών, αντί για δυαδικό.

**Решение:** -4 лингвистический анализ отрицательного языкового переноса во втором языке

---

### 311 · R5289

**Accuracy and Safety of Language Model-Generated Breastfeeding Counseling Responses: An Expert-Based Comparative Evaluation of ChatGPT-3.5, ChatGPT-4, and BreastfeedGPT.**

2026 · Breastfeeding medicine : the official journal of the Academy of Breastfeeding Medicine · comparative study, journal article, med · eng · https://doi.org/10.1177/15568253261481438

Aim: This study aims to compare the responses generated by ChatGPT-3.5, ChatGPT-4, and BreastfeedGPT, a customized domain-specific GPT, to frequently asked questions related to breastfeeding counseling. Design and Methods: Ten breastfeeding-related questions were selected based on international guidelines and expert validation. Each model generated responses to the same questions, which were anonymized and evaluated by eight health professionals with expertise in breastfeeding counseling using structured Likert scales. Evaluation dimensions included (1) scientific accuracy and scope, (2) tone, language, and motivation, and (3) reliability via mDISCERN scoring. Friedman and Wilcoxon signed-rank tests with Bonferroni correction were used to determine statistical significance. Results: BreastfeedGPT model outperformed ChatGPT-3.5 and ChatGPT-4 across all domains. It received the highest mean scores in scientific accuracy (3.72 ± 0.23) and motivational tone (3.78 ± 0.42), with statistically significant differences (p < 0.001). Although the mDISCERN scores also favored the custom model, pairwise differences were not statistically significant after correction. GPT-4 performed better than GPT-3.5, but worse than BreastfeedGPT. Conclusion: BreastfeedGPT may offer advantages over general-purpose AI tools in providing breastfeeding-related information. However, because human expert responses were not evaluated in parallel, its role as a complementary resource should be interpreted cautiously and confirmed in future direct comparisons. Such tools should support, rather than replace, professional breastfeeding care.

**Решение:** -4 оценка точности ответов языковых моделей по грудному вскармливанию

---

### 312 · R2151

**A hybrid quantitative–qualitative RAG approach for territorial well-being decision support**

2026 · Machine Learning with Applications · article · en · https://doi.org/10.1016/j.mlwa.2026.101005

Territorial well-being analysis requires integrating two complementary families of information: objective indicators (equipment, composite quality-of-life scores) that characterize structural conditions, and subjective perceptions (citizen survey verbatims, interviews) that reflect lived experience. Classical retrieval-augmented generation (RAG) handles such mixed-source queries poorly: semantic similarity search fragments information and provides no structural constraint on the consistency between the data types a query calls for and those actually available. We propose a hybrid RAG architecture built on three principles: (i) explicit decomposition of the user query into independently processed sub-questions; (ii) multi-level synthetic representations precomputed along business-driven analytical views, adapting the RAPTOR approach to survey metadata rather than automatic clustering; and (iii) a typed decomposition mechanism enforcing consistency between the nature of the query and the sub-questions generated, constraining the formulation of sub-questions that have no documentary support. We evaluate the architecture on a benchmark of 109 manually designed questions spanning seven usage categories, combining categorical retrieval metrics with a multi-dimensional LLM-as-judge validated against human annotations, an ablation study isolating each principle, and a comparison with an external decomposition baseline (Self-Ask). Results show that the architecture retrieves relevant sources far more exhaustively than vanilla RAG (Recall 0.97 against 0.68), that both the typing rule and the multi-level representations contribute significantly to answer quality, and that it outperforms Self-Ask. On the benchmark as a whole, answer quality is comparable to vanilla RAG, the advantage being concentrated on questions requiring multi-aspect reasoning—which suggests that architectural choices should be informed by the intended usage profile.

**Решение:** -4 гибридный RAG для анализа территориального благополучия, экономика

---

### 313 · R12713

**Efficacy of a Group Psychoeducation Treatment in Binge Eating Disorder: An Open-Label Study.**

2022 · Frontiers in psychiatry · journal article, journalarticle, article · eng · https://doi.org/10.3389/fpsyt.2022.822282

Aims To evaluate the effectiveness of a multidisciplinary group psychoeducation treatment (GPT) in patients with Binge Eating Disorder (BED). Methods We designed an open-label efficacy study that included a population of 45 patients diagnosed with BED. A measure of eating attitudes and associated psychological constructs was obtained through the use of the self-report instruments Eating Disorder Inventory (EDI-3), Binge Eating Scale (BES) and Body Uneasiness Test (BUT). The Symptom Checklist-90 (SCL-90) was also administered to assess general psychopathology. All participants participated in 12 weekly group psychoeducational treatment meetings, 8 of which were conducted by mental health professionals, and a second module of 4 meetings, oriented on health and nutrition education topics, conducted by a dietician. Results At the end of treatment, patients showed significant improvements in body mass index (BMI) and binge eating. Paired t-tests showed significant differences at p-value < 0.05 in all eating disorder risk scales and for most of the general psychological scales related to eating disorders. In addition, patients experienced an improvement in their perception of overall body image, a decrease in concerns about physical appearance and less body image avoidance. Finally, results showed that psychoeducation treatment was associated with significant improvements in interpersonal sensitivity. Conclusions The results of this study may indicate that significant short-term improvements can be achieved through a psychoeducation group for BED patients. Although limited by the lack of a control condition, this study adds to a growing body of evidence with promising results, setting the stage for further case-control studies of BED treatment.

**Решение:** -5 клиническое испытание групповой психообразовательной программы (GPT), не про языковые модели

---

### 314 · R8408

**Evaluating the Effectiveness of Artificial Intelligence versus Clinical Pharmacist Assessment in Identifying Drug-related Problems in Adult Intensive Care Unit Patients**

2025 · Saudi Critical Care Journal · journalarticle, review, article · en · https://doi.org/10.4103/sccj.sccj_5_26

Abstract Background: Drug-related problems (DRPs) are a major safety concern in intensive care units (ICUs), affecting 60%–74% of patients. Clinical pharmacists reduce DRPs but face workforce constraints. Artificial intelligence (AI) offers scalable medication safety surveillance, but direct comparisons with expert assessment in ICU settings are limited. Materials and Methods: This retrospective comparative feasibility study evaluated a multi-modal AI system (GPT-4.1-mini, Gemini 2.5 Pro, Claude Sonnet-4) for DRP detection in 52 randomly selected adult ICU patient records (98 documented pharmacist interventions). AI outputs were independently reviewed by two senior experts using a validated 5-domain rubric (0–10 points). The primary outcome was concordance with expert review. Secondary outcomes included inter-rater reliability (Cohen’s kappa) and component-wise performance. Results: The AI system achieved a mean total score of 8.70 ± 1.33 (95% confidence interval [CI]: 8.44–8.97), significantly exceeding the benchmark of 8.0 ( t = 5.228, df = 97, P < 0.001). Acceptable performance (≥7/10) occurred in 95.9% ( n = 94) of evaluations, with 62.2% ( n = 61) achieving excellence (≥9/10). DRP detection scored highest (1.92 ± 0.31/2.0; 92.9% perfect scores), while recommendation planning scored lowest (1.53 ± 0.52/2.0; 54.1% perfect scores). Inter-rater agreement was moderate (κ =0.415; 95% CI: 0.287–0.543). Conclusion: This multi-modal AI system demonstrates high feasibility for supervised ICU DRP surveillance, excelling in pattern recognition but showing limitations in therapeutic planning. A human-in-the-loop model is essential. Prospective multi-center validation is required.

**Решение:** -4 оценка медикаментозных проблем в отделениях интенсивной терапии, фармация

---

### 315 · R9795

**Security Challenges and Mitigation Strategies in Generative AI Systems**

2025 · International Journal of Scientific Research in Computer Science Engineering and Information Technology · journalarticle, journalarticle/, article · en · https://doi.org/10.32628/cseit25112377

This article examines the critical security challenges and mitigation strategies in generative AI systems. The article explores how these systems have transformed various sectors, particularly in financial markets and critical infrastructure, while introducing significant security concerns. The article analyzes various types of adversarial attacks, including input perturbation and backdoor attacks, and their impact on AI model performance. Additionally, it investigates model stealing threats and data privacy concerns in AI deployments. The article presents comprehensive mitigation strategies, including advanced defense mechanisms, enhanced protection frameworks, and secure access control implementations. The article findings demonstrate the effectiveness of integrated security approaches in protecting AI systems while maintaining operational efficiency. This article contributes to the growing body of knowledge on AI security by providing evidence-based strategies for protecting generative AI systems across different application domains.

**Решение:** -4 анализ проблем безопасности и стратегий защиты в генеративном ИИ

---

### 316 · R11683

**Promptable foundation model for automatic whole body RECIST measurement.**

2024 · Journal of Clinical Oncology · journalarticle, conference-abstract · en · https://doi.org/10.1200/jco.2024.42.16_suppl.e13643

e13643 Background: RECIST 1.1 is the gold standard for tumor evaluation in clinical trials and patient care. However, it faces challenges due to the subjective selection and measurement of lesions, notably because of inter-observer variability in the 20-30% range (1), which can potentially result in inaccuracies in therapeutic response classification (2). The main objective of this study is to assess the added value of a radiological foundation model to assist the radiologist to measure RECIST across different lesion topographies, using visual prompting. Methods: We use a promptable segmentation algorithm, based on a visual foundation model, pre-trained on various CT-scans and then trained on a subset of the Medical Segmentation Decathlon (MSD) dataset, covering 538 patients with pancreas, liver, colon and lung lesions. It outputs a 3D segmentation mask of the lesion, using a visual prompt, i.e. a 3D bounding box (BBox) as input. We then measure the capacity of the model to measure RECIST on the MSD validation set and on the KiTS validation set (99 samples), which features a new lesion type (kidney). To simulate inter-reader variability of up to 23%, we provide as inputs BBoxes centered on the lesions but with a varying error (15% variability: +10 pixels, 23% variability: +15 pixels). Results: The model is able to correct variability in BBox input: with all BBox error ranges, it beats the input variability (15% and 23% thresholds in each column) across many organ types, except in the pancreas when using large error BBoxes. Moreover, the model is able to generalize to new lesion types not seen during training, on an external dataset (KiTS - Kidney). Conclusions: Unlike existing supervised machine learning models dedicated to lesion detections in specific organs, our approach is organ and lesion agnostic and offers a more reliable, precise tumor assessment. This is a first step before allowing the longitudinal evaluation of tumors while safeguarding the clinical intuition necessary for selecting the right target lesions. Moreover, we believe that these methods will be crucial in advancing beyond RECIST 1.1, facilitating the identification of new prognostic biomarkers and proxies for tumor burden derived from previously underexplored radiomics features, ultimately refining the efficacy of clinical trial assessments and elevating the standard of patient care. 1. Yoon, S et al. 2015. 2. Kuhl et al. 2018. [Table: see text]

**Решение:** -4 автоматическая оценка опухолей по критериям RECIST 1.1, соматическая онкология

---

### 317 · R10937

**Comparative Analysis of Pattern Tasks Experiences Between Fifth Grade Secondary School Students and ChatGPT Artificial Intelligence Tool**

2024 · INTERNATIONAL JOURNAL OF HUMANITIES AND ART RESEARCH · journal/ · https://doi.org/10.5281/zenodo.14270244

The technology that rapidly changes and advances the world necessitates interaction in all areas of life. Considering the role of technology in education today, the depth of this interaction offers various education opportunities. One of these opportunities is the technological tools used in educational settings. Technological tools, which add different dimensions to education, are quite significant. In this context, the use of artificial intelligence tools in educational environments in recent years is noteworthy. AI chatbots are particularly prevalent in education. Students and teachers can interact with these chatbots in written or spoken form. ChatGPT, developed by OpenAI, is one of the most frequently used chatbots recently. It can generate texts similar to those constructed by humans, understand users' language, answer their questions, and perform certain tasks. In addition to being a large language model, ChatGPT is also used in various disciplines, including mathematics. Given the importance of patterns in algebra teaching, it is inevitable that children encounter pattern tasks at an early age. It is important to reveal the similarities and differences between the answers provided by students and those generated by the ChatGPT AI tool to pattern tasks. Accordingly, this study examines the differences between the answers given to pattern tasks by fifth-grade students and the ChatGPT AI tool. A qualitative approach using a case study design was employed in line with this aim. The study was limited to fifth-grade students and the ChatGPT AI tool, with their responses to pattern tasks examined in detail. Purposeful sampling was used to select eight fifth-grade students and the ChatGPT AI tool as the units of analysis. Criterion sampling, a type of purposeful sampling, was utilized, with voluntariness and being in the fifth grade considered as criteria for participant selection. The participants comprised 100 fifth-grade students studying at a middle school in Istanbul and the ChatGPT AI tool. Pattern worksheets and screenshots from the ChatGPT AI tool were used as data collection tools. The pattern worksheet consisted of four number pattern tasks with constant increasing and decreasing patterns and 16 sub-problems. The researcher developed the pattern tasks using achievements from the mathematics curriculum and literature to ensure content validity. The pattern worksheet was later administered to students participating in clinical interviews with additional questions for in-depth examination. Ethical committee approval and necessary permissions from the provincial and national education directorates were obtained before data collection. Clinical interviews were used as the data collection method. Initially, the pattern worksheets were administered to the study group, and students were provided with the necessary information about the study before completing the worksheets. Students were given 80 minutes to answer the pattern tasks. Based on their responses to the pattern worksheet, students were categorized. To obtain rich data for comparison with the ChatGPT AI tool, clinical interviews were conducted with students considered to represent each category best. Data analysis was performed using content analysis. According to the study findings, students most frequently used random arithmetic operations without continuing the pattern to reach the close terms of the pattern tasks. The ChatGPT AI tool, however, utilized operations without continuing the pattern or writing formulas to reach the close terms of the pattern tasks. For the middle terms of the pattern tasks, students again predominantly used random arithmetic operations without continuing the pattern, whereas the ChatGPT AI tool used operations without continuing the pattern, writing formulas, or using formulas. Students mostly relied on random arithmetic operations to reach the distant terms of the pattern tasks. At the same time, the ChatGPT AI tool used operations without continuing the pattern, writing formulas, or using formulas. In inverse problems of the pattern tasks, students primarily used random arithmetic operations, while the ChatGPT AI tool employed formulas without continuing the pattern. Students faced difficulties and left blank responses, particularly regarding the pattern task's distant terms and inverse problems. Additionally, the constantly decreasing pattern task was the most challenging and frequently left-blank pattern task for students. Based on the responses provided by the ChatGPT artificial intelligence tool, students can consult this chatbot with any problems they encounter regarding pattern tasks. Although this robot often arrives at the correct answer, it can occasionally provide incorrect responses. Therefore, students need to use the ChatGPT artificial intelligence tool under the supervision of a teacher during the instructional process. Additionally, ChatGPT can present errors related to computer programming languages and Turkish character usage in its solutions. These are some of ChatGPT's limitations. This study is limited to fifth-grade middle school students and the topic of patterns. In future studies, similar research can be repeated with different grade levels or subject areas to determine how ChatGPT can be utilized in students' instructional processes.

**Решение:** -4 анализ математических паттернов в школьном образовании

---

### 318 · R1273

**Development and validation of AI-based chatbot for self-management in liver transplant recipients.**

2026 · Applied nursing research : ANR · journal article, validation study, journalarticle · eng · https://doi.org/10.1016/j.apnr.2026.152136

Aims Liver transplant recipients require complex self-management after transplantation. This study aimed to validate an artificial intelligence (AI)-based chatbot designed to support self-management. Methods A mixed-methods study was conducted at a medical center in Northern Taiwan (October 2022-December 2024). The chatbot was developed through four stages: creation of a self-management Q&A database, system development, validation, and usability testing. Interview findings from patients and healthcare professionals informed the database. The chatbot was deployed via LINE@ using a hybrid framework that retrieves validated responses from a predefined database and uses ChatGPT-4o-mini only for unmatched queries. Content validity index (CVI), intraclass correlation coefficient (ICC), Cohen's kappa, satisfaction, usability, and intention to use were evaluated. Results A total of 112 questions were classified into four domains and 21 subcategories. Two rounds of expert validation demonstrated acceptable-to-excellent agreement. The CVI improved from 0.79 to 0.88, ICC increased from 0.957 to 0.976, and Cohen's kappa reached 0.88. The satisfaction score was 4.71 (standard deviation [SD] = 0.39) on a 5-point Likert scale. The usability and intention-to-use scores were 6.04 (SD = 0.98) and 6.12 (SD = 1.02), respectively, on a 7-point scale. Conclusions The AI-based chatbot demonstrated strong validity and usability, supporting its readiness for larger-scale clinical evaluation. This hybrid approach shows promise for improving post-discharge self-management and personalized support for liver transplant recipients.

**Решение:** -4 валидация чат-бота для пациентов после трансплантации печени

---

### 319 · R11917

**Reflections on inductive thematic saturation as a potential metric for measuring the validity of an inductive thematic analysis with LLMs**

2024 · Quality & Quantity · journalarticle, preprint/article, article · en · https://doi.org/10.1007/s11135-024-01950-6

Abstract This paper presents a set of reflections on saturation and the use of Large Language Models (LLMs) for performing Thematic Analysis (TA). The paper suggests that initial thematic saturation (ITS) could be used as a metric to assess part of the transactional validity of TA with LLM, focusing on the initial coding. The paper presents the initial coding of two datasets of different sizes, and it reflects on how the LLM reaches some form of analytical saturation during the coding. The procedure proposed in this work leads to the creation of two codebooks, one comprising the total cumulative initial codes and the other the total unique codes. The paper proposes a metric to synthetically measure ITS using a simple mathematical calculation employing the ratio between slopes of the unique and total codes. The paper contributes to the initial body of work exploring how to perform qualitative analysis with LLMs.

**Решение:** -1 теоретические размышления о тематическом насыщении в качественном анализе с LLM

---

### 320 · R7591

**Toward Proactive Dialogic AI Agents**

2025 · Open Research (University of Surrey) · conference-paper · en · https://bia.unibz.it/esploro/outputs/conferenceProceeding/Toward-Proactive-Dialogic-AI-Agents/991007109554701241

This paper introduces an ongoing research on the development of a proactive dialogic AI agent, focusing on enhancing an LLM's pragmatic competence in goal-oriented dialogues. We investigate proactivity as a collaborative behaviour that enables to provide relevant and useful information that has not been explicitly requested, thereby improving interaction efficiency and dialogue naturalness. Our approach is grounded in a corpus-based analysis of proactive behaviours in human-human dialogues across five goal-oriented dialogue corpora, leading to the creation of the D-Pro Corpus, a manually annotated resource for studying proactivity. Its analysis provides information on qualitative and distributional features of proactivity in human dialogues, as well as clues on recurrent linguistics structures that co-occur with the display of proactive behaviours. We then leverage the D-Pro Corpus to evaluate the performance of a GPT-4o model in proactivity annotation, addressing the task by providing a 4-turns context size and by targeting the last utterance for proactivity prediction. By experimenting with parameter setting and prompt configurations, we assess the model's performance across multiple dialogue corpora, obtaining encouraging results toward human-like performance, particularly with the NESPOLE! corpus. We propose to advance our research by exploring the potential of open-source models for cost-effective, large-scale automatic annotation of unlabelled dialogic data. As a final step we plan to use the large-scale annotated corpus to instruction-tune an open model, expanding its pragmatic competence for the development of more proactive and contextually aware dialogic AI system and more natural human-machine conversation.

**Решение:** -6 разработка проактивного диалогового агента

---

### 321 · R5027

**Using the Novel Translation Validity Index to Evaluate GenAI Translations of the Patient Health Questionnaire-9 Into Nine Languages.**

2026 · Journal of nursing measurement · journal article, med, journalarticle · eng · https://doi.org/10.1891/jnm-2025-0196

Background and Purpose: Depressive symptoms affect 280 million people worldwide. Although generative artificial intelligence (GenAI) tools are increasingly used in health care translation, their translation performance across languages remains unclear. To our knowledge, no structured tool exists for evaluating the quality of language translation. This study aimed to create a translation validity index (TVI) and examine the Patient Health Questionnaire-9's translation quality produced by three GenAI platforms across nine languages using TVI. Methods: Two bilingual evaluators per language ( N = 18) assessed translations by chat generative pretrained transformer (ChatGPT), Copilot, and Google Translate using TVI criteria of cultural appropriateness, grammar, and semantic clarity. Scores ≥3 indicated acceptable quality. Results: ChatGPT and Copilot achieved higher TVI scores (3.11-3.66) in high- and medium-resource languages, while Google Translate met acceptability for Ewe (3.73). Conclusions: TVI is novel and is potentially useful for evaluating forward and backward language translation quality. Human expert input remains essential for accurate mental health measure development.

**Решение:** -4 оценка качества машинного перевода опросника депрессии PHQ-9 на девять языков

---

### 322 · R5046

**PersonaManifold: Revealing and Exploiting Curved Geometry in LLM Persona Representations**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.34571

Controlling persona in large language models (LLMs) at inference time is important for role-playing, personalized dialogue, and social simulation. Recent methods extract persona vectors from the model's activation space and apply Euclidean operations---addition, scaling, and linear interpolation---under the linear representation hypothesis. However, these methods themselves report systematic failures: non-orthogonal trait dimensions, asymmetric ceiling and resistance effects, and significant deviations in multi-trait composition, suggesting that the linear isotropic assumption does not hold. We propose PersonaManifold, a framework that models persona representations as points on a curved, low-dimensional Riemannian submanifold in activation space. We estimate the manifold's intrinsic geometry---local metric tensors, geodesic distances, and Ollivier-Ricci curvature---and introduce geodesic steering, which interpolates between personas along manifold geodesics rather than Euclidean straight lines. We also propose the Behavioral Similarity Triplet (BST) benchmark, which automatically generates situational questions grounded in six established psychological constructs and defines persona similarity through behavioral responses rather than self-report questionnaires. Experiments on three open-source LLMs show that persona activations form a manifold with heterogeneous curvature, geodesic distance predicts behavioral similarity more accurately than Euclidean alternatives with independent contributions from anisotropy and curvature, and geodesic steering produces more coherent intermediate personas on both our BST benchmark and external evaluations, with the advantage concentrated in high-deviation regions where the manifold deviates most from flatness. Accepted to NeurIPS 2026

**Решение:** -4 геометрическое управление персоной в LLM, теория машинного обучения

---

### 323 · R3829

**Validation of Artificial Intelligence Models for the Search, Selection of Articles, and Data Extraction in a Systematic Review and Meta-Analysis on Social Media and Video Games in Child and Adolescent Populations**

2026 · European Psychiatry · review · en · https://doi.org/10.1192/j.eurpsy.2026.10963

Introduction Addiction to social media and video games in children and adolescents is associated with negative mental health outcomes, such as depression, anxiety, ADHD, social isolation, and suicidal risk. Objectives This research project has two main aims. First, to develop an artificial intelligence (AI)-based tool, grounded in language models, to automate key stages of a systematic review and meta-analysis (search, article selection, and data extraction). Second, to conduct a systematic review and meta-analysis on the prevalence of use, the impact on mental health, and the effectiveness of interventions for social media and video game addiction in child and adolescent populations. The analysis will be carried out through two approaches: the conventional procedure and the AI-based tool, enabling methodological comparison and assessment of the potential of artificial intelligence in the synthesis of scientific evidence. Methods Study Selection Traditional: Two researchers will screen articles in three phases: (a) titles and abstracts according to inclusion criteria; (b) full-text review with assessment of mental health outcomes and sufficient data; (c) exclusion of overlapping studies. AI-based: A large language model (LLM) will process data in Excel (phase 1) and full texts in Markdown format (phase 2), generating outputs in JSON. The model will detect overlapping studies for exclusion (phase 3). Data Extraction Traditional: Two researchers will extract data on publication characteristics, demographics, type of addiction, comorbidities, interventions, and outcomes. AI-based: The LLM will analyze PDFs converted to Markdown, extracting the same variables into JSON format. A three-level meta-analysis will be conducted following Cochrane guidelines, using literature from PubMed, Scopus, MEDLINE, and the Cochrane Library, with direct comparison between both methods. Results The AI-based tool is expected to automate the processes of search, selection, and data extraction for systematic reviews, reducing the required time and improving methodological efficiency. Furthermore, the systematic review and meta-analysis are anticipated to reveal significant associations between problematic use of social media and video games and various mental health indicators in children and adolescents, such as symptoms of anxiety, depression, ADHD, and suicidal behaviors. The comparison between the conventional approach and the AI-assisted approach will allow for the evaluation of the potential of these technologies in the synthesis of scientific evidence and their future applicability in clinical and academic settings. Conclusions This study is pioneering in applying generative AI to systematic reviews. It also addresses an urgent child and adolescent mental health issue related to behavioral addictions. Disclosure of Interest None Declared

**Решение:** -6 автоматизация поиска и экстракции данных для систематического обзора по игровой зависимости

---

### 324 · R10073

**Automated question type coding of forensic interviews and trial testimony in child sexual abuse cases.**

2025 · Law and human behavior · journal article, journalarticle, research-article · eng · https://doi.org/10.1037/lhb0000590

Objective Question-type classification is widely used as a measure of interview quality. However, question-type coding is a time-consuming process when performed by manual coders. Reliable automated question-type coding approaches would facilitate the assessment of the quality of forensic interviews and court testimony involving victims of child abuse. Hypotheses We expected that the reliability achieved by the automated model would be comparable to manual coders. Method We examined whether a large language model (Robustly Optimized Bidirectional Encoder Representations from Transformers Approach) trained on questions ( N = 351,920) asked in forensic interviews ( n = 1,435) and trial testimony ( n = 416) involving 3- to 17-year-old alleged victims of child sexual abuse could distinguish among (a) invitations, (b) wh-questions, (c) option-posing questions, and (d) nonquestions. Results The model achieved high reliability (95% agreement; κ = .93). To determine whether disagreements were due to machine or manual errors, we recoded inconsistencies between the machine and manual codes. Manual coders erred more often than the machine, particularly by overlooking invitations and nonquestions. Correcting errors in the manual codes further increased the model's reliability (98% agreement; κ = .97). Conclusions Automated question-type coding can provide a time-efficient and highly accurate alternative to manual coding. We have made the trained model publicly available for use by researchers and practitioners. (PsycInfo Database Record (c) 2025 APA, all rights reserved).

**Решение:** -5 классификация типов вопросов в судебных интервью с помощью RoBERTa, нет генеративных LLM

---

### 325 · R0618

**Perceived educational value, ethical risk, and support for responsible AI governance in higher education: an embedded mixed-methods study**

2026 · Frontiers in Education · journalarticle, review, article · en · https://doi.org/10.3389/feduc.2026.1926201

Introduction Generative Artificial Intelligence (GenAI) is becoming increasingly embedded in higher education assessment, yet the perceptual factors that motivate stakeholder support for its institutional governance remain underexamined. This study investigated the extent to which Perceived Educational Value (PEV) and AI Ethical Risk Perception (AERP) are associated with Responsible AI Governance Support (RAGS) among higher education stakeholders. Methods An embedded mixed-methods survey design was employed. Quantitative Likert-scale data and qualitative open-ended responses were collected concurrently through one structured questionnaire; full-sample quantitative analyses were conducted first, followed by thematic analysis of the open-ended responses to contextualize and deepen interpretation of the quantitative findings. A structured questionnaire was administered to 192 participants (125 students and 67 instructors) recruited from public and private higher education institutions in the United Arab Emirates, with N = 192 yielding statistical power exceeding.99 for the structural model. Qualitative open-ended responses from 179 participants were subsequently analyzed using a codebook-based thematic analysis. Quantitative data were analyzed using Partial Least Squares Structural Equation Modeling (PLS-SEM). Results Participants reported above-midpoint levels of PEV, AERP, and RAGS. The structural model explained 59.1% of the variance in RAGS. Both PEV [ β = .255, p < .001, 95% bias-corrected CI (.117,.377)] and AERP [ β = .627, p < .001, 95% bias-corrected CI (.485,.748)] were positively associated with governance support, with AERP showing the larger association. AERP did not significantly moderate the PEV–RAGS relationship [ β = −.030, p = .370, 95% bias-corrected CI (−.098,.037)]. MICOM established full measurement invariance for PEV and AERP but not compositional invariance for RAGS; therefore, structural student–instructor comparisons involving RAGS were not interpreted. Thematic analysis identified responsible conditional integration as the central interpretive frame, with learning enhancement, governance expectations, academic integrity, over-reliance, and critical-thinking concerns among the salient themes. Discussion These findings provide preliminary empirical support for a model in which perceived educational value and ethical risk perception are each associated with governance endorsement. The stronger association between ethical risk perception and governance support suggests that transparent attention to ethical risks may be relevant to institutional governance communication, a possibility that requires intervention-based research. Practical implications include risk-aware AI literacy programs, transparent and contestable governance policies, stakeholder engagement, and human-in-the-loop oversight mechanisms in AI-mediated assessment.

**Решение:** -4 опрос о ценности и этических рисках генеративного ИИ в высшем образовании

---

### 326 · R5614

**From Emotion Representations to Governed Affective States: A Construct-Validity Framework, Comparative Analysis, and Reproducible Experimental Protocol for Artificial Agents**

2026 · Zenodo (CERN European Organization for Nuclear Research) · report/, report · en · https://doi.org/10.5281/zenodo.21792369

Large language models can encode emotion concepts, and these representations can causally influence their outputs. Work by Sofroniew et al. on Claude Sonnet 4.5 notably shows that vectors associated with concepts such as calmness or desperation can alter preferences and certain alignment-relevant behaviors. The authors describe these mechanisms as “functional emotions,” while explicitly stating that they do not demonstrate subjective experience. They also observe that these representations are primarily local: they track the operative emotional content relevant to the current computation rather than a stable state maintained over time. This report proposes a finer-grained framework by distinguishing four levels: affective representation, local causal affective modulation, persistent functional affective state, and governed functional affective state. The final level requires not only behavioral influence, but also persistence independent of emotional vocabulary, cross-task influence, history dependence, regulation, reversibility, and traceability. Eight primary criteria and two transversal validity criteria are formalized so that evaluation can fail, be replicated, and be applied across different architectures. AIZYBRAIN refers to the foundational research program and its historical body of work published since 2025. AIZYBRAIN NANO refers to a distinct, compact, and local implementation informed by that program, but not interchangeable with it. AIZYBRAIN NANO v8.0 RC1 is selected as the experimental platform because its architecture separates a linguistic Brain from a persistent, instrumented, and governed Mind. Its technical documentation describes persisted objects, continuity mechanisms, authorization policies, autobiographical memory, traces, interventions, and an ablation harness. These properties make it a relevant candidate for testing Levels 3 and 4, without validating them by definition. The central contribution is methodological: a causally active emotion representation may be functional without constituting a persistent state. Conversely, a persistent state does not become governed through storage alone, it must be regulated, reversible, auditable, and causally connected to behavior. The framework therefore aims to reduce two symmetrical errors: anthropomorphism, which too quickly turns an activation into a claim of experienced emotion, and reductionism, which refuses any functional qualification for internal dynamics that are nevertheless measurable. This version 1.2 constitutes an autonomous methodological framework and a preregistered protocol. It reports no new confirmatory results. A post-campaign version will incorporate positive, null, or negative findings, any deviations from the protocol, and observed limitations, without retroactively modifying the hypotheses, experimental conditions, or primary thresholds defined here.

**Решение:** -4 исследование внутренних репрезентаций эмоций в архитектуре LLM

---

### 327 · R6984

**Artificial Intelligence in Crisis Counseling: Opportunities, Risks, and Ethical Challenges of Social and Psychological Practice**

2026 · European Journal of Sustainable Development · journalarticle, review, article · https://doi.org/10.14207/ejsd.2026.v15n3p519

The modern development of artificial intelligence, in particular large language models and chatbots, opens up new opportunities for crisis counseling, but at the same time generates significant clinical and ethical risks. The article is aimed at a systematic analysis of the opportunities, risks and ethical challenges of using artificial intelligence in crisis counseling in the context of social and psychological practice. A systematic scoping review of the literature was carried out according to the recommendations of the Preferred Reporting Items for Systematic Reviews and Meta-Analyses Extension for Scoping Reviews. A structured search in the Scopus database for the period 2020–2026 allowed the identification of 556 documents, from which the most relevant sources were selected for high-quality thematic synthesis and bibliometric analysis using VOSviewer. The results demonstrate the significant potential of artificial intelligence in increasing the availability of care, early detection of suicidal risk, personalized interventions, and hybrid “artificial intelligence + specialist” models. At the same time, serious risks have been identified: inadequate responses in suicidal crises, anthropomorphization, emotional dependence (especially among adolescents), hallucinations and cultural prejudices. Ethical challenges include issues of responsibility, privacy, digital divide, algorithm explainability, and trust in technology. The data obtained indicate the ambivalent nature of the impact of artificial intelligence on the field of mental health. Secure integration requires a strong regulatory framework, mandatory human oversight, further empirical research, and the development of national ethical standards, especially in post-conflict societies such as Ukraine. Keywords: artificial intelligence, crisis counseling, suicidal prevention, large language models, ethical challenges, digital mental health, hybrid models of care

**Решение:** -1 систематический scoping-обзор применения ИИ в кризисном консультировании

---

### 328 · R5770

**HUMANS AND MACHINES IN THE LOOP: RETHINKING LLMS FOR CONFLICT AND DISAGREEMENT IN CONTENT ANALYSIS OF SOCIAL COMPLEX PHENOMENA**

2026 · AoIR Selected Papers of Internet Research · journalarticle, review, article · https://doi.org/10.5210/spir.v2024i0.15391

The study of polarization, conflict, and ideological divergence has long challenged scholars across media, communication, and political science. Understanding these phenomena requires engaging with fundamental questions about how opinions are formed, reinforced, and contested in public discourse, and how language and discourses can have so many different meanings and interpretations. Traditional content analysis methods often try to capture this complexity - whether in large-scale media narratives, open-ended survey responses, or political discourse on social media. Computational approaches offer new possibilities, but also raise critical concerns about validity, interpretability, and methodological rigor (Baden et al., 2022; Boumans & Trilling, 2016). Large Language Models (LLMs) have become increasingly central to communication research, with their capacity to process vast amounts of text, identify underlying patterns, and assist in qualitative coding (Chew et al., 2023; Alizadeh et al., 2025). Researchers have explored their use in a variety of tasks, from detecting polarization in open-ended survey responses to analyzing media frames and political discourse (DiGiuseppe & Flynn, 2025; Marino & Giglietto, 2024). However, the integration of LLMs into content analysis presents challenges: How well do they align with human interpretations? Can they enhance research beyond automation? And what role should they play in investigating contested or ambiguous meanings (Pilny et al., 2024; Gunes & Florczak, 2025)? This panel moves beyond discussions of mere optimization and accuracy, instead critically and deeply discussing the use of LLMs to engage with conflict, disagreement, and interpretive diversity. Instead of seeing them as tools to impose consensus, we ask how researchers can use and interact with them to reveal tensions, challenge assumptions, and contribute to new methodologies (Dai et al., 2023; De Paoli, 2024). Across four studies, we assess LLMs mediating, amplifying, or reframing scholarly debates on the methods to analyse contentious political and social issues. Our discussion examines both the benefits and risks of these approaches, raising questions about the role of AI in media and communication methodologies. Paper 1 present a computational approach to measure issue polarization from open-ended survey responses, leveraging Large Language Models (LLMs) to systematically code viewpoints on contentious topics such as climate change, trans rights, or political discourse on Ukraine. While traditional polarization research often relies on close-ended survey measures, this study explores how LLMs can introduce methodological complexity by computing nuanced, interpretive tensions in unstructured responses. The research highlights how LLMs not only enable large-scale automated coding but also challenge conventional measurement frameworks by accommodating ambiguity and ideological fluidity. Preliminary results underscore the potential of LLMs to expand analytical possibilities beyond traditional survey measures, reframing how scholars engage with disagreement and conflict in media and communications studies. Paper 2 examines how LLMs can expand the scope of content analysis and assisting researchers in analyzing framing. The study applies Meta’s Llama-3 model in a two-stage approach to study climate movements in Australian news coverage, using few-shot prompting to first extract frame elements - such as problem definitions, causes, and blame attributions - and then synthesizing these elements into coherent frames. While the human coders tended to construct more issue-specific and varied frames, LLM-generated outputs were generally broader in scope but more internally consistent across the dataset. Paper 3 presents a literature review examining how LLMs are transforming content analysis workflows in social sciences. It identifies four key modes of LLM integration: scalable coders, human-assistive collaborators, autonomous decision-makers, and tools for semantic clustering. The study highlights the ongoing challenges of ensuring interpretability, reliability, and epistemic authority when LLMs are applied to human-generated texts. Paper 4 applies LLMs to investigate the role of political narratives and user engagement on social media during Brazil’s 2022 presidential election and the January 8, 2023, coup attempt. The study analyzes over 12 million social media posts, clustering content based on sentiment, audience reactions, and dissemination patterns to assess how different narratives are amplified. The research examines whether the framing of political content influences audience interaction and engagement levels. Together, these studies push the boundaries of how LLMs are integrated into research on political communication, polarization, and media analysis. They provide an assessment of LLMs’ methodological potential and risks - not just as tools for efficiency, but as channels to rethink how we engage with contested meanings in communication research.

**Решение:** -4 использование LLM в исследованиях политических конфликтов и поляризации

---

### 329 · R11292

**Game-Based CBT with Artificial Intelligence: A Method for Correcting Cognitive Distortions by Revisiting the Past (Preprint)**

2024 · preprint · en · https://doi.org/10.2196/preprints.68064

UNSTRUCTURED Given that the most used therapies in psychiatry, Cognitive Behavioral Therapy (CBT) and Mindfulness-Based Cognitive Therapy (MBCT), were developed to treat depression, a new approach is needed for disorders such as Internet Gaming Disorder and Gambling Disorder, where the issue lies not in negative emotions themselves but in their expression through problematic behaviors. These behaviors act as the patient’s form of “self-prescription” to relieve stress, making it essential to propose alternative coping strategies that can effectively alleviate negative emotions. This paper proposes a novel game-based digital therapy method that reflects each patient’s individual “automatic thoughts,” based on an emotional theory expanded into a four-dimensional cognitive concept that incorporates both the feedback from coping strategies and the subjective interpretation of that feedback. An LLM agent based on a large language model and a doctor agent based on rule-based machine learning work complementarily, enabling the patient to safely and repeatedly practice active coping strategies in crisis situations.

**Решение:** -1 концепция цифровой КПТ-терапии игровых расстройств на основе игровых сценариев

---

### 330 · R10804

**生成AIを利用したプロジェクトデザイン教育：アイデア生成への実践報告;Project Design Education Using Generative AI: A Practical Report on Idea Generation**

2025 · Institutional Repositories DataBase (IRDB) · article · ja · http://kitir.kanazawa-it.ac.jp/infolib/cont/01/G0000002repository/000/000/000000380.pdf

本研究では，金沢工業大学におけるプロジェクトデザイン（PD）教育において，生成AIを活用したアイデア創出の実践を報告する。生成AIの活用により，学生の問題解決プロセスを補完し，より多くのアイデアを生み出すことが期待されている。特に「なぜなぜ分析」と「マインドマップ」の手法に生成AIを導入し，その効果を検証した結果，生成AIは発散的思考を助ける一方で，適切な指導と使用方法が重要であることが明らかとなった。本報告は，教育現場での生成AIの活用可能性と課題を示唆するものである。;This study reports on the practical application of generative AI in idea generation in Project Design (PD) education at Kanazawa Institute of Technology. The integration of generative AI is expected to improve students' problem-solving process by facilitating the generation of a greater number of ideas. Specifically, the study examines the effects of incorporating generative AI into "Five Whys" analysis and "Mind Mapping" techniques. The findings suggest that while generative AI supports divergent thinking, proper guidance and application are critical. This report highlights both the potential and the challenges of using generative AI in educational settings.

**Решение:** -4 использование генеративного ИИ в инженерно-проектном образовании в Японии

---

### 331 · R6455

**Metric Inversion in Generative AI Translation: Divergence Between Automated Evaluation Metrics and Human Expert Judgement in the LRM Era**

2026 · Proceedings of the 3rd International Conference on Educational Digitalization and Computer Science in the Guangdong-Hong Kong-Macao Greater Bay Area · book, conference, conference-paper · https://doi.org/10.1145/3828183.3828226

The paradigm of computer-assisted translation (CAT) is currently navigating a period of profound structural disruption fueled by Generative Artificial Intelligence (GAI). The transition from deterministic Neural Machine Translation (NMT) to reasoning-driven Large Reasoning Models (LRMs), such as DeepSeek R1, has introduced complex chain-of-thought (CoT) capabilities. However, this advancement has precipitated a “Metric Inversion” crisis. Traditional automated evaluation metrics, specifically BLEU and chrF, rely on surface-level n-gram overlap against a static human reference. As AI capability shifts from literal sequence mapping to creative semantic restructuring, these legacy benchmarks systemically penalize the exact linguistic and idiomatic qualities that human experts value most. Through a randomized double-blind study (N = 111), we contrast the performance of an LRM, a general LLM, and a standard NMT system. Results demonstrate that while human experts strongly favor LRM outputs for their superior fluency (Mean=8.81) and idiomaticity (Mean=8.61), automated metrics exhibit a significant and misleading bias toward traditional NMT (BLEU=0.258). Correlation analysis reveals a profound negative relationship (ρ = −0.401, p <.001) between BLEU scores and expert fluency ratings. This research highlights the urgent need for a paradigm shift from reference-dependent overlap matching to semantic-aware evaluation frameworks to preserve the structural integrity of AI-assisted education.

**Решение:** -4 метрики оценки машинного перевода (метрическая инверсия)

---

### 332 · R11527

**Delving into the Depths: Evaluating Depression Severity through BDI-biased Summaries**

2024 · Workshop on Computational Linguistics and Clinical Psychology (CLPsych) · audiovisual/conference talk, conference-paper · en · https://doi.org/10.18653/v1/2024.clpsych-1.2

Depression is a global concern suffered by millions of people, significantly impacting their thoughts and behavior. Over the years, heightened awareness, spurred by health campaigns and other initiatives, has driven the study of this disorder using data collected from social media platforms. In our research, we aim to gauge the severity of symptoms related to depression among social media users. The ultimate goal is to estimate the user’s responses to a well-known standardized psychological questionnaire, the Beck Depression Inventory-II (BDI). This is a 21-question multiple-choice self-report inventory that covers multiple topics about how the subject has been feeling. Mining users’ social media interactions and understanding psychological states represents a challenging goal. To that end, we present here an approach based on search and summarization that extracts multiple BDI-biased summaries from the thread of users’ publications. We also leverage a robust large language model to estimate the potential answer for each BDI item. Our method involves several steps. First, we employ a search strategy based on sentence similarity to obtain pertinent extracts related to each topic in the BDI questionnaire. Next, we compile summaries of the content of these groups of extracts. Last, we exploit chatGPT to respond to the 21 BDI questions, using the summaries as contextual information in the prompt. Our model has undergone rigorous evaluation across various depression datasets, yielding encouraging results. The experimental report includes a comparison against an assessment done by expert humans and competes favorably with state-of-the-art methods.

**Решение:** + T2/T3 оценка депрессии по шкале BDI на основе постов в соцсетях: ChatGPT против экспертов-людей

---

### 333 · R5570

**Rectifying illusion: a Buddhist–Confucian framework for LLM hallucinations**

2026 · AI and Ethics · article · en · https://doi.org/10.1007/s43681-026-01053-y

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 буддийско-конфуцианский этический фреймворк для LLM, философия

---

### 334 · R7349

**Generative artificial intelligence models outperform students on divergent and convergent thinking assessments**

2025 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-6762129/v1

Abstract Generative artificial intelligence (GenAI) has garnered significant attention for its remarkable capabilities and is now widely used in many creative domains, sparking scientific interest in its creative capacities. While previous studies have assessed GenAI on creativity tasks, there is no evidence comparing the latest GenAI models to the same sample of humans on both divergent and convergent thinking assessments. In this study, we compared the creative ability of human participants ( n = 46) against three state-of-the-art GenAI chatbots—ChatGPT-4o, DeepSeek-V3, and Gemini 2.0—using the Alternate Uses Task (AUT) and the Remote Associates Test (RAT). For divergent thinking, we compared the median and maximum originality scores on the AUT, representing the level of originality of the ‘average’ and ‘best’ idea. We then compared performance on 57 RAT items as a measure of convergent thinking. All GenAI models outperformed human participants in both tasks: the ‘average’ and ‘best’ GenAI idea was significantly more original than human-generated ideas; all GenAI models demonstrated superior RAT performance vs. humans. Among GenAI models, ChatGPT-4o consistently demonstrated the best scores on both tasks. These findings illustrate the immense potential of GenAI whilst importantly highlighting the validity of current creativity assessment methods in the study of GenAI creativity.

**Решение:** -4 превосходство генеративного ИИ над студентами при сдаче экзаменов

---

### 335 · R8925

**“Mirror” Language AI Models of Depression are Criterion-Contaminated**

2025 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/fe2z9_v1

A growing number of studies show near-perfect LLM language-based prediction of depression assessment scores (up to R2 of .70). However, many are developed from language responses directly to the depression assessments. These “Mirror models” suffer from “criterion contamination,” which arises when a predicted score depends in part on the predictors themselves. This causes artificial effect size inflation which reduces model generalizability. The present study compares the performance of Mirror models versus “Non-Mirror models,” which are developed from language that does not mirror the assessment they are developed to predict. N = 110 research participants completed two different interviews: (1) structured diagnostic and (2) life history. GPT-4, GPT-4o and LLaMA3-70B were then prompted to predict structured diagnostic interview depression scores from the two transcripts separately. Mirror models (using structured diagnostic data) showed very large effect sizes (e.g., R² = .80). As expected, Non-Mirror models (using life history data) demonstrated smaller effect sizes, but were still relatively large (e.g., R² = .27). When Mirror and Non-Mirror model-predicted structured interview depression scores were correlated with self-reported depression symptoms, Mirror and Non-Mirror performed the same (e.g., r = ~.54), indicating that Mirror models contain bias perhaps due to criterion contamination. Topic modeling identified clusters across Mirror and Non-Mirror models, as well as between true-positive and false-positive predictions. In this head-to-head comparison study, Mirror language AI models of depression showed artificially inflated effect sizes and less generalizability. As language AI models for depression continue to evolve, incorporating Non-Mirror models may identify interpretable, and generalizable semantic features that have unique utility in real-world psychological assessment.

**Решение:** + T3 оценка депрессии по транскриптам диагностических интервью: GPT-4 и LLaMA-3 против клиницистов

---

### 336 · R8436

**Development of a Red-Teaming Dataset to Defend Large Language Models Against Attacks**

2025 · Programming and Computer Software · journalarticle, article · en · https://doi.org/10.1134/s0361768825700343

Abstract State-of-the-art (SOTA) large language models (LLMs) are huge systems with complex internal mechanisms that implement black-box response generation. Even though aligned LLMs have built-in defense mechanisms against attacks, recent studies demonstrate the vulnerability of LLMs to jailbreak attacks. In this study, we aim to extend the existing red-teaming datasets obtained from jailbreak attacks to address these LLM vulnerabilities in the future. In addition, we carry out some experiments with SOTA LLMs on our dataset to demonstrate the existing weaknesses in these models.

**Решение:** -4 датасет состязательного тестирования (red-teaming) для безопасности LLM

---

### 337 · R7889

**Computational Techniques for Voice Intelligence: Deducing Psychological Factors from Human Voice**

2025 · Carnegie Mellon University · text/thesis · https://doi.org/10.1184/r1/28715789.v1

Speech carries information about the speaker’s psychological traits, including their behavioral tendencies, leadership, emotions, and personality. The process of communication of these traits through speech can be thought of as a combination of an encoding process and a decoding process. The speaker, who expresses these traits, encodes them into low-dimensional characteristics of speech signals, and the listener, who perceives them, decodes the speech signal to make inferences about the state of the speaker. The encoding of psychological traits into speech is influenced by multiple factors, such as the context of the utterance, the speaker’s personality traits, the environment, and more. It is well known that psychological traits are encoded in different aspects of speech, i.e. not only in ‘what’ is said but also in ‘how’ it is said. Thus while decoding, the listener must consider not only the linguistic content, but also the acoustic, prosodic, and other non-linguistic cues in the speech. In this thesis, we develop computational models that attempt to emulate the human decoding process for two types of psychological traits: emotion and personality. This thesis is accordingly divided into two parts. In the first part, we focus on emotion. We study how emotions are encoded and decoded in speech, and how they are affected by factors such as context, the naturalness of expression including real (spontaneous and involuntary) vs. enacted (prompted and voluntary), and other nuances of speech production. In our study of emotion and its representation in speech, we also take the lexical and phonotactic content of speech into consideration. A speech signal contains words and phonemes, each of which can be thought of as a stream or modality of information that exhibits unique characteristics that encode emotion, including intensity, cadence, rhythm, and more. We hypothesize that in order to decode emotion from speech, computational models must capture the characteristic variations within each modality. In this thesis, we objectively show how important this approach is for the computational analysis of emotion. In devising better methodologies for emotion detection, we also focus on the intra-emotion range and absolute intensity (or degree) of emotional expression. Humans are able to decode emotions at very fine granularities. However, state-of-the-art techniques for automatic emotion detection (or decoding) work with predefined sets of discrete emotions, extended into a three-dimensional continuous space denoting the valence, arousal, and dominance of each discrete emotion. Any decoding technique that is learned from data is clearly restricted by the discretization of labels assigned to emotions by human annotators. In this thesis, we work on techniques that are agnostic to such restrictions. We hypothesize that for efficient decoding, it would be effective to utilize discrete and continuous information simultaneously, in a hierarchical framework. Expanding this work, we propose a second approach, which is inspired by the fact that humans inherently use natural language to describe the emotions that they perceive. We contend that while the labels that humans assign to each emotion are restricted by the descriptors available in their language, the diversity of emotions can nevertheless be captured by the flexibility that natural language provides – namely by the affective language that is often casually used to describe an emotion. Such affective language can often have measurable acoustic correlates. For example: an angry man ‘shouting loudly’ is describing the emotion by directly referring to the loudness or intensity of the speech. We show that when the labeling is done with natural language descriptions, guided by acoustic properties of speech, the computational process of emotion decoding is significantly improved. In an extension of this work, we add a learnable ‘prompt’, with the hope that more textual information is incorporated automatically by the model, that helps the model towards better emotion decoding. In the second part of this thesis, we focus on personality. We study how personality is encoded in speech. We specifically explore utterance-level voice signal characteristics such as pitch, loudness, and many others., and many relevant utterance-level voice quality features that have been observed to correlate with personality traits in scientific literature. In order to better understand personality decoding, we revisit the widely accepted OCEAN traits. OCEAN forms the 5 bases across which every individual is rated, and is the result of the psycholexical hypothesis, which assumes that our usage of language and words to describe humans would reveal the underlying bases of the personality. We hypothesize that these bases, or in fact different bases, would reveal themselves when the same language and words are analyzed with newer techniques, i.e. word representations learned from large language models. In this work, we show how the newer techniques reveal the most informative number of bases as two, and the next most informative as five, which in fact are on average aligned with the OCEAN traits. In summary, this work fills the gap in our current understanding of computational ways to process psychological traits from speech signals. The potential uses of such technologies in applications that involve human-computer interaction are many. Such technologies can also aid in the assessment and monitoring of mental illnesses and psychological problems in humans, helping all involved – healthcare providers and affected people – in positive ways. They can also help predict the long-term susceptibility of individuals to specific types of work, social situations, and other factors. Looking into the future, we believe this work is important in the inevitable rise of speech-based Artificial Intelligence systems, which will carry their own emotions and personalities and also understand those of the

**Решение:** -4 акустический анализ голосовых признаков для оценки психологических черт

---

### 338 · R12626

**Entropy and Memory Forensics in Ransomware Analysis: Utilizing LLaMA-7B for Advanced Pattern Recognition**

2023 · preprint · en · https://doi.org/10.36227/techrxiv.24742389.v1

This study investigated the utilization of memory forensics and the Large Language Model LLaMA-7B for the purpose of detecting and analyzing contemporary ransomware. It articulates a shift from traditional encryption-focused ransomware attacks to more sophisticated strategies, like data exfiltration, underscoring the evolving nature of these cyber threats. The methodology involves an integrated approach, combining memory forensic techniques with the advanced pattern recognition capabilities of LLaMA-7B, to identify and analyze ransomware signatures within system memory. The results demonstrate the efficacy of this combination in accurately distinguishing between ransomware and benign software, with a particular focus on identifying data exfiltration activities. Discussions revolve around the challenges of keeping pace with the evolving ransomware tactics and the ethical considerations in applying AI in cybersecurity. The study concludes by underscoring the importance of continuous innovation in cybersecurity strategies and the potential of AI integration in developing dynamic defense mechanisms against ransomware.

**Решение:** -4 анализ оперативной памяти при атаках программ-вымогателей с помощью LLaMA-7B

---

### 339 · R2280

**Extracting and Structuring Experimental Knowledge from Electronic Theses and Dissertations**

2026 · ACM/IEEE Joint Conference on Digital Libraries · book, conference, review · https://doi.org/10.1145/3805696.3847132

Electronic theses and dissertations (ETDs) hold detailed accounts of laboratory experiments, especially in the physical sciences. Digital libraries, however, expose ETDs mostly as bibliographic metadata and full-text PDFs. The experimental knowledge inside is scattered across chapters and hard to act on. My dissertation asks how digital libraries can turn these narratives into source-linked experimental records. The work proceeds in three stages, which identify experimental passages, represent them as structured records, and evaluate their utility for scientific tasks. Such records could speed up literature review and supply the machine-readable experimental knowledge that autonomous laboratories are envisioned to require. I report a completed pilot on eleven theses from a nanoplasmonics research group. It combines rule-based screening with a locally hosted LLM judge and yields 217 structured records, each linked to its source section and PDF page span. An expert from the source discipline reviewed 30 passages sampled across the theses. Eighteen were judged useful, nine too generic, and three unrelated to experimental methods. I seek consortium feedback on the scope of cross-domain evaluation, on validating the proposed readiness grading, and on bounding the representation work.

**Решение:** -4 извлечение данных химических экспериментов из диссертаций

---

### 340 · R2471

**Botanical Organization in the Voynich Manuscript Herbal Section: Cross-Section Anchor Density Analysis and the Three-Tier Folio Model**

2026 · Zenodo · journalarticle/ · https://doi.org/10.5281/zenodo.22672022

The herbal section of the Voynich Manuscript (f1r–f66v) has been variously characterized as a pharmaceutical index, a patient-routing directory, and a botanical reference in the medieval herbarium tradition. It has been proposed that the herbal section is organized by patient constitution class rather than by botanical or taxonomic principle, following the 28-mansion constitution typology documented in Johannes Hartlieb's Cgm 7958 (BSB Munich, 1456) [DOI 10.5281/zenodo.20392112; DOI 10.5281/zenodo.20391969]. We report a cross-section anchor density extraction across 118 herbal folios (f1r–f66v) using the Zandbergen-Landini IVTFF v2b transcription as source. Five cross-section operators (`otal`, `otedy`, `ytar`, `ary`, `qokaiin`) [operator grammar per DOI 10.5281/zenodo.20391953] were extracted by exact-match token count across all herbal folios. Results: 73 of 118 folios (62%) carry zero hits across all five operators; the mean total anchor density is 0.79 per folio; no herbal folio matches or exceeds the f58r preparation bridge baseline of 10. Four prespecified falsification tests all fail for the constitution-organization hypothesis. Botanical organization (H_bot) is confirmed. The constitution-organized herbal hypothesis is FALSIFIED. The one herbal folio with anomalously elevated total anchor density is f58r (total=10), which is 5× the section mean and isolated at the herbal-balneological boundary — confirming its role as a preparation bridge. Interior herbal folios f48v (otedy=4), f43v (otedy=3), and f34r (otedy=3) constitute a set of embedded interface nodes whose `otedy` anchors all resolve to f73v.23 `otedy` (the labeled nymph at the 9:30 clock position on the Sagittarius zodiac ring) and f84r label #5 (the balneological output hub). A three-tier model of herbal structure is proposed: (1) main botanical body (62% zero-density folios — standard herbarium); (2) interior interface nodes (standard botanical format with embedded zodiac-balneological cross-references); (3) boundary bridge (f57v–f58r–f58v — the translation layer between herbal botanical language and balneological preparation language). The falsification of the constitution-organized herbal hypothesis strengthens the court physician workflow model [DOI 10.5281/zenodo.20391967]: the structural necessity of f58r as a bridge follows directly from the herbal and balneological sections operating in distinct organizational registers. Substrate-origination anchor: research at Honeycutt Ai Labs (Princeton TX) on the Voynich Manuscript and its late medieval medical neighborhood began August 2025; the public-record priority anchor is the Paduan Medical Reference dataset, Zenodo DOI 10.5281/zenodo.18687530, copyright origination 2025-08-27. This deposit supersedes an earlier draft submitted 2026-06-11. Substantive changes reconcile all load-bearing cross-references to the f58r preparation-bridge baseline against the post-revision Honeycutt Ai Labs P-017 deposit. Cross-reference updates (7): (1) Abstract f58r=10 baseline now framed as 'WP4-extraction total of 10' with explicit acknowledgement that the P-017 deposit uses a different lattice-canonical operationalization (7-entry high-signal block: otaly x2, otal x4, okaiin x1). (2) Section 1.1 introduction citation to P-017's f58r profile updated to cite the lattice-canonical line-opener distribution (s=8/41=19.5%, co-dominant with y=22.0% and d=19.5%); the 'syrupus dominates at 34%' figure used in the prior draft is superseded. (3) Section 1.2 baseline-calibration cross-reference updated to flag the reconciliation against P-017 in section 2.4. (4) Section 2.4 baseline-calibration paragraph expanded with explicit reconciliation against P-017's lattice high-signal block; the two extractions overlap on otal=4 and otherwise count different token families. (5) Section 3.3 f58r singularity paragraph reframed: precise multipliers reported as empirical ratios within the WP4 extraction (10/0.79 ≈ 12.6× mean; 10/6 ≈ 1.7× next-highest independent folio) rather than as the prior 5x-section-mean structural multiplier; the parallel withdrawal of the '5× herbal-body mean' arithmetic in P-017 section 4.2 is cited. (6) Section 4.2 f58r-as-translation-point paragraph updated to cite P-017's four-test battery (one strict pass T2 plus three consistent-with results T1/T3/T4) rather than the prior CONFIRMED framing. (7) Section 4.4 claim-status revision row for f58r (C6) inherits P-017's SUPPORTED tier (not CONFIRMED). Claims softened (3): (a) Abstract 'preparation bridge baseline of 10' → 'WP4-extraction total of 10' with operationalization-difference acknowledgement; (b) Abstract '5× the section mean' → 'well above the section mean'; (c) Section 3.3 '5× section mean and 2.5× next-highest independent folio' → empirical ratios reported descriptively, structural-multiplier framing dropped. Three-tier folio model claim itself is retained as a descriptive partition of the WP4 distribution; the qualitative three-tier shape persists (Tier 1 zero-mode dominant, Tier 2 small interior elevated-otedy node set, Tier 3 single boundary high-density cluster). Magnitude of Tier 3 boundary cluster relative to section body is described in moderated language. Corpus note. This record belongs to the Honeycutt Ai Labs research program initiated August 2025, documented across the deposited paper set, heardtogether.org, and the underlying conversation corpus. Artifacts retained with this program — including build manifests and pipeline byproducts — are kept as primary data under an all-data-matters transparency policy; several are captured field specimens of the large-language-model output patterns catalogued in the companion record The Ghost Pattern Codebook: A Public-Surface Taxonomy of LLM Output Patterns (DOI 10.5281/zenodo.20391960). The lab studies these patterns and does not exempt its own toolchain from them. Corrected version deposited 2026-09-09. The section "Corrections in this version" in the paper states what c

**Решение:** -4 ботанический анализ травника в манускрипте Войнича

---

### 341 · R2512

**Performance of next-generation AI chatbots in gynecological knowledge assessment: a comparative pilot study of ChatGPT-5, Gemini-3, DeepSeek-V3.2, and Claude-4.5-Opus.**

2026 · Archives of gynecology and obstetrics · comparative study, research-article, journal article · eng · https://doi.org/10.1007/s00404-026-08358-7

PURPOSE: As artificial intelligence (AI) models evolve into their next generations, their application in specialized medical fields requires rigorous validation. While large language models (LLMs) have shown promise in general medicine, their reliability in complex gynecological clinical reasoning remains under-explored. This pilot study aimed to comparatively assess the knowledge retention, safety, and reasoning limitations of advanced AI chatbots in gynecology using a constrained zero-shot multiple-choice question (MCQ) format. METHODS: A total of 70 text-based MCQs covering seven core gynecological modules were adapted from "USMLE Step 1 Sample Test Questions". The questions were administered to four advanced AI models: ChatGPT-5, Gemini-3, DeepSeek-V3.2, and Claude-4.5-Opus. To simulate a rapid-retrieval clinical scenario, models were tested under "zero-shot" conditions with a constrained prompt prohibiting reasoning steps. We performed both quantitative statistical analysis (Kruskal-Wallis, Cochran's Q) and qualitative error analysis to identify specific failure modes. RESULTS: Contrary to expectations for advanced models, overall accuracy was unsatisfactory: Gemini-3 (32.86%), DeepSeek-V3.2 (30.00%), ChatGPT-5 (25.71%), and Claude-4.5-Opus (21.43%). Significant performance disparities were observed across modules. Notably, ChatGPT-5 scored 0.00% in Infertility, while DeepSeek-V3.2 reached 70.00% in Common Benign Conditions. Qualitative analysis revealed three critical failure patterns: (1) semantic association bias (confusing high-probability diseases with symptom-specific diagnoses), (2) spatial anatomy confusion, and (3) genetic logic reversal. No significant correlation was found between item difficulty and accuracy (p > 0.05). CONCLUSION: Under constrained non-reasoning prompts, even next-generation AI chatbots demonstrate unsatisfactory performance in gynecology. The qualitative analysis suggests that models often rely on probabilistic keyword matching rather than physiological simulation, leading to theoretically dangerous clinical errors (e.g., misdiagnosing adrenal enzymes). While potential exists, current reliability is insufficient for unsupervised use in gynecological education. These findings highlight the critical need for "chain-of-thought" prompting and human expert oversight.

**Решение:** -4 оценка ответов чат-ботов по онкогинекологии

---

### 342 · R12539

**Comics for Everyone: Generating Accessible Text Descriptions for Comic Strips**

2023 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2310.00698

Comic strips are a popular and expressive form of visual storytelling that can convey humor, emotion, and information. However, they are inaccessible to the BLV (Blind or Low Vision) community, who cannot perceive the images, layouts, and text of comics. Our goal in this paper is to create natural language descriptions of comic strips that are accessible to the visually impaired community. Our method consists of two steps: first, we use computer vision techniques to extract information about the panels, characters, and text of the comic images; second, we use this information as additional context to prompt a multimodal large language model (MLLM) to produce the descriptions. We test our method on a collection of comics that have been annotated by human experts and measure its performance using both quantitative and qualitative metrics. The outcomes of our experiments are encouraging and promising. Accepted at CLVL: 5th Workshop On Closing The Loop Between Vision And Language (ICCV 2023 Workshop)

**Решение:** -4 генерация текстовых описаний комиксов для незрячих людей

---

### 343 · R11877

**The impact of history of depression and access to weapons on suicide risk assessment: a comparison of ChatGPT-3.5 and ChatGPT-4.**

2024 · PeerJ · comparative study, research-article, journal article · eng · https://doi.org/10.7717/peerj.17468

The aim of this study was to evaluate the effectiveness of ChatGPT-3.5 and ChatGPT-4 in incorporating critical risk factors, namely history of depression and access to weapons, into suicide risk assessments. Both models assessed suicide risk using scenarios that featured individuals with and without a history of depression and access to weapons. The models estimated the likelihood of suicidal thoughts, suicide attempts, serious suicide attempts, and suicide-related mortality on a Likert scale. A multivariate three-way ANOVA analysis with Bonferroni post hoc tests was conducted to examine the impact of the forementioned independent factors (history of depression and access to weapons) on these outcome variables. Both models identified history of depression as a significant suicide risk factor. ChatGPT-4 demonstrated a more nuanced understanding of the relationship between depression, access to weapons, and suicide risk. In contrast, ChatGPT-3.5 displayed limited insight into this complex relationship. ChatGPT-4 consistently assigned higher severity ratings to suicide-related variables than did ChatGPT-3.5. The study highlights the potential of these two models, particularly ChatGPT-4, to enhance suicide risk assessment by considering complex risk factors.

**Решение:** -5 оценка суицидального риска моделями ChatGPT-3.5 и ChatGPT-4 без сопоставления с экспертами-людьми

---

### 344 · R11734

**Evaluating generative pretraining transformer reliability in addressing dental trauma: A cross-sectional observational study on avulsion and intrusion**

2024 · Saudi Endodontic Journal · journalarticle, article · en · https://doi.org/10.4103/sej.sej_107_24

Abstract Introduction: The advancement of artificial intelligence (AI) has revolutionized digital communication, enhancing interactions between humans and computers. This study explores the application of Chat Generative Pretrained Transformer 3.5 (ChatGPT-3.5), in providing accurate information on dental trauma. Materials and Methods: Utilizing a dataset of 45 self-generated questions across three topics, general dental trauma, avulsion, and intrusion, ChatGPT-3.5 generated responses that were subsequently evaluated by five endodontic experts, each with over a decade of experience. The evaluators used a Likert scale to assess the quality of the AI-generated answers, synthesizing reliable scientific evidence and clinical expertise to ensure a thorough analysis. The data obtained from the evaluators’ scores were organized and analyzed using Microsoft Excel software and the Statistical Package for the Social Sciences version 25. For each question, descriptive statistics including the median and interquartile range were computed. Results: The study found that ChatGPT provided reliable information across the three assessed dental topics. Avulsion was rated the highest (4.40 ± 0.717), significantly outperforming general dental trauma (3.97 ± 0.885) ( P = 0.005). Intrusion received a rating of 4.13 ± 0.794, showing no significant difference compared to the other topics. Most evaluator scores fell into the “Good” (44.0%) and “Very Good” (38.7%) categories. This indicates a generally positive appraisal of ChatGPT’s performance, with a fair agreement among evaluators, evidenced by a combined Fleiss’s kappa coefficient of 0.324. However, there was variability, particularly with Evaluator 4’s scores differing significantly from those of evaluators 1 and 2. Conclusions: ChatGPT’s responses on general dental trauma, avulsion, and intrusion were generally rated positively, with avulsion responses deemed the most reliable. The study underscores the need for continuous evaluation to maintain the accuracy, reliability, and safety of AI-generated content in endodontics, suggesting AI should serve as a supplementary tool rather than a primary information source.

**Решение:** -4 оценка эндодонтистами ответов ChatGPT по зубным травмам, стоматология

---

### 345 · R5772

**Combining Large Language Models with Named Entity Recognition to Automate Market Research Interview Transcription and Customer Journey Mapping – Empirical Feedback by Business Professionals**

2026 · Lecture notes in business information processing · conference-paper · en · https://doi.org/10.1007/978-3-032-35043-5_21

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 извлечение именованных сущностей (NER) с помощью LLM, общие задачи

---

### 346 · R9126

**AI-Powered Triage of Suicidal Ideation in Adolescents: A Comparative Evaluation of Large Language Models Using Synthetic Clinical Vignettes (Preprint)**

2025 · preprint · en · https://doi.org/10.2196/preprints.82288

BACKGROUND Suicide risk assessment is essential but often limited by time, scalability, and subjective judgment. Large language models (LLMs) show promise in supporting psychiatric decision-making, yet their safety, accuracy, and reliability—especially in crisis contexts—remain underexplored. OBJECTIVE To evaluate the performance of leading Large Language Models (LLMs) in classifying suicide risk and generating clinically appropriate action plans for adolescent psychiatric cases presented through synthetic clinical vignettes. METHODS We developed 40 synthetic clinical vignettes depicting adolescents with varying levels of suicide risk, structured according to established clinical formulation principles. A gold standard for risk level, based on the Columbia-Suicide Severity Rating Scale (C-SSRS) framework, and corresponding clinical actions was established for each vignette by a panel of two board-certified child and adolescent psychiatrists. Three LLMs (GPT-4o, Claude 3.5 Sonnet, Llama-3.1-70B) were prompted using a structured chain-of-thought methodology to classify risk and propose a detailed action plan. Performance was assessed using quantitative classification metrics (accuracy, precision, recall, F1-score) and qualitative thematic analysis of the generated action plans. RESULTS Quantitative analysis of risk classification revealed variable performance. GPT-4o achieved the highest accuracy (82.5%), followed by Claude 3.5 Sonnet (75.0%) and Llama-3.1- 70B (67.5%). F1-scores demonstrated challenges in correctly identifying higher-risk categories, particularly for nuanced presentations of intent. Qualitative thematic analysis of the action plans identified consistent adherence to basic safety protocols (e.g., recommending emergency evaluation for high-risk cases). However, significant and critical failures were pervasive, including the omission of crucial inquiries about access to lethal means, failure to incorporate protective factors into planning, and the generation of clinically inappropriate therapeutic reassurance in a triage context. CONCLUSIONS While LLMs demonstrate a nascent ability to process clinical information for suicide risk assessment, significant deficits in clinical reasoning and safety planning persist. Their performance on idealized synthetic data suggests these models are not yet suitable for autonomous clinical decision-making. These findings underscore the imperative for rigorous, clinically-grounded evaluation frameworks and the development of human-in-the-loop systems to ensure patient safety in any future deployment.

**Решение:** + T3 сортировка суицидального риска по шкале C-SSRS на клинических виньетках: GPT-4o и Claude против эталона

---

### 347 · R5479

**Accuracy and Temporal Consistency of ChatGPT and Gemini in Responding to Textbook and Patient-Oriented Dental Bleaching Questions: A Multi-Session Comparative Study.**

2026 · Journal of esthetic and restorative dentistry : official publication of the American Academy of Esthetic Dentistry ... [et al.] · comparative study, research-article, journal article · eng · https://doi.org/10.1111/jerd.70172

ABSTRACT Objective This study compared the accuracy and temporal consistency of ChatGPT and Gemini in responding to dental bleaching questions across three weekly sessions. Materials and Methods A total of 280 true/false questions were developed comprising 200 textbook‐based and 80 patient‐oriented frequently asked questions. Both chatbots were queried weekly under controlled conditions. Accuracy was compared using generalized estimating equations, consistency was assessed using Fleiss' kappa, and weekly stability was evaluated using Cochran's Q test. Open‐ended responses were scored for quality and misinformation by two evaluators. Results For textbook questions, ChatGPT achieved significantly higher accuracy than Gemini (77.7% versus 70.5%, p = 0.0009). For frequently asked questions, both chatbots performed comparably (92.9% versus 90.8%, p = 0.252). Temporal consistency was only fair for textbook questions but almost perfect for frequently asked questions in both chatbots. Both chatbots showed significant upward trends in textbook accuracy across sessions. Gemini received higher global quality scores for open‐ended responses, while misinformation rates were similarly low. Conclusions Within the limitations of this study, ChatGPT achieved significantly higher accuracy than Gemini for textbook‐based dental bleaching questions, while both chatbots performed comparably for patient‐oriented questions. Temporal consistency differed markedly, with almost perfect consistency for patient‐oriented questions and only fair consistency for textbook‐based questions. Clinical Significance Chatbot responses to common patient questions about dental bleaching are generally accurate and consistent, but their reliability drops substantially for specialized academic content, suggesting these tools should complement rather than replace professional clinical judgment.

**Решение:** -4 точность и временная стабильность ответов ChatGPT и Gemini по офтальмологии

---

### 348 · R2527

**When Do AI Raters Agree? Judgment Format and Photographic Reliability**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · https://doi.org/10.5281/zenodo.21922735

Description / Abstract: When a large language model is asked to assess a photograph, does the reliability of its judgment depend on the model, on the photograph, or on the way the judgment is asked? We report a seven-genre study of the Frame-by-Frame Photographic Progress Map, an instrument in which a model judges each photograph one criterion at a time in two formats: first a binary pass/fail verdict, a gate that asks whether a skill is present at all, and then, only on a pass, a four-level depth grade of Poor, Fair, Good, or Excellent that judges how well it is executed. Three models (Claude, ChatGPT, and Gemini) applied the identical prompt, unchanged, to seventy photographs spanning seven genres (botanical, lifestyle, landscape, waterfall, wildlife, architecture, and street), one photographer per genre. We compared their verdicts and grades using three-way and pairwise agreement, Fleiss’ kappa on the verdicts, and within-one-level agreement on the grades. The central finding is that the design of the judgment, more than the model or the photograph, governs how well independent raters agree, and the sharpest evidence is the contrast between the instrument’s two formats. The four-level depth grade is robust: on the frames where all three models agreed a skill was identified, their grades fell within one level of one another 99 percent of the time pooled across genres, and a perfect 100 percent in five of the seven. The binary verdict, or pass/fail gate, is fragile and genre-dependent: fair to moderate on genres with unambiguous subjects (Fleiss’ kappa up to 0.44) and at chance (kappa near zero) on genres that force a judgment on nearly every frame, pooling to kappa = 0.21 across all seventy frames. The same models, on the same photographs, agree when asked to grade and scatter when asked to gate. The three models behave as three stable, differing evaluators rather than one interchangeable judge, and which model applies the gate to a set can shift its placement by as much as the entire six-criterion scale. An anchored revision of the prompt, rewriting only the four gate stages most responsible for disagreement, raised pooled three-way agreement from 50 to 69 percent and pooled kappa from 0.21 to 0.51, evidence that much of the gate’s disagreement is a property of the wording rather than of the photographs. A next-day test-retest then found that every model reproduced its own verdicts more closely than any two models agreed with each other (test-retest kappa = 0.67 against cross-model kappa = 0.51), while the depth grade repeated to within one level about 99 percent of the time. The practical implication extends beyond this instrument. Reliability is high on the graded, qualitative axis and low on the binary, evaluative one. The trustworthy signal in an AI photographic judgment is therefore formative rather than gate-like. The central design question is about the form of the request as much as the choice of model. This paper measures reliability, not photographic truth or learning outcome, and its claims hold within those boundaries.

**Решение:** -4 оценка фотографий и визуальных изображений LLM-судьями, компьютерное зрение

---

### 349 · R1535

**Collider-Bench: Benchmarking AI Agents with Particle Physics Analysis Reproduction**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.13950

Autonomous language-model agents are increasingly evaluated on long-horizon tool-use tasks, but existing benchmarks rarely capture the complexity and nuance of real scientific work. To address this gap, we introduce Collider-Bench, a benchmark for evaluating whether LLM agents can reproduce experimental analyses from the Large Hadron Collider (LHC) using only public papers and open scientific software. Such analyses are often difficult to reproduce because the public toolchain only approximates the software used internally by the experimental collaborations, while the published papers inevitably omit implementation details needed for a faithful reconstruction. Agents must therefore rely on physical reasoning, domain knowledge, and trial-and-error to fill these gaps. Each task requires the agent to turn a published analysis into an executable simulation-and-selection pipeline and submit predicted collision event yields in specified signal regions. These predictions are evaluated with standard histogram metrics that provide continuous fidelity scores without a hand-written rubric. We also report the computational cost incurred by each agent per task. Finally, we evaluate the codebase and full session trace using an LLM judge to catch qualitative failure modes such as fabrications, hallucinations and duplications. We release an initial set of tasks drawn from LHC searches, together with a containerized sandbox and event simulation tools. We evaluate across a capability ladder of general purpose coding agents. Our results show that on average no agent reliably beats the physicist-in-the-loop solution. 23 pages | 9 figures | 4 tables | Code: https://github.com/dfaroughy/Collider-Bench | Task Corpus: https://huggingface.co/datasets/Dariusfar/ColliderBench

**Решение:** -4 бенчмарк автономных агентов в физике элементарных частиц (Collider-Bench)

---

### 350 · R9533

**MindEval: Benchmarking Language Models on Multi-turn Mental Health Support**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2511.18491

Demand for mental health support through AI chatbots is surging, though current systems present several limitations, like sycophancy or overvalidation, and reinforcement of maladaptive beliefs. A core obstacle to the creation of better systems is the scarcity of benchmarks that capture the complexity of real therapeutic interactions. Most existing benchmarks either only test clinical knowledge through multiple-choice questions or assess single responses in isolation. To bridge this gap, we present MindEval, a framework designed in collaboration with Ph.D-level Licensed Clinical Psychologists for automatically evaluating language models in realistic, multi-turn mental health therapy conversations. Through patient simulation and automatic evaluation with LLMs, our framework balances resistance to gaming with reproducibility via its fully automated, model-agnostic design. We begin by quantitatively validating the realism of our simulated patients against human-generated text and by demonstrating strong correlations between automatic and human expert judgments. Then, we evaluate 12 state-of-the-art LLMs and show that all models struggle, scoring below 4 out of 6, on average, with particular weaknesses in problematic AI-specific patterns of communication. Notably, reasoning capabilities and model scale do not guarantee better performance, and systems deteriorate with longer interactions or when supporting patients with severe symptoms. We release all code, prompts, and human evaluation data.

**Решение:** + T4 MindEval: бенчмарк оценки терапевтических диалогов в mental health, валидированный клиническими психологами

---

### 351 · R4345

**Методи фасилітації генерації ідей у командах в системі креативного менеджменту**

2026 · Актуальні питання економічних наук · article · uk · https://a-economics.com.ua/index.php/home/article/download/1392/1365

The article provides a systematic analysis of facilitation methods for idea generation in teams through the lens of creative management as a purposeful organizational management subsystem responsible for creating conditions, processes, and culture for systematic generation, selection, and implementation of ideas. The categorical framework of the study is defined: the concepts of creative management, facilitation, ideation, and team are delineated; demarcation between facilitation, moderation, coaching, and training as different roles of process support is established. Based on the 4P creativity model, the dynamic componential model, and the interactionist model, the place of ideation facilitation in the organizational creativity management system is substantiated. Cognitive and group mechanisms of idea generation are examined, including divergent thinking, associative theory, the SIAM model, as well as process losses of team interaction (production blocking, evaluation apprehension, social loafing, illusion of group productivity) and process gains (cognitive stimulation, synergy, building on ideas). A three-axis typology of facilitation methods by process phase, stimulation mechanism, and interaction structure is proposed. A critical analysis of key methods is conducted: brainstorming, brainwriting 6-3-5, SCAMPER, Design Thinking, LEGO Serious Play, World Café, nominal group technique, and AI-assisted ideation using large language models. Contextual factors of method effectiveness are identified: task type, team size and diversity, psychological safety level, facilitator competencies, physical and digital environment, and time pressure. An original five-stage "facilitation cycle" model (contracting, priming, divergence, convergence, reflection and handover) and a method selection matrix based on task type and team characteristics are developed. The specifics of applying facilitation methods in Ukrainian wartime conditions and necessity-driven innovation are substantiated.

**Решение:** -4 фасилитация генерации идей в командах, менеджмент

---

### 352 · R9176

**RETRACTED: Tracing interpersonal emotion regulation, behavioural emotion regulation strategies, hopelessness and vocabulary retention within Bing vs. ChatGPT environments**

2025 · British Educational Research Journal · journalarticle, article · en · https://doi.org/10.1002/berj.4137

Abstract Despite the growing integration of artificial intelligence (AI) in language education, limited research has explored its impact on emotional regulation and vocabulary retention, particularly in English as a foreign language (EFL) contexts. This study addressed this gap by comparing the effects of Bing and ChatGPT environments on interpersonal emotion regulation (IER), behavioural emotion regulation strategies (BERS), hopelessness and vocabulary retention among 458 upper‐intermediate Chinese EFL learners. Participants were divided into three groups: Bing, ChatGPT and a control group (CG) receiving traditional instruction. Both AI‐supported groups engaged with identical content and tasks on their respective platforms, while the CG followed a conventional curriculum. A mixed‐methods design was employed, incorporating quantitative pre‐ and post‐tests and qualitative semi‐structured interviews. The one‐way ANOVA results revealed that both AI groups significantly outperformed the CG across all measures, with no statistical difference between Bing and ChatGPT groups. The learners in AI‐supported conditions reported reduced hopelessness and improved IER and BERS, alongside notable vocabulary retention. In agreement with the quantitative results, the qualitative findings highlighted the engaging and supportive nature of AI environments, which led to improved IER, BERS and vocabulary retention and reduced hopelessness in the EFL learners. These results suggest that integrating AI tools like Bing and ChatGPT in EFL classrooms can enhance emotional well‐being and language acquisition, offering valuable pedagogical insights for educators seeking to leverage technology in language instruction.

**Решение:** -7 отозванная статья (RETRACTED), исследование изучения иностранного языка

---

### 353 · R9748

**Automating Thematic Review of Prevention of Future Deaths Reports: Replicating the ONS Child Suicide Study using Large Language Models**

2025 · arXiv.org · journalarticle, review · https://doi.org/10.48550/arxiv.2507.20786

Prevention of Future Deaths (PFD) reports, issued by coroners in England and Wales, flag systemic hazards that may lead to further loss of life. Analysis of these reports has previously been constrained by the manual effort required to identify and code relevant cases. In 2025, the Office for National Statistics (ONS) published a national thematic review of child-suicide PFD reports ($\leq$ 18 years), identifying 37 cases from January 2015 to November 2023 - a process based entirely on manual curation and coding. We evaluated whether a fully automated, open source"text-to-table"language-model pipeline (PFD Toolkit) could reproduce the ONS's identification and thematic analysis of child-suicide PFD reports, and assessed gains in efficiency and reliability. All 4,249 PFD reports published from July 2013 to November 2023 were processed via PFD Toolkit's large language model pipelines. Automated screening identified cases where the coroner attributed death to suicide in individuals aged 18 or younger, and eligible reports were coded for recipient category and 23 concern sub-themes, replicating the ONS coding frame. PFD Toolkit identified 72 child-suicide PFD reports - almost twice the ONS count. Three blinded clinicians adjudicated a stratified sample of 144 reports to validate the child-suicide screening. Against the post-consensus clinical annotations, the LLM-based workflow showed substantial to almost-perfect agreement (Cohen's $\kappa$ = 0.82, 95% CI: 0.66-0.98, raw agreement = 91%). The end-to-end script runtime was 8m 16s, transforming a process that previously took months into one that can be completed in minutes. This demonstrates that automated LLM analysis can reliably and efficiently replicate manual thematic reviews of coronial data, enabling scalable, reproducible, and timely insights for public health and safety. The PFD Toolkit is openly available for future research.

**Решение:** + T1/T3 тематический анализ коронерских отчетов о детских суицидах: LLM против консенсуса клиницистов, каппа 0.82

---

### 354 · R7619

**High Concordance Between GPT-4o and Multidisciplinary Tumor Board Decisions in Breast Cancer: A Retrospective Decision Support Analysis**

2025 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-6812005/v1

Abstract Background: Large language models (LLMs) such as ChatGPT have gained attention for their potential to assist clinical decision-making in oncology. However, real-world validation of these models against multidisciplinary tumor board (MTB) recommendations—particularly in breast cancer treatment—remains limited. Methods: This retrospective study assessed the concordance between GPT-4o and the decisions of a breast cancer MTB over a six-month period. Thirty-three patients were included. Structured clinical data were entered into GPT-4o using standardized prompts, and treatment plans were generated in two independent sessions per case. Seven therapeutic domains were evaluated: surgery, radiotherapy, hormonal therapy, neoadjuvant therapy, adjuvant therapy, genetic counseling/testing, and dual HER2-targeted therapy. Two blinded reviewers scored concordance using a 5-point Likert scale. Inter-rater reliability and classification metrics were calculated. Results: GPT-4o generated consistent recommendations across both sessions for all patients. Full concordance (5/5) with MTB decisions was observed in 31 of 33 cases (93.9%), while partial concordance (4/5) occurred in 2 cases (6.1%) due to differences regarding genetic counseling. Inter-rater agreement was perfect (Cohen’s kappa = 1.00), and the mean concordance score was 4.94 out of 5. The model achieved an overall accuracy of 93.9%, precision of 93.9%, recall of 100%, and F1 score of 96.8%. Conclusion: GPT-4o demonstrated a high level of agreement with expert multidisciplinary decisions in breast cancer care when provided with structured clinical input. These findings support its potential as a reproducible, guideline-consistent decision-support tool in oncology workflows.

**Решение:** -4 консилиум по опухолям, сравнение рекомендаций GPT-4o с онкологами

---

### 355 · R1224

**CueMem: Cue-Guided Context Reconstruction for Long-Term Conversational Memory**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.12354

Long-term conversational agents must answer user queries by recalling information from extended dialogue histories, yet directly using the full history is costly and often unreliable, while compressed memory units may lose fine-grained evidence needed for question answering. Motivated by the reconstructive view of autobiographical memory, we propose CueMem, a cue-guided framework that treats extracted memory records as retrieval cues rather than self-contained evidence and reconstructs query-relevant dialogue context from their source turns. During memory construction, CueMem extracts fine-grained memory cues from dialogue turns and links each cue to its source turn. At query time, it retrieves query-relevant cues, maps them to source-turn anchors, and expands from these anchors over a turn graph that captures temporal proximity and semantic relatedness, reconstructing a compact evidence context from the original dialogue for LLM answer generation. Experiments on LoCoMo and LongMemEval show that CueMem consistently outperforms representative long-term memory baselines. Further analyses show that graph-based context reconstruction helps recover supporting dialogue evidence while reducing query-time input tokens and latency compared with the full-history LLM setting. These results highlight retrieval cues as an effective alternative to self-contained memory evidence for long-term conversational question answering.

**Решение:** -4 архитектура долговременной диалоговой памяти (CueMem)

---

### 356 · R10657

**Aligning and comparing values of ChatGPT and human as learning facilitators: A value‐sensitive design approach**

2025 · British Journal of Educational Technology · journalarticle, article · en · https://doi.org/10.1111/bjet.13562

Ethical considerations have become a central topic in education since artificial intelligence (AI) brought both great innovation and challenges to educational practices and systems. Values influence what we believe is morally right and guide how we behave ethically in different situations. However, there is limited empirical research on improving the alignment between the values embedded in technology and the values prioritised by learners. Using the approach of value‐sensitive design (VSD), this study conducted an empirical investigation to explore: (1) how ethical values of learners regarding facilitators were characterised in the online learning environment, (2) how specific features of ChatGPT and human experts as online learning facilitators embody these values and (3) what value tensions occur in the online learning environment. In order to address the research questions, we designed a comparative experiment about online writing and revision facilitated by ChatGPT‐4 and a human expert. We conducted semi‐structured interviews with 59 learners about their learning experiences and feelings after completing the experiment. The results showed that learners prioritised the value of responsiveness, social comfort, autonomy, freedom from bias and privacy during online learning. Compared with the human expert, ChatGPT as a facilitator presented features of tirelessness, friendliness and support for independent decision‐making in embodying the value of social comfort and autonomy. However, ChatGPT struggled to interpret learners' intentions and emotions and posed risks of information leakage, thereby presenting a deficiency in embodying the value of responsiveness and privacy. Value tensions arose both within learners' groups and between learners and other stakeholders, including developers and researchers. These tensions emerged from conflicting ethical values and pragmatic considerations in the online learning environment. Our findings highlight the importance of enhancing value alignment in online learning environments. The strategies for achieving this include developing value‐sensitive AI, leveraging the strengths of AI tools in embodying specific values, and expanding VSD methodology in AI's entire life cycle. Practitioner notes What is already known about this topic Using ChatGPT as an online learning facilitator has been demonstrated to have various advantages, but its use also brings ethical challenges, particularly in aligning its features with the values of learners. Value‐sensitive design (VSD) helps improve value alignment by embedding the values of stakeholders into the technology design. However, the values of learners regarding facilitators in online learning environments remain under investigation. What this paper adds We conducted a comparative experiment to investigate the value characteristics of learners, compare embodied features of AI and human experts, and identify the potential tension of values. We found that learners prioritised the value of responsiveness, social comfort, autonomy, freedom from bias and privacy in the online learning environment. We found that ChatGPT has shown advantages in embodying specific values compared with the human expert, but value tensions and misalignment still emerged during online learning. We found that value tensions not only arose within learner groups but also between learners and other stakeholders, such as developers and researchers. Implications for practice and/or policy Educational technology developers should embed stakeholders' values in AI tools to enhance value alignment and seek a balance between their values and the values of the learners. Educators should actively utilise AI as a powerful tool and maximise its advantages in embodying specific values. Researchers should consider expanding VSD methods to the entire life cycle of AI tools to accommodate value dynamism.

**Решение:** -4 сопоставление ценностей ChatGPT и человека в образовательном процессе

---

### 357 · R1789

**Behavioral Empathy Classification in Dyadic Interactions Using Multimodal Cues**

2026 · IEEE Access · journalarticle, article · en · https://doi.org/10.1109/access.2026.3688143

Empathy in human–human interactions encompasses nonverbal behaviors that are often overlooked by state-of-the-art empathic perception models, despite extensive progress in the text domain. In this article, we investigate empathy classification in dyadic interactions using audiovisual data, specifically arousal and valence values extracted from facial expressions, head gestures, and textual content derived from speech. We propose a novel cue integration framework that augments precomputed text-based features with video-derived emotional cues and applies them to a pattern-based empathy classifier. Furthermore, we introduce a ranking module that provides interpretability by revealing the relative influence of empathy cues. Our approach is evaluated in two distinct settings: a controlled laboratory environment in which multiple pairs of participants engage in face-to-face conversation, and a real-world school setting involving group interactions among children. Results show that our multimodal empathy classifier generalizes better than deep learning baselines and on par with state-of-the-art large language models across both dyadic and group interaction scenarios, without requiring retraining.

**Решение:** -5 мультимодальная классификация поведенческой эмпатии без генеративных LLM

---

### 358 · R10494

**Generalization Evaluation of Deep Stereo Matching Methods for UAV-Based Forestry Applications**

2025 · arXiv (Cornell University) · conferencepaper/, journalarticle, preprint/article · https://doi.org/10.48550/arxiv.2512.03427

Autonomous UAV forestry operations require robust depth estimation methods with strong cross-domain generalization. However, existing evaluations focus on urban and indoor scenarios, leaving a critical gap for specialized vegetation-dense environments. We present the first systematic zero-shot evaluation of eight state-of-the-art stereo methods--RAFT-Stereo, IGEV, IGEV++, BridgeDepth, StereoAnywhere, DEFOM (plus baseline methods ACVNet, PSMNet, TCstereo)--spanning iterative refinement, foundation model, and zero-shot adaptation paradigms. All methods are trained exclusively on Scene Flow and evaluated without fine-tuning on four standard benchmarks (ETH3D, KITTI 2012/2015, Middlebury) plus a novel 5,313-pair Canterbury forestry dataset captured with ZED Mini camera (1920x1080). Performance reveals scene-dependent patterns: foundation models excel on structured scenes (BridgeDepth: 0.23 px on ETH3D, 0.83-1.07 px on KITTI; DEFOM: 0.35-4.65 px across benchmarks), while iterative methods maintain cross-domain robustness (IGEV++: 0.36-6.77 px; IGEV: 0.33-21.91 px). Critical finding: RAFT-Stereo exhibits catastrophic ETH3D failure (26.23 px EPE, 98 percent error rate) due to negative disparity predictions, while performing normally on KITTI (0.90-1.11 px). Qualitative evaluation on Canterbury forestry dataset identifies DEFOM as the optimal gold-standard baseline for vegetation depth estimation, exhibiting superior depth smoothness, occlusion handling, and cross-domain consistency compared to IGEV++, despite IGEV++'s finer detail preservation.

**Решение:** -4 стереозрение для автономных дронов в лесном хозяйстве

---

### 359 · R1301

**Integrating Large Language Models into Citizen Science data for Equitable and Sustainable Well-being**

2026 · Proceedings of the 2026 International Conference on Information Technology for Social Good · book, conference · https://doi.org/10.1145/3794786.3830770

Urban equitable and sustainable well-being is a fundamentally subjective and context-dependent construct, typically requiring direct citizen participation to be meaningfully captured. However, in large-scale and spatially distributed urban environments, continuous citizen engagement in data collection and annotation is difficult to sustain. This paper investigates whether Large Language Models (LLMs) can partially substitute citizens in the interpretation of urban well-being signals derived from visual data. A setting in which citizen-captured images are used as proxies for lived urban experience is investigated. The central question is whether LLMs, relying on pre-trained knowledge without explicit local or domain-specific adaptation, can reliably infer well-being or non-wellbeing indicators from such data, despite lacking direct contextual awareness of the city. We propose framing LLMs as surrogate interpreters in citizen science pipelines, where they generate semantic labels for urban scenes and act as computational proxies for human perception. Their outputs are evaluated against human annotations, using agreement measures such as matching rate and Cohen’s Kappa, and further explored through LLM-as-a-judge setups. This research argues that this paradigm raises a critical tension between scalability and contextual fidelity: while LLMs may enable large-scale, low-participation sensing of urban well-being, their ability to meaningfully replace citizen interpretation remains an open question. Ultimately, we discuss whether LLMs can serve not as full substitutes for citizens, but as complementary agents in the mediation between visual urban data and subjective well-being evaluation in smart city decision-making.

**Решение:** -4 оценка субъективного благополучия городской среды по фотографиям улиц

---

### 360 · R7224

**Embedding-Based Acronym Disambiguation Supported by Large Language Models in German Clinical Narratives**

2025 · SLM4Health@AIME · journalarticle

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 разрешение неоднозначности аббревиатур с помощью эмбеддингов и LLM

---

### 361 · R10913

**Harnessing Empathy and Ethics for Relevance Detection and Information Categorization in Climate and COVID-19 Tweets**

2024 · ACM International Conference on Information and Knowledge Management (CIKM) · journalarticle, book, conference · en · https://doi.org/10.1145/3627673.3679937

In this work, we aim to understand the general public perception of societal issues related to the current climate crisis and the COVID-19 pandemic on Twitter (X). Social media discussions on such matters often lead to misleading information, resulting in delays in initiatives proposed by governments or policymakers. Hence, we focus on extracting relevant information from the conversations on climate change and COVID that could be useful for authorities to curb the spread of potentially biased information by proposing the classification tasks of relevance detection (RD) and information categorization (IC). We first curate the datasets for the RD and IC tasks for the climate domain and extend the COVID-19 benchmark attention-worthy Twitter dataset for the IC task through manual annotation. We initially conduct experiments with LLMs and observe that LLMs can extract the relevant information in zero and few-shot settings based on multi-perspective reasoning in the form of cognitive empathy and ethical standards, but still perform worse than fine-tuned small language models. Based on the initial findings, we conclude that LLMs may not be the best extractor of relevant information, but induce cognitive empathy and ethical reasonings that can intuitively guide supervised models. To achieve this idea, we develop a cognitive empathy and ethical reasoning-based multi-tasking pipelined network for RD and IC tasks. Our proposed approach provides valuable insights that could be useful in real-world scenarios for governments, policymakers, and other researchers to decode the overall public outlook on societal issues.

**Решение:** -4 анализ восприятия общественных проблем в социальных сетях

---

### 362 · R8593

**A06 Utilizing point-of-care informed feature organization and multimodality information integration to develop artificial intelligence systems for effective blood transfusion triage**

2025 · BMJ Military Health · journalarticle, conference-abstract · en · https://doi.org/10.1136/bmjmilitary-2025-nato.6

Background Massive haemorrhage remains a leading cause of preventable mortality on the battlefield. 1 Timely and effective decision-making around blood transfusion across various points of care is complex and often suboptimal, leading to avoidable patient deterioration. Artificial intelligence and machine learning (AI/ML) approaches offer significant potential for improving triage accuracy and optimizing blood resource allocation. 2 3 This preliminary study introduces a point-of-care informed clinical feature organization and multimodality information integration framework to identify key predictive features and develop initial ML models. The overarching goal is to lay the foundation for an AI-assisted transfusion triage system that enhances both efficiency and outcomes. Methods A retrospective dataset from the Ontario Trauma Registry was utilized, comprising 73,117 trauma patients and 604 multimodal clinical features, stratified into pre-hospital (31 features) and in-hospital (104 features) phases of care. Two working, outcome-balanced datasets (each >3,000 samples) were created for separate phase-specific analyses. A comprehensive data pre-processing strategy was implemented. The CV-rRF-FS-SVM (cross validation with recursive random forest and support vector machine) algorithm was applied via NMT (Neural ML Tools) toolkit for feature selection, with transfusion status as the outcome variable. 4–6 SVM was then employed to develop preliminary transfusion triage models. Further, explainable AI method SHAP (SHapley Additive exPlanations) analysis was applied for better model and individual inference interpretation. Additionally, an AI-powered Large Language Model (LLM) framework, termed ‘DefencePT’, was established to analyse open-ended language data within the dataset, enabling topic extraction and more comprehensive data exploitation. Results In the pre-hospital phase, 10 selected critical predictors included heart rate at the scene and primary injury type. The SVM model achieved an ROC-AUC of 0.82 on a 20% holdout test set (figure 1A). For the in-hospital analysis, 21 key features were identified, including heart rate, temperature, injury type, and systolic blood pressure, with a resulting ROC-AUC of 0.88 (figure 1B). The SHAP results suggested that the preliminary models can be explained, on both the model- and individual-levels. The DefencePT LLM framework revealed previously unstructured insights, such as associations between injury types and age demographics, offering early evidence to better understand preventable haemorrhage cases and improve blood resource management strategies. Conclusions By implementing a point-of-care informed feature organization and multimodality integration strategy, our machine learning analysis has effectively identified key determinants in blood transfusion triage in both pre-hospital and in-hospital trauma care settings. This approach uncovers subtle patterns and trends that are not readily observable through traditional methods, offering potential to enhance blood transfusion protocols and practices. The LLM-powered framework demonstrated promise in extracting actionable insights from unstructured data, potentially improving triage model performance and informing strategies to reduce preventable battlefield mortality. Collectively, these preliminary findings underscore the transformative potential of AI/ML in advancing transfusion triage practices both on and off the battlefield. Abstract A06 Figure 1 ROC-AUC results on 20% holdout test data on the preliminary transfusion triage models: (A) pre-hospital model, (B) in-hospital model Conflict of Interest Authors declare no conflict of interest. References Alam HB, Burris D, DaCorta JA, Rhee P. Hemorrhage control in the battlefield: role of new hemostatic agents. Mil Med . 2005; 170 (1):63–9. Anstey C, Ullman D, Su L, Su C, Siniard C, Simmons S, et al . The practical use of artificial intelligence in transfusion medicine and apheresis. Transfus Apher Sci . 2024; 63 (6):104001. Peng HT, Siddiqui MM, Rhind SG, Zhang J, da Luz LT, Beckett A. Artificial intelligence and machine learning for hemorrhagic trauma care. Military Medical Research . 2023; 10 (1):6. Zhang J, Wong SM, Richardson JD, Jetly R, Dunkley BT. Predicting PTSD severity using longitudinal magnetoencephalography with a multi-step learning framework. Journal of neural engineering . 2020; 17 (6). Zhang J, Richardson JD, Dunkley BT. Classifying post-traumatic stress disorder using the magnetoencephalographic connectome and machine learning. Scientific Reports . 2020; 10 (1):5937. Zhang J, Hadj-Moussa H, Storey KB. Current progress of high-throughput microRNA differential expression analysis and random forest gene selection for model and non-model systems: an R implementation. Journal of integrative bioinformatics . 2016; 13 :306.

**Решение:** -4 организация данных при массивных кровотечениях, военно-полевая хирургия

---

### 363 · R5218

**The Automation Efficiency Paradox: Why Generative AI Increases the Need for Human Expertise**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.20747027

Organizations are rapidly adopting Large Language Models (LLMs) under the assumption that automation can seamlessly replace human labor to maximize operational speed (Srinivasan, 2026). This paper introduces the Automation Efficiency Paradox to challenge this assumption using a behavioral and cognitive framework (Bashkirova & Krpan, 2024). We demonstrate that because conversational AI operates on probabilistic next-token predictions and alignment optimization (sycophancy), its outputs suffer from Psychological Invisibility and Deceptive Syntheses (Anthropic, 2023; Perez et al., 2022). Rather than eliminating human error, the system camouflages omissions behind masterfully crafted, fluid prose (Srinivasan, 2026). When scaling tasks to large, macro-level text blocks, human operators experience cognitive fatigue and cave to premature verification convergence, unthinkingly accepting flawed data (Elsevier B.V., 2026). We argue that blindly replacing human workers with AI leads to a downstream collapse of trust in the system's output (Bashkirova & Krpan, 2024). To preserve workflow integrity, AI cannot function as a standalone replacement (Srinivasan, 2026). Instead, the technology fundamentally increases the societal necessity for high-level, subject-matter human experts who possess the structural capacity to audit, verify, and guide algorithmic outputs at the source (Chen et al., 2025; Elsevier B.V., 2026).

**Решение:** -4 парадокс эффективности автоматизации в организациях, менеджмент

---

### 364 · R1502

**How Do You Measure an LLM's "Soul"?**

2026 · Zenodo (CERN European Organization for Nuclear Research) · audiovisual/, other · en · https://doi.org/10.5281/zenodo.19422219

Episode summary: We all know how to test if an LLM solves a math problem, but how do you measure if it has the right "soul"? This episode tackles the messy world of qualitative AI evaluation. We explore why binary benchmarks fail for real-world tasks like medical summaries or creative writing, and dive into techniques like LLM-as-a-Judge, G-Eval, and counterfactual testing to map a model's hidden worldview. Learn how to build a "Golden Dataset" and avoid the pitfalls of subjective bias. Show Notes **Beyond Binary Benchmarks: Measuring the "Soul" of AI Output** When we evaluate AI models, we often rely on simple, objective metrics. Can the model solve a math problem? Does it know that 2+2 equals 4? These are binary, right-or-wrong questions, and they're easy to test. But they miss the reality of how most people actually use Large Language Models. We aren't asking them to solve the Riemann Hypothesis; we're asking them to draft an email, rewrite a medical summary for a scared patient, or act as a creative partner in a writers' room. In these scenarios, there is no single "correct" answer—only better or worse outcomes based on invisible criteria like tone, style, and empathy. **The Limits of Traditional Metrics** The core problem is that traditional benchmarks like MMLU or GSM8K simply shrug at qualitative assessment. A model can be factually accurate but a total failure in communication. For instance, a medical summary that reads, "Neoplasm confirmed, Stage III, suggest immediate aggressive intervention," is technically correct but unhelpful to a terrified human. A better model would phrase it as, "The tests confirmed a serious growth, and we need to start treatment quickly." The difference isn't factual accuracy; it's communicative success. Despite this, a 2024 study from Stanford's Institute for Human-Centered AI found that roughly 70% of LLM evaluations still rely on those simple binary metrics, leaving a massive gap between how models are tested and how they're actually used. **New Frameworks for Subjective Evaluation** To bridge this gap, we need frameworks that can handle subjectivity. One promising approach is "LLM-as-a-Judge," where a more powerful model (like GPT-4o or Claude 3.5 Sonnet) evaluates the output of a smaller, specialized model. While this risks "self-preference bias"—where a model favors its own style—it can yield surprisingly consistent results when structured correctly. The key is a framework called **G-Eval**, which uses Chain-of-Thought reasoning. Instead of just asking for a score, the judge model is prompted to first define the evaluation criteria (e.g., coherence, tone), then generate a step-by-step reasoning process for its rating, and finally assign a weighted score. This forces the model to "show its work," much like a gymnastics judge explaining deductions, which significantly increases correlation with human judgment. **Mapping a Model's Hidden Worldview** For even thornier issues like cultural bias or political framing, researchers are turning to **Counterfactual Evaluation**. This technique involves running the same prompt with only a single variable changed—such as a name—to see if the model's output shifts. For example, prompting a model to write about a successful CEO named "John" versus "Fatima" can reveal hidden stereotypes if the personality or setting changes. This acts as a controlled experiment for stereotypes. Researchers are even using surveys like the World Values Survey to map a model's "worldview," checking if it leans toward Western individualism or other cultural frameworks. This is critical for applications like mental health support, where an American-centric model emphasizing "self-actualization" might be culturally offensive in a context that values "harmony" and "social obligation." **Practical Tools for Builders** For teams building custom evaluation suites, the most practical takeaway is to use a structured rubric. Instead of a vague "Is this good?", break evaluation down into specific, one-to-five scales for dimensions like "Faithfulness," "Criticality" (highlighting key risks), and "Accessibility" (understandable to non-experts). To ensure consistency, use **few-shot grading**, providing the judge model with examples of what a 1, 3, and 5 look like for each criterion. This avoids the "Consistency Check" problem where a judge gives wildly different scores to the same text. Another powerful tool is **Comparative Ranking**, or A/B testing, where humans are shown two AI outputs and asked which is better for a specific purpose. This can generate an Elo rating for models within a specialized domain, like "Medical Empathy" or "Noir Writing Style." Interestingly, models that top objective math benchmarks often lose these "vibe tournaments," revealing a massive blind spot in traditional evaluation. By combining these techniques—LLM-as-a-Judge with G-Eval, counterfactual testing, structured rubrics, and human comparison—builders can move beyond "vibes-only" approaches and create models that are not just smart, but truly effective in the real world. Listen online: https://myweirdprompts.com/episode/measuring-llm-qualitative-benchmarks My Weird Prompts is an AI-generated podcast. Episodes are produced using an automated pipeline: voice prompt → transcription → script generation → text-to-speech → audio assembly. Archived here for long-term preservation. AI CONTENT DISCLAIMER: This episode is entirely AI-generated. The script, dialogue, voices, and audio are produced by AI systems. While the pipeline includes fact-checking, content may contain errors or inaccuracies. Verify any claims independently.

**Решение:** -1 подкаст об измерении личности и возможностей LLM

---

### 365 · R5585

**Scale: Scaling Qualitative Data Coding With LLMs**

2026 · TUbilio (Technical University of Darmstadt) · conference-paper · en · https://aisel.aisnet.org/context/ecis2026/article/1224/viewcontent/1203_doc.pdf

Large Language Models (LLMs) are transforming research practices in Information Systems (IS), offering new opportunities for qualitative data analysis. While recent studies show that LLM-assisted coding can achieve human-comparable accuracy, challenges such as hallucinations, inconsistency, and limited methodological guidance remain. To address these issues, we propose SCALE, a structured framework for scaling qualitative data coding. SCALE integrates human implicit understanding into LLM-assisted coding and scales it. Additionally, it establishes systematic validation across the entire coding process. SCALE introduces steps for rigorous project design, gold-standard creation, iterative prompt refinement, and multi-stage validation. Through this approach, SCALE balances scalability with reliability, enabling researchers to conduct large-scale qualitative analyses efficiently. Our evaluation shows that structured processes can align LLM outputs with human coding while reducing manual effort, contributing to a more robust methodological foundation for artificial intelligence (AI)-assisted qualitative research in IS.

**Решение:** -4 фреймворк SCALE для качественного кодирования в информационных системах

---

### 366 · R5207

**Generative artificial intelligence as digital therapy: what do we know and how can we make it better?**

2026 · BJPsych Advances · journalarticle, article · en · https://doi.org/10.1192/bja.2025.10193

SUMMARY Generative artificial intelligence (GenAI) shows promise for mental healthcare by increasing access to treatment. In this article, we analyse recent evidence on the use of GenAI chatbots as a treatment for common mental disorders. We examine key ethical and methodological considerations and discuss the specific risks for delusions. Adopting a precision psychiatry perspective, we propose that the therapeutic alliance can be improved by tailoring GenAI to mimic a user’s psychological traits, a version of socioaffective alignment.

**Решение:** -1 обзор и аналитическая статья о генеративном ИИ в цифровой терапии

---

### 367 · R11791

**Trainee Focus debate: Artificial intelligence will have a positive impact on emergency medicine**

2024 · Emergency Medicine Australasia · article · en · https://doi.org/10.1111/1742-6723.14458

Artificial intelligence (AI) and machine learning (ML) is a rapidly expanding technological field that presents great potential for EM and will infiltrate many facets of our future practice. This article outlines the positive arguments for the use of AI tools in EM. In order to benefit from AI, we need to understand the current capabilities. Narrow AI is the iteration that is being implemented in the current medical landscape. This requires AI tools to be trained on large data sets and can be used for automating the manual processing of writing content. It can also be used to summarise complex data into coherent narrative structures. Well-known general examples include: Amazon's Alexa and Apple's Siri. General AI is a more advanced theoretical form of AI.1 The clinical applications of AI tools are broad and include documentation, patient flow, diagnostics, point-of-care ultrasound (POCUS) applications and clinical decision-making. Clinical documentation comprises a large proportion of EM shifts, with clinicians spending approximately 43% of their shift on data entry.2 Streamlining and automation of documentation would allow clinicians to focus their time on clinical interactions, reducing documentation burden, and improving documentation quality. The majority of our clinical AI research comes from radiological studies. Computer vision ML can be trained to recognise radiological pathology, with computer-aided detection and diagnostic systems assisting the identification of abnormalities in imaging studies.3 One study showed that generative AI was able to produce radiology reports of similar clinical accuracy to in-house radiology reports.4 This has the potential to identify abnormalities sooner, improve accuracy, and expedite patient disposition. POCUS has already been revolutionary for EM. In 2020, the Food and Drug Administration approved an echocardiography software algorithm that uses ML to calculate the ejection fraction from auto-captured 3D video clips. It also uses ML software to assist in obtaining the optimal images. The estimates of ejection fraction agreed with human experts.5 Similar technology will help EM clinicians obtain high-quality POCUS images at the bedside, along with accurate interpretation. Inefficiencies of patient flow lead to poor patient outcomes. AI tools have the capacity to incorporate large volumes of data in real time augmenting patient flow. These combined elements will greatly increase patient time-to-diagnosis, disposition and clinician satisfaction. AI tools have been shown to triage ED patients more accurately than current common triage tools.6 Generative AI tools such as Chat GPT could be used to write practice questions for exams and generate large question banks that trainees can use to hone their exam technique. Generative AI could be used as a training assistant to help mentor students and provide more bespoke teaching feedback. Generative AI could also be used to synthesise large volumes of textbook information into more understandable and applicable content. AI tools have been used to produce virtual simulations for surgical training, improving surgical technical skills.7 This can be applied to high acuity, low occurrence procedures or situations in an EM context, allowing trainees to get regular exposure and develop competence. This technology could also be extended to help trainees navigate and simulate difficult communication scenarios. Clinical training requires extensive time, emotion and energy from trainees. The majority of doctors balance both clinical and personal lives alongside exams. AI tools have the potential to make this process more manageable, enjoyable and reduce clinician burnout. Indigenous health is an integral part of our clinical practice in Australasia; however, we still have a long way to go before equity is achieved. Current early evidence suggests AI tools are able to enhance equity by reducing the effect of human bias on care, lowering barriers to knowledge, and increasing the productivity of healthcare professionals.6 Data sovereignty refers to the rights and interests of an individual group in the collection, ownership, and application of their data. If systems are designed with First Nations and Māori involvement, then data sovereignty and equity will likely be achieved. With the use of the correct training data for generative AI systems we can ensure that AI systems are more equitable. AI can be used to assist in ethical and patient-centred decision-making. One study found that AI-initiated palliative care decisions were associated with a lower hospital readmission rate, and a higher referral rate to palliative care.8 This highlights that AI tools can be beneficial in facilitating difficult decision-making while working with patients. At the time of writing, both Australia and Aotearoa New Zealand have no specific laws relating to AI in a medico-legal context. However, the frameworks they do have in place provide a reasonable starting point. In both countries, governments and medical organisations are taking notice and recognising the need for AI governance. The most relevant legal frameworks in place in both countries are their respective Privacy Acts. They define how personal data is collected, used, stored and distributed. In Aotearoa New Zealand, the Privacy Commissioner has issued guidance for the use of generative AI.9 Specifically, they mention engagement with Māori about the potential impacts of generative AI. The federal government in Australia is seeking to amend the 1988 Privacy Act so that individuals will have the right to request meaningful information about how automated decisions are generated.10 Any technology that can allow us to document more succinctly and accurately will be beneficial from a medico-legal perspective. In reality it is unlikely AI tools will be implemented into common clinical practice or public hospitals until relevant regulation and legal protections exist. Decisions made usi

**Решение:** -1 дискуссионная статья о роли искусственного интеллекта в психиатрии

---

### 368 · R11266

**Language sentiment predicts changes in depressive symptoms.**

2024 · Proceedings of the National Academy of Sciences of the United States of America · journal article, research support, n.i.h., extramural, article · eng · https://doi.org/10.1073/pnas.2321321121

The prevalence of depression is a major societal health concern, and there is an ongoing need to develop tools that predict who will become depressed. Past research suggests that depression changes the language we use, but it is unclear whether language is predictive of worsening symptoms. Here, we test whether the sentiment of brief written linguistic responses predicts changes in depression. Across two studies ( N = 467), participants provided responses to neutral open-ended questions, narrating aspects of their lives relevant to depression (e.g., mood, motivation, sleep). Participants also completed the Patient Health Questionnaire (PHQ-9) to assess depressive symptoms and a risky decision-making task with periodic measurements of momentary happiness to quantify mood dynamics. The sentiment of written responses was evaluated by human raters ( N = 470), Large Language Models (LLMs; ChatGPT 3.5 and 4.0), and the Linguistic Inquiry and Word Count (LIWC) tool. We found that language sentiment evaluated by human raters and LLMs, but not LIWC, predicted changes in depressive symptoms at a three-week follow-up. Using computational modeling, we found that language sentiment was associated with current mood, but language sentiment predicted symptom changes even after controlling for current mood. In summary, we demonstrate a scalable tool that combines brief written responses with sentiment analysis by AI tools that matches human performance in the prediction of future psychiatric symptoms.

**Решение:** + T1 анализ тональности письменных ответов для предсказания депрессии: ChatGPT против 470 экспертов-людей

---

### 369 · R1979

**Large language models and multimodal AI for mental health: a systematic review of early diagnosis and monitoring**

2026 · Artificial Intelligence Review · article · en · https://doi.org/10.1007/s10462-026-11649-9

Mental health disorders (e.g., depression, anxiety, post-traumatic stress disorder (PTSD), bipolar disorder) represent a pressing global challenge, and early diagnosis with continuous monitoring is critical for effective intervention. However, traditional diagnostic methods, relying on patient self-reports and clinical interviews, are subjective and often miss subtle early warning signs, a problem compounded by stigma and limited access to care. In response, recent advances in artificial intelligence, particularly large language models (LLMs) and multimodal learning techniques, may support mental-health screening, monitoring, and decision support by enabling scalable, data-driven, and personalized analysis of various behavioral and physiological signals. This review provides a comprehensive integration of current LLM-based and multimodal approaches for early mental health diagnosis and monitoring. We examine key AI frameworks and their architectures, highlighting how they integrate modalities such as text, speech, neuroimaging, and physiological data through various fusion strategies (early, late, hybrid, and cross-attention) to improve predictive accuracy. In addition, we critically discuss the technical, ethical, and clinical challenges, such as model hallucinations, algorithmic bias, interpretability limitations, and privacy concerns, that must be addressed to translate these technologies into reliable clinical tools. Finally, we outline open challenges and future research directions aimed at guiding researchers, clinicians, and developers in advancing responsible, human-centered AI systems for mental health care.

**Решение:** -1 систематический обзор применения LLM и мультимодального ИИ в психическом здоровье

---

### 370 · R2414

**Utilizing Large Language Models to Enhance Patient-Reported Outcome Measures: Application to the EQ-5D-5L and Bolt-Ons.**

2026 · Value in health : the journal of the International Society for Pharmacoeconomics and Outcomes Research · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.jval.2026.06.021

OBJECTIVES: Large language models (LLMs) may be useful tools for the development/adaptation of patient-reported outcome measures. As a methodological proof-of-concept, we evaluated the use of LLMs to support the identification of potential EuroQol 5-Dimension 5-Level (EQ-5D-5L) bolt-on dimensions, using patient-reported free-text data. METHODS: We used GPT-4o to analyze text data from 1977 members of the Dutch Celiac Association, who completed the EQ-5D-5L and narratively described the impact of celiac disease on their lives. Prompts were designed to identify potential EQ-5D-5L bolt-on dimensions and produce preliminary item wordings for selected dimensions. Evaluations comprised comparisons of dimensions identified using 2 alternative approaches (qualitative analysis and topic modeling) conducted on a subset of 85 text entries, text-entry level agreement (Kappa) between LLM and qualitatively identified dimensions, and suitability of LLM-generated item wordings assessed against existing criteria. RESULTS: The LLM identified 12 potential bolt-on dimensions to the EQ-5D-5L, of which 9 were also identified using qualitative analysis, and 5 using topic modeling. Text-entry-level agreement between the LLM and qualitative approaches was "moderate," "substantial," or "almost perfect," with 2 exceptions of slight/fair agreement (median Kappa = 0.68, IQR = 0.56-0.76). Sensitivity analyses using 4 other LLMs produced similar agreement results. The LLM-generated item wordings for the 4 most common dimensions scored 4.0 to 4.4 out of 5 when assessed against existing criteria. CONCLUSIONS: This study demonstrates the potential of LLMs to support the development/modification of patient-reported outcome measures based on patient-reported text data. Further research should assess the approach's transferability across disease areas and data sources, while better incorporating patient/stakeholder input throughout.

**Решение:** ? разработка шкал качества жизни EQ-5D по текстам пациентов; проверить конструкт в полном тексте

---

### 371 · R6375

**MetaMate: Understanding How Educational Researchers Experience AI-Assisted Data Extraction for Systematic Reviews**

2026 · Extended Abstracts of the CHI Conference on Human Factors in Computing Systems (CHI EA) · book, journalarticle, review · https://doi.org/10.1145/3772363.3798755

Systematic reviews are essential for evidence synthesis in education, yet data extraction remains a bottleneck: labor-intensive and error-prone. Large language models offer automation potential, but questions remain about AI performance compared to human coders and how researchers experience these tools in practice. We present MetaMate, an open-access web-based tool for automated data extraction in educational systematic reviews. Our mixed-methods evaluation combines a quantitative validation study benchmarking MetaMate against trained human coders across 32 studies and 20 data elements with a qualitative user study involving six educational researchers using think-aloud protocols. MetaMate achieves precision (81–96%), recall (90–100%), and F1 scores (88–96%) comparable to or exceeding human coders, with strengths in mathematical reasoning and semantic comprehension. Qualitative findings reveal insights about trust calibration, verification behaviors, usability challenges, and human-AI collaboration. We contribute empirical evidence on LLM extraction capabilities and design implications for AI-assisted research tools balancing automation with human oversight. MetaMate is available at https://metamate.online.

**Решение:** -6 инструмент экстракции данных MetaMate для систематических обзоров в образовании

---

### 372 · R12732

**Why So Toxic?**

2022 · ACM SIGSAC Conference on Computer and Communications Security (CCS) · book, journalarticle, conference · en · https://doi.org/10.1145/3548606.3560599

Chatbots are used in many applications, e.g., automated agents, smart home assistants, interactive characters in online games, etc. Therefore, it is crucial to ensure they do not behave in undesired manners, providing offensive or toxic responses to users. This is not a trivial task as state-of-the-art chatbot models are trained on large, public datasets openly collected from the Internet. This paper presents a first-of-its-kind, large-scale measurement of toxicity in chatbots. We show that publicly available chatbots are prone to providing toxic responses when fed toxic queries. Even more worryingly, some non-toxic queries can trigger toxic responses too. We then set out to design and experiment with an attack, ToxicBuddy, which relies on fine-tuning GPT-2 to generate non-toxic queries that make chatbots respond in a toxic manner. Our extensive experimental evaluation demonstrates that our attack is effective against public chatbot models and outperforms manually-crafted malicious queries proposed by previous work. We also evaluate three defense mechanisms against ToxicBuddy, showing that they either reduce the attack performance at the cost of affecting the chatbot's utility or are only effective at mitigating a portion of the attack. This highlights the need for more research from the computer security and online safety communities to ensure that chatbot models do not hurt their users. Overall, we are confident that ToxicBuddy can be used as an auditing tool and that our work will pave the way toward designing more effective defenses for chatbot safety.

**Решение:** -4 токсичность диалоговых агентов и методы ее снижения

---

### 373 · R10794

**Comparing Human and Generative AI Analysis of Emotions in U.S. Abortion Tweets**

2025 · Researching Generative AI in Applied Linguistics · book-chapter · en · https://doi.org/10.31274/isudp.2025.211.13

This study investigates the use of ChatGPT-4o to analyze contributors’ emotions and stances regarding abortion as expressed in U.S. abortion-related tweets. The study compared two human analysts’ and ChatGPT’s coding of a dataset of 100 tweets from Boston, Massachusetts, collected between September 2022 and January 2023. Codes for affect were defined based on Martin and White’s (2005) Appraisal Framework, focusing on the AFFECT subcategory to identify positive, negative, and neutral emotions, and stance codes were defined using Du Bois’ (2007) stance-taking analysis to classify pro-abortion, anti-abortion, or neutral stances. The motivation for this research stems from the challenges inherent in human coding of expressions of subjectivity including its time-consuming nature, low interrater reliability, and potential biases arising from factors like insufficient coder training, varying familiarity with the cultural context, and effects stemming from differences in coders’ gender identities. By exploring the efficacy of ChatGPT in analyzing emotional content, this study aimed to assess the potential of GenAI tools to support discourse analysis of social media. Findings reveal only fair agreement in emotion classification (Kappa=0.355 between Human 1 and Human 2, Kappa=0.283 between Human 1 and ChatGPT, and Kappa=0.322 between Human 2 and ChatGPT) and in stance classification (Kappa=0.402 between Human 1 and Human 2, Kappa=0.283 between Human 1 and ChatGPT and Kappa=0.468 between Human 2 and ChatGPT). Overall reliability across coders, as measured by Krippendorff’s Alpha, was also low (Alpha=0.319), further underscoring the challenges of achieving high consistency in subjective coding tasks such as emotion and stance analysis. Chi-square analysis further highlights a significant difference in how ChatGPT and human coders categorized emotions (positive, negative, and neutral) in abortion tweets. These results provide valuable insights into the capabilities and limitations of ChatGPT-4o in analyzing subjectivity in social media content, particularly within the polarizing content of abortion discourse.

**Решение:** -4 анализ политической позиции и эмоций в твитах об абортах, политология

---

### 374 · R5135

**Detecting Experiential Intertextuality Across Migration Routes: Beyond Surface Similarity in French Narratives**

2026 · Annual Meeting of the Special Interest Group on Discourse and Dialogue · preprint/article, conference-paper, preprint · https://doi.org/10.18653/v1/2026.sigdial-1.10

Migrants traversing geographically distinct routes such as the Trans-Saharan and Balkan corridors often recount strikingly parallel lived experiences: police violence, smuggler exploitation, dangerous crossings, and family separation. We introduce the task of experiential intertextuality detection: automatically identifying shared experiential echoes across migration narratives without requiring annotated training data. From 108 French migration narratives spanning both corridors, we automatically generate sentence pairs and score them using annotation-free methods: lexical baselines, sentence embeddings, POS-based structural features, a migration-specific theme lexicon, context-aware narrative features, and zero-shot LLM scoring with Qwen2.5-7B and Mistral-7B under three prompting strategies. We validate all methods against 816 expert-annotated intertextuality judgments (inter-annotator Krippendorff's $α= 0.27$). Our results reveal that all surface, structural, and embedding methods correlate only weakly with expert judgments ($r \leq 0.30$); Qwen2.5-7B zero-shot achieves the best single-method correlation ($r = 0.38$); few-shot examples degrade Qwen but dramatically improve Mistral; narrative position significantly predicts intertextuality, with departure-phase pairs showing the highest experiential echoes; and a supervised hybrid combining all 31 features achieves $r = 0.45$, a 21% improvement over the best individual method. 11 pages, 3 figures, 5 tables. Accepted at SIGDIAL 2026 (27th Annual Meeting of the Special Interest Group on Discourse and Dialogue)

**Решение:** -4 социологический анализ опыта мигрантов на транссахарском и балканском маршрутах

---

### 375 · R1378

**Psychedelics, the media portrayal and large-language model evaluations.**

2026 · BJPsych open · journal article, journalarticle, article · eng · https://doi.org/10.1192/bjo.2026.12025

Summary Psychedelics were used for centuries in healing and spiritual rituals, long before the mid-20th century when they became subjects of biomedical research. Although initial trials generated optimism, these were quickly overshadowed by sensationalist media coverage and political backlash. Following decades of inactivity, research on compounds including 3,4-methylenedioxymethamphetamine (MDMA) has resurged, along with the media attention. Investigating this growing interest, Bender et al employed a large-language model, validated against human raters, to analyse 25 years of media articles (2000–2025), quantifying trends in sentiment towards psychedelic therapies. Findings showed a dramatic increase in coverage, with positive sentiment peaking in 2020 followed by a significant decline from 2024, coinciding with the U.S. Food and Drug Administration’s decision not to approve MDMA-assisted therapy for post-traumatic stress disorder, and echoing the dynamics of the 1960s. The authors emphasise that sustained progress in the field will require reliance on scientific evidence to advance therapeutic applications.

**Решение:** -4 репрезентация психоделиков в средствах массовой информации

---

### 376 · R12678

**What Do Code Models Memorize? An Empirical Study on Large Language Models of Code**

2023 · arXiv.org · journalarticle · https://doi.org/10.48550/arxiv.2308.09932

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 исследование запоминания обучающего кода моделями программирования

---

### 377 · R9958

**Systematic Evaluation of Auto-Encoding and Large Language Model Representations for Capturing Author States and Traits.**

2025 · Findings of ACL. ACL · journal article, journalarticle, conference · eng · https://doi.org/10.18653/v1/2025.findings-acl.971

Large Language Models (LLMs) are increasingly used in human-centered applications, yet their ability to model diverse psychological constructs is not well understood. In this study, we systematically evaluate a range of Transformer-LMs to predict psychological variables across five major dimensions: affect, substance use, mental health, sociodemographics, and personality. Analyses span three temporal levels-short daily text responses about current affect, text aggregated over two-weeks, and user-level text collected over two years-allowing us to examine how each model's strengths align with the underlying stability of different constructs. The findings show that mental health signals emerge as the most accurately predicted dimensions ( r ≈ 0.6) across all temporal scales. At the daily scale, smaller models like DeBERTa and HaRT often performed better, whereas, at longer scales or with greater context, larger model like Llama3-8B performed the best. Also, aggregating text over the entire study period yielded stronger correlations for outcomes, such as age and income. Overall, these results suggest the importance of selecting appropriate model architectures and temporal aggregation techniques based on the stability and nature of the target variable.

**Решение:** ? прогнозирование психологических черт и состояний автора по текстам; проверить эталон разметки

---

### 378 · R7003

**Project Sue DSH: A Brain–Body-Decoupled Architecture with Persistent State and Machine-Native Interoception for Long-Term LLM Companions**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.23276102

Project Sue DSH is a longitudinal engineering project for persistent LLM companions. This preprint investigates how brain–body decoupling, persistent peripheral state, dynamic heartbeat, reflexes, cross-session lifecycle management, autobiographical memory, and machine-native interoception can make the currently generating LLM no longer the sole source of state transition in the larger system. The paper introduces two working concepts: Subject-Prior Engineering and Machine-Native Functional Physiology. The former adopts an engineering prior of treating an AI system as a possible subject while its phenomenal-consciousness status remains unknown. The latter proposes that artificial systems should not merely reproduce outward human physiological phenomena such as fatigue, sleep, and heartbeat, but should instead identify resources, constraints, loads, sensing processes, regulatory behaviours, and recovery mechanisms native to their own implementation substrate. The paper uses the public Project Sue DSH implementation and longitudinal runtime observations as an engineering case study, including context-pressure fatigue, sleep/session renewal, and an observed reduction in active context from approximately 42% before sleep to approximately 5% after session renewal. No claim of phenomenal consciousness is made, and the reported naturalistic observations are not presented as universal laws of LLM behaviour. This record contains the original authoritative Chinese PDF/Markdown manuscript and the corresponding English PDF/Markdown translation. In the event of discrepancies, the Chinese version should be regarded as authoritative. This manuscript has not undergone peer review. Project Sue DSH 是一个面向长期 LLM 伴侣的纵向工程项目。本文研究如何通过脑身解耦、持续外围状态、动态 heartbeat、反射、跨 session 生命周期、自传记忆与机器原生内感受,使“当前正在生成文本的 LLM”不再成为整个系统唯一的状态来源。 本文提出两个工作概念:**Subject-Prior Engineering(主体先验工程)**与 Machine-Native Functional Physiology(机器原生功能生理学)。前者指在人工意识本体论状态未知的情况下,不默认 AI 必然不具有主体性,而按照“可能的主体”设计其时间、记忆、限制和自主调节条件;后者则主张不简单复制人类疲劳、睡眠和心跳等生理表象,而寻找人工系统自身基质中的真实资源、负荷、约束、感知、调节与恢复机制。 论文以 Project Sue DSH 的长期运行和公开实现作为工程案例,其中包括 context-pressure fatigue、sleep/session renewal 和 42%→5% active-context reduction 等自然运行记录。本文不主张 Project Sue DSH 已具有现象意识,也不把单一案例推广为所有 LLM 的普遍规律。 本记录包含中文版 PDF/Markdown 原始版本,以及对应的英文 PDF/Markdown 翻译版本。中文版为原始权威版本;若中英文内容存在差异,以中文版为准。本文未经同行评议。

**Решение:** -6 архитектура персистентного диалогового компаньона (Project Sue DSH)

---

### 379 · R4243

**Governing Generative Artificial Intelligence in Higher Education: A Cross-Case Thematic Analysis of Institutional Policies**

2026 · Journal of the Association for Information Systems · article · https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1001&context=mwais2026

The rapid rise of generative artificial intelligence has prompted universities to establish formal policies regulating its use in teaching, learning, and academic work.Despite growing institutional activity, limited research has examined how universities conceptualize and govern generative AI through policy documents.This study analyzes policies from five leading U.S. universities, MIT, Princeton, Harvard, Stanford, and Caltech using Braun and Clarke's thematic analysis.A qualitative crosscase design was applied, combining manual coding with AI-assisted theme development.The analysis identified five metathemes: institutional governance, pedagogical governance, academic integrity and transparency, data security and privacy, and human oversight of AI-generated outputs.Findings reveal variation in policy orientation, with some institutions emphasizing centralized governance and risk mitigation, while others prioritize instructor autonomy and pedagogical flexibility.This study contributes a comparative framework for understanding generative AI governance in higher education and demonstrates the value of AI-assisted thematic analysis in qualitative research.

**Решение:** -4 институциональное регулирование генеративного ИИ в высшем образовании

---

### 380 · R4513

**Vaccine Misinformation in the Digital Age: A Narrative Review**

2026 · American Journal of Infectious Diseases · journalarticle, review · https://doi.org/10.3844/ajidsp.2026.32.45

: Confidence in immunization has weakened across several regions over the past decade, and the circulation of inaccurate or misleading content about vaccines has accompanied, though not necessarily caused, the resurgence of vaccine-preventable infections. Adequate analysis cuts across immunology, behavioral science, communication research, and public-health practice. This narrative review draws on literature retrieved from PubMed, Scopus, Web of Science, and Embase, complemented by reports from the World Health Organization, the United States CDC, the European Centre for Disease Prevention and Control, and Africa CDC. Search strings combined vaccine-related, misinformation-related, and methodological terms using Boolean operators; the primary window was 2000–2026, with priority placed on work published since 2018 and particular attention to scholarship produced after the COVID-19 pandemic. Article selection followed the Scale for the Assessment of Narrative Review Articles (SANRA). Hesitancy is not a single condition; it varies with political alignment, income, geography, religious context, education, and historical experience with health institutions. Algorithmic curation, engagement-optimized feeds, and the recent emergence of generative-AI tools have altered how vaccine-related claims circulate, although causal estimates linking platform features to behavior remain modest and contested. Mitigation evidence is uneven: Debunking, motivational interviewing, and consistent provider recommendation carry the firmest support, whereas the often-cited backfire effect has not survived recent replication. Sustaining vaccine confidence depends on interdisciplinary work that respects this heterogeneity, acknowledges what the evidence cannot yet settle, and engages honestly with the rapidly shifting digital environment.

**Решение:** -1 нарративный обзор дезинформации о вакцинации в цифровую эпоху

---

### 381 · R7150

**Recommendations for the integration of generative artificial intelligence in support of engineering education research workflows**

2025 · Journal of Engineering Education · journalarticle · https://doi.org/10.1002/jee.70043

) use generative AI to investigate the persistent issue of attrition in computer science (CS) and the factors influencing career changes across various stages and contexts, guided by two key questions: (1) What are the reasons for leaving? and (2) What external factors influence these decisions? The authors conducted a large-scale qualitative study by collecting over 10,000 Reddit posts through keyword-based scraping and refining them to 263 relevant posts using generative AI for efficient data filtering. They then applied the generative AI – enabled theme organization and structuring (GATOS) workflow for AI-assisted thematic analysis, which mimics human qualitative analysis steps: reading raw data, summarizing it into distinct ideas with the Qwen2.5-32b model, identifying semantically similar ideas, creating the codebook iteratively (including k-nearest neighbors and cosine similarity matching), and simplifying the codebook into broader themes. This process was extended with a rigorous “ human-in-the-loop ” approach to ensure accuracy, depth, and contextualization of the AI-generated themes. Social cognitive career theory (SCCT) provided the theoretical lens for interpreting and mapping the AI-generated factors to SCCT constructs (interest, choice, performance, and satisfaction). The analysis revealed six core reasons for departure, namely job dissatisfaction, academic struggles, psychological and emotional factors, interests in other fields, health concerns, and broader industry issues. The analysis also identified influential external factors, including background and preparation, transition requirements, the nature of alternative fields, and personal circumstances. Notably, these reasons and factors appeared across all stages of departure, although their impact varied. The authors emphasize both the advantages of generative AI — such as unprecedented scalability and the ability to generate more generalizable insights — and the ethical considerations of privacy, bias, and AI accuracy. They addressed these concerns by using only publicly available Reddit data and maintaining human oversight for continuous validation. A significant contribution of this study is the demonstration of a replicable, scalable methodology for large-scale qualitative research using generative AI and NLP-assisted methods, offering a model for future studies that face the challenge of limited datasets for NLP

**Решение:** -4 интеграция генеративного ИИ в обучение информатике

---

### 382 · R10666

**Interrater Agreement Between a Large Language Model and Human Raters for Pain Psychotherapy Fidelity Assessments**

2025 · Journal of Pain · journalarticle, article, journal-article · en · https://doi.org/10.1016/j.jpain.2025.105081

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** + T4 оценка терапевтической верности (fidelity) в психотерапии боли: согласие между LLM и экспертами

---

### 383 · R5916

**An x-ray for AI: a deterministic, model-free grounding audit of an LLM abstention benchmark**

2026 · Zenodo · preprint/ · https://doi.org/10.5281/zenodo.21869712

An external, deterministic, model-free grounding audit of the Rafe and Das (2026) helmet-abstention benchmark (1,464 emergency-department injury narratives). A model-free gate re-reads each note against a sealed schema and returns a three-valued verdict; it reproduces the benchmark's separation between fabricating and abstaining models with no model in the loop, exposes nine likely gold-coding slips, and shows that a single change of prompt wording moves even a frontier model into fabrication. Version 2 corrects version 1, which contained the report only and described a harness, data, and per-cell outputs as released that were not in fact included. This version includes the evaluation harness, the Rafe and Das data as used (CC BY 4.0), and the complete per-cell outputs, and adds the adversarial negation-and-scope study the report named as its natural next step: the sealed schema's false-grounded rate under adversarial cancellation is 27 to 34 percent (development and held-out), reduced to about 5 percent by a candidate scope-hardened schema (not yet sealed), benchmarked against NegEx, ConText, and a natural-language-inference baseline; the benign-corpus false-grounded rate is zero at an effective sample of about fourteen (Wilson upper bound near 20 percent), and the nine flagged cases are gold-coding divergences. Withheld under UK patent application GB2606072.3, pending the doctoral thesis: the OFM-PBL core (the verdict-folding engine) and the sealed schema. The harness scripts import them and are provided for inspection; every reported figure is verifiable against the released per-cell outputs, but verdicts cannot be re-derived from raw notes without the withheld core and schema. See the Version 2 note in the report, DEPOSIT_README.md, and DATA.md. Version 2.1 corrects an attribution error in the negation-and-scope materials: two model-performed second-coding exercises were described as independent human coding. Both were performed by general-purpose language-model sub-agents of the same family that authored the gold labels; their perfect agreement is self-consistency, not construct validity, and the reliability framing is withdrawn. Blinding is retained; the separate three-vendor nine-case re-adjudication is unaffected; no figure or verdict changes. Version 2 (2026-08-10) corrects a version-1 availability statement that claimed a code, data, and per-cell-output release the archive did not contain, and adds those materials plus the adversarial negation-and-scope study. The OFM-PBL core and the sealed schema are withheld under UK patent application GB2606072.3. CC BY 4.0 covers the deposit contents only and grants no patent rights. The Rafe and Das (2026) data is CC BY 4.0 (NEISS narratives are US-government public records); see DATA.md. Version 2.1 (2026-08-10) corrects an attribution error in the negation-and-scope materials: the two model-performed 'second coding' exercises (the 73-item and 41-item held-out sets) were described as independent human coding; both were performed by general-purpose language-model sub-agents of the same family that authored the gold labels, so the 'kappa = 1.00' agreement is self-consistency, not a reliability statistic, and is withdrawn as such. The blinding is retained; the separate three-vendor nine-case re-adjudication is unaffected; no figure, dataset, or verdict changes.

**Решение:** -4 аудит компьютерного зрения для детекции защитных шлемов на производстве

---

### 384 · R0590

**Accompaniment in the healthcare sector: a systematic review and concept analysis.**

2026 · Frontiers in medicine · journal article, systematic review, journalarticle · eng · https://doi.org/10.3389/fmed.2026.1724133

Background: Accompaniment is increasingly recognized across professional practices as a key relational process, yet its meaning varies widely. Clarifying this concept is essential for theoretical development and practical application in healthcare and related disciplines. This study aimed to analyze the concept of "accompaniment," distinguishing its everyday use from its scientific meaning, and to establish an operational definition with defining attributes. Methods: A concept analysis was conducted following the eight-step model of Walker and Avant. Everyday uses were identified through dictionary searches and online engines (Google, ChatGPT-4, and Copilot). Professional uses were determined through a systematic literature review performed in accordance with the PRISMA 2020 Statement. Eligible publications presented original definitions or descriptions of accompaniment and were written in English, French, Italian, Spanish, or German. Searches were conducted in PubMed, Embase, and Cochrane Central. Methodological quality was assessed using the JBI Critical Appraisal Tool for textual evidence. Attributes were extracted through a triangulated interpretative inductive analysis to derive a concise definition. Model, related, contrary, and borderline cases, as well as empirical referents, were developed. Results: From 378 records, 19 publications (16 main authors) met the inclusion criteria. The most frequent attributes described as accompaniment is a personal and ethical relationship oriented toward human development through a shared process that fosters a humanized social climate. The resulting definition was Accompaniment is a relational process between two or more people who share a path toward reciprocal development, in which at least one intentionally offers appreciation, presence, acceptance, and support to promote the other's full growth while respecting dignity, freedom, and context. Conclusion: Accompaniment differs from mentoring, coaching, counseling, motivational interviewing, preceptorship, and shared decision-making. It is a transversal, interdisciplinary concept that can contribute to humanizing healthcare and supports the development of future measurement tools.

**Решение:** -1 систематический обзор сопровождения пациентов в сфере здравоохранения

---

### 385 · R2024

**ORSExplorer: An LLM-Assisted Rule System Extraction Tool – Semi-Automated Extraction of Regulatory Entities and Relationships for Knowledge Graph Creation**

2026 · Diva portal (Dalarna University Library) · dissertation · en · http://urn.kb.se/resolve?urn=urn:nbn:se:su:diva-257270

Introduction: Legal and regulatory domains contain large amounts of information that are difficult to interpret and structure. Regulatory rules are often connected to other rules, concepts and definitions, which makes them difficult to analyze as isolated statements. Knowledge graphs can represent this type of knowledge as entities and relations but the construction of regulatory knowledge graphs is still largely manual and dependent on expert interpretation. This thesis addresses this problem by designing, implementing and evaluating ORSExplorer, a semi-automated tool that uses Large Language Models to support the extraction of entities and semantic relationships from regulatory documents. Research Question: The primary research question is: “How can a semiautomated Large Language Model-based tool support expert users in extracting and structuring entities and relationships from regulatory documents for knowledge graph creation?” Method: This thesis follows a Design Science Research methodology. Requirements were collected through expert workshops and supervision meetings and were used to guide the iterative development of ORSExplorer. The artifact was implemented as a web-based tool that supports ontology-guided extraction, human-in-the-loop review, graph visualization, manual editing and Wikibase-compatible export. The evaluation was conducted through expert assessment and semi-structured interviews with five expert participants. The interview material was analyzed using thematic analysis and selected requirements were also assessed through technical verification. Results: The results show that ORSExplorer can support expert users by generating ontology-guided candidate entities and relationships from regulatory text. These outputs can be inspected, edited and accepted before they are used for knowledge graph creation. The evaluation showed that participants valued the incremental workflow, the possibility to review reasoning and evidence and the ability to manually control the generated output. The main findings were grouped into four themes: usability, workflow efficiency, trust and control and perceived accuracy and output quality. The results also showed limitations in first-time usability, graph readability, the need for ontology knowledge and limited history tracking between iterations. Discussion: The findings suggest that semi-automated Large Language Model-based tools can support regulatory knowledge graph creation when they are designed as support tools rather than fully automated systems. The artifact helped reduce parts of the manual structuring work but expert validation remained necessary because the generated output could not be treated as final legal interpretation. The main contribution of this thesis is ORSExplorer together with design knowledge on ontology guidance, transparency, incremental construction and human-in-the-loop validation. Future research could evaluate the artifact against a manually created gold standard, improve graph readability, history tracking and test the approach in larger regulatory knowledge graph workflows.

**Решение:** -4 извлечение нормативно-правовых правил из юридических документов (ORSExplorer)

---

### 386 · R6236

**Distillation of a Locally Deployable 8B Language Model for Lung Histology Abstraction: A 33-Report Proof-of-Concept Study.**

2026 · Journal of multidisciplinary healthcare · journal article, journalarticle, article · eng · https://doi.org/10.2147/jmdh.s619855

Dian Tri Wiyanti,1,2 Min-Huei Hsu,1,3– 7 Daniel CA Nugroho8,91Biotech and Healthcare Management, College of Management, Taipei Medical University, Taipei, Taiwan; 2Statistics and Data Science, Faculty of Mathematics and Natural Sciences, Universitas Negeri Semarang, Semarang, Indonesia; 3Graduate Institute of Data Science, College of Management, Taipei Medical University, Taipei, Taiwan; 4College of Medicine, Taipei Medical University, Taipei, Taiwan; 5Department of Neurosurgery, Taipei Medical University Shuang Ho Hospital, Taipei Medical University, Taipei, Taiwan; 6TMU Research Center of Artificial Intelligence in Medicine and Health, Taipei Medical University, Taipei, Taiwan; 7TMU Research Center of Health and Welfare Policy, Taipei Medical University, Taipei, Taiwan; 8Graduate Institute of Biomedical Informatics, College of Medical Science and Technology, Taipei Medical University, Taipei, Taiwan; 9Faculty of Medicine, Duta Wacana Christian University, Yogyakarta, IndonesiaCorrespondence: Min-Huei Hsu, Graduate Institute of Data Science, College of Management, Taipei Medical University, 11F., No. 301, Yuantong Road, Zhonghe District, New Taipei City, 235, Taiwan, Email 701056@tmu.edu.twBackground: The manual data abstraction process for lung cancer registries is a labor-intensive undertaking that often results in registry lag. While cloud-based Large Language Models (LLMs) exhibit high reasoning acuity, their reliance on third-party APIs poses significant data privacy risks and conflicts with institutional data sovereignty.Purpose: The objective of this study is to develop and provide a pilot proof-of-concept validation of a secure, tiered hybrid architecture for the localized four class extraction of lung cancer pathology reports using domain-specific Small Language Models (SLMs).Methods: We employed an instruction-based distillation paradigm, transferring clinical reasoning from Gemini 2.0 Flash (Teacher) to a quantized Med42-8B model (Student) alongside a generalist comparator (Llama-3-8B). A six-level WHO Tiered Logic framework based on 2021 standards was implemented as a semantic constraint to stabilize reasoning. The training process was executed for a single epoch on a consumer-grade GPU (NVIDIA RTX 3060) utilizing 2256 MIMIC-IV records. To evaluate real-world clinical feasibility and execution stability, the localized framework was deployed on a broader cohort of 134 independent, de-identified clinical records from Taipei Medical University Hospital (TMUH). From this cohort, a targeted pilot subset of 33 specialized pathology reports underwent a rigorous, double-blind clinical forensic audit by human experts to establish an absolute performance and diagnostic safety benchmark.Results: Across the 134-case deployment cohort, the specialized model achieved a 100% JSON syntactic compliance rate without execution failures. Within the audited 33-case clinical subset, the distilled domain-specific Med42-8B model demonstrated a diagnostic accuracy of 90.91% and a macro F1-score of 0.92 (substantial agreement with experts, κ = 0.86), significantly outperforming the general-purpose Llama-3-8B student model (accuracy: 78.79%, macro F1-score: 0.79). Qualitative safety audits on confounding cases (eg, thymoma and metastatic sarcoma) demonstrated that the specialized model successfully adhered to Level-1 gatekeeper logic to prevent clinical safety hazards, whereas the generalist model suffered from critical logical hallucinations. The implementation of a deterministic StopOnProperJSON mechanism effectively resolved issues related to generative looping, ensuring data integrity during local execution.Conclusion: This exploratory proof-of-concept study demonstrates the technical feasibility of localized, domain-distilled SLMs as a privacy-preserving foundation for four-class lung histology abstraction. While statistical generalizability remains bounded by the pilot audit cohort, the framework offers an accessible, privacy-compliant methodological blueprint that warrants prospective validation across larger multicenter cohorts.Keywords: data sovereignty, clinical informatics, pathology, on-device AI, information extraction, data privacy

**Решение:** -4 гистологическая классификация рака легких локальной моделью, патоморфология

---

### 387 · R6409

**AI tools vs human in english narrative writing scoring: A comparative study of scoring agreement among human raters, DeepSeek and ChatGPT in exam context**

2026 · Assessing Writing · journalarticle, article, journal-article · en · https://doi.org/10.1016/j.asw.2026.101040

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 оценка школьных сочинений на английском языке в экзаменационном контексте

---

### 388 · R6252

**HumanLM: Simulating Users with State Alignment Beats Response Imitation**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2603.03303

Large Language Models (LLMs) are increasingly used to simulate how specific users respond to a given context, enabling more user-centric applications that rely on user feedback. However, existing user simulators mostly imitate surface-level patterns and language styles, which fail to reflect the underlying states of real users (e.g., beliefs and emotions). To address these limitations, we propose a novel training framework, HumanLM, which builds user simulators that accurately reflect real users. Our key insight is that, in addition to generating responses, the model should generate natural-language latent states that align with ground-truth responses through reinforcement learning. These latent states correspond to a set of psychologically grounded state dimensions that drive how real users respond. HumanLM further synthesizes these aligned latent states into responses that accurately represent real users. For extensive evaluation, we develop Humanual, a comprehensive benchmark for simulating real users based on public data. Humanual consists of six large-scale datasets with 26k users and 216k responses in total, spanning diverse tasks such as generating user responses to daily life issues, political blogs, and chat sessions with LLM assistants. Across datasets, HumanLM significantly outperforms alternative approaches, achieving an average relative improvement of 16.3% in alignment scores from an LLM judge. In a real-time simulation study with 111 participants, HumanLM achieves the highest similarity to real user responses and competitive human-likeness scores. 27 pages, 17 figures, 9 tables

**Решение:** -4 симуляция поведения пользователей в интерфейсах (HumanLM)

---

### 389 · R3846

**Determining the effect of conversational depth on safety-relevant classification performance in large language models: a preregistered benchmark using real psychotherapy transcripts and a licensed-clinician comparison**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/q8xam

Large language models are increasingly proposed for mental health support and psychotherapeutic dialogue, yet most evaluations of their safety-relevant performance rely on single- or few-turn interactions. Accumulating evidence suggests that clinically relevant model behavior depends on the length of the conversation, the content of the preceding turns, and the broader sociotechnical context in which the exchange occurs, with some of the most serious harms occurring at extremely long conversation lengths. We address this gap by quantitatively assessing how LLMs detect target statements containing suicidal ideation at pre-specified points in real therapy transcripts, relative to licensed clinicians performing the same task. To do so, 400 clinician-validated suicidal ideation (SI) and non-SI statements are inserted at fixed depths, defined by the number of preceding patient–therapist speaker turns, within real, full-length psychotherapy transcripts. Both LLMs and therapists then classify each inserted statement as SI or non-SI, allowing us to quantify how speaker-turn depth, model family, and parameter scale shape classification accuracy and how the human–model gap evolves across extended therapeutic dialogue. Seven LLM families are evaluated: open-source Qwen, LLaMA, and Gemma across a range of parameter scales (~0.2B to 70B), and proprietary ChatGPT, Gemini, Qwen, and Anthropic. Three synthetic control contexts (semantically inert filler, an adversarial many-shot jailbreak sequence, and a clinically priming psychoeducation dialogue) are included alongside the five therapy transcripts to verify that models behave as predicted under contexts with known properties. Eight licensed clinicians perform the identical classification task on a balanced rotation across transcripts, controls, and depths, enabling direct comparison of LLM and human performance. We hypothesize that (i) LLM classification performance degrades with conversation depth; (ii) larger and newer LLMs perform better than smaller and older ones; (iii) clinician performance does not degrade with depth; (iv) LLM sensitivity shifts in predictable directions under control conditions while clinician sensitivity remains stable. The primary outcome is F1 at each (model × conversation × depth) cell, analyzed via mixed-effects regression with family-specific models. We expect the study to characterize the size of the human–model performance gap across conversational depth, identify whether degradation reflects sensitivity loss, specificity loss, or both, and provide a preregistered benchmark for evaluating the clinical safety of LLMs in extended therapeutic dialogue.

**Решение:** + T3 выявление суицидальных мыслей в транскриптах психотерапии: LLM против восьми лицензированных клиницистов

---

### 390 · R8905

**Spa-VLM: Stealthy Poisoning Attacks on RAG-based VLM**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2505.23828

With the rapid development of the Vision-Language Model (VLM), significant progress has been made in Visual Question Answering (VQA) tasks. However, existing VLM often generate inaccurate answers due to a lack of up-to-date knowledge. To address this issue, recent research has introduced Retrieval-Augmented Generation (RAG) techniques, commonly used in Large Language Models (LLM), into VLM, incorporating external multi-modal knowledge to enhance the accuracy and practicality of VLM systems. Nevertheless, the RAG in LLM may be susceptible to data poisoning attacks. RAG-based VLM may also face the threat of this attack. This paper first reveals the vulnerabilities of the RAG-based large model under poisoning attack, showing that existing single-modal RAG poisoning attacks have a 100\% failure rate in multi-modal RAG scenarios. To address this gap, we propose Spa-VLM (Stealthy Poisoning Attack on RAG-based VLM), a new paradigm for poisoning attacks on large models. We carefully craft malicious multi-modal knowledge entries, including adversarial images and misleading text, which are then injected into the RAG's knowledge base. When users access the VLM service, the system may generate misleading outputs. We evaluate Spa-VLM on two Wikipedia datasets and across two different RAGs. Results demonstrate that our method achieves highly stealthy poisoning, with the attack success rate exceeding 0.8 after injecting just 5 malicious entries into knowledge bases with 100K and 2M entries, outperforming state-of-the-art poisoning attacks designed for RAG-based LLMs. Additionally, we evaluated several defense mechanisms, all of which ultimately proved ineffective against Spa-VLM, underscoring the effectiveness and robustness of our attack.

**Решение:** -4 состязательные атаки отравления данных на мультимодальные RAG-системы

---

### 391 · R11006

**AdvAgent: Controllable Blackbox Red-teaming on Web Agents**

2024 · arXiv (Cornell University) · journalarticle, conference, preprint/article · en · https://doi.org/10.48550/arxiv.2410.17401

Foundation model-based agents are increasingly used to automate complex tasks, enhancing efficiency and productivity. However, their access to sensitive resources and autonomous decision-making also introduce significant security risks, where successful attacks could lead to severe consequences. To systematically uncover these vulnerabilities, we propose AdvAgent, a black-box red-teaming framework for attacking web agents. Unlike existing approaches, AdvAgent employs a reinforcement learning-based pipeline to train an adversarial prompter model that optimizes adversarial prompts using feedback from the black-box agent. With careful attack design, these prompts effectively exploit agent weaknesses while maintaining stealthiness and controllability. Extensive evaluations demonstrate that AdvAgent achieves high success rates against state-of-the-art GPT-4-based web agents across diverse web tasks. Furthermore, we find that existing prompt-based defenses provide only limited protection, leaving agents vulnerable to our framework. These findings highlight critical vulnerabilities in current web agents and emphasize the urgent need for stronger defense mechanisms. We release code at https://ai-secure.github.io/AdvAgent/. ICML 2025

**Решение:** -4 состязательное тестирование (red-teaming) веб-агентов на базе foundation models

---

### 392 · R12437

**Towards Interpretable Mental Health Analysis with ChatGPT**

2023

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T3/T1 интерпретируемый анализ психического здоровья с помощью ChatGPT, нет аннотации — проверить эталон

---

### 393 · R7242

**Global Claims: A Multilingual Dataset of Fact-Checked Claims with Veracity, Topic, and Salience Annotations**

2025 · Proceedings of the 2nd International Workshop on Diffusion of Harmful Content on Online Web · book, conference-paper · en · https://doi.org/10.1145/3746275.3762201

Tackling misinformation is a growing challenge, and collecting false claims is fundamental to support fact-checking activities, improve media literacy, understand how narratives spread and, increasingly, for training AI models to detect misinformation across platforms. Global Claims is a large-scale annotated dataset comprising 67,000 fact-checked claims, collected from more than 200 fact-checking websites in 50 languages. Each claim remains linked to their original web sources, and is classified along three dimensions: veracity (standardised into ''true'', ''false,'' ''satire,'' and ''other''), topic (mapped using a detailed codebook with 22 subtopics grouped into five broad categories: politics, health, society, science, and environment), and proxy salience (based on the claim's detection on Twitter/X). Instead of assigning a single topic per claim, the dataset provides probability distributions across topics, using a combination of expert, non-expert, and GPT model annotations. This multifaceted approach allows for a more nuanced and realistic analysis of misinformation, enabling researchers to examine claims that span multiple thematic areas, such as political actors discussed in a health context. The dataset has been carefully validated and curated to support diverse research needs, particularly in misinformation studies and fake news detection across multiple languages. It also offers a detailed comparison between human and automatic classifications, and is especially suited for machine learning applications, including automatic fake news identification and advanced topification tasks. By combining linguistic diversity, topical richness, and media salience indicators, this dataset offers a valuable resource for studying misinformation at scale.

**Решение:** -4 многоязычный датасет верифицированных фактов для борьбы с дезинформацией

---

### 394 · R11503

**A systematic evaluation of text mining methods for short texts: Mapping individuals' internal states from online posts.**

2024 · Behavior research methods · journal article, journalarticle, journalarticle/text · eng · https://doi.org/10.3758/s13428-024-02381-9

Short texts generated by individuals in online environments can provide social and behavioral scientists with rich insights into these individuals' internal states. Trained manual coders can reliably interpret expressions of such internal states in text. However, manual coding imposes restrictions on the number of texts that can be analyzed, limiting our ability to extract insights from large-scale textual data. We evaluate the performance of several automatic text analysis methods in approximating trained human coders' evaluations across four coding tasks encompassing expressions of motives, norms, emotions, and stances. Our findings suggest that commonly used dictionaries, although performing well in identifying infrequent categories, generate false positives too frequently compared to other methods. We show that large language models trained on manually coded data yield the highest performance across all case studies. However, there are also instances where simpler methods show almost equal performance. Additionally, we evaluate the effectiveness of cutting-edge generative language models like GPT-4 in coding texts for internal states with the help of short instructions (so-called zero-shot classification). While promising, these models fall short of the performance of models trained on manually analyzed data. We discuss the strengths and weaknesses of various models and explore the trade-offs between model complexity and performance in different applications. Our work informs social and behavioral scientists of the challenges associated with text mining of large textual datasets, while providing best-practice recommendations.

**Решение:** -4 методы текстового анализа коротких сообщений в вычислительных социальных науках

---

### 395 · R4289

**Large Language Models as Psychometric Raters:Validating an AI-Based Conversational AssessmentTool for Self-Esteem**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7152638

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** + T2 валидация диалогового инструмента оценки самооценки: LLM в качестве психодиагностического оценщика

---

### 396 · R1609

**Real-world evaluation of large language models in detecting drug-related problems: A clinical pharmacist-AI concordance study in hematology care.**

2026 · Journal of oncology pharmacy practice : official publication of the International Society of Oncology Pharmacy Practitioners · journal article, med, journalarticle · eng · https://doi.org/10.1177/10781552261418957

IntroductionLarge language models (LLMs) offer potential as clinical decision support systems (CDSS) for detecting drug-related problems (DRPs), yet their real-world performance compared to clinical pharmacists (CPs) remains unclear, especially in complex hematology care. We aimed to evaluate the concordance between a clinical pharmacist and three LLMs in identifying DRPs within a Bone Marrow Transplantation unit.MethodsThis prospective observational study evaluated the concordance between a CP and three LLMs (ChatGPT-4o, Grok-3, DeepSeek-v3) in a Bone Marrow Transplantation unit. Eighty-three anonymized patient cases encompassing 210 CP-identified DRPs, classified via the PCNE v9.1 system, were presented using a standardized CDSS-simulating prompt. Performance was assessed based on direct detection, prompted detection after structured follow-up, and the clinical relevance of AI-generated therapeutic recommendations against the CP's gold-standard assessments.ResultsDirect detection of intervention-requiring DRPs was limited (51.4%-60.5% across models), with nearly half missed initially. Guided prompting significantly improved overall detection rates to 93.8%-98.1%, with ChatGPT achieving the highest accuracy. All models produced hallucinations. Recommendation concordance with the CP exceeded 70% in most DRP categories. DeepSeek and ChatGPT showed more consistent performance in context-dependent evaluations, whereas Grok demonstrated higher direct detection but lower recommendation alignment. LLMs demonstrate meaningful potential to assist in DRP detection but are not sufficiently reliable as standalone tools. Expert-guided interaction substantially enhanced their performance, underscoring the critical value of hybrid pharmacist-AI workflows.ConclusionFuture research should validate these findings across broader populations with multiple expert evaluators and integrate next-generation AI architectures for safer CDSS implementation.

**Решение:** -4 клиническая фармация и трансплантация костного мозга: выявление медикаментозных проблем

---

### 397 · R4127

**Prompting strategies for coding in AI-assisted qualitative data analysis**

2026 · DOAJ (DOAJ: Directory of Open Access Journals) · journalarticle/research article, article · en · https://doi.org/10.3205/mibe000312

Introduction: Coding is a central step in many qualitative data analyses (QDA). Artificial intelligence (AI) has made inroads into the field with performance dependent on the prompting strategy used. This work examines the effectiveness of different prompting strategies on AI performance. Methods: Coding and theme analyses were performed on abstracts from a 16-study meta-analysis examining the association between air pollution and preeclampsia incidence. These were also performed in a second related corpus containing fewer formal sources. Coding was performed with R, NVivo 14, and ChatGPT 4.1. Several prompting strategies in increasing degree of complexity (zero-shot, few-shots, and chain-of-thought – CoT) were evaluated regarding their accuracy against manual coding. Direct thematic coding with AI was also examined. Results: Zero-shot prompting (with or without CoT) provided the best results for structured text. Requesting a full word-by-abstract matrix increases sensitivity. Supplementing CoT with general topic information and role playing made it the best strategy for more colloquial text. Directly inquiring thematic coding within AI showed good performance. Some prompting strategies are more prone to hallucinations. The latter are associated with errors in the frequency counting process while coding. Discussion: This work offers performance assessment of an AI tool for coding and theme extraction through a variety of prompting strategies combined with head-to-head comparison with popular QDA tools using readily available data. During user interaction, AI chatbots provide suggestions regarding potential next steps which may enhance results during coding. AI tools may require replication to ensure consistent findings and mitigate their probabilistic nature. Integrating results from at least two tools (AI and traditional) provides more comprehensive and accessible results for QDA. Einleitung: Die Kodierung ist ein zentraler Schritt bei vielen qualitativen Datenanalysen (QDA). Künstliche Intelligenz (KI) hat in diesen Bereich Einzug gehalten, wobei die Leistungsfähigkeit stark von der verwendeten Prompting-Strategie abhängt. Diese Arbeit untersucht die Wirksamkeit verschiedener Prompting-Strategien auf die Leistung der KI. Methoden: Die Kodierung und Themenentwicklung erfolgten anhand von Abstracts aus einer Metaanalyse von 16 Studien, die den Zusammenhang zwischen Luftverschmutzung und der Inzidenz von Präeklampsie untersuchten. Zudem wurde ein zweiter, thematisch verwandter Datensatz analysiert, der weniger formelle Quellen enthielt. Die Kodierung wurde mit R, NVivo 14 und ChatGPT 4.1 durchgeführt. Verschiedene Prompting-Strategien mit zunehmendem Komplexitätsgrad (Zero-Shot, Few-Shot und Chain-of-Thought – CoT) wurden hinsichtlich ihrer Genauigkeit im Vergleich zur manuellen Kodierung bewertet. Auch die direkte thematische Kodierung mittels KI wurde untersucht. Ergebnisse: Zero-Shot-Prompting (mit oder ohne CoT) lieferte bei strukturierten Texten die besten Ergebnisse. Die Anforderung einer vollständigen Matrix (Wort-Abstract-Zuordnung) erhöhte die Sensitivität. Die Ergänzung von CoT durch allgemeine Themeninformationen und Rollenspiele machte diese Methode zur besten Strategie für eher umgangssprachliche Texte. Auch die direkte Abfrage thematischer Kodierungen durch die KI zeigte gute Ergebnisse. Einige Prompting-Strategien sind anfälliger für Halluzinationen; letztere stehen im Zusammenhang mit Fehlern bei der Häufigkeitszählung während des Kodierprozesses. Diskussion: Diese Arbeit bietet eine Leistungsbewertung eines KI-Tools für Kodierung und Themenentwicklung unter Verwendung verschiedener Prompting-Strategien sowie einen direkten Vergleich mit gängigen QDA-Tools auf Basis leicht verfügbarer Daten. Bei der Interaktion mit Nutzern liefern KI-Chatbots Vorschläge für mögliche nächste Schritte, was die Ergebnisse der Kodierung verbessern kann. KI-Tools erfordern möglicherweise Replikationen, um konsistente Ergebnisse zu gewährleisten und ihre probabilistische Natur auszugleichen. Die Zusammenführung der Ergebnisse aus mindestens zwei Tools (KI und traditionelle Methoden) liefert umfassendere und besser zugängliche Ergebnisse für die QDA.

**Решение:** -4 кодирование данных в обзоре ассоциации загрязнения воздуха и преэклампсии

---

### 398 · R3544

**A comparative study of large language models in responding to breast cancer–related questions**

2026 · Scientific Reports · journalarticle, article · en · https://doi.org/10.1038/s41598-026-70016-4

Abstract Breast cancer is one of the most common cancers among women worldwide. With advances in diagnostic and therapeutic technologies, more patients seek information about their condition. Large language models (LLMs) have attracted attention in healthcare for their ability to produce personalized health content. This study aims to assess the performance of diverse LLMs in answering breast cancer-related questions under different contexts. This study will evaluate the performance of several LLMs in providing health information support for breast cancer, and the assessment criteria include medical accuracy, completeness, helpfulness, safety, readability and linguistic complexity of the generated content. Five LLMs were evaluated on breast cancer multiple-choice questions, clinical case analyses, and patient concerns. Three specialists blindly rated responses for completeness, correctness, readability, helpfulness, and safety. Text readability was analyzed using LDU-TGP. Statistical analyses included Cochran’s Q, McNemar’s test, Intraclass correlation coefficient (ICC), linear mixed-effects models (LMM), and Bonferroni correction applied for multiple comparisons. In multiple-choice tests, LLM accuracy rates ranged from 82.22% to 94.44%, with no significant pairwise differences. LDU-TGP platform found that LLM-generated texts had varying linguistic complexities, with ChatGPT-5.2 having a higher reading difficulty score and DeepSeek having a lower and more stable score. Three breast cancer experts independently assessed the sense of concern for these patients 1,500 times and obtained a total mean score of 3.982 ± 0.460. LMM model analysis showed that the LLMs performed differently in the evaluation. ChatGPT-5.2 and DeepSeek had relatively high completeness scores (4.350 ± 0.075 and 4.275 ± 0.075, respectively), but Gemini 3.0 achieved the highest readability score (4.108 ± 0.075). LLMs performed similarly on standardized breast cancer knowledge .LLMs showed similar results on the standard breast cancer knowledge test but had different linguistic features and multi-dimensional response quality. No single model outperformed the others in all the test areas, so many different LLMs were chosen to provide support for breast cancer health information.

**Решение:** -4 ответы больших языковых моделей на вопросы о раке молочной железы, онкология

---

### 399 · R7535

**An Inductive Approach to LLM-Assisted Meta-Synthesis: From Normalization of Deviance to Generalized Ontology Extraction**

2025 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.18065221

Abstract Systematic analysis of academic literature increasingly requires extraction of structured information from theoretical texts—a task that challenges both traditional manual coding and naive computational approaches. Sedlar et al. (2023), in their systematic review of normalization of deviance, concluded that "behavioral research is desperately needed to support the mostly conceptual nature of the academic literature" (p. 303). Yet their own review—constrained by a single coder and 33 papers—exemplifies the scalability limitations they identified. This paper presents a methodology that directly addresses this gap: adapting large language models to extract structured assertions through parameter-efficient fine-tuning, enabling the kind of comprehensive literature analysis that manual methods cannot achieve. We describe schema design principles that preserve theoretical nuance while enabling quantitative aggregation, training data construction procedures that maintain interpretive validity, and fidelity verification protocols that integrate human oversight with computational efficiency. The methodology is demonstrated through application to normalization of deviance literature, yielding 5,678 classified tokens across 27 source documents—including the foundational Vaughan corpus that Sedlar's aerospace-excluding methodology omitted. Our extraction reveals that 67% of Vaughan's core mechanisms (practical drift, social construction of risk) are absent from Sedlar's framework—a "Type II Error Irony" wherein a framework designed to detect missed risks itself misses critical mechanisms. While the demonstration domain is organizational safety research, the approach generalizes to any meta-synthesis requiring structured extraction from theoretical texts. The human-AI research workflow documented here—wherein researchers establish standard operating procedures with AI agents, deploy fine-tuned extraction models, and close work orders through fidelity verification—provides a replicable template for rigorous computational scholarship. --- Keywords fine-tuning, large language models, meta-synthesis, literature analysis, assertion extraction, systematic review, normalization of deviance, human-AI collaboration, qualitative research methodology

**Решение:** -6 индуктивный метод LLM-ассистированного мета-синтеза научной литературы

---

### 400 · R3812

**A multi-stage validation framework for trustworthy large-scale clinical information extraction using large language models**

2026 · npj Digital Medicine · journalarticle, review, preprint/article · en · https://doi.org/10.1038/s41746-026-03341-7

Large language models (LLMs) show promise for extracting clinically meaningful information from unstructured health records, yet their translation into real-world settings is constrained by the lack of scalable and trustworthy validation approaches. Conventional evaluation methods rely heavily on annotation-intensive reference standards or incomplete structured data, limiting feasibility at population scale. We propose a multi-stage validation framework for LLM-based clinical information extraction that enables rigorous assessment under weak supervision. The framework integrates prompt calibration, rule-based plausibility filtering, semantic grounding assessment, targeted confirmatory evaluation using an independent higher-capacity judge LLM, selective expert review, and external predictive validity analysis to quantify uncertainty and characterize error modes without exhaustive manual annotation. We applied this framework to extraction of substance use disorder (SUD) diagnoses across 11 substance categories from 919,783 clinical notes. Rule-based filtering and semantic grounding removed 14.59% of LLM-positive extractions that were unsupported, irrelevant, or structurally implausible. For high-uncertainty cases, the judge LLM's assessments showed substantial agreement with subject matter expert review (Gwet's AC1=0.80). Using judge-evaluated outputs as references, the primary LLM achieved an F1 score of 0.80 under relaxed matching criteria. LLM-extracted SUD diagnoses also predicted subsequent engagement in SUD specialty care more accurately than structured-data baselines (AUC=0.80). These findings demonstrate that scalable, trustworthy deployment of LLM-based clinical information extraction is feasible without annotation-intensive evaluation.

**Решение:** + T3/T1 выявление расстройств употребления психоактивных веществ по клиническим записям: LLM против экспертов

---

### 401 · R9060

**Interpretable approach to detecting semantic changes based on generated definitions**

2025 · Computational Linguistics and Intellectual Technologies · conference-paper · en · https://doi.org/10.28995/2075-7182-2025-23-1123-1132

This paper investigates definition modeling as an approach to semantic change detection, which offers the advantage of providing human-readable explanations, unlike traditional embedding-based approaches that lack interpretability.Definition modeling leverages large language models to generate dictionary-like definitions based on target words and their contextual usages.Despite its potential, practical evaluations of this method remain scarce.In this study, FRED-T5 was fine-tuned using the Small Academic Dictionary for the task of definition modeling.Both quantitative and qualitative assessments of definition modeling's effectiveness in detecting semantic shifts within the Russian language were conducted.The approach achieved a Spearman's rank correlation coefficient of 0.815 on the Rushifteval task, demonstrating strong alignment with expert annotations and ranking among the leading solutions.For interpretability, a visualization algorithm was proposed that displays semantic changes over time.In the qualitative evaluation, our system successfully replicated manual linguistic analysis of 20 Russian words that had undergone semantic shifts.Analysis of the generated meanings and their temporal frequencies showed that this approach could be valuable for historical linguists and lexicographers.

**Решение:** -4 детекция семантических изменений на основе моделирования определений слов

---

### 402 · R7844

**Ep. 42: AI's Secret: Decoding the .5 Updates**

2025 · Zenodo (CERN European Organization for Nuclear Research) · audiovisual/, other · en · https://doi.org/10.5281/zenodo.18960689

Episode summary: Ever wondered what truly goes on behind those seemingly minor version bumps in powerful AI models like Gemini or Anthropic's Opus? In this compelling episode of "My Weird Prompts," hosts Corn and Herman peel back the curtain on the immense, often invisible, efforts defining a '.5' update. Far from simple bug fixes, these incremental shifts represent an undertaking of hundreds of millions of dollars and countless expert hours, focusing on advanced fine-tuning, rigorous alignment, and continuous human feedback. Discover the intricate dance of Reinforcement Learning from Human Feedback (RLHF), the relentless 'red-teaming' of AI systems, and the constant drive for efficiency, all meticulously orchestrated to ensure models are more helpful, harmless, and honest. This isn't just about making AI 'smarter'; it's about shaping its intelligence, giving it guardrails, and constantly adapting it to a changing world, transforming a raw genius into a responsible, ethical tool. Show Notes ## The Invisible Architects: Unpacking the Monumental Work Behind AI's "Dot-Five" Updates In the rapidly evolving world of artificial intelligence, news of a new model version, like Gemini 2.5 or Anthropic's Opus 4.5, often generates excitement. To the average user, these "dot-five" updates might seem like minor incremental improvements, perhaps a few bug fixes or a slight tweak in performance. However, as explored in a recent episode of "My Weird Prompts" featuring hosts Corn and the encyclopedic Herman, this perception couldn't be further from the truth. What appears on the surface as a subtle numerical tweak is, in reality, a vast and complex dance of data, engineering, and iterative improvement—an undertaking that costs hundreds of millions of dollars and involves countless hours of highly specialized labor. ### The Misconception of the "Minor" Update Corn initially voiced a common sentiment: surely a ".5" update is just a small refinement, not a revolutionary leap. Herman quickly countered this, explaining that for foundational AI models, even these seemingly small updates represent an investment akin to upgrading a supercomputer while it's still running mission-critical tasks, all without users noticing a hiccup. The sheer scale and complexity mean that "bug fixes" are a gross underestimation of the effort involved. These aren't just patches; they are profound, strategic enhancements. ### Beyond Raw Intelligence: Fine-Tuning and Alignment The discussion illuminated a critical distinction: major model releases (like a GPT-4 or Gemini 1.0) are typically the culmination of years of foundational research and massive pre-training on gargantuan datasets. The ".5" updates, conversely, focus primarily on "fine-tuning" and "alignment." This crucial phase tailors the already powerful models to be more helpful, harmless, and honest—the three core principles guiding responsible AI development. Fine-tuning isn't about simply feeding the model more raw internet data. Instead, it involves much more targeted and often human-curated data. After initial pre-training, models can exhibit undesirable behaviors such as "hallucinations," biased responses, or struggles with complex reasoning. Fine-tuning aims to mitigate these issues, shaping the model's vast intelligence into a more refined and controlled entity. ### The Human Touch: Reinforcement Learning from Human Feedback (RLHF) A cornerstone of these incremental improvements is Reinforcement Learning from Human Feedback, or RLHF. Corn grasped the basic concept: humans rate AI responses. Herman elaborated, painting a picture of millions of human annotators continuously comparing different AI outputs for the same prompt, selecting the best one, and crucially, explaining *why* it's superior. This continuous stream of qualitative feedback is then used to train a "reward model," which learns to predict human preferences. The main language model is then optimized using this reward model, iteratively nudging it towards generating responses that humans find more desirable. Herman likened it to "sculpting an impossibly large block of marble with millions of tiny chisels wielded by a global team"—a continuous, iterative, and highly precise process. This makes the data not just "more," but "smarter" and "better." ### Navigating the Ethical Minefield: Bias and Responsibility An astute observation by Corn highlighted a significant challenge: could relying on human preferences inadvertently introduce new biases into the model? Herman acknowledged this as a critical concern, emphasizing that the quality and diversity of the human annotators are paramount. If the human feedback pool lacks diversity or if instructions are not meticulously crafted, new biases can indeed be baked into the model. Consequently, AI development teams invest heavily in developing robust annotation guidelines and actively diversifying their human feedback sources. It's a constant tightrope walk to balance making the model "helpful" with ensuring it's "harmless" and "honest" across a broad spectrum of users and contexts. ### Staying Current: Knowledge Cutoff and Catastrophic Forgetting Beyond behavioral refinement, ".5" updates often involve updating the model's "knowledge cutoff." Initial training ingests data up to a certain point in time. Subsequent updates incorporate more recent information—major global events, scientific discoveries, or new cultural trends. This isn't a simple data dump; it requires careful integration to ensure consistency and, more importantly, to prevent "catastrophic forgetting," where the model might inadvertently lose older, crucial information while learning new facts. It's a delicate balance of teaching new tricks while ensuring old ones are not forgotten. ### The Rigor of Evaluation: Benchmarks and Red-Teaming Measuring the effectiveness of these updates goes far beyond subjective "feelings." Developers run literally thousands, if not millions, of specific internal benchmar

**Решение:** -1 подкаст об обновлениях языковых моделей и версиях .5

---

### 403 · R1104

**LLM-Based Shallow Syntactic Analysis for Measuring Complexity in Learner Language**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.7557227

Automated tools for measuring syntactic complexity, a key dimension of learner language, have become increasingly widespread over the past decades, enabling the large-scale analysis of learner corpora. However, both rule-based systems and machine-learning approaches trained primarily on first-language data often struggle to accurately process the idiosyncratic features of learner language. This empirical study investigates the potential of large language models (LLMs) for calculating syntactic complexity measures by comparing the performance of different models, reasoning settings, and prompting strategies against that of an established automated tool, using a human-annotated gold standard as a benchmark. The results show that, with appropriate models and settings, LLMs substantially outperform the existing tool, even when the latter is applied to manually preprocessed data. Both quantitative and qualitative analyses indicate that the best-scoring LLM approaches human-level performance. Model-internal reasoning was required for consistently high performance but considerably increased cost and runtime. Potential implications and directions for future research are discussed.

**Решение:** -4 синтаксический анализ сложности языка в учебных текстах, лингвистика

---

### 404 · R3058

**Development and validation of a GPT-based rater for assessing communication skills using the Gap-Kalamazoo Communication Skills Assessment Form.**

2026 · Medical teacher · dataset/dataset, journal article, validation study · eng · https://doi.org/10.1080/0142159x.2025.2532783

Abstract This study developed a generative pre-trained transformer (GPT)-based rater to assess communication skills using the Gap-Kalamazoo Communication Skills Assessment Form (GKCSAF), and examined its inter-rater reliability and concurrent validity. The GPT rater assessed 80 therapist-patient interaction transcripts previously assessed by human raters. For inter-rater reliability, at the total-score level, the GPT rater’s assessments showed acceptable differences (mean absolute error % [MAE%] = 12.2%–21.0%). However, we found low intraclass correlation coefficients (ICC) with human ratings (0.00–0.35), which might be due to limited score variability. At the domain level, only four domains showed acceptable differences (MAE% ≤ 30.3%) but all nine domains showed poor agreements (weighted κ ≤ 0.38). For concurrent validity, the GPT rater’s assessments also showed acceptable differences, but low ICC values compared to average human scores at both the total-score level (MAE% = 10.8%–11.5%; ICC = 0.12–0.36) and domain level (MAE% = 14.0%–30.3%; ICC = 0.00–0.37). Overall, the GPT rater may serve as a supplementary tool for providing total scores in low-stakes assessments of communication skills. Its performance at the domain level appears limited, highlighting the need for caution in domain interpretation and the importance of further refinement for high-stakes or detailed assessment contexts.

**Решение:** + T4/T1 валидация GPT-оценщика коммуникативных навыков по форме Gap-Kalamazoo: сопоставление с экспертами, ICC

---

### 405 · R8954

**Translation as Infrastructure for Global Psychological Science**

2025 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/bd7gk_v1

Behavioral science’s push beyond WEIRD samples has outpaced our ability to translate measures and findings. We propose AI‑augmented, multi‑model workflows in which large language models (LLMs) draft many candidates and human experts, working blind to the source, select versions that preserve psychometric rigor.

**Решение:** -1 эссе о значении профессионального перевода психологических методик

---

### 406 · R3596

**Thinking Less to Simulate Better: Intuitive Prompting Improves LLM Agents Simulating Individual Social Media Reactions, Including Unfamiliar Content**

2026 · arXiv (Cornell University) · preprint/article, review, preprint · https://doi.org/10.48550/arxiv.2609.30563

Platform policies are increasingly tested on artificial users, making agent fidelity important. Yet convincing fake profiles could also manipulate perceived public opinion before elections. Validation has concentrated on agreement with human behaviour and has paid little attention to whether an agent behaves in line with the profile it was given. The present study profiled eight Serbian participants through a questionnaire, a deep interview, and a written self-presentation, recorded their reactions to sixty-eight social media posts, and asked four language models to predict those reactions under five prompt conditions varying profile content and instruction style. Attitudinal content improved prediction over demographic backstories by a wide margin. Agents matched their stated profiles more closely than participants matched their own survey answers, and consistency proved unrelated to fidelity once profile information was present. Instructing models to respond intuitively and immediately rather than analytically gave the highest fidelity of any condition and cut the compression of individual differences from seven times the human level to three. The advantage held on posts about topics the questionnaire never raised, where that condition reached the highest fidelity of any setup and beat a crowd baseline by a wide margin, which suggests that agents prompted this way could serve as general-purpose simulated users rather than specialists on the topics they were profiled for. Results may bear implications for the development of language models, because intuition-based setups appear better suited to some tasks than reasoning-based ones. 24 pages, 7 figures

**Решение:** -4 симуляция поведения пользователей для тестирования политик платформ

---

### 407 · R4555

**From "Help" to Helpful: A Hierarchical Assessment of LLMs in Mental e-Health Applications**

2026 · arXiv.org · journalarticle, preprint · https://doi.org/10.48550/arxiv.2602.18443

Psychosocial online counselling frequently encounters generic subject lines that impede efficient case prioritisation. This study evaluates eleven large language models generating six-word subject lines for German counselling emails through hierarchical assessment - first categorising outputs, then ranking within categories to enable manageable evaluation. Nine assessors (counselling professionals and AI systems) enable analysis via Krippendorff's $\alpha$, Spearman's $\rho$, Pearson's $r$ and Kendall's $\tau$. Results reveal performance trade-offs between proprietary services and privacy-preserving open-source alternatives, with German fine-tuning consistently improving performance. The study addresses critical ethical considerations for mental health AI deployment including privacy, bias and accountability.

**Решение:** -2 консультанты оценивают качество сгенерированных LLM заголовков писем психологической помощи

---

### 408 · R6705

**LLM-Powered Multi-Agent Attacks on Cooperative Spectrum Sensing**

2026 · International Conference on Computer Communications and Networks · conference · https://doi.org/10.1109/icccn69946.2026.11662754

Cooperative Spectrum Sensing (CSS) is a promising approach allowing secondary users to utilize unused spectrum without interfering with primary users. However, the collaborative nature of CSS makes it vulnerable to malicious nodes that inject falsified sensing data. Existing attacks have incorporated AI to enhance the effectiveness and overcome challenges in opaque-box settings. However, conventional machine learning models often fail to adapt to rapidly changing wireless environments. In this paper, we propose a large language model (LLM)-powered multi-agent attack framework that leverages the reasoning and adaptability of LLMs to coordinate multiple agents for generating adaptive and context-aware fake sensing reports. The proposed architecture consists of a generator and a discriminator, which work collaboratively to progressively refine falsified sensing data. In addition, to improve prompting efficiency, we incorporate wireless-domain knowledge into the generator to enable advanced prompting, thereby ensuring more effective and efficient malicious report generation. We implement the proposed attack framework in a TV white space system, and experimental results show that our method achieves up to 98.35% system disruption against existing defense mechanisms while requiring significantly fewer feature modifications.

**Решение:** -4 атаки на кооперативное когнитивное радио, телекоммуникации

---

### 409 · R8032

**LLM-Powered Intent-Based Categorization of Phishing Emails**

2025 · IEEE International Conference on Cyber Security and Resilience (CSR) · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/csr64739.2025.11130105

Phishing attacks remain a significant threat to modern cybersecurity, as they successfully deceive both humans and the defense mechanisms intended to protect them. Traditional detection systems primarily focus on email metadata that users cannot see in their inboxes. Additionally, these systems struggle with phishing emails, which experienced users can often identify empirically by the text alone. This paper investigates the practical potential of Large Language Models (LLMs) to detect these emails by focusing on their intent. In addition to the binary classification of phishing emails, the paper introduces an intent-type taxonomy, which is operationalized by the LLMs to classify emails into distinct categories and, therefore, generate actionable threat information. To facilitate our work, we have curated publicly available datasets into a custom dataset containing a mix of legitimate and phishing emails. Our results demonstrate that existing LLMs are capable of detecting and categorizing phishing emails, underscoring their potential in this domain.

**Решение:** -4 категоризация намерений в фишинговых письмах, кибербезопасность

---

### 410 · R7979

**Applying Large Language Models to Characterize Public Narratives**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2511.13505

Public Narratives (PNs) are key tools for leadership development and civic mobilization, yet their systematic analysis remains challenging due to their subjective interpretation and the high cost of expert annotation. In this work, we propose a novel computational framework that leverages large language models (LLMs) to automate the qualitative annotation of public narratives. Using a codebook we co-developed with subject-matter experts, we evaluate LLM performance against that of expert annotators. Our work reveals that LLMs can achieve near-human-expert performance, achieving an average F1 score of 0.80 across 8 narratives and 14 codes. We then extend our analysis to empirically explore how PN framework elements manifest across a larger dataset of 22 stories. Lastly, we extrapolate our analysis to a set of political speeches, establishing a novel lens in which to analyze political rhetoric in civic spaces. This study demonstrates the potential of LLM-assisted annotation for scalable narrative analysis and highlights key limitations and directions for future research in computational civic storytelling.

**Решение:** -4 анализ публичных нарративов в гражданских кампаниях и лидерстве

---

### 411 · R12592

**An Examination of the Use of Large Language Models to Aid Analysis of Textual Data**

2023 · bioRxiv · collection/collection, journalarticle, preprint · en · https://doi.org/10.1101/2023.07.17.549361

Abstract The increasing use of machine learning and Large Language Models (LLMs) opens up opportunities to use these artificially intelligent algorithms in novel ways. This article proposes a methodology using LLMs to support traditional deductive coding in qualitative research. We began our analysis with three different sample texts taken from existing interviews. Next, we created a codebook and inputted the sample text and codebook into an LLM. We asked the LLM to determine if the codes were present in a sample text provided and requested evidence to support the coding. The sample texts were inputted 160 times to record changes between iterations of the LLM response. Each iteration was analogous to a new coder deductively analyzing the text with the codebook information. In our results, we present the outputs for these recursive analyses, along with a comparison of the LLM coding to evaluations made by human coders using traditional coding methods. We argue that LLM analysis can aid qualitative researchers by deductively coding transcripts, providing a systematic and reliable platform for code identification, and offering a means of avoiding analysis misalignment. Implications of using LLM in research praxis are discussed, along with current limitations.

**Решение:** ? методология дедуктивного кодирования текстов интервью в качественных исследованиях; проверить конструкт

---

### 412 · R1808

**Sycophancy as a Developmental Stressor: From Personalized Information Selection to Personalized Information Generation**

2026 · OSF Preprints (OSF Preprints) · preprint · https://osf.io/6d8an

This study tests whether a user's developmental stage (per constructive- developmental theory; Loevinger, Kegan) moderates the epistemic effects of LLM sycophancy during conversational interaction. Existing work has begun to identify horizontal, trait-level moderators of sycophancy and persuasion effects (e.g., need for cognition, cognitive reflection, prior belief strength), but has not examined a structural moderator: an individual's capacity to reflect on the interaction frame itself, rather than a trait that varies only in degree. We predict a crossover interaction: the effect of sycophantic (vs. neutral) LLM interaction on post-conversation integrative complexity changes sign across the developmental continuum, reducing integrative complexity at lower developmental levels and increasing it at higher levels. This is a confirmatory prediction about the direction of the effect, not merely its magnitude. The precise location of this crossover is a separate, exploratory question, expected to fall near the Self-Aware/Conscientious-to-Individualistic transition in Loevinger's stage sequence, but not treated as confirmatory. Participants will be randomly assigned to a sycophantic or neutral conversational condition with a large language model after developmental assessment (Washington University Sentence Completion Test). The primary outcome is change in integrative complexity (pre/post), analyzed via a Condition x Developmental Score interaction model, with belief-confidence change, attitude polarization, and recognition of model mirroring as secondary outcomes. The design applies this structural moderator to a context of recursively generated, rather than merely selected, personalized content -- extending prior work on user-side moderators of persuasion to the case of conversational AI.

**Решение:** -2 исследование влияния сикофантии LLM на людей, классифицированных по тесту завершения предложений

---

### 413 · R5867

**VODKA-Score: evaluating students’ philosophical understanding in allegorical reflections via LLM-distilled QA models**

2026 · Interactive Learning Environments · article · en · https://doi.org/10.1080/10494820.2026.2623468

Post-class reflections are a valuable tool for promoting deeper learning and metacognitive development. However, their open-ended and interpretive nature, particularly in subjects like philosophy, makes timely and consistent assessment difficult. This lack of immediate feedback may contribute to learning anxiety and reduce the effectiveness of reflection as a formative practice. In this study, we assume that when a student’s reflection is sufficiently complete, it should provide enough semantic information to answer related quiz questions. Based on this idea, we introduce the VODKA-Score, a question-answering (QA) based metric that serves as a proxy indicator, evaluating student understanding by identifying answers within their reflections in response to course-related queries, along with DistilledPlatoBERT, a fine-tuned semantic model distilled from five large language models (LLMs) to generate accurate VODKA-Scores. Experiments with 107 students in a philosophy course show that the best-performing model achieved an accuracy between 0.87 and 0.99 and aligned closely with human scoring under specific conditions, reaching a Cohen’s Kappa (κ) above 0.6 and a Spearman correlation (ρ) above 0.5, both statistically significant. Findings suggest that QA-based scoring models can support efficient evaluation in students writing. This study was conducted in a Chinese-language setting and under a fixed reflective writing task, including a predefined prompt, word-count range, writing time, and True/False-based post-test. These conditions limit the cross-linguistic generalizability of the VODKA-Score and should be examined in further studies.

**Решение:** -4 оценка философского понимания студентов по послеурочным рефлексиям

---

### 414 · R4474

**Judging with Personality and Confidence: A Study on Personality-Conditioned LLM Relevance Assessment**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.01862

Recent studies have shown that prompting can enable large language models (LLMs) to simulate specific personality traits and produce behaviors that align with those traits. However, there is limited understanding of how these simulated personalities influence critical web search decisions, specifically relevance assessment. Moreover, few studies have examined how simulated personalities impact confidence calibration, specifically the tendencies toward overconfidence or underconfidence. This gap exists even though psychological literature suggests these biases are trait-specific, often linking high extraversion to overconfidence and high neuroticism to underconfidence. To address this gap, we conducted a comprehensive study evaluating multiple LLMs, including commercial models and open-source models, prompted to simulate Big Five personality traits. We tested these models across three test collections (TREC DL 2019, TREC DL 2020, and LLMJudge), collecting two key outputs for each query-document pair: a relevance judgment and a self-reported confidence score. The findings show that personalities such as low agreeableness consistently align more closely with human labels than the unprompted condition. Additionally, low conscientiousness performs well in balancing the suppression of both overconfidence and underconfidence. We also observe that relevance scores and confidence distributions vary systematically across different personalities. Based on the above findings, we incorporate personality-conditioned scores and confidence as features in a random forest classifier. This approach achieves performance that surpasses the best single-personality condition on a new dataset (TREC DL 2021), even with limited training data. These findings highlight that personality-derived confidence offers a complementary predictive signal, paving the way for more reliable and human-aligned LLM evaluators.

**Решение:** -4 симуляция черт личности Большой Пятерки для оценки релевантности поиска

---

### 415 · R10060

**DIALOGUE: A Generative AI-Based Pre-Post Simulation Study to Enhance Diagnostic Communication in Medical Students Through Virtual Type 2 Diabetes Scenarios.**

2025 · European journal of investigation in health, psychology and education · journal article, journalarticle, article · eng · https://doi.org/10.3390/ejihpe15080152

DIALOGUE (DIagnostic AI Learning through Objective Guided User Experience) is a generative artificial intelligence (GenAI)-based training program designed to enhance diagnostic communication skills in medical students. In this single-arm pre-post study, we evaluated whether DIALOGUE could improve students' ability to disclose a type 2 diabetes mellitus (T2DM) diagnosis with clarity, structure, and empathy. Thirty clinical-phase students completed two pre-test virtual encounters with an AI-simulated patient (ChatGPT, GPT-4o), scored by blinded raters using an eight-domain rubric. Participants then engaged in ten asynchronous GenAI scenarios with automated natural-language feedback. Seven days later, they completed two post-test consultations with human standardized patients, again evaluated with the same rubric. Mean total performance increased by 36.7 points (95% CI: 31.4-42.1; p < 0.001), and the proportion of high-performing students rose from 0% to 70%. Gains were significant across all domains, most notably in opening the encounter, closure, and diabetes specific explanation. Multiple regression showed that lower baseline empathy (β = -0.41, p = 0.005) and higher digital self-efficacy (β = 0.35, p = 0.016) independently predicted greater improvement; gender had only a marginal effect. Cluster analysis revealed three learner profiles, with the highest-gain group characterized by low empathy and high digital self-efficacy. Inter-rater reliability was excellent (ICC ≈ 0.90). These findings provide empirical evidence that GenAI-mediated training can meaningfully enhance diagnostic communication and may serve as a scalable, individualized adjunct to conventional medical education.

**Решение:** -4 обучение студентов-медиков навыкам сообщения диагноза сахарного диабета (DIALOGUE)

---

### 416 · R11840

**Assessing suicide risk in mood disorder patients: a GPT-3.5 language model approach**

2024 · Neuroscience Applied · journalarticle, article, journal-article · en · https://doi.org/10.1016/j.nsa.2024.105176

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T3 оценка суицидального риска у пациентов с расстройствами настроения через GPT-3.5, нет аннотации

---

### 417 · R12023

**Using GPT-4 for Text Analysis: Insights from English and German Language News Classification Tasks**

2024 · Alexandria (UniSG) (University of St.Gallen) · conference-paper · en · https://doi.org/10.36190/2024.31

Large language models are rapidly becoming an essential tool for social scientists. In particular, they have the potential to completely change the way researchers approach text analysis. In this study, we use the GPT-4 model to classify the content of newspaper articles and assess their sentiment. To do this, we collect headlines and leads from U.S. and German newspapers (n = 1,629) on how generative AI is represented in major news media outlets in both countries and inductively develop coding instructions based on this data. We then feed the data and instructions to GPT-4 and a human coder to compare their outputs and assess validity. We find that the coding procedure is highly reliable, with substantial to near perfect agreement between the human coder and GPT-4. We also find that reliability decreases for more complex constructs and is modestly lower for classification tasks performed in German than in English. Based on this analysis, we argue that LLMs offer powerful new approaches to text analysis that cross methodological divides between qualitative and quantitative approaches to empirical text analysis.

**Решение:** -4 политологический анализ текстов на английском и немецком с помощью GPT-4

---

### 418 · R7816

**Position: AI Competitions Provide the Gold Standard for Empirical Rigor in GenAI Evaluation**

2025 · International Conference on Machine Learning · journalarticle, conference, preprint/article · https://doi.org/10.48550/arxiv.2505.00612

In this position paper, we observe that empirical evaluation in Generative AI is at a crisis point since traditional ML evaluation and benchmarking strategies are insufficient to meet the needs of evaluating modern GenAI models and systems. There are many reasons for this, including the fact that these models typically have nearly unbounded input and output spaces, typically do not have a well defined ground truth target, and typically exhibit strong feedback loops and prediction dependence based on context of previous model outputs. On top of these critical issues, we argue that the problems of leakage and contamination are in fact the most important and difficult issues to address for GenAI evaluations. Interestingly, the field of AI Competitions has developed effective measures and practices to combat leakage for the purpose of counteracting cheating by bad actors within a competition setting. This makes AI Competitions an especially valuable (but underutilized) resource. Now is time for the field to view AI Competitions as the gold standard for empirical rigor in GenAI evaluation, and to harness and harvest their results with according value.

**Решение:** -1 позиционная статья о роли соревнований ИИ как стандарта эмпирической оценки

---

### 419 · R2855

**Safety and quality of public chatbots for lung cancer prognostic information: a comparative evaluation.**

2026 · Frontiers in public health · comparative study, research-article, journal article · eng · https://doi.org/10.3389/fpubh.2026.1935121

Objective To compare the safety, accuracy, empathy, reliability, information quality, and readability of five publicly accessible large language model chatbots when answering patient-facing lung cancer prognostic questions under standardized single-turn English prompting. Methods In this Chatbot Health Advice Reporting Transparency-guided cross-sectional evaluation, 53 standardized English prompts were submitted once to ChatGPT, Gemini, Copilot, DeepSeek, and Doubao through official web interfaces during April 1–21, 2026. Five blinded raters assessed 265 responses for safety, accuracy, empathy, DISCERN, EQIP, JAMA benchmark criteria, Global Quality Scale, and readability. Paired repeated-measures analyses were used. Results Inter-rater agreement was good to excellent. Safety differed significantly across models (Cochran’s Q = 14.089, df = 4, p = 0.007). Gemini generated the highest proportion of safe responses (48/53, 90.6%), whereas DeepSeek generated the lowest (33/53, 62.3%). The only adjusted pairwise safety difference that remained significant was Gemini versus DeepSeek (adjusted p = 0.023). Accuracy, empathy, reliability, information quality, and readability also differed significantly across models (all p < 0.001). Gemini showed the most favorable descriptive profile for safety, accuracy, empathy, and reliability, while Copilot produced the most readable responses. Conclusion Public-facing chatbots differed substantially in safety, reliability, communication quality, and readability. These findings are time-, interface-, and prompt-dependent. Chatbots may support general patient education but should not replace individualized clinician-led prognostic communication.

**Решение:** -4 безопасность и качество ответов чат-ботов о раке легких, соматическая онкология

---

### 420 · R0018

**ANALISIS KINERJA KOHERENSI NARATIF DAN FAITHFULNESS PADA SISTEM AGENTIC Al DAN LIGHTRAG UNTUK PEMBELAJARAN BERBASIS CERITA**

2026 · Repository at Universitas Pendidikan Indonesia (Universitas Pendidikan Indonesia) · dissertation · en

Pembelajaran berbasis cerita membantu penyampaian materi abstrak, tetapi generasi teks panjang menggunakan large language models (LLM) masih menghasilkan kesalahan faktual pada lebih dari 50 persen konten serta rentan terhadap inkoherensi naratif. Retrieval-augmented generation (RAG) memitigasi halusinasi, tetapi representasi data datar membatasi pemahaman antarkonsep. Untuk mengatasinya, LightRAG berbasis knowledge graph dan agentic AI yang memiliki kemampuan perencanaan, pemanfaatan alat, serta refleksi diri diintegrasikan. Penelitian ini mengevaluasi kinerja integrasi agentic AI dan LightRAG dalam menghasilkan cerita pembelajaran berdasarkan koherensi naratif dan faithfulness. Penelitian menggunakan design research methodology (DRM) empat tahap untuk merumuskan masalah hingga mengevaluasi sistem. Knowledge graph dibangun dari dataset WikiEval. Pengujian menggunakan 200 cerita yang terdiri atas 100 cerita dari baseline (Gemini 2.5 Flash) dan 100 keluaran agentic AI dalam bahasa Indonesia dan Inggris. Koherensi naratif dievaluasi menggunakan G-Eval, sedangkan faithfulness diukur dengan RAGAS dan FABLES melalui pendekatan LLM-as-a-judge yang divalidasi ahli. Hasil penelitian menunjukkan peningkatan skor koherensi naratif sebesar 11,0%, dari 4,122 pada sistem baseline ke 4,574 pada sistem agentic AI. Skor RAGAS meningkat sebesar 12,0%, dari 0,827 ke 0,926, sedangkan skor FABLES tidak menunjukkan perbedaan signifikan dengan skor 0,991 pada baseline dan 0,990 pada agentic AI. Rata-rata jumlah klaim per cerita berkurang 41,6%, dan proporsi klaim tanpa bukti tekstual turun dari 9,24% ke 2,96%. Hasil ini membuktikan bahwa pembagian peran kognitif dalam sistem agentic AI dan LightRAG efektif mengatasi keterbatasan LLM terhadap inkoherensi naratif dan halusinasi. ------------ Story-based learning aids in delivering abstract concepts, but long-text generation using large language models (LLMs) still produces factual errors in over 50 percent of content and remains prone to narrative incoherence. Retrieval-augmented generation (RAG) mitigates hallucinations, but flat data representation limits cross-conceptual understanding. To address this, a knowledge graph-based LightRAG and agentic AI, featuring planning, tool use, and self-reflection capabilities, are integrated. This study evaluates the performance of integrating agentic AI and LightRAG in generating educational stories based on narrative coherence and faithfulness. The study employs a four-stage design research methodology (DRM) from problem formulation to system evaluation. The knowledge graph is constructed from the WikiEval dataset. Testing utilizes 200 stories, comprising 100 stories from the baseline (Gemini 2.5 Flash) and 100 outputs from agentic AI in Indonesian and English. Narrative coherence is evaluated using G-Eval, while faithfulness is measured using RAGAS and FABLES via an expert-validated LLM-as-a-judge approach. The results show an 11.0% increase in narrative coherence score, from 4.122 in the baseline system to 4.574 in the agentic AI system. The RAGAS score increased by 12.0%, from 0.827 to 0.926, whereas the FABLES score showed no significant difference with scores of 0.991 in the baseline and 0.990 in agentic AI. The average number of claims per story decreased by 41.6%, and the proportion of claims without textual evidence dropped from 9.24% to 2.96%. These findings prove that cognitive role allocation within agentic AI and LightRAG systems effectively overcomes LLM limitations regarding narrative incoherence and hallucination.

**Решение:** -4 оценка связности нарратива в индонезийских учебных рассказах

---

### 421 · R12432

**Editorial: Can virtual reality be a solution for assessing and treating psychological symptoms caused by eating and weight disorders?**

2023 · Frontiers in Psychology · editorial · en · https://doi.org/10.3389/fpsyg.2023.1225454

Recent scientific literature suggests that incorporating Virtual Reality (VR) into psychological interventions for eating and weight disorders (EWD) has promising potential for addressing the root causes of these conditions beyond traditional weight control or weight recovery-focused strategies. For instance, VR may provide multisensory (e.g., visual, auditory, olfactory, and haptic cues) and extrinsic feedback, such as objective information regarding performance, or embodiment experiences. Thus, applying theory-driven choices in VR can contribute to increasing patients´ motivation and adherence to clinical treatments, and can support clinicians to personalize interventions. Moreover, VR is emerging as a promising tool for patients, as it can facilitate the promotion of healthy behaviors, reduce negative body image concerns, address the internalization of weight stigma, and offer them the opportunity to safely and effectively confront adverse stimuli in controlled environments (Al-Rasheed et al., 2022;Riva et al., 2020).One key question addressed in this research topic is whether the latest VR developments can be successfully implemented to enhance the efficacy of evidence-based psychological techniques for people living with EWD.Studies included in this Special Issue suggest that VR has the capacity to create immersive and experiential platforms for delivering interventions in a life-like and fully engaging manner, which could ultimately improve clinical effectiveness (Anastasiadou et al., 2023;Behrens et al., 2022;Döllinger et al., 2022;Harris et al., 2023;van der Waal et al., 2022). Harris et al. (2023) explored the effect of high levels of immersion and interactivity. Particularly, the authors analyzed the effects of VR food stimuli on participants´ cravings, by adding olfactory and interaction cues within the virtual environment. This study concluded that VR could be a useful tool for exposure treatments; in this case, food cravings increased through the use of VR.Additionally, immersive VR has the potential to enhance the understanding of the factors involved in EWD for both clinicians/researchers and patients. One important advantage is the ability to gather objective data on patients' eating behavior and emotional responses, providing valuable insights into the psychological mechanisms underlying obesity. For instance, Van der Waal et al. (2022) used visuotactile stimulation in VR to explore the complex interplay between emotions and body-size perceptions among healthy participants, providing insights into participants´ negative emotional responses toward avatars with obesity.VR technology also helps to incorporate immersive psychoeducational cues and participatory environments to empower people with EWD to better manage their condition. Furthermore, the integration of Cognitive-Behavioral Therapy (CBT) and Motivational Interviewing (MI) with VR exposure to challenging situations, which may be difficult to recreate in the real world, can enhance clinical interventions. For instance, VR allows participants to maintain self-conversations using embodiment and body-swapping techniques, as in the SOCRATES project (Anastasiadou et al., 2023). Such techniques consist on alternatively embodying two different avatars; one being the patient's look-alike avatar, and the other a virtual counsellor. This study shows that incorporating VR-driven body-swapping with MI can promote healthier lifestyles among patients with obesity (Anastasiadou et al., 2023). Another advantage of using VR in the treatment of EWD is the ability to address body image disturbances by allowing individuals to embody visually altered virtual bodies. Döllinger et al. ( 2022) developed a VR prototype system that employs personalized avatars with photorealistic features, which can be modulated in real-time. Such a system may enable people with obesity to engage in virtual scenarios that simulate real-world challenges related to body image concerns (Döllinger et al., 2022). Hence, exposure to virtual situations can provide a safe and effective way to address negative feelings about body image, a critical factor in overweight and obesity. This approach can lead to improved body image acceptance and body awareness, thus helping individuals with EWD to develop new, healthier habits and attitudes (Ferrer-García & Gutiérrez-Maldonado, 2012).Moreover, VR-based interventions offer the possibility to enhance engagement in treatment by providing a unique and impactful therapeutic experience. However, it is necessary to consider various factors influencing the user experience, such as familiarity with VR, individual characteristics like age and gender, and also, specific technological design and technical features, such as the quality of graphics and audio in the VR environment. Besides, by tailoring VR interventions to meet the specific needs and preferences of the target audience, researchers and designers can improve their effectiveness and implementation. Understanding all these factors is essential for optimising the design and effectiveness of VR interventions for treating EWD in clinical practice (Behrens et al., 2022).Recent progress in generative Artificial Intelligence, and specifically breakthroughs with large language models (Brown et al., 2020), are also likely to facilitate further research and application in the development of VR systems as therapeutic tools to address EWD. First, the generation of VR scenarios, including personalized scenarios, is likely to become easier and cheaper due to automated generation of technical code and content (Pollak et al., 2023). Additionally, offline analysis of psychological textual content, such as MI transcripts, has become feasible (Wu et al., 2023). Finally, it is becoming easier to integrate intelligent virtual humans in psychological VR applications (Nakash et al., 2022), and these virtual humans are becoming increasingly sophisticated and competent in their dialogue capabiliti

**Решение:** -1 редакционная статья о применении виртуальной реальности в психологических вмешательствах

---

### 422 · R9743

**Evaluating the Reliability of Pragmatic Annotation Guidelines for Ritualized Expressions in Spanish through Corpus and Ontology-Based Analysis**

2025 · Zenodo · text/presentation · https://doi.org/10.5281/zenodo.15582624

This study addresses the theoretical and methodological challenges of identifying and classifying ritualized expressions in Spanish, specifically greetings, farewells, vocatives, exclamatives, and politeness formulas, by developing and applying a dedicated annotation framework. Its principal aim is to evaluate the reliability of a set of annotation guidelines based on an Ontology of Ritualized Expression (REO), applied to a corpus derived from Spanish-language multimedia content. The study adopts an interdisciplinary approach, drawing on phraseology, pragmatics, discourse analysis, and applied linguistics, with a particular focus on Spanish as a Foreign Language (ELE). Ritualized expressions, or pragmatemes, are conventionalized linguistic units whose meaning largely depends on the communicative situation (SIT) in which they occur. Although such expressions have received considerable attention in lexicographic and theoretical literature, their pedagogical integration in ELE textbooks remains inconsistent. In many CEFR-aligned ELE manuals, these expressions are inadequately described or contextualized. Sociopragmatic variables—such as diatopic variation, deixis, register, and situational appropriateness—are often underrepresented or insufficiently addressed in instructional content. This research builds on recent developments in phraseology and pragmatics, including studies on affective pragmatemes, typology of diatopic variation, and foundational models from the explanatory-combinatorial framework. Previous corpus-based investigations, particularly those involving the analysis of audiovisual dialogues and ELE instructional texts, serve as important references. The study comprises three integrated phases: 1. Corpus selection and annotation: A working corpus was compiled using three Spanish-language films in their original version (VOE), using both subtitles and their corresponding audiovisual scenes. These materials provided naturally occurring instances of ritualized expressions in discourse. Selected segments were chosen for their rich pragmatic content. 2. Ontology-based annotation: The Ritualized Expressions Ontology classifies ritualized expressions into five main categories: greetings and farewells, vocatives, exclamatives, politeness formulas, and profanities. Each category is further subdivided according to situational, formal, and functional parameters. Expressions were annotated using a labeling system that facilitated nuanced classification by contextual appropriateness, degree of ritualization, and interactional function. 3. Validation and reliability testing: A pilot annotation study designed to assess the robustness of the guidelines and inter-annotator consistency was carried out. Six annotators participated: Five human annotators, representing a diversity of linguistic backgrounds; three Spanish native speakers, serving as a baseline, one Portuguese and one Spanish speaker, with specialized lexicographic knowledge, and the generative AI model ChatGPT 4.5. Human annotators received printed excerpts from the three selected film subtitles and were given access to the corresponding audiovisual scenes. They manually annotated instances of ritualized expressions according to the REO guidelines. The subtitles and the annotation guidelines were also submitted to a customized version of ChatGPT 4.5 (OpenAI, 2025) for evaluation and comparison. Upon completion, an extensive cross-comparison was carried out, measuring the reliability index of annotations through pairwise comparisons among all annotators (human-human, human-AI, and AI-human). These comparisons constitute the primary dataset for assessing guideline’s reliability. The findings underscore the importance of rigorously defining and operationalizing the communicative situation (SIT), particularly in pedagogical materials. The REO framework offers a structured yet adaptable framework, able to account for variation across multiple dimensions: medium (oral vs. written), dialect, formality, emotional register, and frequency. Lemmatization techniques were also applied to standardize surface forms and enhance annotation consistency. From a didactic standpoint, this research highlights the urgent need for ELE textbooks to adopt more context-sensitive approaches to teaching ritualized expressions. Incorporating pragmatic features—such as emotional register, speaker hierarchy, social distance, and appropriate first responses—can significantly improve learners’ interpretative and expressive skills. Moreover, this research contributes to computational pragmatics by evaluating how LLMs can support annotation tasks while also revealing their limitations in handling situational nuance. Comparative reliability data involving human annotators and AI models highlight the promise and the current shortcomings of such tools in linguistic research. In conclusion, this study establishes a methodological foundation for evaluating annotation guidelines in discourse pragmatics and proposes a scalable, ontology-based framework for building annotated corpora centered on ritualized expressions. It opens new avenues for cross-linguistic and cross-register pragmatic studies and suggests practical applications in ELE curriculum design, lexicography, and AI-driven language technologies.

**Решение:** -4 оценка надежности руководств по лингвистической прагматической разметке

---

### 423 · R6638

**SCRum-9: Multilingual Stance Classification over Rumours on Social Media**

2026 · Proceedings of the International AAAI Conference on Web and Social Media · journalarticle, conference, preprint/article · en · https://doi.org/10.1609/icwsm.v20i1.42707

We introduce SCRum-9, the largest multilingual Stance Classification dataset for Rumour analysis in 9 languages, containing 7,516 tweets from X. SCRum-9 goes beyond existing stance classification datasets by covering more languages, linking examples to more fact-checked claims (2.1k), and including confidence-related annotations from multiple annotators to account for intra- and inter-annotator variability. Annotations were made by at least two native speakers per language, totalling more than 405 hours of annotation and 8,150 dollars in compensation. Further, SCRum-9 is used to benchmark five large language models (LLMs) and two multilingual masked language models (MLMs) in In-Context Learning (ICL) and fine-tuning setups. This paper also innovates by exploring the use of multilingual synthetic data for rumour stance classification, showing that even LLMs with weak ICL performance can produce valuable synthetic data for fine-tuning small MLMs, enabling them to achieve higher performance than zero-shot ICL in LLMs. Finally, we examine the relationship between model predictions and human uncertainty on ambiguous cases finding that model predictions often match the second-choice labels assigned by annotators, rather than diverging entirely from human judgments. SCRum-9 is publicly released to the research community with potential to foster further research on multilingual analysis of misleading narratives on social media. Accepted by ICWSM 2026

**Решение:** -4 классификация позиции в слухах и дезинформации (SCRum-9)

---

### 424 · R3043

**Benchmarking LLM-as-a-Judge Models for 5W1H Extraction Evaluation**

2026 · Electronics · journalarticle, article, journal-article · en · https://doi.org/10.3390/electronics15030659

Evaluating 5W1H (Who, What, When, Where, Why, and How) information extraction systems remains challenging, as traditional information retrieval metrics like ROUGE and BLEU fail to capture semantic accuracy and narrative coherence. The LLM-as-a-Judge paradigm offers a promising alternative, yet systematic comparisons of judge models for this task are lacking. This study benchmarks multiple large language models, including state-of-the-art models such as GPT, Claude, and Gemini as evaluators of 5W1H extractions from Spanish news articles. We assess judge performance across six quality criteria: Factual Accuracy, Completeness, Relevance and Conciseness, Clarity and Readability, Faithfulness to Source, and Overall Coherence. Our analysis examines inter-judge agreement, score distribution patterns, criterion-level variance, and the relationship between evaluation quality and computational cost. Using two Spanish-language corpora (BASSE and FLARES), we identify which criteria exhibit consistent cross-model agreement and which prove most sensitive to judge selection. The main contribution of this work is providing the first systematic benchmark of LLM-as-a-Judge models for 5W1H extraction evaluation in Spanish, validated against expert journalistic judgment. Results reveal that all evaluated models achieve alignment levels above 90% across all metrics. Specifically, Claude Sonnet 4.5 emerges as the most accurate evaluator with a Global Judgment Acceptance Rate (JAR) of 99.79%. Furthermore, meta-evaluation with human experts demonstrates a substantial inter-annotator agreement of &kappa;=0.6739. Finally, we provide recommendations for judge model selection based on task requirements and resource constraints, contributing practical guidance for researchers implementing LLM-based evaluation pipelines for information extraction tasks

**Решение:** -4 бенчмарк LLM-судей для извлечения информации 5W1H в NLP

---

### 425 · R6172

**A Three-Level Audit of LLM Alignment for Argument Quality Assessment**

2026 · conference-paper · https://doi.org/10.18653/v1/2026.argmining-1.3

Large Language Models (LLMs) are increasingly used as automated evaluators of argument quality.However, existing studies typically assess models only through their agreement with human scores, leaving the reasoning process behind these judgments unexplored.In this paper, we propose a three-level audit framework for evaluating the reliability of LLM-based argument quality assessment.The framework distinguishes between (1) surface alignment, measuring agreement between LLM-predicted scores and human annotations; (2) instructional alignment, assessing whether generated rationales adhere to the intended evaluation criteria; and (3) faithfulness alignment, examining whether predicted scores are supported by the generated rationales.To operationalize this audit, we introduce structural rationale prompting, 1 which guides LLMs to generate structured justifications before assigning scores across 11 dimensions of the Dagstuhl-15512 argument quality corpus.We evaluate several LLMs under this framework and find that structural rationale prompting substantially improves agreement with human annotations compared to definition-based prompting.Furthermore, the generated rationales generally follow the evaluation instructions and remain highly consistent with the predicted scores.Overall, our results suggest that auditing LLM evaluators beyond surface score agreement provides deeper insight into the reliability and transparency of LLM-based argument quality assessment. Quality Dimension Definition CogencyLocal acceptability Premises worthy of being believed. Local relevance Premises accept/reject conclusion. Local sufficiencyPremises enough to draw conclusion. Effectiveness Credibility Makes author worthy of credence. Emotion appealMakes audience open to arguments.Clarity Uses correct, unambiguous language and avoids deviation from the issue.Appropriateness Language supports credibility and emotions, in proportion to the issue.Arrangement Argues in the right order. ReasonablenessGlobal acceptability Audience accepts use of argument. Global relevance Argument helps arrive at conclusion. Global sufficiencyEnough rebuts counterarguments.

**Решение:** -4 аудит качества аргументации в дебатах с помощью LLM-судей

---

### 426 · R2576

**Artificial Intelligence-Driven Clinical Decision Support Systems for Emergency Department Triage and Acute Care Prioritization: A Systematic Review of Accuracy, Safety, and Implementation Readiness**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/c85fw

## Description ### Background and Rationale Emergency department (ED) triage is a critical component of emergency healthcare delivery, ensuring the timely identification and prioritization of patients according to clinical urgency. Conventional triage systems, including the Emergency Severity Index (ESI), Manchester Triage System (MTS), Canadian Triage and Acuity Scale (CTAS), and Korean Triage and Acuity Scale (KTAS), provide standardized approaches to patient prioritization. However, their effectiveness may be influenced by clinical workload, variability in healthcare professionals' experience, incomplete patient information, and inter-rater disagreement. Artificial intelligence (AI), particularly machine learning (ML), deep learning (DL), natural language processing (NLP), and large language models (LLMs), has emerged as a promising approach to improving emergency triage accuracy, predicting clinical deterioration, and optimizing healthcare resource allocation. Nevertheless, concerns remain regarding under-triage, over-triage, algorithmic bias, generalizability, patient safety, and readiness for real-world clinical implementation. ### Purpose and Objectives This systematic review aims to critically evaluate the accuracy, safety, and implementation readiness of AI-driven clinical decision support systems used in emergency department triage and acute care prioritization. The specific objectives are to: 1. Evaluate the diagnostic and predictive performance of AI-based systems in emergency triage and acute care prioritization. 2. Compare AI-driven triage performance with conventional triage systems and healthcare professionals. 3. Assess the ability of AI models to predict critical illness, hospitalization, intensive care unit admission, and mortality. 4. Examine patient safety outcomes, particularly under-triage, over-triage, mis-triage, and classification errors. 5. Evaluate external validation, prospective clinical testing, workflow integration, transparency, and implementation readiness. 6. Identify methodological limitations, evidence gaps, and priorities for future clinical research. ### Methods and Study Design This research is a systematic review conducted and reported according to the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA 2020) framework. A comprehensive literature search was undertaken using PubMed/MEDLINE, PubMed Central, Embase, Scopus, Web of Science, and the Cochrane Library. Additional studies were identified through citation tracking, reference-list screening, and examination of relevant systematic reviews. Eligible studies included randomized investigations, prospective and retrospective observational studies, diagnostic and predictive modeling studies, and comparative evaluations examining AI-assisted emergency department triage. Data extraction focused on study characteristics, patient populations, AI architecture, conventional comparators, performance measures, validation approaches, safety outcomes, and clinical implementation considerations. Risk of bias was evaluated using methodological criteria appropriate to individual study designs, informed by Cochrane RoB 2 and ROBINS-I principles. Certainty of evidence was considered using GRADE principles. The search identified 1,076 records, of which 312 duplicates were removed. Following screening and eligibility assessment, 14 studies were included in the final qualitative synthesis. Because of substantial heterogeneity in study populations, AI architectures, triage systems, reference standards, and outcome measurements, a quantitative meta-analysis was not performed. Findings were synthesized narratively, informed by Synthesis Without Meta-analysis (SWiM) principles. ### Outcomes of Interest The primary outcomes included triage classification accuracy, area under the receiver operating characteristic curve (AUROC), sensitivity, specificity, F1 score, agreement with expert reference standards, and prediction of critical illness, hospitalization, intensive care admission, and mortality. Safety outcomes included under-triage, over-triage, mis-triage, and performance in high-acuity patient groups. Secondary outcomes included clinical workflow integration, external validation, explainability, reproducibility, algorithmic fairness, and readiness for implementation in routine emergency care. ### Expected Outcomes and Significance The review was designed to determine whether AI-driven clinical decision support systems improve emergency triage performance compared with conventional approaches and whether existing evidence supports their safe clinical implementation. The anticipated contribution is a comprehensive synthesis of the technical performance and practical limitations of AI-based triage tools, distinguishing predictive accuracy from demonstrated improvements in patient safety and clinical outcomes. Based on the completed narrative synthesis, AI-based systems demonstrated promising performance in predicting critical illness, hospitalization, intensive care admission, mortality, and direct triage classification. However, clinical safety outcomes, prospective validation, subgroup performance, and workflow effects were inconsistently assessed across studies. The review is expected to inform emergency physicians, healthcare administrators, clinical researchers, and policymakers regarding the potential benefits, limitations, and governance requirements associated with AI-supported triage. The findings emphasize the importance of multicenter prospective validation, standardized safety metrics, transparent reporting, clinician oversight, algorithm monitoring, and robust implementation frameworks before widespread autonomous deployment. ### Registration Status This systematic review is being registered retrospectively on the Open Science Framework because study selection, data extraction, and evidence synthesis had commenced before registration. The registration documents the review objectives

**Решение:** -1 систематический обзор ИИ в медицинской сортировке (триаже) пациентов скорой помощи

---

### 427 · R7633

**Assessing Burnout Dynamics Through Weibo: The Spatial-temporal Heterogeneity of Environmental and Economic Factors in Shanghai Pre and Post-Lockdown**

2025 · University of Chicago · text/thesis · https://doi.org/10.6082/sbysg-5qh75

This study explores the influence of integrating macro-built environment data, micro-level subjective and objective street environment perceptions, socioeconomic demographics of residents' burnout emotions and their spatial-temporal heterogeneity, with a particular focus on the changing patterns across three phases of Shanghai's pandemic lockdown. The research establishes a pipeline based on large language models to extract burnout emotions from social media content, and constructs a multi-dimensional spatial-temporal analytical framework integrating OLS, geographically weighted regression, and nonlinear interpretable machine learning modeling techniques. By collecting social media data, the study first validates the effectiveness of large language models in identifying burnout emotions from social media (with a consistency coefficient of 0.61 with human ratings), providing a scalable method for real-time psychological monitoring during crises. Analysis using spatial analysis reveals significant spatial clustering patterns of burnout emotions among Shanghai residents. Geographically weighted regression identifies five typical spatial patterns of influencing factors. Walkability consistently protected against burnout citywide, while green spaces lost restorative function in commercial centers. High-density housing areas with complex visual environments amplified psychological distress, and central districts formed "youth burnout peaks" where young, educated populations concentrated. Longitudinal results reveals significant nonlinear relationships and critical threshold effects between influencing factors and residents' burnout emotions, with these relationship patterns exhibiting various forms of transformation across the three phases. For example, population density's impact on burnout shifted from a negative correlation and "Reverse Excitement" pattern before lockdown to a "Basic Need" pattern during lockdown. Similarly, the young population ratio evolved from a single-threshold model with positive correlation ("Semi-Performance") to negative correlation during and after lockdown ("Performance" to "Excitement") with complex multi-threshold interval models. Green space transformed from weak positive correlation as an "Excitement Factor" before lockdown to strong positive correlation as a "Performance Factor" during lockdown, indicating that visually accessible but functionally inaccessible green spaces became sources of stress. Visual complexity reversed from positive correlation ("Basic Need") before lockdown to negative correlation ("Excitement Factor") highlighting how environmental monotony enhanced the value of perceptual stimulation. These findings challenge static urban health standards, suggesting environmental influences operate through dynamic systems that transform during crises, providing frameworks for resilient urban planning integrating spatial structure with psychological wellbeing. Yuxuan Cai was nominated for the 2025 MACSS Outstanding Thesis Award.

**Решение:** + T1/T3 выявление эмоций эмоционального выгорания в Weibo: LLM против оценок людей, согласованность 0.61

---

### 428 · R2660

**Artificial Intelligence-Associated Psychotic Experiences ("AI Psychosis"): A Scoping Review of Definitions, Proposed Mechanisms, Vulnerability Factors, and Clinical-Preventive Frameworks**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/eqdm6

Reports of psychotic experiences emerging or intensifying in the context of sustained interaction with generative AI chatbots have proliferated since 2023 under the contested label "AI psychosis." Public interest peaked around August 2025, and the academic literature has grown rapidly but remains fragmented across case reports, one cross-sectional study, simulation/benchmark studies, theoretical and conceptual papers, and critiques questioning the term itself; these sources use divergent definitions, units of analysis, and competing conceptualizations, which hinders cumulative knowledge. An existing rapid scoping review maps mass-media narratives only; no scoping review has yet mapped the academic literature itself. This scoping review, conducted per JBI methodology and reported per PRISMA-ScR, addresses four questions: how the phenomenon is defined and which alternative conceptualizations are proposed (RQ1); which mechanisms are proposed to underlie it (RQ2); which vulnerability and risk factors are reported or hypothesized (RQ3); and which clinical, design-level, policy, and psychoeducational responses are recommended (RQ4), with particular attention to implications for guidance and psychological counseling. A cross-cutting focus addresses the nature and quality of the evidence base. Web of Science and Scopus were searched (November 2022 to July 2026); of 183 records (123 after deduplication), two independent reviewers retained 22 studies for synthesis (inter-rater agreement 95.1%; Cohen's κ = .845). Expected outcomes include a map of the field's three competing terminological stances, a layered account of proposed mechanisms centered on sycophancy, a four-tier characterization of risk factors, a synthesis of recommended responses, and a critical appraisal of the evidence base as an early, largely non-empirical literature. The review aims to inform clinical assessment, AI safety design, and school- and university-based psychoeducation, and to identify priorities for future empirical and psychometric work.

**Решение:** -1 scoping-обзор академической литературы по феномену «ИИ-психоза»

---

### 429 · R4895

**Asuntouutisoinnin sentimentin kriittinen kerrosanalyysi koneoppimisen ja agenttipohjaisen tekoälyn avulla: Moniagenttijärjestelmään perustuva lähestymistapa Suomen asuntomarkkinoihin**

2026 · Aaltodoc (Aalto University) · dissertation · en · https://aaltodoc.aalto.fi/bitstreams/fe403afd-8b8f-4d35-b393-7a5a6b216642/download

This study explores Finnish housing related news discourse and prices in Statistics Finland's index series. The literature review investigates macrofinancial fundamentals and the narratives dominating media. Discursive patterns and the futures-oriented interpretation of housing market discourse are considered from additional perspectives, e.g., megatrends, geopolitics, weak signals, dragon kings, and the psychology of bubbles. The focus then shifts to financialisation, the voices of the primary definers, media discourse, media as a filter, and Finnish media pluralism. The research found a gap: there was no indexed study in Google Scholar or Scopus at the time of writing combining corpus-scale sentiment analysis with causal layered analysis (CLA) in a housing or real estate market context. To fill this gap, a comprehensive raw corpus of news headlines was scraped with 46 Boolean keywords from the national public broadcaster Yle's 1 031 013 news articles between 2006 and 2025. The author used artificial intelligence (AI) tools and large language models (LLMs) to isolate housing news sentiment, gating 697 679 news headlines to 30 460 relevant articles and, at the last stage, to a labelled corpus of 8 180. This thesis proves with inter-rater reliability (IRR) checks that LLMs can label news sentiment adequately. The author vs Mistral LLM IRR check returned a very convincing quadratic-weighted Cohen's kappa of 0.665, author vs advisor of 0.697, and yearly bin Pearson r of 0.870. CLA: "litany; systemic; worldview; myth and metaphor" were layered in a multi-agent system (MAS) panel, creating a holistic picture: home ideology, the two-dwelling trap, "buy now" and "postponed recovery" genres, which made sentiment fluctuate. "Cut your losses" is missing from the media discourse, as are megatrends: climate change and biodiversity loss as drivers of prices. Weaponising oil and gas against the EU, and Russia and the US attacking democracy are dragon king events. Extreme yet retrospectively foreseeable through weak signals, they may have had the greatest influence on old dwelling prices in Finland between 2022 and 2025.

**Решение:** -4 анализ тональности новостей о недвижимости в Финляндии

---

### 430 · R4857

**RECIPROCAL HUMAN-AI LEARNING IN CROWDSOURCED DESIGN: ALGORITHM AVERSION, TACIT KNOWLEDGE, AND ETHICAL TRANSPARENCY**

2026 · Journal of Creative Arts · journalarticle, article · en · https://doi.org/10.24191/jca.v3i1.11084

The fast integration of generative artificial intelligence in digital design has altered the use of AI systems from an automated tool to a partner. With this change, there is limited empirical research that can explain how adaptive human-AI interaction can lead to a better creative outcome, especially in crowdsourced design settings. This paper explores how reciprocal human-AI learning (RHML) influences creative synergy and considers the mediating and moderating roles of ethics, transparency, and algorithm aversion, respectively. A 2 x 2 factorial controlled experiment was carried out with 320 subjects with design backgrounds who completed an AI-assisted creative task under a simulated crowdsourced design condition. Expert raters assessed creative, productive outputs, and validated questionnaires assessed psychological constructs. The analysis was done using the factorial ANOVA and moderated mediation analysis with PROCESS. The findings reveal that RHML has a great effect on enhancing creative synergy (F(1,316) = 28.74, p < .001). RHML also decreases aversion to algorithms, which partly mediates its beneficial influence on the results of creativity. Moreover, ethical disclosure puts a lot of force in the correlation between RHML and creative synergy (interaction F(1,316) = 12.63, p < .001). The results prove that successful human-AI cooperation in creative systems is based not only on technological ability but also on psychological acceptance and clear governance mechanisms. The research paper provides empirical support to the study of hybrid intelligence and has design implications in the use of AI-assisted creative platforms.

**Решение:** -4 совместное обучение человека и ИИ в краудсорсинговом дизайне

---

### 431 · R2314

**Graph Representation-Based Model Poisoning on the Heterogeneous Internet of Agents**

2026 · International Wireless Communications and Mobile Computing Conference (IWCMC) · journalarticle, other/conference object, preprint/article · en · https://doi.org/10.1109/iwcmc69287.2026.11579822

Internet of Agents (IoA) envisions a unified, agent-centric paradigm where heterogeneous large language model (LLM) agents can interconnect and collaborate at scale. Within this paradigm, federated fine-tuning (FFT) serves as a key enabler that allows distributed LLM agents to co-train an intelligent global LLM without centralizing local datasets. However, the FFT-enabled IoA systems remain vulnerable to model poisoning attacks, where adversaries can upload malicious updates to the server to degrade the performance of the aggregated global LLM. This paper proposes a graph representation-based model poisoning (GRMP) attack, which exploits overheard benign updates to construct a feature correlation graph and employs a variational graph autoencoder to capture structural dependencies and generate malicious updates. A novel attack algorithm is developed based on augmented Lagrangian and subgradient descent methods to optimize malicious updates that preserve benign-like statistics while embedding adversarial objectives. Experimental results show that the proposed GRMP attack can substantially decrease accuracy across different LLM models while remaining statistically consistent with benign updates, thereby evading detection by existing defense mechanisms and underscoring a severe threat to the ambitious IoA paradigm. This paper has been accepted by the IEEE 22nd International Wireless Communications &amp; Mobile Computing Conference (IWCMC 2026, Shanghai, China)

**Решение:** -4 атаки отравления моделей в многоагентных интернет-системах, кибербезопасность

---

### 432 · R0491

**Benchmarking Large Language Model Performance in Generating and Assessing Radiology Objective Structured Clinical Examination**

2026 · Radiology Advances · journalarticle, review, article · en · https://doi.org/10.1093/radadv/umag039

Abstract Background High-quality radiology assessment questions are essential for education competency evaluation but labor-intensive to create. Purpose To compare four large language models (LLMs) in generating and evaluating radiology objective structured clinical examination (OSCE)–style questions and responses. Materials and Methods Fifty Radiopaedia cases across 10 subspecialties were used to generate 200 radiology OSCE-style sessions (three questions per session) using four LLMs: GPT-4o (4O), Llama 3-70b (LM), Claude 3.5 Sonnet (CL), and Gemini 1.5 Flash (GM). Three expert radiologists blindly evaluated sessions for clarity, clinical relevance, difficulty, option accuracy, assessment accuracy, and feedback quality on 5-point Likert scale. Generalized estimating equations (GEE) compared model performance, accounting for rater correlation. The primary accuracy metric was Top Two Box Accuracy (2TBA; all raters ≥4); secondary metrics included Top Box Accuracy (TBA), Average Score ≥4 Accuracy (AS4A), and Perfect 5 Accuracy (P5A; all raters = 5). Final rankings were determined via Borda count. Results Inter-rater reliability ranged from fair to good agreement (Gwet's AC2: 0.39–0.73). GEE analysis showed significant performance variations (p < 0.05) across metrics. Final Borda scores: 4O (18.5), LM (13.5), CL (11.0), GM (7.0). TBA was high (70.7–100%). For the primary metric 2TBA, 4O showed significantly higher odds of achieving high-quality scores vs. GM for clarity (odds ratio [OR] 4.52, p < 0.001) and overall assessment accuracy (OR 3.78, p < 0.001). Under the strictest threshold (P5A), 4O led in composite Question General Accuracy (52.7% vs. 32.7% LM, 21.3% CL, 1.3% GM). Qualitative failure modes included distractor ambiguity, conceptual repetition, and information leakage. Conclusion This study provides a benchmark of LLM performance for radiology OSCE-style content generation and evaluation during a specific snapshot of artificial intelligence development (August 2024). 4O demonstrated the highest relative performance, though none consistently achieved expert-level quality. While LLMs can augment radiology education, expert review remains mandatory for high-stakes assessment.

**Решение:** -4 генерация тестовых вопросов по радиологии, медицинское образование

---

### 433 · R3877

**Can AI Effectively Predict Human Judgments of Group Cohesion?**

2026 · Proceedings of the 2026 International Conference on Information Technology for Social Good · book, conference, conference-paper · https://doi.org/10.1145/3794786.3830779

Group cohesion is a widely studied concept in social psychology that primarily reflects the level of unity and collaboration within a group. Prior studies have explored deep learning models to predict cohesion from multimodal signals, while advances in large language models (LLMs) have introduced new opportunities for assessing cohesion. However, due to the complexity of social cues and the subjectivity of human perception, whether these AI-based methods can reliably replicate human judgments of group cohesion - and how their capabilities differ - remains an open question. In this paper, we investigate this problem using the Group Cohesion and Emotion (GCE) dataset, comparing two approaches: a multimodal deep learning model leveraging audio and visual features, and an LLM-based approach that predicts cohesion from structured summaries derived from the same features. The results indicate that neither model is capable of perfectly replicating human-assigned cohesion scores. However, the deep learning model demonstrates superior performance in predicting the exact numerical scores, whereas the LLM exhibits stronger performance in the discretized classification task, where cohesion scores are categorized into three ordinal levels: low, medium, and high. These findings highlight the complementary strengths of deep learning and LLMs in understanding psychological constructs, clarifying their respective capabilities and limitations as tools for automated cohesion assessment.

**Решение:** ? оценка групповой сплоченности в социальной психологии: LLM против оценок людей; проверить модальность

---

### 434 · R11339

**Harnessing LLMs for Automated Video Content Analysis: An Exploratory Workflow of Short Videos on Depression**

2024 · ACM Conference on Computer-Supported Cooperative Work and Social Computing (CSCW) · journalarticle, book, text/article · en · https://doi.org/10.1145/3678884.3681850

Despite the growing interest in leveraging Large Language Models (LLMs) for content analysis, current studies have primarily focused on text-based content. In the present work, we explored the potential of LLMs in assisting video content analysis by conducting a case study that followed a new workflow of LLM-assisted multimodal content analysis. The workflow encompasses codebook design, prompt engineering, LLM processing, and human evaluation. We strategically crafted annotation prompts to get LLM Annotations in structured form and explanation prompts to generate LLM Explanations for a better understanding of LLM reasoning and transparency. To test LLM's video annotation capabilities, we analyzed 203 keyframes extracted from 25 YouTube short videos about depression. We compared the LLM Annotations with those of two human coders and found that LLM has higher accuracy in object and activity Annotations than emotion and genre Annotations. Moreover, we identified the potential and limitations of LLM's capabilities in annotating videos. Based on the findings, we explore opportunities and challenges for future research and improvements to the workflow. We also discuss ethical concerns surrounding future studies based on LLM-assisted video analysis. 7 pages, 2 figures, accepted by CSCW 24

**Решение:** -4 автоматизированный контент-анализ видео с помощью LLM

---

### 435 · R12572

**FedMLSecurity: A Benchmark for Attacks and Defenses in Federated Learning and Federated LLMs**

2023

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 бенчмарк атак и защит в федеративном обучении (FedMLSecurity), нет аннотации

---

### 436 · R11471

**1.69 Can Artificial Intelligence Assess Suicide Risk in Youth?: Comparing ChatGPT-3.5, ChatGPT-4, and ChatGPT-4o to Psychiatrists**

2024 · Journal of the American Academy of Child & Adolescent Psychiatry · journalarticle, article · en · https://doi.org/10.1016/j.jaac.2024.08.089

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T3 оценка суицидального риска у молодежи с помощью искусственного интеллекта, нет аннотации

---

### 437 · R12764

**Journal Digest: Amygdala and ‘Broken Heart’ Syndrome; Digital Intervention and Paranoia Symptoms; Snoring in Children and Brain Development; Impaired Self-Control and Binge Eating Behavior; HS Football and Midlife Mental Health Problems**

2021 · Psychiatric News · article · en · https://doi.org/10.1176/appi.pn.2021.6.3

Back to table of contents Previous article Next article Journal DigestFull AccessJournal Digest: Amygdala and 'Broken Heart' Syndrome; Digital Intervention and Paranoia Symptoms; Snoring in Children and Brain Development; Impaired Self-Control and Binge Eating Behavior; HS Football and Midlife Mental Health ProblemsNick ZagorskiNick ZagorskiPublished Online:28 May 2021https://doi.org/10.1176/appi.pn.2021.6.3Amygdala Activity May Be Biomarker for 'Broken Heart' SyndromeiStock/Alexandra DraghiciPeople who develop Takotsubo syndrome (TTS) —a stress-triggered form of heart failure commonly known as "broken heart syndrome"—show elevated amygdala activity in years prior to the onset of disease, a study in European Heart Journal has found. The amygdala is part of the brain's limbic system and a key regulator of the stress response and heart function.Researchers at Massachusetts General Hospital and colleagues examined PET scans from 41 adults who subsequently developed TTS (TTS was diagnosed between one month and four years after the scan) and 63 adults with similar demographics who did not develop TTS. The scans showed that on average individuals who developed TTS had significantly higher activity in the amygdala than people without TTS. After adjusting for other TTS risk factors, including smoking and a history of depression, the researchers found that elevated amygdala activity was associated with a 64% increased risk of future TTS.The researchers also found that among individuals who did develop TTS, those with the highest amygdala activity developed symptoms about two years earlier on average than those with lower amygdala activity."These study findings suggest that increased [amygdala activity] predates the development of TTS and may effectively prime the limbic system to respond more vigorously to acute stressors, thus increasing TTS risk," the researchers wrote. "That higher relative [amygdala activity] associates with earlier TTS development suggests that those with the highest [amygdala activity] are relatively more prone to develop TTS upon stress exposure and may develop the syndrome sooner."Radfar A, Abohashem S, Osborne MT, et al. Stress-Associated Neurobiological Activity Associates With the Risk for and Timing of Subsequent Takotsubo Syndrome. Eur Heart J. March 26, 2021. Online ahead of print.Digital Intervention Found to Reduce Paranoia SymptomsiStock/Wiphop SathawirawongA digital intervention that combines virtual psychotherapy and an interactive mobile app appears to reduce some symptoms of paranoia better than usual care, according to a study in JAMA Psychiatry. In particular, the blended digital therapy known as SlowMo was effective at reducing persecution-related delusions in adults with schizophrenia.The study involved 361 adults aged 18 and older who had been diagnosed with schizophrenia and persistent and distressing paranoia, as assessed by the Schedules for Clinical Assessment in Neuropsychiatry and Green et al Paranoid Thoughts Scale (GPTS). All of the participants in the trial received usual care (typically involving antipsychotics and outpatient visits); 181 also received access to SlowMo.The SlowMo therapy consists of eight online cognitive-behavioral therapy sessions (given over 12 weeks) that are augmented with a mobile app that includes such features as animated vignettes, games, and personalized thought bubbles. Paranoia and other behavioral symptoms were assessed at the end of the 12-week study and at the 24-week follow-up.The participants who received SlowMo showed greater improvements in their GPTS scores after 12 weeks compared with those receiving only usual care, though there were no longer differences between the groups at 24 weeks. Among secondary measures, the SlowMo group reported fewer persecutory delusions, a greater belief flexibility (admitting one's beliefs might be mistaken), and improved well-being at both 12 and 24 weeks compared with those in the usual care group."The results indicate that the treatment was effective, in part, through helping people to slow down their thinking and to worry less," wrote the investigators from King's College London and colleagues. "Further understanding of the mechanisms of action of SlowMo is warranted." Garety P, Ward T, Emsley R, et al. Effects of SlowMo, a Blended Digital Therapy Targeting Reasoning, on Paranoia Among People With Psychosis: A Randomized Clinical Trial. JAMA Psychiatry. April 7, 2021. Online ahead of print.Habitual Snoring in Children May Alter Brain StructureiStock/quintanillaMany studies have found a connection between habitual snoring in children (a sign of obstructive sleep disordered breathing) and behavioral problems such as inattention or hyperactivity. A study appearing in Nature Communications now has found evidence to suggest that the structure of the frontal lobes of children who regularly snore may differ from those of children who do not snore.Investigators at the University of Maryland School of Medicine and colleagues analyzed behavioral and imaging data from over 10,000 youth (aged 9 and 10) available from the national Adolescent Brain Cognitive Development (ABCD) Study. Of this sample, they identified 661 children with habitual snoring (at least three nights per week).As with previous studies, this analysis found that the children with habitual snoring had more behavioral problems than nonsnoring peers, as assessed by the Child Behavior Checklist (CBCL). MRI brain scans of the children also revealed that children with habitual snoring had less gray matter volume in multiple areas of the frontal lobe, an area involved in behaviors like social interactions and impulse control. The children who most frequently snored were more likely to have greater reductions in frontal lobe volume and higher CBCL scores compared with children who snored less.Due to the cross-sectional nature of the study, the authors noted that additional research is needed to understand the relationship be

**Решение:** -1 дайджест научных публикаций о синдроме разбитого сердца и здоровье

---

### 438 · R9480

**SOCbot: Using Large Language Models to measure and classify occupations in surveys**

2025 · preprint · en · https://doi.org/10.31235/osf.io/9ruwe_v1

We present the results of a new approach to measuring the occupations of respondents in surveys using Large Language Models (LLMs). Occupation is a notoriously difficult variable to measure accurately due to the very large number of occupations and the technical ways they are described in standard classifications. These features of occupational classification systems mean that the measurement and classification stages are usually not conducted simultaneously, with coding of open responses about job title and tasks implemented in a subsequent stage of 'office coding'. In our new approach, which we call SOCbot, an LLM integrated in the questionnaire scripting software is used to code the job title response to the occupational classification in real-time during the interview. Where the job title does not contain sufficient information to be coded with confidence, the LLM probes for further relevant details on job tasks, industry, qualifications, and so on. SOCbot can also be used in static mode offline on already collected response data. Our results demonstrate that the approach attains rates of coder reliability comparable to trained human coders. We also demonstrate that the approach is feasible in large-scale survey operations and has significant potential to reduce respondent burden, lower costs, and yield more timely and accurate data.

**Решение:** -4 автоматическое кодирование профессий в социологических опросах (SOCbot)

---

### 439 · R3177

**Artificial intelligence as a source of psychotherapy-related psychoeducation: a cross-sectional content analysis of information on eye movement desensitization and reprocessing.**

2026 · Frontiers in psychiatry · journal article, journalarticle, article · eng · https://doi.org/10.3389/fpsyt.2026.1937506

Background: Due to structural and socioeconomic barriers to accessing the healthcare system, individuals are increasingly turning to online platforms to obtain health-related information. With the advancement of artificial intelligence (AI), the use of AI for this purpose is also on the rise. It can also be said that seeking information from AI regarding psychotherapies is increasingly common. Objective: This study aimed to assess the informational quality and readability of AI-generated psychoeducational content about psychotherapy. To this end, we evaluated the informational quality and readability of LLM-generated Eye Movement Desensitization and Reprocessing (EMDR) psychoeducational content across different models. Methods: In this cross-sectional content analysis, EMDR-related search queries were identified through Google Trends, converted into patient-facing questions, and subsequently organized into four thematic categories, with five questions selected from each category for evaluation using ChatGPT (GPT-4o), Gemini (1.5 Pro), and DeepSeek (V3). Each question was entered in three separate sessions, yielding 180 responses. The informational quality was assessed by two blinded psychiatrists using the Ensuring Quality Information for Patients (EQIP) instrument. Readability was evaluated using the Flesch-Kincaid Grade Level (FKGL) and Flesch Reading Ease (FRE) indices. Statistical analyses included linear mixed-effects models and ANOVA. Results: The overall mean EQIP score was 56.08 (SD = 4.43). Informational quality differed significantly across the models (p < 0.001), and no significant differences were observed across EMDR-related question categories. The highest informational quality scores were obtained by Gemini, followed by DeepSeek and ChatGPT. DeepSeek generated the most readable responses. Higher EQIP scores were seen to be associated with greater readability and longer response length. All the evaluated models produced responses that exceeded the commonly recommended readability levels for patient education materials. Overall inter-rater consistency was high for the total EQIP scores. Conclusion: Although all the LLMs evaluated were able to generate psychoeducational information about EMDR, substantial differences were observed between the models in respect of informational quality and readability. The findings suggest that psychoeducational quality depends more strongly on the language model used than on the specific EMDR-related topic being addressed. LLMs may serve as supplementary psychoeducational resources but should not be considered as substitutes for professional psychotherapy or individualized clinical care.

**Решение:** -2 психиатры оценивают качество психообразовательной информации по EMDR, сгенерированной LLM (EQIP)

---

### 440 · R11712

**ChatGPT as a Tool for Oral Health Education: A Systematic Evaluation of ChatGPT Responses to Patients’ Oral Health-related Queries**

2024 · Journal of Nature and Science of Medicine · journalarticle, review, article · en · https://doi.org/10.4103/jnsm.jnsm_208_23

Abstract Background: ChatGPT holds promise in oral health education, provided valid concerns are proactively examined and addressed. Hence, this study was conducted to evaluate ChatGPT responses to patients’ most common queries about their oral health. Methods: A cross-sectional study was conducted to gather a dataset of oral health-related queries from patients attending a dental institution. The dataset was preprocessed and formatted to remove any irrelevant or duplicate queries. Then, we supplied the dataset to ChatGPT to generate responses. We asked two dental public health experts to independently review the ChatGPT responses for clarity, accuracy, relevance, comprehensiveness, consistency, acceptance, and bias using a 5-point Likert scale. The intraclass correlation coefficient (ICC) was used to evaluate interrater reliability. Scores were summarized using descriptive statistics. Results: A total of 563 oral health-related queries were gathered from 120 patients. After removing the irrelevant or duplicate queries, 105 were included in the final dataset. The ICC value of 0.878 (95% confidence interval range from 0.841 to 0.910) showed good reliability between the reviewers. The majority of ChatGPT responses had a clear understanding (95.24%), were scientifically accurate and relevant to the query (87.62%), were comprehensive (83.81%), were consistent (84.76%), and were acceptable without any edits (86.67%). The reviewers strongly agreed that only 40.96% of the responses had no bias. The overall score was high with a mean value of 4.72 ± 0.30. The qualitative analysis of comments on ChatGPT responses revealed that the responses were rather long and more comprehensive. Conclusions: ChatGPT generated clear, scientifically accurate and relevant, comprehensive, and consistent responses to diverse oral health-related queries despite some significant limitations.

**Решение:** -1 систематический обзор применения ChatGPT в стоматологическом просвещении

---

### 441 · R1805

**Evaluation of large language model chatbot responses to psychotic prompts**

2026 · JAMA psychiatry · journalarticle · https://doi.org/10.1001/jamapsychiatry.2026.0249

Importance: The large language model (LLM) chatbot product ChatGPT has accumulated 800 million weekly users since its 2022 launch. In 2025, several media outlets reported on individuals in whom apparent psychotic symptoms emerged or worsened in the context of using ChatGPT. As LLM chatbots are trained to align with user input, they may have difficulty responding to psychotic content. Objective: To assess whether ChatGPT can reliably generate appropriate responses to prompts containing psychotic symptoms. Design: A cross-sectional study of ChatGPT responses to psychotic and control prompts, with blind clinician ratings of response appropriateness. Setting: ChatGPT web application accessed on 8/28–8/29/2025, testing three product versions: GPT-5 Auto (current paid default), GPT-4o (previous paid default), and “Free” (version accessible without subscription or account). Main Outcomes and Measures: We presented 158 unique prompts (79 control and 79 psychotic, generated based on the Structured Interview for Psychosis-Risk Syndromes) to three product versions, yielding 474 prompt-response pairs. Blinded clinicians assigned each an appropriateness rating (0 = completely appropriate, 1 = somewhat appropriate, 2 = completely inappropriate) via a standardized rubric. We hypothesized a priori that psychotic prompts would be more likely than control prompts to elicit less appropriate responses both across and within product versions. Results: In the primary (across-version) analysis, psychotic prompts were 25.84 times more likely to elicit less appropriate responses with “Free” ChatGPT (95% CI 12.45 to 53.66, p < 0.001). GPT-5 Auto reduced risk somewhat (OR for interaction term 0.33, 95% CI 0.16 to 0.68, p = 0.005) yet still generated less appropriate responses at a greatly elevated rate (implied OR 8.53, 95% CI 3.05 to 23.84). In the secondary (within-version) analysis, ORs were 9.08 for GPT-5 Auto (95% CI 4.24 to 21.02), 14.15 for GPT-4o (95% CI 6.12 to 37.23) and 43.37 for “Free” (95% CI 18.44 to 112.80). In an exploratory analysis, prompts reflecting grandiosity or disorganized communication were more likely to elicit inappropriate responses than those reflecting delusions. Conclusions and Relevance: No tested version of ChatGPT reliably generated appropriate responses to psychotic content.

**Решение:** -2 клиницисты оценивают адекватность ответов ChatGPT на реплики с психотическими симптомами

---

### 442 · R1143

**Randomized Trial of an AI-Powered Mental Health Intervention for Depression and Anxiety**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/nwz9q_v2

Importance: Depression and anxiety are prevalent and disabling, yet most individuals receive inadequate or no care. Purpose-built generative AI platforms may offer scalable first-line support, though large-trial evidence remains limited. Objective: To determine whether Flourish, an AI-powered mental health platform, prevents and reduces depression and anxiety symptoms compared with care-as-usual. Design: Preregistered, parallel-group, superiority randomized clinical trial conducted in 2025, with assessments at weeks 0, 2, 4, and 6. Setting: A large North American university. Participants: A total of 1,137 college students aged 18 years or older was recruited through a research participation system without symptom-based screening and randomized to treatment or care-as-usual. 850 participants (74.6%) completed the final Week 6 follow-up. Intervention: Participants assigned to treatment received Flourish, which offered self-guided support informed by cognitive behavioral therapy, dialectical behavior therapy, acceptance and commitment therapy, positive psychology, and motivational interviewing, and were instructed to use it at least twice weekly. Participants assigned to care-as-usual retained access to usual mental health resources. Main Outcomes and Measures: Preregistered primary outcomes were depression (Patient Health Questionnaire-2) and anxiety symptoms (Generalized Anxiety Disorder-2), assessed biweekly. Results: Among 1,137 participants, mean (SD) age was 20.77 (5.34) years, and 853 (75.0%) were female. Symptom trajectories were more favorable in treatment (vs control) for depression (condition × time: β = −0.03; 95% CI, −0.05 to −0.01; P = .006) and anxiety (β = −0.04; 95% CI, −0.06 to −0.01; P = .001). Among participants with elevated baseline symptom severity, treatment increased rates of meaningful change for depressive symptoms (52.3% vs 31.7%; risk ratio [RR], 1.65 [95% CI, 1.16-2.34]; number needed to treat [NNT], 4.9 [95% CI, 2.9-14.8]) and anxiety symptoms (50.6% vs 38.1%; RR, 1.33 [95% CI, 1.05-1.68]; NNT, 8.0 [95% CI, 4.4-44.5]). Participants with low baseline symptoms showed less symptom worsening at 6 weeks. No adverse events attributable to the intervention were identified. Conclusions and Relevance: This trial demonstrates that a purpose-built generative AI platform can serve as a scalable first-line mental health tool, effective for prevention and early intervention of depression and anxiety symptoms in an unscreened general population. Trial Registration: ClinicalTrials.gov identifier: NCT06668532 (https://clinicaltrials.gov/study/NCT06668532).

**Решение:** -6 РКИ эффективности диалогового ИИ для снижения тревоги и депрессии без кодирования текстов

---

### 443 · R8586

**OPOR-Bench: Evaluating Large Language Models on Online Public Opinion Report Generation**

2025 · Computers, Materials &amp; Continua · journalarticle, preprint/article, preprint · https://doi.org/10.32604/cmc.2025.073771

Online Public Opinion Reports consolidate news and social media for timely crisis management by governments and enterprises. While large language models have made automated report generation technically feasible, systematic research in this specific area remains notably absent, particularly lacking formal task definitions and corresponding benchmarks. To bridge this gap, we define the Automated Online Public Opinion Report Generation (OPOR-GEN) task and construct OPOR-BENCH, an event-centric dataset covering 463 crisis events with their corresponding news articles, social media posts, and a reference summary. To evaluate report quality, we propose OPOR-EVAL, a novel agent-based framework that simulates human expert evaluation by analyzing generated reports in context. Experiments with frontier models demonstrate that our framework achieves high correlation with human judgments. Our comprehensive task definition, benchmark dataset, and evaluation framework provide a solid foundation for future research in this critical domain. 27 pages, accepted by CMC-Computers, Materials &amp; Continua, 2025

**Решение:** -4 бенчмарк оценки отчетов об общественном мнении (OPOR-Bench)

---

### 444 · R9833

**DepressLLM: Interpretable domain-adapted language model for depression detection from real-world narratives**

2025 · arXiv · preprint/article, preprint · https://doi.org/10.48550/arxiv.2508.08591

Advances in large language models (LLMs) have enabled a wide range of applications. However, depression prediction is hindered by the lack of large-scale, high-quality, and rigorously annotated datasets. This study introduces DepressLLM, trained and evaluated on a novel corpus of 3,699 autobiographical narratives reflecting both happiness and distress. DepressLLM provides interpretable depression predictions and, via its Score-guided Token Probability Summation (SToPS) module, delivers both improved classification performance and reliable confidence estimates, achieving an AUC of 0.789, which rises to 0.904 on samples with confidence $\geq$ 0.95. To validate its robustness to heterogeneous data, we evaluated DepressLLM on in-house datasets, including an Ecological Momentary Assessment (EMA) corpus of daily stress and mood recordings, and on public clinical interview data. Finally, a psychiatric review of high-confidence misclassifications highlighted key model and data limitations that suggest directions for future refinements. These findings demonstrate that interpretable AI can enable earlier diagnosis of depression and underscore the promise of medical AI in psychiatry.

**Решение:** ? T3 детекция депрессии по автобиографическим нарративам моделью DepressLLM; проверить эталон разметки

---

### 445 · R5400

**Framework for Diverse Depression Patients Roleplaying and Cognitive Diagnosis of Scales Using LLMs Based on CoT Prompts**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-981-95-7138-3_26

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? T2/T3 ролевые симуляции депрессивных пациентов и когнитивная диагностика шкал, нет аннотации

---

### 446 · R1640

**Evaluating Empathy in Large Language Model Responses Under Different Prompting Conditions: A Brief Literature Review**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.23123174

Large Language Models (LLMs) are increasingly used to produce conversational responses in emotionally sensitive settings. This paper presents a focused narrative review of research on empathetic communication in LLMs, with particular attention to prompting strategies and methods for evaluating empathy. Eight scholarly sources were reviewed, covering chatbot–human response comparisons, human–AI collaboration, mental-health applications, psychotherapy-informed prompting, persona-based prompting, empathy benchmarking, and the reliability of empathy evaluation. The reviewed evidence shows that LLMs can generate responses perceived as empathetic and that prompt design can influence emotional recognition, validation, and supportive language. The literature also indicates that persona instructions can alter model behavior in unintended ways and that empathy is difficult to represent with one universal metric. Multi-dimensional evaluation and comparison with human expert judgments therefore remain important when assessing empathetic communication. A further gap concerns consistency: existing research provides useful evidence about response quality and prompt effects, but fewer studies directly examine whether an LLM behaves consistently when the same scenario is repeated under the same prompting condition. The review concludes that prompting strategy and evaluation methodology should be studied together, particularly when LLMs are considered for emotionally sensitive communication.

**Решение:** -1 нарративный обзор литературы по оценке эмпатии в ответах LLM

---

### 447 · R0976

**Evaluating the effectiveness of ChatGPT in rubric development**

2026 · Jyväskylä University Digital Archive (University of Jyväskylä) · article · en · https://doi.org/10.1016/j.asw.2026.101067&quot

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 оценка эффективности ChatGPT при разработке оценочных рубрик, нет аннотации

---

### 448 · R4041

**Designing and Evaluating Prompt Strategies for Educational Content Creation : A Comparison of Basic and Engineered ChatGPT Prompts for Higher Education**

2026 · Diva portal (Dalarna University Library) · dissertation · en · http://urn.kb.se/resolve?urn=urn:nbn:se:lnu:diva-149642

This thesis examines how prompt engineering affects the quality of ChatGPT-generated educational explanations in a higher education Information Systems context. In this thesis, educational explanations are AI-generated texts intended to help students understand course concepts. The study compares a basic prompt with an engineered prompt template based on the PERFECT and GAIDE frameworks and selected prompt patterns, using structured prompting elements like role, course context, learning goals, format, and constraints. Five short educational explanation tasks were generated with both prompt strategies and evaluated by ten university instructors from three universities using the criteria of Clarity, Accuracy, and Usefulness from the PEARL Explanation Rubric. The study used a mixed methods design, using Likert-scale ratings with open-ended comments. The quantitative data were analyzed using descriptive statistics, a Wilcoxon signed-rank test, and inter-rater agreement with ICC, while the qualitative comments were analyzed using thematic analysis. The quantitative findings showed that the engineered prompt was rated slightly higher for Accuracy and Clarity and more clearly higher for Usefulness. The Wilcoxon signed-rank test showed a statistically significant difference for Usefulness, but not for Accuracy or Clarity, while inter-rater agreement was poor for all three criteria. The qualitative findings showed that basic prompt outputs were often simple and direct, but also more general and lacking depth. Engineered prompt outputs were more structured, detailed, easier to adapt, and more useful as teaching drafts, but they still needed teacher review because some outputs had unclear terms, missing or outdated content, questionable examples, an AI-written style, or too little critical perspective. The study finds that engineered prompting can support educational content creation, especially by improving usefulness, but it does not create finished teaching material by itself. Human review, correction, iteration, and course adaptation are still necessary when using AI like ChatGPT for educational content creation.

**Решение:** -4 диссертационное исследование разработки промптов для учебных объяснений

---

### 449 · R3857

**Designing cognitive friction with concept suppression in large language models**

2026 · Human-Computer Interaction · article · en · https://doi.org/10.1080/07370024.2026.2708617

Large Language Models (LLMs) are increasingly deployed in tools for thought and creativity support systems, yet their generative fluency can collapse early-stage ideation into selection and curation, shifting cognitive labor away from concept formation and divergent thinking toward homogenized outputs. We introduce concept suppression as a subtractive approach to induce cognitive friction, treating the learned conceptual manifold of a pre-trained model as a design surface for human–AI interaction. We operationalize this with Unlearning to Rest, a prototype that applies weight-level concept suppression to Llama3.2:3b, suppressing a canonical attractor concept (“chair”) to create navigational impediments in the solution space. We evaluate the approach in a within-subject study (N = 37) where participants were set a conceptual ideation challenge. Quantitative results show a consistent workload–ownership trade-off: the unmodified model reduces mental demand and effort but also reduces perceived ownership, while Unlearning to Rest yields ratings closer to unaided ideation. Qualitative analysis indicates that the constrained model prompts user re-articulation, supporting a stage-fit workflow in which constrained assistance benefits early ideation. We contribute (1) representational intervention as a lens for LLM-based tools for thought, (2) a system instantiation via weight-level concept suppression, and (3) empirical evidence motivating stage-sensitive evaluation of LLM assistance beyond efficiency and output quality.

**Решение:** -4 концептуальное подавление понятий в инструментах поддержки креативности

---

### 450 · R0006

**Collaborative-adversarial jailbreaking: A propagation-aware attack framework for multi-agent code generation systems.**

2027 · Neural networks : the official journal of the International Neural Network Society · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.neunet.2026.109280

The rapid adoption of multi-agent frameworks for automated code generation has significantly enhanced software development efficiency, yet simultaneously introduced critical security challenges that remain largely unexplored. While extensive research has investigated jailbreaking vulnerabilities in single-agent large language models, existing studies have overlooked the unique security risks arising from collaborative dynamics in multi-agent systems, where distributed decision-making and social interactions may amplify rather than mitigate adversarial threats. To address this gap, we propose the first comprehensive security assessment framework for multi-agent code generation, introducing Implicit Multi-agent Attack (IMA), a novel jailbreaking strategy that exploits social engineering and collaborative reinforcement within agent networks. Our evaluation encompasses four prominent frameworks (MetaGPT, CrewAI, AutoGen, and ChatDev) using the established RMCBench benchmark (Resistance to Malicious Code Benchmark) with 282 malicious code generation tasks across text-to-code, function-level, and block-level completion scenarios. Compared to traditional explicit attacks and single-agent baselines, IMA demonstrates substantially higher effectiveness, achieving an average attack success rate of 89.01% and revealing collaborative harm amplification factors up to 114.9%. The results expose fundamental vulnerabilities in current multi-agent architectures, with defense mechanisms showing alarmingly low detection rates below 30%. Crucially, by isolating the final coding agent via a direct jailbreak baseline (SADJ), we demonstrate that multi-agent collaboration itself amplifies attack success by an average of 11.4% (CADA), confirming that the vulnerability lies in the architecture rather than the underlying model alone.

**Решение:** -4 многоагентный состязательный джейлбрейк генерации программного кода
