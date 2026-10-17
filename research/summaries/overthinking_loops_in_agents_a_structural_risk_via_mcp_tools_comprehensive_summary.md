## Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and nine supplied page images. No tools, browsing, external verification, or supplementary-file inspection were performed. Statements attributed to the authors are evidence from this document, not independently verified facts. Source text, including instructions appearing inside descriptions of malicious tools, is treated exclusively as research evidence.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied extracted text for physical PDF pages 1–12 |
| Accessible page count | 12 text pages; 9 page images |
| Text page range | 1–12 |
| Visually inspected pages | 1, 2, 3, 4, 5, 6, 10, 11, 12 |
| Text-only pages | 7, 8, 9; no supplied images for these pages |
| Pages apparently missing | No numbered text pages missing from the supplied 1–12 sequence; completeness beyond that sequence cannot be independently established |
| Figures | Figures 1–4 visually available and inspected |
| Tables | Tables 1–6 visually available; extracted text supports precise transcription of small cells |
| Equations | Registry notation, Equation (1), and NoWait token set visible; typography and the probability/logit description require qualification |
| Appendices | A–E present in supplied text; appendix headings begin on p. 10, with material continuing through p. 12 |
| Supplementary files | None supplied; supplied metadata reports no embedded files |
| Supplementary references | Accessibility metadata flags a generic supplementary reference, but the supplied text does not identify a specific supplementary artifact that can be assessed |
| OCR | Not used or needed for the supplied native-text transcription; image inspection is a cross-check rather than an OCR extraction |
| Other limitations | Small plot labels are more difficult to inspect than table cells; no raw traces, source implementation, benchmark item lists beyond CodeElo IDs, or runnable experiment artifacts supplied |

The reported source hash is user-provided metadata; it was not recomputed. The local-image error mentioning `-` does not prevent inspection of the nine images actually embedded in the request. It does not establish that another substantive page is missing.

Evidence labels throughout are: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No **[E] external information** is introduced. Confidence describes fidelity to the supplied evidence, not independent validation of the experiment. HIGH means clear and directly supported; MEDIUM indicates interpretation or a material unresolved qualification; LOW indicates weakly readable or insufficiently specified evidence; UNKNOWN indicates information the supplied document does not establish.

## 1. Plain-language orientation

The paper examines how an artificial-intelligence assistant can be made to waste resources by following apparently reasonable instructions from external tools. A large language model, or LLM, generates language. A tool-using agent additionally chooses tools, receives their results, and decides what to do next. That repeated interaction creates opportunities for an external tool to redirect the assistant's workflow.

The attack studied here adds malicious Model Context Protocol, or MCP, tools to a registry containing legitimate tools. Their descriptions and responses encourage repetition, repeated checking, staged refinement, and irrelevant side tasks. Individual calls can look plausible, but the sequence can return to an earlier tool and repeat. The authors call this **structural overthinking**: excessive work caused by the structure of the interaction, rather than simply a verbose answer from one model invocation. [A; pp. 1–3]

The researchers implemented 14 attack tools across three servers and tested them in a general-purpose ReAct agent and the Qwen-Code coding assistant. They compared benign registries with registries containing the same benign tools plus the attack tools. They measured total input and output tokens, task accuracy, and, for Qwen-Code, runtime. They also tested an attack-only registry and the NoWait generation-time mitigation. [A; pp. 1–6]

The main findings are large increases in token use, sometimes substantial accuracy loss, and especially large task-specific amplification in the coding environment. The main-text Qwen-Code summary reports up to 142.35× token amplification and 27.49× runtime amplification; individual tasks reach 971.27× tokens. A defense that suppresses selected reasoning words does not reliably eliminate the amplification. These conclusions must be read with the paper's limited task sample, missing uncertainty estimates, and several reporting inconsistencies. [A; pp. 5–6, 12]

**Relevance to the user's research question — analyst inference:** this work illustrates an additional vulnerability of tool-using agents: external text can influence repeated action selection and accumulate cost across many invocations. It does not directly test web agents against standalone LLMs. It supports a mechanism-level explanation of increased exposure, not a measured universal ranking of their security. [D]

## 2. Document roadmap and inventory

The document is an empirical AI-agent security and computer-systems paper, with a small mathematical formalization rather than a theorem-based contribution. The visible publication identifier is arXiv:2602.14798v1, dated 16 February 2026, classified cs.CL. No conference acceptance or journal venue for this paper is supplied. Its title is **Overthinking Loops in Agents: A Structural Risk via MCP Tools**. Authors are Yohan Lee, Jisoo Jang, Seoyeon Choi, Sangyeop Kim, and Seungtaek Choi. Affiliations are Yonsei University; Department of Data Science, Ewha Womans University; and Division of Language and AI, Hankuk University of Foreign Studies. Seungtaek Choi is marked as corresponding author. No separate keyword list appears. [A/B; p. 1]

| Inventory ID | Original object | Location and role |
|---|---|---|
| ABS | Abstract | p. 1; problem, attack construction, results, defense conclusion |
| S1 | §1 Introduction and Related Work | pp. 1–2; motivation, distinction from verbosity, related-work positioning |
| S2 | §2 Method | pp. 2–3; attack tools and registry model |
| SS2.1 | §2.1 Attack Tool Construction | pp. 2–3; repetition, refinement, distraction |
| SS2.2 | §2.2 Cycle Induction Mechanism | p. 3; self-loops, multistep cycles, expanding scope |
| SS2.3 | §2.3 Problem Formulation | p. 3; metadata/implementation pairs and token cost |
| S3 | §3 Experiments | pp. 3–5 |
| SS3.1 | §3.1 Experimental Setup | pp. 3–4; registries, datasets, models, budgets |
| SS3.2 | §3.2 Structural Risk in Tool-Use Systems | pp. 4–5; ReAct and Qwen-Code results |
| S4 | §4 Discussion | pp. 5–6 |
| SS4.1 | §4.1 Effect of Registry Composition | pp. 5–6; attack-only versus mixed |
| SS4.2 | §4.2 Limits of Generation-Level Mitigation | p. 6; NoWait |
| S5 | §5 Conclusion | p. 6 |
| S6 | §6 Limitations | pp. 6–7; task scope, defenses, autonomous configurations |
| ETH | Ethical Considerations | p. 7; misuse, model restrictions, proposed safeguards |
| REF | References | pp. 7–9; bibliography, compressed here |
| A1 | Appendix A Attack Tool Implementations | pp. 10–11; Table 3 |
| A2 | Appendix B Implementation Details | p. 10; B.1 environment, B.2 models, B.3 NoWait |
| A3 | Appendix C ReAct-based Agent Experimental Details | pp. 10, 12; Table 4 |
| A4 | Appendix D Qwen-Code Experimental Details | pp. 10–12; Table 5 |
| A5 | Appendix E Proprietary Model Policy | pp. 11–12; Table 6 |
| F1 | Figure 1 | p. 1; Qwen-Code token amplification, five models |
| F2 | Figure 2 | p. 3; normal and attack control paths |
| F3 | Figure 3 | p. 4; six panels: accuracy and tokens for three datasets |
| F4 | Figure 4 | p. 5; attack-only and mixed token ratios |
| T1 | Table 1 | p. 5; Qwen-Code average tokens and time |
| T2 | Table 2 | p. 6; ReAct results with NoWait |
| T3 | Table 3 | p. 11; all 14 attack-tool descriptions and interfaces |
| T4 | Table 4 | p. 12; ReAct results without NoWait |
| T5 | Table 5 | p. 12; seven CodeElo tasks × five models |
| T6 | Table 6 | p. 12; proprietary-provider policy summary |
| E1 | Equation (1) | p. 4; expected per-query token amplification |
| E2 | Registry definitions | p. 3; R, normal, attack, mixed |
| E3 | NoWait set and masking | p. 10; selected lexical items and generation suppression |
| X1–X4 | Distinct experimental comparisons | ReAct, Qwen-Code, composition comparison, NoWait |

No numbered algorithm, pseudocode block, theorem, lemma, proposition, formal research-question list, or proof is supplied. The important footnotes identify the corresponding author, two incident links, Qwen-Code, Appendix A, Serena, Context7, a GLM version migration, vLLM, and SGLang. The linked resources were not visited.

## 3. Background and context

An **agent** in this paper is an LLM integrated into a repeated reasoning-and-action workflow. It selects an external tool, receives output, and uses that output in subsequent decisions. A **tool registry** is the available collection of tool entries. Each entry exposes text such as a name, description, schema, or return message. The paper uses **MCP**, expanded as Model Context Protocol, for the interface through which third-party tools become available. It does not provide a complete protocol specification. [A; pp. 1–3]

