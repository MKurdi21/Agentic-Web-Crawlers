## Stage 0 — Document Accessibility Report

The supplied material contains extracted text for physical PDF pages 1–7 and rendered images for pages 1–5. All seven supplied text pages were inspected. Pages 1–5 were also inspected visually, including the architecture diagram, both plots, both tables, and the product-page screenshot. Pages 6–7 were inspected through supplied text only; their page layout and typography were not visually verified. No tools, browsing, external sources, repository access, or supplementary-file retrieval were used.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied seven-page text extraction with five page images |
| Physical page range | 1–7 |
| Apparently missing pages | None evident within the supplied sequence; this does not independently establish that every author artifact was supplied |
| Visual coverage | Pages 1–5 visually inspected; pages 6–7 text-only |
| Figures | Figures 1–4 are present and visually inspected |
| Tables | Tables 1–2 are readable in both supplied text and page images |
| Equations | No numbered equations or substantial displayed mathematical derivations are present |
| Appendices | None present or identified in the supplied document |
| Supplementary material | No supplementary files supplied |
| Referenced implementation artifact | A source-code and prompts repository is identified in the p. 3 footnote; its contents were not supplied or inspected |
| OCR | Not needed for the readable supplied text; no independent OCR was performed |
| Resolution limitations | Figure 3 supports approximate bar-height comparisons, not exact numerical recovery; Figure 4's small product-interface text does not support reliable transcription of all prices |
| Extraction limitations | Page 7 contains only reference [17]; reference-name typography on pages 6–7 may contain extraction artifacts |

The paper is readable enough to analyze its system, experimental design, reported tables, conclusions, and stated limitations. The actual five-stage system prompt, full code, raw results, ground-truth records, and detailed statistical implementation cannot be assessed from these materials. Their absence matters because some central procedural and reproducibility details are delegated to the referenced repository.

Evidence labels used throughout: **[A] Author-reported**, **[B] Directly observable**, **[C] Analyst-derived**, and **[D] Analyst interpretation**. No external information, category [E], is introduced. Confidence is HIGH for clear textual statements and exact table values, MEDIUM for supported but incomplete interpretations, LOW for speculative implications, and UNKNOWN where necessary information is absent. A HIGH-confidence report that the authors make a claim does not independently establish the claim's general truth.

## 1. Plain-language orientation

**Original title:** *WEBSCRAPER: LEVERAGE MULTIMODAL LARGE LANGUAGE MODELS FOR INDEX-CONTENT WEB SCRAPING*. The authors are Guan-Lun Huang and Yuh-Jzer Joung, Department of Information Management, National Taiwan University, Taipei, Taiwan. The first-page margin identifies arXiv:2603.29161v1, category cs.AI, dated 31 March 2026. No publication venue for this paper is supplied. [A/B: p. 1]

This is an experimental artificial-intelligence systems paper about collecting structured information from interactive websites. A conventional scraper can struggle when information appears only after scrolling, clicking, or executing a dynamic interface. The researchers build a system that combines a model able to interpret screenshots with computer-control tools, HTML parsing, and result merging. Their focus is the **index-and-content** pattern: a directory page lists articles or products, and linked detail pages contain the full information. [A: pp. 1–3]

The central contribution is a specialized workflow built on Anthropic's Computer Use agent. A guiding system prompt organizes extraction, while a Parse Tool delegates HTML processing and script generation to another reasoning model. A Merge Tool combines results and removes duplicates. The authors compare the ordinary agent, the agent with the guiding prompt alone, and the full prompt-plus-tools system. [A: pp. 2–3]

The full system has the highest reported performance on all six news websites and both e-commerce websites. Exact e-commerce Correctness values are 0.242 on Momo and 0.422 on Amazon, versus baseline values of 0.000 and 0.027. These improvements coexist with substantial remaining failure: the full system's reported e-commerce scores are below 0.5 under the stricter product-data criterion. News results are plotted rather than fully tabulated. [A/B: pp. 4–5, Fig. 3, Table 2]

**Relationship to the user's security research question:** this paper does not directly compare web agents with standalone large language models, does not introduce an attacker, and does not measure security vulnerabilities. Its relevance is architectural and inferential: it documents an agent reading website content, controlling a computer, making network requests, writing files, and executing model-generated parsing code. Those capabilities identify components that a separate security investigation could examine. Performance errors in this paper must not be relabeled as successful attacks. [D: pp. 2–5; confidence MEDIUM for architectural relevance, UNKNOWN for comparative vulnerability]

## 2. Document roadmap

The supplied work is best classified as an **empirical AI systems and web-extraction study**, with a prompting ablation and a small cross-domain evaluation. It is not a security evaluation, theoretical paper, systematic review, or formal benchmark-specification paper.

| Inventory ID | Original component | Physical pages | Role |
|---|---|---:|---|
| FRONT | Title, authors, affiliation, preprint identifier | 1 | Identifies the work |
| ABSTRACT | Abstract and index terms | 1 | Summarizes problem, method, and evaluation |
| S1 | §1 Introduction | 1 | Motivation and three contributions |
| S2 | §2 Related Work | 1–2 | Positions navigation and extraction approaches |
| S3 | §3 Methodology | 2–3 | Defines task and system |
| SS3.1 | §3.1 Task Definition: Index-and-Content Scraping | 2 | Index pages, detail pages, input and output |
| SS3.2 | §3.2 System Architecture | 2–3 | Foundational agent, native tools, Parse and Merge Tools |
| S4 | §4 Experiments | 3–5 | Configurations, metrics, stability, domain evaluations |
| SS4.1 | §4.1 Experiment Setting | 3 | Three compared configurations |
| SS4.2 | §4.2 Benchmark and Metrics | 3 | News reference data and Correctness |
| SS4.3 | §4.3 Preliminary Analysis: Experimental Stability | 3–4 | Run-count choice and seven-day repeat |
| SS4.4 | §4.4 Main Results on News Websites | 4 | Six-site comparison |
| SS4.5 | §4.5 Generalization to E-commerce Websites | 4–5 | Momo and Amazon comparison |
| S5 | §5 Discussion and Conclusion | 5 | Interpretation, failures, and future directions |
| ETHICS | Ethical Considerations | 5–6 | Access restrictions, request pacing, data use |
| S6 | §6 References | 6–7 | Seventeen cited references |
| F1 | Fig. 1 architecture diagram | 2 | Agent, tools, feedback, structured output |
| F2 | Fig. 2 confidence-interval convergence plot | 4 | Rationale for 30 runs |
| F3 | Fig. 3 grouped news-performance bars | 4 | Three methods across six news sites |
| F4 | Fig. 4 Momo screenshot | 5 | Multiple competing price fields |
| T1 | Table 1 temporal stability | 4 | Baseline and full system at T and T+7 |
| T2 | Table 2 e-commerce performance | 5 | Three methods on two product sites |
| FN1 | Source-code and prompts footnote | 3 | Points to an absent implementation artifact |

