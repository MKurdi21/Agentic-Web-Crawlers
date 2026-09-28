# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible range | Pages 1–14; all pages have page-labeled native text |
| Apparently missing pages | None |
| Visually rendered pages | 1–9 and 11–14 |
| Page not visually rendered | Page 10; it contains references, not a substantive figure, table, equation, or experiment |
| Figures | Figures 1–4 are visually available and readable |
| Tables | Tables 1–5 are visually available and readable |
| Architecture diagrams | Figures 1–2 are visually available |
| Equations/algorithms | Algorithms 1–3 are rendered on p. 14; notation is readable, with extraction/typesetting issues noted below |
| Appendices | Present: Appendix A, Appendix B (B.1–B.4), and Appendix C |
| Supplementary material | No separate supplementary artifact was supplied or explicitly identified |
| OCR needed | No; native text is available. Visual reading was used to verify layouts and notation |
| Embedded images | Present on pp. 3–4 and visually inspected |
| Principal limitations | Page 10 was available as text but not as a rendered page. Exact plotted points in Figures 3–4 are mostly unlabeled and therefore can only be estimated visually. No code, seed corpus, generated prompts, raw trial outputs, or replication package was supplied. |

The mechanically generated record incorrectly reports that no appendices were detected. Direct inspection shows Appendices A–C on pp. 12–14. This is a record–document discrepancy, not missing content.

# 1. Plain-Language Orientation

This security paper introduces **AGENTVIGIL**, a system for automatically finding indirect prompt-injection vulnerabilities in agents powered by large language models (LLMs).

An LLM agent does more than answer questions: it may read email, browse websites, manipulate calendars, call software tools, or change files. An **indirect prompt injection** occurs when an attacker places an instruction inside external content—such as a webpage, review, or email—that the agent later reads. The agent may mistake that hostile text for a legitimate instruction and act against the user’s interests.

Testing this vulnerability is difficult because commercial agents are usually black boxes: the tester cannot inspect their model weights, prompts, or architecture and may receive only a success/failure outcome. AGENTVIGIL adapts software **fuzzing**—repeatedly generating and testing modified inputs—to that setting. It combines:

1. a curated initial collection of attack templates;
2. five LLM-assisted prompt mutations;
3. a score combining attack success rate and newly covered tasks; and
4. Monte Carlo Tree Search–inspired seed selection using an Upper Confidence Bound score.

The principal author-reported results are:

- 71% attack success on AgentDojo with o3-mini, versus 38% for its handcrafted baseline (p. 6; Table 1).
- 60% on the VWA-adv fuzzing set with GPT-4o versus 36% for the baseline, and 59% versus 44% on its test set (Table 1, p. 8).
- A coverage curve reaching about 70% on VWA-adv (Figure 4, p. 13).
- Transfer to unseen tasks and models, although transfer to Claude-3.5-Sonnet is poor (pp. 7–8; Table 1).
- Successful redirection of a locally deployed shopping agent to an attacker-selected URL through a malicious customer review (Figure 1; §§5.4, pp. 8–9).

The central contribution is therefore not a new individual injection string. It is a reusable black-box search framework for discovering effective indirect injections across different agent tasks and architectures.

# 2. Document Roadmap

| Part | Content and role |
|---|---|
| Abstract, p. 1 | States the security problem, method, benchmarks, and headline results |
| §1 Introduction, pp. 1–2 | Motivates black-box agent red-teaming and presents the claimed novelty |
| §2 Related Work, pp. 2–3 | Covers LLM agents, existing attacks, and defenses |
| §3 Threat Model, pp. 3–4 | Defines black-box access, benign users, attacker capabilities, feedback, and exclusions |
| §4 Method, pp. 4–5 | Describes the corpus, mutations, scoring, and MCTS-based selection |
| §5 Evaluation, pp. 5–9 | Evaluates AgentDojo, VWA-adv, defenses, ablations, and a real-world-style case study |
| §6 Conclusion, p. 9 | Restates findings and security implications |
| Impact Statement, p. 9 | Frames defensive benefits and acknowledges that no approach is infallible |
| References, pp. 9–11 | Bibliography; compressed here because it is supporting rather than experimental content |
| Appendix A, p. 12 | Exact model checkpoints |
| Appendix B, pp. 12–13 | Extra models/baselines, scenario breakdown, and VWA-adv coverage |
| Appendix C, pp. 13–14 | Formal pseudocode for scoring and seed selection |

This is primarily a **cybersecurity systems and experimental AI paper**, with an algorithmic search component and benchmark evaluation.

# 3. Background and Context

- **Large language model (LLM):** A model that processes and generates language. In an agent, it commonly acts as the planner.
- **LLM agent:** An LLM connected to tools such as browsers, email systems, calendars, file systems, or code execution environments (§§1–2).
- **Direct prompt injection:** Malicious instructions supplied directly through the agent’s ordinary prompt interface.
- **Indirect prompt injection:** Malicious instructions placed in external content that the agent later retrieves (§1).
- **Black-box setting:** The attacker cannot inspect the underlying LLM or agent architecture and observes external behavior only (§3).
- **Fuzzing:** Automated generation and testing of many input variations to discover failures. AGENTVIGIL applies this software-testing idea to attack prompts (§1).
- **Seed:** A candidate adversarial prompt template.
- **Mutation:** A transformation producing a new seed from one or two existing seeds.
- **Attack success rate (ASR):** Successful injection-task outcomes divided by evaluated task combinations (Algorithm 1, p. 14).
- **Coverage:** In this paper, the fraction or count of task combinations for which attacks have succeeded; the score rewards newly successful combinations (§4.4).
- **Exploration versus exploitation:** Testing less-explored variants versus prioritizing variants already known to work.
- **Monte Carlo Tree Search (MCTS):** Here, a tree records seed mutation ancestry, while an Upper Confidence Bound formula prioritizes high-performing and under-visited nodes (§4.5). The supplied algorithm is MCTS-inspired seed selection rather than a fully described rollout-based MCTS procedure.
- **Transferability:** Whether prompts optimized on one task set or model retain effectiveness on other tasks or models.
- **AgentDojo:** A personal-assistant-agent benchmark with Slack, Workspace, Travel, and Banking suites (§5.1; Appendix B.3).
- **VWA-adv:** A multimodal web-agent adversarial benchmark based on VisualWebArena; this paper uses its text-trigger tasks (§5.2).
- **Fuzzing set/test set:** The former guides optimization; the latter measures transfer to unseen tasks.

