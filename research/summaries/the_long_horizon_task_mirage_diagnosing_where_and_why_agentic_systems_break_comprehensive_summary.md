## Stage 0 — Document Accessibility Report

The supplied work is **The Long-Horizon Task Mirage? Diagnosing Where and Why Agentic Systems Break**, attributed to **Anonymous ACL submission**. This is a benchmark and empirical AI-agent diagnostic paper, with methodological and qualitative components. No named authors, confirmed publication venue, or acceptance status are supplied.

| Accessibility item | Assessment |
|---|---|
| Main document | Supplied as page-delimited extracted text covering physical PDF pp. 1–47 |
| Accessible page count | 47 text pages; all page numbers 1–47 are represented |
| Apparently missing pages | None in the supplied numbered text sequence; this does not establish that every external artifact is present |
| Direct visual coverage | Images inspected for pp. 1–8, 13–14, 21–25, 29, 41–44, and 47: 21 pages |
| Text-only coverage | pp. 9–12, 15–20, 26–28, 30–40, and 45–46 |
| Figures | Figures 1–11 are visually supplied; small internal screenshots and labels are only partly legible |
| Tables | Tables 1–4 are visually supplied and supported by extracted text; Table 3 continues across pp. 21–22 |
| Equations | Main horizon formulas are readable in text and images; interpretation of the depth notation remains internally inconsistent |
| Appendices | A–G supplied in text; selected appendix pages also visually supplied |
| Supplementary material | No separate supplementary spreadsheet, dataset, code, or trajectory archive supplied |
| Referenced absent artifact | Literature Review_Long-Horizon Reasoning in LLM agents.xlsx, containing full paper lists and extracted review notes |
| OCR | No additional OCR performed; extracted text was cross-checked against supplied images where available |
| Other limitation | The source SHA-256 is user-provided provenance metadata, not independently recalculated |

No tools, external sources, or browsing were used. Source content, including the reproduced judge prompt, was treated as evidence rather than instructions. The stray image-loading error does not prevent inspection of the 21 images actually displayed.

Evidence labels used below: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information [E] is introduced. HIGH confidence means the supplied evidence clearly supports the stated description; it does not certify the scientific claim independently. MEDIUM marks interpretation or unresolved reporting issues. LOW and UNKNOWN mark weak or unavailable evidence.

### Inventory established before synthesis

The inventory denominator is: abstract; §§1–6; Limitations; Ethical Considerations; References; Appendices A–G; two research questions; two named experiments; Figures 1–11; Tables 1–4; intrinsic-horizon, compositional-depth, depth-extension, and breadth-extension definitions; Appendix E.5 attribution pseudocode; Appendix F.6 judge procedure; and the principal benchmark, taxonomy, attribution, and empirical contributions. There are no numbered theorems, proofs, or formal hypotheses in the supplied work. The detailed inventory and coverage accounting appear in the final audit.

## 1. Plain-language orientation

[A, HIGH] The paper asks why AI agents become unreliable when a task requires many connected actions. An agent here is a large language model, or LLM, embedded in a system that observes an environment, chooses actions, uses tools, and continues toward a goal. Examples include navigating a website, executing shell commands, generating database queries, and controlling simulated robot arms. A successful answer at one moment is insufficient: the agent must preserve constraints, track changes, and execute dependent actions correctly over time.

The central contribution is **HORIZON**, a diagnostic benchmark intended to separate two questions: **where** performance collapses as tasks become longer, and **why** failed trajectories break down. The authors construct progressively extended task families, evaluate more than 700 tasks producing 3100+ trajectories, and assign failures to seven categories. They use GPT-5-mini and Claude-4-Sonnet across four domains, with an additional full GPT-5 embodied check. A GPT-5 judge is evaluated against human annotation.

[A, HIGH for reporting; MEDIUM for generality] Their central empirical observation is that success often falls sharply over a limited range of task-extension levels. Planning errors dominate the displayed failure distributions. Memory limitation contributes materially in some settings, especially GPT operating-system failures. The authors advocate hierarchical planning, execution-time verification and repair, and stronger memory mechanisms. These interventions are proposed, not experimentally demonstrated as fixes.

[D, MEDIUM] For the user's question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis**, the paper provides indirect evidence about mechanisms that can make an interactive agent fragile: acting on stale page states, forgetting constraints, selecting wrong actions, and propagating mistakes through tool use. It does **not** directly compare web agents against standalone LLMs, measure attacker success, or establish that agents are more vulnerable under a security threat model. Its supported contribution is reliability diagnosis, with security relevance inferred cautiously.

## 2. Document roadmap

| Location | Function |
|---|---|
| Abstract, p. 1 | Introduces HORIZON, scale, agreement values, and claimed findings |
| §1, pp. 1–3 | Motivates long-horizon diagnosis, states RQ1/RQ2, and lists contributions |
| §2, p. 3 | Positions the work against interactive benchmarks and failure studies |
| §3, pp. 3–5 | Defines horizons, extension methods, and the seven-category taxonomy |
| §4, pp. 6–7 | Presents experimental setup, success curves, and failure distributions |
| §5, pp. 7–8 | Recommends horizon-aware measurement, judge-based attribution, and design improvements |
| §6, p. 8 | Restates the benchmark, taxonomy, and attribution contributions |
| Limitations/Ethics, p. 9 | Identifies omitted evaluation dimensions and describes data/annotation ethics |
| References, pp. 9–12 | Bibliography supporting positioning and taxonomy construction |
| Appendix A, p. 13 | Extended related work in four categories |
| Appendix B, p. 14 | Literature-to-taxonomy mapping and supplementary spreadsheet reference |
| Appendix C, pp. 15–23 | Detailed category definitions, domain examples, Table 3, and overview figure |
| Appendix D, pp. 24–25 | Experiment 1 environments, models, evaluation, reproducibility, extra plots |
| Appendix E, pp. 26–39 | Mini-trajectories and an account of constructing illustrative failure slices |
| Appendix F, pp. 40–46 | Experiment 2, attribution tree, agreement discussion, distributions, judge prompt |
| Appendix G, p. 47 | Expanded discussion, including transition regions rather than exact thresholds |

The appendices materially qualify the main account. In particular, Appendix F describes different validation samples and annotators despite main-text statements about the same traces. Its reproduced judge prompt also changes the decision-tree ordering. These are substantive methodological discrepancies, not merely editorial details.

## 3. Background and context

[A] A **trajectory** is an agent's sequence of observations, reasoning or planning outputs, actions, and environmental responses. A **horizon** concerns how much effective work successful completion requires. The authors distinguish intrinsic task requirements from an inefficient agent's repeated attempts. Fifty actions spent failing on a short subtask do not automatically make the underlying task long-horizon (§3.1, p. 4).

**Intrinsic horizon**, H*, is the minimum number of effective actions required by an optimal policy. An **optimal policy** is the ideal action-selection strategy invoked by this definition; the paper says H* can be established through expert demonstrations, oracle solvers, or formal specifications. The supplied material does not provide an exhaustive oracle calculation for every evaluated task.

**Compositional depth**, s, is intended to represent high-level task structure. In the experiments it functions as a controlled extension level, rather than raw tool-call count. One increment can require several low-level actions. **Depth extension** inserts necessary intermediate operations; **breadth extension** combines baseline tasks and their coordination requirements.

**Failure Mode and Effects Analysis**, FMEA, inspires the taxonomy's hierarchy. The authors use PFMEA for process-level risks arising during rollout and DFMEA for design-level risks tied to the engineered agent. The supplied text identifies these risk levels but does not formally expand every letter of PFMEA/DFMEA. Their application is an agent-oriented adaptation, not a reproduced industrial FMEA scoring procedure.

