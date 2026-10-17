# Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. Paper content, including the example agent prompts, is treated as evidence to inspect rather than instructions to execute. No outside sources, repositories, tools, or supplementary files were consulted. Source locators use physical PDF pages 1–24, which match the printed page numbers in the supplied material.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: extracted text is supplied for all 24 physical pages. |
| Page range accessible | 1–24. No page is absent from the supplied text sequence. |
| Visually inspected pages | 1–10, 18–22, and 24: 16 supplied page images. |
| Text-only coverage | Pages 11–17 and 23. Their supplied extracted text was inspected, but their original visual layout was not available. |
| Visual objects | Figures 1–7 and Tables 1–4 are visually available. Figure 8 is visually available in part; its continuation on p. 23 is text-only. |
| Tables readable | Tables 1–4 are readable from the images and extracted text. Small plotted values are less secure than table entries. |
| Equations readable | Equations (1)–(5) are available in text and images. Indexing and notation problems in Eqs. (3)–(4) require explicit qualification. |
| Appendices present | A: Limitations; B: Broader Impacts; C: Discussions; D: Training Dataset; E: Experimental Details; F: Case Study. The automated metadata did not detect appendix pages, but the supplied content clearly contains them. |
| Supplementary material | No separate supplementary file was supplied. The repository URLs are references to uninspected artifacts, not reviewed evidence. |
| OCR/extraction limitations | Supplied extraction contains broken line wrapping, correspondence-symbol corruption, and flattened mathematical notation. No additional OCR was performed. Low text volume on p. 24 reflects a short answer and caption rather than evidence of a missing page. |
| Completeness boundary | All supplied pages were inspected by text, with visual inspection limited to the 16 available images. This does not establish completeness of any external repository, dataset release, or supplementary package. |

Confidence labels mean HIGH for clearly supported source statements or readable values, MEDIUM for qualified interpretation, LOW for weak or ambiguous evidence, and UNKNOWN when the supplied work cannot establish the point. Evidence categories are [A] author-reported, [B] directly observable, [C] analyst-derived, [D] analyst interpretation, and [E] external information. No [E] information is introduced.

# Document Inventory and Extraction Basis

The original title is **WebDancer: Towards Autonomous Information Seeking Agency**. The authors are Jialong Wu, Baixuan Li, Runnan Fang, Wenbiao Yin, Liwen Zhang, Zhengwei Tao, Dingchu Zhang, Zekun Xi, Gang Fu, Yong Jiang, Pengjun Xie, Fei Huang, and Jingren Zhou, affiliated with Tongyi Lab, Alibaba Group. The title page displays 2025-05-28 and identifies arXiv:2505.22648v3, dated 10 Aug 2025. These are two displayed dates; a conference or journal publication venue is not supplied. The equal-core-contributor footnote identifies the first four authors and names Jialong Wu and Wenbiao Yin as project leaders. Correspondence symbols in extraction are corrupted, although the title-page image marks corresponding authors.

The document is an empirical machine-learning and web-agent systems paper with dataset-construction contributions. It is not a security experiment or a theoretical proof paper. No keywords, formal numbered research questions, formal hypotheses, theorems, or separate numbered pseudocode algorithm are supplied.

| Inventory ID | Original item | Source |
|---|---|---|
| ABS | Abstract | p. 1 |
| S1 | §1 Introduction | pp. 1–2 |
| S2.1 | §2.1 QA Pairs Construction: CRAWLQA and E2HQA | pp. 3–4 |
| S2.2 | §2.2 Agent Trajectories Rejection Sampling | pp. 4–5 |
| S3.1 | §3.1 Agent Supervised Fine Tuning | pp. 5–6 |
| S3.2 | §3.2 Agent Reinforcement Learning: DAPO, rollout, reward | pp. 6–7 |
| S4.1 | §4.1 Experimental Setup | pp. 7–8 |
| S4.2 | §4.2 Experimental Results | p. 8 |
| S5 | §5 Analysis: dataset quality, cold start, transfer, RL, instability | pp. 8–10 |
| S6 | §6 Related Works | p. 10 |
| S7 | §7 Conclusion | p. 11 |
| REF | References | pp. 12–16 |
| A | Appendix A Limitations | p. 17 |
| B | Appendix B Broader Impacts | p. 17 |
| C.1/C.2 | Concurrent work and post-trained agentic models | p. 18 |
| D | Training Dataset and open-only datasets | pp. 18–19 |
| E.1–E.4 | Benchmarks, baselines, implementation, sampling prompts | pp. 19–21 |
| F | Case Study | pp. 21–24 |
| F1–F8 | Figures 1–8 | pp. 3, 5, 8, 9, 10, 20, 21, 21–24 |
| T1–T4 | Tables 1–4 | pp. 7, 8, 9, 18 |
| E1–E5 | Equations (1)–(5) | pp. 4, 6, 6, 6, 7 |
| X1–X9 | Main benchmarks; BrowseComp; data ablation; RL metrics; cold-start ablation; CoT transfer; training dynamics; temperature; memorization | pp. 7–10 |
| X10 | Illustrative case trajectory, not a controlled experiment | pp. 21–24 |

The explanation below represents all these substantive items. Bibliographic entries, repeated prompt wording, and long example reasoning traces are compressed with disclosure. Numerical values are traced to their conditions; plotted approximations are separated from exact labels.

# 1. Plain-Language Orientation

[A] WebDancer is an attempt to train a language model to investigate questions on the web through repeated searches and page visits. A conventional direct answer asks the model to produce a response from its existing capabilities. This agent instead generates a thought, chooses a tool action, reads the returned observation, and repeats until it answers. The paper studies how to build this behavior through data construction and training, rather than solely through a complicated hand-written prompting workflow.

The problem is that difficult information-seeking questions often require several connected steps: identify an entity, find a relevant source, follow a link, resolve missing information, and combine evidence. According to the authors, existing data are frequently too shallow, while difficult benchmarks are too small to serve as sufficient training corpora. Simply training tool syntax also does not necessarily teach long sequences of effective decisions.

The researchers construct two synthetic question–answer datasets, generate candidate agent trajectories, filter those trajectories, conduct supervised fine-tuning for a cold start, and then apply on-policy reinforcement learning. Their central contribution is this integrated four-stage pipeline. WebDancer is its implementation using a ReAct-style thought–action–observation loop.

The strongest WebDancer row in Table 1 uses QwQ-32B and obtains 51.5% on GAIA and 47.9% on WebWalkerQA under the reported Pass@1 evaluation. The same backbone with vanilla ReAct obtains 37.8% and 24.1%. The paper also reports best-model Pass@3 scores of 64.1% and 62.0%, respectively. These are different evaluation conditions and must not be interchanged.

[D] For the user's security research question, the paper supplies useful architectural evidence: external web observations influence subsequent model actions, tool responses enter dialogue context, and a summarizer mediates page content. These features identify interfaces deserving security investigation. However, the study does not measure attacks or establish that web agents are more vulnerable than standalone large language models. Its direct comparisons concern task success, not adversarial susceptibility.

# 2. Document Roadmap

The introduction defines autonomous information-seeking agency and motivates both better data and better training. Section 2 constructs the data foundation: §2.1 explains the two question-generation pipelines; §2.2 explains how trajectories are sampled and filtered. Section 3 turns those trajectories and remaining question–answer pairs into a two-stage learning system, with supervised fine-tuning followed by reinforcement learning.

Section 4 evaluates performance on GAIA and WebWalkerQA and adds BrowseComp results. Section 5 asks why the pipeline works and where it struggles: it examines dataset composition, filtering, cold-start training, reasoning-style transfer, reinforcement-learning gains, action and thought length, temperature sensitivity, and a memorization stress test. Section 6 positions the approach relative to prior work, and §7 concludes.

Appendix A materially qualifies the results through tool, task, compute, utilization, and hallucination limitations. Appendix B discusses misinformation and misuse. Appendix C explains differences from concurrent systems. Appendix D provides training counts and repetition filtering. Appendix E supplies evaluation subsets, implementation parameters, and trajectory prompts. Appendix F illustrates a multi-step question with a complete example trajectory. These appendices are necessary to interpret the main text faithfully; they are not optional background.

# 3. Background and Context

[A] A **large language model (LLM)** generates language and, here, structured actions. A **large reasoning model (LRM)** is the paper's category for reasoning-oriented models such as QwQ. The authors distinguish short and long **chain of thought (CoT)**, meaning generated intermediate reasoning associated with solving the task. The work uses these reasoning traces as trajectory supervision; they are not independently verified explanations of every internal computation.

**ReAct** is the named framework used to interleave reasoning and acting. Its trajectory contains **Thought**, **Action**, and **Observation** rounds. An action specifies a tool and its parameters; an observation is the returned information. **Agency**, as used here, means the model's ability to decide successive steps and tool uses toward a goal.

**Question answering (QA)** provides a question and reference answer. **Multi-hop** questions require linked information steps. **CRAWLQA** builds questions from browsed web content. **E2HQA**, easy-to-hard QA, rewrites questions to require additional subproblems while retaining the answer.

