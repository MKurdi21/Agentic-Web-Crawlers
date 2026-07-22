# MMInA: Benchmarking Multihop Multimodal Internet Agents

**Authors:** Shulin Tian, Ziniu Zhang, Liangyu Chen, and Ziwei Liu  
**Affiliation:** S-Lab, Nanyang Technological University  
**Published in:** Findings of ACL 2025, pp. 13682–13697

## 1. Background and Context

Autonomous Internet agents are intended to understand user requests, navigate websites, gather information, and perform actions such as shopping or booking travel. Real web tasks are often both:

- **Multihop:** they require a sequence of subtasks on different websites.
- **Multimodal:** they require both textual and visual information.

For example, purchasing a blue cotton shirt requires understanding text such as material descriptions and visual information such as color. A travel request might require identifying a destination on Wikipedia, booking a flight and hotel, and finding relevant videos.

Existing benchmarks do not adequately capture this setting. Many use curated textual interfaces, simulated or static websites, multiple-choice actions, or tasks confined to one website. Although VisualWebArena adds visual cues and WebVoyager uses dynamic websites, their tasks remain substantially shorter than MMInA’s long, cross-site tasks.

The paper describes web browsing as a **partially observable Markov decision process**:

- The full state includes Internet content and the status of the browser and agent.
- Because the entire Internet state cannot practically be represented, the agent receives a partial observation.
- An observation combines the user’s task, a webpage accessibility tree, linked images, and action/state history.
- The agent chooses an action, such as clicking, scrolling, typing, or producing a textual answer.
- The Internet implicitly determines how each action changes the state.
- Each website-specific subtask, called a **hop**, receives a `PASS` or `FAIL`.

The central problem is that success on isolated, single-site tasks does not imply an ability to manage a long workflow. Agents must preserve the user’s intent, select the right website, recognize when a subtask is complete, and carry useful information forward.

## 2. Research Goal and Objectives

The paper aims to determine whether contemporary language- and multimodal-model-based agents can complete realistic, compositional tasks across multiple changing websites.

Its objectives are to:

1. Introduce **MMInA**, a benchmark of human-written tasks that require multimodal reasoning and navigation across multiple real-world websites.
2. evaluate state-of-the-art LLMs, large multimodal models, and web-oriented agents against human users.
3. Measure both complete-task success and progress at individual hops.
4. Analyze why performance deteriorates as workflows become longer.
5. Test whether replaying earlier action trajectories as procedural memory improves performance.

No formal statistical hypotheses or significance tests are stated.

## 3. Methods (Approach/Design)

### 3.1 Benchmark environment

MMInA operates primarily on evolving, real-world websites. It uses Playwright with web pages simulated on an X graphics server and follows a 1280 × 2048 viewport configuration.

The agent’s text representation of a page is an **accessibility tree**. Each tree node contains:

- An element ID.
- The element type.
- Its textual content.

For an image element, the environment downloads the visible image and paints its element ID onto the image, connecting the visual item to the accessibility-tree representation.

The action space is condensed into **12 action types**, covering operations such as clicking links, scrolling, typing, and returning textual answers. The paper does not enumerate all 12 actions in the supplied text.

A task averages **12.9 actions**. Longer-hop tasks generally require more actions, although five-hop tasks average fewer actions than four-hop tasks because many four-hop tasks contain comparative operations.

### 3.2 Dataset composition

MMInA contains:

- **1,050 tasks**.
- Tasks spanning **1–10 hops**.
- An average of **2.85 hops per task**.
- **14 websites**.
- Both information-seeking and action-oriented subtasks.
- A question-answer pair and supporting materials for every task.
- **108 question-answer pairs filtered from WebQA**.

The text reports **2,989 hops**, whereas Figure 2 labels its domain distribution as covering **2,991 hops**. The supplied paper therefore contains an internal two-hop discrepancy; it does not explain it.

Question styles were adapted from WebQA. GPT-4V generated similar multimodal questions, and annotators manually added questions to increase diversity in style, scope, shopping, search, booking, and other categories.

