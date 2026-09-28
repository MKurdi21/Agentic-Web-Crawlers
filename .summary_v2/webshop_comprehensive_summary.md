# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible range | Pages 1–14 |
| Apparently missing pages | None within the supplied 14-page PDF |
| Main-paper text | Available as page-labeled native/extracted text |
| Visually inspected pages | Pages 1–10 |
| Pages not visually rendered | Pages 11–14, which contain references only |
| Figures | Figures 1–4 visually available and readable |
| Tables | Tables 1–5 visually available and generally readable |
| Equations | Equations (1)–(5) are available, but extraction damaged some mathematical symbols; interpretation below is cautious |
| Algorithms/pseudocode | None |
| Theorems/proofs | None |
| Appendices | Not included in the supplied 14 pages |
| Supplementary material | Not supplied |
| Referenced but absent material | Appendix §§A.1–A.6, B, C, and D; the project-site code, data, and demonstrations |
| OCR requirement | No page-level OCR was needed; mathematical extraction remains OCR-sensitive |
| Truncation | The supplied main text ends after the references. Several promised implementation and experimental details exist only in absent appendices |
| Other limitations | Figure 4 reports performance “over 3 trials,” but its variance/error information is not visually plotted. Exact training hyperparameters, hardware, seeds, and most appendix ablations cannot be assessed |

This is a machine-learning benchmark and experimental systems paper. It introduces an environment and dataset, proposes imitation-learning and reinforcement-learning agents, evaluates them against heuristic and human baselines, conducts ablations and trajectory analyses, and tests zero-shot transfer to two real websites.

# 1. Plain-Language Orientation

WebShop asks an artificial agent to shop from a written request. For example, the request might ask for a portable folding desk with a particular color, feature, and maximum price. The agent must turn that request into a search query, inspect search results, open products, read noisy product descriptions, select options such as size or color, possibly backtrack or search again, and finally buy an appropriate item.

The problem matters because many earlier language benchmarks are static: a model reads text and returns one answer. Conversely, earlier interactive environments may be small, artificial, expensive to evaluate, or based on low-level mouse actions. The authors want an environment that combines realistic language, images, long sequences of decisions, scalable data collection, and automatically calculated rewards (§1, pp. 1–3).

They construct WebShop from 1,181,436 Amazon products and collect 12,087 natural-language shopping instructions. A deterministic search engine and four-page website simulation make the environment repeatable. A reward checks whether the purchased item matches requested attributes, options, product type, and price (§3, pp. 3–5).

The authors then compare:

- A fixed rule: search using the complete instruction and buy the first result.
- Imitation learning (IL): learn search queries and button choices from human demonstrations.
- Reinforcement learning (RL): optimize choices using WebShop’s automatic reward.
- IL followed by RL (IL+RL).
- Human workers and selected human experts.

The strongest reported WebShop task score is 62.4/100 for IL+RL, versus 45.6 for the rule and 82.1 for human experts. Its exact-success rate is 28.7%, versus 9.6% for the rule and 59.6% for experts (Fig. 4; §5.2, pp. 7–8). Pure IL has a slightly higher success rate, 29.1%, but a lower average score, 59.9.

The central contribution is therefore not a shopping agent that has solved online shopping. It is a scalable benchmark and experimental platform exposing where grounded web agents fail: selecting noisy product options, reformulating searches, exploring consistently, and remembering previously inspected products.

# 2. Document Roadmap

1. **Abstract and §1 Introduction (pp. 1–3):** motivate scalable grounded-language environments; introduce WebShop and headline results.
2. **§2 Related Work (p. 3):** position WebShop relative to web navigation, supervised webpage tasks, and web-assisted natural-language processing.
3. **§3 The WebShop Environment (pp. 3–6):**
   - §3.1 formulates the task as a partially observable Markov decision process.
   - §3.2 describes product collection, retrieval, attribute mining, instructions, and human demonstrations.
   - §3.3 identifies the benchmark’s research challenges.
4. **§4 Methods (pp. 6–7):**
   - Rule baseline.
   - Imitation learning for searches and choices.
   - Reinforcement-learning fine-tuning.
5. **§5 Experiments (pp. 7–10):**
   - Dataset split and evaluation.
   - Main performance and ablations.
   - Human–agent and oracle analyses.
   - Zero-shot transfer to Amazon and eBay.
6. **§6 Discussion (p. 10):** synthesizes contributions and proposes future directions.
7. **Acknowledgements and References (pp. 10–14).**
8. **Appendices A–D:** repeatedly referenced but absent from the supplied document.

# 3. Background and Context

A **grounded language agent** connects words to observations and actions in an environment. Understanding “black,” for example, must influence which visible product option it clicks.

A **sequential decision problem** requires several dependent actions rather than one classification. An early search affects available products, which affects later option choices and the final reward.

A **partially observable Markov decision process (POMDP)** represents an environment in which the agent acts from incomplete observations. Here the underlying state is a webpage, but product reward attributes are hidden from the agent (§3.1, p. 4).

**Imitation learning (IL)** trains a model to reproduce actions found in demonstrations. WebShop separately imitates human search-query generation and human button choices (§4.2, pp. 6–7).

**Reinforcement learning (RL)** adjusts a policy using rewards obtained through interaction. The WebShop RL stage starts from the imitation-trained choice model and uses policy gradients (§4.3, p. 7).

**BART** is the paper’s pretrained sequence-to-sequence text model for generating searches. **BERT** is the pretrained Transformer used to represent webpage observations and candidate actions. **ResNet-50** represents product images. Their internal pretraining corpora and architecture details are not explained in this paper.

**BM25** is the sparse retrieval method used by WebShop’s Pyserini search engine. It ranks products using indexed product text (§3.2, p. 5).

**Sim-to-real transfer** means training in the simulated WebShop environment and deploying the resulting policy on real Amazon and eBay pages without further model training (§5.4, p. 10).

# 4. Research Problem and Gap

## Existing problem

Language models need environments in which language is tied to meaningful actions and automatically measurable outcomes. Static language datasets do not test sustained interaction, while interactive environments often have restricted language or costly human feedback (§1, pp. 1–2).

## Shortcomings attributed to previous approaches

According to §1 and §2:

- Some web benchmarks reduce interaction to one classification or API prediction.
- Some contain only a few page types or short action sequences.
- WikiNav mainly supports following links and stopping.
- MiniWoB uses low-level mouse/keyboard actions and lacks long-range navigation across diverse pages.
- Longer web tasks such as WebGPT depend on human evaluation.
- Supervised product-page datasets do not test extended decision making.
- Traditional web-assisted NLP uses search chiefly to retrieve evidence rather than as a rich action environment.

These are author characterizations of prior work, not independently verified judgments.

## Research gap

The authors identify a missing combination of:

- Realistic, scalable language and product data.
- Diverse, long-horizon web interaction.
- Semantic actions transferable across sites.
- Automatically computable rewards.
- Both textual and visual observations.
- A platform supporting IL and RL without continuous human scoring.

## Motivation

