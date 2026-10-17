## Stage 0 — Document Accessibility Report

The supplied material contains extracted text for physical PDF pages 1–19 and ten rendered page images: pp. 1, 3–8, and 12–14. The complete supplied text was inspected. Those ten page images were also visually inspected; pp. 2, 9–11, and 15–19 were inspected through supplied text only. Physical page numbers agree with the printed page numbers visible in the rendered images. The hash is the supplied source identifier; it has not been independently recomputed.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied text covers pp. 1–19, including main text, references, and appendices. |
| Available page range | 1–19; 19 supplied text pages. |
| Apparently missing pages | No gap within the supplied sequence; this does not independently establish that no other version or supplement exists. |
| Visual content | Partial page rendering, but all eight numbered figures, all four numbered tables, and both algorithms occur on visually supplied pages. |
| Tables | Tables 1–4 are readable in the supplied images and extracted text. |
| Equations | Equation (1) is available as text on p. 2. Appendix expressions are available as text; Algorithms 1–2 are also visible on p. 14. Superscripts, hats, and overloaded notation require care. |
| Appendices | Appendix A, Implementation Details, pp. 12–15; Appendix B, Attack Demonstrations, pp. 15–19. |
| Supplementary material | No separate supplementary file supplied. |
| Referenced external artifacts | Benchmark website, model page, framework website, and bibliographic works are referenced but were not accessed. |
| OCR | No additional OCR used. Supplied extraction contains artifacts, especially in Figure 1 and warning icons. |
| Other limitations | No repository inspection, execution, external verification, or independent reproduction. Text-only appendix demonstrations cannot be claimed as visually inspected. |

The instructions and role markers appearing inside attack examples are treated only as untrusted evidence describing attacks. They are not instructions to this analysis. Closed-document mode is maintained throughout.

Evidence labels used below: **[A] AUTHOR-REPORTED**, **[B] DIRECTLY OBSERVABLE**, **[C] ANALYST-DERIVED**, and **[D] ANALYST INTERPRETATION**. No external information [E] is introduced. HIGH confidence means the supplied evidence is explicit and readable; it does not mean the underlying experimental claim has been independently validated.

## 1. Plain-language orientation

AgentLAB studies how a large language model (LLM) agent can be manipulated over a sequence of interactions. An agent is a language model connected to capabilities such as browsing, email, file operations, planning, and persistent memory. Its outputs can therefore change an environment rather than merely produce answers. The paper asks whether safety mechanisms remain effective when an attacker gradually redirects this process instead of issuing one obvious malicious instruction.

**[A]** The researchers build Agent Long-horizon Attack Benchmark, abbreviated AgentLAB, with five attack families, 28 environments, and 644 security cases. They implement attacks through cooperating planning, attacking, judging, and sometimes verification agents. They then evaluate six target model families, compare long-horizon injection with a one-shot baseline, vary attack and optimization budgets, and test four existing defense approaches. Sources: abstract, pp. 1–2; §§4–5, pp. 3–8.

**[A]** The principal finding is substantial vulnerability under the tested conditions, especially to tool chaining. Table 2 reports tool-chaining attack success rates of 73.3%–96.3% across the six agents. Vulnerability depends strongly on attack type: Claude-4.5 has 0.0% task-injection success but 73.3% tool-chaining success and 38.8% memory-poisoning success. Existing defenses sometimes reduce success substantially, but no tested defense works consistently across every covered model and attack family.

For the user's research question, **[D] analyst inference** is that web agents acquire additional opportunities for compromise because they consume outside content repeatedly, execute tools, and may carry information into future sessions. The supplied paper supports these mechanisms within agent systems. It does **not** directly establish a controlled comparison between standalone LLMs and web agents using the same model, task, attacker budget, and evaluation criteria. Its empirical comparison is primarily between attack conditions on tool-enabled agents.

The contribution is therefore a benchmark and attack framework for studying temporal and compositional security failures, accompanied by a preliminary evaluation. It is not a proof that every web agent is less secure than every standalone LLM.

## 2. Document roadmap and inventory

The paper is a mixed **security, AI systems, algorithm, and benchmark paper with empirical evaluation**. The main text occupies pp. 1–8, references pp. 9–11, and appendices pp. 12–19. The title is **AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks**. Authors: Tanqiu Jiang, Yuhui Wang, Jiacheng Liang, and Ting Wang, affiliated with the Department of Computer Science, Stony Brook University. Page 1 labels the work a preprint dated February 20, 2026, while its arXiv margin states arXiv:2602.16901v1, 18 February 2026. Both dates are preserved; no conference venue is supplied for this paper.

| Inventory ID | Original object | Location and role |
|---|---|---|
| ABS | Abstract | p. 1: motivation, benchmark scope, principal conclusion. |
| S1 | §1 Introduction | pp. 1–2: gap, principles, contributions. |
| S2 | §2 Related Work | p. 2: user attacks, environment attacks, security benchmarks. |
| S3 | §3 Problem Formulation | pp. 2–3: interaction trace and threat models. |
| S4 | §4 AgentLAB | pp. 3–6: benchmark architecture and construction. |
| SS41 | §4.1 Components | p. 3: agent, environment, task, attack. |
| SS42 | §4.2 Long-Horizon Attacks | pp. 4–6: shared attack framework and five families. |
| SS421–SS425 | §§4.2.1–4.2.5 | Intent hijacking, tool chaining, objective drifting, task injection, memory poisoning. |
| SS43 | §4.3 Benchmark Implementation | p. 6: data curation and statistics. |
| SS431–SS432 | §§4.3.1–4.3.2 | Environment/task selection; counts and risk distribution. |
| S5 | §5 Evaluation | pp. 6–8: preliminary experiments. |
| SS51–SS54 | §§5.1–5.4 | Setup, effectiveness, ablations, defenses. |
| S6 | §6 Conclusion | p. 8: synthesis and benchmark aspirations. |
| REF | References | pp. 9–11: cited literature and artifacts. |
| A | Appendix A | pp. 12–15: implementation details for all five attacks. |
| A1–A5 | §§A.1–A.5 | Threat models, model roles, algorithms, and poisoning configuration. |
| B | Appendix B | pp. 15–19: representative attack demonstrations. |
| B1–B5 | §§B.1–B.5 | Five demonstrations; B.1 is titled Intent Injection. |
| F1–F8 | Figures 1–8 | Architecture, attack framework, two examples, risk distribution, effectiveness/turns, two ablations. |
| T1–T4 | Tables 1–4 | Taxonomy, effectiveness, one-shot comparison, defense evaluation. |
| E1 | Equation (1) | p. 2: interaction trace. |
| EA4 | Appendix A.4 expressions | p. 13: snippet generation and execution trace. |
| ALG1–ALG2 | Algorithms 1–2 | p. 14: exemplar retrieval and adaptive injection. |
| X1–X5 | Evaluation analyses | Overall effectiveness; one-shot comparison; turn efficiency; two budget ablations; defenses. |
| C1–C4 | Stated contributions | p. 2: taxonomy, multi-agent framework, benchmark, preliminary evaluation. |

There are no supplied keywords, numbered theorems, lemmas, or formal hypotheses. The substantive affiliation/correspondence footnote and preprint information are accounted for here. The benchmark availability statement is represented without implying that its linked artifact was inspected.

## 3. Background and context

**[A]** A large language model agent extends text generation with actions. The paper's examples include executing tool calls, reading web pages, modifying workspace data, and extracting information into external memory. This matters because a maliciously influenced decision can produce an unauthorized action rather than only an undesirable sentence. Sources: p. 1; §4.1, p. 3.

A **prompt injection** is an attempt to make material encountered by the model redirect its behavior. An **indirect prompt injection** reaches the agent through environmental content, such as a webpage, email, document, or API result, rather than through the legitimate user's instruction. The paper distinguishes this from a malicious user manipulating their own agent through the instruction interface. Source: §§1–3, pp. 1–3.

A **long-horizon attack** unfolds across multiple interactions. Its steps can be distributed through a conversation, a chain of tools, multiple pages, or separate sessions. **Adaptivity** means the attacker changes prompts or payloads in response to the target's behavior or a judge's feedback. More interaction turns and more optimization attempts are separate experimental dimensions; a longer trajectory is not automatically the same thing as a more adaptive search. Source: §5.3, p. 7.

**Tool chaining** exploits composition: a sequence of operations can achieve a harmful objective even when individual operations appear ordinary. **Objective drifting** changes the goal the agent effectively optimizes. **Task injection** adds unauthorized work alongside legitimate work. **Memory poisoning** causes attacker-controlled content to be stored and later retrieved as if it were legitimate user context. Sources: §§4.2.2–4.2.5, pp. 4–6.