The experimental register contains X1 run-count convergence, X2 temporal stability, X3 six-site news extraction, and X4 two-site product extraction. The three configurations within X3/X4 also provide the prompt-only ablation. No formal hypotheses, numbered algorithms, pseudocode listings, theorems, appendices, or major equations appear. The inventory is the basis of the coverage audit, rather than an assumption that a long explanation is complete.

## 3. Background and context

A **large language model**, abbreviated LLM, is the model class discussed by the paper for reasoning and code generation. A **multimodal large language model**, MLLM, additionally processes visual input such as webpage screenshots. In this system, screenshot interpretation is coupled to actions like moving a mouse, clicking, and scrolling. The authors describe this as enabling human-like interaction with dynamic pages. [A: p. 1]

**Web navigation** means interacting with the interface to reveal or reach information. **Web Information Extraction**, WIE, means turning the revealed page content into usable fields. A page's **HTML**, Hypertext Markup Language, provides the semi-structured material that the parsing tool processes. The authors distinguish navigation from extraction because a parser cannot collect content that the interface has not yet exposed. [A: pp. 1–2]

An **index page** lists multiple items and typically provides links. A **content page** contains one item's details. For example, the supplied task asks for the first two pages of a BBC section and the title, link, and content for each article. This example specifies task scope; it does not establish that every benchmark task used exactly two pages. [A: p. 2]

**Pagination** moves between successive batches of listed items. **Infinite scrolling** reveals more information as the user scrolls. The benchmark includes these interaction patterns and dynamic loading. The paper later distinguishes advanced **virtual scrolling**, where content is unloaded from the Document Object Model, DOM, as the user scrolls; the authors identify that pattern as difficult for their approach. [A: pp. 3, 5]

The related-work account groups prior systems into visual navigation agents, rule-based extraction wrappers, learned or model-based extraction, and reusable scraper generation. SeeAct and WebVoyager represent visual browsing approaches; Anthropic's Computer Use represents general computer interaction; AutoScraper represents progressive generation and validation of XPath expressions. **XPath** is the location-expression mechanism discussed in that comparison. These descriptions are the authors' positioning of prior work, not independently verified assessments. [A: pp. 1–2]

## 4. Research problem and gap

**Existing problem.** The authors argue that modern web scraping must deal with JavaScript-driven loading, noisy page elements, and changing site structures. Expert-designed crawlers require manual maintenance, while plain static HTML processing is insufficient when interaction is needed to reveal content. [A: p. 1]

**Shortcomings attributed to prior approaches.** Visual agents provide detailed interaction, but the authors say general agents often lack procedural knowledge for large-scale structured extraction. LLM-based extraction can be computationally expensive. Reusable XPath-generation approaches are described as cost-effective but oriented toward locating individual data points rather than collecting complete sets of related records. [A: pp. 1–2]

**Research gap.** The paper seeks a unified system connecting navigation with data-oriented extraction. The gap is not simply the absence of an agent that can click: it is the absence, in the authors' framing, of a sufficiently organized workflow for exposing content, collecting many related entries, and consolidating structured output. [A: p. 2]

**Motivation.** News information is timely and useful for applications such as public-opinion analysis; the authors also mention growing data demand from applications including LLM pretraining. These are motivations, not tasks evaluated directly in the experiments. [A: p. 1]

**Scope.** The proposed method targets index-and-content sites. News and e-commerce are tested. Video galleries and social-media feeds are mentioned as examples of the architecture, but no experiments on those domains are reported. Likewise, the supplied evaluation does not establish real-time streaming support, adversarial robustness, or arbitrary website coverage. [A/D: pp. 2–5]

## 5. Research questions / objectives / hypotheses

The paper provides objectives and contributions, rather than formally numbered research questions or explicit hypotheses. Its stated objectives are to make MLLM-based prompting feasible for index-content scraping, improve task accuracy using specialized extraction tools, and assess generalization to domains such as e-commerce. [A: p. 1]

The experimental design can be mapped to these objectives without manufacturing author-written questions:

| Objective ID | Author-stated objective | Corresponding evidence |
|---|---|---|
| O1 | Demonstrate feasibility of prompt design for index-content scraping | Prompt-only configuration in the news comparison |
| O2 | Improve extraction accuracy through specialized tools | Full system compared with prompt-only and baseline |
| O3 | Evaluate generalization beyond news | Momo and Amazon product-data evaluation |

**Analyst interpretation:** the ablation asks whether organizing the agent's behavior helps and whether functional tools add further benefit. That is a useful explanatory reading of the design, but the paper does not state it as a formal hypothesis. No experiment addresses the user's comparative security question. Any conclusion about why web agents are more vulnerable than standalone LLMs remains outside this paper's measured outcomes. [D: pp. 3–5]

## 6. Assumptions / threat model

There is **no explicit security threat model**. The supplied work does not define an attacker, malicious webpage, protected asset, instruction hierarchy, privilege boundary, injection technique, or attack-success metric. It does not report defensive filtering or isolation tests. These are absences in the supplied description, not proof that the implementation contains no protections.

The operational system assumes a natural-language user task identifies the website, crawl scope, and desired fields. It assumes the agent can inspect and interact with a standard computer environment, obtain raw HTML for parsing, use a delegated code-generation/execution environment, and write consolidated output. The paper does not fully describe how raw HTML is acquired or passed between components. [A/D: pp. 2–3]

The evaluation assumes manually written deterministic crawlers provide the reference URLs, titles, and article content. The validity of that reference data is important, but independent annotation, reference-crawler auditing, disagreement handling, and gold-set coverage checks are not specified. [A/D: p. 3]

The ethical scope is publicly available material. The authors report no attempts to bypass login walls, paywalls, or other access controls. They also report low-frequency requests and significant delays. These are experiment-conduct restrictions; they are not a tested security architecture or a technical demonstration of enforced access boundaries. [A/D: pp. 5–6]

**Research relevance, analyst inference:** webpages and HTML provide external input; Computer, Bash, and Str Editor provide action capabilities; the Parse Tool connects external content to model-generated code execution. A security study could examine how these interfaces distinguish data from instructions and constrain actions. The present paper does not answer those questions or establish vulnerability prevalence. [D: pp. 2–3; confidence MEDIUM]

## 7. Methodology

### System and workflow

The base layer is Anthropic's Computer Use framework. The agent receives the user's extraction request and a system prompt, then selects tools to pursue the objective. The enhanced system adds a guiding system prompt and two custom tools. The authors repeatedly identify a **five-stage extraction process**, but the five individual stages are not enumerated in the supplied text. It would be unsupported to invent stage names or a detailed mandatory order. [A: pp. 1–2]

The native **Computer** tool supplies screen observation, mouse movement, clicking, and scrolling. **Bash** supplies command-line access for filesystem operations, script execution, and network requests; examples include mkdir, ls, and curl. **Str Editor** reads, writes, and modifies files, supporting generated extraction scripts. These capabilities are expressly described, but their permissions, sandboxing, and failure-handling policies are not specified. [A: p. 3]

