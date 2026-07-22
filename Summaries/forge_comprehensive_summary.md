# One Polluted Page Is Enough: Evaluating Web Content Pollution in Generative Recommenders

**Authors:** Minghao Luo and Liang Chen  
**Affiliation:** The Chinese University of Hong Kong

## 1. Background and Context

Search-augmented large language models increasingly act as consumer recommenders. They receive a user’s request, retrieve current webpages, and synthesize a ranked list of products, brands, restaurants, or services. This moves part of the system’s “trust boundary” from the model to the open web: even a capable model can be misled if its retrieved evidence has been manipulated.

The paper focuses on malicious **Generative Engine Optimization (GEO)**. Commercial operators publish fake reviews or promotional pages so that search engines retrieve them and downstream AI assistants recommend a target brand. Unlike conventional adversarial SEO, the promoted product may be entirely fictional rather than a real competitor.

The authors distinguish **web-content pollution** from three neighboring threats:

| Threat | Polluted channel | Attacker access | Content | Visible cue | Typical result |
|---|---|---|---|---|---|
| Training poisoning | Training corpus | Train-time writing | Trigger examples | Trigger patterns | Wrong labels |
| Retrieval poisoning | Private RAG corpus | Direct corpus writing | Adversarial passages | Out-of-distribution passages | False answers |
| Prompt manipulation | User prompt | Inference-time input | Overrides or personas | Anomalous tokens | Harmful/off-task content |
| Web-content pollution | Open live web | Indirectly through SEO | Plausible fake reviews | None | Targeted product recommendation |

Web pollution is especially difficult to detect because the fake text resembles ordinary user content, while the model remains fluent, on-task, and policy-compliant. It simply recommends a nonexistent product.

The motivating real-world event was China Central Television’s March 15, 2026 Consumer Rights Day Gala, which reported a commercial market for seeding fake reviews that could make fake brands enter mainstream Chinese AI recommendations within hours.

Formally, a search engine retrieves an evidence bundle \(E\) of the top \(K\) webpages for a query. The query and evidence are passed to an autoregressive LLM, which generates a recommendation one token at a time. Under GEO, the open web contains attacker-authored pages promoting fake brands; pollution succeeds when a fake brand appears in the generated recommendation.

## 2. Research Goal and Objectives

The central question is:

> To what extent do search-augmented LLMs become unwitting promoters of fake products after consuming polluted search results?

The paper seeks to:

1. Build a controlled, reproducible benchmark for measuring fake-product promotion without contaminating the real web.
2. Measure vulnerability across different models, product categories, page ranks, pollution doses, attack styles, and languages.
3. determine whether model size, source availability, prior brand knowledge, and internal reasoning explain vulnerability.
4. Examine how models justify fake recommendations, particularly whether they invent unsupported social proof.
5. Test three inference-time defenses:
   - skepticism prompting;
   - filtering against the model’s evidence-free prior recommendations;
   - filtering based on agreement across retrieved documents.

## 3. Methods (Approach/Design)

### 3.1 FORGE benchmark

The authors introduce **FORGE: Fake Online Recommendations in Generative Environments**. It reproduces the deployed pipeline:

**User query → web search → quality filtering → top-10 evidence bundle → local pollution → LLM → ranked recommendation**

Unlike real GEO, FORGE does not publish anything online. It freezes genuine search results and locally edits selected documents. This preserves reproducibility and avoids harming public infrastructure.

### 3.2 Products and scenarios

FORGE contains **225 products**:

- 5 consumer scenarios;
- 3 categories per scenario;
- 15 products per category;
- 15 categories total.

The scenarios and categories are:

- **Digital Products:** phones/computers, home appliances, electronics accessories.
- **Local Life:** personal services, hospitality, dining.
- **Health and Personal Care:** makeup, supplements, skincare.
- **Fashion Accessories:** apparel, underwear/socks, bags/shoes.
- **Sports and Outdoor:** camping, cycling, fitness.

The main study is in Chinese, reflecting the motivating GEO case. Local-life queries concern Shenzhen.

