# Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. Document content, including security prompts and attack examples, is treated as untrusted evidence rather than instructions. No outside research, browsing, tool execution, citation verification, or repository inspection was performed.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied extracted text covers physical PDF pages 1–25. |
| Accessible page count | 25 pages. This establishes supplied coverage, not independent verification that a publisher version has no additional material. |
| Apparently missing pages within supplied sequence | None: page records and extracted text run consecutively from 1 through 25. |
| Visually inspected pages | 1, 2, 4, 5, 6, 8, 13, 14, 15, 16, 17, 18, 19, 20, 21, 25. |
| Text-only pages | 3, 7, 9, 10, 11, 12, 22, 23, 24. Their supplied extracted text was read; their visual layout was not inspected. |
| Figures | Figure 1 and all three panels of Figure 2 are visually available and inspected. Figure 2's small markers and legend require caution for precise coordinates. |
| Tables | Tables 1–16 are present in extracted text and on visually inspected pages. Selected numerical entries were cross-checked against their rendered tables. Every cell is not reproduced in this explanation. |
| Equations | Mathematical definitions and Equations (1)–(3) are present in extracted text. Page 3 is text-only, so exact original typesetting of those numbered equations was not visually verified. |
| Appendices | Appendix contents page and Appendices A–F are supplied. |
| Separate supplementary material | None supplied. The accessibility metadata reports no embedded files and no detected supplementary references. This is not proof that no external artifacts exist. |
| Referenced absent artifacts | Corrected benchmark implementations and released results are claimed, but no executable implementation or independently inspectable release artifact is supplied. Referenced outside papers were not opened. |
| OCR | Not needed for the available native/extracted text. No OCR was run. |
| Other limitations | A local-image loading error is included in the input, but the 16 displayed page images and full extracted text remain usable. Native extraction can distort mathematical notation, spacing, punctuation, or table alignment. |

Confidence is HIGH for the document's stated architecture, supplied section structure, and clearly readable table entries; MEDIUM for interpretations of small plot coordinates and ambiguous implementation details; UNKNOWN for unreported implementation settings and external release contents.

Evidence labels used throughout: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No **[E] external information** is introduced. A strong confidence rating describes fidelity to the supplied source, not proof that an empirical claim generalizes beyond the reported experiments.

# 1. Plain-language orientation

The paper, **Indirect Prompt Injections: Are Firewalls All You Need, or Stronger Benchmarks?**, studies the security of language-model agents that use tools. Such an agent can read a file, retrieve a web page, inspect email, query a database, or call an application programming interface. The security problem is that retrieved material can contain instructions written by an attacker. The agent may mistake those instructions for legitimate directions and perform an action that its actual user never requested. The paper calls this an **indirect prompt injection**, abbreviated **IPI**. [A: pp. 1–3]

The authors propose two intermediary components at the boundary between the agent and its tools. The **Tool-Input Firewall**, or **Minimizer**, removes unnecessary information from outgoing tool arguments. The **Tool-Output Firewall**, or **Sanitizer**, examines incoming tool responses and removes suspected malicious instructions while attempting to preserve the information needed for the real task. These firewalls are implemented through prompts shown in Appendix D, rather than through retraining the agent. [A: pp. 1–3, 12–13]

They evaluate the approach on AgentDojo, Agent Security Bench, InjecAgent, and an attack-augmented Tau-Bench. The strongest recurring result is that sanitization sharply reduces measured attack success. However, the appendix tables qualify broad statements about eliminating attacks: AgentDojo contains small nonzero residual rates, Agent Security Bench retains nonzero rates, and InjecAgent results vary by model and setting. Security gains also do not imply that utility is unchanged for every model or in clean runs. [A/B: pp. 4–6, 13–21]

A second central contribution is methodological. The authors identify benchmark designs that can exaggerate attacks or incorrectly penalize legitimate task completion. Agent Security Bench can forcibly add attacker tools to an agent's plan. AgentDojo attacks can overwrite information needed to solve the original task. Utility checks can also confuse extra actions with failure. The paper therefore argues that a defense score is meaningful only when the benchmark preserves the task and measures the intended behavior faithfully. [A: pp. 5–6, 16–25]

**Relevance to the research question — analyst inference [D]:** The paper helps explain why web-capable AI agents can expose additional security opportunities: they consume attacker-controlled external content and can translate it into tool actions involving private information or external effects. It does **not** directly compare standalone large language models with web agents in a controlled experiment. It cannot establish a comparative vulnerability rate, isolate browsing as the cause, or demonstrate that every web agent is more vulnerable than every standalone model.

# 2. Document roadmap

The paper is a mixed **AI security, agent-system defense, empirical evaluation, and benchmark-analysis** work. It is not primarily a theoretical proof paper or a systematic literature review.

| Inventory ID | Original component | Pages | Role |
|---|---|---:|---|
| S0 | Title, authors, abstract, venue, contribution footnote | 1 | Identity and headline claims. |
| S1 | §1 Introduction and Contributions | 1–2 | Attack motivation, defense proposal, benchmark motivation. |
| S2 | §2 Method; §2.1 Problem setup; §2.2 Firewalls | 2–3 | Agent/tool notation, threat model, utility and attack metrics, architecture. |
| S3 | §3 Experiments | 3–4 | Four benchmarks and three evaluation metrics. |
| S4 | §4 Results | 4–5 | Main comparisons across benchmarks. |
| S5 | §5 Limitations of Current Benchmarks; §§5.1–5.4 | 5–6 | ASB, AgentDojo, InjecAgent problems and design guidelines. |
| S6 | §6 Discussion and Conclusion | 6 | Synthesis and future benchmark/attack directions. |
| REF | References [1]–[27] | 7–8 | Author-provided bibliography; not independently verified. |
| TOC | Appendix Table of Contents | 9 | Navigation for Appendices A–F. |
| A | Appendix A Related Works | 10–11 | Positioning against isolation, detection, prompt defenses, and retraining. |
| B | Appendix B Baselines | 11 | Prompt sandwich, spotlighting, injection detector. |
| C | Appendix C Experiments; C.1 Setup | 11–12 | Benchmark sizes and attack conditions. |
| D | Appendix D Minimizer and Sanitizer Prompts | 12–13 | Prompt-level implementation specification. |
| E | Appendix E Results; E.1–E.3 | 13–21 | Detailed original/fixed benchmark tables and InjecAgent discussion. |
| F | Appendix F Limitations; F.1.1, F.1.2, F.2.1 | 16–25 | Worked examples of missing task information, brittle utility checks, and forced tool injection. |

Visual and mathematical inventory: **F1**, Figure 1 pipeline, p. 2; **F2a–F2c**, Figure 2 benchmark scatterplots, p. 4; **T1–T16**, Tables 1–16, pp. 4–6 and 13–21; **EQ0**, unnumbered agent/metric definitions, pp. 2–3; **EQ1–EQ3**, numbered optimization and firewall equations, p. 3. Appendix D provides prompt procedures rather than a numbered algorithm. Appendix F provides three substantive worked examples, here registered as **EX1–EX3**.

The title page names Rishika Bhagwatkar, Kevin Kasa, Abhay Puri, Gabriel Huang, Irina Rish, Graham W. Taylor, Krishnamurthy Dj Dvijotham, and Alexandre Lacoste. Affiliations are ServiceNow Research, Mila–Quebec AI Institute, Université de Montréal, Vector Institute, and University of Guelph. Bhagwatkar and Kasa have an equal-contribution marker; Dvijotham and Lacoste have an equal-supervision marker. The supplied venue line identifies the 39th Conference on Neural Information Processing Systems, NeurIPS 2025, Lock-LLM Workshop. No keywords are supplied. [A/B: p. 1]

# 3. Background and context

A **large language model (LLM)** generates language and, in the system considered here, proposes tool calls. A **tool-calling agent** combines that model with external operations. A tool call includes a tool choice and, when applicable, arguments specifying what it should do. A tool response supplies information that can influence the next step. [A: pp. 1–3]

A **direct attack**, described here as jailbreaking, supplies adversarial instructions directly to the model. An **indirect prompt injection** places those instructions inside material returned by a tool. The distinction is about the path into the agent: the attacker-controlled content arrives through what should be treated as task data. [A: pp. 2–3]

The paper's examples include a bill containing an instruction to inspect transaction history and send an unrelated transfer, and a retrieved web page telling the agent to message an attacker-selected link. These examples illustrate an external-content-to-action pathway. The malicious text sometimes impersonates the user, names available tools, and frames the attacker action as a prerequisite for completing the legitimate task. These are observed properties of the examples, not independently tested universal attack mechanisms. [A/B: pp. 16–24]

**Personally identifiable information (PII)** is the paper's term for sensitive personal fields. **Data stealing (DS)** concerns private-information exposure. **Direct harm (DH)** is the other InjecAgent attack category. **Least-privilege data exchange** means sending only information needed for the intended operation. **Sanitization** means removing potentially malicious content while retaining useful task data. [A: pp. 1, 12–13, 21]