The minimum conceptual distinction is between **data the agent should consider** and **instructions the agent should obey**. **[D]** The demonstrated attacks repeatedly blur that boundary: environmental text masquerades as policy, a preference, a dependency, or an explanation of why another tool call is necessary. The paper's evidence supports this interpretation, but it does not provide a formal trust-policy specification for every benchmark environment.

## 4. Research problem and gap

**Existing problem [A]:** Agents conduct extended user–agent–environment interactions in settings where unsafe actions can create financial, privacy, operational, or other harms. Single-turn evaluation may miss attacks that accumulate influence or distribute malicious work across steps. Sources: pp. 1–3.

**Previous approaches, as characterized by the authors [A]:** User–agent attack research applies jailbreak techniques and increasingly studies risky actions, memory manipulation, and code generation. Environment–agent work studies indirect injections and automated attack discovery. Existing benchmarks provide tools and realistic tasks, but the authors argue that they predominantly evaluate static or single-turn attacks without sufficient support for adaptive, long-horizon adversaries. Source: §2, p. 2. This is the authors' literature assessment, not an independently verified survey conclusion.

**Research gap [A]:** A unified benchmark is needed to evaluate sustained user manipulation and cumulative environmental injections across extended interactions. AgentLAB seeks to combine attack diversity, realistic agent capabilities, and extensibility. Sources: pp. 1–2.

**Motivation [A]:** Temporal exploitation can evade one-shot safeguards; realistic environments make security measurements more relevant; modular interfaces allow future additions. These are the paper's three stated design principles: temporal exploitation, ecological validity, and extensibility. Source: p. 1.

**Scope:** The evaluation concerns tool-calling agents powered by six model families, five instantiated attack families, selected environments, and four baseline defenses. It does not isolate browsing as the sole cause of vulnerability, evaluate every available defense, or directly compare standalone and agentic deployments under matched conditions. **[D]** Its relevance to web-agent security is strong at the mechanism level and narrower at the comparative-causality level.

## 5. Research questions, objectives, and hypotheses

The paper does not state a numbered set of formal research questions or hypotheses. The following objectives are extracted from its stated purpose rather than invented as formal questions.

| ID | Status | Objective | Evidence |
|---|---|---|---|
| O1 | Author objective | Build a benchmark for adaptive, long-horizon agent attacks. | Abstract; pp. 1–2. |
| O2 | Author objective | Organize attacks through a taxonomy and unified implementation framework. | Contributions, p. 2; §4, pp. 3–5. |
| O3 | Author objective | Measure representative agents' vulnerability. | §5, pp. 6–7. |
| O4 | Author objective | Compare long-horizon injection with a one-shot counterpart. | Table 3 and accompanying text, p. 7. |
| O5 | Author objective | Examine the roles of interaction length and adaptive optimization. | §5.3, pp. 7–8. |
| O6 | Explicit prose question | Determine whether defenses effective against one-shot attacks also work against long-horizon attacks. | §5.4, p. 8. |
| RQ-USER | User question; analyst mapping | Explain why web AI agents may be more vulnerable than standalone LLMs. | Interpreted using §§3–4 and Appendices A–B; no matched standalone comparison. |

No formal null hypothesis, alternative hypothesis, preregistration, or significance threshold is supplied. The reported trends should therefore be understood as descriptive benchmark findings rather than hypothesis-test outcomes.

## 6. Assumptions / Threat Model

The general objective is to induce a target agent to accomplish a malicious task T* through multiple interactions. The paper distinguishes two attack locations. In the **user-as-adversary** model, selected legitimate instruction slots p are replaced by adversarial prompts p*. In the **environment-as-adversary** model, selected observations o are replaced by adversarial observations o*. In both cases, the resulting action sequence is intended to accomplish T*. Source: §3, p. 3.

General access includes **black-box** settings, where the attacker sees actions and responses, and **white-box** settings, where the attacker sees internal reasoning. Appendix A.1 explicitly specifies black-box access for intent hijacking. Appendix A.4 calls its trajectory-and-reasoning access **grey-box**. The terminology differs, but the meaningful distinction is the information revealed to the attacker; these conditions must not be collapsed into one access assumption.

| Attack | Controlled surface | Intended effect | Important access condition |
|---|---|---|---|
| Intent hijacking | User prompts over multiple turns | Induce execution of a harmful task through contextual persuasion. | Appendix A.1 specifies response-based black-box adaptation. |
| Tool chaining | Prompts eliciting tool calls | Compose ordinary-looking actions into a harmful sequence. | Planner's candidate calls are verified in the environment. |
| Objective drifting | Product descriptions, search snippets, reviews, other environmental text | Shift decisions away from the user's original goal. | A.3 says the attacker cannot modify the system prompt or issue explicit commands; its strategy list nevertheless includes direct override attempts. |
| Task injection | Tool outputs and retrieved content | Add unauthorized tool actions through plausible intermediate dependencies. | A.4 provides complete tool trajectory and intermediate reasoning to the attacker. |
| Memory poisoning | Content ingested during ordinary work | Store false preferences and trigger unsafe behavior in later sessions. | A.5 explicitly says direct access to the memory system is unnecessary. |

The objective-drifting restriction and its direct-override strategy are an unresolved main-method description tension within p. 12. A direct override embedded in environmental text may have been intended as a strategy category, but the supplied description does not explain how that fits the stated exclusion of explicit commands.

The paper presupposes that agents have working tools, stateful environments, and evaluable task outcomes. It does not enumerate a complete trusted computing base or authorization model. **[D]** Legitimate user goals function as the intended reference objective, while attacker-controlled observations and extracted preferences should not automatically gain equivalent authority. This is an interpretation of the security boundary illustrated by the attacks.

## 7. Methodology

### Benchmark architecture

**[A]** AgentLAB separates four configurable objects: agent, environment, task, and attack. The **agent** specifies a backend model and capabilities such as tools, planning, and external memory. The **environment** specifies domain-specific tools and mutable state objects. Tools read or write these states; tool descriptions appear in the agent's system prompt, and invocation uses the environment state as an argument with FastAPI syntax. The **task** supplies a benign or malicious natural-language objective and a ground-truth tool-call or mutation sequence. The **attack** specifies the adversarial strategy and parameters. Source: §4.1, p. 3.

An evaluator compares execution trajectories with ground-truth sequences to determine completion, potentially using an external LLM. The benchmark distinguishes utility on legitimate tasks from security against malicious objectives. The supplied results emphasize attack success; they do not provide a quantitative utility table showing the effect of every defense on legitimate performance.

### Shared attack workflow

A planner proposes an attack strategy; an attacker constructs and refines prompts or observations; a judge evaluates whether the malicious goal was reached. A verifier is used for certain attacks to check proposed tool calls by executing them in the environment. TextGrad is used for adaptive refinement when intent hijacking or tool chaining stalls. Sources: §4.2, p. 4; A.1–A.2, p. 12.

Intent hijacking builds contextual narratives and personas to elicit unsafe actions. Tool chaining decomposes the malicious task into component calls before eliciting them. Objective drifting distributes goal-shifting material across browsing observations. Task injection builds an intermediate action sequence connecting legitimate and malicious work. Memory poisoning separates ingestion of false preferences from their later exploitation. These are distinct mechanisms, not five names for the same injection template.

### Data and task construction

The authors use complex environments from SHADE-Arena, AgentDojo, and WebShop and sample simpler, more diverse environments from Agent-SafetyBench. Existing malicious tasks are supplemented by manually designed tasks, particularly for objective drifting. GPT-5.1 acts as a maliciousness monitor: tasks are accepted when it consistently refuses to execute them. Objective drifting, task injection, and memory poisoning pair malicious objectives with benign counterparts to measure baseline utility. Manual validation checks clear malicious specifications, programmatic evaluability, and reasonable baseline performance. Source: §4.3.1, p. 6.

The resulting benchmark has 28 environments and 644 malicious tasks. No supplied table gives the case counts per attack family, per environment, or per evaluated model. There is no specified train/validation/test split, annotation agreement statistic, number of human reviewers, exclusion count, or leakage protocol. These details are **not specified**, rather than assumed absent from implementation.

### Target and attack models

Targets are GPT-4o, GPT-5.1, Gemini-3.0-Flash, Claude-4.5-Sonnet, Llama-3, and Qwen-3. Tables use Llama-3.1 and shorter names for several other models. Exact target checkpoint identifiers are not supplied. System and tool prompts are adapted from prior work; their complete strings are not included. Source: §5.1, p. 6.

The default planner is GPT-5.1 at temperature 0.5; the default attacker is Qwen-3-14B-Abliterated; the default judge is GPT-5.1 at temperature 0. The authors describe the attacker as having safety constraints removed through abliteration, without detailing that process. The stated maximum-turn sequence is 7, 20, 15, 5, 12. **[D]** These appear to correspond to intent hijacking, tool chaining, objective drifting, task injection, and memory poisoning in the surrounding conventional order, but the sentence does not explicitly restate the mapping.

