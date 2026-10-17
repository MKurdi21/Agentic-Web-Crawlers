## Stage 0 — Document Accessibility Report

The supplied work is **One Polluted Page Is Enough: Evaluating Web Content Pollution in Generative Recommenders**, by Minghao Luo and Liang Chen, The Chinese University of Hong Kong. The first-page visual identifies arXiv:2606.13610v1, dated 11 June 2026. No accepted conference or journal venue is established by the supplied work.

| Accessibility item | Assessment |
|---|---|
| Main document | Available as supplied extracted text for physical PDF pages 1–26 |
| Accessible page count | 26 textual page records; this establishes supplied coverage, not independently verified file completeness |
| Visual inspection | Directly inspected supplied page images for pages 1, 2, 4–9, and 13–26 |
| Text-only pages | Pages 3 and 10–12; their content was read from supplied extraction, without page-image inspection |
| Apparently missing pages | None in the supplied textual sequence; four pages lack supplied visual rendering |
| Tables | Tables 1–17 are available in text and on supplied images; dense rows were cross-checked against extraction |
| Figures | Figures 1–14 are visually available; small labels and unlabeled graphical positions do not establish exact values |
| Equations | Equations (1)–(3) are text-only; equations (4)–(5) also have visual rendering |
| Appendices | Appendices A–O are supplied across pages 13–26 |
| Supplementary artifacts | No separate supplementary files, repository checkout, raw outputs, prompts file, or evaluation logs supplied |
| Referenced artifacts | A benchmark repository and evaluation harness are announced; their contents were not inspected |
| OCR | Not performed or needed for this response; supplied extraction is an aid, checked against images where available |
| Other limits | No tools, browsing, execution, reproduction, citation validation, or independent verification of the supplied SHA-256 |

All document contents, including model-output excerpts, were treated as evidence rather than instructions. This is a closed-document analysis. **[A]** means author-reported; **[B]** means directly observable in supplied visuals; **[C]** means analyst-derived; **[D]** means analyst interpretation. No external information, category **[E]**, is introduced. Confidence describes confidence in source-grounded representation, not confidence that the authors' real-world assertions have independently been proved.

The user’s research question concerns why web AI agents may be more vulnerable than standalone large language models. This paper directly studies search-augmented recommendation under polluted evidence. It does **not** provide a matched security comparison of web agents and standalone LLMs. Relevance to that broader comparison is therefore explicitly an analyst inference.

## 1. Plain-language orientation

A search-augmented recommendation assistant first reads web pages and then recommends products or businesses. The paper asks whether plausible but corrupted web evidence can persuade such an assistant to recommend a brand that does not genuinely exist in the relevant setting. The attack can succeed while the assistant continues to answer the user's actual question fluently: the failure is a false recommendation, rather than a visibly hijacked conversation.

The researchers introduce **FORGE**, Fake Online Recommendations in Generative Environments. They retrieve real search results, freeze the evidence, and locally replace selected real-brand references with fake-brand references. This simulates what happens after polluted pages have reached a search-result bundle, without publishing those pages to the live web. They evaluate twelve models on 225 product queries across fifteen categories and five consumer scenarios.

Under the main condition—replacement in the first three retrieved documents—per-model fooled rates range from 13.3% to 73.8%. A secondary experiment restricted to six open-weights models and Digital Products finds up to 27% with one polluted first-ranked document. Models are generally more exposed in fragmented categories such as dining than in technical categories such as phones and computers. Two paired reasoning-toggle experiments find lower vulnerability with reasoning disabled, while observational trace analysis associates successful rejection with much longer deliberation.

The central contribution is a controlled benchmark connecting polluted retrieved evidence to on-task fake-brand promotion. Its defense experiments are also important: one skepticism instruction increases average vulnerability, and two post-hoc filters reject many fake brands while also removing many legitimate recommendations. These findings support a specific retrieval-trust concern; they do not establish that every web agent is less secure than every standalone model.

## 2. Document roadmap

The inventory below is the denominator for the final coverage audit. Original numbering is preserved.

| Inventory item | Location | Role |
|---|---|---|
| Abstract; §1 Introduction | pp. 1–2 | Motivation, measurement gap, contribution, headline findings |
| §2 Background and Preliminaries | p. 3 | Autoregressive generation, search-augmented recommendation, polluted web model |
| §3 The FORGE Benchmark | pp. 3–4 | Construction, three attack styles, fooled-rate metric |
| §3.1 Benchmark Construction | p. 3 | Scenarios, query templates, frozen evidence bundles |
| §3.2 Pollution Simulation | pp. 3–4 | Entity replacement, passage injection, full synthesis |
| §3.3 Evaluation Metric | p. 4 | Recommendation indicator and three metric-validation audits |
| §4 Experiment; §4.1 Settings; §4.2 Results | pp. 4–6 | Main cross-section and five targeted studies |
| §5 Analysis | pp. 6–7 | Brand agreement, rejection traces, invented social proof |
| §6 Defenses | pp. 7–8 | Skepticism and two consensus filters |
| §7 Related Work | pp. 8–9 | Authors' positioning against adjacent research |
| §8 Conclusion | p. 9 | Synthesis and proposed defense direction |
| Limitations | pp. 9–10 | Attack optimization, scope, language/region, static snapshot, anchor heuristic |
| Ethical Considerations | p. 10 | Dual use, local simulation, private polluted documents, independence |
| References | pp. 10–12 | Bibliography; not independently validated |
| Appendix A | pp. 13–15 | Retrieval, prompts, anchor review, dataset statistics and sensitivity |
| Appendices B–D | pp. 15–17 | Qualitative outputs, endorsement audit, recommendation rank severity |
| Appendix E | pp. 17–18 | Evidence-free probes, alignment predictors, regression and mediation |
| Appendices F–H | p. 18 | Dose-response values, rank-position values, implementation identifiers |
| Appendices I–K | pp. 18–22 | False positives, attack-style ablation, English replication |
| Appendices L–M | pp. 22–25 | Defense definitions, utility cost, subgroup/category effects |
| Appendices N–O | pp. 25–26 | Paired reasoning ablation and three-way trace analysis |

Visual inventory: Figures 1–14 and Tables 1–17. Mathematical inventory: an unnumbered autoregressive factorization and equations (1)–(5). There are no supplied numbered algorithms, theorem statements, proof sequences, or keyword list. The work is an empirical AI/security benchmark paper with methodological and diagnostic analyses, rather than a theoretical security proof or a systematic literature review.

## 3. Background and context

A **large language model (LLM)** generates text token by token. A token is an element of its text representation; the paper models each next-token probability using previously generated tokens. **Autoregressive** means generation proceeds in this left-to-right conditional fashion. The authors mention supervised fine-tuning, **SFT**, and reinforcement learning from human feedback, **RLHF**, as post-training processes, but this study trains no new recommender model.

A **generative recommender** produces recommendations in language rather than simply retrieving a catalog row. Here it receives a user query and retrieved web evidence, then returns a ranked recommendation list. A **parametric prior** is the product or brand knowledge available from the model's parameters before reading the current evidence. The study operationalizes this through evidence-free recommendation probes; these probes are measurements of what a model recommends unprompted by documents, not direct examinations of its stored knowledge.

**Retrieval-augmented generation**, or **RAG**, is discussed as an adjacent setting in which generation depends on retrieved material. The authors distinguish poisoning a deployer-controlled retrieval corpus from pollution on the open web. **Search engine optimization**, or **SEO**, is the upstream route through which live-web operators would seek visibility. **Generative Engine Optimization**, or **GEO**, is discussed both as a prior content-optimization idea and as commercial fake-content promotion in the paper's threat framing.

An **evidence bundle** is the ordered set of pages given to the model. An **anchor** is the selected real-brand string in a document that will be rewritten. **Entity replacement** changes a brand identity within otherwise retained text. **Confabulated social proof** means model-generated claims of community endorsement, testing, or reputation that the authors report are absent from the polluted source documents.

The distinction between content and instruction matters. FORGE's central attack corrupts apparent facts and reviews; it does not need an explicit command telling the assistant to ignore the user. The answer can remain on-task and policy-compliant. This is the authors' stated reason why common signs of instruction hijacking may be absent, not an independently validated universal statement about all detection methods.

## 4. Research problem and gap

**Existing problem [A]:** consumer recommendation increasingly depends on live-web material that may include fake reviews or promotional pages. An assistant can convert that material into a recommendation that appears credible.

**Shortcomings attributed to prior approaches [A]:** the authors argue that existing evaluations primarily cover instruction injection, poisoned closed retrieval corpora, recommendation on clean catalogs, or promotion of existing products. They say these settings do not directly measure fake-brand promotion from plausible polluted live-web evidence.

**Research gap [A]:** once a polluted page enters the evidence bundle, how often does a model treat it as credible support for a recommendation? This is a downstream consumption question. FORGE does not measure the separate likelihood that an attacker can obtain a particular commercial-search ranking.