The prompt supplied to an agent contains:

1. Instructions explaining tasks, accessibility trees, and actions.
2. Rules, including stopping after a `[stop]` action.
3. Small question-answer examples.
4. A list of all websites the agent may visit.
5. The actual multihop task.

Some tasks contain endpoint keywords—for example, an airport’s three-letter code—when a subtask cannot be evaluated using a single uniform rule.

### 3.3 Websites

Table A2 lists the benchmark sites:

- Wikipedia through a Kiwix library.
- Trip.com car rental.
- Momondo flight booking.
- Trip.com hotels.
- Eventbrite.
- Twitter.
- Amazon.
- YouTube.
- Time Out for finding food.
- XE for currency exchange.
- Nomadic Matt for travel guides.
- Allrecipes.
- Trip.com trains.
- OneStopMarket for shopping.

The authors describe all as evolving real-world websites except the offline standalone OneStopMarket shopping site. They also note that the Kiwix Wikipedia URL may change as its library is updated, although this did not affect their experiments.

The formal limitations section additionally says that webpage protections made direct image retrieval unusually difficult, so one utilized website was an offline standalone site and another was open-source. The paper does not identify the second one in that section.

### 3.4 Task domains and intents

Figure 2a distributes the benchmark’s hops across these sources or domains:

| Domain | Share |
|---|---:|
| Wikipedia | 28.4% |
| Shopping | 13.0% |
| Flight | 10.5% |
| Hotel | 10.3% |
| Car rental | 9.2% |
| Twitter | 7.1% |
| YouTube | 6.0% |
| Food | 5.7% |
| Tour guide | 5.6% |
| Transfer | 2.9% |
| Event | 0.9% |
| Train | 0.2% |
| Amazon | 0.2% |
| Recipes | 0.1% |

Figure 2b shows that:

- **64.7%** of hops require an action.
- **35.3%** are information-seeking.

Travel forms much of the multitasking data. A typical construction first asks the agent to infer a destination from Wikipedia and then combines subtasks such as booking flights or hotels, finding guides, exchanging currency, or renting a car. Cooking workflows can combine buying food on Amazon with searching for recipes.

### 3.5 Annotation process

Three trained human annotators constructed MMInA from scratch. They varied in age and gender, were proficient in web browsing, received pre-annotated examples, followed common guidelines, and signed formal agreements.

The annotators:

- Proposed templates with varied intents and difficulty.
- Generated 2–10 tasks per template.
- Labeled different portions of the dataset.
- Cross-validated task diversity and answer accuracy.
- Acted as “omniscient readers” and recorded the shortest successful path with all crucial website nodes.

This is called a **minimalist** protocol. The reference path need only be a subset of an agent’s successful path: agents may visit unnecessary sites as long as they ultimately traverse all required nodes correctly.

### 3.6 Multimodal design

Every MMInA task is described as requiring visual and textual processing over multiple turns. One example asks which of two office chairs appears furrier, requiring image comparison alongside product-page text.

Table A3 contrasts this with a VisualWebArena example that asks a textual Wikipedia question. MMInA’s illustrated example asks whether two visually specified chairs both have armrests, demonstrating reliance on multimodal evidence at multiple stages.

The system automatically extracts accessibility trees and downloads images in the current viewport so that agents receive both structured text and corresponding visuals.

### 3.7 Evaluation

#### Single-hop evaluation

Two methods assess the output or endpoint of a hop:

- **`must_include`:** A response passes only if it includes every required keyword. Missing any keyword produces failure.
- **`fuzzy_match`:** GPT-3.5-Turbo compares the prediction with the reference answer and answers whether the reference can correctly be inferred from the prediction. “Yes” means pass; “No” means fail. This allows semantic equivalences such as “gold” and “yellow.”

#### Multihop evaluation

For an \(N\)-hop task, the evaluator maintains an ordered queue of \(N\) hop-completion conditions plus a final `END` marker.

A hop passes when the agent:

- Produces the required information, such as an answer string; or
- Reaches the required browser state, such as a target URL.

The agent may advance only after completing the current hop. Full-task success requires every hop to be passed in order.

Two metrics are reported:

- **Hop success rate:** percentage of targeted website visits or hop endpoints successfully reached.
- **Task success rate:** percentage of complete tasks solved.

This distinction is important because an agent can make partial progress yet fail to finish the overall chain.

### 3.8 Baselines and experimental setup

The experiments include:

- Open-source pretrained text models such as CodeLLaMA.
- The reasoning model DeepSeek-R1-Distill-Qwen-32B.
- Text decoders associated with multimodal models, including Fuyu-8B.
- API-based language models: GPT-4 and Gemini-Pro.
- Multimodal models: Fuyu-8B, GPT-4V, GPT-4o, and Gemini-Pro-Vision.
- Web-oriented heuristic/trained agents: WebShop and CogAgent.
- Human participants.

Text models were evaluated under:

1. **Text-only input**, ignoring page images.
2. **Caption-augmented input**, using BLIP-2 to caption visible images.

Multimodal agents received page text and images. Table 2 uses icons to distinguish combinations of instructions, accessibility trees, image captions, images, execution histories, and original webpages. Some icons are missing from the extracted text, so the exact input bundle corresponding to every repeated model row cannot be reconstructed with certainty.

The human baseline averages **three test takers** from different socioeconomic backgrounds. They received no prior task information.

Model versions were:

- GPT-4: `gpt-4-0125-preview`.
- GPT-4o: `gpt-4o-2024-11-20`.
- GPT-4V: `gpt-4-vision-preview`.
- Gemini-Pro: `gemini-1.0-pro-001`.
- Gemini-Pro-Vision: `gemini-1.0-pro-vision-001`.

Default model parameters were used. WebShop was trained for a static environment with specially structured queries, so GPT-3.5-Turbo generated appropriately formatted queries for this evaluation.

Local pretrained baselines, mostly with 7B, 8B, or 9B parameters, ran on one NVIDIA RTX6000 Ada GPU with **48 GB** of memory. One inference epoch took approximately **4–8 hours**, depending on the model.

### 3.9 Memory augmentation

The proposed memory framework distinguishes:

- **Semantic memory:** general knowledge stored in model weights and potentially updated from the Internet or knowledge bases.
- **Episodic memory:** the step-by-step trajectory of the currently active task, usually represented in the context or as in-context examples.
- **Procedural memory:** complete trajectories and outcomes of earlier tasks, used to improve strategies on future similar tasks.

The implemented augmentation appends trajectories from the last \(K\) tasks—including task descriptions, actions, and webpage observations—to the prompt. This replay is intended to narrow the search space and ground the agent’s reasoning. It also multiplies prompt length by \(K\).

## 4. Results and Findings

### 4.1 Figure 1: Example multihop workflow

Figure 1 illustrates a four-hop task:

1. Search Wikipedia to determine whether Seoul or Tianjin better matches a city with a Ferris wheel at its center.
2. Use Momondo to book a round-trip flight to Tianjin.
3. Use Trip.com to arrange hotel accommodation in Tianjin.
4. Search YouTube for videos featuring tours of Tianjin.

The diagram shows each website-specific phase receiving its own completion check, followed by overall task evaluation. It demonstrates that the benchmark interleaves information retrieval with real website actions.

### 4.2 Comparison with earlier benchmarks

Table 1 shows that MMInA has the longest and broadest multihop configuration among the listed benchmarks:

| Benchmark | Multimodal | Maximum / average hops | Website setting | Interaction | Websites |
|---|---:|---:|---|---|---:|
| MiniWoB++ | Yes | 1 / 1.00 | Static simplified | Open-ended | 100 |
| WebShop | Yes | 1 / 1.00 | Static simplified | Open-ended | 1 |
| Mind2Web | No | 1 / 1.00 | Static real-world | Multiple choice | 131 |
| RUSS | No | 2 / 1.10 | Static real-world | Multiple choice | 22 |
| WebArena | No | 2 / 1.06 | Static real-world | Open-ended | 6 |
| VisualWebArena | Yes | 2 / 1.05 | Static real-world | Open-ended | 3 |
| WebVoyager | Yes | 4 / 2.40 | Dynamic real-world | Open-ended | 15 |
| MMInA | Yes | **10 / 2.85** | **Evolving real-world** | Open-ended | 14 |

