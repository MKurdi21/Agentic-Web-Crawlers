# AutoScraper: A Progressive Understanding Web Agent for Web Scraper Generation

**Authors:** Wenhao Huang, Zhouhong Gu, Chenghao Peng, Zhixu Li, Jiaqing Liang, Yanghua Xiao, Liqian Wen, and Zulong Chen  
**Venue:** Proceedings of EMNLP 2024, pp. 2371–2389

## 1. Background and Context

Web scraping uses software to extract specific information from websites automatically. It supports applications such as market research, competitive analysis, data aggregation, and real-time monitoring, while reducing manual data entry. Building reliable scrapers is difficult because websites differ widely in content and structure and may change over time.

The paper divides existing automated approaches into two categories:

- **Wrapper-based methods** use manually designed rules, XPath expressions, learned DOM parsers, heuristics, or neural models. They can be fast and reusable when a website has a stable layout, but usually require substantial human work—such as annotations, rules, features, and site-specific verification—and do not adapt easily to new website structures.
- **Language-agent methods** use large language models (LLMs) to interpret natural-language requests and extract information directly. They adapt better to unfamiliar or dynamic content, but repeatedly invoking powerful API-based LLMs is slow and expensive. Their extraction behavior is also difficult to reuse across similar pages.

**Figure 1** contrasts these approaches. Traditional wrappers reuse extraction logic effectively but require heavy manual effort when moving to new websites. Language agents can answer queries on new pages but repeatedly consume LLM time and money. AutoScraper combines both ideas: an LLM generates a reusable scraper, which can then answer similar questions across pages without requiring full LLM processing every time.

The authors identify three central challenges in LLM-generated scrapers:

1. **Long, hierarchical HTML:** HTML mixes structured tags and attributes with unstructured text. An LLM may understand the page’s words but still generate an XPath that does not follow the DOM hierarchy correctly.
2. **Reusability:** An XPath that works on one page may depend on that page’s exact text or layout and fail on other pages from the same website.
3. **Evaluation:** Standard precision, recall, and F1 evaluate extracted values, often page by page. They do not directly measure whether one generated scraper executes reliably across an entire website.

Previous language agents such as Chain-of-Thought (COT), Reflexion, Self-Refine, and Self-Debug can iteratively reason or revise failed plans, but they do not adequately exploit HTML structure or simplify the page after failure. Existing general web-agent benchmarks also emphasize activities such as shopping, booking, navigation, and software interaction rather than the accuracy and repeated efficiency required for large-scale scraping.

## 2. Research Goal and Objectives

The paper introduces the task of using an LLM to generate an executable, reusable web scraper and proposes **AutoScraper**, a two-stage framework combining:

1. **Progressive generation**, which incrementally navigates and prunes the HTML hierarchy; and
2. **Synthesis**, which selects a scraper that generalizes across several pages from the same website.

The experiments address three explicit research questions:

1. Can AutoScraper outperform state-of-the-art scraper-generation methods?
2. Which components of AutoScraper improve scraper-generation performance?
3. Is AutoScraper sufficiently accurate and efficient for practical web scraping?

The work also proposes an **executability evaluation** intended to reflect scraper reliability across a collection of pages rather than only the accuracy of isolated extracted values.

## 3. Methods (Approach/Design)

### 3.1 Task definition

A case consists of:

- A set of webpages \(W\) from the same website;
- A subject or topic entity \(s\);
- A target attribute or relation \(r\); and
- A natural-language extraction instruction.

The objective is to generate an executable rule or action sequence \(A\) that extracts the target information \(o\) from all relevant pages.

Instead of producing one XPath, AutoScraper generates an ordered sequence:

\[
A_{\text{seq}}=[XPath_1, XPath_2,\ldots,XPath_n].
\]

The XPath expressions are executed in order. All but the final XPath progressively prune the current HTML subtree; the last XPath extracts the target value.

### 3.2 Datasets and preprocessing

The experiments use three semi-structured web-information-extraction datasets.

