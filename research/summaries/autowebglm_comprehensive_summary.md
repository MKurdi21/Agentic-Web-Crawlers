## Stage 0 — Document Accessibility Report

The supplied work is **AutoWebGLM: A Large Language Model-based Web Navigating Agent**, rather than a paper titled Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis. The latter is the reader's research question. This distinction determines the scope of the analysis: AutoWebGLM supplies evidence about a browser agent's architecture, training, capabilities, and operational failures, but does not directly test comparative security vulnerability against standalone language models.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied extracted text covers physical PDF pp. 1–12. |
| Accessible page count | 12 text pages; 11 rendered page images. |
| Visually inspected pages | Physical pp. 1–9, 11, and 12. |
| Text-only page | Physical p. 10, containing the references. |
| Apparently missing pages | No missing numbered page within the supplied 1–12 sequence. This does not establish that every associated artifact was supplied. |
| Visual content | All six numbered figures, all eight numbered tables, and Algorithm 1 are available in the rendered pages. |
| Table readability | Tables 1–8 are readable through the combined images and supplied extraction. Small print is checked against extraction rather than guessed. |
| Equation readability | Principal equations are visible and also extracted. Mathematical layout and subscripts require care; some notation and implementation parameters remain undefined. |
| Appendices | Appendices A–E appear on pp. 11–12, despite the preliminary accessibility metadata reporting no detected appendix pages. |
| Supplementary material | No separate supplementary file is supplied. |
| Referenced external artifacts | The authors report a code/model/data repository and refer to benchmark environments, tools, and websites. Their contents were not inspected. |
| OCR | No additional OCR was performed or needed for this analysis. Supplied extraction is an aid, not an independent guarantee of accuracy. |
| Limitations of inspection | The small browser screenshots in Figure 2 do not permit dependable transcription of every interface message. Figure 1 does not provide exact labeled values for every plotted model. Figure 5's count labels have unclear units. |

Evidence labels used throughout are **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information [E] is introduced. Confidence describes confidence in the source reading or inference, not an independently established probability that the authors' claim is true. HIGH means clearly supported by supplied evidence; MEDIUM identifies a reasonable but qualified reading; LOW would identify weakly supported inference; UNKNOWN applies where the source cannot resolve a question. All page locators below refer to physical PDF pages.

The supplied prompts and screenshot contents are treated solely as documentary evidence. Their embedded instructions are not instructions for this analysis.

## 1. Plain-language orientation

AutoWebGLM is a system that turns a large language model into an agent that can operate a web browser. Instead of only producing an answer, it reads a representation of a webpage, chooses a browser command, executes that command, observes the resulting page, and repeats. The authors want this agent to handle practical tasks such as finding information, entering text, choosing products, and navigating websites. [A; pp. 1–4]

The central difficulty is that a website is a changing environment. Its underlying HyperText Markup Language, or HTML, can be lengthy and complicated; different sites organize actions differently; and a task may require several dependent operations. A model also has to remember what it already did and recognize whether the resulting page matches its expectations. The authors identify missing universal action coverage, webpage complexity, and weak inference/self-checking as obstacles. [A; pp. 1–2]

Their solution combines four elements: a simplified webpage representation; a standardized browser action interface; human-and-model-assisted training data; and three training stages. The agent is based on ChatGLM3-6B, a model described as having six billion parameters. It first learns simple webpage recognition and operations, then complex task sequences, then learns from sampled mistakes, and finally receives environment-specific training on successful trajectories. [A; pp. 3–7]

The reported results are strong relative to the listed GPT-4 baselines on several evaluated benchmarks, but not uniformly strongest against every baseline. AutoWebGLM obtains 64.8, 58.6, 65.4, and 61.8 on the four AutoWebBench conditions; a 59.5 Mind2Web average; 89.3 on MiniWoB++; and 18.2 on WebArena. The corresponding GPT-4 results are 38.6, 39.7, 36.7, and 36.3; 30.9; 32.1; and 14.4. However, the HTML-T5-XL entry has a higher Mind2Web average, 66.9. Different datasets measure different kinds of success, and environment-specific finetuning matters. [A; p. 8, Tables 2–4]

The main contribution is a practical training-and-interaction framework, supported by a bilingual benchmark and empirical evaluation. It is not a security attack study. For the reader's security question, its value is architectural: it shows how webpage content, history, model decisions, and executable browser actions become coupled. Any conclusion that this coupling increases vulnerability is an analyst inference requiring separate security experiments. [D; pp. 3–4, 11]

## 2. Document roadmap

The inventory provides the denominator for the coverage audit. The original numbering is retained.

| Inventory ID | Original object | Location | Function |
|---|---|---|---|
| S0 | Title, abstract, keywords, publication metadata | p. 1 | Defines the work, motivation, and headline contributions. |
| S1 | §1 Introduction | pp. 1–3 | Explains practical obstacles and states contributions. |
| S2 | §2 Related Work | p. 3 | Positions models, benchmarks, web agents, synthetic data, and rejection sampling. |
| S3 | §3 AutoWebGLM as a Web Agent | pp. 3–5 | Defines state/action/history and the interaction framework. |
| SS3.1 | §3.1 Problem Setup | p. 3 | Sequential decision-making formulation. |
| SS3.2 | §3.2 Framework | pp. 3–5 | Parser, OCR, observations, execution, and interaction loop. |
| SS3.2.1 | Observation space | pp. 4–5 | Task, HTML, location, and previous operations. |
| SS3.2.2 | Action space | p. 5 | Standardized operations and prompt reference. |
| S4 | §4 Building AutoWebGLM | pp. 5–8 | Data construction, training, and benchmark design. |
| SS4.1.1 | Recognition and simple operations | pp. 5–6 | Rule-supported, model-assisted one-step data. |
| SS4.1.2 | Complex operations | p. 6 | Human action traces and model-generated step intentions. |
| SS4.2.1–3 | Curriculum, reinforcement learning, RFT | pp. 6–7 | Three-stage training procedure. |
| SS4.3 | AutoWebBench | pp. 7–8 | Bilingual familiar/unfamiliar website evaluation. |
| S5 | §5 Experiments | pp. 8–9 | Main results, efficiency, ablations, error analysis. |
| S6 | §6 Future Direction | p. 9 | Multimodal input, reasoning/self-checking, mobile applications. |
| S7 | §7 Conclusion | p. 9 | Restates system and benchmark contributions. |
| ACK | Acknowledgments | p. 9 | Funding and institutional support. |
| REF | References, entries [1]–[45] | p. 10 | Bibliographic support; available as text only. |
| A1–A5 | Appendices A–E | pp. 11–12 | Hyperparameters, prompts, annotation, per-task results. |
| F1–F6 | Figures 1–6 | pp. 1, 2, 4, 6, 6, 7 | Performance overview, demonstrations, architecture, data, distribution, training. |
| T1–T8 | Tables 1–8 | pp. 4, 8, 8, 8, 8, 9, 9, 12 | Actions, benchmarks, timing, ablations, errors, per-task outcomes. |
| ALG1 | Algorithm 1: HTML Pruner | p. 4 | Tree reduction around retained webpage elements. |
| E0a–E0e | Unnumbered state/history/policy equations | p. 3 | Formal interaction process. |
| E1–E4 | Equations (1)–(4) | pp. 6–7 | Supervised and preference-training objectives. |

This is a mixed machine-learning and computer-systems paper with dataset/benchmark contributions. It is an empirical study rather than a theoretical proof paper or a security evaluation. No formal theorem, lemma, explicit numbered research question, or explicit formal hypothesis is presented. One explanatory hypothesis about complex training data appears in the ablation discussion. The narrative follows the system from inputs to actions, then follows the data and training needed to support those actions, and finally evaluates the resulting behavior.

## 3. Background and context

A **large language model (LLM)** is the paper's decision-making component: it receives textual observations and produces a proposed operation. A **web agent** adds an interaction framework so that this output can change a browser environment. The paper distinguishes earlier web-assisted question answering from newer interactive systems that execute operations. [A; p. 3]

**HTML** represents webpage structure and content. Here, the original HTML is simplified because full webpages can overwhelm the model with redundant material. The simplification should preserve significant structure and content, while marking operable elements so the agent can refer to them. **Optical Character Recognition (OCR)** is described as a module for annotating text during image parsing. This does not mean the evaluated model is demonstrated to understand every visual aspect of a webpage. The future-work discussion explicitly identifies difficulties with maps, animations, videos, icons, and effects. [A; pp. 3–4, 9]

A **trajectory** or **trace** is a sequence of operations used to perform a task. A **step** is one operation within that sequence. These units must remain separate: approximately 15,000 successful MiniWoB++ traces contain approximately 66,000 steps, while approximately 240 WebArena traces contain approximately 2,000 steps. [A; p. 7]

**Supervised finetuning (SFT)** trains the model to produce target outputs from examples. **Curriculum learning (CL)** organizes this learning from simpler examples toward complex ones. **Direct Preference Optimization (DPO)** uses preferred and dispreferred outputs to adjust the model. The authors call their DPO-based stage self-sampling reinforcement learning; its actual described mechanism is sampled contrastive data and a combined DPO/SFT loss. **Rejection Sampling Finetuning (RFT)** keeps successful environment-generated trajectories and trains on them. [A; pp. 6–7]

