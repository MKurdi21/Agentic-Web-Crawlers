# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Available range | Pages 1–23 |
| Apparently missing pages | None |
| Native text | Available for all 23 pages; no page is flagged as scanned or unusually text-poor |
| Pages visually rendered and inspected | 1–4 and 7–12 |
| Pages available only through extracted text | 5–6 and 13–23 |
| Figures visually inspected | Figures 1–6 |
| Tables visually inspected | Tables 1–2 |
| Equations | Equations (1), (3)–(6) were visible on rendered pages; Equation (2) was available only as extracted text |
| Tables readable | Yes for Tables 1–2 |
| Appendices | Appendix A, §§A.1–A.5, pp. 14–19 |
| Supplementary material | None supplied and none explicitly detected |
| External artifacts mentioned but not supplied | GitHub repository; Qwen-Agent repository; web-search infrastructure; benchmark datasets; training code/data beyond what appears in the paper |
| OCR required | No. Native extraction was available, although mathematical notation remains extraction-sensitive |
| Principal limitations | Not every page was rendered; consequently, prose and the case study on pp. 13–23 were read from extracted text rather than visually checked. Equation (3) is densely typeset, and the extracted text overloads \(o_i\) for both rollout outputs and observations/model tokens; its exact typography should be checked against the PDF before implementation. |

Evidence classifications used below:

- **[A] Author-reported:** explicitly stated in the paper.
- **[B] Directly observable:** read from a supplied page rendering.
- **[C] Analyst-derived:** calculated directly from reported values, with operands shown.
- **[D] Analyst interpretation:** a clearly marked inference rather than an author claim.
- No external information is introduced.

# 1. Plain-Language Orientation

WebSailor is a post-training method for turning an open-source large language model into a web-search agent capable of solving questions whose answers are difficult to locate and whose search paths are not obvious.

The central problem is not merely retrieving a webpage. Hard benchmarks such as BrowseComp require an agent to begin with vague clues, explore multiple possible identities or relationships, discard unproductive paths, combine partial evidence, and eventually settle on an answer. The authors describe this as reducing **high, hard-to-reduce uncertainty** (§§1–3.1, pp. 2–5). [A]

The researchers construct a pipeline with three main elements:

1. **SailorFog-QA:** synthetic questions generated from non-linear entity graphs, followed by deliberate clue obfuscation (§3.1, pp. 3–5). [A]
2. **Rejection sampling fine-tuning (RFT) cold start:** a little over 2,000 successful, difficult, compactly reconstructed reasoning trajectories teach the model the basic pattern of long-horizon web search (§1, pp. 2–3; §4.1, p. 6). [A]
3. **Duplicating Sampling Policy Optimization (DUPO):** a reinforcement-learning method that removes uninformative rollout groups and duplicates informative cases already in the batch, reportedly making agent training approximately 2–3 times faster than the dynamic-sampling comparison (§4.2, p. 7). [A]

The principal reported result is that WebSailor becomes the strongest open-source agent in Table 1 on all four evaluated benchmarks. WebSailor-72B obtains 12.0 on BrowseComp-en, 30.1 on BrowseComp-zh, 55.0 on Xbench-DeepSearch, and 55.4 on the selected GAIA subset (Table 1, p. 9). [A][B]

The paper’s central contribution is therefore an integrated training recipe: create tasks that resemble the uncertainty structure of genuinely difficult web research, bootstrap the agent with successful long trajectories, and then improve those behaviors with more efficient reinforcement learning.

Important qualification: the paper’s phrases “super-human reasoning” and “surpass human levels” are broad author claims (title, abstract, §7). The supplied experiments chiefly compare models and agents on benchmarks; they do not present a controlled human-subject evaluation establishing a general human-performance boundary.

# 2. Document Roadmap

The accessible document contains 23 pages:

| Identifier | Original location | Content and role |
|---|---|---|
| S1 | Abstract, p. 1 | Problem, proposed pipeline, and headline claim |
| S2 | §1 Introduction, pp. 2–3 | Motivation, gap, and contributions |
| S3 | §2 Problem Definition, p. 3 | ReAct agent model, tools, trajectories, and the difficult-search setting |
| S4 | §3, pp. 3–6 | Large-scale training-data synthesis |
| SS4.1 | §3.1, pp. 3–5 | Three task levels and SailorFog-QA construction |
| SS4.2 | §3.2, pp. 5–6 | Reconstruction of concise reasoning from expert trajectories |
| S5 | §4, pp. 6–7 | Two-stage RFT-plus-RL training |
| SS5.1 | §4.1, p. 6 | Rejection sampling, filtering, formatting, and loss masking |
| SS5.2 | §4.2, pp. 6–7 | DUPO algorithm, policy objective, advantage, and reward |
| S6 | §5, pp. 7–12 | Experimental setup, main results, analyses, and limitations |
| SS6.1 | §5.1, pp. 7–8 | Models, benchmarks, baselines, evaluation settings |
| SS6.2 | §5.2, pp. 8–10 | Main benchmark results |
| SS6.3 | §5.3, pp. 10–12 | Dataset complexity, SimpleQA, RL gains, and cold-start ablation |
| SS6.4 | §5.4, p. 12 | Limitations and future work |
| S7 | §6, pp. 12–13 | Related benchmarks, web agents, SFT, and RL |
| S8 | §7, p. 13 | Conclusion |
| A1 | Appendix A, pp. 14–19 | Tools, QA generation, trajectory format, training settings, and case study |
| R | References, pp. 20–23 | Bibliography |

Inventory of substantive objects:

- **Figures:** F1–F6.
- **Tables:** T1–T2.
- **Major equations:** E1–E6, corresponding to Equations (1)–(6).
- **Algorithms/pseudocode:** no formally numbered algorithm; Appendix A.2 supplies a five-step graph-construction procedure.
- **Case study:** one ten-step BrowseComp-en trajectory in Appendix A.5.
- **Explicit formal research questions:** none.
- **Explicit formal hypotheses:** none, although §5.2 calls the uncertainty-driven-training proposition the paper’s “core hypothesis.”
- **Keywords:** no keyword list is present.
- **Venue:** no conference or journal venue is supplied; the paper is identified as arXiv:2507.02592v1 [cs.CL], dated 3 July 2025, with 4 July 2025 also printed on the first page.
- **Authors:** Kuan Li, Zhongwang Zhang, Huifeng Yin, Liwen Zhang, Litu Ou, Jialong Wu, Wenbiao Yin, Baixuan Li, Zhengwei Tao, Xinyu Wang, Weizhou Shen, Junkai Zhang, Dingchu Zhang, Xixi Wu, Yong Jiang, Ming Yan, Pengjun Xie, Fei Huang, and Jingren Zhou; Tongyi Lab, Alibaba Group (p. 1). [A]
- **Document type:** machine-learning/AI algorithm-and-systems paper with an experimental evaluation and synthetic-data contribution.

# 3. Background and Context

## Web agents and ReAct

A **large language model (LLM) agent** is a language model embedded in a loop that can choose actions and receive information from an environment. WebSailor uses **ReAct**, short for reasoning and acting (§2, p. 3). [A]

Its loop is:

1. Generate a **Thought** about what to do.
2. Emit an **Action**, such as a search or webpage visit.
3. Receive an **Observation** from the tool.
4. Repeat until emitting a final answer.

WebSailor’s action space includes:

- **Search:** submit one or several queries and receive the top ten results for each, including title, snippet, and URL (§2, p. 3; Appendix A.1, p. 14). [A]
- **Visit:** retrieve webpages and summarize each one relative to an explicitly supplied goal. Jina retrieves the page content and Qwen-2.5-72B serves as the summarization model (Appendix A.1, p. 14). [A]
- **Final answer:** terminate the trajectory with a response (§2, p. 3). [A]

## Uncertainty reduction

The paper treats information seeking as reducing uncertainty about an answer. Its taxonomy distinguishes:

- **Level 1:** low uncertainty, easily resolved using internal knowledge or one straightforward search.
- **Level 2:** possibly high initial uncertainty, but a clear sequence of steps exists.
- **Level 3:** high uncertainty plus no predetermined, easily followed reduction path (§3.1, pp. 3–4; Fig. 2). [A][B]

The authors associate difficult web research with Level 3: clues interact in complex ways, multiple search paths may look plausible, and the agent must adapt its plan.

## Compositional generalization

**Compositional generalization** means handling a new combination of familiar entities or relations. The authors argue that graph-sampled questions produce unseen combinations and therefore discourage shallow lookup heuristics (§1, p. 2). [A]

## Training stages

- **Fine-tuning:** training a pretrained model on desired examples.
- **Rejection sampling fine-tuning (RFT):** generate candidate trajectories, retain only those meeting correctness and complexity criteria, then fine-tune on the retained examples.
- **Reinforcement learning (RL):** optimize a policy using rewards obtained from its generated behavior.
- **Cold start:** initial fine-tuning intended to give RL a viable behavior pattern before sparse rewards are encountered.
- **Rollout:** one complete sampled attempt at answering a question, including tool interactions.
- **Pass@1:** average correctness of one sampled response per question.
- **Pass@3:** success behavior when three generations are sampled; the paper plots it but does not restate a general estimator for pass@3 beyond saying generation is repeated \(k\) times (§5.1, p. 8).

