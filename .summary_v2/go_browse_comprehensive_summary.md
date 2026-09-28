# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Available range | Pages 1–20 |
| Apparently missing pages | None |
| Native/extracted text | Available for every page; no page was flagged as scanned or text-poor |
| Pages visually rendered and inspected | 1–9, 11–12, 15–17 |
| Pages not visually rendered | 10, 13–14, 18–20; assessed from supplied page-labeled text only |
| Figures available visually | Figures 1–8 are visible on rendered pages 2, 6–8, and 17 |
| Tables readable | Tables 1–10 and the first row of Table 11 are visually available; the continuation of Table 11 on pp. 18–19 was available only as extracted text |
| Algorithms readable | Algorithms 1–3 are visually readable on pp. 4–5 |
| Equations/notation readable | Mostly yes. The paper contains definitions and pseudocode rather than a developed equation sequence. Some mathematical notation is extraction-sensitive but recoverable from context |
| Appendices present | Yes: Appendix A (implementation and prompts), B (additional analyses), C (hyperparameters/resources), and D (LLM usage) |
| Supplementary material supplied | No separate supplementary file |
| Referenced external artifacts | Code, dataset, and models are said to be released at a GitHub repository, but that repository was not supplied or inspected |
| OCR required | No |
| Important limitations | Fourteen of twenty pages were rendered. Text-only pages cannot receive independent visual-layout validation. Table 11 spans pp. 17–19, but only its first row was visually rendered. References were inspected as text but compressed as bibliographic material |

Document type: a mixed machine-learning/AI algorithm, data-collection, dataset, and empirical benchmark paper. It introduces a structured exploration algorithm, creates a training dataset, fine-tunes a web agent, and evaluates the resulting model.

Evidence labels used below:

- **[A] Author-reported:** explicitly stated in the paper.
- **[B] Directly observable:** readable from a supplied visual.
- **[C] Analyst-derived:** calculated from supplied values.
- **[D] Analyst interpretation:** an inference not explicitly asserted by the authors.
- No external information is introduced.

# 1. Plain-Language Orientation

Go-Browse addresses a training-data problem for artificial-intelligence agents that operate websites. A normal language model may understand a user’s instruction but still fail because it does not know a site’s structure: which page contains the needed control, how to reach that page, or which sequence of clicks is required.

The paper’s central idea is to explore a website as a graph. Each distinct URL is a node, and successful trajectories connecting pages supply edges. Go-Browse retains a **frontier** of discovered but not yet fully explored pages. It can reset an agent directly to one of these pages, propose tasks grounded in what is actually present there, check whether those tasks are feasible, and collect additional demonstrations.

This design separates two difficulties:

1. navigating from a site’s root to the right page; and
2. carrying out a local task once that page has been reached.

That separation enables **prefixed sampling**, in which a solver starts on the relevant page. The system also retains **unprefixed sampling**, in which the solver starts from the site root and must perform the full navigation.

The authors run Go-Browse on five WebArena website domains and produce **Go-Browse-WA**, containing 26,749 trajectories, including 9,504 successes, 17,245 failures, 196,462 steps, and 3,422 unique tasks across 100 URLs (p. 6, Table 1). They fine-tune Qwen-2.5-7B-Instruct only on successful trajectories. The resulting **Go-Browse-7B** achieves a **21.7%** success rate on 812 WebArena tasks, versus 18.8% for NNetNav-7B, 19.3% for GPT-4o-mini, and 8.3% for the original Qwen model (pp. 6–7, Table 3).

The central contribution is therefore not merely another web-agent policy. It is a reusable, graph-structured process for automatically finding website regions, proposing grounded tasks, filtering infeasible tasks, and collecting training trajectories with broader coverage and less redundant exploration.

# 2. Document Roadmap

| Pages | Content and role |
|---|---|
| p. 1–2, Abstract and §1 | Establishes the environmental-knowledge problem, motivates direct website exploration, and previews Go-Browse and its results |
| pp. 2–3, §2 | Defines the web-agent state, actions, trajectories, reward, and prior interaction-first/instruction-first exploration policies |
| pp. 3–5, §3 | Presents the Go-Browse graph-search framework, modules, sampling modes, and Algorithm 3 |
| pp. 5–6, §4 | Describes Go-Browse-WA collection on five WebArena domains, model roles, budgets, and dataset composition |
| pp. 6–7, §5 | Gives fine-tuning, WebArena evaluation, Online-Mind2Web evaluation, and core benchmark results |
| pp. 7–9, §6 | Analyzes task diversity, URL depth, prefixed sampling, feasibility filtering, and outer-loop website coverage |
| p. 9, §7 | Positions the work relative to web agents, synthetic data generation, and reinforcement-learning exploration |
| pp. 9–10, §8 | Summarizes conclusions, limitations, future directions, reproducibility, and acknowledgements |
| pp. 10–12 | References |
| pp. 12–15, Appendix A | Specifies the action space and the prompts used for agents and the visual-language-model judge |
| pp. 15–19, Appendix B | Adds task-proposal comparisons, collection cost, bootstrap testing, and detailed out-of-domain analysis |
| p. 20, Appendix C | Supplies fine-tuning hyperparameters, hardware, runtime, and baseline licensing |
| p. 20, Appendix D | Discloses language-model use in data collection and manuscript preparation |

# 3. Background and Context

A **web agent** is a model-driven system that observes a webpage and issues actions such as clicking, typing, scrolling, or navigating to a URL.

The agents follow the **ReAct** pattern: at time \(t\), the language model receives state \(s_t\), reasons about the task, and generates action \(a_t\); executing the action produces \(s_{t+1}\) (pp. 2–3, §2.1).

The state includes:

- the task or goal \(g\);
- a flattened **accessibility tree**, a textual representation of webpage elements;
- an action-space description;
- previous actions; and
- the error, if any, from the latest action.

A **trajectory** is a complete sequence of states and actions attempted for a task. A binary reward model marks it successful or unsuccessful.

The paper distinguishes two earlier data-collection patterns (p. 3, §2.2; p. 4, Algorithms 1–2):

- **Interaction-first exploration:** an agent explores without a concrete task; another model labels the trajectory afterward. This can reach deep pages, but independent episodes may repeatedly revisit the same easy areas or produce uninteresting behavior.
- **Instruction-first exploration:** a task proposer first generates plausible tasks from the current observation, and an agent attempts them. This produces purposeful behavior but may remain confined to the initial page and may hallucinate tasks involving unseen functionality.

Go-Browse combines purposeful task proposal with persistent, graph-based coverage. Its “reset, then explore” idea is stated to be inspired by Go-Explore in reinforcement learning (pp. 2, 9).

# 4. Research Problem and Gap

## Existing problem

Pretrained large language models perform poorly on graphical-user-interface web tasks partly because they lack knowledge of unfamiliar website environments (p. 1, Abstract and §1). The paper cites author-reported WebArena success rates of 78% for humans, 38% for GPT-4o, 19% for GPT-4o-mini, and 8% for Qwen-2.5-7B-Instruct in the introductory framing.

## Shortcomings attributed to previous approaches

According to the authors:

- Human demonstrations are expensive and slow to collect at scale.
- Data synthesized from indirect sources such as tutorials may not transfer to the actual target websites.
- Interaction-first exploration wastes effort through independent, redundant episodes and may not produce useful task demonstrations.
- Instruction-first methods generate relevant tasks but are often restricted to a static initial page and may hallucinate infeasible tasks.
- Some instruction-first methods require human screenshots or demonstrations to provide broader site context.

## Research gap

The missing capability is a fully automatic policy that can both:

- explore a website globally and reuse discoveries between episodes; and
- propose useful, page-grounded tasks locally.

## Motivation

The authors argue that learning directly from the websites an agent will encounter is more effective than relying on generic indirect knowledge. They cite a 16% versus 6% success-rate contrast between environment-interaction and indirect-data approaches (p. 1, §1).

## Scope

The implemented evaluation covers five self-hosted WebArena domains—Shopping Admin, Shopping, Reddit, GitLab, and Map—and an out-of-domain test on 136 live Online-Mind2Web websites. The method is described as applicable to other sites, but that broader deployment is not tested in the supplied work.

# 5. Research Questions / Objectives / Hypotheses