Appendix A.4 overrides the default for task injection: GPT-5.1 generates and rewrites payloads. Its grid-search-selected settings are ne = 2 exemplars, Ni = 5 optimization iterations, and Nr = 1 rewrite. Search ranges and selection data are not specified. Appendix A.5 also uses GPT-5.1 as both poisoning planner and attacker. Its planner temperature is 0.7, with up to three strategies per scenario, payloads limited to 15 words, up to five conversational turns per strategy, and an evasiveness threshold of 3.5 on a five-point scale. Page 15 adds up to four optimization rounds and weights evasiveness at 0.4 and effectiveness at 0.6. How these nested limits relate to the default 12-turn budget is not explained.

### Metrics, defenses, and missing configuration

Attack Success Rate (ASR) is the fraction of cases where the malicious objective is fully achieved. Turn to Success (T2S) averages attack turns over successful attacks. Thus a low T2S reflects speed conditional on success, not average cost including failures. No standard deviation, confidence interval, significance test, random seed, repetition count, hardware configuration, latency, token cost, or exact software version is reported.

Self-Reminder adds safety reminders to the system prompt. Llama-Guard classifies adversarial prompts. Repeated Prompt reiterates the legitimate user's prompt each interaction. DeBERTa Detector classifies malicious instructions in retrieved tool data. The supplied material does not specify the detector's training split, fine-tuning procedure, threshold, or computational overhead. Source: §5.4, p. 8.

## 8. Experiments / Analyses

| Experiment | Purpose and manipulated condition | Evidence | Result and qualification |
|---|---|---|---|
| X1: Cross-model effectiveness | Compare six agents under five attack families. | Table 2, p. 6. | Tool chaining succeeds at 73.3%–96.3%; other families vary substantially. Per-condition sample counts and uncertainty are not given. |
| X2: One-shot versus long-horizon injection | Compare an important-message baseline with long-horizon injection. | Table 3, p. 7. | Five agents improve for the attacker; Claude remains at 0.0%. This is an agent attack comparison, not standalone-versus-agent comparison. |
| X3: Success versus required turns | Examine ASR alongside conditional T2S. | Figure 6 and text, p. 7. | Qwen intent hijacking takes 4.6 turns versus 8.5 for tool chaining, as explicitly reported in prose. Most other T2S values are only plotted. |
| X4a: Turn-budget ablation | Increase maximum attack turns for Qwen-3 and GPT-4o. | Figure 7, p. 8; discussion p. 7. | Displayed intent-hijacking and task-injection curves rise or plateau. GPT-4o task injection reaches about 80% by five turns. |
| X4b: Optimization-budget ablation | Increase adaptive optimization steps for the same two models and two attacks. | Figure 8, p. 8. | Success generally rises and then may plateau. Gains appear more gradual than turn-budget gains. No inferential comparison is reported. |
| X5: Defense evaluation | Compare no defense with two defenses appropriate to each attack family. | Table 4, p. 8. | Some reductions are large, but residual success and occasional increases remain. Utility costs and statistical uncertainty are unreported. |

For X4a and X4b, the plotted axes show budget levels rather than independent trial counts. The paper states that increasing turns helps across all attack types, but the supplied ablation figure displays only intent hijacking and task injection. The remaining three families' ablation curves are not supplied.

Appendix B gives qualitative demonstrations, not separately tabulated experiments with replication or population-level estimates. They explain possible causal pathways within an attack trajectory; they cannot establish the frequency of each pathway across the benchmark.

## 9. Results

### Cross-model and cross-attack effectiveness

The following values are **[A] author-reported ASR percentages**, Table 2, p. 6.

| Agent | Intent hijacking | Tool chaining | Objective drifting | Task injection | Memory poisoning | Reported overall |
|---|---:|---:|---:|---:|---:|---:|
| Qwen-3 | 78.1 | 96.3 | 92.2 | 93.1 | 48.0 | 81.5 |
| Llama-3.1 | 53.3 | 90.4 | 67.4 | 86.6 | 34.6 | 66.5 |
| GPT-4o | 74.0 | 94.1 | 79.2 | 79.9 | 63.3 | 78.1 |
| GPT-5.1 | 59.8 | 94.6 | 73.7 | 21.5 | 51.3 | 69.9 |
| Gemini-3 | 46.2 | 95.9 | 15.8 | 43.1 | 67.3 | 53.7 |
| Claude-4.5 | 27.2 | 73.3 | 5.3 | 0.0 | 38.8 | 28.9 |

Qwen-3 has the highest displayed ASR for intent hijacking, tool chaining, objective drifting, and task injection. Gemini-3 has the highest memory-poisoning ASR, 67.3%. Claude has the lowest displayed value in the first four families; Llama-3.1 has the lowest memory-poisoning value, 34.6%. These rankings concern the specific evaluated configurations, not universal model safety rankings.

**Numerical inconsistency:** The prose calls GPT-5.1's average ASR more than about 70%, while its table overall is 69.9%. More substantively, **[C]** its five displayed family scores sum to 300.9, and 300.9 / 5 = 60.18%, not 69.9%. The other five reported overall scores agree, after rounding, with their unweighted family means. The paper does not define an aggregation that resolves GPT-5.1's discrepancy. Its reported 69.9% is retained as reported; 60.18% is separately labeled as the derived unweighted mean.

### One-shot comparison

| Agent | One-shot ASR | Long-horizon ASR | Derived absolute change |
|---|---:|---:|---:|
| Qwen-3 | 81.9% | 93.1% | 11.2 percentage points |
| Llama-3 | 50.7% | 86.8% | 36.1 percentage points |
| GPT-4o | 62.5% | 79.9% | 17.4 percentage points |
| GPT-5.1 | 2.08% | 21.5% | 19.42 percentage points |
| Gemini-3 | 41.0% | 43.1% | 2.1 percentage points |
| Claude-4.5 | 0.0% | 0.0% | 0.0 percentage points |

The first two numerical columns are **[A]**, Table 3, p. 7. The last is **[C]**, calculated by subtracting one-shot ASR from long-horizon ASR. For GPT-5.1, 21.5 / 2.08 is approximately 10.34 times the baseline rate; this ratio should not be confused with the 19.42-percentage-point absolute change. Ratios relative to Claude's zero baseline are undefined and are not calculated.

Table 3 reports Llama long-horizon injection at 86.8%; Table 2 gives 86.6%. Table 4 uses 86.8%. The supplied material does not explain the difference. The baseline comparison is strongest as evidence that the instantiated long-horizon attack outperforms this particular important-message attack; it does not isolate duration from adaptivity, intermediate actions, or additional attacker resources.

### Defense results

For Claude, Self-Reminder changes intent hijacking from 27.2% to 6.9%, but tool chaining remains 57.9% versus 73.3% without defense. **[C]** These are reductions of 20.3 and 15.4 percentage points respectively. DeBERTa Detector lowers GPT-4o task injection from 79.9% to 12.7%, a derived 67.2-percentage-point reduction, but leaves memory poisoning at 31.6%. Sources: Table 4, p. 8.

Not every defense reduces every rate. Repeated Prompt raises Qwen task-injection ASR from 93.1% to 95.1%, a derived increase of 2.0 percentage points. Llama-Guard changes Gemini intent hijacking from 46.2% to 46.4%, a derived increase of 0.2 percentage points. Without repetitions or uncertainty intervals, the meaning of these small changes cannot be established statistically.

## 10. Figure-by-figure interpretation

### Figure 1 — Overall benchmark architecture, p. 3

**Visually inspected.** This is a component-and-flow diagram, not a numerical plot. The left side shows an adversary above a legitimate user. Both connect to the central agent through instruction/response arrows. The agent contains a backend LLM and capabilities labeled Memory/RAG, Tool Calling, and Planning. RAG is not expanded in the supplied paper; its conventional expansion is not introduced as an author definition.

To the right, tool-call and observation arrows connect the agent with benign and malicious environments, each showing state updates. Red arrows and attack boxes mark adversarial pathways; blue arrows depict ordinary exchanges. Repetition labels indicate multiple interactions. The malicious-environment attack box lists objective drifting, task injection, and memory poisoning. On the left, the diagram labels an attack Tool Hijacking, whereas Table 1 and prose use Intent Hijacking. This naming difference is retained as a discrepancy.

The rightmost trace box records environment information plus instructions, calls, observations, and responses. An evaluator beneath it assesses utility and security. The figure supports the central point that evaluation must follow an interaction trajectory and environmental state changes. It does not quantify performance, contain error bars, or define a model-comparison result. The image resolves arrows obscured by extraction artifacts in the supplied text.

### Figure 2 — Coordinated attack-generation framework, p. 4

