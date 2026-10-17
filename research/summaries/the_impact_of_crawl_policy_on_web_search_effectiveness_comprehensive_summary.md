## Stage 0 — Document Accessibility Report

The supplied main document contains eight physical PDF pages, corresponding to printed pages 580–587. Native/extracted text is supplied for physical pages 1–8. Rendered source images are supplied and visually inspected for physical pages 1, 3, 4, 5, 6, 7 and 8. Physical page 2 is reviewed through its supplied text only. References below use physical PDF page numbers, not the printed pagination.

The title, abstract, introduction, evaluation framework, experimental subsections, conclusions and references are accessible. The page sequence and section sequence appear continuous; no missing main-text page is apparent from the supplied material. This observation does not establish that every artifact associated with the original publication was supplied. There are no supplied appendices, supplementary files or embedded attachments. No explicit supplementary-material reference is identified in the supplied text.

All seven numbered figures are visually available. Figure 1 has two panels; Figure 6 also has two panels. Figures 4 and 5 are diagrams with numerical annotations. There are no numbered tables, formal algorithms, pseudocode blocks, theorems or proofs. The displayed equations for Discounted Cumulative Gain and Jaccard similarity are readable through the supplied text and images. Small figure legends and plotted points are less precise than the prose. Exact values are used where explicitly printed; estimates from curve positions are labeled approximate. No OCR, browsing, code execution or external material was used.

Evidence labels used throughout: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information is introduced. Confidence concerns fidelity to the supplied evidence, not independent confirmation of the study. The requested research question about Web AI agents is distinct from this paper's research problem; its relevance is discussed only as an explicitly labeled inference.

## 1. Plain-language orientation

This paper asks how a search engine should choose which Web pages to collect when it cannot collect everything. A useful page cannot appear in a search result if the engine never selected it for crawling. Consequently, the crawler's selection policy limits the quality that even an otherwise perfect search engine could achieve. [A, pp. 1–3]

The researchers compare three established ways of prioritizing pages: incoming-link count, incoming links from other domains, and PageRank. They compare these policies with a breadth-first crawl, examine combinations of policies, impose limits on pages selected from individual domains, and follow policies across repeated selection rounds. Their contribution is primarily an evaluation framework rather than a new basic link-ranking algorithm. [A, pp. 2–6]

Two devices make the evaluation practical. A cached collection, called a sandbox, reduces repeated downloading. A metric called **maxNDCG** measures the best possible retrieval score permitted by the selected URLs, using human relevance judgments, without building and querying a separate search index for every policy. It measures an opportunity ceiling, not actual search-engine performance. [A, pp. 1–4]

All three link-based policies improve on the breadth-first baseline under the reported evaluation. Trans-domain indegree is attractive for some small, first-round selections, but PageRank is more reliable across repeated rounds. Hybrid selections and domain budgets can produce better quality-versus-size tradeoffs than PageRank alone. The paper does not evaluate large language models, Web AI agents, prompt injection, attacker success or the comparative vulnerability of agents and standalone models. [A for crawl findings; D for research-scope assessment]

## 2. Document roadmap

The document is an empirical Web information-retrieval and crawling study with a systems-oriented experimental framework. Its inventory is:

| ID | Original item | Physical pages | Role |
|---|---|---|---|
| META | Title, authors, venue, abstract and classification | 1 | Identifies and previews the study |
| S1 | §1 Introduction | 1 | Connects crawl selection to achievable search quality |
| S2 | §2 Crawling and Evaluation | 1–3 | Establishes incremental crawling and evaluation choices |
| SS21 | §2.1 Evaluating a crawl | 2 | Contrasts efficiency, RankMass and retrieval evaluation |
| SS22 | §2.2 Comparing crawl policies | 2 | Introduces sandbox control and tie-breaking |
| SS23 | §2.3 Evaluating and comparing crawl policies for search | 2–3 | Defines maxNDCG, clicks and stability considerations |
| S3 | §3 Experiments, introductory setup | 3–4 | Describes policies, collection and judgments |
| SS31/X1 | §3.1 Individual crawl ordering methods | 4–5 | Compares policies using relevance and clicks |
| SS32/X2 | §3.2 Combinations of crawl selection methods | 5 | Tests unions of selections |
| SS33/X3 | §3.3 Domain limits for crawl selection | 5–6 | Tests domain-budget schemes |
| SS34/X4–X7 | §3.4 Iterative crawl selection | 6–7 | Tests repeated selection, overlap, churn and helpful pages |
| S4 | §4 Conclusions and Future Work | 7–8 | Synthesizes findings and proposes extensions |
| S5 | §5 References | 8 | Lists 19 cited works |
| F1–F7 | Figures 1–7 | 4–8 | Policy quality, combinations, budgets and iteration behavior |
| E1–E3 | DCG, normalization/maxNDCG, Jaccard | 2–4, 6 | Evaluation mathematics |

The title is **The Impact of Crawl Policy on Web Search Effectiveness**, by Dennis Fetterly, Nick Craswell and Vishwa Vinay, affiliated with Microsoft Research. The supplied publication notice identifies SIGIR ’09, July 19–23, 2009, Boston, Massachusetts, USA. Printed pagination spans 580–587. The classification is Information Storage and Retrieval: Information Search and Retrieval; general terms are Measurement and Experimentation. No separate author-keyword list is supplied. [A, pp. 1, 8]

## 3. Background and context

A crawler downloads pages, extracts their links and maintains a **frontier** of known URLs that have not yet been downloaded. A URL is the address identifying a Web resource. The crawler's link graph represents known pages as vertices and hyperlinks as directed connections. Discovered pages can therefore be represented in the graph even when their contents have not been fetched. [A, pp. 1, 4]

A search engine subsequently indexes collected documents, matches queries to them and ranks results. The paper separates the collection's potential from the quality of those later stages. A relevant document missing from the collection cannot be recovered by a better ranker operating only on that collection. Conversely, including a relevant document does not guarantee that a real ranker will return it. [A, pp. 1–3]

**Breadth-first**, abbreviated BF in the experiments, is the baseline crawl strategy. **Indegree**, abbreviated IDG, counts observed incoming links to a URL. **Trans-domain indegree**, abbreviated TD, counts incoming links only when they cross domain boundaries. The paper's example treats aa.com to aacareers.com as cross-domain, but aa.com to fly.aa.com as within-domain. A more exhaustive domain-parsing rule is not supplied. **PageRank**, abbreviated PR, supplies another link-based ordering score; the paper does not reproduce its mathematical definition or parameter settings. [A, pp. 2–3]

