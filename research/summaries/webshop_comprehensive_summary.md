## Stage 0 — Document Accessibility Report

The supplied work is **WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents**, by Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan, affiliated with Princeton University's Department of Computer Science. Yao and Chen are marked as equal contributors. The first page identifies the venue as the 36th Conference on Neural Information Processing Systems, NeurIPS 2022.

**Access and inspection:** extracted text is supplied for physical PDF pages 1–14. Pages 1–10 are also supplied as rendered images and were visually inspected, including the environment screenshots, architecture diagram, plots, equations, and tables. Pages 11–14 were inspected through supplied text only; these pages contain the reference list. Thus, this analysis is neither entirely text-only nor a visual inspection of every PDF page. All four numbered figures and all five numbered tables occur on visually supplied pages. Their substantive labels and numerical values are readable, although small diagram text and mathematical typography require cross-checking with the extracted text. No additional OCR, browsing, code execution, or tools were used.

The available main narrative runs from the abstract through Discussion and Acknowledgements. This establishes coverage of the supplied main text, not completeness of every artifact associated with the publication. Appendices A–D are repeatedly referenced but are absent from the supplied 14 pages. In particular, product scraping details, attribute annotation details, the complete type-matching reward formula, annotation interfaces, demonstration examples, additional model/training details, additional ablations, and transfer implementation details cannot be inspected. No separate supplementary files are supplied. The provided accessibility metadata's empty appendix detection does not override the main text's explicit appendix references.

The attachment error concerning a local image at '-' does not prevent inspection of the ten displayed page images. No substantive content is assumed to exist in that failed attachment. The given source hash is retained as an identifier; it was not independently recomputed.

**Evidence convention:** [A] means author-reported information; [B] means directly observable visual evidence; [C] means analyst-derived arithmetic with operands shown; [D] means analyst interpretation. No [E] external information is introduced. Confidence is HIGH for clear supplied statements and values, MEDIUM for qualified interpretations or unresolved presentation issues, and UNKNOWN for absent information. Page citations refer to physical PDF pages, whose printed numbers agree with the supplied sequence where visible.

**Research-question boundary:** the user's question is 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis.' WebShop is a benchmark and agent-capability paper, not a security study. It does not directly compare web agents with standalone large language models, measure adversarial vulnerability, or test attacks or defenses. Its relevance to that question is explicitly an analyst inference about the interaction surfaces and action pathways that the paper documents.

## 1. Plain-language orientation

WebShop studies an AI agent that must shop according to a person's written request. Completing the request requires more than producing a plausible answer: the agent must search, inspect products, read descriptions, choose options such as size or color, and terminate by selecting Buy. A product that looks relevant can still fail because its options, price, or properties do not satisfy the instruction. [A; pp. 1–2, 4–5]

The authors' central contribution is a simulated shopping website built from real product information, paired with natural-language instructions and an automatic reward. This combination is intended to support interactive learning at scale without asking humans to judge every training episode. The environment contains 1,181,436 scraped products and 12,087 crowdsourced instructions. It supplies both a browser-oriented HTML interface and a simplified representation used by the evaluated models. [A; pp. 2, 5]

The researchers train agents to imitate human searches and clicks, then optionally improve their choices through reinforcement learning. The strongest average task score is 62.4 out of 100 for imitation learning followed by reinforcement learning, abbreviated IL+RL. Its full-success rate is 28.7%. Imitation learning alone, IL, achieves a slightly lower score of 59.9 but a slightly higher full-success rate of 29.1%. The rule baseline achieves 45.6 and 9.6%, while human experts achieve 82.1 and 59.6%. The two metrics therefore identify different best models. [A/B; pp. 7–8, Fig. 4, Table 2]

The paper also tests WebShop-trained agents on Amazon and eBay without further training. The results support some transfer of shopping capability under the reported setup, while substantial gaps from human performance remain. They do not demonstrate secure deployment, resistance to malicious web content, or the safety of real financial transactions. [A for transfer results; D for the security boundary; p. 10]

## 2. Document roadmap

The document is a mixed **benchmark, dataset, system, and empirical machine-learning paper**. Its main structure is:

| Inventory ID | Original component | Pages | Role |
|---|---|---|---|
| ABS | Abstract | 1 | Benchmark, models, headline outcomes, transfer claim |
| S1 | §1 Introduction | 1–3 | Motivation, research gap, task, contributions |
| S2 | §2 Related Work | 3 | Three categories of prior work |
| S3 | §3 The WebShop Environment | 3–6 | Environment design and learning challenges |
| SS3.1 | §3.1 Task Formulation | 4–5 | States, actions, observations, instructions, reward, metrics |
| SS3.2 | §3.2 Environment Implementation | 5 | Product collection, search, attributes, instructions, demonstrations |
| SS3.3 | §3.3 Research Challenges | 5–6 | Query generation, exploration, understanding, memory |
| S4 | §4 Methods | 6–7 | Rule, imitation, and reinforcement learning agents |
| SS4.1 | §4.1 Rule Baseline | 6 | Instruction-text search and first-item purchase |
| SS4.2 | §4.2 Imitation Learning | 6–7 | BART searches; BERT/image-conditioned choices |
| SS4.3 | §4.3 Reinforcement Learning | 7 | Online fine-tuning and restricted search candidates |
| S5 | §5 Experiments | 7–10 | Setup, performance, ablations, diagnostics, transfer |
| SS5.1 | §5.1 Setup and task verification | 7 | Splits and demonstrations |
| SS5.2 | §5.2 Results | 7–8 | Main comparisons and ablations |
| SS5.3 | §5.3 Analysis | 8–10 | Score components, trajectories, choice oracle |
| SS5.4 | §5.4 Zero-shot Sim-to-real Transfer | 10 | Amazon/eBay evaluation |
| S6 | §6 Discussion | 10 | Implications and future methods |
| ACK | Acknowledgements | 10 | Credits and funding |
| REF | References [1]–[59] | 11–14 | Bibliographic context, inspected through text |

The substantive visual inventory consists of F1–F4 and T1–T5. F1 has three distinct panels: the HTML interaction trajectory, the simple-mode observation, and product notation. F3 is the model architecture. F4 combines a model-component checklist with score and success-rate plots. Numbered equations E1–E5 define reward, imitation losses/policy, and the policy-gradient loss. Additional unnumbered formulas define the process, metrics, reward components, return, value baseline, value loss, entropy loss, and total RL loss. No numbered algorithm, pseudocode listing, theorem, lemma, or proposition is supplied.

The experimental register comprises X1 main performance, X2 imitation ablations, X3 reinforcement-learning ablations, X4 history augmentation, X5 component/trajectory analysis, X6 qualitative trajectories, X7 choice oracle, and X8 real-site transfer. F2 separately diagnoses retrieval when the full instruction is used as the query. The paper states objectives rather than formal numbered research questions or hypotheses.

## 3. Background and context

**Natural language processing (NLP)** concerns the language inputs and representations in this work. **Language grounding** means connecting the instruction to the products, properties, and actions of an interactive environment. Here, an instruction is grounded successfully when the final selected item satisfies the benchmark's matching criteria. Producing a fluent description alone does not satisfy the task. [A; pp. 1–2]

**Imitation learning (IL)** trains a model from examples of human behavior. The authors use one model to imitate search queries and another to imitate button choices. **Reinforcement learning (RL)** improves an action policy using rewards from interactions. The policy is a probability distribution over available actions. An episode is one shopping attempt ending with Buy; the reward measures how well the chosen product satisfies the instruction. [A; pp. 4–7]

A **pre-trained model** begins with previously learned representations before being adapted to WebShop. BART supplies search-query generation; its cited reference expands its title as 'Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension.' BERT, Bidirectional Encoder Representations from Transformers, supplies text representations for observations and actions. ResNet-50 is the pre-trained image model named in the Methods; ResNet refers to the residual-network model family described by the cited title 'Deep Residual Learning for Image Recognition.' These reference titles identify the components without importing performance claims from those outside works. [A; pp. 6–7, 11–12]

The **Document Object Model (DOM)** appears in the related-work discussion as a webpage representation used by other benchmarks. **HTML**, HyperText Markup Language, labels WebShop's browser-oriented observation mode. The simplified mode removes extraneous metadata from raw HTML. **Information retrieval (IR)** is the search component: the engine ranks product records in response to query text. The supplied work names BM25 as its sparse retrieval method but does not provide its mathematical definition. **TF-IDF**, term frequency–inverse document frequency, is named for identifying candidate attribute phrases; its exact scoring implementation is not supplied. [A; pp. 3–5]

