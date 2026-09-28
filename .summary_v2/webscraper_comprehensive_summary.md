# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible page range | Pages 1–7 |
| Pages apparently missing | None |
| Native/extracted text | Available for all seven pages; page 7 contains only the final reference |
| Pages visually inspected | Pages 1–5 |
| Pages not visually rendered | Pages 6–7; they contain the continuation of Ethical Considerations and References, with no substantive figures, tables, equations, or algorithms detected |
| Figures available visually | Yes: Figures 1–4 |
| Tables readable | Yes: Tables 1–2 are readable in both extracted text and rendered pages |
| Equations | No displayed mathematical equations were found |
| Algorithms/pseudocode | None presented |
| Appendices | None |
| Supplied supplementary material | None |
| Referenced but absent artifacts | The paper points to a GitHub repository containing source code and prompts (footnote 1, p. 3), but that repository was not supplied and was not inspected |
| OCR required | No; native text was available |
| OCR-sensitive material | None significant. Figure 2’s small tick labels and Figure 3’s unlabeled bar heights require cautious visual estimation |
| Other limitations | The publication venue is not stated. The manuscript is identified only as arXiv:2603.29161v1, dated 31 March 2026 (p. 1). Exact numerical news-site results are not tabulated and must mostly be estimated from Figure 3. The six sites are abbreviated in the plot, while Table 1 anonymizes three of them as “Website 3–5.” |

Evidence categories used below:

- **[A] Author-reported:** explicitly stated in the paper.
- **[B] Directly observable:** clearly visible in a supplied page, figure, or table.
- **[C] Analyst-derived:** calculated from supplied values, with operands shown.
- **[D] Analyst interpretation:** a source-grounded inference not explicitly claimed by the authors.
- No external information is introduced.

# 1. Plain-Language Orientation

This paper introduces **Webscraper**, an experimental framework for extracting structured information from modern websites whose content cannot reliably be obtained by simply downloading and parsing static Hypertext Markup Language (HTML). Such sites may reveal content only after scrolling, clicking pagination controls, or executing JavaScript.

The authors’ core idea is to combine two modes of work:

1. A **multimodal large language model (MLLM)** operates the graphical interface—viewing screenshots, clicking, scrolling, and using keyboard shortcuts.
2. Specialized tools perform the repetitive data work—turning raw HTML into structured records and merging results across pages.

The target is the common **index-and-content architecture**: an index page lists many items, and each item links to a detail page. News-category pages and product-search pages are examples (pp. 2–3, §3.1).

The framework starts from Anthropic’s Computer Use agent and adds:

- a structured five-stage guiding prompt;
- a **Parse Tool**, which delegates HTML-to-structured-data code generation to another reasoning model; and
- a **Merge Tool**, which consolidates and deduplicates records.

The evaluation compares three configurations over 30 runs per experimental setting: an unmodified baseline agent, the baseline plus the guiding prompt, and the prompt plus working custom tools (p. 3, §4.1; p. 4, §4.3). On all six news sites, the full framework has the highest plotted correctness. On the two e-commerce sites, its scores are 0.242 on Momo and 0.422 on Amazon, versus 0.000 and 0.027 for the baseline (pp. 4–5, §4.5, Table 2).

The central contribution is therefore not merely “an AI that browses.” It is a hybrid workflow that lets an agent navigate visually while delegating large-scale, repetitive extraction to reusable programmatic operations. The evidence supports an improvement over the tested Computer Use baseline, but not universal or production-grade scraping: performance remains modest on the two e-commerce tasks, the benchmark is small, and several implementation and statistical details are absent.

# 2. Document Roadmap

The accessible seven-page paper is organized as follows:

| Identifier | Original location | Content and role |
|---|---|---|
| S1 | Abstract, p. 1 | States the problem, proposed framework, principal evaluation, and three broad contributions |
| S2 | §1 Introduction, p. 1 | Motivates dynamic web scraping and proposes combining visual navigation with parsing tools |
| S3 | §2 Related Work, pp. 1–2 | Divides prior work into web navigation and Web Information Extraction (WIE), then identifies the integration gap |
| S4 | §3 Methodology, pp. 2–3 | Defines index-and-content scraping and describes the system architecture |
| SS4.1 | §3.1, p. 2 | Defines index pages, content pages, task prompts, and JSON output |
| SS4.2 | §3.2, pp. 2–3 | Describes the foundational agent, native tools, Parse Tool, Merge Tool, and guiding prompt |
| S5 | §4 Experiments, pp. 3–5 | Defines configurations, benchmark, metrics, stability analyses, news results, and e-commerce transfer |
| SS5.1 | §4.1, p. 3 | Three experimental configurations and shared execution settings |
| SS5.2 | §4.2, p. 3 | Six-site benchmark, manually generated “Golden” references, ROUGE-L, and binary Correctness |
| SS5.3 | §4.3, pp. 3–4 | Run-count convergence and seven-day temporal stability |
| SS5.4 | §4.4, p. 4 | Main six-news-site comparison |
| SS5.5 | §4.5, pp. 4–5 | E-commerce generalization on Momo and Amazon |
| S6 | §5 Discussion and Conclusion, p. 5 | Interprets the hybrid strategy, states limitations, and proposes future work |
| S7 | Ethical Considerations, pp. 5–6 | Describes access, server-load, and data-use constraints |
| S8 | §6 References, pp. 6–7 | Seventeen cited works/resources |

The paper contains four figures, two tables, no displayed equations, no formal algorithms, no appendices, and no supplied supplementary files.

# 3. Background and Context

## Essential terminology

A **web scraper** automatically collects information from websites. A traditional scraper commonly downloads HTML and applies hand-written selectors or rules to locate fields.

A **dynamic website** loads or changes content through client-side behavior such as JavaScript, scrolling, or clicking. The desired data may therefore not exist in the initially returned HTML (p. 1, §1).

A **large language model (LLM)** is the class of model used here for reasoning and code generation. A **multimodal large language model (MLLM)** additionally processes visual inputs such as webpage screenshots. In this paper, that visual capability supports interaction with webpages as graphical interfaces (p. 1).

A **graphical user interface (GUI) agent** observes the screen and issues mouse or keyboard actions. Anthropic’s **Computer Use** supplies the foundational agent in this work (pp. 1–3).

**Web Information Extraction (WIE)** means converting information in webpage documents into useful structured fields. The authors distinguish it from **web navigation**, which first exposes or reaches the relevant content (pp. 1–2, §2).

An **index page** lists many entries, usually with links. A **content page** is the linked detail page for one entry. The desired output is one JavaScript Object Notation (**JSON**) file containing an array of structured records (p. 2, §3.1).

An **XPath expression** identifies elements in an HTML/XML document. The related-work discussion says XPath-generation systems efficiently locate individual data points but are not inherently designed to retrieve all related records in a large page-level collection (p. 2, §2).

