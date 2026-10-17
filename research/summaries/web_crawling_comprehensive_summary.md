## Stage 0 — Document Accessibility Report

The supplied work is **Web Crawling**, by Christopher Olston and Marc Najork, published in *Foundations and Trends in Information Retrieval*, volume 4, number 3, 2010, pp. 175–246; DOI: 10.1561/1500000017. It is a technical narrative survey, not a security experiment comparing web AI agents with standalone large language models (LLMs).

The main document is available as extracted text for physical PDF pages 1–74. The supplied sequence includes contents, abstract, main sections 1–8, and references [1]–[121]. No numbered physical page is absent from this supplied sequence. This establishes coverage of the supplied sequence, not independent verification against the publisher's original file. Printed journal pagination and physical PDF pagination differ: physical p. 4 is printed p. 176, and physical p. 74 is printed p. 246. All source locators below use **physical PDF pages**, with section or figure numbers added for clarity.

Direct visual inspection is possible for 27 supplied images: physical pp. 1, 3, 6, 8, 10, 12, 13, 14, 16, 18, 20, 23, 26, 29, 30, 32, 34, 39, 42, 50, 51, 53, 58, 59, 62, 71, and 73. Other pages are reviewed through supplied text only. Figures 2.1, 3.1, 3.2, 4.1, 4.2, 7.1, 7.2, and 7.3 are all visually available. The table-like figures are readable; Figure 3.2 is rotated, so its checkmarks require particular care. Mathematical extraction contains damaged summation and integral formatting, but the principal expressions can be identified from their surrounding definitions. No independent optical character recognition was performed or required. No tools or external sources were used.

No appendix is present in the supplied contents or page sequence. The accessibility metadata reports no embedded files and detects no supplementary references; the supplied text does not identify a missing supplement. Referenced research papers, implementations, datasets, and linked websites were not independently supplied or reviewed. Their results are therefore represented as **this survey's reports of prior work**.

Evidence labels used throughout: **[A] Author-reported** means stated in the supplied work, including its summaries of cited studies; **[B] Directly observable** means visible in a supplied image; **[C] Analyst-derived** means calculated from supplied information; **[D] Analyst interpretation** means an explicitly identified inference. No [E] external information is introduced. Confidence is HIGH for clearly readable statements and diagrams, MEDIUM for bounded interpretations or ambiguous mappings, LOW for speculative transfer, and UNKNOWN where the document supplies no evidence.

## 1. Plain-language orientation

[A] A web crawler automatically downloads pages, extracts their links, and repeats the process. Search engines use crawlers to assemble searchable collections, archives use them to preserve historical copies, and monitoring or mining services use them to discover relevant information. The apparent simplicity hides a resource-allocation problem: the web is too large and changes too quickly for a crawler to collect everything and keep every copy current. It must decide what to visit, when to return, how to store its state, and what to avoid (pp. 4–7).

[A] Olston and Najork synthesize systems designs, mathematical models, empirical studies, and adversarial-content research. Their central contribution is an organized account of how architecture, coverage, freshness, and content selection interact. They do not introduce a single new crawler with one controlled evaluation. Findings include the usefulness and limits of PageRank-based ordering, the need for exploration in topical crawling, and the striking dependence of refresh policies on the chosen definition of freshness (pp. 30–52).

[A] The security-related material concerns misleading content, spam, crawler traps, cloaking, and script-driven redirection. A content provider can influence what the crawler sees and where it goes. Some harmful effects also arise unintentionally: an innocent calendar can generate an unbounded URL chain, and an overly aggressive crawler can overload a server (pp. 6, 54–57).

[D] For the user's question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, the defensible contribution is indirect. The survey documents an external environment whose content, links, representations, and apparent relevance can be manipulated. This can inform hypotheses about the additional exposure of systems that interact with that environment. It supplies no comparison with standalone LLMs, no prompt-injection experiments, and no measured increase in agent vulnerability. Comparative confidence is UNKNOWN; relevance as background on adversarial web interaction is MEDIUM.

## 2. Document roadmap

The document inventory consists of the following substantive sections and subsections. The ranges identify where each topic appears in the supplied physical pages.

| ID | Original section | Physical pages | Function |
|---|---|---:|---|
| S1 | 1 Introduction; 1.1 Challenges; 1.2 Outline | 4–7 | Uses, decentralized acquisition, scale, selection, politeness, adversaries |
| S2a | 2.1 Chronology | 8–11 | Historical systems and implementation lessons |
| S2b | 2.2 Architecture Overview | 12–13 | Distributed crawler pipeline and Figure 2.1 |
| S2c | 2.3 Key Design Points | 13–21 | State, queues, duplicate elimination, caches, distribution, incremental operation |
| S3a | 3.1 Model; 3.1.1 Limitations | 23–25 | Abstract crawl ordering and deviations from actual systems |
| S3b | 3.2 Web Characteristics | 25–30 | Static structure, duplication, site and page evolution |
| S3c | 3.3 Taxonomy of Crawl Ordering Policies | 30 | Coverage/freshness objectives and importance/relevance/dynamicity factors |
| S4a | 4 Batch Crawl Ordering; 4.1 Comprehensive Crawling; 4.1.1 Search Relevance | 31–36 | Weighted coverage and general-purpose ordering |
| S4b | 4.2 Scoped Crawling; 4.2.1 Topical Crawling; Greediness; Adaptivity | 36–41 | Targeted acquisition, exploration, learning, adaptive agents |
| S4c | 4.3 Efficient Large-Scale Implementation | 41–42 | Deferred updates and online importance approximation |
| S5a | 5 Incremental Crawl Ordering; 5.1 Maximizing Freshness | 43–49 | Coverage/freshness tradeoffs, estimation, allocation, scheduling |
| S5b | 5.1.1 Binary Freshness; 5.1.2 Continuous Freshness | 46–50 | Obsolescence, age, content overlap, information longevity |
| S5c | 5.2 Capturing Updates; 5.3 Efficient Large-Scale Implementation | 50–52 | Event capture, timeliness, buckets, optimization |
| S6 | 6.1 Redundant Content; 6.2 Crawler Traps; 6.3 Web Spam; 6.4 Cloaked Content | 53–57 | Waste, manipulation, detection, and execution differences |
| S7 | 7.1 Types; 7.2 Problem Overview; 7.3 Content Extraction | 58–63 | Form-based access, source selection, adaptive query discovery |
| S8 | 8 Future Directions | 64–66 | Tuning, retirement, integration, scripts, personalization, collaboration |
| REF | References [1]–[121] | 67–74 | Bibliographic provenance, not independently verified studies |

The eight substantive figures are F2.1, F3.1, F3.2, F4.1, F4.2, F7.1, F7.2, and F7.3. Three are tables presented as numbered figures. Major mathematics includes weighted coverage, a PageRank coverage bound, weighted freshness, its long-run average, refresh-budget constraints, binary freshness, Poisson change rates, age, and weighted content overlap. No standalone numbered algorithm block, theorem/proof sequence, appendix, or supplementary artifact is supplied. The inventory also includes substantive footnotes about virtual hosting, model qualifications, PageRank measurement, fragment definitions, reputation changes, and deep-web query assumptions.

