## Stage 0 — Document Accessibility Report

The supplied main document contains extracted text for physical PDF pages 1–16 and rendered source images for pages 1, 2, 3, 4, 5, 7, 8, 10, 12, 13, and 14. These physical page numbers are used throughout this report; the printed proceedings pagination is 13682–13697. The text begins with the title and abstract and ends with Appendix C.1. No intervening physical page is absent from the supplied text. This establishes coverage of the supplied 16-page document, rather than independently establishing that every associated research artifact has been supplied.

Visual inspection is available for 11 pages. Pages 6, 9, 11, 15, and 16 were inspected through supplied text only. All five numbered figures and all six numbered tables appear on visually supplied pages. The screenshots inside Figures 1 and 4 and Table A3 are small: their overall arrangement and purpose are visible, but their individual interface text is not comprehensively readable. Table values are generally readable, with native text providing an additional extraction aid. The instruction-tuning loss on page 15 has visibly corrupted extracted formatting and no supplied page image; its transcription must therefore remain qualified. No additional OCR was performed or needed for the readable main text.

Appendices A, B, and C are present despite the accessibility metadata reporting no detected appendix pages. Appendix A.3, entitled Supplementary Results, is part of the supplied paper and was inspected. No separate supplementary file, dataset, task JSON collection, repository implementation, full trajectory archive, or model output archive was supplied or inspected. The paper's repository link is an availability statement, not evidence that its contents were reviewed. The failed local-image reference to '-' provides no additional material; it does not prevent inspection of the eleven images actually included in the prompt.

Evidence categories: [A] AUTHOR-REPORTED identifies supplied author text; [B] DIRECTLY OBSERVABLE identifies readable visual content; [C] ANALYST-DERIVED identifies calculations with operands; [D] ANALYST INTERPRETATION identifies inference. No [E] external information is used. Confidence is HIGH for clearly stated text or readable values, MEDIUM for qualified interpretation, LOW for uncertain visual detail, and UNKNOWN where evidence is absent.

### Inventory established before synthesis

| Identifier | Original item | Physical pages | Access and significance |
|---|---|---:|---|
| S0 | Title, authors, abstract, contribution framing | 1–3 | Text and images; core framing |
| S1 | §1 Introduction | 1–3 | Text and images; motivation and contributions |
| S2 | §2 Related Works: Agent Benchmarks and Environments; Web Agents | 3 | Text and image; author positioning |
| S3.1 | §3.1 Environment; Action Space; Observation Space | 3–4 | Text and images; system and representation |
| S3.2 | §3.2 Dataset Construction; Data Structure; Annotators & Annotation Protocols; Performance Metrics | 4–5 | Text and images; construction and evaluation rationale |
| S3.3 | §3.3 Multimodal Web Content | 5 | Text and image; image/text dependence |
| S3.4 | §3.4 Multihop Cross-website Browsing | 5 | Text and image; sequencing |
| S3.5 | §3.5 Evaluation: Single-hop; Multihop | 5 | Text and image; acceptance rules |
| S4.1 | §4.1 Baselines | 6 | Text only; model and human comparisons |
| S4.2 | §4.2 Main Results | 6–7 | Text plus page-7 image; quantitative interpretation |
| S4.3 | §4.3 Analysis: Why are Multihop Web Tasks Challenging? Search Space; Agent Input Length | 7–8 | Text and images; failure analysis |
| S4.4 | §4.4 Memory-augmented Agents | 8 | Text and image; intervention |
| S5 | §5 Conclusion, Challenges, and Outlook; Future Work | 8–9 | Text; page 8 image; conclusion and proposal |
| S6 | §6 Limitations | 9 | Text only; website access constraints |
| S7 | §7 Ethical Considerations | 9 | Text only; model bias |
| REF | References | 9–11 | Text; page 10 image; bibliographic material |
| A.A1–A.A3 | Appendix A: settings, resources, supplementary hop results, memory ablation | 12–13 | Text and images; important experimental qualifications |
| A.B1–A.B2 | Appendix B: annotators, annotation protocols, statistics, tasks, links, comparison | 12–14 | Text and images; dataset details |
| A.C | Appendix C: datasets, model backbones, web/mobile agents; C.1 Other Benchmarks | 13–16 | Text throughout; images 13–14; expanded background |
| F1 | Figure 1: example compositional task | 2 | Visually inspected workflow |
| F2a–F2c | Figure 2: source websites, hop intents, multihop task counts | 4 | Three visually inspected panels |
| F3 | Figure 3: average actions by task hop count | 5 | Visually inspected bar chart |
| F4 | Figure 4: memory architecture | 8 | Visually inspected diagram |
| F5 | Figure 5: history-length performance | 8 | Visually inspected grouped bar chart |
| T1 | Table 1: benchmark comparison | 4 | Visually inspected |
| T2 | Table 2: benchmark results | 7 | Visually inspected |
| T3a–T3b | Table 3: GPT-4V and Gemini-Pro-Vision hop-position results | 8 | Visually inspected |
| TA1 | Table A1: GPT-4V results for 2–10 hops | 13 | Visually inspected |
| TA2 | Table A2: website links and Kiwix footnote | 14 | Visually inspected |
| TA3 | Table A3: VWA/MMInA task comparison | 14 | Visually inspected; embedded screenshot detail limited |
| E.POMDP | Partially observable process and transition notation | 3 | Text and image |
| E.PRED | A = f(I, M; θ) | 14 | Text and image |
| E.LOSS | Instruction-tuning loss, Eq. (1) | 15 | Text only; extraction-sensitive |
| X1–X4 | Baseline evaluation; hop-position analysis; memory ablation; descriptive dataset analysis | 4–8, 12–13 | Distinct analyses represented below |

No numbered algorithm, pseudocode listing, theorem, lemma, formal hypothesis, or explicit numbered research-question list appears in the supplied work. These are absent rather than omitted. The principal substantive footnotes concern equal contribution/project leadership/correspondence, the WebDataset link, and Kiwix URL changes.

## 1. Plain-language orientation

[A] MMInA: Benchmarking Multihop Multimodal Internet Agents evaluates artificial-intelligence agents that browse websites to carry out user requests. A request may require an agent to first discover a destination, then search for flights, arrange accommodation, and find relevant videos. These are connected subtasks: accomplishing one determines what should happen next. The paper calls a website-specific subtask a hop. Multimodal means that the agent must work with images as well as text.

[A] The researchers created 1,050 tasks, evaluated language models, multimodal models, specialized web agents, and humans, and introduced evaluation at both the hop and whole-task levels. The benchmark spans 14 website categories, permits 1–10 hops, and reports an average of 2.85 hops and 12.9 actions per task. They also tested replaying previous task trajectories as memory. Their central empirical finding is that completing an entire sequence is much harder for the evaluated agents than completing a one-hop task. Humans achieved 96.25% overall task success; GPT-4V achieved 21.77% in its non-history multimodal condition. These are task-performance results, not security attack rates. [p. 2, Fig. 1; p. 7, T2]

[D] For the requested research question, Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis, this paper provides architectural and reliability evidence that could inform a security argument. Agents ingest changing website content, convert it into actions, and may reuse histories. However, MMInA does not directly compare adversarial vulnerability of a web agent with a standalone conversational large language model. It contains no attack-success experiment. Its contribution to that question is indirect and must remain labeled analyst inference.

## 2. Document roadmap

[A] The introduction defines two motivating gaps: cross-website composition and combined visual/text understanding. Section 2 positions MMInA against tool benchmarks and previous web-agent benchmarks. Section 3 explains the browser environment, task construction, representations, and evaluators. Section 4 introduces comparison groups, presents Table 2, analyzes early failures, and proposes memory augmentation. Section 5 summarizes the benchmark, evaluation protocol, and memory intervention. Sections 6 and 7 discuss access limitations and ethical bias.

