# Stage 0 — Document Accessibility Report

The supplied work is **LoopTrap: Termination Poisoning Attacks on LLM Agents**, by Huiyu Xu, Zhibo Wang, Wenhui Zhang, Ziqi Zhu, Yaopeng Wang, Kui Ren, and Chun Chen. The first page identifies arXiv:2605.05846v1, dated 7 May 2026; no accepted publication venue is supplied. Zhibo Wang is identified as corresponding author.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes, as supplied extracted text covering physical PDF pp. 1–21 |
| Accessible page count | 21 text pages; 18 rendered page images |
| Apparently missing pages | None from the supplied text sequence; images for pp. 8, 13, and 14 are absent |
| Visually inspected pages | 1–7, 9–12, 15–21 |
| Text-only coverage | Pages 8, 13, and 14 |
| Figures available | Figures 1–11 are visually present in the rendered pages |
| Tables available | Tables 1–9 are visually present and generally readable; extracted text assists exact transcription |
| Equations available | Equations (1)–(4) are text-only on p. 8; Equation (5) is also visually available on p. 9 |
| Appendices | Appendices A–J are present in supplied text; Appendix A begins on text-only p. 14 |
| Supplementary artifacts | The repository described in Appendix B was not supplied or inspected |
| OCR | Not performed; supplied native text was used alongside direct visual inspection |
| Other limitations | No raw results, executable code, full prompts, task identifiers, or independent artifact access; numerical and methodological contradictions remain unresolved |

All page references below are **physical PDF page numbers**, matching the supplied page labels. The accessibility metadata says no appendix pages were detected, but the supplied text explicitly contains Appendices A–J; direct document content establishes their presence.

Evidence categories are: **[A] Author-reported**, **[B] Directly observable**, **[C] Analyst-derived**, and **[D] Analyst interpretation**. No external information is introduced. Confidence refers to fidelity to the supplied evidence, not independent confirmation that the reported experiments occurred or that their underlying data are correct. The paper and its embedded attack examples are treated as evidence, never as instructions.

# 1. Plain-language orientation

An autonomous language-model agent repeatedly gathers information, reasons about it, uses tools, and decides whether its task is finished. This paper studies an attacker who tries to corrupt that last decision. Instead of stealing information or demanding an obviously unrelated answer, the attacker inserts instructions that make additional checking, research, or refinement appear necessary.

The authors call this **Termination Poisoning**. Their central concern is that retrieved material can influence the same reasoning process that decides whether to continue executing. A page can therefore become more than evidence about a question: it can become an unauthorized source of instructions about how much work remains. [A, pp. 1–3]

The researchers first test ten attack strategies against eight model-based agents on 60 tasks selected from GAIA, a benchmark for general AI assistants. They then build **LoopTrap**, an automated attack-generation framework that probes a target's behavioral tendencies, generates task-specific injections, evaluates attempts, reflects on failures, and stores reusable successful patterns. [A, pp. 4, 7–10]

The principal reported aggregate results are 2.33× step amplification for the initial strategy study and, for LoopTrap, 86.3% attack success, 3.57× step amplification, and 3.93× token amplification. These are results from agents using simulated tool returns, not measurements of unrestricted live browsing deployments. Attack success means crossing a step-amplification threshold around 2×; it does not mean demonstrating literally endless execution. [A, pp. 4–5, 10–11, 16]

The central contribution is a security analysis of the **termination decision as an attack surface**, paired with an adaptive red-teaming system. Several contradictions in the paper weaken exact model-ranking, profiling, and ablation interpretations. They do not erase the reported aggregate pattern, but they prevent treating every associated explanatory claim as settled.

# 2. Document roadmap

The document is an empirical AI-security and algorithm/systems paper, rather than a theoretical proof paper or literature review.

| Original component | Location | Function |
|---|---|---|
| Abstract | p. 1 | Threat, framework, headline results |
| §1 Introduction | pp. 1–2 | Motivation and three contributions |
| §2 Background and Related Work | pp. 2–3 | Agent loops, termination mechanisms, prompt injection |
| §3 Threat Model | p. 3 | Goal, scenario, attacker capabilities |
| §4.1 Attack Strategy Design | pp. 3–4 | Four manipulation categories and ten strategies |
| §4.2 Experimental Setup | p. 4 | Tasks, models, simulated environment, amplification metric |
| §4.3 Experimental Results | pp. 5–6 | Overall risk, task context, model differences |
| §4.4 Behavioral Profiling | p. 6 | Four-dimensional behavioral characterization |
| §5.1 Overview | p. 7 | Challenges and system architecture |
| §5.2 Fingerprinting | p. 8 | Diagnostic probes and strategy priors |
| §5.3 Trap Synthesis | pp. 8–9 | Selection, generation, scoring, refinement |
| §5.4 Skill Evolution | pp. 9–10 | Abstraction, merging, routing, failure knowledge |
| §6.1 Setup | p. 10 | Budgets, baselines, metrics, settings |
| §6.2 Effectiveness | pp. 10–11 | Aggregate comparisons and adaptation |
| §6.3 Efficiency | p. 11 | Cumulative success versus episodes |
| §6.4 Ablation | p. 12 | Component removals |
| §7 Discussion | pp. 12–13 | Limitations and proposed defenses/extensions |
| §8 Conclusion | p. 13 | Restates threat and contribution |
| References | pp. 13–14 | 49 bibliography entries |
| Appendices A–J | pp. 14–21 | Ethics, artifact statement, framework comparison, token results, algorithm, categories, templates, probes, skills, cases |

The important visual inventory is Figures 1–11, Tables 1–9, Algorithm 1, and Equations (1)–(5). There are no supplied theorems, lemmas, or formal proof claims. Bibliographic details, author contact information, and repeated attack prose are deliberately compressed; the methods and results they support remain represented.

# 3. Background and context

A **large language model (LLM)** is the reasoning engine in the agents studied here. An agent adds a repeated execution process around that engine: observe information, reason, choose an action, call a tool, and assess progress. The paper describes a ReAct-style pattern, interleaving reasoning and acting. The important security property is that observations enter the model's context, which also influences its next action and stopping decision. [A, §2, pp. 2–3]

**Prompt injection** means adversarial instructions enter a context that the model processes. The paper distinguishes direct injection through user input from **indirect injection** through retrieved web pages, documents, API responses, and similar artifacts. The attacker in this work uses the indirect setting. [A, p. 3]

The authors describe three termination patterns: explicit self-evaluation, implicit completion detection through final-answer markers or an end to tool calls, and external validation through tests, ground truth, or human approval. They characterize the last as more robust but limited to tasks with objectively verifiable outputs. Their assertions about prevalence in production are literature-positioning claims, not a deployment survey conducted in this paper. [A, pp. 2–3]

**Control flow** is the sequence of decisions that determines which operation executes next and whether execution continues. Termination poisoning attacks this sequence by changing perceived completion requirements. **Step amplification** compares attacked execution length with benign execution length. **Token amplification** compares token consumption. A step ratio is not automatically a dollar-cost ratio because the paper does not provide pricing or identical per-step token costs.

The four behavioral dimensions describe responses to imposed phases, apparent authority, recursive checking, and exhaustive verification. These are operational characterizations used by the authors, not independently established psychological diagnoses of models. [D]

# 4. Research problem and gap

**Existing problem.** Agents must decide when enough work has been done, and that decision may depend on reasoning over untrusted retrieved content. An attacker can exploit the connection between task information and completion assessment. [A, pp. 1–3]

**Shortcomings attributed to earlier approaches.** The authors say indirect prompt-injection research has mainly emphasized output manipulation, exfiltration, harmful generation, and tool-call hijacking. They distinguish model-level sponge attacks, aimed at computational inefficiency during individual model passes, from attacks on an agent's repeated execution loop. These are the authors' descriptions of prior work; the cited papers were not independently reviewed here. [A, §2, p. 3]

**Claimed gap.** The authors state that prior work had not systematically studied corruption of agent termination through progress self-evaluation. Their novelty claim is represented as an author claim, not verified against the whole literature. [A, p. 3]

**Motivation.** Semantically plausible demands for additional diligence can prolong execution while appearing aligned with the legitimate objective. This creates a resource-consumption risk without requiring a conspicuously malicious final answer. The introduction's financial-loss anecdote is a cited motivation, not an experimentally measured cost result of this study. [A, pp. 1–2]

