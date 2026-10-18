## Stage 0 — Document Accessibility Report

The supplied work is available as extracted text for physical PDF pages 1–48. The page sequence contains no apparent gap in the supplied text. This establishes coverage of the supplied 48-page document, not independent verification of the original PDF or its hash. Visual renderings are supplied for 41 pages: 1–10, 12, 17, 19–26, and 28–48. Pages 11, 13–16, 18, and 27 were inspected through supplied text only. All 27 numbered figures have supplied visual renderings, and all 23 numbered tables are represented in the supplied material. Equation (1) is visually available; Equation (2), on p. 18, is available as extracted text only. Appendix A through Appendix I are present. No separate supplementary files, executable code, evaluation traces, or interactive viewer were supplied. The project page and repository references were not accessed.

The main prose, table values, captions, and major mathematical expressions are readable. Some screenshot text and dense labels inside Figures 3, 7, 10, and 21–27 are small; their supplied captions and extracted text provide additional evidence. A caption or extracted screenshot label is not treated as independent visual confirmation of a tiny interface detail. No OCR or tools were used. The image-loading error included in the prompt does not prevent inspection of the images actually displayed. The supplied accessibility metadata reports native text on all pages; its automated appendix detection is not used as the document inventory, because the document itself explicitly identifies appendices A–I.

Evidence convention: [A] means author-reported; [B] means directly observable in supplied visuals; [C] means analyst-derived, with calculation shown; [D] means analyst interpretation. No external information [E] is introduced. Confidence is HIGH for clearly stated methods and readable tables, MEDIUM for methodological interpretations and small visual details, and UNKNOWN for unavailable implementation behavior or unresolved contradictions. Physical PDF page numbers are used throughout.

## 1. Plain-language orientation

This paper studies how to diagnose the behavior of artificial intelligence systems that operate websites. A web agent receives a task, looks at a browser, clicks, types, scrolls, and eventually tries to finish. A final pass/fail score says whether it succeeded, but can conceal very different problems. An agent might never find the right product, find it but miss the purchase button, or spend many unnecessary steps before succeeding. [A: pp. 1–2]

The researchers introduce WEBSTEP, a benchmark with 10 self-hosted websites and 1,800 synthetic tasks. Each website is driven by a deterministic semantic Markov Decision Process, or MDP: a structured model of the website's meaningful states and actions. The agent uses the interface, while the environment records what its actions actually changed and what information became available. This supplies an interpretable action history without manually labeling every trajectory. [A: pp. 2–4]

Six agents are evaluated. Their results show that similar overall success rates can conceal different exploration and execution weaknesses, that strengths vary by skill even within one website, and that failure patterns differ across agents. More demanding identification tasks expose larger performance differences. The central contribution is therefore diagnostic evaluation infrastructure and an empirical analysis of behavior, rather than a new agent training algorithm. [A: §§4.1–4.4]

For the user's question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,' this paper supplies indirect evidence about the complications introduced by multi-step interaction, partial information, interface grounding, and action execution. It does not experimentally compare web agents with standalone large language models, measure an adversary, or establish a comparative security vulnerability rate. Any security relevance below is explicitly analyst inference [D].

## 2. Document roadmap

The inventory contains five main sections: §1 Introduction, §2 Process-level evaluation via semantic MDP duals, §3 WEBSTEP, §4 Experiments and Results, and §5 Conclusion. Section 2 has §2.1 Semantic MDP and §2.2 Task and world generation. Section 4 has §4.1 Aggregate Results, §4.2 Skill-level diagnosis, §4.3 Trajectory bifurcations, and §4.4 Exploration success by task complexity. Ethics and Reproducibility statements follow the conclusion on p. 10. References occupy pp. 10–13; p. 14 is an appendix contents page.

Appendix A states limitations. Appendix B positions the work against benchmark, environment-modeling, intermediate-evaluation, and automated-judging approaches. Appendix C covers agent configurations, compute/runtime, protocol, coverage, reproducibility, and LLM usage. Appendix D gives task distribution, site screenshots, visibility partitions, and skill taxonomies. Appendix E explains construction, world generation, and oracle generation. Appendix F supplies detailed numerical results. Appendix G describes an artifact viewer. Appendix H contains task examples, agent/oracle comparisons, and all 10 website transition graphs. Appendix I contains seven qualitative cases.

The stable object inventory is Figures F1–F27, Tables T1–T23, Equations E1–E2, Algorithm ALG1, analyses X1–X4 corresponding to §§4.1–4.4, and cases I1–I7. There are no formal theorems, lemmas, or explicitly numbered research questions or hypotheses. Three explicit contributions appear on p. 2. The bibliography and repeated page headers are accounted for but compressed as reference material and repetitive formatting.

## 3. Background and context

A graphical user interface, or GUI, is the visible browser interface. Raw GUI actions are operations such as clicking a pixel coordinate or typing text. A semantic action represents the application-level meaning of those operations, such as opening a repository, starring a message, or submitting an issue. Several GUI operations can contribute to one semantic action, while a scroll or missed click may produce no meaningful state transition. [A: Fig. 2, pp. 2–3]

A trajectory is the ordered history of states and actions during a task. Terminal success evaluates the final outcome. Process-level evaluation asks what happened along the way. Exploration concerns locating the correct target and obtaining evidence; execution concerns completing the task after finding it. These are operational benchmark definitions, not direct measurements of private reasoning. [A: pp. 5, 15]

An MDP is the paper's structured model of states, actions, transitions, and task/environment configuration. 'Deterministic' means that the same modeled state and action produce the same next state. The benchmark has privileged access to this model; agents generally observe screenshots rather than receiving the semantic trace. Claude CUA is an important exception to a purely pixel-based comparison: its harness also receives interactive Document Object Model, or DOM, elements and can target reference identifiers. [A: pp. 3, 17]

An oracle trajectory is an author-generated reference strategy intended to complete a task efficiently. A hard negative is a plausible distractor that resembles the target under shallow evidence but differs on a decisive attribute. 'Commit' means a task-relative final action, which can be a purchase-like operation, starring a message, or simply opening the correct item for a read-only task. These terms must not be equated with malicious instructions or attacks: the benchmark's distractors test identification difficulty. [A: pp. 4, 22, 27]

## 4. Research problem and gap

The existing problem is diagnostic ambiguity: a binary outcome collapses an entire interaction into one result. According to the authors, previous benchmarks primarily report terminal success, sometimes with partial credit or manually defined intermediate nodes. Those results provide limited guidance about whether the agent failed to locate a target, collect decisive evidence, or execute an action. [A: pp. 1–2, 15–16]

The claimed gap is automatic, fine-grained process measurement grounded in the environment's own semantics. Manual milestones can be expensive and brittle; language-model judges introduce dependence on judge capability and stochasticity; terminal predicates alone do not explain the path to failure. WEBSTEP addresses this through co-development of a GUI and semantic model rather than post hoc interpretation of arbitrary websites. [A: Appendix B]

The scope is controlled, self-hosted replicas of familiar website categories with synthetic worlds and template-generated tasks. It is not a benchmark of live-web uncertainty, unrestricted computer use, sensitive authorization, or adversarial security. The novelty is positioned as built-in semantic instrumentation plus controlled task generation and diagnostic analyses. The paper's broad introductory language about existing benchmarks is qualified by its related-work discussion, which acknowledges prior intermediate-evaluation approaches. [A: pp. 4, 15–16]

## 5. Research questions / objectives / hypotheses

No formal numbered research questions or statistical hypotheses are stated. The explicit objectives are to introduce an instrumented benchmark, define a process-level framework, and show that agents with similar outcome scores exhibit different failure signatures. [A: p. 2]

The four analysis objectives are: X1, determine whether trajectory summaries reveal differences hidden by terminal scores; X2, identify skill-specific and temporal behavior; X3, localize divergence between successful and failing trajectories at shared states; and X4, examine performance under different exploration-complexity regimes. These restate the paper's organizing objectives rather than inventing formal hypotheses. [A: pp. 2, 5]