Thus, MMInA is not the benchmark with the most websites, but it combines multimodality, evolving sites, open-ended interaction, and substantially longer task chains.

### 4.3 Task-length and action statistics

Figure 2c shows the distribution of tasks from 2 to 10 hops. Two-hop tasks are by far the most common, at approximately 200; the remaining categories are much smaller. Table A1 gives exact multihop counts for the GPT-4V analysis:

- 2 hops: 200 tasks.
- 3 hops: 44.
- 4 hops: 16.
- 5 hops: 57.
- 6 hops: 60.
- 7 hops: 59.
- 8 hops: 35.
- 9 hops: 30.
- 10 hops: 19.

Figure 3 shows that average actions generally rise with hop count, from only a few actions for the shortest tasks to more than 30 for ten-hop tasks. The exact plotted values are not printed and cannot be read reliably enough to report individually. The five-hop average is lower than the four-hop average because some four-hop tasks involve comparison workflows that demand additional actions.

### 4.4 Main benchmark results

Table 2 reports percentages for hop success and full-task success. The available input-condition labels are partly lost in extraction, but all numerical rows are reproduced below in their printed order.

#### Text-agent rows, first reported input configuration

| Agent | Hop SR: 1 | 2–4 | 5+ | Overall | Task SR: 1 | 2–4 | 5+ | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Fuyu-8B | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| CodeLLaMA-7B | 1.18 | 0 | 0 | 0.29 | 1.18 | 0 | 0 | 0.58 |
| WebShop | 20.67 | 0 | 0 | 4.17 | 20.67 | 0 | 0 | 10.12 |
| DeepSeek-R1-Distill-Qwen-32B | 21.61 | 1.85 | 1.62 | 4.74 | 21.61 | 0 | 0 | 10.46 |
| Gemini-Pro | 19.09 | 34.12 | 2.13 | 11.85 | 19.09 | 0.76 | 0 | 9.54 |
| GPT-4 | 14.37 | 30.56 | 5.23 | 12.26 | 14.37 | 9.09 | 0 | 9.34 |

#### Text-agent rows, second reported input configuration

| Agent | Hop SR: 1 | 2–4 | 5+ | Overall | Task SR: 1 | 2–4 | 5+ | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| CodeLLaMA-7B | 5.71 | 0 | 0 | 1.61 | 5.71 | 0 | 0 | 2.79 |
| WebShop | 29.72 | 0 | 0 | 5.61 | 29.72 | 0 | 0 | 14.55 |
| DeepSeek-R1-Distill-Qwen-32B | 47.68 | 3.84 | 4.68 | 11.11 | 47.68 | 0 | 0 | 23.07 |
| Gemini-Pro | 30.12 | 11.09 | 0.05 | 12.38 | 30.12 | 1.52 | 0.38 | 15.22 |
| GPT-4 | 38.58 | 20.70 | 3.43 | 13.50 | 38.58 | 3.79 | 0 | 19.85 |

These repeated rows appear to represent different text/caption/context inputs, but the lost icons prevent a fully reliable row-by-row mapping.

#### Multimodal-agent rows