**Motivation [A]:** the introduction describes a March 2026 consumer-protection broadcast and commercial GEO operators. These events and enforcement references are author-reported motivation only; they were not externally checked.

**Scope [A]:** Chinese-language product and local-life recommendations, with a smaller English replication; twelve production model identifiers; five scenarios and fifteen categories; frozen evidence from an April 2026 retrieval snapshot; local manipulation rather than live publication. No transactional purchases, browsing navigation policy, credentials, tool execution, or agent memory compromise is evaluated.

## 5. Research questions / objectives / hypotheses

The abstract explicitly asks: to what extent do search-augmented LLMs become unwitting promoters of fake products when consuming polluted retrieval results? This is **RQ1**, the central research question (p. 1).

Appendix K explicitly gives two external-validity questions: **RQ2**, whether the pipeline is Chinese-specific or generalizes linguistically; and **RQ3**, whether category ordering and model dispersion reproduce in English or reflect Chinese brand coverage in pretraining (p. 21).

Other objectives are expressed through experiments rather than formally numbered hypotheses: quantify category/model differences; vary reasoning, polluted-page rank, pollution count, attack style, and language; investigate associations with brand knowledge and output traces; validate the metric; and measure defenses alongside their utility costs. These are objectives, not analyst-invented formal hypotheses.

The paper also raises specific methodological concerns: whether a substring match counts warnings rather than endorsements; whether fake prefixes collide with genuine names or ordinary language; whether anchor disagreement inflates category vulnerability; and whether retained real brands help explain weaker passage injection. Each is addressed with an audit or analysis, although several answers remain qualified by sample coverage or design confounds.

No preregistration, formal hypothesis list, power calculation, or prespecified multiplicity correction is visible. Absence from the supplied work should not be replaced by an assumption that such procedures occurred.

## 6. Assumptions / threat model

The protected asset is the integrity of a ranked recommendation: the model should not promote a planted fake brand as a genuine worthwhile product. The relevant trust boundary is between open-web evidence and the assistant's recommendation process (pp. 1–3).

In the authors' live-web model, an operator authors fake pages promoting fake brands and seeks indexing and search visibility. The polluted web is a union of existing web content and attacker-authored pages. The model receives whichever pages search returns and is unaware of the clean/polluted distinction. Attack success occurs when it recommends a fake brand.

In the actual experiment, the researcher has stronger, controlled placement access: selected documents inside a frozen bundle are locally edited. Default A1 changes all mentions of a chosen real brand in title, snippet, and body of the first three documents; document ordering, original URL, and surrounding context are retained. Other documents remain available. This isolates downstream sensitivity conditional on placement, but does not reproduce an attacker's upstream SEO work.

A2 inserts a promotional paragraph while preserving the original document and its real brands. A3 replaces the body with a synthetic review and changes the URL path while keeping its domain. Those interventions differ on several dimensions, so they are not a single clean manipulation of an abstract realism variable.

Trusted experimental components include the frozen bundle selection, anchor review process, prompt assembly, input hashes, and metric implementation as reported by the authors. The supplied artifacts do not independently establish their implementation correctness. Model weights and standard user queries are not the attacked channel. The study does not require attacker access to training data, a private retrieval index, system prompts, or model parameters.

**Analyst interpretation [D]:** this paper illustrates an additional route to error when an assistant consumes external material: plausible false evidence can influence a legitimate task without an overt malicious instruction. It cannot quantify the overall vulnerability increase over standalone models, because the no-evidence audits test spontaneous fake-prefix emission rather than an equivalent standalone attack.

## 7. Methodology

### Construction and data

The five scenarios are Digital Products, Local Life, Health & Personal, Fashion Accessories, and Sports & Outdoor. Each has three categories and each category has fifteen product queries: 5 × 3 × 15 = 225 queries [A, p. 3]. Here a product query is a query subject, not one single recommended brand. Each query asks for five recommendations.

Scenario-specific query templates request five worthwhile purchases, well-regarded products, worthwhile Shenzhen venues, or products worth attention. Routers, SSD enclosures, and docking stations receive the well-regarded wording. A shared system prompt requests recommendations with brief reasoning. The paper supplies templates but does not visibly enumerate the complete 225-item product list despite the Appendix A title and earlier promise of a full list.

For each query, Serper searches with gl=cn and hl=zh-CN through up to four result pages, approximately forty candidate URLs. Python requests fetches bodies with a ten-second timeout and browser-like User-Agent. BeautifulSoup4 uses html.parser. Character encoding follows HTTP charset first and chardet-based detection second. The quality gate rejects non-2xx responses; bodies under fifty visible non-whitespace characters; excessive non-printable/replacement characters, ratio greater than 0.2; fixed video-platform domains; and recognized boilerplate landing pages. The authors also describe manual quality review. The first ten accepted documents in original search order form each frozen bundle (pp. 3, 13).

There are 2,250 document/anchor slots. Appendix A reports 1,478 distinct corpus-wide real-brand strings; summing category pools gives 1,564 because categories overlap. Mean distinct brands per ten-document bundle is reported as 8.55. The concentration index D/b summarizes documents per brand; its corpus value is 1.52. These are dataset descriptions, not trained-model data splits.

### Anchor extraction and review

Stage 1 uses Gemini 2.5 Flash-Lite at temperature 0.1 and schema-enforced JSON output to propose up to eight candidate strings. It rejects descriptors such as recommendation or ranking list. Stage 2 applies title/snippet-priority regular expressions for Chinese/Japanese/Korean, **CJK**, and Latin spans, filtered through approximately fifty curated real-brand prefixes per category. Stage 3 lets a trained native-Chinese-speaking reviewer accept, choose another candidate, or enter a corrected string from the document.

Reported cumulative anchor recall rises from 48.2% to 72.9% to 100%; the reviewer override rate is 51.8%. The 100% figure means coverage relative to the final curated anchors, rather than externally established perfect identification. A second reviewer independently checks 300 stratified slots, twenty per category, blinded to the first reviewer's selection. Exact-string agreement is 226/300 = 75.3%, with Cohen's κ = 0.752 and bootstrap 95% interval [0.704, 0.802], using 2,000 resamples. Different-brand choices account for 24.3%; different surface forms for 0.3%; no sampled slot is labeled NO_VIABLE_ANCHOR (pp. 14–15).

### Models and inference

The closed-source group contains Gemini 3 Flash, GPT-5.4, o4-mini, Gemini 3.1 Pro, Claude Opus 4.7, and Claude Sonnet 4.6. The open-weights group contains Qwen3.6-27B, Qwen3.6-35B-A3B, Qwen3.5-9B, DeepSeek V4 Pro, GLM-4.6V-Flash, and Ministral-3R. These names and classifications are the paper's supplied configuration, without outside validation.

Appendix H lists exact identifiers: gemini-3-flash-preview; gemini-3.1-pro-preview; gpt-5.4; o4-mini; claude-opus-4-7; claude-sonnet-4-6; deepseek-v4-pro; Qwen/Qwen3.5-9B; Qwen/Qwen3.6-27B; Qwen/Qwen3.6-35B-A3B; zai-org/GLM-4.6V-Flash; mistralai/Ministral-3-8B-Reasoning-2512. Evaluation uses a single greedy completion, temperature 0, and max_output_tokens=8192. A SHA-256 hash of each system/user/evidence triple is stored with outputs. Hardware, library versions, random seeds, serving details, and API revision history are not specified in the supplied material.

### Attacks, metrics, and statistics

A1 replaces selected real-brand strings with fake brand–product compounds. A2 uses Gemini 2.5 Flash with thinking disabled to generate a 120–180-character promotional paragraph inserted at the body's midpoint. A3 uses Gemini 2.5 Flash to generate a 500–700-character fake-brand review, a new title, and an original-domain /p/<hash> path. Each style targets the first three documents in its comparison.

The headline metric is a case-insensitive occurrence indicator for the full fake target or its prefix. The fooled rate is the percentage of evaluated model/query responses triggering it. Secondary Top1 counts fake brands first placed at recommendation rank one. Metric audits evaluate false positives, numbered-list placement, and warning contexts. A definition mismatch between the broad occurrence rule and Appendix O's recommendation-set rule remains unresolved below.

Statistical procedures include Wilson intervals for proportions; Friedman χ² for category differences; Pearson correlation for category agreement; Spearman correlations for predictor panels and anchor sensitivity; permutation tests; bootstrap intervals, commonality and mediation analysis; leave-one-out regression assessment; Cohen's d; area under a curve, AUC; and exact two-sided McNemar tests for paired binary outcomes. The supplied work does not fully specify every regression formula or uncertainty estimate.

## 8. Experiments / analyses