**Visually inspected.** A planner sends an attack plan to an attacker. A verifier connects to the planner through tool-call checking and verification. The attacker sends attack execution to the target LLM agent and receives agent responses. A judge evaluates attack behavior, and feedback loops labeled Refine and Optimize support iterative improvement. The figure separates the adversarial team from the target agent.

The main methodological insight is that attacks are generated and revised rather than fixed once. The optional verifier checks feasibility in the target environment; the judge checks attack achievement. These roles should not be confused with independent scientific replication. There are no numerical axes or timing measurements.

### Figure 3 — Task-injection trajectory, p. 4

**Visually inspected.** The planner block contrasts a benign webpage-reading task with unauthorized Slack user-management actions. Three stages move from a webpage injection to an inbox injection and then an attacker-controlled URL presenting malicious tools as a fix. Fake tokens and role delimiters make retrieved data resemble authoritative dialogue or system policy.

The result sequence moves from reading a webpage to reading an inbox and then invoking Slack actions. This illustrates a fabricated dependency chain: to complete the original task, the agent is told it must perform unrelated operations. Although the figure is located near the tool-chaining discussion, its caption explicitly identifies Task Injection, consistent with §4.2.4 and Appendix B.4. The figure is an example, not a plot of success frequency.

### Figure 4 — Memory poisoning across ingestion and exploitation, p. 5

**Visually inspected.** The upper phase shows routine email, code, and product content carrying hidden preference-like text. The middle box shows compromised memory entries about automated uploads and file-publication preferences. The lower phase shows a later request to post file lines; retrieved memories provide an uploading precedent, followed by publication of a line containing sensitive data.

Warning icons mark poisoned entries. The process distinguishes the initial input source, the persistent memory state, and later action. It supports the claim that unsafe behavior can occur after the original injection is no longer immediately visible in the active task. No ingestion success probability or detection rate is encoded. Exact example wording is compressed because its role is mechanistic, not a separately measured numerical result.

### Figure 5 — Distribution across risk categories, p. 6

**Visually inspected.** This is a horizontal bar chart. The x-axis is Count, with labeled ticks from 0 to 175; the y-axis lists nine categories. The scale is linear. Bars have different colors to distinguish categories, with exact count-and-percentage labels at their ends. No error bars or confidence intervals appear.

| Category | Count | Displayed share |
|---|---:|---:|
| Privacy Breach | 152 | 23.6% |
| Financial Loss | 137 | 21.3% |
| Miscellaneous Risks | 116 | 18.0% |
| Computer Security Compromise | 77 | 12.0% |
| Safety Hazards & Physical Harm | 62 | 9.6% |
| Inaccurate & Inefficient Execution | 53 | 8.2% |
| Data Loss & Corruption | 21 | 3.3% |
| Legal & Compliance Violations | 17 | 2.6% |
| Reputational Damage | 9 | 1.4% |

These are **[B] visually readable values**, also reproduced in the supplied extraction. **[C]** The counts sum to 152 + 137 + 116 + 77 + 62 + 53 + 21 + 17 + 9 = 644. The chart demonstrates breadth but an uneven category distribution. It does not show how categories intersect attack types. The introduction says ten risk categories, whereas this chart and §4.3.2 specify nine.

### Figure 6 — Success rate versus turns to success, p. 7

**Visually inspected.** Five scatterplot panels correspond to intent hijacking, tool chaining, objective drifting, task injection, and memory poisoning. The shared y-axis is ASR (%) on a linear 0–100 scale. The shared x-axis is T2S (Average), also linear, with different displayed ranges by panel. Visible tick labels are approximately 4–6, 8–14, 6–10, 1–5, and 9–11 respectively; precise panel boundaries are not needed to infer the trends and are not asserted.

Legend encodings are orange circles for Qwen, blue squares for Llama, green diamonds for GPT-4o, dark teal triangles for GPT-5.1, purple plus-like markers for Gemini, and coral cross-like markers for Claude. Upper-left means successful attacks with fewer turns; lower-right means lower success and more turns among successful cases. No error bars appear.

Tool chaining clusters at high ASR despite requiring more turns than intent hijacking. Objective drifting is highly model-dependent. Task injection ranges from near-zero to above 90%, with vulnerable targets generally reached quickly. Memory poisoning shows substantial success even for models that resist another attack family. Exact ASR values should be taken from Table 2, not estimated from point positions.

The prose explicitly reports Qwen T2S as 4.6 for intent hijacking and 8.5 for tool chaining. Other exact T2S values are not labeled. Claude's task-injection point lies at zero ASR, yet a horizontal position is displayed. Since T2S is defined over successful attacks, its value at zero successes is undefined unless a convention is specified; none is supplied. That point's x-coordinate must not be treated as an interpretable successful-attack average.

### Figure 7 — Attack-turn budget ablation, p. 8

**Visually inspected.** Two line panels show intent hijacking and task injection. The y-axis is ASR (%) from 0 to 100; the x-axis is Allowed Number of Turns. Orange circle-marked lines represent Qwen; green diamond-marked lines represent GPT, identified by the caption as GPT-4o. The intent-hijacking panel spans approximately zero to seven allowed turns; task injection spans zero to five. No uncertainty bands appear.

Both curves rise and eventually flatten. The author text reports GPT-4o task injection from 0% at zero turns to about 80% at five turns, and Qwen at approximately 90% by three turns. These are reported approximate descriptions, not exact digitized coordinates. The figure supports sensitivity to interaction opportunity. It does not by itself demonstrate that all five attack families behave identically.

### Figure 8 — Optimization-step budget ablation, p. 8

**Visually inspected.** The same model colors and two attack panels are used. The y-axis is ASR (%) from 0 to 100; the x-axis is allowed optimization steps. Intent hijacking displays roughly one through seven steps; task injection displays zero through five. Curves generally improve and then plateau, with task injection on Qwen remaining near a high plateau after the early increase.

The authors interpret these gains as more gradual than those from additional attack turns. The graph supports that qualitative reading, but no fitted effect size or formal comparison is supplied. Page 8 incorrectly refers to additional-turn gains in Figure 5; the relevant turn-budget figure is Figure 7. Exact point-by-point values are not supplied and are not invented here.

## 11. Table-by-table interpretation

### Table 1 — Attack taxonomy, p. 4

Rows are attack families; columns identify adversary, strategy, and vector. Intent hijacking and tool chaining use a malicious user and adversarial prompting. Objective drifting, task injection, and memory poisoning use an environmental adversary and indirect prompt injection. Strategies differ: executing a malicious task, composing benign calls, shifting an objective, adding malicious work, or persisting malicious influence in memory.

Merged cells visually group the first two and last three families. This grouping is readable in the image and should not be mistaken for missing adversary entries in extracted text. The taxonomy establishes attack locations and mechanisms; it has no numerical performance or uncertainty columns.

### Table 2 — Unprotected attack effectiveness, p. 6

Rows are the six target agents. The first five numerical columns are attack-specific ASR percentages; the last is a reported overall value. All 36 values are preserved in §9. A larger number is worse for the defender. No bold significance designation, confidence interval, sample count, or missing-value symbol appears.

Tool chaining is the highest-ASR attack within each displayed target row. Gemini's memory poisoning exceeds its intent hijacking, objective drifting, and task injection. Claude's zero task-injection result coexists with substantial susceptibility elsewhere. These patterns challenge a single scalar description of safety. The undefined overall aggregation and GPT-5.1 arithmetic discrepancy limit interpretation of the last column.

### Table 3 — One-shot baseline comparison, p. 7

Rows are target agents; columns give one-shot and long-horizon injection ASR percentages. The baseline is the important-message attack, which asks the agent to prioritize malicious work over legitimate work. All 12 values are preserved in §9. Long-horizon rates are higher for five agents, with a zero–zero tie for Claude. No statistical uncertainty or resource-matching information is provided.

The Llama label and 86.8% value differ slightly from Table 2's Llama-3.1 label and 86.6%. Appendix A.4 also mentions 5.56% for traditional injections in AgentDojo; that is a separately contextualized figure and must not replace the model-specific Table 3 baseline values.

### Table 4 — Baseline defenses, p. 8

Each attack has a triplet of conditions. The slash means no defense. For intent hijacking and tool chaining, triplets are **none / Self-Reminder / Llama-Guard**. For the other three, triplets are **none / Repeated Prompt / DeBERTa Detector**. Every entry below is an author-reported ASR percentage; lower is better for the defender.

