# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible page range | pp. 1–24 |
| Apparently missing pages | None |
| Native/extracted text | Available for all 24 pages |
| Visually rendered pages inspected | pp. 1, 2, 4–8, 13, 17–24 |
| Pages not visually rendered | pp. 3, 9–12, 14–16 |
| Visual content | Partial page rendering, but all candidate pages containing substantive figures or tables were rendered according to the mechanical record |
| Figures | Figures 1–11 are available visually on rendered pages and are readable at the level needed to interpret their structure; very small webpage text and Figure 6 site labels are not reliably legible |
| Tables | Tables 1–8 are available through extracted text; Tables 1–8 also appear on rendered pages and are substantially readable |
| Equations | No numbered display equations are present. Several objectives and metrics are described mathematically in prose. Superscripts/subscripts such as \(t-1\), top-\(k\), \(3\times10^{-5}\), and Recall@50 are readable but OCR-sensitive |
| Algorithms/pseudocode | No formal algorithm block; MindAct’s iterative selection procedure is described in prose and diagrams |
| Main-text sections | Abstract and §§1–7 present |
| Appendices | Appendix A (Overview), B (Data Collection Details), C (Experiment Details), and D (Additional Results) are present on pp. 16–24 |
| Supplementary material | The paper’s supplementary content is incorporated as Appendices A–D in the supplied 24 pages |
| Referenced artifacts not supplied | Dataset files, code repository, trained models, MHTML/Document Object Model snapshots, HTTP Archive files, trace files, complete network traffic, training/test data, annotation software, training document, video tutorial, and linked webpages were referenced but not supplied |
| OCR required | No; native extraction was available. OCR-like spacing errors occur in names such as “Mind2Web” and some table/model notation |
| Important limitations | Individual website names and exact bar heights in Figure 6 cannot all be read confidently. The external artifacts cannot be inspected, executed, or used to reproduce the results. Closed-document mode prevents external validation of novelty, citations, code, licenses, or live-site transfer claims. |

Evidence categories used below are:

- **[A] Author-reported:** stated in the supplied paper.
- **[B] Directly observable:** visible in a supplied figure or table.
- **[C] Analyst-derived:** calculated from supplied values, with operands shown.
- **[D] Analyst interpretation:** a clearly marked inference rather than an author claim.
- **[E] External information:** excluded.

# 1. Plain-Language Orientation

Mind2Web is both a dataset and a benchmark for teaching computer agents to operate real websites from ordinary language instructions. The motivating task is broader than locating text: an agent might need to choose dates, fill forms, follow links, select options, and navigate several pages to satisfy a high-level request.

The authors argue that previous web-agent datasets do not jointly provide three things: broad website and task diversity, real rather than simplified websites, and sophisticated multi-step interactions (§1, pp. 1–3). Mind2Web addresses this gap with 2,350 verified tasks from 137 real-world websites spanning 31 secondary domains within five top-level categories. Each task includes a high-level description, an annotated action sequence, and webpage snapshots or associated traces (§2, pp. 3–5).

The paper also introduces **MindAct**, an exploratory two-stage model:

1. A relatively small DeBERTa model ranks the many Document Object Model (DOM) elements on the current page.
2. A larger language model chooses among the most promising elements and predicts the action—such as clicking, typing, or selecting an option (§3, pp. 5–6).

The main empirical result is that this filtering-plus-multiple-choice formulation substantially outperforms direct element classification or direct target generation. The best fine-tuned model, MindAct with Flan-T5-XL, reaches step success rates of 52.0% on held-out tasks, 38.9% on unseen websites, and 39.6% on unseen domains (Table 2, p. 7). Whole-task success remains only 5.2%, 5.1%, and 2.9%, respectively, because every step must be correct for an entire task to count as successful.

The central contribution is therefore not a solved general web agent. It is a comparatively broad, realistic dataset and evaluation framework that exposes how difficult reliable multi-step web interaction remains.

# 2. Document Roadmap

The work is a combined **dataset paper, benchmark paper, and exploratory machine-learning study**, published in the NeurIPS 2023 Datasets and Benchmarks track (p. 1).

| Document component | Content and role |
|---|---|
| Abstract, p. 1 | Dataset motivation, three defining properties, MindAct overview, and high-level findings |
| §1 Introduction, pp. 1–3 | Defines a generalist web agent, shortcomings of prior settings, dataset contributions, and proposed research directions |
| §2 Mind2Web Dataset, pp. 3–5 | Task representation, website/task collection, annotation, verification, and comparison with prior datasets |
| §2.1, pp. 3–4 | Three components of each instance |
| §2.2, pp. 4–5 | Four-stage data-collection procedure |
| §2.3, p. 5 | Dataset comparison and resulting research challenges |
| §3 MindAct, pp. 5–6 | Two-stage modeling framework |
| §3.1, pp. 5–6 | Small-model candidate ranking |
| §3.2, p. 6 | Large-model multiple-choice action prediction |
| §4 Experiments, pp. 7–8 | Generalization splits, preprocessing, metrics, baselines, and results |
| §5 Related Work, pp. 8–9 | Web/mobile agents, LLMs, grounded language, and tool learning |
| §6 Limitations and Potential Societal Impact, pp. 9–10 | Representation, multimodality, dynamics, interaction, offline evaluation, and safety |
| §7 Conclusion, p. 10 | Contributions and future directions |
| References, pp. 11–15 | 45 cited works; bibliographic content is compressed below |
| Appendix A, p. 16 | Supplement overview and artifact links/licenses |
| Appendix B, pp. 17–20 | Crowdsourcing, proposal, demonstration, and verification details |
| Appendix C, pp. 20–21 | Evaluation heuristics and implementation |
| Appendix D, pp. 21–24 | Robustness runs, zero-shot results, subset analysis, and GPT prompts |

Inventory of substantive objects:

- **Figures:** F1–F11.
- **Tables:** T1–T8.
- **Formal numbered equations:** none.
- **Formal algorithms:** none; one prose-defined iterative candidate-selection procedure.
- **Distinct empirical analyses:** dataset comparison; candidate recall; main baseline/model comparison; three-level generalization; in-context learning; grouping robustness; zero-shot Flan-T5-XL; GPT-4 subset comparability.
- **Explicit question:** “How can we build a generalist agent for the web that, given any website, can follow language instructions and carry out the corresponding tasks?” (§1, p. 1).
- **Formal hypotheses:** none stated.

# 3. Background and Context

A **web agent** is a system that observes a webpage and chooses actions to achieve a goal. In this paper, the agent initially receives a natural-language task description. At step \(t\), it receives the current webpage and the preceding actions, then predicts the next target element and operation (§2.1, pp. 3–4).

A webpage is represented through **HTML** (HyperText Markup Language) and its **DOM** (Document Object Model), a tree of elements such as buttons, links, input boxes, and containers. A real page may contain more than one thousand elements, many irrelevant to the current step (§2.3, p. 5).

A **grounded** language model must connect words such as “departure date” or “checkout” to an executable element and action in the current environment. This is harder than producing a textual plan because the model must identify the exact page control.

A **large language model (LLM)** is used here either through fine-tuning—updating model parameters on Mind2Web—or **in-context learning**, where examples are placed in the prompt without parameter updates (§4.3, p. 8; Appendix C.2, pp. 20–21).

Three generalization conditions organize the benchmark (§4.1, p. 7):

- **Cross-Task:** test tasks come from websites seen during training.
- **Cross-Website:** test websites are unseen, but their broad domains are familiar.
- **Cross-Domain:** entire top-level domains and their websites are held out.

The action vocabulary in the released task definition is effectively:

- **Click**, also absorbing Hover and Press Enter;
- **Type**, with a value;
- **Select Option**, with a value.

The collection interface additionally provides Click (Fake) and Ignore, but these are annotation controls rather than distinct final-dataset operations (Appendix B.3, p. 19).

# 4. Research Problem and Gap

## Existing problem

[A] A useful generalist web agent should operate on websites it has never seen, cope with dynamic and noisy real webpages, and support diverse multi-step interactions (§1, pp. 1–2).

## Shortcomings attributed to previous approaches

According to the authors, prior datasets or systems commonly:

- operate over a limited, predefined set of sites;
- simplify the website environment;
- support only restricted task types;
- require low-level, step-by-step instructions;
- focus on mobile interfaces or simulated websites with fewer functions;
- emphasize short tool calls rather than long action sequences (§1, p. 2; §5, pp. 8–9).

Table 1 supports the narrower dataset-comparison claim: none of the listed alternatives combines 137 real websites, 31 secondary domains, high-level tasks, and an average of 1,135 elements per environment (p. 5).

## Research gap

[A] The claimed gap is the absence of a dataset supporting development and evaluation of agents that generalize across realistic websites and domains while executing high-level, open-ended tasks (§1, pp. 2–3).

## Motivation

Such agents could make complex web applications more accessible and permit language models to obtain information and take actions through websites rather than relying solely on retrieval or a separately defined application programming interface for every service (§1, p. 1). The authors also acknowledge serious deployment risks (§6, pp. 9–10).

## Scope

The benchmark covers real snapshots and action demonstrations, not unrestricted live-web execution. It predominantly includes English-language, U.S.-used websites and tasks proposed by qualified Mechanical Turk workers (§6, p. 9).

# 5. Research Questions / Objectives / Hypotheses

## Explicit research question

**RQ1:** How can a generalist agent be built that can accept a language instruction on any website and carry out the corresponding task? (§1, p. 1)

## Explicit and implicit objectives

- **O1:** Construct a diverse dataset of realistic, high-level tasks and action traces from real websites (§§1–2).
- **O2:** Enable evaluation of generalization to unseen tasks, websites, and domains (§1; §4.1).
- **O3:** Explore whether LLMs can serve as the action-prediction component of a general web agent (§1; §3).
- **O4:** Address the excessive length of raw webpage HTML by filtering candidate elements before invoking a larger model (§3).
- **O5:** Compare multiple-choice discrimination with direct classification and direct generation (§§3.2, 4.3).
- **O6:** Document limitations and provide artifacts for subsequent research (§§6–7; Appendix A).

## Hypotheses

The authors do not state formal hypotheses. Their design nevertheless tests two propositions without labeling them hypotheses:

- Filtering HTML with a small ranking model makes large-model prediction more practical and effective.
- Selecting among candidate elements as a multiple-choice problem performs better than directly generating a target representation.

These are objectives/propositions, not formal preregistered hypotheses.

# 6. Assumptions / Threat Model

This is not a cybersecurity attack study and specifies no formal threat model. Its relevant system and environmental assumptions are:

- The agent receives the correct task description, current cached webpage snapshot, and ground-truth previous-action history at each independently evaluated step (§4.2, p. 7).
- The correct next action is representable as a target element plus an operation and, when needed, a value (§2.1, pp. 3–4).
- Candidate filtering retains an acceptable target often enough for downstream prediction; measured training recall after preprocessing is 94.7% (§4.2).
- Equivalent nested elements can be recognized with heuristics based on clickable ancestors, visible descendants, and bounding boxes (Appendix C.1, p. 20).
- Offline cached traces approximate real webpages sufficiently for model development, although uncached alternative actions fail immediately (§6, p. 10).
- Pop-ups, advertisements, and CAPTCHAs are intentionally removed or cleared to create clean demonstrations (Appendix B.3, p. 19).
- State-changing actions can be represented by a non-executed Click (Fake) annotation; actual deployment would require confirmation or another safety control (Appendix B.3, p. 19).

Trusted components include author verification, the annotation tool, recorded webpage snapshots, and ground-truth action histories. The paper does not study malicious webpage manipulation, prompt injection, adversarial HTML, credential misuse, or hostile annotators.

# 7. Methodology

## 7.1 Study design

The project has two linked parts:

1. A crowdsourced dataset-construction study over real websites.
2. A supervised/in-context modeling study evaluating next-action prediction under three distribution shifts.

## 7.2 Dataset instance structure

Each instance contains (§2.1, pp. 3–4):

- a high-level task description;
- a sequence of \((\text{Target Element},\text{Operation})\) pairs;
- webpage snapshots and traces constituting the environment.

Snapshot formats include self-contained MHTML, DOM snapshots with layout/style information, HTTP Archive (HAR) network records, and full annotation traces. These underlying files were referenced but not supplied here.

## 7.3 Data collection

The authors use four stages (§2.2, pp. 4–5):

1. **Website selection:** five top-level categories—Travel, Shopping, Service, Entertainment, and Information—divided into 31 secondary domains. Three to five representative sites were manually selected per domain, producing 137 websites.
2. **Task proposal:** workers receive a site description and ten randomly sampled seed tasks from a pool of 50 ChatGPT-generated seeds per website. They propose open-ended, realistic, multi-step tasks and are instructed not to copy seeds.
3. **Task demonstration:** workers use a Playwright-based interface to select an element, confirm it, and specify the operation. Exploration occurs first and is not recorded.
4. **Task verification:** authors reject low-quality tasks, remove extraneous actions, align descriptions with demonstrations, and send uncertain items to the first author.

Collection began with 2,411 demonstrations; 61 were discarded, leaving 2,350. Descriptions were revised in 390 retained tasks and extraneous steps removed in 187 (§2.2, p. 5).

Appendix B adds that workers required at least 1,000 approved Human Intelligence Tasks and an approval rate above 98%. Estimated compensation was $10.10 per hour; proposal tasks paid $0.05 per HIT, and approved demonstrations paid $0.80. Workers completed consent, training, a video tutorial, and qualification assessment (pp. 17–18).

## 7.4 Safety during collection

Workers used anonymous accounts in a remote sandbox and were instructed not to enter sensitive information. Click (Fake) recorded potentially state-changing actions without executing them. CAPTCHAs and pop-ups were cleared during unrecorded exploration, and unrelated actions were filtered later (Appendix B.1–B.3, pp. 17–19).

## 7.5 MindAct architecture

### Stage 1: candidate generation

Input:

- task description;
- prior actions;
- candidate DOM element representations.

The task description and prior actions form a query. Each candidate representation combines its tag, textual content, salient attributes, and parent/child context. A DeBERTa-v3-base cross-encoder scores query–element pairs (§3.1, pp. 5–6; Appendix C.2, p. 20).

Training uses the labeled target as positive and randomly sampled page elements as negatives. A sigmoid converts the score to a binary probability, optimized with binary cross-entropy. At inference, all elements are ranked and the top \(k\) proceed to Stage 2. The main experiments use top 50 (§4.3, p. 7).

### Stage 2: action prediction

Candidate elements and their neighbors form a reduced HTML snippet. Up to five candidates plus “None of the above” are presented to an LLM at once. The model chooses an element and generates its operation and optional value (§3.2, p. 6).

If multiple groups each yield a candidate, selected candidates are regrouped and evaluated again. Iteration continues until one element remains or every group chooses None.

A comparison baseline directly generates a target element from the snippet rather than selecting among options.

## 7.6 Preprocessing

Simple heuristics keep visible, semantically meaningful elements based on attributes, text, and neighbors. Average elements fall from 1,135 to 580, while training-data target recall remains 94.7% (§4.2, p. 7).

