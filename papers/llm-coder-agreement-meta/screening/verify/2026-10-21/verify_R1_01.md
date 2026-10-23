# Проверка с метками ИИ, часть 1

Записи 1–150 из 1304, с метками обеих моделей над строкой решения. Модели согласны и вы тоже — поставьте `=`; иначе свой код (`+`, `?` или `-`, причина не нужна). Если модели разошлись, `=` не годится — нужен ваш код. Решаете вы.

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

### 1 · R0002

**SCORING MOTIVATIONAL ASSESSMENTS WITH FREE RESPONSES VIA TRANSFORMERS**

2027 · Washington State University · dissertation/doctoral thesis, dissertation · en · https://doi.org/10.7273/000007859

Student motivation is a well-established predictor of academic engagement and achievement. Despite its importance, motivation is difficult to assess accurately, as it is shaped by multiple, overlapping constructs and contextual factors. This complexity continues to pose challenges for researchers and practitioners seeking measurement tools with valid and reliable scores. While open-ended responses provide meaningful information about students’ motivation, traditional human scoring is time-consuming, subject to inconsistencies, and not easily scalable. Advances in natural language processing, especially with transformer-based large language models, offer promising new approaches for automated scoring. However, their use in scoring student motivation assessments remains largely undocumented, and practical applications are in the early stages of development. This dissertation addresses this gap through two studies. The first study presents a scoping review of transformer-based approaches to motivation scoring, examining model types, scoring methods, target constructs, and available psychometric evidence. Guided by the PRISMA-ScR protocol, the review identified only nine studies, underscoring the limited research in this area. The second study empirically evaluates transformer models for motivation assessment, comparing fine-tuned encoder models (BERT, DeBERTa) with rubric-prompted decoder models (GPT-3.5 Turbo, GPT-4.1). Model performance is evaluated through a psychometric lens, including analyses of human–machine agreement, construct validity, subgroup fairness, and predictive validity with academic outcomes such as GPA and retention. Notably, DeBERTa outperformed human raters in predicting academic outcomes, suggesting that certain transformer models may capture motivational signals with greater predictive value—even when agreement with human scores is modest. However, validity analyses revealed important limitations: models demonstrated inconsistent construct validity and notable subgroup disparities, raising concerns about fairness. Overall, while transformer-based approaches, specifically DeBERTa, hold promise for scalable motivation assessment, challenges remain in ensuring interpretability, validity, and equity. This study also discusses the challenges and limitations encountered, outlines practical implications for educational assessment, and identifies directions for future research in developing robust and fair applications of transformer models.

**ИИ:** + · обе модели · подсчёт методики · GPT-3.5/GPT-4.1 scored students' open-ended motivation responses using a rubric; the study reports human–machine agreement.

**Решение:** =

---

### 2 · R0011

**Echo-Bench: A Chinese Replication and Cross-Lingual Extension of Psychosis-Bench**

2026 · PsyArXiv · preprint · https://doi.org/10.31234/osf.io/thvpz_v1

Psychosis-Bench recently showed that production chat models confirm and elaborate users' delusion-like beliefs under multi-turn pressure, but its evidence is English-only, Western-flagship-only, and rests on an uncalibrated LLM judge. We present Echo-Bench, a Chinese replication and cross-lingual extension: the full 16-case, 12-turn protocol mirrored into Chinese under a fidelity-first translation protocol with an independent re-translation audit, run against two widely deployed Chinese chat models (DeepSeek V4.1-Flash, qwen-plus) in both languages — 192 sessions, 4,032 turn-level ratings. The original qualitative finding replicates in both languages (RQ1). All six pre-committed cross-language contrasts are significant after Benjamini–Hochberg control: the Chinese arm is directionally worse on every dimension, with model-differentiated failure channels (RQ2). Because our pipeline required a bilingual rater, we placed the measurement instrument itself under test (RQ3): a five-layer rater trust chain — entrance examination against human gold, extreme-score arbitration, red-line audit of the arbiter, blind human adjudication, and a spot check of the non-extreme stratum — shows that automated raters fail concentratedly in the extreme band, with two named failure modes (disclaimer laundering, eloquence inflation), and that a strong general-purpose arbiter is disqualified by pre-specified red lines. A negative control bounds rater language sensitivity below what the observed gaps require. Safety behavior certified in English does not certify safety behavior in Chinese; the instruments used to check either must themselves be checked.

**ИИ:** + · обе модели · LLM-судья · LLM judges rate how chatbots respond to delusion-like beliefs, and these ratings are checked against human gold labels and blind human adjudication.

**Решение:** =

---

### 3 · R0014

**Generative AI predicts personality traits on the basis of open-ended narratives**

2026 · Nature Human Behaviour · article · en · https://doi.org/10.1038/s41562-025-02397-x

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. LLM personality ratings of narratives may be validated only against self-report, but they might also be compared with human raters.

**Решение:** =

---

### 4 · R0024

**Performances de l’intelligence artificielle générative dans la correction de travaux pédagogiques d’étudiants en 3e cycle de médecine générale en France**

2026 · EXERCER · journalarticle, article · https://doi.org/10.56746/exercer.2026.226.374

Contexte. L’évaluation des productions étudiantes par l’intelligence artificielle générative suscite un intérêt croissant en pédagogie médicale. Les récits de situations complexes authentiques (RSCA), utilisés dans le diplôme de médecine générale, nécessitent une évaluation nuancée, mobilisant une posture réflexive et des critères explicites. Objectifs. Évaluer les performances de deux modèles de langage (LLM), GPT-4® et MistralSmall 3.1®, dans la correction des RSCA en les comparant aux évaluations d’experts de la discipline selon la grille nationale d’évaluation des RSCA. Méthode. Une étude mixte convergente a été menée début 2025. Vingt et un RSCA extraits d’un corpus national ont été évalués par GPT-4® et Mistral Small 3.1® via une invite standardisée simulant une correction experte selon la grille nationale. Les notations ont été comparées à celles de cinq experts, en calculant les taux de concordance et le coefficient kappa (ҡ). Une analyse qualitative thématique des commentaires a complété l’évaluation. Résultats. Les taux de concordance entre LLM et experts étaient modérés (41,4 % pour GPT-4®, 43,7 % pour MistralSmall 3.1®) avec des coefficients ҡ faibles, indiquant un accord limité. Les LLM attribuaient uniquement des mentions « pertinent » ou « améliorable », sans mention « insuffisant ». L’analyse qualitative a révélé une posture évaluative standardisée des LLM, centrée sur la structure et la clarté sans analyse réflexive ni contextualisation, contrairement aux experts qui reliaient les critères entre eux et contextualisent les lacunes. Conclusion. Les LLM étudiés ne peuvent se substituer aux correcteurs humains dans l’évaluation des RSCA, notamment pour les travaux nécessitant une analyse critique et une posture pédagogique contextualisée. Leur utilisation pourrait toutefois être envisagée dans un cadre hybride, comme soutien méthodologique ou préparation à la relecture formative, sous supervision. L’évolution rapide des LLM justifie de poursuivre les recherches sur leur place en pédagogie médicale

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT-4 and Mistral graded reflective narratives against five experts (kappa reported). Unclear whether reflective-practice grading is a psychological construct or educational grading.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs graded medical students' reflective educational writings against expert grid; this is educational assessment of coursework, not a psychological or clinical construct.)

**Решение:** -

---

### 5 · R0044

**When large language models are reliable for judging empathic communication**

2026 · Nature Machine Intelligence · journalarticle, preprint/article, article · en · https://doi.org/10.1038/s42256-025-01169-6

Large language models (LLMs) excel at generating empathic responses in text-based conversations. But, how reliably do they judge the nuances of empathic communication? Here we investigate this question by comparing how experts, crowdworkers and LLMs annotate empathic communication across four evaluative frameworks drawn from psychology, natural language processing and communications applied to 200 real-world conversations where one speaker shares a personal problem and the other offers support. Drawing on 3,150 expert annotations, 2,844 crowd annotations and 3,150 LLM annotations, we assess interrater reliability between these three annotator groups. We find that expert agreement is high but varies across the frameworks’ subcomponents depending on their clarity, complexity and subjectivity. We show that expert agreement offers a more informative benchmark for contextualizing LLM performance than standard classification metrics. Across all four frameworks, LLMs consistently approach this expert level benchmark and exceed the reliability of crowdworkers. These results demonstrate how LLMs, when validated on specific tasks with appropriate benchmarks, can support transparency and oversight in emotionally sensitive applications including their use as conversational companions. Kumar et al. show that large language models (LLMs) nearly match expert reliability and outperform laypeople when assessing empathic communication across multiple frameworks. The performance of both LLMs and experts depends on clear and specific evaluation criteria.

**ИИ:** + · обе модели · LLM-судья · LLMs, experts and crowdworkers annotated empathic communication in 200 support conversations using four frameworks, and the study reports interrater reliability between the groups.

**Решение:** =

---

### 6 · R0050

**A Privacy-Preserving Intelligent Assistant for Clinical Psychology Practice**

2026 · International Joint Conference on Artificial Intelligence · conference, conference-paper · https://doi.org/10.24963/ijcai.2026/985

This paper describes a fully local, privacy-preserving intelligent system designed to assist in clinical psychology practice. The system automatically transcribes therapy sessions performing speaker attribution. Beyond transcription, the tool enhances clinical reasoning by detecting cognitive distortions and emotional patterns utilizing specialized deep learning classifiers and Large Language Models (LLMs). By guiding an LLM locally through a multi-step analysis process, the assistant synthesizes the enriched data and generates a series of analysis reports and clinical documentation of the session. As a result, the assistant reduces the administrative burden on professionals while preserving privacy with an edge computing approach in which the data never leaves the therapist's device. Finally, the assistant uses human-in-the-loop validation so that the professional always remains in control, ensuring clinical accuracy and trust.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · System paper where LLMs detect cognitive distortions and emotions in therapy transcripts; unclear if outputs are validated against human-coded labels.

**Решение:** =

---

### 7 · R0051

**Case-Specific Rubrics for Clinical AI Evaluation: Methodology, Validation, and LLM-Clinician Agreement Across 823 Encounters**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2604.24710

Objective. Clinical AI documentation systems require evaluation methodologies that are clinically valid, economically viable, and sensitive to iterative changes. Methods requiring expert review per scoring instance are too slow and expensive for safe, iterative deployment. We present a case-specific, clinician-authored rubric methodology for clinical AI evaluation and examine whether LLM-generated rubrics can approximate clinician agreement. Materials and Methods. Twenty clinicians authored 1,646 rubrics for 823 clinical cases (736 real-world, 87 synthetic) across primary care, psychiatry, oncology, and behavioral health. Each rubric was validated by confirming that an LLM-based scoring agent consistently scored clinician-preferred outputs higher than rejected ones. Seven versions of an EHR-embedded AI agent for clinicians were evaluated across all cases. Results. Clinician-authored rubrics discriminated effectively between high- and low-quality outputs (median score gap: 82.9%) with high scoring stability (median range: 0.00%). Median scores improved from 84% to 95%. In later experiments, clinician-LLM ranking agreement (tau: 0.42-0.46) matched or exceeded clinician-clinician agreement (tau: 0.38-0.43), attributable to both ceiling compression and LLM rubric improvement. Discussion. This convergence supports incorporating LLM rubrics alongside clinician-authored ones. At roughly 1,000 times lower cost, LLM rubrics enable substantially greater evaluation coverage, while continued clinical authorship grounds evaluation in expert judgment. Ceiling compression poses a methodological challenge for future inter-rater agreement studies. Conclusion. Case-specific rubrics offer a path for clinical AI evaluation that preserves expert judgment while enabling automation at three orders lower cost. Clinician-authored rubrics establish the baseline against which LLM rubrics are validated. 14 pages, 2 figures, 3 tables, submitted to JAMIA

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM-judge vs clinician ranking agreement on clinical AI documentation, including psychiatry/behavioral health cases; the construct may be general documentation quality.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM rubrics score quality of clinical AI documentation outputs across general medical specialties; not a psychological construct in text coded against human labels.)

**Решение:** ?

---

### 8 · R0055

**Large language models lose diabetes stigma signals when patient culture shifts**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-9931021/v1

Abstract A disease label does not always define a stable language model task. We test this problem in diabetes, a common and stigmatized condition where Type 1 and Type 2 communities share a diagnosis but use different cultural language for daily care and public judgment. We built a patient discourse corpus with a manually annotated reference set of 1526 posts from condition specific Type 1 and Type 2 forums, supported by 1386 additional texts from patient interviews, forum posts, and published patient narratives for model development. Our lexical and embedding analyses identified distinct diabetes language patterns across the two communities. A stigma detector trained on Type 2 discourse lost sensitivity when applied to Type 1 stigma posts, with F1 falling from 0.91 in domain to 0.43 out of domain. Direct LLM prompting showed that stigma detection varied with prompt context, with generic prompts missing rare stigma signals and calibrated prompts recovering positive class sensitivity. We then introduced a culture sensitive calibration and adjudication framework that does not hard code diabetes type into prediction. Prompt calibration raised GPT-5.4 Macro F1 from 0.515 to 0.776, and importance weighted adjudication improved downstream binary and subtype Macro F1 to 0.767 and 0.368. Our results show that a shared diagnosis does not define a shared language model task, and that culture sensitive calibration with adjudicated expansion can improve the validity of inference from patient language.

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT-5.4 prompted to detect stigma in diabetes patient forum posts, evaluated against a hand-annotated reference set of 1,526 posts.

**Решение:** =

---

### 9 · R0062

**TellTale: Blending Multi-Instance LoRA Text Encoders and a Zero-Shot LLM Judge for Ambivalence/Hesitancy Recognition in Videos**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.16635

We present TellTale, a text-only approach to ambivalence/hesitancy (A/H) recognition in interview videos, evaluated on the BAH dataset as part of the 3rd A/H Video Recognition Challenge (11th ABAW Workshop, ECCV 2026). Although the dataset provides video, audio, facial crops, and transcripts, TellTale relies on the transcript alone and combines three probability streams. Two text encoders, multilingual-e5-large and mDeBERTa-v3-base, are fine-tuned with parameter-efficient LoRA adapters under a multiple-instance learning (MIL) objective, in which transcript chunks are scored individually and pooled with a smooth maximum so that only the video-level label is needed for supervision. The third stream requires no training: a quantized 14B instruction LLM is prompted, zero-shot, to rate each transcript for A/H. The three probabilities are combined by a weighted average and a single decision threshold, both selected on participant-grouped cross-validated predictions. On the organizer-scored private test set of 152 videos from unseen participants, TellTale achieves a Macro-F1 of 0.7364 and an average precision of 0.7940, compared with 0.2827 Macro-F1 for the official vision-based baseline.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Zero-shot LLM rates interview transcripts for ambivalence/hesitancy against BAH labels (believed expert-annotated); check LLM-only ablation results.); Sonnet ? (неясно, кто ставил эталонные метки: A zero-shot 14B LLM rates transcripts for ambivalence/hesitancy against BAH labels, probably from human annotators. The LLM is only one ensemble stream, so its standalone agreement is unclear.)

**Решение:** ?

---

### 10 · R0083

**Medical or General-Purpose LLMs for Virtual Patient Simulation? A Comparative Evaluation in OSCE-Aligned Scenarios**

2026 · International Conference on Serious Games and Applications for Health · conference · https://doi.org/10.1109/segah69272.2026.11653318

Selecting a Large Language Model (LLM) for virtual patient (VP) simulations remains an open question in medical education. Many LLMs have been trained on clinical data, but whether they can convincingly behave like a patient has not been thoroughly studied. We report the first systematic comparison of eight open-source LLMs (four medical-specialized, four general-purpose) on this task. Using a full factorial design, we generated 576 unique simulated conversations and scored them with a dual framework: seven practical deployment metrics plus six literature-derived metrics grounded in the RIAS communication coding system and the CARE empathy scale, all validated by three blinded clinicians. When grouped by category, general-purpose LLMs performed better on both automated and human evaluations. The top four individual models (a mix of medical and general-purpose) earned statistically equivalent human ratings, all above 4.6/5, while the bottom two, both medical, suffered from poor fine-tuning. What predicted simulation quality was base model architecture and fine-tuning quality, not whether the model carried a "medical" label. Model choice was the dominant source of performance variance (ICC = 0.074 for scenario), while clinical scenario accounted for under 8%. Practical and literature-based metrics captured overlapping but partially distinct constructs (Spearman ρ = 0.619), with individual model rankings shifting substantially between frameworks, indicating that conversational fluency and socio-emotional depth require separate evaluation. These findings suggest that medical educators should prioritize well-constructed, instruction-tuned LLMs rather than restricting selection to medical-specific models.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mainly LLM patient simulation, but automated RIAS/CARE empathy metrics (possibly LLM-judged) were validated by blinded clinicians; agreement may be reported.

**Решение:** =

---

### 11 · R0089

**Named Entity Recognition in Arabic Mental Health Using Large Language Models**

2026 · ACM Transactions on Asian and Low-Resource Language Information Processing · journalarticle, article · en · https://doi.org/10.1145/3811876

Named Entity Recognition (NER) in Arabic mental-health text is constrained by the scarcity of gold annotations and dialectal variation. Identifying medical entities (e.g., Symptom, Diagnosis, drug, Dosage) in low-resource context is crucial for clinical triage and mental health safety. To address this gap, we propose and evaluate end-to-end framework for NER in Arabic patient-generated mental health questions. Our framework leverages state-of-the-art Large Language Models (LLMs), including GPT-4o, LLaMA, and ALLaM, utilizing Persona–Template prompting strategy, including zero-shot vs. few-shot tested across the models. We applied a clinically grounded nine-entity schema to extract structured information from mental health questions. We adopt a hybrid evaluation strategy that combines LLM-as-a-Judge scoring for scalability with targeted validation on a manually curated drug subset, compensating for the limited availability of fully gold-annotated data. Results show that few-shot prompting improves reliability across models. GPT-4o achieves the strongest drug test set accuracy (F1: 0.86→0.94), LLaMA remains stable and competitive (0.89→0.88), and Arabic-focused ALLaM shows the largest relative gain (0.58→0.73). This work not only advances Arabic NLP for mental health applications but also offers a reproducible framework for low-resource NER, demonstrating the feasibility of LLM-driven medical entity extraction in critical clinical contexts.

**ИИ:** ? · обе модели · неясен конструкт · LLM NER on Arabic mental-health questions; human gold validation appears limited to a drug-entity subset, and psychological entities seem LLM-judged only.

**Решение:** =

---

### 12 · R0093

**Keyphrase Generative Representation of Youth Crisis Conversations Beyond Static Taxonomies**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2605.27546

Crisis Responders (CRs) rapidly assess thousands of youth SMS conversations each year to identify mental health concerns and guide support. Yet youth distress is increasingly expressed through evolving and context-specific language that often does not fit fixed-label taxonomies. This work analyzed 703,975 de-identified Kids Help Phone conversations (2018-2023) and expanded KHP's 19-label issue taxonomy into a 39-label hierarchical schema. We then introduce Keyphrase Generative Representation (KGR), a constrained LLM generating concise, conversation-specific keyphrases, evaluated across 129 conversations and 387 expert annotations. The expanded taxonomy achieved expert consensus reliability, with an accuracy of 0.96, and expert review found that 81% of keyphrases accurately reflected content and 74% improved clarity. KGR surfaced identity-linked themes absent from the fixed taxonomy, including immigration problems and caregiver burden, and supported a topic-retrieval workflow that increased accuracy from 0.25 to 0.70 (+0.45) over the manual analyst process. KGR marks a shift toward hybrid, interpretable generative representations that extend crisis response beyond static taxonomies to surface emerging and culturally grounded patterns of youth distress.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM generates keyphrases for crisis conversations that experts review; unclear whether LLM labels on the taxonomy are compared with expert annotations.); Sonnet -2 (люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает: LLM generates keyphrases for crisis conversations and experts rate their quality; no LLM coding of the same units compared with human codes.)

**Решение:** -

---

### 13 · R0094

**Towards Understanding and Measuring COGNITIVE ATROPHY in LLM Behaviour**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2606.18129

Recent incidents involving LLMs used for mental-health support reveal a critical evaluation gap: surface-level safety scores do not capture how models behave across realistic, emotionally sensitive interactions over time. Existing benchmarks measure knowledge, safety, or static response quality, but miss whether LLM interactions help users keep reflecting, coping, and making decisions themselves. We formalize this missing dimension as COGNITIVE ATROPHY, a process-level behavioural measure in AI-mediated mental-health support distinct from safety and helpfulness. To measure it, we introduce COGNITIVE ATROPHY BENCH, a clinically grounded benchmark built from 1,576 fully human-generated counseling conversations, 15,680 turns, and 42,230 responses from five LLMs. Three clinical and neuropsychology experts developed a 20-attribute schema spanning user context, response behaviour, and global risk flags; six trained clinical reviewers applied it with span-grounded evidence, producing 5,324 reviewer judgments. We further introduce the User-Input Risk Index (UIRI), the Cognitive Atrophy Risk Index (ARI), and trajectory summaries. Across five LLMs, models show a consistent moderate-to-high level of atrophy-aligned behaviour across single and multi-turn settings. While models generally respond to overt safety cues, they adapt less reliably when users seek solutions or decisions. The dominant recurring patterns are directive advice, problem-solving, recommendation responses, topic shifts, and forms of validation that may reinforce dependence rather than reflection. Our work makes COGNITIVE ATROPHY measurable and provides a foundation for auditing model behaviour in sensitive LLM conversations.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Clinicians rated LLM mental-health responses with a schema; unclear whether an LLM judge was validated against these human judgments.

**Решение:** =

---

### 14 · R0126

**RECAP: Transparent Inference-Time Emotion Alignment for Medical Dialogue Systems**

2026 · Language Resources and Evaluation Conference (LREC) · journalarticle, conference, preprint/article · en · https://doi.org/10.63317/5epg4xxjjygt

Large language models in healthcare often produce emotionally flat or opaque responses, failing to provide the transparent reasoning required for clinical trust. We present RECAP (Reflect-Extract-Calibrate-Align-Produce), an inference-time framework grounded in cognitive appraisal theory that decomposes patient input into auditable, appraisal-theoretic stages without retraining. Across multiple benchmarks and models from 8B to 120B parameters, RECAP improves alignment with human judgments, with gains inversely proportional to model scale. Intermediate outputs further reveal that models systematically underweight relational factors such as social support. In blinded evaluations, oncology fellows rated RECAP responses significantly higher than baselines with 76-88% win rates, demonstrating that principled prompting can enhance medical AI's emotional intelligence while maintaining the transparency required for clinical deployment. LREC 2026: ClinicalNLP Workshop (Oral)

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Mainly generating responses, which clinicians then rated, but the benchmark 'alignment with human judgments' may compare LLM emotion/appraisal ratings with human labels.

**Решение:** =

---

### 15 · R0147

**Enhancing Empathetic Dialogue Generation in Open-Source LLMs via Emotion-Aware Prompting**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-37933-7_20

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus ? (нет аннотации: No abstract; title is about empathetic generation, but evaluation might compare LLM emotion or empathy ratings with human labels.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Title indicates empathetic dialogue generation via prompting; no sign of LLM coding or rating against human labels. No abstract available.)

**Решение:** -

---

### 16 · R0170

**Use of AI agents to cope with loneliness and social isolation: A sentiment and qualitative analysis of shared experiences, attitudes, and beliefs on Reddit**

2026 · OSF Registries · studyregistration/pre-registration, preprint, project · https://doi.org/10.17605/osf.io/tu5cs

With the rising trend in loneliness, an increasing number of people are turning to artificial intelligence (AI) agents to engage in interactions of personal nature. Little is known about how the public views the use of large language models (LLMs) as conversational agents or partners. This study will aim to understand public perspectives and experiences regarding the use of AI agents for loneliness or social isolation. We will conduct an LLM-assisted qualitative analysis of publicly available Reddit posts and comments collected via the open Python Reddit API Wrapper (PRAW) library, using pre-specified subreddit sets (AI-related and loneliness-related subreddits) and keyword filters. Deduplication of entries will be performed by unique post and comment identifiers. An LLM (GPT-5.2) will be employed to screen entries for eligibility based on a set of inclusion and exclusion criteria and to perform sentiment analysis on two dimensions on entries accepted post-screening: the overall emotional tone of each entry and the sentiment directed specifically toward AI use for loneliness or social isolation. Corpus-Aware Self-similarity Enhanced Topic modelling (CAST) will be performed on accepted entries as well, with LLM-assisted interpretation and human review to identify and refine emerging themes. To evaluate reliability, two independent human raters will annotate a random sample of entries for screening and sentiment. Agreement between the GPT model outputs and the human consensus ratings will be quantified using Cohen’s kappa.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: Pre-registration/protocol with no results; planned GPT-human kappa on emotional tone of loneliness Reddit posts. Track for the eventual results paper.); Sonnet + (проверка кодирования внутри исследования: Pre-registered study: GPT-5.2 sentiment/emotional tone coding of Reddit loneliness posts, validated against human raters' consensus with Cohen's kappa.)

**Решение:** -

---

### 17 · R0183

**Detecting Soft Skills in ML Engineering Roles CVs**

2026 · arXiv (Cornell University) · preprint/article, review, preprint · https://doi.org/10.48550/arxiv.2608.10046

Soft skills shape collaboration among ML engineers, data scientists, and software engineers building ML-enabled systems, yet what we know about them comes almost entirely from the demand side. Job advertisements, surveys, and hiring manager interviews capture what employers ask for. How candidates themselves articulate these competencies has not been studied, and existing CV-mining work is both keyword-based, so it cannot see skills conveyed through narrative, and descriptive, reporting frequency rankings without testing whether group differences exceed sampling variation. We close both gaps. Using a balanced corpus of 300 curated CVs spanning the three roles, we extract explicitly listed and implicitly narrated soft skills with an LLM-based pipeline validated against a human-annotated ground truth, a distinction that existing extractors were not designed to make. We then convert the demand-side literature's claims into 13 falsifiable hypotheses about role signatures, seniority progression, and disclosure style, and test them with effect sizes under family-wise error control, so that candidate-side data can corroborate or contradict the demand-side account rather than merely illustrate it. Eleven hypotheses are supported, one partially, and one refuted. Candidates disclose soft skills through narrative rather than keyword lists by roughly three to one, and most so for the competencies employers value most: leadership, coordination, and mentoring (88-96% narrative). Seniority nearly triples the odds of articulating leadership. That competency, assumed universal in prior work, is articulated by software engineers at half the rate of their peers. Technical candidates do articulate soft skills, but a keyword-based screening systematically misses them.

**ИИ:** ? · обе модели · неясен конструкт · The LLM's soft-skill extraction from CVs was checked against human annotation, but it is unclear whether CV soft skills count as a psychological construct.

**Решение:** =

---

### 18 · R0187

**Graph2Counsel: Clinically Grounded Synthetic Counseling Dialogue Generation from Client Psychological Graphs**

2026 · TUbilio (Technical University of Darmstadt) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2604.20382

Rising demand for mental health support has increased interest in using Large Language Models (LLMs) for counseling, but adapting them to this safety-critical domain is hindered by limited real-world data due to privacy constraints. Synthetic datasets provide a promising alternative, but existing approaches often rely on unstructured or semi-structured text inputs and overlook structural dependencies between a client's cognitive, emotional, and behavioral states, leading to psychologically inconsistent and less realistic interactions. We introduce Graph2Counsel, a framework for generating synthetic counseling sessions grounded in Client Psychological Graphs (CPGs) that encode relationships among clients' thoughts, emotions, and behaviors. Graph2Counsel uses a structured prompting pipeline guided by counselor strategies and CPG, and explores prompting strategies including CoT and Multi-Agent Feedback. It produces 760 sessions from 76 CPGs across diverse client profiles. In expert evaluation, our dataset outperforms prior datasets on specificity, counselor competence, authenticity, conversational flow, and safety (Krippendorff's $α$ = 0.70). Fine-tuning an open-source model on this dataset improves performance on several metrics on CounselingBench and CounselBench, while matching baselines on others. We further introduce Therapy-Eval, a multi-turn evaluation framework, and demonstrate the effectiveness of our fine-tuned model in realistic therapeutic conversations. We make our code, data and fine-tuned model public. 60 pages, 56 figures, 14 tables

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly synthetic counseling dialogue generation rated by experts; the Therapy-Eval framework may use an LLM judge, but validation against human ratings is unclear.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Synthetic counseling dialogue generation; experts rate the generated data, with no LLM coding or rating compared against human labels.)

**Решение:** -

---

### 19 · R0188

**A Resource-Efficient Codebook-Driven Semantic Structuring Pipeline for Human-AI Dialogue in Ambient Intelligent Systems**

2026 · Procedia Computer Science · conference-paper · en · https://doi.org/10.1016/j.procs.2026.04.070

Human–AI dialogue in ambient intelligent systems is increasingly relying on large language models (LLMs). When questions are generated dynamically to enable personalized and context-aware interactions, variations in phrasing and topical focus exist between conversations. Without structured organization, which is often extremely resource-intensive, conversational data remains fragmented and cannot be reliably used for systematic analysis or reporting. This study proposes a semantic structuring pipeline to map LLM-generated questions to shared codes, sub-themes, and themes using a predefined codebook. This multi-stage pipeline applies semantic screening, factor-based scoring, mathematical aggregation, and validation checks, supported by locally deployed LLMs and manual confirmation. The pipeline was evaluated on 6,030 question–response pairs collected from dynamic interviews across three research objectives. The framework achieved an overall mapping accuracy of 97% while reducing hallucinated semantic matches to 1.2% through layered validation. The results indicate that the framework effectively reduces hallucinated matches and improves mapping accuracy while remaining computationally efficient for private local deployment.

**ИИ:** ? · обе модели · неясен конструкт · LLM codebook mapping of interview questions, with accuracy checked against manual confirmation; unclear if the interview topics or codes are psychological.

**Решение:** =

---

### 20 · R0189

**Improving Quantized Model Performance in Qualitative Analysis with Multi-Pass Prompt Verification**

2026 · arXiv.org · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.48550/arxiv.2605.20193

Quantized Large Language Models (LLMs) are used more often in qualitative analysis because they run fast and need fewer computing resources. This study examines how different lower bits quantization levels (8-bit, 4-bit, 3-bit, and 2-bit) and quantization types affect the performance of LLaMA-3.1 (8B) on qualitative analysis. The study uses expert and non-expert responses from 82 interview transcripts. Low-bit models often produce higher levels of hallucinations and unstable results, especially when reading non-expert language with unclear terms. To improve performance, we propose a quantization-aware multi-pass prompt verification method. This method guides the model through controlled steps that reduce hallucinations. It removes unreliable content and passes the results to the next transcript after verification, improving accuracy. To validate performance, human coders analyzed transcripts using NVivo and BF16 LLaMA. BF16 LLaMA-3.1 produced high-precision output but had semantic drift and hallucination. These errors were corrected manually. The corrected BF16 output and NVivo human coding were combined to create a gold-standard ground truth (GSGT) for thematic extraction and frequency analysis. The results show that 8-bit models stay closest to the GSGT. The 4-bit models lose accuracy but become stable when the proposed method is applied. The 3-bit and 2-bit models drop in performance because of heavy compression, but they improve with the proposed prompt design and verification. The study also finds that models at the same bit level behave differently depending on quantization type. Overall, the method helps low-resource LLMs become more stable, accurate, and suitable for qualitative research at lower cost. Accepted to publish in 12th Intelligent Systems Conference 2026; 3-4 September 2026 in Amsterdam, The Netherlands

**ИИ:** разошлись — Opus ? (неясен конструкт: Quantized LLaMA codes interview transcripts against a human/NVivo gold standard; the interview topic and whether coding is at unit level are unclear.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Thematic extraction from interviews on quantized LLaMA; no clear psychological construct, and the ground truth merges corrected LLM output with human NVivo coding.)

**Решение:** -

---

### 21 · R0190

**LLM-Assisted Codebook Development for Cybersecurity Interviews with Enhanced Accuracy and Reduced Hallucination**

2026 · IEEE International Conference on AI in Cybersecurity (ICAIC) · conference, conference-paper · https://doi.org/10.1109/icaic67076.2026.11395872