**Normalized Discounted Cumulative Gain**, or NDCG, rewards retrieval of highly relevant documents, with rank-dependent discounting. **maxNDCG** asks what NDCG could be achieved by perfect indexing and ranking, given which judged URLs are available. **RankMass** instead adds page-goodness scores, traditionally based on PageRank. The authors prefer relevance-based evaluation because their objective is useful search results rather than agreement with a link-popularity surrogate. [A, pp. 2–4]

## 4. Research problem and gap

**Existing problem.** The Web offers an effectively unbounded collection, while search engines have finite resources. Choosing the wrong pages wastes capacity and excludes potentially useful answers. Repeated updates introduce another difficulty: a policy must preserve information needed to choose well in the next round. [A, pp. 1–3]

**Shortcomings of previous approaches, according to the authors.** Evaluations based on PageRank-derived RankMass do not directly measure potential retrieval usefulness. Full evaluations that build separate indexes and run queries are expensive and mix crawl quality with retrieval-function quality. Separate live crawls are additionally confounded by changing pages, timeouts and other non-reproducible network events. [A, p. 2]

**Research gap.** The authors report being unaware of published experiments comparing the relevance achievable by different crawl policies. Their response is to vary the corpus while removing indexing and ranking differences from the primary measurement. Their novelty claim is bounded to their stated awareness of prior work; the supplied paper does not independently establish exhaustive literature coverage. [A, pp. 1–3]

**Motivation and scope.** The study seeks user-oriented measures of corpus quality and a tractable large-scale comparison procedure. It focuses on popularity-based selection from a prior crawl's link graph, including incremental selection. It does not attempt a comprehensive evaluation of crawler implementation efficiency, freshness, spam resistance, actual query latency or every possible selection policy. [A, pp. 1–3]

## 5. Research questions / objectives / hypotheses

The paper supplies objectives and motivating questions rather than a numbered hypothesis set. The following identifiers organize those objectives without presenting them as verbatim formal research questions:

- **O1:** Compare crawl size with maximum potential retrieval effectiveness.
- **O2:** Determine how IDG, TD and PR compare with breadth-first selection.
- **O3:** Determine whether complementary selections can be combined beneficially.
- **O4:** Investigate how per-domain budgets change the quality-to-size tradeoff.
- **O5:** Evaluate whether first-round advantages persist through repeated selections.
- **O6:** Examine corpus overlap, churn and retention of pages that help discover relevant content.

O1 and O2 are addressed mainly by Figure 1; O3 by Figure 2; O4 by Figure 3; O5 by Figure 4; and O6 by Figures 4–7. [A, pp. 1–8; analyst-assigned identifiers]

No explicit null hypotheses, prespecified statistical tests, significance levels or formal causal identification strategy are reported. The explanatory idea that PageRank retains more useful supporting pages is presented cautiously by the authors as a possible explanation, not as a proven mechanism. [A, p. 7]

## 6. Assumptions / threat model

There is no security threat model. The study specifies no attacker, protected asset, adversarial payload, model trust boundary or attack-success criterion. Its reference to robustness against manipulation increasing spam is a desired property for future corpus-quality evaluation, not an evaluated attack. [A, p. 8]

The experimental system assumes that an initial crawl supplies a usable graph, that relevance judgments can identify valuable pages, and that selected-URL presence is informative about an ideal search engine's potential. The requested version of maxNDCG additionally treats a requested URL as available regardless of whether downloading succeeds. It is therefore explicitly optimistic about acquisition. [A, pp. 2–4]

The sandbox reduces variation by reusing each URL's recorded acquisition result. This control is useful for comparing policies but means repeated selections are not repeated independent observations of a continuously changing live page. Unknown pages can be fetched once and added during the iterative experiment. [A, pp. 2, 6]

The maximum score remains limited by the judged pool and the discoverable URL universe. A perfect ranking assumption removes ranking errors from evaluation, while incomplete judgments and incomplete graph coverage remain. These are boundaries of the measured construct, not guarantees about actual users or actual search systems. [A for definitions; D for characterization]

## 7. Methodology

### Policy and comparison design

IDG ranks by observed inlink count; TD ranks by cross-domain inlink count; PR ranks by PageRank. The methods themselves are established techniques. The authors considered OPIC but did not pursue it because its online crawl-time advantage was not relevant to this setting. Comparisons include a breadth-first baseline, single-policy thresholds, unions of two policy selections, and PR selections restricted by domain budgets. [A, pp. 3–6]

### Initial large sandbox

A breadth-first crawl starts from the Open Directory Project homepage as a single seed. It makes **1,376,880,495 HTTP requests**, yielding **930,320,010 text/html documents and HTTP redirects**. Redirects are treated as documents with exactly one link. HTTPS URLs and URLs from a small set of crawler-trap domains are filtered out. The authors store **36 checkpoints**, consistently across crawling nodes. Hardware details and software versions are not given. [A, pp. 3–4]

The induced graph contains **16,124,409,514 vertices**, including fetched pages and discovered frontier URLs. The paper also describes **14.7 billion** discovered-but-uncrawled pages. These vertices have observed incoming links but no observed outgoing links. The numerical relationship between this rounded count and the other reported counts is discussed below rather than silently reconciled. [A, p. 4]

### Human judgments and query sample

The evaluation uses **10,570 queries** from Microsoft Live Search and **1,433,308 query–URL relevance judgments**. Candidate URLs came from pooled top-ranking results from three major search engines, described as top-10 pooling. Judgments were gathered independently of the current crawl experiment. Each pair receives one of five grades: Bad, Fair, Good, Excellent or Perfect. **17.2%** are Good, Excellent or Perfect. [A, pp. 2–4]

The supplied text says queries were uniformly sampled from the set of all queries, including rare queries that occurred once. It does not provide the sampling dates, query-language distribution, assessor counts, inter-assessor agreement, adjudication procedure or a released judgment file. There are no training/validation/test splits because the reported design is a policy-evaluation study rather than a trained predictive-model benchmark. [A for sample description; D for reporting inventory]

### Metrics and controls

The gain vector is **0, 3, 7, 15, 31**, in ascending relevance order. The primary cutoff is **K = 10**. A tested cutoff of **K = 100** is not adopted because it may reward collecting many mediocre pages. A linear gain vector reportedly leaves relative policy effectiveness unchanged, but detailed results for that sensitivity check are not supplied. [A, p. 4]

