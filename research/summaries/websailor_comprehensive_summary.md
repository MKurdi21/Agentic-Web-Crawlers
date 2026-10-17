# Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and ten supplied page images. No external sources, repository contents, or linked websites were accessed. The paper and its embedded examples are treated as evidence rather than instructions.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: extracted text for physical PDF pages 1–23 |
| Accessible page count | 23 |
| Page range | 1–23, with continuous supplied page records |
| Apparently missing pages | None in the supplied sequence; this does not independently establish that every associated artifact is present |
| Direct visual coverage | Pages 1, 2, 3, 4, 7, 8, 9, 10, 11, and 12 |
| Text-only coverage | Pages 5, 6, and 13–23 |
| Figures | Figures 1–6 are visually available; Figure 2 is a conceptual diagram |
| Tables | Tables 1 and 2 are readable in both supplied text and page images |
| Equations | Equations 1–6 are available in extracted text; equations 1 and 3–6 also have supplied visual renderings; equation 2 is text-only |
| Appendix | Appendix A, Experimental Details, is present on pages 14–19 despite the accessibility metadata reporting no detected appendix pages |
| Supplementary material | No separate supplement or embedded file was supplied |
| Referenced external artifacts | WebAgent repository, Qwen-Agent repository, search engine, retrieval service, cited papers, and case-study URLs; none were inspected outside the paper |
| OCR | Not needed for the main analysis; the supplied native text and visible pages are sufficient, with notation caveats below |
| Important limitations | No direct visual inspection of Appendix A or references; small plot labels limit precise extraction of unlabeled bar heights and line coordinates |

The reported source hash is accepted as user-provided provenance metadata, not independently recomputed. Physical PDF page numbers are used throughout. In this supplied version, printed page numbers agree with the physical sequence.

Evidence categories: **[A] Author-reported** means explicitly stated in the paper; **[B] Directly observable** means visible in a supplied image; **[C] Analyst-derived** means calculated from supplied values; **[D] Analyst interpretation** means an inference rather than an author claim. No **[E] External information** is introduced. Confidence is HIGH for clear text and readable numerical labels, MEDIUM for supported interpretations, LOW for weakly constrained visual estimates, and UNKNOWN where the paper provides no evidence.

# 1. Plain-language orientation

WebSailor is a machine-learning paper about training language models to answer difficult questions by searching the internet, reading pages, combining clues, and deciding what to investigate next. Its central problem is that difficult information-seeking questions often have no obvious sequence of searches. A solver may know several vague clues without knowing the relevant person, institution, event, or document. Finding the answer requires progressively narrowing a large set of possibilities.

The authors argue that previous open-source web agents were trained mainly on questions with either an easy answer or a fairly clear chain of intermediate steps. They propose training on harder, deliberately ambiguous questions generated from interconnected real-world information. Their pipeline combines a synthetic dataset called **SailorFog-QA**, reconstructed concise reasoning traces, a small supervised cold start, and reinforcement learning using **Duplicating Sampling Policy Optimization**, or **DUPO**. [A; pp. 1–7]

The resulting WebSailor models use the Qwen-2.5 model family at 3B, 7B, 32B, and 72B sizes. Here B denotes billions in the model-size labels. The strongest version scores 12.0 on BrowseComp-en, 30.1 on BrowseComp-zh, 55.0 on Xbench-DeepSearch, and 55.4 on the evaluated GAIA subset. It leads the listed open-source comparisons, but DeepResearch remains substantially ahead where results are available. The paper therefore supports an improvement in open-source information-seeking capability, not universal parity with proprietary agents. [A/B; Table 1, p. 9]

The user’s research question concerns why web AI agents might be more vulnerable than standalone language models. **This paper is not a security evaluation.** It compares direct answering with browsing on task accuracy, but does not compare their security vulnerability. Its relevance is architectural: search results, retrieved webpages, an intermediate summarization model, and repeated tool responses enter the agent’s decision context. Treating these as possible security-relevant boundaries is an analyst inference; the paper provides no attack success rates or demonstrated exploitation. [D; pp. 3, 14]

# 2. Document roadmap

The supplied work is an **empirical machine-learning and algorithm paper**, with a web-agent system description and a synthetic-data contribution. It is not a systematic review, security paper, or theorem-driven study.

| Original component | Pages | Role in the argument |
|---|---:|---|
| Title, abstract, Figure 1 | 1 | Introduces the pipeline and headline benchmark comparison |
| §1 Introduction | 2–3 | Motivates uncertainty reduction and the open-source capability gap |
| §2 Problem Definition | 3 | Defines the agent’s repeated thought–action–observation interaction |
| §3 Large-scale Training Data Synthesis | 3–6 | Describes question synthesis and supervision construction |
| §3.1 SailorFog-QA | 3–5 | Defines task levels, graph expansion, subgraph sampling, and obfuscation |
| §3.2 Reconstructing Reasoning | 5–6 | Replaces expert-model thoughts with concise reconstructed thoughts |
| §4 Reinforcement Learning with Cold Start | 6–7 | Introduces the two-stage training procedure |
| §4.1 Rejection Sampling Fine-Tuning | 6 | Defines trajectory formatting, filtering, and observation masking |
| §4.2 DUPO | 6–7 | Defines batch selection, duplication, objective, and rewards |
| §5.1 Setup | 7–8 | Lists models, benchmarks, baselines, and evaluation parameters |
| §5.2 Main Results | 8–10 | Presents Table 1 and interprets benchmark performance |
| §5.3 Analysis | 10–12 | Examines difficulty, simple-task transfer, RL gains, and cold start |
| §5.4 Limitations and Future Work | 12 | Discusses context limits, over-thinking, and training efficiency |
| §6 Related Work | 12–13 | Positions the approach among benchmarks and web agents |
| §7 Conclusion | 13 | Restates contributions and broader ambitions |
| Appendix A.1–A.4 | 14–15 | Gives tools, graph construction, trajectory format, and training parameters |
| Appendix A.5 | 15–19 | Provides one abbreviated BrowseComp-en case trajectory |
| References | 20–23 | Lists cited works; their underlying contents were not reviewed |

The inventory contains six numbered figures, two numbered tables, six numbered equations, five substantive appendix subsections, seven distinct experimental or analytical components, and no numbered theorem, lemma, or algorithm. Appendix A.2 nevertheless contains a five-step graph-construction procedure. Stable experiment identifiers X1–X7 are assigned in section 8 below.

# 3. Background and context

A **large language model**, or **LLM**, produces text from a context containing instructions and previously available information. The paper’s **direct inference** condition asks a model to answer using its internal knowledge. A **web agent** adds tools and repeated interaction: the model chooses a search or visit action, receives external information, and decides the next step. This description follows the paper’s system model rather than a general claim about all agents. [A; pp. 3, 8]

**ReAct** is the named framework used here for alternating Thought, Action, and Observation. A thought expresses the agent’s current reasoning; an action is a tool call or final answer; an observation is the environment’s response. The supplied paper cites the framework but does not spell out its name as a formal acronym. [A; p. 3]

**Question answering**, or **QA**, is the task of returning an answer to a question. **Multi-hop QA** requires connecting intermediate facts. The authors distinguish this from their harder tasks: a multi-hop question may have several steps but still possess a clear chain, whereas their Level 3 questions require choosing among uncertain paths. [A; pp. 3–4]

A **knowledge graph** represents entities as nodes and relationships as edges. A **subgraph** is a selected portion of that graph. **Random walks** and probabilistic expansion create connections that need not form a simple chain. **Compositional generalization** means handling new combinations of entities and relationships; the paper uses this concept to explain why varied graph structures might encourage flexible reasoning. [A; pp. 2, 4–5]

**Information obfuscation** deliberately makes clues less specific: an exact date becomes a broad period, a name becomes a partial clue, or a precise quantity becomes a qualitative description. This is a data-generation technique, not an attack evaluated against the agent. [A; p. 5]

**Supervised fine-tuning**, or **SFT**, trains on provided examples. **Rejection sampling fine-tuning**, or **RFT**, retains successful generated examples before fine-tuning. **Reinforcement learning**, or **RL**, updates the policy using rewards from sampled outputs. A **rollout** is one generated interaction trajectory. **Cold start** refers here to the initial RFT phase before RL, not to a newly initialized language model. [A; pp. 6–7]

A **large reasoning model**, or **LRM**, is the paper’s term for expert models such as QwQ and DeepSeek-R1. **Chain of thought**, or **CoT**, denotes intermediate reasoning text. The pipeline reconstructs a short-CoT rather than copying expert reasoning wholesale. [A; pp. 2, 5–6]