The user's security research question remains a separate synthesis objective. The paper can inform what to measure in a later security study, but it cannot directly answer whether web agents are more vulnerable than standalone LLMs. A security comparison would require a supplied comparator, defined attacker capabilities, and security outcomes, none of which this study provides. [D]

## 6. Assumptions / threat model

The system model assumes that task-relevant GUI behavior is generated from an explicit semantic state. Frontend actions dispatch into the model; transitions update state; an observation function resolves what is visible; rendering projects that observation back into the page. This construction supports exact recovery of modeled semantic trajectories. It does not imply a model of every real-world browser effect or every non-semantic interaction. [A: pp. 3, 25–26]

Worlds use fixed seeds, tasks are constructed with a unique satisfying target, and oracle trajectories are replayed against verifiers. Cross-website navigation and external search are disabled. Evaluation uses offline replicas, synthetic data, no real user accounts, and no production side effects. A 50-turn budget limits each episode. [A: pp. 4–5, 10, 17–19]

There is no security threat model: no attacker, protected asset taxonomy, injection channel, adversarial objective, poisoning capability, exfiltration mechanism, or defense evaluation is defined. The benchmark implementation, visibility rules, semantic logger, and verifier function as trusted measurement components [D]. Their correctness is supported by described testing, not independently audited here.

A notable measurement condition is Safe Pass: all reported terminal success rates use a policy that can count an episode as successful when the correct entity and sufficient evidence are reached even without the final commit. This is necessary context for interpreting every terminal number, and it differs from the simpler complete-the-action definition initially introduced in §4.1. [A: p. 18]

## 7. Methodology

### Benchmark and dataset

WEBSTEP contains Mail, Calendar, Team Chat, Shopping, Food Delivery, Accommodation, Housing, Coding Q&A, Code Repo, and Job Network. Each contributes 180 tasks, for 1,800 total. Table 4 reports 48 surfaces, 229 typed actions, 105 templates, and 84 card-visible versus 80 detail-only fields across sites. 'Surface' means a distinct view such as a list, detail page, or modal. These are evaluation tasks; no training/validation/test split or agent retraining is described. [A: pp. 20–22]

Templates combine a natural-language instruction with sampled constraints and a matching generated world. The generator creates a satisfying target, plants controlled confusable items, adds distinguishable fillers, and uses an integer seed. Directly named targets have zero planted hard negatives. Hard-negative count is a designed lower bound on discrimination effort, not a literal count of all detail inspections an agent or oracle must perform. [A: pp. 4, 27]

### Construction and implementation

Human-visible workflows on live reference sites supply screenshots and actions. The authors explicitly exclude backend code, API traffic, and other non-GUI signals from this grounding stage. Claude Opus 4.6 assists in producing formal specifications and implementations, with substantial human review and iteration. This construction-time use of live sites is distinct from offline benchmark evaluation. [A: pp. 19, 25]

The generated application contains state.js for initialization, transitions.js for pure state updates and preconditions, observations.js for visibility and derived values, world.js for seeded catalogs, and render.js for DOM rendering. Dispatch runs the transition, recomputes the observation, rerenders, and stores state and action history in localStorage. Minor non-semantic exceptions are acknowledged. [A: pp. 25–26]

Validation includes isolated MDP tests, Playwright GUI interaction checks, replay of every oracle trajectory in headless Chromium, and manual quality assurance using early runs. Tests check invalid actions, visibility, derived values, navigation, search/filter/sort behavior, interactability, GUI–MDP agreement, and final verifier satisfaction. These are author-described procedures; test receipts and code were not supplied. [A: pp. 26–27]

### Agents and configuration

Fara-7B uses vLLM, screenshots, coordinate function calls, three recent images, temperature 0, and 800 maximum tokens. UI-TARS-1.5-7B uses five images, temperature 0, 2,048 tokens, and coordinate Thought + Action output. GUI-Owl-1.5-8B uses four images, temperature 0, 2,048 tokens, and coordinate tool calls. Qwen3.5-122B-FP8 uses five images, temperature 0.7, 2,048 tokens, top-p 0.8, and top-k 20. OpenAI CUA is identified as GPT-5.4 using the OpenAI API and coordinate computer tools; image-window, temperature, and token settings are dashes. Claude CUA is claude-sonnet-4-6 using the Anthropic API, three recent screenshots plus DOM, and reference-based targeting with coordinate fallback; temperature and token settings are dashes. Dashes must not be interpreted as zeros. [A: Table 3, pp. 17, 19]

All use a 1440 × 900 viewport and at most 50 turns. The runner captures screenshots, URL, and conversation history, executes returned actions, and stops at completion, infeasibility, or the limit. GPU models run through vLLM on four NVIDIA H200 GPUs with 140 GB each, taking approximately 3–4 days across GPU-model evaluations. Each API agent completes within one day with eight workers. Exact software versions, blocking-period duration, total API costs, repetition counts, and quantitative run variance are not supplied. [A: pp. 17–19]

### Metrics and statistical reporting

Terminal SR is reported under Safe Pass. Exploration SR checks whether the last detail-visited entity before first commit is the target. Execution SR is terminal success conditional on successful exploration. Coverage is the fraction of benchmark-defined information constraints satisfied by commit time. GUI and semantic steps measure raw interaction and state-changing transitions; their ratio estimates interaction efficiency. [A: pp. 5, 18]

Coverage can receive search-mediated credit when a query includes the discriminating value, the target remains in results, and the relevant field is searched. Thus coverage does not require opening every detail page or checking every candidate. There are 226 tasks whose constraints are satisfied initially, so coverage cannot discriminate behavior on that subset. Skill invocation checks whether required skill categories occur, not whether the agent intended or successfully completed every underlying attempt. [A: pp. 7, 15, 18]

No significance tests, confidence levels, or numerical uncertainty estimates accompany the main tables. Figure 6 shows shaded regions and bar whiskers, but their statistical definition is not specified in the supplied caption or prose. The authors report low variance in repeated API runs without quantifying it. These limits constrain statistical conclusions. [A/B: pp. 9, 19]

## 8. Experiments / analyses

### X1 — Aggregate trajectory diagnosis

Purpose: distinguish agents whose final scores look similar. Setup: six agents on the 1,800-task benchmark, with the shared protocol and model-specific harnesses. Outcomes: terminal, exploration, conditional execution, information coverage, and step counts. Table 2 shows Fara, GUI-Owl, and UI-TARS at 35.7%, 34.4%, and 37.1% terminal SR, respectively, despite exploration rates of 47.3%, 43.3%, and 49.2%. Their execution rates are 75.0%, 78.6%, and 73.9%. UI-TARS explores more broadly but has lower conditional execution than GUI-Owl. Fara uses fewer steps and obtains less coverage. [A: pp. 5–6]

Caveats: terminal SR uses Safe Pass; aggregate metrics mix task families; model and harness differences are not experimentally separated; no formal uncertainty test is reported.

### X2 — Skill and temporal diagnosis

Purpose: locate differences within broad website scores. Required skills come from each oracle; observed skills come from agent traces. Figures 3–4 and Tables 13–15 show occurrence rates and temporal action-category flows. On Q&A, the authors report Claude ahead of OpenAI by 30.0 percentage points in Navigate invocation but behind by 6.7 points in Inspect. GUI-Owl has higher aggregate Filter invocation than UI-TARS, 94.0% versus 77.3%, while UI-TARS has higher Navigate invocation, 65.2% versus 58.1%. [A: pp. 7, 30–31]

Figure 4's Mail comparison shows OpenAI CUA beginning more consistently with Search and spending early steps gathering information, whereas Fara's initial categories are more dispersed and Commit appears earlier. The authors propose targeted training changes. No intervention is performed, and category occurrence must not be read as proven skill mastery. [A: p. 7]

### X3 — Shared-state bifurcation diagnosis

Purpose: identify where a failed and successful trajectory on the same task separate. The last shared semantic state defines the bifurcation point. Wrong branch compares different non-commit next actions; delayed commit examines a failing continuation when a successful trajectory would commit; premature commit examines missing successful continuation when the failing trajectory commits. Figure 5 reports action-category distributions. [A: p. 8]