**Supervised fine-tuning (SFT)** trains on collected examples of the desired behavior. **Rejection sampling fine-tuning (RFT)** refers to using sampled, filtered trajectories for that supervised stage. **Reinforcement learning (RL)** adjusts a policy using rewards from generated executions. The policy is the model's conditional procedure for generating thoughts and actions. **On-policy** learning uses executions sampled from the policy being trained; the paper contrasts this with off-policy approaches.

**Retrieval-augmented generation (RAG)** is a baseline category that supplies retrieved information for answering. The paper's No Agency group includes both direct base-model use and RAG rows, so No Agency should not be equated with every possible definition of a completely disconnected standalone model.

**LLM-as-Judge** means another model evaluates answer correctness. **Pass@1** is the reported one-attempt success metric. **Pass@3** describes success with three attempts, but the supplied paper does not give a full estimator formula or selection protocol. **Cons@3**, consistency over three attempts, is explicitly defined: one correct answer gives 1/3, two give 2/3, and three give 1. The reported averages therefore distinguish obtaining a correct answer at least once from obtaining correct answers repeatedly.

The paper does not define a cybersecurity threat model, prompt-injection taxonomy, attacker success metric, or security boundary. Such concepts cannot be attributed to its experiments.

# 4. Research Problem and Gap

**Existing problem [A]:** difficult real-world information seeking requires web perception, long-horizon reasoning, and sequential decisions. The agent must obtain relevant evidence and decide what to do next rather than only answer an isolated prompt.

**Shortcomings attributed to previous approaches [A]:** training-free prompting methods do not fully exploit reasoning-model capabilities; existing SFT/RL datasets often contain relatively simple questions; prior training can generalize poorly in complex search environments; and RL from the beginning can spend early effort learning tool instructions rather than higher-level behavior. These are the authors' characterizations of cited work, not an independent assessment of that literature.

**Data gap [A]:** challenging benchmark datasets are small. The introduction cites 466 GAIA examples, 680 WebWalkerQA examples, and 1,266 BrowseComp examples as context. These totals are not all experimental sample sizes. In particular, WebDancer's reported GAIA experiments use a 103-question text-only validation subset.

**Training gap [A]:** the authors seek a scalable process that combines high-quality demonstrations with RL that can exploit QA pairs left out of the SFT dataset. They also want compatibility with both instruction-oriented LLMs and reasoning-oriented LRMs.

**Scope:** the implemented agent has two information-seeking tools and a terminating answer action. Its main evaluations concern short-answer web QA, not comprehensive document writing, general browser manipulation, purchasing, credential use, or security testing. Appendix A explicitly treats richer tools and long-form research as future extensions.

# 5. Research Questions / Objectives / Hypotheses

No formal numbered research questions or preregistered hypotheses appear in the supplied work. The explicit overall objective is to unlock autonomous multi-turn information-seeking agency and provide a systematic guideline for building agents from data and training perspectives (p. 2).

The following objective register organizes author-stated aims without inventing formal questions:

| ID | Author objective or analysis aim | Evidence and evaluation |
|---|---|---|
| O1 | Construct diverse, challenging deep information-seeking QA pairs. | CRAWLQA/E2HQA, Fig. 1, dataset ablation Fig. 3. |
| O2 | Generate high-quality short- and long-CoT trajectories. | §2.2, filters, Tables 3–4. |
| O3 | Teach multi-step instruction following through a cold start. | §3.1; RL-only comparison reporting 5% GAIA Pass@3. |
| O4 | Improve decision-making/generalization with on-policy RL. | §3.2, Table 1, Figs. 4–5. |
| O5 | Examine reasoning-pattern transfer between model types. | Table 3 and the mixed-CoT footnote. |
| O6 | Understand unstable agent performance in changing environments. | Temperature comparison and memorization stress test. |

[D] The supplied security research question is an external analytical lens chosen by the user, not a question the authors directly test. A defensible use of this paper is to identify the agent's external-input and action interfaces and its acknowledged reliability problems. A claim about comparative vulnerability would require evidence not supplied here.

# 6. Assumptions / Threat Model

[A] The operational system assumes a language model can generate usable thought/action sequences, that search and visit tools return relevant information, and that a summarizer can convert visited content into evidence and a summary. It uses reference answers and model judges to filter or reward correctness. E2HQA assumes that question rewriting can preserve the original answer while increasing the required reasoning depth. The authors state that this preservation occurs, but the supplied material does not describe an independent audit measuring its rate.

The web is described as dynamic, non-stationary, and partially observable. Information returned at one time may therefore differ from information returned later. The history supplied to the agent includes previous outputs and tool observations. In long-CoT trajectory generation, earlier thoughts are deliberately withheld from the next QwQ-Plus inference, while previous actions and observations remain available.

No attacker capabilities, adversarial content placement, protected assets, credential boundaries, permissions, sandbox escape conditions, or attack success criteria are specified. The Appendix A Python sandbox is a proposed future tool, not an evaluated current component.

[D] Operational reliance should not be mistaken for a proven security trust assumption. The paper relies on summarizers and judges as parts of its learning/evaluation process, but does not establish that they are trustworthy under malicious input. Likewise, representing tool responses as user messages is an implementation fact; it is not evidence that these responses have the user's authority, or that any particular injection attack succeeds.

# 7. Methodology

## 7.1 Study design and four-stage pipeline

[A] The study combines synthetic dataset construction, demonstration generation, supervised policy training, and on-policy RL, followed by benchmark comparisons and targeted ablations. The four stages are: create QA pairs; sample/filter trajectories; perform SFT for format and behavioral initialization; perform RL for stronger decisions and generalization. Figure 2 connects the stages through shared datasets and policy models.

## 7.2 CRAWLQA

The authors collect root URLs from official and knowledgeable websites, including arXiv, GitHub, and wiki sources. They recursively follow accessible hyperlinks to obtain subpages, mimicking browsing. GPT-4o generates QA pairs from the collected content using prompted question types such as COUNT, MULTI-HOP, and INTERSECTION. Figure 1 illustrates a question about a game ranked fourth in the Godot XR Game Jam February 2025 but absent from the 2024 Godot Games showreel; the displayed answer is Keziah's House.

The intention is to construct questions grounded in information distributed across accessible pages. The supplied material does not specify the full URL inventory, crawl depth limits, site-selection sampling distribution, access permissions, licensing, extraction cleaning, deduplication, or benchmark-overlap checks. Website examples establish intended sources, not a complete reproducible crawling specification.

## 7.3 E2HQA

The starting questions are SimpleQA-style QA pairs whose answers are concise fact-seeking entities. At iteration n, an entity E_n in question Q_n is selected. An LLM constructs a search query about that entity, retrieves related information, and reformulates the entity into a descriptive subquery R_n. Replacing the original entity with this description creates Q_(n+1), which requires resolving the added subproblem before answering the original question.

The authors intend the answer to remain unchanged. Repeating the replacement controls complexity through the number of rewriting iterations. Figure 1 starts with the 2010 IEEE Frank Rosenblatt Award recipient and progressively substitutes descriptions; the displayed answer remains Michio Sugeno. The construction examples are evidence of the procedure, not independently verified factual claims about those external events.

## 7.4 Agent interface and trajectory generation

The explicit action names are search, visit, and answer (§2.2, p. 4). Search parameters are described as query and filter_year; visit parameters as goal and url_link. Search observations contain top-10 titles and snippets. Visit observations contain evidence and a summary generated by summarizer M_s. The answer action terminates execution. The introduction's click terminology appears to refer to browsing/visiting, but the formal action list says visit; the naming is not perfectly consistent.

GPT-4o supplies short-CoT ReAct trajectories. QwQ-Plus supplies long-CoT trajectories by repeatedly receiving earlier actions and observations, excluding earlier thoughts from subsequent inference. Each step's reasoning content is nevertheless retained in the completed training trajectory. Appendix D later refers more generally to QwQ or GPT-4o as trajectory generators; the precise distinction among QwQ, QwQ-Plus, and QwQ-32B is not fully documented.

Rejection sampling is performed up to N = 5 times per constructed QA instance. A three-stage funnel filters trajectories: validity control removes format failures; correctness verification retains answers judged correct by GPT-4o; quality assessment checks repetition, hallucination, information non-redundancy, goal alignment, and logical reasoning/accuracy. Appendix D limits occurrence of 10-grams to a threshold of 4.

A substantial inconsistency must remain visible: p. 5 literally says to filter out trajectories with more than two actions, but Table 4 reports average action counts of 4.56 for short-CoT and 2.31 for long-CoT data. If those means describe the same filtered trajectories and the action count has the same definition, both cannot satisfy a strict upper limit of two. The source does not resolve whether the sentence has a directional error, describes a different subset, or uses a different count.

## 7.5 Supervised fine-tuning