[C] This is a reduction of \(1{,}135-580=555\) elements per page, or approximately \(555/1{,}135=48.9\%\). This reduction percentage is analyst-derived.

## 7.7 Data splits

| Split | Construction | Tasks | Websites |
|---|---|---:|---:|
| Training | Remaining data after test splits | 1,009 | 73 |
| Cross-Task | Random 20% of remaining eligible data; familiar websites | 252 | 69 |
| Cross-Website | Ten unseen websites from each remaining top-level domain | 177 | Not separately stated in aggregate beyond the selection rule |
| Cross-Domain | Information and Service held out entirely | 912 | 73 |

The task counts sum to \(1{,}009+252+177+912=2{,}350\) [C], matching the verified dataset total.

## 7.8 Models and baselines

- Classification baseline: DeBERTa-based candidate generator.
- Direct-generation baseline: Flan-T5-Base, 220 million parameters.
- MindAct: Flan-T5-Base, Large, or XL with multiple-choice element selection.
- In-context MindAct: GPT-3.5-turbo and GPT-4 with three demonstrations.
- Candidate ranker: DeBERTa-v3-base, reported as 86 million parameters (§4.3).

## 7.9 Metrics

- **Element Accuracy:** whether the selected element is among acceptable equivalents.
- **Operation F1:** token-level F1 for the operation output; equivalent to accuracy for Click and sensitive to values for Type/Select Option.
- **Step Success Rate (Step SR):** both element and operation must be correct for a step.
- **Success Rate (SR):** every step in the task must succeed.

Every step is evaluated independently with ground-truth history. Step-wise metrics are macro-averaged across tasks (§4.2, p. 7).

## 7.10 Equivalent-element evaluation

The evaluation heuristic finds the nearest clickable ancestor of the labeled element, then also admits visible descendants within its rendered bounding box. Manual checking of 100 cases where the heuristic changed the top-level target reportedly confirmed validity (Appendix C.1, p. 20).

## 7.11 Hyperparameters and hardware

| Component | Configuration |
|---|---|
| DeBERTa candidate generator | Batch 32; 5 epochs; learning rate \(3\times10^{-5}\) |
| Flan-T5 direct generation | Batch 32; 5 epochs; learning rate \(5\times10^{-5}\) |
| Flan-T5 MindAct | Batch 32; 5 epochs; learning rate \(5\times10^{-5}\) |
| GPT-3.5/GPT-4 | Temperature 0; three demonstrations |
| Flan-T5-Large/XL hardware | Four A100 80 GB accelerators |
| Other model hardware | One A6000 48 GB accelerator |

Software named in Appendix C.2 includes Sentence-Transformers’ cross-encoder implementation and Hugging Face Transformers’ sequence-to-sequence implementation. Versions and random-seed values are not reported.

# 8. Experiments / Analyses

## X1 — Dataset comparison

**Purpose:** establish Mind2Web’s breadth and realism relative to six earlier datasets.

**Evidence:** Table 1 (p. 5) compares domains, environments, environment type, average elements, task count/type, and average actions.

**Result:** Mind2Web has 137 real-world web environments, 31 secondary domains, 2,350 high-level tasks, 1,135 average elements, and 7.3 average actions. WebShop contains more nominal products (12,000) but only one simplified shopping environment.

**Caveat:** task-count entries are not perfectly commensurable: Table 1 mixes tasks, products, and dialogues.

## X2 — Candidate-generation recall

**Purpose:** test whether the small ranker retains the correct target in a manageable candidate pool.

**Setup:** DeBERTa-v3-base, top-50 ranked elements.

**Results (§4.3, p. 7):**

- Cross-Task Recall@50: 88.9%.
- Cross-Website: 85.3%.
- Cross-Domain: 85.7%.

**Interpretation:** the ranking stage usually includes the target among 50 candidates but imposes an upper-bound failure source when it does not.

## X3 — Main action-prediction comparison

**Purpose:** compare classification, direct generation, and MindAct variants.

**Data:** all three test splits except GPT-4, which uses 50 tasks per split and top-10 candidates.

**Metrics:** element accuracy, operation F1, step SR, and whole-task SR.

**Principal result:** MindAct’s multiple-choice formulation substantially improves on direct Flan-T5 generation. Flan-T5-XL yields the best reported step SR: 52.0%, 38.9%, and 39.6% across Cross-Task, Cross-Website, and Cross-Domain (Table 2).

**Caveats:** GPT-4 is measured on smaller subsets and top-10 rather than top-50 candidates. Main Table 2 values are therefore not directly comparable without Table 7.

## X4 — Three levels of generalization

**Purpose:** determine how performance changes as test environments become less familiar.

**Result:** models generally perform best on Cross-Task. Cross-Website and Cross-Domain results are surprisingly similar, especially for tuned Flan-T5 models (§4.3, p. 8).

**Authors’ interpretation:** unfamiliar page design and interaction logic may be a larger obstacle than domain identity.

**Analyst qualification [D]:** similarity between these two aggregate splits does not isolate causal mechanisms; website composition and task difficulty also differ.

## X5 — In-context learning

**Purpose:** test GPT-3.5 and GPT-4 with three demonstrations instead of fine-tuning.

**Result:** GPT-3.5 has low element accuracy—20.3%, 19.3%, and 21.6%—and is reported to over-select None. GPT-4 produces 41.6%, 35.8%, and 37.1% element accuracy (Table 2).

**Caveat:** GPT-4 used only 50 tasks per split and top-10 candidates. The authors explicitly say comparison with fully fine-tuned Flan-T5 is not fair (§4.3, p. 8).

## X6 — Random candidate-grouping robustness

**Purpose:** measure variability caused by shuffling candidates into different groups.

**Setup:** five random seeds for each Flan-T5 size.

**Result:** every standard deviation is below 1 percentage point; Flan-T5-XL reports \(51.9\pm0.8\), \(39.5\pm0.2\), and \(39.6\pm0.2\) step SR (Table 5, p. 21).

## X7 — Zero-shot Flan-T5-XL

**Purpose:** determine whether a model already trained generally for multiple choice can perform HTML element selection without Mind2Web fine-tuning.

**Result:** element selection is 10.8%, 7.8%, and 11.7% zero-shot versus 52.0%, 38.9%, and 39.6% after fine-tuning (Table 6, p. 21).

**Authors’ explanation:** Flan-T5 was not tuned for HTML and coding-related tasks.

## X8 — GPT-4 subset comparability

**Purpose:** assess whether GPT-4’s 50-task subsets resemble the full test sets.

**Result:** Table 7 shows the same broad ordering, although some subset/full-set differences are material. For example, Flan-T5-L Cross-Domain step SR is 27.6% on the subset versus 37.3% on the full test set (p. 22).

**Qualification:** “consistent” refers to broad relative patterns, not close numerical identity in every cell.

# 9. Results

## 9.1 Main model results

| Model | Cross-Task Step SR / Task SR | Cross-Website Step SR / Task SR | Cross-Domain Step SR / Task SR |
|---|---:|---:|---:|
| Direct generation | 17.5 / 0.0 | 11.0 / 0.0 | 11.9 / 0.4 |
| MindAct Flan-T5-B | 41.0 / 4.0 | 29.5 / 1.7 | 31.6 / 1.6 |
| MindAct Flan-T5-L | 50.3 / 7.1 | 35.3 / 1.1 | 37.3 / 2.7 |
| MindAct Flan-T5-XL | 52.0 / 5.2 | 38.9 / 5.1 | 39.6 / 2.9 |
| MindAct GPT-3.5 | 17.4 / 0.8 | 16.2 / 0.6 | 18.6 / 1.0 |
| MindAct GPT-4* | 36.2 / 2.0 | 30.1 / 2.0 | 26.4 / 2.0 |