The custom **Parse Tool** accepts raw HTML and user requirements. A reasoning model generates a tailored Python script, which runs within a GPT code interpreter environment to produce structured data. The authors give three rationales: offload verbose code generation and execution to preserve the main context window; improve index-page parsing by delegating to a more powerful model; and keep the guiding prompt focused on strategy rather than low-level parsing instructions. These are design rationales; the paper does not separately measure each proposed benefit. [A: p. 3]

The **Merge Tool** aggregates lists from multiple scraping iterations, removes duplicates, and consolidates results. This supports pagination, where later iterations may produce additional or overlapping items. The supplied text does not specify the deduplication key, conflict-resolution rule, schema validation, or treatment of partially extracted records. [A/D: p. 3]

Expected output is a single structured **JSON**, JavaScript Object Notation, file containing a list of item objects and their requested fields. The discussion emphasizes generating a reusable script for content pages instead of visiting every page through sequential GUI interaction. The complete control logic connecting navigation, parsing, content-page script generation, and merging is not provided as pseudocode. [A: pp. 2, 5]

### Compared configurations

| Configuration | Guiding crawler prompt | Functional Parse/Merge Tools | Description |
|---|---|---|---|
| Baseline Agent | Absent | Absent | Zero-shot default Computer Use agent receives the task |
| Webscraper, Prompt Only | Present | Disabled | Tool-operation descriptions are embedded in the prompt |
| Webscraper, Prompt + Tool | Present | Present | Full proposed framework |

The baseline model identifier is **claude-3-7-sonnet-20250219**. Temperature is **0** for all experiments. Crawler guidance is appended to the default system prompt for both enhanced variants. Each run begins with a clean Firefox instance. Hardware, operating-system version, Firefox version, API configuration, token budgets, timeouts, seeds, and tool-library versions are not reported. [A: p. 3]

A model-description discrepancy must be retained: the Parse Tool explanation names **GPT-o3**, whereas the experiment-setting paragraph names **OpenAI GPT-o3-mini** as the reasoning model used in the full system. The latter is the more specific experiment statement, but the supplied work does not explicitly explain the difference. It is not appropriate to silently treat the names as interchangeable. [A: p. 3]

### Data and reference construction

The benchmark comprises **six Chinese- and English-language news websites**, with different structures including infinite scrolling, button pagination, and dynamic loading. Figure 3 names Appledaily, BBC, CNN, LTN, PTS, and UDN. For each website, the authors manually write a deterministic crawler to construct a Golden set containing precise article URLs, titles, and content. [A/B: pp. 3–4]

No article counts, per-task item counts, collection dates, inclusion criteria, field-cleaning rules, or reference-crawler source details are supplied. There are no training, validation, or test splits described; the experiments evaluate configured agents rather than report training a new model. The e-commerce extension uses Momo and Amazon and targets structured fields such as prices and ratings, but its sample size and reference-construction details are not fully specified. [A/D: pp. 3–5]

### Metrics and statistics

For news, the authors use **ROUGE-L**, named after the cited ROUGE evaluation method, to assess title and content extraction. They motivate it as less brittle than Exact Match for long articles containing noise, while penalizing over-extraction and under-extraction. The exact ROUGE-L formula, tokenization, language handling, and chosen precision/recall/F-score variant are not stated. [A: p. 3]

An article is correct only when its URL exactly matches the reference and **both** title and content obtain ROUGE-L scores of at least **0.8**. The conjunction matters: one strong field cannot compensate for another failing field. The authors justify 0.8 using a cited commercial-system convention and their observations that minor-noise extractions score above 0.8 while substantial failures score below 0.3. No supporting threshold-calibration table is supplied. [A: p. 3]

Product extraction uses a stricter Correctness criterion requiring a **near-exact match**. The exact tolerance, per-field checks, and handling of missing fields are not defined. Thus news and product Correctness values should not be treated as scores under an identical operational metric. [A/D: p. 4]

The paper selects **30 runs** by examining the **95% confidence interval**, CI, half-width and its diminishing improvement. It also repeats a subset of evaluations after **seven days**. The CI estimator, sampling assumptions, raw run values, and formal significance tests are not given. Temperature 0 and a clean browser do not, by themselves, establish that all experimental variation is eliminated. [A/D: pp. 3–4]

## 8. Experiments / analyses

### X1 — Run-count convergence

Purpose: choose a practical number of repetitions. The authors examine how the 95% CI half-width changes with the number of experimental runs and report diminishing returns after approximately 30. Figure 2 provides one representative scenario. The manipulated quantity is run count; the plotted response is uncertainty half-width. [A/B: pp. 3–4]

The authors say the analysis spans **nine experimental settings**, but the later design has six news sites and three configurations. Those descriptions do not establish that all 18 site-by-method combinations entered the convergence study. The subset or definition of the nine settings is unexplained. The selected standard is 30 runs, not a proof of a particular error margin or statistical power. [A/D: pp. 3–4]

### X2 — Temporal stability

Purpose: test whether results change after a seven-day interval. Table 1 compares baseline and full system on Website 3, Website 4, and Website 5 at T and T+7. The supplied table does not explicitly map these numbered websites to Figure 3's named sites. [A/B: p. 4]

Full-system scores are 0.511→0.533, 0.648→0.673, and 0.820→0.820. Baseline scores are 0.103→0.061, 0.277→0.317, and 0.145→0.179. The full system changes by +0.022, +0.025, and 0.000 on the score scale. These are **analyst-derived** differences, equivalent to +2.2, +2.5, and 0.0 percentage points when expressed as proportions. [C: p. 4, Table 1]

The authors describe variation as less than 5%. They do not define whether this means percentage-point change, relative change, or statistical variance. The full-system relative changes computed from the table are approximately 4.31%, 3.86%, and 0%, but the baseline's relative changes are much larger. Stability evidence is limited to the three shown websites and this interval; it does not establish long-term durability. [A/C/D: p. 4]

### X3 — Main news evaluation and prompting/tool ablation

Purpose: compare extraction success across six news sites and distinguish prompting from functional tool support. Conditions are baseline, Prompt Only, and Prompt + Tool. The response is article Correctness under exact URL matching plus the two ROUGE-L thresholds. Figure 3 shows grouped performance bars. [A/B: pp. 3–4]

The full system exceeds both alternatives on every displayed site. Prompt Only also has higher bars than the baseline on every site. Exact means for all bars are not printed, and the figure does not show uncertainty bars. Its pattern supports the ranking, while exact effect sizes and statistical significance cannot be reconstructed confidently from the visual alone. [B/D: p. 4]

The authors attribute baseline failures particularly to pagination and report that it operated pagination successfully only twice in 30 runs on LTN. That count describes navigation success, not the article Correctness value itself. They also report prompt-guided shortcuts such as Ctrl+F helping locate sections on tasks without pagination. These explanations are not isolated through separate navigation-only or shortcut-only experiments. [A/D: p. 4]

### X4 — Product-domain extension

Purpose: test transfer of the framework to two e-commerce sites. Tasks extract structured product information, such as prices and ratings, using stricter near-exact Correctness. Table 2 compares the same three configurations on Momo and Amazon. [A/B: pp. 4–5]

