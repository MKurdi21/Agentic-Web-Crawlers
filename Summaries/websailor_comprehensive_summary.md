# WebSailor: Navigating Super-human Reasoning for Web Agent

**Authors:** Kuan Li, Zhongwang Zhang, Huifeng Yin, Liwen Zhang, Litu Ou, Jialong Wu, Wenbiao Yin, Baixuan Li, Zhengwei Tao, Xinyu Wang, Weizhou Shen, Junkai Zhang, Dingchu Zhang, Xixi Wu, Yong Jiang, Ming Yan, Pengjun Xie, Fei Huang, and Jingren Zhou  
**Affiliation:** Tongyi Lab, Alibaba Group

## 1. Background and Context

Web-based information seeking is fundamentally a process of reducing uncertainty. Humans can search the internet, but finite memory, fragile attention, and difficulty pursuing many exploratory paths simultaneously limit their ability to navigate very large information spaces. Proprietary LLM agents such as DeepResearch have exceeded these human limitations on difficult benchmarks such as BrowseComp-en and BrowseComp-zh.

The authors argue that these systems succeed because they can systematically reduce extreme uncertainty through internal reasoning and interactions with web tools. Open-source agents lack this capability: their accuracy on BrowseComp-en was close to zero before this work.

The paper divides information-seeking questions into three levels:

- **Level 1:** Low uncertainty that is easy to reduce. A model can answer from its internal knowledge or through one straightforward search.
- **Level 2:** High initial uncertainty but a clear path to the answer. Conventional multi-hop questions fit this category because entities are connected through a predefined sequence of reasoning steps.
- **Level 3:** Both high uncertainty and high difficulty reducing it. Entities have complex, emergent relationships, there is no predefined solution path, and the agent must creatively explore, compare evidence, abandon unpromising routes, and combine scattered facts.

Existing training data mainly covers Levels 1 and 2. It therefore does not teach agents to generalize compositionally over the complex, non-linear information structures found in Level 3 tasks. A brute-force search is not viable: it might require thousands of tool calls and exceed an LLM’s context window. Instead, an agent must compress a vast search space into a tractable trajectory of a few dozen steps.

The paper places BrowseComp-en/zh at the most difficult end of an evolution in information-seeking benchmarks. Earlier datasets such as Natural Questions and TriviaQA often permit direct answers or structured searches. HotpotQA and Musique add multi-hop reasoning; GAIA and Xbench-DeepSearch introduce more demanding tool use and information retrieval; BrowseComp adds intricately coupled entities and deliberate obfuscation, requiring non-linear exploration and synthesis.

Existing open-source agents—including WebDancer, WebThinker, Search-o1, and R1-Searcher—have improved performance on simpler tasks but remain far behind proprietary systems on Level 3 problems. Pure supervised fine-tuning also tends to generalize poorly in adaptive settings, while reinforcement learning faces stability, efficiency, and sparse-reward problems.

## 2. Research Goal and Objectives

The paper aims to create an open-source web agent capable of the uncertainty-reducing reasoning required for exceptionally difficult information-seeking tasks.

Its central hypothesis is that an agent can acquire robust, generalizable search strategies if it is post-trained on tasks deliberately constructed to have:

1. High initial uncertainty.
2. Complex relationships among entities.
3. No fixed or easily specified solution path.
4. A need for long-horizon web interaction and evidence synthesis.

To test this hypothesis, the authors develop **WebSailor**, an end-to-end post-training pipeline comprising:

- SailorFog-QA, a scalable source of complex, graph-synthesized questions.
- Reconstructed, concise reasoning trajectories obtained from expert reasoning models.
- A small rejection-sampling fine-tuning cold start.
- Duplicating Sampling Policy Optimization, or **DUPO**, for more efficient agentic reinforcement learning.
- WebSailor models at 3B, 7B, 32B, and 72B parameter scales.

The study evaluates whether this pipeline can:

- Establish a new open-source state of the art on BrowseComp-en/zh.
- Approach proprietary browsing agents.
- Generalize to GAIA and Xbench-DeepSearch.
- Retain “downward compatibility” with simple Level 1 factual questions.
- Improve the reliability and sample efficiency of long-horizon reasoning.

