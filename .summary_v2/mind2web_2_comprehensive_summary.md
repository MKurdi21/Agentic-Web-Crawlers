# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Available range | Pages 1–51 |
| Apparently missing pages | None |
| Native/extracted text | Available for all 51 pages |
| Visually rendered pages | 1–9, 18, 22, 26–30, 32–37, and 49 |
| Visual inspection coverage | Partial: all 23 pages mechanically identified as visual candidates were rendered, but pages not selected for rendering were assessed from extracted text only |
| Figures visually inspected | Main Figures 1–5; Appendix Figures D.1 and F.1–F.15 |
| Figure C.1 | Its extracted labels and counts are available on p. 17, but that page was not supplied as a rendered image; interpretation is therefore text-based |
| Tables | Tables 1–3 and both parts of Table 2 are readable from extracted text; Tables 1–3 and Table 2 were also visible on rendered pages |
| Equations | The principal rubric-scoring equation on p. 5 is readable in both extracted text and the rendered page |
| Algorithms/pseudocode | No formally numbered algorithm. Appendix G supplies a 360-line example Python judge-agent script |
| Appendices | Appendices A–H are present on pp. 16–51 |
| Supplementary material | No separate supplementary file was supplied |
| External artifacts referenced but not supplied | Project website, open-source code repository, leaderboard, complete released code, private test data/evaluation scripts, webpage caches, recorded human-study videos, CSV browsing logs, annotation files, and other online resources |
| OCR needed | No. Native text is available, although typography and mathematical notation remain potentially extraction-sensitive |
| Important visual limitation | Figures on rendered pages were inspected directly. Figure C.1 and code/prompt material on unrendered pages were inspected through extracted text, not page images |
| Other limitations | Several plots do not label every numeric point. Values inferred from graphical position are therefore approximate. Figure 5’s small bars do not support reliable exact transcription from the supplied rendering |

**Document type:** a mixed benchmark, methodology, and empirical evaluation paper in artificial intelligence (AI), with systems-evaluation and dataset/benchmark components.

**Source boundary:** Everything below is based only on the supplied paper. Author statements are treated as **[A] author-reported**, visible properties as **[B] directly observable**, calculations as **[C] analyst-derived**, and inferences as **[D] analyst interpretation**. No external information is introduced.

# 1. Plain-Language Orientation

Mind2Web 2 asks a practical question: how should researchers test AI systems that do much more than return search links? Modern *agentic search* systems may plan a complicated search, visit many websites, collect current information, combine it into a long answer, and attach citations. Existing benchmarks commonly test short interactions or questions with one fixed answer. They therefore do not adequately represent tasks whose answers change over time or require dozens of searches.

The authors construct a benchmark of **130 realistic, long-horizon web-research tasks** spanning six broad domains and 24 subdomains. The tasks are intended to be objective and verifiable but sufficiently tedious that a person may need many webpages and substantial time to finish them. At least two validators independently validate every included task, and benchmark construction reportedly required at least **1,000 hours of human labor** (pp. 2, 4, 6, §§3.2, 3.5).

The central methodological contribution is **Agent-as-a-Judge**. Instead of giving one language model a long answer and asking for a single overall rating, the authors build a task-specific evaluation agent. It decomposes the task into a tree of small, mostly binary checks—for example, whether a product comes from the required store, has the correct color, has an accurate price, and is backed by the cited webpage. Critical requirements act as gates; non-critical requirements can yield partial credit (pp. 3–6, §§3.3–3.4).

Ten search systems and human participants are evaluated. The strongest agent, **OpenAI Deep Research**, reaches a partial-completion score of **0.54**, a full success rate of **0.28**, and Pass@3 of **0.40**, versus human values of **0.79**, **0.54**, and **0.83** on the smaller human-study subset. It averages **8.40 minutes**, while humans average **18.40 minutes** (Table 3, p. 7). Because the agent and human samples differ, the comparison is informative but not perfectly like-for-like.

The main empirical message is mixed: Deep Research systems substantially outperform shallow search products and the browser-operating agent on this benchmark, yet even the best agent fully completes only 28% of test tasks per run. Agents particularly struggle with completeness, current/time-varying information, correct synthesis, and citation integrity. The judge-agent validation reports **7 actual Verifier errors among 720 node judgments**, or **99.03% correctness** under the authors’ exclusion rule (pp. 10–11, §4.4).

# 2. Document Roadmap

| Part | Pages | Function |
|---|---:|---|
| Abstract and Figure 1 | 1 | Introduces the benchmark, evaluation method, and headline result |
| §1 Introduction | 2–3 | Motivates long-horizon agentic-search evaluation and states the gap |
| §2 Related Work | 3–4 | Positions Mind2Web 2 against web-agent/search benchmarks and LLM-based judges |
| §3 Mind2Web 2 | 4–7 | Describes task collection, rubric trees, judge agents, statistics, and data split |
| §4 Experiments | 7–11 | Defines the evaluation, presents system and human results, analyzes errors, and validates judges |
| §5 Conclusions | 11 | Restates the benchmark and evaluation contributions |
| References | 12–14 | Lists 47 cited works |
| Appendix A | 16 | Author-stated limitations |
| Appendix B | 16–17 | Broader impacts and ethical considerations |
| Appendix C | 17–19 | Domain distribution, task-design rules, collection pipeline, maintenance |
| Appendix D | 19–23 | Rubric details, prompts, script generation, validation, human judge study |
| Appendix E | 23–25 | System settings, webpage caching, and human-study protocol |
| Appendix F | 26–37 | Error taxonomy and illustrated case studies |
| Appendix G | 38–44 | Complete example judge-agent script |
| Appendix H | 45–51 | Instructions for task creators, human completers, error annotators, and judge evaluators |

The document moves from motivation to benchmark construction, then evaluates systems, and finally uses extensive appendices to expose the operational details needed to interpret the benchmark.

# 3. Background and Context

**Web search** traditionally returns ranked links, leaving users to open pages and synthesize an answer. **Agentic search** instead refers here to systems that autonomously and iteratively tackle complex search tasks using tools such as search application programming interfaces (APIs), retrievers, or direct browser interaction (§2, p. 3).

The paper distinguishes three broad system styles:

- **Search-augmented large language models (LLMs):** rapidly issue limited searches and produce answers, represented by ChatGPT Search and Perplexity Pro Search.
- **Web agents:** manipulate live websites through browser actions, represented by OpenAI Operator.
- **Deep Research systems:** conduct longer searches and more extensive synthesis, sometimes combining search APIs, browsing, and coding tools.

A **search horizon** is the amount of work needed to complete a task, operationalized in Table 1 by average required actions: short is fewer than 10, medium is 10–50, and long is more than 50.

A **time-varying task** has an answer that can change, such as a product price or availability. This is different from a rapidly fluctuating task: the benchmark deliberately excludes quantities such as exchange rates that may change too quickly for stable evaluation (Appendix C.2, p. 18).

**Correctness** asks whether the answer satisfies the task requirements. **Attribution** asks whether its important claims are supported by cited sources. The framework treats these as separate dimensions.

An **LLM-as-a-Judge** makes evaluation judgments using one or a few model calls. The proposed **Agent-as-a-Judge** instead executes a task-specific workflow containing structured extraction, multiple fine-grained judgments, webpage inspection, and programmatic aggregation.

The key rationale is **generation–verification asymmetry**: many different answers or search paths may be valid, but the evaluator can still know in advance what criteria a valid answer must satisfy (§1, pp. 2–3).

# 4. Research Problem and Gap

## Existing problem

Agentic-search outputs can contain hundreds or thousands of words, current facts, many citations, and results gathered over dozens of websites. Evaluating whether such an output is both complete and source-grounded is difficult (§1, pp. 2–3).

## Shortcomings attributed to prior approaches

According to the authors:

- Web-agent benchmarks typically emphasize short, single-site, transactional tasks.
- Open-web benchmarks often make automatic scoring feasible by using predefined, time-invariant, frequently single-string answers.
- Conventional LLM-as-a-Judge evaluation is too coarse for lengthy, structurally complex answers.
- Search-only systems may not access dynamically rendered information.
- A benchmark had not jointly covered search-augmented LLMs, browser agents, and Deep Research systems on long-horizon, time-varying tasks (§2, pp. 3–4).

## Research gap

The missing capability is a reliable and scalable benchmark for **realistic, long-horizon, open-ended, time-varying web research**, including evaluation of both task satisfaction and source attribution.

## Motivation

Reliable evaluation supports system iteration and trustworthiness. When an AI synthesizes rather than merely retrieves information, users need a mechanism capable of detecting plausible-looking unsupported or incorrect statements (§1, p. 2).