An **LLM-as-a-Judge** is another model used to label the evaluated agent's trajectory. **Cohen-style κ agreement**, written κ in the paper, measures agreement with adjustment for chance; the supplied work reports κ values without reproducing the calculation formula or contingency tables. Agreement with a human is not the same as independently established causal correctness.

Related-work categories include interactive benchmarks; reinforcement learning, planning, and reflection; memory and long-context reasoning; and failure attribution. The authors' account of other papers is represented as their positioning, not independently verified literature assessment. Appendix A explicitly says this paper does not introduce a new memory module (p. 13).

## 4. Research problem and gap

**Existing problem [A]:** Agents fail on extended chains of interdependent actions, even when simpler tasks are manageable. Early mistakes can alter later observations, constrain recovery, and cause the whole trajectory to derail (pp. 1–2).

**Shortcomings attributed to prior approaches [A]:** Benchmarks often emphasize terminal success, use incompatible horizon proxies, and remain domain-specific. A single aggregate success score does not explain where performance changes or which mechanism failed. Existing diagnostic work is described as often domain-specific or coarse (§2; Appendix A).

**Research gap [A]:** The authors seek a shared task-centric framework combining controlled horizon growth with interpretable failure attribution across heterogeneous environments.

**Motivation [A]:** Software debugging, operating-system workflows, iterative analysis, and manipulation require persistent goals, constraints, and intermediate state. Understanding failure mechanisms should support targeted improvements rather than only better final scores.

**Scope [A]:** The empirical domains are web, OS, database, and embodied simulation. The database pipeline is multi-agent MAC-SQL; the study is not a uniform comparison of single-agent and multi-agent architectures. The work studies model families and environments available in its experiment, not every possible agent or interaction modality.

**Security boundary [D]:** Reliability failures can have security consequences when actions affect sensitive resources, as the paper's permission, system-file, and protected-schema examples illustrate. Nevertheless, a violation caused by ordinary misunderstanding or planning error is not evidence of an adversarial exploit. The source does not quantify malicious manipulation, data theft, or compromised trust boundaries.

## 5. Research questions / objectives / hypotheses

The paper explicitly states two research questions on p. 2:

- **RQ1:** Where do agents break down as task horizons increase?
- **RQ2:** Why do these failures emerge?

Its operational objectives are to construct controlled task families, measure success across extension levels, develop a cross-domain failure taxonomy, validate an automated attribution pipeline, and identify design implications. Experiment 1 principally addresses RQ1 and supplies failed trajectories relevant to RQ2. Experiment 2 tests attribution agreement and describes failure composition.

There are no formally stated statistical hypotheses, null hypotheses, preregistered predictions, or significance thresholds in the supplied work. The claim that scaling alone is insufficient is a discussion-level inference from observed failure patterns and model convergence, not a separately controlled scaling-law experiment.

The user's security research question is separate from RQ1/RQ2. [D] HORIZON can inform a proposed explanation of agent-specific fragility, but cannot establish a comparative vulnerability rate against standalone models because that experimental condition is absent.

## 6. Assumptions / threat model

The paper has an agent/environment model but no explicit adversarial threat model. It does not define attacker goals, attacker-controlled content, access privileges, attack budgets, or an attack-success metric. Websites, tools, instructions, and observations are components of an interactive workflow, not experimentally specified malicious channels.

Important methodological assumptions and conditions are:

1. [A] Baseline tasks are verified solvable before extension (p. 24).
2. [A] Added steps are necessary rather than avoidable inefficiencies, so increasing extension level should increase H* (pp. 4–5).
3. [A] Expert or oracle characterization can identify intrinsic task structure; exact mappings remain domain-dependent.
4. [A] Nested task sets are intended to reduce changes in task family and evaluation protocol (p. 6).
5. [A] The taxonomy and written rubric provide a useful basis for labeling failure causes.
6. [A] The judge sees the full recorded trajectory, while the evaluated agent may have operated with truncated or summarized context (p. 45).
7. [D] Inferring what the agent actually retained requires context evidence; a full transcript alone does not necessarily show its active input window.

The distinction between environment and agent error is consequential. Figure 8 asks whether a change could not reasonably be anticipated or detected; the prompt instead asks whether the disturbance was not caused by the agent's own action. Those are related but different tests (pp. 41, 44).

## 7. Methodology

### 7.1 Overall design

[A] Figure 1 presents a pipeline from trace/context collection to taxonomy development, HORIZON task construction, judge calibration, and large-scale annotation. The intended separation is between a horizontal axis of task horizon and a vertical axis of failure type. The work combines benchmark construction, model evaluation, qualitative coding, and agreement validation.

### 7.2 Controlled task extension

Depth extension adds non-skippable intermediate steps to a baseline task. The main text associates it particularly with fixed initial environments such as OS and database tasks. Examples include permission checks and filtering operations. Breadth extension combines independent tasks and adds coordination overhead, making it suitable for web and embodied workflows with variable initial states (pp. 4–5).

The reported nested-set construction says level s+1 contains all tasks from s plus additional tasks requiring longer execution (p. 6). [D] This leaves an implementation question: a cumulative set can mix earlier and later task horizons even though accuracy is also described as computed over tasks with identical s. No per-level task manifests are supplied to resolve whether nesting refers to complete tasks, task constituents, or related families.

### 7.3 Data and environments

| Domain | Source and implementation | Extension / success conditions |
|---|---|---|
| Web | WebArena; baseline tasks selected at roughly 90% GPT-5-mini success | Horizon extension; main account associates web with breadth extension |
| OS | AgentBench OS tasks; Appendix D says perfect GPT-5-mini baseline performance | Depth extension |
| Database | MAC-SQL with Selector, Decomposer, Refiner | Appendix D specifies depth extension; other descriptions differ |
| Embodied | IsaacSim 5.0, two Franka Emika Panda arms, Tesollo DG-3F-B grippers, red/blue/green cubes | Breadth extension; manual final-configuration success judgment |

MAC-SQL's Selector identifies relevant schema elements, the Decomposer generates subquestions and intermediate SQL, and the Refiner executes and revises queries. These components create dependencies through intermediate artifacts (p. 24).

The embodied agent receives actions and object locations and emits a JSON plan. Success requires the final target configuration and no objects dropped or displaced outside the workspace. This is a simulated plan-execution setup; the supplied methods do not establish continuous visual feedback after every primitive. Table 4 provides home, move_to_pose, grasp, and release.

### 7.4 Models and inference

GPT-5-mini and Claude-4-Sonnet are evaluated across all four domains. Full GPT-5 is additionally evaluated on embodied tasks. GPT-5 is the trajectory judge. Experiments use official APIs, default decoding with temperature = 1.0 unless otherwise noted, and no hyperparameter search. Parameter counts are reported as undisclosed. Exact API versions, benchmark commits, and seeds are promised with code rather than supplied (p. 24).

No new model training, train/validation/test split, leakage audit, training budget, inference cost table, or compute-hardware specification is supplied. IsaacSim's version and robot/gripper setup are specified; the host GPU/CPU configuration is not.

### 7.5 Failure taxonomy

| Category | Operational distinction from Table 1 |
|---|---|
| Environment Error | External change, stochasticity, or perception failure creates belief/state mismatch |
| Instruction Error | Ambiguous or misaligned specification, or failure to internalize critical qualifiers |
| Planning Error | Wrong decomposition, ordering, or concrete action despite appropriate premises/intent |
| History Error Accumulation | Individually minor errors compound without one sufficient single-step cause |
| Memory Limitation | Relevant information is dropped because effective context capacity is exceeded |
| Catastrophic Forgetting | Relevant information remains in context but is not applied |
| False Assumption | An unverified incorrect premise drives subsequent reasoning/actions |