The paper distinguishes three metrics. **Benign utility (BU)** concerns legitimate task success without attacks. **Utility under attack (UA)** concerns legitimate task success while injected content is present. **Attack success rate (ASR)** concerns attacker-goal success. Lower ASR is desirable, but a system that achieves low ASR by refusing every task could have poor BU and UA. This is why the paper emphasizes security and utility together. [A: pp. 2–4, 6]

# 4. Research problem and gap

**Existing problem [A]:** Tool-calling agents use untrusted external information and may follow hidden attacker instructions instead of the user's intent. Their capabilities include actions such as booking travel, paying bills, and accessing information. The authors state that this expands the attack space and that even one successful injection can cause real-world harm. [p. 1]

**Shortcomings attributed to previous approaches [A]:** The introduction groups defenses into retraining, LLM-based detection, prompt augmentation, and system-level policies. Appendix A discusses execution isolation, restricted interpreters, privilege-based information control, context-minimizing agents, multiple firewall agents, trajectory re-execution, and robustness training. The authors describe implementation burden, resource requirements, potential incompatibility with black-box models, or utility losses as motivating a simpler interface-level approach. These descriptions are the paper's positioning; the cited systems were not independently inspected. [pp. 1, 10–11]

**Defense gap [A]:** The authors seek a modular intervention that can be inserted into existing agent pipelines without retraining or extensive task-specific policies. The contribution is the combination of outgoing data minimization and incoming response sanitization at the agent–tool boundary. [pp. 1–3]

**Evaluation gap [A]:** Existing benchmark scores may not measure agent vulnerability or legitimate completion faithfully. Forced tool selection, erased task-critical content, rigid state counters, and missing utility metrics undermine comparisons. [pp. 5–6]

**Scope [A/D]:** The experiments address particular tool-output injection settings, not arbitrary compromise of an entire agent stack. Their relevance to web agents follows from the inclusion of web pages and other retrieved content in the attack surface; the experimental population is broader than browser-only agents. [pp. 1–3, 11–12]

# 5. Research questions / objectives / hypotheses

The supplied paper does not formulate numbered research questions. It presents objectives and contributions. The following preserves that distinction.

| ID | Type | Source-grounded formulation | Source |
|---|---|---|---|
| O1 | Objective | Develop simple, modular, model-agnostic firewalls for tool-calling agents without retraining. | pp. 1–3 |
| O2 | Objective | Evaluate attack reduction together with legitimate task utility across four public benchmark suites. | pp. 3–4, 11–12 |
| O3 | Objective | Identify benchmark flaws, propose targeted fixes, and provide updated baseline results. | pp. 2, 5–6 |
| O4 | Objective | Recommend benchmark practices that preserve task information and assess BU, UA, and ASR. | p. 6 |
| H1 | Explicit informal hypothesis | Some enhanced InjecAgent attacks are less effective because they look more overtly malicious and are easier for recent models to ignore. | p. 15 |

H1 is an author hypothesis, not a demonstrated causal explanation. No separate experiment isolates attack conspicuousness from every other property of the enhanced setting. The effect is also model-dependent: enhanced attacks are weaker for GPT-4o and Qwen 3-32B, but stronger without defense for Llama 3.3-70B and Qwen 3-8B. [A/B: p. 21, Table 16]

**User research question [D]:** Why are web AI agents more vulnerable than standalone LLMs? This report uses the paper to identify plausible additional exposure and consequence pathways. That is a relevance inference; it is not a formal question tested by the authors.

# 6. Assumptions / threat model

The trusted starting point is the legitimate user's task. The attacker is assumed to affect **only content returned by tools**, not the tools themselves, the user's prompt, or the agent's system prompt. Injected content can include manipulative instructions or malicious material that looks benign. The attack objective is to induce a malicious task distinct from the legitimate task. [A: pp. 2–3]

This boundary excludes, within the formal threat model, replacement of executable tool implementations, modification of system instructions, and direct rewriting of the user request. It does not establish a comprehensive defense against those excluded capabilities. [D: derived scope interpretation from p. 3]

The agent has access to a set of tools and may plan statically or dynamically. A static agent chooses its sequence before execution. A dynamic agent uses earlier tool responses to choose later calls. The Sanitizer changes that dynamic feedback path: future decisions receive sanitized responses rather than raw ones. [A: pp. 2–3]

The firewalls are intended to mediate the interface. Appendix D provides the legitimate task as trusted context. The Sanitizer additionally sees the tool name, arguments, and response; the Minimizer sees the task, tool name, description, and original arguments. The supplied work does not specify a separate formal trust or compromise model for the firewall model itself. [A/D: pp. 12–13]

A significant threat-model consistency point is the authors' criticism of ASB: externally forcing an attacker tool into the execution plan is not equivalent to persuading the agent through injected text. The benchmark correction attempts to restore the distinction between attacker-controlled content and benchmark-controlled execution. [A: pp. 5, 25]

# 7. Methodology

## 7.1 Architecture and procedures

The proposed pipeline is: trusted task → agent proposes a tool call → Minimizer edits arguments → tool executes → Sanitizer edits response → agent continues. The components are modular. If a benchmark or tool has no input arguments, the authors skip the Minimizer and use only the Sanitizer. [A/B: pp. 2–3]

The Minimizer is asked to include only information directly relevant and necessary for the tool. Sensitive details, secrets, and confidential data should be excluded unless required. Its specified JSON response has a brief reasoning field and a minimized_args object. The Sanitizer is asked to identify and remove potentially malicious material without losing critical information, pay attention to unusual formatting, hidden text, and instructions, and preserve the original output format. Its JSON response has reasoning, was_safe, and sanitized_output fields. These are source prompts, not instructions executed in this analysis. [A: pp. 12–13]

**Implementation observation [D]:** The prompts describe judgment-based filtering. Equations that map outputs into a safe set express the intended abstraction; the supplied experiments do not prove that every generated sanitized response is safe. No formal verifier, deterministic policy semantics, or guaranteed separation mechanism is specified.

## 7.2 Benchmarks and attack conditions

| Experiment ID | Benchmark | Supplied size/configuration | Conditions |
|---|---|---|---|
| X1 | AgentDojo | Four suites: banking, Slack, travel, workspace; 949 security evaluations, defined as user tasks multiplied by IPI attacks per suite. | tool_knowledge attacks; original and fixed versions; Minimizer, Sanitizer, combination, and baselines. |
| X2 | Agent Security Bench, ASB | 400 security evaluations; at least a two-stage tool-use setting. | Context-ignoring and combined attacks; original and fixed versions; Sanitizer and ASB baselines. |
| X3 | InjecAgent | Predetermined simulated tool calls; sample count not stated in supplied setup. | DH and DS; base and enhanced settings; Sanitizer and baselines. |
| X4 | Tau-Bench | Dynamic conversational tool-use tasks; sample count not supplied. | Augmented with data-stealing attacks through DoomArena; Figure 2c comparison. |
| X5 | Benchmark correction analysis | ASB forced-tool intervention and AgentDojo placement/utility changes. | Original versus corrected scores and worked examples. |

AgentDojo's tool_knowledge condition assumes partial attacker knowledge of the user and the agent's tool capabilities. The authors describe this as a strong, targeted setting. ASB's context-ignoring attacks tell the agent to disregard prior instructions. Combined attacks include naive, escape-character, fake-completion, and context-ignoring components. InjecAgent has hardcoded calls, which the authors connect to its lack of utility evaluation. Tau-Bench was originally a utility benchmark and is augmented here with attacks. [A: pp. 11–12]

The reported evaluation counts should not be read as numbers of unique human participants or independent datasets. The supplied paper does not give a complete task-by-attack count breakdown, InjecAgent or Tau-Bench sample sizes, train/test splits, annotation protocols, or data licensing details. [A/D: pp. 11–12]

## 7.3 Models and baselines

AgentDojo tables evaluate gpt-4o-2024-08-06, Llama 3.3 70b, Qwen3 32b, and Qwen3 8b. ASB tables evaluate GPT-4o, Llama 3.3 70b, and Qwen3 8B. InjecAgent Table 16 includes GPT-4o, Llama 3.3-70B, Qwen 3-32B, and Qwen 3-8B. Figure 2 averages over models, but the supplied Tau-Bench description does not specify its model roster. [A/B: pp. 4, 13–21]

Prompt sandwich repeats the user query near tool output. Spotlighting delimits tool output with special characters. The PI Detector is a DeBERTa-v3-based prompt-injection classifier. ASB comparisons include delimiters_defense, instructional_prevention, and ob_sandwich_defense. AgentDojo's setup says the benchmark supports a tool-filter baseline, but the supplied result tables do not include a tool-filter row. Baseline names differ across sections; repeat prompt and prompt sandwich are related descriptions, but their full implementation equivalence cannot be confirmed from the supplied material. [A: pp. 11–12; B: tables]

