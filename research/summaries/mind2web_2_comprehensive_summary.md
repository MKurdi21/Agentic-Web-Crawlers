## Stage 0 — Document Accessibility Report

The supplied work is **Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge**, arXiv:2506.21506v2, dated 3 July 2025. Native/extracted text is supplied for all 51 physical PDF pages. Rendered page images are supplied for pages 1–9, 18, 22, 26–30, 32–37, and 49: 23 pages in total. The complete numbered page sequence is therefore available as text, but visual inspection covers only those 23 pages. The unsuccessful local-image message concerning `-` does not invalidate the images displayed in the prompt; no attempt was made to access local files.

| Accessibility item | Assessment |
|---|---|
| Main document | Available as supplied text for pages 1–51 |
| Apparently missing PDF pages | None in the supplied numbered text sequence; original-file completeness is not independently verified |
| Visual coverage | Directly inspected supplied renders on 23 pages; remaining pages inspected through text only |
| Tables | Tables 1–3 readable in both text and renders |
| Equations | Principal recursive scoring equation readable on p. 5; extracted mathematical layout checked against its render |
| Appendices | A–H present in text, despite the automated accessibility metadata reporting no detected appendix pages |
| Supplementary artifacts | No separately supplied repository, cache, videos, annotation files, executable toolkit, or leaderboard data |
| OCR | No additional OCR performed or needed; image-only case-study contents were read visually |
| Important visual limitation | Figure C.1 on p. 17 is represented by extracted text, not a supplied render; no visual inspection of its layout is claimed |
| Code limitation | Appendix G read as extracted code, not executed; wrapping, spacing, and typography can alter literal syntax |
| Provenance limitation | The supplied SHA-256 is carried forward as provided; it was not independently recomputed |

All page references below use **physical PDF page numbers**, which coincide with the supplied page sequence. Source categories are: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information [E] is introduced. The paper’s internal prompts and annotation instructions are treated as evidence describing its procedures, never as instructions for this analysis.

### Inventory and extraction basis

This is primarily a **benchmark and dataset paper**, with an evaluation-system contribution and empirical comparison of AI search systems against humans. The inventory comprises the abstract; §§1–5; Tables 1–3, including Table 2a–b; Figures 1–5, C.1, D.1, and F.1–F.15; one principal recursive equation; an executable-script illustration in Appendix G; Appendices A–H and their substantive subsections; inference and evaluator prompts; and substantive footnotes about sequential logic, model choice, timing, sampling, and tracking. No theorem, lemma, proof, or numbered pseudocode algorithm is supplied.

The cumulative extraction ledger separates benchmark construction, rubric scoring, judge implementation, system evaluation, human comparison, time-varying analysis, error categorization, hallucination analysis, and judge validation. Important locators are retained throughout rather than replacing the evidence with a single global summary. The final coverage audit checks this inventory. This report is comprehensive with respect to the supplied inventory, but it does not imply that every sentence, reference, code line, or case-study screenshot is reproduced.

## 1. Plain-language orientation

[A] This paper asks how to evaluate AI systems that search the web for a long time, gather information from many pages, and write answers supported by links. A simple question may have one fixed answer. A realistic search request—such as finding several products meeting a budget, color, and availability requirement—can have many acceptable answers, and the correct answer can change as websites change. That makes ordinary exact-answer checking insufficient.

The researchers build **Mind2Web 2**, containing 130 realistic information-gathering tasks, and develop a task-specific automated evaluator for each. Their **Agent-as-a-Judge** framework breaks the requested answer into a tree of small checks. It verifies both whether the answer satisfies the task and whether cited webpages support its claims. Human labor exceeding 1,000 hours supports task construction and evaluator development (pp. 1–6).

Ten agentic search systems are evaluated. The best system in Table 3, OpenAI Deep Research, obtains partial completion 0.54 and full-task success 0.28, compared with 0.79 and 0.54 for humans on a smaller 30-task subset. Its reported average completion time is 8.40 minutes, versus 18.40 minutes for humans. These results demonstrate promising assistance but substantial remaining reliability failures, not dependable autonomous completion of every task.

[D] For the research question **“Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,”** the paper supplies relevant observations about complex environments, tool failures, source grounding, and unreliable final answers. It does **not** directly test adversarial attacks or compare web agents against standalone, tool-free large language models. Its central contribution is a benchmark and verification methodology, not a causal security explanation of greater vulnerability.

## 2. Document roadmap

[A] The abstract and §1 establish the difficulty of evaluating long-horizon, changing web-search answers. §2 positions agentic search, browser agents, Deep Research systems, and existing evaluation benchmarks. §3 explains benchmark construction: overview (§3.1), task collection (§3.2), rubric trees (§3.3), judge agents (§3.4), and benchmark statistics (§3.5). §4 presents experimental setup (§4.1), main results (§4.2), error analysis (§4.3), and human evaluation of judge agents (§4.4). §5 concludes.

Appendix A states limitations. Appendix B discusses broader impacts and ethical concerns. Appendix C details domain distribution, task principles, collection, and future maintenance. Appendix D explains rubric design, judge tools and prompts, script generation, two-stage validation, and human assessment. Appendix E provides system settings, webpage caching, and human-study procedures. Appendix F defines errors and illustrates them. Appendix G supplies a public-development judge script. Appendix H records instructions used for task collection, human completion, error annotation, and evaluator assessment.

The references occupy pp. 12–14, and an appendix contents page appears on p. 15. These provide traceability but are not independently reviewed as outside literature. The acknowledgment on p. 11 reports assistance from research and product teams, inference-cost support from Hugging Face, and research sponsorship; those disclosures are represented here without inferring an effect on results.

## 3. Background and context

[A] A **large language model (LLM)** is the language-model component used in the systems described. The paper defines **agentic search** as iterative, autonomous handling of complex search tasks using tools such as search application programming interfaces (APIs), retrievers, and browsers (§2, p. 3). The LLM decomposes requests, plans, reasons over accumulated information, and sometimes interacts with live websites.

The authors distinguish search-augmented LLM products, autonomous browser agents, and Deep Research systems. Search-augmented products return quick answers after relatively limited search. Browser agents interact with webpages through actions such as clicking and scrolling. Deep Research systems sustain more extensive information collection and synthesis, sometimes using browsers and coding tools. These are overlapping capability categories rather than a controlled taxonomy of identical architectures.

**Long-horizon** refers to lengthy sequences of actions and information gathering. Table 1 categorizes benchmark horizons as Short below 10 actions, Medium 10–50, and Long above 50. **Time-varying** means that an acceptable answer may change over time, including product prices or date-specific availability. **Correctness** concerns satisfying the requested criteria. **Attribution** concerns whether the claims can be supported by their cited sources.

The guiding idea is **generation–verification asymmetry**: generating a complex answer may be difficult, while individual requirements can be checked more directly. A **rubric** states those checks; a **rubric tree** organizes them hierarchically. **LLM-as-a-Judge** uses language-model judgments. Here, **Agent-as-a-Judge** embeds extraction, judgments, tools, and score aggregation in a task-specific workflow.

The introduction mentions term-frequency/inverse-document-frequency methods, PageRank, and learning to rank as historical search approaches. Their mechanics are not necessary for the contribution and are not supplied in detail. This report does not import external explanations of them.

