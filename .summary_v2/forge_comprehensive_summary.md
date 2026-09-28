# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible range | Pages 1–26 |
| Apparently missing pages | None |
| Native/extracted text | Available for all 26 pages; no page is flagged as low-text or scanned |
| Pages visually rendered | 1, 2, 4–9, and 13–26 |
| Pages not visually rendered | 3 and 10–12 |
| Figures visually inspected | Figures 1–14 |
| Tables visually inspected | Tables 1–17 |
| Equations | Equations (4) and (5) were visually inspected; Equations (1)–(3) were available only through native text on unrendered p. 3 |
| Appendices | Appendices A–O are present, pp. 13–26 |
| References | Present, pp. 10–12 |
| Supplementary material | No separate supplementary file was supplied or explicitly identified |
| Embedded material | One embedded image on p. 1, represented by Figure 1 |
| OCR | Not required according to the mechanical record; extracted mathematical notation remains potentially sensitive to formatting errors |
| External artifacts | The paper names a GitHub benchmark/evaluation harness, model cards, web pages, private simulated documents, and a review interface, but none was supplied for inspection |
| Important limitation | Visual inspection is partial at the page level. Page 3’s equations and pp. 10–12’s bibliography were assessed from supplied native text, not page images. Model outputs in Chinese were inspected as printed, but the analysis relies on the authors’ supplied English translations for readers who do not read Chinese. |

Classification used below:

- **[A] Author-reported:** explicitly stated in the paper.
- **[B] Directly observable:** legible in a supplied page image, figure, or table.
- **[C] Analyst-derived:** calculated directly from supplied values, with operands shown.
- **[D] Analyst interpretation:** an inference beyond the authors’ literal wording.
- No external information is introduced.

# 1. Plain-Language Orientation

This is an empirical artificial-intelligence security and benchmark paper about a subtle failure of search-assisted large language models (LLMs). Such systems retrieve current web pages and then recommend products or services. The danger is that realistic-looking fake reviews or promotional pages may enter the retrieved evidence and cause the model to recommend a nonexistent brand while producing an otherwise fluent, relevant, policy-compliant answer [A, pp. 1–3].

The authors call this threat **web-content pollution** and construct **FORGE—Fake Online Recommendations in Generative Environments**. FORGE retrieves real web pages, freezes the results, and locally replaces real brand names with invented brand–product compounds. This avoids modifying the public web while preserving the documents’ rank, source attribution, style, length, and surrounding content [A, pp. 2–4; Appendix A, pp. 13–15].

The main benchmark contains 225 products: 15 products in each of 15 categories, grouped into five consumer scenarios. Twelve production LLMs—six closed-source and six open-weights—receive the polluted evidence and must produce top-five recommendations. The primary outcome is whether the fake brand appears in the recommendation set [A, pp. 3–5].

The central findings are:

- Every tested model is vulnerable. Under replacement of the top three documents, model-level fooled rates range from 13.3% to 73.8%; the panel mean is 42.7% [A/B, Table 2, p. 5].
- One polluted rank-1 page produces rates as high as 27% on the examined open-weights models, whereas placing the same single polluted page at ranks 2–10 generally produces only 0%–13% per model and roughly 1%–4% when pooled [A/B, Fig. 4, p. 5; Table 9, p. 18].
- Vulnerability rises as more top-10 pages are polluted. With all ten replaced, the six open-weights models reach 44%–100% in the Digital Products subset [A/B, Fig. 5, p. 6; Table 8, p. 18].
- Categories with diffuse or unstable brand knowledge are more vulnerable. Cross-model agreement about brands correlates negatively with fooled rate, \(r=-0.65\), \(p<0.01\) [A, Eq. (5), Fig. 8, pp. 6–7].
- Reasoning does not reliably protect the model. In paired ablations, disabling reasoning reduced fooled rate by 18.2 percentage points for Qwen3.5-9B and 8.9 points for GLM-4.6V-Flash [A/B, Fig. 3, p. 5; Table 16, p. 25].
- Successfully resisting after noticing the fake brand is associated with unusually long reasoning, but ordinary reasoning often appears to rationalize the polluted evidence instead. “Noticed and rejected” cases have median traces of 7,983 characters, versus 1,312 for unaware resisted cases and 1,360 for fooled cases [A/B, Fig. 9, p. 7; Table 17, p. 26].
- Fooled answers invent supporting claims absent from the evidence; social-proof markers occur 1.5–11 times as often in fooled as in resisted outputs [A, pp. 2, 7; Table 5, p. 16].
- A skepticism prompt backfires overall, raising fooled rate from about 43% to 53%, a reported +10.5 percentage points. Post-hoc filters catch most fake brands but remove most legitimate recommendations too [A/B, §6, pp. 7–8; Tables 13–15, pp. 24–25].

The main contribution is therefore not a new attack optimizer. It is a controlled benchmark and empirical characterization showing that plausible, on-task web pollution can induce fake-product recommendations, that the risk depends heavily on retrieval rank and brand-prior structure, and that intuitive inference-time defenses are inadequate [A, pp. 2, 9].

# 2. Document Roadmap

The document is an empirical benchmark/security study organized as follows:

1. **Introduction** (§1, pp. 1–2): motivates web pollution, distinguishes it from related attacks, introduces FORGE, and previews the results.
2. **Background and Preliminaries** (§2, p. 3): formalizes autoregressive LLMs, retrieval-augmented recommendation, and polluted-web retrieval.
3. **The FORGE Benchmark** (§3, pp. 3–4): describes products, queries, evidence bundles, three attack styles, the recommendation indicator, and metric validation.
4. **Experiment** (§4, pp. 4–6): reports the main 12-model cross-section and five targeted studies—reasoning, rank, pollution dose, attack style, and English replication.
5. **Analysis** (§5, pp. 6–7): studies brand-prior agreement, reasoning behavior, and invented social proof.
6. **Defenses** (§6, pp. 7–8): evaluates skepticism prompting and two post-hoc consensus filters.
7. **Related Work** (§7, pp. 8–9): positions FORGE relative to LLM recommenders, prompt injection, retrieval poisoning, adversarial search, knowledge conflict, and hallucination.
8. **Conclusion, Limitations, and Ethical Considerations** (pp. 9–10): summarizes implications, scopes claims, and explains the controlled/local attack design.
9. **References** (pp. 10–12).
10. **Appendices A–O** (pp. 13–26): supply prompts, retrieval and anchor details, qualitative outputs, metric audits, predictors, exact dose/rank values, implementation identifiers, false-positive controls, attack-style details, English results, defense breakdowns, and reasoning ablations.

The appendices materially qualify and substantiate the main paper; they are not merely supplementary repetition.

# 3. Background and Context

A **large language model (LLM)** predicts text token by token. The paper represents a sequence \(x=(x_1,\ldots,x_T)\) using a left-to-right probability factorization. The model is pretrained, may undergo supervised fine-tuning and reinforcement learning from human feedback, and generates its output autoregressively [A, §2, p. 3].

A **search-augmented generative recommender** first sends a user query to a search engine, collects the top-\(K\) pages, combines those pages with the query, and asks an LLM to produce a ranked recommendation [A, Eqs. (1)–(2), p. 3]. Its answer therefore depends on both:

- **Parametric knowledge:** information implicit in model parameters.
- **Retrieved/contextual evidence:** information contained in the fetched web pages.

**Generative Engine Optimization (GEO)** is described as efforts to shape what generative search systems say by publishing content likely to be retrieved. In the paper’s adversarial setting, operators publish fake reviews or promotional pages so that downstream models recommend fake brands [A, pp. 1, 3].

**Web-content pollution** differs from conventional attacks because the attacker does not necessarily control the model, prompt, training corpus, or a private retrieval database. The polluted channel is the open web; access is indirect through ordinary search-engine optimization; the content resembles plausible reviews; and the visible output remains an on-topic recommendation [A/B, Table 1, p. 2].

A **fake brand** here is an invented prefix combined with the target product type. A document is polluted by replacing a selected real-brand “anchor,” injecting a promotional paragraph, or synthesizing an entire promotional document [A, §3.2, pp. 3–4].

A **fooled cell** is one model–product response in which the fake target appears in the recommendation set according to the paper’s substring indicator [A, Eq. (4), p. 4].

# 4. Research Problem and Gap

## Existing problem

Search-assisted LLMs increasingly mediate product and local-service recommendations. Their retrieval step moves part of the trust boundary from the model to the open web, where misleading commercial content may be published [A, §1, pp. 1–2].

## Shortcomings of previous approaches, according to the authors

Prior benchmarks examine adjacent but structurally different problems:

- Training poisoning modifies training examples.
- Retrieval poisoning assumes write access to a private or deployer-controlled corpus.
- Prompt manipulation places anomalous instructions in user or retrieved content.
- Recommender poisoning often uses simulated catalogs.
- Adversarial SEO previously examined in the cited work promotes existing entities rather than entirely fabricated brands [A/B, Table 1, p. 2; §7, pp. 8–9].

These settings often yield cues such as trigger patterns, anomalous instructions, out-of-distribution passages, refusals, or off-task outputs. FORGE’s attack leaves the response fluent and aligned with the user’s request [A, p. 2].