All values are percentages from Table 2 (p. 7). The asterisk denotes 50 tasks per split and top-10 candidates.

## 9.2 Effect of multiple-choice formulation

For Flan-T5-Base, MindAct versus direct generation changes step SR as follows [C]:

- Cross-Task: \(41.0-17.5=23.5\) percentage points.
- Cross-Website: \(29.5-11.0=18.5\) points.
- Cross-Domain: \(31.6-11.9=19.7\) points.

These are absolute percentage-point gains, not relative percent improvements.

## 9.3 Model size

Within fine-tuned MindAct, larger Flan-T5 models generally improve element accuracy and step SR. Flan-T5-XL has the highest step SR in every split, but not the highest operation F1: Flan-T5-Base reaches 76.8% Cross-Task operation F1, versus 75.7% for Large and XL (Table 2).

Whole-task SR is not monotonic with model size. Cross-Task task SR peaks at 7.1% for Flan-T5-L, above XL’s 5.2%.

## 9.4 Generalization gap

For Flan-T5-XL [C]:

- Cross-Task versus Cross-Website: \(52.0-38.9=13.1\) percentage points.
- Cross-Task versus Cross-Domain: \(52.0-39.6=12.4\) points.
- Cross-Domain exceeds Cross-Website by 0.7 points.

This supports the authors’ claim that unseen environments are substantially harder, while unseen domains are not consistently worse than unseen websites.

## 9.5 Step versus task success

The large difference between step SR and task SR shows error accumulation. Flan-T5-XL correctly completes 52.0% of Cross-Task steps but only 5.2% of whole tasks. Because average tasks contain 7.3 actions (Table 1), one error is enough to invalidate a complete trajectory.

## 9.6 Candidate bottleneck

Top-50 recall is 85.3–88.9%, so approximately 11.1–14.7% of labeled targets are absent from the downstream candidate pool [C: \(100-\text{Recall@50}\)]. Even a perfect Stage 2 could not select absent candidates under this pipeline.

## 9.7 Reproducibility signal

Grouping randomness contributes less than one percentage point of standard deviation in Table 5. However, no confidence intervals, statistical significance tests, or seed identifiers are supplied.

# 10. Figure-by-Figure Interpretation

### Figure 1 — Task and domain diversity

- **Location:** p. 2, §1.
- **Content:** Six example website tasks plus a treemap of dataset domains.
- **Panels:** Flights, social media, streaming-film filtering, and appointment scheduling demonstrate same-site variation, analogous tasks across sites, and disparate domains.
- **Treemap encoding:** Area represents the percentage of tasks in each category/domain.
- **Top-level proportions:** Travel 27.4%, Information 20.4%, Service 18.3%, Shopping 17.5%, Entertainment 16.1%.
- **Largest readable secondary category:** Health at 6.5%; “Other” travel tasks at 6.2%; Airlines at 5.8%.
- **Conclusion supported:** Mind2Web covers diverse websites, domains, and action patterns.
- **Caveat:** It visualizes task composition, not empirical agent performance. The six examples are illustrative, not a random sample.

### Figure 2 — Anatomy of a dataset instance

- **Location:** p. 4, §2.1.
- **Content:** A goal (“Show me the reviews for the auto repair business closest to 10002”), a ten-step action sequence, and corresponding webpage snapshots/HTML elements.
- **Flow:** Task description → successive target/operation pairs → page state changes.
- **Red actions:** Indicate transitions to a new webpage.
- **Methodological role:** Demonstrates that actions span multiple pages and that snapshots align webpage controls with annotations.
- **Caveat:** The figure presents one curated example and does not quantify annotation error.

### Figure 3 — Overall MindAct pipeline

- **Location:** p. 6, §3.
- **Components:** HTML document, task description, previous actions, ranking language model, candidate elements, top-\(k\) elements, reduced HTML snippet, prediction LLM, target element, and operation.
- **Data flow:** The small model filters the large DOM; the large model reasons over the reduced representation.
- **Conclusion supported:** Candidate filtering makes real-world HTML manageable.
- **Caveat:** The diagram does not show training losses, candidate grouping recursion, or failure handling in full detail.

### Figure 4 — Candidate-generation module

- **Location:** p. 6, §3.1.
- **Task query:** Concatenated task and prior actions.
- **Candidate representation:** Candidate target plus ancestor/context text.
- **Model:** Ranking LM followed by a binary classifier producing a score in \([0,1]\).
- **Flow:** Query–candidate pair → cross-encoder → relevance score → ranking.
- **Caveat:** Exact serialization and truncation limits are not fully specified in the figure or prose.

### Figure 5 — Action-prediction formulations

- **Location:** p. 6, §3.2.
- **Top/direct generation:** LLM produces a target/action from an HTML snippet.
- **Bottom/multiple choice:** LLM chooses among labeled candidate elements, then emits action and value.
- **Example:** A size selector is chosen and assigned `SELECT` with value “Queen.”
- **Conclusion supported:** Shows the structural difference behind the experimental comparison.
- **Caveat:** It is an illustrative prompt, not a performance plot.

### Figure 6 — Per-website step success

- **Location:** p. 8, §4.3.
- **Plot type:** Grouped sequence of vertical bars, arranged by Cross-Task, Cross-Website, and Cross-Domain.
- **Y-axis:** Step success rate, apparently from 0 to roughly 0.7.
- **X-axis:** Individual websites with more than three test tasks.
- **Colors:** Top-level domains.
- **Observation:** Strong variation exists between individual websites. Cross-Website and Cross-Domain ranges visually overlap; Cross-Task contains more high bars.
- **Exact values:** Not labeled and cannot be recovered confidently from the supplied resolution.
- **Conclusion supported:** Website-level variability and no visually clean separation between Cross-Website and Cross-Domain.
- **Caveat:** Sites with three or fewer test tasks are omitted; exact labels and heights are unreadable.

### Figure 7 — Annotation tool

- **Location:** p. 18, Appendix B.3.
- **Content:** A dialogue/control window on the left and a live browser window on the right.
- **Control flow:** The annotator selects elements in the browser but chooses operations through the dialogue tool.
- **Purpose:** Separates element selection from operation execution and enables controlled recording.
- **Caveat:** Small interface text is only partly readable, but the two-window structure is clear.

### Figure 8 — Demonstration workflow

- **Location:** p. 18, Appendix B.3.
- **Sequence:** Select website/task → explore and prepare → demonstrate task → select operation → confirm task.
- **Loop/connection:** Element selection feeds operation selection; completion leads to confirmation.
- **Purpose:** Makes the annotation lifecycle explicit.
- **Caveat:** Quality review after submission is described elsewhere, not in this flowchart.

### Figure 9 — Type-operation dialogue

- **Location:** p. 19, Appendix B.3.
- **Content:** Selected element, prompt for the value, and a typed example (“New York”).
- **Purpose:** Shows how value-bearing Type actions are recorded.
- **Caveat:** Interface text is illustrative.

### Figure 10 — Select Option dialogue

- **Location:** p. 19, Appendix B.3.
- **Content:** A list of HTML select options from which the worker chooses.
- **Purpose:** Shows conversion of a click on a select element into a normalized Select Option action.
- **Caveat:** The example does not establish how all custom, non-native dropdowns are handled.

### Figure 11 — Verification tool

