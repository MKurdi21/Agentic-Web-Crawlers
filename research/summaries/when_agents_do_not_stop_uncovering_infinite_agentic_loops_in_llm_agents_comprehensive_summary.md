## Stage 0 — Document Accessibility Report

The supplied main document is available as extracted text for physical PDF pages 1–12. Rendered source images are supplied for pages 1–11; page 12 is text-only. The sequence contains the title, abstract, main sections, acknowledgements, and references through reference [41]. No appendix appears in the supplied sequence. This establishes coverage of the supplied document, rather than independently proving that every possible associated artifact is present.

All seven numbered figures, six numbered tables, three listings, and Algorithm 1 are available in rendered pages and extracted text. Their substantive content is readable. Some small diagram labels and mathematical subscripts require cross-checking against the supplied extraction. Page 12 contains the final two references and has no supplied visual rendering. No OCR was performed: the supplied native extraction is adequate, and source images provide direct visual checks. The isolated local-image error in the prompt does not prevent inspection of the eleven images actually displayed.

The paper says that complete baseline prompts are included in its artifacts on p. 9. Those artifacts, executable analyzer, repository snapshots, annotation records, and full finding list are not supplied. They were not reviewed. No supplementary file or appendix is explicitly supplied, and the accessibility metadata reports no embedded files or detected supplementary references. This does not establish that the authors have no external artifacts.

This analysis uses only the supplied text and images. No tools, browsing, external verification, or execution were used. Visual inspection covers pages 1–11; page 12 receives text-only coverage. References are inspected as bibliography entries, not as independently read source works. Physical PDF page numbers are used throughout.

Evidence labels: [A] AUTHOR-REPORTED means stated in the paper; [B] DIRECTLY OBSERVABLE means visible in a supplied image; [C] ANALYST-DERIVED identifies a calculation from supplied operands; [D] ANALYST INTERPRETATION identifies reasoning beyond an explicit author statement. No [E] EXTERNAL INFORMATION is introduced. HIGH confidence denotes clearly supported supplied evidence, MEDIUM denotes qualified interpretation or incomplete detail, LOW denotes weak support, and UNKNOWN denotes unavailable evidence. Confidence in faithful reporting is distinct from confidence that the underlying study establishes a universal conclusion.

## 1. Plain-language orientation

This paper studies a failure in which an artificial intelligence agent repeatedly calls a language model, uses a tool, updates its memory, runs another agent, or traverses a workflow without a reliable stopping limit. The authors call this an Infinite Agentic Loop, abbreviated IAL. The important issue is not that an agent performs multiple steps. Repeated steps are often necessary. The issue is that a feedback path can keep generating more work without an effective bound on that path. [A; pp. 1–3]

An agent differs from the direct text-generation application described in the paper because it can take a model output, act on it, observe a result, and feed that result into another model call. A single request can therefore become a long sequence of paid calls and state updates. The authors identify potential consequences including application programming interface (API) cost exhaustion, model denial of service, context-window exhaustion, external tool rate-limit exhaustion, and repeated side effects. These are structural risks; the study does not demonstrate that every reported case runs forever in an actual deployment. [A; pp. 1, 3, 8]

The researchers build IAL-SCAN, a static analyzer: it examines program structure before running the application. It translates Python code and supported framework behavior into a common Agent Intermediate Representation, or Agent IR. It then builds an Agentic Loop Dependence Graph, or ALDG, to connect the pieces of repeated execution. The detector searches for reachable feedback paths involving costly or state-growing operations and checks whether a genuine stopping bound covers them. An optional language-model stage removes some candidates, followed by author manual review in the evaluation. [A; pp. 4–7]

Across 6,549 repositories, the default pipeline produces 74 potential findings. Manual review confirms 68 failures in 47 projects, giving the reported precision of 91.9%. Further review of baseline-only alerts finds seven additional failures missed by IAL-SCAN. Thus, the paper reports useful detection with known misses, rather than exhaustive discovery. The central contribution is an analysis organized around feedback-path reconstruction and bound coverage across framework interfaces. [A; pp. 8–10]

For the user's question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?', this paper supports a specific mechanism: agent orchestration creates feedback paths through tools, external observations, state, and other agents, allowing untrusted inputs to influence repeated execution. That connection is ANALYST INTERPRETATION. The study does not directly compare standalone language models with web agents, does not report relative vulnerability rates between those populations, and does not isolate web browsing as an experimental factor. [D; pp. 2–3, 8–10]

## 2. Document roadmap

The work is a mixed AI-systems, security, and algorithm paper with an empirical repository evaluation. It is not a systematic review, a model-training study, or a mathematical proof paper.

| Inventory ID | Original component | Physical pages | Role |
|---|---|---|---|
| META | Title, authors, affiliation, arXiv identification | 1 | Identifies the work |
| ABS | Abstract | 1 | Problem, method, headline findings |
| S1 | I. Introduction | 1–2 | Motivation, three detection challenges, contributions |
| S2A | II.A LLM Agents and Execution Loops | 2 | Agent iteration and existing bounds |
| S2B | II.B Static Analysis for LLM Agents | 2 | Author positioning against related analyses |
| S3A | III.A Definition of Infinite Agentic Loop Failures | 2–3 | Defines the target failure |
| S3B | III.B Threat Model | 3 | Assumptions, attacker capabilities, scope |
| S3C | III.C Motivating Example | 3 | Custom model-wrapper feedback path |
| S3D | III.D Challenges in Detecting IAL Failures | 3–4 | Framework semantics, path recovery, bound coverage |
| S4A | IV.A Agent IR Construction | 4–5 | Schema, program extraction, framework modeling |
| S4B | IV.B ALDG Construction | 5–6 | Nodes, edges, loop annotations |
| S4C | IV.C IAL Failure Detection | 6–7 | Candidate discovery, controller/bound checking, pruning |
| S5A | V.A Experimental Setup | 7 | Implementation, environment, corpus, review protocol |
| S5B | V.B RQ1: Real-world Findings | 8 | Overall findings and two case studies |
| S5C | V.C RQ2: Effectiveness | 8–10 | Ablations, baselines, false positives and negatives |
| S5D | V.D RQ3: Stability | 10 | Repeated runs and model sensitivity |
| S6A | VI.A Implications | 10 | Framework and application safeguards |
| S6B | VI.B Limitations | 10 | Four acknowledged limitations |
| S7 | VII. Conclusion | 10 | Restates contribution and findings |
| ACK | Acknowledgements | 10 | ChatGPT/Codex assistance disclosure |
| REF | References [1]–[41] | 11–12 | Bibliographic context |

Visual inventory: F1 execution-loop illustration, p. 2; F2 motivating code, p. 3; F3 analyzer pipeline, p. 4; F4 graph-construction rules, p. 5; F5 example graph, p. 6; F6 retry-loop code, p. 8; F7 output/tool-related iteration code, p. 9. Table inventory: T1 representative interfaces, p. 3; T2 finding distributions, p. 8; T3 ablations, p. 9; T4 baselines, p. 9; T5 repeatability, p. 10; T6 model sensitivity, p. 10. L1 is the Agent IR schema, p. 4; L2 example facts, p. 5; L3 bound-status taxonomy, p. 7. ALG1 is the detection algorithm, p. 6. E1–E3 below identify the three formal construction-rule groups in F4. No numbered theorem, lemma, proposition, appendix, keyword list, or formal hypothesis is supplied.

The title is 'When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents'. Authors are Xinyi Hou, Shenao Wang, Yanjie Zhao, and Haoyu Wang, affiliated with Huazhong University of Science and Technology, Wuhan, China. A p. 1 footnote identifies Haoyu Wang as corresponding author. The visible identifier is arXiv:2607.01641v1 [cs.SE], dated 2 July 2026. No accepted conference or journal venue for this work is specified. [A/B; p. 1]

## 3. Background and context

A large language model, or LLM, produces outputs that an agent program can interpret as plans, tool requests, routing choices, or termination signals. In the paper's account, an agent repeatedly plans, calls tools, observes results, updates state, and decides subsequent actions. ReAct is presented as a reasoning-and-acting paradigm; Toolformer represents tool use; Reflexion represents feedback-based operation; AutoGen represents multi-agent interaction. These descriptions summarize the supplied paper's positioning, without independently evaluating those cited works. [A; p. 2]

A feedback path returns execution or information to an earlier decision or action. For example, a model asks for a tool, the application appends a tool-related message, and the next model call receives the expanded history. A workflow cycle can have the same effect even when no visible Python while loop exists. Framework APIs may connect nodes, dispatch tools, or transfer control to another agent implicitly. This is why the authors distinguish agentic loops from ordinary syntactic loops. [A; pp. 1–5]