The web is described as scalable, semantic, interactive, dynamic, and realistic. Shopping provides explicit goals and objectively checkable properties, making it a candidate for scalable grounded-language research (§1, pp. 1–2).

## Scope

WebShop is limited to simulated e-commerce shopping over five product categories. The action interface abstracts the web into semantic `search[...]` and `choose[...]` commands. It does not evaluate unrestricted browser operation or low-level pointing and typing.

# 5. Research Questions / Objectives / Hypotheses

The paper does not state formally numbered research questions or hypotheses.

## Explicit objectives

- Build a scalable web environment combining realistic language, products, images, and automatic rewards (§1).
- Train autonomous agents to complete multi-step shopping tasks (§§1, 4).
- Measure how IL, RL, and pretrained representations affect performance (§§4–5).
- Analyze the gap between agents and humans (§5.3).
- Test whether WebShop-trained agents transfer without fine-tuning to Amazon and eBay (§5.4).

## Informal research questions reconstructed from those objectives

These are **analyst-organized objectives**, not author-labeled RQs:

- **RQ1:** Can WebShop provide a realistic, scalable, automatically scored language-grounding benchmark?
- **RQ2:** How well do rule, IL, RL, and IL+RL agents perform relative to humans?
- **RQ3:** Which components—language-pretrained search, language-pretrained choice, demonstrations, and reward training—matter?
- **RQ4:** What behaviors explain the remaining human–agent gap?
- **RQ5:** Do policies trained in WebShop transfer to real shopping websites?

## Hypotheses

No formal statistical hypotheses are supplied. The Methods section expresses design expectations—for example, that the rule should have low success and that sampling may encourage diverse behavior—but these are not presented as preregistered hypotheses.

# 6. Assumptions / Threat Model

This is not a security paper, so no attacker or cybersecurity threat model applies.

## System and environmental assumptions

- A task consists of one instruction and an e-commerce interaction ending when the agent chooses `Buy`.
- Pages fall into four abstract types: search, results, item, and item-detail (§3.1, p. 4).
- Transitions are deterministic inside WebShop.
- The BM25 search engine is deterministic (§3.2, p. 5).
- Search is available only from the search page; other pages expose discrete text-button choices.
- Candidate buttons are presented to the model as an action set, rather than requiring pixel-coordinate clicking.
- Product attributes used for reward computation are hidden from ordinary agents.
- The target product is the source of the instruction, but another product can receive full reward if it satisfies the same request.
- The instruction’s price ceiling is higher than the target’s price.
- All models train and evaluate in “simple” textual mode; human WebShop evaluations use the HTML interface (§3.1, p. 4).
- The real-site experiment assumes a translator can expose Amazon/eBay pages in the model’s expected simple representation. The two coding changes are not specified in the supplied main text (§5.4).
- The choice oracle is privileged: it can access hidden attributes, options, and the reward and exhaustively inspect candidates (§5.3, p. 9).

# 7. Methodology

## Study design

This is a mixed benchmark/systems/experimental study. The authors:

1. Construct a simulated shopping environment.
2. Populate it with real product records.
3. collect natural-language instructions and human trajectories.
4. Train several agent variants.
5. Evaluate them on 500 held-out instructions.
6. Compare them with rules and humans.
7. Conduct component ablations, behavior analyses, and an oracle study.
8. Test transfer on 100 tasks on each of two real shopping sites.

## Environment architecture

WebShop is modular: website transitions are separated from task instructions and reward computation, intended to permit new tasks or domains (§3, p. 4).

The four page types and permitted transitions are listed in Table 1:

- Search query: search page → results.
- Back to search: any applicable page → search.
- Previous/next results page: results → results.
- Product title: results → item.
- Product option: item → updated item.
- Description/overview: item → item-detail.
- Previous: item-detail → item.
- Buy: item → episode termination.

## Observations and actions

Two rendering modes are provided:

- **HTML mode:** full browser presentation for humans.
- **Simple mode:** removes extraneous HTML metadata and exposes text with marked clickable actions for models.

The action abstraction has two forms:

- `search[query]`
- `choose[button text]`

This abstraction is central to transfer: agents need not learn site-specific mouse coordinates.

## Product data

Author-reported in §3.2 (p. 5):

- 1,181,436 Amazon products.
- Five categories: fashion, makeup, electronics, furniture, and food.
- 113 subcategory query names.
- Average product-text length: 262.9.
- Vocabulary: 224,041 words appearing more than ten times.
- 842,849 unique product options.

The precise scraping, cleaning, deduplication, exclusion, and missing-data procedures are deferred to absent Appendix §A.1.

## Attribute mining

The authors calculate term frequency–inverse document frequency (TF-IDF) for product-category bigrams, manually inspect the top 200 bigrams per category, remove phrases judged noisy or not human-understandable, and consolidate 670 attributes. These attributes are assigned to products and hidden from agents (§3.2, p. 5). Detailed assignment rules are absent with Appendix §A.2.

## Search engine

Pyserini indexes concatenated title, description, overview, and customization-option text using BM25. Indices are built offline, and retrieval is deterministic (§3.2, p. 5). Search parameters are not in the supplied main text.

## Instruction collection

Amazon Mechanical Turk workers see a sampled product’s title, category, attributes, and options. They write a command for an automated shopper, avoiding verbatim full titles while faithfully describing the target.

The resulting dataset contains:

- 12,087 instructions.
- Vocabulary of 9,036 words.
- Mean instruction length of 15.9 words.

Worker compensation, screening, quality-control rates, and interface details are deferred to Appendix §A.4.

## Human demonstrations

Thirteen workers were recruited and trained; the top seven were designated experts. Qualification tests were used to select motivated workers (§3.2, p. 5). The experiment uses:

- 1,012 training trajectories.
- 54 development trajectories.
- Human trajectories for all 500 test tasks (§5.1, p. 7).

The abstract’s “over 1,600” demonstrations is consistent with at least 1,566 explicitly enumerated trajectories, though the exact total is not stated in the main text.

## Dataset split

The 12,087 instructions are split independently and identically distributed (i.i.d.) into:

- Train: 10,587.
- Development: 1,000.
- Test: 500.

The counts sum exactly to 12,087 (**analyst-derived check:** 10,587 + 1,000 + 500). Splitting by product category is proposed as future work; the current split may share category characteristics across partitions (§5.1).

## Rule baseline

The rule searches the entire instruction verbatim, selects the first returned product, selects no customization options, and buys it (§4.1, p. 6).

## Imitation learning

### Search model

The authors extract 1,421 instruction–search pairs from 1,012 training trajectories. BART is fine-tuned to maximize the probability of the demonstrated search given only the instruction. It receives no history of previous searches or inspected products (§4.2, p. 6).

At interaction time, BART produces five beam-search candidates; the system chooses one randomly (§4.2–4.3, p. 7).

### Choice model

The choice dataset contains 9,558 observation/action examples from training trajectories. A 12-layer pretrained BERT encodes the observation and each candidate button. Cross-attention lets each candidate attend to the observation. The representation is mean-pooled and mapped to a scalar action score; a softmax gives a probability distribution over buttons (§4.2, pp. 6–7; Fig. 3).