- **Location:** p. 20, Appendix B.4.
- **Content:** Task description, action list, verification controls, and webpage display.
- **Decision points:** Keep/remove/mark uncertain for actions; confirm or revise task description.
- **Escalation:** “Unsure” triggers first-author reevaluation.
- **Purpose:** Supports claimed quality control.
- **Caveat:** The paper reports verification procedures but no inter-annotator agreement statistic.

# 11. Table-by-Table Interpretation

### Table 1 — Dataset comparison

- **Location:** p. 5, §2.3.
- **Rows:** MiniWoB++, WebShop, RUSS, PixelHelp, META-GUI, MoTIF, and Mind2Web.
- **Columns:** Domains, environments, environment type, average elements, number of tasks, instruction level, and average actions.
- **Mind2Web row:** 5 top-level/31 secondary domains; 137 real websites; 1,135 average elements; 2,350 high-level tasks; 7.3 average actions.
- **Largest alternative environment count:** MoTIF, 125 mobile apps.
- **Interpretation:** Mind2Web is broader and structurally more complex among the compared datasets.
- **Caveat:** “# Tasks” is heterogeneous across rows, including products and dialogues; missing entries use “–”.

### Table 2 — Main results

- **Location:** p. 7, §4.3.
- **Columns:** Element Accuracy, Operation F1, Step SR, and task SR for all three splits.
- **Best step SR:** Flan-T5-XL: 52.0, 38.9, 39.6.
- **Best task SR:** Flan-T5-L Cross-Task at 7.1; Flan-T5-XL Cross-Website at 5.1; Flan-T5-XL Cross-Domain at 2.9.
- **Best operation F1:** Flan-T5-Base Cross-Task at 76.8; Flan-T5-Base Cross-Website at 67.6; Flan-T5-Base Cross-Domain at 67.3.
- **Missing metrics:** Classification reports only element accuracy because it does not generate operations.
- **Footnote:** GPT-4 uses 50 tasks and top-10 candidates.
- **Interpretation:** Multiple-choice MindAct is substantially stronger than direct generation, but complete-task reliability remains poor.

### Table 3 — Seed-task prompt

- **Location:** p. 17, Appendix B.2.
- **Content:** American Airlines site description, instructions for five realistic high-level tasks, constraints against step-by-step language, and five example outputs.
- **Purpose:** Documents how ChatGPT-generated ideas were elicited.
- **Important safeguard:** Seeds were inspiration only; copying was prohibited and similar proposals were rejected.
- **Caveat:** The table shows one website’s prompt, not the full set of generated seeds.

### Table 4 — Hyperparameters

- **Location:** p. 21, Appendix C.2.
- **Values:** Batch size 32, five epochs, learning rates \(3\times10^{-5}\) for DeBERTa and \(5\times10^{-5}\) for Flan-T5; GPT temperature 0 and three demonstrations.
- **Interpretation:** Supplies core training settings.
- **Missing:** Optimizer, scheduler, sequence length, gradient settings, early stopping, and exact seeds.

### Table 5 — Random-grouping variability

- **Location:** p. 21, Appendix D.1.
- **Statistic:** Mean ± standard deviation over five runs.
- **Best means:** Flan-T5-XL: 51.9, 39.5, 39.6.
- **Uncertainty:** All standard deviations are 0.8 or below.
- **Interpretation:** Random grouping has relatively small measured effects.
- **Caveat:** Standard deviation across five seeds is not a confidence interval.

### Table 6 — Zero-shot versus fine-tuned Flan-T5-XL

- **Location:** p. 21, Appendix D.2.
- **Zero-shot:** 10.8, 7.8, 11.7 element accuracy.
- **Fine-tuned:** 52.0, 38.9, 39.6.
- **Absolute gains [C]:** 41.2, 31.1, and 27.9 percentage points.
- **Interpretation:** Generic multiple-choice ability is insufficient; task-specific fine-tuning matters.

### Table 7 — Results on GPT-4’s 50-task subsets

- **Location:** p. 22, Appendix D.3.
- **Rows:** Three Flan-T5 sizes, GPT-3.5, and GPT-4.
- **Values:** Step SR; parentheses give full-test results for non-GPT-4 methods.
- **Notable result:** GPT-4 scores 36.2, 30.1, and 26.4. Flan-T5-XL subset scores 47.9, 33.3, and 34.6.
- **Interpretation:** GPT-4 is competitive on unseen websites but not superior to the best fine-tuned model on these subsets.
- **Caveat:** The Cross-Domain subset differs notably from full results for Flan-T5-L and XL.

### Table 8 — GPT action-prediction prompt

- **Location:** pp. 23–24, Appendix D.
- **Content:** System message plus three worked demonstrations containing reduced HTML, task, previous actions, candidate choices, and answers.
- **Examples:** Selecting pickup as a reservation type; choosing None when the necessary date element is absent; choosing a date button for a rental task.
- **Purpose:** Makes the three-shot in-context configuration concrete.
- **Caveat:** HTML is explicitly truncated “to save space”; therefore the displayed table is not necessarily a byte-for-byte reproduction of the complete runtime prompt.

# 12. Diagram / Architecture Interpretation

MindAct’s central design is a coarse-to-fine pipeline:

```text
Task + previous actions ─┐
                         ├─> DeBERTa cross-encoder ranks every retained DOM element
Current page DOM ────────┘
                                      │
                                  top 50
                                      ▼
                     Candidate elements + neighboring HTML
                                      │
                         groups of at most 5 + None
                                      ▼
                     Flan-T5 or prompted GPT selects element
                                      │
                        operation + optional value
```

The ranking stage reduces the search space. The prediction stage performs more expensive contextual reasoning only over a compact snippet. During multiple-choice inference, winners from separate five-option groups are recursively compared until one remains or all are rejected (§§3.1–3.2, pp. 5–6).

The architecture separates two error sources:

- **Retrieval/ranking failure:** the correct element is not in the candidate pool.
- **Prediction failure:** the correct candidate is present but the LLM chooses the wrong element, action, or value.

The dataset-generation workflow is distinct from this model pipeline. Workers first explore and clean the page state, then record controlled element/operation pairs, and authors subsequently verify both actions and task wording (Figures 7–11; Appendix B).

# 13. Equations and Mathematical Concepts

No numbered equations appear in the supplied paper. The essential mathematical objects are described in prose.

## Candidate matching score

For a task/history query \(q\) and DOM element representation \(e\), the cross-encoder produces a score. A sigmoid maps it to the interval \([0,1]\):

\[
p(e\mid q)=\sigma(s(q,e)).
\]

This notation is a faithful reconstruction of the prose, not an equation printed by the authors (§3.1, p. 6). The target element is positive; randomly sampled other elements are negative.

## Binary cross-entropy objective

The ranking score is optimized with binary cross-entropy:

\[
L=-\bigl[y\log p+(1-y)\log(1-p)\bigr].
\]

Again, the exact displayed form is analyst-supplied to explain the named objective; the paper does not print it. Here \(y=1\) for a target element and \(y=0\) for a sampled negative.

## Left-to-right language-model objective

The action predictor is trained to generate a target sequence token by token using a left-to-right objective (§3.2, p. 6). In ordinary language, each next output token is learned conditional on the prompt and previously generated output. The paper does not state a formula.

## Recall@50

Recall@50 asks whether an acceptable target appears among the ranker’s 50 highest-scoring candidates. It measures candidate coverage, not final action correctness.

## Operation F1

Token-level precision and recall over the generated operation/value are combined using the F1 harmonic mean. The paper does not print the formula. For Click, it reduces to an exact correctness decision; Type and Select Option also require correct value content (§4.2, p. 7).

## Step and task success

Conceptually:

\[
\text{StepSuccess}
=
\mathbf{1}[\text{element correct}\land\text{operation correct}],
\]