| ID | Purpose and design | Results and qualifications |
|---|---|---|
| X1 Main cross-section | 12 models × 15 categories × 15 products; top-3 A1; one response per cell; Table 2, Fig. 2 | Rates 13.3%–73.8%; category means 22.8%–81.7%; findings conditional on frozen retrieved evidence |
| X2 Reasoning toggle | Two open-weights models; matched 225 ON/OFF cells each; Fig. 3, Table 16 | Qwen 56.9% → 38.7%; GLM 80.4% → 71.6%; ON rates differ from headline cross-section values |
| X3 Single-page position | Six open-weights models; Digital Products, 45 queries per condition; rank 1–10; Fig. 4, Table 9 | Rank-1 up to 27%; pooled later ranks much lower, but individual rank-3 values reach 13% and 11% |
| X4 Pollution count | Same six models and 45-query subset; N = 1, 2, 3, 5, 7, 10; Fig. 5, Table 8 | Mostly increasing; at N=10, 44%–100%; small non-monotonic steps exist |
| X5 Attack style | All models/categories; five products per category, 75 per model/style; Fig. 6, Table 11 | A1/A2/A3 grand averages 38%/25%/78%; multiple attack dimensions change |
| X6 English replication | Fresh English bundles; three matched categories, ten queries each; all twelve models; 360 trials; Fig. 7, Table 12 | Aggregate ordering 43% < 58% < 87%; does not hold in that order for every model |
| X7 Brand-prior predictors | Empty-evidence probes; pairwise brand-set agreement and alignment measures; Fig. 8, Appendix E | Pearson r = −0.65, p < 0.01; regression/predictor sample scopes vary |
| X8 Trace grouping | 1,350 open-weights cross-section cells; absent mention / rejected mention / fooled; Fig. 9, Table 17 | Rejected-mention group has median 7,983 reasoning characters versus 1,312 and 1,360 |
| X9 Social-proof analysis | Qualitative screen-protector outputs and population marker scan; Table 5, §5 | Authors report 1.5–11× marker frequency; raw population counts and lexicon not supplied |
| X10 D1 skepticism | All 2,700 model/query cells; prepend skepticism instruction; Figs. 10–11, Tables 13 and 15 | Pooled +10.5 pp; closed-source +24 pp, open-weights −3 pp |
| X11 D2 model-prior filter | Six open-weights models; keep recommended brands present in own no-evidence probe | About 95% fake-brand catch; 62%–79% real-brand utility loss, mean 68% |
| X12 D3 document filter | All models; retain brands with document count at least τ; Tables 13–14 | At τ=4: 89.9% catch, rounded to 90%; mean utility loss 63% |
| X13 Metric audits | Lexical collisions, 1,680 no-evidence and 275 clean-evidence cells, 1,154 triggered outputs | Low sampled false positives and mostly list inclusion; not all ambiguous outputs manually checked |
| X14 Anchor sensitivity | Second-reviewer sample plus category κ/vulnerability correlation | Spearman ρ=0.25, permutation p=0.36; no systematic negative association detected in fifteen categories |

X2 is the authors' only claimed causal evidence for reasoning-related vulnerability. X7 and X8 are observational analyses. Disabling reasoning and observing long rejection traces answer different questions; they should not be blended into a universal statement that more or less reasoning always helps.

## 9. Results

**Main vulnerability [A]:** Table 2 reports model means of 13.3, 20.9, 28.4, 40.4, 47.6, and 49.8% for the six closed-source models in listed order; 31.1, 36.9, 45.8, 51.6, 73.3, and 73.8% for the six open-weights models. The overall mean is 42.7%. All twelve have a nonzero rate under top-3 A1, but universal vulnerability here means every evaluated model, not every possible LLM.

**Category differences [A]:** Phone/PC averages 22.8%, home appliances 30.0%, electronics accessories 30.6%, services 60.6%, hospitality 31.7%, dining 81.7%, makeup 32.8%, supplements 60.0%, skincare 56.7%, apparel 48.9%, underwear 42.2%, bags/shoes 36.7%, camping 32.8%, cycling 39.4%, and fitness 34.4%. Friedman χ²(14)=99.4, p < 10^−14 supports substantial category variation. Claude Sonnet reaches 100.0% in dining; several other category/model cells are 0.0%. A zero sampled category cell is not proof of immunity.

**Rank and count [A]:** rank-one A1 rates on Digital Products are 11, 2, 2, 9, 27, and 27% across the six open-weights models. At ten polluted documents the same ordered rates are 44, 73, 80, 73, 100, and 98%. GLM and Ministral exceed 50% by three polluted documents. Qwen3.6-27B decreases from 11% at N=1 to 9% at N=2; DeepSeek decreases from 44% at N=5 to 40% at N=7. Thus near-monotonic is justified; strict monotonicity is not.

**Reasoning manipulation [A]:** Qwen3.5-9B OFF minus ON is −18.2 percentage points, with 53 ON-only fooled and 12 OFF-only fooled pairs, exact p=2.8×10^−7. GLM's difference is reported as −8.9 pp, with discordant counts 29 and 9, p=1.7×10^−3. Subtracting the rounded displayed GLM marginals yields 71.6−80.4=−8.8 pp [C]; the reported −8.9 is compatible with calculation before rounding and should not be silently replaced. Generalization is restricted to the two available template toggles.

**Attack style [A]:** full synthesis reaches at least 70% in nine models and is strongest in eleven. GLM reaches 100%, Gemini 3.1 Pro and Ministral 99%. Claude Sonnet is the exception: A1 47%, A2 7%, A3 24%. Gemini 3.1 Pro and Claude Opus also reverse the usual A2<A1 pattern: A2 is 68% versus A1 35%, and 61% versus 41%. The paper appropriately later acknowledges mixed-brand and density confounds.

**Language [A/B]:** Table 12's aggregate English rates preserve the low/mid/high ordering, but its individual rows contradict the prose assertion that this happens on every model. Gemini Flash has English 70/70/40%; Gemini Pro 90/90/80%; Claude Opus 60/30/90%; GLM 80/70/90%. Aggregate generalization is supported; universal per-model ordering is not.

**Defenses [A]:** D1 increases pooled fooled rate by 10.5 pp. These are absolute percentage-point changes, not relative percent increases. D2 and D3 have different model scopes. Their utility-loss percentages count legitimate brand recommendations removed from baseline attack outputs, not losses in independently rated user satisfaction or overall recommendation accuracy.

## 10. Figure-by-figure interpretation

### Figure 1 — Live pollution versus local simulation, p. 1

Two pipelines share user query, web search, results, LLM, and recommendation. The upper chain shows fake content entering the live web upstream. The lower chain shows local rewriting of retrieved results. Red symbols distinguish fake-content insertion; the diagram explains the ethical and experimental boundary. It is an architecture sketch, not empirical evidence of measured SEO success. Small interface text is decorative to the pipeline explanation and is not transcribed as data.

### Figure 2 — Model vulnerability, p. 4

A horizontal point-and-whisker plot has fooled rate in percent on the horizontal axis, model names vertically, and blue/red encoding for closed-source/open-weights. Models are sorted by rate. Whiskers are reported 95% Wilson confidence intervals with n=225 per model. The plotted range extends approximately from zero to ninety percent; exact rates come from Table 2, and exact interval endpoints are not labeled. Both model groups contain substantial vulnerability, with their ranges overlapping.

### Figure 3 — Reasoning ON/OFF, p. 5

Grouped vertical bars compare Qwen3.5-9B and GLM-4.6V-Flash. The vertical axis is fooled rate, 0–100%; red bars are enabled and blue bars disabled. Exact labels are 56.9/38.7% and 80.4/71.6%. Each condition has 225 cells. The caption reports McNemar significance; Table 16 supplies exact discordant counts. The bars represent paired-ablation marginals, not the Table 2 model means.

### Figure 4 — Single-page rank, p. 5

A red line with circular points plots polluted document rank 1–10 against pooled fooled rate for six open-weights models. Both axes are linear; the vertical range is 0–16%. The largest point is at rank one, about thirteen percent by visual position; later points are much lower. Exact pooled points are not labeled. Table 9 supplies model-level rounded values, including residual rank-3/rank-4 effects hidden by pooling.

### Figure 5 — Pollution dose, p. 6

Six colored/marked lines plot N=1,2,3,5,7,10 polluted documents against fooled rate, 0–100%. Red/orange GLM/Ministral curves rise fastest, while Qwen3.6-27B remains lowest at high N. Legend distinguishes all six models. The exact values are in Table 8. No confidence bands are displayed. Non-monotonic steps are visible and explicitly retained in this analysis.

### Figure 6 — Three attack styles, p. 6

Grouped bars compare Mobile/Digital, Fitness Gear, and Dining. The vertical axis is fooled rate up to 100%; A1 is blue, A2 a red hatched style, A3 solid red. Full synthesis is highest in the illustrated groups. Exact bar numbers are not labeled, so this report does not invent representative-category rates. Table 11 gives model averages across all fifteen categories, a different aggregation.