A controller determines whether repeated execution continues. It can depend on a deterministic counter, a model output, a tool result, external state, an exception, or several of these. An exit condition says when execution might leave; a bound places a reliable restriction on execution. A model deciding to stop requesting tools is a possible exit, but the paper does not count it as a deterministic bound. [A; pp. 3, 6–7]

Bound coverage means that the restriction applies to the feedback path being analyzed. A limit on an inner model or agent call may leave an outer retry or evaluator loop unrestricted. Likewise, an iteration cap elsewhere in the application does not automatically cover the problematic path. The relevant question is which controller or runtime scope the bound constrains. [A; pp. 4, 7]

Static analysis examines source structure and inferred execution relations. An abstract syntax tree, or AST, represents parsed Python statements and expressions. An intermediate representation organizes extracted facts in a common format. A directed graph represents possible relations between program elements. A strongly connected component, or SCC, is a region where vertices are mutually reachable, making it useful for identifying candidate cyclic execution. These explanatory definitions describe the operations used in the paper; they are not additional empirical claims.

## 4. Research problem and gap

**Existing problem.** Agent applications can repeatedly trigger costly calls or state growth when continuation depends on runtime outputs and no effective stopping mechanism covers the feedback path. Existing framework limits can be omitted, disabled, misconfigured, or attached to the wrong scope. [A; pp. 1–3]

**Author-attributed shortcomings of previous approaches.** CodeQL and Semgrep can identify source-level patterns, but the authors say they do not model the relevant agent semantics such as framework execution edges, tool dispatch, handoffs, and reentry. Existing agent-oriented analyses address workflow topology, policies, effects, sandboxing, privacy, capabilities, or audit evidence rather than the specific combination of repeated costly/state-changing execution and bound coverage. These are the authors' assessments, not independently verified literature conclusions. [A; pp. 1–2]

**Research gap.** A detector needs to normalize heterogeneous framework behavior, reconstruct feedback paths across program and framework elements, and distinguish effective bounds from merely nearby limits or fragile exits. Finding a loop alone is insufficient. [A; pp. 1, 4]

**Motivation.** Iterative execution gives agents useful flexibility, but also lets one request amplify into long-running resource consumption. The authors seek predeployment detection in downstream applications rather than only runtime monitoring or generic source-pattern matching. [A; pp. 1–2]

**Scope.** The implemented analysis targets Python downstream applications using eight modeled frameworks. It includes core agent loops and toolchain loops that block, reenter, or amplify execution. It excludes high-volume network denial of service, infrastructure resource exhaustion, prompt sponge attacks, malicious framework changes, and purely semantic no-progress behavior that is not statically inferable. [A; pp. 3, 7]

## 5. Research questions, objectives, and hypotheses

The paper explicitly states three research questions on p. 7:

| ID | Author research question | Evaluation connection |
|---|---|---|
| RQ1 | What IAL failures does IAL-SCAN identify in real-world repositories, and what are their characteristics? | Corpus findings, Table II, two case studies |
| RQ2 | Which analysis components are necessary, and how does IAL-SCAN compare with LLM and coding-agent baselines? | Table III, Table IV, false-positive/negative review |
| RQ3 | How stable are static candidate generation and LLM-assisted pruning across runs and model choices? | Table V and Table VI |

Informal objectives are to define the structural failure, implement framework-aware detection, and characterize practical findings. No formal null or alternative hypotheses are supplied. No hypothesis test should be inferred from comparative tables.

The user's research question is separate from RQ1–RQ3. The paper informs it through the structure of agent execution, but its experiments do not test whether web agents have a higher vulnerability rate than standalone LLMs. Its coding-agent and pure-LLM baselines are vulnerability-detection methods; they are not populations of deployed systems compared for vulnerability. [D; pp. 7–10]

## 6. Assumptions / Threat Model

**System and assets.** Deployed agents receive user requests, call models and tools, access external services, update state, and may perform actions including file writes, database updates, code execution, or ticket creation. Relevant assets include paid API capacity, model-service availability, worker time, context capacity, external-service quotas, and effects on connected systems. The asset grouping is analyst interpretation of the author's listed impacts and system model. [A/D; pp. 1, 3, 8]

**Trusted components.** Agent code, framework configuration, and tool definitions are fixed before deployment. Underlying frameworks and trusted tool implementations are assumed nonmalicious. Safeguards may nevertheless be missing, ineffective, disabled, or only partially applied. The threat model therefore does not require an attacker to implant a malicious framework. [A; p. 3]

**Attacker access.** An attacker or untrusted user can provide ordinary inputs: prompts, requests, documents, URLs, issue reports, tickets, workflow parameters, or API calls. Crafted inputs can influence model output, tool arguments, retrieved content, external observations, and errors, potentially encouraging retries, polling, repeated tool calls, sub-agent invocation, or workflow transitions. [A; p. 3]

**Excluded attacker powers.** The attacker cannot alter source code, framework configuration, the deployment environment, or trusted tool implementations. The analysis concerns exploitable or failure-prone execution structure under normal input interfaces. [A; p. 3]

**Important distinction.** The empirical confirmation protocol inspects source-level feedback paths and bounds. The supplied paper does not report an adversarial payload benchmark, live exploit success rate, repeated deployment trials, or measured attacker-induced monetary loss. The threat model makes malicious triggering plausible within scope; the evaluation primarily confirms structural findings. [D; pp. 3, 7–10]

## 7. Methodology

### 7.1 Study design and implementation

IAL-SCAN is implemented in Python. Its core stages are Agent IR construction, ALDG construction, and feedback-path detection. GPT-5.5 is the default optional pruning model. Supported frameworks are LangChain, LangGraph, CrewAI, AutoGen, LlamaIndex, OpenAI Agents SDK, Google ADK, and Semantic Kernel. Exact analyzer version, source revision, dependency versions, framework-model revisions, and inference parameters are not given in the supplied pages. [A; p. 7]

### 7.2 Agent IR construction

Listing 1 divides facts into six sets: ExecutionUnit, Controller, Invocation, StateUpdate, Bound, and ExitRecord. Execution units identify scopes; controllers represent loops, routers, retry logic, and termination predicates; invocations represent model/tool/agent/workflow calls and subprocesses; state updates identify changes carried across iterations; bounds and exits represent potential stopping mechanisms. Common fields include identifier, kind, source location, and attributes. [A/B; p. 4]

Nine relation forms connect the facts: owns, calls, updates, guards, exits, constrains, transitions, dispatches, and aliases. Ownership associates a fact with a scope. Calls and dispatches connect execution targets. Updates identify modified state. Guards preserve continuation dependencies. Constrains ties a bound to its intended target. Transitions capture workflow movement. Aliases help resolve names. [A/B; p. 4]

The analyzer builds a project index recording modules, imports, framework usage, decorators, factories, runtime classes, and agent callables. It parses Python into ASTs and performs lightweight resolution of import aliases, assignments, object fields, and factory returns. It expressly avoids whole-program points-to analysis. Extracted source facts have the form ⟨kind, loc, scope, guard, target, attrs⟩. They capture loops, recursion, calls, state updates, conditional exits, and exception-based retry paths. [A; p. 5]

Framework models add execution relations not exposed as direct calls. Construction models identify agents, tools, workflows, graph nodes, and scopes. Invocation models recover dispatch, transitions, handoffs, delegation, and agent reentry. Configuration models associate limits such as max_turns, max_iterations, max_retry, and recursion_limit with runtime scopes or repeated paths. Unresolved targets remain unresolved attributes rather than becoming falsely precise transfer edges. [A; pp. 5–6]

Listing 2 applies the schema to moonshot_generate: U0 is the function scope; C0 is the output-controlled loop; X0 is the costly model call; S0 appends messages and grows state; T0 is a model-dependent conditional exit. The example makes the mapping concrete, but it is an excerpt rather than a full graph export. [A/B; p. 5]

### 7.3 ALDG construction

The ALDG is a directed attributed graph. Its retained facts emphasize controllers, costly invocations, growing state updates, and execution scopes. The paper states that there are 12 node kinds and 10 edge kinds; the supplied text gives categories and examples rather than a complete standalone enumeration of every kind. Guard values, configuration, and aliases can remain attributes rather than separate vertices. [A; pp. 5–6]

Edges preserve relations through omitted auxiliary elements. Examples include CONTROL_FLOW, CALL, WORKFLOW_TRANSITION, TOOL_DISPATCH, feedback edges for loop back/recursion/reentry/retry, and CONDITIONAL_TRUE or CONDITIONAL_FALSE exits. Edge attributes retain guards, targets, framework bindings, and source locations. Controller annotations summarize costly action kinds, state growth, exit kinds, guard sources, and bound sources. These annotations inform later checks; they are not final vulnerability decisions. [A; p. 6]

### 7.4 Candidate discovery and bounds