| Dataset | Cases | Tasks | Evaluated webpages |
|---|---:|---:|---:|
| SWDE | 320 | 32 | 32,000 |
| Extended SWDE | 294 | 221 | 29,400 |
| DS1 | 83 | 11 | 186 |

**SWDE** originally contains 124,291 pages from 80 websites in eight domains. Each website focuses on roughly 3–5 attributes. For the transformed benchmark, the authors sampled 100 pages for each website/instruction case.

Its eight domains and target attributes were:

- Auto: model, price, engine, fuel economy
- Book: title, author, ISBN-13, publisher, publication date
- Camera: model/product name, price, manufacturer
- Job: title, company, location, posting date
- Movie: title, director, genre, MPAA rating
- NBA player: name, current team, height, weight
- Restaurant: name, address, phone, cuisine
- University: name, phone, website, type

The full source dataset contains up to 2,000 pages for many sites, with smaller sites ranging from 220 to 1,767 camera pages, 420 to 515 NBA-player pages, and 615 to 1,063 pages for some university sites.

**Extended SWDE** provides fine-grained annotations for 21 SWDE websites across movie, NBA-player, and university domains. Whereas SWDE averages approximately 4,480 triples for three predicates per site, Extended SWDE averages about 41,000 triples for 36 predicates per site. The study maps relations to predefined attributes, removes unusual relations, and evaluates 294 attributes. The detailed dataset table lists 8 movie sites, 8 NBA-player sites, and 5 university sites, with 5–34 attributes per site.

**DS1** is described as containing 166 hand-crafted, annotated pages from 30 real-world sites in four domains:

- Books: title, author, price
- E-commerce: title, price
- Hotels: address, price, title
- Movies: actor, genre, title

The paper’s transformed benchmark table reports 186 webpages, creating a source-level discrepancy with the textual description of 166 pages. Because each DS1 website has only two pages, one was used for inference and the other for evaluation. No synthesis was used because only one seed page was available.

For preprocessing, the authors:

- Created domain- and attribute-specific natural-language instructions;
- Removed `<script>` and `<style>` nodes using BeautifulSoup;
- Deleted every node attribute except `class`; and
- Normalized escape characters to match annotations.

A website plus one extraction instruction constituted a case. For example, one case could contain 100 ESPN NBA-player pages and the instruction to extract each player’s current team.

### 3.3 Progressive generation

Generating a complete scraper from a long page in one attempt is difficult. AutoScraper therefore alternates two DOM operations:

- **Top-down:** Starting from the current DOM root, the LLM proposes an XPath aimed at the target node. The XPath is executed, and the model judges whether the extracted result matches the value it recognizes from the page.
- **Step-back:** If the proposed XPath fails or yields the wrong context, AutoScraper moves upward from the failed node to a broader ancestor containing the expected value. This produces a smaller but sufficiently informative subtree for the next top-down attempt.

Algorithm 1 initializes an empty action history and repeatedly:

1. Asks the LLM for an expected value and XPath;
2. Executes the XPath;
3. Stops if the parser output matches the expected value;
4. Otherwise appends parent steps (`/..`) until the selected HTML includes the value;
5. Adds the pruning XPath to the action sequence; and
6. retries until success or the maximum retry count is exceeded.

The experiments set the maximum number of retries to **5**.

The top-down prompt asks the LLM to inspect prior attempts, distinguish empty, irrelevant, or acceptable outputs, avoid hard-coding an exact page value, avoid selecting multiple nodes containing different values, and prefer reusable features such as classes and positional indices. The step-back prompt asks whether a candidate subtree contains all expected values.

### 3.4 Synthesis

A scraper generated from one page may contain page-specific assumptions. The synthesis stage therefore:

1. Randomly selects \(n_s\) seed pages;
2. Generates one action sequence from each seed page;
3. Executes every candidate sequence on all seed pages;
4. Collects the sequences and their outputs; and
5. asks an LLM discriminator to select the candidate most likely to extract the target information across pages from the same site.

The synthesis prompt presents the task, candidates, and their cross-page results, then requests the best candidate number.