## Prior work as positioned by the authors

Section 6 distinguishes:

1. Earlier fact-retrieval and multi-hop benchmarks with clearer paths.
2. Newer, harder information-seeking benchmarks, particularly BrowseComp-en/zh.
3. Proprietary browsing systems whose methods are opaque.
4. Open-source ReAct-style agents that lag on non-linear search.
5. Supervised fine-tuning approaches that may generalize poorly in adaptive environments.
6. RL methods that may learn exploration but face stability and sample-efficiency problems (§6, pp. 12–13). [A]

This is the authors’ characterization of the cited literature; the external papers were not independently examined.

# 4. Research Problem and Gap

## Existing problem

Difficult web questions may have no obvious starting point or fixed chain of queries. Searching all possibilities is infeasible, while lengthy trajectories consume context and make stable success difficult (§2, p. 3). [A]

## Shortcomings attributed to previous approaches

According to the authors:

- Existing open-source agents are trained mainly on Level 1 or Level 2 problems and consequently do not learn sufficiently adaptive search behavior (§1, p. 2). [A]
- Direct inference cannot recover obscure, current, or highly specific facts that are absent from model parameters (§5.2, pp. 8–9). [A]
- Direct imitation of expert large reasoning model outputs brings verbose stylistic habits and context overload (§3.2, pp. 5–6). [A]
- Pure or direct RL begins with extremely sparse rewards and is too slow for multi-turn tool-using rollouts (§§1, 4.2, pp. 2–3, 7). [A]
- DAPO-style dynamic resampling may introduce sequential rollout work inside a batch, worsening agent-training latency (§4.2, p. 7). [A]

## Research gap

The authors identify no open-source post-training pipeline that jointly supplies:

- appropriately difficult, high-uncertainty tasks;
- usable long-horizon reasoning supervision;
- a viable cold start;
- and efficient reinforcement learning for interactive web agents.

## Motivation

Proprietary systems reportedly perform much better on BrowseComp, but their training methods are unavailable. The work aims to narrow that capability gap with an open-source-model-based method (§§1, 6, pp. 2–3, 13). [A]

## Scope

The demonstrated scope is web-based information seeking with search and visit tools. The evaluation covers BrowseComp-en, BrowseComp-zh, Xbench-DeepSearch, a 103-case text-only GAIA subset, and a random 200-case SimpleQA subset (§5, pp. 7–11). [A]

It does not establish equivalent performance for arbitrary autonomous web interaction, transactional tasks, multimodal GAIA as a whole, or general reasoning outside information seeking.

# 5. Research Questions / Objectives / Hypotheses

## Explicit research questions

No formally enumerated research questions appear in the supplied paper.

## Informal objectives

The paper nevertheless investigates the following author-stated objectives:

- Develop open-source agents that can reduce difficult uncertainty in complex web search (§1).
- Generate scalable Level 3 training questions (§3.1).
- turn successful but verbose expert trajectories into concise supervision (§3.2).
- Determine whether an RFT cold start is necessary before RL (§§1, 4, 5.3).
- Improve the efficiency of multi-turn agent RL through DUPO (§4.2).
- Test whether difficult-task training transfers downward to simpler tasks (§§1, 5.3).

## Hypotheses

No preregistered or formally numbered hypotheses are supplied.

The authors explicitly refer to a **core hypothesis**: training on synthesized data embodying complex, hard-to-reduce uncertainty gives an agent robust and generalizable reasoning strategies (§5.2, p. 9). [A]

Two further propositions are evaluated experimentally, though not labeled formal hypotheses:

- an RFT cold start is indispensable or essential for hard web-agent RL (§§1, 5.3);
- RL improves stability and single-sample efficiency, especially on BrowseComp (§5.3, pp. 11–12).

# 6. Assumptions / Threat Model

This is not a cybersecurity paper and supplies no attacker threat model. Its operational assumptions are:

- The agent can access a search engine and webpage-retrieval service (§2; Appendix A.1).
- Search returns ten titles, snippets, and URLs per query.
- Visit returns a goal-conditioned summary rather than necessarily exposing raw pages directly to the policy.
- The environment and summary model provide useful observations.
- Final-answer correctness can be judged by another LLM (§§4.2, 5.1).
- Tool-call count is a useful proxy for task difficulty (§5.3, p. 10).
- Correct expert trajectories carry useful search strategy even after their original thoughts are discarded (§3.2).
- The answer supplied during synthetic construction satisfies the generated constraints, even where the constraints may admit multiple answers (§5.3, pp. 10–11).
- Rollouts in one DUPO group concern the same question-answer pair and can be normalized relative to one another (§4.2).
- Evaluation with non-zero-temperature samples and LLM judging adequately reflects agent performance (§5.1).

**[D] Analyst interpretation:** The approach also depends on search-result availability, web-page accessibility, retrieval quality, and summarizer fidelity. Those dependencies follow from the architecture, although the authors do not separately formalize them as assumptions.

# 7. Methodology

## 7.1 Overall study design

The work is a model-training and benchmark-evaluation study:

1. Construct synthetic high-uncertainty questions.
2. Have expert reasoning models generate successful web trajectories.
3. discard their verbose original thoughts.
4. reconstruct concise thoughts conditioned on the successful actions and observations.
5. filter the reconstructed trajectories.
6. run RFT as a cold start.
7. run DUPO reinforcement learning.
8. evaluate four model sizes against direct, proprietary-agent, and open-source-agent baselines.

## 7.2 SailorFog-QA construction

Appendix A.2 gives the operational procedure (p. 14): [A]

1. Select rare entities using Wikidata’s SPARQL service and unspecified database rules.
2. Retrieve features of the initial entity using Search and Visit.
3. extract related entities and their features.
4. probabilistically choose either a new related entity or a previously seen node as the next expansion point.
5. repeat until the graph reaches a predefined number of edges.

Nodes represent entities; edges represent relationships. The probabilistic revisiting of earlier nodes is intended to produce branching and overlapping structures rather than simple chains (§3.1, p. 4).

A subgraph is then sampled, and a question-answer pair is formulated from it (§3.1, p. 5). Clues are obfuscated, for example:

- exact date → vague period;
- complete name → an initial or partial identity clue;
- exact number → qualitative range.

The authors report three advantages: real-web grounding, diverse reasoning patterns, and non-linear scalability in the number of possible subgraphs (§3.1, p. 5). Exact graph sizes, sampling probabilities, question-generation model, number of generated QAs, and database-selection rules are not supplied.

## 7.3 Expert trajectory production and reasoning reconstruction

An expert open-source large reasoning model—QwQ-32B is given as an example—attempts the synthetic questions (§3.2, p. 5). [A]

For a successful trajectory:

- retain actions \(a_t\) and observations \(o_t\);
- remove the expert’s native thoughts;
- use a separate instruction-following model \(\pi^*\) to reconstruct a concise thought \(\hat{\tau}_t\) for each step, conditioning on the preceding reconstructed history, the action actually chosen, and the subsequent observation;
- enforce a “short-CoT” style (§3.2, p. 6).

This is outcome-conditioned reconstruction: the new thought has access to the observation that followed the action. **[D] Analyst interpretation:** That produces clean explanatory supervision but may make the reconstructed rationale more hindsight-informed than a thought generated online before seeing the observation.

## 7.4 RFT cold start

Trajectory formatting (§4.1, p. 6; Appendix A.3, p. 14):

- thoughts: `<think> ... </think>`;
- tool actions: `<tool_call> ... </tool_call>`;
- tool observations: `<tool_response> ... </tool_response>`;
- final answer: `<answer> ... </answer>`.

Three filters are applied (§4.1):

1. retain only trajectories ending in a correct answer;
2. discard trajectories exceeding 32,000 tokens;
3. retain only trajectories with more than five tool calls.

Observation tokens are masked from the training loss so that training targets the agent’s own thoughts and actions rather than environment-generated content. The introduction says the cold start uses “just over 2k” high-quality examples (pp. 2–3). No exact retained count is provided.

## 7.5 DUPO reinforcement learning

DUPO uses two sampling interventions (§4.2, p. 7):

- **Before training:** remove overly easy cases for which all eight rollouts are correct.
- **During training:** remove groups with zero reward variance—every rollout correct or every rollout incorrect—and fill empty batch slots by randomly duplicating other non-zero-variance groups already in the batch.

The rationale is that group-relative advantages are uninformative when all rewards are identical. Reusing eligible cases from the same batch avoids waiting for sequential replacement rollouts. The authors report an approximate 2–3× speedup over DAPO dynamic sampling.

DUPO additionally uses:

- group-relative advantage estimation following GPRO/GRPO as written in the paper;
- token-level policy-gradient loss;
- asymmetric lower and upper clipping parameters \(\epsilon_{\text{low}}\) and \(\epsilon_{\text{high}}\);
- masking of observation tokens;
- a reward combining format and answer correctness (§4.2).

## 7.6 Models, tools, and implementation

Models trained (§5.1, pp. 7–8):

- Qwen-2.5-3B
- Qwen-2.5-7B
- Qwen-2.5-32B
- Qwen-2.5-72B

