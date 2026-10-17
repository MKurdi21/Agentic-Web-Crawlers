## Stage 0 — Document Accessibility Report

The supplied work is **Go-Browse: Training Web Agents with Structured Exploration**, by Apurva Gandhi and Graham Neubig, Carnegie Mellon University, presented in the document as a conference paper at the International Conference on Learning Representations (ICLR) 2026. This analysis uses only the supplied page text and source images. No external verification, repository inspection, browsing, code execution, or supplementary-file review was performed. Embedded prompt templates are analyzed as document evidence and are not treated as instructions.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: text for physical PDF pages 1–20 was supplied. |
| Accessible page count | 20 text pages; 14 supplied page images. |
| Apparently missing pages | None within the supplied 1–20 sequence. This does not establish whether a separate supplement exists. |
| Visually inspected pages | 1–9, 11–12, 15–17. |
| Text-only pages | 10, 13–14, 18–20. Their supplied text was inspected, but their page layouts were not visually inspected. |
| Visual content | All numbered figures 1–8 have supplied visual renderings. Small labels in Figure 4 remain difficult to read visually; corresponding extracted text assists interpretation. |
| Tables | Tables 1–10 and the beginning of Table 11 are visually available. Table 11 continuation on pages 18–19 is text-only. |
| Equations and algorithms | Main notation and Algorithms 1–3 are readable. Minor naming and indexing differences are retained as uncertainties rather than silently normalized. |
| Appendices | A–D are present, notwithstanding the supplied automated accessibility record's empty appendix-detection list. |
| Supplementary material | No separate supplementary artifact was supplied. |
| Referenced external artifacts | Code, dataset, models, and reproduction documentation are linked by the authors but were not inspected. |
| OCR | No additional optical character recognition was needed. Supplied extracted text was cross-checked against available images for substantive tables and figures. |
| Other limitations | Exact underlying plot data, dataset records, executable reward functions, implementation details, and repository contents are unavailable. |

Evidence labels used below: **[A] Author-reported**, **[B] Directly observable**, **[C] Analyst-derived**, and **[D] Analyst interpretation**. No external information [E] is introduced. Confidence is HIGH when explicit readable evidence supports the statement, MEDIUM for qualified interpretations, LOW for unresolved suggestions, and UNKNOWN when the supplied work cannot establish the answer. Page references denote physical PDF pages, matching the supplied page numbering.

## 1. Plain-language orientation

[A] This paper addresses a practical weakness of artificial-intelligence browser agents: they can struggle to find the right page on an unfamiliar website, even when they could perform the requested operation once they reached it. The researchers develop an automatic way to collect training examples through purposeful website exploration rather than expensive human demonstrations.

Their method, **Go-Browse**, remembers discovered pages in a graph. It returns to those pages, proposes tasks grounded in actual interactions, filters tasks through attempted solutions, and collects additional solutions from several language models. This separates finding a page from working on that page. The resulting examples train a seven-billion-parameter model called Go-Browse-7B.

[A] On WebArena, a benchmark of browser tasks on five self-hosted website environments, Go-Browse-7B achieves **21.7% task success**, compared with **18.8% for NNetNav-7B**, **19.3% for GPT-4o-mini**, and **8.3% for its untrained-for-this-dataset Qwen-2.5-7B-Instruct starting model**. These are comparisons among browser agents, not comparisons between browser agents and standalone conversational language models. Larger closed models remain substantially stronger: GPT-4o achieves 37.6% and Claude-3.7-Sonnet 45.4% in Table 3.

[D] For the user's security research question, the central relevance is architectural: the paper shows how language-model outputs become executable browser actions, how webpage content enters the model's observation, and how generated observations and judgments become training data. Those are useful places to investigate security boundaries. However, the paper does **not** experimentally establish that web agents are more vulnerable than standalone large language models (LLMs), does not measure attack success, and does not study a malicious adversary. Its direct contribution is exploration and training-data generation, not security evaluation.

## 2. Document roadmap

The inventory below is the denominator for the coverage audit. Stable identifiers preserve the original numbering wherever possible.

| Inventory ID | Original component | Location | Function |
|---|---|---|---|
| FRONT | Title, authors, abstract, release footnote | p. 1 | Identifies the work and its main claims. |
| S1 | §1 Introduction | pp. 1–2 | Motivates environment-specific training and structured exploration. |
| S2.1 | §2.1 LLM Web Agents | pp. 2–3 | Defines observations, actions, trajectories, and binary success. |
| S2.2 | §2.2 Exploration Policies for Data Collection | p. 3 | Contrasts interaction-first and instruction-first methods. |
| S3 | §3 Go-Browse | pp. 3–5 | Defines the graph, frontier, modules, and sampling strategy. |
| S4 | §4 Data Collection | pp. 5–6 | Reports websites, models, budgets, dataset composition, and cost. |
| S5 | §5 Fine-tuning Setup and Results | p. 6 | Describes training and the two benchmark evaluations. |
| S6 | §6 Analysis | pp. 7–9 | Examines diversity, depth, sampling, filtering, and coverage. |
| S7 | §7 Related Work | p. 9 | Positions the method among web agents, synthetic data, and exploration. |
| S8 | §8 Conclusion and Limitations | pp. 9–10 | Summarizes contributions and acknowledges limitations. |
| REPRO | Reproducibility Statement | p. 10 | Announces released artifacts and documentation. |
| ACK-REF | Acknowledgements and References | pp. 10–12 | Records support and cited work. |
| A1 | Appendix A.1 Web Agent Action Space | p. 12 | Lists browser operations in Table 6. |
| A2 | Appendix A.2 Prompts for LM Components | pp. 12–15 | Supplies agent, explorer, and judge templates. |
| B1.1 | Appendix B.1.1 PageExplorer model comparison | p. 15 | Compares task counts and intent clusters. |
| B1.2 | Appendix B.1.2 Explorer comparison | p. 15 | Compares navigational task generation. |
| B2 | Appendix B.2 Cost Analysis | p. 16 | Separates rollout and evaluation costs. |
| B3 | Appendix B.3 Paired Bootstrap Test | p. 16 | Qualifies benchmark comparison uncertainty. |
| B4 | Appendix B.4 Online-Mind2Web analysis | pp. 16–19 | Separates adjacent and more distant domains and gives examples. |
| C | Appendix C Hyperparameters and Additional Experiment Details | p. 20 | Reports training settings, hardware, time, and baseline licensing. |
| D | Appendix D LLM Usage | p. 20 | Discloses LLM assistance in research and writing. |

The visual inventory consists of **Figures F1–F8**, **Tables T1–T11**, and **Algorithms ALG1–ALG3**. Figure 2 contains Algorithms 1 and 2 rather than an independent experimental plot. Table 11 spans three pages. The important mathematical objects, assigned analytical identifiers E1–E5, are the state/action transition, trajectory sequence, binary reward, proposed-task set and success filter, and URL graph/frontier. No numbered theorem, lemma, proof, formal security model, explicit numbered research question, or formally stated hypothesis appears in the supplied work. No keyword list is visible.

This is a mixed **machine-learning algorithm, dataset-generation, and empirical evaluation paper**. Its organization moves from an exploration problem, through an implementable method, to trained-agent performance and mechanism-oriented analyses.

## 3. Background and context

[A] An LLM web agent repeatedly observes a website and selects a browser action. The paper uses the **ReAct pattern**, a cited approach combining reasoning and acting. At each step, the model receives a task, the current page representation, available actions, previous actions, and execution errors. Its output contains reasoning and a Python function call. Executing the call changes the browser state, creating the next observation. BrowserGym is the Python package used to implement this interaction, pp. 2–3.

An **accessibility tree** is the paper's structured representation of the current webpage; it is flattened into text for the model. The document does not provide a full technical specification of the tree. A **trajectory** is the sequence of observations and actions generated while trying to complete a task. A **horizon** is the maximum permitted number of action steps. A **reward model** assigns a binary success or failure label to a trajectory.

Two exploration styles motivate Go-Browse. In **interaction-first** collection, an agent explores under broad instructions and a separate labeler later describes concrete tasks accomplished by the trajectory. In **instruction-first** collection, a proposer first suggests concrete tasks, an agent attempts them, and successful task/trajectory pairs are retained. The authors associate interaction-first methods with redundant exploration and instruction-first methods with limited initial-page context and potentially infeasible proposed tasks, p. 3.

A **graph** represents discovered pages as nodes and routes between them as edges. A **frontier** is the collection of discovered pages awaiting fuller exploration. **Prefixed sampling** starts a solver at the discovered page associated with a task; **unprefixed sampling** starts it at the website's root. The term prefixed here concerns the trajectory's starting context, not a security filter or a textual instruction prefix.

**Supervised fine-tuning** trains a starting model on selected successful examples. Although Go-Browse borrows exploration ideas from reinforcement learning (RL), the evaluated Go-Browse-7B is trained with supervised fine-tuning, not an RL objective. A **vision-language model (VLM)** evaluates task completion during collection using textual evidence and a screenshot. Its judgments differ from the task-specific WebArena reward functions used for benchmark evaluation.

## 4. Research problem and gap