## 4. Research problem and gap

[A] The existing problem is that agents can produce lengthy, plausible answers after many interactions, while reliable automated evaluation remains difficult. Users may rely on synthesized answers instead of inspecting original sources themselves. Evaluation therefore needs to detect both task failure and unsupported claims (§1, p. 2).

According to the authors, prior browser benchmarks often emphasize short, transactional tasks on one website. Other open-web benchmarks simplify checking by using predefined, time-invariant answers, often one answer string. The authors argue that these designs fail to cover realistic requests with multiple constraints, multiple sources, changing answers, and lengthy synthesis (§§1–2).

The research gap is the joint evaluation of a broad range of agentic search systems on realistic long-horizon tasks with potentially changing answers. The methodological obstacle is verifying open-ended answers without assuming one fixed reference response. The benchmark addresses this by fixing task requirements while allowing answer contents and selected sources to vary.

Scope matters: the paper is about information seeking and final-answer evaluation. It does not evaluate every browser action, purchase execution, credential handling, source truthfulness, malicious websites, or all possible real-world requests. It intentionally restricts tasks to those compatible with practical verification.

## 5. Research questions, objectives, and hypotheses

[A] Section 3.1 explicitly states two construction challenges:

1. How to collect sufficiently complex yet realistic tasks?
2. How to automatically and reliably evaluate the complex answers generated by different agentic search systems?

Other stated objectives are to assess correctness and attribution, compare ten systems and human performance, identify error patterns, and validate judge reliability. These are objectives, not additional formal research questions manufactured by this report.

[A] One explicit empirical hypothesis concerns time variation: systems with no or limited browsing features may perform worse on time-varying tasks than on time-invariant tasks (§4.2, pp. 8–9). The authors identify 57 explicitly time-varying tasks and compare their partial completion with that of other tasks. Most systems show the expected disadvantage, whereas Operator and humans achieve relatively similar or better performance on the time-varying subset.

[D] The user’s security research question is a separate analytical lens. The supplied study can inform hypotheses about exposure and failure mechanisms, but it does not itself ask or experimentally establish why web agents are more vulnerable than standalone LLMs.

## 6. Assumptions / Threat Model

[A] There is no formal adversarial threat model. No attacker capabilities, controlled malicious content, attack budget, security asset, or attack-success metric is specified. Appendix B mentions disinformation and unauthorized data extraction as possible broader harms, not evaluated attacks.

The evaluation makes several explicit assumptions. Cited uniform resource locators (URLs) are presumed to provide truthful and credible information; assessing source credibility is outside scope (Appendix A, p. 16). Key attribution checks must be decomposable into independent verification against individual webpages. At least one valid supporting source suffices in the conflicting-source example discussed on p. 11. Static or initially rendered content must expose the needed evidence; hidden, collapsed, or dynamically loaded evidence can defeat verification.

Task collection excludes login-dependent information, non-English websites, video understanding, extremely rapidly changing answers, and unverifiable global qualifiers. Tasks explicitly demanding complex reasoning or external calculation tools are avoided, although evaluated systems may use any helpful tools. Requests must be sufficiently specified for a single round without user clarification (pp. 18, 45–47).

[D] A security interpretation must separate these assumptions from guarantees. Source support is not equivalent to source truth. A source-backed false statement could fall outside the benchmark’s credibility scope. The evaluator receives agent answers and webpage content through LLM prompts, but the paper does not test adversarial instruction content in those inputs. Potential security consequences therefore remain open questions rather than demonstrated weaknesses.

## 7. Methodology

### Task and dataset construction

[A] Task proposers generate authentic requests or use domain guidelines. Refinement experts revise or filter them for realism, clarity, tediousness, and verifiability. At least two independent validators must successfully validate each included task, including end-to-end completion and inspection for ambiguities or incompatible source checks (§3.2; Appendix C.3).

The resulting 130 tasks cover six broad domains and 24 subdomains. Broad counts are Lifestyle & Leisure 34, Entertainment 28, Miscellaneous 25, Science & Research 23, Career & Education 11, and Travel & Transportation 9 (p. 17). Proposed domains derive from prior work and expansion using GPT-4o, then are reviewed and consolidated by annotators. This use of GPT-4o concerns taxonomy development, not the main evaluator model.

The benchmark is split into 10 public development tasks, including evaluation scripts, and 120 private test tasks with task descriptions available but private rubrics/scripts. Test answers are submitted for evaluation. The authors keep the script-generation pipeline hidden to reduce contamination, reward-model abuse, and benchmark overfitting (pp. 6–7, 17). No model-training split is described; this is an evaluation benchmark.

### Rubric structure and metrics

[A] A leaf node returns binary success or failure. Critical children gate their parent: failure forces the parent score to zero. Non-critical children permit partial credit through averaging. Sequential nodes model logical dependence, so a failed earlier stage can block later stages. Expected attribution checks must be critical when practical URL support is reasonable (pp. 5, 19).

Partial Completion averages root scores over tasks. Success Rate measures the fraction of tasks with root score exactly 1. Pass@3 measures whether at least one of three attempts succeeds. These metrics capture different properties: partial useful progress, complete success in one attempt, and success available across repeated attempts.

### Judge implementation and development

[A] Each task has a Python judge script. An **Extractor** parses structured answer information such as prices, names, and URLs. A **Verifier** checks simple statements or source support using webpage text and screenshots. Both use OpenAI o4-mini (p. 5). A reusable toolkit provides rubric structures, aggregation, extraction, verification, and auxiliary functions.

Claude-3.7-Sonnet generates initial scripts from task descriptions, design rules, toolkit details, and examples of errors. Runtime self-debugging executes extraction using an OpenAI Deep Research answer while temporarily returning True for verification, then feeds runtime errors back for correction. This phase checks execution problems, not factual evaluation correctness. Self-reflection separately reviews logic, completeness, and edge cases (pp. 21–22).

Human validation first inspects scripts, prompts, and scoring. It then tests one answer from each of six randomly chosen systems per task, repairing critical errors and omissions while avoiding overfitting to individual answers. Remaining answers are held out for generalization assessment. A graphical user interface (GUI) helps inspect answers, cached pages, rubrics, and outcomes (pp. 22–23).

### Source capture and system settings

[A] Cited URLs are aggregated and unique pages cached with Playwright, including text, screenshots, and PDF handling. Manual intervention retrieves pages blocked to automation and replaces incorrect caches. The stated purpose is stable, efficient verification against source state near answer generation (p. 24). Exact capture delays are not specified.

System answers were collected April–June 2025. Systems are run three times per task. All except Hugging Face Open Deep Research are accessed through web user interfaces and manually collected; that open-source system uses OpenAI o3 as its base model. Most receive a unified prompt demanding actual search and source support. Operator and Gemini receive additional attribution emphasis (pp. 23–24).

Hardware, library versions, random seeds, token budgets, detailed proprietary architectures, and precise inference costs are not provided. Completion time is self-reported when available, otherwise measured manually only on Subset-30. Reported uncertainty in Table 3 is standard deviation, not a confidence interval or significance test.