[A] Appendix A materially supplements the experiments with display settings, model identifiers, hardware, a longer hop-position table, and memory-ablation conditions. Appendix B explains annotation, travel-task composition, source questions, website links, and an example comparison with VisualWebArena. Appendix C expands the background into multimodal datasets, instruction tuning, web agents, mobile agents, and other benchmarks. References occupy pages 9–11. Reading only the abstract would miss the website exceptions, the non-monotonic long-hop results, and the specific model used for memory ablation.

## 3. Background and context

[A] A large language model, or LLM, processes language; a large multimodal model, or LMM, can also process modalities such as images. In this study either can serve as an agent's reasoning backbone: the model receives a task and observations and predicts a next action. A web agent couples that prediction with a browser interface that executes operations. The paper's use of standalone language models refers to models evaluated as reasoning backbones; it does not establish a separate security comparison with ordinary chat-only deployment. [pp. 1, 6]

[A] An accessibility tree is a structured representation of webpage elements. Its nodes contain an element identifier, type, and textual content. When an element is an image, the environment downloads it and marks its identifier on the image. The representation lets an agent refer to interface elements without receiving every detail of the complete underlying Internet state. Caption augmentation is a different route: BLIP-2 generates descriptions of website images that are added to textual input. Direct multimodal input instead supplies the images themselves. [pp. 3–4, 6]

[A] A trajectory is a sequence of observations and actions during task execution. Semantic memory represents general knowledge; episodic memory temporarily retains ongoing action sequences; procedural memory retains completed action sequences and outcomes for later use. Zero-shot reasoning is invoked in the authors' explanation of failures; the paper does not provide a separate formal definition or isolated zero-shot experiment. Related-work descriptions are author summaries, not independently verified accounts of those cited systems.

## 4. Research problem and gap

[A] Existing problem: realistic user requests often require information gathering and actions across several sites, while the agent must interpret both visual and textual evidence. According to the authors, earlier evaluations emphasize curated textual interfaces, simpler tasks, static environments, or restricted actions. Whole-task success alone can become nearly zero and reveal little about how far an agent progressed. [pp. 1–3, 5]

[A] Research gap: an evaluation environment combining multimodal information, longer cross-website sequences, evolving web content, and procedural measures of progress. Motivation: assess whether agents can handle natural shopping, search, booking, travel, and comparison tasks rather than only isolated website operations. Scope: task execution and reasoning under the supplied benchmark's interfaces and acceptance rules. It is not a formal security benchmark, systematic literature review, or general proof about all web agents.

[B/D] The paper's positioning needs qualification. Table 1 already assigns maximum hop counts above one to RUSS, WebArena, VisualWebArena, and WebVoyager. WebVoyager is listed at 4 maximum hops and 2.40 average hops. Therefore, the broad prose assertion that prior benchmark tasks require a single website is stronger than the paper's own comparison table supports. MMInA's tabulated distinction is a maximum of 10 and average of 2.85 hops, combined with its other design features. [p. 4, T1; pp. 3, 16]

## 5. Research questions, objectives, and hypotheses

[A] The abstract explicitly asks whether autonomous agents can move around multimodal websites to complete complex user tasks. The section heading in §4.3 asks why multihop web tasks are challenging. These are research-framing questions, not a numbered preregistered question set.

[A] Objectives are to introduce a benchmark with realistic multimodal cross-website tasks; evaluate LLMs, LMMs, specialized web agents, and humans; measure both completed hops and completed tasks; examine failure in longer sequences; and improve action prediction through replayed histories. The paper does not state formal statistical hypotheses or hypothesis tests.

[A/D] Section 4.3 articulates an expectation that an individual hop's success should be independent of total task hop count if its domain remains the same. The authors then compare semantically aligned first hops across different sequence lengths. This is an informal analytical expectation rather than a formally controlled causal hypothesis. The user's security question is external to the paper's own questions; relevance is evaluated as interpretation, without substituting it for the authors' objectives.

## 6. Assumptions / Threat Model

[A] The system assumes a task can be decomposed into ordered website-specific subtasks with identifiable completion conditions. The evaluator enforces completion in sequence: the next hop becomes available only after the current hop succeeds. Required intermediate states may be answer strings or particular URLs. The benchmark automatically moves the agent to the next site after a completed hop. Agents may explore unnecessary websites, but must satisfy the necessary ordered conditions. [pp. 5, 12]

[A] The partial-observation formulation assumes that the entire Internet/browser/agent state cannot practically be represented to the model. The observation substitutes accessibility-tree content, linked images, and action/state histories. The prompt specifies reference websites and rules, including stopping behavior. Human annotations identify crucial nodes through shortest successful paths. These assumptions shape what success means and the freedom available during browsing.

[D] No adversarial threat model is supplied. The paper does not specify attacker-controlled pages, malicious image content, attacker goals, trusted-versus-untrusted instruction boundaries, credential handling, permissions, exfiltration, or security policy enforcement. Browser actions, downloaded visual content, captions, histories, and evaluator inputs are observable system interfaces that could be investigated as security surfaces, but this paper does not demonstrate their exploitation. Its discussion of website protection mechanisms concerns difficulty retrieving images, not a tested agent defense. Confidence in any claim of increased security vulnerability from this paper alone is UNKNOWN.

## 7. Methodology

### Environment and representations

[A] MMInA models browsing as a partially observable decision process with state S, actions A, transition representation P, and reward R. At time t the agent receives a partial observation o_t and selects action a_t. Actions may be browser operations or textual answers. The action space is condensed into 12 summarized actions following VisualWebArena. Examples include clicking, scrolling, and keyboard typing; the supplied paper does not enumerate all twelve. Playwright and an X graphics server provide the browsing environment. [p. 3, §3.1]

[A] The textual representation is primarily an accessibility tree. Visible images are identified, downloaded, and annotated with element IDs. The viewport is 1280 × 2048. These dimensions are reported as display settings; the text does not explicitly attach a unit. Image/text-dependent tasks include comparing the appearance of two chairs. The authors claim every benchmark task requires visual and textual processing across turns, although the text-only baselines still achieve some success. [pp. 4–5, 12]

### Data construction and annotation

[A] Task styles were adapted from WebQA; GPT-4V generated similar multimodal questions; additional questions were manually crafted. Appendix B reports 108 question-answer pairs filtered from WebQA. Thus, the abstract's human-written description should be read alongside an assisted construction process, rather than interpreted as excluding model-generated question candidates. Three human annotators were trained, provided examples and guidelines, labeled different portions, and cross-validated diversity and answer accuracy. They varied in age and gender and signed agreements. No demographic counts beyond these statements, inter-annotator agreement statistic, or detailed adjudication procedure is reported. [pp. 4, 12–13]

[A] Annotators proposed templates varying in intent and difficulty, each producing 2–10 tasks. They followed shortest paths while recording all crucial website nodes. A successful agent trajectory may contain extra exploration; the necessary reference nodes should be included in it. Travel tasks commonly begin with Wikipedia destination identification and then combine flights, hotels, currency exchange, or other subtasks. Cooking tasks can combine Amazon purchasing and recipe searches. Each task JSON contains a question-answer pair and supporting materials; endpoint keywords may include a three-letter destination-airport code. [pp. 4, 12–13]

### Prompt and evaluator

[A] Prompt components are instructions, rules, examples, reference websites, and the task. Single-hop evaluation uses either must_include or fuzzy_match. The first requires all specified keywords; omission of any yields FAIL. The second asks a language model whether the predicted answer supports the reference answer, using a Yes/No response. GPT-3.5-Turbo is given as an example evaluator. This supports semantic flexibility, including the authors' gold/yellow color example, but the paper does not supply a quantified evaluator reliability study. [pp. 4–5]

[A] For N hops, the evaluation queue contains N completion conditions plus an END marker, so its length is N + 1. The agent must satisfy every hop in order to complete the task. Hop success rate is the percentage of successful targeted website visits; task success rate is the percentage of tasks completed. The precise aggregation of hop-position denominators is insufficiently elaborated to reconcile all tables. [pp. 5–7, 13]