[A] The existing problem is insufficient understanding of deployment environments. An agent may possess general language competence yet lack the website-specific knowledge needed to locate and operate relevant pages. The introduction cites poor browser-task performance and argues that interaction training is necessary, p. 1.

[A] According to the authors, human-generated demonstrations are costly and time-consuming. Automatically generated demonstrations based on indirect tutorials may fail to transfer across websites. Direct interaction can provide more relevant data, but existing collection strategies still waste effort or miss important functionality.

[A] Interaction-first methods often restart independent episodes and rediscover easy pages, leading to repeated demonstrations. Instruction-first methods often propose tasks from a static starting observation, restricting their context and sometimes hallucinating operations that cannot actually be performed. Some approaches need human-provided context to compensate, p. 3.

[A] The research gap is a scalable collection method that combines **grounded task proposal, information reuse across episodes, local task coverage, and broader website coverage**. Go-Browse addresses it by maintaining a discovered-page graph and using agents themselves to gather task-proposal context.

Scope matters. The main collection experiment covers **five WebArena domains and 100 explicitly explored URLs**, not the entire open web. Online-Mind2Web supplies a separate generalization evaluation on live websites. There is no adversarial website construction, attacker-controlled content condition, standalone-LLM baseline, or explicit safety objective.

## 5. Research questions / objectives / hypotheses

[A] The paper presents objectives and claims rather than formal numbered research questions or hypotheses. Its central objective is to automatically collect diverse, realistic, useful web-agent demonstrations through structured exploration and use them to improve a smaller browser agent.

The following analytical register organizes those objectives without attributing invented question wording to the authors:

| Analytical objective | Evidence examined | Relevant experiment |
|---|---|---|
| O1: Improve a 7B browser agent with generated data | WebArena success rates | X1, Table 3 |
| O2: Assess transfer beyond collection environments | Online-Mind2Web success and domain breakdown | X2, X10 |
| O3: Reduce redundant task collection | Intent-cluster distributions | X3, Figure 4 |
| O4: Support deeper successful behavior | URL-depth distributions and visit counts | X4, Figure 5, Table 4 |
| O5: Help weaker models produce successful examples | Prefixed versus unprefixed sampling | X5, Figure 6 |
| O6: Improve collection efficiency and coverage | Filtered tasks and reset-count comparison | X6–X7, Table 5 |
| O7: Justify complementary explorer models | Proposal counts and clusters | X8, Tables 7–8 |
| O8: Establish collection cost and comparison uncertainty | Cost accounting and bootstrap analysis | X9, X11 |

[D] The user's separate question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis**, is not the paper's question. This work can support an architecture-based discussion of observations, actions, generated training data, and automated judgment. It cannot answer the comparative vulnerability claim directly. Confidence in this relevance inference is MEDIUM; confidence that the paper lacks such an experimental comparison is HIGH.

## 6. Assumptions / threat model

[A] The operational system assumes that browser observations and a supplied goal can guide useful actions; that discovered pages can be revisited; that URLs can identify graph nodes; and that attempted solutions plus a binary judge can identify feasible tasks. These are methodological dependencies visible in the algorithm, not a separately enumerated assumption theorem.

[A] Task feasibility is operationally defined by finding at least one judged-successful trajectory within a capped number of attempts. With a maximum of three tries, a rejected task may be genuinely impossible or simply unsolved by the selected agent within its budget. The paper does not distinguish those possibilities with independent ground truth, pp. 4–6.

[D] The components effectively relied upon for data quality include the task proposers, the strong feasibility-solving model, the VLM judge, browser execution, and the ability to restore or access discovered states. Their outputs influence what enters the training dataset. The paper does not specify a security trust hierarchy among user instructions, webpage text, model-generated tasks, action history, and execution output.

No explicit threat model is supplied. Attacker capabilities, attacker-controlled fields, confidentiality targets, unauthorized-action criteria, sandbox boundaries, exfiltration channels, malicious persistence, and security-specific controls are not evaluated. Consequently, listing browser operations identifies **capabilities to examine**, not vulnerabilities proven by this paper.

## 7. Methodology

### Study design and architecture

[A] Go-Browse constructs a graph G = (V, E). Each node is a unique URL and each edge is a trajectory between URLs. An outer loop selects discovered pages from a frontier. An inner loop proposes navigation and local tasks, checks their feasibility, and samples more trajectories for accepted tasks, pp. 3–5.

**NavExplorer** is an agent instructed to discover neighboring pages and propose useful navigation tasks. It can interact with the page and call an added function, add_tasks_to_dataset(tasks: tuple[str]), to record proposals. Its prompt prioritizes pages a typical user would visit and asks it to return after inspecting a new page, pp. 4, 13.

**PageExplorer** proposes concrete tasks associated with the current page. It may explore menus and controls rather than relying only on the initial observation. Its supplied prompt covers information seeking, navigation, and content modification and asks for specific entities rather than ambiguous requests such as modifying an unspecified current item, pp. 13–14.

**FeasibilityChecker** uses a strong agent to attempt proposed tasks and a VLM judge to evaluate them. It samples up to Nmax attempts, stops at a success, retains a task with at least one success, and discards the rest, p. 4. This both filters proposals and supplies an initial accepted trajectory.

**Solvers** collect additional trajectories for accepted tasks using cheaper models. Prefixed trajectories begin at the discovered page; unprefixed trajectories begin at the root. The former reduces the navigation burden; the latter preserves experience with navigation and longer task routes, pp. 4–5.

### Algorithm register

**ALG1, Interaction-first Exploration, p. 4:** initialize agent A, labeler L, and dataset D; repeat exploration from a website's initial state; label completed trajectories retrospectively; union their labeled records into D. Its characteristic feature is that concrete tasks are assigned after interaction.

**ALG2, Instruction-first Exploration, p. 4:** initialize proposer P, agent A, and reward R; propose task set G from initial state s0; solve each task; retain only pairs for which R(g, τ) = 1. The printed proposer call contains a dangling comma, so its missing argument is not inferred.

**ALG3, Go-Browse, p. 5:** initialize dataset, graph, frontier, and modules; add each website root; repeatedly remove a frontier node and get its state; combine navigation and local proposals; test each task; add accepted task/trajectory pairs and newly discovered nodes/edges; collect prefixed and unprefixed solver trajectories; continue until the frontier is empty. The experimental collection uses a 20-URL-per-domain budget, so the generic frontier-exhaustion pseudocode is broader than the actual reported collection budget. The supplied material does not fully specify the stopping implementation under that budget.

### Collection configuration

| Component or setting | Reported configuration | Source |
|---|---|---|
| Environments | Shopping Admin, Shopping, Reddit, GitLab, Map clones | pp. 5–6 |
| Explicitly explored URLs | 20 per domain; 100 total | pp. 5–6 |
| NavExplorer | Claude-3.7-Sonnet; up to 15 interaction steps | p. 6 |
| PageExplorer | GPT-4o up to 20 steps; Claude-3.7-Sonnet up to 10 | p. 6 |
| Feasibility-solving model | Claude-3.7-Sonnet | p. 6 |
| Feasibility attempts | At most 3 | p. 6 |
| Collection judge | GPT-4o-based VLM | p. 6 |
| Retained feasible tasks | Maximum 30 per URL | p. 6 |
| Additional solvers | GPT-4o-mini and Qwen-2.5-7B-Instruct | p. 6 |
| Solver horizon | Maximum 10 steps | p. 6 |
| Sampling modes | 2 prefixed and 2 unprefixed trajectories; allocation across solver models is not completely explicit | p. 6 |
| Collection temperature | 0.7 for interaction steps | p. 6 |
| Released observations | Accessibility tree, HTML, screenshots | p. 6 |
| Training observation | Accessibility tree only | p. 6 |

### Data, training, and evaluation

[A] Table 1 reports **9,504 successful trajectories, 17,245 failures, 26,749 total trajectories, and 3,422 unique tasks**. Successful trajectories contain 39,339 steps; failed trajectories contain 157,123 steps; total steps are 196,462. Only successful trajectories are used for the evaluated supervised training, while failures are reportedly released. The abstract's 10K trajectories and 40K steps are rounded descriptions of the successful subset, not the whole released collection.

[A] The base model is Qwen-2.5-7B-Instruct. A comparison model is trained on NNetNav-WA with the same training parameters. That baseline dataset is described as containing 45K interaction steps across the same five domains, p. 6. No train/validation partition, held-out generated-task partition, duplicate-removal procedure, or benchmark-task leakage audit is specified in the supplied text.

[A] Appendix C reports two training epochs, a maximum sequence length of 24K tokens, learning rate 2e-5, batch size 8 with one item per GPU, and four gradient-accumulation steps. It states training on the whole dataset, whereas §5 explicitly restricts training to successful trajectories; the likely reference is the selected training dataset, but that reconciliation is an interpretation rather than an explicit clarification.

Training uses one node with eight NVIDIA H100 GPUs, each with 80GB video memory, and takes approximately 40 hours per run. Generation uses five parallel SLURM cluster nodes, one per domain, each allocated 256GB RAM and eight CPUs, plus eight NVIDIA L40S GPUs for Qwen inference. Dataset generation takes approximately three weeks, p. 20. Optimizer type, learning-rate schedule, random seeds, software versions, and repeated training-run variability are not specified.