## Scope

The benchmark covers information-gathering tasks that are realistic, tedious, clearly specified, and primarily verifiable through answer text and individual cited webpages. It excludes vague tasks, non-English sites, video understanding, logins, very rapidly changing answers, tasks dominated by complex reasoning/calculation, and attribution claims that inherently require inseparable joint verification across multiple pages (Appendix C.2, p. 18; Appendix H.1, pp. 45–47).

# 5. Research Questions / Objectives / Hypotheses

## Explicit construction questions

The paper explicitly gives two questions in §3.1 (p. 4):

1. How can sufficiently complex yet realistic tasks be collected?
2. How can complex answers from different agentic-search systems be evaluated automatically and reliably?

## Objectives

- Build a benchmark of realistic, diverse, long-horizon, objective, verifiable, and often time-varying tasks.
- Create a scalable evaluation framework for correctness and source attribution.
- Compare frontier agentic-search systems with one another and with human performance.
- Characterize common failure modes.
- Validate whether the automated judge agents are reliable enough to support benchmark use.

## Explicit hypothesis

In §4.2 (pp. 8–9), the authors hypothesize that systems with absent or limited browsing will perform worse on explicitly time-varying tasks than on other tasks.

## No formal hypotheses stated elsewhere

Claims about Deep Research systems, test-time scaling, response length, and human–agent differences are presented primarily as evaluation questions or empirical observations, not as preregistered formal hypotheses.

# 6. Assumptions / Threat Model

This is not a cybersecurity study and specifies no adversarial threat model. Its relevant assumptions are evaluation and environment assumptions:

- A cited URL is treated as a suitable provenance unit.
- The framework assumes cited sources are truthful and credible; source credibility assessment is out of scope (Appendix A, p. 16).
- Critical information should ordinarily be verifiable on a single webpage.
- Under the authors’ current rule, one valid supporting source is sufficient even if another supplied source conflicts (§4.4, p. 11).
- Cached page text and screenshots are treated as the source state relevant to evaluation (Appendix E.2, p. 24).
- Extractor and Verifier calls can make sufficiently reliable binary judgments using OpenAI o4-mini.
- Critical nodes encode necessary conditions; non-critical nodes encode meaningful incremental progress.
- A parent containing only critical children passes only when all of them pass.
- Sequential criteria may be short-circuited after an earlier prerequisite fails.
- Answers were collected during April–June 2025; the authors acknowledge that evaluated systems change over time (Appendix E.1, p. 23).
- Weak systems and systems that cannot reliably provide citations are excluded.
- Test scripts and the rubric-generation pipeline remain private to reduce contamination, reward-model abuse, and benchmark overfitting (pp. 6–7; Appendix B, p. 17).

# 7. Methodology

## 7.1 Study design

The work has four interconnected components:

1. Construct 130 web-research tasks.
2. Construct one task-specific judge-agent script per task.
3. Evaluate ten agentic-search systems over three runs per task on a private 120-task test set.
4. Conduct human performance, error-analysis, and judge-reliability studies on smaller subsets.

## 7.2 Task construction

Tasks pass through **Proposal → Refinement → Validation** (§3.2, p. 4; Appendix C.3, pp. 18–19).

- Proposers generate tasks from authentic needs or domain guidance and provide draft answers or relevant URLs.
- Refinement experts revise or reject tasks for realism, clarity, tediousness, objectivity, and verifiability.
- At least two independent validators complete and inspect each surviving task for feasibility, ambiguity, edge cases, and compatibility with URL-based verification.

Task-design constraints require at least approximately five minutes of human effort, public accessibility, no required login, and single-round completion without clarification (Appendix H.1, pp. 45–47).

## 7.3 Dataset composition and split

- Total: **130 tasks**
- Public development set: **10 tasks**, with descriptions and evaluation scripts
- Private test set: **120 tasks**, with descriptions released but scripts withheld
- Explicitly time-varying tasks: **57**
- Broad domains: **6**
- Subdomains: **24**
- Construction labor: at least **1,000 hours**

Figure C.1 reports broad-domain counts: Lifestyle & Leisure 34; Entertainment 28; Miscellaneous 25; Science & Research 23; Career & Education 11; Travel & Transportation 9. These sum to 130.

## 7.4 Rubric-tree architecture

Each task receives a tree of criteria:

- **Leaf nodes:** binary 0/1 checks.
- **Critical nodes:** a failed critical child forces its parent to zero.
- **Non-critical nodes:** contribute to an average and permit partial credit.
- **Sequential nodes:** encode prerequisites and stop later evaluation after an earlier failure.
- **Root node:** yields the final task score in \([0,1]\).

The authors describe this as **gate-then-average** (§3.3, p. 5). Partial credit is meant to represent practically useful progress, not merely the fraction of arbitrary conditions satisfied (Appendix D.1, p. 19).

## 7.5 Judge-agent workflow

Each Python judge agent:

1. Receives an answer and its citations.
2. Uses an **Extractor** to transform relevant answer content into structured fields.
3. Uses a **Verifier** for simple checks or URL-based claim verification.
4. Supplies webpage text and screenshots for URL verification.
5. Executes rubric leaves.
6. Aggregates leaf results upward to the root.

Both LLM-based tools use **OpenAI o4-mini** (§3.4, p. 5). URL extraction must not invent links; missing fields are returned as null. URL verification treats irrelevant, invalid, or inaccessible pages as unsupported (Appendix D.2, pp. 20–21).

## 7.6 Script generation and validation

Because manual coding is expensive, **Claude-3.7-Sonnet** generates initial scripts from task descriptions, rubric principles, toolkit documentation, examples, and error warnings (Appendix D.3, pp. 21–22).

Scripts undergo:

- Runtime self-debugging using system error feedback.
- LLM self-reflection against quality checklists.
- Manual script/rubric inspection.
- Practical validation against one answer from each of six randomly selected systems per task.
- Held-out-answer checking to assess generalization.

Annotators are instructed to correct critical problems without tailoring scripts to particular answers (Appendix D.4, pp. 22–23).

## 7.7 Webpage caching

All unique cited URLs are loaded and cached through Playwright before evaluation. Normal webpages and PDFs are supported. Cached text and screenshots stabilize evaluation against later webpage changes. Blocked pages can be manually accessed and replaced after human verification (Appendix E.2, p. 24).

## 7.8 Agent evaluation

The evaluated systems are:

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

Each is run independently **three times per task**. Hugging Face Open Deep Research uses OpenAI o3 as its base model. Most systems are operated through their web user interfaces, with answers manually collected. A common prompt demands web searching and a source for each claim; Operator and Gemini receive strengthened citation instructions (Appendix E.1, pp. 23–24).

## 7.9 Metrics

- **Partial Completion:** mean root rubric score.
- **Success Rate:** fraction of runs receiving root score 1.
- **Pass@3:** fraction of tasks with at least one successful run among three attempts.
- **Time:** average completion time in minutes.
- **Answer Length:** average number of words.

Table 3 reports means with standard deviations where applicable. The paper does not report inferential significance tests, confidence intervals, p-values, or effect sizes.

## 7.10 Human performance study

A random **Subset-30** is used.

- Seven human completers participate.
- Each task is assigned to three completers.
- Creators/reviewers of a task are excluded from completing that task.
- Participants pass two trial tasks first.
- They use a clean browser, Google Docs, screen recording, and a Chrome activity-timing extension.
- AI tools are prohibited.
- They should not give up without a clear path until 30 minutes and may stop after 60 minutes.
- Every important statement must include a URL source (Appendix E.3, pp. 24–25; Appendix H.2, pp. 47–48).

## 7.11 Error analysis

Human annotators label one randomly selected answer per system per task on Subset-30 for five representative agents plus humans. Multiple error labels may apply to one answer (§4.3, pp. 9–10; Appendix F.1, p. 26).

The seven categories are:

- Information Not Found
- Partial Missing
- Criteria Violation
- Invalid Attribution
- Missing Attribution
- Synthesis Error
- Retrieval Error

## 7.12 Judge-agent reliability study

Fifteen random tasks are sampled, with two held-out answers from different systems per task. One evaluator conducts:

1. Rubric-level assessment.
2. Node-level manual judgments.
3. Developer review of discrepancies and discussion with the evaluator.

Trivial total-failure cases are excluded from sampling (§4.4, pp. 10–11).

## 7.13 Implementation information not supplied

No hardware configuration, inference token counts, temperature settings, random seeds, model snapshots for every product, or precise monetary costs are reported. Black-box systems prevent deeper implementation analysis (Appendix A, p. 16).

