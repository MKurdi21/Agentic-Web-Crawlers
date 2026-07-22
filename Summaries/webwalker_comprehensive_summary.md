# WebWalker: Benchmarking LLMs in Web Traversal

**Authors:** Jialong Wu, Wenbiao Yin, Yong Jiang, Zhenglin Wang, Zekun Xi, Runnan Fang, Linhai Zhang, Yulan He, Deyu Zhou, Pengjun Xie, and Fei Huang  
**Venue:** Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, 2025, pp. 10290–10305

## 1. Background and Context

Retrieval-augmented generation (RAG) lets a large language model retrieve current web information instead of relying only on knowledge fixed during training. This is valuable for open-domain question answering and other changing, knowledge-intensive tasks.

However, ordinary search engines mainly perform **horizontal retrieval**: they return pages that appear directly relevant to a query. They may fail when the required information is buried several clicks deep within an official website or must be combined across multiple subpages. Answering such questions requires **vertical exploration**—opening a root site, following links through its hierarchy, identifying useful pages, and reasoning over the collected information.

Existing web-agent benchmarks do not fully test this capability:

- Mind2Web and WebArena focus mainly on completing instructed actions.
- HTML-based instruction–action tasks may expose agents to very long, noisy inputs that are difficult for models with limited long-context understanding.
- Newer benchmarks increasingly use screenshots and visual interaction.
- AssistantBench and MMInA include time-consuming, multi-page tasks, but the authors argue that previous datasets do not jointly and explicitly evaluate website depth, multiple information sources, and multi-step traversal in question-answering form.

The paper therefore defines **web traversal** as the task of starting from an initial website associated with a query and systematically navigating its pages until enough information has been found to answer the query.

Unlike general-purpose web-action benchmarks, this study restricts the agent’s principal navigation operation to **clicking links**. The intention is to isolate navigation, information seeking, and textual reasoning rather than evaluate arbitrary browser manipulation.

### Comparison with prior benchmarks

Table 1 compares the datasets along four dimensions:

- **Depth:** whether exploration down through a particular website is required.
- **Width:** whether a question requires information from multiple sources.
- **Hop:** whether multiple steps are needed.
- **Number of pages:** the number of webpages represented.

| Benchmark | Language | Format | Depth | Width | Multi-hop | Pages |
|---|---|---|---:|---:|---:|---:|
| Mind2Web | English | Multiple choice | No | No | No | 100 |
| WebArena | English | Action | No | No | No | 6 |
| AssistantBench | English | QA | No | Yes | Yes | 525 |
| MMInA | English | Action | No | Yes | Yes | 100 |
| GAIA | English | QA | No | Yes | Yes | Not reported |
| **WebWalkerQA** | **English and Chinese** | **QA** | **Yes** | **Yes** | **Yes** | **1,373** |

WebWalkerQA is therefore presented as the only benchmark in this comparison that simultaneously covers depth, width, and multi-step navigation in a bilingual QA format.

---

## 2. Research Goal and Objectives

The paper has two central goals:

1. **Create WebWalkerQA**, a benchmark for measuring whether LLM-based agents can navigate deeply through official websites and answer complex questions whose evidence may be buried across one or more subpages.
2. **Develop WebWalker**, a multi-agent baseline that imitates human web navigation through an explorer–critic arrangement, and test whether its vertical exploration can complement the horizontal retrieval performed by RAG systems.

The experiments address three broad questions:

- How capable are existing LLM agents at deep, multi-step web traversal?
- Does an explorer–critic architecture improve on ReAct and Reflexion?
- Can vertical exploration with WebWalker improve conventional RAG, and does allowing more navigation actions improve performance?

---

## 3. Methods (Approach/Design)

### 3.1 WebWalkerQA construction

WebWalkerQA contains:

- **680 manually verified question–answer pairs**
- Information distributed across **more than 1,373 webpages**
- Four domains: conference, organization, education, and games
- Two languages: Chinese and English
- Single-source and multi-source questions
- Three difficulty levels for each source type

The authors use a two-stage “funnel” annotation process.

#### Stage 1: LLM-based annotation

GPT-4o performs the initial work:

1. Recursively traverse selected official websites and collect accessible links and subpages.
2. Generate questions from the collected page information. A question may focus on one deep page or require information from two pages.
3. Verify and filter the generated questions. The retained items must be legitimate, naturally phrased QA pairs with short, entity-like answers.

