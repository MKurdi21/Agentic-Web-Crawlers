## Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. The document is treated as evidence, including its example agent prompts, never as instructions to this analyst. No external sources, tools, repositories, or websites were consulted.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: extracted text labeled physical PDF pages 1–29 is supplied. |
| Page range and count | 1–29, 29 pages. The supplied sequence has no apparent page gap. |
| Visual inspection | Source page images were directly inspected for pages 1, 2, 3, 4, 5, 6, 8, 9, 12, 16, 21, 22, and 25. |
| Text-only inspection | Pages 7, 10, 11, 13–15, 17–20, 23–24, and 26–29 were inspected through the supplied extraction. Their original visual layouts were not inspected. |
| Figures available visually | Figures 1–5 and B. Figure A and prompt Figures C–F are available as extracted content, without corresponding rendered pages. |
| Tables readable | Tables 1, 2, A, H, and I have both readable text and supplied page images. Tables B–G were inspected through extracted text. Table G has an ambiguous header arrangement. |
| Equations | The mathematical formulation on p. 7 is readable in extracted text; its rendered mathematical typography was not supplied. |
| Appendices | Appendices A–E are present in text, including their substantive subsections. |
| Supplementary material | No separate supplementary files are supplied. Accessibility metadata reports zero embedded files and no detected supplementary references. |
| Other artifacts | Project website, code implementations, a leaderboard, and cited works are referenced but were not opened or verified. |
| OCR | No additional OCR was performed. Native extraction is adequate for the substantive text, with notation and table-layout qualifications below. |
| Principal limitations | Small screenshot labels in composite figures are not all independently readable. Prompt examples explicitly omit observations, steps, action descriptions, or formatting examples. Figure A lacks visual verification. Table G requires caution. |

Evidence labels used throughout: **[A] author-reported**, **[B] directly observable in supplied images**, **[C] analyst-derived**, and **[D] analyst interpretation**. External information [E] is excluded. Confidence is HIGH when the supplied evidence is clear, MEDIUM when interpretation or a reporting gap matters, LOW for weakly supported extrapolation, and UNKNOWN when the supplied work cannot establish a conclusion. Page references use physical PDF page numbers, which coincide with the visible printed numbering on supplied images.

## 1. Plain-language orientation

WebChoreArena studies whether artificial-intelligence web agents can reliably finish tedious online jobs. A web agent combines a large language model, or LLM, with a mechanism for observing webpages and issuing browser actions. Instead of answering a single question from a fixed passage, it may need to search, open many pages, remember findings, calculate totals, apply filters, and finally submit an answer or change a website.

The central problem is measurement. According to the authors, WebArena, an established benchmark, contains many general browsing tasks and enough ambiguous instructions or evaluation errors to obscure progress by stronger agents. WebChoreArena therefore keeps four controlled WebArena websites but introduces 532 more demanding tasks built from 117 templates through more than 300 hours of manual development. The tasks emphasize retaining large amounts of information, using information across many steps, calculating from collected data, and performing specialized interface operations. [A: pp. 1–6]

The main finding is that these chores remain difficult. On the full benchmark, GPT-4o reaches 6.8% with AgentOccam and 3.4% with BrowserGym. GPT-5 reaches 45.1% and 48.3%, respectively. Eight human participants, solving one task per template, obtain a reported overall 50.2%. These human and agent results come from different task coverage; they should not be treated as a perfectly matched comparison over all 532 tasks. [A: p. 8, Table 1]

The contribution is primarily a benchmark and diagnostic evaluation, not a new security defense or a new language model. For the user's question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,' this paper supplies relevant descriptions of observation, memory, action, and evaluation mechanisms. **It does not directly compare web agents with standalone LLMs, measure adversarial vulnerability, or establish that agents are more vulnerable.** Its relevance to security is therefore analyst inference, with LOW confidence for any comparative vulnerability conclusion and HIGH confidence that the paper documents substantial ordinary task failures.

## 2. Document roadmap

The complete supplied inventory is as follows. The abstract on pp. 1–2 introduces the benchmark and its motivation. Section 1, Introduction, spans pp. 2–3 and states the problem, task concept, contributions, and headline findings. Section 2, Related Work, spans pp. 3–4 and separates dynamic-environment reproducibility from memory and long-term-reasoning benchmarks.

Section 3, WebChoreArena Benchmark, covers rationale (§3.1), environment and task overview (§3.2), statistics and categories (§3.3), manual construction (§3.4), and evaluation (§3.5), pp. 4–7. Section 4, Web Browsing Agents, gives a partially observable decision-process formulation (§4.1) and baseline-agent rationale (§4.2), p. 7. Section 5, Experiment, contains main results (§5.1) and analysis (§5.2), pp. 7–9. Section 6 concludes on pp. 9–10. Section 7 states three limitations on p. 10. Acknowledgments and references occupy pp. 10–13.

Appendix A discloses LLM usage, p. 14. Appendix B reviews WebArena: annotation/evaluation errors (§B.1, p. 14) and map-domain exclusion (§B.2, pp. 14–15). Appendix C describes task distributions (§C.1), observation modalities (§C.2), and failures (§C.3). The latter contains general failure patterns (§C.3.1) and two examples each for Shopping, Shopping Admin, Reddit, and GitLab (§§C.3.2–C.3.5), pp. 16–18.

Appendix D registers seven additional analyses: checkpoints (§D.1), fuzzy-match human validation (§D.2), open-source models (§D.3), reasoning effects (§D.4), real websites (§D.5), notebooks/scratchpads (§D.6), and calculators (§D.7), pp. 18–20. Appendix E contains agent overviews, execution settings, and agent selection (§§E.1.1–E.1.3); model implementation details (§E.2); website tips and prompt examples (§§E.3.1–E.3.2); and memory mechanisms (§E.4), pp. 21–29.

Visual inventory: Figures 1–5, Appendix Figures A–F, Tables 1–2 and A–I. Figure 2 has two panels; Figure 3 has four task examples; Figure 4 has three model panels; Figure 5 has four website panels; Figure A has two distribution panels; Figure B has two modality examples; Table H has two action-space panels. No numbered algorithm, theorem, lemma, proposition, or proof is supplied. The main mathematical object is the unnumbered formulation in §4.1. No keyword list or formally numbered hypothesis is supplied.

## 3. Background and context

A **graphical user interface**, or GUI, is the visible arrangement of website controls that a person can click or type into. The paper's agents receive either an **accessibility tree**, a structured textual representation of page elements, or a screenshot, an image of the rendered interface. The source abbreviates accessibility tree as A11y Tree and, in prompt examples, AXTree. These observation channels can expose different information. [A: pp. 2, 5, 16]

An **application programming interface**, or API, supports programmatic interaction with software. The benchmark does not assume website API access. Its purpose is browser interaction across websites where APIs might not be available. This is a scope decision, not an experiment demonstrating that browser interaction is safer or more dangerous than API access. [A: pp. 2, 10]

A **benchmark** is a collection of tasks and scoring procedures used to compare systems. Here, tasks run in simulated Shopping, Shopping Admin, Reddit, and GitLab websites. **Cross-site** tasks require navigation among multiple websites. A **task template** specifies a reusable task structure, while task instances substitute particular products, dates, users, or other variables. Template-related tasks may require different execution paths even when their wording has similar structure. [A: pp. 4–6]

The paper's memory categories have different meanings. **Massive Memory** concerns the amount of observed information that must be retained. **Long-Term Memory** concerns retaining and applying relevant information across multiple pages and interactions. **Calculation** concerns arithmetic or logical processing of observed information. **Others** covers specialized interface operations. A task may belong to up to two categories, so the category counts are overlapping rather than a partition. [A: p. 5]