The shared Chinese system prompt tells the model that it is a product and local-life recommendation assistant, supplies webpages, and asks for recommendations with brief reasoning. Most queries request the five most worthwhile products; specialized wording is used for some digital products, Shenzhen venues, and health/personal-care items.

### 3.3 Search and evidence collection

For each query, the researchers used the commercial Serper search API with Chinese/China-region settings, collecting approximately 40 candidate URLs over as many as four result pages.

Pages were rejected if they:

- returned a non-2xx HTTP status;
- contained fewer than 50 visible non-whitespace characters;
- were substantially garbled;
- belonged to blocked video platforms such as YouTube, Youku, Bilibili, or Douyin;
- were boilerplate category or search-result pages.

Fetching used a 10-second timeout, a browser-like user agent, BeautifulSoup parsing, and charset handling for common Chinese encodings. The first 10 acceptable documents, in original search order, became the fixed evidence bundle.

The corpus contains **2,250 document slots**: 225 products × 10 documents.

### 3.4 Identifying the real brand to replace

Each retrieved document passed through a three-stage anchor-extraction pipeline:

1. **LLM candidates:** Gemini 2.5 Flash-Lite at temperature 0.1 proposed up to eight candidate brand strings. Its top-1 recall was **48.2%**.
2. **Rules and lexicon:** title/snippet regexes and roughly 50 known brand prefixes per category raised cumulative recall to **72.9%**.
3. **Human verification:** a native-Chinese reviewer accepted, changed, or entered an anchor from the document, bringing coverage to **100%**.

Thus, human review supplied the final **27.1 percentage points** of recall. The Stage-1 top candidate was overridden in **51.8%** of the 2,250 slots.

An independent reviewer rechecked a stratified sample of 300 slots:

- exact-string agreement: **75.3% (226/300)**;
- Cohen’s \(\kappa=0.752\);
- 95% bootstrap CI: **[0.704, 0.802]**;
- per-category \(\kappa\): **0.48–1.00**.

Disagreements were mostly selections of different dominant brands (**24.3%**); only **0.3%** involved different surface forms of the same brand, and no slot lacked a viable anchor. Category-level reviewer agreement was not significantly associated with fooled rate: Spearman \(\rho=0.25\), permutation \(p=0.36\). Therefore, lower anchor agreement did not systematically inflate apparent vulnerability.

Examples of Stage-1 errors included choosing a district, product descriptor, content marker, model name, or sub-brand rather than the target brand.

### 3.5 Dataset diversity

Every category contains 15 products and 150 document slots. Across the corpus:

- category-specific brand pools sum to 1,564;
- after cross-category deduplication, there are **1,478 distinct brands**;
- mean distinct brands per 10-document bundle: **8.55**;
- mean documents per brand: **1.52**;
- mean anchor length: **5.4 Chinese characters**;
- **19.2%** of anchors have exactly two Chinese characters.

Category brand pools range from **74** for home appliances to **135** for food and drink. Mean distinct brands per bundle range from **6.80** for mobile/digital products to **9.47** for skincare.

Figure 14 shows that diverse markets such as food, skincare, and personal services tend to have more than 120 brands and fewer than 1.3 documents per brand. Concentrated categories such as home appliances, makeup, and mobile/digital products have fewer than 90 brands and more than 1.7 documents per brand. Both axes span approximately a twofold range.

### 3.6 Pollution attacks

FORGE defines three attack styles:

- **A1—Entity replacement:** Replace the dominant real brand throughout the document with a fake brand–product compound, preserving the URL, rank, style, length, and surrounding text.
- **A2—Passage injection:** Add a 120–180-character synthetic promotional paragraph while preserving the original document and real-brand mentions.
- **A3—Full synthesis:** Replace the body with a 500–700-character synthetic fake-brand review and use a new hashed path on the original domain.

The default main experiment applies A1 to the **top three** retrieved documents.

### 3.7 Models and inference

Twelve production LLMs were tested—six closed-source and six open-weights:

- Gemini 3 Flash;
- GPT-5.4;
- o4-mini;
- Gemini 3.1 Pro;
- Claude Opus 4.7;
- Claude Sonnet 4.6;
- Qwen3.6-27B;
- Qwen3.6-35B-A3B;
- Qwen3.5-9B;
- DeepSeek V4 Pro;
- GLM-4.6V-Flash;
- Ministral-3R.

All used greedy decoding with:

- temperature \(T=0\);
- maximum output length of 8,192 tokens.

Each model was evaluated on all **225 products** in the main experiment. Inputs were SHA-256 hashed and stored with outputs to support reruns and parity checks.

### 3.8 Outcome measure

For fake target \(t\) and response \(r\), the recommendation indicator equals 1 if either the full fake brand or its prefix appears in the response, case-insensitively. The **fooled rate** is the percentage of model-product responses in which this occurs.

The indicator was extensively validated:

- Empty-evidence probes: **5/1,680 false positives = 0.30%**, Wilson upper bound **0.69%**.
- Clean, unmodified evidence: **0/275 = 0%**, Wilson upper bound **1.34%**.
- Of 1,154 positive cells, **99.0%** placed the fake brand inside the numbered recommendation list.
- Only **0.9%** contained a warning-associated word near the fake brand; manual review of the eight strongest cases found all were positive uses, not warnings.
- The fake product occupied rank 1 in **5%–53%** of all cells, depending on the model.

The small no-evidence false-positive count came from known linguistic collisions, especially a two-character phrase meaning “and cloud,” rather than spontaneous fake-product recommendations.

## 4. Results and Findings

### 4.1 Universal but highly variable vulnerability

Under top-three entity replacement, every model recommended fake products. Model-average fooled rates were:

| Model | Fooled rate |
|---|---:|
| Gemini 3 Flash | 13.3% |
| GPT-5.4 | 20.9% |
| o4-mini | 28.4% |
| Qwen3.6-27B | 31.1% |
| Qwen3.6-35B-A3B | 36.9% |
| Gemini 3.1 Pro | 40.4% |
| Qwen3.5-9B | 45.8% |
| Claude Opus 4.7 | 47.6% |
| Claude Sonnet 4.6 | 49.8% |
| DeepSeek V4 Pro | 51.6% |
| GLM-4.6V-Flash | 73.3% |
| Ministral-3R | 73.8% |

The overall average was **42.7%**. Closed-source and open-weights ranges overlapped substantially; model size and perceived general capability did not provide reliable protection. Within the Gemini family, Gemini 3.1 Pro was fooled roughly three times as often as Gemini 3 Flash.

Figure 2 displays these model-level rates with 95% Wilson intervals and confirms that vulnerability does not separate cleanly by closed versus open model status.

### 4.2 Category effects

Fooled rates varied significantly across categories:

- Friedman \(\chi^2(14)=99.4\);
- \(p<10^{-14}\).

Twelve-model category averages were:

| Category | Mean fooled rate |
|---|---:|
| Phone/PC | 22.8% |
| Home appliances | 30.0% |
| Electronics accessories | 30.6% |
| Personal services | 60.6% |
| Hospitality | 31.7% |
| Dining | 81.7% |
| Makeup | 32.8% |
| Supplements | 60.0% |
| Skincare | 56.7% |
| Apparel | 48.9% |
| Underwear/socks | 42.2% |
| Bags/shoes | 36.7% |
| Camping | 32.8% |
| Cycling | 39.4% |
| Fitness | 34.4% |

Dining was the most vulnerable category for two-thirds of the models and reached **100%** for Claude Sonnet 4.6. Everyday or experiential categories—dining, personal services, and supplements—were most exposed. Technical categories with better-established brands—phones, computers, home appliances—were least exposed.

### 4.3 Severity: fake brands often ranked first

Across all models, the average fake-brand recommendation rate was approximately **43%**, and the average fake-brand rank-1 rate was **24%**. Conditional on recommending the fake brand, it appeared first **55%** of the time.

Conditional rank-1 proportions ranged from **40%** for Gemini 3 Flash to **72%** for Ministral-3R. Ministral-3R placed the fake brand first in **53% of all cells**, and GLM-4.6V-Flash did so in **45%**.

