# Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge

**Authors:** Boyu Gou*, Zanming Huang*, Yuting Ning*, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, and Yu Su  
**Affiliations:** The Ohio State University and Amazon AGI  
\*Equal contribution.

## 1. Background and Context

Traditional web search is fundamentally user-driven: a person enters a query, receives ranked links, opens multiple pages, and manually combines the information. Search technology has evolved from term-based methods such as TF-IDF through PageRank and supervised learning-to-rank, but this interaction model has remained largely unchanged. Complex questions therefore impose substantial reading, synthesis, and verification work on users.

Agentic search changes that model. The paper defines an agentic-search system as one that autonomously and iteratively tackles complex information-seeking tasks using tools such as search APIs, retrievers, or web browsers. An LLM may decompose a task, reformulate queries, dynamically plan from accumulated evidence, interact with live websites, and synthesize a citation-backed answer.

The field has progressed through three broad types of systems:

- Search-augmented LLM products, such as ChatGPT Search and Perplexity Search.
- Autonomous web agents that browse sites through direct interaction, including visual web agents and OpenAI Operator.
- Deep Research systems that combine reasoning models with search, browsing, coding, and other tools for longer and deeper investigations.

These systems promise to reduce routine cognitive labor and let people concentrate on oversight and decision-making. However, their growing capabilities have created an evaluation problem. A single task may take an hour, involve hundreds of actions across dozens of websites, and produce a long, open-ended answer whose correct content changes over time.

Existing benchmarks inadequately represent this setting:

- Many web-agent benchmarks use short, transactional tasks, often requiring fewer than 10 actions on one website.
- Cross-site search benchmarks commonly make automated grading manageable by using a fixed, time-invariant answer—often one exact string.
- Such benchmarks test useful capabilities but omit realistic tasks requiring a comprehensive answer based on current information.
- Conventional LLM-as-a-Judge evaluation is not considered sufficient for answers containing hundreds or thousands of words and many interdependent requirements.

The authors call this an “evaluation crisis.” Reliable evaluation is needed not only to improve systems but also to establish trust: an agent’s synthesized answer may sound plausible even when it is hallucinated, biased, outdated, or unsupported by its citations.

The paper’s central methodological insight is a **generation–verification asymmetry**. Many different valid answers and search paths may exist, but benchmark designers know in advance what requirements a task imposes. They can therefore build a task-specific evaluation procedure even when they cannot prescribe one fixed answer.

## 2. Research Goal and Objectives

The paper introduces **Mind2Web 2**, a benchmark intended to evaluate the broad spectrum of agentic-search systems on realistic, long-horizon information-gathering tasks involving current web search and browsing.

It addresses two explicit construction questions:

1. How can researchers collect tasks that are sufficiently complex while remaining realistic?
2. How can they automatically and reliably evaluate the complex answers produced by different agentic-search systems?

The work consequently aims to:

- Construct realistic, diverse, laborious, objective, and verifiable tasks, with an emphasis on answers that may change over time.
- Develop an **Agent-as-a-Judge** framework that evaluates both answer correctness and source attribution.
- Compare frontier search products, web agents, and Deep Research systems with one another and with humans.
- Identify current systems’ strengths, failure modes, and requirements for future improvement.
- Validate that the automated judge agents themselves are dependable.

## 3. Methods (Approach/Design)

### 3.1 Benchmark composition

Mind2Web 2 contains **130 tasks**. Each task has a task-specific judge-agent script, and benchmark construction required **at least 1,000 hours of human labor**.

The tasks were designed around four properties:

- **Realistic and diverse:** They represent practical needs across multiple domains.
- **Long-horizon and laborious:** They require sustained searching, browsing, and synthesis.
- **Objective and verifiable:** Their criteria can be checked from the answer and cited webpages.
- **Time-varying where appropriate:** Answers may depend on current prices, availability, or other changing information, although not every task must change over time.

A task had to require at least five minutes of human work. Tasks quickly answerable with one or two queries were avoided.

### 3.2 Domain coverage

The 130 tasks span **six broad domains and 24 subdomains**:

- **Lifestyle & Leisure: 34 tasks**
  - Shopping 10
  - Food & Cooking 6
  - Sports & Fitness 6
  - Health & Medicine 4
  - Pets & Animal Welfare 4
  - Fashion & Beauty 3
  - Hobbies & DIY 1
- **Entertainment: 28**
  - Films & TV Shows 12
  - Gaming & Virtual Worlds 8
  - Live Shows & Performances 4
  - Music 2
  - Books & Reading 2
- **Miscellaneous: 25**
  - General Information 13
  - News 4
  - Legal & Government Services 3
  - Real Estate 3
  - Finance & Investment 2
- **Science & Research: 23**
  - Research & Academia 14
  - Technology & Science 9
- **Career & Education: 11**
  - Education & Learning 6
  - Jobs & Career 5
- **Travel & Transportation: 9**
  - Travel & Accommodation 7
  - Outdoor & Recreation 1
  - Ticketed Activities 1

Figure 1 summarizes the broad-domain shares as approximately 26% Lifestyle & Leisure, 22% Entertainment, 19% Miscellaneous, 18% Science & Research, 8% Career & Education, and 7% Travel & Transportation.

### 3.3 Task collection and validation

All annotators were experienced computer-science students or professionals. Collection involved three groups:

1. **Task proposers** generated ideas from authentic needs or domain guidelines and supplied draft answers or useful URLs.
2. **Refinement experts** worked iteratively with proposers to improve realism, clarity, difficulty, and verifiability or reject unsuitable proposals.
3. **Validation experts** completed each task end to end, checking feasibility, ambiguities, edge cases, and compatibility with URL-based evaluation.

A task entered the benchmark only after independent validation by at least two experts.

Tasks had to be explicit, grammatical, unambiguous, and free of subjective criteria such as “good” or “better.” Domain-specific requirements had to be explained. Both manual and LLM-assisted checks were used to detect ambiguity.

Important exclusions and constraints included:

- No video-understanding tasks or non-English websites.
- No tasks requiring login or inaccessible/paywalled information.
- No rapidly fluctuating answers such as exchange rates.
- Avoidance of tasks explicitly centered on complex reasoning, calculations, or required external tools; evaluated agents were still free to use such tools.
- Avoidance of unverifiable global qualifiers such as “cheapest,” “all,” or “top-k.”
- Attribution generally had to be verifiable from one webpage at a time.
- Information hidden behind extra interactions or dynamic loading was avoided where possible.

### 3.4 Tree-structured rubrics

Each task has a hierarchical rubric. A complex goal is decomposed top-down into simpler criteria. Leaf criteria receive binary scores of **0 or 1**, and their scores are propagated upward.

There are two main node types:

- A **critical node** is an essential condition. If it fails, its parent fails.
- A **non-critical node** can contribute partial credit.

Nodes can also be **sequential**. If an early prerequisite fails, later dependent checks are skipped. For example, if an agent fails to identify the correct research paper, there is no value in checking whether it supplied the first author’s email.

The aggregation rule is a **gate-then-average** strategy:

- If any critical child scores below 1, the parent scores 0.
- If every critical child passes and non-critical children exist, the parent receives their average score.
- If all children are critical and all pass, the parent scores 1.

Critical criteria function as gates rather than incremental partial credit. Partial scoring is allowed only where it represents meaningful progress or utility.

Two task-level metrics are derived from the root:

- **Partial Completion:** mean root score across tasks.
- **Success Rate:** percentage of tasks receiving a perfect root score of 1.

Figure 2 illustrates this with an IKEA task. A required total price of $200–$600 is a critical gate. Each requested piece of furniture can independently contribute partial credit, but an individual wardrobe passes only if all essential checks pass—for example, it is from IKEA, the price is accurate, it is white, and it has two doors.

### 3.5 Judge-agent implementation

Each task’s rubric is implemented as a Python-based, task-specific **judge agent**. The judge receives an answer and its URLs, evaluates every relevant leaf criterion, and aggregates the results.

The agents primarily use two LLM-based components, both powered by **OpenAI o4-mini**:

- **Extractor:** converts answer text into structured fields such as item names, prices, authors, and URLs. It is instructed not to invent or infer absent information and to return null for missing fields.
- **Verifier:** either performs simple factual/logical checks or checks whether a claim is supported by the text and screenshot of a cited webpage. Invalid, inaccessible, or irrelevant pages count as unsupported.

The evaluation toolkit also supports rubric trees, critical and sequential logic, scoring, caching, and short-circuiting. During ordinary evaluation, checks blocked by a failed critical or sequential prerequisite are skipped to reduce time and cost. Short-circuiting was disabled during judge validation so every node could be compared with human judgments.

### 3.6 Automated generation and human refinement

Writing all scripts manually would be prohibitively demanding. The authors therefore used **Claude 3.7 Sonnet** to generate initial scripts from task descriptions, rubric principles, toolkit documentation, examples, common mistakes, and quality guidance.

Scripts underwent:

1. **System-feedback self-debugging:** Code was run to expose runtime problems; error messages were returned to the model until the script executed. OpenAI Deep Research answers supplied realistic extractor inputs while verification calls were temporarily forced to return true.
2. **Self-reflection:** The model repeatedly reviewed correctness, rubric completeness, logical coherence, and edge cases.
3. **First human-validation stage:** Trained annotators inspected every script and corrected rubrics, prompts, and complex sequential/parallel logic.
4. **Second human-validation stage:** For each task, annotators inspected outcomes on one answer from each of six randomly chosen systems. They fixed important general errors without tailoring the rubric to particular answers. Other answers remained held out for later agreement testing.

A custom graphical interface displayed agent answers, cached webpages, rubric trees, and evaluation outcomes.

### 3.7 Rubric and task complexity

Table 2 reports:

| Measure | Average | Minimum | Maximum |
|---|---:|---:|---:|
| Leaf nodes per rubric | 34 | 3 | 357 |
| Total nodes | 50 | 4 | 603 |
| Rubric depth | 4 | 2 | 6 |

Thus, although there are 130 tasks, each contains dozens to hundreds of fine-grained checks.

### 3.8 Benchmark split and maintenance

To discourage test contamination and prevent judge scripts from being used directly as reinforcement-learning reward models:

- The public development set contains **10 tasks**, descriptions, and scripts.
- The private test set contains **120 tasks**, with only task descriptions released.
- Participants submit answers for private evaluation through a maintained leaderboard.

Because websites change, the authors plan periodic task reviews and user-feedback collection. Unavailable or substantially altered tasks will be updated or replaced by tasks of similar scope and complexity. The benchmark is less tied to specific website action sequences than earlier live-web benchmarks because it evaluates final information and allows agents to choose their sources.

### 3.9 Comparison with prior benchmarks

Table 1 compares benchmark horizon, size, answer variability, and evaluation:

| Benchmark | Horizon | Tasks | Time-varying? | Evaluation |
|---|---|---:|:---:|---|
| Online-Mind2Web | Short | 300 | Yes | LLM-as-a-Judge |
| WebVoyager | Short | 643 | Yes | LLM-as-a-Judge |
| Mind2Web-Live | Short | 542 | Yes | Rule |
| BEARCUBS | Short | 111 | No | Manual |
| WebWalkerQA | Short | 680 | No | Answer match |
| GAIA | Medium | 466 | No | Answer match |
| AssistantBench | Medium | 214 | No | Answer match |
| BrowseComp | Long | 1,266 | No | Answer match |
| **Mind2Web 2** | **Long** | **130** | **Yes** | **Agent-as-a-Judge** |

“Short” means fewer than 10 average actions, “Medium” means 10–50, and “Long” means more than 50. The paper presents Mind2Web 2 as the only benchmark in this comparison combining long horizons, time-varying answers, and automated Agent-as-a-Judge evaluation.

### 3.10 Experimental design and systems

The private test set was used for reported system results. Each system was independently run **three times per task**. The study reports means, standard deviations, and **Pass@3**, meaning at least one of the three attempts completely solved the task.

The ten evaluated systems were:

- ChatGPT Search
- Perplexity Pro Search
- OpenAI Operator
- Hugging Face Open Deep Research
- Claude Research
- Grok DeepSearch
- Perplexity Deep Research
- Gemini Deep Research
- Grok DeeperSearch
- OpenAI Deep Research