## 3. Methods (Approach/Design)

### Agent framework and tools

WebSailor uses the ReAct framework. For each question, it repeatedly cycles through:

1. **Thought:** Reason about the current evidence and next step.
2. **Action:** Search, visit webpages, or provide a final answer.
3. **Observation:** Receive results from the external environment.

A trajectory with \(T\) iterations is a sequence of thoughts, actions, and observations. At each step, the next thought and action depend on the entire previous trajectory.

The two web tools are:

- **Search:** Sends one or more queries to Google and returns the top 10 results per query. Each result contains a title, snippet, and URL.
- **Visit:** Retrieves one or more webpages with Jina. A summary model—Qwen-2.5-72B in this study—then extracts information relevant to a separately specified goal for each page.

The ReAct implementation uses Qwen-Agent and permits no more than 30 tool calls per trajectory.

### SailorFog-QA construction

The synthetic dataset is generated from knowledge graphs created by random walks:

1. Use Wikidata’s SPARQL service and database rules to select a rare or “fuzzy” starting entity.
2. Gather its features using search and visit tools.
3. Extract related entities and relationships from unstructured web content.
4. Probabilistically choose either a newly discovered entity or an earlier graph node as the next expansion point.
5. Repeat until the graph reaches a predefined number of edges.

Choosing expansion nodes stochastically discourages simple linear chains. It instead creates dense graphs with overlapping, non-linear relationships.

The system samples subgraphs with different topologies, then formulates question–answer pairs from their entities and relations. It deliberately obscures clues to increase uncertainty. Examples include:

- Replacing an exact date with “in the early 2010s.”
- Partially masking a name, such as referring to an institution founded by someone whose initial is “F.”
- Replacing an exact quantity with a qualitative condition, such as “a market share of less than 1%.”

This produces questions grounded in real web information but requiring multi-step deduction, compositional reasoning, comparisons, and synthesis. The number of possible subgraphs grows non-linearly with graph size, making the process scalable.

Two examples illustrate the construction:

- A question connects a late-antique hymn writer’s approximate death date to the endpoint of a scientific chronology. Its answer is **“Estimated Tree-Ring Chronology: 300–450 A.D.”**
- A question links a musical work associated with a South American capital, a lyricist receiving a civic honor, and a composer trained in western Colombia. Its answer is **“the Rue de Rivoli.”**

Manual evaluation found such questions intractable for human researchers under typical constraints such as a two-hour limit because they offer no clear starting point and demand extensive non-linear exploration. Some generated problems reportedly required the proprietary o3 model to make as many as 40 tool calls.

### Figure 2: The three task levels

Figure 2 depicts the information structure of each level:

- Level 1 has mostly independent nodes and one highlighted target, representing a direct lookup.
- Level 2 has a clearly connected chain through several nodes, representing fixed multi-hop reasoning.
- Level 3 begins with a sampled interconnected graph and then “fuzzes” it into several ambiguous clusters linked through partially hidden relationships.

The figure’s Level 1 examples ask who received the Richard Dawkins Award in 2004 and who was the most prominent figure in the 1986 People Power Revolution. Its Level 2 examples ask for the first Chinese Academy of Sciences academician from the current Alibaba CEO’s alma mater and for the state containing the hometown of the American athlete who won the most gold medals at the 2004 Olympics.

### Reconstructing reasoning from expert trajectories

Expert reasoning models such as QwQ-32B can solve some synthetic questions, but their native reasoning is unsuitable for direct fine-tuning:

- **Stylistic contamination:** Their verbose, strongly stylized thoughts may cause the trainee to imitate one rigid style rather than develop flexible exploration strategies.
- **Context overload:** Long thoughts combined with dozens of tool calls can exceed context limits and impair performance and readability.

The authors therefore retain only the expert’s successful action–observation sequence and discard its original thoughts. A separate, powerful instruction-following model reconstructs a short, goal-directed justification for each action using:

- The trajectory history before that step.
- The expert’s selected action.
- The resulting observation.

This produces a complete trajectory containing concise “short-CoT” thoughts, expert actions, and observations. It preserves the solution logic without copying the expert’s verbosity.