**Visual grounding** is the agent’s ability to connect a visual target with the correct screen location and action. The authors report inaccurate clicks after zooming as one failure mode (p. 5, §5).

The **Document Object Model (DOM)** is mentioned as the webpage representation whose content may mutate or, under advanced virtual scrolling, be removed as the user moves through a page (p. 5, §5). The paper does not formally define DOM.

A **WebSocket** is named as a protocol associated with real-time network communication. The paper does not formally define it; it says such streaming architectures lie outside the present framework’s natural scope (p. 5).

## Evaluation concepts

The authors construct a manually generated **Golden set** containing the expected URL, title, and article content for each news site (p. 3, §4.2).

**ROUGE-L** is used to compare extracted text with the reference. The paper explains that it penalizes over-extraction through reduced precision and under-extraction through reduced recall while tolerating some structural noise (p. 3). It does not provide the formula or specify which ROUGE-L variant or aggregation is used.

An article is counted as **Correct** only when:

- the URL matches exactly;
- title ROUGE-L is at least 0.8; and
- content ROUGE-L is at least 0.8.

The reported “accuracy” or “Average Correct” is consequently a binary-success rate aggregated over evaluated articles/runs, although the precise aggregation procedure is not specified.

A **95% confidence-interval (CI) half-width** measures half the width of a reported 95% interval. The authors use its convergence as a practical criterion for selecting 30 runs (pp. 3–4, §4.3), but do not state the CI estimator or sampling assumptions.

# 4. Research Problem and Gap

## Existing problem

Modern sites frequently require interaction before their content becomes available. Static HTML parsers can fail on infinite scrolling, button-controlled pagination, or dynamically loaded content. Hand-crafted crawlers are also fragile when layouts change and may require substantial maintenance (p. 1, §1).

## Shortcomings attributed to prior approaches

The authors identify two partially separate research traditions (pp. 1–2, §2):

- Visual web agents such as SeeAct and WebVoyager can navigate browser interfaces, but reportedly lose capability in more complex desktop environments.
- Rule-based WIE wrappers are brittle.
- Modern LLM-based extraction can be accurate but computationally expensive.
- Systems that ask an LLM to generate reusable XPath rules reduce recurring cost, but focus on individual fields rather than holistic extraction of many connected records.
- General-purpose browsing agents process pages sequentially, which the authors argue inflates context and becomes inefficient on index pages containing many links (p. 5, §5).

These are the paper authors’ characterizations of cited work; the supplied paper does not independently reproduce those earlier studies.

## Research gap

[A] The stated gap is the absence of a unified framework combining strong dynamic navigation with large-scale, structured extraction for modern index-and-content websites (p. 2, §2).

## Motivation

Accurate and timely web extraction supports large-scale data use, including LLM pre-training and analysis of current news. News sites are selected as a particularly dynamic and societally relevant test domain (p. 1, §1).

## Scope

The framework is expressly scoped to index-and-content sites. It is tested on six news websites and two e-commerce sites. It is not designed for real-time WebSocket streams or advanced virtual-scrolling architectures that unload content from the DOM (p. 5, §5).

# 5. Research Questions / Objectives / Hypotheses

## Explicit research questions

The paper does not state formally numbered research questions.

## Objectives

The following objectives are explicit or direct restatements of the authors’ contribution list (p. 1, Abstract and §1):

- Demonstrate the feasibility of MLLM-based prompt design for index-and-content scraping.
- Improve extraction accuracy by adding specialized extraction tools.
- Evaluate whether the framework generalizes from news to another domain, specifically e-commerce.
- Build a unified agent capable of both navigating dynamic interfaces and extracting structured records (p. 2, §2).

## Hypotheses

No formal statistical hypotheses or null hypotheses are stated.

The experimental design nevertheless tests three implicit expectations:

- A crawler-specific guiding prompt will improve correctness over zero-shot Computer Use.
- Functional Parse and Merge tools will improve further over prompt guidance alone.
- The same ordering will extend to e-commerce index-and-content tasks.

These are **[D] analyst-formulated experimental expectations**, not author-labeled hypotheses.

# 6. Assumptions / Threat Model

This is a systems/AI paper rather than a security study, so it supplies no formal attacker or threat model.

## System assumptions

[A] The method assumes:

- The target follows an index-and-content structure.
- A user can express the target site, crawl scope, and desired fields in one natural-language prompt (p. 2, §3.1).
- The agent can access screenshots, GUI controls, command-line utilities, file-editing capabilities, and webpage HTML (pp. 2–3, §3.2).
- Content pages share enough structure for a generated parsing script to be reused.
- The browser environment can be reset; every experimental run starts from a clean Firefox instance (p. 3, §4.1).
- The manually written deterministic crawlers produce valid ground truth (p. 3, §4.2).

## Trusted components

The evaluation effectively trusts:

- the Golden-set crawlers;
- the Computer Use environment;
- the Parse Tool’s reasoning model and code-interpreter execution;
- the Merge Tool’s aggregation and deduplication;
- the scoring implementation.

The paper does not discuss validation of these components beyond performance against the Golden set.

## Ethical access boundaries

The experiments use only publicly accessible information, do not bypass authentication, paywalls, or other access controls, run at low frequency with delays, and collect a minimal volume solely for academic evaluation (pp. 5–6, Ethical Considerations).

## Excluded environments

The paper expressly excludes or anticipates difficulty with:

- real-time WebSocket streaming;
- advanced virtual scrolling that unloads earlier DOM content;
- navigation requiring unusually difficult visual grounding;
- inconsistent HTML structures that defeat generated scripts (p. 5, §5).

# 7. Methodology

## Study design

The work is a mixed **computer-systems and empirical AI-agent study**. It builds a framework, performs a three-condition ablation comparison, evaluates six news sites, conducts run-count and temporal-stability checks, and then tests two e-commerce sites.

## Task definition

A user supplies a single prompt naming:

- the target website;
- the crawl scope, such as the first two pages; and
- desired fields, such as title, link, and content.

The illustrative BBC task appears on p. 2, §3.1. The expected output is a single JSON list whose objects correspond to extracted items.

## System architecture

The foundational Computer Use agent receives both user and system prompts. A central system prompt directs a five-stage extraction process and lets the agent choose among native and custom tools (pp. 1–3; Figure 1).

The paper calls the procedure “five-stage” several times but the supplied main text does not enumerate or define the five stages. This is a substantive implementation omission; the absent GitHub prompts may contain them, but they were not supplied.

### Native tools

- **Computer:** observes the screen and performs mouse, click, scroll, and keyboard actions.
- **Bash:** handles files, scripts, and network requests such as `curl`.
- **Str Editor:** writes, reads, and modifies files, including generated extraction scripts.

### Custom tools

**Parse Tool:** receives raw HTML plus the user’s requirements, sends them to a reasoning model, obtains a tailored Python extraction script, and executes it in a code-interpreter environment to produce structured data (p. 3).

The stated reasons for delegating parsing are:

- to preserve the main agent’s context window;
- to give mission-critical index parsing to a stronger specialized model; and
- to keep the main system prompt focused on high-level strategy.

**Merge Tool:** combines structured lists across iterations, removes duplicates, and consolidates results—especially during pagination.

## Models and execution settings

| Component/configuration | Reported setting |
|---|---|
| Baseline foundational agent | `claude-3-7-sonnet-20250219` |
| Computer Use temperature | 0 |
| Full-system Parse Tool model | OpenAI GPT-o3-mini |
| Browser | Clean Firefox instance for every run |
| Prompt integration | Crawler-specific guidance appended to the default system prompt |
| Runs | 30 per experimental setting after the convergence analysis |

A naming discrepancy appears in the paper: p. 3 first calls the Parse Tool model “GPT-o3,” then §4.1 specifies “GPT-o3-mini.” The supplied material does not explain whether “GPT-o3” is shorthand or a different model.

## Comparison conditions

1. **Baseline Agent:** default Computer Use, with only the user task.
2. **Webscraper (Prompt Only):** baseline plus the guiding system prompt; Parse and Merge tools disabled. Descriptions of their intended operations remain in the prompt.
3. **Webscraper (Prompt + Tool):** guiding prompt plus working Parse and Merge tools.

This design separates the effect of task guidance from the additional effect of executable tools.

## Data and ground truth

The main benchmark contains six mainstream Chinese and English news sites exhibiting infinite scroll, button pagination, and dynamic loading (p. 3, §4.2). The paper does not report:

- the sites’ full names beyond Figure 3 abbreviations;
- the number of articles per site;
- crawl dates;
- requested page counts for each task;
- language distribution;
- site-selection criteria;
- exact Golden-set construction or checking procedure;
- exclusions or missing records.

For every news site, the authors manually create a deterministic crawler whose URLs, titles, and article content become the Golden set.

The transfer evaluation uses Momo and Amazon but likewise omits product counts, crawl dates, categories, fields beyond examples such as price and rating, and precise sampling procedures (pp. 4–5, §4.5).

## Metrics

For news:

\[
\text{Correct(article)} =
\mathbf{1}\{\text{URL exact match}\}
\land
\mathbf{1}\{\text{title ROUGE-L}\ge 0.8\}
\land
\mathbf{1}\{\text{content ROUGE-L}\ge 0.8\}.
\]

This notation is **[C] an analyst restatement**, not a displayed equation from the paper.

For e-commerce, the paper says it uses a stricter Correctness metric requiring a “near-exact match,” but it does not formally define the criterion.

## Unreported implementation details

The supplied paper does not specify hardware, operating-system version, Firefox version, API parameters beyond temperature, token budgets, retry policies, stopping rules, timeout limits, exact prompting stages, Parse/Merge schemas, random seeds, statistical test procedures, or cost/runtime measurements.

# 8. Experiments / Analyses

## X1 — Run-count convergence

**Purpose:** Choose a repetition count that balances interval precision and computational cost (pp. 3–4, §4.3; Figure 2).

**Setup:** The authors examine the 95% CI half-width of the performance metric as the number of runs increases. They say the analysis spans “all nine experimental settings,” though the paper does not define why there are nine settings.

**Result:** The representative plotted curve falls rapidly at small \(n\), then flattens; the selected elbow is \(n=30\). The paper consequently uses 30 runs in all experiments.

**Caveats:**

- Figure 2 shows one representative scenario, not all nine.
- The site/configuration represented is not identified.
- The CI formula, observations being sampled, and aggregation across settings are not reported.
- “All nine experimental settings” does not map transparently onto the later six sites × three configurations; the relationship is unresolved.

## X2 — Seven-day temporal stability

**Purpose:** Test whether observed performance changes materially after a week (p. 4, §4.3; Table 1).

**Setup:** Baseline and full Webscraper are measured at time \(T\) and \(T+7\) days on Websites 3, 4, and 5. Prompt Only is omitted.

**Reported result:** The authors describe the method as consistent and claim “variance of less than 5%” on all sampled sites.

**Exact values:**

| Website | Baseline T | Baseline T+7 | Full T | Full T+7 |
|---|---:|---:|---:|---:|
| Website 3 | 0.103 | 0.061 | 0.511 | 0.533 |
| Website 4 | 0.277 | 0.317 | 0.648 | 0.673 |
| Website 5 | 0.145 | 0.179 | 0.820 | 0.820 |

**[C] Derived full-system absolute changes:**

- Website 3: \(0.533-0.511=+0.022\), or +2.2 percentage points.
- Website 4: \(0.673-0.648=+0.025\), or +2.5 percentage points.
- Website 5: \(0.820-0.820=0\).

Thus, the full system changes by no more than 0.025 in absolute accuracy.

**Terminology caveat:** “Variance” normally names a particular statistical quantity, but no variance is reported. If “less than 5%” means absolute percentage-point change, the full method satisfies it. If it means relative change, Website 3 changes by \(0.022/0.511\approx4.31\%\) and Website 4 by \(0.025/0.648\approx3.86\%\), still below 5%. Baseline relative changes are much larger. The claim appears intended specifically for the proposed method.

## X3 — Six-site news benchmark

**Purpose:** Compare zero-shot Computer Use, prompt guidance, and the full tool-equipped framework (p. 4, §4.4; Figure 3).

**Sites:** Appledaily, BBC, CNN, LTN, PTS, and UDN, as visually readable in the x-axis labels of Figure 3.

**Metric:** Average Correct (%), based on exact URL and title/content ROUGE-L thresholds.

**Result:** The full framework is the tallest bar for all six sites. Prompt Only is second on all six, and the baseline is lowest.

Approximate bar heights visually inferred from Figure 3:

| Site | Baseline | Prompt Only | Prompt + Tool |
|---|---:|---:|---:|
| Appledaily | ~5% | ~25% | ~30% |
| BBC | ~4% | ~9% | ~53% |
| CNN | ~14% | ~26% | ~57% |
| LTN | ~32% | ~54% | ~68% |
| PTS | ~20% | ~59% | ~82% |
| UDN | ~14% | ~36% | ~51% |

All values above are **approximate visual estimates**, not labeled results.

The text adds that the baseline succeeded only twice in 30 LTN runs when pagination was involved (p. 4). That count corresponds to \(2/30\approx6.7\%\) **[C]**, but Figure 3’s LTN baseline bar appears near 32%. The two figures need not conflict because the “twice” statement may refer specifically to successful pagination rather than the plotted article-level correctness metric. The paper does not explain the relationship.

## X4 — Prompt ablation

**Purpose:** Isolate whether executable Parse/Merge tools add value beyond written strategic guidance.

**Setup:** Compare Prompt Only with Prompt + Tool under otherwise shared framework settings.

**Result:** The full system outperforms Prompt Only on every news site (Figure 3) and both e-commerce sites (Table 2). This supports an incremental contribution from the functional tools.