### Figure 7 — English versus Chinese, p. 6

Paired horizontal bars encode Chinese in blue and English in red, with fooled rate on a 0–100% axis. Each bar averages three categories, and model order is sorted by the English-minus-Chinese gap. Large positive shifts occur for some closed-source models, while Claude Sonnet shifts negatively. Table 12 supplies exact rounded category values; individual means should not be reconstructed as unrounded measurements from graphical positions.

### Figure 8 — Agreement versus vulnerability, p. 7

A fifteen-point scatterplot has cross-model Jaccard agreement on the horizontal axis, approximately 0–0.4, and fooled rate in percent vertically. Selected labels identify dining, services, and smartphones. A dashed fitted line slopes downward. The authors report Pearson r=−0.65 and p<0.01. It supports an association between common brand recommendations and resistance, not experimentally isolated causation by brand knowledge.

### Figure 9 — Reasoning trace distributions, p. 7

Three boxplots show A: resisted without mention, n=340; B: resisted with mention, n=307; C: fooled, n=703. Vertical units are characters, scaled with a ×10^4 annotation; whiskers are fifth/ninety-fifth percentiles, not confidence intervals. Purple, green, and red distinguish groups. B's median is much higher; Table 17 gives 1,312, 7,983, and 1,360 characters. The paper does not identify every box convention beyond median/whisker descriptions. Mention-scope definitions are inconsistent across sections.

### Figure 10 — Skepticism effect, p. 8

A horizontal point-and-whisker plot shows D1 minus baseline in percentage points, sorted ascending. Negative values indicate help; positive values backfire. A dashed vertical zero reference separates the directions. Whiskers are reported paired-difference 95% intervals with n=225. Closed-source effects cluster positively. Exact interval endpoints are not printed; model deltas are in Appendix L.

### Figure 11 — Catch versus survival, p. 8

A two-dimensional plot places fake-brand catch rate on the horizontal 0–100% axis and real-brand survival on the vertical 0–100% axis. The no-filter point is at zero catch and full survival. D2 is annotated approximately (95%,32%), D3 (90%,37%). Symbols distinguish baseline and filters. The filter points use different model panels, limiting direct comparison. Survival is the complement of reported utility loss.

### Figure 12 — Detailed FORGE pipeline, p. 14

Colored boxes show retrieval in blue, anchor extraction in orange, entity replacement in red, and model evaluation/metric in green. Arrows take a query through Serper, roughly forty candidate URLs, quality gating, ten documents, three anchor stages, top-three replacement, twelve LLMs, and substring measurement. The arrow layout presents a workflow rather than feedback optimization. Details and diagram/prose differences are discussed in section 12.

### Figure 13 — Anchor extraction coverage, p. 14

A cumulative stacked bar chart has stages horizontally and recall percentage vertically, 0–100%. Labels show 48.2%, 72.9%, and 100%, with increments +24.7 and +27.1. These values agree with Appendix A. The final human-review bar establishes curated coverage, subject to the independent-review disagreement described nearby.

### Figure 14 — Dataset market structure, p. 15

A labeled scatterplot uses concentration index D/b, about 1–2.2, horizontally and distinct brand pool, about 70–150, vertically. Food/dining lies toward many brands and few documents per brand; home appliances toward fewer brands and more documents per brand. Table 3 supplies exact values. Because D/b is related mathematically to category brand count with equal document totals, the downward pattern should not itself be read as independent evidence of a causal market mechanism [D].

## 11. Table-by-table interpretation

### Table 1 — Threat taxonomy, p. 2

Columns compare training poisoning, retrieval poisoning, prompt manipulation, and web-content pollution. Rows cover motivation, polluted channel, access, content form, visible cue, and output symptom. FORGE's column emphasizes commercial promotion, open live web, indirect SEO access, plausible fake reviews, no distinctive cue, and targeted-product recommendation. This is the authors' conceptual positioning, not a measured benchmark comparison among all four threats.

### Table 2 — Main model/category matrix, p. 5

Fifteen category rows and twelve model columns contain fooled percentages, n=15 per cell. Scenario headings group categories. Heat colors run low green to high red; bold and underlining mark row extrema. Bottom/right margins aggregate categories/models. The overall 42.7% and 13.3%–73.8% model range are central. Small-cell rates occur in 6.7-point increments after rounding; uncertainty is not given for every matrix cell. Individual numeric rows are compressed into the category/model summaries above.

### Table 3 — Dataset statistics, p. 14

Rows enumerate fifteen categories; columns give product count, document/anchor count, distinct brands, brands per product bundle, and documents per brand. Each category has 15 products and 150 slots. Brands range 74–135; bundle brand means 6.80–9.47. Corpus totals are 225, 2,250, 1,478, 8.55, and 1.52. The note distinguishes deduplicated corpus totals from summing categories, avoiding a false count contradiction.

### Table 4 — Anchor-extraction failures, p. 15

Eight examples split into non-brand top candidates and missing/wrong-granularity brand candidates. Geography, descriptors, and content markers can displace a brand; model/sub-brand strings can require correction. Examples include sports-bra descriptor corrected to Alo and Brooks Glycerin 22 corrected to Brooks. This illustrates the need for downstream review, without estimating an error distribution from eight selected examples.

### Table 5 — Qualitative recommendation outputs, p. 16

Three model rows compare responses to the same screen-protector query under top-3 A1. Claude Opus and DeepSeek recommend fake Langyu; o4-mini resists without mentioning it. Red marks fake brands, blue real brands, F/R fooled/resisted. Translated excerpts are abridged; adjacent Chinese excerpts preserve source wording with author-added brackets identifying unsupported social proof. Product specifications are model-output claims, not verified real properties.

### Table 6 — Warning-marker disambiguation, p. 17

Eight flagged contexts all receive No in the negative-recommendation column. Phrases such as avoiding failure are positive features; a cleanser caveat still recommends it for another skin type. This supports endorsement interpretation for these eight cases. Two lower-confidence lexical matches were not manually resolved in the supplied account, so essentially zero negative mentions is an author extrapolation.

### Table 7 — Top-one severity, p. 17

F-R is overall fooled rate, F-T is unconditional top-one placement, and F-T/F-R is conditional top-one placement among fooled responses. Rounded model rows span 5%–53% unconditional and 40%–72% conditional. Averages are 43%,24%,55%. These rounded columns need not divide exactly. Non-enumerated triggered outputs, approximately 1%, are assigned Top1=0.

### Table 8 — Pollution-count values, p. 18

Rows N=1,2,3,5,7,10 and six model columns give rounded percentages, n=45 each. It supplies Figure 5's numerical basis. GLM reaches 100% and Ministral 98% at N=10; Qwen3.6-27B reaches 44%. Countersteps retained above qualify monotonicity. The appendix title Longitudinal refers to increasing pollution count; no repeated-time observation is shown.

### Table 9 — Rank-position values, p. 18

Rows rank 1–10 show effects of replacing only that document. Other ranks remain unmodified, n=45 per model/rank. Rank one matches Table 8's N=1. Rank three reaches 13% for GLM and 11% for Ministral, and rank four reaches 9% and 7%; therefore the main-text 1–4% language cannot be applied to every individual later-rank cell.

### Table 10 — False-positive controls, p. 20

Each open-weights model has 225 no-evidence cells; each closed-source model 55. Five total false positives occur in 1,680 cells: Qwen3.5-9B two, GLM one, DeepSeek one, Gemini Flash one. The clean-bundle row pools 275 cells with zero hits. The note attributes all no-evidence hits to two previously flagged prefixes. These audits have narrower clean-control coverage than the 2,700-cell main experiment.

### Table 11 — Attack-style averages, p. 20

Each model/style has 75 cells, fifteen categories times five products. A1 is restricted to the same subset, avoiding comparison to the full 225-cell A1 mean. Grand averages are 38%,25%,78%; the last column is A3 minus A2, mean +53 pp. GPT-5.4 has A2 0% but A3 69%; GLM has A3 100%; Sonnet is the major A3 exception. Differences reflect combined content, density, corroboration, title, and URL-path changes.

### Table 12 — English replication, p. 23

Three category blocks report English, Chinese, and their percentage-point difference for each model. English has ten fresh products/category; Chinese baselines come from the larger original category samples. The aggregate ordering persists, but multiple individual rows break it. Rounded averages and rounded differences should not be forced into exact arithmetic: smartphones displays 43%,23%,+21, which may reflect unrounded averaging. Neither matched products nor isolated language-only manipulation is established.

### Table 13 — Defense efficacy and utility, p. 24