### RFT cold start

Training has two stages. The first is a modest **rejection sampling fine-tuning (RFT)** cold start intended to teach basic tool use and the structure of long-horizon reasoning.

The expert trajectories undergo three filters:

1. Keep only trajectories ending in the correct answer.
2. Discard trajectories longer than 32,000 tokens.
3. Retain only trajectories with more than five tool calls to emphasize complex reasoning and planning.

Thoughts are enclosed in `<think>` tags, tool calls in `<tool_call>`, observations in `<tool_response>`, and final responses in `<answer>`. Observation tokens are excluded from the training loss because the objective is to improve the model’s thoughts and actions, not reproduce environment outputs.

The paper says that just over 2,000 high-quality examples provide an effective cold start.

### DUPO reinforcement learning

After RFT, the authors apply **Duplicating Sampling Policy Optimization**.

Agentic RL is slow because each rollout requires multiple interactions with web tools. Earlier dynamic-sampling methods discard groups whose rollouts are all correct or all incorrect, then sequentially generate new questions to refill the batch. DUPO avoids this extra sequence of rollouts.

Its two sampling stages are:

- **Before training:** Remove overly easy cases for which all eight rollouts are correct.
- **During training:** Remove groups with zero reward standard deviation—that is, groups where all answers are correct or all are incorrect. Refill the batch by randomly duplicating other non-zero-variance cases already present in the same batch.

This gives an approximately **2–3× speedup** over DAPO-style dynamic sampling.

DUPO uses:

- Group-relative advantage estimation.
- A token-level policy-gradient objective.
- Asymmetric low and high clipping.
- Observation masking in the policy loss.
- Eight rollouts per question.

In plain language, each rollout’s advantage is its reward minus the group mean, divided by the group standard deviation. A response is therefore reinforced according to how well it performs relative to other responses for the same question.

The reward is:

- **10% format score**, verifying tags and compliance with the ReAct sequence.
- **90% answer score**, using an LLM judge to assess final-answer correctness.

The rule-based combination is intended to discourage reward hacking.

### Training setup

The authors train Qwen-2.5 models with 3B, 7B, 32B, and 72B parameters.

For supervised fine-tuning, they use Megatron with:

- Batch size: 32.
- Learning rate: \(5 \times 10^{-6}\).
- Minimum learning rate: \(1 \times 10^{-10}\).
- Warmup followed by cosine decay.
- Weight decay: 0.1.

For reinforcement learning, they use verl with:

- Eight rollouts per group.
- Temperature: 1.0.
- Top-p: 1.0.
- Batch size: 128.
- Mini-batch size: 32.
- Learning rate: \(1 \times 10^{-6}\).

### Evaluation design

The four main benchmarks are:

- **BrowseComp-en:** Hard-to-find, multifaceted English web information.
- **BrowseComp-zh:** A similar Chinese-language benchmark.
- **GAIA:** A multimodal and tool-use benchmark; the paper evaluates 103 cases from its text-only validation subset.
- **Xbench-DeepSearch:** Dynamic, professionally aligned deep-search and tool-use tasks.

A separate analysis uses 200 randomly sampled questions from SimpleQA’s full set of 4,326 questions.

Baselines include:

- Direct inference with Qwen-2.5-32B/72B, GPT-4o, GPT-4.1, QwQ-32B, o4-mini, and DeepSeek-R1.
- Proprietary browsing agents: DeepResearch, Grok-3/Grok-DeepResearch, Doubao with Deep Think and Search, and browsing-enabled GPT-4o.
- Open-source agents: Search-o1, WebThinker, R1-Searcher, and WebDancer.

The primary metric is pass@1: the average correctness of one sampled response per question. Main evaluations use temperature 0.6 and top-p 0.95, with an LLM judge determining accuracy. Pass@\(k>1\) uses \(k\) independently generated responses. Some proprietary results were manually evaluated through product websites or taken from benchmark publications, and some combinations were unavailable because of cost.

## 4. Results and Findings

### Main benchmark results