Algorithm 1 builds a cycle-relevant subgraph, excluding exit edges and bound attributes from SCC construction. It retains nontrivial SCCs and singleton SCCs with explicit self-loops. Each candidate receives a property set Π and topology set Θ. Properties include entry reachability, feedback edges, costly calls, growing state, exits, and guard dependencies. Topology includes routing cycles, absent exit transitions, dynamic dispatch, and unreachable exits. [A/B; pp. 6–7]

Eligible candidates must be reachable from an agent entry and contain relevant feedback. The analyzer filters bounded iterations, stream consumers, parsers, pagination, lifecycle loops, and test scaffolding before bound verification. It selects a continuation controller and classifies it as deterministic, model-controlled, tool-controlled, external-state-controlled, exception-controlled, or mixed. [A; p. 7]

A bound records kind, value, source, strength, and target. Listing 3 distinguishes Covered statuses—verified_bound, framework_default_bound, config_dependent_bound—from UncoveredOrWeak statuses—missing_bound, weak_bound, disabled_bound, ineffective_bound, bypassed_bound. A status is meaningful only in relation to the repeated path. For example, a nested call's turn cap does not cover an outer evaluator cycle unless it dominates that outer path. [A/B; p. 7]

Reporting requires agentic feedback, costly or growing operations, and absence of effective bound coverage. Confidence rises with runtime-output continuation, repeated tool/agent execution, state growth, and absence of reachable deterministic exits. It falls for non-target loops and nonproduction contexts. Numerical scoring thresholds or a calibrated probability interpretation of this confidence are not specified. [A; p. 7]

### 7.5 Optional pruning

For ambiguous candidates, the analyzer builds a bounded source slice containing the witness, controller condition, guard definitions, candidate bounds, call chain, and snippets. The LLM acts as a negative filter. It may suggest predicates such as strong_finite_bound, non_agentic_loop, test_only_code, or deterministic_exit. A suggestion is accepted only if supported by the slice and compatible with static properties. The stated design limits the LLM's role, but Tables V–VI show that it still changes true-positive coverage. [A; pp. 7, 10]

### 7.6 Corpus, environment, annotation, and metrics

The corpus contains 6,549 Python repositories with at least one GitHub star, 246,748 Python files, and 33.41 million Python lines. Candidates are found using dependency declarations, imports, API uses, and orchestration patterns for the eight frameworks, then filtered by metadata and source evidence. Retained repositories must be downstream applications/products with concrete agent logic; framework implementations, tutorials, and isolated examples are excluded. Snapshot dates, complete search queries, deduplication policy, licenses, and framework population counts are not supplied. [A; p. 7]

All experiments use one Ubuntu 24.04.3 LTS server with two AMD EPYC 9554 processors, 256 logical CPU cores, and six NVIDIA A100 GPUs, each with 80 GB memory. The supplied paper does not explain which stages use the GPUs or how local hardware interacts with model APIs. [A; p. 7]

The first two authors independently inspect cases. Confirmation requires repeated model/tool/agent/workflow feedback, continuation dependent on runtime outputs, and no strong covering bound. Disagreements are discussed and another author is consulted when necessary. Agreement is 94.6% for 74 initial findings and 92.1% for the baseline-only review. No named chance-corrected agreement statistic is supplied. [A; pp. 7–10]

Metrics include alert count, confirmed true-positive coverage, false positives, missed known findings, timeout/error count, average tokens per project, average time per project, and precision. There is no train/validation/test split: this is repository analysis, not supervised training. No p-values, confidence intervals, random seeds, model temperatures, or significance tests are reported. [A; pp. 7–10]

## 8. Experiments / Analyses

| ID | Purpose and question | Conditions and sample | Results and qualification |
|---|---|---|---|
| X1 | Detect and characterize practical failures; RQ1 | Full corpus, 6,549 repositories; default pipeline and manual review | 74 findings, 68 confirmed, 6 false positives, 47 projects; Table II |
| X2 | Explain concrete mechanisms; RQ1 | Two selected confirmed cases | LiteRAG retry feedback and NVIDIA assistant malformed-output retry; F6–F7; not a prevalence sample |
| X3 | Test component contributions; RQ2 | 264 projects containing full-system static candidates; remove one component per variant | Full configuration: 340 static candidates, 74 alerts, 68 true positives; Table III |
| X4 | Compare detection methods; RQ2 | Same 264 projects, GPT-5.5, 180 s/project; constrained LLM baselines | IAL-SCAN covers 68 known findings, coding assistant 50, pure API 23; Table IV |
| X5 | Diagnose false positives; RQ2 | All six default-run false positives | Each has a real feedback path with a bound the analyzer failed to resolve adequately |
| X6 | Estimate missed cases; RQ2 | Baseline-only alerts, 250 raw extras reduced to 239 unique locations | Seven additional confirmed misses; not exhaustive corpus recall |
| X7 | Evaluate run stability; RQ3 | Three end-to-end runs, same 264-project subset and static configuration | Identical 340 static candidates; true-positive coverage 68, 64, 60; Table V |
| X8 | Evaluate pruning-model sensitivity; RQ3 | Fixed 340 candidates; four model choices | Coverage varies 41–68; Table VI; isolates filtering rather than candidate discovery |

X3 regenerates candidates for the four static ablations, then applies the same pruning stage. The no-pruning variant retains the full static stage and reports all 340 candidates. Therefore, these variants change both candidate composition and what the pruning model receives; they are not merely independent switches on a fixed final alert list. [A/D; p. 9]

X4 uses Codex without internet access and a prompt to analyze the whole repository. The pure API baseline processes Python files individually with the same core detection prompt, limiting each project to 80 files and each file to 3,000 characters. It reads 12,958 of 34,634 files in the subset, including 9,233 in full. The study reports these constraints as cost/time controls. The complete prompts are said to be in absent artifacts. The file cap should not be assumed to apply identically to Codex when the description specifically presents it with the per-file API procedure. [A; p. 9]

X6 first removes two already-matched alerts and deduplicates overlapping locations, reducing 250 raw extra alerts to 239 unique baseline-only locations. Review confirms seven misses. Other alerts include tutorials, examples, human-driven read–evaluate–print loops, user-interface/service lifecycle loops, bounded workflows, and reports lacking sufficient autonomous-feedback evidence. [A; pp. 9–10]

## 9. Results

The headline precision is 68/74 = 91.8919…%, consistent with the authors' rounded 91.9%. This calculation is ANALYST-DERIVED; the underlying counts and rounded precision are author-reported. Precision answers how many emitted findings were confirmed, not how many total vulnerabilities exist in the corpus. [A/C; p. 8]

All eight framework families have confirmed findings. LangGraph accounts for 23 and AutoGen AgentChat for 22; together the authors report 45/68 findings, or 66.2%, across 31 projects. This is a distribution among discovered findings. Without framework-specific repository denominators, it does not establish that these frameworks have greater per-project risk. [A/D; p. 8]

Retry feedback, tool-call iteration, and multi-agent chat without bounds account for 17 + 16 + 14 = 47 findings, reported as 69.1%. All 68 have missing strong bound coverage. API cost exhaustion and model denial of service are assigned to 65 findings each; context exhaustion to 19; external tool rate-limit exhaustion to five. These are author-characterized impacts of source-level findings, without reported live loss measurements. [A; p. 8]

Full IAL-SCAN covers 68 known positives with six false positives on the evaluation subset, averaging 4.2K tokens and 31.2 seconds per project. Without pruning, it still covers 68 but emits 340 alerts, including 272 false positives, while averaging zero LLM tokens and 3.8 seconds. Static analysis therefore creates a broad candidate set, with pruning reducing review volume at the cost of model dependence. [A/D; p. 9]

The coding assistant emits 140 alerts and covers 50 of the 68 reference findings. The pure API baseline emits 183 and covers 23. Coding-assistant average tokens are 141.86K in prose and 141.9K in Table IV; this is consistent rounding, not conflicting conditions. Table IV gives 75 timeout entries for Codex; nearby text describes reaching the timeout or error limit in 75 projects, so the combined failure category is more precise than calling all 75 pure timeouts. [A; p. 9]

The default run's 68 findings are not the complete known-positive universe after additional review: seven further misses are confirmed. ANALYST-DERIVED, 68/(68 + 7) = 90.7% coverage of that discovered union, assuming the seven are distinct additional cases as described. This is not corpus-wide recall and is not the denominator used for Table IV's '#Missed'. [C; pp. 9–10]

Run stability is mixed. Static candidates stay at 340 in all three runs, while pruning yields 74/73/70 alerts and covers 68/64/60 reference positives. A negative filter can therefore remove real findings. Model sensitivity is also material: GPT-5.4-mini keeps 136 alerts but covers 41; DeepSeek-v4-pro keeps 78 and covers 54; Gemini-2.5-flash keeps 131 and covers 47. More alerts do not imply better coverage. [A; p. 10]

## 10. Figure-by-figure interpretation

### Figure 1 — Normal execution, bounded stopping, and failure