| Agent | Hop SR: 1 | 2–4 | 5+ | Overall | Task SR: 1 | 2–4 | 5+ | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| CogAgent-9B | 6.92 | 0 | 0 | 1.06 | 6.92 | 0 | 0 | 3.35 |
| GPT-4o | 21.90 | 9.23 | 0.96 | 5.94 | 21.90 | 3.85 | 0 | 11.61 |
| Fuyu-8B | 27.36 | 0 | 0 | 5.52 | 27.36 | 0 | 0 | 13.39 |
| Gemini-Pro-Vision | 28.94 | 16.38 | 4.03 | 10.66 | 28.94 | 1.51 | 1.13 | 18.40 |
| GPT-4V | 42.91 | 21.23 | 3.99 | 13.89 | 42.91 | 3.03 | 0 | 21.77 |
| GPT-4o, additional input condition | 27.45 | 17.76 | 10.13 | 14.36 | 27.45 | 3.32 | 0 | 14.04 |
| Gemini-Pro-Vision, additional input condition | 39.17 | 23.93 | 4.78 | 14.27 | 39.17 | 10.61 | 1.13 | 20.13 |
| Human | **99.02** | **97.91** | **93.77** | **98.43** | **99.02** | **95.34** | **88.12** | **96.25** |

Key findings include:

- Humans achieved **98.43% overall hop success** and **96.25% overall task success**.
- GPT-4V achieved **21.77% overall task success**, rounded in the main text to **21.8%**, versus the human **96.3%**.
- The strongest printed model result for overall task success is **23.07%** for one DeepSeek-R1-Distill-Qwen-32B input configuration, driven by strong single-hop performance; it still scored zero task success in the 2–4 and 5+ groups.
- GPT-4V had **42.91%** single-hop task success but only **3.03%** for 2–4-hop tasks and **0%** for 5+.
- Gemini-Pro-Vision was one of the few models with nonzero full-task success at 5+ hops: **1.13%**.
- Humans also declined with length, but much less sharply: from **99.02%** one-hop task success to **95.34%** at 2–4 hops and **88.12%** at 5+.
- Fuyu-8B scored zero in the first text configuration but reached **13.39% overall task success** when evaluated multimodally.
- Web-oriented training did not solve the problem: WebShop and CogAgent failed completely on full multihop tasks in their reported rows.

The authors conclude that multimodal models generally outperform purely textual ones and make more accurate benchmark predictions. Models designed for structured or long-context inputs, such as CodeLLaMA and GPT models, are comparatively better suited to accessibility-tree representations. DeepSeek-R1 shows strong single-hop contextual comprehension and planning but deteriorates when it must retain longer multihop context.

Caption augmentation did not uniformly help. In some 2–4-hop cases, Gemini-Pro and GPT-4 without captions outperformed caption-augmented counterparts. Trajectory inspection suggested that under-informed agents sometimes wandered among sites, entered loops, and lost the original objective. This can yield reasonable hop success but poor complete-task success.

### 4.5 Hop-by-hop failure analysis

Table 3 isolates GPT-4V and Gemini-Pro-Vision performance for tasks with 2–6 total hops.

#### GPT-4V hop success by total task length

| Total hops | Hop 1 | Hop 2 | Hop 3 | Hop 4 | Hop 5 | Hop 6 |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 56.50 | 11.00 | — | — | — | — |
| 3 | 22.73 | 4.55 | 0.00 | — | — | — |
| 4 | 12.50 | 0.00 | 0.00 | 0.00 | — | — |
| 5 | 12.28 | 1.75 | 0.00 | 0.00 | 0.00 | — |
| 6 | 16.67 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |

#### Gemini-Pro-Vision hop success by total task length

| Total hops | Hop 1 | Hop 2 | Hop 3 | Hop 4 | Hop 5 | Hop 6 |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 69.28 | 8.43 | — | — | — | — |
| 3 | 32.56 | 0.00 | 0.00 | — | — | — |
| 4 | 40.00 | 0.00 | 0.00 | 0.00 | — | — |
| 5 | 41.67 | 5.00 | 0.00 | 0.00 | 0.00 | — |
| 6 | 31.03 | 1.72 | 0.00 | 0.00 | 0.00 | 0.00 |

Even the first hop becomes harder when embedded in a longer prompt. For GPT-4V, first-hop success falls from **56.50%** in two-hop tasks to roughly **12–17%** in four- to six-hop tasks. Gemini-Pro-Vision also falls from **69.28%** on two-hop tasks to **31.03%** on six-hop tasks.