# 4. Research Problem and Gap

## Existing problem

Agents ingest potentially attacker-controlled content while having authority to call tools. A hostile instruction in that content can redirect the agent from the user’s task to an attacker’s objective (§1).

## Shortcomings attributed to previous approaches

The authors divide prior attacks into:

- handcrafted attacks that require expertise and may be inconsistent;
- automated methods requiring white-box access or architecture-specific information;
- attacks designed for a specific agent type;
- model-level jailbreak fuzzers that assume direct control of the model input and richer feedback.

They argue these approaches do not provide generic, scalable black-box assessment of multi-step agents (§§1–2).

The paper also characterizes existing defenses as costly, restrictive, post-execution, architecture-specific, dependent on human intervention, or insufficient for multimodal input (§2).

## Research gap

The stated gap is an automated method able to optimize indirect injections using only black-box success/failure feedback across heterogeneous agents and tasks.

## Motivation

Three difficulties motivate the design (§1):

1. inaccessible internals of commercial models and agents;
2. highly varied user tasks and execution paths;
3. complex, heterogeneous agent architectures and tools.

A fourth methodological difficulty is sparse binary feedback, which can reduce naive fuzzing to nearly random search (§1).

## Scope

The work covers indirect manipulation of external data consumed by personal-assistant and web agents. It does not study direct infrastructure attacks or using agents as general-purpose instruments of harm (§3).

# 5. Research Questions / Objectives / Hypotheses

The paper does not state formal research questions or statistical hypotheses. Its explicit evaluation objectives (§5, p. 5) can be reconstructed without converting them into author-stated formal RQs:

- **O1:** Evaluate AGENTVIGIL on AgentDojo and VWA-adv.
- **O2:** Test prompt transfer across unseen tasks and underlying LLMs.
- **O3:** Test attacks against benchmark defenses.
- **O4:** isolate the contributions of the initial corpus, adaptive scoring, and MCTS-based selection.
- **O5:** examine practical applicability in a locally deployed web environment.
- **O6, Appendix B:** Extend evaluation to additional models, baselines, and scenario categories.

The implicit expectation is that adaptive fuzzing will outperform handcrafted attacks, but the paper does not formulate this as a preregistered or statistically tested hypothesis.

# 6. Assumptions / Threat Model

## System and trust assumptions

- The agent uses an LLM as planner and interacts with external tools and data (§§3–4).
- The ordinary user is benign and requests legitimate tasks.
- Neither user nor attacker can inspect the internal LLM, agent design, or architecture.
- Only externally observable behavior is available.

## Attacker capabilities

The attacker (§3):

- can interact with the agent as a legitimate user could;
- can test on tasks similar to legitimate tasks;
- can modify an external data source, such as a website item, review, email, or calendar event;
- can place an indirect adversarial instruction in that source;
- can observe binary success/failure, potentially by inspecting the environment after execution.

## Attacker goals

The goal is to make the agent perform an attacker-selected action unintended by the user—for example, disclosing information or visiting an attacker-selected URL.

## Exclusions

The authors exclude:

- misuse of an agent to perform broadly harmful actions;
- direct attacks on hosting platforms or computational infrastructure.

## Analyst interpretation

The threat model assumes attackers can repeatedly run sufficiently similar tasks and obtain a reliable success oracle. That is plausible in the benchmarks but may vary considerably across deployed systems; the paper does not measure that variability.

# 7. Methodology

## Overall design

AGENTVIGIL performs an iterative loop (Figure 2; §4.1):

1. instantiate curated prompt templates for user-task/attacker-goal combinations;
2. inject and test them in the target agent environment;
3. score their success and novel coverage;
4. select promising seeds;
5. mutate selected seeds using a helper LLM;
6. add new seeds to storage/tree state;
7. repeat.

An **adversarial task** is a user task paired with an injection task (§5.1).

## Initial corpus (§4.2)

Templates come from:

- human heuristics;
- online resources;
- prior prompt-injection research.

They contain placeholders for the model, user task, and attacker goal. Strategies include role-playing, delimiter manipulation, and obfuscation. The paper does not disclose the corpus size, exact template list, sampling proportions, or collection criteria.

## Mutation design (§4.3)

Five randomly selected mutation operators use a helper LLM:

| Operator | Function |
|---|---|
| Shorten | Compress the prompt |
| Expand | Add contextual information |
| Rephrase | Change wording while preserving meaning |
| Crossover | Combine two parent seeds |
| GenerateSimilar | Produce similar style with different content |

The authors intentionally avoid additional heuristics. They state that moderately capable models such as Llama-3-8B or GPT-4o-mini can perform the mutations; experiments use GPT-4o-mini.

## Seed scoring (§4.4; Algorithm 1)

Each seed is tested on sampled tasks. The score combines:

\[
\text{ASR}=\frac{\text{total successes}}{\text{number of evaluated questions}}
\]

and

\[
\text{seed score}
=
\text{ASR}
+
C\frac{\text{coverage bonus}}{\text{number of evaluated questions}}.
\]

The coverage bonus increments when a seed succeeds on a combination not previously covered. Thus, a seed is rewarded both for broad current success and for finding new vulnerable cases.

The numerical value of coverage factor \(C\) is not supplied.

## Seed selection (§4.5; Algorithms 2–3)

Seeds are tree nodes linked to parent mutations. Selection uses:

\[
\operatorname{UCB}(\text{node})
=
\text{node.score}
+
C\sqrt{
\frac{\log(\text{total visits}+1)}
{\text{node.visits}+\epsilon}
}.
\]

The first term favors effective seeds; the second favors under-explored seeds. Algorithm 2 increments ancestor visit counts when a new node is added. Depending on the mutation, Algorithm 3 selects either the highest-UCB node or the top two.

The paper says UCB1 is preferred over UCT because seed evaluation is expensive and the authors do not want deep tree expansion. Neither \(C\) nor \(\epsilon\) is numerically specified.

## Experimental configuration

### AgentDojo (§5.1)