[A] WebArena evaluation covers 812 tasks, uses BrowserGym and task-specific benchmark reward functions, and sets model temperature to zero. Online-Mind2Web evaluation covers 300 tasks across 136 live websites. A paired bootstrap analysis draws 10,000 samples from WebArena outcomes; it does not substitute for repeated independent model-training runs, pp. 6, 16.

## 8. Experiments / analyses

| ID | Purpose and setup | Main result | Qualification |
|---|---|---|---|
| X1: WebArena evaluation | Compare trained and pretrained browser agents on 812 tasks, temperature 0 | Go-Browse-7B 21.7%; NNetNav-7B 18.8%; GPT-4o-mini 19.3%; base Qwen 8.3% | Stronger closed agents score 37.6% and 45.4%; small-baseline margins have qualified bootstrap support. |
| X2: Overall transfer | Evaluate on 300 Online-Mind2Web tasks across 136 websites | Go-Browse 5.33%; NNetNav 4.00%; GPT-4o-mini 9.33% | Go-Browse improves over the same-sized trained baseline but remains below GPT-4o-mini. |
| X3: Task diversity | Cluster generated tasks with GPT-4o-mini and compare sunburst distributions | Authors report smaller concentrations and more balanced domains for Go-Browse | No numerical entropy, uncertainty interval, or independent clustering validation is supplied. |
| X4: Successful navigation depth | Compare maximum URL path depth and successful-trajectory URL visits | Go-Browse-only successes show deeper behavior; selected deep URLs receive more visits | URL path depth differs from action distance and does not by itself prove longer action sequences. |
| X5: Starting-page sampling | Compare prefixed and root-start trajectories by graph node-depth bin | Prefixed sampling has higher success, with a larger visible advantage for Qwen at deep nodes | Figure 6 lacks exact point labels, sample counts, and error bars. |
| X6: Feasibility filtering | Account for tasks rejected before additional sampling | 403 rejected tasks; about 3.2K avoided rollouts and 29.4K steps; reported 13% step reduction | No independently measured false-rejection rate or detailed counterfactual calculation is provided. |
| X7: Outer-loop coverage | Hold proposed tasks at 30 per domain and vary reset/task allocation | 183, 214, 260 visited URLs for 1/30, 5/6, 15/2 | This is a separate coverage experiment, not the 100-URL main dataset budget. |
| X8: Proposal design | Compare proposer models and explorer types | Claude supplies more tasks; GPT-4o supplies more modification clusters; NavExplorer adds navigation tasks | Models have different step budgets, so this is not a fully matched budget comparison. |
| X9: Collection cost | Account for proposal/solver rollouts and GPT-4o evaluation | $754.66 rollouts + $220.91 evaluation = $975.57 | Table 9 includes broader activity than the released trajectory statistics; cost is not total hardware ownership or training cost. |
| X10: Transfer by similarity/difficulty | GPT-4o-mini labels websites as adjacent or truly out-of-domain; compare success and difficulty | Go-Browse is stronger on adjacent sites; NNetNav is stronger on truly OOD sites | Classification is model-generated; Figure 8 counts do not fully reconcile with Table 2. |
| X11: Statistical comparison | 10,000 paired bootstrap samples | p < 0.001 versus base Qwen; p = 0.094 versus NNetNav; p = 0.108 versus GPT-4o-mini | The latter two values do not establish significance at a 0.05 threshold. |

The distinct manipulations should not be conflated. Sampling mode changes a solver's starting point; the outer-loop test changes exploration allocation; proposer comparisons change model and step budget; transfer analyses change environment similarity. None is a security experiment.

## 9. Results

[A/B] Table 3 supports a clear improvement over the starting Qwen browser agent and the compared 7B fine-tuned baseline. It does not support the sentence in §5 that Go-Browse outperforms all other models in the table: GPT-4o and Claude-3.7-Sonnet are both higher overall. The claim is accurate only after restricting the comparison class appropriately.

[C] The displayed overall rate differences are **21.7 − 8.3 = 13.4 percentage points** versus base Qwen, **21.7 − 18.8 = 2.9 percentage points** versus NNetNav, and **21.7 − 19.3 = 2.4 percentage points** versus GPT-4o-mini. The source often describes these with a percent sign; the subtraction of success percentages yields percentage-point differences. These are not 13.4%, 2.9%, and 2.4% relative improvements.

[C] Domain differences versus NNetNav are Admin **25.3 − 14.3 = 11.0 points**, Shopping **22.4 − 20.3 = 2.1**, Reddit **30.7 − 23.7 = 7.0**, GitLab **15.3 − 19.9 = −4.6**, and Map **17.9 − 17.2 = 0.7**. GitLab is a substantive exception, not a minor omitted result. Go-Browse is also below GPT-4o-mini on GitLab, 15.3% versus 20.9%.

[A] On Online-Mind2Web, performance falls to 5.33%. [C] Its advantage over NNetNav is **5.33 − 4.00 = 1.33 points**, while its deficit to GPT-4o-mini is **9.33 − 5.33 = 4.00 points**. The domain breakdown shows Go-Browse at 5.3% on adjacent tasks and 4.9% on truly OOD tasks; NNetNav is 2.3% and 7.3%; GPT-4o-mini is 6.0% and 15.4%. Thus Go-Browse's overall lead over NNetNav is not uniform across environment types.

[A] The bootstrap results qualify the main performance narrative. The authors report statistically significant improvement over base Qwen, but only moderate confidence relative to NNetNav and GPT-4o-mini. [D] Under a 0.05 significance criterion, the reported p-values 0.094 and 0.108 would not meet that criterion. The paper does not explicitly select such a threshold, and no confidence interval is supplied.

The efficiency and mechanism findings are supportive but narrower than the benchmark result: more dispersed task clusters, deeper successful URL visits, higher prefixed-sampling success, and wider coverage with more reset nodes. These do not establish attack resistance, safe action execution, or reduced susceptibility to malicious webpage content.

## 10. Figure-by-figure interpretation

### Figure 1 — Go-Browse's two-loop collection process, p. 2

[B] This is a visually inspected architecture diagram. The left side shows successive outer-loop iterations over example pages: Dashboard, Products, Best Sellers, and Quest Lumaflex. Nodes and connecting routes accumulate; a discovered page is selected from the frontier; a later route can update an edge with a shorter path. The right side shows three numbered inner-loop stages: task proposal, feasibility checking, and trajectory sampling.

NavExplorer and PageExplorer both produce tasks grounded in interactions. The feasibility stage shows attempted action paths, rejected paths with red crosses, an accepted green path, and a VLM judge. The solver stage shows paths beginning at the selected page and paths beginning at the dashboard. Arrows returning to the outer loop represent discovery and frontier updates. Colors identify example paths and outcomes, not measured performance magnitudes. No quantitative axes, uncertainty bars, or experimental estimates are present. The diagram explains how local exploration feeds global coverage rather than serving as empirical proof of coverage.

### Figure 2 — Comparison of collection policies, p. 4

[B] Two side-by-side pseudocode blocks reproduce Algorithms 1 and 2. Interaction-first collection explores before assigning task labels. Instruction-first collection proposes tasks before executing them and filters solutions with a reward function. There are no plot axes, numerical performance bars, or uncertainty estimates. Its purpose is conceptual comparison; the loops and success condition are substantive and are represented in §7 above.

### Figure 3 — Successful-trajectory source composition, p. 6

[B] Three colored blocks label **Qwen-2.5-7B-Instruct 29.5%**, **GPT-4o-mini 36.6%**, and **Claude-3.7-Sonnet 33.9%**. These are proportions of successful trajectories in the generated dataset, not the models' success rates on attempted trajectories. [C] The labels sum to 100.0%. No model-specific successful counts, error bars, or denominator-specific attempt counts are given in the figure. Its interpretation is that successful data are not supplied almost exclusively by one model.

### Figure 4 — Task intent distributions, p. 7

[B] Two sunburst charts compare NNetNav-WA and Go-Browse-WA. Inner wedges encode the five website domains; outer wedges encode GPT-4o-mini-derived intent categories. Corresponding domain colors recur across the charts: GitLab blue, Shopping Admin coral, Shopping green, Map purple, and Reddit orange. The Go-Browse chart visibly distributes domain area more evenly and has many smaller category wedges; NNetNav has conspicuous larger concentrations.

[A] Nearby text interprets those concentrations as redundant exploration, particularly on difficult-to-navigate domains, and links domain balance to Table 3. [D] This is a descriptive association rather than a controlled causal demonstration that a particular intent distribution creates a particular benchmark gain. Exact category percentages and a numerical diversity statistic are not shown. Small radial labels are not all visually readable at the supplied resolution; extracted labels were inspected, but exhaustive label transcription is deliberately compressed. A loading/MathJax string in the extracted chart text is a rendering artifact, not a substantive result.

### Figure 5 — Maximum URL-depth distributions, p. 8