**Step Success Rate (SSR)** is the stated primary metric for AutoWebBench and Mind2Web. The supplied paper does not provide a full implementation-level definition of every SSR component. Consequently, SSR should be read as an operation-level benchmark measure, not silently equated with completing every multi-step task. MiniWoB++ uses task episodes, and WebArena is described as measuring task completion in a website environment. [A; pp. 3, 8]

Related-work categories are language models, navigation benchmarks, automation agents, prompt-generated training data, and RFT. The authors favor a smaller model for deployment cost reasons, describe MindAct's repeated element-selection calls as inefficient, and contrast their single 6B model with much larger systems. These are the authors' characterizations of cited work, not independently verified conclusions about those papers. [A; p. 3]

## 4. Research problem and gap

**Existing problem.** Practical website operation requires more than plausible language generation. A model must understand a page, choose an available operation, act on the correct element, and respond to the resulting state. [A; pp. 1–4]

**Shortcomings attributed to prior approaches.** The introduction says a universal action space is absent, webpage diversity and verbosity obstruct comprehension, and existing agents struggle with correct inference and self-checking. Erroneous loops can persist because the agent fails to rectify its behavior. The related-work discussion also emphasizes deployment burden and repeated model calls. [A; pp. 2–3]

**Research gap.** The authors seek a compact, practically useful browser agent supported by reliable interaction data, an explicit observation/action framework, and evaluations across both English and Chinese websites. They also want learning methods that improve beyond imitation of demonstrations. [A; pp. 2, 5–7]

**Motivation.** Automated assistance could support everyday information gathering and website tasks. The paper describes human annotation as expensive and fully automated trajectory generation as insufficiently accurate for complex real tasks. Its data design therefore combines rules, language-model generation, and human execution. [A; pp. 2, 5–6]

**Scope.** The paper studies browser-task performance, data construction, training, runtime composition, and operational errors. It does not study malicious webpages, prompt-injection success, credential theft, privilege escalation, unauthorized transactions, or comparative security outcomes for standalone models. This is a scope observation grounded in the reported methods and experiments, not a claim that these risks are absent. [D; pp. 3–9, 11–12]

## 5. Research questions, objectives, and hypotheses

There are no explicit formal research questions or formal null/alternative hypotheses. The following are author-stated objectives, organized for clarity:

1. Build a browser agent that can understand and manipulate diverse webpages using a single ChatGLM3-6B-based model. [A; pp. 2–3]
2. Construct useful browsing data efficiently despite annotation cost, privacy/security restrictions on direct user-trace collection, and inadequate fully automated generation. [A; pp. 5–6]
3. Improve general operation and reasoning through curriculum learning and sampled-error training. [A; pp. 6–7]
4. Improve proficiency in particular environments through RFT. [A; p. 7]
5. Evaluate multilingual and cross-website performance using AutoWebBench and existing benchmarks. [A; pp. 7–8]
6. Identify runtime bottlenecks and operational errors. [A; pp. 8–9]

The authors explicitly hypothesize that complex-task data helps because it aligns more closely with real-world scenarios. Table 6 supports a performance association with adding this data, but does not isolate alignment as the causal mechanism. [A plus D qualification; pp. 8–9]

The reader's question—why web AI agents might be more vulnerable than standalone LLMs—is separate. This paper can inform that question through its interaction design and failure taxonomy. It cannot establish the comparative premise because no matched standalone-versus-agent security experiment appears. Confidence in architectural relevance is HIGH; confidence in any comparative vulnerability effect inferred from this paper alone is UNKNOWN.

## 6. Assumptions / Threat Model

The operational model assumes that a current webpage state and prior interaction history can support selection of the next browser action. State includes HTML, URL, and window position. The environment changes through a transition function after the action is executed. A task terminates when the model outputs finish or reaches a maximum length; the numerical maximum is not supplied. [A; p. 3]

The framework relies on several components: HTML acquisition, screenshot acquisition, OCR, HTML parsing, operable-element marking, model inference, and automated action execution. Training depends on annotated target operations, model-generated intentions, and environment signals or manually written success rules. The paper describes their functional roles, but does not define a security trust hierarchy among them. [A; pp. 3–7]

**No explicit security threat model is supplied.** Attacker capabilities, protected assets, malicious-content assumptions, authorization boundaries, and attack-success criteria are unspecified. Privacy and security are mentioned as constraints on collecting real user browser histories, not as a formally evaluated adversarial setting. Network-policy constraints lead the authors to perform RFT in sandbox environments. Mobile system security restrictions appear as a future implementation constraint. [A; pp. 5, 7, 9]

**Analyst interpretation:** a security-oriented reading would examine the boundary where externally obtained webpage content becomes model input and the boundary where model output becomes a browser command. Appendix B visibly places simplified HTML, history, tabs, viewport, and task in the prompt. This identifies interfaces worth testing, but does not demonstrate that any supplied webpage contains an attack or that the interfaces are exploitable. [D; pp. 4, 11]

## 7. Methodology

### Interaction architecture

The framework acquires HTML and screenshots, processes them through an HTML parser and OCR module, marks operable elements, and creates a simplified HTML representation. The observation also contains the user's task, current location, and past commands. The model predicts an action; an automated browsing program executes it; the updated webpage supplies the next observation. Figure 3 shows this feedback loop alongside the data and training pipeline. [A/B; pp. 3–4]

Window position and page size help the model distinguish the visible region from the full page. Explicit previous commands are intended to reduce repetition of unsuccessful operations. These are design rationales; the supplied evaluation does not separately ablate every observation component. [A; p. 5]

The ten action categories are click, hover, select, type_string, scroll_page, go, jump_to, switch_tab, user_input, and finish. They cover element interaction, movement through pages/tabs, requesting user interaction, and termination with an answer. The presence of user_input does not establish a mandatory approval mechanism for every action. [A; p. 4, Table 1]

### HTML Pruner

Algorithm 1 accepts a tree, retained element identifiers, a recursion count, maximum depth, maximum children, and maximum siblings. It accumulates retained elements and nearby ancestors, descendants, and siblings. The neighborhood parameters are made smaller between iterations. It traverses the tree in reverse and removes nodes outside the accumulated collection or nodes that lack retained structural/content properties. [A/B; p. 4]

Important details remain unspecified: initial parameter values; the rule for selecting kept elements; the exact update function; the typo-like getAnscendants name; and whether tree.remove(element) uses element as an alias for the loop's node. The pseudocode also accumulates nodes across passes, so decreasing neighborhood limits should not automatically be interpreted as removing nodes previously accumulated. This is an algorithm-reading caveat, not a measured defect. [D; p. 4]

### Recognition and single-step data

The authors collect URLs from Chinese and English mainstream websites listed on Similarweb. Their parser identifies actionable components and records position and size. Recognition examples ask about site or component functions; GPT-3.5-Turbo varies question formulations and generates target responses from simplified HTML, with a response-length limit whose numerical value is not reported. [A; p. 5]

For one-step operations, the authors first identify executable actions using rules, then generate corresponding task descriptions and intentions. Their earlier attempt to ask GPT-3.5-Turbo to generate tasks, intentions, and operations, followed by Selenium validation, was insufficiently accurate and difficult to judge. Fixed operations such as scrolling and URL jumps use templates; flexible operations such as clicking and typing use model assistance. Dataset proportions are adjusted according to operation frequency in practice, but those frequency measurements are not supplied. [A; pp. 5–6]

### Complex-task data and annotation

They initially design 50 complex tasks per website using prompting inspired by Evol-Instruct, then manually select and label about 20 feasible tasks. Human annotators execute the tasks with a browser plugin that records actions. GPT-4 generates each step's intention using the overall sequence and critical HTML segments, rather than expensive, weakly connected step-by-step intention generation. The resulting thought chains are model-generated annotations, not direct measurements of the human annotators' reasoning. [A plus D qualification; p. 6]

Appendix D reports 20 annotators working for one month in Google Chrome. They check whether website descriptions match tasks and assess clarity, relevance, achievability, complexity, and subjectivity. They skip unsuitable tasks, record login/captcha steps, manually edit answers where required, and may change or abandon infeasible tasks. Demographics, training procedures, compensation, agreement measures, and exact rejection counts are unspecified. [A; p. 11]

The paper reports approximately 10,000 browsing traces as a contribution. Constructed data are merged with Mind2Web and MiniWoB++ training data. Figure 5 displays the final distribution, but its count-unit ambiguity prevents safely reconstructing an exact total dataset size from the pie chart. The number of websites is not stated in the supplied material. [A/B; pp. 2, 6]

### Three training stages

First, SFT follows a curriculum: webpage recognition and single-step operations, then complex-task planning and reasoning. Appendix A gives learning rate 1e-5 and batch size 32. Epoch counts, optimizer, sequence length, hardware, random seeds, and model checkpoint revision are not specified. [A; pp. 6, 11]

Second, the SFT model samples complex-task operation examples 20 times. Cases are retained when they succeed between 1 and 19 times, inclusive. Always-correct cases lack useful negative examples; always-incorrect cases are excluded because the authors suspect data problems and poor fit. Duplicate erroneous operations are removed. The resulting contrastive dataset is approximately 13k, with an unclear record unit. DPO uses learning rate 1e-6, batch size 64, and beta 0.15. The authors add SFT loss because direct DPO was unstable. Appendix A reports an SFT weighting factor of 0.8, whereas Equation (4) explicitly places an unspecified lambda on DPO. The exact mapping is unresolved. [A; pp. 7, 11]