The model samples from that distribution rather than always taking the highest-scoring button. The authors say this helps prevent narrow exploration or repeated oscillation.

### Images

A pretrained ResNet-50 maps images to 512-dimensional features. A learned linear layer maps these to 768 dimensions, after which they are concatenated with BERT’s observation representation (§4.2, p. 7).

## Reinforcement learning

The authors fine-tune the imitation-trained choice model using online policy-gradient RL. BART is frozen because they report concern that directly optimizing generated language with RL could cause language drift. BART supplies ten candidate searches, and the choice policy learns which to select (§4.3, p. 7).

Training includes:

- Policy-gradient loss.
- Learned value-function baseline.
- Squared-error value loss.
- Entropy term intended to discourage premature policy collapse.

## Baselines and ablations

Figure 4 evaluates:

- Rule.
- IL without language-pretrained choice.
- IL without language-pretrained search.
- Full IL.
- Pure RL.
- RL with recurrent neural-network text encoders.
- IL+RL.

A history ablation adds one previous observation and five previous actions, reducing the score from 59.9 to 57.3 (§5.2, p. 8).

## Metrics

- **Task Score:** 100 times mean episode reward.
- **Success Rate (SR):** percentage of episodes with reward exactly 1.
- Four diagnostic components: attribute, option, product-type, and price scores.
- Trajectory statistics: states visited, unique items inspected, and searches performed.

Figure 4 reports three trials. The supplied paper does not give confidence intervals, error bars, standard deviations, seeds, or statistical-test details. Although the prose uses “significantly,” no inferential statistical evidence is supplied in the main paper.

## Unreported configuration

Hardware, optimizer, learning rate, batch size, discount factor, entropy coefficient, maximum episode length, training duration, random seeds, and checkpoint criteria beyond use of 54 development demonstrations are not specified in the supplied main text. They may be in absent Appendices B and C.

# 8. Experiments / Analyses

## X1 — Main WebShop performance

**Purpose:** Compare learned agents, rules, and humans.

**Data:** 500 test instructions; model results averaged over three trials.

**Metrics:** Task Score and Success Rate.

**Results:** Rule 45.6/9.6%; IL 59.9/29.1%; IL+RL 62.4/28.7%; human expert 82.1/59.6% (Fig. 4; Table 2).

**Interpretation:** IL delivers a large gain over the fixed rule. RL after IL increases partial reward but slightly lowers exact completion.

**Caveat:** The paper reports no uncertainty bars or statistical test despite “significantly” language.

## X2 — IL component ablations

**Purpose:** Test the contribution of pretrained choice and learned search generation.

- Removing pretrained choice yields 45.8 score and 10.6% SR.
- Removing pretrained search yields 56.0 and 26.3%.
- Full IL yields 59.9 and 29.1%.

Pretrained choice is the more consequential component. Learned search still contributes approximately 3.9 score points and 2.8 percentage points of SR relative to IL without it (**analyst-derived differences**).

## X3 — RL initialization and architecture ablations

- Pure RL: 52.5 score, 11.2% SR.
- RL with RNN encoders: 55.2 score, 17.6% SR.
- IL+RL: 62.4 score, 28.7% SR.

The authors infer that imitation warm-starting and strong pretrained language representations are important.

## X4 — History ablation

Adding one prior observation and the last five actions reduces score from 59.9 to 57.3 (§5.2, p. 8). A simple short-history concatenation therefore does not solve the memory problem.

## X5 — Score-component and trajectory analysis

Table 2 compares rule, IL, IL+RL, and experts on attribute, option, type, price, and browsing behavior.

Experts lead on every reward component. The largest reported model–expert deficit is option matching: expert 73.9 versus IL 45.2 or IL+RL 38.9.

RL raises IL’s attribute score from 69.3 to 74.0, type from 86.4 to 89.7, and price from 84.0 to 88.7, but lowers option score from 45.2 to 38.9. It also shortens trajectories and reduces exploration (§5.3, pp. 8–9).

## X6 — Qualitative trajectory comparison

Table 3 shows two tasks.

For blackout shades, the human reformulates a verbose measurement phrase into “66 x 66,” finds matching size/color options, and obtains reward 1.0. IL+RL performs three actions and receives 0.2.

For a hand-painted gingko pillow cover, the human explores product details, returns to an earlier product, selects size and color/design options, and obtains 1.0. IL+RL immediately buys a different product and obtains 0.25.

The authors use these examples to illustrate query reformulation, option interpretation, exploration, and memory. Two hand-picked examples do not establish prevalence by themselves.

## X7 — Choice-oracle analysis

**Purpose:** Separate search quality from downstream choice quality.

**Setup:** For 500 test instructions, a privileged oracle exhaustively evaluates every retrieved item and all options using hidden reward data. Four search sources are tested.

| Query source | Score | SR |
|---|---:|---:|
| Complete instruction | 79.7 | 52.6% |
| IL BART query | 83.0 | 57.6% |
| Human’s first query | 82.1 | 57.9% |
| Human’s last query | 84.4 | 61.0% |

The oracle raises the rule-query SR from 9.6% to 52.6% and the IL-query condition from the full IL agent’s 29.1% to 57.6%. This supports the authors’ claim that action and option selection is a major bottleneck.

The oracle takes more than 100 steps per episode and has hidden information, so it is diagnostic rather than deployable. In 74.8% of human trajectories there is only one query, limiting the distinction between first and last human searches (p. 9 footnote).

## X8 — Zero-shot Amazon transfer

**Data:** 100 sampled test instructions; no fine-tuning; manual scoring with Eq. (1).

- Rule: 45.8 score, 19% SR.
- IL: 61.5, 27%.
- IL+RL: 65.9, 25%.
- Human: 88.2, 65% in Table 5.

IL+RL obtains the highest agent score, while IL has the highest agent SR.

## X9 — Zero-shot eBay transfer

On the same stated 100-task transfer setup:

- Rule: 31.7 score, 7% SR.
- IL: 58.2, 21%.
- IL+RL: 62.3, 21%.
- Human: 79.7, 40%.

The two learned models tie on SR, while IL+RL has the higher partial-credit score.

## X10 — Runtime observation

Humans require an average of 815 seconds per Amazon episode, whereas IL and IL+RL require under eight seconds (§5.4, p. 10). Hardware and timing methodology are not supplied, so this is not a controlled computational-efficiency comparison.

# 9. Results

## Benchmark difficulty

The rule earns a substantial partial score, 45.6, because lexical retrieval can find related products, but succeeds completely on only 9.6% of tasks. This gap shows that retrieving a roughly relevant product is easier than satisfying every requested property and option.

## Benefit of imitation learning

Full IL improves over the rule by:

- **14.3 score points:** 59.9 − 45.6.
- **19.5 percentage points of SR:** 29.1% − 9.6%.

These differences are **analyst-derived absolute differences**, not relative percentages.

## Effect of RL after IL

IL+RL improves Task Score from 59.9 to 62.4, an absolute 2.5-point gain. Its SR falls from 29.1% to 28.7%, a 0.4-percentage-point reduction. The reward-component analysis attributes this pattern to stronger attribute/type/price matching but weaker option selection and less exploration.

