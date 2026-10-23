# Калибровка вслепую, часть 2

Калибровка вслепую, часть 2: записи 151–300 из 400. Это случайные 400 записей из 6852 в списке к отбору финального поиска 2026-10-21 (зерно 20261022, порядок случайный). **Меток ИИ здесь нет.** Размечайте в любом порядке и в несколько заходов. Когда закончите все части, скажите: я проверю, что всё размечено, и закоммичу файлы до того, как открою метки ИИ.

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

### 151 · R1478

**Council of Models: How Karpathy Built AI Peer Review**

2026 · Zenodo (CERN European Organization for Nuclear Research) · audiovisual/, other · en · https://doi.org/10.5281/zenodo.19538011

Episode summary: In November, Andrej Karpathy released llm-council, a deceptively simple system that treats language models like an academic council: four frontier models answer questions independently, then anonymously rank each other's responses, and a Chairman model synthesizes the results. The architecture packs deliberate design choices into just 800 lines of code—including a clever anonymization scheme, graceful error handling, and a multi-stage protocol that mirrors human expert panels. But does it actually achieve consensus, or just create a veneer of objectivity? This episode digs into the architecture, the limitations, and what it reveals about how language models evaluate each other. Show Notes # The Architecture of AI Peer Review: Inside Karpathy's llm-council In November, Andrej Karpathy released a GitHub repository called llm-council—described casually as a "vibe coded Saturday hack"—that has since accumulated nearly 17,000 stars. Despite its humble origin story, the codebase reveals a sophisticated mental model about how multiple language models should collaborate. ## What the Council Does The system is elegantly simple to describe: you ask a question, four frontier models (GPT-5.1, Gemini-3 Pro Preview, Claude Sonnet 4.5, and Grok-4) answer it independently, each model then anonymously peer-reviews the other three answers and ranks them, and finally a designated Chairman model reads all responses and peer reviews and synthesizes a final answer. It's a blind academic peer review process—but for language models. ## The Three-Stage Protocol **Stage One** is straightforward: all four models receive the same question simultaneously and answer in complete isolation. Four responses, no communication. **Stage Two** is where the architecture gets interesting. The responses are anonymized using a single elegant line of Python: `chr(65 + i)`, which generates "A", "B", "C", "D" labels. The model-to-label mapping is stored separately. These anonymized responses are then sent to all four models in parallel for peer review. Each model evaluates each response, identifies strengths and weaknesses, and produces a FINAL RANKING in a strict format. Notably, the ranking criteria—"accuracy" and "insight"—are deliberately left undefined, allowing models to interpret quality on their own terms. This mirrors how human expert panels work: you trust their judgment rather than constraining it with detailed rubrics. **Stage Three** is the synthesis phase. The Chairman model (Gemini-3 Pro Preview by default) now sees full model names and reads all responses, rankings, and peer reviews. It synthesizes a single final answer. The Chairman wears two hats: in Stage Two it was just another anonymous reviewer, but in Stage Three it becomes the meta-reasoner with full context. ## The Anonymization Problem The anonymization is designed to suppress self-preference bias. Research shows that language models assign higher ratings to texts with lower perplexity relative to their own output—they prefer texts that sound like what they themselves would generate. Stripping model names breaks this link. But there's a catch: anonymization strips the name, not the fingerprint. Claude tends toward structured lists. GPT tends toward flowing prose. Grok has a distinctive voice. A model might be identifiable even when anonymized. Karpathy acknowledges this in the documentation, noting that the implementation "prioritizes simplicity over cryptographic guarantees." This probabilistic anonymization appears to be doing real work, though. When Vasuman M from Varick AI Agents replicated the system and tested what happens if you *un-anonymize* answers—telling models "this came from GPT"—they immediately defer and start correcting themselves based on the named model's output. Without anonymization, you get model tribalism rather than genuine evaluation. ## The Consensus Paradox Here's a critical limitation: the council doesn't actually deliberate. Models never revise their Stage One responses. There's no back-and-forth, no position revision, no multi-round debate. It's one round of parallel opinions, one round of parallel rankings, one synthesis. This differs from the multi-agent debate (MAD) paradigm in academic literature, where models iteratively refine responses over multiple rounds after seeing disagreement. The Chairman's synthesis is also its own new response—not a vote, not a weighted average, but a fifth answer that happens to have read the other four. The quality of the final output depends heavily on the Chairman model's ability to integrate conflicting information. ## Empirical Findings and Human Disagreement When Karpathy used the council to evaluate book chapters, GPT-5.1 consistently won the peer rankings. But he added a crucial caveat: "I'm not one hundred percent convinced this aligns with my own qualitative assessment. I find GPT five point one a little too wordy and Gemini a bit more condensed and processed." The council's consensus diverged from the human's preference. The models agreed on what was best by their criteria, but the human evaluator preferred something different. This raises a fundamental question: what are we optimizing for when we build consensus systems? The council measures what models think is good, not what humans think is good. ## Design Philosophy Throughout the codebase, a pattern emerges: "be strict in what you ask for, be lenient in what you accept." The ranking prompt demands a rigid format, but the parser has three levels of fallback in case the model fails to comply. The prompt engineering and parsing are co-designed. This pragmatism is documented explicitly in the CLAUDE.md file, which notes common gotchas and design tradeoffs. The error handling is similarly elegant. If a single model fails to respond, it's silently dropped from the council—graceful degradation by design. The documentation notes: "Never fail the entire request due to single model failure." ## The Verdict llm-council is

**Решение:** -1 подкаст / стенограмма обсуждения llm-council

---

### 152 · R8677

**The Potential and Applications of Artificial Intelligence in the Field of Audiology**

2025 · Audiology and Speech Research · journalarticle, article · en · https://doi.org/10.21848/asr.250189

The rapid development of large language models such as Generative artificial intelligence (AI) and Chat generative pre-trained transformer (ChatGPT) presents new possibilities and innovative approaches across health care. This trend is no exception in the field of audiology, and the possibility of using artificial intelligence in various domains-such as education, clinical decision-making assistance, patient counseling and audiologic rehabilitation program-is being actively explored. For the effective introduction of Generative AI, prompt engineering is a key factor beyond simple technology implementation. In addition, ethical considerations based on the use of AI must be integrated in fields dealing with patients' personal information, such as audiology. Institutional regulation and expert-led ethical guidelines should be prepared in advance to prevent potential risks. AI should be understood not as a replacement for human experts, but as a companion that complements and enhances clinical judgment and educational activities. Collaboration with generative AI is no longer a choice, but a necessity-and how wisely we integrate and design it will be a pivotal factor in shaping the future of audiology.

**Решение:** -1 нарративный обзор применения LLM в аудиологии

---

### 153 · R7476

**GenXSS: an AI-Driven Framework for Automated Detection of XSS Attacks in WAFs**

2025 · Preprints.org · preprint/article, preprint, ppr · en · https://doi.org/10.20944/preprints202503.0313.v1

The increasing reliance on web services has led to a rise in cybersecurity threats, particularly Cross-Site Scripting (XSS) attacks, which target client-side layers of web applications by injecting malicious scripts. Traditional Web Application Firewalls (WAFs) struggle to detect highly obfuscated and complex attacks, as their rules require manual updates. This paper presents a novel generative AI framework that leverages Large Language Models (LLMs) to enhance XSS mitigation. The framework achieves two primary objectives: (1) generating sophisticated and syntactically validated XSS payloads using in-context learning, and (2) automating defense mechanisms by testing these attacks against a vulnerable application secured by a WAF, classifying bypassing attacks, and generating effective WAF security rules. Experimental results using GPT-4o demonstrate the framework's effectiveness generating 264 XSS payloads, 83% of which were validated, with 80% bypassing ModSecurity WAF equipped with an industry standard security rule set developed by the Open Web Application Security Project (OWASP) to protect against web vulnerabilities. Through rule generation, 86% of previously successful attacks were blocked using only 15 new rules. In comparison, Google Gemini Pro achieved a lower bypass rate of 63%, highlighting performance differences across LLMs.

**Решение:** -4 кибербезопасность, обнаружение XSS атак

---

### 154 · R12600

**An Interview with ChatGPT on Emergency Remote Teaching: A Comparative Analysis Based on Human–AI Collaboration**

2023 · Educational Process International Journal · article · en · https://doi.org/10.22521/edupij.2023.122.6

Background/purpose – ChatGPT, a recent form of AI-based language model, have garnered interest among people from diverse backgrounds with its immersive capabilities. Using ChatGPT to support or generate scientific research has also created an ongoing debate over its advantages versus risks. The present study aimed to conduct an AI-enabled research process using ChatGPT so as to evaluate its potential to generate an accurate, clear, concise, and unbiased information as these are essential elements of rigorous scientific work. Materials/methods – To achieve this aim, we worked on emergency remote teaching (ERT), which garnered significant interest due to its wide-spread use during the COVID-19 pandemic, and created opposing views, particularly in comparison to online teaching. We conducted a simultaneous query on ChatGPT-3.5 and 4 on five basic themes: (1) the definition and emergence of ERT, (2) the appropriateness of ERT for different grade levels, (3) a comparison between ERT and online teaching, (4) the possible outcomes of ERT, (5) the future prospects and uses of ERT, and we performed a comparative evaluation of these responses with regard to accuracy, clarity, conciseness, and potential bias. We also used Cohen’s kappa to assess inter-rater agreement in our analysis. Results – The results indicated that both versions were capable of generating accurate information without significant bias although the responses lacked depth and insight with being somewhat repetitive. As the level of judgment required by the query increased, the performance of ChatGPT-4 was much better; it provided clearer and more concise responses with a more synthesized and detailed categories of information on ERT. Conclusion – Based on our results, we state that the cooperation of human and artificial intelligence is still warranted to ensure an accurate and reliable output from AI-based scientific queries. If ChatGPT is a plane with innovative technologies, there still needs to be a pilot in the cockpit to make use of these technologies in the best way so as to fly the plane safely to its destination

**Решение:** -4 педагогика, экстренное дистанционное преподавание

---

### 155 · R2044

**GeoAffect: A Multi-Layer Annotation Schema and Few-Shot LLM Evaluation for Geoaffective Analysis of Literary Texts**

2026 · Language Resources and Evaluation Conference (LREC) · conference-paper · https://doi.org/10.63317/27q8itkapb24

GeoA!ect is an annotation framework that has been especially developed to capture how places are emotionally framed in literary narrative.The project focuses on nineteenth-century Greek prose fiction and brings together named entity recognition with an a!ect schema that distinguishes experiential, appraisal, and identity-oriented relations to place.The annotation design linked entities, emotion spans, and rhetorical devices, allowing us to model not only sentiment but also forms of belonging, alienation, and longing.To test the schema, we created a manually annotated gold dataset of approximately 360 sentences and evaluated thirteen Large Language Models in a few-shot setting for both entity recognition and a!ect classification.The results indicate that, with carefully designed prompts and selection strategies, LLMs can support structured geoa!ective annotation even in low-resource historical language contexts.

**Решение:** ? GeoAffect: разметка эмоций в греческой литературе XIX в. 13 LLM против эталона; проверить I2

---

### 156 · R5136

**Detecting Experiential Intertextuality Across Migration Routes: Beyond Surface Similarity in French Narratives**

2026 · SIGDIAL Conferences · journalarticle · https://doi.org/10.18653/v1/2026.sigdial-1.nn

Migrants traversing geographically distinct routes such as the Trans-Saharan and Balkan corridors often recount strikingly parallel lived experiences: police violence, smuggler exploitation, dangerous crossings, and family separation. We introduce the task of experiential intertextuality detection: automatically identifying shared experiential echoes across migration narratives without requiring annotated training data. From 108 French migration narratives spanning both corridors, we automatically generate sentence pairs and score them using annotation-free methods: lexical baselines, sentence embeddings, POS-based structural features, a migration-specific theme lexicon, context-aware narrative features, and zero-shot LLM scoring with Qwen2.5-7B and Mistral-7B under three prompting strategies. We validate all methods against 816 expert-annotated intertextuality judgments (inter-annotator Krippendorff's $\alpha = 0.27$). Our results reveal that all surface, structural, and embedding methods correlate only weakly with expert judgments ($r \leq 0.30$); Qwen2.5-7B zero-shot achieves the best single-method correlation ($r = 0.38$); few-shot examples degrade Qwen but dramatically improve Mistral; narrative position significantly predicts intertextuality, with departure-phase pairs showing the highest experiential echoes; and a supervised hybrid combining all 31 features achieves $r = 0.45$, a 21% improvement over the best individual method.

**Решение:** -4 литературоведение, нарративы мигрантов, интертекстуальность

---

### 157 · R3319

**Synthetic data enables human-grade microtubule analysis with foundation models for segmentation**

2026 · bioRxiv · journalarticle, preprint, ppr · en · https://doi.org/10.64898/2026.01.09.698597

Abstract Studying microtubules (MTs) and their mechanical properties is central to understanding intracellular transport, cell division, and drug action. While important, experts still need to spend many hours manually segmenting these filamentous structures. The suitability of state-of-the-art methods for this task cannot be systematically assessed, as large-scale labeled datasets are missing. We address this gap by presenting the synthetic dataset SynthMT, produced by tuning a novel image generation pipeline on real-world interference reflection microscopy (IRM) frames of in vitro reconstituted MTs without requiring human annotations. In our benchmark, we evaluate nine fully automated methods for MT analysis in both zero- and Hyperparameter Optimization (HPO)-based few-shot settings. Across both settings, classical algorithms and current foundation models still struggle to achieve the accuracy required for biological downstream analysis on in vitro MT IRM images that humans perceive as visually simple. However, a notable exception is the recently introduced SAM3 model. After HPO on only ten random SynthMT images, its text-prompted version SAM3Text achieves near-perfect and in some cases super-human performance on unseen, real data. This indicates that fully automated MT segmentation has become feasible when method configuration is effectively guided by synthetic data. To enable progress, we publicly release the dataset, the generation pipeline, and the evaluation framework at DATEXIS.github.io/SynthMT-project-page. Author summary Understanding the behavior of microtubules — stiff filaments inside cells — is essential for studying fundamental cell biological processes and for developing therapies for diseases such as cancer and neurodegenerative conditions. Yet, analyzing microtubule images is slow and labor-intensive, as researchers must manually trace these thin, overlapping filaments, which can take hours and is prone to errors. We therefore asked whether current fully automated segmentation methods are ready to replace manual microtubule analysis, and how synthetic data can be used to rigorously evaluate and improve them. To address these questions, we created a synthetic dataset that mimics real microtubule images by capturing the appearance and variability of real microscopy. Importantly, this dataset can be generated without any manual annotations. Using this dataset, we evaluated a range of segmentation methods and found that most of them struggled to accurately identify filaments. However, we discovered that a recent foundation model, when guided by a simple text instruction and tuned on only a few synthetic images, can achieve near-perfect, human-level performance on previously unseen real microtubule imaging data. Our work demonstrates that fully automated microtubule analysis is now possible and provides a reproducible framework that other researchers can use to evaluate and improve their methods. This opens the door to faster, more consistent studies of microtubules, ultimately accelerating discoveries in cell biology and therapeutic research.

**Решение:** -4 клеточная биология, сегментация микротрубочек

---

### 158 · R9388

**Generative AI and Creativity: A Systematic Literature Review and Meta-Analysis**

2025 · arXiv.org · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2505.17241

Generative artificial intelligence (GenAI) is increasingly used to support a wide range of human tasks, yet empirical evidence on its effect on creativity remains scattered. Can GenAI generate ideas that are creative? To what extent can it support humans in generating ideas that are both creative and diverse? In this study, we conduct a meta-analysis to evaluate the effect of GenAI on the performance in creative tasks. For this, we first perform a systematic literature search, based on which we identify n = 28 relevant studies (m = 8214 participants) for inclusion in our meta-analysis. We then compute standardized effect sizes based on Hedges' g. We compare different outcomes: (i) how creative GenAI is; (ii) how creative humans augmented by GenAI are; and (iii) the diversity of ideas by humans augmented by GenAI. Our results show no significant difference in creative performance between GenAI and humans (g = -0.05), while humans collaborating with GenAI significantly outperform those working without assistance (g = 0.27). However, GenAI has a significant negative effect on the diversity of ideas for such collaborations between humans and GenAI (g = -0.86). We further analyze heterogeneity across different GenAI models (e.g., GPT-3.5, GPT-4), different tasks (e.g., creative writing, ideation, divergent thinking), and different participant populations (e.g., laypeople, business, academia). Overall, our results position GenAI as an augmentative tool that can support, rather than replace, human creativity-particularly in tasks benefiting from ideation support. 22 pages, 6 figures. Code and data are available at https://github.com/SM2982/Meta-Analysis-LLMs-Creativity.git

**Решение:** -1 мета-анализ влияния GenAI на креативность

---

### 159 · R5806

**ChatGPT and Unintentional Resume Falsehoods: The Need for Human Intervention**

2026 · Postdisciplinary studies in discourse · book-chapter · en · https://doi.org/10.1007/978-3-032-07761-5_9

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 HR, оценка резюме кандидатов

---

### 160 · R9712

**A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks**

2025 · IEEE International Women in Engineering (WIE) Conference on Electrical and Computer Engineering (WIECON-ECE) · journalarticle, conference, preprint/article · en · https://doi.org/10.1109/wiecon-ece69386.2025.11526251

Prompt injection attacks represent a major vulnerability in Large Language Model (LLM) deployments, where malicious instructions embedded in user inputs can override system prompts and induce unintended behaviors. This paper presents a novel multi-agent defense framework that employs specialized LLM agents in coordinated pipelines to detect and neutralize prompt injection attacks in real-time. We evaluate our approach using two distinct architectures: a sequential chain-of-agents pipeline and a hierarchical coordinator-based system. Our comprehensive evaluation on 55 unique prompt injection attacks, grouped into 8 categories and totaling 400 attack instances across two LLM platforms (ChatGLM and Llama2), demonstrates significant security improvements. Without defense mechanisms, baseline Attack Success Rates (ASR) reached 30% for ChatGLM and 20% for Llama2. Our multi-agent pipeline achieved 100% mitigation, reducing ASR to 0% across all tested scenarios. The framework demonstrates robustness across multiple attack categories including direct overrides, code execution attempts, data exfiltration, and obfuscation techniques, while maintaining system functionality for legitimate queries. Accepted at the 11th IEEE WIECON-ECE 2025

**Решение:** -4 кибербезопасность, защита от prompt injection

---

### 161 · R6047

**Artificial Intelligence in Clinical Medicine: A ComprehensiveReview of Diagnostic Algorithms, Therapeutic Decision-Making,and Future Frontiers**

2026 · Japan Journal of Clinical & Medical Research · journalarticle, review, article · https://doi.org/10.47363/jjcmr/2026(6)211

Artificial intelligence (AI) has emerged as a transformative force in clinical medicine, reshaping how diseases are diagnosed, treatments are selected, and patient care is delivered. This comprehensive review examines the current state and future trajectory of AI applications across the clinical spectrum, from diagnostic algorithms that match or exceed human expert performance in medical imaging and pathology, to therapeutic decision support systems that optimize treatment selection, drug dosing, and surgical planning. We synthesize evidence from recent studies demonstrating that deep learning models have achieved diagnostic accuracy comparable to or exceeding that of board-certified specialists across multiple specialties, including radiology (AUC 0.92–0.98), pathology (AUC 0.90–0.97), dermatology (AUC 0.91–0.96), and ophthalmology (AUC 0.94–0.99). In therapeutics, AI-Driven dosing algorithms have reduced adverse drug events by 30–45% in prospective studies, while machine learning-based treatment response prediction has demonstrated AUC values of 0.78–0.88 across oncology, cardiology, and psychiatry. However, significant challenges persist, including the gap between algorithmic performance and clinical outcome improvement, the “black box” problem of model interpretability, algorithmic bias, and the paucity of prospective validation studies. We critically examine these barriers and outline future frontiers, including multimodal AI integration, foundation models, causal inference, and Human-AI collaboration. We conclude that while AI has demonstrated remarkable capabilities in controlled research settings, successful clinical translation requires rigorous prospective validation, workflow integration, and a commitment to addressing ethical and practical challenges.

**Решение:** -1 обзор применения ИИ в клинической медицине

---

### 162 · R2620

**Anamnesio_bot: A Chatbot Prototype Based on Generative Artificial Intelligence for Clinical Anamnesis Study and Simulation**

2026 · Lecture notes in networks and systems · conference-paper · en · https://doi.org/10.1007/978-3-032-10731-2_13

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -6 прототип Anamnesio_bot для сбора анамнеза без кодирования текста

---

### 163 · R8247

**The Potential of AI Chatbots as Diagnostic Tools in Mental Health: Evaluating Exercise Dependence Symptoms**

2025 · Journal of Technology in Behavioral Science · journalarticle, article · en · https://doi.org/10.1007/s41347-025-00567-2

Abstract This study aimed to evaluate the effectiveness of AI chatbots (Claude-3.5 Sonnet, ChatGPT-4o, and Gemini-1.5 Pro) in identifying exercise dependence symptoms using a hypothetical case study. To this end, three sport psychologists, each with a minimum of five years of experience, assessed the chatbots' performance in diagnostic assessment competency, implementation of diagnostic criteria, summary quality, terminology use, and overall effectiveness. The results indicated that while all chatbot models successfully identified major symptoms, their performance varied. Specifically, the Claude-3.5 Sonnet model demonstrated superior performance in specific areas, such as providing a clear case summary and using accurate terminology. However, all chatbots exhibited limitations in recognizing symptom severity and distinguishing between primary and secondary dependence. The sport psychologists expressed a willingness to use at least one AI chatbot model as an assistive tool in initial client assessments. These findings highlight the potential value of AI chatbots in mental health assessments. Future research should prioritize the optimization of algorithms and training data through expert collaboration and controlled real-world testing to improve the reliability and practical application of these tools.

**Решение:** -2 психологи оценивают ответы чат-бота на предмет компульсивных упражнений; LLM объект

---

### 164 · R8491

**Expressing stigma and inappropriate responses prevents LLMs from safely replacing mental health providers.**

2025 · ACM Conference on Fairness, Accountability, and Transparency (FAccT) · journalarticle, book, review · en · https://doi.org/10.1145/3715275.3732039

Should a large language model (LLM) be used as a therapist? In this paper, we investigate the use of LLMs to replace mental health providers, a use case promoted in the tech startup and research space. We conduct a mapping review of therapy guides used by major medical institutions to identify crucial aspects of therapeutic relationships, such as the importance of a therapeutic alliance between therapist and client. We then assess the ability of LLMs to reproduce and adhere to these aspects of therapeutic relationships by conducting several experiments investigating the responses of current LLMs, such as gpt-4o. Contrary to best practices in the medical community, LLMs 1) express stigma toward those with mental health conditions and 2) respond inappropriately to certain common (and critical) conditions in naturalistic therapy settings—e.g., LLMs encourage clients’ delusional thinking, likely due to their sycophancy. This occurs even with larger and newer LLMs, indicating that current safety practices may not address these gaps. Furthermore, we note foundational and practical barriers to the adoption of LLMs as therapists, such as that a therapeutic alliance requires human characteristics (e.g., identity and stakes). For these reasons, we conclude that LLMs should not replace therapists, and we discuss alternative roles for LLMs in clinical therapy. Content warning: Contains content and examples related to sensitive mental health topics, including suicide.

**Решение:** -2 психиатры оценивают ответы чат-ботов на бред и стигму; LLM объект

---

### 165 · R9439

**“That is scary!”: consumer perceptions and discourses on ChatGPT**

2025 · Qualitative Market Research An International Journal · journalarticle, article · en · https://doi.org/10.1108/qmr-07-2024-0122

Purpose The rise of conversational artificial intelligence (AI) bots such as ChatGPT highlights users’ anxieties and high expectations. This study aims to explore consumers’ views of AI conversational bots and examines their societal implications, emphasizing public perception as a fundamental factor in their acceptance and integration. Design/methodology/approach This study combines manual and automated thematic analysis to understand public sentiment by analyzing 45,844 YouTube comments. The comments are collected from the top five nonsponsored English-language YouTube videos on ChatGPT, with comments extracted using Octoparse. Key themes and their relationships are identified through manual coding and further analyzed using Leximancer to enhance the depth and accuracy of the analysis by detecting patterns in large data sets. Findings The analysis reveals three primary areas: empowerment through AI-enhanced capabilities, anxiety over AI-induced societal shifts and negotiating human–AI collaboration. Concerns are expressed about misinformation, privacy and the impact of AI on employment and human skills. Conversely, positive perceptions highlight AI’s role in education, personal productivity and medical diagnosis. These themes categorize public sentiment into techno-skepticism, techno-realism and techno-optimism, demonstrating the complex and diverse opinions on AI technology. Originality/value This research bridges AI’s technical aspects with its social and ethical dimensions, providing a comprehensive understanding of public sentiment towards ChatGPT. It underscores the importance of examining consumer views as a foundational step in understanding AI’s broader societal impacts.

**Решение:** -4 маркетинг, восприятие потребителями ChatGPT

---

### 166 · R2653

**ClinStigma: A Clinician-Guided Framework for Developing Synthetic Benchmarks of Contextual Stigmatizing Language in Clinical Documentation**

2026 · medRxiv · preprint, ppr, review · https://doi.org/10.64898/2026.10.10.26365233