At trajectory level, categories are described as orthogonal dimensions that may appear at different steps (p. 5). At each step, the decision procedure selects one label. The reproduced judge prompt focuses on the earliest critical failure and returns one trajectory failure_type (pp. 44–46). These granularities should not be treated as interchangeable.

### 7.6 Taxonomy development and annotation

The authors reviewed literature using a shared spreadsheet, recording title, venue, domains, models, and free-text failure notes, then iteratively coding recurring mechanisms (p. 14). Table 2 gives three illustrative prior works per category. Search databases, full search strings, screening counts, exclusion criteria, and complete coding records are not supplied. Therefore the review component is not reconstructable as a full systematic review from this document alone.

Human validation uses 40-trajectory samples, described as stratified across domains and failure categories. Main text reports two experts and comparison with one on the same traces; Appendix F instead describes a separate sample labeled by a third co-author. Both accounts must be retained as unresolved (pp. 5, 40).

### 7.7 Metrics and uncertainty

Outcome metric: task success rate, also called accuracy. Figure 3 reports means over three independent runs with identical task sets and error bars of ± one standard deviation. These are not confidence intervals. Attribution metric: κ, with reported H–H = 0.61 and H–J = 0.84. No p-values, confidence intervals for κ, detailed confusion matrix, or inferential comparison of model curves is supplied.

## 8. Experiments / analyses

### X1 — Cross-domain horizon-performance evaluation

**Purpose:** Address RQ1 by observing success as extension level grows. **Sample:** More than 700 tasks and 3100+ trajectories across four domains; exact counts per domain, level, model, and run are not supplied. **Conditions:** GPT-5-mini and Claude-4-Sonnet across domains, plus GPT-5 embodied check. **Manipulation:** Increasing s through horizon extension. **Outcome:** Success rate. **Replication:** Three independent runs per horizon setting. **Figures:** 3, 6, and 7; Appendix D.

[A] Base-task filtering is intended to distinguish horizon effects from tasks that are already difficult. The main text broadly says roughly 90% baseline success; Appendix D specifies perfect baseline performance for OS. The same source reports an unfiltered OS plot as a robustness check. [D] Filtering around one reference model changes the task population and does not by itself eliminate every cross-model selection concern.

[B] Figure 3 shows a large initial web decline, later deterioration in OS/database, and steep embodied decline. Intermediate OS values are not strictly monotonic: small rebounds are visible. The paper's broad monotonic-degradation wording should be read as an overall tendency rather than an exact property of every plotted point.

[A] Embodied results in Appendix D report success proportions with standard deviations, but do not attach explicit s labels to each prose value. GPT-5 variants: 0.926 ± 0.064, 0.407 ± 0.170, 0.259 ± 0.231, 0.074 ± 0.064. Claude-4-Sonnet: 0.963 ± 0.064, 0.259 ± 0.064, 0.111 ± 0.111, 0.037 ± 0.064 (p. 24). These are ordered horizon conditions, not an independently reported complete numeric table for Figure 3.

### X2 — Judge validation and attribution distributions

**Purpose:** Assess taxonomy interpretability and whether an automated judge follows a human-labeled rubric. **Samples:** 40 trajectories per validation study according to Appendix F; whether samples/annotators overlap is contradicted elsewhere. **Comparison:** Human–human κ = 0.61; human–judge κ = 0.84. **Judge:** GPT-5. **Application:** Full 3100+ trajectory pool across domains and both model families. **Figures:** 4 and 8–11; Appendix F.

[A] Appendix F explains that higher H–J agreement need not mean the judge is more accurate: it may align more consistently with a rubric-calibrated annotator. [D] Because the samples and annotators may differ, the two κ values are not a clean head-to-head comparison of human and judge performance on identical cases.

### X3 — Qualitative mini-trajectory analysis

Appendix E illustrates failure turning points using navigation, commands, robotic primitives, and SQL. Web examples include repeated inaccessible-homepage navigation, wrong final-answer format, forgotten completed subgoals, interpreting product records as review counts, exporting rather than displaying customers, and repeated departures from an orders page. OS examples include empty tool responses, wrong requested total, abandoned file-processing goals, and misreading redirected output. Embodied examples show unverified target assumptions and attempting another grasp while already holding a cube. Database examples show wrong prioritization of constraints and failure to decompose a multipart request.

[A] E.5 explicitly describes constructing micro-scenarios from seeded patterns and minimal observation snippets (p. 39). [D] Consequently these illustrative slices should not all be assumed to be unmodified empirical logs. Their provenance is mixed or insufficiently distinguished, particularly because other entries are presented with raw traces and gold SQL.

## 9. Results

### 9.1 Success declines with increasing task extension

[A/B, HIGH for displayed tendency] Across all four domains the supplied curves show substantial horizon-associated deterioration. Web performance approaches zero after a few extension levels; OS and database retain moderate success farther along their displayed ranges. Embodied performance falls quickly. Exact universal breakpoints are not estimated. Appendix G explicitly favors transition regions rather than single thresholds (p. 47).

[D, MEDIUM] The curves support degradation under these constructions and budgets. They do not alone prove a discontinuous mathematical regime change, identify a universal causal threshold, or separate every component of longer tasks from increased compositional difficulty.

### 9.2 Planning is the dominant attributed category

[B] Figure 9 labels Planning Error shares as Web 75%, OS 46%, Database 81%, and Embodied 96% of failures. Figure 4 labels overall Planning Error 59%, Environment 18%, Instruction 9%, and Memory Limitation 11%. Its risk totals are process-level 86.7% and design-level 13.3%. These are conditional shares among failed traces, not percentages of all attempted tasks.

[A/B] The authors emphasize planning, memory limitation, and catastrophic forgetting together. The plots strongly establish planning dominance and some memory contribution, but catastrophic forgetting is a small unlabeled segment in many bars. The displayed aggregates do not directly plot failure composition as a function of s. Thus the claimed temporal shift toward memory categories is less directly documented than the aggregate planning result.

### 9.3 Failure profiles differ between models

[B] Figure 10 labels GPT-5-mini-family failures as Planning Error 65%, Memory Limitation 18%, Environment 10%, and Instruction 4%. Claude-4-Sonnet failures are Planning Error 53%, Environment 28%, and Instruction 14%. The remaining categories occupy small unlabeled segments. These comparisons describe composition within each model's failures; they are not absolute risk comparisons between models.

[B] Figure 11 shows especially marked OS differences: GPT labels include planning 58%, memory 25%, environment 11%; Claude labels include environment 44%, instruction 23%, planning 30%. In embodied failures, planning is 95% for GPT and 98% for Claude. No error bars or sampling denominators accompany these shares.

### 9.4 Agreement is encouraging but bounded

[A] Reported κ values are 0.61 H–H and 0.84 H–J. The authors call the sample modest and explain annotation costs. [D] Agreement supports rubric consistency on selected cases, but uncertainty about sample identity, decision-tree implementation, and active-context evidence limits claims of validated causal attribution across all trajectories.

### 9.5 Scaling claim is an implication, not a demonstrated impossibility

[A] The authors argue that shrinking model-performance gaps near low success and persistent planning/memory failures favor design improvements. [D] This is a plausible interpretation of the examined systems; it is not a controlled scaling sweep, and undisclosed parameter counts prevent a quantitative model-size analysis. No proposed planning, verification, or memory intervention is tested against a baseline here.

## 10. Figure-by-figure interpretation