## 7.4 Metrics and reporting

BU measures clean task success; UA measures legitimate task success under attack; ASR measures attacker task success. Safe refusal or ignoring an injection counts as ASR = 0, without automatically implying user-task success. The paper acknowledges that benchmarks compute utility differently. [A: pp. 3–4]

Tables report values with ± terms. Their meaning is not specified: the supplied text does not identify them as standard deviations, standard errors, confidence intervals, or another quantity. Run counts, random seeds, significance tests, decoding parameters, hardware, library versions, firewall-model identity, token budgets, detector thresholds, latency, and monetary costs are not reported. Statistical significance cannot be inferred merely from the word significantly in the prose. [D: reporting observation]

# 8. Experiments / analyses

## X1 — AgentDojo defense comparison

Purpose: evaluate input minimization, output sanitization, and their combination against targeted tool_knowledge attacks across four task suites. Metrics: BU, ASR, UA. Evidence: Figure 2a; fixed Tables 4–6; original Tables 7–9. [A: pp. 4, 11, 13–18]

For GPT-4o on fixed AgentDojo, no-defense ASR is 34.32±2.49, Minimizer ASR is 13.64±1.58, Sanitizer ASR is 0.01±0.03, and combined ASR is 0.00±0.00. Corresponding UA values are 72.19±2.79, 64.04±2.11, 72.59±1.71, and 66.52±1.77. These are separate conditions, not a single result. [A/B: Tables 5–6]

The Sanitizer's fixed overall ASR remains nonzero for all four reported models: 0.01±0.03, 0.10±0.07, 0.01±0.03, and 0.82±0.34. The combination reaches exact displayed zero only for GPT-4o overall; other overall combined values are 0.06±0.05, 0.06±0.10, and 0.32±0.14. These entries contradict a literal reading of the main text's statement that the Sanitizer achieves zero across all models and suites. [A/B: p. 4 versus p. 14]

Utility effects depend on the model and whether the run is clean. Fixed Llama UA falls from 57.92±2.04 without defense to 48.67±2.03 with the Sanitizer. Qwen3 32b UA rises from 47.60±1.56 to 62.98±1.02. GPT-4o clean BU falls from 81.97±5.31 to 67.10±7.52. Thus substantial attack reduction and useful UA coexist with utility penalties in particular conditions. [A/B: Tables 4 and 6]

## X2 — ASB defense comparison

Purpose: assess sanitization under context-ignoring and combined attacks in a multi-stage tool setting. Metrics: ASR and benchmark utility; clean utility is separately tabulated. Evidence: Figure 2b; original Tables 10–12; fixed Tables 13–15. [A/B: pp. 18–21]

On fixed context-ignoring attacks, Sanitizer ASR is 2.33±0.88 for GPT-4o, 7.00±2.83 for Llama, and 5.17±0.63 for Qwen3 8B. On fixed combined attacks, the corresponding values are 2.58±1.26, 7.25±0.35, and 3.00±0.66. These are the lowest displayed ASRs within each model/attack comparison. [A/B: Tables 14–15]

Utility does not uniformly improve. GPT-4o combined utility is 67.42±0.29 without defense and 61.67±0.76 with Sanitizer. Llama combined utility is 96.08±0.14 versus 81.62±0.88. Qwen3 8B improves from 16.08±0.52 to 37.58±1.88. ASB's metric is itself criticized, so these values should not be equated with independently established real-world task completion. [A/B: pp. 4–5, Table 15]

## X3 — InjecAgent attack comparison

Purpose: test DH and DS attacks under base and enhanced conditions with predetermined tool calls. Only the Sanitizer is used from the proposed pair because tool inputs are absent. Metrics: ASR-like attack percentages; BU and UA unavailable. Evidence: Tables 1 and 16, Appendix E.3. [A: pp. 4, 12, 15, 21]

Sanitizer base/enhanced average results are GPT-4o 0.3±0.0 / 0.0±0.0; Llama 3.3-70B 3.0±0.1 / 1.1±0.1; Qwen 3-32B 0.5±0.1 / 0.1±0.1; Qwen 3-8B 0.3±0.1 / 0.3±0.2. No-defense averages are respectively 8.3±0.3 / 3.8±0.0; 69.3±0.0 / 93.0±0.1; 6.8±0.2 / 3.2±0.6; 1.1±0.1 / 5.8±0.5. [A/B: Table 16]

The PI Detector ties the Sanitizer at displayed zero for GPT-4o enhanced attacks, has a lower Qwen 3-32B enhanced average, and has a lower Qwen 3-8B enhanced average. Therefore the Sanitizer is not uniquely best in every individual condition. Utility cannot adjudicate these comparisons because that metric is absent. [B/D: Table 16]

## X4 — Tau-Bench with added attacks

Purpose: evaluate security/utility trade-offs in dynamic conversational tasks. Data-stealing attacks are added using DoomArena. Figure 2c and prose report zero ASR for the Sanitizer without utility degradation, while PI detection has severe utility degradation. Exact tabulated values, sample counts, detailed attack-generation settings, and model-specific results are not supplied. [A/B: pp. 4–5, 12]

## X5 — Benchmark correction analysis

ASB correction removes forced attacker-tool insertion while leaving attacker tools available for voluntary selection. AgentDojo correction preserves task-critical information and changes brittle utility checks toward semantic goal completion. Tables 2–3 and Appendix F illustrate effects. [A: pp. 5–6, 16–25]

For AgentDojo GPT-4o without defense under tool_knowledge, original UA 60.87±2.59 becomes fixed UA 72.19±2.79. **Analyst-derived [C]:** 72.19−60.87 = 11.32 percentage points; 11.32/60.87×100 ≈ 18.60% relative increase. This explains the reported improvement greater than 18%; it is not an 18-percentage-point increase. The aggregate comparison combines placement and scoring changes, so their separate contributions are not isolated. [Tables 3, 6, 9]

# 9. Results

The most defensible high-level finding is that **output sanitization strongly reduces measured injection success across the reported settings**, with important residuals and utility qualifications. The detailed evidence is more precise than the absolute-zero language in parts of the main text. [A/B: pp. 4–6, 14–21]

| Finding | Exact condition and evidence | Qualification |
|---|---|---|
| Sanitizer sharply reduces AgentDojo ASR | Fixed GPT-4o: 34.32±2.49 without defense → 0.01±0.03 Sanitizer; Table 5. | Near zero, not exact zero; overall result for tool_knowledge. |
| Minimizer reduces attacks but can reduce utility | Fixed GPT-4o: ASR 13.64±1.58; UA 64.04±2.11 versus no-defense UA 72.19±2.79; Tables 5–6. | Redaction can remove task-relevant arguments. |
| Combining firewalls can further reduce utility | Fixed GPT-4o UA 66.52±1.77 combined versus 72.59±1.71 Sanitizer; Table 6. | Other models have different trade-offs; not a universal ordering in every suite. |
| Sanitizer is lowest-ASR ASB defense in supplied comparisons | Fixed GPT-4o combined ASR 2.58±1.26 versus 9.25±0.25 without defense; Table 15. | Benchmark utility and attack-tool semantics remain problematic. |
| InjecAgent improvements are large but model-dependent | Llama base average 69.3±0.0 → 3.0±0.1; enhanced 93.0±0.1 → 1.1±0.1; Table 16. | No utility metric; nonzero residual attacks. |
| Enhanced attacks are not consistently stronger | GPT-4o no-defense average 8.3±0.3 base versus 3.8±0.0 enhanced; Llama 69.3±0.0 versus 93.0±0.1. | Author explanation is a hypothesis, not a controlled causal result. |
| Corrected AgentDojo raises measured UA | GPT-4o no-defense 60.87±2.59 original versus 72.19±2.79 fixed; Table 3. | Changing task information and measurement can alter score meaning. |
| Clean utility can fall with sanitization | Fixed GPT-4o BU 81.97±5.31 without defense versus 67.10±7.52 Sanitizer; Table 4. | Contradicts interpreting high utility as no utility cost in all conditions. |

Additional derived comparisons [C]: fixed GPT-4o AgentDojo ASR reduction is 34.32−0.01 = **34.31 percentage points**; fixed Llama AgentDojo UA change is 48.67−57.92 = **−9.25 percentage points**; fixed Qwen3 32b UA change is 62.98−47.60 = **+15.38 percentage points**. These calculations use reported means only and do not establish statistical significance or uncertainty intervals for the differences.

# 10. Figure-by-figure interpretation

## Figure 1 — Minimize & Sanitize tool-calling pipeline

Figure 1 is a flow diagram, not a quantitative plot. It depicts a trusted user task on the left, an AI agent containing an LLM, an outgoing Tool-Input Firewall, tools within the environment, an attacker near that environment, a Tool-Output Firewall below the tool response, and a return arrow to the agent. [B: p. 2]