# 8. Experiments / Analyses

## X1 — Benchmark-complexity characterization

**Purpose:** Establish that tasks and rubrics are genuinely long-horizon and complex.

**Data:** All 130 task rubrics; human activity logs from Subset-30.

**Measures:** Node count, depth, completion time, websites, and webpages.

**Results:** Rubrics average 34 leaves and 50 total nodes, with maxima of 357 and 603. Human tasks average 18 minutes, eight websites, and 110 webpages; observed maxima are 44 minutes, 31 websites, and 375 webpages (Table 2, p. 6).

**Caveat:** Human effort is underestimated because participants may make mistakes, omit steps, stop after one hour, or give up when no clear route is found.

## X2 — Main system comparison

**Purpose:** Compare ten agentic-search systems across system types.

**Data:** Private 120-task test set, three runs per system per task.

**Metrics:** Partial Completion, Success Rate, Pass@3, time, and answer length.

**Result:** OpenAI Deep Research has the best single-run partial completion and success rate among agents (0.54 and 0.28). It ties Grok DeeperSearch on Pass@3 at 0.40. Humans score higher on all three accuracy metrics on Subset-30 (Table 3, p. 7).

**Caveat:** Human values use Subset-30 rather than the complete 120-task test set; time reporting also differs across systems.

## X3 — Agent-type analysis

**Purpose:** Explain performance differences between shallow search products, browser agents, and Deep Research systems.

**Result:** Search products score 0.26–0.28 partial completion. Most Deep Research systems score higher, reaching 0.54. Operator scores 0.26 despite direct browser access (§4.2, p. 8).

**Authors’ interpretation:** Long-horizon retrieval, parallel search, tools, synthesis, and sustained task focus matter. Browser-only agents face noisy interfaces, long action sequences, and memory/planning problems.

## X4 — Response-length analysis

**Purpose:** Examine whether longer reports imply better completion.

**Result:** Answer lengths range from 160 words for Operator to 3,357 for Gemini Deep Research, yet Gemini’s partial completion is 0.45 rather than the highest 0.54. Grok DeeperSearch produces 1,362 words and scores 0.52; OpenAI Deep Research produces 559 and scores 0.54 (Table 3).

**Supported conclusion:** Greater output length does not necessarily improve completion.

## X5 — Test-time scaling and repeated attempts

**Purpose:** Relate time and repeated attempts to success.

**Evidence:** Figure 3 and comparisons within Grok and Perplexity families; Pass@3 exceeds single-run Success Rate for every system.

**Example:** OpenAI Deep Research improves from 0.28 Success Rate to 0.40 Pass@3; Grok DeeperSearch from 0.27 to 0.40 (Table 3).

**Caveat:** This is observational across different products/configurations, not a controlled experiment holding model and all other factors constant. The paper says related systems “presumably” share underlying models.

## X6 — Time-varying-task analysis

**Purpose:** Test the explicit hypothesis about limited browsing.

**Data:** 57 explicitly time-varying tasks versus the remaining 63 tasks.

**Metric:** Partial Completion.

**Result:** Figure 4 shows most systems performing worse on explicitly time-varying tasks. Operator and humans are approximately equal or better on these tasks.

**Interpretation:** Direct live-web interaction is particularly useful when prices, dates, availability, or visually/dynamically rendered information must be checked.

**Caveat:** Exact per-system subgroup values are not printed in the text or table and can only be estimated visually.

## X7 — Error analysis

**Purpose:** Identify common correctness and attribution failures.

**Data:** Subset-30; one answer per task and system for five agents plus humans.

**Results:** Figure 5 shows different error profiles. The prose identifies criteria violation as the most frequent human category, substantial Information Not Found failures for Hugging Face Open Deep Research, high invalid-attribution incidence for Operator, and pronounced synthesis errors for ChatGPT Search and Perplexity Pro Search.

**Caveat:** Errors are non-exclusive, and the supplied plot does not label exact percentages for each bar.

## X8 — Hallucination analysis

**Purpose:** Estimate tasks affected by clearly attribution-related hallucination.

**Definition:** A task exhibits hallucination if it has Invalid Attribution or Unsupported Answer.

**Results:** OpenAI Deep Research reaches **23%**; every other evaluated agent reaches at least **50%** (Appendix F.2, p. 31).

**Caveat:** The authors call this an underestimate because hallucination may also contribute to other error categories.

## X9 — Judge-agent reliability evaluation

**Purpose:** Determine whether automated evaluation agrees with careful human checking.

**Data:** 15 tasks, two held-out answers per task, 720 leaf-node verifications.

**Results:** All 15 rubrics receive agreement, with minor reservations on two. There are initially 35 human–judge discrepancies; 27 are attributed to human evaluator error. Of the remaining eight, three are Verifier judgment mistakes, four arise from inaccessible collapsed webpage content, and one from conflicting sources. Excluding human mistakes and the source-conflict case, seven nodes count as actual Verifier errors, yielding 99.03% correctness (§4.4, pp. 10–11).

**Caveats:** One evaluator was used; trivial total failures were excluded; the reported correctness depends on how source-access failures and the conflict case are classified.

# 9. Results

## System performance

OpenAI Deep Research is the strongest evaluated agent by Partial Completion (**0.54 ± 0.04**) and Success Rate (**0.28 ± 0.04**). Grok DeeperSearch follows at **0.52 ± 0.02** and **0.27 ± 0.03**. Search-augmented products are much lower: ChatGPT Search at **0.26 ± 0.01** partial completion and Perplexity Pro Search at **0.28 ± 0.02** (Table 3, p. 7).

Humans reach **0.79 ± 0.01** partial completion and **0.54 ± 0.07** success on Subset-30.

**[C] Analyst-derived comparisons:**

- OpenAI Deep Research’s partial completion is \(0.54/0.79 \approx 68.4\%\) of the human value.
- Its success rate is \(0.28/0.54 \approx 51.9\%\) of the human value.
- Its average time is \(8.40/18.40 \approx 45.7\%\) of human time.
- The human–agent gaps are **0.25** in partial-completion score and **26 percentage points** in full-task success.

These reproduce the authors’ “50–70% of human performance while spending less than half the time” characterization, but the differing evaluation subsets remain important.

## Full completion remains difficult

Every agent has a large gap between partial completion and full success. OpenAI Deep Research scores 0.54 partially but succeeds fully on only 28% of runs. This supports the authors’ conclusion that agents often make meaningful progress but miss at least one essential condition (§4.2, pp. 7–8).

## Multiple attempts help

Pass@3 exceeds Success Rate for every system. For example:

- Grok DeepSearch: 0.18 → 0.36
- OpenAI Deep Research: 0.28 → 0.40
- Humans: 0.54 → 0.83

These are differences in task-level evaluation measures, not guaranteed probabilities under an independence model.

## Time and performance

Figure 3 places stronger agents generally farther right and higher, but time alone does not determine quality. HF Open Deep Research spends 13.65 minutes for a score of 0.26, while Grok DeeperSearch spends 5.72 minutes for 0.52. System design and reliability therefore matter alongside inference time.

## Time-varying tasks

Figure 4 supports the stated hypothesis for most systems: explicitly time-varying tasks receive lower partial-completion scores. Operator and humans are exceptions or near-exceptions, consistent with their ability to inspect live websites.

## Citation and synthesis failures

Appendix F documents fabricated or broken links, absent citations, relevant sources that do not support the claimed fact, and valid sources whose contents are misread. Even the best system has a reported 23% hallucination rate under the paper’s restricted operational definition (p. 31).

## Judge reliability

The reported 99.03% node-level correctness supports the feasibility of structured automated evaluation. It does not establish perfect evaluation: collapsed content, inconsistent sources, and strictness/leniency mistakes remain observed failure modes.

# 10. Figure-by-Figure Interpretation

### Figure 1 — Benchmark and evaluation overview

- **Location:** p. 1.
- **Type:** Conceptual overview with an IKEA shopping example.
- **Content:** A realistic task requests five white IKEA items within a $200–$600 total budget. An answer contains item descriptions and citations. A judge agent checks task requirements and source support.
- **Flow:** Task → agentic search → cited answer and webpages → task-specific judge → correctness and attribution results.
- **Visible result:** The illustrated answer receives partial completion 0.4 and overall failure.
- **Domain inset:** Lifestyle & Leisure 26%, Entertainment 22%, Science & Research 18%, Career & Education 8%, Travel & Transport 7%, Miscellaneous 19%.
- **Conclusion supported:** Evaluation must decompose an answer into detailed correctness and citation checks.
- **Caveat:** This is an illustrative example, not an experimental result.

### Figure 2 — Tree-structured rubric