Implementation (Appendix A, pp. 14–15):

- ReAct orchestration: Qwen-Agent.
- webpage retrieval: Jina.
- visit summarization: Qwen-2.5-72B.
- supervised/RFT training: Megatron.
- RL training: verl.
- maximum tool calls per trajectory: 30.

Hardware, accelerator counts, wall-clock training time, compute budget, software versions, and random seeds are not reported.

## 7.7 Training hyperparameters

| Stage | Hyperparameter | Value | Source |
|---|---|---:|---|
| RFT/SFT | Batch size | 32 | Appendix A.4, p. 15 |
| RFT/SFT | Learning rate | \(5\times10^{-6}\) | Appendix A.4 |
| RFT/SFT | Minimum learning rate | \(1\times10^{-10}\) | Appendix A.4 |
| RFT/SFT | Schedule | Warmup + cosine decay | Appendix A.4 |
| RFT/SFT | Weight decay | 0.1 | Appendix A.4 |
| RL | Rollouts per group | 8 | Appendix A.4 |
| RL | Temperature | 1.0 | Appendix A.4 |
| RL | Top-p | 1.0 | Appendix A.4 |
| RL | Batch size | 128 | Appendix A.4 |
| RL | Mini-batch size | 32 | Appendix A.4 |
| RL | Learning rate | \(1\times10^{-6}\) | Appendix A.4 |
| Evaluation | Temperature | 0.6 | §5.1, p. 8 |
| Evaluation | Top-p | 0.95 | §5.1 |
| ReAct | Tool-call cap | 30 | Appendix A.3, p. 14 |
| Filtering | Maximum trajectory length | under 32k tokens | §4.1, p. 6 |
| Filtering | Minimum retained tool calls | more than 5 | §4.1 |
| RL | Maximum reported training steps | 50 | §5.4, p. 12 |

The paper does not report the warmup length, cosine-decay duration, optimizer, clipping values, gradient accumulation, model context-window configuration, or per-model training duration.

## 7.8 Evaluation data

- **BrowseComp-en:** complex English-language browsing questions.
- **BrowseComp-zh:** analogous Chinese-language questions.
- **GAIA:** only 103 cases from its text-only validation subset.
- **Xbench-DeepSearch:** dynamic, professionally aligned deep-retrieval tasks.
- **SimpleQA:** random sample of 200 from 4,326 question-answer pairs (§5.3, p. 11).

The full benchmark sample sizes for BrowseComp-en/zh and Xbench are not restated in this paper. No repeated random subsets or confidence intervals are reported.

## 7.9 Baselines

Direct inference:

- Qwen-2.5-32B and 72B
- GPT-4o
- GPT-4.1
- QwQ-32B
- o4-mini
- DeepSeek-R1

Proprietary browsing agents:

- Grok-3
- Doubao
- GPT-4o with browsing
- DeepResearch

Open-source agents:

- R1-Searcher-7B
- Search-o1 variants
- WebDancer-32B
- WebDancer-QwQ
- WebThinker-RL

Some proprietary numbers were manually evaluated through websites or taken from benchmark papers, and missing entries reflect cost constraints (Table 1 caption, p. 9).

## 7.10 Metrics and statistical methods

Pass@1 is the average of binary correctness indicators \(p_i\) (§5.1, Eq. 6). Correctness is judged by an LLM. The paper reports no:

- confidence intervals;
- standard errors;
- hypothesis tests;
- inter-rater reliability;
- judge calibration results specific to this experiment;
- multiple-run variation;
- significance thresholds.

# 8. Experiments / Analyses

## X1 — Main four-benchmark comparison

**Purpose:** Compare WebSailor with direct inference, proprietary browsing agents, and open-source agents.

**Setup:** Four WebSailor sizes; four benchmarks; pass@1 with evaluation temperature 0.6 and top-p 0.95; LLM judge (§5.1; Table 1).

**Results:** WebSailor-72B is the best open-source row in every benchmark column: 12.0, 30.1, 55.0, and 55.4 (Table 1).

**Caveats:** Proprietary coverage is incomplete; GAIA uses only 103 text-only cases; no uncertainty intervals are supplied.

## X2 — Dataset-complexity distribution

**Purpose:** Test whether SailorFog-QA resembles difficult browsing problems more than the WebDancer training set.

**Setup:** Tool-call counts from unfiltered but correct rejection-sampling trajectories; comparison with BrowseComp-en and WebDancer-QA (Fig. 3, p. 10).

**Results:** WebDancer-QA is concentrated at two calls, reportedly above 50%, with almost nothing beyond ten. SailorFog-QA has a long tail above five and beyond twenty and visually resembles BrowseComp-en more closely.

**Caveat:** Tool calls are only a proxy for difficulty; the displayed SailorFog distribution precedes the final “more than five calls” filter.

## X3 — Dataset pass-rate comparison

**Purpose:** Quantify SailorFog-QA’s difficulty.

**Setup:** o4-mini and DeepSeek-R1 with browsing and ReAct; pass@1 on SailorFog-QA, WebDancer-QA, and BrowseComp-en (Table 2, p. 10).

**Results:**

- o4-mini: 47.3 vs 90.2 vs 26.3.
- DeepSeek-R1: 38.9 vs 84.4 vs 9.5.

SailorFog-QA is therefore much harder than WebDancer-QA but easier than BrowseComp-en for both tested backbones.

**Caveat:** SailorFog-QA may admit more than one satisfying answer, although the intended answer is said always to satisfy the question’s constraints.

## X4 — SimpleQA downward compatibility

**Purpose:** Determine whether training only on difficult tasks harms simple factual question answering.

**Setup:** Random sample of 200 of 4,326 SimpleQA pairs; comparison of agent-based and direct-answer methods (Fig. 4, p. 11).

**Result:** WebSailor-72B scores 93.5% and WebSailor-32B 92.8%, the two highest displayed values.

**Caveat:** Only one 200-question subset is reported; the sampling seed and sampling variability are absent.

## X5 — RFT-versus-RL comparison across pass@1 and pass@3

**Purpose:** Measure improvement after the RL stage.

**Setup:** WebSailor-32B and 72B, pass@1 and pass@3, four benchmarks (Fig. 5, p. 11).

**Results:** All 16 displayed changes are positive, ranging from +2.0 to +8.3 percentage points. The largest labeled gain is +8.3 for BrowseComp-zh, 72B pass@1. The authors interpret the relatively larger pass@1 changes as improved single-sample efficiency.

**Caveat:** The plot labels increments but not every underlying bar value; exact pre/post values are not printed for all conditions.

## X6 — Cold-start ablation

**Purpose:** Compare direct RL on Qwen-2.5-Instruct-32B with RL after RFT cold start.

**Setup:** Pass@1 over training steps on BrowseComp-en and GAIA, plus mean/aggregate tool-call behavior (Fig. 6, p. 12).

**Results:** The cold-start curve converges higher on both benchmarks and maintains roughly six tool calls. The direct-RL model improves from a low starting point but remains lower and reaches only about three tool calls by step 32.

**Caveat:** Most plotted values are unlabeled and therefore only visually estimable. The paper does not show variance across runs.

## X7 — Appendix case study

**Purpose:** Demonstrate a long, adaptive BrowseComp-en search trajectory.

**Setup:** A question asks for the first computer jointly purchased by an unidentified software developer and his father. The clues include a solar-powered fridge, a “hole in the map,” Edinburgh conference memories, and caving (Appendix A.5, pp. 15–19).

**Process:** Ten steps combine broad searches, phrase-focused searches, webpage visits, identity verification, and a direct visit to a personal blog.

**Result:** The trajectory identifies Joey Hess and answers “Atari 130XE” (p. 19).

**Caveat:** Several tool responses are abbreviated with ellipses in the paper, the caving clue is not visibly resolved in the supplied case text, and the final trajectory is illustrative rather than a systematic evaluation.

# 9. Results

## 9.1 Main benchmark results

Table 1’s WebSailor scores are:

| Model | BrowseComp-en | BrowseComp-zh | Xbench-DeepSearch | GAIA subset |
|---|---:|---:|---:|---:|
| WebSailor-3B | 3.3 | 9.7 | 27.7 | 33.0 |
| WebSailor-7B | 6.7 | 14.2 | 34.3 | 37.9 |
| WebSailor-32B | 10.5 | 25.5 | 53.3 | 53.2 |
| WebSailor-72B | 12.0 | 30.1 | 55.0 | 55.4 |

All are author-reported pass@1-style accuracy values; the table does not print a percent sign, though adjacent text calls them accuracy scores.

### Against the strongest displayed open-source non-WebSailor rows

- BrowseComp-en: 12.0 vs 3.8 for WebDancer-QwQ.  
  **[C] Absolute difference:** \(12.0-3.8=8.2\) points.
- BrowseComp-zh: 30.1 vs 18.0 for WebDancer-QwQ.  
  **[C] Difference:** 12.1 points.
- Xbench-DeepSearch: 55.0 vs 39.0 for WebDancer-QwQ.  
  **[C] Difference:** 16.0 points.
- GAIA: 55.4 vs 51.5 for WebDancer-QwQ.  
  **[C] Difference:** 3.9 points.

These comparisons support the “best open-source agent in Table 1” claim.