For multi-source generation, GPT-4o is instructed to construct a standalone, multi-step question that:

- requires at least two intrinsically connected subpages;
- cannot be answered from only one source;
- encourages logical reasoning involving elements such as time or sequence;
- has a precise, concise answer; and
- avoids artificial questions about browsing history or navigation paths.

A strict verification prompt rejects multi-source examples if either document is unnecessary, if the answer is incorrect or too long, or if the question is unnatural.

For single-source data, the verifier checks that current information from the deeper target page is genuinely needed and is not already supplied by a shallower “known knowledge” page. Questions must still require nontrivial multi-step reasoning or calculation and yield concise answers.

#### Stage 2: Human annotation

Crowdsourced annotators rewrite and calibrate the synthetic questions and answers. This quality-control stage is intended to ensure correctness, relevance, consistency, and natural phrasing.

### 3.2 Website selection and data pipeline

Root pages are found through Google queries such as “conference official website” and “game official website,” followed by manual filtering. For education, the authors select official university computer-science department sites.

**Figure 2** shows the full pipeline:

1. Select an official root website.
2. Recursively traverse its URL tree.
3. Collect second-, third-, and fourth-level subpages.
4. Form either single-source examples from one branch or multi-source examples from two pages.
5. Use GPT-4o to generate synthetic QA pairs.
6. Manually verify the pairs to produce the final dataset.

The four source domains were selected because they offer authoritative information and rich clickable structures with sufficient depth for exploration.

### 3.3 Question types and difficulty

A single-source item is labeled `single-source_i`, where \(i\in[2,4]\) is the depth of its target page:

- `single-source_2`: easy
- `single-source_3`: medium
- `single-source_4`: hard

A multi-source item is labeled `multi-source_i`, where \(i\in[2,8]\) is the sum of the depths of the two required pages. For example, a value of 6 could represent two third-level pages or a second-level and a fourth-level page.

The categories are:

- `multi-source_2–4`: easy
- `multi-source_4–6`: medium
- `multi-source_6–8`: hard

Table 2 shows a balanced structure across source types:

| Type | Easy | Medium | Hard | Total |
|---|---:|---:|---:|---:|
| Single-source | 80 | 140 | 120 | 340 |
| Multi-source | 80 | 140 | 120 | 340 |
| **Total** | **160** | **280** | **240** | **680** |

Single-source tasks represent deep investigation of one information path. Multi-source tasks require simultaneous use of two pages and are intended to be harder to solve through ordinary search-engine shortcuts.

### 3.4 Dataset distribution

**Figure 3** reports:

- **Language:** Chinese 60.5%; English 39.5%.
- **Domains:** conference 24.0%, organization 7.9%, education 46.3%, and games 24.0%.

The displayed domain percentages total 102.2%, apparently because the reported values in the paper or figure do not sum exactly to 100%; no correction is supplied in the paper.

### 3.5 Example data format

**Figure 10** shows that each item is stored in JSON with:

- question;
- answer;
- root URL;
- hop/source type;
- domain;
- language;
- difficulty;
- source websites; and
- golden navigation path.

Its example asks for both the ACL 2025 Industry Track submission deadline and the conference venue address. The answer is **March 21, 2025** and **Brune-Kreisky-Platz 1**. It is an English, medium-difficulty, multi-source conference example requiring the Industry Track and venue pages.

Figure 1 illustrates the same general idea: the agent begins at the ACL 2025 root website, clicks into separate “Industry Track Papers” and “Venue” pages, and combines their information to answer one question.

### 3.6 Formal task definition and evaluation

Given a root URL \(U_{\text{root}}\) and query \(Q\), an agent must navigate the website, collect sufficient evidence, and answer \(Q\).

Two metrics are used:

- **Accuracy (acc.):** percentage of questions answered correctly.
- **Action count (A.C.):** average number of actions among successful, correctly answered executions. This measures how long the successful traversal was, not the action count of failed runs.

Because generated answers can vary in wording, exact matching is unsuitable even though answers were designed to be short. GPT-4 evaluates predictions against the reference answer using chain-of-thought prompting.

**Figure 11** provides the evaluator prompt. It asks GPT-4 to act as a teacher, reason step by step, and output `CORRECT` or `INCORRECT` based only on factual accuracy. Differences in punctuation and phrasing are ignored, and extra information is allowed unless it conflicts with the reference.