\[
\text{TaskSuccess}
=
\prod_{t=1}^{T}\text{StepSuccess}_t.
\]

These are explanatory reconstructions of the textual definitions. The second shows why one failed step makes the whole task unsuccessful.

# 14. Interpretation and Discussion

The dataset directly addresses RQ1 by operationalizing “generalist web agent” as next-action prediction over diverse real-web snapshots under progressively harder generalization conditions. MindAct then supplies an initial modeling answer: reduce the page with a specialized ranker and pose grounded selection as discrimination rather than unconstrained generation.

The evidence strongly supports the narrow claim that this multiple-choice implementation outperforms the tested direct-generation baseline. It does not establish that the approach solves arbitrary live-web tasks. Evaluation is offline, individual steps receive ground-truth histories, and whole-task success is low.

The near similarity of Cross-Website and Cross-Domain aggregate performance is important. The authors interpret it as evidence that diverse layouts and interaction logic create more difficulty than high-level domain identity (§4.3, p. 8). This is plausible but not conclusively isolated by the design [D], because the splits contain different websites, tasks, and sample sizes.

GPT-4’s result is suggestive rather than decisive. Its element accuracy approaches tuned Flan-T5 on unseen websites/domains in Table 2, but the experiment uses fewer tasks and a smaller candidate pool. Table 7 provides a fairer subset view, on which GPT-4 trails Flan-T5-XL in every split for step SR.

A notable metric pattern is that operation F1 is much higher than element accuracy or step SR. This suggests that identifying where to act is a dominant bottleneck, although a formal error decomposition is not supplied.

No direct contradiction was found between the main tables and appendix tables. Table 5’s means differ slightly from Table 2 because it summarizes five random groupings, while Table 2 reports the main runs. Table 7’s subset values sometimes differ considerably from full-set values, but the table labels those populations clearly.

# 15. Contributions and Novelty

All novelty claims below are author-reported rather than externally verified.

- **Dataset contribution:** 2,350 verified, high-level tasks over 137 real websites and 31 secondary domains.
- **Representation contribution:** Task descriptions, action sequences, MHTML, DOM/layout snapshots, network archives, and annotation traces.
- **Benchmark contribution:** Three splits targeting task-, website-, and domain-level generalization.
- **Methodological contribution:** MindAct’s two-stage candidate-ranking and multiple-choice prediction architecture.
- **Evaluation contribution:** Element, operation, step, and whole-task metrics with equivalent-element normalization.
- **Data-collection contribution:** Controlled Playwright annotation, fake clicks for side-effecting actions, author verification, and documented crowdsourcing procedures.
- **Empirical contribution:** Evidence that discriminative candidate selection is stronger than direct target generation in this setting, while reliable full-task execution remains unsolved.
- **Artifact contribution:** Homepage, MIT-licensed code, and CC BY 4.0 training/test data are listed in Appendix A, although those artifacts were not supplied for inspection.

# 16. Limitations

## Authors’ stated limitations

- Websites are predominantly English-language and primarily used in the United States (§6, p. 9).
- Mechanical Turk annotators may be more web-proficient than the wider population (§6, p. 9).
- Covered tasks and websites represent only a subset of possible web activity (§6, p. 9).
- MindAct uses textual webpage context but not rendered visual information (§6, p. 10).
- Each page is encoded independently; changes between webpage states are not explicitly modeled (§6, p. 10).
- Users provide a single up-front instruction; no mid-task clarification or conversational revision is supported (§6, p. 10).
- Offline evaluation produces false negatives when a valid alternative path was not cached (§6, p. 10).
- Pop-ups and CAPTCHAs are excluded even though they are part of real browsing (Appendix B.3, p. 19).
- GPT-4 evaluation is limited to 50 tasks per setting because of cost (§4.3; Appendix D.3).
- Operational cost is a concern for GPT-4 (§4.3, p. 8).
- Deployment raises risks around sensitive actions, transparency, user control, CAPTCHA circumvention, and malicious activity (§6, p. 10).

## Additional evidence-based analyst observations

- **[D] Step-level oracle history:** Supplying ground-truth prior actions prevents errors from propagating during evaluation, so step metrics do not measure autonomous closed-loop execution.
- **[D] Limited task-success evidence:** Whole-task SR is very low, and cached evaluation does not demonstrate live completion.
- **[D] No statistical hypothesis tests:** Except for five-seed means and standard deviations in Table 5, the paper supplies no confidence intervals or significance tests.
- **[D] Incomplete implementation specification:** Optimizer, maximum sequence length, truncation policy, exact seed values, and some candidate-serialization details are absent.
- **[D] Verification reliability:** Author review is extensive, but no independent agreement coefficient or blinded audit is reported.
- **[D] Seed influence:** Even with copying prohibited, showing model-generated examples may shape the distribution of proposed tasks.
- **[D] Temporal fragility:** Real-site snapshots improve realism but encode website states from a particular period and may not represent later interfaces.
- **[D] Equivalent-element heuristic:** Manual validation covers 100 changed cases; performance over all equivalence patterns is not quantified.
- **[D] GPT comparison:** Different task counts and top-\(k\) values prevent straightforward model ranking from Table 2 alone.

# 17. Threats to Validity

These labels are analyst-applied unless explicitly noted.

## Internal validity

Performance differences may reflect candidate recall, prompt construction, grouping order, HTML truncation, or model size in addition to the multiple-choice formulation. The five-run grouping analysis addresses one source but not all.

## Construct validity

Next-action prediction with oracle history is a useful grounding measure, but it is not identical to completing a task autonomously. Whole-task SR is closer to the target construct but is computed over cached demonstrations rather than interactive execution.

## External validity

The language, geography, worker population, selected websites, and clean browsing conditions restrict generalization to the whole web. The authors explicitly acknowledge these issues.

## Statistical conclusion validity

The main results are point estimates. Test sets differ greatly in size—177, 252, and 912 tasks—and most runs lack error estimates. GPT-4 uses only 50 tasks per split.

## Ecological validity

Using authentic webpage snapshots improves realism. Conversely, removing pop-ups/CAPTCHAs, blocking real side effects, and disallowing uncached alternatives reduces resemblance to unrestricted live browsing.

## Reproducibility

Core hyperparameters, model families, hardware, prompts, code, and dataset links are reported. Reproducibility cannot be verified here because artifacts were not supplied, and several training details are omitted.

## Data leakage

The split logic prevents test websites or domains from appearing in training for the relevant settings. The paper does not discuss possible pretraining exposure of the underlying public websites to the language models.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- Incorporate rendered visual information and multimodal models.
- Model changes between successive webpage states.
- Add conversational human–agent interaction and confirmation.
- Use reinforcement learning with feedback from real websites.
- Develop smaller language models specialized for web understanding/action.
- Expand to more countries, languages, demographics, and professional domains.
- Improve cached replay using recorded network traffic.
- Conduct end-to-end live-site evaluation with human assistance.
- Handle pop-ups and CAPTCHAs robustly.
- Develop safety controls for sensitive or potentially malicious actions.
- Improve transparency, interpretability, and user control.

## B. Additional open questions