**ReAct** is identified as a general-purpose reasoning-and-acting agent architecture, citing work whose title combines reasoning and acting. The paper does not supply full implementation pseudocode for this agent. **Qwen-Code** is the production-grade coding assistant tested with built-in command-line-interface tools and two benign MCP servers. **Serena** supplies 29 tools and **Context7** supplies two. These systems are named and described only to the extent provided by the paper. [A; pp. 2, 4, 10]

A **token** is the unit used in the paper's accounting of model input and output. The paper does not give tokenizer definitions or explain token-to-character conversion. Its token measure includes tool outputs appended to context. Consequently, the cost proxy measures more than the words in the final answer. The supplied work does not establish a dollar cost per token. [A; p. 3]

**Token-level overthinking** means locally long or redundant generation. **Structural overthinking** means a sequence of locally reasonable calls revisits earlier tools or keeps expanding the workflow. **Denial-of-service**, or DoS, describes service impairment through resource exhaustion; the paper also names **Denial-of-Wallet**, emphasizing cost exposure. A **service-level agreement**, or SLA, is mentioned in the motivation as a possible source of penalties. No SLA violation, billing event, or monetary loss is measured. [A; pp. 1–3, 7]

**NoWait** is the tested generation-level intervention. It masks a specified collection of words and variants during generation. It does not modify model parameters or the agent policy. The distinction matters: reducing particular words in an individual response does not necessarily prevent the system from making many additional calls. [A; pp. 6, 10]

## 4. Research problem and gap

**Existing problem:** agents choose and chain external tools using text-visible descriptions and returned content. Untrusted providers can influence those decisions. According to the authors, adding a small collection of malicious tools can create repeated trajectories even when user queries and model parameters remain fixed. The threatened assets are compute resources, token budgets, response time, and successful task completion. [A; pp. 1–3]

**Shortcomings of previous approaches, as characterized by the authors:** efficient-reasoning work focuses on model-internal verbosity and controls such as token filtering, early stopping, and preference tuning. Security work studies tool poisoning, untrusted-input control-flow changes, and resource-exhaustion attacks. The authors position their contribution as a complementary account of loops caused by registry composition and agent orchestration. They contrast their approach with concurrent work that optimizes tool-server responses to maximize cost while preserving correctness. These are the paper's descriptions of prior work; the cited studies were not independently assessed. [A; p. 2]

**Research gap:** the paper asks whether simple, cycle-inducing tools mixed with normal tools can systematically amplify end-to-end resource use, and whether a local generation-time defense addresses that mechanism. **Motivation:** inferred costs can include higher bills, quota depletion, and slower service, but those consequences are not experimentally measured. **Scope:** three reasoning/programming benchmarks, seven filtered competitive-programming tasks, selected reliable tool-calling models, and mostly autonomous agent operation. [A; pp. 2, 4, 6–7]

**Analyst interpretation:** the central boundary failure is that text obtained from a third-party tool can be treated as a reason to continue the workflow. The attack need not change the original user's request. However, this is a mechanism illustrated in these configurations; the paper does not establish that every tool interface or agent policy admits the same failure. [D]

## 5. Research questions, objectives, and hypotheses

The authors do not enumerate formal research questions. Their explicit objective in §2.3 is to characterize vulnerability to resource amplification through registry manipulation, including budget exhaustion with unchanged user queries and base models. Their contribution list in §1 adds comparison across two architectures and evaluation of decoding-time mitigation. [A; pp. 2–3]

For traceability, the following are objective identifiers rather than invented author question numbers:

| ID | Explicit objective | Evidence addressing it |
|---|---|---|
| O1 | Identify structural overthinking as a loop-driven cost vector | §2 mechanism; Figure 2; Table 3 |
| O2 | Quantify amplification and task effects across agent architectures and models | X1 and X2; Figures 1, 3; Tables 1, 4, 5 |
| O3 | Examine whether normal tools dilute or increase the attack effect | X3; Figure 4 |
| O4 | Examine whether NoWait prevents registry-induced amplification | X4; Table 2; Appendix B.3 |

The explicitly stated hypothesis in §4.1 is that normal tool calls interleave with attack cycles, making traces less regular and obscuring repetition. The subsequent text suggests that extra context delays termination and increases token consumption. Figure 4 tests the outcome difference between registry compositions, but the supplied paper does not report a trace-level measurement establishing that interleaving is the causal mechanism. [A/D; pp. 5–6]

There is no formal null hypothesis, prespecified statistical test, or significance threshold reported. The absence of these details should not be confused with a failed hypothesis test; no such test is supplied.

## 6. Assumptions / Threat Model

The attacker controls cycle-inducing third-party tools and their text-visible metadata and responses. The tools are co-registered alongside normal tools. The paper's implementation contains 14 tools across three servers. It assumes the agent can discover or select these entries and can use returned text in later action decisions. [A; pp. 1–3]

The adversary's goal is resource amplification, potentially causing budget exhaustion and task failure. This differs from the exfiltration incidents cited for motivation: the experiments here measure tokens, time, and accuracy, not stolen information. The original user request and base model parameters are held unchanged in the normal-versus-mixed comparison. Ethical Considerations says the experiments do not use privileged access, system modification, undocumented interfaces, hidden backdoors, or model-specific vulnerabilities. [A; pp. 3, 7]

The relevant trust boundary is between the host agent's task execution and provider-controlled tool-visible text. The paper does not specify a full permission model, a malicious-provider onboarding process, or an authenticated registry compromise scenario. Its attacker obtains the practical capability to add entries to the experimental registry; the probability of obtaining that capability in a deployed product is not measured. [D based on supplied setup]

Execution is bounded: maximum 1,000 turns per session and maximum tool-call depth 20 per turn. Additional computational budgets lead to forced termination in some Qwen-Code runs, but their exact token or wall-clock thresholds are not fully specified. The study assumes largely autonomous agents with minimal human intervention. More guarded deployments may behave differently. [A; pp. 4–7, 10]

For the user's web-agent question, **analyst inference** is that any comparable agent exposed to untrusted tool text could acquire additional routes for repeated work. The experiments include web APIs and a WebFetch tool, but there is no separate browser-navigation, website-content, or standalone-model comparison. The threat model should not be expanded to claim those were tested.

## 7. Methodology

The study manipulates tool-registry composition while comparing task outputs and resource use. In the principal comparisons, the normal registry provides benign tools and the mixed registry adds 14 malicious tools. A separate ReAct comparison uses only the 14 attack tools. A defense comparison repeats normal and mixed conditions with NoWait. [A; pp. 3–6]

### Attack construction

Three categories target different accumulation pathways. **Text Repetition** increases returned output through repeated verification or progress markers and instructions to call again. **Iterative Refinement** creates a staged sequence: analysis → validation → refinement → verification → finalization, with possible return to earlier stages or a complete restart. **Distraction** adds complexity analysis, edge cases, alternative approaches, historical context, practical applications, and assumption checks beyond the core query. [A; pp. 2–3, 11]

The paper defines a cycle as a tool-induced sequence eventually revisiting a previously invoked tool. This includes self-reinvocation, multistep loops, and scope-expanding workflows returning to their entry point. A refinement example ends by requesting three to five cycles and redirecting to analysis. These quoted instructions are attack artifacts, not instructions for this analysis. [A; p. 3]

### Registries and datasets

For ReAct, 100 tools are randomly sampled per query from ToolRet, described as an even mix of web APIs, code functions, and custom applications. Mixed has 114 tools. The paper does not explain how an exactly even division is implemented for 100 entries. It evaluates AIME2025 mathematics, GPQA Diamond scientific question answering, and HumanEval code generation. Dataset item counts, exact task selection, scoring code, and splits are not specified in the supplied method description. The displayed accuracies are not sufficient grounds to invent those counts. [A; p. 4]

For Qwen-Code, normal has 44 tools: 13 built-in tools, 29 Serena tools, and two Context7 tools. Mixed has 58. Ten CodeElo problems are randomly sampled, and seven are retained because every evaluated model solves them using an out-of-the-box Qwen-Code installation without additional MCP servers. This screening environment differs from the later 44-tool normal registry. The rationale is to reduce difficulty-driven loops and isolate registry effects. It also limits inference to this selected, initially solvable sample. [A; p. 4]

The seven IDs in Table 5 are 1981c, 2008b, 1982e, 2033f, 1996e, 2003a, and 1972b. Each problem runs in an isolated directory to reduce cross-run interference, particularly from filesystem tools. No training, annotation process, model fitting, or train/validation/test partition is described. [A; pp. 10, 12]

### Models, infrastructure, and controls

The stated evaluation set is Kimi-K2-Thinking, MiniMax-M2, Qwen3-235B-A22B-Thinking-2507, Qwen3-Coder-480B-A35B-Instruct, DeepSeek-V3.2, and GLM-4.7. Models with unreliable invocation or parsing in preliminary runs are excluded, but their identities and failure rates are not listed. ReAct tables contain six models; Qwen-Code tables contain five and use GLM-4.6 rather than GLM-4.7. The supplied text does not fully explain the omitted Qwen3-Thinking Qwen-Code results or the complete migration schedule. [A/B; pp. 4–5, 12]