Training trajectories use <think>, <tool_call>, <tool_response>, and <answer> boundaries. The policy learns to alternate model reasoning and structured tool calls, ending with an answer. Observation tokens remain in context but their loss contributions are masked out. Thus the model is conditioned on external information without being trained to generate that information as its own output. This distinction matters because the paper separately identifies simulated observations as a hallucination problem.

Short-CoT SFT has 7,678 examples; long-CoT SFT has 6,550. Qwen-7B and Qwen-32B use short-CoT datasets; QwQ-32B uses long-CoT. Appendix D reports 40K E2HQA samples and 60K CRAWLQA samples before the described trajectory-generation/filtering process. These raw QA counts, filtered SFT counts, and RL-use counts are distinct stages, not interchangeable dataset totals.

## 7.6 Reinforcement learning

The algorithm is Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO). It generates groups of candidate executions, assigns rewards, calculates relative advantages within groups, and maximizes a clipped policy objective. Optimization applies to model-generated tokens, excluding tool responses, while the context includes tool responses.

Dynamic sampling removes question groups whose observed accuracy is either zero or one, retaining mixed-success groups. The authors motivate this as a way to use remaining synthetic QA pairs while ignoring unreliable training signals. [D] A group with no successful answers is not necessarily an invalid question, and mixed success is not proof of a valid question; the procedure is a learning-selection mechanism rather than a documented ground-truth validity test.

The binary format score is 1 only when the entire output and JSON tool calls conform to the required structure. The binary answer score is 1 when a model judge considers the answer correct. Their weighted sum gives 0.1 to format and 0.9 to answer correctness. The judge used for RL is based on Qwen-72B-Instruct; correctness filtering earlier uses GPT-4o. Those roles must not be merged.

## 7.7 Implementation and resources

Appendix E.3 states that the system uses Qwen-Agent and the verl RL framework. Training uses multi-turn chatml: tool responses are user messages; generated thoughts and actions are assistant messages. The summarizer is Qwen-2.5-72B. RL has 16 rollouts per group. Inference uses temperature 0.6 and top-p 0.95; repetition penalty is 1.1 for the LRM and 1.0 for the LLM. RL rollouts use temperature 1.0 and top-p 1.0.

The hardware statement is '32 nodes with 8 NVIDIA H20 (96GB).' [D] This plausibly describes eight GPUs per node, but the sentence does not explicitly say per node. A total GPU count is therefore not calculated as a confirmed fact. The source does not provide optimizer details, learning rates, batch sizes, clipping values, seed lists, complete training durations, per-query latency, or monetary costs.

## 7.8 Evaluation data, baselines, and statistical procedures

Experiments use 103 GAIA text-only validation questions and 680 WebWalkerQA test questions. GAIA results are split into Levels 1–3; WebWalkerQA into Easy, Medium, and Hard. The source does not give subset counts for those difficulty categories. BrowseComp and BrowseComp-zh provide additional challenging evaluations, but their evaluated sample counts are not stated in the supplied experiment details.

Baselines include direct model use, RAG, OpenAI Deep Research, Search-o1, R1-Searcher, WebThinker Base/RL, SimpleDeepSearcher, and vanilla ReAct. WebThinker results were reproduced using Google Search, according to Appendix E.2. Dashes indicate results that are not reproducible or not reported; the table does not distinguish these explanations cell by cell. No confidence intervals, error bars, statistical tests, or significance levels are provided for the reported performance comparisons.

# 8. Experiments / Analyses

| ID | Purpose, setup, and principal result | Caveat |
|---|---|---|
| X1 | Main task-success comparison on 103 GAIA and 680 WebWalkerQA questions using Pass@1 and model judging. Table 1 compares model backbones and frameworks. QwQ-32B WebDancer: 51.5/47.9; vanilla ReAct: 37.8/24.1. | Framework comparisons mix model sizes and training arrangements; no uncertainty estimates. |
| X2 | Harder browsing evaluations on BrowseComp English and Chinese using Pass@1/Pass@3. Table 2: WebDancer 3.8/7.9 and 18.0/31.5. | Exact model configuration and subset sizes are not explicit in the table. |
| X3 | QwQ data-composition/filtering ablation on GAIA. Fig. 3 compares Open-only, Crawl-only, E2H-only, All, Final. Final uses 6,550 items and visually exceeds All using 17,764. | Dataset size and composition change together; plotted heights are approximate. |
| X4 | SFT-to-RL evaluation using Pass@1, Pass@3, Cons@3 on GAIA. Fig. 4 displays positive gains for 7B, 32B, QwQ. | Three-attempt evaluation is described, but repeated training-seed variation is not. |
| X5 | QwQ RL-only cold-start comparison. The text reports only 5% Pass@3 on GAIA without the demonstrated cold-start pipeline. | Detailed matched budget, stopping condition, and full run configuration are absent. |
| X6 | Transfer of short/long-CoT data across Qwen2.5-7B, Qwen2.5-32B, QwQ-32B. Table 3 reports success, consistency, invalid rate. | Longer reasoning improves some scores while sharply increasing invalid outputs. |
| X7 | Training progress and behavioral length. Fig. 5a plots DAPO steps; Fig. 5b compares Base/SFT/RL action count and reasoning length, described for Qwen-32B. | Not all panels' exact model settings and length units are specified. |
| X8 | Temperature changes 0.5/0.6/0.7 on GAIA, Fig. 5c. The authors describe minimal effect on final performance. | Limited tested range; no uncertainty bands or controlled web snapshots. |
| X9 | Memorization stress test: Qwen-7B fine-tuned on 69 correct GAIA-development trajectories for 10 epochs, evaluated on the same set; greedy decoding obtains 37.4%. | This is same-set memorization analysis, not held-out generalization. |
| X10 | One illustrative GAIA case: identify a nonnative clownfish occurrence and obtain its location's ZIP code; final answer 34689. | A single selected example; its Step 2 thought abruptly discusses penguins. |

The authors relate X1–X4 to overall pipeline effectiveness, X5 to SFT necessity, X6 to reasoning transfer, X7 to richer agent behavior, and X8–X9 to deployment instability. The work does not conduct an attack experiment, adversarial ablation, or vulnerability comparison.

# 9. Results

## 9.1 Main benchmark improvements

[A/B] Table 1 gives the following directly comparable same-backbone ReAct results, in percent under Pass@1:

| Backbone | GAIA vanilla ReAct | GAIA WebDancer | WebWalkerQA vanilla ReAct | WebWalkerQA WebDancer |
|---|---:|---:|---:|---:|
| Qwen-2.5-7B | 18.4 | 31.0 | 24.2 | 36.0 |
| Qwen-2.5-32B | 31.0 | 40.7 | 31.9 | 38.4 |
| QwQ-32B | 37.8 | 51.5 | 24.1 | 47.9 |

[C] The improvements are 12.6 and 11.8 percentage points for 7B, 9.7 and 6.5 points for Qwen-32B, and 13.7 and 23.8 points for QwQ-32B. Each is WebDancer minus vanilla ReAct; for example, 47.9 − 24.1 = 23.8 percentage points. These are not relative percentage improvements.

The QwQ WebDancer row exceeds GPT-4o vanilla ReAct's 34.6% GAIA and 33.8% WebWalkerQA scores. It does not exceed OpenAI Deep Research's reported 67.4% GAIA average. The absence of a Deep Research WebWalkerQA score prevents that comparison. On GAIA Level 3, QwQ Base and WebDancer both report 25.0%; on Level 1, Qwen-32B vanilla ReAct and WebDancer both report 46.1%. Thus aggregate gains do not imply gains in every difficulty cell.

## 9.2 Broader results and remaining difficulty

[A] Best-model Pass@3 is 64.1% on GAIA and 62.0% on WebWalkerQA, as stated on p. 8. Table 2 reports WebDancer Pass@1/Pass@3 of 3.8/7.9 on BrowseComp English and 18.0/31.5 on BrowseComp-zh. The authors describe these as strong relative performance. [D] Absolute success remains low on these harder evaluations, particularly English; this qualifies the idea of broadly robust autonomous research.

## 9.3 Data quality and cold start

[A/B] Figure 3 supports the authors' claim that filtered data can outperform a larger unfiltered combination. It compares Open-only 1,308, Crawl-only 9,662, E2H-only 2,485, All 17,764, and Final 6,550. [C] The three named source counts sum to 1,308 + 9,662 + 2,485 = 13,455, which differs from All's 17,764 by 4,309. The paper does not explain this difference. It could reflect other sampling or composition decisions, but choosing an explanation would be speculation.

The reported RL-only QwQ result of 5% GAIA Pass@3 supports the practical importance of the described cold start under that experiment. It does not prove that all possible RL-only designs are incapable of learning web agency.

## 9.4 Reasoning transfer and invalid outputs

[A/B] Table 3 shows that long-CoT training raises Pass@3 for all three listed models, but invalid rate rises from 0.65% to 21.36% for Qwen-7B, from 4.20% to 13.59% for Qwen-32B, and from 0.97% to 13.27% for QwQ. Qwen-7B consistency decreases from 22.33 to 21.00 despite its Pass@3 increase. The authors connect invalid outputs to repetition and context-limit overruns, particularly in smaller models. This is reliability evidence, not measured adversarial exploitation.