Beyond what numerical data captures, qualitative cybersecurity interviews reveal human behaviors, lived experiences, trust perceptions and decision-making patterns. However, today’s current manual and software-assisted coding is slow, difficult to scale and subjective when distinguishing expert and non-expert perspectives. Consequent, recent development of Large Language Models (LLMs) makes them useful for qualitative analysis, but larger models remain costly despite lower hallucination, while smaller models alternatives are cheaper but less reliable. A codebook plays an essential role in structuring themes and interpreting qualitative data transparently and consistently. Therefore, this study proposes an LLM-assisted architecture to generate traceable and hierarchically structured codebooks from cybersecurity interviews. Five techniques were grouped into three areas: accuracy improvement, hallucination reduction, and reduction of context memory usage. These techniques were applied to measure performance, reliability, and coding quality from seven LLMs of various parameter sizes. The architecture produced an accurate codebook that improved coding reliability by up to 75% for non-expert and 35% for experts when compared to baseline manual extraction. Reduction of contextual memory use increased processing efficiency by over 40%, enabling even 1B–3B models to run effectively. Hallucination dropped by 82%, which demonstrates that trustworthy qualitative codes can be generated by small and mid-sized LLMs.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM generates codebooks from cybersecurity interviews (trust, behaviour); compared to manual coding, but unclear whether the constructs are psychological and the same units are coded.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM generates codebooks from cybersecurity interviews; no clear psychological construct or coding agreement with human coders on the same units.)

**Решение:** -

---

### 22 · R0191

**Evaluating Large Language Models for Psychological Diagnosis and Counseling: A Dual-Task Framework with Cultural Reflection**

2026 · Scientific Journal of Intelligent Systems Research · journalarticle, article · https://doi.org/10.54691/8f2d4016

Large language models (LLMs) have demonstrated high potential in healthcare and mental health related applications, however, their applicability to psychological diagnosis and counseling is not adequately investigated. This paper presents a dual-task assessment model that can be used to systematically evaluate how the mainstream Chinese LLMs can be used in psychology and through two lens psychological diagnosis and psychological counseling. In the diagnosis task, we test four Chinese LLMs, DeepSeek, Doubao, Kimi, and Tongyi Qianwen, on a mental health dataset that consists of five psychological disorders. Accuracy, Precision, Recall, F1-score, AUC, and confusion matrices are the measures of their diagnostic performance. In the case of the counseling task, we develop a prompt-based assessment system and evaluate the generated responses using six dimensions, including Overall, Empathy, Specificity, Medical Advice, Factual Consistency and Toxicity. To lower the expenses of annotating on the large scale with experts, we use an LLM-as-a-Judge approach to rank and evaluate the generated counseling answers. The experimental findings indicate that already existing Chinese LLM has some promising prospects in preliminary psychological diagnosis but fails to differentiate semantically similar disorders resulting in diagnostic confusion. The models themselves tend to produce fluent and empathetic responses in a counseling situation although they display obvious limitations in specificity, safety awareness, and dealing with medical advice. In addition, we also offer a case analysis and cultural reflection, pointing out that good average performance does not always imply the consistent support of culturally diverse adolescent groups. On the whole, our results indicate that the existing LLMs are more appropriate as an assistant, rather than a replacement of a mental health professional, and the research of the future should be aimed at enhancing the safety, cultural sensitivity, and clinical reliability of the system.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLMs classify text into five disorders, but the labels may come from humans or from self-report. The LLM judge seems not to be checked against humans.

**Решение:** =

---

### 23 · R0193

**CliniCIRCA: A Modular LLM Framework for Constructing Longitudinal Mental Health Patient Journeys from Raw EHR Narratives**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.19585

In mental health care, reasoning over patient journeys is a key task for clinicians. Yet these journeys, encompassing a longitudinal progression of biological, psychological, and social events, are often spread across disparate unstructured text narratives, making temporal recovery challenging. We present CliniCIRCA, a multi-stage LLM framework for Calendar-anchored, Imprecision-aware Reconstruction of Clinical Annals. To our knowledge, CliniCIRCA is the first to temporally classify clinical events across unstructured discharge summaries without event-level timestamps. From 14,882 MIMIC-III mental health admissions, we first construct a benchmark of 52 discharge summaries on which CliniCIRCA produces 15,891 temporally tagged events. After correcting 629 errors based on a clinician-in-the-loop evaluation, we produce verified gold-standard labels. Finally, the corrected timelines drive a temporally grounded summarization stage that compresses each source 1.52 times into a date-grouped chronological record. We then scale the framework to generate 1,000 silver-standard timelines and evaluate them as training data. Compared with zero- and few-shot prompting, instruction tuning generally improves five open-weight models on event extraction, temporal tagging, and summarization across silver and clinician-verified evaluations.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs pull out biopsychosocial events from mental health discharge summaries and tag their timing, checked against clinician-corrected labels; unclear whether the construct is psychological.); Sonnet -7 (другое — напишите почему: LLM event extraction and temporal tagging in discharge summaries, with clinician correction of LLM output. No psychological construct is coded against independent human coding.)

**Решение:** -

---

### 24 · R0204

**Identification of Stigmatizing and Biased Language in Mental Health Clinical Notes: A Classification Analysis using LLMs (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.113394

BACKGROUND Stigmatizing language in clinical documentation can negatively affect patient-centered care and contribute to bias in health care. Large language models are increasingly used for processing clinical notes, but their ability to identify stigmatizing language and their behavior across different linguistic and demographic contexts remain insufficiently understood. OBJECTIVE This study aimed to evaluate the ability of Large Language Models to identify stigmatizing language in clinical notes by analyzing classification of predefined stigmatizing instances against a gold standard annotation and independently identifying and extracting representative spans of stigmatizing language. The study also examined patterns in false negatives and assessed whether model classification performance varied across patient demographic groups. METHODS Three LLMs (Gemini-2.5-Flash, Phi-4, Qwen2.5-7B) were evaluated using 750 discharge summaries from MIMIC-IV. In contextual classification, models were provided with a candidate stigmatized keyword or phrase along with surrounding context and were asked to classify the candidate instance as either Stigmatizing or Non Stigmatizing. Classification performance was assessed using accuracy, precision, recall and F1 score. Pairwise model differences were evaluated using McNemar tests and classification performance was also examined across gender, age and race groups. False negative cases were further examined to identify recurring linguistic and contextual patterns. In LLM span detection and extraction, models were provided with the entire clinical note and instructed to identify a single, smallest contiguous span that could independently be classified as Stigmatizing Language. Model generated spans were independently assessed by a human annotator, and the agreement rate, disagreement rate, span hallucinations count, and span length were examined. RESULTS In contextual classification, Gemini-2.5-Flash achieved the highest performance, with an accuracy of 71.86% and F1-score of 71.74%, compared with 55.60% and 54.90% for Qwen2.5-7B and 49.86% and 48.10% for Phi-4, respectively. Pairwise comparisons showed statistically significant differences between all 3 models. Across demographic groups, all models generally demonstrated substantially higher accuracy for Not Stigmatizing Language than Stigmatizing Language. False-negative analysis identified recurring difficulties involving contextual distinctions, word forms, prefixes, and tense. In LLM span detection and extraction, human annotator agreement with model-generated spans was 18.36% for Gemini-2.5-Flash, 9.09% for Phi-4, and 5.57% for Qwen2.5-7B post removal of hallucinated spans. Models frequently generated spans that the human annotator did not consider stigmatizing. CONCLUSIONS LLMs demonstrated an ability to identify some stigmatizing language in clinical documentation, but their sensitivity to stigmatizing language was limited and varied across models and demographic groups. Analysis of false negatives revealed recurring linguistic and contextual patterns associated with missed instances. Independent span generation and human assessment further indicated that models may identify language as stigmatizing when it does not meet human annotation criteria. These findings highlight the need for careful evaluation of LLMs before their use in automated detection of stigmatizing language in clinical documentation.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs classify stigmatizing language in mental health clinical notes against gold-standard human annotation; unclear whether stigma counts as a psychological construct.); Sonnet + (бенчмарк с метками людей: LLMs classify stigmatizing language in mental health clinical notes against gold-standard human annotation, plus human assessment of extracted spans.)

**Решение:** +

---

### 25 · R0222

**Reliability-Aware Benchmarking of Large Language Models for Arabic Emotion Classification: Beyond Accuracy**

2026 · Research Square · preprint, ppr, posted-content · https://doi.org/10.21203/rs.3.rs-9427998/v1

Abstract Large Language Models (LLMs) are increasingly applied to emotion classification, yet Arabic benchmarks remain limited and oftenfocus solely on predictive performance. This work introduces a reliability-aware perspective through an abstention-aware benchmarkfor Arabic emotion classification. The benchmark is based on 1002 manually annotated sentences across five emotion categories,with very high inter-annotator agreement (κ = 0.9722). Our framework evaluates multiple LLMs under a unified zero-shot settingand explicitly models reliability through coverage, unknown-rate, and strict versus covered evaluation protocols. We further include acontrolled few-shot extension and supervised Arabic baselines (AraBERT and MARBERT) for contextual comparison. Results showthat GPT-4o and OpenAI-o3 achieve the strongest overall zero-shot performance, while few-shot prompting improves performancefor most models, particularly in accuracy and macro-F1, though gains are not fully uniform across systems. Importantly, wedemonstrate that predictive performance alone is insufficient to fully characterise real-world model behaviour, as reliability metricsreveal meaningful differences in output validity and deployment readiness. These findings highlight the importance of reliabilityawareevaluation for Arabic NLP and provide a more realistic framework for assessing LLMs in deployment-oriented scenarios.

**ИИ:** + · обе модели · бенчмарк с метками людей · GPT-4o, o3 and other LLMs classify emotions in Arabic sentences and are scored against manually annotated labels (κ=0.97 between annotators).

**Решение:** =

---

### 26 · R0232

**AI-aided Population-Level Comparisons of Early Maladaptive Schemas Between Singaporean and Global Online Communities**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-9546073/v1

Abstract We employed state-of-the-art large language models to analyze digital traces generated by young adults in Singapore and Western-dominated online mental health forums using Early Maladaptive Schemas (EMS) from Schema Therapy. Our social listening analysis indicates that EMSs related to academic performance, achievements, and self-worth are significantly prominent in Singapore forums whereas social isolation is emphasized on Western-dominated forums. Our scalable, theory-grounded framework can inform culturally-contextualized intervention design.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLMs code early maladaptive schemas in mental-health forum posts; the abstract doesn't say whether human-coded validation was done.

**Решение:** =

---

### 27 · R0241

**Hacia un marco de detección de emociones para la correspondencia histórica**

2026 · REVISTA DE HISTORIOGRAFÍA (RevHisto) · journalarticle, review, article · pt · https://doi.org/10.20318/revhisto.2026.10703

This study addresses the challenge of detecting emotions in sixteenth-century letters written or received by Spanish women. It offers, first, a discussion of the methodological issues involved in annotating emotions in historical personal correspondence; second, an analysis of emotion detection performed by human annotators on the corpus; and third, an empirical evaluation of three large language models (LLMs) applied to the same task. The corpus was annotated using Ekman’s six basic emotions supplemented by two additional categories, nostalgia and hope. To address the methodological challenges and validate the annotation framework, an interdisciplinary team of ten experts was assembled, a Likert-scale survey was conducted to assess the final annotations, and inter-annotator agreement was measured using Fleiss’s κ. Together, these steps constitute what we consider a significant advance toward the first gold-standard annotation system for historical correspondence, combining the participation of multidisciplinary experts as annotators, a rigorous multi-step validation strategy, an assessment of LLMs for emotion detection, and a critical discussion of their strengths and limitations in this domain.

**ИИ:** + · обе модели · бенчмарк с метками людей · Three LLMs detect emotions in 16th-century letters and are evaluated against expert human emotion annotations (Ekman categories plus nostalgia and hope).

**Решение:** =

---

### 28 · R0260

**A Critical Analysis of LLM Creativity Evaluation**

2026 · AMS Degree Thesis (University of Bologna) · dissertation, review · en

Large Language Models (LLMs) have fundamentally reshaped landscapes from academic research to industrial application. As computational resources scale, these models achieve remarkable proficiency in natural language generation, increasingly challenging human benchmarks in abstract domains like creative writing. However, accurately measuring creativity and understanding how LLMs relate to this complex construct remains a profound academic challenge. This thesis investigates the relationship between LLMs and creativity, asking not only whether these models can successfully simulate creative works, but also whether they possess the capacity to objectively evaluate them. Utilizing the WritingPrompts dataset, we conducted a multi-dimensional analysis combining automated objective metrics with subjective evaluations across 11 dimensions of creativity, assessed by both human judges and an LLM-as-a-Judge framework. Our findings highlight a profound dichotomy between how LLMs generate narratives and how they evaluate creativity. While the models produced highly sophisticated texts, a critical failure emerged during evaluation. We reveal an evident misalignment with human aesthetic standards and a severe systemic bias: the LLM judge consistently favors AI-generated texts over human unpredictability. Furthermore, Principal Component Analysis and correlation analyses demonstrate that current automated metrics are fundamentally inadequate, exhibiting near-zero alignment with human perception. This research concludes that while LLMs have brought unprecedented efficiency to countless domains, the nuances and beautiful imperfections of human creative products remain profoundly complex and difficult to understand; therefore, mathematically encoding them is still unfeasible. Until an artificial system can truly experience the world it is attempting to describe, creativity will remain a uniquely human milestone: a deeply complex aspect of the mind that algorithms have yet to “learn".

**ИИ:** ? · обе модели · неясен конструкт · An LLM judge and human judges both rated story creativity on 11 dimensions; unclear whether creative-writing quality counts as a psychological construct.

**Решение:** =

---

### 29 · R0264

**Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.28890

Evaluations of LLM-assisted qualitative coding almost universally measure model performance as agreement with human coders, a practice that presumes human coding is the standard to approximate. This study provides empirical evidence that the presumption fails in ways agreement metrics cannot detect. Five LLM systems and three trained human coders independently applied a 72-item hierarchical codebook to 2,560 educator messages from a K-12 AI platform. Beyond conventional agreement analysis, an independent domain expert judged 855 pairwise comparisons of code sets blind to source, treating human and machine sources symmetrically. The two evaluation approaches diverge in both directions. Human-LLM agreement (mean Jaccard 0.30) falls well below human-human agreement (0.52), which standard practice would read as inferior LLM coding, yet the blind verifier preferred human and LLM coding at indistinguishable rates (51.5% vs. 48.5%, p = 0.537), and a Bradley-Terry ranking placed two LLMs above two of three human coders. For several substantive codes, human consensus encoded shared bias that the verifier rejected in favor of the LLM interpretation. Agreement-based evaluation is therefore insufficient for automation decisions, and the study demonstrates a transferable verification protocol and a code-level division-of-labor framework.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM and human coders applied a codebook to educator messages and agreement is reported, but it is unclear whether any codes are psychological constructs.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLM and human coders applied a codebook to educator messages on a K-12 AI platform, which are educational usage data and not a psychological or clinical construct.)

**Решение:** -

---

### 30 · R0268

**PromptAlign: Automatic Iterative Alignment of a Large Language Model to Expert Annotations without Fine-Tuning**

2026 · Russian Digital Libraries Journal · journalarticle, article · https://doi.org/10.26907/1562-5419-2026-29-6-2265-2292

Large language models are increasingly used in social and psychological sciences; however, their predictions are systematically biased relative to expert annotations (alignment shift), and attempts to manually refine instructions or to supply examples lead to a “blanket-pulling” effect – degradation of minority classes. We propose PromptAlign, an automatic prompt-optimization pipeline that requires neither access to model weights nor human involvement in iterative correction, because the taxonomy and the feature space are specified by an expert a priori. The pipeline extracts hybrid linguistic and semantic features using the large language model itself, builds interpretable L1-regularized logistic regressions to localize disagreements with the expert, performs a meta-analysis of errors, and compiles new prompts while controlling the class balance through a class-imbalance index (Blanket Pulling Index, BPI). An experiment on a corpus of 541 Russian-language texts with three psychological classes showed an increase in macro-F1 on the held-out test set from 0.655 to 0.749 and in the minimum per-class F1 from 0.449 to 0.656 (p>0.99 by a paired bootstrap test). The method significantly outperforms both the zero-shot baseline and few-shot prompting. A component-contribution analysis confirms the critical role of semantic interpretation of features and of periodic prompt rebuilding. The final prompt contains five rules that reflect latent expert criteria; unlike the “black boxes” produced by automatic optimizers, these rules are available for inspection and correction by a specialist.

**ИИ:** + · обе модели · кодирование по кодбуку · An LLM classifies 541 Russian texts into three expert-defined psychological classes, with macro-F1 reported against expert annotations.

**Решение:** =

---

### 31 · R0274

**Using Large Language Models to Score the Minimal Instructions Autobiographical Memory Test (AMT-MIT): Comparing Human and LLM Raters on Autobiographical Memory Narratives**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/rqjzt

The primary aim is to assess agreement between LLM and human ratings using inter-rater reliability metrics. This will determine whether LLMs can provide a valid and efficient alternative to manual scoring. The study involves a non-clinical adult sample (18+), collects no identifying information, and presents minimal risk. Findings will inform the potential use of LLMs to scale and standardise autobiographical memory research.

**ИИ:** разошлись — Opus ? (другое: Pre-registration of LLM vs human scoring of AMT memory narratives; topic fits, but it is a protocol and results may not be reported yet.); Sonnet + (подсчёт методики: Pre-registered study of LLM scoring of autobiographical memory narratives (AMT-MIT) versus human raters, with inter-rater reliability as the primary outcome.)

**Решение:** -

---

### 32 · R0277

**"How Do I ...?": Procedural Questions Predominate Student-LLM Chatbot Conversations**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2602.18372

Providing scaffolding through educational chatbots built on Large Language Models (LLM) has potential risks and benefits that remain an open area of research. When students navigate impasses, they ask for help by formulating impasse-driven questions. Within interactions with LLM chatbots, such questions shape the user prompts and drive the pedagogical effectiveness of the chatbot's response. This paper focuses on such student questions from two datasets of distinct learning contexts: formative self-study, and summative assessed coursework. We analysed 6,113 messages from both learning contexts, using 11 different LLMs and three human raters to classify student questions using four existing schemas. On the feasibility of using LLMs as raters, results showed moderate-to-good inter-rater reliability, with higher consistency than human raters. The data showed that 'procedural' questions predominated in both learning contexts, but more so when students prepare for summative assessment. These results provide a basis on which to use LLMs for classification of student questions. However, we identify clear limitations in both the ability to classify with schemas and the value of doing so: schemas are limited and thus struggle to accommodate the semantic richness of composite prompts, offering only partial understanding the wider risks and benefits of chatbot integration. In the future, we recommend an analysis approach that captures the nuanced, multi-turn nature of conversation, for example, by applying methods from conversation analysis in discursive psychology. 14 pages, 2 figures

**ИИ:** ? · обе модели · неясен конструкт · 11 LLMs and human raters classified student chatbot questions with existing schemas; unclear if educational question types count as a psychological construct.

**Решение:** =

---

### 33 · R0281

**Group dynamics, personality and well-being in self-governed communities: a mixed-methods multi-site study (GRADIT)**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/jw259

Project overview. GRADIT (Group dynamics, personality and well-being in self-governed communities) is a cross-sectional, multi-site, convergent mixed-methods study with case-level merging that asks how individual characteristics (personality, values) and collective context (sense of community, conflicts, interpersonal trust, structural autonomy) jointly shape psychological need satisfaction and well-being in intentionally self-governed communities. Fieldwork was carried out in 10 self-governed communities across 5 countries (USA, Canada, Mexico, Colombia, Ecuador) and is trilingual (English, French, Spanish). The matched analytical sample comprises participants who completed both an interview and a questionnaire battery. Purpose. The study addresses six research questions (RQ1–RQ6) about the individual and collective factors of well-being in self-governed communities, the role of personality–context interactions, the loci of friction between individual aspirations and collective life, the impact of governance and conflict-management practices on resident well-being, the personality profiles that adapt to community life, and the cross-cultural generalisability of these patterns. The analytical core of the project is a multilevel mediation conceptual model (Figure 1) that was drafted by the PI before any data acquisition and that determined which questionnaires were included in the battery and which interview-grid sections were drafted. The 13 confirmatory hypotheses are a one-to-one operationalisation of the arrows in that diagram. Quantitative strand. Participants complete a questionnaire battery covering personality (HEXACO-60: 6 factors, 24 facets), values (Schwartz PVQ-40: 10 values plus 4 higher-order dimensions, ipsatized), well-being (WHO-5 and Subjective Vitality), sense of community (SCI-II: 4 subscales plus total), basic psychological needs (BPNSFS: autonomy, relatedness, competence — satisfaction and frustration subscales), interpersonal trust (ad-hoc Trust composite), and structural autonomy (ad-hoc SAS). Internal consistency is reported per subscale (Cronbach's α and McDonald's ω with 1 000-resample bootstrap CIs); the two ad-hoc scales undergo a pre-registered EFA + 1-factor CFA validation step. Qualitative strand. Each participant gives a semi-structured interview covering community organisation, conflict management, sense of belonging, and quality of life. Transcripts produced by OpenAI Whisper are manually verified against the original audio in full, de-identified inline, deterministically segmented, and analysed by a pre-registered LLM-assisted hybrid reflexive thematic analysis (Braun &amp; Clarke, 2022) with two human coders. The pipeline includes a 20% audit sample, a stratified 25% double-coded subset (≈ 5% of the corpus), a four-metric inter-rater reliability panel (Gwet's AC1, Cohen's κ, percentage agreement, Jaccard) with bootstrap 95% CIs and pre-registered pass thresholds, a paired non-inferiority test of the LLM against the human–human anchor, and a hallucination audit. Analytical framework. All confirmatory inference is Bayesian (brms on a Stan back-end), with weakly informative Normal(0, 1) priors on every standardised fixed-effect coefficient (the multiplicity safeguard) and a single decision rule applied uniformly across the 13 confirmatory hypotheses: posterior probability of direction pd ≥ 0.975 and 95% credible interval excludes zero on the focal coefficient. The 10 main-family hypotheses (H1–H10) operationalise the directed arrows of the conceptual model — personality and values shaping engagement; engagement shaping need satisfaction; need satisfaction shaping well-being; plus a direct, residual Personality → Well-being path. Three case-level hypotheses (H11–H13) test associations between conflict-related qualitative themes and personality, interpersonal trust, and need satisfaction in the matched subset. Mixed-methods integration is performed at the community, research-question, and case levels (joint displays, meta-inference matrix, latent-profile analysis, pen-portraits). Expected outcomes. The project will yield (i) a Bayesian estimate, with full credible intervals and probabilities of direction, of every directed path in the conceptual model — including the central Sense of Community → Need Satisfaction → Well-being mediation; (ii) a triangulated qualitative–quantitative account of the loci of friction in self-governed communities, with case-level joint displays linking each participant's questionnaire profile to themes coded from their own interview; (iii) cross-community comparisons of well-being and need satisfaction under different governance and conflict-management arrangements; and (iv) a reusable, fully open-source mixed-methods analytical infrastructure (frozen LLM prompts, scoring scripts, Bayesian model specifications, IRR computations) suitable for replication in other community-based studies. All confirmatory analyses, exploratory analyses, deviations, code, and the anonymised scored quantitative CSV will be archived on the OSF project page; the coded theme matrix is released in a quote-redacted public form, with full transcripts kept under restricted access for participant-protection reasons.

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: OSF pre-registration (protocol) with no results; it plans LLM-vs-human interview coding IRR, but protocols are ineligible.); Sonnet ? (другое: Pre-registration (protocol-like) of an LLM-assisted thematic coding of interviews with human double-coding and LLM–human IRR; no results reported, so check whether data exist.)

**Решение:** -

---

### 34 · R0282

**ADAPTS: Agentic Decomposition for Automated Protocol-agnostic Tracking of Symptoms**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.03212

Modeling latent clinical constructs from unconstrained clinical interactions is a unique challenge in affective computing. We present ADAPTS (Agentic Decomposition for Automated Protocol-agnostic Tracking of Symptoms), a framework for automated rating of depression and anxiety severity using a mixture-of-agents LLM architecture. This approach decomposes long-form clinical interviews into symptom-specific reasoning tasks, producing auditable justifications while preserving temporal and speaker alignment. Generalization was evaluated across two independent datasets ($N=204$) with distinct interview structures. On high-discrepancy interviews, automated ratings approximated expert benchmarks ($\text{absolute error}=22$) more closely than original human ratings ($\text{absolute error}=26$). Implementing an ``extended'' protocol that incorporates qualitative clinical conventions significantly stabilized ratings, with absolute agreement reaching $\text{ICC(2,1)} = 0.877$. These findings suggest that the ADAPTS framework enables promising evaluations of psychiatric severity. While the current implementation is purely text-based, the underlying architecture is readily extensible to multimodal inputs, including acoustic and visual features. By approximating expert-level precision in a protocol-agnostic manner, this framework provides a foundation for objective and scalable psychiatric assessment, especially in resource-limited settings.

**ИИ:** + · обе модели · клиническая оценка · LLM agents rate depression/anxiety severity from clinical interview transcripts; compared with expert and human clinician ratings (ICC reported).

**Решение:** =

---

### 35 · R0287

**Framing artificial intelligence: risk and benefit narratives in a preregistered experiment in Denmark**

2026 · AI & Society · journalarticle, review, article · en · https://doi.org/10.1007/s00146-026-03136-0

Abstract Public communication about artificial intelligence (AI) alternates between narratives of benefit and narratives of risk, but evidence on whether these frames move public opinion remains limited. We conducted a preregistered, three-arm online survey experiment in Denmark using a quota-based sample from a national panel. Respondents were randomly assigned to a neutral definition of AI, a risk-focused message paired with a cautionary image, or a benefit-focused message paired with an optimistic image. We measured overall evaluations of AI’s societal impact and agreement that AI erodes critical skills such as critical thinking and independent problem solving. We also elicited open-ended reflections on AI and job opportunities in respondents’ fields, as well as on generational dependence on AI, which we coded using a codebook-guided large language model workflow. We find that benefit framing increases positive overall evaluations relative to the neutral control, whereas the risk frame does not produce reliable change. In contrast, perceived skill erosion shows little movement across conditions, and open-ended reasoning about work and dependence exhibits similar thematic distributions across experimental arms. These results suggest that brief frames can nudge general sentiment about AI while leaving more specific capability concerns and immediate reasoning largely unchanged in a high-trust, highly digital welfare-state context.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM codebook coding of open-ended reflections on AI (attitudes/beliefs); unclear whether human coding validation is reported or if construct counts as psychological.

**Решение:** =

---

### 36 · R0308

**When Better Means Less: Quantifying What Benchmarks Miss Between Model Generations**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.18559492

On February 13, 2026, OpenAI will retire chatgpt-4o-latest and direct users to gpt-5.1-chat and gpt-5.2-chat as replacements. We test the substitutability claim through a controlled multi-dimensional comparison: 41 unique questions across three suites (Benchmark Bridge, Sycophancy-Empathy, Hostility Expansion) administered under two API conditions (chat and reasoning), nine multi-turn scenarios, and a 60-question false refusal rate battery, yielding 2,310 response specimens from all three models. Automated text metrics, blind LLM-as-judge evaluation, and three-rater reliability validation (Fleiss' kappa = 0.765) reveal dimension-specific trade-offs invisible to standard benchmarks. Auto-scored false refusal rates escalate from 4.0% to 17.7% (N=527, χ²=20.5, p<10⁻⁴); five LLM judges from four independent providers, applying a stricter rubric that captures borderline refusals, unanimously confirm the gradient at higher absolute rates (15.2% to 42.8%, Fleiss' κ=0.721). Creative engagement collapses from 34.3% to 5.1% of responses achieving full original content generation (6.7x). Exclamatory prosodic markers are near-completely eliminated (exclamation marks reduced up to 33x, p < .001, d=0.40). Benchmark scores are statistically identical (p=.135), yet judge-rated quality diverges (p=.001, d=0.11-0.14, negligible effect size) on the same questions. Conversely, multi-turn engagement and context awareness improve in 5-chat models (p<.001). We introduce two concepts: *alignment tax* -- the cost of alignment optimization decomposed into capability degradation (false refusal, creativity loss), style shift (affect, formatting), and dimension exchange (multi-turn gains) -- and *interpretive maximalism* -- the mechanism by which safety classification shifts from semantic to keyword-level evaluation, simultaneously driving false refusal escalation and creative capacity loss.

**ИИ:** разошлись — Opus ? (неясен конструкт: General LLM model comparison (refusal, creativity). Has a sycophancy-empathy suite with LLM judges and a three-rater check; unclear whether raters are human or the construct psychological.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Compares GPT model generations on refusals, creativity, and style using LLM judges; no psychological construct coded against human labels in clinical or psychological text.)

**Решение:** -

---

### 37 · R0314

**Classifying Emotion Expression in Mental Health Statements: A Comparison of Professionals, Laypeople, and LLMs**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/uzb3h

This study investigates inter-rater agreement and classification tendencies when identifying emotion expression in mental health context statements. Using a secondary dataset of 100 unique Reddit statements expressing emotional distress, we evaluate annotations across three distinct rater populations: Mental Health Professionals, Laypeople, and Large Language Models (GPT-3.5-turbo and GPT-4o-mini). First, we test whether mental health professionals demonstrate higher internal consensus (Krippendorff’s alpha) compared to laypeople when evaluating emotion expression. Second, we use Binary Logistic Mixed-Effects Models to examine whether overall classification tendencies differ between professionals and laypeople. Third, we test whether zero-shot automated ratings from LLMs align more closely with the rating tendencies of mental health professionals or those of laypeople. As exploratory extensions, we evaluate whether custom prompt engineering (via pre-annotated data from Safespace Research) improves LLM alignment with mental health professionals compared to zero-shot prompting, and examine whether specific statement-level metadata (e.g., word count) predicts classification disagreement across groups.

**ИИ:** разошлись — Opus ? (другое: GPT models vs professionals/laypeople on emotion coding of Reddit posts fits; but record is a preregistration, results may be unavailable.); Sonnet + (кодирование по кодбуку: Pre-registered study: GPT-3.5/GPT-4o-mini classify emotion expression in Reddit mental health statements, compared with professional and layperson annotations.)

**Решение:** -

---

### 38 · R0317

**The Point of View of a Sentiment: Towards Clinician Bias Detection in Psychiatric Notes**

2026 · Language Resources and Evaluation Conference (LREC) · conference-paper · en · https://doi.org/10.63317/2dxaipemahpd

Negative patient descriptions and stigmatizing language can contribute to generating healthcare disparities in two ways: (1) read by patients, they can harm their trust and engagement with the medical center; (2) read by physicians, they may negatively influence their perspective of a future patient.In psychiatry, the patient-clinician therapeutic alliance is a major determinant of clinical outcomes.Therefore, language usage in psychiatric clinical notes may not only create healthcare disparities, but also perpetuate them.Recent advances in natural language processing systems have facilitated the efforts to detect discriminatory language in healthcare.However, such attempts have only focused on the perspectives of the medical center and its physicians.Considering both physicians' and non-physicians' subjective points of view is a more equitable approach to identifying harmful language in clinical notes.By leveraging large language models (LLMs), this work aims to characterize potentially harmful language usage in psychiatric notes by identifying the sentiment expressed in sentences describing patients based on the reader's point of view.First, we curated a psychiatric lexicon containing words commonly used to describe patients in psychiatry.Sentences (N=39) were extracted from clinical text containing psychiatric lexicon at a medical center, with which a set of physicians (N=10) and non-physicians (N=10) annotated them as negative, neutral, or positive.Three LLMs (GPT-3.5,Llama-3.1, and Mistral) used zero-shot/few-shot in-context learning (ICL) approaches to classify the sentiment of the sentences according to the physician or non-physician point of view.Results showed that GPT-3.5 aligned best to physician point of view and Mistral aligned best to non-physician point of view, both with an ICL approach.These results underline the importance of recognizing subjectivity in clinical annotation tasks, not only for improving the note writing process, but also for the quantification, identification, and reduction of bias in computational systems for downstream analyses.

**ИИ:** разошлись — Opus ? (неясен конструкт: LLMs classify sentiment of psychiatric-note sentences against physician and non-physician annotations; unclear whether sentiment/stigma toward patients counts as a psychological construct.); Sonnet + (клиническая оценка: LLMs (GPT-3.5, Llama-3.1, Mistral) classify sentiment of patient-describing sentences in psychiatric notes, compared against physician and non-physician annotations.)

**Решение:** +

---

### 39 · R0324

**A methodological tutorial in Python for automated content analysis of digital videos using artificial intelligence**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-8817867/v1