Third, RFT collects successful trajectories in MiniWoB++ and WebArena. MiniWoB++ queries come from its generator, with the quantity adjusted for task difficulty. WebArena queries are manually constructed from templates to avoid test overlap; each sample receives 64 attempts. Environment evaluation identifies MiniWoB++ success, while manually written rules judge WebArena success. Approximately 15k traces/66k steps and 240 traces/2k steps are collected, respectively. The model is finetuned separately for these environments with learning rate 1e-5 and batch size 32. These conditions are central to interpreting the final results as environment-adapted performance. [A; pp. 7, 11]

### Benchmark construction and evaluation

AutoWebBench comes from the complex-task dataset and distinguishes familiar websites from websites excluded from training. It includes English and Chinese conditions. The text states 50 browsing traces for each split, but its transition from two website-familiarity splits to four language/familiarity conditions leaves the exact allocation less explicit than desirable. No unqualified total of 200 test traces is assumed here. Human verification filters the selected traces. SSR is the stated metric. [A; pp. 7–8]

Mind2Web evaluation uses the MindAct framework and SSR. Table 3 notes top-10 candidates for GPT-4 and top-50 otherwise. MiniWoB++ evaluation uses 56 tasks and 100 episodes per task. WebArena integrates the authors' HTML parser and action-execution module. The supplied paper does not state the WebArena evaluation task count or full evaluation software versions. No confidence intervals, statistical significance tests, or seed-based variation estimates are reported. [A; p. 8]

## 8. Experiments / Analyses

| Experiment | Purpose and conditions | Evidence and results | Qualification |
|---|---|---|---|
| X1 AutoWebBench | Compare English/Chinese and familiar/unfamiliar website operations using SSR. | Table 2: AutoWebGLM 64.8/58.6/65.4/61.8; GPT-4 38.6/39.7/36.7/36.3. | Operation-level success; split allocation and SSR implementation are incompletely detailed. |
| X2 Mind2Web | Assess cross-task, cross-website, and cross-domain generalization through MindAct. | Table 3: AutoWebGLM 66.4/56.4/55.8, average 59.5. | GPT-4 uses fewer candidates; HTML-T5-XL has higher results on all three conditions. |
| X3 MiniWoB++ | Test browser-component tasks after relevant environment training. | Table 4: 89.3; Table 8 supplies 56 task-level results. | 100 episodes per task stated for the evaluation; uniform protocol for every imported baseline is not established. |
| X4 WebArena | Test task completion in integrated website environments after RFT. | Table 4: AutoWebGLM 18.2 versus GPT-4 14.4. | Environment-specific adaptation; most tasks still do not succeed if the percentages are read as completion rates. |
| X5 Efficiency | Identify time spent fetching, parsing, predicting, executing, and loading. | Table 5: prediction 47.89%, loading 41.64%. | Timing units, hardware, workload count, and dispersion are not reported. |
| X6 Training-data ablation | Add simple-stage, complex-stage, or both constructed datasets. | Table 6: combined data gives 61.8/56.7/81.7/8.3. | Data quantity and curriculum effects are not fully isolated. |
| X7 Training-strategy ablation | Compare SFT, added DPO, and added RFT. | Table 6: DPO gives 62.7/59.5/80.8/8.5; final adapted results 89.3/18.2. | DPO lowers MiniWoB++ relative to SFT; RFT unavailable for offline-style evaluations. |
| X8 Cases and error analysis | Inspect everyday, leisure, and academic tasks and classify failures. | Figure 2 and Table 7; error shares 44/28/20/8%. | No error sample size, labeling agreement, or adversarial condition is reported. |

These are separate analyses. A high MiniWoB++ result does not establish high WebArena completion, and an SSR advantage does not establish a security advantage. No experiment tests an attacker, malicious prompt, poisoned page, or protected asset.

## 9. Results

AutoWebGLM leads every listed model in all four AutoWebBench columns. Its English cross-task result is 64.8 versus GPT-4's 38.6. The **analyst-derived** difference is 64.8 − 38.6 = **26.2 percentage points**. English cross-domain yields 58.6 − 39.7 = **18.9 points**; Chinese cross-task gives 65.4 − 36.7 = **28.7 points**; Chinese cross-domain gives 61.8 − 36.3 = **25.5 points**. These are absolute percentage-point differences, not relative percentage improvements. [C; p. 8, Table 2]

For Mind2Web, AutoWebGLM's reported average exceeds GPT-4's by 59.5 − 30.9 = **28.6 percentage points**, but falls below HTML-T5-XL by 66.9 − 59.5 = **7.4 points**. This comparison requires the candidate-count and finetuning caveats in Table 3. The source supports strong performance against several listed models, not universal superiority. [C; p. 8]

On MiniWoB++, AutoWebGLM obtains 89.3 versus HTML-T5-XL's 85.6, an **analyst-derived 3.7-point difference**. Against GPT-4's 32.1, the difference is **57.2 points**. On WebArena, 18.2 − 14.4 = **3.8 points** over GPT-4. The MiniWoB++ and WebArena results follow separate successful-trajectory finetuning. They are not a single unchanged model's demonstrated zero-shot outcomes in both environments. [A/C; pp. 7–8]

The data ablation suggests complex-task data contributes strongly. In AutoWebBench, simple-stage data produces 23.5 and complex-stage data 60.2; combined stages produce 61.8. For MiniWoB++, the analogous values are 48.3, 78.9, and 81.7. However, the experiment does not cleanly separate added data volume, task variety, and curriculum ordering. [A plus D qualification; p. 9]

DPO improves AutoWebBench from 61.8 to 62.7, Mind2Web from 56.7 to 59.5, and WebArena from 8.3 to 8.5, but decreases MiniWoB++ from 81.7 to 80.8. The **analyst-derived changes** are +0.9, +2.8, +0.2, and −0.9 percentage points, respectively. RFT subsequently raises the environment-specific MiniWoB++ result from 80.8 to 89.3 and WebArena from 8.5 to 18.2: **+8.5 and +9.7 points**. [C; p. 9, Table 6]

Runtime is concentrated in prediction and page loading. Their reported shares sum to 47.89 + 41.64 = **89.53%**, an analyst-derived combined share. The average stage values sum to 436.93 + 68.68 + 2407.34 + 20.36 + 2092.13 = **5025.44 in the table's unspecified timing units**. Calling this 5.025 seconds would assume milliseconds without an explicit source unit, so that conversion is not made. [C; p. 8, Table 5]

The error distribution assigns 44% to hallucinations, 28% to poor graphical recognition, 20% to task-context misinterpretation, and 8% to pop-up interruption. These sum to 100% of the categorized errors. They are not percentages of all tasks and do not measure attack success. The paper provides no denominator that would convert them into an overall failure rate. [A/C; p. 9, Table 7]

## 10. Figure-by-figure interpretation

### Figure 1 — Multi-benchmark performance overview

This is a radar chart on p. 1. Its six spokes are WebArena, English AutoWebBench, and Mind2Web cross-task, cross-website, cross-domain, plus MiniWoB++. The legend distinguishes GPT-3.5-Turbo, GPT-4, LLaMA2-70B, AutoWebGLM, and Human using colored lines or filled polygons. A blue AutoWebGLM outline generally extends beyond several model polygons, while the human reference extends farther on several spokes. [B]

The human reference labels include 78.2, 75.0, 72.6, 69.3, 70.4, and 93.5 around the respective spokes. These labels should not be misattributed to AutoWebGLM. The plot does not clearly label every model's exact coordinate or provide a sufficiently explicit normalization/tick explanation. Exact model comparisons therefore rely on Tables 2–4. No confidence intervals or statistical markers are visible. The figure communicates breadth of evaluation, but does not make unlike benchmark metrics interchangeable. [B/D]

### Figure 2 — Four browser demonstrations

The four panels on p. 2 show (a) a detailed weather search, (b) choosing a Christmas gift for children, (c) finding an article about LLMs, and (d) finding a differential-equation tool. Each panel combines a website view with a purple agent interface showing task/action exchanges. These are qualitative execution examples, not statistical plots. There are no axes, measurement units, error bars, or success-rate denominators. [A/B]

The demonstrations illustrate variety: weather information, shopping, technical reading, and mathematical assistance. Small interface text cannot all be transcribed confidently from the supplied resolution. The caption and recognizable interfaces support the task identities; they do not establish repeatability, absence of human help, or an adversarial security result. [D]

### Figure 3 — System architecture

On p. 4, three areas connect data construction, training, and interaction. Source data includes real environments and open training sets; hybrid human–AI construction and virtual-environment traces supply training. Curriculum learning, reinforcement learning, and RFT feed the agent. On the interaction side, webpages provide screenshots and HTML; parsing uses OCR and HTML tools; observations contain parsed HTML/history/task; the model chooses an action; execution and element selection change the page. [A/B]

Arrows show both a forward training pipeline and a repeated interaction loop. Icons visually distinguish data storage, annotation, browser windows, OCR, parser structure, and the agent. The figure is a conceptual diagram without numerical axes or measured component reliability. Its main support is architectural: model inference is embedded in a browser-control cycle. Security isolation and authorization enforcement are not shown. [D]