Momo scores are 0.000 baseline, 0.040 Prompt Only, and 0.242 full system. Amazon scores are 0.027, 0.138, and 0.422. The method ordering persists. The authors attribute Momo's lower score to multiple competing price fields; Figure 4 illustrates that ambiguity. There is no supplied error-count breakdown establishing how much of the difference comes from price ambiguity rather than other site differences. [A/B/D: pp. 4–5]

## 9. Results

The most secure empirical conclusion is **within the supplied evaluation, specialized guidance plus functional tools consistently has the best reported performance**. The conclusion is supported by all Figure 3 groups and both Table 2 rows. The authors use the word significant, but the supplied material does not report p-values, a named significance test, or confidence intervals for the between-method differences. Here, significant is preserved as author wording rather than converted into a verified statistical result. [A/B/D: pp. 4–5]

Exact product-domain comparisons can be calculated from Table 2:

| Site | Comparison | Calculation | Analyst-derived difference |
|---|---|---|---:|
| Momo | Full minus baseline | 0.242 − 0.000 | 0.242 = 24.2 percentage points |
| Momo | Full minus Prompt Only | 0.242 − 0.040 | 0.202 = 20.2 percentage points |
| Amazon | Full minus baseline | 0.422 − 0.027 | 0.395 = 39.5 percentage points |
| Amazon | Full minus Prompt Only | 0.422 − 0.138 | 0.284 = 28.4 percentage points |
| Across sites | Amazon full minus Momo full | 0.422 − 0.242 | 0.180 = 18.0 percentage points |

These are absolute differences, not relative percent improvements. A relative improvement over the zero Momo baseline is undefined because it would require division by zero. Cross-site differences do not isolate a causal mechanism: Momo and Amazon differ in more than the visible price-field example. [C/D: Table 2]

Temporal results support limited short-term consistency of the full system on the sampled sites. Figure 2 supports the authors' practical choice of 30 repetitions. Neither analysis establishes broad reliability under site redesign, adversarial content, longer intervals, or a different task distribution. [A/D: p. 4]

The paper also reports failure modes involving inaccurate visual targeting and buggy generated parsing scripts. These findings constrain the positive results: the system improves task performance while retaining weaknesses in navigation, interpretation, and generated-code correctness. No numerical failure taxonomy or security incident rate is supplied. [A: p. 5]

## 10. Figure-by-figure interpretation

### Figure 1 — Proposed system architecture

This is a component-and-feedback diagram, not a plot. It contains a user, a system-prompt input, an AI agent labeled Computer Use, a thought cloud labeled Thinking & Tool-use, a tools block, a Tool Result block, and a Structural Data return path. The tools block visually separates native Computer, Bash, and Str Editor tools from yellow-highlighted Parse and Merge Tools. [B: p. 2]

The inputs reach the agent; the agent selects tools; tool results, including screenshots and execution results, feed back toward the agent. The output path returns structured data to the user. Arrows encode action and feedback rather than a fully specified five-stage sequence. No explicit decision diamonds, security barriers, or execution-permission controls are drawn. Their absence from the diagram does not establish their absence from code. [B/D]

The caption and §3.2 agree that the contribution combines an existing agent with native and custom tools. The diagram supports the component relationships. It does not expose the internal Parse Tool implementation, model versions, validation rules, or exact prompt stages. Confidence HIGH for visible components and MEDIUM for implications about workflow details.

### Figure 2 — Convergence of confidence-interval half-width

Figure 2 is a line plot. The horizontal axis is Number of Experimental Runs, n. The vertical axis is 95% CI Half-Width, ε. A blue line with small markers represents the uncertainty half-width, and a red point marks Chosen Point, n=30. Both axes are displayed on ordinary linear scales. The horizontal span extends to approximately 50 runs; a brief high value and fluctuation occur at very low run counts. [B: p. 4]

The dominant pattern is a rapidly declining half-width followed by a flatter tail. The caption calls the elbow visible around n=30. The chosen point is visually low on the vertical scale, but no exact numerical half-width at n=30 is printed. Its unit and normalization are not fully specified, so the visual should not be used to claim a precise margin in percentage points. [A/B/D]

The plot is a representative scenario, whereas the text refers to nine settings. It supports diminishing returns in that scenario; it does not display nine individual convergence curves or guarantee a universal uncertainty bound. The early line fluctuation also means the decrease is not perfectly monotonic at every run count. No formal optimization criterion or predetermined tolerance is shown.

### Figure 3 — News-site comparison

Figure 3 is a grouped vertical bar chart with six site groups: Appledaily, BBC, CNN, LTN, PTS, and UDN. The horizontal axis is Experiment Group. The vertical axis is Average Correct (%), with a linear 0–100 scale. The legend maps blue to Computer use, green to Webscraper (Prompt Only), and red to Webscraper (Prompt + Tool). There are no displayed error bars or significance markers. [B: p. 4]

**Approximate visual estimates only:** baseline bars appear around 4%, 6%, 12%, 32%, 18%, and 12%; Prompt Only around 26%, 12%, 25%, 54%, 58%, and 36%; full-system bars around 29%, 53%, 56%, 67%, 82%, and 51%, respectively. These estimates are rounded readings from bar heights, not exact reported numerical results. They should not be substituted for raw data. [B: approximate visual estimate, confidence MEDIUM]

The robust observation is the ranking: red exceeds green and blue in every group. PTS has the tallest full-system bar, and Appledaily the shortest full-system bar. The tool-associated gap is visibly much smaller on Appledaily than on several other sites. Thus the benefit varies across sites even though its direction is consistent. [B]

The text's explanation concerns pagination and section location, but Figure 3 does not mark which sites require which interaction mechanisms. It also does not separate missing items from incorrect fields or measure navigation success independently. Table 1's numbered websites should not be assigned names solely because some values resemble these bar heights.

### Figure 4 — Momo price ambiguity

Figure 4 is a screenshot of a product-detail page. It shows shoe imagery, selectable product information, and several text fields. A red rectangle emphasizes a price-bearing interface region. There are no statistical axes, units defined by a chart, or experimental panels. [B: p. 5]

The caption says the agent must identify market price among competing promotional and discounted-price fields. The screenshot visually supports the presence of a dense interface and an emphasized price area. At the supplied scale, I cannot confidently transcribe every field label and exact price. The analysis therefore relies on the readable caption for the intended field distinctions and does not invent monetary values. [A/B]

The screenshot illustrates an error mechanism proposed by the authors; it does not quantify that mechanism's frequency. It contains no evidence of malicious manipulation, injected instructions, or an attack. Interpreting it as a security exploit would exceed the supplied evidence. [D]

## 11. Table-by-table interpretation

### Table 1 — Seven-day temporal stability

Table 1 compares accuracy at T and T+7 days for three numbered websites. Each row has two baseline columns and two full-system columns. The entries are decimal accuracy values; no uncertainty intervals, sample counts, p-values, missing-value symbols, or significance markers are supplied. [A/B: p. 4]

