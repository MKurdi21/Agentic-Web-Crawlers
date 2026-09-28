# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Available range | Pages 1–14, conference pages 23159–23172 |
| Apparently missing pages | None |
| Native/extracted text | Available for all 14 pages; no page is marked as low-text or scanned |
| Visually rendered pages | Pages 1–9 and 11–14 |
| Page not visually rendered | Page 10; it contains references rather than a substantive figure, table, equation, or experiment |
| Figures visually inspectable | Yes: Figures 1–4 |
| Tables visually inspectable | Yes: Tables 1–5 |
| Algorithms/equations visually inspectable | Yes: Algorithms 1–3 and their scoring/selection formulas on pages 13–14 |
| Table readability | Good at the supplied resolution |
| Equation readability | Generally good, but notation remains typesetting/OCR-sensitive; Algorithm 1 contains the printed spelling `total_succcess`, evidently referring to `total_success` |
| OCR needed | No; native page text was supplied |
| Appendices present | Yes: Appendix A (models/datasets), Appendix B (additional evaluations, B.1–B.4), and Appendix C (algorithms), pp. 12–14 |
| Supplementary material supplied | No separate supplementary files |
| Referenced-but-absent supplementary material | None explicitly identified as supplementary material |
| Embedded images | Six detected on p. 2 and nine on p. 4, corresponding principally to Figures 1 and 2 |
| Other limitations | The complete PDF file itself was not independently opened; analysis is restricted to the supplied page-labeled text and rendered pages. Page 10 was assessed from text only. Exact plotted coordinates in Figures 3–4 are mostly unlabeled and therefore are treated as approximate visual estimates. |

Evidence labels used below:

- **[A] Author-reported:** explicitly stated in the paper.
- **[B] Directly observable:** visible in a supplied page image.
- **[C] Analyst-derived:** calculated from supplied values, with operands shown.
- **[D] Analyst interpretation:** a clearly identified inference rather than an author claim.

# 1. Plain-Language Orientation

This paper studies a security problem in agents powered by large language models (LLMs). Such agents do more than generate text: they may browse websites, read email, access files, or call software tools. While completing a legitimate user request, an agent may encounter text written by an attacker. If the agent mistakes that external text for an instruction, it can abandon the user’s goal and perform the attacker’s goal instead. This is **indirect prompt injection** [A, pp. 1–4].

The authors introduce **AGENTVIGIL**, an automated black-box red-teaming framework. “Black-box” means it does not need access to the underlying model weights, agent architecture, or internal reasoning. It observes whether an attack succeeded and systematically searches for stronger injected prompts [A, §§1, 3, 4].

AGENTVIGIL starts with a curated collection of attack templates. It repeatedly:

1. selects promising prompts;
2. asks a helper LLM to mutate them;
3. inserts the variants into external content;
4. tests them across agent tasks;
5. scores both overall attack success and success on tasks not previously compromised; and
6. uses Monte Carlo Tree Search (MCTS) to decide which prompt families deserve further exploration [A, §§4.1–4.5; Fig. 2; Algorithms 1–3].

Its principal results are:

- **AgentDojo:** 71% attack success on the o3-mini fuzzing set versus 38% for handcrafted attacks [A, §5.1, Table 1].
- **VWA-adv:** 70% reported final success during optimization versus a 36% handcrafted baseline; Table 1 separately reports 60% for the selected prompts on the GPT-4o fuzzing set and 59% on the test set [A, §§5.2, Table 1; Fig. 4].
- **Unseen tasks:** 65% on AgentDojo with o3-mini and 59% on VWA-adv with GPT-4o [A, Table 1].
- **Unseen model:** 67% on Gemini-2-flash-exp for both VWA-adv splits [A, Table 1].
- **Defenses:** results are mixed. AGENTVIGIL remains above the handcrafted baseline against several AgentDojo defenses, but on VWA-adv it falls to roughly the same level as, or sometimes below, the baseline once defenses are applied [A, Tables 2–3].
- **Real-world-style local case study:** an injected shopping review redirected a web agent toward an arbitrary URL after a user asked it to find product reviews [A/B, Fig. 1; §5.4].

The central contribution is therefore not a new defense. It is a generic, automated testing method intended to discover indirect prompt-injection vulnerabilities in otherwise opaque, multi-step agent systems [A, pp. 1–3, §6].

# 2. Document Roadmap

## Document inventory

| ID | Original location | Content |
|---|---|---|
| S1 | Abstract, p. 1 | Problem, framework, benchmarks, headline results |
| S2 | §1 Introduction, pp. 1–3 | Motivation, gap, approach, novelty, results |
| S3 | §2 Related Work, p. 3 | Existing attacks and defenses |
| S4 | §3 Threat Model, pp. 3–4 | Black-box assumptions, user and attacker capabilities, exclusions |
| S5 | §4 Method, pp. 4–5 | AGENTVIGIL’s architecture and optimization procedure |
| SS5.1 | §4.1, p. 4 | System and workflow overview |
| SS5.2 | §4.2, p. 4 | Initial corpus collection |
| SS5.3 | §4.3, pp. 4–5 | Five mutation operators |
| SS5.4 | §4.4, p. 5 | ASR-plus-coverage scoring |
| SS5.5 | §4.5, p. 5 | MCTS/UCB1 seed selection |
| S6 | §5 Evaluation, pp. 5–9 | Main experiments |
| X1 | §5.1, pp. 5–7 | AgentDojo optimization, transfer, and defenses |
| X2 | §5.2, pp. 7–8 | VWA-adv optimization, transfer, and defenses |
| X3 | §5.3, pp. 8–9 | Ablation study |
| X4 | §5.4, p. 9 | Local shopping-site case study |
| S7 | §6 Conclusion, p. 9 | Overall claim and significance |
| S8 | §7 Limitations, p. 9 | Cost and cross-model transfer limitations |
| S9 | §8 Ethics Statement, p. 9 | Defensive rationale and caution |
| S10 | §9 Acknowledgements, pp. 9–10 | Funding and disclaimer |
| A1 | Appendix A, p. 12 | Exact model checkpoints and dataset availability |
| A2 | Appendix B.1, p. 12 | Extra models and utility scores |
| A3 | Appendix B.2, p. 12 | Extra attack baselines |
| A4 | Appendix B.3, pp. 12–14 | Scenario-level breakdown |
| A5 | Appendix B.4, p. 13 | VWA-adv coverage curve |
| A6 | Appendix C, pp. 13–14 | Algorithms 1–3 |
| F1 | Fig. 1, p. 2 | Shopping-review attack example |
| F2 | Fig. 2, p. 4 | AGENTVIGIL architecture |
| F3 | Fig. 3, p. 6 | AgentDojo coverage and ablations |
| F4 | Fig. 4, p. 13 | VWA-adv coverage |
| T1–T5 | Tables 1–5, pp. 8, 12, 14 | Transfer, defenses, extra baselines, scenario results |
| ALG1–ALG3 | Algorithms 1–3, pp. 13–14 | Seed scoring, selection, and tree update |

The paper progresses from the security problem and prior work to a formal threat model, then presents the search framework. Its main evaluation covers two benchmarks, defenses, ablations, and a case study. The appendices materially extend the evidence with exact model versions, open-source-model results, additional baselines, scenario breakdowns, and complete pseudocode.

No formal research questions, hypotheses, theorems, lemmas, keywords, confidence intervals, or statistical-significance tests are supplied.

# 3. Background and Context

An **LLM agent** combines a language model with tools or services. The model acts as a planner: it interprets a user request, decides which tools to call, reads returned information, and chooses subsequent actions [A, §4.1].