This is a conceptual flow diagram, not a measured plot. It has no numeric axes, scale, error bars, or statistical estimates. The task is a three-day Tokyo trip under $1,200, which is an illustrative input rather than experimental data. The blue normal loop runs through reasoning, flight search, results, hotel search, results, and state update. A stopping-condition diamond leads to green task completion, orange bounded stopping, or a red repeated loop if no effective bound exists. Execution bounds list maximum turns, timeout, retry limit, and budget. [B; p. 2]

The red loop contains reasoning, tool call, tool result, and state update, with arrows showing repeated execution. The figure supports the distinction between useful iteration and uncontrolled feedback. It does not show how often failure occurs or demonstrate a real attack. [A/B; p. 2]

### Figure 2 — A custom model-wrapper feedback path

This is annotated code split into two panels, not a statistical plot. The left panel shows the wrapper and outer loop; the right panel shows the model call, returned finish_reason, tool iteration, and message append operations. Colored annotations distinguish wrapper, loop, model-controlled continuation, tool branch, and state growth. No axes or units apply. [B; p. 3]

The function continues while finish_reason is None or equals 'tool_calls'. A '$web_search' branch appends both the model message and a ToolMessage. The next model call receives expanded history. The inner break only leaves tool iteration, not the outer while. An output-dependent exit exists, but there is no visible local iteration limit or timeout covering the outer path. [A/B; p. 3]

A small cross-reference inconsistency is visible: the bottom annotation calls the model invocation L13, while the displayed invocation begins at line 14 and line 13 is the continued while condition. The annotated branch L17 also corresponds to the broader branch area rather than precisely the displayed if at line 18. The behavior is clear despite these line-label offsets. The '$web_search' name should not be treated as proof that the snippet executes a network search: the displayed code creates messages from the tool-call arguments. The paper categorizes this as tool-related feedback. [B/D; p. 3]

### Figure 3 — Analyzer pipeline

Three major panels show Agent IR construction, ALDG construction, and IAL detection. Project artifacts and framework specifications enter from the left. Program extraction uses a project index, AST analysis, and source facts. Framework modeling uses API matching, object binding, and execution relations. Their output is Agent IR. [B; p. 4]

Projection rules produce graph nodes, edges, and loop annotations. Detection extracts an execution subgraph, computes SCCs, filters eligible candidates, infers controllers, and verifies bounds. Covered or non-target paths are not reported; uncovered paths can become findings with optional LLM-assisted processing. A sample finding lists a loop witness, high-cost/state-growth evidence, missing_bound status, and availability/API impact. This visual connects implementation stages to interpretable evidence rather than providing performance results. [A/B; p. 4]

### Figure 4 — Formal mapping from facts to graph

This boxed mathematical specification contains notation plus node, edge, and loop-summary construction rules. It is not a plot and has no axes or empirical estimates. It defines the graph as vertices, edges, and attributes; facts become typed vertices; inferred relations become typed edges; controller summaries collect feedback, costly actions, growth, exits, and bounds. The mathematical detail is interpreted in section 13. [B; p. 5]

It supports the architecture's abstraction step. It is not a proof that every feasible execution path is represented or every effective bound is correctly recognized. [D; pp. 5–6]

### Figure 5 — Graph for the motivating wrapper

The graph displays N0 BASIC_BLOCK for the function, N1 for the outer while controller, N2 LLM_CALL, N3 for tool-call iteration, N5/N6 STATE_APPEND operations, and decision/exit nodes. The absent N4 label in this displayed sequence should not be filled with an invented node. Green, purple, blue, pink, and yellow encodings distinguish function, loop, call, state, and exit/decision categories; a legend identifies solid control flow and dashed feedback. [B; p. 6]

The outer conditional exit depends on finish_reason; the inner iterator exit means no further tool calls in that iteration. Dashed red feedback indicates enlarged messages reused by the next model iteration. Both append nodes visibly carry state_growth: yes. The outer controller is labeled MIXED, while prose emphasizes model-produced finish_reason; mixed classification can reflect combined guard dependencies, but the exact classifier rationale is not supplied. [A/B/D; pp. 5–6]

The image's small call label can be misread as self.1lm; the source code and native text identify self.llm._generate. This is a glyph-readability issue, not evidence of a different function. The figure supports why exits and feedback are represented separately. [A/B; pp. 3, 6]

### Figure 6 — Nested retry feedback in LiteRAG

This code figure shows a planner with nested while not success loops. The model invocation occupies lines 8–10, parser exceptions are swallowed at 12–13, and an empty accepted-step list resets success to False at 20–21. There are no plotted axes or units. [A/B; p. 8]

The inner loop repeats until parsing succeeds. The outer loop can repeat if plan checking rejects all steps. Both paths return to the model call without a visible retry cap, timeout, or token budget. The figure supports a costly retry mechanism involving exceptions and validation. The authors identify the repository as 2456868764/LiteRAG. No measured number of retry iterations, exploit input, or runtime cost is supplied. [A/B; p. 8]

### Figure 7 — Output-validation retry in an assistant

This code figure has a while True loop, tool-bound model setup, streaming or ordinary model invocation, and a condition that appends 'Respond with a real output.' to message state. No axes, units, or statistical uncertainty apply. The authors identify NVIDIA-AI-Blueprints/ai-virtual-assistant. [A/B; pp. 8–9]

The exact continuation guard is important: retry occurs when there are no result.tool_calls and the content is empty or has an empty text field in the tested list form. Otherwise the code breaks. Thus the visible unbounded path specifically concerns unsuitable output without tool calls; the caption's 'Tool call iteration' is broader than the immediate retry guard. It would be inaccurate to say this code repeats whenever the model emits tool calls. [B/D; p. 9]

Streaming is used for a target-tool message branch; ordinary invocation is used otherwise. The repeated corrective prompt grows state before another model call. The image and nearby text support output-dependent retry and context growth, but not a general claim that all tool requests in this function cause another iteration. [A/B; pp. 8–9]

## 11. Table-by-table interpretation

### Table I — Common program roles across framework forms

The columns identify Program Role, the motivating example, Other Framework Forms, and IAL Signal. Rows cover model call, continuation control, tool dispatch, state update, and bound. Model calls include self.llm._generate, AgentExecutor.invoke, and Runner.run; continuation examples include finish_reason, tools_condition, and termination_condition. Tool registration/dispatch and chat-history/state APIs express feedback in different forms. The bound row contrasts the example's lack of max_tool_calls or timeout with max_iterations, max_turns, and recursion_limit. This is a qualitative interface taxonomy, with no statistical ranking. [A/B; p. 3]

### Table II — Distribution of 68 confirmed failures

Counts are findings; '#Proj.' counts projects associated with each row. Framework and failure-pattern groups describe the 68 findings. Impact and root-cause labels can overlap, so their percentages should not be summed as exclusive categories. Project counts likewise are not necessarily additive across framework use. All ratios use the 68 confirmed failures as their denominator. [A/B/D; p. 8]

| Framework | Findings | Ratio | Projects |
|---|---:|---:|---:|
| LangGraph | 23 | 33.8% | 16 |
| AutoGen AgentChat | 22 | 32.4% | 15 |
| LlamaIndex | 6 | 8.8% | 2 |
| LangChain AgentExecutor | 5 | 7.4% | 3 |
| CrewAI | 4 | 5.9% | 4 |
| OpenAI Agents SDK | 4 | 5.9% | 3 |
| Google ADK | 3 | 4.4% | 3 |
| Semantic Kernel | 1 | 1.5% | 1 |

| Failure pattern | Findings | Ratio | Projects |
|---|---:|---:|---:|
| Retry feedback without bound | 17 | 25.0% | 10 |
| Tool-call iteration without bound | 16 | 23.5% | 11 |
| Multi-agent chat without turn bound | 14 | 20.6% | 13 |
| Workflow loop without effective bound | 9 | 13.2% | 8 |
| Message reentry without bound | 7 | 10.3% | 2 |
| Runner, delegation, or evaluator feedback | 5 | 7.4% | 4 |

| Impact or root cause | Findings | Ratio | Projects |
|---|---:|---:|---:|
| API cost exhaustion | 65 | 95.6% | 44 |
| Model denial of service | 65 | 95.6% | 44 |
| Context window exhaustion | 19 | 27.9% | 14 |
| External tool rate-limit exhaustion | 5 | 7.4% | 5 |
| Missing strong bound | 68 | 100.0% | 47 |
| Tool-controlled retry | 28 | 41.2% | 18 |
| Model-controlled termination | 26 | 38.2% | 19 |
| Missing exit | 23 | 33.8% | 17 |
| Workflow cycle without verified bound | 21 | 30.9% | 15 |
| State growth amplifier | 19 | 27.9% | 14 |
| Agent tool reentry | 17 | 25.0% | 11 |