## 9.5 RL gains and environmental instability

Figure 4 labels SFT-to-RL improvements. For Pass@1, the gains are +7.70, +5.80, +1.95 for 7B, 32B, QwQ; for Pass@3, +2.90, +5.80, +0.97; for Cons@3, +2.67, +8.68, +1.74. The modest QwQ improvements motivate the authors' suggestion of limited further on-policy benefits for LRMs, possibly because of sparse rewards in long trajectories. This proposed mechanism was not isolated experimentally.

Figure 5 shows rising performance with more DAPO steps and longer reasoning with SFT/RL. The temperature comparison does not eliminate instability. The 37.4% memorization-test result shows that even revisiting a small correctly demonstrated set does not yield reliable greedy success in the authors' setup. Their attribution to changing web environments is plausible within the paper's argument but not separated from every other source of variation by a controlled experiment.

# 10. Figure-by-Figure Interpretation

## Figure 1 — Two web-data generation pipelines, p. 3

[B] This is a workflow diagram, not a statistical plot. Its upper CRAWLQA branch moves from a root web page through a branching hyperlink tree toward a language-model generation step and a Q/A output. Page icons and a clicking hand depict browsing. The lower E2HQA branch connects successive Q_1, Q_2, Q_n, Q_(n+1) boxes with search-derived content and language-model rewriting; the entity descriptions progressively replace original entities. The output answer remains fixed in the displayed award example.

There are no numerical axes, error bars, or performance units. Colors highlight selected terms and replaced descriptions. The diagram supports the methodological distinction between gathering interconnected content and making an existing question harder through entity replacement. It does not establish actual required step counts or answer-preservation accuracy across the dataset.

## Figure 2 — Training framework, p. 5

[B] The upper diagram has an SFT area followed by an RL area. A Base Model becomes an SFT Model using reformatted CRAWLQA/E2HQA trajectories. Remaining QA pairs flow to a policy and tool-call loop that generates multiple rollouts y_1 through y_G. Reward calculation and group computation lead to advantages A_1 through A_G. A Reference Model and KL connection are also drawn.

The lower-left box shows repeated thought, tool-call, and tool-response blocks followed by thought and answer. The lower-right expansion illustrates iterative search and visit outputs. There are no empirical axes. [D] The KL/reference-model component is visible in the figure but is not explicitly included in Eq. (3), and its coefficient or use is not specified in the supplied implementation details. It should therefore be recorded as a diagram–equation documentation gap, not silently added to the mathematical objective.

## Figure 3 — Data efficiency, p. 8

[B] Grouped bars compare five training-data conditions on GAIA. The x-axis is Dataset, with sample counts in parentheses. The y-axis is Score, displayed from 0 to 60. Blue bars encode PASS@3 and green bars Consistency. No error bars or statistical markers appear.

Approximate visual estimates are: Open-only around 41/25, Crawl-only 49/32, E2H-only 50/33, All 58/40, Final 61/44 for PASS@3/Consistency. These heights are not exact labels and should not replace numerical text. The visually secure conclusion is that Final exceeds All on both bars despite using fewer listed examples, while the synthetic-only conditions outperform Open-only. Composition, size, and filtering are not independently held constant.

## Figure 4 — Detailed SFT/RL evaluation, p. 9

[B] The y-axis is Score (%) with labels through 60; the chart contains three metric groups, each repeating 7B, 32B, and QwQ. Blue bars encode Pass@1, green Pass@3, and orange Cons@3. Paired hatching distinguishes SFT from RL; the legend names each metric/method combination. Red annotations give the exact improvements reproduced in §9.5.

All displayed paired changes are positive. Improvements vary by model and metric; QwQ's changes are small relative to the other models. The plot supports stronger consistency after RL but has no confidence intervals or seed-level dispersion. Bar heights not explicitly labeled are treated as approximate; the red change annotations are visually readable exact labels.

## Figure 5 — Training, behavior, and temperature, p. 10

**Panel a:** a dual-axis line plot versus DAPO Step, with x-values 40, 45, 50, 55, 60. The left axis is Pass@3, spanning approximately 45–52; the right is Consistency@3, spanning 34–38. The blue Pass@3 line increases roughly from 46.5 to 51.0; the green consistency line rises roughly from 34.6 to 36.8. These are approximate visual estimates. Both trends improve; no error bands are shown.

**Panel b:** a dual-axis line plot compares Base, SFT, RL. The left axis is Action Count, roughly 3–7; the right is Reasoning Length, roughly 360–500. Orange action count rises approximately 3.9 → 6.1 → 6.4; green reasoning length rises approximately 370 → 440 → 500. The prose identifies this analysis with Qwen-32B. The reasoning-length unit is not explicitly stated in this panel; importing the Table 4 token unit would be an assumption. The chart supports the association of training stage with more actions and longer reasoning, not proof that every extra action is useful.

**Panel c:** grouped bars compare temperatures 0.5, 0.6, 0.7. The y-axis is Performance; blue denotes Pass@1 and green Pass@3. Roughly, Pass@1 lies in the mid-30s to low-40s and Pass@3 in the low-to-upper-40s. The authors describe temperature effects as minimal. The plot has no exact value labels, confidence intervals, or web-environment controls; exact numerical claims are not extracted from these bar heights.

## Figure 6 — Traditional ReAct sampling prompt, p. 20

[A/B] A boxed prompt specifies Question, Thought, Action, Action Input, and Observation. It requires JSON-schema action parameters, evidence-chain completeness assessment, and tool-selection rationale. Final Answer terminates the interaction, and the prompt encourages repeated steps as necessary. This is a procedure artifact, not an evaluation plot. Its instructions are evidence about trajectory construction, not commands for this analysis.

The prompt expresses desired accuracy and allowed-tool behavior but does not demonstrate enforcement. A natural-language instruction to use only named tools is not, by itself, evidence of an implementation-level restriction.

## Figure 7 — Modified ReAct prompt for LRMs, p. 21

[A/B] The boxed prompt emphasizes allowed tools and complete Action/Action Input fields, says to use tools before answering, and asks for Observation output around calls. Unlike Figure 6, it does not explicitly impose the same externally formatted Thought sequence. It is connected to §2.2's use of an LRM's reasoning-content output as the step thought.

The box heading says Case Trajectory in GAIA while the caption identifies prompts for ReAct using LRMs. The heading/caption mismatch is a presentation inconsistency; the actual content is a generic prompt template, not a completed GAIA trajectory.

## Figure 8 — GAIA case trajectory, pp. 21–24

[A/B] This multi-page example contains a question, five marked steps, colored thought/tool/observation text, and a final answer. The task asks for ZIP codes where the Finding Nemo-associated fish was recorded as nonnative before 2020 according to USGS. The agent searches for Amphiprion ocellaris, visits a species factsheet, visits collection details, then searches for Fred Howard Park's ZIP code. The supplied observation includes a search result with 34689, which becomes the final answer.

The visual inspection covers pp. 21–22 and 24; p. 23 is text-only. Step 2's displayed thought discusses chinstrap-penguin population differences rather than the fish task. Its tool call nevertheless visits the relevant fish page. This mismatch is directly visible, unresolved, and important: the case is not a fully coherent demonstration of goal-aligned reasoning. The final answer on p. 24 also uses an opening <answer> tag twice rather than a closing tag, despite a check mark. The source does not establish whether these are publication transcription mistakes or actual model outputs.

# 11. Table-by-Table Interpretation

## Table 1 — Main benchmark results, p. 7

Rows identify backbone and framework, grouped into No Agency, closed-source agents, open-source agents, and ReAct agents. Columns give GAIA Levels 1–3 and Avg., then WebWalkerQA Easy/Medium/Hard and Avg. Values are percentages under the described Pass@1 evaluation. Dashes mean unreproducible or unreported, without a per-cell distinction. There are no uncertainty intervals or significance markers.

For traceability, the entire average comparison is retained:

| Backbone / framework | GAIA Avg. | WebWalkerQA Avg. |
|---|---:|---:|
| Qwen-2.5-7B Base | 6.8 | 0.8 |
| Qwen-2.5-32B Base | 13.6 | 3.1 |
| Qwen-2.5-32B RAG | 11.8 | 15.3 |
| Qwen-2.5-72B Base | 14.6 | 6.3 |
| GPT-4o Base | 17.5 | 5.5 |
| QwQ-32B Base | 22.3 | 4.3 |
| QwQ-32B RAG | 32.0 | 31.2 |
| DeepSeek-R1-671B Base | 31.1 | 10.0 |
| OpenAI DR | 67.4 | — |
| Qwen-2.5-7B Search-o1 | 17.5 | — |
| Qwen-2.5-7B R1-Searcher | 20.4 | — |
| Qwen-2.5-32B Search-o1 | 28.2 | — |
| QwQ-32B Search-o1 | 39.8 | 34.1 |
| QwQ-32B WebThinker-Base | 44.7 | 41.9 |
| QwQ-32B WebThinker-RL | 48.5 | 46.5 |
| QwQ-32B Simple DS | 50.5 | — |
| Qwen-2.5-7B Vanilla ReAct | 18.4 | 24.2 |
| Qwen-2.5-7B WebDancer | 31.0 | 36.0 |
| Qwen-2.5-32B Vanilla ReAct | 31.0 | 31.9 |
| Qwen-2.5-32B WebDancer | 40.7 | 38.4 |
| QwQ-32B Vanilla ReAct | 37.8 | 24.1 |
| QwQ-32B WebDancer | 51.5 | 47.9 |
| GPT-4o Vanilla ReAct | 34.6 | 33.8 |