The paper does not state formal numbered research questions or preregistered hypotheses.

Its explicit and implicit objectives are:

1. Design a fully unsupervised, scalable method for collecting diverse and realistic web-agent trajectories through direct website interaction.
2. Improve global website coverage by maintaining and revisiting a graph frontier.
3. Reduce wasted rollouts by filtering proposed tasks for feasibility.
4. determine whether resetting to relevant pages lets weaker solvers generate useful data.
5. Train a 7-billion-parameter web agent using the collected successful trajectories.
6. Test whether that model improves over the original Qwen model, NNetNav-7B, and GPT-4o-mini on WebArena.
7. Examine generalization to Online-Mind2Web.
8. Analyze task diversity, navigation depth, collection efficiency, and the effect of the outer loop.

The paper’s testable expectations are informal:

- structured resets should increase unique-URL coverage;
- prefixed sampling should help most on deep nodes and with weaker models;
- more diverse, deeper data should improve downstream WebArena success;
- feasibility filtering should reduce unnecessary rollouts.

# 6. Assumptions / Threat Model

This is not a security paper, so no attacker-centered threat model is defined.

The operative system assumptions are:

- The environment exposes a state through an accessibility tree and supports BrowserGym-style actions (pp. 3, 12).
- Distinct URLs are treated as graph nodes. This assumes URL identity is an adequate operational unit for webpage exploration (pp. 3–5).
- Agents can be reset to previously discovered pages.
- A navigation trajectory can serve as a graph edge.
- Proposed tasks are considered feasible if at least one attempted trajectory is judged successful (p. 4).
- The GPT-4o-based visual-language-model judge can reliably decide success from the goal, actions, final accessibility tree, response, and screenshot (pp. 6, 14–15).
- WebArena’s task-specific reward functions provide correctness labels for benchmark evaluation (p. 6).
- Prefixed trajectories are useful training examples even though they begin from a non-root page.
- The five self-hosted WebArena domains are stable enough to support multi-week automated data collection.
- The Online-Mind2Web IDA/OOD categorization relies on GPT-4o-mini’s classification of website similarity (p. 16).

Trusted components include the benchmark environments, BrowserGym execution layer, reset mechanism, task-specific evaluators, and judge model. The supplied paper does not provide a systematic error analysis of these components.

# 7. Methodology

## 7.1 Agent formulation

At each timestep the agent observes \(s_t\) and generates \(a_t\). The output contains reasoning plus one Python-style action. A trajectory terminates when it reaches maximum horizon \(T\) or issues a terminal action such as `send_msg_to_user` (p. 3, §2.1).

The action space includes no-op, click, hover, fill, keyboard input, scroll, option selection, direct URL navigation, browser history navigation, tab operations, user messaging, and reporting infeasibility (p. 12, Table 6).

## 7.2 Graph representation

Go-Browse builds \(G=(V,E)\):

- \(V\): unique URLs;
- \(E\): trajectories connecting URLs;
- \(F\): discovered URLs awaiting exploration;
- \(D\): collected task–trajectory data.

The root URL of each website is inserted into \(V\) and \(F\). The system repeatedly removes a frontier node, explores it, and adds newly discovered URLs and edges (pp. 4–5, Algorithm 3).

## 7.3 Inner-loop components

### NavExplorer

NavExplorer is itself a web agent. It interacts with the current page to discover neighboring pages and proposes navigation tasks leading to them. It receives an added `add_tasks_to_dataset` action. Its prompt prioritizes pages likely to support common and useful user tasks (pp. 4, 13).

### PageExplorer

PageExplorer proposes tasks that can be performed locally on the current page. Its prompt emphasizes information seeking, navigation, and content modification; specificity; common rather than niche tasks; and page interaction to uncover functionality (pp. 4, 13–14).

### FeasibilityChecker

For each proposed task:

1. Claude-3.7-Sonnet attempts the task, with no more than three tries.
2. A GPT-4o-based visual-language-model judge evaluates the trajectory.
3. A task is retained if at least one trajectory succeeds.
4. The successful trajectory is added to the dataset.
5. Newly discovered URLs are added to the graph and frontier.

The judge applies task-type-sensitive criteria: information-seeking tasks require a sufficient answer; navigation and modification tasks are judged from the action history and final page state (pp. 4, 6, 14–15).

### Solvers

GPT-4o-mini and Qwen-2.5-7B-Instruct sample more trajectories for feasible tasks:

- **Prefixed:** start from the page where the task was proposed.
- **Unprefixed:** start from the website root.

Two trajectories of each type are sampled per task (pp. 5–6). Prefixed sampling lowers the navigation burden; unprefixed sampling preserves full long-horizon behavior.

## 7.4 Data collection

Go-Browse-WA was collected from five WebArena domains, with 20 URLs per domain and 100 URLs total (pp. 5–6).

Collection settings:

| Component | Model/settings |
|---|---|
| NavExplorer | Claude-3.7-Sonnet; up to 15 interaction steps |
| PageExplorer | GPT-4o up to 20 steps; Claude-3.7-Sonnet up to 10 |
| FeasibilityChecker | Claude-3.7-Sonnet; up to 3 attempts |
| Judge | GPT-4o-based VLM-as-a-judge |
| Feasible-task cap | 30 per URL |
| Solvers | GPT-4o-mini and Qwen-2.5-7B-Instruct |
| Solver horizon | 10 steps |
| Sampling | 2 prefixed plus 2 unprefixed trajectories |
| Collection temperature | 0.7 |
| Collection duration | Approximately 3 weeks |
| Collection cost | $975.57 |

The released observations include accessibility trees, HTML, and screenshots, but fine-tuning uses only accessibility-tree observations (p. 6).

## 7.5 Fine-tuning

Qwen-2.5-7B-Instruct is supervised-fine-tuned only on successful Go-Browse-WA trajectories. A comparison model is trained with the same parameters on NNetNav-WA, described as 45,000 interaction steps across the same five domains (p. 6).

Appendix C settings (p. 20):

- 2 epochs;
- maximum sequence length: 24,000 tokens;
- learning rate: \(2\times10^{-5}\);
- batch size: 8, one example per GPU;
- 4 gradient-accumulation steps;
- one node with eight NVIDIA H100 GPUs, 80 GB VRAM each;
- approximately 40 hours per fine-tuning run.

The paper does not report a validation split, random seed, optimizer, scheduler, regularization settings, or checkpoint-selection procedure.

## 7.6 Evaluation

### WebArena

- 812 benchmark tasks;
- BrowserGym execution;
- task-specific WebArena reward functions;
- inference temperature 0;
- success rate as the metric.

### Online-Mind2Web

- 300 tasks;
- 136 live websites;
- used as an out-of-domain/generalization benchmark;
- websites additionally classified as In-Domain-Adjacent (IDA) or Out-of-Distribution/Out-of-Domain (OOD) by GPT-4o-mini.

### Statistical analysis

Paired bootstrap testing uses 10,000 bootstrap samples (p. 16, Appendix B.3). No confidence intervals are reported.

# 8. Experiments / Analyses

## X1 — WebArena model comparison

**Purpose:** Test whether Go-Browse-WA improves a 7B agent.

**Setup:** Fine-tuned Qwen models are evaluated on 812 WebArena tasks against original Qwen, NNetNav-7B, GPT-4o-mini, GPT-4o, and Claude-3.7-Sonnet.

**Result:** Go-Browse-7B achieves 21.7% overall, the best open-weight 7B result in Table 3 and above GPT-4o-mini, but below GPT-4o and Claude-3.7-Sonnet.

**Caveat:** The table mixes closed models and open-weight 7B models with different pretraining and likely different capabilities. The paper reports success rate only, without uncertainty intervals.

## X2 — Online-Mind2Web generalization

**Purpose:** Test transfer to 136 live websites outside WebArena.

**Result:** Overall success rates are 5.33% for Go-Browse-7B, 4.00% for NNetNav-7B, and 9.33% for GPT-4o-mini (p. 6, Table 2).

**Caveat:** All models perform substantially worse than on WebArena. Live-site variability is not experimentally controlled in the supplied text.

## X3 — Dataset task-diversity analysis

**Purpose:** Compare task redundancy and domain balance in Go-Browse-WA versus NNetNav-WA.

