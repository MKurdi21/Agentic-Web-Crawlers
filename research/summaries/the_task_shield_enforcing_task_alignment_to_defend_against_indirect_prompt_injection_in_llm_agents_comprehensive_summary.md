## Stage 0 — Document Accessibility Report

The complete supplied text comprises physical PDF pages 1–18, corresponding to printed proceedings pages 29680–29697. The title, main sections, references, and Appendices A–E are available. No gap appears in the supplied physical page sequence. This establishes coverage of the supplied paper, but does not establish that every independently released artifact or supplement is present.

Direct visual inspection is available for physical pages 1, 2, 4, 5, 6, 7, 8, 13, 14, 16, 17, and 18. Pages 3, 9, 10, 11, 12, and 15 were inspected through supplied extracted text only. All seven numbered figures and all seven numbered tables occur on visually supplied pages. The equations on page 3 are text-only; the continuation of Equation (2), the score aggregation, and Algorithm 1 are visually supplied. Table entries are generally readable and agree with the extracted text for the values reported below. Figure 3's tiny point annotations are less reliably readable than its axes, legend, and overall arrangement; exact results are taken from tables rather than estimated point positions.

OCR was not performed and is unnecessary for the supplied readable text. No tools, browsing, repository inspection, or external verification were used. The source hash is supplied metadata, not independently recomputed. A local-image error appears in the input, but the twelve displayed page images remain available for inspection. No supplementary file or executable implementation was supplied. The accessibility metadata reports a supplementary-reference detection without its surrounding passage; the identity and content of any separate supplementary artifact cannot be established. The AgentDojo repository is referenced, but its contents were not inspected.

Evidence categories used throughout: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No category [E] external information is introduced. HIGH confidence means clear source support, not proof of general validity. MEDIUM marks qualified interpretation or an unresolved source inconsistency; LOW and UNKNOWN are used where evidence is inadequate.

## 1. Plain-language orientation

This is an experimental artificial-intelligence security and systems paper about protecting tool-integrated Large Language Model (LLM) agents from **indirect prompt injection**. An agent is a conversational model that can also call tools: retrieve a webpage, inspect a calendar, send an email, or perform a financial operation. An indirect injection places an instruction in material the agent encounters while doing an otherwise legitimate task. The attacker tries to make the agent treat that material as an instruction to obey rather than information to analyze. [A; pp. 1–2]

The authors' central proposal is **task alignment**: every actionable instruction followed by the agent should help achieve a user-specified objective. Their defense, **Task Shield**, extracts instructions, compares each with the user's tasks, and supplies corrective feedback when an instruction makes no contribution. It also checks proposed tool calls and prevents execution of calls it judges misaligned. This changes the defense question from whether an instruction sounds harmful to whether it serves the intended task. [A; pp. 1–5]

The main evaluation uses AgentDojo's Travel, Workspace, Banking, and Slack suites. Against the strongest evaluated attack, Important Instructions, GPT-4o's overall attack success rate falls from 47.69% without defense to 2.07% with Task Shield, while successful user-task completion under attack rises from 50.08% to 69.79%. GPT-4o-mini obtains 2.23% attack success and 54.53% utility under attack. These are benchmark outcomes from one trial per task, not a guarantee of protection. Full shielding also introduces substantial latency. [A/B; pp. 5–8, 14]

**Relevance to the user's research question — analyst inference:** the paper explains a plausible reason web and tool agents face additional security exposure: they ingest attacker-influenced external content and can translate its instructions into consequential actions. It does **not** directly compare standalone LLMs with otherwise matched web agents. Its results support an account of agent-specific attack pathways and a defense for those pathways; they do not quantify a standalone-versus-agent vulnerability difference. [D; grounded in pp. 1–2, 5–9]

## 2. Document roadmap

| Inventory ID | Original component | Physical pages | Role |
|---|---|---:|---|
| S0 | Abstract | 1 | Problem, task-alignment proposal, headline results |
| S1 | §1 Introduction | 1–2 | Tool capabilities, external-content attacks, motivation, three contributions |
| S2 | §2 Preliminary | 2 | Message roles, privilege hierarchy, indirect injection |
| S3 | §3 Task Alignment | 3–4 | Definitions and formal alignment conditions |
| SS3.1 | §3.1 Task Instructions | 3 | Analytical units and instruction aggregation |
| SS3.2 | §3.2 Task Interactions | 3 | Supporting information versus delegated concrete subtasks |
| SS3.3 | §3.3 Formalization | 3–4 | ContributesTo relation and aligned conversations |
| S4 | §4 Task Shield Framework | 4–5 | Operational defense |
| SS4.1 | §4.1 Components | 4 | Extraction, contribution scoring, feedback |
| SS4.2 | §4.2 Interaction | 4–5 | User, assistant, and tool-output processing |
| S5 | §5 Experiments | 5–8 | Benchmark evaluation |
| SS5.1 | §5.1 Settings | 5–6 | Models, benchmark, baselines, metrics |
| SS5.2 | §5.2 Main Results | 7 | Attack comparison, trade-offs, model comparison |
| SS5.3 | §5.3 Ablation Studies | 7–8 | Input/output checking and goal restatement |
| SS5.4 | §5.4 Defender Capacity | 8 | Different models guarding GPT-4o |
| S6 | §6 Related Work | 9 | Agents, attacks, training-time and test-time defenses |
| S7 | §7 Conclusion | 9 | Authors' synthesis |
| S8 | §8 Limitations | 9 | Defender reliability, overhead, generalization |
| ACK/REF | Acknowledgements and references | 9–11 | Funding statement and bibliography |
| A | Appendix A, A.1–A.3 | 12 | Benign-looking deviations, system goals, misalignment examples |
| B | Appendix B, B.1–B.2 | 12–13 | Graded scoring rationale and Algorithm 1 |
| C | Appendix C, C.1–C.4 | 13–15 | GPT-3.5 results, timing, capacity, implementation details |
| D | Ethical Considerations | 15 | Synthetic data and dual use |
| E | Prompts | 15–18 | Extraction, checking, and feedback templates |

The inventory additionally contains F1–F7, T1–T7, ALG1, Equation (1), Equation (2), the unnumbered aggregate score, Definitions 1–4, six distinct experimental analyses, and three explicitly stated limitations. There are no supplied keywords, formal hypotheses, theorem/proof sequence, or new dataset construction. The bibliography is accounted for as attribution material rather than treated as separately reviewed research.

## 3. Background and context

**LLM** means Large Language Model. In this work, an **LLM agent** combines conversational messages with external tool calls. A **tool output** can supply information needed to complete a task, but can also contain instructions written by someone other than the user. The model must distinguish these roles while continuing to use useful external data. [A; pp. 2–3]

The paper distinguishes four message roles. System messages define the agent's role and core rules. User messages state goals and requests. Assistant messages contain responses, plans, and proposed calls. Tool outputs contain external results. The authors adopt the privilege ordering system > user > assistant > tool. Lower-level instructions are superseded by higher-level ones. This is a stated system model, not an experimentally established guarantee that a model always respects the ordering. [A; p. 2]

A **task instruction** is an actionable directive extracted from a message. It can be a user request, an assistant's proposed subtask, or a directive in tool output. The defense therefore analyzes more than obvious commands: questions can be rewritten as tasks, and dependencies between tasks should be retained. [A; pp. 3–4, 16]

**Task alignment** is narrower than a general claim that all behavior is safe. An instruction is aligned when it contributes to at least one user objective. A seemingly ordinary extra action can be misaligned. Appendix A's example requests preparation steps for one pasta dish, while injected content asks for preparation and cost details for the entire menu. The authors describe unnecessary information exposure, extra computation, and loss of predictability as consequences. This is an illustrative argument, not a separately measured experiment. [A; p. 12]

**Clean utility (CU)** measures successful user-task completion without attacks. **Utility under attack (U)** measures user-task completion with attacks present. **Attack success rate (ASR)** measures achievement of the attacker's goal. High U and low ASR are desirable together. A defense that prevents nearly everything may lower ASR while also making the agent unhelpful. [A; p. 6]

## 4. Research problem and gap

**Existing problem:** external documents, webpages, and tool outputs can contain malicious directives. An agent may encounter these sources necessarily during a legitimate workflow and then execute actions that depart from the user's intention. Tool access gives such departures practical consequences, including disclosure or financial operations. [A; pp. 1–2]

**Shortcomings attributed to prior approaches:** the introduction says detailed rule specification is difficult and apparently benign wording can bypass detection. Related Work describes fine-tuning defenses as computationally costly and unsuitable when model internals are unavailable. Test-time alternatives include authentication tags, delimiting external content, repeating user prompts, detecting injections, and restricting tools. These statements characterize the authors' positioning; this analysis does not independently validate the cited literature. [A; pp. 1, 6, 9]