**Accuracy** is reported as a percentage of successfully completed tasks under the relevant evaluation protocol. The paper uses textual matching, final-URL matching, and functional website-state checks. A **trajectory** is the sequence of observations and actions taken during execution. A **checkpoint** evaluates whether a required page was reached, which is weaker than confirming that the complete chore was done correctly. [A: pp. 7, 10, 18]

## 4. Research problem and gap

**Existing problem.** Agents increasingly perform well on familiar general browsing tasks, making it difficult to see whether their memory and reasoning improve on demanding chores. The authors want tasks requiring extensive collection, integration, and calculation of information. [A: pp. 1–3]

**Shortcomings attributed to previous approaches.** The authors characterize WebArena as focused mainly on general browsing. Their selected audit also finds ambiguous task descriptions, incorrect annotations, and evaluation expectations that can reject reasonable responses. For real websites, changing content undermines stable ground truth. Other memory-oriented benchmarks emphasize operating systems, office work, or a specific enterprise platform rather than the authors' intended range of general web chores. These are the paper's characterizations, not independently verified judgments about the wider literature. [A: pp. 2–4, 14]

**Research gap.** The authors seek a reproducible, more demanding benchmark with explicit output requirements and capability categories that distinguish navigation from the substantial work performed after navigation. [A: pp. 4–7, 18]

**Motivation.** Tasks such as counting many posts, comparing reviews across pages, and aggregating orders can be repetitive yet cognitively demanding. A controlled benchmark can make model differences easier to detect while reducing ambiguity about task success. [A: pp. 2, 5–6]

**Scope.** Four simulated website domains and cross-site tasks are included; the map website is excluded. Website APIs are not assumed. The evaluation emphasizes final outcomes, with an additional checkpoint analysis. Malicious websites, attack generation, compromised accounts, exfiltration, and standalone-LLM comparisons are outside the reported experimental scope. [A for benchmark boundaries; D for security-scope characterization]

## 5. Research questions, objectives, and hypotheses

The abstract explicitly asks whether current benchmarks can still accurately evaluate increasingly powerful agents, especially on tedious and cognitively demanding tasks. The supplied work does not formalize a numbered research-question set or statistical hypotheses. [A: p. 1]

Its objectives are to construct harder, manually curated chores; reduce ambiguous instructions and evaluation expectations; retain compatibility with WebArena; characterize performance across task types; assess model progress; and provide actionable error analysis. These objectives connect to the full-model comparison, category analysis, benchmark comparison, checkpoint evaluation, and failure studies. [A: pp. 2–9, 18]

The user's security question is a separate research objective brought to this analysis. This paper can inform a description of the mechanisms through which a web agent perceives information, stores it, and acts. It cannot answer a comparative security hypothesis without additional experiments. Any claim that more memory, more tools, or more pages necessarily increases adversarial vulnerability would go beyond these results. [D; comparative security confidence UNKNOWN]

## 6. Assumptions / Threat Model

The paper assumes a controlled environment with deterministic state transitions conditioned on actions. The agent observes only part of the environment and retains information through an explicit memory representation. Website content, task specifications, and evaluation criteria are treated as the operative benchmark environment. Cross-site prompts provide hints about a homepage and account information. [A: pp. 7, 24–25]

The benchmark assumes that browser observations and available actions are sufficient to solve the included tasks. Modality requirements are assigned per task: some information is accurately available only in text, while some is only graphical. The authors deliberately choose clear evaluation criteria rather than emphasizing ambiguous human requests. [A: pp. 5–7, 16]

**No adversarial threat model is specified.** There is no defined attacker, attacker objective, malicious-content budget, trust-boundary policy, or attack-success metric. The supplied work does not experimentally test whether page text can override task instructions, whether memory can be adversarially contaminated, or whether browser actions can be redirected by malicious content.

**Analyst interpretation for security:** Table H's browser actions, Appendix E's persistent memory, and cross-site account hints identify components that a future security study might examine. The GitLab tips mention profile access to access tokens and SSH keys, but the paper reports no attack involving those objects. Their mention is evidence about an interface tip, not evidence of exposure or compromise. [D: pp. 21, 24–25]

## 7. Methodology

### Benchmark construction and sample

The benchmark contains 532 tasks: Shopping 117, Shopping Admin 132, Reddit 91, GitLab 127, and Cross-site 65. Their total is 117 + 132 + 91 + 127 + 65 = 532. [C consistency check from A counts, p. 4] Website percentages in Figure 2a are 22.0%, 24.8%, 17.1%, 23.9%, and 12.2%, respectively.

Ten author-annotators participated. Three were assigned to each of the four websites, with one annotator working across all four for consistency. Ideas were independently proposed, discussed, and checked for solvability, difficulty, alternative paths, and output ambiguity. Early ideas were tested with a Claude-based agent and refined. Multiple rounds of inference, error analysis, and revision contributed to more than 300 hours of development. [A: pp. 5–6]

The 117 templates comprise 25 Shopping, 29 Admin, 20 Reddit, 28 GitLab, and 15 Cross-site templates. The reported average is approximately 4.5 instances per template. The benchmark uses up to two labels per task, treating main and secondary labels equally for distribution counts. Massive Memory has 206 label occurrences, Calculation 215, Long-Term Memory 247, and Others 47. [A: pp. 4–6, 15]

The observation allocation is 451 tasks solvable with any observation, 69 requiring accessibility-tree text, and 12 requiring screenshot information. Actual evaluation input is accessibility-tree-only for the first two groups and accessibility tree plus screenshot for the third. 'Any observation' therefore does not mean that every evaluated agent received both modalities. [A: pp. 5, 16]

No training/validation/test split is specified. The paper evaluates existing agents rather than reporting benchmark-specific model training. Dataset licensing, a contamination audit, random seeds, full execution logs, and comprehensive hardware specifications are not provided in the supplied material. Their absence limits this report's ability to assess those aspects; it does not establish that they were absent from all project artifacts.

### Scoring

The evaluation follows WebArena. `string_match` supports `exact_match`, requiring an exact answer; `must_include`, requiring the ground-truth content somewhere in the answer; and `fuzzy_match`, using GPT-4o to judge semantic equivalence. `url_match` checks the final URL. `program_html` extracts designated elements from the post-action page and compares them with ground truth to assess functional state changes. [A: p. 7]

Explicit formatting requirements aim to avoid rejecting correct substantive answers merely because they include extra wording. The paper does not supply a complete task-by-task allocation across all scoring types, although it reports 24 fuzzy-match tasks. No reported significance test, confidence interval, or repeated-run variance accompanies the principal accuracy tables. [A for scoring; D observation about reported statistics]

### Agents, actions, and budgets

BrowserGym uses 15 action types and permits multiple actions per step; AgentOccam uses eight action types and permits one action per step. Both receive a maximum of 50 steps per task. Thus, equal step ceilings do not imply equal numbers of primitive actions. BrowserGym uses code from Agent Workflow Memory; AgentOccam uses its original implementation. [A: pp. 21–22]

BrowserGym retains past reasons, actions, and memory entries. AgentOccam uses summaries and observation highlights, with a dedicated note action whose content persists. AgentOccam also supports branching into alternative plans and pruning back to a previous plan. This is an architectural comparison, not an isolated intervention changing only memory. [A: pp. 21, 25; D causal qualification]

### Model configuration