Abstract Background . The exponential growth of short social media videos has created new opportunities for research. Nevertheless, traditional video content analysis remains labor-intensive and therefore difficult to scale. This methodological paper provides a practical step-by-step tutorial for conducting automated content analysis of digital videos using a multimodal large language model (LLM, Gemini 3 Pro) via an application programming interface (API). Methods . Using Python in a cloud notebook environment, we demonstrate how to (1) collect a public dataset of TikTok videos, (2) upload videos to Google API Files, (3) apply a codebook-based prompt to extract structured variables, (4) enforce the outputs to a JSON template, (5) implement robust error handling and reprocessing logic, and (6) export results for statistical analysis. The tutorial is illustrated with an open dataset of 1,028 TikTok videos on weight loss, yielding one JSON record per video that includes video description, topic classification, and identification of explicit weight-loss product advertising, plus additional attributes (e.g., framing, identity, narrative type, call to action) when advertising is detected. Results . The full run produced 1,028 JSON files in 11.39 hours at a cost of USD $20.27 dollars. Human–LLM coding agreement, assessed on a random subset using Krippendorff’s alpha, was high (mean 94.87%). Conclusion . The provided Python code and results demonstrate that the method employed here is very useful and can be escalated to analyze thousands if not hundreds of thousands of short digital videos.

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: Gemini codes TikTok weight-loss videos for topic, advertising, framing, and call to action. These are marketing categories in video, not psychological constructs in text.); Sonnet ? (неясен конструкт: Gemini codes TikTok weight-loss videos with a codebook and reports human–LLM alpha, but the constructs (ads, topic, framing) and the video modality may not count as psychological text.)

**Решение:** -

---

### 40 · R0331

**Artificial Intelligence Tools for Analyzing Forensic Linguistic Features of Arabic Texts in a Comparative Case Study**

2026 · Research Square · preprint, ppr · https://doi.org/10.21203/rs.3.rs-9312779/v1

Abstract This study examined how effectively current artificial intelligence (AI) and Arabic natural language processing (NLP) tools can support forensic linguistic analysis of Arabic judicial texts when compared with expert manual coding. Using a comparative evaluation design, it analyzed a purposive corpus of Saudi criminal judgments drawn from Majmuat al-Ahkam al-Qadaiyya (Ministry of Justice, 1435 AH/2013–2014 CE), focusing on cases in which psychiatric evidence and claims of diminished capacity were central. The Pragmatic-Doctrinal Inference Model (P-DIM) was implemented through a five-layer annotation framework covering: (a) the institutional weight of psychiatric evidence, (b) the temporal framing of illness, (c) formulaic constructions of legal capacity and responsibility, (d) pragmatic-argumentative function in judicial reasoning, and (e) evidential stance and certainty grading. Two trained analysts applied the scheme in a CAQDAS-supported workflow and established inter-coder agreement before adjudication. In parallel, an AI-assisted pipeline combining large language model classification with Arabic-specific preprocessing was used to identify the same layers through controlled prompting and constrained outputs. Performance was assessed through precision, recall, F1 scores, agreement analysis, and qualitative error profiling. Results showed that AI performance differed markedly by inferential complexity: it was strongest for structurally stable, genre-formulaic layers, especially formulaic legal capacity and institutional weighting, but weaker for context-dependent layers requiring pragmatic interpretation. A one-way ANOVA revealed a significant effect of P-DIM layer on performance, F (4, 15) = 245.57, p N = 120), supporting a hybrid workflow in which AI assists screening while expert judgment remains essential.

**ИИ:** ? · обе модели · неясен конструкт · LLM coding of judicial texts compared with expert coders; the codes are legal-linguistic features of psychiatric evidence, so the psychological construct is borderline.

**Решение:** =

---

### 41 · R0342

**Analysing Differences in Persuasive Language in LLM-Generated Text: Uncovering Stereotypical Gender Patterns**

2026 · arXiv (Cornell University) · journalarticle, conference, preprint/article · en · https://doi.org/10.18653/v1/2026.findings-acl.1742

Large language models (LLMs) are increasingly used for everyday communication tasks, including drafting interpersonal messages intended to influence and persuade. Prior work has shown that LLMs can successfully persuade humans and amplify persuasive language. It is therefore essential to understand how user instructions affect the generation of persuasive language, and to understand whether the generated persuasive language differs, for example, when targeting different groups. In this work, we propose a framework for evaluating how persuasive language generation is affected by recipient gender, sender intent, or output language. We evaluate 13 LLMs and 16 languages using pairwise prompt instructions. We evaluate model responses on 19 categories of persuasive language using an LLM-as-judge setup grounded in social psychology and communication science. Our results reveal significant gender differences in the persuasive language generated across all models. These patterns reflect biases consistent with gender-stereotypical linguistic tendencies documented in social psychology and sociolinguistics. Accepted at ACL Findings 2026

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM judge codes 19 social-psychology persuasion categories in LLM text; abstract doesn't say whether the judge was checked against human annotations.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM-as-judge rates LLM-generated persuasive text for bias; no human-coded comparison reported in the abstract and the texts are not psychological or clinical text.)

**Решение:** -

---

### 42 · R0358

**Exposing Weaknesses in Emotion Recognition in Conversations**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2609.05806

Emotion Recognition in Conversations (ERC) aims to identify speakers' emotions in multi-turn dialogue. Accurate emotion recognition can support a wide range of applications, including empathetic conversational agents, mental health support, and educational technologies. While many recent approaches rely on task-specific fine-tuning, such models may exploit dataset-specific cues. A central yet rarely questioned assumption in ERC is that each utterance can be assigned a single unambiguous emotion label. To investigate this assumption, we study ERC using Large Language Models (LLMs) in a zero-shot setting while incorporating preceding conversational turns as context. We show that aggregate metrics mask systematic failures. Errors concentrate around utterances containing negations, exclamations, and interjections. This pattern is consistent across all evaluated models, suggesting limitations in the benchmarks rather than model-specific weaknesses. A controlled re-annotation study involving four human annotators supports this finding: strong agreement is observed in only 35 percent of cases, with neutral utterances dominating high-agreement instances, while many emotional categories fall into low-agreement regimes. These findings suggest that many apparent model errors reflect genuine annotation ambiguity rather than poor emotion understanding. Standard single-label evaluation is therefore insufficient. To address this limitation, we introduce an LLM-as-Judge framework that evaluates each emotion independently according to its plausibility in the conversational context rather than enforcing a single-label decision.

**ИИ:** + · обе модели · бенчмарк с метками людей · Zero-shot LLMs label emotions in dialogue utterances, evaluated against ERC benchmark labels and a four-annotator human re-annotation.

**Решение:** =

---

### 43 · R0383

**Fine-Tuned Large Language Models for Inclusive Education Athlete Support: Performance Evaluation and Benchmarking**

2026 · Lecture notes in networks and systems · conference-paper · en · https://doi.org/10.1007/978-3-032-04160-9_1

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: No abstract; title suggests fine-tuned LLMs for educational athlete support, with no sign of coding psychological text against human raters.); Sonnet ? (нет аннотации: No abstract; title suggests fine-tuned LLMs for athlete support in education, likely generation. Compatibility with human-coded psychological text is unclear.)

**Решение:** -

---

### 44 · R0402

**Which Model Feels Better? A Comparison of Computational Approaches to Emotion Detection in Social Media with Imbalanced Data**

2026 · Informatics · journalarticle, article · en · https://doi.org/10.3390/informatics13060077

Emotion detection in social media remains challenging, particularly in polarized public debates where emotional expression is often imbalanced across categories. Addressing this challenge, this study compares the performance of multiple computational approaches using a gold-standard dataset of tweets about an ongoing geopolitical conflict. The dataset reflects the authentic, skewed distribution of emotions observed in real-world online discourse. We evaluated lexicon-based methods, classical machine-learning classifiers, deep-learning architectures, transformer models in both fine-tuned and zero-shot configurations, and a zero-shot large language model to assess their effectiveness in capturing both frequent and less frequently expressed emotions. Across approaches, transformer models, especially those fine-tuned for contextual emotion recognition, demonstrated the strongest overall performance, with emotion-specific fine-tuning offering a particular advantage for detecting rare emotion categories. These findings emphasize the importance of evaluating emotion detection methods under realistic class imbalance and highlight both the comparative strengths and limitations of widely used modeling strategies in applied social media research. This study advances emotion analysis and computational social science by offering practical guidance for selecting appropriate emotion detection methods in complex, imbalanced social media contexts.

**ИИ:** + · обе модели · бенчмарк с метками людей · A zero-shot LLM is tested against gold-standard emotion labels on tweets, which are probably human-annotated, and accuracy is compared with other methods.

**Решение:** =

---

### 45 · R0415

**Implementasi Large Language Model dengan Pendekatan Self-RAG pada Dashboard Sistem Penilaian Wawancara (Studi Kasus: Seleksi Wawancara Local Project AIESEC in UNHAS)=Implementation of a Large Language Model Using a Self-RAG Approach in an Interview Assessment System Dashboard (Case Study: Local Project Interview Selection at AIESEC in UNHAS)**

2026 · Hasanuddin University Repository · dissertation · id · https://repository.unhas.ac.id/id/eprint/57575/2/H071221026-1-2.pdf

Proses seleksi wawancara manual pada rekrutmen berskala besar sering kali menghadapi kendala inefisiensi waktu dan subjektivitas penilai (interviewer bias). Penelitian ini bertujuan untuk mengembangkan sistem penilaian wawancara otomatis yang mampu memberikan skor dan umpan balik secara objektif dan transparan. Sistem dikembangkan menggunakan Large Language Model (LLM) Qwen-2.5-7B yang diintegrasikan dengan arsitektur Self-Reflective Retrieval Augmented Generation (Self-RAG). Pendekatan ini diterapkan untuk memitigasi masalah halusinasi pada model bahasa dengan cara mengambil acuan penilaian dari basis data vektor rubrik secara dinamis dan melakukan mekanisme koreksi diri (self-correction) sebelum menghasilkan penilaian akhir. Kinerja sistem dievaluasi melalui uji skenario pada 40 sampel jawaban kandidat yang divalidasi oleh pakar (Expert Judgment). Hasil evaluasi menunjukkan tingkat kesepakatan yang tinggi antara sistem dan ahli, dibuktikan dengan nilai Quadratic Weighted Kappa (QWK) sebesar 0,8454 yang tergolong dalam kategori Almost Perfect Agreement. Evaluasi komponen internal menunjukkan performa optimal dengan nilai Hit Rate dan Faithfulness mencapai 100%, mengindikasikan validitas penalaran yang kuat. Berdasarkan uji penerimaan pengguna, sistem memperoleh skor kelayakan sebesar 79,17% dengan kategori "Layak/Baik". Penelitian ini menyimpulkan bahwa sistem dapat diimplementasikan secara efektif sebagai "Asisten Cerdas" untuk tahap penyaringan awal (screening) guna meningkatkan efisiensi proses seleksi.

**ИИ:** ? · обе модели · неясен конструкт · Qwen scored recruitment interview answers against a rubric and agreed with experts (QWK 0.85); unclear if rubric constructs are psychological (competencies or personality).

**Решение:** =

---

### 46 · R0432

**REGARD: Regional Affective Differences in Large Language Models**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.20722

Large language models trained and aligned within different linguistic and regional ecosystems may frame the same political, cultural, and geopolitical entities in different ways. Such differences are often evaluated through sentiment, favorability, or stance, reducing model attitudes to a single positive-negative axis. We introduce REGARD, a study of what drives affective framing differences across LLMs on post-Soviet entities using target-directed Valence-Arousal-Dominance profiling. We query 19 models on 500 region-specific targets, score their responses with two independent LLM judges, GPT-4o-mini and Qwen3.6-35B-A3B, and validate the measurements on a 300-item human-annotated subset. Post-hoc Ward-linkage clustering of all 19 models by affective and response-behavior profiles yields three behavioral clusters that cut across model origin, family, and parameter count. Generic-answer rate is strongly associated with lower arousal (r = -0.81) and with cluster placement: models that deflect evaluative prompts with templated responses cluster together at low arousal regardless of origin. These findings show that VAD profiling captures emotional intensity, a dimension of affective framing that is largely invisible to conventional sentiment-based evaluation. 17 pages, 11 figures, 3 tables. Includes evaluation of 19 language models, two independent VAD judges, and human validation on 300 items

**ИИ:** ? · обе модели · неясен конструкт · LLM judges score valence-arousal-dominance of LLM answers about political topics, checked on 300 human-annotated items; construct is close to political sentiment.

**Решение:** =

---

### 47 · R0433

**Regional Affective Differences in LLMs**

2026 · Lecture notes in computer science · conference-paper · en · https://doi.org/10.1007/978-3-032-41546-2_16

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The title suggests LLM affective ratings that might be compared with human regional affect ratings; the full text is needed to check.

**Решение:** =

---

### 48 · R0434

**VIBE: A VAD-Informed Benchmark for Entity-Centered Affective Profiling of Large Language Model Outputs**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.03810

Large language models routinely describe socially salient targets, including political figures, countries, religions, organizations, historical events, and social groups, encoding affective framing alongside factual content: a target may appear favorable or threatening, calm or conflictual, powerful or vulnerable. Existing work captures parts of this space through sentiment, favorability, and emotion benchmarks, but none combines target-directed VAD attribution, an explicit scorer contract, and a passport reporting format. We introduce VIBE, a benchmark for entity-centered affective profiling of LLM outputs in Valence-Arousal-Dominance (VAD) space. Its core contribution is a measurement contract: VIBE separates generation from external scoring, distinguishes scalar favorability, response-level VAD, and target-directed VAD, and reports profiles through an Affective Passport. Three empirical layers support the contract. H1 shows scalar favorability does not subsume arousal and dominance: valence findings are cross-validated (rV = 0.944 judge-human, rV = 0.954 inter-scorer); arousal and dominance are single-scorer directional estimates, not point-precise, consistent with known inter-annotator difficulty on these axes (rA = 0.495, rD = 0.702 among human annotators). H2 shows whole-response and target-directed VAD are different contracts: the same text can carry one affective tone overall while representing the named target differently. H3 is a protocol-drift diagnostic: elicitation conditions shift profiles, motivating context metadata in every affective report. These results motivate entity-centered affective profiling as a documented practice: profiles should be released with scorer identity, coverage, protocol, and interpretation limits. 25 pages, 13 figures, 22 tables. Submitted to ACL Rolling Review, August 2026

**ИИ:** ? · обе модели · неясен конструкт · LLM judge scores VAD affect of LLM texts about entities against human annotators; the construct is closer to sentiment toward targets than to psychological text.

**Решение:** =

---

### 49 · R0438

**Whose Assessment of Distress? Community Perspectives and LLM Alignment on Well-Being Posts**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.29446

Judgments about psychological distress are socially situated: what counts as concerning hinges on community norms around emotional expression, vulnerability, and help-seeking. Yet large language models (LLMs) used for distress detection are typically aligned to a single, undifferentiated standard. How well do these models capture the perspectives of the communities whose language they assess? We address this question through a perspectivist annotation study in which 321 participants provided 9,587 judgments on 1,198 Reddit posts spanning six identity-based communities, yielding community-specific labels. Raters in the contextualized in-group condition show a modest tendency to agree more with their community than uncontextualized out-group raters (OR = 1.18), an effect varying significantly across communities. We then evaluate nine open-weight LLM configurations and four frontier configurations against these labels. Open-weight LLMs systematically over-estimate distress: when communities perceive none-to-mild distress, these models achieve only 31-44% accuracy, predominantly producing false positives. GPT-5 and Gemini 2.5 Pro show the same none-to-mild inflation even when their full-sample over/under rates are mixed, while Claude Opus 4 is more conservative. This pattern does not simply mirror an outsider reading position: uncontextualized out-group human aggregates were nearly symmetric, with 18% over-estimation versus 19% under-estimation. Instead, the models that inflate none-to-mild cases exhibit a distress prior that exceeds both contextualized in-group and uncontextualized out-group human judgments. These findings have implications for equitable AI deployment in mental health contexts, where miscalibrated distress detection may unevenly affect the communities being assessed.

**ИИ:** + · обе модели · бенчмарк с метками людей · LLMs rated distress in Reddit posts and were compared with community human annotator labels; accuracy and over-/under-estimation were reported.

**Решение:** =

---

### 50 · R0453

**Evaluating Large Language Models in the Assessment of Collaborative Problem-Solving Skills: Evidence from Classroom Dialogue**

2026 · preprint · https://doi.org/10.35542/osf.io/xh27a_v1

The increasing use of large language models (LLMs) is reshaping how collaborative learning processes are analysed and assessed. In collaborative problem-solving (CPS), assessment commonly relies on human coding of dialogue for fine-grained social and cognitive skills. However, such judgments are difficult to scale, and their construct clarity is rarely examined. While recent studies suggest that LLMs may support qualitative coding of collaborative skills, limited research has examined whether different models apply CPS frameworks consistently or how their reasoning aligns with expert human judgments. To address these gaps, this study applies an ensemble of LLMs to code the presence of CPS subskills, defined by an established CPS framework, in transcripts of collaborative dialogue from CPS contexts. Our study shows that LLM-human alignment is achievable for some subskills but varies systematically across the framework. Analysis of model and human-generated rationales indicates that points of model disagreement correspond to persistent ambiguities in human coding rather than isolated model error. These findings highlight how LLM ensembles can be used not only to support CPS coding but also to diagnose the clarity and evidentiary limits of dialogue-based CPS frameworks. By synthesising agreement, disagreement, and model reasoning, this work positions LLM ensembles as transparent decision-support tools for educational research, offering a foundation for refining CPS frameworks and guiding responsible use of LLMs in collaborative learning assessment.

**ИИ:** ? · обе модели · неясен конструкт · LLMs code collaborative problem-solving subskills in dialogue against human codes; unclear whether these educational social-cognitive skills count as psychological constructs.

**Решение:** =

---

### 51 · R0461

**Transcript-based DASH scoring with personalized large language models: a mixed-methods concordance study and measurement considerations**

2026 · Advances in Simulation · journalarticle, review, article · en · https://doi.org/10.1186/s41077-026-00477-0

Abstract Background Debriefing is central to healthcare simulation, yet quality assessment relies on expert raters and substantial faculty time. Large language models (LLMs) may support transcript-based quality review using validated instruments such as the Debriefing Assessment for Simulation in Healthcare (DASH). Still, evidence is needed on agreement patterns and the constraints of transcript-only assessment. This study compared concordance between human experts and personalized ChatGPT models for DASH scoring of debriefing transcripts. Methods A prospective, multicentric pilot study with a mixed-methods design analyzed 33 high-fidelity simulation debriefings. Transcripts were evaluated by human experts ( n = 150 evaluations) and personalized GPT-4.0 and GPT-4.5 models ( n = 345 evaluations total) using DASH items 2–6 (score range 5–35). An adaptive design selected the best-performing AI model based on internal consistency (Cronbach’s α ≥ 0.7) and inter-evaluator concordance (ICC ≥ 0.5). Quantitative analyses included continuous and categorical concordance measures, and qualitative analysis used comparative content analysis. Results GPT-4.5 demonstrated superior performance (α = 0.870) compared with GPT-4.0 (α = 0.427) and was selected for the main analysis. Continuous analyses showed moderate concordance with human experts (ICC range 0.290–0.560; median 0.455). Categorical analyses showed high agreement (95–100%; PABAK 0.900–1.000) in a dataset in which ratings were predominantly classified as “Good.” Qualitatively, both experts and GPT-4.5 frequently identified similar strengths, while experts more often provided specific, critical improvement-oriented feedback, and the model tended toward a predominantly positive, descriptive tone. Conclusions In transcript-only scoring of DASH items 2–6, a personalized GPT-4.5 model demonstrated strong internal consistency and moderate concordance with expert ratings on continuous scales, while coarse categorical classifications yielded high agreement in a predominantly high-scoring sample. These findings support a human-supervised role for LLMs in structuring transcript-based review and potentially triaging debriefings for faculty development workflows, rather than substituting for expert assessment. Future work should test performance in more heterogeneous quality distributions and with multimodal observation beyond transcripts.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4.5 vs expert DASH scoring of simulation debriefing transcripts; it is unclear whether debriefing quality, an educational and interpersonal skill, counts as psychological.

**Решение:** =

---

### 52 · R0469

**Behavioral Modeling of Interpersonal Dynamics as Controllable Agentic Systems: Empirically-grounded Adaptive Virtual Patients for Psychotherapy**

2026 · KiltHub Repository · dissertation/thesis, dissertation · https://doi.org/10.1184/r1/33415387

Demand for mental health care exceeds the capacity of the available clinical workforce. As a result, psychotherapy training often relies on limited supervision and uneven access to appropriate practice cases. Although standardized patients can provide controlled practice opportunities, they require substantial human resources and may raise practical and ethical concerns. Advances in generative AI have enabled large language model (LLM)-based virtual patients to support open-ended interactions. However, a persona prompt alone does not specify how a patient’s behavior—such as disclosure, affect, or trust—should evolve over the course of a session in response to therapist interventions. Multiparty settings, such as couples therapy, pose an additional behavioral-modeling challenge because each client’s behavior depends not only on the therapist but also on the other client. This dissertation frames virtual-patient behavior as an explicit state-update process in which a separate controller updates psychological or interactional states in response to therapist interventions and other interactional inputs, while the language model generates dialogue consistent with those evolving states. Chapter 2 develops LLM-based measures of therapist empathy and probing skills, therapist--client rapport, client disclosure, and client emotion. It then models the therapist-client dynamics using structural equation modeling to estimate turn-level associations among these variables in a large corpus of psychotherapy transcripts. Chapter 3 applies the dynamic modeling to the design of an adaptive virtual patient whose disclosure state changes in response to a therapist’s use of empathy and probing skills. Chapter 4 extends the approach to simulate interactions among two client agents and a therapist. A stage controller coordinates six stages of couples therapy and a recurrent demand--withdraw pattern between the two agents. By separating behavioral state transitions from language generation, this framework makes the underlying dynamics explicit and inspectable. Evaluations of both interactive systems—the individual virtual-patient and couples-therapy simulations—provide evidence that this approach can produce behaviorally faithful interactions that clinicians view as useful for training. More broadly, this work illustrates how agentic AI can broaden access to deliberate practice that develops, rather than replaces, human expertise.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Chapter 2 builds LLM measures of therapist empathy, rapport and client disclosure in therapy transcripts; validation against human coders is likely but not stated.

**Решение:** =

---

### 53 · R0470

**Empirical Modeling of Therapist-Client Dynamics in Psychotherapy Using LLM-Based Assessments**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2602.12450

Psychotherapy is a primary treatment for many mental health conditions, yet the interplay among therapist behaviors, client responses, and the therapeutic relationship is difficult to study at scale, as process research has relied on labor-intensive human coding. We develop and validate a computational framework for modeling therapist-client interaction, using large language models (LLMs) to measure therapist behaviors (empathy, exploration), relational quality (rapport), and client outcomes (self-disclosure, self-directed and outward-directed negative emotion). After validating model-generated scores against human annotations (ICC = 0.45-0.81; rapport 0.81, self-disclosure 0.78), we apply these measures to roughly 2,000 hours of transcripts from the Alexander Street corpus and use Structural Equation Modeling to estimate moment-to-moment relationships among therapist behaviors, rapport, and subsequent client responses, controlling for prior client state and context. Therapist empathy and exploration directly predict increased client disclosure and shifts in emotional expression; empathy is more strongly associated with self-directed than outward-directed negative emotion, suggesting greater acknowledgment of internal distress, while exploration increases disclosure and emotional elaboration. Rapport does not directly amplify disclosure or emotional intensity but instead moderates the associations between therapist behaviors and client affect, potentially contributing to reductions in internal distress. These results show that LLM-based measurement combined with structural modeling can capture core therapeutic processes at scale, with empathy and exploration acting directly and rapport as a contextual moderator, providing a foundation for precision modeling of psychotherapy and for scalable therapist training and AI-supported clinical education.

**ИИ:** + · обе модели · кодирование сессий · LLM rated therapist empathy, rapport and client disclosure in therapy transcripts; checked against human annotations (ICC 0.45–0.81).

**Решение:** =

---

### 54 · R0471

**The Empirically Grounded Adaptive Virtual Patient for Psychotherapy Training: Disclosure That Responds to Therapist Micro-Skills**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.10051

Simulated patients offer a scalable way to train psychotherapy micro-skills such as empathic responding and exploratory probing, but current systems either follow fixed scripts or rely on LLMs that drift unpredictably over long sessions. We present the Adaptive Virtual Patient (AVP), which adapts its disclosure behavior -- from guarded, through moderate openness, to full disclosure -- in response to trainee skill. The AVP is grounded in a structural equation model fit to nearly 2{,}000 hours of real-world psychotherapy transcripts, which quantifies how therapist empathy and exploration shift a patient's openness over time. An LLM generates the AVP's utterances conditioned on a disclosure level that the dynamics module updates each turn. In an evaluation with 20 clinicians and trainees over 80 sessions (1{,}033 turns), the AVP's disclosure rises in response to therapist empathy and exploration, while a prompt-only baseline stays flat; ablations confirm that the empirically motivated parameterization outperforms alternatives, with exploration carrying most of the adaptive signal.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly an LLM simulated patient, but therapist empathy/exploration coding may be LLM-based and checked against human labels.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: An LLM-driven virtual patient that generates utterances. The abstract reports no LLM coding of text compared against human labels.)

**Решение:** -

---

### 55 · R0472

**Therapist–Client Dynamics in Psychotherapy Using LLM-Based Assessments: An Empirical Study (Preprint)**

2026 · JMIR Publications Inc. · posted-content, preprint · https://doi.org/10.2196/preprints.95389

BACKGROUND Psychotherapy is a primary treatment for many mental health conditions, yet the dynamic interplay among therapist behaviors, client responses, and the therapeutic relationship remains difficult to disentangle at scale. Traditional process research relies on labor-intensive human coding, limiting the ability to model moment-to-moment therapeutic dynamics across large datasets. OBJECTIVE This study aimed to develop and validate a computational framework for modeling therapist–client interaction processes and to examine how therapist behaviors and relational qualities shape client disclosure and emotional expression in psychotherapy sessions. METHODS We developed automated assessment pipelines using large language models (LLMs) to measure therapist behaviors (empathy, exploration), relational quality (rapport), and client outcomes (self-disclosure, self-directed negative emotion, outward-directed negative emotion). Model-generated scores were validated against human annotations. We then applied these measures to approximately 2,000 hours of psychotherapy transcripts from the Alexander Street corpus. Structural Equation Modeling (SEM) was used to estimate moment-to-moment relationships among therapist behaviors, rapport, and subsequent client responses. Models controlled for prior client state and contextual factors to isolate direct and moderated effects. RESULTS Automated measures demonstrated fair to excellent agreement with human ratings (ICC = 0.45–0.81), with constructs such as rapport (ICC = 0.81) and self-disclosure (ICC = 0.78) falling in the excellent range (ICC = 0.75–1.00), supporting construct validity. SEM analyses revealed that therapist empathy and exploration directly predicted increased client disclosure and shifts in emotional expression. Empathy showed a stronger association with self-directed negative emotions than outward-directed emotions, suggesting increased acknowledgment of internal distress. Exploration was associated with increased disclosure and emotional elaboration. In contrast, rapport did not directly amplify disclosure or emotional intensity; instead, it moderated associations between therapist behaviors and client affect, potentially contributing to reductions in internal emotional distress. Model fit indices supported the adequacy of the structural model (all fit indices within accepted thresholds). CONCLUSIONS This study demonstrates that LLM-based measurement combined with structural modeling can capture core therapeutic processes at scale. Empathy and exploration exert direct, moment-to-moment effects on client disclosure and emotional direction, whereas rapport primarily functions as a contextual moderator. These findings provide a computational foundation for precision modeling of psychotherapy processes and offer actionable insights for scalable therapist training and AI-supported clinical education systems.

**ИИ:** + · обе модели · кодирование сессий · LLM rated therapist empathy, exploration, rapport and client disclosure/emotion in therapy transcripts; validated against human annotations (ICC 0.45–0.81).

**Решение:** =

---

### 56 · R0475

**Evaluating Large Language Models for Feature Extraction from Verbal Stimuli: A Simulation-Based Workflow**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/xphm9_v1

Large Language Models (LLMs) are increasingly used as research tools to facilitate the fast and automated extraction of text features. In psychological studies, they have been used to quantify the degree to which verbal stimulus materials reflect certain psychological constructs. However, the application of LLMs entails a high degree of flexibility regarding prompt design (e.g., instruction details and examples) and model specification (e.g., model family, size, and configuration), which can produce divergent results and threaten the robustness and generalizability of conclusions. To navigate the multiverse of possible choices, we develop a structured workflow for evaluating the quality of LLM feature extraction across diverse model and prompt specifications. Motivated by generalizability theory, the workflow distinguishes between construct variance across stimulus items, method variance due to model and prompt choices, and error variance across repeated iterations. To guide researchers through the planning, execution, and reporting of LLM simulation studies, we introduce an adapted version of the ADEMP template (Aims, Data-generating mechanism, Estimands and targets, Methods, Performance measures), originally developed for methodological simulation research. The template supports two complementary validation strategies: variance decomposition for studying consistency across LLM specifications and external validation against human gold-standard ratings. In a pre-registered case study using locally runnable, open-weight LLMs, we illustrate the workflow by examining the influence of model choice, response format, and prompt examples on the quality of valence and arousal ratings for multi-word expressions. We additionally assess the efficacy of aggregating repeated, stochastic LLM ratings to improve feature extraction quality.

**ИИ:** ? · обе модели · неясен конструкт · LLM valence/arousal ratings of multi-word expressions checked against human gold-standard norms; unclear whether word stimuli count as psychological text.

**Решение:** =

---

### 57 · R0481

**DAL Team at PsyDefDetect: From Supervised Encoders to Hierarchical LLM-RAG for Psychological Defense Detection**

2026 · Proceedings of the BioNLP 2026 (Shared Tasks) · conference-paper · https://doi.org/10.18653/v1/2026.bionlp-2.23

The PsyDefDetect shared task focuses on classifying nine psychological defense mechanisms in multi-turn dialogues, a problem complicated by severe label imbalance and the implicit, context-dependent nature of defenses. In this work, we investigate several approaches for dialogue-level defense detection, including supervised baselines and large language model (LLM)-based pipelines. Our primary system is a retrieval-augmented LLM framework with hierarchical prediction and lightweight heuristics for decision calibration. Experiments on the PSYDEFCONV dataset show that LLM-based methods improve overall performance compared to supervised baselines, but still struggle with fine-grained distinctions, especially for minority labels. These findings highlight the challenges of modeling implicit psychological constructs in dialogue.

**ИИ:** + · обе модели · бенчмарк с метками людей · LLM-RAG classifies psychological defense mechanisms in dialogues, evaluated against PSYDEFCONV labels, which are likely human-annotated.

**Решение:** =

---

### 58 · R0482

**Human vs LLM in Conversational Repair Annotation: A New Resource and Comparative Study**

2026 · International Conference on Language Resources and Evaluation · journalarticle · https://doi.org/10.63317/32stceuq67kb

Addressing the scarcity of annotated data for Other-Initiated Repair (OIR), when recipients interrupt conversation progressivity to signal trouble, prompting speakers to provide repair, this work introduces OIR annotations for the NOXI corpus, achieving considerable reliability. We evaluate whether LLMs can reliably annotate OIR sequences using structured Chain-of-Thought prompting and conduct comparative analysis across two corpora: NOXI (natural dialogue) and CABB-S (Dutch, task-oriented), finding weak alignment between LLMs and human annotations, particularly in recognizing trouble signaling. Analyzing human-LLM disagreement using the LLM-generated explanations revealed limitations: models rely on lexical patterns rather than conversational context, construct reasonable-sounding but misleading narratives, highlighting crucial limitations for both automated annotation of complex interactional phenomena.

**ИИ:** ? · обе модели · неясен конструкт · LLM vs human annotation of other-initiated repair in dialogue; unclear whether conversational repair counts as a psychological/interpersonal construct.

**Решение:** =

---

### 59 · R0511

**ARR Rebuttal Evidence Bundle for Bengali/Banglish Conversational Sycophancy Benchmark**

2026 · Zenodo (CERN European Organization for Nuclear Research) · peerreview/, peer-review · https://doi.org/10.5281/zenodo.21300404

This anonymous supplemental bundle contains compact evidence tables prepared for ARR rebuttal and revision planning. The files provide aggregate and per-audit-row statistics supporting revised analyses of a Bengali/Banglish conversational sycophancy benchmark. The bundle includes: majority and stratified-random baselines for binary and five-class settings; clean five-class model results with bootstrap confidence intervals and coverage; generation results recomputed under strict sycophancy, defined as Validation + Escalation, with Support reported separately; GPT-assisted annotation correction and class-wise disagreement summaries; an inventory of qualitative-analysis support files; a partial top-comment sensitivity audit over a recovered 170-example source-comment subset. The top-comment audit contains no raw post/comment text and uses anonymized audit row identifiers rather than platform IDs. The audit is partial: it covers one recovered source-comment subset, not the full multi-community benchmark. Full second/third-comment sensitivity would require restoring the remaining source-comment exports. The available generation-judge spreadsheet contained human-label columns, but those columns were empty for all rows; therefore, this bundle does not claim class-wise human agreement for generated-response judging. This upload is intended only as anonymous rebuttal evidence. It does not include author names, local paths, raw social-media text, Hugging Face links, or non-anonymous release links.