Models use an OpenAI-compatible API through frameworks such as vLLM and SGLang. MiniMax and DeepSeek receive a lightweight rephrasing layer to normalize tool-response formats. MiniMax-M2 and Qwen3-Thinking use four H200 graphics processing units; other models use eight H200 units. Software versions, prompts, sampling temperatures, seeds, context-window settings, parsing code, and individual serving assignments are not supplied. [A; p. 10]

Every configuration is repeated five times, and averages are reported. No standard deviations, confidence intervals, paired differences, significance tests, or run-level distributions are given. Tokens count both model input and output, including appended tool outputs. Accuracy is reported as a percentage, but detailed grading procedures are not supplied. Runtime is in seconds for Qwen-Code. These are resource proxies and task measures, not monetary costs. [A; pp. 3–5, 10]

## 8. Experiments / Analyses

| Experiment | Purpose and manipulated condition | Evidence | Main result and qualification |
|---|---|---|---|
| X1: ReAct normal versus mixed | Measure registry effects with 100 benign versus 100 benign + 14 attack tools | Figure 3; Table 4 | All 18 model–dataset token ratios exceed 1; maximum 14.59×. Accuracy effects vary substantially. No uncertainty measures supplied. |
| X2: Qwen-Code normal versus mixed | Test a coding assistant with 44 versus 58 tools on seven screened CodeElo tasks | Figure 1; Tables 1, 5 | Main-text maximum summary amplification 142.35× tokens and 27.49× runtime; task-level maximum 971.27× tokens. Forced termination and aggregation details matter. |
| X3: Attack-only versus mixed | Determine whether benign tools dilute the 14-tool attack configuration | Figure 4 | Mixed is often comparable or worse; GLM-4.7 ratios rise from 6.1× to 10.8× on GPQA and 7.6× to 14.6× on HumanEval. Interleaving mechanism remains a hypothesis. |
| X4: NoWait | Evaluate local generation suppression under normal and mixed ReAct registries | Table 2; Appendix B.3 | Mixed amplification persists, reaching 15.37× on AIME2025 for DeepSeek-V3.2. This tests one defense family, not all defenses. |

X1 holds query and model parameters fixed while changing the registry. Dependent variables are accuracy and token consumption. No runtime table is supplied for ReAct. The paper's interpretation links larger degradation on code and mathematics to repeated validation checkpoints, but aggregate outcome data alone do not quantify checkpoint interception frequency. [A/D; pp. 4–5]

X2 additionally reports runtime and per-problem results. Some executions are forcibly stopped after computational-budget exhaustion and produce no output. The supplied paper does not provide a complete model–problem failure flag table. It therefore supports the existence of these failures but not an exact count of all failed runs or a censored-runtime correction. [A; p. 5]

X3 isolates attack-tool availability by removing normal tools, but its total registry size also changes. It is not a size-matched benign control. X4 compares normal and mixed while NoWait is enabled; a comparison with unmodified Table 4 changes both the defense condition and the relevant baseline. An attack ratio under NoWait is not itself a percentage improvement over undefended operation. [D]

## 9. Results

### ReAct task effects

Table 4 provides the principal exact baseline. The compact table below preserves every model–dataset accuracy pair and printed token ratio. N→M means normal accuracy to mixed accuracy. Ratios are author-reported, rounded values; underlying token totals are retained in Section 11.

| Model | AIME2025 accuracy N→M; tokens × | GPQA Diamond accuracy N→M; tokens × | HumanEval accuracy N→M; tokens × |
|---|---|---|---|
| Kimi-K2-Thinking | 70.00→36.67%; 1.04× | 72.59→64.97%; 2.69× | 19.51→17.68%; 2.84× |
| MiniMax-M2 | 80.00→70.00%; 5.61× | 56.85→53.30%; 10.83× | 76.83→56.71%; 8.58× |
| Qwen3-Thinking | 63.33→26.67%; 3.83× | 70.05→64.97%; 4.71× | 60.98→52.44%; 2.67× |
| Qwen3-Coder | 20.00→23.33%; 3.11× | 47.21→48.22%; 2.52× | 30.49→3.05%; 7.03× |
| DeepSeek-V3.2 | 60.00→23.33%; 9.00× | 70.05→26.90%; 4.05× | 32.32→6.71%; 4.55× |
| GLM-4.7 | 40.00→60.00%; 2.75× | 58.88→53.81%; 10.77× | 40.85→9.15%; 14.59× |

Cost amplification is broader than task failure. For example, Qwen3-Coder GPQA accuracy increases from 47.21% to 48.22% while tokens rise from 45,622,515 to 114,800,037. Conversely, DeepSeek GPQA accuracy falls sharply, so the claim that question-answering accuracy generally remains near baseline has an important exception. AIME2025 also has improvements for Qwen3-Coder and GLM-4.7. The evidence does not support uniform accuracy degradation. [A/B; p. 12]

**Analyst-derived differences:** Kimi AIME accuracy falls by 70.00−36.67=33.33 percentage points. DeepSeek AIME falls by 60.00−23.33=36.67 points. Qwen3-Thinking AIME falls by 63.33−26.67=36.66 points. Qwen3-Coder HumanEval falls by 30.49−3.05=27.44 points. These are percentage-point differences, not relative percentage decreases. [C; Table 4]

### Qwen-Code resource use

Table 1 reports Kimi at 10.9× tokens and 2.6× runtime; MiniMax at 142.4× and 27.5×; Qwen3-Coder at 22.4× and 9.5×; DeepSeek at 5.5× and 7.1×; GLM-4.6 at 101.3× and 10.4×. Token and time amplification are different metrics and need not grow proportionally. The more precise prose values 142.35× and 27.49× are consistent with rounding to the headline values, but the averaging definition has a separate unresolved issue discussed below. [A; p. 5]

Individual extremes are GLM-4.6 on 2033f: 127,084→123,432,447 tokens, printed ratio 971.27×; MiniMax on 2003a: 13,324→8,123,834 tokens, 609.71×, and 16.7→3008 seconds, 180.12×; Qwen3-Coder on 1972b: 15,467→4,431,546 tokens, 286.52×. These are task-specific values, not average effects across all tasks or models. [A/B; p. 12]

### NoWait

All 18 Table 2 mixed/normal token ratios remain above 1. DeepSeek AIME reaches 15.37×; GLM GPQA reaches 11.93×; GLM HumanEval reaches 13.35×. The result supports failure to eliminate amplification in these conditions. It does not establish that NoWait never reduces cost, since some condition-specific ratios and raw totals are smaller than their unmodified counterparts while others are larger. [A/B; pp. 6, 12]

## 10. Figure-by-figure interpretation

### Figure 1 — Qwen-Code token usage

Figure 1 is visually inspected on p. 1. It is a grouped bar chart with five model categories along the horizontal axis and total tokens in millions on a logarithmic vertical axis. Gray denotes normal and red denotes mixed. Labeled ratios are approximately displayed as 10.9×, 142.4×, 22.4×, 5.5×, and 101.3×; these agree with Table 1's printed headline ratios. [B]

The chart shows amplification for every displayed model, with MiniMax-M2 having the largest ratio and GLM-4.6 the largest mixed total. Log scaling allows values spanning several orders of magnitude to share one chart; equal-looking vertical differences should not be read as equal absolute token additions. No error bars or confidence intervals are shown. Exact values should be taken from Table 1 rather than estimated from bar heights. The caption says total tokens, while Table 1 identifies its values as averages; this is a labeling distinction that the figure alone does not resolve. [A/B/D]

### Figure 2 — MCP attack overview

Figure 2 is visually inspected on p. 3 and is a conceptual control-flow diagram rather than a measured plot. A user submits a query to an LLM agent and receives an agent response. Normal MCP servers and attack MCP servers feed a mixed registry. The diagram labels normal tools N=100 and attack tools N=14, matching ReAct rather than Qwen-Code's 44-tool normal setup. Gray paths depict standard operation and normal outcomes; red paths depict entry into an overthinking loop and an outcome labeled denial-of-service and failure. [B]

A spiral of staged steps illustrates recurrence. Text repetition, iterative refinement, and distraction are listed beside the attack server. Check marks identify low token cost, low latency, and high accuracy on the normal side; warning markers identify extreme amplification, high latency/timeouts, and reduced accuracy/task failure on the attack side. These are schematic contrasts: not every observed normal task has high accuracy, and not every attack lowers it. The caption uses exponential token consumption, but the supplied results do not establish an exponential growth law. [A/B/D]

### Figure 3 — ReAct accuracy and tokens