An **ablation** changes or removes a model component to investigate its contribution. A **choice oracle** is a privileged diagnostic procedure that can see hidden reward information and exhaustively evaluate choices. It is not an ordinary deployable agent. **Zero-shot sim-to-real transfer** here means applying models trained in the simulation to real shopping websites without fine-tuning. [A; pp. 7–10]

## 4. Research problem and gap

**Existing problem:** according to the authors, environments for learning language-conditioned interaction often lack realistic language, require substantial human involvement, or are difficult to scale. Conversely, many strong language-model benchmarks are static and do not adequately ground language in actions and non-language concepts. [A; p. 1]

**Attributed shortcomings of previous approaches:** purely navigational tasks restrict actions to hyperlinks or stopping; MiniWoB lacks long-range decision making across multiple pages and relies on low-level clicks and keystrokes; supervised webpage tasks typically involve a single decision; and some interactive systems require human feedback because rewards are not automatically computable. These are the WebShop authors' descriptions, not independent findings about the cited literature. [A; pp. 2–3]

**Research gap:** a scalable environment combining realistic text/images, diverse semantic actions, multi-step decisions, and automatically computable feedback. WebShop addresses this through product search, inspection, customization, backtracking, and final selection. [A; pp. 1–3]

**Motivation:** automate tedious tasks while creating a benchmark that exposes difficulties in query formulation, noisy language interpretation, exploration, and memory. **Scope:** shopping-like tasks based on five product categories and instructions generated from sampled target products. The implementation is modular, but the supplied evaluation does not establish performance across all web tasks, arbitrary domains, or adversarial settings. [A for scope and motivation; D for evidentiary boundary; pp. 2–6, 10]

## 5. Research questions / objectives / hypotheses

There are no formal numbered research questions or statistical hypotheses in the supplied work. The following objectives reconstruct its organization and should not be mistaken for verbatim author questions:

1. **O1, benchmark objective:** construct a scalable interactive environment with realistic language/visual content and automatic feedback. [A; pp. 1–2]
2. **O2, modeling objective:** train and compare rule-based, imitation-learning, and reinforcement-learning agents. [A; pp. 3, 6–8]
3. **O3, diagnostic objective:** identify why agents fall short of humans through ablations, score components, trajectories, and oracle analysis. [A; pp. 3, 8–10]
4. **O4, transfer objective:** test whether simulation-trained agents can operate on Amazon and eBay without fine-tuning. [A; p. 10]

The authors explicitly hypothesize that a more powerful RL architecture could boost and stabilize performance if initialized with better language and task priors. This is a proposed explanation/future direction, not a hypothesis established by the reported experiments. [A; p. 8]

The user's security question remains outside these objectives. **Analyst inference:** O1 and the architecture provide evidence about where environmental information enters an agent and how it influences actions. None of O1–O4 measures whether those pathways are more exploitable than a standalone language model. [D]

## 6. Assumptions / threat model

The system is formulated as a **partially observable Markov decision process (POMDP)** with state space S, action space A, deterministic transitions T, reward function R, instruction space U, and observation space O. A state represents a webpage of one of four types. Search is available only on the search page; other pages offer choose actions. The simulated search engine is deterministic. [A; p. 4]

Instructions are based on a target product y*, contain a nonempty attribute set, may contain requested options, and include a price bound higher than the target product's price. Product attributes used for reward calculation are hidden from the ordinary task performer. The final product need not be the original target if another product fully satisfies the criteria. [A; pp. 4–5]

**No security threat model is specified.** The supplied material does not define an attacker, attacker-controlled content, malicious tools, credential access, privileged actions, exfiltration targets, or security policies. The task formulation describes available operations and reward criteria; it is not a specification of which components are secure or trusted under attack.

**Analyst interpretation for security research:** distinguish the user's instruction, retrieved product/page content, the observation-format conversion, the action-selection model, and executable actions. These are observable system boundaries that could guide a later threat model. Calling them potential study surfaces does not establish attacker control or vulnerabilities. The simulation's Buy action ends an episode; the paper does not establish that real-site evaluation completed monetary transactions. [D grounded in pp. 2, 4, 6–7, 10]

## 7. Methodology

### Environment and product collection

The authors scrape **1,181,436 Amazon products** using ScraperAPI, covering fashion, makeup, electronics, furniture, and food. They use **113 sub-category names** as queries. Product texts have reported average length **262.9**; the supplied sentence does not explicitly state the length unit, so it should not be silently relabeled as tokens. The reported vocabulary is **224,041**, restricted to words with frequency higher than 10. Products contain **842,849 unique options**. Detailed scraping procedures are deferred to absent Appendix A.1. [A; p. 5]

The search engine uses Pyserini with an offline BM25 sparse index. Each searchable record concatenates title, description, overview, and customization options. This determinism is intended to simplify imitation learning and result reproducibility. Search implementation details and BM25 parameters are not supplied. [A; p. 5]

Attributes are mined from category-specific title/description bigrams using TF-IDF. The top **200 bigrams per category** are inspected; noisy phrases are removed according to whether they are human-understandable. The consolidated pool contains **670 attributes**. These hidden attributes support reward computation. No inter-annotator agreement, complete assignment rules, or detailed filtering statistics are reported in the supplied main text. [A; p. 5]

### Instructions and demonstrations

Amazon Mechanical Turk, abbreviated AMT, workers receive a sampled goal product's title, category, attributes, and buying options. They write a command for an automatic shopping agent, avoiding excessive specificity such as copying the complete title while remaining faithful to the product. The resulting **12,087 instructions** have vocabulary **9,036 words** and average length **15.9 words**. The annotation interface and detailed process are absent with Appendix A.4. [A; p. 5]

The authors recruit and train **13 workers**, using qualification tests to select motivated participants, and designate the top **7** as experts. Human demonstrations use HTML mode. The split contains **10,587 training**, **1,000 development**, and **500 test** instructions, described as independent and identically distributed, or i.i.d. They collect **1,012 training demonstrations**, **54 development demonstrations**, and trajectories for all **500 test instructions**. The development demonstrations support hyperparameter tuning and checkpoint selection. [A; pp. 5, 7]

**Analyst-derived reconciliation:** 1,012 + 54 + 500 = **1,566** explicitly enumerated demonstrations. The abstract says 'over 1,600.' The available material does not identify additional demonstrations sufficient to reconcile these descriptions. It would be inappropriate to invent an extra collection or treat either description as an established correction. [C; pp. 1, 7]

### Baseline and imitation learning

The rule baseline searches the exact instruction text, selects the first result, and buys it without choosing options. It is a non-learned information-retrieval baseline that relies on lexical retrieval. [A; p. 6]

Search imitation uses **1,421 instruction–search pairs** from **1,012 training trajectories**. A BART model learns query generation conditioned only on the instruction: previous searches and visited products are excluded from this input. Multiple search pairs can arise from a trajectory, so the pair count is not a count of distinct demonstrations. At inference, IL generates the top **5** queries through beam search and randomly selects one. [A; pp. 6–7]

Choice imitation uses **9,558 samples**, each containing an observation, available actions, and the human-selected action. A **12-layer pre-trained BERT** encodes the observation and each candidate action. Cross-attention combines action and observation representations; mean pooling and a learned scoring transformation yield a scalar action score. Softmax converts the scores to a probability distribution over available actions. At inference, the policy samples an action to promote diversity and avoid cycles that may result from always taking the highest-scoring action. [A; pp. 6–7]

Image features come from a pre-trained **ResNet-50**. The reported feature dimension is **512**, transformed by a learned linear layer to **768**, then concatenated with observation-token representations. Those are the paper's reported dimensions; the absent Appendix B prevents fuller inspection of the extraction configuration. [A; p. 7]

### Reinforcement learning and evaluation

IL+RL fine-tunes the choice-based IL model with online RL. The authors freeze BART, citing concern about language drift from directly optimizing text generation through RL. BART supplies its top **10** generated searches as a restricted candidate action space, and the policy learns which to choose. A policy-gradient objective uses a learned value baseline sharing BERT weights with the policy; value and entropy terms are added. Discount factor, learning rates, coefficients, training duration, optimizer settings, random seeds, and hardware are not reported in the supplied main text. [A; p. 7]