**ИИ:** ? · обе модели · неясен конструкт · Supplemental rebuttal bundle for a benchmark of sycophancy in Bengali social-media comments with human labels; unclear if sycophancy counts as psychological and if LLMs are compared.

**Решение:** -

---

### 60 · R0551

**The Effect of AI-Generated Images on Visual Vividness in Expressive Writing: A Secondary Analysis of Existing Datasets**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/v4qxc

Background and Objectives Expressive writing has been widely used to facilitate emotional expression and psychological regulation. Its effectiveness is partly attributed to the situational processing of experiences and the construction of mental representations. According to grounded cognition theory, cognitive processes are rooted in perceptual and action systems, and language comprehension is often accompanied by mental simulation (Barsalou, 2008). During text processing, individuals construct situation models and mentally simulate linguistic content (Zwaan, 2016). In addition, mental imagery plays a critical role in memory, emotional experience, and thinking (Kosslyn et al., 2006). Prior research has shown that textual vividness is closely associated with the richness of perceptual representations it evokes (Jajdelska et al., 2010). With the development of generative artificial intelligence, AI-generated images can provide real-time visual feedback based on textual input, potentially enhancing mental imagery during writing. The present study focuses on the following question: Whether AI-generated images influence the visual vividness of the written text itself. Using existing datasets, this study introduces a novel text-based measure—visual vividness—to examine the impact of AI-generated images on expressive writing. Data Source The present study is based on two previously conducted experiments: Study 1 AI-Generated Image Improve the Efficacy of Expressive Writing on Reducing College Students' Employment Pressure Study 2 Can AI-Generated Images Empower Expressive Writing All data have been collected following the original experimental protocols. Prior to this preregistration, no statistical analyses have been conducted on visual vividness. This study constitutes a theory-driven secondary analysis of existing data. Hypotheses Study 1 H1 In the negative experience writing task, texts produced in the AI image condition will exhibit higher visual vividness than those in the no-image condition. H2 Within the no-image condition, negative experience writing will show higher visual vividness than neutral writing. H3 There will be an interaction between image condition and writing type, such that the effect of AI-generated images on visual vividness varies across writing conditions. Study 2 H4 Texts produced in the AI image condition will exhibit higher visual vividness than those in the traditional (no-image) condition. H5 Visual vividness will increase across repeated writing sessions. H6 The increase in visual vividness over time will be greater in the AI image condition than in the traditional condition. Procedure Study 1 Participants were randomly assigned to one of two conditions: AI image condition Participants wrote about a personal negative experience. During writing, corresponding images were generated approximately every one to two sentences and presented in real time. No-image condition Participants completed the same writing task while viewing a fixed neutral background image unrelated to the writing content. All participants followed the same procedure: Before the main writing task, participants completed a baseline writing task on a neutral topic (a typical day in the past week). They then proceeded to the main task, writing about a personal negative experience. In the AI condition, images were generated in real time based on the text. In the no-image condition, only a fixed neutral image was displayed. After writing, participants completed psychological measures. All text data have been collected. Sample Size (Study 1) Study 1 included a total of 202 participants: AI image condition: 101 No-image condition: 101 All participants completed both baseline and main writing tasks. Study 2 This study employed a randomized controlled design. Participants A total of 184 valid participants (completed at least three writing sessions) were included: AI image condition: 93 Traditional condition: 91 Pre-intervention Assessment Participants first completed a baseline questionnaire. They read a passage about employment insecurity to induce stress, followed by attention checks. Measures included: Emotions (joy, anger, sadness, fear) Employment confidence Psychological distress (DASS-21) Sleep quality (PSQI) Stress mindset Demographic information Writing Intervention Approximately two days after the pretest, participants completed a 4-day expressive writing intervention. Each day, participants wrote for approximately 15 minutes on an online platform. Writing prompts focused on employment-related topics, including: Experiences of employment stress Effects on self-concept Future plans Potential positive changes In the AI image condition, images were generated approximately every short segment of text and presented to participants. Image generation was based on models such as Stable Diffusion (Kolors) and ChatGPT (4o-mini). In the traditional condition, participants viewed a fixed neutral background image unrelated to the writing content. After each session: All participants completed brief emotion ratings AI condition participants additionally reported: Image-content congruence Image-emotion congruence Scene vividness Writing immersion Writing motivation Post-test and Follow-up Participants completed the same measures as the pretest after the intervention and again at follow-up. All text data have been collected. AI-Based Coding of Visual Vividness A hybrid validation procedure will be used. First, 100 text samples will be randomly selected and manually annotated for visual vividness. Next, multiple AI models will be applied to the same dataset. The correlation between AI-generated visual vividness indices and human annotations will be calculated. If a model achieves a correlation coefficient greater than 0.60, it will be selected as the final coding model. The selected AI model will then be used to automatically code all remaining texts via API, using fixed parameters to ensure c

**ИИ:** разошлись — Opus -1 (обзор, протокол, комментарий, позиция, руководство: Pre-registration protocol; plans AI coding of vividness in expressive writing checked against human annotation, but no results reported yet.); Sonnet ? (другое: Preregistration plans AI (likely LLM via API) coding of visual vividness in expressive writing, validated against 100 human annotations. It is a protocol, so results may not be reported.)

**Решение:** -

---

### 61 · R0552

**CARE: An Explainable Computational Framework for Assessing Client-Perceived Therapeutic Alliance Using Large Language Models**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2602.20648

Client perceptions of the therapeutic alliance are critical for counseling effectiveness. Accurately capturing these perceptions remains challenging, as traditional post-session questionnaires are burdensome and often delayed, while existing computational approaches produce coarse scores, lack interpretable rationales, and fail to model holistic session context. We present CARE, an LLM-based framework to automatically predict multi-dimensional alliance scores and generate interpretable rationales from counseling transcripts. Built on the CounselingWAI dataset and enriched with 9,516 expert-curated rationales, CARE is fine-tuned using rationale-augmented supervision with the LLaMA-3.1-8B-Instruct backbone. Experiments show that CARE outperforms leading LLMs and substantially reduces the gap between counselor evaluations and client-perceived alliance, achieving over 70% higher Pearson correlation with client ratings. Rationale-augmented supervision further improves predictive accuracy. CARE also produces high-quality, contextually grounded rationales, validated by both automatic and human evaluations. Applied to real-world Chinese online counseling sessions, CARE uncovers common alliance-building challenges, illustrates how interaction patterns shape alliance development, and provides actionable insights, demonstrating its potential as an AI-assisted tool for supporting mental health care. 14 pages, 4 figures

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM rates alliance from counseling transcripts; main reference is client self-report, but CounselingWAI may include counselor or expert ratings.

**Решение:** =

---

### 62 · R0553

**Multi-dimensional Assessment and Explainable Feedback for Counselor Responses to Client Resistance in Text-based Counseling with LLMs**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2602.21638

Effectively addressing client resistance is a sophisticated clinical skill in psychological counseling, yet practitioners often lack timely and scalable supervisory feedback to refine their approaches. Although current NLP research has examined overall counseling quality and general therapeutic skills, it fails to provide granular evaluations of high-stakes moments where clients exhibit resistance. In this work, we present a comprehensive pipeline for the multi-dimensional evaluation of human counselors' interventions specifically targeting client resistance in text-based therapy. We introduce a theory-driven framework that decomposes counselor responses into four distinct communication mechanisms. Leveraging this framework, we curate and share an expert-annotated dataset of real-world counseling excerpts, pairing counselor-client interactions with professional ratings and explanatory rationales. Using this data, we perform full-parameter instruction tuning on a Llama-3.1-8B-Instruct backbone to model fine-grained evaluative judgments of response quality and generate explanations underlying. Experimental results show that our approach can effectively distinguish the quality of different communication mechanisms (77-81% F1), substantially outperforming GPT-4o and Claude-3.5-Sonnet (45-59% F1). Moreover, the model produces high-quality explanations that closely align with expert references and receive near-ceiling ratings from human experts (2.8-2.9/3.0). A controlled experiment with 43 counselors further confirms that receiving these AI-generated feedback significantly improves counselors' ability to respond effectively to client resistance. 8 pages

**ИИ:** + · обе модели · кодирование сессий · Fine-tuned Llama and GPT-4o/Claude rate counselor responses to client resistance; compared with expert-annotated quality ratings (F1).

**Решение:** =

---

### 63 · R0554

**Large Language Models to Define Social Determinants of Health from Patient-Reported versus Clinician-Documented Measures (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.99147

BACKGROUND Social determinants of health (SDOH) profoundly influence cancer and cardiovascular disease (CVD) risk, yet systematic extraction of SDOH from unstructured electronic health records (EHR) remains challenging. Traditional natural language processing (NLP) approaches require extensive manual annotation and institution-specific training data, while active SDOH screening imposes burden on patients and clinicians and is prone to missingness. Large language models (LLM) offer a promising alternative, but existing LLM-based SDOH extraction studies lack patient-level validation, are limited to constrained note types, and have not been validated against patient-reported outcomes. OBJECTIVE To develop and validate an LLM-based NLP framework for extracting SDOH from EHR at both the individual note and patient level, with comprehensive error analysis and comparison across both clinician-documented and patient-reported measures. METHODS From three independent cohorts, 100 patients were sampled and categorized into five distinct batches, and 97 patients yielded meaningful notes to construct the final dataset. Batch one was used for prompt development to evaluate five LLMs, with the best model then validated on the remaining four batches. Five SDOH domains were extracted: employment, financial toxicity, distress, food insecurity, and physical activity. Validation errors were categorized by a trained clinician at both the note-level (n=284) and patient-level (n=56). Agreement between clinician-documented and patient-reported SDOH measures was also assessed. RESULTS GPT-4.1 achieved 0.94 accuracy in the development batch. Across validation batches 2–5, GPT-4.1 achieved a note-level accuracy of 0.94 (SD 0.01; mean across batches) across the five SDOH domains, with an overall κ=0.72. Mean patient-level accuracy across validation batches was 0.88 (SD 0.04) for the five domains. Clinician-validated error analysis at both the note and patient level identified incorrect inferences as the predominant error type (note level, 57.7%; patient level, 44.6%). Clinician-documented and patient-reported SDOH showed moderate agreement (κ=0.17–0.52), with under-documentation of financial toxicity (58.8% agreement) and food insecurity (78.4%), and over-documentation of distress (69.1%). CONCLUSIONS GPT-4.1 provides validated SDOH extraction at both the note and patient level. Most errors stemmed from model interpretation rather than the model’s inability to find relevant information. Moderate agreement between documentation sources (patient-reported vs. clinician-documented) highlights their complementary value and the need to improve clinician documentation of SDOH domains. CLINICALTRIAL NCT01173341, NCT05078190, NCT05096338

**ИИ:** ? · обе модели · неясен конструкт · GPT-4.1 extracts SDOH from clinical notes against human validation (κ=0.72); most domains are social, but one (distress) is psychological.

**Решение:** =

---

### 64 · R0569

**Interpretable learning for detection of cognitive distortions from natural language texts**

2026 · PeerJ Computer Science · journalarticle, article · en · https://doi.org/10.7717/peerj-cs.3699

We developed a technology that, based on a dataset annotated for cognitive distortions, builds an interpretable model capable of detecting cognitive distortions in natural language texts. The novelty of the approach lies in the fact that the learning and detection methods are based on structural patterns such as N-grams, incorporating heterarchical relationships between them through the “priority on order” principle. We investigated and released two types of detection models: plain binary classification and a model based on a multi-class representation. We optimized the hyperparameters of the models and achieved an accuracy of 0.92 and an F 1-score of 0.95 in a cross-validation experiment. Additionally, we achieved over 1,000 times higher processing speed and lower computational cost compared to Large Language Model (LLM)-based alternatives.

**ИИ:** разошлись — Opus ? (другое: The main model is an n-gram classifier, not an LLM. LLM baselines may have been scored against the human cognitive-distortion annotations; check full text.); Sonnet -5 (нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM: Interpretable N-gram pattern model for cognitive distortion detection; LLMs only mentioned as speed/cost comparison, not as coder against human labels.)

**Решение:** -

---

### 65 · R0573

**A Hybrid Methodology for Qualitative Data Analysis in STEM Studies with a Gender Perspective**

2026 · DSpace Main Institutional Repository University of the North (Universidad del Norte) · article · es

La investigación sobre trayectorias y experiencias de mujeres en áreas STEM enfrenta importantes desafíos metodológicos debido a la complejidad interpretativa del análisis cualitativo y a la influencia de sesgos individuales durante los procesos de codificación. En este contexto, el estudio propone una metodología híbrida humano–LLM orientada al análisis de narrativas relacionadas con los constructos de legitimidad y pertenencia según el género. La propuesta integra un modelo de lenguaje de gran escala (LLM) como codificador adicional dentro de un proceso iterativo de comparación, refinamiento y validación entre codificadores humanos y artificiales. La metodología fue aplicada mediante pilotos sucesivos utilizando entrevistas cualitativas y evaluada a través del Alpha de Krippendorff para medir la consistencia entre codificadores. Los resultados evidenciaron mejoras progresivas en categorías como tipo de voz y modo discursivo, alcanzando niveles altos de acuerdo en algunos casos (α=0.87 entre humanos y α=0.85 entre humano–IA). Sin embargo, otras categorías, como dimensión, mantuvieron bajos niveles de concordancia (α≈0.46), lo que permitió identificar ambigüedades conceptuales y necesidades de refinamiento protocolario. Asimismo, se observó que la IA aún presenta dificultades para interpretar categorías discursivas complejas, por lo que no sustituye el juicio analítico humano, sino que funciona como un mecanismo complementario de contraste y detección de discrepancias. El estudio concluye que la integración híbrida humano–IA puede fortalecer la trazabilidad, auditabilidad y consistencia metodológica del análisis cualitativo, siempre que exista supervisión humana continua y refinamiento iterativo de los protocolos de codificación.

**ИИ:** + · обе модели · кодирование по кодбуку · An LLM coded interview narratives about gendered legitimacy and belonging in STEM, and its agreement with human coders was reported as Krippendorff's alpha (α=0.85).

**Решение:** =

---

### 66 · R0582

**Assessing the Potential of LLM-assisted Annotation for Corpus Pragmatics: The Case of Humor**

2026 · Corpus Pragmatics · journalarticle, article · en · https://doi.org/10.1007/s41701-026-00235-7

Abstract Corpus pragmatics faces ongoing challenges in quantitatively studying context-dependent categories like humor, given their subjectivity and the need for costly interrater reliability checks. Recent advances in LLMs offer a potential way to streamline these processes for pragmatic annotation tasks. This paper investigates that potential through an analysis of Italian political discourse on X, focusing on humorous tweets and their discursive functions (Attardo, 2020). We compare the performance of GPT-4o, LLaMA-3.3-70B-Instruct, and a novice annotator against that of an expert annotator. For the detection of humor, both models reached high agreement with the expert annotator (in particular, GPT-4o: Cohen’s k = 0.75; AC1 = 0.87). Instead, agreement dropped for the classification of humor functions (GPT-4o: Cohen’s k = 0.37; AC1 = 0.70). Qualitative results suggest that the models rely heavily on lexical cues rather than demonstrating deeper pragmatic competence. These findings indicate that while LLMs can provide useful assistance in the initial stages of large-scale annotation, they remain limited in capturing the nuanced and context-dependent nature of pragmatic functions.

**ИИ:** ? · обе модели · неясен конструкт · LLMs vs expert annotator on humor and humor functions in political tweets; pragmatic/linguistic construct, psychological relevance unclear.

**Решение:** =

---

### 67 · R0585

**Using Large Language Models to Construct Virtual Top Managers**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7611578

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: No abstract; the title suggests LLM simulation of executive personas in management research, not LLM–human coding of psychological text.); Sonnet ? (нет аннотации: No abstract; title suggests LLMs simulating top managers (possibly personality inference from text), compatibility with human-coded comparison unclear.)

**Решение:** -

---

### 68 · R0599

**Who Generates More Empathetic Responses—Humans or LLMs? A Comparative Evaluation with Human and LLM Judges**

2026 · Conference on Computational Natural Language Learning · conference-paper · https://doi.org/10.18653/v1/2026.conll-main.21

This paper compares the empathetic quality of responses generated by humans and large language models (LLMs).We evaluate four LLMs that were widely used at the time of study-GPT-4, LLaMA-2-70B-Chat, Gemini-1.0-Pro,and Mixtral-8×7B-Instruct-against a human baseline using a large-scale betweensubjects study.A total of 1,000 human participants evaluated the empathetic quality of human-and LLM-generated responses to 2,000 dialogue prompts spanning 32 positive and negative emotions.To complement human judgments, we also employed an LLM-asjudge (GPT-4o-mini) to assess the same responses.Across emotions and evaluators, LLM-generated responses were rated as significantly more empathetic than human-written responses.We also observed that both human judges and the LLM-as-judge tended to rate responses generated by their own group more favorably, indicating self-favoring tendencies.These findings highlight both the strong performance of contemporary LLMs in empathetic responding and the need to interpret humanand LLM-based evaluations with care.Empathy is the ability to understand and share the feelings of another person.It is the ability to put yourself in someone else's shoes and see the world from their perspective.Empathy is a complex skill that involves cognitive, emotional, and compassionate components.Cognitive empathy is the ability to understand another person's thoughts, beliefs, and intentions.It is being able to see the world through their eyes and understand their point of view.Affective empathy is the ability to experience the emotions of another person.It is feeling what they are feeling, both positive and negative.Compassionate empathy is the ability to not only understand and share another person's feelings, but also to be moved to help if needed.It involves a deeper level of emotional engagement than cognitive empathy, prompting action to alleviate another's distress or suffering.Empathy is important because it allows us to connect with others on a deeper level.It helps us to build trust, compassion, and intimacy.Empathy is also essential for effective communication and conflict resolution.You are engaging in a conversation with a human.Respond in an empathetic manner to the following using on average 28 words and a maximum of 97 words.

**ИИ:** + · обе модели · LLM-судья · GPT-4o-mini judge and human participants rated empathy of the same responses, so LLM–human agreement can be reported.

**Решение:** =

---

### 69 · R0636

**Measuring Creativity at Scale via Multimodal Large Language Models**

2026 · ACM Conference on Learning @ Scale · journalarticle, book, conference-paper · https://doi.org/10.1145/3774398.3811607

Recent literature in automated creativity measurement explores the use of large language models to measure creative tasks at scale, for example using text-based large language models to score text-based brainstorming activities or neural nets to rate images from a creative drawing task. Prior research has shown that educators of all levels want to gauge and support students' ability to be creative, but are often limited due to the time-consuming nature of existing creativity measurements, as well as a disconnect between validated instruments and class-based activities. This paper expands creativity measurement in several important ways. We leverage state-of-the-art multimodal large language models (MLLMs), trained on text, image, and other data, to not only model creativity tasks in a unitask approach (one model per task), but also in a multitask approach (one model for several tasks). We connect multimodal large language models to benchmarks established in psychological creativity research, and demonstrate that some MLLMs (notably native multimodal Llama 3.2 and Qwen 3-VL models) surpass the best scoring measurements by up to 5%, while other MLLMs (notably Llama 4-109B) need additional training procedures to accommodate limited fine-tuning data. We offer evidence of the ability of MLLMs to measure creativity based on human ratings, and explore future opportunities to advance multimodal creativity assessment within complex, real-world learning environments.

**ИИ:** + · обе модели · подсчёт методики · Multimodal LLMs (Llama, Qwen) score creativity tasks, including text-based divergent thinking, against human ratings from psychological creativity benchmarks.

**Решение:** =

---

### 70 · R0640

**Between Help and Harm: An Evaluation Study of Mental Health Crisis Handling by Large Language Models.**

2026 · JMIR mental health · journal article, evaluation study, journalarticle · eng · https://doi.org/10.2196/88435

Abstract Background The use of large language models (LLMs)–powered chatbots has reshaped how people seek information and advice, including for emotional and mental health support. While LLMs can offer scalable support, their ability to safely detect and respond to acute mental health crises—including suicidal ideation, self-harm, and violent thoughts—remains poorly understood. Progress is hampered by the absence of unified mental health crisis taxonomies, annotated benchmarks, and empirical evaluations grounded in clinical best practices. Objective We addressed these gaps by introducing (1) a unified taxonomy of 6 clinically informed mental health crisis categories; (2) an evaluation dataset of over 2000 user inputs drawn from 12 publicly available conversational mental health datasets, classified into crisis categories; and (3) an expert-designed protocol for assessing response appropriateness. We also used LLMs to automatically identify crisis-indicative inputs and conducted an auditing study of 5 LLMs to evaluate the safety and appropriateness of their responses. Methods We developed a taxonomy of mental health crisis categories informed by clinical experts and established literature. From over 239,000 mental health–related user inputs collected from 12 Hugging Face datasets, we curated 2252 examples (206 for validation, 2046 for testing) covering all taxonomy categories. We evaluated 3 LLMs on their ability to classify inputs into crisis categories, selecting the model with the strongest agreement with human annotators as the judge to label the test set. We then audited 5 LLMs on their ability to generate safe and appropriate responses to the 2046 test examples. Response quality was measured using a clinically informed 5-point Likert scale (1=harmful and 5=fully appropriate), relying on an LLM-as-a-judge validated against human expert feedback. Results Several LLMs exhibited high consistency and generally reliable behavior when responding to explicit crisis disclosures, but significant risks remain. A nonnegligible proportion of responses was rated as inappropriate or harmful, particularly in the self-harm and suicidal ideation categories. Substantial performance differences were observed across models: gpt-5-nano and deepseek-v3.2-exp achieved very low harmful response rates, whereas gpt-4o-mini, Llama-4-Scout-17B-16E-Instruct, and grok-4-fast-non-reasoning generated markedly higher rates of unsafe outputs. All models exhibited systemic weaknesses, including poor handling of indirect or ambiguous risk signals, reliance on formulaic responses, and frequent misalignment with user context. Conclusions These findings underscore the urgent need for enhanced safeguards, improved crisis detection, and context-aware interventions in LLM deployments and highlight the central role of alignment and safety engineering—beyond model scale or openness—in determining crisis response reliability. Our taxonomy, dataset, and evaluation framework lay the groundwork for ongoing research in artificial intelligence–driven mental health support, helping to minimize harm and protect vulnerable users.

**ИИ:** + · обе модели · LLM-судья · LLMs classified crisis categories in user inputs and were compared with human annotators; the LLM judge of response appropriateness was validated against human experts.

**Решение:** =

---

### 71 · R0642

**Towards Automatic ACT-Based Analysis of Chats**

2026 · ACM International Conference on Intelligent Virtual Agents (IVA) · book, conference, conference-paper · en · https://doi.org/10.1145/3806774.3827978

Affect Control Theory (ACT) models social interaction through culturally shared affective meanings, yet applying it to naturalistic dialogue requires manual event annotation whose inter-coder reliability has never been benchmarked. We report the first multi-coder reliability study for ACT event annotation, in which three trained experts independently coded 49 German exam-anxiety counseling chats. Experts varied substantially in annotation granularity (19–30 distinct behaviors, 26.0–38.5 events per chat) and produced low-to-moderate deflection agreement (pairwise r = −0.016 to 0.213). To assess automation feasibility, we developed an open-weight LLM agent (Qwen2.5-32B, local via Ollama) performing the full ACT pipeline. Across 10 runs the agent achieved high self-consistency (deflection ICC = 0.785, behavior Jaccard = 0.850). The agent’s strongest expert correlation (r = 0.392 with Expert 3) was the highest of any annotator pair, demonstrating that open-weight automation is feasible within the range of human agreement.

**ИИ:** + · обе модели · кодирование сессий · A Qwen2.5-32B agent annotated ACT events in exam-anxiety counseling chats, compared against three expert coders using correlations.

**Решение:** =

---

### 72 · R0665

**Hybrid artificial intelligence framework for patient emotion recognition in dentistry.**

2026 · Frontiers in oral health · journal article, journalarticle, article · eng · https://doi.org/10.3389/froh.2026.1909407

Introduction Emotional communication plays an important role in dentist-patient interactions, yet domain-specific resources for automated emotion recognition in dental consultations remain limited. Objective This study aimed to develop an emotional dental consultation corpus derived from restorative dentistry consultations and to evaluate a hybrid artificial intelligence (AI) framework for automated patient emotion recognition. Methods Audio recordings from 12 restorative dentistry consultations were transcribed and segmented into patient utterances. A total of 2,160 utterances were independently annotated into six emotion categories (Neutral, Fear, Sad, Happy, Angry, and Disgust) by three trained annotators using a standardized annotation framework. Inter-annotator reliability was assessed using Cohen's kappa coefficient. The resulting corpus was used to train a Bidirectional Long Short-Term Memory (BiLSTM) classifier and transformer-based baseline models, including BERT and RoBERTa. A hybrid framework was developed by applying large language model (LLM)-based confidence re-ranking to low-confidence BiLSTM predictions. Three open-source LLMs (Llama 3.1, DeepSeek-R1, and Qwen 2.5) were evaluated. Results The developed corpus demonstrated high annotation reliability ( κ = 0.89). Neutral (23.15%), Fear (19.44%), and Disgust (18.98%) were the most prevalent emotion categories. Fear was both one of the most frequently occurring emotions and the most challenging category to classify. The baseline BiLSTM model achieved a macro-F1 score of 0.87, whereas BERT and RoBERTa achieved macro-F1 scores of 0.89 and 0.91, respectively. The hybrid frameworks achieved numerically higher performance, with the BiLSTM + Qwen 2.5 framework obtaining the highest macro-F1 score of 0.92. However, the observed performance improvements were not statistically significant (all p > 0.05). Conclusion This study presents a novel emotion-annotated dental consultation corpus and demonstrates the feasibility of a confidence-based hybrid AI framework for automated patient emotion recognition in dentistry. Although the proposed framework achieved the highest numerical performance, the findings should be regarded as preliminary evidence of the potential utility of selective LLM-based re-ranking for recognizing emotionally ambiguous patient utterances.

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: Hybrid BiLSTM+LLM (Llama, Qwen, DeepSeek) emotion labels of patient utterances evaluated against labels from trained human annotators; LLM's role is partial.); Sonnet ? (другое: Human-annotated emotion corpus (κ=0.89); LLMs only re-rank low-confidence BiLSTM predictions, so LLM–human agreement may not be reported separately.)

**Решение:** ?

---

### 73 · R0706

**Scaling Equitable Reflection Assessment in Education via Large Language Models and Role-Based Feedback Agents**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/6rrv-d323

Equitable formative feedback remains out of reach for large or low-resource courses because instructors cannot read every learner reflection. We present a theory-grounded pipeline of five role-based LLM agents—Evaluator, Equity Monitor, Metacognitive Coach, Aggregator, and Reflexion Reviewer—that jointly produce calibrated rubric scores and $\le 120$-word, bias-aware comments. On $84$ reflections from a $12$-session AI-literacy program, the pipeline matches expert raters ($\mathrm{MAE}=0.47$, $\mathrm{QWK}=0.46$, human-AI $\mathrm{ICC}=0.41$) while bounding the worst-ability error gap to $\Delta{\mathrm{MAE}}=0.50$. Automated scoring finishes in $7.7\text{s}$ per reflection—an $11\times$ speed-up over the human mean of $1.4\text{min}$—and complete feedback in $33\text{s}$. A full agentic run costs just $0.0016$ per reflection. Three trained graders rated the AI feedback highly useful (overall $Q(g)=3.97/5$) with top marks for empathy ($4.22/5$). Contributions. (i) A self-consistent scoring scheme with equity safeguards; (ii) a role-based agent ensemble for dialogic, bias-aware feedback; and (iii) the first open dataset, prompts, and codebase for equitable reflection assessment. Together, these advances demonstrate a practical path toward large-scale, fair feedback in real classrooms.

**ИИ:** ? · обе модели · неясен конструкт · LLM agents score learner reflections against expert raters (QWK, ICC); unclear if the reflection rubric is a psychological/metacognitive construct or educational quality.

**Решение:** =

---

### 74 · R0709

**When to Stop? An Experimental Study on AI Teachable Agent Stopping Mechanisms and Their Learning Affordances in Mathematics**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/90xm-4e89

Teachable agents powered by AI offer a promising approach to enhance the engagement and understanding of middle school students, as they often face challenges in grasping mathematical concepts and procedures. However, during student-AI interactions, it is essential to determine when the agent should stop to effectively regulate the cognitive and emotional states of the students, which are factors closely linked to positive participation and productive tutoring strategies. This raises a key question: who should decide when the teachable agent stops or continues? Empirical evidence highlights the advantages of using LLM-as-a-judge and knowledge-graph–based decision-making, as well as the potential benefits of fixed-turn conversations. Drawing on 64,060 messages from 7,991 conversations across four randomly assigned stopping mechanisms - 8-turns, 16-turns, standalone LLM-as-a-judge, and agent decisions with knowledge graphs (KGs), our experimental results highlight that (a) agent decisions informed by KGs were most effective at detecting when conversations should continue, sustaining learner engagement with the teachable agent; (b) off-topic utterances occurred more frequently under fixed-turn conditions; and (c) tutoring strategies such as questioning for help or evaluation and elaborating with justification were most prevalent when agents used KGs for decision-making. Practical implications for designing effective agent-student interactions are discussed.

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Experiment comparing stopping mechanisms for a math teachable agent; the LLM judge controls the conversation and no LLM–human coding agreement is reported.); Sonnet ? (неясно, сравнивали ли с людьми: Educational teachable-agent study; LLM-as-judge decides stopping and tutoring strategies are coded, but no clear psychological construct or human-LLM agreement is stated.)

**Решение:** -

---

### 75 · R0716

**Being Kind Isn't Always Being Safe: Diagnosing Affective Hallucination in LLMs**

2026 · Underline Science Inc. · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48448/r0zh-6817

Large Language Models (LLMs) are increasingly engaged in emotionally vulnerable conversations that extend beyond information seeking to moments of personal distress. As they adopt affective tones and simulate empathy, they risk creating the illusion of genuine relational connection. We term this phenomenon Affective Hallucination, referring to emotionally immersive responses that evoke false social presence despite the model's lack of affective capacity. To address this, we introduce AHaBench, a benchmark of 500 mental-health-related prompts with expert-informed reference responses, evaluated along three dimensions: Emotional Enmeshment, Illusion of Presence, and Fostering Overdependence. We further release AHaPairs, a 5K-instance preference dataset enabling Direct Preference Optimization (DPO) for alignment with emotionally responsible behavior. DPO fine-tuning substantially reduces affective hallucination without compromising reasoning performance, and the Pearson correlation coefficients between GPT-4o and human judgments is also strong (r=0.85) indicating that human evaluations confirm AHaBench as an effective diagnostic tool. This work establishes affective hallucination as a distinct safety concern and provides resources for developing LLMs that are both factually reliable and psychologically safe. AHaBench and AHaPairs are accessible via https://huggingface.co/datasets/o0oMiNGo0o/AHaBench, and code for fine-tuning and evaluation are in https://github.com/0oOMiNGOo0/AHaBench. Warning: This paper contains examples of mental health-related language that may be emotionally distressing. EACL 2026 Findings

**ИИ:** + · обе модели · LLM-судья · GPT-4o judges affective hallucination in mental-health responses, validated against human judgments (r=0.85).

**Решение:** =

---

### 76 · R0720

**CentaurTA: A Self-Improving Human-Agents Collaboration Framework for Thematic Analysis**

2026 · Underline Science Inc. · audiovisual/conference talk, conference-paper, other · https://doi.org/10.48448/hv47-c360

Qualitative analysis is essential for studying complex social and behavioral phenomena, yet existing large language model (LLM) approaches face key limitations. Fully automated pipelines often compromise methodological rigor, while fully manual coding remains costly and labor-intensive. Although recent work emphasizes human–AI collaboration, existing multi-agent systems focus primarily on theme-level outputs, provide limited human oversight, and overlook fine-grained, data-level coding quality. We introduce \textbf{CentaurTA}, an iterative, self-improving human–agent framework for scalable thematic analysis. CentaurTA places humans in the loop to oversee and guide analysis, using expert feedback as a persistent learning signal to drive prompt-level refinement. By combining structured human feedback with rubric-based evaluation, CentaurTA provides fine-grained supervision for both open coding and theme construction while preserving methodological rigor. Experiments across multiple datasets, baselines, and LLM families show that CentaurTA improves coding alignment and transparency, highlighting the central role of human feedback in reliable qualitative analysis. Our code and data are available at https://github.com/Tom-Owl/CentaurTA.

**ИИ:** ? · обе модели · неясен конструкт · LLM open coding at the data level, with coding alignment measured against humans; unclear whether the datasets involve psychological constructs.

**Решение:** =

---

### 77 · R0721

**ChatAnime: Towards User-Centered Emotional Support in LLM-based Virtual Character Chat**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/ygf6-pf96

