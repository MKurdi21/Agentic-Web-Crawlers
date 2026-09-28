# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible range | All 19 pages, proceedings pp. 2371–2389 |
| Apparently missing pages | None |
| Native text | Available for every page; no page was classified as scanned or low-text |
| Visually rendered pages inspected | Document pages 1–8, 12–16, 18–19 |
| Pages not visually rendered | Pages 9–11 and 17; these were inspected through supplied native text only |
| Figures available visually | Yes. Figures 1–4 were rendered and inspected |
| Tables | Tables 1–15 and 18 were rendered; Tables 16–17 were also rendered on p. 18. All 18 tables are readable, although dense tables required reliance on the supplied native text as well as the images |
| Equations | Equations (1)–(6) are readable in the supplied text; Equations (1)–(2) and (3)–(6) also appear on rendered pages |
| Algorithm | Algorithm 1 is readable on rendered p. 12 |
| Appendices | Appendices A–D are present on pp. 12–19 |
| Supplementary material | No separate supplementary file was supplied |
| Referenced external artifact | The paper identifies an open-source GitHub repository, but its contents were not supplied or inspected |
| OCR required | No. Native extraction was available. OCR-sensitive XPath punctuation, subscripts, quotation marks, and mathematical typesetting were cross-checked against rendered pages where possible |
| Important limitations | Hardware details are mostly absent beyond naming the Fudan University CFFF platform. Software versions, decoding parameters, random seeds, exact model snapshots, API settings, costs, and complete repetition details are not supplied. References on pp. 10–11 were not visually rendered, but their text is accessible. |

Evidence labels used below:

- **[A] Author-reported:** explicitly stated in the paper.
- **[B] Directly observable:** visible in a supplied page image.
- **[C] Analyst-derived:** calculated directly from reported quantities.
- **[D] Analyst interpretation:** a clearly marked inference.
- No external information is introduced.

# 1. Plain-Language Orientation

AUTOSCRAPER is a method for asking a large language model (LLM) to write a reusable web scraper rather than repeatedly asking the LLM to read every page itself.

A conventional rule-based scraper is efficient once written but often requires human rewriting when a site changes. An LLM can adapt to unfamiliar pages, but repeatedly sending whole pages to a powerful model is slow and potentially expensive. The authors try to combine the advantages of both approaches: use an LLM to generate a reusable sequence of XPath operations, then run that sequence with an ordinary parser on many pages.

The central difficulty is that HyperText Markup Language (HTML) is long and hierarchical. A model must identify both the desired value and a structural path that continues to work on other pages. AUTOSCRAPER addresses this in two phases:

1. **Progressive generation:** the model alternates between moving downward toward the target and stepping back to a broader HTML subtree when a proposed XPath does not work.
2. **Synthesis:** scrapers generated from several seed pages are tested across those pages, and one candidate is selected for reuse.

The authors also introduce an **executability evaluation**. Rather than scoring only the text returned by a scraper, it asks whether one generated scraper succeeds across the collection of pages constituting a website-level task.

The principal reported result is that AUTOSCRAPER generally produces more fully correct and fewer unexecutable scrapers than Chain-of-Thought (COT) and Reflexion baselines across eight LLMs and three datasets. The strongest reported configuration, GPT-4-Turbo plus AUTOSCRAPER, reaches:

- **71.56% Correct, 4.06% Unexecutable, and 88.69 F1** on SWDE;
- **64.11% Correct, 15.33% Unexecutable, and 76.21 F1** on Extended SWDE;
- **57.83% Correct, 16.87% Unexecutable, and 75.52 F1** on DS1.

These are author-reported values from Table 2 (p. 6).

# 2. Document Roadmap

The paper is an empirical machine-learning/AI and algorithmic systems study.

| Part | Content and role |
|---|---|
| Abstract and §1, pp. 1–2 | Introduce the scalability problem, three technical challenges, AUTOSCRAPER, and the executability metric |
| §2, pp. 2–3 | Position the work against wrapper induction, neural web extraction, and LLM-based web agents |
| §3, pp. 3–4 | Define scraper generation, describe SWDE, Extended SWDE, and DS1, and introduce executable evaluation |
| §4, p. 5 | Specify action-sequence modeling, progressive generation, and synthesis |
| §5, pp. 5–7 | Give experimental settings, principal results, ablation, and seed-page analysis |
| §6, pp. 7–9 | Compare direct LLM extraction and supervised systems; analyze efficiency and errors |
| §7 and statements, p. 9 | Conclude; report limitations, ethics, annotation use, and risks |
| References, pp. 9–11 | Bibliography; compressed here because it is contextual rather than experimental evidence |
| Appendix A, pp. 12–14 | Extended SWDE and DS1 results plus a golden-label experiment |
| Appendix B, pp. 12–16 | Compare COT/Reflexion, study action-sequence length, and analyze XPath fragility |
| Appendix C, pp. 13, 16, 18 | Detailed dataset statistics |
| Appendix D, pp. 14–19 | Task and module prompts |

# 3. Background and Context

A **web scraper** is a program that retrieves specified information from web pages. A **wrapper** is a site-specific extraction rule or parser.

HTML represents a page as a **Document Object Model (DOM) tree**. Elements are nodes; nesting establishes parent–child relationships. **XPath** is the rule language used here to select nodes or text in that tree.

Two prior paradigms frame the paper (§1–§2):

- **Wrapper-based extraction:** humans or learned systems construct rules tied to page structure. The rules can be efficient and reusable on stable layouts but may require annotation, heuristics, engineered features, or site-specific redesign.
- **Language-agent extraction:** an LLM reads a page and responds to an instruction. It is adaptable but must repeatedly process pages and, according to the authors, does not adequately reuse structural similarities across a site.

The paper evaluates two LLM-agent baselines:

- **Chain-of-Thought (COT):** here, a one-turn prompted generation baseline.
- **Reflexion:** an iterative baseline that reflects after a failed XPath and regenerates it.

AUTOSCRAPER differs by changing the HTML context during repair: it prunes the DOM through top-down and step-back operations (§4.2; Appendix B.1).

A **seed webpage** is one of the small number of pages used to generate and select the reusable action sequence. In the main settings, the authors use three seed pages for SWDE and Extended SWDE and one for DS1 (§5.1, p. 6).

# 4. Research Problem and Gap

## Existing problem

Producing reliable scrapers for many sites requires substantial human work, while invoking an LLM independently on every page creates repeated model-processing overhead (§1, pp. 1–2).

## Shortcomings attributed to previous approaches

- Wrapper methods do not automatically scale well to new structures and may require annotations, handcrafted rules, features, or prior knowledge (§1–§2).
- LLM agents adapt to content but are time- and financially demanding when used repeatedly (§1).
- Existing agents do not sufficiently exploit site-level structural similarity or simplify the HTML after failed attempts (§2).
- Ordinary precision, recall, and F1 assess extracted items but can conceal empty or unexecutable outputs (§3.3 and §5.2).

## Research gap

The authors identify a missing middle ground: an LLM-driven method that generates an executable, reusable scraper by reasoning about HTML hierarchy and validating the rule over multiple same-site pages.

## Motivation

A reusable generated scraper incurs LLM effort during rule construction but subsequently extracts pages using a parser. That could offer adaptability during generation and efficiency during repeated use.

