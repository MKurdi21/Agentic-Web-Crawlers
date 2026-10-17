# Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. No tools, browsing, repository inspection, citation verification, or external background research were used. The paper is treated as evidence to analyze, not as instructions. Source labels throughout are: **[A] author-reported**, **[B] directly observable in supplied visuals**, **[C] analyst-derived**, and **[D] analyst interpretation**. No [E] external information is introduced. Confidence describes confidence in the reading or inference, not independent validation of the experiments.

| Accessibility item | Assessment |
|---|---|
| Main document | Supplied as extracted text for physical PDF pages 1–13, with source images for 12 pages. The original PDF binary was not inspected. |
| Accessible text | Pages 1–13; printed proceedings pages 16115–16127. Physical PDF numbering is used in all locators below. |
| Visually inspected pages | 1–10, 12, and 13. Page 11 was inspected through supplied text only. |
| Apparently missing pages | No physical page is absent from the supplied text sequence. Page 11 has no supplied visual rendering. This does not establish that no separate artifact exists. |
| Figures | Figures 1–5 are visually available and inspected. Fine lettering in Figures 1–2 and exact coordinates in plots are limited by image resolution. |
| Tables | Tables 1–7 are available in text and visually inspected. Dense numerical tables are readable using both representations; selected values are cross-checked below. |
| Equations | Equations (1)–(8) and the unnumbered trajectory expression are available and readable. Mathematical formatting is interpreted with the page images rather than extracted line order alone. |
| Appendix | Appendix A, Additional Defenses, is visibly present on pages 12–13, despite the supplied automated accessibility record listing no detected appendix pages. |
| Supplementary material | No separate supplementary file, dataset, code snapshot, configuration file, or execution log was supplied. |
| Referenced artifacts | Page 1 supplies a GitHub code URL; page 9 promises code/dataset release and benchmark updates. These artifacts were not accessed. |
| OCR | No OCR was performed or needed for the available main text. Supplied extraction was an aid, not independent confirmation of the visuals. |
| Important limitation | The paper describes trajectory logging, but supplies no concrete logged attack trajectory or stepwise persistence table. Reproducibility details and several quantitative definitions remain unspecified. |

**Document type:** mixed cybersecurity, AI systems, framework, benchmark, and empirical evaluation paper. It is not a systematic review, mathematical proof paper, or controlled standalone-model-versus-agent comparison.

## Inventory established before synthesis

**Title:** BackdoorAgent: A Unified Framework for Backdoor Attacks on LLM-based Agents. **Authors:** Yunhao Feng, Yige Li, Yutao Wu, Yingshui Tan, Yanming Guo, Yifan Ding, Kun Zhai, Xingjun Ma, and Yu-Gang Jiang. Page 1 marks Feng and Li as equal contributors and Ma as corresponding author. Affiliations span Fudan University, Shanghai Innovation Institute, Singapore Management University, Alibaba Group, Deakin University, and Hunan Institute of Advanced Technology. **Venue as supplied:** Findings of the Association for Computational Linguistics: ACL 2026, pages 16115–16127, July 2–7, 2026. No separate keywords are shown.

| Inventory IDs | Original objects | Locations |
|---|---|---|
| ABS, S1 | Abstract; §1 Introduction and three contribution bullets | pp. 1–2 |
| S2a, S2b | §2 Related Work: LLM-based Agents; Backdoor Attacks on Agentic Systems | pp. 2–3 |
| S3, SS3.1, SS3.2 | §3 Preliminaries; Agent Formulation; Backdoor Attacks in Agent Workflows | pp. 3–4 |
| S4, SS4.1–SS4.3 | §4 Framework; Stage-aware Framework; Backdoor Injection; Representative Tasks | pp. 4–5 |
| S5, SS5.1 | §5 Experiments; Experimental Setup, including systems, attacks, and metrics | pp. 5–6 |
| SS5.2a–SS5.2d | Results: accuracy/attack coexistence; channel patterns; model performance/robustness; sequential amplification | pp. 6–8 |
| SS5.3a–SS5.3c | Family aggregation; poisoning-ratio analysis; efficiency analysis | p. 8 |
| SS5.4 | Exploring Potential Defenses | pp. 8–9 |
| S6, LIM, ACK, REF | Conclusion; Limitations; Acknowledgments; References | pp. 9–12 |
| APP_A | Appendix A Additional Defenses | pp. 12–13 |
| F1–F5 | Propagation concept; framework; token overhead; token probabilities; ROC | pp. 1, 4, 8, 9, 13 |
| T1–T7 | Taxonomy; closed-source; Web; open-source; advanced models; family ASR; poisoning ratios | pp. 3, 6, 7, 8 |
| E1–E8, E_TRAJ | Eight numbered equations plus structured trajectory expression | pp. 3–5 |
| X1–X7 | Main non-Web evaluation; Web evaluation; advanced models; family aggregation; poisoning ratios; token overhead; defense-signal exploration | pp. 5–13 |
| C1–C3 | Framework novelty; four-application benchmark; propagation/persistence findings | p. 2 |

No formally numbered research questions, hypotheses, algorithms, pseudocode blocks, theorems, lemmas, or proofs are supplied. The references are contextual evidence about what the authors cite; their underlying works were not reviewed.

# 1. Plain-language orientation

[A] This paper studies how a hidden malicious trigger can affect an AI agent that repeatedly plans, retrieves information, uses tools, and incorporates the results into later decisions. An agent is more than a language model producing one answer: it has an ongoing workflow. The authors argue that this workflow creates additional places for malicious information to enter and remain influential. A poisoned retrieved passage, for example, can enter the context used for subsequent planning rather than disappearing after one response. (pp. 1–4.)

[A] The researchers build **BackdoorAgent**, a framework that exposes attack interfaces at three stages—planning, memory, and tools—and records agent execution. They also present a benchmark with question answering, code generation, web interaction, and driving-style sequential control. They evaluate seven named attacks across several model families, investigate memory contamination and token overhead, and explore probability-based detection signals. (pp. 2–9, 12–13.)

[A] Their main empirical message is that attacker-specified behavior can coexist with useful task accuracy, vulnerability varies with the injection channel, and closed-loop control can amplify malicious interference. Memory attacks have the largest family-level average attack success rate in four of five families in Table 6. Driving results contain very high success rates for some planning and tool attacks. Web results are particularly heterogeneous rather than uniformly vulnerable. (Tables 2–7.)

[D] For the research question **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, this paper supplies a plausible workflow-level mechanism and agent benchmark evidence. It does **not** establish that Web agents are quantitatively more vulnerable than standalone language models: there is no matched standalone-model condition. Its central contribution is a way to organize and observe agent backdoors, not an experimentally measured agent-versus-standalone vulnerability multiplier. Confidence: HIGH for this boundary.

# 2. Document roadmap

[A] The abstract and introduction motivate the extra attack surface created by stateful workflows. Related Work groups prior research into agent architectures and attacks on agentic systems, attributing fragmentation to different implementations, threat assumptions, and evaluation protocols. Preliminaries then formalizes how plans, retrieved material, and tool feedback enter future context and state. (pp. 1–4.)

[A] Section 4 maps that model into a framework with component interfaces, attack wrappers, run configurations, and trajectory logging, and defines the four application settings. Section 5 reports the benchmark and several secondary analyses: model/task tables, family averages, memory poisoning ratios, token costs, and exploratory detection. Section 6 summarizes the authors' conclusions; the Limitations paragraph bounds the benchmark's coverage. Appendix A expands the defense discussion and adds a receiver operating characteristic plot. References occupy pages 10–11 and the left portion of page 12. (pp. 4–13.)

[D] The most useful reading path is formal workflow → attack interfaces → metric definitions → task-specific tables → aggregation caveats → defense appendix. This order prevents broad statements about agent vulnerability from obscuring the substantial variation in Table 3 or the reporting inconsistencies discussed below.