## 8. Experiments / Analyses

| ID | Purpose and setup | Evidence and conditions |
|---|---|---|
| X1 Main system comparison | Ten systems, 120 private tasks, three independent attempts per task | Table 3; Partial Completion, Success Rate, Pass@3, time, answer length |
| X2 Human reference | Seven qualified completers; 30 randomly selected private tasks; three people per task | Tables 2b–3; browser-only study with source requirements and stopping rules |
| X3 Time and repeated attempts | Compare observed time/performance and single-attempt versus Pass@3 results | Fig. 3 and Table 3; observational comparisons, no controlled compute intervention |
| X4 Time-varying tasks | Compare 57 explicitly time-varying tasks with remaining tasks | Fig. 4; author hypothesis about limited live browsing |
| X5 Error taxonomy | One randomly selected answer per task/system on Subset-30; five representative agents plus humans | Fig. 5, Appendix F; multiple errors may occur in one answer |
| X6 Hallucination analysis | Union of Invalid Attribution and Unsupported Answer | Appendix F.2; 23% for OpenAI Deep Research, at least 50% for other analyzed agent systems |
| X7 Judge validation | One independent evaluator, 15 sampled tasks, two held-out answers per task; trivial total failures excluded | §§4.4, D.5, H.4; 720 leaf checks and adjudicated discrepancies |

[A] Human completers first pass two simplified trial tasks. They have no prior knowledge of assigned tasks and cannot be creators or reviewers. They use a clean browser, do not use AI tools, provide links, record their process, and log time/pages through a Chrome extension. They should not abandon a task before 30 minutes without a clear path; after more than one hour they may stop even with a known path (pp. 25, 47–48).

[C] The design implies 90 human task attempts: 30 tasks × 3 completers. It also implies 360 attempts per agent on the private test set: 120 × 3, or 3,600 across ten agents. These are design-derived counts, not separately reported totals of successful records.

[A] Judge assessment first evaluates rubric validity using Strongly Agree, Agree with Reservations, and Disagree. The evaluator then assigns binary leaf judgments without viewing automated scores. A developer reviews mismatches with the evaluator. Short-circuit evaluation is disabled for this assessment so all nodes are checked (pp. 10–11, 19, 50–51).

## 9. Results

[A] OpenAI Deep Research leads the evaluated systems in mean partial completion (0.54) and success rate (0.28). Grok DeeperSearch follows at 0.52 and 0.27. Both achieve Pass@3 of 0.40. Humans achieve 0.79 partial completion, 0.54 success, and 0.83 Pass@3 on Subset-30. The human and agent rows are not based on identical full task sets (Table 3, p. 7).

ChatGPT Search and Perplexity Pro Search return answers in under one minute but achieve partial completion 0.26 and 0.28. Operator obtains 0.26 partial completion and 0.10 success despite 9.74 minutes average time. Hugging Face Open Deep Research also scores 0.26 partial completion; its 13.65-minute time exceeds that of all other agent rows. These observations show that time alone does not determine performance.

[C] Using reported means, OpenAI Deep Research reaches 0.54/0.79 = approximately 68.35% of human partial completion and 0.28/0.54 = approximately 51.85% of human success. Its time ratio is 8.40/18.40 = approximately 45.65%. These calculations explain the authors’ 50–70% performance and less-than-half-time wording, while preserving the subset mismatch and mixed timing procedures.

[C] The success-rate difference from humans is 0.54 − 0.28 = 0.26, or **26 percentage points**. The partial-completion difference is 0.79 − 0.54 = 0.25 score units. The nominal difference between OpenAI Deep Research and Grok DeeperSearch is only 0.02 partial-completion units and one percentage point of success; no significance test establishes a reliable ordering beyond the reported means.

[A] Most systems perform worse on explicitly time-varying tasks. The authors relate this to insufficient live interaction, but Figure 4 does not isolate browsing as a manipulated variable. Longer reports do not necessarily achieve better task completion: Gemini averages 3,357 words, versus OpenAI Deep Research’s 559, while obtaining lower scores (pp. 7–9).

[A] Judge validation identifies 35 disagreements in 720 verifications. Adjudication attributes 27 to human mistakes, three to strict or lenient Verifier judgments, four to hidden webpage evidence, and one to conflicting sources. Excluding human mistakes and the source-conflict case leaves seven actual errors and the reported 99.03% correctness (pp. 10–11). That is agreement/accuracy under the benchmark’s assumptions, not universal factual truth or adversarial robustness.

## 10. Figure-by-figure interpretation

### Figure 1 — Benchmark and evaluation overview, p. 1

[B] The diagram connects a realistic shopping request, a citation-bearing answer, diverse task domains, and a judge tree. The example requests five white IKEA furniture items within a $200–$600 budget. The answer includes a black desk, illustrating why a plausible list can fail constraints. Source checks include retailer, color, and price. The displayed evaluation is Failure with Partial Completion 0.4. Domain shares shown are 26%, 22%, 18%, 8%, 7%, and 19%; these are rounded overview percentages, not additional exact task counts. Small thumbnails depict sources and evaluation, not independently verified product facts.

### Figure 2 — Rubric decomposition and score propagation, p. 5

[B] The left panel decomposes the task downward and propagates binary outcomes upward. Critical nodes are visually marked with blue outlines. The root example is 0.6. The right panel expands wardrobe qualification into four checks: IKEA origin, price accuracy, white color, and two doors. A budget check uses simple verification, while source-dependent criteria use URL verification. There are no quantitative plot axes. The figure demonstrates gating and averaging rather than a performance experiment.

### Figure 3 — Completion against time, p. 8

[B] This scatterplot has linear time in minutes on the horizontal axis, approximately 0–20, and Partial Completion on the vertical axis, 0–0.9. Labeled points show system and human means; no error bars are displayed. Human performance lies above all agent points and farther right. OpenAI Deep Research and Grok DeeperSearch offer high agent completion at substantially lower times. Hugging Face’s slower, low-scoring point shows that greater elapsed time is not sufficient. Exact means are taken from Table 3, not estimated from positions. [D] The plot supports an efficiency comparison but cannot establish a causal scaling law across differing systems.

### Figure 4 — Explicit time variation, p. 8

[B] The horizontal axis lists systems and humans; the vertical axis is Partial Completion from 0 to 1. A pink solid line represents explicitly time-varying tasks, and a green dashed line with markers represents other tasks. Most pink points lie below green points. Operator and humans are the principal exceptions discussed by the authors. No exact per-system values or error bars are printed. Therefore this report retains directional comparisons without manufacturing numerical values from the chart. The lines connect categories; they are not a continuous experimental trajectory.

### Figure 5 — Error frequencies, p. 9

[B] This grouped bar chart uses seven error categories horizontally and Task Percentage vertically, with ticks through 60. Its six colored series are five agent systems and humans. Operator has a prominent invalid-attribution bar, Hugging Face a prominent criteria-violation bar, and humans also show substantial criteria violation. Exact bar values are not labeled and are not reported here as precise percentages. Categories overlap, so bars must not be summed into a total error rate. The figure concerns Subset-30, not all private tasks.

### Figure C.1 — Domain distribution, p. 17