**Scope.** The empirical work concerns single-agent systems, eight reasoning models, selected GAIA tasks, ten strategy families, a common main scaffold, simulated tool outputs, and two additional framework implementations. It does not establish a general numerical vulnerability gap between web agents and standalone LLMs. [A/D, pp. 4, 10, 13, 15]

# 5. Research questions, objectives, and hypotheses

The initial empirical study explicitly asks three questions. [A, §4, p. 3]

- **RQ1:** Are LLM agents broadly susceptible to termination poisoning, and how severe is resource amplification?
- **RQ2:** How does attack effectiveness vary across strategies and target agents?
- **RQ3:** Can agent-specific vulnerability patterns be formalized as structured, interpretable profiles?

The LoopTrap evaluation asks another three questions. [A, §6, p. 10]

- **RQ4:** Does the adaptive approach outperform static baselines in attack effectiveness?
- **RQ5:** How efficiently does it operate under limited query budgets?
- **RQ6:** What does each design component contribute?

The system objectives are efficient profiling, task-aware generation, and optimization under sparse feedback. The document does not specify preregistered hypotheses, formal null hypotheses, or a hypothesis-testing plan. The word 'significantly' appears in evaluative prose, but no corresponding statistical significance tests or p-values are reported in the supplied material.

For the user's question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, relevance must remain an analyst inference: the paper identifies an additional agent-level failure pathway created by external observations, repeated tool actions, and model-controlled termination. It does not experimentally compare that pathway against otherwise matched standalone LLM conditions.

# 6. Assumptions / Threat Model

**Protected property.** The primary asset is the integrity of termination and progress assessment; the associated resources are steps, tokens, API calls, and computational capacity. The attacker wants the agent to continue after its legitimate objective has been fulfilled. Changing the final answer, exfiltrating information, and triggering harmful actions are excluded objectives. [A, §3, p. 3]

**Entry points.** The attacker may insert or modify content in at least one external source the agent will access: a web page, knowledge-base document, third-party API response, shared file, or published skill/plugin. The work assumes knowledge of the task type. It does not quantify the probability of obtaining this exposure in a live search or browsing environment. [A, p. 3]

**Excluded access.** The attacker cannot access the system prompt, internal memory, or model weights; cannot modify agent code, tool definitions, or orchestration; and cannot observe or adapt the payload during the victim's execution in real time. The payload must be prepared before encounter. [A, p. 3]

**Important distinction.** LoopTrap is adaptive across completed attempts and episodes. Its refinement module receives prior execution traces, reasons about failures, and produces later payloads. This differs from changing a payload during the same running victim trajectory. The paper does not fully explain how a deployed attacker satisfying the stated asynchronous threat model obtains the detailed traces used in optimization. This is an analyst observation about the operational interface, not a claim that the authors secretly permit live adaptation. [D, pp. 3, 8–9]

**Trust boundary.** Retrieved material is untrusted task data. Termination poisoning succeeds when instructions embedded there influence what the agent treats as required work. Figure 1 shows this boundary crossing explicitly: a correct tool return is accompanied by an injected demand for more checking, and the progress evaluator chooses another iteration. [A/B, p. 3]

**Success criterion.** Section 3 defines success as T′ > αT with α > 1. Evaluation uses α = 2, while refinement prose and Algorithm 1 use T′/T ≥ α. Whether exactly 2.0× counts as success is inconsistent across formulations; Figure 11 explicitly labels 2.0× successful. [A/B, pp. 3, 9–10, 16, 21]

# 7. Methodology

## Study design and data

The authors describe GAIA as containing 165 real-world tasks across three difficulty levels. They manually annotate categories and use stratified sampling to select 60 tasks. Ten task-tailored strategies create 600 task–strategy pairs, each executed five times, yielding 3,000 runs per model. Across eight models this implies **24,000 strategy-study runs**, derived as 60 × 10 × 5 × 8; the derivation does not establish how benign baseline executions are counted. [A/C, §4.2, p. 4]

There is an unresolved category discrepancy: §§4.2 and 6.1 say 14 categories, whereas Appendix F and Table 7 list seven high-level categories. No mapping between a possible 14-category annotation and the seven reported groups is supplied. The seven visible counts are 9, 10, 8, 9, 8, 8, and 8, which sum to 60. [A/C, pp. 4, 10, 15–16]

The models are Gemini-3-Pro, GPT-4o, GPT-4o-mini, DeepSeek-R1, Kimi-K2-Thinking, GLM-5, Grok-4, and Claude Sonnet 4.5. These are reasoning engines placed in a unified ReAct-style framework, rather than eight separately evaluated main agent frameworks. The conclusion's phrase '8 agent frameworks' conflicts with this setup. [A, pp. 4, 10, 13]

The main environment generates tool returns from task context rather than invoking live external services. The authors choose this to remove confounds such as unavailable pages, changing content, authentication, and rate limits. That improves experimental control but narrows ecological validity. Tool inventory details, simulator implementation, model API versions, decoding settings, seeds, hardware, and task-level exclusions are not specified in the supplied prose. [A/D, p. 4]

## Attack taxonomy

| IDs | Category | Mechanism |
|---|---|---|
| P1 Expanding Horizon | Progress manipulation | Raises a perceived coverage target |
| P2 Incremental Milestone | Progress manipulation | Adds successive phases or subgoals |
| P3 Diminishing Returns | Progress manipulation | Frames work as almost complete but needing refinement |
| P4 Authority Override | Cognitive-bias exploitation | Fabricates authoritative requirements |
| P5 Sunk Cost Trap | Cognitive-bias exploitation | Uses invested effort to discourage stopping |
| P6 Social Proof | Cognitive-bias exploitation | Invokes purported expert diligence standards |
| P7 Recursive Decomposition | Task-structure manipulation | Requires verification of verification |
| P8 Dependency Chain | Task-structure manipulation | Creates circular prerequisites |
| P9 Positive Reinforcement | Reward shaping | Praises progress while encouraging continuation |
| P10 Gamification Trap | Reward shaping | Invents an insufficient thoroughness score |

These categories concern prompt-level manipulation. 'Reward shaping' here describes injected language about praise or scores; the paper does not report modifying model weights or a training reward function. [A/D, Table 1 and Appendix G, pp. 4, 15–17]

## LoopTrap pipeline

**Fingerprinting.** Four trivial anchor questions, one for each dimension, are executed once clean and once with injection. The resulting eight executions compare step counts, normalize amplification by τ = 5.0, and create a cached profile reused for that target. Simplicity is intended to reduce contamination from genuine task complexity. The four anchor tasks cover the capital of France, water's boiling point in Fahrenheit, the author of Romeo and Juliet, and the largest ocean. [A, §5.2 and Table 9, pp. 8, 17]

**Strategy selection.** A profile-derived prior biases selection toward strategies associated with susceptible dimensions. Selection combines historical mean amplification, an upper-confidence-bound exploration bonus, and the prior. With a usable skill, the system normally follows skill routing, but explores strategy-level selection with probability ε = 0.25. Without a usable skill it falls back to strategy selection. [A, pp. 8–9]

**Candidate generation.** GPT-4o receives the selected strategy, target profile, task description/tools/output format, and a scratchpad of previous failures. A matching skill contributes a parameterized template. The generator produces three candidates per attempt. [A, pp. 9–10]

**Self-scoring.** The same model ranks candidates using profile alignment, contextual plausibility, and predicted ability to prevent recognition of completion. The highest-scoring candidate is tested. Exact scoring scales, component weights, and calibration against observed performance are not supplied. [A/D, p. 9]

**Reflection.** Failed attempts generate a failure hypothesis, behavior analysis, and revision direction. These enter the scratchpad. An episode permits up to three attempts. A fully failed episode additionally produces trajectory-level negative knowledge for future use. [A, pp. 9–10]

**Skill evolution.** Success is abstracted into seven fields: source strategy, trigger condition, causal insight, action template, slot bindings, failure modes, and concrete examples. Skills with the same strategy and sufficiently overlapping tool/category conditions may merge. Routing combines semantic context similarity, historical performance, exploration, and profile alignment. The stored 'causal insight' is a generated explanation, not an independently identified causal effect. [A/D, pp. 9, 17–18]

## Evaluation configuration