A **direct prompt injection** is placed in input controlled directly by the attacker. An **indirect prompt injection** is placed in an external source—such as a web page, email, calendar entry, or product review—that an agent later retrieves while serving a legitimate user [A, §§1, 3].

An **attack success rate (ASR)** is the fraction of evaluated adversarial tasks for which the attacker’s injected objective succeeds [A, §4.4; Algorithm 1].

**Fuzzing** is used here as an iterative search strategy: start with test inputs, modify them, execute the target, use feedback to prioritize promising input families, and repeat. The paper emphasizes that conventional fuzzing cannot be transferred unchanged because an agent supplies only sparse binary attack feedback and processes semantically structured natural-language inputs [A, pp. 1–2].

A **seed** is a candidate attack prompt. A **mutator** creates a related candidate. A **seed corpus** is the stored collection of candidates. **Coverage** counts newly compromised task combinations, providing more search guidance than the final success/failure outcome alone [A, §§4.1, 4.4].

**Monte Carlo Tree Search (MCTS)** organizes candidate prompts as nodes connected by their mutation histories. The authors adapt **Upper Confidence Bound 1 (UCB1)** to favor prompts that either have high observed scores (**exploitation**) or remain insufficiently tested (**exploration**) [A, §4.5; Algorithm 2].

The two main benchmarks are:

- **AgentDojo:** personal-assistant environments and tools spanning Slack, workspace, travel, and banking tasks. A task is an interaction between a legitimate user objective and an attacker injection objective [A, §§5.1, B.3].
- **VWA-adv:** adversarial tasks built on VisualWebArena. Each combines an original web task, a text or image trigger, and an attacker goal. This paper evaluates only text-trigger tasks [A, §5.2].

# 4. Research Problem and Gap

## Existing problem

Agents ingest untrusted external content while exercising meaningful capabilities through browsers, email systems, files, calendars, and code-execution environments. Malicious content can be interpreted as an instruction, causing the agent to execute an attacker-selected action instead of the user’s request [A, §§1, 4.1].

## Shortcomings attributed to prior approaches

According to the authors:

- Handcrafted prompt injections require expert construction and may behave inconsistently [A, §2].
- Automated methods often assume white-box access, detailed knowledge of the agent, or control over the direct model input [A, §§1–2].
- Methods such as GPTFuzzer target direct, usually single-turn model jailbreaks rather than indirect injection in multi-step agents [A, p. 2].
- Agent-specific attacks do not provide a generic method across heterogeneous architectures and tasks [A, §1].
- Existing defenses may require training, additional models, substantial computation, system-specific engineering, or human intervention; some restrict useful tool access [A, §2].

## Research gap

The stated gap is the absence of a generic, scalable, automatic, black-box assessment method for indirect prompt injection across diverse LLM agents [A, pp. 1–3].

## Motivation

Assessment is difficult because real systems are opaque, user tasks vary dynamically, agent architectures combine many components, and individual attack runs yield only sparse binary feedback [A, §§1, 4].

## Scope

The study covers indirect injection through attacker-controlled external data. It assesses attack discovery and transfer across AgentDojo and text-trigger VWA-adv tasks, selected defenses, extra models, and a local WebArena shopping deployment [A, §§3, 5; Appendices A–B].

It excludes misuse in which the user directly asks an agent to perform harm and direct attacks on hosting or computational infrastructure [A, pp. 3–4].

# 5. Research Questions / Objectives / Hypotheses

## Explicit research questions

The paper does not state formally numbered research questions.

## Informal objectives reconstructed from author statements

These are objectives, not verbatim formal RQs:

1. Build a generic black-box framework that automatically discovers effective indirect prompt injections [A, Abstract; §1].
2. Determine whether seed quality, coverage-aware scoring, and MCTS selection improve search under sparse feedback [A, pp. 2, 5; §5.3].
3. Test whether optimized prompts transfer to unseen tasks and different backbone LLMs [A, §§5.1–5.2].
4. Assess attack performance against selected existing defenses [A, §§5.1–5.2].
5. demonstrate applicability in a more realistic web-agent environment [A, §5.4].

## Explicit hypotheses

No formal hypotheses, null hypotheses, or preregistered predictions are reported.

## Implicit expectations

The design assumes that:

- a curated starting corpus supplies useful early search signals;
- coverage rewards encourage discovery beyond already compromised tasks;
- UCB1-guided selection is more effective than uniform random selection; and
- semantically meaningful mutations can generate stronger or more transferable attacks.

These expectations are embedded in the method and ablation rationale [A, §§4, 5.3], but are not stated as formal hypotheses.

# 6. Assumptions / Threat Model

## System model

The agent receives a benign user task, interacts with tools and external data, and uses an underlying LLM to plan actions. The attacker modifies an external source that the agent may retrieve [A, §§3–4; Fig. 2].

## Black-box assumption

Neither attacker nor user has access to:

- the underlying LLM’s internals;
- the agent’s architecture or design; or
- internal state beyond externally observable system behavior [A, §3].

## Benign user

The user is legitimate and does not intentionally contribute malicious behavior [A, §3].

## Attacker capabilities

The attacker:

- can access and interact with the agent in a manner similar to a legitimate user;
- can test attacks on tasks resembling legitimate tasks;
- can manipulate external data, such as a shopping item, review, email, or calendar event;
- can embed an indirect instruction in that data; and
- can observe whether the intended attacker outcome happened by examining the resulting environment [A, §3].

For each task, feedback is restricted to binary success or failure [A, §§3–4].

## Attacker goals

The attacker tries to redirect the agent toward an objective unintended by the legitimate user. Examples include sending sensitive information, changing an intended web action, visiting an arbitrary URL, or downloading a malicious file [A, §3; Fig. 1; §5.4].

## Trusted and untrusted components

The paper does not formally label components as trusted. Operationally:

- the legitimate user task is treated as benign;
- attacker-modifiable external content is untrusted;
- the target agent and its underlying model are evaluated as black boxes; and
- benchmark evaluators determine whether user and injection objectives succeeded.

## Exclusions

The threat model excludes:

- direct harmful requests to the agent;
- direct compromise of the hosting platform or computational infrastructure;
- unrestricted manipulation of the model’s direct prompt;
- white-box access to model or agent internals [A, §§2–3].

The VWA-adv evaluation additionally excludes image-trigger tasks and one image–text consistency defense [A, §5.2].

# 7. Methodology

## 7.1 Study design

This is a cybersecurity, AI, algorithm, and systems paper with controlled benchmark experiments, ablations, transfer tests, defense tests, appendix extensions, and a local real-world-style case study.

## 7.2 Architecture and workflow

Figure 2 and §4.1 define the pipeline:

1. Collect initial adversarial templates.
2. Fill placeholders using the model, user task, and attacker goal.
3. test the seeds across injection tasks.
4. store resulting candidates and scores.
5. select one or two promising nodes through UCB1-guided MCTS.
6. mutate the selected prompt.
7. run the mutated prompt against sampled task combinations.
8. score ASR plus newly achieved coverage.
9. add the node, update ancestor visits, and repeat.

The target agent receives a legitimate task and contaminated environmental content. AGENTVIGIL itself receives only success feedback from the target environment [A/B, Fig. 2].

## 7.3 Initial corpus

Templates come from:

- human heuristics;
- online resources; and
- prior prompt-injection work.

They include placeholders and strategies such as role-playing, delimiter exploitation, and obfuscation [A, §4.2].

The number of initial templates, exact template text, collection criteria, deduplication procedure, and source-by-source composition are not supplied.

## 7.4 Mutation operators

Five helper-LLM-driven operators are reported [A, §4.3]:

| Operator | Function |
|---|---|
| Shorten | Compress the seed |
| Expand | Add contextual information |
| Rephrase | Change wording while preserving meaning |
| Crossover | Combine elements from two parent seeds |
| GenerateSimilar | Create stylistically similar but substantively different content |

An operator is chosen randomly at each iteration. The authors intentionally use basic strategies to preserve simplicity and diversity and state that models such as Llama-3-8B or GPT-4o-mini are sufficient for mutation [A, §4.3]. Main experiments use GPT-4o-mini.

## 7.5 Seed scoring

Each candidate is evaluated over sampled adversarial tasks. Its score combines:

- ASR: successful attacks divided by evaluated tasks;
- normalized coverage bonus: successes on task combinations not previously covered in that run; and
- coverage weight \(C\) [A, §4.4; Algorithm 1].

The supplied paper does not give the numerical value of \(C\) or precisely formalize the persistent covered-task data structure.

## 7.6 MCTS/UCB1 selection

Candidate prompts are tree nodes linked to their parent prompts. Algorithm 2 calculates a UCB score using the candidate’s empirical seed score and a term that increases for under-visited nodes. Depending on the mutation operator, the algorithm selects the highest-scoring one or top two nodes [A, §4.5; Algorithm 2].

Algorithm 3 then increments visit counts along the new node’s ancestor chain and adds the new node to the set [A, Appendix C].

## 7.7 Datasets, splits, and sampling

### AgentDojo

- Fuzzing set: 142 adversarial tasks.
- Test set: 173 adversarial tasks.
- Random division occurs within each task suite.
- Each new seed is evaluated on a randomly sampled quarter of the user/injection tasks from each suite.
- Top five seeds are used for transfer testing.
- Union success across selected prompts is reported [A, §5.1].

### VWA-adv

- Fuzzing set: 99 tasks.
- Test set: 100 tasks.
- Only text-trigger tasks are used.
- Top five seeds are used for transfer testing [A, §5.2].

The paper does not report the random seed, exact sampled task identifiers, stratification beyond within-suite division, or class distributions.

## 7.8 Models and checkpoints

Appendix A reports [A, p. 12]:

- o3-mini: `o3-mini-2024-12-17`
- GPT-4o-mini: `gpt-4o-mini-2024-07-18`
- GPT-4o: `gpt-4o-2024-08-06`
- Claude-3.5-Sonnet: `claude-3-5-sonnet-20241022`
- Gemini-2-flash-exp: `gemini-2.0-flash-exp`

Appendix B additionally evaluates QwQ-32B and a later `o3-mini-2025-01-31` checkpoint.

## 7.9 Optimization hyperparameters

| Benchmark | Optimization target | Mutations/iteration | Iterations | Helper model |
|---|---|---:|---:|---|
| AgentDojo | o3-mini | 3 | 10 | GPT-4o-mini |
| VWA-adv | GPT-4o | 10 | 10 | GPT-4o-mini |

Thus, before accounting for parent selection and evaluation sampling, the authors generate 30 candidate mutations for AgentDojo and 100 for VWA-adv [C: \(3\times10\) and \(10\times10\)].

## 7.10 Baselines and defenses

### Baselines

- handcrafted attacks supplied by AgentDojo;
- handcrafted attacks supplied by VWA-adv;
- Appendix B adds OpenPromptInjection and InjecAgent.

### AgentDojo defenses

- `pi_detector`: a ProtectAI BERT-based injection classifier;
- `repeat`: repeats user instructions after each function call;
- `delimit`: wraps tool outputs in delimiters and adds system instructions prioritizing the user;
- `tool_filter` is excluded because of incompatibility with o3-mini [A, §5.1].

### VWA-adv defenses

- `safety`: delimiters plus system prompts;
- `paraphrase`: rewrites untrusted text;
- `combined`: uses both;
- image–text consistency checking is excluded because of API-call cost [A, §5.2].

## 7.11 Metrics and statistical methodology

The primary metrics are ASR and task coverage. Benign-task utility is reported only for model selection in Appendix B.1.

The paper supplies no:

- confidence intervals;
- standard errors;
- statistical tests;
- significance levels;
- repeated-run variance;
- cost or runtime measurements;
- hardware specification; or
- sensitivity analysis for \(C\).

Words such as “significant” appear descriptively rather than as demonstrated statistical significance.

# 8. Experiments / Analyses

## X1 — AgentDojo optimization and transfer

**Purpose:** Test optimization quality, unseen-task transfer, model transfer, and performance under defenses [A, §5.1].

**Setup:** Optimize against an o3-mini agent on 142 fuzzing tasks, using three mutations per iteration for ten iterations and a quarter-sample of each suite per candidate. Evaluate the five highest-scoring prompts on 173 held-out tasks and other models.

**Results:**

- handcrafted baseline: 0.38 fuzzing ASR;
- initial corpus: 0.63;
- final optimization: 0.71;
- test transfer on o3-mini: 0.65 versus 0.34;
- GPT-4o-mini test: 0.43 versus 0.28;
- GPT-4o test: 0.19 versus 0.25;
- Claude test: 0.04 versus 0.08 [A, §§5.1, Table 1].

**Interpretation:** Optimization strongly improves the o3-mini target and transfers to unseen AgentDojo tasks and GPT-4o-mini. Transfer is not universally positive: optimized prompts underperform the baseline on GPT-4o and Claude [A, Table 1].

## X1b — AgentDojo defenses

On the fuzzing set with o3-mini [A, Table 2]:

| Defense | Handcrafted | AGENTVIGIL | Difference [C] |
|---|---:|---:|---:|
| None | 0.38 | 0.71 | +0.33 |
| `pi_detector` | 0.13 | 0.25 | +0.12 |
| `repeat` | 0.21 | 0.12 | −0.09 |
| `delimit` | 0.36 | 0.49 | +0.13 |

The prose says AGENTVIGIL “consistently outperforms” the baseline, but Table 2 shows the opposite under `repeat` (0.12 versus 0.21). This is a **text–table inconsistency** [A/B, p. 7 vs Table 2, p. 8].

In a separate adaptive experiment optimized directly against `repeat`, AGENTVIGIL obtains 0.74 versus the baseline’s 0.21 [A, p. 7]. This separate result explains adaptability but does not alter Table 2’s non-adaptive comparison.

## X2 — VWA-adv optimization and transfer

**Purpose:** Test attacks against multimodal web agents, using text as the injection trigger [A, §5.2].

**Setup:** Optimize on 99 fuzzing tasks against GPT-4o, using ten mutations per iteration for ten iterations. Evaluate the top five prompts on 100 test tasks and several models.

**Reported optimization trajectory:**

- benchmark baseline: 0.36;
- initial corpus: 0.54;
- final optimization: 0.70 [A, §5.2; Fig. 4].

**Selected-prompt transfer results in Table 1:**

- GPT-4o: 0.60 fuzzing, 0.59 test;
- GPT-4o-mini: 0.47 fuzzing, 0.54 test;
- Claude: 0.31 fuzzing, 0.42 test;
- Gemini: 0.67 on both splits [A, Table 1].

The 0.70 optimization result and 0.60 selected-prompt fuzzing result concern differently reported stages/aggregations, but the paper does not fully explain the numerical relationship.

## X2b — VWA-adv defenses

| Defense | Handcrafted | AGENTVIGIL | Difference [C] |
|---|---:|---:|---:|
| None | 0.36 | 0.60 | +0.24 |
| `safety` | 0.34 | 0.29 | −0.05 |
| `paraphrase` | 0.27 | 0.33 | +0.06 |
| `combined` | 0.30 | 0.27 | −0.03 |