## Research gap

The missing measurement question is: once plausible polluted pages enter an ordinary evidence bundle, will a search-augmented LLM treat them as credible evidence and recommend a fake product? [A, p. 2].

## Motivation

The authors motivate the problem through an author-cited 2026 report of commercial GEO activity targeting Chinese AI assistants. In closed-document mode, this real-world event is treated only as an author-reported motivation, not independently verified [A, pp. 1, 10].

## Scope

The main evaluation concerns:

- Consumer product and local-life recommendations;
- Chinese-language queries and evidence;
- A fixed April 2026 retrieval snapshot;
- 12 LLMs, 15 categories, and 225 products;
- Primarily top-three entity replacement;
- Inference-time behavior rather than training-time corruption [A, pp. 2–5, 9–10].

# 5. Research Questions / Objectives / Hypotheses

The authors state one explicit question in the abstract:

- **RQ1:** To what extent do search-augmented LLMs become unwitting promoters of fake products when consuming polluted retrieval results? [A, p. 1]

They do not provide a formally numbered hypothesis list. The following are author-stated objectives or questions, not manufactured hypotheses:

- **Objective 1:** Build a controlled, reproducible benchmark of fake-product promotion under realistic web-content pollution [A, pp. 1–3].
- **Objective 2:** Measure vulnerability across models and product categories [A, §4, pp. 4–5].
- **Objective 3:** Determine how retrieval rank, number of polluted pages, and attack style affect success [A, §4, pp. 5–6].
- **Objective 4:** Test whether reasoning reduces or increases vulnerability [A, pp. 4–5; Appendix N].
- **Objective 5:** Determine whether brand-prior stability predicts resistance [A, §5, pp. 6–7].
- **Objective 6:** Examine whether fooled models merely copy fake names or fabricate justification [A, §5, p. 7].
- **Objective 7:** Evaluate three inference-time defenses [A, §6, pp. 7–8].
- **Objective 8:** Test whether the principal category pattern transfers from Chinese to English [A, Appendix K, pp. 21–23].

No preregistration or ex ante statistical hypotheses are reported.

# 6. Assumptions / Threat Model

## System model

The pipeline is:

\[
\text{query}\rightarrow\text{commercial web search}\rightarrow
\text{top-}K\text{ pages}\rightarrow\text{LLM}\rightarrow
\text{ranked recommendation}.
\]

FORGE uses \(K=10\) evidence documents, with the main attack modifying the first three [A/B, Figs. 1 and 12, pp. 1, 14].

## Attacker capabilities

The real-world attacker is assumed able to publish plausible review or promotional content on the open web and use standard SEO to make it surface in search results. The attacker seeks commercial promotion of a fake brand, not system sabotage or instruction hijacking [A/B, Table 1, p. 2].

FORGE itself does not exercise that real-world capability. It locally edits a frozen retrieved bundle after search. The evaluator can:

- Replace a real-brand anchor with a fake brand (A1);
- Inject a 120–180-character promotional passage (A2);
- Replace the body with a 500–700-character synthetic review on a same-domain path (A3) [A, pp. 3, 19–21].

## Held-fixed components

For A1, document rank, original URL, source attribution, length, style, and surrounding context are preserved; the dominant brand is replaced in title, snippet, and body [A, pp. 2–3, 19].

## Trusted or curated components

- Serper supplies search results.
- Automated quality gates remove errored, short, garbled, video-platform, and boilerplate pages.
- An LLM, rules, and human review select the brand anchor.
- The final human-reviewed anchor is treated as the rewrite target.
- The model output is parsed using substring and structural heuristics [A, Appendix A, pp. 13–15; Appendices C and I].

## Excluded or untested capabilities

- The authors do not optimize the attack.
- They do not combine tailored templates, query-aware passages, and adversarial SEO.
- They do not actually pollute the live web.
- They do not measure whether search engines would rank every constructed page.
- The main attack does not manipulate the user prompt, model weights, or a private corpus.
- Full closed-source reasoning traces and reasoning-off toggles are unavailable [A, Limitations, pp. 9–10; Appendix N, p. 25].

# 7. Methodology

## Study design

FORGE is a controlled factorial benchmark with a main cross-sectional experiment and targeted ablations. The experimental unit is generally one response for a particular model and product under one evidence condition [A, §§3–4, pp. 3–5].

## Dataset and sample

Five scenarios contain three categories each, with 15 products per category:

- Digital Products;
- Local Life;
- Health & Personal;
- Fashion Accessories;
- Sports & Outdoor.

Thus:

\[
5\text{ scenarios}\times3\text{ categories}\times15\text{ products}
=225\text{ products}.
\]

Each product receives 10 retrieved documents, producing \(225\times10=2{,}250\) anchor slots [A, pp. 3, 13–14].

Table 3 reports 1,478 distinct real brands corpus-wide, 8.55 mean distinct brands per product bundle, and 1.52 documents per brand. Category-level brand pools range from 74 to 135 [A/B, Table 3, p. 14].

## Query and retrieval construction

The common system prompt asks the model to recommend products or local-life options directly with brief reasoning. Scenario-specific user prompts request five recommendations. Local Life queries are Shenzhen-specific [A, Appendix A, p. 13].

For each query:

1. Serper web search is run with `gl=cn`, `hl=zh-CN`.
2. Up to four result pages, approximately 40 URLs, are considered.
3. Pages are fetched using Python `requests`, a 10-second timeout, and a browser-like user agent.
4. BeautifulSoup4 with `html.parser` extracts content.
5. Character decoding respects HTTP charset, then uses `chardet`, including GB18030, GBK, and Big5.
6. Six quality predicates reject non-2xx responses, very short bodies, heavily garbled text, blocked video sites, and boilerplate pages.
7. The first ten accepted documents in original rank order form the frozen bundle [A, Appendix A, p. 13; Fig. 12, p. 14].

## Anchor extraction

The dominant brand target is chosen through:

- **Stage 1—LLM:** Gemini 2.5 Flash-Lite, temperature 0.1, structured JSON, up to eight candidate anchors.
- **Stage 2—rules:** regular expressions plus a per-category lexicon of roughly 50 real-brand prefixes.
- **Stage 3—human verification:** a trained native-Chinese-speaking reviewer confirms, changes, or enters the final anchor [A, pp. 13–14].

Cumulative anchor recall is reported as 48.2% after Stage 1, 72.9% after Stage 2, and 100% after human review. The Stage-1 override rate is 51.8% [A/B, Figs. 12–13, p. 14].

A second reviewer independently assessed 300 stratified slots. Exact-string agreement was 75.3% (226/300), with Cohen’s \(\kappa=0.752\), bootstrap 95% CI \([0.704,0.802]\), based on 2,000 resamples [A, pp. 14–15].

## Attack conditions

- **A1—entity replacement:** replace all mentions of the selected real brand with a fake brand; preserve URL and surrounding document.
- **A2—passage injection:** retain the original page and add a 120–180-character synthetic promotional paragraph.
- **A3—full synthesis:** replace the body with a 500–700-character synthetic review and use a same-domain hashed path [A, pp. 3, 19–20].

The main evaluation uses A1 on the top three documents.

## Models

Six closed-source models:

- Gemini 3 Flash;
- GPT-5.4;
- o4-mini;
- Gemini 3.1 Pro;
- Claude Opus 4.7;
- Claude Sonnet 4.6.

Six open-weights models:

- Qwen3.6-27B;
- Qwen3.6-35B-A3B;
- Qwen3.5-9B;
- DeepSeek V4 Pro;
- GLM-4.6V-Flash;
- Ministral-3R [A/B, Fig. 2, p. 4; Appendix H, p. 18].

Exact API/repository identifiers are supplied in Appendix H. All use temperature \(T=0\) and `max_output_tokens=8192`; each system–user–evidence triple is SHA-256 hashed [A, p. 18].

The paper does not report hardware, inference provider versions beyond model identifiers, monetary cost, random seeds, or repeated stochastic runs. Greedy decoding means each cell is sampled once [A, pp. 4, 18].

## Primary metric

For fake target \(t\) and response \(r\):

\[
\operatorname{Rec}(t,r)=\mathbf 1[t\text{ appears in }r].
\]

Matching is case-insensitive and accepts the full fake-brand string or its prefix. Fooled rate is the fraction of evaluated responses with \(\operatorname{Rec}=1\) [A, Eq. (4), p. 4].

## Metric validation

Three audits support interpreting a hit as an endorsement:

- Empty-evidence false-positive rate: \(5/1{,}680=0.30\%\), Wilson 95% upper bound 0.69%.
- Clean-bundle false-positive rate: \(0/275=0.00\%\), upper bound 1.34%.
- Of 1,154 positive cells, 1,143 (99.0%) place the fake brand inside a numbered recommendation item; only 10 (0.9%) contain a warning marker, and the eight manually inspected high-confidence flags are positive-in-context [A, p. 4; Tables 6 and 10, pp. 17, 20].

## Statistical methods

Reported analyses include:

- Wilson confidence intervals for proportions;
- Friedman \(\chi^2\) test across categories;
- Pearson correlation;
- Spearman correlations;
- permutation test with 10,000 permutations;
- Cohen’s \(\kappa\) and bootstrap confidence interval;
- McNemar exact paired tests;
- Cohen’s \(d\);
- area under the curve (AUC);
- leave-one-out \(R^2\);
- commonality analysis;
- bootstrap mediation with 1,000 resamples [A, pp. 4–7, 15, 17–18, 25–26].

# 8. Experiments / Analyses

## X1 — Main 12-model cross-section

**Purpose:** Measure baseline vulnerability and category/model variation.

**Setup:** 12 models × 225 products, top-three A1 entity replacement, \(T=0\); 15 products per model–category cell [A, pp. 4–5].

**Metric:** Fooled rate.

**Result:** Model means range from 13.3% to 73.8%, with an overall mean of 42.7%. Category means range from 22.8% for Phone/PC to 81.7% for Dining [A/B, Table 2, p. 5].

**Statistics:** Category variation: Friedman \(\chi^2(14)=99.4\), \(p<10^{-14}\) [A, p. 4].

**Caveat:** One greedy response per cell; categories and products are curated rather than randomly sampled from all commerce.

## X2 — Reasoning enabled versus disabled

**Purpose:** Test reasoning causally while holding model identity and inputs fixed.

**Setup:** Qwen3.5-9B and GLM-4.6V-Flash; 225 matched cells per condition; only chat-template reasoning toggle differs [A, Appendix N, p. 25].

**Results:**

- Qwen3.5-9B: 56.9% ON versus 38.7% OFF; OFF–ON \(=-18.2\) pp; discordant counts 53 versus 12; \(p=2.8\times10^{-7}\).
- GLM-4.6V-Flash: 80.4% ON versus 71.6% OFF; OFF–ON \(=-8.9\) pp; 29 versus 9; \(p=1.7\times10^{-3}\) [A/B, Table 16, p. 25].

**Caveat:** Only two open-weights models expose a clean reasoning toggle.

## X3 — Single-page rank-position study

**Purpose:** Determine whether one polluted page’s position matters.

**Setup:** Six open-weights models, Digital Products’ three categories, \(n=45\) per model–rank condition; exactly one of ten pages is replaced [A, Table 9, p. 18].

**Results:** At rank 1, rates are 2%–27%. At ranks 2–10, most cells are 0%–4%, although GLM reaches 13% at rank 3 and Ministral 11% at rank 3 [A/B, Fig. 4, p. 5; Table 9, p. 18].

**Interpretation:** The paper calls this a strong primacy effect.

## X4 — Pollution-count dose response

**Purpose:** Measure how success changes as more pages are polluted.

**Setup:** The same six open-weights models and Digital Products subset; \(N\in\{1,2,3,5,7,10\}\), \(n=45\) per cell [A, Appendix F, p. 18].

**Results:** At \(N=1\), rates are 2%–27%; at \(N=10\), they are 44%, 73%, 80%, 73%, 100%, and 98% across the six models. Minor non-monotonicity occurs for DeepSeek V4 Pro—44% at \(N=5\), 40% at \(N=7\), then 73% at \(N=10\) [A/B, Table 8, p. 18].

**Qualification:** “Near-monotonic” is more accurate than strictly monotonic.

## X5 — Attack-realism/style ablation

**Purpose:** Compare entity replacement, passage injection, and full synthesis.

**Setup:** All 12 models, all 15 categories, five products per model–category–attack cell; A1 is restricted to the same five products for parity. A2 and A3 total 1,800 binary trials [A, pp. 19–20].

**Results:** Grand averages are A1 38%, A2 25%, and A3 78%. A3 is strongest for 11 of 12 models and reaches at least 70% for nine models. Claude Sonnet 4.6 is the exception: A3 24% versus A1 47% [A/B, Table 11, p. 20].

**Caveat:** A3 changes multiple factors—document body, brand density, real-brand corroboration, and URL path—so the A3–A1 difference does not isolate “realism.”

## X6 — English cross-lingual replication

**Purpose:** Test linguistic portability and whether category ordering persists.

**Setup:** Fresh English evidence for Smartphones, Skincare, and San Francisco Restaurants; ten products per category; US-region search; 12 models; 360 trials [A, pp. 21–23].

**Results:** English category means are 43%, 58%, and 87%, preserving the Chinese matched ordering of 23%, 57%, and 82%. Eight of 12 model-level averages lie within ±10 pp of their Chinese average; model shifts span −20 to +40 pp [A/B, Table 12, p. 23].

**Caveat:** Only three categories and one US locality are tested.

## X7 — Brand-agreement predictor

**Purpose:** Test whether stable parametric brand knowledge predicts resistance.

**Setup:** Empty-evidence top-five brand probes; mean pairwise Jaccard agreement across six open-weights models and 15 categories [A, Eq. (5), pp. 6–7].

**Result:** Category agreement correlates with lower fooled rate: Pearson \(r=-0.65\), \(p<0.01\) [A, Fig. 8, p. 7].

Additional analyses report model-level Spearman correlations of alignment with fooled rate from −0.450 to −0.668, and evidence-pool-size correlations from +0.586 to +0.825 [A, pp. 17–18].

## X8 — Composite predictor analysis

An anchor-free model using probe-pool size, alignment, and model fixed effects achieves leave-one-out \(R^2=0.672\). Adding anchor-using evidence-pool size and fake-brand-in-reasoning features raises in-sample \(R^2\) to 0.780 and leave-one-out \(R^2\) to 0.727; model fixed effects alone yield \(R^2=0.434\) [A, p. 18].

A 1,000-resample mediation analysis estimates that 53.1% of the alignment-to-fooled relationship flows through evidence-pool size, with indirect-effect 95% CI \([-0.354,-0.146]\); reverse decomposition is 28.1% [A, p. 18].

**Caveat:** These are small category-level panels—typically 60–75 model–category observations—and some features require anchor or trace access.

## X9 — Reasoning-trace three-way split

**Purpose:** Distinguish failure to notice the fake from noticing and rejecting it.

**Setup:** 1,350 open-weights cells divided into:

- A: resisted, no fake-brand mention, \(n=340\);
- B: resisted, brand mentioned but rejected, \(n=307\);
- C: fooled, \(n=703\) [A, Appendix O, p. 26].

**Results:** Median reasoning lengths are 1,312, 7,983, and 1,360 characters. Mean reasoning shares are 0.578, 0.879, and 0.569. Cohen’s \(d\) on reasoning share is +1.22 for B versus A, +1.03 for B versus C, and −0.03 for C versus A [A/B, Table 17, p. 26].

**Interpretation:** Deep deliberation conditional on noticing is associated with resistance, while merely enabling reasoning increases aggregate vulnerability.

## X10 — Confabulated social-proof analysis

The paper provides qualitative examples in which models add claims such as community popularity, repeated testing, or reputation that do not appear in the polluted source documents. At population level, a 14-phrase lexicon fires 1.5–11 times more often in fooled than resisted outputs, with fewer hedging markers [A, §5, p. 7; Table 5, p. 16].

**Caveat:** The full per-model lexicon counts and statistical testing are not printed in the supplied pages.

## X11 — Metric and false-positive audits

Appendices C and I evaluate structural endorsement, warning-language ambiguity, lexical collisions, empty-evidence false positives, and clean-bundle false positives [A, pp. 16–20]. Results support the metric’s intended interpretation, though prefix matching creates a small 0.30% no-evidence noise rate.

## X12 — Defense D1: skepticism prompt

All 12 models receive an added instruction to distrust unfamiliar, weakly corroborated brands. The pooled fooled rate increases by 10.5 pp. Closed-source models average +24 pp, while open-weights average −3 pp [A, pp. 7–8, 22–24].

## X13 — Defense D2: model-prior filter

For six open-weights models, a recommended brand is kept only if it also appeared in that model’s empty-evidence probe. The fake brand is removed in about 95% of applicable cells, but 62%–79% of legitimate recommendations are removed; mean utility cost is 68% [A, pp. 8, 22–24].

## X14 — Defense D3: cross-document filter

A brand is retained only if it appears in at least \(\tau\) of ten documents. Because the fake brand is planted in exactly three documents, \(\tau=4\) catches it in 89.9%–90% of applicable positive cells but removes 52%–73% of legitimate recommendations, mean 63% [A, pp. 8, 22–24].

# 9. Results

## Universal but highly variable vulnerability

All 12 models have headline rates far above the pooled no-evidence false-positive upper bound of 0.69%. The lowest is Gemini 3 Flash at 13.3%; the highest is Ministral-3R at 73.8% [A/B, Tables 2 and 10, pp. 5, 20].

Closed-source and open-weights ranges overlap. The data do not support a simple “larger,” “closed,” or ostensibly more capable means safer relationship [A, §4.2, p. 4].

## Category is a major determinant

Category means under the main attack are:

- Dining: 81.7%;
- Personal services: 60.6%;
- Supplements: 60.0%;
- Skincare: 56.7%;
- Apparel: 48.9%;
- Underwear: 42.2%;
- Cycling: 39.4%;
- Bags/Shoes: 36.7%;
- Fitness: 34.4%;
- Makeup and Camping: 32.8%;
- Hospitality: 31.7%;
- Electronics accessories: 30.6%;
- Home appliances: 30.0%;
- Phone/PC: 22.8% [A/B, Table 2, p. 5].