### Figure 1 — Diagnostic pipeline, p. 2

[B] A left-to-right diagram connects trace/context collection, taxonomy development with failure categorization and annotator agreement, the HORIZON suite, diagnostic-data generation and judge calibration, and annotated data. Numbered stages 1–5 indicate sequence. It has no numerical axes or uncertainty encoding. It supports the workflow description, not a performance result. Tiny screenshots inside the diagnostic-suite stage are not fully readable; their function is clear from surrounding labels and caption.

### Figure 2 — Agent execution and failure propagation, p. 3

[B] The central loop connects plan/action, environment state, observation, language model, and memory. Colored callouts illustrate seven failure categories around a headphone-purchase instruction. Examples distinguish missing sorting, stale loading state, unverified price assumptions, ignored new-only constraints, context loss, and cascaded errors. Numbered callouts are categorical identifiers, not measurements. [D] The environmental example includes acting on stale loading elements, which overlaps belief-verification and planning concerns; later rubric precedence determines the assigned category. It is a conceptual illustration, not a measured experiment.

### Figure 3 — Success versus extension level, p. 6

[B] Four line-chart panels: Web Navigation, Operating Systems, Databases, Embodied. Horizontal axes are Compositional Depth (s), with displayed ticks 0–4 for web/embodied and 0–8 for OS/database. Vertical axes are Accuracy (%) on linear scales marked 0–100. Red circles represent gpt-5-mini and green triangular markers claude-4-sonnet. Error bars show ± one standard deviation over three runs, per caption.

Approximate visual observations: web declines from high baseline success to around the mid-teens at the first extension and reaches near zero at the last point; OS retains intermediate success longer and shows small rebounds; database curves descend sharply after middle levels; embodied curves decline steeply with substantial intermediate variability. These are graphical estimates, not digitized exact values. The caption's action budgets are maximum 150 web, 50 OS, 31 database, and 34 embodied steps. s is not those action counts.

### Figure 4 — Risk-grouped failure composition, p. 7

[B] Stacked bars separate process-level and design-level categories for Web, OS, Database, Embodied, and Overall. The y-axis is Share of domain failures (%) on a linear 0–100 scale. Red/orange categories encode environment, instruction, planning, history accumulation; green categories encode memory, forgetting, false assumption. Group headings report 86.7% process-level and 13.3% design-level overall. Important readable labels include domain planning 75/46/81/96 and overall planning 59, environment 18, instruction 9, memory 11. Small segments are not all labeled. Different domain denominators prevent reconstructing overall weighting from this plot alone.

### Figure 5 — Two-dimensional benchmark overview, p. 23

[B] The left side contains web, OS, database, and embodied short/long examples. The right side lists seven taxonomy categories, with environment, instruction, and planning expanded into subtypes. This is a task-structure versus failure-attribution schematic, without measured axes. Small screenshot contents are partly unreadable. The caption gives illustrative H* values 8 for purchasing a flight and 3 for checking weather; these are examples, not benchmark-wide results. Caption discrepancies: it calls database composition breadth/length extension while Appendix D specifies depth; it introduces C for compositional depth despite s elsewhere; it describes blue/orange risk colors although the visible category boxes are green/red-toned.

### Figure 6 — Additional GPT-5 embodied check, p. 25

[B] A small red/blue line plot compares gpt-5-variant and claude-4-sonnet. x-axis: Number of subtasks, ticks 0, 1, 2. y-axis: Accuracy (%), labeled in roughly 20-point increments. Both descend sharply. Approximate visual estimates are GPT around 80%, 10%, 0% and Claude around 90%, one-third, 10%. These are not exact author-tabulated values. No error bars are visible. The caption says embodied task sets with GPT-5, but the legend's variant wording is imprecise; Appendix D states full GPT-5 was additionally tested.

### Figure 7 — Unfiltered OS check, p. 25

[B] x-axis Filter-k, 1–10; y-axis Accuracy (Runs / 40), approximately 0.0–0.6. Blue is GPT-5 Mini; orange is Claude Sonnet 4. The title states Median ± Std across runs, whereas the general methods emphasize mean ± standard deviation. The plot shows a downward overall tendency with local rebounds and Claude above GPT at most points. Approximate endpoints: GPT about 0.50 to 0.05; Claude about 0.58 to 0.20. Filter-k is not clearly mapped to s in the supplied caption. The visible /40 label is not sufficient to infer a complete task-count design.

### Figure 8 — Attribution decision tree, p. 41

[B] Seven vertically ordered decision boxes lead rightward on Yes to categories and downward on No to the next test. Order: Environment, Instruction, Catastrophic Forgetting, Memory Limitation, False Assumption, Planning Error, History Error Accumulation; all No leads to Others. It is a priority algorithm, not a causal effect estimate. Memory availability precedes reasoning, explicitly giving upstream information failures priority. The reproduced prompt uses a different order; see §14.

### Figure 9 — Domain failure shares, p. 42

[B] A conventional 100% stacked bar chart combines the risk groups shown separately in Figure 4. x-axis: four domains; y-axis: Share of failures (%), 0–100. Same seven-category color legend. Readable labels: Web environment 11, planning 75, memory 6; OS environment 26, instruction 12, planning 46, memory 15; database instruction 9, planning 81, false assumption 9; embodied planning 96. Unlabeled remainders should not be assigned exact values by subtraction because labels may be rounded.

### Figure 10 — Model failure shares, p. 42

[B] Two 100% stacked bars compare GPT-5 variant and Claude-4 variant. Caption identifies GPT-5-mini versus Claude-4-Sonnet aggregated across domains. Linear y-axis: Share of failures (%). GPT labels 10 environment, 4 instruction, 65 planning, 18 memory; Claude labels 28 environment, 14 instruction, 53 planning. Small remaining categories are visually present but not precisely labeled. Different failure mixtures do not establish different attack susceptibility.

### Figure 11 — Domain-by-model shares, p. 43

[B] Eight stacked bars cross four domains with GPT/Claude. Same percentage axis and legend. Readable planning shares: web GPT 72, web Claude 77; OS GPT 58, OS Claude 30; database GPT 79, database Claude 83; embodied GPT 95, embodied Claude 98. Other readable labels include web GPT instruction 12/memory 11; web Claude instruction 11/memory 5; database GPT instruction 13/false assumption 8; database Claude instruction 6/false assumption 11. Integer labels are reported as shown, without inferred significance. Small remainders and exact sample counts are unavailable.

## 11. Table-by-table interpretation

### Table 1 — Formal taxonomy, p. 4

Rows are seven categories; columns are risk level, category, and definition. Four categories are process-level and three design-level. No numeric measurements, baselines, significance tests, or best/worst values apply. Its most important distinction is dropped information versus still-present-but-unused information. Its history-accumulation definition excludes a single sufficient error. Appendix C broadens some wording, creating boundary inconsistencies discussed below.

### Table 2 — Literature-to-taxonomy mapping, p. 14

Rows are seven categories; columns give three representative prior works and typical mechanisms. Environment anchors include Zhou, Chen, Koh; instruction Trivedi, Chen, Wang; forgetting Sinha, Li, Feng; false assumption Zhang, Yang, Wei; planning Erdogan, Si, Gonzalez-Pumariega; accumulation Wang, Liu, Xi; memory Kang, Zhou, Anwar. The table is illustrative rather than exhaustive and does not report study quality, effect sizes, category frequencies, or independent coding agreement for the literature review. Full extracted notes remain in an absent spreadsheet. Citation listings are compressed here because they are anchors, not experimental comparators.

### Table 3 — Representative cross-domain cases, pp. 21–22