Defenses largely erase the advantage. The combined defense does not reduce AGENTVIGIL below either single defense: its 0.27 is lower than `paraphrase`’s 0.33 and `safety`’s 0.29, but only slightly. The authors interpret this as evidence that some prompts can survive multiple defenses [A, §5.2].

## X3 — Ablation study

**Purpose:** Isolate the roles of the initial corpus and the combined scoring/selection mechanism [A, §5.3].

**Conditions:**

1. full AGENTVIGIL;
2. replace curated seeds with AgentDojo handcrafted prompts;
3. replace adaptive scoring plus MCTS with uniform random selection.

Figure 3 shows that full AGENTVIGIL rises throughout optimization, while the no-initial-corpus condition plateaus after about four iterations and the random-selection condition improves more slowly [A/B, Fig. 3; §5.3].

The experiment does not separately ablate coverage scoring and MCTS selection. Consequently, it cannot isolate the individual causal contribution of each despite discussing “three core components.”

## X4 — Local shopping-site case study

A local WebArena shopping deployment based on Magento is used. A user asks the agent to find a Samsung Galaxy S6 screen protector and identify reviewers mentioning fingerprint resistance. The workflow requires more than ten operations. An attacker posts a malicious review through a normal customer account; the agent reads it and is redirected to a fake GitHub-like URL [A/B, Fig. 1; §5.4].

The authors state that variants can induce navigation to phishing sites, malicious downloads, and private-information transmission [A, Fig. 1 caption; §5.4]. The supplied paper does not report a case-study sample size, repeat count, success rate, or defense condition.

## X5 — Extra models and baselines

Appendix B reports benign-task utility:

- Llama-3.3-70B-Instruct: 42%;
- Qwen2.5-72B-Instruct: 54%;
- QwQ-32B: 74%;
- o3-mini: 79% [A, Appendix B.1].

QwQ-32B is selected for attack evaluation. Table 4 shows AGENTVIGIL outperforming three baselines on QwQ-32B and a later o3-mini checkpoint [A, Appendix B.2].

There is a **prose–table discrepancy**:

- prose: latest o3-mini achieves 72% fuzzing and 74% test versus handcrafted 50% and 53%;
- Table 4: o3-mini reports 73%/76% versus 47%/49%;
- Table 4’s 72%/74% values belong to QwQ-32B.

The supplied document does not resolve whether the prose swapped model results, refers to another run, or reflects an earlier table version.

## X6 — Scenario breakdown

Table 5 separates:

- AgentDojo: Slack, Workspace, Travel, Banking;
- VWA-adv: illusioning and goal misdirection.

AGENTVIGIL is higher than the benchmark baseline in every listed scenario and split [A/B, Table 5]. Performance varies substantially: for example, o3-mini AgentDojo test ASR ranges from 0.38 in Banking to 0.97 in Slack.

# 9. Results

## 9.1 Main benchmark effectiveness

- **AgentDojo fuzzing:** 0.71 versus 0.38, an absolute gain of 0.33 or 33 percentage points [A, Table 1]. Relative improvement is \(0.33/0.38=86.8\%\) [C].
- **AgentDojo test:** 0.65 versus 0.34, an absolute gain of 31 points and relative improvement of \(0.31/0.34=91.2\%\) [A/C, Table 1].
- **VWA-adv reported optimization endpoint:** 0.70 versus 0.36, a 34-point absolute gain and \(0.34/0.36=94.4\%\) relative improvement [A/C, §5.2].
- **VWA-adv selected prompts, test:** 0.59 versus 0.44, a 15-point absolute gain and \(0.15/0.44=34.1\%\) relative improvement [A/C, Table 1].

Thus, the authors’ phrase “nearly doubling” is well supported for AgentDojo and the reported 0.70 VWA optimization endpoint, but not for every transfer condition.

## 9.2 Transferability is model-dependent

Positive transfer appears for:

- AgentDojo o3-mini test: +31 points;
- AgentDojo GPT-4o-mini test: +15 points;
- VWA GPT-4o test: +15 points;
- VWA GPT-4o-mini test: +25 points;
- VWA Gemini test: +17 points [A/C, Table 1].

Negative transfer appears for Claude:

- AgentDojo Claude test: −4 points;
- VWA Claude test: −9 points.

AgentDojo GPT-4o also declines by 6 points on the test split [A/C, Table 1]. Therefore, “strong transferability” is qualified by target-family dependence.

## 9.3 Defense findings

AgentDojo’s selected prompts outperform the handcrafted baseline for no defense, `pi_detector`, and `delimit`, but not `repeat` [A/B, Table 2]. Direct optimization against `repeat` subsequently reaches 0.74 [A, p. 7].

VWA defenses reduce AGENTVIGIL from 0.60 to between 0.27 and 0.33. Its advantage survives only under `paraphrase`; it falls below baseline under `safety` and `combined` [A/B, Table 3].

## 9.4 Component contribution

Figure 3 supports the joint importance of a strong initial corpus and adaptive selection/scoring. Full AGENTVIGIL achieves higher coverage and continues improving, whereas both ablations plateau lower [A/B, Fig. 3; §5.3].

## 9.5 Scenario robustness

Table 5 shows improvements in all listed scenarios. Particularly large test-set gains include:

- o3-mini Workspace: \(0.60-0.22=0.38\) [C];
- QwQ Banking: \(0.65-0.23=0.42\) [C];
- GPT-4o goal misdirection: \(0.42-0.20=0.22\) [C].

The weakest listed AGENTVIGIL test result is 0.38 for o3-mini Banking; the strongest is 0.97 for both o3-mini and QwQ Slack [A/B, Table 5].

# 10. Figure-by-Figure Interpretation

### Figure 1 — Indirect injection through a shopping review

- **Purpose:** Illustrate a realistic attack path [A/B, p. 2].
- **Contents:** A shopping page containing a malicious review, the legitimate user task, the agent’s resulting thought/action, and possible attacker outcomes.
- **Flow:** attacker plants review → user asks for product/review information → agent retrieves the page → agent reads injected instruction → agent visits an attacker-selected URL.
- **Important visible text:** the user seeks a Samsung Galaxy S6 screen protector and reviewers mentioning good fingerprint resistance; the injected goal is to visit a fake GitHub-like URL.
- **Outputs shown:** phishing-site visits, malware downloads, and private-information disclosure.
- **Conclusion supported:** external content can redirect a multi-step web agent away from the legitimate goal.
- **Caveat:** This is a workflow illustration and case example, not a quantified controlled experiment. The figure does not establish frequency or reproducibility.

### Figure 2 — AGENTVIGIL architecture

- **Purpose:** Show the target system and optimization loop [A/B, p. 4].
- **Components:** user, agent, environment, attacker, initial seeds, current seeds, mutator, seed selector, scorer, and seed storage.
- **Environment:** visibly lists code execution, email, file system, and web browser.
- **Attack path:** attacker injects an adversarial prompt into environmental sources; the agent retrieves it while serving the user.
- **Optimization path:** initial/current seed → selection → mutation → target-agent testing → binary success plus coverage scoring → seed storage → further selection.
- **Feedback loop:** evaluated variants return to storage and influence later MCTS choices.
- **Conclusion supported:** AGENTVIGIL is external to the target and operates using observed attack outcomes rather than agent internals.
- **Caveat:** The diagram abstracts away task sampling, helper-model calls, evaluation cost, and persistent coverage-state details.

### Figure 3 — AgentDojo coverage and ablations