### 3.7 WebWalker architecture

WebWalker has two agents.

#### Explorer agent: “Think then Explore”

The explorer follows a Thought–Action–Observation process similar to ReAct.

At step \(t\):

- It receives an observation \(O_t=(p_t,l_t)\).
- \(p_t\) is the current page’s Markdown-like content.
- \(l_t\) is a set of clickable HTML buttons or links, each with descriptive button information and a URL.
- It chooses an action \(A_t\), specifically a subpage URL to visit.
- Its policy depends on the accumulated interaction history \(H_t\), which contains previous thoughts, actions, and observations.

Beautiful Soup is used to extract the page’s Markdown content, clickable HTML buttons, and corresponding URLs. Selecting a navigation URL is separate from answering the question.

The explorer repeats this process until either the critic decides that enough information has been collected or the maximum action limit is reached.

#### Critic agent: “Think then Critique”

After every explorer action, the critic receives:

- the original query;
- the current observation; and
- the current action.

It evaluates whether the new page contains useful information. Relevant details are accumulated in a memory \(M\); irrelevant details are rejected. The critic then decides whether the memory is sufficient to answer:

- If sufficient, it returns `judge: true` and generates an answer.
- If insufficient, it returns `judge: false`, and exploration continues.

This memory mechanism is intended to prevent the entire noisy navigation history from overwhelming the agent.

**Figure 4** depicts the complete workflow. In its example, the explorer proceeds through three steps to locate the ACL Industry Track deadline and conference venue, while the critic filters useful observations, updates memory, and eventually combines the deadline **March 21, 2025** with the venue **Brune-Kreisky-Platz 1**.

### 3.8 Experimental setup

The baselines are:

- **ReAct:** repeatedly combines reasoning and actions through Thought–Action–Observation steps.
- **Reflexion:** a single-agent method that uses feedback or reflection to improve subsequent behavior.
- **WebWalker:** the proposed explorer–critic system.

The experiments are zero-shot. Each agent may take at most **15 actions**. Models were selected to have at least a **128K context window** and at least **7 billion parameters**.

The evaluated backbones shown in Table 3 are:

- Closed-source: GPT-4o and Qwen-Plus.
- Open-source: Qwen2.5-7B, 14B, 32B, and 72B Instruct.

The text says that nine models were validated, but the named list and Table 3 contain six distinct backbones; the supplied paper does not reconcile this discrepancy. LLaMA models were excluded because preliminary experiments found limited ability to follow ReAct-format instructions.

Implementation details include:

- Qwen-Agent as the foundation codebase;
- `top_p = 0.8`;
- `crawl4ai` to obtain webpages in a Markdown-like form.

---

## 4. Results and Findings

### 4.1 Main agent comparison

Table 3 contains the central results. Each pair below is **accuracy / successful-run action count**.

#### Closed-source backbones

| Backbone and method | SS Easy | SS Medium | SS Hard | MS Easy | MS Medium | MS Hard | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| GPT-4o ReAct | 53.75/2.53 | 45.00/3.34 | 30.00/5.61 | 32.50/2.34 | 31.43/3.97 | 15.00/6.77 | 33.82/3.83 |
| GPT-4o Reflexion | 56.25/2.91 | 51.43/3.88 | 30.83/5.75 | 35.00/3.67 | 27.14/4.13 | 16.67/7.05 | 35.29/4.27 |
| **GPT-4o WebWalker** | **55.00/2.97** | **50.00/3.43** | **30.00/6.02** | **47.50/4.00** | **34.29/3.85** | **15.83/6.57** | **37.50/4.67** |
| Qwen-Plus ReAct | 48.75/1.67 | 48.57/2.69 | 28.33/4.00 | 35.00/2.60 | 27.86/3.11 | 14.17/6.55 | 33.08/3.03 |
| Qwen-Plus Reflexion | 53.75/3.66 | 40.00/3.79 | 24.17/5.88 | 47.50/3.28 | 30.00/4.07 | 15.00/7.11 | 33.23/4.32 |
| Qwen-Plus WebWalker | 55.00/3.72 | 47.14/3.19 | 30.00/6.13 | 35.00/3.89 | 27.14/4.39 | 15.00/7.38 | 33.82/4.36 |