## Human–agent gap

Relative to experts, IL+RL is lower by:

- 19.7 Task Score points: 82.1 − 62.4.
- 30.9 SR percentage points: 59.6% − 28.7%.

The prose sometimes calls 29.1% the “best model’s” SR, because IL has the highest SR even though IL+RL has the best Task Score (§5.2).

## Option selection as the main bottleneck

Experts score 73.9 on options, versus 45.2 for IL and 38.9 for IL+RL (Table 2). The oracle analysis independently shows that keeping a query fixed but making exhaustive privileged choices raises SR into the 52.6–61.0% range.

## Search quality still matters

With the choice oracle, BART’s query obtains 57.6% SR versus 52.6% for the unmodified instruction. The human last query obtains 61.0%, the best Table 4 result. Search reformulation therefore matters, but the paper’s evidence indicates that ordinary agents lose more performance during choice than during retrieval.

## Transfer

Learned agents retain broadly similar scores on WebShop, Amazon, and eBay, while the rule varies more:

- IL+RL: 62.4 WebShop; 65.9 Amazon; 62.3 eBay.
- Rule: 45.6 WebShop; 45.8 Amazon; 31.7 eBay.

This supports nontrivial transfer under the paper’s semantic-interface setup. It does not establish unrestricted autonomous browsing.

# 10. Figure-by-Figure Interpretation

### Figure 1 — WebShop interface, trajectory, and product notation

**Location:** p. 2.

**Panel A:** A visual HTML-mode trajectory. Red numbered annotations show search, result selection, option selection, detail inspection/backtracking, and purchase. The final displayed reward is 1.0.

**Panel B:** The same type of result page in simple mode. Clickable actions are blue, and the selected action is bold. This is the format used for model training and evaluation.

**Panel C:** Defines the product/instruction representation:

- \(u\): instruction.
- \(\bar y\): product text.
- \(y_{\text{price}}\): price.
- \(Y_{\text{opt}}\): options.
- \(Y_{\text{att}}\): hidden attributes.

**Purpose:** Demonstrates that the task is a multi-page, multi-action interaction rather than a one-shot product classifier.

**Caveat:** The figure is a single successful example and does not quantify typical behavior.

### Figure 2 — Target-product rank under verbatim instruction search

**Location:** p. 4.

This is a pie chart with three visually readable categories:

- Rank 1: **32.2%**.
- Rank 1–50 but on pages 2–5: **11.7%**.
- Not found within ranks 1–50: **56.1%**.

The categories sum to 100.0% (**analyst-derived check**). Thus the target product is not among the first 50 results for more than half the instructions when the full instruction is used directly.

The chart supports learned query generation and exploration. It concerns the original target product, while the reward allows alternative fully satisfying products; target rank is therefore not identical to task solvability.

### Figure 3 — Choice-model architecture

**Location:** p. 6.

The diagram shows three representational streams:

1. Product image → ResNet.
2. Instruction/page text → Transformer initialized with BERT.
3. Each candidate action → a weight-sharing Transformer encoder.

Image and text representations are concatenated. An attention-fusion/cross-attention layer combines the observation with each action representation. The fused representation is mean-pooled and passed through a multilayer perceptron (MLP) to produce \(S(o,a)\), a scalar logit. The illustrated action is `choose[khaki]`.

Arrows show data flow from inputs to representations, fusion, pooling, and scoring. Candidate actions are evaluated individually with shared parameters; softmax across their scores produces the policy.

### Figure 4 — WebShop task performance and model components

**Location:** p. 8.

Two bar charts show Task Score and Success Rate. Values are explicitly labeled:

| Model | Score | SR |
|---|---:|---:|
| Rule | 45.6 | 9.6% |
| IL without pretrained choice | 45.8 | 10.6% |
| IL without pretrained search | 56.0 | 26.3% |
| IL | 59.9 | 29.1% |
| RL | 52.5 | 11.2% |
| RL (RNN) | 55.2 | 17.6% |
| IL+RL | 62.4 | 28.7% |

Horizontal references mark human average/expert performance:

- Score: average 75.5; expert 82.1.
- SR: average 50.0%; expert 59.6%.

A component matrix indicates use of pretrained search, pretrained choice, demonstrations, and reward. The caption says results are over three trials, but no error bars or per-trial data appear.

# 11. Table-by-Table Interpretation

### Table 1 — Permitted WebShop actions and transitions

**Location:** p. 4.

It defines the environment’s transition structure across four page types. Search and choice are mutually exclusive action classes depending on the current page. All transitions are described as deterministic, including retrieval through the fixed search engine.

### Table 2 — Reward decomposition and browsing behavior

**Location:** p. 8.

| Model | Overall | Attribute | Option | Type | Price |
|---|---:|---:|---:|---:|---:|
| Rule | 45.6 | 66.6 | 0.0 | 80.5 | 86.0 |
| IL | 59.9 | 69.3 | 45.2 | 86.4 | 84.0 |
| IL+RL | 62.4 | 74.0 | 38.9 | 89.7 | 88.7 |
| Human expert | 82.1 | 81.8 | 73.9 | 94.4 | 97.7 |

The right side reports average with maximum/minimum in parentheses:

| Model | States | Items | Searches |
|---|---:|---:|---:|
| Rule | 3.0 (3/3) | 1.0 (1/1) | 1.0 (1/1) |
| IL | 9.4 (90/3) | 1.6 (11/1) | 1.3 (17/1) |
| IL+RL | 4.5 (5/1) | 1.0 (1/1) | 1.0 (1/1) |
| Human expert | 11.3 (114/4) | 1.9 (16/1) | 1.4 (16/1) |

The table demonstrates expert superiority, IL exploration, and the post-RL reduction in trajectory length. There is a source inconsistency: §5.3 prose says IL+RL’s trajectory length falls to **4.8**, whereas Table 2 and its later oracle discussion report **4.5**. The supplied work does not resolve which is correct.

### Table 3 — Human and IL+RL trajectory examples

**Location:** p. 9.

It contrasts long, adaptive human trajectories with three-action IL+RL trajectories. Item names and some human actions are explicitly truncated. Red text represents option choices and blue text attributes. It is qualitative evidence, not an exhaustive error distribution.

### Table 4 — Choice-oracle results

**Location:** p. 9.

It compares four search-query sources while holding downstream choice at an exhaustive privileged oracle. Human last queries are best at 84.4 score and 61.0% SR; BART is competitive with human first queries. No uncertainty or significance test is reported.

### Table 5 — Zero-shot transfer to Amazon and eBay

**Location:** p. 10.

It reports overall Score/SR plus attribute, option, type, and price components for rule, IL, IL+RL, and humans.

Important observations:

- IL+RL has the best learned-agent score on both websites.
- IL has higher SR than IL+RL on Amazon, 27% versus 25%.
- IL and IL+RL tie at 21% SR on eBay.
- Humans lead all conditions.
- The rule performs much worse on eBay than Amazon.