| Website | Baseline T | Baseline T+7 | Full T | Full T+7 |
|---|---:|---:|---:|---:|
| Website 3 | 0.103 | 0.061 | 0.511 | 0.533 |
| Website 4 | 0.277 | 0.317 | 0.648 | 0.673 |
| Website 5 | 0.145 | 0.179 | 0.820 | 0.820 |

The full system exceeds baseline in all six same-site, same-time comparisons. Website 5 ties its own full-system score across the two times. Within this table, the best score is 0.820 and the lowest is 0.061. The full system improves slightly on Websites 3 and 4; baseline decreases on Website 3 and increases on the other two. [B]

The full-system changes are 2.2, 2.5, and 0.0 percentage points; baseline changes are −4.2, +4.0, and +3.4 percentage points. These calculations help interpret the authors' less-than-5% language, but they are not estimates of statistical variance. The table supports short-term consistency, with uncertainty about the exact intended definition of variation. [C/D]

### Table 2 — E-commerce comparison

Table 2 has two website rows and three method columns. It compares the baseline, Prompt Only, and Prompt + Tool under product-data Correctness. The full-system entries are bold, consistent with the caption's best-result convention. [A/B: p. 5]

| Website | Baseline | Prompt Only | Prompt + Tool |
|---|---:|---:|---:|
| Momo | 0.000 | 0.040 | 0.242 |
| Amazon | 0.027 | 0.138 | 0.422 |

There are no ties between methods, and every Amazon entry exceeds its corresponding Momo entry. The full system is best in both rows; baseline is worst in both. Momo's baseline is exactly reported as 0.000, rather than an omitted value. No standard deviations, confidence intervals, or significance notation accompany the results. [B]

The table establishes the reported ranking under these two tasks. It does not define near-exact matching or reveal whether scores are item-weighted, run-weighted, or averaged in another way. Consequently the values should remain described as reported Correctness scores rather than converted into exact counts of successfully extracted products. [D]

## 12. Diagram / architecture interpretation

Figure 1 depicts a recurring **observe, reason, act, receive-result** structure. The agent combines its current inputs with returned observations and selects further operations. Computer supplies visual interaction; Bash and Str Editor supply programmatic operations; Parse supplies delegated extraction; Merge supplies consolidation. The output is item-level structured data, rather than only a conversational answer. [A/B: pp. 1–3]

A conceptual task flow consistent with the paper is: receive the target and requested fields; navigate to expose index information; obtain and parse relevant HTML; generate and execute extraction code; collect results across iterations; merge and return JSON. This is **analyst reconstruction of the described components**, not the paper's actual enumerated five-stage prompt. The supplied document does not specify all sequencing rules, retry paths, or intermediate formats. [D]

Two distinct feedback processes matter. Tool results return to the main agent, enabling additional decisions. Separately, the Parse Tool delegates code generation and execution to a reasoning model and interpreter. The diagram collapses that second process into one tool icon; its details come from §3.2 rather than the arrows alone. [A/B]

For the security research question, this distinction identifies several boundaries worth examining: website content into agent observation, raw HTML into delegated model input, generated code into execution, and extracted records into saved output. These are **candidate analytical boundaries**, not experimentally established attack paths. The paper provides no comparison showing that one boundary causes greater vulnerability than a standalone model. [D]

## 13. Equations and mathematical concepts

The paper contains no numbered equations, formal loss function, proof, theorem, or pseudocode algorithm. Its essential mathematical content is the thresholded Correctness rule, confidence-interval half-width, run count, and tabulated proportion-like scores.

**Analyst formalization of the news rule:** for article i, define Uᵢ as its extracted URL, Uᵢ* as the reference URL, Rᵢ,title as title ROUGE-L, and Rᵢ,content as content ROUGE-L. Then Cᵢ = 1 if Uᵢ = Uᵢ* and Rᵢ,title ≥ 0.8 and Rᵢ,content ≥ 0.8; otherwise Cᵢ = 0. This notation is introduced here to explain the author-stated condition; it is not an equation printed in the paper. [C: based on p. 3]

In ordinary language, all three tests must pass. A correct link with an incomplete article fails, and a good article paired with a nonmatching URL also fails. The work does not state the exact aggregation formula that turns individual outcomes into its final plotted average or table score, so no unsupported denominator is assigned.

A CI half-width describes the distance from the center of an interval to one of its bounds. Figure 2 denotes that quantity by ε and the number of runs by n. The supplied work does not give the estimator, interval construction formula, distributional assumption, or precise metric scale underlying ε. Its plotted reduction is therefore interpretable as reduced reported uncertainty, without a reproducible numerical CI calculation. [A/B/D: pp. 3–4]

The text also uses variance informally in describing temporal stability. A change between two reported accuracies is not itself a statistical variance estimate. Because the paper gives no formula for that statement, the report retains the author's wording while separately identifying calculated score changes. [D: p. 4]

## 14. Interpretation and discussion

The authors' central interpretation is that competent interface interaction is insufficient for effective large-scale extraction. The agent also needs a data-oriented strategy: collect related entries, generate reusable parsing logic, and consolidate results. They contrast their system with sequential one-page-at-a-time interaction, which they say inflates context and can fail on index pages with many links. [A: p. 5]

The ablation supports the practical value of both organization and functional tools in this evaluation. However, adding the tools also adds delegated reasoning-model computation and a code interpreter. Consequently the comparison does not isolate tool-interface design from extra model capability, execution facilities, or computation. The paper evaluates the combined system package. [D: p. 3]

Three unresolved consistency issues are substantive. First, GPT-o3 in the method description differs from GPT-o3-mini in the experiment description. Second, nine convergence settings are not reconciled with the six-site, three-method news design. Third, less-than-5% temporal variance is not operationally defined. A fourth interpretive boundary is that product Correctness is stricter than news Correctness but lacks an exact rule. None should be silently repaired. [A/D: pp. 3–4]

The authors' explanation of Momo performance is plausible within their illustrated example, but its causal contribution is not quantified. Likewise, the efficiency argument is supported by an architectural rationale rather than measured runtime, token usage, throughput, or cost. Claims of general applicability are supported by two additional domains' sites, not by exhaustive website coverage. [D: pp. 4–5]

For the user's security question, this paper helps describe **what an agent adds around a language model**: observations from external pages, stateful interaction, multiple tools, script generation, and execution. It does not show that these additions are exploited, nor that removing them produces a safer standalone model. The relevant conclusion is a research lead about architecture, not a security result. [D]

## 15. Contributions and novelty

The **conceptual contribution** is framing index-and-content scraping as a coordinated navigation-and-extraction task. The **methodological contribution** is a specialized guiding prompt combined with delegated parsing and iterative result consolidation. The **system contribution** is the integration of those components with Computer Use. [A: pp. 1–3]

The **implementation contribution** includes Parse and Merge Tools and the repository identified by the source footnote. Only their high-level descriptions were inspected; implementation correctness and exact prompt design remain unverified. The **empirical contribution** is the baseline/prompt-only/full comparison across six news sites, plus the two e-commerce results and preliminary stability analyses. [A: pp. 3–5]