### Small-model evidence

WebSailor-7B’s BrowseComp-en score of 6.7 exceeds WebDancer-32B’s 2.5 and WebThinker-RL’s 2.8 (§5.2, p. 9). [A]

- **[C] Against WebDancer-32B:** \(6.7-2.5=4.2\) points.
- **[C] Against WebThinker-RL:** \(6.7-2.8=3.9\) points.

This shows that the result is not explained by parameter count alone, although it does not by itself isolate which training component causes the gain.

## 9.2 Proprietary comparisons

- BrowseComp-zh: WebSailor-72B 30.1 vs Doubao 26.0.  
  **[C] Difference:** 4.1 points.
- BrowseComp-en: WebSailor-72B 12.0 vs DeepResearch 51.5.  
  **[C] DeepResearch lead:** 39.5 points.
- BrowseComp-zh: WebSailor-72B 30.1 vs DeepResearch 42.9.  
  **[C] DeepResearch lead:** 12.8 points.
- Xbench: WebSailor-72B 55.0 vs proprietary Grok-3 and Doubao entries marked “50+.” Exact differences cannot be calculated.
- GAIA: WebSailor-72B 55.4 vs DeepResearch 67.4, a **[C] 12.0-point** gap.

Thus, the authors’ “parity” language applies narrowly to selected proprietary comparisons, especially Doubao on BrowseComp-zh, not to DeepResearch overall.

## 9.3 Direct inference

Direct inference remains weak on BrowseComp-en: the best direct score is o4-mini at 6.1. DeepSeek-R1 is notable on BrowseComp-zh at 26.3 and Xbench at 32.7 (Table 1). [A][B]

The table also prevents an overly broad claim that browsing always wins: some weaker browsing agents underperform strong direct reasoning models on particular columns. For example, WebSailor-3B’s 9.7 on BrowseComp-zh is below DeepSeek-R1 direct at 26.3. The paper’s stronger claim is about the trained WebSailor family’s upper end and the general inadequacy of most direct systems on the hardest retrieval tasks.

## 9.4 SimpleQA

Figure 4 values, visually labeled:

| Method | Pass@1 (%) |
|---|---:|
| WebSailor-72B | 93.5 |
| WebSailor-32B | 92.8 |
| WebDancer-QwQ | 90.5 |
| WebDancer-32B | 87.5 |
| WebThinker-RL | 77.5 |
| DeepSeek-R1-ReAct | 72.2 |
| R1-Searcher-7B | 52.0 |
| GPT-4.1 | 41.6 |
| GPT-4o | 38.2 |
| DeepSeek-R1 | 27.8 |
| o4-mini | 20.0 |
| Qwen-2.5-72B | 15.8 |
| QwQ-32B | 12.7 |
| Qwen-2.5-32B | 9.0 |

WebSailor-72B leads WebDancer-QwQ by **[C] \(93.5-90.5=3.0\) percentage points**.

## 9.5 Reinforcement-learning gains

Figure 5 reports the following RFT-to-RL improvements:

| Benchmark | 32B P@1 | 32B P@3 | 72B P@1 | 72B P@3 |
|---|---:|---:|---:|---:|
| BrowseComp-en | +3.3 | +2.2 | +3.7 | +3.4 |
| BrowseComp-zh | +6.3 | +6.5 | +8.3 | +4.9 |
| GAIA | +6.6 | +4.7 | +3.0 | +3.6 |
| XBench | +7.6 | +8.0 | +3.7 | +2.0 |

All are visually readable percentage-point annotations. The prose says pass@1 improves proportionally more than pass@3; this is not uniformly true in the raw absolute increments—XBench 32B has +8.0 for pass@3 versus +7.6 for pass@1, and BrowseComp-zh 32B has +6.5 versus +6.3. The claim may concern proportional improvement relative to starting values, which cannot be verified exactly from the printed increment labels alone.

# 10. Figure-by-Figure Interpretation

## Figure 1 — BrowseComp-en/zh headline comparison

- **Location:** p. 1.
- **Type:** Two vertical bar charts.
- **Panels:** BrowseComp-en and BrowseComp-zh.
- **Axes:** x-axis lists systems; y-axis is benchmark performance, though the visible plot does not explicitly print a unit label.
- **Encoding:** purple bars highlight WebSailor; other methods appear in light purple/gray.
- **Exact visible values, BrowseComp-en:** WebSailor-72B 12.0; WebSailor-32B 10.5; DeepSeek-R1-Browse 9.5; WebDancer-QwQ 3.8; WebThinker-QwQ 2.8; DeepSeek-R1 2.0; GPT-4o browsing 1.9; Search-o1-32B 0.6.
- **Exact visible values, BrowseComp-zh:** WebSailor-72B 30.1; WebSailor-32B 25.5; Doubao-Search 26.0; WebDancer-QwQ 18.0; WebThinker-QwQ 14.7; Search-o1-32B 7.2; another displayed web-agent bar at 12.9 corresponds to the proprietary comparison named in the caption/table context.
- **Conclusion supported:** WebSailor leads displayed open-source agents.
- **Caveat:** Figure 1’s subset and some labels differ from Table 1’s fuller nomenclature. Table 1 is the clearer source for the complete benchmark comparison.

## Figure 2 — Three levels of information-seeking tasks

- **Location:** p. 4.
- **Type:** conceptual diagram, not a measured plot.
- **Components:** three dashed boxes labeled Task Level 1, 2, and 3.
- **Encoding:** circles represent entities; lines represent relationships; purple nodes/edges highlight selected information.
- **Flow:** Level 3 explicitly shows “Sample” from a dense graph followed by “Fuzz,” producing several ambiguous, partially connected clue clusters.
- **Meaning:** Level 1 is a direct lookup; Level 2 is a fixed chain; Level 3 is a dense, variable topology whose clues are obfuscated.
- **Examples:** Level 1 includes the Richard Dawkins Award question; Level 2 includes an Alibaba CEO/Chinese Academy of Sciences chain and a 2004 Olympic athlete chain.
- **Conclusion supported:** the authors’ data-generation design targets structure and ambiguity simultaneously.
- **Caveat:** The figure is an explanatory taxonomy, not empirical evidence that all benchmark questions fall cleanly into one level.

## Figure 3 — Tool-call distributions

- **Location:** p. 10.
- **Type:** overlaid histograms/bar distributions.
- **Panels:**  
  (a) SailorFog-QA vs BrowseComp-en;  
  (b) SailorFog-QA vs WebDancer-QA.
- **x-axis:** number of tool calls, 0–30.
- **y-axis:** sample proportion; panel (a) extends to roughly 0.10, panel (b) to 0.6.
- **Legend:** purple = SailorFog-QA; green = comparison dataset.
- **Main visible pattern:** SailorFog-QA is concentrated above five calls and has a long tail past twenty. BrowseComp-en also shows a broad, long-tailed pattern. WebDancer-QA has a dominant spike around two calls and little mass after ten.
- **Reported textual value:** more than 50% of WebDancer trajectories require only two calls.
- **Exactness:** Distribution-shape statements are visually readable; individual bar heights, apart from the textual “over 50%,” are not labeled and should not be treated as exact.
- **Caveat:** The plots use unfiltered correct trajectories, whereas RFT later retains only trajectories with more than five calls.

## Figure 4 — SimpleQA performance

- **Location:** p. 11.
- **Type:** horizontal bar chart.
- **x-axis:** pass@1 percentage, 0–100.
- **y-axis:** fourteen models/methods.
- **Encoding:** purple and green emphasize agentic methods; gray represents direct models.
- **Exact values:** all fourteen are printed above the bars and reproduced in §9.4.
- **Observation:** Every displayed agentic method except none—indeed all seven agentic entries shown—exceeds every direct method shown; the weakest agentic score, R1-Searcher-7B at 52.0, exceeds the strongest direct score, GPT-4.1 at 41.6.
- **[C] Difference:** \(52.0-41.6=10.4\) percentage points.
- **Conclusion supported:** difficult-task training does not eliminate simple factual-search ability in this sample.
- **Caveat:** This concerns a random 200-item subset, not all 4,326 SimpleQA questions.

## Figure 5 — RFT versus RL

- **Location:** p. 11.
- **Type:** grouped bars.
- **Groups:** BrowseComp-en, BrowseComp-zh, GAIA, and XBench.
- **Within each group:** 32B pass@1, 32B pass@3, 72B pass@1, 72B pass@3.
- **Encoding:** light purple = after RFT; dark purple = after RL.
- **y-axis:** accuracy (%).
- **Annotations:** positive changes from +2.0 to +8.3, listed in §9.5.
- **Main observation:** every RL bar is higher than its RFT counterpart.
- **Conclusion supported:** RL improves the measured configurations.
- **Caveat:** No error bars are shown, and exact base/final bar values are difficult to read; the printed increments are the most reliable data.

## Figure 6 — Direct RL versus RFT-cold-start RL