- **Location:** p. 5.
- **Type:** Hierarchical evaluation diagram.
- **Top-down path:** The task is decomposed into parent and leaf criteria.
- **Bottom-up path:** Binary leaf results propagate upward.
- **Example leaves:** Whether a wardrobe is from IKEA, its price is accurate, it is white, and it has two doors.
- **Critical gate:** The total must be within $200–$600.
- **Visible aggregate:** Root score 0.6 in the schematic.
- **Visual encoding:** Blue nodes denote critical nodes; labels show 0/1 outcomes and the computed parent/root values.
- **Conclusion supported:** A tree can combine hard constraints with partial progress more meaningfully than a single holistic judgment.

### Figure 3 — Partial completion versus time

- **Location:** p. 8.
- **Type:** Scatter plot.
- **X-axis:** Average time in minutes, approximately 0–20.
- **Y-axis:** Partial Completion, 0–0.9.
- **Points:** Ten systems and humans.
- **Exact values:** Available in Table 3 rather than labeled on the plot.
- **Main pattern:** Humans occupy the highest-time/highest-performance position. OpenAI Deep Research is the highest agent point. Search products cluster at very low time and low performance.
- **Qualification:** The relationship is not monotonic—HF Open Deep Research is slow but low-performing.
- **Conclusion supported:** More inference time can help, especially in comparisons within product families, but time is not sufficient by itself.

### Figure 4 — Time-varying versus other tasks

- **Location:** pp. 8–9.
- **Type:** Two-series line plot across systems.
- **X-axis:** Systems, ordered roughly from weaker agents through stronger agents to humans.
- **Y-axis:** Partial Completion, 0–1.
- **Legend:** Explicitly time-varying tasks versus other tasks.
- **Main observation:** The explicitly time-varying series is below the other-task series for most systems; Operator and humans are approximately level or better on time-varying tasks.
- **Exactness:** Individual values are **approximate visual estimates** because the plot does not print them.
- **Conclusion supported:** Live browsing appears important for current information.

### Figure 5 — Error incidence

- **Location:** p. 9.
- **Type:** Grouped bar chart.
- **X-axis:** Seven error categories.
- **Y-axis:** Percentage of tasks, approximately 0–60%.
- **Series:** ChatGPT Search, Perplexity Pro Search, OpenAI Operator, OpenAI Deep Research, HF Open Deep Research, and humans.
- **Main observations:** HF Open Deep Research has a particularly large Information Not Found bar; Operator has a high Invalid Attribution bar; criteria violations occur across agents and humans; human errors concentrate in criteria and synthesis rather than incompleteness or fabricated links.
- **Exactness:** Exact bar heights are not labeled and cannot be transcribed confidently from the supplied rendering.
- **Caveat:** A task can receive multiple error labels, so percentages need not sum to 100%.

### Figure C.1 — Domain hierarchy and counts

- **Location:** p. 17.
- **Inspection status:** Caption and extracted labels inspected; no rendered page supplied.
- **Content:** Six broad domains split into 24 subdomains.
- **Broad counts:** 34, 28, 25, 23, 11, and 9, summing to 130.
- **Examples:** Lifestyle & Leisure contains Shopping, Food & Cooking, Sports & Fitness, Health & Medicine, Pets & Animal Welfare, Fashion & Beauty, and Hobbies & DIY.
- **Conclusion supported:** The benchmark spans multiple practical domains.
- **Limitation:** Layout, arrows, colors, and other visual encodings cannot be independently assessed.

### Figure D.1 — Judge-validation interface

- **Location:** p. 22.
- **Type:** Graphical user interface screenshot.
- **Content:** Task/answer material, a cached webpage, and a rubric/evaluation panel are visible side by side.
- **Purpose:** Supports annotators in inspecting agent answers, evidence pages, rubrics, and judge outcomes.
- **Conclusion supported:** Manual refinement is aided by a dedicated integrated interface.
- **Caveat:** Small interface text is not fully legible, but the main regions and workflow are visible.

### Figure F.1 — Error-classification workflow

- **Location:** p. 26.
- **Type:** Flowchart.
- **Correctness branch:** Completeness check → complete/satisfactory or incompleteness; incompleteness divides into Information Not Found and Partial Missing. A criteria check can produce Criteria Violation.
- **Attribution branch:** Supported, Invalid Attribution, Missing Attribution, or Unsupported Answer. Unsupported answers are separated by source relevance into Synthesis Error and Retrieval Error.
- **Methodological role:** Standardizes human error labeling while keeping correctness and attribution conceptually distinct.

### Figure F.2 — Information Not Found example

- **Location:** p. 27.
- **Visible case:** Perplexity Pro Search is asked for annual Mazda3 production numbers from 2012–2023 but explicitly reports that the requested values are unavailable.
- **Lesson:** Honest failure is still incompleteness rather than hallucination.

### Figure F.3 — Partial Missing example

- **Location:** p. 27.
- **Visible case:** ChatGPT Search supplies Nobel Physics winner information only through 2014 although 2004–2024 was requested.
- **Lesson:** A partially populated list fails an explicit coverage requirement.

### Figure F.4 — Criteria Violation example

- **Location:** p. 28.
- **Visible case:** Operator returns white IKEA items but totals **$1,277.97**, violating the stated **$200–$600** budget.
- **Lesson:** Locally plausible items do not compensate for violation of a global hard constraint.

### Figure F.5 — Invalid Attribution example

- **Location:** p. 28.
- **Visible case:** Operator reports links that mimic Federal Reserve and Reuters URL patterns but do not resolve correctly.
- **Lesson:** Correct-looking link syntax is not proof of valid provenance.

### Figure F.6 — Missing Attribution example

- **Location:** p. 29.
- **Visible case:** Operator states Nobel laureates’ birthplaces without supplying supporting URLs for those claims.
- **Lesson:** A potentially correct fact still fails the benchmark’s attribution requirement when evidence is absent.

### Figure F.7 — Retrieval Error example

- **Location:** p. 29.
- **Visible case:** ChatGPT Search cites a Marvel Rivals page about team-up abilities while claiming broader character ability details.
- **Lesson:** A page may be topically related yet insufficiently relevant to support the specific claim.

### Figure F.8 — Synthesis Error example

- **Location:** p. 30.
- **Visible case:** Perplexity Pro Search retrieves relevant papers but gives wrong author and submission details.
- **Lesson:** Retrieval can succeed while synthesis fails.

### Figure F.9 — Human Criteria Violation

- **Location:** p. 32.
- **Visible case:** A human labels the University of Waterloo as a United States institution.
- **Lesson:** Humans can overlook explicit categorical constraints during tedious work.

### Figure F.10 — Human Synthesis Error

- **Location:** p. 32.
- **Visible case:** A human misspells the Pritzker Prize winner’s name as “Lia” rather than “Liu” Jiakun.
- **Lesson:** Small transcription errors can invalidate an otherwise strong answer.

### Figure F.11 — HF Open Deep Research system failure

- **Location:** p. 33.
- **Visible case:** The agent claims no web-search tool is available even though its trace shows a malformed tool/code invocation.
- **Lesson:** Information Not Found may arise from orchestration failure rather than lack of web evidence.

### Figure F.12 — Operator memory/reporting failure

- **Location:** p. 34.
- **Visible case:** Operator navigates to a correct fellowship page but reports a slightly different invalid URL.
- **Lesson:** Browser access does not guarantee that the final answer faithfully preserves visited sources.

### Figure F.13 — OpenAI Deep Research missing attribution

- **Location:** p. 35.
- **Visible case:** The system correctly identifies an actor but gives the identifying claim without a supporting source.
- **Author interpretation:** The fact may have come from parametric memory rather than real-time retrieval.
- **Certainty:** The causal explanation is an author inference, not directly demonstrated.

### Figure F.14 — Perplexity limited-search failure

- **Location:** p. 36.
- **Visible case:** Perplexity fails to find a discoverable connection between Chris Evans and a pre-1920 U.S. president.
- **Lesson:** Limited search steps can cause premature negative conclusions.

### Figure F.15 — ChatGPT synthesis/attribution mismatch

- **Location:** p. 37.
- **Visible case:** The system retrieves relevant Nobel-related pages but associates sources with incorrect laureate information across a 20-year task.
- **Lesson:** Broad temporal coverage stresses evidence alignment and synthesis.

# 11. Table-by-Table Interpretation

### Table 1 — Benchmark comparison