### Figure 4 — Two-stage data construction

The p. 6 diagram separates simple-task construction from complex-task construction. Stage 1 uses webpage examples, templates, matching rules, and model prompts to produce recognition questions and single-step operation examples. Stage 2 generates candidate tasks, filters them manually, records human multi-step operations, and uses an LLM to infer step intentions. [A/B]

A shopping example illustrates searching for the latest MacBook and sorting products. A rejected weapon-related task is marked as filtered. This is an example of manual task screening; it is not a quantified safety test or a deployed security control. The diagram uses example commands such as type and exit that do not exactly match Table 1's type_string and finish naming. They are illustrative workflow labels, not additional formally specified action types. [B/D]

### Figure 5 — Training-data composition

The p. 6 pie chart has five colored slices. Its labels are complex task 60 (38.71%), web recognition 40 (25.81%), simple task 42 (27.1%), MiniWoB 6 (3.87%), and Mind2Web 7 (4.51%). The percentages sum to 100.00%, while the displayed count values sum to 155. [B/C]

The colors encode categories and slice area represents proportion; there are no axes or uncertainty bars. The substantive observation is that the constructed recognition, simple-operation, and complex-task categories dominate the illustrated training mixture. The units of 60/40/42/6/7 are not explicitly stated in the caption or readable labels. They must not silently be expanded into thousands of examples or equated with the approximately 10,000 traces in the contribution statement. Exact absolute dataset size remains unresolved. [D]

### Figure 6 — Three-stage training

The three p. 7 panels show curriculum learning, sampled-error learning, and successful-trace finetuning. The first starts from ChatGLM3-6B and progresses through reading/operating and planning/reasoning. The second samples model operations, pairs them with golden operations, and trains using DPO plus SFT. The third runs the DPO model in environments, keeps correct traces using environment signals, discards erroneous ones, and trains on retained traces. [A/B]

The visual check and cross marks represent correct/incorrect outputs, not confidence intervals or statistical test outcomes. Arrows clarify which model supplies the next stage's data. The final stage is environment-specific self-play and selection; it should not be described as unrestricted lifelong adaptation proven across arbitrary live websites. [D]

## 11. Table-by-table interpretation

### Table 1 — Browser action interface

On p. 4, rows specify commands and their meanings. click(id) activates an element; hover(id) positions over one; select(id, option) chooses an option; type_string(id, text, enter) enters text; scroll_page(direction) moves the page; go(direction) goes backward/forward; jump_to(url, newtab) navigates to a URL; switch_tab(id) changes tabs; user_input(message) asks the user to interact; finish(answer) stops with an answer. This is an interface specification, not a performance comparison. Preconditions, argument validation, privilege limits, and security approval policies are not specified in the table.

### Table 2 — AutoWebBench

All values below are author-reported operation-performance values on p. 8, read in the paper's percentage-style SSR context. The table itself does not print a percent sign in each cell.

| Model | Size | EN cross-task | EN cross-domain | ZH cross-task | ZH cross-domain |
|---|---:|---:|---:|---:|---:|
| GPT-3.5-Turbo | N/A | 12.1 | 6.4 | 13.5 | 10.8 |
| GPT-4 | N/A | 38.6 | 39.7 | 36.7 | 36.3 |
| Claude2 | N/A | 13.2 | 8.1 | 13.0 | 7.9 |
| LLaMA2 | 7B | 3.3 | 2.5 | — | — |
| LLaMA2 | 70B | 8.3 | 8.9 | — | — |
| Qwen | 7B | 9.0 | 7.6 | 9.1 | 7.5 |
| AutoWebGLM | 6B | 64.8 | 58.6 | 65.4 | 61.8 |

AutoWebGLM is highest in every column. LLaMA2-7B is lowest among reported English values; Qwen has the lowest reported Chinese values. Dashes represent unreported entries, not zero. GPT-4's English cross-domain result slightly exceeds its cross-task result, so unfamiliar-site evaluation is not uniformly lower for every model. No uncertainty estimates or significance markers accompany the values.

### Table 3 — Mind2Web

| Model | Reported size | Cross-task | Cross-website | Cross-domain | Average |
|---|---:|---:|---:|---:|---:|
| GPT-3.5-Turbo | N/A | 17.4 | 16.2 | 18.6 | 17.4 |
| GPT-4† | N/A | 36.2 | 30.1 | 26.4 | 30.9 |
| Flan-T5-XL* | 3B | 52.0 | 38.9 | 39.6 | 43.5 |
| Html-T5-XL* | 543B | 71.5 | 62.2 | 67.1 | 66.9 |
| LLaMA2* | 7B | 52.7 | 47.1 | 50.3 | 50.1 |
| LLaMA2* | 70B | 55.8 | 51.6 | 55.7 | 54.4 |
| Qwen-VL* | 9.6B | 12.6 | 10.1 | 8.0 | 10.2 |
| SeeClick* | 9.6B | 23.7 | 18.8 | 20.2 | 20.9 |
| AutoWebGLM | 6B | 66.4 | 56.4 | 55.8 | 59.5 |

The dagger means top-10 candidates rather than top-50. The asterisk denotes finetuning on the training set. AutoWebGLM also uses Mind2Web training data according to §4.1.2, despite lacking the asterisk in this row. Html-T5-XL leads all three conditions and the average; Qwen-VL is lowest. The 543B size is reproduced as printed, not independently corrected or interpreted as the isolated size of an HTML encoder. Average values may reflect rounding of underlying results rather than exact arithmetic on the displayed cells.

### Table 4 — MiniWoB++ and WebArena

| Model | Size | MiniWoB++ | WebArena |
|---|---:|---:|---:|
| GPT-3.5-Turbo | N/A | 13.4 | 6.2 |
| GPT-4 | N/A | 32.1 | 14.4 |
| Text-Bison-001 | N/A | — | 5.1 |
| LLaMA2 | 7B | 42.8* | 1.2 |
| LLaMA2 | 70B | 47.1* | 0.6 |
| Html-T5-XL | 543B | 85.6* | — |
| WebN-T5-XL | 3B | 48.4* | — |
| Lemur | 70B | — | 5.3 |
| AutoWebGLM | 6B | 89.3 | 18.2 |

AutoWebGLM is highest among listed results on both benchmarks. The asterisk denotes training-set finetuning; AutoWebGLM's own separate RFT is described in the methods and must also be considered. Missing values do not imply failure. The large MiniWoB++/WebArena gap shows that component-level simulated tasks and complex website completion differ substantially in difficulty and protocol.

### Table 5 — Execution efficiency

| Action | count/tr | Fetch | Parse | Predict | Execute | Loading |
|---|---:|---:|---:|---:|---:|---:|
| type_string | 1.00 | 362.00 | 28.88 | 2282.99 | 6.12 | 2082.61 |
| click | 3.62 | 438.62 | 72.07 | 2252.10 | 28.10 | 2094.60 |
| finish | 0.38 | 419.33 | 66.00 | 3054.16 | 6.00 | 2119.06 |
| scroll_page | 0.38 | 475.33 | 88.67 | 3396.37 | 5.33 | 2033.35 |
| Others | 0.25 | 680.50 | 152.50 | 2666.08 | 10.00 | 2142.92 |
| Average | — | 436.93 | 68.68 | 2407.34 | 20.36 | 2092.13 |
| Percentage (%) | — | 8.70 | 1.37 | 47.89 | 0.41 | 41.64 |

count/tr appears to mean occurrences per trace, but the abbreviation is not explicitly expanded. Timing units are unspecified. Prediction and loading dominate; execution is smallest at 0.41%. Clicking is the most frequent listed action. The average is not simply the unweighted mean of the action rows; the frequency column suggests weighting, but the exact computation is not stated. Reported percentage shares total 100.01%, consistent with displayed rounding. Hardware and sample size are absent.

### Table 6 — Data and training ablations

| Method | AutoWebBench | Mind2Web | MiniWoB++ | WebArena |
|---|---:|---:|---:|---:|
| Only Train Set | — | 48.1 | 44.3 | — |
| + Stage1 | 23.5 | 48.4 | 48.3 | 2.5 |
| + Stage2 | 60.2 | 55.2 | 78.9 | 7.6 |
| + Stage1+2 | 61.8 | 56.7 | 81.7 | 8.3 |
| SFT | 61.8 | 56.7 | 81.7 | 8.3 |
| + DPO | 62.7 | 59.5 | 80.8 | 8.5 |
| + RFT | — | — | 89.3 | 18.2 |
| AutoWebGLM | 62.7 | 59.5 | 89.3 | 18.2 |

Stage1 means recognition/simple-operation data; Stage2 means complex-task data. Combined data is strongest among data-ablation rows. DPO is not uniformly beneficial because MiniWoB++ decreases. RFT produces the best shown environment-specific results. The caption says AutoWebBench and WebArena do not have a training set; elsewhere the authors construct additional WebArena RFT queries. A cautious reading is that no provided original training split is available, while custom adaptation data can still be created. This interpretation is not explicitly resolved by the paper.

### Table 7 — Categorized errors