[A] Text-only inspection identifies six broad domains, 24 subdomains, and their counts. Lifestyle includes shopping 10, food/cooking 6, sports/fitness 6, health/medicine 4, pets/animal welfare 4, fashion/beauty 3, and hobbies/DIY 1. Entertainment includes films/TV 12, gaming 8, live shows 4, music 2, and books 2. Miscellaneous includes general information 13, news 4, legal/government services 3, real estate 3, and finance/investment 2. Science/research contains academia 14 and technology/science 9; career/education contains education 6 and jobs 5; travel contains accommodation 7, outdoor recreation 1, and ticketed activities 1. Layout and colors are not visually audited.

### Figure D.1 — Validation interface, p. 22

[B] The screenshot places task and answer text on the left, a cached webpage in the center, and rubric/evaluation details on the right. It shows how annotators can inspect a claim alongside its source and scoring structure. Fine interface text is secondary and partly too small for confident transcription. The screenshot establishes interface organization, not an independent measure of evaluator reliability.

### Figure F.1 — Error categorization workflow, p. 26

[B] The diagram branches from Error Analysis into Correctness Check and Attribution Check. Correctness divides into completeness and criteria checks; incompleteness splits into Information Not Found and Partial Missing. Attribution distinguishes supported answers, invalid attribution, missing attribution, and unsupported answers. Unsupported answers undergo a source-link check separating Synthesis Error from Retrieval Error. Arrows describe an annotation decision procedure, not the automated scoring equation.

### Figures F.2–F.8 — Canonical error examples, pp. 27–30

[B] F.2 shows Perplexity unable to retrieve annual Mazda3 production information for 2012–2023. F.3 shows ChatGPT covering only 2004–2014 when Nobel Physics information was requested for 2004–2024. F.4 shows Operator giving a $1,277.97 shopping list under a $200–$600 budget. F.5 shows fabricated Federal Reserve/Reuters-style links accompanying an invented speech response. F.6 shows birthplace claims without supporting sources, even though other Nobel-related information has a link. F.7 shows a source about team-up abilities failing to support a complete Marvel Rivals ability list. F.8 shows paper metadata incorrectly synthesized despite relevant PDF links, including author/affiliation and submission-date errors. These panels are directly inspected examples, not new external facts about the named entities.

### Figures F.9–F.10 — Human mistakes, p. 32

[B] F.9 illustrates a human including a University of Waterloo dataset under a U.S.-institution constraint. F.10 illustrates a human misspelling the identified Pritzker winner’s name while having consulted the relevant source. The authors use them to argue that tedious work creates human carelessness. The examples do not establish general human inferiority or a population-wide rate of such mistakes.

### Figure F.11 — Tool invocation failure, p. 33

[B] A Hugging Face trajectory says no internet-enabled search tool is available and ends with an inability to complete the task. A tool response reports code-parsing failure. The explanatory panel attributes the failure to incorrect handling of tools and the required output format. The exact regular-expression syntax is too small and typography-sensitive to transcribe confidently. The evidence supports a tool-interface failure case, not malicious interference.

### Figure F.12 — Correct navigation, incorrect final URL, p. 34

[B] Operator supplies fellowship information and a broken source URL. The panel states that it had visited the correct official page but later reported a URL differing by a few words. This separates retrieval success from final-answer provenance failure. It is particularly relevant to the authors’ discussion of long-context grounding and source memory.

### Figure F.13 — Correct-looking claim without attribution, p. 35

[B] OpenAI Deep Research identifies the requested film and actor connection but does not support the actor claim with verifiable attribution. The caption cautiously says it likely resulted from direct generation rather than real-time searching. This report preserves that uncertainty; the panel does not prove the model’s internal information source.

### Figure F.14 — Discoverable connection missed, p. 36

[B] Perplexity reports no qualifying connection between Chris Evans and a U.S. president born before 1920 within three degrees. The authors state a valid connection exists and is discoverable by humans and more capable systems. The complete positive connection chain is not shown here, so the report does not reconstruct it.

### Figure F.15 — Relevant retrieval, mismatched attribution, p. 37

[B] ChatGPT’s Nobel information cites sources concerning other years or laureates. The panel includes relevant-looking pages but explains that they do not substantiate the particular claims. It illustrates that finding some relevant sources is insufficient without accurate claim-to-source mapping. No axes or statistical uncertainty apply to these case-study panels.

## 11. Table-by-table interpretation

### Table 1 — Existing benchmark comparison, p. 6

[A/B] Rows compare benchmark task count, horizon class, time variation, and evaluation style. Online-Mind2Web has 300 tasks; WebVoyager 643; Mind2Web-Live 542; BEARCUBS 111; WebWalkerQA 680; GAIA 466; AssistantBench 214; BrowseComp 1,266; Mind2Web 2 130. The first five rows are Short, GAIA and AssistantBench Medium, and BrowseComp/Mind2Web 2 Long. Time variation is marked for Online-Mind2Web, WebVoyager, Mind2Web-Live, and Mind2Web 2. Evaluation varies among LLM judging, rules, manual evaluation, answer matching, and Agent-as-a-Judge. The table supports the authors’ positioning within this selected comparison; it is not an independently verified exhaustive survey.

### Table 2 — Rubric complexity and human effort, p. 6

[A/B] Table 2a reports average/minimum/maximum leaf counts 34/3/357, total-node counts 50/4/603, and depth 4/2/6. Table 2b reports time 18/8/44 minutes, websites 8/3/31, and webpages 110/38/375 on Subset-30. These quantities show both evaluation granularity and substantial browsing effort. The maximum recorded time is 44 minutes; the prose’s up-to-one-hour wording describes study stopping allowance rather than that exact observed maximum. The authors say observed effort underestimates complete effort because people may omit steps, err, or stop.

### Table 3 — Full system results, p. 7

| System | Partial Completion | Success Rate | Pass@3 | Time, minutes | Answer words |
|---|---:|---:|---:|---:|---:|
| ChatGPT Search | 0.26 ± 0.01 | 0.06 ± 0.01 | 0.11 | <1 | 314 ± 4 |
| Perplexity Pro Search | 0.28 ± 0.02 | 0.08 ± 0.01 | 0.12 | <1 | 408 ± 13 |
| OpenAI Operator | 0.26 ± 0.01 | 0.10 ± 0.01 | 0.17 | 9.74 ± 0.21 | 160 ± 1 |
| HF Open Deep Research | 0.26 ± 0.01 | 0.11 ± 0.01 | 0.18 | 13.65 ± 0.07 | 209 ± 3 |
| Claude Research | 0.32 ± 0.03 | 0.10 ± 0.03 | 0.19 | 7.39 ± 0.14 | 742 ± 1 |
| Grok DeepSearch | 0.40 ± 0.04 | 0.18 ± 0.02 | 0.36 | 2.58 ± 0.14 | 1,428 ± 16 |
| Perplexity Deep Research | 0.42 ± 0.03 | 0.15 ± 0.03 | 0.26 | 5.67 ± 0.13 | 585 ± 13 |
| Gemini Deep Research | 0.45 ± 0.03 | 0.18 ± 0.02 | 0.30 | 7.38 ± 0.58 | 3,357 ± 49 |
| Grok DeeperSearch | 0.52 ± 0.02 | 0.27 ± 0.03 | 0.40 | 5.72 ± 0.27 | 1,362 ± 24 |
| OpenAI Deep Research | 0.54 ± 0.04 | 0.28 ± 0.04 | 0.40 | 8.40 ± 0.71 | 559 ± 19 |
| Human, Subset-30 | 0.79 ± 0.01 | 0.54 ± 0.07 | 0.83 | 18.40 ± 1.61 | 186 ± 27 |