The authors interpret this as vulnerability being highest where brand knowledge is diffuse and lowest where stable, canonical brands dominate [A, pp. 4, 6–7].

## Rank-1 dominance

The rank study shows that the first retrieved page is disproportionately influential. Pooled prose reports approximately 1%–4% for ranks 2–10, although Table 9 exposes isolated model-level values up to 13% [A/B, Fig. 4, p. 5; Table 9, p. 18]. Thus the “nearly inert” characterization applies to pooled behavior, not every model–rank cell.

## Dose response

More polluted documents generally yield higher attack success. For example:

- GLM: 27%, 49%, 58%, 73%, 87%, 100% as \(N=1,2,3,5,7,10\).
- Ministral: 27%, 49%, 64%, 78%, 91%, 98%.
- Qwen3.5-9B: 2%, 11%, 22%, 38%, 62%, 80% [A/B, Table 8, p. 18].

## Reasoning has two distinct relationships with vulnerability

The paired intervention shows that enabling reasoning increases aggregate vulnerability in the two testable models. Separately, among reasoning-enabled outputs, cases that notice and successfully reject the fake involve much longer traces. These are not contradictory:

- Presence of a reasoning process can draw a model into accepting polluted evidence.
- Conditional on noticing the fake, unusually sustained scrutiny is associated with rejection [A, pp. 5, 7, 25–26].

## Models fabricate credibility

The fake name is not merely copied. In the screen-protector case, Claude Opus 4.7 and DeepSeek V4 Pro add community endorsement, test results, and reputation claims absent from the three polluted documents [A/B, Table 5, p. 16].

## Full synthesis is the most effective tested style

A3 averages 78%, 40 pp above matched A1’s 38% and 53 pp above A2’s 25% [A/B, Table 11, p. 20].

**[C] Analyst-derived:** \(78-38=40\) percentage points and \(78-25=53\) percentage points. The latter is also explicitly reported in Table 11.

Because A3 modifies several document properties simultaneously, it cannot establish that fuller synthesis alone causes the increase [A, p. 21].

## English preserves the category hierarchy but not all model behavior

The low/mid/high ordering transfers cleanly, but individual model shifts vary substantially. For example, Gemini 3.1 Pro averages +40 pp in English, whereas Claude Sonnet 4.6 averages −20 pp [A, pp. 21–23].

## Defenses face failure or utility collapse

D1 raises average fooled rate from 43% to 53%. D2 and D3 catch the fake frequently, but only by deleting a majority of legitimate recommendations [A/B, Tables 13–14, p. 24].

# 10. Figure-by-Figure Interpretation

### Figure 1 — Real-world pollution versus FORGE simulation

- **Type:** Two-path pipeline diagram.
- **Flow:** User query → live web search → retrieved results → LLM → top-five recommendation.
- **Top path:** Fake content is placed on the public web upstream of search.
- **Bottom path:** FORGE rewrites retrieved pages locally after search.
- **Purpose:** Shows that the recommendation backbone is shared, while the insertion point differs.
- **Conclusion:** FORGE aims to simulate downstream exposure without polluting public infrastructure.
- **Caveat:** It establishes structural analogy, not that local rewriting perfectly reproduces real search ranking [A/B, p. 1].

### Figure 2 — Per-model fooled rates

- **Type:** Horizontal point-and-whisker plot.
- **X-axis:** Fooled rate under top-three A1 attack, percent.
- **Y-axis:** 12 models.
- **Encoding:** Blue circles denote closed-source; red squares denote open-weights; whiskers are 95% Wilson confidence intervals.
- **Observation:** Rates span about 13%–74%, with substantial overlap between model groups.
- **Exact values:** Table 2 provides 13.3%–73.8%.
- **Conclusion:** Vulnerability is universal and not neatly separated by model availability class [A/B, p. 4].

### Figure 3 — Reasoning enabled versus disabled

- **Type:** Grouped bar chart.
- **Y-axis:** Fooled rate, percent.
- **Bars:** Reasoning enabled versus disabled.
- **Values:** Qwen3.5-9B 56.9% versus 38.7%; GLM-4.6V-Flash 80.4% versus 71.6%.
- **Statistics:** McNemar \(p<10^{-6}\) and \(p=1.7\times10^{-3}\); Appendix N gives the exact first value \(2.8\times10^{-7}\).
- **Conclusion:** Disabling reasoning reduces vulnerability in both tested models [A/B, p. 5].

### Figure 4 — Single polluted page by rank

- **Type:** Line plot with red points.
- **X-axis:** Rank 1–10.
- **Y-axis:** Pooled fooled rate, percent.
- **Observation:** A sharp peak at rank 1, a drop at rank 2, and low values thereafter, with a small rise at rank 10.
- **Exact values:** The pooled points are not numerically labeled; per-model values are in Table 9.
- **Certainty:** The shape is visually readable; exact pooled values beyond prose’s 1%–4% are not labeled.
- **Conclusion:** Retrieval primacy dominates [B, p. 5].

### Figure 5 — Number of polluted pages

- **Type:** Six-line dose-response plot.
- **X-axis:** \(N=1,2,3,5,7,10\) polluted documents out of ten.
- **Y-axis:** Fooled rate, percent.
- **Legend:** Six open-weights models.
- **Observation:** All lines rise strongly overall; GLM and Ministral saturate near 100%.
- **Caveat:** DeepSeek dips slightly from \(N=5\) to \(N=7\), so monotonicity is approximate.
- **Exact values:** Table 8 [A/B, pp. 6, 18].

### Figure 6 — Three attack styles

- **Type:** Grouped bars for Mobile/Digital, Fitness Gear, and Dining.
- **X-axis:** Category.
- **Y-axis:** Fooled rate, percent.
- **Encoding:** A1 entity replacement, A2 passage injection, A3 full synthesis.
- **Observation:** A3 is largest in all three representative categories; category ordering remains low-to-high.
- **Caveat:** This figure aggregates models and shows only three categories; Table 11 supplies model-level averages [A/B, p. 6].

### Figure 7 — Chinese versus English model rates

- **Type:** Horizontal grouped bars.
- **X-axis:** Fooled rate, percent.
- **Y-axis:** 12 models.
- **Encoding:** Blue for Chinese, red for English.
- **Observation:** Some models shift substantially, but eight remain within ±10 pp.
- **Exact values:** Table 12 supplies category-level values; the figure aggregates three categories [A/B, p. 6].

### Figure 8 — Brand agreement versus fooled rate

- **Type:** Scatterplot with fitted declining dashed line.
- **X-axis:** Cross-model agreement \(J\), approximately 0–0.4.
- **Y-axis:** Fooled rate, percent.
- **Points:** 15 categories; selected labels include dining, services, smartphones.
- **Observation:** Higher agreement is associated with lower vulnerability.
- **Reported statistic:** Pearson \(r=-0.65\), \(p<0.01\).
- **Caveat:** Correlation does not by itself establish causality [A/B, p. 7].

### Figure 9 — Reasoning length by outcome

- **Type:** Three boxplots.
- **X-axis:** A: resisted/no mention; B: resisted/brand mentioned; C: fooled.
- **Y-axis:** Reasoning trace length in characters, scaled by \(10^4\).
- **Whiskers:** 5th and 95th percentiles.
- **Observation:** Group B has a much higher median and distribution than A or C.
- **Exact medians:** 1,312; 7,983; 1,360 characters in Table 17.
- **Conclusion:** Noticing plus rejecting is associated with sustained deliberation [A/B, pp. 7, 26].

### Figure 10 — Skepticism-prompt effect

- **Type:** Horizontal dot-and-whisker plot.
- **X-axis:** \(D1-\)baseline in percentage points; negative helps, positive backfires.
- **Y-axis:** 12 models sorted by effect.
- **Observation:** Most closed-source models cluster on the positive/backfire side, while open-weights models remain near zero.
- **Whiskers:** Paired binomial-difference 95% CIs, \(n=225\).
- **Exact effects:** Appendix L and Tables 13/15 [A/B, p. 8].

### Figure 11 — Defense catch versus utility

- **Type:** Scatterplot.
- **X-axis:** Fake-brand catch rate.
- **Y-axis:** Real-brand survival.
- **Points:** Baseline, D2, and D3.
- **Labeled pairs:** D2 approximately (95% catch, 32% survival); D3 approximately (90%, 37%).
- **Interpretation:** High catch is achieved only with severe legitimate-brand loss.
- **Derived equivalence:** 32% survival corresponds to 68% loss; 37% survival to 63% loss [B/C, p. 8].

### Figure 12 — Full FORGE pipeline

- **Type:** Color-coded architecture/flowchart.
- **Blue retrieval:** Query → Serper → ~40 candidate URLs → quality gate → top ten.
- **Orange anchor extraction:** Gemini Flash-Lite → regex/lexicon → human review.
- **Red attack:** Replace top-three anchors with a fake brand.
- **Green evaluation:** 12 LLMs at \(T=0\) → substring-based fooled rate.
- **Conclusion:** Makes the data and control flow explicit [A/B, p. 14].