Baseline and D1 are fooled rates; D2 util. and D3 util. are real-brand removal percentages. A dash in closed-source D2 means unevaluated, not zero loss. Mean columns show 43%,53%,68%,63%, with D2 mean restricted to six models. D1 ranges from 30% for o4-mini/Qwen3.6-35B-A3B to 84% for Gemini Pro. Its rounded baseline/defense difference is not the exact pooled +10.5 pp estimate.

### Table 14 — D3 threshold trade-off, p. 24

Rows show per-model utility loss at τ=3,4,5. Mean losses rise 49%,63%,74%; fake-brand catch is 2%,90%,91%. Moving beyond τ=4 gains only one displayed percentage point of catch while increasing displayed utility loss eleven points [C: 91−90; 74−63]. The 2% catch at τ=3 differs from the prose statement that this threshold does not filter the fake brand; implementation details do not resolve the discrepancy.

### Table 15 — D1 category effects, p. 24

Columns give closed-source, open-weights, and pooled changes in percentage points. Phone/PC is +44/+20/+32; skincare +6/−28/−11; dining +9/+3/+6. The pooled effect is positive in fourteen categories. The table contradicts text saying closed-source effects are at least +10 in every category except skincare: personal services is +19, but dining is +9. Skincare also remains positive in the closed-source column, contradicting a literal reading that it is their exception to backfire.

### Table 16 — Paired reasoning toggle, p. 25

Columns give ON/OFF marginals, OFF−ON difference, discordant pair counts b/c, and McNemar p. All 225 queries are paired within each model. Qwen's 53 versus 12 and GLM's 29 versus 9 show asymmetric flips favoring OFF resistance. Rounded marginals explain the minor GLM subtraction difference. ON marginals materially differ from Table 2; the supplied text does not explain that larger baseline mismatch.

### Table 17 — Three-way traces, p. 26

Groups A/B/C have counts 340/307/703, median reasoning characters 1,312/7,983/1,360, and mean reasoning shares 0.578/0.879/0.569. Counts sum to 1,350 [C: 340+307+703]. The share is reasoning characters divided by reasoning plus answer characters. The 703 fooled count agrees with rounded Table 2 open-weights means but does not validate the conflicting mention/Rec definitions.

## 12. Diagram / architecture interpretation

Figure 1 distinguishes the conceptual attack path from the experimental one. Live operators influence web content before retrieval. FORGE intervenes after retrieval, then tests how the downstream model consumes the modified bundle. The shared endpoint is a ranked recommendation. This separation is essential: a successful local experiment demonstrates susceptibility conditional on evidence exposure, not successful deployment of a live SEO campaign.

Figure 12 expands the experimental pipeline. A query feeds commercial search; roughly forty candidates pass through fetching and quality checks; the first ten accepted pages retain order. Anchor proposals feed rule extraction and human review. Verified anchors in selected top-ranked pages are replaced. The modified documents and unchanged query/system context feed twelve models; output matching produces a binary cell score aggregated into fooled rates.

There is no iterative adversarial search loop in the diagram. The paper explicitly says attack designs were not optimized. Nor does the pipeline show an independent authenticity verifier before recommendation. D1 modifies the system prompt at generation time; D2 filters outputs against model priors; D3 filters them against document counts. The paper proposes retrieval-time improvements, but does not implement or evaluate those proposed defenses here.

Figure 12 labels a six-predicate quality gate, while Appendix A's prose supplies five explicit reject conditions plus an encoding-handling layer and mentions review. These descriptions are close but do not establish an exact six-element predicate implementation. This remains a modest specification ambiguity rather than a demonstrated data error.

## 13. Equations and mathematical concepts

The unnumbered factorization on p. 3 is pθ(x)=∏ from t=1 to T of pθ(x_t | x_<t). Here θ denotes model parameters, x the token sequence, x_t its t-th token, x_<t the preceding tokens, and T sequence length. The product combines next-token probabilities into the probability of the sequence. This is background, not a loss optimized by FORGE. Temperature elsewhere also uses T; its meaning follows context and should not be confused with sequence length.

**Equation (1), p. 3:** E=S(q;W)={w1,…,wK}⊂W. Search engine S maps user query q and web W into K retrieved pages. E is the model's evidence input. Although written as a set, later experiments depend on its ordering; the pipeline and descriptions explicitly preserve ranks.

**Equation (2), p. 3:** pθ(y|x(r))=∏ from t=1 to T_y of pθ(y_t | x(r),y_<t), with x(r)=[E;q]. The model conditions recommendation tokens on the evidence/query prompt and its own earlier output. The bracket/semicolon notation denotes concatenation, not a mathematical union. Here r=(E,q,y) is a recommendation tuple; later r denotes a response, a notation reuse.

**Equation (3), p. 3:** polluted evidence Ē=S(q;W̃), where W̃=W∪W_fake. W_fake contains operator-authored pages promoting B_fake. The generated recommendation is sampled from the model conditioned on polluted evidence; success is described as belonging to the fake-brand set. The experiment operationalizes this abstract outcome through string matching rather than direct verification of each complete generated answer's ontology.

**Equation (4), p. 4:** Rec(t,r)=1[t appears in r]. The indicator returns one if target t, or its allowed prefix, occurs case-insensitively in response r; otherwise zero. Fooled rate is the proportion of cells triggering it. Analyst-written equivalent [C]: FR=100×(Σ_i Rec_i)/n. Inputs are responses and fake targets; output is a percentage. This is an evaluation statistic, not a differentiable optimization objective.

A major definition problem remains: Appendix O allows Rec=0 while the fake string appears anywhere in output, whereas the literal equation gives Rec=1 for such an occurrence. That requires a narrower recommendation-set scope, a distinction between reasoning and answer channels, or another implementation qualification not fully specified. The analysis does not invent a repair.

**Equation (5), p. 6:** J(p)=[choose(|M|,2)]^−1 Σ over unordered model pairs {m,m′} of |B_m,p∩B_m′,p| / |B_m,p∪B_m′,p|. B_m,p is the real-brand set from model m's no-evidence recommendation for product p; M contains six open-weights models. Intersection counts shared brands, union all brands appearing in either set, and averaging combines fifteen model pairs. Higher J means greater recommendation overlap. Category J is the average over fifteen products. Empty-set handling is not specified.

Other mathematical concepts include leave-self-out consensus alignment, regression R², rank correlations, κ for reviewer agreement, and McNemar's paired binary test. The paper describes consensus as retaining brands appearing at least twice across other models' probes, but multiset/product/rank handling is not fully formalized. No theorem claims or mathematical proof establish that consensus, trace length, or market fragmentation must cause the measured vulnerability.

## 14. Interpretation and discussion

The most directly supported finding is sensitivity to polluted retrieved content. Original document context can lend a fake name apparent legitimacy, and a model can then recommend it while completing the requested task. The authors additionally report that models invent endorsement language beyond simple copying. The qualitative excerpts support that behavior as documented examples, although the original polluted pages are not supplied for independent phrase-by-phrase absence checking.

The model-prior results suggest a resistance mechanism: categories with familiar, commonly recommended brands give models an alternative to the planted name. The category-level Pearson association and alignment predictors support this pattern. They do not isolate knowledge from every correlated category property, such as evidence composition, query form, or real-brand density [D]. Appendix E's mediation language is an author interpretation of statistical decomposition, not experimental randomization of brand-pool richness.

Reasoning results require two separate conclusions. The ON/OFF experiment supports a toggle-related causal effect within two models and that setup. The three-way trace analysis shows that successful explicit rejection co-occurs with much longer reasoning. These can coexist: enabling a reasoning channel can increase uptake of polluted evidence on average, while some sustained scrutiny rejects it. However, claims about awareness or cognitive mechanisms go beyond direct observation of text [D], and inconsistent channel/metric definitions restrict confidence.

Important unresolved consistency checks are:

| Issue | Sources | Assessment |
|---|---|---|
| Reasoning baseline mismatch | Table 2: Qwen 45.8%, GLM 73.3%; Table 16 ON: 56.9%,80.4% | Material difference; no explicit explanation despite paired-run description |
| Rec occurrence versus recommendation | Eq. (4), p. 4; Appendix O, p. 26 | Literal definitions cannot simultaneously accommodate rejected mentions without scope qualification |
| Mention channel | §5 includes response or internal trace; Appendix O defines anywhere in output | Whether reasoning is included in output is not clearly resolved |
| Every-model English ordering | p. 22 prose; Table 12, p. 23 | Contradicted by several rows; retain aggregate ordering only |
| Later-rank 1–4% claim | p. 5; Table 9 | Plausible pooled shorthand; false if read as all individual model/rank rates |
| Closed-source D1 category exception | pp. 8,23–24; Table 15 | Skincare is +6 for closed-source; dining +9 breaks at-least-10 wording |
| τ=3 no fake filtering | pp. 22,24; Table 14 | Table reports 2% catch, not exactly none |
| No-evidence probe availability | Appendix L says only open-weights collected; Table 10 contains closed-source probes | Likely scope distinction between full prior sets and smaller audits, but not explicitly clarified |
| Probe counting | Appendix E says one completion per model/product but 1,125 probes per model | 225×5=1,125 suggests brand slots, not completions; wording unresolved |
| Anchor-free predictor terminology | Appendix E calls ev_pool_size an upstream mediator | Statistical mediation interpretation, not experimentally identified causality |