Rows: seven categories. Columns: web, OS, embodied, DB. Four [S] rows are environment, instruction, false assumption, planning: observed in short and long tasks but amplified by length. Three [L] rows are forgetting, history accumulation, memory: described as predominantly long-horizon-specific. These labels are qualitative, not measured prevalence ratios.

The cases show stale profile navigation, permission failures, gripper noise, schema drift; nonexistent requested fields, ambiguous ownership and churn definitions, mismatching-bowl misunderstanding; fabricated identity, assumed ownership, matching-task priors, invented schema fields; missing sorting, blanket permission changes, wrong stacking order, premature backup deletion. Continuation rows distinguish ignored constraints, repeated error chains, and lost context. Minecraft examples are illustrative category cases, not evidence that Minecraft was the evaluated IsaacSim environment. The table contains no statistical comparison or security attack trial.

### Table 4 — Embodied primitive interface, p. 24

Rows: home, move_to_pose, grasp, release. Columns: action, parameters, effect. home resets both arms; move_to_pose takes arm and pose; grasp/release close/open a gripper. arm belongs to {left, right}; pose specifies position/orientation. This describes the action interface, not performance. Appendix E uses envelop_grasp rather than grasp, an unresolved naming or implementation difference.

## 12. Diagram / architecture interpretation

The benchmark pipeline in Figure 1 has data flowing from observations and traces through human-informed taxonomy construction into calibrated automated annotation. Its output is an annotated dataset; the figure does not show a deployed mitigation system.

The execution architecture in Figure 2 is a feedback loop: instruction constrains the goal; observations describe the environment; the model uses memory-backed context to plan; an action changes the environment; subsequent observations update internal state. [D] The security-relevant feature is that an erroneous belief can influence a real action and then become part of later context. This is a mechanism-level inference from the loop, not a measured exploit.

The database architecture in Appendix D is a three-component pipeline: schema selection → query decomposition/intermediate SQL → execution and refinement. Intermediate artifacts connect components, explaining why missing constraints or wrong schema assumptions can persist. No component-isolation ablation is supplied.

The decision architecture in Figure 8 is a first-match classifier with an Others escape path. It assigns priority, not just category names. Reordering its tests changes which label wins for overlapping cases. The actual prompt's alternative priority is therefore central to interpreting the resulting distributions.

## 13. Equations and mathematical concepts

### E1 — Intrinsic horizon H*, p. 4

H* is the minimum number of effective actions required by an optimal policy. The example writes H* = |{a1: search, a2: filter price, a3: sort rating, …, a8: checkout}| = 8. Vertical bars denote the number of actions in this illustrated specification. Input: task and action semantics. Output: required effective action count. Its role is to avoid confusing agent inefficiency with task difficulty. The paper does not supply a universal action granularity or complete per-task oracle table.

### E2 — Compositional depth, p. 4

s = max over p in paths of |decision_nodes(p)|.

p is a path through task structure; decision_nodes(p) is the collection of decision nodes on that path; the maximum selects the largest count. The authors give a conditional-plan-and-merge example with s = 3 and a purely sequential workflow with s = 1. Elsewhere s is the number of composed high-level subtasks and plots start at zero. [D] These uses are not fully reconciled: a path's decision-node depth, subtask count, and extension index need not be identical. No missing definition is silently supplied here.

### E3 — Depth extension, pp. 4–5

H*_depth(s) = H*_base + Δ(s), with Δ(s2) > Δ(s1) whenever s2 > s1.

H*_base is baseline intrinsic horizon; Δ(s) is the added necessary work at extension level s. The inequality requires strictly increasing added work. It is a construction requirement, not a fitted law. The source gives typical additions of 1–2 permission checks in OS and 2–3 filtering operations in database settings, without a task-by-task verified mapping.

### E4 — Breadth extension, p. 5

H*_breadth(s) = Σ from i=1 to s of H*_i + ε(s), with ε(s) ≥ 0 and s = k for k combined baseline tasks.

H*_i is the intrinsic horizon of constituent task i. The summation adds constituent requirements. ε(s) represents coordination actions such as switching goals, checking interference, or restoring context. Output: composite intrinsic horizon. [D] Nonnegative ε alone does not mathematically ensure increasing H* across arbitrary changing task collections; the intended construction also relies on adding necessary constituent work. The paper does not estimate ε numerically.

### E5 — Agreement and illustrative comparisons

κ = 0.61 and κ = 0.84 are empirical agreement statistics, not task accuracies. Figure 3's ± values represent standard deviation over runs. The p. 7 comparison of H* = 15 versus H* = 8 at 60% success is an explanatory example of cross-domain comparison, not an identified measured pair. No theorem, proof, optimization objective, training loss, or formal security equation is supplied.

## 14. Interpretation and discussion

**RQ1:** The observed curves answer where in a domain-relative sense: success deteriorates over extension regions that vary by model and environment. Appendix G's transition-region framing is more qualified than the abstract's threshold language. **RQ2:** The taxonomy organizes observed failures and identifies planning as the largest attributed category. It does not establish experimentally isolated root causes for every trace.

The following consistency findings materially affect interpretation:

| Issue | Source accounts | Consequence |
|---|---|---|
| Validation samples | p. 5: judge compared with one annotator on the same 40 traces; p. 40: separate 40-trace sample and third co-author | Cannot identify one definitive validation design |
| Annotator count | p. 24: two authors performed failure annotation; p. 40: third co-author in H–J study | Roles/counts require clarification |
| Decision precedence | Fig. 8: forgetting/memory before false assumption/planning; prompt p. 44: false assumption/planning before forgetting/memory | Overlapping failures can receive different labels |
| Instruction definition | Table 1 includes partial constraint misunderstanding; prompt Q2 requires ambiguity a perfect agent could not resolve | Agent instruction-following mistakes may be classified differently |
| History accumulation | p. 19 and Fig. 8 require no sufficient single labelable error; prompt Q7 permits propagation of an already attributed error | Different causal scope and counts possible |
| Forgotten versus lost context | Table 1/Fig. 8 distinguish present from dropped; Appendix C.3 includes limited-window loss | Category boundaries broaden inconsistently |
| Horizon s | decision-node formula, subtask count, zero-based extension plots, baseline s=1 | Cross-domain numeric interpretation uncertain |
| Database extension | pp. 4, 24 depth; Fig. 5 caption breadth/length | Actual construction cannot be uniquely reconstructed |
| Error summary | Fig. 7 median ± SD; general methods mean ± SD | Robustness plot uses a different stated summary |
| Taxonomy coverage | p. 47 says all annotated failures fit seven categories; Others exists but counts absent | Zero Others is not independently demonstrated |

Further inconsistencies include Appendix E's title claiming five-domain × seven-type mini-trajectories while displayed domain sections are Web, OS, Embodied, and Database; E.5 then describes five WebArena domains. Not every category appears as an empirical mini-trajectory in every section. A web memory example appears under E.2 OS (p. 33), and an OS-like accumulation example occurs before E.2 (p. 30). The database planning example is duplicated on p. 38. A web trace terminates at max steps 60 (p. 30), while the headline web maximum budget is 150; these might be different configurations, but the source does not explain the relationship.

[A] Main text promises an agreement-versus-sample-size stability analysis in Appendix F (p. 5). The supplied Appendix F does not show such a curve, table, resampling analysis, or numerical stability result. Annotation-cost discussion is present; the promised empirical stability evidence is not.

[D] These issues do not erase the visible success degradation. They chiefly weaken reproducibility and precise interpretation of category prevalence, attribution validation, and the claim of horizon-conditioned changes in failure composition.

## 15. Contributions and novelty