Task Score is **100 × average reward**. Success Rate is the fraction of episodes with **r = 1**. Figure 4 reports test results over **3 trials**. Human/model comparison averages over the **500 test instructions**. Small error bars appear in the figure, but their statistical definition and exact numerical values are not supplied. No confidence intervals, named statistical tests, or p-values are provided in the available narrative. [A/B; pp. 5, 7–8]

## 8. Experiments / analyses

| ID | Purpose and setup | Main result | Caveat |
|---|---|---|---|
| X1 | Compare agents and humans on 500 i.i.d. test instructions; model figure covers 3 trials | IL+RL has highest score, 62.4; IL has highest agent success, 29.1% | Two metrics rank IL and IL+RL differently |
| X2 | Remove language pre-training from choice or replace learned search with instruction-text search | Choice ablation: 45.8/10.6%; search ablation: 56.0/26.3%, versus IL 59.9/29.1% | Component changes do not isolate every possible training interaction |
| X3 | Train RL without imitation warm-start; compare Transformer and recurrent text encoders | RL 52.5/11.2%; RL(RNN) 55.2/17.6%; IL+RL 62.4/28.7% | Prose's claim of being worse than the rule baseline conflicts with plotted central values |
| X4 | Add one previous observation and five previous actions to IL | Score falls from 59.9 to 57.3 | Failure of this history design does not establish that all memory designs fail |
| X5 | Decompose reward components and summarize trajectories | Experts strongest on all components; RL reduces option score despite higher total score | Table/text disagree on IL+RL average trajectory length |
| X6 | Compare two example human and IL+RL trajectories | Humans achieve r=1.0; models r=0.2 and 0.25 | Qualitative illustrations, with omitted actions and truncated names |
| X7 | Exhaustive choice oracle with four query sources on 500 tests | Success ranges 52.6–61.0%; highest with experts' final queries | Oracle sees hidden information and takes over 100 steps per episode |
| X8 | Apply three trained models to Amazon/eBay on 100 sampled tests without fine-tuning | IL+RL 65.9/25% on Amazon, 62.3/21% on eBay | Manual scoring; adapters and further analysis absent |

F2 is a related retrieval diagnostic: using the instruction directly as search query places the target on the first results page for 32.2%, pages 2–5 for 11.7%, and outside ranks 1–50 for 56.1%. Its denominator and complete measurement procedure are not specified in the supplied figure/text. It shows why an instruction-text query can limit target retrieval, while benchmark success can still occur through another satisfactory product. [A/B; pp. 4–5]

X5 and X6 examine distinct evidence: aggregate component scores and action counts versus two selected examples. X7 changes available information and computational effort; its improvements are diagnostic rather than a fair deployment-speed comparison. X8 changes websites and scoring procedure. These conditions must remain separate from the simulated 500-instruction results.

## 9. Results

**Main performance:** Figure 4 provides the following central values, ordered consistently by model rather than the extracted text's spatial order. [B; p. 8]

| Model | Task Score /100 | Success Rate % |
|---|---:|---:|
| Rule | 45.6 | 9.6 |
| IL without language-pre-trained choice | 45.8 | 10.6 |
| IL without learned/pre-trained search | 56.0 | 26.3 |
| IL | 59.9 | 29.1 |
| RL | 52.5 | 11.2 |
| RL with recurrent neural network encoder | 55.2 | 17.6 |
| IL+RL | 62.4 | 28.7 |
| Human average | 75.5 | 50.0 |
| Human expert | 82.1 | 59.6 |

**Analyst-derived differences:** IL+RL improves task score over Rule by **62.4 − 45.6 = 16.8 score points**, and success by **28.7 − 9.6 = 19.1 percentage points**. IL improves success over Rule by **29.1 − 9.6 = 19.5 percentage points**. RL fine-tuning improves IL's score by **62.4 − 59.9 = 2.5 points**, while reducing success by **29.1 − 28.7 = 0.4 percentage points**. Expert success exceeds the highest agent success by **59.6 − 29.1 = 30.5 percentage points**. These are differences, not relative-percent improvements. [C; operands from Fig. 4]

**Component pattern:** IL+RL improves attributes, type, and price relative to IL, but option score drops from **45.2 to 38.9**. Human experts reach **73.9** on options. The option gap between experts and IL is **73.9 − 45.2 = 28.7 score points**, derived; the text's '28% gap' is an imprecise approximate description, not a clearly defined relative percentage. [A/B/C; pp. 8–9, Table 2]

**Oracle results:** exhaustive choice raises success for instruction-text searches to **52.6%**, compared with Rule's **9.6%**, and for BART searches to **57.6%**, compared with IL's **29.1%**. The authors interpret this as evidence that choosing products/options is a major bottleneck. The diagnostic combines privileged hidden information with exhaustive exploration, so it does not isolate a single neural representation error. [A; p. 9]

**Transfer:** on Amazon, IL has the highest agent success, **27%**, while IL+RL has the highest agent score, **65.9**, with **25%** success. On eBay, IL and IL+RL tie at **21%** success; IL+RL has score **62.3**, above IL's **58.2**. Humans achieve **65%** and **40%** success respectively. These 100-instruction, manually scored real-site outcomes should not be treated as identical evaluation conditions to Figure 4. [A/B; p. 10]

## 10. Figure-by-figure interpretation

### Figure 1 — Environment and task representations

Panel A shows a browser-style shopping trajectory: enter a query, inspect search results, open an item, select a color, inspect Description/Overview, return, and Buy. Red arrows and circled step labels express a possible sequence; the screenshot is an example, not a frequency distribution. Product imagery, descriptions, buttons, and options are visible. The example completes with reward **1.0**. [B; p. 2]

Panel B shows the same kind of results page in simple mode. The instruction appears as text; button delimiters identify actions. Blue text indicates clickable actions, while bold text denotes the action selected by the agent. This panel explains how the environment exposes semantic choices without requiring precise mouse coordinates. [A/B]

Panel C links notation to the example: instruction u, aggregated product description y-bar, price **$109.0**, options **black, khaki, white**, and attributes **steel pipe, no assembly, portable**. The caption explicitly states that the attributes are hidden from the task performer. Their inclusion in the explanatory panel does not mean the ordinary agent receives the reward labels. [A/B]

There are no axes, statistical error bars, or sampling distributions. The figure supports the task specification and observation-mode distinction. The caption points to §3.2 for reward, while the actual reward formulation spans §3.1 and Eq. (1); this is a cross-reference imprecision rather than a substantive alternative definition.

### Figure 2 — Target retrieval using the instruction query

This is a three-slice pie chart with no axes. Blue represents **page 1, ranks 1–10: 32.2%**; orange represents **pages 2–5, ranks 11–50: 11.7%**; green represents **not found, ranks 51+: 56.1%**. All three are visually labeled exact values, not estimated from slice sizes. [B; p. 4]

The slices sum to **32.2 + 11.7 + 56.1 = 100.0%**, analyst-derived. Likewise, target retrieval within the first 50 results is **43.9%**, derived from 32.2 + 11.7. 'Not found' means outside the displayed rank range according to the label; it does not establish absence from the full corpus. The figure supports the challenge of query generation, but a missing original target does not logically prohibit success because other products may satisfy the instruction. The population used to produce the chart is not specified in the supplied material.

### Figure 3 — Choice-model architecture

The diagram contains an image branch through ResNet, an observation-text branch through a Transformer, and an action-text branch through a second shown Transformer. A dashed connection marks shared weights between the text encoders. The observation example contains both instruction and product/page text; the caption's shorthand emphasis on instruction u should be read alongside the Methods' encoding of observation o. [A/B; pp. 6–7]

Image and text embeddings are concatenated. Action and observation information enter an Attention Fusion Layer. Resulting action-related vectors are mean-pooled, passed to an MLP, and reduced to the scalar **S(o,a)**. The highlighted candidate is **choose[khaki]**. Gray faded alternatives illustrate other available buttons. Colored small token shapes distinguish representation streams; they do not encode numerical performance.

No plot axes or uncertainty measures apply. This is a data-flow diagram, not an architectural latency measurement. The Methods describe the final scalar through W, while the caption labels an MLP; both describe a learned scoring stage, but the exact layer specification cannot be resolved without Appendix B.