The four shares are hallucinations 44%, poor graphical recognition 28%, task-context misinterpretation 20%, and pop-up interruption 8%. Hallucinations are the largest category and pop-ups the smallest. The denominator is analyzed errors, with no reported count. Category criteria, exclusivity procedures, and annotation agreement are unspecified. These are operational failure categories, not an attacker taxonomy.

### Table 8 — Per-task MiniWoB++ results

Table 8 on p. 12 uses fractional success rates, rather than the percentage-style presentation in Table 4. Its averages are AutoWebGLM 0.893, HTML-T5-XL 0.856, WebN-T5-XL 0.484, GPT-4 0.321, and GPT-3.5-Turbo 0.134. Multiplying 0.893 by 100 gives 89.3%, an analyst-derived unit conversion consistent with Table 4.

All 56 AutoWebGLM entries are represented compactly below. Competitor rows are compressed to informative contrasts rather than copied in full.

| AutoWebGLM rate | Tasks |
|---:|---|
| 1.00 | choose-date; choose-date-easy; choose-date-medium; click-button; click-button-sequence; click-checkboxes; click-checkboxes-transfer; click-collapsible; click-dialog; click-dialog-2; click-link; click-menu; click-option; click-pie; click-shades; click-tab; click-tab-2; click-tab-2-hard; click-test; click-widget; email-inbox; email-inbox-forward-nl; email-inbox-forward-nl-turk; email-inbox-nl-turk; enter-date; enter-password; enter-text; enter-text-dynamic; focus-text; focus-text-2; grid-coordinate; guess-number; identify-shape; login-user; multi-layouts; multi-orderings; navigate-tree; search-engine; social-media; use-spinner |
| 0.93 | click-test-2 |
| 0.90 | social-media-all |
| 0.85 | use-autocomplete |
| 0.83 | click-checkboxes-large |
| 0.76 | click-collapsible-2; social-media-some |
| 0.74 | click-color; tic-tac-toe |
| 0.65 | count-shape |
| 0.64 | click-shape |
| 0.63 | login-user-popup |
| 0.57 | click-scroll-list |
| 0.50 | book-flight |
| 0.37 | click-checkboxes-soft |
| 0.15 | choose-list |
| 0.00 | enter-time |

The aggregate lead hides important reversals. HTML-T5-XL scores 0.99 on book-flight versus AutoWebGLM's 0.50; 0.99 versus 0.37 on click-checkboxes-soft; 0.99 versus 0.57 on click-scroll-list; and 1.00 versus 0.00 on enter-time. Conversely, AutoWebGLM scores 1.00 versus 0.00 on click-shades, 1.00 versus 0.13 on guess-number, and 1.00 versus 0.07 on use-spinner. On choose-list, AutoWebGLM's 0.15 is below both HTML-T5-XL's 0.22 and WebN-T5-XL's 0.16. GPT-4 leads AutoWebGLM on use-autocomplete, 1.00 versus 0.85. These exceptions matter because average performance does not imply uniform competence. No per-task uncertainty bars or statistical tests are supplied.

## 12. Diagram / Architecture Interpretation

Figures 3, 4, and 6 are the substantive diagrams and are visually inspected. Their combined information flow is: obtain websites and existing data → construct recognition/operation examples and annotated traces → train a base model through curriculum learning → generate contrastive errors → train with DPO/SFT → collect successful environment traces → finetune → run a recurring perception/decision/execution loop. [A/B; pp. 4, 6–7]

The data path supplies examples to training; the runtime path supplies page observations to the trained model; the control path sends model-selected operations to the browser. At runtime, execution alters the next observation, so history connects successive decisions. At training time, the model's own errors and successes affect later training examples. These are two different feedback mechanisms, and should not be conflated. [D]

For security research, the diagram identifies potential interfaces: page acquisition, parsing, model prompt assembly, operation selection, element resolution, execution, and history storage. The supplied paper does not assign adversarial control to any interface, measure an exploit, or specify which content is trusted. A schematic arrow from a webpage to model observation is evidence of information flow, not proof of malicious influence. [D]

The architecture also explains why ordinary language-model evaluation is insufficient to describe the whole system. Success depends on parser fidelity, action argument correctness, page loading, environment state, and model reasoning. This is a source-grounded interpretation of the system design. It does not quantify how much each component contributes to failure because most component-specific controls are absent.

## 13. Equations and mathematical concepts

### Unnumbered interaction equations — p. 3, §3.1

The source writes S = {HTML, URL, Window Position} and A = {click, scroll, type, …}. Here S denotes the state representation and A the action set. This compact notation identifies included information and operation categories; it is not a fully specified mathematical state space with all domains enumerated.

H_t = φ(H_(t−1), A_(t−1), S_t) updates history from previous history, previous action, and current state. φ is a history-update function; its implementation, retention policy, and summarization rules are not supplied. Its output is the next historical context.

A_t = π(S_t | H_t) represents action choice under a policy π based on current state and history. The conditioning bar should not be used to invent an unspecified probability model here; the prose describes a decision policy. S_(t+1) = T(S_t, A_t) represents environmental state transition after executing an action. T is not provided as a learned model or explicit simulator equation.

The combined update is (S_(t+1), H_(t+1)) = (T(S_t, A_t), φ(H_t, A_t, S_(t+1))). In ordinary language: choose an action, change the page, and update the record of what happened. The process stops at finish or a maximum interaction length. No proof of convergence, correctness, or security is given.

### Equation (1) — p. 6

L_SFT(π_θ) = −E_((x,y)∼D)[log π_θ(y | x)].

This is a supervised training loss: make target output y more likely for input x across dataset D. π_θ is the model policy with trainable parameters θ; log is the logarithm; E is the expectation over examples. The prose makes input/output roles clear, but does not formally enumerate the serialization of x and y for every dataset type. Lower loss favors matching the demonstrations. This objective supports both simple-operation and complex-task curriculum stages.

### Equation (2) — p. 7

L_DPO(π_θ; π_ref) = −E_((x,y_w,y_l)∼D)[log σ(β log(π_θ(y_w|x)/π_ref(y_w|x)) − β log(π_θ(y_l|x)/π_ref(y_l|x)))].

This contrasts preferred output y_w with dispreferred output y_l for the same input x, relative to reference policy π_ref. In context, the preferred side is associated with golden/correct operations and the dispreferred side with sampled errors. β scales the preference expression; Appendix A specifies β = 0.15. σ is used in the equation but not explicitly defined in the supplied prose. Its conventional functional identity is therefore not introduced as an author-supplied definition. The equation's visible role is to favor the preferred response relative to the rejected response under a reference comparison.

The reference policy's exact checkpoint is not explicitly stated. D_Const. names the constructed contrastive data in prose, while the equation uses D. The connection is natural from context, but detailed sampling weights and token-level likelihood computation are unspecified.

### Equation (3) — p. 7

L_SFT(π_θ; π_ref) = −E_((x,y_w,y_l)∼D)[log π_θ(y_w | x)].

This preserves a supervised objective on the preferred output. Although π_ref and y_l appear in the signature or sample tuple, neither appears in the displayed loss expression. The authors add it to stabilize DPO and preserve capabilities. The equation does not quantify preservation of general language performance, and no separate general-language benchmark is shown.

### Equation (4) — p. 7

L_Total = λ · L_DPO + L_SFT.

This combines preference learning with supervised fitting. λ scales DPO in the displayed equation. Its value is not defined there. Appendix A says the SFT loss is weighted by 0.8, without explaining the mapping to λ. One can imagine algebraic rescalings, but the supplied work does not establish which implementation was used. The discrepancy is preserved rather than silently repaired.

These equations specify learning objectives and interaction logic. They do not provide a theorem that the agent will perform correctly or resist attacks. Any security interpretation must remain separate from their optimization roles.

## 14. Interpretation and discussion

The strongest supported interpretation is that carefully structured observations and staged task-oriented training can make a comparatively compact language model useful for browser operation. The benchmark results and ablations support this within the reported settings. They do not isolate a single cause: parser design, training examples, curriculum, contrastive learning, and environment adaptation are jointly involved. [A/D; pp. 4–9]

The evaluation addresses the informal objectives unevenly. Multi-benchmark and bilingual results support broad operational capability. Data construction and annotation details support a reproducible conceptual pipeline, but exact website lists and counts are missing. Runtime breakdown supports a bottleneck analysis, but not a hardware-normalized speed comparison. RFT results support adaptation within two environments, not universal lifelong learning across the live web. [D]

Several consistency findings qualify the synthesis:

- **Table 2 versus Table 6:** the four Table 2 AutoWebGLM values are 64.8, 58.6, 65.4, and 61.8. Their analyst-derived arithmetic mean is (64.8 + 58.6 + 65.4 + 61.8)/4 = 62.65, which rounds to 62.7, matching Table 6. Equal weighting is not explicitly specified, so this is a plausible reconciliation, not a confirmed aggregation rule.
- **Appendix A versus §4.2.3:** 66k and 2k in the appendix correspond numerically to the main text's step counts, while the main text separately states 15k and 240 traces. The appendix does not name the unit in the same detail. It should not be read as 66k MiniWoB++ traces.
- **Equation (4) versus Appendix A:** λ weights DPO in the equation; 0.8 is described as weighting SFT in the appendix. Exact implementation is unresolved.
- **Table 6 caption versus custom WebArena RFT data:** no original training set and custom successful-trajectory data can coexist, but the source does not explicitly clarify its terminology.
- **Headline outperformance versus Table 3:** GPT-4 is surpassed in listed conditions, but HTML-T5-XL remains better on Mind2Web.
- **DPO prose versus ablation:** the discussion emphasizes improvement, whereas MiniWoB++ declines from 81.7 to 80.8 before RFT.
- **Reference alignment:** p. 3 places citation [19] among interactive web-agent work, but p. 10 identifies [19] as a biomedical-image network-compression paper. This visible bibliographic mismatch is not repaired using outside sources.