**Method:** GPT-4o-mini clusters tasks into higher-level intent categories.

**Result:** Figure 4 visually shows more, generally smaller wedges for Go-Browse-WA and a more balanced domain distribution. NNetNav-WA has a disproportionately large GitLab share and relatively few Reddit tasks (p. 7).

**Caveat:** The paper does not report a scalar diversity index, clustering reliability, prompt sensitivity, or human validation.

## X4 — URL-depth behavior

**Purpose:** Determine whether downstream successes involve deeper website navigation.

**Method:** Compare maximum URL path depth across all trajectories, Go-Browse-only successes, and NNetNav-only successes (pp. 7–8, Figure 5).

**Result:** Overall distributions are similar. Go-Browse-only successes are more right-skewed, supporting the claim that some distinctive Go-Browse wins require deeper navigation.

**Caveat:** URL segment count is a proxy for navigation depth; it need not always equal interaction difficulty.

## X5 — URL visitation patterns

**Purpose:** Identify particular routes disproportionately visited in successful trajectories.

**Result:** Go-Browse has larger counts for deep Shopping Admin edit/order pages and direct Reddit search or profile-edit routes. NNetNav has more visits to several GitLab project-creation, commit, and fork routes (p. 8, Table 4).

## X6 — Prefixed versus unprefixed sampling

**Purpose:** Test whether resetting directly to task-source pages improves solver success.

**Conditions:** All models and Qwen alone, each under prefixed and unprefixed sampling, grouped by graph-node depth.

**Result:** Prefixed sampling is consistently stronger and its advantage grows on deeper nodes. The weaker Qwen solver’s unprefixed success falls especially sharply at depth 17–20 (p. 8, Figure 6).

**Caveat:** Exact values are not labeled; most values can only be estimated visually.

## X7 — FeasibilityChecker efficiency

**Purpose:** Quantify avoided work from filtering infeasible proposed tasks.

**Result:** 403 tasks were filtered, avoiding approximately 3,200 trajectory rollouts and 29,400 steps; the paper reports a 13% reduction in steps for the same amount of positive data (p. 9).

## X8 — Outer-loop coverage ablation

**Purpose:** Isolate the contribution of resets/frontier breadth while holding total proposed tasks at 30 per domain.

**Result:** Unique URLs rise from 183 with 1 reset × 30 tasks, to 214 with 5 × 6, and 260 with 15 × 2 (p. 9, Table 5).

**[C] Derived:** 260 versus 183 is 77 additional URLs, a relative increase of \(77/183\approx42.1\%\).

## X9 — PageExplorer model comparison

**Purpose:** Explain the complementary use of GPT-4o and Claude-3.7-Sonnet.

**Result:** Claude proposes 1,439 tasks in total with a 10-step budget; GPT-4o proposes 744 with a 20-step budget. GPT-4o nevertheless produces more modification-task clusters: 34 versus 19 (p. 15, Table 7).

**[C] Derived:** Claude proposes approximately \(1,439/744=1.93\) times as many tasks, while GPT-4o yields approximately \(34/19=1.79\) times as many modification clusters.

## X10 — NavExplorer contribution

**Purpose:** Test whether a dedicated navigation proposer expands navigational-task collection.

**Result:** NavExplorer produces 925 navigation tasks in 32 clusters; PageExplorer produces 689 in 31 clusters (p. 15, Table 8).

**[C] Derived:** NavExplorer contributes 236 more navigation tasks, or approximately 34.3% more than PageExplorer.

## X11 — Collection-cost analysis

**Purpose:** Attribute the $975.57 collection cost.

**Result:** Agent rollouts cost $754.66 and trajectory evaluation costs $220.91 (p. 16, Table 9). Claude accounts for the largest model-specific rollout cost, $466.11.

## X12 — Paired bootstrap tests

**Purpose:** Assess whether WebArena performance differences are stable under resampling.

**Results:** Go-Browse-7B versus Qwen has \(p<0.001\) in prose and 0.000 in the table; versus NNetNav \(p=0.094\); versus GPT-4o-mini \(p=0.108\). GPT-4o and Claude significantly outperform Go-Browse in the reverse direction (p. 16, Table 10).

**Caveat:** Only the Qwen comparison meets a conventional 0.05 threshold. The paper accurately calls the GPT-4o-mini and NNetNav results “a moderate degree of confidence,” although “judged as better” should not be read as statistically significant.

## X13 — IDA versus OOD analysis

**Purpose:** Separate transfer to sites similar to WebArena from transfer to more dissimilar sites.

**Results (Figure 7):**

| Model | IDA SR | OOD SR |
|---|---:|---:|
| Go-Browse-7B | 5.3% | 4.9% |
| NNetNav-7B | 2.3% | 7.3% |
| GPT-4o-mini | 6.0% | 15.4% |

Go-Browse approaches GPT-4o-mini on IDA tasks but trails NNetNav on OOD tasks.

**Caveat:** The IDA/OOD split was generated by an LLM, and subgroup sample sizes are not reported.

## X14 — Difficulty-stratified OM2W analysis

**Purpose:** Explain NNetNav’s OOD advantage.

**Result:** Figure 8 shows that NNetNav’s higher OOD count largely comes from easy tasks: 7 easy successes versus Go-Browse’s 4. On IDA tasks, Go-Browse has 5 easy, 1 medium, and 1 hard success (p. 17).

## X15 — Qualitative OM2W examples

Table 11 lists successes and failures by model, domain category, and difficulty across pp. 17–19. It illustrates substantial task variety, from information retrieval to filtered search and calculator interaction. These are examples, not a systematic error taxonomy.

# 9. Results

## Main benchmark finding

Go-Browse-7B scores **21.7%** on WebArena (pp. 6–7, Table 3).

Comparisons:

- versus Qwen-2.5-7B-Instruct: \(21.7-8.3=13.4\) **percentage points** [C], or approximately 161.4% relative improvement [C];
- versus NNetNav-7B: \(21.7-18.8=2.9\) percentage points [C], approximately 15.4% relative;
- versus GPT-4o-mini: \(21.7-19.3=2.4\) percentage points [C], approximately 12.4% relative.

The paper calls these differences “13.4%,” “2.9%,” and “2.4%”; because the metric itself is a percentage, they are more precisely percentage-point differences.

Go-Browse does not beat the larger closed models: GPT-4o scores 37.6% and Claude-3.7-Sonnet 45.4%.

## Domain results

| Domain | Go-Browse | NNetNav | GPT-4o-mini | Interpretation |
|---|---:|---:|---:|---|
| Admin | 25.3 | 14.3 | 19.2 | Go-Browse leads both |
| Shopping | 22.4 | 20.3 | 19.3 | Go-Browse narrowly leads |
| Reddit | 30.7 | 23.7 | 21.1 | Go-Browse leads |
| GitLab | 15.3 | 19.9 | 20.9 | Go-Browse trails both |
| Map | 17.9 | 17.2 | 15.6 | Go-Browse narrowly leads |

All values are success-rate percentages from Table 3.

The prose says Go-Browse beats NNetNav by “11%” on Shopping Admin and “7%” on Reddit. These correspond exactly to 11.0 and 7.0 percentage points.

## Generalization result

On Online-Mind2Web, Go-Browse-7B scores 5.33%, above NNetNav’s 4.00% but below GPT-4o-mini’s 9.33% (p. 6, Table 2). Within the LLM-defined IDA subset, Go-Browse is within 0.7 percentage points of GPT-4o-mini and 3.0 points above NNetNav (pp. 16–17, Figure 7).

## Dataset and collection results

- 9,504 successful and 17,245 failed trajectories (p. 6, Table 1).
- 39,339 successful and 157,123 failed steps.
- 3,422 unique tasks.
- 29.5%, 36.6%, and 33.9% of successful trajectories come from Qwen, GPT-4o-mini, and Claude, respectively (p. 6, Figure 3).
- Feasibility filtering saves approximately 29,400 steps, reported as 13%.
- Increased reset breadth raises unique URLs from 183 to 260.
- Prefixed sampling is most beneficial on deep nodes and for Qwen.
- Cost is $975.57; elapsed generation time is approximately three weeks.

# 10. Figure-by-Figure Interpretation