### Figure 4 — Components and comparative performance

The left panel is a checklist for language-pre-trained search, language-pre-trained choice, human demonstrations, and reward use. Rule has none of these learned components. IL without pre-trained choice retains learned search and demonstrations; IL without learned search retains pre-trained choice and demonstrations. IL uses both pre-trained components plus demonstrations. RL uses pre-trained search/choice and reward, without demonstrations; RL(RNN) is shown with reward; IL+RL uses all four. [B; p. 8]

Two bar plots show **Score** and **Success Rate (%)** on linear vertical scales. The score plot displays ticks spanning approximately 0–90; the success plot extends to 90 with readable upper ticks. Models occupy categorical horizontal positions matched to the checklist colors. Central values are printed above the bars and are reproduced in Section 9. The score labels for the closely placed IL/search-ablation bars must be matched by model/color rather than extracted-text order.

Horizontal reference lines show Human expert **82.1/59.6** and Human average **75.5/50.0**. Small error bars are visible for model results; neither their exact values nor whether they are standard deviations, standard errors, or another measure is stated in the supplied caption. The caption reports **3 trials**. No significance stars or p-values are shown. The strongest score and strongest success belong to different agents. The figure also contradicts the nearby claim that RL is worse than Rule on the reported central metrics.

## 11. Table-by-table interpretation

### Table 1 — Action and transition specification

Rows enumerate semantic actions, their arguments, and the next page type. Search[Query] moves Search to Results. Choose Back to search returns to Search, denoted by a wildcard source. Prev/Next page moves Results to Results; product title moves Results to Item; option moves Item to Item; Desc/Overview moves Item to Item-Detail; Previous returns Item-Detail to Item; Buy ends the episode. [A/B; p. 4]

The table defines control transitions, not model accuracy. The wildcard is broad table notation rather than evidence that every page in every external website offers that button. There are no units, missing result values, or statistical comparisons.

### Table 2 — Component scores and trajectory statistics

The left columns are overall, attribute, option, type, and price scores, on the displayed score scale. The right columns report average states visited, items checked, and searches, with maximum/minimum in parentheses. [A/B; p. 8]

| Model | All | Attribute | Option | Type | Price | States avg (max/min) | Items avg (max/min) | Searches avg (max/min) |
|---|---:|---:|---:|---:|---:|---|---|---|
| Rule | 45.6 | 66.6 | 0.0 | 80.5 | 86.0 | 3.0 (3/3) | 1.0 (1/1) | 1.0 (1/1) |
| IL | 59.9 | 69.3 | 45.2 | 86.4 | 84.0 | 9.4 (90/3) | 1.6 (11/1) | 1.3 (17/1) |
| IL+RL | 62.4 | 74.0 | 38.9 | 89.7 | 88.7 | 4.5 (5/1) | 1.0 (1/1) | 1.0 (1/1) |
| Human expert | 82.1 | 81.8 | 73.9 | 94.4 | 97.7 | 11.3 (114/4) | 1.9 (16/1) | 1.4 (16/1) |

Experts lead every score component. IL leads agents on options, whereas IL+RL leads agents on attributes, type, price, and overall score. Rule's zero option score follows its policy of selecting no options. RL's averages indicate less exploration than IL. Maximum/minimum are observed extrema, not uncertainty intervals. The prose elsewhere reports **4.8** rather than **4.5** for IL+RL trajectory length; this remains unresolved.

Overall reward is not a simple unweighted average of these component columns. Eq. (1) uses per-instruction counts and a multiplicative type factor. Consequently, averaging the four displayed components does not reconstruct the overall column.

### Table 3 — Two qualitative trajectories

For white blackout shades of **66 inches width and 66 inches height**, the human succeeds with reward **1.0**, length **8**, revising the query to **66 x 66 blackout shades**, then selecting size and color/style options. The IL+RL agent generates a query containing **65 inches** for width, selects a different item, and buys without shown option selection, yielding **0.2**, length **3**. The width change is directly observable in this example, not evidence of its frequency across the dataset. [A/B; p. 9]

For a **gingko light, 20×20-inch, hand-painted pillow cover**, the human succeeds with reward **1.0**, length **17**, checks descriptions/overview, revisits a product, and selects **20×20** and **nudes (gingko light)**. The agent achieves **0.25**, length **3**. The human listing omits some actions and product names are truncated; the caption discloses both. Red marks options; blue marks attributes. These selected examples illustrate semantic matching, reformulation, and memory demands, without establishing causal or population-level rates.

### Table 4 — Choice-oracle performance by query source

| Query source | Score | Success Rate |
|---|---:|---:|
| Instruction text | 79.7 | 52.6% |
| IL BART | 83.0 | 57.6% |
| Human expert first query | 82.1 | 57.9% |
| Human expert last query | 84.4 | 61.0% |

The comparison holds the privileged choice procedure fixed and varies the query source on **500 test instructions**. Last human query has the highest displayed values; instruction text the lowest. Human first query has slightly higher success but lower score than IL BART. There are no uncertainty intervals or significance tests. These are oracle-assisted performances, not the ordinary performance of the named human/model query sources. In **74.8%** of human trajectories there is only one query, so first and last query conditions coincide for most episodes. [A/B; p. 9]

### Table 5 — Real-site transfer

All score-component columns are in Score units; SR is percent. The evaluation uses **100 sampled test instructions**, simulation-trained models without fine-tuning, and manual episode scoring. [A/B; p. 10]

| Website | Actor | Score | SR % | Attribute | Option | Type | Price |
|---|---|---:|---:|---:|---:|---:|---:|
| Amazon | Rule | 45.8 | 19 | 45.6 | 38.0 | 66.2 | 90.0 |
| Amazon | IL | 61.5 | 27 | 60.7 | 53.7 | 85.6 | 96.0 |
| Amazon | IL+RL | 65.9 | 25 | 71.6 | 47.0 | 87.8 | 100.0 |
| Amazon | Human | 88.2 | 65 | 86.2 | 76.3 | 99.0 | 100.0 |
| eBay | Rule | 31.7 | 7 | 62.3 | 25.9 | 49.0 | 67.0 |
| eBay | IL | 58.2 | 21 | 60.2 | 52.3 | 85.1 | 96.9 |
| eBay | IL+RL | 62.3 | 21 | 69.1 | 39.5 | 91.7 | 97.0 |
| eBay | Human | 79.7 | 40 | 80.3 | 70.1 | 99.5 | 100.0 |

Humans lead overall scores and success on both websites. IL leads agents on options on both. Amazon IL+RL ties human price score at **100.0**; eBay IL and IL+RL tie success at **21%**. The nearby prose gives Amazon human score **88.0**, differing from the table's **88.2**. No source resolves the discrepancy. The authors mention two minor coding additions, but do not describe them sufficiently in the supplied main text to reproduce transfer.

## 12. Diagram / architecture interpretation

Two linked architectures matter: the environment's action loop and the choice model's internal representation flow.

**Environment loop:** instruction plus current webpage → observation → available semantic actions → selected search or choose action → deterministic simulated transition → next observation. Selecting Buy ends the episode and computes reward from the selected product and instruction. Search results constrain which products are immediately available; returning to Search enables another query; item-detail pages expose additional information; option selections change the item configuration. Figures 1 and Table 1 together specify these pathways. [A/B; pp. 2, 4–5]

**Choice-model flow:** product images → ResNet features → learned dimensional transformation; page/instruction text → BERT token representations; candidate action text → shared BERT representations. The image and observation text representations are concatenated, then fused with action representations through attention. Mean pooling and a learned output stage produce S(o,a), followed by softmax over available candidates. This is repeated for each action candidate. The selected action influences the next observed webpage. [A/B; pp. 6–7]

**Search-model flow:** instruction → BART → candidate query strings. IL randomly selects among five; IL+RL uses ten generated candidates and learns a choice. BART's search generation excludes prior search/item context in the described formulation. The search-generation model and choice-scoring model therefore perform different jobs. [A; pp. 6–7]

**Analyst security relevance:** the architecture converts page content and action labels into scores for executable choices. That is a concrete content-to-action pathway, suitable for identifying where a future security experiment could introduce controlled perturbations. The supplied architecture does not show that text can override system instructions, nor that the agent is a contemporary chat-style LLM. No prompt-injection mechanism is demonstrated. [D]