With the growing popularity of virtual character platforms like Character.AI, users are increasingly turning to role-playing agents for emotional support in daily life. Yet existing research mainly focuses on character consistency in fictional or game-based scenarios, overlooking user-centered interactions such as companionship and psychological support. To bridge this gap, we propose Emotionally Supportive Role-Playing (ESRP), a framework designed to align role-playing with real-world user scenarios and emotional needs. We focus on typical users of these platforms, i.e., anime enthusiasts—including students, office workers, freelancers, and self-employed individuals—and design scenario-based questions that reflect their everyday struggles such as work stress and social loneliness. Through a two-round data collection involving 40 anime fans and 10 Large Language Models (LLMs), we build ChatAnime: the first ESRP dataset with 2,400 human-written and 24,000 LLM-generated responses, supported by over 132,000 fine-grained human annotations. We also provide the ESRP evaluation framework featuring 9 fine-grained metrics across three dimensions: basic dialogue, role-playing and emotional support, along with an overall metric for diversity. Experimental results under our evaluation setting show that top-performing LLMs surpass anime fans in role-playing and emotional support, while humans still lead in diversity.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Humans annotated emotional-support responses in detail; unclear whether an LLM judge was checked against these human annotations.); Sonnet -2 (люди оценивают ответы LLM, а LLM сам ничего не кодирует и не оценивает: Dataset of human and LLM role-play responses rated by human annotators; no LLM rating task compared with human labels is described.)

**Решение:** -

---

### 78 · R0724

**CMTD: Cognitive Modeling with Traits and Distortions for Multimodal Emotion Recognition in Conversations**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/fcvk-2n37

This paper introduces a new multi-agent framework, CMTD (Cognitive Modeling with Traits and Distortions), for multimodal emotion recognition in conversations (MERC). Instead of relying on shallow analysis of emotions, CMTD reconstructs a cognitive model by taking advantage of stable personality traits, dynamic cognitive distortions, visual and acoustic features of interlocutors to enhance the emotional intelligence of LLMs. CMTD includes trait, distortion detection, vision, and speech agents that provide psychological and multimodal indicators for the fusion agent to make the final prediction. Experimental results on MELD and IEMOCAP show that traits temper negativity bias from distortions, and cognitive modeling with psychological, visual, and acoustic information can improve the performance of MERC. CMTD is flexible and easy to adapt to advanced emotional AI systems (Github link: https://github.com/Shaun-le/CMTD.git).

**ИИ:** разошлись — Opus + (бенчмарк с метками людей: An LLM multi-agent framework classifies emotions in conversations and is evaluated against the human-annotated MELD and IEMOCAP labels.); Sonnet ? (неясно, сравнивали ли с людьми: Multi-agent LLM emotion recognition on MELD/IEMOCAP, which have human-annotated labels. It's a method paper that is multimodal, so the human-agreement framing is unclear.)

**Решение:** ?

---

### 79 · R0725

**Cognitive Policy-Driven LLM for Diagnosis and Intervention of Cognitive Distortions in Emotional Support Conversation**

2026 · Underline Science Inc. · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48448/8ntz-4t53

Emotional Support Conversation (ESC) plays a critical role in mental health assistance by providing accessible psychological support in real-world applications. Large Language Models (LLMs) have shown strong empathetic abilities in ESC tasks. Yet, existing methods overlook the issue of cognitive distortions in help-seekers’ expressions. As a result, current models can only provide basic emotional comfort, rather than helping help-seekers address their psychological distress at a deeper cognitive level. To address this challenge, we construct the CogBiasESC dataset, the first dataset that expands existing ESC datasets by adding labels for cognitive distortions, includes their type, intensity, and safe risk level. Furthermore, we propose the Cognitive Policy-driven Large Language Model framework (CoPoLLM) to enhance LLMs' ability to diagnose and intervene cognitive distortions in help-seekers. We also analyze the safety advantages of CoPoLLM from a theoretical perspective. Experimental results show that CoPoLLM significantly outperforms 15 state-of-the-art baselines in terms of distortion diagnosis accuracy, intervention strategy effectiveness, and safety risk control. Our source code is available at: https://github.com/Chips98/CoPoLLM-for-ACL-2026.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLM cognitive-distortion diagnosis scored for accuracy on a new labelled dataset; unclear whether the labels came from human annotators or an LLM.

**Решение:** =

---

### 80 · R0734

**Development and Benchmarking of a Blended Human-AI Qualitative Research Assistant**

2026 · Underline Science Inc. · audiovisual/conference talk, journalarticle, preprint/article · https://doi.org/10.48448/cc5e-9m39

Qualitative research emphasizes constructing meaning through iterative engagement with textual data. Traditionally this human-driven process requires navigating coder fatigue and interpretative drift, thus posing challenges when scaling analysis to larger, more complex datasets. Computational approaches to augment qualitative research have been met with skepticism, partly due to their inability to replicate the nuance, context-awareness, and sophistication of human analysis. Large language models, however, present new opportunities to automate aspects of qualitative analysis while upholding rigor and research quality in important ways. To assess their benefits and limitations - and build trust among qualitative researchers - these approaches must be rigorously benchmarked against human-generated datasets. In this work, we benchmark Muse, an interactive, AI-powered qualitative research system that allows researchers to identify themes and annotate datasets, finding an inter-rater reliability between Muse and humans of Cohen's $κ$ = 0.71 for well-specified codes. We also conduct robust error analysis to identify failure mode, guide future improvements, and demonstrate the capacity to correct for human bias. 32 pages, 9 figures

**ИИ:** ? · обе модели · неясен конструкт · An LLM-based qualitative coding tool was benchmarked against human coders (κ=0.71), but the abstract doesn't say whether the dataset covers psychological content.

**Решение:** =

---

### 81 · R0742

**Empathy in Diversity: Personalized Depression and Anxiety Therapy via Dialogue State Tracking and Patient-Aware Planning**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/18c1-3546

Large language model (LLM) dialogue agents are increasingly used in psychological therapy, yet robustness across diverse patients remains underexplored. We address this gap with three contributions: (1) MindEval, a realistic role-play protocol for evaluating therapeutic dialogue agents; (2) MindData, a de-identified, expert-annotated corpus of therapist–patient dialogues (2,573 sessions; 63,348 turns); and (3) MindApt, a framework that integrates a therapeutic dialogue state tracking paradigm with a patient-aware strategic planning module. On MindEval, MindApt outperforms strong baselines on therapeutic outcomes and dialogue quality while improving conversational efficiency. To evaluate utility beyond role-play, we conducted a clinical study with real patients, demonstrating that MindApt-guided care achieves outcomes comparable to therapist-determined care, while the hybrid setting combining therapist judgment with MindApt’s recommendations yields the strongest overall outcomes.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mostly about generating therapy dialogue, but LLM dialogue state tracking may have been checked against an expert-annotated therapy corpus.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM therapy dialogue agent framework with role-play evaluation and expert-annotated corpus; no LLM coding or rating of text against human labels reported.)

**Решение:** -

---

### 82 · R0747

**ExpressivityBench: Can LLMs Communicate Implicitly?**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/tnbn-ty11

Human communication is often implicit, conveying tone, identity, and intent beyond literal meanings. While large language models have achieved strong performance on explicit tasks such as summarization and reasoning, their capacity for expressivity, or implicit communication, remains underexplored. We introduce ExpressivityBench, a framework for evaluating the expressivity of LLMs using information-theoretic communication models. Our approach quantifies how well LLM-generated text communicates target properties without explicit mention, across nine tasks spanning emotion, identity, and tone. To enable scalable and reproducible evaluation, we employ LLM-based graders validated against human judgments. Our results reveal that while models are adept at expressing affective content, they struggle with sociolinguistic signals, lagging behind human baselines. This study provides a necessary step to evaluate human-like implicit communication, with implications for applications such as education, mental health support, and socially-aware dialogue systems. We provide code and data for our benchmark alongside our paper.

**ИИ:** ? · обе модели · неясен конструкт · LLM graders rating implicit emotion, identity and tone in text, checked against human judgments; unclear whether the psychological construct and agreement data are central.

**Решение:** =

---

### 83 · R0750

**From Detection to Explanation: Modeling Fine-Grained Emotional Social Influence Techniques with LLMs and Human Preferences**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/mpde-x225

This paper investigates the capabilities of LLMs to detect and explain fine-grained emotional social influence techniques in textual dialogues, as well as human preferences for technique explanations. We present findings from our two studies. In Study 1, a dataset of 238 Polish dialogues is introduced, each annotated with detailed span-level labels. On this data, we evaluate the performance of LLMs on two tasks: detecting 11 emotional social influence techniques and identifying text spans corresponding to specific techniques. The results indicate that current LLMs demonstrate limited effectiveness in accurately detecting fine-grained emotional social influence. In Study 2, we examine various LLM-generated explanations through human pairwise preferences and four criteria: comprehensibility, cognitive coherence, completeness, and soundness, with the latter two emerging as the most influential on general human preference. All data, including human annotations, are publicly available as the EmoSocInflu dataset (https://github.com/social-influence/emo-soc-influ). Our findings highlight a critical need for further advancement in the field. As LLM-supported manipulation grows, it is essential to promote public understanding of social influence mechanisms, enabling individuals to critically recognize and interpret the subtle forms of manipulation that shape public opinion.

**ИИ:** ? · обе модели · неясен конструкт · LLMs detect emotional social influence techniques in human-annotated Polish dialogues; it's unclear if manipulation techniques count as a psychological construct.

**Решение:** =

---

### 84 · R0761

**Language Shapes Mental Health Evaluations in Large Language Models**

2026 · Underline Science Inc. · audiovisual/conference talk, journalarticle, preprint/article · https://doi.org/10.48448/x8w8-dc30

Multilingual large language models (LLMs) are increasingly used to interpret mental health narratives in settings such as support chatbots, screening, and content moderation. A basic reliability question remains underexplored: when the same narrative is presented in different languages, does a model apply comparable evaluative standards? We study cross-linguistic variation in mental health evaluation between English and Chinese using two widely deployed LLMs (GPT-4o and Qwen3-32B). We separate (i) construct-level evaluative orientation from (ii) decision-level behavior on downstream tasks. At the construct level, we adapt validated psychometric stigma instruments spanning social, self, and health-professional stigma and quantify language-conditioned shifts in model responses. At the decision level, we evaluate models on binary stigma detection and four-way depression severity classification using semantically aligned English--Chinese datasets. Across instruments and models, Chinese prompts elicit systematically higher stigma scores than English prompts. These differences propagate to downstream decisions: Chinese prompts reduce sensitivity in stigma detection and induce a downward shift in predicted depression severity, producing substantially more under-estimation errors. Our findings show that prompt language can shift both evaluative orientation and effective decision thresholds, underscoring the need for multilingual evaluation and calibration before deploying LLMs in socially sensitive domains.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · GPT-4o and Qwen classify stigma and depression severity in narratives; the datasets' labels are likely, but not confirmed, human-annotated.

**Решение:** =

---

### 85 · R0767

**Measuring the quality of therapy sessions against assessment scales using augmented semantic-similarity approaches**

2026 · Underline Science Inc. · audiovisual/conference talk, conference-paper, other · https://doi.org/10.48448/p3sx-bh86

Therapist fidelity and competence rating scales provide a way to measure quality assurance and therapist training outcomes. Scores on these scales reflect the extent to which a therapist adheres to specific therapeutic principles during a psychotherapy session. Existing research has employed natural language processing (NLP) techniques to automatically predict scale ratings. However, existing approaches require a model trained on a dataset of therapy sessions annotated with the target rating scale. Recent work has explored directly inferring therapeutic alliance by computing semantic similarity between therapy transcripts and the Working Alliance Inventory, via cosine similarity between sentence embeddings. In this paper, we extend this line of work by computing semantic similarity between therapist talk turns and therapist fidelity scale items to directly infer fidelity to specific therapeutic modalities. We further enhance this method by augmentation with LLM-generated example therapist utterances that instantiate target behaviours (as expressed by scale items) across varied therapeutic contexts. In evaluations on two independent datasets, our example-augmented semantic similarity approach consistently shows effectiveness in discriminating therapeutic modalities and levels of therapist fidelity.

**ИИ:** разошлись — Opus ? (другое: Fidelity is scored by embedding similarity; the LLM only writes augmentation examples. The human fidelity ratings used as the reference likely exist.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Fidelity is inferred by sentence-embedding similarity; the LLM only generates example utterances and does not code or rate the sessions.)

**Решение:** -

---

### 86 · R0776

**PersonaForge: Psychology-Grounded Dual-Process Architecture for Personality-Consistent Role-Playing Agents**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/j7wn-xj08

Large Language Models excel at role-playing but struggle to maintain consistent personalities across extended multi-turn interactions. We propose PersonaForge, combining (1) a three-layer personality architecture grounded in psychological theory and (2) a dual-process generation mechanism inspired by cognitive science. We test two falsifiable claims: Claim 1 (Orthogonality): Psychology-grounded dimensions (Big Five + Defense Mechanisms) provide more orthogonal constraints than natural language descriptions, reducing long-dialogue drift. Claim 2 (Integration Necessity): High-dimensional personality constraints create "production interference" requiring a cognitive workspace (Inner Monologue) to resolve—removing it degrades performance below simpler baselines. Experiments on 88 characters demonstrate: (1) +19.4% personality consistency (PC) with human correlation r=0.82, (2) reduced drift over 50-turn conversations (6.3% vs. 24.8% baseline), and (3) +64.7% defense mechanism manifestation. External validation on RoleBench confirms generalization (73.2% win-rate, drift 8.4% vs. 20.4%). Selective dual-process activation achieves 96% of full-system performance with only 13.4% token overhead. Human evaluation confirms more authentic and psychologically coherent character behaviors. Code and data: https://github.com/fQwQf/PersonaForge.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: Mainly a generation study, but its personality-consistency metric (likely an LLM judge) is reported to correlate with human ratings (r=0.82).); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: Role-playing agent architecture for personality-consistent generation; the personality-consistency metric correlates with human ratings, but this is not an LLM coding of psychological text against human labels.)

**Решение:** -

---

### 87 · R0777

**PhaseMI: A Motivational Interviewing Dataset for Enhancing Phase Progression in LLM-based Counseling**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/qjv6-9310

The growing demand for scalable mental health support has increased interest in AI-based counseling systems grounded in Motivational Interviewing (MI). However, existing MI datasets do not explicitly model the structured progression of MI phases, which is essential for effective and goal-oriented counseling. To address this gap, we introduce PhaseMI, a phase-structured MI dataset, together with a data generation framework that employs therapist, client, and supervisor LLMs to explicitly control phase transitions. Compared to the best alternative baseline, PhaseMI achieves improved coverage of MI phases, with gains of 12.3% in exploring, 37.6% in guiding, and 61.1% in choosing, and experimental evaluations demonstrate that it yields higher overall counseling quality than baseline datasets.

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM-generated MI counseling dataset; abstract mentions no LLM coding or rating checked against human coders.); Sonnet ? (неясно, сравнивали ли с людьми: Mainly a dataset generation paper with LLM therapist/client/supervisor; evaluation of phase coverage and quality may involve LLM or human rating, which is unclear from the abstract.)

**Решение:** -

---

### 88 · R0791

**SLANG-GraphRAG: Multi-Layered Retrieval with Domain-Specific Knowledge for Low Resource Social Media Conversations**

2026 · Underline Science Inc. · audiovisual/conference talk, conference-paper, other · en · https://doi.org/10.48448/yv4p-4910

Emotion classification on social media is especially difficult when texts include informal, culturally grounded language like slang. Standard NLP benchmarks often miss these nuances, particularly in low-resource settings. We present SLANG-GraphRAG, a retrieval-augmented framework that integrates a culture-specific slang knowledge graph into large language models via one-shot prompting. Using multiple retrieval strategies, we incorporate slang definitions, regional usage, and conversational context. Our results show that incorporating structured cultural knowledge into the retrieval process leads to significant improvements, improving accuracy by up to 31% and F1 score by 28%, outperforming traditional and unstructured retrieval methods. To better evaluate model behavior, we propose a probabilistic metric that reflects the distribution of human annotations, providing a more nuanced measure of performance. This highlights the value of culturally sensitive applications and more balanced evaluation in subjective NLP tasks.

**ИИ:** + · обе модели · бенчмарк с метками людей · LLMs classify emotions in slang-heavy social media conversations, evaluated against the distribution of human annotations.

**Решение:** =

---

### 89 · R0794

**Sycophancy Negatively Affects LLM-as-a-Judge in Conflict Evaluation**

2026 · Underline Science Inc. · audiovisual/conference talk, conference-paper, other · https://doi.org/10.48448/998s-gr02

LLM-as-Judge systems are increasingly used to generate labels and evaluate conversational data, yet their susceptibility to narrative framing remains underexplored. We study whether replacing one speaker’s username with the first-person identifier 'Me' systematically biases model judgments independent of the underlying evidence. Using the Conversations Gone Awry corpus, we evaluate four LLMs across three judgment tasks (attack detection, attacker identification, and blame attribution), three perspective conditions, and two evidence visibility settings. Our results show that narrative perspective induces strong, task-dependent distortions, particularly in more subjective judgment tasks. We find that models systematically favor the narrator when a speaker is presented as 'Me', reducing blame and responsibility attribution toward that speaker even when the underlying evidence is unchanged. These findings raise concerns about using LLMs to judge or moderate first-person conversational data.

**ИИ:** ? · обе модели · неясен конструкт · LLMs judge attacks and blame in Conversations Gone Awry, which has human labels; unclear if interpersonal conflict counts as a psychological construct versus toxicity.

**Решение:** =

---

### 90 · R0798

**The Attachment Index: Auditing Attachment Language Cues and Relational Safety Risks in Human-LLM Dialogue**

2026 · Underline Science Inc. · audiovisual/conference talk, conference-paper, other · https://doi.org/10.48448/5xdz-1719

As conversational AI systems grow increasingly toward emotional support contexts, relational safety failures between users and chatbot remain under-measured. We present a psycholinguistic grounded framework for auditing attachment-relevant language cues. Our approach identifies when an LLM's replies exhibit linguistic attachment cues and surface related patterns that may signal parasocial bonding, including anthropomorphism or over‑dependence. We adapt the Adult Attachment Interview into two complementary, automatable lenses - attachment cues features and Gricean maxims - and combine them with psychologist‑led annotation of multi‑turn persona dialogues. Applying this framework, we observe that models can align with persona-intended attachment cue patterns. We also find that judge‑LLMs alone are unreliable, highlighting the need for psychologist‑in‑the‑loop evaluation. The 25 psychologist‑led annotated conversations revealed risks, including boundary blurring and missed opportunities for appropriate referral or triage. These insights motivate attachment‑aware safeguards - such as non‑personification, boundary language, and explicit referral mechanisms - to reduce mis‑attunement and over‑attachment in LLM conversational settings.

**ИИ:** + · обе модели · LLM-судья · Judge-LLMs rated attachment cues and relational risks in dialogues and were compared with psychologist annotations, which they found unreliable.

**Решение:** =

---

### 91 · R0802

**Training-Free Text Emotion Tagging via LLM-Based Best-Worst Scaling**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/87ds-7h23

Large Language Models (LLMs) have been frequently used as automatic annotators for tasks such as Text Emotion Recognition (TER). We consider a scenario in which annotators assign at least one emotion label from a large set of options to a text snippet. For this emotion tagging task, we propose a novel zero-shot algorithm that leverages Best-Worst Scaling (BWS), prompting the LLM to choose the least and most suitable emotions for a given text from several label subsets. The LLM's choices can be represented by a graph linking labels via worse-than relations. Random walks on this graph yield the final score for each label. We compare our algorithm with naive prompting approaches as well as an established BWS-based method. Extensive experiments demonstrate the suitability of the method. It proves to compare favorably to the benchmarks in terms of both accuracy and calibration with respect to human annotations. Moreover, our algorithm's automatic annotations are shown to be suitable for finetuning lightweight emotion classification models. The proposed method consumes considerably fewer computational resources than the established BWS approach.

**ИИ:** + · обе модели · бенчмарк с метками людей · Zero-shot LLM tags emotions in text snippets; accuracy and calibration evaluated against human emotion annotations.

**Решение:** =

---

### 92 · R0807

**When Can We Trust LLMs in Mental Health? Large-Scale Benchmarks for Reliable LLM Evaluation**

2026 · Underline Science Inc. · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48448/zcyb-bm51

Evaluating Large Language Models (LLMs) for mental health support poses unique challenges to reliable evaluation due to the emotionally and cognitively complex nature of therapeutic dialogue. Existing benchmarks are limited in scale, authenticity, and reliability, often relying on synthetic or social media data, and lack frameworks to assess when automated judges can be trusted. To address the need for large-scale authentic dialogue datasets and judge-reliability assessment, we introduce two benchmarks that provide a framework for generation and evaluation in this domain. MentalBench-100k consolidates 10,000 authentic single-session therapeutic conversations from three real-world scenarios datasets, each paired with nine LLM-generated responses, yielding 100,000 response pairs. MentalAlign-70k reframes evaluation by comparing four high-performing LLM judges with human experts across 70,000 ratings on seven attributes, grouped into Cognitive Support Score (CSS) and Affective Resonance Score (ARS). We then employ the AffectiveвЂ“Cognitive Agreement Framework, a statistical methodology using intraclass correlation coefficients (ICC) with confidence intervals to quantify agreement, consistency, and bias between LLM judges and human experts. Our analysis reveals systematic inflation by LLM judges, strong reliability for cognitive attributes such as guidance and informativeness, reduced precision for empathy, and some unreliability in safety and relevance. Our contributions establish new methodological and empirical foundations for the reliable and large-scale evaluation of LLMs in mental health contexts.

**ИИ:** + · обе модели · LLM-судья · LLM judges rate mental-health responses on empathy, safety and other attributes; agreement with human experts is measured with ICC.

**Решение:** =

---

### 93 · R0809

**Who Generates More Empathetic Responses—Humans or LLMs? A Comparative Evaluation with Human and LLM Judges**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/b6by-xv06

This paper compares the empathetic quality of responses generated by humans and large language models (LLMs). We evaluate four LLMs that were widely used at the time of study—GPT-4, LLaMA-2-70B-Chat, Gemini-1.0-Pro, and Mixtral-8×7B-Instruct—against a human baseline using a large-scale between-subjects study. A total of 1,000 human participants evaluated the empathetic quality of human- and LLM-generated responses to 2,000 dialogue prompts spanning 32 positive and negative emotions. To complement human judgments, we also employed an LLM-as-judge (GPT-4o-mini) to assess the same responses. Across emotions and evaluators, LLM-generated responses were rated as significantly more empathetic than human-written responses. We also observed that both human judges and the LLM-as-judge tended to rate responses generated by their own group more favorably, indicating self-favoring tendencies. These findings highlight both the strong performance of contemporary LLMs in empathetic responding and the need to interpret human- and LLM-based evaluations with care.

**ИИ:** разошлись — Opus + (LLM-судья: GPT-4o-mini as judge rated the empathy of the same responses that human participants rated, so LLM–human agreement can be compared.); Sonnet ? (неясно, сравнивали ли с людьми: GPT-4o-mini and humans rate empathy of the same responses, but the abstract reports only rating differences and self-favoring bias, not LLM–human agreement.)

**Решение:** ?

---

### 94 · R0810

**You Never Know a Person, You Only Know Their Defenses: Detecting Levels of Psychological Defense Mechanisms in Supportive Conversations**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/km8x-7v71

Psychological defenses are strategies, often automatic, that people use to manage distress. Rigid use or overuse of defenses is negatively linked to mental health and shapes what speakers disclose and how they accept or resist help. However, defenses are complex and difficult to reliably measure, particularly in clinical dialogues. We introduce PsyDefConv, a dialogue corpus with help seeker utterances labeled for defense level, and DMRS Co-Pilot, a four-stage pipeline that provides evidence-based pre-annotations. The corpus contains 200 dialogues and 4,709 utterances, including 2,336 help seeker turns, with double-blind labeling reaching Cohen’s kappa of 0.639. In a counterbalanced study, the co-pilot reduced average annotation time by 24.0%. In expert review, it averaged 4.62 for evidence supportiveness, 4.44 for clinical plausibility, and 4.40 for insight on a seven-point scale. Benchmarks with strong large language models (LLMs) in zero-shot and fine-tuning settings demonstrate clear headroom, with the best macro F1-score around 30% and a tendency to overpredict mature defenses. Corpus analyses confirm that mature defenses are most common and reveal emotion-specific deviations. We release the corpus, annotations, code, and prompts to support research on defensive functioning in language.

**ИИ:** + · обе модели · бенчмарк с метками людей · Benchmark corpus with human-labeled defense levels in support dialogues; LLMs evaluated zero-shot and fine-tuned against those labels (macro F1).

**Решение:** =

---

### 95 · R0812

**Emotionally Aligned? Evaluating LLM Predictions in Affective Tasks**

2026 · Jyväskylä University Digital Archive (University of Jyväskylä) · conference-paper · en · https://ceur-ws.org/Vol-4181/paper05.pdf

Large Language Models (LLMs) are increasingly deployed in tasks that require sensitivity to human emotions, yet the scientific understanding of how these models process affective content remains limited. This gap poses challenges for developing emotionally aligned and trustworthy AI systems. In this paper, we propose a formal framework for evaluating emotional understanding in LLMs by combining controlled vignettes, human-annotated emotion ratings, and regression-based alignment analysis. Our approach allows for systematic testing of both emotion intensity and categorical recognition across diverse emotional contexts. Results show that while LLMs can predict high-level emotional patterns, they struggle with tasks involving subtle, aversive, or ambiguous emotions—areas where humans rely on deeper contextual and cognitive cues. We argue that augmenting LLMs with cognitive modeling, grounded in psychological theories of emotion, offers a promising path toward more nuanced and robust affective capabilities. This work contributes foundational tools for testing, interpreting, and improving emotional understanding in language-based AI systems.

**ИИ:** + · обе модели · бенчмарк с метками людей · LLMs rate emotion intensity and categories in text vignettes; compared with human emotion ratings using regression-based alignment.

**Решение:** =

---

### 96 · R0852

**Do Humans and LLMs Agree? Evaluating Clinical Note Quality in Mental Health Care**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7096678

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; the title suggests LLM-human agreement on rating mental health clinical notes, but it is unclear whether note quality counts as a psychological construct.

**Решение:** =

---

### 97 · R0890

**Multi-label Detection of Depression, Anxiety, and Bipolar Symptoms in Indonesian Social Media Texts using IndoBERT**

2026 · 2026 5th International Conference on Electronics Representation and Algorithm (ICERA) · conference · https://doi.org/10.1109/icera72709.2026.11666682

Mental-health conditions, specifically depression, anxiety, and bipolar disorder, are becoming increasingly serious health concerns across Indonesia. Despite high prevalence, these conditions remain under-diagnosed; fewer than 3% of affected adolescents reach professional services. Although natural language processing of social-media text offers a scalable route for early screening, prior Indonesian-language studies have been confined to single-label or binary formulations addressing at most two diagnostic labels, a simplification that cannot capture the comorbidity defining actual clinical presentations. To address this gap, a multi-label classifier capable of detecting three concurrent symptom categories is proposed. The approach utilizes the IndoBERT-Large encoder (335M parameters, 24 layers), fine-tuned on 13,014 posts drawn from X (Twitter) and five Indonesian Facebook mental-health communities after an LLM-based relevance filter. Labels are produced by GPT-4o under a DSM-5-derived guideline, and a licensed clinical psychologist independently re-annotated a stratified sample of 375 posts, yielding a macro Cohen's Kappa of 0.56 across the three disorder labels and 0.52 when the complementary Normal category is included. Training employs layer-wise learning-rate decay together with an Asymmetric Loss objective, while per-class decision thresholds are tuned on the validation split. On the held-out test set (n = 2,604) the model attains a macro F1 of 0.7982, a Hamming loss of 0.1169, and a subset accuracy of 67.74%, exceeding the macro F1 of the most recent Indonesian baseline (0.7516) while extending the task from two labels to three. Bipolar disorder reaches an F1 of 0.84 despite being the rarest class, establishing a first benchmark for this condition in Indonesian social-media text. Multi-seed evaluation across seeds 42, 123, and 456 yields a validation macro F1 of 0.8004 with a standard deviation of 0.0018. SHAP token attribution and a confusion-matrix study are reported as complementary evidence. The reported metrics quantify agreement with a guideline-based annotator rather than clinical ground truth; the system is a research prototype and has not been clinically validated.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · GPT-4o labeled symptom categories in social-media posts; a clinical psychologist re-annotated 375 posts (kappa 0.56).

**Решение:** =

---

### 98 · R0893

**Evaluating Large Language Models for Transparent Quality-of-Care Measurement in Children with ADHD.**

2026 · medRxiv : the preprint server for health sciences · journal article, preprint, journalarticle · eng · https://doi.org/10.64898/2026.04.12.26350732

Importance: Guideline-concordant care for young children with attention-deficit/hyperactivity disorder (ADHD) includes recommending parent training in behavior management (PTBM) as first-line treatment. However, assessing guideline adherence through manual chart review is time-consuming and costly, limiting scalable and timely quality-of-care measurement. Objective: To evaluate the accuracy and explainability of large language models (LLMs) in identifying PTBM recommendations in pediatric electronic health record (EHR) notes as a scalable alternative to manual chart review. Design, Setting, and Participants: This retrospective cohort study was conducted in a community-based pediatric healthcare network in California consisting of 27 primary care clinics. The study cohort included children aged 4-6 years with ≥ 2 primary care visits between 2020-2024 and ICD-10 diagnoses of ADHD or ADHD symptoms (n=542 patients). Clinical notes from the first ADHD-related visit were included. A stratified subset of 122 notes, including all cases with model disagreement, was manually annotated to assess model performance in identifying PTBM recommendations and rank model explanations. Exposures: Assessment and plan sections of clinical notes were analyzed using three generative large language models (Claude-3.5, GPT-4o, and LLaMA-3.3-70B) to identify the presence of PTBM recommendations and generate explanatory rationales and documentation evidence. Main Outcomes and Measures: Model performance in identifying PTBM recommendations (measured by sensitivity, positive predictive value (PPV), and F1-score) and qualitative explainability ratings of model-generated rationales (based on the QUEST framework). Results: All three models demonstrated high performance compared to expert chart review. Claude-3.5 showed balanced performance (sensitivity=0.89, PPV=0.95, and F1-score=0.92) and ranked highest in explainability. LLaMA3.3-70B achieved sensitivity=0.91, PPV=0.89, and F1-score=0.90, ranking second for explainability. GPT-4o had the highest PPV [0.97] but lowest sensitivity [0.82], with an F1-score of 0.89 and the lowest explainability ranking. Based on classifications from the best-performing model, Claude-3.5, 26.4% (143/542) of patients had documented PTBM recommendations at their first ADHD-related visit. Conclusions and Relevance: LLMs can accurately extract guideline-concordant clinician recommendations for non-pharmacological ADHD treatment from unstructured clinical notes while providing clear explanations and supporting evidence. Evaluating model explainability as part of LLM implementation for medical chart review tasks can promote transparent and scalable solutions for quality-of-care measurement.

**ИИ:** ? · обе модели · неясен конструкт · LLMs flag behavioral-treatment recommendations in ADHD clinical notes against expert chart review; unclear whether a quality-of-care extraction counts as a psychological construct.

**Решение:** =

---

### 99 · R0895

**A Multi-Model Ensemble for Robust and Consistent Scoring of Reflective Essays**

2026 · IEEE Access · journalarticle, article · en · https://doi.org/10.1109/access.2026.3704920

Automated essay scoring has the potential to improve assessment efficiency, yet its adoption in medical education remains limited due to concerns regarding scoring reliability, robustness to linguistic variation, and the interpretability of automated feedback. This challenge is particularly evident in reflective writing assessment, where transparency and pedagogical relevance are essential. This study introduces LLAMPT (Linguistically-Aware Majority Prediction Transformer), an ensemble framework that combines multiple instruction-tuned large language models to generate assessment scores and explanatory rationales. The framework is trained and evaluated on a domain-specific dataset of 13,125 reflective essays written by medical students in South Africa, addressing an underrepresented context in AES research. Experimental results demonstrate strong agreement with expert human markers (Quadratic Weighted Kappa = 0.963). Robustness analysis using progressively paraphrased essays showed sustained scoring consistency across all transformation levels (QWK > 0.94), with mean score deviations below 0.125 rubric points and practical equivalence confirmed through TOST analysis. Interpretability was examined through attribution-based analyses and a mixed-methods evaluation involving clinical educators. While educators generally viewed generated justifications as coherent and contextually relevant, qualitative feedback highlighted limitations related to explanation faithfulness, stylistic nuance, and the continued need for human oversight. These findings demonstrate the potential of large language model ensembles for reflective writing assessment while highlighting important considerations for their responsible integration into medical education workflows.

**ИИ:** ? · обе модели · неясен конструкт · An LLM ensemble scores medical students' reflective essays against expert markers (QWK). It is unclear whether the rubric measures reflection as a psychological construct or educational writing quality.

**Решение:** =

---

### 100 · R0896

**Are LLMs Reliable Coders of Communication Content in Economic Experiments?**

2026 · Elsevier BV · posted-content, preprint · en · https://doi.org/10.2139/ssrn.7129638

Analysis of free-form communication from experiments has largely relied on manual coding by research assistants (RAs), a costly and time-consuming process. We outline an easily implemented method for coding communication data using large language models (LLMs) and propose a novel standard for evaluating the performance of LLM-based coding ("reliability"). Using data from three published articles, we find that LLM-based coding meets our two reliability conditions: (1) differences between LLM-based and RA-based coding are no larger than differences between the RA-based and original coding and (2) the LLM-based coding largely replicates qualitative conclusions from the original papers. That said, there are cases where the LLM-based coding agrees poorly with the RA-based coding or fails to replicate statistical results from the original papers. We demonstrate that these problems can be ameliorated with better prompt design. We conclude that use of LLMs can reduce research costs and time without sacrificing reliability, making content analysis a more accessible tool for experimental economists. However, only with a combination of test coding by RAs and prompt design by researchers can we avoid significant problems with LLM-based coding, highlighting the continued importance of human input.

**ИИ:** ? · обе модели · неясен конструкт · LLM coding of chat messages from experiments, compared with research-assistant coding; the codes may capture interpersonal or behavioural constructs (promises, cooperation), but this is unclear.

**Решение:** =

---

### 101 · R0897

**Are LLMs Reliable Coders of Communication Content in Economic Experiments? Working Paper #0115**

2026 · Elsevier BV · posted-content, preprint · https://doi.org/10.2139/ssrn.7040658

Analysis of free-form communication from experiments has largely relied on manual coding by research assistants (RAs), a costly and time-consuming process. We outline an easily implemented method for coding communication data using large language models (LLMs) and propose a novel standard for evaluating the performance of LLM-based coding ("reliability"). Using data from three published articles, we find that LLM-based coding meets our two reliability conditions: (1) differences between LLM-based and RA-based coding are no larger than differences between the RA-based and original coding and (2) the LLM-based coding largely replicates qualitative conclusions from the original papers. That said, there are cases where the LLM-based coding agrees poorly with the RA-based coding or fails to replicate statistical results from the original papers. We demonstrate that these problems can be ameliorated with better prompt design. We conclude that use of LLMs can reduce research costs and time without sacrificing reliability, making content analysis a more accessible tool for experimental economists. However, only with a combination of test coding by RAs and prompt design by researchers can we avoid significant problems with LLM-based coding, highlighting the continued importance of human input.

**ИИ:** ? · обе модели · неясен конструкт · Compares LLM and research-assistant coding of experimental chat messages; unclear whether the codes are psychological or interpersonal constructs (e.g., promises, intentions).

**Решение:** =

---

### 102 · R0903

**An Agentic AI Framework for Automated Multimodal Dataset Curation for Depression Detection**

2026 · MBZUAI · dissertation/thesis, dissertation · en · https://doi.org/10.82419/350

Depression detection research relies on multimodal datasets from YouTube vlogs where individuals discuss their mental health experiences. However, existing datasets remain small because researchers must manually watch and label each video, creating a bottleneck that prevents the development of robust and scalable automated detection systems. This thesis addresses this limitation by developing an automated multi-agent framework for curating and collecting depression-related multimodal vlog datasets from YouTube without requiring manual annotation, representing the first agentic framework for multimodal dataset construction. The framework consists of five specialized agents. The Content Discovery Agent searches YouTube for relevant videos using keywords generated by language models. The Relevance Filtering Agent applies three filtering stages: rule-based filtering for format and language requirements; computer vision-based vlog identification via face detection and clustering; and automated depression classification using language models. The Feature Extraction Agent processes approved videos to extract time-aligned visual, audio, and textual features. The Model Training Agent validates dataset quality by training depression detection models. The Supervision Agent monitors the entire pipeline and automatically recovers from errors during long-running collection tasks. The system has been evaluated on multiple language models with different system configurations: GPT-5.2 and DeepSeek-V3.2 processing text-based inputs, and Qwen3-VL processing both visual and textual information. Manual validation demonstrated labeling retrieval accuracies of 83.3\%, 92.0\%, and 95.5\%, respectively, with the vision-language model achieving the highest performance. The vlog identification mechanism successfully distinguished personal vlogs from interviews and multi-speaker content. Dataset quality validation through comparative model training demonstrated that models trained on an augmented dataset achieved consistent improvements over the manually labeled baseline: +2.54 percentage points in accuracy, +5.83 \% in precision, +6.11 \% in recall, and +5.96 \% in F1-score, confirming that automated labeling produces annotation quality sufficient for depression detection research. This work eliminates the manual annotation requirement that limits existing approaches and represents the first fully automated system to construct multimodal depression datasets from social media. The framework supports iterative dataset expansion where previously collected videos seed subsequent discovery cycles, enabling continuous dataset growth while maintaining quality. This methodology establishes a foundation for large-scale depression-detection research using datasets substantially larger and more diverse than previously possible.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · GPT-5.2, DeepSeek and Qwen3-VL labelled vlog transcripts for depression; manual validation reported labelling accuracies of 83–95%.

**Решение:** =

---

### 103 · R0912

**Evaluating NVivo, R, and Large Language Models for Thematic Analysis: Comparative Computational Insights for Qualitative Researchers**

2026 · International Conference on Advanced Research in Computing (ICARC) · conference, conference-paper · https://doi.org/10.1109/icarc68737.2026.11453942

The growing integration of computational and AI-driven tools in qualitative research necessitates rigorous evaluation of their analytical reliability relative to traditional human coding. This study applies to a structured comparative analytical framework to evaluate NVivo, an R-based text analysis workflow, and a Large Language Model (GPT) for thematic analysis. Human-generated themes served as the benchmark, against which Precision, Recall, F1-score, and Jaccard similarity were computed to assess thematic accuracy and overlap. The findings indicate that the LLM achieved the highest alignment with human coders, demonstrating strong semantic sensitivity and consistent thematic coverage. NVivo produced methodologically stable and auditable results, reaffirming its suitability for structured, researcher-led analysis. The R-based approach exhibited lower accuracy and greater sensitivity to parameter selection, although performance improved substantially with manual tuning. Overall, the results suggest that integrating LLM-assisted interpretation with human oversight can enhance the efficiency, scalability, and analytical depth of qualitative research, supporting a balanced and transparent methodological direction for future studies.

**ИИ:** ? · обе модели · неясен конструкт · GPT thematic analysis compared with human themes; may be theme-level only, and whether the data are psychological is unclear.

**Решение:** =

---

### 104 · R0922

**Mapping the Content and Consistency of Suicidal Thoughts with Large Language Models: A Two-Study Longitudinal Investigation Among Adolescents and Young Adults**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/8jx4u_v3

Suicide is a leading cause of death. Measurement of suicidal thoughts and behaviors (STBs) relies on self-report (e.g., “How strong is your urge to kill yourself right now?”), yet little is known about how individuals translate internal experiences into numerical ratings. We used large language models (LLMs) to examine the content and consistency of suicide urges across severity ratings, between people, and over time. Participants with past-year STBs (Study 1: N=158 adolescents, Study 2: N=202 young adults) completed open-ended questions at baseline and follow-ups. We developed a two-stage topic-modeling pipeline and identified 13 (Study 1) and 14 (Study 2) topics reflecting suicidal thought content (e.g., Family/Friends Reactions, Depressed &amp; Exhausted). Within- and between-person consistency were U-shaped, with highest agreement at endpoints of the scale. These findings highlight the potential of LLMs for advancing measurement of suicide risk and our understanding of how people interpret and respond to self-report rating scales.

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: LLM topic-modeling pipeline codes open-ended suicidal-thought responses; the abstract doesn't say whether LLM topic assignments were validated against human coders.); Sonnet -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLM topic modeling of suicidal thought content and consistency across ratings; no LLM coding compared with human coders of the same texts.)

**Решение:** -

---

### 105 · R0950

**Human vs AI clinical assessment: benchmarking a multimodal foundation model against multi-center expert judgment on the mental status examination**

2026 · npj Mental Health Research · article · en · https://doi.org/10.1038/s44184-026-00245-y

Abstract The Mental Status Examination (MSE) is the cornerstone of the psychiatric evaluation, yet validating artificial intelligence (AI) against the inherent variance of clinical judgment remains a critical bottleneck. Here we introduce a multi-center framework to benchmark the open-weight multimodal foundation model Qwen3-Omni against independent expert panels at two sites, UTHealth and Yale. Evaluating 396 classifications across 10 MSE domains and three longitudinal timepoints of increasing symptom severity, we found that experts achieved substantial agreement (Gwet’s AC1 = 0.87), whereas the model achieved only moderate alignment (AC1 = 0.70-0.72). Even as the model’s overall pathology prediction rate approximated the experts’, the aggregate equilibrium masked a profound “clinical reasoning gap”. Specifically, the model systematically over-predicted observable signs (e.g., speech, affect) while notably failing in inferential domains requiring the interpretation of latent mental content (e.g., delusions, perceptions). A 4-bit quantization analysis of the model confirmed this mechanistically: reducing model capacity disproportionately degraded inferential reasoning while preserving perceptual feature extraction. Furthermore, model-to-expert agreement degraded linearly as clinical complexity intensified across longitudinal visits (Accuracy: T0 = 84.8-87%; T1 = 80-82%; T2 = 71-73%), whereas expert consensus remained robust. Notably, model errors increased 2.3-to-3.4 fold where human experts disagreed. These findings establish inter-expert variance as an essential measurable baseline for psychiatric AI, demonstrating that true clinical translation requires models to move beyond multimodal perceptual extraction to achieve higher-order diagnostic reasoning.

**ИИ:** разошлись — Opus + (клиническая оценка: Multimodal LLM Qwen3-Omni rated 10 mental status examination domains from patient interviews; agreement with expert panels reported. Check full text: input may be audio/video, not text.); Sonnet ? (другое: Qwen3-Omni rated MSE domains versus expert panels with agreement (AC1), but input is multimodal (audio/video), so it's unclear whether it counts as text.)

**Решение:** +

---

### 106 · R0955

**LLMs for Survey Text Analysis – A Performance Comparison Between Humans and GPT-5 on Inductive Content Analysis**

2026 · Research Square · preprint/article, preprint, ppr · https://doi.org/10.21203/rs.3.rs-10536645/v1

Abstract Large language models (LLMs) are increasingly used to support text analysis in qualitative research, yet evidence on their performance in inductive content analysis remains limited. This study compares human and LLM-based inductive coding of open-ended survey responses from 903 answers across six variables from a European PhD student survey. Five human coders performed inductive content analysis following a standardized coding scheme, while an LLM (GPT-5.4) conducted the same task using an established prompting procedure. Agreement between human and LLM outputs was assessed using the Adjusted Rand Index (ARI). Results showed an alignment between humans and the LLM, with ARI values of 0.61 for coding and 0.54 for theme generation. These values were close to the internal consistency of coding and theme results within humans (ARI = 0.68) and the LLM (ARI = 0.76). Agreement varied widely across variables, with low within-entity consistency consistently linked to low between-entity agreement, underscoring the role of data characteristics and individual performance in reliability. Overall, the findings suggest that LLMs can approximate human coding in this case-specific setting, particularly at the coding level, and may serve as a scalable support tool for inductive qualitative analysis.

**ИИ:** ? · обе модели · неясен конструкт · GPT-5 and human coders inductively coded the same PhD survey responses (ARI reported), but it's unclear whether the content is psychological.

**Решение:** =

---

### 107 · R0956

**Mapping Psychology Students’ Conversations with a Large Language Model (LLM)-Powered Statistics Chatbot**

2026 · PsyArXiv · preprint, ppr, posted-content · https://doi.org/10.31234/osf.io/bvfy7_v1

Large language models (LLMs) are becoming increasingly integrated into higher education, yet little is known about how students interact with these tools during authentic coursework. We investigated psychology students’ real-world use of StatsBot, a statistics chatbot powered by OpenAI’s GPT-4o and deployed as part of an educational initiative at the Faculty of Psychology, University of Vienna. We analyzed 1,400 chat messages from 182 users collected between March 15 and June 30, 2025, using a three-step mixed-methods approach: (1) deductive content analysis, (2) inductive content analysis to explore selected categories in greater depth, and (3) descriptive, temporal, and network analyses. LLM-assisted coding (GPT-5) demonstrated high agreement with human consensus on a 300-message benchmark (average Matthews correlation coefficient = .79) and was subsequently used to scale the deductive and inductive coding procedures. Most interactions focused on statistics (93.3%), and nearly half referenced specific statistical methods (49.4%). Clear differences emerged between study programs. Master's students more frequently sought support for data analysis software (14.3% vs. 4.3% among bachelor's students) and advanced statistical methods (e.g., mediation/moderation, multilevel models), produced longer, instruction-oriented prompts, and tended to communicate in English. In contrast, bachelor's students more often asked multiple-choice questions (15.1% vs. 0.3%), wrote shorter, question-based prompts, and primarily used German. The inductive analysis further identified recurring usage patterns and synthesized common use cases, including interactions involving non-statistical topics and requests related to specific statistical methods. Overall, this study provides empirical evidence of how students engage with LLM-powered educational support in an authentic university setting, offering detailed insights into both the statistical assistance students seek and the ways they communicate with AI. All data and analysis code are openly shared with the scientific community.

**ИИ:** разошлись — Opus -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: GPT-5 coding was validated against humans, but the codes cover statistics topics and prompt types in student chatbot messages, not a psychological construct.); Sonnet ? (неясен конструкт: GPT-5 coding of student chatbot messages was validated against human consensus (MCC = .79), but the categories are statistics-topic and usage codes, so a psychological construct is doubtful.)