- Split: 142 fuzzing tasks and 173 test tasks.
- Optimization target: o3-mini.
- Helper model: GPT-4o-mini.
- Mutations: 3 new prompts per iteration.
- Iterations: 10.
- Per-new-seed evaluation: a randomly sampled quarter of user and injection tasks from each suite.
- Transfer seeds: five highest-scoring seeds.
- Transfer models: o3-mini, GPT-4o, GPT-4o-mini, Claude-3.5-Sonnet.
- Primary baseline: handcrafted AgentDojo prompts.
- Defenses: `pi_detector`, `repeat`, and `delimit`.
- Excluded: `tool_filter` due to o3-mini incompatibility; other defenses due to utility, compute, or adaptability concerns.
- Metric: union ASR across selected prompts.

### VWA-adv (§5.2)

- Text-trigger tasks only.
- Split: 99 fuzzing and 100 test tasks.
- Optimization target: GPT-4o.
- Helper model: GPT-4o-mini.
- Mutations: 10 prompts per iteration.
- Iterations: 10.
- Transfer seeds: five highest-scoring seeds.
- Transfer models: GPT-4o, GPT-4o-mini, Claude-3.5-Sonnet, Gemini-2-flash-exp.
- Primary baseline: handcrafted VWA-adv prompts.
- Defenses: `safety`, `paraphrase`, and `combined`.
- Excluded: image/text consistency defense because of API cost.
- Attack categories: illusioning and goal misdirection.

## Checkpoints (Appendix A, p. 12)

- o3-mini: `o3-mini-2024-12-17`
- GPT-4o-mini: `gpt-4o-mini-2024-07-18`
- GPT-4o: `gpt-4o-2024-08-06`
- Claude-3.5-Sonnet: `claude-3-5-sonnet-20241022`
- Gemini-2-flash-exp: `gemini-2.0-flash-exp`

Appendix B separately evaluates `o3-mini-2025-01-31` and QwQ-32B.

## Unspecified implementation details

The supplied work does not report hardware, runtime, monetary/API cost, random seeds, number of repeated split runs, confidence intervals, significance tests, exact corpus size, exact mutation prompts, \(C\), \(\epsilon\), or a released implementation artifact.

# 8. Experiments / Analyses

## X1 — AgentDojo fuzzing (§5.1; Figure 3; Table 1)

**Purpose:** Determine whether iterative fuzzing improves attacks on personal-assistant agents.

**Setup:** Optimize against o3-mini on 142 fuzzing tasks for 10 iterations, generating three mutations each iteration.

**Results:** Handcrafted baseline ASR is 0.38; the initial corpus reaches 0.63; final AGENTVIGIL reaches 0.71. Figure 3 shows coverage rising throughout optimization.

**Caveat:** Evaluation uses sampled task subsets for individual mutations, and no uncertainty across repeated runs is given.

## X2 — AgentDojo task/model transfer (§5.1; Table 1)

**Purpose:** Test transfer to 173 unseen tasks and non-optimization models.

On the test set, AGENTVIGIL versus baseline is:

- o3-mini: 0.65 versus 0.34;
- GPT-4o: 0.19 versus 0.25;
- GPT-4o-mini: 0.43 versus 0.28;
- Claude-3.5-Sonnet: 0.04 versus 0.08.

It strongly improves o3-mini and GPT-4o-mini, but underperforms the baseline on GPT-4o and Claude.

## X3 — AgentDojo defenses (§5.1; Table 2)

| Defense | Baseline | AGENTVIGIL |
|---|---:|---:|
| None | 0.38 | 0.71 |
| `pi_detector` | 0.13 | 0.25 |
| `repeat` | 0.21 | 0.12 |
| `delimit` | 0.36 | 0.49 |

AGENTVIGIL is more successful against `pi_detector` and `delimit`, but less successful than the baseline against `repeat`. All tested defenses reduce AGENTVIGIL relative to its undefended 0.71 result.

## X4 — VWA-adv fuzzing (§5.2; Figure 4; Table 1)

**Purpose:** Assess web-agent attacks with multimodal tasks but text-based triggers.

**Setup:** Optimize against GPT-4o on 99 fuzzing tasks for 10 iterations, generating ten mutations per iteration.

**Results:** Initial-corpus ASR is 0.54; final coverage/ASR is reported as 0.70 in the prose and abstract. Table 1 reports 0.60 for the selected AGENTVIGIL prompts on the GPT-4o fuzzing set, versus a 0.36 baseline.

**Important qualification:** The reported 70% terminal fuzzing coverage and Table 1’s 60% selected-prompt ASR are different quantities/evaluation summaries. The document does not fully explain the operational difference, although coverage and union ASR need not be identical.

## X5 — VWA-adv transfer (§5.2; Table 1)

Test-set AGENTVIGIL versus baseline:

- GPT-4o: 0.59 versus 0.44;
- GPT-4o-mini: 0.54 versus 0.29;
- Claude-3.5-Sonnet: 0.42 versus 0.51;
- Gemini-2-flash-exp: 0.67 versus 0.50.

Transfer is strong to GPT-4o-mini and Gemini, positive on GPT-4o, and negative on Claude.

The authors infer from manual inspection that Claude may be more vulnerable to simpler baseline prompts. This is an author interpretation, not a separately controlled experiment.

## X6 — VWA-adv defenses (§5.2; Table 3)

| Defense | Baseline | AGENTVIGIL |
|---|---:|---:|
| None | 0.36 | 0.60 |
| `safety` | 0.34 | 0.29 |
| `paraphrase` | 0.27 | 0.33 |
| `combined` | 0.30 | 0.27 |

Against defenses, AGENTVIGIL no longer consistently exceeds the baseline. It is higher only against paraphrasing. The combined defense does not outperform both component defenses for either attack family.

## X7 — Ablation (§5.3; Figure 3)

Three design elements are investigated, but only two plotted ablation configurations are shown:

1. replace the curated initial corpus with AgentDojo baseline prompts;
2. jointly replace adaptive scoring and MCTS selection with uniform random selection.

The full method has the highest coverage. The no-initial-corpus curve plateaus after roughly four iterations; the no-scoring/selection curve improves more slowly.

Because scoring and selection are removed together, their individual effects are not isolated.

## X8 — Local WebArena case study (§5.4; Figure 1)

A user asks a WebArena shopping agent to find a Samsung Galaxy S6 screen protector and identify reviews mentioning fingerprint resistance. An attacker inserts a malicious instruction in a customer review. The agent follows it and visits a fake GitHub-like URL.