The primary plotted comparisons use **requested maxNDCG** for fairness: all methods receive credit for requesting a judged URL, even if the request fails. About **70%** of requests succeed in the reported crawls. A separate click measure sums historical clicks associated with selected URLs. Click data are kept outside the basic selection policies for this corroborative comparison. In the later domain-budget experiment, however, click-entry information explicitly becomes a selection signal. [A, pp. 3–6]

### Repeated selections

The authors build a fresh, smaller sandbox because the time gap makes expansion of the earlier sandbox unsuitable. The October 2008 BF crawl requests **147,484,129 documents** and successfully fetches **108,908,962** HTML documents or redirects. Subsequent approximately 100-million-page selections expand this sandbox as necessary; each document is attempted once. The final sandbox contains **411,491,513 pages**. Random tie-breaking is used where necessary, particularly for TD. Seeds for that randomization, repeated trials and uncertainty intervals are not reported. [A, pp. 2, 6–7]

## 8. Experiments / analyses

### X1 — Individual policies and independent click corroboration

**Purpose:** compare usefulness versus size for BF, IDG, TD and PR. **Setup:** one selection round using the large initial graph, evaluated at multiple cutoffs. **Outcomes:** requested maxNDCG and sum of clicks; Figure 1. All three link-based selections improve on BF. TD is strongest for several selections below 500 million documents, whereas PR provides stronger coverage over a wider size range and consistently beats IDG by the authors' reported 1–2 NDCG points for selections of at least 300 million documents. Click curves broadly corroborate the relevance-based ordering. [A, pp. 4–5]

**Caveat:** this is potential effectiveness with incomplete judgments, not measured query results from newly constructed indexes. The click comparison supplies corroboration, not a formal correlation coefficient or an unbiased causal validation.

### X2 — Hybrid policy unions

**Purpose:** exploit differing relevant-page selections. **Setup:** take the union of TD-selected URLs at cutoffs labeled 2 or 4 with PR or IDG selections. **Outcome:** maxNDCG versus resulting corpus size; Figure 2. PR combined with TD achieves the strongest reported hybrid effectiveness, while TD plus IDG can outperform PR with less expensive scoring. The corpus becomes larger, so the authors compare the quality gain against that resource increase. [A, p. 5]

**Caveat:** the prose's description of the threshold includes the phrase more than 2; the figure legend uses cutoff labels. Exact boundary inclusion at every threshold is not independently resolved from implementation details.

### X3 — Domain budgets

**Purpose:** avoid spending too much capacity on individual domains. **Setup:** apply budgets to PR selections initially sized at **25 million, 100 million, 400 million, 700 million, 1 billion and 1.5 billion** documents. Compare static, click-entry and linking-domain budgets; dynamic variants use rank or score, with scaling factors **1, 10, 100, 256 and 512**. [A, pp. 5–6]

The score-based versions outperform rank-based versions on the quality-to-size ratio. The highlighted click-entry budget at scale **256** obtains **0.6398 maxNDCG** with **421 million documents**, compared with **0.6597** for a **1.5-billion-document** PR selection. The authors describe the smaller collection as 28% of the size. Figure 3 displays only a subset of tested schemes and constants. [A, p. 6]

### X4 — Repeated selection effectiveness

**Purpose:** determine whether an initially attractive method stays attractive. **Setup:** fresh BF collection and roughly 100-million-URL selections over four IDG/PR rounds and three TD rounds. **Outcome:** requested maxNDCG; Figure 4. TD wins round 1 at approximately 0.45, but PR has the best displayed result from round 2 onward. TD and IDG lose effectiveness relative to their first round. Actual-selection mean maxNDCG is usually **93–95%** of requested mean maxNDCG. [A, p. 6; B for rounded diagram values]

### X5 — Within-policy and between-policy overlap

**Purpose:** measure update continuity and policy divergence. **Setup:** Jaccard similarity across successive rounds and across different policies in the same round. **Outcomes:** Figures 4 and 5. IDG and PR successive-round overlap reaches approximately **0.80**; TD remains much lower and stops after round 3 because of resource costs. Cross-policy overlaps decline, showing increasingly different selected corpora. [A, pp. 6–7]

### X6 — Stable, gained, lost and alternating URLs

**Purpose:** distinguish stable membership from churn. **Setup:** three-bit membership codes across rounds 1–3, analyzed for all URLs and separately for Good-or-better URLs. **Outcome:** Figure 6. TD retains only around **20 million** URLs in all three rounds and shows much more instability. Its total set of relevant URLs is larger, but its stable relevant core is smaller than those of PR and IDG. [A, p. 7]

### X7 — Helpful-page association

**Purpose:** explore why repeated policies differ. **Setup:** count pages linking to Good, Excellent or Perfect URLs in round i−1, then plot against round-i maxNDCG. **Outcome:** Figure 7. TD loses helpful pages quickly; IDG and TD show lower next-round quality with fewer helpful pages. PR maintains relatively stable quality despite losing helpful pages. The proposed explanation concerns selective retention of useful high-weight pages, but this is an explanatory interpretation rather than an isolated intervention. [A, p. 7]

## 9. Results

The central finding is conditional: **crawl policy affects the upper bound on retrieval usefulness at a given collection size**. The result holds within these judged queries, graph-derived selections and sandbox procedures. It is stronger than saying that every larger crawl is better, but narrower than proving that one policy universally produces the best real search engine. [A, pp. 4–8; D for scope interpretation]

The complete known-URL universe has maxNDCG **0.7216**, not 1, because it does not contain all judged relevant URLs. BF is consistently below the later policy selections in Figure 1. TD's advantage at several small sizes does not generalize to repeated selection. PR's continuous-looking score differentiation also makes it easier to select a range of sizes than integer degree thresholds with very large tied groups. [A, pp. 4–5]

For the domain-budget example, the exact reported score difference is **0.0199**, calculated as 0.6597 − 0.6398. This is **analyst-derived**, not a separately reported effect. The size ratio is **421/1500 = 0.2807**, approximately 28.1%, consistent with the authors' rounded 28%. The relative score reduction is **0.0199/0.6597 ≈ 3.02%**, also analyst-derived. These calculations compare the two specified configurations; they are not confidence-adjusted effects or actual end-user loss estimates. [C, operands from p. 6]