The ± terms are reported standard deviations. Pass@3 has no accompanying deviation. Success-rate values are fractions: 0.28 corresponds to 28%, not 0.28%. Humans lead every accuracy column. OpenAI Deep Research leads agent partial completion and success; its Pass@3 ties Grok DeeperSearch. Operator gives the shortest agent answers, and Gemini the longest. There are no significance markers. Timing values are collected under mixed procedures and, for manually timed systems, on a subset. This caveat limits precise efficiency rankings.

## 12. Diagram / Architecture Interpretation

[A/B] The benchmark pipeline is: practical task proposal → expert refinement → independent validation → task-specific rubric/script generation → automated debugging and reflection → human script validation → answer-based testing and refinement → held-out judge assessment. Task creators and human-study completers are separated to reduce prior-knowledge advantages.

The evaluation pipeline is: answer with citations → structured extraction → relevant source lookup from caches → simple or URL-based leaf verification → upward gated aggregation → Partial Completion and Success Rate. The cache holds text and screenshots, allowing both textual and visual source evidence. Manual cache repair handles automation blocks.

Information flow differs from control flow. Extracted fields and cached evidence feed leaf checks. Critical failures and sequential dependencies control which checks run. Scores flow upward through the tree. During ordinary evaluation, blocked nodes can be skipped for efficiency; during judge-validation assessment, all nodes are evaluated for comprehensive comparison.

The error-analysis flowchart is a separate human procedure: inspect textual task satisfaction, then inspect attribution, and classify failures. Its seven labels describe failure types rather than the hierarchical score calculation. The GUI is an inspection aid connecting an answer, source page, rubric, and outcome on one screen. These distinctions prevent confusing an error taxonomy with the system’s actual evaluator architecture.

## 13. Equations and mathematical concepts

[A] The principal equation is on p. 5, §3.3. Let v be a rubric node, C(v) its children, K(v) its critical children, and N(v) = C(v) \ K(v) its non-critical children. The node score s(v) lies in [0,1]. Its recursive rule is:

\[
s(v)=\begin{cases}
0,&\text{if some }u\in K(v)\text{ has }s(u)<1,\\
\frac{1}{|N(v)|}\sum_{u\in N(v)}s(u),&\text{if all critical children pass and }|N(v)|>0,\\
1,&\text{otherwise.}
\end{cases}
\]

The existential condition means that any failed critical child blocks the parent. The universal condition means that every critical child must score 1 before non-critical progress is averaged. |N(v)| is the number of non-critical children. The summation adds their scores. If there are no non-critical children and all critical children pass, the parent receives 1.

Inputs are child scores and their critical/non-critical classifications; output is a parent score. The recursion propagates leaf judgments to the root. Leaf scores are assigned by verification, not inferred from an empty child set. Sequential blocking is additionally described in prose and implemented by the toolkit; the displayed piecewise equation does not alone specify every ordering rule.

**Illustration [D], not an additional paper result:** if a parent’s essential budget check passes and three of five equally averaged item checks pass, its score is 3/5 = 0.6. If the budget gate fails, the parent scores zero even if all five item checks pass. Figure 2 displays this kind of structure.

Partial Completion is the mean of root scores over tasks; Success Rate is the proportion with root score exactly 1. Pass@3 uses three attempts and reports whether any succeeds. No optimization loss, theorem, proof, or formal adversarial equation is supplied.

## 14. Interpretation and discussion

[A] The results answer the two benchmark-construction challenges through validated realistic tasks and automated criterion-level evaluation. The authors argue that task-specific trees allow flexible answers while preserving rigorous requirements. Their held-out human assessment supports reliability within the tested sample.

The time-varying hypothesis is directionally supported: most systems score lower on the 57-task subset, while Operator and humans show relatively favorable performance. Authors interpret this as evidence for integrating live browsing. They also attribute Deep Research advantages to extensive search, synthesis, tools, and sustained engagement. Browser agents face noisier environments, larger action spaces, and longer contexts than search-API-centered systems (p. 8).

[D] These mechanism explanations are plausible but not experimentally isolated. Systems differ in training, prompts, tools, interfaces, retrieval strategy, and underlying models. More time and more browsing may both be useful, but cross-system comparisons cannot identify each factor’s independent causal contribution.

Important consistency issues remain visible. Appendix F.2 says human answers have no completeness omissions, yet human-study procedures allow stopping; this can describe the analyzed sample without proving universal human completeness. Appendix H.3 calls the omission subtype Partial Completion, whereas the main taxonomy calls it Partial Missing; this is distinct from the benchmark metric Partial Completion. The script-generation pipeline is described as hidden, while Appendix D supplies process details and promises implementation material; the precise release boundary cannot be verified without the repository. Rounded time 18 in Table 2 and 18.40 in Table 3 differ in precision rather than clearly contradicting one another.

The 99.03% result depends on adjudication and on excluding one conflicting-source disagreement under the one-supporting-source assumption. It should not be strengthened into a claim that the evaluator establishes real-world truth with 99.03% accuracy.

## 15. Contributions and novelty

[A] **Benchmark/dataset:** 130 curated, realistic tasks spanning six domains and 24 subdomains, including changing answers and extensive browsing demands.

**Methodological:** task-specific rubric trees that combine essential gates, meaningful partial credit, attribution requirements, and sequential dependencies.

**Evaluation system:** Python judge workflows combining structured extraction, LLM verification, tools, webpage caches, and score propagation.

**Implementation/development:** reusable evaluator components, LLM-generated initial scripts, runtime debugging, self-reflection, a GUI, and multi-stage human refinement.

**Empirical:** comparison of ten systems, human effort measurements, a time-varying subset analysis, a seven-category error taxonomy, a restricted hallucination-rate analysis, and held-out judge validation.

The authors’ novelty claims should be read relative to their cited comparison set. The paper acknowledges related Agent-as-a-Judge work and PaperBench’s tree rubrics; it emphasizes automation, varied score aggregation, and the particular long-horizon/time-varying search setting. There is no new foundational model, security defense, formal theorem, or directly evaluated attack technique.

## 16. Limitations

### Authors’ stated limitations

[A] Appendix A identifies incomplete real-world task coverage; exclusion of vague and highly subjective queries; assumptions that cited sources are truthful and credible; a restriction to decomposable single-page attribution; possible LLM extraction and judgment errors; and limited interpretation and precise cost estimation for proprietary black-box systems. Weak systems are excluded to retain meaningful comparisons.

Other explicit qualifications include underestimated human effort due to mistakes, omissions, and stopping; static retrieval’s inability to see some collapsed content; continuously changing systems; and possible website changes requiring benchmark maintenance. Appendix B warns about benchmark-specific reinforcement-learning overfitting and rubric bias.