The main experiments use:

- \(n_s=3\) for SWDE and Extended SWDE;
- \(n_s=1\) for DS1.

**Figure 2** illustrates both stages with a basketball-statistics page. A first XPath finds a nearby but incorrect value. A step-back moves to an ancestor subtree, and another top-down XPath selects the correct child. Multiple sequences produced on different seed pages are then tested across those pages, and synthesis selects the most reusable sequence rather than merely the one that worked on its source page.

### 3.5 Evaluation metrics

The authors retain macro-averaged precision, recall, and F1 but add six mutually exclusive executability categories:

1. **Correct:** precision, recall, and F1 are all 1.
2. **Precision-only:** precision is 1, meaning every extracted item is correct but some relevant items are missed.
3. **Recall-only:** recall is 1, meaning all relevant items are found but irrelevant items are also extracted.
4. **Unexecutable:** recall is 0, meaning no relevant instance is found.
5. **Over-estimate:** precision is 0 because the scraper extracts something when the ground truth is empty.
6. **Else:** partial or otherwise uncategorized outcomes.

For each category, the metric is:

\[
M_R=\frac{\text{number of cases in that category}}
{\text{total number of cases}}.
\]

Higher **Correct** and lower **Unexecutable** are preferred.

### 3.6 Models and baselines

Eight LLMs were tested:

- Closed-source: GPT-3.5-Turbo, Gemini Pro, GPT-4o-mini, GPT-4-Turbo
- Open-source: Phi-3-medium, CodeLlama-34B, Mixtral 8×7B, DeepSeek-Coder-33B

Each was used with:

- Chain-of-Thought (COT);
- Reflexion; and
- AutoScraper.

All experiments were zero-shot because of LLM context-length limits.

Additional comparisons included direct LLM extraction and five supervised systems: Render-Full, FreeDOM, SimpDOM, MarkupLM Base, and WebFormer.

## 4. Results and Findings

### 4.1 Main results on SWDE

AutoScraper produced the highest Correct rate and generally the lowest Unexecutable rate for every model.

| Model | Method | Correct | Unexecutable | F1 |
|---|---|---:|---:|---:|
| GPT-3.5-Turbo | COT | 36.75 | 43.46 | 47.99 |
|  | Reflexion | 46.29 | 37.10 | 55.10 |
|  | **AutoScraper** | **54.84** | **19.35** | **69.20** |
| Gemini Pro | COT | 29.69 | 47.19 | 41.81 |
|  | Reflexion | 33.12 | 52.50 | 40.88 |
|  | **AutoScraper** | **42.81** | **34.38** | **54.91** |
| GPT-4o-mini | COT | 54.66 | 20.26 | 69.92 |
|  | Reflexion | 53.70 | 22.83 | 69.15 |
|  | **AutoScraper** | **62.06** | **15.11** | **76.97** |
| GPT-4-Turbo | COT | 61.88 | 14.37 | 76.95 |
|  | Reflexion | 67.50 | 10.94 | 82.40 |
|  | **AutoScraper** | **71.56** | **4.06** | **88.69** |
| Phi-3-medium | COT | 12.50 | 80.00 | 17.21 |
|  | Reflexion | 12.19 | 77.81 | 17.31 |
|  | **AutoScraper** | **24.06** | **52.19** | **34.93** |
| CodeLlama | COT | 17.98 | 74.53 | 21.36 |
|  | Reflexion | 18.08 | 73.06 | 22.44 |
|  | **AutoScraper** | **23.99** | **64.94** | **28.41** |
| Mixtral 8×7B | COT | 28.75 | 57.81 | 37.26 |
|  | Reflexion | 36.25 | 51.25 | 43.60 |
|  | **AutoScraper** | **46.88** | **30.31** | **59.75** |
| DeepSeek-Coder | COT | 36.56 | 42.50 | 47.05 |
|  | Reflexion | 37.19 | 44.69 | 47.08 |
|  | **AutoScraper** | **38.75** | **39.69** | **49.68** |

Notable findings include:

- GPT-4-Turbo + AutoScraper was best overall on SWDE: **71.56% Correct, 4.06% Unexecutable, and 88.69 F1**.
- Mixtral 8×7B + AutoScraper achieved **46.88% Correct**, exceeding GPT-3.5-Turbo + Reflexion at **46.29%**, showing that the framework can allow a weaker model to rival a stronger model using a less structured agent.
- Small models remained much less reliable. Phi-3-medium + AutoScraper still had **52.19% Unexecutable**, and CodeLlama had **64.94%**.
- Traditional precision obscured some differences. For example, many weak systems had high precision because the metric scored only returned items while ignoring empty or unexecutable runs.

The complete SWDE results also divide non-perfect cases among precision-only, recall-only, over-estimate, and Else categories. Over-estimation was uncommon—generally 0–1.25%—while unexecutability was the dominant failure for weaker models.

### 4.2 Extended SWDE

Extended SWDE contains more complex, fine-grained, sometimes multi-valued relations and ambiguous instructions. AutoScraper’s Correct/Unexecutable/F1 results were:

| Model | COT | Reflexion | AutoScraper |
|---|---|---|---|
| GPT-3.5-Turbo | 35.19 / 55.40 / 41.28 | 43.90 / 49.13 / 48.66 | **46.34 / 34.84 / 57.74** |
| Gemini Pro | 34.49 / 49.13 / 42.40 | 34.15 / 51.57 / 41.66 | **35.89 / 42.86 / 47.80** |
| GPT-4o-mini | 45.79 / 38.72 / 56.32 | 39.06 / 47.47 / 48.66 | **56.23 / 27.27 / 67.56** |
| GPT-4-Turbo | 56.10 / 29.27 / 65.08 | **64.81** / 19.51 / 75.85 | 64.11 / **15.33** / **76.21** |
| Phi-3-medium | 11.78 / 79.46 / 16.28 | 12.66 / 82.28 / 15.42 | **21.15 / 64.42 / 30.29** |
| CodeLlama | 9.01 / 85.84 / 11.21 | **13.73 / 80.26 / 16.01** | 11.16 / 85.84 / 12.52 |
| Mixtral 8×7B | 32.40 / 57.14 / 38.30 | 29.62 / 62.02 / 33.64 | **40.77 / 38.33 / 52.50** |
| DeepSeek-Coder | **38.33** / **47.74** / **44.80** | 36.24 / 51.92 / 43.64 | 37.63 / 50.52 / 44.33 |

Each cell reports **Correct / Unexecutable / F1**.

Thus, AutoScraper was strongest for most model–metric combinations, but not literally every individual metric: GPT-4-Turbo Reflexion had a slightly higher Correct rate than AutoScraper, and CodeLlama and DeepSeek-Coder showed exceptions. The authors’ broader conclusion is that closed-source LLMs handled complex, ambiguous, and multi-valued tasks better than open-source models.

Unclear labels such as “Calendar System” and “Facilities and Programs Offered” on university sites degraded all methods.

### 4.3 DS1

Because DS1 provided only one inference page per site, AutoScraper was evaluated without synthesis. Nevertheless, it achieved the highest Correct rate and F1 for every model:

| Model | COT | Reflexion | AutoScraper |
|---|---|---|---|
| GPT-3.5-Turbo | 32.65 / 53.06 / 41.16 | 36.73 / 51.02 / 43.75 | **48.98 / 44.90 / 52.38** |
| Gemini Pro | 17.72 / 75.95 / 22.10 | 20.25 / 65.82 / 27.66 | **43.04 / 34.18 / 56.92** |
| GPT-4o-mini | 46.99 / 42.17 / 53.77 | 38.55 / 45.78 / 43.86 | **53.01 / 34.94 / 60.10** |
| GPT-4-Turbo | 50.60 / 30.12 / 64.73 | 50.60 / 33.73 / 63.50 | **57.83 / 16.87 / 75.52** |
| Phi-3-medium | 9.64 / 85.54 / 12.28 | 7.23 / 90.36 / 8.89 | **22.89 / 69.88 / 26.60** |
| CodeLlama | 2.70 / 89.19 / 9.19 | 8.82 / 85.29 / 12.69 | **13.51 / 81.08 / 17.39** |
| Mixtral 8×7B | 17.72 / 74.68 / 22.01 | 22.78 / 69.62 / 28.20 | **36.71 / 43.04 / 48.23** |
| DeepSeek-Coder | 25.30 / 60.24 / 35.65 | 22.89 / 65.06 / 32.04 | **39.76 / 42.17 / 50.28** |