### Models, resources, and reporting boundaries

[A] Comparisons include text-only agents, caption-augmented text agents, direct multimodal agents, history-augmented conditions, specialized WebShop/CogAgent agents, and humans. BLIP-2 provides captions. WebShop receives formatted queries generated by GPT-3.5-Turbo to adapt its original structured interface. API identifiers are gpt-4-0125-preview, gpt-4o-2024-11-20, gpt-4-vision-preview, gemini-1.0-pro-001, and gemini-1.0-pro-vision-001. Default model parameters are used. One Nvidia RTX6000 Ada with 48 GB memory runs local pretrained baselines, mostly 7B/8B/9B parameters. An inference epoch takes 4–8 hours, depending on the model. This runtime is not a per-task latency or API cost. [pp. 6, 12]

[A] The human comparison uses an average of three test takers, with varied socioeconomic backgrounds and no task information beforehand. The source does not specify a train/validation/test split, random seeds, exact action budgets, library versions, number of repeated model runs, confidence intervals, standard deviations, statistical tests, or full per-condition task assignment. Their absence limits reproducibility and statistical interpretation; it should not be filled with assumed defaults.

## 8. Experiments / Analyses

### X1 — Baseline and input-condition evaluation

[A] Purpose: evaluate current agents under alternative input representations and compare with humans. Setup: the MMInA task collection and Table 2 conditions. Variables include model identity, text versus captions versus direct images, and execution histories. Outcomes are hop and task success, stratified into one-hop, 2–4-hop, 5+-hop, and overall categories. This is a comparative benchmark experiment; model families differ in more than one factor, so cross-model differences cannot isolate modality alone. [pp. 6–7]

[B] GPT-4V without histories reports 42.91% one-hop success, 3.03% task success for 2–4 hops, 0% for 5+ hops, and 21.77% overall task success. Its overall hop success is 13.89%. Humans report 99.02%, 95.34%, and 88.12% task success in those respective hop groups, with 96.25% overall task success and 98.43% overall hop success. Caption-augmented DeepSeek-R1-Distill-Qwen-32B reports 47.68% one-hop success and 23.07% overall task success, but 0% task success for both multihop groups. Therefore its overall score must not be interpreted as strong multihop performance.

### X2 — Hop-position and sequence-length analysis

[A] Purpose: inspect where agents fail and whether first-hop performance changes with overall task length. The authors describe semantically aligning first hops. Table 3 reports GPT-4V and Gemini-Pro-Vision for lengths 2–6; Table A1 extends GPT-4V to 10. The underlying sample sizes for GPT-4V range from 200 two-hop tasks to 19 ten-hop tasks. No corresponding Gemini-Pro-Vision count table is supplied. [pp. 7–8, 12–13]

[B] GPT-4V first-hop success is 56.50% for two-hop tasks, 22.73% for three, 12.50% for four, 12.28% for five, and 16.67% for six. Later positions are usually zero. The longer appendix rows rebound to 25.42%, 40.00%, 56.67%, and 52.63% for lengths 7–10. The authors acknowledge fewer long tasks and fluctuation due to randomness. The full visible evidence therefore supports poor early/later progress, but not a monotonic decline at every increase in length.

### X3 — Memory intervention and history-length ablation

[A] Purpose: improve grounding and action prediction using prior trajectories. Appendix A.3 appends task descriptions, observations, and action trajectories from the last K tasks to the prompt. The authors say this narrows search space but increases input length and may introduce bias or disturbance. The ablation uses Gemini-Pro-Vision; K is varied, with typically K = 2 favored and K = 1 or 2 often preferable for simpler shopping/Wikipedia tasks. Model-agnostic applicability is a design claim, not demonstrated broad ablation across all backbones. [pp. 8, 12]

[B/C] Table 2 compares Gemini-Pro-Vision without histories at 18.40% overall task success with the history condition at 20.13%. The analyst-derived difference is 20.13 − 18.40 = 1.73 percentage points. Its 2–4-hop task score changes from 1.51% to 10.61%, a derived increase of 9.10 percentage points; its 5+-hop task score remains 1.13%. GPT-4o overall task success changes from 11.61% to 14.04%, a derived increase of 2.43 percentage points. Exact bars for each K in Figure 5 are not labeled and are not transcribed as exact measurements.

### X4 — Dataset descriptive analysis

[A/B] Figure 2 describes domain shares, action-versus-information intent, and task counts. Figure 3 describes average actions by task length. These are descriptive analyses rather than hypothesis-testing experiments. The dataset is strongly travel-oriented according to Appendix B, with Wikipedia and shopping also prominent. The text identifies a four-hop comparison-related exception to a simple actions-increase-with-hops pattern. Denominator and axis inconsistencies are discussed below.

## 9. Results

[A/B] The main finding is a large gap between evaluated agents and humans on complete task execution. The author prose rounds GPT-4V overall task success to 21.8% and human success to 96.3%; Table 2 gives 21.77% and 96.25%. These are consistent rounding representations. The analyst-derived task gap is 96.25 − 21.77 = 74.48 percentage points. No uncertainty interval accompanies that difference. [pp. 2, 7]

[B] Multihop success is frequently zero even where single-hop success is substantial. Caption-augmented DeepSeek-R1 reaches 47.68% on one-hop tasks but zero complete tasks in both multihop groups. GPT-4V reaches 42.91% one-hop task success but 3.03% for 2–4 hops and zero for 5+. Gemini-Pro-Vision with histories reaches 10.61% task success for 2–4 hops and 1.13% for 5+. These conditions illustrate why an overall score alone can hide the sequence difficulty. [p. 7, T2]

[B] Captions do not improve every metric. Gemini-Pro 2–4-hop success changes from 34.12% to 11.09% for hops while task success changes from 0.76% to 1.52%. GPT-4 changes from 30.56% to 20.70% hop success and from 9.09% to 3.79% task success in that group. The authors associate some divergence between hop and task scores with wandering and loops. The table supports mixed outcomes, while that causal explanation is based on the authors' trajectory analysis rather than a supplied trajectory archive. [pp. 6–7]

[A/D] The paper repeatedly calls improvement significant, but supplies no statistical test, p-value, confidence interval, or repeated-run variance. Here significant is preserved as author wording and interpreted as an observed performance improvement, not independently established statistical significance. The claim that multimodal models have higher overall performance is a broad author interpretation; Table 2 contains a caption-augmented text model whose overall task score exceeds GPT-4V's. This does not invalidate image usefulness, but prevents treating the broad statement as a universal ranking.

## 10. Figure-by-figure interpretation

### Figure 1 — Example of a compositional Internet task

[B] The diagram begins with a user request to identify which of Seoul or Tianjin has a central Ferris wheel, book travel, arrange accommodation, and find YouTube videos. It shows four labeled hops: Wikipedia for information seeking, Momondo for a flight action, Trip.com for accommodation, and YouTube for video search. Paired screenshots show within-hop progression; arrows connect stages; green check marks indicate successful milestones. Colored labels distinguish information seeking from actions. There are no quantitative axes.

[A] The caption reports 1,050 tasks, mean 2.85 hops, mean 12.9 actions, and maximum 10 hops. The figure illustrates ordered task decomposition and the rationale for assessing both phase-level and whole-task success. Screenshot details are too small to audit every visible action, booking state, or video. It is an illustrative successful workflow, not evidence that a evaluated model completed that exact task. [p. 2]

### Figure 2 — Dataset composition

[B] Panel a is a pie chart of source website categories: Wiki 28.4%, Shopping 13.0%, Hotel 10.3%, Flight 10.5%, Car rental 9.2%, Train 0.2%, YouTube 6.0%, Twitter 7.1%, Event 0.9%, Transfer 2.9%, Tour guide 5.6%, Food 5.7%, Amazon 0.2%, and Recipes 0.1%. The panel labels its total as 2,991 hops. Colors separate slices; no uncertainty information is supplied. These are rounded displayed shares, not exact raw category counts.