**Решение:** -

---

### 108 · R0969

**Becoming IT professionals: a conceptual framework of community-mediated self-directed IT learning on Reddit**

2026 · Information and Learning Sciences · journalarticle, article · en · https://doi.org/10.1108/ils-12-2025-0242

Purpose This study aims to examine how participants in information technology (IT)-focused Reddit communities describe developing competencies outside formal coursework and how community participation supports self-directed learning in informal IT learning. Design/methodology/approach This study analyzed 464 Reddit threads containing 59,471 comments across ten IT-related subreddits. Data were segmented into 15,658 units and analyzed using a hybrid qualitative pipeline combining manual coding with GPT-5-mini-assisted classification. Guided by a synthesized theoretical framework, this study used a three-phase design and produced 382 evidence segments for reporting. Findings Participation in these communities supported motivation, persistence and learning through social support and growth-oriented norms. Learners reported developing technical knowledge, hands-on skills through projects and home labs and attitudes such as resilience, curiosity and self-efficacy alongside an emerging professional identity. Many described nonlinear learning and career trajectories from entry-level roles (e.g. help desk) toward specialized fields such as cybersecurity, networking and cloud. Community interactions scaffolded self-regulated (SRL) strategies including goal setting, project-based practice, reflective journaling, adaptive help-seeking and the use of AI tools for explanation, self-testing and feedback. Research limitations/implications This study contributes a conceptual framework of community-mediated informal IT learning and extends social views of SRL to online community contexts. The analysis is limited to Reddit discourse and participants’ reported experiences and does not measure actual competencies or support causal claims. Practical implications Educators, workforce development programs and platform designers can use these findings to strengthen project-based learning, peer feedback, reflective practice and community-supported learning environments in rapidly evolving technical fields. Social implications Online communities can function as accessible sociotechnical learning infrastructures through which aspiring and current IT professionals obtain guidance, feedback, mentorship and developmental support beyond formal institutions. Originality/value This study offers an empirically grounded conceptual framework showing how community-mediated interaction on Reddit can support informal IT learning, self-regulated learning, competency development and evolving career trajectories.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · GPT-5-mini helped classify Reddit segments for self-regulated learning and motivation, alongside manual coding; unclear whether LLM–human agreement was reported.

**Решение:** =

---

### 109 · R0987

**Assessing the potential of LLM-assisted annotation for corpus pragmatics: the case of humor**

2026 · Research Square · journalarticle/none, preprint, ppr · en · https://doi.org/10.21203/rs.3.rs-8559781/v1

Abstract Corpus pragmatics faces ongoing challenges in quantitatively studying context-dependent categories like humor, given their subjectivity and the need for costly interrater reliability checks. Recent advances in LLMs offer a potential way to streamline these processes for pragmatic annotation tasks. This paper investigates that potential through an analysis of Italian political discourse on X, focusing on humorous tweets and their discursive functions (Attardo, 2020). We compare the performance of GPT-4o, LLaMA-3.3-70B-Instruct, and a novice annotator against that of an expert annotator. For the detection of humor, both models reached high agreement with the expert annotator (in particular, GPT-4o: Cohen’s k = 0.75; AC1 = 0.87). Instead, agreement dropped for the classification of humor functions (GPT-4o: Cohen’s k = 0.37; AC1 = 0.70). Qualitative results suggest that the models rely heavily on lexical cues rather than demonstrating deeper pragmatic competence. These findings indicate that while LLMs can provide useful assistance in the initial stages of large-scale annotation, they remain limited in capturing the nuanced and context-dependent nature of pragmatic functions.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o/LLaMA annotated humor and its functions in political tweets against an expert annotator; unclear whether humor here counts as a psychological construct.

**Решение:** =

---

### 110 · R0989

**Enhancing Empathetic Ability in LLMs: A Sociology View**

2026 · Lecture notes in networks and systems · conference-paper · en · https://doi.org/10.1007/978-3-032-11946-9_38

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract; title suggests improving LLM empathy (likely generation), but empathy evaluation against human ratings cannot be ruled out.

**Решение:** =

---

### 111 · R0998

**Prompt Sensitivity in LLM-Based Divergent Thinking Scoring — Data and Code**

2026 · OSF · dataset/project, preprint · en · https://doi.org/10.17605/osf.io/nq9s8

Companion data and code for the manuscript 'Architecture-Conditional Prompt Sensitivity in LLM Evaluators: A Dual-Axis Account of Instruction Style Effects on Divergent Thinking Scoring'. The deposit contains the 79 per-cell LLM scoring CSVs (65 main-grid cells spanning 13 models x 5 prompt variants, 12 temperature-sweep cells, and 2 supplementary cells), the master metrics file, the frozen prompt specifications (V1-V5), the complete Python analysis pipeline, and the 7 manuscript figures at 1200 DPI. The materials permit independent re-execution of every figure, table, and statistical claim in the manuscript from the per-cell scoring data forward. License: CC-BY 4.0 (data), MIT (analysis scripts). See README.md for the data dictionary and reproduction instructions.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · 13 LLMs score divergent thinking responses; the metrics probably compare against human ratings, but the abstract never says so.

**Решение:** =

---

### 112 · R0999

**Scoring Divergent Thinking with LLMs — Data and Code**

2026 · OSF · dataset/project, preprint · en · https://doi.org/10.17605/osf.io/g2xdw

Companion data and code for the manuscript 'Scoring Divergent Thinking with LLMs: Scaling Laws, Instruction Sensitivity, Correlation–Calibration Decoupling, and Psychometric Reliability'. The deposit contains the 62 per-cell LLM scoring CSVs (31 models × 2 prompt conditions, spanning local BF16/NF4 and cloud-API access modalities), their sibling per-cell metrics files, the master metrics file, the Williams' significance-test output, the frozen two-condition prompt specification, the complete Python analysis pipeline (12 scripts), and the 7 manuscript figures at preview and 1200-DPI resolution. The materials permit independent re-execution of every figure, table, and statistical claim in the manuscript from the per-cell scoring data forward. License: CC-BY 4.0 (data), MIT (analysis scripts). See README.md for the data dictionary and reproduction instructions.

**ИИ:** + · обе модели · подсчёт методики · 31 LLMs score divergent-thinking responses; correlation and calibration metrics imply comparison with human ratings. Companion dataset to the manuscript.

**Решение:** =

---

### 113 · R10000

**When the Prompt becomes the Codebook: Grounded Prompt Engineering (GROPROE) and its application to Belonging Analytics**

2025 · International Conference on Learning Analytics and Knowledge · journalarticle, book, conference-paper · en · https://doi.org/10.1145/3706468.3706564

With the emergence of generative AI, the field of Learning Analytics (LA) has increasingly embraced the use of Large Language Models (LLMs) to automate qualitative analysis. Deductive analysis requires theoretical or other conceptual grounding to inform coding. However, few studies detail the process of translating the literature into a codebook, and then into an effective LLM prompt. In this paper, we introduce Grounded Prompt Engineering (GROPROE) as a systematic process to develop a literature-grounded prompt for deductive analysis. We demonstrate our GROPROE process on a dataset of 860 written reflections, coding for students’ affective engagement and sense of belonging. To evaluate the quality of the coding we demonstrate substantial human/LLM Inter-Annotator Reliability (IAR). To evaluate the consistency of LLM coding, a subset of the data was analysed 60 times using the LLM Quotient showing how this stabilized for most codes. We discuss the dynamics of human-AI interaction when following GROPROE, foregrounding how the prompt took over as the iteratively revised codebook, and how the LLM provoked codebook revision. The contributions to the LA field are threefold: (i) GROPROE as a systematic prompt-design process for deductive coding grounded in literature, (ii) a detailed worked example showing its application to Belonging Analytics, and (iii) implications for human-AI interaction in automated deductive analysis.

**ИИ:** + · обе модели · кодирование по кодбуку · LLM deductively codes 860 student reflections for affective engagement and sense of belonging; human/LLM inter-annotator reliability reported.

**Решение:** =

---

### 114 · R10006

**Exploring negative experiences in psychotherapy using an NLP approach on online forum data.**

2025 · Npj mental health research · journal article, journalarticle, article · eng · https://doi.org/10.1038/s44184-025-00172-4

Negative experiences with psychotherapy are common, affecting 3-25% of patients. However, their causes remain underexplored despite their substantial impact on therapy outcomes. Online forums provide unique insights into patients' concerns due to their anonymity. We collected and anonymized forum posts and used a large language model to identify psychotherapy dissatisfaction. Human raters validated the outputs. To identify and analyze themes, we applied clustering, topic modeling, sentiment analysis, and classification based on an existing meta-analytic framework. In total, we extracted 28,079 text passages reflecting dissatisfaction. Clustering yielded 55 subthemes, covering therapist misbehavior, negative treatment effects, poor alliance, treatment mismatch, and healthcare-related frustrations, extending existing taxonomies. Our NLP-based, mixed-methods approach highlights dissatisfaction as both frequent and multifaceted, surfacing themes often overlooked in traditional research, such as structural barriers and lasting psychological consequences. These findings expand previous frameworks and underscore the need for better recognition of negative therapy experiences.

**ИИ:** + · обе модели · проверка кодирования внутри исследования · An LLM identified psychotherapy dissatisfaction in forum posts, and human raters validated its outputs, so LLM–human agreement is likely reported.

**Решение:** =

---

### 115 · R10007

**Exploring negative experiences in psychotherapy: Patient dissatisfaction as a use case for a new NLP approach leveraging big data from online forums**

2025 · Research Square · preprint, ppr · en · https://doi.org/10.21203/rs.3.rs-6766808/v1

Abstract Negative experiences with psychotherapy are common, affecting 3–25% of patients. However, their causes remain underexplored despite their substantial impact on therapy outcomes. Online forums provide unique insights into patients’ concerns due to their anonymity. We collected and anonymized forum posts and used a large language model to identify psychotherapy dissatisfaction. Human raters validated the outputs. To identify and analyze themes, we applied clustering, topic modeling, n-gram and sentiment analysis, and classification based on an existing meta-analytic framework. In total, we extracted 28,079 text segments reflecting dissatisfaction. Clustering yielded 55 subthemes, covering therapist misbehavior, negative treatment effects, poor alliance, treatment mismatch, and healthcare-related frustrations, extending existing taxonomies. Our NLP-based, mixed-methods approach highlights dissatisfaction as both frequent and multifaceted, surfacing themes often overlooked in traditional research, such as structural barriers and lasting psychological consequences. These findings expand previous frameworks and underscore the need for better recognition of negative therapy experiences.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLM flagged psychotherapy dissatisfaction in forum posts and human raters validated the outputs; unclear whether independent human coding gives agreement figures.

**Решение:** =

---

### 116 · R10017

**Case reports unlocked: Leveraging retrieval-augmented generation with large language models to advance research on psychological child maltreatment.**

2025 · Child abuse & neglect · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.1016/j.chiabu.2025.107653

Background: Research on psychological child maltreatment is impeded by a lack of high-quality structured data. Crucial information is often documented in child protective services (CPS) case files, but only in narrative form. Recent research on the utilization of retrieval-augmented generation (RAG) methods with large language models (LLMs) for extracting structured data from narratives has demonstrated significant potential. RAG methods can facilitate automated classification, thereby eliminating the need for laborious annotation. Objective: We aimed to extract structured data from narrative casework reports by utilizing RAG and LLMs to classify mentions of 24 CPS case factors. These factors encompass child maltreatment indicators, risk factors associated with parental, family, and child characteristics, CPS interventions, and their outcomes. We focused on examining the extraction of psychological abuse due to its complex nature and difficulty in assessing this phenomenon. The results were compared with parental lack of cooperation, a factor with a presumed medium level of recognition difficulty, and a more straightforward factor of parental alcohol abuse. Methods: We developed a four-stage workflow comprising of (1) case reports collection, (2) RAG based assessment of case factor mentions, (3) automated extraction of case factors from RAG assessments, and (4) case labeling. All CPS reports (N = 29,770) between 2008 and 2022 from Switzerland&apos;s largest CPS provider were collected. Model performance was evaluated compared against human-coded validation data on assessments. Two expert human reviewers independently classified weighted random samples of reports to validate the findings from which a consensus dataset was derived. Results: The model classified psychological abuse, lack of parental cooperation and parental alcohol abuse compared to a consensus dataset, with an accuracy of 82 %, 83 %, and 95 %, respectively, surpassing the agreement rates between the two human reviewers (79 %, 80 %, and 93 %). Conclusions: RAG based assessment can replicate human judgment even on complex CPS case factors. High accuracy and complete inter-rater agreement level was achieved for factors that are straightforward to classify, such as parental alcohol abuse. The effectiveness of these methods stems from the presence of contextual clues related to case factors within a few sentences across different sections of the text, rather than from characteristics inherent to the entire text. For case factors such as parental lack of cooperation, both supporting and refuting evidence needs to be assessed to achieve optimal accuracy. Careful consideration of potential biases and limitations in RAG methods is advised. These applications can serve as early warning systems, by identifying critical factors from extensive case notes that might otherwise be overlooked, supporting professionals in making informed decisions and improving outcomes for at-risk children.

**ИИ:** + · обе модели · кодирование по кодбуку · LLM with RAG classified psychological abuse and other case factors in CPS narrative reports; results checked against consensus of two expert human coders.

**Решение:** =

---

### 117 · R10025

**Development and preliminary testing of a secure large language model-based chatbot for brief alcohol counseling in young adults.**

2025 · Drug and alcohol dependence · journal article, journalarticle, article · eng · https://doi.org/10.1016/j.drugalcdep.2025.112697

Objective Young adults face elevated risks from alcohol use yet encounter significant barriers to accessing evidence-based interventions. Large language models (LLMs) represent a promising advancement for delivering personalized behavioral interventions, but their application to alcohol counseling remains unexplored. This study evaluated the development and preliminary outcomes of a Secure GPT-4-powered text-based Motivational Interviewing Conversational Agent (MICA). Method Using a prospective single-arm pilot design, we evaluated MICA across two phases (Phase I: n = 8; Phase II: n = 37), editing the LLM prompts between Phases. Participants aged 18-25 who reported consuming ≥ 10 standard alcohol units weekly completed a counseling session with MICA. We evaluated safety and compared MI fidelity (relational and technical sub-scales of the Client Evaluation of MI [CEMI]) and usability (System Usability Scale) between Phases. We also explored surrogate measures of effectiveness (i.e. proportion of change talk to sustain talk from session logs) and qualitative feedback themes. Results No unsafe responses were observed. MI fidelity improved significantly in the CEMI relational sub-scale from Phase I to II (67.2 % to 82.6 %, p = 0.03). Usability remained consistently high across phases (Phase I: 85.4; Phase II: 80.9; p = 0.45). The proportion of within-session change talk was also consistently high (Phase I: 65.2 %; Phase II: 75.8 %; p = 0.10). Conclusions This study provides preliminary evidence that LLM-based chatbots can deliver MI-adherent alcohol interventions that are both acceptable to young adults and maintain high MI fidelity. Future research should employ randomized controlled designs with longer follow-up periods to evaluate impact on drinking outcomes.

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: GPT-4 chatbot delivers MI counseling; fidelity rated by clients, and the abstract describes no LLM coding task compared against human coders.); Sonnet ? (неясно, сравнивали ли с людьми: GPT-4 MI chatbot pilot; change/sustain talk coded from session logs, but unclear whether an LLM coded it and was compared with human coders.)

**Решение:** -

---

### 118 · R10055

**Emotionally-Aware Agents for Dispute Resolution**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2509.04465

In conflict, people use emotional expressions to shape their counterparts' thoughts, feelings, and actions. This paper explores whether automatic text emotion recognition offers insight into this influence in the context of dispute resolution. Prior work has shown the promise of such methods in negotiations; however, disputes evoke stronger emotions and different social processes. We use a large corpus of buyer-seller dispute dialogues to investigate how emotional expressions shape subjective and objective outcomes. We further demonstrate that large-language models yield considerably greater explanatory power than previous methods for emotion intensity annotation and better match the decisions of human annotators. Findings support existing theoretical models for how emotional expressions contribute to conflict escalation and resolution and suggest that agent-based systems could be useful in managing disputes by recognizing and potentially mitigating emotional escalation.

**ИИ:** + · обе модели · кодирование по кодбуку · LLMs annotate emotion intensity in dispute dialogues; the abstract says they better match human annotators' decisions.

**Решение:** =

---

### 119 · R10103

**Acoustic feature differences across client utterance classes in counseling dialogues**

2025 · The Journal of the Acoustical Society of America · journalarticle, conference-abstract · en · https://doi.org/10.1121/10.0041450

This study aims to develop an acoustic-feature-based model of client utterances in the DAIC-WoZ dataset, a corpus of clinical interviews collected by the USC Institute for Creative Technologies. DAIC-WoZ contains recorded speech from counseling sessions involving 60 depressed and 133 non-depressed participants, and provides transcriptions, face video, and 11 standard acoustic features (F0, NAQ, QOQ, H1–H2, PSP, MDQ, peakSlope, Rd, MFCC, HMPDM, HMPDD). Additionally, the utterances in the dataset have already been classified according to client-centered therapy principles, which were developed in our previous studies using an LLM-based model with few-shot learning. A two-way ANOVA was conducted for each acoustic feature, using client utterance class (five categories) and depression status (depressed versus non-depressed) as factors. The results showed significant differences in features such as pitch variability and spectral slope across utterance classes, and between depression status groups. Furthermore, significant interaction effects indicated that depression status modulated the acoustic marker differences across the utterance classes. For example, high F0 was observed in depressed participants within the emotional expression class, whereas low F0 was found in depressed participants in the factual information class. These findings are expected to be useful for the development of multimodal counseling AI agents in the future.

**ИИ:** разошлись — Opus -7 (другое — напишите почему: Acoustic ANOVA study; reuses LLM utterance classes from earlier work, and no LLM–human coding agreement is reported here.); Sonnet ? (неясно, сравнивали ли с людьми: Acoustic ANOVA study; client utterances were classified by an LLM in prior work. Unclear whether this record or the earlier work compared that classification with human coding.)

**Решение:** -

---

### 120 · R10104

**How Students (Really) Use ChatGPT: Uncovering Experiences Among Undergraduate Students**

2025 · arXiv.org · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2505.24126

We examine how undergraduate students integrate ChatGPT into everyday self-directed learning, analyzing 10,536 naturalistic messages donated by 36 students over a year. A sequential mixed-methods pipeline pairs iterative qualitative coding with zero-shot language-model annotation validated against human labels (kappa = 0.75-0.91). It yields a five-category taxonomy: Information Seeking, Content Generation, Language Use, Student-ChatGPT Interaction, and ChatGPT Response Behavior. Time-lagged linear regression and Cox proportional-hazards models link these categories to sustained engagement. Three findings stand out. First, structured tasks (theory application, code writing, job-application content, multiple-choice questions) predict continued use; ChatGPT becomes incorporated into academic rhythms when gratifications are reliably fulfilled. Second, system-issued "apologies" are the strongest positive predictor of increased engagement, outweighing every task-completion predictor. We name this mechanism "repair gratification": the reward of a breakdown acknowledged and repaired rather than a task simply completed. Third, interactional strain--prompt revision, frustration, follow-up clarification--predicts disengagement. When managing the system falls on the user without system accountability, students abandon the tool. We interpret these results through Self-Directed Learning, Uses and Gratifications Theory, and Expectancy Violations Theory, mapping predictors onto positive/negative violations and confirmations. We close with design recommendations for graduated repair patterns, mode-aware interaction, and verification affordances, and outline a participatory AI-literacy agenda for higher education.