The prose reports the Amazon human score as **88.0**, but Table 5 reports **88.2**. The table value is retained as the exact tabulated result; the inconsistency cannot be resolved from the supplied material.

# 12. Diagram / Architecture Interpretation

The substantive architecture diagram is Figure 3.

The system is factorized into search and choice:

```text
Instruction
   ├── BART → candidate search queries
   └── BERT observation encoder
Images → ResNet → projected visual features ─┐
                                             ├─ observation representation
Candidate buttons → shared BERT encoder ─────┘
                         ↓
                cross-attention/fusion
                         ↓
                    mean pooling
                         ↓
                    scalar score
                         ↓
            softmax/sample a web action
```

During IL, BART learns demonstrated searches and BERT learns demonstrated choices. During IL+RL, BART is frozen and generates a restricted set of ten search candidates; the choice policy learns among these and other available buttons using reward.

This modular division is methodologically important. It avoids directly applying RL to free-form language generation, but it also means search generation cannot use interaction history in the described IL model.

# 13. Equations and Mathematical Concepts

### Equation (1) — Episode reward

**Location:** §3.1, p. 5.

The rendered formula is:

\[
r =
r_{\text{type}}
\cdot
\frac{
|U_{\text{att}}\cap Y_{\text{att}}|
+
|U_{\text{opt}}\cap Y_{\text{opt}}|
+
\mathbf{1}[y_{\text{price}}\le u_{\text{price}}]
}{
|U_{\text{att}}|+|U_{\text{opt}}|+1
}.
\]

The visual typesetting indicates that \(r_{\text{type}}\) multiplies the entire normalized match expression.

- \(U_{\text{att}}\): requested attributes.
- \(Y_{\text{att}}\): purchased product’s hidden attributes.
- \(U_{\text{opt}}\): requested options.
- \(Y_{\text{opt}}\): selected product options.
- \(y_{\text{price}}\): purchased-product price.
- \(u_{\text{price}}\): instruction’s price ceiling.
- \(\mathbf{1}[\cdot]\): 1 when the price condition holds, otherwise 0.
- \(r_{\text{type}}\): product-type compatibility from `TextMatch`.

The numerator counts matched requirements plus price compliance. The denominator normalizes by the number of requested elements. Type matching suppresses rewards for superficially similar but wrong product classes. The exact `TextMatch` formula is absent with Appendix §A.5.

### Equation (2) — Search imitation loss

\[
\mathcal L_{\text{search}}
=
\mathbb E_{(u,a)\sim D}
[-\log \pi_\phi(a\mid u)].
\]

This is negative log-likelihood. The model is penalized when it assigns low probability to a human-demonstrated search \(a\) for instruction \(u\). Minimizing it trains BART to imitate human queries.

### Equation (3) — Choice imitation loss