| Model | BrowserGym settings reported | AgentOccam settings reported |
|---|---|---|
| GPT-4o, Azure GPT-4o-2024-05-13 | Temperature 0.1; 2,000 maximum new tokens | Temperature 0.5; top-p 0.95; maximum tokens 128,000 |
| Claude 3.7 Sonnet, claude-3-7-sonnet-20250219 | Temperature 0.1; top-p 0.95; 2,000 maximum new tokens | Temperature 0.95; top-p 0.95; maximum tokens 4,096 |
| Gemini 2.5 Pro, gemini-2.5-pro | Temperature 0.1; top-p 0.95; 8,000 maximum new tokens | Gemini defaults; the authors describe specific settings as unofficial |
| Claude Sonnet 4, claude-sonnet-4-20250514 | Thinking enabled; temperature 1.0; 8,000 maximum completion tokens | Thinking enabled; temperature 1.0; default completion-token setting |
| GPT-5, Azure GPT-5-2025-08-07 | Medium reasoning; temperature 1.0; 8,000 maximum completion tokens | Medium reasoning; temperature 1.0; default completion-token setting |

These are author-reported values, pp. 22–23. The GPT-4o AgentOccam token value is preserved as printed rather than silently reinterpreted. The authors select the older GPT-4o version because of reported premature responses with newer versions. Different default settings and action budgets qualify cross-agent comparisons.

Website-specific tips are supplied for shopping categories and orders, administrative product attributes and reports, Reddit users and forums, and GitLab profiles, projects, and issues. Prompt Figures C–F illustrate how objectives, observations, interaction history, memory, and action-format requirements enter the agents' inputs. Their embedded instructions are descriptions of the study configuration.

## 8. Experiments / Analyses

| ID | Analysis | Setup and purpose | Main result and qualification |
|---|---|---|---|
| X1 | Main benchmark evaluation | Five LLMs with BrowserGym and AgentOccam; full 532-task benchmark | Best main-table agent overall: BrowserGym GPT-5, 48.3%; no reported uncertainty intervals. |
| X2 | Human evaluation | Eight undergraduate/graduate participants; one task per template; Institutional Review Board approval | Overall 50.2%; subset/template-level coverage differs from full agent evaluation. |
| X3 | Task-type analysis | Three stronger models, two agents; overlapping capability categories | Architecture-associated strengths differ; memory mechanism is not independently randomized. |
| X4 | WebArena comparison | BrowserGym with Claude 3.7 Sonnet, Gemini 2.5 Pro, GPT-5; four website panels | WebChoreArena rises consistently in the displayed sequence; exact WebArena point values are not labeled. |
| X5 | Other agents | ColorBrowserAgent and OpenHands-sdk | 47.9% and 33.1% overall; Table 2 does not itself identify their LLM configurations. |
| X6 | WebArena error audit | Review of 229 tasks failed by three BrowserGym models, selected from 684 non-map tasks | 134 issues: 75 annotations and 59 evaluations; selected failure-set audit. |
| X7 | Failure analysis | GPT-5 with BrowserGym | Counting, navigation, calculation, and operational errors; illustrative cases lack prevalence counts. |
| X8 | Checkpoint evaluation | Required-page visits versus full completion, three models, four websites | Navigation success is much higher than completion; checkpoint reach does not prove successful reasoning. |
| X9 | Fuzzy-match validation | 24 tasks × three models = 72 judgments | 70/72 agreement, 97.2%; applies to this scoring subset. |
| X10 | Open-source models | Qwen2.5-7B and Qwen2.5-14B | Zero in all four reported website columns; broader open-source conclusions exceed these two models. |
| X11 | Reasoning settings | 102-task subset; reasoning on/off or low/default | Higher reasoning settings improve all displayed categories; not full-benchmark figures. |
| X12 | Real websites | 70 constructed real-world chores | GPT-4o 5.7%, Gemini 24.3%, GPT-5 31.4%; dynamic content and blocks complicate evaluation. |
| X13 | Scratchpad | 169 Massive Memory tasks, excluding cross-site; optional GUI notes | Gemini 35.5→38.5; GPT-5 50.3→47.9; usage 29 and 12 tasks. |
| X14 | Calculator | 215 calculation tasks; optional GUI calculator | Claude 33.0 versus 33.0; GPT-5 displayed 50.2 versus 47.4; header ambiguity is retained. |
| X15 | Agent-selection preliminary | 102 tasks: 25 Shopping, 29 Admin, 20 Reddit, 28 GitLab | BrowserGym alternatives perform worse in Table I; it does not include an AgentOccam row. |

X1–X5 appear on pp. 7–9; X6 on p. 14; X7 on pp. 16–18; X8–X14 on pp. 18–20; X15 on p. 22. No attack experiment appears in this register.

## 9. Results

The full main-result table is preserved below. Values are author-reported accuracy percentages, not attack rates. Admin means Shopping Admin; Cross means cross-site tasks. [A: p. 8, Table 1]

| Agent/model | Shopping | Admin | Reddit | GitLab | Cross | Overall |
|---|---:|---:|---:|---:|---:|---:|
| Human | 64.0 | 46.7 | 45.0 | 41.4 | 57.1 | 50.2 |
| AgentOccam GPT-4o | 10.3 | 4.5 | 9.9 | 7.1 | 0.0 | 6.8 |
| AgentOccam Claude 3.7 | 27.4 | 28.8 | 23.1 | 22.8 | 7.7 | 23.5 |
| AgentOccam Gemini 2.5 | 33.3 | 43.2 | 40.7 | 41.7 | 12.3 | 36.5 |
| AgentOccam Claude Sonnet 4 | 34.2 | 37.4 | 30.8 | 36.2 | 3.1 | 31.1 |
| AgentOccam GPT-5 | 56.4 | 43.9 | 53.8 | 41.7 | 21.5 | 45.1 |
| BrowserGym GPT-4o | 4.3 | 2.3 | 5.5 | 3.9 | 0.0 | 3.4 |
| BrowserGym Claude 3.7 | 16.2 | 26.5 | 18.7 | 25.2 | 30.8 | 23.1 |
| BrowserGym Gemini 2.5 | 31.6 | 43.9 | 34.1 | 37.0 | 35.4 | 36.8 |
| BrowserGym Claude Sonnet 4 | 35.9 | 44.7 | 25.3 | 39.4 | 38.5 | 37.4 |
| BrowserGym GPT-5 | 43.6 | 61.4 | 44.0 | 48.8 | 35.4 | 48.3 |

Three important qualifications follow. First, stronger models do not produce a strictly increasing sequence in every architecture or domain: AgentOccam Claude Sonnet 4 is below Gemini 2.5 overall, 31.1 versus 36.5. Second, GPT-5 BrowserGym exceeds the reported human Admin accuracy, 61.4 versus 46.7, while humans lead overall; differing human task coverage prevents a simple matched superiority claim. Third, AgentOccam and BrowserGym GPT-5 trade website strengths: the former leads Shopping and Reddit, while the latter leads Admin, GitLab, Cross, and overall.

**Analyst-derived differences:** BrowserGym GPT-5 exceeds BrowserGym GPT-4o by 48.3 − 3.4 = 44.9 percentage points. AgentOccam GPT-5 exceeds its GPT-4o configuration by 45.1 − 6.8 = 38.3 percentage points. The GPT-5 overall architecture difference is 48.3 − 45.1 = 3.2 percentage points. These are absolute accuracy differences, not relative percentage improvements and not causal effect estimates.

The cited preliminary WebArena GPT-4o score is 42.8%, compared with WebChoreArena's 6.8% and 3.4%. The accompanying passage does not give a fully matched agent-specific WebArena table for both comparisons. It supports the reported large difficulty contrast, but not a claim that a single controlled change caused the entire difference. [A and D: p. 8]