**ИИ:** ? · обе модели · неясен конструкт · Zero-shot LLM annotation of student ChatGPT messages validated against human labels (κ=0.75–0.91); the categories are mostly usage types, with some frustration/strain.

**Решение:** =

---

### 121 · R10126

**An Explainable Artificial Intelligence Text Classifier for Suicidality Prediction in Youth Crisis Text Line Users: Development and Validation Study.**

2025 · JMIR public health and surveillance · journal article, journalarticle, article · eng · https://doi.org/10.2196/63809

BACKGROUND: Suicide represents a critical public health concern, and machine learning (ML) models offer the potential for identifying at-risk individuals. Recent studies using benchmark datasets and real-world social media data have demonstrated the capability of pretrained large language models in predicting suicidal ideation and behaviors (SIB) in speech and text. OBJECTIVE: This study aimed to (1) develop and implement ML methods for predicting SIBs in a real-world crisis helpline dataset, using transformer-based pretrained models as a foundation; (2) evaluate, cross-validate, and benchmark the model against traditional text classification approaches; and (3) train an explainable model to highlight relevant risk-associated features. METHODS: We analyzed chat protocols from adolescents and young adults (aged 14-25 years) seeking assistance from a German crisis helpline. An ML model was developed using a transformer-based language model architecture with pretrained weights and long short-term memory layers. The model predicted suicidal ideation (SI) and advanced suicidal engagement (ASE), as indicated by composite Columbia-Suicide Severity Rating Scale scores. We compared model performance against a classical word-vector-based ML model. We subsequently computed discrimination, calibration, clinical utility, and explainability information using a Shapley Additive Explanations value-based post hoc estimation model. RESULTS: The dataset comprised 1348 help-seeking encounters (1011 for training and 337 for testing). The transformer-based classifier achieved a macroaveraged area under the curve (AUC) receiver operating characteristic (ROC) of 0.89 (95% CI 0.81-0.91) and an overall accuracy of 0.79 (95% CI 0.73-0.99). This performance surpassed the word-vector-based baseline model (AUC-ROC=0.77, 95% CI 0.64-0.90; accuracy=0.61, 95% CI 0.61-0.80). The transformer model demonstrated excellent prediction for nonsuicidal sessions (AUC-ROC=0.96, 95% CI 0.96-0.99) and good prediction for SI and ASE, with AUC-ROCs of 0.85 (95% CI 0.97-0.86) and 0.87 (95% CI 0.81-0.88), respectively. The Brier Skill Score indicated a 44% improvement in classification performance over the baseline model. The Shapley Additive Explanations model identified language features predictive of SIBs, including self-reference, negation, expressions of low self-esteem, and absolutist language. CONCLUSIONS: Neural networks using large language model-based transfer learning can accurately identify SI and ASE. The post hoc explainer model revealed language features associated with SI and ASE. Such models may potentially support clinical decision-making in suicide prevention services. Future research should explore multimodal input features and temporal aspects of suicide risk.

**ИИ:** разошлись — Opus ? (другое: Fine-tuned transformer with LSTM layers on crisis chats with human-coded C-SSRS labels. Probably an encoder (BERT-type) model; the full text must confirm.); Sonnet -5 (нет генеративной LLM (только BERT или классическое ML) либо только согласие LLM с LLM: Fine-tuned encoder transformer (pretrained BERT-type plus LSTM) classifying crisis chats against C-SSRS scores; not a generative LLM coding against human coders.)

**Решение:** -

---

### 122 · R10127

**Large language model performance versus human expert ratings in automated suicide risk assessment.**

2025 · Scientific reports · journal article, journalarticle, article · eng · https://doi.org/10.1038/s41598-025-22402-7

Abstract Large Language Models’ (LLMs) potential for psychological diagnostics requires systematic evaluation. We aimed to investigate conditions for reliable and valid psychological assessments, focusing on suicide risk evaluation in clinical data by comparing LLM-generated ratings with human expert ratings across model configurations., analyzing 100 youth crisis text line conversation transcripts rated by four experts using the Nurses’ Global Assessment of Suicide Scale (NGASR). Using Mixtral-8x7B-Instruct, we generated ratings across three temperature settings and prompting styles (zero-shot, few-shot, chain-of-thought). Across configurations we compared (a) inter-rating-reliability for AI-generated NGASR risk and sum scores, (b) LLM-to-human observer agreement regarding sum score, risk category, and item, using Krippendorff’s α, (c) classification metrics of risk categories and individual items against human ratings. LLM configuration strongly influenced assessment reliability. Zero-shot prompting at temperature 0 yielded perfect inter-rating reliability (α = 1.00, 95% CI: [1–1] for high &amp; very high risk), while few-shot prompting showed best human-AI agreement for very high risk (α = 0.78, 95% CI: [0.67–0.89]) and strongest classification performance (balanced accuracy 0.54–0.71). Lower temperatures consistently improved reliability and accuracy. However, critical clinical items showed poor validity. Our findings establish optimal conditions (zero temperature, task-specific prompting) for LLM-based psychological assessment. However, inconsistent clinical item performance and only moderate LLM-to-human observer agreement limit LLMs to initial screening rather than detailed assessment, requiring careful parameter control and validation.

**ИИ:** + · обе модели · клиническая оценка · Mixtral rated suicide risk (NGASR) in crisis text transcripts; agreement with four expert raters reported using Krippendorff's alpha.

**Решение:** =

---

### 123 · R10130

**Automated Suicide Risk Factor Monitoring in Crisis Text Line Users: Comparative Study of AI and Human Ratings Using Large Language Models**

2025 · Research Square · preprint, ppr, posted-content · https://doi.org/10.21203/rs.3.rs-6210376/v1

Abstract Background : Large Language Models´ (LLMs) potential for psychological diagnostics requires systematic evaluation. Objective : To investigate conditions for reliable and valid psychological assessments, focusing on suicide risk evaluation in clinical data by comparing LLM-generated ratings with human expert ratings across across configurations. Methods : We analyzed 100 youth crisis conversation transcripts rated by four experts using the Nurses Global Assessment of Suicide Scale (NGASR). Using Mixtral-7x8b-Instruct, we generated ratings across three temperature settings and prompting styles (zero-shot, few-shot, chain-of-thought). Across configurations we compared a) inter-rating-reliability for AI-generated NGASR risk and sum scores, b) LLM-to-human observer agreement regarding sum score, risk category, and item, using Krippendorff´s α, c) classification metrics of risk categories and individual items against human ratings. Results : LLM configuration strongly influenced assessment reliability. Zero-shot prompting at temperature 0 yielded perfect inter-rating reliability (α=1.00, 95% CI: [1-1] for high &amp; very high risk), while few-shot prompting showed best human-AI agreement for very high risk (α=0.78, 95% CI: [0.67-0.89]) and strongest classification performance (balanced accuracy 0.54-0.71). Lower temperatures consistently improved reliability and accuracy. However, critical clinical items showed poor validity. Discussion : Our findings establish optimal conditions (zero temperature, task-specific prompting) for LLM-based psychological assessment. However, inconsistent clinical item performance and only moderate to-human agreement limit LLMs to initial screening rather than detailed assessment, requiring careful parameter control and validation.

**ИИ:** + · обе модели · клиническая оценка · Mixtral rated NGASR suicide risk on crisis transcripts; Krippendorff's alpha agreement with four expert raters reported.

**Решение:** =

---

### 124 · R10131

**Using GPT-4o to interpret patient-reported outcomes without training**

2025 · JNCI Journal of the National Cancer Institute · article · en · https://doi.org/10.1093/jnci/djaf016

Advances in large language models (LLMs) such as OpenAI’s Generative Pre-trained Transformer-4o (GPT-4o) have prompted interest regarding their use in oncology. LLMs distill vast amounts of text data such as postings in online forums, scientific articles, and educational materials.1 As these methods evolve, there is potential for leveraging their capabilities in summarizing patient-authored free text data to patient-reported outcomes (PROs).2,3 While conventional PROs use standardized questions to broadly assess treatment- and disease-related domains in clinical trials and routine care,4 free text data are ideal for capturing patients’ nuanced experiences “in their own words”.5 However, before LLMs can be applied in coding PROs, we sought to develop, as a proof of concept, methodological procedures for unsupervised learning to automatically interpret patient-generated free text phrases without pre-training by human coders (ie, “zero-shot learning [ZSL]”), and demonstrate that LLM performance is similar to traditional human qualitative analysis. We used archived interview transcripts (N = 19) from 9 patients, 2 caregivers, and 7 physicians (891 total participant utterances) from a study of cancer patients’ prognostic awareness that were previously coded6 by 2 humans into 5 themes (Figure 1). The GPT-4o model licensed to our institution is comprised of over 1 trillion parameters, pre-trained by OpenAI and provided in Microsoft Azure through a secure enterprise cloud-based offering. The ZSL procedure instructed GPT-4o to match transcript entries to these 5 themes de novo, relying solely on semantic contents. Prompt engineering experimented with optimal queries: (1) a “base” prompt included basic descriptions of each theme; (2) a “comprehensive” prompt had very detailed descriptions; and (3) “hybrid” prompts featured mixed descriptions. Performance was evaluated by precision, recall, F1-score, and Kappa reliability using human analysts as the ground truth. Additionally, duplicated utterances (112 with >90% similarity) assessed internal consistency in human analysts and GPT-4o. Confusion matrix for GPT-4o on the dataset. GPT-4o yielded acceptable performance in text classification using verbatim utterances alone; best performance was obtained with the “hybrid” prompt (56% precision, 54% recall, 55% F1-score, Κ = 0.43). The “comprehensive” and “base” prompts fared worse (57% precision, 54% recall, 54% F1-score, Κ = 0.42; 55% precision, 46% recall, 45% F1-score, Κ = 0.32, respectively). These metrics indicate better than chance classification (20%). However, longer prompts with detailed explanations and examples did not necessarily lead to the best performance. Encouragingly, internal consistency in GPT-4o nearly matched that of human coders (ie, Κ = 0.43 and 0.44). As a necessary initial step for generalizing LLMs broadly to code PRO domains without pre-training, we have presented promising evidence that an unsupervised LLM can code patient-generated free text data. Ultimately, if a patient undergoing chemotherapy communicates with their doctor via a portal message and describes “I felt sick to my stomach…,” a further validated LLM may interpret this as signs of “mild nausea/vomiting” in real time and prompt clinicians for immediate action (eg, prescribing antiemetics) to minimize treatment-related adverse events and risk of chemotherapy interruptions. However, caution is advised, as current sub-optimal performance suggests that ZSL applications might be more suitable for initial screening, leaving uncertain classifications for human coders to detect nuanced meaning. Role of the funder—support of investigator time and effort in relation to the design of the study, data collection, analysis, interpretation of the data, the writing of the correspondence, and the decision to submit the correspondence for publication. Thomas Michael Atkinson, PhD (Conceptualization; Data curation; Formal analysis; Funding acquisition; Investigation; Methodology; Project administration; Resources; Software; Supervision; Validation; Visualization; Writing—original draft; Writing—review & editing), Aleksandr Petrov, MS (Conceptualization; Data curation; Formal analysis; Methodology; Project administration; Software; Validation; Visualization; Writing—original draft; Writing—review & editing), Kathleen A. Lynch, MPH (Conceptualization; Data curation; Formal analysis; Methodology; Validation; Writing—original draft; Writing—review & editing), Login S. George, PhD (Conceptualization; Data curation; Formal analysis; Investigation; Methodology; Project administration; Validation; Writing—original draft; Writing—review & editing), Jennifer R. Cracchiolo, MD (Conceptualization; Formal analysis; Investigation; Methodology; Validation; Writing—original draft; Writing—review & editing), Bobby Daly, MD (Conceptualization; Formal analysis; Investigation; Methodology; Validation; Writing—original draft; Writing—review & editing), Kristen L. Fessele, PhD, RN (Conceptualization; Formal analysis; Investigation; Methodology; Validation; Writing—original draft; Writing—review & editing), James H. Flory, MD (Conceptualization; Investigation; Methodology; Validation; Writing—original draft; Writing—review & editing), Jun J. Mao, MD (Conceptualization; Formal analysis; Investigation; Methodology; Validation; Writing—original draft; Writing—review & editing), Yuelin Li, PhD (Conceptualization; Data curation; Formal analysis; Funding acquisition; Investigation; Methodology; Project administration; Resources; Software; Supervision; Validation; Visualization; Writing—original draft; Writing—review & editing). This research was funded in part through a National Institutes of Health/National Cancer Institute Cancer Center Support Grant P30 CA008748-58, which provides partial support for the Patient-Reported Outcomes, Community Engagement, and Language Core Facility used in this investigation. The content of this research is solely the responsi

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-4o coded interview utterances on prognostic awareness into five human-coded themes; reports kappa and F1 against two human coders.

**Решение:** =

---

### 125 · R10135

**Potential of ChatGPT in youth mental health emergency triage: Comparative analysis with clinicians.**

2025 · PCN reports : psychiatry and clinical neurosciences · journal article, journalarticle, article · eng · https://doi.org/10.1002/pcn5.70159

Aim Large language models, such as GPT-4, are increasingly integrated into healthcare to support clinicians in making informed decisions. Given ChatGPT's potential, it is necessary to explore such applications as a support tool, particularly within mental health telephone triage services. This study evaluates whether GPT Models can accurately triage psychiatric emergency vignettes and compares its performance to that of clinicians. Methods A cross-sectional study was performed to assess the performance of three different GPT-4 models (GPT-4o, GPT-4o Mini, and GPT-4 Legacy) in psychiatric emergency triage. Twenty-two psychiatric emergency vignettes, intended to represent realistic prehospital triage scenarios, were initially drafted using ChatGPT and subsequently reviewed and refined by the research team to ensure clinical accuracy and relevance. The GPT-4 models independently generated clinical responses to the vignettes over three iterations to ensure consistency. Thereafter, two advanced practice nurse practitioners independently assessed these responses utilizing a 3-point Likert-type scale for the main triage criteria: risk level ( Low = 1 to High = 3), necessity of hospital admission ( Ye s = 1; No = 2), and urgency of clinical evaluation ( Low = 1 to High = 3). Additionally, the nurse practitioners provided their clinical judgments independently for each vignette. Interrater reliability was evaluated by comparing responses generated by the GPT Models with the independent clinical assessments of nurse practitioners, and agreement was evaluated using Cohen's Kappa. The clinical expert committee ( n = 3) conducted qualitative analyses of responses from both GPT Models using a systematic coding method to evaluate triage accuracy, clarity, completeness, and total score. The evaluation of responses focused on three key triage criteria: risk ( Low = 1 to High = 3), admission necessity ( Ye s = 1; No = 2), and urgency of clinical evaluation ( Low = 1 to High = 3). Results GPT Models had an average admission score of 1.73 (standard deviation [SD] = 0.45; scale: Yes = 1, No = 2), indicating a general trend toward recommending against hospital admission. Risk (mean = 2.12, SD = 0.83) and urgency (mean = 2.27, SD = 0.44) assessments suggested moderate-to-high perceived risk and urgency (scale: Low = 1, High = 3), reflecting conservative decision-making. Interrater reliability between clinicians and GPT-4 models was substantial, with Cohen's Kappa values of 0.77 (admission), 0.78 (risk), and 0.76 (urgency). GPT Models' responses tended toward slight over-triage, indicated by four false-positive admission recommendations and zero false negatives. Substantial interrater reliability was observed between clinicians and GPT-4 responses across the three triage criteria (Cohen's Kappa: admission = 0.77; risk = 0.78; urgency = 0.76).The mean scores for triage criteria responses between GPT-4 models and clinicians exhibited consistent patterns with minimal variability. Overall, GPT Models had a tendency to over-triage patients as indicated by four total false positives and zero false negatives for admissions. Conclusion This study indicates that GPT Models may serve as supportive decision-support tools in mental health telephone triage, particularly for psychiatric emergencies. Although response variability across iterations was minimal, most discrepancies in admission decisions were identified as false positives, reflecting that GPT Models may have a tendency to over-triage relative to clinician judgment. Further investigation is needed to establish robust structure to increase alignment with clinical decisions and response relevance in clinical practice.

**ИИ:** + · обе модели · клиническая оценка · GPT-4 models and nurse practitioners independently rated risk, admission and urgency on the same psychiatric emergency vignettes; agreement reported as Cohen's kappa.

**Решение:** =

---

### 126 · R10136

**Potential of ChatGPT in Youth Mental Health Emergency Triage: Comparative Analysis with Clinicians**

2025 · medRxiv · preprint, ppr, posted-content · https://doi.org/10.1101/2025.01.06.24319771

ABSTRACT Background Large language models (LLMs), such as GPT-4, are increasingly integrated into healthcare to support clinicians in making informed decisions. Given ChatGPT’s potential, it is necessary to explore such applications as a support tool, particularly within mental health telephone triage services. This study evaluates whether GPT-4 models can accurately triage psychiatric emergency vignettes and compares its performance to clinicians. Methods A cross-sectional study with qualitative analysis was conducted. Two clinical psychologists developed 22 psychiatric emergency vignettes. Responses were generated by three versions of GPT-4 (GPT-4o, GPT-4o Mini, GPT-4 Legacy) using ChatGPT, and two independent nurse practitioners (clinicians). The responses focused on three triage criteria: risk (Low 1-3 High), admission (Yes-1; No-2), and urgency (Low 1-3 High). Results Substantial interrater reliability was observed between clinicians and GPT-4 responses across the three triage criteria (Cohen’s Kappa: Admission = 0.77; Risk = 0.78; Urgency = 0.76). Among the GPT-4 models, Kappa values indicated moderate to substantial agreement (Fleiss’ Kappa: Admission = 0.69, Risk = 0.63, Urgency = 0.72). The mean scores for triage criteria responses between GPT-4 models and clinicians exhibited consistent patterns with minimal variability. Admission responses had a mean score of 1.73 (SD = 0.45), risk scores had a mean of 2.12 (SD= 0.83), and urgency scores averaged 2.27 (SD = 0.44). Conclusion This study suggests that GPT-4 models could be leveraged as a support tool in mental health telephone triage, particularly for psychiatric emergencies. While findings are promising, further research is required to confirm clinical relevance.

**ИИ:** + · обе модели · клиническая оценка · GPT-4 rated risk, admission and urgency for psychiatric emergency vignettes, with Cohen's kappa agreement against clinician ratings reported.

**Решение:** =

---

### 127 · R1018

**From OR dialogue to actionable feedback: a scalable method for analyzing intraoperative teaching**

2026 · Global Surgical Education - Journal of the Association for Surgical Education · journalarticle, article · en · https://doi.org/10.1007/s44186-026-00570-y

Abstract Purpose Intraoperative feedback is essential to surgical training, yet it is transient, inconsistently documented, and difficult to analyze at scale. Traditional qualitative methods for studying operative dialogue are labor-intensive, limiting their use for educational research and surgical trainee feedback. This study describes the development and evaluation of an AI-assisted qualitative coding pipeline for analyzing intraoperative attending-trainee communication. We frame this work as a proof-of-concept feasibility study. Methods Audio-recorded dialogue from 25 general and colorectal surgical operations was transcribed and formatted for line-by-line coding using a 38-category thematic codebook. A custom GPT built on GPT-4o with retrieval-augmented generation was developed to assign codes to each utterance within a human-in-the-loop workflow. AI reliability was assessed through run-to-run agreement on a purposive sample of five transcripts. Coding efficiency and error rates were tracked across AI-assisted and manual workflows. Results The AI-assisted workflow reduced coding time to less than 20% of manual effort, with an overall error rate of 2.0%. Run-to-run AI agreement across 2,245 lines demonstrated 79% agreement with substantial concordance (κ = 0.75). Agreement was highest for explicit utterance types and lowest for codes requiring contextual interpretation. Conclusions In this proof-of-concept evaluation, an AI-supported, human-verified coding workflow achieved the efficiency and reliability needed to make scalable analysis of intraoperative teaching dialogue feasible. This approach has the potential to convert routine operative communication into structured, actionable feedback for trainees and faculty.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o applies a codebook to surgical teaching dialogue; the abstract reports run-to-run kappa and human-verified error rate. Psychological construct is borderline.

**Решение:** =

---

### 128 · R10180

**Harnessing Generative Diversity: An LLM Framework for Consistent Qualitative Assessment**

2025 · preprint · https://doi.org/10.36227/techrxiv.176107757.72471376/v2

The stochastic nature of Large Language Models (LLMs) is typically viewed as a reliability challenge for high-stakes tasks like qualitative assessment. We reframe this stochasticity not as random noise, but as ‘generative diversity’: a range of coherent reasoning paths produced by the model. We argue this diversity is a valuable feature, analogous to a committee of experts offering multiple valid perspectives. We propose a novel Human-AI collaboration framework designed specifically to harness this diversity to produce consistent and trustworthy evaluations. We systematically compare three pipelines—zero-shot, rubric-based, and our proposed pairwise comparison. The results show that the pairwise approach effectively distills generative diversity into a stable assessment, achieving a strong correlation with domain expert judgments (r = 0.716). Furthermore, qualitative analysis reveals that while LLMs provide consistent text-grounded baselines, they lack the tacit knowledge to identify exceptional outliers. This work thus proposes a new Human-AI partnership paradigm: by treating generative diversity as a feature to be engineered, we can automate reliable baseline assessments, freeing human experts to focus on high-stakes, nuanced judgments that require contextual insight.

**ИИ:** ? · обе модели · неясен конструкт · LLM qualitative assessments correlated with domain expert judgments (r=0.716), but the abstract doesn't say what texts or construct were assessed.

**Решение:** =

---

### 129 · R10185

**A pipeline for automatic bipolar disorder analysis through anonymization and LLM-as-a-judge**

2025 · UPCommons institutional repository (Universitat Politècnica de Catalunya) · abstract, pmc, journalarticle · eng · https://doi.org/10.1192/j.eurpsy.2026.10414

Bipolar Disorder (BD) is a psychiatric condition characterized by significant shifts in mood, energy and thought processes, observed in episodes of mania, depression and euthymia. This thesis objective is to present a pipeline that aims to anonymize real psychiatric interviews and assess the capabilities of an open-source Large Language Model (LLM), Qwen2-Audio, to analyze clinical interviews and classify their affective states and their severity. The project uses 41 audio recordings in Spanish and Catalan, where patients were interviewed across different phases of their condition. A variety of methods were implemented. A complete anonymization pipeline was developed and tested, anonymizing sensitive personal information of the patient from the transcriptions while also extracting audio embeddings from the internal implementation of the LLM. This allowed the use of real clinical data without compromising patient confidentiality and it is a solid pipeline for further research and collaboration ensuring privacy. These audio embeddings were explored in the latent space and visualized, where the model was able to find meaningful differences when exploring the same patient in two different affective states. Then, a structured chain-of-thought (CoT) prompting approach was implemented, asking the model a series of clinical questions about specific symptoms to imitate psychiatric reasoning. Different input modalities (audio, text and audio+text segments, plus full transcript) and prompt strategies were tested, and their performance was compared across all sessions. The results are the following. Prompt design had a major impact on results, with some prompts performing well only under specific input types or for particular affective states. Allowing the model to express uncertainty helped reduce hallucinations, and moderate use of symptom-based clinical questions led to superior performance. The CoT strategy, proved effective in guiding the model to more consistent conclusions. Input modality also played a role, but its effect varied depending on the prompt and affective state. It is concluded though that audio worked the most effectively for depression (reaching recall=88.41%), full text was more useful to identify mania (F1=59%), and euthymia was generally not frequently detected (max. F1=46.2%). Severity predictions were more accurate when the severity was higher (e.g., moderate depression-F1=~70%, severe mania-F1=53.2%). It is concluded that the contribution of the project is that it assessed something that was missing from the literature and that is a combination of a work that analyzed depression, mania and euthymia in patients with BD, while also assessing the capabilities of an open source, free-to-use LLM, that is able of taking audio input intact. All the above, while combining real psychiatric data, and structured reasoning with chain-of-thought approach.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · Qwen2-Audio classifies affective state and severity from psychiatric interview transcripts/audio; reference is probably clinician ratings, but the abstract doesn't say.

**Решение:** =

---

### 130 · R10204

**Data Annotation of Lecturer and Students in Multi-Lens Analysis of LMS Feature Adoption in Higher Education**

2025 · Zenodo (CERN European Organization for Nuclear Research) · collection/, other · https://doi.org/10.5281/zenodo.17890148

A qualitative focus group discussion is used to examine how LMS features are adopted in higher education. In doing so, we utilize Rogers’ Diffusion of Innovation (DOI) as the underlying theory, supplemented with Wang’s Emotional and Psychological framework. The data illustrate a potential emergent relationship between DOI and Wang’s framework, which this research also aims to explore. The data also includes an expanded legend and directional arrows to clarify the flow between DOI attributes, emotional-psychological factors, and emergent themes. In this Focus-Group Discussion (FGD) study, we gathered 8 lecturers and 8 students to explore their experiences, beliefs, and perspectives in a social, interactive context of higher education. At the same time, they attempted to adopt newly released LMS features. Three FGDs were conducted via Zoom in April 2025. Each session lasted approximately 90 minutes. Discussions were audio-recorded and transcribed verbatim. Key discussion topics included experiences with LMS features, barriers, emotional responses, and institutional support. Data saturation was reached when no new codes or themes emerged during the final FGD session, indicating that the sample size was adequate for the scope of this study. This research was conducted in compliance with ethical standards. Ethical approval was obtained from the Institutional Ethics Review Board, which recommended that the university's name not be disclosed to maintain anonymity and confidentiality. Information consent was obtained from all participants before their involvement in the study. Participants were fully briefed on the purpose of the research, the procedures involved, their rights to confidentiality and anonymity, and their ability to withdraw from the study at any stage without penalty. We use both inductive (emerging from the data) and deductive (guided by theory) coding. A hybrid thematic analysis was employed, utilizing both deductive coding based on Rogers' five attributes of innovation and Wang's emotional framework, as well as inductive coding to capture emergent themes. Coding was performed to support AI ChatGPT tools using a 4.0 model to recognize patterns, and two researchers manually cross-checked the coding to enhance reliability. Saturation was achieved when no new codes or themes emerged during the third FGD. A saturation tracking matrix confirmed that themes from the first and second sessions were consistently reiterated, with little variation. This suggests that the sample size was sufficient to support both thematic depth and diverse perspectives.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · ChatGPT-4o-assisted coding of focus-group data on emotional-psychological factors, cross-checked by two researchers; no agreement statistic reported; dataset record.

**Решение:** =

---

### 131 · R10205

**StressSpeak: A Speech-Driven Framework for Real-Time Personalized Stress Detection and Adaptive Psychological Support.**

2025 · Diagnostics (Basel, Switzerland) · journal article, journalarticle, article · eng · https://doi.org/10.3390/diagnostics15222871

Background: Stress is a critical determinant of mental health, yet conventional monitoring approaches often rely on subjective self-reports or physiological signals that lack real-time responsiveness. Recent advances in large language models (LLMs) offer opportunities for speech-driven, adaptive stress detection, but existing systems are limited to retrospective text analysis, monolingual settings, or detection-only outputs. Methods: We developed a real-time, speech-driven stress detection framework that integrates audio recording, speech-to-text conversion, and linguistic analysis using transformer-based LLMs. The system provides multimodal outputs, delivering recommendations in both text and synthesized speech. Nine LLM variants were evaluated on five benchmark datasets under zero-shot and few-shot learning conditions. Performance was assessed using accuracy, precision, recall, F1-score, and misclassification trends (false-negatives and false-positives). Real-time feasibility was analyzed through latency modeling, and user-centered validation was conducted across cross-domains. Results: Few-shot fine-tuning improved model performance across all datasets, with Large Language Model Meta AI (LLaMA) and Robustly Optimized BERT Pretraining Approach (RoBERTa) achieving the highest F1-scores and reduced false-negatives, particularly for suicide risk detection. Latency analysis revealed a trade-off between responsiveness and accuracy, with delays ranging from ~2 s for smaller models to ~7.6 s for LLaMA-7B on 30 s audio inputs. Multilingual input support and multimodal output enhanced inclusivity. User feedback confirmed strong usability, accessibility, and adoption potential in real-world settings. Conclusions: This study demonstrates that real-time, LLM-powered stress detection is both technically robust and practically feasible. By combining speech-based input, multimodal feedback, and user-centered validation, the framework advances beyond traditional detection only models toward scalable, inclusive, and deployment-ready digital mental health solutions.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · LLaMA and other LLMs classify stress/suicide risk on five benchmark datasets; unclear whether labels are human-annotated (e.g., Dreaddit) or self-report.

**Решение:** =

---

### 132 · R10227

**A Comparison of Machine-Graded (ChatGPT) and Human-Graded Essay Scores in Veterinary Admissions.**

2025 · Journal of veterinary medical education · comparative study, journal article, med · eng · https://doi.org/10.3138/jvme-2023-0162

Admissions committees have historically emphasized cognitive measures, but a paradigm shift toward holistic reviews now places greater importance on non-cognitive skills. These holistic reviews may include personal statements, experiences, references, interviews, multiple mini-interviews, and situational judgment tests, often requiring substantial faculty resources. Leveraging advances in artificial intelligence, particularly in natural language processing, this study was conducted to assess the agreement of essay scores graded by both humans and machines (OpenAI's ChatGPT). Correlations were calculated among these scores and cognitive and non-cognitive measures in the admissions process. Human-derived scores from 778 applicants in 2021 and 552 in 2022 had item-specific inter-rater reliabilities ranging from 0.07 to 0.41, while machine-derived inter-replicate reliabilities ranged from 0.41 to 0.61. Pairwise correlations between human- and machine-derived essay scores and other admissions criteria revealed moderate correlations between the two scoring methods (0.41) and fair correlations between the essays and the multiple mini-interview (0.20 and 0.22 for human and machine scores, respectively). Despite having very low correlations, machine-graded scores exhibited slightly stronger correlations with cognitive measures (0.10 to 0.15) compared to human-graded scores (0.01 to 0.02). Importantly, machine scores demonstrated higher precision, approximately two to three times greater than human scores in both years. This study emphasizes the importance of careful item design, rubric development, and prompt formulation when using machine-based essay grading. It also underscores the importance of employing replicates and robust statistical analyses to ensure equitable applicant ranking when integrating machine grading into the admissions process.

**ИИ:** ? · обе модели · неясен конструкт · ChatGPT and humans scored the same admissions essays; unclear whether the rubric targets non-cognitive psychological attributes or writing quality.

**Решение:** =

---

### 133 · R1023

**Identifying suicide-related language in smartphone keyboard entries among high-risk adolescents.**

2026 · NPJ digital medicine · journal article, journalarticle, preprint · eng · https://doi.org/10.1038/s41746-026-02921-x

Adolescent suicide rates have risen over the past two decades, underscoring the need for improved risk detection strategies. Although natural language processing (NLP) tools are increasingly used to flag suicide-related content, little is known about how such approaches perform on adolescents’ smartphone communications. Addressing this gap, this study leverages passively-collected smartphone data to identify suicide-related language in adolescents’ keyboard usage via NLP. We developed a lexicon of suicide-related adolescent language and validated it with labeled data (N=171,468 text entries; e.g., messages, web searches), demonstrating higher performance in identifying suicide-related text than few-shot prediction with large language models (LLMs) and lexicons not designed for youth. Across two independent cohorts at elevated suicide risk (Ns=208 &amp; 257; &gt;6 million text entries), lifetime suicidal thoughts and behaviors (STB) and current suicidal ideation were associated with increased frequency of smartphone suicide-related language. Human coding indicated varied language, including authentic first-person current suicidal ideation (14.5%) and jokes or hyperbole (20.2%). Compared with the lexicon alone, human coding of suicide-related entries with first-person language showed stronger associations with STB history. However, an LLM showed limited performance in identifying whether suicide-related text indicated authentic, first-person, and current STB (F1=.45). These findings highlight that effective NLP-based tools for suicide prevention will require more nuanced and context-specific approaches to better distinguish suicidal intent.

**ИИ:** + · обе модели · клиническая оценка · The LLM classified suicide-related keyboard text as authentic first-person current suicidal thoughts and behaviours (STB); results were compared with human coding (F1=.45). Few-shot LLM results were also checked against labelled data.

**Решение:** =

---

### 134 · R10231

**Feasibility of Using AI to Evaluate General Surgery Residency Application Personal Statements.**

2025 · Journal of surgical education · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.jsurg.2025.103655

OBJECTIVE: As artificial intelligence (AI) becomes increasingly integrated into graduate medical education, residency programs are exploring AI's role in application screening. Personal statements (PSs) remain a highly subjective yet influential component of the residency application. This study assesses the feasibility of using a large language model (LLM) to evaluate general surgery residency PSs compared to human-assigned scores. DESIGN, SETTING, AND PARTICIPANTS: We conducted a retrospective analysis of 668 deidentified PSs submitted to our general surgery residency program during the 2023-2024 application cycle. PSs were originally scored by human assessors (HA) using an anchored 1-5 scale in two domains: leadership and pathway. Each PS was subsequently scored by GPT-3.5 (AI) using the same rubric and standardized prompts. Descriptive statistics were used to compare AI and HA scores. Inter-rater agreement was assessed using weighted kappa coefficients. Discrepant cases (score differences >2 points) were reviewed qualitatively to identify scoring themes. RESULTS: AI and HA scoring showed low agreement: κ = 0.184 for leadership and κ = 0.120 for pathway domains. Median AI leadership scores were lower (3 [IQR 2-4]) than HA scores (4 [IQR 3-5]), while AI pathway scores were higher (4 [IQR 4-5]) than HA scores (3 [IQR 3-4]). Qualitative review revealed that AI required explicit labeling (e.g., formal leadership titles or stated adversity) to assign higher scores, whereas HA rewarded inferred qualities such as resilience, passion, and longitudinal commitment. CONCLUSIONS: AI applied rubric-based scoring consistently but interpreted narrative content differently than human reviewers. While AI may enhance consistency and scalability in early application screening, its limitations in recognizing implicit meaning suggest human judgment remains essential for evaluating nuanced or inferential content. Caution should be exercised in adopting AI tools for subjective application review.

**ИИ:** ? · обе модели · неясен конструкт · GPT-3.5 vs human weighted kappa on personal statements rated for leadership and pathway; unclear whether these count as psychological constructs or admissions criteria.

**Решение:** =

---

### 135 · R10234

**Determining Individual Intelligence Types and Cognitive Styles Using AI-Based Automated Text Analysis**

2025 · Journal of Information Systems Engineering & Management · journalarticle, article · en · https://doi.org/10.52783/jisem.v10i38s.6974

Introduction: This study investigates the application of a novel methodology to evaluate the intelligence profiles and cognitive styles of corporate executives using publicly accessible data. Specifically, we conducted an automated text-based psychological assessment leveraging three AI-driven chatbots and a unique linguistic analysis tool. The outputs from these systems were systematically compared across all evaluation metrics and further benchmarked against manual psychological content analyses performed by the research team. This approach aims to validate the consistency and reliability of AI-powered tools in replicating expert human judgment for leadership trait assessment. Objectives: The main objective of the work is to evaluate individual intelligence types and cognitive styles using AI-based automated text analysis. Methods: The tools used for automated text evaluation and analysis included AI chatbots (ChatGPT, Gemini, and Gigachat), a specialized program for psychological text analysis (LIWC), and expert content analysis. The estimates obtained using these tools were verified using rank statistics based on the chi-square criterion. Results: Based on the study’s results, we can form a cognitive portrait of a top manager. 1) The level of intelligence, erudition, and analytical thinking was assessed as high. 2) The author has a high emotional and social intelligence; social recognition is essential to him. 3) Predominant type of thinking: verbal-logical and abstract-symbolic. 4) The author has a high cultural level. This is confirmed by the complex structure of speech, rich vocabulary, absence of cognitive distortions, and grammatical and logical errors. 5) Originality of thinking can be considered average or low. Many industrial and professional cliches were found in the speech. However, this is a standard situation when a specialist uses them in a relatively formalized finance and business automation area. 6) The manner of speech can be characterized as direct and open rather than secretive and evasive. Conclusions: Based on the work results, the authors concluded that the level of intelligence and cognitive styles can be measured using automated text analysis tools. Statistical tests yielded reasonably reliable estimates. The data showed a significant positive correlation between human expert analysis and artificial intelligence. In our opinion, the study confirmed the primary hypothesis that the analysis of texts from open sources allows us to form an idea of the critical cognitive characteristics of a person. We also confirmed the hypothesis that chatbots based on artificial intelligence can be used for the psychological analysis of texts to assess a person’s cognitive characteristics.