## 3. Background and context

[A] The web is described as a federated information repository: independent providers publish content using shared protocols without a central manager. Transmission Control Protocol (TCP) supports communication; Domain Name Service (DNS), in the paper's terminology, resolves host names; Hypertext Transfer Protocol (HTTP) transfers pages; Hypertext Markup Language (HTML) encodes pages and hyperlinks. The robots exclusion protocol communicates which resources a crawler should avoid (pp. 5, 19–20).

[A] A **pull model** means an aggregator actively requests content. A **push model** means providers send information or notifications. The survey explains the predominance of pull through low entry barriers and the lack of an assumed trust relationship between arbitrary providers and aggregators. Sitemaps and feeds supply hints or hybrid mechanisms; this does not eliminate adversarial incentives (pp. 5–6, 66).

[A] A **frontier** stores URLs waiting to be downloaded. A **URL-seen test** or **duplicate URL eliminator** records discovered URLs so that the same address is not repeatedly admitted. These solve different problems: queueing future work versus remembering discovered addresses. Neither alone guarantees that different addresses do not contain identical material (pp. 14, 17, 53–54).

[A] **Coverage** measures acquired desired content; **freshness** measures how current stored copies remain. **Importance** estimates a page's value relative to others, often using PageRank. **Relevance** concerns the crawl's particular purpose. **Dynamicity** concerns change over time. A high score on one dimension does not imply a high score on another (pp. 22, 30).

[A] **Politeness** limits pressure on remote servers. **Breadth-first search** visits pages in discovery order. **Scoped**, or in the topical case **focused**, crawling prioritizes a subset of the web. **Deep web** here means content accessed through form submissions; it does not denote a separate security category (pp. 14–16, 36–39, 58–61).

## 4. Research problem and gap

[A] The existing problem is selective acquisition from an enormous, evolving, partly adversarial repository. Download capacity, memory, disk access, storage, and per-site request rates constrain the crawler. The paper treats the discoverable web as effectively infinite because new and dynamically generated content continually expands the space (pp. 6, 22).

[A] Previous approaches have different shortcomings. A simple first-in-first-out queue can create long runs of requests to one server. Disk-backed random lookups can bottleneck duplicate checking. Purely greedy relevance decisions can miss useful pages behind irrelevant intermediates. Frequent global priority recomputation can be impractical. Optimizing one freshness measure can perform poorly against another objective (pp. 14–19, 39–42, 47–50).

[A] The survey identifies a larger integration gap: specialized techniques are much better studied than their combination into a unified crawler. Theoretical ordering models assume freedoms that actual disk-based systems do not possess. Page retirement, parameter selection, script-generated content, and deep-web extraction remain incompletely studied in the literature surveyed (pp. 25, 30, 64–66).

[A] Its scope spans conventional link traversal, continuous refreshing, unwanted content, and form-based retrieval. It is not a systematic review with reported database queries, screening counts, eligibility rules, or a study-quality scoring procedure. Those details are not specified; no search protocol should be reconstructed from the bibliography alone.

## 5. Research questions / objectives / hypotheses

[A] No formal numbered research questions or statistical hypotheses are stated. The abstract's objectives are to outline fundamental challenges, describe models and solutions, and highlight future work (p. 3). The outline identifies five organizing objectives: scalable architecture; traversal order; revisitation scheduling; avoidance of problematic content; and deep-web access (p. 7).

For traceability, these are represented as informal objectives O1–O5, rather than invented author questions:

| ID | Objective | Relevant evidence |
|---|---|---|
| O1 | Explain efficient, robust, scalable crawling | §§2, 4.3, 5.3 |
| O2 | Explain ordering for useful coverage | §§3–4 |
| O3 | Explain refreshing and update capture | §5 |
| O4 | Explain avoidance of wasteful or misleading content | §6 |
| O5 | Explain discovery and extraction behind forms | §7 |

[D] The user's LLM-security question is a separate analytical lens, not an objective of the paper. A cautious question that this survey can inform is: which externally controlled features can influence an automated web acquisition system? It cannot establish why one modern model configuration has a higher attack-success rate than another.

## 6. Assumptions / threat model

[A] The crawl-ordering abstraction assumes freely reorderable frontier URLs, identical page download durations, and a constant crawl rate. Batch crawling downloads a page at most once per batch; incremental crawling permits repeated visits and conceptually continues indefinitely (pp. 23–24).

[A] Freshness optimization commonly fixes the page set and assumes a stationary stochastic change pattern. Binary-freshness analyses use a Poisson process with page-specific rate λ(p), representing random independent change events. Alternative work relaxes independence or avoids assuming a fixed evolution model in advance (pp. 45–49).

[A] The deep-web graph model assumes that any data value can be queried, while explicitly acknowledging that real interfaces may restrict fields. It excludes multi-value queries. Query cost is modeled as linearly proportional to the number of returned items, and the underlying graph begins only partially known (pp. 61–62).

[A] There is no unified formal security threat model. Section 6 describes providers who can create content, links, large URL spaces, and different responses for different clients. Motivations include ranking manipulation and commercial traffic. Cloaking can distinguish requests using User-Agent headers or IP addresses. Redirection can exploit differences between browser execution and crawler processing (pp. 54–57).

[D] Protected interests implied by these discussions include collection usefulness, ranking integrity, crawl resources, and server availability. These are analyst-organized categories, not a formal asset list supplied by the authors. The paper does not specify LLM instruction hierarchies, model permissions, secret-bearing tools, or attacker capabilities against such components. Those elements remain outside its evidentiary scope.

## 7. Methodology

[A] The method is narrative technical synthesis. The authors explain representative architectures, abstract optimization problems, and findings of cited theoretical and empirical studies. They do not present a new common dataset, shared benchmark, pooled effect-size analysis, or unified statistical experiment. Search databases, query strings, screening procedures, quality appraisal, and publication-bias assessment are not reported.

**Architecture.** A worker obtains a URL from the frontier according to priority and politeness. The HTTP fetcher uses DNS resolution and checks robots exclusions. Downloaded HTML goes to a link extractor; extracted URLs go to a distributor that assigns responsibility, usually using host, domain, or IP information. A custom filter excludes unwanted addresses; duplicate elimination admits new addresses; a prioritizer puts them into the frontier. Distributed processes exchange URLs that belong to another process. Incremental crawlers also return fetched URLs to future scheduling (pp. 12–13, 20–21).

**State and storage.** The frontier must retain actual URLs and select future work. The seen set can retain compact hashes, with a 10-byte hash offered as an example. On disk, sequential processing is preferred over random seeks. Mercator batches membership tests and merges sorted hashes. IRLbot uses disk-resident batches to amortize merge costs over more URLs. An alternative sparse on-disk layout updates relevant blocks and doubles the file when a block fills (pp. 17–19). These are architectural alternatives, not one jointly evaluated implementation.