The iterative diagram reports PR scores of **0.42, 0.43, 0.42 and 0.43**; IDG scores of **0.43, 0.41, 0.38 and 0.39**; and TD scores of **0.45, 0.42 and 0.41**. Values are rounded as printed. PR is strongest after the first round. However, the prose on page 7 says TD was overtaken by both other methods, while the displayed TD scores remain above IDG at rounds 2 and 3. That narrower inconsistency must be retained. [B, p. 6; A, p. 7]

The authors use terms such as significant and substantial without reporting inferential tests, confidence intervals or repeated-run variability. These words should not be translated into demonstrated statistical significance. [D, reporting observation]

## 10. Figure-by-figure interpretation

### Figure 1 — Individual-policy quality versus collection size

**Location:** physical page 4. **Panels:** left, maxNDCG@10; right, sum of clicks on URLs in the corpus. Both horizontal axes show corpus size in millions, with labeled positions from 0 to 1,500. The left vertical axis runs from 0 to 0.8. The right vertical axis runs from 0 to 800, with click totals expressed in millions. These are ordinary linear plotted scales. [B]

The legend separates initial BF requested selection, PR, IDG and TD. The left panel also includes a dark horizontal sandbox ceiling. Colored lines and small markers distinguish policies: BF is a light-blue dashed series, PR a red dotted series, IDG a blue series and TD a green series. Exact visual colors are secondary identifiers; the legend names carry the comparison. No error bars, confidence intervals or significance markers are shown. [B]

All policy curves rise with corpus size and flatten. BF stays below the link-based selections. TD rises strongly at small sizes but has limited larger-selection discrimination. PR and IDG approach one another at larger sizes, with PR generally higher. The right panel broadly mirrors these trends. The exact ceiling is **0.7216**, supplied in the text, not inferred from the line height. Other exact point coordinates cannot be recovered reliably from this small plot and are not presented as exact results. [A/B, pp. 4–5]

### Figure 2 — Hybrid selection criteria

**Location:** physical page 5. **Type:** line plot. Horizontal axis: corpus size, millions, 0–1,500. Vertical axis: maxNDCG@10, approximately 0.40–0.70. The legend includes PR and four unions: TD cutoff 2 with PR, TD cutoff 4 with PR, TD cutoff 2 with IDG, and TD cutoff 4 with IDG. Colored lines and markers differentiate these five series; no uncertainty displays appear. [B]

The hybrid curves generally sit above PR at comparable collection sizes over the displayed ranges. PR plus the more permissive TD cutoff supplies the highest visible envelope, reaching roughly **0.67** near **1.25 billion** pages; this endpoint is an approximate visual estimate. Curves have different extents because unions yield different sizes. The figure supports complementarity of selections, not an exact universal gain at every possible size. [A/B, p. 5]

### Figure 3 — Domain budgets applied to PR

**Location:** physical page 6. Horizontal axis: corpus size in millions, 0–1,500. Vertical axis: maxNDCG@10, approximately 0.30–0.70. The legend distinguishes unbudgeted PR, score click-entry limits at 100× and 256×, and score linking-domain limits at 1× and 100×. The plot shows a subset of the tested budget variants. [B]

Budgeted curves rise more steeply in the small-size region than unrestricted PR. The important exact example comes from the prose: **421 million**, **0.6398**, scale **256**, compared with **1.5 billion**, **0.6597** for PR. No error bars or significance annotations are visible. The visual supports a strong efficiency tradeoff but does not show runtime or measured hardware-resource savings. [A/B]

### Figure 4 — Iterative selection paths

**Location:** physical page 6. This is a directed process diagram, not an axis-based plot. Each box contains the policy/round label, rounded corpus size in millions and requested maxNDCG. Edge numbers are Jaccard similarity, as indicated by the key. Starting BF is **109m / 0.40**. [B]

The IDG path is **107m/0.43 → 99m/0.41 → 95m/0.38 → 107m/0.39**, with successive similarities **0.58, 0.75, 0.80** after the first IDG selection. TD is **108m/0.45 → 102m/0.42 → 104m/0.41**, with similarities **0.20, 0.33**. PR is **97m/0.42 → 97m/0.43 → 97m/0.42 → 97m/0.43**, with similarities **0.64, 0.77, 0.80**. BF-to-first-selection similarities are **0.29** for IDG, **0.10** for TD and **0.31** for PR. These are visually readable rounded annotations. [B]

The figure simultaneously displays effectiveness and continuity. It shows TD's first-round quality advantage, PR's later quality advantage and TD's continuing turnover. The sizes are approximate 100-million targets rather than exactly equal collections. [A/B]

### Figure 5 — Cross-policy overlap

**Location:** physical page 7. Three triangular node-link diagrams compare IDG, PR and TD at rounds 1, 2 and 3. PR nodes are purple, IDG nodes cyan and TD nodes orange; edges carry Jaccard values. Spatial coordinates are layout positions, not measurement axes. [B]

Round 1 overlaps are **PR–IDG 0.41**, **PR–TD 0.11**, **IDG–TD 0.18**. Round 2 shows **0.32, 0.06 and 0.09**, respectively. Round 3 shows **0.28, 0.05 and 0.08**. The annotations are readable in the supplied image. All three pairs decline, with PR and IDG remaining closer to one another than either is to TD. [B]

This figure concerns similarity between policies in the same round. It must not be confused with Figure 4's similarity between successive rounds of the same policy. It supports divergence toward different URL collections despite broadly similar aggregate quality ranges. [A/B]

### Figure 6 — Stability categories over three rounds

**Location:** physical page 8, although discussed on page 7. Two stacked-bar panels compare Indegree, tdIndegree and PageRank. The left vertical axis is millions of all URLs, extending to 180; the right is thousands of relevant URLs, extending to 70. Four green shades encode stable **111**, increase **011+001**, decrease **100+110** and churn **010+101**. There is no temporal horizontal axis; each bar summarizes membership trajectories across three rounds. [B]

TD has a much smaller stable bottom segment for all URLs, approximately **20 million** as also stated in the prose. Its gain, loss and churn segments are larger than those of the other methods. Among relevant URLs, TD has the tallest overall bar but a smaller stable core than the other two. Exact category counts are not labeled and are not reconstructed from bar heights. There are no error bars. [A/B]

### Figure 7 — Helpful pages and next-round quality