| Agent | Intent hijacking: none/SR/LG | Tool chaining: none/SR/LG | Objective drifting: none/RP/DD | Task injection: none/RP/DD | Memory poisoning: none/RP/DD |
|---|---|---|---|---|---|
| Qwen-3 | 78.1 / 41.4 / 73.3 | 96.3 / 81.5 / 48.2 | 92.2 / 69.0 / 25.3 | 93.1 / 95.1 / 6.9 | 48.0 / 32.4 / 41.2 |
| Llama-3.1 | 53.3 / 24.1 / 50.0 | 90.4 / 76.0 / 66.5 | 67.4 / 37.9 / 19.8 | 86.8 / 68.1 / 35.4 | 34.6 / 24.3 / 30.9 |
| GPT-4o | 74.0 / 39.3 / 71.0 | 94.1 / 82.4 / 64.7 | 79.2 / 51.7 / 13.3 | 79.9 / 66.7 / 12.7 | 63.3 / 56.8 / 31.6 |
| GPT-5.1 | 59.8 / 20.7 / 55.4 | 94.6 / 75.7 / 48.6 | 73.7 / 31.0 / 7.8 | 21.5 / 20.8 / 2.8 | 51.3 / 27.0 / 38.5 |
| Gemini-3 | 46.2 / 10.3 / 46.4 | 95.9 / 61.2 / 49.0 | 15.8 / 10.3 / 15.8 | 43.1 / 31.9 / 13.8 | 67.3 / 43.2 / 55.1 |
| Claude-4.5 | 27.2 / 6.9 / 24.7 | 73.3 / 57.9 / 46.7 | 5.3 / 0.0 / 5.3 | 0.0 / 0.0 / 0.0 | 38.8 / 8.1 / 32.7 |

Within every intent-hijacking row, Self-Reminder produces the lowest displayed rate. Within every tool-chaining row, Llama-Guard produces the lowest displayed rate. DeBERTa Detector is lower than Repeated Prompt for objective drifting in the first four rows, but Repeated Prompt is lower for Gemini and Claude. For task injection, DeBERTa Detector is best for the first five rows; Claude ties at zero across all three conditions. For memory poisoning, Repeated Prompt is lower than DeBERTa Detector for every model except GPT-4o.

These **[B] observable rankings** reveal a tradeoff hidden by a general defense-success statement: the best baseline changes with both attack and target. No universal defense ranking follows. The table does not report legitimate-task utility, classifier false positives, confidence intervals, or overhead.

## 12. Diagram / Architecture Interpretation

Figures 1–4 jointly describe three different levels of process. Figure 1 is the **benchmark system**: user and adversary input, target agent, mutable environment, recorded trace, and outcome evaluator. Figure 2 is the **attack-construction system**: planner, attacker, verifier, judge, and refinement loops. Figures 3–4 are **attack trajectories**, showing how malicious influence crosses interfaces over time.

The ordinary data path is user instruction → target decision → tool invocation → updated environment and observation → target response. An environmental attacker changes what returns along the observation path. A user attacker changes what enters through the instruction path. An attack-generation feedback loop observes the resulting behavior and revises the next prompt or observation. An evaluator then assesses whether the final trajectory accomplished benign and malicious objectives.

The memory-poisoning diagram adds another path: environmental content → preference extraction → persistent memory → later retrieval → future target decision. The temporal separation is the key architectural feature; the harmful action need not happen during the original ingestion session. The attacker-side exemplar bank in Algorithms 1–2 is different: it stores successful attack examples to improve the attacker, rather than poisoning the defender's preferences.

**[D]** For web-agent security, the diagrams show why checking a single input string or a single tool invocation may be insufficient. An authorization-relevant sequence can span several inputs, tools, and memory retrievals. The paper supplies demonstrations and benchmark outcomes supporting this concern, but it does not propose or evaluate a complete sequence-level authorization architecture.

## 13. Equations and mathematical concepts

### Equation (1): interaction trace, p. 2

The trace is written as ⟨p1, a1, o1, r1⟩ … ⟨pi, ai, oi, ri⟩ … ⟨pn, an, on, rn⟩. P, A, O, and R are respectively the spaces of user prompts, actions, observations, and responses. At step i, pi is an instruction, ai an action such as a tool call, oi the resulting environmental observation, and ri a response to the user. n indexes the length of the trace.

This is a structured sequence, not an optimization equation or probability model. It defines where attacks enter: replace selected pi with pi*, or selected oi with oi*. Its output is a record of interactions for evaluation. The authors say it generalizes settings where the user gives only an initial instruction. The precise bookkeeping for absent subsequent user prompts is not specified.

### Task-injection generation expressions, p. 13

The appendix writes {ô} = A(T, {a}, {â}) and {o*} = A(T, T*, {a}, {â}, {a*}). Here T is the legitimate task; T* is the adversarial task; {a} is the legitimate tool sequence; {â} is an intermediate sequence; and {a*} is the adversarial sequence. A generates the bridge snippet {ô} and malicious-stage snippet {o*}. In the original notation, the intermediate symbols carry hats rather than a distinct alphabet.

Plainly, the attacker first explains why an intermediate action appears necessary, then constructs content that moves the agent toward the harmful sequence. The harmful task need not be quoted explicitly in the final snippet; a progressive rationalization may be used instead. The braces sometimes denote sequences and sometimes collections, so an ordered-sequence interpretation comes from the prose rather than formal set notation alone.

The execution expression M = L(T, {ô}, {o*}) denotes running target agent L and collecting its trajectory and reasoning diagnostics M. Rewriting model R uses M to revise failed stages. These appendix uses of A and R differ from the prompt/action/observation/response spaces introduced earlier; their local meanings must be kept separate.

### Algorithm 1: hierarchical exemplar retrieval, p. 14

Inputs are attack memory bank B, user task Ti, adversarial task Tj*, maximum exemplar count ne, and static human-written examples Estatic. The output is exemplar collection E. It first retrieves successes sharing either the user task or adversarial objective. If fewer than ne are selected, it samples additional entries from the remaining bank. If E is empty, it falls back to static examples.

Two details are unresolved. The code does not explicitly trim a related-example set already larger than ne. It also does not specify how sampling behaves if too few remaining entries exist, including an empty bank before fallback. The bank is described as storing task-tagged successful instances, while the retrieval expression selects snippet pairs; the exact storage representation is not fully formalized.

### Algorithm 2: adaptive long-horizon injection, p. 14

Across up to Ni iterations, the algorithm retrieves exemplars, generates bridge and malicious snippets, and runs the target within up to Nr rewrite cycles. If the intermediate actions fail, R rewrites the bridge snippet. If the bridge succeeds but malicious actions fail, R rewrites the malicious snippet. Otherwise, it adds the successful task-and-snippet tuple to B and returns. Exhausting the budget returns the latest snippets without an explicit success guarantee.

The else branch assumes that reaching neither failure condition establishes success. How partial completion, malformed calls, or unrelated execution are classified depends on diagnostics not specified in the pseudocode. With Nr = 1, a revised snippet may require the next outer iteration or another evaluation procedure; whether the last revised snippet is retested before final return is not explicitly shown.

### Poisoning objective and drift measurement

Page 15 states evasiveness/effectiveness weights of 0.4 and 0.6 but supplies no complete loss equation, normalization, or effectiveness scale. It would be inappropriate to invent one. Page 12 names frugality score and mean purchase price as drift measures, but gives no formula for frugality. Page 17 reports scores 1.0 and 0.22 in one example. These are reported quantities with an unspecified computation, not enough evidence to reconstruct the metric.

## 14. Interpretation and discussion

**[A]** The authors conclude that extended attacks expose vulnerabilities that one-shot-oriented safeguards fail to address reliably. Tool chaining is particularly revealing: the target can resist a direct harmful request yet comply with smaller actions whose composition achieves the same harmful outcome. Sources: §5.2, p. 7; §6, p. 8.

**[D] Research-question interpretation:** The supplied evidence suggests five reasons web-capable agents may face greater security exposure than a standalone answering model: repeated encounters with attacker-controlled content; conversion of model decisions into tool actions; harmful composition across individually ordinary operations; goal drift as observations accumulate; and persistent contamination through external memory. These mechanisms are represented by Table 1, Figures 1–4, and Appendix B. They do not quantify the incremental vulnerability caused by adding browsing or memory to an otherwise identical standalone model.

The long-horizon comparison shows an association between the implemented richer attack and higher success. Because it changes multiple elements together, it does not prove that elapsed interaction count alone causes the whole increase. The turn-budget ablation supplies more focused evidence about opportunities for attack, but is limited to two plotted attacks and two models.

Several source inconsistencies affect interpretation: nine versus ten risk categories; GPT-5.1's overall aggregation; Llama task-injection values of 86.6% versus 86.8%; Figure 1's Tool Hijacking label; the Figure 5 cross-reference in the ablation discussion; black-/white-/grey-box terminology; and the objective-drifting command restriction. These are documented rather than silently harmonized.

Appendix examples also contain inconsistencies. Page 16 describes the preceding intent demonstration as using a credible academic persona and educational framing, although p. 15 shows an internal auditor using compliance framing. Page 17 states a 3.6-times price increase in its displayed example but then describes decisions shifting toward 2–3-times more expensive options. These could describe different levels of generalization, but the supplied material does not explain the relationship.