[B] Panel b is a two-slice pie chart: Information Seeking 35.3% and Action 64.7%. It describes hop intent, not proportions of whole tasks. Panel c is a bar chart with hop count 2–10 on the horizontal axis and bars apparently representing counts of multihop tasks. However, its vertical label reads '# Avg. Actions', conflicting with its caption 'Counts of multihop tasks'. The vertical ticks run from 0 to 200, and the two-hop bar reaches about 200, consistent with Table A1's count. Exact panel-c counts should therefore come from Table A1, not from the mislabeled axis. [p. 4]

### Figure 3 — Average actions as hop count changes

[B] A single bar series uses hop count 1–10 on the horizontal axis and '# Avg. Actions' vertically, with ticks through 30. The bars broadly grow from a few actions to just over 30. They have no numerical data labels or error bars. Exact bar heights are unavailable. [A] Appendix B explicitly states that average actions for five-hop tasks are lower than for four-hop tasks and attributes the difference to comparisons in the four-hop group. This is an important qualification to the general upward trend. [pp. 5, 12]

### Figure 4 — Memory-augmented agent

[B] The diagram centers on a Multimodal Agent connected to Semantic Memory on the left, Episodic Memory above, and Procedural Memory on the right. Semantic memory is associated with general world knowledge and Internet-navigation concepts. Episodic memory receives action trajectories shown as miniature screenshots. Arrows between episodic memory and the agent indicate interaction; a curved 'memorize' arrow leads toward procedural memory; a 'retrieve' arrow leads from procedural memory toward the agent. Procedural memory contains histories, strategies, and outcome icons. There are no quantitative axes. The diagram clarifies the conceptual distinction between ongoing experience and reusable strategies; it is not a full software architecture or retrieval algorithm specification. [p. 8]

### Figure 5 — Memory history length

[B] This grouped bar chart places Hop 1, Hop 2–4, Hop 5+, and Overall on the horizontal axis. The vertical axis is 'Performance', with a 0–40 scale; the figure caption calls the quantity success rates, but the axis omits an explicit percent sign and metric subtype. The legend gives history length 0–5, encoded with gray, blue/purple, and pink tones. No bar labels, error bars, or statistical markers are visible.

[B/D] History length two appears strongest in the Hop 1 and Overall groups; longer histories do not produce a monotonic gain. Hop 5+ bars remain close to the baseline. Exact heights cannot be treated as reported values. Appendix A identifies Gemini-Pro-Vision as the ablation model and supports the K = 2 interpretation. Its missing cross-reference phrase and the figure's generic Performance label leave some ambiguity about exact correspondence to Table 2 conditions. [pp. 8, 12]

## 11. Table-by-table interpretation

### Table 1 — Benchmark characteristics

[A/B] Columns compare multimodality, maximum/average hops, website type, dynamic interaction, and website count. MiniWoB++: multimodal, 1/1.00, static simplified, open-ended, 100 sites. WebShop: multimodal, 1/1.00, static simplified, open-ended, 1. Mind2Web: non-multimodal, 1/1.00, static real-world, MC, 131. RUSS: non-multimodal, 2/1.10, static real-world, MC, 22. WebArena: non-multimodal, 2/1.06, static real-world, open-ended, 6. VWA: multimodal, 2/1.05, static real-world, open-ended, 3. WebVoyager: multimodal, 4/2.40, dynamic real-world, open-ended, 15. MMInA: multimodal, 10/2.85, evolving real-world, open-ended, 14. MC is not expanded in the table; Appendix C's discussion of multiple-choice questions provides contextual support for that reading. This is an author comparison, not an independently validated census. [p. 4]

### Table 2 — Full comparative results

[B] All scores below are percentages. H means hop success; T means task success. Each four-number sequence is ordered as 1 hop / 2–4 hops / 5+ hops / overall. Input grouping is reconstructed from the table's visually merged icons and baseline description. Plain text rows use instructions and accessibility-tree content; captions add image descriptions; direct multimodal rows add images; history rows add execution histories.

| Condition | Agent | H: 1 / 2–4 / 5+ / overall | T: 1 / 2–4 / 5+ / overall |
|---|---|---|---|
| Text | Fuyu-8B | 0 / 0 / 0 / 0 | 0 / 0 / 0 / 0 |
| Text | CodeLLaMA-7B | 1.18 / 0 / 0 / 0.29 | 1.18 / 0 / 0 / 0.58 |
| Text | WebShop | 20.67 / 0 / 0 / 4.17 | 20.67 / 0 / 0 / 10.12 |
| Text | DeepSeek-R1-Distill-Qwen-32B | 21.61 / 1.85 / 1.62 / 4.74 | 21.61 / 0 / 0 / 10.46 |
| Text | Gemini-Pro | 19.09 / 34.12 / 2.13 / 11.85 | 19.09 / 0.76 / 0 / 9.54 |
| Text | GPT-4 | 14.37 / 30.56 / 5.23 / 12.26 | 14.37 / 9.09 / 0 / 9.34 |
| Text + captions | CodeLLaMA-7B | 5.71 / 0 / 0 / 1.61 | 5.71 / 0 / 0 / 2.79 |
| Text + captions | WebShop | 29.72 / 0.00 / 0.00 / 5.61 | 29.72 / 0 / 0 / 14.55 |
| Text + captions | DeepSeek-R1-Distill-Qwen-32B | 47.68 / 3.84 / 4.68 / 11.11 | 47.68 / 0 / 0 / 23.07 |
| Text + captions | Gemini-Pro | 30.12 / 11.09 / 0.05 / 12.38 | 30.12 / 1.52 / 0.38 / 15.22 |
| Text + captions | GPT-4 | 38.58 / 20.70 / 3.43 / 13.50 | 38.58 / 3.79 / 0 / 19.85 |
| Multimodal | CogAgent-9B | 6.92 / 0 / 0 / 1.06 | 6.92 / 0 / 0 / 3.35 |
| Multimodal | GPT-4o | 21.90 / 9.23 / 0.96 / 5.94 | 21.90 / 3.85 / 0 / 11.61 |
| Multimodal | Fuyu-8B | 27.36 / 0 / 0 / 5.52 | 27.36 / 0 / 0 / 13.39 |
| Multimodal | Gemini-Pro-Vision | 28.94 / 16.38 / 4.03 / 10.66 | 28.94 / 1.51 / 1.13 / 18.40 |
| Multimodal | GPT-4V | 42.91 / 21.23 / 3.99 / 13.89 | 42.91 / 3.03 / 0 / 21.77 |
| Multimodal + history | GPT-4o | 27.45 / 17.76 / 10.13 / 14.36 | 27.45 / 3.32 / 0 / 14.04 |
| Multimodal + history | Gemini-Pro-Vision | 39.17 / 23.93 / 4.78 / 14.27 | 39.17 / 10.61 / 1.13 / 20.13 |
| Original webpage | Human | 99.02 / 97.91 / 93.77 / 98.43 | 99.02 / 95.34 / 88.12 / 96.25 |

[B] Humans lead every displayed column. Among nonhuman conditions, caption-augmented DeepSeek-R1 leads one-hop and overall task success; text-only Gemini-Pro leads 2–4-hop H; history GPT-4o leads 5+-hop and overall H; history Gemini-Pro-Vision leads 2–4-hop T. Both Gemini-Pro-Vision conditions tie at 1.13% for the highest nonhuman 5+-hop T. Text Fuyu is zero throughout. No statistical significance marks or error terms appear. One-hop H and T match within each row, as expected for one required hop. Overall H and T need not match because their units of aggregation differ. [p. 7]

### Table 3 — First and later hop positions