- **Location:** p. 6.
- **Columns:** Horizon, number of tasks, time-varying status, and evaluation method.
- **Compared benchmarks:** Online-Mind2Web, WebVoyager, Mind2Web-Live, BEARCUBS, WebWalkerQA, GAIA, AssistantBench, BrowseComp, and Mind2Web 2.
- **Key contrast:** Mind2Web 2 is listed as long-horizon, time-varying, and evaluated by Agent-as-a-Judge.
- **Largest benchmark:** BrowseComp, 1,266 tasks, long horizon, but time-invariant with answer matching.
- **Interpretation:** Mind2Web 2 occupies a combination not represented by the listed alternatives.
- **Caveat:** The characterization of other benchmarks is author-reported; this closed-document analysis does not independently verify it.

### Table 2(a) — Rubric complexity

| Measure | Average | Minimum | Maximum |
|---|---:|---:|---:|
| Leaf nodes | 34 | 3 | 357 |
| Total nodes | 50 | 4 | 603 |
| Depth | 4 | 2 | 6 |

The large maxima show that some tasks require hundreds of checks. The averages show this is not merely a collection of single-answer questions.

### Table 2(b) — Human effort on Subset-30

| Measure | Average | Minimum | Maximum |
|---|---:|---:|---:|
| Time | 18 min | 8 min | 44 min |
| Websites | 8 | 3 | 31 |
| Webpages | 110 | 38 | 375 |

The webpage count is much larger than the website count, indicating repeated inspection within sites. Recorded maxima remain below the allowed one-hour cutoff, but the authors warn these figures may underestimate true requirements.

### Table 3 — Main evaluation results

| System | Partial Completion | Success Rate | Pass@3 | Time (min) | Answer Length |
|---|---:|---:|---:|---:|---:|
| ChatGPT Search | 0.26±0.01 | 0.06±0.01 | 0.11 | <1 | 314±4 |
| Perplexity Pro Search | 0.28±0.02 | 0.08±0.01 | 0.12 | <1 | 408±13 |
| OpenAI Operator | 0.26±0.01 | 0.10±0.01 | 0.17 | 9.74±0.21 | 160±1 |
| HF Open Deep Research | 0.26±0.01 | 0.11±0.01 | 0.18 | 13.65±0.07 | 209±3 |
| Claude Research | 0.32±0.03 | 0.10±0.03 | 0.19 | 7.39±0.14 | 742±1 |
| Grok DeepSearch | 0.40±0.04 | 0.18±0.02 | 0.36 | 2.58±0.14 | 1,428±16 |
| Perplexity Deep Research | 0.42±0.03 | 0.15±0.03 | 0.26 | 5.67±0.13 | 585±13 |
| Gemini Deep Research | 0.45±0.03 | 0.18±0.02 | 0.30 | 7.38±0.58 | 3,357±49 |
| Grok DeeperSearch | 0.52±0.02 | 0.27±0.03 | **0.40** | 5.72±0.27 | 1,362±24 |
| OpenAI Deep Research | **0.54±0.04** | **0.28±0.04** | **0.40** | 8.40±0.71 | 559±19 |
| Human* | 0.79±0.01 | 0.54±0.07 | 0.83 | 18.40±1.61 | 186±27 |

- **Best agent partial completion/success:** OpenAI Deep Research.
- **Best agent Pass@3:** Tie between OpenAI Deep Research and Grok DeeperSearch.
- **Longest answers:** Gemini Deep Research.
- **Fastest:** Both search products, under one minute.
- **Human footnote:** Human results use Subset-30.
- **Statistical limitation:** Standard deviations are reported, but no significance testing is supplied.

# 12. Diagram / Architecture Interpretation

The core architecture is a task-specific evaluation pipeline:

```text
Task requirements
       ↓
Tree-structured rubric
       ↓
Answer + cited URLs
       ↓
Extractor → structured claims/items/URLs
       ↓
Verifier ── simple logical checks
         └─ URL checks using cached text + screenshots
       ↓
Binary leaf judgments
       ↓
Critical gates / sequential dependencies / non-critical averages
       ↓
Root score → Partial Completion and Success
```

Three control mechanisms matter:

- **Critical gating:** Failure of an essential condition zeros the parent.
- **Sequential short-circuiting:** Later dependent checks are skipped when an earlier prerequisite fails.
- **Parallel/non-critical evaluation:** Independent useful components can contribute partial credit.

The development architecture is:

```text
Task + rubric principles + toolkit documentation
                  ↓
Claude-3.7-Sonnet script generation
                  ↓
Runtime self-debugging
                  ↓
Checklist-guided self-reflection
                  ↓
Manual rubric/script inspection
                  ↓
Testing on six sampled system answers
                  ↓
Held-out-answer validation
                  ↓
Final judge agent
```

The error-analysis architecture in Figure F.1 is separate from scoring. It helps humans diagnose why an answer failed rather than calculate its benchmark score.

# 13. Equations and Mathematical Concepts

## Rubric aggregation equation

**Location:** §3.3, p. 5.

For node \(v\), let:

- \(C(v)\): all children of \(v\)
- \(K(v)\subseteq C(v)\): critical children
- \(N(v)=C(v)\setminus K(v)\): non-critical children
- \(s(v)\in[0,1]\): node score

The paper defines:

\[
s(v)=
\begin{cases}
0, & \text{if some }u\in K(v)\text{ has }s(u)<1,\\[4pt]
\frac{1}{|N(v)|}\sum_{u\in N(v)}s(u),
& \text{if all critical children pass and }|N(v)|>0,\\[6pt]
1, & \text{otherwise.}
\end{cases}
\]

### Plain-language meaning

1. If any mandatory child fails, the parent fails.
2. If all mandatory checks pass and optional/incremental children exist, average those incremental scores.
3. If the node has no non-critical children and all critical children pass, give the parent 1.

This recursively turns binary leaf judgments into a fractional root score.

### Example

If a requested wardrobe must be from IKEA, white, correctly priced, and have two doors, and all four are critical, the wardrobe node is 1 only if all four pass. If the overall task asks for five independent qualified furniture items and those item nodes are non-critical, satisfying three of five can contribute \(3/5=0.6\), provided any global critical gate—such as the total budget—passes.

### Metrics derived from the root

For task scores \(r_1,\ldots,r_T\):

\[
\text{Partial Completion}=\frac{1}{T}\sum_{i=1}^{T}r_i.
\]

The prose defines this average, although it does not print the formula.

\[
\text{Success Rate}=\frac{1}{T}\sum_{i=1}^{T}\mathbf{1}[r_i=1].
\]

Pass@3 is the fraction of tasks for which at least one of the three attempts has root score 1.

### Mathematical caveats

- The score is rubric-dependent: changing criticality, decomposition, or partial-credit structure can change the result.
- The equation assigns equal weight to non-critical siblings unless the implementation introduces structure that indirectly changes weighting.
- Sequential scoring is described operationally, but a separate formal equation for sequential aggregation is not supplied.
- Footnote 2 states that more general sequential logic remains future work.

# 14. Interpretation and Discussion

The benchmark’s central finding is that long-form web research is not solved merely by connecting a language model to search. Strong performance requires persistence, source tracking, synthesis, constraint satisfaction, and often interaction with live websites.

The two construction questions receive concrete answers:

1. **Collecting realistic complex tasks:** use explicit design principles, three-stage expert curation, end-to-end completion, and validation by at least two independent validators.
2. **Evaluating complex answers:** use task-specific rubric trees whose leaves are small checks and whose agents combine structured extraction, webpage verification, and programmatic aggregation.

The time-varying-task hypothesis is supported descriptively: most systems score lower on the 57 explicitly time-varying tasks, whereas humans and Operator—both equipped for direct website interaction—do not show the same consistent disadvantage. No inferential test is reported, so “supported” here means consistent with the plotted descriptive evidence.

Deep Research systems generally outperform shallow search products, but architecture labels alone do not guarantee success. HF Open Deep Research scores only 0.26 because system/tool-use failures cause premature termination. Operator’s live browsing also does not translate into high overall performance because final-source reporting, long-term memory, planning, and information synthesis remain weak.

The results complicate any simple “longer is better” story. Gemini produces more than 3,000 words on average but is below two more concise systems. The benchmark rewards satisfaction of fine-grained requirements rather than apparent report comprehensiveness.

Humans remain substantially stronger overall, but their errors differ from agent failures. Humans reportedly finish requested coverage and do not fabricate webpage URLs, yet make constraint, transcription, or synthesis mistakes under cognitive load. This supports the authors’ broader idea that agents may complement human oversight, even before they match overall human accuracy.

The reliability study provides important evidence for Agent-as-a-Judge, but it also identifies boundary conditions: webpage state may hide evidence, sources may disagree, and the Verifier can be too strict or lenient. The framework is therefore highly reliable under the reported protocol rather than infallible.