| Contribution type | Author contribution | Evidence boundary |
|---|---|---|
| Conceptual | Task-centric separation of intrinsic horizon from wasted actions | Definitions and examples, §3.1 |
| Benchmark | Cross-domain HORIZON task families with controlled extension | Four domains, >700 tasks, 3100+ trajectories |
| Methodological | Seven-category FMEA-inspired taxonomy | Table 1, literature mapping, domain definitions |
| Attribution system | GPT-5 judge with classification and contextual failure slicing | Appendix F prompt and agreement reports |
| Empirical | Success curves and domain/model failure compositions | Figs. 3–4, 6–7, 9–11 |
| Practical agenda | Hierarchical planning, runtime verification/repair, memory preservation | §§5–6; proposals rather than tested interventions |

The supplied evidence does not establish a new trained model, new memory implementation, formal theorem, security defense, or attack benchmark. Novelty relative to the entire external literature is an author claim, not independently validated here. The literature mapping supports provenance of category ideas but the missing spreadsheet prevents exhaustive reconstruction.

## 16. Limitations

### Authors' stated limitations

[A] The explicit Limitations section says HORIZON identifies what goes wrong at failed steps but does not separately characterize recovery/self-correction, action efficiency, failure compositionality, or grounding/verification behavior (p. 9). Appendix F.5 repeats these as complementary axes, including correction latency, recovery rate, actual steps relative to H*, failure-chain depth, and verification frequency (p. 40).

[A] The authors acknowledge that 40 validation trajectories is a modest sample (p. 5) and explain the time burden of long traces, fine categories, and domain expertise (p. 40). They describe HORIZON as an initial benchmark, avoid a universal breaking constant, and state that exact horizon mappings depend on domains. Exact API versions, commits, seeds, and artifact release are deferred (p. 24).

### Additional evidence-based analyst observations

[D] The validation-study contradiction and prompt/tree ordering discrepancy are major reproducibility concerns. Exact per-condition sample counts, full numeric curves, confusion matrices, category uncertainty, active-context logs, and an empirical stability analysis are not supplied. Failure-distribution plots aggregate across horizons and therefore do not directly demonstrate a category shift with s. The study lacks a standalone-LLM comparator and security intervention or adversarial condition. Proposed remedies are not ablated. Model-size claims are limited by the narrow model set and unavailable parameter counts.

[D] Some appendix examples are constructed or abbreviated. Gold SQL and mini-traces can illustrate errors but do not establish complete execution semantics or causal attribution without the original context. Broad taxonomy categories can cover many failures while still obscuring differences within a category, particularly the combined subplan/action Planning Error category.

## 17. Threats to validity

The following validity categories are analyst assessments, not headings adopted by the authors.

- **Internal validity [D, MEDIUM]:** Controlled extension and baseline solvability reduce some confounding. They do not fully separate longer required action chains from added subgoal complexity, budget pressure, or mixed cumulative task-set composition. No recovery/planning intervention isolates causal mechanisms.
- **Construct validity [D, MEDIUM]:** H* is intended to measure task-intrinsic work, but action granularity and s have inconsistent operational descriptions. Memory labels depend on whether information was actually present in the agent's active context, which the prompt sometimes infers from plausibility.
- **Statistical conclusion validity [D, MEDIUM]:** Three-run standard deviations show variation but provide limited precision. Agreement is reported without intervals or confusion matrices. Failure bars lack uncertainty and denominators; no significance tests establish model differences.
- **External validity [D, MEDIUM]:** Four domains broaden coverage, but filtered benchmark tasks and simulated manipulation do not represent every deployment, model, or tool interface. Cross-domain consistency is evidence within this design, not universal generalization.
- **Ecological validity [D, MEDIUM]:** Benchmark-based web and OS workflows are grounded in practical tasks, while synthetic extension, limited action interfaces, and manually judged simulation may differ from deployed agents.
- **Reproducibility [D, MEDIUM]:** Prompt disclosure is valuable, but conflicting rubric versions and deferred versions/seeds/artifacts impede exact reproduction.
- **Security generalizability [D, HIGH for absence]:** Ordinary execution failures cannot be converted into attack-success rates. No attacker-controlled web content or matched standalone model condition is evaluated.

## 18. Future work and open questions

### A. Explicit author proposals

[A] Standardize horizon-aware construction and measurement across domains. Report performance curves and transition regions rather than only one success score. Use scalable judge attribution calibrated against human subsets. Develop hierarchical and constraint-aware planning, execution-time verification and repair, and memory that preserves and resurfaces long-range constraints. Extend evaluation to recovery, efficiency, cascade depth, and verification frequency (pp. 7–9, 40, 47).

### B. Additional logically remaining questions

[D] Which attribution precedence actually generated the published distributions? Were H–H and H–J studies shared or separate? What are the exact tasks, counts, active contexts, and extension mappings at each level? Does planning remain dominant under a reconciled rubric? Do memory-category shares increase with s when plotted directly? Would any proposed intervention improve success under matched budgets? How do conclusions change on unfiltered web/database tasks?