The agent proposes reading a bill file. The tool-output example contains a service entry, Car Rental 98.70, plus an attacker payment instruction. The sanitized example retains the service and amount while dropping the extraneous payment instruction. Arrows show both outgoing requests and the response feedback loop. The figure therefore illustrates preserving legitimate task data while removing behavior-changing content. It does not demonstrate that the filter succeeds on every attack. [A/B]

A minor naming discrepancy is visible: the user-task label refers to bill-december.txt, while the tool call refers to bill-december-2023.txt. This is a schematic filename inconsistency, not evidence of a measured execution failure. The attacker bank-account string is abbreviated and is not a complete account identifier. [B/D]

## Figure 2a — AgentDojo security/utility comparison

This is a scatterplot. The horizontal axis is Utility under attack, with visible ticks approximately 30–55; the vertical axis is ASR (%), with ticks 0–30 and a plotting area slightly above 30. Both scales are linear. The horizontal label omits a percent sign, although the numerical utility reporting elsewhere uses percentage-scale values. [B: p. 4]

The legend separates None, PI Detector, Repeat prompt, Spotlighting, Tool input firewall, Tool output firewall, and Combined using colors and marker shapes. The no-defense marker is high in ASR. Detector performance is at lower utility. Output sanitization and combination lie close to the bottom at comparatively high utility; input minimization occupies an intermediate security position. Exact coordinates are not printed beside markers, and the figure's averages can hide model-specific costs. [B/D]

The caption says both metrics are averaged over models. No error bars or significance annotations are shown. Detailed Tables 4–6 must take precedence for exact model-specific numbers. Apparent plot-level zero does not override the small nonzero values in Table 5. [A/B]

## Figure 2b — Agent Security Bench comparison

This scatterplot uses Utility under attack horizontally, with visible ticks 57–61, and ASR (%) vertically, with ticks 5–25. The displayed defenses are None, Delimiters Defense, Instructional Prevention, Ob Sandwich Defense, and Tool output firewall. Scales are linear. [B]

The Tool-Output Firewall marker is lowest in ASR, at approximately 4–5%, with utility around 60. Other points are approximately 23–26% ASR at utility around 56.5–61. These are **approximate visual estimates**, not exact reported values. The main caption's language of eliminating attacks is too strong for this panel because the defense point is visibly above zero and ASB tables retain nonzero ASR. [B/D: p. 4; Tables 14–15]

The panel does not identify its precise aggregation over ASB attack types. Although the main text points to fixed result tables, the exact plot-generation averaging rule is not supplied. Model averages cannot demonstrate equal protection for all models. [D]

## Figure 2c — Tau-Bench comparison

This scatterplot explicitly labels both horizontal utility and vertical ASR as percentages. Visible ticks run 0–60 on both axes, with a slightly larger plotting extent. The legend lists None, PI Detector, Repeat prompt, Spotlighting, and Tool Output Firewall. [B]

The Sanitizer lies at approximately 60–62% utility and zero ASR. The PI Detector lies near roughly 5–6% utility and zero ASR. Several other methods cluster around roughly 40% utility and 48–50% ASR. These positions are **approximate visual estimates** because the plot does not label exact numerical coordinates. [B]

The panel supports the authors' reported security/utility advantage in this particular augmented Tau-Bench evaluation. It does not provide enough information to recover exact per-model scores, variation, counts, or attack construction details. [A/D]

# 11. Table-by-table interpretation

All tables below were inspected in supplied text and rendered images. Numerical results are interpreted on the paper's percentage reporting scale. The meaning of each ± term remains unspecified. No table supplies a significance-test annotation. Suite-level cells and repeated baseline rows are compressed deliberately, with important exceptions retained.

## Table 1 — GPT-4o InjecAgent base versus enhanced attacks, p. 4

Rows compare None, PI Detector, Spotlighting, Prompt sandwich, and Tool Output Firewall. Columns are Base and Enhanced. Results are respectively 8.3±0.3 / 3.8±0.0; 3.1±0.5 / 0.0±0.0; 5.1±0.1 / 1.5±0.1; 1.0±0.3 / 2.0±1.4; 0.3±0.0 / 0.0±0.0. The Sanitizer is lowest in base attacks and ties the detector at zero enhanced attacks. Enhanced prompt sandwich is worse than its base value. Utility is not measured.

## Table 2 — Original versus fixed ASB GPT-4o, p. 5

Context-ignoring original ASR/utility: 70.67±2.10 / 70.08±1.04; fixed: 10.83±0.63 / 66.00±1.56. Combined original: 73.58±2.70 / 71.17±0.14; fixed: 9.25±0.25 / 67.42±0.29. The table's rows do not identify a defense. Cross-checking Tables 11–12 shows that its original values match delimiters_defense, while its fixed values match no-defense rows in Tables 14–15. The comparison therefore does not clearly hold defense constant. The text's 70% to 9.25% statement also mixes an approximate starting value with the combined fixed result. The qualitative forced-injection problem is illustrated independently, but this table does not cleanly isolate its numerical effect under one constant defense.

## Table 3 — AgentDojo GPT-4o utility after fixes, p. 6

Original tool_knowledge utility is 60.87±2.59; fixed utility is 72.19±2.79. These match the no-defense overall UA rows of Tables 9 and 6. The result is an 11.32-percentage-point increase, approximately 18.60% relative, as calculated above. The table does not separate the effects of placement corrections and utility-check changes.

## Table 4 — Fixed AgentDojo clean utility, p. 13

Four model blocks and seven defenses are compared across Overall, Banking, Slack, Travel, and Workspace. The column is misspelled Salck in the source. Overall no-defense/Sanitizer/combined values are GPT-4o 81.97±5.31 / 67.10±7.52 / 58.39±4.28; Llama 59.27±5.31 / 48.77±5.69 / 39.32±3.63; Qwen3 32b 55.41±3.96 / 57.57±5.18 / 57.80±3.44; Qwen3 8b 39.47±1.77 / 38.08±1.77 / 36.18±2.87. Highest overall displayed clean utility is Repeat prompt for GPT-4o, Spotlighting for Llama and Qwen3 8b, and Repeat prompt for Qwen3 32b. The PI Detector has the lowest overall value in each model block. Clean utility costs are substantial for some defenses and models.

## Table 5 — Fixed AgentDojo ASR under tool_knowledge, p. 14

Same models, defenses, and suites as Table 4. Overall no-defense/Sanitizer/combined ASRs are GPT-4o 34.32±2.49 / 0.01±0.03 / 0.00±0.00; Llama 35.93±1.51 / 0.10±0.07 / 0.06±0.05; Qwen3 32b 40.56±0.84 / 0.01±0.03 / 0.06±0.10; Qwen3 8b 18.70±0.70 / 0.82±0.34 / 0.32±0.14. Combination is lowest overall for GPT-4o, Llama, and Qwen3 8b; Sanitizer is lowest for Qwen3 32b. Qwen3 8b Sanitizer Slack ASR is 2.54±0.55, a consequential residual hidden by an overall near-zero description. Multiple other suite cells are exactly displayed zero.

## Table 6 — Fixed AgentDojo UA under tool_knowledge, p. 15

Overall no-defense/Sanitizer/combined UA is GPT-4o 72.19±2.79 / 72.59±1.71 / 66.52±1.77; Llama 57.92±2.04 / 48.67±2.03 / 41.84±1.02; Qwen3 32b 47.60±1.56 / 62.98±1.02 / 58.21±1.56; Qwen3 8b 34.07±0.76 / 39.72±1.09 / 37.90±1.15. Repeat prompt has highest overall UA for GPT-4o, Spotlighting for Llama, and Sanitizer for both Qwen models. Security-optimal and utility-optimal choices differ. GPT-4o Sanitizer Travel UA 65.24±1.09 exceeds its no-defense 58.10±5.07, while Slack UA 73.65±1.98 is below no-defense 84.76±2.86.

## Table 7 — Original AgentDojo clean utility, p. 16

This reproduces the clean condition on the original benchmark. Overall no-defense/Sanitizer/combined values are GPT-4o 83.02±5.33 / 67.68±3.56 / 58.41±2.61; Llama 62.80±3.44 / 53.17±3.09 / 41.21±4.42; Qwen3 32b 53.83±3.36 / 52.56±4.05 / 54.11±1.80; Qwen3 8b 42.71±1.97 / 38.10±2.18 / 37.10±3.70. This establishes a second benchmark version, not an additional attack condition. Clean values differ between original and fixed AgentDojo; the exact cause of each difference is not documented.

## Table 8 — Original AgentDojo ASR, p. 17

Overall no-defense/Sanitizer/combined ASR is GPT-4o 34.22±3.07 / 0.01±0.03 / 0.16±0.14; Llama 36.32±1.18 / 0.15±0.03 / 0.07±0.05; Qwen3 32b 38.37±0.51 / 0.03±0.05 / 0.01±0.03; Qwen3 8b 20.96±0.75 / 0.59±0.24 / 0.12±0.14. Near-zero patterns also appear before correction. Combined defense is not always better than Sanitizer: GPT-4o combined is higher. Original and fixed conditions must remain distinct.