This is unexpected because a semantically equivalent first subtask should, in principle, have similar difficulty regardless of how many later hops follow it. The authors attribute the reduction to a larger search space and weak zero-shot long-context reasoning.

### 4.6 Extended GPT-4V hop analysis

Table A1 extends the GPT-4V analysis through ten-hop tasks:

| Total task length | Count | Hop-success sequence (%) |
|---|---:|---|
| 2 | 200 | 56.50, 11.00 |
| 3 | 44 | 22.73, 4.55, 0.00 |
| 4 | 16 | 12.50, then 0.00 for hops 2–4 |
| 5 | 57 | 12.28, 1.75, then 0.00 |
| 6 | 60 | 16.67, then 0.00 |
| 7 | 59 | 25.42, then 0.00 |
| 8 | 35 | 40.00, then 0.00 |
| 9 | 30 | 56.67, 20.00, 3.33, then 0.00 |
| 10 | 19 | 52.63, then 0.00 |

The authors caution that results fluctuate for tasks longer than seven hops because there are fewer such samples. Nevertheless, nearly all progress stops after the first or second hop, with the nine-hop group being the only listed long group to reach hop 3 at all.

### 4.7 Why agents fail

The trajectory analysis identifies several failure mechanisms:

- In a single-hop task with one reference URL, an agent tends to keep retrying within that site until it succeeds.
- In a multihop task listing several websites, failure on the expected site often causes the agent to switch prematurely to another site.
- This expands exploration, increases irrelevant actions, and reduces task completion.
- Limited memory causes repeated actions because the agent does not remember earlier progress.
- Agents may fail to detect a hop’s termination condition and continue acting even after the hop is complete.
- Long prompts enlarge the search space and dilute the current objective.
- Task-flow management is therefore a separate difficulty beyond the difficulty of each isolated hop.

### 4.8 Memory augmentation results

Figure 4 diagrams the memory system:

- A multimodal agent exchanges general knowledge with semantic memory.
- Its action trajectories enter episodic memory.
- Completed histories are memorized as procedural memory.
- Similar successful and failed histories are retrieved to guide later behavior.

Figure 5 compares history lengths \(K=0\) through \(K=5\) for Hop 1, Hops 2–4, Hops 5+, and overall performance. Exact bar labels are not printed, so values can only be estimated visually:

- With no history, first-hop performance is roughly in the low 30s and overall performance around 15.
- One or two historical trajectories raise first-hop performance to roughly the high 30s and overall performance to approximately 20–22.
- The 2–4-hop group also improves modestly, to around 10–11 at its best.
- Performance on 5+ hops remains very low, around 1 or less.
- Larger histories, particularly four or five examples, reduce performance relative to the best \(K=1\) or \(K=2\) settings.

The appendix identifies **\(K=2\)** as the typical optimum. In simpler shopping and Wikipedia tasks, \(K=1\) or \(K=2\) works better than larger histories. More examples produce diminishing returns and introduce irrelevant biases or disturbances. The reported memory experiments used Gemini-Pro-Vision, although the technique is designed to be model-agnostic.

## 5. Analysis and Interpretation

The experiments answer the central question negatively: current agents cannot reliably carry out realistic, long, multimodal Internet workflows, even though humans solve them with very high success.

The authors’ interpretation has four main elements:

1. **Multimodality is necessary but insufficient.**  
   Images improve performance because many tasks cannot be solved from text alone. Nevertheless, even leading multimodal agents remain far below humans, especially on complete multihop tasks.

2. **Long workflows change the difficulty of individual steps.**  
   A hop does not behave like an independent single-hop task when placed inside a longer instruction. The additional websites and objectives expand the search space and tax the agent’s context handling. This explains declining first-hop success as total task length grows.

3. **Partial progress must be separated from completion.**  
   A high hop-success rate can coexist with a low task-success rate when the agent visits some correct sites but loses the overall workflow. Reporting only complete-task success, which is frequently zero, conceals where and how failure occurs. Hop-level evaluation provides more diagnostic information.