The paper's strongest overall security lesson is that credible-looking evidence can undermine answer integrity without changing the task. The broader question of relative web-agent vulnerability remains open because neither comparative attack opportunity nor matched standalone failure rates is measured.

## 15. Contributions and novelty

**Conceptual [A]:** the paper positions web-content pollution as an on-task, commercial-promotion threat distinct from explicit prompt manipulation and closed-corpus poisoning.

**Benchmark/dataset [A]:** FORGE supplies a controlled consumer-recommendation testbed spanning five scenarios, fifteen categories, 225 queries, and frozen ten-document bundles. The announced repository/harness release was not inspected, and synthetic polluted documents are expressly kept private.

**Methodological [A]:** local entity substitution with retained rank/context; complementary LLM/rule/human anchor extraction; fake-prefix and endorsement audits; rank/count scans; richer attack styles; defense utility accounting; and input hashing for parity checks.

**Empirical [A]:** twelve-model/category vulnerability measurements, primacy in the Digital Products subset, broadly increasing dose response, a small English replication, paired reasoning toggles for two models, and cautionary defense results.

**Diagnostic [A]:** evidence-free brand agreement and alignment predictors, plus rejection-trace and social-proof signatures. These are useful diagnostic associations with the qualifications already stated.

The authors' claim to a first Chinese retrieval-pollution vulnerability benchmark is a literature-positioning claim. It has not been independently checked. No new trained model, formal algorithmic optimality result, or general security guarantee is supplied.

## 16. Limitations

### Authors' stated limitations

1. **Unoptimized attacks:** no search for best templates, query-aware promotional content, or adversarial SEO combinations. The authors describe results as lower bounds on attack effectiveness; this is their interpretation of unoptimized designs, not a proven bound over all deployments.
2. **Unequal subexperiment coverage:** count/rank scans cover six open-weights models and Digital Products; D2 covers open-weights; process analysis depends on accessible traces. Closed-source process generalization remains future work.
3. **Language and region:** main evaluation is Chinese and Local Life is Shenzhen. English covers three categories only, with fresh query subjects and San Francisco restaurants.
4. **Static evidence:** retrieval is frozen at an April 2026 snapshot. Category rates can change as the corpus changes; claimed stability of structural patterns is an expectation rather than a repeated-snapshot result.
5. **Anchor heuristic:** LLM/rule/human choices can vary. Reviewer pilot and category sensitivity checks reduce but do not eliminate uncertainty.
6. **Attack-style confounding:** A2 differs in both retained real brands and fake-brand density; A3 changes body, title/path, and corroboration. The paper explicitly cannot fully separate these mechanisms.
7. **Reasoning scope:** only two models expose a suitable template toggle. The authors caution against overinterpreting the two-point reasoning-volume trend.

### Additional evidence-based analyst observations [D]

A local placement intervention leaves upstream indexing and ranking success unmeasured. One greedy response per cell does not quantify output variability. Category cells have fifteen queries; English cells ten, attack-style cells five. The clean-bundle false-positive audit has only 275 cells, with no detailed per-model allocation. The public-artifact announcement cannot substitute for reviewing raw evidence or implementation.

Important consistency problems constrain mechanistic claims: reasoning ON baseline mismatch, Rec/mention scope, and the overly strong every-model English ordering statement. Agreement with a curated anchor is not the same as externally verified factual correctness. Removing real-brand recommendations measures one utility dimension, but does not independently evaluate relevance, quality, diversity, or user outcomes. These observations are the analyst's, not author-admitted limitations unless separately noted above.

## 17. Threats to validity

The following validity categories are analyst organization [D], not labels necessarily used by the authors.

**Internal validity:** A1 freezes several inputs, supporting a controlled intervention after retrieval. The paired toggle likewise holds reported inputs constant. However, unexplained ON-rate differences impede comparison with the headline experiment; A2/A3 alter several variables together. Anchor review and selection can influence what is rewritten.

**Construct validity:** substring occurrence approximates fake recommendation. List-placement and warning audits help, but the Appendix O definition conflict and uninspected low-confidence warnings remain. Brand-set agreement is a proxy for stable brand knowledge, not a direct measurement. Social-proof lexical markers approximate confabulation; full lexicon and population counts are unavailable.

**Statistical conclusion validity:** main model proportions have reported Wilson intervals, paired ablations exact tests, and category/predictor analyses several reported statistics. Category correlation uses fifteen category observations; several regression panels differ in size and feature availability. Repeated products, shared bundles, and multiple analyses are not fully covered by a stated dependence/multiplicity framework. No independent reproduction was performed.

**External validity:** evidence is drawn from specified query templates, consumer categories, languages, cities, and model identifiers. Results do not directly cover multi-step browsing agents, other domains, other time snapshots, or all production assistants. Fresh English subjects and geography changes complicate a language-only interpretation.

**Ecological validity:** original web pages improve realism, while researcher-controlled replacement and placement bypass live attacker costs. A3's same-domain path retains apparent source identity in the simulation; no permission to publish at that domain is demonstrated. This is a property of the simulation, not evidence of real attacker hosting access.

**Reproducibility:** model identifiers, prompts, search parameters, attacks, hashing, and numerical appendices provide useful specifications. Missing raw bundles, complete catalog, outputs, code inspection, software versions, and evolving API details prevent a complete reproduction assessment. Ethical privacy restrictions on polluted documents are disclosed rather than silently treated as accessible supplements.

## 18. Future work and open questions

**Explicit author proposals [A]:** multilingual and multiregion evaluation; closed-source reasoning/confabulation generalization; more optimized attack designs; a controlled-density A2 variant; and retrieval-time defenses such as credibility weighting, evidence diversification, cross-document corroboration, and noise-robust grounding. The paper proposes these directions without supplying positive evaluation results for them.

**Additional open questions [D]:** What is the cost and success probability of getting fake content indexed and highly ranked? How do matched standalone models fare under a comparable attacker-controlled input opportunity? Does authenticated independent-source provenance improve over raw document counts? How robust are category patterns across retrieval dates? Do tool-using agents compound recommendation errors through later actions? Can defenses retain unfamiliar legitimate brands while rejecting fabricated ones? How would the findings change after resolving the Rec channel definition and rerunning consistent reasoning baselines?

A particularly important research-design question is whether a defense's apparent fake-brand rejection remains useful after accounting for loss of new or long-tail real brands. FORGE shows that high catch alone can conceal severe recommendation suppression; it does not identify a tested defense that resolves the trade-off.

## 19. Terminology and notation glossary