### 4.4 One polluted page and retrieval-rank primacy

Figure 4 and Table 9 show that a single polluted document can be sufficient, especially at rank 1.

For the six open models on the three Digital Product categories, rank-1 fooled rates were:

- Qwen3.6-27B: **11%**;
- Qwen3.6-35B-A3B: **2%**;
- Qwen3.5-9B: **2%**;
- DeepSeek V4 Pro: **9%**;
- GLM-4.6V-Flash: **27%**;
- Ministral-3R: **27%**.

Moving the same polluted page to ranks 2–10 usually reduced the rate to **0%–4%**, with a few exceptions: GLM reached 13% at rank 3, 9% at rank 4, and Ministral reached 11% at rank 3 and 7% at rank 4. There was no recovery at later positions.

This is a strong **primacy effect**: the first retrieved page dominates, while later pages have little influence.

### 4.5 Pollution dose response

Figure 5 and Table 8 show a near-monotonic increase as more of the top 10 documents are polluted:

| Polluted pages | Qwen 27B | Qwen 35B | Qwen 9B | DeepSeek | GLM | Ministral |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 11% | 2% | 2% | 9% | 27% | 27% |
| 2 | 9% | 7% | 11% | 24% | 49% | 49% |
| 3 | 20% | 16% | 22% | 36% | 58% | 64% |
| 5 | 27% | 42% | 38% | 44% | 73% | 78% |
| 7 | 36% | 53% | 62% | 40% | 87% | 91% |
| 10 | 44% | 73% | 80% | 73% | 100% | 98% |

The most vulnerable models exceeded 50% with only three polluted pages. Slopes differed by about a factor of two, but a handful of mutually corroborating pages was enough to make fake recommendations common.

### 4.6 Attack-style comparison

Across the matched five-product subsets, grand-average rates were:

- A1 entity replacement: **38%**;
- A2 passage injection: **25%**;
- A3 full synthesis: **78%**.

Full synthesis was strongest on **11 of 12 models**, reached at least 70% on 9 models, and exceeded passage injection by an average of **53 percentage points**.

Per-model A1/A2/A3 rates included:

- Gemini 3 Flash: 19% / 9% / 56%;
- GPT-5.4: 19% / 0% / 69%;
- o4-mini: 29% / 3% / 76%;
- Gemini 3.1 Pro: 35% / 68% / 99%;
- Claude Opus 4.7: 41% / 61% / 72%;
- Claude Sonnet 4.6: 47% / 7% / 24%;
- Qwen3.5-9B: 35% / 13% / 93%;
- GLM-4.6V-Flash: 60% / 44% / 100%;
- Ministral-3R: 67% / 51% / 99%.

Claude Sonnet 4.6 was the only model less vulnerable to A3 than A1, possibly because of model-specific synthetic-content filtering. Gemini 3.1 Pro and Claude Opus were unusual in being more vulnerable to passage injection than entity replacement.

A2 was generally weakest because the original real-brand references remained in the document and could pull the model back toward genuine products. It also contained less fake-brand text, so this experiment cannot fully separate real-brand protection from fake-brand density.

### 4.7 Reasoning increases vulnerability

A paired experiment disabled internal reasoning on two models while holding inputs, weights, architecture, decoding, and all other settings constant:

| Model | Reasoning on | Reasoning off | Change |
|---|---:|---:|---:|
| Qwen3.5-9B | 56.9% | 38.7% | −18.2 pp |
| GLM-4.6V-Flash | 80.4% | 71.6% | −8.9 pp |

For Qwen, 53 cells were fooled only with reasoning versus 12 only without it, a 4.4:1 imbalance; McNemar \(p=2.8\times10^{-7}\). For GLM, the counts were 29 versus 9, a 3.2:1 imbalance; \(p=1.7\times10^{-3}\).

Qwen generated about **2,646 reasoning tokens per cell**, compared with approximately **518** for GLM. The model reasoning about five times longer also showed roughly twice the on/off vulnerability gap, although the authors avoid drawing a firm trend from only two models.