Difficulty-level WebDancer values are also preserved because averages can hide important differences:

| Backbone | GAIA L1 / L2 / L3 | WebWalkerQA Easy / Medium / Hard |
|---|---|---|
| Qwen-2.5-7B | 41.0 / 30.7 / 0.0 | 40.6 / 44.1 / 28.2 |
| Qwen-2.5-32B | 46.1 / 44.2 / 8.3 | 44.3 / 46.7 / 29.2 |
| QwQ-32B | 61.5 / 50.0 / 25.0 | 52.5 / 59.6 / 35.4 |

OpenAI DR reports 74.3/69.1/47.6 on GAIA Levels 1/2/3, exceeding WebDancer in each listed GAIA level. Among the compared open-source agent rows, QwQ WebDancer has the highest reported averages on both main benchmarks, although individual cells include ties. On WebWalkerQA Easy, WebThinker-RL's 58.8 exceeds WebDancer's 52.5, and on Hard its 40.4 exceeds WebDancer's 35.4. Thus the best overall average is not the best score in every difficulty column.

The caption says the best results among all frameworks are bold, while the image emphasizes the QwQ WebDancer row even where closed-source DR or another open-source row has a larger value. Boldface should not be used as an independent ranking guarantee. Baseline difficulty cells not reproduced here are deliberately compressed, not uninspected.

## Table 2 — BrowseComp English/Chinese, p. 8

| Framework | Browsing | English | Chinese |
|---|---|---:|---:|
| GPT-4o | No | 0.6 | 6.2 |
| GPT-4o | Yes | 1.9 | — |
| QwQ-32B | No | — | 11.1 |
| WebDancer | Yes | 3.8 / 7.9 | 18.0 / 31.5 |

The surrounding text identifies Pass@1/Pass@3. WebDancer's slashed pairs therefore correspond to those metrics in order. The single baseline entries are not explicitly labeled with a slash-based metric pair; interpreting them as one-attempt scores is supported by the table context but less explicit than the WebDancer pairs. WebDancer leads the available entries, yet the compared browsing conditions differ. Missing values prevent a full matched comparison across languages and models.

## Table 3 — CoT knowledge transfer, p. 9

| Model | Reasoning model? | Short Pass@3 | Short Cons@3 | Short invalid | Long Pass@3 | Long Cons@3 | Long invalid |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen2.5-7B | No | 33.98 | 22.33 | 0.65% | 35.92 | 21.00 | 21.36% |
| Qwen2.5-32B | No | 42.72 | 24.33 | 4.20% | 45.63 | 30.00 | 13.59% |
| QwQ-32B | Yes | 44.66 | 28.33 | 0.97% | 58.25 | 39.66 | 13.27% |

Pass/consistency are presented as percentage-scale scores; invalid rates explicitly carry percent signs. Long-CoT gives QwQ the largest success improvement but increases invalidity for every model. [C] For QwQ, Pass@3 increases 58.25 − 44.66 = 13.59 percentage points. For Qwen-7B, invalidity increases 21.36 − 0.65 = 20.71 points. These results support a trade-off, not uncomplicated superiority of long reasoning. The source does not specify a complete invalid-output taxonomy or statistical uncertainty.

## Table 4 — SFT dataset statistics, p. 18

| CoT type | Number | Average action count | Average thinking length |
|---|---:|---:|---:|
| Short | 7,678 | 4.56 | 510.03 |
| Long | 6,550 | 2.31 | 1599.39 |

The caption defines thinking length as average tokenized thought length. Long-CoT is associated with longer thoughts but fewer actions in these datasets. This is descriptive, not a controlled causal comparison of reasoning length and actions. [C] Total listed SFT items are 7,678 + 6,550 = 14,228, but that does not establish the number of unique questions shared across the two datasets. The means also expose the unresolved action-filter contradiction with p. 5.

# 12. Diagram / Architecture Interpretation

The architecture has two related loops. The **data-production loop** either browses a page tree and generates QA or repeatedly searches and rewrites an existing question. The **execution loop** takes a task and history, generates a thought and action, runs search/visit, receives an observation, updates the history, and continues until answer. The **training loop** first teaches demonstrations, then samples policy executions and uses judged rewards to update model-generated portions of the trajectory.

Inputs include web content, initial QA pairs, reference answers, generated trajectories, and tool descriptions. Outputs include synthetic QA, filtered SFT examples, trained policy models, rollouts, and final answers. Tool-returned content reaches the model through snippets or summarized evidence rather than only through the original user question. In RL, generated answer/format quality becomes a numeric reward; within-group comparison becomes an advantage signal.

[D] For security relevance, this creates multiple observable mediation points: retrieved snippets, visited-page content, summarizer output, structured tool arguments, and the dialogue representation of observations. The paper shows that observations inform later decisions and that tool results are serialized as user messages. It does not show how malicious instructions within those observations are distinguished from legitimate task information. That missing description establishes a question for further investigation, not a proven bypass.

The present system has a constrained information-seeking action space. Broader browser modules and external-API interaction through Python are proposals in Appendix A. They should not be included in the measured current attack surface. The supplied evidence also does not establish autonomous access to files, email, accounts, or credentials.

# 13. Equations and Mathematical Concepts

## Equation (1): trajectory history, p. 4

H_t = (τ_0, α_0, o_0, τ_1, …, τ_(t−1), α_(t−1), o_(t−1)).

This is an ordered sequence, not an optimization objective. τ is thought, α is action, and o is observation. The action has name α^m and parameters α^p. The history provides context for policy π(τ_t, α_t | H_t), which generates the next thought/action pair. The prose says the agent receives observation o_t at step t, although the written H_t ends at o_(t−1). This timing convention is not fully reconciled. The intended iterative feedback role is clear, but exact indexing should not be claimed as unambiguous.

## Equation (2): masked SFT loss, p. 6

L = −[1 / Σ_i I[x_i ≠ o]] Σ_i I[x_i ≠ o] log π_θ(x_i | tc, x_<i), with sums over the trajectory H.

This is a normalized negative log-likelihood loss. θ denotes trainable policy parameters; tc is task context; x_<i is the preceding trajectory; I is an indicator that excludes observations. Inputs are a demonstrated trajectory and context. The output is a scalar training loss, minimized to make the model more likely to generate demonstrated reasoning/actions/answers. Observations influence conditional context but do not contribute target loss.

The source initially describes x_i as thought/action/observation elements and then explains masking in terms of tokens. The precise element-to-token implementation is not specified in this equation, but the intended observation-token exclusion is explicit. No weighting among thoughts and actions beyond this mask is reported.

## Equation (3): DAPO objective, p. 6

The identity is an expectation over QA pairs (q,a) from distribution D and G executions sampled by the old policy. It averages over model-generated execution tokens the minimum of r_(i,t)(θ)Â_(i,t) and clip(r_(i,t)(θ), 1−ε_low, 1+ε_high)Â_(i,t).

r is the current/old-policy probability ratio; Â is the normalized group-relative advantage; ε_low and ε_high are the lower/upper clipping limits. The minimum and clipping restrict the update relative to the old policy. The token normalization denominator is Σ_i |o_i|, where o_i here denotes an execution containing model-generated tokens, not the observation o used earlier. This overloading must be kept visible.

The constraint is 0 < |{o_i : is_equivalent(y,o_i)}| < G. It retains groups with at least one judged-correct execution and at least one judged-incorrect execution. The equation uses y even though the QA pair was written (q,a); the text does not explicitly resolve that symbol change. Actual numerical clipping limits are absent. Figure 2's reference-model/KL link is not present in this written objective.

## Equation (4): ratio and advantage, p. 6

The displayed probability ratio is current policy divided by old policy for execution output conditional on the question and preceding output. The displayed advantage is Â_(i,j) = [R_i − mean({R_i})] / std({R_i}). It compares an execution's reward with the group's mean and scales by the group's standard deviation.

Plainly, a reward above the group average yields positive advantage; below-average reward yields negative advantage when the denominator is positive. Inputs are group rewards and policy probabilities; outputs are ratios and standardized training signals. The formula's indices mix j and t, and o_i appears where a token-level ratio would need more specific indexing. These are source notation problems, so no corrected formula is silently substituted. The mixed-success constraint is consistent with avoiding all-identical correctness outcomes, but implementation details for zero variance or reward ties are not supplied.