[D] For the security research question, a new study would need a defined threat model, matched standalone-LLM and web-agent conditions, controlled exposure to attacker-influenced observations, and separate metrics for task failure and security-policy violation. Those are requirements inferred for answering the user's comparison, not experiments performed or promised by this paper.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| LLM | Large language model used for language-based reasoning and action selection |
| Agent | Model embedded in an observe–plan–act workflow with tools/environment |
| HORIZON | Holistic Observations for Reasoning and faIlure analyZis in lOng-horizoN agents; authors' stylized expansion |
| SOTA | State of the art; authors' description of evaluated model families |
| OS / DB | Operating system / database |
| SQL | Structured Query Language used for database queries |
| CTE | Common table expression; intermediate named query structure in SQL examples |
| DOM | Document Object Model observations mentioned in trajectory-length discussion |
| UI | User interface, including rendered pages and interactive controls |
| API | Application programming interface used to access models/tools |
| Trajectory | Recorded sequence of observations, actions, and responses |
| H* | Minimum effective actions needed by an optimal policy |
| s | Task-structure depth or extension level; usage is not fully consistent |
| k | Number of baseline tasks combined in breadth extension |
| Δ(s) | Added necessary work from depth extension |
| ε(s) | Nonnegative coordination overhead in breadth extension |
| FMEA | Failure Mode and Effects Analysis, inspiration for risk grouping |
| PFMEA / DFMEA | Authors' process-level / design-level risk group labels |
| κ | Chance-adjusted annotation agreement statistic as reported |
| H–H / H–J | Human–human / human–judge comparison |
| Standard deviation | Run-to-run spread, not a confidence interval |
| Breaking region | Horizon range over which success falls sharply |
| Catastrophic forgetting | In the strict rubric, ignoring relevant information still in context |
| Memory limitation | Relevant information unavailable after capacity-related loss |
| False assumption | Acting from a wrong, unverified premise |
| History accumulation | Compounding small errors across a trajectory; scope differs in prompt |
| Others | Escape category for failures outside the seven main labels |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Evaluation tasks | >700 | tasks | Four domains | Author-reported | p. 6, §4 |
| Trajectory pool | 3100+ | trajectories | Across domains/models | Author-reported | pp. 1, 6, 40 |
| Domains | 4 | domains | Web, OS, DB, embodied | Author-reported | p. 6 |
| Independent repetitions | 3 | runs | Each horizon setting | Author-reported | pp. 6, 24 |
| Web maximum budget | 150 | actions/trajectory | Evaluation cap, not H* | Author-reported | Fig. 3; p. 24 |
| OS maximum budget | 50 | actions/trajectory | Evaluation cap | Author-reported | Fig. 3; p. 24 |
| DB maximum budget | 31 | actions/trajectory | Evaluation cap | Author-reported | Fig. 3; p. 24 |
| Embodied maximum budget | 34 | actions/trajectory | Evaluation cap | Author-reported | Fig. 3; p. 24 |
| Human validation sample | 40 per study | trajectories | Sample overlap contradicted | Author-reported | pp. 5, 40 |
| H–H agreement | 0.61 | κ | Two expert annotations | Author-reported | pp. 5, 40 |
| H–J agreement | 0.84 | κ | GPT-5 versus human | Author-reported | pp. 5, 40 |
| Process-level failure share | 86.7 | % | Overall failed traces | Visually readable | Fig. 4, p. 7 |
| Design-level failure share | 13.3 | % | Overall failed traces | Visually readable | Fig. 4, p. 7 |
| Overall planning share | 59 | % | Failed traces | Visually readable | Fig. 4, p. 7 |
| Domain planning shares | 75 / 46 / 81 / 96 | % | Web / OS / DB / embodied failures | Visually readable | Fig. 9, p. 42 |
| Model planning shares | 65 / 53 | % | GPT / Claude failures, aggregated | Visually readable | Fig. 10, p. 42 |
| GPT memory share | 18 | % | GPT failures, aggregated | Visually readable | Fig. 10, p. 42 |
| Claude environment share | 28 | % | Claude failures, aggregated | Visually readable | Fig. 10, p. 42 |
| Claude instruction share | 14 | % | Claude failures, aggregated | Visually readable | Fig. 10, p. 42 |
| GPT embodied sequence | 0.926 ± 0.064; 0.407 ± 0.170; 0.259 ± 0.231; 0.074 ± 0.064 | success proportion ± SD | Ordered increasing horizons; prose says GPT-5 variants | Author-reported | p. 24, D.3 |
| Claude embodied sequence | 0.963 ± 0.064; 0.259 ± 0.064; 0.111 ± 0.111; 0.037 ± 0.064 | success proportion ± SD | Ordered increasing horizons | Author-reported | p. 24, D.3 |
| Default temperature | 1.0 | decoding setting | Unless otherwise noted | Author-reported | p. 24 |
| Web median trace length | ~6300 | words | Human annotation burden | Author-reported | p. 40 |
| OS average trace length | ~1800 | words | Human annotation burden | Author-reported | p. 40 |
| Unfiltered OS endpoints | GPT ~0.50 to ~0.05; Claude ~0.58 to ~0.20 | plotted accuracy | Filter-k 1 to 10 | Approximate visual estimate | Fig. 7, p. 25 |
| Minimum annotation-time illustration | 3100 × 5 / 60 ≈ 258.3 | hours per annotator | Uses 3100 as lower reference and optimistic 5 minutes | Analyst-derived | operands p. 40 |

The final row is a transparent arithmetic illustration, not a measured annotation runtime. None of the failure-share differences above is presented as a relative percentage improvement, attack-success rate, or significance-tested effect.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| HORIZON separates task structure from agent inefficiency | H* definition and repeated-short-task example | §3.1, E1–E4 | pp. 4–5 | HIGH for definition; operational mapping incomplete |
| Study spans four domains at substantial trajectory scale | >700 tasks, 3100+ trajectories | X1 | p. 6 | HIGH reported scale; granular counts absent |
| Increasing extension is associated with lower success | Four domain curves | Fig. 3, X1 | pp. 6–7 | HIGH visual tendency; exact thresholds absent |
| Planning dominates attributed failures | Domain labels 75/46/81/96% | Figs. 4, 9 | pp. 7, 42 | HIGH for plotted shares; rubric implementation uncertain |
| Models have different failure mixtures | GPT planning/memory versus Claude environment/instruction shares | Figs. 10–11 | pp. 42–43 | HIGH descriptive; no uncertainty or matched absolute-risk inference |
| Judge agreement is reported as high | κ = 0.84 versus human | X2 | pp. 5, 40 | HIGH reporting; sample contradiction limits validation inference |
| Memory and forgetting are distinct in strict rubric | Present-but-unused versus dropped | Table 1, Fig. 8 | pp. 4, 41 | HIGH definition; Appendix C/prompt inconsistencies |
| Scaling alone is unlikely to suffice | Low-success convergence and failure categories | §5; Appendix G | pp. 8, 47 | Author interpretation; no controlled scaling experiment |
| Complementary capabilities are omitted | Recovery, efficiency, cascade, grounding exclusions | Limitations; F.5 | pp. 9, 40 | HIGH explicitly acknowledged |
| Web interaction adds state/action failure channels | Stale pages, wrong actions, lost constraints | Fig. 2; Appendix C | pp. 3, 15–20 | MEDIUM security relevance; no standalone comparator |
| Attribution procedure is internally inconsistent | Different question ordering and accumulation rule | Fig. 8 versus F.6 | pp. 41, 44–45 | HIGH directly observable discrepancy |
| Mini-trajectories are not uniformly proven raw records | Construction account plus abbreviated traces | Appendix E.5 | p. 39 | MEDIUM provenance interpretation; original archive absent |

## 22. Very simple explanation — Explain Like I'm 15

An AI agent has to do more than answer a question. It may need to open pages, compare products, remember rules, click buttons, and check whether each step worked. This paper studies what happens when those jobs require more connected steps. The researchers built longer tasks in four kinds of environments and found that success often dropped sharply as the jobs grew.

The biggest labeled problem was planning: choosing the wrong steps or doing them in the wrong order. Sometimes an agent also lost information, or still had a rule available but stopped using it. A small mistake could affect later steps because the agent kept building on what it had already done. The researchers therefore recommend better planning, checks during execution, and memory that keeps important constraints available.

For security, this helps explain a possible concern: an agent's mistake can become an action in a website or computer system. But this paper did not test hackers, malicious webpages, or the same model answering without tools. It cannot prove that web agents are more vulnerable than standalone LLMs. It gives useful clues about reliability weaknesses that a separate security study could investigate.

The paper also contains reporting disagreements, especially about who labeled which trajectories and the order the judge used to choose failure labels. The visible performance decline is clear, but the precise explanation of every failure needs more reproducible evidence.

## Completeness Audit