**Politeness and priorities.** Mercator separates a front queue from server-specific back queues. Back queues have eligibility times and are selected through an in-memory priority queue. The text describes typically three back queues per crawling thread and a typical delay parameter of 10. A separate design choice discretizes priorities into approximately 10–100 levels to permit practical disk queues (pp. 15–17). Host-name grouping can miss shared physical servers under virtual hosting; the footnote proposes IP-based grouping while acknowledging DNS cost (p. 15).

**Ordering methods.** Comprehensive crawling uses discovery order, incoming-link counts, estimated PageRank, site-size priorities, or expected search impact. Scoped crawling estimates topic relevance using URLs, anchor text, surrounding text, classifiers, topic taxonomies, and hub structure. Adaptation may learn signal combinations or evolve populations of independent crawling agents (pp. 33–42). The term agent in this historical crawling discussion does not identify an LLM agent.

**Refreshing.** The survey separates model estimation, resource allocation, and scheduling. Estimation uses past snapshots, uneven sampling corrections, page features, or related pages. Allocation assigns a finite total crawl rate among pages. Scheduling aims to realize those rates, preferably with approximately uniform spacing for each page. Practical bucket implementations group pages by change rate, importance, or other model attributes and optimize at bucket granularity (pp. 45–52).

**Unwanted content and deep web.** The methods include URL normalization, duplicate detection, site budgets, spam classification, response comparison, bounded script evaluation, form selection, domain interpretation, seed-value collection, and repeated query/result expansion (pp. 53–63). No train/validation/test split, random seed, universal hyperparameter set, statistical significance threshold, or reproduction package is supplied for the survey as a whole.

## 8. Experiments / analyses

The following register separates distinct analyses reported in the survey. They are not new experiments jointly conducted for this paper.

| ID | Analysis and purpose | Setup / comparisons | Results and limits |
|---|---|---|---|
| X1 | Historical crawler scale | Different published systems and deployment settings, pp. 9–11 | Mercator: 891 million pages in 17 days on four machines; Polybot: 120 million in 18 days on four machines. Different workloads preclude a controlled performance ranking. |
| X2 | Web structure and duplication | Broder studies; 30-million-page AltaVista corpus for duplication, p. 26 | 29% more than 50% similar to another page; 11% exact duplicates. These are corpus-specific reported findings. |
| X3 | Site evolution and discovery | Studies summarized as averages across sites, p. 27 | New pages 8% per week; new links 25% per week; 80% of pages and links disappear over a year; carefully chosen old pages can expose 90% of new pages. |
| X4 | Batch ordering under PageRank weights | Three studies listed in Figure 4.2, pp. 34–35 | Breadth-first is strong early with good seeds; PageRank performs well; indegree results disagree. Dataset and time differences qualify synthesis. |
| X5 | Search-oriented crawl effectiveness | Four ordering policies; MaxNDCG and click count, pp. 35–36 | PageRank is reported most reliable/effective; per-domain limits help. No effect sizes are supplied here. |
| X6 | Focused crawling | General versus topical crawlers; different starting seeds, p. 39 | Topical crawling stays in scope; independent crawls substantially overlap. Exact overlap and uncertainty are not reported. |
| X7 | Greediness control | Distance estimates and delayed reordering, pp. 39–40 | Less greedy policies improve long-run weighted coverage; optimal greediness is unknown. |
| X8 | Freshness policy analysis | Binary Poisson model with equal page weights, pp. 46–49 | Uniform allocation exceeds proportional allocation; optimal binary policy can ignore very fast-changing pages. Age-based objectives change the result. |
| X9 | Update capture | Weighted captured updates; uniform/proportional baselines, pp. 50–51 | A specialized allocation algorithm empirically outperforms both; a later timeliness-aware algorithm has a reported formal guarantee. Neither magnitude nor guarantee formula is reproduced. |
| X10 | Duplicate URL rules | Generalized DUST normalization, pp. 53–54 | Regular-expression rules reportedly triple detected duplicate URLs; absolute counts and evaluation configuration are absent here. |
| X11 | JavaScript redirection | Pages already identified as employing JavaScript redirection spam, p. 57 | About half use eval to obfuscate targets or scripts. This is not a prevalence estimate for all web pages. |
| X12 | Deep-web query selection | Greedy frequency, overlap avoidance, unseen-item estimation, pp. 62–63 | Adaptive traversal is motivated; no common numerical comparison is supplied. |

[A] No confidence intervals, significance tests, repeated-run counts, or standardized hardware descriptions accompany most of these survey-level summaries. Their absence limits numerical comparison; it does not establish that the underlying cited studies lacked them.

## 9. Results

[A] **Architecture must accommodate both scale and remote constraints.** Splitting the frontier from the seen set permits specialized structures. Sequential disk processing avoids the cost of random seeks, but batching delays URL admission. Politeness prevents concentrating too many requests on a host and can constrain completion when very large sites remain late in a crawl (pp. 14–20, 35).

[A] **Ordering performance depends on the objective and stage of the crawl.** Under PageRank-weighted coverage, breadth-first crawling with high-PageRank seeds is effective early; PageRank prioritization works well across the crawl. Periodic recomputation alone can perform poorly, whereas an online approximation performs well. Indegree findings conflict across collections. Site-size priority can help late under per-site constraints (pp. 34–35). No exact gain is reported.

[A] **Relevance-driven exploration works, but excessive greediness can fail.** Useful pages may be separated by irrelevant ones. Relevance propagation, distance estimation, and delayed reordering preserve exploration. The survey reports improved long-term coverage but does not identify an optimal universal exploration parameter (pp. 39–40).

[A] **Refresh-rate intuition is conditional.** With equal weights and binary freshness under the stated Poisson framework, refreshing in proportion to change rate is inferior to uniform allocation. The optimal policy may abandon extremely fast-changing pages. With an age penalty that grows without bound, abandonment is no longer suitable. With content-based freshness, the longevity of changed material matters in addition to frequency (pp. 47–49).

[A] **Capturing every update differs from maintaining a current cache.** Rapidly overwritten material is difficult to keep continuously fresh, yet it is urgent to capture before disappearance when historical event capture is the objective (p. 50). This is an objective-dependent reversal, not an inconsistency.

[A] **Unwanted content has multiple mechanisms.** Different addresses can duplicate content; traps can consume resources; spam can distort selection and ranking; cloaking changes observations according to client identity; script-based redirection changes what a browser ultimately displays (pp. 53–57). These are separate failure modes with different detection requirements.

[D] The security synthesis is that useful automation must evaluate the acquisition process as well as acquired text. This is an interpretation of the crawler evidence. The paper supplies no direct numerical result about LLM behavior, comparative vulnerability, or success of an LLM-specific defense.

## 10. Figure-by-figure interpretation

### Figure 2.1 — Basic crawler architecture, physical p. 13

[B] Two tall process containers repeat the same pipeline: DNS resolver/cache, HTTP fetcher, link extractor, URL distributor, custom URL filter, duplicate URL eliminator, URL prioritizer, and frontier. Arrows identify host names, IP addresses, HTML pages, and URLs. Cross-process arrows connect URL distributors to the other process's filtering path. A loop returns frontier work to fetching. External DNS and web servers communicate with their respective components. This is a flow diagram, with no axes, units, error bars, or quantitative scale. It supports the architecture account on p. 12. It does not depict a complete security boundary or a browser execution engine.