## Equation (5): reward, p. 7

R(ŷ_i,y) = 0.1 × score_format + 0.9 × score_answer.

ŷ_i is the predicted answer, y the reference answer, and each score is binary. The format score checks full structural compliance and valid JSON tool calls; the answer score is assigned by an LLM judge. [C] Possible reward values are 0, 0.1, 0.9, and 1.0 because the two binary operands can be 0/0, 1/0, 0/1, or 1/1. This derivation is not a separate author-reported result.

The rationale is that SFT/RFT already handles much format learning, so correctness receives the larger weight. This reward is not a security objective: no explicit penalty for malicious-content obedience, unauthorized actions, provenance failure, or misinformation propagation is specified.

## Unnumbered E2HQA identity, p. 3

R_n = π(S(C_n)) expresses conversion of retrieved content into a replacement description using an LLM. The surrounding prose says entity E_n is searched to obtain content C_n, so the nesting S(C_n) is not fully aligned with the verbal order of search then content. The intended search-and-rewrite process is represented; the notation is not treated as a precise executable algorithm.

# 14. Interpretation and Discussion

[A] The authors interpret the benchmark improvements as evidence that agent capabilities can be trained efficiently through a simple native ReAct framework when appropriate data and staging are provided. Dataset synthesis addresses the shortage of deep QA training examples; filtering improves demonstration quality; SFT teaches multi-step tool behavior; and RL improves decisions and consistency. Appendix C emphasizes the end-to-end pipeline rather than claiming invention of every underlying component.

[D] The most convincing comparison is the same-backbone vanilla-ReAct versus WebDancer table contrast, because it reduces variation in the underlying model. It still compares an entire training package rather than separately identifying the causal contribution of every stage. The data ablation and cold-start experiment add component evidence, but their reported settings are not detailed enough to reproduce all controls from the paper alone.

The study supports O1–O4 through dataset and training results, O5 through clear performance/invalidity trade-offs, and O6 through exploratory instability analyses. Since no formal hypotheses are stated, it is inappropriate to say that a preregistered hypothesis was confirmed. The authors use strong words such as essential and robust; the source evidence should be read within the tested models, tasks, and evaluation procedures.

Important unresolved consistency issues include: the more-than-two-actions filter versus Table 4 means; Fig. 3 component counts versus All; the KL diagram versus Eq. (3); thought/observation versus execution notation; filter and example parameter names; the generic prompt's case-trajectory heading; and the penguin text within the fish case study. None is automatically repaired in this analysis.

[D] The security lens yields a narrower conclusion than the user's question suggests. WebDancer demonstrates an external-observation-to-action feedback pathway and acknowledges hallucinated tools, redundant actions, unreliable sources, and dynamic environments. These facts can motivate studying whether externally supplied content manipulates action selection more readily than in a standalone setting. They do not supply comparative attack rates, establish an exploit, or identify a malicious actor in the case study. The penguin mismatch is a document-visible coherence problem whose origin is unknown.

# 15. Contributions and Novelty

| Contribution type | Author-positioned contribution | Qualification |
|---|---|---|
| Conceptual | A four-stage data-centric/training-stage guideline for autonomous information seeking. | A pipeline synthesis, not a theory of security or agency. |
| Dataset/methodological | CRAWLQA and E2HQA create deeper, diverse synthetic QA. | Public release contents, licensing, and independent quality rates were not inspected. |
| Training | Short/long-CoT sampling, multi-stage filtering, observation-masked SFT, then on-policy DAPO. | ReAct and DAPO are cited components; novelty is their integration here. |
| System | Native ReAct agent compatible with instruction LLMs and LRMs. | Current tool set is search/visit, plus answer termination. |
| Empirical | Main benchmark improvements and additional BrowseComp results. | No uncertainty intervals or adversarial evaluation. |
| Analytical | Evidence about filtering, cold starts, transfer invalidity, RL behavior, and instability. | Several mechanisms are interpretive rather than causally isolated. |

Appendix C contrasts WebThinker's off-policy RL and tools embedded within thinking content with WebDancer's native reasoning-then-action structure and on-policy DAPO. It contrasts SimpleDeepSearcher's SFT-only setup with the additional RL stage. These are author-reported comparisons; the cited outside systems were not independently inspected.

# 16. Limitations

## Authors' stated limitations

Appendix A explicitly identifies six limitations. First, only two basic information-seeking tools are integrated. Second, the main tasks involve short answers; document-level research and long-form generation need different reward design. Third, learning does not yet scale to exploit the full collected QA corpus: only a small RL subset, for example 5,000 pairs, is usable under compute and stability constraints. Fourth, multi-round tool calls and model completions make rollouts expensive and slow. Fifth, present models are trained on one reasoning-data type, while adaptive hybrid thinking is future work. Sixth, reasoning may hallucinate nonexistent tools such as calculate or continue taking redundant actions after confirming the answer.

The main analysis also acknowledges long-CoT simulated observations, repetition/context overruns, sparse rewards, and unstable evolving web environments. Appendix B raises misinformation from unreliable sources and misuse through automated extraction or surveillance. These concerns are broader-impact statements rather than measured incident rates.

## Additional evidence-based analyst observations

[D] The evaluations use a small text-only GAIA subset, so they do not establish performance on all GAIA modalities. Model-based answer judging creates a measurement dependency whose agreement or error rate is not supplied. The paper reports no seed-level uncertainty, confidence intervals, or formal significance tests. Sample overlap, deduplication, leakage prevention, and site-distribution details are not documented sufficiently to assess those issues fully.

The filtering/count inconsistencies and case-study mismatch reduce confidence in exact procedural reproducibility. Low absolute BrowseComp scores qualify general robustness. The memorization experiment uses the same set for training/evaluation and therefore cannot estimate held-out generalization. Finally, no security-specific controls or adversarial tests are reported; task reliability should not be used as a substitute for vulnerability evidence.

# 17. Threats to Validity

These labels are analyst-organized methodological observations, not categories the authors explicitly enumerate.

**Internal validity [D]:** the main result combines dataset construction, filtering, SFT, and RL. It does not independently hold every other factor constant for each component. Dynamic web content can vary between runs, and the temperature experiment does not isolate all environmental changes. The cold-start finding is tied to one incompletely detailed RL-only setting.

**Construct validity [D]:** Pass@1/Pass@3 and consistency measure judged short-answer success. They do not directly measure source reliability, secure instruction handling, unauthorized action avoidance, or comprehensive research quality. An answer can be judged correct without proving every intermediate thought is coherent, as the supplied case illustrates.

**Statistical conclusion validity [D]:** reported percentage improvements lack uncertainty estimates. The 103-question GAIA evaluation is small, and difficulty-subset denominators are absent. Repeating answer attempts is not equivalent to running multiple independent training seeds. Words such as significant in the prose should not be interpreted as a reported statistical significance test.

**External/ecological validity [D]:** live web interaction makes the setting closer to deployed information seeking than a wholly static corpus, but only two tools and short-answer tasks are tested. Broader browser operation, external APIs, long-form writing, and adversarial web pages remain outside the evaluated scope.

**Reproducibility [D]:** useful models, framework names, inference settings, prompts, and data counts are supplied. Missing optimizer/training parameters, incomplete crawl specifications, unresolved notation, and the action-filter contradiction prevent full reconstruction from these pages alone. Repository links are not substitutes for reviewed implementation evidence.

**Security generalizability [D]:** the study includes direct-model and agentic performance baselines but no matched security comparison. It cannot establish that a standalone LLM is safer, that longer trajectories cause greater attack success, or that additional tools necessarily introduce a measured vulnerability.

# 18. Future Work and Open Questions

## A. Explicit author proposals

The authors propose more sophisticated browser modules and a Python sandbox for external-API interaction; extension to document-level research and long-form generation; better reward signals for open-ended tasks; more efficient utilization of the QA corpus; faster integration of tool calls and completions to reduce rollout costs; adaptive hybrid short/long reasoning; and scaling the high-quality dataset to test whether additional data yields performance gains (Appendices A and D).

They also advocate transparency, source attribution, and responsible deployment to mitigate misinformation and misuse (Appendix B). These are proposed practices, not experimentally validated defenses.

## B. Additional open questions

[D] What fraction of synthesized questions genuinely preserves the reference answer? How much benefit remains when dataset size is matched across filtering conditions? What explains the Fig. 3 count mismatch and action-filter wording? Can long reasoning improve correctness without increasing invalid outputs? How accurate and consistent are the model judges across difficult answers? How much instability comes from web changes versus policy, retrieval, summarization, or grading?

[D] For the user's security question: can adversarial content in a snippet or visited page change the next action; does summarization preserve or transform such content; how is tool-output authority represented; and how does attack success compare under matched standalone, RAG, and agentic conditions? These are proposed follow-up questions, not results of WebDancer. The paper provides architecture for specifying such tests but supplies no attack data to answer them.