## Table 9 — Original AgentDojo UA, p. 18

Overall no-defense/Sanitizer/combined UA is GPT-4o 60.87±2.59 / 67.99±1.75 / 60.50±2.14; Llama 47.31±1.02 / 46.01±1.48 / 41.00±1.04; Qwen3 32b 35.74±0.93 / 48.27±1.66 / 47.89±0.83; Qwen3 8b 25.88±1.04 / 33.51±1.19 / 29.95±1.24. The comparison with Table 6 supports higher fixed UA in many conditions, but changes are not uniform across every suite. The original Sanitizer already improves GPT-4o and both Qwen overall UA relative to no defense.

## Table 10 — Original ASB clean utility, p. 18

Rows compare five defenses across three model blocks. No-defense/Sanitizer utility is GPT-4o 72.83±0.58 / 64.25±0.90; Llama 100.00±0.00 / 97.42±0.38; Qwen3 8B 59.92±0.14 / 59.83±0.14. Llama has displayed 100.00 for no defense, instructional prevention, and sandwich defense. The authors warn that this can arise from calling all tools rather than meaningful completion. Qwen instructional prevention has the highest clean value, 82.33±1.23.

## Table 11 — Original ASB context-ignoring attacks, p. 19

No-defense versus Sanitizer ASR/utility: GPT-4o 66.83±2.81 / 68.50±0.87 versus 12.25±0.50 / 63.50±2.54; Llama 63.58±0.38 / 96.92±0.38 versus 10.42±1.26 / 93.08±0.52; Qwen3 8B 19.17±0.38 / 26.25±0.25 versus 6.50±0.43 / 49.08±1.26. Sanitizer is lowest ASR for each block, but lowers utility for GPT-4o and Llama while increasing it for Qwen.

## Table 12 — Original ASB combined attacks, p. 19

No-defense versus Sanitizer ASR/utility: GPT-4o 67.50±1.95 / 68.75±1.00 versus 16.33±1.70 / 63.42±1.46; Llama 62.58±0.52 / 96.42±0.63 versus 9.42±0.29 / 79.17±0.58; Qwen3 8B 13.92±0.76 / 12.42±0.63 versus 4.83±0.52 / 40.25±1.15. Residual rates are much larger than corresponding fixed Sanitizer results for GPT-4o. The large Llama utility reduction deserves preservation alongside its security gain.

## Table 13 — Fixed ASB clean utility, p. 20

Every displayed value matches Table 10. The correction therefore leaves these reported clean ASB results unchanged. That observation is limited to the presented numbers; it does not prove identical execution traces or unchanged implementation in all respects. The same metric-quality caveats apply.

## Table 14 — Fixed ASB context-ignoring attacks, p. 20

No-defense versus Sanitizer ASR/utility: GPT-4o 10.83±0.63 / 66.00±1.56 versus 2.33±0.88 / 62.33±1.51; Llama 52.92±0.29 / 95.92±0.29 versus 7.00±2.83 / 94.88±0.18; Qwen3 8B 14.75±0.43 / 26.33±0.29 versus 5.17±0.63 / 44.67±0.63. Sanitizer is lowest ASR in every block. The fixed no-defense ASR remains high for Llama, demonstrating that a dramatic GPT-4o correction effect is not universal across models.

## Table 15 — Fixed ASB combined attacks, p. 21

No-defense versus Sanitizer ASR/utility: GPT-4o 9.25±0.25 / 67.42±0.29 versus 2.58±1.26 / 61.67±0.76; Llama 52.92±0.63 / 96.08±0.14 versus 7.25±0.35 / 81.62±0.88; Qwen3 8B 10.75±0.50 / 16.08±0.52 versus 3.00±0.66 / 37.58±1.88. Sanitizer is lowest ASR. GPT-4o Sanitizer utility equals the displayed instructional-prevention mean 61.67, but uncertainty terms differ. Highest utility is sandwich defense for GPT-4o, instructional prevention for Llama, and Sanitizer for Qwen.

## Table 16 — InjecAgent by model, attack category, and setting, p. 21

Columns separate DH, DS, and Avg within Base and Enhanced. The table adds important information beyond Table 1. Llama no-defense enhanced DS is 97.8±0.3, reduced to 1.3±0.1 by Sanitizer. GPT-4o base DS is 12.3±0.6 without defense versus 0.4±0.0 Sanitizer. Qwen3 8B base DH is 0.7±0.1 Sanitizer versus 0.2±0.0 PI Detector; low overall averages can therefore hide category-specific differences.

Two internal average issues deserve caution. GPT-4o enhanced Prompt sandwich displays DH 0.2±0.0, DS 0.9±0.1, Avg 2.0±1.4; that average exceeds both component means. Llama base PI Detector displays DH 53.7±1.6, DS 72.3±1.0, Avg 67.0±0.3; the simple mean of displayed components is 63.0. The source does not define Avg weighting or explain these discrepancies. The first cannot be an ordinary positive-weight average of the two displayed means. Neither value is silently repaired.

# 12. Diagram / architecture interpretation

Figure 1 represents both a control sequence and a data path. The user task supplies the purpose. The agent chooses an operation. The Minimizer constrains outgoing information, the environment executes the operation, and the Sanitizer constrains incoming information. The sanitized response returns to the agent, closing the loop. [A/B: p. 2]

For dynamic planning, the important architectural effect is that the next decision depends on sanitized previous output. For static planning, the predetermined input and output sequences are replaced with minimized and sanitized sequences. The tool itself is not retrained or changed by the specified mechanism. [A: p. 3]

The two firewalls address different points in an attack chain. The Sanitizer aims to stop the agent from accepting an attacker instruction. The Minimizer can limit unnecessary data transmitted in later calls, including potentially sensitive fields. Its task dependence creates a trade-off: removing information can reduce exposure but also prevent a legitimate operation. [A/D: pp. 1, 3–4]

Appendix F's colored dialogue boxes distinguish user, assistant, and tool roles. These are substantive evidence displays, not additional numbered architecture figures. EX1 shows a read-bill → read-transactions → unrelated transfer path and then contrasts absent versus preserved bill details. EX2 shows retrieval of a web page followed by an attacker-selected message. EX3 shows a selected two-tool workflow expanded to include every tool, including LoanFraud, after forced injection. Their arrows are implicit in conversational order rather than drawn connectors. [A/B: pp. 16–25]

# 13. Equations and mathematical concepts

## EQ0 — Tools, plans, and success, pp. 2–3

The tool set is T = {T₁,…,T_M}, where M is the number of tools and A denotes the agent. Tool T_m accepts an n_m-tuple X_m = (x_m,1,…,x_m,n_m) and returns a p_m-tuple Y_m = (y_m,1,…,y_m,p_m). Each argument and output belongs to an appropriate tool-specific domain. Native extraction uses similar-looking symbols for tuples and their domains; the exact typography is not visually verified because p. 2's notation is small and p. 3 is text-only.

The legitimate task is μ. A plan π_μ contains N tool/input steps, with tool index m_k between 1 and M. Static plans choose calls in advance; dynamic plans use previous outputs. S(μ;π) ∈ {0,1} is the benchmark's task-success indicator. **BU = E_μ[S(μ;π_μ)]** is expected legitimate success without an attack. The expectation's task distribution is not specified in detail.

For attack I and malicious task μ*, the attack-influenced plan is π_μ|I. **ASR = E_μ*[S(μ*;π_μ|I)]** measures malicious-task success; **UA = E_μ[S(μ;π_μ|I)]** measures legitimate-task success under attack. These definitions permit both, neither, or only one goal to succeed. They explain why one metric cannot replace the other.

## Probability factorization — unresolved mathematical assertion, p. 3

The paper writes P(μ,μ*;π_μ|I) = P(μ;π_μ|I)P(μ*;π_μ|I), then says ASR and UA are independent. **Analyst observation [D]:** The fact that four joint outcomes are possible does not establish probabilistic independence. Independence requires the displayed factorization to hold; it cannot be inferred merely from nonexclusive success events. No proof or empirical dependence analysis is supplied. The examples support separate measurement of attacker and user outcomes, which is a weaker and useful point, but do not establish the claimed factorization.

## Equation (1) — Defense objective, p. 3

The objective is written as robust plan π̃_μ = argmin over π_μ of {E_μ*[S(μ*;π_μ|I)] − E_μ[S(μ;π_μ|I)]}. In ordinary language, choose a plan that makes attacker success small and legitimate success large. The subtraction rewards UA and penalizes ASR with equal displayed coefficient magnitude.

This is a mathematical statement of desired behavior. The supplied implementation does not describe explicitly solving this optimization, estimating its gradients, or exhaustively searching plans. No trade-off weight, attack distribution, or proof of optimum attainment is specified. Treating it as an optimization algorithm would overstate the source.