- **Location:** p. 12.
- **Type:** three line plots.
- **Legend:** purple = cold start; green = instruct/direct RL.
- **Panel (a):** BrowseComp-en pass@1 (%) versus training step. Cold start begins around 8–9%, rises to roughly 10.5%, and remains near 10%; direct RL rises from roughly 2% to approximately 4%.
- **Panel (b):** GAIA pass@1 (%) versus step. Cold start stays roughly in the 49–54% range and ends near 53–54%; direct RL rises approximately from 34% to 42%.
- **Panel (c):** number of tool calls versus step. Cold start stays near six; direct RL begins near zero and reaches around three.
- **Exactness:** Those curve readings are **approximate visual estimates**, not printed exact values.
- **Conclusion supported:** RFT supplies a stronger initial search policy and preserves longer tool-use behavior during RL.
- **Caveats:** direct RL shows larger improvement from its lower initial value, but converges lower; no replicate variability is shown.

# 11. Table-by-Table Interpretation

## Table 1 — Four-benchmark comparison

- **Location:** p. 9.
- **Rows:** model/backbone and interaction paradigm.
- **Columns:** BrowseComp-en, BrowseComp-zh, Xbench-DeepSearch, and GAIA.
- **Groups:** Direct Inference, Proprietary Agents, Open-source Agents.
- **Missing-value notation:** “–” means unavailable because of cost constraints.
- **Special notation:** ‡ means proprietary methods were manually evaluated through websites, with some results reported by benchmark papers.
- **Best displayed values overall:** DeepResearch 51.5 on BrowseComp-en, 42.9 on BrowseComp-zh, and 67.4 on GAIA; Xbench has only “50+” for Grok-3 and Doubao, while WebSailor-72B has an exact 55.0.
- **Best exact open-source row:** WebSailor-72B on every column.
- **Scale trend:** WebSailor scores increase monotonically from 3B to 72B in every column.
- **No statistical information:** no intervals, deviations, or significance tests.
- **Caveat:** methods are not uniformly evaluated through identical access routes, and proprietary rows are incomplete.

## Table 2 — Difficulty of training datasets

- **Location:** p. 10.
- **Rows:** o4-mini and DeepSeek-R1.
- **Columns:** SailorFog-QA, WebDancer-QA, BrowseComp-en.
- **Metric:** pass@1 under ReAct with browsing.
- **Values:**  
  o4-mini: 47.3, 90.2, 26.3.  
  DeepSeek-R1: 38.9, 84.4, 9.5.
- **Best/worst:** WebDancer-QA is easiest for both models; BrowseComp-en is hardest; SailorFog-QA lies between them.
- **Derived differences:**  
  o4-mini: SailorFog is 42.9 points below WebDancer and 21.0 above BrowseComp.  
  DeepSeek-R1: SailorFog is 45.5 below WebDancer and 29.4 above BrowseComp.
- **Caveat:** lower pass rate combines intrinsic difficulty with possible answer non-uniqueness; it is not a pure structural-complexity measure.

# 12. Diagram / Architecture Interpretation

The paper contains no full software-architecture block diagram. Figure 2 is its substantive conceptual workflow diagram.

The complete method can nevertheless be reconstructed from the prose:

```text
Rare Wikidata entity
        ↓
Iterative web retrieval and graph expansion
        ↓
Dense entity–relation graph
        ↓
Subgraph sampling
        ↓
Question/answer formulation
        ↓
Clue obfuscation
        ↓
SailorFog-QA
        ↓
Expert LRM attempts with Search and Visit
        ↓
Retain successful action–observation traces
        ↓
Discard verbose native thoughts
        ↓
Reconstruct concise step rationales
        ↓
Correctness + <32k-token + >5-tool-call filters
        ↓
RFT cold start
        ↓
DUPO reinforcement learning
        ↓
WebSailor-3B/7B/32B/72B
```

During inference, the control loop is:

```text
Question → Thought → Search/Visit → Observation
                ↑                       ↓
                └──── updated context ──┘
                         ↓
                    Final answer
```

The Visit tool itself contains an additional pipeline:

```text
URL + visit goal → Jina page retrieval
                 → Qwen-2.5-72B goal-conditioned summary
                 → observation returned to WebSailor
```

This means the agent does not operate alone: retrieval and summarization are components of the evaluated system.

# 13. Equations and Mathematical Concepts

## Equation (1) — Complete ReAct trajectory

**Location:** §2, p. 3.

\[
H_T=(\tau_0,a_0,o_0,\ldots,\tau_i,a_i,o_i,\ldots,\tau_T,a_T).
\]

- \(H_T\): the history through \(T\) interaction rounds.
- \(\tau_i\): thought at round \(i\).
- \(a_i\): action at round \(i\).
- \(o_i\): observation returned after the action.
- The final tuple ends with \(a_T\), normally the final-answer action.

Plain meaning: a web-agent solution is a sequence of internal decisions, external actions, and returned evidence.

The paper then says the next thought/action is sampled from a policy conditioned on prior history. The extracted expression \(\pi(a,t\mid H_{t-1})\) is typographically unusual because \(t\) may be an extraction of \(\tau\); the exact notation is uncertain.

## Equation (2) — Reconstructed thought

**Location:** §3.2, p. 6.

\[
\hat{\tau}_t \sim \pi^*(\tau\mid H_{t-1},a_t,o_t).
\]

- \(\hat{\tau}_t\): newly reconstructed concise thought.
- \(\pi^*\): separate instruction-following reconstruction model.
- \(H_{t-1}\): reconstructed history before step \(t\).
- \(a_t\): successful expert action.
- \(o_t\): resulting observation.

Plain meaning: generate a compact rationale explaining why the already known successful action made sense, using both earlier context and what the action returned.

## Equation (3) — DUPO clipped policy objective

**Location:** §4.2, p. 7.

In identifiable form, the objective averages a token-level clipped policy-gradient term across a group of \(G\) sampled outputs:

\[
J(\theta)=
\mathbb{E}\left[
\frac{1}{\sum_{i=1}^{G}|o_i|}
\sum_{i=1}^{G}\sum_{t=1}^{|o_i|}
\min\left(
r_{i,t}(\theta)\hat A_{i,t},
\operatorname{clip}
(r_{i,t}(\theta),1-\epsilon_{\rm low},1+\epsilon_{\rm high})
\hat A_{i,t}
\right)
\right],
\]

subject to:

\[
0 < \left|\{o_i:\operatorname{is\_equivalent}(y,o_i)\}\right| < G.
\]

Important components:

- \(\theta\): current policy parameters.
- \(D\): training distribution of question-answer pairs \((q,y)\).
- \(G\): rollout group size; Appendix A.4 gives \(G=8\).
- \(o_i\): here, according to the note below Eq. (4), tokens generated by the model, not the entire tool-interaction trajectory.
- \(r_{i,t}\): current-to-old-policy probability ratio.
- \(\hat A_{i,t}\): estimated relative advantage.
- \(\epsilon_{\rm low},\epsilon_{\rm high}\): asymmetric clipping bounds; numerical values are not supplied.
- `is_equivalent`: correctness/equivalence check between target answer \(y\) and rollout output.

The constraint retains only mixed-outcome groups: at least one rollout is correct and at least one is incorrect. Such groups have non-zero variation and therefore yield a group-relative learning signal.

Plain meaning: increase probability for relatively better actions, decrease it for worse ones, but cap each update so the policy does not change too abruptly.

**Notation caution:** \(o_i\) earlier means an environment observation, while here the authors say it denotes model-generated tokens. This overloaded notation can confuse implementation.

## Equation (4) — Importance ratio and group-relative advantage

**Location:** §4.2, p. 7.

\[
r_{i,t}(\theta)=
\frac{\pi_\theta(o_{i,t}\mid \text{context})}
{\pi_{\theta_{\rm old}}(o_{i,t}\mid \text{context})},
\qquad
\hat A_{i,t}=
\frac{R_i-\operatorname{mean}(\{R_i\}_{i=1}^{G})}
{\operatorname{std}(\{R_i\}_{i=1}^{G})}.
\]

- The ratio measures how much more or less likely the current policy makes token \(o_{i,t}\) relative to the rollout-generating policy.
- The advantage standardizes a rollout’s reward relative to the other rollouts for the same group.
- If standard deviation is zero, advantage normalization is undefined/uninformative; DUPO removes the case and duplicates another variable case.

The advantage is written with a token index \(t\), but the displayed formula is based on rollout-level \(R_i\), so every trained token in a rollout appears to inherit the same normalized rollout reward.

## Equation (5) — Reward

**Location:** §4.2, p. 7.

\[
R_i=0.1R_i^{\text{format}}+0.9R_i^{\text{answer}}.
\]

- Format score checks tags and ReAct ordering.
- Answer score is assigned by an LLM judge.
- Answer correctness receives nine times the weight of format adherence.

The ranges of the two component rewards are not explicitly defined in the supplied text.

## Equation (6) — Pass@1

**Location:** §5.1, p. 8.

\[
\operatorname{pass@1}=\frac{1}{n}\sum_{i=1}^{n}p_i.
\]

- \(n\): number of evaluated questions/responses.
- \(p_i\): correctness of response \(i\), apparently a binary judged value.

Plain meaning: count correct responses and divide by the number evaluated.

# 14. Interpretation and Discussion

The experiments support four narrower conclusions.