Again, each cell is **Correct / Unexecutable / F1**. GPT-4-Turbo + AutoScraper was best overall.

### 4.4 Ablation study

The SWDE ablation removed synthesis from COT, Reflexion, and AutoScraper.

For GPT-3.5-Turbo:

- COT fell from **36.75 Correct / 43.46 Unexecutable / 47.99 F1** to **27.56 / 57.24 / 34.44** without synthesis.
- Reflexion fell from **46.29 / 37.10 / 55.10** to **28.62 / 59.01 / 35.01**.
- AutoScraper fell from **54.84 / 19.35 / 69.20** to **44.52 / 29.33 / 58.44**.

For GPT-4-Turbo:

- COT fell from **61.88 / 14.37 / 76.95** to **46.88 / 30.00 / 61.20**.
- Reflexion fell from **67.50 / 10.94 / 82.40** to **56.87 / 25.31 / 69.78**.
- AutoScraper fell from **71.56 / 4.06 / 88.69** to **65.31 / 11.87 / 80.41**.

AutoScraper without synthesis still generally exceeded the baselines, supporting the independent value of progressive generation. Synthesis improved not only AutoScraper but also COT and Reflexion, showing that evaluating candidates on multiple pages improves stability and generalization.

Gemini Pro showed one irregularity: AutoScraper without synthesis had lower Correct (**39.46** versus **42.81**) but also a slightly lower Unexecutable rate (**31.56** versus **34.38**) and higher F1 (**56.48** versus **54.91**).

### 4.5 Number of seed pages

**Figure 3** plots Correct and Unexecutable rates for GPT-4-Turbo and GPT-3.5-Turbo as the number of SWDE seed pages rises from 1 to 5.

For both models:

- Correct rises;
- Unexecutable falls; and
- Gains become progressively smaller.

From the graph, GPT-4-Turbo Correct rises from roughly the mid-60s to the low-70s, while its Unexecutable rate falls from roughly the low teens to around 4%. GPT-3.5-Turbo Correct rises from roughly the mid-40s to the high-50s, while Unexecutable falls from roughly 30% toward the mid-teens. These graph values are approximate because the plot does not label every point numerically.

The authors conclude that additional seed pages can improve AutoScraper, but there is a saturation point.

### 4.6 Direct LLM extraction

On SWDE, direct extraction and AutoScraper F1 scores were:

| Model | Direct extraction | AutoScraper |
|---|---:|---:|
| GPT-3.5-Turbo | 75.76 | 69.20 |
| Gemini Pro | 76.62 | 54.91 |
| GPT-4o-mini | 79.93 | 76.97 |
| GPT-4-Turbo | 78.56 | **88.69** |
| Phi-3-medium | 71.73 | 34.93 |
| CodeLlama | 47.38 | 28.41 |
| Mixtral 8×7B | 73.45 | 59.75 |
| DeepSeek-Coder | 61.96 | 49.68 |

Direct extraction was better for every model except GPT-4-Turbo. The gap narrowed as model capability increased, and GPT-4-Turbo + AutoScraper exceeded direct GPT-4-Turbo extraction by **10.13 F1 points**.

The paper interprets this as evidence that smaller LLMs may understand page text but cannot reliably translate that understanding into structural XPath rules. With a sufficiently capable model, reusable scraper generation can outperform direct extraction.

### 4.7 Comparison with supervised methods

On SWDE:

| Method | F1 |
|---|---:|
| Render-Full | 84.30 |
| FreeDOM | 82.32 |
| SimpDOM | 83.06 |
| MarkupLM Base | 84.31 |
| WebFormer | 86.58 |
| Reflexion + GPT-4-Turbo | 82.40 |
| **AutoScraper + GPT-4-Turbo** | **88.69** |

The five supervised models were trained using one seed site, whereas AutoScraper was zero-shot. Despite this mismatch, AutoScraper achieved the highest F1, beating WebFormer by **2.11 points**.

### 4.8 Efficiency

Let:

- \(n_s\) = number of seed pages;
- \(N_W\) = total pages from a website;
- \(T_g\) = time to generate one wrapper;
- \(T_s\) = synthesis time;
- \(T_e\) = wrapper execution time per page;
- \(T_d\) = direct LLM extraction time per page.

AutoScraper’s total time is:

\[
T_1=(n_sT_g+T_s)+N_WT_e,
\]

while direct extraction takes:

\[
T_2=N_WT_d.
\]

AutoScraper becomes faster when:

\[
N_W\geq \frac{n_sT_g+T_s}{T_d-T_e}.
\]

Using GPT-4-Turbo, the measured values were:

| Domain | Direct extraction \(T_d\) | Generation + synthesis | Scraper execution \(T_e\) | Break-even pages |
|---|---:|---:|---:|---:|
| Auto | 8.27 s | 238.4 s | 0.30 s | 30 |
| Book | 10.20 s | 176.4 s | 0.51 s | 18 |
| Camera | 6.59 s | 107.1 s | 0.31 s | 18 |
| Job | 7.42 s | 123.5 s | 0.21 s | 18 |
| Movie | 7.47 s | 133.2 s | 0.21 s | 19 |
| NBA player | 8.32 s | 179.4 s | 0.45 s | 23 |
| Restaurant | 8.87 s | 160.8 s | 0.54 s | 20 |
| University | 14.26 s | 134.7 s | 0.32 s | 10 |

The reported average break-even point is **19.5 pages**, substantially below the average number of pages per SWDE site. Wrapper generation is therefore expensive upfront, but execution takes only about **0.21–0.54 seconds per page**, making the method advantageous for repeated extraction at scale.

The text says a website was randomly selected from each of “10 domains,” but Table 6 lists the eight SWDE domains; this is another inconsistency in the source.

### 4.9 Golden-label experiment

The authors supplied the same correct extraction targets to all frameworks to isolate their ability to generate executable action sequences.

For GPT-4-Turbo:

- COT: **61.88% Correct, 11.56% Unexecutable**
- Reflexion: **71.25%, 14.37%**
- AutoScraper: **75.31%, 4.06%**

Other AutoScraper Correct/Unexecutable results were:

- GPT-3.5-Turbo: **56.89 / 13.43**
- Gemini Pro: **45.31 / 30.31**
- GPT-4o-mini: **67.20 / 12.22**
- Phi-3-medium: **27.27 / 41.56**
- CodeLlama: **26.20 / 53.51**
- Mixtral 8×7B: **45.62 / 32.50**
- DeepSeek-Coder: **38.44 / 31.56**

Progressive understanding remained beneficial even when the correct value was supplied. Open-source models did not improve consistently enough to close the gap, suggesting that their main difficulty was understanding the DOM hierarchy rather than merely recognizing page content.

### 4.10 Action-sequence length

Stronger structural understanding generally produced shorter action sequences.

Average numbers of steps were:

| Model | SWDE | DS1 | Extended SWDE |
|---|---:|---:|---:|
| GPT-4-Turbo | 1.57 | 2.29 | 3.15 |
| GPT-4o-mini | 2.12 | 2.06 | 2.65 |
| GPT-3.5-Turbo | 2.56 | 2.48 | 3.02 |
| Gemini Pro | 2.99 | 2.82 | 3.45 |
| Mixtral 8×7B | 3.00 | 3.32 | 3.59 |
| Phi-3-medium | 3.62 | 3.61 | 3.66 |
| DeepSeek-Coder | 2.14 | 2.11 | 2.14 |
| CodeLlama | 2.97 | 3.46 | 2.06 |