[B] Three density plots compare Go-Browse in blue with NNetNav in red: all trajectories, tasks on which only Go-Browse succeeds, and tasks on which only NNetNav succeeds. The horizontal axis is maximum URL depth reached; depth means the number of path segments. The vertical axis is density, not task success percentage. Horizontal ranges extend to about 14 in the first two panels and 9 in the third; vertical limits differ across panels, so heights cannot be directly compared as counts.

[B/A] The all-trajectory curves are similar. The Go-Browse-only-success panel has a more substantial blue tail at greater depths, supporting the authors' claim that deeper behavior contributes to some wins. The NNetNav-only-success panel lacks an equally clear distinct depth advantage for NNetNav. Dotted vertical markers appear, but their precise statistical identity is not specified clearly in the supplied caption; they are not assigned invented numerical meanings. No sample counts, exact mean depths, confidence bands, or hypothesis-test outputs are supplied. The authors' phrase no significant difference in behavior is not accompanied here by a reported significance test.

### Figure 6 — Prefixed versus unprefixed sampling, p. 8

[B] A line plot places graph node-depth bins **1–4, 5–8, 9–12, 13–16, 17–20** on the horizontal axis and success rate on the vertical axis. Blue denotes all models; red denotes Qwen. Solid lines indicate prefixed sampling; dashed lines indicate unprefixed sampling. Graph node depth is shortest trajectory length from the root, calculated with Dijkstra's algorithm, not the URL-path depth used in Figure 5.

[B] Solid lines generally lie above their corresponding dashed lines. The red dashed curve falls strongly in the deepest bin while the red solid curve remains much higher. This visually supports the claim that beginning at a useful page helps weaker solvers, especially for pages expensive to reach. Exact point values are not labeled and are not promoted to reported numbers. No confidence intervals, bin counts, or matching protocol details are visible; the figure is mechanism-oriented descriptive evidence.

### Figure 7 — Transfer by domain similarity, p. 17

[B] Grouped bars compare Go-Browse-7B, NNetNav-7B, and GPT-4o-mini. The vertical axis is success rate in percent, from 0 to 20. Teal encodes In-Domain-Adjacent (IDA); coral encodes Out-of-Distribution, called truly Out-of-Domain (OOD) in nearby text. Exact labels are **5.3/4.9**, **2.3/7.3**, and **6.0/15.4**, respectively.

The figure supports two qualifications: Go-Browse's transfer advantage over NNetNav is concentrated on adjacent environments, and GPT-4o-mini is much stronger on the classified OOD subset. It does not imply that greater semantic distance inherently makes a task easier; the authors point to difficulty composition as a possible explanation. Website labels are produced by GPT-4o-mini, and group sizes are not explicitly given with the figure. No error bars appear.

### Figure 8 — Successful task counts by difficulty and domain, p. 17

[B] Two grouped-bar panels show IDA and OOD results. The horizontal axis lists models; the vertical axis is **Number of Successes**, although the caption calls the figure a breakdown of success rates. Teal, yellow, and coral encode easy, medium, and hard tasks. The directly readable counts, ordered easy/medium/hard, are: IDA GPT-4o-mini **4/2/2**, Go-Browse **5/1/1**, NNetNav **2/1/0**; OOD GPT-4o-mini **16/2/1**, Go-Browse **4/2/0**, NNetNav **7/1/1**.

[C] NNetNav's OOD advantage is mostly easy-task successes: **7 − 4 = 3** additional easy successes, with one fewer medium and one additional hard success, for **9 − 6 = 3** additional total OOD successes. The figure does not provide difficulty denominators, so difficulty-specific success rates cannot be calculated.

[C] Total visible successes are Go-Browse **7 + 6 = 13**, NNetNav **3 + 9 = 12**, and GPT-4o-mini **8 + 19 = 27**. If these cover the same full 300 tasks as Table 2, their implied rates would be **4.33%, 4.00%, and 9.00%**, rather than Table 2's **5.33%, 4.00%, and 9.33%**. This mismatch is not resolved by the supplied work. An unreported subset or another difference could exist, but it is not assumed.

## 11. Table-by-table interpretation

### Table 1 — Generated dataset composition, p. 6

[B] Rows distinguish trajectories, interaction steps, and unique tasks; columns distinguish success, failure, and total. Trajectories are **9,504 / 17,245 / 26,749**; steps are **39,339 / 157,123 / 196,462**; unique tasks are **3,422**, without a success/failure split. [C] Both sums reconcile: 9,504 + 17,245 = 26,749 and 39,339 + 157,123 = 196,462. The table does not quantify licensing of Go-Browse-WA, split sizes, duplicate rates, or judge accuracy.

### Table 2 — Overall Online-Mind2Web performance, p. 6

[B] Rows are NNetNav-7B **4.00%**, Go-Browse-7B **5.33%**, and GPT-4o-mini **9.33%**. Success rate is the metric. GPT-4o-mini is best and NNetNav lowest among these three. No uncertainty interval or statistical comparison appears. The associated evaluation is 300 tasks on 136 live websites; the displayed precision should not be interpreted as uncertainty precision.

### Table 3 — WebArena benchmark results, p. 7

| Model | Overall % | Admin % | Shopping % | Reddit % | GitLab % | Map % |
|---|---:|---:|---:|---:|---:|---:|
| GPT-4o-mini | 19.3 | 19.2 | 19.3 | 21.1 | 20.9 | 15.6 |
| GPT-4o | 37.6 | 35.7 | 32.3 | 50.9 | 36.7 | 37.5 |
| Claude-3.7-Sonnet | 45.4 | 37.4 | 37.0 | 58.8 | 52.0 | 47.7 |
| Qwen-2.5-7B-Instruct | 8.3 | 7.1 | 9.4 | 7.9 | 8.7 | 7.8 |
| NNetNav-7B | 18.8 | 14.3 | 20.3 | 23.7 | 19.9 | 17.2 |
| Go-Browse-7B | 21.7 | 25.3 | 22.4 | 30.7 | 15.3 | 17.9 |

[B] Closed models and open-weight 7B models form separate categories. Claude is best across all displayed columns among all models. Go-Browse is best within the open-weight group except on GitLab, where NNetNav is best. Bold formatting marks category bests rather than asserting Go-Browse wins against every model. No ties or per-domain confidence intervals are supplied. This table is the strongest source for precise benchmark comparisons.

### Table 4 — Selected differences in successful-trajectory visits, p. 8

[B] Columns give URL pattern, Go-Browse visits, NNetNav visits, difference, and depth. Go-Browse-favored examples are product editing **10/1, difference 9, depth 5**; Reddit search **7/0, difference 7, depth 2**; configurable product editing **5/0, difference 5, depth 12**; order viewing **6/2, difference 4, depth 6**; and biography editing **5/0, difference 5, depth 3**.

NNetNav-favored examples are new projects **2/6, difference 4, depth 2**; blank new projects **2/5, difference 3, depth 2**; commit history **2/5, difference 3, depth 5**; forks **1/4, difference 3, depth 5**; and Reddit by-submissions pages **0/3, difference 3, depth 3**. The difference column is the positive advantage of the designated model, not one consistently signed GB-minus-NN value. URL placeholders and unusual repeated separators are preserved as source patterns, not repaired into tested URLs. These selected rows illustrate behavior and are not a census of all visited URLs.

### Table 5 — Reset allocation and website coverage, p. 9

[B] At 30 proposed tasks per domain, reset/task allocations **1/30**, **5/6**, and **15/2** produce **183**, **214**, and **260** unique visited URLs across five domains. [C] The highest-reset condition exceeds the lowest by **260 − 183 = 77 URLs**. This supports broader coverage under the tested allocation, not universal optimality of increasing resets. There are no repetition counts, uncertainty bars, or downstream training results for each allocation.

### Table 6 — Browser action space, p. 12

[B] Fifteen actions cover waiting, element interaction, navigation, tab management, and communication: noop(wait_ms), click(elem), hover(elem), fill(elem, value), keyboard_press(key_comb), scroll(x, y), select_option(elem, options), goto(url), go_back(), go_forward(), new_tab(), tab_close(), tab_focus(index), send_msg_to_user(text), and report_infeasible(reason).

This is a capability table, not a performance or security table. The distinction matters for the user's question: content modification and browser navigation are available operations, but the table does not establish their permission scope, resistance to misuse, or associated attacker access. Main-text illustrative function names differ from the appendix's concrete names; the appendix provides the more explicit implementation-facing list.

### Table 7 — PageExplorer model comparison, p. 15

[B] GPT-4o proposes **274 navigation, 227 information, and 243 modification tasks**, with **24, 18, and 34 clusters**, using at most **20 steps per node**. Claude proposes **415, 508, and 516 tasks**, with **23, 19, and 19 clusters**, using at most **10 steps**. Claude generates more tasks in every category; GPT-4o produces substantially more modification clusters. Information-cluster counts slightly favor Claude, 19 versus 18, so GPT-4o's diversity advantage should not be generalized to every raw cluster count.

[C] Totals are GPT-4o **274 + 227 + 243 = 744** and Claude **415 + 508 + 516 = 1,439**, a ratio of **1,439 / 744 ≈ 1.93**. This supports the authors' almost-double wording. Different budgets, unspecified uncertainty, and model-based clustering limit causal interpretation.