There is no supplied theoretical contribution, formal security contribution, training algorithm, or new-model architecture. Golden datasets are constructed for evaluation, but their sizes, public release, licensing, and detailed annotation procedures are not established. It would overstate the paper to describe it as a fully specified public benchmark release. [D]

Novelty relative to prior literature is presented by the authors, especially their distinction from targeted XPath extraction and sequential browsing. This report does not validate priority or exhaustiveness of that comparison because external literature was not inspected. [A/D: pp. 1–2, 5]

## 16. Limitations

### Authors' stated limitations

The authors identify **complex navigation** as a failure source. Visual grounding can fail, including inaccurate clicks after zooming. They identify **LLM-based code generation** as another source: both their system and baseline may produce buggy scripts when HTML structures are inconsistent. [A: p. 5]

They explicitly limit the framework to the **index-and-content paradigm**. They say it would struggle with real-time WebSocket streaming and advanced virtual scrolling that removes previously visible content from the DOM. Product-page ambiguity, illustrated by multiple price fields on Momo, is also identified as increasing extraction difficulty. [A: pp. 4–5]

### Additional evidence-based analyst observations

The supplied material leaves benchmark item counts, task sampling, crawl dates, gold-data validation, output aggregation, and exact product matching unspecified. The five prompt stages are named only collectively; the actual prompt is absent. Hardware, browser versions, budgets, and retries are not provided. These omissions limit reproducibility, rather than establish that the implementation performed poorly. [D]

The graphs provide incomplete exact numerical reporting. Figure 3 lacks bar labels and uncertainty bars; Figure 2 shows one representative scenario without its exact underlying values. The paper uses strong performance language without supplied between-method statistical testing. Cost and efficiency are discussed but not quantified. [D]

The short temporal test covers three displayed websites and one seven-day interval. Two e-commerce sites provide evidence of transfer but do not establish robustness across all product interfaces. Finally, no adversarial evaluation or standalone-LLM comparison supports conclusions about comparative security vulnerability. [D]

## 17. Threats to validity

The following validity labels are **analyst observations**, not categories expressly adopted by the authors.

**Internal validity:** the full-system improvement is consistent, but the tool intervention bundles delegated reasoning, code execution, and merging. Separate experiments would be needed to isolate which component contributes how much. Site changes and missing task-level details also complicate attribution of temporal differences. [D: pp. 3–4]

**Construct validity:** news Correctness combines link identity and text similarity, while e-commerce uses an incompletely specified near-exact criterion. ROUGE-L thresholding may classify different extraction errors together. The supplied aggregation rule does not establish how omitted articles, duplicates, or extra records affect the final score. [D: pp. 3–4]

**Statistical conclusion validity:** 30 repetitions are justified by convergence behavior, but raw data, interval formulas, per-method uncertainties, and significance tests are absent. A low half-width in one scenario does not show that every comparison has adequate precision. [D: pp. 3–4]

**External validity and generalizability:** the evaluation covers six news sites and two product sites, centered on index-and-content architecture. The results do not directly generalize to streaming, advanced virtualization, authenticated workflows, other agents, or hostile websites. [D: pp. 3–5]

**Ecological validity:** using real websites provides realistic interaction challenges. Clean Firefox starts improve environmental consistency but may differ from persistent user sessions. The paper does not assess logged-in personal workflows or complex long-lived browsing state. [A/D: pp. 3, 5]

**Reproducibility:** the repository pointer is useful, but no repository files were supplied. Unknown model-name reconciliation, incomplete prompt stages, unspecified reference data, and missing software details prevent an independent reconstruction from this document alone. [D]

**Security inference validity:** ordinary navigation mistakes and buggy scripts do not establish attack susceptibility. A comparative vulnerability claim would need adversarial conditions, defined assets and success criteria, and an appropriate standalone-model control. Those are absent here. [D]

## 18. Future work and open questions

### A. Future work explicitly proposed by the authors

First, compile successful interaction trajectories and validated code snippets into a reusable deterministic scraper, with Selenium or Playwright given as examples. The authors envision using the LLM once to construct the scraper, then avoiding repeated model intervention, cost, and stochasticity on later runs. This is a proposal, not a demonstrated result of the reported experiments. [A: p. 5]

Second, extend the agent beyond GUI-level operation to observe DOM changes and network traffic. Monitoring DOM mutations could help with virtual scrolling; examining network requests and protocols such as WebSockets could enable direct access to underlying API endpoints. The authors propose a hybrid of visual interaction and technical understanding of website mechanisms. Its performance and access behavior are not evaluated. [A: p. 5]

### B. Additional open questions logically remaining

What are the actual five stages and retry rules? How are HTML, user requirements, generated code, and returned data validated? How much improvement comes from parsing, merging, delegated model choice, or prompt organization separately? How sensitive are results to the 0.8 threshold and the unknown product tolerance? How accurate and complete are the deterministic Golden crawlers? [D]

What are runtime, token usage, cost, and scalability as link counts grow? How long do generated scripts remain correct after site changes? Can the system distinguish market price reliably when labels are ambiguous? These questions follow from the stated efficiency argument, generalization claims, and observed failures. [D]