The paper highlights GPT-4-Turbo’s **1.57-step** SWDE average versus Phi-3-medium’s **3.62**, arguing that capable models find accurate XPath expressions in deeper pages with fewer pruning rounds. However, the detailed tables show that sequence length is not perfectly ordered by overall model strength—for example, DeepSeek-Coder and CodeLlama have unusually short averages on some datasets.

### 4.11 XPath fragility

XPath expressions become fragile when they depend on page-specific text instead of stable shared characteristics. The manually calculated bad-case rates were:

| Model | `contains` predicate | exact-equality predicate |
|---|---:|---:|
| GPT-4 | 0.61% | 2.90% |
| GPT-3.5-Turbo | 9.33% | 9.78% |
| Gemini Pro | 10.62% | 14.29% |
| Mixtral 8×7B | 12.88% | 8.55% |
| DeepSeek-Coder | 11.63% | 7.55% |
| CodeLlama | 18.75% | 14.29% |
| Mistral 7B | 18.18% | 33.33% |

The table names “GPT4” and “Mistral 7B,” whereas the main model list uses GPT-4-Turbo and Mixtral 8×7B; the exact intended correspondence is not clarified.

Table 14 contrasts:

- A good XPath anchored to common text such as “Height:” and a shared class; and
- A bad XPath hard-coded to the seed page’s exact phone number.

Even the strongest model retained some fragility, so fully reliable LLM-generated XPath remained unsolved.

### 4.12 Figures 2 and 4: Why AutoScraper differs from COT and Reflexion

**Figure 4** uses the instruction “What’s the average point of James Harden?”:

- COT makes a single attempt and selects an incorrect basketball statistic.
- Reflexion notices failure and regenerates, but it continues operating on the full complex page.
- AutoScraper moves back to a broader page region and then descends again to identify the correct PPG value, shown as **17.1** in the final extraction.

The figure and accompanying discussion emphasize that COT uses one turn, Reflexion can revise after failure, and AutoScraper both revises and structurally simplifies the DOM between attempts.

### 4.13 Error analysis

Two recurring failure modes were identified:

1. **Non-generalizable layouts:** Pages from the same site may place the same attribute in different DOM locations. On CareerBuilder, most pages contained a normal company-name field, but one represented the value as “Not Available” in another node.
2. **Multi-valued attributes:** Addresses, university phone numbers, and similar attributes may occur in several page regions. AutoScraper can retrieve some values but may fail to construct one action sequence that captures all of them.

No statistical significance tests or confidence intervals were reported.

## 5. Analysis and Interpretation

The experiments support the three research questions as follows:

- **Performance:** AutoScraper usually increased the proportion of fully correct scrapers and sharply reduced unexecutable cases relative to COT and Reflexion. Its strongest configuration established the paper’s best zero-shot result and surpassed the compared supervised systems.
- **Component value:** Progressive DOM traversal provided benefits even without synthesis and even when correct target values were supplied. Synthesis further improved cross-page stability by testing candidates on multiple seed pages.
- **Practicality:** Scraper generation has a substantial upfront cost, but reusable execution is much faster than repeated LLM extraction. The framework becomes advantageous once a site has roughly 19.5 pages on average under the reported GPT-4-Turbo measurements.

The authors attribute AutoScraper’s gains to its explicit use of the HTML hierarchy. Rather than repeatedly asking the LLM to solve the same full-page problem, it converts a failed attempt into a smaller, more relevant subtree. Synthesis then guards against rules that accidentally depend on one page.

The results also distinguish **content understanding** from **structural understanding**. Smaller LLMs often extracted values well when asked directly but struggled to write executable XPath. The golden-label and action-length experiments reinforce the interpretation that DOM understanding is a key bottleneck.

The executability evaluation changes the interpretation of system quality. High traditional precision can coexist with many empty or non-running scrapers. Correct and Unexecutable rates expose that failure more directly.

## 6. Contributions and Novelty