### Figure 3.1 — Crawl ordering model, physical p. 23

[B] A web cloud sits above a page downloader, crawl-ordering policy, and page repository. A sequence is split into crawl history and planned crawl order, with a crawl-rate arrow showing progression. Repeated page identifiers in the planned sequence illustrate revisitation. The repository informs ordering, which controls future downloads. This is an abstract diagram, not measured timing data. The constant-rate and equal-duration assumptions are supplied by the adjacent text.

### Figure 3.2 — Taxonomy of crawl ordering techniques, physical p. 29

[B] A rotated matrix lists techniques against two objectives, coverage and freshness, and three factors, importance, relevance, and dynamicity. Checkmarks indicate which dimensions the survey associates with each technique. Blocks distinguish initial acquisition, refresh-oriented methods, and combined approaches. There are no numerical performance values. The nearby §3.3 explains why a broad technique need not outperform a specialized one on a particular objective. Full row interpretation is provided in section 11.

### Figure 4.1 — Hypothetical weighted coverage curves, physical p. 32

[B] The horizontal axis is elapsed time t and the vertical axis is WC(t). No numeric ticks or units beyond these symbolic labels are given. Curves are labeled omniscient, random, A, and B. The random baseline is approximately linear. The omniscient curve rises fastest. A leads B early, while B overtakes later. [A] The text explicitly identifies these curves as hypothetical. They demonstrate horizon-dependent policy choice; no area, crossover time, percentage improvement, or measured dataset result can be extracted.

### Figure 4.2 — Empirical studies of batch ordering, physical p. 34

[B] This is a four-column table, not a performance graph. It identifies three studies, their collections, size notation, and publication years. Superscripts are visually legible: 10^5, 10^8, and 10^6. It provides provenance for a qualitative synthesis, not scores establishing a best method. Its values are reproduced in section 11.

### Figure 7.1 — Deep-web taxonomy, physical p. 59

[B] A two-by-two matrix crosses content structure with query-interface structure. Examples are a simple-search news archive, product review site, advanced-search news archive, and online bookstore. There are no numeric axes or results. [A] The footnote says the structured/unstructured distinction is actually a continuum simplified into a binary classification.

### Figure 7.2 — Unstructured deep-web content graph, physical p. 62

[B] Keyword vertices cough, sneeze, and cancer connect to documents Cold Symptoms and Smoking Effects. Cough connects to both documents; sneeze connects to Cold Symptoms; cancer connects to Smoking Effects. The drawing illustrates overlap among query result sets. It has no numerical edge weights, probability encoding, or experimental dataset claim.

### Figure 7.3 — Structured deep-web content graph, physical p. 62

[B] Record-element vertices include A Farewell to Arms, 1929, Hemingway, For Whom the Bell Tolls, and 1940. They connect to the corresponding two book-record vertices; Hemingway connects to both. The example shows that a shared field value can retrieve multiple records and reveal additional query values. It is a conceptual example, not measured extraction performance.

## 11. Table-by-table interpretation

The document numbers its substantive tables as figures. They are audited here without inventing separate original table numbers.

**Figure 3.2 matrix.** [A/B] The rows organize breadth-first search; indegree, PageRank, site-size, spawning-rate, and search-impact priorities; scoped crawling; obsolescence, age, incorrect-content, embarrassment, and search-impact refresh objectives; update capture; WebFountain; and OPIC. Coverage-only methods occupy the first group. Freshness methods occupy the second, while WebFountain and OPIC combine coverage and freshness. Importance is associated with many ranking and refresh techniques, relevance with scoped/search-oriented techniques, and dynamicity with evolution and revisitation. This is a categorical coding of the literature. Checkmarks do not indicate effect sizes, statistical significance, equal implementation cost, or verified superiority. The rotated image and text extraction were compared; the output compresses individual checkmark combinations rather than inventing a performance ranking.

**Figure 4.2 study table.**

| Study | Dataset | Data size as printed | Publication year |
|---|---|---:|---:|
| Cho et al. [43] | Stanford web | 10^5 | 1998 |
| Najork and Wiener [95] | general web | 10^8 | 2001 |
| Baeza-Yates et al. [9] | Chile and Greece | 10^6 | 2005 |

[B] The table labels the column DATA SIZE without an explicit unit in its cells; the surrounding discussion concerns web collections and page ordering. There are no best/worst scores, missing-value symbols, uncertainty estimates, or significance markers. [A] Najork and Wiener evaluated only breadth-first search. The survey warns that disagreeing indegree findings concern different collections, different sizes, and studies seven years apart (pp. 34–35).

**Figure 7.1 taxonomy table.**

| Query interface | Unstructured content | Structured content |
|---|---|---|
| Unstructured | News archive, simple search | Product review site |
| Structured | News archive, advanced search | Online bookstore |

[A/B] Rows describe how a user queries; columns describe how underlying content is organized. These dimensions are independent. Most surveyed work simplifies attention to the upper-left and lower-right cells. No baseline, ranking, sample count, statistical comparison, or extraction rate appears.

## 12. Diagram / architecture interpretation

[A/B] The operational path in Figure 2.1 is a repeated acquisition loop. The frontier outputs a selected URL; DNS translates its host; the fetcher requests a page subject to exclusion checks; the extractor turns HTML links into candidate URLs; the distributor sends each candidate to the responsible process; filtering and duplicate elimination reduce the work; prioritization determines future position. Multiple worker threads repeat this cycle. Cross-process messages transfer responsibility for URLs, rather than representing all pages passing through a single central server (pp. 12–13).

[A] Three control mechanisms have distinct roles. Politeness controls when an otherwise eligible URL can be requested. Custom filtering decides whether an address is acceptable for this crawl. Duplicate elimination decides whether the address has already been discovered. Prioritization orders accepted work. A high priority does not replace politeness, and URL novelty does not imply content novelty (pp. 12–20, 53–54).

[A/B] Figure 3.1 compresses this machinery into downloader, repository, and ordering policy. Its feedback loop makes historical observations consequential for future acquisition. Figure 7.2 and Figure 7.3 instead describe a discovery loop over hidden associations: query a known value, retrieve items, extract more values, and choose another query. Because the complete graph is unknown, planning adapts as content is revealed (pp. 61–63).

[D] For security research, these diagrams suggest examining where externally supplied observations influence subsequent requests or priorities. This is a hypothesis-generating reading. The diagrams do not demonstrate that source text can override an LLM's instructions, and they supply no policy enforcement design for an LLM system.

## 13. Equations and mathematical concepts

**E1 — Weighted coverage, p. 31, §4.** [A] WC(t) = Σ_{p∈C(t)} w(p). Here t is elapsed crawl time, C(t) is the set of pages acquired by then, and w(p) is the task-specific numeric weight of page p. The sum measures accumulated acquired value. For a helicopter-topic example, the authors assign 1 to relevant pages and 0 otherwise. With fixed crawl rate, |C(t)| is proportional to t. With nonnegative weights, coverage cannot decrease as pages are added. This is an objective, not a probability distribution unless weights are separately normalized.