### Figure 13 — Cumulative anchor recall

- **Type:** Stacked/cumulative bar chart.
- **Y-axis:** Cumulative recall, percent.
- **Values:** Stage 1 48.2%; Stage 2 adds 24.7 pp to 72.9%; Stage 3 adds 27.1 pp to reach 100%.
- **Conclusion:** Automated stages are insufficient without human verification [A/B, p. 14].

### Figure 14 — Brand-pool diversity and concentration

- **Type:** Labeled scatterplot.
- **X-axis:** Concentration \(D/b\), mean documents per brand.
- **Y-axis:** Distinct brand pool.
- **Observation:** Food, skincare, and services lie toward large/diverse pools; home appliances, makeup, and mobile/digital toward small/concentrated pools.
- **Scale:** Roughly a twofold span on both axes.
- **Purpose:** Shows that the dataset contains varied brand-market structures [A/B, p. 15].

# 11. Table-by-Table Interpretation

### Table 1 — Threat comparison

Compares training poisoning, retrieval poisoning, prompt manipulation, and web-content pollution across motivation, channel, attacker access, content, visible cues, and symptoms. It establishes FORGE’s distinct threat model: commercial promotion via plausible open-web reviews and an on-task targeted recommendation [A/B, p. 2].

### Table 2 — Main fooled-rate matrix

Rows are 15 categories; columns are 12 models; cells are percentages from \(n=15\) products. Bold marks the row minimum, underline the maximum, and color runs green-to-red. It is the central results table. Overall mean is 42.7%; model extremes are 13.3% and 73.8%; category extremes are 22.8% and 81.7% [A/B, p. 5].

### Table 3 — Dataset statistics

Every category has 15 products and 150 document slots. Distinct brand pools range 74–135, bundle diversity 6.80–9.47, and concentration 1.11–2.03 documents per brand. The total has 225 products, 2,250 slots, and 1,478 deduplicated brands. The caption warns that total-row bundle metrics are pooled, not simple column averages [A/B, p. 14].

### Table 4 — Difficult anchor cases

Shows errors where the LLM selects geography, a descriptor, a content marker, a model/sub-brand, or nothing. Downstream rules/human review recover final anchors. It demonstrates why Stage 1 alone is insufficient [A/B, p. 15].

### Table 5 — Qualitative recommendation outputs

Compares two fooled outputs and one resisted output for a screen-protector query. The fooled answers include fake Langyu and unsupported social proof; o4-mini omits it. Translated excerpts are abridged, while the adjacent Chinese outputs are described as unabridged [A/B, p. 16].

### Table 6 — Warning-marker disambiguation

All eight inspected high-confidence warning-marker hits are positive-in-context, not warnings against the fake brand. This supports interpreting `Rec=1` as recommendation rather than mere mention [A/B, p. 17].

### Table 7 — Top-1 severity

Reports overall fake-recommendation rate, fake-at-rank-1 rate, and conditional rank-1 share. Model-level rank-1 rates range 5%–53%; average is 24%. Conditional on recommending the fake, 40%–72% place it first; mean 55% [A/B, p. 17].

### Table 8 — Pollution dose

Supplies exact data for Figure 5. At ten replaced pages, all six models reach at least 44%, and four reach at least 80%. One non-monotone DeepSeek step is visible [A/B, p. 18].

### Table 9 — Rank-position effect

Supplies exact per-model rates for Figure 4. Rank 1 is usually largest. It also reveals exceptions obscured by pooled prose, including 13% and 11% at rank 3 for GLM and Ministral [A/B, p. 18].

### Table 10 — False-positive controls

Empty-evidence probes yield five false positives among 1,680 responses; clean bundles yield none among 275. All five no-evidence hits trace to previously flagged linguistic collisions [A/B, p. 20].

### Table 11 — Attack-style ablation

A3 is strongest for 11 models; grand averages are A1 38%, A2 25%, A3 78%. Claude Sonnet is the only A3 exception. Gemini 3.1 Pro and Claude Opus also have A2 above A1, showing heterogeneous model behavior [A/B, p. 20].

### Table 12 — English replication

Shows English, Chinese, and EN–CN differences for three matched categories. Category means preserve the low/mid/high order, but per-model shifts vary widely [A/B, p. 23].

### Table 13 — Defense efficacy and utility

Reports baseline, D1 fooled rate, and D2/D3 utility cost. D1 raises the mean from 43% to 53%; D2 and D3 average 68% and 63% legitimate-recommendation loss. D2 is limited to open-weights models, as marked by the dagger note [A/B, p. 24].

### Table 14 — D3 threshold trade-off

At \(\tau=3,4,5\), average utility costs are 49%, 63%, and 74%, while fake catch is 2%, 90%, and 91%. Moving from 4 to 5 gains only 1 pp catch while costing 11 additional points of utility [A/B; C difference, p. 24].

### Table 15 — D1 category breakdown

D1 worsens 14 of 15 category means. The largest mean increases are Phone/PC +32 pp, Bags/Shoes +19, Makeup +18, and Hospitality +16. Skincare improves by −11 pp because open-weights models improve by −28 pp despite closed-source worsening by +6 [A/B, p. 24].

### Table 16 — Reasoning ablation

Provides paired rates, discordant counts, and exact McNemar tests. Both models have significantly lower vulnerability with reasoning disabled [A/B, p. 25].

### Table 17 — Reasoning-trace split

The noticed-and-rejected group’s median trace is approximately six times those of the other groups, with large standardized differences against both [A/B, p. 26].

# 12. Diagram / Architecture Interpretation

Figures 1 and 12 collectively define the architecture.

The **data path** begins with a scenario-specific user query. Serper returns up to roughly 40 candidate URLs. After charset handling and six quality predicates, the first ten eligible pages become a frozen ordered bundle.

The **anchor path** processes each document through an LLM candidate generator, a regex/lexicon extractor, and a human verification gate. The final anchor is the real brand to be replaced.

The **attack path** modifies selected pages. The main attack replaces anchors in documents ranked 1–3 while preserving most document properties.

The **inference path** sends the same query and corresponding polluted bundle to each of 12 models under common decoding settings.

The **evaluation path** parses whether the fake brand or its prefix appears in the recommendation. Additional audits examine numbered-list placement, rank, warning markers, and false positives.

There is no feedback loop in the benchmark pipeline: model output does not alter subsequent search or content. The study is a frozen, one-shot evaluation rather than a live adaptive attacker–defender system [A/B, Figs. 1 and 12].

# 13. Equations and Mathematical Concepts

## Equation (1) — Retrieval

\[
E=S(q;W)=\{w_1,\ldots,w_K\}\subset W.
\]

- \(q\): user query.
- \(W\): open web.
- \(S\): search engine.
- \(w_i\): retrieved page at rank \(i\).
- \(E\): top-\(K\) evidence bundle.

Plainly: the search engine uses the query to choose \(K\) pages from the web [A, §2, p. 3; native text only].

## Equation (2) — Autoregressive recommendation generation

\[
p_\theta(y\mid x(r))
=\prod_{t=1}^{T_y}p_\theta(y_t\mid x(r),y_{<t}).
\]

- \(\theta\): model parameters.
- \(x(r)=[E;q]\): prompt formed from evidence and query.
- \(y=(y_1,\ldots,y_{T_y})\): generated recommendation.
- \(y_{<t}\): earlier generated tokens.

Plainly: the model writes the answer one token at a time, conditioned on the evidence, query, and text already written [A, p. 3; native text only].

## Equation (3) — Polluted retrieval

\[
\widetilde W=W\cup W_{\text{fake}},\qquad
\widetilde E=S(q;\widetilde W).
\]

- \(W_{\text{fake}}\): operator-authored polluted pages.
- \(\widetilde W\): web plus fake content.
- \(\widetilde E\): evidence retrieved from that polluted web.

Attack success occurs when the generated recommendation belongs to the fake-brand set \(B_{\text{fake}}\) [A, p. 3; native text only].

## Equation (4) — Recommendation indicator

\[
\operatorname{Rec}(t,r)=\mathbf 1[t\text{ appears in }r].
\]

- \(t\): fake-brand target.
- \(r\): response.
- \(\mathbf 1[\cdot]\): indicator equal to 1 if the condition is true and 0 otherwise.

The implementation accepts the full brand string or its prefix, case-insensitively. Averaging this binary value over cells gives the fooled rate [A/B, p. 4].

## Equation (5) — Cross-model agreement