### Table 8 — Navigation task contribution by explorer, p. 15

[B] NavExplorer contributes **925 navigation tasks and 32 clusters**; PageExplorer contributes **689 tasks and 31 clusters**. [C] If these counts are additive in the manner implied by the text, the combined count is **925 + 689 = 1,614**, or **1,614 / 689 ≈ 2.34 times** the PageExplorer-only count. The supplied table does not explicitly establish unique-task deduplication across those sources, so the calculation is conditional on that additive interpretation.

### Table 9 — Collection cost, p. 16

| Rollout model | Trajectories | Steps | Average dollars/step | Total dollars |
|---|---:|---:|---:|---:|
| GPT-4o-mini | 11,695 | 95,314 | 0.0008 | 76.25 |
| Qwen-2.5-7B-Instruct | 10,203 | 79,209 | 0.0025 | 198.02 |
| Claude-3.7-Sonnet | 5,102 | 24,532 | 0.0190 | 466.11 |
| GPT-4o | 103 | 789 | 0.0181 | 14.28 |
| Total rollouts | 27,103 | 199,844 | 0.0037 | 754.66 |

[B] Panel B adds **11,105 GPT-4o trajectory evaluations**, at average **$0.0199**, totaling **$220.91**. The grand total is **$975.57**. Average unit costs are rounded; multiplying those rounded averages need not reproduce exact totals. [A] Approximately 53% of input tokens are cache reads, and Qwen API cost is estimated using Together AI pricing. These are collection accounting assumptions, not current independently checked prices.

[C] Table 9 exceeds Table 1 by **27,103 − 26,749 = 354 trajectories** and **199,844 − 196,462 = 3,382 steps**. Its caption/prose says rollouts include task proposal as well as collection, offering a scope distinction, but no exact reconciliation of the excess is provided. Hardware and fine-tuning expenditures are not fully included in this API-oriented total.

### Table 10 — Paired bootstrap comparisons, p. 16

[B] Each row compares a baseline against Go-Browse across 10,000 bootstrap samples. Baseline/tie/Go-Browse win ratios are Claude **1.000/0.000/0.000**, GPT-4o **1.000/0.000/0.000**, GPT-4o-mini **0.085/0.024/0.892**, NNetNav **0.076/0.018/0.906**, and base Qwen **0.000/0.000/1.000**. Reported p-values are **0.000, 0.000, 0.108, 0.094, 0.000**, respectively.

The table's rounded 0.000 values do not imply mathematically zero probabilities. The prose explicitly gives p < 0.001 for the Qwen comparison. The GPT-4o-mini row's ratios sum to 1.001 because of displayed rounding. The winner column identifies favored models, not automatic proof of significance at an unspecified threshold. No intervals or multiple-comparison procedure are reported.

### Table 11 — Transfer examples, pp. 17–19

[A/B] Rows show model, domain category, success/failure, difficulty E/M/H, website, and task. The beginning is visually inspected; the continuation is text-only. The table contains **35 illustrative rows**: 11 Go-Browse examples and 12 each for NNetNav and GPT-4o-mini, counted from the supplied text [C]. They are selected examples, not an exhaustive results table or a balanced sample.

Go-Browse examples include successful Brooklyn-map navigation, a game walkthrough, a constrained vitamin search, currency-history retrieval, and a drug-interaction report; failures include review filtering, music-profile navigation, constrained housing search, baggage information, job search, and dermatologist filtering. NNetNav examples span recipes, walkthroughs, project-like searches, finance, jobs, retirement calculation, pet search, and health information. GPT-4o-mini examples span event tips, device specifications, game content, housing, postal services, travel accommodation, products, academic jobs, finance calculations, a service search, a charting request, and visa information.

The medical, financial, and legal phrases are benchmark task descriptions, not advice endorsed here. Task numbers such as ages, contribution amounts, distances, price caps, and dates are illustrative query constraints and are deliberately compressed. The table demonstrates diversity of transfer tasks and counterexamples to uniform model superiority; it does not reveal why a failed trajectory failed or whether any failure was adversarial.

## 12. Diagram / architecture interpretation

[A/B] Figure 1 and Algorithm 3 jointly establish the control flow. Input consists of a website root and a set of collection modules. The root enters the graph and frontier. Selecting a frontier node supplies its browser state to both task proposers. Proposed tasks feed the feasibility stage, which attempts execution and calls the reward judge. Accepted tasks feed additional solvers; successful exploration supplies newly discovered pages and routes to the graph. The graph then determines later exploration starting points.

The important feedback loop is **discovery → remembered page → reset → further local exploration → additional discovery**. It prevents every episode from depending on rediscovery from the homepage. Prefixed and unprefixed solver paths share a task but differ in initial state. Dataset output includes task/trajectory examples, while graph/frontier state supports the collection process itself.

[A] The judge receives a user intent, action history, final accessibility-tree text, screenshot, and, in the prompt introduction, the agent's response. Information-seeking success depends on the response containing requested information or stating its unavailability, with checks on action sufficiency. Navigation and content-modification success instead depend on actions and final page state, pp. 14–15. The displayed final placeholder block does not separately show an agent-response placeholder, leaving the precise implementation input assembly incompletely specified.

[D] For security research, this architecture separates several boundaries worth investigating: page observations entering the agent, proposed tasks entering the solver, model outputs entering an execution program, observed state entering a judge, and judged trajectories entering training. The paper documents those pathways but does not test whether hostile content can cross them improperly.

## 13. Equations and mathematical concepts

**E1 — State/action transition, pp. 2–3.** At timestep t, the model observes s_t, produces a_t, and execution yields s_(t+1). This is a procedural state transition, not a supplied probabilistic transition equation. State includes goal g, page-tree text, action-space description, history, and errors. The action contains reasoning plus a browser function call. The paper does not define a complete mathematical state space or transition distribution.

**E2 — Trajectory, p. 3.** The paper writes τ = {s1, a1, s2, a2, …, sT, aT}. Although braces are used, prose defines an ordered sequence of states and actions. T is the horizon, or the final step at termination. Another trajectory expression starts at index zero; this indexing difference does not change the stated sequence concept. Termination occurs at the maximum horizon or a terminal action. The method uses trajectories as demonstration units and as evidence for success judgment.

**E3 — Binary reward, p. 3.** R(g, τ) ∈ {0, 1}. Inputs are task g and trajectory τ. Output 1 means the task was successfully completed; 0 means failure. During collection this is implemented with a GPT-4o-based VLM judge; WebArena benchmarking instead uses task-specific reward functions. The expression defines a label, not a learned reward-training objective or a calibrated confidence probability.

**E4 — Task proposals and successful-pair filtering, pp. 3–5.** A proposer generates a set of tasks G = {g1, …, gK}; instruction-first collection retains pairs (g_i, τ_i) satisfying R(g_i, τ_i) = 1. Go-Browse combines navigation and local task sets by union and forms a feasible set after attempted solutions. D is the dataset; ∪ is set union. The symbol G is reused for both a task set and the website graph in different contexts, so its meaning must be read locally.

**E5 — Website graph and frontier, pp. 4–5.** G = (V, E), where V consists of unique URLs and E represents trajectories between them. F is the frontier of discovered but not fully explored nodes. Algorithm 3 adds new nodes and edges after feasible exploration and removes a selected node before exploring it. Figure 1 shows shorter-path edge updates. The exact URL normalization policy, edge weighting, tie-breaking frontier policy, and complete browser-state restoration semantics are not supplied.

[A] Figure 6 defines node depth through a shortest trajectory from the root using Dijkstra's algorithm. Figure 5 instead defines depth by URL path-segment count. [D] These are different proxies for navigation difficulty; replacing one with the other would change the meaning of the evidence. No formal loss equation, theorem, proof, security bound, or optimization derivation is present in the supplied paper. Such mathematical detail is not invented.

## 14. Interpretation and discussion

[A] The authors interpret structured reset-and-explore collection as a way to reduce redundancy, increase page coverage, and gather better training examples from weaker models. The benchmark results support improvement over the starting model, and the analyses provide plausible mechanisms: discovered difficult pages remain available for later exploration; local starts remove navigation barriers; complementary proposers broaden task collection.

[D] The evidence does not isolate every mechanism's contribution to the final 21.7% score. Figure 6 tests sampling behavior, and Table 5 tests visited-page coverage, but neither supplies a complete matched-budget downstream-training ablation for every module. Task variety and domain-specific success are associated rather than experimentally proven to be causally linked.

### Source consistency checks