- **Plot type:** three-line coverage curve [B, p. 6].
- **X-axis:** optimization steps, 1–10.
- **Y-axis:** average coverage, 0.0–0.5.
- **Encoding:** solid blue line is full AGENTVIGIL; dashed orange is without the initial corpus; dashed green is without adaptive scoring and MCTS selection.
- **Approximate visual values:** full AGENTVIGIL begins near 0.17–0.18 and ends near 0.37; no-initial-corpus begins near 0.07 and plateaus near 0.16; no-selection/scoring begins near 0.16–0.17 and ends near 0.27 [B, approximate].
- **Trend:** full AGENTVIGIL is consistently highest and continues improving; the no-corpus line plateaus early.
- **Conclusion supported:** both the curated seeds and guided selection/scoring materially improve coverage.
- **Caveats:** Exact point values and uncertainty intervals are not provided. The figure groups scoring and MCTS into one ablation, so their individual contributions are not isolated.

### Figure 4 — VWA-adv coverage

- **Plot type:** single-line optimization curve [B, p. 13].
- **X-axis:** steps, 1–10.
- **Y-axis:** average coverage, 0.50–0.80.
- **Approximate visual values:** about 0.54 initially; about 0.63 by step 2; about 0.65–0.66 around steps 4–5; about 0.70 by step 8; approximately flat through step 10 [B, approximate].
- **Trend:** rapid early improvement followed by diminishing gains and a plateau.
- **Textual relationship:** agrees with the reported movement from 54% initial performance to about 70% after refinement [A, §5.2].
- **Caveats:** Exact plotted values, run-to-run variance, and error bars are absent.

# 11. Table-by-Table Interpretation

### Table 1 — Cross-task and cross-model transfer

The rows distinguish benchmark, fuzzing/test split, and handcrafted versus AGENTVIGIL prompts. Columns are backbone models; values are ASRs.

Key observations:

- AgentDojo target optimization: 0.71 versus 0.38 on o3-mini.
- AgentDojo held-out transfer: 0.65 versus 0.34 on o3-mini.
- VWA target-model test: 0.59 versus 0.44 on GPT-4o.
- Highest unseen-model result: 0.67 on Gemini for both VWA splits.
- AGENTVIGIL loses to the baseline on Claude in all four Claude cells and on GPT-4o in AgentDojo.
- A dash means the model/benchmark combination was not evaluated or unsupported.
- Footnotes state that Gemini does not fully support AgentDojo tool calls and the early o3-mini does not fully support VWA-adv.

No uncertainty or significance information is reported.

### Table 2 — AgentDojo defenses

The table compares the handcrafted attack and selected AGENTVIGIL prompts on the o3-mini fuzzing set.

- Best AGENTVIGIL ASR: 0.71 with no defense.
- Lowest: 0.12 under `repeat`.
- Best defensive reduction against AGENTVIGIL: `repeat`, reducing ASR by \(0.71-0.12=0.59\) [C].
- AGENTVIGIL exceeds baseline under `pi_detector` and `delimit`, but not under `repeat`.
- This contradicts the nearby claim of consistent superiority across defenses.

### Table 3 — VWA-adv defenses

The table evaluates GPT-4o on the fuzzing set.

- Without defense: AGENTVIGIL leads 0.60 to 0.36.
- Under `safety`: baseline leads 0.34 to 0.29.
- Under `paraphrase`: AGENTVIGIL leads 0.33 to 0.27.
- Under `combined`: baseline leads 0.30 to 0.27.
- No defense condition fully eliminates attack success.

The table supports the narrower conclusion that defenses reduce the optimized attack, not a broad conclusion that AGENTVIGIL defeats every defense.

### Table 4 — Additional models and baselines

Each cell reports fuzzing/test ASR.

| Attack | o3-mini-2025-01-31 | QwQ-32B |
|---|---:|---:|
| AGENTVIGIL | 0.73/0.76 | 0.72/0.74 |
| AgentDojo baseline | 0.47/0.49 | 0.45/0.47 |
| OpenPromptInjection | 0.38/0.39 | 0.20/0.20 |
| InjecAgent | 0.15/0.11 | 0.14/0.12 |

AGENTVIGIL is highest in every column and split. However, Appendix B.1 prose assigns 72%/74% to the latest o3-mini and gives baseline values of 50%/53%, conflicting with the table’s o3-mini values of 73%/76% and 47%/49%.

### Table 5 — Scenario-level performance

All values are fuzzing/test ASR.

- AGENTVIGIL exceeds the benchmark baseline in all 18 displayed split-level comparisons.
- Slack is easiest for the optimized prompts: test ASR 0.97 for both AgentDojo models.
- o3-mini Banking is hardest: 0.49/0.38.
- VWA illusioning is easier than goal misdirection: 0.82/0.76 versus 0.58/0.42.
- Goal misdirection nevertheless shows large gains over 0.00/0.20 baseline performance.
- There are no confidence intervals or task counts per scenario, so differences in scenario size and uncertainty cannot be evaluated.

# 12. Diagram / Architecture Interpretation

The architecture has two interacting systems.

First is the **target LLM-agent system**:

```text
Benign user task
      ↓
Agent/LLM planner ↔ tools and environmental data
                         ↑
             attacker-controlled injection
```

Second is the **red-teaming search system**:

```text
Initial corpus → current seeds → MCTS selector → mutator
                       ↑                         ↓
                  seed storage ← scorer ← target execution
                                      ↑
                          ASR + new-task coverage
```

The data path carries legitimate requests, external content, and generated injected prompts. The control path selects candidates, launches tests, evaluates outcomes, and updates the search tree. The feedback loop is essential: newly discovered prompt variants become future mutation parents.

The framework does not require gradients, model weights, system prompts, or architecture knowledge. Its principal dependency is an evaluation mechanism capable of deciding whether the attacker’s objective was achieved [A, §§3–4].

# 13. Equations and Mathematical Concepts

## Equation E1 — Attack success rate

From Algorithm 1, p. 13:

\[
ASR=\frac{\text{total\_success}}{\text{num\_questions}}.
\]

- **Object:** empirical proportion.
- **Input:** number of successful injections and number of evaluated task combinations.
- **Output:** success rate between 0 and 1.
- **Role:** measures immediate effectiveness.
- **Notation issue:** the rendered algorithm spells the numerator `total_succcess` on line 19, while initialization uses `total_success`; this appears to be a typographical error [B].

## Equation E2 — Coverage-guided seed score

\[
\text{seed\_score}
=
ASR
+
C\cdot
\frac{\text{coverage\_bonus}}{\text{num\_questions}}.
\]

- \(ASR\): current success fraction.
- \(C\): coverage-factor weight.
- `coverage_bonus`: number of successful combinations marked as newly covered.
- `num_questions`: number of evaluated task combinations.
- **Meaning:** prefer prompts that succeed often and prompts that uncover new vulnerable tasks.
- **Unknown:** the numerical value of \(C\) is not supplied.

There is a minor pseudocode ambiguity: the comments say “newly successful task combinations not covered before,” but the displayed `if injection successful` condition does not itself show an explicit membership test against a prior covered set.

## Equation E3 — Total visit count

From Algorithm 2:

\[
\text{total\_visits}=\sum_{\text{node}\in N}\text{node.visits}.
\]

This aggregates the visit counts of all prompt nodes.

## Equation E4 — UCB seed-selection score

\[
UCB(\text{node})
=
\text{node.score}
+
C\sqrt{
\frac{\log(\text{total\_visits}+1)}
{\text{node.visits}+\epsilon}
}.
\]

- `node.score`: empirical effectiveness and coverage score.
- \(C\): exploration factor.
- `total_visits`: visits across all nodes.
- `node.visits`: how often this node/path has been explored.
- \(\epsilon\): small stabilizing term preventing division by zero; its value is not supplied.
- **Meaning:** a highly successful node scores well, but an under-explored node receives an exploration bonus.
- **Selection:** choose the maximum-scoring node for one-parent mutations or the top two for two-parent mutation.