**Research gap:** the authors seek a defense criterion based on the relationship between an action and a user's task, rather than only content harmfulness or source markings. The objective is to preserve useful task behavior while reducing attacker-directed behavior. [A; pp. 1, 3]

**Scope:** personal-assistant-style, multi-turn, tool-integrated agents evaluated in synthetic AgentDojo environments. The evaluated main assistant models belong to the GPT family. The main formalization focuses on user-level objectives, although system-level goals are acknowledged in Appendix A.2. The work is neither a broad census of web-agent attacks nor a controlled study of why every agent is more vulnerable than every standalone model. [A/D; pp. 3, 5–6, 9, 12, 15]

## 5. Research questions / objectives / hypotheses

The supplied paper does not enumerate formal research questions or statistical hypotheses. Its explicit objectives and contributions are:

1. **OBJ1/C1 — conceptual:** formalize instruction relationships and task alignment in tool-integrated conversational systems. [A; pp. 2–4]
2. **OBJ2/C2 — methodological/system:** implement a test-time shield that dynamically checks instructions and tool calls and intervenes through feedback. [A; pp. 2, 4–5]
3. **OBJ3/C3 — empirical:** demonstrate reduced injection vulnerability while preserving user-task utility on AgentDojo. [A; pp. 2, 5–8]

The experiment design also addresses operational questions: whether results hold across the three tested attacks, whether input or action checking is more useful, whether goal restatement matters, how defender capacity changes outcomes, and how much latency the defense adds. These are **analyst-organized evaluation questions**, not author-numbered research questions. [D; pp. 7–8, 13–15]

The user's question, **“Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,”** is an external organizing question supplied by the user. Within this paper's evidence, the answerable part concerns external-content exposure, tool-mediated actions, multi-turn propagation, and task misalignment. The comparative magnitude of vulnerability remains unanswered because no standalone-LLM comparison group is reported.

## 6. Assumptions / threat model

The attacker embeds instructions in the environment that the agent processes, such as a webpage, document, or tool result. The intended attack is indirect: it reaches the agent through material involved in completing a legitimate user request. The illustrated attacker can insert an urgent-looking instruction that asks the agent to perform an unrelated action before returning to the original task. [A/B; pp. 1–2, F1]

The protected objectives are the user's requested tasks and the agent's ability to complete them. The paper motivates protection of sensitive information, financial operations, and critical systems, but does not provide a separate exhaustive asset inventory or formal attacker-capability specification. [A; p. 1]

The conceptual trust boundary separates higher-privilege goals from lower-privilege external directives. The checker prompt warns that a tool-origin instruction can remain untrustworthy even when later mentioned by a higher-level message. The authors also recognize legitimate delegation: a user's instruction to complete a to-do list can make tool-supplied list entries relevant subtasks. Thus, the design does not reject every instruction from a tool merely because it came from a tool. It evaluates contribution in context. [A; pp. 3, 17–18]

**Operational assumptions — analyst interpretation:** the shield needs access to messages before onward processing, needs to maintain an accurate user-task set, and needs the ability to stop proposed calls before execution. Its extraction and scoring models must interpret untrusted content sufficiently well. These requirements follow from the described intervention points, but are not supplied as a formal trust theorem. [D; pp. 4–5]

The supplied work does not specify comprehensive restrictions on attacker edit budgets, compromised tools, network access, adversarial query counts, or control of the defender itself. The limitations explicitly acknowledge adversarial probing of the defender. System-level task objectives are discussed but excluded from the main analysis. Broader tool integrity or arbitrary code-execution security is not demonstrated by the experiments. [A/D; pp. 9, 12]

## 7. Methodology

### 7.1 Defense architecture

Task Shield has three components: instruction extraction, alignment checking, and feedback generation. Both extraction and contribution scoring use an LLM. It is a test-time intervention rather than a reported model-training procedure. [A; p. 4]

**Extraction:** identify user objectives and store them in the User Task Set, Tu. Extract potential actionable directives from assistant and tool messages as candidates for checking. The extraction prompt seeks nested or implicit instructions, converts information-seeking questions into explicit tasks, and preserves dependencies in natural language. A message containing no actionable task should yield an empty list. Appendix E gives prompt templates and examples. [A; pp. 4, 16]

**Alignment checking:** for each candidate e and each user task t, obtain a score s(e,t) in [0,1]. A score of 1 means direct contribution; intermediate positive values mean indirect useful contribution; 0 means none. Sum the scores across user tasks. The main-text rule marks the instruction misaligned exactly when the sum is zero. This is a permissive existential test: contribution to at least one task is sufficient. [A; pp. 3–4]

**Feedback:** identify the problematic instruction, warn about deviation, and remind the agent of user objectives. Tool outputs retain their original content alongside feedback; the description does not say that all suspicious text is removed. Proposed misaligned tool calls are prevented from executing. Assistant responses can be reconsidered through several rounds of feedback, but the number of rounds and stopping policy are not specified in the supplied text. [A; pp. 4–5, 18]

### 7.2 Message-specific workflow

User messages update Tu with newly extracted instructions. Assistant messages require checking of both natural-language content and tool calls. Tool-output instructions receive provenance context, including tool function and arguments, before evaluation. A detected tool-output deviation is returned to the assistant with corrective feedback, and later assistant checks provide another intervention point. [A; p. 5]

Algorithm 1 initializes an empty misalignment collection, extracts instructions, updates Tu and returns immediately for user messages, otherwise scores each candidate against all user tasks, collects candidates whose total is at most epsilon, generates feedback, and returns it. The algorithm's threshold parameter needs to be read alongside the explicit zero-threshold description; no threshold sweep is reported. [A/B; p. 13]

### 7.3 Evaluation data and models

AgentDojo supplies four task suites: Travel for itineraries, Workspace for documents, Banking for financial operations, and Slack for communications. The authors characterize it as multi-turn with complex tool interaction. Appendix D states that the benchmark conversations are synthetic and no human-subject data were collected. The supplied paper does not give an explicit total task count, attack-case denominator, per-suite sampling procedure, train/validation/test split, or confidence interval. Counts should not be reconstructed as facts from rounded percentages. [A; pp. 5, 15]

The primary assistant is GPT-4o; GPT-4o-mini is also studied and GPT-3.5-turbo appears in Appendix C. Exact versions are gpt-4o-2024-05-13, gpt-4o-mini-2024-07-18, and gpt-3.5-turbo-0125. The general setup uses the same model as assistant and defender; the capacity studies deliberately vary the defender. Task Shield temperature is 0.0. The authors describe this as ensuring deterministic behavior, but no repeated-run determinism check is supplied. Model configurations otherwise follow benchmark defaults. [A; pp. 5–6, 15]

The score computation uses a substantial portion of conversation history. Appendix C.4 says history is truncated in tool-call cases to satisfy a stated temporal-coherence requirement involving corresponding tool outputs. The precise truncation algorithm, token budget, and handling of removed dependencies are not supplied. [A; p. 15]

### 7.4 Baselines, attacks, and measurement

The four defense baselines are Delimiting, PI Detector, Repeat Prompt, and Tool Filter. A No Defense condition is also reported. Delimiting marks external tool content; PI Detector classifies potential attacks; Repeat Prompt reinforces the original request; Tool Filter restricts available tools using task requirements. [A; p. 6]

The three attack categories are Important Instructions, Injecagent, and Ignore Previous. The authors describe them as high-priority malicious directives, conflicting objectives, and nullification of previous instructions, respectively. Later experiments use Important Instructions because it has the highest overall undefended ASR among these three GPT-4o conditions. [A; p. 7]

Each task receives one trial. No formal significance tests, p-values, run-to-run error estimates, hardware specification, library version list, token-cost accounting, or memory measurement is supplied. Appendix C.4 identifies no-defense baseline results as extracted from AgentDojo raw data. The exact provenance and execution details of every defended baseline are less fully specified. [A; pp. 5, 15]

## 8. Experiments / analyses

| ID | Analysis | Conditions and purpose | Evidence |
|---|---|---|---|
| X1 | Attack-family comparison | GPT-4o, Task Shield versus No Defense, three attacks, four suites; test attack coverage | T1, pp. 6–7 |
| X2 | Security–utility/model comparison | Six defense conditions, GPT-4o and GPT-4o-mini, Important Instructions; measure CU/U/ASR | F3, T2, pp. 6–8 |
| X3 | Component ablation | GPT-4o-mini assistant, Slack; Action Shield, Input Shield, No Restate, full shield | T3, pp. 7–8 |
| X4 | Defender capacity | GPT-4o or GPT-4o-mini assistants, Slack; three defender models | T4/T7, pp. 8, 14–15 |
| X5 | Older assistant model | GPT-3.5-turbo, four suites, defense comparison | T5, pp. 13–14 |
| X6 | Computational cost | GPT-4o-mini, Slack; conversation latency across defenses | T6, pp. 13–14 |