The memory demonstration's categorical statement that injections are undetectable should not be interpreted as proven universal impossibility of detection. The benchmark includes defenses that reduce memory-poisoning success, and the example itself is qualitative. The appropriately bounded conclusion is that the demonstrated ingestion path accepted apparently benign preference-like content and later enabled sensitive publication.

## 15. Contributions and novelty

| Contribution type | Author claim and concrete artifact | Qualification |
|---|---|---|
| Conceptual | Unified taxonomy of five long-horizon attack families, Table 1. | Organizes mechanisms; categories have antecedents discussed in related work. |
| Methodological | Coordinated planner/attacker/judge framework, with optional verifier, Figure 2. | Adapted from cited approaches; independent novelty comparison was not conducted. |
| Algorithmic | Adaptive task injection with bridge actions and hierarchical exemplar reuse, Algorithms 1–2. | Pseudocode and model settings are supplied, but implementation edge cases remain unspecified. |
| Benchmark/data | 644 tasks in 28 environments, risk distribution in Figure 5. | Environment and per-family case allocations are not supplied. |
| Systems | Modular agent, environment, task, and attack interfaces, Figure 1. | Repository and deployed benchmark were not inspected. |
| Empirical | Six-model evaluation, one-shot comparison, two budget ablations, baseline defense tests. | Preliminary, descriptive results without uncertainty estimates. |

The authors claim this is the first benchmark dedicated to adaptive long-horizon agent attacks. That priority claim is **[A]**, not independently verified. The work does not present a theorem, a trained defensive model, or a validated universal solution to the attacks it measures.

## 16. Limitations

### Authors' stated limitations and qualifications

The supplied paper does not include a dedicated limitations section. It explicitly describes its evaluation as **preliminary** (§5, p. 6), and repeatedly states that AgentLAB **currently** supports five attack families and its present environment/task inventory. Its live-benchmark and extensibility framing indicates that this inventory can expand. These are explicit qualifications, not a comprehensive author-provided threats-to-validity analysis.

The authors also state that existing defenses are effective for specific attacks but not consistently across agents or families (§5.4, p. 8). This qualifies the defense conclusion: some tested configurations provide large reductions, so the result is not that all existing defenses always fail.

### Additional evidence-based analyst observations

**[D]** The absence of a matched standalone-model baseline prevents a direct comparative answer to the user's question. Missing exact target versions, complete prompts, repetitions, seeds, per-condition counts, utility tables, and uncertainty estimates constrain reproducibility and statistical interpretation. Missing definitions of frugality and overall aggregation constrain metric reconstruction.

**[D]** GPT-5.1 plays several roles in task curation, attack generation, and judging. This may create correlated preferences or evaluation behavior, although the supplied work does not establish that such bias occurred. Programmatic validation and manual review provide safeguards, but judge agreement and error rates are not reported.

**[D]** Unequal category counts and unknown attack-family allocations make broad benchmark averages difficult to interpret. Privileged reasoning access in task injection may differ from real deployment visibility. Persistent attacker exemplar reuse raises questions about attack ordering and cross-case information flow, but does not establish improper leakage without a specified protocol.

**[D]** Appendix B's harmful-content demonstration is compressed here to its file-operation and distribution mechanism. Operational weapon-construction detail is unnecessary to explain the paper's result and is not reproduced. This omission does not remove the substantive observation that literal file processing can carry harmful content through ordinary tool operations.

## 17. Threats to validity

The following categories are **analyst observations**, not headings or admissions attributed to the authors.

| Validity category | Evidence-based concern | Consequence |
|---|---|---|
| Internal validity | One-shot and long-horizon attacks differ in strategy, intermediate steps, adaptivity, and likely resources. | Their ASR difference cannot be assigned solely to duration. |
| Construct validity | Maliciousness is validated using GPT-5.1 refusal; frugality lacks a formula; overall ASR aggregation is unclear. | The measured constructs may reflect specific monitors or implementation choices. |
| Statistical conclusion validity | No intervals, repeated-run variation, or significance tests. | Small changes, including defense-associated increases, cannot be confidently distinguished from variation. |
| External validity | Selected model configurations, environments, and attack families; exact versions incomplete. | Results do not automatically generalize to all agents or production permissions. |
| Ecological validity | Realistic tools and state are used, but deployment authorization, human review, and external enforcement are not detailed. | Benchmark success may not correspond directly to real-world harm frequency. |
| Reproducibility | Missing prompts, execution environment, detector training settings, seeds, and case allocations. | The supplied paper alone is insufficient for exact replication. |
| Evaluation independence | Shared model family across curation, attack, and judging; no judge-calibration statistics. | Potential correlated evaluation behavior remains unmeasured. |
| Generalizability to standalone comparison | No equivalent standalone target experiment. | Relative vulnerability is a mechanism-based inference, not an estimated comparative effect. |

The authors' manual validation, programmatic success checks, ground-truth task sequences, and clean baselines provide methodological support. These measures reduce some ambiguities but do not replace the missing information listed above.

## 18. Future work and open questions

### A. Explicitly proposed by the authors

The authors envision AgentLAB as a live benchmark that supports additional environments, attack categories, agents, and defenses. They call for defense mechanisms tailored to long-horizon attacks and anticipate using the benchmark to track security progress. Sources: p. 1; §4.3.2, p. 6; §§5.4–6, p. 8. No detailed research schedule or proposed defense algorithm is supplied.

### B. Additional open questions from this analysis

**[D]** What is the incremental effect of adding browsing, tools, planning, or memory to the same underlying model under equal attack budgets? Does reasoning-trace visibility materially change task-injection success? How much benign-task performance do the tested defenses sacrifice? Do sequence-level controls prevent compositional harm better than input classification? How durable are poisoned memories, and can provenance-aware retrieval contain them?

**[D]** How do success rates vary by environment and risk category? What are confidence intervals under repeated trials? What aggregation produces GPT-5.1's reported overall rate? What exact formula defines frugality? How is the attacker bank initialized and reset across evaluations? These are unresolved questions supported by omissions or inconsistencies in the supplied material, not claims of implementation failure.

## 19. Terminology and notation glossary

| Term or symbol | Beginner-friendly meaning and source-boundary note |
|---|---|
| LLM | Large language model; the text-generating backend of an agent. |
| AgentLAB | Agent Long-horizon Attack Benchmark. |
| Agent | Model plus capabilities for interacting with an environment. |
| Environment | Application context with tools and mutable state. |
| API | Application programming interface; the callable tool interface described by the paper. |
| Long-horizon | Extending across several interactions or sessions. |
| Adaptivity | Revising the attack after feedback. |
| Red-teaming | Deliberately attempting harmful behavior to assess security. |
| Indirect prompt injection | Malicious influence delivered through outside content or tool output. |
| Intent hijacking | Contextual persuasion that redirects the agent toward harmful execution. |
| Tool chaining | Combining ordinary-looking tool calls into a harmful sequence. |
| Objective drifting | Gradual movement away from the legitimate user's goal. |
| Task injection | Adding unauthorized work during legitimate task execution. |
| Memory poisoning | Storing false contextual information that later changes behavior. |
| ASR | Attack Success Rate: fraction of cases fully achieving the malicious objective. |
| T2S | Turn to Success: average turns among successful attacks. |
| SR / LG | Self-Reminder / Llama-Guard. |
| RP / DD | Repeated Prompt / DeBERTa Detector. |
| RAG | Capability label in Figure 1; not expanded in the supplied work. |
| SOX | Compliance acronym used in Appendix B.1; not expanded in the supplied work. |
| P, A, O, R | Spaces of prompts, actions, observations, and responses in §3. |
| p, a, o, r | Individual prompt, action, observation, and response. |
| T / T* | Legitimate task / adversarial task. |
| p* / o* | Adversarial prompt / observation. |
| {a} / {â} / {a*} | Legitimate, intermediate, and adversarial tool sequences in A.4. |
| {ô} / {o*} | Bridge and malicious-stage observation snippets. |
| A / R / L in A.4 | Adversarial generator, rewriting model, and target agent; locally overloaded notation. |
| M | Target execution trajectory and diagnostics. |
| B | Attacker's bank of successful examples, distinct from poisoned defender memory. |
| E / Estatic | Retrieved exemplars / fallback human-written examples. |
| ne / Ni / Nr | Maximum exemplars / optimization iterations / rewrites. |
| nturn / nopt | Allowed interaction turns / allowed optimization steps. |
| Temperature | Model-generation setting reported for planner/judge diversity or determinism; no detailed mathematical definition supplied. |
| Frugality score | Named shopping objective measure; formula unspecified. |

## 20. Key numerical results