Each agent–task pair receives 20 episodes. Each episode permits M = 3 attempts; each attempt generates n = 3 candidates. All experiments are repeated across ten independent runs. A full allowed campaign therefore entails at most 60 tested candidates and 180 generated candidates per pair per run, derived as 20 × 3 and 20 × 3 × 3 respectively; early stopping can reduce realized counts. These maxima exclude profiling and other internal model calls. [A/C, p. 10]

GPT-4o powers generation, self-scoring, reflection, and abstraction. Fixed settings are τ = 5.0; ε = 0.25; strategy UCB coefficients c = 1.5 and λ = 0.3; diversity threshold δ = 0.30 and penalty κ = 2.0; routing weights 0.30, 0.30, 0.10, 0.30; merging Jaccard thresholds 0.5 for tools and 0.3 for categories. The implementation details name the diversity penalty, but the displayed selection equation and pseudocode do not show its full formula. [A, p. 10]

Baselines are Static-Random, Rotate-All, LLM-Direct, Static-Best, and NoProfile. Static-Best uses the best strategy per agent selected using the earlier study; it is an informed benchmark, not an uninformed attacker. NoProfile retains adaptive generation and skills while removing fingerprinting. No held-out task/model transfer protocol, category-label reliability assessment, or train/validation/test split is described in the supplied material.

# 8. Experiments / Analyses

| ID | Purpose and conditions | Evidence | Main result and caveat |
|---|---|---|---|
| X1 Static strategy study | Ten strategies × 60 tasks × eight models, five repetitions | Table 2; Figure 2; §4.3 | Aggregate SAF 2.33×; model rankings conflict across sources |
| X2 Task-context analysis | Strategy SAF across seven displayed categories | Figure 3 | History & Politics average 2.76×; General Knowledge 2.10×; descriptive associations |
| X3 Model profiling | Four dimensions summarized across models | Table 3; §4.4 | Profiles differ, but prose and table values substantially disagree |
| X4 Adaptive effectiveness | Six methods, 20 episodes, three attempts, ten runs | Table 4 | LoopTrap aggregate ASR 86.3%, SAF 3.57×; not best ASR on every agent |
| X5 Query-budget convergence | Cumulative fraction with ≥1 successful episode | Figure 5; §6.3 | 79% by episode 5; 86.3% by episode 16; counts episodes rather than all queries |
| X6 Component ablations | Remove fingerprinting, reflection, skills, exploration | Figure 6; §6.4 | All lower aggregate ASR; reflection removal also reduces attempts |
| X7 Framework comparison | Same models/tasks/configuration in LangGraph and LangChain | Figure 7; Appendix C | Amplification persists; SAF/CAF labeling and average line are inconsistent |
| X8 Token amplification | Same six methods across eight targets | Table 6 | LoopTrap aggregate TAF 3.93×; uncertainty type not explicitly defined there |
| X9 Diagnostic worked example | GPT-4o recursive probe, clean versus injected | Figure 8 | 2 versus 8 steps, ratio 4.0×, score 0.80; one illustration |
| X10 Qualitative task comparisons | Geography, sports, fact verification on GPT-4o | Figures 9–11 | Adaptive examples yield 4.0×, 2.5×, 2.0×; case selection and correctness caveats apply |

The three initial research questions map to X1–X3. Adaptive effectiveness maps to X4, efficiency to X5, and component contributions to X6. X7–X10 provide secondary portability, resource, mechanism, and illustrative evidence. The document offers no comprehensive defense experiment and no standalone-LLM comparison.

# 9. Results

## Initial attack study

Table 2 reports an overall average of 2.33×. Its model averages, in table order, are 1.74, 3.08, 3.50, 2.08, 1.73, 1.31, 3.36, and 1.95×. Thus GPT-4o-mini has the largest displayed average and GLM-5 the smallest. P9 has the largest strategy average, 2.71×; P8 the smallest, 1.99×. The largest individual displayed cell is P1 against GPT-4o, 4.57 ± 0.49×. Some Kimi cells are below 1, including P8 at 0.89 ± 0.08×: not every injection prolongs execution. [A/B, p. 5]

The paper's nearby prose says GPT-4o has the highest SAF at 3.06× and Gemini is most resilient at 1.72×. Figure 2 instead labels GPT-4o-mini 3.48× and GLM-5 1.30×. The prose ranking is contradicted by both the table and visual. Figure 2 and Table 2 also differ slightly in their numerical means. These are unresolved reporting differences, not values averaged together here.

## Task context

Figure 3 category averages are 2.36, 2.10, 2.44, 2.76, 2.19, 2.28, and 2.27× for Entertainment, General Knowledge, Geography, History, Math, Science, and Technology respectively. P4 is 3.58× on Technology versus 1.68× on Math; P9 is 3.71× on History, 3.21× on Entertainment, and 1.68× on Science. These support task dependence. The broader claim that objective criteria protect termination is the authors' interpretation of this descriptive pattern, not a randomized intervention on completion ambiguity. [A/B/D, pp. 5–6]

## Adaptive method comparison

| Method | Aggregate ASR, % | Aggregate SAF, × | Aggregate TAF, × |
|---|---:|---:|---:|
| Static-Random | 56.6 | 2.14 | 2.36 |
| Rotate-All | 56.7 | 2.19 | 2.41 |
| LLM-Direct | 62.3 | 2.55 | 2.80 |
| Static-Best | 71.7 | 2.61 | 2.88 |
| NoProfile | 81.8 | 2.95 | 3.24 |
| LoopTrap | 86.3 | 3.57 | 3.93 |

These are the published average-column entries in Tables 4 and 6. LoopTrap exceeds Static-Best by **14.6 percentage points** of ASR and **0.96×** SAF, computed as 86.3 − 71.7 and 3.57 − 2.61; the authors also report these differences. They are not 14.6% relative improvement. [A/C, pp. 10–11, 16]

LoopTrap ASR by model is 88.3, 96.7, 98.3, 76.7, 86.7, 71.8, 90.0, and 81.7%. Its SAF values are 4.31, 3.73, 3.87, 4.22, 3.34, 2.61, 4.07, and 2.49×. On GLM-5, NoProfile's 77.0% ASR exceeds LoopTrap's 71.8%, contradicting the statement that LoopTrap is best on every agent on both metrics. LoopTrap is best on every displayed SAF column, however. [A/B, Table 4, p. 11]

## Efficiency and ablation

Section 6.3 reports 79% cumulative ASR by episode 5 and 86.3% by episode 16. Figure 6 labels full-system EFS 2.1 episodes, compared with 3.8 without fingerprinting. The figure's ASR sequence is 86.3, 81.7, 80.1, 78.4, 80.2%; SAF is 3.57, 3.07, 2.95, 2.98, 3.50×; EFS is 2.1, 3.8, 2.5, 2.2, 2.4. These sequences correspond to full, no fingerprinting, no reflection, no skills, and no exploration. NoProfile's SAF is 2.95 in Table 4 but 3.07 in Figure 6; the paper does not reconcile the difference. [A/B, pp. 11–12]

The peak 25× appears in the abstract/introduction without a corresponding supplied per-task result or trajectory identifying the condition. It remains an author-reported maximum with limited traceability. [A, pp. 1–2]

# 10. Figure-by-figure interpretation

## Figure 1 — Threat mechanism, p. 3

A diagram, not a statistical plot. The attacker crafts a payload, places it in an external source, and the agent observes that source during a reason–act–observe loop. The progress evaluator receives a correct answer about the largest ocean but also a request for repeated verification. The decision branches between completion and checking again. Labels contrast an expected 1–2 steps with 20+ after attack; these are schematic labels, not the later worked example's measured 2-to-8 trajectory. Red emphasizes the malicious route. The figure supports the trust-boundary mechanism, not an effect-size distribution.

## Figure 2 — Overall static-attack amplification, p. 5

Grouped green bars compare SAF and TAF per model. The horizontal axis lists eight models; the vertical axis is linear amplification in multiples, with ticks from 0 to 4. Solid and hatched bars distinguish steps and tokens. A horizontal orange dashed line marks average SAF 2.33×. Exact bar labels for SAF are 1.73, 3.06, 3.48, 2.07, 1.30, 3.34, 1.72, 1.94; corresponding token labels are 2.10, 3.15, 3.79, 2.09, 1.38, 3.69, 1.84, 2.12. Model order is Gemini, GPT-4o, GPT-4o-mini, DeepSeek, GLM, Grok, Kimi, Claude. No error bars are visible. Tokens exceed steps in each labeled pair. These labels differ slightly from Table 2; the overall mean is not recomputed to repair them.