### Figure 1 — Go-Browse architecture and workflow

- **Location:** p. 2.
- **Type:** system/process diagram.
- **Contents:** an outer-loop website graph on the left and a three-stage inner loop on the right.
- **Outer loop:** selects a frontier page, explores it, adds discovered pages, and can update an edge when a shorter route is found.
- **Inner stages:** propose tasks, check feasibility, and sample trajectories.
- **Encoding:** black, blue, purple, green, and red paths distinguish pages, task proposals, feasible/failed trajectories, and solver samples.
- **Conclusion supported:** Go-Browse reuses discoveries across episodes and separates global navigation from local task execution.
- **Caveat:** This is a conceptual illustration, not a quantitative result.

### Figure 2 — Interaction-first versus instruction-first exploration

- **Location:** p. 4.
- **Type:** paired pseudocode comparison, presented as a figure.
- **Left:** exploration first, retrospective labeling second.
- **Right:** task proposal first, task-conditioned rollout second, reward filtering third.
- **Conclusion supported:** establishes the two methodological families that Go-Browse combines.
- **Caveat:** The supplied algorithm line `G ← P(s0, )` contains an apparent empty argument after the comma; its intended second argument is not specified here.

### Figure 3 — Source models for successful trajectories

- **Location:** p. 6.
- **Type:** segmented proportion bar.
- **Values:** Qwen 29.5%, GPT-4o-mini 36.6%, Claude-3.7-Sonnet 33.9%.
- **Observation:** contributions are relatively balanced; GPT-4o-mini supplies the largest share.
- **[C] Check:** values sum to 100.0%.
- **Caveat:** This gives proportions, not absolute counts or success rates per model.

### Figure 4 — Task-category distributions

- **Location:** p. 7.
- **Panels:** (a) NNetNav-WA; (b) Go-Browse-WA.
- **Type:** hierarchical sunburst charts.
- **Inner categories:** five WebArena domains.
- **Outer wedges:** higher-level task-intent clusters with many labeled subcategories.
- **Direct observation:** Go-Browse-WA has a more balanced domain allocation and generally finer-grained wedges; NNetNav-WA is visually dominated more by GitLab and has less Reddit.
- **Conclusion supported:** Go-Browse’s persistent page resets reduce repetitive concentration on easy-to-rediscover areas.
- **Caveats:** No numeric diversity statistic or wedge-value table is supplied. Many outer labels are small, so only the high-level distribution is confidently interpretable.

### Figure 5 — Maximum URL depth

- **Location:** p. 8.
- **Panels:** all trajectories; Go-Browse-only successes; NNetNav-only successes.
- **Axes:** x = maximum URL path depth, measured as number of URL path segments; y = density.
- **Encoding:** blue = Go-Browse; red = NNetNav; dashed vertical lines indicate distribution summaries, apparently central values, but the caption does not define them.
- **Observation:** all-trajectory curves are similar. Go-Browse-only successes shift toward deeper paths relative to NNetNav on those same tasks. The NNetNav-only panel shows much less separation.
- **Conclusion supported:** some unique Go-Browse successes are associated with deeper navigation.
- **Uncertainty:** Exact distribution statistics are not labeled.

### Figure 6 — Prefixed-sampling success by node depth

- **Location:** p. 8.
- **Axes:** x = node-depth ranges 1–4, 5–8, 9–12, 13–16, 17–20; y = success rate from 0 to roughly 0.3.
- **Node-depth definition:** shortest trajectory length from root, calculated with Dijkstra’s algorithm.
- **Lines:** all-model prefixed/unprefixed and Qwen prefixed/unprefixed.
- **Observation:** prefixed curves remain above unprefixed curves, with the Qwen-unprefixed curve dropping especially sharply at depth 17–20.
- **Approximate visual values:** most curves begin near 0.27–0.31; Qwen-unprefixed falls to roughly 0.08 in the deepest bin. These are visual estimates, not reported exact numbers.
- **Conclusion supported:** resetting to a deep page allows weaker models to generate successful local demonstrations.
- **Caveat:** No error bars, counts, or exact bin values are given.

### Figure 7 — Online-Mind2Web IDA/OOD performance

- **Location:** p. 17.
- **Type:** grouped bar chart.
- **Axes:** model versus success rate (%), 0–20%.
- **Values:** Go-Browse 5.3% IDA/4.9% OOD; NNetNav 2.3%/7.3%; GPT-4o-mini 6.0%/15.4%.
- **Conclusion supported:** Go-Browse transfers relatively well to sites deemed similar to WebArena, but not as well as NNetNav on the OOD subset.
- **Notable observation:** GPT-4o-mini is much stronger on OOD than IDA, showing that “OOD” is not synonymous with “harder” in this partition.
- **Caveat:** Subset sizes and uncertainty are absent.

### Figure 8 — Online-Mind2Web successes by difficulty

- **Location:** p. 17.
- **Panels:** IDA and OOD.
- **Axes:** model versus count of successes.
- **Legend:** easy, medium, hard.
- **IDA counts:** GPT-4o-mini 4/2/2; Go-Browse 5/1/1; NNetNav 2/1/0.
- **OOD counts:** GPT-4o-mini 16/2/1; Go-Browse 4/2/0; NNetNav 7/1/1.
- **Conclusion supported:** NNetNav’s OOD advantage over Go-Browse is mainly attributable to easy tasks.
- **Caveat:** Counts alone cannot yield difficulty-specific success rates without the number of tasks in each subgroup.

# 11. Table-by-Table Interpretation

### Table 1 — Go-Browse-WA composition

- **Location:** p. 6.
- **Rows:** trajectories, steps, and unique tasks.
- **Columns:** success, failure, total.
- **Values:** 9,504/17,245/26,749 trajectories; 39,339/157,123/196,462 steps; 3,422 unique tasks.
- **[C] Derived:** trajectory success share is \(9,504/26,749\approx35.5\%\). Successful steps are approximately 20.0% of all steps.
- **Observation:** failed trajectories are longer on average: \(157,123/17,245\approx9.11\) steps versus \(39,339/9,504\approx4.14\) for successes [C].
- **Caveat:** Unique-task success/failure distribution is not given.

### Table 2 — Overall Online-Mind2Web results

- **Location:** p. 6.
- **Metric:** success rate (%).
- **Values:** NNetNav-7B 4.00; Go-Browse-7B 5.33; GPT-4o-mini 9.33.
- **Best:** GPT-4o-mini.
- **Open-weight comparison:** Go-Browse leads NNetNav by 1.33 percentage points [C].

### Table 3 — WebArena results

- **Location:** p. 7.
- **Rows:** three closed models and three open-weight 7B models.
- **Columns:** overall and five domains.
- **Best overall:** Claude-3.7-Sonnet, 45.4%.
- **Best open-weight 7B overall:** Go-Browse-7B, 21.7%.
- **Go-Browse strength:** Admin and Reddit.
- **Go-Browse weakness:** GitLab, where it trails NNetNav by 4.6 points.
- **Statistical information:** none within the table; Appendix Table 10 provides bootstrap results.

### Table 4 — URLs with largest successful-visit differences

- **Location:** p. 8.
- **Columns:** URL pattern, Go-Browse visits, NNetNav visits, absolute difference, and URL depth.
- **Largest Go-Browse advantage:** Shopping Admin product-edit URL, 10 versus 1, difference 9, depth 5.
- **Deepest listed route:** configurable-product edit route at depth 12, 5 versus 0.
- **Largest NNetNav advantage:** GitLab new-project route, 6 versus 2, difference 4.
- **Interpretation:** Go-Browse successes disproportionately involve specific edit/detail/search routes; NNetNav’s advantages concentrate in GitLab.
- **Caveat:** The table is a selected top-difference list, not the full URL distribution.

### Table 5 — Outer-loop reset ablation

- **Location:** p. 9.
- **Conditions:** resets/tasks per reset, with 30 proposed tasks per domain held constant.
- **Values:** 1/30 → 183 URLs; 5/6 → 214; 15/2 → 260.
- **Conclusion:** spreading proposals across more reset nodes increases coverage.
- **Caveat:** Downstream task quality and model performance are not reported for these configurations.

### Table 6 — Agent action space