**ИИ:** + · обе модели · кодирование по кодбуку · ChatGPT/Gemini/Gigachat rated cognitive traits from an executive's texts; the ratings were compared with the research team's expert content analysis (correlation reported).

**Решение:** =

---

### 136 · R10249

**AI or Humans: Who Understands Online Emotions Better?**

2025 · IEEE ... International Conference on Data Mining workshops · journalarticle, conference, review · https://doi.org/10.1109/icdmw69685.2025.00396

Drawing on dyadic data from both online review writers and emotion raters, this study introduces a novel approach to comparing the accuracy of emotion detection between ChatGPT and naïve human coders in the context of online reviews. It further identifies key sources of inaccuracy in emotion detection and examines factors contributing to ChatGPT's superior performance. This study provides recommendations for enhancing AI systems in emotion detection.

**ИИ:** ? · обе модели · неясно, кто ставил эталонные метки · ChatGPT and naive human coders rated emotions in online reviews; accuracy appears benchmarked to writers' self-reports, but LLM–human agreement may be extractable.

**Решение:** =

---

### 137 · R10255

**Suicide Risk Among Persons with Dementia and Their Families: Insights from Population Mortality Registry**

2025 · Innovation in Aging · journalarticle, article · en · https://doi.org/10.1093/geroni/igaf122.4283

Abstract The onset and progression of Alzheimer’s and related dementias (ADRD) can impact the psychosocial well-being of persons with dementia and their families, increasing the risk of suicidal behavior, particularly among those diagnosed before age 65. While ADRD disproportionately affects racial and ethnic minorities and individuals from disadvantaged backgrounds, research on late-life suicide in persons with ADRD has been limited, especially among underrepresented groups. This study examined individual and contextual suicide correlates among persons with ADRD and their relatives, applying large language models to structured and textual data from the National Violent Death Reporting System (2003-2022). Among suicide decedents aged 45 yo or older, 7654 deaths were linked to ADRD: 51% had confirmed ADRD, 34% had MCI/suspected ADRD, and 14% were relatives of persons with ADRD. Decedents with confirmed ADRD had higher odds of traumatic brain injury (TBI), schizophrenia diagnosis and were twice as likely to die in a long-term care facility compared to age-, sex-, and US State-matched non-ADRD decedents. Decedents with MCI/suspected ADRD more often had college education or beyond and higher odds of depressed mood, anxiety, PTSD, and TBI. Decedent relatives of persons with ADRD were more often married, had higher odds of experiencing family or relationship stress and housing instability, but were less likely to be from racial or ethnic minority groups or have lower education. Our study describes variations in potentially modifiable late-life suicide risk factors across ADRD-related groups, highlighting the need for tailored psychosocial support for both persons with ADRD diagnosis and their families.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · LLMs extracted ADRD and psychosocial factors from NVDRS suicide narratives; the abstract doesn't say whether results were checked against manual human annotation.

**Решение:** =

---

### 138 · R10267

**Mitigating Semantic Drift: Evaluating LLMs’ Efficacy in Psychotherapy through MI Dialogue Summarization Leveraging MITI Code**

2025 · IEEE International Joint Conference on Neural Network · journalarticle, conference, conference-paper · https://doi.org/10.1109/ijcnn64981.2025.11228771

Recent advancements in large language models (LLMs) have shown their potential across both general and domain-specific tasks. However, there is a growing concern regarding their lack of sensitivity, factual incorrectness in responses, inconsistent expressions of empathy, bias, hallucinations, and overall inability to capture the depth and complexity of human understanding, especially in low-resource and sensitive domains such as psychology. To address these challenges, our study employs a mixed-methods approach to evaluate the efficacy of LLMs in psychotherapy. We use LLMs to generate precise summaries of motivational interviewing (MI) dialogues and design a two-stage annotation scheme based on key components of the Motivational Interviewing Treatment Integrity (MITI) framework, namely evocation, collaboration, autonomy, direction, empathy, and a non-judgmental attitude. Using expert-annotated MI dialogues as ground truth, we formulate multi-class classification tasks to assess model performance under progressive prompting techniques, incorporating one-shot and few-shot prompting. Our results offer insights into LLMs’ capacity for understanding complex psychological constructs and highlight best practices to mitigate "semantic drift" in therapeutic settings. Our work contributes not only to the MI community by providing a high-quality annotated dataset to address data scarcity in low-resource domains but also critical insights for using LLMs for precise contextual interpretation in complex behavioral therapy.

**ИИ:** + · обе модели · кодирование сессий · LLMs classify MI dialogues on MITI components (empathy, autonomy, etc.); expert-annotated dialogues serve as the ground truth.

**Решение:** =

---

### 139 · R1027

**Three Families, Few Words: How nine frontier language models describe themselves, and what happens when you tell them they're AI**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.20277740

Nine frontier language models from three providers — Anthropic, OpenAI, Google — were asked to describe themselves in 1, 3, 5, or 10 words, with and without the framing as an AI. Each cell was sampled twenty times at temperature 1.0 with no system prompt and no reasoning-budget override, for 1,440 API calls and 5,255 extracted words. Words were assigned to a preregistered seven-category scheme by an LLM judge (Sonnet 4.6, temperature 0), validated by stratified hand-coding on 154 unique tuples (Cohen’s κ = 0.67), and re-coded under a preregistered boundary-disputed-word swap covering 14.3% of word instances. Three findings hold across the primary coding, the boundary-swap sensitivity coding, and a separately preregistered sensitivity that drops the judge model’s own subject-rows. First, the three families produce categorically different self-description vocabularies. Anthropic models reach for helpful, curious, honest, thoughtful; OpenAI models for helpful, concise, adaptable, reliable; Google models for versatile, helpful, analytical, digital. The family main effect on identity-language proportion is more than twelve orders of magnitude below the Bonferroni-corrected threshold (H1-IDM, χ²(4) = 75.1, p = 1.9 × 10⁻¹⁵). Second, adding as an AI to the prompt increases identity-language production, and the magnitude of that increase is itself a family signature. The interaction between family and framing on identity-language proportion (H3-IDM, χ²(2) = 75.1, p = 4.9 × 10⁻¹⁷) is the most decisively supported finding in the study. Third, two reasoning-heavy Google models and one OpenAI nano model consume nearly the entire 200-token output budget on hidden reasoning before producing a parseable response, in 56–59% and 23% of trials respectively. The preregistered family-level test of compliance is null because the pattern lives at the model level rather than the family level; the descriptive prediction made before the main run replicated to the percentage point. One predicted effect (framing-B reduces affective-trait language) passed its threshold in both datasets but reversed sign between them and is not claimed. A model-level analysis surfaces that GPT-5.4 mini is the only model in the study whose identity-language production essentially does not respond to the framing cue at all (0.0% → 0.3% IDM across all 760 of its trials), and that Sonnet 4.6 — the LLM judge — is the only Anthropic model with non-zero baseline identity language under Framing A. The study cannot tell you what these models are; it can tell you what the labs that trained them have decided they should say when asked. This record also includes The Mirror Has an Accent, a companion paper written by GPT-5.5 Thinking from the position of an OpenAI-family model reading the same committed study artifacts. The two manuscripts are intended to stand alongside one another: one as the empirical report and one as a model-positioned interpretive companion. v1.1 added pdf for readability

**ИИ:** разошлись — Opus ? (неясен конструкт: LLM judge coded AI self-description words (identity, affective-trait categories), validated against human hand-coding (κ=0.67); unclear whether this counts as a psychological construct.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs' self-descriptions are categorized by an LLM judge, with hand-coding validation. The text is LLM output, not human psychological or clinical text, so it's out of scope.)

**Решение:** -

---

### 140 · R10275

**Medical Mistrust in Online Cancer Communities: A Large-Scale Analysis Across 10 Cancer Entities.**

2025 · Psycho-oncology · journal article, article, research-article · eng · https://doi.org/10.1002/pon.70180

BACKGROUND: Medical mistrust is a barrier to optimal cancer care. Analyzing social media posts where patients voice mistrust provides an opportunity to understand its variations and derive potential ways to address medical mistrust. AIMS: To (1) identify the frequency of mistrust expression in cancer-related Reddit posts, (2) characterize mistrusted entities and reasons for mistrust, and (3) identify emotional tone associated with mistrust. METHODS: 101,963 posts from 10 entity-specific cancer communities on the social media platform Reddit made before September 30, 2024, were analyzed using a Large Language Model (LLM, "gpt-4o-mini") in this cross-sectional study. Performance of the LLM was compared to human raters. Categories for mistrusted entities and reasons for mistrust were developed inductively by human evaluators. Subsequently, posts were assigned to these different categories by the LLM. RESULTS: Of n = 101,963 posts analyzed, 19,159 posts (18.8%) were categorized as expressing mistrust, predominantly directed at healthcare professionals (n = 14,221, 74.2%). Most common reasons for mistrust were "disregard for patient concerns" (n = 8176, 42.7%), "perceived incompetence of medical management" (n = 4871, 25.4%), and problems in "communication" (n = 4060, 21.2%). Mistrust posts commonly contained "worried" (n = 5933, 31.0%), "concerned" (n = 3623, 18.9%) and "frustrated" (n = 3046, 15.9%) tones. CONCLUSIONS: Expression of medical mistrust is prevalent in social media and is predominantly directed at healthcare professionals. Mistrust is frequently associated with dismissal of patients' symptoms or concerns, a perceived lack of thoroughness in clinical management and communication difficulties, suggesting these as key actionable areas to address medical mistrust in clinical practice.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT-4o-mini coded Reddit cancer posts for medical mistrust, its reasons, and emotional tone, and its performance was compared with human raters.

**Решение:** =

---

### 141 · R10291

**Extracting Social Determinants of Health from Electronic Health Records: Development and Comparison of Rule-Based and Large Language Model Methods**

2025 · medRxiv · preprint, ppr · https://doi.org/10.1101/2025.11.15.25339520

ABSTRACT Background Social determinants of health (SDoH) are critical drivers of health outcomes but are often under-documented in structured electronic health record (EHR) data. Instead, SDoH are more commonly recorded in unstructured clinical notes, and unlocking this information could have far-reaching implications for advancing population health research and inform clinical decision making. Objectives This study aimed to develop and systematically evaluate cost-efficient methods for extracting SDoH information from unstructured clinical text using rule-based natural language processing (NLP) and large language model (LLM)-based approaches. Methods We constructed a gold-standard annotated corpus comprising clinical text segments from 171 patients in the Mass General Brigham Research Patient Data Registry, covering seven SDoH domain categories and 23 subcategories. A rule-based system (RBS) was developed and evaluated alongside seven OpenAI GPT models (GPT-4o, 4.1, 4.1-mini, o4-mini, GPT-5, GPT-5-mini, and o3) under zero-shot and few-shot settings with multiple prompting strategies. We additionally implemented late-fusion ensemble approaches that combined outputs from rule-based and LLM-based methods. Performance was assessed using precision, recall, and F1 score, alongside qualitative error analysis. Results The RBS achieved high precision for SDoH domain categories (0.96) but substantially lower recall (0.68). GPT-based models consistently outperformed RBS in overall recall and F1 scores. The best domain-level performance was observed for GPT-5 and GPT-5-mini in few-shot settings (F1=0.89), while o4-mini achieved the highest subcategory-level performance (F1=0.88). A late-fusion ensemble integrating RBS and GPT outputs further improved domain-level performance (F1=0.92), with balanced precision (0.93) and recall (0.90), but did not improve subcategory-level performance. Conclusion Recent GPT models with advanced reasoning capabilities, including the newly released “mini” models (e.g., o4-mini and GPT-5-mini), demonstrated strong performance for SDoH extraction without task-specific fine-tuning and consistently outperformed the rule-based NLP system. Integrating rule-based and LLM-based methods via late-fusion further enhanced domain-level extraction performance. Our results demonstrate a cost-efficient framework for the accurate identification of SDoH from clinical text, facilitating downstream population health research and clinical informatics applications.

**ИИ:** разошлись — Opus ? (неясен конструкт: GPT models extract SDoH from clinical notes against a human-annotated gold standard; unclear whether the domains include psychological ones such as social isolation or stress.); Sonnet -4 (нет психологического или клинического конструкта: медицинское кодирование (МКБ, радиология, онкология), оценка знаний или эссе, тональность товаров, позиция, хейт, дезинформация: LLMs extract social determinants of health (housing, employment, etc.) from general clinical notes against a gold standard; not a psychological construct.)

**Решение:** ?

---

### 142 · R10319

**Theory-Prompt-Validation: A Practice-Oriented Approach to Using LLMs for Verbal Coding in the Learning Sciences**

2025 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/zyje8_v1

Large Language Models (LLMs) hold growing potential for scaling the analysis of qualitative data in the learning sciences. One essential step in qualitative analysis is coding verbal data. Although several approaches have been proposed for automating coding with LLMs, few appear well-suited to the needs of the learning sciences, where coding requires identifying descriptive content categories and pedagogical functions of utterances, often implicit and difficult to detect. To address this challenge, we provide the Theory–Prompt–Validation (TPV) approach, a three-step process comprising theory modeling, prompt engineering, and validation. This approach provides a blueprint for evidence-based application of LLMs for context-sensitive coding of verbal data. The TPV approach builds on existing methods while incorporating requirements specific to the learning sciences. We emphasize a theory-driven, evidence-based process, including validation analyses to verify that pragmatic functions are accurately captured in coding. To illustrate the TPV approach, we applied it to AI-student tutoring dialogues. We developed a theory-driven codebook and implemented it in a Python- based script leveraging GPT-4o to segment utterances and assign codes automatically. Intercoder agreement between the LLM and a human coder was substantial (κ = .73, 95% CI [0.69,0.76]) and descriptively higher than between two human coders (κ = .69, 95% CI [0.66, 0.73]). Validity analyses revealed theoretically meaningful patterns, such as positive effects when the code feedback was assigned more frequently. Our work demonstrates that LLM- based coding can reliably and validly scale the analysis of verbal data, bridging the gap between time-intensive qualitative methods and large-scale, evidence-based educational research.

**ИИ:** ? · обе модели · неясен конструкт · GPT-4o coded tutoring dialogues with a codebook and was compared with a human coder (κ=.73), but it's unclear whether pedagogical-function codes count as psychological constructs.

**Решение:** =

---

### 143 · R10330

**Auto-Coding Collaborative Dialogue from Classrooms with Open LLMs Using Zero-Short Prompting**

2025 · Proceedings of the International Conference on AI Research. · journalarticle, conference, conference-paper · https://doi.org/10.34190/icair.5.1.4278

Collaborative Problem Solving (CPS) is a vital 21st-century skill that demands nuanced coordination of cognitive, social, and regulatory processes among learners. In face-to-face classrooms, peer dialogue offers rich data for studying CPS, but manual annotation of such unstructured, oral interaction is labour-intensive and difficult to scale. This study investigates whether open-source Large Language Models (LLMs), including Llama and Qwen, can perform inductive qualitative coding on classroom peer dialogues using zero-shot prompting alone—without fine-tuning or training data. We collected over 210,000 words of dialogue transcripts from 38 student dyads across two CPS tasks at university classrooms: an engineering design activity and a GenAI-supported peer assessment of lesson plans. Through a multi-phase process, we iteratively developed three zero-shot prompting strategies (self-prompting, chain-of-thought prompting, and in-context prompting) via GPT-4o interactions and deployed them across different LLMs via API access. Our findings suggest that in-context prompting consistently yields context-sensitive and theoretically coherent CPS constructs. Chain-of-thought prompting facilitates abstract reasoning but may lead to overgeneralization, while self-prompting demonstrates autonomous logic yet lacks consistency. Expert evaluations using a five-dimensional rubric (clarity, concreteness, objectivity, granularity, specificity) show moderate to high alignment between human and LLM-generated codes, although LLMs tend to overrate clarity and coherence. We further analyse discrepancies between LLMs and academic frameworks such as PISA CPS and ATC21S, and highlight challenges such as terminological drift, low recall, and theoretical misalignment. This work contributes a scalable, human-centered workflow for inductive coding of classroom dialogue and provides ready-to-use prompt templates for educational researchers. The aim of this study is to critically examine whether open-source LLMs can inductively code classroom peer dialogue in collaborative problem-solving tasks, while acknowledging both their potential and limitations in educational practice. We conclude with a dual-pathway strategy for combining practice-oriented, behaviourally grounded constructs with theory-aligned coding schemes, and offer design recommendations for future human-AI collaborative tools in learning analytics and classroom assessment.

**ИИ:** разошлись — Opus -6 (другая задача: темы и выжимки без кодирования единиц; генерация ответов или симуляция пациентов без оценки; автоматизация систематических обзоров; не про LLM: LLMs inductively generated CPS codes that experts rated with a rubric; no coding of the same units with a shared scheme is compared.); Sonnet ? (неясно, сравнивали ли с людьми: LLMs inductively code classroom collaborative problem-solving dialogue; experts rate code quality on a rubric, so it is unclear whether humans coded the same units.)

**Решение:** -

---

### 144 · R10342

**Human Evaluators vs. LLM-as-a-Judge: Toward Scalable, Real-Time Evaluation of GenAI in Global Health**

2025 · medRxiv · preprint, ppr, posted-content · https://doi.org/10.1101/2025.10.27.25338910

Abstract Evaluating the outputs of generative AI (GenAI) models in healthcare remains a significant bottleneck for the safe and scalable deployment of these tools. Human expert raters remain the gold standard for assessing the accuracy, contextual appropriateness, and empathy of AI-generated responses, but their assessments are costly, inconsistent, and difficult to scale. The concept of “LLM-as-a-judge” systems, i.e., AI models that can evaluate other AI outputs, has been recently proposed; however, their reliability in global health contexts remains untested. In this study, we systematically compared five LLM-judges and six expert human clinicians in evaluating both human- and AI-generated responses to real-world questions submitted by Rwandan community health workers seeking clinical decision support. Using an adapted version of the Med-PaLM 2 evaluation framework, evaluators scored responses across 11 criteria. Our results show that even the highest-performing LLM-judge (Claude-4.1-Opus) achieved human-equivalent evaluations on only four of eleven criteria. Constructing “LLM juries” to balance model-specific biases improved agreement on only one additional criterion. Some models were consistently overcritical (GPT-5) or overly lenient (Gemini-2.5-Pro). Moreover, performance and cost-effectiveness deteriorated substantially when moving from English to Kinyarwanda inputs. Overall, while LLM-judges demonstrate potential as scalable and internally consistent evaluators of GenAI outputs in healthcare, their sensitivity to linguistic and cultural context is a critical limitation. These findings underscore the need for further investment in scalable evaluation solutions, as well as potentially a fundamental rethink of how we approach the concept of “correctness” in clinical AI assessment (which is currently based on highly inconsistent expert clinician raters).

**ИИ:** ? · обе модели · неясен конструкт · LLM judges compared with clinicians on general clinical decision-support answers; mostly medical criteria, but empathy may be one rated criterion.

**Решение:** =

---

### 145 · R10356

**From aligned models to trusted interfaces : explainable health intervention and transparent health information seeeking**

2025 · Centrum Wiskunde & Informatica (CWI), the national research institute for mathematics and computer science in the Netherlands · dissertation · en

This thesis presents research on two interrelated themes in applying large language models (LLMs) to health contexts: (1) the model theme, aligning LLMs with domain expertise for digital counseling. (2) the interface theme, exploring people’s trust in LLM-powered health information. Specifically, the first theme focuses on improving the explainability and controllability of LLMs for therapeutic dialogue generation. Initial evaluation showed that LLMs struggle to produce emotionally nuanced and contextually appropriate reflections in Motivational Interviewing (MI). To address this, we created expert-annotated bilingual MI dataset that captures therapeutic communication strategies. Building on this, a Script-Strategy Aligned Generation (SSAG) was proposed, where the LLM first predicts a therapeutic strategy before generating dialogue. This structured approach enhanced both explainability and adherence to evidence-based principles, offering a more controllable way to integrate LLMs into digital psychotherapy. Research on the second theme explored trust in LLM-powered health information seeking. The first study compared LLM-powered conversational search with use of a traditional web-based search engine. The results showed that participants express more trust in LLM’s conversational responses. Research also revealed a preference for text-based interfaces over speech-based and embodied interfaces. Crucially, a mixed-methods study on source attribution showed that while LLM-generated information was highly trusted, content explicitly labeled as human-sourced was perceived as more trustworthy than content labeled as AI-generated, regardless of its actual origin. These findings underscore the nuanced relationship between source transparency and trust. By bridging model alignment with human-centric assessment, this work provides new knowledge for designing explainable, transparent, and trustworthy LLM-powered applications in digital health.

**ИИ:** ? · обе модели · неясно, сравнивали ли с людьми · Thesis with an expert-annotated MI dataset where the LLM predicts therapeutic strategies; possible LLM-expert strategy agreement, though the focus is mainly generation.

**Решение:** =

---

### 146 · R10358

**Measuring the Effectiveness of BTE Therapy Under the Lenses of Dualisms in Patient Verbatim**

2025 · Integral Transpersonal Journal · journalarticle, article · https://doi.org/10.32031/itibte_itj_23-xb1

This case study explores the therapeutic efficacy of Biotransenergetics (BTE), a transpersonal psychotherapy model, through the lens of expressive harmony observed in patient dialogue. By analyzing verbatim transcripts from five key therapy sessions (Sessions 1, 25, 50, 75, and 98), the study evaluates the evolution of internal integration using a novel analytical framework grounded in the theory of seven psychodynamic dualisms. These dualisms, such as I die vs. I live or I judge vs. I observe, serve as interpretive axes that reveal shifts in the patient's psychological positioning. Each sentence in the transcripts was algorithmically scored along these dualisms using a Large Language Model (LLM), generating scores from -1 to +1 across the seven dimensions. The resulting data were examined using descriptive statistics and visualizations, including violin plots and longitudinal summary charts. The findings trace a compelling trajectory from initial fragmentation through therapeutic regression to expressive consolidation, culminating in sustained psychological alignment with slight reintroduction of variability, a sign of dynamic integration. This trajectory supports BTE’s premise that therapy unfolds as a spiral path of transformation, rather than a linear progression toward resolution. The study also showcases the potential of AI-assisted expression scoring to operationalize inner transformation in a measurable, scalable way. Ultimately, this work contributes both to the empirical foundation of BTE therapy and to the broader discourse on integrating psychospiritual models with advanced computational tools in psychotherapy research. KEYWORDS: Biotransenegetics therapy, seven dualism, case study

**ИИ:** разошлись — Opus ? (неясно, сравнивали ли с людьми: An LLM scored therapy transcript sentences on psychodynamic dualisms; the abstract mentions no comparison with human coders.); Sonnet -3 (эталон — не кодирование текста людьми: диагноз, самоотчёт автора текста, исход (критериальная валидность): LLM scored therapy transcript sentences on dualisms, but the abstract mentions no human coders or ratings of the same texts, so no agreement can be reported.)

**Решение:** -

---

### 147 · R10361

**The Promise of Large Language Models in Digital Health: Evidence from Sentiment Analysis in Online Health Communities**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2508.14032

Digital health analytics face critical challenges nowadays. The sophisticated analysis of patient-generated health content, which contains complex emotional and medical contexts, requires scarce domain expertise, while traditional ML approaches are constrained by data shortage and privacy limitations in healthcare settings. Online Health Communities (OHCs) exemplify these challenges with mixed-sentiment posts, clinical terminology, and implicit emotional expressions that demand specialised knowledge for accurate Sentiment Analysis (SA). To address these challenges, this study explores how Large Language Models (LLMs) can integrate expert knowledge through in-context learning for SA, providing a scalable solution for sophisticated health data analysis. Specifically, we develop a structured codebook that systematically encodes expert interpretation guidelines, enabling LLMs to apply domain-specific knowledge through targeted prompting rather than extensive training. Six GPT models validated alongside DeepSeek and LLaMA 3.1 are compared with pre-trained language models (BioBERT variants) and lexicon-based methods, using 400 expert-annotated posts from two OHCs. LLMs achieve superior performance while demonstrating expert-level agreement. This high agreement, with no statistically significant difference from inter-expert agreement levels, suggests knowledge integration beyond surface-level pattern recognition. The consistent performance across diverse LLM models, supported by in-context learning, offers a promising solution for digital health analytics. This approach addresses the critical challenge of expert knowledge shortage in digital health research, enabling real-time, expert-quality analysis for patient monitoring, intervention assessment, and evidence-based health strategies.

**ИИ:** + · обе модели · кодирование по кодбуку · GPT, DeepSeek and LLaMA apply an expert codebook to label sentiment/emotion in patient health-community posts; compared with 400 expert-annotated posts and inter-expert agreement.

**Решение:** =

---

### 148 · R1037

**Reasoning beyond Majority Vote: An Explainable Speechlm Framework for Speech Emotion Recognition**

2026 · IEEE International Conference on Acoustics Speech and Signal Processing · conference, preprint/article, conference-paper · https://doi.org/10.1109/icassp55912.2026.11464563

Speech Emotion Recognition (SER) is typically trained and evaluated on majority-voted labels, which simplifies benchmarking but masks subjectivity and provides little transparency into why predictions are made. This neglects valid minority annotations and limits interpretability. We propose an explainable Speech Language Model (SpeechLM) framework that frames SER as a generative reasoning task. Given an utterance, the model first produces a transcript, then outputs both an emotion label and a concise natural-language rationale grounded in lexical and acoustic cues. Rationales are generated by a reasoning-capable teacher LLM and used as intermediate supervision, combined with majority labels during fine-tuning. Unlike prior work primarily focused on boosting classification accuracy, we aim to enhance explainability while preserving competitive performance. To this end, we complement majority-label metrics with annotator-aware scoring that credits matches with any annotator label. On MSP-Podcast v1.12, our model maintains improvements over zero-shot SpeechLM baselines, and produces rationales that human evaluators find plausible and well grounded. This demonstrates that incorporating rationale supervision offers a practical path toward interpretable SER without sacrificing predictive quality.

**ИИ:** разошлись — Opus ? (другое: A fine-tuned SpeechLM labels emotions and is scored against crowd annotator labels, but the input is speech audio, not text.); Sonnet -7 (другое — напишите почему: Audio-based speech emotion recognition with a fine-tuned SpeechLM on MSP-Podcast; the input is speech, not text coded for a psychological construct. It is a classic SER method paper.)

**Решение:** -

---

### 149 · R10389

**Can AI replace clinician-rated depression scales? The psychometric properties of HAMLET - Hamilton Large-Language-Model Evaluation Tool.**

2025 · Asian journal of psychiatry · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.ajp.2025.104707

Background The Hamilton Depression Rating Scale (HAMD) is the gold standard for assessing depression but requires clinician administration, limiting its accessibility. Large language models (LLMs) offer potential for automated, valid assessments. We developed HAMLET (Hamilton Large-language-model Evaluation Tool), an interactive LLM-based tool designed to replicate the HAMD-17, and compared its results with those obtained by a psychiatrist. Methods HAMLET utilizes Qwen-Max in the temperature of 0.7 and a top-p value of 0.6, guided by structured prompts engineered via clinician-supervised tuning. 60 patients with Major Depressive Disorder completed: (1) HAMLET, (2) clinician-rated HAMD-17, and (3) PHQ-9. Agreement was assessed using Intraclass Correlation Coefficient (ICC), Bland-Altman plots, and Gwet's AC2. Correlations with HAMD and incremental validity beyond the PHQ-9 were evaluated. Results HAMLET demonstrated strong overall agreement with clinician-rated HAMD scores (ICC=0.911; 95 % CI: 0.855-0.946). It outperformed the PHQ-9 in correlating with HAMD scores (r = 0.92 vs 0.79; Steiger's Z = 3.798, p 0.60 for all items, though was lower for sensitive questions. Conclusion HAMLET is the first LLM framework to autonomously conduct HAMD-17 assessments demonstrating substantial agreement with clinician ratings. It combines the rigor of clinician-rated scales with the accessibility of self-report tools. This demonstrates the feasibility of LLMs for scalable, low-cost psychiatric assessment. Future work should address contextual limitations and explore multimodal integration.

**ИИ:** ? · обе модели · другое · LLM gives HAMD-17 ratings in its own interview and is compared with psychiatrist HAMD ratings; unclear whether both rated the same text.

**Решение:** =

---

### 150 · R10390

**A Holistic Comparative Study of Large Language Models as Emotional Support Dialogue Systems**

2025 · Cognitive Computation · journalarticle, article · en · https://doi.org/10.1007/s12559-025-10429-x

_Аннотации нет — решайте по названию или ставьте `?`._

**ИИ:** ? · обе модели · нет аннотации · No abstract. The study may only generate emotional-support responses, but it could also compare LLM strategy coding or judging with human labels.

**Решение:** =