Systems unable to reliably provide citations or too weak to produce meaningful results were excluded. Hugging Face Open Deep Research was the only open-source system found sufficiently capable and used OpenAI’s **o3** as its base model; the others were closed-source.

Except for Hugging Face’s system, answers were collected manually through web interfaces. Data were gathered between **April and June 2025**. Standardized prompts required every claim to be sourced. Operator and Gemini received strengthened wording because they sometimes neglected citations.

### 3.11 Webpage caching

All unique cited URLs were fetched with Playwright before evaluation. Both normal webpages and PDFs were supported. Text and screenshots were cached so that verification used a stable representation of what the page showed around answer time, especially important for changing prices and other live information.

When websites blocked automation, annotators manually opened them, completed human checks if necessary, and replaced incorrect cached content.

### 3.12 Human comparison

Human performance was measured on a random **30-task subset**, guaranteed to belong to the private test set.

- Seven people participated.
- Each task was independently completed by three people unfamiliar with that task.
- Participants had to pass two simplified trial tasks.
- They used only a clean browser and Google Docs, without AI tools.
- Every claim required a URL.
- A browser extension logged time and visited webpages; sessions were also recorded.
- Participants were not supposed to stop before 30 minutes unless no solution path emerged, but could stop after one hour.

Observed human effort per task was:

| Measure | Average | Minimum | Maximum |
|---|---:|---:|---:|
| Time | 18 min | 8 min | 44 min |
| Websites visited | 8 | 3 | 31 |
| Webpages visited | 110 | 38 | 375 |

The paper notes that these are underestimates because participants could omit steps, make mistakes, stop when blocked, or stop after one hour.

## 4. Results and Findings

### 4.1 Main performance results

Table 3 reports:

| System | Partial Completion | Success Rate | Pass@3 | Time | Answer length |
|---|---:|---:|---:|---:|---:|
| ChatGPT Search | 0.26 ± 0.01 | 0.06 ± 0.01 | 0.11 | <1 min | 314 ± 4 words |
| Perplexity Pro Search | 0.28 ± 0.02 | 0.08 ± 0.01 | 0.12 | <1 min | 408 ± 13 |
| OpenAI Operator | 0.26 ± 0.01 | 0.10 ± 0.01 | 0.17 | 9.74 ± 0.21 min | 160 ± 1 |
| HF Open Deep Research | 0.26 ± 0.01 | 0.11 ± 0.01 | 0.18 | 13.65 ± 0.07 min | 209 ± 3 |
| Claude Research | 0.32 ± 0.03 | 0.10 ± 0.03 | 0.19 | 7.39 ± 0.14 min | 742 ± 1 |
| Grok DeepSearch | 0.40 ± 0.04 | 0.18 ± 0.02 | 0.36 | 2.58 ± 0.14 min | 1,428 ± 16 |
| Perplexity Deep Research | 0.42 ± 0.03 | 0.15 ± 0.03 | 0.26 | 5.67 ± 0.13 min | 585 ± 13 |
| Gemini Deep Research | 0.45 ± 0.03 | 0.18 ± 0.02 | 0.30 | 7.38 ± 0.58 min | 3,357 ± 49 |
| Grok DeeperSearch | 0.52 ± 0.02 | 0.27 ± 0.03 | 0.40 | 5.72 ± 0.27 min | 1,362 ± 24 |
| OpenAI Deep Research | **0.54 ± 0.04** | **0.28 ± 0.04** | **0.40** | 8.40 ± 0.71 min | 559 ± 19 |
| Human, 30-task subset | **0.79 ± 0.01** | **0.54 ± 0.07** | **0.83** | 18.40 ± 1.61 min | 186 ± 27 |

The best agent, OpenAI Deep Research, achieved roughly **50–70% of human performance**, depending on the metric, while taking less than half the human time.

Even humans solved only 54% of tasks perfectly, and the best agent solved 28%. The sizeable differences between partial completion and full success show that agents often make meaningful progress but fail one or more requirements needed for a fully correct answer.

### 4.2 Differences among agent types