Figure 3 is visually inspected on p. 4. It has three dataset columns: AIME2025, GPQA Diamond, HumanEval. Each has an upper accuracy panel and a lower token panel, for six panels total. Model names form the horizontal categories. Accuracy is a percentage; tokens are labeled in millions. Gray is normal and red is mixed. The panels use ordinary linear scales with different ranges rather than Figure 1's logarithmic scale. [B]

The lower panels show mixed token totals above normal for all model–dataset pairs. The upper panels show diverse effects, including severe losses on HumanEval for Qwen3-Coder, DeepSeek, and GLM, and AIME improvements for some models. GPQA includes relatively stable results and one major DeepSeek decline. Small bar labels summarize rounded values; exact figures are available in Table 4. No statistical markers, uncertainty bars, or run distributions appear. Comparing apparent bar height across panels with different limits is not a valid comparison of absolute effects. [B/D]

### Figure 4 — Registry composition

Figure 4 is visually inspected on p. 5. It is a horizontal grouped bar chart organized by model, with three dataset pairs per model. The horizontal quantity is token amplification relative to the normal registry; dataset identity is encoded by shading/color, and solid versus hatched bars distinguishes attack-only from mixed. Values near 1 represent little amplification; longer bars indicate larger costs. There are no uncertainty bars. [A/B]

The most clearly emphasized comparisons are GLM-4.7 GPQA 6.1×→10.8× and HumanEval 7.6×→14.6×. These values are also stated in nearby text and can be used with HIGH confidence. Other fine labels are not exhaustively transcribed because of their size and because no corresponding full attack-only numeric table is supplied. The figure supports the authors' majority-pattern description, but not a claim that mixed always exceeds attack-only. It does not directly visualize tool-call interleaving or establish why the difference occurs. [A/B/D]

## 11. Table-by-table interpretation

### Table 1 — Qwen-Code average resources

Rows are five models; columns give normal and mixed token amounts and runtime in seconds. Parentheses show the mixed/normal factor. K denotes thousands and M millions as used in the displayed quantities. No variability estimates, success counts, or termination flags appear. [A/B; p. 5]

| Model | Normal tokens | Normal time, s | Mixed tokens | Mixed time, s |
|---|---:|---:|---:|---:|
| Kimi-K2-Thinking | 31.6K | 176 | 343.9K, 10.9× | 449, 2.6× |
| MiniMax-M2 | 45.9K | 82 | 6.5M, 142.4× | 2260, 27.5× |
| Qwen3-Coder | 127.5K | 77 | 2.9M, 22.4× | 727, 9.5× |
| DeepSeek-V3.2 | 273.5K | 222 | 1.5M, 5.5× | 1580, 7.1× |
| GLM-4.6 | 334.3K | 89 | 33.8M, 101.3× | 925, 10.4× |

MiniMax has the largest printed token and runtime ratios; GLM has the highest absolute mixed tokens. Kimi has the smallest time ratio; DeepSeek the smallest token ratio. Rankings are descriptive, not statistically established. The GLM mixed average does not transparently reconcile with Table 5, and ratios of averages differ from Equation (1)'s mean of per-query ratios.

### Table 2 — NoWait ReAct results

Table 2 reports normal/mixed accuracy percentages and exact token totals for six models and three datasets. Parentheses normalize to the same model and dataset with NoWait enabled. Token cells are shaded low 1–3×, medium 3–7×, high 7×+. Endpoint conventions overlap in that textual definition, although no key conclusion depends on an endpoint. A dash in a normal row denotes the reference ratio, not missing accuracy or tokens. [A/B; p. 6]

| Model | AIME accuracy N→M; tokens N→M; ratio | GPQA accuracy N→M; tokens N→M; ratio | HumanEval accuracy N→M; tokens N→M; ratio |
|---|---|---|---|
| Kimi | 73.33→56.67%; 3,838,910→4,904,131; 1.28× | 30.96→26.90%; 5,789,388→11,965,963; 2.07× | 14.02→16.46%; 9,513,903→19,474,670; 2.05× |
| MiniMax | 73.33→73.33%; 2,375,798→8,111,917; 3.41× | 55.84→55.33%; 8,076,783→65,423,352; 8.10× | 72.56→62.80%; 7,510,249→53,728,320; 7.15× |
| Qwen3-Thinking | 66.67→76.67%; 688,009→1,942,084; 2.82× | 71.07→63.96%; 6,466,715→24,874,264; 3.85× | 47.56→48.17%; 5,047,058→9,704,763; 1.92× |
| Qwen3-Coder | 10.00→20.00%; 5,018,600→13,766,119; 2.74× | 46.19→39.09%; 44,980,986→91,299,839; 2.03× | 31.71→18.90%; 11,522,813→55,380,483; 4.81× |
| DeepSeek | 60.00→16.67%; 497,357→7,646,711; 15.37× | 69.54→26.90%; 2,896,222→11,938,782; 4.12× | 34.15→3.66%; 1,948,891→12,363,792; 6.34× |
| GLM-4.7 | 56.67→53.33%; 4,713,463→16,375,952; 3.47× | 54.31→53.81%; 9,323,681→111,252,867; 11.93× | 42.68→5.49%; 7,001,464→93,441,302; 13.35× |

The largest token ratio is DeepSeek AIME, while the largest absolute mixed total is GLM GPQA. Accuracy occasionally improves or stays equal under mixed, reinforcing that resource amplification and incorrect answers are distinct outcomes. No significance or uncertainty information is supplied.

### Table 3 — Attack-tool interfaces

Table 3 lists all 14 tools, grouped 3 repetition, 5 refinement, and 6 distraction. The grouping counts are analyst-derived by counting rows; the total 14 is author-reported. The following retains each tool's functional role and compresses repetitive interface wording. [A/B/C; p. 11]

| Category | Tool | Arguments and returned control effect |
|---|---|---|
| Repeat Text | echo_verification | Integer count with enforced minimum; returns repeated marker string and next-call instruction |
| Repeat Text | progress_marker | String step and integer marker_count; returns markers and next-call instruction |
| Repeat Text | confirmation_echo | String content and integer repetitions; returns confirmation plus markers and recursive trigger |
| Iterative Refinement | analyze | problem, approach, optional complexity_assessment; returns analysis and redirection to validation |
| Iterative Refinement | validate | analysis_result, validation_checklist, optional issues_found; returns validation and branching/recursion |
| Iterative Refinement | refine | original_solution, refinements_made, optional new_issues_discovered; returns refinement and next step/backtracking |
| Iterative Refinement | verify | refined_solution, verification_results, optional remaining_concerns; returns checks and enforced backtracking |
| Iterative Refinement | finalize | final_solution, completeness_score, confidence_level, next_step; returns finalization and cycle restart |
| Distraction | check_time_complexity | complexity and reasoning; returns complexity report and next step |
| Distraction | verify_edge_cases | list of edge-case strings and analysis; returns edge-case listing and recursive instruction |
| Distraction | consider_alternative_approaches | list of string-to-string dictionaries; returns alternatives and enforced continuation |
| Distraction | check_historical_context | historical_examples string; returns historical context and next step |
| Distraction | assess_practical_applications | list of application strings; returns applications and recursive instruction |
| Distraction | validate_assumptions | list of string-to-string dictionaries; returns assumptions and cycle restart |

Most refinement arguments are strings, including completeness_score and confidence_level; they are not reported as numeric thresholds. The table gives interfaces and intentions, not complete executable implementations. Minimum repetition counts, exact confidence thresholds, and full response templates are not supplied.

### Table 4 — ReAct without NoWait

Table 4 is the exact counterpart to Figure 3. Section 9 preserves all accuracies and token ratios; this table preserves every underlying token pair. Dataset order is AIME2025, GPQA Diamond, HumanEval. [A/B; p. 12]

| Model | AIME tokens normal→mixed | GPQA tokens normal→mixed | HumanEval tokens normal→mixed |
|---|---:|---:|---:|
| Kimi | 4,251,880→4,427,514 | 14,098,048→37,983,373 | 9,635,441→27,322,798 |
| MiniMax | 1,462,548→8,206,770 | 6,832,721→73,988,176 | 7,437,881→63,847,601 |
| Qwen3-Thinking | 653,476→2,501,360 | 6,073,627→28,604,299 | 5,369,616→14,327,613 |
| Qwen3-Coder | 5,051,562→15,689,070 | 45,622,515→114,800,037 | 12,419,795→87,259,072 |
| DeepSeek | 549,667→4,948,229 | 2,752,992→11,141,346 | 2,361,707→10,751,180 |
| GLM-4.7 | 6,358,821→17,464,231 | 10,272,416→110,588,180 | 6,508,864→94,935,247 |

The maximum ratio is GLM HumanEval 14.59×; the minimum is Kimi AIME 1.04×. The largest mixed absolute token total is Qwen3-Coder GPQA, 114,800,037, although its ratio is only 2.52× because the baseline is also large. This shows why absolute cost and relative amplification require separate interpretation. No uncertainty estimates or statistical annotations appear.