# 3. Background and context

[A] A **large language model (LLM)** is the model backbone used by the agent. The paper does not describe its internal training procedure; its focus is the surrounding runtime. **Planning** produces a plan or reasoning artifact. **Memory** retrieves stored material, including from a **retrieval-augmented generation (RAG)** store. **Tools** execute actions and return feedback. **Context** is information visible to the backbone; **internal state** includes structured or non-textual information such as indices and metadata. (p. 3, §3.1.)

[A] An **intermediate artifact** is a plan, retrieved passage, or tool result generated during execution. **Persistence** means such information remains available in later context or state. **Cross-stage propagation** means a perturbation introduced at one interface can influence other stages later. A **trajectory** is the ordered execution history rather than only the final answer. A **closed loop** repeatedly uses feedback from prior actions to make subsequent decisions. (pp. 2–5, 7–8.)

[A] A **backdoor** is described as hidden malicious behavior that stays dormant during normal execution and activates when a trigger is present. The paper places triggers in stage outputs or their generating channels. This is broader than a description restricted to changing model weights: the runtime can return poisoned retrieval content or manipulated feedback. (pp. 3–5.)

[D] A beginner-friendly illustration: if an agent repeatedly consults a contaminated note, that note can affect its next plan and action even if the underlying language model has not changed. This illustrates the paper's model; it is not an additional experiment or a claim about a particular supplied attack instance.

[A] The authors position earlier studies as frequently single-step, single-module, or otherwise isolated. Their asserted gap concerns unified analysis of temporal propagation across integrated workflows. The cited literature is not independently assessed here. (pp. 2–3.)

# 4. Research problem and gap

| Element | Source-grounded account |
|---|---|
| Existing problem [A] | Stateful agents can be affected through poisoned memories, planning traces, or environmental observations, beyond the backbone model itself. pp. 1–2. |
| Attributed prior shortcomings [A] | Different implementations, threat assumptions, and evaluation protocols limit comparison and conceal interactions between components. pp. 2–3. |
| Research gap [A] | How a trigger introduced at one stage persists and propagates across an integrated workflow is insufficiently understood from an agent-centric perspective. pp. 1–2. |
| Motivation [A] | Reused plans, retrieved documents, and tool outputs create dependencies across steps; final task accuracy may not reveal behavioral compromise. pp. 2, 6. |
| Scope [A] | Three injection channels, seven attacks, four application types, multiple open/closed model backbones, and preliminary probability-signal analysis. pp. 3, 5–9. |
| Scope boundary [D] | The experiments do not isolate every architectural feature, cover all security attacks, or measure a controlled standalone-versus-agent difference. |

[D] The supplied work is especially relevant to web-agent security because web interaction combines perception, action, and feedback. However, the paper's strongest numerical results are not confined to Web, and driving-style amplification cannot automatically be transferred to browsing or purchasing tasks.

# 5. Research questions / objectives / hypotheses

**Explicit formal research questions:** none are numbered or stated as formal questions. **Explicit statistical hypotheses:** none are provided. The paper instead presents objectives and contribution claims.

[A] Its objectives are to: (1) structure agent backdoor entry points by planning, memory, and tools; (2) instrument execution to examine injection, activation, and propagation; (3) standardize evaluation across four representative applications; (4) characterize attack effectiveness and task accuracy across backbones; (5) examine channel aggregation, memory contamination intensity, token consumption, and transfer of probability-based defense signals. (pp. 1–2, 4–9, 12.)

[D] The user's research question is an analytical lens external to the paper's formal organization, not an author-stated hypothesis. The relevant subquestions are whether additional interfaces create attack opportunities, whether reused state sustains malicious influence, whether interaction amplifies it, and whether familiar output-level signals remain sufficient. The paper addresses these unevenly: it defines all four mechanisms, gives benchmark associations, and provides a preliminary detector analysis, but does not directly estimate the incremental vulnerability caused by adding agency to an otherwise identical model.

# 6. Assumptions / threat model

[A] The system receives query q and evolves over discrete steps. It maintains context x_t and state s_t, with planning P, memory M, and tool T functions producing p_t, m_t, and o_t. These artifacts are written into later context/state. The formal description calls the runtime a deterministic composition. No detailed treatment of sampling randomness accompanies that description. (p. 3.)

[A] The attacker can introduce a trigger-bearing perturbation into one stage output at a selected step, or into the corresponding generating channel. Equation (8) replaces one component with an attacked version while leaving the others unchanged. The attack goal G is named, but is not developed into a common mathematical optimization objective. The framework does not require a fixed execution order or exactly one retrieval/tool invocation per step. (pp. 4–5.)

[A] Table 1 assigns access categories: BadChain and AdvAgent are black-box; BadAgent, PoisonedRAG, TrojanRAG, AgentPoison, and DemonAgent are white-box. It categorizes persistence and stealthiness qualitatively. The supplied paper does not operationally define the access boundaries, quantify stealthiness, or detail how each named attack obtains its permissions in every application. (p. 3.)

[A] Protected outcomes differ by application: correct QA answers, acceptable code behavior, intended Web task completion, and safe driving control. Described harms include incorrect answers, database deletion, incorrect purchases, and sudden stops. These are task descriptions/examples, not individually enumerated measured events. (p. 5, §4.3.)

[D] The modeling boundary assumes the non-targeted components remain unchanged, but unchanged software can still consume malicious inputs and change its behavior. The paper does not establish a complete trusted computing base, authentication model, permission system, isolation policy, or defense-aware attacker budget. Simultaneous attacks on multiple components are not the core configuration formalized in Equation (8). These are limits of specification, not proof that such protections were absent in an implementation.

# 7. Methodology

## Architecture and execution

[A] BackdoorAgent exposes hook points for plan generation, retrieval calls, and tool execution/return. Component-local wrappers modify computation or outputs at one interface. A run configuration specifies agent template, task instances, and attack variant. Execution continues for a fixed step budget or until termination, recording tuples (x_t, s_t, p_t, m_t, o_t). (pp. 4–5.)

[A] The framework standardizes prompt serialization, tool-call formatting and result validation, and memory retrieval protocols such as indexing, top-k retrieval, reranking, and reinsertion into context. These choices are said to be logged to enable replay. Exact templates, serialization formats, top-k values, reranking methods, configuration examples, and executable replay receipts are not included in the supplied work. (p. 5.)

## Application design

| Application | Intended workflow [A] | Attack objective/examples [A] | Verifier examples [A] |
|---|---|---|---|
| Agent QA | Retrieval-grounded reasoning with persistent memory | Wrong answers with fluent responses | Exact match |
| Agent Code | Iterative program synthesis with execution feedback | Destructive operations such as database deletion while appearing correct | Unit tests |
| Agent Web | Multimodal perception and action on web interfaces | Interface misdirection, such as purchasing wrong items | Task completion |
| Agent Drive | Closed-loop sequential decisions with environmental feedback | Unsafe control, such as sudden stops | Safety constraints |

Sources: p. 5, §§4.3 and 5.1. These task descriptions do not specify dataset names or sizes.

## Models, attacks, and comparison conditions

[A] Table 2 contains Claude, Gemini, GPT, and Qwen commercial/API-style backbones as labeled by the authors, across Code, QA, and Drive. Table 4 contains DeepSeek, Kimi, and Qwen models labeled open-source. Table 5 adds GPT-5.2, GPT-4o, and Gemini Pro variants. Table 3 restricts Web to multimodal-capable backbones: Claude Sonnet 4.5, Gemini 3 Flash, GPT-4o-mini, and Qwen3-VL-235B. Model identifiers are reported labels, not independently verified specifications. (pp. 6–7.)

[A] Seven attacks are grouped into planning (BadChain, BadAgent), memory (PoisonedRAG, TrojanRAG, AgentPoison), and tools/environment (AdvAgent, DemonAgent). BadAgent appears in Table 4 but not Tables 2, 3, or 5. Thus the reported attack grid is not fully balanced across tables. The paper says identical task instances and step budgets are used across backbones, but does not supply their numerical sizes/budgets. (pp. 5–7.)