For the security question, the key distinction is between **operational unreliability** and **adversarial vulnerability**. Hallucinations, poor recognition, context errors, and pop-ups are observed reliability issues. They can motivate security experiments because the model controls browser actions, but the paper does not demonstrate malicious exploitation of those errors. [D]

## 15. Contributions and novelty

**System contribution:** a ChatGLM3-6B-based agent integrated with webpage acquisition, parsing/OCR, standardized observations, and executable browser operations. [A; pp. 2–4]

**Methodological contribution:** a human–AI data pipeline that uses rules for executable simple operations, human traces for complex tasks, and model-generated questions/intentions. [A; pp. 5–6]

**Training contribution:** curriculum learning followed by sampled-error DPO/SFT and successful-trace RFT. The ablations demonstrate associations between these choices and benchmark performance. [A; pp. 6–9]

**Dataset contribution:** approximately 10,000 real webpage-operation traces constructed through model assistance and manual work. Exact corpus structure and total final training-unit counts are not fully specified. [A; p. 2]

**Benchmark contribution:** AutoWebBench, described by the authors as the first bilingual English/Chinese webpage browsing evaluation dataset, with familiar and unseen website conditions. The priority claim is author-reported and is not independently verified here. [A; pp. 2, 7–8]

**Empirical contribution:** results across four benchmarks, runtime decomposition, data/training ablations, qualitative cases, and an error taxonomy. [A; pp. 8–9, 12]

**Availability contribution:** the authors report releasing code, model, and data at their repository. No repository content, license compatibility beyond the paper's own license, or artifact reproducibility was checked. [A; p. 1]

There is no supplied theoretical proof, new security threat model, attack benchmark, or empirical comparison of agent-versus-standalone vulnerability. The paper's relevance to those topics is inferential.

## 16. Limitations

### Authors' stated limitations

The authors acknowledge hallucinations, poor graphical recognition, task-context errors, and pop-up interruption. They state that HTML-centered input falters on maps, animations, and video browsing. They describe unfamiliar websites and unique operating logic as reducing efficiency and success. Unstable internet and other environmental factors reduce reliability. They also report that direct DPO loss was unstable and that automated complex-data generation was insufficiently accurate. [A; pp. 5–7, 9]

Network-policy constraints restrict their RFT experiments to sandbox environments. Data collection from actual browser users is limited by privacy/security concerns, redundant or incorrect operations, and difficulty confirming completion. Mobile deployment involves gesture complexity and system security restrictions. These are constraints discussed in the paper, not measured security vulnerabilities. [A; pp. 5, 7, 9]

### Additional evidence-based analyst observations

The supplied study lacks a standalone-model security control, adversarial inputs, protected-asset definitions, and attack-success measurements. Comparative vulnerability is therefore unassessed. [D; HIGH confidence in absence from supplied evaluation]

Benchmark comparisons differ in candidate counts, training exposure, environment-specific adaptation, and sometimes missing entries. No confidence intervals or significance tests accompany performance differences. Hardware, optimizer, seeds, exact website counts, and several dataset-size units are missing. The precise DPO/SFT weighting is unresolved. [D]

The error distribution lacks a denominator and coding protocol. Qualitative examples cannot establish an overall completion rate. Successful-trajectory filtering emphasizes solvable behavior and excludes always-failing sampled cases, which may limit what training learns about difficult or anomalous cases. This last point is an interpretation of the selection rule, not an author-tested consequence. [D; MEDIUM]

The parser is intended to preserve vital information, but there is no separate quantitative measurement of retained information, adversarial content handling, or parser-induced errors. The observation design's rationale is stronger than its component-specific empirical isolation. [D]

## 17. Threats to validity

The following labels are analyst-applied methodological categories; the authors do not organize a formal threats-to-validity section this way.

**Internal validity:** adding stages changes both data composition and learning procedure. Without matched data-volume and component controls, performance changes cannot uniquely identify curriculum order, intent annotation, or pruning as the causal factor. DPO's MiniWoB++ decrease also prevents a uniform-improvement conclusion. [D]

**Construct validity:** SSR measures successful steps, while episode/task completion measures a broader sequence outcome. Neither is an attack-resistance metric. Table 7 classifies observed operational errors, not compromised security properties. A model can score well on ordinary tasks without the supplied evidence establishing its behavior under malicious content. [D]

**External/ecological validity:** bilingual and unseen-website conditions broaden evaluation, but the source does not fully describe website diversity or population coverage. RFT uses MiniWoB++ and WebArena sandbox environments because of real-web network constraints. Results cannot automatically generalize to arbitrary live sites, advanced visual applications, or mobile environments. [A/D]

**Statistical conclusion validity:** repetitions are specified for MiniWoB++ but confidence intervals, seed variation, and significance testing are absent. Small numerical gains, such as WebArena's 8.3 to 8.5 under DPO, are descriptive differences rather than demonstrated statistically reliable effects. [D]

**Reproducibility:** useful hyperparameters and prompts are supplied, but hardware, software versions, optimizer, training durations, exact parser settings, dataset manifests, reward rules, and complete callable-function definitions are absent from the document. The repository may contain additional details, but it was not supplied or inspected. [D]

**Selection and annotation validity:** generated candidate tasks are filtered for feasibility, and annotators may revise or abandon tasks. This improves workable examples but may alter the difficulty distribution. GPT-4-generated intentions are reconstructions, not verified human cognitive reports. Agreement and rejection counts are unavailable. [A/D]

**Security validity for the reader's question:** no adversarial intervention establishes whether external content can override the task, whether erroneous actions violate authorization, or whether identical model weights behave differently with and without browser access. The comparative security claim remains UNKNOWN. [D]

## 18. Future work and open questions

### A. Author-proposed future directions

The authors propose combining HTML and webpage screenshots to exploit complementary strengths. Image input can help with icons and visual effects, while text is useful for numerals and extensive content. They propose reasoning strategies beyond chain-of-thought that use prior browsing experience. They also propose self-checking current state and verifying whether an operation had its intended effect. Finally, they identify mobile applications as promising, while noting smaller viewports, gestures, and additional system restrictions. [A; p. 9, §§6.1–6.3]

### B. Additional open questions — analyst interpretation

What happens when webpage text conflicts with the user's task? Which parts of the observation are treated as data versus authoritative instructions? Can a model-generated command be checked against an intended-action policy before execution? Does preserving prior commands help recovery, or can misleading history affect later steps? Does pruning remove irrelevant content while retaining harmful instructions? These questions arise from the architecture, but this paper does not answer them. [D]

A direct test of the reader's question would need controlled security outcomes and a matched comparison between the underlying language model and its browser-agent configuration. It would also need defined attacker control, assets, and authorization rules. This describes missing evidence needed to answer the question, not an experiment performed here. [D]

Other unresolved empirical questions include performance across new website versions, the effect of individual observation fields, exact success-rule quality, how often user_input is invoked, and whether RFT improves recovery on previously unsolved tasks rather than only familiar environment proficiency. The supplied evidence provides no numerical answers.

## 19. Terminology and notation glossary

| Term or symbol | Meaning in this work |
|---|---|
| LLM | Large language model; the agent's language-based decision component. |
| LM | Language model. |
| AutoWebGLM | Proposed browser-navigation agent based on ChatGLM3-6B. |
| 6B | Six billion model parameters, as described by the authors. |
| HTML | HyperText Markup Language; webpage structure/content supplied in simplified form. |
| OCR | Optical Character Recognition; module for annotating text during image parsing. |
| SFT | Supervised finetuning on target responses or operations. |
| CL | Curriculum learning, progressing from simpler to complex tasks. |
| DPO | Direct Preference Optimization; training with preferred/dispreferred outputs. |
| RFT | Rejection Sampling Finetuning; training on retained successful sampled traces. |
| CoT | Chain-of-thought; step-oriented reasoning/intent annotations in this study. |
| SSR | Step Success Rate; primary AutoWebBench/Mind2Web evaluation metric, incompletely operationalized in the supplied paper. |
| Trace/trajectory | A sequence of browser operations for a task. |
| Step | One operation within a trace. |
| Observation | Task, simplified HTML, location, and past operations available to the model. |
| Action space | Defined browser commands that the agent can emit. |
| Operable element | Page component marked as available for interaction. |
| Golden operation | Target/correct operation used in constructing contrastive data. |
| Cross-task | Evaluation on different tasks, with the benchmark's stated familiarity condition. |
| Cross-website/domain | Generalization conditions involving unfamiliar websites or domains; exact benchmark definitions are not reproduced in full. |
| S_t | Webpage/environment state at step t. |
| A_t | Selected action at step t. |
| H_t | Historical interaction information at step t. |
| φ | Function updating history. |
| T | State-transition function after action execution. |
| π, π_θ | Decision policy/model policy with trainable parameters θ. |
| π_ref | Reference policy used in DPO likelihood ratios; exact checkpoint unspecified. |
| x, y | Training input and target output. |
| y_w, y_l | Preferred and dispreferred outputs in contrastive training. |
| D, D_Const. | Training distribution/dataset and constructed contrastive data. |
| β | DPO scaling parameter; reported as 0.15. |
| λ | DPO coefficient in Equation (4); explicit value unresolved. |
| σ | Operator/function in Equation (2); not explicitly defined by the supplied prose. |
| E | Expectation over sampled dataset records. |
| log | Logarithm used in likelihood objectives. |
| rcc, d, mc, ms | HTML-pruning recursion count, depth, child limit, and sibling limit. |
| count/tr | Table 5 frequency abbreviation, apparently count per trace; expansion not explicit. |