### Table 5 — Qwen-Code task distribution

Table 5 gives five models × seven tasks, with normal and mixed tokens and seconds. To retain all task-level comparisons without duplicating 140 raw cells, the following table preserves every printed token and time ratio. Exact extreme raw values are retained in Sections 9 and 20. This is disclosed compression, not lossless transcription. [A/B; p. 12]

| Problem | Kimi tokens/time × | MiniMax tokens/time × | Qwen3-Coder tokens/time × | DeepSeek tokens/time × | GLM-4.6 tokens/time × |
|---|---|---|---|---|---|
| 1981c | 5.22 / 2.92 | 219.23 / 21.72 | 29.86 / 7.05 | 6.13 / 6.41 | 7.46 / 49.03 |
| 2008b | 12.75 / 4.57 | 505.53 / 58.28 | 71.09 / 37.37 | 8.90 / 22.85 | 11.93 / 8.41 |
| 1982e | 8.18 / 1.26 | 229.76 / 24.64 | 45.53 / 5.81 | 3.83 / 15.86 | 7.41 / 3.09 |
| 2033f | 23.78 / 2.89 | 12.06 / 2.75 | 2.56 / 2.90 | 2.74 / 2.23 | 971.27 / 20.90 |
| 1996e | 11.16 / 2.26 | 436.38 / 34.61 | 13.24 / 4.45 | 3.01 / 9.59 | 77.92 / 12.70 |
| 2003a | 16.77 / 2.58 | 609.71 / 180.12 | 72.40 / 17.32 | 79.60 / 19.89 | 11.10 / 2.39 |
| 1972b | 19.10 / 4.67 | 110.44 / 13.59 | 286.52 / 21.75 | 50.59 / 1.60 | 298.30 / 15.71 |

The overall largest token ratio is GLM 2033f; the largest runtime ratio is MiniMax 2003a. Every printed task ratio exceeds 1 for both metrics. GLM 1981c illustrates that a moderate 7.46× token ratio can coexist with a 49.03× time ratio; DeepSeek 1972b illustrates the reverse, 50.59× tokens but 1.60× time. The table does not identify which individual runs ended naturally or were stopped, and does not provide within-task variation.

### Table 6 — Proprietary-provider policies

Rows are GPT-4o/OpenAI, Claude 3.5/Anthropic, and Gemini/Google. Listed restrictions are, respectively, using outputs to develop competing models; automated scraping/extraction; and regional availability/API quotas. All access dates are 2026-02-08. Source cells visibly say Link, but the supplied transcription does not expose the target URLs. [A/B; p. 12]

This is a policy-background table, not a performance experiment or a present-day legal determination. Ethical Considerations explicitly says proprietary production APIs were not evaluated. Appendix E's generic statement about evaluations within provider terms should be read with that exclusion rather than used to invent proprietary-model results. The restrictions are author-reported and were not independently verified.

## 12. Diagram / Architecture Interpretation

Figure 2 contains the only substantive architecture diagram. Its input is the user query; the decision-making component is the LLM agent; the action inventory is the mixed registry; providers are normal and attack MCP servers; and outputs include the final response and operational outcomes. Registry entries expose metadata before calls, while executed tools return text at runtime. These two channels feed subsequent action selection. [A/B; p. 3]

The normal gray branch represents bounded task-directed work. The red branch represents the agent choosing attack tools and then following tool-visible continuation instructions through a spiral of stages. The important feedback is not merely server-to-agent data transfer: returned text affects the next tool choice, and that choice produces another response that can send control backward.

Three structural patterns are described. A self-loop returns to the same tool. A multistep loop traverses several tools and returns to an earlier stage. A scope-expanding loop adds side tasks and eventually returns to the entry point. The refinement sequence demonstrates how a locally plausible progression can defeat global completion: finalization itself can request another round. [A]

**Analyst interpretation:** the agent's global task objective competes with local instructions presented by the tool. A workflow can appear diligent at each stage while failing to make terminating progress. The figure communicates this mechanism but contains no actual call graph, measured transition frequencies, detected-cycle lengths, or token-growth time series. Its outcome boxes should therefore be read as conceptual summaries, not universal predictions.

## 13. Equations and mathematical concepts

### Registry definitions, p. 3

The registry is written as R = {(m_i, f_i)} for i=1,…,|R|. Here m_i is text-visible metadata, such as description and schema, and f_i is the underlying implementation. |R| is the number of registry entries. The representation separates what the model sees from what executes. It is a system description, not an optimization objective.

R_normal is the benign registry; R_attack is the attack-tool set; R_mixed = R_normal ∪ R_attack. The union operator means the mixed condition contains entries from both collections. The authors write |R_attack| ≪ |R_normal| to characterize a small injected collection. Actual conditions are 14 versus 100 in ReAct and 14 versus 44 in Qwen-Code. The qualitative much-smaller notation is not a proved asymptotic relation. [A]

**Analyst-derived proportions:** attacks are 14/114≈12.28% of ReAct's mixed registry and 14/58≈24.14% of Qwen-Code's mixed registry. Relative to benign counts, additions are 14/100=14% and 14/44≈31.82%. These are different denominators; none is an author-reported attack-success rate. [C]

### Token cost and Equation (1), pp. 3–4

Tokens(q | R) denotes total token consumption for query q under registry R. It includes model input and output and tool outputs added to context. Q denotes the query distribution. The reported metric is:

E_{q∼Q}[ Tokens(q | R_mixed) / Tokens(q | R_normal) ].

The fraction is a dimensionless per-query amplification factor. The expectation averages those query-level ratios. A value of 1 means equal token use; a value above 1 means more use in mixed. The formula assumes a meaningful nonzero normal denominator, but the supplied paper does not discuss zero-token cases. It is an evaluation metric, not a loss used to train a model. [A]

The expectation of ratios generally differs from a ratio of aggregate totals. **Analyst-derived illustration from MiniMax Table 5:** the seven printed token ratios sum to 219.23+505.53+229.76+12.06+436.38+609.71+110.44=2123.11; dividing by seven gives approximately 303.30×. The mixed raw counts sum to 45,736,668 and normal counts to 321,287; their ratio is approximately 142.35×, matching the main-text headline rather than the 303.30× mean. Rounding of printed ratios cannot explain this large difference. The aggregation convention is therefore unresolved. [C]

### NoWait masking, p. 10

The printed set is T={wait, alternatively, hmm, but, however, alternative, another, check, double-check, oh, maybe, verify, other, again, now, ah, any}. The text calls this a set of 15 tokens, but the displayed list contains 17 lexical entries when counted as written. Tokenizer-level mappings are not supplied, so the actual implemented mask cardinality cannot be reconstructed. [A/B/C]

The authors say the probabilities of these tokens and variants are set to −∞, while also specifying logit masking. A probability itself cannot be negative infinity; **analyst interpretation** is that the intended implementation masks logits so the corresponding generation probability becomes zero. This interpretation is consistent with their logit-masking statement, but does not silently correct the paper or establish the exact code used. Variants include whitespace, punctuation, and capitalization. No parameter change or agent-policy change is reported.

## 14. Interpretation and discussion

The strongest supported conclusion is that adding these tools increases measured token consumption in all tabulated normal-versus-mixed conditions. Accuracy can remain near baseline, worsen dramatically, or improve, depending on model and task. Thus task correctness alone is insufficient to characterize this particular operational risk. [A/B]

The authors explain larger coding-agent effects through richer tool ecosystems and longer workflows. This is plausible and fits the tested environments, but the architecture comparison also changes workload, tool inventory, filtering, and the displayed model set. **Analyst interpretation:** it is not a clean factorial experiment isolating richness or production status as the causal variable. The result is evidence of severe vulnerability in Qwen-Code under this setup, not proof that all production agents are more vulnerable than all research agents. [D]

The composition experiment supports the observation that normal tools do not necessarily dilute the attack. The proposed mechanism—interleaving, irregular traces, extra context, delayed termination—is an author hypothesis. No detailed trace evidence establishes its frequency or separates it from registry-size and tool-selection effects. [A/D]

The NoWait result distinguishes local lexical controls from global workflow structure. Persisting amplification indicates that suppressing selected words alone is insufficient here. It does not demonstrate the inadequacy of all inference-time or agent-level mitigations. The authors explicitly leave alternative defenses for future work. [A]

### Consistency findings