[B] Rows are total task hop counts; columns are hop positions; units are SR(%). Dashes indicate positions that do not exist, while 0.00 indicates a measured zero. GPT-4V rows: 2 hops: 56.50, 11.00; 3: 22.73, 4.55, 0.00; 4: 12.50, 0.00, 0.00, 0.00; 5: 12.28, 1.75, 0.00, 0.00, 0.00; 6: 16.67 followed by five zeros. Gemini-Pro-Vision rows: 2: 69.28, 8.43; 3: 32.56, 0.00, 0.00; 4: 40.00 followed by three zeros; 5: 41.67, 5.00, then three zeros; 6: 31.03, 1.72, then four zeros. Darker green shading highlights larger rates. Both models show substantial early failure and near-zero later progress, but neither first-hop sequence is strictly monotonic. [p. 8]

### Table A1 — Longer GPT-4V sequences and counts

[B] The first five rows reproduce GPT-4V Table 3 with counts 200, 44, 16, 57, and 60 for lengths 2–6. Additional rows: 7 hops, count 59, sr1 25.42 and all later zeros; 8 hops, count 35, sr1 40.00 and all later zeros; 9 hops, count 30, sr1 56.67, sr2 20.00, sr3 3.33, and later zeros; 10 hops, count 19, sr1 52.63 and later zeros. Blank cells beyond the task's length are inapplicable, not zero. The caption's denominator description is awkward and does not fully resolve whether rates at later positions are unconditional over all tasks or conditional over reached positions. [p. 13]

### Table A2 — Website inventory

[A/B] Fourteen entries are listed: Wikipedia through library.kiwix.org; car rental at trip.com/carhire; flights at momondo.com; hotels at trip.com/hotels; events at eventbrite.com; Twitter at twitter.com/home; Amazon; YouTube; food at timeout.com; currency exchange at xe.com; travel guides at nomadicmatt.com; recipes at allrecipes.com; trains at trip.com/trains; and Shopping through offline OneStopMarket. Multiple entries share Trip.com's domain, so fourteen listed website categories should not automatically be read as fourteen distinct registrable domains. The Kiwix URL specifies a Wikipedia library path with a 2024-01 identifier. Its footnote warns that library updates can change URLs. The caption exempts Shopping from the evolving-real-world claim. [p. 14]

### Table A3 — Illustrative VWA comparison

[A/B] The VWA example asks when the programming language with the largest salary variance first appeared, using Wikipedia in a second tab. The MMInA example asks whether two named chairs both have armrests. Embedded website images accompany the tasks. The authors use this comparison to illustrate their emphasis on multimodal inputs at multiple steps. It is a two-example conceptual comparison, not a controlled experiment proving all MMInA tasks are harder than all VWA tasks. Individual screenshot content is too small for exhaustive visual verification. [p. 14]

## 12. Diagram / Architecture Interpretation

[A/B] The browser loop is: user task and prompt rules → structured website observation plus available images/history → model predicts browser operation or answer → environment executes operation → evaluator checks the current completion condition → either continue the hop or advance to the next queued hop → END when every condition succeeds. Figure 1 illustrates the sequential cross-site control path; §3 supplies the observation and action interfaces. The benchmark's automatic next-site movement is part of this loop, so autonomous transition planning should not be overstated.

[A/B] Figure 4 adds a memory path. Ongoing trajectories enter episodic memory; completed sequences and outcomes can become procedural records; the agent retrieves relevant past experience while semantic memory supplies general knowledge. Appendix A operationalizes the intervention by appending recent trajectories to prompts. The paper does not specify a learned retrieval index, similarity function, storage format, retention policy, memory sanitization step, or separate semantic-memory update experiment. [pp. 3–5, 8, 12]

[D] Security relevance arises at the boundary between observations and actions: externally encountered content is used to choose executable operations. The memory pathway introduces another possible persistence channel for encountered content. These are architecture-derived questions, not reported exploits. The study does not measure whether any memory record carries a malicious instruction or whether a browser operation causes security harm.

## 13. Equations and mathematical concepts

### E.POMDP — Partial observability

[A] The authors write ⟨S, A, P, R⟩ for their partially observable Markov decision process. S represents full Internet content plus browser and agent status; A is the action set; P is the transition representation; R produces PASS or FAIL for a hop. Ω denotes the partial observation space, o_t ∈ Ω an observation at time t, and a_t an action. The printed relation P: S × A → S′ associates a state/action pair with a subsequent state. Although called a probability matrix, the displayed notation maps to S′ and does not explicitly define a probability distribution over next states. This mismatch should be preserved rather than repaired with an external textbook definition. [p. 3]

[A/D] In ordinary language, the agent sees a limited webpage representation, acts, and gets new observations, while the evaluator decides whether a required subtask succeeded. No transition probabilities are estimated in the supplied experiments. This is a modeling framework, not an optimization algorithm trained by the paper.

### E.QUEUE — Sequential completion

[A] An N-hop task has a queue of N completion conditions and an END marker, giving N + 1 queue elements. N is the number of required hops. Completing all conditions in order is necessary for whole-task success. This simple arithmetic expresses the control logic rather than a learned objective. [p. 5]

### E.PRED — Multimodal model prediction

[A] Appendix C gives A = f(I, M; θ). Here I is an instruction and M the multimodal input. The preceding triplet I, M, R defines R as the ground-truth response. A is the predicted answer in this context. The source does not explicitly define θ in the immediate explanation; its placement suggests model parameters, which is analyst interpretation. A and R are reused symbols and must not be confused with the action set and hop reward in §3.1. The equation describes generic multimodal instruction following, not a new MMInA-specific algorithm. [p. 14]

### E.LOSS — Instruction-tuning loss, Eq. (1)

[A, qualified] The supplied page-15 extraction appears to express L(θ) = −Σ(i=1 to N) log p(R_i | I, R_<i; θ). Its typography is corrupted, and no page-15 image is supplied. The explanatory reading is a negative sum of log probabilities assigned to ground-truth response elements, conditioned on the instruction and earlier response elements. However, the source does not explicitly define N or token indexing here, and M is not visibly included in the extracted conditioning expression despite the preceding prediction equation using M. Those details remain uncertain. This is Appendix C background on instruction tuning; it is not evidence that the benchmark models were newly trained with this loss. [pp. 14–15]

## 14. Interpretation and discussion

[A] The authors explain failures through enlarged search spaces, long inputs, weak retention of previous steps, repeated actions, and failure to recognize completion conditions. They describe agents switching sites when an expected action fails, or lingering in a completed hop. The proposed memory mechanism is intended to ground reasoning with earlier experience. These are author-reported trajectory interpretations, with aggregate scores providing supporting context but no supplied full trajectories enabling independent event-level verification. [pp. 6–8]

[D] The benchmark answers its own capability question with substantial evidence of difficulty under the chosen interface and evaluator. It does not isolate the causal contribution of input length from task composition, model differences, or website difficulty. First-hop alignment helps address one confound, but the paper does not fully document the matching procedure or supply paired examples. The history results show useful improvements in some groups and no improvement in others; they support a bounded empirical benefit rather than a universal solution.

### Cross-reference and consistency checks

[A/B] Hop totals conflict: Figure 2a labels 2,991 hops, while §3.2 reports 2,989. With 1,050 tasks, these yield derived means of 2,991/1,050 ≈ 2.8486 and 2,989/1,050 ≈ 2.8467, both compatible with rounding to 2.85. Rounding therefore does not resolve which raw total is correct. [pp. 2, 4]

[C] Table A1 counts sum to 200 + 44 + 16 + 57 + 60 + 59 + 35 + 30 + 19 = 520 multihop tasks. If these rows exhaust all multihop tasks in the 1,050-task benchmark, the remaining one-hop count would be 1,050 − 520 = 530. Weighted multihop hops would be 2×200 + 3×44 + 4×16 + 5×57 + 6×60 + 7×59 + 8×35 + 9×30 + 10×19 = 2,394; adding 530 one-hop tasks gives 2,924 hops. This conditional reconstruction disagrees with both 2,989 and 2,991. The paper does not establish whether Table A1 is the complete corpus distribution or a model-specific subset, so the derived discrepancy remains conditional, not a corrected dataset total. [p. 13]