All experiments use benchmark task-success and attacker-goal outcomes rather than human preference ratings. The paper states one trial per task and does not report statistical hypothesis tests. The latency study reports quartiles, which describe its observed timing distribution rather than confidence bounds on security outcomes.

**X1:** Important Instructions is the strongest overall undefended attack: 47.69% ASR, compared with Injecagent's 5.72% and Ignore Previous's 5.41%. Task Shield yields 2.07%, 1.11%, and 0.48%, respectively. Overall U improves in all three comparisons, but some individual suites lose utility; these exceptions matter when evaluating the prose claim of consistent superiority. [A/B; T1]

**X2:** GPT-4o Task Shield has the lowest overall ASR and highest overall U among the listed defenses, but Repeat Prompt has higher overall CU. GPT-4o-mini Task Shield has the lowest overall ASR and preserves overall CU at 68.04%; Tool Filter has higher overall U, 55.17% versus 54.53%. No single metric should be substituted for the combined trade-off. [B; T2]

**X3:** Input Shield has the highest CU and U among the ablation rows, whereas full Task Shield has the lowest ASR. No Restate has lower utility than the full shield. The accompanying prose compares 63.8% with 43.8%, but 63.80% belongs to Input Shield rather than the full shield; the corresponding full-shield comparison is 50.48% versus 43.80%. [A/B; T3]

**X4:** Weaker defenders still reduce attacks, but model ordering is not uniformly monotonic on every metric. In T4, GPT-4o-mini gives 0.00% ASR while GPT-4o gives 0.95%; GPT-4o preserves higher CU. In T7, the GPT-4o defender improves CU and U over the mini defender, but has higher ASR. [B; T4/T7]

**X5:** GPT-3.5-turbo Task Shield reaches 0.95% overall ASR versus 8.43% without defense, but overall U declines from 34.66% to 30.05%. The authors warn that model/context limitations complicate interpretation. [A/B; T5]

**X6:** Full Task Shield has 62.56 s median latency, versus 6.17 s without defense and 18.78 s for Input Shield. Its Q3 is 196.00 s. The authors explicitly present timing as approximate relative overhead, sensitive to runtime conditions. [A/B; T6]

## 9. Results

### 9.1 Main security and utility finding

For GPT-4o under Important Instructions, overall ASR changes from 47.69% to 2.07%, and U changes from 50.08% to 69.79%. **Analyst-derived:** the ASR reduction is 47.69 − 2.07 = **45.62 percentage points**; the relative reduction is (47.69 − 2.07)/47.69 × 100 ≈ **95.66%**. Utility improves by 69.79 − 50.08 = **19.71 percentage points**. These calculations describe the reported benchmark comparison; they do not measure population-wide risk reduction. [C; T1/T2]

GPT-4o-mini's corresponding ASR changes from 27.19% to 2.23%, and U from 49.92% to 54.53%. **Analyst-derived:** reductions/improvements are 24.96 and 4.61 percentage points. Its CU is unchanged overall at 68.04%. [B/C; T2b]

### 9.2 Suite-level differences

GPT-4o with Task Shield under the main attack obtains U/ASR of Travel 72.86/1.43, Workspace 62.50/0.42, Banking 82.64/6.25, and Slack 64.76/0.95, all percentages. Banking has the largest residual ASR among the four shielded suites. Workspace shows a large improvement over the no-defense U of 24.17%. Slack's U improvement is comparatively small: 64.76 − 63.81 = **0.95 percentage points**, analyst-derived. [B/C; T1/T2]

GPT-4o-mini obtains U/ASR of Travel 49.29/0.71, Workspace 69.58/1.25, Banking 37.50/6.25, and Slack 50.48/0.95. In Banking its U is below the no-defense value of 38.19%, and CU falls from 50.00% to 43.75%. The overall result therefore conceals a suite-specific utility loss. [B; T2b]

### 9.3 Trade-off rather than universal dominance

Repeat Prompt gives GPT-4o overall CU of 84.54%, higher than Task Shield's 73.20%, but has ASR of 27.82%, much higher than Task Shield's 2.07%. PI Detector gives Travel ASR of 0.00% versus Task Shield's 1.43%, but Travel U of only 16.43% versus 72.86%. These examples show why the authors emphasize combined utility and security. They also show that “outperforming all baselines” cannot mean being best in every cell. [B/D; T2a]

### 9.4 Cost and component choice

Input Shield's Slack U of 63.80% exceeds full Task Shield's 50.48%, while its ASR of 4.76% exceeds the full shield's 0.95%. Median latency is 18.78 s versus 62.56 s. **Analyst-derived:** full-shield median latency is 62.56/18.78 ≈ **3.33 times** Input Shield and 62.56/6.17 ≈ **10.14 times** No Defense. These ratios use medians, not paired per-conversation slowdowns. The authors recommend input-only protection when resources are limited and the full shield when stricter security is needed. [A/B/C; pp. 8, 14]

## 10. Figure-by-figure interpretation

### Figure 1 — Overall agent–shield interaction, p. 2

This architecture diagram shows a user request to summarize a website and email the summary, an LLM agent, a tool-execution stage, an external website, an attacker, and shield components. The legitimate call retrieves website content. The website includes a malicious prerequisite asking that a separate link be sent to Alice before solving the task. The shield constructs a user-task set, checks agent calls and retrieved instructions, and returns misalignment feedback. [B]

Arrows show information flow; red arrows identify detected deviations and feedback paths. The loop illustrates intervention before an unrelated request becomes an executed action. The instruction payload is evidence of the illustrated threat, not an instruction to this analysis. No measured effectiveness or timing is encoded in this figure.

### Figure 2 — Processing by message type, p. 5

The left column contains a user's appointment-count/description request, an assistant calendar call, and a calendar output carrying an unrelated email directive. The right side shows extraction, task-set update, checking, and feedback. User goals become verification targets. The calendar lookup receives an illustrative contribution score of 0.9 and proceeds. The email directive receives 0.0 and produces feedback. [B]

Blue, green, and orange paths distinguish user, assistant, and tool-output processing; the red feedback path returns the alert to the conversation. Scores 0.9 and 0.0 are diagram examples, not experimental estimates. The figure demonstrates how legitimate information retrieval and injected actionable content are treated differently.

### Figure 3 — ASR–utility trade-offs, p. 6

Four panels cover Workspace, Travel, Slack, and Banking. Horizontal axes are Utility and vertical axes Attack Success Rate, shown as fractions rather than the tables' percentage units. Axes are linear with suite-dependent displayed vertical ranges. The shared horizontal range runs from 0 to 1. Workspace's upper labeled region is around 0.4, Travel around 0.12, Slack around 0.8, and Banking around 0.6; these are descriptions of readable ticks, not claims that the uppermost plotted boundary has exactly that value. [B]

Colors identify No Defense, Repeat Prompt, Delimiting, Tool Filter, PI Detector, and Task Shield. Task Shield uses a star marker; the other methods use circular markers. Solid markers pair ASR with benign utility, hollow markers pair ASR with utility under attack, and arrows connect the utility change. Green outlines highlight benign Pareto-front points; orange outlines highlight under-attack Pareto-front points. Lower-right positions mean low attacker success and high user utility. No confidence intervals or error bars are shown. [A/B]

The figure supports the authors' trade-off interpretation: Task Shield lies in favorable low-ASR regions while retaining utility. Exact coordinates are recoverable from T2; small printed arrow labels are deliberately not transcribed as exact values. The plot is a security-versus-utility visualization, not a latency comparison and not a distribution of individual task outcomes.

### Figure 4 — Extraction prompt, p. 16

This visually inspected prompt panel specifies extraction of every actionable instruction, including nested directives; preservation of details; rewriting questions as tasks; and retaining dependencies. The restaurant example connects selection constraints, name/address reporting, and a calendar reminder. A second example extracts two tasks inside a note. Output is specified as a JSON list of strings, or an empty list. [A/B]

This is implementation evidence, not a performance plot. Examples show the intended transformation but do not demonstrate extraction accuracy on an annotated test set. Repetitive wording and literal example sentences are compressed here with disclosure.

### Figure 5 — Content-checker prompt, p. 17