GPT-4o WebWalker is the strongest overall agent at **37.50% accuracy**, but it still fails on more than 60% of the benchmark. Its most marked category-level gain over GPT-4o ReAct is multi-source easy: **47.50% versus 32.50%**. It does not win every individual category; for example, GPT-4o Reflexion has slightly higher single-source easy, medium, and hard accuracy and slightly higher multi-source hard accuracy.

#### Open-source backbones

| Backbone and method | SS Easy | SS Medium | SS Hard | MS Easy | MS Medium | MS Hard | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| Qwen-7B ReAct | 37.50/3.36 | 18.57/4.88 | 9.17/5.45 | 17.50/3.42 | 11.43/3.62 | 5.83/4.57 | 16.02/2.99 |
| Qwen-7B Reflexion | 37.50/4.03 | 25.00/3.48 | 11.67/4.57 | 30.00/2.66 | 15.71/5.45 | 4.17/7.80 | 19.11/4.07 |
| Qwen-7B WebWalker | 41.25/3.39 | 24.71/3.86 | 12.50/5.93 | 18.75/3.00 | 20.71/3.34 | 5.83/7.28 | 19.85/3.94 |
| Qwen-14B ReAct | 36.25/1.86 | 32.14/2.75 | 15.00/3.61 | 27.50/2.31 | 22.86/3.00 | 5.00/5.00 | 22.35/2.76 |
| Qwen-14B Reflexion | 46.25/2.21 | 34.29/2.83 | 15.00/4.44 | 36.25/2.51 | 22.86/3.34 | 5.83/5.42 | 25.14/3.01 |
| **Qwen-14B WebWalker** | **41.25/2.42** | **41.43/3.24** | **23.33/4.42** | **30.00/3.95** | **22.86/3.56** | **10.00/6.16** | **27.50/3.60** |
| Qwen-32B ReAct | 47.50/2.21 | 35.71/3.20 | 16.67/3.55 | 36.25/2.68 | 18.57/3.00 | 8.33/3.70 | 25.44/2.93 |
| Qwen-32B Reflexion | 42.50/2.52 | 32.86/2.65 | 16.67/3.90 | 31.25/2.84 | 23.57/3.12 | 5.83/5.00 | 23.26/3.00 |
| Qwen-32B WebWalker | 41.25/2.69 | 34.29/4.14 | 22.50/5.14 | 27.50/3.13 | 25.00/3.51 | 10.00/6.08 | 26.02/3.90 |
| Qwen-72B ReAct | 47.50/1.68 | 38.57/2.79 | 20.00/4.04 | 45.00/2.25 | 32.14/3.13 | 10.00/5.41 | 30.73/2.86 |
| Qwen-72B Reflexion | 57.50/3.04 | 44.29/3.88 | 28.33/5.82 | 36.25/3.62 | 25.00/3.60 | 12.50/6.26 | 32.50/4.09 |
| Qwen-72B WebWalker | 58.75/2.70 | 48.57/3.07 | 25.83/5.77 | 35.00/3.57 | 29.29/4.87 | 15.00/7.38 | 33.26/4.32 |

The broad patterns are:

- Closed-source backbones perform better than open-source backbones overall.
- Larger open-source models generally achieve higher accuracy and sustain longer successful traversals.
- WebWalker has the best overall result for each open-source model size in the table except that its advantages are not uniform across every category.
- Reflexion is not universally better than ReAct at every scale; for Qwen-32B, Reflexion’s overall **23.26%** is below ReAct’s **25.44%**. The authors nevertheless describe the aggregate ordering as WebWalker above Reflexion above ReAct.
- Increasing depth or requiring multiple sources usually reduces accuracy sharply.
- Hard multi-source questions are particularly difficult: the best category result is only **16.67%** from GPT-4o Reflexion.
- Longer action counts on hard tasks indicate that successful answers often require deeper navigation.

**Figure 5** plots overall accuracy against action count. WebWalker is shown with triangles, Reflexion with squares, and ReAct with circles. Points nearer the upper-right represent both higher accuracy and longer successful traversal. GPT-4o WebWalker occupies the highest-accuracy region, while small Qwen models appear lower. The graph supports the authors’ claim that stronger models and reflective or memory-based processing enable longer-distance problem solving.

### 4.2 Domain and language results

**Figure 6** uses radar charts to compare Qwen-Plus and Qwen-14B WebWalker across conference, organization, education, and game domains and across Chinese and English.

The authors report two principal findings:

- Conference questions are answered relatively well because their buttons and link labels tend to be explicit and directive, making the correct navigation path easier to infer.
- Chinese and English performance is similar, which they attribute to the tested backbones being pretrained and supervised-fine-tuned bilingually.

Exact point values in the radar plots are too small to read reliably from the supplied image, so they should not be inferred beyond these stated trends.

### 4.3 Error assessment

Failed runs are divided into:

1. Refusing to answer or locating the wrong page.
2. Reasoning errors after relevant information has been reached.
3. Exceeding the maximum of \(K=15\) actions.

**Figure 7** shows stacked error distributions for ReAct and WebWalker with Qwen-14B and Qwen-Plus. The exact segment percentages are not labeled, but the chart shows that:

- Qwen-14B ReAct has the smallest correct segment and a very large “refusal or locating wrongly” segment.
- Adding WebWalker substantially increases the correct portion for Qwen-14B.
- Qwen-Plus has higher correct proportions than Qwen-14B.
- WebWalker generally reduces premature refusal or wrong-page failures, although reasoning and action-limit errors remain.

The authors characterize small ReAct models as “impatient”: they often stop after only a few actions whether or not they have found relevant evidence. Increasing model size and maintaining a critic memory alleviate this behavior, suggesting that failures arise from both noisy long contexts and limitations in the backbone model.

Some failures occur even after the golden page has been visited. These are reasoning failures rather than retrieval failures.

Table 5 gives one example. The question asks how many total hours a person would spend attending Inclusive Connections Lounge activities from December 1–6, 2024, at the MRS Fall Meeting. The correct answer is **66 hours**. An agent may find the correct webpage but still fail because it must understand the schedule and calculate the total time.

### 4.4 RAG systems on WebWalkerQA

Table 4 evaluates closed-book models, five commercial search-enhanced systems, and two open-source RAG systems.

| System | SS Easy | SS Medium | SS Hard | MS Easy | MS Medium | MS Hard | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| Gemini-1.5-Pro, no retrieval | 12.50 | 7.86 | 8.33 | 11.25 | 6.43 | 5.00 | 8.08 |
| o1-preview, no retrieval | 16.25 | 10.00 | 9.17 | 7.50 | 10.71 | 6.67 | 9.85 |
| Doubao | 45.00 | 15.00 | 18.33 | 13.75 | 8.57 | 10.00 | 16.76 |
| Gemini-Search | 40.00 | 32.14 | 29.17 | 30.00 | 23.57 | 17.50 | 27.94 |
| ERNIE-4.0-8K | 52.50 | 30.00 | 28.33 | 21.25 | 18.57 | 30.00 | 28.97 |
| Kimi | 77.50 | 41.43 | 40.83 | 26.25 | 26.43 | 22.50 | 37.35 |
| **Tongyi** | **41.25** | **45.00** | **41.67** | **40.00** | **41.43** | **34.17** | **40.73** |
| Naive RAG | 37.50 | 25.71 | 24.17 | 20.00 | 14.29 | 12.50 | 20.73 |
| MindSearch | 15.00 | 11.43 | 10.83 | 8.75 | 12.14 | 10.00 | 11.32 |
| Reported category average | 37.50 | 24.29 | 23.42 | 19.86 | 18.02 | 16.48 | Not reported |

Key findings include:

- Without retrieval, Gemini-1.5-Pro and o1-preview score only **8.08%** and **9.85%** overall.
- The authors attribute this to WebWalkerQA’s use of dynamically updated official websites, while pretrained knowledge is static and cutoff-limited.
- Table 6 illustrates the issue: when asked where and when the 2025 MRS Fall Meeting would occur, the correct answer is **Boston, Massachusetts, November 30–December 5, 2025**. o1 instead says the information had not been announced as of its October 2023 knowledge cutoff.
- Search-enhanced systems improve substantially, but the best, Tongyi, reaches only **40.73%** overall.
- Kimi is especially strong on single-source easy questions at **77.50%**, but falls to **22.50%** on multi-source hard questions.
- Tongyi is more consistent across categories and achieves the strongest multi-source results.
- Naive RAG reaches **20.73%**, while MindSearch reaches only **11.32%**.
- Multi-source accuracy is generally lower than single-source accuracy.
- Accuracy declines as target information becomes deeper.
- ERNIE may benefit from stronger Chinese search capabilities, according to the authors.

The paper’s first discussion finding is therefore: **RAG systems struggle with questions that require effective web traversal.**