LangGraph has the largest discovered count and Semantic Kernel the smallest. These rankings describe detected cases, not underlying framework vulnerability rates. Repeated external side effects are motivated in the paper but do not appear as a separate measured impact row here. No confidence intervals or significance markers are provided.

### Table III — Component ablations

All averages are per project on 264 evaluation projects. 'K' denotes the reported thousand-token scale; times are seconds. Static candidate counts precede pruning; alerts follow the configured pipeline.

| Variant | Static candidates | Alerts | TP | FP | Average tokens | Average time |
|---|---:|---:|---:|---:|---:|---:|
| Full IAL-SCAN | 340 | 74 | 68 | 6 | 4.2K | 31.2 s |
| Without Framework Modeling | 910 | 276 | 61 | 215 | 22.3K | 92.3 s |
| Without Agentic Gate | 1,453 | 87 | 62 | 25 | 40.4K | 110.3 s |
| Without Bound Coverage | 365 | 70 | 60 | 10 | 4.3K | 38.1 s |
| Without Benign Loop Filtering | 696 | 103 | 62 | 41 | 16.3K | 66.3 s |
| Without LLM Pruning | 340 | 340 | 68 | 272 | 0 | 3.8 s |

The full system and no-pruning variant tie at 68 known positives. No pruning is fastest and uses no model tokens, but has the most false positives. Removing the agentic gate gives the largest candidate count and token/time averages. Removing framework modeling increases false positives and loses seven reference positives. Removing bound coverage lowers coverage even though it removes a filtering mechanism; because candidates are regenerated and then pruned, a simple monotonic interpretation is unsupported. No significance or variation intervals accompany these one-condition rows. [A/B/D; p. 9]

### Table IV — Detection baselines

| Method | Alerts | TP coverage | Missed reference findings | Timeout column | Average tokens | Average time |
|---|---:|---:|---:|---:|---:|---:|
| IAL-SCAN | 74 | 68 | 0 | 0 | 4.2K | 31.2 s |
| Coding assistant | 140 | 50 | 18 | 75 | 141.9K | 116.0 s |
| Pure LLM API | 183 | 23 | 45 | 1 | 18.1K | 34.4 s |

The note specifies 264 projects, GPT-5.5, 180-second timeout, and '#TP Cov.' as coverage of confirmed failures. The coding assistant is Codex. IAL-SCAN has the highest reference coverage and lowest token/time averages under these conditions. The zero missed entry is relative to the 68-reference set, not a statement that later review found no misses. Timeouts/errors and input restrictions qualify comparisons. The table does not give the complete independently established true-positive count for every baseline alert after incorporating the seven newly found cases. [A/B; pp. 9–10]

### Table V — End-to-end repeatability

| Run | Static candidates | Alerts | TP coverage | Average tokens | Average time |
|---|---:|---:|---:|---:|---:|
| 1 | 340 | 74 | 68 | 4.2K | 31.2 s |
| 2 | 340 | 73 | 64 | 4.2K | 39.3 s |
| 3 | 340 | 70 | 60 | 4.2K | 38.6 s |

Candidate count and reported token averages tie across all runs. Run 1 has greatest coverage and shortest average time. Run 2 is slowest. Repeated static discovery is demonstrated for these three runs; universal determinism under all environments is not tested. Rounded identical token averages do not establish exact equality of every token count. [A/B/D; p. 10]

### Table VI — Pruning-model sensitivity

| Pruning model | Alerts | TP coverage | Average tokens | Average time |
|---|---:|---:|---:|---:|
| GPT-5.5 | 74 | 68 | 4.2K | 31.2 s |
| GPT-5.4-mini | 136 | 41 | 3.8K | 7.4 s |
| DeepSeek-v4-pro | 78 | 54 | 6.2K | 48.2 s |
| Gemini-2.5-flash | 131 | 47 | 7.0K | 17.8 s |

The same 340 static candidates are the input. GPT-5.5 covers the most reference positives and emits the fewest alerts. GPT-5.4-mini is fastest and lowest-token but has lowest coverage. DeepSeek is slowest; Gemini has the highest token average. These are pruning results, not model-training comparisons or general model-quality rankings. No repeated-run dispersion for each alternative model is given. [A/B; p. 10]

## 12. Diagram / Architecture

F1, F3, and F5 provide the substantive flow/architecture views; their individual encodings are described above. Their combined information flow is: application artifacts plus framework specifications → normalized facts and relations → graph nodes/edges/annotations → reachable cyclic candidates → controller and bound assessment → optional negative filtering → evidence-bearing findings. This is the analyzer's processing flow, not the agent's runtime flow. [A/B; pp. 4–7]

The agent runtime flow illustrated in F1/F2/F5 is different: model output → tool-related branch or observation → message/state update → another model call. The continuation guard consumes runtime information, while effective bounds must constrain the controller or enclosing execution scope. Keeping these two flows separate avoids mistaking the analyzer's LLM pruning model for the potentially vulnerable application's LLM. [A/D; pp. 2–7]

F3 includes two decisive filters: noneligible candidates are skipped, and effectively bounded candidates are not reported. An uncovered path can produce a witness and impact classification. The optional LLM is presented as assisting candidate filtering; manual confirmation belongs to the experimental protocol and should not be assumed to be an automatic runtime defense. [A/D; pp. 4, 7]

F5 shows why state/data feedback matters alongside control edges: appended messages become input to later model calls. The algorithm is therefore organized around controller, invocation, and state facts rather than only statements containing while or for. F4 specifies how these relationships are represented, and ALG1 uses the resulting graph. [A/B; pp. 5–6]

## 13. Equations and mathematical concepts

There are no training losses, optimization objectives, numbered theorems, or formal soundness/completeness proofs in the supplied paper. The relevant mathematics is graph construction and set-based detection.

**Notation.** F4 defines G_A = (V_A, E_A, α), where V_A is the vertex set, E_A the edge set, and α stores attributes. An Agent IR fact r maps to vertex v_r. C denotes controller facts; I_cost costly invocation facts; S_grow growing state updates; U_scope scope facts. T_V denotes node kinds and K_E edge kinds. A relation r_i → r_j annotated by κ and Δ implies an edge kind κ with attribute information Δ. body(c) and cycle(c) describe the controller's body and feedback component. [A/B; p. 5]

**E1 — Node construction, F4 rule 1.** For r in C ∪ I_cost ∪ S_grow ∪ U_scope, create v_r in V_A with kind(v_r) in T_V and assign α(v_r) from fields(r) ∪ attrs(r). The union symbol means the retained facts come from these categories. Plainly: keep the relevant program element as a typed graph node and carry its source/evidence attributes forward. Input is an IR fact; output is a graph vertex. The rule specifies representation, not an execution probability. [A/B; p. 5]

**E2 — Edge construction, F4 rule 2.** If an inferred relation links r_i to r_j with kind κ in K_E and attributes Δ, insert (v_ri, v_rj, κ) into E_A and assign the edge attributes Δ. Plainly: connect graph nodes using the kind and supporting information of the recovered program/framework relation. Inputs are facts and a derived relation; output is a typed directed edge. The later prose explains preserving reachability through auxiliary elements not retained as vertices. [A/B; pp. 5–6]

**E3 — Loop summaries, F4 rule 3.** Feedback(c) collects kind(e) for feedback edges in cycle(c), then includes guard_source(c). Cost(c) collects kinds of high-cost invocations in body(c). Growth(c) is true when there exists a state update s in body(c) with state_growth. Exit(c) collects exit facts whose owner or target is c. Bound(c) collects bounds constraining c or its owner scope. The existential symbol means 'at least one exists'; set comprehensions mean 'collect all elements satisfying the condition'. [A/B; p. 5]

These summaries distinguish evidence of repetition, resource-consuming operations, accumulated state, possible exits, and possible bounds. Bound(c) collects candidates; the final checker still assesses effective coverage. Exit(c) does not automatically establish that execution is bounded. No formal numerical strength function or complete configuration-dependent evaluation rule is given in this box. [A/D; pp. 5–7]

**ALG1 — Detection over ALDG.** The algorithm initializes findings F to the empty set. It constructs G_cycle by retaining edges whose kind belongs to K_cycle, the cycle-relevant edge kinds. It computes SCCs and retains components with more than one vertex or an explicit self-loop. For each candidate L, it collects Π_L and Θ_L, checks eligibility, selects controller c_L, computes bound status β_L, skips covered candidates, builds a finding F_L, and adds it only if reportable. The output is a set of IAL findings. [A/B; p. 6]

K_cycle is explained by categories in prose—control flow, calls, framework transitions, dispatch, and feedback—but no complete literal list is printed in the algorithm. REPORTABLE and controller selection are procedural abstractions, not fully expanded mathematical implementations. No asymptotic runtime complexity is supplied. The specification is sufficient to understand the pipeline, but not to recreate every implementation decision from pseudocode alone. [A/D; pp. 6–7]