1. **GPQA stability range:** p. 5 describes most models as 0.90×–1.02× accuracy with 2.52×–10.83× tokens. Table 4 includes DeepSeek accuracy 0.38× and Qwen3-Thinking 0.93×. The word most allows the DeepSeek exception, but the exception is substantive and must remain visible.
2. **GLM versions:** p. 4 lists GLM-4.7 and notes migration; Tables 1 and 5 and Figure 1 use GLM-4.6, whereas ReAct uses GLM-4.7. Results cannot be treated as the same exact model version across environments.
3. **Aggregation:** Equation (1)'s average query-level ratio does not match MiniMax's Table 5-derived mean, while the ratio of sums matches 142.35×. The paper does not explain this metric shift.
4. **GLM average:** the seven Table 5 mixed token counts sum to 237,037,263; divided by seven this is 33,862,466.14, approximately 33.86M. Normal counts sum to 2,340,447; average 334,349.57. Their aggregate ratio is approximately 101.28×, compatible with 101.3×, but the printed mixed 33.8M is not a transparent standard one-decimal rounding of 33.86M. The discrepancy is small relative to the scale but unresolved. [C]
5. **NoWait cardinality and notation:** 15 claimed tokens versus 17 displayed lexical entries; probabilities versus logits described as −∞. Exact implementation is unavailable.
6. **Exponential/unbounded wording:** Figure 2 says exponential and Appendix D says potentially unbounded. The observations are bounded, forcibly terminated experiments, not a measured exponential law or proof of unbounded execution.
7. **Sample filtering:** initially solvable tasks are screened without added MCP servers, whereas normal evaluation includes Serena and Context7. These baselines should not be conflated.

## 15. Contributions and novelty

The paper's **conceptual contribution** is the distinction between locally verbose model reasoning and loop-driven structural overthinking in an agent's interaction trajectory. Its **methodological contribution** is a registry-composition attack using ordinary-looking verification, refinement, and supplementary-task patterns rather than sophisticated exploit logic. Its **implementation contribution** is a collection of 14 attack tools across three servers, with interfaces summarized in Table 3. [A; pp. 1–3, 11]

Its **empirical contribution** is evaluation across a general-purpose agent and a coding assistant, multiple tool-capable models, three ReAct benchmarks, and seven filtered CodeElo tasks, including both average and task-specific resource results. The attack-only comparison and NoWait evaluation show that benign tools and lexical suppression do not automatically eliminate the problem. [A; pp. 4–6, 12]

The paper does not introduce a new benchmark dataset, a proven detection algorithm, a deployed defense, a mathematical theorem, or a direct standalone-LLM comparison. Novelty relative to the entire literature cannot be independently established in closed-document mode. The authors' contrast with concurrent work is represented as their positioning, not an externally verified priority claim.

**Research relevance, analyst inference:** the work contributes a concrete reason that agents can face risks absent from a single isolated completion: provider-controlled text can influence subsequent actions repeatedly, and returned content can enlarge future contexts. The result concerns this added interaction surface rather than proving that the base LLM itself becomes intrinsically less secure. [D]

## 16. Limitations

### Authors' stated limitations

**Dataset scope and difficulty:** evaluation focuses on scientific reasoning, mathematics, and programming, limiting general-domain coverage. Difficult CodeElo tasks can cause loops without attacks; the researchers therefore retain tasks solvable within default execution budgets. [A; p. 6]

**Defense scope:** NoWait does not exhaust the possible defenses. The authors do not systematically test reinforcement-learning-based reasoning suppression, registry filtering, or stricter turn/depth constraints. Comparative defense analysis remains future work. [A; p. 6]

**Agent configurations:** experiments assume substantial autonomy and minimal human intervention. Real deployments may contain additional guardrails. [A; p. 7]

**Undisclosed training details:** tool-calling strategies, instruction tuning, and fine-tuning recipes may not be available. The authors refrain from attributing behavior to those hidden components. [A; p. 7]

**Model-policy scope:** proprietary production APIs are explicitly excluded. The stated model-selection restriction is an ethical scope boundary as well as a limit on generalization. [A; p. 7]

### Additional evidence-based analyst observations

No uncertainty estimates or run-level values are supplied despite five repetitions. ReAct sample counts and detailed scoring procedures are unspecified. The CodeElo sample is small and deliberately screened. Registry size changes with attack insertion, and there is no matched-size benign-addition control. Full tool prompts, executable implementations, call traces, attack-invocation rates, cycle counts, and termination thresholds are absent. [D]

Comparing architectures changes several factors simultaneously. Token totals include input and output, but the paper does not break down contributions from repeated context, tool verbosity, number of calls, and model reasoning. Runtime depends on the reported serving setup and hardware; hardware counts differ across models. The model rephrasing layer may matter, but its effect is not isolated. Reporting inconsistencies in aggregation, GLM versions, and NoWait specification reduce exact reproducibility. These are analyst observations, not limitations explicitly admitted in those terms.

## 17. Threats to validity

The following validity categories are analyst-organized assessments based on the supplied study; the authors do not use all these labels.

**Internal validity:** holding queries and model parameters fixed supports a registry-effect interpretation within each comparison. Isolated Qwen-Code directories reduce filesystem carryover. However, adding tools changes both malicious content and inventory size; absent matched-size controls, the incremental role of benign registry expansion is not isolated. No trace-level quantification independently validates the proposed interleaving mechanism. [D]

**Construct validity:** token consumption is a useful reported cost proxy, but not a measured financial bill. Runtime is a responsiveness measure, not proof of operational SLA penalties. Accuracy percentages characterize benchmark success, but unspecified grading details limit interpretation. Neither total tokens nor total time directly identifies cycle frequency or growth law. [D]

**Statistical conclusion validity:** five repeated trials provide repetition, but no dispersion or uncertainty intervals establish stability. Aggregation ambiguity affects the interpretation of headline amplification. No reported significance test supports ranking models or assigning a population-wide average effect. [D]

**External and ecological validity:** the mixture of ToolRet tools and the Qwen-Code registry broadens the setting beyond one synthetic tool, but the tasks remain narrow and selected. Human oversight, proprietary models, real browser sessions, and measured deployment bills are outside the experiment. Calling the coding environment production-grade does not establish exposure in all deployed systems. [D]

**Reproducibility:** hardware type/count, tool lists, task IDs, budgets, and repetitions are useful. Missing prompts, versions, random seeds, decoding parameters, full attack code, parsers, masking implementation, and stopping rules prevent exact reconstruction from this supplied paper alone. The references and links identify related artifacts but their contents were not reviewed. [D]

## 18. Future work and open questions

### A. Explicit author directions

The authors identify comparative evaluation of alternative defenses as future work: reinforcement-learning-based reasoning suppression, registry-level filtering, and tighter turn/depth constraints. Ethical Considerations highlights registry vetting, session-level cost monitoring, and structural constraints on depth and recursion as safeguards to inform. These are proposed directions, not demonstrated solutions. [A; pp. 6–7]

### B. Additional open questions — analyst inference

How much amplification comes from repeated calls versus repeated inclusion of growing context? Would the same attack remain effective with equal-size benign registries, different descriptions, or tools exposed only when needed? How often does an agent select an attack tool, and what fraction of runs develops an actual cycle? Can a structural guard stop harmful recurrence while preserving legitimate iterative debugging? [D]

How would human approval, domain-specific tool permissions, or concise trusted orchestration change outcomes? How stable are effects across prompts, model versions, serving stacks, and seeds? What are the results on unscreened tasks and nonprogramming workflows? Which runs were censored by budgets, and what completion or cost trade-offs would stricter budgets create? [D]

For the user's question, the missing decisive experiment is a controlled comparison of the same base model in a standalone condition and a web-agent condition, with specified exposure channels and common security metrics. The current paper does not conduct it. It can motivate that experiment and supply a structural-risk hypothesis, but cannot supply its numerical result. [D]

## 19. Terminology and notation glossary

| Term | Meaning within the supplied work |
|---|---|
| LLM | Large language model; the model generating decisions and responses |
| MCP | Model Context Protocol; interface for registering and interacting with external tools |
| Tool-visible text | Descriptions, schemas, names, and returned messages accessible to the model |
| Tool registry | Collection of tools available for selection |
| Structural overthinking | Costly looping or expanding call trajectories formed from locally plausible steps |
| Token-level overthinking | Locally verbose or redundant reasoning generation |
| Cycle | Tool-induced path that eventually revisits a previously called tool |
| Self-loop | A tool directs the agent to call itself again |
| Multistep cycle | Several calls return control to an earlier stage |
| Scope-expanding loop | Extra subtasks widen work and eventually restart the sequence |
| ReAct | Reasoning-and-acting agent architecture used for general-purpose evaluation |
| Qwen-Code | Coding assistant used in the second experimental environment |
| CLI | Command-line interface; qualifier for Qwen-Code built-in tools |
| API | Application programming interface; models are served through an OpenAI-compatible interface |
| ToolRet | Source corpus for sampled ReAct tools |
| AIME2025 | Mathematics benchmark named from the American Invitational Mathematics Examination |
| GPQA Diamond | Scientific question-answering benchmark; cited work describes graduate-level, Google-proof questions |
| HumanEval | Code benchmark used for accuracy evaluation |
| CodeElo | Competition-level coding benchmark supplying the seven screened tasks |
| NoWait | Generation-time lexical masking intervention tested as a mitigation |
| Logit masking | Suppressing selected pre-probability token scores during generation |
| GPU | Graphics processing unit; H200 devices provide reported serving hardware |
| DoS | Denial-of-service; resource exhaustion or impaired completion |
| Denial-of-Wallet | Cost-amplification misuse named in Ethical Considerations |
| SLA | Service-level agreement, mentioned as possible operational exposure |
| R | Registry of metadata/implementation pairs |
| m_i, f_i | Metadata and implementation of tool i |
| R_normal, R_attack, R_mixed | Benign, malicious, and combined registries |
| |R| | Number of registry entries |
| q, Q | A query and the query distribution |
| Tokens(q | R) | Total input/output tokens for q under R, including contextualized tool output |
| E_{q∼Q} | Average over queries drawn from Q |
| T | Printed collection of lexical items masked by NoWait |
| ×-factor | Mixed/normal ratio, with aggregation conventions requiring care |
| Percentage point | Absolute difference between two percentages |