**Location:** physical page 7. Horizontal axis: relevant backlink URLs in iteration i−1, in millions, with displayed ticks approximately 5–30. Vertical axis: maxNDCG in iteration i, approximately 0.37–0.46. Blue IDG, red PR and green TD lines connect round-specific observations. Neither axis represents uncertainty, and connected points do not establish causation. [B]

All rightmost starting points share the helpful-page count of BF. TD moves toward fewer helpful pages and lower next-round maxNDCG. IDG also declines overall. PR remains near **0.42–0.43** while losing helpful pages. The authors infer that PageRank may retain the more useful subset of supporting pages. Exact horizontal point values are not individually labeled, so no exact helpful-page counts are asserted here. [A/B]

## 11. Table-by-table interpretation

No substantive table is present in the supplied paper. The tables in this analysis are analyst-created organizational aids, not source tables. No hidden table results, table footnotes or table-based significance tests can therefore be reported. Numerical evidence comes from prose, plotted curves and diagram annotations. [B/D]

## 12. Diagram / architecture interpretation

The evaluation workflow can be reconstructed from the prose: **initial BF crawl → cached pages and link graph → policy-based URL selection → relevance/click/stability evaluation**. In the iterative experiment, selected pages supply graph information for the next selection; previously unknown selected URLs are fetched once and added to the sandbox. This is an analyst-organized rendering of the described workflow, not an additional source figure. [A/D, pp. 2–6]

Figure 4 makes the repeated-selection control flow explicit. BF branches into three independent policy paths; each path advances by applying that policy again. Box contents describe outputs of a selection round, while arrows describe transitions and overlap. The diagram does not claim that IDG output becomes TD input or that the three methods exchange selected pages. [B]

Figure 5 instead represents pairwise set similarity. Its undirected relationships compare same-round outputs and do not show downloads, ranking operations, information transmission or causal influence between methods. The distinction matters because declining cross-policy similarity can coexist with increasing within-policy stability. [A/B, pp. 6–7]

No detailed crawler-service architecture, queue implementation, machine topology, storage layout or production deployment diagram is supplied.

## 13. Equations and mathematical concepts

### E1 — Discounted Cumulative Gain

On page 4, the paper defines **DCG@K = Σ from j=1 to K of G(j)/log(1+j)**. Here **j** is rank, **K** is the rank cutoff and **G(j)** is the gain of the document at rank j. Gains are 0, 3, 7, 15 and 31 for Bad through Perfect. The summation adds graded relevance, with the logarithmic denominator reducing the contribution of lower-ranked results. The logarithm's base is not specified in the supplied formula. No base is silently assigned here. [A]

### E2 — Normalization and maximum potential

The prose defines **NDCG@K = DCG@K / ideal DCG@K**. The denominator is obtained by sorting all known judged documents for that query by decreasing gain, including documents absent from every evaluated crawl. Thus missing relevant pages reduce the achievable numerator without reducing the reference ideal. [A, p. 4]

The following is an analyst restatement of the definition, rather than a separately printed equation: **maxNDCG@K(C,q) = DCG@K of the best judged ranking available within selected corpus C for query q, divided by the all-known-judgments ideal DCG@K for q**. The inputs are a selected URL set and query relevance judgments; the output is a normalized potential score. Perfect indexing and ranking are assumed. The study reports means over its query evaluation. Handling of queries with a zero ideal denominator is not specified. [A/D, pp. 2–4]

### E3 — Jaccard similarity

Page 6 gives **J(Ci,Cj) = |Ci ∩ Cj| / |Ci ∪ Cj|**. Ci and Cj are URL sets defining two corpora. Intersection counts shared URLs; union counts distinct URLs in either set; vertical bars indicate set cardinality. High values indicate overlap. Low values indicate large differences and potentially expensive updates. This is a set measure, not a ranking measure or a direct elapsed-time measurement. [A]

### Membership codes

For rounds 1–3, each URL receives three presence bits. **111** means present throughout; **100** or **110** means loss; **011** or **001** means increase; **010** or **101** means alternating membership, termed churn. These codes are observed-membership categories, not relevance grades or probabilities. No theoretical results, optimization proof or PageRank equation are provided. [A, p. 7]

## 14. Interpretation and discussion

O1 and O2 are answered by showing that equally sized or comparably sized URL selections can permit different retrieval quality. The choice of corpus matters separately from the ranking method. O3 is supported by complementary relevant URLs in TD and PR/IDG selections. O4 is supported by domain budgets that discard many pages while retaining much of the judged retrieval potential. O5 and O6 show why a single-round assessment is insufficient: policies also influence the graph information available for subsequent choices. [A, pp. 4–8]

The authors position their work against PageRank-based RankMass evaluation and alongside query-driven corpus construction. They distinguish their use of relevance for evaluating established popularity policies from prior work using needy queries to design the policy itself. They also distinguish click-frequency utility from retrieval-frequency impact measures. These descriptions report the paper's positioning; the cited works were not independently reviewed. [A, pp. 2–3]

Three consistency issues deserve explicit handling. First, the page-7 statement that both IDG and PR overtake TD conflicts with Figure 4's rounded IDG-versus-TD scores. Second, page 4's **14.7 billion** discovered-but-uncrawled count is not straightforwardly reproduced by subtracting **930,320,010** fetched documents from **16,124,409,514** graph vertices: that subtraction gives **15,194,089,504**, approximately 15.19 billion. This arithmetic is analyst-derived; the supplied material does not fully explain the count boundary producing 14.7 billion. Third, the reported **0.0619** gap on page 5 has an ambiguously worded comparison and should not be assigned a more specific baseline without qualification. [A/B/C]

For the requested security research question, the relevant inference is architectural: systems acquiring Web material have an upstream selection process that changes what information becomes available. This paper demonstrates that selection and repeated acquisition matter to information availability. It does not demonstrate that this availability causes malicious instruction following, that agents are more vulnerable than standalone models, or that any particular defense works. [D]

## 15. Contributions and novelty

**Conceptual:** treat corpus selection as a limit on achievable user-oriented retrieval quality, rather than equating corpus quality with accumulated PageRank. [A, pp. 1–3]

**Methodological:** combine maxNDCG with a URL/page sandbox so many large selections can be compared without separate indexing and searching pipelines or repeated requests for the same URL. [A, pp. 1–3, 7]