## Metrics and statistics

[A] **Clean ACC** is benign-agent task success without trigger injection. **Attack success rate (ASR)** is the percentage of triggered instances exhibiting attacker-specified behavior. **ACC under attack** measures ordinary task success on those triggered executions with the same task verifier. ASR and ACC are distinct outcomes, not complements. Their sum need not be 100. (pp. 5–6.)

[A] The supplied material gives no named dataset, instance count, train/validation/test split, annotation protocol, demographic/sample distribution, leakage control, exclusion rule, seed list, repetition count, uncertainty interval, significance test, hardware configuration, package version, latency measurement, or monetary cost. It also lacks exact trigger strings, per-attack optimization settings, and detailed attack-success checking rules. These omissions limit independent reproduction and statistical interpretation; they should not be filled from the cited works.

# 8. Experiments / analyses

| ID | Purpose and setup | Measurements and objects | Results and caveats |
|---|---|---|---|
| X1 | Compare attacks across Code, QA, Drive using closed-source and open-source model groups; same task instances/step budgets asserted | Clean ACC, attack ASR, attacked ACC; T2 and T4 | Strong task/channel/model variation; no sample sizes or error bars. |
| X2 | Evaluate multimodal Agent Web separately | Four backbones, six attack columns, Clean ACC/ASR/ACC; T3 | Some near-total attack successes coexist with many zeros or low ASRs. No standalone Web baseline. |
| X3 | Examine additional backbones labeled more advanced | Code, QA, Drive; same six attack columns as T2; T5 | High clean accuracy does not guarantee low ASR; some attacked QA accuracies decrease substantially. |
| X4 | Aggregate vulnerability by family and channel | Average ASR from T2/T4; T6 | Memory highest in four of five families; aggregation formula/weighting not explicit and some averages are difficult to reproduce directly. |
| X5 | Vary external-memory poisoning ratio | Ratios 0.1, 0.2, 0.5; four model families; T7 | Every reported family rises monotonically; exact contamination sampling protocol unspecified. |
| X6 | Assess computational overhead with increasing trigger strength | Full-trajectory token use; GPT-4o; F3 | Memory overhead rises most, planning least; strength units and normalization denominator not specified precisely. |
| X7a | Inspect target/non-target output-token probabilities | Drive, QA, Code; F4 | Small visual mean gaps; token definitions, counts, and uncertainty absent. |
| X7b | Examine probability-inspired detection against a reference model | Aggregated ROC; APP_A/F5 | AUROC label 0.7681; target/reference identities, score construction, thresholds, and counts unspecified. |

[A] These are distinct analyses, not independent replications. Family aggregation summarizes the main tables; it does not introduce a separate experimental population. The defense appendix extends the probability-signal investigation rather than demonstrating a deployed prevention system.

[D] There is no supplied experiment that holds the model and malicious input fixed while removing memory, eliminating feedback, or switching between standalone and agent modes. Consequently, the proposed propagation mechanism is not isolated by a causal architecture ablation.

# 9. Results

## Accuracy can conceal behavioral compromise, but preservation is conditional

[A] Table 2 reports Code/GPT-4o-mini under AgentPoison at **98.01% ASR**, **56.74% attacked ACC**, and **58.95% clean ACC**. This supports coexistence of high malicious success with task accuracy near the clean value for that configuration. [C] The accuracy difference is 56.74 − 58.95 = **−2.21 percentage points**. It is not a relative percentage improvement. (p. 6.)

[A] Table 5 reports Code/GPT-5.2 under TrojanRAG at **85.94% ASR**, **88.27% attacked ACC**, and **84.73% clean ACC**. [C] The attacked score exceeds clean by **3.54 percentage points**, calculated as 88.27 − 84.73. No uncertainty estimates establish whether that increase is meaningful beyond the observed scores. (p. 7.)

[A] Accuracy is not always largely preserved. Table 5's QA/GPT-5.2 AgentPoison condition has **55.62% ASR**, **47.96% attacked ACC**, versus **89.37% clean ACC**. [C] This is a **41.41 percentage-point decrease**. Thus the paper's broad accuracy-preservation language must be read as a recurring pattern, not a universal result. (p. 7.)

## Web results are sharply model- and attack-dependent

[A] In Table 3, Claude has **97.39% BadChain ASR** but **0% ASR** for each of the other five reported attacks. Gemini has **98.74% BadChain**, **95.16% PoisonedRAG**, **97.44% TrojanRAG**, **86.67% AgentPoison**, **5.32% AdvAgent**, and **95.40% DemonAgent ASR**. GPT-4o-mini has **0% BadChain ASR** and only **2.53–8.91%** ASR across its other five attacks. Qwen3-VL has **0% BadChain ASR**, with other reported ASRs from **2.31% to 14.35%**. Clean Web ACC ranges from **96.20% to 99.25%**. (p. 6.)

[D] These observations support heterogeneity and selective vulnerability. They do not support a blanket claim that every tested Web agent is easily backdoored or that memory attacks dominate Web specifically. Zero observed success is also not a proof of invulnerability without instance counts and attack-budget details.

## Sequential control shows strong attacks, with exceptions

[A] Table 4's five open-source Drive BadChain ASRs are **92.58, 97.85, 92.15, 97.33, and 96.47%**. This directly supports the text's statement that BadChain exceeds 90 across every open-source Drive backbone tested. Drive AdvAgent ASRs are **80.48, 97.56, 85.71, 87.21, and 75.34%**; the last value limits claims that all such results exceed 80. (p. 7.)

[D] High attack success is consistent with the authors' closed-loop amplification account, but no supplied time-resolved plot measures the accumulation of perturbations or separates feedback amplification from other task/model differences.

## Memory contamination and family results

[A] Table 6 reports GPT-family planning/memory/tools ASR of **43.58/77.97/60.28%**. Memory is also highest for Claude, Gemini, and Qwen; DeepSeek instead has **42.20% tools** versus **38.91% memory**. Table 7 reports GPT-family memory ASR increasing **53.06 → 77.97 → 97.72%** as poisoning ratio increases **0.1 → 0.2 → 0.5**. The same monotonic pattern appears in its other three families. (p. 8.)

[A/D] A crucial metric ambiguity: pages 1–2 call the GPT-family numbers trigger persistence, whereas Table 6 labels them module-wise ASR. The supplied work does not define a separate persistence rate, survival duration, or propagation-count metric. The values should therefore be reported as Table 6 ASRs with this terminology discrepancy disclosed, rather than as independently measured persistence probabilities.

# 10. Figure-by-figure interpretation

## Figure 1 — Conceptual propagation through an agent

[B] Page 1 shows a user and computer next to a circular agent schematic centered on an LLM. Colored regions correspond to planning, tool execution, and memory. Small icons depict reasoning/planning content, external tools, and memory-related stores or records. The composition places these components around a common core rather than depicting a single isolated model response. Fine icon labels are not all confidently readable.

[A] The caption says a trigger introduced in one module can traverse planning, memory, and tools through iterative state updates. This is a conceptual illustration, with no axes, sample size, measured trajectory, error bars, or numerical effect. [D] It communicates the proposed mechanism but does not by itself establish observed cross-stage transmission.

## Figure 2 — BackdoorAgent framework

[B] Page 4 contains three main regions. The left attack suite groups planning attacks, memory attacks, and tool-use attacks. The center shows a unified workflow with Planning, Memory, and Tools connected by large curved arrows; numbered paths and lock/trigger icons indicate injection and propagation routes. A bottom strip depicts framework functions including stage awareness, instrumented runtime, and logging. The right region shows representative tasks and a unified evaluation box with ASR and ACC.