| Model or system | Paradigm | BrowseComp-en | BrowseComp-zh | Xbench-DeepSearch | GAIA |
|---|---:|---:|---:|---:|---:|
| Qwen-2.5-32B | Direct | 0.6 | 3.9 | 8.7 | 13.6 |
| Qwen-2.5-72B | Direct | 0.6 | 7.0 | 12.7 | 14.6 |
| GPT-4o | Direct | 0.6 | 6.2 | 18.0 | 17.5 |
| GPT-4.1 | Direct | 1.5 | 14.4 | 17.0 | 22.3 |
| QwQ-32B | Direct | 0.5 | 10.0 | 10.7 | 22.3 |
| o4-mini | Direct | 6.1 | 15.2 | 22.3 | 33.3 |
| DeepSeek-R1 | Direct | 2.0 | 26.3 | 32.7 | 16.5 |
| Grok-3 | Browsing | unavailable | 12.9 | 50+ | unavailable |
| Doubao | Browsing | unavailable | 26.0 | 50+ | unavailable |
| GPT-4o | Browsing | 1.9 | unavailable | unavailable | unavailable |
| DeepResearch | Browsing | 51.5 | 42.9 | unavailable | 67.4 |
| R1-Searcher-7B | ReAct | 0.4 | 0.6 | 4.0 | 20.4 |
| Qwen-2.5-32B Search-o1 | Search-o1 | 0.1 | 2.4 | 3.7 | 28.2 |
| WebDancer-32B | ReAct | 2.5 | 14.1 | 38.7 | 40.7 |
| QwQ-32B Search-o1 | Search-o1 | 2.8 | 17.9 | 25.0 | 39.8 |
| WebThinker-RL | ReAct | 2.8 | 7.3 | 24.0 | 48.5 |
| WebDancer-QwQ | ReAct | 3.8 | 18.0 | 39.0 | 51.5 |
| **WebSailor-3B** | ReAct | **3.3** | **9.7** | **27.7** | **33.0** |
| **WebSailor-7B** | ReAct | **6.7** | **14.2** | **34.3** | **37.9** |
| **WebSailor-32B** | ReAct | **10.5** | **25.5** | **53.3** | **53.2** |
| **WebSailor-72B** | ReAct | **12.0** | **30.1** | **55.0** | **55.4** |

These results establish several findings:

- Direct inference is generally inadequate for BrowseComp. Even GPT-4.1 reaches only 1.5 on BrowseComp-en and 14.4 on BrowseComp-zh.
- Strong reasoning models show some ability without tools. DeepSeek-R1 reaches 26.3 on BrowseComp-zh, while o4-mini scores 6.1 on BrowseComp-en.
- Every WebSailor size substantially improves over the corresponding general pattern of open-source agents.
- WebSailor-7B scores 6.7 on BrowseComp-en, beating much larger 32B agents such as WebDancer-32B at 2.5 and WebThinker-RL at 2.8. This supports the claim that the training method, rather than scale alone, produces the gain.
- WebSailor-32B and 72B achieve 53.3 and 55.0 on Xbench-DeepSearch, exceeding the reported 50+ results for Grok-3 and Doubao.
- WebSailor-72B reaches 30.1 on BrowseComp-zh, exceeding Doubao’s 26.0 and Grok-3’s 12.9.
- DeepResearch remains clearly ahead, scoring 51.5 on BrowseComp-en, 42.9 on BrowseComp-zh, and 67.4 on GAIA.
- WebSailor’s advantage is smaller on GAIA because many GAIA questions require mathematics or computation, capabilities that were not the focus of its training. The authors report that performance remains especially strong on GAIA’s pure information-retrieval portion, but do not provide a separate numerical score.

### Figure 1: BrowseComp-en and BrowseComp-zh

Figure 1 presents bar charts that highlight the difficult BrowseComp results.

For **BrowseComp-en**:

- WebSailor-72B: 12.0.
- WebSailor-32B: 10.5.
- DeepSeek-R1-Browse: 9.5.
- WebDancer-QwQ: 3.8.
- WebThinker-QwQ: 2.8.
- DeepSeek-R1: 2.0.
- GPT-4o with browsing: 1.9.
- Search-o1-32B: 0.6.

For **BrowseComp-zh**:

- WebSailor-72B: 30.1.
- WebSailor-32B: 25.5.
- Doubao-Search: 26.0.
- WebDancer-QwQ: 18.0.
- WebThinker-QwQ: 14.7 in the figure.
- Grok-3: 12.9.
- Search-o1-32B: 7.2.

Some labels in Figure 1 do not exactly match the naming or values in Table 1—for example, the chart displays WebThinker-QwQ at 14.7 on BrowseComp-zh, while Table 1 lists WebThinker-RL at 7.3. The supplied paper does not explain this difference, so the values should be treated as results for differently labeled configurations rather than assumed to be the same experiment.

### Complexity of SailorFog-QA

Figure 3 compares the distribution of tool-call counts in unfiltered but correct SailorFog-QA trajectories with BrowseComp-en and WebDancer-QA.

- More than 50% of WebDancer trajectories require only two tool calls.
- Almost none require more than 10 calls.
- SailorFog-QA has a long-tailed distribution, with many examples requiring more than five calls and some requiring more than 20.
- Its distribution closely resembles BrowseComp-en’s complexity profile.
- The displayed SailorFog-QA data precedes the final filter that removes trajectories with five or fewer calls.

The analysis uses tool-call count as a proxy for task difficulty. It supports the claim that SailorFog-QA is structurally representative of difficult browsing tasks rather than being dominated by simple searches.

### Table 2: Difficulty of the synthetic data

| Browsing backbone | SailorFog-QA | WebDancer-QA | BrowseComp-en |
|---|---:|---:|---:|
| o4-mini | 47.3 | 90.2 | 26.3 |
| DeepSeek-R1 | 38.9 | 84.4 | 9.5 |

Both models use browsing tools under ReAct. Before filtering, SailorFog-QA is much harder than WebDancer-QA but easier than the already difficulty-filtered BrowseComp-en benchmark.

The relatively low SailorFog-QA scores arise partly from genuine difficulty and partly from answer ambiguity. Some questions may have multiple intersections satisfying their clues rather than one unique solution. The authors nevertheless ensure that the designated answer satisfies all conditions in the question.

### Figure 4: Compatibility with SimpleQA

On the random sample of 200 SimpleQA questions, Figure 4 reports:

- WebSailor-72B: **93.5%**.
- WebSailor-32B: **92.8%**.
- WebDancer-QwQ: **90.5%**.
- WebDancer-32B: **87.5%**.
- WebThinker-RL: **77.5%**.
- DeepSeek-R1-ReAct: **72.2%**.
- R1-Searcher-7B: **52.0%**.
- GPT-4.1: **41.6%**.
- GPT-4o: **38.2%**.
- DeepSeek-R1: **27.8%**.
- o4-mini: **20.0%**.
- Qwen-2.5-72B: **15.8%**.
- QwQ-32B: **12.7%**.
- Qwen-2.5-32B: **9.0%**.

Almost every agent-based method outperforms direct answering. WebSailor ranks first despite being trained exclusively on high-difficulty data, indicating that its learned tool-use and reasoning strategies transfer downward to simpler factual tasks.

### Figure 5: Effect of reinforcement learning

Figure 5 compares RFT-only WebSailor with the final RL-trained model, using pass@1 and pass@3 for 32B and 72B models.

The annotated RL improvements are:

| Benchmark | 32B pass@1 | 32B pass@3 | 72B pass@1 | 72B pass@3 |
|---|---:|---:|---:|---:|
| BrowseComp-en | +3.3 | +2.2 | +3.7 | +3.4 |
| BrowseComp-zh | +6.3 | +6.5 | +8.3 | +4.9 |
| GAIA | +6.6 | +4.7 | +3.0 | +3.6 |
| Xbench | +7.6 | +8.0 | +3.7 | +2.0 |

RL improves every reported model–metric–benchmark combination. The largest gains are concentrated on BrowseComp-en/zh and, for the 32B model, Xbench.

BrowseComp initially shows a wide difference between pass@1 and pass@3, meaning the model sometimes succeeds but cannot do so reliably in a single attempt. RL reinforces effective trajectories and suppresses ineffective ones. Because pass@1 often improves proportionally more than pass@3, the authors interpret the results as evidence that RL improves sample efficiency and lets the model approach its multi-sample potential with one generation.