4. **Procedural experience helps constrain search.**  
   Replaying trajectories from similar tasks gives the model examples of useful action sequences and endpoints. This improves action prediction and execution, but too much history enlarges the prompt and introduces distracting or biased precedents. The resulting relationship between history size and performance is nonlinear.

The authors view multihop browsing as a planning and task-flow problem, not simply the sum of multiple independent website operations. Effective agents need to know which subgoal is active, remember what has already happened, recognize termination conditions, and advance at the correct moment.

## 6. Contributions and Novelty

The paper claims three principal contributions:

- **A realistic multihop, multimodal benchmark:** MMInA supplies 1,050 human-written tasks across 14 diverse websites, with up to 10 hops and an average of 2.85. Tasks require open-ended interaction with evolving web content and combine visual and textual evidence.
- **A holistic evaluation protocol:** It measures both full-task success and hop-level progress, revealing early-hop failures and the relationship between workflow length and behavior.
- **A lightweight memory augmentation method:** It replays earlier action trajectories as procedural memory and improves both single-hop and multihop performance without requiring a model-specific architecture.

Additional practical contributions include a structured observation pipeline that links accessibility-tree nodes to downloaded images and a benchmark design that can be expanded to additional websites.

## 7. Limitations and Caveats

### Explicit limitations

- Website protection mechanisms make it difficult to fetch images directly from HTML.
- The benchmark therefore includes an offline standalone shopping website and an open-source website.
- Biases in the underlying multimodal models may produce inaccurate or unfair outcomes. Users should consider whether model training data are representative.

### Experimental and benchmark caveats

- Dynamic websites frequently change, complicating reproducibility and endpoint evaluation.
- The Kiwix Wikipedia library and its dated URLs may change over time.
- The benchmark’s URL-based evaluation checks whether required sites or states are reached in order, but it does not yet directly evaluate the quality of every individual action.
- Some task endpoints require manually defined keywords because no unified criterion applies.
- Long tasks are relatively scarce, causing volatile success rates beyond seven hops.
- Memory replay increases input length by a factor related to \(K\), which can exceed what models accustomed to shorter contexts handle well.
- Larger memory sets can introduce bias, distraction, and diminishing returns.
- The memory experiment was conducted with Gemini-Pro-Vision; model-agnostic applicability is proposed but not empirically demonstrated for every LLM or LMM in the supplied results.
- Although the environment is described as using evolving real-world sites, one shopping site is offline and standalone.
- The dataset reports 2,989 hops in the text but 2,991 in Figure 2.
- The paper reports no confidence intervals, formal significance tests, or inter-annotator agreement statistic.
- The extracted Table 2 lacks some input-type icons, preventing exact identification of every repeated model row’s input combination.

## 8. Future Work or Open Questions

The authors explicitly propose developing an **action-focused evaluation method** that would assess and directly guide an agent’s operations, rather than relying mainly on endpoint answers and visited URLs.

Other open issues identified by the paper include:

- Improving zero-shot long-context reasoning.
- Enabling agents to manage subgoals and termination conditions reliably.
- Preventing excessive website switching, wandering, and loops.
- Developing stronger episodic and procedural memory.
- Determining how to retrieve relevant histories without overloading the prompt.
- Applying the model-agnostic memory method to other LLMs and LMMs.
- Expanding the flexible benchmark environment to more websites.
- Handling changing content and protected image access more robustly.
- Addressing bias inherited from base multimodal models.

## 9. High-Level Takeaway (Plain Language)

MMInA tests whether an AI agent can do a realistic online chore that spans several websites and requires understanding both words and pictures. Humans complete these tasks about **96%** of the time, while the tested agents usually fail—often during the first few steps—and GPT-4V completes only about **21.8%** overall. Showing an agent a small number of successful past action sequences helps, but too much history becomes distracting. The paper’s main message is that being good at one website at a time is not enough: useful Internet agents must remember progress, manage a long plan, and know when to move from one subtask to the next.