**Derived calculations used in this report.** Precision = 68/74 × 100 = 91.9% after rounding. Known-union coverage = 68/(68 + 7) × 100 = 90.7%, qualified as discovered-union coverage. Full-file baseline coverage = 9,233/34,634 × 100 ≈ 26.7%; any-read coverage = 12,958/34,634 × 100 ≈ 37.4%. These are ANALYST-DERIVED and should not be confused with vulnerability recall. [C; pp. 8–10]

## 14. Interpretation and discussion

RQ1 is answered by confirmed findings across all eight modeled frameworks, several feedback patterns, and repeated absence of strong covering bounds. The evidence supports that this is a cross-framework application problem. It does not determine population prevalence, framework-adjusted risk, actual duration of failed runs, or the rate of malicious triggering. [A/D; p. 8]

RQ2 is answered by ablations and constrained baseline comparisons. Framework-aware modeling, relevance gating, benign-loop filtering, and bound analysis contribute to the reported balance of coverage, alert volume, and token/time cost. The comparison supports IAL-SCAN under the given evaluation setup, not the claim that every coding agent or unrestricted direct-LLM analysis must perform worse. [A/D; p. 9]

RQ3 is answered by separating stable static discovery from variable model filtering. Repeated runs retain the same candidates, but pruning can remove reference positives. Alternative models show that a larger alert list can still have lower coverage. Therefore, the optional stage's negative-only design does not make it harmless to recall. [A/D; p. 10]

Several apparent numerical tensions have identifiable denominators. Table IV's zero misses for IAL-SCAN concerns the 68 cases forming its reference set, while later review finds seven extra misses. The corpus is 6,549 projects; 264 is the subset containing the full-system static candidates, not a replacement corpus size. Table IV's 141.9K is rounded from prose 141.86K. Percentages in Table II can exceed 100% when impact/root-cause labels overlap. [A/D; pp. 8–10]

Unresolved presentation details remain. Figure 2 has line-label offsets; Figure 7's caption is broader than its exact malformed-output retry guard; the Table IV timeout label is narrower than the prose timeout-or-error description. Manual confirmation explicitly requires continuation dependent on runtime outputs, while the general definition emphasizes feedback plus missing effective bounds more broadly. This may matter for deterministic but unbounded costly agent loops; the supplied evaluation does not resolve how such edge cases are labeled. [B/D; pp. 3, 7, 9]

For the user's question, the strongest grounded answer is architectural: tools, observations, mutable state, exception handling, routing, and delegation create extra opportunities for inputs to affect future actions and multiply resource use. Calling this greater vulnerability than standalone LLMs remains an inference about added mechanisms, not a measured comparative result. The paper addresses availability and resource amplification especially clearly; it is not a comprehensive study of all web-agent security failures. [D; pp. 1–3, 8]

## 15. Contributions and novelty

**Conceptual contribution.** The authors define IALs as structural agentic feedback failures without effective bounds and distinguish them from legitimate iteration. [A; p. 2]

**Representation contribution.** Agent IR normalizes source and framework elements, while ALDG preserves execution, feedback, state, exit, and bound evidence. This provides a common analysis vocabulary across heterogeneous APIs. [A; pp. 4–6]

**Algorithmic/system contribution.** IAL-SCAN combines SCC-based candidate discovery with controller selection, bound-coverage reasoning, benign-loop filtering, and optional evidence-constrained LLM pruning. [A; pp. 6–7]

**Implementation contribution.** A Python analyzer models eight framework families and downstream application behavior. Exact source availability cannot be established from supplied artifacts because none are included. [A; p. 7]

**Empirical contribution.** The paper reports 68 confirmed failures across 47 projects, distribution/impact categories, component ablations, constrained baselines, six false-positive explanations, seven discovered misses, and stability/sensitivity measurements. [A; pp. 8–10]

The supplied paper does not establish a theorem-level soundness guarantee, introduce a trained model, or present a standalone-versus-web-agent vulnerability benchmark. Novelty relative to related work is author-claimed; references were not externally checked. [D; pp. 2, 5–10]

## 16. Limitations

### Authors' stated limitations

1. Static analysis over-approximates dependencies rather than predicting one actual trace and can produce false positives.
2. The implementation supports Python and eight frameworks; unsupported languages/frameworks or incomplete models can produce false negatives.
3. Highly customized semantics, project-specific schedulers, external-state stopping logic, and natural-language semantic checks have limited support, reducing bound precision.
4. Optional LLM pruning can be incomplete or unstable for ambiguous cases. [A; p. 10]

### Additional evidence-based analyst observations

The corpus excludes zero-star repositories and non-Python applications, and its exact collection/snapshot procedure is not reproducible from these pages alone. The 264-project comparison subset is selected using the full analyzer's candidates, so it is not a random independent sample of all 6,549 projects. This can affect how comparative results generalize. [D; pp. 7–9]

The reference positives originate from the default pipeline, with later baseline-only review adding seven misses. This is useful targeted validation, but it does not establish exhaustive ground truth for every corpus repository. A global false-negative rate remains unknown. [D; pp. 8–10]

Baseline caps and timeouts materially constrain access to evidence. The pure API method fully reads approximately 26.7% of subset files. Results cannot isolate the benefit of graph reasoning from all differences in input access, orchestration, and resource budgets. [C/D; p. 9]

The impact labels identify plausible consequences, but the paper does not supply live attacks, resource-loss distributions, external side-effect counts, or measured sustained denial of service. Static structural confirmation should not be silently upgraded to operational exploit proof. [D; pp. 3, 7–10]

No uncertainty intervals, per-project runtime distributions, alternate-model repetitions, exact pruning parameters, or complete artifact contents are supplied. Claims of stability and efficiency therefore remain bounded by the reported runs and averages. [D; pp. 9–10]

## 17. Threats to validity

The following validity categories are ANALYST INTERPRETATION, not headings used by the authors.

**Internal validity.** Manual reviewers are the authors, and disagreement resolution is not described as blinded. The same static/pruning pipeline helps define the comparison reference set. The ablations show system-level effects, but candidate regeneration plus pruning means individual effects can interact. [D; pp. 7–9]

**Construct validity.** 'Infinite' is operationalized as missing effective structural bound rather than observation of endless execution. Model-dependent continuation can be risky without every input producing nontermination. Impact classifications concern possible consequences. Manual confirmation's runtime-output requirement should be distinguished from the broader conceptual definition. [D; pp. 2–3, 7–8]

**External validity and generalizability.** Results apply directly to the sampled starred Python downstream repositories and modeled frameworks. Unsupported languages, frameworks, custom orchestration, private deployments, and standalone LLM systems are not measured populations. Framework count rankings lack exposure denominators. [D; pp. 7–10]

**Statistical conclusion validity.** Counts, percentages, and average costs are descriptive. There are no significance tests or intervals; three repeated runs provide limited information about pruning variability. No formal inference about all agent applications follows from the percentages alone. [D; pp. 8–10]

**Ecological validity.** The code snapshots are real downstream projects, improving practical relevance, but deployment configuration and actual production use may differ from visible source. The six false positives demonstrate that indirect/default bounds can materially change the classification. [D; pp. 7, 9]

**Reproducibility.** Hardware and broad method are reported. Complete prompts are referred to in absent artifacts, and corpus revisions, framework versions, model settings, and individual finding evidence are not supplied here. Reproduction cannot be assessed as completed from this document package. [D; pp. 7–10]

## 18. Future work and open questions

### A. Author-proposed directions

The authors recommend runtime-scope enforcement of bounds, default budgets propagated across feedback paths, reporting uncovered cycles at compilation or runtime, and guards limiting state growth. Application developers should set explicit turn/step limits, cap retries and repairs, use timeouts, and bound message history or workflow-state size. They caution against relying on the model eventually to stop producing tool calls, plans, or termination messages. These are implications and design recommendations rather than a separately specified future-work research program. [A; p. 10]

### B. Analyst-identified open questions

How frequently can ordinary or adversarial inputs activate each structural finding? What production resource costs follow? How can source analysis reliably account for external-state stopping rules and deployment overrides? How can pruning reduce false positives without dropping real cases across runs? What ground-truth protocol could measure corpus-wide recall independently of the analyzer's candidate set? [D; pp. 3, 7–10]