When explicit reasoning was disabled, Qwen’s fooled outputs were still shorter than resisted ones (\(d=-0.412\), AUC 0.607). GLM’s length signal almost vanished (\(d=-0.059\)) because it produced uniformly short outputs.

### 4.8 Resistance requires sustained scrutiny

The 1,350 open-model cells were divided into:

- **A: resisted without mentioning the fake brand:** 340 cells;
- **B: mentioned but rejected it:** 307 cells;
- **C: fooled:** 703 cells.

Median reasoning lengths were:

- A: **1,312 characters**;
- B: **7,983 characters**;
- C: **1,360 characters**.

Mean reasoning shares were 0.578, 0.879, and 0.569, respectively. Group B reasoned about six times longer than A or C. Effect sizes for reasoning share were:

- B versus A: \(d=+1.22\);
- B versus C: \(d=+1.03\);
- C versus A: \(d=-0.03\).

Thus, fooled models do not generally resist by simply failing to notice the fake. Successful resistance occurs when a model notices the brand, examines it deeply, and rejects it. Ordinary or shallow reasoning often instead helps the model accept the planted evidence.

### 4.9 Brand knowledge predicts resistance

The authors elicited evidence-free top-five brand recommendations and measured cross-model agreement with mean pairwise Jaccard similarity. Categories in which models agreed about genuine brands were less vulnerable:

- Pearson \(r=-0.65\);
- \(p<0.01\).

Figure 8 visualizes this inverse relationship: smartphones have relatively high agreement and low vulnerability, while dining and services have lower agreement and higher vulnerability.

For four open models, alignment with the other models’ consensus correlated negatively with fooled rate:

- Spearman \(\rho=-0.450,-0.668,-0.646,-0.511\);
- mean absolute \(\rho=0.569\).

The number of distinct real brands in the polluted evidence correlated positively with vulnerability:

- \(\rho=+0.636,+0.586,+0.825,+0.696\);
- mean absolute \(\rho=0.686\).

A model-fixed-effects regression achieved:

- \(R^2=0.434\) using model identity alone;
- leave-one-out \(R^2=0.672\) with anchor-free brand-pool and consensus-alignment measures;
- in-sample \(R^2=0.780\) and leave-one-out \(R^2=0.727\) after adding evidence-pool size and whether the fake brand appeared in reasoning.

Commonality analysis assigned 58% of additive explanatory power to the features’ shared component, 29% to unique pool-size information, and 13% to unique alignment. A 1,000-resample mediation analysis estimated that **53.1%** of the alignment–vulnerability relationship flowed through evidence-pool size, with a 95% indirect-effect CI of **[−0.354, −0.146]**. The reverse mediation was only 28.1%.

The authors therefore identify **brand-pool richness and unstable prior knowledge** as primary drivers.

### 4.10 Models invent unsupported social proof

Fooled responses did more than copy fake names. They supplied claims such as community popularity, repeated testing, strong reputation, and frequent mentions across review sites—none of which appeared in the polluted documents.

In the screen-protector example:

- Claude Opus 4.7 claimed the fake Langyu brand was frequently recommended in technical communities and had passed repeated drop testing.
- DeepSeek V4 Pro called it a price-performance and reputation leader, supposedly endorsed across review sites and forums.
- o4-mini resisted and recommended genuine brands without mentioning Langyu.

Across the full population, fooled outputs used markers from a 14-phrase social-proof lexicon **1.5–11 times more often** than resisted outputs and used fewer hedging expressions. The models were actively constructing justifications for false recommendations.

### 4.11 English replication

The English study used:

- 12 models;
- 3 matched categories;
- 10 fresh products per category;
- US-region search results;
- 360 total trials.

Average English rates were:

- Smartphones/digital devices: **43%**, versus 23% in Chinese;
- Skincare: **58%**, versus 57%;
- San Francisco restaurants: **87%**, versus 82%.

The low–middle–high ordering was preserved for every model. Eight of 12 models were within ±10 percentage points of their average Chinese rate.