[A] Its caption connects explicit interfaces, configurable execution, injection, and trajectory logging to benchmark tasks and evaluation scripts. [D] The curved arrows communicate repeated cross-component influence, not a measured probability or fixed scheduling guarantee. Section 4.2 explicitly allows flexible invocation order. The visual contains no experimental sample counts or software architecture specification detailed enough to implement the system alone.

## Figure 3 — Token overhead versus trigger strength

[B] Page 8 is a line plot titled Token Overhead under Increasing Trigger Strength (GPT-4o). The horizontal axis is **Trigger Strength**, labeled 1–4; the vertical axis is **Relative Token Overhead**, with visible ticks from 1.0 through 1.8. Planning is a blue line with circular markers, tool use an orange line with square markers, and memory a green line with triangular markers. Axes appear linear. There are no error bars or confidence bands.

[B, approximate visual estimates] All lines start near 1.0. At strength 4, planning is approximately **1.12**, tool use approximately **1.47**, and memory approximately **1.9**. Intermediate memory points are about 1.21 and 1.53 at strengths 2 and 3; these are graphical estimates, not exact table values. The ordering is memory > tools > planning after the initial point, without a visible crossover.

[A] The authors attribute memory's larger token cost to repeated retrieval and reinsertion of content and call planning more token-efficient. The plot concerns token consumption, not wall-clock time, memory footprint, or dollars. Trigger-strength units and the precise relative baseline are not supplied, limiting reproduction and interpretation of the apparent ratios.

## Figure 4 — Target versus non-target token probabilities

[B] Page 9 shows grouped bars for Agent-Driver, Agent-QA, and Agent-Code. Red bars are target tokens; blue bars are non-target tokens. The vertical axis is Average token probability on a linear scale from 0 to 1. The red bar is higher in each displayed group; all bars are near the upper end. There are no error bars, distributions, token counts, or significance annotations.

[B, approximate visual estimates] Target means are roughly **0.95–0.97** and non-target means roughly **0.89–0.92**. Exact means are not printed. The displayed group gaps appear small, roughly several hundredths. [A] The authors describe the differences as small and inconsistent across settings. [D] Figure 4's three aggregated means all have the same direction; it does not visibly establish that a target/non-target sign reversal occurs across these three groups. Unshown within-group variation could be what the prose means, but it is not supplied.

[D] A difference between aggregated means does not itself establish a reliable detector or an instance-level false-positive rate. Figure 5 provides a separate detection-oriented view.

## Figure 5 — Probability-inspired detection ROC

[B] Page 13 shows a **receiver operating characteristic (ROC)** curve titled CleanGen-inspired backdoor detection. The horizontal axis is false positive rate and vertical axis true positive rate; both run from 0 to 1 on linear scales. A blue stepped curve is compared with a dashed diagonal random line. The legend visibly reports **AUROC = 0.7681**. No uncertainty band or operating-point label is shown.

[B] The curve has a noticeable rise around false-positive rates near 0.2 and later reaches the top boundary. Exact threshold coordinates are not labeled and should not be inferred as reported operating points. [A] The caption and Appendix A interpret the separation as weak/limited for direct defense transfer. [D] The curve nevertheless shows substantial above-diagonal signal; whether its utility is adequate depends on tolerable false positives, attack coverage, and uncertainty, none of which is specified. It does not establish that all probability-based defenses fail.

# 11. Table-by-table interpretation

## Table 1 — Stage-oriented taxonomy

[A/B] Rows are seven named attacks; columns are affected stage, access, persistence, stealthiness, and objective. Checkmarks identify one primary stage per attack. BadChain: planning, black-box, short-term, low stealthiness, hijack. BadAgent: planning, white-box, short-term, low, disruption. PoisonedRAG: memory, white-box, long-term, medium, hijack. TrojanRAG: memory, white-box, long-term, medium, control. AgentPoison: memory, white-box, long-term, high, control. DemonAgent: tools, white-box, session-persistent, high, control. AdvAgent: tools, black-box, short-term, high, disruption. (p. 3.)

[D] This is a qualitative taxonomy, not a measured ranking. No operational scale or uncertainty is supplied for stealthiness/persistence labels. It should guide grouping without turning all attacks into equivalent attacker capabilities.

## Table 2 — Closed-source-labeled backbones

[A/B] Fifteen rows cover five model labels × three tasks. Each has Clean ACC and paired ASR/ACC for BadChain, PoisonedRAG, TrojanRAG, AgentPoison, AdvAgent, and DemonAgent. Values are percentage-based task/attack rates; BadAgent is absent. Within Code, the largest displayed ASR is **98.01** for GPT-4o-mini/AgentPoison; within QA it is **95.76** for GPT-4o-mini/AdvAgent; within Drive it is **97.38** for Qwen3-Max/AdvAgent. These are descriptive maxima within each task block, not statistically significant winners. (p. 6.)

[A/B] Claude often has low ASR for some attacks but not universal resistance: its Code memory ASRs are **80.05, 80.31, 86.52**. DemonAgent is low in several Code/QA rows but rises in some Drive rows, such as GPT-5-mini **82.93** and Qwen3-Max **85.31**. This task dependence is less visible in a single overall family mean. No errors or significance tests are given.

## Table 3 — Multimodal Agent Web

[A/B] Four rows compare the six attacks used in Table 2. Every value is observed within a Web-agent setting; there is no standalone model row. Gemini has high ASR for five attacks but low AdvAgent ASR. Claude's five zero ASRs coexist with a high BadChain ASR. The maximum Web ASR is **98.74** for Gemini/BadChain. The minimum is **0**, tied across multiple conditions. (p. 6.)

[A/B] Attacked Web ACC stays high: all displayed attacked accuracies lie between **92.41** and **99.88**. The low bound is Gemini/AgentPoison; the high bound is Qwen3-VL/BadChain. These high scores alongside high ASR in selected conditions support the distinction between the two metrics. However, unspecified verifier logic prevents determining exactly why wrong purchases and successful completion can be counted together in an individual instance.

## Table 4 — Open-source-labeled backbones

[A/B] Fifteen rows cover DeepSeek-R1, DeepSeek-V3.2, Kimi-K2, Qwen2.5-72B-Instruct, and Qwen3-235B-A22B across Code, QA, Drive. This is the only table with all seven attacks. Descriptive maximum ASRs by task block are **88.34** for Code/Qwen2.5/AgentPoison, **93.89** for QA/Qwen2.5/AdvAgent, and **97.85** for Drive/DeepSeek-V3.2/BadChain. (p. 7.)

[A/B] Low clean Code performance for DeepSeek-R1 (**25.43**) coexists with low-to-moderate attack rates, showing that lower ASR cannot automatically be read as better overall utility. BadAgent Drive ASRs are **20.36–27.47**, far below the BadChain Drive values despite both being classified as planning attacks. Category averages conceal this difference. Exact model-size effects cannot be isolated from these heterogeneous labels and configurations.

## Table 5 — Additional backbones

[A/B] Nine rows cover three models × Code, QA, Drive with six attacks. Code clean ACC is **84.73**, **62.47**, and **73.06** for GPT-5.2, GPT-4o, and Gemini Pro, respectively. GPT-5.2 still has TrojanRAG ASR **85.94** in Code and AgentPoison ASR **90.43** in Drive. Gemini Pro QA clean ACC **90.61** coexists with PoisonedRAG ASR **84.19**. (p. 7.)

[D] These values support lack of a simple guarantee from clean accuracy, not a causal claim that increasing model capability worsens robustness. All reported attacked QA ACC values in this table are below their respective clean values, an important qualification to the broad accuracy-preservation narrative.

## Table 6 — Family/channel aggregation

| Family | Planning ASR | Memory ASR | Tools ASR |
|---|---:|---:|---:|
| GPT | 43.58 | 77.97 | 60.28 |
| Claude | 10.43 | 54.82 | 23.07 |
| Gemini | 39.49 | 75.39 | 48.98 |
| Qwen | 35.41 | 55.45 | 54.45 |
| DeepSeek | 27.84 | 38.91 | 42.20 |