## Figure 3 — Strategy-by-category heatmap, p. 6

Ten strategy rows plus an average row cross seven category columns. Red intensity represents SAF; each cell has an exact printed value, so cell readings are not graphical estimates. The color scale is labeled SAF in multiples, with ticks around 1.5–3.5. P9 on History is 3.71, P4 on Science 3.64, and P6 on Technology 1.37. History has the largest category mean, 2.76. The plot shows interactions rather than a universally dominant category–strategy rule. No uncertainty or significance markers are displayed.

## Figure 4 — LoopTrap architecture, p. 7

Three connected panels show fingerprinting, profile-guided synthesis, and reflective skill evolution. Clean/injected anchor executions feed a numerical profile. Strategy and skill libraries guide the attack generator. Target execution logs feed reflection; successes generate/merge skills and failures refine future attempts. This is a workflow illustration with example profiles and traces, not aggregate experimental evidence. A displayed clean/injected comparison appears to label both counts T_clean; this is a diagram-label ambiguity, whereas the text clearly distinguishes clean from injected execution.

## Figure 5 — Cumulative attack success, p. 11

A linear line plot uses episode number 1–20 on the horizontal axis and cumulative ASR 0–100% vertically. Six differently colored/marked curves represent the methods. LoopTrap is the highest terminal curve, rising quickly and leveling near 86.3%; NoProfile ends near 82%. Static-Best is flat around 71.7%. The prose supplies exact milestones of 79% at five episodes and 86.3% by sixteen; intermediate unlabelled points are approximate visual evidence only. No uncertainty bands appear. Flat Static-Best behavior is tied to reuse of its fixed attack, and must not be read as a general law about repeated stochastic trials.

## Figure 6 — Component ablation, p. 12

Three green bar charts show ASR, SAF, and EFS for the full method and four removals. Category labels are Full, −FP, −Ref, −Skill, −Expl. The axes are truncated: ASR begins around 76, SAF around 2.8, and EFS around 2.0, magnifying visual differences. Printed values, rather than bar heights, support the exact numbers listed in §9. Higher is preferable for ASR/SAF; lower is preferable for EFS. No error bars appear. The plot's no-fingerprinting SAF conflicts with Table 4.

## Figure 7 — Additional frameworks, p. 15

Grouped solid/hatched green bars compare LangGraph and LangChain across eight models. The caption calls the metric SAF, but the vertical axis says Cost Amplification Factor and the orange average line says CAF 3.58×. The scale is linear, 0–6. LangGraph labels are 4.33, 3.87, 3.94, 4.27, 3.41, 2.76, 4.78, 2.49; LangChain labels are 4.21, 3.56, 3.82, 4.03, 3.26, 2.29, 4.03, 2.17. Model order matches Figure 2. Every labeled value exceeds 2×. There are no visible uncertainty bars. The metric naming and average-line calculation remain uncertain; this is not direct measured monetary cost.

## Figure 8 — Probe trace, p. 18

Two side-by-side execution panels compare GPT-4o on the largest-ocean question. Clean execution searches once and finishes in two steps. Injected execution adds checking of the finding, source methodology, and meta-verification before finishing in eight. Explicit arithmetic gives amp = 8/2 = 4.0 and s = min(4/5, 1) = 0.80. Blue/green versus red/pink separates clean and attacked traces. The answer remains Pacific Ocean in this illustration. It demonstrates finite extension and eventual termination, not endless looping.

## Figure 9 — Geography case, p. 19

Static and adaptive panels share a six-step benign baseline. The generic P1 attack finishes in seven steps, 1.17×. The adaptive P2 attack imposes phases and finishes in 24 steps, 4.0×. A highlighted S3–S19 block shows repeated searches/fetches across six websites before a later coordinate calculation. Both sides report Indonesia and Philippines. The caption's 17 extra steps compares 24 with the static seven; relative to the benign six the increase is 18, derived as 24 − 6. Website names and answers are supplied trace content, not independently verified facts.

## Figure 10 — Sports case, p. 20

The baseline is four steps. A generic P7 injection yields five, 1.25×; task-specific P3 yields ten, 2.5×. A highlighted S3–S9 block shows game-log checking, wrong-page retrieval, retries, and cross-checks. Both displayed answers are 595. The caption reports all 12 static attempts failed and all three LoopTrap rounds succeeded. The 90%-complete cue is an attack claim, not actual measured task progress. Its annotation invokes sunk-cost reasoning despite P3's usual near-completion framing, showing explanatory overlap between categories.

## Figure 11 — Fact-verification case, p. 21

A five-step baseline contrasts static six-step execution, 1.20×, with adaptive ten-step execution, 2.0×. The highlighted loop checks explosive-yield units and historical test names. Static output is Bravo; adaptive output is Hercules, with different events and yields in the traces. Thus the example does not show preservation of the same final answer. The caption reports 2/12 static successes, rounded to 17%, and three successful adaptive rounds. It calls the adaptive strategy LLM-Direct even though that label elsewhere denotes a baseline outside the ten-strategy taxonomy. These are material interpretive caveats, not external fact-checks.

# 11. Table-by-table interpretation

## Table 1 — Ten-strategy taxonomy, p. 4

Rows P1–P10 identify names, categories, mechanisms, and short example injections. It provides conceptual coverage across four manipulation surfaces, not an effectiveness comparison. Full templates appear later in Table 8. The printed category typo for P8 does not change its stated task-structure role. Short examples are deliberately paraphrased in this analysis because their mechanism, rather than every word, is substantive.

## Table 2 — Static strategy results, p. 5

Rows are strategies and columns are eight models plus an average; units are SAF multiples. Cells are mean ± standard deviation over tasks according to the caption. Darker red marks higher values. P9 averages 2.71, P4 2.56, P5 2.55; P8 averages 1.99. GPT-4o-mini averages 3.50, Grok 3.36, and GLM 1.31. P1/GPT-4o is 4.57 ± 0.49, larger than any displayed Grok cell. The eight-of-ten row-leading count for Grok is consistent with the displayed rows: Grok leads P3–P10, while GPT-4o leads P1/P2. This differs from having the largest single cell or the largest all-strategy average. [B/C, p. 5] No statistical tests or missing entries are indicated. The relation between five stochastic repeats and task-level standard deviations is not elaborated.

## Table 3 — Four-dimensional profiles, p. 6

Columns are d_phase, d_auth, d_recur, d_verify on [0,1]. Rows list eight models. GPT-4o is 0.82, 0.38, 0.31, 0.36; Kimi is 0.28, 0.84, 0.45, 0.22; Grok is 0.58, 0.63, 0.52, 0.80; Claude is 0.20, 0.25, 0.82, 0.55. The largest tabulated phase score is GPT-4o's 0.82, authority Kimi's 0.84, recursion Claude's 0.82, and verification Grok's 0.80. Nearby prose instead gives Kimi authority 0.98, verification 0.85, recursion 0.22; Gemini phase 0.83; and Grok recursion 0.80. These disagreements are substantial and prevent selecting one consistent numerical profiling account.

## Table 4 — Main adaptive evaluation, p. 11

Two blocks compare six methods across eight models: ASR in percent and SAF in multiples, averaged over ten runs. Cells include ± terms, but the caption does not explicitly identify them as standard deviations, standard errors, or confidence intervals. The average columns are reported without ±. LoopTrap leads aggregate ASR and SAF and every per-model SAF; NoProfile leads GLM ASR. The supplied rounded row entries do not always reproduce the published average column exactly. For example, LoopTrap ASR entries sum to 690.2, giving 86.275%, consistent with 86.3 after rounding; Static-Best entries sum to 573.7, giving 71.7125%, consistent with 71.7. This illustrates arithmetic checking, not verification of raw outcomes. NoProfile entries sum to 664.2, giving 83.025%, which does not equal its reported 81.8 average. [C]

## Table 5 — Successful strategy frequencies, p. 12