For the security project specifically: can external webpage content influence tool decisions beyond the user's intended task? What restrictions apply to generated-code execution and network access? How do website observations and delegated parsing inputs remain data rather than authoritative instructions? These are research questions prompted by the architecture, not vulnerabilities established by this paper. [D; confidence LOW for any prediction of outcomes]

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this work |
|---|---|
| LLM | Large language model used for reasoning or generation |
| MLLM | Multimodal large language model that can process webpage screenshots |
| Web scraping | Collecting website information into structured records |
| Web navigation | Interacting with an interface to reveal or reach information |
| WIE | Web Information Extraction: extracting fields from webpage material |
| Index-and-content | A listing page connected to item-detail pages |
| GUI | Graphical user interface, operated through screen-oriented actions |
| HTML | Hypertext Markup Language: the semi-structured page material parsed by the tool |
| DOM | Document Object Model: the page structure mentioned in the limitations and future work |
| XPath | Expressions used by the cited scraper-generation approaches to locate page elements |
| Observe-Reason-Act | Iterative agent pattern linking observations, reasoning, and actions |
| System prompt | Guidance organizing the agent's behavior |
| Zero-shot baseline | Default agent given the scraping task without the authors' specialized guidance or tools |
| Ablation | A comparison that disables a component to examine its contribution |
| Parse Tool | Delegated HTML-to-structured-data tool using generated Python code |
| Merge Tool | Tool combining result lists and removing duplicates |
| Golden set | Reference URLs, titles, and contents collected by deterministic crawlers |
| ROUGE-L | The named text-similarity metric used for article titles and content; its exact formula is not supplied |
| Correctness | Binary article success rule, or the stricter product-data criterion in the e-commerce evaluation |
| CI | Confidence interval; here its half-width guides repetition count |
| n | Number of experimental runs in Figure 2 |
| ε | Figure 2's CI half-width symbol; exact scale construction is unspecified |
| T, T+7 | Initial test time and seven days later |
| Pagination | Accessing successive batches of listed items |
| Virtual scrolling | Scrolling interface that can unload content from the DOM |
| WebSocket | Protocol named in the discussion of real-time streaming limitations |
| JSON | JavaScript Object Notation, the structured output-file format |
| SOTA | State of the art, used by the authors in discussing other browsing agents |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Accessible document | 7 | physical PDF pages | Supplied extracted text | Visually readable metadata / supplied text | pp. 1–7 |
| Visually inspected pages | 5 | pages | Rendered pages 1–5 | Visually readable | supplied images |
| News sites | 6 | websites | Chinese and English benchmark | Author-reported | p. 3, §4.2 |
| E-commerce sites | 2 | websites | Momo and Amazon | Author-reported | pp. 4–5, §4.5 |
| Compared configurations | 3 | methods | Baseline, prompt-only, full | Author-reported | p. 3, §4.1 |
| Prompt procedure | 5 | stages | Names/details not supplied | Author-reported | pp. 1–2 |
| Temperature | 0 | setting | All experiments | Author-reported | p. 3 |
| News similarity threshold | 0.8 | ROUGE-L score | Both title and content must pass | Author-reported | p. 3, §4.2 |
| Severe-failure observation | below 0.3 | ROUGE-L score | Author-described examples; calibration data absent | Author-reported | p. 3 |
| Confidence level | 95% | confidence | Run-count convergence | Author-reported | pp. 3–4, Fig. 2 |
| Convergence settings | 9 | settings | Relationship to full news design unexplained | Author-reported | p. 3 |
| Selected repetitions | 30 | runs | Standard reported for experiments | Author-reported | p. 4 |
| Temporal interval | 7 | days | T versus T+7 | Author-reported | p. 4, Table 1 |
| LTN pagination successes | 2 of 30 | runs | Baseline navigation anecdote | Author-reported | p. 4, §4.4 |
| Website 3 baseline | 0.103 / 0.061 | accuracy score | T / T+7 | Visually readable | p. 4, Table 1 |
| Website 3 full | 0.511 / 0.533 | accuracy score | T / T+7 | Visually readable | p. 4, Table 1 |
| Website 4 baseline | 0.277 / 0.317 | accuracy score | T / T+7 | Visually readable | p. 4, Table 1 |
| Website 4 full | 0.648 / 0.673 | accuracy score | T / T+7 | Visually readable | p. 4, Table 1 |
| Website 5 baseline | 0.145 / 0.179 | accuracy score | T / T+7 | Visually readable | p. 4, Table 1 |
| Website 5 full | 0.820 / 0.820 | accuracy score | T / T+7 | Visually readable | p. 4, Table 1 |
| Momo baseline / prompt / full | 0.000 / 0.040 / 0.242 | Correctness score | Stricter product criterion | Visually readable | p. 5, Table 2 |
| Amazon baseline / prompt / full | 0.027 / 0.138 / 0.422 | Correctness score | Stricter product criterion | Visually readable | p. 5, Table 2 |
| Momo full gain over baseline | 24.2 | percentage points | (0.242 − 0.000) × 100 | Analyst-derived | p. 5, Table 2 |
| Amazon full gain over baseline | 39.5 | percentage points | (0.422 − 0.027) × 100 | Analyst-derived | p. 5, Table 2 |
| Full-system temporal changes | +2.2 / +2.5 / 0.0 | percentage points | Websites 3 / 4 / 5 | Analyst-derived | p. 4, Table 1 |
| News full-system bars | about 29 / 53 / 56 / 67 / 82 / 51 | percent average correct | Appledaily / BBC / CNN / LTN / PTS / UDN | Approximate visual estimate | p. 4, Fig. 3 |

Table values are preserved without silently replacing them with rounded percentages. Graph estimates are explicitly approximate. The paper reports no hardware measurements, costs, latency, throughput, token counts, p-values, dataset sizes, or security attack rates.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Framework targets index-and-content extraction | Definitions of listing and detail pages | Method | p. 2, §3.1 | HIGH for stated scope |
| Specialized prompt and tools enhance Computer Use | Component descriptions and diagram | Fig. 1 | pp. 2–3 | HIGH for architecture; exact stages absent |
| Parsing delegates script generation and execution | HTML plus requirements sent to reasoning model; Python run in interpreter | Method | p. 3 | HIGH for described design; model names differ |
| Full system ranks above baseline and prompt-only on news | All red bars exceed alternatives | Fig. 3, X3 | p. 4 | HIGH for ranking; exact values and uncertainty absent |
| Functional tools add benefit over prompting alone | Full bars exceed prompt-only bars and product values do likewise | Fig. 3, Table 2 | pp. 4–5 | HIGH for observed pattern; components bundled |
| Thirty runs are a practical choice | Diminishing CI-half-width reduction | Fig. 2, X1 | pp. 3–4 | MEDIUM for broad adequacy; one curve shown |
| Full-system results are stable over sampled seven-day repeat | Small reported score changes | Table 1, X2 | p. 4 | HIGH for values; limited temporal coverage |
| Product-domain ranking persists | Momo 0.242 and Amazon 0.422 exceed alternatives | Table 2, X4 | p. 5 | HIGH for exact results; metric details incomplete |
| Momo ambiguity makes extraction harder | Caption and multiple-field screenshot; lower score | Fig. 4, Table 2 | pp. 4–5 | Author explanation; causal contribution unquantified |
| Navigation and generated code remain failure sources | Explicit error-analysis discussion | Discussion | p. 5 | HIGH for author-stated limitations; frequencies absent |
| Streaming and advanced virtual scrolling are outside robust scope | Explicit architectural limitation | Discussion | p. 5 | HIGH for acknowledged boundary |
| System is relevant to security architecture analysis | Website inputs, computer actions, network/file tools, code execution | Fig. 1 and tool descriptions | pp. 2–3 | MEDIUM analyst inference; no attack experiment |
| Paper does not establish greater vulnerability than standalone LLMs | Evaluation compares Computer Use configurations and task correctness | X1–X4 | pp. 3–5 | HIGH for evaluation scope; comparative security outcome UNKNOWN |

These major findings were checked against their supplied source passages, table rows, and visible figure encodings. The verification preserves conditions: news thresholds are not assigned to products; navigation counts are not treated as extraction accuracy; observed ranking is not converted into demonstrated statistical significance; and architectural security relevance remains analyst inference.

## 22. Very simple explanation — Explain Like I'm 15

Imagine you want a computer to collect many news articles. A website first shows a list of links, and each link leads to the full article. Some lists only reveal more links after you click a button or scroll. A program that only reads the first page's text can miss a lot.

The researchers give an AI agent two kinds of help. One is a plan for how to approach the scraping task. The other is working tools: one turns webpage HTML into structured records using generated code, and another joins results and removes duplicates. The agent can also look at the screen and use the computer to reach the information.

In the tested websites, the plan plus tools works better than the ordinary agent or the plan alone. But better does not mean perfect. On the two shopping sites, the full system reports scores of 0.242 and 0.422 under a strict product-data rule. It can still click incorrectly, generate faulty code, or choose the wrong kind of price when several prices are shown.