## Scope

The evaluated task is semi-structured information extraction from “vertical” detail pages: pages on one site describing the same type of entity, such as books, automobiles, or universities. It is not evaluated as a general browsing or transaction agent (§9, Limitation).

# 5. Research Questions / Objectives / Hypotheses

## Explicit research questions

The authors state three questions in §5 (p. 5):

- **RQ1:** Can AUTOSCRAPER outperform state-of-the-art scraper-generation methods?
- **RQ2:** How does the AUTOSCRAPER framework improve scraper-generation performance?
- **RQ3:** Does AUTOSCRAPER meet web-scraping requirements, specifically accuracy and efficiency?

## Objectives

- Formulate LLM-based web-scraper generation as action-sequence generation.
- Use HTML hierarchy to make long pages more manageable.
- improve cross-page reusability through synthesis.
- Evaluate scraper reliability at the website/case level.
- Compare against COT, Reflexion, direct extraction, and supervised web-extraction systems.

## Hypotheses

No separately labeled formal hypotheses, null hypotheses, confidence thresholds, or significance tests are supplied. The design nevertheless tests the authors’ expectations that progressive generation and multi-page synthesis improve correctness, executability, and reuse.

# 6. Assumptions / Threat Model

This is not a security study and supplies no attacker–defender threat model.

The operational assumptions are:

- Pages within a case belong to the same website and describe the same kind of entity (§3.1).
- A predefined target attribute and natural-language extraction instruction are available.
- Same-site pages possess enough structural similarity for one action sequence to generalize.
- The desired value is represented in the supplied HTML after preprocessing.
- A parser can execute generated XPath expressions.
- The LLM can propose an expected value and an XPath and judge whether parser output matches that value.
- The allowed retry limit is finite: \(d_{\max}=5\) in the experiments (§5.1).
- Synthesis can judge candidate generalizability from their results on seed pages.
- For the efficiency analysis, per-page costs are treated by the additive time model in Equations (3)–(6).

Excluded or unsupported cases include general open-world web interaction, arbitrary site actions, and environments such as Mind2Web and WebArena (§9, Limitation).

# 7. Methodology

## 7.1 Task definition

Given pages \(w\in W\) from one website, a subject entity \(s\), and target attribute \(r\in R\), the goal is to create an executable action sequence \(A\) extracting target information \(o\) from all pages (§3.1, p. 3).

The paper models the scraper as:

\[
A_{\mathrm{seq}}=[XPath_1,XPath_2,\ldots,XPath_n].
\]

All but the last XPath prune or change the active subtree; the final XPath extracts the target value (§4.1, Eq. 2).

## 7.2 Progressive generation

For each step (§4.2; Algorithm 1):

1. Give the current HTML subtree and task instruction to the LLM.
2. Ask it for an expected value and XPath.
3. Execute the XPath with a parser.
4. If parser output equals the model-recognized value, stop.
5. Otherwise, repeatedly append `/..` to move upward from the failed selection.
6. Select an ancestor subtree containing the expected value.
7. append the XPath to the sequence and repeat on that smaller context.

The intended effect is to remove irrelevant parts of a long DOM while retaining enough context to find a more reliable selector.

## 7.3 Synthesis

For a case (§4.3):

1. Randomly choose \(n_s\) seed pages.
2. Generate one action sequence from each.
3. Execute every candidate on the seed pages.
4. provide candidate sequences and their results to a synthesis prompt.
5. select a sequence expected to extract all target information across the pages.

The output is one site/task-specific reusable action sequence.

## 7.4 Datasets and samples

### SWDE

The source Structured Web Data Extraction dataset has 124,291 pages from 80 websites in eight domains, with 3–5 attributes per domain/site description (§3.2). The transformed benchmark contains:

- 320 cases;
- 32 extraction tasks;
- 32,000 sampled pages.

Each selected site contributes 100 sampled pages per applicable task (Table 1, p. 3).

### Extended SWDE

The source data contains 21 sites in three domains. The paper says SWDE averages 4,480 triples for three predicates per site, whereas Extended SWDE averages 41,000 triples for 36 predicates (§3.2).

For evaluation, relations are mapped to predefined attributes and unusual relations removed. The transformed benchmark contains:

- 294 cases/attributes;
- 221 tasks;
- 29,400 pages (Table 1);
- 21 selected websites (Appendix A.1).

### DS1

DS1 contains 166 annotated pages from 30 sites in four domains: books, e-commerce/shopping, hotels, and movies. Each website has two pages; one is used for inference and the other for evaluation. The transformed count is:

- 83 cases;
- 11 tasks;
- 186 pages in Table 1.

There is a source inconsistency here: §3.2 and Appendix A.2 say DS1 contains **166** pages, while Table 1 reports **186** transformed webpages. The supplied work does not reconcile the difference.

## 7.5 Preprocessing

The authors:

- construct domain and attribute instructions;
- sample 100 pages per selected website for SWDE-style cases;
- remove `<script>` and `<style>` nodes;
- remove all element attributes except `class`;
- replace annotation escape characters to align with page content (§3.2).

No data-leakage analysis beyond the site/page organization is reported.

## 7.6 Models and baselines

Eight LLMs are tested (§5.1):

- Closed-source: GPT-3.5-Turbo, Gemini Pro, GPT-4-o-mini, GPT-4-Turbo.
- Open-source: Phi-3-medium, CodeLlama-34B, Mixtral 8×7B, Deepseek-Coder-33B.

Generation frameworks:

- COT;
- Reflexion;
- AUTOSCRAPER.

Additional comparisons use:

- direct LLM extraction;
- five supervised methods: Render-Full, FreeDOM, SimpDOM, MarkupLMBASE, and WebFormer.

## 7.7 Experimental parameters and implementation details

Reported parameters:

- \(n_s=3\) for SWDE and Extended SWDE;
- \(n_s=1\) for DS1;
- \(d_{\max}=5\);
- zero-shot prompting throughout because of limited LLM context (§5.1);
- efficiency measurements repeated three times for AUTOSCRAPER, with direct-extraction time averaged over ten pages (§6.3).

Reported infrastructure:

- computations used the CFFF platform of Fudan University (Acknowledgement, p. 9).

Not reported:

- hardware specifications;
- software/library versions, aside from naming BeautifulSoup;
- API/model snapshot identifiers;
- temperature, top-p, token budgets, or decoding policy;
- random seed;
- prompt-order controls;
- monetary cost;
- confidence intervals or statistical significance tests.

## 7.8 Evaluation metrics

For each site/task case, executable outcomes are mutually exclusive (§3.3):

- **Correct:** precision = recall = F1 = 1.
- **Prec.:** only precision = 1; extracted items are correct but incomplete.
- **Reca.:** only recall = 1; all relevant items found plus irrelevant items.
- **Unexecutable:** recall = 0.
- **Over-estimate:** precision = 0 when the ground truth is empty but the scraper extracts something.
- **Else:** remaining partial or mixed cases.

The ratio for situation \(R\) is:

\[
M_R=\frac{\#\text{cases in situation}}{\#\text{total cases}}.
\]

Higher Correct and lower Unexecutable are preferred. Conventional precision, recall, and macro-F1 are also averaged over cases.

# 8. Experiments / Analyses

## X1 — Main comparison across three datasets

**Purpose:** answer RQ1 and establish broad effectiveness.

**Setup:** eight LLMs × COT, Reflexion, or AUTOSCRAPER; SWDE, Extended SWDE, and DS1; zero-shot; Table 2.

**Results:** AUTOSCRAPER usually increases Correct and reduces Unexecutable relative to the same model’s baselines. Examples on SWDE:

- GPT-3.5-Turbo: Correct 54.84 versus 46.29 Reflexion; Unexecutable 19.35 versus 37.10.
- GPT-4-o-mini: Correct 62.06 versus 54.66 COT and 53.70 Reflexion.
- GPT-4-Turbo: Correct 71.56 versus 67.50 Reflexion; Unexecutable 4.06 versus 10.94.
- Mixtral 8×7B: Correct 46.88 versus 36.25 Reflexion.

**Caveat:** “outperforms” depends on metric. Some conventional precision values decrease because executable evaluation penalizes failure modes differently.

## X2 — Component ablation

**Purpose:** answer RQ2 by separating progressive generation from synthesis.

**Setup:** SWDE; GPT-3.5-Turbo, Gemini Pro, and GPT-4-Turbo; synthesis removed from COT, Reflexion, and AUTOSCRAPER variants; Table 3.

Key full-versus-no-synthesis changes:

- GPT-3.5 AUTOSCRAPER: Correct 54.84 vs 44.52; Unexecutable 19.35 vs 29.33; F1 69.20 vs 58.44.
- GPT-4-Turbo AUTOSCRAPER: Correct 71.56 vs 65.31; Unexecutable 4.06 vs 11.87; F1 88.69 vs 80.41.
- Gemini AUTOSCRAPER: Correct 42.81 vs 39.46. However, the no-synthesis row has lower Unexecutable, 31.56 vs 34.38, and higher F1, 56.48 vs 54.91.

Thus synthesis generally helps but not every displayed metric/model combination. That qualification is visible in Table 3 but is understated by the prose.

## X3 — Number of seed pages

**Purpose:** test whether additional cross-page evidence improves generalization.

**Setup:** AUTOSCRAPER on SWDE with 1–5 seed pages; GPT-4-Turbo and GPT-3.5-Turbo; Figure 3.

**Result:** Correct rises and Unexecutable falls as seeds increase, with diminishing improvements. Exact values are not labeled in the plot, so point-by-point values can only be approximated visually.

## X4 — Direct LLM extraction

**Purpose:** assess the accuracy tradeoff between reusable scrapers and direct page reading.

**Setup:** each of eight LLMs, zero-shot; SWDE; F1; Table 4.

**Result:** direct extraction beats AUTOSCRAPER for seven of eight models. GPT-4-Turbo is the exception: AUTOSCRAPER 88.69 versus direct extraction 78.56. The authors interpret narrowing gaps for stronger models as evidence that HTML-structure understanding is the key bottleneck.

## X5 — Supervised baselines

**Purpose:** compare zero-shot AUTOSCRAPER with established trained extractors.

**Setup:** SWDE F1; five supervised systems trained on one seed site, Reflexion + GPT-4-Turbo, and AUTOSCRAPER + GPT-4-Turbo; Table 5.

**Result:** AUTOSCRAPER reaches 88.69, above WebFormer’s 86.58, the best displayed supervised baseline.

**Caveat:** the authors explicitly call the comparison “unfair” because the learning conditions differ. It is evidence of competitive F1, not a fully controlled training-regime comparison.

## X6 — Efficiency/break-even analysis

**Purpose:** answer the efficiency part of RQ3.

**Setup:** GPT-4-Turbo; one randomly selected website in each domain, although the table lists eight domains rather than the “10 domains” claimed in the prose; AUTOSCRAPER repeated three times; Table 6 and Equations (3)–(6).

**Result:** average reported break-even page count is 19.5. Per-page wrapper execution is 0.21–0.54 seconds, versus direct extraction at 6.59–14.26 seconds, but generation plus synthesis costs 107.1–238.4 seconds.

**Interpretation:** wrapper generation is slower for a few pages but can amortize over a sufficiently large same-site collection.

## X7 — Error analysis

**Purpose:** identify remaining failures.

Two reported modes (§6.4):

- **Cross-page non-generalizability:** e.g., a CareerBuilder page stores “Not Available” at a different DOM node.
- **Multi-valued targets:** addresses or phone numbers may occur in several locations, and one sequence may retrieve only some of them.

No failure frequencies are reported.

## X8 — Extended SWDE detailed analysis

**Purpose:** assess more numerous and ambiguous relations.

**Setup:** 294 attributes from 21 sites; Table 7.

**Result:** closed-source models generally generate more executable sequences than open-source models. Ambiguous task labels such as “Calendar System” and “Facilities and Programs Offered” degrade every approach.

The best displayed F1 is GPT-4-Turbo AUTOSCRAPER at 76.21. Its Correct value, 64.11, is slightly below GPT-4-Turbo Reflexion’s 64.81, but its Unexecutable value is lower: 15.33 versus 19.51.

## X9 — DS1 detailed analysis

**Purpose:** test transfer when each site has only two pages.

**Setup:** one page for inference, one for evaluation; no synthesis; Table 8.

**Result:** GPT-4-Turbo AUTOSCRAPER is best overall at Correct 57.83, Unexecutable 16.87, and F1 75.52. AUTOSCRAPER improves Correct over both baselines for every listed model.

## X10 — Golden-label experiment

**Purpose:** separate recognizing the target value from constructing a valid structural path.

**Setup:** SWDE; models receive the same extraction targets; Table 9.

**Result:** progressive generation still improves most configurations. GPT-4-Turbo AUTOSCRAPER reaches Correct 75.31 and Unexecutable 4.06. Open-source models remain substantially weaker, which the authors attribute to hierarchical-structure understanding rather than target-content recognition.

## X11 — Action-sequence length

**Purpose:** use the number of steps as an indicator of structural understanding.

**Setup:** distributions of sequences of length 1–5 on SWDE, DS1, and Extended SWDE; Tables 10–12.

Examples:

- SWDE: GPT-4-Turbo averages 1.57 steps; Phi-3-medium averages 3.62.
- DS1: Deepseek-Coder averages 2.11; Phi-3-medium 3.61.
- Extended SWDE: CodeLlama averages 2.06 and Deepseek-Coder 2.14, while GPT-4-Turbo averages 3.15.

The authors’ broad claim that “stronger LLMs generate fewer” steps is supported clearly on SWDE but not monotonically across Extended SWDE, where two open-source code models have the lowest averages.

## X12 — XPath fragility

**Purpose:** examine whether selectors depend on page-specific literal text.

**Setup:** manual bad-case proportions for `contains` and equality predicates; Tables 13–14.

**Result:** GPT4 has the lowest shown rates, 0.61% for `contains` and 2.90% for equality. The table still indicates nonzero fragility for the strongest model.

# 9. Results

## RQ1: Comparative scraper-generation performance

[A] The authors’ central claim is broadly supported by Table 2: AUTOSCRAPER produces the best same-model Correct result in all displayed SWDE rows, all displayed DS1 rows, and most Extended SWDE rows.

Important qualifications:

- Extended SWDE GPT-4-Turbo Reflexion has Correct 64.81 versus AUTOSCRAPER 64.11, although AUTOSCRAPER has better Unexecutable and F1.
- Extended SWDE CodeLlama Reflexion has Correct 13.73 versus AUTOSCRAPER 11.16.
- Extended SWDE Deepseek-Coder COT has Correct 38.33 versus AUTOSCRAPER 37.63.
- Therefore, the literal statement that AUTOSCRAPER beats every alternative on every metric is too strong; its advantage is most consistent when Correct, Unexecutable, and F1 are considered jointly.

[C] On SWDE, GPT-4-Turbo AUTOSCRAPER improves Correct over GPT-4-Turbo Reflexion by **4.06 percentage points**: \(71.56-67.50\). It reduces Unexecutable by **6.88 percentage points**: \(10.94-4.06\).

[C] On DS1, GPT-4-Turbo AUTOSCRAPER improves F1 over Reflexion by **12.02 points**: \(75.52-63.50\).

## RQ2: How the framework helps

The evidence supports two mechanisms:

- **Progressive structural pruning:** AUTOSCRAPER without synthesis still often beats COT and Reflexion (Table 3).
- **Cross-page synthesis:** full AUTOSCRAPER usually improves Correct, Unexecutable, and F1 relative to its no-synthesis version (Table 3), and more seeds improve the plotted trends (Figure 3).

The Gemini exception in Table 3 prevents treating synthesis as universally beneficial on every metric.

## RQ3: Accuracy and efficiency

Accuracy is strongest with GPT-4-Turbo:

- SWDE F1 88.69;
- Extended SWDE F1 76.21;
- DS1 F1 75.52.

Efficiency is conditional on reuse. Table 6 shows very low parser-execution times after rule generation, but a substantial up-front generation cost. The reported average break-even point is 19.5 pages.

## Metric-design result

Traditional precision may remain high even for systems with many unexecutable cases. For example, on SWDE, Phi-3-medium COT reports conventional precision 94.38 but Correct only 12.50 and Unexecutable 80.00 (Table 2). This directly illustrates why the proposed case-level categories reveal failures obscured by precision alone.

# 10. Figure-by-Figure Interpretation

## Figure 1 — Comparison of scraping paradigms

- **Location:** p. 1.
- **Type:** conceptual comparison diagram; no quantitative axes.
- **Content:** wrapper-based extraction, language-agent extraction, and AUTOSCRAPER.
- **Flow:** wrappers associate page-specific structure with prewritten extraction logic; language agents answer requests per page; AUTOSCRAPER uses an LLM to generate a reusable wrapper-like procedure.
- **Visual encoding:** orange and yellow bands distinguish conventional paradigms; green emphasizes AUTOSCRAPER.
- **Claim supported:** AUTOSCRAPER is intended to combine wrapper reuse with LLM adaptability.
- **Caveat:** labels such as “highly reusable with great performance” and “heavy time & financial consuming” are conceptual claims, not measured results in this figure.

## Figure 2 — Two-phase AUTOSCRAPER architecture

- **Location:** p. 4.
- **Panels:** (a) progressive generation; (b) synthesis.
- **Input:** a task instruction, full HTML, and several seed pages.
- **Progressive path:** an initial XPath retrieves the wrong value; a step-back operation expands context; a subsequent top-down XPath reaches the desired value.
- **Synthesis path:** candidate action sequences are run on multiple pages, results are compared, and one final sequence is chosen.
- **Outputs:** a final action sequence intended to generalize within the website.
- **Visual details:** the basketball-stat example distinguishes labels such as PPG, APG, and RPG and shows why selecting a nearby number without sufficient structural context is unsafe.
- **Claim supported:** generation is interactive and hierarchical, while synthesis is cross-page.
- **Uncertainty:** the small illustrative numeric values are examples within the diagram, not evaluation results.

## Figure 3 — Effect of seed-page count

- **Location:** p. 7.
- **Plot:** line chart.
- **x-axis:** number of seed websites/pages, 1–5. The caption says “seed websites,” while surrounding prose says “seed webpages.”
- **y-axis:** executable metric, 0–100%.
- **Series:** Correct and Unexecutable for GPT-4-Turbo and GPT-3.5-Turbo.
- **Trend:** Correct increases and Unexecutable decreases; changes flatten by roughly four to five seeds.
- **Approximate visual estimates:** GPT-4-Turbo Correct appears to rise from roughly the mid-60s to mid-70s; its Unexecutable rate declines from roughly low teens to around 4%. GPT-3.5 Correct rises from the high-30s to mid-50s, while Unexecutable declines from around 30% to the mid-teens.
- **Status:** these are approximate visual estimates, not labeled exact values.
- **Caveat:** no error bars or run-to-run variation are shown.

## Figure 4 — COT, Reflexion, and AUTOSCRAPER behavior

- **Location:** p. 15; discussed in Appendix B.1.
- **Type:** qualitative execution trace.
- **Task:** retrieve James Harden’s average points.
- **COT:** makes a one-turn incorrect selection.
- **Reflexion:** retries after failure but does not structurally simplify the page.
- **AUTOSCRAPER:** steps back to a broader context and then generates a corrected selector.
- **Claim supported:** AUTOSCRAPER’s repair changes the active DOM context, unlike pure regeneration.
- **Caveat:** this is one illustrative case, not frequency evidence.

# 11. Table-by-Table Interpretation

## Table 1 — Benchmark sizes

Reports cases, tasks, and transformed webpage counts:

- SWDE: 320 / 32 / 32,000.
- Extended SWDE: 294 / 221 / 29,400.
- DS1: 83 / 11 / 186.

The DS1 value conflicts with the prose’s 166 pages.

## Table 2 — Main results

The principal comparison table spans all eight models and three datasets. SWDE contains the full six-category executable breakdown and conventional precision/recall/F1; Extended SWDE and DS1 show Correct, Unexecutable, and F1 in this condensed table.

GPT-4-Turbo AUTOSCRAPER has the strongest displayed aggregate results. Small/open-source models generally have much higher Unexecutable rates.

No confidence intervals or significance markers are provided; bold denotes best displayed values, not statistical significance.

## Table 3 — Synthesis ablation

Compares full methods with “− synthesis” on SWDE. It demonstrates that multi-page synthesis generally helps, but Gemini AUTOSCRAPER has the previously noted mixed result. The table also shows that removing synthesis from COT or Reflexion can seriously worsen them, suggesting synthesis is a reusable module rather than an exclusively AUTOSCRAPER-specific idea.

## Table 4 — Direct extraction versus AUTOSCRAPER

Reports F1 for eight models. Only GPT-4-Turbo performs better with AUTOSCRAPER:

- Direct: 78.56.
- AUTOSCRAPER: 88.69.

The largest displayed gap favoring direct extraction is Phi-3-medium: 71.73 versus 34.93.

## Table 5 — Supervised baselines

F1 values:

- Render-Full 84.30;
- FreeDOM 82.32;
- SimpDOM 83.06;
- MarkupLMBASE 84.31;
- WebFormer 86.58;
- Reflexion + GPT-4-Turbo 82.40;
- AUTOSCRAPER + GPT-4-Turbo 88.69.

[C] AUTOSCRAPER exceeds WebFormer by **2.11 F1 points**, \(88.69-86.58\).

## Table 6 — Timing

| Domain | Direct/page \(T_d\) | Generation+synthesis | Wrapper/page \(T_e\) | Reported \(N_W\) |
|---|---:|---:|---:|---:|
| Auto | 8.27 s | 238.4 s | 0.30 s | 30 |
| Book | 10.20 s | 176.4 s | 0.51 s | 18 |
| Camera | 6.59 s | 107.1 s | 0.31 s | 18 |
| Job | 7.42 s | 123.5 s | 0.21 s | 18 |
| Movie | 7.47 s | 133.2 s | 0.21 s | 19 |
| NBAPlayer | 8.32 s | 179.4 s | 0.45 s | 23 |
| Restaurant | 8.87 s | 160.8 s | 0.54 s | 20 |
| University | 14.26 s | 134.7 s | 0.32 s | 10 |

The final column is the integer break-even count obtained from Equation (6), apparently rounded upward. Its arithmetic mean is 19.5, matching the prose.

## Table 7 — Extended SWDE detail

Gives all six executable categories plus precision, recall, and F1. It confirms strong GPT-4-class performance but also exceptions to universal Correct superiority. Extended tasks produce substantial Unexecutable rates even for strong models.

## Table 8 — DS1 detail

Reports the full breakdown. GPT-4-Turbo AUTOSCRAPER leads on Correct, Unexecutable, and F1. Because \(n_s=1\), these results test progressive generation without synthesis.

## Table 9 — Golden-label evaluation

Supplying target values improves several configurations, but structural failures persist. GPT-4-Turbo AUTOSCRAPER is best displayed at Correct 75.31 and Unexecutable 4.06. Deepseek-Coder Reflexion slightly exceeds AUTOSCRAPER on Correct, 38.75 versus 38.44, while AUTOSCRAPER lowers Unexecutable to 31.56 from 42.19.

## Tables 10–12 — Sequence-length distributions

Columns 1–5 count generated sequences of each length, plus the mean.

- Table 10: SWDE.
- Table 11: DS1.
- Table 12: Extended SWDE.

The distributions show that mean length depends on model and dataset. They do not establish a universal ordering by presumed model strength.

## Table 13 — Text-predicate fragility

Reports manually determined bad-case rates for `contains` and exact equality predicates. GPT4 has the lowest rates. Mistral 7B appears here even though it is not one of the eight main experimental models; the paper does not explain this substitution or addition.

## Table 14 — Good and bad XPath examples

The good selector uses stable semantic text, `Height:`, combined with a class and sibling relationship. The bad selector embeds the literal seed-page phone number `703-528-7809`, making it page-specific. Green and red highlighting distinguish general from seed-specific predicates.

## Table 15 — Detailed SWDE statistics

Lists eight domains, their attributes, sites, and per-site page counts. Most sites have 2,000 pages, but several have fewer—for example, camera sites range from 220 to 1,767 and some university/NBA sites have roughly 400–1,063 pages. This table describes the source dataset, whereas Table 1 describes the transformed experimental sample.

## Table 16 — Extended SWDE statistics

Lists 21 sites in Movie, NBAPlayer, and University domains, with 5–34 attributes per site. These counts explain the dataset’s more fine-grained task inventory.

## Table 17 — DS1 statistics

Lists Book, E-commerce, Hotel, and Movie domains; each has seven or eight named sites and three attributes. It does not include per-site page counts.

## Table 18 — SWDE task prompts

Lists domain-level context sentences and attribute requests for all 32 SWDE tasks. These range from auto model/price/engine/fuel efficiency to university name/phone/URL/type. It documents task construction rather than results.

# 12. Diagram / Architecture Interpretation

AUTOSCRAPER has two connected control loops.

```text
Instruction + seed HTML
          |
          v
  LLM proposes value + XPath
          |
          v
    Parser executes XPath
       /          \
   matches       fails
     |              |
 candidate      move XPath upward
 sequence       to containing subtree
     |              |
     +------ repeat-+
          |
          v
Repeat on several seed pages
          |
          v
Execute all candidates across seeds
          |
          v
LLM synthesis selects one sequence
          |
          v
Reusable site/task scraper
```

The **data path** carries HTML, proposed XPath expressions, parser results, and reduced HTML subtrees. The **control path** decides whether extraction matches the expected value, whether to step back, whether to retry, and which candidate to retain.

The final scraper remains an ordered sequence rather than a single XPath because intermediate XPaths prune the page before the terminal extraction step.

# 13. Equations and Mathematical Concepts

## Equation (1) — Executable-result ratio

\[
M_R=\frac{\#\text{cases classified as }R}
          {\#\text{total cases}}.
\]

- \(R\): one mutually exclusive result category.
- \(M_R\): percentage or proportion of cases in that category.
- Purpose: measure website/task-level scraper outcomes.
- Higher is desirable only for Correct; lower is desirable for Unexecutable.

## Equation (2) — Action sequence

\[
A_{\mathrm{seq}}=[XPath_1,\ldots,XPath_n].
\]

- \(A_{\mathrm{seq}}\): generated scraper.
- \(n\): number of steps.
- First \(n-1\) paths prune/change context.
- Final path extracts the value.

## Equation (3) — AUTOSCRAPER total time

\[
T_1=T_G+T_E=(n_sT_g+T_s)+N_WT_e.
\]

- \(n_s\): seed-page count.
- \(T_g\): time to generate a wrapper/action sequence for one seed.
- \(T_s\): synthesis time.
- \(N_W\): number of pages to extract.
- \(T_e\): parser extraction time per page.
- \(T_G=n_sT_g+T_s\): up-front generation cost.
- \(T_E=N_WT_e\): repeated execution cost.

## Equation (4) — Direct-extraction total time

\[
T_2=N_WT_d,
\]

where \(T_d\) is LLM direct-extraction time per page.

## Equation (5) — Break-even condition

\[
(n_sT_g+T_s)+N_WT_e \leq N_WT_d.
\]

AUTOSCRAPER is faster overall when its up-front cost plus parser executions do not exceed repeated direct LLM calls.

## Equation (6) — Break-even page count

\[
N_W\geq\frac{n_sT_g+T_s}{T_d-T_e}.
\]

This assumes \(T_d>T_e\). The paper does not state that condition explicitly, although it holds for every row in Table 6.

## Algorithm 1 — Progressive understanding

Inputs are original HTML \(h_0\), instruction \(I\), and retry limit \(d_{\max}\); output is \(A_{\mathrm{seq}}\). The LLM generator \(LLM_g\) returns a value and XPath, `Parser_text` executes extraction, and `Parser_node` returns an ancestor subtree.

A notation ambiguity exists at line 10: the algorithm text says “until \(h\) contains value,” whereas the evolving subtree is indexed as \(h_{k+1}\). The intended reference is inferable, but the notation is not fully precise.

# 14. Interpretation and Discussion

The paper’s most convincing contribution is the separation between **content recognition** and **structural program generation**. Direct extraction and golden-label experiments indicate that a model can recognize the desired answer yet still fail to express a reusable XPath.

The executable metric exposes this difference. A system may have high conventional precision among nonempty predictions while failing to return anything for many cases. The six-way partition therefore measures failure modes relevant to deployment.

RQ1 is substantially, but not universally, supported. AUTOSCRAPER is strongest across the combined metrics and obtains the best headline configurations, but a few model/dataset rows have higher Correct under a baseline.

RQ2 is supported by:

- no-synthesis AUTOSCRAPER performance, which isolates progressive generation;
- full-versus-ablated comparisons;
- Figure 3’s seed-count trend;
- the qualitative trace in Figure 4.

RQ3 is supported conditionally:

- Accuracy is high for the strongest LLM, but weak models remain unreliable.
- Efficiency improves only after enough pages amortize generation.
- The paper estimates the average break-even point as 19.5 pages.

## Cross-reference and consistency findings

1. **DS1 page count:** 166 in prose versus 186 in Table 1.
2. **Efficiency domains:** §6.3 says one website in each of ten domains, but Table 6 lists eight domains—the eight SWDE domains.
3. **Detailed-result reference:** §5.1 says detailed results can be found in Tables 16 and 17, but those are dataset-statistics tables; detailed result tables are 7 and 8.
4. **Seed terminology:** Figure 3 says “seed websites,” while the method generally selects seed webpages within a case.
5. **Sequence-length claim:** Tables 10–12 do not uniformly support a simple strong-model/fewer-step ordering.
6. **Model naming:** Table 13 includes “Mistral 7B,” not among the eight principal models; elsewhere the model is Mixtral 8×7B.
7. **Table 9 caption:** it says “executable and IE evaluation,” but the rendered columns show only executable categories.
8. **Algorithm notation:** line 10’s subtree variable is underspecified.
9. **Synthesis claim:** Table 3 contains a Gemini case where synthesis does not improve every reported metric.

These do not invalidate the main reported trend, but they constrain how broadly it should be stated.

# 15. Contributions and Novelty

## Conceptual contribution

The paper proposes treating LLM-based web scraping as **reusable scraper generation**, positioned between manually designed wrappers and per-page language-agent extraction.

## Methodological contribution

It decomposes generation into:

- progressive, hierarchy-aware action-sequence construction;
- multi-page candidate synthesis.

## Algorithmic contribution

The top-down/step-back loop uses parser feedback and changing DOM context rather than merely regenerating against the entire original page.

## Evaluation contribution

The six-category executable evaluation measures complete correctness and operational failure across site-level cases.

## Experimental contribution

The authors evaluate:

- eight LLMs;
- three benchmarks;
- COT and Reflexion;
- component ablations;
- seed counts;
- direct extraction;
- supervised extractors;
- efficiency;
- error modes;
- golden labels;
- sequence lengths;
- XPath fragility.

## Implementation contribution

The paper says its resources are open source, but the repository was not part of the supplied material and therefore cannot be assessed here.

# 16. Limitations

## Authors’ stated limitations

From the Limitation section and error analysis (p. 9):

- The framework is restricted to information extraction from vertical detail pages.
- It transfers poorly to broader web-agent environments such as those represented by Mind2Web and WebArena.
- Performance depends on the backbone LLM.
- Improving LLM HTML understanding requires further corpus and training-strategy research.
- Same-site pages can still differ structurally.
- Multi-valued information remains difficult to capture comprehensively.
- The authors cannot guarantee that public datasets contain no socially harmful or toxic language.

Appendix B adds that XPath expressions remain fragile, especially when they include literal seed-page text.

## Additional evidence-based analyst observations

[D] These are not presented as author admissions:

- No confidence intervals, hypothesis tests, or variance estimates are reported for accuracy results.
- One random seed or sampling specification is not provided.
- The synthesis model and candidate-selection reliability are not independently evaluated.
- Most result tables appear to report a single aggregate per condition.
- Model/API versioning and decoding settings are insufficient for exact reproduction.
- The supervised comparison changes learning regimes and is acknowledged as unfair.
- The efficiency analysis reports wall-clock values without hardware, network-latency, batching, or API-load controls.
- A few numerical and cross-reference inconsistencies reduce traceability.
- Synthesis tests candidates on the same seed pages used to generate them; no dedicated validation subset is described.
- Exact-match comparison between model-recognized value and parser result could inherit recognition errors, though prompt logic and postprocessing may mitigate some formatting differences.

# 17. Threats to Validity

## Internal validity

- Unreported randomness in page sampling, LLM generation, and synthesis may affect results.
- Missing decoding and API settings make it difficult to attribute differences solely to the framework.
- Candidate selection on generation seed pages could favor seed-specific selectors.

## Construct validity

- “Correct” is stringent and useful, but the mutually exclusive categories compress different degrees of partial success.
- Action-sequence length is an indirect proxy for structural understanding and can be affected by selector style.
- Conventional F1 and executability measure different constructs; neither alone characterizes all deployment needs.

## External validity

- The task covers vertical, semi-structured detail pages rather than arbitrary modern web applications.
- JavaScript-heavy interaction, authentication, forms, navigation, anti-bot controls, and dynamically changing sessions are not evaluated.
- Performance relies strongly on model capability.

## Statistical conclusion validity

- No uncertainty intervals or statistical significance tests are reported.
- Figure 3 has no error bars.
- The timing experiment has only three AUTOSCRAPER repetitions and does not report dispersion.

## Ecological validity

The reuse scenario is realistic for extracting many same-site pages, but the datasets may not capture live layout changes, site defenses, or production failures.

## Reproducibility

Prompts and much dataset detail are supplied, which helps. Exact reproduction remains limited by absent model snapshots, decoding settings, hardware details, random seeds, and unsupplied repository contents.

# 18. Future Work and Open Questions

## A. Author-proposed future work

The authors explicitly propose improving LLM HTML understanding through:

- corpus collection;
- training strategies (§9, Limitation).

Appendix B also says they aim to explore XPath generation from non-text features.

## B. Additional open questions

[D] Questions remaining from the supplied evidence include:

- Would a held-out validation set improve synthesis reliability?
- Can selectors combine classes, relative structure, semantic labels, and fallback rules without literal values?
- How robust is a generated scraper after a live website redesign?
- Can the system extract all members of a multi-valued field?
- How often do model-recognized target values themselves contain errors?
- Would uncertainty-aware synthesis or voting across several candidates outperform choosing one sequence?
- How do token usage and monetary cost compare with direct extraction?
- Are gains stable across repeated page samples and decoding seeds?
- Can the executable categories be extended to capture latency, coverage, and robustness over time?
- How would the framework handle client-side rendering and interactive pages?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| AUTOSCRAPER | The proposed two-phase LLM-guided scraper generator |
| LLM | Large language model |
| HTML | Markup describing page content and structure |
| DOM | Document Object Model; the page represented as a tree |
| XPath | A language for selecting nodes in an HTML/XML tree |
| Wrapper | Reusable site-specific extraction rule or parser |
| Action sequence | Ordered XPath operations, with pruning steps followed by extraction |
| Seed webpage | A page used to create or choose a scraper |
| Progressive generation | Repeatedly narrow, test, and revise the active HTML context |
| Top-down | Search downward from the current subtree root |
| Step-back | Move upward to a broader ancestor when a selection is unreliable |
| Synthesis | Choose one candidate sequence using its results across seed pages |
| COT | Chain-of-Thought baseline; one-turn generation in this implementation |
| Reflexion | Iterative self-reflection and regeneration baseline |
| SWDE | Structured Web Data Extraction dataset |
| Extended SWDE | A more fine-grained relation-extraction extension of SWDE |
| DS1 | A dataset of hand-crafted pages from 30 real-life sites |
| IE | Information extraction |
| OpenIE | Open information extraction; relations are not initially restricted to a small fixed schema |
| Precision | Fraction of extracted items that are relevant |
| Recall | Fraction of relevant items that are extracted |
| F1 | Harmonic combination of precision and recall |
| Macro-F1 | Mean of case-level F1 scores |
| Correct | Precision, recall, and F1 all equal 1 |
| Unexecutable | Evaluation category defined by recall equal to 0 |
| Over-estimate | Extraction from a page/case whose ground truth is empty |
| \(A_{\mathrm{seq}}\) | Generated XPath action sequence |
| \(n\) | Number of XPaths in an action sequence |
| \(n_s\) | Number of seed pages |
| \(d_{\max}\) | Maximum retry count |
| \(N_W\) | Number of webpages processed |
| \(T_g\) | Per-seed generation time |
| \(T_s\) | Synthesis time |
| \(T_e\) | Wrapper execution time per page |
| \(T_d\) | Direct LLM extraction time per page |
| XPath predicate | A condition narrowing selected nodes, such as matching a class or text |
| XPath fragility | Failure of a selector on another page because it encodes unstable details |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Accessible document | 19 | pages | Entire paper | Author-reported/supplied | pp. 1–19 |
| SWDE source size | 124,291 | pages | 80 sites, 8 domains | Author-reported | §3.2, p. 3 |
| SWDE transformed benchmark | 320 / 32 / 32,000 | cases/tasks/pages | Main benchmark | Author-reported | Table 1, p. 3 |
| Extended SWDE benchmark | 294 / 221 / 29,400 | cases/tasks/pages | Main benchmark | Author-reported | Table 1 |
| DS1 benchmark | 83 / 11 / 186 | cases/tasks/pages | Conflicts with prose’s 166 pages | Author-reported | Table 1 |
| Main models | 8 | LLMs | Four closed, four open | Author-reported | §5.1 |
| Main seed count | 3 | pages | SWDE, Extended SWDE | Author-reported | §5.1 |
| DS1 seed count | 1 | page | No synthesis | Author-reported | §5.1; App. A.2 |
| Maximum retries | 5 | retries | All main experiments | Author-reported | §5.1 |
| GPT-4-Turbo AUTOSCRAPER SWDE | 71.56 / 4.06 / 88.69 | Correct% / Unexecutable% / F1 | Main result | Author-reported | Table 2 |
| GPT-4-Turbo AUTOSCRAPER Extended SWDE | 64.11 / 15.33 / 76.21 | Correct% / Unexecutable% / F1 | Main result | Author-reported | Tables 2, 7 |
| GPT-4-Turbo AUTOSCRAPER DS1 | 57.83 / 16.87 / 75.52 | Correct% / Unexecutable% / F1 | Main result | Author-reported | Tables 2, 8 |
| SWDE Correct gain over GPT-4 Reflexion | 4.06 | percentage points | \(71.56-67.50\) | Analyst-derived | Table 2 |
| SWDE Unexecutable reduction | 6.88 | percentage points | \(10.94-4.06\), GPT-4 Reflexion→AUTOSCRAPER | Analyst-derived | Table 2 |
| AUTOSCRAPER vs direct extraction | 88.69 vs 78.56 | F1 | GPT-4-Turbo, SWDE | Author-reported | Table 4 |
| AUTOSCRAPER vs WebFormer | 88.69 vs 86.58 | F1 | Zero-shot vs supervised comparison | Author-reported | Table 5 |
| Difference over WebFormer | 2.11 | F1 points | \(88.69-86.58\) | Analyst-derived | Table 5 |
| Mean break-even page count | 19.5 | pages/site | GPT-4-Turbo timing analysis | Author-reported; arithmetically consistent | §6.3, Table 6 |
| Wrapper execution range | 0.21–0.54 | seconds/page | Eight Table 6 domains | Author-reported | Table 6 |
| Direct extraction range | 6.59–14.26 | seconds/page | Eight Table 6 domains | Author-reported | Table 6 |
| Up-front generation+synthesis | 107.1–238.4 | seconds | Eight Table 6 domains | Author-reported | Table 6 |
| GPT-4 sequence length, SWDE | 1.57 | steps average | AUTOSCRAPER | Author-reported | Table 10 |
| Phi-3 sequence length, SWDE | 3.62 | steps average | AUTOSCRAPER | Author-reported | Table 10 |
| GPT4 XPath bad cases | 0.61 / 2.90 | percent | `contains` / equality predicates | Author-reported | Table 13 |
| Seed-count plot trends | Correct ↑; Unexecutable ↓ | direction | 1–5 seeds | Visually readable | Figure 3 |
| Plot point values | Approx. only | percent | Figure 3 lacks labels | Approximate visual estimate | Figure 3 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| AUTOSCRAPER improves scraper generation | Higher Correct/lower Unexecutable in most same-model comparisons | X1, Table 2 | §5.2, p. 6 | Strong aggregate evidence; not universal on every row/metric |
| Progressive HTML understanding helps | No-synthesis AUTOSCRAPER often beats COT/Reflexion | X2, Table 3 | §5.3 | Moderate; only three models in ablation |
| Synthesis improves reuse | Full variants usually beat no-synthesis; more seeds improve trends | Table 3, Figure 3 | §5.3–§5.4 | Generally supported; Gemini exception and no error bars |
| Executability metrics reveal hidden failure | High conventional precision can coexist with low Correct/high Unexecutable | Table 2 | §3.3, §5.2 | Strong construct example |
| Strong models better handle HTML structure | GPT-4 variants obtain better headline results; golden-label failures remain for smaller models | Tables 2, 9 | §5.2; App. A.3 | Supported overall, though model order is not uniform |
| AUTOSCRAPER can beat direct extraction | GPT-4-Turbo: 88.69 vs 78.56 | Table 4 | §6.1 | True only for one of eight displayed models |
| AUTOSCRAPER can beat supervised baselines | 88.69 exceeds WebFormer 86.58 | Table 5 | §6.2 | Numerically supported but training regimes are not controlled |
| AUTOSCRAPER becomes efficient at scale | Parser execution is much faster; mean break-even 19.5 pages | Eqs. 3–6, Table 6 | §6.3 | Conditional on additive timing assumptions and measured environment |
| More seed pages help | Correct rises and Unexecutable falls | Figure 3 | §5.4 | Visually supported; diminishing returns; exact points unlabeled |
| XPath remains fragile | Literal seed-specific text causes failures; nonzero bad-case rates | Tables 13–14 | App. B.2 | Supported by manual analysis, but sample counts are absent |
| Multi-valued extraction remains difficult | Qualitative failures for addresses/phone numbers | Error analysis | §6.4 | Author-reported examples; no frequency data |

# 22. Very Simple Explanation

Imagine you want a program to read the price from thousands of product pages. You could ask a powerful AI to read every page, but that repeats expensive work. Or you could hand-write a rule, but the rule may break whenever the page layout changes.

AUTOSCRAPER asks the AI to write the rule. If its first rule grabs the wrong number, the system backs up in the page’s tree structure, keeps a useful part of the page, and tries again. It repeats this on a few example pages and chooses the rule that works most consistently across them.

The experiments show that this often creates more usable rules than simply asking the AI to reason once or reflect on a failed rule. The best model, GPT-4-Turbo, performed especially well. Once a rule has been generated, running it is far faster than asking the AI to read every new page.

It is not a universal web robot, however. It works on similarly structured information pages, can break when pages differ, and still struggles with fields that appear in several places. Its success also depends heavily on how well the underlying language model understands HTML.

# Completeness Audit

## Inventory

- **Title:** *AUTOSCRAPER: A Progressive Understanding Web Agent for Web Scraper Generation*
- **Authors:** Wenhao Huang, Zhouhong Gu, Chenghao Peng, Zhixu Li, Jiaqing Liang, Yanghua Xiao, Liqian Wen, Zulong Chen.
- **Venue:** 2024 Conference on Empirical Methods in Natural Language Processing, pp. 2371–2389.
- **Document type:** empirical AI/algorithm and web-information-extraction systems paper.
- **Sections:** Abstract; §§1–7; Acknowledgement; Limitation; Ethics; References; Appendices A–D.
- **Figures:** 4.
- **Tables:** 18.
- **Equations:** 6 numbered equations.
- **Algorithms:** 1.
- **Explicit research questions:** 3.
- **Distinct analyses:** 12 registered above.
- **Formal hypotheses/theorems:** none.

## Coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes | Yes | Fully represented | Orientation and contributions |
| §1 Introduction | Yes | Yes | Fully represented | Problem, gap, challenges |
| §2 Related Work | Yes | Yes | Represented in compressed form | Major categories and positioning retained; individual citations compressed |
| §3.1 Task Formulation | Yes | Yes | Fully represented | Definition and variables |
| §3.2 Datasets | Yes | Yes | Fully represented | Includes preprocessing and count conflict |
| §3.3 Metrics | Yes | Yes | Fully represented | All six categories and Eq. 1 |
| §4.1 Modeling | Yes | Yes | Fully represented | Eq. 2 and sequence semantics |
| §4.2 Progressive Generation | Yes | Yes | Fully represented | Top-down and step-back |
| §4.3 Synthesis | Yes | Yes | Fully represented | Cross-page selection |
| §5.1 Settings | Yes | Yes | Fully represented | Models, seeds, retries, omissions |
| §5.2 Main Results | Yes | Yes | Fully represented | Includes counterexamples to universal wording |
| §5.3 Ablation | Yes | Yes | Fully represented | Includes Gemini exception |
| §5.4 Seed Websites | Yes | Yes | Fully represented | Figure 3 uncertainty noted |
| §6.1 Direct Extraction | Yes | Yes | Fully represented | Table 4 |
| §6.2 Supervised Baselines | Yes | Yes | Fully represented | Unfair-comparison caveat retained |
| §6.3 Efficiency | Yes | Yes | Fully represented | Eqs. 3–6 and Table 6 |
| §6.4 Error Analysis | Yes | Yes | Fully represented | Both failure modes |
| §7 Conclusion | Yes | Yes | Fully represented | Central conclusion |
| Acknowledgement | Yes | Yes | Represented in compressed form | Funding/platform reported |
| Author Limitation section | Yes | Yes | Fully represented | Both explicit limitations |
| Ethics/annotations/risks | Yes | Yes | Represented in compressed form | Consent, compensation, public/anonymized data, residual toxic-language risk |
| References | Yes, text | Contextually | Deliberately compressed | Individual bibliography entries are not substantive findings |
| Appendix A.1 | Yes | Yes | Fully represented | X8 and Table 7 |
| Appendix A.2 | Yes | Yes | Fully represented | X9 and Table 8 |
| Appendix A.3 | Yes | Yes | Fully represented | X10 and Table 9 |
| Appendix B.1 | Yes | Yes | Fully represented | Figure 4 |
| Appendix B.2 | Yes | Yes | Fully represented | Tables 10–14 |
| Appendix C | Yes | Yes | Fully represented | Tables 15–17 |
| Appendix D.1 | Yes | Yes | Fully represented | Table 18 |
| Appendix D.2 | Yes | Yes | Represented in compressed form | Top-down, step-back, and synthesis prompt functions summarized |
| RQ1–RQ3 | Yes | Yes | Fully represented | Addressed separately |
| Figure 1 | Visually | Yes | Fully represented | Conceptual |
| Figure 2 | Visually | Yes | Fully represented | Architecture |
| Figure 3 | Visually | Yes | Fully represented | Approximate values labeled as such |
| Figure 4 | Visually | Yes | Fully represented | Qualitative trace |
| Tables 1–18 | Yes | Yes | Fully represented or compressed with disclosure | Dense row-by-row values summarized; key extrema and exceptions retained |
| Equations 1–6 | Yes | Yes | Fully represented | Symbols and roles explained |
| Algorithm 1 | Visually | Yes | Fully represented | Notation ambiguity flagged |
| X1–X12 | Yes | Yes | Fully represented | Each has purpose, setup, evidence, and caveat |
| Major contributions | Yes | Yes | Fully represented | Conceptual through empirical |
| Author-stated limitations | Yes | Yes | Fully represented | Kept separate from analyst observations |
| Supplementary material | No separate artifact | Yes | Missing from supplied material | Repository not inspected |

## Missing or inaccessible material

- No separate code repository or supplementary artifact was supplied.
- Pages 9–11 and 17 were not visually rendered; their native text was available and inspected.
- Exact hardware, software versions, model snapshots, decoding settings, random seeds, costs, and complete run-level outputs are absent from the paper.
- Figure 3 does not label exact point values.
- Table 13 does not provide manual-review sample counts.
- Full prompts are supplied, but actual per-case prompt histories and raw model responses are not.

## Uncertain interpretations

- DS1 contains 166 pages in prose but 186 webpages in Table 1.
- The efficiency experiment says ten domains but shows eight.
- Figure 3 alternates between “seed websites” and “seed webpages.”
- Algorithm 1 line 10 ambiguously refers to \(h\) rather than a clearly indexed subtree.
- Table 13’s “Mistral 7B” is not explained relative to the main Mixtral 8×7B model.
- The sequence-length/LLM-strength relationship is not monotonic across all datasets.
- Exact Figure 3 points cannot be read as author-reported numbers.

## Deliberately compressed material

- Individual bibliographic entries were not summarized one by one.
- Table 2 and Tables 7–9 contain hundreds of metric cells; all table structures, leading values, important counterexamples, and claims were represented, while non-leading cells were compressed.
- Tables 15–18 contain long lists of sites, attributes, and prompts; their full roles and domain coverage were represented without duplicating every supplied row.
- Appendix module prompts were explained by their fields, constraints, and role rather than reproduced verbatim.
- Acknowledgement and ethics prose was condensed because it does not change the algorithm or results.

## Potential omissions

No substantive section, research question, experiment, figure, table, numbered equation, algorithm, appendix, major contribution, or author-stated limitation identified in the inventory is knowingly omitted. Dense repetitive table cells and bibliographic details were deliberately compressed as disclosed above.