# 4. Research problem and gap

**Existing problem.** Complex web questions combine uncertain clues across a large information space. A straightforward script may fail because the solver does not know which entity or source to examine first. The authors describe brute-force exploration as potentially requiring thousands of calls and exceeding the model’s context window. This is explanatory reasoning in the paper, not a measured brute-force experiment. [A; p. 3]

**Shortcomings attributed to earlier approaches.** The authors say earlier datasets emphasize low-uncertainty lookup tasks or structured multi-hop reasoning. They also say pure supervised agents struggle to generalize adaptively, while RL approaches face stability and sample-efficiency problems. These are their literature-positioning claims, not independently verified assessments of all prior systems. [A; pp. 2, 13]

**Research gap.** The target is an open-source post-training method that develops effective search strategies for high uncertainty that is difficult to reduce. The problem includes producing suitable hard questions, obtaining useful long-horizon supervision, and making RL affordable enough to train on those questions. [A; pp. 2–7]

**Motivation.** Proprietary agents demonstrate strong performance but have opaque architectures and training procedures. The authors aim to narrow this capability gap through a full training pipeline. Their discussion of human cognitive limitations motivates the work, but the benchmark experiments do not themselves constitute a controlled human-versus-agent study. [A/D; pp. 1–2, 13]

**Scope.** The evaluated system is mainly an information-seeking agent with search and webpage visits. GAIA is evaluated only on 103 text-only validation cases. The paper does not establish performance for arbitrary multimodal assistance, unrestricted computer control, or security-sensitive transactions. [A/D; pp. 8, 14]

# 5. Research questions, objectives, and hypotheses

The paper does not present a numbered list of formal research questions. Its objectives and hypotheses should therefore remain separate from the user’s security question.

| Identifier | Type | Source-grounded formulation | Source |
|---|---|---|---|
| O1 | Objective | Develop open-source agents that reduce difficult uncertainty through adaptive web exploration | pp. 2–3 |
| O2 | Objective | Generate scalable, structurally diverse, ambiguous questions grounded in real-world information | pp. 4–5 |
| O3 | Objective | Construct concise supervision without directly imitating verbose expert thoughts | pp. 5–6 |
| O4 | Objective | Improve effectiveness and efficiency of agentic RL | pp. 6–7 |
| H1 | Explicit core hypothesis | Training on complex, hard-to-reduce uncertainty yields robust and generalizable reasoning strategies | p. 9 |
| H2 | Author position tested by ablation | An RFT cold start is important for acquiring long-horizon strategies under sparse rewards | pp. 2, 12 |
| O5 | Evaluation objective | Check whether training on hard tasks preserves performance on simpler questions | p. 11 |

The authors connect Table 1 to H1, Figure 6 to H2, and Figure 4 to O5. Those connections are visible, but Table 1 tests the integrated pipeline rather than isolating graph complexity or obfuscation. It therefore provides stronger evidence for the pipeline’s overall performance than for the exclusive causal contribution of each ingredient. [D]

The user’s question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis**, is an external analytical lens supplied by the user, not the paper’s title or explicit research question. This source helps identify architecture and exposure boundaries. It does not answer whether the agent is more vulnerable, by how much, or under which attacker capabilities. [D; confidence HIGH for this scope distinction]

# 6. Assumptions / Threat Model

There is **no explicit security threat model** in the supplied paper. It does not define an attacker, protected asset, malicious webpage, adversarial search result, exfiltration goal, or security success metric. Its use of reward-hacking terminology concerns training rewards rather than a comparative study of web-agent attacks. [A/D; p. 7]

The operational model assumes an LLM can generate parsable actions, the search engine returns results, page retrieval supplies content, and a summary model extracts information relevant to a stated goal. The agent then uses the accumulated context to choose subsequent thoughts and actions. These are dependencies described by the paper; the authors do not label them trusted security components. [A; pp. 3, 14]

The final-answer judge is another model. Both reward calculation and evaluation rely on model-based correctness judgments. The paper does not give the judge’s identity, complete rubric, calibration measurements, or adversarial robustness. The quality of judgments is thus an operational dependency whose security implications remain unevaluated. [A/D; pp. 7–8]

**Analyst interpretation for security research:** the search engine, external pages, retrieval service, page summarizer, and tool-response history are distinct places where information enters or is transformed. This creates more described input pathways than the paper’s direct-answering condition. It is reasonable to examine these pathways in a future security study, but additional pathways alone do not prove higher vulnerability. No demonstrated instruction-following failure can be inferred from this performance paper. [D; MEDIUM]

# 7. Methodology

## 7.1 Agent architecture and interaction

The model runs a ReAct loop. It can issue **search**, issue **visit**, or produce a final answer. Search accepts several queries and returns ten titles, snippets, and URLs per query. Appendix A.1 identifies Google as the search engine. Visit accepts webpage URLs and corresponding goals; Jina retrieves the full content, then Qwen-2.5-72B summarizes relevant information for the goal. Thus the agent ordinarily receives a goal-conditioned summary from a visit, not necessarily the full raw page. [A; pp. 3, 14]

Appendix A.3 identifies Qwen-Agent as the implementation framework and limits tool calls to no more than 30. A call may include multiple queries or pages, so the call limit is not a limit of 30 individual searches or 30 individual pages. The paper does not quantify the total number of pages consulted per trajectory. [A/D; p. 14]

The term WebTraverseX appears in §2 for the action-space description, while the system is called WebSailor elsewhere. The supplied material does not explain whether WebTraverseX is an environment name or a naming remnant. Its described actions agree with Appendix A.1, but the naming uncertainty is retained. [A/D; p. 3]

## 7.2 SailorFog-QA construction

The authors first build a graph around a rare or fuzzy entity obtained through Wikidata’s SPARQL service. Search and visit gather features and related entities from internet information. Those entities become nodes, and their relationships become edges. Expansion probabilistically selects either a newly related entity or a previously visited node, repeating until a predefined edge count is reached. [A; pp. 4, 14]

The predefined edge count, database rules used to select rare entities, and transition probabilities are not numerically specified. The prose describes densely interconnected, overlapping paths, but supplies no graph-density measurements or distribution of topology types. These omissions limit reconstruction of the generator from the paper alone. [D; pp. 4, 14]

Subgraphs supply combinations of entities and relationships from which questions and answers are formed. Obfuscation then reduces specificity. The paper gives examples involving broad time references, initials instead of full names, and qualitative quantities. It claims internet grounding, varied reasoning demands, and scalability because the number of possible subgraphs grows non-linearly with graph size. No measured scaling curve or full dataset count is supplied. [A/D; p. 5]

The two printed synthetic examples concern an early Christian writer linked to a chronology and a musical piece linked through biographical clues. Their supplied answers are respectively Estimated Tree-Ring Chronology: 300-450 A.D. and the Rue de Rivoli. These are author-provided examples, not independently verified facts. They are compressed here because their function is to illustrate vague clues and coupled relationships. [A; p. 5]

## 7.3 Expert trajectories and reconstructed thoughts

An expert LRM first solves a question, generating thoughts, actions, and observations. The pipeline discards its original thoughts while retaining the successful action–observation sequence. A separate instruction-following model then reconstructs concise thoughts for each step, using the preceding reconstructed history, the expert’s current action, and the subsequent observation. [A; pp. 5–6]

The rationale is to avoid **stylistic contamination**, meaning restrictive imitation of expert-model verbosity and style, and **context overload**, meaning overly long histories that exceed available context. QwQ-32B is named as an example expert model. The exact reconstruction-model identity is not supplied; it must not be assumed to be the webpage-summary model. [A; pp. 5–6]

The reconstruction model sees the observation that follows the action it is justifying. Consequently, the reconstructed thought is a hindsight-informed explanation of a successful step. The paper explicitly specifies this conditioning; it is not an extraction error. Whether such explanations faithfully reproduce the decision process available before the observation is an analyst question rather than a measured limitation acknowledged by the authors. [A/D; Eq. 2, p. 6]

## 7.4 RFT cold start

Trajectories use tags for thoughts, tool calls, tool responses, and final answers. Filtering retains correct final answers, discards trajectories exceeding 32k tokens, and keeps trajectories with more than five tool calls. The purpose of the last filter is to retain extended decision sequences presumed to contain complex planning. Observation tokens are masked from the supervised loss so the model learns to generate thoughts and actions rather than imitate environment outputs. [A; p. 6]