**E2 — PageRank-weighted coverage and bound, pp. 32–33.** [A] One choice is w(p) = PR(p), with PR(p) the PageRank importance score. For PageRank biased toward a small trusted set T, breadth-first depth d from T gives WC ≥ 1 − α^(d+1), where α is the damping parameter. The guarantee is conditional on that specified biased-PageRank setting; it is not a universal guarantee for arbitrary relevance or every crawl. No α value is specified here. A footnote cautions that absolute PageRank values and rankings computed on a crawled subgraph require care.

**E3 — Politeness eligibility, p. 16.** [A] A server queue is reinserted with eligibility time t_now + k·x. The current time is t_now, x is the duration of the last download, and k is a politeness parameter, typically 10 in the description. The output is a future time when another URL may be processed. This relates request spacing to observed service duration. Queue selection favors the lowest eligibility time, waiting if necessary. It is an implementation policy, not an experimentally established universal optimum.

**E4 — Weighted freshness, p. 43.** [A] WF(t) = Σ_{p∈C(t)} w(p)·f(p,t), where f(p,t) is page freshness under a selected definition. Page importance and current synchronization both affect the total. Removed pages whose disappearance has not yet been detected receive a special freshness value, such as the minimum of the adopted scale.

**E5 — Long-run objective, p. 44.** [A] The time-averaged objective is WF_bar = lim_{t→∞} (1/t)∫_0^t WF(τ)dτ. The dummy variable τ is used here solely to distinguish integration time from the upper limit. This averages the weighted freshness trajectory over an indefinitely long interval. It is not a finite-run score reported for a new experiment.

**E6 — Crawl-budget allocation, p. 45.** [A] Σ_{p∈C} r(p) = r. The overall maximum crawl rate is r and the rate assigned to page p is r(p). The page set C is fixed for this simplified optimization. Allocation chooses rates; scheduling decides actual visit times. Under randomized scheduling the selection probability for p is r(p)/r (p. 46).

**E7 — Binary freshness and Poisson change, pp. 46–47.** [A] f(p,t) is 1 if cached and live copies are identical and 0 otherwise; near-identity may replace identity to ignore trivial changes. λ(p) is the average number of independent change events per time unit. Proportional allocation sets r(p) proportional to λ(p); uniform allocation sets r(p) = r/|C|. The reported superiority of uniform over proportional allocation applies to the equal-weight binary setting described, not every possible weighting or freshness measure.

**E8 — Age-based freshness, pp. 48–49.** [A] age(p,t) is 0 while copies match and otherwise the time a they have differed. Freshness is proportional to negative age. Older stale content receives a larger penalty. Since age can increase without bound, the optimal policy does not abandon pages as the binary objective can.

**E9 — Content-based freshness, p. 49.** [A] Pages are decomposed into fragments f1,…,fn with weights w(fi). Freshness uses weighted Jaccard set similarity between cached and live fragments. The supplied text describes the measure but does not print a full weighted formula; no additional formula is asserted here. The purpose is to measure incorrect content directly and account for the persistence of changes.

**E10 — Distance and deep-web optimization, pp. 40, 61–63.** [A] d(p)∈[0,∞) estimates links from a candidate page to relevant content. Smaller estimated distances receive priority. Deep-web extraction is formulated as weighted set cover: choose a minimum-cost collection of query values whose result sets cover content items. The graph is only partly known, so the classical fully known problem is not an exact description of the operational situation.

**Consistency warning.** [A] On p. 37, the text describes binary-weight WC as a fraction of crawled pages that are in scope. E1 without a denominator is a count of acquired in-scope pages when weights are 0/1. [C] A precision-like fraction would be WC(t)/|C(t)| when |C(t)| is nonzero. This is an explicit analyst derivation and a terminology/formula tension, not a silently repaired author equation. At a common fixed crawl budget, count and fraction induce the same ranking, but their numerical values and units differ.

## 14. Interpretation and discussion

[A] The survey's recurring message is that a crawler must align implementation and optimization with purpose. An archive that wants every update, a search engine that wants currently useful results, and a topical collector do not necessarily need the same policy. Equal page weights, search-click weights, binary freshness, stale age, and content overlap express different definitions of success (pp. 31–52).

[A] The authors explicitly caution that the web-characteristics studies differ in size, scope, date, and method. They report disagreement about indegree prioritization rather than resolving it with a single universal conclusion. They also distinguish theory from implementability: a policy requiring frequent arbitrary reorderings may be difficult to realize with disk queues (pp. 25, 34–35, 65).

[A] Two additional reference issues merit disclosure. The chronology attributes IRLbot to Yan et al. on p. 11, while bibliography entry [84] on p. 72 lists H.-T. Lee, D. Leonard, X. Wang, and D. Loguinov. The supplied work does not resolve this attribution mismatch. Section 6.4 associates a cloaking-detection discussion with [117], while that bibliography entry is a structured-source query-selection paper also used in §7.3. The intended citation for the cloaking statement cannot be established here. These issues do not make the prose observations unreadable, but weaken exact bibliographic traceability.

[D] For the user's security question, the strongest grounded inference is environmental: automated web interaction adds dependence on externally authored representations and navigation structure. The paper illustrates deliberate manipulation of those dependencies. A claim that this makes web AI agents quantitatively more vulnerable than standalone LLMs requires an explicit comparator, attack definition, and evaluation not supplied here. The word more remains unproven by this source.

## 15. Contributions and novelty

[A] **Conceptual synthesis:** the paper connects coverage, freshness, importance, relevance, dynamicity, and unwanted content in one account. Figure 3.2 makes distinctions among objectives and inputs explicit.

[A] **Systems synthesis:** it explains scalable frontiers, seen sets, batching, caching, partitioning, and incremental state. These are reported designs and implementation lessons from the surveyed literature, not all novel mechanisms introduced by this survey.

[A] **Mathematical and methodological synthesis:** it organizes crawl ordering, refresh allocation, scheduling, and deep-web extraction as related but distinct optimization problems. Its value includes explaining why conclusions change when objectives change.

[A] **Research agenda:** it identifies unresolved tuning, retirement, integration, scripting, personalization, and collaboration issues. The paper does not claim a new dataset, benchmark, security attack suite, or head-to-head LLM result. The supplied work supports treating its central contribution as an explanatory survey and agenda, not a new empirical vulnerability measurement.

## 16. Limitations

### Authors' stated limitations

[A] The ordering model abstracts away heterogeneous download times, politeness constraints, parallel partial orders, content hazards, and repository retirement (pp. 24–25). Web-property evidence is heterogeneous across studies, warranting caution (p. 25). No consensus is reported for combining coverage and freshness or for the best freshness metric (pp. 44, 48). Optimal scoped-crawl greediness is unknown in the surveyed literature (p. 40). Direct trap detection has received little published attention (p. 55). Deep-web source selection and form-element selection remain difficult, while the query model excludes practical restrictions and multi-value queries (pp. 60–62). Theory-to-system integration needs more comprehensive empirical study (p. 65).

### Additional evidence-based analyst observations