\[
\mathcal L_{\text{choose}}
=
\mathbb E_{(o,A(o),a^*)\sim D'}
[-\log \pi_\theta(a^*\mid o,A(o))].
\]

- \(o\): current observation.
- \(A(o)\): available button actions.
- \(a^*\): demonstrated human action.
- \(\pi_\theta\): learned choice policy.

It is a multiclass negative-log-likelihood objective over currently available buttons.

### Equation (4) — Choice policy scoring

The extracted notation is damaged, but the text defines the intended computation:

\[
\pi_\theta(a\mid o,A(o))
\propto
\exp(S(o,a)),
\]

where \(S(o,a)\) results from BERT encodings of the observation and action, cross-attention, mean pooling, and multiplication by a learned matrix/vector \(W\).

Plainly: score every visible button according to how well it fits the current instruction/page, then normalize all scores into probabilities.

### Equation (5) — Policy-gradient loss

\[
\mathcal L_{\text{PG}}
=
\mathbb E_\pi[
-(R_t-V(o_t))
\log \pi(a_t\mid o_t,A(o_t))
].
\]

- \(R_t\): discounted return-to-go, recursively defined using reward and discount \(\gamma\).
- \(V(o_t)\): learned estimate of expected return.
- \(R_t-V(o_t)\): advantage-like signal.
- \(a_t\): action taken at time \(t\).

Actions yielding better outcomes than predicted are made more likely; worse-than-predicted actions are discouraged.

The value function is trained with:

\[
\mathcal L_{\text{value}}=(R_t-V(o_t))^2.
\]

An entropy-related term is added to resist premature convergence. The printed definition is \(\sum_a \pi(a)\log\pi(a)\), which is negative Shannon entropy; minimizing it with a positive coefficient encourages higher entropy. The coefficients and \(\gamma\) are not supplied.

The total stated RL loss is:

\[
\mathcal L_{\text{RL}}
=
\mathcal L_{\text{PG}}
+
\mathcal L_{\text{value}}
+
\mathcal L_{\text{entropy}}.
\]

# 14. Interpretation and Discussion

The results answer the informal objectives as follows:

- **RQ1:** WebShop demonstrates a large, automatically scored, interactive benchmark containing realistic product text, options, images, and multi-step navigation.
- **RQ2:** Learned agents substantially beat a fixed retrieval rule but remain far below humans.
- **RQ3:** Pretrained choice representations and imitation warm-starting are especially important. Learned search generation also helps.
- **RQ4:** The main observed failures concern noisy option matching, insufficient exploration, poor query reformulation, and lack of long-term memory.
- **RQ5:** Agents retain useful performance on Amazon and eBay through a semantic page translator without fine-tuning.

A central methodological insight is that average reward and exact success need not move together. RL makes the agent better at acquiring partial reward but slightly worse at satisfying everything. The paper interprets this as more “greedy” behavior: the agent commits earlier, checks fewer products, and more often misses customization options.

The evidence also separates retrieval from interaction. Figure 2 shows verbatim instructions often fail to retrieve the target in the first 50 results. Yet Table 4 shows that, once retrieval results are provided, a privileged choice procedure can more than double ordinary agents’ success. Both stages matter, but downstream choice is the stronger demonstrated bottleneck.

The transfer result is promising under the paper’s abstraction. It should not be interpreted as proof that the agents can robustly operate arbitrary websites: they receive translated semantic observations and actions, and the necessary interface engineering is not described in the supplied main text.

## Internal inconsistencies and unresolved points

- Rule SR is reported as 9.6% in Fig. 4 and the abstract, but rounded to 10% in §5.2. This appears to be ordinary rounding.
- The abstract rounds IL+RL SR to 29% and expert SR to 59%; exact figure values are 28.7% and 59.6%.
- §5.3 says IL+RL trajectory length is 4.8; Table 2 and later text say 4.5.
- Table 5 gives Amazon human score 88.2; adjacent prose says 88.0.
- The paper uses “significantly” without reporting a statistical test, uncertainty interval, or p-value in the supplied main text.
- Human “average” and “expert” refer to different worker groupings, but the complete aggregation protocol is deferred to Appendix §A.6/C.

# 15. Contributions and Novelty

## Conceptual

The paper frames online shopping as a grounded, long-horizon language-interaction problem combining search, reading, comparison, customization, and purchase.

## Dataset

- 1,181,436 real product records.
- 12,087 crowdsourced instructions.
- 670 mined attributes.
- 842,849 unique customization options.
- More than 1,600 human demonstrations according to the abstract.

## Benchmark

WebShop supplies deterministic transitions, a repeatable search engine, semantic action choices, two observation modes, and an automatically computed partial-credit reward.

## System

The environment is implemented using Flask and packaged through an OpenAI Gym-style interface. It separates page transitions from task-specific instructions and reward.

## Methodological

The authors factor action generation into BART-based search and BERT/ResNet-based choice, then combine imitation and reinforcement learning.

## Experimental

They provide baseline comparisons, component ablations, reward-component analysis, trajectory analysis, a privileged choice oracle, and zero-shot deployment to Amazon and eBay.

## Empirical

The work documents a large human–agent gap and localizes much of it to option selection, semantic matching, exploration, reformulation, and memory.

# 16. Limitations

## Authors' stated limitations

The authors do not provide a dedicated limitations section, but explicitly acknowledge:

- Models remain far below human experts (§§1, 5.2).
- Search generation ignores past searches and visited items (§4.2).
- Agents lack adequate memory for comparison and backtracking (§§3.3, 5.3).
- Agents struggle with noisy paraphrases in product options (§5.3).
- RL fine-tuning becomes less exploratory and lowers option performance (§5.3).
- A simple history mechanism degrades performance (§5.2).
- Direct RL without imitation performs poorly (§5.2).
- The i.i.d. split does not test stronger category-level generalization (§5.1).
- Human data have a caveat: some crowd workers may lack patience and consistency, depressing the nonexpert human average (p. 3 footnote).
- The choice oracle is unrealistic, hidden-information access and takes over 100 steps (§5.3).
- Real-site interactions are slower for humans, but the transfer requires small coding adaptations rather than being interface-free (§5.4).

## Additional evidence-based analyst observations

These are not author admissions:

- Product data come from one commercial source and five categories, limiting domain and marketplace coverage.
- Hidden attributes are created partly through manual judgment over top TF-IDF bigrams; annotation consistency cannot be evaluated without Appendix §A.2.
- The reward uses lexical/heuristic matching and may not capture all semantic notions of user satisfaction.
- Full success can be obtained by a product other than the generating target; appropriate for open-ended shopping, but it complicates retrieval analyses based on target rank.
- Humans use HTML while models use simplified observations, so their interfaces are not identical.
- The paper supplies no statistical uncertainty for three-trial model results.
- Manual real-site scoring may introduce evaluator variation; the protocol is absent.
- Real-site evaluation uses only 100 tasks.
- The interface abstraction removes low-level visual interaction and much website variability.
- Commercial webpages and inventories are dynamic, but the experiment’s dates and captured conditions are not provided.
- Missing appendices prevent full reproducibility assessment.

# 17. Threats to Validity

## Internal validity

Model improvements combine several ingredients—pretraining, architecture, demonstrations, sampling, and reward learning. The ablations help separate them, but absent hyperparameters and uncertainty estimates limit causal confidence. Real-site manual scoring could also vary between evaluators.

## Construct validity

Reward approximates instruction satisfaction through mined attributes, exact option matches, price compliance, and heuristic type similarity. This measurable construct may differ from genuine consumer preference, quality, availability, safety, shipping constraints, or satisfaction.

Success Rate is stringent but inherits the reward’s representation. Task Score gives partial credit and may reward agents that consistently buy approximately relevant products.

## Statistical conclusion validity

Figure 4 averages three trials but does not show variance. No confidence intervals, tests, or effect-size uncertainty are reported. Statements of statistical significance cannot be independently evaluated from the supplied material.

## External validity

Generalization is demonstrated only for Amazon and eBay and only through 100 instructions under a translated semantic interface. Generalization to other sites, tasks, languages, layouts, or product domains is not established.

## Ecological validity

Product records and real websites add realism, but the model does not interact through ordinary low-level browser controls. WebShop also ends at simulated purchase selection and does not address authentication, payment, shipping, popups, failures, or changing inventory.

## Reproducibility

Deterministic search and released project artifacts are favorable design choices. However, the supplied document lacks appendices, code, versions, seeds, hardware, optimization settings, scraper details, and real-site adapter details.

## Data leakage and split validity

The split is i.i.d. by instruction, not by product category. The main text does not say whether products or near-duplicate instructions can occur across partitions. No explicit leakage analysis is supplied.

# 18. Future Work and Open Questions

## A. Future work proposed by the authors

- Query generation and reformulation that reacts to retrieval results.
- Strategic and intrinsic-reward exploration.
- Explicit working or episodic memory for comparison and backtracking.
- More robust semantic handling of noisy webpage text and option names.
- Multimodal pretraining over images and language.
- Pretraining on hypertext and web instruction–action mappings.
- Stronger category-based or otherwise distribution-shifted splits.
- More powerful RL architectures with better language and task priors.
- New web tasks and domains built through WebShop’s modular design.

## B. Additional open questions

- How reliable are the mined attributes and `TextMatch` reward against independent human judgments?
- How often does reward 1 correspond to genuine user satisfaction?
- Would performance persist under inventory, layout, language, or site-policy changes?
- Can agents learn memory without the failure observed for simple history concatenation?
- Can exploration improve option success without making trajectories prohibitively long?
- How much performance comes from simplified semantic page translation?
- Are products, sellers, or near-duplicate instructions shared across splits?
- How sensitive are results to beam size, stochastic sampling, and reward coefficients?
- Can real-site evaluation be made repeatable without freezing dynamic webpages?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| Agent | A program that observes a page and chooses the next action |
| Grounding | Connecting language to objects, properties, and actions in an environment |
| NLP | Natural language processing |
| RL | Reinforcement learning: learning from interaction rewards |
| IL | Imitation learning: learning to copy demonstrated actions |
| POMDP | A sequential decision model where the agent cannot directly see all relevant state |
| Observation \(o\) | The page/instruction representation visible to the agent |
| State \(s\) | The underlying webpage state |
| Action \(a\) | A search query or selected text button |
| Policy \(\pi\) | A probability distribution over actions |
| Reward \(r\) | A number from 0 to 1 measuring final purchase compatibility |
| Task Score | 100 times average reward |
| SR | Success Rate: fraction of episodes with reward exactly 1 |
| Attribute | A descriptive property such as “waterproof” |
| Option | A selectable field/value such as color = khaki |
| BM25 | The sparse text-ranking method used for search |
| TF-IDF | A method for identifying phrases characteristic of documents/categories |
| BART | Pretrained sequence-to-sequence model used for search generation |
| BERT | Pretrained Transformer used for observations and candidate actions |
| Transformer | Attention-based neural network for text representation |
| ResNet-50 | Image encoder used to produce visual features |
| RNN | Recurrent neural network; used in an RL ablation |
| Beam search | Procedure retaining several high-probability generated sequences |
| Logit \(S(o,a)\) | Unnormalized numerical score assigned to an action |
| Softmax | Converts action scores into probabilities |
| Cross-attention | Lets an action representation focus on relevant observation content |
| Return-to-go \(R_t\) | Expected discounted reward from time \(t\) onward |
| Value \(V(o)\) | Prediction of future return from an observation |
| Entropy regularization | Objective term encouraging a less prematurely deterministic policy |
| Oracle | Privileged diagnostic procedure with information unavailable to normal agents |
| Sim-to-real | Training in simulation and evaluating in a real environment |
| \(u\) | Natural-language instruction |
| \(\bar y\) | Aggregated product text |
| \(Y_{\text{att}}\) | Product’s hidden attribute set |
| \(Y_{\text{opt}}\) | Product’s available/selected options |
| \(U_{\text{att}}\) | Attributes required by the instruction |
| \(U_{\text{opt}}\) | Options required by the instruction |
| \(y_{\text{price}}\) | Product price |
| \(u_{\text{price}}\) | Instruction’s maximum permitted price |
| \(r_{\text{type}}\) | Heuristic score for matching the correct product type |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Products | 1,181,436 | products | Five Amazon categories | Author-reported | p. 5, §3.2 |
| Categories | 5 | categories | Fashion, makeup, electronics, furniture, food | Author-reported | p. 5 |
| Subcategory queries | 113 | queries | Scraping | Author-reported | p. 5 |
| Product-text mean length | 262.9 | unspecified text-length unit | Title/item details | Author-reported | p. 5 |
| Product vocabulary | 224,041 | words | Frequency >10 | Author-reported | p. 5 |
| Unique options | 842,849 | options | Product corpus | Author-reported | p. 5 |
| Attribute pool | 670 | attributes | TF-IDF/manual filtering | Author-reported | p. 5 |
| Instructions | 12,087 | instructions | Full benchmark | Author-reported | p. 5 |
| Instruction vocabulary | 9,036 | words | Full instruction set | Author-reported | p. 5 |
| Mean instruction length | 15.9 | words | Full instruction set | Author-reported | p. 5 |
| Worker pool / experts | 13 / 7 | people | Demonstration collection | Author-reported | p. 5 |
| Train/dev/test | 10,587/1,000/500 | instructions | i.i.d. split | Author-reported | p. 7 |
| Search IL pairs | 1,421 | pairs | From 1,012 trajectories | Author-reported | p. 6 |
| Choice IL examples | 9,558 | examples | Training trajectories | Author-reported | p. 6 |
| Choice encoder | 12 | layers | BERT | Author-reported | p. 6 |
| Image vectors | 512→768 | dimensions | ResNet then projection | Author-reported | p. 7 |
| Rule performance | 45.6 / 9.6 | Score / % SR | WebShop test | Visually readable | Fig. 4, p. 8 |
| IL performance | 59.9 / 29.1 | Score / % SR | WebShop test | Visually readable | Fig. 4 |
| IL+RL performance | 62.4 / 28.7 | Score / % SR | WebShop test | Visually readable | Fig. 4 |
| Expert performance | 82.1 / 59.6 | Score / % SR | WebShop test | Visually readable | Fig. 4 |
| Expert–IL+RL SR gap | 30.9 | percentage points | 59.6−28.7 | Analyst-derived | Fig. 4 |
| Target ranked first | 32.2 | % | Instruction used verbatim | Visually readable | Fig. 2, p. 4 |
| Target at ranks 1–50 but pages 2–5 | 11.7 | % | Verbatim instruction | Visually readable | Fig. 2 |
| Target absent from top 50 | 56.1 | % | Verbatim instruction | Visually readable | Fig. 2 |
| Choice oracle, instruction query | 79.7 / 52.6 | Score / % SR | 500 tests | Author-reported | Table 4, p. 9 |
| Choice oracle, BART query | 83.0 / 57.6 | Score / % SR | 500 tests | Author-reported | Table 4 |
| Choice oracle, human last query | 84.4 / 61.0 | Score / % SR | 500 tests | Author-reported | Table 4 |
| Amazon IL+RL | 65.9 / 25 | Score / % SR | 100 transfer tasks | Author-reported | Table 5, p. 10 |
| eBay IL+RL | 62.3 / 21 | Score / % SR | 100 transfer tasks | Author-reported | Table 5 |
| Amazon human | 88.2 / 65 | Score / % SR | Table value | Visually readable | Table 5 |
| eBay human | 79.7 / 40 | Score / % SR | Transfer | Author-reported | Table 5 |
| Human Amazon time | 815 | seconds/episode | Mean | Author-reported | p. 10, §5.4 |
| IL/IL+RL Amazon time | <8 | seconds/episode | Mean stated collectively | Author-reported | p. 10 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| WebShop is large-scale | 1.18M products, 12,087 instructions, 842,849 options | Dataset construction | §3.2, p. 5 | Strong descriptive evidence; collection details absent |
| Task is nontrivial | Rule has 45.6 score but 9.6% SR | X1, Fig. 4 | pp. 7–8 | Strong within-benchmark evidence |
| IL improves over fixed rules | IL 59.9/29.1% vs rule 45.6/9.6% | X1 | Fig. 4 | Clear numerical difference; no uncertainty |
| Pretrained choice representations matter | Removing them gives 45.8/10.6% | X2 | Fig. 4 | Strong ablation evidence |
| Learned searches help | Full IL 59.9/29.1%; no pretrained search 56.0/26.3% | X2 | Fig. 4 | Moderate ablation evidence |
| Imitation warm-start is important for RL | Pure RL 52.5/11.2%; IL+RL 62.4/28.7% | X3 | Fig. 4 | Supports claim; other training differences incompletely documented |
| RL increases partial matching but reduces exact success | Score 59.9→62.4; SR 29.1→28.7 | X1/X5 | Fig. 4; Table 2 | Strong descriptive result |
| RL reduces exploration | Fewer states/items/searches after RL | X5 | Table 2, §5.3 | Supported, subject to 4.5/4.8 inconsistency |
| Option choice is a major bottleneck | Low option scores and large oracle gains | X5/X7 | Tables 2 and 4 | Converging quantitative evidence |
| Humans use more adaptive search/memory | Longer trajectories plus two examples | X5/X6 | Tables 2–3 | Quantitative behavior counts plus limited qualitative examples |
| Agents remain far below humans | 28.7% vs 59.6% expert SR | X1 | Fig. 4 | Strong benchmark evidence |
| WebShop policies transfer to real sites | Learned models beat rules on Amazon/eBay without fine-tuning | X8/X9 | Table 5 | Meaningful but limited to 100 tasks/site and translated interface |
| WebShop enables fast execution | Models <8 s vs humans 815 s on Amazon | X10 | §5.4, p. 10 | Hardware/timing protocol unavailable |

# 22. Very Simple Explanation

Imagine giving a computer a request such as: “Find me a small folding desk that is already assembled, is khaki, and costs under $125.” The computer cannot answer with a sentence. It has to shop: search, open products, read their details, choose the right color, and decide what to buy.

The researchers built a huge practice store called WebShop using more than a million real product listings. They also collected over twelve thousand human-written shopping requests. Because the store knows each product’s properties, it can automatically give the agent partial credit or full credit for its purchase.

Agents trained from human examples were much better than a simple rule that bought the first search result. Reinforcement learning improved how closely purchases matched requests on average, but it made the agent rush: it explored less and slightly reduced the number of perfectly completed tasks. Humans were still about twice as successful.

The most serious problem was not merely finding relevant search results. Agents often failed to understand and select messy options such as unusual size or color labels. Humans were better at rewriting searches, comparing products, going back to earlier items, and remembering what they had seen. The benchmark’s main value is that it makes these weaknesses visible and measurable.

# Completeness Audit

## Inventory

- **Title:** *WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents*
- **Authors:** Shunyu Yao, Howard Chen, John Yang, Karthik Narasimhan
- **Venue:** 36th Conference on Neural Information Processing Systems (NeurIPS 2022)
- **Document type:** Benchmark/dataset, machine-learning agent, and experimental systems paper
- **Accessible pages:** 14
- **Major sections:** Abstract; §§1–6; acknowledgements; references
- **Substantive subsections:** §§3.1–3.3, 4.1–4.3, 5.1–5.4
- **Figures:** 1–4
- **Tables:** 1–5
- **Major equations:** (1)–(5), plus value and entropy losses embedded in prose
- **Algorithms:** None
- **Formal research questions/hypotheses:** None
- **Distinct analyses:** Main benchmark, IL ablations, RL ablations, history ablation, reward/trajectory decomposition, qualitative trajectories, choice oracle, Amazon transfer, eBay transfer, runtime comparison
- **Appendices referenced:** A.1–A.6, B, C, D; absent
- **Supplementary artifacts:** Project site/code/data/demos referenced but not supplied

## Coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes | Yes | Fully represented | Headline scale and results included |
| §1 Introduction | Yes | Yes | Fully represented | Motivation, gap, contributions |
| §2 Related Work | Yes | Yes | Represented in compressed form | Three prior-work categories retained |
| §3 Environment | Yes | Yes | Fully represented | Design and modularity |
| §3.1 Task Formulation | Yes | Yes | Fully represented | POMDP, observations, actions, reward |
| §3.2 Implementation | Yes | Yes | Fully represented subject to absent appendices | Data, retrieval, attributes, instructions, humans |
| §3.3 Challenges | Yes | Yes | Fully represented | Search, exploration, semantics, memory |
| §4 Methods | Yes | Yes | Fully represented | Rule, IL, RL |
| §4.1 Rule | Yes | Yes | Fully represented | Exact behavior stated |
| §4.2 IL | Yes | Yes | Fully represented | Search, choice, images, pipeline |
| §4.3 RL | Yes | Yes | Fully represented | Policy/value/entropy objectives |
| §5 Experiments | Yes | Yes | Fully represented | All main experiments separated |
| §5.1 Setup | Yes | Yes | Fully represented | Splits and demonstrations |
| §5.2 Results | Yes | Yes | Fully represented | Main results and ablations |
| §5.3 Analysis | Yes | Yes | Fully represented | Components, trajectories, oracle |
| §5.4 Transfer | Yes | Yes | Fully represented | Amazon/eBay and timing |
| §6 Discussion | Yes | Yes | Fully represented | Meaning and proposed directions |
| Figure 1 | Visually | Yes | Fully represented | Panels A–C audited |
| Figure 2 | Visually | Yes | Fully represented | All three labeled percentages |
| Figure 3 | Visually | Yes | Fully represented | Architecture and data flow |
| Figure 4 | Visually | Yes | Fully represented | All labeled model results |
| Table 1 | Visually/textually | Yes | Fully represented | Actions and transitions |
| Table 2 | Visually/textually | Yes | Fully represented | Scores, counts, inconsistency noted |
| Table 3 | Visually/textually | Yes | Fully represented | Truncation disclosed |
| Table 4 | Visually/textually | Yes | Fully represented | All four oracle conditions |
| Table 5 | Visually/textually | Yes | Fully represented | Both sites and inconsistency noted |
| Equation (1) | Visually/textually | Yes | Fully represented with notation caution | Exact appendix definition missing |
| Equations (2)–(5) | Visually/textually | Yes | Fully represented | Extraction damage handled through prose |
| Value/entropy losses | Textually | Yes | Fully represented | Coefficients absent |
| Algorithms | Yes | Yes | Not applicable | No formal algorithms |
| Major contributions | Yes | Yes | Fully represented | Separated by contribution type |
| Author-stated limitations | Yes | Yes | Fully represented | Paper has no dedicated limitations section |
| Acknowledgements | Yes | Minimally | Inspected but deliberately omitted as non-substantive | Funding and thanks do not affect method/results |
| References | Yes as supplied text | Compressed | Inspected but deliberately compressed | Related-work role summarized; individual entries not restated |
| Appendices A–D | No | No | Missing from supplied material | Frequently referenced |
| Code/data/demos | No | No | Missing from supplied material | URL appears on p. 1 only |
| Supplementary material | No | No | Missing from supplied material | None embedded |

## Missing or inaccessible material

- Appendix §A.1: detailed product scraping.
- Appendix §A.2: attribute mining/assignment details.
- Appendix §A.3: search-engine configuration.
- Appendix §A.4: instruction-annotation interface and process.
- Appendix §A.5: exact `TextMatch` formula.
- Appendix §A.6: human-worker examples/protocol.
- Appendix §B: detailed model methods.
- Appendix §C: setup, hyperparameters, and additional ablations.
- Appendix §D: expanded sim-to-real analysis.
- Project-site code, data, and demonstrations.
- Hardware, software versions, seeds, optimization settings, uncertainty measurements, and several implementation details.
- Visual renderings of pp. 11–14 were not provided, but these pages contain references rather than substantive figures or results.

## Uncertain interpretations

- Equation extraction corrupts some symbols, especially Eq. (4). Its computational meaning is recoverable from the accompanying prose and Figure 3, but exact typography is not fully reliable.
- `TextMatch` cannot be evaluated because its formula is absent.
- Table 2 reports IL+RL trajectory length 4.5, while prose reports 4.8.
- Table 5 reports Amazon human score 88.2, while prose reports 88.0.
- “Significant” improvements cannot be interpreted statistically because tests and uncertainty are absent.
- The exact total behind “over 1,600 human demonstrations” is not enumerated in the main text.
- Product-text “average length 262.9” does not explicitly state whether its unit is words, tokens, or another segmentation unit.

## Deliberately compressed material

- The 59 bibliographic entries were not individually summarized; their thematic use in §2 and §6 was represented.
- Acknowledgement names and the full funding disclaimer were omitted as non-substantive to the scientific claims.
- Repeated statements of the same headline agent–human gap were consolidated.
- Table 5’s complete component values are discussed and the principal figures retained, but not every component was duplicated again in the compact numerical ledger.
- Figure captions were integrated into the corresponding audits rather than repeated verbatim.

## Potential omissions

No known substantive item from the accessible main-paper inventory was omitted. The largest coverage gap is not an overlooked main-text item but the complete absence of the referenced appendices and external project artifacts. Consequently, the benchmark’s headline design and results can be represented, but its full implementation, annotation, training, reproducibility, and expanded transfer details cannot be assessed from the supplied material.