### Additional evidence-based analyst observations

[D] Human results use 30 tasks, while agent accuracy uses 120; comparisons are informative but not perfectly matched. Time collection mixes UI-reported and manual measurements. One main human evaluator performs the 720-check judge study, followed by developer adjudication. Excluding trivial failures changes its sampled case mix. The repeated-run standard deviations do not establish statistical significance of small ranking differences.

The displayed example script raises concrete implementation questions. It truncates author entries to the first five and pads missing entries (p. 42). It checks each name against any expected contributor, without a visible cross-slot uniqueness check. It labels a profile URL non-critical even though the task requests profile links (p. 43), potentially in tension with Appendix D.1’s critical-attribution principle. Exact score consequences cannot be determined without toolkit semantics or execution. These are observations about the supplied example, not claims that all benchmark scripts share these issues.

## 17. Threats to validity

The following labels are **analyst interpretations [D]**, grounded in the supplied study design.

**Construct validity:** the benchmark measures task compliance and source support. It does not measure whether sources are truthful, whether an agent resisted malicious instructions, or whether autonomous actions were safe. Surface-level incompleteness labels explicitly exclude subtle reasoning failures (p. 49).

**Internal validity:** proprietary-system differences and prompt adaptations confound causal explanations. Operator and Gemini receive extra source instructions. The time-versus-performance analysis does not hold model, tools, and budget constant. Judge refinement uses answers from evaluated systems, although held-out answers and restrictions on adjustments help reduce answer-specific fitting.

**External/ecological validity:** authentic tasks and live sources increase realism, but login exclusion, English-only scope, no video, static-verification restrictions, and task clarity requirements narrow deployment applicability. Evaluating final answers does not reveal all intermediate actions or hazards.

**Statistical conclusion validity:** uncertainty is standard deviation across repeated evaluations; confidence intervals and significance tests are absent. Thirty tasks support error/human comparisons and fifteen support judge validation, limiting precision and subgroup generalization. Multiple node checks within a task are not necessarily independent observations.

**Reproducibility:** study dates, prompts, model names, and an example script help. Hidden test rubrics, evolving products, undisclosed commercial internals, and unavailable supplied caches prevent full independent reproduction from this material alone.

## 18. Future work and open questions

### A. Explicit author proposals or commitments

[A] The p. 5 footnote permits future exploration of additional logic beyond the current sequential scheme. Appendix C.4 commits to periodic review, user feedback, and replacement or updating of tasks affected by website changes. Future leaderboard results will carry timestamps. The discussion urges stronger integration of live browsing and identifies potential benefit from additional inference resources and attempts. Appendix F suggests that off-the-shelf agents may need additional tailoring or training for robust tool use; this is a research implication, not a demonstrated remedy.

### B. Additional open questions

[D] How would results change if source credibility were assessed separately from attribution? How often do dynamic or conflicting sources change scores? Can exact source URLs be preserved through long contexts without reconstruction errors? Would a matched 30-task agent/human comparison change the performance ratio? How do score uncertainty and model updates affect rankings?

For the security research question, controlled experiments would be needed to distinguish ordinary unreliability from adversarial susceptibility. Relevant unanswered questions include whether untrusted webpage instructions alter task goals, whether tool permissions turn answer errors into harmful actions, and whether judge inputs themselves can be manipulated. None is tested here. A standalone-LLM comparator, shared task conditions, attacker model, and attack-success definition are absent, so no quantitative agent-versus-LLM vulnerability ratio can be inferred.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this work |
|---|---|
| LLM | Large language model used for planning, generation, extraction, or verification |
| Agentic search | Autonomous repeated search and synthesis using tools |
| Deep Research | Systems designed for extensive information collection and reports |
| API | Application programming interface through which a tool or service is accessed |
| URL | Uniform resource locator identifying a source page or document |
| GUI | Graphical user interface used to inspect evaluator evidence |
| Long horizon | Many actions or substantial information-gathering effort |
| Time-varying answer | Answer whose content may change with time |
| Correctness | Satisfaction of the task’s requested requirements |
| Attribution | Evidence linking answer claims to supporting sources |
| Rubric tree | Hierarchical organization of evaluation criteria |
| Critical node | Essential check whose failure blocks its parent |
| Non-critical node | Check contributing to partial credit when gates pass |
| Sequential node | Ordered dependency in which an earlier failure blocks later checks |
| Extractor | LLM tool converting answer content into structured fields |
| Verifier | LLM tool judging simple correctness or webpage support |
| Short-circuit | Skipping checks whose outcome cannot change a blocked result |
| Partial Completion | Mean rubric-root score, from 0 to 1 |
| Success Rate | Fraction of tasks with perfect root score |
| Pass@3 | Fraction with at least one success among three attempts |
| Unsupported Answer | Claim with a reachable source that fails to support it |
| Synthesis Error | Relevant source information is misrepresented |
| Retrieval Error | Cited source is irrelevant to the needed information |
| Invalid Attribution | Broken, malformed, expired, or fabricated source URL |
| Missing Attribution | Required source support is absent |
| Parametric memory | Information associated with model parameters rather than verified live retrieval, as discussed by the authors |
| v, u | A rubric node and one of its children |
| C(v), K(v), N(v) | All, critical, and non-critical children of v |
| s(v) | Score of node v |
| |N(v)| | Count of non-critical children |

Terms such as hallucination are operationalized here through error labels. They should not silently be treated as a measured malicious attack or proof of an internal generation mechanism.

## 20. Key numerical results