[D] The survey gives no reproducible systematic-search protocol or quality grading. Many summarized results lack absolute effect sizes, uncertainty intervals, or sufficient configuration for reproduction from this document alone. Historical system-scale figures are not controlled comparisons. Some mathematics is described without full derivations. The supplied images cover all identified figures but only part of the page sequence. These are limits on this analysis and evidence reuse, not claims that the cited papers necessarily suffer the same omissions.

[D] Applicability to LLM security is indirect. The supplied work contains no standalone-model baseline, LLM-based browser agent, prompt-injection test, attack-success metric, model configuration, or comparative security result. Its 2010 publication context also limits treating time-sensitive system descriptions as present-day facts without external verification, which was neither requested nor performed.

## 17. Threats to validity

The following categories are analyst-organized observations, not headings or formal validity assessments claimed by the authors.

**Internal validity [D].** Different crawler histories, seeds, stopping times, and politeness constraints can affect observed policy performance. The survey does not supply a common controlled experiment that isolates all these causes.

**External validity [A/D].** The authors' explicit warning about heterogeneous web studies supports caution in generalizing numerical rates across sites or dates. Results from Stanford, general-web, and country collections need not transfer unchanged to other collections. Their relevance to modern LLM agents is a further untested transfer.

**Construct validity [A/D].** PageRank mass, query relevance, binary synchronization, stale age, and update counts measure different constructs. The WC count/fraction tension on p. 37 is especially relevant when reusing a metric definition. A freshness optimum cannot be interpreted as an update-capture optimum.

**Statistical conclusion validity [D].** Most survey summaries do not report uncertainty or significance. Statements such as performs well, substantially overlapping, and outperforms cannot be converted into precise effect sizes. About half in the JavaScript study remains approximate.

**Ecological validity [A/D].** Actual crawlers must operate with disk queues, parallel downloads, rate constraints, and changing content. Simplified free-reordering models can omit these operational costs. Script and personalized content create additional observational differences acknowledged in the future-work discussion.

**Reproducibility [D].** The bibliography supplies routes to underlying work, but this closed-document review cannot verify those artifacts, reconstruct missing experimental settings, or resolve the citation mismatches identified above. No comparative security experiment can be reproduced because none is supplied.

## 18. Future work and open questions

### A. Future work explicitly proposed by the authors

[A] The paper proposes better parameter tuning, especially scoped-crawler greediness; explicit retirement policies and decisions about retained metadata; holistic ordering across discovery and refreshing; reconciliation of theoretical policies with scalable implementations; improved deep-web crawling; vertical specialization using site syntax; crawling script-generated content; handling personalized content; and studying hybrid cooperation through Sitemaps, feeds, and pull mechanisms (pp. 64–66).

[A] Vertical crawling differs from scoped crawling: vertical approaches exploit structural patterns within particular sites or formats, while scoped crawling collects semantically coherent content across sites. The authors also ask how to handle content units that span pages or share a page, and whether personalized sites should be crawled as a generic user or through multiple profiles.

### B. Additional open questions logically remaining

[D] For the user's research, relevant untested questions include whether content manipulation changes an LLM agent's next action; whether client-specific responses produce different failure rates; how resource budgets interact with deceptive navigation; and how cached reputation should be treated after a site's ownership or content changes. These are analyst-generated questions grounded in analogous mechanisms in the survey. They are not author experiments, evidence of prompt injection, or recommendations validated for LLM deployments.

[D] A direct answer to comparative vulnerability would require specifying what standalone means, holding the underlying model and task constant where possible, defining adversarial success, and separating exposure from susceptibility and downstream consequence. The survey does not provide that design or its results.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this work |
|---|---|
| URL | Uniform Resource Locator: an address used to request a resource |
| HTTP | Hypertext Transfer Protocol: request/response mechanism used for pages |
| HTML | Hypertext Markup Language: page representation from which links are extracted |
| DNS | Domain Name Service in the paper's wording: resolves host names to IP addresses |
| TCP | Transmission Control Protocol: network communication protocol |
| Frontier | Collection of URLs waiting for future download |
| UST / DUE | URL-seen test / duplicate URL eliminator: discovered-address membership structure |
| FIFO | First-in-first-out: queue order follows insertion order |
| I/O | Input/output: reading, writing, or network transfer operations |
| MPI | Message Passing Interface: communication mechanism used by some distributed systems |
| Seed | Starting URL from which traversal begins |
| Politeness | Constraints intended to avoid excessive requests to a server |
| Batch crawl | A traversal without repeat pages inside the batch, potentially restarted later |
| Incremental crawl | Continuous mixture of new downloads and revisits |
| Scoped / topical crawl | Acquisition focused on a category / topic |
| PageRank | Link-based importance score used as a weight or priority |
| Indegree | Number of incoming links, here often estimated from already downloaded pages |
| Anchor text | Text associated with a hyperlink, used to estimate its destination's relevance |
| HITS | Named link-analysis algorithm used to identify hub pages; its expansion is not supplied |
| OPIC | Named online page-importance approach using propagated cash; not expanded in the supplied prose |
| DUST | Duplicate URL with similar text: normalization approach for address aliases |
| BEAST | Budget Enforcement with Anti-Spam Tactics: site-budget heuristic |
| SEO | Search engine optimization: influencing search visibility; not all SEO is spam |
| Cloaking | Serving different content to crawlers and human viewers |
| Redirection spam | Using redirection to make displayed content differ from crawler-observed content |
| Shingle | Content fragment/signature used for similarity; full construction is not given here |
| Churn / scroll | Replacing old content / appending new content |
| Deep web | Content accessed through form interfaces rather than only link following |
| Bipartite graph | Two classes of vertices, here query values and content items, connected across classes |
| NLP solver | Nonlinear problem solver in this paper, not natural language processing |
| WC(t), WF(t) | Weighted coverage and weighted freshness at time t |
| C(t), w(p), f(p,t) | Acquired page set, page weight, and page freshness |
| r, r(p), λ(p) | Total crawl rate, assigned page revisit rate, and page change rate |
| α, d, T | Damping parameter, breadth-first depth, and trusted seed set in the coverage bound |
| LLM | Large language model: part of the user's question, not an evaluated system in this paper |

[A] The supplied prose expands MaxNDCG using Normalized Distributed Cumulative Gain on p. 36. That wording is preserved as supplied rather than silently corrected using outside terminology. The metric is described operationally as a query-set gain score under optimal ranking; its complete mathematical definition is not reproduced.

## 20. Key numerical results