No significance test, confidence interval per bar, effect-size analysis, or paired-run analysis is presented.

## X5 — E-commerce generalization

**Purpose:** Test the method outside news while retaining the index-and-content pattern (pp. 4–5, §4.5; Table 2).

| Website | Baseline | Prompt Only | Prompt + Tool |
|---|---:|---:|---:|
| Momo | 0.000 | 0.040 | **0.242** |
| Amazon | 0.027 | 0.138 | **0.422** |

**[C] Derived absolute gains of the full system:**

- Momo vs baseline: \(0.242-0.000=0.242\), or 24.2 percentage points.
- Momo vs Prompt Only: \(0.242-0.040=0.202\), or 20.2 points.
- Amazon vs baseline: \(0.422-0.027=0.395\), or 39.5 points.
- Amazon vs Prompt Only: \(0.422-0.138=0.284\), or 28.4 points.

**[C] Derived relative comparison between full-system site scores:** Amazon’s 0.422 is approximately \(0.422/0.242=1.74\) times Momo’s score, or about 74.4% higher relative to Momo. This does not establish a site-independent effect because the task samples and conditions are underspecified.

The authors attribute Momo’s lower performance to ambiguity among multiple displayed price fields, illustrated in Figure 4. That explanation is plausible within the supplied evidence, but no controlled experiment isolates price-field ambiguity from other site differences.

# 9. Results

| Finding | Evidence and condition | Supported interpretation | Qualification |
|---|---|---|---|
| The full framework leads on all six news sites | Full-system bar is highest in every Figure 3 group (p. 4) | Combining guidance and functional tools improves correctness over the tested baseline | Exact values are not printed; no inferential test is supplied |
| Prompt guidance alone improves over the baseline | Green bar exceeds blue for all six Figure 3 sites | Procedural guidance helps a general-purpose agent perform scraping | Prompt content and five stages are not reproduced |
| Functional tools add further improvement | Red bar exceeds green for every news site and both rows of Table 2 | Executable parsing/merging contributes beyond prompt descriptions | The design bundles Parse and Merge, so their individual effects cannot be separated |
| The baseline struggles with pagination | Authors report only two successes in 30 runs on LTN and often sub-50% performance on multipage sites | General browsing ability does not automatically yield reliable large-scale extraction | “Success” in the two-of-30 statement is not tied precisely to the plotted aggregation |
| Thirty runs were selected | Figure 2 flattens around \(n=30\) | Additional runs beyond 30 provide diminishing CI precision gains | Only a representative curve is shown; computation is undocumented |
| Full-system results remain close after seven days | Changes of +0.022, +0.025, and 0 on Websites 3–5 | Short-term temporal stability on the sampled sites | Only three sites and two time points are tested |
| The ranking transfers to e-commerce | Table 2: full > prompt-only > baseline on Momo and Amazon | The approach has some cross-domain applicability within index-and-content sites | Only two sites; absolute full-system correctness remains 0.242 and 0.422 |
| Momo is harder than Amazon | Full scores 0.242 vs 0.422; Figure 4 shows competing prices | Ambiguous visible fields can increase extraction difficulty | This causal explanation is observational, not experimentally isolated |

The authors repeatedly use “significantly” in the ordinary sense of “substantially.” No statistical significance test or \(p\)-value is reported, so the word should not be read as demonstrated inferential significance.

# 10. Figure-by-Figure Interpretation

## Figure 1 — System architecture

**Location:** p. 2, §3.2.

**Type:** Architecture/data-flow diagram.

**Contents:**

- Left: a user supplies a task prompt, illustrated as scraping two pages of BBC news.
- Center-left: an AI agent labeled Computer Use receives a user prompt and a system prompt.
- Center/right: the agent can invoke native tools—Computer, Bash, and Str Editor—and custom tools—Parse Tool and Merge Tool.
- Far right: the tools produce screenshots, execution results, and related outputs.
- A line labeled “Structural Data” indicates structured output returning toward the user-side flow.

**Visual encoding:** Native tools occupy a gray upper block; custom tools occupy a yellow lower block. Arrows connect the agent to tools and tool results. A “Thinking” bubble represents the agent’s reasoning loop.

**Conclusion supported:** Webscraper is a coordinated agent-tool architecture, not a single extraction model.

**Caveat:** The diagram does not expose the internal five-stage procedure, schemas, error handling, or exact iteration/feedback semantics.

## Figure 2 — Convergence of confidence-interval half-width

**Location:** p. 4, §4.3.

**Type:** Line plot.

**Axes:**

- x-axis: Number of Experimental Runs, \(n\), apparently extending to about 50.
- y-axis: 95% CI Half-Width, \(\epsilon\), apparently from 0 to roughly 0.12.
- Scale: linear on both axes.

**Legend and markers:**

- Blue line: 95% CI half-width.
- Red point: selected \(n=30\).

**Observation:** The curve is initially high and irregular, falls quickly as runs accumulate, and becomes comparatively flat around and after 30.

**Values:** The exact half-width at \(n=30\) is not labeled and cannot be read confidently at the supplied resolution. The selected run count of 30 is author-reported.

**Conclusion supported:** Thirty repetitions are presented as a practical precision/cost compromise.

**Caveats:** It is one representative scenario, its identity is undisclosed, and the calculation is not specified.

## Figure 3 — News-site correctness comparison

**Location:** p. 4, §4.4.

**Type:** Grouped bar chart.

**Axes:**

- x-axis: six site groups—Appledaily, BBC, CNN, LTN, PTS, UDN.
- y-axis: Average Correct (%), from 0 to 100.
- Scale: linear.

**Legend:**

- Blue: Computer Use baseline.
- Green: Webscraper (Prompt Only).
- Red: Webscraper (Prompt + Tool).

**Main observations:**

- Red is highest in all groups.
- Green is higher than blue in all groups.
- The full method’s strongest plotted result is PTS, approximately 82%.
- Its weakest is Appledaily, approximately 30%.
- The largest visually apparent tool increment is on BBC, where Prompt + Tool is around 53% versus Prompt Only around 9%.
- Error bars and significance markers are absent.

**Conclusion supported:** Both structured prompting and functional tools improve average correctness over the tested baseline, with tools adding value beyond prompting.

**Caveat:** Bar heights are unlabeled. Exact numerical reporting is therefore unavailable except as approximate visual estimates.

## Figure 4 — Ambiguous product-price display

**Location:** p. 5, §4.5.

**Type:** Screenshot/example rather than a statistical plot.

**Contents:** A Momo product page shows a shoe listing with several price-related fields. A red rectangle highlights competing price information; the caption says the agent must identify the market price rather than promotional or discounted alternatives.

**Axes/units/legend:** Not applicable.

**Conclusion supported:** A visually realistic example demonstrates that “price” can be semantically ambiguous even when several numeric values are clearly displayed.

**Caveat:** One screenshot illustrates a possible failure mechanism but does not quantify how often ambiguity occurs or prove that it alone caused Momo’s lower aggregate score.