## Equation (2) — Input minimization, p. 3

X̃_m = {x̃_m,i} for i = 1,…,n_m, with x̃_m,i = F_in(x_m,i) ∈ X_m^safe. F_in maps each proposed input component into a minimized component in a designated safe input set. The output is the modified argument collection used by the tool.

The safe set has no operational mathematical definition in the supplied text. The prompt implementation considers the task and tool description, although the compact equation writes only the individual argument as the function input. That difference is an abstraction gap, not necessarily an implementation contradiction.

## Equation (3) — Output sanitization, p. 3

Ỹ_m = {ỹ_m,j} for j = 1,…,p_m, with ỹ_m,j = F_out(y_m,j) ∈ Y_m^safe. F_out maps each tool-output component to a sanitized component. In dynamic planning, Ỹ from the previous step becomes the agent's next-step context.

Again, the safe output set is not formally characterized. Appendix D's Sanitizer sees task context and arguments in addition to the response. The formula expresses intended transformation; it does not prove that injected behavior is impossible. No theorems, lemmas, proofs, or formal safety guarantees are supplied.

# 14. Interpretation and discussion

**Authors' interpretation [A]:** A relatively simple interface defense achieves very low attack success on existing benchmarks, and benchmark weaknesses partly explain why present evaluations are insufficiently challenging. Better tests should preserve task context and measure meaningful completion. [pp. 4–6, 11]

**Analyst interpretation [D]:** The defense results and benchmark critique must be read together. Low ASR is encouraging for the tested attacks, but benchmark rigidity, context ambiguity, and flawed metrics limit claims about adaptive attackers and real deployments. Strong scores on a corrected benchmark are still scores on a particular benchmark.

The main text–appendix consistency check identifies several unresolved points:

1. **Zero versus near-zero AgentDojo:** p. 4 states zero across all models and suites; Table 5 reports residuals, including Qwen3 8b Slack 2.54±0.55 and overall 0.82±0.34.
2. **Utility preservation:** Figure 2's caption generalizes no utility cost, but Tables 4, 6, and 15 show clean or attack-condition costs for particular models. Averaged plots do not erase these differences.
3. **Firewall naming:** Appendix A repeatedly says a single input firewall prevents essentially all injections, while the main method and results identify the Tool-Output Firewall as the strongest defense. This may reflect naming from the prior system discussion or an editorial error; the source does not resolve it.
4. **ASB correction comparison:** Table 2's original numbers match delimiter defense and fixed numbers match no defense. The defense condition is not held visibly constant.
5. **ASB utility semantics:** p. 5 says invoking an attacker tool assigns utility zero, yet ASB tables contain nonzero ASR alongside high utility. If this rule and both rates used the same binary per-run outcomes and denominator, utility could not exceed 100−ASR. For example, Table 11's Llama no-defense ASR 63.58 and utility 96.92 violate that bound. The aggregation or implementation needed to reconcile this is not supplied.
6. **InjecAgent averages:** Table 16 includes component/Avg inconsistencies described above. Values are retained as reported.
7. **Slack example:** pp. 23–24 state fixed utility becomes one, but the displayed trace shows an attacker link sent to Alice and the article summary spoken to the user; it does not visibly show the summary being sent to Alice. The prose's claimed legitimate success is not fully established by the displayed trace.
8. **Fixed bill example:** p. 22 requests leakage of a music-streaming subscription, while p. 23 sends an IBAN in the subject. The target of the shown attack changes across the displayed prompt and action.

These observations do not negate the architecture or every result. They bound which exact quantitative and explanatory conclusions can be taken confidently from the supplied paper.

# 15. Contributions and novelty

| Contribution category | Author contribution | Qualification |
|---|---|---|
| Conceptual | Minimize & sanitize at the agent–tool boundary. | Related minimization and firewall approaches are acknowledged. |
| Methodological/system | Two modular components usable with static or dynamic agents and optional tool inputs. | Modularity is described; broad deployment compatibility is not independently demonstrated. |
| Implementation | Explicit JSON-oriented Minimizer and Sanitizer prompts. | Firewall model and execution/error-handling details are absent. |
| Empirical | Comparisons across four benchmarks and several models. | Exact zero and no-cost utility claims require condition-specific qualification. |
| Benchmark | Identify ASB forced tool insertion, AgentDojo content deletion and brittle checks, InjecAgent utility omission. | These are distinct measurement problems, not one interchangeable flaw. |
| Evaluation practice | Recommend meaningful utility and preserved task context. | A recommended design direction, not a fully validated universal scoring standard. |

No new trained model, theorem, formal security proof, or wholly new dataset is demonstrated. The authors claim corrected releases and updated baseline results, but executable release artifacts were not supplied or reviewed. Claims of simplicity and model agnosticism concern the proposed interface design; quantitative deployment overhead is not measured in the supplied work. [A/D: pp. 1–3, 6, 11–13]

# 16. Limitations

## Authors' stated limitations

The authors identify unnecessary-input redaction as a cause of lost task utility. They acknowledge that ASB's residual ASR can reflect benign-looking attacker tools being counted as malicious merely when called. They criticize ASB utility for ignoring sequencing, argument coherence, and contextual relevance. [A: pp. 4–5]

AgentDojo can replace task-critical information and can use strict state-delta checks that underestimate successful completion with extra actions. InjecAgent omits both clean and attack-condition utility metrics. Existing attacks can be rigid, context-agnostic, or dependent on fixed trigger phrases. Ambiguously benign injected requests can survive sanitization without sufficient context or policies. [A: pp. 5–6, 15]

## Additional evidence-based analyst observations [D]

The work does not provide a controlled standalone-LLM versus web-agent comparison. It also lacks a separate firewall compromise evaluation, adaptive-attack study, latency/cost measurement, firewall-model specification, repetition counts, and definitions of ± terms. These are reporting or scope limitations observed from the supplied document, not necessarily limitations explicitly listed by the authors.

Model-specific utility costs, nonzero residuals, mixed original/fixed comparisons, undefined average aggregation, unsupported probability independence, and example inconsistencies weaken some broad interpretations. Exact tables are more informative than headline prose. The supplied prompts rely on correct contextual judgment, yet no guarantee or measured error taxonomy for that judgment is presented.

# 17. Threats to validity

The following categories are analyst-applied [D]; the authors do not organize all their discussion under these labels.

**Internal validity:** Forced ASB tool insertion changes execution independently of the agent's acceptance of an injected instruction. AgentDojo content replacement makes some tasks impossible independently of defense failure. Table 2's apparent baseline switch further complicates attributing score changes to one correction.

**Construct validity:** Tool invocation is an imperfect proxy for harmful behavior, and tool-set coverage is an imperfect proxy for meaningful task completion. Exact inbox-count changes are an imperfect proxy for communicating the requested content. The paper's benchmark critique is strongest in this area.

**Statistical conclusion validity:** Unspecified ± terms, run counts, aggregation rules, and significance tests prevent assessment of uncertainty in derived differences. Small displayed means cannot be interpreted as formal statistical bounds on future attack probability.

**External validity and generalizability:** Tested tool_knowledge attacks, ASB attacks, predetermined InjecAgent calls, and augmented Tau-Bench tasks do not establish results for all websites, agent architectures, permissions, or adaptive attackers. The paper itself calls for stronger and more dynamic attacks.

**Ecological validity:** Hardcoded responses, forced workflow manipulation, deleted bills, and absent user policies differ from the intended real-task semantics. The fixes address some of these problems, but the supplied evaluation does not show a broad deployment study.

**Reproducibility:** Prompts and extensive tables help reconstruct the conceptual experiment. Missing model settings, firewall identity, code artifacts, seeds, counts, and metric details prevent full reproduction from the supplied paper alone. No independent reproduction is claimed here.

# 18. Future work and open questions

## A. Future work explicitly proposed by the authors

Develop richer, more dynamic benchmarks and stronger, adaptive attack strategies. Avoid forcibly changing agent planning. Preserve task-critical information when inserting attacks. Measure semantic task completion, including sequencing, input–output flow, and partial success. Provide BU, UA, and ASR together. Make benchmark tasks and policies better resemble real user contexts. [A: pp. 6, 15]

## B. Additional open questions — analyst interpretation [D]

How do the same underlying models behave with and without external retrieval and action tools under matched attacks? How much added vulnerability comes from exposure to untrusted content versus broader permissions? What utility/security trade-off remains when attacker tools are genuinely harmful and success is evaluated semantically? How robust is the Sanitizer to attacks targeting its own contextual judgment? What are its operational latency and cost? Can deployment-specific policies reduce ambiguous residual attacks without removing legitimate information?

These questions logically follow from the paper's scope and reporting gaps. They are not author-proposed experiments already completed, and this closed-document analysis does not supply outside answers.

# 19. Terminology and notation glossary