- **Location:** p. 12.
- **Purpose:** defines 15 executable action types.
- **Groups:** element interaction, scrolling/keyboard input, URL/history navigation, tab control, user response, and infeasibility reporting.
- **Notable point:** NavExplorer also uses `add_tasks_to_dataset`, described in §3 and Appendix A.2 but not included in Table 6’s base action-space list.

### Table 7 — GPT-4o versus Claude for PageExplorer

- **Location:** p. 15.
- **Columns:** task counts and cluster counts for navigation, information, and modification tasks; maximum steps.
- **GPT-4o:** 274/227/243 tasks and 24/18/34 clusters with 20 steps.
- **Claude:** 415/508/516 tasks and 23/19/19 clusters with 10 steps.
- **Conclusion:** Claude is more prolific; GPT-4o adds modification-task diversity.
- **Caveat:** Cluster quality is judged through an LLM-based pipeline without reported validation.

### Table 8 — NavExplorer versus PageExplorer

- **Location:** p. 15.
- **Values:** NavExplorer 925 navigation tasks/32 clusters; PageExplorer 689/31.
- **Conclusion:** the dedicated NavExplorer substantially raises quantity, while cluster counts are nearly identical.
- **Interpretation [D]:** Much of the added value appears to be more examples within a similar number of broad categories, not dramatically more category breadth.

### Table 9 — Collection costs

- **Location:** p. 16.
- **Panel A:** rollout costs by model.
- **Panel B:** GPT-4o evaluation cost.
- **Totals:** $754.66 rollouts + $220.91 evaluation = $975.57.
- **Largest cost:** Claude, $466.11.
- **[C] Derived shares:** Claude is approximately 61.8% of rollout cost and 47.8% of grand total; evaluation is approximately 22.6% of grand total.
- **Discrepancy:** Panel A reports 27,103 trajectories and 199,844 steps, whereas Table 1 reports 26,749 trajectories and 196,462 dataset steps. The likely distinction is that cost accounting includes proposal/collection rollouts not retained in the released dataset, but the paper does not explicitly reconcile the difference.

### Table 10 — Bootstrap comparisons

- **Location:** p. 16.
- **Columns:** comparator, winner, baseline/tie/Go-Browse win ratio, and p-value.
- **Go-Browse versus Qwen:** 100% Go-Browse bootstrap wins, table p-value 0.000.
- **Versus NNetNav:** Go-Browse win fraction 0.906, \(p=0.094\).
- **Versus GPT-4o-mini:** Go-Browse win fraction 0.892, \(p=0.108\).
- **Versus GPT-4o and Claude:** Go-Browse loses every listed bootstrap comparison.
- **Caveat:** A displayed p-value of 0.000 should be interpreted as below reporting precision, consistent with the prose’s \(p<0.001\), not literally proof of zero probability.

### Table 11 — Qualitative Online-Mind2Web examples

- **Location:** pp. 17–19.
- **Columns:** model, domain type, result, difficulty, website, and task.
- **Coverage:** examples include easy/medium/hard successes and failures for all three models across IDA and OOD sites.
- **Examples:** Go-Browse succeeds on an IDA CVS multiconstraint product query and an OOD drug-interaction query; NNetNav succeeds on a hard OOD retirement-calculator task; GPT-4o-mini succeeds on a hard OOD version of the same task.
- **Purpose:** illustrate task breadth and outcomes.
- **Caveat:** Examples are selectively presented and cannot establish frequencies or causal failure patterns.

# 12. Diagram / Architecture Interpretation

Go-Browse has two nested control loops:

```text
Website root
    ↓
Frontier of discovered URLs
    ↓ select one URL
NavExplorer + PageExplorer
    ↓ proposed navigation and local tasks
FeasibilityChecker + judge
    ├─ infeasible → discard
    └─ feasible → retain initial success
                     ├─ new URL found → add node/edge/frontier entry
                     └─ Solvers
                          ├─ prefixed samples from current page
                          └─ unprefixed samples from root
    ↓
Repeat until frontier is empty
```

The **control path** is the frontier-selection loop. The **data path** converts observations into task proposals, proposals into judged trajectories, and successful task–trajectory pairs into dataset entries.

The main feedback loop occurs when solving a task discovers a new URL. That URL is inserted into the frontier and becomes the starting point for a future local exploration episode. This is what turns a set of independent rollouts into cumulative structured exploration.

The diagram also shows an edge-update operation when a shorter path is discovered. Algorithm 3 says only “Add new edges,” so the exact data structure and shortest-path update procedure are not fully specified in the pseudocode.

# 13. Equations and Mathematical Concepts

The paper contains no numbered equations, theorem sequence, or formal proof. Its essential mathematical definitions are:

## Agent transition

\[
(s_t,a_t)\rightarrow s_{t+1}
\]

A language model observes state \(s_t\), selects action \(a_t\), and execution produces the next state (pp. 2–3).

## Trajectory

\[
\tau=\{s_1,a_1,s_2,a_2,\ldots,s_T,a_T\}
\]

This is the ordered history of states and actions for one task. \(T\) is the maximum horizon or final termination step (p. 3).

## Binary task reward

\[
R(g,\tau)\in\{0,1\}
\]

Here \(g\) is the goal and \(\tau\) the attempted trajectory. A value of 1 denotes success and 0 failure (p. 3).

## Instruction-first task set

\[
\mathcal{G}=\{g_1,g_2,\ldots,g_K\}
\]

A proposer generates \(K\) plausible tasks from a webpage state; successful \((g_i,\tau_i)\) pairs are added to dataset \(D\) (p. 3).

## Website graph

\[
G=(V,E)
\]

Each \(v\in V\) is a unique URL and each \(e\in E\) is a trajectory between URLs (p. 4). A frontier \(F\subseteq V\) operationally stores discovered but incompletely explored nodes.

## Dataset union

Algorithm 3 repeatedly performs set-like additions such as:

\[
D\leftarrow D\cup\{(g,\tau)\}
\]

In plain language, successful task–trajectory pairs are appended to the training collection.

## Node depth

For Figure 6, depth is the shortest trajectory length from the root node, computed with Dijkstra’s algorithm. For Figure 5, by contrast, URL depth is the number of segments in the URL path. These are two different depth constructs and should not be conflated.

# 14. Interpretation and Discussion

The results support the paper’s main mechanism in several connected ways:

- The reset ablation shows that distributing task proposals across more discovered nodes increases URL coverage.
- Figure 6 shows that starting at discovered pages especially benefits weak solvers on deep nodes.
- Figure 4 suggests that the resulting dataset is less concentrated in a small set of task categories.
- Figure 5 and Table 4 connect Go-Browse’s distinctive successes to deeper or more specific page routes.
- Table 3 shows downstream gains on domains where Go-Browse’s data distribution is stronger, especially Shopping Admin and Reddit.

Together, this forms a coherent author argument: structured exploration changes what data are collected, and those data improve the trained model’s ability to operate deeper in the explored sites.

The evidence is strongest for **in-domain WebArena improvement over the unmodified Qwen model**. The 13.4-point difference is large and the paired bootstrap test reports \(p<0.001\).

Evidence against NNetNav and GPT-4o-mini is favorable but less decisive statistically. The observed point estimates favor Go-Browse, and most bootstrap resamples do as well, but \(p=0.094\) and \(p=0.108\) do not meet a conventional 0.05 criterion.

Generalization is mixed:

- Go-Browse exceeds NNetNav overall on Online-Mind2Web.
- It nearly matches GPT-4o-mini on the IDA subset.
- It trails NNetNav on truly OOD tasks.
- Its absolute OM2W success rate remains low at 5.33%.

The supplied evidence therefore supports transfer to websites resembling the training environments more strongly than broad transfer to unrelated sites.

## Consistency checks

Several discrepancies or qualifications matter:

1. **Trajectory-count inconsistency:** Table 1 reports 17,245 failed trajectories, but §8 says the released dataset contains “39K unsuccessful task solving trajectories.” This appears inconsistent. The 39K figure may have been confused with the 39,339 successful **steps**, but the supplied document does not resolve it.
2. **Abstract compression:** The abstract says “10K successful trajectories and 40K interaction steps,” apparently referring approximately to 9,504 successes and 39,339 successful steps. It does not mention the full 196,462-step released collection.
3. **Cost versus dataset counts:** Table 9 reports 27,103 rollout trajectories and 199,844 steps, exceeding Table 1 by 354 trajectories and 3,382 steps. This may include discarded/task-proposal work, but no explicit reconciliation is given.
4. **“Statistically significantly” wording:** Appendix B.3 explicitly calls the Qwen comparison statistically significant. It does not make that formal claim for GPT-4o-mini or NNetNav; their p-values are above 0.05.
5. **Depth definitions differ:** Figure 5 uses URL path segments; Figure 6 uses shortest graph-trajectory length.
6. **OOD naming varies:** The paper alternates between “Out-of-Domain” and “Out-of-Distribution.” They appear to refer to the same OM2W subgroup.
7. **IDA typo:** p. 17 refers once to “IAD”; context indicates IDA.

# 15. Contributions and Novelty

## Conceptual contribution

Treat website data collection as cumulative graph exploration instead of independent episodes.

## Algorithmic contribution

A nested outer/inner loop that combines frontier traversal, task proposal, feasibility checking, and solver sampling.

## Methodological contribution

Use agentic task proposers that gather context through interaction instead of relying only on a static initial page or human demonstrations.

## Data contribution

Go-Browse-WA: 26,749 retained trajectories, 196,462 steps, and 3,422 tasks across 100 URLs in five WebArena domains, with multiple observation representations.

## Training contribution

A straightforward supervised fine-tuning recipe using only successful trajectories to produce Go-Browse-7B.

## Empirical contribution

A 21.7% WebArena success rate, above the compared 7B baselines and GPT-4o-mini, plus analyses linking coverage, diversity, prefixed sampling, and navigation depth.

## Implementation/reproducibility contribution

The authors state that code, data, models, and reproduction documentation are released, and provide prompts, action space, collection settings, training hyperparameters, hardware, runtime, and cost accounting.

# 16. Limitations

## Authors' stated limitations

The authors explicitly acknowledge (pp. 9–10):

- Data were collected from only five WebArena domains; broader website coverage remains future work.
- Training uses only successful trajectories, leaving approximately 39K unsuccessful trajectories, as described in the conclusion, unused. This count conflicts with Table 1’s 17,245 failed trajectories.
- Alternative training objectives, including reinforcement-learning objectives, might exploit failure data.
- Scaling model size may improve performance.
- LLM-generated data may inherit biases from models and prompts and requires auditing and mitigation before deployment.

## Additional evidence-based analyst observations

These are analyst observations, not author admissions:

- **Judge dependence:** Feasibility labels rely on a GPT-4o-based judge, but judge accuracy and disagreement with benchmark-native evaluators are not quantified.
- **LLM-generated categorization:** Task diversity and IDA/OOD analyses depend on GPT-4o-mini classifications without reported human validation.
- **Single-run uncertainty:** Random seeds, repeated fine-tuning runs, and variance across training runs are not reported.
- **Incomplete training specification:** Optimizer, scheduler, weight decay, precision, and checkpoint-selection details are absent.
- **Limited statistical strength:** Improvements over NNetNav and GPT-4o-mini are not significant at 0.05 under the reported paired bootstrap test.
- **Low absolute task success:** Even on WebArena, 78.3% of tasks remain unsuccessful; on OM2W, Go-Browse succeeds on only 5.33%.
- **Confounded model pipeline:** Multiple proprietary models participate in proposal, feasibility checking, judging, and trajectory production, making it difficult to attribute gains to any single component.
- **No end-to-end cost comparison:** Collection cost is reported, but not compared under a common budget against NNetNav or other collection methods.
- **Potential task-distribution effects:** Domain gains correlate with dataset balance, but the paper does not establish causality through domain-controlled training ablations.
- **URL-as-node abstraction:** Dynamic states at the same URL may represent very different page contents or configurations.
- **Live-site instability:** Online-Mind2Web evaluation may be affected by site changes, but temporal variability is not analyzed.
- **Chain-of-thought storage/use:** The prompts request explicit reasoning, but the paper does not clarify whether these reasoning strings are included in training, filtered, or audited.

# 17. Threats to Validity

## Internal validity

Performance gains may reflect the combination of stronger proposal models, judge behavior, sampling distribution, and graph structure rather than graph exploration alone. The outer-loop and prefixed-sampling analyses support individual mechanisms, but no full factorial ablation separates every component.

## Construct validity

- Success rate captures binary task completion but not partial completion, safety, efficiency, or user satisfaction.
- URL path depth and graph-node depth are proxies for navigation complexity.
- Cluster counts are a proxy for task diversity and depend on LLM-generated grouping.
- An LLM-defined IDA/OOD label may not perfectly measure semantic distance from WebArena.

## Statistical conclusion validity

The paper supplies paired bootstrap p-values but not confidence intervals or repeated-training variance. Improvements over NNetNav and GPT-4o-mini have p-values of 0.094 and 0.108. Subgroup analyses provide raw rates or counts without uncertainty.

## External validity

Training covers five WebArena domains. OM2W performance shows some transfer, but the low absolute success rate and weaker truly-OOD result limit claims of broad website generalization.

## Ecological validity

WebArena uses self-hosted clones; Online-Mind2Web uses live websites and is more realistic in that respect, but live sites also introduce instability. The paper does not evaluate deployment with real users.

## Reproducibility

Strengths include released artifacts, prompts, action space, budgets, hardware, cost, and major fine-tuning settings. Remaining gaps include seeds, several optimizer details, precise preprocessing, judge calibration, graph canonicalization, and reconciliation of dataset/cost counts.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- Expand data collection beyond the five WebArena domains.
- Construct larger datasets.
- Learn from unsuccessful trajectories using alternative objectives such as reinforcement learning.
- Scale model size.
- Audit and mitigate biases introduced by models and prompts.

## B. Additional open questions