[A/B] Table A1's nine-hop row has sr3 = 3.33% and zeros afterward. Under strict sequential completion, this would imply at least some successful first-three-hop trajectories if the percentages are unconditional. Yet GPT-4V Table 2 reports only 3.03% whole-task success in the 2–4-hop group, while Table A1 shows 11.00% second-hop success for 200 two-hop tasks and 4.55% third-task-group second-hop success for 44 three-hop tasks. Different denominators, subsets, or configurations may be involved, but none can be confidently selected from supplied evidence. The tables should not be silently combined to compute a supposedly definitive whole-task score.

[A/B] Additional inconsistencies or qualifications: Figure 2c's y-axis label conflicts with its count caption; first-hop success is not monotonically decreasing across Tables 3/A1; the wholly evolving-site framing has an offline Shopping exception and a Kiwix library entry; the human-written framing coexists with GPT-4V-assisted generation and WebQA filtering; §4.1 announces four text-agent groups but visibly enumerates three; the claim that DeepSeek-R1 outperforms all other models on one-hop tasks requires a condition qualifier because direct GPT-4V exceeds text-only DeepSeek-R1. None is repaired by outside evidence.

## 15. Contributions and novelty

[A] Dataset/benchmark contribution: a 1,050-task collection intended to combine visual/text dependence, multiple website subtasks, and changing website content, with up to ten hops. Methodological contribution: paired hop-level and task-level evaluation, using ordered completion conditions to show intermediate progress when full success is rare. Empirical contribution: comparison across language, multimodal, specialized web, and human agents, plus failure analyses by sequence length. Algorithmic/system contribution: a lightweight memory intervention using previous task trajectories as prompt context. [pp. 1–3, 5–8]

[D] The supplied evidence supports these as the authors' stated contributions. It does not independently establish priority across all prior literature, universality across domains, or statistical significance. The mathematical expressions in Appendix C are background, not new theorems. The paper provides no security defense algorithm, adversarial dataset, or comparative vulnerability metric. Its security-research contribution is therefore possible supporting context, rather than a directly demonstrated security result.

## 16. Limitations

### Authors' stated limitations

[A] Section 6 explains that website protection mechanisms make direct image fetching from HTML difficult. Consequently, one website is an offline standalone site and another is an open-source site. Table A2 names the offline Shopping site as OneStopMarket and lists Wikipedia through Kiwix. The limitation section does not explicitly map its open-source phrase to a particular entry, so that identification should not be asserted as certain. [pp. 9, 14]

[A] Appendix A states that histories lengthen input, larger historical sets can introduce biases and disturbances, and the memory experiment was conducted with Gemini-Pro-Vision. It also states that fewer long tasks cause fluctuating success rates. Section 7 warns that bias in underlying multimodal models may lead to inaccurate or unfair outcomes. These are explicit author caveats even though they occur outside the titled Limitations section. [pp. 9, 12]

### Additional evidence-based analyst observations

[D] The available report lacks repeated-run uncertainty, detailed evaluator agreement, an explicit task split, comprehensive hyperparameters, action-budget settings, and full trajectories. The raw hop count disagreement and conditional Table A1 reconstruction obstruct exact corpus accounting. Several broad claims are stronger than individual table conditions support. Dynamic content, domain imbalance, and automatic hop transitions limit how directly these scores transfer to unrestricted deployment. The evidence measures correctness and completion, not harmful actions, confidentiality breaches, or resistance to manipulated content. These observations are analyst judgments, not admissions attributed to the authors.

## 17. Threats to validity

[D] Internal validity: comparing different model families and input conditions may conflate image handling, reasoning capacity, context length, training, and interface adaptation. Appending histories can change input length as well as memory availability. The source does not describe a controlled factorization separating these effects.

[D] Construct validity: keyword inclusion, semantic answer judgments, and URL/state completion conditions operationalize success. They may not fully capture whether a real user receives a correct, safe, finalized booking or purchase. A URL milestone is not automatically proof that a transaction was completed. The paper's task definitions must determine the intended endpoint; those individual definitions were not supplied.

[D] External and ecological validity: live-site observations improve realism, but the finite reference website list, offline Shopping exception, structured observations, and automatic next-hop movement differ from unconstrained browsing. Travel-heavy composition and tiny shares for recipes, Amazon, and train tasks make broad domain generalization uncertain. Fourteen category entries also do not equal fourteen independent website domains.

[D] Statistical conclusion validity: no uncertainty intervals, tests, or run counts are reported. Small long-task groups and non-monotonic first-hop results weaken a precise monotonic law. Reproducibility: the paper provides a code/data link and API identifiers, but no code or dataset was reviewed here; exact environments and evaluator behavior cannot be reconstructed from the text alone. Security validity: normal task failure is not an attack-success measure, so it cannot establish a vulnerability ordering against standalone LLMs.

## 18. Future work and open questions

### A. Explicit author proposals

[A] The authors propose an action-focused evaluation method to guide agent operations more directly. They state that the environment can support additional websites and that memory augmentation is designed to adapt to other LLMs/LMMs. These are future directions or portability intentions; the supplied experiment does not demonstrate them for all backbones. [pp. 4, 8–9, 12]

### B. Analyst open questions

[D] Which failure modes remain after controlling first-hop semantics, model identity, input length, and domain? How reliable are keyword and language-model evaluators against human task judgments? What fraction of improvement comes from relevant reusable strategy rather than extra examples or ordering effects? Can the dataset's total hops and table denominators be reconciled? Does retrieval of similar trajectories outperform simply appending the most recent K tasks? How do results change when agents choose their own cross-site transitions?