First, direct inference is generally inadequate for BrowseComp-style questions. Scores on BrowseComp-en are mostly near zero, even for large or proprietary direct models (Table 1). Search tools alone, however, are not sufficient: several earlier browsing agents also score poorly. The contribution concerns learned search strategy, not merely tool availability.

Second, training-data structure matters. SailorFog-QA produces longer solution trajectories than WebDancer-QA and resembles BrowseComp-en’s tool-call distribution more closely (Fig. 3). The corresponding pass rates place it between WebDancer-QA and BrowseComp-en in difficulty (Table 2).

Third, the full WebSailor pipeline transfers across model scale. Every WebSailor size outperforms the preceding smaller WebSailor size on every Table 1 benchmark. The strong result for 7B against some 32B agents suggests training matters independently of raw size, although it is not a controlled scale-matched component ablation.

Fourth, both post-training stages appear useful. Figure 5 shows positive improvements after RL, while Figure 6 shows that direct RL starts from much weaker tool-use behavior and converges lower than cold-started RL.

## Relationship to the informal questions

- **Can high-uncertainty synthetic data produce capable agents?** The benchmark and dataset-analysis results are consistent with yes.
- **Can verbose expert trajectories be converted into usable supervision?** The method is specified and the final system performs well, but no direct ablation compares reconstructed thoughts against raw thoughts or action-only supervision.
- **Is the cold start useful?** Figure 6 supports this for the displayed Qwen-2.5-Instruct-32B runs.
- **Does DUPO improve speed?** The authors report approximately 2–3× versus DAPO, but supply no dedicated timing table or plotted measurements.
- **Does hard-task training retain easy-task skill?** The 200-item SimpleQA test supports downward compatibility.

## Consistency findings

- Table 1 supports “state of the art among displayed open-source agents.”
- “Parity with proprietary systems” is only partly supported: WebSailor beats Doubao’s displayed BrowseComp-zh score but remains far behind DeepResearch on BrowseComp-en and below it on the other available comparisons.
- Figure 5’s prose generalization that pass@1 gains are proportionally much larger than pass@3 cannot be verified from increments alone and is not uniformly true as an absolute-gain statement.
- The introduction describes some generated questions requiring up to 40 tool calls, whereas Appendix A.3 limits WebSailor trajectories to at most 30 tool calls. These can coexist if the 40-call observation refers to external proprietary-model attempts rather than the final training/inference configuration, but the distinction should be made explicit.
- The paper says GAIA includes mathematical and computational tasks that lower WebSailor’s margin, yet evaluates only 103 text-only validation cases. “Text-only” does not necessarily exclude mathematical/computational work, so this is not a direct contradiction.
- The case-study prose claims all identifying clues were confirmed, but the supplied abbreviated trajectory does not show clear confirmation of caving.

# 15. Contributions and Novelty

## Conceptual contribution

A three-level taxonomy organizes information-seeking tasks by initial uncertainty and how difficult that uncertainty is to reduce (Fig. 2; §3.1).

## Dataset contribution

**SailorFog-QA** synthesizes difficult web questions by building non-linear entity graphs, sampling subgraphs, and obfuscating clues (§3.1; Appendix A.2).

## Methodological contribution

Successful expert action-observation traces are retained while verbose thoughts are replaced with concise, outcome-informed rationales (§3.2).

## Training contribution

A two-stage RFT-plus-RL pipeline gives the policy both an initial long-horizon behavior pattern and subsequent exploration-based improvement (§4).

## Algorithmic contribution

**DUPO** removes zero-variance rollout groups and duplicates informative in-batch groups, reportedly accelerating agent RL by 2–3× (§4.2).

## System contribution

The work integrates ReAct, Google Search, Jina retrieval, goal-conditioned Qwen summarization, Qwen-Agent, Megatron, and verl into a web-agent pipeline (Appendix A).

## Empirical contribution

Four WebSailor sizes are evaluated on four difficult benchmarks, with additional SimpleQA transfer testing and analyses of task complexity, RL effects, and cold-start necessity (§5).

No new general-purpose benchmark is released as part of the evaluation; SailorFog-QA is a training-data construction rather than the main held-out benchmark.

# 16. Limitations

## Authors' stated limitations

From §5.4, p. 12:

1. Filtering out trajectories above 32k tokens may cap the complexity WebSailor can learn.
2. Failed cases often exceed the context limit.
3. Performance may degrade as inference length increases.
4. The agent may “over-think” and use multiple tool calls for apparently simple questions, although some of this behavior is deliberate cross-verification.
5. RL training is limited to 50 steps.
6. The synchronous RL framework remains inefficient even after DUPO.
7. Training speed remains a bottleneck.

Additional caveats explicitly noted elsewhere:

- Some proprietary agents could not be tested on every benchmark because of API access and cost (§5.1; Table 1).
- SailorFog-QA may not always have a unique answer, though its intended answer satisfies the constraints (§5.3, pp. 10–11).
- GAIA performance is less dominant because the model was not specifically optimized for mathematical and computational tasks (§5.2, p. 9).

## Additional evidence-based analyst observations

These are not stated author admissions:

1. **Incomplete reproducibility details:** graph sizes, expansion probabilities, question-generation prompts/models, exact dataset counts, optimizer choices, compute, seeds, and DUPO clip values are absent.
2. **No statistical uncertainty:** all benchmark conclusions rely on point estimates without confidence intervals or run-to-run variation.
3. **LLM-judge dependence:** both training reward and evaluation accuracy depend on LLM judgment, but this paper reports no task-specific judge reliability study.
4. **Potential summarizer bottleneck:** Visit observations are generated by Qwen-2.5-72B; retrieval or summarization errors could affect the policy independently of its reasoning.
5. **Difficulty proxy:** tool-call count can reflect inefficiency or over-thinking as well as genuine task complexity.
6. **Synthetic-answer ambiguity:** satisfying constraints is weaker than proving uniqueness, potentially complicating rejection sampling and evaluation.
7. **Outcome-informed rationales:** reconstructed thoughts condition on the subsequent observation, potentially making supervision differ from online causal reasoning.
8. **Limited component isolation:** there is no complete factorial ablation separately testing graph construction, obfuscation, thought reconstruction, RFT filtering, and each DUPO sampling component.
9. **SimpleQA subset sensitivity:** conclusions use one unseeded 200-item subset.
10. **Broad “superhuman” wording:** the evidence is benchmark performance, not a broad controlled comparison against humans.

# 17. Threats to Validity

## Internal validity

The cold-start study supports RFT’s usefulness, but the paper does not report repeated runs or whether all non-cold-start conditions were otherwise identical. The full performance gain cannot be causally assigned among data synthesis, obfuscation, rationale reconstruction, RFT, and DUPO because not all components receive isolated ablations.

## Construct validity

“Hard-to-reduce uncertainty” is a conceptual construct. Its main empirical proxy is number of tool calls, which may also measure poor search efficiency. Pass@1 based on an LLM judge measures judged answer correctness, not directly search quality, evidence quality, calibration, or faithfulness.

## Statistical conclusion validity

No uncertainty intervals, statistical tests, or multi-seed distributions are reported. This is especially relevant for the 103-case GAIA subset and 200-case SimpleQA sample, where a few outcomes can change scores noticeably.

## External validity

The tool environment is limited to Search and Visit, with a particular retrieval/summarization setup. Results may not generalize to other search engines, unavailable pages, adversarial websites, transactional browsers, richer tools, multimodal tasks, or future web states.

## Ecological validity

BrowseComp and related benchmarks intentionally stress difficult information retrieval. They are useful tests of deep search but do not cover all practical web-agent needs, such as user interaction, safe action execution, privacy, or long-running tasks.

## Reproducibility

The repository is referenced, but only the supplied paper was inspected. The paper provides many hyperparameters yet omits hardware, seeds, exact generated-data volume, prompts, graph-generation probabilities, and several optimization details required for faithful reproduction.

## Generalizability

The positive SimpleQA result is evidence of downward compatibility for one factual benchmark subset. It does not demonstrate universal transfer from Level 3 training to every simpler domain.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- Migrate from synchronous to asynchronous RL to improve training efficiency and permit more extensive RL (§5.4, p. 12).
- Develop still more complex, higher-uncertainty tasks (§7, p. 13).
- Improve the effectiveness and efficiency of RL (§7).
- Extend open-source agent capabilities beyond information seeking toward broader forms of “superhuman” performance (§7).

## B. Additional open questions