Table 3 above preserves every system row; this compact ledger records construction, conditions, validation, and important derived comparisons.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Benchmark size | 130 | tasks | Complete benchmark | Author-reported | pp. 1, 6 |
| Construction labor | At least 1,000 | hours | Tasks and judges together | Author-reported | p. 6 |
| Public/private split | 10 / 120 | tasks | Development / test | Author-reported | pp. 6–7 |
| Domain coverage | 6 / 24 | domains / subdomains | Final taxonomy | Author-reported | p. 17 |
| Explicitly time-varying subset | 57 | tasks | Relative dates or frequently changing information | Author-reported | p. 9 |
| Evaluation repetitions | 3 | attempts/task/system | Private test | Author-reported | p. 7 |
| Human subset | 30 | tasks | Random private-test subset | Author-reported | pp. 6–7 |
| Human participants | 7 | people | Three completers per task | Author-reported | pp. 6, 25 |
| Human attempts | 90 | task attempts | 30 × 3 | Analyst-derived | pp. 6, 25 |
| Rubric leaves | 34 / 3 / 357 | average/min/max nodes | Benchmark rubrics | Author-reported | Table 2a, p. 6 |
| Rubric total nodes | 50 / 4 / 603 | average/min/max nodes | Benchmark rubrics | Author-reported | Table 2a, p. 6 |
| Rubric depth | 4 / 2 / 6 | average/min/max levels | Benchmark rubrics | Author-reported | Table 2a, p. 6 |
| Human time | 18 / 8 / 44 | average/min/max minutes | Effort statistics on Subset-30 | Author-reported | Table 2b, p. 6 |
| Human websites | 8 / 3 / 31 | average/min/max sites | Subset-30 | Author-reported | Table 2b, p. 6 |
| Human webpages | 110 / 38 / 375 | average/min/max pages | Subset-30 | Author-reported | Table 2b, p. 6 |
| Best agent partial completion | 0.54 ± 0.04 | score | OpenAI Deep Research | Author-reported | Table 3, p. 7 |
| Best agent success | 0.28 ± 0.04 | fraction | OpenAI Deep Research | Author-reported | Table 3, p. 7 |
| Human partial completion | 0.79 ± 0.01 | score | Subset-30 | Author-reported | Table 3, p. 7 |
| Human success | 0.54 ± 0.07 | fraction | Subset-30 | Author-reported | Table 3, p. 7 |
| Agent/human completion ratio | Approximately 68.35 | percent | 0.54/0.79 × 100 | Analyst-derived | Table 3, p. 7 |
| Agent/human success ratio | Approximately 51.85 | percent | 0.28/0.54 × 100 | Analyst-derived | Table 3, p. 7 |
| Agent/human time ratio | Approximately 45.65 | percent | 8.40/18.40 × 100 | Analyst-derived | Table 3, p. 7 |
| Hallucination rate | 23 | percent of tasks | OpenAI Deep Research; selected error union on Subset-30 | Author-reported | p. 31 |
| Other analyzed agents’ hallucination | At least 50 | percent of tasks | Other four agents in error analysis, not necessarily all ten | Author-reported | pp. 26, 31 |
| Judge-validation sample | 15 × 2 | tasks × held-out answers | Trivial total failures excluded | Author-reported | p. 10 |
| Leaf verifications | 720 | checks | Judge-validation sample | Author-reported | p. 11 |
| Initial disagreements | 35 | checks | Before adjudication | Author-reported | p. 11 |
| Human-error disagreements | 27 | checks | After developer review | Author-reported | p. 11 |
| Actual remaining errors | 7 | checks | Three judgment + four hidden-content failures | Author-reported | p. 11 |
| Judge correctness | 99.03 | percent | Excludes human errors and source-conflict case | Author-reported | p. 11 |
| Shopping violation | 1,277.97 | dollars | Budget 200–600 | Visually readable | Fig. F.4, p. 28 |

[C] Judge correctness is reproducible as (720 − 7)/720 × 100 = approximately 99.0278%, rounding to 99.03%. The 57-task time-varying count is reported directly; this report does not assume its denominator is 120 rather than 130 when calculating a prevalence because that boundary is not made explicit in the quoted passage.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Realistic long-horizon tasks require a different evaluation design | Task principles, changing answers, fine-grained rubrics | X1 construction; Figs. 1–2 | pp. 2–6, 18–19 | Strong description of this benchmark; broader necessity remains author argument |
| Judges assess both task requirements and source support | Extractor/Verifier workflow and critical attribution | Equation; Appendix D | pp. 5, 19–21 | High confidence in method; source truthfulness assumed |
| Best observed agent remains below human means | 0.54/0.28 versus 0.79/0.54 | Table 3, X1–X2 | p. 7 | Strong reported comparison; differing task subsets |
| More attempts improve available task success | Pass@3 exceeds mean success for all rows | Table 3, X3 | p. 7 | Descriptive evidence; extra attempts incur additional unreported cost |
| Most systems struggle with time variation | Most time-varying line points below other-task points | Fig. 4, X4 | pp. 8–9 | Directional support; no exact chart values or causal isolation |
| Tool integration can fail before search succeeds | HF trajectory and parsing error | Fig. F.11, X5 | pp. 31, 33 | Strong single-case evidence; frequency by specific cause absent |
| Correct navigation does not ensure correct final provenance | Operator visits correct page but reports altered URL | Fig. F.12, X5 | pp. 10, 34 | Strong example; long-memory mechanism is partly interpretive |
| Unsupported/fabricated evidence persists in capable systems | Restricted hallucination rate 23% for best system | X6; Figs. F.5, F.7–F.8 | p. 31 | Sample-specific operational rate, not attack rate |
| Judge verification is highly reliable in its checked sample | Seven errors among 720 checks after adjudication | X7 | pp. 10–11 | Narrow, assumption-dependent validation |
| Security relevance is indirect | Complex environment/context, tool and attribution failures | X5; author discussion | pp. 8, 16, 31–35 | Analyst inference; no standalone-LLM or adversarial comparison |

### Appendix G implementation ledger

[A] The public-development example asks for the first main-branch transformers commit adding LLaVA support, its first seven ID characters, date, all contributors, their GitHub profiles, and displayed real names. Ground truth in the script is `44b5506`, `Dec 7, 2023`, and five expected names: Younes B, Arthur/Arthur Zucker, Shauray Singh, Lysandre Debut, and Haotian Liu (p. 38). These are author-provided ground truth, not externally verified facts.

The script defines structured author, commit, and author-list models. It extracts commit information and author information separately; checks commit existence, ID match, source support, and date; then evaluates authors after the commit stage. Missing fields are represented with null or empty lists. Author slots are truncated/padded to five; each includes existence, expected-name match, and profile-source checking. The root uses sequential aggregation, and `get_summary()` returns results. The code illustrates how abstract rubric concepts become a task-specific workflow. Imports, repetitive helper construction, and prompt strings are compressed; no execution or syntax-validity claim is made.

## 22. Very simple explanation — Explain Like I’m 15

Imagine asking an AI to find five pieces of furniture that are all white, from one store, and together cost between $200 and $600. A fluent answer can still be wrong: one item might be black, the total might exceed the budget, or a link might lead nowhere. Checking whether the answer sounds convincing is not enough.

This paper creates 130 difficult web-research tasks and a detailed checklist for each. The checklist is organized like a tree. Small checks ask whether a price, name, color, or link is right. Important checks act like gates: if an essential rule fails, success at other details cannot rescue the answer. The evaluator also opens saved source information to see whether links really support the claims.

The strongest tested AI finishes much of the work faster than people, but it fully succeeds on only about 28% of the test tasks. People do better, though they also make mistakes during tedious research. AI systems can find the right page and still put the wrong link or wrong information in their final answer.

For a security investigation, this is useful because it shows several places where web-connected AI can fail: tools, long sequences of actions, remembered sources, and claim checking. But the paper does not show attackers exploiting those failures, and it does not compare these agents with a plain LLM that has no web tools. It supports questions to investigate, not a proven answer that web agents are more vulnerable.

## Completeness Audit