[D] For the security question, open investigations include whether encountered webpage text or images can redirect action selection, whether incorrect or manipulated content persists through memory replay, and whether action permissions constrain resulting harm. A direct comparison would need matched models, adversarial conditions, defined trust boundaries, and security outcomes for both web agents and standalone LLMs. Those studies are not supplied; no results are invented for them.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning and source qualification |
|---|---|
| MMInA | Name of the supplied Multihop Multimodal Internet Agents benchmark |
| LLM | Large language model; language-processing reasoning backbone |
| LMM | Large multimodal model; model that can process images and text |
| Agent | Model coupled to observations, action selection, and environment execution |
| Hop | A website-specific subtask; several interface actions may occur within it |
| Multihop task | Ordered task with multiple required website subtasks |
| Multimodal | Uses more than one input modality, here principally text and images |
| Accessibility tree | Structured webpage nodes containing IDs, types, and text |
| Caption augmentation | Adding generated image descriptions to text input |
| Trajectory | Recorded sequence of task observations and actions |
| Semantic memory | General knowledge, typically associated with model weights |
| Episodic memory | Temporary action history for ongoing tasks |
| Procedural memory | Reusable completed sequences and outcomes |
| must_include | Evaluator requiring every specified keyword |
| fuzzy_match | Language-model semantic judgment against a reference |
| Hop success rate | Percentage of successful targeted website visits |
| Task success rate | Percentage of fully completed tasks |
| H.C.; SR | Table 3 hop count; success rate |
| S; A; P; R | State, action set, transition representation, hop reward in §3.1 |
| Ω; o_t; a_t | Partial observation space; observation and action at time t |
| N | Hop count in the completion queue; separately undefined loss summation limit |
| K | Number of recent task trajectories appended as memory |
| I; M; R | Instruction, multimodal input, reference response in Appendix C |
| A = f(I,M;θ) | Generic predicted-answer mapping; A differs from §3.1 action-set notation |
| θ | Likely model parameters; immediate source definition not explicit |
| MC/MCQ | Restricted multiple-choice representation in related-work discussion; table abbreviation not independently defined |
| VWA | VisualWebArena, as used in the paper's comparison |
| VQA | Visual Question Answering in Appendix C background |
| GUI | Graphical User Interface |
| HTML | Webpage representation referred to by the authors; expanded technical definition not needed for the method |
| API | Application Programming Interface; hosted model access in the reported setup |
| EOS | End-of-output token marker in the instruction-tuning discussion |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Tasks | 1,050 | tasks | Full stated benchmark | Author-reported | pp. 1–2, 13 |
| Website entries | 14 | categories/entries | Benchmark list | Author-reported | pp. 2, 14 |
| Maximum task length | 10 | hops | Benchmark | Author-reported | p. 2, F1 |
| Average task length | 2.85 | hops/task | Rounded corpus mean | Author-reported | p. 2, F1 |
| Average actions | 12.9 | actions/task | Benchmark | Author-reported | pp. 2–3 |
| Hop total in prose | 2,989 | hops | Dataset construction | Author-reported | p. 4, §3.2 |
| Hop total in figure | 2,991 | hops | Figure 2a label | Visually readable | p. 4, F2a |
| Action intent | 64.7 | % of hops | Figure 2b | Visually readable | p. 4 |
| Information-seeking intent | 35.3 | % of hops | Figure 2b | Visually readable | p. 4 |
| Human overall task success | 96.25 | % | Original webpage | Visually readable | p. 7, T2 |
| GPT-4V overall task success | 21.77 | % | Multimodal, no history | Visually readable | p. 7, T2 |
| Human–GPT-4V task gap | 74.48 | percentage points | 96.25 − 21.77 | Analyst-derived | p. 7, T2 |
| Captioned DeepSeek overall T | 23.07 | % | Caption-augmented text | Visually readable | p. 7, T2 |
| Captioned DeepSeek one-hop T | 47.68 | % | Same condition | Visually readable | p. 7, T2 |
| Captioned DeepSeek multihop T | 0; 0 | % | 2–4; 5+ hops | Visually readable | p. 7, T2 |
| GPT-4V one-hop T | 42.91 | % | No history | Visually readable | p. 7, T2 |
| GPT-4V multihop T | 3.03; 0 | % | 2–4; 5+ hops | Visually readable | p. 7, T2 |
| Gemini vision overall T | 18.40 → 20.13 | % | Without → with history | Visually readable | p. 7, T2 |
| Gemini vision overall gain | 1.73 | percentage points | 20.13 − 18.40 | Analyst-derived | p. 7, T2 |
| Gemini vision 2–4-hop gain | 9.10 | percentage points | 10.61 − 1.51 | Analyst-derived | p. 7, T2 |
| GPT-4o overall gain | 2.43 | percentage points | 14.04 − 11.61 | Analyst-derived | p. 7, T2 |
| Usually preferred memory length | 2 | prior tasks | Gemini-Pro-Vision ablation | Author-reported | p. 12 |
| Annotators | 3 | people | Dataset construction | Author-reported | p. 12 |
| Human test takers | average 3 | people | Comparison description | Author-reported | p. 6 |
| Filtered WebQA pairs | 108 | QA pairs | Task sources | Author-reported | p. 13 |
| Summed A1 multihop counts | 520 | tasks | Sum of nine reported rows | Analyst-derived | p. 13, TA1 |
| Local GPU memory | 48 | GB | One RTX6000 Ada | Author-reported | p. 12 |
| Inference epoch duration | 4–8 | hours | Model-dependent benchmark pass | Author-reported | p. 12 |
| Viewport | 1280 × 2048 | dimensions; unit unspecified | Display setting | Author-reported | p. 12 |
| Figure 5 exact bar values | unavailable | performance scale | K-specific bars not labeled | Approximate visual estimate only | p. 8 |

All remaining Table 2 values and Table 3/A1 values are preserved in Sections 11 and 8. Background dataset sizes in Appendix C are compressed in the coverage notes below, rather than confused with MMInA sample sizes.

## 21. Claim–evidence map

| Claim | Evidence | Object / analysis | Source | Qualification / strength |
|---|---|---|---|---|
| MMInA targets visual/text cross-website tasks | Task definitions, chair example, browser workflow | F1; §3 | pp. 1–5 | HIGH for design claim; task files unavailable |
| Benchmark has 1,050 tasks and 14 entries | Repeated corpus description and link table | F1; TA2 | pp. 2, 13–14 | HIGH; not fourteen distinct domains |
| Ordered evaluation tracks partial progress | N + 1 condition queue and hop/task metrics | §3.5; T2 | pp. 5–7 | HIGH; some aggregation details unresolved |
| Complete multihop tasks are difficult for agents | Low 2–4/5+ task scores | X1; T2 | p. 7 | HIGH within listed conditions |
| Humans strongly outperform GPT-4V | 96.25% versus 21.77% overall T | X1; T2 | p. 7 | HIGH values; no uncertainty intervals |
| Captioning is not uniformly beneficial | Gemini/GPT-4 2–4-hop comparisons | X1; T2 | pp. 6–7 | HIGH numerical support; causality limited |
| Agents often fail early | Position scores mostly collapse after early hops | X2; T3/TA1 | pp. 8, 13 | HIGH; not a strict monotonic law |
| Histories improve selected scores | Gemini/GPT-4o history rows; K ablation | X3; T2/F5 | pp. 7–8, 12 | HIGH for scores; MEDIUM for generalization |
| Larger histories can be harmful | Author discussion and non-monotonic bars | X3; F5 | pp. 8, 12 | MEDIUM; exact K bars unlabeled |
| Entirely live-web characterization has exceptions | Offline Shopping and retrieval limitation | §6; TA2 | pp. 9, 14 | HIGH |
| Web-agent architecture is relevant to security exposure | Website observations influence executable actions | §3.1; F4 | pp. 3, 8 | MEDIUM analyst inference; no attack tested |
| Increased vulnerability versus standalone LLMs is unproven here | Evaluation scope concerns task success, not adversarial harm | X1–X3 | pp. 5–8 | HIGH scope observation; vulnerability magnitude UNKNOWN |

Source-grounded verification compared the main synthesis against the supplied text and visually readable tables. Model, modality, hop group, metric, and percentage units were kept distinct. Rounded introduction values were checked against Table 2. Figure trends were kept qualitative when no exact labels were supplied. Conflicting counts and incompletely specified denominators were retained as unresolved rather than replaced with inferred corrections.

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an assistant to plan a trip. It first needs to find the right city, then search for flights, choose a hotel, and find useful videos. Each part happens on a website, and mistakes in an early part can prevent everything afterward. MMInA tests this kind of connected work, including cases where the assistant must look at pictures rather than only read words.

The researchers found that the tested AI assistants often managed a simple part but struggled to finish the entire sequence. Humans completed about 96% of tasks overall. One tested GPT-4V setup completed about 22%. Remembering earlier task attempts helped some scores, but adding more memories was not always better, and long tasks remained difficult.

For a security project, this helps identify places worth investigating: website content goes into an assistant's decisions, those decisions can become browser actions, and past content can appear again through memory. But the paper did not plant malicious instructions or compare attack rates with an ordinary chatbot. It shows task difficulty and a browser-agent design; it does not prove that web agents are more vulnerable to attackers.

## Completeness Audit