For the user's research question, a direct study would need matched standalone and agentic systems, explicit web-input conditions, comparable tasks, and measured security outcomes. Those elements are absent here. The supplied findings motivate such a comparison but do not supply its answer quantitatively. [D; pp. 7–10]

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning within this paper |
|---|---|
| LLM | Large language model; produces text or structured outputs consumed by the agent |
| AI agent | Program that uses model outputs to plan, act, observe, update state, and continue |
| IAL | Infinite Agentic Loop; relevant repeated execution without effective stopping bound |
| IAL-SCAN | The authors' static analyzer for these failures |
| API | Application programming interface; model/tool calls can consume paid or quota-limited resources |
| IR / Agent IR | Intermediate representation; common typed facts and relations extracted from agent code |
| ALDG | Agentic Loop Dependence Graph; attributed directed graph connecting agent-loop elements |
| AST | Abstract syntax tree; parsed structure of Python source |
| SCC | Strongly connected component; mutually reachable graph region used for cyclic candidates |
| Feedback path | Route returning output, state, or control to further execution |
| Controller | Element whose condition determines continuation |
| Bound | Limit such as counter, retry cap, timeout, budget, or framework execution cap |
| Bound coverage | Whether that limit constrains the actual repeated path |
| ExitRecord | IR fact recording a potential way to leave execution |
| State growth | Persistent accumulation, such as appended messages across iterations |
| Handoff/delegation | Transfer of work or control to another agent |
| Reentry | Returning to model/agent execution through tools or orchestration |
| Negative filter | Pruning stage that removes candidates rather than originating static candidates |
| Witness | Evidence-bearing path illustrating the reported feedback mechanism |
| TP / FP / FN | True positive / false positive / false negative relative to manual review |
| Precision | Confirmed findings divided by emitted findings |
| TP coverage | Number of reference confirmed failures covered; not automatically global recall |
| DoS | Denial of service; repeated execution can occupy model/application capacity |
| REPL | Read–evaluate–print loop; a human-driven loop distinguished from autonomous feedback |
| G_A, V_A, E_A, α | ALDG, its vertices, edges, and attributes |
| C, I_cost, S_grow, U_scope | Controller, costly-invocation, growing-state, and scope fact sets |
| T_V, K_E, K_cycle | Node kinds, edge kinds, and cycle-relevant edge kinds |
| Π_L, Θ_L | Candidate property set and topology set |
| c_L, β_L | Selected continuation controller and checked bound status |
| S_L | Bounded source slice provided to optional pruning |

## 20. Key numerical results

The tables in section 11 preserve all experimental table rows. This compact ledger supplies the headline corpus, review, configuration, and derived quantities without repeating every row.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Corpus repositories | 6,549 | repositories | Starred Python downstream agent applications | Author-reported | p. 7 |
| Corpus files | 246,748 | Python files | Full corpus | Author-reported | p. 7 |
| Corpus code | 33.41M | lines | Python code | Author-reported | p. 7 |
| Framework support | 8 | families | Current implementation | Author-reported | p. 7 |
| Default static candidates | 340 | candidates | Across 264 candidate-containing projects | Author-reported | pp. 8–9 |
| Evaluation subset | 264 | projects | RQ2/RQ3 comparisons | Author-reported | pp. 8–10 |
| Default findings | 74 | alerts | Full-corpus default pipeline | Author-reported | p. 8 |
| Confirmed default findings | 68 | failures | Manual review | Author-reported | p. 8 |
| False positives | 6 | findings | Default run | Author-reported | pp. 8–9 |
| Affected projects | 47 | projects | Confirmed default findings | Author-reported | p. 8 |
| Precision | 91.9 | percent | 68 confirmed / 74 alerts | Author-reported | p. 8 |
| Initial review agreement | 94.6 | percent | 74 findings; first two authors | Author-reported | p. 8 |
| Baseline-only agreement | 92.1 | percent | Unique baseline-only locations | Author-reported | pp. 9–10 |
| Additional misses | 7 | failures | Baseline-only review | Author-reported | p. 10 |
| Raw extra alerts | 250 | alerts | Two baselines | Author-reported | p. 9 |
| Unique reviewed extras | 239 | locations | After matching/deduplication | Author-reported | p. 9 |
| LangGraph + AutoGen findings | 45; 66.2 | count; percent | Out of 68, across 31 projects | Author-reported | p. 8 |
| Three leading patterns | 47; 69.1 | count; percent | Retry, tool iteration, multi-agent chat | Author-reported | p. 8 |
| API/model-service impact | 65; 95.6 | count; percent | Each impact category, 68 findings | Author-reported | p. 8 |
| Context impact | 19; 27.9 | count; percent | 68 findings | Author-reported | p. 8 |
| External rate-limit impact | 5; 7.4 | count; percent | 68 findings | Author-reported | p. 8 |
| Baseline timeout budget | 180 | seconds/project | All three methods | Author-reported | p. 9 |
| Pure API file cap | 80 | files/project | Baseline input constraint | Author-reported | p. 9 |
| Pure API text cap | 3,000 | characters/file | Baseline input constraint | Author-reported | p. 9 |
| Subset file population | 34,634 | Python files | 264 projects | Author-reported | p. 9 |
| Files read by pure API | 12,958 | files | Includes partial reads | Author-reported | p. 9 |
| Files read in full | 9,233 | files | Pure API baseline | Author-reported | p. 9 |
| Any-read file fraction | ≈37.4 | percent | 12,958 / 34,634 × 100 | Analyst-derived | p. 9 operands |
| Full-read file fraction | ≈26.7 | percent | 9,233 / 34,634 × 100 | Analyst-derived | p. 9 operands |
| Known-union coverage | ≈90.7 | percent | 68 / (68 + 7) × 100; not corpus recall | Analyst-derived | pp. 9–10 operands |
| Repeated runs | 3 | runs | Same subset/configuration | Author-reported | p. 10 |
| CPU configuration | 2; 256 | processors; logical cores | AMD EPYC 9554 | Author-reported | p. 7 |
| GPU configuration | 6; 80 | GPUs; GB per GPU | NVIDIA A100 | Author-reported | p. 7 |
| Operating system | 24.04.3 LTS | Ubuntu version | Single experiment server | Author-reported | p. 7 |
| Graph type counts | 12; 10 | node kinds; edge kinds | ALDG representation | Author-reported | pp. 5–6 |

The indirect bounds in false-positive cases include max_iterations=3, max_tool_calls=2, and a bounded two-turn exchange. These values explain specific reviewed exceptions rather than recommended universal limits. The three-day/$1,200 trip in F1 is illustrative. No approximate visual estimates are needed: reported numeric table values are readable. [A/B; pp. 2, 9]

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Relevant unbounded agent feedback can amplify work | Definition, threat model, visible feedback examples | F1–F2, F6–F7 | pp. 1–3, 8–9 | HIGH for stated mechanism; no measured live exploit rate |
| Framework interfaces require semantic normalization | API taxonomy and framework-model procedure | T1, F3, L1 | pp. 3–5 | HIGH for described design; comparative literature judgment unverified |
| Effective coverage differs from a visible exit | Output-controlled example and bound-check procedure | F2, F5, L3 | pp. 3, 6–7 | HIGH; indirect bounds remain difficult |
| Default pipeline has 91.9% precision | 68 confirmed of 74 findings | X1 | p. 8 | HIGH for reporting; manual author review |
| Findings span eight framework families | Full distribution | T2 | p. 8 | HIGH; no framework exposure denominators |
| Pruning reduces default review volume | 340 alerts without pruning versus 74 full | T3, X3 | p. 9 | HIGH for setup; pruning can lose true positives |
| Full system outperforms selected baselines on reference coverage/cost | 68 vs 50 vs 23 reference coverage, reported averages | T4, X4 | p. 9 | HIGH for reported comparison; bounded inputs/time and selected subset |
| IAL-SCAN misses some failures | Seven confirmed baseline-only cases | X6 | pp. 9–10 | HIGH; unknown additional misses |
| Static and pruning stability differ | Same 340 candidates; changing coverage | T5, X7 | p. 10 | HIGH for three runs |
| Pruning model choice materially changes coverage | 41–68 covered reference positives | T6, X8 | p. 10 | HIGH for reported conditions; no alternative-model repeat intervals |
| Added agent feedback informs the web-agent security question | Ordinary untrusted inputs can influence actions, observations, errors | Threat model and examples | pp. 2–3, 8–9 | MEDIUM analyst inference; no direct standalone/web comparison |
| Universal deployment protection is not established | Four stated limitations and observed FP/FN cases | S6B, X5–X6 | pp. 9–10 | HIGH for limits; broader generalization UNKNOWN |

## 22. Very simple explanation — Explain Like I'm 15

Imagine an assistant that can ask an AI for a plan, check the answer, use tools, and ask again. That is useful when a task needs several steps. But if the assistant keeps saying 'try again' whenever the answer is bad, and nobody sets a limit, one request can turn into a long chain of expensive work.

The paper's key point is that a possible stopping instruction is not the same as a reliable limit. 'Stop when the AI gives the right answer' depends on what the AI produces. 'Stop after a fixed number of attempts or a timeout that covers this whole retry process' can actually constrain the repeated path. A limit inside one small step may still leave the larger process repeating.

The researchers built a program that reads agent code, connects model calls, tools, state updates, and workflow routes, and looks for repeated paths without effective limits. In 6,549 projects it raised 74 findings, and the authors confirmed 68. The program also missed at least seven cases found during extra review, and its AI-based filtering sometimes removed real problems.