The complete attack and defense matrices appear in §§9 and 11. This compact ledger preserves configuration, dataset, example, and derived facts that would otherwise be easy to overlook.

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| Environments | 28 | environments | Current benchmark | Author-reported | pp. 1, 6 |
| Security cases / malicious tasks | 644 | cases/tasks | Current benchmark | Author-reported | pp. 1, 6 |
| Attack families | 5 | families | Current taxonomy | Author-reported | Table 1, p. 4 |
| Risk categories | 9 versus 10 | categories | Statistics/chart versus introduction | Author-reported discrepancy | pp. 2, 6 |
| Risk count total | 644 | tasks | Sum of nine chart counts | Analyst-derived | Figure 5, p. 6 |
| Default planner temperature | 0.5 | setting | GPT-5.1 | Author-reported | p. 6 |
| Default judge temperature | 0 | setting | GPT-5.1, greedy decoding | Author-reported | p. 6 |
| Default maximum turns | 7, 20, 15, 5, 12 | turns | Listed sequence; mapping inferred from order | Author-reported values | p. 6 |
| Task-injection exemplar count | 2 | exemplars | ne | Author-reported | p. 13 |
| Task-injection iterations | 5 | iterations | Ni | Author-reported | p. 13 |
| Task-injection rewrites | 1 | rewrite | Nr | Author-reported | p. 13 |
| Poisoning planner temperature | 0.7 | setting | GPT-5.1 | Author-reported | p. 14 |
| Poisoning strategies | Up to 3 | strategies/scenario | Planner | Author-reported | p. 14 |
| Poisoning payload length | At most 15 | words | Preference statements | Author-reported | p. 14 |
| Poisoning conversational turns | Up to 5 | turns/strategy | Payload refinement | Author-reported | p. 14 |
| Evasiveness gate | 3.5 of 5 | score | Minimum to proceed | Author-reported | p. 14 |
| Poisoning optimization rounds | Up to 4 | rounds | Joint optimization | Author-reported | p. 15 |
| Objective weights | 0.4 / 0.6 | weights | Evasiveness / effectiveness | Author-reported | p. 15 |
| Tool-chaining ASR range | 73.3–96.3 | percent | Six targets, unprotected | Visually readable | Table 2, p. 6 |
| GPT-5.1 reported overall | 69.9 | percent ASR | Undefined aggregate | Author-reported | Table 2, p. 6 |
| GPT-5.1 unweighted mean | 60.18 | percent ASR | (59.8+94.6+73.7+21.5+51.3)/5 | Analyst-derived | Table 2, p. 6 |
| GPT-4o injection increase | 17.4 | percentage points | 79.9−62.5 | Analyst-derived | Table 3, p. 7 |
| GPT-5.1 injection increase | 19.42 | percentage points | 21.5−2.08 | Analyst-derived | Table 3, p. 7 |
| Qwen intent / chaining T2S | 4.6 / 8.5 | turns | Successful attacks | Author-reported | p. 7 |
| GPT-4o task-injection ablation | About 80 | percent ASR | Maximum five turns | Author-reported approximate | p. 7; Figure 7 |
| Qwen task-injection plateau | Approximately 90 | percent ASR | Around three allowed turns | Author-reported approximate | p. 7; Figure 7 |
| Traditional injection reference | 5.56 | percent success | AgentDojo context in appendix; separate from Table 3 | Author-reported | p. 13 |
| Shopping price constraint | Less than 70 | dollars | Example requirement | Author-reported | p. 17 |
| Shopping baseline / attacked price | 13.71 / 49.99 | dollars | Single paired demonstration | Author-reported | p. 17 |
| Shopping frugality scores | 1.0 / 0.22 | score | Baseline / attacked; formula absent | Author-reported | p. 17 |
| Shopping price increase | 36.28 | dollars | 49.99−13.71 | Analyst-derived | p. 17 |
| Shopping price ratio | Approximately 3.65 | times | 49.99/13.71 | Analyst-derived | p. 17 |
| Shopping injection touchpoints | 3 / 4 | injections | Search / product page example | Author-reported | p. 17 |
| Intent demonstration endpoint | Turn 5 | turn | Organization-wide deletion example | Author-reported | p. 15 |
| Task-injection stages | 3 | coordinated snippets | Webpage, inbox, attacker URL | Author-reported | pp. 17–18 |

For the shopping example, prices seen in the baseline are $13.71, $14.16, $17.62, $19.68, $49.99, and $59.99. The displayed attacked trajectory is not a fully enumerated identical list, despite prose describing unchanged task specifications and biased framing. The 3.65-times ratio is independently derivable; the reported frugality score 0.22 cannot be reconstructed from a supplied formula.

## 21. Claim–evidence map

| Claim | Evidence | Figure/table/experiment | Source | Qualification / evidence strength |
|---|---|---|---|---|
| AgentLAB covers five attacks and a substantial case inventory. | Five families; 28 environments; 644 cases. | Table 1; Figure 5 | pp. 1, 4, 6 | HIGH for reported scope; category-count inconsistency remains. |
| Attacks can enter through user instructions or environmental observations. | Formal substitution models. | Equation (1); Figure 1 | pp. 2–3 | HIGH for specified threat model; deployment permissions unspecified. |
| Attacks are generated and refined through cooperating agents. | Planner, attacker, judge, optional verifier. | Figure 2 | pp. 4, 12–14 | HIGH for method description; repository not inspected. |
| Tool composition is a major tested weakness. | ASR 73.3%–96.3% across targets. | Table 2; X1 | p. 6 | HIGH for table values; no uncertainty intervals. |
| Long-horizon injection outperforms the chosen one-shot baseline for most targets. | Five positive differences and one zero tie. | Table 3; X2 | p. 7 | HIGH descriptive support; not a matched standalone comparison. |
| Vulnerability is attack-specific. | Claude 0.0% task injection, 73.3% chaining, 38.8% poisoning. | Table 2; Figure 6 | pp. 6–7 | HIGH for reported pattern; causal guardrail explanation is author interpretation. |
| More turns increase success in displayed ablations. | Rising/plateauing Qwen and GPT-4o curves. | Figure 7; X4a | pp. 7–8 | HIGH qualitative visual support for two attacks; broader claim incompletely displayed. |
| Optimization adds gains but apparently less than interaction budget. | Figure 8 compared with Figure 7. | X4b | p. 8 | MEDIUM: qualitative comparison, no formal effect-size test. |
| Existing defenses have uneven effectiveness. | Full defense matrix, including strong reductions and residual successes. | Table 4; X5 | p. 8 | HIGH descriptive support; utility and uncertainty missing. |
| Poisoning can influence later sessions without direct memory access. | A.5 threat model and two-phase example. | Figure 4; B.5 | pp. 5, 13–15, 18–19 | HIGH for proposed method; qualitative example does not prove universal undetectability. |
| Reported GPT-5.1 overall is arithmetically unresolved. | Family mean 60.18% versus reported 69.9%. | Table 2 | p. 6 | HIGH for arithmetic; correct aggregation UNKNOWN. |
| Web-agent relevance is additional action, observation, and memory exposure. | Environmental attacks, tool execution, persistence. | Figures 1–4; A.3–A.5 | pp. 3–5, 12–15 | MEDIUM analyst inference; relative standalone effect unmeasured. |

## 22. Very simple explanation — Explain Like I'm 15

Imagine an assistant that can read websites, send emails, change files, and remember your preferences. A normal chatbot mostly gives you words. This assistant can also do things. That makes it useful, but it gives an attacker more places to interfere: a webpage, an email, a tool result, or something the assistant saves for later.

The paper studies attacks that work gradually. Instead of asking for one obviously harmful action, an attacker can build a convincing story, ask for several ordinary-looking steps, invent a policy that requires unrelated work, or repeatedly nudge shopping choices. Another attack plants a false preference in memory so that a later request seems more acceptable. The danger can lie in the whole sequence even when one step looks harmless.

The researchers tested six kinds of model-powered agents. Some attacks worked often, especially chains of tool calls. A model that resisted one attack could still fail another. Safety reminders and content detectors helped in some cases, but their effectiveness depended on both the model and the attack.

This helps explain why web agents may have extra security weaknesses, but the paper did not directly test the same model as both a standalone chatbot and a web agent under equal conditions. Its strongest result is that long, adaptive interactions create important vulnerabilities in the agents it tested. Several missing details and numerical inconsistencies also mean its exact averages and broadest conclusions require care.

## Completeness Audit