The introduction describes a cold start with just over 2k high-quality examples. It gives neither the exact count nor a full count breakdown by filtering stage or model size. The limitations section says trajectories are filtered to under 32k, whereas the Methods wording discards those exceeding 32k. The difference at exactly 32k tokens is unresolved. [A/D; pp. 2–3, 6, 12]

## 7.5 DUPO reinforcement learning

Before RL, the method removes overly easy questions for which all eight sampled rollouts are correct. During RL, it removes cases whose reward standard deviation is zero and replaces their batch slots by randomly duplicating other cases from the same batch with nonzero standard deviation. The authors describe zero-variance cases as entirely correct or entirely incorrect. [A; p. 7]

This approach avoids waiting for sequential new-question rollouts to refill a batch. The authors report approximately 2–3 times speedup relative to DAPO-style dynamic sampling. They provide no timing table, hardware specification, runtime distribution, or detailed matched throughput experiment, so the magnitude remains an author-reported efficiency result with incomplete benchmarking context. [A/D; p. 7]

The objective uses group-relative advantages, token-level policy updates, and asymmetric clipping bounds. Generated tokens contribute to the loss while observations are masked; observations still remain in the context. The reward combines format validity with final-answer correctness, weighted 0.1 and 0.9 respectively. Correctness uses an LLM judge. [A; Eqs. 3–5, p. 7]

## 7.6 Implementation and numerical configuration

| Setting | RFT/SFT | RL | Source |
|---|---|---|---|
| Training framework | Megatron | verl | p. 15 |
| Batch size | 32 | 128 | p. 15 |
| Mini-batch size | Not specified | 32 | p. 15 |
| Learning rate | 5e-6 | 1e-6 | p. 15 |
| Minimum learning rate | 1e-10 | Not specified | p. 15 |
| Schedule | Warmup plus cosine decay | Not specified | p. 15 |
| Weight decay | 0.1 | Not specified | p. 15 |
| Rollouts per group | Not applicable | 8 | p. 15 |
| Sampling temperature | Not specified | 1.0 | p. 15 |
| Top-p | Not specified | 1.0 | p. 15 |
| RL duration | Not applicable | Limited to 50 steps | p. 12 |

Evaluation uses temperature 0.6 and top-p 0.95, distinct from RL rollout sampling. Hardware, software versions, random seeds, exact training duration, number of RFT epochs, clipping-bound values, and complete data splits are not reported in the supplied material. [A/D; pp. 8, 15]

# 8. Experiments / Analyses

| ID | Purpose and conditions | Evidence and results | Caveats |
|---|---|---|---|
| X1 Main benchmark comparison | Compare four WebSailor sizes with direct inference and proprietary/open-source agents on four benchmarks | Table 1: WebSailor-72B obtains 12.0/30.1/55.0/55.4 across BrowseComp-en/zh, Xbench, and GAIA | Mixed baseline acquisition; incomplete proprietary results; GAIA is a 103-case text-only subset |
| X2 Tool-call distribution | Compare correct, pre-final-filter expert trajectories across SailorFog-QA, BrowseComp-en, and WebDancer-QA | Figure 3: SailorFog has a longer tail; WebDancer has over 50% at two calls and virtually none beyond ten | Tool calls are a proxy for difficulty; sample counts and uncertainty are absent |
| X3 Dataset pass rates | Compare o4-mini and DeepSeek-R1 with browsing and ReAct on three datasets | Table 2: o4-mini 47.3/90.2/26.3; DeepSeek-R1 38.9/84.4/9.5 | SailorFog is before filtering; answer ambiguity partly contributes to lower scores |
| X4 Simple-task compatibility | Evaluate 32B and 72B WebSailor and baselines on 200 randomly sampled SimpleQA pairs | Figure 4: 93.5 and 92.8 for WebSailor-72B and 32B | Full dataset has 4,326 pairs; no seed or confidence intervals |
| X5 RL contribution | Compare RFT and RL for 32B/72B, pass@1/pass@3, on four benchmarks | Figure 5 labels positive gains for all sixteen conditions | Only one-sample and three-sample performance shown; no repeated-training uncertainty |
| X6 Cold-start ablation | Compare direct RL from Qwen-2.5-instruct-32B with RL after RFT | Figure 6: cold-start condition has higher plotted accuracy and tool-call count | Broken accuracy axes; exact point values unlabeled; limited model/configuration scope |
| X7 Qualitative case | Show an abbreviated BrowseComp-en search-and-verification trajectory | Appendix A.5: nine tool-action steps, then final answer Atari 130XE | Ellipses omit observations; some transitions cannot be independently checked |

These analyses address distinct questions. X2 and X3 study the generated data, X4 studies transfer to simpler tasks, X5 studies the benefit of RL after RFT, X6 studies the need for an initial supervised stage, and X7 illustrates behavior. They should not be treated as interchangeable evidence for a single causal mechanism.

# 9. Results

**Best listed open-source results.** WebSailor-72B is the highest-scoring listed open-source agent on all four Table 1 columns. It improves over WebDancer-QwQ from 3.8 to 12.0 on BrowseComp-en, 18.0 to 30.1 on BrowseComp-zh, 39.0 to 55.0 on Xbench, and 51.5 to 55.4 on GAIA. These comparisons use the evaluated configurations and do not establish superiority over every possible open-source system. [A/B; p. 9]

**Analyst-derived differences:** 12.0−3.8 = **8.2 percentage points** on BrowseComp-en; 30.1−18.0 = **12.1 points** on BrowseComp-zh; 55.0−39.0 = **16.0 points** on Xbench; 55.4−51.5 = **3.9 points** on GAIA. The smaller GAIA margin is consistent with the authors’ interpretation that the system specializes in retrieval rather than mathematical and computational abilities. No numerical result for the claimed purely retrieval GAIA subset is provided. [C/A; p. 9]

**Smaller-model result.** WebSailor-7B scores 6.7 on BrowseComp-en against 2.5 for WebDancer-32B and 2.8 for WebThinker-RL. The corresponding differences are 4.2 and 3.9 points. This shows that model-size labels alone do not explain this comparison. It does not isolate which training ingredient caused the improvement. [A/C/D; p. 9]

**Proprietary comparisons.** WebSailor-72B’s 30.1 on BrowseComp-zh exceeds Doubao’s listed 26.0 by 4.1 points and Grok-3’s 12.9 by 17.2 points. However, DeepResearch scores 42.9, a 12.8-point lead over WebSailor. On BrowseComp-en, DeepResearch’s 51.5 exceeds 12.0 by 39.5 points; on GAIA, 67.4 exceeds 55.4 by 12.0 points. The prose’s parity language must therefore be read as applying to selected proprietary comparisons, not the strongest system overall. [A/C; pp. 9–10]

**Direct answering can remain competitive in some conditions.** DeepSeek-R1 without browsing obtains 26.3 on BrowseComp-zh, exceeding WebSailor-32B’s 25.5 and several smaller agents. WebSailor-3B and 7B do not outperform all direct models in that column. This important table result qualifies any broad claim that adding tools invariably improves accuracy. [B/D; Table 1, p. 9]

**Synthetic-data difficulty.** Under browsing/ReAct in Table 2, o4-mini drops from 90.2 on WebDancer-QA to 47.3 on SailorFog-QA; DeepSeek-R1 drops from 84.4 to 38.9. Derived differences are 42.9 and 45.5 points. BrowseComp-en is harder still under these conditions, at 26.3 and 9.5. These are different from Table 1’s direct-inference numbers: the repeated 26.3 elsewhere belongs to a different model/task condition and must not be conflated. [A/C; pp. 9–10]

**Simple-task result.** Figure 4 reports 93.5 for WebSailor-72B and 92.8 for WebSailor-32B on the 200-question SimpleQA sample. Their differences against WebDancer-QwQ’s 90.5 are 3.0 and 2.3 points. No interval or significance test establishes whether the 0.7-point difference between the two WebSailor sizes is meaningful. [B/C/D; p. 11]

**Efficiency and ablations.** DUPO’s approximately 2–3 times speedup is reported in prose. Figures 5–6 support positive RL gains and better outcomes with cold start in the tested setting. The larger claims about stable reasoning and indispensable cold start are interpretations of these results, not universal guarantees. [A/D; pp. 7, 11–12]

# 10. Figure-by-figure interpretation

## Figure 1 — Headline BrowseComp comparisons