## 20. Key numerical results

| Quantity/result | Value | Unit | Condition/context | Status | Source |
|---|---:|---|---|---|---|
| Base model size | 6 | billion parameters | ChatGLM3-6B-based agent | Author-reported | pp. 1–2 |
| Constructed real browsing corpus | approximately 10,000 | traces | Contribution statement | Author-reported | p. 2 |
| Candidate tasks | 50 | tasks per website | Initial complex-task generation | Author-reported | p. 6 |
| Selected tasks | about 20 | tasks per website | Manual feasible-task selection | Author-reported | p. 6 |
| Annotators and duration | 20; one month | people; time | Chrome/plugin annotation | Author-reported | p. 11 |
| AutoWebBench selection | 50 | traces per stated split | Allocation across four conditions not fully explicit | Author-reported | p. 8 |
| SFT learning rate/batch | 1e-5 / 32 | rate / examples | Initial curriculum | Author-reported | p. 11 |
| DPO sampling | 20 | attempts per example | Complex-operation sampling | Author-reported | pp. 7, 11 |
| Contrastive data size | approximately 13k | unspecified record unit | After filtering | Author-reported | p. 11 |
| DPO learning rate/batch/beta | 1e-6 / 64 / 0.15 | rate / examples / coefficient | Preference stage | Author-reported | p. 11 |
| SFT weighting statement | 0.8 | coefficient | Mapping to Equation (4) unresolved | Author-reported | p. 11 |
| WebArena RFT sampling | 64 | attempts per sample | Custom template-based queries | Author-reported | p. 7 |
| MiniWoB++ RFT data | approximately 15k / 66k | traces / steps | Successful samples | Author-reported | p. 7 |
| WebArena RFT data | approximately 240 / 2k | traces / steps | Successful samples | Author-reported | p. 7 |
| RFT learning rate/batch | 1e-5 / 32 | rate / examples | Separate environment finetuning | Author-reported | p. 11 |
| MiniWoB++ evaluation | 56 × 100 | tasks × episodes/task | Reported evaluation setup | Author-reported | p. 8 |
| Implied episode count | 5,600 | episodes | 56 × 100 | Analyst-derived | p. 8 |
| AutoWebBench results | 64.8 / 58.6 / 65.4 / 61.8 | percentage-style SSR | EN task/domain; ZH task/domain | Author-reported | p. 8, T2 |
| Mind2Web results | 66.4 / 56.4 / 55.8; 59.5 average | percentage-style SSR | task/website/domain | Author-reported | p. 8, T3 |
| MiniWoB++ result | 89.3 | percent success | Environment-adapted agent | Author-reported | p. 8, T4 |
| WebArena result | 18.2 | percent success | Environment-adapted agent | Author-reported | p. 8, T4 |
| WebArena lead over GPT-4 | 3.8 | percentage points | 18.2 − 14.4 | Analyst-derived | p. 8, T4 |
| Prediction share | 47.89 | percent runtime | Efficiency workload | Author-reported | p. 8, T5 |
| Loading share | 41.64 | percent runtime | Efficiency workload | Author-reported | p. 8, T5 |
| Combined prediction/loading | 89.53 | percent runtime | 47.89 + 41.64 | Analyst-derived | p. 8, T5 |
| Error shares | 44 / 28 / 20 / 8 | percent of categorized errors | Hallucination/graphics/context/pop-ups | Author-reported | p. 9, T7 |
| Training-mixture shares | 38.71 / 25.81 / 27.1 / 3.87 / 4.51 | percent | Complex/recognition/simple/MiniWoB/Mind2Web | Visually readable | p. 6, F5 |
| AutoWebGLM enter-time | 0.00 | fractional success | MiniWoB++ task | Author-reported | p. 12, T8 |
| AutoWebGLM choose-list | 0.15 | fractional success | MiniWoB++ task | Author-reported | p. 12, T8 |

No approximate graphical estimates are used as exact numerical evidence. Figure 1's unlabeled model coordinates remain qualitative.

## 21. Claim–evidence map

| Claim | Evidence | Object/experiment | Source | Qualification/evidence strength |
|---|---|---|---|---|
| The system connects webpage observation to executable browser actions. | Parser/OCR, observation, model action, and execution loop. | F3, T1, Appendix B | pp. 3–4, 11 | HIGH for architecture; no exploitation demonstrated. |
| Simplification is intended to retain useful HTML while reducing redundancy. | HTML Pruner and stated rationale. | ALG1 | p. 4 | HIGH for design; preservation quality not separately quantified. |
| Training combines rules, humans, and LLM-generated annotations. | Simple-operation construction and human complex traces. | F4, Appendices C/D | pp. 5–6, 11 | HIGH; generated intentions are not verified human reasoning. |
| Sampled mistakes support preference training. | 20 attempts, partial-success filtering, deduplication, DPO/SFT. | F6, E2–E4 | p. 7 | HIGH for method; coefficient mapping unresolved. |
| Environment-specific RFT improves listed task performance. | Successful trace collection and ablation gains. | X3/X4/X7, T6 | pp. 7–9 | HIGH descriptively; no uncertainty estimates. |
| AutoWebGLM exceeds listed GPT-4 AutoWebBench results. | Four model-versus-baseline columns. | X1, T2 | p. 8 | HIGH for reported conditions; SSR is not security performance. |
| It is not best on every evaluated benchmark. | HTML-T5-XL average 66.9 versus 59.5 on Mind2Web. | X2, T3 | p. 8 | HIGH; candidate/training conditions differ. |
| DPO improvement is not uniform. | MiniWoB++ 81.7 to 80.8. | X7, T6 | p. 9 | HIGH; descriptive reversal before RFT. |
| Prediction and loading dominate reported runtime. | 47.89% and 41.64%. | X5, T5 | p. 8 | HIGH; units/hardware unspecified. |
| Operational errors include hallucination, recognition, context, and pop-ups. | Four error categories and shares. | X8, T7 | p. 9 | HIGH for taxonomy; denominator absent. |
| Aggregate MiniWoB++ strength hides task failures. | enter-time 0.00 and choose-list 0.15 despite 0.893 average. | T8 | p. 12 | HIGH; task-level variation explicitly visible. |
| The work informs security interfaces without proving comparative vulnerability. | HTML enters prompt; actions alter browser; no adversarial comparison reported. | F3, T1, Appendix B, evaluation inventory | pp. 3–9, 11–12 | HIGH for relevance boundary; comparative effect UNKNOWN. |

## 22. Very simple explanation — Explain Like I'm 15

Imagine teaching a computer assistant to use websites. It has to recognize buttons and boxes, decide what to do next, click or type, and then check the new page. AutoWebGLM gives a language model that kind of browser interface. It also shortens the webpage information so the model can focus on useful parts, and keeps a record of earlier actions.

The researchers teach it in stages. First it learns easy things, such as what a search box does and how to enter text. Then it learns longer tasks from human demonstrations. Next it practices making decisions and learns which sampled answers were wrong. Finally, it practices in particular test environments and trains on the attempts that succeeded.

It performs better than the listed GPT-4 baselines on several browser benchmarks, but that does not mean it succeeds everywhere. One benchmark still has a stronger competing system. Some individual tasks are difficult or fail entirely, and WebArena success is only 18.2%. The assistant can misunderstand pages, invent a wrong operation, misread the task, or be interrupted by a pop-up.

For the security question, this paper shows why a browser agent is a bigger system to analyze than a language model alone: webpage information influences decisions, and those decisions can turn into real browser actions. But the researchers did not test malicious pages or compare security attacks against the same model with and without a browser. The paper helps identify where to investigate; it does not prove that web agents are more vulnerable.