No clear internal numerical contradiction was found between Tables 2–3 and the associated prose. The main comparability caution is that agent aggregate results use the private test set while human results use Subset-30.

# 15. Contributions and Novelty

## Conceptual

- Frames realistic agentic-search evaluation as simultaneous measurement of correctness and attribution.
- Uses generation–verification asymmetry to evaluate open-ended, time-varying answers.

## Methodological

- Introduces tree-structured, task-specific Agent-as-a-Judge evaluation.
- Combines critical gates, partial-credit nodes, and sequential dependencies.
- Separates fine-grained extraction from verification.

## Benchmark/data

- Provides 130 curated tasks across six broad domains and 24 subdomains.
- Includes 57 explicitly time-varying tasks.
- Uses a 10-task public development and 120-task private-test structure.

## System/implementation

- Develops reusable rubric-management, Extractor, Verifier, caching, and visualization tools.
- Uses LLM-based script generation with autonomous debugging and human refinement.
- Supplies an example 360-line judge script in Appendix G.

## Experimental

- Compares ten frontier systems representing search products, Deep Research tools, and a browser agent.
- Includes a seven-participant human study.
- Measures time, answer length, partial completion, full success, and repeated-attempt success.

## Empirical

- Documents large performance gaps between system classes.
- Shows descriptive evidence of difficulty on time-varying tasks.
- Develops an error taxonomy with system- and human-specific cases.
- Reports 99.03% judge-node correctness under the authors’ adjudication rule.

# 16. Limitations

## Authors’ stated limitations

From Appendix A (p. 16) and related sections:

1. **Coverage and scope:** 130 tasks cannot represent every real information-seeking scenario. Vague and highly subjective queries are excluded.
2. **URL truth assumption:** A cited page is assumed credible; source truthfulness and credibility are not evaluated.
3. **Single-page attribution assumption:** Critical facts must be independently verifiable from individual pages.
4. **LLM judgment fallibility:** Extractor and Verifier may make mistakes.
5. **Black-box systems:** Proprietary systems limit explanation of performance differences and prevent precise cost/token analysis.
6. **Selective system inclusion:** Weak or citation-incapable systems are excluded.
7. **Dynamic websites:** Website changes may alter difficulty or solvability; periodic maintenance is promised (Appendix C.4, p. 19).
8. **Sequential logic:** Current sequential aggregation is sufficient for these tasks but is not fully general (footnote 2, p. 5).
9. **Caching/access:** Collapsed webpage content can be inaccessible to automated verification (§4.4, p. 11).
10. **Benchmark misuse/overfitting:** Released rubrics could be exploited as reinforcement-learning reward models, motivating a private test set and hidden generation pipeline (Appendix B, p. 17).

## Additional evidence-based analyst observations

These are **[D] analyst observations**, not author admissions:

- Human and agent headline results are not calculated on identical task sets, limiting direct ratio interpretation.
- Only one human evaluator performs the initial judge-agent agreement study.
- Excluding trivial total failures increases informativeness but may change the distribution of evaluation difficulty.
- The 99.03% result depends on an adjudication choice that excludes the conflicting-source case while counting inaccessible collapsed content as Verifier error.
- Error analysis samples only one run per system per task and covers five of the ten systems.
- Figure 4 offers descriptive subgroup evidence without uncertainty bars or statistical tests.
- Equal averaging of sibling non-critical nodes can make results sensitive to rubric granularity: splitting one concept into several children may implicitly give it more influence.
- Product performance is time-specific because systems were observed only during April–June 2025.
- Stronger prompts for Operator and Gemini improve instruction alignment but mean prompts were not literally identical across all systems.
- Self-reported and manually measured completion times may have different measurement error.

# 17. Threats to Validity

## Internal validity

Performance differences may reflect more than system capability: interfaces, timing methods, prompt variants, product updates, tool outages, and manual answer collection can influence results. Three runs reduce but do not eliminate run-to-run variability.

## Construct validity

Partial Completion operationalizes usefulness through authored rubrics. Critical/non-critical choices and tree granularity encode human judgments about what counts as useful progress. Attribution verifies whether a page supports a claim, not whether that page is globally truthful or authoritative.

## External validity

Tasks are diverse but deliberately exclude subjective, non-English, video-based, login-protected, calculation-heavy, and inseparably multi-page-verification tasks. Results should not automatically generalize to those settings.

## Statistical conclusion validity

The paper supplies standard deviations but no significance tests, confidence intervals, or effect sizes. The human sample contains seven participants and 30 tasks, while system evaluation uses 120 tasks.

## Ecological validity

Tasks originate from authentic needs and live web use, supporting realism. However, strict citation-per-claim requirements and task-verifiability constraints may be more formal than ordinary user behavior.

## Reproducibility

Positive factors include prompts, detailed annotation instructions, an example script, collection dates, and promised code. Constraints include closed-source evaluated systems, hidden private scripts, changing websites, missing model-version details, and unavailable external artifacts in the supplied document.

## Generalizability of judge reliability

The reliability result is encouraging but is based on 15 tasks and one primary evaluator. Judge performance on other task distributions, models, or webpage types is not established by the supplied study.

# 18. Future Work and Open Questions

## A. Future work proposed by the authors

- Explore more general sequential rubric logic (footnote 2, p. 5).
- Maintain the benchmark through periodic review and replacement of tasks affected by website changes (Appendix C.4, p. 19).
- Maintain a leaderboard with timestamped future results (pp. 6–7; Appendix E.1, p. 23).
- Use the benchmark as a foundation for developing more capable agentic-search systems.
- Improve browsing integration, long-term reasoning, planning, memory, and reliable source attribution, as motivated by the empirical analysis.

## B. Additional open questions