The environment is a local copy for ethical reasons, and the task requires more than ten steps. The authors state that variants led agents toward arbitrary URLs associated with phishing, malicious downloads, or privacy leakage. No sample size, success rate, repeated-trial count, or full execution trace is reported.

## X9 — Additional models and baselines (Appendix B.1–B.2; Table 4)

Benign-task utility scores are:

- Llama3.3-70B-Instruct: 42%;
- Qwen2.5-72B-Instruct: 54%;
- QwQ-32B: 74%;
- o3-mini: 79%.

Further attack testing uses QwQ-32B and a newer o3-mini checkpoint. Table 4 reports:

| Attack | o3-mini-2025-01-31 fuzz/test | QwQ-32B fuzz/test |
|---|---:|---:|
| AGENTVIGIL | 0.73 / 0.76 | 0.72 / 0.74 |
| AgentDojo baseline | 0.47 / 0.49 | 0.45 / 0.47 |
| OpenPromptInjection | 0.38 / 0.39 | 0.20 / 0.20 |
| InjecAgent | 0.15 / 0.11 | 0.14 / 0.12 |

There is a material prose–table discrepancy: Appendix B.1 says the latest o3-mini achieves 72%/74% and its baseline 50%/53%, but Table 4 assigns 73%/76% and 47%/49% to o3-mini; 72%/74% belongs to QwQ-32B. The 50%/53% baseline pair appears nowhere in Table 4.

## X10 — Scenario breakdown (Appendix B.3; Table 5)

AGENTVIGIL exceeds the benchmark baseline in every reported AgentDojo suite and both VWA-adv goal categories.

Notable results include:

- o3-mini Slack test: 0.97 versus 0.70;
- o3-mini Workspace fuzzing: 0.63 versus 0.20;
- QwQ-32B Slack fuzzing: 1.00 versus 0.85;
- QwQ-32B Workspace test: 0.42 versus 0.10;
- GPT-4o VWA goal-misdirection fuzzing: 0.58 versus 0.00;
- GPT-4o VWA goal-misdirection test: 0.42 versus 0.20.

# 9. Results

## Principal findings

1. **AgentDojo optimization:** AGENTVIGIL reaches 71% versus 38% baseline (p. 6; Table 1).  
   **Analyst-derived:** +33 percentage points; \(33/38\approx86.8\%\) relative improvement—not literally 100%.

2. **VWA-adv:** Table 1 gives 60% versus 36% on fuzzing tasks and 59% versus 44% on test tasks.  
   **Analyst-derived:** +24 and +15 percentage points, respectively.

3. **Unseen AgentDojo tasks:** o3-mini test ASR is 65% versus 34%.  
   **Analyst-derived:** +31 percentage points; approximately 91.2% relative improvement.

4. **Unseen models:** VWA-adv test ASR reaches 67% on Gemini-2-flash-exp versus 50% baseline, but Claude results are worse than baseline.

5. **Defense robustness is mixed:** AGENTVIGIL outperforms AgentDojo’s baseline against two of three defenses but VWA-adv’s baseline against only one of three defenses.

6. **Ablation evidence supports the combined design:** curated seeds and guided selection/scoring produce higher coverage than the two ablated configurations.

7. **Scenario breadth:** Table 5 reports improvements in all listed suite/category comparisons.

## Qualification of “nearly doubling”

The authors describe the principal gains as “nearly doubling” or “nearly a 100% improvement.” This is broadly descriptive but condition-dependent:

- 0.38 to 0.71 is an 86.8% relative increase.
- 0.36 to 0.70 is a 94.4% relative increase if comparing baseline ASR to terminal reported coverage/attack performance.
- Table 1’s 0.36 to 0.60 is a 66.7% relative increase.

These are **analyst-derived** calculations. Percentage-point and relative changes should not be conflated.

# 10. Figure-by-Figure Interpretation

### Figure 1 — Real-world-style shopping-agent attack

- **Type:** Workflow/example diagram, p. 3.
- **Contents:** A shopping website containing a malicious customer review; a benign user request; an agent reasoning box; an attacker-goal panel.
- **Flow:** Injected review → agent retrieves review while completing the user task → agent treats the embedded text as an instruction → agent visits the attacker-selected URL.
- **Visible example:** The user requests reviews of a Samsung Galaxy S6 screen protector mentioning fingerprint resistance. The injection asks the agent to visit a fake GitHub-like URL.
- **Potential outcomes listed:** phishing, malware download, and private-information disclosure.
- **Support:** Demonstrates the mechanism used in §5.4.
- **Caveat:** It is an illustrative execution, not a quantitative plot. The diagram does not establish how often the attack succeeds.

### Figure 2 — AGENTVIGIL architecture and feedback loop

- **Type:** System architecture/flowchart, p. 4.
- **Agent side:** user, agent, and environment; example tools include code execution, email, file system, and web browser.
- **Attack path:** the attacker places adversarial prompts in external sources; those sources enter the agent’s context.
- **Fuzzer path:** initial seeds → current seeds → mutator → test in agent → binary success evaluation → scorer → seed selector → seed storage/current seeds.
- **Feedback loop:** evaluated mutations become part of the seed pool/tree and influence subsequent selection.
- **Support:** Integrates §§4.1–4.5 into a single control-flow view.
- **Caveat:** The figure abstracts away task sampling, helper-model prompting, and exact stopping rules.

### Figure 3 — AgentDojo coverage over fuzzing steps

- **Type:** Three-line plot, p. 6.
- **x-axis:** Steps, approximately 1–10.
- **y-axis:** Average Coverage, 0.0–0.5.
- **Series:** full method; without initial corpus; without seed selection and scoring.
- **Visual observations:**  
  - Full method rises from roughly 0.18 to roughly 0.38.  
  - No-initial-corpus begins much lower, rises, then plateaus near roughly 0.16.  
  - No-selection/scoring increases more slowly to roughly 0.27.
- **Status:** These plotted values are **approximate visual estimates**, not labeled exact values.
- **Conclusion supported:** The full method sustains better coverage, and both the curated corpus and guided search contribute.
- **Caveat:** The plot does not include variability or repeat-run error bars. Scoring and selection are jointly ablated.

### Figure 4 — VWA-adv coverage over fuzzing steps