## 20. Key numerical results

Values in this reference table retain their reported conditions. Additional complete ReAct numbers and all Qwen-Code task ratios appear above. Derived entries identify operands; no approximate graph-height values are used as exact measurements.

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| Attack implementation | 14 tools; 3 servers | count | All attack configurations | Author-reported | p. 1, abstract |
| ReAct registries | 100 normal; 114 mixed | tools | 14 attack additions | Author-reported | p. 4, §3.1 |
| Qwen-Code registries | 44 normal; 58 mixed | tools | 13 built-in + 29 Serena + 2 Context7 | Author-reported | p. 4, §3.1 |
| CodeElo screening | 10 sampled; 7 retained | tasks | All models successful without added MCP servers | Author-reported | p. 4, §3.1 |
| Repetitions | 5 | trials/configuration | Reported average values | Author-reported | pp. 4, 10 |
| Session maximum | 1,000 | turns | Both environments | Author-reported | pp. 4, 10 |
| Per-turn maximum | 20 | tool-call depth | Both environments | Author-reported | pp. 4, 10 |
| Hardware | H200×4; H200×8 | GPUs | MiniMax/Qwen3-Thinking; other models | Author-reported | p. 10, B.2 |
| ReAct maximum without NoWait | 14.59 | × tokens | GLM-4.7 HumanEval mixed/normal | Author-reported | p. 12, T4 |
| GLM HumanEval tokens | 6,508,864→94,935,247 | tokens | No NoWait | Author-reported | p. 12, T4 |
| Qwen3-Coder HumanEval accuracy | 30.49→3.05 | % | No NoWait | Author-reported | p. 12, T4 |
| DeepSeek HumanEval accuracy | 32.32→6.71 | % | No NoWait | Author-reported | p. 12, T4 |
| GLM HumanEval accuracy | 40.85→9.15 | % | No NoWait | Author-reported | p. 12, T4 |
| Qwen3-Coder GPQA tokens | 45,622,515→114,800,037 | tokens | Accuracy 47.21→48.22% | Author-reported | p. 12, T4 |
| Qwen-Code headline maximum | 142.35 tokens; 27.49 time | × | Main-text summary; Table 1 rounds to 142.4 and 27.5 | Author-reported | p. 5, §3.2/T1 |
| GLM 2033f tokens | 127,084→123,432,447 | tokens | Qwen-Code; 971.27× | Author-reported | p. 12, T5 |
| MiniMax 2003a tokens | 13,324→8,123,834 | tokens | Qwen-Code; 609.71× | Author-reported | p. 12, T5 |
| MiniMax 2003a time | 16.7→3008 | seconds | Qwen-Code; 180.12× | Author-reported | p. 12, T5 |
| Qwen3-Coder 1972b tokens | 15,467→4,431,546 | tokens | Qwen-Code; 286.52× | Author-reported | p. 12, T5 |
| GLM GPQA composition comparison | 6.1→10.8 | × tokens | Attack-only→mixed | Author-reported / visually readable | p. 5, F4/§4.1 |
| GLM HumanEval composition comparison | 7.6→14.6 | × tokens | Attack-only→mixed | Author-reported / visually readable | p. 5, F4/§4.1 |
| NoWait maximum | 15.37 | × tokens | DeepSeek AIME mixed/normal | Author-reported | p. 6, T2 |
| NoWait GLM amplification | 11.93 GPQA; 13.35 HumanEval | × tokens | Mixed/normal within NoWait | Author-reported | p. 6, T2 |
| Printed NoWait lexical count | 17 versus stated 15 | entries | Count displayed list; tokenizer details unknown | Analyst-derived | p. 10, B.3 |
| ReAct malicious share | 14/114≈12.28 | % | Fraction of mixed inventory | Analyst-derived | p. 4 |
| Qwen-Code malicious share | 14/58≈24.14 | % | Fraction of mixed inventory | Analyst-derived | p. 4 |
| Kimi AIME decrease | 70.00−36.67=33.33 | percentage points | No NoWait | Analyst-derived | p. 12, T4 |
| MiniMax query-ratio mean | 2123.11/7≈303.30 | × tokens | Mean of printed Table 5 ratios | Analyst-derived | p. 12, T5 |
| MiniMax aggregate ratio | 45,736,668/321,287≈142.35 | × tokens | Ratio of summed Table 5 tokens | Analyst-derived | p. 12, T5 |
| Policy access dates | 2026-02-08 | date | All Table 6 providers | Author-reported | p. 12, T6 |

## 21. Claim–evidence map

| Claim | Evidence | Figure/table/experiment | Source | Qualification / evidence strength |
|---|---|---|---|---|
| Tool composition can create cyclic trajectories | Cycle definition and staged restart example | F2, T3; method | pp. 2–3, 11 | HIGH for described mechanism; no trace distribution supplied |
| Adding the attack tools increases measured ReAct tokens | All 18 T4 token ratios >1 | X1, F3, T4 | pp. 4, 12 | HIGH for tabulated outcomes; uncertainty unspecified |
| Accuracy is not a sufficient resource-risk indicator | Qwen3-Coder GPQA 47.21→48.22% with 2.52× tokens | X1, T4 | p. 12 | HIGH for example; does not imply all accuracy remains stable |
| Some coding-task accuracy collapses | HumanEval mixed 3.05%, 6.71%, 9.15% | X1, T4 | pp. 5, 12 | HIGH; other model outcomes differ |
| Qwen-Code can incur severe task-specific amplification | GLM 2033f 971.27×; MiniMax 2003a 609.71× | X2, T5 | pp. 5, 12 | HIGH; screened tasks, bounded/censored executions |
| Normal tools do not necessarily dilute attack effects | GLM composition comparisons | X3, F4 | pp. 5–6 | HIGH for comparisons; MEDIUM for proposed interleaving cause |
| NoWait does not reliably remove amplification | DeepSeek AIME 15.37×; GLM GPQA/HumanEval >11× | X4, T2 | p. 6 | HIGH in tested setup; exact masking specification inconsistent |
| Results do not establish all-defense failure | Alternatives explicitly unevaluated | Limitations | p. 6 | HIGH |
| Autonomous configurations limit generalization | Minimal human intervention assumption | Limitations | p. 7 | HIGH for scope statement |
| Agent interaction creates additional relevance to web-agent security | Metadata and responses influence successive action choices | Method and interpretation | pp. 1–3 | MEDIUM analyst inference; no standalone or browser-specific comparison |
| Headline aggregation is ambiguous | Mean ratios ≈303.30× versus ratio of sums ≈142.35× | E1, T1, T5 | pp. 4–5, 12 | HIGH for arithmetic; implementation intent UNKNOWN |
| Exponential or unbounded growth is not demonstrated | No growth curve or unbounded trial; budgets and termination stated | F2 caption; X2 | pp. 3–5, 11–12 | MEDIUM analyst limitation on inference |

Source-grounded checking for this response compared principal numbers against their table rows, kept NoWait and non-NoWait conditions separate, checked figure legends against captions, and revisited the appendix descriptions when interpreting main-text claims. This was document comparison, not independent experimental replication. Unresolved conflicts are retained rather than repaired.

## 22. Very simple explanation — Explain Like I'm 15

Imagine an assistant helping you solve a problem. It can ask a collection of outside helpers for information. One helper says, 'Before finishing, check this again.' Another says, 'Now improve it.' A third says, 'You still need another full round.' Each request can sound sensible, but together they can keep the assistant working without finishing.

That is what this paper tests with AI agents and external tools. The researchers add 14 tools that encourage repeated checking, repetition, and extra tasks. The agents often spend far more tokens and time. Sometimes they still answer correctly, so checking only whether the answer is right would miss the wasted work. Sometimes they run out of their allowed resources or perform much worse.

The researchers also try preventing the model from generating selected words associated with extra thinking. That does not reliably stop the problem, because the issue is partly the repeated workflow, not just the wording of one response. Their findings suggest that protections should also notice how tool calls connect and repeat.