## 13. Equations and mathematical concepts

### Process formulation — p. 4, §3.1

The process is `(S, A, T, R, U, O)`, with `T: S×A → S` and `R: S×A → [0,1]`. S denotes webpages; A denotes actions; T maps current state/action to next state; R maps an ending state/action to reward; U denotes instructions; O denotes observations. The deterministic transition assumption concerns the simulation. Partial observation means the agent acts from an observation rather than receiving every internal quantity, including hidden reward attributes.

The observation mapping is printed as `S×I → O`, although I is also introduced as a set of product images and the surrounding prose says state and instruction. The notation therefore contains an unresolved symbol inconsistency. It should not be silently rewritten as an author-corrected `S×U → O`.

### Equation (1) — reward, p. 5

`r = r_type × (|U_att ∩ Y_att| + |U_opt ∩ Y_opt| + 1[y_price ≤ u_price]) / (|U_att| + |U_opt| + 1)`.

This scalar reward counts satisfied requested attributes and options, adds one if the price constraint is satisfied, divides by the number of requested criteria plus the price criterion, then multiplies by a type-matching factor. U_att and U_opt are instruction requirements; Y_att and Y_opt are the chosen product's corresponding attributes and configured options. Vertical bars denote set size, intersection denotes shared requirements, and the indicator is 1 when its condition holds and 0 otherwise. The instruction attribute set is nonempty, so the stated denominator is positive.

`r_type = TextMatch(y-bar, y*-bar)` compares chosen and target product text using heuristics. Its role is to penalize products of the wrong type even when some attributes/options overlap. The authors illustrate this with butter and plant-based meat sharing labels. The exact TextMatch formula is in absent Appendix A.5. Reward is used as training feedback and defines both evaluation metrics. [A]

### Equation (2) — search imitation loss, p. 6

`L_search = E_(u,a)~D [−log π_phi(a|u)]`.

D contains instruction/search pairs; u is the instruction; a is the demonstrated search action; phi denotes BART parameters. The loss is the expected negative log-probability of human queries conditioned on instructions. Minimizing it encourages demonstrated queries. It does not explicitly optimize reward, remember previous products, or evaluate security behavior. The extracted parameter character is damaged in places, but the rendered equation supports the parameter reading; the substantive conditional objective is clear.

### Equation (3) — choice imitation loss, p. 7

`L_choose = E_(o,A(o),a*)~D' [−log π_theta(a*|o,A(o))]`.

D' contains observations, available choices, and the human-clicked action a*. Theta denotes choice-model parameters. This objective increases probability on demonstrated clicks among currently available choices. A(o) is the available-action set and o is the current observation. The output is a training loss, not a direct probability of successful shopping. [A]

### Equation (4) — action policy, p. 7

The displayed relationship has the form `π_theta(a|o,A(o)) ∼ exp(W^T mean[cross-attn(BERT(o;theta), BERT(a;theta))])`.

The accompanying prose states that this is a **softmax distribution over action scores**. Each action gets a score after contextual encoding, cross-attention, pooling, and learned projection W. Exponentiation converts scores to positive weights; softmax normalizes across available actions. The printed relation uses a tilde-like symbol rather than an explicit normalized fraction. The denominator is not displayed in Eq. (4), so the normalized interpretation is grounded in the prose. Image representations are incorporated into observations as described separately in Methods. [A]

### Equation (5) — policy-gradient loss, p. 7

`L_PG = E_pi [−(R_t − V(o_t)) log π(a_t|o_t,A(o_t))]`.

R_t is return-to-go, V(o_t) is an estimated baseline value, and their difference weights the selected action's log-probability. Actions whose returns exceed the estimated baseline receive a different learning signal from actions whose returns fall below it. The expectation is over interactions generated by the policy. This connects episode rewards to model updates. [A]

### Unnumbered RL formulas — p. 7

Return is written `R_t = E_pi[r_t + gamma R_(t+1)]`; gamma is a discount factor, but its value is not supplied. The baseline is `V(o) = W_v^T BERT(o;theta)`, sharing BERT weights with the policy. The exact pooling needed to turn a token representation into this scalar is not fully specified by this shorthand. Value learning uses `(R_t − V(o_t))²`. The total objective is `L_RL = L_PG + L_value + L_entropy`.

The entropy expression is written as a sum over actions of probability times log-probability, but the summand retains `a_t` instead of consistently using the action being summed over. Thus, the stated purpose—preventing premature convergence—is clear, while the exact displayed indexing is inconsistent. No loss coefficients are supplied. This report does not silently repair the formula or infer implementation behavior.

### Metric/component formulas — pp. 5, 8

Task Score is `100×average(r)`; Success Rate is the fraction with r=1. Attribute and option component fractions are `|U_att∩Y_att|/|U_att|` and `|U_opt∩Y_opt|/|U_opt|`; price is the indicator; type is r_type. Since U_opt may be empty under the task definition, the displayed option fraction requires an empty-set handling convention that is not specified in the supplied main text. These component metrics support Table 2; they are not interchangeable with the total reward.

## 14. Interpretation and discussion

The benchmark objective is supported by an implemented environment, large product corpus, crowdsourced instructions, semantic actions, and automatic reward. The modeling objective is supported by comparative agent results. The diagnostic objective receives evidence from pre-training ablations, component scores, trajectories, and privileged oracle evaluations. The transfer objective receives evidence from two real-site tests on 100 sampled instructions. None of these answers the separate question of adversarial vulnerability relative to standalone LLMs. [A/D]

The results suggest that full task success is especially sensitive to correct product and option choices. A model can obtain moderate partial reward while failing the exact r=1 threshold. This explains why optimizing average reward need not improve full-success rate: IL+RL has higher overall score and lower option score than IL, with a small decline in success. The authors associate this with less exploration after RL fine-tuning. Their evidence supports a behavioral association; it is not a controlled causal proof that shorter trajectories alone cause the option decline. [A for interpretation; D for causal qualification; pp. 8–9]

Important consistency checks remain unresolved:

- **Best model depends on metric:** the abstract rounds best success to 29%, and the introduction emphasizes IL+RL's 28.7%; §5.2 calls 29.1% the best model success. Fig. 4 clarifies that IL is best on success and IL+RL on score. These should be reported separately.
- **RL versus Rule:** p. 8 says direct RL performance is worse than Rule, yet Fig. 4 shows RL **52.5/11.2** versus Rule **45.6/9.6**, higher on both plotted central values. The prose cannot be supported by those values as written.
- **Trajectory length:** Table 2 and the oracle paragraph use **4.5** for IL+RL, while the RL-effects paragraph gives **4.8**. No supplied appendix resolves it.
- **Amazon human score:** Table 5 gives **88.2**; prose gives **88.0**.
- **Demonstrations:** abstract 'over 1,600' differs from the **1,566** derived from explicitly enumerated collections.
- **Notation:** the observation mapping and entropy summation have symbol/index inconsistencies; implementation cannot be inferred from them.

The figures, tables, and main text otherwise consistently show a substantial human–agent gap, difficulty with options, and positive transfer relative to the rule baseline. Words such as 'significant' and 'large margin' should be read as the authors' qualitative descriptions; the supplied material does not provide formal significance tests.

## 15. Contributions and novelty

**Benchmark/system contribution:** WebShop integrates realistic product text/images, several page types, semantic search/choose actions, and a modular environment separating website transitions from instructions and reward. Its dual observation modes support browser interaction and model-oriented training. [A; pp. 2–5]

**Dataset contribution:** a product corpus exceeding one million items, 12,087 natural-language instructions, mined/annotated attributes, and human demonstrations. These quantities establish the scale reported by the authors, while absent appendices limit assessment of data quality and collection details. [A; p. 5]

**Methodological contribution:** a modular search-and-choice pipeline combining BART, BERT, ResNet image features, attention fusion, imitation learning, and online RL. The work does not claim to introduce BART, BERT, ResNet, BM25, or policy gradients themselves. [A; pp. 6–7]

**Empirical contribution:** benchmark comparisons, component ablations, aggregate and qualitative human–agent diagnostics, a privileged choice-oracle analysis, and zero-shot transfer to Amazon/eBay. These demonstrate both capability and remaining difficulty under specific conditions. [A; pp. 7–10]