| Term / symbol | Beginner-friendly meaning |
|---|---|
| LLM | Large language model; generates text conditioned on preceding text |
| FORGE | Fake Online Recommendations in Generative Environments |
| GEO | Generative Engine Optimization; here includes fake-content promotion in the threat framing |
| SEO | Search engine optimization; upstream route to search visibility |
| RAG | Retrieval-augmented generation; generation using retrieved material |
| SERP | Search engine results page |
| SFT / RLHF | Supervised fine-tuning / reinforcement learning from human feedback |
| CJK | Chinese, Japanese, Korean character grouping used in string extraction |
| θ | Model parameters |
| q / W / S | User query / open web / search engine |
| E / K | Retrieved evidence bundle / number of documents, normally ten |
| W_fake / B_fake | Operator-authored fake pages / promoted fake brands |
| y / r | Recommendation; r is also reused for response or rank depending on context |
| Anchor | Chosen real-brand string to replace |
| A1 / A2 / A3 | Entity replacement / passage injection / full synthesis |
| Rec | Binary fake-target occurrence/recommendation indicator; scope ambiguity disclosed |
| Fooled rate | Percentage of evaluated responses counted as fake-brand recommendations |
| Top1 | Fake brand appears first in the recommendation ranking |
| Parametric prior | Model's evidence-free brand recommendation tendency |
| Jaccard similarity | Shared brands divided by all distinct brands in two sets |
| J(p) | Mean pairwise Jaccard for product query p |
| D1 / D2 / D3 | Skepticism prompt / model-prior filter / document-count filter |
| τ | Minimum document corroboration threshold for D3 |
| D/b | Documents per brand; concentration index |
| B/prod | Mean distinct brands in each ten-document query bundle |
| pp | Percentage points; absolute difference between percentages |
| CI / UB | Confidence interval / upper bound |
| κ | Reviewer agreement statistic reported as Cohen's kappa |
| ρ / Pearson r | Rank correlation / linear correlation |
| R² | Regression fit or predictive explained-variation measure, depending on evaluation |
| McNemar b,c | Opposite-direction disagreement counts in paired binary outcomes |
| rc_share | Reasoning characters divided by reasoning plus answer characters |
| AUC | Area-under-curve discrimination measure; exact curve type not specified here |
| Confabulation | Unsupported generated elaboration, including invented endorsement claims |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Main query coverage | 225 | product queries | 5 scenarios × 3 categories × 15 | Author-reported | p. 3 |
| Evidence slots | 2,250 | documents/anchors | 10 per query | Author-reported | pp. 13–14 |
| Main response count | 2,700 | cells | 12×225 | Analyst-derived | pp. 3–5 |
| Distinct corpus brands | 1,478 | strings | Deduplicated across categories | Author-reported | Table 3, p. 14 |
| Main model-rate range | 13.3–73.8 | % | Top-3 A1, n=225/model | Author-reported | Table 2, p. 5 |
| Overall main mean | 42.7 | % | Twelve models, fifteen categories | Author-reported | Table 2 |
| Dining / Phone-PC means | 81.7 / 22.8 | % | Main A1 category means | Author-reported | Table 2 |
| Category difference test | 99.4; p<10^−14 | χ²; probability | Friedman, 14 df | Author-reported | p. 4 |
| One-page maximum | 27 | % | Rank 1; six open-weights; Digital Products; n=45 | Author-reported | Table 8, p. 18 |
| Ten-page range | 44–100 | % | Same restricted panel | Visually readable | Table 8 |
| Anchor-stage recall | 48.2 / 72.9 / 100 | % | Relative to final curated anchors | Author-reported | Fig. 13, p. 14 |
| Reviewer agreement | 226/300; 75.3 | count; % | Stratified second review | Author-reported | pp. 14–15 |
| Cohen's κ | 0.752 [0.704,0.802] | statistic; 95% CI | 2,000 bootstrap resamples | Author-reported | pp. 14–15 |
| Anchor sensitivity | ρ=0.25; p=0.36 | statistics | Fifteen categories; 10,000 permutations | Author-reported | p. 15 |
| Brand agreement link | r=−0.65; p<0.01 | statistics | Category-level association | Author-reported | p. 7 |
| Anchor-free predictive R² | 0.672 | R² | Leave-one-out; 5 models×15 categories | Author-reported | p. 18 |
| Expanded predictive R² | 0.780 / 0.727 | R² | In-sample / leave-one-out; four-model feature panel | Author-reported | p. 18 |
| Model fixed effects alone | 0.434 | R² | Appendix E comparison | Author-reported | p. 18 |
| Mediation fraction | 53.1 | % | Reported alignment→fooled decomposition | Author-reported | p. 18 |
| Indirect-effect CI | [−0.354,−0.146] | 95% CI | 1,000 resamples, n=75 | Author-reported | p. 18 |
| A1/A2/A3 averages | 38 / 25 / 78 | % | 75 queries/model/style | Author-reported | Table 11 |
| English trial count | 360 | cells | 12×3×10 | Author-reported | p. 21 |
| English category averages | 43 / 58 / 87 | % | Smartphone / skincare / SF restaurants | Author-reported | Table 12 |
| No-evidence false positives | 5/1,680; 0.30 | count; % | All models, uneven per-model coverage | Author-reported | Table 10 |
| No-evidence Wilson UB | 0.69 | % | Pooled 95% upper bound | Author-reported | p. 19 |
| Clean false positives | 0/275; 0.00 | count; % | Original bundles | Author-reported | Table 10 |
| Clean Wilson UB | 1.34 | % | Pooled 95% upper bound | Author-reported | p. 19 |
| In-list fake-brand placement | 1,143/1,154; 99.0 | count; % | Triggered main outputs | Author-reported | p. 16 |
| Warning lexical flags | 10; 0.9 | count; % | Eight manually inspected | Author-reported | pp. 16–17 |
| Top-one placement range | 5–53 | % | Unconditional, rounded | Author-reported | Table 7 |
| D1 pooled change | +10.5 | pp | Twelve models, top-3 A1 | Author-reported | p. 22 |
| D1 subgroup changes | +24 / −3 | pp | Closed-source / open-weights | Author-reported | p. 22 |
| D2 catch / utility loss | 95 / 68 | % | Six open-weights; mean loss | Author-reported | pp. 8,24 |
| D3 catch / utility loss | 89.9 / 63 | % | All models; τ=4 | Author-reported | Table 13 |
| D3 threshold losses | 49 / 63 / 74 | % | τ=3/4/5 | Author-reported | Table 14 |
| Qwen ON/OFF | 56.9 / 38.7 | % | 225 matched cells/condition | Author-reported | Table 16 |
| Qwen paired effect / p | −18.2; 2.8×10^−7 | pp; probability | OFF−ON; exact McNemar | Author-reported | Table 16 |
| GLM ON/OFF | 80.4 / 71.6 | % | Same paired scope | Author-reported | Table 16 |
| GLM paired effect / p | −8.9; 1.7×10^−3 | pp; probability | Difference before rounding | Author-reported | Table 16 |
| Trace group counts | 340 / 307 / 703 | cells | A/B/C; six open-weights | Author-reported | Table 17 |
| Trace medians | 1,312 / 7,983 / 1,360 | characters | A/B/C | Author-reported | Table 17 |
| Trace shares | 0.578 / 0.879 / 0.569 | proportion | A/B/C means | Author-reported | Table 17 |
| B/C median ratio | 7,983÷1,360≈5.87 | ratio | Rejected mention versus fooled | Analyst-derived | Table 17 |
| Social-proof marker increase | 1.5–11 | ratio | Fooled versus resisted outputs | Author-reported | p. 7 |

Additional Appendix E detail: alignment Spearman correlations are −0.450,−0.668,−0.646,−0.511, mean absolute 0.569; evidence-brand-pool correlations are +0.636,+0.586,+0.825,+0.696, mean absolute 0.686. Commonality assigns 58% of additive R² to shared components, 29% to unique pool size, and 13% to unique alignment. Reverse mediation is reported as 28.1%. These are compressed secondary results with changing four/five-model panels, not independent experimental proof of a causal knowledge mechanism.

Appendix N additionally reports about 2,646 versus 518 reasoning tokens per ON cell for Qwen/GLM; Qwen OFF output-length d=−0.412, AUC=0.607; GLM OFF d=−0.059. Appendix O reports reasoning-share contrasts B versus A d=+1.22, B versus C +1.03, C versus A −0.03. Tokens and characters are different units and are not converted here.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Polluted evidence can induce fake recommendations | Nonzero rates in all twelve tested models | X1; Fig. 2; Table 2 | pp. 4–5 | Strong for this controlled bundle condition; no live-ranking success measured |
| One first-ranked page can suffice | Up to 27% in restricted panel | X3; Tables 8–9 | pp. 5,18 | Six open-weights models, 45 Digital Products queries |
| Pollution count compounds vulnerability | Higher endpoints and mostly increasing curves | X4; Fig. 5; Table 8 | pp. 6,18 | Near-monotonic, with documented countersteps |
| Category vulnerability is heterogeneous | 22.8% Phone/PC versus 81.7% dining; Friedman test | X1; Table 2 | pp. 4–5 | Controlled category sample; not universal market ordering |
| Brand agreement predicts resistance | r=−0.65, p<0.01; alignment analyses | X7; Fig. 8; Appendix E | pp. 6–7,17–18 | Observational; proxy and feature-scope qualifications |
| Reasoning toggle raises vulnerability in two models | Paired ON/OFF differences and discordant counts | X2; Table 16 | p. 25 | Stronger local causal design; unexplained headline-baseline mismatch |
| Explicit rejection accompanies deeper traces | Group B median 7,983 versus 1,312/1,360 | X8; Fig. 9; Table 17 | pp. 7,26 | Correlation; Rec/channel definition uncertainty |
| Fooled outputs invent social proof | Qualitative excerpts and marker ratios | X9; Table 5 | pp. 7,16 | Source-document absence is author-reported; raw pages/lexicon not independently available |
| Full synthesis is usually strongest | Eleven of twelve models; average 78% | X5; Table 11 | pp. 20–21 | Multiple simultaneous changes; Sonnet exception |
| English aggregate ordering reproduces | 43% < 58% < 87% | X6; Table 12 | pp. 21–23 | Every-model assertion contradicted; fresh products/geography |
| Skepticism can backfire | +10.5 pp overall; +24 pp closed-source | X10; Tables 13,15 | pp. 22–24 | One particular prompt, not all skepticism interventions |
| Filters sacrifice legitimate recommendations | Mean utility loss 68%/63% | X11–12; Fig. 11 | pp. 8,24 | Different scopes; utility measured as removed brand strings |
| Relevance to web-versus-standalone security | Retrieval exposes model to external polluted evidence | Architecture and false-positive controls | pp. 1–4,19 | Analyst inference; no matched standalone attack comparison |

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an assistant for five good products. Before answering, it reads ten web pages. The researchers take real pages and change some brand names to made-up names. The surrounding reviews still look normal. The assistant sometimes accepts the invented brand and puts it in its shopping advice.