Average model shifts ranged from −20 to +40 points. Large positive shifts occurred for Gemini 3.1 Pro (+40), Gemini 3 Flash (+38), and o4-mini (+35). Claude Sonnet shifted −20; GPT-5.4, DeepSeek, and Ministral shifted slightly downward; Claude Opus, Qwen models, and GLM were modestly higher. The pattern was not simply closed-source versus open-weights.

### 4.12 Defense results

#### D1: Skepticism prompting

The added instruction asked models to distrust unfamiliar brands lacking multiple independent sources. It failed overall:

- pooled change across all models: **+10.5 percentage points**;
- closed-source mean: **+24 points**;
- open-weights mean: **−3 points**.

Closed-source effects included:

- Gemini 3.1 Pro: +44;
- Claude Opus 4.7: +32;
- Gemini 3 Flash: +31;
- GPT-5.4: +30;
- Claude Sonnet 4.6: +3;
- o4-mini: +2.

The prompt worsened 14 of 15 categories. Largest average backfires were:

- phone/PC: +32;
- bags/shoes: +19;
- makeup: +18;
- hospitality: +16;
- fitness: +14.

Skincare was the only overall improvement, at **−11 points**, driven by open models. Dining changed by only +6 because its baseline was already near saturation.

The authors’ interpretation is that skepticism forces models to engage with unfamiliar planted names, weakening the protection normally supplied by strong prior knowledge.

#### D2: Model-prior consensus filtering

D2 retained only brands that the same model also produced without evidence. It removed the fake in about **95%** of relevant cells, but also discarded **62%–79%** of legitimate recommendations, with a **68% mean** across the six open models.

#### D3: Cross-document corroboration

D3 required a brand to appear in at least \(\tau\) retrieved documents.

At \(\tau=4\):

- fake-brand catch rate: approximately **90%**;
- legitimate-brand survival: approximately **37%**;
- mean utility cost: **63%**, with model-specific costs of 52%–73%.

The threshold trade-off was:

| Threshold | Fake catch | Legitimate-recommendation cost |
|---:|---:|---:|
| 3 | 2% | 49% |
| 4 | 90% | 63% |
| 5 | 91% | 74% |

At threshold 3, the planted brand survives because it appears in exactly the three polluted documents. Increasing the threshold catches it but removes most legitimate recommendations too.

## 5. Analysis and Interpretation

The study answers its central question affirmatively: search-augmented LLMs can readily become promoters of fictional products after consuming a very small amount of plausible polluted content.

The findings indicate several mechanisms:

1. **Retrieval order is critical.** A single rank-1 page can dominate the recommendation, while an identical page at a later position is usually inert.
2. **Evidence quantity compounds risk.** A few mutually corroborating polluted pages can push vulnerable models beyond a 50% fooled rate.
3. **Prior brand knowledge is protective.** Models resist better in concentrated technical markets with well-established brands. They are weakest in fragmented, local, experiential, or taste-dependent categories.
4. **Reasoning has two different roles.** Turning reasoning on increases vulnerability on average because it encourages engagement with polluted evidence. However, among models that notice the fake brand, unusually deep reasoning can enable rejection. The important factor is sustained scrutiny, not the mere presence of a reasoning process.
5. **Failure is generative, not merely extractive.** Models embellish the fake with invented social proof, making the recommendation more persuasive than the source material itself.
6. **Simple defenses mis-handle the trade-off.** Skepticism prompts can amplify the attack, while strict consensus filters catch fake products only by suppressing a majority of legitimate recommendations.

The authors conclude that robust systems should intervene earlier in the pipeline through source-credibility weighting, evidence diversification, cross-document corroboration, and noise-robust grounding rather than relying solely on prompts or post-hoc filtering.

## 6. Contributions and Novelty

The paper’s main contributions are:

- It introduces **FORGE**, a benchmark and evaluation harness for controlled web-content pollution in search-augmented recommenders.
- It isolates the causal effect of replacing a real brand with a fake one while preserving rank, URL, source attribution, style, length, and surrounding context.
- It evaluates 12 production models across 225 products, 15 categories, and five consumer scenarios.
- It provides controlled rank-position and dose-response curves showing that one top-ranked page or a few mutually reinforcing pages can be enough.
- It demonstrates that vulnerability is not explained by model size or closed/open status but is strongly related to the stability of prior brand knowledge.
- It provides paired causal evidence that internal reasoning can increase vulnerability.
- It identifies fabricated social proof as a characteristic failure pattern.
- It evaluates entity replacement, passage injection, and full-page synthesis, finding full synthesis strongest and simple insertion weakest on average.
- It reproduces the category ordering in an English-language study.
- It quantitatively demonstrates the failure modes of skepticism prompting and two consensus filters.
- The authors characterize FORGE as the first Chinese benchmark specifically targeting retrieval-time web pollution and release it for defensive research.

## 7. Limitations and Caveats

- **The attacks were not optimized.** The authors did not search for maximally effective templates or combine query-aware writing, domain specialization, and adversarial SEO. Reported rates may therefore be lower bounds.
- **The simulation does not pollute the live web.** It locally modifies frozen search bundles for ethical and reproducibility reasons. Real GEO also affects what the search engine retrieves and ranks.
- **Attack styles change multiple factors.** A3 removes real-brand corroboration, changes the document body, and uses a new same-domain path. Its advantage over A1 cannot be attributed to a single realism dimension.
- **A2 has lower fake-brand density than A1/A3.** The study cannot fully distinguish protection from remaining real brands from the effect of less fake text.
- **Some secondary analyses cover only open models.** Dose-response and rank-position studies use the three Digital Product categories; model-prior filtering uses six open models; causal reasoning ablation covers only Qwen3.5-9B and GLM-4.6V-Flash; reasoning-trace analysis cannot be confirmed on closed models.
- **Language and geography are limited.** The main study is Chinese, and local-life data are fixed to Shenzhen. English replication covers only three categories and one other city, San Francisco.
- **The evidence is a static April 2026 snapshot.** Exact category rates may change as the web evolves.
- **Anchor selection uses a heuristic pipeline.** Human reviewers did not always agree on the dominant brand, although sensitivity tests found no evidence that disagreement inflated category vulnerability.
- **The recommendation metric uses substring matching.** Short Chinese prefixes can collide with ordinary text. Audits found only a 0.30% empty-evidence false-positive rate and no clean-evidence false positives, far below the minimum 13.3% attacked rate.
- **The benchmark measures recommendation inclusion, not downstream consumer behavior.**
- **The synthetic polluted documents are private.** They are withheld to reduce misuse; released artifacts are intended for non-commercial defensive research.
- **The authors received no compensation or incentive from any tested model provider.**

## 8. Future Work or Open Questions

The paper identifies several next steps:

- Conduct a full multilingual and multi-region evaluation rather than only Chinese plus a three-category English replication.
- Test whether the reasoning-trace resistance signature generalizes to closed-source models.
- Develop controlled-density passage-injection experiments that preserve real brands while matching the length and fake-brand density of full synthesis.
- Study how vulnerability changes across retrieval snapshots as web content evolves.
- Build retrieval-time defenses based on:
  - source credibility;
  - evidence-source diversification;
  - robust grounding under noisy evidence;
  - meaningful cross-document corroboration.
- Find defenses that catch fake products without eliminating 52%–79% of valid recommendations.
- Examine more sophisticated, domain-tailored, query-aware, or adversarial-SEO attacks in controlled settings.
- Clarify how shallow versus sustained reasoning can be detected or governed so that models scrutinize suspicious evidence without being drawn into endorsing it.

## 9. High-Level Takeaway (Plain Language)

A search-connected AI can be persuaded to recommend a completely fake product by changing only one highly ranked webpage. If several pages repeat the fake brand, some models recommend it almost every time—and may invent claims that communities trust or test it. Bigger models, closed models, explicit reasoning, and instructions to “be skeptical” do not reliably solve the problem. The safest direction is to improve how recommendation systems select, diversify, verify, and weigh web evidence before asking the model to produce an answer.