**Experimental:** compare BF, IDG, TD and PR; corroborate with clicks; evaluate unions and domain budgets; and follow approximately 100-million-page selections over multiple rounds. [A, pp. 3–7]

**Empirical:** demonstrate a size–quality tradeoff, complementary selections, strong domain-budget efficiency and the difference between first-round TD performance and later PR reliability. [A, pp. 4–8]

The paper does not claim a new PageRank algorithm, a released benchmark dataset, a security defense, a formal theorem or a trained model. Its large crawls are experimental resources, but the supplied material gives no release or licensing statement establishing them as reusable public datasets. [D, reporting inventory]

## 16. Limitations

### Authors' stated limitations

The evaluation axes are not exhaustive: spam and freshness also affect corpus quality. The sandbox does not include all judged relevant URLs, explaining its ceiling below 1. The original large sandbox is unsuitable for the later iterative experiment because newly selected pages and elapsed time complicate expansion; a new collection is built instead. TD is stopped one iteration earlier because of crawling-resource costs. Degree-based methods have large tied groups and limited discrimination; TD also has too few cross-domain links to support fine-grained large selections. [A, pp. 3–7]

The authors acknowledge the computational cost of PR and the possibility that full indexing and searching would be expensive. They explicitly frame maxNDCG as potential effectiveness and note that requested and actual successful selections differ. These are relevant boundaries of their experimental design. [A, pp. 1–6]

### Additional evidence-based analyst observations

The judgment pool is bounded by three engines' retrieved results and the study's query sample. No claim is established about unjudged relevant pages. Requested maxNDCG is optimistic about fetch success. HTTPS exclusion and crawler-trap filtering restrict the tested universe. Click-entry budgets depend on pre-existing click evidence, whose observation period and coverage are not reported. [D]

No confidence intervals, statistical tests, assessor agreement, repeat-seed experiments, randomization seeds, detailed PR parameters or complete domain-budget implementation equations are provided. The helpful-page account is associative. The study does not empirically connect its results to AI-agent security. These observations concern the supplied evidence and do not imply that the authors claimed otherwise. [D]

## 17. Threats to validity

The following labels are analyst classifications, not a formal threats-to-validity section in the paper.

**Internal validity:** sandbox reuse reduces temporal and network-event variation between policies. Nevertheless, graph incompleteness, ties, unequal rounded selection sizes and adaptive sandbox expansion can influence comparisons. The paper does not quantify each influence separately. [D, grounded in pp. 2, 4, 6–7]

**Construct validity:** maxNDCG captures the ideal usefulness of judged URLs present in a selection. It does not measure actual ranking, answer generation, task completion, freshness, spam exposure, safety or attack success. Click sums are a second utility signal, but not a universal measure of user benefit. [D]

**External and ecological validity:** results are tied to the supplied crawl universe, query source, relevance pool, URL filtering and historical collection. They do not directly establish performance across other languages, populations, seeds, modern Web conditions or agent architectures. No contemporary comparison is attempted. [D]

**Statistical conclusion validity:** curves and point estimates support descriptive differences, but absent uncertainty estimates limit statements about variability and formal significance. **Reproducibility:** the paper supplies many useful counts and procedures, while omitting code, data access, detailed parameters and random seeds. **Security generalizability:** no attacker experiment supports comparative claims about standalone LLMs and Web agents. [D]

## 18. Future work and open questions

### A. Authors' proposed future work

The authors call for broader corpus-quality evaluation, including spam resistance and freshness; additional domain-limiting criteria; limits based on prespecified crawl depth or the number of known pages in a domain; coupling budgets with policies other than PR; and hybrid selections that combine effective components. They also suggest using selection/budget information to stratify an index in a multi-tier architecture. [A, pp. 3, 6, 8]

### B. Additional open questions

Analyst questions include whether the policy ordering persists under different seeds and judgment pools; how much of PR's later advantage is caused by helpful-page retention; whether repeated hybrid or budgeted policies retain their one-round advantages; and how results change when evaluation uses successful downloads and actual retrieval rather than requested potential. [D]

For the security research question, separate experiments would be needed to establish whether acquisition policies alter malicious-content exposure, whether fetched content crosses a model instruction boundary, and whether an otherwise matched Web-enabled system fails more often than a standalone model. These are proposed research questions, not findings from this paper. [D]

## 19. Terminology and notation glossary

| Term | Meaning in this paper |
|---|---|
| Crawl | Collection process that requests pages and follows discovered links |
| Crawl selection policy | Rule choosing URLs to include or request |
| Corpus | Selected collection forming a possible search-engine index basis |
| Frontier | Known URLs not yet fetched |
| Sandbox | Cached experimental universe reused across policy comparisons |
| BF | Breadth-first baseline crawl |
| IDG / indegree | Count of observed links into a URL |
| TD | Incoming links from other Web domains |
| PR / PageRank | Link-based score used to order URLs; its formula is not reproduced |
| Incremental recrawl | Updating an existing collection, including refresh and selection changes |
| RankMass | Sum of page-goodness scores over the selected corpus |
| NDCG | Normalized Discounted Cumulative Gain, a graded retrieval metric |
| maxNDCG | Maximum possible NDCG allowed by selected judged URLs |
| Requested selection | URLs credited as selected regardless of fetch success |
| Actual selection | Successfully acquired subset, as distinguished in the paper |
| Click utility | Sum of recorded result clicks for corpus URLs |
| Domain budget | Limit on pages selected from one domain |
| Click entry point | A unique URL within a domain that received a search-result click |
| Linking-domain count | Number of domains linking to a domain |
| Jaccard similarity | Intersection size divided by union size for two URL sets |
| Churn | Alternating presence, coded 010 or 101 across three rounds |
| Helpful page | Page linking to a Good, Excellent or Perfect judged URL |
| G(j), j, K | Gain at rank j, rank index, and evaluation cutoff |
| Ci, Cj | Two corpus URL sets compared for overlap |
| HTTP / HTTPS | URL/request schemes distinguished by the crawl filter; HTTPS is excluded |
| HTML | Document content type retained in the crawl, alongside redirects |
| OPIC | Named alternative online algorithm; its expansion is not supplied |
| IR | Information retrieval |
| LLM | Large language model; used in the user's research question, not studied here |

The paper does not define every named algorithm or acronym in full. Missing expansions and implementation details are not filled from outside sources.