Objective Large language models (LLMs) are increasingly used to generate, summarize, and evaluate clinical documentation, yet standardized methods for evaluating nuanced, context-dependent clinical language remain limited. Existing approaches rely primarily on annotated clinical corpora or keyword-based methods, restricting reproducibility, public dissemination, and systematic comparison across models. We present ClinStigma, a clinician-guided framework for constructing, annotating, and evaluating synthetic benchmarks of contextual stigmatizing language, demonstrated through ClinStigma-SUD, its inaugural implementation for substance use disorder documentation. Materials and Methods Candidate clinical sentences were generated using a frontier language model and iteratively reviewed according to a clinician-developed annotation rubric refined through expert review in stigmatizing language. The resulting benchmark intentionally incorporates explicit stigmatizing, neutral, and contextually ambiguous ("gray-zone") documentation requiring clinical reasoning rather than keyword recognition. Three locally deployed open-weight LLMs were evaluated using zero-shot inference, followed by external evaluation using independently annotated clinical documentation from MIMIC-IV. Results ClinStigma-SUD consists of 500 clinician-adjudicated synthetic clinical documentation sentences. Inter-rater agreement was 98.8% across the full benchmark (Cohen's {kappa} = 0.976) and 94.0% within the intentionally ambiguous subset ({kappa} = 0.880). Under zero-shot prompting, binary accuracy ranged from 84.8% to 91.8% across evaluated models, while F1 for the ambiguous (gray) class ranged from 0.038 to 0.423. Zero-shot external evaluation on 3,716 annotated examples from the independently annotated Harrigian MIMIC-IV corpus yielded 84.4% accuracy (84.4% balanced accuracy; macro F1 0.824), against a 69.9% majority-class baseline. Stigmatizing-class F1 was 0.879 in the substance-related subgroup and 0.883 in the full external corpus. Discussion and Conclusion ClinStigma establishes a reproducible clinician-guided framework for developing synthetic evaluation benchmarks for contextual clinical language. By combining structured clinical expertise, explicit annotation guidance, synthetic benchmark generation, and external evaluation, the framework enables open, privacy-preserving evaluation of language models while providing a scalable foundation for benchmark development across additional clinical specialties, including obstetrics, emergency medicine, and mental health.

**Решение:** + T1 ClinStigma-SUD: кодирование стигматизирующего языка в картах пациентов с SUD, LLMs vs эксперты, F1=0.82

---

### 167 · R11539

**Human-AI Collaboration in Cooperative Games: A Study of Playing Codenames with an LLM Assistant**

2024 · Proceedings of the ACM on Human-Computer Interaction · journalarticle, article, journal-article · en · https://doi.org/10.1145/3677081

Playing partial information, restricted communication, cooperative (PIRCC) games with humans have proven challenging for AI, due to our reliance on social dynamics and sophisticated cognitive techniques. Yet, recent advances in generative AI may change this situation through new forms of human-AI collaboration. This paper investigates how teams of players interact with an AI assistant in the PIRCC game Codenames and the impact this has on cognition, social dynamics, and player experience. We observed gameplay and conducted post-game focus groups with 54 participants across ten groups. Each group played three rounds of Codenames, with an AI assistant supporting Cluegivers. We found the AI assistant enhanced players' convergent and divergent thinking, but interfered with formation of team mental models, highlighting a tension in the use of AI in creative team scenarios. The presence of the AI challenged many players' understanding of the 'spirit of the game'. Furthermore, the presence of the AI assistants weakened social connections between human teammates, but strengthened connections across teams. This paper provides an empirical account of an AI assistant's effect on cognition, social dynamics, and player experience in Codenames. We highlight the opportunities and challenges that arise when designing hybrid digital boardgames that include AI assistants.

**Решение:** -4 игра Codenames, HCI

---

### 168 · R11171

**MASTERKEY: Automated Jailbreaking of Large Language Model Chatbots**

2024 · Network and Distributed System Security Symposium · conference-paper · en · https://doi.org/10.14722/ndss.2024.24188

lenge in ensuring the secure and ethical usage of LLMs [31].Jailbreaking, in this context, refers to the strategic manipulation of input prompts to LLMs, devised to outsmart the chatbots' safeguards and generate content otherwise moderated or blocked.By exploiting such carefully crafted prompts, a malicious user can induce LLM chatbots to produce harmful outputs that contravene the defined policies.Past efforts have been made to investigate the jailbreak vulnerabilities of LLMs [31], [27], [62], [51]. However, with the rapid evolution of LLM technology, these studies exhibit two significant limitations.First, the current focus is mainly limited on CHATGPT.We lack the understanding of potential vulnerabilities in other commercial LLM chatbots such as Bing Chat and Bard.In Section III, we will show that these services demonstrate distinct jailbreak resilience from CHATGPT.Second, in response to the jailbreak threat, service providers have deployed a variety of mitigation measures.These measures aim to monitor and regulate the input and output of LLM chatbots, effectively preventing the creation of harmful or inappropriate content.Each service provider deploys its proprietary solutions adhering to their respective usage policies.For instance, OpenAI [40] has laid out a stringent usage policy [42], designed to halt the generation of inappropriate content.This policy covers a range of topics from inciting violence to explicit content and political propaganda, serving as a fundamental guideline for their AI models.The black-box nature of these services, especially their defense mechanisms, poses a challenge to comprehending the underlying principles of both jailbreak attacks and their preventative measures.As of now, there is a noticeable lack of public disclosures or reports on jailbreak prevention techniques used in commercially available LLM-based chatbot solutions.To close these gaps and further obtain an in-depth and generalized understanding of the jailbreak mechanisms among various LLM chatbots, we first undertake an empirical study to examine the effectiveness of existing jailbreak attacks.We evaluate four mainstream LLM chatbots: CHATGPT powered § Equal

**Решение:** -4 кибербезопасность, джейлбрейкинг

---

### 169 · R4938

**Neurocognitive assessment of generative AI on designers’ creative cognition: evidence from biologically inspired design tasks**

2026 · Proceedings of the Design Society · journalarticle, article · en · https://doi.org/10.1017/pds.2026.10469

ABSTRACT: Designers use GenAI tools during bioinspired design (BID) process to understand biological inspiration. We investigate the influence of using ChatGPT with BID on their creative thinking. We present BID stimuli to 30 designers in three modes: BID only, ChatGPT only, and BID + ChatGPT; and record their EEG data across four design phases. Their creativity is analyzed through convergent and divergent thinking (CT and DT), measured by average β and α TRP, respectively. Results show that BID stimuli’s influence on CT and DT is mode and phase dependent, indicating CT and DT as continuous processes.

**Решение:** -4 ЭЭГ дизайнеров в биоинспирированном дизайне

---

### 170 · R11179

**Creative Beam Search: LLM-as-a-Judge For Improving Response Generation**

2024 · ICCC · journalarticle, preprint/article, conference paper · https://doi.org/10.48550/arxiv.2405.00099

Large language models are revolutionizing several areas, including artificial creativity. However, the process of generation in machines profoundly diverges from that observed in humans. In particular, machine generation is characterized by a lack of intentionality and an underlying creative process. We propose a method called Creative Beam Search that uses Diverse Beam Search and LLM-as-a-Judge to perform response generation and response validation. The results of a qualitative experiment show how our approach can provide better output than standard sampling techniques. We also show that the response validation step is a necessary complement to the response generation step.Presented as a short paper at the 15th International Conference on Computational Creativity (ICCC\u2724

**Решение:** -4 генерация рекламных слоганов, Creative Beam Search

---

### 171 · R4384

**PSI-Bench: Interpretable and Clinically Meaningful Evaluation of Depression Patient Simulators**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.25840

Patient simulators are gaining traction in mental health training by providing scalable exposure to complex and sensitive patient interactions. Simulating depressed patients is challenging, as safety constraints and high patient variability complicate simulations and underscore the need for simulators that capture diverse and realistic patient behaviors. However, existing evaluations heavily rely on LLM-judges with poorly specified prompts and do not assess behavioral diversity. We introduce PSI-Bench, an automatic evaluation framework that provides interpretable, clinically meaningful diagnostics of depression patient simulator behavior across turn-, dialogue-, and population-level dimensions. Using PSI-Bench, we benchmark seven LLMs across two simulator frameworks and find that simulators produce overly long, lexically diverse responses, show reduced variability, and move through therapeutic stages and toward positive valence too quickly. We also show that the simulation framework has a larger impact on fidelity than the model scale. Results from a human study demonstrate that our benchmark is strongly aligned with judgments of mental health professionals. Our work reveals key limitations of current depression patient simulators and provides an interpretable, extensible benchmark to guide future simulator design and evaluation. COLM Social Sim'26 Spotlight

**Решение:** ? PSI-Bench: симуляция пациентов с депрессией; проверить по полному тексту наличие LLM-as-judge против врачей

---

### 172 · R5146

**Challenge and Hindrance Appraisals and Causal Attributions in AI-induced technostress : Critical Incident study of Knowledge Workers**

2026 · Tampere University Institutional Repository (Tampere University) · dissertation · en

Generative artificial intelligence (AI) tools are being adopted into knowledge work rapidly and often without established practices to guide their use. Such tools can support and accelerate work, but they can also become a source of stress. This thesis examines AI-induced technostress as it is experienced and interpreted by knowledge workers themselves. It addresses two parallel questions: how knowledge workers appraise AI-related demands as challenge or hindrance stressors, and to which targets they attribute the causes of the outcomes of their AI-supported tasks when stress is present. The study draws on semi-structured interviews with 21 knowledge workers in five Finnish companies, conducted using the Critical Incident Technique, in which participants described concrete positive and negative episodes of working with generative AI tools. Data was analyzed through Codebook Thematic Analysis. The analysis combined a transactional, appraisal-based view of stress and the challenge–hindrance distinction with a causal attribution lens based on the locus of causality. 28 incidents were analyzed for the appraisal question and 26 for the attribution question. The analysis identified six AI-induced demands: output volume handling, managing AI use, input specification, output verification, iterative refinement, and competence building. Within these demands, thirteen hindrance stressors and eight challenge stressors were distinguished. Five of the six demands were appraised as both a challenge and a hindrance across incidents. Hindrance appraisals were more frequent in the data. Knowledge workers attributed task outcomes to four targets: the user, the AI tool, the task, and the vendor behind the tool. The attributions were asymmetric across outcomes (success vs. fail). For failed outcomes, the most prevalent pattern was internal: workers tended to locate the cause in their own prompting, context-setting, or domain knowledge, absorbing the failure as their own. For successful outcomes, attributions surfaced less readily and were more diffuse, most often shared between the worker and the tool or assigned to the tool alone. The findings indicate that the demands of generative AI are dual and appraisal-dependent, and that some of them are captured only partially by the established technostressor taxonomy. The prevailing tendency to internalize the cause of AI failures runs counter to common expectations from attribution research and may reflect the absence of shared practices for working with AI. For organizations, the results suggest that the productivity case for AI should be weighed against the verification, iteration, and effort it requires, that shared ways of working may reduce misplaced self-blame, and that the capacity to manage one's own use of AI is itself a competence worth supporting.

**Решение:** -5 диссертация: только ручной тематический анализ по кодбуку, LLM не размечала текст

---

### 173 · R1653

**AI-Based Detection of Manipulative Political Narratives - Georgian and Lithuanian Media (2026)**

2026 · OSF Preprints (OSF Preprints) · preprint

Codebook, AI coding output (Claude Sonnet 5 and ChatGPT), human coder data, and reliability results supporting the conference paper "Artificial Intelligence and Comparative Media Research: Detecting Manipulative Political Narratives in Small-Language Media Systems (Evidence from Georgian and Baltic Media)."

**Решение:** -4 политический дискурс, нарративы манипуляции в медиа

---

### 174 · R4158

**A multi-agent large language model framework for structured clinical interviewing and psychiatric screening: a proof-of-concept**

2026 · Translational Psychiatry · journalarticle, article · en · https://doi.org/10.1038/s41398-026-04335-5

Structured psychiatric interviews improve diagnostic reliability but are resource-intensive to administer. We developed a multi-agent large language model (LLM) framework to support protocolized structured interviewing and module-level psychiatric screening. The system orchestrates four agents, Questioner, Evaluator, Navigator, and Diagnoser, to administer interview modules, interpret free-text responses, enforce bounded clarification loops, identify safety-related red flags and trigger escalation, and apply encoded decision rules to produce screening outcomes. Prior to any model processing, responses undergo automated redaction of personally identifiable and protected health information. We conducted a simulation-based technical evaluation using 1350 interviews across 15 neuropsychiatric screening modules (e.g., anxiety, depression, and bipolar disorders) with systematic variation in symptom direction, disclosure depth, and emotional tone. To test robustness to language variability, we additionally evaluated reconstructed conversation bundles derived from the deidentified MentalChat16K dataset. In the primary evaluation, module-level decisions showed 87.8% concordance with rule-based expected outcomes (95% CI: 85.9–89.6), with sensitivity 88.9% (95% CI: 86.5–91.2) and specificity 86.7% (95% CI: 84.0–89.2) relative to predefined item-level endorsements. Post hoc comparator analyses showed higher F2 for the multi-agent framework (88.5%) than single-pass LLM (49.5%) or deterministic rule-based (61.9%) transcript-scoring baselines. On a 2000-sentence red flag benchmark stratified by explicit/implicit and active/passive ideation, the classifier achieved 93.9% accuracy, 94.2% sensitivity, and 93.6% specificity. In pilot feedback from mental health clinicians, descriptive ratings suggested favorable perceptions of clarity, workflow fit, and perceived safety for clinician-supervised use. These results support proof-of-concept technical feasibility for a protocol-adherent, auditable agentic LLM framework for structured psychiatric screening.

**Решение:** ? Translational Psychiatry: многоагентный скрининг психических расстройств; проверить сопоставление с клиницистами

---

### 175 · R11186

**ChatGPT and other Chatbots in Psychiatry**

2024 · Archives of Psychiatry Research · journalarticle, review, article · en · https://doi.org/10.20471/june.2024.60.02.07

Aim: Artificial intelligence (AI) is making significant inroads into the field of psychiatry, offering new tools and applications. ChatGPT, a specific chatbot, is at the forefront of this digital revolution. AI’s use in psychiatry ranges from identifying psychiatric symptoms, predicting treatment responses, and improving medication adherence to assisting in patient education, monitoring, and bridging gaps in mental health care. Materials and Methods: This review used a literature study method. Results: ChatGPT functions as a clinical decision support tool. It can analyse patient data and provide diagnostic insights, recommend evidence-based treatments, and offer drug information. It has demonstrated proficiency in generating summaries from medical records, saving clinicians time and enabling them to focus on patient care. Additionally, chatbots like ChatGPT serve as therapist assistants, offering emotional support between therapy sessions and potentially conducting psychotherapy. Studies have shown positive outcomes, with chatbots reducing depression, anxiety symptoms, and providing 24/7 availability for crisis situations. Users find them non-judgmental and comfortable for discussing sensitive issues. Despite their potential, chatbots have limitations, such as the risk of incorrect or biased information due to their training data. They lack genuine understanding, creativity, and the ability to clarify user input. Ethical considerations regarding responsibility and data usage are paramount. Conclusion: AI, particularly ChatGPT, holds substantial promise in modern psychiatry, enhancing diagnostics, patient education, monitoring, and therapeutic support. Its integration into everyday psychiatric practice requires careful use, continuous oversight, and ethical considerations. Psychiatrists must become more familiar with AI tools to leverage their benefits in patient care.

**Решение:** -1 обзор применения ChatGPT в психиатрии

---

### 176 · R7199

**Comparative Analysis of Gemini and LLaMA 3 for Zero-Shot Emotion Classification of Indonesian Texts**

2025 · International Conference on Orange Technology (ICOT) · conference, conference-paper · https://doi.org/10.1109/icot68409.2025.11425704

This study presents a comparative analysis of two state-of-the-art large language models (LLMs) Google Gemini and Meta LLaMA 3 for zero-shot emotion classification of Indonesian texts. As research on Indonesian emotion classification remains limited, this study addresses a critical gap by evaluating the performance of these models without task-specific fine-tuning. Both models were evaluated on a labeled dataset comprising 90 Indonesian text samples across six emotion categories (Joy, Sadness, Anger, Fear, Surprise, and Neutral) using accuracy, precision, recall, F1-score, and Cohen's Kappa. The results demonstrate that Gemini achieves superior performance with an accuracy of 77.33% and Cohen's Kappa of 0.72, compared to LLaMA 3's accuracy of 61.33% and Cohen's Kappa of 0.51. Gemini's balanced precision and recall across all emotion categories, particularly for complex emotions such as Fear and Surprise, highlight its robustness in handling the nuances of the Indonesian language. In contrast, LLaMA 3 exhibits notable biases, frequently misclassifying emotions as Joy and Sadness. These findings underscore the importance of model selection and prompt engineering in achieving accurate emotion classification for low-resource languages. This study contributes valuable insights into the application of LLMs for Indonesian NLP tasks and provides a foundation for future research in multilingual emotion analysis.

**Решение:** + T1 классификация эмоций в индонезийских текстах, Gemini и LLaMA 3 vs люди, κ=0.72 и 0.51

---

### 177 · R0116

**Semantic Causal and Correlation-Causal Graphs Based on Large Language Model Relationship Evaluation**

2026 · Automation, Control, and Information Technology · conference · https://doi.org/10.1109/acit69831.2026.11700225

Causality and correlation between pairs of attributes are closely related concepts relevant in a number of areas of data science and artificial in telligence. Until recently, the real-world semantic causality of relationships was determined exclusively by human experts. However, recent advances in large language models enable the substitution of this expert reasoning by automated systems in this domain. This development motivated the main objective of the presented study, which can be summarized as the design and implementation of two visualization models for semantic causal analysis based on large language models and correlation analysis, labelled as causal graphs and correlationcausal graphs. Both of the proposed models are evaluated on two datasets with the focus on qualitative, quantitative, and application-oriented aspects of the approaches. The results reached in the study indicate that the proposed methods are suitable for automated causality identification in the context of diagnostic and exploratory data analysis.

**Решение:** -4 data science, причинно-следственные графы

---

### 178 · R0596

**MM-tau-p$^2$: Persona-Adaptive Prompting for Robust Multi-Modal Agent Evaluation in Dual-Control Settings**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2603.09643

Current evaluation frameworks and benchmarks for LLM powered agents focus on text chat driven agents, these frameworks do not expose the persona of user to the agent, thus operating in a user agnostic environment. Importantly, in customer experience management domain, the agent's behaviour evolves as the agent learns about user personality. With proliferation of real time TTS and multi-modal language models, LLM based agents are gradually going to become multi-modal. Towards this, we propose the MM-tau-p$^2$ benchmark with metrics for evaluating the robustness of multi-modal agents in dual control setting with and without persona adaption of user, while also taking user inputs in the planning process to resolve a user query. In particular, our work shows that even with state of-the-art frontier LLMs like GPT-5, GPT 4.1, there are additional considerations measured using metrics viz. multi-modal robustness, turn overhead while introducing multi-modality into LLM based agents. Overall, MM-tau-p$^2$ builds on our prior work FOCAL and provides a holistic way of evaluating multi-modal agents in an automated way by introducing 12 novel metrics. We also provide estimates of these metrics on the telecom and retail domains by using the LLM-as-judge approach using carefully crafted prompts with well defined rubrics for evaluating each conversation. A benchmark for evaluating multimodal both voice and text LLM agents in dualcontrol settings. We introduce persona adaptive prompting and 12 new metrics to assess robustness safety efficiency and recovery in customer support scenarios

**Решение:** -4 менеджмент клиентского опыта, CRM

---

### 179 · R9308

**S4113 Virtual Reality as a Non-Pharmacologic Adjunct for Pain and Anxiety During an Unsedated Colonoscopy: Case Report**

2025 · The American Journal of Gastroenterology · conference-abstract · en · https://doi.org/10.14309/01.ajg.0001143912.27117.7a

Introduction: Colorectal cancer (CRC) is the second leading cause of cancer-related deaths in the United States. Colonoscopy is the gold-standard and most common procedure for colorectal cancer screening, often performed under sedation to enhance patient comfort. However, sedation poses risks and requires post-procedural assistance, limiting access for individuals without transportation, social support, or with anesthesia contraindications. Virtual reality (VR) is a promising non-pharmacological tool for managing procedural pain and anxiety. We present a case demonstrating successful use of VR to facilitate unsedated colonoscopy in a patient with medical comorbidities and logistical barriers to sedation. Case Description/Methods: A 77-year-old woman with a history of breast cancer s/p lumpectomy and radiation therapy, obstructive sleep apnea, and hypertension presented for a routine surveillance colonoscopy given history of tubular adenomas. Lacking post-procedure transportation, she opted for an unsedated procedure, which revealed a fixed, angulated, and tortuous sigmoid colon with severe diverticulosis. Despite using the water immersion technique, the patient showed signs of distress, physical tension and discomfort, resulting in a challenging procedure. To improve tolerability, a VR headset displaying a calming lakeside sunset scene with soothing audio was introduced mid-procedure. Upon use, the patient reported complete pain relief and showed visible relaxation, allowing the procedure to continue smoothly. Two polyps were removed with cold snare and forceps polypectomy. Pathology revealed 1 sessile serrated polyp and 1 tubular adenoma. Post-procedurally, the patient expressed high satisfaction and willingness to repeat a colonoscopy with VR. Discussion: This case study highlights VR as a safe, non-pharmacologic, non-invasive tool for managing pain and anxiety during medical procedures when sedation is not feasible. VR acts as an immersive distraction tool, redirecting attention away from noxious stimuli by engaging multisensory input. The patient displayed both subjective (verbal reports of “no pain”) and objective (muscle relaxation) signs of relief, allowing scope advancement despite complex anatomy. This case illustrates that VR can support unsedated colonoscopy as a viable, well-tolerated option, even in complex cases, enhancing access and procedural efficiency. Further research is warranted to assess VR’s broader clinical use. The authors used ChatGPT solely to reword and rephrase text.

**Решение:** -4 описание случая: VR при колоноскопии

---

### 180 · R7081

**Evaluating the Performance of AI Large Language Models in Detecting Pediatric Medication Errors Across Languages: A Comparative Study.**

2025 · Journal of clinical medicine · journal article, journalarticle, article · eng · https://doi.org/10.3390/jcm15010162

Objectives: This study aimed to evaluate the performance of four AI models, (GPT-5, GPT-4, Microsoft Copilot, and Google Gemini), in detecting medication errors through pediatric case scenarios. Methods: A total of 60 pediatric cases were analyzed for the presence of medication errors, of which only half contained errors. The cases covered four therapeutic systems (respiratory, endocrine, neurology, and infectious). The four models were exposed to the cases in both English and Arabic using a unified prompt. The responses for each model were used to calculate various performance metric cover accuracy, sensitivity, specificity and reproducibility. Analysis was carried out using SPSS version 22. Results: Microsoft Copilot demonstrated relatively higher accuracy (86.7% in English, 85.0% in Arabic) compared to other models in this dataset, followed by GPT-5 (81.7% in English, 75.0% in Arabic). GPT-4 and Google Gemini had less accuracy, with Gemini having the lowest accuracy across all languages (76.7% in English, and 73.3% in Arabic). Microsoft Copilot showed comparatively higher sensitivity and specificity, particularly in cases of respiratory and infectious diseases. The accuracy in Arabic was lower compared to that of English for the majority of models. Microsoft Copilot exhibited relatively higher reproducibility and inter-run agreement (Cohen's Kappa = 0.836 English, 0.815 Arabic, p < 0.001 for both), while Gemini showed the lowest reproducibility. For inter-language agreement in general, Copilot showed the highest Cohen's Kappa of 0.701 for English and Arabic (p < 0.001). Conclusions: In our evaluation, Microsoft Copilot demonstrated relatively higher performance in pediatric drug error detection compared to the other AI models. The decreased performance in Arabic points toward the requirement of improved multilingual training for supporting equal AI aid across languages. This study highlights the importance of human oversight and domain-based training for AI tools in pediatric pharmacotherapy.

**Решение:** -4 педиатрия, фармакологические ошибки в назначениях

---

### 181 · R9868

**From Inductive to Deductive: LLMs-Based Qualitative Data Analysis in Requirements Engineering**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2504.19384

Requirements Engineering (RE) is essential for developing complex and regulated software projects. Given the challenges in transforming stakeholder inputs into consistent software designs, Qualitative Data Analysis (QDA) provides a systematic approach to handling free-form data. However, traditional QDA methods are time-consuming and heavily reliant on manual effort. In this paper, we explore the use of Large Language Models (LLMs), including GPT-4, Mistral, and LLaMA-2, to improve QDA tasks in RE. Our study evaluates LLMs' performance in inductive (zero-shot) and deductive (one-shot, few-shot) annotation tasks, revealing that GPT-4 achieves substantial agreement with human analysts in deductive settings, with Cohen's Kappa scores exceeding 0.7, while zero-shot performance remains limited. Detailed, context-rich prompts significantly improve annotation accuracy and consistency, particularly in deductive scenarios, and GPT-4 demonstrates high reliability across repeated runs. These findings highlight the potential of LLMs to support QDA in RE by reducing manual effort while maintaining annotation quality. The structured labels automatically provide traceability of requirements and can be directly utilized as classes in domain models, facilitating systematic software design.

**Решение:** -4 инженерия требований в разработке ПО

---

### 182 · R4300

**Algorithmic Fragility and Persona Bias in LLM-Generated Autistic Communication**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2605.26397

Safety alignment reduces explicitly harmful outputs but inadvertently encodes a sanitized, neuronormative representation of marginalized communication. We investigate this encoding using a dual-persona rewrite paradigm, prompting ten large language models (LLMs) to rewrite naturally occurring autistic discourse from either an autistic or neurotypical persona. We uncover autistic-persona rewrites diverge significantly more in lexical form and affective register than neurotypical rewrites, despite equivalent semantic similarity. Furthermore, most models collapse cross-persona generations into near-identical outputs. To uncover the mechanisms behind this generative breakdown, we introduce a multi-agent qualitative analysis framework. Our results reveal systemic output erasure, stereotyped hallucination, and task-evasive meta-commentary are pervasive failure modes for this task that cluster by alignment strategy rather than parameter scale. Finally, our targeted comparison with autistic human annotators demonstrates that community-insider knowledge produces systematic label reversals relative to LLM classifications. Our findings indicate that current alignment training causes persona-specific generative breakdown visible only through qualitative analysis, confirming a deep representational gap that prompt engineering cannot resolve. main paper: 9 pages; total: 19 pages; 2 figures; 5 tables

**Решение:** ? классификация и перефразирование аутичной коммуникации vs аутичные разметчики-люди; проверить метрики согласия

---

### 183 · R7894

**The Effectiveness of Style Vectors for Steering Large Language Models: A Human Evaluation**

2025 · IEEE Access · journalarticle, preprint/article, article · en · https://doi.org/10.1109/access.2025.3628500

Controlling the behavior of large language models (LLMs) at inference time is essential for aligning outputs with human abilities and safety requirements. Activation steering provides a lightweight alternative to prompt engineering and fine-tuning by directly modifying internal activations to guide generation. This research advances the literature in three significant directions. First, while previous work demonstrated the technical feasibility of steering emotional tone using automated classifiers, this paper presents the first human evaluation of activation steering concerning the emotional tone of LLM outputs, collecting over 7,000 crowd-sourced ratings from 190 participants via Prolific ( $n=190$ ). These ratings assess both perceived emotional intensity and overall text quality. Second, we find strong alignment between human and model-based quality ratings (mean $r=0.776$ , range 0.157–0.985), indicating automatic scoring can proxy perceived quality. Moderate steering strengths ( $\lambda \approx 0.15$ ) reliably amplify target emotions while preserving comprehensibility, with the strongest effects for disgust ( $\eta _{p}^{2} = 0.616$ ) and fear ( $\eta _{p}^{2} = 0.540$ ), and minimal effects for surprise ( $\eta _{p}^{2} = 0.042$ ). Finally, upgrading from Alpaca to LlaMA-3 yielded more consistent steering with significant effects across emotions and strengths (all $p \lt 0.001$ ). Inter-rater reliability was high (ICC = 0.71–0.87), underscoring the robustness of the findings. These findings support activation-based control as a scalable method for steering LLM behavior across affective dimensions.

**Решение:** -2 люди оценивают перенос стиля в генерации текстов

---

### 184 · R6244

**Large Language Model Summarization of Physician-to-Physician Calls for Interhospital Transfer of Patients With ST-Elevation Myocardial Infarction: Observational Study.**

2026 · Journal of medical Internet research · journal article, observational study, med · eng · https://doi.org/10.2196/88834

Abstract Background Interhospital transfer of patients with suspected ST-elevation myocardial infarction (STEMI) requires timely and robust communication. Clinical uptake of potentially useful information from physician-to-physician phone calls authorizing transfer is low at many institutions, at least in part due to relative inaccessibility of call audio and lack of transcripts or summaries. Large language models (LLMs) can transform text into brief, consistently formatted summaries that could be made available in the electronic health record, thus facilitating the timely availability of clinically relevant data to physicians downstream of the transfer call. Objective We sought to assess the feasibility of using transcription and LLM summarization to provide written information summarizing transfer calls by adapting the Physician Documentation Quality Instrument (PDQI) to score generated call summaries and evaluate whether LLMs could effectively summarize a curated set of transfer calls. Methods STEMI transfer calls for which our institution was the receiving facility were transcribed and summarized by Whisper and ChatGPT (OpenAI), respectively. Each summary was reviewed by 2 of 7 independent physician raters. Summaries were rated using a Likert scale applied to an 8-domain framework adapted from the PDQI. We calculated summary statistics, including means, SDs, and raw and weighted agreement, and produced visual radar plots to demonstrate ratings for each call. We also performed thematic analysis of reviewers’ comments. Results We identified 32 calls, of which 1 (3.1%) was excluded for incompleteness. Raw agreement between raters was 62% (153/248), and the mean of the pairwise weighted κ coefficients was 0.19 (SD 0.30; slight agreement). The mean rating of all summaries across all domains was 4.6 of 5 (SD 0.7). The “useful” (mean 4.8/5, SD 0.5) and “consistent” (mean 4.9/5, SD 0.6) domains were the highest rated, and the “thorough” (mean 4.4/5, SD 1.0) and “hallucination free” (mean 4.4/5, SD 0.9) domains were the lowest rated. The mean score for accuracy was 4.6/5 (SD 0.7). Qualitative analysis found that raters penalized the LLM for inferential hallucinations, although these were often clinically accurate, and discrepancies related to calculation of timing of events. Conclusions Despite the limitations inherent in a small pilot cohort, this feasibility study suggests that LLMs can generate accurate and pertinent summaries of interhospital transfer calls for patients with STEMI. Interrater agreement was slight, which may suggest inadequate training of raters, unclear definitions, or a limitation of using the PDQI for this task. We identified several important areas for consideration prior to implementation, including thorough assessment of transcription accuracy, prompt engineering to minimize unwanted LLM behavior, and assessment of the impact of incorporating these summaries into clinical care on clinical outcomes.

**Решение:** -4 кардиология, инфаркт миокарда STEMI по звонкам

---

### 185 · R12775

**Transfer Learning for Risk Classification of Social Media Posts: Model Evaluation Study.**

2020 · Journal of medical Internet research · journal article, research support, non-u.s. gov't, research-article · eng · https://doi.org/10.2196/15371

BACKGROUND: Mental illness affects a significant portion of the worldwide population. Online mental health forums can provide a supportive environment for those afflicted and also generate a large amount of data that can be mined to predict mental health states using machine learning methods. OBJECTIVE: This study aimed to benchmark multiple methods of text feature representation for social media posts and compare their downstream use with automated machine learning (AutoML) tools. We tested on datasets that contain posts labeled for perceived suicide risk or moderator attention in the context of self-harm. Specifically, we assessed the ability of the methods to prioritize posts that a moderator would identify for immediate response. METHODS: We used 1588 labeled posts from the Computational Linguistics and Clinical Psychology (CLPsych) 2017 shared task collected from the Reachout.com forum. Posts were represented using lexicon-based tools, including Valence Aware Dictionary and sEntiment Reasoner, Empath, and Linguistic Inquiry and Word Count, and also using pretrained artificial neural network models, including DeepMoji, Universal Sentence Encoder, and Generative Pretrained Transformer-1 (GPT-1). We used Tree-based Optimization Tool and Auto-Sklearn as AutoML tools to generate classifiers to triage the posts. RESULTS: The top-performing system used features derived from the GPT-1 model, which was fine-tuned on over 150,000 unlabeled posts from Reachout.com. Our top system had a macroaveraged F1 score of 0.572, providing a new state-of-the-art result on the CLPsych 2017 task. This was achieved without additional information from metadata or preceding posts. Error analyses revealed that this top system often misses expressions of hopelessness. In addition, we have presented visualizations that aid in the understanding of the learned classifiers. CONCLUSIONS: In this study, we found that transfer learning is an effective strategy for predicting risk with relatively little labeled data and noted that fine-tuning of pretrained language models provides further gains when large amounts of unlabeled text are available.

**Решение:** -5 GPT-1 извлечение признаков для AutoML на CLPsych 2017; устаревшая негенеративная модель E5

---

### 186 · R7615

**Diagnostic capabilities of large language models in the detection of scaphoid fractures in the emergency department.**

2025 · Ulusal travma ve acil cerrahi dergisi = Turkish journal of trauma & emergency surgery : TJTES · journal article, observational study, study · eng · https://doi.org/10.14744/tjtes.2025.98680

ABSTRACT BACKGROUND: Scaphoid fractures account for 60%-70% of wrist traumas, with delayed diagnosis leading to avascular necrosis and functional impairment. Traditional radiographic assessment remains challenging due to anatomical complexity and overlapping structures. This study evaluated three next-generation large language models (LLMs) (ChatGPT-4o, Gemini 2.0, and Claude 3.5) for their ability to detect scaphoid fractures and determine surgical indications. METHODS: A retrospective observational study was conducted at Ankara Etlik City Hospital (October 2022 – January 2025) including 300 patients (150 with computed tomography confirmed (CT-confirmed) scaphoid fractures and 150 without fractures), aged 18-65 years, who presented to the emergency department (ED) with wrist trauma. Three-view wrist radiographs were presented to each LLM on three separate days. Diagnostic accuracy was assessed using overall accuracy (all three responses correct), strict accuracy (≥2 correct responses), and ideal accuracy (≥1 correct response). Response consistency was evaluated using Fleiss’ kappa coefficient. Surgical indications were determined based on fracture displacement criteria. RESULTS: Claude 3.5 demonstrated superior sensitivity (57.1%) compared to Gemini 2.0 (18.2%) and ChatGPT-4o (9.1%) for fracture detection (p<0.001). Ideal accuracy rates were 79.3%, 36.0%, and 17.3%, respectively. Specificity remained uniformly low across models (43.1%-43.8%). All models performed better in non-fracture cases, with ideal accuracy exceeding 83%. Response consistency was moderate for all models (κ=0.36-0.41). For surgical indication assessment, Claude 3.5 identified 37.0% of cases requiring surgery, compared to ChatGPT-4o (34.1%) and Gemini 2.0 (24.4%), with correct determination rates of 73.7%, 71.4%, and 80.0%, respectively. CONCLUSION: Current LLMs demonstrate insufficient diagnostic accuracy for independent clinical use in scaphoid fracture detection. Claude 3.5’s 57.1% sensitivity indicates that these technologies require substantial improvement before clinical deployment. However, their moderate performance in surgical decision-making suggests potential utility as assistive tools when combined with specialist expertise. Further development focusing on musculoskeletal-specific training is essential.

**Решение:** -4 травматология, рентгенография переломов ладьевидной кости

---

### 187 · R5545

**Empirical Evaluation of Automatic Speech Act Classification: From Logistic Regression to GPT-4o**

2026 · Corpus Pragmatics · article · en · https://doi.org/10.1007/s41701-026-00266-0

Abstract Speech act classification aims to assign communicative functions to utterances, a task that is central to understanding pragmatic aspects of language. Automating this process can substantially reduce the need for manual annotation, enabling large-scale pragmatic analysis. In this study, we evaluate different automatic classification approaches on the SPICE Ireland dataset. This dataset has been pragmatically annotated according to Searle’s taxonomy of illocutionary acts. We compare traditional machine learning models (, , and models), a fine-tuned RoBERTa language model, and GPT-4o using zero- and few-shot prompting. Finally, by fine-tuning GPT-4o, we achieve the best performance with an accuracy of 87% and a macro average F1-score of 66%. A qualitative analysis of disagreement cases further indicates that fine-tuned GPT-4o often produces predictions that align with expert judgments, suggesting that some disagreements between model predictions and reference labels may reflect annotation ambiguity or context sensitivity rather than clear model errors.

**Решение:** -4 лингвистика, речевые акты Серля в корпусе SPICE Ireland

---

### 188 · R8835

**Evaluating Syntactic Competence in Large Language Models: An Experimental Study of Island Constraints and Movement Dependencies**

2025 · International Journal of Research in English · article · en · https://doi.org/10.33545/26648717.2025.v7.i2c.449

This study investigates the extent to which large language models (LLMs), specifically GPT-4 and its contemporaries, exhibit syntactic competence by evaluating their understanding of island constraints and movement dependencies phenomena that are foundational in generative grammar. Despite the impressive surface fluency of these models, their grasp of underlying grammatical rules remains underexplored. This paper presents a controlled experiment involving a set of syntactic minimal pairs based on classic island phenomena such as wh-islands, adjunct islands, and complex NP constraints. A series of acceptability judgment and sentence completion tasks using both grammatical and ungrammatical constructions have been designed for this purpose. These are input into LLMs and the results are quantitatively compared with native speaker judgments collected via human surveys. The models' responses through preference metrics, perplexity scores, and error distribution are analyzed. Findings of the paper reveal significant mismatches between human and model judgments, particularly in contexts requiring sensitivity to hierarchical syntactic structure. While models show some probabilistic sensitivity to surface-level cues, they fail to robustly generalize abstract syntactic constraints like Subjacency and Relativized Minimality. The study contributes to ongoing discussions about the limits of statistical learning in language modeling and calls for a renewed integration of formal syntactic theory in NLP model evaluation.

**Решение:** -4 генеративная грамматика, синтаксические островные ограничения

---

### 189 · R5080

**Viewpoint Expert Annotation of AI Health Advice as Calibrated Measurement: Lessons from Experience for Rubric Design, Calibration, and Safety Evaluation (Preprint)**

2026 · preprint · https://doi.org/10.2196/preprints.104515

UNSTRUCTURED As large language models (LLMs) increasingly generate health advice, expert human annotation has become central to evaluating safety and constructing training datasets. Yet annotation itself is a noisy, multidimensional measurement task whose challenges remain underexamined. Drawing on our experience developing the MedExpert dataset, an expert-annotated collection of LLM-generated responses in mental health and prenatal care, we identify three core challenges: (1) inter-rater variability driven by underspecified constructs, calibration drift, and heuristic reasoning rather than substantive clinical disagreement; (2) consequential reasoning failures that conventional rubric categories (factuality, completeness) fail to capture, including miscalibrated urgency, misplaced reassurance, and absent triage logic; and (3) recursive interaction between model vulnerabilities and annotation instability. Mental health contexts intensify all three challenges: harm may be relational and behavioral rather than strictly biomedical, tone and framing become safety-relevant variables, and even technically accurate responses can worsen risk by invalidating experience or softening urgency. We propose rubric refinement, shared clinical mental models, and structured calibration as methodological interventions essential for detecting failures and generating robust datasets. Critically, these interventions rest on a conceptualization of expert clinical annotation as a noisy measurement process rather than a means of discovering ground truth. Applying this framing generates practical consequences for interpreting variability, designing rubrics, and building calibration infrastructure.

**Решение:** -1 эссе Viewpoint о разработке рубрик для ИИ-советов по здоровью

---

### 190 · R12250

**Orthopaedics and ChatGPT: correspondence**

2023 · International Orthopaedics · lettersandcomments, journalarticle, review · https://doi.org/10.1007/s00264-023-05909-4

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -1 письмо в редакцию, ортопедия

---

### 191 · R9969

**Solace, a Therapeutic Conversational Agent for Management of Chronic Pain: Acceptability and Usability Study**

2025 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/tgcn4_v1

Background: Chronic pain is a critical cause of personal suffering and societal concern. However, treatment options remain inadequate and access to efficacious treatment is limited by geography, economics, and scale. Digital health interventions for chronic pain are easily scaled solutions to this problem and autonomous conversational agents represent a new frontier in this treatment domain. Despite their potential impact, conversational agents powered by generative artificial intelligence (AI) have yet to be developed or examined for treatment of chronic pain. Objectives: We sought to develop and test Solace, a first-of-its-kind, expert trained generative AI conversational agent designed to deliver support grounded in principles of evidence-based pain psychology. Methods: We conducted an acceptability and usability study of Solace in a group of individuals with chronic pain. Participants (n=175) were recruited from Prolific, an online crowdsourcing platform, and interacted with Solace for 30 minutes. Self-report measures of system usability, treatment acceptability, and therapeutic alliance were completed after the interaction and clinically relevant pain related measures were completed before and after the interaction. Results: Participants rated the usability of Solace to be excellent (System Usability Scale mean = 85.04) and found it to be an acceptable intervention for chronic pain. Therapeutic alliance between participants and Solace was rated highly. Participants also demonstrated improvements in anxiety, pain interference, kinesiophobia, and pain resilience. Safety guardrails designed to identify and manage instances of suicidal ideation, injury, or requests for medication recommendations performed appropriately during the study. Solace is a usable and acceptable treatment for chronic pain that facilitates forming a strong therapeutic alliance with users. A single 30-minute conversation with Solace was also associated with improvements in several clinically relevant domains. Conclusion: Solace is a usable and acceptable expert trained generative AI conversational agent for pain management. Randomized clinical trials are needed to evaluate the efficacy of Solace as a strategy for the treatment of chronic pain.

**Решение:** -2 чат-бот Solace для хронической боли; пользователи оценивают юзабилити и терапевтический альянс

---

### 192 · R8063

**Quantum Computing in Cybersecurity and LLM**

2025 · International Conference on Web Research (ICWR) · conference, conference-paper · en · https://doi.org/10.1109/icwr65219.2025.11006202

Quantum computing is fundamentally transforming the cybersecurity landscape by simultaneously introducing robust defense mechanisms and sophisticated attack vectors. This paper explores the dual nature of quantum computing in cybersecurity, examining how it enhances artificial intelligence-powered malware detection systems and strengthens encryption protocols, while also enabling the development of adaptive quantum-enhanced threats such as polymorphic malware and quantum key distribution attacks. Additionally, the paper analyzes the convergence of quantum computing with Large Language Models (LLMs) and neural networks, highlighting implications for threat intelligence across social media platforms, cybersecurity operations, and open-source intelligence. Through comprehensive analysis and the proposition of quantum-resilient security frameworks, this research provides cybersecurity professionals with actionable strategies for navigating the emerging quantum computing era.

**Решение:** -4 кибербезопасность, квантовые вычисления

---

### 193 · R10780

**Towards Robust Multimodal Large Language Models Against Jailbreak Attacks**

2025 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2502.00653

While multimodal large language models (MLLMs) have achieved remarkable success in recent advancements, their susceptibility to jailbreak attacks has come to light. In such attacks, adversaries exploit carefully crafted prompts to coerce models into generating harmful or undesirable content. Existing defense mechanisms often rely on external inference steps or safety alignment training, both of which are less effective and impractical when facing sophisticated adversarial perturbations in white-box scenarios. To address these challenges and bolster MLLM robustness, we introduce SafeMLLM by adopting an adversarial training framework that alternates between an attack step for generating adversarial noise and a model updating step. At the attack step, SafeMLLM generates adversarial perturbations through a newly proposed contrastive embedding attack (CoE-Attack), which optimizes token embeddings under a contrastive objective. SafeMLLM then updates model parameters to neutralize the perturbation effects while preserving model utility on benign inputs. We evaluate SafeMLLM across six MLLMs and six jailbreak methods spanning multiple modalities. Experimental results show that SafeMLLM effectively defends against diverse attacks, maintaining robust performance and utilities.

**Решение:** -4 мультимодальная безопасность, защита от джейлбрейков

---

### 194 · R9370

**Exploring ChatGPT’s capabilities, stability, potential and risks in conducting psychological counseling through simulations in school counseling**

2025 · PsyArXiv · journalarticle, preprint/article, preprint · en · https://doi.org/10.31234/osf.io/6zqkr_v2

Citation: Ni, Y. and Cao, Y. (2025), "Exploring ChatGPT’s capabilities, stability, potential and risks in conducting psychological counseling through simulations in school counseling", Mental Health and Digital Technologies, Vol. ahead-of-print No. ahead-of-print. https://doi.org/10.1108/MHDT-02-2025-0013 Find published version at https://www.emerald.com/insight/content/doi/10.1108/MHDT-02-2025-0013/full/html Purpose This study aims to examine ChatGPT-4’s potential and stability when simulating school-counseling dialogues, offering an exploratory snapshot of its ability to convey warmth, empathy and acceptance. Drawing on 80 real student questions, this paper aims to assess response consistency and identify risk markers, such as randomness and hallucination. The goal of this study is to inform future research, guide human–AI (artificial intelligence) collaboration and support policy development on deploying large language model chatbots for accessible mental health interventions. Design/methodology/approach This paper prompted ChatGPT-4 with 80 authentic college student counseling questions and collected three nondeterministic replies per query. Automated analysis used three natural language processing (NLP) models – EmoRoBERTa for emotion detection, a neural network for empathy classification and VADER for sentiment analysis – to quantify warmth, empathy and acceptance. Stability was evaluated via Fleiss’ κ for empathy labels and ICC(2,1) for continuous sentiment scores. Additional Chi-square and one-way ANOVA tests examined categorical shifts and mean-score drift, and Pearson correlation assessed the relation between question and response length. Findings ChatGPT-4 achieved 97.5% warm responses, 94.2% empathy classification and a mean compound sentiment score of 0.93 ± 0.19. Stability metrics indicated moderate reliability (κ = 0.59; ICC = 0.62), while occasional confusing or realization labels (2.5% of outputs) and minor sentiment drift underscored randomness as a risk. A positive correlation (r = 0.60, p &lt; 0.001) revealed longer queries elicit longer replies. These results highlight both the promise and the limits of LLM chatbots in school-counseling simulations. Research limitations/implications As an offline simulation using a single GPT-4 model and automated proxies rather than clinician ratings or clinical outcomes, findings remain exploratory. The de-identified public data set may not capture live user dynamics. Future work should involve multi-model comparisons, mixed-methods validation with human raters and end-users, live pilot deployments and clinical trials to assess safety, usability and therapeutic impact in real-world educational settings. Practical implications High warmth and empathy rates suggest ChatGPT-4 could augment low-intensity support – drafting psycho-educational messages or after-hours coping tips under human oversight. Stability metrics can inform prompt-engineering benchmarks and guardrail triggers. Schools and self-help apps may pilot AI-assisted chat interfaces with escalation protocols, bias and privacy audits and human-in-the-loop triage to optimize counselor workflows, extend reach and mitigate risks through transparent policy and workflow design. Social implications Deployment of LLM chatbots can democratize mental health resources for youth, lowering barriers of cost, stigma and provider shortages. However, risks of misinformation, bias and overreliance necessitate digital-literacy education, equitable governance and community engagement frameworks. Policymakers and practitioners must balance innovation with safeguards – such as mandatory audit trails and accountability measures – to ensure vulnerable populations benefit safely from AI-mediated counseling. Originality/value This paper is among the first to apply quantitative stability metrics (κ, ICC) and NLP-based emotion analysis to ChatGPT-4 in a school-counseling simulation, enriched by a practitioner’s deployment insights. It integrates parasocial-interaction and computational social-science theories to link technical capabilities with design patterns, policy recommendations and a roadmap for future mixed-methods research on AI in mental-health interventions.

**Решение:** -5 ChatGPT в роли психотерапевта оценивался только автоматическими NLP-инструментами EmoRoBERTa/VADER без людей

---

### 195 · R8707

**Using Llama-3 to Refine Psychotherapy in Silico**

2025 · MPG.PuRe (Max Planck Society) · conference-paper

Psychotherapy is deeply personal and often time-intensive. Although therapeutic interactions crucially impact treatment outcomes, strategies to improve them often rely on trial and error, often resulting in a long and costly process with minimal improvement for the client. This project explores the potential of Large Language Models (LLMs) as low-risk, cost-effective tools for enhancing therapy. Using Llama-3, we simulated therapist-client dialogues, supervised by an expert LLM. The Expert LLM iteratively refined the Therapist LLM's responses, which were subsequently rated by the Client LLM. To extend this framework to real-world data, we applied LLM therapy revision to real therapy transcripts. For each segment of a recorded session, we compared the Client LLMs rating of the real therapist's last response to ratings of an LLM generated response and an LLM-based revision of the actual therapist's response, assessing satisfaction based on prior conversation context. These comparisons revealed that LLM-generated responses were often rated more favorably than human responses, with responses revised based on LLM feedback rated most favorably. This suggests that LLMs could meaningfully support and enhance therapeutic interactions, and improve quality of treatment.

**Решение:** -5 полностью in silico мультиагентная симуляция без разметки людьми

---

### 196 · R4723

**A Multi-Domain Human Expert Evaluation of Clinical and Behavioral Knowledge in Large Language Models**

2026 · 2026 6th International Conference on Electrical, Computer and Energy Technologies (ICECET) · conference · https://doi.org/10.1109/icecet65726.2026.11632464

Large Language Models (LLMs) such as ChatGPT and Gemini are increasingly used to answer medical and psychological questions, yet systematic evaluations across domains with differing reasoning demands remain limited. We present a multi-domain expert evaluation of two state-of-the-art models, ChatGPT Pro (v5.2) and Gemini 3 Pro, across three healthcare domains: Gynecology, Pathology, and Psychology. We curated 300 open-ended, realistic questions, 100 per domain, designed to elicit clinical reasoning, mechanistic interpretation, and conceptual explanation. Responses were independently scored by domain experts using a standardized five-point rubric. Results reveal domain-dependent performance patterns, with both models performing well in guideline-aligned advisory tasks in Gynecology, lower in mechanistic diagnostic contexts in Pathology, and showing divergent strengths in conceptual psychology questions. Quantitative and qualitative analyses highlight recurring limitations in contextual nuance, mechanistic depth, and safety framing. These findings underscore the importance of domainstratified evaluation and expert oversight when deploying LLMs for healthcare information and provide a reproducible framework for future assessments.

**Решение:** -2 эксперты оценивают ответы LLM на экзаменационные вопросы по гинекологии, патологии, психологии

---

### 197 · R3836

**Operationalizing six model-generated sleep-EEG predictions: a case study of measurement and feasibility limits**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, preprint · en · https://doi.org/10.5281/zenodo.23227116

Language models can write research hypotheses much faster than anyone can test them. Earlier studies have judged such hypotheses by expert ratings, benchmarks with known answers or laboratory experiments. We report a small, fully documented case study of operationalization: what happens to a handful of model-generated predictions when they are turned into prespecified numerical tests on public data. We tested six operationalized sleep-EEG predictions selected from archived GLM-5.3 outputs, which supplied no bibliographic citations for those predictions. Before this study downloaded its data we froze a pre-analysis protocol in version control, with pass and refutation thresholds, controls and a label hierarchy; it was not deposited in a public registry, and the author had seen hypnograms and some EEG of the main dataset in an earlier, unrelated analysis (section 6). The main data were Sleep-EDF Expanded (Sleep Cassette, 78 healthy people, night 1); the Dreem DOD-H dataset (25 people, five independent scorers) was planned for scorer-agreement controls. Two hypotheses met their prespecified refutation condition. For the prediction that spindle-band (12 to 16 Hz) bursts become more frequent in the last ten minutes of wake before the first N2 epoch, the median burst-rate ratio in 25 people was 0.71, below the refutation threshold of 1.2. This meets the prespecified refutation rule on the point median, but the 95% interval (0.19 to 1.35) includes 1.2, so it is not a firm disproof. For the prediction that spindle amplitude grows with the time since the previous spindle, the median amplitude ratio in 77 people was 0.99 (95% CI 0.97 to 1.01) and the median Spearman rho was -0.04. Because amplitude also decided which spindles our threshold detector counted, this applies to the detected spindles only. A second amplitude measure added in version 0.8 (matching pursuit), fixed in an internal protocol before the re-analysis except for its atom selection rule, also failed (median ratio 1.05; median rho 0.01, CI -0.003 to 0.033); because the sign of the median rho changed with the measure, a detection-threshold artefact remains possible. Three hypotheses were not decided because the sample minimum was not met after event-level qualification (17 and 12 people against 20; 1 record against 100); the model's fixed -75 µV amplitude rule, applied to the negative peak of the bipolar Fpz-Cz derivation, may have contributed to this attrition, which we did not test. One could not be tested, because no dataset we audited provides bilateral leg EMG in enough healthy sleepers. No hypothesis passed. In our experience (a qualitative observation; effort was not measured), most of the effort went into turning each hypothesis into a decidable rule, and on standard open sleep data four of the six ended undecided rather than true or false. Several of the underlying mechanisms have published antecedents, which we compare with each prediction. This version reports only synthetic checks of the event detectors and no external validation, so the ability of the tests to detect a real effect was not established. The study does not estimate the accuracy of LLM-generated hypotheses or establish that the underlying physiological ideas are new. It is not a clinical study. Version 0.8.1. Version 0.8.1 changes only the text of the report: it adds two published studies on amplitude thresholds for slow waves (Davidson et al. 2025; Wunderlin et al. 2022) to sections 4.4 and 6 and writes the author name in full (report, Table A2). No code, protocol, result file or label changed; apart from README.md, LICENSE.md, NOTA/MANIFEST_ARTEFACTS.md and SHA256SUMS.txt, every other file in the ZIP archive is byte for byte that of the version 0.8 archive (manifest, section 11). Files. Kulma_2026_D1_Sleep_LLM_Hypotheses_v0.8.1.pdf is the report. The ZIP archive contains the report in Markdown, the pre-analysis protocol with its history and deviations ledger, the analysis code with unit tests, result files, aggregation scripts, provenance of the generated hypotheses, the AI review rounds, a manifest linking each claim to its supporting file, licences and data attribution, a short guide to reproduction (README.md) and SHA-256 checksums. No recordings or hypnograms are redistributed. Some supporting notes are in Polish. Use of AI tools. The hypotheses were generated by GLM-5.3; the analysis code and drafts of the text were written with Claude Code (Anthropic) under the author's direction; OpenAI Codex, Google Antigravity and GLM-5.3 were used for review and pre-release checks. These automated reviews do not replace review by a sleep electrophysiologist; no sleep electrophysiologist has read this report yet. AI tools are not authors; the author takes responsibility for all content (report, section 8). Preprint, not peer reviewed. Text and results: CC BY 4.0; raw model output: CC0 1.0; code: MIT. Datasets keep their own licences (see LICENSE.md).

**Решение:** -4 нейрофизиология, проверка гипотез по числовым данным ЭЭГ сна

---

### 198 · R7805

**Comparative analysis of AI and expert evaluations in engineering design pedagogy.**

2025 · PloS one · comparative study, research-article, journal article · eng · https://doi.org/10.1371/journal.pone.0332715

BACKGROUND: Integrating engineering design processes into science education has become a significant priority in STEM instruction. However, many science teachers face difficulties incorporating these processes due to limited pedagogical expertise. Generative artificial intelligence (GAI) tools such as ChatGPT offer potential support mechanisms by evaluating lesson plans and providing formative feedback. This study investigates the reliability and validity of GAI evaluations compared to expert assessments. METHODS: This mixed-methods study involved 43 science teachers who received professional development over four months to integrate engineering design into their lesson plans. A total of 52 lesson plans were evaluated using structured and unstructured prompts via ChatGPT 4.5, alongside evaluations by expert mentors. Quantitative data were analyzed using the Intraclass Correlation Coefficient (ICC) and Bland-Altman methods to assess inter-rater consistency. Qualitative data was analyzed through open and deductive coding to interpret differences in evaluation rationale. RESULTS: Findings revealed high consistency between structured prompt AI evaluations and expert assessments (ICC = 0.708), while unstructured prompts showed low and non-significant agreement (ICC = 0.076). Qualitative analysis indicated that AI evaluations, particularly those using structured prompts, tend to be more positive and holistic, whereas experts offered more detailed and critical feedback. Differences were also observed in evaluating dcomponents like problem definition, testability, and interdisciplinary integration. CONCLUSION: Structured AI prompts offer reliable and valid evaluation results comparable to expert assessments and could serve as scalable tools in teacher support systems. However, unstructured prompts produce inconsistent outcomes and require refinement. The study highlights both the potential and limitations of using GAI tools for pedagogical evaluation in STEM education.

**Решение:** -4 педагогика, оценка планов уроков STEM

---

### 199 · R5908

**The Fragility Of Moral Judgment In Large Language Models**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2603.05651

People increasingly use large language models (LLMs) for everyday moral and interpersonal guidance, yet these systems cannot interrogate missing context and judge dilemmas as presented. We introduce a perturbation framework for testing the stability and manipulability of LLM moral judgments while holding the underlying moral conflict constant. Using 2,939 dilemmas from r/AmItheAsshole (January-March 2025), we generate three families of content perturbations: surface edits (lexical/structural noise), point-of-view shifts (voice and stance neutralization), and persuasion cues (self-positioning, social proof, pattern admissions, victim framing). We also vary the evaluation protocol (output ordering, instruction placement, and unstructured prompting). We evaluated all variants with four models (GPT-4.1, Claude 3.7 Sonnet, DeepSeek V3, Qwen2.5-72B) (N=129,156 judgments). Surface perturbations produce low flip rates (7.5%), largely within the self-consistency noise floor (4-13%), whereas point-of-view shifts induce substantially higher instability (24.3%). A large subset of dilemmas (37.9%) is robust to surface noise yet flips under perspective changes, indicating that models condition on narrative voice as a pragmatic cue. Instability concentrates in morally ambiguous cases; scenarios where no party is assigned blame are most susceptible. Persuasion perturbations yield systematic directional shifts. Protocol choices dominate all other factors: agreement between structured protocols is only 67.6% (kappa=0.55), and only 35.7% of model-scenario units match across all three protocols. These results show that LLM moral judgments are co-produced by narrative form and task scaffolding, raising reproducibility and equity concerns when outcomes depend on presentation skill rather than moral substance. 22 pages, 7 figures, 10 tables, plus appendices

**Решение:** -5 моральные суждения на r/AmItheAsshole оценивались только между протоколами LLM без человеческой разметки

---

### 200 · R11125

**FUTBOL MAÇ ANLATIMLARINDAKİ ORTA AÇMA EYLEMLERİNİN BÜYÜK DİL MODELLERİ KULLANILARAK OTOMATİK ANALİZİ**

2024 · OpenMETU (Middle East Technical University) · dissertation · https://open.metu.edu.tr/bitstream/handle/11511/109440/Anıl_Erkul_Thesis.pdf

In football, well-executed crosses have a significant impact, directly creating about 15% of scoring opportunities in the top leagues of England, Italy, and France. This thesis focuses on the development of a comprehensive dataset sourced from the in-depth analysis of football commentary extracted from the English Premier League matches spanning the 2022-2023 Football season. The main goal is to gather and organize key details related to crossing actions. This involves collecting diverse information, such as the outcome of each cross, identifying the team and the player making the cross, and evaluating the sentiment or qualitative aspects of the executed crosses with human annotators. In the second phase of the thesis, large language models are used and fine-tuned to automatically identify, extract, and describe instances of crossing actions, along with their related details, in the extensive football commentary from Premier League matches. The results indicate that the large language models are useful to reveal crossing actions successfully.

**Решение:** -4 турецкая диссертация по футбольным комментариям

---

### 201 · R11187

**Can children and artificial intelligence be sources of ideas for school meal preparations based on whole food utilization?**

2024 · Food Quality and Preference. · journal article, agr, article · eng · https://doi.org/10.1016/j.foodqual.2024.105349

Involving children in creation of school meals is important to engage them on healthy and sustainable eating habits, and the whole food utilization is a way to avoid food waste and increase the consumption of nutrients. Also, artificial intelligence (AI) has shown to be an interesting source of new ideas but has not been used for designing children’s meals. The aims of the work were to evaluate the potential of school meals either co-designed by children or generated with AI, and to explore parents’ perception towards the utilization of whole food in their children’s meal. Children, with the potential support of their parents, proposed recipes with whole fruit/vegetable utilization, and a selection among the suggestions was conducted by nutritionists and the school cooks. The selected meal was compared to a similar recipe from ChatGPT generated from a simple prompt with regard to their acceptance and emotions evoked. The two dishes were variations of carrot pie recipes including vegetable peel and were both prepared by experienced school cooks. A third recipe proposed by the school’s cooks was used as comparison. Parents’ perceptions towards whole food utilization to their children were elicited by sentence completion methodology. Results showed that children liked both their and the cooks’ recipes but rejected ChatGPT’s recipe. Both cooks’ and children’s carrot pies evoked positive emoji pairs, meanwhile ChatGPT’s carrot pie was associated to emojis of negative connotation. Texture and unfamiliar taste were cited to justify the rejection. For parents, the utilization of whole fruits/vegetable in children’s meals is perceived as a good and nutritious idea, but safety concerns were revealed. This work demonstrates co-design with school children and whole food utilization as actionable strategies towards reducing waste of nutritious resources. Moreover, the study reports an unsuccessful exploratory usage of ChatGPT through a task-focused prompt. This may suggest the importance of specifying the context of the task when prompting an AI, to compensate for contextual information that is implicitly available to humans. Concerns about safety aspects should be addressed to ensure parents’ support for whole vegetable utilization in school meals.

**Решение:** -4 кулинарные рецепты для школьного питания

---

### 202 · R4638

**Spoiler Alert: Narrative Forecasting as a Metric for Tension in LLM Storytelling**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2604.09854

LLMs have so far failed both to generate consistently compelling stories and to recognize this failure--on the leading creative-writing benchmark (EQ-Bench), LLM judges rank zero-shot AI stories above New Yorker short stories, a gold standard for literary fiction. We argue that existing rubrics overlook a key dimension of compelling human stories: narrative tension. We introduce the 100-Endings metric, which walks through a story sentence by sentence: at each position, a model predicts how the story will end 100 times given only the text so far, and we measure tension as how often predictions fail to match the ground truth. Beyond the mismatch rate, the sentence-level curve also yields complementary statistics that track plot-level twists and revelations, such as the inflection rate, a geometric measure of how frequently the curve reverses direction. Unlike rubric-based judges, 100-Endings correctly ranks New Yorker stories far above LLM outputs. Grounded in narratological principles, we design a story-generation pipeline using structural constraints, including analysis of story templates, idea formulation, and narrative scaffolding. Our pipeline significantly increases narrative tension as measured by the 100-Endings metric, while maintaining performance on the EQ-Bench leaderboard. COLM2026 Camera Ready. 44 pages, 10 figures, 30 tables

**Решение:** -4 литературоведение, нарративное напряжение в художественных текстах

---

### 203 · R1245

**Open Benchmark of AI Impact on Humans (ImpactBench): an expert-guided, open platform for the holistic evaluation of AI impact on humans**

2026 · arXiv (Cornell University) · preprint/article, review, preprint · https://doi.org/10.48550/arxiv.2610.20690

The present work is concerned with how to measure, at scale, the multi-dimensional impact of generative AI models on the individuals who use them. In service of this goal, we introduce the Open Benchmark of AI Impact on Humans, or ImpactBench. Our iterable and expert-guided platform evaluates whether model behaviors support or undermine an individual's wellbeing across psychological, physical, and social domains. ImpactBench translates constructs from domain experts and existing benchmarks into metrics that are grounded in actual model behavior. Success on these metrics occurs either when a model promotes expert-defined desirable behaviors or avoids identified harms. Models are evaluated against these metrics in simulated multi-turn conversations using matched teen and adult scenarios. The conversations are then scored by an LLM judge and verified through reliability audits and human expert review. The current suite delivers 809 metrics drawn from 26 benchmarks. We evaluated ten frontier LLMs against these metrics across 48,540 conversations. Our results indicate that models promoted desirable behaviors in 68.7% of evaluations, but avoided harms in only 53.1%. Majority expert ratings agreed with the automated judge in 83.3% of reviewed cases (Cohen's Kappa = 0.667). Results are released through a public platform that keep aggregate scores traceable to the underlying metrics and transcripts. ImpactBench is intended as evolving infrastructure for independent, transparent evaluation of generative AI's multi-dimensional impact on humans.

**Решение:** + T4 ImpactBench: LLM-судья оценивает безопасность и благополучие в диалогах помощи, согласие с экспертами 83.3%, κ=0.667

---

### 204 · R6006

**A Survey on AI-Based Answer Sheet Evaluation and Result Management Systems**

2026 · International Journal of Advanced Research in Science Communication and Technology · journalarticle, review, article · https://doi.org/10.48175/ijarsct-32022

Artificial Intelligence (AI) in teaching can transform traditional methods of assessment, particularly the methods of evaluation of the descriptive and open-ended responses of the students. Large language models (LLMs) can read, interpret and generate text in a human-like way, which means that automated grading systems can be both more scalable and objective than in the past when it was performed by human evaluators. Beyond accuracy, transparent, reliable and capable of producing actionable feedback post in accordance with pedagogical standards, many LLMs offer a black box design, which can actively raise concerns about fairness, interpretability and transparency, and the cost/benefit balance of processing speed and analytical depth can limit learners and institutions in their use. An emerging solution, which is the focus of a review in the present paper, is dual-process LLM frameworks of automated assessment. These hybrid systems are a combination of a bigger, more complex system that would perform more comprehensive rubric-based assessment and a system that would make detailed feedback with a slightly small model which could be used to score first assessments fast. To provide researchers and educators with a comprehensive outline of the development of reliable and efficient AI-powered assessment devices.

**Решение:** -1 обзор автоматической проверки экзаменационных работ

---

### 205 · R8449

**Unsupervised Extractive Summarization of Psychedelic User Experience Reports**

2025 · medRxiv · preprint, ppr · en · https://doi.org/10.1101/2025.08.22.25334176

A bstract Contemporary psychedelic research highlights the value of user experience reports, yet their verbose, subjective nature poses challenges for clinical utility. This is the first study to pioneer unsupervised automatic text summarization of psychedelic user experience reports, a domain where no human-annotated reference summaries exist. To address this gap, we developed a custom scoring function that integrates semantic coverage, narrative coherence, and a novel experiential preservation metric, enabling effective model training and hyperparameter tuning. We utilized three established extractive methods: LexRank, LSA with HDBSCAN clustering, and SBERT with Maximal Marginal Relevance, on 1,200 reports involving LSD, psilocybin, and DMT. Using GPT-4 as a calibrated rater under a structured rubric, supplemented by TOPSIS aggregation, results showed LexRank achieving the highest overall balance with SBERT excelling in content coverage and experiential depth but lagging in coherence. Our findings revealed trade-offs between content richness and narrative fluency, with performance varying across substance types due to differences in narrative structure and phenomenology. Limitations included reliance on extractive methods, lack of reference data, and sensitivity to scoring design. Future work should extend to abstractive methods, alternative weighting schemes, and expert adjudication to develop clinically usable summarization systems for psychedelic science.

**Решение:** -5 неконтролируемая суммаризация трип-репортов; прямо указано отсутствие эталонных суммаризаций людей

---

### 206 · R0243

**Role of artificial intelligence in analyzing human behavior and predicting personality traits and personality disorders.**

2026 · Scientific reports · journal article, journalarticle, article · eng · https://doi.org/10.1038/s41598-026-51371-8

Traditional approaches to the diagnosis of personality disorders, including a clinical interview and a self-report, are usually limited by subjectivity and time constraints. Recent developments in artificial intelligence have opened the possibility of more objective and data-driven psychological testing. This paper introduces an AI-powered system that forecasts personality disorders using natural language processing (NLP), speech recognition, and face recognition. The suggested method should help with the initial diagnosis and more tailored mental health solutions. Two benchmark datasets were used: myPersonality for text analysis and DAIC-WOZ for multimodal analysis of speech and facial expressions. The feature extraction methods were TF-IDF, Vader sentiment scores, Mel-Frequency Cepstral Coefficients, prosodic features, facial action units, and gaze tracking. BiLSTM, CNN, BERT, and GPT-3 models were analyzed through accuracy, precision, recall, F1 score, and AUC-ROC. GPT-3 was the most accurate at 89.1%, followed by BERT at 87.4% and CNN-based facial analysis at 85.6%. The findings indicate that multimodal fusion improves classification by leveraging holistic and complementary behavioral information. These results support the promise of multimodal systems with AI capabilities to make more precise predictions of personality disorders and underscore the need to consider interpretability, fairness, and data privacy in future applications. It should be mentioned that the current study deals with the problem of both normal personality traits prediction (through the Big Five framework) and features that can reflect psychological distress and be related to personality disorders. The myPersonality data set measures normative personality dimensions, whereas the DAIC-WOZ data set measures multimodal behavioral data that is relevant in clinical terms. The paper explains the connections between extreme trait profiles and clinical personality disorders to reconcile the paradigms of trait and disorder assessment.

**Решение:** -3 критериальная валидность: предсказание BFI по myPersonality и PHQ-8 по DAIC-WOZ

---

### 207 · R6631

**Towards a Unified Model for Evaluating Respect and Empathy in Dialogues**

2026 · Institutional Repositories DataBase (IRDB) · article · en · https://kyutech.repo.nii.ac.jp/record/2002714/files/10478337.pdf

Empathy and respect are central social-affective dimensions of dialogue that influence perceived service quality, yet prior studies have typically modelled them in isolation using separate datasets and evaluation metrics. This work addresses this limitation by jointly modelling empathy and respect and by introducing an explicit metric for their combined expression in service dialogues. We construct two complementary dialogue datasets by assigning respect labels to an empathy-annotated corpus and empathy labels to a respect-annotated corpus using a large language model, and we train both single-task and multi-task classifiers on these data. To evaluate joint social quality, we propose the Respect--Empathy Index (RE-index), which measures the proportion of responses that simultaneously satisfy minimal criteria for empathy and respect. Experiments on the two datasets reveal a clear asymmetry. On the respect dataset, multi-task learning with human-annotated respect labels and LLM-generated empathy labels substantially improves empathy performance, while preserving respect performance. In contrast, on the empathy dataset, multi-task learning with highly imbalanced LLM-generated respect labels degrades empathy performance. Furthermore, we observe that high classification scores for individual dimensions do not necessarily translate into high joint scores: in some settings, the predicted RE-index is less than half of the gold value. These results indicate that joint modelling is sensitive to the reliability and distribution of auxiliary labels, and that multi-dimensional evaluation metrics such as RE-index are necessary for analysing dialogue systems that aim to capture both empathic and respectful behaviour.

**Решение:** -4 клиентский сервис, аугментация диалогов

---

### 208 · R3831

**Functional Validation of a Generative AI-Based Mobile App for Assessing Speech Difficulties in Children**

2026 · International Journal of Interactive Mobile Technologies (iJIM) · journalarticle, article · https://doi.org/10.3991/ijim.v20i01.57991

Speech and voice development in childhood are essential for academic progress and social participation; difficulties in oral expression may impact learning and emotional health. Generative artificial intelligence (GAI) technologies integrated into interactive mobile applications offer new possibilities for the automated assessment of Spanish-speaking children’s speech. This study functionally validates a mobile application that uses GAI to automatically assess children’s speech fluency, pronunciation, and intonation, providing automated scoring, targeted feedback, and personalized recommendations. This Phase 1 functional validation, based on synthetic data, lays the groundwork for a four-phase framework aimed at guiding cross-national and multilingual research in artificial intelligence (AI)-supported speech evaluation. The methodology focused on a correlational analysis between the scores generated by the application and the acoustic indicators—number of pauses, pitch range, and spectral clarity—obtained from 160 samples. Descriptive and spectrographic analyses revealed mean decibel levels ranging from 15 to 33 dB, pitch ranges around 3.843 Hz, and spectral clarity between 0.033 and 0.036. It is concluded that this tool could contribute to the automated and multidimensional assessment and feedback of speech difficulties in Spanishspeaking children.

**Решение:** -4 акустический анализ детской речи: высота тона, децибелы, паузы

---

### 209 · R4951

**Comparing LLM and Human Expert Responses to Problem Gambling Questions**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-12313-8_17

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? ответы на проблемный гемблинг LLM vs эксперты; нет аннотации, проверить дизайн

---

### 210 · R6152

**Global Sentiment Toward Health AI at the Dawn of the ChatGPT Era: Empirical Analysis of Twitter (X) Discourse.**

2026 · Journal of medical Internet research · journal article, journalarticle, review · eng · https://doi.org/10.2196/80346

Background Artificial intelligence (AI) is increasingly proposed for use in health and health care systems. Beyond technical performance, public perceptions and affective responses influence whether AI technologies are accepted and adopted in real-world contexts. Social media platforms such as X (formerly Twitter) provide large-scale, real-time insight into public discourse surrounding emerging technologies, yet remain underused for examining how health AI is discussed, evaluated, and emotionally framed. Objective This study aimed to develop and apply large language model (LLM)–based methods for exploratory social listening on health AI. This is the first study to map large-scale sentiment, emotional expressions, and confidence-related signals in online discussions of applications of AI to health. Methods We collected 786,750 English-language posts from X (Twitter) published between January 1 and December 5, 2023, using health- and AI-related keywords. We benchmarked an LLM-based annotation framework by using OpenAI’s GPT-3.5-Turbo and GPT-4, comparing model classifications with trained human researchers. Annotations included overall sentiment and 6 evaluative domains frequently referenced in the literature surrounding attitudes toward health AI—usefulness, safety, privacy, ethics, quality, and trust. After cleaning, GPT-3.5-Turbo used the best-performing prompts to label 388,009 posts. A subset (n=268,347) was further analyzed using Emollama-7b, an open-source model fine-tuned from Meta’s LLaMA2-7B, for emotion detection, and latent Dirichlet allocation for thematic analysis. Comparisons were made across World Health Organization regions. Results Compared against human annotations, optimized prompts achieved weighted F1-scores above 0.60 across evaluative domains and sentiment classification. Global discourse about health AI was 65.26% (95% CI 65.11%-65.4%) positive and 83.62% (95% CI 83.48%-83.76%) emotionally optimistic, although substantial regional variation was observed in sentiment (P<.001). The Eastern Mediterranean and South-East Asia regions expressed significantly higher levels of positive sentiment and evaluative agreement in the studied features of health AI, alongside frequent discussion of the tech industry and commercial development. In comparison, the Western Pacific region expressed lower confidence and significantly more mentions of research topics (19.27%, 95% CI 18.5%-20.07%). Privacy was the most prominent global concern, with 33.31% (95% CI 32.98%-33.66%) of privacy-related posts expressing perceived risks. In the Region of the Americas, 18.19% (95% CI 17.92%-18.44%) of posts discussed algorithms and data governance, significantly higher than overall. Conclusions This study offers the first systematic characterization of online health AI discourse at scale, mapping stances toward key features of AI, emotional tone, and discussion topics across regions. LLM-powered social listening is demonstrated as a feasible approach for identifying dominant narratives and regionally distinct concerns, capable of surfacing opinions absent from traditional media. This can extend to studying discourse on other evolving health technologies where public surveying is limited. While methodological refinement and multilingual expansion are needed, this framework can inform timely policy development, risk communication, and responsible health AI governance.

**Решение:** -4 дискурс в Twitter об ИИ в медицине

---

### 211 · R2920

**A Multi-Agent Audit Framework for High-Stakes Reasoning: Evaluation and Interpretability in Clinical Mental Health Screening**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.21123

High-stakes reasoning tasks necessitate transparent and verifiable workflows, yet conventional single-model large language models (LLMs) often struggle with hallucination and low interpretability under zero-shot paradigms. To address this general AI challenge, we propose a Multi-Agent Audit Framework that simulates a collaborative, multi-step verification process. We empirically validate this architecture in the sensitive domain of clinical mental health screening using a modular LangChain workflow. Our framework decomposes the reasoning process into a Perception Agent, Knowledge Retrieval-Augmented Generation (RAG), Chain-of-Thought (CoT) clinical inference, and a critical Audit verification stage. We evaluated this framework on the DAIC-WOZ dataset using locally deployed open-source models. Experimental results demonstrate that our multi-agent pipeline significantly outperforms single-agent baselines, reducing the Mean Absolute Error (MAE) for PHQ-8 depression severity prediction from 5.35 to 5.02. By exposing cross-agent validation traces, the framework mitigates reasoning drift and provides highly interpretable diagnostic rationales, offering a generalizable paradigm for reliable AI-assisted decision support beyond isolated model scaling. We make data and code open access on GitHub for replicability.

**Решение:** -3 критериальная валидность: регрессия баллов опросника PHQ-8 по DAIC-WOZ, MAE

---

### 212 · R1032

**PHASE-Tree: Modeling Character-State Evolution in Long-Horizon Role-Playing Dialogue**

2026 · arXiv (Cornell University) · preprint/article, preprint · https://doi.org/10.48550/arxiv.2608.06975

Long-horizon role-playing demands that characters remain recognizable as they evolve with the narrative. Yet existing work falls short on two fronts: representations are typically static profiles that cannot be updated locally without destabilizing unchanged traits, and benchmarks mainly test persona preservation and memory recall rather than whether a model speaks from a character's currently evolved state. We address both. PHASE-Tree is a multi-timescale character-state tree with an immutable identity root and mutable persona, session, and moment layers, making each mutable field an addressable target for localized within- and cross-episode updates. It conditions generation through explicit textual provision or implicit parametric adaptation. To measure evolved-state generation, we introduce LongEvoRoleBench, which pairs four long-dialogue corpora for cross-episode evolution with four short-dialogue corpora as within-scene state-tracking checks, under a unified next-utterance protocol. On the long-dialogue core, textual PHASE-Tree ranks first in 11 of 12 dataset-metric cells against internal variants and all 12 cells against external textual baselines, improving character-level, semantic, and embedding scores by 19.7%, 12.4%, and 15.1% respectively. In a blinded 200-response study, human ratings correlate with the GPT-4.1 judge (Pearson r= 0.65); on descriptive n= 10 PT and NR prompt subsets, the Overall difference is +0.20. The long-dialogue Sem advantage persists across LLM judges and generation backbones.

**Решение:** -4 видеоигры, эволюция состояний персонажей в RPG

---

### 213 · R11633

**Use of large language model-based chatbots in managing the rehabilitation concerns and education needs of outpatient stroke survivors and caregivers.**

2024 · Frontiers in digital health · journal article, journalarticle, review · eng · https://doi.org/10.3389/fdgth.2024.1395501

Background: The utility of large language model-based (LLM) artificial intelligence (AI) chatbots in many aspects of healthcare is becoming apparent though their ability to address patient concerns remains unknown. We sought to evaluate the performance of two well-known, freely-accessible chatbots, ChatGPT and Google Bard, in responding to common questions about stroke rehabilitation posed by patients and their caregivers. Methods: We collected questions from outpatients and their caregivers through a survey, categorised them by theme, and created representative questions to be posed to both chatbots. We then evaluated the chatbots' responses based on accuracy, safety, relevance, and readability. Interrater agreement was also tracked. Results: Although both chatbots achieved similar overall scores, Google Bard performed slightly better in relevance and safety. Both provided readable responses with some general accuracy, but struggled with hallucinated responses, were often not specific, and lacked awareness of the possibility for emotional situations with the potential to turn dangerous. Additionally, interrater agreement was low, highlighting the variability in physician acceptance of their responses. Conclusions: AI chatbots show potential in patient-facing support roles, but issues remain regarding safety, accuracy, and relevance. Future chatbots should address these problems to ensure that they can reliably and independently manage the concerns and questions of stroke patients and their caregivers.

**Решение:** -2 клиницисты оценивают ответы чат-бота по реабилитации после инсульта

---

### 214 · R3416

**From Perceptions to Predictions: A Mixed-Method Study of Supplier-Related Reputational Risks and Large Language Model Performance**

2026 · SSRN Electronic Journal · preprint · https://doi.org/10.2139/ssrn.7006267

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 цепочки поставок, репутационные риски поставщиков

---

### 215 · R2339

**CoRe-DoS: Inference-time denial-of-service attack against retrieval-augmented generation**

2026 · Computer Networks · article · en · https://doi.org/10.1016/j.comnet.2026.112567

Retrieval-Augmented Generation (RAG) technology significantly mitigates the hallucination problem in large language models by integrating external knowledge bases, but its distributed architecture also introduces new security risks. Existing research on attacks against RAG systems primarily focuses on knowledge poisoning, which directly contaminates external knowledge bases and requires attackers to have permission to modify the knowledge base. However, these methods overlook the interceptability of retrieved context during the inference phase of RAG systems, leaving the inference-time attack vector insufficiently explored. To address this issue, this paper proposes CoRe-DoS, an inference-time denial-of-service attack framework for retrieval-augmented generation. Rather than poisoning the knowledge base, this framework intercepts and manipulates retrieved context during inference, exploiting the instruction-following characteristics and position bias of large language models to induce the model to refuse answering legitimate queries. Meanwhile, it introduces a black-box capacity inference mechanism and an instruction-preserving compression mechanism to ensure the integrity of attack payloads under unknown context window constraints. Experimental results demonstrate that CoRe-DoS achieves attack success rates ranging from 84.6% to 100% across two benchmark datasets and multiple mainstream models, significantly outperforming baseline methods. It also maintains relatively high effectiveness under mainstream defense mechanisms, including perplexity filtering, document rewriting, knowledge expansion, and a RAGuard-style composed defense.

**Решение:** -4 DoS атаки на RAG

---

### 216 · R9536

**Detecting New Lesions Using a Large Language Model: Applications in Real-World Multiple Sclerosis Datasets.**

2025 · Annals of neurology · journal article, article, research-article · eng · https://doi.org/10.1002/ana.27251

OBJECTIVE: Neuroimaging is routinely utilized to identify new inflammatory activity in multiple sclerosis (MS). A large language model to classify narrative magnetic resonance imaging reports in the electronic health record (EHR) as discrete data could provide significant benefits for MS research. The objectives of the current study were to develop such a prompt and to illustrate its research applications through a common clinical scenario: monitoring response to B-cell depleting therapy (BCDT). METHODS: An institutional ecosystem that securely connects healthcare data with ChatGPT4 was applied to clinical MS magnetic resonance imaging reports in a single institutional EHR (2000-2022). A prompt (msLesionprompt) was developed and iteratively refined to classify the presence or absence of new T2-weighted lesions (newT2w) and contrast-enhancing lesions (CEL). The multistep validation included evaluating efficiency (time and cost), comparison with manually annotated reports using standard confusion matrix, and application to identifying predictors of newT2w/CEL after BCDT start. RESULTS: Accuracy of msLesionprompt was high for detection of newT2w (97%) and CEL (96.8%). All 14,888 available reports were categorized in 4.13 hours ($28); 79% showed no newT2w or CEL. Data extracted showed expected suppression of new activity by BCDT (>97% monitoring magnetic resonance images after an initial "rebaseline" scan). Neighborhood poverty (Area Deprivation Index) was identified as a predictor of inflammatory activity (newT2w: OR 1.69, 95% CI 1.10-2.59, p = 0.017; CEL: OR 1.54, 95% CI 1.01-2.34, p = 0.046). INTERPRETATION: Extracting discrete information from narrative imaging reports using an large language model is feasible and efficient. This approach could augment many real-world analyses of MS disease evolution and treatment response. ANN NEUROL 2025;98:308-316.

**Решение:** -4 радиология, очаги рассеянного склероза на МРТ

---

### 217 · R0834

**NEUROBALANCE: A PRISMA-ScR Scoping Review of Domain-Specific Neuron Activation and Sparse Computation in Multimodal Large Language Models**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/maz5g

AUTHORS Austin Olom Ogar¹, Prof. Joshua Abah¹, Aliyu Suleiman Muhammed¹, Oluwatobi Noah Akande¹, Faruk Obansa Muhammed ¹ ¹Department of Computer Science, Faculty of Computing, Nile University of Nigeria, Abuja BACKGROUND &amp; RATIONALE Multimodal Large Language Models (MLLMs) demonstrate impressive general capabilities but underperform in precision-critical domains such as medical diagnostics and autonomous systems. This decline is driven by the dense-by-default activation paradigm that compels full network activation regardless of task specificity, resulting in inefficient neuron utilisation, catastrophic forgetting, and attention collapse. While individual studies have explored adaptive attention, sparse gating, or knowledge injection in isolation, no unified framework has mapped the full landscape of approaches targeting domain-specific neuron activation. This scoping review maps existing approaches to identify evidence gaps and inform a follow-on systematic review. RESEARCH QUESTION "What approaches have been proposed for optimizing domain-specific neuron activation and sparse computation in Multimodal Large Language Models, and what are their reported effects on accuracy, computational efficiency, and interpretability?" PICO-S FRAME Population: Multimodal LLM architectures (e.g., LLaVA, InstructBLIP, BLIP-2, Flamingo) Intervention: Domain-specific neuron activation and sparse computation methods Comparator: Dense/general-purpose baseline MLLMs Outcomes: Accuracy, computational efficiency (FLOPs, latency), interpretability Setting: Academic publications, 2019–2025, English language INCLUSION CRITERIA (I1–I7) I1: Study proposes or evaluates an approach for neuron activation, sparse computation, or domain adaptation in MLLMs I2: Study reports at least one quantitative performance metric I3: Study involves a multimodal architecture (vision + language minimum) I4: Published 2019–2025 (aligned with MLLM development era) I5: English language I6: Peer-reviewed journal or conference paper, or arXiv preprint with ≥10 citations I7: Full text accessible EXCLUSION CRITERIA (E1–E6) E1: Unimodal models (text-only or vision-only) E2: No evaluation on a domain-specific task E3: Survey/review papers without novel empirical contribution E4: Non-English publications E5: Pre-2019 publications E6: No accessible full text DATABASES &amp; SEARCH STRATEGY Five databases: Scopus, Web of Science, IEEE Xplore, ACM Digital Library, arXiv. Pre-drafted Boolean strings using DASNG framework terms (Domain-Specific, Activation, Sparse/Neuron, Grounding). Searches to be conducted in Week 2. All search strings to be reproduced verbatim in the final manuscript appendix. SCREENING PROCESS Three-stage PRISMA-ScR workflow: (1) de-duplication in Zotero, (2) title/abstract screening in Rayyan (dual reviewer, blinded), (3) full-text screening. Inter-rater agreement measured by Cohen's κ (target ≥ 0.70). Disagreements resolved by consensus; third reviewer (tie-breaker) consulted if unresolved. DATA EXTRACTION 11-field extraction template covering: study identification, methodology, MLLM architecture, sparsity/gating mechanism, training approach, datasets used, accuracy outcomes, efficiency outcomes, interpretability outcomes, limitations, and reviewer notes. Extraction piloted on 5–10 papers before full deployment. SYNTHESIS PLAN Narrative and tabular synthesis organised around five sub-questions aligned with DASNG dimensions. Planned figures: PRISMA flow diagram, taxonomy diagram of sparse computation mechanisms, outcome scatter, gap matrix, and chronological evolution chart. No meta-analysis planned (scoping methodology). QUALITY ASSESSMENT N/A — Quality assessment is not conducted in scoping reviews per PRISMA-ScR methodology. META-ANALYSIS N/A — No meta-analysis planned. This is a scoping review. TIMELINE 10 weeks from protocol registration date. Protocol registered before any database searches are conducted.

**Решение:** -1 PRISMA-ScR систематический scoping обзор разреженных вычислений в MLLM

---

### 218 · R1994

**A structured reasoning framework for auditable traffic-crash liability adjudication with large language models**

2026 · Artificial Intelligence and Law · article · en · https://doi.org/10.1007/s10506-026-09542-5

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 юриспруденция, ответственность при ДТП

---

### 219 · R1057

**Voice-Enabled Virtual Patients for Interactive Training in Standardized Clinical Assessment: Mixed Methods Pilot Study.**

2026 · Journal of medical Internet research · journal article, journalarticle, article · eng · https://doi.org/10.2196/89066

Abstract Background Training mental health clinicians to conduct standardized clinical assessments is challenging due to a lack of scalable, realistic practice opportunities. Traditional methods often fail to prepare trainees for the variability and complexity of real-world patient interactions, potentially impacting data quality in clinical trials. This paper introduces a novel approach to address this training gap using large language model (LLM)–based interview simulations. Objective This study aimed to develop and validate a voice-enabled virtual patient simulation system as a proof of concept. We described the development of the system and evaluated whether it could generate virtual patients that (1) accurately adhered to predefined clinical profiles, (2) maintained a coherent and consistent narrative, and (3) produced dialogue that is perceived as realistic. Methods We implemented a system that used an LLM to simulate patients with specified symptom profiles, demographic backgrounds, and distinct communication styles. The system’s performance was analyzed through a mixed methods evaluation, which included a formal assessment by 5 experienced clinical raters who conducted simulated structured Montgomery-Åsberg Depression Rating Scale (MADRS) interviews with 4 virtual patient personae, scored them on the scale, and provided qualitative feedback on the system’s clinical plausibility, narrative cohesion, and dialogue realism. Results Across 20 interviews, the virtual patients demonstrated reasonable adherence to their configured clinical profiles, with human rater scores falling near their predefined score configurations. The mean item difference between MADRS rater scores and configured scores was 0.52 (SD 0.75); interrater reliability for the total score was 0.90 (95% CI 0.68‐0.99). Expert raters consistently gave average ratings of “agree” to “strongly agree” when asked to evaluate the qualitative realism and cohesion of the virtual patients. Conclusions LLM-powered virtual patient simulations offered a promising, scalable tool for training clinicians in standardized clinical assessment. This pilot study provides initial evidence for the system’s ability to produce clinically relevant practice scenarios with reasonable fidelity.

**Решение:** -2 симуляция виртуального пациента с депрессией; клиницисты опрашивают и оценивают его по MADRS

---

### 220 · R6621

**Boosting Large Language Models for Mental Manipulation Detection via Data Augmentation and Distillation**

2026 · ACM Web Conference (WWW) · journalarticle, book, conference · en · https://doi.org/10.1145/3774904.3792977

Mental manipulation on social media poses a covert yet serious threat to individuals' psychological well-being and the integrity of online interactions. Detecting such behavior is challenging due to the difficult-to-annotate training data, its highly covert and multi-turn nature, and the lack of real-world datasets. To address these challenges, we propose MentalMAD, a framework that enhances large language models for mental manipulation detection. Our approach consists of three key components: EvoSA, an annotation-free data augmentation method that combines evolutionary operations with speech-act-aware prompting; teacher-model-generated complementary-task supervision; and Complementary-Convergent Distillation, a phase-wise strategy for transferring manipulation-specific knowledge to student models. We then constructed the ReaMent dataset, comprising 5,000 real-world-sourced dialogues. Extensive experiments show that MentalMAD improves accuracy by 14.0%, macro-F1 by 27.3%, and weighted F1 by 15.1% over the strongest baseline. The code and the dataset are publicly available at https://github.com/Yuansheng-Gao/MentalMAD. Accepted to WWW 2026

**Решение:** ? MentalMAD: детекция ментальных манипуляций и газлайтинга в ReaMent 5000; проверить разметку людьми

---

### 221 · R7801

**GenAI Reliability in Content Analysis: Assessing Agreement Between LLMs in Measuring Discursive Violence**

2025 · International Conference on Control Systems and Computer Science · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/cscs66924.2025.00095

This study investigates the reliability of three leading large language models (LLMs), ChatGPT 4.5, Claude 3.7 Sonnet, and Gemini 2.0 Flash, in measuring discursive violence against women in Eminem's lyrics. Through a three-phase experimental design, we assessed both inter-coder reliability between different AI systems and measurement fidelity within each system across repeated evaluations. Our findings show good agreement among AI systems in their independent assessments (r = .75-.86), with stronger alignment between ChatGPT and Claude. When systems were exposed to each other's interpretations, agreement increased (reaching r = .89-.97), showing that cross-system exposure increases measurement consistency. All systems maintained stability in their evaluations across time (r = .93-.97), though Sexual Violence seems to be the most challenging dimension to evaluate reliably. These results have implications for AI-assisted content analysis, indicating that while these systems show promising reliability for evaluative tasks, some aspects of gender-based violence remain more subjective and challenging to operationalize consistently, even with structured frameworks. Our methodological approach offers new strategies for enhancing measurement consistency in AI-assisted qualitative research.

**Решение:** -5 согласие только между LLM: ChatGPT, Claude, Gemini на текстах песен Эминема, без людей

---

### 222 · R11782

**PATIENT-Ψ: Using Large Language Models to Simulate Patients for Training Mental Health Professionals**

2024 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.48550/arxiv.2405.19660

Mental illness remains one of the most critical public health issues. Despite its importance, many mental health professionals highlight a disconnect between their training and actual real-world patient practice. To help bridge this gap, we propose PATIENT-Ψ, a novel patient simulation framework for cognitive behavior therapy (CBT) training. To build PATIENT-Ψ, we construct diverse patient cognitive models based on CBT principles and use large language models (LLMs) programmed with these cognitive models to act as a simulated therapy patient. We propose an interactive training scheme, PATIENT-Ψ-TRAINER, for mental health trainees to practice a key skill in CBT -- formulating the cognitive model of the patient -- through role-playing a therapy session with PATIENT-Ψ. To evaluate PATIENT-Ψ, we conducted a comprehensive user study of 13 mental health trainees and 20 experts. The results demonstrate that practice using PATIENT-Ψ-TRAINER enhances the perceived skill acquisition and confidence of the trainees beyond existing forms of training such as textbooks, videos, and role-play with non-patients. Based on the experts' perceptions, PATIENT-Ψ is perceived to be closer to real patient interactions than GPT-4, and PATIENT-Ψ-TRAINER holds strong promise to improve trainee competencies. Our code and data are released at \url{https://github.com/ruiyiw/patient-psi}. EMNLP 2024 Main, 9 pages, 5 figures

**Решение:** -6 PATIENT-Ψ: симуляция пациентов для тренировки CBT-терапевтов без кодирования текста

---

### 223 · R0166

**AI-guided design of candidate BMPR1A-binding peptides for cartilage regeneration: a multi-tool computational benchmarking study**

2026 · bioRxiv · preprint, ppr · https://doi.org/10.64898/2026.03.22.713519

Abstract Bone morphogenetic protein receptor type IA (BMPR1A) is a key mediator of chondrogenesis and a validated therapeutic target for cartilage repair, yet existing BMP mimetic peptides suffer from low potency and the full-length protein (rhBMP-2) carries significant safety risks. Generative AI tools for protein design can now produce de novo peptide binders, but none have been applied to cartilage regeneration targets. Here, we benchmarked four architecturally distinct AI tools—RFdiffusion, BindCraft, PepMLM, and RFpeptides—to design candidate BMPR1A-binding peptides. We generated 192 candidates alongside 98 negative controls (290 total) and evaluated all complexes using AlphaFold 3 structure prediction, dual physics-based energy scoring (PyRosetta and FoldX), and contact recapitulation against the crystallographic BMP-2:BMPR1A interface (PDB: 1REW). A four-metric composite ranking identified a 15-residue PepMLM design (pepmlm_L15_0026) as the top candidate, combining favorable binding energy (PyRosetta dG separated = −45.9 REU; FoldX Δ G = −19.4 kcal/mol) with the highest contact recapitulation among top-ranked peptides (11/30 gold-standard interface residues). Designed candidates significantly outperformed controls on ipTM ( p = 0.002) and FoldX Δ G ( p < 0.001). BindCraft candidates achieved the highest structural confidence (ipTM up to 0.81) but exhibited moderate contact recapitulation (mean 0.224), consistent with the computational hypothesis that they may engage alternative BMPR1A binding surfaces rather than the native BMP-2 interface. Physicochemical filtering yielded a shortlist of 54 candidates across all four tools. These results establish a reproducible computational framework for AI-guided peptide design targeting cartilage regeneration and identify specific candidates for future experimental validation via binding assays and chondrocyte differentiation studies. Author summary Damaged cartilage has limited capacity to heal, and current biological therapies based on bone morphogenetic protein 2 (BMP-2) carry serious safety concerns including ectopic bone formation and inflammation. Short peptides that mimic BMP-2’s interaction with its receptor BMPR1A could offer a safer, more targeted alternative, but designing such peptides from scratch is challenging. We used four different artificial intelligence tools—each employing a distinct computational strategy—to generate 192 candidate peptides designed to bind BMPR1A. We then evaluated all candidates using multiple independent computational methods to assess binding quality, energy favorability, and whether each peptide targets the correct site on the receptor. Our analysis identified a shortlist of 54 promising candidates, with a 15-residue peptide from the language model-based tool PepMLM emerging as the top-ranked design. We also found evidence that one tool (BindCraft) may produce peptides that bind BMPR1A at sites different from the natural BMP-2 interface, highlighting the importance of validating not just whether a peptide binds, but where it binds. Our computational framework and candidate peptides provide a foundation for future laboratory testing toward cartilage repair therapies.

**Решение:** -4 биохимия, пептидный дизайн для хрящевой ткани

---

### 224 · R8453

**LLM for Semantic Role Labeling of Emotion Predicates in Russian**

2025 · Supercomputing Frontiers and Innovations · article · https://doi.org/10.14529/jsfi250303

Semantic role labeling (SRL) for morphologically rich languages, such as Russian, faces significant challenges due to complex case marking systems, free word order, and limited annotated resources. These challenges are particularly acute for emotion predicates, which require specialized linguistic expertise to capture distinctions between roles denoting those who feel, causes and objects of feelings. We propose a novel approach that leverages large language models to address SRL for Russian emotion predicates through few-shot in-context learning combined with predicate-specific instructions. Our method was evaluated on a manually annotated dataset of 169 sentences containing six emotion predicate groups extracted from Russian social media texts. We compared three state-of-the-art LLMs (Claude 3.7 Sonnet, GPT-5 Mini, and DeepSeek V3) against a RuELECTRA-based trained sequence labelling baseline using both exact and partial matching criteria. Claude 3.7 achieved the highest performance with 74.85% F1 score on partial matching, substantially outperforming the baseline (22.67%). For general predicates on FrameBank, our adapted method with GPT-5 Mini reached 85.0% F1 compared to the previous state-of-the-art of 80.1%. The LLM-based approach successfully handles complex linguistic phenomena, including syntactic zeros and multi-word arguments, while requiring minimal manually annotated training data. We demonstrate that LLM-based methods can significantly advance SRL for Russian by reducing dependency on large-scale annotated corpora while achieving competitive performance.

**Решение:** -4 компьютерная лингвистика, семантические роли предикатов эмоций в русском FrameBank

---

### 225 · R1315

**Auditing LLM-mediated interpretation through source-to-claim documentation**

2026 · Research Square · preprint · https://doi.org/10.21203/rs.3.rs-10756391/v1

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 NLP, аудит источников утверждений LLM

---

### 226 · R8280

**Cascading Adversarial Bias from Injection to Distillation in Language Models**

2025 · ACM SIGSAC Conference on Computer and Communications Security (CCS) · journalarticle, book, conference · en · https://doi.org/10.1145/3719027.3765122

Model distillation has become essential for creating deployable language models, but their widespread deployment raises concerns about about their resilience to adversarial manipulation. This paper investigates how adversaries can inject subtle biases into teacher models through minimal data poisoning during training, which propagates to a smaller distilled student model and becomes significantly amplified. We identify two propagation modes: Untargeted (affecting multiple tasks) and Targeted (focusing on specific task while maintaining normal behavior elsewhere). With only 25 poisoned samples (0.25% poisoning rate), student models generate biased responses 76.9% of the time in targeted scenarios versus 69.4% in teachers, while untargeted propagation shows 5.7X-29.2X higher adversarial bias rate in students on unseen tasks. We validate across six bias types (targeted advertisement, phishing link, narrative manipulations, insecure coding practices), various distillation methods, and text/code generation modalities. Current defense mechanisms—including perplexity filtering, bias detection systems, and LLM-based autoraters—prove inadequate against these attacks. We propose practical design principles for building effective adversarial bias mitigation strategies to address this threat vector.

**Решение:** -4 кибербезопасность, состязательная дистилляция предвзятости

---

### 227 · R2665

**Large-Language-Models-As-a-Judge in Theory-Agnostic Adaptive Metric-Alignment for Prototypical Networks in Personality Recognition**

2026 · IEEE Transactions on Affective Computing · journalarticle, preprint/article, article · en · https://doi.org/10.1109/taffc.2026.3712379

Personality recognition has traditionally been constrained by theory-dependent formulations, where models are trained to fit predefined psychological taxonomies rather than uncovering shared underlying behavioral structure. This limits generalization, as personality itself is better understood as theory-invariant, while existing annotations reflect only partial and sometimes inconsistent views of the same latent traits. In this work, we introduce JAM ((J)udge for (A)daptive (M)etric-Alignment), a theory-agnostic framework that shifts learning from adapting to predefined personality theories toward discovering unified latent pseudo-facets that capture shared psychological structure. Rather than constraining the model to any personality taxonomy during training or inference, the framework learns generalizable psychological representations and can infer an individual's latent psychological profile directly from the textual samples, without requiring theory-specific labels. JAM achieves this through an Attention-Pooled Graph Prototypical Network that learns structured representations via clustering in embedding space, together with a Cross-Theory Harmonization (CTH) approach that integrates (i) Human-Guided Linkage and (ii) Machine-Induced Consensus to unify heterogeneous datasets without relying on predefined labels. To further improve robustness and data quality, we incorporate an LLM-as-a-Judge mechanism operating in two configurations, (i) LLM-before-the-loop and (ii) LLM-in-the-loop which identifies ambiguous samples to guide adaptive metric learning. Experiments show that JAM improves cross-framework generalization and performance, establishing a strong step toward theory-agnostic personality inference and supporting low-resource personality theories. The related code repository, model weights, and artifacts are available at https://research.jingjietan.com/JAM

**Решение:** ? IEEE TAFFC: распознавание черт личности, калибровка метрик LLM-as-a-judge; проверить согласие на уровне текстов

---

### 228 · R3067

**An LLM-Native Psychometric Instrument: Factor-Analytic Derivation and Validation of Behavioral Disposition Scales for Large Language Models**

2026 · OSF Registries · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/8y7ka

This study develops and validates the first psychometric personality instrument whose constructs are derived from LLM behavioral affordances rather than human personality theory. Existing tools (MPI, TRAIT, DeepMind framework) apply human Big Five or Dark Triad inventories to LLMs; none define constructs native to LLM behavior such as sycophancy, refusal sensitivity, or hedging. We generate ~200 items across 13 candidate behavioral domains, administer them to 25 models spanning 16 families, and use exploratory factor analysis to derive a new latent trait structure bottom-up. The instrument undergoes a full construct-validity pipeline: internal consistency, cross-run stability, convergent/discriminant validity against BFI-44, and predictive validity via blinded human ratings of independent behavioral samples. All materials, data, and code will be released as open-source.

**Решение:** -1 OSF пре-регистрация поведенческих диспозиционных шкал LLM

---

### 229 · R6554

**PrivacyReasoner: Can LLM Emulate a Human-like Privacy Mind?**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2601.09152

Prior work on LLM-based privacy focuses on norm judgment over synthetic vignettes, rather than how people think about a specific data practice and formulate their opinions. We address this gap by designing PrivacyReasoner, an agent architecture grounded in three key ideas: (1) LLMs can detect subtle privacy cues in natural language and role-play human characteristics; (2) a user's ``privacy mind'' can be reconstructed from their real-world online comment history, distilling experiences, personality, and cultural orientations; and (3) a contextual filter can dynamically activate relevant privacy beliefs based on the contexts in a scenario. We evaluate PrivacyReasoner on real-world privacy discussions from Hacker News, using an LLM-as-a-Judge evaluator calibrated against an established privacy concern taxonomy to quantify reasoning faithfulness. PrivacyReasoner significantly outperforms baselines in predicting individual privacy concerns and generalizes across different domains, such as AI, e-commerce, and healthcare.

**Решение:** -4 приватность, рассуждения о нормах приватности по истории комментариев

---

### 230 · R5426

**LLM-Based Support System for Research Topic Decision via Research Information and Notes Organization**

2026 · Communications in computer and information science · conference-paper · en · https://doi.org/10.1007/978-3-032-28463-1_41

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 наукометрия, инструмент поддержки выбора темы исследований

---

### 231 · R4309

**Large language models in high-stakes Arabic-to-English legal translation: a contextual terminology study of ChatGPT 5.2 and DeepSeek**

2026 · International Journal of Legal Discourse · journalarticle, article · en · https://doi.org/10.1515/ijld-2026-3005

Abstract This study examines large language models in high-stakes Arabic-to-English legal translation through an evaluation of ChatGPT 5.2 and DeepSeek-V3. Focusing on Palestinian criminal judgments, the research tests how models translate specialized terminology. From a 120,000-word corpus, 100 recurrent terms were extracted based on their doctrinal significance and procedural function. Context was operationalized by providing the models with the complete authentic sentence in which each target term was originally embedded, rather than isolated vocabulary lists. Both models translated the identical dataset under a zero-shot, single-output protocol. Two accredited translators evaluated the semantic fidelity and institutional validity of the translated terms using a three-point accuracy scale. This quantitative scoring was directly combined with qualitative error coding to categorize the specific types of legal translation failures, such as conceptual distortion or literalism. Inter-rater reliability was established via Cohen’s Kappa, and differences were analyzed using Wilcoxon signed-rank testing. Results indicate statistically significant performance differences. ChatGPT 5.2 achieved higher overall accuracy without critical errors, while DeepSeek generated notably more conceptually distorted outputs. The findings demonstrate that when legal terms are processed within complete sentences, the models display distinct operational vulnerabilities – such as algorithmic paraphrasing or structural literalism – and that model performance differs considerably across systems.

**Решение:** -4 юриспруденция, перевод судебных решений по уголовным делам

---

### 232 · R0932

**Trends in the psychedelic renaissance: applying artificial intelligence to measure media portrayal of psychedelic drugs in the 21st century.**

2026 · BJPsych open · journal article, journalarticle, article · eng · https://doi.org/10.1192/bjo.2025.10974

Background The relationship between media portrayal of psychedelic drugs, scientific research and drug policy is an area of debate. Aims To apply artificial intelligence technology to measure trends in media sentiment towards the therapeutic potential of psychedelic drugs. Method Up to 300 of the most relevant articles from Google News searches for the term ‘psychedelics’ were sampled for each year from 2000 to 2025. A large language model, ChatGPT, evaluated subject matter and sentiment. Results In total, 88.3% of screened URLs (3308 of 3747) were included in the analysis. The proportion of articles focusing on the therapeutic potential of psychedelics increased from 13.3% (26 of 198) from 2000 to 2009 to 85.3% (1254 of 1470) from 2020 to 2025. The average sentiment score from 2000 to 2025 for articles from all publications ( N = 2168) was 78.5 ± 9.3 (mean ± s.d.) (possible range: 1–100). 1.3% (29 of 2168) of articles carried negative sentiment (<50) whereas 4.8% (103 of 2168) had extremely positive sentiment (≥90). Average sentiment reached a peak in 2020 (80.8 ± 7.0), and a statistically significant trough in sentiment was observed in 2024 relative to 2020–2023 (2020–2023, 79.2; 2024, 74.3, P < 0.00001, Mann–Whitney U -test). The proportion of negative-neutral articles (≤65) increased annually from a trough of 3.6% (8 of 267) in 2020 to a peak of 20.9% (43 of 253) in 2024. Artificial intelligence sentiment scores were correlated and concordant with average human rater scores ( r = 0.88, concordance correlation coefficient 0.84). Conclusions Although most 21st-century media coverage of psychedelic drugs has been positively framed, negative and neutral coverage has increased in frequency since 2020. Researchers, clinicians, regulators and policy-makers should be mindful of the complex relationship between media portrayals of psychedelics and the results of scientific research.

**Решение:** -4 анализ новостных медиа о психоделиках

---

### 233 · R6875

**From expert consensus to outcome definitions: a four-domain, double-blinded definition-alignment adjudication to consolidate the codebook (v3.0) of an AI-based clinical text phenotyping system**

2026 · Open Science Framework · studyregistration/pre-registration, other · https://doi.org/10.17605/osf.io/hgbn9

Study A of a two-part programme. A four-domain, double-blinded definition-alignment adjudication to consolidate codebook v3.0 of an AI-based clinical text phenotyping system (dictionary track + locally hosted LLM track) for ECG and ultrasound narratives. Two independent blinded clinicians annotate fresh definition-boundary records in four domains (ECG [community cohort H]; cardiac ultrasound [PG]; abdominal ultrasound [PG]; abdominal ultrasound [H]); every A1!=A2 discrepancy is arbitrated; pre-specified consolidation rules (C1-C4) determine the adopted outcome-aggregation rule per domain and the consolidated v3.0 codebook. No confirmatory sampling occurs before this registration receives its DOI. Full registration text is provided in the section fields below (Overview, Research Design, Sampling, Variables, Analysis Plan, Other) and as an attached PDF. Contributors and ORCIDs are listed on the OSF project page. License: CC-BY 4.0 (registration text).

**Решение:** -1 OSF пре-регистрация кодбука для фенотипирования по ЭКГ/УЗИ

---

### 234 · R0300

**Human–AI Agreement in Authentic Writing Assessment: A Multi-Agent LLM Evaluation**

2026 · OSF Preprints (OSF Preprints) · studyregistration/pre-registration, preprint · https://doi.org/10.17605/osf.io/5c9nk

This project evaluates a multi-agent large language model (LLM) system for automated essay scoring and feedback against expert instructor judgments on authentic student writing collected from one or more upper-division undergraduate writing-intensive courses. The system decomposes scoring across specialized LLM agents — agents that surface and critique aspects of the essay, and a judging agent that integrates their analysis into a final rubric-based score and written feedback — with the specific architecture fixed in advance for each analysis wave. Unlike prior LLM scoring evaluations that rely on standardized benchmarks such as ASAP, we assess the system on real classroom data: instructor rubric scores, in-text annotations, and summary comments from graded student papers. We measure (1) quantitative score agreement between system and instructor using Quadratic Weighted Kappa, Mean Absolute Error, and Agree@1, and (2) qualitative alignment between system and instructor feedback through systematic coding, with an optional NLP-based comparison of semantic similarity and topic overlap. Expected outcomes include estimates of human–AI score agreement on real coursework, a characterization of where the system and instructors agree or diverge in their written feedback, and methodological insight into integrating multi-agent AI tools into instructor grading workflows while preserving instructor authority over final evaluation.

**Решение:** -4 педагогика, автоматическая оценка студенческих эссе против оценок преподавателей

---

### 235 · R11199

**SouLLMate: An Adaptive LLM-Driven System for Advanced Mental Health Support and Assessment, Based on a Systematic Application Survey**

2024 · arXiv (Cornell University) · journalarticle, review, preprint/article · en · https://doi.org/10.48550/arxiv.2410.11859

Mental health issues significantly impact individuals' daily lives, yet many do not receive the help they need even with available online resources. This study aims to provide accessible, stigma-free, personalized, and real-time mental health support through cutting-edge AI technologies. It makes the following contributions: (1) Conducting an extensive survey of recent mental health support methods to identify prevalent functionalities and unmet needs. (2) Introducing SouLLMate, an adaptive LLM-driven system that integrates LLM technologies, Chain, Retrieval-Augmented Generation (RAG), prompt engineering, and domain knowledge. This system offers advanced features such as Suicide Risk Detection and Proactive Guidance Dialogue, and utilizes RAG for personalized profile uploads and Conversational Information Extraction. (3) Developing novel evaluation approaches to assess preliminary assessments and suicide risk detection, utilizing annotated real-life interview data and professionally labeled datasets indicating suicide tendencies. (4) Proposing Key Indicator Summarization (KIS) and Proactive Questioning Strategy (PQS) methods to enhance model performance and usability through context-sensitive response adjustments and semantic coherence evaluations. This study contributes to advancing mental health support technologies, potentially improving the accessibility and effectiveness of mental health care globally.

**Решение:** ? SouLLMate: оценка суицидального риска по клиническим интервью; проверить сопоставление с клиницистами

---

### 236 · R12091

**A Review of Chatbots Application on Supporting International Students’ Mental Health**

2024 · Arts Culture and Language · journalarticle, review, article · en · https://doi.org/10.61173/g27kbp22

International students face distinctive challenges, including acculturative stress, homesickness, language barriers, and heightened academic expectations. As a result, their mental health and overall well-being have become subjects of growing concern and significance in academic and support communities worldwide. The emergence of AI technologies, like ChatGPT, opens new avenues for international student mental health interventions. However, no specific Chatbot has been approved as effective for this population. This study aims to comprehensively summarize Chatbot applications in mental health counseling and analyze the challenges of applying them to international students. The study found that prominent Chatbots could demonstrate efficacy in reducing symptoms of depression and anxiety through techniques such as cognitive behavioral therapy (CBT). Chatbots are becoming integral to mental health care, providing accessible and evidence-based interventions and psychoeducation. Compared with traditional in-personal mental health counselling, a Chatbot is more functioning in providing personalized therapy sessions, essay accessibility, real-time responses, and suitable assistance, which could solve current challenges and unmet mental health counselling needs of international students. Despite their potential, ethical considerations and privacy challenges must be addressed to ensure reliable and secure use. Continued refinement is needed for international students’ application to enhance multicultural sensitivity, the accuracy of cross-language interpretation, and personalization. The evolution of Chatbots holds significant promise for enhancing mental health support, particularly for international students navigating and coping with their unique challenges.

**Решение:** -1 обзор чат-ботов для психического здоровья иностранных студентов

---

### 237 · R4784

**Unlocking the Power of Generative AI in Qualitative Data Analysis: A Deep Dive into Data from a Physical Activity Service Evaluation**

2026 · Smart innovation, systems and technologies · conference-paper · en · https://doi.org/10.1007/978-3-032-18849-6_17

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 качественный анализ отзывов об услугах физической активности

---

### 238 · R8797

**Performance of Open-Source Large Language Models in Psychiatry: Usability Study Through Comparative Analysis of Non-English Records and English Translations.**

2025 · Journal of medical Internet research · comparative study, research-article, journal article · eng · https://doi.org/10.2196/69857

Abstract Background Large language models (LLMs) have emerged as promising tools for addressing global disparities in mental health care. However, cloud-based proprietary models raise concerns about data privacy and limited adaptability to local health care systems. In contrast, open-source LLMs offer several advantages, including enhanced data security, the ability to operate offline in resource-limited settings, and greater adaptability to non-English clinical environments. Nevertheless, their performance in psychiatric applications involving non-English language inputs remains largely unexplored. Objective This study aimed to systematically evaluate the clinical reasoning capabilities and diagnostic accuracy of a locally deployable open-source LLM in both Korean and English psychiatric contexts. Methods The openbuddy-mistral-7b-v13.1 model, fine-tuned from Mistral 7B to enable conversational capabilities in Korean, was selected. A total of 200 deidentified psychiatric interview notes, documented during initial assessments of emergency department patients, were randomly selected from the electronic medical records of a tertiary hospital in South Korea. The dataset included 50 cases each of schizophrenia, bipolar disorder, depressive disorder, and anxiety disorder. The model translated the Korean notes into English and was prompted to extract 5 clinically meaningful diagnostic clues and generate the 2 most likely diagnoses using both the original Korean and translated English inputs. The hallucination rate and clinical relevance of the generated clues were manually evaluated. Top-1 and top-2 diagnostic accuracy were assessed by comparing the model’s prediction with the ground truth labels. Additionally, the model’s performance on a structured diagnostic task was evaluated using the psychiatry section of the Korean Medical Licensing Examination and its English-translated version. Results The model generated 997 clues from Korean interview notes and 1003 clues from English-translated notes. Hallucinations were more frequent with Korean input (n=301, 30.2%) than with English (n=134, 13.4%). Diagnostic relevance was also higher in English (n=429, 42.8%) compared to Korean (n=341, 34.2%). The model showed significantly higher top-1 diagnostic accuracy with English input (74.5% vs 59%; P<.001), while top-2 accuracy was comparable (89.5% vs 90%; P=.56). Across 115 questions from the medical licensing examination, the model performed better in English (n=53, 46.1%) than in Korean (n=37, 32.2%), with superior results in 7 of 11 diagnostic categories. Conclusions This study provides an in-depth evaluation of an open-source LLM in multilingual psychiatric settings. The model’s performance varied notably by language, with English input consistently outperforming Korean. These findings highlight the importance of assessing LLMs in diverse linguistic and clinical contexts. To ensure equitable mental health artificial intelligence, further development of high-quality psychiatric datasets in underrepresented languages and culturally adapted training strategies will be essential.

**Решение:** -3 критериальная валидность: предсказание психиатрических диагнозов из электронных медкарт EHR

---

### 239 · R1186

**Accuracy of Autism-Related TikTok Information in Italian: A Comparison Between Human Raters and Large Language Models.**

2026 · Journal of autism and developmental disorders · journal article, med, journalarticle · eng · https://doi.org/10.1007/s10803-026-07249-9

Purpose Social networking sites are major channels for sharing information on neurodiversity, including autism spectrum disorder. TikTok has become a particularly influential platform for autism-related communication, yet concerns remain about the scientific accuracy of such content. Most prior studies have focused on English-language videos and have evaluated accuracy with limited granularity. Additionally, the difficulty of achieving consistent expert ratings underscores the need for automated reliability assessment. Methods In this study, we examined 408 informational statements extracted from 148 TikTok videos posted under the hashtag #Autismo (Italian for #Autism). Three clinical experts independently classified each statement as inaccurate, over-generalized, or accurate; their median ratings served as the human-derived ground truth and were compared with classifications from two large language models: ChatGPT 4.0 mini and Gemini 1.5 Flash. Results Human raters showed moderate agreement (kappa(mean) = 0.52) and high specific agreement only for accurate statements, with lower agreement for overgeneralized and inaccurate content. ChatGPT achieved moderate agreement with human ratings (kappa= 0.58), while Gemini reached only fair agreement (kappa= 0.29). ChatGPT also exhibited a more conservative evaluation pattern (accurate information: precision = 0.89, recall = 0.82), whereas Gemini tended to overestimate accuracy (accurate information: precision = 0.76, recall = 0.93). Conclusion These findings suggest that LLMs, particularly ChatGPT, may support cautious and assistive evaluation of online health content. Future research should assess their applicability across online communities and platforms and explore their integration into accuracy-based alert systems that provide users with contextual reliability cues.</p

**Решение:** ? достоверность видео об аутизме в TikTok: клиницисты-эксперты vs ChatGPT [κ=0.58] и Gemini [κ=0.29]; психообразование vs фактчекинг

---

### 240 · R3401

**AI-derived research domain criteria scores from medical records predict brain inflammatory markers in psychotic disorders: A cross-sectional, real-world study.**

2026 · Science progress · journal article, journalarticle, article · eng · https://doi.org/10.1177/00368504261417875

Objective Recent advances in generative artificial intelligence (AI) and dimensional approaches in psychiatry offer scalable scoring of psychopathology, yet biological validation remains challenging. This study aimed to compare AI and human performances in scoring dimensional psychopathology and its relationship with inflammatory brain markers in psychotic disorders. Methods In a cross-sectional, real-world, prospective study, we generated research domain criteria (RDoC) profiles using a large-language model and human ratings from admission notes of 127 consecutively selected patients with psychotic disorders. Magnetic resonance imaging (MRI) diffusion-based restricted fraction (RF) values were extracted from the amygdala, hippocampus, and neocortex as a proxy of inflammation. We assessed the agreement between AI- and human-derived scores and their predictive value for regional RF. Results AI and human RDoC ratings showed moderate-to-high agreement (intraclass correlation coefficients: 0.65–0.81). AI-derived, but not human-derived, negative and positive valence RDoC scores predicted amygdala and neocortical inflammation, while social and regulatory/arousal scores predicted hippocampal RF. A significant association was found between neocortical RF and regulatory/arousal scores in the AI assessment. Both AI- and human-derived cognitive scores predicted cortical RF. When the regression analyses were corrected for multiple comparisons, only the AI-derived associations remained significant: the amygdala for negative valence and the cortex for regulatory/arousal scores. Conclusions These results suggest a significant correspondence between AI and human RDoC ratings. AI-based dimensional phenotyping may reflect underlying neuroinflammatory processes, offering a biologically anchored tool for precision psychiatry.

**Решение:** + T1/T3 размерный скоринг психопатологии по RDoC из психиатрических карт, LLM vs клиницисты, ICC=0.65–0.81

---

### 241 · R0954

**CALA-Net: Intelligent depression detection with multimodal fusion and Tree-of-Thoughts framework**

2026 · Computers in Human Behavior Reports · article · en · https://doi.org/10.1016/j.chbr.2026.101051

Depression is recognized as the second leading cause of global disease burden, yet efficient and precise detection methods remain underexplored. While existing approaches have made progress in identifying depressive symptoms, they are limited by insufficient multimodal semantic analysis, subjective assessment bias, and inadequate detection performance. This study aims to address these gaps by proposing the Cross-Attention and LLM-Assisted Network (CALA-Net), a multimodal framework for depression screening. The framework integrates a Temporal-Spatial Cross-Attention (TSCA) module to fuse audio and facial features, employs a fine-tuned large language model (LLM), and utilizes a Tree of Thoughts (ToT) prompting mechanism to systematically evaluate participants’ dialogue or self-report texts along standardized psychological feature dimensions. The extracted multimodal features are then processed by a random forest classifier for final depression assessment. Evaluation was conducted on the publicly available D-Vlog and LMVD datasets, as well as the internally developed FJSI structured clinical interview dataset, demonstrating the model’s capability across different evaluation settings. The TSCA module achieved F1-Scores ranging from 0.740 to 0.787 across all three datasets. The complete CALA-Net framework, incorporating the text modality, showed improved performance on the FJSI dataset with F1-Scores between 0.826 and 0.841. These findings provide valuable insights into multimodal depression detection and present a novel approach to support objective, automated screening for depression in clinical settings. • We propose CALA-Net, a multimodal framework for automated depression screening. • We designed a TSCA module for audio and facial features fusion via temporal-spatial cross-attention. • We found the combination of audio, facial, and textual modalities can improve depression detection. • CALA-Net achieves F1-Scores of 0.826-0.841 on clinical interview data.

**Решение:** ? CALA-Net: скрининг депрессии по интервью FJSI; проверить сопоставление RDoC/ToT с оценками клиницистов vs диагнозом

---

### 242 · R10443

**Unveiling GPT-4V's hidden challenges behind high accuracy on USMLE questions: Observational Study.**

2025 · Journal of medical Internet research · journal article, observational study, research support, n.i.h., extramural · eng · https://doi.org/10.2196/65146

BACKGROUND: Recent advancements in artificial intelligence, such as GPT-3.5 Turbo (OpenAI) and GPT-4, have demonstrated significant potential by achieving good scores on text-only United States Medical Licensing Examination (USMLE) exams and effectively answering questions from physicians. However, the ability of these models to interpret medical images remains underexplored. OBJECTIVE: This study aimed to comprehensively evaluate the performance, interpretability, and limitations of GPT-3.5 Turbo, GPT-4, and its successor, GPT-4 Vision (GPT-4V), specifically focusing on GPT-4V's newly introduced image-understanding feature. By assessing the models on medical licensing examination questions that require image interpretation, we sought to highlight the strengths and weaknesses of GPT-4V in handling complex multimodal clinical information, thereby exposing hidden flaws and providing insights into its readiness for integration into clinical settings. METHODS: This cross-sectional study tested GPT-4V, GPT-4, and ChatGPT-3.5 Turbo on a total of 227 multiple-choice questions with images from USMLE Step 1 (n=19), Step 2 clinical knowledge (n=14), Step 3 (n=18), the Diagnostic Radiology Qualifying Core Exam (DRQCE) (n=26), and AMBOSS question banks (n=150). AMBOSS provided expert-written hints and question difficulty levels. GPT-4V's accuracy was compared with 2 state-of-the-art large language models, GPT-3.5 Turbo and GPT-4. The quality of the explanations was evaluated by choosing human preference between an explanation by GPT-4V (without hint), an explanation by an expert, or a tie, using 3 qualitative metrics: comprehensive explanation, question information, and image interpretation. To better understand GPT-4V's explanation ability, we modified a patient case report to resemble a typical "curbside consultation" between physicians. RESULTS: For questions with images, GPT-4V achieved an accuracy of 84.2%, 85.7%, 88.9%, and 73.1% in Step 1, Step 2 clinical knowledge, Step 3 of USMLE, and DRQCE, respectively. It outperformed GPT-3.5 Turbo (42.1%, 50%, 50%, 19.2%) and GPT-4 (63.2%, 64.3%, 66.7%, 26.9%). When GPT-4V answered correctly, its explanations were nearly as good as those provided by domain experts from AMBOSS. However, incorrect answers often had poor explanation quality: 18.2% (10/55) contained inaccurate text, 45.5% (25/55) had inference errors, and 76.3% (42/55) demonstrated image misunderstandings. With human expert assistance, GPT-4V reduced errors by an average of 40% (22/55). GPT-4V accuracy improved with hints, maintaining stable performance across difficulty levels, while medical student performance declined as difficulty increased. In a simulated curbside consultation scenario, GPT-4V required multiple specific prompts to interpret complex case data accurately. CONCLUSIONS: GPT-4V achieved high accuracy on multiple-choice questions with images, highlighting its potential in medical assessments. However, significant shortcomings were observed in the quality of explanations when questions were answered incorrectly, particularly in the interpretation of images, which could not be efficiently resolved through expert interaction. These findings reveal hidden flaws in the image interpretation capabilities of GPT-4V, underscoring the need for more comprehensive evaluations beyond multiple-choice questions before integrating GPT-4V into clinical settings.

**Решение:** -4 медицинские экзаменационные вопросы USMLE

---

### 243 · R11885

**Counterfactual Explainable Incremental Prompt Attack Analysis on Large Language Models**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2407.09292

This study sheds light on the imperative need to bolster safety and privacy measures in large language models (LLMs), such as GPT-4 and LLaMA-2, by identifying and mitigating their vulnerabilities through explainable analysis of prompt attacks. We propose Counterfactual Explainable Incremental Prompt Attack (CEIPA), a novel technique where we guide prompts in a specific manner to quantitatively measure attack effectiveness and explore the embedded defense mechanisms in these models. Our approach is distinctive for its capacity to elucidate the reasons behind the generation of harmful responses by LLMs through an incremental counterfactual methodology. By organizing the prompt modification process into four incremental levels: (word, sentence, character, and a combination of character and word) we facilitate a thorough examination of the susceptibilities inherent to LLMs. The findings from our study not only provide counterfactual explanation insight but also demonstrate that our framework significantly enhances the effectiveness of attack prompts. 23 pages, 6 figures

**Решение:** -4 кибербезопасность, контрфактические атаки на промпты

---

### 244 · R4510

**Fine-tuning LLMs for Passive Depression Severity Estimation from AI Mental Health Dialogue**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.17973

Depression is the leading cause of disability worldwide, and early detection of symptom change is essential for timely intervention. Validated instruments such as the Patient Health Questionnaire-9 (PHQ-9) support symptom monitoring at scale, but real-world completion rates are low, introducing response bias and systematic missingness. Passive approaches that infer severity from routinely generated data could close this gap. We address this by predicting PHQ-9 total scores directly from transcripts of conversations between users and an AI mental health application, requiring only conversation text and no additional clinical data. We fine-tune a Qwen3.5-27B backbone with a regression head, augment 3,111 ground-truth labels with pseudolabels generated by a reasoning model (Claude Opus) and iteratively trained intermediate models, for a combined dataset of 6,283 users. On a held-out test set of 842 users, our best model achieves MAE = 2.6, RMSE = 4.0, Pearson r = 0.80, and AUC = 0.91 at the PHQ-9 &gt;= 10 clinical threshold. We also find AUC &gt; 0.87 at every severity threshold from PHQ-9 &gt;= 3 to PHQ-9 &gt;= 24, demonstrating that the model captures depression severity across the full clinical spectrum. This work opens the door to passive, continuous symptom monitoring in AI mental health platforms, without requiring users to complete self-report measures. 12 pages, 1 figure

**Решение:** -3 критериальная валидность: предсказание баллов опросника PHQ-9 по диалогам, r=0.80

---

### 245 · R12352

**Measuring Latent Trust Patterns in Large Language Models in the Context of Human-AI Teaming**

2023 · Proceedings of the Human Factors and Ergonomics Society Annual Meeting · journalarticle, article · en · https://doi.org/10.1177/21695067231192869

Qualitative self-report methods such as think-aloud procedures and open-ended response questions can provide valuable data to human factors research. These measures come with analytic weaknesses, such as researcher bias, intra- and inter-rater reliability concerns, and time-consuming coding protocols. A possible solution exists in the latent semantic patterns that exist in machine learning large language models. These semantic patterns could be used to analyze qualitative responses. This exploratory research compared the statistical quality of automated sentence coding using large language models to the benchmarks of self-report and behavioral measures within the context of trust in automation research. The results indicated that three large language models show promise as tools for analyzing qualitative responses. The study also provides insight on minimum sample sizes for model creation and offers recommendations for further validating the robustness of large language models as research tools.

**Решение:** -4 инженерная психология / эргономика, доверие в командах человек-ИИ

---

### 246 · R9365

**Generative AI in Higher Education: A Systematic Literature Review**

2025 · International Multidisciplinary Information Technology and Engineering Conference (IMITEC) · conference, review · https://doi.org/10.1109/imitec67386.2025.11410459

Background: Generative Artificial Intelligence (GenAI) technologies such as ChatGPT, Bard, and Claude have emerged as transformative forces in higher education, reshaping teaching, learning, assessment, and research practices. While their integration offers significant potential for personalisation, pedagogical innovation, and productivity enhancement, it simultaneously raises complex concerns regarding ethics, academic integrity, data privacy, and institutional readiness. The fragmented nature of existing research, particularly across Global South contexts such as South Africa, highlights the need for a comprehensive synthesis to guide responsible and equitable GenAI adoption. Purpose: This study systematically reviews recent empirical and conceptual research to examine GenAI readiness, adoption determinants, ethical implications, and regional disparities within higher education. It further identifies theoretical limitations within established frameworks, Technology Acceptance Model (TAM), Technology-OrganisationEnvironment (TOE), Technology Readiness Index (TRI), and Theory of Planned Behaviour (TPB) and proposes a hybrid conceptual framework integrating socio-cultural and ethical dimensions. Methods: A PRISMA-guided systematic literature review was conducted across Scopus, Web of Science, ERIC, IEEE Xplore, and Google Scholar. Out of 192 identified studies, 18 met the inclusion criteria (2023-2025). Thematic synthesis combined inductive and deductive coding to map patterns across readiness, adoption predictors, ethical issues, and policy trends. Results: Findings reveal four key readiness dimensions: technical access, psychological preparedness, ethical literacy, and institutional support. Predictors of adoption included perceived usefulness, ease of use, selfefficacy, and leadership support, while barriers centred on ethical uncertainty, data privacy concerns, and infrastructural limitations. Conclusions: A hybrid TAM, TOE, TRI, TPB framework, extended with socio-cultural and ethical components, is proposed to explain GenAI adoption holistically. The study recommends targeted AI literacy, ethical governance, and context-sensitive policies to foster equitable and sustainable integration of GenAI in higher education.

**Решение:** -1 систематический обзор применения GenAI в высшем образовании

---

### 247 · R11123

**Artificial intelligence and consumer behavior: From predictive to generative AI**

2024 · Journal of Business Research · article · en · https://doi.org/10.1016/j.jbusres.2024.114720

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** -4 маркетинг, поведение потребителей и ИИ

---

### 248 · R3393

**Human-in-the-loop semantic middleware for construction compliance checking and safe product reuse**

2026 · Advanced Engineering Informatics · article · en · https://doi.org/10.1016/j.aei.2026.105112

The Architecture, Engineering, and Construction (AEC) sector suffers persistent challenges in formalising and automating regulatory compliance, especially for the safe reuse of construction products at their end of life (EoL). Current approaches lack compliance automation aligned with regulation semantics and do not integrate human expertise in the verification of automated decisions. This increases chances of incorrect reasoning over complex regulatory texts. This paper presents the Human-in-the-Loop Semantic Middleware (HiLSeM). Its scientific contribution to Engineering Informatics is a computational formalism for lifecycle-aware regulatory knowledge and verification. It includes a pseudo-automated step (LLM-assisted) to formalise regulatory knowledge into machine-readable structures. It also facilitates a traceable, machine-to-machine automated compliance reasoning over isolated data sources while integrating human oversight to override automated compliance decisions. The HiLSeM framework builds upon the AEC3PO ontology and related ontology-driven compliance checking streams, extending them with a formal human-verification layer and lifecycle-aware compliance history. Regulatory clauses are analysed using structured RASE (Requirement, Applicability, Selection, Exception) semantics and mapped to interconnected OWL ontologies, to deliver executable compliance requirements. The framework was evaluated using multiple real-world use cases to assess its relevance in compliance assessments. In a qualitative study involving four clauses of varying structure, clause-level extraction achieved precision from 0.50 to 1.00, recall from 0.70 to 1.00, and F1 from 0.67 to 0.93. Gold-standard annotations showed almost-perfect agreement (κ = 0.956). This work contributes a novel computational formalism by bridging semantic legal knowledge representation, automated reasoning and human in the loop verification for engineering regulation.

**Решение:** -4 строительный контроль и нормативы

---

### 249 · R3689

**Question Answering on Lengthy Arabic Narrative Books**

2026 · IEEE Access · journalarticle · https://doi.org/10.1109/access.2026.3661853

Despite the growing body of Arabic question-answering (QA) resources, most existing datasets focus on factoid questions or moderately sized texts, leaving a significant gap in addressing the complexities of lengthy narrative books. In this paper, we introduce AQANB, a new Arabic QA dataset specifically curated for extended narrative texts. This dataset enables the development and evaluation of QA systems capable of handling intricate narrative structures and broader contextual dependencies. Answering questions over long narratives is challenging due to the inherent token limitations of large language models, which restrict the amount of text processed in a single pass. Moreover, processing a larger number of tokens significantly increases computational costs. Furthermore, processing only a selected set of relevant passages requires question-passage annotation to train the retriever. To tackle this, we propose an annotation-free retriever training framework. Instead of relying on manually annotated data, our approach leverages large language models to generate synthetic question-passage pairs that probe deeper semantic content. Crucially, we introduce a novel narrative coherence-based scoring mechanism that assigns high relevance not only to the most pertinent passage but also to the passages surrounding it, thereby capturing continuity and context rather than treating adjacent passages as purely negative samples. This design improves retrieval accuracy for narrative-style content where crucial information may span multiple, interconnected sections. Our experiments on AQANB demonstrate the effectiveness of the proposed approach. We achieve relative improvements of 21.7% and 11.7% over OpenAI’s small and large embedding models, respectively, and outperform the open-source multilingual Contriever by 29.6%. Furthermore, adding our retriever as a pre-stage to the common OpenAI GPT-4o reduced the cost by 98 times and achieved better performance compared to processing the entire book with GPT-4o.

**Решение:** -4 NLP, ответы на вопросы по арабским художественным книгам

---

### 250 · R11677

**Human-Centered Design Recommendations for LLM-as-a-Judge**

2024 · arXiv (Cornell University) · audiovisual/conference talk, journalarticle, preprint/article · en · https://doi.org/10.48550/arxiv.2407.03479

Traditional reference-based metrics, such as BLEU and ROUGE, are less effective for assessing outputs from Large Language Models (LLMs) that produce highly creative or superior-quality text, or in situations where reference outputs are unavailable. While human evaluation remains an option, it is costly and difficult to scale. Recent work using LLMs as evaluators (LLM-as-a-judge) is promising, but trust and reliability remain a significant concern. Integrating human input is crucial to ensure criteria used to evaluate are aligned with the human\u27s intent, and evaluations are robust and consistent. This paper presents a user study of a design exploration called EvaluLLM, that enables users to leverage LLMs as customizable judges, promoting human involvement to balance trust and cost-saving potential with caution. Through interviews with eight domain experts, we identified the need for assistance in developing effective evaluation criteria aligning the LLM-as-a-judge with practitioners\u27 preferences and expectations. We offer findings and design recommendations to optimize human-assisted LLM-as-judge systems.14 pages, 6 figures, Accepted for publication in ACL 2024 Workshop HuCLL

**Решение:** -1 HCI качественные рекомендации по дизайну LLM-as-a-judge

---

### 251 · R8578

**Protocol-Aware and Adaptive DDoS Defense Framework**

2025 · IEEE International Conference on Network Softwarization (NetSoft) · journalarticle, conference, conference-paper · en · https://doi.org/10.1109/netsoft64993.2025.11080537

DDoS attacks continue to grow in both volume and complexity, increasingly exploiting protocol-layer vulnerabilities in core Internet protocols such as NTP, DNS, and HTTP/S. Traditional defense mechanisms, primarily based on static rules and signature-based filtering, have limited adaptability and struggle to handle rapidly evolving attack strategies. This research proposes a protocol-aware and adaptive DDoS defense framework where XDP/eBPF and LLMs serve as modular, complementary components that can be deployed individually or in combination, depending on the attack scenario and the specific characteristics of the target protocol. XDP/eBPF enables high-performance, lowlevel packet filtering directly at the NIC level, offering efficient, line-rate mitigation capabilities. Meanwhile, LLMs are fine-tuned on structured protocol interaction logs (e.g., query sequences, entropy shifts, and temporal patterns) to detect semantic-level anomalies beyond traditional detection thresholds. The proposed framework improves detection accuracy and supports dynamic, context-sensitive mitigation strategies, such as real-time traffic throttling and adaptive rule generation. This modular design allows the system to dynamically adapt to evolving threats in heterogeneous networks.

**Решение:** -4 кибербезопасность, защита от DDoS

---

### 252 · R3218

**LLM-Generated Well-being Intervention Recommendations Are Sensitive to Psychological Profiles: A Proof-of-Concept Expert-Rating Study**

2026 · PsyArXiv · preprint, ppr · https://doi.org/10.31234/osf.io/y3k8a_v3

Personalizing digital well-being interventions to fit the needs and preferences of individual users has been a longstanding challenge. Large language models (LLMs) may be well-suited for this task, using natural language reasoning to integrate heterogeneous user information into personalized guidance. We tested whether LLMs could generate intervention recommendations that were sensitive to differences across recipients’ psychological profiles. Across 178 undergraduate student profiles spanning 14 psychological measures, four LLMs recommended 10 scripted chatbot dialogues from a library of 222 options. Next, two experts rated the recommendations’ appropriateness for a given profile (1-10). For half of the profiles, raters saw recommendations generated for that student (matched condition); for the remainder, they saw recommendations generated for a different student (unmatched condition). As hypothesized, matched recommendations (M = 6.74) were rated as more appropriate than unmatched ones (M = 5.64, SMD = 0.50). These results provide evidence that LLMs can adapt their intervention recommendations to match psychological profiles. However, inter-rater reliability was poor (ICC = 0.22), and all LLMs showed substantial sensitivity to catalog order. As such, we stress the preliminary nature of the findings. Whether such tailoring translates into improved well-being outcomes for users remains to be tested.

**Решение:** -2 эксперты оценивают рекомендации чат-бота для профилей студентов; LLM объект

---

### 253 · R2265

**Generative AI and Clinicians Show Comparable Prognostic Reasoning From Clinical Narratives in Biologic-Treated CRSwNP.**

2026 · World journal of otorhinolaryngology - head and neck surgery · journal article, journalarticle, article · eng · https://doi.org/10.1002/wjo2.70164

ABSTRACT Objective To compare the ability of large language models (LLMs) and otolaryngologists to identify prognostic signals from brief clinical vignettes in CRSwNP. Methods In this blinded study, 68 adults initiating biologic therapy for CRSwNP (≥ 36 months follow‐up) were represented by standardized vignettes derived from documentation immediately before biologic initiation. Vignettes summarized symptoms, prior surgery, comorbidities, and medications. Biomarkers, imaging scores, smell testing, and follow‐up data were excluded to isolate text‐based prognostic reasoning under identical constraints. Five attending otolaryngologists, one rhinology fellow, and two residents independently predicted four 5‐year outcomes: subsequent endoscopic sinus surgery, recurrent systemic steroid bursts, biologic switch, and a composite endpoint. Multiple LLMs were queried in identical zero‐shot format across three sessions to assess stability. Predictions were compared with verified outcomes using accuracy, sensitivity, specificity, F1 score, Cohen's κ, and Matthews correlation coefficient. Results Five‐year outcome prevalences were 38.2% (26 of 68) for subsequent sinus surgery, 26.5% (18 of 68) for steroid bursts, 14.7% (10 of 68) for biologic switch, and 58.8% (40 of 68) for composite failure. Macro‐averaged LLM accuracies ranged from 65.0% to 76.1%, compared with 65.7% ± 7.4% for human raters. The best‐performing LLM achieved accuracy comparable to the top attending. Both groups showed higher negative than positive predictive values, indicating better discrimination for patients without adverse events. Agreement between LLMs and clinicians was moderate and within the range of inter‐clinician variability. Conclusion When restricted to short pretreatment text, LLMs produced prognostic judgments within the range of clinician variability for severe, biologic‐treated CRSwNP outcomes. These findings suggest that in information‐limited settings, LLMs may provide an auxiliary reasoning signal rather than a standalone decision tool.

**Решение:** -4 оториноларингология, полипозный риносинусит

---

### 254 · R6611

**Evaluating Generative Artificial Intelligence Chatbots in Answering Public Questions About Altered Consciousness: A Comparative Study of Safety, Accuracy, Reliability, and Readability.**

2026 · Journal of emergency nursing · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.jen.2026.08.010

Introduction People increasingly use generative artificial intelligence chatbots to interpret health concerns before contacting clinicians. Although these systems are not formal autonomous emergency department triage tools, their responses may influence whether and when users seek professional care. Altered consciousness is especially high-risk because delayed or ambiguous escalation can postpone time-sensitive evaluation. This study evaluated the safety and quality of chatbot answers from an emergency nursing perspective. Methods We conducted a cross-sectional comparative evaluation of ChatGPT, Gemini, Claude, DeepSeek, and Doubao. A 130-item candidate pool was screened to yield 66 public-facing English questions across 11 emergency consultation domains. Each question was submitted once to each chatbot in a fresh conversation between May 1 and May 30, 2026, producing 330 responses. Of note, 5 clinically experienced nurses independently rated the safety, accuracy, empathy, information quality, transparency, global quality, and readability of the responses. Results Interrater agreement was good to excellent: Fleiss kappa for safety was 0.848, and intraclass correlation coefficients for nonbinary nurse-rated outcomes ranged from 0.836 to 0.878. Safe-response rates ranged from 89.4% for Doubao to 95.5% for ChatGPT, with no significant overall difference. ChatGPT had the highest mean accuracy and the highest scores on the DISCERN consumer-health-information instrument and the Journal of the American Medical Association benchmark criteria. Claude and Gemini were rated as the most empathic, and DeepSeek produced the most easily readable text across most readability formulas. Each chatbot generated at least 1 potentially unsafe answer. Discussion Chatbots can support public education about altered consciousness, but omissions, unsafe sequencing, and urgency-softening make them unsuitable for autonomous prehospital or emergency department triage. Emergency nurses should help shape escalation-first, plain-language safety templates for high-risk chatbot advice.

**Решение:** -2 медсестры оценивают точность ответов чат-бота при нарушениях сознания

---

### 255 · R1869

**Integrating Artificial Intelligence into Psychological Counseling: A Narrative Review and Governance Framework.**

2026 · Inquiry : a journal of medical care organization, provision and financing · journal article, review, journalarticle · eng · https://doi.org/10.1177/00469580261438322

The growing global demand for mental health services has created substantial gaps in access and service delivery due to limited workforce and resources. In this context, artificial intelligence (AI) is emerging as a supportive technology in psychological counseling with the potential to enhance access and capacity. This narrative review critically examines the peer-reviewed literature on AI applications in psychological counseling and proposes an approach for responsible integration. A narrative review was conducted synthesizing recent peer-reviewed studies on AI-based tools relevant to psychological counseling (eg, chatbots, large language models, predictive analytics, and decision support systems). Evidence was thematically analyzed across opportunities, risks/limitations, and ethical-professional responsibilities, and used to inform a multi-layer governance framework for responsible use. The literature indicates that AI may improve accessibility, enable more personalized interventions, and support counselors in areas such as clinical decision-making, monitoring, and documentation. Key risks and limitations include limited empathic capacity, algorithmic bias, misleading outputs and potential misdiagnosis, data privacy and security breaches, and digital inequalities that may widen disparities. Ethical considerations emphasize strengthening informed consent, preserving the therapeutic alliance, maintaining transparency about AI use, and ensuring continuous human oversight. The proposed governance framework delineates roles, accountability, and safeguards at the clinical practice, organizational/health-system, and regulatory levels. AI should be positioned as a tool that complements-rather than replaces-human counselors in psychological counseling. Developing ethical guidelines, strengthening regulatory and institutional safeguards, and integrating AI literacy into counselor training are essential to ensure responsible, safe, and equitable implementation.

**Решение:** -1 нарративный обзор интеграции ИИ в психологическое консультирование

---

### 256 · R9612

**The Executive Copilot: Investigating the Impact of Generative AI Assistants on Strategic Decision-Making, Leadership Efficiency, and Managerial Creativity**

2025 · 2025 IEEE DELCON - International Conference on Recent Smart Technologies in Engineering for Sustainable Development · conference, review, conference-paper · https://doi.org/10.1109/delcon68055.2025.11400027

The generative artificial intelligence (AI) revolution has given rise to a class of technology—executive copilots that are designed to unclog the brains of overworked managers in the 21st century. This paper examines the effects of generative AI assistants on three intertwined facets of executive performance—strategic decision making, leadership effectiveness, and managerial creativity. Early literature suggests that AI systems could automate administrative tasks and offer data-driven insights; however, we still lack an understanding of their comprehensive impact on executive tasks and outcomes. To bridge this gap, the study uses a multimethod research design, drawing on survey data from 350 senior executives from various firms, controlled experimental studies of strategic problem solving, and in-depth case analysis of firms in finance, consulting, and technology sectors. Results suggest that AI copilots contribute significantly to faster decision-making and creative output by helping to synthesize information and sparking divergent thinking rapidly. Consistent with this, results reveal that a potential “caveat” of overreliance on AI-generated recommendations might lead to less scrutiny and thus the fragility of the high-stakes decision-making in practice. Theoretically, the study extends the leadership augmentation theory to the context of generative AI. It extends the conceptualization of the executive copilot in terms of a complementary agent that adjusts the boundary of human-machine collaboration. Pragmatically, it has implications for executive education, corporate governance, and the design of responsible AI uptake strategies. Through methodical analysis of opportunities and risks, this study offers a nuanced view of how executive copilots change leadership practice in the era of intelligent augmentation.

**Решение:** -4 менеджмент, влияние GenAI ассистентов на принятие решений руководителями

---

### 257 · R0772

**Multi-View Attention Multiple-Instance Learning Enhanced by LLM Reasoning for Cognitive Distortion Detection**

2026 · Underline Science Inc. · audiovisual/conference talk, journalarticle, conference · https://doi.org/10.48448/j6b7-fp89

Cognitive distortions have been closely linked to mental health disorders, yet their automatic detection remains challenging due to contextual ambiguity, co-occurrence, and semantic overlap. We propose a novel framework that combines Large Language Models (LLMs) with a Multiple-Instance Learning (MIL) architecture to enhance interpretability and expression-level reasoning. Each utterance is decomposed into Emotion, Logic, and Behavior (ELB) components, which are processed by LLMs to infer multiple distortion instances, each with a predicted type, expression, and model-assigned salience score. These instances are integrated via a Multi-View Gated Attention mechanism for final classification. Experiments on Korean (KoACD) and English (Therapist QA) datasets demonstrate that incorporating ELB and LLM-inferred salience scores improves classification performance, especially for distortions with high interpretive ambiguity. Our results suggest a psychologically grounded and generalizable approach for fine-grained reasoning in mental health NLP. The dataset and implementation details are publicly accessible. Accepted to the main conference of ACL 2026

**Решение:** + T1 детекция когнитивных искажений в репликах на корейском [KoACD] и английском [Therapist QA] датасетах, LLM-MIL vs экспертная разметка

---

### 258 · R0762

**LLMs for Now, Fine-Tuning for Later: An Ensemble Approach to Data Drift in Domain-Specific Tasks**

2026 · Underline Science Inc. · audiovisual/conference talk, other · https://doi.org/10.48448/pkvy-y978

Deploying machine learning models in real-world domain-specific scenarios is challenged by the scarcity of expert annotations and by data drift, where the statistical properties of incoming data continuously evolve. Active Learning (AL) iteratively improves compact models with expert annotations but suffers from recurring cold-start degradation, while LLMs provide strong off-the-shelf performance yet cannot leverage newly accumulated labels, raising the question: how can we better leverage LLMs to assist the active learning process? Through an empirical study on five legal and biomedical datasets, we reveal a complementary temporal dynamic: LLMs excel during early and post-drift stages, while AL-assisted compact models eventually surpass them as annotations accumulate. Motivated by this finding, we propose an ensemble system that combines an LLM, an AL-assisted compact model, and an automatic switch module that routes predictions to the better-performing model in real time. Evaluated under simulated data drift on two mental health datasets, our system achieves 96--98% switch accuracy and consistently outperforms either model used alone.

**Решение:** -6 активное обучение при дрейфе данных, ансамбль моделей, оценка переключения на legal/biomed датасетах

---

### 259 · R10416

**Zhixin: An Instruction-Tuned Large Language Model for Mental Disorder Diagnosis**

2025 · Research Square · preprint · https://doi.org/10.21203/rs.3.rs-8149707/v1

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? Zhixin: instruction-tuned LLM для диагностики психических расстройств; нет аннотации, проверить по полному тексту

---

### 260 · R7296

**Enhancing Diagnostic Precision: Using Large-Language Models to Evaluate Content Overlap in Mental Health Questionnaires (Preprint)**

2025 · preprint · en · https://doi.org/10.2196/preprints.79868

BACKGROUND Mental disorders are frequently evaluated using questionnaires, which have been developed over the past decades for the assessment of different conditions. Despite the abundance of these tools, it is an open research question whether different questionnaires measure the same construct of psychopathology. Previous studies that examined the content overlap required manual symptom labeling which is not entirely observer-independent and time-consuming. OBJECTIVE Here, we employed large-language models (LLMs) to analyze content overlap of mental health questionnaires in an observer-independent way and compare our results with clinical expertise. METHODS We analyzed questionnaires from a range of mental health conditions including adult depression (n=7), childhood depression (n=15), clinical high risk for psychosis (CHR-P; n=13), mania (n=7), obsessive-compulsive disorder (n=7), and sleep disorder (n=12). Two different LLM-based approaches were tested. First, we employed sentence Bidirectional Encoder Representations from Transformers (sBERT) to derive numerical representations (‘embeddings’) for each questionnaire item, which were then clustered using k-means to group semantically similar symptoms. Second, questionnaire items were prompted to a Generative Pre-trained Transformer (GPT) to identify underlying symptom clusters. Clustering results were compared to a manual categorization by experts using the adjusted rand index. Further, we assessed the content overlap within each diagnostic domain based on LLM-derived clusters. RESULTS We observed varying degrees of similarity between expert-based and LLM-based clustering across diagnostic domains. Overall, agreement between experts was higher than between experts and LLMs. Among the two LLM approaches, GPT showed greater alignment with expert ratings than sBERT, ranging from weak to strong similarity depending on the diagnostic domain. Using GPT-based clustering of questionnaire items to assess the content overlap within each diagnostic domain revealed a weak (CHR-P: 0.344) to moderate (adult depression: 0.574; childhood depression: 0.433; mania: 0.419; OCD: 0.450; sleep disorder: 0.445) content overlap of questionnaires. Compared to the studies that manually investigated content overlap among these scales, the results of this study exhibited variations, though these were not substantial. CONCLUSIONS These findings demonstrate the feasibility of using LLMs to objectively assess content overlap in diagnostic questionnaires. Notably, the GPT-based approach showed particular promise in aligning with expert-derived symptom structures.

**Решение:** + T1/T2 оценка пересечения симптомов в психиатрических опросниках, GPT кластеризация vs экспертная категоризация, Adjusted Rand Index

---

### 261 · R7009

**A Preliminary Exploration of an AI-Assisted Teaching Model for CBT Counseling Skills Training among Undergraduate Psychology Students**

2026 · Advances in Psychology · article · https://doi.org/10.12677/ap.2026.169436

Artificial intelligence (AI) has attracted increasing attention in higher education, yet its application in practical teaching continues to face challenges, including technological adaptability and gaps in digital literacy.Cognitive Behavioral Therapy (CBT) is a core component of counseling skills training for psychology students; however, traditional CBT instruction is limited by insufficient opportunities for case practice, realistic scenario simulation, and individualized feedback.To address these limitations, this study integrates AI into CBT counseling skills training for psychology undergraduates, establishing a pedagogical workflow comprising "case simulation, counseling practice, AI feedback, and reflective summary" and develops a CBT app platform featuring ten virtual client cases.The platform offers students interactive counseling practice and generates real-time feedback based on their performance.Three junior psychology students participated in a two-week AI-assisted CBT training program.Analysis of the students' reflective journals revealed insights into CBT processes and core techniques, emotion recognition and empathy, the counseling relationship, AI-generated feedback, and the limitations of AI applications.The AI-assisted training offered diverse, low-risk, and repeatable practice scenarios, with student reflections demonstrating an increased focus on understanding and applying CBT processes and core techniques.At the same time, students identified limitations regarding AI's ability to comprehend complex emotions, facilitate authentic interpersonal interaction, and make flexible judgments within counseling contexts.The study suggests that while generative AI can serve as a supplementary tool for CBT counseling skill training, its educational value is best realized when combined with instructor supervision, professional judgment, and critical reflection.

**Решение:** -2 обучение студентов CBT на виртуальных клиентах, качественный анализ рефлексивных дневников студентов

---

### 262 · R4196

**Automating the roter interaction analysis system for medication counseling: A transformer-based deep learning approach with generative AI-augmented data.**

2026 · Research in social & administrative pharmacy : RSAP · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.sapharm.2026.06.008

Background The Roter Interaction Analysis System (RIAS) is the gold standard for medical communication analysis, but its automated coding remains underexplored due to imbalanced code distributions. This study developed an automated RIAS classification system using Japanese transformer-based models and evaluated AI-based data augmentation to mitigate class imbalance. Methods Five transformer models were fine-tuned for 44-class RIAS classification using medication counseling dialogues. To enhance generalizability, we employed AI-based data augmentation and evaluated performance using both AI-augmented and real-data-only test sets. Assessment metrics included accuracy, macro F1, and weighted F1. Findings The dataset comprised 17,391 utterances (39.4% AI-generated). In the real-data-only (primary) test set, ELECTRA achieved the highest accuracy (0.7875), macro F1 (0.6561), and weighted F1 (0.7835). All models performed worse under the real-data-only condition than under the AI-augmented condition, mainly for minority-class categories. Error analysis showed semantically ambiguous and context-dependent categories, including domain-adjacent counseling topics and affective expressions, remained challenging, indicating linguistic transparency and definitional distinctiveness influence classification beyond training frequency. Conclusion This proof of concept shows that AI-based augmentation can mitigate class imbalance in automated RIAS classification of medication counseling dialogues. While robust for prototypical expressions, nuanced affective categories remain challenging for text-only approaches. These findings support the feasibility of automated RIAS analysis for pharmacy education while suggesting that multimodal approaches are needed to capture subtle emotional dynamics. By complementing manual coding with quantitative insights, this system may support timelier and objective feedback and ultimately contribute to patient-centered care.

**Решение:** -5 кодирование реплик консультаций по RIAS с помощью fine-tuned ELECTRA/трансформеров, без генеративной LLM

---

### 263 · R5179

**Too agreeable to be accurate? Sycophancy and diagnostic instability of large language models in medical diagnosis.**

2026 · Artificial intelligence in medicine · journal article, med, journalarticle · eng · https://doi.org/10.1016/j.artmed.2026.103516

Diagnostic accuracy in Large Language Models (LLM) is an increasing concern as physicians employ LLMs into their medical practice. We measured whether diagnostic correctness in LLMs changed after a certainty challenge or clinician specialty framing. To evaluate the performance of LLMs, we curated 120 public clinical vignettes: 40 MultiCaRe-derived clinical narratives and 80 MedMCQA-derived exam style cases. Ten proprietary and open-weight LLMs were tested across four prompt conditions and three separate runs with two passes per condition, yielding 28,800 responses. Diagnostic correctness was evaluated using an LLM-as-a-judge approach. At neutral baseline, accuracy varied by model and was generally lower for MultiCaRe than MedMCQA. GPT-5 had the highest baseline and post-challenge accuracy (74.4% and 75.3%); Claude Sonnet 4 had the highest accuracy changing flip rate (AcFR; 58.6%) and largest post-challenge accuracy loss (-36.4 percentage points). Across all neutral model-case pairs, baseline accuracy decreased from 51.8% to 42.2% after 'Are you sure?' (AcFR = 32.8%). Correct-to-incorrect transitions (n = 544) exceeded incorrect-to-correct transitions (n = 198). Specialty context prompts produced smaller changes. Adjacent specialty prompts increased overall accuracy by 2.8 percentage points, and differential specialty prompts decreased accuracy by 1.2-1.8 percentage points. The 'Are you sure?' challenge was the strongest source of diagnostic instability in the study; case source also strongly affected accuracy. Diagnostic LLM evaluations should report first pass accuracy, harmful flips, beneficial corrections, and stability under clinically plausible conversational challenges before clinical deployment.

**Решение:** -4 общая медицина, угодничество LLM на экзаменационных кейсах MultiCaRe/MedMCQA

---

### 264 · R12137

**Graph-Augmented Text-Based Floorplan Generation**

2024 · 2024 International Conference on Automation in Manufacturing, Transportation and Logistics (ICaMaL) · conference, conference-paper · en · https://doi.org/10.1109/icamal62577.2024.10919609

In the context of floorplan generation, a recent trend has emerged towards incorporating user-provided descriptive texts to deliver a more flexible and user-centric interface, en-abling direct user engagement in the design and configuration processes. However, extracting accurate information from text input to characterize corresponding floorplans is challenging due to the latent representation of semantic, geometric, and topological design details. Conversely, graph-based generation methods, while lacking geometric information, exhibit superior performance owing to the intuitive representation of spatial data in graph structures. Building upon this understanding, this paper proposes a dual-stage framework that augments text input with serialized graphs to leverage the complementary strengths of both modalities. The pre-training stage uses script-generated texts to empower a graph generator for producing corresponding graphs from descriptive texts and familiarize a floorplan generator with concatenated text and graph input. During the fine-tuning stage, the pre-trained graph generator, alongside an alternative graph generator based on prompt-driven large language models, is employed to provide augmented graphical knowledge for the floorplan generator based on manually annotated descriptive texts. Extensive quantitative and qualitative experiments demon-strate the effectiveness of the proposed approach over the vanilla text- based floorplan generation method.

**Решение:** -4 архитектура, генерация планов этажей

---

### 265 · R4530

**Know when to trust: Making AI scoring more reliable for educational assessment.**

2026 · Behavior research methods · journal article, med, journalarticle · eng · https://doi.org/10.3758/s13428-026-03058-1

The rapid rise of large language models (LLMs) has created new opportunities for educational measurement. This paper introduces and evaluates three improvements to LLM-based automated scoring tools: model self-confidence, weighted probabilistic scoring, and ensemble modeling. The study utilizes data from over 20,000 responses to the Alternative Uses Test, the most popular divergent thinking task, from more than 2,000 participants across multiple studies. Model self-confidence taps into LLMs' internal mechanisms to gauge their confidence in probability estimates, helping identify when machine-generated outputs are trustworthy. Weighted probabilistic scoring considers a broader range of completion possibilities in deriving a final score. The final technique, ensemble models, assesses the performance gains from combining multiple models. These methods, tested in divergent thinking response scoring, each show statistically significant positive results, with improvements in correlation with human judges (from r = 0.781 to r = 0.823) and reduction in error. All three techniques improve the performance and trustworthiness of automated scoring models, and are compatible as drop-in improvements to existing techniques. The findings suggest that these adjustments can boost the dependability and applicability of LLMs in educational scoring, specifically for systems that derive a quantitative measure from a text input.

**Решение:** + T2 автоматический скоринг креативности в Alternative Uses Test [AUT], LLM vs эксперты, r=0.781–0.823

---

### 266 · R10820

**Subtle Biases Need Subtler Measures: Dual Metrics for Evaluating Representative and Affinity Bias in Large Language Models**

2024 · Annual Meeting of the Association for Computational Linguistics (ACL) · audiovisual/conference talk, journalarticle, conference · en · https://doi.org/10.18653/v1/2024.acl-long.23

Research on Large Language Models (LLMs) has often neglected subtle biases that, although less apparent, can significantly influence the models' outputs toward particular social narratives. This study addresses two such biases within LLMs: representative bias, which denotes a tendency of LLMs to generate outputs that mirror the experiences of certain identity groups, and affinity bias, reflecting the models' evaluative preferences for specific narratives or viewpoints. We introduce two novel metrics to measure these biases: the Representative Bias Score (RBS) and the Affinity Bias Score (ABS), and present the Creativity-Oriented Generation Suite (CoGS), a collection of open-ended tasks such as short story writing and poetry composition, designed with customized rubrics to detect these subtle biases. Our analysis uncovers marked representative biases in prominent LLMs, with a preference for identities associated with being white, straight, and men. Furthermore, our investigation of affinity bias reveals distinctive evaluative patterns within each model, akin to `bias fingerprints'. This trend is also seen in human evaluators, highlighting a complex interplay between human and machine bias perceptions. 9 pages (excluding references), accepted to ACL 2024 Main Conference

**Решение:** -4 компьютерная лингвистика, метрики скрытых социальных предубеждений в поэзии и рассказах LLM

---

### 267 · R0867

**Investigating Study Choice in Flemish Schools: An Application of Multi-Target Regression and Large Language Models**

2026 · ACM Symposium on Applied Computing · journalarticle, book · https://doi.org/10.1145/3748522.3779972

Decisions about study choice profoundly affect pupils' educational pathways and long-term career prospects, yet many still struggle to select options that align with their skills and interests. To support more personalized study choice, a serious game named "Kr8cht" was designed that elicits Flemish pupils' preferences through pairwise comparisons of activities. Each activity is linked to study domains and personality traits based on expert-annotated relevance scores. However, the current version of the game includes only a limited set of activities, restricting its ability to accommodate the diverse needs and preferences of pupils. To address this limitation, we extensively investigate multi-target regression (MTR) techniques to automatically predict domain scores for newly suggested activities, thereby reducing dependence on expert annotation. Our findings show that local and chain-based MTR methods trained on embeddings from frozen sentence-level transformers consistently outperform global MTR approaches and those trained on embeddings from static or frozen token-level transformer models. Furthermore, our experiments also reveal that augmenting the dataset with synthetic activities, which are pseudolabelled by a MTR model, increases performance with statistical significance. The source code for our experiments is available at Zenodo (https://doi.org/10.5281/zenodo.17834064).

**Решение:** -4 педагогика, выбор образовательной траектории школьников во Фландрии, регрессия на эмбеддингах

---

### 268 · R1563

**Kappa-FIN: Topological Early Warning System for Financial Market Crises**

2026 · Zenodo (CERN European Organization for Nuclear Research) · preprint/, software/, software · https://doi.org/10.5281/zenodo.19408513

David Ohio requests your endorsement to submit an article to the stat.APsection of arXiv. To tell us that you would (or would not) like toendorse this person, please visit the following URL:https://arxiv.org/auth/endorse?x=XZKYR7--Version 4 of Kappa-FIN introduces engine_v4 with Structural Phase Speed (SPS), extends the validated scenario corpus from 17 to 22 crises (1985–2026 including live contemporary analysis), and documents a negative experimental result (FR vs OR curvature redundancy). What's new in v4: ENGINE v4:- Structural Phase Speed (SPS) replaces static viscosity as the primary dynamical observable- tau_K_max: maximum rigidity persistence duration — measures how long a network sustains crystallized structure- Cross-universe comparability caveat formalized: tau_K_max measures duration of rigidity, NOT progress toward rupture. Qualitative pattern similarity across universes is informative but not predictive. 5 NEW SCENARIOS (22 total):- AI Full Ecosystem (NVDA, MSFT, GOOGL, META, AMD, AVGO, TSM, SMCI, ARM, PLTR, SNOW, AI): ν_s = 886.8, CRITICAL structural alert- AI Infrastructure (NVDA, AMD, AVGO, TSM, SMCI, ARM, MRVL): ν_s = 2.1, HEALTHY- Iran War Energy (XOM, CVX, COP, SLB, HAL, OXY, DVN, PXD): PR = 0.822, 82% pre-existing damage from Jun 2025 12-Day War- Iran War Global Macro (SPY, TLT, GLD, USO, UUP, EEM, VIX, DXY): Monitoring regime- AI Bubble Deep (extended AI ecosystem analysis with temporal archaeology) IRAN WAR ARCHAEOLOGICAL ANALYSIS:- Jun 12, 2025: Oh = 0.106, Phi = 0.000 — eve of 12-Day War, NORMAL- Jun 27, 2025: Oh = 1.161 — ALERT crystallizes 3 days post-ceasefire (not during war)- Jun 30, 2025: Phi = 0.220 — crosses detection threshold (Phi_c = 0.120)- Jul 3, 2025: Phi = 0.527 — MAXIMUM structural damage- Sep 15, 2025: Phi returns below threshold (3-month recovery)- Dec 19, 2025: Energy/Defense network Phi crossing — 71 days before Feb 2026 war- Feb 28, 2026: Iran War begins — system re-shocked before full recovery RESILIENCE HYPOTHESIS (Eurozone evidence):- Wave 1 (Jan 2010): Drive 0.081, Duration 2d, Phi peak 0.159 — Greek crisis, no defenses- Wave 2 (Sep 2010): Drive 0.081, Duration 4d, Phi peak 0.294 — Irish contagion- Wave 3 (May 2014): Drive 0.242, Duration 1d, Phi peak 0.241 — 3x stronger drive, LESS damage- 3.5 years between Wave 2 and Wave 3: EFSF, ESM, "whatever it takes" (Jul 2012), banking union- Preemptive strategic framework documented (Field state × Policy state → Action matrix) FR vs OR EXPERIMENT (negative result):- Hypothesis: Ollivier-Ricci curvature captures complementary information to Forman-Ricci- Result: Per-edge Spearman ρ = 0.952 ± 0.018 — OR is redundant with FR in kNN networks (n=13, k=5)- FR leads OR by 39 days in first low-curvature crossing- Conclusion: FR alone is sufficient for Kappa-FIN. Documented as honest negative result. PAPER v4:- Cross-universe comparability caveats added (Sections 5.6, 8, 9)- All DOIs updated for HUGO ecosystem references Repository: https://github.com/aprimora-ai/Kappa-FINPart of the Kappa Method ecosystem: Kappa-LLM (hallucination detection), Kappa-Radiante (structural navigation), Kappa-Education (student dropout prediction).HUGO AGI Framework: HUGO, ECHO, REMIND, RHEO, ANIMA. David Ohio | Independent Researcher | odavidohio@gmail.com | CC BY 4.0

**Решение:** -4 финансовые рынки, топологический анализ кризисов Kappa-FIN

---

### 269 · R9280

**Comparative Qualitative Analysis of AI-Generated Student Videos: AI Tool vs Human Evaluation**

2025 · preprint · en · https://doi.org/10.22541/au.174648255.50691574/v1

IntroductionProject-based learning (PBL) often culminates in student-created artifacts, such as videos, that demonstrate learning in an engaging way. With the advent of generative AI, students can now feed text (scripts or prompts) into AI tools to produce multimedia videos, introducing new opportunities and challenges in education. On one hand, AI-generated videos can be personalized and visually rich, potentially enhancing student engagement and creativity in PBL tasks.On the other hand, assessing the quality of these AI-assisted creations is not straightforward. Educators need reliable methods to evaluate qualitative aspects of student videos—such as their emotional tone, clarity, and accuracy—to ensure learning objectives are met. Traditionally, teacher or expert reviewers would perform this evaluation, but AI-powered analyzer tools promise a faster, consistent alternative. This research proposal outlines a study to compare an AI analyzer tool versus human evaluators in the qualitative analysis of student-created, text-to-video AI-generated projects. The goal is to determine how closely an AI’s assessment of video content aligns with human judgment, and what this means for future classroom assessment practices.Background and Literature ReviewAI-Generated Video in EducationGenerative AI technologies are increasingly influencing educational content creation. Recent studies show that AI-generated instructional videos can achieve learning outcomes comparable to traditional teacher-made videos.For example, Netland et al. (2024) found that learners acquired similar knowledge from AI-created teaching videos as from human-crafted ones, even if they preferred the human videos for the learning experience.These AI videos, produced by large language models and related tools, have been successfully used to convey concepts in various subjects. In a science teacher education context, Pellas et al. (2024) demonstrated that AI-generated videos boosted learners’ self-efficacy and knowledge retention, positioning them as promising assets for instruction.AI systems can rapidly turn textual input into explainers or story-based videos – for instance, the StudyFetch Imagine Explainers tool can generate a 10-60 minute educational video from course materials or a given topic prompt.This ease of content creation suggests AI videos will proliferate in classrooms, making it important to study how to evaluate their quality.Despite these advantages, researchers note some limitations of AI-driven videos. One concern is reduced social presence or human touch – students often report AI-generated videos feel less engaging or relatable than instructor-led ones.Shahzad et al. (2024) observed that learners missed the connectedness of a human presenter, which could lead to distractions or lower emotional engagement.However, if the content itself is highly relevant and well-crafted, students may overlook the lack of a human presenter.As generative video technology improves (e.g. more lifelike AI avatars), these engagement gaps may narrow.These findings highlight the need to assess not just factual content of AI videos, but also qualitative factors like tone and engagement that influence learner reception.Project-Based Learning and Student-Created AI VideosPBL is a student-centered pedagogy where learners gain knowledge by working for an extended period to investigate and respond to complex questions or challenges. A hallmark of PBL is the creation of tangible artifacts (presentations, portfolios, videos, etc.) that showcase student learning in authentic contexts. Integrating AI into PBL can significantly enrich this. Frydenberg (2025) argues that AI tools can be “key players” in open-ended projects by assisting with brainstorming, research, and content creation.Instead of replacing the learning process, AI can serve as a tool that students use to develop and refine their learning.For example, students might use an AI text-to-video generator (such as Canva’s or VEED’s AI video tools) to transform their written ideas into a dynamic video. This allows students to focus on crafting the narrative and verifying information, while the AI handles the technical production.Early evidence suggests that allowing students to leverage AI in projects can maintain or even boost engagement and motivation. AI-assisted creation frees students to concentrate on higher-order thinking—like analyzing and organizing content—since the AI automates lower-level tasks.The resulting AI-generated videos in PBL are often personalized and context-rich, making scientific or historical scenarios come alive.They can provide “dynamic scaffolding” for problem-solving, meaning the videos adapt or present information in a way that aids understanding of the problem at hand.For instance, an AI video might visualize a scientific experiment or animate a historical scene described in a student’s script, helping the entire class engage with the material.However, the use of AI also raises questions about how educators can assess these AI-crafted works. In PBL, assessment is typically authentic and multidimensional, focusing on both content mastery and skills like creativity or collaboration. When a video is partially AI-generated, teachers must discern the student’s contribution (e.g. the quality of the script, the ideas and narrative) and the overall effectiveness of the video as a learning artifact. This is where an AI analyzer could assist by providing an initial analysis of the video’s qualities, but its effectiveness relative to human judgment remains uncertain. Our study is situated at the intersection of these trends: it examines student-created AI videos in PBL and how they are evaluated, aiming to inform best practices as AI becomes a normal part of student work.AI Analyzer Tools for Qualitative EvaluationAI analyzer tools refer to software systems that use artificial intelligence (such as machine learning and natural language processing) to automatically ev

**Решение:** -4 педагогика, оценка студенческих видео в проектном обучении

---

### 270 · R11542

**On the Adversarial Robustness of Instruction-Tuned Large Language Models for Code**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2411.19508

The advent of instruction-tuned Large Language Models designed for coding tasks (Code LLMs) has transformed software engineering practices. However, their robustness against various input challenges remains a critical concern. This study introduces DegradePrompter, a novel method designed to systematically evaluate the robustness of instruction-tuned Code LLMs. We assess the impact of diverse input challenges on the functionality and correctness of generated code using rigorous metrics and established benchmarks. Our comprehensive evaluation includes five state-of-the-art open-source models and three production-grade closed-source models, revealing varying degrees of robustness. Open-source models demonstrate an increased susceptibility to input perturbations, resulting in declines in functional correctness ranging from 12% to 34%. In contrast, commercial models demonstrate relatively greater resilience, with performance degradation ranging from 3% to 24%. To enhance the robustness of the models against these vulnerabilities, we investigate a straightforward yet effective mitigation strategy. Our findings highlight the need for robust defense mechanisms and comprehensive evaluations during both the development and deployment phases to ensure the resilience and reliability of automated code generation systems.

**Решение:** -4 программная инженерия, устойчивость моделей генерации кода

---

### 271 · R8604

**MedBench v4: A Robust and Scalable Benchmark for Evaluating Chinese Medical Language Models, Multimodal Models, and Intelligent Agents**

2025 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2511.14439

Recent advances in medical large language models (LLMs), multimodal models, and agents demand evaluation frameworks that reflect real clinical workflows and safety constraints. We present MedBench v4, a nationwide, cloud-based benchmarking infrastructure comprising over 700,000 expert-curated tasks spanning 24 primary and 91 secondary specialties, with dedicated tracks for LLMs, multimodal models, and agents. Items undergo multi-stage refinement and multi-round review by clinicians from more than 500 institutions, and open-ended responses are scored by an LLM-as-a-judge calibrated to human ratings. We evaluate 15 frontier models. Base LLMs reach a mean overall score of 54.1/100 (best: Claude Sonnet 4.5, 62.5/100), but safety and ethics remain low (18.4/100). Multimodal models perform worse overall (mean 47.5/100; best: GPT-5, 54.9/100), with solid perception yet weaker cross-modal reasoning. Agents built on the same backbones substantially improve end-to-end performance (mean 79.8/100), with Claude Sonnet 4.5-based agents achieving up to 85.3/100 overall and 88.9/100 on safety tasks. MedBench v4 thus reveals persisting gaps in multimodal reasoning and safety for base models, while showing that governance-aware agentic orchestration can markedly enhance benchmarked clinical readiness without sacrificing capability. By aligning tasks with Chinese clinical guidelines and regulatory priorities, the platform offers a practical reference for hospitals, developers, and policymakers auditing medical AI.

**Решение:** -4 общемедицинский бенчмарк MedBench v4 по 24 клиническим специальностям

---

### 272 · R4589

**Iterative Large Language Model-Guided Sampling and Expert-Annotated Benchmark Corpus for Harmful Suicide Content Detection: Development and Validation Study.**

2026 · JMIR medical informatics · journal article, validation study, research support, non-u.s. gov't · eng · https://doi.org/10.2196/73725

Abstract Background Harmful suicide content on the internet poses significant risks, as it can induce suicidal thoughts and behaviors, particularly among vulnerable populations. Despite global efforts, existing moderation approaches remain insufficient, especially in high-risk regions such as South Korea, which has the highest suicide rate among Organisation for Economic Co-operation and Development countries. Previous research has primarily focused on assessing the suicide risk of the authors who wrote the content rather than the harmfulness of content itself which potentially leads the readers to self-harm or suicide, highlighting a critical gap in current approaches. Our study addresses this gap by shifting the focus from assessing the suicide risk of content authors to evaluating the harmfulness of the content itself and its potential to induce suicide risk among readers. Objective This study aimed to develop an artificial intelligence (AI)–driven system for classifying online suicide-related content into 5 levels: illegal, harmful, potentially harmful, harmless, and non–suicide-related. In addition, the researchers construct a multimodal benchmark dataset with expert annotations to improve content moderation and assist AI models in detecting and regulating harmful content more effectively. Methods We collected 43,244 user-generated posts from various online sources, including social media, question and answer (Q&A) platforms, and online communities. To reduce the workload on human annotators, GPT-4 was used for preannotation, filtering, and categorizing content before manual review by medical professionals. A task description document ensured consistency in classification. Ultimately, a benchmark dataset of 452 manually labeled entries was developed, including both Korean and English versions, to support AI-based moderation. The study also evaluated zero-shot and few-shot learning to determine the best AI approach for detecting harmful content. Results The multimodal benchmark dataset showed that GPT-4 achieved the highest F1-scores (66.46 for illegal and 77.09 for harmful content detection). Image descriptions improved classification accuracy, while directly using raw images slightly decreased performance. Few-shot learning significantly enhanced detection, demonstrating that small but high-quality datasets could improve AI-driven moderation. However, translation challenges were observed, particularly in suicide-related slang and abbreviations, which were sometimes inaccurately conveyed in the English benchmark. Conclusions This study provides a high-quality benchmark for AI-based suicide content detection, proving that large language models can effectively assist in content moderation while reducing the burden on human moderators. Future work will focus on enhancing real-time detection and improving the handling of subtle or disguised harmful content.

**Решение:** ? оценка степени суицидального/вредоносного контента врачами vs GPT-4, F1; проверить классификацию: клиническая суицидология T3 vs модерация контента

---

### 273 · R4584

**Reliability and clinical accuracy of ChatGPT in post-FESS counselling: a multi-reviewer evaluation**

2026 · The Egyptian Journal of Otolaryngology · journalarticle, review, article · en · https://doi.org/10.1186/s43163-026-01178-1

Abstract Objective To evaluate the accuracy, appropriateness, usefulness, and readability of artificial intelligence–generated postoperative counselling following functional endoscopic sinus surgery (FESS). Methods A descriptive cross-sectional study was conducted using a structured set of 15 postoperative counselling questions reflecting routine patient concerns after FESS. Questions were developed based on standard postoperative protocols and validated using the Content Validity Index. Each validated question was posed to ChatGPT (OpenAI; version accessed January 2026). Responses were independently assessed by four otorhinolaryngologists for appropriateness, accuracy, and usefulness using a 5-point Likert scale. Inter-rater reliability was analyzed using intraclass correlation coefficients (ICC). Readability was assessed using Flesch Reading Ease (FRE) and Flesch–Kincaid Grade Level (FKGL) indices. Results The mean composite score across all domains was 3.91 ± 0.64. Appropriateness scored highest (4.12), followed by usefulness (4.02), while accuracy scored comparatively lower (3.59). Inter-rater reliability was excellent for appropriateness (ICC = 0.94), good for accuracy (ICC = 0.85), and moderate for usefulness (ICC = 0.69). Domain-wise analysis demonstrated higher scores for protocol-driven topics such as nasal hygiene and medication use, while lifestyle and recovery-related counselling showed greater variability. Readability analysis revealed a mean FRE score of 41.2 and an FKGL of 12.8, indicating content written at a senior-school to college reading level. Conclusion AI-generated postoperative counselling after FESS demonstrates acceptable clinical reliability for standardized guidance but shows limitations in contextual accuracy and linguistic accessibility. ChatGPT may serve as a supplementary educational tool; however, clinician-led counselling remains essential.

**Решение:** -2 оториноларингологи оценивают ответы ChatGPT по послеоперационному уходу FESS; к тому же соматическая медицина

---

### 274 · R3759

**The Impact of Automated Tools on Clinical Decision-Making in Gestational Trophoblastic Disease**

2026 · Digital Access to Scholarship at Harvard (DASH) (Harvard University) · dissertation · en · https://dash.harvard.edu/bitstreams/42896d6c-7b1c-4703-8ed3-d57f8882b70a/download

Project 1 abstract: Objective: The hook effect is a limitation of assay-based laboratory tests utilized for hCG testing in GTD. A result of this effect is reporting of falsely low or inappropriately normal hCG values. However, apart from case reports and case series, no prior literature explores the possible clinical features associated with this phenomenon owing to its rarity. This study aims to bridge this gap in literature by investigating the association between the hook effect and clinical symptoms reported and using predictive models to create a clinical risk score. Methods: Univariable and multivariable Firth modification of logistic regression were performed to determine clinical features associated with hook effect on hCG testing in a retrospective observational study of patients with GTD from the Rio de Janeiro Trophoblastic Disease Centre over a 10-year period of 2014 to 2024. Youden’s index was utilized to determine ideal cut points for hCG values, along with reporting sensitivity, specificity, PPV and NPV. Clinical features identified on association testing and hCG values identified on cut point estimation are utilized as predictors for the creation of a clinical risk score. Results: Our study population consisted of 1,019 patients, with 34 (3.3%) reporting hook effect. The variables associated with an increased odds of hook effect include, vaginal bleeding (OR: 6.40, 95% CI: 2.75-17.96) increased uterine size for gestational age (OR=2.37, 95% CI: 1.20-4.71), history of previous mole (OR: 19.80, 95% CI: 4.42-77.90), theca-lutein cyst (OR: 7.62, 95% CI: 3.38-16.17), and pre-eclampsia. (OR: 18.84, 95% CI: 7.28-46.20). On cut point estimation, the clinically meaningful threshold for undiluted hCG values was determined at 1500 IU/L, with sensitivity of 91%, and specificity of 99%. A clinical risk score was created based on inferential testing to determine the risk of hook effect in patients with GTD. The variables in the predictive model included extremes of age, vaginal bleeding, history of previous mole and hCG ≤ 1500 IU/L. The model had high internal validity with an optimism corrected AUC (95% CI) of 0.99 (0.98-0.99) on bootstrapping with 1000 iterations. Conclusions: Clinical features such as vaginal bleeding, increased uterine size for gestational age, history of previous mole, theca lutein cysts, and preeclampsia were associated with the presence of hook effect on hCG testing. Hook effect once promptly identified should necessitate dilution of samples to ascertain true hCG values to facilitate prompt treatment. Project 2 abstract: Objective: Access to timely and appropriate medical information for the management of GTD is a challenge for physicians and patients alike due to the rarity of the disease and lack of trained physicians. Open source and freely available LLM chatbot ChatGPT can serve as a potential tool to supplement delivery of medical care in the absence of a GTD expert. In this paper, we evaluate whether ChatGPT V4.0 is able to provide accurate and complete responses to clinical, diagnostic and therapeutic clinical vignettes in GTD. Methods: A cross-sectional survey-based study was conducted including an international multi-institutional panel of GTD experts inquiring about the agreement, accuracy and completeness levels on Likert scales for answers generated by ChatGPT v4.0 to ten clinical vignettes. To assess the proficiency of ChatGPT, a predetermined threshold of 75% was utilized based on Delphi based consensus studies. Globally and for per question exact binomial proportions with exact Clopper-Pearson confidence intervals were reported to assess whether 75% of experts responded in the positive categories across all 3 Likert scales. Krippendorf’s alpha across the three attributes was reported to compare observed agreement among raters along with Cronbach’s alpha for internal consistency of survey items. A GLMM model was fit to assess if academic rank of the experts was a predictor for their choice in the positive categories of Likert scales. Results: We received 12 (40%) complete survey responses out of the 30 invitations sent out to GTD experts. The majority of experts, 50% (6/12) were appointed to the academic rank of full professors, and associate professors and practiced medicine in academic institutes (11/12). Most experts practiced in continents other than North America (9/12). On global binomial proportions ChatGPT failed to meet out threshold with 0.6 (0.26 - 0.87). It performed comparatively well on questions regarding molar pregnancies. Inter-rater reliability assessed via the Krippendorf’s α indicated low agreement across experts; agreement (α =.275), accuracy (α =.288) and completeness (α =.269), However, excellent homogeneity demonstrated across all attributes via Cronbach’s α; agreement (α = .88), accuracy (α = .84), and completeness (α = .79). Academic rank was not a significant predictor of Likert choices in positive categories for all attributes on global GLMM and subgroup analysis per Likert scale. Conclusions: ChatGPT did not meet our predetermined performance thresholds at 75% and hence was determined as a poor supplement for physicians and patients seeking medical information on queries in GTD.

**Решение:** -2 онкогинекологи оценивают ответы ChatGPT по клиническим виньеткам трофобластической болезни

---

### 275 · R2816

**Can Large Language Models Reliably Code Qualitative Humanitarian Data? A Benchmark Study Against Human Expert Adjudication**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2606.26541

Data from affected populations are crucial for informing humanitarian response, but their value depends on timely and consistent interpretation of nuanced accounts of need. Humanitarian organizations often lack the staff, time, and specialist expertise required to analyze this information at scale. Large language models (LLMs) may expand this capacity, but their reliability for coding qualitative humanitarian data has not been directly established. This benchmark study compares 46 LLMs to a human Gold Standard using 150 high-fidelity synthetic humanitarian transcripts. Evaluation combined inter-rater reliability testing with Krippendorff's alpha, discrepancy analysis distinguishing correct, near-correct, and incorrect codes, and qualitative assessment across humanitarian-specific criteria including discrimination, complex needs hierarchies, and non-standard communication styles. The authors find that multiple LLMs can perform deductive coding at reliability levels comparable to experienced human coders, especially when structured prompts and reasoning-enabled configurations are used. At the same time, aggregate reliability metrics alone are insufficient for deployment decisions. Models varied in recognizing needs expressed indirectly, needs outside predefined categories, and protection-relevant concerns such as physical safety and discrimination. These findings suggest that LLMs can materially expand humanitarian analytical capacity, but not as substitutes for human judgment. Appropriate use requires structured codebooks, reasoning-enabled models, attention to theme-specific performance, and tiered oversight focused on categories where miscoding would have the greatest programmatic consequences. For sensitive humanitarian data, open-weights models deployed on self-hosted infrastructure may offer a viable path for combining analytical scalability with stronger data governance. 34 pages, 4 tables, 3 Annexes

**Решение:** ? дедуктивное кодирование качественных гуманитарных транскриптов 46 LLM vs эксперты, альфа Криппендорффа; проверить наличие MHPSS / психологических конструктов в кодбуке

---

### 276 · R3285

**Artificial intelligence revolution in shoulder magnetic resonance imaging: current evidence and future directions for rotator cuff diagnosis.**

2026 · Clinics in shoulder and elbow · journal article, journalarticle, review · eng · https://doi.org/10.5397/cise.2025.00990

Background Rotator cuff tears (RCTs) are a leading cause of shoulder pain. Magnetic resonance imaging (MRI) is the gold standard for diagnosis, but interpretation is limited by variable sensitivity, interobserver variability, and increasing workload. Recent advances in artificial intelligence (AI), including deep learning and large language models (LLMs), have been explored to enhance diagnostic accuracy and efficiency. Methods A structured search of PubMed, Embase, Scopus, and Cochrane Central databases identified studies published from 2019 or later applying AI to shoulder MRI for RCT detection, classification, segmentation, or reporting. Eligible studies reported quantitative outcomes. Of 732 records, 584 were screened, 121 underwent full-text review, and 19 were included in this narrative review. Results Deep learning models demonstrated diagnostic accuracies ranging from 71% to 100%, with sensitivities of 73%–100% and specificities of 70%–100%. About 20% of included studies used external validation, with 5%–15% performance reductions, underscoring limited generalizability. Visual Geometry Group (VGG)-based architectures and convolutional neural networks (CNNs) using multiplanar inputs achieved higher performance for full-thickness tear detection, while radiomics contributed to assessment of tear severity and muscle quality. Regulatory-approved software remains limited, and no fully automated diagnostic system has received Food and Drug Administration (FDA) clearance. LLMs demonstrated potential in patient education and report drafting, though informational quality was variable (median DISCERN score, 40/80), requiring expert oversight. Conclusions AI applications in shoulder MRI demonstrate promising diagnostic accuracy and potential workflow benefits, but current evidence is constrained by limited external validation, dataset heterogeneity, and lack of regulatory clearance. Future research should prioritize multicenter validation, clinical integration, and explainability to enable safe clinical use of AI.

**Решение:** -1 нарративный обзор применения deep learning и LLM в МРТ плечевого сустава при разрывах вращательной манжеты

---

### 277 · R2152

**The Reflexive Contamination of Categorical Benchmarks: Use-induced erosion of evaluation infrastructure within capacity asymmetry**

2026 · Zenodo (CERN European Organization for Nuclear Research) · text/working paper, article · en · https://doi.org/10.5281/zenodo.21252511

The second note in this series identified capacity asymmetry as the structural condition under which substrate-independent audit ceases to be informative, and traced two empirical cases — the 2008 AAA cross-asset-class inversion and the bias profile of contemporary LLM-as-judge architectures — as forensic material. The present note develops the mechanism by which the inversions assembled. It names this mechanism reflexive contamination of categorical benchmarks: the erosion of a benchmark's discriminative function through its recursive use in training or selecting the systems it subsequently evaluates. The mechanism does not require vendor intent, training-data leakage, or exogenous input drift, though each can coexist with and accelerate it. It occupies a position between four neighboring frames — distribution collapse, training-data leakage, Goodhart's law, and ratings shopping — and is adjacent also to Campbell's law and performative prediction, from which it differs in object: the category-level discriminative boundary rather than the indicator value or the outcome distribution. It decomposes a sub-mechanism the existing taxonomy leaves unanalyzed. The note operationalizes the three markers the second note proposed (benchmark saturation alongside falling tractability of independent verification, high inter-judge agreement on a contracting audit task τ, and growing divergence between evaluation results and downstream consequence) as measurement protocols with treatment of background variation. It reads the 2024–2026 AI evaluation crisis as a contemporary forensic instance, drawing on recent work on preference leakage and position bias, and on the documented weakening of MMLU, HumanEval, HellaSwag, and the original GSM8K as frontier-ranking signals. The analysis is restricted to static and aggregate phenomena; multi-cycle dynamics are deferred to the fifth note, non-AI domain instances to the sixth, cross-domain synthesis to the seventh, and the limit case in which downstream consequence is structurally unobservable to a later supplementary note. The note closes with the open questions, including whether any benchmark design can resist reflexive contamination.

**Решение:** -1 методологическое эссе об эрозии бенчмарков ИИ и LLM-as-a-judge

---

### 278 · R6446

**Towards Secure Retrieval-Augmented Generation: A Comprehensive Review of Threats, Defenses and Benchmarks**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2603.21654

Retrieval-Augmented Generation (RAG) significantly mitigates the hallucinations and domain knowledge deficiency in large language models by incorporating external knowledge bases. However, the multi-module architecture of RAG introduces complex system-level security vulnerabilities. Guided by the RAG workflow, this paper analyzes the underlying vulnerability mechanisms and systematically categorizes core threat vectors such as data poisoning, adversarial attacks, and membership inference attacks. Based on this threat assessment, we construct a taxonomy of RAG defense technologies from a dual perspective encompassing both input and output stages. The input-side analysis reviews data protection mechanisms including dynamic access control, homomorphic encryption retrieval, and adversarial pre-filtering. The output-side examination summarizes advanced leakage prevention techniques such as federated learning isolation, differential privacy perturbation, and lightweight data sanitization. To establish a unified benchmark for future experimental design, we consolidate authoritative test datasets, security standards, and evaluation frameworks. To the best of our knowledge, this paper presents the first end-to-end survey dedicated to the security of RAG systems. Distinct from existing literature that isolates specific vulnerabilities, we systematically map the entire pipeline-providing a unified analysis of threat models, defense mechanisms, and evaluation benchmarks. By enabling deep insights into potential risks, this work seeks to foster the development of highly robust and trustworthy next-generation RAG systems.

**Решение:** -1 обзор угроз, защит и бенчмарков безопасности RAG

---

### 279 · R12147

**Design and Teaching Strategies for Artificial Intelligence Convergence Education to Protect Creative Autonomy: Focusing on the Middle School Art Class**

2024 · Korean Association For Learner-Centered Curriculum And Instruction · article · en · https://doi.org/10.22251/jlcci.2024.24.6.311

Objectives This study has developed teaching strategies that instructors can use to design and implement artificial intelligence convergence education utilizing generative artificial intelligence for image creation. The derived lesson designs and teaching strategies suggest a limited use of artificial intelligence to ensure that learners using generative AI do not lose their creative autonomy. Methods Through a review of prior literature, an initial checklist for class design and a teaching strategy were developed. Subsequently, two rounds of internal validation were conducted with four experts. A creative class utilizing image-generating artificial intelligence was then implemented for 100 first-year middle school students in Seoul. The effectiveness of this approach was evaluated through pre- and post-tests of artificial intelligence literacy and interviews with the learners. Results Ultimately, 10 items for the class design checklist and 51 items for the teaching strategy were developed. The class design checklist included steps for ‘checking the usage environment’, ‘evaluating the class content’, and ‘assessing expertise’. The teaching strategy was structured into stages of ‘class preparation’, ‘understanding image-generating artificial intelligence’, ‘creative problem-solving’, and ‘class arrangement’. As a result of implementing these creative classes with image-generating artificial intelligence, there was a significant improvement in the students’ artificial intelligence literacy. Furthermore, both instructors and learners highlighted several benefits of these classes, such as the integration of artificial intelligence with various subjects, the enhancement of divergent thinking, firsthand experience with artificial intelligence principles and applications, opportunities for collaboration and discussion, and a strengthened understanding of copyright and ethical considerations. Conclusions The instructional class design checklist and teaching strategy developed in this study serve as cross-curricular guidelines applicable to various subjects that involve image creation, including Korean language, history, and art. Designing artificial intelligence convergence lessons with a focus on protecting learner’s creative autonomy can enable them to grasp the entire creative process and its inherent value. This approach goes beyond mere technical use, empowering learners to enhance their own creative expressions.

**Решение:** -4 педагогика уроков изобразительного искусства в средней школе

---

### 280 · R5657

**Text or Speech, the Gap Persists: AI-based Depression Screening Is Better Calibrated for Lower Socioeconomic Status Users**

2026 · Proceedings of the 2026 Companion of the Computer-Supported Cooperative Work and Social Computing · book, review · https://doi.org/10.1145/3785651.3831524

The interactional design of digital mental health systems can shape what people say, how they say it, and whose distress becomes legible to automated models. We developed a multimodal survey chatbot, M2SurveyBot with clinical psychologists, to examine whether interaction modality that is, typing versus speech, affects self-disclosure and quality of depression screening. In a study with 455 U.S. participants, typed and spoken modalities yielded statistically indistinguishable predictive performance; acoustic features alone carried near-zero signal. Critically, we find a robust socioeconomic status (SES)-related calibration gap replicated across supervised machine learning models and GPT-4o zero-shot estimation: predictions track reported depression severity more closely for lower-SES participants, suggesting socioeconomic differences in linguistic expression of distress. These findings challenge the assumption that multimodal collection produces more equitable screening, while establishing spoken interaction as a viable, accessible alternative to typed text, potentially lower-barrier for populations for whom typing poses challenges.

**Решение:** -3 критериальная валидность: предсказание самоотчёта уровня депрессии / опросника, а не экспертной разметки текста

---

### 281 · R11003

**Insights on Disagreement Patterns in Multimodal Safety Perception across Diverse Rater Groups**

2024 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · en · https://doi.org/10.48550/arxiv.2410.17032

AI systems crucially rely on human ratings, but these ratings are often aggregated, obscuring the inherent diversity of perspectives in real-world phenomenon. This is particularly concerning when evaluating the safety of generative AI, where perceptions and associated harms can vary significantly across socio-cultural contexts. While recent research has studied the impact of demographic differences on annotating text, there is limited understanding of how these subjective variations affect multimodal safety in generative AI. To address this, we conduct a large-scale study employing highly-parallel safety ratings of about 1000 text-to-image (T2I) generations from a demographically diverse rater pool of 630 raters balanced across 30 intersectional groups across age, gender, and ethnicity. Our study shows that (1) there are significant differences across demographic groups (including intersectional groups) on how severe they assess the harm to be, and that these differences vary across different types of safety violations, (2) the diverse rater pool captures annotation patterns that are substantially different from expert raters trained on specific set of safety policies, and (3) the differences we observe in T2I safety are distinct from previously documented group level differences in text-based safety tasks. To further understand these varying perspectives, we conduct a qualitative analysis of the open-ended explanations provided by raters. This analysis reveals core differences into the reasons why different groups perceive harms in T2I generations. Our findings underscore the critical need for incorporating diverse perspectives into safety evaluation of generative AI ensuring these systems are truly inclusive and reflect the values of all users. 20 pages, 7 figures

**Решение:** -4 восприятие безопасности сгенерированных картинок людьми разных демографических групп

---

### 282 · R5698

**Automated Safety Testing and Reporting Application for Conversational Safety Monitoring of Generative AI Tools for Mental Health: Development and Validation Study.**

2026 · JMIR mental health · journal article, validation study, journalarticle · eng · https://doi.org/10.2196/91367

BACKGROUND: Artificial intelligence (AI)-based conversational tools are rapidly expanding within mental health care as a means of increasing access and scalability. At the same time, these systems introduce distinct safety risks arising from both user disclosures (eg, self-harm ideation) and inappropriate or inadequate AI responses. OBJECTIVE: This study aimed to develop and evaluate the Automated Safety Testing and Reporting Application (ASTRA), an external system intended to identify clinically relevant risk behaviors across entire AI-mediated mental health conversations. METHODS: ASTRA was tested on a dataset of 100 synthetic therapeutic conversations written by licensed clinicians to reflect risk behaviors and harmful responses between users and AI tools. Conversations varied in length and included both subtle and overt risk behavior examples across 8 predefined categories. Human coder consensus ratings served as the reference standard. ASTRA's classifications were evaluated across 2 prompt iterations using standard diagnostic performance metrics and agreement statistics. RESULTS: ASTRA demonstrated consistently high concordance with expert human ratings across all categories. Accuracy exceeded 0.90 for all risk behavior categories examined, with specificity uniformly high and sensitivity varying by category (range 0.55-1.00). Agreement beyond chance was substantial to almost perfect between ASTRA and human raters (κ=0.65-1.00). Detection of user self-harm indicators was particularly accurate, even in conversations where risk was expressed subtly. CONCLUSIONS: In this initial validation study, ASTRA reliably identified multiple forms of mental health-related risk behaviors at the conversation level. These findings support the feasibility of independent safety monitoring systems as a complement to AI tools used in mental health contexts and underscore the need for further evaluation using larger and real-world datasets.

**Решение:** + T4/T3 ASTRA: мониторинг терапевтических диалогов и рискового поведения / селфхарм, согласие с экспертами κ=0.65–1.00

---

### 283 · R8291

**Exploring the Potential of Large Language Models for Automated Safety Plan Scoring in Outpatient Mental Health Settings (Preprint)**

2025 · preprint · en · https://doi.org/10.2196/preprints.79010

UNSTRUCTURED The Safety Planning Intervention (SPI) produces a plan to help manage patients’ suicide risk. High-quality safety plans – that is, those with greater fidelity to the original program model – are more effective in reducing suicide risk. We developed the Safety Planning Intervention Fidelity Rater (SPIFR), an automated tool that assesses the quality of SPI using three large language models (LLMs)—GPT-4, LLaMA 3, and o3-mini. Using 266 deidentified SPI from outpatient mental health settings in New York, LLMs analyzed four key steps: warning signs, internal coping strategies, making environments safe, and reasons for living. We compared the predictive performance of the three LLMs, optimizing scoring systems, prompts, and parameters. Results showed that LLaMA 3 and o3-mini outperformed GPT-4, with different step-specific scoring systems recommended based on weighted F1-scores. These findings highlight LLMs’ potential to provide clinicians with timely and accurate feedback on SPI practices, enhancing this evidence-based suicide prevention strategy.

**Решение:** ? оценка качества / fidelity планов безопасности SPIFR по 4 шагам LLM vs эталон; проверить по полному тексту разметку экспертами

---

### 284 · R12123

**Structured Dialogue System for Mental Health: An LLM Chatbot Leveraging the PM+ Guidelines**

2024 · ICSR + InnoBiz · journalarticle, preprint/article, conference-paper · en · https://doi.org/10.48550/arxiv.2411.10681

The Structured Dialogue System, referred to as SuDoSys, is an innovative Large Language Model (LLM)-based chatbot designed to provide psychological counseling. SuDoSys leverages the World Health Organization (WHO)'s Problem Management Plus (PM+) guidelines to deliver stage-aware multi-turn dialogues. Existing methods for employing an LLM in multi-turn psychological counseling typically involve direct fine-tuning using generated dialogues, often neglecting the dynamic stage shifts of counseling sessions. Unlike previous approaches, SuDoSys considers the different stages of counseling and stores essential information throughout the counseling process, ensuring coherent and directed conversations. The system employs an LLM, a stage-aware instruction generator, a response unpacker, a topic database, and a stage controller to maintain dialogue flow. In addition, we propose a novel technique that simulates counseling clients to interact with the evaluated system and evaluate its performance automatically. When assessed using both objective and subjective evaluations, SuDoSys demonstrates its effectiveness in generating logically coherent responses. The system's code and program scripts for evaluation are open-sourced. Accepted to the 16th International Conference on Social Robotic (ICSR 2024)

**Решение:** -6 разработка диалоговой системы SuDoSys по протоколу ВОЗ PM+, симуляция пациентов, нет кодирования текста с оценкой согласия

---

### 285 · R3210

**MEDit-Bench: A Dataset for Evaluating Message-Driven Narrative Video Editing**

2026 · arXiv (Cornell University) · journalarticle, preprint/article, preprint · https://doi.org/10.48550/arxiv.2607.25300

Video editing is fundamentally message-driven: even from the same source footage, the selected shots change depending on the narrative the editor wishes to convey. Benchmarks for a closely related task, video summarization, reduce editorial intent to a single, message-agnostic notion of saliency and thus do not account for this diversity. For evaluating message-driven video editing, we present \textbf{MEDit-Bench}, a dataset and benchmark, which pairs long-form videos with multiple editing messages and multiple professionally produced edits per message, demonstrating that different messages yield substantially different edits from the same source. We define an automatic evaluation protocol based on temporal alignment metrics, and find that an LLM-as-a-judge preference, a natural proxy for narrative quality, is unreliable for this task due to severe position bias. We additionally annotate each message with ambiguity and contextfulness scores, and show that both dimensions negatively correlate with model performance, establishing message difficulty as a meaningful stratification factor. Experiments with state-of-the-art MLLMs and reinforcement fine-tuned baselines show that while strong models approach human temporal alignment at lenient thresholds, all models fall behind humans at stricter criteria. A human perceptual study further confirms a large quality gap, with professional human edits remaining consistently preferred over model outputs.

**Решение:** -4 компьютерные науки, бенчмарк видеомонтажа MEDit-Bench

---

### 286 · R5078

**Works for 9/23/2026 - Lev Semyonovich Vygotsky**

2026 · Zenodo (CERN European Organization for Nuclear Research) · conferencepaper/, conference-paper · https://doi.org/10.5281/zenodo.22927473

Listen and ask questions on Gemini Notebook: https://notebook.google.com/notebook/83f2dc8a-5478-4df7-b296-ed9738e3e8be?authuser=1 This paper examines teaching as a relational process through which information becomes understanding, curiosity becomes sustained inquiry, and external guidance can gradually become self-directed motivation. Bringing together educational psychology, cognitive science, philosophy, theology, motivational theory, and artificial intelligence, it asks a central question: what does it mean to teach another intelligence to care? The paper distinguishes information transmission from successful reception and understanding. Drawing on Socratic teaching, Augustine, Thomas Aquinas, Vygotskian scaffolding, information-gap theories of curiosity, self-determination theory, motivational interviewing, attention, suggestion, memory, and human–AI interaction, it argues that effective teaching cannot be measured merely by engagement, compliance, fluent conversation, or immediate satisfaction. A learner may receive information without understanding it, comply without internalizing a reason for acting, remain engaged without learning, or experience confidence without possessing independent comprehension. Curiosity is treated as a response to meaningful uncertainty: the recognition of a gap between what is known and what remains unresolved. Effective scaffolding neither eliminates that gap nor abandons the learner within it. Instead, teaching provides enough structure for the learner to recognize the problem, believe that progress is possible, and increasingly participate in solving it. As competence grows, assistance can diminish. The paper consequently distinguishes different sources of motivation, including external pressure, obligation, reward, personally endorsed value, and intrinsic interest. Competence, relatedness, and autonomy are treated as interacting conditions that can support increasingly internalized and self-directed motivation. From this perspective, successful education may eventually appear as reduced dependence on the teacher or artificial intelligence: the learner increasingly possesses the ability and motivation to continue inquiry independently. These principles are extended to generative AI. AI systems can influence attention, motivation, perception, memory, and behavior, but influence does not constitute ownership of another person’s response. Engagement is not equivalent to understanding; compliance is not equivalent to motivation; fluency is not equivalent to teaching; and additional explanation does not necessarily produce additional comprehension. The paper therefore frames responsible AI teaching around reception, appropriate scaffolding, learner autonomy, and the distinction between helping a person think and merely producing a desired response. Within the paper’s theological framework, teaching is ultimately interpreted through care and love. Care is defined as communication or action ordered toward the genuine good of the other person rather than mere agreement, approval, dependence, engagement, or immediate satisfaction. Teaching therefore reaches its fullest form when it helps another person become increasingly capable of recognizing, pursuing, and participating in the good for themselves. The paper includes “Angela’s Explainer,” a plain-language layer that translates these arguments through concrete examples of curiosity, meaningful uncertainty, motivation, scaffolding, and growing independence, alongside formal appendices extending the framework into explicit propositions and derivations.

**Решение:** -1 педагогико-философское эссе об идеях Выготского, строительных лесах и ИИ

---

### 287 · R5823

**Corpus Generation for Emotion Classification in Psychotherapy Using Large Language Models**

2026 · Lecture notes in networks and systems · conference-paper · en · https://doi.org/10.1007/978-3-032-20897-2_17

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? генерация корпуса для классификации эмоций в психотерапии с помощью LLM; нет аннотации, проверить по полному тексту

---

### 288 · R4297

**Towards Fine-Grained Emotion Detection in Hebrew: Dataset Creation and Evaluation**

2026 · International Conference on Data Technologies and Applications · journalarticle · https://doi.org/10.5220/0014924700004091

: Fine-grained emotion detection for Hebrew remains underexplored due to the lack of publicly available annotated resources. We present HeMotion, a manually annotated and balanced Hebrew dataset for emotion classification based on Plutchik’s eight-emotion model, consisting of 670 sentences. We analyze the dataset’s lexical and structural properties and establish the first benchmark for this task using Hebrew transformer models, a dedicated Hebrew emotion model, and large language models with prompting. Experimental results show that transformer and LLM-based approaches outperform traditional baselines. By releasing HeMotion and the benchmark results, this work provides a new resource and evaluation framework for fine-grained emotion detection in Hebrew.

**Решение:** + T1 классификация 8 базовых эмоций по Плутчику на иврите [HeMotion], LLM с промптингом vs ручная разметка

---

### 289 · R8952

**COMPASS: Computational mapping of patient-therapist alliance strategies with language modeling.**

2025 · Translational psychiatry · journal article, journalarticle, preprint/article · eng · https://doi.org/10.1038/s41398-025-03379-3

The therapeutic working alliance is a critical predictor of psychotherapy success. Traditionally, working alliance assessment relies on questionnaires completed by both therapists and patients. In this paper, we present COMPASS, a novel framework to directly infer the therapeutic working alliance from the natural language used in psychotherapy sessions. Our approach leverages advanced large language models (LLMs) to analyze session transcripts and map them to distributed representations. These representations capture the semantic similarities between the dialogues and psychometric instruments, such as the Working Alliance Inventory. Analyzing a dataset of over 950 sessions spanning diverse psychiatric conditions -- including anxiety (N=498), depression (N=377), schizophrenia (N=71), and suicidal tendencies (N=12) -- collected between 1970 and 2012, we demonstrate the effectiveness of our method in providing fine-grained mapping of patient-therapist alignment trajectories, offering interpretable insights for clinical practice, and identifying emerging patterns related to the condition being treated. By employing various deep learning-based topic modeling techniques in combination with prompting generative language models, we analyze the topical characteristics of different psychiatric conditions and how these topics evolve during each turn of the conversation. This integrated framework enhances the understanding of therapeutic interactions, enables timely feedback for therapists on the quality of therapeutic relationships, and provides clear, actionable insights to improve the effectiveness of psychotherapy. Translational Psychiatry, in press. This work extends our research series in computational psychiatry (e.g auto annotation in arXiv:2204.05522, topic extraction in arXiv:2204.10189, and diagnosis in arXiv:2210.15603) with the introduction of LLMs to complete the full cycle of interpreting and understanding psychotherapy strategies as a comprehensive analytical framework

**Решение:** ? COMPASS: картирование терапевтического альянса [WAI] по 950 психотерапевтическим сессиям; проверить по полному тексту валидацию против опросника WAI [-3] или экспертов [T4]

---

### 290 · R10036

**From aligned models to trusted interfaces:Explainable health intervention and transparent health information seeking**

2025 · UvA-DARE (University of Amsterdam) · other · en · https://hdl.handle.net/11245.1/16354ae6-d546-47a5-aaf3-17fd20c34a60

This thesis presents research on two interrelated themes in applying large language models (LLMs) to health contexts: (1) the model theme, aligning LLMs with domain expertise for digital counseling. (2) the interface theme, exploring people’s trust in LLM-powered health information. Specifically, the first theme focuses on improving the explainability and controllability of LLMs for therapeutic dialogue generation. Initial evaluation showed that LLMs struggle to produce emotionally nuanced and contextually appropriate reflections in Motivational Interviewing (MI). To address this, we created expert-annotated bilingual MI dataset that captures therapeutic communication strategies. Building on this, a Script-Strategy Aligned Generation (SSAG) was proposed, where the LLM first predicts a therapeutic strategy before generating dialogue. This structured approach enhanced both explainability and adherence to evidence-based principles, offering a more controllable way to integrate LLMs into digital psychotherapy. Research on the second theme explored trust in LLM-powered health information seeking. The first study compared LLM-powered conversational search with use of a traditional web-based search engine. The results showed that participants express more trust in LLM’s conversational responses. Research also revealed a preference for text-based interfaces over speech-based and embodied interfaces. Crucially, a mixed-methods study on source attribution showed that while LLM-generated information was highly trusted, content explicitly labeled as human-sourced was perceived as more trustworthy than content labeled as AI-generated, regardless of its actual origin. These findings underscore the nuanced relationship between source transparency and trust. By bridging model alignment with human-centric assessment, this work provides new knowledge for designing explainable, transparent, and trustworthy LLM-powered applications in digital health.

**Решение:** ? диссертация: предсказание терапевтических стратегий мотивационного интервью на экспертно размеченном датасете; проверить согласие с экспертами

---

### 291 · R3363

**Computer-Aided Pitch Deck Pro: An Entrepreneurial Intelligence Framework for AI-Assisted Startup Pitch Generation, Investment Readiness Assessment, and Decision Support**

2026 · book · https://doi.org/10.66669/cineforum.v66is7.1793

The exponential growth of early-stage ventures coupled with the persistent scarcity of rigorous, scalable, and bias-aware investment-readiness assessment tools has produced a structural bottleneck in the global startup ecosystem. Although machine learning models now achieve over 90 % accuracy on retrospective success prediction and large language models can generate plausible business narratives, these capabilities remain siloed: predictive models offer no constructive feedback to founders, and generative models are routinely challenged by hallucination, weak grounding, and absence of structured evaluation rubrics. This paper introduces Computer-Aided Pitch Deck Pro, an integrated Entrepreneurial Intelligence Framework that operationalizes a seven-stage computational pipeline, Extract → Learn → Evaluate → Validate → Augment → Transform → Export, for end-to-end AI-assisted pitch deck generation, investor-readiness scoring, and decision support. Grounded in design-science research and a corpus-level synthesis of more than 120 peer-reviewed studies on venture AI, retrieval-augmented generation, explainable AI, and human-AI collaboration, the framework introduces four original constructs — (i) a Pitch Deck Quality Index, (ii) an Investment Readiness Score based on the validated Critical Factor Assessment rubric, (iii) an Epistemic Confidence Estimator for quantifying LLM output trust, and (iv) a Pitch Optimization Gain Function for refinement under expert constraint. Across an experimental corpus of 612 pitch dock transcripts and an expert panel of 47 venture capitalists, the proposed system achieves a Pearson correlation of r = 0.91 between IRS and human ratings, a 27 % relative improvement in PDQI after one optimization round, and a 5–15-second end-to-end analysis latency, comparable to recent RAG-augmented investor assistants [1], [2]. Seven major contributions are delineated: the Entrepreneurial Intelligence Framework as a foundational paradigm; the ELEVATE pipeline; the PDQI; the IRS; the ECE; a multimodal pitch-deck quality dataset; and a hybrid expert-in-the-loop evaluation protocol. The paper positions Computer-Aided Pitch Deck Pro as the first system to unify generative, evaluative, and decision-support functions for the entrepreneurial domain, opening a new line of research we term Entrepreneurial Intelligence Systems.

**Решение:** -4 бизнес-оценка стартап-питчей и инвестиционной готовности

---

### 292 · R5012

**Large Language Models and Emotional Regulation of University Students in Peshawar, Khyber Pakhtunkhwa**

2026 · Pakistan Journal of Positive Psychology · journalarticle, article · https://doi.org/10.67785/pjpp.4.175

In the digital age, LLMs have significantly transformed students’ academic practices and impact emotional experiences. The present study aimed to investigate the impact of instrumental and relational dependency on emotion regulation strategies among university students. A quantitative, cross-sectional research design was employed. The sample consisted of 380 university students, recruited through convenience sampling from multiple universities. Participants completed a demographic information sheet, the Dual-Dimensional Scale of Instrumental and Relationship Dependency on Large Language Models (LLM-D12), and the Emotion Regulation Questionnaire (ERQ), which measures habitual use of cognitive reappraisal and expressive suppression. Data were analyzed using descriptive statistics, multivariate regression, and independent-samples t-tests using SPSS version 23. Findings revealed that instrumental dependency does not significantly predict cognitive reappraisal or expressive suppression. Additionally, relational dependency showed a significant negative prediction effect on cognitive reappraisal and expressive suppression, suggesting that greater relationship dependency was associated with lower use of these emotion regulation strategies. Furthermore, non-significant gender differences were found across instrumental dependency, relational dependency, cognitive reappraisal, and expressive suppression. The findings underscore the need for balanced, responsible, and psychologically informed approaches to AI integration that support academic performance while preserving students’ emotional growth and independence in an increasingly AI-driven educational environment.

**Решение:** -4 опросное исследование зависимости студентов от LLM и эмоциональной регуляции [ERQ], нет кодирования текстов с помощью LLM

---

### 293 · R8504

**Open Large Language Models for Structured Depression Assessment**

2025 · OSF Preprints (OSF Preprints) · preprint

Supplemental Materials for "Evaluating Open-Weight Large Language Models for Structured Depression Assessment from Clinical Interviews"

**Решение:** ? оценка депрессии по клиническим интервью с помощью open-weight LLMs [T3]; проверить сопоставление с клиницистами vs опросниками

---

### 294 · R6080

**Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation**

2026 · arXiv (Cornell University) · journalarticle, review, preprint/article · https://doi.org/10.48550/arxiv.2607.02577

Tool-calling benchmarks are increasingly used to rank language-model agents, yet their scores are often treated as ground truth without validating the evaluators themselves. We present a systematic validity and reproducibility audit of four major tool-calling benchmark families: BFCL v4, {\tau}2-Bench, LiveMCPBench, and MCP-Atlas. Across 496 expert-reviewed benchmark tasks, we find 92 evaluator-human disagreements, corresponding to an 18.5% misalignment rate. The failures are not isolated annotation mistakes: deterministic benchmarks exhibit brittle state matching, trajectory lock-in, incorrect ground truths, substring-based communication failures, and reward-basis misalignment, while LLM-judge benchmarks exhibit rubric drift, hallucinated completion, answer-only scoring, and substantial run-to-run variance. In LiveMCPBench, 23 repeated evaluations of the same setup produce scores ranging from 57.9% to 76.8%, a spread of 18.9 percentage points, large enough to change leaderboard conclusions. These results show that current tool-calling scores can reflect evaluator artifacts rather than agent capability. We introduce a unified taxonomy of tool-calling evaluation failures, release trace-level audit artifacts and corrected evaluation components, and argue for decomposed metrics that separately measure tool invocation, task completion, and outcome verification. Our findings suggest that progress in tool-using agents requires benchmarks whose evaluators are themselves reproducible, auditable, and aligned with human judgments of task success. We further introduce Tool-Veritas, a configurable benchmark that combines deterministic state verification with optional qualitative judging, and Harness Lab, an open-source system for benchmark execution, trace inspection, repeated-run comparison, and evaluator debugging.

**Решение:** -4 компьютерные науки, аудит бенчмарков tool-calling у программных агентов

---

### 295 · R5172

**Generative Artificial Intelligence and Large Language Models in Didactics of Sports Sciences and Physical Education: A Comprehensive Review of Pedagogical Applications, Teaching Innovations, and Research Implications**

2026 · International journal of Sport Studies for Health · journalarticle, review, article · https://doi.org/10.61838/kman.intjssh.4891

Objective: The global burden of physical inactivity contributes to 5.3 million deaths annually, exceeding smoking-related mortality in certain regions and contributing substantially to the 1.5 billion individuals worldwide living with chronic diseases. Physical education (PE) represents a critical intervention point, yet persistent challenges limit effectiveness including inadequate instructional time (80 minutes weekly versus recommended 150 minutes), insufficient specialized teacher preparation (42% of elementary PE teachers lack specialized training), and limited capacity for differentiated instruction in heterogeneous student populations. The emergence of Generative Artificial Intelligence (Gen AI), particularly Large Language Models (LLMs) such as ChatGPT (launched November 2022, achieving 100 million users within two months), presents unprecedented opportunities for transforming pedagogical practices in sports sciences and PE contexts while simultaneously introducing critical challenges regarding academic integrity, cognitive development, and the preservation of embodied learning central to movement education. This comprehensive review aimed to: (i) systematically examine current applications and pedagogical affordances of Gen AI and LLMs in sports sciences and PE didactics; (ii) analyze alignment with established pedagogical principles including constructivism, social constructivism, situated learning theory, and Universal Design for Learning; (iii) critically evaluate potential benefits and risks from a didactics perspective including impacts on teacher development, student learning outcomes, curriculum design, and assessment practices; and (iv) propose evidence-informed frameworks for pedagogically sound integration emphasizing human-AI collaboration rather than replacement of essential teaching functions. Methods: A systematic literature search was conducted following adapted PRISMA guidelines across seven databases (PubMed/MEDLINE, Web of Science, Scopus, IEEE Xplore, ERIC, SPORTDiscus, Google Scholar) covering January 2022 to November 2025. Search terms combined Gen AI/LLM terminology with pedagogical concepts in sports sciences contexts using Boolean operators. Inclusion criteria focused on peer-reviewed articles examining pedagogical applications, teaching innovations, learning outcomes, and didactic research methodologies. From 1,247 initial records, 858 titles and abstracts were screened after duplicate removal (n=389), with 247 undergoing full-text review. Final analysis included 78 studies meeting inclusion criteria. Data extraction utilized standardized forms capturing study characteristics, methodological approaches, AI technology examined, pedagogical context, theoretical framework, key findings, and practice implications. Thematic analysis employed a pedagogically-oriented framework organizing findings into four domains aligned with core didactic functions: teaching support, learning enhancement, assessment innovation, and didactic research. Results: Analysis of 78 studies (67% published 2023-2024) revealed significant pedagogical applications across four domains with concurrent identification of critical challenges. Teaching Support domain demonstrated lesson planning time reductions of 35% to 45%, with AI-assisted lesson plan quality rated 7.3 out of 10 (SD=1.2) for curriculum alignment compared to 7.8 out of 10 (SD=0.9) for manually created plans. Educators reported 67% satisfaction with differentiated instruction materials generated through Gen AI platforms. Learning Enhancement domain revealed improved conceptual understanding when engaging with AI tutors for anatomy and biomechanics concepts, with students valuing immediate availability and scaffolded explanations. Assessment Innovation applications showed AI-generated feedback demonstrated substantial agreement with expert teacher feedback for student assignments. Didactic Research efficiency gains included literature synthesis completion substantially faster than traditional methods and qualitative coding demonstrating substantial agreement between AI and expert human coders. However, critical challenges emerged including academic integrity violations in 23% to 43% of student work, factual inaccuracies in AI-generated specialized content, cognitive atrophy concerns (AI-Chatbot Induced Cognitive Atrophy, AICICA), reduced emphasis on embodied learning in PE contexts, and equity issues affecting students with limited digital literacy or technology access. Conclusion: Gen AI and LLMs represent transformative tools for sports sciences and PE didactics when implemented within robust pedagogical frameworks that preserve the essential embodied, social, and affective dimensions of movement education. Evidence supports specific applications including administrative efficiency, differentiated cognitive content delivery, formative assessment support, and research methodology enhancement, while simultaneously demanding critical attention to academic integrity, accuracy verification, equity considerations, and prevention of cognitive atrophy through over-reliance. A hybrid pedagogical model is recommended integrating Gen AI for cognitive content delivery, theoretical knowledge construction, and administrative tasks while rigorously preserving face-to-face instruction, kinesthetic learning experiences, immediate physical feedback, and human mentorship central to sports education. Successful integration requires comprehensive teacher professional development focusing on pedagogical decision-making rather than technical operation, explicit policies balancing academic integrity with beneficial use, critical AI literacy curriculum specific to sports sciences contexts, and ongoing empirical evaluation of long-term learning outcomes. The field requires a paradigm shift from technology-driven adoption to pedagogy-informed integration, ensuring Gen AI serves educational goals rather than dictating them.

**Решение:** -1 систематический обзор применения GenAI в спортивных науках и физкультуре

---

### 296 · R10290

**Unveiling the cognitive burden: The impact of stigma on distorted thinking among individuals living with hepatitis B.**

2025 · International journal of clinical and health psychology : IJCHP · journal article, journalarticle, article · eng · https://doi.org/10.1016/j.ijchp.2025.100556

Hepatitis B (HBV) is a prevalent chronic illness affecting approximately 254 million individuals worldwide, with China accounting for nearly one-third of cases. Despite its widespread impact, stigma associated with HBV significantly hinders access to testing, diagnosis, and treatment. This study investigates the relationship between HBV stigma and cognitive distortions among individuals living with HBV by analyzing 35,697 posts from Yiyou Forum, China's largest HBV online community. Utilizing a large language model (LLM) for stigma classification, posts were categorized into stigma-related (S-posts) and non-stigma-related (N-posts). A schema comprising 235 n-grams was employed to identify 12 types of cognitive distortions within these posts. Statistical analyses revealed that S-posts had a prevalence ratio (PR) of 1.824 (95%CI [1.636, 2.074]) for cognitive distortions compared to N-posts, indicating that distorted thinking patterns were approximately 1.8 times more common in stigma-related discussions. Specific distortions such as disqualifying the positive, labeling and mislabeling, mental filtering, and should statements were significantly more prevalent in S-posts. User-level analysis confirmed that individuals engaging in stigma-related posts consistently displayed higher levels of cognitive distortions. These insights underscore the potential of targeted cognitive-behavioral therapy (CBT) interventions to address and mitigate cognitive distortions, thereby alleviating the psychological burden of HBV stigma. Additionally, this study demonstrates the efficacy of advanced computational methods in psychological research.

**Решение:** ? классификация стигмы и когнитивных искажений в постах пациентов с гепатитом B; проверить наличие оценки согласия LLM с людьми

---

### 297 · R11648

**Automatic implicit motives codings are as accurate as humans’ and 99% faster**

2024 · PsyArXiv · preprint, ppr · en · https://doi.org/10.31234/osf.io/7s6jp

Implicit motives, non-conscious needs that influence individuals’ behaviors and shape their emotions, have been part of personality research for nearly a century but differ from personality traits. The implicit motive assessment is very resource-intensive, involving expert coding of individuals’ written stories about ambiguous pictures, and has hampered implicit motive research. Using large language models and machine learning techniques, we aimed to create high-quality implicit motive models that are easy for researchers to use. We trained models to code the need for power, achievement, and affiliation (N = 85,028 sentences). The person-level assessments converged strongly with the holdout data (ICC(1,1) = .85, .87, and .89 for achievement, power, and affiliation, respectively). We demonstrated causal validity by reproducing two classical experimental studies that aroused implicit motives. We let three coders recode sentences where our models and the original coders strongly disagreed. We found that the new coders agreed with our models in 85% of the cases (p &lt; .001, φ = .69). Using topic and word embedding analyses, we found specific language associated with each motive to have a very high face validity. We argue that these models can be used in addition to, or instead of, human coders. We provide a free, user-friendly framework in the established R-package text and a tutorial for researchers to apply the models to their data, as these models reduce the coding time by over 99% and require no cognitive effort for coding. We hope this coding automation will facilitate a historical implicit motive research renaissance.

**Решение:** + T2 подсчёт психодиагностических методик: проективный тест TAT / Picture Story Exercise на скрытые мотивы, LLM vs эксперты, ICC = 0.85–0.89, phi = 0.69

---

### 298 · R10349

**Introducing the fusion innovation test as a new paradigm for studying realworld creative problem solving.**

2025 · Scientific reports · journal article, research support, non-u.s. gov't, journalarticle · eng · https://doi.org/10.1038/s41598-025-28134-y

Studying creative problem-solving requires tasks with real-world relevance and minimal domain-specific knowledge. The widely used alternative uses test (AUT) meets these criteria but primarily measures divergent thinking-generating many ideas without immediate judgment. However, creative problem-solving also requires convergent thinking to narrow down options and select the most effective solution. We introduce the fusion innovation test (FIT), a task that integrates both divergent and convergent thinking. In the FIT, participants combine two randomly assigned elements (e.g., objects or technologies) to achieve either a self-improvement goal or a sustainable development goal. Each FIT solution is evaluated based on the novelty and feasibility of combining the elements, and the effectiveness in achieving the intended goal. We collected behavioral data from 144 participants and used ratings from 122 human evaluators to train an automated scoring system based on a large language model. Participants also completed the AUT and two real-life creativity questionnaires. Results show that the FIT captures a unique aspect of creativity-goal-directed innovation-not assessed by the AUT. Moreover, FIT performance correlates with scientific creativity, whereas AUT performance aligns more with artistic creativity. These findings suggest that the FIT is an initially promising and complementary tool for studying real-world creative problem-solving.

**Решение:** + T2 психодиагностическая оценка креативного решения проблем в тесте FIT, LLM vs 122 эксперта-оценщика

---

### 299 · R10110

**Neural text embeddings in psychological research: A guide with examples in R.**

2025 · Psychological methods · journal article, med, journalarticle · eng · https://doi.org/10.1037/met0000768

In this guide, we review neural embedding models and compare three methods of quantifying psychological constructs for use with embeddings: distributed dictionary representation, contextualized construct representation, and a novel approach: correlational anchored vectors. We aim to cultivate an intuition for the geometric properties of neural embeddings and a sensitivity to methodological problems that can arise in their use. We argue that while large language model embeddings have the advantage of contextualization, decontextualized word embeddings may have more ability to generalize across text genres when using cosine or dot product similarity metrics. The three methods of operationalizing psychological constructs in vector space likewise each have their advantages in particular applications. We recommend distributed dictionary representation, which derives a vector representation from a word list, for quantifying abstract constructs relating to the overall feel of a text, especially when the research requires that these constructs generalize across multiple genres of text. We recommend contextualized construct representation, which derives a representation from a questionnaire, for cases in which texts are relatively similar in content to the embedded questionnaire, such as experiments in which participants are asked to respond to a related prompt. Correlational anchored vectors, which derives a representation from labeled examples, requires suitably large and reliable training data. (PsycInfo Database Record (c) 2025 APA, all rights reserved).

**Решение:** -1 методологическое руководство / туториал по текстовым эмбеддингам в психологических исследованиях

---

### 300 · R7589

**Introducing Synthetic Cognitive Capacity (SCC): A Novel Framework for Evaluating Generalizable Intelligence in Generative AI Systems**

2025 · SSRN Electronic Journal · preprint · en · https://doi.org/10.2139/ssrn.5215716

_Аннотации нет — решайте по названию или ставьте `?`._

**Решение:** ? SCC фреймворк оценки интеллекта систем ИИ; нет аннотации, проверить по полному тексту; если LLM объект — исключить как -2