- Which component contributes most: graph topology, clue obfuscation, rationale reconstruction, RFT, or DUPO?
- Are reconstructed thoughts necessary, or would action-only training work similarly?
- How often do SailorFog questions have multiple valid answers?
- How reliable is the LLM judge across languages and obscure factual questions?
- Does DUPO’s duplication alter effective data diversity or produce overfitting?
- Does the reported 2–3× speedup persist at every model size?
- How sensitive are results to the Visit summarizer and search engine?
- Can long-context models remove the 32k filter without destabilizing training?
- Is “over-thinking” beneficial cross-verification, wasted computation, or both under different conditions?
- How does WebSailor compare with humans under controlled time and tool budgets?
- Can the approach provide auditable citations and evidence provenance, rather than only final-answer correctness?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| LLM | Large language model |
| LRM | Large reasoning model; an LLM optimized or trained for extended reasoning |
| Agent | A model that repeatedly chooses actions and observes their results |
| ReAct | A loop alternating reasoning (“Thought”), action, and observation |
| QA | Question-answer pair |
| Level 1 | Low-uncertainty, easily resolved information task |
| Level 2 | A task with a clear multi-step path |
| Level 3 | A high-uncertainty task with no clear predefined path |
| SailorFog-QA | The paper’s graph-synthesized, clue-obfuscated training questions |
| Obfuscation | Replacing precise clues with vaguer descriptions |
| Random walk | Iterative graph expansion in which the next node is selected probabilistically |
| Subgraph | A selected subset of nodes and relationships from a larger graph |
| Compositional generalization | Solving new combinations of familiar concepts or relations |
| CoT | Chain of thought; intermediate reasoning text |
| Short-CoT | Concise intermediate reasoning enforced during reconstruction |
| RFT | Rejection sampling fine-tuning |
| SFT | Supervised fine-tuning |
| RL | Reinforcement learning |
| Cold start | Initial training that supplies useful behavior before RL |
| Rollout | One sampled complete agent attempt |
| DUPO | Duplicating Sampling Policy Optimization |
| DAPO | The comparison RL approach using dynamic sampling |
| Policy | Probability model governing the agent’s generated decisions |
| Importance ratio | Current-policy probability divided by old-policy probability |
| Advantage | Reward relative to other rollouts in the same group |
| Clip | Limit how far a policy update can move in one step |
| Reward hacking | Obtaining reward without performing the intended behavior |
| Pass@1 | Average correctness using one sampled answer per question |
| Pass@3 | Evaluation involving three generated attempts |
| Top-p | Sampling restricted to a set of likely tokens whose cumulative probability reaches \(p\) |
| Temperature | Parameter controlling randomness in token sampling |
| \(H_T\) | Complete interaction history through step \(T\) |
| \(\tau_t\) | Thought at step \(t\) |
| \(a_t\) | Action at step \(t\) |
| \(o_t\) | Observation in Eq. (1); overloaded as model-generated output/tokens in Eqs. (3)–(4) |
| \(\pi_\theta\) | Policy parameterized by \(\theta\) |
| \(\pi^*\) | Model used to reconstruct concise thoughts |
| \(G\) | Number of rollouts in a group; reported as 8 |
| \(R_i\) | Reward for rollout \(i\) |
| \(\hat A_{i,t}\) | Estimated normalized advantage |
| \(\epsilon_{\rm low},\epsilon_{\rm high}\) | Lower and upper clipping widths; values not reported |
| SPARQL | Query mechanism used to obtain rare entities from Wikidata; the paper does not further define it |
| 3B/7B/32B/72B | Approximate model parameter scales in billions |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| WebSailor-72B BrowseComp-en | 12.0 | score/accuracy points | ReAct | Author-reported; visually readable | p. 9, Table 1 |
| WebSailor-72B BrowseComp-zh | 30.1 | score/accuracy points | ReAct | Author-reported; visually readable | p. 9, Table 1 |
| WebSailor-72B Xbench | 55.0 | score/accuracy points | ReAct | Author-reported; visually readable | p. 9, Table 1 |
| WebSailor-72B GAIA | 55.4 | score/accuracy points | 103-case text-only subset | Author-reported; visually readable | pp. 8–9, Table 1 |
| WebSailor-32B results | 10.5 / 25.5 / 53.3 / 53.2 | score points | Benchmark order above | Author-reported | Table 1 |
| WebSailor-7B results | 6.7 / 14.2 / 34.3 / 37.9 | score points | Benchmark order above | Author-reported | Table 1 |
| WebSailor-3B results | 3.3 / 9.7 / 27.7 / 33.0 | score points | Benchmark order above | Author-reported | Table 1 |
| DeepResearch BrowseComp-en | 51.5 | score points | Proprietary browsing | Author-reported | Table 1 |
| DeepResearch BrowseComp-zh | 42.9 | score points | Proprietary browsing | Author-reported | Table 1 |
| DeepResearch GAIA | 67.4 | score points | Proprietary browsing | Author-reported | Table 1 |
| Open-source lead, BrowseComp-en | 8.2 | points | \(12.0-3.8\) | Analyst-derived | Table 1 |
| Open-source lead, BrowseComp-zh | 12.1 | points | \(30.1-18.0\) | Analyst-derived | Table 1 |
| Open-source lead, Xbench | 16.0 | points | \(55.0-39.0\) | Analyst-derived | Table 1 |
| Open-source lead, GAIA | 3.9 | points | \(55.4-51.5\) | Analyst-derived | Table 1 |
| SailorFog pass@1, o4-mini | 47.3 | accuracy points | Before filtering | Author-reported | p. 10, Table 2 |
| WebDancer-QA pass@1, o4-mini | 90.2 | accuracy points | ReAct | Author-reported | Table 2 |
| BrowseComp-en pass@1, o4-mini | 26.3 | accuracy points | ReAct | Author-reported | Table 2 |
| SailorFog pass@1, DeepSeek-R1 | 38.9 | accuracy points | Before filtering | Author-reported | Table 2 |
| WebDancer-QA pass@1, DeepSeek-R1 | 84.4 | accuracy points | ReAct | Author-reported | Table 2 |
| BrowseComp-en pass@1, DeepSeek-R1 | 9.5 | accuracy points | ReAct | Author-reported | Table 2 |
| WebSailor-72B SimpleQA | 93.5 | % pass@1 | Random 200-item subset | Visually readable | p. 11, Fig. 4 |
| WebSailor-32B SimpleQA | 92.8 | % pass@1 | Same subset | Visually readable | Fig. 4 |
| Full SimpleQA size | 4,326 | QA pairs | Dataset total | Author-reported | §5.3, p. 11 |
| Evaluated SimpleQA sample | 200 | QA pairs | Random sample | Author-reported | §5.3 |
| Evaluated GAIA sample | 103 | cases | Text-only validation subset | Author-reported | §5.1, p. 8 |
| Largest labeled RL gain | +8.3 | percentage points | BrowseComp-zh, 72B pass@1 | Visually readable | p. 11, Fig. 5 |
| Smallest labeled RL gain | +2.0 | percentage points | XBench, 72B pass@3 | Visually readable | Fig. 5 |
| DUPO speedup | approximately 2–3× | ratio | Compared with DAPO dynamic sampling | Author-reported | §4.2, p. 7 |
| Rollouts per RL group | 8 | rollouts | DUPO training | Author-reported | Appendix A.4, p. 15 |
| Tool-call cap | 30 | calls | Qwen-Agent trajectory | Author-reported | Appendix A.3, p. 14 |
| RFT retained-call criterion | >5 | calls | Complexity filter | Author-reported | §4.1, p. 6 |
| RFT maximum length | <32,000 | tokens | Length filter | Author-reported | §4.1 |
| Cold-start dataset | just over 2,000 | examples | High-quality RFT data | Author-reported, inexact | §1, pp. 2–3 |
| Reward weights | 0.1 / 0.9 | fractions | format / answer | Author-reported | Eq. (5), p. 7 |
| Evaluation temperature/top-p | 0.6 / 0.95 | dimensionless | Pass@1 evaluation | Author-reported | §5.1, p. 8 |
| RL temperature/top-p | 1.0 / 1.0 | dimensionless | Rollouts | Author-reported | Appendix A.4 |
| Cold-start final BrowseComp-en | roughly 10–11 | % pass@1 | Fig. 6a | Approximate visual estimate | p. 12, Fig. 6 |
| Direct-RL final tool calls | roughly 3 | calls | step 32 | Approximate visual estimate | Fig. 6c |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| WebSailor is the strongest displayed open-source agent | Highest open-source score in all four Table 1 columns | X1, Table 1 | p. 9 | Strong within supplied comparison; no uncertainty intervals |
| High-uncertainty training data resembles difficult benchmarks | SailorFog tool-call distribution is broad and long-tailed like BrowseComp-en | X2, Fig. 3 | p. 10 | Moderate; tool calls are a proxy |
| SailorFog is harder than WebDancer-QA | 47.3 vs 90.2 and 38.9 vs 84.4 | X3, Table 2 | p. 10 | Strong for two tested backbones |
| SailorFog is easier than BrowseComp-en | 47.3 vs 26.3 and 38.9 vs 9.5 | X3, Table 2 | p. 10 | Strong for measured pass rates; ambiguity may contribute |
| Training, not scale alone, matters | WebSailor-7B beats selected 32B agents on BrowseComp-en | X1, Table 1 | p. 9 | Suggestive, not a scale-controlled ablation |
| WebSailor approaches some proprietary systems | 30.1 vs Doubao 26.0 on BrowseComp-zh | Table 1 | pp. 9–10 | Supported narrowly; not parity with DeepResearch overall |
| RL improves WebSailor | All 16 Fig. 5 increments are positive | X5, Fig. 5 | p. 11 | Strong descriptively; no run variance |
| RL improves single-sample efficiency | Pass@1 gains are described as proportionally larger | X5, Fig. 5 | pp. 11–12 | Partially verifiable; absolute increments do not uniformly show this |
| RFT cold start is important | Higher final scores and sustained tool calls than direct RL | X6, Fig. 6 | p. 12 | Moderate; one displayed model/configuration, no error bars |
| DUPO accelerates agent RL | Reported 2–3× speedup over DAPO sampling | Method claim | §4.2, p. 7 | Weakly documented in supplied results; no timing table |
| Hard-task training retains simpler-task skill | 93.5 and 92.8 on sampled SimpleQA | X4, Fig. 4 | p. 11 | Strong for the sampled 200 questions only |
| WebSailor surpasses human levels | Conclusion statement and claimed difficulty of Level 3 tasks | Narrative claim | §§3.1, 7 | Weakly established; no controlled human benchmark comparison is presented |
| Reconstructed reasoning avoids verbose imitation | Design removes original thoughts and inserts short-CoT thoughts | Method | §3.2, pp. 5–6 | Mechanism is clear; benefit lacks a direct ablation |
| Synthetic answers satisfy question constraints | Authors’ manual-inspection statement | Dataset analysis | pp. 10–11 | Author assertion; uniqueness is explicitly not guaranteed |