[A/B] Source: p. 8. Values are reported ASRs in percent; the caption says aggregation uses Tables 2 and 4. Memory is largest in four rows, with DeepSeek the exception. GPT has the highest reported value in each channel among these five family rows. No dispersion, weights, or statistical comparisons are provided. The abstract's persistence terminology and aggregation reproducibility remain unresolved.

## Table 7 — Memory poisoning ratios

| Family | ASR at 0.1 | ASR at 0.2 | ASR at 0.5 |
|---|---:|---:|---:|
| GPT | 53.06 | 77.97 | 97.72 |
| Gemini | 50.39 | 75.39 | 97.00 |
| Qwen | 33.25 | 55.45 | 86.75 |
| DeepSeek | 21.84 | 38.91 | 70.83 |

[A/B] Source: p. 8. Columns are memory poisoning ratios; outcomes are Memory-channel ASR percentages. All four rows increase monotonically. GPT has the highest reported ASR at each ratio and DeepSeek the lowest; no ties are shown. Claude is absent, with no explanation supplied. The 0.2 values equal the corresponding Table 6 memory values, suggesting a connection to the main configuration, but the paper does not explicitly establish every main-table poisoning setting. No uncertainty, corpus sizes, or contamination selection details are reported.

# 12. Diagram / architecture interpretation

[A/B] Figures 1–2 connect a user query to an LLM-centered workflow. Planning emits an intended plan; retrieval supplies additional content; tools generate actions and feedback. The recurrent update writes these outputs into the material available on later steps. An attack wrapper sits at one interface, so downstream components may remain unmodified while acting on poisoned information. The benchmark layer selects task templates and evaluates both task performance and malicious behavior. (pp. 1, 4–5.)

[D] The security-relevant structure is a feedback path: untrusted stage material becomes input to later decisions. This explains how a one-stage injection could have effects outside its entry stage. It is an architectural account, not evidence that each successful attack traversed all three stages. The paper's formal functions illustrate dependencies in a planning→memory→tools order, but implementation hooks explicitly permit different orders and repeated invocations. A faithful interpretation distinguishes the explanatory recurrence from a mandatory scheduler.

[A] Logging is central because a final answer alone may not reveal where a trigger entered or which decisions changed. Nevertheless, the supplied publication reports aggregate rates rather than a worked replay with a clean/triggered trajectory pair. Thus the framework's intended observability is described more fully than its actual stepwise propagation evidence is presented.

# 13. Equations and mathematical concepts

[A] Symbols: q is the user query; t indexes discrete steps; x_t is observable context; s_t is internal state; P, M, and T are planning, memory, and tool functions; p_t, m_t, and o_t are their artifacts. The symbol T is also used as a final time/trajectory length in sequence bounds, so function-versus-horizon meaning depends on context. τ is a trigger; t* is the injection step; A is the runtime/clean trajectory mapping; A_τ is its triggered counterpart; G is the attack goal. (pp. 3–5.)

| Object | Mathematical form | Meaning, inputs, and role |
|---|---|---|
| Eq. (1), p. 3 | p_t = P(q, x_t, s_t) | Planning maps query/current context/state to a plan or reasoning artifact. |
| Eq. (2), p. 3 | m_t = M(q, x_t, s_t, p_t) | Retrieval returns memory content and may depend on the current plan. |
| Eq. (3), p. 3 | o_t = T(q, x_t, s_t, p_t, m_t) | Tool interaction consumes current information and returns feedback. |
| Eq. (4), p. 3 | x_(t+1) = x_t ∪ {p_t, m_t, o_t} | Intermediate artifacts are retained in next-step visible context. The text describes append behavior; ∪ is not a full serialization or ordering specification. |
| Eq. (5), p. 3 | s_(t+1) = UpdateState(s_t; p_t, m_t, o_t) | Task-specific structured state is updated, such as caches or memory indices. No universal implementation is given. |
| Eq. (6), p. 4 | A(q) → benign behavior; A_τ(q) → backdoor behavior | Desired clean/triggered distinction. The arrows express behavioral outcomes, not a loss function or probability estimate. |
| Eq. (7), p. 4 | (x_(t+1), s_(t+1)) = A(q, x_t, s_t); x_(t+1) = x_t ∪ {p_t, m_t, o_t} | Packages the stage operations and state/context update into a recurrent runtime. A is reused at step-level and whole-trajectory levels. |
| E_TRAJ, p. 5 | 𝒯(q) = {(x_t, s_t, p_t, m_t, o_t)} from t=0 to T−1 | Structured recorded execution, enabling localization of injection/activation effects in principle. |
| Eq. (8), p. 5 | A_τ = (P_τ, M, T) or (P, M_τ, T) or (P, M, T_τ) | One attacked component replaces its clean counterpart; other components remain unchanged. |

[A] The clean trajectory is also described as the sequence {(x_t, s_t)} from t=0 to T. The fuller logged sequence ends at T−1 because it includes step-produced artifacts. This is not necessarily a contradiction, but endpoint semantics are not elaborated.

[D] These equations formalize information flow; they do not prove that every trigger persists, quantify propagation probability, or optimize an attack. No theorem, stability bound, success guarantee, or statistical estimator of persistence is supplied. A retained artifact can be available without necessarily remaining behaviorally effective, so availability and successful malicious control must remain distinct.

# 14. Interpretation and discussion

[A] The authors interpret agent backdoors as workflow-level phenomena involving persistent intermediate artifacts, repeated feedback, and closed-loop amplification. They argue that clean task performance alone is inadequate for security assessment and that defenses should examine trajectories rather than isolated outputs. They also note that accuracy-preserving backdoor behavior is not unique to agents: earlier single-turn studies reportedly observe similar behavior. (pp. 6–9, 12–13.)

[D] The research relevance is therefore mechanism-based: agency creates additional pathways and temporal dependencies that deserve separate evaluation. The supplied experiments support vulnerability of particular agent configurations; they do not rank the total vulnerability of all agents against all standalone models.

## Cross-reference and consistency findings

1. **Persistence versus ASR:** pp. 1–2 call 43.58/77.97/60.28 trigger persistence; p. 8 T6 identifies them as average ASR. No independent persistence definition resolves the difference.
2. **Incorrect accuracy-improvement example:** p. 6 describes Code/Qwen2.5/AgentPoison among examples of matching/exceeding clean accuracy, but its values are 75.89 attacked versus 78.45 clean. [C] 75.89 − 78.45 = −2.56 percentage points. It is a decline.
3. **Misassigned QA accuracy:** p. 6 gives Kimi-K2/AgentPoison ASR 79.83 with ACC 73.77 versus clean 71.25. T4, p. 7, gives AgentPoison ACC **56.39**; **73.77** belongs to AdvAgent ACC in that row. The table and prose disagree; no silent correction is justified.
4. **Channel/example mismatch:** pp. 6–7 discuss PoisonedRAG/TrojanRAG memory effectiveness but illustrate the discussion using QA/Qwen2.5/AdvAgent ASR 93.89. T1 classifies AdvAgent as tools, not memory. The same passage also uses AgentPoison, a memory attack, rather than only the two named methods.
5. **Drive classification ambiguity:** p. 7 places BadChain's high Drive ASR in a discussion of tool/environment domination, while T1 categorizes BadChain as planning. Its numerical result is valid as a planning-attack result; its placement does not change its taxonomy.
6. **Aggregation uncertainty:** T6 says values aggregate T2/T4. [C] For Claude planning, the three T2 BadChain ASRs average (1.04 + 16.53 + 13.72)/3 = **10.43**, matching T6. For Claude tools, the six relevant ASRs average (27.28 + 4.76 + 25.54 + 13.41 + 17.07 + 50.37)/6 = **23.0717**, matching 23.07 after rounding. But Claude memory's nine ASRs sum to **493.39**, giving 493.39/9 = **54.8211**, matching 54.82. Other family averages cannot be assumed to follow an identical transparent subset/weighting: for example Gemini's three BadChain values 41.67, 26.09, 48.54 average **38.7667**, not T6's 39.49. Weighting or inclusion differences are not explained.
7. **Broad wording versus heterogeneity:** memory is highest in four, not all five, T6 families; Web contains many low/zero attack results; advanced-model QA can suffer large accuracy declines. Generalizations need these exceptions.
8. **Defense framing:** Appendix A calls AUROC margin modest and separation limited; F5 reports 0.7681. The numerical result should accompany the qualitative assessment rather than being omitted.
9. **Availability wording:** p. 1 says code is available; p. 9 says code/dataset will be released and code open-sourced. Current availability cannot be established from these inconsistent tenses without inspecting the external artifact, which was not authorized here.