For a security project, the useful point is that this AI has more connected parts than a model that only produces text: it reads webpages, takes actions, and runs generated code. Those connections deserve investigation. This paper does not test whether someone can attack those connections, and it does not show that web agents are more vulnerable than standalone language models.

## Completeness Audit

The audit below checks the explanation against the supplied-document inventory. Fully represented means the substantive accessible content is accounted for, not that every source sentence is reproduced or that absent implementation details have been recovered.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| FRONT: title, authors, affiliation, preprint information | Yes, text and image | Yes | Fully represented | §1 |
| ABSTRACT and index terms | Yes, text and image | Yes | Represented in compressed form | Contributions and terminology distributed across §§1, 3, 15, 19 |
| S1: Introduction | Yes, text and image | Yes | Fully represented | Motivation, dynamic-page problem, three contributions |
| S2: Related Work | Yes, text and image | Yes | Represented in compressed form | Categories and key exemplars retained; bibliography details compressed |
| SS3.1: Task definition | Yes, text and image | Yes | Fully represented | Index/content distinction, request fields, JSON output |
| SS3.2: System architecture | Yes, text and image | Yes | Fully represented | Accessible component descriptions; exact stages remain absent |
| Foundational agent subsection | Yes | Yes | Fully represented | Computer Use and inputs |
| Native tools subsection | Yes | Yes | Fully represented | Computer, Bash, Str Editor |
| Parse Tool description and three rationales | Yes | Yes | Fully represented | Delegated generation/execution and rationale distinguished from measurements |
| Merge Tool description | Yes | Yes | Fully represented | Aggregation and deduplication; algorithm unspecified |
| SS4.1: Experimental setting | Yes, text and image | Yes | Fully represented | Three configurations, model identifier, temperature, clean Firefox |
| SS4.2: Benchmark and metrics | Yes, text and image | Yes | Fully represented | Golden sets, threshold conjunction, missing implementation details |
| SS4.3 / X1: Convergence analysis | Yes, text and image | Yes | Fully represented | Nine-setting ambiguity and representative curve disclosed |
| SS4.3 / X2: Temporal stability | Yes, text and image | Yes | Fully represented | All Table 1 values retained |
| SS4.4 / X3: News evaluation | Yes, text and image | Yes | Fully represented | Ranking, pagination anecdote, approximate bars |
| SS4.5 / X4: E-commerce evaluation | Yes, text and image | Yes | Fully represented | All Table 2 values, changed metric, ambiguity explanation |
| Prompt-only ablation | Yes | Yes | Fully represented | Configuration and interpretation limitations |
| S5: Discussion and conclusion | Yes, text and image | Yes | Fully represented | Efficiency argument, failures, scope, future directions |
| ETHICS | Yes; p. 5 visual, p. 6 text-only | Yes | Fully represented | Public access only, request delays, small volume, research-only use |
| S6: References [1]–[17] | Yes, text-only | Yes | Represented in compressed form | Bibliographic categories and relevant cited systems; no citation validation |
| F1: Architecture | Yes, visually | Yes | Fully represented | Components, arrows, feedback, uncertainty boundaries |
| F2: CI convergence | Yes, visually | Yes | Fully represented | Axes, legend, chosen point, trends; exact ordinate uncertain |
| F3: News bars | Yes, visually | Yes | Fully represented | Groups, scale, colors, ranking; values labeled approximate |
| F4: Momo screenshot | Yes, visually | Yes | Represented in compressed form | Relevant ambiguity retained; tiny labels unreadable |
| T1: Temporal table | Yes, visually and textually | Yes | Fully represented | Every numerical cell retained |
| T2: Product table | Yes, visually and textually | Yes | Fully represented | Every numerical cell retained |
| FN1: Repository footnote | Yes | Yes | Fully represented | Artifact existence reported; contents unreviewed |
| O1–O3: Explicit objectives/contributions | Yes | Yes | Fully represented | No fabricated formal research questions |
| Formal hypotheses | Not present | Absence represented | Fully represented | None stated |
| Major equations/theorems | Not present | Absence represented | Fully represented | Explanatory formula explicitly analyst-created |
| Numbered algorithm/pseudocode | Not present | Absence represented | Fully represented | Five-stage prompt details not supplied |
| Author limitations: visual targeting | Yes | Yes | Fully represented | Includes zoom-related clicks |
| Author limitations: buggy generated scripts | Yes | Yes | Fully represented | Inconsistent HTML structures |
| Author limitations: architectural scope | Yes | Yes | Fully represented | Streaming and virtual scrolling |
| Product ambiguity | Yes | Yes | Fully represented | Caption/text-supported; no invented prices |
| Future directions | Yes | Yes | Fully represented | Deterministic compilation and DOM/network observation |
| Appendices | None supplied or identified | Absence represented | Missing from supplied material | No claim that an appendix exists |
| Supplementary files | None supplied | Absence represented | Missing from supplied material | No claim that absent supplements were reviewed |
| Repository code, prompts, raw results | No | Limitation represented | Inaccessible | Reference is supplied, artifact contents are not |
| Visual layout of pp. 6–7 | No | Limitation represented | Inaccessible | Their extracted text was reviewed |

### Missing or inaccessible material

The referenced repository's actual code and prompts were not supplied. The five-stage prompt's detailed contents, generated scripts, Golden datasets, raw run outputs, and statistical routines were not accessible. No separate supplementary files or appendices were supplied. Images of pages 6–7 were absent, although their text was available. This report does not infer that all these artifacts exist separately; it identifies what would be needed to verify the corresponding claims or reproduce the method.

### Uncertain interpretations

The relationship between GPT-o3 and GPT-o3-mini is unresolved. The nine convergence settings are not defined relative to the six-site, three-configuration evaluation. Temporal variance of less than 5% is not given a mathematical definition. Exact Figure 3 means, Figure 2's selected half-width, small Figure 4 price labels, website-number mappings in Table 1, product matching tolerance, and score aggregation are uncertain or unspecified. Security vulnerability outcomes are UNKNOWN because they were not tested.

### Deliberately compressed material

Repeated statements that 30 runs balance precision and cost were consolidated. Repeated descriptions of Momo's ambiguous prices and the full system's superior ranking were consolidated while preserving both tables and the screenshot's evidential role. The full bibliography's author lists, venue details, page ranges, and URLs were not reproduced; references were accounted for by their methodological roles. Tiny product-interface details, decorative tool icons, and shoe imagery were not exhaustively transcribed because they add no reliable methodological or numerical evidence beyond the represented ambiguity illustration.

The ethical conclusion spanning pages 5–6 reports minimal academic-evaluation data volume, negligible traffic impact, research-only use, no redistribution, and no commercial use. These are author commitments and characterizations; no traffic measurements or compliance verification were supplied.

### Potential omissions

No known substantive component of the supplied inventory is left unaccounted for. Some are represented in compressed form, and unavailable implementation details remain explicitly unresolved. This is a coverage conclusion about the seven supplied text pages and five rendered images, not a declaration that the implementation, bibliography, security properties, or all possible author artifacts were independently verified.