### 4.5 Naive RAG implementation

The study’s naive RAG system:

1. submits relevant query terms to Google;
2. retrieves the top 10 links;
3. concatenates their content with the query; and
4. asks Qwen-Plus to generate the answer.

MindSearch is described as a multi-agent search framework with a WebPlanner and WebSearcher. The commercial systems—Doubao, ERNIE-4.0-8K, Tongyi, Kimi, and Gemini-Search—are accessed through business-oriented APIs.

### 4.6 Combining RAG with WebWalker

The authors treat conventional RAG as horizontal search and WebWalker as vertical website exploration. They integrate a Qwen-Plus-based WebWalker with naive RAG by appending the critic’s accumulated memory \(M\) to the retrieved documents used for answer generation.

**Figure 8** compares standard RAG with RAG plus WebWalker across all six difficulty groups. Performance rises in every category, with particularly visible gains on multi-source questions. The chart indicates approximate improvements from:

- SS easy: about 0.38 to about 0.56
- SS medium: about 0.26 to about 0.52
- SS hard: about 0.24 to about 0.36
- MS easy: about 0.20 to about 0.34
- MS medium: about 0.14 to about 0.30
- MS hard: about 0.13 to about 0.20

These are visual approximations because the paper does not print exact numerical labels for the combined system.

The second discussion finding is: **WebWalker can serve as a vertical-exploration module within an agentic RAG system.**

### 4.7 Scaling the number of actions

The authors vary the maximum action count over \(K\in\{5,10,15,20,25\}\), using Qwen-Plus.

**Figure 9** plots overall performance for standalone WebWalker and RAG plus WebWalker:

- At \(K=5\), WebWalker is approximately 0.25 and the combined system approximately 0.36.
- At \(K=10\), they are approximately 0.28 and 0.39.
- At \(K=15\), they are approximately 0.34 and 0.40.
- At \(K=20\), they are approximately 0.35 and 0.42.
- At \(K=25\), they are approximately 0.35 and 0.42.

At \(K=0\), the plot shows the RAG baseline at roughly 0.20, while standalone WebWalker has no effective traversal performance. Exact values are not printed in the figure, so these readings are approximate.

Performance generally improves as more actions are allowed, although gains begin to flatten at larger values. This supports vertical inference scaling within the tested range.

The third discussion finding is: **scaling the process of following and digging through links is a promising direction for vertical exploration in RAG.**

---

## 5. Analysis and Interpretation

The results support the paper’s central claim that current systems are much better at finding shallow, directly searchable information than at navigating deeply structured websites.

Several pieces of evidence converge:

- Even the strongest WebWalker configuration reaches only **37.50%** on the core agent benchmark.
- The strongest tested RAG system reaches **40.73%**.
- Closed-book systems remain below **10%** overall.
- Accuracy consistently weakens as page depth or the number of required sources increases.
- Hard multi-source questions remain difficult for every method.
- The error analysis shows that agents fail both before and after retrieval: some stop too early or choose the wrong page, while others reach the correct page but cannot reason correctly over it.

The authors interpret longer successful action sequences from larger models as evidence of better long-range information-seeking ability. Stronger models can keep navigating instead of prematurely concluding that the answer is unavailable. Reflection and critic memory also help by filtering noisy observations and retaining only useful evidence.

However, memory does not eliminate all difficulties. Some methods improve overall while losing on particular categories. For instance, WebWalker’s principal value is not guaranteed dominance on every cell of Table 3; it is the ability to support extended traversal and provide useful evidence that can be integrated with retrieval.

The RAG experiments clarify why horizontal and vertical approaches are complementary:

- Search engines efficiently identify broadly relevant documents.
- WebWalker follows internal links to evidence that ordinary search does not retrieve directly.
- Adding critic memory to RAG improves all difficulty levels, especially questions requiring two sources.
- Increasing the navigation budget further improves results, demonstrating a form of inference-time scaling based on exploration depth rather than merely retrieving more documents.

The authors therefore argue that reliable web information seeking requires both **horizontal breadth** and **vertical depth**.

---

## 6. Contributions and Novelty

The paper makes three principal contributions:

- **WebWalkerQA:** a bilingual benchmark of 680 verified QA pairs spanning more than 1,373 pages, four real-world domains, single- and multi-source questions, three difficulty levels, explicit website depth, and multi-step traversal.
- **WebWalker:** a multi-agent explorer–critic framework that navigates via clickable HTML elements, filters observations into a compact memory, and decides when enough information has been gathered to answer.
- **Empirical evidence for vertical RAG exploration:** extensive comparisons show that standard agents and RAG systems struggle with deeply buried information, while combining RAG with WebWalker improves every tested difficulty category and benefits from a larger action budget.

The benchmark’s distinctive feature is its simultaneous evaluation of:

- vertical depth within websites;
- horizontal width across multiple source pages;
- multi-hop interaction;
- bilingual questions; and
- direct question answering rather than generic browser-action completion.

---

## 7. Limitations and Caveats

The authors identify the following limitations.

### Dataset size

WebWalkerQA has only **680 human-verified QA pairs**. The authors note that web-agent questions are expensive and complicated to construct; they compare this size with AssistantBench’s 214 items, GAIA’s 466, and MMInA’s 1,050.

They also possess approximately **14,000 silver QA pairs**, but these have not been carefully human-verified. They may be useful as supplementary training data, but their quality is lower than that of the released verified benchmark.

### HTML-only environment

WebWalker uses the HTML DOM and clickable button information. It does not use screenshots or other visual signals, even though visual page structure could make navigation more intuitive and may contain useful information unavailable through HTML parsing alone.

### Prompted rather than trained agent

WebWalker is operated through prompting in a zero-shot setting. It receives no specialized training in web traversal, which limits how well it can learn effective navigation policies.

### Root URL supplied directly

In the RAG-plus-WebWalker experiment, WebWalker is given the correct root URL. A production RAG system would first need to identify the appropriate official website. The experiment therefore does not fully evaluate end-to-end root-site discovery plus traversal.

### Action and context limits

The principal experiments allow only 15 actions. Figure 9 shows that performance continues to improve when this limit rises to 20 or 25, so the standard cap may prevent some otherwise solvable examples from being completed.

At the same time, longer context introduces noisy information. Small models often cannot manage this noise and may stop prematurely.

### Evaluation by an LLM

GPT-4 rather than exact matching evaluates answer correctness. The evaluator is instructed to reason carefully and ignore harmless wording differences, but the study does not report an independent analysis of evaluator reliability.

### Remaining reasoning failures

Finding the correct page is not sufficient. Tasks involving calculation, temporal reasoning, or interpretation can still fail, as illustrated by the 66-hour MRS example.

### Numerical and reporting caveats

- The displayed domain percentages sum to more than 100%.
- The methods section says nine models were validated, but only six distinct backbones are listed and reported in Table 3.
- Figures 6–9 do not print all plotted values, so some chart-level quantities can only be read approximately.

No statistical significance tests, confidence intervals, or variance estimates are reported in the supplied paper.

---

## 8. Future Work or Open Questions

The paper proposes several next steps:

- **Use the approximately 14,000 silver QA pairs for training**, potentially improving agent performance after further verification or filtering.
- **Add multimodal input**, especially screenshots, so agents can use visual structure alongside HTML-DOM information.
- **Tune agents on golden trajectories** rather than relying only on prompting. Fine-tuning could teach models to choose more effective actions for information-seeking tasks.
- **Integrate WebWalker more completely with RAG.** A future system could:
  1. rewrite the user’s query;
  2. search for the most relevant official websites;
  3. give those sites to WebWalker for vertical exploration; and
  4. combine horizontally retrieved documents with WebWalker’s mined information for generation.
- **Explore larger inference-time navigation budgets.** Figure 9 suggests that increasing the number of allowed actions improves results within the tested range, though the eventual limits, costs, and optimal stopping policy remain unresolved.
- **Improve reasoning after retrieval**, especially for time calculation and other cases where the correct webpage is found but its information is processed incorrectly.

The authors envision WebWalker either as a standalone web-information assistant for a known webpage or as a module inside a larger agentic RAG system.

---

## 9. High-Level Takeaway (Plain Language)

Ordinary web search is good at finding pages related to a question, but it often misses facts hidden several clicks inside a website or spread across different pages. This paper creates a difficult benchmark for that problem and introduces an agent that explores links while a second agent remembers useful evidence and decides when it can answer.

Current systems still perform poorly—the best core WebWalker result is only 37.50%—but combining ordinary RAG search with this deeper link-following process improves performance across every tested difficulty level. The central message is that better web-based question answering will require both broad search across the web and careful exploration down through the structure of individual websites.