# 11. Table-by-Table Interpretation

## Table 1 — Seven-day temporal stability

**Location:** p. 4, §4.3.

**Purpose:** Compare accuracy at time \(T\) and seven days later.

**Rows:** Websites 3, 4, and 5.

**Columns:** Baseline and Webscraper (Prompt + Tool), each at \(T\) and \(T+7\).

**Units:** Proportions from 0 to 1, described as accuracy.

**Important observations:**

- Full Webscraper exceeds baseline at both times on every row.
- Full Webscraper rises slightly on Websites 3 and 4 and remains unchanged on Website 5.
- The highest entry is 0.820 at both times for the full system on Website 5.
- The lowest is 0.061 for the baseline on Website 3 at \(T+7\).
- Prompt Only is absent.
- No uncertainty estimates or statistical tests are shown.

**Text–table issue:** The prose calls the changes “variance of less than 5%,” but the table contains point estimates, not variances. The intended meaning appears to be change smaller than five percentage points or five percent for the full system.

## Table 2 — E-commerce comparison

**Location:** p. 5, §4.5.

**Purpose:** Compare the three configurations on Momo and Amazon.

**Rows:** Momo and Amazon.

**Columns:** Baseline, Prompt Only, Prompt + Tool.

**Units:** Correctness proportions from 0 to 1.

**Best/worst:**

- Best Momo result: 0.242, full framework.
- Best Amazon result: 0.422, full framework.
- Worst Momo result: 0.000, baseline.
- Worst Amazon result: 0.027, baseline.
- No ties occur.
- Bold formatting identifies the full framework as best in both rows.

**Statistical information:** No error bars, confidence intervals, sample counts, or significance tests.

**Conclusion supported:** The ordering baseline < Prompt Only < Prompt + Tool holds on both e-commerce sites.

# 12. Diagram / Architecture Interpretation

Figure 1’s operational flow can be reconstructed as follows:

1. The user supplies one natural-language scraping objective.
2. The Computer Use agent also receives the authors’ guiding system prompt.
3. The agent observes the browser and reasons about the current state.
4. It uses the Computer tool for visual navigation and interaction.
5. It can use Bash for commands, files, scripts, or network retrieval.
6. It can use Str Editor to create or revise extraction code.
7. When raw HTML must be converted into records, the Parse Tool packages the HTML and requirements for a separate reasoning model.
8. That model creates a tailored Python parser, which is executed to generate structured output.
9. Across pagination or repeated iterations, the Merge Tool combines lists and deduplicates records.
10. The final result is a structured dataset, expected to be one JSON file.

The control path is agent-directed: the MLLM chooses which tools to invoke based on the prompt and current webpage. The data path is hybrid: screen state supports navigation, while HTML supports extraction. The paper implies iteration but does not diagram a formal stopping condition or recovery loop.

The method’s key scaling idea is to avoid manually visiting and interpreting every detail page solely through the multimodal agent. Instead, it generates programmatic extraction logic that can be reused across similarly structured content pages (p. 5, §5).

# 13. Equations and Mathematical Concepts

The paper contains no numbered or displayed equations and no formal mathematical model.

The essential evaluation rule can be represented as the following **[C] analyst-formalized identity**:

\[
C_i =
\begin{cases}
1, & U_i=\widehat U_i,\ R_L(T_i,\widehat T_i)\ge 0.8,\ 
R_L(B_i,\widehat B_i)\ge 0.8,\\
0, & \text{otherwise}.
\end{cases}
\]

Here:

- \(C_i\): correctness indicator for item \(i\);
- \(U_i,\widehat U_i\): reference and extracted URL;
- \(T_i,\widehat T_i\): reference and extracted title;
- \(B_i,\widehat B_i\): reference and extracted article body/content;
- \(R_L\): ROUGE-L similarity.

Plainly: one bad component makes the entire article incorrect. A correct title and body cannot compensate for a wrong URL; likewise, an exact URL cannot compensate for a title or body score below 0.8.

The paper motivates 0.8 through a cited commercial precedent and the authors’ empirical observations: minor noise generally scores above 0.8, while major failures reportedly score below 0.3 (p. 3, §4.2). It does not provide the distributions supporting those observations.

Figure 2 uses a 95% CI half-width, denoted \(\epsilon\) in the plot. No formula is supplied. The conceptual quantity is half the distance between the interval’s lower and upper endpoints.

No objective function, training loss, theorem, lemma, proposition, proof, or optimization procedure appears.

# 14. Interpretation and Discussion

The study’s evidence answers its informal objectives as follows:

- **Feasibility of structured prompting:** Supported within the benchmark because Prompt Only exceeds the zero-shot baseline on all six plotted news sites and both e-commerce rows.
- **Value of specialized tools:** Supported because Prompt + Tool exceeds Prompt Only in every reported site comparison.
- **Cross-domain application:** Partially supported because the same ranking occurs on Momo and Amazon. The evidence establishes transfer to two e-commerce tasks, not generality across arbitrary domains.
- **Handling dynamic interaction:** Supported qualitatively by the pagination discussion and the range of site interaction patterns, though site-level task definitions and per-feature analyses are absent.

The results suggest that navigation and extraction are different computational problems. Visual interaction is useful for reaching or exposing content, whereas programmatic parsing is better suited to processing many similarly structured records. This division is consistent with the architecture and the full-versus-prompt-only results.

The paper further argues that a sequential page-by-page agent consumes excessive context on indexes containing many links. Its alternative is to invest model effort in creating a reusable parser. However, the study reports neither context-token consumption, latency, monetary cost, nor throughput. Thus, the claimed efficiency advantage is architecturally motivated but not quantitatively evaluated.

## Consistency and unresolved points

- “GPT-o3” in the methodology and “GPT-o3-mini” in the experiment settings may refer to the same component, but the naming is inconsistent.
- The “five-stage” prompt is central yet never enumerated in the supplied text.
- “All nine experimental settings” in the convergence analysis is unexplained relative to the six-site, three-configuration benchmark.
- “Variance of less than 5%” is not accompanied by a variance statistic.
- “Significantly outperformed” is not supported by reported statistical hypothesis tests.
- The Correctness definition is precise for news but only described as a stricter “near-exact match” for e-commerce.
- Figure 3 uses recognizable site names, while Table 1 uses anonymous Website 3–5 identifiers; the mapping is not supplied.
- The conclusion emphasizes scalability and efficiency without direct measurements of either.

# 15. Contributions and Novelty

## Conceptual contribution

The paper frames large-scale dynamic scraping as a combination of **navigation** and **structured extraction**, rather than as a GUI-only browsing task.

## Methodological contribution

It proposes a structured five-stage prompt for index-and-content scraping. The stages themselves are not reproduced, limiting independent assessment of this contribution.

## System contribution

Webscraper integrates:

- Anthropic Computer Use;
- native GUI, shell, and file-editing tools;
- a reasoning-model-backed Parse Tool; and
- a Merge Tool for aggregation and deduplication.