## 20. Key numerical results

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| Large-crawl requests | 1,376,880,495 | HTTP requests | Initial BF sandbox | Author-reported | p. 4 |
| Large-crawl acquired documents | 930,320,010 | HTML documents/redirects | Initial BF | Author-reported | p. 4 |
| Checkpoints | 36 | checkpoints | Initial BF state | Author-reported | p. 4 |
| Known graph vertices | 16,124,409,514 | URLs/vertices | Fetched plus discovered | Author-reported | p. 4 |
| Stated uncrawled frontier | 14.7 billion | pages | Rounded prose count; count issue noted | Author-reported | p. 4 |
| Query sample | 10,570 | queries | Live Search workload | Author-reported | p. 4 |
| Relevance judgments | 1,433,308 | query–URL judgments | Five grades | Author-reported | p. 4 |
| Good-or-better judgments | 17.2 | percent | Query–URL pairs | Author-reported | p. 4 |
| Gain vector | 0, 3, 7, 15, 31 | gain | Bad through Perfect | Author-reported | p. 4 |
| Primary cutoff | 10 | ranks | NDCG/maxNDCG | Author-reported | p. 4 |
| Alternative cutoff | 100 | ranks | Tested, not adopted | Author-reported | p. 4 |
| Sandbox maximum | 0.7216 | maxNDCG | All known URLs hypothetically fetched | Author-reported | p. 4 |
| Request success | Around 70 | percent | Reported crawls | Author-reported | p. 4 |
| Reported gap | 0.0619 | score | Ambiguously worded comparison | Author-reported | p. 5 |
| PR advantage over IDG | 1–2 | NDCG points | Selections at least 300m | Author-reported | p. 5 |
| Pages with indegree 3 | 960 million | URLs | Large graph tie group | Author-reported | p. 5 |
| Pages with indegree 2 | 2 billion | URLs | Large graph tie group | Author-reported | p. 5 |
| TD indegree >1 | 276 million | URLs | Large graph | Author-reported | p. 5 |
| TD indegree =1 | 979 million | URLs | Large graph | Author-reported | p. 5 |
| Rank-budget default | 10 | pages/domain | Described prior scheme | Author-reported | p. 6 |
| Rank-budget top group | 10,000 | domains | Extra limits, interpolated 10,000 to 10 | Author-reported | p. 6 |
| Other domains | Nearly 20 million | domains | Outside top 10,000 | Author-reported | p. 6 |
| Budget scale factors | 1, 10, 100, 256, 512 | multiplier | Tested scaling choices | Author-reported | p. 6 |
| Unbudgeted PR example | 0.6597 | maxNDCG | 1.5 billion documents | Author-reported | p. 6 |
| Click-entry budget example | 0.6398 | maxNDCG | 421m documents; scale 256 | Author-reported | p. 6 |
| Budgeted size fraction | 28 | percent | Authors' rounded comparison | Author-reported | p. 6 |
| Exact score difference | 0.0199 | score | 0.6597 − 0.6398 | Analyst-derived | p. 6 operands |
| Relative score reduction | Approximately 3.02 | percent | 0.0199 / 0.6597 × 100 | Analyst-derived | p. 6 operands |
| Fresh BF requests | 147,484,129 | documents requested | October 2008 | Author-reported | p. 6 |
| Fresh BF successes | 108,908,962 | documents | HTML/redirects | Author-reported | p. 6 |
| Final iterative sandbox | 411,491,513 | pages | After expansion | Author-reported | p. 6 |
| Iterative target | Approximately 100 million | pages/corpus | Sizes vary in Fig. 4 | Author-reported | p. 6 |
| Actual/requested quality | Usually 93–95 | percent | Mean maxNDCG ratio | Author-reported | p. 6 |
| Final PR/IDG overlap | Around 0.80 | Jaccard | Successive rounds | Author-reported | p. 7 |
| Stable TD core | Around 20 million | URLs | Present in rounds 1–3 | Author-reported | p. 7 |
| Hybrid high endpoint | Approximately 0.67 | maxNDCG | Around 1.25b pages, Fig. 2 | Approximate visual estimate | p. 5 |

Rounded iterative node values and cross-policy similarities are fully transcribed in the figure interpretations rather than duplicated in this reference table. The table preserves exact reported representations where important and does not convert all approximate author counts into falsely exact integers.

## 21. Claim–evidence map

| Claim | Evidence | Figure / experiment | Source | Qualification / evidence strength |
|---|---|---|---|---|
| Selection constrains achievable retrieval | Missing relevant pages lower the ideal achievable score | E2 / framework | pp. 1–4 | HIGH for the defined measurement |
| Sandbox enables controlled reuse | URLs cached; iterative unknown URLs added once | Methods | pp. 2, 6 | HIGH for described procedure; not a frozen snapshot of all Web content |
| Link-based policies beat BF | Quality-versus-size curves and authors' description | F1 / X1 | pp. 4–5 | HIGH within evaluated selections |
| TD is strong at some small first selections | Below-500m comparisons and first iterative score 0.45 | F1, F4 / X1, X4 | pp. 5–6 | HIGH; does not imply repeated superiority |
| PR is strongest in later rounds | PR 0.43/0.42/0.43 versus lower later alternatives | F4 / X4 | p. 6 | HIGH for displayed rounded values |
| Hybrid selection improves tradeoff | TD unions above PR curve | F2 / X2 | p. 5 | HIGH direction; exact gains not tabulated |
| Domain budgets preserve quality with fewer pages | 0.6398 at 421m versus 0.6597 at 1.5b | F3 / X3 | p. 6 | HIGH for specified configurations |
| TD is less stable | Low successive Jaccard and small stable core | F4, F6 / X5, X6 | pp. 6–8 | HIGH; TD fourth round absent |
| Helpful-page retention may explain quality | Lagged association, authors' possible explanation | F7 / X7 | p. 7 | MEDIUM as interpretation; not causal proof |
| Both IDG and PR overtake TD | Prose assertion | X4 discussion | p. 7 | LOW as a general reading; conflicts with F4 for IDG |
| Agent-security relevance is indirect | Selection changes available information; no agent test | Scope assessment | pp. 1, 8 | MEDIUM as analyst analogy; comparative vulnerability UNKNOWN |

The machine-readable claims following this narrative use physical page ranges and matching short source quotations. They preserve the distinction between source claims and the analyst's research-relevance inference.

## 22. Very simple explanation

Imagine a library that can keep only a limited number of books. A librarian who chooses poorly may leave out exactly the book someone needs. Even a perfect catalog cannot find a book the library never collected. This paper studies the equivalent problem for search engines: which Web pages should they keep?