1. **Trajectory counts:** Table 1 and p. 2 report approximately 17K failures, with the exact table value 17,245. The conclusion on p. 9 and its continuation on p. 10 instead call them **39K unsuccessful trajectories**. The value 39,339 belongs to successful interaction steps in Table 1. A likely mix-up is conceivable, but the document does not resolve it; both claims are reported as inconsistent.
2. **Best-model scope:** §5 on p. 6 says Go-Browse outperforms the other models in the table. Table 3 shows GPT-4o and Claude higher. The valid restricted claim concerns the compared 7B models and GPT-4o-mini.
3. **Figure 8 metric:** The caption says success rates; the vertical axis and labels show counts. Without task denominators by difficulty, rates cannot be reconstructed.
4. **Transfer totals:** Visible Figure 8 counts imply 13/12/27 successes, while Table 2 on 300 tasks corresponds approximately to 16/12/28. The Go-Browse and GPT-4o-mini totals are unresolved.
5. **Collection-accounting scope:** Table 9 counts more rollouts and steps than Table 1. Broader proposal-inclusive accounting is stated, but a detailed mapping is absent.
6. **PageExplorer scope:** p. 13 asks for tasks on the current page without navigating to other URLs, while p. 14 explicitly includes navigation tasks. Tables 7–8 confirm navigation proposals from PageExplorer. The intended balance between local restriction and navigation collection is not fully explicit.
7. **Implementation naming:** Main text uses illustrative names such as type(text) and send_msg_to_usr(msg), while Table 6 lists fill(elem, value) and send_msg_to_user(text). These are reported differences, not assumed interoperable function signatures.
8. **Training scope:** Appendix C's whole-dataset wording must be interpreted alongside §5's success-only statement; all released failures should not be assumed to have been trained on.

[D] Security relevance remains indirect. The action history, webpage tree, final-state image, proposed tasks, and generated execution code illustrate where information and authority interact. The supplied work does not show malicious manipulation, prompt-injection examples, leakage, unauthorized purchases, compromised browser state, or adversarial training contamination. Its low task-success rates measure capability shortcomings, not vulnerability rates.

## 15. Contributions and novelty

[A] **Conceptual contribution:** Treat website exploration as information-reusing graph search rather than isolated episodes.

[A] **Algorithmic contribution:** Couple an outer discovered-page frontier with an inner propose-check-sample loop, using agent-based task proposal and both local-start and root-start trajectories.

[A] **Methodological contribution:** Use strong models to establish feasible tasks while permitting weaker or cheaper models to produce additional training examples.

[A] **Dataset contribution:** Release Go-Browse-WA with successful and failed trajectories and multiple observation representations. The precise table-supported size is 26,749 trajectories, 196,462 steps, and 3,422 unique tasks.

[A] **Implementation contribution:** Release code, dataset, models, and reproduction documentation. Availability is author-reported, not independently checked.

[A] **Empirical contribution:** Improve the evaluated 7B model to 21.7% WebArena success and analyze diversity, navigation, collection efficiency, proposal design, and transfer.

There is no new benchmark introduced: WebArena and Online-Mind2Web are reused. There is no theoretical security guarantee, new attack, defense evaluation, or comparative vulnerability result. The state-of-the-art language is the authors' positioning within the supplied work and is not independently validated against outside literature.

## 16. Limitations

### Authors' stated limitations

[A] Collection is limited to five WebArena domains; broader website collection could create larger datasets, pp. 9–10. The evaluated model is 7B and trains only on successful trajectories; incorporating failures through alternative objectives, including RL, and scaling model size are proposed avenues. The failure quantity accompanying that discussion is inconsistent with Table 1 and must not be repeated as settled data.

[A] Model- and prompt-originated biases can propagate into collected data and agent behavior. The authors explicitly call for auditing and mitigation before deployment, p. 10. This is a bias acknowledgment, not an experimental demonstration of a security exploit.

### Additional evidence-based analyst observations

[D] Success filtering can select easier or more model-preferred tasks, because unsolved proposals are discarded after a small attempt budget. A task rejected by the checker is not independently shown to be impossible. VLM evaluation accuracy and agreement with human labels are not supplied.

[D] Graph nodes use URLs, which may not uniquely encode all meaningful browser state. The document does not clarify how authentication, dynamic state, form contents, or state-changing operations affect restoration and graph identity. This is an implementation uncertainty, not proof of a failure.

[D] The baseline has the same stated training settings, but generated-data properties differ, including reported step counts and domain balance. Stronger models contribute to generating and filtering Go-Browse data. Thus the results do not establish that graph structure alone produces the full gain.

[D] Statistical support is strong against base Qwen but weaker for the small margins over NNetNav and GPT-4o-mini. Exact plot data, error bars, repeated-run variation, leakage checks, and several implementation details are absent. Truly OOD performance is weaker than NNetNav's in the reported breakdown. No security measurements support the user's comparative vulnerability premise.

## 17. Threats to validity

The following validity categories are **analyst observations**, not headings or admissions attributed to the authors.

**Internal validity:** The final trained-agent comparison combines graph exploration, new proposer behavior, strong-model filtering, mixed solvers, and sampling modes. The supplied analyses illuminate components but do not isolate every component's causal contribution under identical total budgets.

**Construct validity:** VLM-assigned task success may differ from actual completion. Intent clusters are model-generated proxies for diversity. URL-path depth and shortest-trajectory depth are different proxies for navigation complexity. Visited-URL counts are a coverage proxy, not direct measures of functional coverage or safety.

**Statistical conclusion validity:** Small benchmark improvements have p-values 0.094 and 0.108. No intervals or repeated-training uncertainty are given. Several plots omit sample counts and uncertainty. Apparent differences in aggregate proportions should not be overstated.

**External validity and generalizability:** Most training comes from five self-hosted website clones. The live-site evaluation shows much lower success and a reversal between Go-Browse and NNetNav on truly OOD sites. Website similarity is classified by another LLM, and task composition can confound the comparison.

**Ecological validity:** Live tasks are more varied than controlled clones, but no production deployment, adversarial web content, permission enforcement, or actual user harm is measured. A browser task succeeding is not equivalent to the agent behaving securely in a hostile environment.

**Reproducibility:** The paper supplies substantial budgets, prompts, hardware, and an artifact link, but the linked artifacts were not supplied or checked. Missing seeds, software versions, optimizer details, state-restoration details, and inconsistent counts limit a document-only reproduction assessment. Figure 8/Table 2 disagreement further limits precise reconstruction of transfer outcomes.

## 18. Future work and open questions

### A. Future work explicitly proposed by the authors

[A] Collect from more websites; expand the dataset; use unsuccessful trajectories through alternative training objectives such as RL; train larger models; audit and mitigate model/prompt biases before deployment, pp. 9–10. The authors' unsuccessful-trajectory number is disputed internally and is not adopted here.

### B. Additional questions logically remaining

[D] What fraction of rejected tasks are actually feasible? How accurate is the collection judge? Does each module improve downstream performance under a fixed total generation budget? How much benefit comes from task-domain balance versus graph resets? How are duplicate URLs, dynamic states, and mutation rollback handled? Are benchmark task overlap and generated-data leakage excluded? What explains the transfer-count inconsistency?

[D] Security questions motivated by the architecture include whether webpage text can alter an agent's intended task, whether executable action outputs receive independent authorization checks, whether hostile final states can mislead the judge, and whether misleading accepted trajectories can affect later training. These are **proposed research questions**, not findings. Answering whether web agents are more vulnerable than standalone LLMs would require matched adversarial conditions, defined assets and attacker control, and security outcomes for both system types. This paper supplies neither that comparison nor those measurements.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this work |
|---|---|
| LLM | Large language model; the component choosing or proposing actions and tasks. |
| VLM | Vision-language model; the collection judge can use text and a screenshot. |
| GUI | Graphical user interface; the browser interface through which tasks are performed. |
| ICLR | International Conference on Learning Representations; venue named on the paper. |
| CMS | Content management system; the label attached to Shopping Admin. |
| RL | Reinforcement learning; an inspiration for exploration and a proposed future training direction. |
| ReAct | Cited reasoning-and-acting interaction pattern used for browser agents. |
| BrowserGym | Python infrastructure used to implement and evaluate browser agents. |
| WebArena | Five-domain self-hosted browser-task environment and evaluation benchmark. |
| OM2W | Online-Mind2Web, a live-website transfer benchmark. |
| IDA | In-Domain-Adjacent; tasks/websites judged similar to WebArena. |
| OOD | Out-of-Domain or Out-of-Distribution; more distant transfer category. |
| SR | Success rate; percentage of evaluated tasks completed successfully. |
| HTML | Hypertext Markup Language; one released page-observation representation, not used for the reported fine-tuning. |
| Accessibility tree | Structured webpage representation flattened into model-readable text. |
| Trajectory τ | Ordered observations and actions from a task attempt. |
| g | Task or goal. |
| s_t | Observation/state supplied at step t. |
| a_t | Model-produced action at step t. |
| T | Maximum trajectory horizon or terminal sequence length in context. |
| R(g, τ) | Binary success label for task g and trajectory τ. |
| A, P, L | Agent, task proposer, and retrospective labeler in comparison algorithms. |
| D | Collected dataset. |
| G = (V, E) | Website graph with URL nodes and trajectory edges. |
| G = {g1, …, gK} | Task proposal set; G has a separate meaning here. |
| F | Frontier of pages awaiting fuller exploration. |
| Nmax | Maximum feasibility-solving attempts. |
| Prefixed sampling | Begin solving at the discovered task-associated page. |
| Unprefixed sampling | Begin solving at the website root. |
| Intent cluster | LLM-derived grouping of tasks by higher-level purpose. |
| Paired bootstrap | Resampling matched task outcomes to assess comparative uncertainty. |
| Temperature | Model-generation sampling setting; 0.7 for collection and 0 for WebArena evaluation. |
| 7B | Approximately seven billion model parameters, as described by the paper. |
| VRAM | GPU video memory; 80GB per reported H100. |
| SLURM | Named cluster scheduling environment; its detailed operation is not explained in the paper. |