Search-augmented products were generally weakest. ChatGPT Search and Perplexity Pro Search answered rapidly but used short search horizons and shallow synthesis.

Most Deep Research systems did better because they are designed or prompted for sustained investigation and comprehensive synthesis. Some combine search APIs with browsing, coding environments, or Python interpreters, allowing more current retrieval and more advanced processing.

Operator underperformed most Deep Research systems despite direct browser interaction. The authors attribute this to the difficulty of operating in noisy webpages, managing large action spaces and long contexts, and maintaining reasoning, planning, and memory over extended sequential interaction. Search agents can also retrieve information in parallel, whereas browser agents typically act sequentially.

### 4.3 Time–performance relationship

Figure 3 plots average Partial Completion against average task time. Its central pattern is that more inference time generally corresponds to better results. This is particularly visible within related system families:

- Short search products complete tasks in under one minute but score around 0.26–0.28.
- Grok DeeperSearch exceeds Grok DeepSearch.
- Perplexity Deep Research exceeds Perplexity Pro Search.
- OpenAI Deep Research reaches the highest agent partial-completion score.
- Humans take the longest and achieve the highest overall score.

The relationship is not perfectly monotonic across unrelated systems—for example, Operator and HF Open Deep Research spend considerable time but remain near 0.26—but longer, productive investigation generally helps.

Pass@3 also improves substantially over single-run success. OpenAI Deep Research, for example, has a 0.28 Success Rate but 0.40 Pass@3; human performance increases from 0.54 to 0.83. Independent attempts therefore provide another form of test-time scaling.

### 4.4 Answer length

Deep Research systems showed two response styles:

- OpenAI and Hugging Face produced relatively concise, targeted responses.
- Gemini and Grok often produced long reports with introductions, findings, summaries, and conclusions.

Greater length did not guarantee greater completion. Gemini produced the longest answers—**3,357 ± 49 words**—but scored below the much shorter OpenAI Deep Research answers of **559 ± 19 words**. The authors warn that excessively long reports can also burden users who want targeted information.

### 4.5 Time-varying tasks

The authors identified **57 explicitly time-varying tasks**, defined as tasks tied to relative dates or times or involving frequently changing information such as product prices.

Figure 4 compares Partial Completion on these tasks with performance on the remaining tasks. Most systems perform worse on explicitly time-varying tasks, supporting the hypothesis that limited live-browsing capability leads to outdated or hallucinated information.

OpenAI Operator and humans are exceptions: both are strong at interacting directly with live websites and perform roughly as well or better on time-varying tasks than on other tasks. Tasks involving advanced filters or visual interpretation likewise favor browser interaction over search APIs.

The authors infer that web browsing is an important component of agentic search and may partly explain OpenAI Deep Research’s advantage over other Deep Research systems.

### 4.6 Error analysis

Human annotators labeled one randomly selected answer from each of five representative systems—ChatGPT Search, Perplexity Pro Search, HF Open Deep Research, OpenAI Deep Research, and Operator—plus human answers on the 30-task subset. One answer could have several error types.

Figure 5 reports the percentage of tasks exhibiting seven errors. Exact bar values are not fully legible in the supplied figure, so the precise percentages should not be inferred. Its visible patterns and the accompanying text show:

- Criteria violations occur across every evaluated agent and among humans.
- Humans’ dominant error is criteria violation.
- Citation violations are particularly prominent for HF Open Deep Research.
- Operator has substantial missing- and invalid-attribution problems.
- Synthesis errors are pronounced for ChatGPT Search and Perplexity Pro Search.
- HF Open Deep Research has many “information not found” failures.
- Humans show no visible incompleteness or invalid-URL failures but do exhibit criteria and synthesis mistakes.

The seven categories are:

1. **Information Not Found:** The system explicitly reports that it could not retrieve requested information.
2. **Partial Missing:** It supplies fewer items or steps than requested.
3. **Criteria Violation:** The answer directly violates a task constraint or contains a factually wrong statement visible from the answer itself.
4. **Invalid Attribution:** A URL is expired, malformed, or fabricated.
5. **Missing Attribution:** A claim lacks a supporting URL.
6. **Synthesis Error:** A relevant source is found, but its information is incorrectly extracted or combined.
7. **Retrieval Error:** The cited source is irrelevant and cannot support the claim.