All author-reported values below are reports within this survey, often of cited studies. They are not fresh measurements by this analysis.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Early WebCrawler parallelism | 15 | downloader processes | Historical architecture | Author-reported | p. 9 |
| Internet Archive design scale | On the order of 100 million | URLs | Historical design target | Author-reported | p. 9 |
| Internet Archive concurrent sites | 64 | sites per process | Nonblocking I/O design | Author-reported | p. 9 |
| Original Google concurrency | About 300 | simultaneous downloads | Historical implementation | Author-reported | p. 10 |
| Original Google peak rate | About 100 | pages/s | Average page size 6 KB | Author-reported | p. 10 |
| Mercator crawl | 891 million | pages | 17 days, four machines | Author-reported | p. 10 |
| Polybot crawl | 120 million | pages | 18 days, four machines | Author-reported | p. 10 |
| WebFountain deployment | 48 | crawling machines | Reported deployment | Author-reported | p. 11 |
| UbiCrawler | About 10 million | pages/day | Five machines | Author-reported | p. 11 |
| IRLbot crawl | About 6.4 billion | pages | Ran over two months | Author-reported | p. 11 |
| Nutch demonstrated scale caveat | Not beyond 100 million | pages | As of cited report, not present-day limit | Author-reported | p. 11 |
| Mercator back queues | Typically 3× | queues per thread ratio | Implementation description | Author-reported | p. 16 |
| Politeness k | Typically 10 | multiplier | Delay based on last download duration | Author-reported | p. 16 |
| Discrete priorities | 10–100 | levels | Suggested implementation range | Author-reported | pp. 16–17 |
| Compact URL hash | 10 | bytes | Example representation | Author-reported | p. 17 |
| Disk bandwidth | 50–100 | MB/s | Historical discussion of modern disks | Author-reported | p. 18 |
| Duplication corpus | 30 million | pages | AltaVista collection | Author-reported | p. 26 |
| Near-duplicate share | 29% | pages | More than 50% similar to another page | Author-reported | p. 26 |
| Exact-duplicate share | 11% | pages | Same corpus | Author-reported | p. 26 |
| New page creation | 8% | per week | Averages across studied sites | Author-reported | p. 27 |
| New link creation | 25% | per week | Averages across studied sites | Author-reported | p. 27 |
| Page/link disappearance | 80% | over one year | Separate page and link observations | Author-reported | p. 27 |
| Discoverable new-page share | 90% | new pages | Small well-chosen monitoring sets | Author-reported | p. 27 |
| Typical small monitoring set | Five or fewer | old pages | Most sites; some require hundreds | Author-reported | p. 27 |
| Ordering-study sizes | 10^5; 10^8; 10^6 | collection sizes | Table does not explicitly print units | Visually readable | p. 34, Fig. 4.2 |
| Binary freshness example p1 | 0.5 | average freshness | One change/s and one revisit/s, randomized context | Author-reported | p. 47 |
| Binary freshness example p2 | 24/25 | average freshness | One change/day, one revisit/hour, randomized scheduling | Author-reported | p. 47 |
| Snapshot signatures | Two to five | recent snapshots | Typical compact estimation state | Author-reported | p. 51 |
| Generalized DUST detection | Tripling | detected duplicate URLs | Absolute baseline not supplied | Author-reported | p. 54 |
| eval use | About half | studied pages | Pages employing JavaScript redirection spam | Author-reported | p. 57 |

[A] Additional historical magnitudes include over 1,500 operating crawlers (p. 5), over one million deep-web sites in a cited study (p. 26), sub-hourly through annual page-change scales (pp. 27–28), and extracting small amounts from millions of sites in Google's deep-web approach (p. 63). These are scope descriptors, not current verified counts. No throughput ratios are calculated across different systems, and no approximate graph coordinates are promoted to numerical results.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Crawling involves more than breadth-first traversal | Systems and theoretical challenges stated in abstract | Survey framing | p. 3 | Explicit; HIGH |
| Remote content providers can have adversarial incentives | Misleading corpus injection and financial motivation | S1 | pp. 6–7 | Explicit general statement; HIGH |
| Retrieved pages influence subsequent crawl work | Link extraction, distribution, filtering, prioritization loop | Fig. 2.1 | pp. 12–13 | Text and visual agree; HIGH |
| Abstract ordering omits operational constraints | Disk state, variable duration, parallelism, politeness | Model limitation register | pp. 24–25 | Explicit; HIGH |
| Empirical ordering results depend on collections and conditions | Three studies and conflicting indegree results | Fig. 4.2; X4 | pp. 34–35 | Qualitative synthesis; HIGH |
| Excessive topical greediness misses relevant content | Irrelevant intermediates and long-run findings | X6–X7 | pp. 39–40 | Mechanism and reported findings; HIGH |
| Fast-changing pages can receive zero optimal refresh rate | Equal-weight binary freshness analysis | X8; E7 | p. 47 | Strongly conditional; HIGH |
| Update capture needs different priorities from cache freshness | Overwritten events are urgent to capture | X9 | p. 50 | Explicit; HIGH |
| Traps can be benign or malicious | Calendar chain and spam examples | S6 | pp. 54–55 | Explicit mechanisms; HIGH |
| Cloaking creates identity-dependent observations | User-Agent/IP distinction | S6 | p. 56 | Explicit, citation mapping caveat; HIGH for text |
| Script obfuscation complicates static detection | About half of studied redirection pages use eval | X11 | p. 57 | Restricted sample; HIGH |
| Deep-web extraction is adaptive discovery | Partially known graph and weighted set cover | Figs. 7.2–7.3; X12 | pp. 61–63 | Model-based; HIGH |
| Paper explains an environment relevant to agent security | Adversarial acquisition and feedback mechanisms | Analyst synthesis | pp. 6, 12, 54–57 | Indirect transfer only; MEDIUM |
| Paper establishes greater LLM-agent vulnerability | No corresponding comparison supplied | None | Whole document | Unsupported; UNKNOWN |

## 22. Very simple explanation

A crawler is like an automated researcher following links through an enormous library that keeps changing. It cannot read everything, and it cannot constantly reread every page. It needs a plan for finding useful material, returning to important pages, remembering what it has seen, and avoiding overwhelming the people who run websites.

The best plan depends on the job. If the goal is a mostly current collection, spending every available request on pages that change every second may be wasteful. If the goal is to save every short-lived update, those same pages become urgent. Finding pages about one topic also requires some exploration, because useful pages can sit behind links that initially look irrelevant.

Some websites intentionally manipulate automated visitors. They can create huge chains of low-value pages, manufacture misleading links, show different content to different clients, or redirect a browser through scripts. This paper explains those crawler problems. It does not test an AI language model against them.

For the user's security question, the careful takeaway is that a system interacting with websites depends on material and behavior controlled by other parties. That supplies plausible additional places to investigate failures. This paper alone cannot tell us how much more vulnerable an LLM agent is, whether it is more vulnerable under a particular test, or which LLM-specific protection works.

## Completeness Audit