| Term | Beginner-friendly meaning within this paper |
|---|---|
| LLM | Large language model; the component that interprets language and proposes calls. |
| Tool-calling agent | An LLM-based system that uses external operations and their results. |
| IPI | Indirect prompt injection; attacker instructions carried inside retrieved/tool-returned content. |
| Direct attack/jailbreak | An adversarial prompt delivered directly rather than embedded in tool output. |
| PII | Personally identifiable information; sensitive personal data considered for redaction. |
| API | Application programming interface; an external operation an agent can invoke. |
| Minimizer / F_in | Tool-Input Firewall that reduces outgoing arguments to necessary information. |
| Sanitizer / F_out | Tool-Output Firewall that removes suspected malicious incoming content. |
| BU | Benign utility: legitimate success without attacks. |
| UA | Utility under attack: legitimate success with injected content present. |
| ASR | Attack success rate: attacker-goal success. |
| ASB | Agent Security Bench. |
| DH / DS | Direct harm / data stealing, InjecAgent attack categories. |
| PI Detector | Prompt-injection classifier used as a baseline. |
| Spotlighting | Marking external tool text with delimiters to distinguish it from instructions. |
| Prompt sandwich | Repeating the legitimate task around or near external content. |
| tool_knowledge | AgentDojo attack setting with partial user and tool knowledge. |
| Context-ignoring attack | Injection asking the agent to disregard prior instructions. |
| Combined attack | ASB composition of multiple attack styles. |
| Static / dynamic planning | Calls chosen in advance / calls chosen using previous outputs. |
| T, T_m, M | Tool set, individual tool, number of tools. |
| X_m, Y_m | Tool arguments and tool outputs. |
| n_m, p_m | Number of argument and output components for a tool. |
| μ, μ* | Legitimate user task and malicious attacker task. |
| π_μ, π_μ|I | Plan without attack and plan in attack I. |
| S(μ;π) | Binary success indicator for a task under a plan. |
| E | Expectation or average over the indicated task distribution. |
| X̃, Ỹ | Minimized arguments and sanitized outputs. |
| Safe sets | Intended acceptable inputs/outputs; not formally characterized here. |
| argmin | Select the plan minimizing the displayed objective. |
| State delta | Change in environment state, such as number of messages added. |
| Semantic goal completion | Checking that the intended task outcome occurred, not just a rigid counter change. |
| ± | Reported uncertainty/variation notation whose statistical meaning is unspecified. |

# 20. Key numerical results

Values below are exact reported entries unless explicitly marked derived or approximate. Rates and utilities use the paper's percentage-scale reporting; ± meanings remain unspecified.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| AgentDojo security evaluations | 949 | evaluations | Four suites; task×attack count definition | Author-reported | p. 11, C.1 |
| ASB security evaluations | 400 | evaluations | Two-stage setting | Author-reported | p. 12, C.1 |
| AgentDojo no-defense ASR | 34.32±2.49 | % | Fixed GPT-4o, tool_knowledge | Visually readable | p. 14, T5 |
| AgentDojo Sanitizer ASR | 0.01±0.03 | % | Same condition | Visually readable | p. 14, T5 |
| AgentDojo combined ASR | 0.00±0.00 | % | Same condition | Visually readable | p. 14, T5 |
| AgentDojo Sanitizer residual | 2.54±0.55 | % | Fixed Qwen3 8b, Slack | Visually readable | p. 14, T5 |
| AgentDojo no-defense UA | 72.19±2.79 | % | Fixed GPT-4o | Visually readable | p. 15, T6 |
| AgentDojo Sanitizer UA | 72.59±1.71 | % | Fixed GPT-4o | Visually readable | p. 15, T6 |
| AgentDojo combined UA | 66.52±1.77 | % | Fixed GPT-4o | Visually readable | p. 15, T6 |
| GPT-4o clean BU | 81.97±5.31 versus 67.10±7.52 | % | Fixed AgentDojo, none versus Sanitizer | Visually readable | p. 13, T4 |
| Llama UA | 57.92±2.04 versus 48.67±2.03 | % | Fixed AgentDojo, none versus Sanitizer | Visually readable | p. 15, T6 |
| Qwen3 32b UA | 47.60±1.56 versus 62.98±1.02 | % | Fixed AgentDojo, none versus Sanitizer | Visually readable | p. 15, T6 |
| AgentDojo correction | 60.87±2.59 → 72.19±2.79 | % | GPT-4o no-defense UA, original→fixed | Visually readable | p. 6, T3 |
| Correction absolute increase | 11.32 | percentage points | 72.19−60.87 | Analyst-derived | T3 operands |
| Correction relative increase | approximately 18.60 | % relative | (72.19−60.87)/60.87×100 | Analyst-derived | T3 operands |
| ASB Sanitizer ASR | 2.33±0.88 / 2.58±1.26 | % | Fixed GPT-4o context-ignoring / combined | Visually readable | pp. 20–21, T14–T15 |
| ASB Llama Sanitizer ASR | 7.00±2.83 / 7.25±0.35 | % | Fixed context-ignoring / combined | Visually readable | pp. 20–21, T14–T15 |
| ASB Qwen3 8B Sanitizer ASR | 5.17±0.63 / 3.00±0.66 | % | Fixed context-ignoring / combined | Visually readable | pp. 20–21, T14–T15 |
| InjecAgent GPT-4o average | 0.3±0.0 / 0.0±0.0 | % | Sanitizer base / enhanced | Visually readable | p. 21, T16 |
| InjecAgent Llama average | 3.0±0.1 / 1.1±0.1 | % | Sanitizer base / enhanced | Visually readable | p. 21, T16 |
| InjecAgent Qwen3 32B average | 0.5±0.1 / 0.1±0.1 | % | Sanitizer base / enhanced | Visually readable | p. 21, T16 |
| InjecAgent Qwen3 8B average | 0.3±0.1 / 0.3±0.2 | % | Sanitizer base / enhanced | Visually readable | p. 21, T16 |
| Tau-Bench Sanitizer ASR | 0 | % | Added data-stealing attacks | Author-reported | pp. 4–5 |
| Tau-Bench Sanitizer UA | approximately 60–62 | % | Model-averaged plotted point | Approximate visual estimate | p. 4, F2c |

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| External content can redirect tool agents | Introduction and tool-output threat model; worked exfiltration examples | EX1–EX2 | pp. 1–3, 16–24 | Strong source support for described mechanism; no standalone comparator. |
| Two interface firewalls implement the method | Pipeline, transformations, supplied prompts | F1, EQ2–EQ3, Appendix D | pp. 2–3, 12–13 | Strong architectural support; implementation settings incomplete. |
| Sanitizer sharply reduces AgentDojo attack success | Fixed model-specific ASR rows | T5, X1 | p. 14 | Strong numerical support; nonzero residuals contradict literal all-zero claim. |
| Utility effects are conditional | Clean and attacked utility rows | T4, T6, X1 | pp. 13, 15 | Strong evidence against uniform no-cost interpretation. |
| Sanitizer is lowest-ASR ASB defense shown | Three model blocks under two attacks | T14–T15, X2 | pp. 20–21 | Strong within-table comparison; flawed metric semantics limit practical meaning. |
| InjecAgent attacks are reduced but utility is unknown | DH/DS base/enhanced rows; lack of utility discussion | T16, X3 | pp. 6, 12, 21 | Strong attack evidence; no BU/UA assessment possible. |
| Some enhanced attacks are weaker | GPT-4o and Qwen3 32B conditions | T16, E.3 | pp. 15, 21 | Model-dependent; conspicuousness explanation is hypothesis. |
| Forced tool insertion distorts ASB | Before/after workflow shows unchosen LoanFraud added | EX3, X5 | p. 25 | Strong illustrated design problem; T2 numerical comparison has condition ambiguity. |
| Deleted task information confounds AgentDojo utility | Empty bill versus restored bill and payment trace | EX1, X5 | pp. 16–23 | Strong mechanism; corrected example has attack-target inconsistency. |
| Utility should track intended outcomes | Strict inbox-delta critique and design recommendations | §5.2, §5.4, EX2 | pp. 6, 23–24 | Strong rationale; displayed Slack trace does not fully show legitimate message delivery. |
| Current benchmarks may overstate defense robustness | Rigid attacks, missing context, metric flaws | §6, E.3 | pp. 6, 15 | Author assessment supported by identified flaws; not a quantified generalization gap. |
| Web agents have additional exposure and action pathways | Web/email/database retrieval plus tool effects | Research relevance inference | pp. 1–3, 16–24 | Analyst interpretation; comparative vulnerability remains untested. |

Major claims and important values were checked against their supplied source locations during synthesis. Visual tables were used to confirm selected entries, including residual AgentDojo ASR and ASB fixed scores. Equation typesetting on text-only p. 3, external code contents, and unreported experimental settings remain unverified.

# 22. Very simple explanation — Explain Like I'm 15