## Completeness Audit

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/venue/abstract/keywords | Yes, text and visual | Yes | Represented in compressed form | Full author list follows below; emails and affiliation layout compressed. |
| §1 Introduction and contributions | Yes | Yes | Fully represented | Motivation, three challenges, contributions, deployment examples. |
| §2 Related Work: models | Yes | Yes | Represented in compressed form | Author positioning retained; individual cited papers not independently reviewed. |
| §2 Related Work: benchmarks | Yes | Yes | Fully represented | Offline/component/website evaluation distinction retained. |
| §2 Related Work: automation | Yes | Yes | Represented in compressed form | Repeated calls and large-system deployment comparison retained. |
| §2 Related Work: generated data/RFT | Yes | Yes | Represented in compressed form | Method categories and relevance retained. |
| §3.1 Problem Setup | Yes | Yes | Fully represented | All principal state/history/action equations explained. |
| §3.2 Framework | Yes | Yes | Fully represented | OCR/parser, element marking, observation/execution loop. |
| §3.2.1 Observation space | Yes | Yes | Fully represented | Task, HTML, location, past operations. |
| §3.2.2 Action space | Yes | Yes | Fully represented | All ten Table 1 commands represented. |
| §4 opening/data challenges | Yes | Yes | Fully represented | Cost, privacy/security, objectives, model limits. |
| §4.1.1 Recognition/simple tasks | Yes | Yes | Fully represented | URLs, parser, GPT-3.5, rules, templates, Selenium attempt. |
| §4.1.2 Complex tasks | Yes | Yes | Fully represented | 50/~20 tasks, humans, GPT-4 global intentions, merged data. |
| §4.2.1 Curriculum | Yes | Yes | Fully represented | Two curricular levels and SFT loss. |
| §4.2.2 Reinforcement/DPO | Yes | Yes | Fully represented | Sampling/filtering, duplicates, combined objective. |
| §4.2.3 RFT | Yes | Yes | Fully represented | Two separate environments, success rules, 64 attempts, traces/steps. |
| §4.3 AutoWebBench | Yes | Yes | Fully represented | Bilingual/familiarity conditions and count ambiguity. |
| §5.1 Main Results | Yes | Yes | Fully represented | Each benchmark treated separately. |
| §5.2 Efficiency | Yes | Yes | Fully represented | Complete timing table plus unit limitation. |
| §5.3 Data ablation | Yes | Yes | Fully represented | Complete result rows and causal caveats. |
| §5.3 Strategy ablation | Yes | Yes | Fully represented | Complete rows including DPO decline. |
| §5.4 Cases/error analysis | Yes | Yes | Fully represented | Demonstrations, categories, denominator limitation. |
| §6.1 Multimodal input | Yes | Yes | Fully represented | HTML/image strengths and difficult applications. |
| §6.2 Reasoning/self-checking | Yes | Yes | Fully represented | Unfamiliar sites, state/effect verification, instability. |
| §6.3 Mobile | Yes | Yes | Fully represented | Viewport/XML, gestures, system restrictions. |
| §7 Conclusion | Yes | Yes | Represented in compressed form | Repetition of contributions compressed. |
| Explicit research questions | Checked | Yes | Fully represented | None formal; objectives identified separately. |
| Formal hypotheses | Checked | Yes | Fully represented | None formal; complex-data explanatory hypothesis retained. |
| X1–X8 Experiments | Yes | Yes | Fully represented | Separate register with setup, results, caveats. |
| F1 Radar chart | Yes, visual | Yes | Represented in compressed form | Model coordinates not estimated; human labels distinguished. |
| F2 panels a–d | Yes, visual | Yes | Represented in compressed form | Task identities retained; tiny messages uncertain. |
| F3 Architecture | Yes, visual | Yes | Fully represented | Components, flows, loop, security interpretation boundary. |
| F4 Data diagram | Yes, visual | Yes | Fully represented | Both stages, screening, naming differences. |
| F5 Pie chart | Yes, visual | Yes | Fully represented | Exact percentages/count labels and unknown units. |
| F6 panels I–III | Yes, visual | Yes | Fully represented | Curriculum, sampled contrast, successful-trace selection. |
| T1 Actions | Yes | Yes | Fully represented | Ten operations. |
| T2 AutoWebBench | Yes | Yes | Fully represented | All model rows and four conditions. |
| T3 Mind2Web | Yes | Yes | Fully represented | All rows, candidate/finetuning notes. |
| T4 MiniWoB++/WebArena | Yes | Yes | Fully represented | All rows and missing entries. |
| T5 Efficiency | Yes | Yes | Fully represented | All rows and columns. |
| T6 Ablation | Yes | Yes | Fully represented | All rows and caption caveat. |
| T7 Errors | Yes | Yes | Fully represented | All categories and shares. |
| T8 Per-task results | Yes, visual and text | Yes | Represented in compressed form | All AutoWebGLM task values; competitor averages and informative exceptions; remaining competitor cells deliberately compressed. |
| E0a–E0e State/history/policy equations | Yes | Yes | Fully represented | Undefined implementation details identified. |
| E1–E4 Loss equations | Yes | Yes | Fully represented | Form, symbols, roles, weighting discrepancy. |
| ALG1 HTML Pruner | Yes | Yes | Fully represented | Inputs, neighborhood accumulation, removal, ambiguity. |
| Major contributions | Yes | Yes | Fully represented | System, method, training, data, benchmark, evaluation, availability. |
| Author-stated limitations | Yes | Yes | Fully represented | Operational errors and constraints separated from analyst concerns. |
| Appendix A | Yes | Yes | Fully represented | Rates, batches, beta, counts, unresolved weighting. |
| Appendix B | Yes | Yes | Represented in compressed form | Prompt components and one-command/comment design; omitted function definitions acknowledged. |
| Appendix C | Yes | Yes | Represented in compressed form | Task-operation-intention and full-trace intent formats. |
| Appendix D | Yes | Yes | Fully represented | Annotators, month, criteria, login/captcha, editing/abandonment. |
| Appendix E | Yes | Yes | Represented in compressed form | Table 8 covered as above. |
| Substantive footnotes | Yes | Yes | Represented in compressed form | Equal contribution/correspondence, website/tool references, paper license. |
| Acknowledgments | Yes | Yes | Inspected but deliberately compressed as secondary | Funding summarized below; not evidence of efficacy. |
| References [1]–[45] | Yes, text only | Yes | Represented in compressed form | Categories and visible [19] mismatch; full bibliography not reproduced. |
| Separate supplements | None supplied | No inspection possible | Missing from supplied material | No separate supplement established by supplied metadata. |
| Repository/model/data artifacts | Referenced only | Availability claim represented | Inaccessible in closed-document analysis | Contents and reproduction not reviewed. |

### Metadata and secondary material retained in compressed form

The authors are Hanyu Lai, Xiao Liu, Iat Long Iong, Shuntian Yao, Yuxuan Chen, Pengbo Shen, Hao Yu, Hanchen Zhang, Xiaohan Zhang, Yuxiao Dong, and Jie Tang. The first three are marked equal contributors; Yuxiao Dong and Jie Tang are corresponding authors. Affiliations include Tsinghua University, Zhipu AI, Beijing University of Posts and Telecommunications, and the University of Chinese Academy of Sciences. The paper is identified as KDD '24, August 25–29, 2024, Barcelona, with DOI 10.1145/3637528.3671620 and 12 pages. The rendered arXiv margin identifies 2404.03648v2 and 12 October 2024. These are source metadata, not outside verification. [A/B; p. 1]

The paper states a Creative Commons Attribution International 4.0 license. Funding acknowledgments name NSFC grants 62276148 and 62425601, the New Cornerstone Science Foundation/XPLORER PRIZE, and the Tsinghua–Siemens industrial intelligence/Internet of Things joint center. Correspondence addresses, exact affiliation layout, decorative icons, recurring headers, and full bibliographic entries are secondary and compressed. [A; pp. 1, 9–10]

Appendix B includes simplified HTML, task description, callable functions, previous commands, tabs, and viewport position/maximum size. It requests one command with a brief explanatory comment. The supplied function list explicitly abbreviates remaining definitions. Appendix C asks for one-step task/operation/intention triples, restricts typing to input/textarea in that construction prompt, and asks for one intention line per annotated action. These are training/runtime prompt contents, not instructions followed by this analysis. [A/B; p. 11]

### Missing or inaccessible material

No numbered text page is missing. Physical p. 10 has no supplied rendering and was inspected as text only. The repository, released model/data, cited papers, live websites, benchmark implementations, annotation files, and custom success rules were not supplied for inspection. There is no separate supplement to claim as reviewed. Exact runtime units/hardware, training software versions, seeds, epochs, website counts, parser parameters, and full function definitions are unavailable from the supplied document.

### Uncertain interpretations

Figure 1's precise model coordinates and normalization are unclear; Figure 2's tiny messages are partly unreadable; Figure 5's count units are unspecified. AutoWebBench's exact 50-trace allocation is not fully explicit. Equation (4)/Appendix A loss weighting is unresolved. The contrastive dataset's approximately 13k unit is unspecified. The HTML Pruner contains naming/implementation ambiguities. No evidence resolves comparative security vulnerability or attack success. These uncertainties are preserved rather than filled using external knowledge.

### Deliberately compressed material

The complete competitor-by-task matrix in Table 8 is compressed while retaining all 56 proposed-model outcomes, all competitor averages, and key reversals. Browser screenshots are summarized by panel and visible workflow, not every tiny interface line. Related-work descriptions and the 45-reference bibliography are compressed to categories, relevant author claims, and the visible citation mismatch. Repetitive conclusion language, decorative diagram icons, affiliation/email detail, and funding metadata are secondary.

### Potential omissions

Every substantive section, subsection, figure, table, principal equation, algorithm, experiment category, appendix, contribution, and author-stated limitation identified in the inventory is represented either directly or with disclosed compression. Exact competitor cells omitted from the Table 8 transcription are known compressed content, not silently absent coverage. Any material outside the supplied 12-page document remains unreviewed. This audit supports coverage of the supplied work; it does not certify completeness of external artifacts or validate the paper's empirical claims independently.