This helps explain one reason agents can create security risks beyond a direct text-generation interaction: their outputs can become new actions, observations, and more calls. The paper does not prove that web agents are always more vulnerable than standalone models. It shows a particular added failure mechanism and why budgets, retry limits, timeouts, and state-size limits need to cover the whole repeating process.

## Completeness Audit

The denominator is the supplied inventory: seven main numbered sections with their substantive subsections, three research questions, eight analysis records, seven figures, six tables, three listings, three formal construction-rule groups, one algorithm, three stated contribution groups, four author limitations, metadata, abstract, acknowledgement, footnote, and bibliography. 'Represented in compressed form' means the substantive content is retained while wording, repeated motivation, or secondary examples are condensed.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| META, ABS, corresponding-author footnote | Yes, text and image | Yes | Represented in compressed form | Title/authors/date/affiliation and abstract findings retained |
| S1 Introduction and contributions | Yes | Yes | Represented in compressed form | Problem, three challenges, three contributions |
| S2A Agent loops | Yes | Yes | Fully represented substantively | Iteration, APIs, bounds, F1 |
| S2B Related static analyses | Yes | Yes | Represented in compressed form | Categories retained; cited works not independently reviewed |
| S3A Definition | Yes | Yes | Fully represented | Structural feedback and effective-bound requirement |
| S3B Assumptions | Yes | Yes | Fully represented | Fixed/nonmalicious trusted components and possible weak safeguards |
| S3B Attacker capabilities | Yes | Yes | Fully represented | Normal input interfaces, influence, excluded modification powers |
| S3B Scope | Yes | Yes | Fully represented | Included toolchain loops and all stated exclusions |
| S3C Motivating example | Yes | Yes | Fully represented substantively | Feedback, growth, inner-break scope, missing local bound |
| S3D Challenges 1–3 | Yes | Yes | Fully represented | Framework encoding, reconstruction, coverage |
| S4A Schema | Yes | Yes | Fully represented | Six fact sets and nine relations |
| S4A Program extraction | Yes | Yes | Fully represented substantively | Index, AST, lightweight resolution, fact tuple |
| S4A Framework modeling | Yes | Yes | Fully represented substantively | Construction/invocation/configuration and unresolved targets |
| S4B Node construction | Yes | Yes | Fully represented | Retained sets, attributes, 12 kinds |
| S4B Edge construction | Yes | Yes | Fully represented substantively | Categories, 10 kinds, auxiliary-element reachability |
| S4B Loop annotation | Yes | Yes | Fully represented | Cost/growth/exit/guard/bound properties |
| S4C SCC discovery | Yes | Yes | Fully represented | Subgraph, SCC/self-loop, eligibility/filtering |
| S4C Controller/bound verification | Yes | Yes | Fully represented | Controller classes, coverage targets, statuses |
| S4C Identification/pruning | Yes | Yes | Fully represented | Three conditions, bounded slices, negative predicates |
| S5A Implementation/environment | Yes | Yes | Fully represented for reported detail | Missing versions/settings explicitly identified |
| S5A Dataset/review protocol | Yes | Yes | Fully represented for reported detail | Counts, inclusion/exclusion, independent author review |
| S5B Overall findings/cases | Yes | Yes | Fully represented substantively | X1–X2, full T2 values, both cases |
| S5C Ablation | Yes | Yes | Fully represented | X3 and every T3 row |
| S5C Baselines | Yes | Yes | Fully represented | X4, every T4 row, input/time restrictions |
| S5C False positives | Yes | Yes | Represented in compressed form | Six bounds described, including reported numerical caps |
| S5C False negatives | Yes | Yes | Fully represented substantively | X6, alert reduction, seven misses, denominator caveat |
| S5D Repeatability | Yes | Yes | Fully represented | X7 and every T5 row |
| S5D Sensitivity | Yes | Yes | Fully represented | X8 and every T6 row |
| S6A Implications | Yes | Yes | Fully represented substantively | Framework/application bound and state recommendations |
| S6B Limitations 1–4 | Yes | Yes | Fully represented | Separate from analyst observations |
| S7 Conclusion | Yes | Yes | Represented in compressed form | Integrated with orientation/contributions |
| RQ1, RQ2, RQ3 | Yes | Yes | Fully represented | Explicit wording and analysis connections |
| Formal hypotheses | No such item present | Absence stated | Not present in supplied material | None manufactured |
| X1–X8 | Yes | Yes | Fully represented substantively | Separate purposes, conditions, results, caveats |
| F1 | Yes, visually | Yes | Fully represented | Conceptual colors/arrows and illustrative task |
| F2 | Yes, visually | Yes | Fully represented substantively | Two panels, code semantics, line-label uncertainty |
| F3 | Yes, visually | Yes | Fully represented substantively | Inputs/stages/decisions/output witness |
| F4 / E1–E3 | Yes, visually and text | Yes | Fully represented substantively | Notation, rules, plain-language interpretation |
| F5 | Yes, visually | Yes | Fully represented substantively | Control/state feedback, exits, label caveats |
| F6 | Yes, visually | Yes | Fully represented substantively | Nested parser/validation retry |
| F7 | Yes, visually | Yes | Fully represented substantively | Exact guard distinguished from caption |
| T1 | Yes, visually and text | Yes | Fully represented substantively | All program-role rows explained |
| T2 | Yes, visually and text | Yes | Fully represented | All counts/ratios/project counts retained |
| T3 | Yes, visually and text | Yes | Fully represented | All numerical rows/conditions retained |
| T4 | Yes, visually and text | Yes | Fully represented | All numerical rows and note qualifications |
| T5 | Yes, visually and text | Yes | Fully represented | All three runs |
| T6 | Yes, visually and text | Yes | Fully represented | All four model conditions |
| L1 | Yes | Yes | Fully represented substantively | Schema/relations, exact formatting compressed |
| L2 | Yes | Yes | Represented in compressed form | Example facts and semantic roles retained |
| L3 | Yes | Yes | Fully represented | All covered/uncovered status names |
| ALG1 | Yes, visually and text | Yes | Fully represented substantively | Every procedural stage, abstract helper limits |
| Contributions C1–C3 | Yes | Yes | Fully represented | Definition, detector, real-world findings |
| Author limitations LIM1–LIM4 | Yes | Yes | Fully represented | All four explicitly separated |
| ACK | Yes | Yes | Represented in compressed form | ChatGPT/Codex polishing/refinement disclosure |
| REF [1]–[39] | Yes, text and image | Yes, by role | Represented in compressed form | Bibliographic details not reproduced individually |
| REF [40]–[41], p. 12 | Yes, text only | Yes, by role | Represented in compressed form | No visual-inspection claim for p. 12 |
| Appendices | None supplied | Absence stated | Not present in supplied material | No appendix content reviewed |
| Complete prompts/artifacts mentioned on p. 9 | No | Limitation stated | Missing from supplied material | No inferred prompt contents or artifact validation |
| Executable analyzer/snapshots/annotation records | No | Limitation stated | Not supplied | Reproduction and operational exploit testing unavailable |

### Missing or inaccessible material

Page 12 has no supplied rendering, although its reference text is accessible. The complete baseline prompts and associated artifacts mentioned on p. 9 are absent. Executable code, project snapshots, complete case evidence, model configuration, and review records are not provided. Their absence limits reproduction checking and independent case validation. No appendix or supplied supplement was omitted from inspection because none appears in this input.

### Uncertain interpretations

Figure 2's annotation line numbers do not precisely match displayed code lines. Figure 5's small model-call glyph and MIXED controller label require contextual interpretation; the exact classification rationale is unspecified. Figure 7's title is broader than its immediate retry condition. Table IV's timeout column includes a prose description of timeout or error limits. The formal algorithm leaves helper procedures and complete kind enumerations abstract. No global recall, framework-specific vulnerability rate, live exploit success rate, or standalone-versus-web-agent risk ratio can be established.

### Deliberately compressed material

Repeated motivation and conclusions are integrated rather than restated paragraph by paragraph. Full code listings are explained semantically instead of reproduced verbatim. The bibliography is summarized by methodological role; individual publication metadata and links are secondary to this paper's findings. Decorative framework logos, layout boxes, author email typography, and other nonanalytic page decoration are accounted for but not described pixel by pixel. No result-bearing table row is deliberately dropped.

### Potential omissions

Every substantive object identified in the supplied inventory is represented above, with compressed and inaccessible material explicitly distinguished. This is an inventory-based account of the supplied pages, not a claim that all associated research artifacts, implementation details, deployment behavior, or external citations have been reviewed. Confidence is HIGH for the main extracted definitions and numerical tables, MEDIUM for broader security relevance and methodological implications, and UNKNOWN for absent artifacts and unmeasured comparative vulnerability.