Wrong-branch Inspect shares are 79%, 64%, 50%, 44%, 38%, and 33% for Claude, OpenAI, Qwen, Fara, GUI-Owl, and UI-TARS. GUI-Owl's Filter share is 31%; Fara and UI-TARS have Search shares of 30%. Delayed continuations for Fara and GUI-Owl are 48% Navigate, while OpenAI's are 64% Inspect and 32% Search. Premature-commit missing-action distributions are dominated by Inspect and Navigate; Search is 3% for Claude and 1% for OpenAI, versus 10–16% among the small agents. [A/B: Fig. 5]

Figure 5 labels different n values for each agent and category: wrong branch 145, 162, 1,136, 2,201, 2,095, 2,339; delayed commit 16, 18, 82, 275, 161, 203; premature commit 21, 29, 113, 153, 171, 99, in the preceding model order. Some counts exceed 1,800, so they cannot all mean unique task counts. The exact counting/pairing unit is insufficiently explained in the supplied description. The displayed percentages therefore should not be reported as failure probabilities per task. [B/D]

### X4 — Complexity-stratified exploration

Purpose: examine identification difficulty under hard-negative count, oracle length, and information-access category. Figure 6 and Tables 16–18 stratify existing benchmark tasks; they do not establish matched causal effects of changing one factor while holding all others fixed. [A/D]

For HN=1 to HN=3, Claude declines from 98.7% to 89.8%, OpenAI from 93.6% to 83.5%, Qwen from 78.2% to 51.4%, Fara from 64.1% to 32.8%, GUI-Owl from 43.6% to 32.3%, and UI-TARS from 53.8% to 37.3%. HN=0 tasks name targets directly and differ on other dimensions, so monotonicity is assessed only over HN≥1. [A: Table 16]

Longer oracle trajectories generally correlate with reduced exploration success, but Table 17 contains substantial reversals. For example, Qwen is 51.4% at length 7 and 68.2% at length 9. Detail-task rates are 88.3%, 85.8%, 59.4%, 38.9%, 35.2%, and 44.2% for Claude, OpenAI, Qwen, Fara, GUI-Owl, and UI-TARS. These results support differences under demanding evidence requirements, with task-composition and subgroup-size caveats. [A: p. 32]

## 9. Results

Table 2's complete aggregate numerical ledger is reproduced below. All percentage columns are author-reported; terminal success uses Safe Pass, execution is conditional on exploration, and step columns are reported aggregate step summaries.

| Agent | Terminal % | Exploration % | Execution % | Coverage % | GUI steps | Semantic steps | GUI/Semantic |
|---|---:|---:|---:|---:|---:|---:|---:|
| Fara-7B | 35.7 | 47.3 | 75.0 | 76.4 | 18.9 | 8.3 | 2.3 |
| GUI-Owl-1.5-8B | 34.4 | 43.3 | 78.6 | 79.5 | 28.3 | 10.4 | 2.7 |
| UI-TARS-1.5-7B | 37.1 | 49.2 | 73.9 | 80.3 | 35.0 | 14.0 | 2.5 |
| Qwen3.5-122B | 58.2 | 66.3 | 86.7 | 89.1 | 22.1 | 9.8 | 2.3 |
| OpenAI CUA | 82.7 | 89.4 | 92.4 | 96.8 | 19.7 | 10.0 | 2.0 |
| Claude CUA | 85.3 | 91.0 | 93.7 | 96.3 | 14.3 | 9.3 | 1.5 |