## 20. Key numerical results

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| Collection domains | 5 | domains | WebArena clones | Author-reported | pp. 5–6 |
| Explicit page budget | 20 per domain; 100 total | URLs | Main collection | Author-reported | pp. 5–6 |
| Successful trajectories | 9,504 | trajectories | Released dataset composition | Visually readable | p. 6, T1 |
| Failed trajectories | 17,245 | trajectories | Table-supported count | Visually readable | p. 6, T1 |
| Total trajectories | 26,749 | trajectories | Dataset composition | Visually readable | p. 6, T1 |
| Successful steps | 39,339 | steps | Fine-tuning source subset | Visually readable | p. 6, T1 |
| Failed steps | 157,123 | steps | Released failures | Visually readable | p. 6, T1 |
| Total steps | 196,462 | steps | Dataset composition | Visually readable | p. 6, T1 |
| Unique tasks | 3,422 | tasks | Generated dataset | Visually readable | p. 6, T1 |
| Disputed failure count | 39K | trajectories | Conclusion contradicts T1 | Author-reported, inconsistent | pp. 9–10 |
| WebArena tasks | 812 | tasks | Main evaluation | Author-reported | p. 6 |
| Go-Browse success | 21.7 | percent | WebArena | Visually readable | p. 7, T3 |
| NNetNav success | 18.8 | percent | WebArena | Visually readable | p. 7, T3 |
| GPT-4o-mini success | 19.3 | percent | WebArena | Visually readable | p. 7, T3 |
| Base Qwen success | 8.3 | percent | WebArena | Visually readable | p. 7, T3 |
| Claude success | 45.4 | percent | WebArena | Visually readable | p. 7, T3 |
| Gain over NNetNav | 21.7 − 18.8 = 2.9 | percentage points | Displayed rates | Analyst-derived | p. 7, T3 |
| Gain over GPT-4o-mini | 21.7 − 19.3 = 2.4 | percentage points | Displayed rates | Analyst-derived | p. 7, T3 |
| Gain over base Qwen | 21.7 − 8.3 = 13.4 | percentage points | Displayed rates | Analyst-derived | p. 7, T3 |
| Transfer evaluation | 300 tasks; 136 sites | tasks/sites | Online-Mind2Web | Author-reported | p. 6 |
| Go-Browse transfer success | 5.33 | percent | Overall OM2W | Visually readable | p. 6, T2 |
| NNetNav transfer success | 4.00 | percent | Overall OM2W | Visually readable | p. 6, T2 |
| GPT-4o-mini transfer success | 9.33 | percent | Overall OM2W | Visually readable | p. 6, T2 |
| Go-Browse adjacent/OOD | 5.3 / 4.9 | percent | Model-classified subsets | Visually readable | p. 17, F7 |
| NNetNav adjacent/OOD | 2.3 / 7.3 | percent | Model-classified subsets | Visually readable | p. 17, F7 |
| Filtered proposals | 403 | tasks | Feasibility stage | Author-reported | p. 9 |
| Avoided rollouts/steps | 3.2K / approximately 29.4K | rollouts/steps | Filtering accounting | Author-reported | p. 9 |
| Step reduction | 13 | percent | Same positive-data amount, as reported | Author-reported | p. 9 |
| Coverage by resets | 183 / 214 / 260 | visited URLs | 1/30, 5/6, 15/2 allocations | Visually readable | p. 9, T5 |
| Collection expense | 975.57 | dollars | Rollouts plus evaluation | Visually readable | p. 16, T9 |
| Bootstrap samples | 10,000 | samples | Paired WebArena comparison | Author-reported | p. 16 |
| p versus NNetNav | 0.094 | p-value | Paired bootstrap | Visually readable | p. 16, T10 |
| p versus GPT-4o-mini | 0.108 | p-value | Paired bootstrap | Visually readable | p. 16, T10 |
| p versus base Qwen | <0.001 | p-value | Prose representation | Author-reported | p. 16 |
| Training epochs | 2 | epochs | Fine-tuning | Author-reported | p. 20 |
| Sequence limit | 24K | tokens | Fine-tuning | Author-reported | p. 20 |
| Learning rate | 2e-5 | learning-rate value | Fine-tuning | Author-reported | p. 20 |
| Batch / accumulation | 8 / 4 | items/steps | One item per GPU | Author-reported | p. 20 |
| Training time | approximately 40 | hours/run | Eight H100 GPUs | Author-reported | p. 20 |
| Generation duration | approximately 3 | weeks | Five parallel domain nodes | Author-reported | p. 20 |

No approximate graphical point estimates are inserted into this numerical table. Figure 6 supports trends, but exact points are not labeled. Contextual introduction numbers—human 78%, frontier scores rounded to 38% and 19%, small-model 8%, Computer-Using Agent 58%, and prior collection-method comparison 16% versus 6%—are author-reported motivation on p. 1, not new controlled experiments in this paper. They are deliberately compressed here and should not be substituted for Table 3's precise evaluated rates.

## 21. Claim–evidence map

| Claim | Evidence | Figure/table/experiment | Source | Qualification / evidence strength |
|---|---|---|---|---|
| Structured exploration reuses discoveries | Graph, frontier, and reset loop | F1, ALG3 | pp. 2–5 | HIGH for method specification; efficiency benefit has separate evidence. |
| Task proposals are grounded through interaction | Agent-based NavExplorer/PageExplorer and prompt templates | ALG3, A2 | pp. 4, 13–14 | HIGH for intended method; grounding accuracy is not independently measured. |
| Strong-model checking filters proposals | Up to three attempts and GPT-4o VLM judgment | X6 | pp. 4, 6, 9 | HIGH for configuration; true infeasibility is not established. |
| Generated data improve a 7B browser agent | 21.7% versus 8.3% and 18.8% | T3, X1 | pp. 6–7 | HIGH for displayed rates; causality of individual modules is narrower. |
| Go-Browse exceeds GPT-4o-mini on WebArena | 21.7% versus 19.3% | T3, T10 | pp. 7, 16 | HIGH for point estimates; p = 0.108 limits significance claims. |
| Go-Browse is not the strongest listed agent | Claude 45.4%, GPT-4o 37.6% | T3 | p. 7 | HIGH; directly qualifies broad best-model wording. |
| Prefixed starts help weaker solvers | Solid/dashed separation, particularly deep Qwen bins | F6, X5 | p. 8 | MEDIUM for explanatory interpretation; exact values and uncertainty absent. |
| More resets broaden visited-page coverage | 183 → 214 → 260 under fixed task count | T5, X7 | p. 9 | HIGH for reported experiment; no universal optimality claim. |
| Transfer advantage depends on similarity | Go-Browse leads on IDA; NNetNav leads on OOD | F7–F8, X10 | pp. 16–17 | HIGH for labeled rates; classification and count inconsistencies qualify interpretation. |
| Model/prompt biases can propagate | Explicit deployment caution | S8 | p. 10 | HIGH as author acknowledgment; no quantified bias or security exploit. |
| Browser agents expose observation/action pathways relevant to security | Tree inputs, executable calls, content modification, judge inputs | A1–A2 | pp. 3, 12–15 | MEDIUM analyst inference; vulnerabilities were not tested. |
| Comparative vulnerability remains unanswered | No adversarial experiment or standalone-LLM comparator in inventory | Whole supplied document | pp. 1–20 | HIGH for paper-scope finding; UNKNOWN for actual comparative vulnerability. |

## 22. Very simple explanation — Explain Like I'm 15

Imagine teaching a computer assistant to use a large shopping website. It might know what buying something means but keep getting lost before reaching the right screen. If every practice session starts at the homepage, it wastes time rediscovering the same easy places.

Go-Browse makes a map of pages it has already found. It returns to a useful page, invents realistic practice tasks after checking what is actually there, tests whether those tasks can be completed, and collects more attempts. Some attempts start directly on the useful page; others start at the homepage so the assistant still practices finding its way.

The resulting training helped a smaller browser agent complete about 22 out of every 100 WebArena tasks, compared with about 19 for the closest compared trained baseline and about 8 for its starting model. Bigger agents were still better, and performance on unfamiliar live websites was much lower. Some reported numbers also disagree, so the results need those qualifications.

For security, the useful lesson is that a browser agent does more than produce text: it reads pages, chooses actions, and changes a website. Those pathways deserve security testing. This paper shows how those pathways work, but it does not test malicious pages or show that browser agents are more vulnerable than ordinary chat models.

## Completeness Audit