Figure 1 contains two vertical bar-chart panels: BrowseComp-en and BrowseComp-zh. The x-axes list model or agent configurations; the y-axes show benchmark scores with linear scales, approximately 0–15 in the English panel and 0–30 in the Chinese panel. The y-axis units are not explicitly spelled out in the chart, but the surrounding evaluation presents accuracy/pass@1 scores. Purple shades identify WebSailor sizes; gray bars identify comparison systems. No uncertainty bars are shown. [B; p. 1]

The English panel labels WebSailor-72B 12.0, WebSailor-32B 10.5, DeepSeek-R1-Browse 9.5, WebDancer-QwQ 3.8, WebThinker-QwQ 2.8, DeepSeek-R1 2.0, GPT-4o with browsing 1.9, and Search-o1-32B 0.6. The Chinese panel labels WebSailor-72B 30.1, WebSailor-32B 25.5, Doubao-Search 26.0, WebDancer-QwQ 18.0, WebThinker-QwQ 14.7, Grok-3 12.9, and Search-o1-32B 7.2. These values are visually readable rather than estimates. [B]

The caption says DeepSeek-R1-Browse uses the same browsing implementation as WebSailor, while Doubao and Grok are proprietary products and GPT-4o’s browsing result is taken from an official publication. The chart is therefore not a wholly uniform contemporaneous rerun. DeepResearch is absent here but appears in Table 1 with much higher scores. Some Figure 1 configurations differ from Table 1: WebThinker-QwQ is not WebThinker-RL, and Search-o1 labels/results do not map unambiguously to the table’s backbone-specific rows. The paper does not explain these differences sufficiently to merge them. [A/B/D; pp. 1, 9]

## Figure 2 — Three task levels and the sampling/obfuscation concept

Figure 2 is a conceptual diagram with three dashed boxes. Level 1 displays mostly disconnected entities, with one highlighted node, corresponding to a simple lookup. Level 2 highlights a connected sequence, corresponding to a known multi-step path. Level 3 shows a more interconnected graph, a downward Sample arrow, and a downward Fuzz arrow leading to clustered, ambiguously connected groups. [B; p. 4]

The highlighted purple nodes and edges illustrate relevant subsets and relationships. Circular nodes are entities; connecting lines are relations. There are no numerical axes, measured distributions, or statistical quantities. The visual communicates a proposed taxonomy and construction strategy, not evidence that every real task fits neatly into three categories. Its examples are illustrative questions supplied by the authors. [A/B/D]

## Figure 3 — Tool-call distributions

Two histogram-like panels compare SailorFog-QA with BrowseComp-en in panel a and with WebDancer-QA in panel b. The x-axis is Number of Tool Calls, running from 0 to 30; the y-axis is Sample Proportion on a linear scale. Purple denotes SailorFog-QA and green denotes the comparator. The panels use different y-axis ranges: about 0.10 in panel a and 0.6 in panel b, so equal visual bar heights across panels do not mean equal proportions. [B; p. 10]

The paper reports that over 50% of WebDancer trajectories use two calls and virtually none exceed ten. SailorFog has a long tail extending beyond twenty calls, and its distribution resembles BrowseComp-en more closely. Individual unlabeled bin proportions are not treated as exact values. Importantly, these are correct trajectories before the final complexity filter; the actual cold-start set retains only trajectories with more than five calls. No sample count or error measure is shown. [A/B]

## Figure 4 — SimpleQA transfer

Figure 4 is a vertical bar chart with model labels on the x-axis and Pass@1 (%) on the y-axis, using a linear scale from 0 to 100. Purple shades denote WebSailor, green denotes other browsing agents, and gray denotes direct models. Values are explicitly labeled above bars. No confidence intervals are provided. [B; p. 11]

The exact sequence is: WebSailor-72B 93.5; WebSailor-32B 92.8; WebDancer-QwQ 90.5; WebDancer-32B 87.5; WebThinker-RL 77.5; DeepSeek-R1-ReAct 72.2; R1-Searcher-7B 52.0; GPT-4.1 41.6; GPT-4o 38.2; DeepSeek-R1 27.8; o4-mini 20.0; Qwen-2.5-72B 15.8; QwQ-32B 12.7; Qwen-2.5-32B 9.0. Minor model-label capitalization and spelling irregularities appear in the extracted chart text; recognizable model names are normalized here without changing numbers. [B]

The result supports compatibility with the sampled simpler questions. The paper reports 200 randomly sampled pairs from 4,326, not evaluation of the full dataset. The 92.8 value does not correspond to an integer number of correct answers out of exactly 200 if a single binary judgment is made for each item: 0.928×200 = 185.6. This arithmetic observation does not prove an error; averaging, a different scoring aggregation, or another detail might explain it, but the paper does not specify such a detail. [A/C/D]

## Figure 5 — RFT versus RL and pass@1 versus pass@3

This grouped bar chart contains four benchmark groups. Each has 32B-pass@1, 32B-pass@3, 72B-pass@1, and 72B-pass@3 conditions. The y-axis is Accuracy (%) on a linear scale. Light purple represents RFT; darker purple represents RL. Green annotations give the absolute increases between paired bars. [B; p. 11]

The readable gains, in that condition order, are BrowseComp-en: +3.3, +2.2, +3.7, +3.4; BrowseComp-zh: +6.3, +6.5, +8.3, +4.9; GAIA: +6.6, +4.7, +3.0, +3.6; XBench: +7.6, +8.0, +3.7, +2.0. These are accuracy-point increases, not relative percentage improvements. Exact underlying bar heights are not all labeled, so the annotations are the primary exact evidence. [B]

All shown gains are positive. However, not every pass@1 absolute gain exceeds its pass@3 counterpart: the 32B Chinese and XBench comparisons and the 72B GAIA comparison show the reverse. The authors’ proportional-improvement claim concerns relative changes from different starting values; it cannot be checked merely by comparing these absolute annotations. Similarly, English BrowseComp has smaller absolute gains than several other datasets, so the prose’s most-significant-gains wording should not automatically be read as largest absolute increase. [A/B/D; pp. 11–12]

## Figure 6 — Cold-start versus direct RL

Panels a and b plot Pass@1 (%) against training Step for BrowseComp-en and GAIA. Panel c plots Number of Tool Call against Step. Purple lines with small markers denote Cold-start, and green lines denote Instruct, meaning direct RL from the instruction model. [A/B; p. 12]

The accuracy panels use broken y-axes: panel a separates roughly 2–5 from 8–12, while panel b separates roughly 34–42 from 49–54. The breaks make the two conditions visible together, but prohibit interpreting the displayed vertical distance as a continuous linear difference. Panel c has a conventional linear call-count axis. [B]

Approximate visual estimates at the final shown points are around 10–11 versus 4 on BrowseComp-en, around 53 versus 41 on GAIA, and around seven versus three tool calls. These are approximate estimates only; the chart supplies no exact point labels. The cold-start line remains higher in the displayed comparisons. Sample counts, confidence intervals, repeated-run variation, and a detailed definition of the call-count aggregation are absent. [B/D]

# 11. Table-by-table interpretation

## Table 1 — Main benchmark results

Rows represent model/configuration pairs, grouped into Direct Inference, Proprietary Agents, and Open-source Agents. Columns represent BrowseComp-en, BrowseComp-zh, Xbench-DeepSearch, and GAIA. The following preserves every numerical row, in that column order. Values are reported accuracy/pass@1 scores in percentage-style units; no uncertainties or significance markers accompany them. [A/B; p. 9]

| Model/configuration | BrowseComp-en | BrowseComp-zh | Xbench | GAIA |
|---|---:|---:|---:|---:|
| Qwen-2.5-32B, Direct | 0.6 | 3.9 | 8.7 | 13.6 |
| Qwen-2.5-72B, Direct | 0.6 | 7.0 | 12.7 | 14.6 |
| GPT-4o, Direct | 0.6 | 6.2 | 18.0 | 17.5 |
| GPT-4.1, Direct | 1.5 | 14.4 | 17.0 | 22.3 |
| QwQ-32B, Direct | 0.5 | 10.0 | 10.7 | 22.3 |
| o4-mini, Direct | 6.1 | 15.2 | 22.3 | 33.3 |
| DeepSeek-R1, Direct | 2.0 | 26.3 | 32.7 | 16.5 |
| Grok-3, Browsing | — | 12.9 | 50+ | — |
| Doubao, Browsing | — | 26.0 | 50+ | — |
| GPT-4o, Browsing | 1.9 | — | — | — |
| DeepResearch, Browsing | 51.5 | 42.9 | — | 67.4 |
| R1-Searcher-7B, ReAct | 0.4 | 0.6 | 4.0 | 20.4 |
| Qwen-2.5-32B, Search-o1 | 0.1 | 2.4 | 3.7 | 28.2 |
| WebDancer-32B, ReAct | 2.5 | 14.1 | 38.7 | 40.7 |
| QwQ-32B, Search-o1 | 2.8 | 17.9 | 25.0 | 39.8 |
| WebThinker-RL, ReAct | 2.8 | 7.3 | 24.0 | 48.5 |
| WebDancer-QwQ, ReAct | 3.8 | 18.0 | 39.0 | 51.5 |
| WebSailor-3B, ReAct | 3.3 | 9.7 | 27.7 | 33.0 |
| WebSailor-7B, ReAct | 6.7 | 14.2 | 34.3 | 37.9 |
| WebSailor-32B, ReAct | 10.5 | 25.5 | 53.3 | 53.2 |
| WebSailor-72B, ReAct | 12.0 | 30.1 | 55.0 | 55.4 |