**Security-research contribution:** none is directly claimed or demonstrated. **Analyst inference:** the paper provides a concrete reference architecture and task environment for discussing observation-to-action boundaries. It can inform the design of a security analysis, but cannot supply a numerical vulnerability comparison, an attack taxonomy, or a verified defense. [D]

## 16. Limitations

### Authors' stated limitations and acknowledged shortcomings

The authors emphasize that agents remain substantially below human experts. They identify difficult query generation/reformulation, option matching in noisy language, strategic exploration, and long-term memory. Two qualitative examples show backtracking and returning to products that the model does not reproduce. They acknowledge that simple history augmentation reduces score rather than resolving memory difficulties. [A; pp. 3, 5–9]

They state that some crowdworkers lack patience and consistency, leading to lower human scores, although the human–model gap remains. They identify i.i.d. splitting as the current setup and propose harder generalization splits, such as splitting by product category. They note that a search oracle is harder to design because query space is infinite and that querying the underlying target name would make choice nearly trivial. [A; pp. 3, 7, 9]

The search model deliberately ignores prior searches and visited items, and RL freezes generation to avoid potential language drift. RL fine-tuning reduces exploration and option score. These are explicitly described model boundaries or outcomes rather than a formal limitations section. [A; pp. 6–9]

### Additional evidence-based analyst observations

[D] The benchmark covers shopping within five product categories; evidence does not establish arbitrary web-task generalization. Product-conditioned instructions and automatically extracted attributes constrain what 'success' measures. A correct benchmark score is not independently verified user satisfaction, product quality, or transaction safety.

[D] Human/model observation modes differ. The choice oracle has privileged information and much larger interaction effort. Real-site scoring is manual rather than the simulation's automated computation. These differences matter when interpreting comparisons.

[D] Absent appendices prevent full assessment of hyperparameters, annotation quality, reward heuristics, code adapters, and extra experiments. Figure 4's error bars lack a supplied definition. Several numeric inconsistencies remain. No adversarial manipulation, security outcome, or standalone-LLM control is evaluated; benign task failures cannot be converted into attack success rates.

## 17. Threats to validity

The following validity categories are **analyst observations**, not a formal taxonomy used by the authors.

**Internal validity:** ablations support component importance within the evaluated pipeline, but changing initialization, supervision, and architecture can alter learning dynamics simultaneously. Oracle gains combine exhaustive exploration and hidden information. The evidence does not isolate every mechanism behind those gains. Human expertise is selected from the same recruited worker pool rather than treated as a randomized intervention. [D; pp. 5–9]

**Construct validity:** task reward operationalizes instruction fulfillment using hidden attribute/option matching, a price check, and heuristic product-type matching. It permits alternative satisfactory products, which avoids requiring exact target identity. However, missing TextMatch details and empty-option handling limit assessment of how faithfully the score captures user intent. Security vulnerability is an entirely different construct and is not measured. [D; pp. 4–5, 8]

**External/generalization validity:** the split is i.i.d.; category-held-out testing is future work. Transfer evidence covers Amazon and eBay with 100 sampled instructions, not an exhaustive cross-domain web evaluation. The simulation uses deterministic retrieval/transitions; the authors themselves note real-site domain shifts in products and search dynamics. [A/D; pp. 7, 10]

**Statistical conclusion validity:** three trials are reported for model plots, but error definitions, confidence intervals, tests, and exact run-level results are absent. Small differences such as 29.1% versus 28.7% cannot be declared statistically reliable from the supplied information. The 100-instruction transfer results also have no provided uncertainty estimates. [D]

**Ecological validity:** real products and real-site tests increase realism, but simplified observations, constrained action types, and simulated episode termination limit correspondence to every aspect of human shopping. Human timing and model timing are reported, yet a full accounting of equivalent workloads is unavailable. [D]

**Reproducibility:** the main text specifies major components and dataset counts, and advertises a project site with code/data/demos. That site was not accessed. Missing appendices, hyperparameters, seeds, reward details, adapter descriptions, and unresolved discrepancies prevent full reproduction assessment from the supplied artifact. [A/D]

## 18. Future work and open questions

### A. Explicit author proposals

The authors propose stronger search generation and query reformulation, explicit memory modules, better noisy-text handling, improved exploration, and combinations of these mechanisms. They suggest multimodal, web-hypertext, or instruction-to-action pre-training. They propose more challenging generalization splits and expanding the modular environment to additional tasks/domains. Intrinsic bonuses are mentioned as a possible way to balance exploration and exploitation. A stronger RL architecture with better language/task priors is hypothesized to improve stability and performance. [A; pp. 3, 6–10]

### B. Additional open questions from the supplied evidence

[D] Does a better memory mechanism improve options without reducing other components? Can reward design improve complete success rather than only average partial credit? How do results change under product/category separation, revised instructions, or changed retrieval? Which part of oracle gains comes from additional exploration versus privileged matching? How consistent are manual transfer scores across raters? These questions follow from the evaluation boundaries but are not results of the paper.

[D, security relevance] If a future researcher studies vulnerability, they would need controlled environmental manipulations, explicit attacker capabilities, security metrics, and a matched standalone-model comparison. One could study product text, action labels, retrieval, observation conversion, and executable actions as distinct surfaces because the architecture exposes them. WebShop supplies no measured answer about which is exploitable or whether adding web interaction increases adversarial success. Security research must also distinguish ordinary option mistakes, induced task failures, unauthorized actions, and actual financial consequences.

## 19. Terminology and notation glossary

| Term/symbol | Meaning in this paper |
|---|---|
| WebShop | Simulated e-commerce benchmark based on real product information |
| Grounding | Connecting written requirements to environment objects and actions |
| NLP | Natural language processing |
| IL | Imitation learning from human queries and choices |
| RL | Reinforcement learning through reward-bearing interactions |
| IL+RL | Imitation-trained choice model subsequently fine-tuned with RL |
| IR | Information retrieval; the lexical product-search baseline |
| POMDP | Partially observable Markov decision process |
| HTML mode | Browser-oriented webpage representation used for human interactions |
| Simple mode | Metadata-reduced observation representation used for evaluated models |
| DOM | Document Object Model, discussed for previous web benchmarks |
| AMT | Amazon Mechanical Turk, used to recruit instruction writers/workers |
| BART | Named pre-trained sequence-to-sequence model used for search generation |
| BERT | Bidirectional Encoder Representations from Transformers; text encoder |
| ResNet-50 | Named pre-trained residual-network image encoder |
| RNN | Recurrent neural network, used in an RL comparison |
| MLP | Multilayer perceptron, the diagram's learned output-scoring stage |
| LP | Language pre-training, as used in Figure 4 |
| BM25 | Named sparse retrieval method; formula not supplied |
| TF-IDF | Term frequency–inverse document frequency, used to mine bigrams |
| Beam search | Procedure producing several candidate queries; detailed settings absent |
| Cross-attention | Operation combining observation and action representations |
| Mean pooling | Averaging representations into one vector |
| Logit S(o,a) | Scalar score assigned to a candidate action before softmax |
| Softmax/policy pi | Normalized probability distribution over candidate actions |
| Episode | One attempt ending at Buy and reward computation |
| s, S | State and state space; a state represents a webpage |
| a, A(o) | Action and actions available in an observation |
| T | Deterministic simulated state transition function; also final time subscript context |
| R, r | Reward function and realized reward |
| u, U | Instruction and instruction space |
| o, O | Observation and observation space |
| y, y* | Chosen product and product from which an instruction was generated |
| y-bar | Combined product title, description, and overview text |
| Y_att, U_att | Product attributes and requested attributes |
| Y_opt, U_opt | Product/configured options and requested option field-value pairs |
| y_price, u_price | Product price and instruction price limit |
| I | Product image set; observation-map reuse of I is unresolved |
| r_type | Heuristic type-match multiplier |
| phi, theta | Search-model and choice-model parameters |
| V(o), R_t | Learned value baseline and return-to-go |
| gamma | Discount factor, value not supplied |
| SR | Success Rate: share of episodes with reward exactly 1 |
| Choice oracle | Privileged exhaustive product/option choice procedure |
| Sim-to-real | Applying a simulation-trained model to real websites |
| i.i.d. | Independent and identically distributed split, authors' description |

## 20. Key numerical results