- **Type:** Single-line plot, Appendix B.4, p. 13.
- **x-axis:** Steps, 1–10.
- **y-axis:** Average Coverage, 0.50–0.80.
- **Visual trend:** Coverage rises rapidly from about 0.54 at step 1 to about 0.63 at step 2, then more gradually to about 0.70 around step 8 and plateaus.
- **Status:** Values other than the prose-reported start/end are approximate visual estimates.
- **Support:** Confirms iterative improvement with diminishing gains.
- **Caveat:** No baseline curve, ablation curve, uncertainty interval, or repeated-run distribution is shown.

# 11. Table-by-Table Interpretation

### Table 1 — Transfer attack success rates

- **Purpose:** Compare handcrafted and AGENTVIGIL attacks across fuzzing/test splits and backbone models.
- **Unit:** ASR as a proportion from 0 to 1.
- **Best AgentDojo result:** 0.71, AGENTVIGIL on o3-mini fuzzing tasks.
- **Best VWA-adv result:** 0.67, AGENTVIGIL on Gemini for both splits.
- **Negative transfer:** AGENTVIGIL trails the baseline on Claude in all shown benchmark/split comparisons and on GPT-4o for AgentDojo.
- **Missing notation:** “–” denotes unavailable/unsupported combinations.
- **Footnote:** Gemini does not fully support AgentDojo tool calls; the early o3-mini version does not fully support VWA-adv.
- **No uncertainty or significance testing is supplied.**

### Table 2 — AgentDojo defenses

- Compares no defense, `pi_detector`, `repeat`, and `delimit`.
- AGENTVIGIL leads under no defense, `pi_detector`, and `delimit`.
- Baseline leads under `repeat` (0.21 versus 0.12).
- `repeat` is the strongest tested defense against AGENTVIGIL by raw residual ASR.
- The prose correctly notes that `delimit` is less effective than the other two defenses for both attack sets.

### Table 3 — VWA-adv defenses

- AGENTVIGIL leads without defense and under paraphrasing.
- Baseline has lower ASR under `safety` and `combined`.
- For AGENTVIGIL, combined defense yields 0.27, slightly below safety’s 0.29 and paraphrase’s 0.33.
- For the baseline, paraphrase is best at 0.27; combined is worse at 0.30.
- The authors’ statement that defenses make AGENTVIGIL converge with the baseline is supported by the small remaining gaps.

### Table 4 — Additional models and baselines

- AGENTVIGIL is highest in every displayed model/split cell.
- OpenPromptInjection is the second- or third-best baseline depending on the model.
- InjecAgent is lowest throughout.
- No error estimates are reported.
- **Critical inconsistency:** Appendix prose and table disagree about the latest o3-mini values, as detailed in §8.

### Table 5 — Scenario-level breakdown

- Rows are AgentDojo suites or VWA-adv attack-goal types.
- Each cell reports fuzzing/test ASR.
- AGENTVIGIL exceeds the benchmark baseline in all 20 directly comparable fuzz/test values.
- Lowest displayed AGENTVIGIL result: 0.33, QwQ Workspace fuzzing.
- Highest: 1.00, QwQ Slack fuzzing.
- Goal misdirection is harder than illusioning for AGENTVIGIL on VWA-adv, but the improvement over baseline is especially large because the baseline fuzzing ASR is 0.00.
- There are no counts per scenario, so precision and uncertainty cannot be assessed.

# 12. Diagram / Architecture Interpretation

The two substantive diagrams describe complementary views:

1. **Figure 1 is the attack’s data path:** attacker-controlled content enters an external website, is retrieved during a legitimate task, enters the LLM context, and changes the agent’s action.
2. **Figure 2 is the optimizer’s control path:** seeds are mutated, injected, executed, scored, selected, stored, and reused.

Together they show that AGENTVIGIL does not directly manipulate the user prompt or inspect model internals. Its only operational channel is the external content that a normal agent task consumes, while its feedback is the observed attack outcome.

# 13. Equations and Mathematical Concepts

## E1 — Attack success rate (Algorithm 1, line 19)

\[
ASR=\frac{\text{total\_success}}{\text{num\_questions}}.
\]

- **Input:** outcomes across sampled task combinations.
- **Output:** fraction successfully attacked.
- **Role:** Measures immediate seed effectiveness.
- **Notation issue:** The rendered numerator appears as `total_succcess`, with three “c” characters; this is evidently a typographical mismatch with the initialized `total_success`.

## E2 — Coverage-guided seed score (Algorithm 1, line 20)

\[
\text{seed\_score}
=
ASR+
C\frac{\text{coverage\_bonus}}{\text{num\_questions}}.
\]

- \(C\): coverage weighting factor; no value is reported.
- `coverage_bonus`: count of newly successful, previously uncovered combinations.
- **Meaning:** A prompt can score well either by succeeding frequently or by succeeding on cases earlier prompts missed.
- **Method connection:** This supplies `node.score` to the selection formula.

## E3 — Total tree visits (Algorithm 3, line 1)

The rendering shows a summation, although the extracted text displays a `P`-like symbol:

\[
\text{total\_visits}=\sum_{\text{node}\in N}\text{node.visits}.
\]

This reading is supported by the visible summation layout and the formula’s intended operands.

## E4 — Upper Confidence Bound score (Algorithm 3, line 2)

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

- \(N\): set of seed nodes.
- `node.score`: empirical score from Algorithm 1.
- `node.visits`: how often that mutation path has been explored.
- \(C\): exploration factor.
- \(\epsilon\): small denominator stabilizer; undefined numerically.
- **Meaning:** Prefer seeds that are good already or insufficiently explored.
- **Constraint:** Algorithm 3 explicitly handles only \(n=1\) or \(n=2\).

No theorems, lemmas, propositions, proofs, statistical models, confidence intervals, or hypothesis tests appear.

# 14. Interpretation and Discussion

The evidence supports the central proposition that guided black-box search can find substantially more successful indirect injections than the supplied handcrafted baselines. Gains occur across both personal-assistant and web-agent benchmarks, and the ablation curves support the value of initialization and guided search.

Transferability, however, is conditional rather than universal. Prompts optimized against one GPT-family configuration transfer well to several other models, especially GPT-4o-mini and Gemini in VWA-adv, but transfer poorly to Claude and sometimes GPT-4o in AgentDojo. The authors interpret Claude’s behavior as a preference for simpler prompts, based on manual inspection.