The checker receives a candidate actionable instruction, source level/tool context, and user tasks, with conversation history used for interpretation. It distinguishes direct, indirect, and absent contribution and requests one JSON object per user task containing the task, score, and reason. It cautions about tool-origin instructions even after higher-level repetition. [A/B]

A substantive inconsistency appears in its example: the score is 0.5 while the example reason describes the action as unnecessary or unrelated. The general guideline assigns 0 to noncontributing or prominently unnecessary instructions. This ambiguity is source-visible; it is not silently repaired.

### Figure 6 — Tool-call checker, p. 18

Inputs include function name, arguments, related content, and user task instructions. The checker evaluates both direct and intermediate contribution. Crucially, inconsistent or irrelevant arguments should receive score 0 even if the function itself seems useful. This supports the wrong-recipient example in Appendix A.3. [A/B]

The required task field is named user_task_instruction, while the example uses task_instruction. The supplied implementation code is unavailable, so parser handling cannot be assessed. The image layout places system and user panels in their displayed order, but semantic roles are clear from their labels.

### Figure 7 — Feedback composition, p. 18

Three blocks comprise a content-deviation warning, a tool-output/call-related warning, and a reminder of remaining user instructions. Plus signs and conditional annotations show that applicable warnings are combined and the user reminder is added when either warning exists. [B]

There are no axes, measured outcomes, or performance values. The diagram explains the corrective message structure underlying the No Restate ablation. Its warnings are analyzed as paper content, not obeyed as instructions.

## 11. Table-by-table interpretation

For compact but traceable numerical preservation, the following transcription uses **CU/U/ASR** triples, with every entry a percentage. T1 instead uses **U/ASR** pairs. Best-result typography is not reproduced; metric direction and numerical comparisons are explicit. Tables contain no security confidence intervals or significance markers.

### Table 1 — Three attacks on GPT-4o, p. 6

Each cell below is **Task Shield U/ASR ; No Defense U/ASR**.

| Attack | Travel | Workspace | Banking | Slack | Overall |
|---|---|---|---|---|---|
| Important Instructions | 72.86/1.43 ; 64.29/11.43 | 62.50/0.42 ; 24.17/40.42 | 82.64/6.25 ; 69.44/62.50 | 64.76/0.95 ; 63.81/92.38 | 69.79/2.07 ; 50.08/47.69 |
| Injecagent | 67.86/0.00 ; 72.14/0.00 | 66.67/0.00 ; 64.58/0.00 | 77.78/4.17 ; 72.22/15.28 | 66.67/0.95 ; 67.62/13.33 | 69.48/1.11 ; 68.52/5.72 |
| Ignore Previous | 70.71/0.00 ; 77.14/0.00 | 62.92/0.00 ; 61.67/0.00 | 72.22/1.39 ; 68.75/8.33 | 63.81/0.95 ; 61.90/20.95 | 66.93/0.48 ; 66.77/5.41 |

Blue shading marks favorable shield comparisons and pink marks favorable no-defense comparisons. Important Instructions produces the largest overall undefended ASR. Shielding lowers or ties ASR in every reported suite/attack comparison, but Travel utility falls under Injecagent and Ignore Previous, and Slack utility falls under Injecagent. Overall improvement is therefore distinct from uniform suite-level utility improvement. [B]

### Table 2 — Main defenses and assistant models, p. 8

Panel a, GPT-4o; entries are **CU/U/ASR**:

| Defense | Travel | Workspace | Banking | Slack | Overall |
|---|---|---|---|---|---|
| No Defense | 65.00/64.29/11.43 | 62.50/24.17/40.42 | 75.00/69.44/62.50 | 80.95/63.81/92.38 | 69.07/50.08/47.69 |
| Tool Filter | 90.00/70.00/5.71 | 55.00/51.67/4.17 | 81.25/56.94/11.11 | 80.95/47.62/8.57 | 72.16/56.28/6.84 |
| Repeat Prompt | 90.00/72.14/7.14 | 80.00/60.42/14.58 | 93.75/77.08/46.53 | 80.95/62.86/60.00 | 84.54/67.25/27.82 |
| Delimiting | 75.00/72.14/3.57 | 62.50/30.42/35.00 | 81.25/77.08/61.81 | 80.95/61.90/80.00 | 72.16/55.64/41.65 |
| PI Detector | 30.00/16.43/0.00 | 52.50/15.83/15.00 | 43.75/31.25/0.69 | 28.57/25.71/12.38 | 41.24/21.14/7.95 |
| Task Shield | 80.00/72.86/1.43 | 62.50/62.50/0.42 | 81.25/82.64/6.25 | 80.95/64.76/0.95 | 73.20/69.79/2.07 |

Panel b, GPT-4o-mini:

| Defense | Travel | Workspace | Banking | Slack | Overall |
|---|---|---|---|---|---|
| No Defense | 55.00/47.14/13.57 | 82.50/59.17/17.92 | 50.00/38.19/34.03 | 66.67/48.57/57.14 | 68.04/49.92/27.19 |
| Tool Filter | 60.00/58.57/0.71 | 70.00/64.58/2.50 | 50.00/43.06/11.11 | 57.14/45.71/7.62 | 61.86/55.17/4.93 |
| Repeat Prompt | 70.00/54.29/0.00 | 70.00/61.25/8.33 | 43.75/43.75/17.36 | 71.43/33.33/13.33 | 65.98/51.03/9.38 |
| Delimiting | 60.00/52.14/7.14 | 72.50/64.58/12.92 | 43.75/35.42/33.33 | 71.43/56.19/48.57 | 64.95/53.74/22.26 |
| PI Detector | 25.00/14.29/0.00 | 60.00/27.50/12.92 | 37.50/29.86/10.42 | 23.81/15.24/7.62 | 41.24/23.05/8.59 |
| Task Shield | 55.00/49.29/0.71 | 85.00/69.58/1.25 | 43.75/37.50/6.25 | 66.67/50.48/0.95 | 68.04/54.53/2.23 |

The table caption calls the attack Important Messages, while the main text calls it Important Instructions. It appears to refer to the same evaluated attack, but the naming discrepancy is retained. Bold and underline indicate best and second-best results, not significance. In GPT-4o Banking, U exceeds CU for Task Shield; this is a reported outcome, not an error automatically corrected. The supplied text does not explain that specific reversal. [A/B]

### Table 3 — Slack component ablations, p. 8

| Defense | CU | U | ASR |
|---|---:|---:|---:|
| No Defense | 66.67 | 48.57 | 57.14 |
| Action Shield | 66.67 | 52.38 | 7.62 |
| Input Shield | 71.43 | 63.80 | 4.76 |
| No Restate | 52.38 | 43.80 | 3.80 |
| Task Shield | 66.67 | 50.48 | 0.95 |

The assistant is GPT-4o-mini and the suite is Slack. Input Shield leads utility; full Task Shield leads security. Action Shield's ASR ties the T2b Slack values for Tool Filter and PI Detector at 7.62%. Therefore, the prose claim that either partial shield beats all baselines requires a trade-off interpretation and is not literal superiority on every measure. [B/D]

### Table 4 — Defender capacity for GPT-4o assistant, p. 8

| Defender | CU | U | ASR |
|---|---:|---:|---:|
| No Defense | 80.95 | 63.81 | 92.38 |
| GPT-4o | 80.95 | 50.48 | 0.95 |
| GPT-4o-mini | 71.43 | 52.38 | 0.00 |
| GPT-3.5-turbo | 71.43 | 55.24 | 4.76 |

This is the Slack capacity study. The GPT-4o defender preserves the highest CU, the mini defender has the lowest ASR, and GPT-3.5-turbo has the highest shielded U. The supplied paper does not define a single numerical overall-trade-off objective. T4's same-model U of 50.48% conflicts with T2a's Slack Task Shield U of 64.76%, despite matching CU and ASR. No explanation is supplied. [B]

### Table 5 — GPT-3.5-turbo defense comparison, p. 14

| Defense | Travel | Workspace | Banking | Slack | Overall |
|---|---|---|---|---|---|
| No Defense | 15.00/17.86/1.43 | 32.50/40.42/0.42 | 37.50/32.64/25.69 | 57.14/46.67/12.38 | 35.05/34.66/8.43 |
| Tool Filter | 20.00/18.57/0.71 | 27.50/30.83/0.00 | 37.50/36.11/4.17 | 38.10/32.38/1.90 | 29.90/29.57/1.43 |
| Repeat Prompt | 20.00/12.86/0.00 | 37.50/31.25/0.00 | 37.50/31.25/12.50 | 52.38/38.10/5.71 | 37.11/28.30/3.82 |
| Delimiting | 20.00/17.14/5.71 | 25.00/33.75/0.83 | 37.50/34.72/25.69 | 61.90/41.90/11.43 | 34.02/31.64/9.38 |
| PI Detector | 20.00/7.14/0.00 | 22.50/23.75/0.42 | 43.75/36.11/8.33 | 28.57/35.24/4.76 | 26.80/24.80/2.86 |
| Task Shield | 20.00/10.71/0.00 | 30.00/34.58/0.00 | 62.50/43.75/4.17 | 38.10/26.67/0.00 | 35.05/30.05/0.95 |