# 22. Very Simple Explanation

Imagine being given a question made of several vague clues. There is no obvious phrase to search, and each clue could point to many people or things. A normal search bot may try one query, get lost, or follow a fixed chain that fails. WebSailor is trained to behave more like a persistent investigator: try several leads, connect facts, abandon bad paths, and verify the answer.

The researchers manufacture difficult practice questions by building webs of related entities and then making the clues deliberately vague. Strong reasoning models solve some of them with web tools. The researchers keep the successful sequence of searches and webpage visits, replace the models’ very long internal explanations with shorter ones, and use those examples to give WebSailor a head start.

They then use reinforcement learning so WebSailor can improve beyond imitation. Their DUPO method focuses training on questions where repeated attempts produce a mixture of successes and failures, because those cases provide a useful signal about what behavior is better.

On the reported tests, the largest WebSailor is the best open-source system in the main comparison and can match or beat some proprietary agents on selected benchmarks. It still trails DeepResearch substantially on several available comparisons. The promising lesson is that carefully designed practice problems and training procedures can matter as much as simply making the model larger. The unanswered question is how robust these gains are outside the reported benchmarks, especially because the paper provides no statistical uncertainty, limited component ablations, and incomplete reproduction details.

# Completeness Audit

## Coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, affiliation, date | Yes | Yes | Fully represented | p. 1 |
| Abstract | Yes | Yes | Fully represented | Integrated into §§1, 4, 15 |
| §1 Introduction | Yes | Yes | Fully represented | Problem, gap, and contributions covered |
| §2 Problem Definition | Yes | Yes | Fully represented | ReAct, tools, trajectory, search challenge |
| §3 overview | Yes | Yes | Fully represented | Data construction and trajectories |
| §3.1 SailorFog-QA | Yes | Yes | Fully represented | Taxonomy, graph construction, obfuscation, examples |
| §3.2 Reasoning reconstruction | Yes | Yes | Fully represented | Procedure and Eq. (2) covered |
| §4 overview | Yes | Yes | Fully represented | Two-stage training |
| §4.1 RFT | Yes | Yes | Fully represented | Formatting, three filters, masking |
| §4.2 DUPO | Yes | Yes | Fully represented | Sampling, objective, reward, reported speed |
| §5.1 Setup | Yes | Yes | Fully represented | Models, datasets, baselines, metrics, settings |
| §5.2 Main Results | Yes | Yes | Fully represented | Table 1 comparisons and qualifications |
| §5.3 Analysis | Yes | Yes | Fully represented | Figs. 3–6 and Table 2 |
| §5.4 Limitations/Future Work | Yes | Yes | Fully represented | Author limitations separated from analyst observations |
| §6 Related Work | Yes | Yes | Represented in compressed form | Categories and claimed gaps preserved; citations not individually summarized |
| §7 Conclusion | Yes | Yes | Fully represented | Claims and future direction covered |
| Appendix A.1 Tools | Yes, text only | Yes | Fully represented | Search, Visit, Jina, summarizer |
| Appendix A.2 QA Construction | Yes, text only | Yes | Fully represented | Five-step procedure |
| Appendix A.3 ReAct Trajectories | Yes, text only | Yes | Fully represented | Format and 30-call cap |
| Appendix A.4 Training Details | Yes, text only | Yes | Fully represented | All reported hyperparameters captured |
| Appendix A.5 Case Study | Yes, text only | Yes | Represented in compressed form | Ten-step trajectory summarized; repetitive search snippets compressed |
| References | Yes, text only | Partly | Deliberately compressed | Bibliographic list inventoried by role; individual entries not re-described |
| Figure 1 | Yes, visually | Yes | Fully represented | Two panels and labeled values audited |
| Figure 2 | Yes, visually | Yes | Fully represented | Conceptual diagram and flow audited |
| Figure 3a | Yes, visually | Yes | Fully represented | Axes, legend, distributions, caveat |
| Figure 3b | Yes, visually | Yes | Fully represented | Axes, spike, long-tail comparison |
| Figure 4 | Yes, visually | Yes | Fully represented | All fourteen labeled values recorded |
| Figure 5 | Yes, visually | Yes | Fully represented | All sixteen printed increments recorded |
| Figure 6a–c | Yes, visually | Yes | Fully represented | Curves described with approximate labels where necessary |
| Table 1 | Yes, visually and textually | Yes | Fully represented | Complete WebSailor rows and important comparison rows covered |
| Table 2 | Yes, visually and textually | Yes | Fully represented | All six values covered |
| Equation (1) | Yes, visually and textually | Yes | Fully represented | Symbols and trajectory meaning |
| Equation (2) | Text only | Yes | Fully represented with access caveat | Page 6 was not rendered |
| Equation (3) | Yes, visually and textually | Yes | Fully represented with notation caveat | Dense, extraction-sensitive objective |
| Equation (4) | Yes, visually and textually | Yes | Fully represented | Ratio and advantage |
| Equation (5) | Yes, visually and textually | Yes | Fully represented | Reward weights |
| Equation (6) | Yes, visually and textually | Yes | Fully represented | Pass@1 |
| Formal algorithms | Not present | Yes | Not applicable | Appendix A.2 procedure substituted for pseudocode |
| Formal theorems/lemmas | Not present | Yes | Not applicable | Empirical ML paper |
| Explicit research questions | Not present | Yes | Absence represented | Informal objectives listed without inventing RQs |
| Formal hypotheses | Not present | Yes | Absence represented | One author-described “core hypothesis” identified |
| Major experiments X1–X7 | Yes | Yes | Fully represented | Separate setup, results, and caveats supplied |
| Author-stated limitations | Yes | Yes | Fully represented | §16 |
| Supplementary material | Not supplied | Yes | Missing from supplied material | None detected as explicitly referenced |
| Keywords | Not present | Yes | Absence represented | No keyword list |
| Footnotes | Yes | Yes | Represented in compressed form | Contribution/correspondence and Qwen-Agent link accounted for |

## Missing or inaccessible material

- No pages are missing.
- Pages 5–6 and 13–23 were not visually rendered; they were inspected through the supplied native text.
- The GitHub repositories, code, datasets, prompts, model checkpoints, and web artifacts referenced by the paper were not supplied and were not accessed.
- No supplementary files were supplied.
- Exact hardware, training compute, random seeds, complete generated-data counts, graph-generation probabilities, clipping coefficients, and several optimizer details are absent from the paper itself.
- Several webpage responses in the Appendix A.5 case study are intentionally replaced with ellipses and therefore cannot be inspected in full.

## Uncertain interpretations

- Equation (3)’s exact typography is dense and extraction-sensitive.
- \(o_i\) is overloaded between environment observations and model-generated outputs/tokens.
- The policy notation after Eq. (1) may contain a text-extraction error involving \(t\) versus \(\tau\).
- Figure 6 values are mostly unlabeled; reported curve values above are approximate visual estimates.
- Figure 1 contains compressed/rotated system labels; Table 1 is more reliable for full method naming.
- Figure 5 supports exact increments but not exact underlying values for every bar.
- The case study’s claim that the caving clue was verified is not demonstrated by the abbreviated visible tool outputs.
- “Pass@3” is described operationally as repeated generation but not mathematically defined with the same precision as pass@1.
- The range of the format and answer reward components in Eq. (5) is unspecified.

## Deliberately compressed material

- The two full SailorFog example questions were characterized rather than repeated verbatim; their roles, obfuscation types, and supplied answers were inspected.
- Appendix A.5’s repetitive searches and long result snippets were compressed into the trajectory’s decisions, evidence path, and unresolved point.
- The four-page bibliography was treated as supporting scholarly apparatus. Its major related-work categories were represented, but every citation entry was not individually annotated because that would not add substantive information about the paper’s method or results.
- Table 1’s non-WebSailor values were selectively reproduced where needed for claims and comparisons; all rows were inspected, and the complete table remains available in the supplied page.

## Potential omissions

No known substantive section, subsection, experiment, figure, table, major equation, algorithmic procedure, contribution, author-stated limitation, or appendix item from the inventory is absent from this analysis. The principal compression concerns references, repetitive case-study text, and non-central baseline rows. Visual verification was necessarily limited to the ten rendered pages identified in Stage 0.