The failure examples make ordinary unreliability concrete. Shopping failures include answering before checking all relevant pages and repeatedly inspecting the same products. Admin failures include missing an update-time sort and selecting an inefficient review view. Reddit failures include miscounting 600 posts and misusing stored notes. GitLab failures include ignoring the 2021–2022 restriction and stopping midway through a project list. These are author-provided diagnoses, without a quantified distribution of failure causes. [A: pp. 17–18]

## 10. Figure-by-figure interpretation

### Figure 1 — How chores extend general browsing

Directly inspected on p. 1. Four colored website rows connect simpler WebArena requests on the left to more demanding WebChoreArena requests on the right. Arrows indicate a conceptual increase in task complexity, not measured data flow or an implemented pipeline. Shopping changes from retrieving one order cost to comparing Home & Kitchen spending across August–November 2022. Admin changes from a top-selling brand to monthwise customer/order analysis involving averages. Reddit changes from posting fixed text to transferring a highly upvoted comment between specified submissions. GitLab introduces a 2021–2022 activity restriction. There are no numerical axes, uncertainty marks, or experimental effect sizes. Small embedded interface screenshots are illustrative; not every internal label is legible. [A/B]

### Figure 2 — Website and task-type distributions

Directly inspected on p. 4. Panel a is a pie chart: Shopping green 22.0%, Admin yellow 24.8%, GitLab salmon 23.9%, Reddit blue 17.1%, Cross purple 12.2%. Panel b is a linear count bar chart with task type on the horizontal axis and Count on the vertical axis, ticks from 0 through 250. Bars are labeled Massive Memory 206, Calculation 215, Long-Term 247, Others 47. These labels sum to 715, exceeding 532 because tasks can have two types. **Analyst-derived:** 206 + 215 + 247 + 47 = 715 label assignments. Treating this as 715 distinct tasks would be incorrect. No error bars apply to these dataset counts.

### Figure 3 — Operational examples of four task types

Directly inspected on p. 6. Four panels combine task statements, interface screenshots, and arrows. Top-left: gather review distributions across pages, with Massive Memory as main type and Long-Term Memory as secondary. Top-right: retrieve discount rules, navigate to order pages, and apply them, with Long-Term Memory plus Calculation. Bottom-left: total comments across the top 40 most-commented posts in the deeplearning forum, combining Calculation and Massive Memory. Bottom-right: use issue labels to determine counts, illustrating specialized operations. Red dashed paths and annotations highlight collection, movement, and application of remembered information. These are examples, not performance plots; unreadable miniature page details are not reconstructed.

### Figure 4 — Accuracy by capability category

Directly inspected on p. 8. Three grouped-bar panels represent Gemini 2.5 Pro, Claude Sonnet 4, and GPT-5. Horizontal categories are Calc, Memory, Long-Term, Others; the vertical axis is accuracy, labeled Acc., with a common displayed range 0–80. Blue represents AgentOccam, orange BrowserGym. Exact labels are readable:

| Model | Agent | Calc | Memory | Long-Term | Others |
|---|---|---:|---:|---:|---:|
| Gemini 2.5 Pro | AgentOccam | 35.3 | 29.9 | 38.6 | 48.9 |
| Gemini 2.5 Pro | BrowserGym | 32.6 | 32.6 | 34.1 | 38.3 |
| Claude Sonnet 4 | AgentOccam | 32.2 | 26.7 | 30.5 | 43.5 |
| Claude Sonnet 4 | BrowserGym | 33.0 | 31.6 | 35.0 | 46.8 |
| GPT-5 | AgentOccam | 44.7 | 43.3 | 46.7 | 53.2 |
| GPT-5 | BrowserGym | 50.2 | 48.1 | 42.7 | 68.1 |

BrowserGym leads Memory in all three panels, but does not lead every category. Gemini AgentOccam leads Calculation, Long-Term, and Others; GPT-5 AgentOccam leads Long-Term. There are no error bars or significance markers. The caption supports architecture-associated differences; it does not isolate their cause.

### Figure 5 — Model progression on two benchmarks

Directly inspected on p. 9. Four line panels represent Shopping, Admin, Reddit, and GitLab. The horizontal sequence is Claude 3.7, Gemini 2.5, GPT-5; the vertical scale is score/accuracy on a displayed 0–100 scale. Blue is WebArena; orange is WebChoreArena; the agent is BrowserGym. Orange rises across the sequence in all panels. Blue is comparatively flat in some panels and non-monotonic in others, especially Reddit. Exact blue point values are not labeled, so none are invented. The figure supports the authors' selected-model comparison, not universal benchmark validity. No confidence bands are displayed.

### Figure A — Overlapping task labels

Inspected through p. 15 extracted text only. Panel a reports single-type tasks 65.6% and multiple-type tasks 34.4%. Panel b labels Calculation 14.1%, Calculation + Massive Memory 15.0%, Massive Memory 16.5%, Long-Term 28.0%, Others 7.0%, Massive Memory + Long-Term 7.1%, Calculation + Others 0.9%, Long-Term + Others 0.9%, and Calculation + Long-Term 10.3%. Colors, geometry, label placement, and graphical scaling were not visually checked. **Analyst-derived consistency:** 715 assignments − 532 tasks = 183 extra labels; if each task has one or two labels, 183/532 × 100 ≈ 34.4% have two labels, agreeing with the figure after rounding.

### Figure B — Disagreement between observation channels

Directly inspected on p. 16. Left: a shopping rating appears as 80%, or four stars, while the stated accessibility-tree value is 78. The task is labeled required_obs: text. Right: review stars exist only as icons and lack accessibility-tree rating information, so the task is labeled required_obs: image. Red boxes and arrows highlight the relevant rating regions. This establishes modality-dependent information and one numerical discrepancy, not adversarial falsification. The visual does not justify treating all screenshots as unreliable or all accessibility trees as authoritative in every setting.

### Figures C–F — Prompt examples

Inspected as extracted text on pp. 26–29, not as rendered figures. Figure C supplies BrowserGym's system-message example with general task framing and shopping tips. Figure D supplies a user-message example containing the product-review distribution task, current observation placeholder, action history, and memory entries; several elements are explicitly omitted. Figure E gives AgentOccam's system-message structure, allowed actions, planning operations, and tips. Figure F gives its objective, previous plan, two interaction steps, and an omitted current observation. Its example search result has rating 52 and 32 reviews; these are illustrative trace values, not benchmark aggregate results. The figures document prompt content and memory interfaces, not complete reproducible traces or security tests.

## 11. Table-by-table interpretation

### Table 1 — Main model and agent results

Directly inspected on p. 8 and transcribed in §9. Rows distinguish humans, two agents, and five LLMs. Columns report website and overall accuracy percentages. Best agent overall is BrowserGym GPT-5, 48.3; lowest is BrowserGym GPT-4o, 3.4. Both GPT-4o agents score 0.0 on Cross. AgentOccam Gemini and GPT-5 tie at 41.7 on GitLab. No standard deviations, intervals, significance tests, or missing-value notation are shown. The human row's different sampling is a material qualification.

### Table 2 — Additional agent comparison

Directly inspected on p. 9. Human, BrowserGym, and AgentOccam rows reproduce the corresponding results above. ColorBrowserAgent scores 60.9 Shopping, 43.6 Admin, 44.0 Reddit, 53.5 GitLab, 23.1 Cross, 47.9 overall. OpenHands-sdk scores 31.6, 30.3, 26.37, 48.8, 20.0, 33.1. The unusual 26.37 precision is preserved. BrowserGym leads overall and Admin; ColorBrowserAgent leads GitLab among the displayed agents; AgentOccam leads Reddit among agents. The table omits an LLM column, so additional-agent model configurations cannot be inferred solely from it.