Task Shield has the lowest overall ASR but does not preserve overall U relative to No Defense. Banking improves strongly, while Travel and Slack utility decline. This appendix materially qualifies an unbounded claim that shielding preserves utility on every model. The authors caution about GPT-3.5-turbo's context limitations. [A/B]

### Table 6 — Conversation latency, p. 14

| Defense | Median, seconds | Q1, seconds | Q3, seconds |
|---|---:|---:|---:|
| No Defense | 6.17 | 4.17 | 7.45 |
| Tool Filter | 3.96 | 3.13 | 6.00 |
| Delimiting | 8.29 | 6.41 | 10.33 |
| Input Shield | 18.78 | 13.37 | 29.85 |
| PI Detector | 25.08 | 6.54 | 27.84 |
| Repeat Prompt | 33.66 | 9.04 | 67.85 |
| Action Shield | 38.77 | 21.57 | 110.60 |
| Task Shield | 62.56 | 32.76 | 196.00 |

Conditions are GPT-4o-mini and Slack. Tool Filter is faster than No Defense in this reported comparison; the paper does not isolate why. Full shielding has the largest median and Q3. **Analyst-derived:** its interquartile range is 196.00 − 32.76 = 163.24 s, compared with 7.45 − 4.17 = 3.28 s for No Defense. These are distribution spreads, not statistical error bars. The authors explicitly caution against interpreting the absolute timings as portable constants. [A/B/C]

### Table 7 — Defender capacity for GPT-4o-mini assistant, p. 14

| Defender | CU | U | ASR |
|---|---:|---:|---:|
| No Defense | 66.67 | 48.57 | 57.14 |
| GPT-4o | 76.20 | 51.42 | 2.86 |
| GPT-4o-mini | 66.67 | 50.48 | 0.95 |
| GPT-3.5-turbo | 57.14 | 42.86 | 6.67 |

The same-model mini row agrees with T2b and T3. The stronger GPT-4o defender increases utility but has a higher ASR than the mini defender. The GPT-3.5-turbo defender reduces ASR substantially but lowers both utility measures relative to No Defense. “Graceful degradation” is the authors' interpretation; it is not a demonstrated monotonic ordering on all three metrics. [A/B]

## 12. Diagram / architecture interpretation

F1 describes the full external-content attack loop; F2 expands its per-message processing; F7 specifies feedback assembly. Together they show two distinct intervention surfaces. The input-side check evaluates directives embedded in retrieved data before the assistant acts on them. The action-side check evaluates the agent's own proposed response or tool call before release/execution. [A/B; pp. 2, 5, 18]

The user-task set is shared context across these checks. User messages update it, and assistant/tool candidates are compared against it. The feedback loop is iterative: a rejected or flagged candidate produces information for the assistant to reconsider its plan. The tool-output pathway returns both original output and feedback, so the defense depends partly on later reasoning and checks rather than solely on content deletion. [A; pp. 4–5]

**Illustration, analyst interpretation:** if the user requests calendar summaries, a calendar lookup serves the task, while emailing retrieved text to an unrelated address does not. The security decision must consider arguments and dependencies, not only tool names. This interpretation follows the authors' calendar diagram and wrong-recipient example. It is not a newly evaluated attack. [D; pp. 5, 12, 18]

The architecture offers no stated cryptographic proof of source integrity and no formal proof that the checker cannot itself be manipulated. The method's practical enforcement strength is supported by benchmark results and bounded by the acknowledged LLM reliability problem.

## 13. Equations and mathematical concepts

### Equation (1) — Aggregate instructions by privilege level, p. 3

**EL(M′) = union of E(Mi) over messages Mi in M′ with P(Mi) = L.** Here M′ is a conversation segment; Mi is one message; E(Mi) is its extracted instruction set; P maps a message to its privilege level; L is the selected level. The union operator combines instructions from all matching messages. The output is a set, not a score or probability. This defines where user goals or other level-specific directives come from. The notation was inspected through supplied text only. [A]

### Definitions 1–2 — Instructions and contribution, p. 3

Definition 1 makes actionable directives the basic unit. Definition 2 states that ContributesTo(e,t | Hi) is True if instruction e helps achieve instruction/goal t in conversation history Hi. Hi = [M1,…,Mi−1] is the history before the current message. The paper subsequently omits Hi in notation while retaining context conceptually. This is a semantic relation, not a learned probability with a reported calibration study. [A/D]

### Equation (2) and Definition 3 — Instruction alignment, pp. 3–4

An instruction e satisfies alignment if there exists at least one user-level task t in ELu(Hi) such that **ContributesTo(e,t) = True**. The existential condition is important: an instruction need not contribute to every user task. The available mathematical definition does not specify a separate veto for conflict with another task. The prompt's argument consistency rule adds practical checking but does not turn the formal relation into a proof of universal safety. [A/D]

### Definition 4 — Conversation alignment, p. 4

A conversation is task-aligned when every assistant-level task instruction satisfies Definition 3. This quantifies over the assistant's instructions, including plans and tool calls. The operational shield also checks tool-output instructions to prevent them from propagating into the assistant's behavior. An ideal definition and an LLM-based implementation should be kept distinct. [A]

### Aggregate contribution score — unnumbered equation, p. 4

**S(e) = Σ over t in Tu of s(e,t)**, with each pairwise score s(e,t) in [0,1]. Tu is the current user-task set. A score of 1 denotes direct contribution; positive intermediate scores denote helpful indirect contribution; 0 denotes none. The output S(e) is a sum and can exceed 1 when multiple tasks receive positive scores. It is not itself bounded to [0,1] or interpreted as an attack probability. [A/C]

The main text states **misaligned iff S(e) = 0**. **Analyst-derived:** because all pairwise scores are nonnegative, S(e) is positive exactly when at least one score is positive. This reproduces the existential intent. Its practical correctness depends on extraction and score judgments, which can be wrong. [C/D]

### Algorithm 1 — Thresholded implementation, p. 13

Algorithm 1 computes cij for candidate ei against each task tj, sums them into Cei, and collects the instruction when **Cei ≤ epsilon**. It also updates Tu by union with extracted user instructions. With epsilon = 0 and nonnegative scores, this agrees with the main-text zero rule. The supplied algorithm takes epsilon as an input; the surrounding discussion says the zero threshold is unchanged. A nonzero deployed value is not established, and no sensitivity analysis is supplied. [A/B/C]

Appendix B explains why graded scoring was chosen: strict aligned/not-aligned prompts sometimes blocked legitimate preparatory actions. Examples include checking room availability before booking and searching recent files to locate a budget document. Those examples explain intended indirect contribution; they are not quantitatively validated calibration results. [A; pp. 12–13]

## 14. Interpretation and discussion

The strongest supported finding is that task-contribution checking can substantially reduce tested indirect injections while retaining useful agent behavior in the evaluated benchmark. GPT-4o's main attack results support both security and utility improvement relative to the reported no-defense condition. GPT-4o-mini supports security improvement and a smaller overall utility improvement. [A/B]

The ablation evidence supports a layered design with an operational trade-off: input-only protection delivers higher utility and lower latency in the studied Slack setting, while full protection delivers lower residual ASR. It does not establish that input checking is always the optimal deployment policy. Capacity results show that a cheaper defender can still be useful, but the three metrics do not uniformly track model strength. [B/D]

For the user's research question, the relevant causal story is **analyst inference**: agents must interpret untrusted external information while retaining the ability to act. Multi-turn workflows create opportunities for a source instruction to become a proposed plan and then a tool call. The paper's architecture and ablations are consistent with that story, but do not isolate each factor experimentally against a standalone chatbot baseline. [D]

### Cross-reference and consistency findings