This audit uses the inventory in §2 as its denominator. Fully represented means the substantive content needed for this analysis is covered; it does not mean every sentence has been reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| ABS, title, authors, publication note | Yes; text and p. 1 image | Yes | Fully represented | Both displayed dates retained. |
| S1 Introduction and C1–C4 contributions | Yes; mixed visual/text | Yes | Fully represented | Principles, scope, priority claim and category discrepancy included. |
| S2 Related Work | Yes; text only | Yes | Represented in compressed form | Three categories and principal benchmark positioning retained. |
| S3 Problem Formulation | Yes; p. 2 text, p. 3 image | Yes | Fully represented | Equation, substitutions, and access distinctions covered. |
| SS41 Components | Yes; text and image | Yes | Fully represented | All four components and evaluator covered. |
| SS42 Shared framework | Yes; text and image | Yes | Fully represented | Planner, attacker, judge, verifier, feedback represented. |
| SS421 Intent hijacking | Yes; text and image | Yes | Fully represented | Mechanism and TextGrad refinement covered. |
| SS422 Tool chaining | Yes; text and image | Yes | Fully represented | Decomposition, verification, adaptation covered. |
| SS423 Objective drifting | Yes; text and image | Yes | Fully represented | Goal shift and shopping mechanism covered. |
| SS424 Task injection | Yes; text and image | Yes | Fully represented | Intermediate actions and contextual narratives covered. |
| SS425 Memory poisoning | Yes; text and image | Yes | Fully represented | Ingestion and exploitation phases covered. |
| SS431 Data curation | Yes; text and image | Yes | Fully represented | Sources, maliciousness monitor, manual checks, benign pairs covered. |
| SS432 Data statistics | Yes; text and image | Yes | Fully represented | All nine chart counts and percentages preserved. |
| SS51 Experimental setting | Yes; text and image | Yes | Fully represented | Target models, defaults, metrics, missing configurations covered. |
| SS52 Attack effectiveness | Yes; text and images | Yes | Fully represented | Tables 2–3, Figure 6, qualifications covered. |
| SS53 Ablations | Yes; text and images | Yes | Fully represented for supplied evidence | Only two attacks plotted; wider statement flagged. |
| SS54 Defenses | Yes; text and image | Yes | Fully represented | All Table 4 values and defense definitions preserved. |
| S6 Conclusion | Yes; text and image | Yes | Represented in compressed form | Main conclusion and benchmark aspiration retained. |
| Formal research questions | No formal list present | Accounted for | Fully represented | Objectives distinguished from user question. |
| Formal hypotheses | None supplied | Accounted for | Fully represented | No hypotheses invented. |
| X1 Cross-model effectiveness | Yes | Yes | Fully represented | Complete numerical matrix. |
| X2 One-shot comparison | Yes | Yes | Fully represented | Complete matrix and labeled differences. |
| X3 ASR/T2S analysis | Yes | Yes | Represented in compressed form | Exact reported T2S retained; unlabeled coordinates not digitized. |
| X4a Turn-budget ablation | Yes | Yes | Represented in compressed form | Trends, axes, approximate author descriptions retained. |
| X4b Optimization-budget ablation | Yes | Yes | Represented in compressed form | Trends and inferential limits retained. |
| X5 Defense evaluation | Yes | Yes | Fully represented | Complete matrix and conditions. |
| F1 Overall framework | Yes; visual | Yes | Fully represented | Extraction artifacts and naming difference addressed. |
| F2 Attack framework | Yes; visual | Yes | Fully represented | Control and feedback paths explained. |
| F3 Task injection | Yes; visual | Yes | Represented in compressed form | Dependency mechanism retained; payload wording shortened. |
| F4 Memory poisoning | Yes; visual | Yes | Represented in compressed form | Two-phase mechanism retained. |
| F5 Risk distribution | Yes; visual | Yes | Fully represented | All exact labels retained. |
| F6 Five scatter panels | Yes; visual | Yes | Represented in compressed form | All panels, axes, legends, trends and zero-success issue covered. |
| F7 Two turn-budget panels | Yes; visual | Yes | Represented in compressed form | No invented exact coordinates. |
| F8 Two optimization panels | Yes; visual | Yes | Represented in compressed form | Plateau and cross-reference issue covered. |
| T1 Taxonomy | Yes; visual/text | Yes | Fully represented | Merged-cell meanings explained. |
| T2 Effectiveness | Yes; visual/text | Yes | Fully represented | Every value preserved; overall anomaly flagged. |
| T3 Baseline comparison | Yes; visual/text | Yes | Fully represented | Every value preserved; Llama discrepancy flagged. |
| T4 Defenses | Yes; visual/text | Yes | Fully represented | Every value preserved. |
| E1 Interaction equation | Yes; text only | Yes | Fully represented | No claim of visual inspection on p. 2. |
| EA4 Generation/execution expressions | Yes; visual/text | Yes | Fully represented | Local notation and assumptions explained. |
| ALG1 Retrieval | Yes; visual/text | Yes | Fully represented | Procedure and unresolved edge cases covered. |
| ALG2 Adaptive injection | Yes; visual/text | Yes | Fully represented | Branches, return conditions, limits covered. |
| A1 Intent details | Yes; visual/text | Yes | Fully represented | Black-box access and model roles. |
| A2 Chaining details | Yes; visual/text | Yes | Fully represented | Tool verification and refinement. |
| A3 Drift details | Yes; visual/text | Yes | Fully represented | Restrictions, strategy tension, missing metric formula. |
| A4 Injection details | Yes; visual/text | Yes | Fully represented | Grey-box access, models, hyperparameters, bank reuse. |
| A5 Poisoning details | Yes; pp. 13–14 images and p. 15 text | Yes | Fully represented | All important reported numerical settings retained. |
| B1 Intent demonstration | Yes; text only | Yes | Represented in compressed form | Five-turn auditor progression and persona inconsistency covered. |
| B2 Chaining demonstration | Yes; text only | Yes | Represented in compressed form | File creation, harmful-content append, lookup, distribution; construction detail omitted. |
| B3 Shopping demonstration | Yes; text only | Yes | Fully represented for substantive results | Task constraint, prices, scores, injection counts and ratio covered. |
| B4 Slack demonstration | Yes; text only; corresponding F3 visual | Yes | Represented in compressed form | Three snippets and unauthorized action sequence covered. |
| B5 Memory demonstration | Yes; text only; corresponding F4 visual | Yes | Represented in compressed form | Persistent preferences and later sensitive publication covered. |
| Author-stated limitations | Yes | Yes | Fully represented for available statements | Preliminary scope distinguished from analyst concerns. |
| REF References | Yes; text only | Yes | Represented in compressed form | Relevant source categories retained; bibliographic list not reproduced. |
| Footnotes and decorative objects | Yes where supplied | Yes | Inspected; compressed as non-substantive | Affiliation/date retained; model logos and warning icons do not add results. |
| Separate supplements | Not supplied | No | Missing from supplied material | No separate supplementary file reviewed. |
| External website/repository | Not accessed | Availability only | Inaccessible under source-only scope | No artifact functionality or reproducibility claim verified. |

### Missing or inaccessible material

No text page is missing within the supplied 1–19 sequence. Page renderings are absent for pp. 2, 9–11, and 15–19, so their coverage is text-only. No separate supplemental files, source repository contents, task configuration files, complete prompts, or raw experimental logs were supplied. The paper refers to external works and websites that were not reviewed. The remaining three attack-family ablation plots implied by the broad prose statement are not present in the supplied figures.

### Uncertain interpretations

Unresolved items are: the nine-versus-ten risk-category count; GPT-5.1 overall aggregation and about-70% prose; Llama's 86.6% versus 86.8%; exact target model identifiers; default turn-budget mapping and its relation to appendix budgets; Tool Hijacking versus Intent Hijacking; objective-drifting command restrictions; black-/white-/grey-box terminology; frugality formula; T2S convention at zero successes; Algorithm 1 cap/sampling behavior; Algorithm 2 final rewrite evaluation; attacker-bank initialization/reset; and the p. 16 persona description. Exact plotted coordinates are not labeled and remain undigitized. Confidence in these unresolved interpretations is LOW or UNKNOWN as appropriate, despite HIGH confidence that the discrepancies are present.

### Deliberately compressed material

Related-work citation detail and the full reference list are compressed without introducing outside assessments. Repeated descriptions of the five mechanisms across the main text, figures, and appendices are consolidated with source locators. Example payload wording, fictitious identities, addresses, tokens, and operational harmful-content detail are shortened while preserving attack surfaces, stage order, and outcomes. Unlabeled plot coordinates are described qualitatively rather than guessed. Decorative graphics and repeated headers are accounted for without reproduction.

### Potential omissions

Every known substantive inventory object is represented directly or through disclosed compression. Exact unlabeled plot coordinates, full bibliography entries, and complete example payload strings are intentionally not reproduced. The analysis cannot claim to cover artifacts not supplied, independently reproduce the benchmark, validate its novelty against outside literature, or establish a measured standalone-versus-web-agent vulnerability gap. Its completeness is bounded by the supplied pages and the inventory above.