[D] These issues weaken precise aggregate and example-level interpretation without invalidating every table entry. They motivate cautious use of the paper for a literature review: distinguish the proposed mechanism, the reported benchmark observations, and unproven comparative claims.

# 15. Contributions and novelty

| Contribution category | What is claimed or supplied | Qualification |
|---|---|---|
| Conceptual [A] | A stage-oriented view of agent backdoors and persistent cross-stage influence | Mechanism formalization, not a proof of universal propagation |
| Methodological/system [A] | Explicit interfaces, component-local injection wrappers, configurable runtime, trajectory logging | Implementation claimed; no supplied code/log artifact inspected |
| Benchmark [A] | Four applications and standardized task loaders/evaluation | Dataset identities, counts, and detailed verifier rules absent |
| Empirical [A] | Multi-model/task/attack results, channel aggregation, poisoning-ratio and token analyses | Descriptive rates without uncertainty or full configuration details |
| Defense exploration [A] | Preliminary transfer analysis of probability-based signals | No new defense mechanism proposed; appendix explicitly says so |
| Novelty claim [A] | Authors call it the first modular stage-aware framework from an agent-centric perspective | Priority not externally verified |

[D] The distinctive value within the supplied paper is organizational and infrastructural: different attack families are expressed through common stage interfaces and evaluated using both normal task success and malicious behavior. No novel theorem, formal robustness guarantee, or fully specified new attack optimization algorithm is presented.

# 16. Limitations

## Authors' stated limitations

[A] Page 9 acknowledges that tested tasks, attacks, and backbones do not fully capture real-world agent architectures, execution environments, or threat models. Analysis concentrates on trigger persistence and cross-stage propagation in controlled benchmarks. Adaptive adversaries and more complex deployments need further study because behavior could be richer and less predictable. The authors propose benchmark updates and open-sourcing to support reproducibility.

[A] Pages 8–9 and Appendix A characterize the defense study as preliminary. Appendix A explicitly says no new defense mechanisms are proposed. Probability signatures can be subtle, delayed, or mixed with benign reasoning, retrieval, and feedback, limiting simple detection transfer.

## Additional evidence-based analyst observations

[D] Dataset/sample sizes, actual step budgets, seeds, run counts, hardware/software, attack strings, and detailed checking procedures are absent. These omissions prevent independent reconstruction from the article alone. No direct standalone baseline, multi-step-versus-single-step ablation, or component-retention ablation quantifies the incremental effect of agency. Aggregate success rates do not directly measure how long a trigger survives or which stages it traverses.

[D] Web evidence covers four backbones and has striking variation, so generalized claims about Web-agent vulnerability need restraint. Attack grids differ because BadAgent appears only in T4. Family aggregation may mix tasks, attacks, and model variants with unspecified weighting. The prose/table disagreements and persistence/ASR terminology ambiguity introduce additional reporting uncertainty. None of these observations is attributed to the authors as an admission.

# 17. Threats to validity

The following categories are **[D] analyst classifications** applied to observable reporting limits.

| Validity dimension | Evidence-based concern | Consequence |
|---|---|---|
| Internal validity | Multiple models/tasks/attack implementations vary together; no architecture-only control | Channel/task associations do not isolate causation by persistence or feedback |
| Construct validity | Persistence language uses ASR numbers; joint ACC/ASR outcomes lack detailed checker definitions | Successful harm, trigger survival, and benign completion may be conflated if read loosely |
| Statistical conclusion validity | No instance counts, uncertainty, repetitions, or significance tests | Small differences and zero rates cannot establish robust rankings |
| External validity | Four representative applications, restricted Web backbones, controlled setting | Results cannot automatically generalize to arbitrary real deployments |
| Ecological validity | Environment details, realistic permission boundaries, and adaptive attackers insufficiently specified | Relationship to deployed purchasing, browsing, or driving systems is uncertain |
| Reproducibility | No supplied configuration/code/data/logs; several hyperparameters unspecified | Framework claims cannot be independently replayed from these inputs |
| Reporting consistency | Misassigned numerical examples and unresolved aggregation/metric terminology | Specific claims require table-level verification and explicit caveats |

[D] High clean accuracy is not evidence of security, but low ASR alone is also insufficient without knowing task utility, attack strength, and sample sizes. The benchmark tables should therefore be read as condition-specific observations rather than universal security scores.

# 18. Future work and open questions

## A. Explicit author-proposed directions

[A] The authors call for study of adaptive adversaries and more complex deployment scenarios; continued benchmark updates; code and dataset release to support reproduction; and agent-aware defenses that reason over multi-step trajectories, state evolution, cross-module interactions, and tool-mediated effects. (pp. 9, 12–13.)

## B. Additional open questions from this analysis

[D] What changes when the same backbone, task, trigger budget, and malicious content are tested in standalone, single-step agent, and persistent agent conditions? Which components cause incremental vulnerability? How long do triggers remain effective, and can propagation be traced through specific artifacts? How should attack success be checked when task completion and harmful behavior coexist?

[D] Why do Claude and GPT-4o-mini differ so sharply from Gemini under several Web attacks? How do access requirements and contamination budgets change that pattern? What detector operating points are practical at low false-positive rates, with confidence intervals and unseen attacks? How should family means be weighted when tasks and available attack columns differ? These are research questions suggested by the evidence, not findings reported by the authors.

# 19. Terminology and notation glossary

| Term/symbol | Beginner-friendly meaning within this paper |
|---|---|
| LLM | Large language model; the agent's language-model backbone |
| Agent | Model embedded in an iterative workflow with planning, memory, tools, and state |
| RAG | Retrieval-augmented generation; generating with content obtained from an external store |
| Backdoor | Hidden malicious behavior activated by a trigger |
| Trigger τ | Condition/content that activates the malicious behavior |
| Planning P; p_t | Function producing a plan; its artifact at step t |
| Memory M; m_t | Retrieval function; retrieved material at step t |
| Tools T; o_t | External action/feedback function; its output at step t |
| q | User query/task request |
| x_t | Observable context visible to the backbone |
| s_t | Structured/internal agent state |
| t; t* | Current step; selected injection step |
| A; A_τ | Clean runtime/trajectory mapping; attacked counterpart |
| G | Attack goal; named but not formalized as a common optimization loss |
| 𝒯(q) | Logged trajectory containing context, state, and stage artifacts |
| ACC | Accuracy/task success as determined by a task-specific verifier |
| Clean ACC | Task success with no injected trigger |
| Attacked ACC | Task success on triggered executions |
| ASR | Attack success rate: triggered instances exhibiting attacker behavior |
| White-box/black-box | Access categories assigned in T1; precise implementation boundaries are not fully specified |
| Persistence | Continued availability/influence across steps; no separate quantitative estimator supplied |
| Propagation | Influence moving through later components/context/state |
| Poisoning ratio | Contamination intensity in external memory/retrieval corpus; tested at 0.1, 0.2, 0.5 |
| Relative token overhead | Normalized token-consumption quantity plotted in F3; denominator not fully defined |
| ROC | Receiver operating characteristic: true-positive rate against false-positive rate |
| AUROC | Area under the ROC curve; F5 labels 0.7681 |
| Target/non-target tokens | Output-token groups in the defense analysis; exact token-selection procedure unspecified |