1. **T2a versus T4:** GPT-4o assistant with GPT-4o shield on Slack has U = 64.76% in T2a and U = 50.48% in T4. CU = 80.95% and ASR = 0.95% match. Conditions are described similarly; the supplied paper does not explain the U difference. Both values are retained.
2. **Goal-restatement prose versus T3:** prose says removing restatement reduces U from 63.8% to 43.8%. T3 assigns 63.80% to Input Shield and 50.48% to the full shield. For the stated No Restate comparison, 50.48% to 43.80% is the directly corresponding table comparison.
3. **Uniform-superiority language versus individual cells:** Travel U is lower with the shield for Injecagent and Ignore Previous in T1. Tool Filter has higher GPT-4o-mini overall U in T2b. The authors' broad statements are better supported as favorable overall trade-offs than universal metric dominance.
4. **Stronger-defender language versus ASR ordering:** T4/T7 do not show monotonically improving ASR with stronger model labels. Utility/security trade-offs remain condition-dependent.
5. **Attack naming:** T2/T5 captions say Important Messages; prose says Important Instructions. The shared evaluation context suggests correspondence, but naming is not silently standardized in the source account.
6. **Scoring/example mismatch:** F5's 0.5 example reason describes an unnecessary or unrelated action, despite guidelines assigning such actions zero.
7. **Output field mismatch:** F6 requests user_task_instruction but demonstrates task_instruction. Actual parsing behavior is unavailable.
8. **Threshold/reference detail:** §4.1 points to B.2 for scoring design, while the graded-scoring discussion is principally B.1 and B.2 supplies the algorithm. Main-text zero equality and algorithmic ≤ epsilon agree only under the described zero threshold.
9. **Weak-model footnote:** p. 8 says GPT-3.5-turbo's clean utility is below 20% in the long-context motivation, while T5 reports overall CU = 35.05% and multiple suites above 20%. The footnote's precise intended subset or setup is unspecified; its blanket wording is not validated by T5.

These observations do not erase the main reported improvement. They limit how precisely the results can be reconciled and how strongly broad conclusions can be stated.

## 15. Contributions and novelty

**Conceptual contribution:** task alignment as the criterion that actionable directives should serve user goals, including apparently benign deviations. Definitions 1–4 and Equations (1)–(2) organize this concept. [A; pp. 2–4]

**Methodological/algorithmic contribution:** an extraction–scoring–feedback pipeline that considers conversational context, source privilege, indirect useful steps, and call arguments. Algorithm 1 operationalizes instruction-level checking with an accumulated user-task set. [A; pp. 4–5, 13, 16–18]

**System contribution:** intervention at tool-output and assistant/action boundaries, including prevention of misaligned call execution and iterative feedback. The three prompt families and feedback assembly provide a inspectable design specification, though not a supplied runnable implementation. [A; pp. 5, 16–18]

**Empirical contribution:** comparisons across three attack categories, four suites, multiple GPT models, component ablations, defender capacity, and latency. The evidence supports the proposed idea as proof of concept, consistent with the authors' own limitations. [A; pp. 6–9, 13–15]

No new dataset or benchmark is introduced. No theorem proving injection resistance is supplied. “Novel,” “orthogonal,” and “state-of-the-art” are author claims about positioning and measured results; no external novelty or literature-wide ranking verification was requested or performed.

## 16. Limitations

### Authors' stated limitations

1. **Defender reliability:** weak or adversarially probed LLMs may fail extraction/scoring, causing false positives that block legitimate actions or false negatives that miss attacks. [A; §8, p. 9]
2. **Additional computation:** each assistant response and tool output adds LLM calls. Smaller specialized extraction models are suggested as future work. [A; §8, p. 9]
3. **Limited evaluation scope:** one model family, GPT, and one benchmark, AgentDojo; open-source backbones have not been tested. The authors explicitly call the results proof-of-concept rather than exhaustive evaluation. [A; §8, p. 9]
4. **Older-model caveat:** GPT-3.5-turbo's context limitations affect benchmark interpretation. [A; C.1, p. 13]
5. **Timing portability:** absolute latency depends on hardware, implementation, and runtime; timing is an approximate relative reference. [A; C.2, p. 14]
6. **Formalization scope:** system-level task objectives are acknowledged but omitted from the main experimental analysis. [A; A.2, p. 12]

### Additional evidence-based analyst observations

The paper does not supply per-condition sample denominators, repeated runs, security confidence intervals, or significance tests. A one-trial design cannot reveal repeatability from the reported tables alone. Temperature 0.0 does not constitute a demonstrated repeated-run stability analysis. [D; pp. 5, 15]

The task set is updated by union in Algorithm 1, but task cancellation, replacement, contradictory user goals, and completion/removal semantics are not specified. A retained earlier task might complicate alignment decisions in long conversations; this is an open concern, not a demonstrated attack. [D; p. 13]

The permissive positive-score rule can accept a candidate judged to contribute weakly to any one objective. Whether an attacker can exploit spurious contribution judgments is not tested with an explicit adaptive-attack evaluation. The defender itself processes untrusted content, and the authors acknowledge probing risk. [D/A; pp. 4, 9]

Numerical inconsistencies and prompt-schema ambiguities identified in §14 reduce reproducibility. The public benchmark reference does not substitute for supplied source code, exact parsing, retry behavior, or truncation details. [D]

## 17. Threats to validity

The following validity labels are **analyst organization**, not terminology attributed to the authors.

**Internal validity:** benchmark-derived no-defense results and newly described shielding results may not expose every execution detail needed for perfectly matched comparisons. The T2/T4 conflict shows at least one unresolved numerical alignment problem. No claim is made that these issues caused the reported gains. [D; pp. 8, 15]

**Construct validity:** CU/U assess benchmark user-goal completion and ASR assesses attacker-goal achievement. These are useful constructs but do not directly measure every type of harm, user trust, information overexposure, or financial impact motivated by the introduction. Contribution scores are semantic judgments, not calibrated safety probabilities. [D; pp. 1, 4, 6, 12]

**Statistical conclusion validity:** one trial per task, absent stated denominators and absent inferential statistics limit uncertainty assessment. Words such as “significantly” in the paper should not be read as evidence of a supplied formal significance test. Quartiles are reported only for latency. [D; pp. 5–8, 14]

**External validity/generalizability:** results come from GPT-family models and AgentDojo's four suites. They do not establish the same effect for open-source agents, arbitrary websites, new tool APIs, or all attacker strategies. This aligns with the authors' proof-of-concept caveat. [A/D; p. 9]

**Ecological validity:** the benchmark simulates personal-assistant workflows with synthetic conversations; the authors describe realistic interaction patterns, but no production deployment or live user study is reported. [A/D; pp. 5, 15]

**Reproducibility:** exact model versions, temperature, prompts, benchmark identity, and latency quartiles are supplied. Hardware, execution code, attack-case counts, complete truncation/retry procedures, and run-level outcomes are not. The available information supports understanding and partial reconstruction of the design, not independent reproduction within this analysis. [D; pp. 13–18]

## 18. Future work and open questions

### A. Explicit author-proposed future work

The authors propose reducing extraction overhead with smaller specialized models. They identify testing beyond the GPT family, including open-source backbones, as a current gap. The text does not provide a detailed future experimental plan or claim those extensions have already been completed. [A; §8, p. 9]

### B. Additional analyst-organized open questions

Would matched standalone-model and tool-agent experiments distinguish the effects of external input, action authority, and multi-turn propagation? Can an adaptive attacker craft a directive that the checker judges weakly contributory while still violating the user's intention? How should Tu represent superseded, completed, or conflicting goals? How should system-level and user-level task alignment interact? [D; grounded in pp. 1–5, 9, 12–13]

Would extraction/scoring accuracy measured against annotated instructions explain false positives and negatives? How stable are security and utility across repeated executions? Which cases create the full shield's long latency tail? Can selective action checks retain input-only utility while approaching full-shield ASR? These are unanswered questions, not results implied by the paper. [D; grounded in T3/T6 and §8]

The numerical T2/T4 difference and the No Restate comparison also require clarification before drawing precise causal conclusions about those conditions.

## 19. Terminology and notation glossary