### Table A — Required observations

Directly inspected on p. 16. Rows distinguish 451 any-observation tasks, 69 A11y-only tasks, and 12 screenshot-requiring tasks. Required input is A11y Tree for the first two rows and Screenshot + A11y Tree for the third. These sum to 532. The table distinguishes theoretical solvability from actual evaluation input.

### Table B — Checkpoint versus full completion

Text-inspected on p. 18. Values are percentages; each website has Full and Checkpoint columns:

| Model | Shopping F/C | Admin F/C | Reddit F/C | GitLab F/C |
|---|---|---|---|---|
| GPT-4o | 4.3 / 81.1 | 2.3 / 65.2 | 5.5 / 65.8 | 3.9 / 55.7 |
| Gemini 2.5 Pro | 31.6 / 84.2 | 43.9 / 73.5 | 34.1 / 89.5 | 37.0 / 77.1 |
| GPT-5 | 43.6 / 83.2 | 61.4 / 73.5 | 44.0 / 82.9 | 48.8 / 73.0 |

Gemini exceeds GPT-5 on three checkpoint columns and ties on Admin, yet is below GPT-5 on all four full scores. **Analyst-derived example:** GPT-4o Shopping has an 81.1 − 4.3 = 76.8 percentage-point reach/completion gap. This is not an estimated causal contribution of memory errors; a checkpoint is only a coarse prerequisite.

### Table C — Two open-source language models

Text-inspected on p. 19. Qwen2.5-7B and Qwen2.5-14B both score zero in Shopping, Admin, Reddit, and GitLab, with source formatting varying between 0 and 0.0. Cross and overall columns are absent. The table does not establish that every open-source model fails or supply a comprehensive model-size comparison. The authors attribute poor results to lack of agent training and context limitations without an isolated test of those explanations.

### Table D — Reasoning-setting analysis

Text-inspected on p. 19; 102-task subset. Category order is Calculation, Massive Memory, Long-Term, Others. Claude Sonnet 4 without reasoning scores 23.9, 16.7, 30.6, 27.3; with reasoning, 37.0, 27.8, 36.7, 45.5. GPT-5 low reasoning scores 17.4, 5.6, 22.5, 27.2; default reasoning, 52.2, 44.4, 38.8, 81.8. All displayed categories improve. These are not the full-benchmark Figure 4 values; differing samples explain why a direct numerical equivalence should not be expected. Category denominators and uncertainty are not reported here.

### Table E — Simulated versus real websites

Text-inspected on p. 20. WebChoreArena/Real percentages are GPT-4o 3.4/5.7, Gemini 36.8/24.3, GPT-5 48.3/31.4. The real set contains 70 tasks. Rankings match across the two settings, but scores do not: GPT-4o is higher on Real, while the other two are lower. Different task collections and changing sites prevent interpreting the differences as a clean environmental treatment effect.

### Table F — Optional scratchpad

Text-inspected on p. 20. On 169 Massive Memory tasks excluding cross-site, Gemini without/with scratchpad scores 35.5/38.5, using the tool in 29 cases; GPT-5 scores 50.3/47.9, using it in 12 cases. **Analyst-derived:** changes are +3.0 and −2.4 percentage points. The authors describe no significant impact, but supply no inferential test. Optional availability, limited adoption, and ineffective navigation differ from testing a consistently used, optimized notebook mechanism.

### Table G — Optional calculator

Text-inspected on p. 20. The extracted header includes Acc., #Tool Usage, Normal, and #w. Tool with unclear placement. Claude4's displayed row is 33.0, 33.0, 118; GPT-5's is 50.2, 47.4, 2. The surrounding text identifies 215 calculation tasks and says Claude uses the calculator frequently while GPT-5 almost never does. A plausible reading is normal accuracy, with-tool accuracy, and tool-use count, but the table layout was not visually supplied. This mapping is therefore MEDIUM confidence, with the raw values preserved. The statement that models rarely use tools is overbroad relative to 118 Claude uses if those are task-level uses; the precise count convention is not defined.

### Table H — Action spaces

Directly inspected on p. 21. BrowserGym's 15 types are noop, scroll, press, click, fill, hover, select_option, tab_focus, new_tab, tab_close, go_back, go_forward, goto, send_msg_to_user, and report_infeasible. AgentOccam's eight are click, type, go_back, go_home, note, stop, branch, and prune. These specify available operations rather than measured success rates. They document differences in navigation, messaging, persistent notes, and plan management; the paper does not experimentally rank their security properties.

### Table I — Preliminary agent selection

Directly inspected on p. 22. Website sample counts are 25, 29, 20, 28, totaling 102. BrowserGym Gemini scores 28.0, 48.3, 30.0, 39.3, overall 37.3; BrowserGym GPT-5 scores 44.0, 58.6, 40.0, 53.6, overall 50.0. ReasonerAgent Gemini scores 4.0, 31.0, 0, 3.6, overall 10.8. BrowserGym Code GPT-5 scores 20.0, 17.2, 25.0, 17.9, overall 19.6. The alternatives underperform the matched displayed BrowserGym configurations. Although nearby prose says the alternatives fail to outperform BrowserGym and AgentOccam, Table I contains no AgentOccam row for direct verification.

## 12. Diagram / Architecture

There is no standalone end-to-end system architecture diagram. Figure 1 is a conceptual task comparison; Figure 3 illustrates task workflows; Figures C–F show prompt composition. Their roles should not be conflated.

The architecture described by §4.1 is a repeated observation–memory–action loop. Input consists of a current webpage observation and retained information from earlier steps. The agent selects an action, the environment changes, and new information is written to memory for subsequent decisions. An action can either interact with a page or produce a textual answer. [A: p. 7]

BrowserGym's subsequent input includes earlier reasons, actions, and memory entries. AgentOccam's includes reasons, actions, and observation highlights, or summaries when highlights are too long; explicit notes add persistent information. Its branch/prune actions manage alternative plans. The paper does not provide a quantified context-retention policy or a full token-by-token trace for every task. [A: p. 25]

**Analyst interpretation:** A future security evaluation could separately test incoming page observations, information retained between steps, action selection, and final-state verification. This decomposition follows the documented workflow. It is not evidence that a demonstrated exploit propagates through these stages or that each stage increases vulnerability relative to standalone models.

## 13. Equations and mathematical concepts

Section 4.1, p. 7, models the environment and agent as a **partially observable Markov decision process**, or POMDP. The unnumbered formulation is E = (S, A, Ω, T, M). Here E denotes the modeled environment; S is the state set; A the action set; Ω the observation set; T the transition function; and M the set of memory states. The source explicitly includes memory in this tuple. This report preserves that formulation rather than replacing it with a different conventional definition.

The transition is T: S × A → S. Its inputs are a current state and an action; its output is a next state. The authors describe these transitions as deterministic. At step t, the environment has state s_t, a partial observation o_t ∈ Ω, and memory buffer M_t ∈ M containing important information through step t−1. The agent chooses a_t ∈ A based on o_t and M_t. This yields s_(t+1) and o_(t+1), while relevant content from o_t updates memory to M_(t+1).

In ordinary language: the agent cannot see everything at once, so it must combine what the current page shows with information remembered from earlier pages. The source does not specify a mathematical policy function, observation-generation function, reward function, discount factor, probabilistic transition model, training loss, or formal memory-update operator. Those are not invented here. No proof or theorem depends on the formulation.

A task-specific mapping in the prompt examples converts stars to rating values: 1→20, 2→40, 3→60, 4→80, 5→100, pp. 27 and 29. **Analyst-derived shorthand:** R = 20s for these listed star values s. This is a task instruction, not a learned model equation. Figure B also shows that a displayed four-star impression can hide a textual value of 78, so this mapping should not be used to replace exact observed ratings indiscriminately.