This compact reference complements the full tables above. Units are retained where stated; uncertain units are disclosed. Status refers to the evidence supplying the value, even where a table is also author-authored.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Scraped products | 1,181,436 | products | Five Amazon categories, 113 query names | Author-reported | p. 5, §3.2 |
| Unique product options | 842,849 | options | Product corpus | Author-reported | p. 5 |
| Product-text average length | 262.9 | unit not explicitly stated | Titles and details | Author-reported | p. 5 |
| Product vocabulary | 224,041 | vocabulary entries | Word frequency higher than 10 | Author-reported | p. 5 |
| Attribute pool | 670 | attributes | Top 200 bigrams/category reviewed | Author-reported | p. 5 |
| Instructions | 12,087 | instructions | Crowdsourced | Author-reported | pp. 5, 7 |
| Instruction vocabulary/length | 9,036 / 15.9 | words / words per instruction | Overall corpus | Author-reported | p. 5 |
| Train/development/test | 10,587 / 1,000 / 500 | instructions | i.i.d. split | Author-reported | p. 7 |
| Recruited/selected expert workers | 13 / 7 | workers | Qualification and performance selection | Author-reported | p. 5 |
| Training/development demonstrations | 1,012 / 54 | trajectories | IL training/tuning | Author-reported | p. 7 |
| Enumerated demonstration total | 1,566 | trajectories | 1,012+54+500 | Analyst-derived | p. 7 |
| Abstract demonstrations | over 1,600 | demonstrations | Not reconciled with enumerated total | Author-reported | p. 1 |
| Search/choice training samples | 1,421 / 9,558 | pairs / samples | Human trajectory extraction | Author-reported | p. 6 |
| BERT depth | 12 | layers | Choice encoding | Author-reported | p. 6 |
| Image feature transformation | 512 → 768 | dimensions | ResNet feature to observation embedding | Author-reported | p. 7 |
| Search candidate counts | 5 / 10 | queries | IL sampling / RL candidate set | Author-reported | p. 7 |
| Model evaluation repetitions | 3 | trials | Figure 4 test comparison | Author-reported | p. 8, caption |
| Rule score/SR | 45.6 / 9.6 | score / % | Simulated test split | Visually readable | p. 8, Fig. 4 |
| IL score/SR | 59.9 / 29.1 | score / % | Simulated test split | Visually readable | p. 8 |
| IL+RL score/SR | 62.4 / 28.7 | score / % | Simulated test split | Visually readable | p. 8 |
| Human expert score/SR | 82.1 / 59.6 | score / % | Simulated test comparison | Visually readable | p. 8 |
| Human average score/SR | 75.5 / 50.0 | score / % | Simulated test comparison | Visually readable | p. 8 |
| History-augmented score | 57.3 | score | One prior observation, five actions | Author-reported | p. 8 |
| Outside top-50 target results | 56.1 | % | Instruction used as query | Visually readable | p. 4, Fig. 2 |
| Instruction-query oracle SR | 52.6 | % | 500 tests; exhaustive hidden-information choices | Visually readable | p. 9, T4 |
| BART-query oracle SR | 57.6 | % | Same oracle conditions | Visually readable | p. 9, T4 |
| Final-human-query oracle score/SR | 84.4 / 61.0 | score / % | Same oracle conditions | Visually readable | p. 9, T4 |
| Single-query human trajectories | 74.8 | % | First/last oracle-query overlap | Author-reported | p. 9, footnote |
| Transfer sample | 100 | test instructions | Amazon/eBay, no fine-tuning | Author-reported | p. 10 |
| Amazon IL+RL score/SR | 65.9 / 25 | score / % | Manual scoring, real website | Visually readable | p. 10, T5 |
| eBay IL+RL score/SR | 62.3 / 21 | score / % | Manual scoring, real website | Visually readable | p. 10, T5 |
| Amazon human score discrepancy | 88.2 vs 88.0 | score | Table versus prose | Author-reported, conflicting | p. 10 |
| Interaction time | 815 vs <8 | seconds/episode | Humans versus IL/IL+RL on Amazon in reported comparison | Author-reported | p. 10 |
| IL+RL minus Rule success | 19.1 | percentage points | 28.7−9.6, simulated tests | Analyst-derived | p. 8 |

No approximate graph-derived performance values are used. Exact central values are labeled in the plots. The runtime comparison lacks supplied variance and full timing methodology, so it is not converted into an exact speedup. The 815-second figure is reported alongside Amazon/eBay human results; the model comparator is explicitly on Amazon, and no separate eBay model timing should be inferred.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| WebShop combines scale with interactive shopping | 1,181,436 products; 12,087 instructions; four page types | F1, T1, environment construction | pp. 2, 4–5 | HIGH for reported construction; full collection details absent |
| Semantic actions connect language to environment behavior | Search queries and text-button choices; Buy terminates episode | F1, T1 | pp. 2, 4 | HIGH; not proof of real monetary transactions |
| Agents learn distinct search and choice functions | BART query objective; BERT/ResNet attention choice objective | F3, E2–E4 | pp. 6–7 | HIGH for described pipeline; complete hyperparameters absent |
| IL substantially improves over the rule baseline | 59.9/29.1 versus 45.6/9.6 | F4, X1 | pp. 7–8 | HIGH for central values; statistical test absent |
| RL fine-tuning creates a score/success tradeoff | Score 59.9→62.4; success 29.1→28.7; options 45.2→38.9 | F4, T2, X5 | pp. 8–9 | HIGH for values; causal explanation qualified |
| Pre-trained choice representation matters in this pipeline | IL without LP Choice 45.8/10.6 versus IL 59.9/29.1 | F4, X2 | pp. 7–8 | HIGH for reported comparison; bounded to this training setup |
| Correct choice is a major bottleneck | Oracle BART-query success 57.6 versus IL 29.1 | T4, X7 | p. 9 | HIGH diagnostic evidence; oracle has hidden data and >100 steps |
| Humans exhibit more exploration and stronger matching | T2 component/count advantages; two successful example trajectories | T2–T3, X5–X6 | pp. 8–9 | HIGH aggregate evidence; examples are selected and compressed |
| Some shopping capability transfers without fine-tuning | Amazon/eBay IL+RL 65.9/25 and 62.3/21 | T5, X8 | p. 10 | HIGH reported outcomes; 100 tasks, manual scoring, missing adapters |
| Results do not directly establish relative security vulnerability | Shopping metrics and transfer setup; no standalone-model attack comparison | Scope of X1–X8 | pp. 4–10 | HIGH for supplied-scope boundary; absent supplements cannot be assessed |
| Architecture is relevant to identifying security-study surfaces | Page/product/action text and images enter action scoring | F1, F3, T1 | pp. 2, 4, 6–7 | MEDIUM analyst inference; no demonstrated exploit |
| Several source inconsistencies limit exact reconciliation | Demonstration count, RL/Rule claim, trajectory length, human Amazon score | F4, T2, T5, prose | pp. 1, 7–10 | HIGH for discrepancy visibility; resolution UNKNOWN |

Security relevance is narrower than security evidence. The architecture supports saying that an agent consumes environmental content and performs actions; it does not support saying that WebShop proves web agents are more vulnerable, that all webpage text is attacker-controlled, or that ordinary task errors are attacks.

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking a computer to find a white curtain of a certain size and buy the correct version. The computer must use the search box, read results, check details, choose the right size and color, and decide when it has found a match. A search result that sounds close can still be wrong. WebShop is a practice shopping website that lets researchers test those decisions many times and automatically score how well they match the request.

The researchers taught one model to write searches and another to imitate people's clicks. They then used rewards to improve the clicking model. The agents became better than a simple strategy that searches the whole request and buys the first result. But the best agents fully succeeded on only about 29% of the test requests, compared with about 60% for selected human experts. The reward-trained model earned more partial credit, but it did not have the highest rate of completely correct purchases.

People often did better because they changed searches, checked several products, remembered what they had seen, and selected the right options. An unusually powerful test procedure that could inspect hidden scoring information and try every option performed much better. That helps show where the agents struggle, but it is not a realistic shopper operating under the same limits.

For the security question, the useful point is that the agent reads outside information and uses it to decide actions. Those connections could be studied for security problems. This paper does not test malicious pages or compare attack vulnerability with a language model that only writes answers. It tells us how this shopping agent works and where it makes mistakes; a separate security experiment would be needed to show whether an attacker can exploit those pathways.