The exact underlying RFT and RL bar heights are not printed numerically in the supplied figure; only the improvement annotations are stated precisely.

### Figure 6: Necessity of the RFT cold start

Figure 6 compares direct RL of Qwen-2.5-Instruct-32B with RL following an RFT cold start.

- On BrowseComp-en, the cold-started model remains roughly in the 9–11% range over the displayed training steps, while the direct-RL model rises from about 2% to around 4%.
- On GAIA, the cold-started model remains roughly around 50–53%, while the direct-RL model rises from the mid-30s to about 41%.
- The cold-started model maintains approximately 6–7 tool calls throughout training.
- The direct-RL model increases from approximately zero to around 3–4 tool calls but remains substantially below the cold-started model.

These values are visually approximate because Figure 6 does not print exact point labels. The qualitative conclusion is explicit: direct RL shows a larger increase from its own starting point, but converges to a substantially worse result. Its lower tool-call count indicates that it fails to acquire long-horizon reasoning. The performance gap is especially wide on BrowseComp-en, suggesting that sparse RL feedback alone cannot readily discover the necessary sophisticated strategies.

### Appendix case study

The case study asks for the first computer jointly purchased by a software developer and his father in the 1980s. The developer is described indirectly through a solar-powered refrigerator, rustic living “in a hole in the map,” memories of a developer conference in Edinburgh, and an interest in caving.

Across 10 steps, the agent:

1. Searches combinations of the clues.
2. Refines searches after irrelevant results.
3. Uses the distinctive “hole in the map” phrase to locate a relevant LWN article.
4. Identifies **Joey Hess**.
5. Verifies that Hess designed and tested an off-grid solar-powered refrigerator.
6. Searches for evidence about conference memories and caving.
7. Visits an interview concerning Debian conference memories.
8. Performs further caving-related searches.
9. Visits Hess’s personal Atari blog entry.
10. Synthesizes the evidence and answers **Atari 130XE**, reportedly bought jointly with his father around 1986.

The example illustrates the intended reasoning pattern: identify a person by intersecting weak clues, verify the identity through independent sources, then retrieve the requested detail from a primary personal account.

## 5. Analysis and Interpretation

The results support the paper’s uncertainty-reduction hypothesis. Pretrained knowledge alone is insufficient because BrowseComp questions concern highly specific facts that must be gathered dynamically. Strong direct reasoning helps—shown by DeepSeek-R1’s 26.3 on BrowseComp-zh—but does not replace external evidence acquisition.

The authors attribute WebSailor’s gains to the combination of:

- Training questions with complex, non-linear structures.
- Deliberately ambiguous clues.
- Long action–observation trajectories.
- Concise reconstructed reasoning that avoids copying an expert model’s verbosity.
- A cold start that provides an initial repertoire of sophisticated strategies.
- Reinforcement learning that improves trajectory selection, reliability, and single-sample performance.

Model scale still matters: results generally rise from WebSailor-3B through 72B. However, the success of WebSailor-7B against several 32B agents indicates that data and training design are independently important.

The SailorFog-QA analyses provide evidence that the synthetic data matches the target problem structure. Its tool-call distribution resembles BrowseComp-en much more closely than WebDancer-QA, and capable browsing models find it substantially harder than WebDancer’s training set.

The SimpleQA findings show downward compatibility: training on difficult tasks does not prevent the agent from solving simple questions. Instead, learned search and verification behavior transfers to Level 1 factual retrieval.

The RFT-versus-direct-RL comparison shows that complex exploration strategies are difficult to discover from sparse rewards alone. The cold start places the agent in a useful part of the policy space, after which RL can refine rather than invent long-horizon behavior.