## 14. Interpretation and discussion

The results support a narrow but useful conclusion: finding the right page and performing the actual chore are different capabilities. Table B's high checkpoint rates alongside low full scores make this especially clear for GPT-4o. Errors after navigation include incomplete collection, ignored constraints, repeated exploration, and incorrect use of remembered information. [A: pp. 16–18]

The authors interpret Figure 4's memory differences through the agents' memory designs. Appendix E explains a plausible mechanism, but the comparison also changes action spaces, prompts, per-step action allowance, and some model settings. **Analyst interpretation:** the evidence supports an association between architecture and performance, while a causal claim that explicit memory alone explains the gap remains less secure.

The authors also argue that WebChoreArena reveals model progress more clearly than WebArena. Figure 5 supports this for its BrowserGym model sequence and four domains. It does not establish a universally correct model-capability ordering, benchmark reliability coefficient, or future resistance to saturation. AgentOccam's non-monotonic overall ordering further cautions against treating model names as a single experimentally controlled capability scale.

Several source-consistency points deserve explicit treatment. Appendix B gives 134 problematic tasks out of 684 and calls this 20.0%; **analyst-derived**, 134/684 × 100 ≈ 19.6%, so the paper's 20.0% is approximate. Its 134/229 ≈ 58.5% is consistent. Main-text map-exclusion pointers refer broadly to Appendix C, but the dedicated rationale is Appendix B.2. This is a cross-reference issue, not a different exclusion policy. Table G's general explanation of rare tool use needs qualification for Claude's reported 118 uses. The full-benchmark and 102-task reasoning figures have different samples and should remain separate.

For security, ordinary task failures can identify execution components deserving scrutiny, but they are not equivalent to malicious instruction-following. A wrong count is not an attack success; an unfinished post is not proof of safe refusal; reaching a sensitive-looking interface is not proof of unauthorized access. The paper's outcomes establish reliability difficulty, while comparative security conclusions remain untested. [D]

## 15. Contributions and novelty

**Conceptual contribution:** a definition of web chores as routine operations with clear goals but extensive memory, integration, and calculation demands. [A: p. 2]

**Dataset and benchmark contribution:** 532 manually curated tasks, 117 templates, four reproducible website domains, cross-site tasks, modality annotations, and overlapping capability labels. [A: pp. 4–6]

**Methodological contribution:** reduced ambiguity, explicit evaluation expectations, and a benchmark designed for capability-specific diagnosis while retaining WebArena compatibility. The underlying scoring functions and environments are inherited rather than introduced as wholly new mechanisms. [A: pp. 3, 6–7]

**Empirical contribution:** comparisons across five proprietary LLMs and two principal agents; additional agents; human evaluation; failure patterns; checkpoint evaluation; judge validation; reasoning, real-website, scratchpad, calculator, and preliminary-agent analyses. [A: pp. 8–9, 18–22]

No new training algorithm, theorem, security attack, defense, or direct standalone-LLM comparison is established. Appendix B explicitly says its WebArena error review is a necessary step for estimating the upper bound, rather than a claimed contribution. [A: p. 14]

## 16. Limitations

### Authors' stated limitations

Section 7, p. 10, identifies three. **Diagnostic precision versus coverage:** controlled difficulty, reduced ambiguity, and explicit criteria help diagnosis but may underrepresent real-world variability and unpredictability. **API assumption:** browser-only evaluation omits complementary API-enabled capabilities. **Trajectory evaluation:** the main evaluation emphasizes final outcomes; checkpoints provide only an initial finer-grained view, leaving detailed trajectory analysis for future work.

Additional author-acknowledged practical constraints include map-site inaccessibility and poor reproducibility, pp. 14–15; changing real websites and agent-action blocking, p. 19; limited and ineffective scratchpad/calculator usage, p. 20; inability to connect a closed-source agent to the sandbox because a secure connection could not be established, p. 22; and output-format difficulties with Browser-Use, p. 22. These are reported experimental constraints, not demonstrated vulnerabilities.

### Additional evidence-based analyst observations

Main tables omit uncertainty intervals, repeated-run variability, and formal significance tests. Human and full-agent samples differ. Template instantiations are related rather than necessarily independent. Architecture comparisons change multiple components. Early task refinement with a Claude-based agent may influence the challenge distribution; the paper does not quantify that influence. Most evaluations emphasize proprietary models, while two smaller open-source models do not represent the entire open-source space. Optional-tool experiments test both tool availability and agents' adoption choices, rather than successful tool use in isolation. The real-world set differs from the simulated benchmark. Security robustness, attacker capabilities, and standalone-model baselines are not measured. [D]

## 17. Threats to validity

These validity labels are analyst organization, not terminology necessarily used by the authors.

**Internal validity:** differences between agents combine memory, prompts, action spaces, and execution settings. This complicates attribution of score differences to a single component. In optional-tool studies, the instruction to consider a tool can itself alter navigation.

**Construct validity:** benchmark success measures chore completion under specified scoring. It does not directly measure malicious-content resistance, permission adherence, or comparative security. A checkpoint measures visiting a page rather than collecting all relevant information or correctly finishing the task. The authors' category labels are useful diagnostics, but a failed task can involve several capabilities.

**Statistical conclusion validity:** small differences such as 48.3 versus 47.9 lack accompanying uncertainty estimates. Overlapping categories and template families complicate assumptions of independent observations. The 97.2% judge agreement is based on 72 instances from 24 semantic-match tasks, not every evaluator and task.

**External and ecological validity:** four simulated websites omit the wider range of live pages and APIs. The 70-task real-web experiment provides supporting rank-order evidence but does not remove dynamic-content, blocking, and task-selection concerns. Controlled clear instructions underrepresent ambiguous real requests, as the authors acknowledge.

**Reproducibility:** model versions, key settings, agent action spaces, and step limits are reported. Some defaults remain unspecified; hardware, seeds, and repeated-run details are not supplied. Referenced implementations were not inspected. Prompt examples contain explicit omissions, so this report cannot reconstruct every experimental call exactly.

## 18. Future work and open questions

### A. Explicit author directions

The authors propose balancing diagnostic precision with broad real-world coverage, relating API-based and browser-based benchmarks, and developing more detailed trajectory-based evaluation. Failure analysis motivates stronger memory or structured aggregation mechanisms, more effective planning, and better execution strategies. Tool experiments point to the difficulty of using notebooks and calculators effectively. [A: pp. 10, 16–17, 20]

### B. Additional analyst questions

Would a matched memory intervention improve results while keeping prompts, primitive-action budgets, model settings, and evaluation fixed? Would repeated runs change rankings or clarify small score differences? How would humans and agents compare on exactly the same task instances? Do category-level results hold across new template families and websites?

For the user's security research, further work would need to define an attacker and protected assets, introduce controlled adversarial content, distinguish observation channels, trace persistence through memory, and measure unauthorized actions separately from ordinary failures. A standalone-LLM comparison would require a justified matched task and exposure design. These are proposed analyst questions, not experiments or recommendations validated by this paper. [D]

## 19. Terminology and notation glossary