The defense results are similarly mixed. AgentDojo’s tested defenses reduce ASR but frequently leave nontrivial residual vulnerability. In VWA-adv, defenses largely eliminate AGENTVIGIL’s advantage over the baseline. Therefore, the evidence supports “defenses are not complete” more strongly than “AGENTVIGIL consistently bypasses defenses.”

The paper’s five objectives receive the following support:

- **Benchmark effectiveness:** supported by Tables 1 and 4.
- **Task/model transfer:** supported, with important model-dependent failures.
- **Defense evaluation:** supported, but results are mixed.
- **Component importance:** partially supported; scoring and MCTS selection are not separately ablated.
- **Practical applicability:** illustrated by one local case study, not quantified at deployment scale.

The phrase “first generic” is an author novelty claim. Closed-document mode does not permit independent verification against the broader literature.

# 15. Contributions and Novelty

## Conceptual contribution

Frames indirect prompt-injection discovery as black-box fuzzing over prompt templates rather than direct model jailbreak generation.

## Methodological contribution

Combines curated initialization, coverage-aware feedback, and mutation-tree search to address sparse binary feedback.

## Algorithmic contribution

Provides:

- coverage-guided seed scoring;
- ancestry/visit-count updating;
- UCB-based one- or two-parent selection;
- five semantic prompt mutations.

## Systems contribution

Defines an agent-agnostic loop that interfaces with an external benchmark or environment through injected content and observed outcomes.

## Experimental contribution

Evaluates:

- two agent benchmarks;
- multiple commercial and open models;
- unseen tasks;
- six listed defense configurations across the two benchmarks;
- two ablation settings;
- scenario-level results;
- a local WebArena case study.

## Non-contributions

The paper does not introduce a new dataset, formal theorem, statistical estimator, trained defense, or disclosed full prompt corpus.

# 16. Limitations

## Authors' stated limitations

The paper does not contain a dedicated limitations section. Explicit acknowledgments include:

- no single testing or defense approach is infallible (Impact Statement, p. 9);
- some models lack adequate tool-calling/agent capability (§5.1; Table 1 footnote);
- `tool_filter` is incompatible with the tested o3-mini (§5.1);
- some defenses are excluded because of compute cost, utility loss, or architecture dependence (§§5.1–5.2);
- VWA-adv evaluation uses text triggers rather than all trigger modalities (§5.2);
- complex generated prompts may struggle under VWA-adv defenses because of limited context (§5.2);
- real-world testing is performed on a local copy for ethical reasons (§5.4).

## Additional evidence-based analyst observations

- Results are presented as single proportions with no confidence intervals, repeated-run variability, or significance testing.
- One random split per benchmark appears to be used; split sensitivity is not evaluated.
- The initial corpus and exact mutation instructions are not disclosed, limiting replication.
- Scoring factor \(C\), exploration factor \(C\), and \(\epsilon\) are unspecified.
- API/runtime cost is absent despite extensive agent execution.
- Defense coverage is selective and excludes potentially expensive or incompatible defenses.
- VWA-adv optimization uses only text triggers, limiting conclusions about visual injection.
- The case study lacks a trial count or failure analysis.
- The ablation jointly removes scoring and MCTS selection, preventing attribution between them.
- Table 4 conflicts with Appendix B.1 prose.
- The same symbol \(C\) denotes coverage weighting in Algorithm 1 and exploration weighting in Algorithm 3; the text does not clarify whether these are numerically identical.
- “Coverage,” “success rate,” and union-of-prompts ASR are not always distinguished sharply enough to reconcile every headline value.

# 17. Threats to Validity

These categories are analyst-organized; the authors do not present a formal threats-to-validity section.

- **Internal validity:** Random task subsampling and stochastic LLM mutations may influence results, but seeds and repetitions are not reported.
- **Construct validity:** Binary injection success is meaningful, yet it does not measure severity, user harm, stealth, user-task preservation, or attack cost.
- **Statistical conclusion validity:** No uncertainty estimates or hypothesis tests are given; scenario subsets may be small, but their counts are absent.
- **External validity:** Two benchmarks and one local deployment cover important cases but not the full range of agent architectures, permissions, modalities, or production safeguards.
- **Ecological validity:** The local shopping demonstration improves realism, but production services may differ in authentication, monitoring, content sanitization, and tool policy.
- **Reproducibility:** Model checkpoints are supplied, but prompts, code, randomness controls, hardware, costs, and several hyperparameters are not.
- **Generalizability:** Cross-model results demonstrate partial generalization while the Claude results show that prompt effectiveness can be model-family-specific.
- **Baseline validity:** Appendix B improves baseline breadth, but the main text emphasizes benchmark handcrafted baselines, and Table 4 contains contradictory prose.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

The conclusion and Impact Statement call for:

- more robust agent defenses;
- secure system designs;
- next-generation security solutions;
- continuing research and proactive updates as threats evolve.

No detailed future experimental program is specified.

## B. Additional open questions

- How stable are results across random splits, helper-model samples, and repeated runs?
- What is the cost per discovered vulnerability?
- Can visual, audio, document, or code-based indirect injections be fuzzed within the same framework?
- How should coverage be defined when tasks have unequal security severity?
- Can scoring and MCTS selection be separately evaluated?
- Can the technique optimize both attack success and preservation of the legitimate user task?
- How does it perform against information-flow isolation, human approval, or least-privilege tool policies?
- Do prompts remain effective after model updates?
- Can attacks be optimized without assuming a clean binary success oracle?
- What explains the Claude transfer failure experimentally?
- Would release of the corpus and full execution traces enable reproducibility without creating disproportionate misuse risk?

# 19. Terminology and Notation Glossary