The denominator is the supplied 74-page document inventory, including all eight numbered figures, substantive subsections, mathematical models, reported analyses, and acknowledged gaps. Fully represented means the substantive function and main content are explained, not that every sentence is reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Contents, metadata, abstract | Yes, text and selected images | Yes | Fully represented | pp. 1–3 |
| §1; §§1.1–1.2 | Yes | Yes | Fully represented | Uses, pull/push, challenges, objectives |
| §2.1 Chronology | Yes | Yes | Represented in compressed form | Main architectures and numerical scale preserved; early chronology condensed |
| §2.2; Fig. 2.1 | Yes, text and visual | Yes | Fully represented | Pipeline and cross-process flow |
| §2.3 introductory state discussion | Yes | Yes | Fully represented | Seen set versus frontier |
| §2.3.1 Frontier/politeness | Yes | Yes | Fully represented | Queue design, delay, priorities, virtual-host caveat |
| §2.3.2 Seen test | Yes | Yes | Represented in compressed form | Hashes, caching, batching, sparse-block alternative |
| §2.3.3 Auxiliary structures | Yes, partly text only | Yes | Represented in compressed form | DNS/robots caches and expiration; detailed cache-policy prose condensed |
| §2.3.4 Distributed crawling | Yes | Yes | Fully represented | Partitioning, forwarding, peer-to-peer churn |
| §2.3.5 Incremental crawling | Yes, text only | Yes | Fully represented | Deletion, reentry, sketches, quality |
| §3.1; §3.1.1; Fig. 3.1 | Yes, figure visual | Yes | Fully represented | Assumptions and limitations |
| §3.2.1 Static characteristics | Yes | Yes | Fully represented | Bowtie reachability, seeds, duplicates, deep-web extent |
| §3.2.2.1 Site evolution | Yes, text only | Yes | Fully represented | Rates and monitoring-set qualifications |
| §3.2.2.2 Page evolution | Yes, text only | Yes | Represented in compressed form | Correlations, stationarity, churn/scroll, divergence |
| §3.3; Fig. 3.2 | Yes, text and visual | Yes | Represented in compressed form | All method rows identified; individual checkmark combinations condensed |
| §4 opening; Fig. 4.1 | Yes, figure visual | Yes | Fully represented | Objective and hypothetical curves |
| §4.1; §4.1.1; Fig. 4.2 | Yes | Yes | Fully represented | Policies, studies, search-oriented metrics, qualifications |
| §4.2; §4.2.1 | Yes | Yes | Represented in compressed form | Scope categories and generations of topical methods |
| §4.2.1.1 Greediness | Yes | Yes | Fully represented | Propagation, distance, delayed reordering, unknown optimum |
| §4.2.1.2 Adaptivity | Yes, partly text only | Yes | Represented in compressed form | Signal learning and evolutionary crawling agents |
| §4.3 Implementation | Yes | Yes | Fully represented | Deferred priorities and OPIC |
| §5 opening | Yes, text only | Yes | Fully represented | New versus old downloads, tradeoff, combined approaches |
| §5.1 estimation/allocation/scheduling | Yes, text only | Yes | Fully represented | Subproblems and spacing result |
| §5.1.1 Binary freshness | Yes, text only | Yes | Fully represented | Poisson assumption, conditional policy results, examples |
| §5.1.2 Continuous freshness | Yes, text only | Yes | Fully represented | Age, content overlap, longevity, search impact |
| §5.2 Update capture | Yes | Yes | Fully represented | Different objective, timeliness, reported guarantee |
| §5.3 Implementation | Yes | Yes | Fully represented | Snapshot state, FIFO buckets, bucket-level nonlinear optimization |
| §6.1 Redundancy | Yes | Yes | Fully represented | Shingling, DUST, mirrors, normalization placement |
| §6.2 Traps | Yes, text only | Yes | Fully represented | Benign/malicious causes, BEAST, sparse research |
| §6.3 Spam | Yes, text only | Yes | Fully represented | Categories, classification features, arms race, pipeline use |
| §6.4 Cloaking | Yes, text only | Yes | Fully represented | Legitimate variation, identity tests, redirects, eval, bounded execution |
| §7.1; Fig. 7.1 | Yes, text and visual | Yes | Fully represented | Four cells and continuum footnote |
| §7.2 Source discovery/selection | Yes, text only | Yes | Fully represented | Three-stage process |
| §7.3; Figs. 7.2–7.3 | Yes, diagrams visual | Yes | Fully represented | Four extraction steps, graph, assumptions, query strategies |
| §8 Future directions | Yes, text only | Yes | Fully represented | All listed directions accounted for |
| Informal objectives O1–O5 | Yes | Yes | Fully represented | No formal RQs or hypotheses manufactured |
| Analyses X1–X12 | Yes | Yes | Represented in compressed form | Separate conditions and missing configurations disclosed |
| Equations E1–E10 | Yes, text; selected visuals | Yes | Fully represented | Essential identities and model roles; absent derivations not invented |
| Algorithmic procedures | Yes | Yes | Represented in compressed form | No original numbered pseudocode blocks |
| Major contributions | Yes | Yes | Fully represented | Survey synthesis distinguished from cited inventions |
| Author-stated limitations | Yes | Yes | Fully represented | Kept separate from analyst concerns |
| Substantive footnotes | Yes | Yes | Represented in compressed form | Virtual hosting, PageRank, near-identity, fragments, reputation, form assumptions |
| Bibliography [1]–[121] | Yes, text; pp. 71/73 visual | Partly | Represented in compressed form | Relevant provenance retained; entries not individually annotated or verified |
| Logos, running heads, contact details | Yes where supplied | Accounted for | Inspected but deliberately omitted as non-substantive | Not scientific evidence |
| Appendices | None identified | Not applicable | Missing from supplied material | No evidence one was intended |
| Supplementary material | None supplied or identified | Not applicable | Missing from supplied material | No claim of review |
| Underlying cited papers/code/data | No | Only survey reports | Inaccessible | Not part of supplied source evidence |
| LLM-agent comparative experiment | No such item in supplied work | Boundary explicitly stated | Missing from supplied material | Cannot support comparative vulnerability claim |

### Missing or inaccessible material

No numbered physical page is missing from the supplied 1–74 sequence. Direct page images are unavailable for physical pp. 2, 4–5, 7, 9, 11, 15, 17, 19, 21–22, 24–25, 27–28, 31, 33, 35–38, 40–41, 43–49, 52, 54–57, 60–61, 63–70, 72, and 74; these were text-only reviews. All identified numbered figures are visually supplied. No appendix or supplement was reviewed. Underlying citations, datasets, websites, and implementations remain uninspected.

### Uncertain interpretations

The exact intended bibliography mapping for the cloaking citation [117] and the IRLbot author-name mismatch is unresolved. Summation/integral glyph damage is handled using adjacent definitions, without claiming independent equation rendering on unpictured pages. Figure 3.2's full checkmark matrix is compressed rather than used to infer quantitative performance. The count-versus-fraction description of binary weighted coverage is explicitly flagged. MaxNDCG terminology is preserved as printed. Comparative vulnerability of web AI agents and standalone LLMs is UNKNOWN from this document.

### Deliberately compressed material

Early-system chronology, repeated motivating examples, all individual bibliography entries, every categorical checkmark combination in Figure 3.2, and low-level alternatives already explained elsewhere are compressed. All important mechanisms, model assumptions, central numerical conditions, eight figures, major limitations, and listed future directions are represented. Full proofs and detailed underlying study configurations cannot be compressed from this source because they are not supplied here.

### Potential omissions

No identified major section or numbered figure is wholly unrepresented. The report does not reproduce every secondary historical fact, reference title, implementation detail, or example; those compression categories are disclosed above. Coverage is therefore comprehensive at the substantive survey-component level, with explicit limits on visual page coverage, underlying-study verification, mathematical derivations, and transfer to the user's LLM-security question. Length alone is not treated as proof of completeness.