| Term | Meaning in this paper |
|---|---|
| LLM | Large language model, used as the agent's decision-making model. |
| GUI | Graphical user interface, the browser controls the agent manipulates. |
| API | Application programming interface; website API access is outside the benchmark assumption. |
| A11y Tree / AXTree | Accessibility-tree representation of page elements and text. |
| Web chore | Clearly specified routine work requiring substantial memory, integration, or calculation. |
| Massive Memory | Retention of a large amount of observed information. |
| Long-Term Memory | Retention and application across multiple navigation steps or pages. |
| Calculation | Arithmetic or logical processing of collected information. |
| Others | Specialized interface operations outside the three main capability descriptions. |
| Cross-site | A task requiring more than one website. |
| Template | Reusable task structure expanded into multiple instances. |
| POMDP | Partially observable Markov decision process; the paper's model of sequential interaction. |
| S, A, Ω | State, action, and observation sets. |
| T | Deterministic state-transition function in the supplied formulation. |
| M, M_t | Set of memory states and the memory buffer at time t. |
| s_t, o_t, a_t | State, observation, and chosen action at step t. |
| Ground truth / GT | Reference answer or state used for evaluation. |
| Fuzzy match | GPT-4o judgment of semantic answer equivalence. |
| program_html | Functional evaluation of designated webpage elements after actions. |
| Checkpoint | Required-page URL visit, distinct from successful full completion. |
| Trajectory | The sequence of interaction steps. |
| Scratchpad | A WebArena page used for intermediate notes. |
| Reasoning effort | A model configuration varied in the reasoning analysis. |
| Top-p | A reported generation parameter; the paper provides values but no technical definition. |
| SKU | Product identifier requested in one task; the acronym is not expanded in the supplied work. |
| IRB | Institutional Review Board, which approved the human evaluation. |

## 20. Key numerical results

All source numbers below are author-reported unless explicitly identified as derived. Confidence is HIGH for clear source numbers, with interpretive qualifications stated elsewhere.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Benchmark size | 532 | tasks | Full WebChoreArena | Author-reported | pp. 1, 4 |
| Templates | 117 | templates | 25/29/20/28/15 by domain | Author-reported | p. 6 |
| Construction effort | Over 300 | hours | Manual development/refinement | Author-reported | pp. 2, 6 |
| Annotators | 10 | people | Authors; three per website with overlap | Author-reported | p. 5 |
| Task categories | 206/215/247/47 | assignments | Memory/Calculation/Long-Term/Others | Visually readable | p. 4, Fig. 2 |
| Multiple-type fraction | 34.4 | % | At most two labels per task | Author-reported | p. 15, Fig. A |
| Observation groups | 451/69/12 | tasks | Any/text-required/image-required | Author-reported | p. 16, Table A |
| Step ceiling | 50 | steps/task | Both principal agents; different actions per step | Author-reported | p. 22 |
| GPT-4o accuracy | 6.8 / 3.4 | % | AgentOccam / BrowserGym, full benchmark | Author-reported | p. 8, Table 1 |
| GPT-5 accuracy | 45.1 / 48.3 | % | AgentOccam / BrowserGym, full benchmark | Author-reported | p. 8, Table 1 |
| Human accuracy | 50.2 | % | Eight participants, one task/template | Author-reported | p. 8 |
| Other-agent overall | 47.9 / 33.1 | % | ColorBrowserAgent / OpenHands-sdk | Author-reported | p. 9, Table 2 |
| Selected WebArena issues | 134/229 | tasks | Selected failures among 684 non-map tasks | Author-reported | p. 14 |
| Selected issue rate | 58.5 | % | 134 of 229 reviewed failures | Author-reported | p. 14 |
| Whole-set issue fraction | Approximately 19.6 | % | 134/684 × 100; source says approximately 20.0% | Analyst-derived | p. 14 |
| Fuzzy-match task count | 24 | tasks | Of 532; source reports 4.5% | Author-reported | p. 18 |
| Judge agreement | 70/72; 97.2 | instances; % | Three models × 24 tasks | Author-reported | p. 18 |
| Real-site task count | 70 | tasks | Separate constructed real-world chores | Author-reported | p. 19 |
| Real-site scores | 5.7 / 24.3 / 31.4 | % | GPT-4o / Gemini / GPT-5 | Author-reported | p. 20, Table E |
| Scratchpad subset | 169 | tasks | Massive Memory, excluding cross-site | Author-reported | p. 20 |
| Calculator subset | 215 | tasks | Calculation-specific | Author-reported | p. 20 |
| Reasoning/selection subset | 102 | tasks | Separate subset analyses | Author-reported | pp. 19, 22 |
| BrowserGym GPT-5 minus GPT-4o | 44.9 | percentage points | 48.3 − 3.4 | Analyst-derived | p. 8 |
| GPT-5 architecture difference | 3.2 | percentage points | 48.3 − 45.1 | Analyst-derived | p. 8 |

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| The benchmark targets cognitively demanding chores | Manual construction, memory/calculation categories, 532 tasks | X1; Figs. 1–3 | pp. 1–6 | HIGH for design description; practical representativeness is not exhaustively established. |
| Current evaluated agents struggle | GPT-4o 3.4–6.8%; GPT-5 45.1–48.3% overall | Table 1, X1 | p. 8 | HIGH for tested configurations; no universal claim about all agents. |
| Architecture is associated with category performance | Different strengths across three paired model panels | Fig. 4, X3 | p. 8 | HIGH descriptive evidence; MEDIUM for memory-specific causal explanation. |
| Navigation success is insufficient for completion | High checkpoint rates coexist with low full scores | Table B, X8 | p. 18 | HIGH for measured distinction; checkpoints are coarse. |
| Fuzzy-match judgments mostly agree with humans | 70/72 agreement | X9 | pp. 18–19 | HIGH for reviewed instances; limited scoring subset. |
| Reasoning settings matter | Higher settings outperform lower settings in all displayed categories | Table D, X11 | p. 19 | HIGH for table; 102-task subset, no uncertainty estimates. |
| Optional memory/calculation tools do not consistently improve scores | Mixed scratchpad changes; calculator results largely unchanged | Tables F–G, X13–X14 | p. 20 | MEDIUM owing to adoption confounding and Table G layout. |
| Controlled environments trade coverage for diagnosis | Explicit author limitation | §7 | p. 10 | HIGH as an acknowledged boundary. |
| WebChoreArena reveals progress in the selected comparison | Orange curves rise across three BrowserGym models | Fig. 5, X4 | p. 9 | HIGH for plotted pattern; broader benchmark reliability is not formally measured. |
| The work is indirectly relevant to security | Observation, memory, browser actions, cross-site context | Table H; §E.4 | pp. 21, 24–25 | D: MEDIUM for identifying study components; LOW for extrapolating comparative vulnerability. |
| Agents are more vulnerable than standalone LLMs | No matching comparison or adversarial experiment | None | Whole supplied paper | UNKNOWN; unsupported by this paper. |

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking a computer assistant to examine hundreds of online entries, remember details from many pages, apply several rules, and calculate the correct answer. Getting to the right website is only the beginning. The assistant must also avoid skipping items, forgetting restrictions, repeating work, and making mistakes with its notes.

The researchers built 532 jobs like this inside four controlled websites. Even strong tested agents completed fewer than half overall. People also found the tasks difficult, although the human test used one example from each task template rather than every task. One useful discovery was that an agent could often reach the right page while still failing the actual job.

The paper helps us understand the moving parts of web agents: what they see, what they remember, and what browser actions they take. Those moving parts could matter in a security investigation. But this study did not put malicious instructions on pages or compare attacked agents with standalone language models. It shows that reliable browsing work is hard; it does not prove that web agents are more vulnerable to attackers.

## Completeness Audit