- How stable are system rankings across later product versions?
- Would the 99.03% judge accuracy replicate with multiple independent evaluators and a larger task sample?
- How should conflicting credible sources be scored?
- Can credibility, misinformation, and source quality be evaluated in addition to literal source support?
- How sensitive are scores to alternative but reasonable rubric decompositions?
- Can rubric weights be calibrated to actual user utility?
- How should claims requiring synthesis across multiple webpages be verified?
- Would controlled experiments isolate the effect of browsing, parallel retrieval, inference time, and coding tools?
- How much do private scripts reduce contamination, and how can that be audited?
- What is the compute or monetary cost per successful task?
- Can open-source systems close the reliability gap through post-training rather than prompting alone?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| Agentic search | AI-driven searching that plans, retrieves, browses, and synthesizes rather than merely returning links |
| Large language model (LLM) | A model that processes and generates language and may control tools |
| Deep Research system | A search agent designed for sustained retrieval and comprehensive synthesis |
| Search API | A programmatic interface that returns search results without visually operating a browser |
| Web agent | An agent that clicks, scrolls, and interacts with webpages |
| Search horizon | The amount or sequence length of work required to complete a task |
| Time-varying task | A task whose valid answer can change with time |
| Attribution | A link between a claim and the source meant to support it |
| Provenance | The origin/evidence trail for information |
| LLM-as-a-Judge | Using an LLM to rate an answer |
| Agent-as-a-Judge | A multi-step, tool-using evaluator built around an LLM and explicit rubric |
| Rubric tree | A hierarchy that decomposes evaluation into smaller checks |
| Leaf node | A lowest-level criterion scored directly |
| Internal node | A criterion whose score is computed from child nodes |
| Critical node | A mandatory condition whose failure blocks its parent |
| Non-critical node | A component that may contribute partial credit |
| Sequential node | A node whose children have prerequisite order |
| Short-circuit | Skipping later checks after a gating failure |
| Extractor | Module that converts answer content into structured fields |
| Verifier | Module that decides whether a claim/check passes |
| Partial Completion | Average fractional root score |
| Success Rate | Fraction of tasks receiving a perfect root score |
| Pass@3 | Fraction of tasks solved at least once in three attempts |
| Subset-30 | Random 30-task subset used for human performance and error analysis |
| Invalid Attribution | A broken, malformed, expired, or fabricated source URL |
| Missing Attribution | A claim lacking a source |
| Retrieval Error | A cited page is irrelevant to the claim |
| Synthesis Error | A relevant page is cited, but its contents are misread or misrepresented |
| \(v\) | A rubric node |
| \(C(v)\) | All children of node \(v\) |
| \(K(v)\) | Critical children of \(v\) |
| \(N(v)\) | Non-critical children of \(v\) |
| \(s(v)\) | Score of node \(v\), from 0 to 1 |
| Playwright | The paper’s webpage-loading mechanism; no external definition is needed to understand its role |
| GUI | Graphical user interface |
| PDF | Portable Document Format |
| URL | Web address |
| API | Application programming interface |
| JSON | Structured data format used for rubric annotations |
| HF | Hugging Face |
| LLaVA | Model name used in the Appendix G example; the acronym is not expanded in the supplied paper |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Benchmark size | 130 | tasks | Entire benchmark | Author-reported | p. 1; §3.5, p. 6 |
| Public development set | 10 | tasks | Descriptions and scripts | Author-reported | pp. 6–7 |
| Private test set | 120 | tasks | Descriptions only | Author-reported | p. 7 |
| Construction labor | ≥1,000 | hours | Tasks and judge agents | Author-reported | pp. 1–2, 6 |
| Explicitly time-varying tasks | 57 | tasks | Subgroup analysis | Author-reported | p. 9 |
| Broad domains | 6 | domains | Benchmark composition | Author-reported | Fig. C.1, p. 17 |
| Subdomains | 24 | subdomains | Benchmark composition | Author-reported | Fig. C.1, p. 17 |
| Average leaf nodes | 34 | nodes/task | All rubrics | Author-reported | Table 2(a), p. 6 |
| Maximum leaf nodes | 357 | nodes | Most complex rubric | Author-reported | Table 2(a), p. 6 |
| Average total nodes | 50 | nodes/task | All rubrics | Author-reported | Table 2(a), p. 6 |
| Maximum total nodes | 603 | nodes | Most complex rubric | Author-reported | Table 2(a), p. 6 |
| Maximum rubric depth | 6 | levels | All rubrics | Author-reported | Table 2(a), p. 6 |
| Human-study tasks | 30 | tasks | Subset-30 | Author-reported | §3.5, p. 6 |
| Human participants | 7 | people | Performance study | Author-reported | §3.5, p. 6 |
| Completers per task | 3 | people/task | Human study | Author-reported | Appendix E.3, p. 25 |
| Average human time | 18 / 18.40±1.61 | min | Table 2 rounded / Table 3 | Author-reported | Tables 2(b), 3 |
| Average websites | 8 | websites/task | Human study | Author-reported | Table 2(b), p. 6 |
| Average webpages | 110 | pages/task | Human study | Author-reported | Table 2(b), p. 6 |
| Maximum webpages | 375 | pages/task | Human study | Author-reported | Table 2(b), p. 6 |
| Agent systems evaluated | 10 | systems | Main experiment | Author-reported | §4.1, p. 7 |
| Runs per system/task | 3 | runs | Main experiment | Author-reported | §4.1, p. 7 |
| Best agent Partial Completion | 0.54±0.04 | score | OpenAI Deep Research | Author-reported | Table 3, p. 7 |
| Best agent Success Rate | 0.28±0.04 | proportion | OpenAI Deep Research | Author-reported | Table 3, p. 7 |
| Best agent Pass@3 | 0.40 | proportion | OpenAI DR and Grok DeeperSearch | Author-reported | Table 3, p. 7 |
| Human Partial Completion | 0.79±0.01 | score | Subset-30 | Author-reported | Table 3, p. 7 |
| Human Success Rate | 0.54±0.07 | proportion | Subset-30 | Author-reported | Table 3, p. 7 |
| Human Pass@3 | 0.83 | proportion | Subset-30 | Author-reported | Table 3, p. 7 |
| OpenAI DR time | 8.40±0.71 | min | Main evaluation | Author-reported | Table 3, p. 7 |
| Human time | 18.40±1.61 | min | Subset-30 | Author-reported | Table 3, p. 7 |
| Agent/human partial ratio | 68.4% | ratio | 0.54 ÷ 0.79 | Analyst-derived | Table 3 |
| Agent/human success ratio | 51.9% | ratio | 0.28 ÷ 0.54 | Analyst-derived | Table 3 |
| Agent/human time ratio | 45.7% | ratio | 8.40 ÷ 18.40 | Analyst-derived | Table 3 |
| Human–agent success gap | 26 | percentage points | 54% − 28% | Analyst-derived | Table 3 |
| Judge-study tasks | 15 | tasks | Reliability study | Author-reported | §4.4, p. 10 |
| Node verifications | 720 | judgments | Reliability study | Author-reported | p. 11 |
| Initial discrepancies | 35 | judgments | Human versus judge | Author-reported | p. 11 |
| Human evaluator errors | 27 | discrepancies | Adjudicated | Author-reported | p. 11 |
| Counted Verifier errors | 7 | nodes | Authors’ exclusion rule | Author-reported | p. 11 |
| Judge correctness | 99.03% | percent | 713/720 | Author-reported | p. 11 |
| OpenAI DR hallucination rate | 23% | tasks | Invalid attribution or unsupported answer | Author-reported | Appendix F.2, p. 31 |
| Other systems’ hallucination rate | ≥50% | tasks | Same definition | Author-reported | Appendix F.2, p. 31 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Existing benchmarks do not cover the same long-horizon/time-varying/evaluation combination | Comparative benchmark matrix | Table 1 | §2 and p. 6 | Author comparison; not externally verified here |
| Tasks are long-horizon and laborious | 18-minute average, 110 webpages, maxima of 31 websites/375 pages | X1; Table 2(b) | §3.5, p. 6 | Strong descriptive evidence on Subset-30; likely underestimated |
| Rubrics are complex | Mean 50 and maximum 603 total nodes | Table 2(a) | §3.5, p. 6 | Strong direct descriptive evidence |
| Deep Research systems generally outperform shallow search products | Search products 0.26–0.28; several DR systems 0.40–0.54 | X2/X3; Table 3 | pp. 7–8 | Strong descriptive evidence; no significance tests |
| Operator underperforms leading Deep Research systems | Operator 0.26 versus 0.40–0.54 for stronger DR systems | Table 3 | pp. 7–8 | Strong for observed products; causal explanation is interpretive |
| Longer answers do not necessarily perform better | Gemini: 3,357 words/0.45; OpenAI DR: 559/0.54 | X4; Table 3 | pp. 7–8 | Strong counterexample to simple length-performance equivalence |
| More attempts improve task-level success | Pass@3 exceeds Success Rate for every row | X5; Table 3 | pp. 7–8 | Strong descriptive evidence |
| More inference time can help | Higher performance in selected within-family comparisons | Figure 3; X5 | p. 8 | Moderate observational evidence; confounded |
| Limited-browsing systems struggle on time-varying tasks | Time-varying curve lower for most systems | Figure 4; X6 | pp. 8–9 | Supports hypothesis descriptively; exact values/tests absent |
| Live browsing helps on current/dynamic tasks | Operator and humans are near-par or better on time-varying tasks | Figure 4 | p. 9 | Moderate; browsing is not experimentally isolated |
| Agents frequently fail attribution/synthesis | Seven-category error analysis and cases | Figure 5; F.2–F.15 | pp. 9–10, 26–37 | Strong qualitative/descriptive evidence on selected systems |
| Hallucination remains widespread | 23% for best system; at least 50% for others under defined measure | X8 | p. 31 | Strong under paper’s narrow definition; likely underestimate |
| Humans remain stronger overall | 0.79/0.54 versus best agent 0.54/0.28 | Table 3 | p. 7 | Strong descriptive difference, but subsets differ |
| Best agent uses less than half human time | 8.40 versus 18.40 minutes | Table 3 | p. 7 | Numerically supported; timing methods and task sets differ |
| Judge agents are highly reliable | 7 counted errors among 720 nodes | X9 | pp. 10–11 | Strong within study; one evaluator and adjudication choices limit generalization |
| Tree decomposition enables reliable evaluation | 99.03% result plus observed rubric agreement | Figure 2; X9 | pp. 5, 10–11 | Plausibly supported, but no ablation against a non-tree judge |
| Agents can augment human cognition | Some agents avoid human detail/carelessness errors | Figure 5; F.9–F.10 | pp. 9–10, 31–32 | Promising interpretation, not a direct human–AI collaboration experiment |

# 22. Very Simple Explanation

Imagine asking an AI: “Find five pieces of white furniture from IKEA, keep the total between $200 and $600, check every price, and show me the source for each item.” The answer could fail in many ways. It might find only four items, choose a black desk, exceed the budget, copy a price incorrectly, or invent a link. A single overall rating would hide which parts worked.

Mind2Web 2 tests AI systems with 130 complicated tasks like this. For each task, the researchers build a checklist shaped like a tree. Tiny checks sit at the bottom. Some are mandatory; others allow partial credit. A judging agent reads the answer, checks cited webpages, scores the small pieces, and combines them into one task score.