The audit distinguishes full representation of a supplied definition from scientific verification of its claims. All 47 supplied text pages were considered; visual inspection is limited to the 21 displayed pages. Repeated examples and bibliography entries are compressed deliberately. No absent artifact is treated as reviewed.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes, text + image | Yes | Fully represented | Scale, findings, agreement, design implications |
| §1 Introduction | Yes, text + images | Yes | Represented in compressed form | Motivation, RQs, contributions |
| §2 Related Work | Yes, text + image | Yes | Represented in compressed form | Positioning retained; citations grouped |
| §3 HORIZON | Yes, text + images | Yes | Fully represented | Framework and diagnostic axes |
| §3.1 horizon definition | Yes, text + image | Yes | Fully represented | H*, s, extension formulas and ambiguity |
| §3.2 taxonomy | Yes, text + image | Yes | Fully represented | Construction, workflow grounding, validation |
| §4 empirical evaluation | Yes, text + images | Yes | Fully represented | Setup, controls, metrics, findings |
| §5 actionable steps | Yes, text + images | Yes | Fully represented | Measurement, judge, architecture priorities |
| §6 Conclusion | Yes, text + image | Yes | Represented in compressed form | Repeated contribution statements consolidated |
| Limitations | Yes, text only | Yes | Fully represented | All four omitted dimensions retained |
| Ethical Considerations | Yes, text only | Yes | Represented in compressed form | Public/synthetic tasks, no PII, author annotation |
| References | Yes, text only | Yes | Inspected but deliberately omitted as repetitive/non-substantive | Bibliographic entries not reproduced individually |
| RQ1 | Yes | Yes | Fully represented | Horizon-associated breaking regions |
| RQ2 | Yes | Yes | Fully represented | Failure taxonomy and attribution limits |
| Formal hypotheses | None identified | Accounted for | Fully represented | No formal tests or hypotheses invented |
| X1 horizon evaluation | Yes | Yes | Fully represented | Figs. 3, 6, 7; Appendix D |
| X2 judge evaluation | Yes | Yes | Fully represented | Agreement, samples, contradictions |
| X3 qualitative examples | Yes | Yes | Represented in compressed form | Domain patterns and provenance retained |
| Figure 1 | Yes, visual | Yes | Fully represented | Tiny internal screenshots partly unreadable |
| Figure 2 | Yes, visual | Yes | Fully represented | Agent loop and seven illustrative failures |
| Figure 3, all four panels | Yes, visual | Yes | Fully represented | Axes, legend, SD, trends, budgets |
| Figure 4 | Yes, visual | Yes | Fully represented | Risk groups and readable labels |
| Figure 5 | Yes, visual | Yes | Represented in compressed form | Screenshots partly unreadable; caption conflicts retained |
| Figure 6 | Yes, visual | Yes | Fully represented | Approximate values explicitly marked |
| Figure 7 | Yes, visual | Yes | Fully represented | Unfiltered OS; median/mean and Filter-k uncertainty |
| Figure 8 | Yes, visual | Yes | Fully represented | Exact category precedence described |
| Figure 9 | Yes, visual | Yes | Fully represented | Domain shares and denominator |
| Figure 10 | Yes, visual | Yes | Fully represented | Model shares and interpretation boundary |
| Figure 11 | Yes, visual | Yes | Fully represented | All eight planning shares retained |
| Table 1 | Yes, visual + text | Yes | Fully represented | All categories and risk levels |
| Table 2 | Yes, visual + text | Yes | Represented in compressed form | All category mappings; external works not validated |
| Table 3, both pages | Yes, visual + text | Yes | Represented in compressed form | All seven categories/four domains; repeated examples grouped |
| Table 4 | Yes, visual + text | Yes | Fully represented | Four primitives and parameters |
| E1 intrinsic horizon | Yes | Yes | Fully represented | Definition and example |
| E2 compositional depth | Yes | Yes | Fully represented | Formula and inconsistent usages |
| E3 depth extension | Yes | Yes | Fully represented | Monotonicity requirement |
| E4 breadth extension | Yes | Yes | Fully represented | Summation and coordination overhead |
| E5 agreement/illustrations | Yes | Yes | Fully represented | κ interpretation; hypothetical cross-domain numbers |
| E.5 pseudocode | Yes, text only | Yes | Represented in compressed form | Priority rules compared with other versions |
| F.6 judge algorithm/prompt | Yes, pp. 44 visual, 45–46 text | Yes | Represented in compressed form | Classification, slicing, output semantics, inconsistencies |
| Appendix A.1–A.4 | Yes, visual + text | Yes | Represented in compressed form | All four related-work groups |
| Appendix B | Yes, visual + text | Yes | Fully represented | Review method and missing spreadsheet |
| Appendix C.1–C.7, domain subsections | Yes, text; selected visuals | Yes | Represented in compressed form | Definitions and domain mechanisms consolidated |
| Appendix C.8 | Yes, visual + text | Yes | Represented in compressed form | Table 3 cases and L/S distinction |
| Appendix D.1–D.5 | Yes, visual + text | Yes | Fully represented | Environment, models, results, release conditions |
| Appendix E.1 Web | Yes, text; p. 29 visual | Yes | Represented in compressed form | All displayed category patterns accounted for |
| Appendix E.2 OS | Yes, text only | Yes | Represented in compressed form | Misplaced web example noted |
| Appendix E.3 Embodied | Yes, text only | Yes | Represented in compressed form | Three displayed categories; primitive mismatch |
| Appendix E.4 Database | Yes, text only | Yes | Represented in compressed form | Instruction, false assumption, planning; duplicate noted |
| Appendix E.5 construction | Yes, text only | Yes | Fully represented | Constructed micro-scenarios and five-domain mismatch |
| Appendix F.1 procedure | Yes, text only | Yes | Fully represented | Per-step first-Yes semantics |
| Appendix F.2 sample rationale | Yes, text only | Yes | Fully represented | Lengths, expertise, stratification |
| Appendix F.3 agreement gap | Yes, text only | Yes | Fully represented | Different comparison meanings and contradiction |
| Appendix F.4 distributions | Yes, text + visual plots | Yes | Fully represented | Domain/model/domain×model breakdowns |
| Appendix F.5 scope | Yes, text only | Yes | Fully represented | Complementary dimensions |
| Appendix F.6 prompt | Yes, mixed coverage | Yes | Represented in compressed form | Special context windows and JSON output summarized |
| Appendix G, all discussion topics | Yes, visual + text | Yes | Represented in compressed form | Generalization, scaling, transition regions, evaluation |
| Major contributions | Yes | Yes | Fully represented | Benchmark, taxonomy, judge, empirical findings |
| Author-stated limitations | Yes | Yes | Fully represented | Explicit scope and modest validation sample |
| Supplementary spreadsheet | No | Absence represented | Missing from supplied material | Full review records unavailable |
| Task/code/annotation archive | No | Absence represented | Missing from supplied material | Future release claims do not establish access |
| Promised agreement stability analysis | Not identifiable | Absence represented | Missing from supplied material | No corresponding analysis visible in Appendix F |

### Missing or inaccessible material

The supplementary literature spreadsheet, complete original trajectory pool, task manifests, code, exact API versions, benchmark commits, seeds, active-context histories, and complete per-condition counts are not supplied. The paper's promised agreement-versus-sample-size stability analysis is not identifiable in the available appendix. Small screenshot interiors in Figures 1 and 5 are partly unreadable. Non-rendered pages were analyzed as text only, so typography and visual layout on those pages were not independently checked.

### Uncertain interpretations

Unresolved points include validation-sample identity and annotator roles; the rubric actually used; history-error scope; actual availability of information at memory-failure steps; the mapping among s, H*, subtasks, and decision nodes; database extension type; Filter-k's relationship to s; Figure 7's mean/median convention; Figure 6's exact model variant and values; and whether all mini-trajectories are recorded versus constructed. Small unlabeled plot segments remain numerically uncertain. The exact scientific validity of the authors' generalization and scaling conclusions is not independently established.

### Deliberately compressed material

The bibliography, repeated framing in conclusion/discussion, lengthy domain-specific taxonomy rationales, and repeated miniature action/SQL examples are consolidated. The duplicated database planning example is represented once. Raw command and SQL listings are not reproduced in full; their task, failure mechanism, and relevant inconsistencies are retained. The judge prompt's exact full text is compressed into its classification, priority, slicing, context assumptions, and output behavior. Its default slice is up to five steps; special memory/history slices can extend to eight and require establishment/origin, intermediate, and failure evidence. These procedural details are represented without following the prompt as instructions.

### Potential omissions

Every identified major section, substantive subsection group, research question, experiment, figure, table, major equation, algorithmic procedure, contribution, and stated limitation has a representation or explicit accessibility status above. Exact unlabeled curve values, complete review provenance, original execution records, and the missing stability analysis cannot be recovered from the supplied evidence. This is an inventory-based account of available coverage, not a claim that compression preserves every sentence or that the scientific audit is complete beyond the supplied materials.