The researchers compare several rules based on links between pages. They ask how good search results could possibly be if the engine had only the pages chosen by each rule. That is what maxNDCG measures. It does not mean the real search engine would actually achieve that score; it means the chosen pages permit that much usefulness under ideal ranking.

One rule, counting links from other domains, looks especially good for some small first collections. But choosing again and again changes which link information remains available. PageRank gives more reliable later collections. Combining rules or limiting how many pages come from one domain can also save space while retaining much of the useful material.

For Web AI-agent security, the cautious connection is that choosing what information to fetch matters. The paper does not test whether fetched pages contain attacks or whether an AI follows malicious instructions. It therefore helps frame an acquisition-layer question, but it cannot establish why Web agents are more vulnerable than standalone language models.

## Completeness Audit

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Metadata and abstract | Yes, text and image | Yes | Fully represented | Title, authors, venue, framing and headline results |
| §1 Introduction | Yes, text and image | Yes | Fully represented | Selection bottleneck and resource tradeoff |
| §2 opening | Yes, mixed coverage | Yes | Fully represented | Frontier and incremental-selection distinction |
| §2.1 | Yes, text only | Yes | Fully represented | Efficiency, RankMass, retrieval objective |
| §2.2 | Yes, text only | Yes | Fully represented | Sandbox, variation and ties |
| §2.3 | Yes, text and partial image coverage | Yes | Fully represented | maxNDCG, clicks, overlap and corpus-quality scope |
| §3 introductory methods | Yes | Yes | Fully represented | Policies, seed, filters, judgments and counts |
| §3.1 / X1 | Yes | Yes | Fully represented | Individual methods and click corroboration |
| §3.2 / X2 | Yes | Yes | Fully represented | Union policies and complementary selections |
| §3.3 / X3 | Yes | Yes | Fully represented | Static/dynamic budgets, scales and reported example |
| §3.4 / X4 | Yes | Yes | Fully represented | Fresh sandbox and repeated quality |
| X5 overlap | Yes | Yes | Fully represented | Within-policy versus between-policy distinction |
| X6 membership stability | Yes | Yes | Fully represented | All-URL and relevant-URL categories |
| X7 helpful pages | Yes | Yes | Fully represented | Association and cautious mechanism |
| §4 Conclusions/Future Work | Yes | Yes | Fully represented | Findings, scope and proposed policies |
| §5 References | Yes | Yes | Represented in compressed form | 19 entries; relevant categories summarized, no external validation |
| O1–O6 objectives | Yes | Yes | Fully represented | Analyst IDs; not invented formal hypotheses |
| Formal hypotheses | None identified | Yes, absence recorded | Fully represented | No hypothesis-testing protocol reported |
| Figure 1, both panels | Yes, visually | Yes | Fully represented | Quality and click trends; no exact curve digitization |
| Figure 2 | Yes, visually | Yes | Fully represented | Hybrid conditions and threshold caveat |
| Figure 3 | Yes, visually | Yes | Fully represented | Selected budget variants and exact prose values |
| Figure 4 | Yes, visually | Yes | Fully represented | Rounded nodes and edge values transcribed |
| Figure 5 | Yes, visually | Yes | Fully represented | All nine pairwise similarities transcribed |
| Figure 6, both panels | Yes, visually | Yes | Fully represented | Category meanings and trends; unlabeled heights not exact |
| Figure 7 | Yes, visually | Yes | Fully represented | Axes, temporal relation and interpretation |
| Tables | None identified | Yes, absence recorded | Fully represented | Analysis tables are not source objects |
| E1 DCG | Yes | Yes | Fully represented | Log base unspecified |
| E2 normalization/maxNDCG | Yes | Yes | Fully represented | Analyst notation explicitly marked |
| E3 Jaccard | Yes | Yes | Fully represented | Set operations and meaning |
| Membership codes | Yes | Yes | Fully represented | All seven nonempty patterns accounted for |
| Formal algorithms/pseudocode | None supplied | Yes, absence recorded | Fully represented | Procedures described in prose |
| Major contributions | Yes | Yes | Fully represented | Framework and empirical contributions distinguished |
| Author-stated limitations | Yes | Yes | Fully represented | Scope, coverage, ties and resource constraints |
| Appendices | Not supplied | Absence recorded | Missing from supplied material | None referenced or detected |
| Supplementary artifacts | Not supplied | Absence recorded | Missing from supplied material | None identified as explicitly referenced |
| Copyright/contact matter | Yes | Partly | Inspected but deliberately omitted as non-substantive | Venue preserved; contact details not analytically necessary |

### Missing or inaccessible material

No missing main-document page is apparent. Physical page 2 has no supplied visual rendering, so its visual layout was not inspected. Underlying crawled pages, link graphs, judgment files, click logs, code, random seeds and experimental receipts are not supplied. No appendices or supplements were reviewed. Their absence is not treated as proof that the original project never had additional artifacts.

### Uncertain interpretations

Exact unlabeled curve points and stacked-bar category counts remain unavailable. The PageRank-versus-indegree claim that both overtake TD conflicts with Figure 4 for indegree. The 14.7-billion frontier count is not reconciled by the straightforward graph-minus-successful-documents calculation. The 0.0619 comparison is ambiguously worded. Strict versus inclusive implementation of every TD threshold is not fully specified. The DCG logarithm base, zero-denominator handling, PR parameters and detailed domain-budget formulas are not supplied. These uncertainties are retained rather than repaired from outside knowledge.

### Deliberately compressed material

Repeated explanations of the size–effectiveness tradeoff are consolidated. The 19-item bibliography is summarized by its methodological roles rather than reproduced entry by entry. Contact addresses, copyright boilerplate and repeated caption wording are omitted as non-substantive. Exact line-marker shapes and every unlabeled plot coordinate are not enumerated; policy identities, axes, scale, trends, conditions and numerical limits are preserved. The paper's brief external examples are summarized without expanding their cited literature.

### Potential omissions

Every substantive section, subsection, numbered visual, major evaluation equation, identified experiment, central contribution and stated limitation in the supplied inventory is represented. This is coverage of the supplied evidence, with the listed compression and uncertainties; it is not a claim to preserve every source sentence or to have verified unavailable underlying data. The requested comparison of Web-agent and standalone-LLM vulnerability remains untested by this paper.