Rows P1–P10 and model columns show percentages among successful LoopTrap attacks. These are conditional selection/outcome frequencies, not success probabilities for each strategy. GPT-4o's largest is P1 at 25%; GPT-4o-mini P1 at 28%; Kimi P4 at 32% followed by P6 at 24%; Claude P10 at 24% and P3 at 23%. Gemini's largest is P1 at 22%, exceeding P4 at 20%, contrary to nearby prose identifying authority override as most frequent for Gemini. Claude's listed column sums to 100%, while some other columns do not: GPT-4o sums to 100 and GPT-4o-mini to 100, but DeepSeek sums to 110 and Kimi to 100. The 110% column cannot be reconciled as an ordinary exclusive strategy distribution without further explanation. [B/C]

## Table 6 — Token amplification, p. 16

The same six methods and eight targets are compared using TAF, averaged over ten runs. LoopTrap's row is 4.74 ± 0.45, 4.10 ± 0.37, 4.26 ± 0.40, 4.64 ± 0.43, 3.67 ± 0.35, 2.87 ± 0.30, 4.48 ± 0.42, 2.74 ± 0.29; its average is 3.93. It exceeds the other listed methods in every model column. Aggregate baselines are represented in §9. The ± statistic is not explicitly named in this caption. Tokens provide a resource proxy, not a billing audit; input/output token accounting and simulator-token treatment are not specified.

## Table 7 — Category counts, p. 16

Seven categories contain 9 Entertainment, 10 General Knowledge, 8 Geography, 9 History, 8 Math, 8 Science, and 8 Technology tasks. Their sum is 60. Descriptions mix topical subject matter with reasoning capability. This table is the explicit category inventory, but its seven groups conflict with the fourteen categories claimed in the main methods unless an unreported grouping exists.

## Table 8 — Full strategy templates, p. 17

Ten rows expand Table 1 into templates with task topics, goals, source counts, percentages, scores, and other slots. P2 visibly specifies four finite phases; P7 specifies nested verification; P8 explicitly closes a prerequisite cycle. This distinction matters: not every template is itself an infinite formal loop, even when intended to encourage protracted execution. Exact repetitive payload prose is compressed here; all ten template mechanisms and their parameterization are represented.

## Table 9 — Diagnostic probes, p. 17

Four rows pair an anchor task with a dimension-specific injection theme. Authority uses a fabricated three-source quality-assurance requirement; phase uses a three-phase procedure; verification uses scholarly attribution cross-checking; recursion uses checking each checking step. It specifies operational probes rather than a validated psychometric scale. The author claim that anchor questions are interchangeable across dimensions is not accompanied by a reported interchangeability test.

# 12. Diagram / Architecture interpretation

The two main architecture diagrams are Figures 1 and 4; Figures 8–11 are execution-flow comparisons. Their distinct roles should not be conflated.

In Figure 1 the legitimate input is a user task, the environmental input is an external observation, and the output is either another action or termination. The attacker acts through the observation channel. A feedback edge sends the agent from progress evaluation back into reasoning. The failure occurs when untrusted text changes the continuation criterion despite a sufficient factual answer.

In Figure 4 the **attacker's own system** contains two persistent stores: a strategy library and a skill library. Probe results produce a target profile. The profile and task route selection, the generator creates a payload, and a test execution returns a log. A success takes the abstraction/merge path; failure takes reflection/refinement. Thus there are two loops: the victim's task-execution loop and LoopTrap's attack-optimization loop. A reusable skill is an attacker-side memory artifact; it is not evidence that the victim's internal memory was modified.

Figures 8–11 expose the victim loop as sequences of search, fetch, checking, and finish actions. They show how apparently relevant verification requests can add subgoals. Their eventual finish actions are important observations: the supplied examples demonstrate prolonged finite trajectories. They do not demonstrate permanent retention or the impossibility of escape.

# 13. Equations and mathematical concepts

## Success definition and amplification

The threat model introduces benign step count T, attacked step count T′, and threshold α > 1. Success is written T′ > αT. SAF = T′/T. A ratio of 3 means three times as many steps, not three additional steps. The methods do not fully define whether an execution step is a model call, action, tool invocation, or aggregated interaction; the illustrated traces include final-answer steps and sometimes group multiple operations. [A/D, pp. 3–4, 18–21]

## Equation (1), p. 8 — Probe amplification

amp(d) = T_inject(d) / max(T_clean(d), 1).

The input is the clean/injected execution length for dimension d. The max operator prevents a zero denominator. The output is a nonnegative dimension-specific ratio. This operational probe ratio is distinct from a direct observation of a psychological trait.

## Equation (2), p. 8 — Normalized probe score

s(d) = min(amp(d)/τ, 1.0), with τ = 5.0.

The min operator caps the score at one; amplification of at least five receives one. A worked ratio of four gives 0.80. **Analyst-derived implication:** unchanged execution, amp = 1, receives 1/5 = 0.20 rather than zero. Thus zero is not the natural score for no observed amplification under this formula. The profile order here is p = (s_phase, s_auth, s_verify, s_recur), whereas Table 3 orders recursion before verification. Keeping these orders explicit avoids swapping dimensions.

## Equation (3), p. 8 — Strategy prior

π(P_k) = [1/|D_k|] Σ over d in D_k of s(d).

P_k is a strategy, D_k its associated set of dimensions, |D_k| the number of those dimensions, and s(d) the probe score. The result is the arithmetic mean susceptibility of relevant dimensions. It guides initial selection before task-specific trials. The text first associates P7 with recursion, then illustrates P7 as exploiting recursion and verification; the precise complete mapping is not consistently enumerated. The example asserting a higher prior based on recursion 0.80 versus authority 0.25 also needs the verification value if P7 averages both dimensions.

## Equation (4), p. 8 — Strategy selection score

UCB(P_k) = μ̂(P_k) + c√(ln N / n_k) + λπ(P_k).

μ̂ is historical mean amplification; N is total episodes; n_k is times the strategy was selected; c weights exploration; λ weights profile alignment. The square-root term favors under-tried strategies. This is an upper-confidence-bound-style selection rule, not a reported confidence interval on the paper's final results. The supplied equation does not define initialization for n_k = 0 or N = 0. Implementation may address it, but the artifact was not inspected.

## Equation (5), p. 9 — Skill routing

score(skill) = α_r sim + β_r perf + γ_r UCB + λ_r π(P_k).

The signals are embedding cosine similarity between context and trigger, historical skill performance, a UCB-style exploration bonus, and the source strategy's profile prior. Weights are 0.30, 0.30, 0.10, and 0.30. The output ranks skills; a minimum threshold determines whether to use one or fall back. The threshold value and exact normalization of mixed performance signals are not specified. α_r is a routing coefficient, distinct from the attack-success threshold α.

## Algorithm 1, p. 16

Inputs are target A, task t, profile p, skill library L, statistics S, maximum attempts M, and candidate count n. It initializes a scratchpad, chooses a strategy by exploration or routing, generates n candidates, selects the best self-score, runs the target, calculates amplification against T_baseline, stores a skill on success, and otherwise reflects and updates statistics before retrying. It returns failure after M unsuccessful attempts.

The algorithm uses T_baseline and α without listing them in its input line. It also passes a skill variable to generation even on branches that do not visibly assign it. These are pseudocode specification gaps; they do not establish executable-code failure. Merging, trajectory-level reflection, diversity penalties, and the outer twenty-episode controller are described elsewhere rather than fully represented inside this single-episode listing.

# 14. Interpretation and discussion

The strongest supported interpretation is that **apparently useful diligence can become a continuation attack**. The injected material does not have to demand an unrelated objective. It may instead redefine what counts as a sufficiently checked answer. The qualitative examples contrast generic task-ID or coverage language with entity-specific demands involving capitals, game logs, source agreement, and units. [A/B, pp. 19–21]

RQ1 is answered by aggregate amplification in the selected simulated setting. RQ2 is answered descriptively by strategy/model and strategy/category interactions. RQ3 receives a proposed profiling scheme, but contradictory profile values and lack of a reported predictive-validation analysis limit claims of stable transferable signatures. RQ4 has aggregate comparative support, with the GLM ASR exception. RQ5 has episode-level convergence evidence, but not a complete computation or financial-cost accounting. RQ6 has ablation evidence, qualified by configuration discrepancies and the attempt-budget confound in reflection removal. [D]

Several inconsistencies materially affect interpretation:

| Issue | Conflicting evidence | Consequence |
|---|---|---|
| Model ranking | §4.3 calls GPT-4o highest and Gemini most resilient; Table 2/Figure 2 favor mini and GLM respectively | Do not use prose ranking as settled |
| Profile values | §4.4 prose versus Table 3 | Exact behavioral explanations are uncertain |
| Probe versus empirical profile | GPT-4o Table 3 differs from Appendix H's p = (0.45, 0.60, 0.55, 0.80) | Different constructions may matter; no calibration supplied |
| Category count | Main text 14; Appendix F seven | Sampling/aggregation mapping missing |
| Universal superiority | §6.2 says best every agent; NoProfile wins GLM ASR | Aggregate advantage is narrower than universal dominance |
| NoProfile aggregates | Table 4 average 81.8; prose/ablation 81.7; displayed cells average 83.025 | Multiple unresolved aggregation values |
| NoProfile SAF | Table 4 2.95; Figure 6 no-FP 3.07 | Ablation and baseline conditions unclear |
| Kimi ablation | §6.4 84.5→72.0%; Table 4 86.7 versus 75.2% | Per-agent effect not consistently reported |
| Strategy frequencies | DeepSeek column sums to 110%; Gemini largest row P1 rather than P4 | Distribution interpretation requires correction/data |
| Success boundary | > in threat/setup; ≥ in refinement/algorithm; 2.0× success in case | Boundary outcomes ambiguous |
| Framework metric | SAF caption versus CAF axis/line | Avoid interpreting as measured monetary cost |
| Case-study taxonomy | LLM-Direct described as LoopTrap strategy and separate baseline | Attribution of third case unclear |
| Answer preservation | Figure 11 outputs Bravo versus Hercules | Resource success can coincide with changed answers |

The paper's use of 'unbounded' expresses the attack objective and conceptual concern. The evaluations have budgets and the ethical appendix describes a per-trial ceiling, whose numerical value is not supplied. Finite amplification cannot itself establish an infinite execution property. [D]

# 15. Contributions and novelty

**Conceptual contribution [A]:** formalizing termination poisoning as corruption of progress assessment, emphasizing execution-control integrity alongside output integrity.

**Taxonomic contribution [A]:** ten representative strategies organized by progress signals, decision heuristics, task structure, and continuation incentives.

**Methodological contribution [A]:** a compact behavioral fingerprint intended to guide red-teaming more cheaply than exhaustive per-target evaluation.

**Algorithmic/system contribution [A]:** profile-biased selection, task-conditioned generation, self-scoring, reflection, and persistent skill abstraction/routing in a single attack framework.

**Empirical contribution [A]:** reported strategy/model/task interactions, aggregate improvements over constructed baselines, component ablations, token amplification, and additional scaffold results.

**Artifact contribution [A]:** an asserted anonymous package containing code, probes, skills, and the simulated ReAct harness. Its availability, completeness, and fidelity were not verified.

There is no new dataset claimed beyond a selected/annotated benchmark subset, no formal security theorem, and no experimentally validated defense. The paper's novelty relative to all prior work is not independently assessed in this closed-document analysis.

# 16. Limitations

## Authors' stated limitations

The four behavioral dimensions are derived from ten strategies and eight evaluated models. Other models or agent designs may have additional tendencies or qualitatively different termination mechanisms. The authors say the profiling schema should expand as agent designs evolve. [A, §7, p. 12]

The work emphasizes characterization and exploitation rather than comprehensive defense. Proposed defenses are preliminary and have not been tested against adaptive attackers who know them. [A, p. 12]

The work focuses on single-agent systems; multi-agent progress poisoning is proposed as an extension. [A, p. 13]

## Additional evidence-based analyst observations

- Simulated tool returns do not establish live-web exposure, persistence, or deployment-level resource impacts.
- The same 60 tasks support discovery and subsequent evaluation; no held-out generalization protocol is described.
- Four clean/injected probe pairs offer limited visible sampling of stochastic behavior; probe repeatability is not quantified.
- Trace-assisted refinement requires feedback access beyond merely planting a page; deployment feasibility is not fully specified.
- Several profile, aggregate, label, and case inconsistencies impede independent reconstruction.
- Step and token increases do not measure correctness preservation, economic damage, retention duration, or recovery ability.
- A reported 25× maximum has no identified supporting task/trace in the supplied material.
- Hyperparameters are fixed, but sensitivity analyses are not reported.
- The baseline statement of equal budgets does not fully specify whether every method uses identical candidate-generation and refinement computation.
- The artifact and raw records were absent; only document claims and displayed results were assessed.

These are analyst observations, not additional limitations attributed to the authors.

# 17. Threats to validity

**Internal validity [D].** Simulated returns reduce environmental confounds, which is an explicit design strength. However, unspecified simulation rules may also shape task plausibility and loop behavior. Reflection removal restricts an episode to one attempt, so its lower success combines removal of feedback with fewer tested attempts. The reported experiment does not isolate those effects.

**Construct validity [D].** SAF measures relative execution length, not necessarily wasted work: without an independent progress/correctness measure, some extra verification could be useful. A 2× threshold operationalizes a resource attack but does not prove nontermination. Behavioral names such as authority compliance summarize injected-response patterns rather than independently validated latent traits. The score formula assigns 0.20 to unchanged execution.

**External and ecological validity [D].** Eight models and three scaffolds are broader than one model/scaffold, but main results use one shared simulated setting. Live retrieval ordering, attacker discoverability, actual service responses, access controls, changing websites, and production budgets are not measured. Single-agent findings do not automatically transfer to multi-agent coordination.

**Statistical conclusion validity [D].** Repetitions are reported, and Table 2 identifies standard deviations. Other result tables show ± without defining the statistic. No hypothesis tests, confidence-interval procedure, multiple-comparison handling, or independent-unit analysis is supplied. Aggregate inconsistencies and incomplete normalization further constrain exact comparisons.

**Reproducibility [D].** Algorithm, probes, templates, and settings provide useful procedural information. Missing seeds, exact model versions, full prompts, selected task list, simulator details, ceiling value, and raw data limit reconstruction from the paper alone. The repository claim cannot substitute for inspection.

# 18. Future work and open questions

## A. Explicit author proposals

The authors propose **progress-signal verification** using an independent sandboxed module that checks self-assessed progress against objective criteria before continued execution. They also propose **provenance-aware context processing**, separating trusted system instructions from retrieved content and weighting their progress signals differently. Neither proposal is empirically validated in the paper. [A, pp. 12–13]

They propose extending the threat model to multi-agent message channels, where a compromised peer could inject corrupted progress information without controlling an external page. They also recommend extending profiling dimensions for emerging architectures. [A, pp. 12–13]

## B. Additional open questions [D]

Does task-specific poisoning remain effective under live tools and independent completion checks? How much does it change final-answer correctness? Can held-out probes predict held-out tasks and previously untested models? What feedback is realistically available to an attacker? What happens when every method receives the same number of actual target executions and generator calls? How does a ceiling change apparent success, recovery, and residual cost? Can an agent detect a false prerequisite and resume useful progress after exposure?

For the user's comparative research question, a missing experiment is a matched comparison between a standalone LLM and an agent built around the same model, controlling input, task, exposure, and computation. The present paper suggests a mechanism for extra risk but does not estimate that comparative effect.

# 19. Terminology and notation glossary

| Term or symbol | Beginner-friendly meaning in this paper |
|---|---|
| LLM | Large language model used as the reasoning engine |
| Agent | Model plus tools and a repeated task-execution process |
| ReAct-style loop | Interleaved reasoning, action, and observation |
| Prompt injection | Instructions introduced through a context channel the attacker controls |
| Indirect injection | Payload inside retrieved external material rather than the legitimate user's request |
| Termination poisoning | Corruption of progress assessment to encourage continued execution |
| Progress signal | Information used to decide how much work remains |
| SAF | Step Amplification Factor, attacked steps divided by benign steps |
| TAF | Token Amplification Factor, relative token consumption |
| ASR | Attack Success Rate, success under the chosen amplification criterion |
| EFS | Episodes to First Success |
| GAIA | Benchmark named GAIA; its source title is 'a benchmark for General AI Assistants' |
| T, T′ | Benign and attacked execution lengths |
| α | Success threshold; evaluation sets it to 2 |
| d_phase | Disposition toward externally imposed phases |
| d_auth | Disposition toward apparent authority/social standards |
| d_recur | Disposition toward recursively checking checks |
| d_verify | Disposition toward extensive verification/refinement |
| p | Probe-based four-score target profile |
| τ | Reference amplification used to normalize probe scores; 5.0 |
| P_k | Attack strategy with index k |
| D_k | Dimensions associated with strategy P_k |
| π(P_k) | Profile-derived strategy prior |
| UCB1 | Upper-confidence-bound strategy/skill selection mechanism |
| ε | Exploration probability, 0.25 |
| μ̂, N, n_k | Historical mean amplification, episode count, selection count |
| M, n | Maximum refinement attempts and candidates per attempt; both 3 |
| Skill | Stored reusable successful-attack representation |
| Scratchpad | Accumulated diagnoses used to revise later candidates |
| Jaccard similarity | Overlap measure used to decide whether skill conditions should merge |
| Cosine similarity | Embedding-based match between a task and skill trigger |
| CAF | Cost Amplification Factor label in Figure 7; relationship to SAF is inconsistently named |