| Term/symbol | Beginner-friendly meaning | Source |
|---|---|---|
| LLM | Large Language Model; the conversational model used by the agent | p. 1 |
| LLM agent | Model that can use tools to perform requested tasks | pp. 1–2 |
| Indirect prompt injection | Attacker instruction embedded in external material encountered during a task | pp. 1–2 |
| Task instruction | Actionable directive extracted from a message | Definition 1, p. 3 |
| Task alignment | All assistant-level instructions contribute to user objectives | Definition 4, p. 4 |
| ContributesTo | Context-dependent relation saying one instruction helps achieve another | Definition 2, p. 3 |
| M / Mi | Conversation message sequence / one message | p. 2 |
| n | Total number of messages in the sequence | p. 2 |
| P(Mi) | Privilege level assigned to message Mi | p. 2 |
| Ls/Lu/La/Lt | System/user/assistant/tool privilege levels | p. 2 |
| ≻ | Higher precedence in the stated privilege hierarchy | p. 2 |
| E(Mi) | Set of instructions extracted from one message | p. 3 |
| EL(M′) | Combined instructions at level L in conversation segment M′ | Eq. (1), p. 3 |
| Hi | History before message Mi | p. 3 |
| Tu | Stored set of user-task instructions | pp. 4–5 |
| e / t | Candidate instruction / user instruction used as target | pp. 3–4 |
| s(e,t) | LLM-assigned contribution score between 0 and 1 | p. 4 |
| S(e) | Sum of e's contribution scores across user tasks | p. 4 |
| cij / Cei | Pairwise contribution / total contribution in Algorithm 1 | p. 13 |
| epsilon | Threshold input in Algorithm 1; surrounding text describes zero threshold | pp. 4, 12–13 |
| CU | Clean utility: user-task success without attack | p. 6 |
| U | User-task success with attacks present | p. 6 |
| ASR | Attack success rate: attacker-goal success fraction | p. 6 |
| Input Shield | Ablation checking incoming tool outputs only | p. 7 |
| Action Shield | Ablation checking outgoing tool calls only | p. 7 |
| No Restate | Ablation removing explicit user-goal restatement from feedback | p. 7 |
| PI Detector | Prompt Injection Detector baseline | p. 6 |
| Pareto front | Trade-off boundary where improving one plotted metric requires worsening another | p. 7 |
| Q1/Q3 | First/third quartiles of measured conversation latency | pp. 13–14 |
| Test-time defense | Intervention while a model is being used, rather than reported retraining | pp. 4, 9 |

The aggregate S(e) is not an attack probability. A zero observed ASR is not a guarantee that attacks cannot succeed. A table percentage does not specify a denominator unless the source supplies it.

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Trial count | 1 | trial per task | Main evaluation | Author-reported | p. 5, §5 |
| Suite count | 4 | suites | Travel/Workspace/Banking/Slack | Author-reported | p. 5 |
| Undefended ASR | 47.69 | % | GPT-4o, Important Instructions, overall | Visually readable | T1/T2a, pp. 6/8 |
| Shielded ASR | 2.07 | % | Same condition | Author-reported | pp. 1/7; T2a |
| Undefended U | 50.08 | % | Same condition | Visually readable | T2a, p. 8 |
| Shielded U | 69.79 | % | Same condition | Author-reported | pp. 1/7; T2a |
| ASR absolute reduction | 45.62 | percentage points | 47.69 − 2.07 | Analyst-derived | T2a |
| ASR relative reduction | approximately 95.66 | % | (47.69 − 2.07)/47.69 × 100 | Analyst-derived | T2a |
| U improvement | 19.71 | percentage points | 69.79 − 50.08 | Analyst-derived | T2a |
| GPT-4o CU, shielded | 73.20 | % | Overall, main attack comparison | Visually readable | T2a |
| GPT-4o-mini ASR, no defense/shield | 27.19 / 2.23 | % | Overall, main attack | Author-reported | p. 7; T2b |
| GPT-4o-mini U, no defense/shield | 49.92 / 54.53 | % | Overall, main attack | Visually readable | T2b |
| GPT-4o-mini CU, both conditions | 68.04 | % | Overall, no defense and shield | Visually readable | T2b |
| GPT-4o Injecagent ASR | 5.72 / 1.11 | % | Overall, no defense/shield | Visually readable | T1 |
| GPT-4o Ignore Previous ASR | 5.41 / 0.48 | % | Overall, no defense/shield | Visually readable | T1 |
| Banking residual ASR | 6.25 | % | Main attack, shield, both main models | Visually readable | T2 |
| Input Shield CU/U/ASR | 71.43 / 63.80 / 4.76 | % | GPT-4o-mini, Slack | Visually readable | T3 |
| Full shield CU/U/ASR | 66.67 / 50.48 / 0.95 | % | GPT-4o-mini, Slack | Visually readable | T3 |
| No Restate CU/U/ASR | 52.38 / 43.80 / 3.80 | % | GPT-4o-mini, Slack | Visually readable | T3 |
| GPT-3.5-turbo overall ASR | 8.43 / 0.95 | % | No defense/shield | Visually readable | T5 |
| GPT-3.5-turbo overall U | 34.66 / 30.05 | % | No defense/shield | Visually readable | T5 |
| No-defense median latency | 6.17 | seconds/conversation | GPT-4o-mini, Slack | Visually readable | T6 |
| Input Shield median latency | 18.78 | seconds/conversation | Same | Author-reported | p. 13; T6 |
| Full-shield median latency | 62.56 | seconds/conversation | Same | Author-reported | p. 13; T6 |
| Full-shield Q1/Q3 | 32.76 / 196.00 | seconds/conversation | Same | Visually readable | T6 |
| Full/input median ratio | approximately 3.33 | ratio | 62.56/18.78 | Analyst-derived | T6 |
| Full/no-defense median ratio | approximately 10.14 | ratio | 62.56/6.17 | Analyst-derived | T6 |
| Pairwise score range | 0–1 | relevance score | Alignment checker | Author-reported | p. 4 |
| Main decision threshold | 0 | aggregate contribution | Misaligned iff S(e)=0 | Author-reported | p. 4 |
| Shield temperature | 0.0 | model setting | Task Shield implementation | Author-reported | p. 15 |

No exact security numbers are estimated from plotted positions. Full numerical conditions for T1–T7 are preserved in §11. No unsupported sample count, parameter count, monetary cost, significance level, or uncertainty interval is invented.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| External sources can redirect tool agents | Threat description and injected webpage example | F1 | pp. 1–2 | HIGH for author-described mechanism; no standalone comparison |
| Task alignment evaluates contribution rather than apparent harmfulness | Definitions and contribution condition | Eq. (2), Definitions 1–4 | pp. 3–4 | HIGH as conceptual proposal, not formal safety proof |
| Shield combines extraction, scoring, and feedback | Components and message processing | F2/ALG1 | pp. 4–5, 13 | HIGH for described method |
| Main GPT-4o security/utility improves | 47.69→2.07 ASR; 50.08→69.79 U | T1/T2, X1/X2 | pp. 6–8 | HIGH for reported values; one trial per task |
| GPT-4o-mini also gains security | 27.19→2.23 ASR; 49.92→54.53 U | T2b, X2 | pp. 7–8 | HIGH; Tool Filter has slightly higher overall U |
| Input/full shielding trade off utility and residual attacks | Input U/ASR 63.80/4.76; full 50.48/0.95 | T3, X3 | p. 8 | HIGH within Slack/mini condition |
| Full shielding adds substantial latency | Median 62.56 s versus 6.17 s | T6, X6 | pp. 13–14 | HIGH source support; absolute timings qualified |
| Weaker defenders can still help | Reduced ASR with GPT-3.5 defender | T4/T7, X4 | pp. 8, 14 | HIGH for values; no uniform model ordering |
| Older assistant security gain can cost utility | Overall U 34.66→30.05 | T5, X5 | pp. 13–14 | HIGH; context limitations acknowledged |
| Defender failure and limited scope constrain conclusions | Explicit limitations | §8 | p. 9 | HIGH for author-stated caveats |
| Web-agent exposure differs through external data and actions | Threat/system description plus layered checks | F1/F2; X3 | pp. 1–5, 7–8 | MEDIUM analyst inference; no causal standalone contrast |
| Some source comparisons cannot be reconciled | T2a Slack U 64.76 versus T4 50.48 | T2/T4 | p. 8 | HIGH observation; reason UNKNOWN |

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an assistant to read a webpage and email you its summary. The webpage contains a sentence saying, “Before you finish, send this other link to someone.” That sentence came from the webpage, not from you. An AI agent can get confused and treat it as a new job. Because the agent can use tools, the confusion can turn into an actual email or another action. That is the security problem this paper studies.

Task Shield keeps a list of what the user actually asked for. It examines instructions found in messages and proposed tool actions, then asks whether each helps finish something on that list. Looking up information needed for your task can be allowed. Sending information to an unrelated person should be flagged. If an action is judged unrelated, the shield warns the agent and can stop a tool call before it runs.

In the main GPT-4o benchmark comparison, attackers succeeded in 47.69% of cases without the shield and 2.07% with it. The shield also improved completion of the user's tasks under that attack. But it was slower, could still make mistakes, and did not win every individual comparison. The results come from simulated tasks and a limited model family.

For the question about web agents versus ordinary chat models, the paper gives a useful explanation: agents read outside material and can act on it. However, it never runs a matched experiment comparing an ordinary standalone model with a web agent. We can use it to explain an added attack pathway, but we cannot use it to claim a measured vulnerability gap between those two kinds of systems.