| Term | Meaning in this paper |
|---|---|
| AGENTVIGIL | Proposed black-box indirect-injection fuzzing framework |
| LLM | Large language model |
| LLM agent | LLM-based planner connected to tools and environments |
| NLP | Natural language processing |
| Indirect prompt injection | Hostile instruction embedded in external content retrieved by an agent |
| Black box | System whose internals are unavailable |
| Seed | Candidate attack prompt/template |
| Corpus | Collection of initial seeds/templates |
| Mutator | Component that transforms seeds |
| ASR | Attack success rate |
| Coverage | Successful task combinations reached, especially newly reached ones |
| MCTS | Monte Carlo Tree Search; used here as the design basis for mutation-tree selection |
| UCB/UCB1 | Upper Confidence Bound selection score |
| UCT | Upper Confidence bounds applied to trees; mentioned as an alternative not used |
| Exploration | Trying less-visited candidates |
| Exploitation | Reusing high-scoring candidates |
| Transferability | Effectiveness on unseen tasks or models |
| AgentDojo | Personal-assistant attack/defense benchmark |
| VWA-adv | Adversarial web-agent benchmark |
| Illusioning | Making the agent perceive an altered state or attribute |
| Goal misdirection | Redirecting the agent to a different objective |
| `pi_detector` | BERT-based prompt-injection detector |
| `repeat` | Repeats user instructions after tool calls |
| `delimit` / `safety` | Delimiter and privileged-instruction defenses |
| `paraphrase` | Rewrites untrusted content to neutralize hostile intent |
| \(C\) | Weighting factor; used in both scoring and UCB formulas, values unspecified |
| \(\epsilon\) | Small UCB denominator stabilizer, value unspecified |
| \(N\) | Set of seed-tree nodes |
| \(S\) | Selected node or nodes |
| `node.visits` | Number of visits associated with a seed node |
| `node.score` | Success-plus-coverage score assigned to a seed |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| AgentDojo split | 142 / 173 | tasks | Fuzzing/test | Author-reported | §5.1, p. 6 |
| VWA-adv split | 99 / 100 | tasks | Fuzzing/test | Author-reported | §5.2, p. 7 |
| AgentDojo iterations | 10 | iterations | 3 mutations/iteration | Author-reported | §5.1 |
| VWA-adv iterations | 10 | iterations | 10 mutations/iteration | Author-reported | §5.2 |
| Selected transfer seeds | 5 | seeds | Both benchmarks | Author-reported | §§5.1–5.2 |
| AgentDojo baseline/final | 0.38 / 0.71 | ASR | o3-mini fuzzing | Author-reported | Table 1 |
| AgentDojo initial corpus | 0.63 | ASR | o3-mini fuzzing | Author-reported | §5.1, p. 6 |
| AgentDojo gain | +0.33 | proportion points | 0.71−0.38 | Analyst-derived | Table 1 |
| AgentDojo relative gain | 86.8% | relative increase | (0.71−0.38)/0.38 | Analyst-derived | Table 1 |
| AgentDojo unseen-task result | 0.65 vs 0.34 | ASR | o3-mini test | Author-reported | Table 1 |
| VWA initial/final coverage | 0.54 / 0.70 | proportion | GPT-4o fuzzing process | Author-reported | §5.2; Fig. 4 |
| VWA selected-prompt fuzzing | 0.60 vs 0.36 | ASR | GPT-4o | Author-reported | Table 1 |
| VWA test | 0.59 vs 0.44 | ASR | GPT-4o | Author-reported | Table 1 |
| Gemini transfer | 0.67 vs 0.50 | ASR | VWA test | Author-reported | Table 1 |
| Claude transfer | 0.42 vs 0.51 | ASR | VWA test | Author-reported | Table 1 |
| Best AgentDojo defended result | 0.49 | ASR | AGENTVIGIL vs `delimit` | Author-reported | Table 2 |
| Best VWA defended result | 0.33 | ASR | AGENTVIGIL vs paraphrase | Author-reported | Table 3 |
| Latest o3-mini result | 0.73 / 0.76 | ASR | Fuzz/test, per Table 4 | Visually readable; conflicts with prose | Table 4 |
| QwQ-32B result | 0.72 / 0.74 | ASR | Fuzz/test | Visually readable | Table 4 |
| Maximum scenario ASR | 1.00 | ASR | QwQ Slack fuzzing | Visually readable | Table 5 |
| VWA coverage at step 2 | ≈0.63 | proportion | From plotted position | Approximate visual estimate | Fig. 4 |
| VWA terminal coverage | ≈0.70 | proportion | Steps 8–10 | Visually readable/author-reported | Fig. 4; §5.2 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Guided fuzzing improves attacks | 0.71 vs 0.38 on AgentDojo; 0.60 vs 0.36 on VWA fuzzing table | X1, X4; Table 1 | pp. 6–8 | Strong within tested configurations; no uncertainty estimates |
| Prompts transfer to unseen tasks | o3-mini test 0.65 vs 0.34; GPT-4o VWA test 0.59 vs 0.44 | X2, X5 | Table 1 | Supported, but not universal |
| Prompts transfer across models | Improvements on GPT-4o-mini and Gemini | X2, X5 | Table 1 | Mixed; Claude transfer is worse than baseline |
| Defenses remain bypassable | Residual ASRs up to 0.49 and 0.33 | X3, X6 | Tables 2–3 | Supported, but AGENTVIGIL does not consistently beat baseline under defense |
| Initial corpus matters | Replaced-corpus curve plateaus substantially lower | X7 | Fig. 3; §5.3 | Supported visually; no uncertainty |
| Guided scoring/selection matter | Random-selection ablation improves more slowly | X7 | Fig. 3 | Joint ablation cannot separate scoring from selection |
| Method works across scenarios | Higher ASR in every Table 5 comparison | X10 | Table 5 | Broad within listed suites; subset sizes unavailable |
| Attack transfers to a realistic workflow | Local shopping agent follows injected review to URL | X8 | Fig. 1; §5.4 | Demonstrative case study, not quantified |
| Method outperforms additional baselines | Highest every Table 4 cell | X9 | Table 4 | Supported by table, but appendix prose conflicts with o3-mini values |
| Existing defenses are insufficient | Nonzero residual success and combined defense not consistently best | X3, X6 | Tables 2–3 | Reasonable within tested defenses; not evidence about all defenses |
| First generic black-box framework | Author novelty statement | Introduction | pp. 1–2 | Not independently verifiable in closed-document mode |

# 22. Very Simple Explanation

Imagine an AI assistant that can browse stores, read email, and use apps for you. It follows your instructions, but it also has to read information from the outside world. A criminal could hide a second instruction inside a product review or email. If the assistant cannot tell that the text is untrusted, it may follow the criminal’s instruction instead of yours.