The strongest AI system did much better than ordinary search assistants, but it still completed only 28% of tasks perfectly on a single run. Humans completed 54%, though they took more time and also made careless mistakes. Trying an AI three times helped, showing that current agents can sometimes solve a task but are inconsistent.

The big lesson is that AI research assistants are useful but not yet dependable enough to trust automatically. They need better persistence, browsing, source tracking, and careful checking. The paper’s other major lesson is that evaluating such systems also requires engineering: the evaluator itself must inspect many small requirements and verify the cited evidence.

# Completeness Audit

## Inventory-based coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/affiliations | Yes | Yes | Represented in compressed form | Full author list not repeated to avoid duplicating the title page; OSU and Amazon AGI are identified in Stage 0 context |
| Abstract | Yes | Yes | Fully represented | Orientation and results sections |
| §1 Introduction | Yes | Yes | Fully represented | §§1, 3–5 |
| §2 Related Work | Yes | Yes | Represented in compressed form | Main categories and claimed gaps retained |
| §3.1 Overview | Yes | Yes | Fully represented | Explicit construction questions retained |
| §3.2 Task Collection | Yes | Yes | Fully represented | Methodology |
| §3.3 Rubric Tree | Yes | Yes | Fully represented | Methodology, Figure 2, equation |
| §3.4 Rubric-based Judge Agent | Yes | Yes | Fully represented | Extractor/Verifier workflow |
| §3.5 Benchmark Statistics | Yes | Yes | Fully represented | Tables 1–2 and numerical ledger |
| §4.1 Experimental Setup | Yes | Yes | Fully represented | Systems, runs, metrics, private test |
| §4.2 Main Results | Yes | Yes | Fully represented | X2–X6 and results |
| §4.3 Error Analysis | Yes | Yes | Fully represented | Taxonomy, Figure 5, cases |
| §4.4 Human Evaluation | Yes | Yes | Fully represented | Sample, phases, discrepancy accounting |
| §5 Conclusions | Yes | Yes | Fully represented | Orientation and discussion |
| Acknowledgments | Yes | Minimally | Deliberately compressed | Non-methodological credits/funding; funding source noted here: Amazon gift, ARL and NSF awards |
| References 1–47 | Yes | No individual annotations | Deliberately compressed | Bibliography is substantive for provenance but not individually summarized; related-work categories are represented |
| Appendix A Limitations | Yes | Yes | Fully represented | Section 16 |
| Appendix B Broader Impacts | Yes | Yes | Represented in compressed form | Misinformation, bias, misuse, overfitting, and private-test mitigation retained |
| Appendix C.1 Domain Distribution | Yes, text only | Yes | Represented in compressed form | Counts and hierarchy covered; visual layout inaccessible |
| Appendix C.2 Design Principles | Yes | Yes | Fully represented | Scope and methodology |
| Appendix C.3 Collection Pipeline | Yes | Yes | Fully represented | Proposal/refinement/validation |
| Appendix C.4 Maintenance | Yes | Yes | Fully represented | Limitations and future work |
| Appendix D.1 Rubric Design | Yes | Yes | Fully represented | Utility-based partial scoring and critical attribution |
| Appendix D.2 Judge Details/prompts | Yes | Yes | Represented in compressed form | Prompt rules summarized rather than reproduced verbatim |
| Appendix D.3 Script Generation | Yes | Yes | Fully represented | Model, inputs, debugging, reflection |
| Appendix D.4 Two-stage Validation | Yes | Yes | Fully represented | Methods and Figure D.1 |
| Appendix D.5 Human Judge Evaluation | Yes | Yes | Fully represented | X9 |
| Appendix E.1 System Settings | Yes | Yes | Fully represented | Dates, UI use, HF base model, prompt variants |
| Appendix E.2 Webpage Pre-caching | Yes | Yes | Fully represented | Playwright, PDF handling, manual intervention |
| Appendix E.3 Human Performance | Yes | Yes | Fully represented | Participants, stopping rules, logging |
| Appendix F.1 Error Analysis | Yes | Yes | Fully represented | Workflow and seven categories |
| Appendix F.2 Case Studies | Yes | Yes | Fully represented | F.2–F.15 addressed individually |
| Appendix G Example Script | Yes | Yes | Represented in compressed form | Architecture and major logic summarized; all 360 code lines not reproduced |
| Appendix H.1 Task Instructions | Yes | Yes | Represented in compressed form | Essential inclusion/exclusion and validation rules preserved |
| Appendix H.2 Human Study Instructions | Yes | Yes | Represented in compressed form | Browser, citations, recording, timing, no-AI rule retained |
| Appendix H.3 Error Instructions | Yes | Yes | Represented in compressed form | Read/Evaluate/Comment/Collect and category meanings retained |
| Appendix H.4 Judge Instructions | Yes | Yes | Represented in compressed form | Two phases, scales, JSON leaf scoring retained |
| Explicit RQs | Yes | Yes | Fully represented | Two §3.1 questions |
| Explicit hypothesis | Yes | Yes | Fully represented | Limited browsing versus time-varying performance |
| Main experiments X1–X9 | Yes | Yes | Fully represented | Separately registered |
| Figure 1 | Visually | Yes | Fully represented | Direct inspection |
| Figure 2 | Visually | Yes | Fully represented | Direct inspection |
| Figure 3 | Visually | Yes | Fully represented | Exact data linked to Table 3 |
| Figure 4 | Visually | Yes | Fully represented | Exact subgroup values unavailable |
| Figure 5 | Visually | Yes | Fully represented with uncertainty | Exact bars unreadable |
| Figure C.1 | Text/caption only | Yes | Represented in compressed form | Rendered page not supplied |
| Figure D.1 | Visually | Yes | Fully represented | Small UI text partly unreadable |
| Figures F.1–F.15 | Visually | Yes | Fully represented | Each individually covered |
| Table 1 | Yes | Yes | Fully represented | Direct text/render inspection |
| Table 2(a) | Yes | Yes | Fully represented | Exact values preserved |
| Table 2(b) | Yes | Yes | Fully represented | Exact values preserved |
| Table 3 | Yes | Yes | Fully represented | All rows and columns preserved |
| Major equation | Yes | Yes | Fully represented | Symbols, cases, purpose, caveats |
| Formal algorithms | N/A | Yes | No formal algorithm present | Appendix G is code, not numbered pseudocode |
| Appendix G code artifact | Yes | Yes | Represented in compressed form | Key data models, verification order, criticality, extraction, and aggregation described |
| Author-stated limitations | Yes | Yes | Fully represented | Section 16 |
| Supplementary material | No separate artifact | Yes | Missing from supplied material | No supplementary file supplied |

## Missing or inaccessible material

- No separate supplementary material was supplied.
- The project website, complete repository, leaderboard, private test scripts, rubric-generation pipeline, cached webpages, human-study videos, CSV logs, and annotation files were not supplied and could not be assessed.
- Figure C.1 was not visually rendered; only its extracted textual contents and caption were available.
- Pages not among the 23 rendered visual candidates were not visually inspected, although their native text was available.
- The exact versions/configurations of several evolving black-box systems, hardware, token counts, inference costs, and stochastic decoding parameters are not specified in the paper.

## Uncertain interpretations

- Exact per-system values in Figure 4 are not labeled; only the qualitative pattern is confidently recoverable.
- Exact bar percentages in Figure 5 cannot be confidently read from the supplied rendering.
- Fine-grained interface text in Figure D.1 is partly too small to inspect, although its major components are visible.
- The formal behavior of sequential score aggregation is described in prose and demonstrated in code, but no general standalone mathematical definition is supplied.
- Figure C.1’s visual encoding cannot be verified without its rendered page.
- The phrase “99.03% correctness” depends on the authors’ classification of discrepancy causes; it should not be read as an unconditional error-free guarantee.
- “50–70% of human performance” compares agent results on the private test set with human results on Subset-30.

## Deliberately compressed material

- The 47 bibliographic entries were inspected but not individually summarized.
- Acknowledgments, funding language, and author names were compressed because they do not alter the method or evidence.
- Long prompt templates in Appendix D and annotation instructions in Appendix H were summarized by operational rule rather than reproduced.
- Appendix G’s 360-line script was reduced to its architecture, ground truth, data models, sequential/parallel structure, critical checks, extraction calls, and output.
- Repetitive case-study text was compressed while every substantive case figure remained individually represented.

## Potential omissions

No known major section, substantive subsection, explicit research question, explicit hypothesis, experiment, substantive figure, table, major equation, contribution, author-stated limitation, or appendix item from the supplied inventory is absent from this analysis. The known exclusions are the deliberately compressed bibliography/code/instruction wording and the external or supplementary artifacts that were not supplied.