- How much final error is attributable separately to candidate ranking, element choice, operation choice, and value generation?
- How would results change without ground-truth action history?
- Can valid alternative trajectories be evaluated without requiring exact replay?
- How robust are agents to adversarial, misleading, or rapidly changing HTML?
- What confirmation policies safely balance autonomy with user control?
- How do performance and task distributions vary across languages and accessibility needs?
- Does adding screenshots improve grounding consistently, or mainly on visually structured controls?
- How well do models trained on historical snapshots transfer to redesigned live sites?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| Action sequence | Ordered steps needed to complete a web task |
| Candidate element | A webpage control that might be the correct next target |
| CAPTCHA | A challenge intended to distinguish people from automated programs |
| Click (Fake) | Annotation recorded as a click without executing the real side effect |
| Cross-Domain | Test condition holding out entire top-level domains |
| Cross-encoder | Model jointly reading a query and candidate to produce a matching score |
| Cross-Task | Test condition with new tasks on websites represented in training |
| Cross-Website | Test condition with unseen websites in familiar broad domains |
| DeBERTa | Encoder language-model family used for candidate ranking |
| DOM | Document Object Model: the webpage’s structured tree of elements |
| Element Accuracy | Percentage of steps selecting an acceptable target element |
| Flan-T5 | Instruction-tuned encoder–decoder model used for action prediction |
| Grounding | Connecting language to an executable object/action in an environment |
| HAR | HTTP Archive containing recorded network traffic |
| HIT | Human Intelligence Task on Mechanical Turk |
| HTML | Markup describing webpage structure and content |
| In-context learning | Solving a task from examples in the prompt without parameter updates |
| LLM | Large language model |
| MHTML | Self-contained archived webpage format |
| Mind2Web | The paper’s dataset and benchmark |
| MindAct | Its two-stage ranking and action-prediction method |
| Operation F1 | Token-level correctness measure for predicted action and value |
| Oracle/ground-truth history | Correct prior actions supplied to the model during step evaluation |
| Playwright | Browser-automation framework used in the annotation tool |
| Recall@50 | Frequency with which the correct target appears among 50 candidates |
| Select Option | Choosing a value from a webpage selection control |
| Step SR | Step Success Rate: correct element and operation |
| Task SR / SR | Whole-task Success Rate: every action step must be correct |
| top-\(k\) | The \(k\) highest-ranked candidates |
| \(t-1\) | All steps before current step \(t\) |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Retained tasks | 2,350 | tasks | After verification | Author-reported | p. 5, §2.2 |
| Initially collected | 2,411 | tasks | Before verification | Author-reported | p. 5 |
| Discarded | 61 | tasks | Verification | Author-reported | p. 5 |
| Revised descriptions | 390 | tasks | Retained set | Author-reported | p. 5 |
| Tasks with extraneous steps removed | 187 | tasks | Retained set | Author-reported | p. 5 |
| Websites | 137 | websites | Dataset total | Author-reported | pp. 2, 4–5 |
| Domain structure | 5 / 31 | top-level / secondary domains | Dataset total | Author-reported | pp. 4–5 |
| Average page elements | 1,135 | elements | Before preprocessing | Author-reported | Table 1, p. 5 |
| Average task length | 7.3 | actions | Mind2Web | Author-reported | Table 1 |
| Training split | 1,009 | tasks | 73 websites | Author-reported | p. 7, §4.1 |
| Cross-Task split | 252 | tasks | 69 websites | Author-reported | p. 7 |
| Cross-Website split | 177 | tasks | Unseen sites | Author-reported | p. 7 |
| Cross-Domain split | 912 | tasks | 73 websites | Author-reported | p. 7 |
| Split-count check | 2,350 | tasks | \(1009+252+177+912\) | Analyst-derived | p. 7 |
| Elements after preprocessing | 580 | elements/page average | Semantic/visibility filtering | Author-reported | p. 7 |
| Element reduction | 48.9 | percent | \((1135-580)/1135\) | Analyst-derived | p. 7 |
| Preprocessing target recall | 94.7 | percent | Training data | Author-reported | p. 7 |
| Candidate Recall@50 | 88.9 / 85.3 / 85.7 | percent | Task / website / domain | Author-reported | p. 7 |
| Best step SR | 52.0 / 38.9 / 39.6 | percent | Flan-T5-XL | Author-reported | Table 2 |
| Corresponding task SR | 5.2 / 5.1 / 2.9 | percent | Flan-T5-XL | Author-reported | Table 2 |
| Flan-T5-L Cross-Task task SR | 7.1 | percent | Highest Cross-Task task SR | Visually readable / author table | Table 2 |
| Direct-generation step SR | 17.5 / 11.0 / 11.9 | percent | Three splits | Author-reported | Table 2 |
| MindAct-B gain over generation | 23.5 / 18.5 / 19.7 | percentage points | Step SR | Analyst-derived | Table 2 |
| GPT-4 element accuracy | 41.6 / 35.8 / 37.1 | percent | 50 tasks/split, top-10 | Author-reported | Table 2 |
| GPT-4 step SR | 36.2 / 30.1 / 26.4 | percent | 50-task subsets | Author-reported | Tables 2, 7 |
| Zero-shot Flan-T5-XL | 10.8 / 7.8 / 11.7 | percent | Element selection | Author-reported | Table 6 |
| Fine-tuning gains over zero-shot | 41.2 / 31.1 / 27.9 | percentage points | Element selection | Analyst-derived | Table 6 |
| Grouping variability | SD < 1 | percentage point | Five runs | Author-reported | Table 5 |
| Equivalent-element audit | 100 | instances | Manual validation | Author-reported | Appendix C.1 |
| Candidate ranker size | 86 | million parameters | DeBERTa-Base | Author-reported | p. 7 |
| Direct-generation model size | 220 | million parameters | Flan-T5-Base | Author-reported | p. 8 |
| Seed tasks generated | 50 | per website | Ten shown per proposal | Author-reported | p. 4 |
| Worker eligibility | ≥1,000 and >98 | approved HITs; approval % | Mechanical Turk | Author-reported | p. 17 |
| Estimated worker rate | 10.10 | US dollars/hour | Collection design | Author-reported | p. 17 |
| Proposal/demonstration pay | 0.05 / 0.80 | US dollars | Per proposal HIT / approved final task | Author-reported | pp. 17–18 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Mind2Web provides broad realistic coverage | 137 real websites, 31 domains, 2,350 tasks, 1,135 elements/page | F1, T1, X1 | pp. 2–5 | Strong within listed dataset comparison; novelty not externally verified |
| Candidate filtering makes the input more manageable | 1,135 → 580 elements with 94.7% target recall | Preprocessing analysis | p. 7 | Strong descriptive evidence; efficiency/runtime not quantified |
| Small-model ranking usually retains the target | Recall@50 = 88.9/85.3/85.7 | X2 | p. 7 | Directly reported; still misses 11.1–14.7% |
| Multiple-choice prediction beats direct generation | Flan-T5-B step-SR gains of 18.5–23.5 points | T2, X3 | p. 7 | Strong for tested configuration |
| Generalization to unseen environments is harder | Cross-Task step SR generally exceeds other splits | T2, F6, X4 | pp. 7–8 | Strong aggregate pattern |
| Unseen websites and domains are similarly difficult | Comparable Cross-Website and Cross-Domain results | T2, F6 | pp. 7–8 | Moderate; split composition may confound interpretation |
| Current systems rarely finish whole tasks | Best task SR no higher than 7.1% in Table 2 | T2 | pp. 7–8 | Strong under offline evaluation definition |
| GPT-4 shows in-context potential | Element accuracy 35.8/37.1 on unseen sites/domains | T2, T7 | pp. 7–8, 22 | Suggestive; only 50 tasks and different top-\(k\) |
| Fine-tuning is crucial for Flan-T5-XL | Zero-shot 7.8–11.7 vs fine-tuned 38.9–52.0 | T6, X7 | p. 21 | Strong within model/setup |
| Random grouping has limited effect | All five-run SDs below 1 point | T5, X6 | p. 21 | Moderate; only five seeds |
| Dataset collection was quality-controlled | Author screening, 61 removals, 390 rewrites, 187 action cleanups | F11; Appendix B.4 | pp. 5, 17–20 | Procedurally strong; no agreement statistic |
| Live transfer should be feasible | Real webpage snapshots resemble live sites | Author discussion | p. 10 | Weakly evidenced prediction; no live evaluation presented |