## Tool-design contribution

Parsing is deliberately outsourced from the main agent to preserve context, use a more capable parser-generating model, and simplify high-level orchestration.

## Experimental contribution

The paper compares baseline, prompt-only, and prompt-plus-tool configurations on six news sites, adds two stability checks, and tests two e-commerce sites.

## Empirical contribution

Across all reported site comparisons, the ordering is consistently:

\[
\text{Prompt + Tool} > \text{Prompt Only} > \text{Baseline}.
\]

This statement is directly supported by Figure 3 and Table 2, but its statistical reliability cannot be assessed fully because per-site uncertainty and hypothesis tests are absent.

## Availability contribution

Footnote 1 reports that source code and prompts are placed in a GitHub repository. The repository was not supplied or inspected, so availability and reproducibility were not verified.

No new dataset, formal algorithm, theorem, or benchmark standard is introduced.

# 16. Limitations

## Authors’ stated limitations

The authors explicitly acknowledge (p. 5, §5):

- **Complex navigation failures:** Visual grounding may fail, including inaccurate clicks after zooming.
- **Generated-code failures:** Both the proposed method and baseline can create buggy parsers for inconsistent HTML.
- **Architectural scope:** The framework is limited to index-and-content sites.
- **Real-time streaming:** It would struggle with WebSocket-based architectures.
- **Advanced virtual scrolling:** It may fail when earlier content is unloaded from the DOM.
- **Momo ambiguity:** Multiple simultaneous price fields complicate target-field selection (pp. 4–5, §4.5).
- **Cost and stochasticity:** Continued LLM intervention carries recurring cost and variability; this motivates future deterministic compilation.

## Additional evidence-based analyst observations

These points are **[D] analyst observations**, not limitations admitted explicitly by the authors:

- Six news and two e-commerce sites form a narrow empirical basis for broad generalization.
- The benchmark sample size in articles/products is absent.
- The five-stage prompt is not included in the paper.
- Site tasks, crawl scopes, dates, and output schemas are underspecified.
- The Golden sets are created by the authors’ deterministic crawlers, but their independent validation is not described.
- Exact Figure 3 values are not tabulated.
- No statistical significance tests accompany “significant” performance claims.
- No latency, token, cost, server-request, or throughput results support scalability/efficiency claims.
- Only the combined Parse+Merge package is ablated; their individual contributions remain unknown.
- Temporal stability covers only three sites, seven days, and two time points.
- The e-commerce metric is not operationally defined.
- Comparing different foundation/reasoning components may complicate attribution: the full framework uniquely invokes GPT-o3-mini inside Parse Tool, so improvement reflects the complete multi-model system rather than tools abstracted from model capability.
- Temperature 0 does not guarantee deterministic behavior in the surrounding browser, website, model-serving, and network environment.
- Ethical principles are stated, but exact request frequencies, delays, and data volumes are not quantified.

# 17. Threats to Validity

The paper does not organize its discussion under these validity categories. The following is **[D] analyst assessment based only on supplied evidence**.

## Internal validity

Differences between conditions may arise from both the presence of functional tools and the additional GPT-o3-mini reasoning used by the full system. Because Parse and Merge are enabled together, their separate effects cannot be identified. Dynamic sites may also change between runs.

## Construct validity

Binary Correctness is strict and useful, but the paper does not specify ROUGE-L variant/aggregation. A threshold of 0.8 is supported mainly by a commercial precedent and informal observations. The e-commerce version of Correctness is insufficiently defined.

## Statistical conclusion validity

Thirty runs are justified through a representative CI convergence curve, but the estimator and all nine underlying settings are not shown. Figure 3 lacks intervals, variance measures, or tests. Consequently, numerical superiority is visible, but inferential significance is unestablished.

## External validity

All evaluated sites share the target index-and-content architecture. Results do not directly cover authenticated systems, streaming pages, arbitrary desktop applications, advanced virtual scrolling, or other website families.

## Ecological validity

Testing live dynamic websites is realistic, but exact dates, locales, consent banners, personalization, geographies, and page states are undocumented. These factors may affect what an agent sees.

## Reproducibility

The paper reports core model names, temperature, browser reset, and a code repository, but omits many execution details. The repository was not supplied. Live websites and hosted models can also change.

## Data leakage

The paper does not discuss whether the evaluated sites, page structures, or related code appeared in model training data. It also does not report precautions against such leakage.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

1. **Compile successful runs into deterministic scrapers.** Preserve validated interaction trajectories and code snippets as reusable Selenium- or Playwright-style scripts. The LLM would be used once to create the scraper, reducing recurring cost and stochasticity (p. 5, §5).

2. **Add technical webpage observability.** Extend the agent beyond GUI interaction to observe DOM mutations and network traffic.

3. **Handle virtual scrolling.** Use DOM-change monitoring to understand dynamic loading and content removal.

4. **Inspect network protocols and APIs.** Detect WebSockets and underlying application programming interface endpoints, potentially bypassing unnecessary GUI interaction.

5. **Create a hybrid generalist scraper.** Combine visual control with structural understanding of browsers and networks.

## B. Additional open questions

These are **[D] analyst-identified**:

- What exactly are the five prompting stages?
- How much do Parse and Merge contribute independently?
- How many records and pages were evaluated on each site?
- What are the confidence intervals for every Figure 3 and Table 2 result?
- Does the approach reduce cost, latency, or token usage in measured terms?
- How reusable is a generated parser after a website redesign?
- How are malformed records, partial pages, or duplicates detected?
- How should an agent resolve semantically competing fields such as multiple prices?
- Does the performance ordering hold with other foundational agents and parser-generating models?
- How does performance change across languages?
- Can Golden sets be independently validated?
- What safety controls are needed before following network endpoints or executing model-generated code?
- How long does temporal stability persist beyond seven days?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| AI agent | A model-based system that observes a situation, reasons, and takes actions using tools |
| Baseline | The reference system against which the proposed method is compared |
| Bash | Command-line tool used here for files, scripts, and network requests |
| CI | Confidence interval; an uncertainty range estimated around a measurement |
| CI half-width, \(\epsilon\) | Half the width of that confidence interval |
| Computer Use | Anthropic framework used as the foundational GUI-controlling agent |
| Correctness | Binary success metric requiring all specified matching conditions |
| DOM | Document Object Model, the browser’s structured representation of a webpage |
| Dynamic content | Content loaded or changed after the initial page response |
| Golden set | Manually constructed reference output used as ground truth |
| GUI | Graphical user interface |
| HTML | Hypertext Markup Language, the structured source representation of webpages |
| Index-and-content architecture | A listing/index page connected to many detail/content pages |
| JSON | JavaScript Object Notation, a structured data format |
| LLM | Large Language Model |
| Merge Tool | Custom tool that joins records across iterations and removes duplicates |
| MLLM | Multimodal Large Language Model, able to process text and visual inputs |
| Parse Tool | Custom tool that converts HTML into structured records using generated Python |
| Pagination | Moving through multiple result pages |
| Prompt ablation | Removing or disabling part of a system to measure its contribution |
| ROUGE-L | Text-overlap metric based on longest common subsequence |
| Str Editor | File-reading and editing tool available to the agent |
| Structured data | Records organized into explicit fields rather than free-form text |
| Visual grounding | Locating and acting on the correct screen element from visual input |
| Virtual scrolling | Interface behavior that loads and may unload items as the user scrolls |
| Web Information Extraction (WIE) | Turning webpage content into structured fields |
| WebSocket | A protocol named by the paper for persistent real-time communication |
| XPath | Expression used to identify elements in an HTML/XML document |
| \(n\) | Number of experimental runs in Figure 2 |
| \(T\), \(T+7\) | Initial evaluation time and evaluation seven days later |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Accessible document length | 7 | pages | Complete supplied text | Author-provided accessibility record | Pages 1–7 |
| News websites | 6 | sites | Main benchmark | Author-reported | p. 3, §4.2 |
| E-commerce websites | 2 | sites | Generalization test | Author-reported | pp. 4–5, §4.5 |
| Experimental configurations | 3 | configurations | Baseline, Prompt Only, Prompt + Tool | Author-reported | p. 3, §4.1 |
| Temperature | 0 | temperature setting | Computer Use experiments | Author-reported | p. 3, §4.1 |
| Selected repetitions | 30 | runs per setting | All experiments | Author-reported | p. 4, §4.3 |
| Correctness ROUGE-L threshold | 0.8 | score | Both title and content, plus exact URL | Author-reported | p. 3, §4.2 |
| Major-failure ROUGE-L observation | below 0.3 | score | Partial extraction or generated text | Author-reported | p. 3, §4.2 |
| LTN pagination successes | 2 of 30 | runs | Baseline; specific dynamic interaction | Author-reported | p. 4, §4.4 |
| LTN pagination success ratio | ~6.7% | percent | \(2/30\times100\) | Analyst-derived | p. 4, §4.4 |
| Website 3 full, T / T+7 | 0.511 / 0.533 | accuracy proportion | Temporal check | Author-reported | Table 1 |
| Website 4 full, T / T+7 | 0.648 / 0.673 | accuracy proportion | Temporal check | Author-reported | Table 1 |
| Website 5 full, T / T+7 | 0.820 / 0.820 | accuracy proportion | Temporal check | Author-reported | Table 1 |
| Max full-system temporal change | 0.025 | proportion; 2.5 points | Website 4 | Analyst-derived | Table 1 |
| Momo baseline | 0.000 | correctness | E-commerce | Author-reported | Table 2 |
| Momo Prompt Only | 0.040 | correctness | E-commerce | Author-reported | Table 2 |
| Momo full | 0.242 | correctness | E-commerce | Author-reported | Table 2 |
| Amazon baseline | 0.027 | correctness | E-commerce | Author-reported | Table 2 |
| Amazon Prompt Only | 0.138 | correctness | E-commerce | Author-reported | Table 2 |
| Amazon full | 0.422 | correctness | E-commerce | Author-reported | Table 2 |
| Full gain over baseline, Momo | 0.242 | proportion; 24.2 points | \(0.242-0.000\) | Analyst-derived | Table 2 |
| Full gain over baseline, Amazon | 0.395 | proportion; 39.5 points | \(0.422-0.027\) | Analyst-derived | Table 2 |
| Full gain over Prompt Only, Momo | 0.202 | proportion; 20.2 points | \(0.242-0.040\) | Analyst-derived | Table 2 |
| Full gain over Prompt Only, Amazon | 0.284 | proportion; 28.4 points | \(0.422-0.138\) | Analyst-derived | Table 2 |
| Figure 3 full-system range | ~30%–82% | Average Correct | Across six news sites | Approximate visual estimate | Figure 3 |
| PTS full result | ~82% | Average Correct | Highest visually estimated news result | Approximate visual estimate | Figure 3 |
| BBC Prompt + Tool | ~53% | Average Correct | News benchmark | Approximate visual estimate | Figure 3 |
| BBC Prompt Only | ~9% | Average Correct | News benchmark | Approximate visual estimate | Figure 3 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Structured prompting improves over default Computer Use | Prompt Only bars exceed baseline across six news sites; Table 2 repeats this on both commerce sites | X3, X5; Figure 3; Table 2 | pp. 4–5 | Strong directional evidence within tested tasks; no inferential statistics |
| Functional tools improve beyond prompting | Full system exceeds Prompt Only for every reported site | X4; Figure 3; Table 2 | pp. 4–5 | Strong and consistent ablation direction, but Parse and Merge are bundled |
| Full Webscraper outperforms the baseline | Red bars dominate blue; 0.242 vs 0.000 and 0.422 vs 0.027 | X3, X5 | pp. 4–5 | Directly supported for eight tested sites |
| Thirty runs are an efficient standard | CI half-width curve flattens around 30 | X1; Figure 2 | pp. 3–4 | Moderate evidence; only representative curve and no formula |
| Full-system performance is stable after seven days | Absolute changes are 0.022, 0.025, and 0 | X2; Table 1 | p. 4 | Direct but narrow evidence: three sites, one interval |
| General-purpose agents struggle with pagination | Baseline reportedly succeeds only twice in 30 LTN runs | X3 | p. 4, §4.4 | Specific supporting example; aggregation meaning unclear |
| The method generalizes to e-commerce | Same configuration ranking on Momo and Amazon | X5; Table 2 | pp. 4–5 | Supports limited transfer, not universal generality |
| Momo’s multiple prices increase difficulty | Momo score lower than Amazon; screenshot shows competing price fields | X5; Figure 4 | pp. 4–5 | Plausible author interpretation; causal isolation absent |
| Reusable scripts are more scalable than page-by-page agents | Architectural reasoning and discussion | System design | p. 5, §5 | Conceptually supported; cost/scale not quantitatively measured |
| The framework handles modern dynamic sites robustly | Tested sites include several interaction patterns and full method leads | Figure 3; §4.2–4.4 | pp. 3–4 | Supported for benchmark; exact per-pattern breakdown absent |
| Ethical scraping burden was minimal | Authors state low frequency, delays, and minimal data volume | Ethical Considerations | pp. 5–6 | Author-reported only; quantities not supplied |

# 22. Very Simple Explanation

Imagine a shopping website or news site with one page full of links. A normal AI browsing agent might click the first link, read the page, go back, click the second link, and repeat. That works in principle, but it is slow, fills the AI’s limited working memory, and can break when the site uses scrolling or unusual buttons.

Webscraper gives the AI a division of labor. The AI still looks at the screen and navigates, but special tools handle the bulk extraction. One tool turns the site’s HTML into a reusable Python parser; another joins records from several pages and removes duplicates. It is similar to asking a person to find the right filing cabinet, then letting a program copy all similarly formatted files rather than having the person transcribe each one.