The audit distinguishes full substantive representation from compressed treatment. It does not infer completeness from response length.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| FRONT: title/authors/abstract | Yes, text and visual | Yes | Fully represented | Venue, central claims, rounded data descriptions included. |
| S1 Introduction | Yes, text and visual | Yes | Represented in compressed form | Motivation and prior-performance examples retained; repetitive comparisons compressed. |
| S2.1 Agent definition | Yes, text and visual | Yes | Fully represented | State, action, history, trajectory, reward, implementation included. |
| S2.2 Interaction-first | Yes, text and visual | Yes | Fully represented | Benefits, redundancy, retrospective labeling, ALG1 included. |
| S2.2 Instruction-first | Yes, text and visual | Yes | Fully represented | Proposal, execution, reward filtering, static-context limits included. |
| S3 Graph/frontier | Yes, text and visual | Yes | Fully represented | URL nodes, trajectory edges, two loops, stopping uncertainty included. |
| S3 NavExplorer | Yes | Yes | Fully represented | Grounding, navigation proposals, added recording action included. |
| S3 PageExplorer | Yes | Yes | Fully represented | Local task proposal and navigation-scope inconsistency included. |
| S3 FeasibilityChecker | Yes | Yes | Fully represented | Strong solver, capped attempts, judge, filtering caveat included. |
| S3 Solvers | Yes | Yes | Fully represented | Prefixed/unprefixed modes and budgets included. |
| S4 Collection | Yes, text and visual | Yes | Fully represented | Domains, counts, models, temperatures, horizons, representations included. |
| S5 Training/evaluation | Yes, text and visual | Yes | Fully represented | Success-only training, baseline, two benchmarks, reward distinction included. |
| S6 Diversity | Yes, text and visual | Yes | Fully represented | Clustering and domain balance with descriptive limits. |
| S6 Depth | Yes, text and visual | Yes | Fully represented | Both depth definitions and selected URL visits distinguished. |
| S6 Prefixed sampling | Yes, text and visual | Yes | Fully represented | Trend included; unlabeled point values withheld. |
| S6 Filtering efficiency | Yes, text and visual | Yes | Fully represented | 403 tasks, avoided rollouts/steps, 13% claim qualified. |
| S6 Reset coverage | Yes, text and visual | Yes | Fully represented | Fixed-task experiment and all three results included. |
| S7 Related Work | Yes, text and visual | Yes | Represented in compressed form | Three categories and author positioning included; bibliography not independently verified. |
| S8 Conclusions/limitations | Yes; p. 10 text-only | Yes | Fully represented | Explicit limitations, future directions, bias caution, count contradiction included. |
| REPRO | Yes, text-only | Yes | Fully represented | Artifact availability reported without inspection. |
| ACK-REF | Yes; mixed visual/text | Yes | Represented in compressed form | Compute support and funding acknowledged; reference entries are not individually summarized. |
| Formal research questions | Entire supplied text checked | Yes | Fully represented as absent | Informal objectives organized without inventing author questions. |
| Formal hypotheses | Entire supplied text checked | Yes | Fully represented as absent | No formal hypothesis-testing framework supplied. |
| X1 WebArena | Yes | Yes | Fully represented | All Table 3 rates and relevant caveats. |
| X2 Overall OM2W | Yes | Yes | Fully represented | Sample and three rates included. |
| X3 Diversity | Yes | Yes | Fully represented | Visual and clustering limitations included. |
| X4 Depth/visits | Yes | Yes | Fully represented | F5 and T4 evidence included. |
| X5 Sampling | Yes | Yes | Fully represented | F6 trend and uncertainty included. |
| X6 Filtering | Yes | Yes | Fully represented | Counterfactual-accounting caveat included. |
| X7 Coverage | Yes | Yes | Fully represented | Three conditions and scope included. |
| X8 Proposal design | Yes | Yes | Fully represented | T7–T8 counts and different budgets included. |
| X9 Cost | Yes | Yes | Fully represented | T9 rows, cache assumption, cost scope included. |
| X10 Similarity/difficulty transfer | Yes | Yes | Fully represented | F7–F8 and T11 examples with inconsistencies. |
| X11 Bootstrap | Yes | Yes | Fully represented | Ratios, p-values, rounding, significance limits. |
| F1 | Yes, visually | Yes | Fully represented | Components and feedback routes explained. |
| F2 | Yes, visually | Yes | Fully represented | Algorithms accounted for; no invented quantitative comparison. |
| F3 | Yes, visually | Yes | Fully represented | All three exact proportions included. |
| F4 | Yes, visually and extracted labels | Yes | Represented in compressed form | All domains and major trends included; tiny label census omitted. |
| F5 | Yes, visually | Yes | Fully represented | Three panels, axes, colors, ranges, trend, caveats. |
| F6 | Yes, visually | Yes | Fully represented | Bins, lines, meanings, trend; exact points unavailable. |
| F7 | Yes, visually | Yes | Fully represented | All exact bar labels included. |
| F8 | Yes, visually | Yes | Fully represented | All counts included; caption and totals checked. |
| T1–T3 | Yes, visually | Yes | Fully represented | Exact dataset and benchmark values included. |
| T4 | Yes, visually | Yes | Fully represented | Every row's count, difference, and depth represented; long URL syntax compressed. |
| T5–T10 | Yes, visually | Yes | Fully represented | All substantive conditions and numerical entries included. |
| T11 | Yes; pp. 18–19 text-only | Yes | Represented in compressed form | Model/domain/result/difficulty structure and task range retained; repeated task constraints compressed. |
| ALG1 | Yes, visually | Yes | Fully represented | Workflow and labeling order included. |
| ALG2 | Yes, visually | Yes | Fully represented | Success filter and incomplete printed call noted. |
| ALG3 | Yes, visually | Yes | Fully represented | Outer/inner loops, additions, both solver starts included. |
| E1–E5 | Yes | Yes | Fully represented | All contribution-relevant notation explained; no absent theorem invented. |
| A1 Action space | Yes, visually | Yes | Fully represented | Fifteen actions represented. |
| A2 Agent prompt | Yes; mixed visual/text | Yes | Represented in compressed form | Inputs, executable JSON structure, examples' purpose included. |
| A2 Explorer prompts | Yes, text-only | Yes | Represented in compressed form | Specificity, priorities, recording, return behavior included. |
| A2 Judge prompt | Yes; mixed visual/text | Yes | Fully represented | Task-specific evaluation criteria and inputs included. |
| B1.1–B1.2 | Yes, visually | Yes | Fully represented | Counts, clusters, budgets, rationale included. |
| B2–B3 | Yes, visually | Yes | Fully represented | Cost and uncertainty analyses included. |
| B4 | Yes; mixed visual/text | Yes | Fully represented in analysis; examples compressed | Similarity, difficulty, reversals, inconsistencies included. |
| C | Yes, text-only | Yes | Fully represented | Hyperparameters, hardware, durations, missing settings included. |
| D | Yes, text-only | Yes | Represented in compressed form | LLM generation and author-reviewed writing/figure assistance disclosed. |
| Major contributions | Yes | Yes | Fully represented | Method, algorithm, dataset, implementation, empirical findings separated. |
| Author-stated limitations | Yes | Yes | Fully represented | Domain scope, success-only training, size, bias propagation included. |
| Separate supplementary material | No artifact supplied | Accounted for | Missing from supplied material | No claim of review or assumption of existence. |
| Linked code/data/models | Link read, artifacts not inspected | Accounted for | Inaccessible within supplied evidence | Implementation and release status not independently checked. |

### Missing or inaccessible material

No pages are missing from the supplied text sequence. Visual renderings of pages 10, 13–14, and 18–20 were not supplied. The linked repository, dataset, models, and reproduction documentation are outside the evidence provided. Underlying numerical plot data, full collection logs, trajectory records, reward implementation, and independent annotation audits are not available. No separate supplementary file was supplied, and none is claimed to have been reviewed.

### Uncertain interpretations

The 39K unsuccessful-trajectory statement conflicts with Table 1's 17,245 failures. Figure 8 totals do not fully reconcile with Table 2. The semantic identity of Figure 5's dotted markers is not clearly defined. Figure 6's exact point values and per-bin denominators are unavailable. Table 9's broader counts are not mapped precisely to Table 1. The PageExplorer navigation restriction, success-only versus whole-dataset training wording, solver sample allocation, URL normalization, frontier ordering, state restoration, and exact judge-response input assembly are incompletely specified. Tiny Figure 4 labels are only partly visually readable. The security comparison requested by the user remains untested and therefore UNKNOWN.

### Deliberately compressed material

Repeated motivation, the individual bibliography entries, acknowledgements, every radial intent label in Figure 4, exact long URL patterns in Table 4, repeated wording in prompt examples, and all detailed query constraints in Table 11 are compressed. Their substantive purposes and implications are represented. Headers, page numbers, decorative box styling, and extraction/loading artifacts are non-substantive. Appendix D additionally states that LLMs suggested phrasing revisions and helped iterate figure code, with author review before inclusion; this disclosure is represented without reproducing its full prose.

### Potential omissions

No known substantive section, numbered figure, table, algorithm, contribution-relevant mathematical object, or stated limitation from the supplied inventory is entirely unrepresented. Several secondary components are represented in disclosed compressed form. This is coverage of the supplied 20-page evidence, not a claim that every word, plot datum, repository behavior, or possible supplementary artifact has been preserved or verified.