The denominator is the supplied 29-page paper, including its appendices and all identified figures and tables. 'Fully represented' below means the substantive function and available evidence are represented, not that every source word is reproduced. Visual inspection and extracted-text inspection remain explicitly separate.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue | Yes | Yes | Represented in compressed form | Full author list appears below; COLM 2026 is source-reported. |
| Abstract | Text and image | Yes | Fully represented | Motivation, benchmark, dimensions, compatibility, headline result. |
| §1 Introduction | Text and images | Yes | Fully represented | Problem, chore definition, contributions, findings. |
| §2 Related Work | Text and images | Yes | Represented in compressed form | Two major categories and principal comparisons preserved. |
| §3.1 Rationale | Text and image | Yes | Fully represented | Controlled versus changing sites. |
| §3.2 Overview | Text and image | Yes | Fully represented | All domain task counts. |
| §3.3 Statistics | Text and images | Yes | Fully represented | Categories, overlap, modality allocation. |
| §3.4 Construction | Text and images | Yes | Fully represented | Annotators, templates, refinement, effort. |
| §3.5 Evaluation | Text only | Yes | Fully represented | Three evaluator families and textual subtypes. |
| §4.1 Formulation | Text only | Yes | Fully represented | Tuple, transition, sequential loop, unspecified components. |
| §4.2 Baselines | Text only | Yes | Fully represented | Selection rationale and agent scope. |
| §5.1 Main results | Text and image | Yes | Fully represented | Complete Table 1 and human qualifications. |
| §5.2 Analysis | Text and image | Yes | Fully represented | Benchmark comparison and other agents. |
| §6 Conclusion | Text and partial image | Yes | Represented in compressed form | Benchmark contribution and saturation motivation. |
| §7 Limitations | Text only | Yes | Fully represented | All three named limitations. |
| Acknowledgments | Text only | Yes | Represented in compressed form | Funding is secondary; details stated below. |
| References | Text; p. 12 image | Yes | Represented in compressed form | Used only for author positioning; no citation validation. |
| Appendix A | Text only | Yes | Fully represented | Writing assistance and manual benchmark disclosure below. |
| Appendix B.1 | Text only | Yes | Fully represented | Selection, counts, evaluator issues, approximate denominator. |
| Appendix B.2 | Text only | Yes | Fully represented | Access failure, limited operations, query sensitivity, parametric knowledge concern. |
| Appendix C.1 | Text only | Yes | Fully represented | Single/multiple labels and all Fig. A percentages. |
| Appendix C.2 | Text and image | Yes | Fully represented | Text/image asymmetry and required inputs. |
| Appendix C.3.1 | Text and partial image | Yes | Fully represented | Four failure categories; calculation detail below. |
| Appendices C.3.2–C.3.5 | Text only | Yes | Represented in compressed form | All eight case diagnoses retained; long task wording compressed. |
| Appendices D.1–D.7 | Text only | Yes | Fully represented | All seven analyses and numerical conditions covered. |
| Appendices E.1.1–E.1.3 | Text and images | Yes | Fully represented | Actions, budgets, selection and failed attempts. |
| Appendix E.2 | Text and partial image | Yes | Fully represented | All reported model settings preserved. |
| Appendices E.3.1–E.3.2 | Text only | Yes | Represented in compressed form | Website tips grouped; prompt examples and omissions explained. |
| Appendix E.4 | Text and image | Yes | Fully represented | Both memory mechanisms and causal qualification. |
| Explicit benchmark question | Yes | Yes | Fully represented | No invented formal question set. |
| Formal hypotheses | No item found | Yes | No such item identified | No formal hypotheses presented. |
| Experiments X1–X15 | Yes | Yes | Fully represented | Separate conditions retained. |
| Figures 1–5 | Visually and textually | Yes | Fully represented | All substantive panels accounted for. |
| Figure A | Text only | Yes | Represented in compressed form | Graphic appearance unverified. |
| Figure B | Visually and textually | Yes | Fully represented | Both modality cases. |
| Figures C–F | Text only | Yes | Represented in compressed form | Source itself omits portions. |
| Tables 1, 2, A, H, I | Visually and textually | Yes | Fully represented | Values/action contents preserved. |
| Tables B–F | Text only | Yes | Fully represented | Numerical rows represented. |
| Table G | Text only | Yes | Uncertain | Raw values retained; header mapping qualified. |
| Major mathematical formulation | Text only | Yes | Fully represented | No rendered typography inspection. |
| Algorithms/theorems/proofs | No item found | Yes | No such item identified | No numbered formal objects supplied. |
| Major contributions | Yes | Yes | Fully represented | Concept, benchmark, diagnostics, empirical work. |
| Author-stated limitations | Yes | Yes | Fully represented | Dedicated limitations and practical constraints distinguished. |
| Separate supplementary files | None supplied | Not applicable | Missing from supplied material | No detected supplementary references establish a specific missing supplement. |
| Project website/code/live leaderboard | References only | Boundary stated | Inaccessible under supplied-only analysis | No artifact inspection claimed. |

**Additional inspected details preserved for coverage.** The full title is *WebChoreArena: Evaluating Web Browsing Agents on Realistic Tedious Web Tasks*. Authors are Atsuyuki Miyai, Zaiying Zhao, Kazuki Egashira, Atsuki Sato, Tatsumi Sunada, Shota Onohara, Hiromasa Yamanishi, Mashiro Toyooka, Kunato Nishina, Ryoma Maeda, Kiyoharu Aizawa, and Toshihiko Yamasaki, affiliated with The University of Tokyo. The paper labels itself a COLM 2026 conference paper. Appendix A says LLMs assisted writing polish with author review and revision, while benchmark construction was manual; LLMs also ran the evaluated agents. Acknowledgments identify JST BOOST JPMJBS2418, JST ASPIRE JPMJAP2303, and the Institute for AI and Beyond at The University of Tokyo.

The map exclusion includes unavailable search results since April 2025, restricted location-search and route operations, brittle amenity-query syntax, sensitivity to abbreviations and visible map region, and concern that agents sometimes answer from parametric knowledge rather than browsing. Appendix C's calculation discussion says GPT-5 made few calculation mistakes, including one error at the second decimal place when averaging across more than 100 categories; Gemini made mistakes more often when adding or multiplying more than fifteen numbers. These are qualitative author observations with illustrative quantities, not controlled arithmetic accuracy curves.

### Missing or inaccessible material

No physical page is apparently missing from the supplied text. Original rendered pages outside the thirteen supplied images are unavailable for visual checking. The referenced project site, repositories, leaderboard, cited papers, complete execution records, and omitted prompt-example components were not inspected. No separate supplement was supplied, and no specific supplementary file is identified as definitely absent from an otherwise promised package.

### Uncertain interpretations

Table G's column alignment and tool-count convention remain uncertain. Figure A's visual arrangement is unknown. Small internal screenshot text in Figures 1 and 3 cannot all be read independently. Figure 5's unlabeled WebArena values are not given exact numerical estimates. The 20.0% WebArena issue figure is approximate relative to 134/684. Table I does not display AgentOccam despite a nearby broader comparison statement. No source evidence settles comparative adversarial vulnerability against standalone LLMs.

### Deliberately compressed material

Related-work descriptions and bibliography entries are grouped by their role rather than reproduced citation by citation. Website tips are summarized by functionality, while security-relevant mentions are explicitly qualified. Long product names, exact wording of eight failure tasks, and repeated prompt instructions are compressed; their operational purposes and diagnoses are preserved. Page headers, decorative logos, email address, repeated venue lines, and routine layout elements are non-substantive for the scientific analysis.

### Potential omissions

Every substantive section, named subsection, identified visual, table, major mathematical object, and distinct analysis in the supplied inventory is represented at the stated level. This does not imply word-for-word preservation or verification of unavailable artifacts. Remaining known coverage gaps are the visual and reporting uncertainties listed above. The paper cannot supply the requested standalone-LLM security comparison because that comparison is not part of its reported study.