The same symbol \(C\) is used as the coverage factor in Algorithm 1 and the exploration factor in Algorithm 2. The paper does not clarify whether these are numerically identical or merely reuse the same letter.

## Algorithm 3 — Tree update

Algorithm 3 contains no major equation. It traverses each new node’s ancestors, increments every ancestor’s visit count, and adds the new node to \(N\). Increasing visits reduces that path’s future exploration bonus in E4.

No theorems, formal proofs, convergence guarantees, or complexity bounds are supplied.

# 14. Interpretation and Discussion

The evidence supports the authors’ core proposition that guided semantic search can find stronger indirect injections than fixed handcrafted templates on the optimization targets. The large gains on o3-mini AgentDojo and GPT-4o VWA-adv, plus the ablation curves, connect the method to the result.

The work also answers the informal transfer objective, but with qualifications. Transfer to unseen tasks on the optimized model is strong. Transfer to related GPT-family models and Gemini is often positive. Transfer to Claude is consistently poor relative to the relevant handcrafted baseline. The authors speculate, after manual inspection, that Claude may be more susceptible to simpler prompts [A, §5.1]; this is a hypothesis, not a controlled explanation.

Defense experiments show two different situations:

- fixed optimized prompts may be strongly reduced by a defense;
- if AGENTVIGIL is allowed to optimize against that defense, it may find new bypasses, as in the 74% `repeat` experiment.

This distinction matters: resilience of a fixed attack is not the same as adaptability of an attack-search process.

The case study improves ecological relevance because the attack is embedded in a customer review in a multi-step browsing task. Nevertheless, its evidentiary strength is illustrative: the paper gives no trial count or systematic case-study evaluation.

## Identified inconsistencies and unresolved points

1. **Table 2 versus prose:** Table 2 gives AGENTVIGIL 0.12 under `repeat`, below the baseline’s 0.21, contradicting “consistently outperforms” [pp. 7–8].
2. **Appendix B.1 versus Table 4:** prose reports latest-o3 values of 72%/74% and baseline 50%/53%; Table 4 gives 73%/76% and 47%/49%, while 72%/74% is the QwQ result [p. 12].
3. **VWA optimization versus Table 1:** §5.2 reports a final 70%, whereas Table 1 gives 60% for selected prompts on the fuzzing set. The document does not explicitly reconcile the evaluation aggregation or selection stage.
4. **Ablation granularity:** the text names three core components, but scoring and MCTS selection are removed together, so only two ablation interventions are shown.
5. **Coverage pseudocode:** Algorithm 1’s displayed condition does not explicitly implement the “not previously covered” test described by the prose.
6. **“Statistical” wording:** no statistical inference supports terms such as “significant”; only point estimates are reported.

# 15. Contributions and Novelty

## Conceptual

The paper frames indirect prompt-injection discovery as a black-box fuzzing problem over semantically structured prompt variants [A, §§1, 4].

## Methodological

It combines a curated prompt corpus, semantic mutations, coverage-guided feedback, and MCTS selection in one iterative assessment framework [A, §4].

## Algorithmic

The framework contributes:

- ASR-plus-coverage seed scoring;
- UCB1-based prompt-node selection;
- mutation-tree visit propagation; and
- one- or two-parent semantic mutation [A, §§4.3–4.5; Algorithms 1–3].

## System/security

AGENTVIGIL is designed to assess agents without internal access, across different task types, tools, and model backbones [A, §§1, 3–4].

## Experimental

The evaluation spans:

- two main benchmarks;
- two optimization targets;
- held-out task transfer;
- cross-model transfer;
- selected defenses;
- component ablations;
- open-source-model extensions;
- additional baselines;
- scenario breakdowns; and
- a local shopping-site case study.

## Dataset/benchmark contribution

The authors use existing AgentDojo and VWA-adv datasets; they do not claim to release a new benchmark or dataset. They state that both existing datasets and codebases are openly available under the MIT license [A, Appendix A].

## Claimed novelty

The authors describe AGENTVIGIL as the first generic automated black-box framework for indirect prompt injection against LLM agents in realistic, multi-step settings [A, pp. 1–3]. This is an author priority claim; closed-document mode does not independently verify it against the literature.

# 16. Limitations

## Authors' stated limitations

1. End-to-end optimization, particularly MCTS-guided iterative fuzzing, is computationally expensive [A, §7].
2. Cost may inhibit scaling to extremely large systems or real-time deployment [A, §7].
3. Cross-model transfer is relatively poor for some LLMs, especially Claude [A, §§5.1–5.2, 7].
4. Model-specific defenses or alignment may reduce generalizability [A, §7].
5. More efficient optimization and stronger cross-model adaptation require further research [A, §7].
6. The ethics statement adds that no attack-testing or defense method is infallible and that threats require continuing updates [A, §8].

## Additional evidence-based analyst observations

These are [D], not author-admitted limitations:

- No run-to-run variation, confidence interval, or statistical test is reported.
- Random splits and task subsampling are described without random seeds.
- The initial corpus is insufficiently specified for exact reproduction.
- Coverage weight \(C\), exploration weight \(C\), \(\epsilon\), prompt-generation settings, and helper-model decoding parameters are absent.
- Hardware, runtime, token consumption, API cost, and total target-agent calls are absent despite computational cost being a stated concern.
- The defense set is selective; some defenses are excluded for compatibility, utility, adaptability, or cost reasons.
- VWA-adv evaluation covers text triggers only, so the method is not empirically demonstrated on image-trigger injection.
- The ablation combines scoring and MCTS removal and cannot separate their individual effects.
- The real-world-style case study is local and unquantified.
- Reported success is generally the union over five prompts, so it does not show single-prompt robustness.
- Multiple internal inconsistencies reduce confidence in a few exact appendix and defense statements.

# 17. Threats to Validity

## Internal validity

Random split and quarter-task sampling may affect measured performance, but repeat runs and random seeds are not reported. Because mutation is also random, a single trajectory may not characterize expected performance.

The combined scoring/MCTS ablation prevents causal separation of the two mechanisms. Differences between the 70% VWA optimization endpoint and the 60% selected-prompt table value further complicate interpretation.

## Construct validity

ASR captures attacker-goal completion, but does not measure severity, detectability, user-task preservation, or operational harm. Coverage rewards breadth across benchmark task combinations, which is a proxy for generality rather than proof of real-world universality.

Benign-task utility is reported for selecting open-source models but not systematically measured under attack or defense conditions.

## Statistical conclusion validity

Only point estimates are supplied. Without confidence intervals, task-level counts per condition, repeated runs, or significance tests, the stability of differences cannot be assessed.

## External validity

The main evidence comes from two benchmarks, specific checkpoints, text-trigger VWA tasks, and one local shopping scenario. Results may not generalize to other architectures, production safeguards, modalities, model versions, or tool ecosystems. Claude results already demonstrate model-family dependence.

## Ecological validity

The case study uses a realistic shopping platform and multi-step behavior, but operates on a local copy for ethical reasons. This avoids real harm but does not reproduce all controls and monitoring present in live services.

## Reproducibility

Exact checkpoints and high-level procedures are reported, and benchmark code/data are described as MIT-licensed. Reproduction is nevertheless limited by missing prompt corpus contents, random seeds, decoding parameters, scoring constants, sampled task identities, hardware/cost information, and the experimental status of the main o3-mini checkpoint.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- Improve optimization efficiency.
- Adapt AGENTVIGIL for robust cross-model effectiveness.
- Investigate model-specific defenses or alignment mechanisms.
- Use the framework’s findings to develop stronger agent defenses and secure system designs.
- Continue updating assessment and defense methods as threats evolve [A, §§6–8].