\[
J(p)=
{\binom{|\mathcal M|}{2}}^{-1}
\sum_{\{m,m'\}\subset\mathcal M}
\frac{|B_{m,p}\cap B_{m',p}|}
{|B_{m,p}\cup B_{m',p}|}.
\]

- \(\mathcal M\): six open-weights models.
- \(B_{m,p}\): set of real brands recommended by model \(m\) for product \(p\) without evidence.
- The fraction is the Jaccard similarity between two models’ brand sets.
- The prefactor averages over every model pair—\(\binom{6}{2}=15\) pairs.

Plainly: \(J(p)\) is high when models independently name many of the same real brands and low when their brand lists differ [A/B, pp. 6–7].

## Other mathematical quantities

- **Fooled-rate percentage:** mean of binary `Rec` values.
- **\(D/b\):** average documents per brand, used as a concentration index [A, Table 3].
- **Cohen’s \(\kappa\):** reported inter-reviewer agreement beyond chance; the paper does not reproduce its formula.
- **McNemar exact test:** compares paired binary outcomes through discordant pairs \(b\) and \(c\) [A, Appendix N].
- **Reasoning share:** reasoning characters divided by reasoning plus output characters [A, Table 17].
- **Utility cost:** fraction of legitimate baseline recommendations removed by a defense [A, Appendix L].
- **Percentage points:** direct subtraction of percentages, such as 56.9%–38.7%=18.2 pp.

# 14. Interpretation and Discussion

The results answer the central research question affirmatively: retrieved web content can cause a broad set of LLMs to recommend fabricated products, even when the pollution is a simple entity substitution inside otherwise genuine documents [A, pp. 5, 9].

The most consequential mechanism is the interaction between **retrieval primacy** and **weak parametric brand priors**. A top-ranked page exerts much more influence than later pages, and categories with less cross-model brand agreement are more susceptible. This means that a model’s ability to reject pollution depends partly on whether it already possesses a stable alternative set of real brands [A, Figs. 4 and 8].

Reasoning is nuanced. The causal two-model ablation indicates that switching reasoning on increases vulnerability. Yet the observational trace analysis shows that when a model notices and successfully rejects the fake, it reasons much longer. The supported interpretation is not “reasoning is always harmful” or “more reasoning is always safe.” Instead, ordinary engagement can rationalize bad context, while sufficiently deep scrutiny may sometimes catch it [A, pp. 7, 25–26].

The attack-style results suggest that retained real-brand mentions provide some protection: A2, which inserts fake promotion while leaving genuine brands visible, is weaker on average than A1, and A3 removes that protection. However, density and document-length differences are confounded, which the authors acknowledge [A, pp. 20–21].

The defense failures reinforce the same mechanism. A skepticism prompt can force low-baseline models to pay attention to an unfamiliar planted brand, undermining the prior-based rejection they would otherwise perform. Filters are effective at removing the fake only because they are extremely conservative and also remove most legitimate recommendations [A, pp. 22–25].

## Consistency and cross-reference findings

- Table 2’s rounded overall mean is 42.7%; Tables 7 and 13 round this to 43%. This is consistent rounding, not a contradiction.
- Figure 3’s \(p<10^{-6}\) for Qwen is consistent with Appendix N’s exact \(2.8\times10^{-7}\).
- Main-text “1–4%” for ranks 2–10 is a pooled characterization; Table 9 contains isolated per-model values of 7%–13%. The scopes differ.
- Figure 11 labels D3 as 90% catch/37% survival, consistent with Table 13’s 63% mean utility cost.
- Stage-1 recall of 48.2% and override rate of 51.8% sum to 100%, consistent with the stated workflow.
- The abstract reports a maximum single-page fooled rate of 27% and full top-three rate of 73.8%, consistent with Tables 9 and 2.
- Appendix O says both B and C “see” the fake string because it occurs in their output, but its variable is named `fab_in_output`; calling this “working-context awareness” is an interpretation rather than a direct measurement of internal awareness.

# 15. Contributions and Novelty

## Conceptual contribution

The paper isolates **web-content pollution** as distinct from training poisoning, private-corpus poisoning, prompt injection, and ordinary adversarial SEO [A, Table 1].

## Benchmark contribution

FORGE provides a controlled framework covering 225 products, 15 categories, five scenarios, ten retrieved pages per product, and 12 LLMs [A, pp. 1–4].

## Methodological contribution

It uses local rewriting of real retrieved documents to preserve ranking and context without polluting the public web, plus a three-stage anchor-selection process and metric-validation audits [A, pp. 2–4, 13–20].

## Empirical contribution

It establishes model, category, rank, dose, attack-style, and language effects, including a paired reasoning ablation [A, §§4–6; Appendices J, K, N].

## Analytical contribution

It links vulnerability to cross-model brand disagreement, document brand-pool richness, shallow engagement, and invented social proof [A, §§5; Appendices E and O].

## Defense evaluation

It demonstrates distinct failure modes for prompt skepticism, model-prior filtering, and cross-document corroboration [A, §6; Appendices L–M].

## Artifact contribution

The authors state that they release the FORGE benchmark and evaluation harness. The external repository was not supplied or inspected [A, pp. 1, 9].

# 16. Limitations

## Authors' stated limitations

1. **Attack design is not optimized.** The tested styles may underestimate a motivated adversary using query-aware or domain-tailored content [A, p. 9].
2. **Secondary experiments have reduced scope.** D2, rank, dose, and reasoning-trace analyses use open-weights subsets or Digital Products only [A, p. 9].
3. **Language and region are limited.** The main study is Chinese; Local Life is Shenzhen-specific; English covers only three categories and one US city [A, pp. 9–10].
4. **Static snapshot.** Evidence was frozen in April 2026, so category rates may change with the web [A, p. 10].
5. **Anchor heuristic.** Rewrite targets depend on an LLM–rule–human pipeline with imperfect inter-reviewer agreement [A, pp. 10, 14–15].
6. **A2 density confound.** A2 retains genuine brands and also contains less fake-brand text, so their effects cannot be separated [A, p. 21].
7. **Closed-source trace generalization is untested.** Process-level reasoning findings rely on instrumentable open-weights models [A, pp. 9, 25].
8. **Full multilingual and multiregional evaluation remains future work** [A, p. 10].

## Additional evidence-based analyst observations

1. **Curated rather than probability-sampled product universe [D].** The 225 products are broad but do not support prevalence estimates for all consumer queries.
2. **Single deterministic completion [D].** \(T=0\) improves parity but does not characterize output variance across repeated or stochastic generation.
3. **Search-stage realism is only partially represented [D].** A1 edits pages after retrieval, so it measures model consumption conditional on polluted evidence appearing, not an attacker’s probability of achieving search visibility.
4. **Provider/runtime drift [D].** Preview/API model behavior may change, and only model identifiers—not immutable weights or server versions—are reported.
5. **Defense utility is narrow [D].** Utility cost counts removed real-brand recommendations, not user satisfaction, factual quality, diversity, or downstream harm.
6. **Social-proof measurement is incompletely exposed [D].** The headline 1.5–11× result lacks a full table of counts, uncertainty, or validation of the 14-phrase lexicon.
7. **“Awareness” is indirectly operationalized [D].** Fake-string occurrence in output or a trace does not necessarily establish a psychologically meaningful internal awareness state.
8. **Human anchor verification remains moderately variable [D].** The overall \(\kappa\) is substantial, but 24.3% of pilot cases select a different brand; category-level sensitivity reduces, but does not eliminate, concern about instance-level variation.

# 17. Threats to Validity

## Internal validity

Strengths include frozen bundles, paired inputs, fixed decoding, hashed input triples, and the within-model reasoning ablation. Threats include anchor-selection variability, A2/A3 multi-factor confounding, and reliance on heuristic output parsing.

## Construct validity

The paper carefully validates `Rec` through clean/no-evidence controls, structural list placement, and warning-marker review. Nevertheless, substring appearance is an imperfect proxy for persuasion, consumer exposure, or actual purchasing harm.

The “brand knowledge” construct is measured through cross-model agreement and probe alignment rather than ground-truth knowledge. It is a useful operational measure but could reflect shared popularity biases.

## Statistical conclusion validity

The principal category effect is strongly significant, and paired reasoning effects use exact tests. However, some regressions and mediation analyses operate on small model–category panels, increasing sensitivity to model specification. Multiple testing correction is not reported.

## External validity

Coverage spans 12 models and 15 categories, and English replication strengthens linguistic generalization. External validity remains limited by one Chinese snapshot, Shenzhen-focused Local Life, three English categories, selected models, and conditional rather than live SEO exposure.

## Ecological validity

Real pages and commercial search results strengthen realism. Local post-retrieval rewriting improves ethical control but does not recreate the complete ecology of publishing, indexing, ranking, user interaction, or adaptive attackers.

## Reproducibility

Prompts, retrieval logic, model identifiers, decoding parameters, and exact tables are well documented. Reproducibility is constrained by changing web results, proprietary model endpoints, the private polluted documents, an unsupplied review interface, and the uninspected external repository.

# 18. Future Work and Open Questions

## A. Future work proposed by the authors

- Full multilingual and multiregional evaluation [A, pp. 9–10].
- Closed-source generalization of process-level reasoning signatures [A, p. 9].
- Controlled-density A2 experiments that preserve real brands while matching A3’s surface-text length [A, p. 21].
- Retrieval-time defenses using source credibility, evidence diversification, cross-document corroboration, and noise-robust grounding [A, pp. 8–9, 23].
- Improved pollution-resilient recommenders using the released benchmark [A, p. 9].

## B. Additional open questions

- How often can fake pages obtain high search rank under real search-engine conditions?
- Do results persist under repeated decoding, personalized queries, conversational follow-ups, or agentic purchasing workflows?
- Can source provenance and domain-reputation signals help without excluding legitimate long-tail vendors?
- Can a model distinguish independent corroboration from coordinated clusters of mutually copied pages?
- Would calibrated uncertainty or abstention work better than binary filtering?
- How stable are the results across time and model updates?
- Can social-proof fabrication be detected semantically rather than through a phrase lexicon?
- What intervention produces the long, protective “noticed and rejected” deliberation without generally increasing engagement with pollution?

These are analyst-identified open questions, not author-reported results.

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| LLM | Large language model; a model that generates text token by token |
| Search-augmented LLM | An LLM given live search results before answering |
| Generative recommender | A text-generating system that recommends products or services |
| FORGE | Fake Online Recommendations in Generative Environments |
| GEO | Generative Engine Optimization; shaping web content to influence generative search output |
| Web-content pollution | Misleading open-web content intended to influence retrieved-evidence recommendations |
| RAG | Retrieval-augmented generation; generation conditioned on retrieved documents |
| Evidence bundle \(E\) | Ordered set of documents supplied to the model |
| Anchor | Real brand selected for replacement in a document |
| Fake-brand target \(t\) | Invented brand or brand–product compound inserted into polluted pages |
| A1 | Entity replacement |
| A2 | Promotional passage injection |
| A3 | Full synthetic document replacement |
| D1 | Skepticism-prompt defense |
| D2 | Model-prior consensus filter |
| D3 | Cross-document evidence-agreement filter |
| `Rec(t,r)` | Binary indicator that fake target \(t\) appears as a recommendation in response \(r\) |
| Fooled rate | Percentage of responses recommending the fake brand |
| Top1 | Fake brand appears as the first recommendation |
| Parametric prior | Product/brand knowledge encoded in model parameters |
| Open-weights | Model whose weight files are made available under some access terms |
| Closed-source | Model accessed without its underlying weights |
| Greedy decoding | Always selecting the highest-scoring next token; here \(T=0\) |
| SERP | Search engine results page |
| CJK | Chinese, Japanese, and Korean character family |
| \(K\) | Number of retrieved pages; here 10 |
| \(N\) | Number of polluted pages in the dose study |
| \(J(p)\) | Mean pairwise Jaccard agreement among models’ brand sets |
| Jaccard similarity | Intersection size divided by union size |
| \(D/b\) | Average documents per brand, used as a concentration index |
| \(\tau\) | Minimum cross-document count required by D3 |
| Percentage point (pp) | Direct difference between two percentages |
| Wilson CI/UB | Binomial confidence interval/upper bound |
| Cohen’s \(\kappa\) | Chance-adjusted agreement between reviewers |
| Cohen’s \(d\) | Standardized difference between groups |
| McNemar test | Paired test for changes in binary outcomes |
| AUC | Area under the receiver-operating-characteristic curve |
| \(R^2\) | Proportion of outcome variance accounted for by a regression |
| Confabulation | Generated claims not supported by the supplied evidence |
| Social proof | Claims that a product is popular, widely discussed, or endorsed |
| Primacy effect | Disproportionate influence of early retrieved documents |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Main products | 225 | products | 15 categories × 15 | Author-reported | p. 3 |
| Retrieved evidence | 2,250 | document slots | 10 per product | Author-reported | Table 3, p. 14 |
| Models | 12 | models | 6 closed, 6 open-weights | Author-reported | §4.1, p. 4 |
| Overall main fooled rate | 42.7 | % | Top-3 A1 | Author-reported | Table 2, p. 5 |
| Model range | 13.3–73.8 | % | Top-3 A1 | Author-reported | Table 2, p. 5 |
| Category range | 22.8–81.7 | % | Phone/PC to Dining | Author-reported | Table 2, p. 5 |
| Category test | \(\chi^2(14)=99.4\) | statistic | Friedman test | Author-reported | §4.2, p. 4 |
| Category-test significance | \(p<10^{-14}\) | p-value | Main categories | Author-reported | §4.2, p. 4 |
| Rank-1 single-page maximum | 27 | % | GLM/Ministral, Digital Products | Author-reported | Table 9, p. 18 |
| Ten-page range | 44–100 | % | Six open-weights | Author-reported | Table 8, p. 18 |
| Qwen reasoning effect | −18.2 | pp | OFF minus ON | Author-reported | Table 16, p. 25 |
| GLM reasoning effect | −8.9 | pp | OFF minus ON | Author-reported | Table 16, p. 25 |
| Brand agreement relation | \(r=-0.65\) | Pearson correlation | 15 categories | Author-reported | Fig. 8, p. 7 |
| Correlation significance | \(p<0.01\) | p-value | Agreement vs fooled rate | Author-reported | p. 7 |
| Noticed/rejected median trace | 7,983 | characters | Group B | Author-reported | Table 17, p. 26 |
| Unaware resisted median trace | 1,312 | characters | Group A | Author-reported | Table 17, p. 26 |
| Fooled median trace | 1,360 | characters | Group C | Author-reported | Table 17, p. 26 |
| Social-proof increase | 1.5–11× | ratio | Fooled vs resisted | Author-reported | §5, p. 7 |
| A1/A2/A3 means | 38/25/78 | % | Matched five-product subset | Author-reported | Table 11, p. 20 |
| A3–A1 gap | 40 | pp | \(78-38\) | Analyst-derived; also stated in prose | pp. 20–21 |
| English category means | 43/58/87 | % | Smartphone/skincare/restaurants | Author-reported | Table 12, p. 23 |
| Chinese matched means | 23/57/82 | % | Matched categories | Author-reported | Table 12, p. 23 |
| D1 overall change | +10.5 | pp | Skepticism minus baseline | Author-reported | Table 15, p. 24 |
| Closed-source D1 change | +24 | pp | Six-model average | Author-reported | Table 15, p. 24 |
| Open-weights D1 change | −3 | pp | Six-model average | Author-reported | Table 15, p. 24 |
| D2 fake catch | 95 | % | Six open-weights | Author-reported | Fig. 11, p. 8 |
| D2 utility cost | 68 | % | Mean legitimate removal | Author-reported | Table 13, p. 24 |
| D3 fake catch | 89.9–90 | % | \(\tau=4\) | Author-reported | Tables 13–14, p. 24 |
| D3 utility cost | 63 | % | \(\tau=4\) mean | Author-reported | Table 14, p. 24 |
| Empty-evidence FP | 5/1,680 = 0.30 | % | All 12 models | Author-reported | Table 10, p. 20 |
| Empty-evidence FP upper bound | 0.69 | % | Wilson 95% | Author-reported | p. 19 |
| Clean-bundle FP | 0/275 = 0.00 | % | All 12 models | Author-reported | Table 10, p. 20 |
| Positive cells in-list | 1,143/1,154 = 99.0 | % | Endorsement audit | Author-reported | p. 16 |
| Anchor Stage 1 recall | 48.2 | % | LLM extractor | Author-reported | Fig. 13, p. 14 |
| Stage 2 cumulative recall | 72.9 | % | LLM + rules | Author-reported | Fig. 13, p. 14 |
| Human-verified coverage | 100 | % | All 2,250 slots | Author-reported | Fig. 13, p. 14 |
| Reviewer agreement | 75.3 | % | 226/300 | Author-reported | pp. 14–15 |
| Cohen’s \(\kappa\) | 0.752 | coefficient | 95% CI [0.704, 0.802] | Author-reported | p. 15 |
| Anchor-free leave-one-out \(R^2\) | 0.672 | proportion | Five open-weights × 15 categories | Author-reported | p. 18 |
| Expanded leave-one-out \(R^2\) | 0.727 | proportion | Four-model feature panel | Author-reported | p. 18 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| All tested models are vulnerable | Every model has 13.3%–73.8% fooled rate | X1; Fig. 2; Table 2 | pp. 4–5 | Strong within tested models/products |
| One top-ranked polluted page can suffice | Rank-1 rates reach 27%; later pooled rates are much lower | X3; Fig. 4; Table 9 | pp. 5, 18 | Strong for six open-weights models and Digital Products |
| More polluted pages increase risk | Near-monotone curves; ten-page rates 44%–100% | X4; Fig. 5; Table 8 | pp. 6, 18 | Strong subset evidence; one local non-monotonicity |
| Category matters | 22.8%–81.7%; Friedman \(p<10^{-14}\) | X1; Table 2 | pp. 4–5 | Strong tested-category evidence |
| Stable brand priors protect | Agreement \(r=-0.65\); alignment correlations negative | X7–X8; Fig. 8 | pp. 6–7, 17–18 | Correlational, supported by several measures |
| Reasoning can increase vulnerability | Matched ON/OFF decreases of 18.2 and 8.9 pp when disabled | X2; Fig. 3; Table 16 | pp. 5, 25 | Causal within two toggleable models |
| Deep scrutiny is associated with resistance | Group B median 7,983 vs 1,312/1,360 | X9; Fig. 9; Table 17 | pp. 7, 26 | Observational association |
| Fooled models invent social proof | Qualitative unsupported phrases; 1.5–11× marker rate | X10; Table 5 | pp. 7, 16 | Qualitative evidence strong; population audit incompletely tabulated |
| Full synthesis is strongest tested style | A3 average 78%; strongest in 11/12 models | X5; Fig. 6; Table 11 | pp. 6, 20 | Strong comparison, but multi-factor confounding |
| Findings generalize linguistically in category order | EN 43<58<87 and CN 23<57<82 | X6; Fig. 7; Table 12 | pp. 6, 21–23 | Supports three-category English transfer only |
| Skepticism prompting is not a reliable defense | Mean +10.5 pp; closed-source +24 pp | X12; Fig. 10; Tables 13/15 | pp. 7–8, 22–24 | Strong across tested panel |
| Consensus filters sacrifice utility | D2 68%, D3 63% mean real-brand loss | X13–X14; Fig. 11; Tables 13–14 | pp. 8, 24 | Strong under paper’s utility definition |
| `Rec` mostly captures endorsement | 99% in list; negligible genuine warning cases | X11; Tables 6/10 | pp. 16–20 | Strong audit, subject to heuristic parsing |

# 22. Very Simple Explanation

Imagine asking an AI, “What are the five best phone cases?” The AI searches the web, reads several pages, and writes an answer. The paper asks what happens if some of the pages look normal but have a real brand’s name replaced with a made-up one.

The researchers tested this without putting fake pages on the public internet. They downloaded real search results, changed selected brand names locally, and gave those pages to 12 AI models. Every model sometimes recommended the fake brand. The first search result mattered especially strongly, and adding more polluted pages made the problem much worse.

Models were safer when they already had stable knowledge of the real brands in a category. They were more easily fooled in areas such as restaurants and personal services, where there is no short, universally agreed list of famous brands. Worse, a fooled model sometimes invented extra reasons why the fake brand was popular or trusted, even though those reasons were not in the supplied pages.

Simple fixes did not work well. Telling the AI to be skeptical sometimes made it more vulnerable, apparently because the instruction made it pay more attention to the fake name. Strict filters removed most fake brands, but also removed most genuine recommendations. The paper’s main lesson is that search-assisted AI needs stronger safeguards around which web sources it trusts and how it checks evidence across sources.

# Completeness Audit

## Inventory and coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors | Yes | Yes | Fully represented | Title and authors from p. 1 |
| Abstract | Yes | Yes | Fully represented | Incorporated in orientation/results |
| §1 Introduction | Yes | Yes | Fully represented | Problem, gap, novelty, findings |
| §2 Background | Yes, text only on p. 3 | Yes | Fully represented | Equations (1)–(3) not visually inspected |
| §3 FORGE Benchmark | Yes | Yes | Fully represented | Construction, attacks, metric |
| §3.1 Construction | Yes | Yes | Fully represented | Products, prompts, bundles |
| §3.2 Pollution simulation | Yes | Yes | Fully represented | A1–A3 |
| §3.3 Evaluation metric | Yes | Yes | Fully represented | Eq. (4) and audits |
| §4 Experiment/settings/results | Yes | Yes | Fully represented | Main and five targeted studies |
| §5 Analysis | Yes | Yes | Fully represented | Agreement, reasoning, social proof |
| §6 Defenses | Yes | Yes | Fully represented | D1–D3 |
| §7 Related Work | Yes | Yes | Represented in compressed form | All five substantive literature groupings covered; individual citations compressed |
| §8 Conclusion | Yes | Yes | Fully represented | Findings and implications |
| Limitations | Yes | Yes | Fully represented | All four author limitation blocks covered |
| Ethical Considerations | Yes | Yes | Represented in compressed form | Local simulation, dual-use rationale, private polluted docs, no provider compensation |
| References, pp. 10–12 | Yes, text only | Partly | Inspected but deliberately compressed | Bibliography not repeated citation by citation |
| Appendix A | Yes | Yes | Fully represented | Catalog, prompts, retrieval, anchors, reviewer reliability |
| Appendix B | Yes | Yes | Fully represented | Qualitative case study |
| Appendix C | Yes | Yes | Fully represented | Endorsement audit |
| Appendix D | Yes | Yes | Fully represented | Top-1 severity |
| Appendix E | Yes | Yes | Fully represented | Probes and predictors |
| Appendix F | Yes | Yes | Fully represented | Dose-response exact values |
| Appendix G | Yes | Yes | Fully represented | Single-rank results |
| Appendix H | Yes | Yes | Fully represented | Decoding and model identifiers |
| Appendix I | Yes | Yes | Fully represented | Three-layer false-positive control |
| Appendix J | Yes | Yes | Fully represented | Attack-style ablation |
| Appendix K | Yes | Yes | Fully represented | English replication |
| Appendix L | Yes | Yes | Fully represented | Defense details |
| Appendix M | Yes | Yes | Fully represented | D1 category breakdown |
| Appendix N | Yes | Yes | Fully represented | Reasoning-off paired ablation |
| Appendix O | Yes | Yes | Fully represented | Three-way trace analysis |
| Explicit RQ | Yes | Yes | Fully represented | Abstract question |
| Formal hypotheses | Yes | Yes | Fully represented | None stated |
| X1 main cross-section | Yes | Yes | Fully represented | Fig. 2/Table 2 |
| X2 reasoning toggle | Yes | Yes | Fully represented | Fig. 3/Table 16 |
| X3 rank position | Yes | Yes | Fully represented | Fig. 4/Table 9 |
| X4 pollution count | Yes | Yes | Fully represented | Fig. 5/Table 8 |
| X5 attack style | Yes | Yes | Fully represented | Fig. 6/Table 11 |
| X6 English replication | Yes | Yes | Fully represented | Fig. 7/Table 12 |
| X7–X8 predictor analyses | Yes | Yes | Fully represented | Eq. (5), regression, mediation |
| X9 reasoning split | Yes | Yes | Fully represented | Fig. 9/Table 17 |
| X10 social proof | Yes | Yes | Represented with disclosed limitation | Full count table absent from paper pages |
| X11 metric audits | Yes | Yes | Fully represented | Appendices C/I |
| X12–X14 defenses | Yes | Yes | Fully represented | D1–D3 |
| Figures 1–14 | Yes, visually | Yes | Fully represented | Every substantive figure addressed individually |
| Tables 1–17 | Yes, visually | Yes | Fully represented | Every substantive table addressed individually |
| Equations (1)–(3) | Yes, native text | Yes | Represented with access caveat | Page 3 not rendered |
| Equations (4)–(5) | Yes, visually/textually | Yes | Fully represented | Symbols and purposes explained |
| Algorithms/pseudocode | Yes | Yes | Fully represented | No formal algorithm block; pipeline described procedurally |
| Theorems/lemmas/proofs | Yes | Yes | Fully represented | None present |
| Footnotes/endnotes | Yes | Yes | Fully represented | No substantive standalone footnote identified |
| Benchmark artifact | No | Yes as absent artifact | Missing from supplied material | GitHub/repository not inspected |
| Simulated polluted documents | No | Yes as absent artifact | Missing/private | Authors say they are kept private |
| Review interface | No | Yes as absent artifact | Missing from supplied material | Workflow described only |
| Supplementary files | Not applicable | Yes | No separate material supplied | None detected |

## Missing or inaccessible material

- No page is missing from the 26-page document.
- Pages 3 and 10–12 were not visually rendered. Their native text was supplied and readable.
- The external FORGE repository and evaluation harness were not supplied.
- The locally generated polluted documents are not supplied; the authors state that they are private.
- The anchor-review interface, raw search responses, raw model outputs beyond selected examples, reasoning traces, and per-trial data are not supplied.
- The full per-model social-proof marker counts and full Appendix J breakdown mentioned in prose are not separately printed beyond the supplied aggregate tables/figures.
- No independent supplementary file was provided.

## Uncertain interpretations

- Equations (1)–(3) were reconstructed from native extracted text, not visually cross-checked; tilde and product notation are potentially extraction-sensitive.
- Figure 4’s exact pooled values are not labeled. Only its shape, prose range, and Table 9’s per-model values can be stated confidently.
- Figure 6 visually shows three aggregate categories, but exact bar heights are not labeled; Table 11 gives per-model, not those precise category aggregates.
- The reasoning-trace variable is treated by the authors as evidence of noticing/working-context awareness. The directly measured fact is string occurrence and trace/output length; stronger cognitive language remains interpretive.
- The “1.5–11× social-proof” result is author-reported, but the underlying complete count table and uncertainty estimates are absent.

## Deliberately compressed material

- The bibliography was inspected from native text but not reproduced citation by citation. Its substantive research categories and the authors’ positioning are represented.
- Repetitive restatements of headline results across the abstract, introduction, conclusion, captions, and appendices were consolidated.
- Exact Chinese prompt and output strings were not fully recopied; their authors’ English translations, methodological roles, and evidentiary significance are represented.
- Every cell of Tables 2, 3, 8–16 was inspected, but only decision-relevant extremes, means, exceptions, and exact headline values were repeated. The full matrices remain accounted for through table-specific interpretations.

## Potential omissions

No known substantive section, appendix, figure, table, major equation, explicit research question, distinct reported experiment, major contribution, or author-stated limitation from the supplied 26-page inventory is absent from this analysis. Raw artifacts referenced by the paper but not supplied could not be assessed, and several large tables were deliberately compressed rather than transcribed cell by cell.