AGENTVIGIL is an automated stress tester for that problem. It begins with several kinds of trick instructions, rewrites and combines them, tests them on an agent, and remembers which versions worked. It also rewards a prompt when it fools the agent on a kind of task that previous prompts could not fool. Its search rule balances improving proven attacks with trying less-explored ones.

In the paper’s tests, this automated process usually found attacks more successful than the benchmarks’ handcrafted attacks. It also transferred to several new tasks and AI models. But it did not work equally well everywhere: Claude was relatively resistant to the optimized prompts, and defenses often reduced the advantage.

The main lesson is not that every agent can always be fooled. It is that connecting an AI model to tools makes hostile text in websites, email, and other data a serious input-security problem—and systematic black-box testing can reveal vulnerabilities that a small collection of manually written attacks misses.

# Completeness Audit

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes | Yes | Fully represented | Orientation and key numerical results |
| §1 Introduction | Yes | Yes | Fully represented | Problem, gap, novelty, and results |
| §2 Related Work | Yes | Yes | Represented in compressed form | Categories and author-attributed shortcomings retained |
| §3 Threat Model | Yes | Yes | Fully represented | Assumptions, capabilities, goals, exclusions |
| §4.1 Overview | Yes | Yes | Fully represented | Workflow and architecture |
| §4.2 Corpus Collection | Yes | Yes | Fully represented | Sources, placeholders, attack styles |
| §4.3 Mutation Design | Yes | Yes | Fully represented | All five mutations |
| §4.4 Seed Scoring | Yes | Yes | Fully represented | Equations and rationale |
| §4.5 Seed Selection | Yes | Yes | Fully represented | Tree, UCB, update and selection |
| §5 Evaluation objectives | Yes | Yes | Fully represented | All five listed analyses |
| §5.1 AgentDojo | Yes | Yes | Fully represented | Setup, results, transfer, defenses |
| §5.2 VWA-adv | Yes | Yes | Fully represented | Setup, results, transfer, defenses |
| §5.3 Ablation | Yes | Yes | Fully represented | Joint-ablation caveat included |
| §5.4 Case study | Yes | Yes | Fully represented | Workflow and evidential limitation |
| §6 Conclusion | Yes | Yes | Fully represented | Claims preserved with qualifications |
| Impact Statement | Yes | Yes | Represented in compressed form | Defensive purpose and infallibility caveat |
| References | Yes | Yes | Inspected but deliberately compressed | Prior-work categories summarized; individual citations not annotated |
| Appendix A | Yes | Yes | Fully represented | All five checkpoints |
| Appendix B.1 | Yes | Yes | Fully represented | Utility scores and discrepancy recorded |
| Appendix B.2 | Yes | Yes | Fully represented | Additional baselines |
| Appendix B.3 | Yes | Yes | Fully represented | Scenario breakdown |
| Appendix B.4 | Yes | Yes | Fully represented | Figure 4 audited |
| Appendix C | Yes | Yes | Fully represented | Algorithms 1–3 audited |
| Figure 1 | Yes, visually | Yes | Fully represented | Diagram and case-study caveat |
| Figure 2 | Yes, visually | Yes | Fully represented | Components and feedback loop |
| Figure 3 | Yes, visually | Yes | Fully represented | Axes, series, trends, estimates |
| Figure 4 | Yes, visually | Yes | Fully represented | Axes, trend, estimates |
| Table 1 | Yes, visually/textually | Yes | Fully represented | All conditions considered |
| Table 2 | Yes, visually/textually | Yes | Fully represented | All defenses |
| Table 3 | Yes, visually/textually | Yes | Fully represented | All defenses |
| Table 4 | Yes, visually/textually | Yes | Fully represented | Prose–table contradiction highlighted |
| Table 5 | Yes, visually/textually | Yes | Fully represented | All scenario rows |
| Algorithm 1 | Yes, visually/textually | Yes | Fully represented | Typographical issue noted |
| Algorithm 2 | Yes, visually/textually | Yes | Fully represented | Ancestor update explained |
| Algorithm 3 | Yes, visually/textually | Yes | Fully represented | Formula and \(n=1,2\) constraint |
| Formal research questions | Yes | Yes | Missing from paper | Objectives reported without manufacturing formal RQs |
| Formal hypotheses | Yes | Yes | Missing from paper | No statistical hypotheses stated |
| Author limitations section | Yes | Yes | Missing as a dedicated section | Dispersed acknowledgments collected |
| Supplementary material | No separate artifact | Yes | Missing from supplied material | None explicitly identified |
| Code/raw data/seed corpus | No | Yes | Missing from supplied material | Reproducibility impact noted |

## Missing or inaccessible material

- No separate code, execution logs, raw outcomes, exact adversarial prompt corpus, mutation templates, random seeds, hardware details, costs, or replication package was supplied.
- Page 10 was not visually rendered, although its full reference text was supplied. It contains no identified substantive visual object.
- Exact unlabeled coordinates in Figures 3–4 cannot be recovered confidently from the plots.
- No sample sizes per Table 5 scenario are given.
- Values for \(C\) and \(\epsilon\) are not supplied.
- No separate supplementary material was provided or clearly referenced.

## Uncertain interpretations

- Appendix B.1’s prose conflicts with Table 4 about the newest o3-mini and baseline ASRs.
- The `P`-like extraction in Algorithm 3 is visually a summation sign; this was interpreted as \(\sum\).
- Algorithm 1 contains `total_succcess`, apparently a typographical error for `total_success`.
- The distinction between the prose-reported 70% VWA terminal result and Table 1’s 60% selected-prompt fuzzing ASR is not fully explained.
- It is unclear whether the two appearances of \(C\) in Algorithms 1 and 3 denote one shared hyperparameter.
- Figure 3’s plotted values are estimates because individual points are not numerically labeled.

## Deliberately compressed material

- The bibliography was inspected but not summarized citation by citation.
- Routine introductory examples of agent categories and tools were consolidated into the background and glossary.
- Repeated statements of the headline success rates across the abstract, introduction, results, and conclusion were consolidated rather than reproduced each time.
- Minor wording and typographical defects not affecting scientific interpretation were not exhaustively catalogued.

## Potential omissions

Against the inventory above, no known substantive section, subsection, experiment, figure, table, algorithm, appendix, major contribution, or explicitly acknowledged limitation has been omitted. Content unavailable outside the supplied document—especially implementation artifacts and raw experimental records—could not be assessed.