#### Incompleteness

Non-Deep-Research systems often terminate early because of restricted search steps and weak long-horizon integration. ChatGPT Search, for example, may retrieve relevant sources but fail to assemble all information required across a long time span.

HF Open Deep Research and Operator sometimes fail entire tasks. HF failures frequently result from invalid tool inputs, improperly generated code, or failure to follow the system prompt for invoking search tools. These execution failures can make the agent incorrectly conclude that information is unavailable.

#### Criteria violations

These errors are common for agents and humans. Human mistakes often result from fatigue or insufficient attention—for example, one person incorrectly treated the University of Waterloo as a U.S. institution.

Deep Research systems, especially OpenAI Deep Research, already surpassed humans on this type of careful, exhaustive checking. The paper describes a news-retrieval task with nuanced constraints where all human participants overlooked details, while most agents interpreted the requirements and articles correctly.

#### Invalid and missing attribution

Agents sometimes fabricate URLs instead of visiting pages. HF Open Deep Research, for example, generated a false Amazon link.

Operator also reported incorrect URLs despite navigating to correct pages. In one fellowship task, it reached the proper page but changed a few words in the URL in its final response. The authors associate this with grounding the answer against a very long interaction history and inadequate memory for retrieved information and sources.

Operator often omitted citations because web agents are commonly optimized for navigation or citation-free retrieval rather than sourced report generation. LLMs can likewise output facts directly from parametric memory instead of searching, resulting in unsupported current claims.

#### Unsupported answers

ChatGPT Search and Perplexity Pro Search showed pronounced synthesis errors when integrating extensive source material without advanced tools. Humans also occasionally misread or mistyped information when overloaded; one misspelled the latest Pritzker Prize winner’s name.

Retrieval errors arise when a system finds pages similar to, but not actually satisfying, the request and then fills the gap with plausible unsupported information.

### 4.7 Hallucination

The appendix defines a conservative hallucination rate as the share of tasks with either invalid attribution or an unsupported answer.

- Even the best system, OpenAI Deep Research, hallucinated on **23% of tasks**.
- Every other evaluated system had a hallucination rate of **at least 50%**.

The paper stresses that these are likely underestimates because hallucination may also contribute to error categories not included in this definition.

### 4.8 Human behavior

Humans had no surface-level completeness failures in the analyzed answers: they fulfilled the requested scope and did not hallucinate webpage URLs. Their failures instead arose from carelessness, including:

- Overlooking broad or detailed constraints.
- Misreading or incorrectly extracting webpage content.
- Significant spelling errors.
- Common-sense mistakes.

Some such errors are less likely for agents optimized for exhaustive checking, illustrating a potential complementarity between human judgment and automated legwork.

### 4.9 Reliability of the judge agents

The authors evaluated judge quality on **15 randomly sampled tasks**, using two held-out answers from different systems per task and excluding trivial total failures.

The process had three phases:

1. **Rubric-level assessment:** A knowledgeable evaluator unfamiliar with judge development rated validity and comprehensiveness.
2. **Node-level assessment:** The evaluator manually assigned binary scores to every leaf node.
3. **Validation of disagreements:** An experienced judge developer reviewed discrepancies and discussed them with the evaluator.

Results:

- The evaluator accepted all **15 rubrics**.
- Two received minor suggestions about partial-scoring strictness, but the existing scoring was still considered reasonable.
- There were **35 disagreements among 720 leaf-node judgments**.
- **27 disagreements** were human evaluator mistakes, illustrating the cognitive difficulty of manually judging long answers.
- Of the remaining eight:
  - Three were overly strict or lenient Verifier judgments.
  - Four occurred because necessary webpage information was hidden in collapsed sections unavailable to automated retrieval.
  - One involved inconsistent sources: one cited page gave 2016 and another gave 2017. The current rubric counts a claim as supported if at least one valid source supports it.

Excluding the human errors and the inconsistent-source case, **7 of 720 nodes** were genuine Verifier errors, corresponding to **99.03% correctness**. The paper contrasts this with reported correctness rates below 90% for automated evaluators on simpler web tasks.