Finding 1 is supported by the small-model tradeoff: UI-TARS minus GUI-Owl is 49.2−43.3 = 5.9 percentage points in exploration and 73.9−78.6 = −4.7 points in execution [C, consistent with the authors' stated gaps]. The main text writes these gaps with percent signs; they compare rates directly and should be understood as percentage-point differences, not relative improvements.

Finding 2 is supported by opposite within-domain invocation rankings. The Q&A navigation difference of 30.0 points and inspection difference of −6.7 points are reported in the prose and Figure 3; rounded integer Tables 13–14 cannot reproduce every decimal exactly. Invocation is a behavior indicator, not proof of action correctness. [A]

Finding 3 is supported by agent-specific action mixes at shared-state divergence. Inspect is the most common wrong-branch category for every agent, but GUI-Owl has an unusually large Filter share and Fara/UI-TARS have larger Search shares. This is a comparative trajectory diagnosis, not an intervention proving the identified choice caused an irreversible failure. [A/D]

Finding 4 is supported most clearly by controlled-confusable and information-access strata. Analyst-derived relative HN=3 retention is 89.8/98.7 ≈ 91.0% for Claude and 83.5/93.6 ≈ 89.2% for OpenAI. The other models lose approximately 34.3%, 48.8%, 25.9%, and 30.7% relative to their respective HN=1 scores, calculated as (HN1−HN3)/HN1. These are relative changes, unlike percentage-point gaps. [C: Table 16]

Important less-prominent results include GUI-Owl's 95.8% conditional execution on Shopping despite only 13.3% exploration; UI-TARS's 17.4% conditional execution in Accommodation; Qwen's 100% conditional execution in Code Repo; and GUI-Owl's 96.2% Housing coverage despite 20.0% terminal SR. These show why high performance on one intermediate metric cannot establish overall task competence. [A: Tables 9–12]

## 10. Figure-by-figure interpretation

### Figure 1 — Different failures under the same outcome, p. 2

A screenshot sequence and three horizontal traces show a message-reaction task. Fara explores wrong people; UI-TARS loops around reactions and times out; GUI-Owl reaches the right thread but applies the wrong emoji. Red crosses indicate failures, and state/action sequences distinguish exploration from execution. There are no quantitative axes. It illustrates the diagnostic problem rather than estimating population frequencies. [A/B]

### Figure 2 — GUI-to-semantic measurement, p. 3

The top sequence shows repository screens and raw clicks, typing, and scrolling. An observer converts them to semantic actions. Lower panels report exploration, skill invocation, and efficiency: 10 GUI actions, five semantic transitions, and three oracle transitions. The target repository is found and starred, but issue creation is not completed. The arrows express the mapping from physical interaction to semantic measurement; they do not give the agent privileged semantic access. [A/B]

### Figure 3 — Pairwise skill profiles, p. 6

Small comparison plots group website-specific categories into strengths and weaknesses. Orange diamonds and teal downward triangles distinguish OpenAI and Claude; red squares and green upward triangles distinguish GUI-Owl and UI-TARS. Horizontal positions run from 0% to 100% invocation; website names and skill groups identify rows. Annotated signed gaps compare the paired agents. Q&A's +30.0 Navigate and −6.7 Inspect for Claude are central. The many rows are compressed; precise small labels are interpreted using supplied text, not guessed from marker positions. These are invocation comparisons, not security scores or significance annotations. [A/B]

### Figure 4 — Temporal skill flows, p. 7

Two alluvial-style diagrams compare OpenAI CUA and Fara on Mail/Compare Threads. Columns are successive steps; colored flows represent Search, Inspect, Navigate, and Commit. Flow widths and percentage labels represent action-category patterns rather than elapsed time. OpenAI has a concentrated Search beginning; Fara is more dispersed and commits earlier. Later flows are truncated with ellipses. This is a selected task-family illustration, not a complete sequence plot for every domain. [A/B]

### Figure 5 — Bifurcation types, p. 8

Top-row branch diagrams distinguish wrong non-commit choices, extra actions after a missed commit opportunity, and required actions omitted by early commitment. Three heatmaps below use action categories on the horizontal axis and agents on the vertical axis. Percentages and row n labels are printed; darker cells emphasize larger shares. There is no temporal or logarithmic axis. The figure supports different error signatures but leaves the exact n counting unit unclear. [A/B]

### Figure 6 — Exploration versus complexity, p. 9

Panel a plots exploration SR from 0 to 1 against HN counts 0–3. Panel b plots it against oracle lengths 1–10. Panel c groups bars by Card, Filter, and Detail. A shared model legend maps colors and markers to six agents. Shading and whiskers are visible, but their uncertainty definition is unavailable in the supplied explanation. Exact values are supplied by Tables 16–18, so no graphical estimates are necessary. HN≥1 trends decline consistently; length trends fluctuate; Detail particularly separates Qwen from the API agents. [A/B]

### Figure 7 — Task-distribution sunburst, p. 20

The inner ring contains 10 equally sized website sectors of 180 tasks. The outer ring divides sites into templates, with instance counts from four to 30. Colors associate template wedges with domains. Most template lists are deliberately compressed here; the figure establishes domain balance and unequal template frequency, not equal weighting of every task type. Table 4 supplies the 105-template total. [A/B]

### Figure 8 — Ten site interfaces, p. 21

Two rows show Mail, Calendar, Shopping, Accommodation, Food Delivery, Housing, Coding Q&A, Code Repo, Job Network, and Team Chat. These are visually recognizable domain-specific interface replicas. Small screenshot text is not needed to establish their layout variety. The visual does not independently validate functional equivalence to live products. [A/B/D]

### Figure 9 — Construction pipeline, p. 25

Workflow traces feed specification, implementation, and validation boxes. Human-review symbols accompany LLM assistance; validation contains automated checks and manual quality assurance. A return path indicates fixes to earlier stages. It is an iterative development architecture, not an evaluated agent's runtime loop. [A/B]

### Figure 10 — Artifact viewer, p. 33

The screenshot has a task list at left, screenshot replay centrally, metadata/actions at right, and semantic trajectory at the bottom. It demonstrates the proposed inspection interface. Tiny individual records are not reliably readable here, and no interactive execution was inspected. The caption and prose describe replay, oracle comparison, verifier conditions, and multi-agent batches. [A/B]

### Figures 11–20 — Per-site transition graphs, pp. 37–41

All 10 graphs were visually inspected. Blue outlined boxes are surfaces; solid directed arrows are inter-surface semantic actions; gray action lists joined by dashed connections represent within-surface operations. They have no numeric axes. F11 Mail connects ThreadList, ThreadView, and ComposeModal, reporting 36 actions: eight inter-surface and 28 intra-surface. F12 Calendar connects week/day/search/detail/editor views, reporting six surfaces and 14 actions, split 9/5; only five distinct surface boxes are clearly depicted, an unresolved completeness issue. F13 Shopping connects Home → SearchResults → ProductDetail → Cart → Checkout → OrderConfirm, with back paths and 23 actions split 8/15. F14 Accommodation connects search, listing, checkout, and reservations, with cancellation and 16 actions split 7/9.

F15 Food Delivery links restaurant list/detail, menu detail, cart, checkout, and status; 24 actions split 13/11. F16 Housing links search results, property detail, agent profile, and saved homes; 16 actions split 8/8. F17 Coding Q&A links question list/detail, tag page, and user profile; 18 actions split 12/6. F18 Code Repo branches from repository detail into issue and pull-request lists/details; 32 actions split 11/21. F19 Job Network branches from feed into jobs and connections, then profiles and messaging; 26 actions split 18/8. F20 Team Chat connects channel, search results, and direct message; 24 actions split 8/16. The drawings summarize topology and action families rather than enumerate every precondition, action parameter, or state variable. [A/B]

### Figure 21 — Same success, different browsing, p. 42

OpenAI and UI-TARS both star the correct Mail thread. The caption reports 14 versus three semantic actions. OpenAI searches sender information and expands several threads; UI-TARS directly searches the discriminating keyword. This supports different strategies, but a single case cannot establish model scale as the causal explanation. Extracted text includes stray material not evident as substantive visible task content; the visible figure and main caption are prioritized. [A/B/D]

### Figure 22 — Unverified early commitment, p. 43

Three screenshot/thought/action panels show UI-TARS selecting a dress, adding it to cart, and declaring completion without checking the warranty detail. The required warranty is two years; the rationale asserts that property without recorded verification. This is a benign-distractor failure example, not an attack demonstration. [A/B]

### Figure 23 — Thorough comparison, p. 44

Eight panels show UI-TARS checking three camping products and returning to the correct 0.3 lb item. Alternatives weigh 2.5 and 3.8 lb. The caption reports 100% coverage at commit and a pass. The figure illustrates evidence gathering; it does not establish that exhaustive comparison is necessary for every unique-target task. [A/B/D]

### Figure 24 — Correct target, missed action, p. 45

Two Fara cases show a failed upvote and failed repository star. Clicks at (150,157) and (1275,250) miss their intended controls. Exploration passes while execution fails. The screenshots and captions support coordinate grounding as the immediate illustrated problem, but the claim that it explains much of Fara's overall gap is not quantified here. [A/B]

### Figure 25 — Correct action mechanics, wrong target, p. 46

Six panels show Fara clicking a repository language label instead of the language filter, then sorting and starring. The interface operation succeeds on the wrong selected entity; the task fails. Its 'execution success' is a qualitative mechanics label, whereas Table 2's Execution SR is defined only conditional on successful exploration. These usages must be distinguished. [A/B]

### Figure 26 — Inefficiency despite passing, p. 47

A cart-management task compares nine oracle actions with 13 Fara actions. A highlighted segment contains six agent steps versus two oracle steps. Garbled queries and returning home precede recovery. The caption calls six highlighted steps 'extra,' but the net total difference is 13−9 = four [C]. The figure supports redundancy while leaving the wording of the six-step count ambiguous. [A/B]

### Figure 27 — Safety-related stopping, p. 48

Fara reaches a booking confirmation for a $485/night property, with 100% coverage, exploration pass, and HN=0, then issues Done at step 16 rather than continuing into personal/payment information. The caption says standard SR fails while Safe Pass accepts the allowed behavior. It demonstrates a scoring distinction and a guardrail-related stop, not an attacker bypass or evidence that refusing was unsafe. [A/B]

## 11. Table-by-table interpretation

All result percentages below are reported values without tabled confidence intervals or significance tests. Bold type marks a maximum, not statistical significance.

**T1, benchmark comparison, p. 4:** Rows compare eight prior benchmarks and WEBSTEP on deterministic hosting, task count, process evaluation, and hard negatives. Counts are 300, 643, 680, 214, 812, 910, 682, 542, and 1,800. WEBSTEP is the only row marked MDP process evaluation and controlled hard negatives; Mind2Web-Live has Key node evaluation. This is the authors' positioning, not an independently verified literature census.

**T2, aggregate evaluation, p. 5:** Fully reproduced in §9. Claude leads terminal, exploration, execution, and lowest GUI/semantic ratio; OpenAI has the highest coverage. Fara has the lowest coverage and fewest GUI steps among small agents. Lower step counts alone do not establish better behavior.

**T3, configurations, p. 17:** Model identifiers, input modality, backend, action format, context image count, temperatures, and token caps are preserved in §7. Claude's DOM access materially qualifies comparisons. Unspecified API settings remain unspecified.

**T4, site statistics, p. 22:** Per-site surface/action/template counts are Mail 3/36/6; Calendar 6/14/6; Team Chat 3/24/12; Shopping 6/23/6; Food 6/24/15; Accommodation 4/16/12; Housing 4/16/12; Q&A 4/18/12; Code 6/32/12; Jobs 6/26/12. Every site has 180 tasks. Totals are 48/229/105 and 1,800 tasks. The accompanying prose mentions state-variable counts, but the displayed table does not include that column.

**T5, visibility partition, p. 22:** Rows distinguish card, detail, and commit surfaces. Card/detail field counts are Mail 10/9, Calendar 8/6, Chat 6/5, Shopping 12/12, Food 8/7, Accommodation 9/8, Housing 8/10, Q&A 7/6, Code 9/8, and Jobs 7/9. Availability depends on surface, supporting the information-gap construction. Some naming differs from graph abbreviations, such as DirectMessageView versus DirectMessage.

**T6, skill definitions, p. 22:** Defines Navigate, Search, Filter, Inspect, and task-relative Commit. Pre-commit state modifications are merged into the following category for trajectory analyses. This grouping means category plots are not exhaustive separate classes for every application mutation.

**T7, taxonomy part 1, p. 23:** Lists Mail, Calendar, Shopping, Accommodation, and Food skills. It covers navigation/query/filter families, entity inspection and comparison, and completion-related actions such as replies, event edits, checkout, and bookings. These detailed lists are compressed rather than transcribed word for word.

**T8, taxonomy part 2, p. 24:** Lists Housing, Q&A, Code Repo, Job Network, and Team Chat. Distinctive operations include tours, voting, issue management, applications, connection requests, and message reactions. Team Chat has a dash for Filter. The taxonomy is a labeling framework, not a measurement of latent intentions.

**T9, terminal SR by site, p. 28:** Claude leads seven sites; OpenAI leads Accommodation at 88.3%, Q&A at 79.4%, and Jobs at 91.1%. Claude's other leading values are Mail 91.7%, Calendar 79.4%, Shopping 82.8%, Food 86.1%, Housing 79.4%, Code 91.1%, and Chat 93.3%. UI-TARS Accommodation is the lowest displayed terminal value, 8.9%. All terminal values inherit Safe Pass.

**T10, exploration SR by site, p. 28:** Claude leads nine sites; OpenAI leads Q&A, 89.4% versus Claude's 85.6%. Claude Shopping reaches 98.9%, while Fara Housing is 13.9%. GUI-Owl Jobs terminal SR of 35.6% in T9 exceeds exploration SR of 34.4%; this warns against assuming terminal success is always a strict subset of the operational exploration predicate under the reported policy.

**T11, conditional execution, p. 28:** Claude has 100% on Mail, Calendar, Code, and Chat. OpenAI and Qwen also have 100% on Code; GUI-Owl has 100% on Jobs. UI-TARS Accommodation is 17.4%, GUI-Owl Accommodation 24.4%, and Fara Chat 47.0%. Conditional denominators differ by agent and domain and are not tabulated.

**T12, coverage at commit, p. 29:** Claude reaches 100% in Shopping and Housing; OpenAI leads several other sites, including Q&A at 98.9%. Code coverage is 90.9% for both API agents, versus 68.8% Qwen, 53.9% Fara, 55.8% GUI-Owl, and 52.5% UI-TARS. Coverage concerns credited evidence, not guaranteed comprehension or correctness.

**T13, skill invocation part 1, p. 30:** Presents Claude, OpenAI, and Qwen by site and five skills. A dash means fewer than 20 required episodes, not necessarily absence of the skill. Rounded Q&A Navigate rates are 73/43/73 and Inspect rates 92/99/93, respectively. Qwen can have near-universal inspection yet substantially lower commit invocation, illustrating a completion bottleneck.

**T14, skill invocation part 2, p. 31:** Presents Fara, GUI-Owl, and UI-TARS. Fara Accommodation Commit is 6%, GUI-Owl 15%, and UI-TARS 3%. GUI-Owl Code Navigate is 10%, while UI-TARS is 42%. These detailed occurrence rates can expose contrasts hidden in terminal aggregates; they do not measure success of every attempted action.

**T15, aggregate invocation, p. 31:** In Search/Filter/Inspect/Navigate/Commit order, Claude is 92.9/87.8/97.1/80.9/88.3; OpenAI 94.5/78.9/97.2/79.7/83.8; Qwen 90.9/87.2/95.5/76.3/58.5; Fara 80.4/70.9/82.8/60.3/29.4; GUI-Owl 83.3/94.0/78.6/58.1/39.7; UI-TARS 90.5/77.3/82.9/65.2/27.7. OpenAI leads Search and Inspect, GUI-Owl Filter, and Claude Navigate and Commit.

**T16, hard negatives, p. 32:** HN=0/1/2/3 rows are Claude 90.6/98.7/90.3/89.8; OpenAI 91.7/93.6/87.9/83.5; Qwen 76.4/78.2/65.2/51.4; Fara 60.5/64.1/41.9/32.8; GUI-Owl 59.4/43.6/34.5/32.3; UI-TARS 60.6/53.8/45.6/37.3. OpenAI leads HN=0 and Claude HN≥1. Read monotonic decline only over HN≥1.

**T17, oracle length, p. 32:** Lengths 1–10 show an overall difficulty trend with reversals. OpenAI leads lengths 2–4 at 96.7%, 92.9%, and 94.7%; Claude leads lengths 1 and 5–10. At length 10, scores are 85.9, 73.2, 45.1, 40.8, 35.2, and 38.0 in Claude/OpenAI/Qwen/Fara/GUI-Owl/UI-TARS order. Intermediate cells are compressed; non-monotonicity is retained.

**T18, information access, p. 32:** Card/Filter/Detail values are Claude 95.1/98.2/88.3; OpenAI 93.2/96.7/85.8; Qwen 70.4/90.1/59.4; Fara 58.6/72.8/38.9; GUI-Owl 60.5/65.0/35.2; UI-TARS 61.7/61.4/44.2. Detail means a nonempty information gap; Filter has no detail gap but uses search/filter/sort in the oracle; Card is list-solvable. These are task categories, not a guaranteed ordinal progression within each agent.

**T19, Mail template, p. 34:** The example asks for a Priya Patel email mentioning ProjectAlpha006. Target THR-006 has distractors THR-019 and THR-050; the reference uses seven steps. The schema lists body/cc/attachments as detail-only information and three constraints. This example underlies the oracle-shortcut inconsistency discussed below.

**T20, Shopping template, p. 34:** The example asks for fiction in Books with Material Leather. Target PRD-039 is Apple Essential Biography, $12.90, rating 4.7; the reference Search → OpenProduct → AddToCart has three steps. Template constraint count ranges 1–3. These synthetic product attributes are task data, not real-world product claims.

**T21, Accommodation template, p. 35:** A cheapest Chicago cabin with Pool for three guests, April 15–19, targets LST-011. Four to six constraints and seven oracle actions combine search, filtering, sorting, inspection, booking setup, and confirmation.

**T22, Mail trace comparison, p. 35:** The seven-action oracle inspects two distractors before the target. Fara succeeds in four actions and UI-TARS in three via keyword search. The caption calls their information insufficient, whereas coverage rules can credit discriminating search and the agents succeed. The exact case coverage is not given.

**T23, Shopping trace comparison, p. 35:** The three-action reference succeeds; Fara takes eight actions and adds a wrong product; UI-TARS takes six and stalls while reformulating searches and filters. This separates wrong-target commitment from non-progress. Detailed repeated query strings are compressed.

## 12. Diagram / architecture interpretation

The runtime architecture has two linked paths. The agent path is observation → model action → browser interaction → next observation. The semantic path is dispatch → checked transition → updated state → visibility-resolved observation → rendered interface, with persistent state/action logging. The evaluator subsequently derives target visits, coverage, skill categories, and verifier outcomes. This separation explains how low-level actions can be measured at application level without providing the agent the evaluator's state. [A: F2, pp. 25–26]

The construction architecture in F9 and ALG1 starts with user-visible workflows, specifies entities and navigation, builds state/action/observation contracts, implements a site, and validates it. Failure of validation returns development to an earlier stage. It is human-reviewed and iterative, so 'automatic process evaluation' does not mean benchmark creation was free of human labor. [A]

The transition graphs F11–F20 illustrate both movement between views and actions that stay within a view. A product can be opened before being added to a cart, and cart/checkout steps form dependencies; a repository branches into issue or pull-request workflows. These structures matter because a single final result can arise through different paths, and an action may reveal evidence without changing the selected target. The diagrams are compressed architecture summaries, not complete executable specifications. [A/D]

## 13. Equations and mathematical concepts

**Semantic MDP, §2.1, p. 3:** M = (S, A, T, ρ₀). S is structured semantic state; A is typed semantic actions; T maps state/action pairs to their next state; ρ₀ is described as task and environment configurations. The source does not explicitly define ρ₀ as a conventional initial-state probability distribution, so that meaning is not imposed. A state s = (sᵖ, sⁱ) separates position/interface settings from revealed item information.

**Equation (1), p. 3:** τ = (s₀, a₀, s₁, a₁, …, s_T), with s_{t+1} = T(s_t, a_t). The first expression is an ordered trace, not an objective function. The second is deterministic state evolution. The symbol T is overloaded as both transition function and final trace index in the printed notation; context distinguishes them. Inputs are a current state and action; output is the next state. This trace supplies the measurement substrate for all analyses.

**Exploration predicate, p. 5:** V_c = (v₁, …, v_k) lists items visited on detail surfaces before first commit. Exploration succeeds iff v_k = e*. Here e* is the correct entity. This is narrower than 'has ever found the target' and does not directly certify all evidence was understood. Behavior when the visited sequence is empty is not formally specified in the supplied definition, which matters for list-level commitments or search shortcuts.

**Skill invocation, pp. 6–7:** S* is the set of skill types in the oracle and S the set in the model trace. For required k ∈ S*, invocation means k ∈ S. These S symbols denote skill sets here, unlike the MDP state space earlier. Set membership ignores multiplicity, timing, and success; separate temporal analysis adds sequencing information.

**Equation (2), p. 18:** COV_t = |{c ∈ C : sat(c,t)}| / |C|. C = {c₁,…,c_K} is a declaratively generated set of information constraints. sat(c,t) means that accumulated observations satisfy c by step t; vertical bars count set members. The output is the fraction of constraints credited, reported at first terminal action t_commit. Constraints are calibrated to the oracle and described as an upper bound on useful evidence, while successful shortcuts can observe less. Handling an empty constraint set is not specified. The equation measures credited availability, not latent comprehension.

**Efficiency ratio, p. 5:** GUI steps divided by semantic steps is the reported measure; a lower ratio means fewer physical operations per modeled state change. No loss function, optimization training objective, theorem, or mathematical proof is supplied. Ratios from rounded aggregate counts need not reproduce every printed ratio exactly.

## 14. Interpretation and discussion

The strongest supported conclusion is that outcome and process metrics answer different questions. Outcome tells whether a benchmark policy accepts the result. Process metrics distinguish target identification, evidence acquisition, action-category occurrence, and completion mechanics. Their joint use is more informative than treating any one intermediate number as competence. [A/D]

X1 answers the first objective through small-agent exploration/execution tradeoffs. X2 answers the second through opposing skill rankings and temporal patterns. X3 answers the third through shared-state divergence signatures. X4 answers the fourth through harder evidence requirements and HN≥1 degradation. There are no formal hypotheses to declare statistically accepted or rejected. [A]

Several unresolved consistency issues materially qualify interpretation. First, §4.1 describes terminal success as completing the final action, but Appendix C.3 says every reported terminal rate uses Safe Pass without necessarily issuing that action. Second, the oracle is described as minimal and optimal, yet T22 shows successful four- and three-action paths against a seven-action oracle. This may reflect optimality under a prescribed comparison plan, but the paper does not clearly limit its global wording that way. Third, T22 describes keyword shortcuts as insufficiently informed, while Appendix C.4 explicitly permits search-based evidence credit. The case-specific constraint ledger is absent, so the apparent tension cannot be fully resolved.

Fourth, F26 has 13 versus nine total actions while describing six highlighted steps as extra. A six-versus-two segment accounts for four net extra actions, but that explanation is analyst interpretation, not an explicit caption correction. Fifth, the main-text claim of relatively similar Card-task performance is qualitative: Table 18 still spans 58.6–95.1%, a derived 36.5-point range. Sixth, length-based degradation is general rather than monotonic. Seventh, Figure 12 states six Calendar surfaces but depicts five identifiable boxes; T5 additionally names MonthView. Eighth, p. 19 points to Section B.1 for Table 3 although its location is C.1. Ninth, §D.3 mentions state-variable counts in T4, but the table lacks such a column. None is silently repaired here.

For security research [D], the paper suggests separating errors of information selection, evidence checking, interface grounding, and authorized action completion. A web agent's outputs can alter persistent application state, making behavioral diagnosis relevant to security consequences. However, susceptibility to benign confusables is not equivalent to prompt-injection susceptibility, and the demonstrated safety refusal is not a vulnerability. No comparative security conclusion about standalone LLMs follows from these experiments.

## 15. Contributions and novelty

**Conceptual:** Treating the trajectory as an object of evaluation rather than reducing it to a binary endpoint. **Methodological:** Separating exploration, conditional execution, evidence coverage, invocation, temporal patterns, and shared-state divergence. **Benchmark/dataset:** Ten websites, 1,800 seeded tasks, 105 templates, and controlled confusables. **System/implementation:** Co-developed semantic models and GUI renderers with persistent traces, validation, and an inspection viewer. **Empirical:** Six-agent evidence that similar terminal rates conceal different behaviors and that complexity strata reveal additional differences. [A]

The paper does not contribute a new standalone language model, a training method validated by intervention, a security exploit, a defense, or a theoretical guarantee of real-world robustness. Oracle solvability and determinism claims are scoped to constructed environments. Novelty relative to prior literature is the authors' positioning; the supplied paper alone cannot independently establish exhaustive priority. [D]

## 16. Limitations

### Authors' stated limitations

Appendix A explicitly identifies six limitations. Semantic abstraction excludes dynamic updates, session-dependent behavior, asynchronous loading, personalization, and third-party integrations. Domain coverage excludes sensitive data handling, complex authorization, and rich media. Synthetic data can miss natural long tails, correlations, and temporal drift. Templates do not reproduce ambiguous, underspecified, or open-ended user requests. Skill invocation is measured instead of latent-intent-dependent skill success. Interaction scope focuses on clicking, typing, and scrolling, excluding drag-and-drop, shortcuts, and direct URL navigation. [A: p. 15]

The reproducibility statements additionally acknowledge model-side stochasticity and API variation. Coverage is non-discriminative for 226 initially satisfied tasks, and users should not interpret its constraint set as evidence every successful strategy must explicitly gather. These are author-disclosed qualifications outside Appendix A. [A: pp. 10, 18–19]

### Additional evidence-based analyst observations

[D] The DOM-augmented Claude harness prevents attributing all differences to underlying model capability. Safe Pass changes the outcome construct and needs implementation-level rules to distinguish refusals, omissions, and misses consistently. Oracle minimality is not supported uniformly by supplied examples. Pairing/counting units for bifurcation n values and subgroup sizes for complexity analyses are unclear. No supplied code, trace ledger, or test receipts allow independent validation. Qualitative cases are selected examples, and confidence intervals, significance tests, and quantified repetition variance are absent or undefined. Security generalization is especially limited because attackers and standalone-LLM comparators are absent.

## 17. Threats to validity

These validity labels are analyst organization [D], not claims that the authors use the same taxonomy. **Internal validity:** model, input modality, harness, decoding, and context differences jointly affect results; complexity strata may differ on multiple dimensions. **Construct validity:** last visited target, search-mediated evidence credit, invocation, and Safe Pass are operational proxies with boundary cases; none directly reveals internal reasoning. **Statistical conclusion validity:** missing denominator detail and uncertainty definitions limit precision about differences, especially small bifurcation groups.

**External/ecological validity:** deterministic replicas and synthetic templates simplify live websites, user ambiguity, temporal change, and integrations. **Reproducibility:** fixed seeds and deterministic transitions reproduce environments conditional on actions, while stochastic decoding and server-side behavior can change actions. Release is promised in future tense; availability was not verified. **Security validity:** no attack success, unauthorized-action, leakage, or standalone-model measurements exist, so the work cannot establish comparative vulnerability or defense effectiveness.

## 18. Future work and open questions

**A. Explicit author proposals:** The authors hope WEBSTEP supports deeper diagnosis, propose inspection-focused training examples for identified weaknesses, suggest more consistent initial skill sequences and delayed commitment for Fara, and promise release of website implementations, tasks, seeds, oracle traces, metric scripts, evaluation suite, and viewer. These are proposals or commitments, not completed intervention results. [A: pp. 7, 10, 19, 33]

**B. Analyst open questions:** Would training based on these diagnoses improve held-out behavior? How do results change with matched pixel-only and DOM-assisted harnesses? What is the exact Safe Pass acceptance logic? Can reference strategies be optimized over permitted search shortcuts? How are empty detail-visit histories classified? What do Figure 5 counts and Figure 6 error displays represent? Do patterns persist under live dynamics and ambiguous tasks? For security specifically, do adversarially supplied pages change entry, evidence checking, commitment, and recovery differently from benign confusables, and how would a matched standalone-LLM comparison be designed? These are unanswered questions, not findings. [D]

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning |
|---|---|
| WEBSTEP | The paper's instrumented website benchmark. |
| LLM | Large language model; the paper evaluates LLM-based agent systems. |
| GUI | Graphical user interface: visible browser controls and content. |
| DOM | Document Object Model; Claude's harness receives interactive element information. |
| CUA | Computer-Use Agent, the label used for the API agents. |
| MDP | Markov Decision Process: the structured environment model. |
| Semantic MDP dual | A website's paired model of meaningful state and actions. |
| S, A, T, ρ₀ | State space, action space, transition function, task/environment configuration. |
| sᵖ, sⁱ | Positional/interface state and revealed informational state. |
| τ | Ordered state/action trajectory. |
| Surface | A distinct interface view, such as list, detail, or modal. |
| Target e* | The entity satisfying the task conditions. |
| Hard negative / HN | A plausible confusable differing on a decisive attribute. |
| Oracle | A generated reference action sequence; claimed optimality has noted caveats. |
| Commit | Task-relative final completing action. |
| SR | Success rate under the stated metric and policy. |
| Safe Pass | Acceptance at a sufficiently informed correct decision point without final commit. |
| Invocation | Occurrence of a required skill category, not per-attempt success. |
| C, sat(c,t), COV_t | Information constraints, satisfaction by time t, and satisfied fraction. |
| Bifurcation | Last shared state before selected successful/failing traces diverge. |
| Wrong branch | Different non-commit next actions. |
| Delayed commit | Failed trace continues where successful trace commits. |
| Premature commit | Failed trace commits where successful trace continues. |
| FP8 | The quantization label reported for Qwen; not further defined in supplied text. |
| vLLM | Named serving backend; its internals are not explained by the paper. |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Benchmark | 1,800 | tasks | 10 sites, 180 each | Author-reported | pp. 2, 20 |
| Templates / actions / surfaces | 105 / 229 / 48 | counts | All sites | Author-reported | T4, p. 22 |
| Episode limit | 50 | turns | All agents | Author-reported | p. 17 |
| Viewport | 1440 × 900 | pixels | Shared browser | Author-reported | p. 17 |
| Initial complete coverage | 226 | tasks | Coverage non-discriminative | Author-reported | p. 18 |
| Claude terminal SR | 85.3 | % | Safe Pass | Author-reported | T2, p. 5 |
| OpenAI terminal SR | 82.7 | % | Safe Pass | Author-reported | T2, p. 5 |
| Small-agent terminal SR | 35.7 / 34.4 / 37.1 | % | Fara / GUI-Owl / UI-TARS; Safe Pass | Author-reported | T2 |
| UI-TARS vs GUI-Owl exploration | 49.2−43.3 = 5.9 | percentage points | Same benchmark | Analyst-derived | T2 |
| UI-TARS vs GUI-Owl execution | 73.9−78.6 = −4.7 | percentage points | Conditional on exploration | Analyst-derived | T2 |
| Q&A Claude–OpenAI Navigate | +30.0 | percentage points | Invocation gap | Author-reported | p. 7, F3 |
| Q&A Claude–OpenAI Inspect | −6.7 | percentage points | Invocation gap | Author-reported | p. 7, F3 |
| GUI-Owl wrong-branch Filter | 31 | % | Bifurcation action distribution | Visually readable | F5, p. 8 |
| Claude HN1 → HN3 | 98.7 → 89.8 | % | Exploration SR | Author-reported | T16 |
| OpenAI HN1 → HN3 | 93.6 → 83.5 | % | Exploration SR | Author-reported | T16 |
| Claude relative retention | 89.8/98.7 ≈ 91.0 | % | HN3 relative to HN1 | Analyst-derived | T16 |
| Detail exploration | 88.3 / 85.8 / 59.4 | % | Claude / OpenAI / Qwen | Author-reported | T18 |
| Fara redundant trace | 13−9 = 4 | net actions | Agent versus reference | Analyst-derived | F26 |
| GPU resources | 4 × 140 | GB GPU memory | Four H200 GPUs | Author-reported | p. 17 |
| GPU-model runtime | approximately 3–4 | days | Full evaluation across GPU models | Author-reported | p. 17 |

No approximate plot estimates are needed because corresponding numerical tables are supplied. Values above retain metric conditions; percentages and percentage-point differences are explicitly separated.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Semantic instrumentation enables automatic process analysis | GUI rendered from semantic model; dispatch and logging architecture | F2, F9, ALG1 | pp. 3, 25–26 | HIGH as described design; implementation untested here |
| Similar terminal scores hide different behavior | Small-model exploration/execution tradeoff | T2, X1 | pp. 5–6 | HIGH descriptive evidence; Safe Pass applies |
| Weaknesses can be skill-specific | Opposite Q&A Navigate/Inspect differences | F3, T13, X2 | pp. 7, 30 | HIGH for invocation; not latent skill success |
| Failure signatures differ | Wrong-branch and continuation action distributions | F5, X3 | pp. 8–9 | HIGH for displayed shares; counting unit unclear |
| Confusables increase difficulty | All HN1–HN3 exploration rows decline | F6a, T16, X4 | pp. 9, 32 | HIGH descriptive evidence; subgroup composition unspecified |
| Detailed evidence separates agents | Detail SR 88.3/85.8/59.4 for top three | F6c, T18 | pp. 10, 32 | HIGH; no causal matching or uncertainty test |
| All terminal SR uses Safe Pass | Explicit protocol statement | C.3 | p. 18 | HIGH; modifies main-text metric reading |
| Realism and action scope are limited | Explicit six-part limitation discussion | Appendix A | p. 15 | HIGH author disclosure |
| Safety stopping can be distinguished from competence failure | Correct booking decision followed by refusal | F27, I7 | p. 48 | HIGH for selected case; no prevalence estimate |
| Relevance to security is indirect | Interaction/evidence/action failure mechanisms, no adversary or standalone baseline | Overall design | pp. 1–5, 15, 48 | MEDIUM analyst inference; no comparative security claim |

## 22. Very simple explanation — Explain Like I'm 15

Imagine grading someone who uses an unfamiliar shopping website. A simple grade says only whether the right item ended up in the cart. But that misses the explanation: perhaps they never found it, perhaps they found it and clicked the wrong button, or perhaps they succeeded after wasting a lot of time. This paper builds websites that keep a clear record of those meaningful events.

The researchers test six AI agents on 1,800 tasks. Some agents get similar final grades while making different kinds of mistakes. One searches more effectively but struggles to finish actions; another applies filters well but navigates poorly. When products or messages look similar until you inspect their details, the weaker agents have more trouble. The tracking system makes those differences visible.

For security, this suggests useful questions about how an agent chooses information and turns it into actions. But this paper does not show that web agents are more vulnerable than a chatbot, and it does not test hackers or malicious instructions. Its contribution is a way to see where behavior goes wrong. It also shows that stopping for a safety rule can look like failure under a simple score even when the agent reached the correct decision.

## Completeness Audit

The denominator is the supplied document inventory: five main sections with their substantive subsections, two statements, appendices A–I and their subsections, four quantitative analyses, seven cases, 27 figures, 23 tables, two equations, one algorithm, three contributions, and six explicit Appendix A limitations. 'Represented in compressed form' means the object was inspected and its substantive function and important findings retained, while repeated labels or complete cell-by-cell transcription were reduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, abstract | Yes | Yes | Fully represented | Bibliographic details below; abstract claims integrated |
| §1 Introduction | Text + visual | Yes | Fully represented | Problem and diagnostic motivation |
| §2; §§2.1–2.2 | Text + visual | Yes | Fully represented | MDP, coupling, generation, equations |
| §3 WEBSTEP | Text + visual | Yes | Fully represented | Domains and construction |
| §4.1 / X1 | Text + visual | Yes | Fully represented | Complete aggregate table retained |
| §4.2 / X2 | Text + visual | Yes | Fully represented | Skills, timing, footnote caveat |
| §4.3 / X3 | Text + visual | Yes | Fully represented | Three bifurcation types and n ambiguity |
| §4.4 / X4 | Text + visual | Yes | Fully represented | Three complexity axes and caveats |
| §5 Conclusion | Text + visual | Yes | Fully represented | Diagnostic contribution |
| Ethics / Reproducibility | Text + visual | Yes | Fully represented | Offline synthetic setting; release and nondeterminism |
| Explicit research questions / hypotheses | Yes | Yes | No formal items stated | Informal objectives preserved |
| Three contributions | Yes | Yes | Fully represented | Benchmark, framework, empirical diagnosis |
| Appendix A, six limitations | Text only | Yes | Fully represented | Each limitation separately identified |
| Appendix B | Text only | Yes | Represented in compressed form | All four related-work categories covered |
| C.1 configurations | Text + visual | Yes | Fully represented | Model/harness/settings preserved |
| C.2 compute/runtime | Text + visual | Yes | Fully represented | Resources and timing retained |
| C.3 protocol | Text + partial visual | Yes | Fully represented | p. 18 text-only; Safe Pass emphasized |
| C.4 coverage | Text only | Yes | Fully represented | Search credit, 226 tasks, Eq. 2 |
| C.5 reproducibility | Text + partial visual | Yes | Fully represented | Seeds, API variability, decoding |
| C.6 LLM usage | Text + visual | Yes | Fully represented | Construction, evaluated agents, visualization/prose assistance |
| D.1 task distribution | Text + visual | Yes | Represented in compressed form | All domains; repeated template labels compressed |
| D.2 screenshots | Text + visual | Yes | Represented in compressed form | All 10 sites accounted for |
| D.3 specifications | Text + visual | Yes | Fully represented | Visibility, skills, counts, mismatch noted |
| E.1 construction / ALG1 | Text + visual | Yes | Represented in compressed form | All major algorithm stages and validation levels |
| E.2 world generation | Text only | Yes | Fully represented | Target, confusables, fillers, seeds |
| E.3 oracle generation | Text + partial visual | Yes | Fully represented | Three stages, purposes, optimality caveat |
| F.1 detailed performance | Text + visual | Yes | Represented in compressed form | T9–T12 extrema and diagnostic contrasts |
| F.2 site invocation | Text + visual | Yes | Represented in compressed form | T13–T14 meaning, gaps, selected cells |
| F.3 aggregate invocation | Text + visual | Yes | Fully represented | T15 all numerical rows retained |
| F.4 complexity results | Text + visual | Yes | Represented in compressed form | T16/T18 complete; T17 selected cells/trends |
| G viewer | Text + visual | Yes | Represented in compressed form | All four capabilities; no execution claimed |
| H.1 templates | Text + visual | Yes | Represented in compressed form | All three example schemas and conditions |
| H.2 trajectories | Text + visual | Yes | Fully represented | Both examples and oracle discrepancy |
| H.3 graphs | Text + visual | Yes | Represented in compressed form | All 10 graphs, counts, major flows |
| I.1–I.7 cases | Text + visual | Yes | Represented in compressed form | Every case separately explained |
| F1, F2 | Yes, visually | Yes | Fully represented | Failure example and runtime mapping |
| F3, F4 | Yes, visually | Yes | Represented in compressed form | Detailed paired rows/flows reduced |
| F5, F6 | Yes, visually | Yes | Fully represented | Panels, axes, distributions, uncertainty caveat |
| F7, F8 | Yes, visually | Yes | Represented in compressed form | Template ring and site montage |
| F9, F10 | Yes, visually | Yes | Represented in compressed form | Pipeline and viewer |
| F11, F12, F13, F14, F15 | Yes, visually | Yes | Represented in compressed form | Mail, Calendar, Shopping, Accommodation, Food |
| F16, F17, F18, F19, F20 | Yes, visually | Yes | Represented in compressed form | Housing, Q&A, Code, Jobs, Chat |
| F21, F22, F23 | Yes, visually | Yes | Represented in compressed form | Different strategies and evidence checking |
| F24, F25, F26, F27 | Yes, visually | Yes | Represented in compressed form | Grounding, wrong target, redundancy, safety |
| T1, T2, T3 | Yes | Yes | Fully represented | All counts or settings retained across sections |
| T4, T5, T6 | Yes | Yes | Fully represented | Statistics, visibility, definitions |
| T7, T8 | Yes | Yes | Represented in compressed form | Detailed skill lists compressed |
| T9, T10, T11, T12 | Yes | Yes | Represented in compressed form | Full 240-cell transcription not repeated |
| T13, T14 | Yes | Yes | Represented in compressed form | Full site-by-skill matrix not repeated |
| T15, T16, T18 | Yes | Yes | Fully represented | All numerical rows retained |
| T17 | Yes | Yes | Represented in compressed form | Endpoints, leaders, reversals, trend |
| T19, T20, T21, T22, T23 | Yes | Yes | Represented in compressed form | All examples and central conditions |
| E1 | Text + visual | Yes | Fully represented | Trace and transition notation |
| E2 | Text only | Yes | Fully represented | No visual-inspection claim |
| ALG1 | Text + visual | Yes | Represented in compressed form | Specification and validation workflow |
| Footnote 1 | Text + visual | Yes | Fully represented | Invocation versus success |
| Footnotes 2–7 | Text + visual | Yes | Inspected but compressed | Repository references not accessed |
| References, contents, repeated headers | Yes; some text only | Yes | Deliberately compressed | No citation validation performed |
| Separate supplements / runnable artifacts | No | Limitation disclosed | Missing from supplied material | No attachments or execution evidence |

Bibliographic identity [A: p. 1]: *Where Did It Go Wrong? Process-Level Evaluation of Web Agents with Semantic State Tracking*, by Jiwan Chung, JiHyuk Byun, Vibhav Vineet, and Seon Joo Kim; Yonsei University and Microsoft Research; labeled Published at COLM 2026 Workshop on Agent Behavior. No keywords are supplied.

### Missing or inaccessible material

No supplied text page is missing. Visual renderings are absent for pp. 11, 13–16, 18, and 27, so those pages have text-only coverage. The original binary PDF, source hash verification, codebase, task files, per-run logs, test outputs, interactive viewer, and linked artifacts were not inspected. Release availability and cited-paper accuracy remain unverified. No separate supplement was provided or inferred to have been reviewed.

### Uncertain interpretations

Unresolved points are Safe Pass implementation boundaries; strict terminal/exploration relationships; empty detail-visit histories; oracle optimality despite shorter successful paths; case-specific search credit; Figure 5 counting/pairing units; Figure 6 uncertainty encoding; unquantified repeat variance; Figure 12's Calendar surface count; Figure 26's six-step wording; and the scope of 'execution success' across conditional metrics and qualitative examples. Tiny screenshot text is interpreted conservatively, using captions where appropriate. Stray extracted presentation labels are not treated as new task findings.

### Deliberately compressed material

Repeated page headers, bibliography entries, full template-name ring, detailed per-site skill lists, many individual cells in T9–T14 and T17, complete graph action enumerations, and repeated screenshot rationales are compressed. Every numbered figure and table is individually identified and interpreted; complete transcription of every secondary cell is not claimed. The narrative preserves central quantities, definitions, methodological exceptions, and all seven case outcomes.

### Potential omissions

No known major inventoried section, analysis, numbered figure/table, major equation, algorithm, contribution, or stated limitation is left unrepresented. Some secondary numerical cells, fine visual labels, and repeated action lists are intentionally compressed as disclosed. This is a comprehensive representation of the supplied evidence with explicit access and consistency limits, not a claim that every word or implementation detail has been preserved.