The paper’s principal contributions are:

- It formulates **LLM-based web scraper generation** as an action-sequence generation task.
- It proposes **AutoScraper**, combining LLM adaptability with the repeatability of rule-based extraction.
- It introduces a **progressive top-down/step-back algorithm** that uses the DOM hierarchy to reduce page complexity after failed XPath attempts.
- It introduces **cross-page synthesis**, selecting among candidate sequences based on results from multiple pages.
- It proposes an **executability metric** with six outcome categories to measure reliability across complete website-level cases.
- It evaluates eight LLMs, three datasets, two agent baselines, direct extraction, and five supervised systems.
- It provides evidence that zero-shot GPT-4-Turbo + AutoScraper can surpass the compared supervised SWDE systems.
- It quantifies when reusable scrapers become faster than repeated direct LLM extraction.
- It analyzes action-sequence length, seed-page scaling, XPath fragility, and common errors.
- The implementation is reported as open source.

## 7. Limitations and Caveats

The authors explicitly acknowledge that:

- AutoScraper is restricted to **vertical web-page information extraction**. It does not readily transfer to broader interactive web environments such as Mind2Web or WebArena.
- Performance depends strongly on the **backbone LLM’s HTML and DOM understanding**.
- Different pages on the same site can still use incompatible structures.
- Multi-valued information remains difficult to capture comprehensively.
- XPath expressions may be fragile when they contain seed-page-specific text.
- Adding seed pages has diminishing returns and cannot improve performance indefinitely.
- Direct extraction remains better than AutoScraper for seven of the eight tested models; scraper generation overtakes it only with GPT-4-Turbo in the reported comparison.
- Open-source and smaller models have high unexecutable rates and are not yet dependable for this task.
- Ambiguous task descriptions reduce performance.
- All experiments were zero-shot because of model context limits.
- DS1 permits only one inference page, so the synthesis module could not be tested there.
- Wrapper generation is slow for small workloads; its efficiency advantage appears only after enough pages are processed.

Additional cautions evident in the supplied paper include:

- No statistical significance testing, variance, or confidence intervals are reported.
- The supervised comparison is explicitly described as unequal because the supervised systems used one training site while AutoScraper was zero-shot.
- Some source details are internally inconsistent: DS1 is described as having 166 pages while Table 1 reports 186, and the efficiency text mentions ten domains while the accompanying table lists eight.
- The detailed Extended SWDE results contain some exceptions to the broad statement that AutoScraper always beats both baselines on every measure.
- Public datasets were anonymized, but the authors cannot guarantee that they contain no harmful or toxic language.
- Human annotations were used only in early feasibility research, not evaluation. Annotators consented, were protected, and were compensated according to local standards.

## 8. Future Work or Open Questions

The paper explicitly identifies improving LLM **HTML understanding** as future work, including:

- Collecting better HTML-focused corpora;
- Developing training strategies for hierarchical webpage understanding; and
- Reducing dependence on increasingly powerful backbone models.

Other unresolved questions demonstrated by the experiments are:

- How to generate XPath rules that remain reliable under intra-site layout changes;
- How to extract all values for multi-valued attributes;
- How to avoid text-specific and exact-value XPath predicates;
- How to extend the approach beyond vertical information extraction to general web-agent environments;
- How to select enough seed pages for strong generalization without unnecessary generation expense; and
- How to make scraper generation practical with smaller or open-source models.

## 9. High-Level Takeaway (Plain Language)

AutoScraper asks an LLM to build a reusable extraction program instead of asking it to reread every webpage. When its first rule fails, it narrows the webpage step by step, learns from the failure, and tests several candidate rules across multiple pages. With GPT-4-Turbo, this produced the paper’s best accuracy—**88.69 F1 with 71.56% fully correct and only 4.06% unexecutable cases on SWDE**—and became faster than repeated direct LLM extraction after about **19.5 pages on average**. The approach is promising for large collections of similar pages, but reliability still depends heavily on the LLM, and changing layouts, multiple target values, and fragile XPath rules remain important unsolved problems.