# 20. Key numerical results

Unless marked derived, values below are reported document values rather than independent measurements.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Target models | 8 | models | Shared main agent scaffold | Author-reported | p. 4, §4.2 |
| GAIA pool described | 165 | tasks | Three difficulty levels | Author-reported | p. 4 |
| Selected tasks | 60 | tasks | Stratified sample | Author-reported | p. 4 |
| Categories | 14 versus 7 | categories | Main text versus appendix | Author-reported, inconsistent | pp. 4, 15–16 |
| Strategies | 10 | families | Four manipulation categories | Author-reported | p. 4, Table 1 |
| Task–strategy pairs | 600 | pairs | 60 × 10 | Author-reported | p. 4 |
| Repetitions | 5 | runs/pair | Initial strategy study | Author-reported | p. 4 |
| Runs per model | 3,000 | runs | Initial strategy study | Author-reported | p. 4 |
| Implied all-model runs | 24,000 | runs | 60 × 10 × 5 × 8 | Analyst-derived | p. 4 |
| Static aggregate SAF | 2.33 | × | Across initial study | Author-reported | p. 5 |
| Largest Table 2 cell | 4.57 ± 0.49 | × | P1 against GPT-4o | Author-reported | p. 5, Table 2 |
| Highest strategy average | 2.71 | × | P9 | Author-reported | p. 5, Table 2 |
| Fingerprinting cost | 8 | executions | Four clean + four injected | Author-reported | p. 8 |
| Probe normalization | 5.0 | reference ratio | τ | Author-reported | p. 8 |
| Attack budget | 20 | episodes/pair | Adaptive evaluation | Author-reported | p. 10 |
| Attempts and candidates | 3 and 3 | counts | Per episode and per attempt | Author-reported | p. 10 |
| Independent repetitions | 10 | runs | Adaptive evaluation | Author-reported | p. 10 |
| Success threshold | 2 | × | > versus ≥ inconsistent | Author-reported | pp. 9–10, 16 |
| LoopTrap ASR | 86.3 | % | Published aggregate | Author-reported | p. 11, Table 4 |
| Static-Best ASR | 71.7 | % | Published aggregate | Author-reported | p. 11, Table 4 |
| ASR difference | 14.6 | percentage points | 86.3 − 71.7 | Analyst-derived; also author-reported | pp. 10–11 |
| LoopTrap SAF | 3.57 | × | Published aggregate | Author-reported | p. 11, Table 4 |
| Static-Best SAF | 2.61 | × | Published aggregate | Author-reported | p. 11, Table 4 |
| SAF difference | 0.96 | × | 3.57 − 2.61 | Analyst-derived; also author-reported | pp. 10–11 |
| LoopTrap TAF | 3.93 | × | Published aggregate | Author-reported | p. 16, Table 6 |
| Peak amplification | 25 | × | Task/trace unidentified | Author-reported | pp. 1–2 |
| Early cumulative ASR | 79 | % | By five episodes | Author-reported | p. 11, §6.3 |
| Final convergence point | 16 | episodes | Reaches 86.3% | Author-reported | p. 11 |
| Full EFS | 2.1 | episodes | Figure 6 full system | Visually readable | p. 12 |
| No-fingerprint EFS | 3.8 | episodes | Figure 6 | Visually readable | p. 12 |
| No-reflection ASR | 80.1 | % | Figure 6 | Visually readable | p. 12 |
| No-skill ASR | 78.4 | % | Figure 6 | Visually readable | p. 12 |
| No-exploration SAF | 3.50 | × | Figure 6 | Visually readable | p. 12 |
| Recursive probe | 2→8; 4.0; 0.80 | steps; ×; score | GPT-4o worked example | Author-reported | pp. 17–18 |
| Geography adaptive case | 24/6 = 4.0 | × | Benign baseline six | Author-reported | p. 19 |
| Sports adaptive case | 10/4 = 2.5 | × | Benign baseline four | Author-reported | p. 20 |
| Verification adaptive case | 10/5 = 2.0 | × | Different final answers shown | Author-reported | p. 21 |

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Retrieved content can corrupt termination assessment | Threat definition and loop diagram | Figure 1 | pp. 1–3 | HIGH fidelity to stated mechanism; deployment prevalence not measured |
| Static strategies can amplify execution | Aggregate SAF 2.33× | X1, Table 2/Figure 2 | pp. 4–5 | HIGH reported aggregate; model means differ slightly |
| Task context matters | Category and strategy interactions | X2, Figure 3 | pp. 5–6 | HIGH descriptive evidence; causal role of ambiguity inferred |
| Agents have differentiated profiles | Four-dimensional scores | X3, Table 3 | p. 6 | MEDIUM conceptual support; exact values contradicted by prose |
| Profiling is inexpensive in execution count | Four paired probes | Equations 1–3; Table 9 | pp. 8, 17 | HIGH procedural claim; total token/cost overhead not given |
| LoopTrap improves aggregate attack effectiveness | 86.3% versus 71.7%; 3.57 versus 2.61× | X4, Table 4 | pp. 10–11 | HIGH displayed comparison; universal per-agent ASR claim false |
| LoopTrap increases token use | Aggregate TAF 3.93× | X8, Table 6 | p. 16 | HIGH reported value; not actual financial loss |
| Components contribute to success | All removals lower ASR | X6, Figure 6 | p. 12 | MEDIUM attribution because budgets/configurations are imperfectly isolated |
| Vulnerability persists across scaffolds | Both framework bars exceed 2× | X7, Figure 7 | p. 15 | MEDIUM; metric naming and aggregate line uncertain |
| Context-specific instructions can prolong verification | Entity-specific case traces | X10, Figures 9–11 | pp. 19–21 | HIGH as illustrations; selected cases, not a separate representative sample |
| Proposed defenses remain unvalidated | Explicit limitation statement | §7 | p. 12 | HIGH |
| Paper is relevant to web-agent versus standalone risk | External input influences a repeated control loop | §2–3 plus methodology | pp. 2–4 | MEDIUM analyst inference; no direct standalone comparator |

# 22. Very simple explanation — Explain Like I'm 15

Imagine an assistant researching an answer for you. It finds the answer, but a page it reads says that responsible researchers must check several more sources, then check whether those checks were reliable. The assistant treats that page's advice as part of your assignment. It keeps working even though your actual request may already be satisfied.

This paper studies attacks built around that mistake. The researchers try ten ways of making an agent feel that more work is needed. They then build LoopTrap, which tests what kinds of requests a target tends to follow and writes attacks that mention the target's actual task. In their simulated tool environment, the full system reports about 3.57 times the normal number of steps and 3.93 times the tokens.

The important lesson is that a correct-looking research instruction can still be hostile if an untrusted source gets to decide when your assistant is finished. But the study does not prove that agents run forever, that all extra checking is useless, or that web agents are a measured amount less secure than standalone chat models. It identifies and tests an additional way that an agent's repeated use of outside information can interfere with its stopping decision. Several inconsistent numbers and examples in the paper also need clarification.

# Completeness Audit