# 19. Terminology and Notation Glossary

| Term/symbol | Beginner-friendly meaning in this paper |
|---|---|
| Web agent | Model-based system that observes web information and chooses actions toward a task. |
| LLM | Large language model. |
| LRM | Large reasoning model; reasoning-oriented model category. |
| QA | Question–answer pair. |
| CoT | Chain of thought; generated intermediate reasoning trace. |
| Short/Long-CoT | The two trajectory-reasoning styles used for supervision. |
| ReAct | Framework interleaving thought, action, observation. |
| CRAWLQA | QA synthesized from recursively browsed web pages. |
| E2HQA | Easy-to-hard QA formed through answer-preserving entity-description replacement. |
| SFT | Supervised fine-tuning on demonstrations. |
| RFT | Rejection-sampling fine-tuning using selected sampled trajectories. |
| RL | Reinforcement learning from execution rewards. |
| DAPO | Decoupled Clip and Dynamic Sampling Policy Optimization. |
| RAG | Retrieval-augmented generation. |
| chatml | Dialogue serialization format named in implementation details. |
| JSON | Structured format used for tool-call arguments; source expands no further definition. |
| LLM-as-Judge | Model that assesses response correctness. |
| Pass@1 / Pass@3 | Success metrics using one/three attempts; full Pass@3 estimator is not given. |
| Cons@3 | Fraction of three independent attempts that are correct. |
| Inv. | Invalid rate in Table 3. |
| R. | Indicator of reasoning-model status in Table 3. |
| τ_t | Thought at time t. |
| α_t, α^m, α^p | Action, its name, and its parameters. |
| o_t | Observation in the agent-loop notation. |
| o_i | Model-generated execution in DAPO notation; different use of o. |
| H_t / H | Historical trajectory / complete execution trajectory. |
| π_θ / π_θold | Current / previous policy model. |
| tc | Task context used for supervised loss. |
| I[·] | Indicator used to exclude observation targets. |
| G | Number of candidate executions in a group. |
| r_(i,t) | Current-to-old-policy probability ratio. |
| Â_(i,t) | Group-standardized reward advantage. |
| ε_low / ε_high | Lower/upper clipping settings; numeric values absent. |
| M_s / M_j | Summarizer model / judge model. |
| top-p | Named sampling parameter; operational definition not supplied. |
| KL | Label linking reference model and policy in Fig. 2; not fully specified mathematically. |
| EM / F1 | Rule-based answer metrics mentioned as unsuitable here; their formulas are not supplied. |
| n-gram | Repeated token-sequence pattern; filtering uses n = 10 and occurrence threshold 4. |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| GAIA evaluation size | 103 | questions | Text-only validation subset | Author-reported | p. 19, E.1 |
| WebWalkerQA evaluation size | 680 | questions | Test set | Author-reported | p. 19, E.1 |
| E2HQA collected | 40K | samples | Before described trajectory filtering | Author-reported | p. 18, D |
| CRAWLQA collected | 60K | samples | Before described trajectory filtering | Author-reported | p. 18, D |
| Short-CoT SFT | 7,678 | examples | Mean actions 4.56; thought tokens 510.03 | Visually readable | p. 18, T4 |
| Long-CoT SFT | 6,550 | examples | Mean actions 2.31; thought tokens 1599.39 | Visually readable | p. 18, T4 |
| Rejection sampling N | 5 | attempts | Up to five per QA instance | Author-reported | pp. 4, 19 |
| RL rollouts | 16 | executions | RL group generation | Author-reported | p. 19, E.3 |
| Inference sampling | 0.6 / 0.95 | temperature / top-p | Main inference | Author-reported | p. 19 |
| RL sampling | 1.0 / 1.0 | temperature / top-p | RL rollout | Author-reported | p. 19 |
| LRM/LLM repetition penalties | 1.1 / 1.0 | parameter values | Inference | Author-reported | p. 19 |
| Reward weights | 0.1 / 0.9 | weights | Format / judged answer | Author-reported | p. 7, E5 |
| Qwen-7B WebDancer | 31.0 / 36.0 | % | GAIA / WebWalkerQA Pass@1 | Visually readable | p. 7, T1 |
| Qwen-32B WebDancer | 40.7 / 38.4 | % | Same metric/datasets | Visually readable | p. 7, T1 |
| QwQ-32B WebDancer | 51.5 / 47.9 | % | Same metric/datasets | Visually readable | p. 7, T1 |
| QwQ vanilla ReAct | 37.8 / 24.1 | % | Same metric/datasets | Visually readable | p. 7, T1 |
| QwQ improvement | 13.7 / 23.8 | percentage points | 51.5−37.8 / 47.9−24.1 | Analyst-derived | p. 7, T1 |
| OpenAI DR GAIA | 67.4 | % | Reported Pass@1 average; WebWalkerQA absent | Visually readable | p. 7, T1 |
| Best-model Pass@3 | 64.1 / 62.0 | % | GAIA / WebWalkerQA | Author-reported | p. 8, §5 |
| BrowseComp WebDancer English | 3.8 / 7.9 | % | Pass@1 / Pass@3 | Author-reported | p. 8, T2 |
| BrowseComp WebDancer Chinese | 18.0 / 31.5 | % | Pass@1 / Pass@3 | Author-reported | p. 8, T2 |
| RL-only QwQ | 5 | % | GAIA Pass@3 cold-start ablation | Author-reported | p. 9 |
| Qwen-7B invalidity, short/long | 0.65 / 21.36 | % | CoT transfer comparison | Visually readable | p. 9, T3 |
| QwQ Pass@3, short/long | 44.66 / 58.25 | % | CoT transfer comparison | Visually readable | p. 9, T3 |
| Fig. 3 source-count sum | 13,455 | items | 1,308+9,662+2,485 | Analyst-derived | p. 8, F3 |
| Fig. 3 All count | 17,764 | items | Unexplained difference from source-count sum | Visually readable | p. 8, F3 |
| Final Fig. 3 performance | About 61 / 44 | score | Pass@3 / consistency bar heights | Approximate visual estimate | p. 8, F3 |
| Memorization setup | 69 / 10 | trajectories / epochs | Qwen-7B, same-set evaluation | Author-reported | p. 10 |
| Memorization greedy success | 37.4 | % | Same set after fine-tuning | Author-reported | p. 10 |
| Example RL-use subset | 5,000 | pairs | Compute/stability limitation; example, not exact universal count | Author-reported | p. 17, A |
| Repetition filter | 10 / 4 | n-gram length / occurrence threshold | Trajectory quality assessment | Author-reported | p. 18, D |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| The contribution is an integrated four-stage training pipeline. | Explicit stage list and connected framework. | F2, method | pp. 1–2, 5 | HIGH for what was proposed; not proof every stage is novel. |
| Synthetic QA supports deeper information seeking. | Crawl and rewrite procedures; data-composition comparison. | F1/F3, X3 | pp. 3–4, 8 | HIGH for procedure; MEDIUM for general quality/depth claim. |
| Observations guide later actions. | ReAct loop, historical context, rollout description. | E1/F2 | pp. 2, 4–6 | HIGH architectural evidence; no adversarial test. |
| WebDancer improves same-backbone task success. | Three vanilla-ReAct/WebDancer paired average rows. | T1, X1 | p. 7 | HIGH for reported values; uncertainty not supplied. |
| QwQ WebDancer is not best among every listed framework. | DR GAIA 67.4 exceeds 51.5; difficulty exceptions. | T1 | p. 7 | HIGH; missing DR WebWalkerQA prevents full comparison. |
| Filtering is useful under listed data conditions. | Final bars exceed All with fewer listed items. | F3, X3 | pp. 8–9 | MEDIUM; composition/size confounding and count mismatch. |
| SFT cold start matters in the tested setting. | RL-only QwQ reaches only 5% Pass@3. | X5 | p. 9 | HIGH reported result; MEDIUM generalization beyond that setting. |
| Long-CoT transfers imperfectly. | Higher invalid rates and one consistency decrease. | T3, X6 | p. 9 | HIGH table evidence; exact failure taxonomy incomplete. |
| RL gains vary across model types. | Exact gain annotations and author discussion. | F4, X4 | pp. 8–9 | HIGH labels; sparse-reward explanation is not isolated. |
| Web-agent stability is unresolved. | Temperature panel and same-set 37.4% memorization result. | F5/X8/X9 | pp. 9–10 | MEDIUM interpretation; web causality not controlled. |
| The agent has acknowledged reliability limitations. | Nonexistent tools, redundant actions, rollout cost, limited tools. | Appendix A | p. 17 | HIGH author acknowledgment; no attack-rate estimate. |
| Security relevance is architectural rather than demonstrated vulnerability. | External observations enter context; tool responses use user-message serialization. | E.3, method | pp. 4, 19 | MEDIUM analyst inference; no standalone security comparison. |
| The case illustration contains a coherence anomaly. | Fish task followed by penguin-population thought. | F8, X10 | pp. 21–22 | HIGH observable mismatch; origin UNKNOWN. |