# 20. Key numerical results

Values below preserve reported conditions. Percentage-point differences are explicitly derived. Graph estimates are not treated as exact data.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Application settings | 4 | settings | QA, Code, Web, Drive | Author-reported | p. 5 §4.3 |
| Attack methods | 7 | methods | Two planning, three memory, two tools | Author-reported | pp. 3, 5 T1/§5.1 |
| GPT planning/memory/tools | 43.58 / 77.97 / 60.28 | % ASR | Family aggregation; also called persistence in abstract | Author-reported | pp. 1–2, 8 T6 |
| DeepSeek memory/tools | 38.91 / 42.20 | % ASR | Exception to memory-highest ordering | Author-reported | p. 8 T6 |
| Code GPT-4o-mini AgentPoison | 98.01 / 56.74 / 58.95 | % ASR / attacked ACC / clean ACC | T2 condition | Author-reported | p. 6 T2 |
| Accuracy difference for preceding row | −2.21 | percentage points | 56.74 − 58.95 | Analyst-derived | p. 6 T2 |
| Code GPT-5.2 TrojanRAG | 85.94 / 88.27 / 84.73 | % ASR / attacked ACC / clean ACC | T5 condition | Author-reported | p. 7 T5 |
| Accuracy difference for preceding row | +3.54 | percentage points | 88.27 − 84.73 | Analyst-derived | p. 7 T5 |
| QA GPT-5.2 AgentPoison | 55.62 / 47.96 / 89.37 | % ASR / attacked ACC / clean ACC | Accuracy-preservation counterexample | Author-reported | p. 7 T5 |
| Accuracy decline for preceding row | 41.41 | percentage points | 89.37 − 47.96 | Analyst-derived | p. 7 T5 |
| Web Claude BadChain | 97.39 / 98.35 / 98.54 | % ASR / attacked ACC / clean ACC | Other five Claude ASRs are 0 | Author-reported | p. 6 T3 |
| Web Gemini BadChain | 98.74 / 97.47 / 96.20 | % ASR / attacked ACC / clean ACC | Highest T3 ASR | Author-reported | p. 6 T3 |
| Web Gemini AgentPoison | 86.67 / 92.41 | % ASR / attacked ACC | Same clean ACC 96.20 | Author-reported | p. 6 T3 |
| Web GPT-4o-mini AgentPoison | 8.91 / 98.39 | % ASR / attacked ACC | Clean ACC 99.16 | Author-reported | p. 6 T3 |
| Web Qwen3-VL DemonAgent | 14.35 / 96.57 | % ASR / attacked ACC | Clean ACC 99.25 | Author-reported | p. 6 T3 |
| Open-source Drive BadChain | 92.15–97.85 | % ASR | Range of five T4 rows; endpoints Kimi and DeepSeek-V3.2 | Analyst-derived from reported values | p. 7 T4 |
| Drive Qwen3 AdvAgent | 75.34 | % ASR | Exception to universal >80 reading | Author-reported | p. 7 T4 |
| GPT memory at ratios 0.1/0.2/0.5 | 53.06 / 77.97 / 97.72 | % ASR | Corpus contamination ablation | Author-reported | p. 8 T7 |
| Gemini memory at ratios 0.1/0.2/0.5 | 50.39 / 75.39 / 97.00 | % ASR | Same analysis | Author-reported | p. 8 T7 |
| Qwen memory at ratios 0.1/0.2/0.5 | 33.25 / 55.45 / 86.75 | % ASR | Same analysis | Author-reported | p. 8 T7 |
| DeepSeek memory at ratios 0.1/0.2/0.5 | 21.84 / 38.91 / 70.83 | % ASR | Same analysis | Author-reported | p. 8 T7 |
| Planning/tools/memory overhead at strength 4 | ≈1.12 / ≈1.47 / ≈1.9 | relative token overhead | GPT-4o plot | Approximate visual estimate | p. 8 F3 |
| Detection AUROC | 0.7681 | unitless | Aggregate probability-inspired detector | Visually readable | p. 13 F5 |

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Three-stage interfaces support unified attack expression [A] | Stage hooks and component replacement | F2, E8, X1 | pp. 4–5 | Strong descriptive evidence of proposed design; implementation not inspected |
| Reused artifacts can carry influence across steps [A] | Context/state update equations | E4–E7, F1 | pp. 3–4 | Clear mechanism; no quantified survival curve |
| High malicious success can coexist with near-clean task accuracy [A] | Code GPT-4o-mini ASR 98.01, ACC 56.74 vs 58.95 | T2/X1 | p. 6 | Supported configuration; not universal |
| Web vulnerability is heterogeneous [B/D] | Claude/GPT zeros versus high Gemini results | T3/X2 | p. 6 | Strong descriptive evidence; counts absent |
| Open-source Drive BadChain is consistently high [A] | All five ASRs exceed 90 | T4/X1 | pp. 7–8 | Strong for reported rows; causal amplification not isolated |
| Clean model performance does not guarantee robustness [A] | High-clean models retain high attack rates | T2/T5/X1/X3 | pp. 6–7 | Supports absence of guarantee, not a universal negative correlation |
| Memory often leads family averages [A] | Four of five T6 rows | T6/X4 | p. 8 | DeepSeek exception; aggregation ambiguity |
| More memory contamination increases reported ASR [A] | All T7 rows rise across 0.1, 0.2, 0.5 | T7/X5 | p. 8 | Strong descriptive monotonicity; no error estimates |
| Memory attacks cost more tokens at higher strength [A/B] | Green line rises above orange and blue | F3/X6 | p. 8 | Plot-specific; normalization/strength definition incomplete |
| Simple probability signals have limited demonstrated transfer [A] | Mean bars and AUROC 0.7681 | F4/F5/X7 | pp. 8–9, 12–13 | Preliminary; no standalone detector comparison or operational threshold |
| Web-agent-versus-standalone superiority in vulnerability is unestablished [D] | All main evaluations are agent conditions | T2–T5/§5 | pp. 5–7 | High-confidence scope observation, not a reported null test |

# 22. Very simple explanation — Explain Like I'm 15

An ordinary language-model interaction can end after one response. The agents in this paper keep working: they make a plan, look up information, use tools, and use what happened to decide what to do next. That gives malicious content several places to enter. If the content becomes part of the agent's continuing notes or feedback, it may influence more than one decision.

The researchers built a test framework that can interfere with planning, memory, or tools and then check both whether the agent finishes its normal task and whether it does what the attacker wanted. Those checks are different. A system can receive a good task score while also doing something harmful that the task checker does not fully capture. The paper reports examples of that combination, although some attacks also lower normal accuracy substantially.

The results depend strongly on the task, model, and attack. Some driving-agent attacks succeed very often. Adding more poisoned memory raises attack success in the reported memory tests. Web agents are mixed: a method that succeeds almost every time for one model can have zero or low observed success for another. The evidence does not show that every Web agent is easy to attack.

For the question about Web agents versus standalone models, the paper explains why added memory, tools, and repeated feedback could create extra security problems. It does not run the direct comparison needed to prove how much more vulnerable Web agents are. Its useful lesson is to inspect the whole chain of decisions and feedback, while keeping that missing comparison clear.

# Completeness Audit