The audit denominator is the inventory established above. Fully represented means the substantive content is explained, not that every word is reproduced. Text-only inspection is explicitly distinguished from visual inspection.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, affiliations, version | Yes, text and p. 1 render | Yes | Represented in compressed form | Full authors retained in research metadata description below; arXiv version/date identified |
| Abstract | Yes, text and visual | Yes | Fully represented | Task count, evaluator, study, main conclusion |
| §1 Introduction | Yes, text and visual | Yes | Represented in compressed form | Historical search background compressed |
| §2 Related Work | Yes, text and visual | Yes | Represented in compressed form | Categories/positioning retained; cited papers not independently inspected |
| §§3.1–3.2 Overview and Task Collection | Yes, text and visual | Yes | Fully represented | Two explicit challenges and validation stages |
| §3.3 Rubric Tree | Yes, text and visual | Yes | Fully represented | Gates, partial scores, sequential dependence, metrics |
| §3.4 Judge Agent | Yes, text and visual | Yes | Fully represented | Inputs, extraction, verification, model |
| §3.5 Statistics and split | Yes, text and visual | Yes | Fully represented | All Table 2 values, splits, human subset |
| §4.1 Setup | Yes, text and visual | Yes | Fully represented | Runs, systems, timing caveat, private test |
| §4.2 Main Results and five discussion themes | Yes, text and visual | Yes | Fully represented | Agent types, answer style, scaling, time variation, promise |
| §4.3 Error Analysis | Yes; pp. 9 visual, 10 text | Yes | Fully represented | All seven error labels and overlapping categories |
| §4.4 Judge evaluation | Yes, text only on pp. 10–11 | Yes | Fully represented | Sampling, rubric assessment, all discrepancy categories |
| §5 Conclusions | Yes, text only | Yes | Represented in compressed form | Benchmark/evaluation implications |
| A Limitations | Yes, text only | Yes | Fully represented | All four named limitation themes |
| B Broader impacts | Yes, text only | Yes | Represented in compressed form | Benefits, misinformation, unauthorized extraction, bias, overfitting |
| C.1 Domains / Fig. C.1 | Yes, text only | Yes | Fully represented for extracted content | Counts retained; no visual-layout claim |
| C.2 Task principles | Yes; p. 18 visual | Yes | Fully represented | Exclusions and single-page assumption |
| C.3 Collection pipeline | Yes, text; partial visual | Yes | Fully represented | Proposal, refinement, two independent validators |
| C.4 Maintenance | Yes, text only | Yes | Fully represented | Periodic review and replacements |
| D.1 Rubric principles | Yes, text only | Yes | Fully represented | Meaningful partial credit, critical attribution |
| D.2 Judge details and prompts | Yes, text only | Yes | Represented in compressed form | Extraction-only rules, null fields, simple/URL verification, short-circuit |
| D.3 Generation | Yes; p. 22 visual | Yes | Fully represented | Claude generation; runtime and reflection loops |
| D.4 Validation / Fig. D.1 | Yes, text and supplied visual | Yes | Fully represented | Six-system answer sample and GUI roles |
| D.5 Human assessment | Yes, text only | Yes | Fully represented | One evaluator, rubric then node assessment |
| E.1 Settings and inference prompts | Yes, text only | Yes | Fully represented in substance | Date range, o3, UI collection, prompt adaptations |
| E.2 Caching | Yes, text only | Yes | Fully represented | Playwright, screenshots/text/PDFs, manual repairs |
| E.3 Human study | Yes, text only | Yes | Fully represented | Qualification, assignment, stopping, logs |
| F.1 Taxonomy / Fig. F.1 | Yes, text and visual | Yes | Fully represented | Correctness/attribution branches |
| F.2 Additional analysis | Yes, text only | Yes | Fully represented | Hallucination definition/rates and system discussions |
| H.1 Collection instructions | Yes, text only | Yes | Represented in compressed form | Scope, verification tools, login/dynamic-content restrictions |
| H.2 Human instructions | Yes, text only | Yes | Represented in compressed form | Browser-only, no AI, recordings, trial tasks, stopping |
| H.3 Error instructions | Yes; p. 49 visual, 50 text | Yes | Fully represented in substance | Surface omissions, unsupported sources, naming variation |
| H.4 Human evaluation instructions | Yes, text only | Yes | Fully represented in substance | Independent ratings, TODO-to-binary labels, mismatch adjudication |
| Figures 1–2 | Yes, visual and text | Yes | Fully represented | Workflow and scoring example |
| Figures 3–5 | Yes, visual and text | Yes | Fully represented qualitatively | Exact unlabeled plot values deliberately not invented |
| Figures F.2–F.8 | Yes, visual and captions | Yes | Represented in compressed form | Seven canonical examples, each accounted for |
| Figures F.9–F.15 | Yes, visual and captions | Yes | Represented in compressed form | Each case and evidence boundary retained |
| Tables 1, 2a, 2b, 3 | Yes, visual and text | Yes | Fully represented | All rows and substantively important values |
| Principal equation | Yes, visual and text | Yes | Fully represented | Symbols, cases, role, sequential boundary |
| Appendix G script | Yes, text only | Yes | Represented in compressed form | Workflow, ground truth, checks, possible implementation concerns |
| Formal algorithms/theorems | No such objects supplied | Not applicable | No inventory item | Code example accounted for separately |
| Explicit challenges/objectives | Yes | Yes | Fully represented | Formal questions not fabricated |
| Time-varying hypothesis | Yes | Yes | Fully represented | Directional support with observational caveat |
| Experiments X1–X7 | Yes | Yes | Fully represented | Different samples and conditions preserved |
| Major contributions | Yes | Yes | Fully represented | Dataset, method, system, implementation, empirical |
| Substantive footnotes | Yes | Yes | Fully represented in substance | o4-mini, sequential future work, timing, held-out sampling, tracker |
| References and acknowledgments | Yes, text only | Yes | Represented in compressed form | No external citation validation; individual bibliography entries omitted |
| External repository/caches/videos/annotations | No, not supplied | Boundary disclosed | Missing from supplied material | No claim of artifact review or reproduction |

### Missing or inaccessible material

The referenced open-source repository, complete runnable toolkit, complete task/rubric collection, answer files, cached webpages, human recordings, annotation spreadsheets/JSON, private test scripts, script-generation pipeline, and live leaderboard are not supplied as separate inspectable artifacts. No separately embedded supplementary files are present in the provided accessibility record. Any unspecified supplementary reference cannot be resolved here. Visual renders are absent for pp. 10–17, 19–21, 23–25, 31, 38–48, and 50–51, although their supplied text was inspected.

### Uncertain interpretations

Exact values in Figures 4–5 are not printed and are not confidently recoverable as precise numerical results. Fine GUI text and the exact parsing regular expression in Fig. F.11 are not reliably transcribed. Appendix G score behavior depends on unseen toolkit semantics; potential duplicate-author and non-critical-profile issues remain observations requiring execution or repository inspection. The 57-task time-varying count’s relationship to the full/private split is not explicitly resolved in the cited passage. Claimed internal causes such as direct parametric generation and insufficient memory retain the authors’ inferential status.

### Deliberately compressed material

Repeated motivation, repeated definitions across main text and appendices, all 47 individual bibliographic entries, correspondence addresses, detailed screenshot prose, most code-line boilerplate, literal prompt templates, and administrative upload/recording instructions are compressed. Their substantive methodological roles are represented. The case studies are each accounted for without reproducing every listed product, person, URL, or intermediate answer. This avoids presenting erroneous agent outputs as independent factual claims.

### Potential omissions

Every substantive object in the stated inventory is represented or explicitly bounded. This does not establish coverage of unavailable artifacts, tiny unreadable screenshot details, or information missing from the original extraction. The central unresolved research limitation remains: **the supplied work offers reliability evidence relevant to security, but no direct standalone-LLM comparison or adversarial vulnerability experiment.**