The authors interpret the smaller gains on GAIA as a consequence of specialization. WebSailor targets information retrieval rather than the mathematical and computational skills required by many GAIA cases.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- **An uncertainty-based account of web-agent difficulty:** It explains the open-source/proprietary gap in terms of the ability to reduce high, hard-to-reduce uncertainty.
- **A three-level task taxonomy:** It distinguishes direct lookup, structured multi-hop reasoning, and open-ended Level 3 exploration.
- **SailorFog-QA:** A scalable method for generating real-web-grounded Level 3 questions from random-walk knowledge graphs, subgraph sampling, and information obfuscation.
- **Reasoning reconstruction:** It retains expert action–observation traces while replacing verbose native thoughts with short, action-oriented justifications.
- **Evidence for an RFT cold start:** A little over 2,000 high-quality trajectories are sufficient to bootstrap tool use and long-horizon reasoning before RL.
- **DUPO:** A reinforcement-learning method that duplicates useful within-batch cases instead of sequentially generating replacements, producing an estimated 2–3× speedup over DAPO-style sampling.
- **A complete open-source-oriented post-training pipeline:** The work integrates data creation, supervision generation, RFT, and RL across 3B–72B models.
- **New open-source benchmark performance:** WebSailor reaches 12.0 on BrowseComp-en, 30.1 on BrowseComp-zh, 55.0 on Xbench-DeepSearch, and 55.4 on GAIA at 72B.
- **Evidence of downward compatibility:** WebSailor-72B achieves 93.5% on the evaluated SimpleQA subset despite training only on high-difficulty data.

## 7. Limitations and Caveats

The authors identify several limitations:

- **32K training-trajectory cutoff:** Filtering out longer trajectories may cap performance on even more complex questions.
- **Context-length failures:** Many failed cases exceed the available context, and performance can deteriorate as inference length grows.
- **Potentially non-unique synthetic answers:** Obfuscated conditions may sometimes admit multiple satisfying entities. The designated answer is guaranteed to satisfy the question, but it may not always be uniquely determined.
- **Over-thinking:** WebSailor may use multi-step tool calls on apparently simple questions. The authors note that this can represent useful cross-verification rather than aimless search, so they do not treat it as an unambiguous defect.
- **Training limited to 50 RL steps:** Synchronous agentic RL remains slow even with DUPO.
- **Specialization:** WebSailor was not optimized for the mathematical and computational demands present in parts of GAIA.
- **Partial evaluations:** GAIA uses only 103 text-only validation cases, and SimpleQA uses 200 randomly sampled questions rather than all 4,326.
- **Incomplete proprietary comparisons:** Some proprietary agents were not available through APIs, so they were manually evaluated, taken from external benchmark reports, or omitted because of cost.
- **LLM-based judging:** Final-answer correctness is assessed by an LLM judge rather than exclusively by deterministic evaluation.
- **Tool-call count is a proxy:** The analysis treats more tool calls as an indicator of greater difficulty, although the number of calls does not capture every aspect of reasoning complexity.
- **DeepResearch remains ahead:** WebSailor narrows but does not eliminate the gap on all benchmarks, particularly BrowseComp-en.

No statistical significance tests, confidence intervals, or error bars are reported in the supplied paper.

## 8. Future Work or Open Questions

The authors plan to:

- Replace synchronous RL with an asynchronous training framework.
- Improve training efficiency enough to run substantially more than 50 RL steps.
- Support longer contexts and trajectories beyond the current 32K-token training filter.
- Define and generate still more complex tasks with greater uncertainty.
- Improve the effectiveness and efficiency of reinforcement learning for agents.
- Continue enhancing open-source models in information seeking.
- Extend the pursuit of “superhuman” capabilities beyond web information retrieval to other dimensions of general agent performance.

Open technical questions left by the paper include how to handle questions with multiple valid answers, how to prevent unnecessary tool use while preserving valuable cross-verification, and how to maintain performance as trajectories become longer.

## 9. High-Level Takeaway (Plain Language)

WebSailor teaches an open-source language model how to solve web questions whose answers cannot be found through one obvious search. It generates difficult, deliberately ambiguous questions, shows the model concise examples of how to navigate them, and then reinforces successful search behavior. The resulting agents outperform prior open-source systems, sometimes match or beat proprietary browsing products, and remain effective on much simpler factual questions. The central message is that advanced web reasoning depends not merely on making a model larger, but on training it to steadily narrow uncertainty across many searches, webpages, and possible solution paths.