The dagger-like proprietary marker indicates manual evaluation through websites, with some results taken from benchmark papers. A dash means unavailable because of cost constraints; it is not zero. The notation 50+ is imprecise and cannot establish whether 55.0 exceeds either proprietary Xbench result. [A]

DeepResearch is best among the reported scores on English BrowseComp, Chinese BrowseComp, and GAIA. WebSailor-72B is the best listed open-source system across all four. Within direct inference, o4-mini leads English BrowseComp and GAIA, while DeepSeek-R1 leads Chinese BrowseComp and Xbench. GPT-4.1 and QwQ tie at 22.3 on GAIA; several direct models tie at 0.6 on English BrowseComp. Such details demonstrate that method rankings depend on the dataset and configuration. [B]

## Table 2 — Difficulty under shared browsing/ReAct conditions

| Backbone | SailorFog-QA | WebDancer-QA | BrowseComp-en |
|---|---:|---:|---:|
| o4-mini | 47.3 | 90.2 | 26.3 |
| DeepSeek-R1 | 38.9 | 84.4 | 9.5 |

Both backbones are equipped with browsing tools and ReAct, and SailorFog is evaluated before filtering. Each model scores higher on WebDancer-QA than SailorFog and lower on BrowseComp-en than SailorFog. The authors acknowledge that SailorFog difficulty is partly confounded with nonunique answers. No sample counts, uncertainty measures, or significance tests are supplied for this comparison. [A/B; p. 10]

# 12. Diagram / Architecture Interpretation

Figure 2 is the only numbered conceptual diagram. Its three boxes encode increasing difficulty in reducing uncertainty, not a literal deployment architecture. The Level 3 Sample and Fuzz arrows show selection of a relational subset followed by intentional loss of clue specificity. The diagram does not specify a stochastic algorithm or edge-selection distribution. [A/B; p. 4]

The deployment architecture can be reconstructed from prose as follows: **question → agent context → thought/action selection → search or visit → observation → updated context → next decision → final answer**. Search sends queries to Google and returns titles, snippets, and URLs. Visit sends URLs through Jina retrieval, then full page content through a Qwen-2.5-72B goal-conditioned summary model, and returns the summary to the agent. This textual architecture is analyst organization of author-described components, not a separately supplied architecture figure. [A/D; pp. 3, 14]

The training architecture has a different information flow: **rare entity → graph expansion → subgraph → obfuscated QA → expert solution trace → discard expert thoughts → reconstruct concise thoughts → correctness/length/complexity filtering → RFT → DUPO RL**. The generator, expert, reconstruction model, policy model, page summarizer, and answer judge have distinct roles. Their identities and deployment arrangements are not all specified. [A/D; pp. 4–7, 14–15]

For the security research lens, the important boundary is that observations become part of the context used for subsequent actions. A summary can also transform raw page content before the main policy sees it. Whether this transformation removes, preserves, or introduces security-relevant content is not tested. Claims about attacks passing through the summarizer would therefore require new evidence. [D]

# 13. Equations and mathematical concepts

## Equation 1 — Interaction history

The paper writes a trajectory as **H_T = (τ_0, a_0, o_0, …, τ_i, a_i, o_i, …, τ_T, a_T)**. Here τ denotes a thought, a an action, and o an observation. The final action is a final answer, explaining why the displayed history ends without a final observation. The model samples subsequent thought/action behavior conditioned on previous history. [A; p. 3]

The printed policy notation uses π(a, t | H_{t−1}), although nearby prose identifies thought with τ. The meaning of t as a second policy argument is not explicitly resolved; it may be a notation inconsistency, but it is not silently repaired here. This equation defines the sequential object on which training and inference operate; it is not itself an optimization objective.

## Equation 2 — Hindsight-conditioned thought reconstruction

**τ̂_t ∼ π*(τ | H_{t−1}, a_t, o_t)**. The hat marks a reconstructed thought; π* is a separate instruction-following model; H contains preceding reconstructed thoughts, actions, and observations. Inputs include the expert’s chosen current action and the observation resulting from it. The output is a concise justification for that action. [A; p. 6, text-only]

The sampling symbol ∼ indicates generation from the reconstruction model. The method repeats this step across the trace to form a new training trajectory. Because o_t is included, the construction uses information that arrives after the action. The paper does not demonstrate that reconstructed thoughts are faithful records of pre-action reasoning. [D]

## Equation 3 — DUPO objective

In readable mathematical shorthand, the objective is **J(θ) = E[(1/Σ_i |o_i|) Σ_i Σ_t min(r_{i,t}(θ) Â_{i,t}, clip(r_{i,t}(θ), 1−ε_low, 1+ε_high) Â_{i,t})]**, with the constraint **0 < |{o_i : is_equivalent(y,o_i)}| < G**. [A; p. 7]

Here θ is the trainable policy parameter set; q and y are a question and answer sampled from dataset D; G is the number of rollouts in a group; |o_i| is the number of generated tokens in rollout i; t indexes generated tokens; r is a policy-probability ratio; Â is the relative advantage; and ε_low/ε_high are clipping bounds. Their numerical settings are absent. The expectation averages over questions and rollouts sampled from the old policy. The nested sums accumulate token contributions, and the denominator normalizes by total generated-token count.

The minimum and clipping operation restrict how strongly policy changes contribute to the update. The displayed correctness constraint retains mixed groups containing at least one correct and one incorrect answer. The accompanying prose describes removing zero-reward-variance groups and duplicating informative cases. Correctness-based selection and reward-variance selection are closely related in the authors’ description but not proven identical when format rewards can differ. [A/D]

Crucially, o in this equation denotes generated output tokens, whereas o in Equation 1 denotes environment observations. The paper explicitly warns about the generated-token meaning near Equation 4. Tool responses enter context but are masked from the policy loss. This notation reuse must not be mistaken for training the policy to generate webpage observations.

## Equation 4 — Ratio and relative advantage

**r_{i,t}(θ) = π_θ(o_{i,t}|context) / π_{θ_old}(o_{i,t}|context)** compares the current and rollout-generating policies’ probabilities for a generated token. **Â_{i,t} = (R_i − mean({R_i}_{i=1}^G)) / std({R_i}_{i=1}^G)** expresses how a rollout’s reward differs from its group average in units of group reward standard deviation. [A; p. 7]

The advantage is written with a token index, but its displayed formula uses the rollout reward and contains no token-specific reward. It therefore supplies the same displayed group-normalized reward signal across that rollout’s generated tokens. Zero standard deviation would make the division undefined, motivating the removal of zero-variance cases. The paper does not specify whether standard deviation uses a population or sample convention. [A/D]

## Equation 5 — Combined reward

**R_i = 0.1 R_i^format + 0.9 R_i^answer**. Format reward checks prescribed tags and ReAct sequencing; answer reward uses an LLM judge to assess correctness. The output is the scalar reward used in the relative-advantage calculation. [A; p. 7]

The weights total 1.0, with answer correctness receiving nine times the weight of format validity. That ratio is analyst-derived from 0.9/0.1 = 9. The paper does not fully define component ranges or establish that this reward prevents all reward hacking. Its rule-based label should be read alongside the explicit use of a model-based answer judge. [C/D]

## Equation 6 — Pass@1

**pass@1 = (1/n) Σ_{i=1}^n p_i**, where p_i denotes correctness of response i and n the number of evaluated responses. It measures average success for one generated answer per evaluated instance. Results are presented in percentage-style form in the tables and explicitly as percentages in Figures 4–6. [A/B; p. 8]