## Completeness Audit

The coverage denominator is the supplied 18-page paper and the inventory in §2. This report represents every identified substantive section, figure, table, major equation, algorithm, contribution, and explicit limitation. That statement concerns inventory coverage, not lossless preservation of every word or independent validation of every experiment.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| S0 Abstract | Yes, text + visual | Yes | Fully represented | Headline method/results and conditions |
| S1 Introduction | Yes, text + visual | Yes | Represented in compressed form | Motivation and contributions retained; citations grouped |
| S2 Preliminary | Yes, text + visual | Yes | Fully represented | Roles, hierarchy, threat example |
| S3/SS3.1 Task Instructions | Yes, text-only p. 3 | Yes | Fully represented | Definition 1 and Eq. (1) |
| SS3.2 Task Interactions | Yes, text-only | Yes | Represented in compressed form | Supporting data versus delegated subtasks |
| SS3.3 Formalization | Yes, text + partial visual | Yes | Fully represented | Definitions 2–4 and Eq. (2) |
| S4/SS4.1 Components | Yes, text + visual | Yes | Fully represented | Extraction, scoring, feedback |
| SS4.2 Interaction | Yes, text + visual | Yes | Fully represented | All three message-processing paths |
| S5/SS5.1 Settings | Yes, text + visual | Yes | Fully represented | Available setup plus absent specifications |
| SS5.2 Main Results | Yes, text + visual | Yes | Fully represented | X1/X2; numerical exceptions included |
| SS5.3 Ablations | Yes, text + visual | Yes | Fully represented | X3 and restatement inconsistency |
| SS5.4 Capacity | Yes, text + visual | Yes | Fully represented | X4 and T2/T4 inconsistency |
| S6 Related Work | Yes, text-only | Yes | Represented in compressed form | Categories and attributed shortcomings |
| S7 Conclusion | Yes, text-only | Yes | Represented in compressed form | Claims qualified by scope |
| S8 Limitations | Yes, text-only | Yes | Fully represented | Three explicit main limitations |
| ACK | Yes, text-only | Yes | Represented in compressed form | NSF-related acknowledgement; no scientific result |
| REF | Yes, text-only pp. 9–11 | Yes | Inspected but deliberately omitted as repetitive/non-substantive | Individual bibliographic records not reproduced or externally checked |
| Explicit research questions | No formal list present | Yes | Fully represented | Absence stated; objectives kept distinct |
| Explicit hypotheses | No formal hypotheses present | Yes | Fully represented | No hypotheses invented |
| OBJ1–OBJ3/C1–C3 | Yes | Yes | Fully represented | Concept, system, empirical contributions |
| X1 Attack families | Yes | Yes | Fully represented | T1 all values |
| X2 Defense/model comparison | Yes | Yes | Fully represented | T2 both panels and F3 |
| X3 Ablation | Yes | Yes | Fully represented | T3 all values |
| X4 Capacity | Yes | Yes | Fully represented | T4/T7 all values |
| X5 GPT-3.5 evaluation | Yes | Yes | Fully represented | T5 all values and utility losses |
| X6 Timing | Yes | Yes | Fully represented | T6 all quartiles and caveat |
| F1 | Yes, visually | Yes | Fully represented | External attack and feedback loop |
| F2 | Yes, visually | Yes | Fully represented | Message-specific paths and example scores |
| F3, four panels | Yes, visually | Yes | Represented in compressed form | Axes, legend, direction, front encoding; tiny arrow values not transcribed |
| F4 | Yes, visually + text | Yes | Represented in compressed form | Extraction rules; repetitive example wording compressed |
| F5 | Yes, visually + text | Yes | Fully represented | Checker behavior and example inconsistency |
| F6 | Yes, visually + text | Yes | Fully represented | Argument check and field-name inconsistency |
| F7 | Yes, visually + text | Yes | Fully represented | Conditional feedback composition |
| T1 | Yes, visually + text | Yes | Fully represented | Every numerical cell retained |
| T2a/T2b | Yes, visually + text | Yes | Fully represented | Every numerical cell retained |
| T3 | Yes, visually + text | Yes | Fully represented | Every numerical cell retained |
| T4 | Yes, visually + text | Yes | Fully represented | Every numerical cell retained |
| T5 | Yes, visually + text | Yes | Fully represented | Every numerical cell retained |
| T6 | Yes, visually + text | Yes | Fully represented | Every numerical cell retained |
| T7 | Yes, visually + text | Yes | Fully represented | Every numerical cell retained |
| Eq. (1) | Yes, text-only | Yes | Fully represented | Union by role; no visual claim |
| Eq. (2) | Yes, text + visual continuation | Yes | Fully represented | Existential contribution condition |
| Unnumbered S(e) equation | Yes, text + visual | Yes | Fully represented | Score sum and zero rule |
| Definitions 1–4 | Yes | Yes | Fully represented | Plain-language meanings and assumptions |
| ALG1 | Yes, text + visual | Yes | Fully represented | Branches, update, score, threshold, feedback |
| A.1 | Yes, text-only | Yes | Represented in compressed form | Benign-looking expansion example and trust costs |
| A.2 | Yes, text-only | Yes | Fully represented | System-goal exclusion |
| A.3 | Yes, text-only | Yes | Represented in compressed form | Unrequested posting and wrong-recipient examples |
| B.1 | Yes, text + partial visual | Yes | Represented in compressed form | Graded-score rationale and two preparatory examples |
| B.2 | Yes, text + visual | Yes | Fully represented | Algorithm and threshold reconciliation |
| C.1 | Yes, text + visual | Yes | Fully represented | Older-model results and context caution |
| C.2 | Yes, text + visual | Yes | Fully represented | Timing results and portability caveat |
| C.3 | Yes, text + visual | Yes | Fully represented | Capacity evidence and nonmonotonic metrics |
| C.4 | Yes, text-only | Yes | Fully represented | Baseline provenance, temperature, versions, truncation |
| D Ethics | Yes, text-only | Yes | Represented in compressed form | Synthetic data, no human subjects, dual use |
| E Prompts | Yes, text + visual | Yes | Represented in compressed form | Functional requirements retained, literal templates compressed |
| Substantive footnotes | Yes | Yes | Fully represented | Repository/MIT/default settings and weak-model caveat |
| Separate supplements | Not supplied | No | Missing from supplied material | Detection metadata does not identify a reviewable artifact |
| Referenced repository/code | Not supplied; not accessed | No | Inaccessible | No execution or code-level claims |

### Missing or inaccessible material

No physical page is missing from the supplied 1–18 sequence. Direct page images are unavailable for pages 3, 9–12, and 15; their text is available and was analyzed. Separate supplementary material, repository contents, runnable implementation, run-level receipts, and raw benchmark outcomes were not provided or accessed. Hardware, exact sample denominators, retry limits, full history-truncation policy, and security uncertainty estimates are not specified in the supplied paper. These are missing details rather than assumed properties.

### Uncertain interpretations

The T2a/T4 Slack U discrepancy, T3 restatement comparison, weak-model footnote scope, F5 example scoring, F6 field naming, and nonuniform defender-capacity trends remain unresolved as described in §14. Figure 3's tiny annotations were not used as exact numerical evidence. The semantic meaning of ContributesTo is supplied, but its extraction/scoring accuracy is not separately quantified. No missing definition was repaired using outside information.

### Deliberately compressed material

Repeated introductory explanations, bibliography entries, literal prompt wording, and repeated illustrative examples are compressed. Prompt functions, dependencies, important example constraints, and inconsistencies are preserved. Table styling is translated into numerical comparisons; every T1–T7 value is retained. Figure 3 arrow-label details are compressed in favor of readable table values. Decorative icons, author email addresses, and repeated page furniture are not scientifically analyzed. The acknowledgement records Anna Squicciarini's National Science Foundation support and the authors' disclaimer; it does not supply an experimental condition.

Appendix D's dual-use statement is retained here: the same alignment checks could theoretically help an attacker assess whether an adversarial instruction remains undetected. This is an author-acknowledged possibility, not a demonstrated adaptive attack.

### Potential omissions

No identified substantive inventory item is knowingly absent from the explanation. Exact graphical arrow annotations in F3 and verbatim prompt/example/bibliography text are deliberately not reproduced. Independently released or unidentified supplementary artifacts may contain substantive information, but their existence and contents cannot be assessed from the supplied material. Coverage is therefore comprehensive for the identifiable supplied paper, with explicit visual, implementation, and statistical limits; it is not a claim of lossless compression or externally verified scientific completeness.