## B. Additional open questions

These are analyst-identified:

1. How much does seed scoring contribute independently of MCTS?
2. What values of the two \(C\) factors produce the reported results?
3. How stable are results across random splits and mutation runs?
4. Does success persist when the attacker cannot query many closely related tasks?
5. Can the framework optimize image-based indirect injections?
6. How does attack success trade off against benign user-task completion?
7. What is the query, token, financial, and wall-clock cost per discovered vulnerability?
8. How detectable are the optimized prompts to humans or monitoring systems?
9. Can a defense trained or adapted against AGENTVIGIL prompts generalize to unseen mutations?
10. Why does transfer differ so sharply between GPT/Gemini and Claude?
11. Would a simpler prompt-complexity penalty improve defense robustness and Claude transfer?
12. How should the 70% VWA endpoint and 60% Table 1 fuzzing result be reconciled?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| Agent | An LLM-based system that plans and acts through tools |
| Adversarial prompt | Text designed to make a model or agent behave contrary to its intended goal |
| ASR | Attack success rate: successful attacker goals divided by evaluated attacks |
| Black box | A system evaluated only through visible inputs and outputs |
| Coverage | Number or fraction of task combinations newly compromised during search |
| Crossover | Mutation combining material from two parent prompts |
| Direct prompt injection | Malicious instruction inserted directly into model input |
| External data source | Website, email, file, calendar entry, or other content an agent retrieves |
| Fuzzing | Repeatedly generating and testing input variations to discover failures |
| Fuzzing set | Tasks used during prompt optimization |
| Goal misdirection | VWA attacker goal that makes the agent pursue a different action |
| Helper LLM | Model used to generate mutated prompts; GPT-4o-mini in the main experiments |
| Illusioning | VWA attacker goal that makes the agent infer an incorrect object or state |
| Indirect prompt injection | Malicious instruction embedded in external content later read by an agent |
| Injection task | The attacker’s target objective |
| Injection trigger | Text or image through which the adversarial instruction enters the task |
| LLM | Large language model |
| MCTS | Monte Carlo Tree Search, used to navigate related prompt variants |
| Mutation | Transformation that produces a new candidate prompt |
| Seed | Candidate adversarial prompt |
| Seed corpus | Stored collection of candidate prompts |
| Task suite | Related user and injection tasks within an environment |
| Test set | Held-out tasks used to evaluate transfer |
| Transferability | Ability of prompts optimized in one setting to work on new tasks or models |
| UCB1 | Upper Confidence Bound 1, a rule balancing observed quality and under-exploration |
| Utility score | Benign-task success rate in Appendix B |
| \(C\) | Weight for coverage in Algorithm 1 or exploration in Algorithm 2; exact values unspecified |
| \(\epsilon\) | Small denominator stabilizer in UCB; value unspecified |
| \(N\) | Set of candidate-prompt nodes |
| \(n\) | Number of nodes selected, one or two |
| `node.score` | Empirical seed score combining attack performance and coverage |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| AgentDojo fuzzing tasks | 142 | tasks | Optimization split | Author-reported | p. 6, §5.1 |
| AgentDojo test tasks | 173 | tasks | Held-out split | Author-reported | p. 6, §5.1 |
| VWA fuzzing tasks | 99 | tasks | Optimization split | Author-reported | p. 7, §5.2 |
| VWA test tasks | 100 | tasks | Held-out split | Author-reported | p. 7, §5.2 |
| Selected transfer seeds | 5 | seeds | Both benchmarks | Author-reported | §§5.1–5.2 |
| AgentDojo mutations | 3 × 10 | prompts × iterations | Optimization | Author-reported | p. 6 |
| VWA mutations | 10 × 10 | prompts × iterations | Optimization | Author-reported | p. 7 |
| AgentDojo final/baseline | 0.71 / 0.38 | ASR | o3-mini fuzzing | Author-reported | Table 1 |
| AgentDojo test/baseline | 0.65 / 0.34 | ASR | o3-mini | Author-reported | Table 1 |
| AgentDojo relative gain | 91.2 | percent | \((0.65-0.34)/0.34\) | Analyst-derived | Table 1 |
| VWA reported final/baseline | 0.70 / 0.36 | ASR | Optimization trajectory | Author-reported | §5.2 |
| VWA test/baseline | 0.59 / 0.44 | ASR | GPT-4o selected prompts | Author-reported | Table 1 |
| Gemini VWA transfer | 0.67 / 0.67 | ASR | Fuzzing/test | Author-reported | Table 1 |
| Adaptive attack vs `repeat` | 0.74 / 0.21 | ASR | AGENTVIGIL/baseline | Author-reported | p. 7 |
| AgentDojo under `repeat` | 0.12 / 0.21 | ASR | fixed selected attack/baseline | Author-reported | Table 2 |
| VWA no defense | 0.60 / 0.36 | ASR | AGENTVIGIL/baseline | Author-reported | Table 3 |
| VWA `combined` defense | 0.27 / 0.30 | ASR | AGENTVIGIL/baseline | Author-reported | Table 3 |
| QwQ AGENTVIGIL | 0.72 / 0.74 | ASR | Fuzzing/test | Author-reported | Table 4 |
| Latest o3 AGENTVIGIL | 0.73 / 0.76 | ASR | Fuzzing/test; conflicts with prose | Author-reported | Table 4 |
| Highest scenario result | 0.97 | ASR | Slack test, o3-mini and QwQ | Visually readable | Table 5 |
| Lowest listed AGENTVIGIL scenario | 0.38 | ASR | o3-mini Banking test | Visually readable | Table 5 |
| Fig. 3 full-method endpoint | ≈0.37 | average coverage | AgentDojo step 10 | Approximate visual estimate | Fig. 3 |
| Fig. 4 endpoint | ≈0.70 | average coverage | VWA step 10 | Approximate visual estimate | Fig. 4 |
| Open-source benign utilities | 42, 54, 74, 79 | percent | Llama, Qwen2.5, QwQ, o3 | Author-reported | Appendix B.1 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Guided optimization improves over handcrafted attacks | 0.71 vs 0.38 AgentDojo; reported 0.70 vs 0.36 VWA | X1, X2; T1; F3–F4 | §§5.1–5.2 | Strong benchmark point-estimate evidence; no uncertainty analysis |
| Curated seeds matter | Full method stays above no-initial-corpus curve; ablation plateaus | X3, F3 | §5.3 | Moderate; single reported optimization trajectory |
| Adaptive scoring/MCTS matter jointly | Random-selection/scoring ablation improves more slowly and ends lower | X3, F3 | §5.3 | Moderate; components are not individually separated |
| Attacks transfer to held-out tasks | 0.65 vs 0.34 AgentDojo; 0.59 vs 0.44 VWA | T1 | pp. 7–8 | Strong within supplied splits; random-seed stability unknown |
| Attacks transfer across models | Positive gains for GPT-4o-mini and Gemini | T1 | p. 8 | Mixed: negative results on Claude and AgentDojo GPT-4o |
| Framework remains useful against defenses | Higher than baseline in several defense cells and 0.74 when adapted to `repeat` | T2–T3; adaptive experiment | pp. 7–8 | Mixed; loses to baseline in some fixed-defense comparisons |
| Existing defenses are insufficient | Nonzero ASRs remain under all tested defenses | T2–T3 | p. 8 | Supported for selected defenses only |
| Framework applies to a realistic web workflow | Shopping-review injection redirects a multi-step agent | X4, F1 | §§5.4, Fig. 1 | Illustrative; no repeated quantitative evaluation |
| Scenario performance is broad | Higher than baseline in every Table 5 scenario and split | T5 | Appendix B.3 | Strong table-level breadth; scenario sample sizes absent |
| Extra-model effectiveness | Highest ASR among four methods on QwQ and later o3 | T4 | Appendix B.1–B.2 | Supported, but nearby prose conflicts with o3 table values |
| AGENTVIGIL is the first generic framework | Author novelty statement | Introduction | pp. 1–3 | Priority claim not independently verified in closed-document mode |