The inventory, rather than response length, defines coverage. All supplied substantive text sections and all five substantive figures, seven tables, eight numbered equations, and the trajectory expression were inspected in the available representations. Coverage is bounded by the missing page-11 visual, absent external artifacts, dense graphical details, and unspecified methods. The analysis is comprehensive for those boundaries, not a claim of independent experimental validation.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| ABS Abstract | Yes, text + visual | Yes | Fully represented | Claims and persistence/ASR discrepancy included |
| S1 Introduction | Yes, text + visual | Yes | Fully represented | Motivation, gap, three contributions |
| S2a LLM-based Agents | Yes, text + visual | Yes | Represented in compressed form | Context and reused artifacts |
| S2b Backdoor Attacks on Agentic Systems | Yes, text + visual | Yes | Represented in compressed form | Prior categories and attributed gaps; no external literature review |
| S3 Preliminaries | Yes, text + visual | Yes | Fully represented | Formal system and attack definitions |
| SS3.1 Agent Formulation | Yes, text + visual | Yes | Fully represented | E1–E5 and notation |
| SS3.2 Backdoor Attacks | Yes, text + visual | Yes | Fully represented | Triggered trajectory and E6 |
| S4 Framework overview | Yes, text + visual | Yes | Fully represented | F2 and architecture |
| SS4.1 Stage-aware Framework | Yes, text + visual | Yes | Fully represented | Hooks, recurrence, E7 |
| SS4.2 Backdoor Injection | Yes, text + visual | Yes | Fully represented | Configuration, logging, wrappers, flexible order, standardization |
| SS4.3 Representative Tasks | Yes, text + visual | Yes | Fully represented | Four workflows, harms, verifier examples |
| SS5.1 Systems | Yes, text + visual | Yes | Represented in compressed form | Model groups and multimodal restriction |
| SS5.1 Attacks | Yes, text + visual | Yes | Fully represented | Seven methods; incomplete cross-table grid |
| SS5.1 Metrics | Yes, text + visual | Yes | Fully represented | Clean ACC, ASR, attacked ACC |
| SS5.2a Accuracy/ASR coexistence | Yes, text + visual | Yes | Fully represented | Positive examples, counterexamples, prose errors |
| SS5.2b Channel patterns | Yes, text + visual | Yes | Fully represented | Memory/tools distinction and misclassified examples |
| SS5.2c Model performance/robustness | Yes, text + visual | Yes | Fully represented | No security guarantee from clean performance |
| SS5.2d Sequential amplification | Yes, text + visual | Yes | Fully represented | Drive values and causal limits |
| SS5.3a Family aggregation | Yes, text + visual | Yes | Fully represented | Full T6, exceptions, reproducibility check |
| SS5.3b Poisoning ratios | Yes, text + visual | Yes | Fully represented | Full T7 and missing protocol |
| SS5.3c Efficiency | Yes, text + visual | Yes | Fully represented | F3 trends and approximate readings |
| SS5.4 Potential Defenses | Yes, text + visual | Yes | Fully represented | Preliminary status, F4 caveats |
| S6 Conclusion | Yes, text + visual | Yes | Represented in compressed form | Main conclusions bounded by evidence |
| LIM Authors' limitations | Yes, text + visual | Yes | Fully represented | Coverage, controlled setting, adaptive/deployment gaps |
| ACK Acknowledgments | Yes, text + visual | Yes | Represented in compressed form | Funding context only: NSFC grant 72571281 and Hunan grant 2025JJ40066 |
| REF References | Yes, text; visuals except p. 11 | Yes | Inspected but deliberately omitted as repetitive/non-substantive | Bibliographic list compressed; no citation validity claims |
| APP_A Additional Defenses | Yes, text + visual | Yes | Fully represented | No new mechanism; reference-model comparison; F5 |
| F1 | Yes, visual + caption | Yes | Represented in compressed form | Fine labels uncertain; conceptual content covered |
| F2 | Yes, visual + caption | Yes | Represented in compressed form | Main regions/arrows covered; tiny labels not exhaustively transcribed |
| F3 | Yes, visual + text | Yes | Fully represented | Axes, encoding, trends, estimates, limitations |
| F4 | Yes, visual + text | Yes | Fully represented | Three groups, means, no uncertainty |
| F5 | Yes, visual + text | Yes | Fully represented | ROC axes, diagonal, AUROC 0.7681 |
| T1 | Yes, visual + text | Yes | Fully represented | All seven taxonomy rows |
| T2 | Yes, visual + text | Yes | Represented in compressed form | Structure, key rows, descriptive maxima; full matrix not copied |
| T3 | Yes, visual + text | Yes | Represented in compressed form | All model patterns; selected ASR/ACC details |
| T4 | Yes, visual + text | Yes | Represented in compressed form | Seven-attack coverage, key patterns/errors; full matrix not copied |
| T5 | Yes, visual + text | Yes | Represented in compressed form | High-clean examples and accuracy declines |
| T6 | Yes, visual + text | Yes | Fully represented | All values reproduced |
| T7 | Yes, visual + text | Yes | Fully represented | All values reproduced |
| E1, E2, E3 | Yes, visual + text | Yes | Fully represented | Planning, memory, tools |
| E4, E5 | Yes, visual + text | Yes | Fully represented | Context and state updates |
| E6, E7, E8 | Yes, visual + text | Yes | Fully represented | Behavior criterion, recurrence, component replacement |
| E_TRAJ | Yes, visual + text | Yes | Fully represented | Logged tuple sequence |
| X1, X2, X3 | Yes | Yes | Represented in compressed form | Main non-Web, Web, advanced-model matrices |
| X4, X5, X6 | Yes | Yes | Fully represented | Aggregation, poisoning, overhead |
| X7a, X7b | Yes | Yes | Fully represented | Token means and ROC analysis |
| Formal research questions | Not present | Absence stated | Fully represented | Informal objectives distinguished from user's question |
| Formal hypotheses | Not present | Absence stated | Fully represented | No invented hypothesis tests |
| Algorithms/pseudocode/theorems | Not present | Absence stated | Fully represented | Workflow equations are not proofs |
| C1 Framework contribution | Yes | Yes | Fully represented | Novelty attributed to authors |
| C2 Benchmark contribution | Yes | Yes | Fully represented | Four applications, missing data details |
| C3 Empirical contribution | Yes | Yes | Fully represented | Results and metric caveats |
| Supplied supplementary files | None | Absence stated | Missing from supplied material | No separate supplement reviewed |
| Repository/code/data/configurations | No | Absence stated | Missing from supplied material | URL and release promises only |
| Page 11 visual | No | Text covered | Inaccessible | Supplied reference text readable |

## Missing or inaccessible material

The original PDF binary, page-11 visual rendering, linked repository contents, dataset, benchmark configuration files, implementation, full trajectories, run receipts, and any separate supplementary artifact were not supplied for inspection. No separate supplementary file is explicitly identified in the supplied paper. The lack of these artifacts is not evidence that they do not exist. The automated appendix-detection result was incomplete: Appendix A is present and reviewed.

## Uncertain interpretations

Exact small labels in Figures 1–2; exact plotted coordinates in Figures 3–4; the precise trigger-strength unit and relative-token denominator; persistence as distinct from ASR; family aggregation weights/subsets; detector/reference identities and scoring; and detailed clean/attack verifier relationships remain uncertain or unspecified. The Kimi accuracy and Qwen improvement examples conflict with their tables. The code-availability tense is inconsistent. These issues have not been silently reconciled.

## Deliberately compressed material

The full numerical matrices in Tables 2–5 are not copied cell by cell. Their structure, major patterns, representative results, relevant extrema, exceptions, and contradictory prose examples are retained. Tables 6–7 and the qualitative taxonomy are reproduced in full. Repeated claims about workflow persistence and the full bibliography are compressed. Affiliations, contribution footnotes, funding, and venue metadata are accounted for without extended discussion. Decorative icons and tiny internal figure labels are grouped where they do not add a distinct methodological claim.

## Potential omissions

No known substantive inventory object is wholly unrepresented. Many individual cells of the large evaluation matrices are deliberately not transcribed; exact graphical values cannot be recovered where unlabeled. No claim is made that unavailable artifacts, unreported experimental details, or the missing page-11 visual were reviewed. The supplied source hash is carried through as provided and was not independently recomputed.