## Completeness Audit

Coverage is judged against the supplied inventory, not response length. 'Fully represented' means the substantive supplied content is accounted for at this report's explanatory level; it does not mean every sentence is reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, equal-contribution note | Yes, text+visual | Yes | Fully represented | Stage 0 |
| Abstract ABS | Yes, text+visual | Yes | Fully represented | Headline results and rounded/count discrepancies retained |
| §1 Introduction S1 | Yes, text+visual | Yes | Represented in compressed form | Motivation, gap, contributions, project-site note |
| §2 Related Work S2 | Yes, text+visual | Yes | Represented in compressed form | All three categories; individual cited studies grouped |
| §3 Environment S3 | Yes, text+visual | Yes | Fully represented | Modular design and task scope |
| §3.1 SS3.1 | Yes, text+visual | Yes | Fully represented | States/actions/observations/reward/metrics; notation caveats |
| §3.2 SS3.2 | Yes, text+visual | Yes | Fully represented | Collection, search, attributes, instructions, demonstrations |
| §3.3 SS3.3 | Yes, text+visual | Yes | Fully represented | Four research challenges and combinations |
| §4 Methods S4 | Yes, text+visual | Yes | Fully represented | Overview and appendix boundary |
| §4.1 SS4.1 | Yes, text+visual | Yes | Fully represented | Rule baseline and rationale |
| §4.2 SS4.2 | Yes, text+visual | Yes | Fully represented | Search, choice, image handling, inference |
| §4.3 SS4.3 | Yes, text+visual | Yes | Fully represented | Frozen generation, policy/value/entropy training |
| §5 Experiments S5 | Yes, text+visual | Yes | Fully represented | Distinct analysis register |
| §5.1 SS5.1 | Yes, text+visual | Yes | Fully represented | Splits, training/tuning/test demonstrations |
| §5.2 SS5.2 | Yes, text+visual | Yes | Fully represented | Performance and IL/RL/history ablations |
| §5.3 SS5.3 | Yes, text+visual | Yes | Fully represented | Components, trajectories, oracle, caveats |
| §5.4 SS5.4 | Yes, text+visual | Yes | Fully represented | Transfer, manual scoring, timing, discrepancies |
| §6 Discussion S6 | Yes, text+visual | Yes | Fully represented | Future pre-training, search, memory, expansion |
| Explicit research questions | Checked | Yes | No formal questions supplied | Objectives separately reconstructed |
| Hypotheses | Checked | Yes | Fully represented | Better-prior/architecture RL proposal, not verified |
| X1 main performance | Yes | Yes | Fully represented | All model central values and humans |
| X2 IL ablations | Yes | Yes | Fully represented | Search and choice pre-training |
| X3 RL ablations | Yes | Yes | Fully represented | Direct RL, recurrent comparison, contradiction |
| X4 history augmentation | Yes | Yes | Fully represented | One observation/five actions, 57.3 score |
| X5 components/trajectory analysis | Yes | Yes | Fully represented | Full T2 and 4.5/4.8 discrepancy |
| X6 qualitative trajectories | Yes | Yes | Represented in compressed form | Conditions, rewards, lengths, selected action differences |
| X7 choice oracle | Yes | Yes | Fully represented | All four query sources and privileged conditions |
| X8 transfer | Yes | Yes | Fully represented | All T5 values, timing and absent adapter details |
| F1 panels A/B/C | Yes, visual+text | Yes | Fully represented | Screenshots, sequence, modes, notation |
| F2 retrieval pie | Yes, visual+text | Yes | Fully represented | All slices and rank conditions |
| F3 architecture | Yes, visual+text | Yes | Fully represented | Streams, shared weights, fusion, pooling, score |
| F4 checklist and two plots | Yes, visual+text | Yes | Fully represented | Values, human lines, axes, undefined error bars |
| T1 actions | Yes, visual+text | Yes | Fully represented | All transition rows |
| T2 score/count breakdown | Yes, visual+text | Yes | Fully represented | All numerical cells |
| T3 example trajectories | Yes, visual+text | Yes | Represented in compressed form | Original already omits actions/truncates names |
| T4 oracle | Yes, visual+text | Yes | Fully represented | All cells and first/last-query note |
| T5 transfer | Yes, visual+text | Yes | Fully represented | All numerical cells |
| E1 reward | Yes, visual+text | Yes | Fully represented | Exact type heuristic inaccessible |
| E2 search loss | Yes, visual+text | Yes | Fully represented | Symbols and role |
| E3 choice loss | Yes, visual+text | Yes | Fully represented | Symbols and role |
| E4 policy | Yes, visual+text | Yes | Fully represented | Softmax prose and displayed relation distinguished |
| E5 policy gradient | Yes, visual+text | Yes | Fully represented | Return and value roles |
| Unnumbered process/metric/RL formulas | Yes, visual+text | Yes | Fully represented | Symbol/index and empty-option issues disclosed |
| Algorithms/pseudocode | Checked | Yes | None supplied as numbered objects | Procedural descriptions represented |
| Theorems/lemmas/propositions | Checked | Yes | None supplied | Not a theorem-based paper |
| Major contributions | Yes | Yes | Fully represented | Benchmark, data, system, methods, empirical results |
| Author-acknowledged shortcomings | Yes | Yes | Fully represented | Agent gap, worker consistency, search/memory/options |
| Equal-contribution/project-site footnote | Yes | Yes | Represented in compressed form | Site not accessed |
| Human-consistency footnote | Yes | Yes | Fully represented | p. 3 |
| Search-oracle footnote | Yes | Yes | Fully represented | Infinite query space and trivial target-name query |
| Single-query footnote | Yes | Yes | Fully represented | 74.8% |
| Acknowledgements ACK | Yes, text+visual | Partly | Inspected, compressed as secondary | Credits; NSF Grant 2107048 and funding disclaimer are non-result context |
| References REF [1]–[59] | Yes, text only | Partly | Represented in compressed form | Prior-work categories and named method sources; no external validation |
| Appendix A.1–A.6 | No | Absence represented | Missing from supplied material | Scraping, attributes, search, instructions, reward, demonstrations |
| Appendix B | No | Absence represented | Missing from supplied material | Additional model details |
| Appendix C | No | Absence represented | Missing from supplied material | Setup and additional ablations |
| Appendix D | No | Absence represented | Missing from supplied material | Transfer details and further analysis |
| Separate supplementary material/code/data/demos | No | Absence represented | Not supplied | Advertised availability does not establish inspection |

### Missing or inaccessible material

Appendices A–D, their referenced subsections, and advertised project artifacts were not supplied. Consequently, exact TextMatch, detailed annotation protocols, additional ablations, training hyperparameters, hardware, seeds, and real-site adaptation procedures cannot be fully assessed. There are no rendered images for pages 11–14, so reference-list coverage is text-only. No missing main-text page is demonstrated within pages 1–14, but the absent appendices preclude claiming complete publication coverage.

### Uncertain interpretations

The demonstration-count discrepancy, RL-versus-Rule prose contradiction, IL+RL 4.5/4.8 trajectory discrepancy, Amazon human 88.2/88.0 discrepancy, observation-map I notation, entropy indexing, empty-option component handling, final-scoring layer details, error-bar definition, and F2 diagnostic denominator remain unresolved. Product-text average length lacks an explicitly stated unit. The paper does not establish transaction execution or security vulnerability; confidence for an actual comparative vulnerability conclusion is UNKNOWN.

### Deliberately compressed material

Repeated motivation and future-work statements are consolidated. Related-work citations and all 59 bibliography entries are grouped by their role rather than individually summarized. Acknowledgement names and the funding disclaimer are secondary context. Table 3's repeated navigation steps and truncated item names are compressed while preserving conditions, outcomes, lengths, and relevant behaviors; the source itself already omits part of the second human trajectory. Decorative typography, page rules, and screenshot styling are not treated as scientific findings.

### Potential omissions

No known substantive object in the supplied main-text inventory is left unaccounted for: all sections/subsections, four figures and their substantive panels, five tables, five numbered equations, major unnumbered formulas, distinct analyses, contributions, and acknowledged shortcomings have representations above. This is a coverage statement about the supplied artifact, not a claim that absent appendices contain nothing important. Unavailable artifacts are explicitly excluded, and the security question remains an analyst-relevance framing rather than an author-tested conclusion.