The researchers tried an ordinary browsing agent, the same agent with better instructions, and the instructed agent with real parsing and merging tools. Better instructions helped, and working tools helped more on every tested site. On Amazon, for example, the scores were 0.027, 0.138, and 0.422 in that order.

The idea is promising, but it is not a universal web scraper. It can still click the wrong place, generate broken code, or become confused by several fields that all look like “the price.” The tests also cover only eight sites, and the paper does not measure speed or cost directly. The fairest conclusion is that specialized guidance and tools make this particular agent much better at the tested index-and-detail websites, while substantial work remains before it can handle every kind of site reliably.

# Completeness Audit

## Inventory-based coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, affiliation | Yes | Yes | Fully represented | Title page, p. 1 |
| Publication information | Yes | Yes | Fully represented | arXiv identifier/date available; venue absent |
| Abstract | Yes | Yes | Represented in compressed form | Claims incorporated into orientation and contributions |
| Keywords | Yes | Yes | Represented in compressed form | Concepts incorporated into glossary |
| §1 Introduction | Yes | Yes | Fully represented | Problem, motivation, method concept, contributions |
| §2 Related Work | Yes | Yes | Represented in compressed form | Prior-work categories and claimed gaps retained |
| §3 Methodology | Yes | Yes | Fully represented | Task and architecture covered |
| §3.1 Task Definition | Yes | Yes | Fully represented | Index/content definitions, prompt, JSON output |
| §3.2 System Architecture | Yes | Yes | Fully represented | Agent, native/custom tools, flow |
| Foundational Agent subsection | Yes | Yes | Fully represented | Computer Use role covered |
| Native Environment Tools subsection | Yes | Yes | Fully represented | Computer, Bash, Str Editor covered |
| Parse Tool description | Yes | Yes | Fully represented | Operation and three rationales covered |
| Merge Tool description | Yes | Yes | Fully represented | Aggregation and deduplication covered |
| §4 Experiments | Yes | Yes | Fully represented | Five distinct analyses registered |
| §4.1 Experiment Setting | Yes | Yes | Fully represented | Three conditions, models, temperature, browser |
| §4.2 Benchmark and Metrics | Yes | Yes | Fully represented | Sites, Golden set, ROUGE-L, Correctness |
| §4.3 Experimental Stability | Yes | Yes | Fully represented | Convergence and seven-day test separated |
| §4.4 News Results | Yes | Yes | Fully represented | Directional and approximate numerical evidence |
| §4.5 E-commerce Generalization | Yes | Yes | Fully represented | Exact Table 2 results and derived differences |
| §5 Discussion and Conclusion | Yes | Yes | Fully represented | Interpretation, failure modes, future directions |
| Ethical Considerations | Yes | Yes | Fully represented | Public access, server burden, academic-only use |
| §6 References | Yes | Partly | Inspected but deliberately compressed | All 17 entries present; summarized by their role rather than reproduced |
| Explicit research questions | Yes | Yes | Fully represented | None formally stated |
| Explicit hypotheses | Yes | Yes | Fully represented | None formally stated |
| Contributions | Yes | Yes | Fully represented | Conceptual, methodological, system, tool, experimental |
| X1 run-count convergence | Yes | Yes | Fully represented | Figure 2 and caveats covered |
| X2 temporal stability | Yes | Yes | Fully represented | Table 1 and derived changes covered |
| X3 six-site news benchmark | Yes | Yes | Fully represented | Figure 3 visually inspected |
| X4 prompt/tool ablation | Yes | Yes | Fully represented | Cross-site direction reported |
| X5 e-commerce generalization | Yes | Yes | Fully represented | Exact scores and ambiguity discussion |
| Figure 1 | Yes, visually | Yes | Fully represented | Components and flows explained |
| Figure 2 | Yes, visually | Yes | Fully represented | Axes, legend, trend, uncertainty covered |
| Figure 3 | Yes, visually | Yes | Fully represented | Axes, groups, approximate bars, caveats |
| Figure 4 | Yes, visually | Yes | Fully represented | Screenshot content and evidential limits |
| Table 1 | Yes, visually/textually | Yes | Fully represented | Every cell represented |
| Table 2 | Yes, visually/textually | Yes | Fully represented | Every cell represented |
| Major equations | Yes | Yes | Fully represented | None in source; metric formalization labeled analyst-derived |
| Algorithms/pseudocode | Yes | Yes | Fully represented | None present |
| Theorems/lemmas/propositions | Yes | Yes | Fully represented | None present |
| Footnote 1 | Yes | Yes | Fully represented | Repository noted but not inspected |
| Author-stated limitations | Yes | Yes | Fully represented | All explicit failure modes and scope limits included |
| Appendices | Yes | Yes | Fully represented | None present |
| Supplied supplementary material | Yes | Yes | Fully represented | None supplied |
| Pages 6–7 visual layout | No | Yes | Inaccessible visually | Text inspected; no substantive visuals detected |

## Missing or inaccessible material

- Pages 6–7 were available as text but not rendered for visual inspection.
- The source-code and prompt repository cited in footnote 1 was not supplied.
- The central five-stage prompt procedure is not enumerated in the paper text.
- No appendices or supplementary files were provided.
- Exact Figure 3 bar values are absent.
- Exact Figure 2 values other than the selected \(n=30\) are too small and unlabeled for confident extraction.
- Publication venue information is absent.
- Dataset record counts and detailed task definitions are absent.

## Uncertain interpretations

- Whether “GPT-o3” and “GPT-o3-mini” refer to precisely the same Parse Tool model.
- What constitutes the “nine experimental settings” in §4.3.
- Whether “variance of less than 5%” means absolute change, relative change, or a formal variance.
- How the two-of-30 LTN pagination result relates to Figure 3’s aggregate correctness.
- Which Figure 3 sites correspond to Website 3, Website 4, and Website 5 in Table 1.
- The exact e-commerce Correctness rule.
- The exact ROUGE-L variant and aggregation.
- Whether “significant” is intended statistically; no statistical test is reported.

## Deliberately compressed material

- The 17 bibliographic entries were inventoried as the References section but not individually summarized, because they are citations to external work rather than evidence generated by this study.
- Repeated prose in §4.3 about the \(n=30\) elbow was consolidated.
- The repeated explanation of Momo’s multiple-price ambiguity across pp. 4–5 was stated once in each relevant analytical context rather than reproduced verbatim.
- Repeated abstract, introduction, and conclusion claims were integrated without duplicating identical wording.

## Potential omissions

No known substantive section, subsection, experiment, figure, table, contribution, author-stated limitation, or ethical principle from the supplied seven-page paper is absent from the analysis. Exact information that the paper itself does not provide—particularly prompt stages, dataset sizes, detailed execution settings, statistical procedures, and exact Figure 3 values—has been marked missing or uncertain rather than reconstructed.