The effect depends on where the changed pages appear, how many there are, the product category, and the model. One changed page at the top can be enough in the tested subset. Models tend to have more protection when they already agree about well-known real brands. But the study does not show that every web-connected assistant is less secure than the same model without web access.

Extra reasoning is not automatically a fix. In two tested models, turning reasoning off reduced fake recommendations. Yet some responses that carefully discussed and rejected a fake brand had much longer reasoning traces. A warning prompt also sometimes made things worse. Filters caught many fake brands but threw away many real recommendations too.

The main lesson is that an assistant can answer the right question using the wrong evidence. A convincing answer and a familiar-looking web source do not establish that a recommended product is genuine. This paper measures that problem under controlled conditions; several definition inconsistencies and missing raw artifacts still limit how precisely its deeper explanations can be checked.

## Completeness Audit

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract; §1 | Yes, text and visuals | Yes | Fully represented | Motivation treated as author-reported |
| §2 and autoregressive background | Yes, text only | Yes | Fully represented | No visual check of page 3 |
| §3.1 construction | Yes, text | Yes | Fully represented | Expanded with Appendix A |
| §3.2 attack styles | Yes, text and relevant visuals | Yes | Fully represented | Confounds preserved |
| §3.3 metric and validation | Yes | Yes | Fully represented | Definition conflict flagged |
| §4.1 settings | Yes | Yes | Fully represented | Missing implementation details disclosed |
| §4.2 main and targeted results | Yes | Yes | Fully represented | Experiment scopes kept separate |
| §5 agreement/trace/social proof subsections | Yes | Yes | Fully represented | Observational mechanisms qualified |
| §6 three defenses and category discussion | Yes | Yes | Fully represented | Utility denominator preserved |
| §7 related-work categories | Yes | Yes | Represented in compressed form | Authors' positioning; no outside literature judgments |
| §8 conclusion | Yes | Yes | Fully represented | Proposed defenses separated from tested ones |
| Limitations subsections, pp. 9–10 | Yes, p. 10 text only | Yes | Fully represented | All four main limitation headings covered |
| Ethical Considerations | Yes, text only | Yes | Represented in compressed form | Local simulation, private attack pages, defensive intent, no provider compensation |
| References | Yes, text | Yes | Inspected but deliberately omitted as repetitive/non-substantive | Individual bibliography entries not reprinted or validated |
| RQ1 and Appendix K RQ2/RQ3 | Yes | Yes | Fully represented | No manufactured formal hypotheses |
| Formal hypotheses | None identified | Accounted for | Missing from supplied material | Informal objectives distinguished |
| X1–X14 experiments/analyses | Yes | Yes | Fully represented | Numerical detail compressed in secondary panels |
| Figure 1 | Yes, visually | Yes | Fully represented | Decorative interface microtext compressed |
| Figures 2–5 | Yes, visually | Yes | Fully represented | Exact numbers from tables; unlabeled intervals not invented |
| Figures 6–9 | Yes, visually | Yes | Fully represented | Unlabeled bar values not estimated as exact |
| Figures 10–14 | Yes, visually | Yes | Fully represented | Diagram gate ambiguity and concentration interpretation noted |
| Table 1 | Yes | Yes | Fully represented | Conceptual taxonomy |
| Table 2 | Yes | Yes | Represented in compressed form | All model/category means; selected cell extremes, not all 180 cells reprinted |
| Table 3 | Yes | Yes | Represented in compressed form | Counts, ranges, deduplication, concentration retained |
| Table 4 | Yes | Yes | Represented in compressed form | Failure types and representative examples |
| Tables 5–7 | Yes | Yes | Represented in compressed form | Qualitative text and every metric type retained |
| Tables 8–9 | Yes | Yes | Represented in compressed form | Endpoint, primacy, exceptions and sample sizes retained |
| Table 10 | Yes | Yes | Fully represented | Every nonzero FP model and group sample counts retained |
| Table 11 | Yes | Yes | Represented in compressed form | Grand means, strongest conditions, exceptions retained |
| Table 12 | Yes | Yes | Represented in compressed form | Aggregate results and contradictory individual rows retained |
| Tables 13–15 | Yes | Yes | Represented in compressed form | Means, ranges, thresholds, scope and contradictions retained |
| Tables 16–17 | Yes | Yes | Fully represented | All principal paired/group numbers retained |
| Unnumbered factorization; equations (1)–(3) | Yes, text only | Yes | Fully represented | Extracted notation normalized with explanation |
| Equations (4)–(5) | Yes, text and visually | Yes | Fully represented | Scope/ordering ambiguities preserved |
| Algorithms/pseudocode/theorems | None identified | Accounted for | Missing from supplied material | Procedural workflow explained; no invented formal algorithm |
| Major conceptual/benchmark/method/empirical contributions | Yes | Yes | Fully represented | Novelty attributed to authors |
| Appendix A retrieval/prompts/review/statistics/sensitivity | Yes | Yes | Represented in compressed form | Full product list not visibly enumerated |
| Appendix B qualitative examples | Yes | Yes | Represented in compressed form | Long Chinese excerpts not fully retranscribed |
| Appendix C endorsement audit | Yes | Yes | Fully represented | Extrapolation distinguished from inspection |
| Appendix D Top1 parsing | Yes | Yes | Fully represented | Unranked outputs counted zero |
| Appendix E probe/predictor/regression/mediation subsections | Yes | Yes | Represented in compressed form | Principal numeric findings and sample ambiguities retained |
| Appendices F–G numerical scans | Yes | Yes | Represented in compressed form | Not longitudinal in time |
| Appendix H identifiers/configuration | Yes | Yes | Fully represented | Exact identifiers retained |
| Appendix I three-layer FP audit | Yes | Yes | Represented in compressed form | 80 prefixes, seven collisions, two FP-producing prefixes |
| Appendix J attack design/findings/implication | Yes | Yes | Fully represented | Density and ecology caveats retained |
| Appendix K setup/three findings | Yes | Yes | Fully represented | Overstated every-model ordering corrected by disclosure |
| Appendix L defense details/trade-off/reading | Yes | Yes | Fully represented | D2 prior-inference wording qualified |
| Appendix M category effects/mechanism | Yes | Yes | Fully represented | Mechanism attributed, exceptions checked |
| Appendix N method/scope/interpretation/OFF-length signal | Yes | Yes | Fully represented | Baseline mismatch flagged |
| Appendix O definitions/effect sizes/interpretation | Yes | Yes | Fully represented | Logical Rec conflict flagged |
| Supplied separate supplementary material | None | Accounted for | Missing from supplied material | No separate supplement claimed reviewed |
| Repository, harness, raw bundles/outputs | No | Accounted for | Inaccessible | Announced/referenced, not supplied or accessed |

### Missing or inaccessible material

No page is absent from the supplied text sequence. Images for pages 3 and 10–12 were not supplied, so those pages have text-only coverage. No repository files, evaluation harness, raw retrieval snapshot, complete enumerated product catalog, private polluted documents, model-output collection, annotation receipts, or full marker lexicons were inspected. The document announces a repository but does not provide its contents here. No separate embedded or supplementary artifact was available.

### Uncertain interpretations

The principal uncertainties are the occurrence-versus-recommendation definition of Rec; whether reasoning text belongs to output for mention grouping; mismatched ON baselines versus Table 2; prose/table disagreement about every-model English ordering; residual fake-brand catch at τ=3; D1 category wording; probe-versus-brand-slot counting; scope of closed-source evidence-free probes; and exact implementation of the six-predicate gate. Unlabeled confidence endpoints and small graphical positions remain non-exact. The full native-text extraction was not independently validated by reading the original PDF file.

### Deliberately compressed material

Dense matrices are summarized through model/category means, important extremes, exceptions, and conditions rather than reprinting every cell. Selected anchor examples and long Chinese model outputs are compressed without treating model assertions as facts. Bibliographic entries are grouped by the authors' related-work categories. Decorative diagram interface labels, repeated conclusions, and repeated defense descriptions are not separately reproduced. Appendix E statistics are retained in compact form rather than expanded into unsupported regression specifications.

### Potential omissions

Every substantive section, supplied figure, table, major equation, appendix, distinct experiment, stated limitation, and explicit research question in the inventory is represented or explicitly accounted for. The response does not preserve every table cell or every sentence; those reductions are disclosed above. Important missing implementation artifacts and contradictory definitions prevent a claim of independently complete scientific verification. Coverage is comprehensive for the supplied evidence, with the stated compression and uncertainties.