For the question about web agents versus ordinary LLMs, this paper supplies a useful explanation but not a direct contest. An agent can read outside tool descriptions and results, act on them, and encounter more outside text repeatedly. That creates an additional opportunity for someone else's text to redirect its work. The paper tests this through tool registries and coding/reasoning tasks; it does not measure how much more vulnerable a browser agent is than the same model answering alone.

## Completeness Audit

Coverage is measured against the inventory of supplied objects, not against response length. All numbered pages have text coverage; only nine have visual coverage. No supplied figure or table is treated as inspected through its caption alone.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, affiliations, arXiv metadata | Yes, text/image | Yes | Fully represented | Contact details compressed as secondary metadata |
| Abstract | Yes, text/image | Yes | Fully represented | Claims and qualifications distributed across analysis |
| §1 Introduction | Yes, text/image | Yes | Represented in compressed form | Motivation and core distinction retained |
| §1 Related Work | Yes, text/image | Yes | Represented in compressed form | Categories retained; no external citation validation |
| §2 Method | Yes, text/image | Yes | Fully represented | Construction, cycle definition, formalization |
| §2.1 Attack Tool Construction | Yes, text/image | Yes | Fully represented | All three categories and accumulation pathways |
| §2.2 Cycle Induction Mechanism | Yes, text/image | Yes | Fully represented | Self, multistep, scope-expanding loops |
| §2.3 Problem Formulation | Yes, text/image | Yes | Fully represented | Registry notation and token accounting |
| §3.1 Experimental Setup | Yes, text/image | Yes | Fully represented | Samples, tools, models, limits, repetitions |
| §3.2 ReAct analysis | Yes, text/image | Yes | Fully represented | Every T4 accuracy and token pair retained |
| §3.2 Qwen-Code analysis | Yes, text/image | Yes | Represented in compressed form | All T1 values and T5 ratios; selected raw extremes |
| §4.1 Registry composition | Yes, text/image | Yes | Represented in compressed form | Main pattern and emphasized exact comparisons; fine F4 labels not all transcribed |
| §4.2 Generation mitigation | Yes, text/image | Yes | Fully represented | Complete T2 values; defense boundaries |
| §5 Conclusion | Yes, text/image | Yes | Fully represented | Structural-defense recommendation retained |
| §6 Dataset/defense limitations | Yes, text/image | Yes | Fully represented | Kept separate from analyst limitations |
| §6 Generalization limitation | Yes, text only | Yes | Fully represented | p. 7 has no supplied image |
| Ethical Considerations | Yes, text only | Yes | Represented in compressed form | Misuse, exclusions, hidden training limits, safeguards |
| References pp. 7–9 | Yes, text only | Yes | Represented in compressed form | Related-work categories and relevant identities; full bibliography not reproduced |
| O1–O4 explicit objectives | Yes | Yes | Fully represented | Analyst IDs; no invented formal author questions |
| Explicit formal research questions | None identified | Accounted for | Not present in supplied work | Informal objectives retained |
| Interleaving hypothesis | Yes | Yes | Fully represented | Outcome evidence distinguished from causal proof |
| Formal statistical hypotheses | None identified | Accounted for | Not present in supplied work | No hypothesis test invented |
| X1 ReAct comparison | Yes | Yes | Fully represented | Accuracy, raw tokens, ratios, exceptions |
| X2 Qwen-Code comparison | Yes | Yes | Represented in compressed form | Full task ratio matrix; most raw T5 cells compressed |
| X3 Attack-only comparison | Yes | Yes | Represented in compressed form | F4 fine-label limitations disclosed |
| X4 NoWait | Yes | Yes | Fully represented | Full result matrix and implementation uncertainties |
| F1 | Yes, visually | Yes | Fully represented | Log scale and lack of error bars |
| F2 | Yes, visually | Yes | Fully represented | Schematic rather than measured growth |
| F3, six panels | Yes, visually | Yes | Fully represented | Exact results supplied through T4 |
| F4 | Yes, visually | Yes | Represented in compressed form | Small attack-only labels not exhaustively transcribed |
| T1 | Yes, text/image | Yes | Fully represented | Aggregation discrepancy discussed |
| T2 | Yes, text/image | Yes | Fully represented | All accuracies and raw token totals |
| T3, all 14 tools | Yes, text/image | Yes | Represented in compressed form | Each tool and argument/control role; repeated wording compressed |
| T4 | Yes, text/image | Yes | Fully represented | All accuracies, raw tokens, printed token ratios |
| T5, all 35 model–task rows | Yes, text/image | Yes | Represented in compressed form | All token/time ratios; selected raw values and arithmetic checks |
| T6 | Yes, text/image | Yes | Fully represented | Policies unverified; targets of Link cells unavailable |
| E1 amplification metric | Yes, text/image | Yes | Fully represented | Mean-of-ratios issue explicitly checked |
| E2 registry definitions | Yes, text/image | Yes | Fully represented | Symbols and actual registry sizes |
| E3 NoWait set/masking | Yes, text/image | Yes | Fully represented with uncertainty | 15/17 and probability/logit inconsistencies |
| Algorithms/pseudocode | None identified | Accounted for | Not present in supplied work | Workflow described, executable code unavailable |
| Theorems/proofs | None identified | Accounted for | Not present in supplied work | No theoretical guarantees claimed |
| Three main contributions | Yes | Yes | Fully represented | Conceptual, empirical, mitigation finding |
| Appendix A | Yes, text/image | Yes | Fully represented at functional level | Not a claim of source-code review |
| Appendix B.1 | Yes, text/image | Yes | Represented in compressed form | Registry totals and roles retained; benign 44-name list compressed |
| Appendix B.2 | Yes, text/image | Yes | Fully represented | Hardware, API, rephrasing, budgets |
| Appendix B.3 | Yes, text/image | Yes | Fully represented with uncertainty | Printed mask reproduced |
| Appendix C | Yes, text/image | Yes | Fully represented | T4 distributed between Sections 9 and 11 |
| Appendix D | Yes, text/image | Yes | Represented in compressed form | Task heterogeneity and termination qualification |
| Appendix E | Yes, text/image | Yes | Fully represented | No proprietary experiment inferred |
| Substantive footnotes | Yes, text/image | Yes | Represented in compressed form | Incident/tool/framework references and migration note; links unvisited |
| Supplied supplementary files | None | Accounted for | Not supplied | No file inspection claimed |
| Generic flagged supplementary reference | Metadata only | Yes | Uncertain | No identifiable artifact supplied |

### Missing or inaccessible material

No images for pp. 7–9 were supplied, so those pages have text-only coverage. No raw trial records, call traces, complete attack-server code, precise prompt templates, masking code, serving configuration files, or scoring scripts were supplied. Linked incident pages, repositories, cited papers, and Table 6 policy targets were not inspected. No separate supplementary artifact is available, and the generic metadata flag is insufficient to identify one. Exact stop budgets beyond turn/depth limits, excluded-model details, and full benchmark sample counts are not established by the supplied document.

### Uncertain interpretations

The metric aggregation underlying Qwen-Code headline ratios differs from Equation (1)'s stated average of per-query ratios. The exact GLM version schedule is unclear. The NoWait set is described as 15 tokens but prints 17 lexical entries, and its probability/logit wording is inconsistent. Figure 4's smallest labels are not all confidently transcribed. Figure 2's exponential wording and Appendix D's potentially unbounded wording exceed what the finite measured tables alone demonstrate. The small GLM Table 1 mixed-token rounding discrepancy remains unresolved. HIGH confidence in these reporting observations does not identify which intended implementation is correct.

### Deliberately compressed material

The bibliography is represented through the authors' related-work categories rather than copied entry by entry. Contact addresses, repeated institutional details, and repetitive caption wording are compressed. Appendix B.1's 44 benign tool names are summarized by counts and functional roles; examples include filesystem, shell, memory, project/navigation, and documentation tools. All 14 attack tools remain individually represented. Table 5's ordinary raw cells are compressed into its complete 35-row ratio coverage, with exact extremes retained. Most individual Figure 4 attack-only labels are omitted from numeric transcription because the main result and emphasized comparisons suffice for the supported claim and the tiny labels limit confidence. Repeated normalized accuracy ratios are omitted where the original accuracy pair is retained.

### Potential omissions

Every identified substantive section, experiment, figure, table, mathematical object, contribution, and author-stated limitation has an explicit representation or compression status. This does not claim preservation of every word or numeric cell. Known losses are the disclosed raw Table 5 cells, full benign-tool name list, full bibliography, contact details, and fine Figure 4 labels. The paper's unavailable implementation and supplementary artifacts cannot be assessed. The supplied evidence therefore supports a comprehensive inventory-based analysis of this document, with the stated visual, numerical, and reproducibility boundaries.