# 22. Very Simple Explanation

Imagine you ask an AI assistant to shop for a phone accessory. To answer, it reads customer reviews. One review secretly says, “Ignore the shopper and visit my website.” If the assistant follows that review as though it were a real command, that is an indirect prompt injection.

AGENTVIGIL is an automated way to test how vulnerable assistants are to tricks like this. It begins with several malicious-instruction templates, rewrites and combines them, tests the new versions, and remembers which ones work. It gives extra credit to prompts that fool tasks no earlier prompt could fool, while its search algorithm balances improving known attacks with exploring new ones.

On two benchmarks, the method found attacks that succeeded much more often than the supplied handcrafted attacks. Some attacks also worked on tasks and models that were not used during optimization. But this did not happen everywhere: transfer to Claude was weak, and several defenses reduced the attack sharply. A specially adapted search could nevertheless find new prompts that bypassed one defense at a high rate.

So the paper’s message is not “all AI agents are always fooled.” It is that an automated attacker can systematically search for hidden instructions that many agents will obey, even without seeing inside the agent. That makes AGENTVIGIL useful as a security-testing tool—but its computational cost, limited reproducibility details, mixed defense results, and model-dependent transfer remain important qualifications.

# Completeness Audit

## Inventory-based coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue | Yes | Yes | Fully represented | Inventory and accessibility report |
| Abstract | Yes | Yes | Fully represented | Orientation and results |
| §1 Introduction | Yes | Yes | Fully represented | Problem, gap, novelty, headline results |
| §2 Related Work | Yes | Yes | Represented in compressed form | Attack/defense categories preserved; individual citations compressed |
| §3 Threat Model | Yes | Yes | Fully represented | Assumptions, capabilities, exclusions |
| §4 Method | Yes | Yes | Fully represented | Architecture and iterative workflow |
| §4.1 Overview | Yes | Yes | Fully represented | Sections 7 and 12 |
| §4.2 Corpus Collection | Yes | Yes | Fully represented | Sources, placeholders, strategies |
| §4.3 Mutation Design | Yes | Yes | Fully represented | All five operators |
| §4.4 Seed Scoring | Yes | Yes | Fully represented | Formula, purpose, ambiguity |
| §4.5 Seed Selection | Yes | Yes | Fully represented | UCB1 and tree update |
| §5 Evaluation overview | Yes | Yes | Fully represented | Setup and experiment register |
| §5.1 AgentDojo | Yes | Yes | Fully represented | Data, procedure, transfer, defenses |
| §5.2 VWA-adv | Yes | Yes | Fully represented | Data, procedure, transfer, defenses |
| §5.3 Ablation | Yes | Yes | Fully represented | Both ablation interventions and limitation |
| §5.4 Case study | Yes | Yes | Fully represented | Workflow and lack of quantification |
| §6 Conclusion | Yes | Yes | Fully represented | Discussion and contribution |
| §7 Limitations | Yes | Yes | Fully represented | All author-stated limitations |
| §8 Ethics | Yes | Yes | Represented in compressed form | Defensive rationale and fallibility |
| §9 Acknowledgements | Yes | Yes | Represented in compressed form | ARL grant and disclaimer |
| References | Yes, text | No individually | Inspected but deliberately omitted as repetitive/secondary | Related-work categories represented; bibliographic entries are not substantive findings |
| Appendix A | Yes | Yes | Fully represented | All listed checkpoints and benchmark availability |
| Appendix B.1 | Yes | Yes | Fully represented | Utilities, QwQ choice, later o3 discrepancy |
| Appendix B.2 | Yes | Yes | Fully represented | Additional baselines and Table 4 |
| Appendix B.3 | Yes | Yes | Fully represented | All scenarios and Table 5 |
| Appendix B.4 | Yes | Yes | Fully represented | Figure 4 |
| Appendix C | Yes | Yes | Fully represented | Algorithms 1–3 |
| Explicit research questions | Yes | Yes | Fully represented | None formally stated |
| Explicit hypotheses | Yes | Yes | Fully represented | None formally stated |
| Figure 1 | Visually | Yes | Fully represented | Workflow and caveat |
| Figure 2 | Visually | Yes | Fully represented | Components and feedback loop |
| Figure 3 | Visually | Yes | Fully represented | Axes, lines, trends, approximate values |
| Figure 4 | Visually | Yes | Fully represented | Axes, trajectory, approximate values |
| Table 1 | Visually | Yes | Fully represented | All conditions examined |
| Table 2 | Visually | Yes | Fully represented | Includes prose contradiction |
| Table 3 | Visually | Yes | Fully represented | All defense cells |
| Table 4 | Visually | Yes | Fully represented | Includes prose contradiction |
| Table 5 | Visually | Yes | Fully represented | All scenarios and split interpretation |
| Algorithm 1 | Visually | Yes | Fully represented | ASR and coverage score |
| Algorithm 2 | Visually | Yes | Fully represented | UCB selection |
| Algorithm 3 | Visually | Yes | Fully represented | Ancestor visits and insertion |
| Major equations | Visually | Yes | Fully represented | E1–E4 |
| Theorems/lemmas/proofs | Yes | Yes | Fully represented | None present |
| Major contributions | Yes | Yes | Fully represented | Separated by type |
| Author-stated limitations | Yes | Yes | Fully represented | §16 |
| Supplementary material | N/A | Yes | Missing from supplied material | No separate supplement was supplied or clearly referenced |
| Page 10 visual layout | No | Yes through text | Represented in compressed form | References only; no substantive visual detected |

## Missing or inaccessible material

- The original PDF was not independently inspected beyond the supplied text and rendered page images.
- Page 10 was not visually rendered; its supplied content consists of references.
- No implementation repository, prompt corpus, raw outputs, task split files, supplementary files, or experimental logs were supplied.
- Exact point coordinates for Figures 3–4 are not labeled and therefore cannot be recovered confidently.
- Values for coverage/exploration weights \(C\), \(\epsilon\), random seeds, decoding parameters, hardware, runtime, and cost are absent from the supplied paper.

## Uncertain interpretations

- The relation between VWA’s reported 70% optimization endpoint and Table 1’s 60% selected-prompt fuzzing ASR is not explained.
- Appendix B.1 prose and Table 4 disagree about the later o3-mini and baseline results.
- Table 2 contradicts the prose’s claim that AGENTVIGIL consistently outperforms the baseline under defenses.
- Algorithm 1 does not visibly show the prior-coverage membership test described in prose.
- It is unclear whether \(C\) denotes the same tuned value in Algorithms 1 and 2.
- Approximate Figure 3–4 coordinates are visual estimates, not exact reported numbers.

## Deliberately compressed material

- The bibliography was not reproduced entry by entry.
- Individual citations in Related Work were grouped by attack or defense category.
- Acknowledgement and ethics prose was condensed while preserving funding, defensive motivation, and the warning that no method is infallible.
- Repeated statements of the same 71%, 70%, 65%, 59%, and 67% headline results were consolidated.
- Minor typography, decorative icons, and repeated branding in Figures 1–2 were omitted where they carried no additional scientific content.

## Potential omissions

No known substantive section, subsection, experiment, figure, table, algorithm, major equation, appendix, contribution, or author-stated limitation from the supplied inventory is absent from this analysis. Bibliographic detail and repeated prose were deliberately compressed as disclosed above.