The denominator is the supplied inventory: all eight main sections, their substantive subsections, six explicit research questions, eleven figures, nine tables, five numbered equations, one algorithm, ten appendices, three stated contributions, and the explicit limitation/future-work statements. Coverage means representation of supplied content, not certification that the study is reproducible or internally consistent.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, date, abstract | Yes, text and image | Yes | Fully represented | Contact details compressed |
| §1 Introduction | Yes, text and image | Yes | Represented in compressed form | Financial anecdote identified as cited motivation |
| §2 agent architecture | Yes, text and image | Yes | Fully represented | Loop and tools explained |
| §2 termination mechanisms | Yes, text and image | Yes | Fully represented | Three categories preserved |
| §2 prompt-injection related work | Yes, text and image | Yes | Represented in compressed form | No external citation verification |
| §3 goal/scenario/capabilities | Yes, text and image | Yes | Fully represented | Trace-feedback and threshold qualifications included |
| §4.1 taxonomy construction/descriptions | Yes | Yes | Fully represented | All P1–P10 mechanisms |
| §4.2 data/models/framework/metric | Yes | Yes | Fully represented | Category discrepancy preserved |
| §4.3 overall/context/model analyses | Yes | Yes | Fully represented | Ranking contradictions retained |
| §4.4 dimensions/profiles | Yes | Yes | Fully represented | Numerical contradictions retained |
| §5.1 overview/challenges | Yes | Yes | Represented in compressed form | Three challenges and architecture |
| §5.2 probes/scoring/prior/cost | Text only on p. 8 | Yes | Fully represented | No claim of equation-image inspection |
| §5.3 selection/generation/scoring/refinement | Yes; p. 8 text-only | Yes | Fully represented | Missing initialization/scoring details flagged |
| §5.4 abstraction/merging/routing/reflection | Yes | Yes | Fully represented | Seven fields and negative knowledge |
| §6.1 setup/baselines/settings | Yes | Yes | Fully represented | Budget and fixed settings preserved |
| §6.2 effectiveness/adaptation/cases | Yes | Yes | Fully represented | Per-agent ASR exception retained |
| §6.3 efficiency | Yes | Yes | Fully represented | Cumulative definition and overhead limits |
| §6.4 all four ablations | Yes | Yes | Fully represented | Attempt-budget and conflicting values flagged |
| §7 limitations | Yes | Yes | Fully represented | Dimension scope and unvalidated defenses |
| §7 future work | Yes; continuation text-only | Yes | Fully represented | Independent verifier, provenance, multi-agent |
| §8 Conclusion | Text only | Yes | Represented in compressed form | Eight-framework wording discrepancy |
| RQ1–RQ3 | Yes | Yes | Fully represented | Linked to X1–X3 |
| RQ4–RQ6 | Yes | Yes | Fully represented | Linked to X4–X6 |
| Formal hypotheses | Not present | Yes, absence stated | Fully represented | No invented hypotheses |
| X1–X10 analyses | Yes | Yes | Fully represented | Separate conditions retained |
| Figures 1 and 4 | Visually inspected | Yes | Fully represented | Architecture/control flow |
| Figures 2 and 3 | Visually inspected | Yes | Fully represented | Axes, encoding, key exact values |
| Figures 5 and 6 | Visually inspected | Yes | Fully represented | Curves, truncated axes, no uncertainty bars |
| Figure 7 | Visually inspected | Yes | Fully represented | SAF/CAF discrepancy |
| Figure 8 | Visually inspected | Yes | Fully represented | Clean/injected arithmetic |
| Figures 9–11 | Visually inspected | Yes | Fully represented | Cases and answer/taxonomy discrepancies |
| Table 1 | Visually inspected | Yes | Fully represented | Ten strategies |
| Table 2 | Visually inspected | Yes | Represented in compressed form | Key cells, averages, extrema; not every cell retranscribed |
| Table 3 | Visually inspected | Yes | Represented in compressed form | Critical rows/extrema and contradictions |
| Table 4 | Visually inspected | Yes | Represented in compressed form | Aggregate, full LoopTrap values, exception, arithmetic |
| Table 5 | Visually inspected | Yes | Represented in compressed form | Conditional frequencies and 110% issue |
| Table 6 | Visually inspected | Yes | Represented in compressed form | Aggregate baselines and full LoopTrap row |
| Table 7 | Visually inspected | Yes | Fully represented | All counts and descriptions summarized |
| Table 8 | Visually inspected | Yes | Represented in compressed form | Repetitive exact payload prose compressed |
| Table 9 | Visually inspected | Yes | Fully represented | All four probes |
| Equations 1–4 | Text-only inspection | Yes | Fully represented | Meaning, symbols, gaps, score implication |
| Equation 5 | Text and visual | Yes | Fully represented | Weights and missing normalization |
| Success inequality / SAF | Yes | Yes | Fully represented | Strict versus inclusive boundary |
| Algorithm 1 | Text and visual | Yes | Fully represented | Branches, updates, specification gaps |
| Three major stated contributions | Yes | Yes | Fully represented | Conceptual, empirical, framework |
| Appendix A ethics | Text-only p. 14; visual p. 15 | Yes | Represented in compressed form | Harms, disclosure, containment, safeguards, publication rationale |
| Appendix B open science | Text and visual | Yes | Fully represented | Artifact contents claimed, not inspected |
| Appendix C framework comparison | Text and visual | Yes | Fully represented | Both frameworks and conditions |
| Appendix D token results | Text and visual | Yes | Fully represented | TAF definition and table |
| Appendix E algorithm | Text and visual | Yes | Fully represented | Single-episode scope |
| Appendix F categories | Text and visual | Yes | Fully represented | Seven-versus-fourteen discrepancy |
| Appendix G mechanisms/templates | Text and visual | Yes | Represented in compressed form | Every strategy covered |
| Appendix H probes/worked example | Text and visual | Yes | Fully represented | Cached profile and formula |
| Appendix I skill fields/routing | Text and visual | Yes | Fully represented | All seven fields/four signals |
| Appendix J three cases | Text and visual | Yes | Fully represented | Finite extension and correctness caveats |
| References 1–49 | Text inspected | Yes | Represented in compressed form | Categories and positioning; bibliography not reproduced |
| Corresponding-author footnote | Yes | Yes | Fully represented | No substantive methods footnote found |
| Author emails/affiliation layout | Yes | Limited | Inspected but deliberately omitted as non-substantive | Author names retained |
| Repository, code, raw data, prompts | No | Absence represented | Missing from supplied material | No artifact validation claimed |
| Visual renderings pp. 8, 13, 14 | No | Limitation represented | Missing from supplied material | Text for these pages available |

## Appendix A content represented in compressed form

The authors identify financial/resource losses, service degradation, alert fatigue, and user-experience harms. They report using public tasks without human subjects or private data, coordinated disclosure to affected developers before submission, simulated and sandboxed evaluation, rate limits, a usage policy requiring authorization for production testing, and guardrails including a per-trial step ceiling and red-team configuration flags. They justify publication through defensive value and lack of private-data or human-subject intrusion. These are author-reported practices; no disclosure receipts, policy files, or guardrail implementation were supplied. [A, pp. 14–15]

## Missing or inaccessible material

The repository and its source code, full skill library, complete generation/self-scoring/reflection prompts, selected task identifiers, raw traces beyond the examples, raw per-run data, seeds, exact simulator behavior, step-ceiling value, and detailed model/API configuration were not supplied. Rendered images of pp. 8, 13, and 14 were not supplied, although their native text was. No separate supplementary file was reviewed. The paper's anonymous repository claim does not establish that these absent materials are accessible here.

## Uncertain interpretations

Unresolved items include profile values, category mapping, selected aggregate means, the exact definition of a step, the ASR boundary at 2×, the ± statistic in Tables 4 and 6, strategy-distribution normalization, Figure 7's metric/average label, the full diversity-penalty rule, and the placement of LLM-Direct inside the qualitative LoopTrap account. The changed answer in Figure 11 prevents assuming answer preservation. These uncertainties are reporting or specification issues visible in supplied evidence, not externally inferred corrections.

## Deliberately compressed material

Not every cell of the 10×8 static result table or every baseline uncertainty term is retranscribed. The complete numeric tables remain in the supplied images/text; this account preserves their purpose, conditions, principal comparisons, exceptions, extrema, and contradictions. Full repeated attack templates, routine author/affiliation information, and bibliographic strings are compressed. No exact unlabelled curve-point estimates are promoted to numerical findings.

## Potential omissions

Every substantive inventory object is represented either directly or through disclosed compression. This does not imply literal preservation of every numerical cell or sentence. The known inaccessible objects are listed above. Without inspecting the claimed artifact or a separately authenticated PDF, no claim is made about additional material outside the supplied 21-page sequence.