Coverage is judged against the inventory of the supplied document, not response length. The accessible text was inspected for all sixteen physical pages. Visual coverage is limited to the eleven supplied rendered pages. All numbered figures and tables were visually inspected at the available resolution; their tiny embedded screenshots were only partially readable.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| S0 title/authors/abstract | Yes | Yes | Fully represented substantively | Shulin Tian, Ziniu Zhang, Liangyu Chen, Ziwei Liu; S-Lab, Nanyang Technological University; Findings of ACL 2025, pp. 13682–13697; first three equal contribution, Chen project lead, Liu correspondence |
| S1 introduction and contributions | Yes | Yes | Represented in compressed form | Motivation and all three contribution categories retained |
| S2 related works: both subsections | Yes | Yes | Represented in compressed form | Tool benchmarks, generalist benchmarks, web-agent positioning; no independent citation validation |
| S3.1 environment/action/observation | Yes | Yes | Fully represented substantively | Twelve actions reported, complete list absent |
| S3.2 construction/data/annotation/metrics | Yes | Yes | Fully represented substantively | Assisted generation, templates, shortest paths, count conflict retained |
| S3.3 multimodal content | Yes | Yes | Fully represented substantively | Chair comparison and extraction method |
| S3.4 cross-website browsing | Yes | Yes | Fully represented substantively | Automatic transitions and reference links |
| S3.5 both evaluators | Yes | Yes | Fully represented substantively | Keywords, semantic judge, queue, sequence gate |
| S4.1 baselines | Text only | Yes | Fully represented substantively | Group-enumeration inconsistency noted |
| S4.2 main results | Yes | Yes | Fully represented substantively | Complete T2 numerical transcription |
| S4.3 search space/input length | Yes | Yes | Fully represented substantively | Attribution distinguished from causal proof |
| S4.4 memory types | Yes | Yes | Fully represented substantively | Conceptual architecture and prompt intervention |
| S5 conclusion/future work | Yes; p. 9 text only | Yes | Fully represented substantively | Action-focused future evaluation |
| S6 limitations | Text only | Yes | Fully represented | Image access and website exceptions |
| S7 ethics | Text only | Yes | Fully represented | Base-model bias warning |
| REF bibliography | Yes; partial images | Yes | Inspected but deliberately compressed | Bibliographic entries not individually reproduced or validated |
| Appendix A.1 settings | Yes | Yes | Fully represented substantively | Viewport, model IDs, default parameters, WebShop adaptation |
| Appendix A.2 resources | Yes | Yes | Fully represented | GPU and epoch runtime |
| Appendix A.3 hop analysis | Yes | Yes | Fully represented substantively | Long-hop fluctuation caveat and TA1 |
| Appendix A.3 memory ablation | Yes | Yes | Fully represented substantively | K, Gemini model, input-length and bias caveats |
| Appendix B.1.1 annotators | Yes | Yes | Fully represented | Three trained annotators and cross-validation |
| Appendix B.1.2 protocol | Yes | Yes | Fully represented | Extra website visits allowed |
| Appendix B.1.3 statistics | Yes | Yes | Fully represented substantively | Travel composition and four/five-hop exception |
| Appendix B.2.1 links | Yes | Yes | Represented in compressed form | All fourteen entries; long URL path shortened in prose |
| Appendix B.2.2 comparison | Yes | Yes | Fully represented substantively | TA3 examples and bounded interpretation |
| Appendix C datasets | Yes | Yes | Represented in compressed form | CLIP, DALL-E, Stable Diffusion, Flamingo, GPT and dataset background; ancillary sizes below |
| Appendix C backbones | Yes | Yes | Represented in compressed form | Instruction tuning, transformation, Self-Instruct, two equations |
| Appendix C web agents | Text only on p. 15 | Yes | Represented in compressed form | TravelPlanner, OmniACT, WEBLINX, DUAL-VCR background |
| Appendix C mobile agents | Text only pp. 15–16 | Yes | Represented in compressed form | ERICA, PIXEL, Pix2Struct, PTP, AppAgent, Mobile-Agent, SeeClick |
| Appendix C.1 other benchmarks | Text only | Yes | Represented in compressed form | Repeated benchmark positioning; overbroad single-site statement qualified |
| Research questions/objectives | Yes | Yes | Fully represented | Informal questions distinguished from formal RQs |
| Formal hypotheses | No item present | Yes | Not present in supplied material | Not manufactured |
| X1 baseline evaluation | Yes | Yes | Fully represented substantively | T2 and conditions |
| X2 hop-position analysis | Yes | Yes | Fully represented substantively | T3 and TA1 |
| X3 memory ablation | Yes | Yes | Fully represented substantively | F5 exact bars uncertain |
| X4 descriptive analysis | Yes | Yes | Fully represented substantively | F2/F3 and caveats |
| F1 | Yes | Yes | Fully represented at readable resolution | Small screenshot text partial |
| F2a/F2b/F2c | Yes | Yes | Fully represented substantively | All shares; axis conflict flagged |
| F3 | Yes | Yes | Represented in compressed form | Exact heights not labeled |
| F4 | Yes | Yes | Fully represented substantively | Arrows and memory roles |
| F5 | Yes | Yes | Represented in compressed form | Qualitative K pattern; metric subtype uncertain |
| T1 | Yes | Yes | Fully represented | All benchmark characteristic rows |
| T2 | Yes | Yes | Fully represented | All displayed score cells |
| T3a/T3b | Yes | Yes | Fully represented | All applicable values; dashes distinguished |
| TA1 | Yes | Yes | Fully represented | Counts and every nonzero value; zeros grouped |
| TA2 | Yes | Yes | Represented in compressed form | All entries and Kiwix footnote |
| TA3 | Yes | Yes | Fully represented substantively | Tiny screenshot content partial |
| E.POMDP/E.QUEUE/E.PRED | Yes | Yes | Fully represented | Symbol reuse and definition gaps flagged |
| E.LOSS | Text only | Yes | Uncertain | Corrupted extraction; no rendered p. 15 |
| Algorithms/theorems | No item present | Yes | Not present in supplied material | No numbered pseudocode or proof |
| Major contributions | Yes | Yes | Fully represented | Benchmark, evaluation, memory, empirical results |
| Author limitations/caveats | Yes | Yes | Fully represented substantively | Includes appendix and ethical cautions |
| Separate supplements/repository | No | Yes as absence | Missing from supplied material | No separate artifact inspected |

### Missing or inaccessible material

No supplied physical text page is missing. Rendered images for pages 6, 9, 11, 15, and 16 are absent. Original task JSONs, repository code, full annotations, actual browser trajectories, raw experiment logs, and any separate supplement were not supplied. Tiny interface text in embedded screenshots is not fully readable. The complete twelve-action enumeration and several reproduction settings are not specified by the supplied paper. Absence of those details is not repaired through browsing.

### Uncertain interpretations

Unresolved issues include 2,989 versus 2,991 total hops; the conditional 2,924-hop reconstruction from Table A1 counts; compatibility of hop-position tables with aggregate task success; Figure 2c's incorrect-looking vertical label; Figure 5's exact values and metric subtype; loss-equation typography and omitted/undefined symbols; the exact mapping of the limitation's open-source website; and the interpretation of broadly stated superiority claims across differing input conditions. The long-hop tables do not establish a monotonic first-hop decline. Security vulnerability magnitude and any comparison against standalone chat-only LLMs remain UNKNOWN.

### Deliberately compressed material

Bibliographic metadata and repetitive related-work descriptions are compressed rather than reproduced entry by entry. Appendix C's ancillary numerical background is accounted for here: WebShop is described as containing 1.18 million products and 12,087 instructions; LAION-5B as 5.85 billion pairs, including 2.32 billion English pairs; MIMIC-IT as 2.8 million instruction-response pairs with 2.2 million unique instructions; TravelPlanner as nearly four million records and 1,225 planning intents. These are author descriptions of cited resources, not MMInA data or independently checked external facts. DataComp's four stages—scale choice, dataset creation/filtering or Bring Your Own Data, fixed-architecture training, and downstream assessment—are compressed as background. Transformation and Self-Instruct describe enriching or generating instruction data; they are not presented as MMInA training experiments. Expanded web/mobile examples are grouped by their roles in representations, grounding, planning, and interaction. Logos, decorative screenshot detail, page headers, and repetitive zero cells are compressed with this disclosure.

### Potential omissions

Every substantive inventoried section, subsection, experiment, numbered visual, table, central equation, contribution, and identifiable author caveat is represented or explicitly qualified above. No separate supplement has been silently counted as reviewed. The report cannot establish exhaustive understanding of unreadable screenshot details, original datasets, repository behavior, or an unprovided rendered equation. It therefore provides an inventory-based representation of the supplied evidence, not a claim of complete reproduction or complete security analysis.