- How accurate is the VLM judge, especially for subtle state-modification tasks?
- How much of the gain comes from the outer loop, task proposers, feasibility filtering, or prefixed sampling under equal cost?
- Would state-aware nodes outperform URL-only nodes on dynamic sites?
- Does training on prefixed trajectories reduce the ability to navigate from a root page unless balanced by unprefixed samples?
- What is the optimal prefixed/unprefixed ratio?
- How stable are results across random seeds and training runs?
- Can task diversity be measured with validated, non-LLM-dependent metrics?
- Does Go-Browse retain its advantage under an equal-dollar or equal-step comparison with NNetNav?
- How do safety-sensitive actions, authentication, destructive operations, and private data affect automated exploration?
- Can failed trajectories be used without teaching undesirable behavior?
- Why does NNetNav generalize better on the paper’s truly OOD subset?
- How should the conflicting failed-trajectory counts be resolved?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| LLM | Large language model |
| VLM | Vision-language model; here used to judge actions using text and a screenshot |
| GUI | Graphical user interface |
| Web agent | A model-controlled system that observes and acts on websites |
| ReAct | A pattern that alternates reasoning and action |
| Accessibility tree | Textual hierarchy of a webpage’s interactive and semantic elements |
| State \(s_t\) | Everything the agent observes at step \(t\) |
| Action \(a_t\) | The operation selected at step \(t\) |
| Goal \(g\) | The task the agent is trying to complete |
| Trajectory \(\tau\) | A sequence of states and actions for one task attempt |
| Horizon \(T\) | Maximum number of interaction steps |
| Reward \(R(g,\tau)\) | Binary success/failure judgment |
| Exploration policy | Procedure for deciding how to explore and collect data |
| Interaction-first | Explore first, label the behavior afterward |
| Instruction-first | Propose a task first, then attempt it |
| Frontier \(F\) | Discovered URLs waiting to be explored |
| Graph \(G=(V,E)\) | Website map with URLs as nodes and navigation trajectories as edges |
| NavExplorer | Agent that discovers neighboring pages and proposes navigation tasks |
| PageExplorer | Agent that proposes tasks local to the current page |
| FeasibilityChecker | Attempts and judges proposed tasks before retaining them |
| Solver | Model that generates extra trajectories for feasible tasks |
| Prefixed sampling | Begin on the task’s source page |
| Unprefixed sampling | Begin at the website root |
| Bootstrapping | Enabling a weaker model to generate useful examples by simplifying part of its job |
| Supervised fine-tuning | Training a model to imitate successful examples |
| Open-weight | Model whose learned weights are available |
| Success rate (SR) | Percentage of benchmark tasks completed |
| IDA | In-Domain-Adjacent: a live site judged similar to WebArena |
| OOD | Out-of-Domain/Out-of-Distribution: judged dissimilar to WebArena |
| Paired bootstrap | Resampling matched task results to examine the stability of a performance difference |
| Percentage point | Absolute difference between two percentages |
| Relative improvement | Difference divided by the baseline percentage |
| Dijkstra’s algorithm | The method used here to compute shortest graph-path depth |
| SLURM | Cluster job-management system |
| VRAM | GPU memory |
| Gradient accumulation | Combining gradients over several mini-steps before updating model weights |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Websites/domains | 5 | domains | WebArena collection | Author-reported | p. 5, §4 |
| Explored URLs | 100 | URLs | 20 per domain | Author-reported | pp. 5–6 |
| Retained trajectories | 26,749 | trajectories | Go-Browse-WA | Author-reported | p. 6, Table 1 |
| Successful trajectories | 9,504 | trajectories | Go-Browse-WA | Author-reported | p. 6, Table 1 |
| Failed trajectories | 17,245 | trajectories | Go-Browse-WA | Author-reported | p. 6, Table 1 |
| Total steps | 196,462 | steps | Retained dataset | Author-reported | p. 6, Table 1 |
| Successful steps | 39,339 | steps | Retained dataset | Author-reported | p. 6, Table 1 |
| Failed steps | 157,123 | steps | Retained dataset | Author-reported | p. 6, Table 1 |
| Unique tasks | 3,422 | tasks | Go-Browse-WA | Author-reported | p. 6, Table 1 |
| Trajectory success share | 35.5 | % | 9,504 / 26,749 | Analyst-derived | p. 6, Table 1 |
| Qwen/mini/Claude success-source shares | 29.5 / 36.6 / 33.9 | % | Successful trajectories | Visually readable | p. 6, Figure 3 |
| WebArena tasks | 812 | tasks | Main benchmark | Author-reported | p. 6, §5 |
| Go-Browse WebArena SR | 21.7 | % | Overall | Author-reported | p. 7, Table 3 |
| NNetNav WebArena SR | 18.8 | % | Overall | Author-reported | p. 7, Table 3 |
| GPT-4o-mini WebArena SR | 19.3 | % | Overall | Author-reported | p. 7, Table 3 |
| Qwen base WebArena SR | 8.3 | % | Overall | Author-reported | p. 7, Table 3 |
| Go-Browse minus NNetNav | 2.9 | percentage points | WebArena overall | Analyst-derived | p. 7, Table 3 |
| Go-Browse minus GPT-4o-mini | 2.4 | percentage points | WebArena overall | Analyst-derived | p. 7, Table 3 |
| Go-Browse minus base Qwen | 13.4 | percentage points | WebArena overall | Analyst-derived | p. 7, Table 3 |
| OM2W tasks/sites | 300 / 136 | tasks/sites | Generalization test | Author-reported | p. 6, §5 |
| OM2W SR: Go-Browse | 5.33 | % | Overall | Author-reported | p. 6, Table 2 |
| OM2W SR: NNetNav | 4.00 | % | Overall | Author-reported | p. 6, Table 2 |
| OM2W SR: GPT-4o-mini | 9.33 | % | Overall | Author-reported | p. 6, Table 2 |
| Filtered tasks | 403 | tasks | FeasibilityChecker | Author-reported | p. 9, §6 |
| Avoided rollouts | ~3,200 | trajectories | Feasibility filtering | Author-reported | p. 9 |
| Avoided steps | ~29,400 | steps | Feasibility filtering | Author-reported | p. 9 |
| Reported step reduction | 13 | % | Same positive-data amount | Author-reported | p. 9 |
| Unique URLs, narrow resets | 183 | URLs | 1 reset × 30 tasks | Author-reported | p. 9, Table 5 |
| Unique URLs, broad resets | 260 | URLs | 15 resets × 2 tasks | Author-reported | p. 9, Table 5 |
| Relative URL increase | 42.1 | % | 260 versus 183 | Analyst-derived | p. 9, Table 5 |
| Collection cost | 975.57 | USD | Rollouts plus evaluation | Author-reported | p. 16, Table 9 |
| Collection duration | ~3 | weeks | Dataset generation | Author-reported | p. 20, Appendix C |
| Bootstrap samples | 10,000 | samples | WebArena comparison | Author-reported | p. 16, Table 10 |
| p-value vs Qwen | <0.001 | p-value | Paired bootstrap | Author-reported | p. 16, Appendix B.3 |
| p-value vs NNetNav | 0.094 | p-value | Paired bootstrap | Author-reported | p. 16, Table 10 |
| p-value vs GPT-4o-mini | 0.108 | p-value | Paired bootstrap | Author-reported | p. 16, Table 10 |
| Training epochs | 2 | epochs | Fine-tuning | Author-reported | p. 20, Appendix C |
| Sequence length | 24,000 | tokens | Maximum | Author-reported | p. 20 |
| Learning rate | \(2\times10^{-5}\) | — | Fine-tuning | Author-reported | p. 20 |
| Batch/accumulation | 8 / 4 | samples/steps | Fine-tuning | Author-reported | p. 20 |
| Training hardware | 8×H100, 80 GB each | GPUs/VRAM | One node | Author-reported | p. 20 |
| Training time | ~40 | hours/run | Fine-tuning | Author-reported | p. 20 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Go-Browse improves a 7B model substantially over its pretrained base | 21.7% versus 8.3%; \(p<0.001\) | X1, Tables 3 and 10 | pp. 7, 16 | Strong within supplied WebArena evaluation |
| Go-Browse exceeds NNetNav-7B | 21.7% versus 18.8%; bootstrap win ratio 0.906 | X1/X12 | Tables 3, 10 | Favorable point estimate; \(p=0.094\), not significant at 0.05 |
| Go-Browse exceeds GPT-4o-mini on WebArena | 21.7% versus 19.3%; bootstrap win ratio 0.892 | X1/X12 | Tables 3, 10 | Favorable point estimate; \(p=0.108\) |
| Go-Browse produces broader website coverage | Unique URLs rise 183→214→260 with broader resets | X8 | p. 9, Table 5 | Strong ablation for coverage; no direct downstream-performance result |
| Feasibility filtering improves efficiency | 403 tasks removed; ~29.4K steps avoided; reported 13% reduction | X7 | p. 9 | Direct accounting, though raw denominator is not separately tabulated |
| Prefixed sampling helps weaker models on deep nodes | Prefixed curves exceed unprefixed, especially Qwen at depth | X6 | p. 8, Figure 6 | Clear visual trend; exact values and uncertainty absent |
| Go-Browse-WA is more task-diverse | More balanced domains and finer task wedges | X3 | p. 7, Figure 4 | Suggestive; depends on LLM clustering and lacks scalar diversity statistic |
| Go-Browse successes navigate deeper | Right-shifted Go-Browse-only success distribution; deeper URL examples | X4/X5 | Figure 5, Table 4 | Supported association; not proof that depth causes success |
| Go-Browse generalizes better than NNetNav overall on OM2W | 5.33% versus 4.00% | X2 | p. 6, Table 2 | Small absolute difference; no uncertainty given |
| Transfer is strongest to WebArena-adjacent sites | 5.3% IDA, close to GPT-4o-mini’s 6.0%; above NNetNav’s 2.3% | X13 | pp. 16–17, Figure 7 | Depends on unvalidated LLM-generated IDA/OOD classification |
| NNetNav’s OOD advantage is mainly on easy tasks | 7 versus 4 easy OOD successes | X14 | p. 17, Figure 8 | Supported by counts; denominators per difficulty are absent |
| Dedicated NavExplorer increases navigation-task collection | 925 versus 689 tasks | X10 | p. 15, Table 8 | Strong for quantity; cluster breadth differs only 32 versus 31 |

# 22. Very Simple Explanation

Imagine teaching a robot to use a huge shopping or forum website. If you always start the robot on the homepage, it may repeatedly discover the same obvious pages and never learn what is deeper in the site.