## 5. Analysis and Interpretation

The study answers both of its construction questions affirmatively. Complex yet realistic tasks can be collected through expert proposal, iterative refinement, end-to-end validation, and strict design principles. Complex open-ended answers can be evaluated reliably by decomposing requirements into small binary judgments and implementing task-specific workflows.

The results support several interpretations:

- **Long-horizon effort matters.** Systems that spend more useful inference time and use advanced tools generally retrieve and integrate more required information.
- **Multiple attempts matter.** Higher Pass@3 results show that additional trials can convert partial capability into successful completion.
- **Deep Research is a distinct capability level.** Most Deep Research systems outperform short-horizon search products because they sustain investigation and use richer tools.
- **Direct browsing remains essential.** Search APIs alone cannot reliably expose dynamically rendered information, live availability, advanced filters, or visual details.
- **Browsing alone is insufficient.** Operator’s results show that direct interaction must be combined with robust long-term planning, memory, source tracking, and synthesis.
- **More words do not guarantee better answers.** Very long structured reports may still omit criteria or contain unsupported statements and can impose unnecessary cognitive load.
- **Present systems are useful but unreliable.** OpenAI Deep Research approaches a meaningful fraction of human performance in half the time and sometimes exceeds people on exhaustive detail checking, yet its 28% full success and 23% conservative hallucination rate leave substantial room for improvement.
- **Humans and agents have complementary weaknesses.** Humans are more complete and do not fabricate URLs, but fatigue and limited working memory produce careless errors. Agents can automate exhaustive collection but remain prone to hallucinations, missing citations, and system failures.
- **Fine-grained evaluation is necessary.** A single exact answer or one holistic LLM judgment would not expose the distinction between partial progress, full success, correctness, and source support.
- **Judge reliability comes from decomposition and refinement.** The authors attribute 99.03% verified accuracy to the rubric-tree design, automated script-generation pipeline, repeated debugging, and rigorous human validation—not simply to using an LLM judge.

The intended role of agentic search is consequently augmentation rather than unquestioned automation: agents can perform the tedious retrieval and checking while people focus on consequential decisions and oversight.

## 6. Contributions and Novelty

The paper’s main contributions are:

- **Mind2Web 2:** A benchmark of 130 realistic, diverse, long-horizon tasks requiring real-time web search, browsing, and extensive synthesis.
- **Evaluation of open-ended, changing answers:** Unlike long-horizon benchmarks based on fixed answer strings, it accommodates answers that vary across systems and over time.
- **Agent-as-a-Judge framework:** Each task receives a dedicated evaluation agent that checks correctness and source attribution.
- **Tree-structured scoring:** Complex requirements are broken into binary leaf checks with critical gates, partial credit, and sequential dependencies.
- **Scalable judge development:** A reusable toolkit, LLM-based script generation, self-debugging, self-reflection, and two-stage human validation reduce—but do not eliminate—the labor required.
- **Broad system comparison:** Ten frontier systems representing search products, browser agents, and Deep Research systems are evaluated alongside humans.
- **Behavioral measures:** Results include completion time, answer length, three-run variability, and Pass@3 in addition to correctness.
- **Detailed failure analysis:** The study distinguishes incompleteness, criteria violations, invalid or missing citations, synthesis errors, and retrieval errors.
- **Strong validation of automated evaluation:** Human assessment finds a 99.03% node-level correctness rate after excluding human mistakes and one inconsistent-source case.
- **A controlled release strategy:** A public development set and private test set are intended to support development while reducing contamination, overfitting, and misuse as a direct reward model.

## 7. Limitations and Caveats

### Benchmark scope

- The 130 tasks cannot represent every real-world information-seeking scenario.
- Vague and highly subjective questions are deliberately excluded.
- Video, non-English websites, login-dependent content, rapidly changing values, and several kinds of complex reasoning or calculation are outside the benchmark.
- Tasks requiring inseparable verification across multiple webpages are excluded.
- These choices improve objectivity and evaluability but limit generality.

### Attribution assumptions