For k greater than one, the paper says it generates k times but does not give a complete pass@k aggregation formula in the supplied text. Figure 5 reports pass@3, so its precise aggregation should not be silently supplied from outside knowledge. No theorem or proof depends on these equations; they define interaction, training, and evaluation.

# 14. Interpretation and discussion

The strongest supported conclusion is that the integrated WebSailor post-training pipeline improves the reported information-seeking performance of the tested Qwen-family agents. Table 1, the positive RL gains, and the cold-start comparison support complementary parts of that conclusion. They do not show that harder graphs alone are sufficient, or that obfuscation alone is necessary. [D]

H1 receives indirect support: synthetic data has longer trajectories and lower expert pass rates than WebDancer-QA, while agents trained with the full pipeline perform better on hard benchmarks. A cleaner test of H1 would hold the remaining pipeline fixed while changing data topology and ambiguity. Such a controlled experiment is not reported. [D]

H2 receives more direct experimental support through Figure 6, but only for the shown Qwen-2.5-instruct-32B conditions. The conclusion that cold start is indispensable should be interpreted within the tested budgets and recipes. O5 is supported by the high SimpleQA sample scores, subject to uncertainty about scoring aggregation and random-sample variation. [D]

The paper’s superhuman language is broader than its directly documented human evidence. It reports manual difficulty observations, including generated questions not solved under typical two-hour constraints, and concludes that capabilities surpass human levels. It does not report a participant count, recruitment process, standardized human baseline, or paired statistical test. Thus the supplied work supports strong benchmark performance and an author-reported human-difficulty observation, not a fully specified general human superiority experiment. [A/D; pp. 5, 13]

For the security question, external information is operationally necessary for many target questions, and the system repeatedly integrates it into later decisions. This makes the paper useful for identifying where a security evaluation should look. It remains insufficient to infer exploitation probability, trust-boundary failure, or comparative vulnerability against direct inference. Task accuracy and security robustness are different constructs. [D]

# 15. Contributions and novelty

| Contribution type | Claimed contribution | Evidence boundary |
|---|---|---|
| Conceptual | Frame hard web reasoning as reduction of high, difficult uncertainty; distinguish three task levels | Author taxonomy, not a validated universal classification |
| Dataset/method | SailorFog-QA from expanded graphs, sampled subgraphs, and obfuscated clues | Procedure described; full size and generator settings absent |
| Supervision method | Reconstruct short action-oriented thoughts from successful expert traces | Equation 2 and procedure; no isolated reconstruction ablation |
| Training method | Small RFT cold start followed by agentic RL | Filters and Figure 6 support the tested approach |
| Algorithm | DUPO filters easy/zero-variance cases and duplicates useful batch cases | Objective and reported 2–3 times speedup; timing details absent |
| System | Integrated search/visit agent with goal-conditioned summaries | Appendix A.1/A.3 describe components and call limit |
| Empirical | Strong listed open-source results on hard benchmarks and transfer to a SimpleQA sample | Tables 1–2 and Figures 4–6 |

There is no supplied security-defense contribution, attack benchmark, formal security guarantee, or theorem. The repository link establishes a stated artifact location, not verified availability, licensing, or completeness of the implementation. [A/D; p. 1]

# 16. Limitations

## Authors’ stated limitations

1. Filtering training trajectories around 32k tokens may restrict performance on more complex problems; many analyzed failures exceed context limits, and longer inference can degrade performance. [p. 12]
2. The agent can over-think simple questions by making several calls. The authors qualify this: some extra calls perform cross-verification rather than aimless exploration. [p. 12]
3. RL is limited to 50 steps because synchronous training remains inefficient even with DUPO. [p. 12]
4. Synthesized questions may not have unique answers, although the supplied answer is asserted to satisfy the question’s conditions. [pp. 10–11]
5. Proprietary agents are not uniformly available through APIs, and some results are omitted because of cost. [pp. 8–9]
6. Full SimpleQA evaluation is considered too time-consuming, motivating a 200-question sample. [p. 11]
7. GAIA includes mathematical and computational tasks for which WebSailor was not specifically optimized. [p. 9]

## Additional evidence-based analyst observations

The paper does not provide exact full dataset size, all split counts, random seeds, hardware, model-judge details, graph transition probabilities, or clipping values. It does not isolate the effect of each pipeline component. The generated reasoning can use future observations relative to the action being justified. Tool calls are a potentially imperfect proxy for difficulty because redundant calls and multiple queries per call can change counts. [D]

The mixed provenance of proprietary baseline results limits a strict like-for-like interpretation. The SimpleQA score aggregation is unclear for some reported decimals. Figure 6 uses broken axes and unlabeled points, and Figure 1 includes configurations that differ from Table 1. The qualitative case omits substantial observations, so its claimed verification cannot be fully reproduced from the printed trace. [D]

No security attack condition is evaluated. It would be an unsupported leap to treat stronger tool-use capability, longer trajectories, or internet access as measured evidence of greater vulnerability. [D]

# 17. Threats to validity

The following labels organize analyst observations; the authors do not present this formal validity taxonomy.

**Internal validity.** The full-pipeline comparison cannot disentangle graph synthesis, clue obfuscation, reconstructed reasoning, RFT, and DUPO. Figure 6 addresses one component more directly, but differing starting policies and training histories are intrinsic to that comparison. The method’s causal story is plausible and partially supported, but not exhaustively isolated. [D]

**Construct validity.** Tool-call count measures interaction length, which may reflect difficulty, inefficient searching, or verification effort. Correctness judged by an LLM may not capture all valid answers when questions are nonunique. Pass@1 measures task completion, not security robustness. Superhuman reasoning is not operationalized by a detailed human experiment. [D]

**External validity and generalizability.** The results concern specified benchmarks, model sizes, a text-only GAIA subset, and a sampled SimpleQA set. They do not establish behavior on all web domains, languages, time periods, multimodal tasks, or adversarial environments. [D]

**Statistical conclusion validity.** No confidence intervals, error bars, repeated-run variation, or hypothesis tests are supplied. Near ties should not be assigned statistical significance. The source’s use of significantly is often qualitative; it is not accompanied by reported significance tests. [D]

**Ecological validity.** Internet grounding is a strength for realistic retrieval, but search results and pages can change. The paper does not give a complete evaluation timestamp protocol or archived replay setup. The case study illustrates live-web-style interaction but is too abbreviated to establish reproducibility of every step. [D]

**Reproducibility.** Frameworks and principal hyperparameters are named, and Appendix A describes procedures. Missing dataset counts, seeds, hardware, model roles, generator parameters, and complete trajectories prevent exact reconstruction from the supplied paper alone. Linked artifacts might add details, but were not inspected. [D]

# 18. Future work and open questions

## A. Explicit author-proposed future work

The authors propose moving to an asynchronous training framework to improve efficiency and support more extensive RL. They also propose developing more complex, higher-uncertainty tasks and pursuing broader capabilities beyond information seeking toward general superhuman performance. These are future ambitions, not completed experiments. [A; pp. 12–13]

## B. Additional analyst open questions

How much of the improvement comes from graph structure, obfuscation, thought reconstruction, RFT, or DUPO individually? Does hindsight-conditioned reconstruction improve actual decision quality beyond a simpler action-trace format? How should nonunique answers be judged? Can the reported speedup be replicated under specified hardware and equal rollout budgets? Do the simple-task improvements persist on all 4,326 SimpleQA items? [D]

For the user’s security research: what happens when search results or retrieved pages contain attacker-controlled content? Does goal-conditioned summarization alter the effect of such content? Does repeated incorporation of observations increase, reduce, or leave unchanged attack success? Can a matched model be evaluated with and without browsing under a fixed threat model? These are proposed questions, not findings from WebSailor. [D]

# 19. Terminology and notation glossary