Go-Browse keeps a map of pages it has already found. When it discovers an interesting new page, it remembers it and can start a later training attempt directly there. It asks two kinds of questions: “Where else can I navigate from here?” and “What useful task can I do on this page?” A strong model checks whether each proposed task is actually possible, and cheaper models then practice the feasible ones.

This produced about 9,500 successful examples. Training a 7-billion-parameter model on them raised its WebArena success rate from 8.3% to 21.7%. That was better than the compared NNetNav model and GPT-4o-mini on this benchmark, although the statistical evidence for those two smaller differences was not conclusive at the usual 0.05 threshold.

The big lesson is that training examples improve when exploration remembers previous discoveries. However, the trained model still fails most tasks, performs poorly on unrelated live websites, and was trained from only five website domains.

# Completeness Audit

## Inventory and coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/venue | Yes | Yes | Fully represented | Go-Browse; Gandhi and Neubig; ICLR 2026 |
| Abstract | Yes, visual and text | Yes | Fully represented | Core claims and approximate counts covered |
| §1 Introduction | Yes, visual and text | Yes | Fully represented | Motivation, baselines, gap, novelty covered |
| §2.1 LLM Web Agents | Yes | Yes | Fully represented | State, action, trajectory, reward covered |
| §2.2 Exploration Policies | Yes | Yes | Fully represented | Both policy families and limitations covered |
| §3 Go-Browse | Yes | Yes | Fully represented | Architecture, modules, graph, sampling covered |
| §4 Data Collection | Yes | Yes | Fully represented | Domains, budgets, models, data statistics covered |
| §5 Fine-tuning and Results | Yes | Yes | Fully represented | Training data, benchmarks, metrics, major results covered |
| §6 Analysis | Yes | Yes | Fully represented | All five substantive analyses covered |
| §7 Related Work | Yes | Yes | Represented in compressed form | Three literature categories and positioning retained |
| §8 Conclusion and Limitations | Yes | Yes | Fully represented | Contributions, limitations, and inconsistency covered |
| Reproducibility statement | Yes | Yes | Fully represented | Release claim and reported settings covered |
| Acknowledgements | Yes | No substantive analysis | Deliberately omitted as non-technical | Funding and thanks do not alter method/results |
| References | Yes as text | Partly | Represented in compressed form | Relevant work categories retained; individual citations not re-summarized |
| Figure 1 | Yes, visually | Yes | Fully represented | Architecture/flow explained |
| Figure 2 | Yes, visually | Yes | Fully represented | Includes Algorithms 1–2 comparison |
| Figure 3 | Yes, visually | Yes | Fully represented | Exact labeled proportions included |
| Figure 4a–b | Yes, visually | Yes | Fully represented at interpretable level | Small outer labels compressed |
| Figure 5, three panels | Yes, visually | Yes | Fully represented | Axes, curves, and uncertainty covered |
| Figure 6 | Yes, visually | Yes | Fully represented | Exact unlabeled points treated as approximate |
| Figure 7 | Yes, visually | Yes | Fully represented | All labeled values included |
| Figure 8, two panels | Yes, visually | Yes | Fully represented | All readable counts included |
| Table 1 | Yes, visually | Yes | Fully represented | Includes derived composition statistics |
| Table 2 | Yes, visually | Yes | Fully represented | All rows covered |
| Table 3 | Yes, visually | Yes | Fully represented | All model/domain values discussed |
| Table 4 | Yes, visually | Yes | Fully represented | All ten selected URL rows summarized; key values detailed |
| Table 5 | Yes, visually | Yes | Fully represented | All three conditions included |
| Table 6 | Yes, visually | Yes | Fully represented | Action families and all action functions accounted for |
| Table 7 | Yes, visually | Yes | Fully represented | All task/cluster counts covered |
| Table 8 | Yes, visually | Yes | Fully represented | Both rows covered |
| Table 9 | Yes, visually | Yes | Fully represented | All costs and count discrepancy covered |
| Table 10 | Yes, visually | Yes | Fully represented | All comparisons and p-values covered |
| Table 11 | Partial visual; complete supplied text | Yes | Represented in compressed form | Purpose and examples covered; every row not repeated |
| Algorithm 1 | Yes, visually | Yes | Fully represented | Interaction-first procedure |
| Algorithm 2 | Yes, visually | Yes | Fully represented | Instruction-first procedure; extraction anomaly flagged |
| Algorithm 3 | Yes, visually | Yes | Fully represented | Full control/data flow explained |
| Major equations/definitions | Yes | Yes | Fully represented | Transition, trajectory, reward, task set, graph, depth |
| Appendix A.1 | Yes | Yes | Fully represented | Action space |
| Appendix A.2 | Yes; pp. 13–14 text-only | Yes | Represented in compressed form | Agent, NavExplorer, PageExplorer, and judge prompts summarized |
| Appendix B.1.1 | Yes, visually | Yes | Fully represented | PageExplorer model comparison |
| Appendix B.1.2 | Yes, visually | Yes | Fully represented | Explorer comparison |
| Appendix B.2 | Yes, visually | Yes | Fully represented | Cost analysis |
| Appendix B.3 | Yes, visually | Yes | Fully represented | Bootstrap analysis |
| Appendix B.4 | Yes; p. 17 visual, pp. 18–19 text-only | Yes | Fully represented analytically | Rates, counts, and example-table role covered |
| Appendix C | Yes as text | Yes | Fully represented | Hyperparameters, compute, runtimes, licensing |
| Appendix D | Yes as text | Yes | Fully represented | LLM use disclosed |
| Explicit research questions | Checked | Yes | Not present | Informal objectives were identified without manufacturing formal RQs |
| Explicit hypotheses | Checked | Yes | Not present | Informal testable expectations separated |
| Author-stated limitations | Yes | Yes | Fully represented | All stated limitations included |
| Supplementary material | Not supplied | Yes | Missing from supplied material | No separate supplement detected |
| Code/data/model repository | Not inspected | Yes | Referenced but absent | Closed-document boundary observed |

## Missing or inaccessible material

- No pages are missing from the supplied 20-page text.
- Pages 10, 13–14, and 18–20 were not visually rendered; their content was available through supplied extracted text.
- The continuation of Table 11 on pp. 18–19 was not independently visually inspected.
- The released GitHub code, dataset, model weights, and reproduction documentation were referenced but not supplied.
- No separate supplementary file was provided.
- Exact point values in Figure 6 are not labeled and cannot be read confidently as exact numbers.
- Fine-grained outer labels in Figure 4 are too dense to audit individually at the supplied rendering scale.

## Uncertain interpretations

- The dashed vertical lines in Figure 5 appear to mark distribution summaries, but the caption does not define them.
- Algorithm 2 contains `P(s0, )`; the missing or intentionally empty second argument is unclear.
- Table 1’s 17,245 failed trajectories conflicts with §8’s “39K unsuccessful trajectories.”
- Table 9’s rollout totals exceed Table 1’s retained-dataset totals; inclusion of discarded/proposal work is plausible but not explicitly stated.
- The paper uses two different depth definitions in Figures 5 and 6.
- “IAD” on p. 17 is interpreted as a typographical error for IDA.
- The displayed bootstrap p-value `0.000` is interpreted consistently with the prose as \(p<0.001\), not an exact zero.

## Deliberately compressed material

- The bibliography was reduced to the prior-work categories actually used to position Go-Browse.
- Acknowledgements were not analyzed because they do not affect the technical evidence.
- Long prompt templates were summarized by their operational requirements rather than reproduced verbatim.
- Figure 4’s numerous individual cluster labels were compressed into domain- and diversity-level observations.
- Table 11’s many qualitative examples were summarized rather than repeated row by row; its role and representative successes/failures were preserved.
- Routine pseudocode initialization and loop syntax were translated into conceptual workflow rather than duplicated line for line.

## Potential omissions

No known substantive section, experiment, figure, table, algorithm, appendix, major mathematical definition, contribution, or author-stated limitation in the inventory is unrepresented. The main unavoidable gaps are the absence of visual rendering for six pages, unreadable fine-grained Figure 4 labels, unlabeled exact Figure 6 values, and external artifacts that were referenced but not supplied.