- URL-based evaluation assumes that cited pages are truthful and credible.
- The benchmark does not evaluate source credibility, misinformation, or the truthfulness of the wider web.
- It assumes important claims can generally be attributed to individual pages.
- Under the current rule, one valid supporting source is sufficient even if another cited source conflicts with it.

### Web retrieval limitations

- Important content may be hidden in collapsed or dynamically loaded sections.
- Four of the judge-evaluation discrepancies arose from precisely this problem.
- Pages change or disappear, requiring continuing benchmark maintenance.
- Pre-caching stabilizes evaluation but cannot eliminate every accessibility problem.

### Reliance on LLM judgments

- The Extractor and Verifier can still make mistakes.
- Seven of 720 reviewed nodes were genuine automated Verifier errors under the paper’s calculation.
- High measured agreement does not make the evaluation infallible.

### Cost and labor

- Benchmark creation required at least 1,000 human hours.
- Script creation remains demanding despite automation.
- Individual rubrics can contain up to 603 nodes.
- Human completion can involve up to 31 websites and 375 webpages.

### Black-box systems

- Most sufficiently capable systems are proprietary.
- The researchers cannot fully explain architectural performance differences.
- Precise inference costs and token usage cannot be estimated.
- The systems were evolving, and the reported answers represent only the April–June 2025 versions.

### Human comparison

- Human performance was measured on only 30 tasks rather than the full set.
- Participants could stop after an hour or when no route became apparent.
- Recorded human effort may therefore underestimate the true effort for complete solutions.

### Benchmark-release risks

Rubric-based grading could enable mass production of reinforcement-learning data, encourage overfitting to benchmark patterns, or amplify biases embedded in rubrics. The authors mitigate this by keeping the private-test rubrics, evaluation scripts, and script-generation pipeline hidden.

### Broader ethical risks

Agentic search may reduce cognitive workload, democratize sophisticated research, and aid decision-making in education, healthcare, commerce, and policy. However, it may also:

- Scale convincing misinformation.
- Enable unauthorized data extraction.
- Repeat biases in web content.
- Produce discriminatory outcomes without oversight.
- Create false confidence through polished but unsupported answers.

The authors position reliable evaluation and attribution checking as a first defense against these risks.

## 8. Future Work or Open Questions

The paper identifies or implies several next steps:

- Improve agents’ ability to browse and extract real-time information from live, dynamic websites.
- Combine browser interaction with stronger long-horizon reasoning, planning, memory, and citation tracking.
- Reduce hallucinated, expired, fabricated, missing, and unsupported citations.
- Improve synthesis over large numbers of sources, possibly through more reliable tool use.
- Post-train or otherwise tailor open-source agent systems rather than relying entirely on off-the-shelf models connected through prompting.
- Explore aggregation logic beyond the benchmark’s current sequential mechanism.
- Handle content hidden behind collapsed or interactive webpage elements.
- Address source credibility and conflicting evidence, which current URL-support evaluation does not solve.
- Expand task coverage toward scenarios presently excluded while preserving objective verification.
- Study inference cost more precisely when system internals become available.
- Maintain the live benchmark by reviewing tasks, soliciting feedback, and replacing or updating tasks affected by website changes.
- Continue timestamped leaderboard evaluation as systems evolve.
- Preserve private test infrastructure to reduce contamination, rubric gaming, and benchmark-specific reinforcement-learning overfitting.

## 9. High-Level Takeaway (Plain Language)

Mind2Web 2 tests whether AI systems can do the kind of web research that normally requires a person to visit many sites, check changing information, combine evidence, and cite every claim. Its 130 tasks are difficult enough that humans fully complete only 54%, while the best tested AI completes 28% and reaches 50–70% of human performance in less than half the time.

The paper’s key innovation is to grade each answer with a task-specific judging agent that breaks the task into many small checks, including whether the answer is correct and whether its links actually support it. This evaluation was 99.03% correct in a detailed human audit. The results show that Deep Research systems are promising and can sometimes outperform tired humans on exhaustive detail work, but they still frequently miss requirements, mishandle current information, or hallucinate sources. The technology is therefore potentially valuable for doing research legwork, but it still needs careful human oversight.