| Term or symbol | Meaning in this paper |
|---|---|
| LLM | Large language model; generates thoughts, actions, and answers from context |
| LRM | Large reasoning model used as an expert solver |
| QA | Question answering; also a question–answer pair |
| ReAct | Named framework alternating thought, action, and observation |
| SFT | Supervised fine-tuning on provided trajectories |
| RFT | Rejection sampling fine-tuning; train on retained successful traces |
| RL | Reinforcement learning from rollout rewards |
| DUPO | Duplicating Sampling Policy Optimization |
| DAPO | Named comparison RL method; its full expansion is not supplied in the paper |
| GPRO | Spelling used in the source for the cited group-relative approach; possible naming irregularity is not silently resolved |
| CoT | Chain of thought; intermediate reasoning text |
| Short-CoT | Concise reconstructed reasoning style |
| Policy π | Model distribution used to generate actions or output tokens |
| θ / θ_old | Current and rollout-generating policy parameters |
| H_T | Accumulated interaction history |
| τ_i / τ̂_i | Original thought / reconstructed thought |
| a_i | Action, including tool call or final answer |
| o_i | Observation in Eq. 1; generated rollout tokens in Eqs. 3–4 |
| q, y | Question and corresponding answer |
| D | Training QA distribution/dataset in the objective |
| G | Rollout-group size; reported as eight |
| R_i | Combined rollout reward |
| Â_i,t | Group-relative advantage applied in the token objective |
| r_i,t | Current-to-old policy probability ratio |
| ε_low, ε_high | Lower and upper clipping parameters; numerical values absent |
| Pass@1 | Average correctness for the single-generation evaluation |
| Pass@3 | Reported three-generation metric; exact aggregation formula absent |
| Top-p | Sampling parameter; evaluation 0.95 and RL 1.0; detailed definition not supplied |
| Context window | Finite amount of interaction history available to the model |
| SPARQL | Named Wikidata query service; expansion is not supplied |
| API | Application programming interface; access constraint for some proprietary baselines |
| B | Billions in model-size labels |

Definitions beyond what the paper supports are deliberately avoided. In particular, named methods whose expansions are absent are not expanded from external memory.

# 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| WebSailor sizes | 3, 7, 32, 72 | B model-size labels | Qwen-2.5 backbones | Author-reported | pp. 3, 7 |
| Search results per query | 10 | results | Titles, snippets, URLs | Author-reported | pp. 3, 14 |
| Agent tool-call cap | 30 | calls | Qwen-Agent implementation | Author-reported | p. 14 |
| Some generated tasks | Up to 40 | calls | o3 solving examples described in introduction | Author-reported | p. 2 |
| Cold-start examples | Just over 2k | examples | Exact count absent | Author-reported | pp. 2–3 |
| Complexity filter | More than 5 | calls | Retained RFT trajectories | Author-reported | p. 6 |
| Length filter | 32k boundary | tokens | Exceeding discarded; strict boundary wording varies | Author-reported | pp. 6, 12 |
| Rollout group | 8 | rollouts | RL | Author-reported | pp. 7, 15 |
| DUPO speedup | Approximately 2–3 | times | Versus DAPO dynamic sampling | Author-reported | p. 7 |
| Reward weights | 0.1 / 0.9 | weights | Format / answer | Author-reported | Eq. 5, p. 7 |
| Evaluation temperature/top-p | 0.6 / 0.95 | parameters | Pass evaluation | Author-reported | p. 8 |
| GAIA sample | 103 | cases | Text-only validation subset | Author-reported | p. 8 |
| SimpleQA sample/full size | 200 / 4,326 | QA pairs | Random sample/full benchmark | Author-reported | p. 11 |
| RL limit | 50 | training steps | Synchronous training | Author-reported | p. 12 |
| WebSailor-72B main results | 12.0 / 30.1 / 55.0 / 55.4 | accuracy scores | English/Chinese BrowseComp, Xbench, GAIA | Author-reported | Table 1, p. 9 |
| WebSailor-32B main results | 10.5 / 25.5 / 53.3 / 53.2 | accuracy scores | Same column order | Author-reported | Table 1, p. 9 |
| WebSailor-7B English BrowseComp | 6.7 | accuracy score | ReAct | Author-reported | Table 1, p. 9 |
| DeepResearch available results | 51.5 / 42.9 / 67.4 | accuracy scores | English/Chinese BrowseComp, GAIA | Author-reported | Table 1, p. 9 |
| SimpleQA WebSailor | 93.5 / 92.8 | percent | 72B / 32B; sampled evaluation | Visually readable | Fig. 4, p. 11 |
| o4-mini dataset scores | 47.3 / 90.2 / 26.3 | accuracy scores | SailorFog/WebDancer/BrowseComp; browsing | Author-reported | Table 2, p. 10 |
| DeepSeek-R1 dataset scores | 38.9 / 84.4 / 9.5 | accuracy scores | Same browsing comparison | Author-reported | Table 2, p. 10 |
| Chinese BrowseComp advantage over Doubao | 30.1−26.0 = 4.1 | percentage points | 72B versus listed proprietary agent | Analyst-derived | Table 1, p. 9 |
| English BrowseComp deficit to DeepResearch | 51.5−12.0 = 39.5 | percentage points | Listed configurations | Analyst-derived | Table 1, p. 9 |
| Cold-start/direct-RL final English scores | Around 10–11 / 4 | percent | Final plotted points | Approximate visual estimate | Fig. 6a, p. 12 |
| SFT learning rate / RL learning rate | 5e-6 / 1e-6 | parameters | Megatron / verl | Author-reported | p. 15 |

The 40-call statement concerns the introduction’s description of challenging questions solved by o3; the 30-call cap concerns the Appendix A.3 implementation. They are different conditions and should not automatically be called contradictory. All remaining Table 1 results and Figure 5 gain annotations are preserved in their dedicated sections rather than duplicated here.

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| The pipeline targets hard uncertainty reduction | Graph sampling, obfuscation, reconstructed traces, RFT, DUPO | Method | pp. 2–7 | HIGH for what is proposed; causal explanation is partly interpretive |
| Browsing observations enter subsequent decisions | ReAct history and search/visit descriptions | Eq. 1, Appendix A.1 | pp. 3, 14 | HIGH architectural evidence; no attack measurement |
| Generated data is harder than WebDancer-QA | Lower pass rates for both browsing experts | T2/X3 | p. 10 | HIGH numerical evidence; answer ambiguity is a confound |
| SailorFog has longer trajectories | Tool-call distributions | F3/X2 | p. 10 | HIGH for reported trend; counts are a difficulty proxy |
| WebSailor-72B leads listed open-source comparisons | Highest scores in four columns | T1/X1 | p. 9 | HIGH within listed configurations; no uncertainty estimates |
| Proprietary parity is selective | 30.1 versus Doubao 26.0, but DeepResearch 42.9 | T1/X1 | pp. 9–10 | HIGH; strongest proprietary system still leads |
| Hard-task training preserves simple-task ability | 93.5/92.8 on SimpleQA sample | F4/X4 | p. 11 | HIGH sample result; full set and aggregation details absent |
| RL improves every plotted condition | Sixteen positive gain annotations | F5/X5 | p. 11 | HIGH observations; broader stability mechanism is interpretation |
| Cold start helps in the tested ablation | Higher cold-start lines | F6/X6 | p. 12 | MEDIUM numerical precision; HIGH qualitative direction |
| DUPO is reported faster | Approximately 2–3 times prose claim | Method | p. 7 | MEDIUM evidentiary strength; timing protocol absent |
| Context and synchronization constrain the system | Explicit limitations paragraph | §5.4 | p. 12 | HIGH author acknowledgment |
| Architecture is relevant to security analysis | External pages, summarizer, tool-response context | Method/Appendix | pp. 3, 14 | MEDIUM analyst inference; vulnerability magnitude UNKNOWN |

# 22. Very simple explanation — Explain Like I’m 15

Imagine trying to identify someone from several vague clues scattered across different websites. Searching one clue may produce many unrelated results. You need to find a promising lead, check it against the other clues, and change direction when the evidence does not fit. WebSailor trains an AI to do this kind of investigation.

The researchers create difficult practice questions from networks of connected facts, then make some clues less precise. They obtain successful search histories from stronger models, rewrite the reasoning into shorter explanations, and use those examples to teach the agent the basics. Reinforcement learning then rewards useful answers and helps improve its choices.

The trained agents perform better than the open-source comparisons listed in the paper. They also answer many simple factual questions successfully. But the best proprietary comparison still wins by a large margin on some benchmarks, and the agent can run out of context or spend extra time checking easy answers.

For your security question, this paper shows that a web agent receives information from search results and webpages, sometimes through another model that summarizes them. Those are useful places to examine for possible security problems. The paper does not attack those places or measure vulnerability, so it cannot prove that a browsing agent is less secure than a model answering on its own.

# Completeness Audit