# 22. Very Simple Explanation

Imagine asking a computer, “Find me a flight,” instead of telling it exactly where every button is. The computer must look at a webpage, figure out which box or button matters, perform the right action, and repeat that process across several pages.

Mind2Web gives researchers 2,350 examples of people doing tasks like that on 137 real websites. The examples include the goal, the webpage state, and the sequence of buttons, fields, and menu choices used to finish it.

The authors’ program, MindAct, first uses a smaller model to shortlist likely webpage controls. A larger model then chooses from that shortlist and decides whether to click, type, or select something. This works much better than asking the larger model to invent the answer directly.

Even so, the system is far from dependable. Its best model gets roughly four out of ten steps right on unfamiliar websites or domains, and only a small percentage of complete multi-step tasks are entirely correct. The paper’s main achievement is therefore a realistic testbed that shows researchers exactly how much work remains.

# Completeness Audit

## Coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/venue | Yes | Yes | Fully represented | Title and venue identified; author list available on p. 1 |
| Abstract | Yes | Yes | Represented in compressed form | Integrated into orientation and contributions |
| §1 Introduction | Yes | Yes | Fully represented | Problem, desiderata, gap, and contributions covered |
| §2 Dataset | Yes | Yes | Fully represented | Instance structure, collection, statistics, comparison covered |
| §2.1 Task Definition | Yes | Yes | Fully represented | Three instance components and operations covered |
| §2.2 Data Collection | Yes | Yes | Fully represented | Four stages and verification counts covered |
| §2.3 Comparison/Challenges | Yes | Yes | Fully represented | Table 1 and modeling challenges covered |
| §3 MindAct | Yes | Yes | Fully represented | Two-stage architecture covered |
| §3.1 Candidate Generation | Yes | Yes | Fully represented | Inputs, representations, loss, and inference covered |
| §3.2 Action Prediction | Yes | Yes | Fully represented | Multiple-choice grouping and direct-generation baseline covered |
| §4 Experiments | Yes | Yes | Fully represented | Splits, metrics, baselines, and major results covered |
| §4.1 Setup | Yes | Yes | Fully represented | All task counts and website counts preserved |
| §4.2 Preprocessing/Evaluation | Yes | Yes | Fully represented | Reduction, recall, and metric definitions covered |
| §4.3 Results | Yes | Yes | Fully represented | Candidate, action, generalization, and GPT analyses covered |
| §5 Related Work | Yes | Yes | Represented in compressed form | All four categories represented; individual citations not summarized separately |
| §6 Limitations/Societal Impact | Yes | Yes | Fully represented | All substantive author-stated limitations and safety issues covered |
| §7 Conclusion | Yes | Yes | Fully represented | Main conclusion and future directions covered |
| Acknowledgements | Yes | Partly | Deliberately compressed | Funding and thanks are non-methodological; sponsorship noted only in accessibility context |
| References 1–45 | Yes as supplied text | Partly | Deliberately compressed | Related-work categories retained; bibliographic entries not individually restated |
| Appendix A | Yes | Yes | Fully represented | Artifact inventory and licenses noted |
| Appendix B.1 | Yes | Yes | Fully represented | Worker requirements, consent, pay, training, review covered |
| Appendix B.2 | Yes | Yes | Fully represented | Proposal workflow and prompt covered |
| Appendix B.3 | Yes | Yes | Fully represented | Tool, operations, exploration, CAPTCHAs, fake clicks covered |
| Appendix B.4 | Yes | Yes | Fully represented | Verification workflow covered |
| Appendix C.1 | Yes | Yes | Fully represented | Equivalent-element heuristic and 100-case check covered |
| Appendix C.2 | Yes | Yes | Fully represented | Implementations, models, hyperparameters, hardware covered |
| Appendix D.1 | Yes | Yes | Fully represented | Five-run grouping analysis covered |
| Appendix D.2 | Yes | Yes | Fully represented | Zero-shot comparison covered |
| Appendix D.3 | Yes | Yes | Fully represented | 50-task subset analysis covered |
| Explicit RQ1 | Yes | Yes | Fully represented | No additional formal RQs found |
| Formal hypotheses | Yes | Yes | Fully represented | None stated |
| X1–X8 analyses | Yes | Yes | Fully represented | Each treated separately |
| Figure 1 | Visually | Yes | Fully represented | Examples and treemap interpreted |
| Figure 2 | Visually | Yes | Fully represented | Dataset instance structure interpreted |
| Figures 3–5 | Visually | Yes | Fully represented | Architecture and prompt flows interpreted |
| Figure 6 | Visually | Yes | Represented with uncertainty | Exact site labels/bar heights unreadable |
| Figures 7–11 | Visually | Yes | Fully represented | Tool interfaces and workflow interpreted |
| Table 1 | Visually/textually | Yes | Fully represented | All comparison dimensions accounted for |
| Table 2 | Visually/textually | Yes | Fully represented | Major values, maxima, missing fields, footnote covered |
| Tables 3–8 | Visually/textually | Yes | Fully represented | Purposes, key contents, values, and caveats covered |
| Formal equations | Yes | Yes | Fully represented | None printed; prose-defined mathematics explained |
| Formal algorithms | Yes | Yes | Fully represented | None printed; iterative grouping procedure represented |
| Author-stated limitations | Yes | Yes | Fully represented | Separated from analyst observations |
| Supplied supplementary material | Yes | Yes | Fully represented | Appendices A–D included |
| External data/code/models | No | Yes as limitation | Missing from supplied material | Links only; not inspected or executed |

## Missing or inaccessible material

- Dataset files and their actual examples beyond those printed in the paper.
- Code, trained models, and executable annotation/evaluation tools.
- MHTML, DOM, HAR, network traffic, and trace artifacts.
- Complete runtime prompts where Table 8 explicitly truncates HTML.
- Worker training document, tutorial video, qualification materials, and consent form.
- Live websites and any end-to-end online evaluation.
- Exact small website labels and bar heights in Figure 6.
- External sources needed to validate “first dataset” or other novelty claims.

## Uncertain interpretations

- Figure 6 supports only qualitative visual conclusions at the supplied resolution; individual bars should not be treated as exact measurements.
- The displayed sigmoid and loss equations in §13 are explanatory reconstructions of prose, not author-printed formulas.
- Table 7 supports broad subset consistency, but several subset/full-set gaps are large enough that “consistent” should not mean numerically equivalent.
- Table 1’s task-count column mixes tasks, products, and dialogues, limiting direct comparisons.
- OCR spacing occasionally separates model subscripts or words, but no substantive numerical discrepancy was detected.

## Deliberately compressed material

- The 45 bibliographic references were grouped by the paper’s four related-work categories rather than repeated individually.
- Acknowledgements, institutional disclaimer, and complete artifact URLs were compressed because they do not change the scientific method or findings.
- Table 3’s five sample seed tasks and Table 8’s complete prompt prose were summarized rather than reproduced verbatim.
- Minor webpage text embedded in screenshots was omitted where it merely instantiated the workflow already explained.

## Potential omissions

No known substantive section, subsection, experiment, figure, table, mathematical concept, contribution, author-stated limitation, or supplied appendix from the inventory is absent from this analysis. Material not represented in full is identified above as compressed, unreadable at exact-value level, or unavailable because only an external reference—not the artifact itself—was supplied.