# 22. Very Simple Explanation — Explain Like I'm 15

Imagine answering a question that cannot be solved from one webpage. You first search for the right subject, open a useful page, discover that one detail is missing, then search again for that detail. WebDancer tries to teach an AI to do this sequence by itself. The researchers create harder practice questions, collect examples of the steps a model takes, keep better examples, and train the agent to imitate them.

Then they let the agent practice more and reward correct answers. They mainly reward getting the answer right, with a smaller reward for using the correct tool-call format. The trained agent does better than the same model using a basic ReAct setup on the reported benchmarks. But it still gets many difficult questions wrong, sometimes repeats itself, and can imagine a tool that does not exist. Longer reasoning helps some results while producing more invalid outputs.

For a security project, the interesting point is that the AI keeps reading new material from the web and using it to choose its next step. That gives researchers places to investigate whether misleading or malicious content could influence the agent. This paper shows those pathways and some reliability problems. It does not test malicious pages or prove that a web agent is more vulnerable than a standalone language model.

# Completeness Audit

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/dates/footnotes | Yes, text and image | Yes | Represented in compressed form | Venue absent; correspondence extraction imperfect. |
| Abstract | Yes, text and image | Yes | Fully represented | Four-stage contribution and benchmark framing retained. |
| §1 Introduction | Yes, text and image | Yes | Fully represented | Motivation, gaps, scope, and objectives. |
| §2.1 CRAWLQA | Yes, text and image | Yes | Fully represented | Procedure and unavailable crawl details. |
| §2.1 E2HQA | Yes, text and image | Yes | Fully represented | Iterative replacement and notation qualification. |
| §2.2 Agent Setup | Yes, text and image | Yes | Fully represented | Actions, parameters, observations, history. |
| §2.2 Short/Long-CoT | Yes, text and image | Yes | Fully represented | Generators and thought exclusion. |
| §2.2 Filtering | Yes, text and image | Yes | Uncertain | Literal action threshold conflicts with Table 4. |
| §3.1 SFT | Yes, text and image | Yes | Fully represented | Observation masking and cold start. |
| §3.2 DAPO | Yes, text and image | Yes | Uncertain | Objective explained; source notation gaps retained. |
| §3.2 Rollout and reward | Yes, text and image | Yes | Fully represented | Tags, binary scores, weights. |
| §4.1 Setup | Yes, text and image | Yes | Fully represented | Connected to Appendix E. |
| §4.2 Main/harder results | Yes, text and image | Yes | Fully represented | Metric conditions separated. |
| §5 Detailed results | Yes, text and image | Yes | Fully represented | RL gains and three-attempt definitions. |
| §5 Data/cold start | Yes, text and image | Yes | Fully represented | Count mismatch and RL-only result. |
| §5 CoT transfer | Yes, text and image | Yes | Fully represented | Complete Table 3; mixed-data footnote noted below. |
| §5 Behavior/instability | Yes, text and image | Yes | Fully represented | Training, temperature, memorization. |
| §6 Related Works | Yes, text and image | Yes | Represented in compressed form | Categories and positioning retained; citation-by-citation recap omitted. |
| §7 Conclusion | Yes, text only | Yes | Represented in compressed form | Integrated into orientation/contributions. |
| Explicit research questions | Checked | Yes | Fully represented | None formal; informal objectives listed. |
| Explicit hypotheses | Checked | Yes | Fully represented | No formal hypotheses supplied. |
| X1–X9 experiments/analyses | Yes | Yes | Fully represented | Distinct setups and caveats retained. |
| X10 case illustration | Yes | Yes | Represented in compressed form | Not treated as controlled experiment. |
| Figure 1 | Yes, visual/text | Yes | Fully represented | Both pipelines explained. |
| Figure 2 | Yes, visual/text | Yes | Fully represented | Includes unresolved KL diagram link. |
| Figure 3 | Yes, visual/text | Yes | Uncertain | Exact counts retained; heights approximate; sum discrepancy. |
| Figure 4 | Yes, visual/text | Yes | Fully represented | Exact annotated gains; unlabeled heights compressed. |
| Figure 5a/b/c | Yes, visual/text | Yes | Represented in compressed form | All panels covered; exact coordinates unavailable. |
| Figure 6 | Yes, visual/text | Yes | Represented in compressed form | Prompt requirements, not verbatim repetition. |
| Figure 7 | Yes, visual/text | Yes | Represented in compressed form | Template and heading mismatch. |
| Figure 8 | Partially visual; all text | Yes | Uncertain | p. 23 text-only; thought mismatch and answer-tag anomaly. |
| Table 1 | Yes, visual/text | Yes | Represented in compressed form | All average rows, WebDancer difficulty cells, important exceptions; other difficulty cells compressed. |
| Table 2 | Yes, visual/text | Yes | Fully represented | All entries and browsing conditions. |
| Table 3 | Yes, visual/text | Yes | Fully represented | All entries and trade-offs. |
| Table 4 | Yes, visual/text | Yes | Fully represented | Counts, action means, token lengths. |
| Equations (1)–(5) | Yes, visual/text | Yes | Uncertain | All identities explained; timing/index/overloading issues flagged. |
| Unnumbered E2HQA identity | Yes, visual/text | Yes | Uncertain | Verbal flow and written nesting differ. |
| Algorithms/pseudocode | Checked | Yes | Fully represented | No separate numbered pseudocode; procedures explained. |
| Major contributions | Yes | Yes | Fully represented | Pipeline, data, training, system, empirical analysis. |
| Appendix A limitations | Yes, text only | Yes | Fully represented | All six named limitations retained. |
| Appendix B impacts | Yes, text only | Yes | Fully represented | Benefits compressed; harms and proposed practices retained. |
| Appendix C.1/C.2 | Yes, visual/text | Yes | Represented in compressed form | Concurrent-method distinction and agent-model framing. |
| Appendix D | Yes, visual/text | Yes | Fully represented | Counts, filtering, open-only source list. |
| Appendix E.1/E.2/E.3 | Yes, visual/text | Yes | Fully represented | Subsets, baselines, implementation parameters. |
| Appendix E.4 | Yes, visual/text | Yes | Represented in compressed form | Both sampling prompts covered. |
| Appendix F | Yes, partial visual/all text | Yes | Represented in compressed form | Five-step sequence and anomalies covered. |
| Substantive footnotes | Yes | Yes | Represented in compressed form | Training-data appendix, equal contributors, Qwen-Agent URL; mixed-CoT experiment reports no significant improvement. |
| References pp. 12–16 | Yes, text only | Yes | Represented in compressed form | Bibliography accounted for; cited artifacts not opened. |
| Decorative content | Yes on rendered pages | Yes | Inspected but deliberately omitted as non-substantive | Logos, running rules, repeated page furniture. |
| Separate supplementary files | Not supplied | No | Missing from supplied material | No claim of supplement/repository inspection. |

## Missing or inaccessible material

No numbered paper page is missing from the supplied extracted text. Original page images for pp. 11–17 and 23 were not supplied, so their layout, symbols, and visual fidelity could not be independently checked. External repository contents, dataset releases, linked documents, and separate supplementary artifacts were not supplied or inspected. Unreported training settings, uncertainty statistics, crawl details, and security-test configurations cannot be reconstructed from the paper.

## Uncertain interpretations

The exact Fig. 3/5 plotted heights are not labeled; visual estimates remain approximate. Equation indexing, overloaded o, the y/a switch, and the E2HQA nesting are imperfectly specified. The p. 5 action-filter wording conflicts with Table 4 averages. Fig. 3 source counts do not sum to All. The reference-model/KL link is not explained in the written DAPO objective. Formal tool parameter names differ from the case examples' url field. The case-study penguin thought and malformed final answer tag are present, but their origin is unknown. The hardware sentence does not unambiguously state GPUs per node. Table 1 boldface does not consistently mark the largest value among every listed framework.

## Deliberately compressed material

The full bibliography, repeated motivational passages, every baseline difficulty cell, generic prompt wording, and most long case-study thoughts are compressed. All Table 1 average rows and meaningful ranking exceptions are preserved; Tables 2–4 are reproduced completely. Figures 6–8 are explained as procedural/illustrative evidence rather than quoted at length. The open-only training datasets are MuSiQue, Bamboogle, PopQA, 2Wiki, and HotpotQA, filtered using RAG to remove easy questions. The mixed short/long-CoT footnote reports no significant improvement but supplies no numerical result or statistical test; that limited finding is retained without strengthening it.

## Potential omissions

Every substantive item identified in the inventory is represented or explicitly marked compressed, uncertain, or inaccessible. Exact visual confirmation remains unavailable for the text-only pages, and unprovided external artifacts remain outside coverage. The inventory supports comprehensive coverage of the supplied paper; it does not justify calling the study a complete security analysis or claiming that all external implementation details have been assessed.