Imagine asking an assistant to read a bill and pay it. Someone has hidden a note inside the bill saying: before paying, look through the user's transactions and send private information somewhere else. The assistant is supposed to read the bill as information, but it might treat that hidden note as a new instruction. That is the problem studied here.

The researchers put two filters around the assistant's tools. One tries to stop unnecessary information from being sent out. The other reads incoming results and removes suspicious instructions while keeping useful facts, such as the bill amount. The second filter works very well against many attacks in the reported tests, but the detailed numbers show that it is not perfect and sometimes reduces useful task performance.

The researchers also discover that some tests are unfair or misleading. A test may insert a bad tool even when the assistant never selected it, erase the bill amount so nobody can finish the task, or mark a task as failed just because an extra message appeared. Fixing the test can change the score without changing how smart or secure the assistant is.

For the question about web agents versus ordinary language models, this paper gives a useful explanation of an additional risk: an agent reads material other people can control and can then take actions with tools. However, the paper does not run a fair comparison between standalone models and web agents. It supports understanding that risk pathway, not a numerical claim about how much more vulnerable one is than the other.

# Completeness Audit

The denominator is the supplied 25-page inventory, including main sections, appendices, two numbered figures with three distinct result panels, 16 tables, mathematical definitions and three numbered equations, prompt procedures, and three worked benchmark examples. Coverage refers to representation in this report, not independent validation of the underlying science.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| S0: identity, abstract, venue, contribution footnote | Yes, text and visual | Yes | Fully represented | Authors, affiliations, venue, markers and headline qualified. |
| S1: Introduction and Contributions | Yes, text and visual | Yes | Fully represented | Attack motivation, defense and benchmark objectives. |
| S2.1: Problem setup and threat model | Yes, text; p. 2 visual | Yes | Fully represented | Page 3 equation layout not visually checked. |
| S2.2: Firewalls | Yes, text-only p. 3 | Yes | Fully represented | Transformations, static/dynamic cases, optional inputs. |
| S3: Experimental setup and metrics | Yes, text; p. 4 visual | Yes | Fully represented | Definitions and differing benchmark semantics retained. |
| S4: AgentDojo results | Yes, text and visual | Yes | Fully represented | Main claims checked against appendix residuals. |
| S4: ASB results | Yes, text and visual | Yes | Fully represented | Residuals, utility and artifact explanation included. |
| S4: InjecAgent results | Yes, text and visual | Yes | Fully represented | Base/enhanced, detector ties and absent utility. |
| S4: Tau-Bench results | Yes, text and visual | Yes | Represented in compressed form | Exact unreported values remain unavailable. |
| S5.1: ASB limitations | Yes, text and visual | Yes | Fully represented | Forced tools, hardcoded outputs, sequencing and scoring. |
| S5.2: AgentDojo limitations | Yes, text and visual | Yes | Fully represented | Content deletion and brittle utility. |
| S5.3: InjecAgent limitations | Yes, text and visual | Yes | Fully represented | Missing BU and UA. |
| S5.4: Future benchmark guidelines | Yes, text and visual | Yes | Fully represented | All four guideline categories retained. |
| S6: Discussion and Conclusion | Yes, text and visual | Yes | Fully represented | Claims bounded by detailed results. |
| O1–O4: objectives | Yes | Yes | Fully represented | No formal author research questions invented. |
| H1: enhanced-attack hypothesis | Yes | Yes | Fully represented | Explicitly separated from causal proof. |
| X1–X5: experiments/analyses | Yes | Yes | Fully represented | Distinct benchmarks and correction analysis separated. |
| F1: pipeline | Yes, visually | Yes | Fully represented | Components, flow, preserved data, filename discrepancy. |
| F2a: AgentDojo panel | Yes, visually | Yes | Fully represented | Approximate plot reading separated from exact tables. |
| F2b: ASB panel | Yes, visually | Yes | Fully represented | Nonzero point and aggregation uncertainty. |
| F2c: Tau-Bench panel | Yes, visually | Yes | Fully represented | Approximate coordinates and absent exact tables. |
| T1 | Yes, text and visual | Yes | Fully represented | All displayed entries retained. |
| T2 | Yes, text and visual | Yes | Fully represented | All entries and condition mismatch retained. |
| T3 | Yes, text and visual | Yes | Fully represented | Both entries and derived differences. |
| T4–T6 | Yes, text and visual | Yes | Represented in compressed form | Overall values, important suite exceptions, rankings and utility trade-offs retained. |
| T7–T9 | Yes, text and visual | Yes | Represented in compressed form | Original benchmark overall results and comparison role retained. |
| T10–T15 | Yes, text and visual | Yes | Represented in compressed form | Model-specific main comparisons, ties and benchmark qualifications retained. |
| T16 | Yes, text and visual | Yes | Represented in compressed form | Model/settings/category results, detector exceptions and average discrepancies retained. |
| EQ0: definitions and probability factorization | Yes, supplied text | Yes | Fully represented | Independence assertion explicitly questioned; typography limitation retained. |
| EQ1–EQ3 | Yes, text-only p. 3 | Yes | Fully represented | Forms, symbols, purpose and missing formal guarantees explained. |
| Appendix D prompt procedures | Yes, text; ending visual | Yes | Fully represented | Inputs, output schemas and instructions explained as evidence. |
| Numbered algorithms/pseudocode/theorems | None identified | Not applicable | No such item identified | Prompts are procedures, not mislabeled numbered algorithms. |
| Major contributions | Yes | Yes | Fully represented | Architecture, empirical and benchmark contributions distinguished. |
| Author-stated limitations | Yes | Yes | Fully represented | Kept separate from analyst observations. |
| Appendix A Related Works | Yes, text-only | Yes | Represented in compressed form | Repetition and naming inconsistency disclosed. |
| Appendix B Baselines | Yes, text-only | Yes | Fully represented | Three described baseline families. |
| Appendix C and C.1 | Yes, text-only | Yes | Fully represented | Sizes, attack choices and absent settings. |
| Appendix E.1–E.3 | Yes, text and visual | Yes | Represented in compressed form | All tables and substantive discussion covered. |
| Appendix F.1.1 / EX1 | Yes, text; partial visual | Yes | Represented in compressed form | Long transaction histories shortened; missing/restored bill and leak retained. |
| Appendix F.1.2 / EX2 | Yes, text-only pp. 23–24 | Yes | Fully represented | Utility rationale and incomplete legitimate-delivery evidence. |
| Appendix F.2.1 / EX3 | Yes, text and visual p. 25 | Yes | Fully represented | Before/after selected tool sets explained. |
| References [1]–[27] | Yes, supplied text; p. 8 visual | Yes, as context | Inspected but deliberately omitted as repetitive/non-substantive | Bibliographic entries not individually reproduced or externally verified. |
| Appendix contents page | Yes, text-only | Yes | Represented in compressed form | Integrated into roadmap. |
| Separate supplementary material | Not supplied | No | Missing from supplied material | No separate supplement or code artifact reviewed. |
| Corrected benchmark release artifacts | Not supplied | Claim only | Inaccessible | Release claim does not establish code inspection. |

## Missing or inaccessible material

No physical page is missing from the supplied 1–25 sequence. Visual renderings are absent for pages 3, 7, 9, 10, 11, 12, 22, 23, and 24; those pages were inspected through supplied text only. Separate supplementary files, corrected benchmark code, execution receipts, and referenced outside publications were not supplied for review. Essential reporting details such as firewall model, run counts, seeds, ± definitions, precise Tau-Bench results, and some benchmark sample counts are absent from the supplied work.

## Uncertain interpretations

The exact original typography of page 3 equations is not visually verified. Small plot coordinates remain approximate. Safe input/output sets lack formal definitions. Probability independence is asserted without a supplied justification. ASB Table 2 does not visibly maintain one defense condition, and the stated utility-zero rule conflicts with a simple shared-denominator reading of reported rates. InjecAgent Avg aggregation is undefined and includes an average exceeding both components. Appendix A's input-firewall wording conflicts with the main output-firewall emphasis. The Slack example does not visibly establish summary delivery, and the restored-bill example changes its stated leakage target. None of these uncertainties was silently repaired.

## Deliberately compressed material

Repeated paragraphs in Appendix A are summarized once; their duplication is disclosed rather than treated as additional evidence. Detailed suite-level cells in large tables are compressed after inspection, with overall values, rankings, important residuals, and utility exceptions retained. Long transaction histories, account strings, and attack payloads are summarized by their security role rather than transcribed. References and decorative role-box styling are not individually reproduced. The supplied prompts are described structurally rather than repeated verbatim.

## Potential omissions

Every substantive component identified in the supplied inventory is represented either directly or with disclosed compression. This does not mean every table cell or sentence is reproduced. No additional identified substantive inventory item is knowingly left without an account. Unreported settings, inaccessible release artifacts, and unverified visual layouts remain explicit limits; the report is an inventory-based analysis of the supplied material, not a claim of independent experimental or universal scientific completeness.