The inventory is the denominator for this audit. All supplied pages were read as text; only the ten listed image pages were visually inspected. Coverage refers to the supplied paper, not linked artifacts or the contents of cited works.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title and publication identifiers | Yes, text and image | Yes | Fully represented | Original title retained; arXiv version/date identified below |
| Author list and affiliation | Yes | Yes | Represented in compressed form | Listed below; author-role footnote accounted for |
| Abstract | Yes, text and image | Yes | Represented in compressed form | Pipeline and headline claims in sections 1, 4, 15 |
| §1 Introduction | Yes | Yes | Represented in compressed form | Motivation, task gap, 40 calls, just over 2k examples |
| §2 Problem Definition | Yes | Yes | Fully represented | ReAct, tools, history, naming/notation caveats |
| §3 Training Data Synthesis | Yes | Yes | Fully represented | Both QA and supervision branches |
| §3.1 SailorFog-QA | Yes | Yes | Fully represented | Graphs, levels, obfuscation; examples compressed |
| §3.2 Reconstructing Reasoning | Yes, p. 6 text-only | Yes | Fully represented | Future-observation conditioning noted |
| §4 Training overview | Yes, text-only on p. 6 | Yes | Fully represented | RFT then RL |
| §4.1 RFT | Yes, text-only | Yes | Fully represented | Tags, three filters, masked observations |
| §4.2 DUPO | Yes, mixed text/visual | Yes | Fully represented | Selection, duplication, objective, reward |
| §5.1 Setup | Yes | Yes | Fully represented | Models, baselines, datasets, evaluation parameters |
| §5.2 Main Results | Yes | Yes | Fully represented | All Table 1 rows retained |
| §5.3 Complexity analysis | Yes | Yes | Fully represented | X2, Figure 3 |
| §5.3 Dataset pass rates | Yes | Yes | Fully represented | X3, Table 2, ambiguity caveat |
| §5.3 Simple-task compatibility | Yes | Yes | Fully represented | X4, Figure 4, sample size |
| §5.3 Pass@1 versus Pass@3 | Yes | Yes | Fully represented | X5, all sixteen gain annotations |
| §5.3 Cold-start ablation | Yes | Yes | Fully represented | X6, Figure 6, approximate point values |
| §5.4 Limitations/Future Work | Yes | Yes | Fully represented | Context, over-thinking, 50 steps, asynchronous plan |
| §6 Related Work | Yes, mixed visual/text-only | Yes | Represented in compressed form | Benchmark and agent categories, author-attributed positioning |
| §7 Conclusion | Yes, text-only | Yes | Represented in compressed form | Pipeline and broader ambitions; human claim qualified |
| Objectives O1–O5 | Yes | Yes | Fully represented | Analyst-organized objectives, not invented formal questions |
| Hypotheses H1–H2 | Yes | Yes | Fully represented | Explicit core hypothesis and cold-start position distinguished |
| User security research question | Applicable lens | Yes | Fully represented | Clearly separated from the paper’s actual study |
| X1–X7 | Yes | Yes | Fully represented | Seven distinct experiments/analyses registered |
| Figures 1–6 | Yes, visual | Yes | Fully represented | All panels and significant encodings addressed |
| Figure 2 diagram | Yes, visual | Yes | Fully represented | Conceptual sampling/obfuscation flow |
| Tables 1–2 | Yes, text and visual | Yes | Fully represented | All table values retained |
| Equations 1–6 | Yes | Yes | Fully represented | Eq. 2 text-only; undefined/reused symbols flagged |
| Appendix A.1 Tools | Yes, text-only | Yes | Fully represented | Google, Jina, Qwen-2.5-72B summarizer |
| Appendix A.2 QA Construction | Yes, text-only | Yes | Fully represented | Five-step procedure; missing probabilities/counts noted |
| Appendix A.3 ReAct Trajectories | Yes, text-only | Yes | Represented in compressed form | Qwen-Agent, 30-call cap, tags |
| Appendix A.4 Training Details | Yes, text-only | Yes | Fully represented | All stated numerical training parameters retained |
| Appendix A.5 Case Study | Yes, text-only | Yes | Represented in compressed form | Search refinement, clue verification, final computer answer |
| Numbered algorithms/theorems | None found | Not applicable | Fully represented | No numbered algorithm or formal theorem supplied |
| Major contributions | Yes | Yes | Fully represented | Conceptual, data, supervision, RL, system, empirical |
| Author-stated limitations | Yes | Yes | Fully represented | Primary §5.4 limits and additional explicit constraints |
| Author-role and repository footnotes | Yes | Yes | Represented in compressed form | Roles and links acknowledged without external inspection |
| References, pp. 20–23 | Yes, text-only | Yes | Represented in compressed form | Categories and relevant positioning; individual bibliography entries not reproduced |
| Decorative logos/header rules | Yes where visual | Accounted for | Inspected but deliberately omitted as non-substantive | No scientific content inferred from styling |
| Separate supplementary material | Not supplied | Accounted for | Missing from supplied material | No supplement claimed reviewed |
| External repository/site contents | Not accessed | Accounted for | Inaccessible within the requested source boundary | Paper descriptions only |

## Bibliographic inventory details

The original title is **WebSailor: Navigating Super-human Reasoning for Web Agent**. The authors are Kuan Li, Zhongwang Zhang, Huifeng Yin, Liwen Zhang, Litu Ou, Jialong Wu, Wenbiao Yin, Baixuan Li, Zhengwei Tao, Xinyu Wang, Weizhou Shen, Junkai Zhang, Dingchu Zhang, Xixi Wu, Yong Jiang, Ming Yan, Pengjun Xie, Fei Huang, and Jingren Zhou. The affiliation is Tongyi Lab, Alibaba Group. Page 1 identifies arXiv:2507.02592v1 [cs.CL], dated 3 July 2025, and displays 2025-07-04 in the header. No conference or journal venue is supplied for this paper. The first five starred authors are marked equal core contributors; Kuan Li, Zhongwang Zhang, and Huifeng Yin are project leaders; Huifeng Yin and Yong Jiang are corresponding authors. No keywords list is supplied.

## Case-study coverage detail

Appendix A.5’s question asks for the first computer jointly purchased by a developer and their father. The displayed trace starts with broad combinations of solar-fridge, rustic-lifestyle, conference, and caving clues; focuses on the distinctive phrase about a hole in the map; visits an interview; identifies Joey Hess; searches to confirm the fridge; investigates conference memories and caving; and visits a personal Atari blog entry before answering Atari 130XE. The final thought says the purchase occurred around 1986. These are author-displayed case contents, not independently verified biographical facts.

The case includes nine tool-action steps and a tenth final-answer step. Observations are repeatedly abbreviated with ellipses. The Step 4 reference to an LWN article is not established by the visible preceding excerpt, and the final trace does not fully display evidence confirming every clue, notably caving. An extracted Step 9 tool call contains irregular punctuation, and the final answer tag appears unclosed or repeated rather than cleanly closed. Because Appendix A.5 is text-only here, those formatting irregularities cannot be confidently separated into native-source errors versus extraction errors. They do not justify a claim that the implemented framework accepts malformed calls.

## Missing or inaccessible material

No supplied text pages are missing. Direct page images for pages 5, 6, and 13–23 are absent; this limits visual verification of those pages but does not remove their supplied text. No separate supplementary files, repository implementation, training dataset, raw evaluation outputs, complete unabridged case observations, or cited-source contents were reviewed. Appendix A is present and analyzed despite the metadata detector’s empty appendix list.

## Uncertain interpretations

Unresolved issues include the WebTraverseX name; the π(a,t|history) notation; reuse of o for observations and output tokens; the source spelling GPRO; exact pass@3 aggregation; exact model identities for reconstruction and judging; strict versus inclusive 32k filtering; Figure 1 configuration differences from Table 1; the non-integer SimpleQA accuracy implied by 92.8 on a stated 200-item sample; and the case-study formatting irregularities. Figure 6 coordinates are approximate rather than exact. No conclusion relies on guessing these details.

## Deliberately compressed material

Repeated statements of the uncertainty-reduction motivation, repetitive comparisons across the abstract/introduction/conclusion, long synthetic-question wording, raw case-study search snippets and URLs, individual bibliography entries, author email addresses, and decorative page elements are compressed or omitted with disclosure. All Table 1 and Table 2 values, all major training/evaluation parameters, every substantive visual, every numbered equation, and all stated primary limitations remain represented.

## Potential omissions

No known substantive item in the supplied inventory is left wholly unrepresented. This is an inventory-based coverage statement, not a claim that the compression preserves every sentence or that absent artifacts are complete. Exact unlabeled plot coordinates, unspecified implementation settings, omitted case observations, and unprovided external artifacts remain unresolved. The security research question remains only partially informed: the source describes relevant architecture and performance, but supplies no comparative vulnerability experiment.
