# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible range | Pages 1–50 |
| Apparently missing pages | None |
| Native/extracted text | Available for every page; no page was mechanically classified as scanned or low-text |
| Visually rendered pages | 37 of 50: pp. 1–8, 10, 12–13, 19–26, 28–32, 34–41, 43–47 |
| Pages not visually rendered | pp. 9, 11, 14–18, 27, 33, 42, 48–50; assessed from supplied page-labeled text only |
| Figures | Figures 1–11 were available on rendered pages and visually inspected |
| Tables | Tables 1–30 were supplied as extracted text; Tables 1–21 and 22–30 were also visually available where their pages were rendered |
| Equations | The Intersection-over-Union, Dense Markup Ranking loss, cosine similarity, complexity expressions, and human-agreement equations are readable; mathematical notation remains potentially extraction-sensitive |
| Appendices | Appendices A–E are present |
| Supplementary material | Appendix C is the paper’s supplied supplementary-results section; no separate supplementary file was supplied |
| Embedded files | None |
| OCR required | No; native text was available |
| Material limitations | Reference-only pages not rendered visually were read from text. Appendix B.8.3 continues across pp. 33–34, but p. 33 was not rendered. Annotator instructions on pp. 48–50 were not visually inspected. No executable code, dataset files, model checkpoints, videos, DOM snapshots, annotation interface, or external website artifacts were supplied. |

Source classifications used below:

- **[A] Author-reported:** stated in the paper.
- **[B] Directly observable:** visible in a supplied rendered page.
- **[C] Analyst-derived:** calculated from supplied values; operands are shown.
- **[D] Analyst interpretation:** a clearly marked inference.
- No external information is introduced.

# 1. Plain-Language Orientation

WEBLINX studies a form of browser assistant that does more than receive one fixed command. A human “instructor” and an assistant “navigator” converse while the task develops, and the navigator acts on real websites. A request can therefore be clarified, revised, or extended over several turns. The agent must decide both **what kind of action to perform**—click, type, load a page, submit, or speak—and **what argument to use**, such as the correct element, URL, or text (pp. 1–5, §§1, 3–4).

The practical obstacle is that a real webpage may contain thousands of Document Object Model (DOM) elements, too much information to place economically or rapidly into a language model’s prompt. The authors introduce **Dense Markup Ranking (DMR)**, a retrieval-style dual encoder that ranks webpage elements against the current conversational state and retains the most promising candidates. They combine this with an **Optimal Text Representation (OTR)** containing pruned HTML, element identifiers, XPath locations, bounding boxes, attributes, viewport dimensions, and recent dialogue/action history (pp. 2, 5–6; Appendix B.1–B.4).

The paper’s principal artifact is the WEBLINX benchmark:

- 2,337 human demonstrations;
- more than 100,000 recorded actions and utterances;
- 155 real-world website entry points;
- 15 geographic areas;
- 8 task categories and 50 subcategories;
- an average of 43 turns per demonstration;
- DOM trees, screenshots, element boxes, chat, actions, and demonstration-level video frames (pp. 1–4; Tables 1, 7–12).

The authors evaluate 19 model variants drawn from eight architectures, spanning text-only, screenshot-only, and image-plus-text models. The central empirical finding is that models finetuned on WEBLINX greatly outperform zero-shot models, and the strongest systems are finetuned text-only decoder models rather than the evaluated multimodal models. On the aggregate out-of-domain test, LLaMA-2-13B obtains an overall score of 25.21 and Sheared-LLaMA-2.7B obtains 25.02, versus 10.72 for GPT-4 Turbo and 10.45 for GPT-4V (Appendix Table 28, p. 46). Yet the finetuned models lose substantial performance outside familiar settings: LLaMA-2-13B falls from 37.09 in-domain to 25.21 out-of-domain (Table 28).

The central contribution is consequently not a solved web agent. It is a task definition, dataset, representation method, action-sensitive evaluation framework, and extensive baseline showing that realistic, conversational website navigation remains difficult—especially on unfamiliar websites, subcategories, geographies, and dialogues where the instructor cannot see the screen.

# 2. Document Roadmap

The work is a combined **dataset/benchmark, machine-learning method, and empirical evaluation paper**.

| Part | Role in the argument |
|---|---|
| Abstract and §1, pp. 1–3 | Defines conversational web navigation, motivates WEBLINX, and states four contributions |
| §2, pp. 3–4 | Positions WEBLINX against web-agent benchmarks, webpage representations, and conversational interfaces |
| §3, pp. 4–5 | Defines the dataset, collection roles, action/state representation, and evaluation splits |
| §4, p. 5 | Defines intent, element, text, turn-level, and aggregate metrics |
| §5, pp. 5–6 | Introduces DMR/OTR and the model taxonomy |
| §6, pp. 7–8 | Reports aggregate quantitative results and qualitative errors |
| §7–§8, pp. 8–9 | Interprets findings, states limitations, concludes, and proposes future work |
| Impact Statement, p. 9 | Discusses employment, malicious use, unintended actions, supervision, and data-collection ethics |
| References, pp. 10–16 | Bibliography; compressed here as non-empirical support material |
| Contents, pp. 17–18 | Maps the main paper and appendices |
| Appendix A, pp. 19–26 | Dataset statistics, categories, processing, collection, action space, and all website entry points |
| Appendix B, pp. 27–35 | OTR, truncation, DMR equations/speed, prompts, implementations, hyperparameters, and examples |
| Appendix C, pp. 36–42 | Representation, modality, scale, generalization, qualitative, human-agreement, and prompting analyses |
| Appendix D, pp. 43–47 | Complete per-intent and grouped results by split |
| Appendix E, pp. 48–50 | Operational instructions given to annotators |

## Inventory

- **Figures:** F1–F11.
- **Tables:** T1–T30.
- **Major mathematical objects:** demonstration sequence definition; state/input processing function; intent match; IoU-based element score; chrF/URLF text score; text-input product score; DMR cosine-loss equation; two computational-complexity expressions; two human-agreement equations.
- **Algorithms/procedures without formal pseudocode:** DMR candidate selection, OTR construction, strategic truncation, output parsing, coordinate-to-element mapping, URL segmentation, collection/curation pipeline.
- **Distinct analyses:** benchmark comparison; candidate-ranker recall and speed; representation ablation; modality comparison; model-size comparison; in-domain/out-of-domain evaluation; four OOD split analyses; qualitative action errors; human agreement; in-context prompt augmentation; per-intent breakdowns.
- **Explicit formal hypotheses:** none.
- **Central informal research question:** whether conversational-assistant models can directly navigate websites in the user’s browser while retaining dialogue capability (p. 1, §1).

# 3. Background and Context

A webpage is represented internally by HTML organized as a **Document Object Model (DOM)** tree. A visible control may be associated with a tag, attributes, text, an XPath describing its tree location, and a bounding box locating it on screen. Real pages often contain many irrelevant or nested elements, making the full DOM expensive to process (pp. 2, 5–6).

A web-navigation agent must perform **grounding**: connect an instruction such as “click the 4:15 article” to the correct page element. WEBLINX adds dialogue: the task is not assumed to be completely specified in the first instruction. The system may need to ask questions, acknowledge instructions, or respond while acting (pp. 1–5).

The paper distinguishes three input modalities (p. 6; Appendix B.3):

- **Text-only:** instructions, recent history, pruned DOM, and candidate-element descriptions.
- **Image-to-text:** a screenshot is the main input; instructions and history are rendered into its header.
- **Multimodal:** both screenshot and structured textual information are provided.

Because different actions require different notions of correctness, the paper does not use one exact-match metric. A click is judged by spatial overlap, while generated text and URLs are judged by F1-like similarity. These turn-level measures are proxies for similarity to a recorded human action, not proof that the full real-world task succeeded (p. 5, §4).

According to the authors’ related-work account (§2):

- Simulated systems such as MiniWoB++ simplify the environment but transfer poorly to realistic websites.
- WebShop, Mind2Web, WebArena, VisualWebArena, and WebVoyager move toward realistic navigation but do not provide WEBLINX’s combination of real websites and multi-turn dialogue.
- RUSS and META-GUI include dialogue but are specialized or mobile-focused.
- Earlier DOM compression used rules, accessibility trees, graphs, or learned representations.
- WEBLINX positions DMR as a fast learned element-selection mechanism and the benchmark as a general dialogue-enabled counterpart to task-specific resources.

These are the authors’ descriptions of prior work, not an external literature review.

# 4. Research Problem and Gap

## Existing problem

Current assistants may browse through website-specific plugins, but those plugins must be separately implemented and may expose only part of a website’s functionality. Direct browser control could be more general, but real webpages are large, visually complex, dynamic, and varied (pp. 1–3).

## Shortcomings attributed to previous approaches

The authors identify four principal deficiencies:

1. Many benchmarks use simplified, simulated, mobile, or specialized environments rather than broad real websites.
2. Most web-agent tasks are self-contained rather than revised through multi-turn conversation.
3. Entire DOM trees can exceed practical context, latency, and cost constraints.
4. Task-success metrics are unsuitable when the goal evolves during a dialogue and when multiple actions could plausibly advance it (pp. 2–5).

## Research gap

The claimed gap is the absence of a large, expert-created benchmark simultaneously offering:

- real websites;
- general task coverage;
- browser control;
- multi-turn dialogue;
- sufficiently detailed state recordings;
- systematic in-domain and multiple out-of-domain evaluations (Tables 1–2).

## Motivation

The proposed capability could assist visually impaired users, enable voice-controlled browsing, and reduce repetitive knowledge-work steps while preserving human steering. Scientifically, it tests whether agents can combine language understanding, environmental interaction, conversational updating, and transfer to unforeseen settings (p. 2).

## Scope

The paper evaluates imitation of recorded next actions from static demonstrations. It does not deploy agents to autonomously complete live tasks, measure end-to-end task success, explore alternative trajectories, or authorize consequential real-world transactions (pp. 5, 8–9; Appendix E).

# 5. Research Questions / Objectives / Hypotheses

## Explicit research question

- **RQ1:** Can the models underlying conversational assistants navigate websites directly in a user’s browser while retaining conversational capabilities? (p. 1, §1)

## Author-stated objectives

- Define real-world conversational web navigation.
- Construct a large, diverse expert benchmark.
- represent large webpages compactly enough for practical model input.
- Design action-specific turn-level evaluation metrics.
- Compare text-only, image-only, and multimodal models under zero-shot and finetuned conditions.
- Test generalization to unseen websites, subcategories, geographies, and a visionless-instructor condition.
- Examine representative model errors and compare selected models with alternative human actions.

## Implicit empirical questions, not formally labeled by the authors

- Does DMR/OTR improve action modeling relative to MindAct-style formatting?
- How do image-only, multimodal, and text-only systems compare?
- How much does model size matter before and after finetuning?
- How large is the in-domain/out-of-domain gap?
- Do descriptions and in-context action examples improve zero-shot prompting?

## Hypotheses

The paper states no formal preregistered hypotheses. It presents design motivations and empirical expectations, but these should not be relabeled as formal hypotheses.

# 6. Assumptions / Threat Model

This is not a cybersecurity paper with a formal attacker model. Its operative system assumptions are:

- A human instructor communicates only through chat; a human or modeled navigator controls the browser (Figures 1, 3, 6).
- The instructor normally sees the screen, except in `TEST_VIS`.
- A state may include candidates \(c_t\), DOM \(d_t\), screenshot \(i_t\), instructor utterance \(u_t\), viewport \(v_t\), and history \(h_t\), but not every component is always present (pp. 4–5).
- Models see a restricted history: the first instructor utterance, the latest four additional instructor utterances, and the last five actions/turns, depending on the template (p. 5; Appendix A.3, B.5).
- DMR’s top ten elements are assumed sufficient for candidate-based action prediction.
- Static demonstrations are treated as reference trajectories. The automatic score estimates similarity to those references, not true online success.
- Vision models selecting coordinates are mapped to the smallest-area overlapping element because CSS z-index information is unavailable (Appendix A.4).
- Recorded tasks stop before consequential actions such as purchases or reservations are finalized (Appendix E, p. 50).
- Human supervision is required; the authors expressly state that the released models should be used for research and not deployed (p. 9).

The impact statement identifies malicious automation, impersonation, spam, and costly unintended actions as risks, but it does not experimentally evaluate attacks or defenses.

# 7. Methodology

## 7.1 Study design

The work combines:

1. expert collection of conversational browser demonstrations;
2. preprocessing into synchronized states and actions;
3. learned candidate retrieval;
4. supervised finetuning or zero-shot prompting of action models;
5. turn-level offline evaluation;
6. aggregate, split-specific, qualitative, and small-scale human-agreement analyses.

## 7.2 Dataset collection

Eight trained expert annotators worked in instructor–navigator pairs through Zoom chat. Only the navigator controlled Chrome. A custom extension recorded screenshots, DOM trees, visible-element bounding boxes, browser actions, and tab state. Zoom supplied screen recording and chat. A custom interface supported upload and review (pp. 4, 22–23; Figures 3 and 6).

Quality control included:

- removing unnecessary actions;
- correcting asynchronously misordered events;
- correcting typographical errors;
- realigning screenshots to video frames;
- marking states invalid if the screenshot lacked sufficient information for the action;
- validation by a different annotator under the original navigator’s supervision.

Recording paid US$7.50/hour; preparation, upload, and review paid US$5/hour; reported average cost was US$2.58 per demonstration (Appendix A.5, p. 23).

## 7.3 Data composition

The benchmark contains 2,337 demonstrations over 155 website entry points, 15 geographic areas, 8 categories, and 50 subcategories (§3). Table 8 gives the actual mutually exclusive split counts:

| Split | Demos | Mean turns | SD turns | Active turns | Total turns |
|---|---:|---:|---:|---:|---:|
| Train | 969 | 44.93 | 17.37 | 24,418 | 43,538 |
| Validation | 100 | 40.76 | 14.51 | 1,717 | 4,076 |
| Test IID | 100 | 43.18 | 16.08 | 1,846 | 4,318 |
| Test CAT | 223 | 45.30 | 25.43 | 4,979 | 10,102 |
| Test WEB | 211 | 40.47 | 18.17 | 4,184 | 8,540 |
| Test VIS | 444 | 36.05 | 20.09 | 7,725 | 16,006 |
| Test GEO | 290 | 48.05 | 18.66 | 6,141 | 13,934 |

The counts sum to 2,337 demonstrations and 100,514 total turns **[C: 969+100+100+223+211+444+290; 43,538+4,076+4,318+10,102+8,540+16,006+13,934]**.

Figure 2 instead labels Train 1,404, Valid 140, Test-IID 146, and Test-OOD 1,692. Those counts sum to 3,382, not 2,337. The most plausible explanation is category-linked counting with multi-category demonstrations, but the figure caption calls them “demonstrations” and does not explain the discrepancy. It is therefore reported as an unresolved figure–table inconsistency.

## 7.4 Action and state representation

A demonstration is

\[
D=\{s_1,a_1,\ldots,s_n,a_n\},
\]

with state \(s_t\) and action \(a_t\) at turn \(t\) (p. 4). Five core modeled intents are `click`, `load`, `say`, `submit`, and `textinput` (Table 3). Thirteen intent types were recorded (Table 6); `change` and `scroll` are also finetuning targets, while copy/paste/hover/tab operations remain available in history.

Table 7’s dominant recorded actions are `say` (39,305 turns) and `click` (33,865), followed by copy (6,477), text input (4,799), scroll (3,999), and load (3,702). The table’s 13 action totals sum to 100,514 **[C]**, matching Table 8’s total-turn sum.

## 7.5 Dense Markup Ranking

For each turn, DMR encodes the processed state and each candidate element separately, trains cosine similarity toward a binary target, ranks all candidates, and returns the top \(k=10\). MiniLM was selected as the ranker backbone after comparison with BGE, GTE, and the MindAct DeBERTa cross-encoder (Appendix B.4; Table 13).

Its motivations are:

- independent encodings avoid the cross terms of concatenated cross-encoder attention;
- compact retrievers reduce latency;
- retained candidates let the larger action model focus on decision making.

## 7.6 Optimal Text Representation and truncation

OTR adds four elements to the earlier representation:

- HTML attributes and values;
- viewport dimensions;
- candidate XPath and bounding box;
- stable element IDs rather than alphabetical labels.

Inputs are strategically truncated by component rather than cut blindly. The method preserves structural fields, treats content as subcomponents, and finds a length threshold that disproportionately shortens only long subcomponents. The target is 2,048 tokens: 700 for the DOM, 40 per utterance, 50 per action, 65 per candidate, and approximately 248 for the prompt (Appendix B.1–B.2, B.7).

## 7.7 Output processing

Generated text is searched with a regular expression for the first valid intent call and parsed into key/value arguments. Screenshot-only coordinate predictions are mapped to page elements. URLs are segmented into normalized network location and slash-delimited path components before URL F1 evaluation (Appendix A.4).

## 7.8 Models and baselines

Nineteen variants from eight architectural families are reported:

- MindAct: 250M, 780M, 3B;
- Flan-T5 with OTR: 250M, 780M, 3B;
- Pix2Act/Pix2Struct: 282M, 1.3B;
- Sheared-LLaMA: 1.3B, 2.7B;
- LLaMA-2 chat: 7B, 13B, plus zero-shot LLaMA variants in detailed tables;
- Fuyu: 8B;
- GPT-3.5 Turbo: zero-shot and finetuned;
- GPT-4 Turbo: zero-shot;
- GPT-4V: zero-shot.

The count “19 models” refers to variants; the paper’s “eight architectures” groups related sizes/settings.

## 7.9 Training configuration

Each open model was finetuned once because of computational cost; the authors report a fixed seed and no task-specific random initialization (Appendix B.6). Common settings were:

- linear learning-rate scheduler;
- 256 maximum output tokens;
- bfloat16 precision;
- AdamW optimizer;
- Fully Sharded Data Parallel for models of 7B parameters or more;
- training learning rate generally \(5\times10^{-5}\), except Pix2Act at \(2\times10^{-5}\);
- three epochs for LLaMA, Sheared-LLaMA, Fuyu, and GPT-3.5F;
- five epochs for Flan-T5, MindAct, and Pix2Act;
- FlashAttention-2 for LLaMA-family models;
- 100 warm-up steps only for Pix2Act in Table 14.

No confidence intervals, hypothesis tests, multiple seeds, or statistical significance tests are reported.

# 8. Experiments / Analyses

## X1 — Benchmark comparison

**Purpose:** establish novelty relative to prior datasets.  
**Evidence:** Table 1, p. 2.  
WEBLINX is the only listed benchmark marked yes for multi-turn chat, general tasks, and web browsing simultaneously. It has 155 domains, 2,337 instances, 1,775 average HTML elements, and 43.0 average turns. The comparison depends on the authors’ selected benchmark set and categorizations.

## X2 — Candidate-ranker quality and speed

**Purpose:** test whether DMR is fast enough while retaining relevant elements.  
**Setup:** BGE, GTE, MiniLM dual encoders versus a DeBERTa cross-encoder; Recall@10 across ID and four OOD splits (Table 13).  
**Result:** DeBERTa has the best OOD Recall@10, 54.78; MiniLM obtains 51.87. MiniLM requires 186 ms per active training turn versus 916 ms for DeBERTa (Appendix B.4.1).

**[C] Derived:** DeBERTa’s absolute recall advantage is 2.91 points (54.78−51.87), while DMR’s reported time ratio is 916/186 ≈ 4.92×, consistent with “five times faster.” The total runtimes, 22,385/4,545 ≈ 4.93×, independently agree.

## X3 — Representation comparison

**Purpose:** isolate the effect of OTR versus MindAct/Mind2Web formatting on the same Flan-T5 sizes.  
**Data:** validation split; Table 16.  
**Results:**

- 250M: overall 21.91 vs 17.78;
- 780M: 23.94 vs 21.39;
- 3B: 31.97 vs 27.86.

The 3B OTR system also improves IM from 79.91 to 82.00, IoU from 24.24 to 31.18, and text F1 from 24.79 to 27.81.

**[C] Derived:** the 3B overall gain is 4.11 points, or approximately 14.75% relative to 27.86. Because several representation and candidate-processing details differ, this supports the bundled OTR design rather than any single OTR field.

## X4 — Image-only versus multimodal models

**Purpose:** assess screenshot-only and image-plus-text input.  
**Evidence:** validation, Table 17.

- Pix2Act-282M: 14.39 overall;
- Pix2Act-1.3B: 24.21;
- Fuyu-8B: 31.60;
- zero-shot GPT-4V: 14.26.

Fuyu has the strongest overall and element IoU (26.34); Pix2Act-1.3B has the strongest IM (83.40) and text F1 (31.61). GPT-4V is not finetuned, so architecture, scale, information access, and training regime are confounded.

## X5 — Decoder size and finetuning

**Purpose:** compare scale and adaptation among text-only decoder models.  
**Evidence:** validation, Table 18.

Zero-shot performance rises from LLaMA-2-13B 6.07 to GPT-3.5T 11.48 and GPT-4T 13.75. After finetuning, Sheared-LLaMA-2.7B scores 35.47, LLaMA-2-13B 38.03, and GPT-3.5F 28.98.

**[C] Derived:** finetuned LLaMA-2-13B exceeds Sheared-LLaMA-2.7B by only 2.56 points on validation despite having about 4.8 times as many parameters (13/2.7). This is descriptive, not a controlled parameter-efficiency proof.

## X6 — Aggregate model comparison

**Purpose:** rank the major systems under in-domain and out-of-domain evaluation.  
**Evidence:** Table 4 and corrected/more precise Appendix Table 28.

Out-of-domain leaders are LLaMA-2-13B (25.21) and Sheared-LLaMA-2.7B (25.02). The best zero-shot system is GPT-4T (10.72), narrowly above GPT-4V (10.45). Fuyu reaches 19.97, Pix2Act-1.3B 16.88, Flan-T5-3B 23.77, and GPT-3.5F 21.22.

## X7 — Generalization across OOD conditions

**Purpose:** distinguish unfamiliar websites, categories, geographies, and instructor visibility.  
**Evidence:** LLaMA-2-13B in Table 5:

- `TEST_WEB`: 27.0;
- `TEST_CAT`: 24.3;
- `TEST_GEO`: 25.9;
- `TEST_VIS`: 25.0.

The paper calls `TEST_CAT` the hardest for this model. Appendix Tables 29–30 show that “hardest split” varies somewhat by model, so it should not be generalized universally.

## X8 — Qualitative action assessment

**Purpose:** inspect errors hidden by aggregate scores.  
**Evidence:** Figures 4, 9–11 and Table 19.

Observed error types include:

- selecting a wrong time-specific link;
- restarting a subtask whose dialog is already open;
- choosing a theoretically possible but less efficient route;
- clicking an inert heading;
- confusing recipient, subject, username, and password fields;
- repeating text already entered;
- failing to perform the second stage of a multistep request;
- forgetting information supplied earlier;
- producing an irrelevant link or refusing a feasible request;
- receiving a low reference-based score for a pragmatically reasonable alternative question.

This analysis uses selected examples rather than a systematic error-frequency sample.

## X9 — Human-alternative agreement

**Purpose:** allow multiple plausible next actions rather than only the original action.  
**Data:** 402 new annotations from three annotators over 134 validation turns (Table 20).  
**Results:** original navigator 48.07 overall; annotator mean 46.62; LLaMA-2-13B 31.45; Fuyu 26.24; GPT-4T 16.90; GPT-4V 14.95. Normalized to the original, these are 65.42%, 54.58%, 35.15%, and 31.09%.

This is a subset of validation, not a complete test-set human baseline.

## X10 — In-context examples

**Purpose:** test whether per-action descriptions and examples improve non-finetuned systems.  
**Evidence:** Test IID, Table 21.

- GPT-3.5T falls from 10.87 to 8.50.
- GPT-4V falls from 13.52 to 13.04.
- GPT-4V without screenshot scores 12.33.

The authors conclude that differences are not substantial. Table 21 contains no D&E GPT-4T row, despite the zero-shot section containing GPT-4T.

## X11 — Per-intent and per-split analysis

Appendix Tables 22–27 provide click, submit, text-input, say, and load argument scores and intent matches for IID and every OOD split. Tables 28–30 aggregate them into overall, IM, element IoU, and text F1. They show, among other patterns, that:

- several small finetuned systems predict `say` intent almost perfectly but have much lower textual similarity;
- zero-shot GPT models are comparatively stronger on text-input argument metrics than on `say` text;
- screenshot-only Pix2Act often has high click intent match but weak click-element overlap;
- LLaMA models are much stronger on submit and load arguments than many smaller baselines;
- no one model dominates every action and split.

# 9. Results

## 9.1 Finetuning dominates zero-shot use

The strongest zero-shot OOD score is 10.72 for GPT-4T. The best finetuned score is 25.21 for LLaMA-2-13B (Table 28).

**[C] Derived:** absolute difference 14.49 points; relative increase over GPT-4T approximately 135.2% \((25.21-10.72)/10.72\). This is not a pure finetuning effect because model families differ.

Within LLaMA-2-13B, zero-shot OOD is 5.16 and finetuned OOD is 25.21, an absolute increase of 20.05 points **[C]** (Table 28), providing a more direct but still not necessarily hyperparameter-controlled comparison.

## 9.2 Text-only decoders lead the evaluated multimodal systems

On OOD:

- LLaMA-2-13B: 25.21;
- Sheared-LLaMA-2.7B: 25.02;
- Fuyu-8B: 19.97;
- Pix2Act-1.3B: 16.88;
- GPT-4V zero-shot: 10.45 (Table 28).

This establishes leadership among the evaluated configurations, not a universal result about all multimodal models. GPT-4V was not finetuned, and Pix2Act lacked the candidate-rich text input used by text-only systems.

## 9.3 OTR improves the Flan-T5 baseline

On validation, Flan-T5-3B with OTR reaches 31.97 versus MindAct-T5-3B at 27.86 (Table 16). Improvements occur in all reported metrics. The paper attributes this to careful input construction for large DOMs and longer history.

## 9.4 DMR trades modest recall for much lower latency

MiniLM DMR reaches 51.87 OOD Recall@10 versus DeBERTa’s 54.78, but candidate retrieval declines from 916 ms to 186 ms per turn (Table 13; Appendix B.4.1). This keeps retrieval itself below the paper’s cited one-second interaction target, although full agent latency—including generation and networking—was not measured.

## 9.5 Strong in-domain performance does not transfer fully

For LLaMA-2-13B, overall score falls from 37.09 IID to 25.21 OOD, a 11.88-point absolute decrease and approximately 32.0% relative reduction **[C]** (Table 28). For Sheared-LLaMA-2.7B, the decline is 12.41 points (37.43 to 25.02), approximately 33.2% **[C]**.

The pattern holds across all finetuned models in Table 28, supporting the authors’ generalization concern.

## 9.6 Model scale matters less after finetuning

On IID, LLaMA-2-7B actually has a slightly higher overall score than LLaMA-2-13B: 38.12 versus 37.09. On OOD, 13B is slightly higher: 25.21 versus 24.57 (Table 28). Sheared-LLaMA-2.7B is also very close at 25.02. Thus parameter count does not yield a monotonic or large improvement among these finetuned decoder configurations.

## 9.7 Screenshots do not automatically improve action prediction

GPT-4V scores 12.99 IID and 10.45 OOD versus GPT-4T’s 12.24 and 10.72 (Table 28): vision helps slightly IID but is slightly worse OOD. With D&E prompting on Test IID, GPT-4V scores 13.04 and its no-screenshot variant 12.33 (Table 21). These differences are small and do not demonstrate robust screenshot benefit.

## 9.8 Human-level next-action agreement remains distant

LLaMA-2-13B receives 65.42 normalized overall agreement against original and alternative human actions. Fuyu receives 54.58; GPT-4T 35.15; GPT-4V 31.09 (Table 20). The evaluation makes the reference more permissive, yet a substantial gap remains.

## 9.9 Metrics can penalize valid alternatives

The qualitative `say` examples show that a model may ask a different but pragmatically useful clarification from the recorded human question. Character-based F1 can score such a response poorly despite its plausibility (pp. 39–40). This is direct evidence that the benchmark’s automatic metrics are useful heuristics but incomplete measures of interactive quality.

# 10. Figure-by-Figure Interpretation

## Figure 1 — Example conversational navigation task

- **Visual type:** two-column sequence of chat messages, browser screenshots, and structured actions.
- **Content:** creating a “Career Fair” Google Calendar task, with the instructor later adding “Bring multiple copies of my resume.”
- **Encoding:** blue bubbles are instructor messages; gray items are navigator actions/responses; screenshots show target regions.
- **Support:** demonstrates that the objective evolves and that an agent alternates browser actions with natural-language exchanges.
- **Caveat:** illustrative example, not performance evidence.
- **Status:** [B] visually inspected, p. 1.

## Figure 2 — Demonstration distribution

- **Visual type:** Sankey/alluvial diagram.
- **Flow:** split groups on the left connect to eight task categories on the right; link width represents frequency.
- **Categories:** AI Tools, Booking, Composing, Information Lookup, Productivity, Shopping, Social Interaction, Summarizing.
- **Observation:** Booking and AI Tools receive especially substantial flows; all splits span several categories.
- **Uncertainty:** displayed split labels sum to 3,382 rather than the 2,337 unique demonstrations in Table 8. Because demonstrations may carry multiple categories, the graphic may count category assignments, but neither its caption nor nearby text says so.
- **Status:** [B], p. 3.

## Figure 3 — Pairwise collection setup

- **Components:** instructor, navigator, browser.
- **Control flow:** instructor instructs navigator; navigator replies; navigator controls the browser.
- **Visibility:** the browser provides views to the instructor except in `TEST_VIS`.
- **Meaning:** separates conversational authority from browser control.
- **Status:** [B], p. 4.

## Figure 4 — Six qualitative examples

- **Panels:** C1–C2 click, T1–T2 text input, S1–S2 dialogue.
- **Color:** red marks incorrect model output; blue marks references/correct actions.
- **Observations:** GPT-4V confuses time links, repeats an already-open workflow, confuses form-field roles, and generates irrelevant dialogue. Finetuned LLaMA handles these selected cases better.
- **Caveat:** selected examples are not frequency estimates. The caption refers broadly to “predicting click actions” although the figure also contains text-input and `say` panels—a caption–content wording inconsistency.
- **Status:** [B], p. 8.

## Figure 5 — Full action-space diagram

- **Components:** ten browser actions and one chat action displayed as small control icons.
- **Arguments:** strings, integers, elements, or tab IDs.
- **Relationship:** visual summary of Table 6; it distinguishes browser operations from `say`.
- **Caveat:** Table 6 has 13 intent types because click and hover each have UID and coordinate forms, while Figure 5 groups those forms conceptually.
- **Status:** [B], p. 19.

## Figure 6 — End-to-end collection pipeline

- **Components:** instructor, navigator, browser, recording, post-processing, web interface, dataset.
- **Flow:** the instructor instructs and receives replies; navigator controls the browser and uploads records; browser interactions are recorded; uploaded artifacts are post-processed into the dataset.
- **Visibility path:** browser views go to instructor except in `TEST_VIS`.
- **Method connection:** expands Figure 3 from roles into data production.
- **Status:** [B], p. 22.

## Figure 7 — Pix2Act input

- **Content:** viewport dimensions and dialogue/action history rendered above an Encyclopedia.com screenshot.
- **Meaning:** shows how a nominally image-only model receives language—as pixels in the screenshot header rather than separate text tokens.
- **Status:** [B], p. 32.

## Figure 8 — Highlighted target element

- **Content:** Encyclopedia.com page with the search box highlighted.
- **Meaning:** grounds the sample state and output table; correct next action is a click on the search field because “biotechnology” is already represented as the pending instruction and the workflow’s reference next step is focus/click.
- **Caveat:** the visual alone cannot determine that reference without the associated history and Table 15.
- **Status:** [B], p. 34.

## Figure 9 — Submit-versus-repeat error

- **Content:** a restaurant-search form whose location field is already populated.
- **Observation:** reference action is the green submit/search control; GPT-4T predicts typing a date and GPT-4V repeats the existing location, while LLaMA-2.7B submits.
- **Support:** illustrates state-awareness failure even when page text is readable.
- **Status:** [B], p. 34.

## Figure 10 — Extended click assessment

- **Panels:** four scenarios: time-specific news tab, open delivery-details dialog, email composition route, top-questions filtering.
- **Observation:** LLaMA wins the first three selected comparisons; GPT-4V wins the fourth, where LLaMA clicks an inert heading.
- **Importance:** prevents the qualitative claim from becoming one-sided: finetuned LLaMA also fails.
- **Status:** [B], p. 38.

## Figure 11 — Extended text-input assessment

- **Panels:** email subject, login password, translation-language change, long-context post drafting.
- **Observation:** GPT-4V confuses semantic roles in the first two. Both systems fail the translation step. Both omit previously supplied title information in the fourth panel, although LLaMA correctly adds the currently requested introduction.
- **Status:** [B], p. 39.

No substantive conventional plots with numerical axes, error bars, or confidence bands appear; the figures are examples, flow diagrams, or a distribution diagram.

# 11. Table-by-Table Interpretation

## Table 1 — Benchmark comparison

Compares dialogue, generality, browser use, domains, instances, average element count, turns, and setting. WEBLINX is the only listed benchmark with all three capability checks and has the longest reported average interaction, 43.0 turns. Missing values are shown as dashes. AITW’s 30K refers to unique prompts with multiple demonstrations.

## Table 2 — Split definitions

Defines Train, Valid, Test IID, and four OOD tests: unseen websites (`WEB`), unseen subcategories (`CAT`), unseen geographies (`GEO`), and instructor without screen access (`VIS`). It is foundational for interpreting every result table.

## Table 3 — Core action space

Lists the five evaluated core intents and their meanings. It compresses the fuller 13-intent observed space in Table 6.

## Table 4 — Main aggregate results

Reports IM, element IoU, text F1, OOD overall, and IID overall for 11 representative models. LLaMA-2-13B and Sheared-LLaMA-2.7B lead OOD; Sheared-LLaMA-2.7B leads the displayed IID column at 37.4. Values are rounded relative to Table 28.

## Table 5 — LLaMA-2-13B across OOD splits

`TEST_WEB` has the strongest overall score, 27.0; `TEST_CAT` the weakest, 24.3. `TEST_VIS` has the strongest IM and IoU but weakest text F1, consistent with a different dialogue condition.

## Table 6 — Complete observed action space

Defines 13 recorded intents, their arguments, descriptions, listeners, and browser event/API triggers. It clarifies that agents may only generate navigator speech and that tab actions belong to Chrome tabs.

## Table 7 — Action frequencies

Shows demonstration incidence, mean/SD turns per applicable demo, and totals. `say` and `click` dominate. `change` is rarest at 322 total turns. The totals reproduce the benchmark’s 100,514 turns.

## Table 8 — Split statistics

Provides the authoritative unique-demo counts and active versus history-inclusive turns. `TEST_VIS` has fewer mean turns (36.05), which the authors attribute to reduced screen-dependent follow-up. `TEST_GEO` has the highest mean, 48.05.

## Table 9 — AI-tool usage

Of 2,337 demonstrations, 280 use AI tools and 2,057 do not. AI-tool demonstrations average 46.79 turns versus 42.50. No causal conclusion is warranted.

## Table 10 — `TEST_CAT` subcategories

Lists subcategories assigned to the category-generalization split and compares them with other splits. The “Difference” row isolates Handmade, Reviews, Computer Vision, Professional Network, and Geography as unique to `TEST_CAT`; other `TEST_CAT` entries also appear elsewhere.

## Table 11 — Category/subcategory counts

Provides all 50 subcategories by split and URL count. Demonstrations may occur in multiple rows because they can use multiple websites. Transport is especially frequent (757), while Furniture has 6; Research Directory has 10. These are overlapping incidence counts, not a class partition.

## Table 12 — Website inventory

Lists all 155 entry points, category, subcategory, geography, and URL across pp. 24–26. It demonstrates domain diversity and includes both popular and lesser-known sites. The list was visually inspected on all three rendered pages but is deliberately not reproduced row by row.

## Table 13 — Candidate rankers

DeBERTa has the highest Recall@10 everywhere: ID 76.86 and OOD 54.78. MiniLM is the strongest dual encoder OOD at 51.87 and is selected for efficiency. No confidence intervals are shown.

## Table 14 — Hyperparameters

Lists model size, epochs, batch, learning rate, accumulation, warmup, vision, and FlashAttention-2. It supports reproducibility but also reveals that model families use different effective batch configurations and epoch counts.

## Table 15 — One-state outputs

Most finetuned text models and Fuyu click the correct input. Zero-shot GPT-3.5T, GPT-4T, and GPT-4V type “biotechnology” prematurely. Pix2Act-1.3B’s coordinate is near the target; Pix2Act-282M’s coordinate is incorrect. The example illustrates the difference between understanding the task and selecting the immediate next action.

## Table 16 — MindAct formatting versus OTR

All three Flan-T5 sizes with OTR beat matched-size MindAct configurations in overall score. The largest absolute overall improvements occur at 250M (4.13) and 3B (4.11) **[C]**.

## Table 17 — Visual-model comparison

Fuyu-8B has the best overall and element score; Pix2Act-1.3B has the best intent and marginally best text score. GPT-4V is disadvantaged by being zero-shot.

## Table 18 — Decoder scale/adaptation

Shows weak zero-shot open LLaMA performance and large gains after finetuning. LLaMA-2-13B is best overall on validation; Sheared-LLaMA-2.7B is close despite smaller size.

## Table 19 — `say` examples

Shows style mismatch, irrelevant-link generation, unsupported refusal, and an alternative but defensible clarification. It directly motivates caution when interpreting lexical F1.

## Table 20 — Human and model agreement

Three alternative human annotators score close to the original reference. LLaMA is the strongest model but reaches only 65.42 normalized overall. The sample is limited to 134 validation turns.

## Table 21 — Prompt examples

Descriptions and examples do not consistently improve Test IID. GPT-3.5T worsens, GPT-4V changes little, and removing GPT-4V’s screenshot reduces performance slightly. The evaluated D&E rows are incomplete across model families.

## Tables 22–27 — Full per-intent results

These six tables provide IID, OOD average, CAT, GEO, VIS, and WEB results. Each separates zero-shot and finetuned systems and reports argument quality plus per-intent IM. They are essential for diagnosing whether failure is caused by choosing the wrong action or the wrong argument. Because they contain hundreds of cells, they are represented in compressed form rather than reproduced verbatim.

Notable table-only patterns include:

- On IID, Fuyu’s submit IoU is 62.21, while LLaMA-2-7B’s is 82.76 (Table 22).
- On OOD, LLaMA-2-13B has the strongest displayed load F1 among finetuned models at 33.55, while LLaMA-2-7B has higher text-input IM, 64.99 versus 62.06 (Table 23).
- On `TEST_CAT`, LLaMA-2-13B reaches submit IoU 51.53 and text-input IoU 57.11, but its click IM is only 84.98 compared with many smaller finetuned systems above 90 (Table 24).
- On `TEST_VIS`, LLaMA-2-7B exceeds 13B on text-input IoU and IM, while 13B is slightly stronger on `say` chrF (Table 26).
- On `TEST_WEB`, GPT-3.5F has the strongest displayed text-input IM at 68.69 and load F1 at 41.20, despite weaker overall performance (Table 27).

## Tables 28–30 — Grouped split results

These consolidate overall, IM, element IoU, and text F1 for IID/OOD, CAT/GEO, and VIS/WEB. They are the cleanest source for cross-model comparisons. LLaMA-family finetuned systems lead most overall conditions, but the leading variant changes:

- IID: LLaMA-2-7B, 38.12;
- OOD aggregate: LLaMA-2-13B, 25.21;
- CAT: Sheared-LLaMA-2.7B, 25.06;
- GEO: LLaMA-2-13B, 25.93;
- VIS: LLaMA-2-13B, 25.00;
- WEB: LLaMA-2-13B, 27.00.

No table reports uncertainty intervals or significance markers.

# 12. Diagram / Architecture Interpretation

The paper’s operational architecture can be summarized as:

1. **Human data generation:** an instructor gives or revises instructions; a navigator converses and manipulates Chrome.
2. **Capture:** a browser extension records DOMs, screenshots, bounding boxes, events, and tabs; Zoom records chat/video.
3. **Curation:** records are synchronized, cleaned, visually aligned, and validity-checked.
4. **State construction:** current page information and bounded history form \(s_t\).
5. **Candidate retrieval:** DMR compares the processed state against individual DOM elements and returns the top ten.
6. **Input construction:** OTR combines the pruned DOM, candidate metadata, viewport, and conversation/action history; visual systems also receive a screenshot.
7. **Action generation:** a model outputs a structured intent call.
8. **Parsing and grounding:** arguments are parsed; coordinates or URLs are normalized where necessary.
9. **Offline scoring:** predicted next action is compared with the recorded next action using intent, spatial, and textual similarity.

The control path in data collection is human-to-human; the model evaluation path later imitates the navigator. There is no evaluated feedback loop in which a model action changes a live browser and generates a new state. That distinction explains the authors’ “static demonstrations” limitation.

# 13. Equations and Mathematical Concepts

## E1 — Demonstration sequence

\[
D=\{s_1,a_1,\ldots,s_n,a_n\}.
\]

A demonstration contains alternating states and actions. At turn \(t\), the model observes a representation of \(s_t\) and predicts \(a_t\) (p. 4).

## E2 — Model-specific processing function

\[
P_m(s_t,a_{1:t-1}).
\]

Appendix A.3 defines a preprocessing function tailored to model \(m\). It maps the current state and prior actions into the model’s input representation. Different modalities receive different subsets or renderings.

## E3 — Intent Match

\[
IM(a',a)=
\begin{cases}
1,&\text{if predicted and reference intents match}\\
0,&\text{otherwise.}
\end{cases}
\]

This evaluates action type only—not whether the target element or text is correct (p. 5).

## E4 — Element similarity

The displayed formula is:

\[
IM(a',a)\times
\frac{B_{\text{reference}}\cap B_{\text{predicted}}}
     {B_{\text{reference}}\cup B_{\text{predicted}}}.
\]

Here \(B\) denotes bounding-box area. This is Intersection over Union (IoU), gated by intent correctness. Exact overlap scores 1; disjoint boxes or wrong intents score 0. Partial overlap lies between 0 and 1.

## E5 — Text and URL similarity

For `say` and `textinput`:

\[
IM(a',a)\times chrF(a',a),
\]

where chrF is character \(n\)-gram F1 with \(n=6\). For `load`, URL components replace character \(n\)-grams, producing `URLF`. Intent gating makes a textually similar argument score zero if attached to the wrong action.

## E6 — Turn and overall score

- Element actions (`click`, `submit`) use IoU.
- `load` and `say` use F1.
- `textinput` uses \(\text{IoU}\times\text{F1}\) because both target and text must be right.
- Overall is the micro-average of turn scores.

A product makes text-input performance stringent: a near-zero score in either element selection or text generation suppresses the whole turn.

## E7 — DMR training loss

\[
L_t=
\left\|
y(c_{t,i})-
\operatorname{sim}_{cos}
\left(E(P_{\mathrm{DMR}}(s_t)),E(c_{t,i})\right)
\right\|_2^2,
\]

with

\[
\operatorname{sim}_{cos}(x,y)=
\frac{x\cdot y}{\|x\|\|y\|}.
\]

\(E\) is an encoder; \(P_{\mathrm{DMR}}(s_t)\) is the processed state; \(c_{t,i}\) is candidate \(i\); and \(y(c_{t,i})\) is 1 for the target candidate and 0 otherwise. The squared loss trains cosine similarity to approximate the binary target. At inference, similarities rank candidates.

The displayed equation appears to write one candidate’s error rather than an explicit sum or mean over candidates, despite the prose calling it mean-squared error. The aggregation scope is therefore not fully shown in the formula.

## E8 — Computational complexity

Self-attention over sequence length \(n\) and embedding size \(e\) is stated as:

\[
O(n^2e).
\]

For separate state and candidate encodings, the paper gives:

\[
O(|P_{\mathrm{DMR}}(s_t)|^2+|c_{t,i}|^2),
\]

versus cross-encoder concatenation:

\[
O((|P_{\mathrm{DMR}}(s_t)|+|c_{t,i}|)^2).
\]

The dual encoder removes the positive cross term \(2|P||c|\), although the displayed expressions suppress embedding-size and multi-candidate/cache considerations.

## E9 — Human agreement

For a human prediction \(a_p\):

\[
Agreement_M(a_p,A)=
\max_{a_r\in A\setminus a_p}M(a_p,a_r).
\]

For model prediction \(\hat a\):

\[
Agreement_M(\hat a,A)=
\max_{a_r\in A}M(\hat a,a_r).
\]

\(A\) includes the original action and three alternative human annotations. The maximum credits a prediction if it resembles any plausible annotation. Excluding \(a_p\) prevents a human annotation from matching itself trivially.

# 14. Interpretation and Discussion

The benchmark’s major lesson is that next-action prediction on real websites is not solved merely by adding a large language or vision-language model. Adaptation to the task and a compact, structured page representation matter at least as much as raw model scale in the tested configurations.

DMR/OTR separates two problems:

- deciding which small subset of the page could matter;
- deciding what action to take using that subset and dialogue history.

This division makes computation tractable and improves Flan-T5 over the prior formatting baseline. It also creates a dependency: if the correct element is absent from DMR’s top ten, a candidate-based downstream model cannot select it. MiniLM’s OOD Recall@10 of 51.87 reveals substantial headroom at this stage.

The results answer the central research question cautiously. Models can imitate many human browser actions and dialogue responses, especially after finetuning, but they do not yet demonstrate dependable direct web navigation. The offline setup does not test recovery, compounding error, final success, or safety under live execution. The qualitative examples show deficient state awareness and memory even when the intended action class is correct.

The paper’s conclusion that finetuned text-only models outperform the evaluated multimodal models is supported by Tables 4 and 28–30. It should retain three qualifications:

1. the evaluated multimodal set is small;
2. GPT-4V is zero-shot rather than finetuned;
3. Pix2Act receives less explicit structured text than OTR systems.

The out-of-domain degradation strongly supports the generalization claim. However, “unseen website,” “unseen category,” “geography,” and “visionless instructor” change different factors and are not equally difficult for every model. Their aggregate should therefore not conceal split-specific behavior.

## Consistency findings

- Table 4’s values are rounded versions of Table 28 and are substantially consistent.
- Table 5’s one-decimal LLaMA-2-13B results agree with Tables 29–30.
- DMR’s per-turn and total-runtime ratios both support the approximately 5× speed claim.
- Table 7’s action totals and Table 8’s split totals both equal 100,514 **[C]**.
- Figure 2’s split counts conflict with Table 8’s unique-demo counts unless interpreted as overlapping category incidences; this is not explained.
- Main text says “over 100K occurrences,” consistent with 100,514.
- The abstract says “across 2300 expert demonstrations,” an informal rounded expression consistent with 2,337.
- The stated “average of 43 turns” is consistent with 100,514/2,337 ≈ 43.01 **[C]**.
- No formal statistical inference supports claims of superiority; comparisons are point estimates from single training runs.

# 15. Contributions and Novelty

## Conceptual

- Defines **conversational web navigation** as real-browser task completion through evolving multi-turn dialogue.

## Dataset and benchmark

- Provides 2,337 expert demonstrations, 100,514 recorded turns, and multimodal browser state across 155 real websites.
- Introduces four OOD axes plus IID evaluation.
- Supplies detailed action, website, category, and annotation metadata.

## Methodological

- Defines action-specific turn-level evaluation instead of relying on final task success.
- Introduces a small alternative-human-action evaluation to account for multiple plausible trajectories.

## Algorithmic

- Introduces DMR, a dual-encoder element ranker chosen to reduce candidate-selection latency.
- Introduces OTR and strategic component-aware truncation.

## Experimental

- Compares 19 variants spanning text-only, image-only, and multimodal approaches.
- Shows large finetuning benefits, weak scale gains after finetuning, and substantial OOD degradation.
- Provides per-intent, per-split, prompt, and qualitative analyses.

## Implementation

- Describes a custom Chrome extension, collection interface, synchronization/curation process, prompts, hyperparameters, and parsing mechanisms.
- The paper states that code, data, and models are available for research, but those external artifacts were not supplied and were not inspected.

# 16. Limitations

## Authors’ stated limitations

- **Static demonstrations:** alternative online trajectories cannot be meaningfully evaluated (p. 8, §7.2).
- **Architectural modality limitations:** a text-only model cannot draw on a canvas or describe images; better multimodal architectures are needed (pp. 8–9).
- **Generalization:** all finetuned models decline on OOD scenarios (pp. 7–9).
- **Commercial training opacity:** GPT-3.5F hyperparameters are largely inaccessible; non-optimal settings may explain weaker performance (pp. 7, 37).
- **History/context limits:** only a bounded history is included; prior screenshots/elements cannot be retained (p. 5).
- **Coordinate mapping approximation:** z-index is unavailable, so coordinate predictions use smallest-area/default-render assumptions (p. 22).
- **Screenshot timing:** Chrome capture was limited to one screenshot per 500 ms, requiring video-based realignment (p. 23, footnote 12).
- **Metric ambiguity:** different but pragmatically valid dialogue responses can score poorly (pp. 39–40).
- **Human comparison scope:** only 134 validation turns were reannotated; complete test annotation was estimated to require approximately ten months for three annotators (p. 40).
- **Single-run training:** each model was finetuned once because of cost (p. 30).

## Additional evidence-based analyst observations

- **[D] Candidate bottleneck:** MiniLM OOD Recall@10 is 51.87, so roughly half of target-element instances are absent from its top ten under that measure. Downstream candidate-based models cannot recover excluded targets.
- **[D] Confounded modality comparison:** training regime, parameter count, text access, and architecture change together; the tables do not isolate “vision” as a single causal variable.
- **[D] No online evaluation:** turn-level imitation cannot reveal error accumulation, recovery, page change, or actual completion.
- **[D] Single reference bias:** except for the small human subset, one recorded trajectory is treated as ground truth.
- **[D] No uncertainty estimates:** single runs and no confidence intervals make small differences—such as 25.21 versus 25.02—insufficient to establish reliable ordering.
- **[D] Temporal website drift:** static captures of live websites may become less representative as layouts change; the supplied paper does not quantify this.
- **[D] Ambiguous distribution graphic:** Figure 2’s counts require clarification.
- **[D] Selection and curation effects:** expert preparation, freedom to choose sites, removal of unnecessary actions, and stopping before consequential actions produce high-quality data but may differ from ordinary end-user browsing.
- **[D] Safety is discussed rather than tested:** the impact statement gives deployment cautions but no adversarial or harm-prevention experiment.

# 17. Threats to Validity

These labels are analyst-organized unless explicitly attributed.

## Internal validity

Representation, architecture, scale, pretraining, and finetuning differ simultaneously in several comparisons. One training run per configuration prevents separating systematic gains from run variability. GPT-4V’s zero-shot comparison with finetuned Fuyu or LLaMA is especially confounded.

## Construct validity

The overall score measures similarity to one recorded next action, not completion, usefulness, recovery, or safety. Character-level F1 may undervalue semantically appropriate responses, and bounding-box IoU can undervalue functionally equivalent nested or overlapping elements.

## External and ecological validity

Using 155 real websites and multi-turn human interaction improves ecological relevance. Nevertheless, tasks are demonstrations by trained annotators, consequential actions are stopped, and live autonomous execution is absent. Generalization results show that diversity alone does not guarantee transfer.

## Statistical conclusion validity

No repeated-seed distributions, standard errors, confidence intervals, or significance tests are supplied. Very small score differences should be read descriptively.

## Reproducibility

The paper supplies extensive prompts, hyperparameters, website lists, and processing details, and states that artifacts are released. Reproduction still depends on unavailable artifacts, proprietary APIs, mutable websites, unspecified library defaults, and partly hidden commercial finetuning settings.

## Data validity

Curation corrects event order and screenshot timing, but those corrections involve judgment. Invalid screenshot/action alignments are marked, yet counts of excluded or invalid turns are not reported in the supplied text.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- Create multimodal architectures that efficiently combine visual input and structured webpage information.
- Evaluate more complex websites and advanced browser events.
- Extend beyond browsers to operating-system-level interactions.
- Use reward-based training such as reinforcement learning from human feedback and direct preference optimization.
- Explore self-experience and grounded synthetic training.
- Develop multimodal-specific capabilities for tasks text-only systems cannot perform.
- Expand alternative-action human annotation.

## B. Additional open questions

- Can an online WEBLINX-style agent recover after an incorrect action?
- How much total performance is capped by candidate Recall@10?
- Which individual OTR components—attributes, XPath, boxes, IDs, or truncation—cause the improvement?
- Can semantic or learned evaluators credit valid alternative dialogue without masking unsafe actions?
- Does vision help when multimodal systems receive equivalent finetuning and equivalent structured text?
- How robust are results across random seeds and changing website versions?
- How should privacy, permissions, transaction confirmation, and irreversible actions be represented in an executable benchmark?
- Why do Figure 2’s split totals differ from Table 8’s demonstration totals?
- Can longer memory preserve early constraints without exceeding real-time latency?
- What is the full end-to-end latency after retrieval, prompt construction, model generation, network delay, and browser execution?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| WEBLINX | “Web Language Interface for Navigation & eXecuting actions”; the paper’s benchmark |
| Conversational web navigation | Browser control in which the task is developed through dialogue |
| Instructor | Human who requests and revises the task |
| Navigator | Human demonstrator or modeled assistant that talks and controls the browser |
| DOM | Document Object Model: tree-structured representation of an HTML page |
| HTML | Markup describing webpage structure and content |
| XPath | A path identifying an element’s location in the DOM tree |
| Bounding box | Rectangle locating an element in screen coordinates |
| Viewport | Visible browser area and its dimensions |
| Candidate element | A webpage element retained as a possible action target |
| DMR | Dense Markup Ranking, the proposed candidate retriever |
| OTR | Optimal Text Representation, the proposed structured prompt representation |
| Dual encoder | Separately encodes state and candidate, then compares their vectors |
| Cross-encoder | Jointly processes state and candidate in one sequence |
| Recall@10 | Fraction of cases where the correct element appears among the ten retrieved candidates |
| LLM | Large Language Model |
| Multimodal | Accepts more than one modality, here image and text |
| Image-to-text | Produces text/actions from screenshot pixels |
| Finetuning | Additional task-specific training |
| Zero-shot | Use without task-specific examples or parameter training |
| IID | Independent and identically distributed; here familiar in-domain conditions |
| OOD | Out of distribution; here aggregated unfamiliar conditions |
| `TEST_WEB` | New websites within familiar subcategories |
| `TEST_CAT` | New subcategories within familiar broad categories |
| `TEST_GEO` | Geographic regions absent from training |
| `TEST_VIS` | Instructor cannot see the screen |
| Intent | Action type such as click, load, say, submit, or text input |
| IM | Intent Match: whether action types agree |
| IoU | Intersection over Union: spatial overlap divided by combined box area |
| chrF | Character \(n\)-gram F1; the paper uses \(n=6\) |
| URLF | F1 over segmented URL components |
| EG | Element Group: click, submit, and text input |
| TG | Text Group: load, say, and text input |
| Micro-average | Average over turns rather than first averaging per class/group |
| \(s_t\) | State at turn \(t\) |
| \(a_t\) | Action at turn \(t\) |
| \(c_t\) | Candidate elements |
| \(d_t\) | Current DOM |
| \(i_t\) | Browser screenshot |
| \(u_t\) | Instructor utterance |
| \(v_t\) | Viewport size |
| \(h_t\) | Interaction history |
| \(P_m\) | Model-specific input-processing function |
| \(E(x)\) | Encoder vector for input \(x\) |
| \(L_t\) | DMR training loss at turn \(t\) |
| bfloat16 | The numeric precision used in training |
| AdamW | Reported optimization algorithm |
| FSDP | Fully Sharded Data Parallel training for 7B+ models |
| FlashAttention-2 | Memory/speed optimization used for LLaMA-family training |
| Behavior cloning | Learning to imitate demonstrated actions |
| RLHF | Reinforcement Learning from Human Feedback |
| DPO | Direct Preference Optimization |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Demonstrations | 2,337 | demos | Entire benchmark | Author-reported | p. 4, §3 |
| Total turns | 100,514 | turns | Sum of Table 7 or 8 | Analyst-derived | pp. 20, Tables 7–8 |
| Mean turns/demo | 43.01 | turns/demo | 100,514 ÷ 2,337 | Analyst-derived | Tables 7–8 |
| Website entry points | 155 | websites | 15 geographic areas | Author-reported | p. 4 |
| Categories/subcategories | 8 / 50 | groups | Dataset taxonomy | Author-reported | pp. 4, 20–21 |
| Annotators | 8 | experts | Collection | Author-reported | p. 4 |
| Average elements/page | 1,775 | elements | WEBLINX comparison | Author-reported | Table 1 |
| Train split | 969 | demos | 24,418 active turns | Author-reported | Table 8 |
| OOD test total | 1,168 | unique demos | 223+211+444+290 | Analyst-derived | Table 8 |
| Most frequent intent | 39,305 | `say` turns | Entire benchmark | Author-reported | Table 7 |
| Second-most frequent | 33,865 | click turns | Entire benchmark | Author-reported | Table 7 |
| AI-tool demonstrations | 280 | demos | Mean 46.79 turns | Author-reported | Table 9 |
| DMR MiniLM OOD Recall@10 | 51.87 | score | Candidate retrieval | Author-reported | Table 13 |
| DeBERTa OOD Recall@10 | 54.78 | score | Candidate retrieval | Author-reported | Table 13 |
| MiniLM candidate latency | 186 | ms/turn | 24,418 active train turns | Author-reported | p. 29 |
| DeBERTa candidate latency | 916 | ms/turn | Same environment | Author-reported | p. 29 |
| Runtime speed ratio | 4.93× | ratio | 22,385 ÷ 4,545 s | Analyst-derived | p. 29 |
| OTR Flan-T5-3B | 31.97 | overall score | Validation | Author-reported | Table 16 |
| MindAct-T5-3B | 27.86 | overall score | Validation | Author-reported | Table 16 |
| OTR 3B gain | 4.11 | points | 31.97−27.86 | Analyst-derived | Table 16 |
| Best validation decoder | 38.03 | overall score | LLaMA-2-13B finetuned | Author-reported | Table 18 |
| Best IID aggregate | 38.12 | overall score | LLaMA-2-7B finetuned | Author-reported | Table 28 |
| Best OOD aggregate | 25.21 | overall score | LLaMA-2-13B finetuned | Author-reported | Table 28 |
| Sheared-LLaMA OOD | 25.02 | overall score | 2.7B finetuned | Author-reported | Table 28 |
| Best zero-shot OOD | 10.72 | overall score | GPT-4T | Author-reported | Table 28 |
| GPT-4V OOD | 10.45 | overall score | Zero-shot with screenshot | Author-reported | Table 28 |
| Fuyu-8B OOD | 19.97 | overall score | Finetuned multimodal | Author-reported | Table 28 |
| LLaMA-13B OOD decline | 11.88 | points | 37.09 IID−25.21 OOD | Analyst-derived | Table 28 |
| Human-alternative annotations | 402 | annotations | 134 validation turns | Author-reported | p. 40, Table 20 |
| LLaMA human-normalized score | 65.42 | percent | Alternative-action subset | Author-reported | Table 20 |
| GPT-4V human-normalized score | 31.09 | percent | Same subset | Author-reported | Table 20 |
| Annotation recording pay | 7.50 | US$/hour | Demonstration recording | Author-reported | p. 23 |
| Mean collection cost | 2.58 | US$/demo | Includes reported overhead | Author-reported | p. 23 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| WEBLINX uniquely combines real browsing, general tasks, and dialogue among listed benchmarks | Capability columns and dataset scale | Table 1, X1 | p. 2 | Strong within the authors’ selected comparison set |
| DMR is about five times faster than the prior cross-encoder | 186 vs 916 ms; 4,545 vs 22,385 s | Table 13, X2 | pp. 28–29 | Strong descriptive timing evidence; full agent latency not measured |
| DMR sacrifices some retrieval quality | 51.87 vs 54.78 OOD Recall@10 | Table 13 | p. 29 | Strong point-estimate evidence; no uncertainty |
| OTR improves matched Flan-T5 systems over MindAct formatting | Higher overall scores at 250M, 780M, 3B | Table 16, X3 | p. 36 | Moderate-to-strong; bundled representation comparison, single runs |
| Finetuned models outperform zero-shot models | Finetuned leaders around 25 OOD vs zero-shot leader 10.72 | Tables 4, 18, 28 | pp. 6, 37, 46 | Strong across reported configurations; not every family has paired tuning |
| Evaluated text-only decoders outperform evaluated multimodal systems | LLaMA/S-LLaMA above Fuyu, Pix2Act, GPT-4V | Tables 4, 17–18, 28–30 | pp. 6, 36–37, 46–47 | Strong for these configurations; modality comparisons are confounded |
| Model scale yields limited post-finetuning gains | 2.7B, 7B, 13B scores are close | Tables 18, 28 | pp. 37, 46 | Moderate; different model variants/training histories |
| Finetuned models generalize poorly OOD | Large IID-to-OOD decline across every finetuned row | Table 28, X7 | p. 46 | Strong descriptive evidence |
| `TEST_CAT` is difficult for LLaMA-2-13B | 24.3 overall, lowest among its four OOD rows | Table 5 | p. 7 | Strong for that model; not universally the lowest split |
| Screenshots alone do not guarantee better performance | GPT-4V≈GPT-4T; Pix2Act trails structured text models | Tables 4, 17, 21, 28 | pp. 6, 36, 41, 46 | Moderate; screenshot benefit not cleanly isolated |
| Models lack situational awareness in selected cases | Wrong tabs, repeated subtasks, confused fields, repeated text | Figures 4, 9–11 | pp. 8, 34, 38–39 | Strong qualitative examples; unknown prevalence |
| Automatic text similarity misses plausible alternatives | Alternative clarification example; human-action evaluation | Table 19–20 | pp. 39–40 | Strong demonstration of construct limitation |
| A substantial human gap remains | LLaMA normalized 65.42; GPT-4V 31.09 | Table 20 | p. 40 | Moderate; only 134 validation turns |
| In-context action examples do not materially help | Similar or worse Test IID scores | Table 21, X10 | p. 41 | Moderate; limited models and one prompt design |
| Safe deployment is not established | Authors require supervision and research-only use | Impact Statement | p. 9 | Policy/safety position, not experimental evidence |

# 22. Very Simple Explanation

Imagine teaching a computer to help you use websites while you talk to it. You might first say, “Book a restaurant,” then later add, “Make it Italian,” and then ask, “What times are available?” The computer has to remember the conversation, look at the page, choose the right button or box, and sometimes ask you a question.

The researchers recorded 2,337 examples of trained people doing this across 155 real websites. Because a webpage can contain thousands of pieces, they built a fast “shortlisting” system called DMR. It picks ten page elements that seem most relevant, and another model chooses the next action from that smaller list.

Models trained on these examples did much better than very large models used without training. Surprisingly, the strongest tested models mostly relied on carefully organized webpage text, not screenshots. But even the best models often became confused on unfamiliar sites, forgot earlier details, clicked useless headings, or repeated steps already completed.

So the paper’s message is: the researchers built a valuable training ground and a faster way to read webpages, but reliable conversational browser assistants still need much better memory, visual understanding, generalization, evaluation, and safety.

# Completeness Audit

## Coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes | Yes | Fully represented | Orientation and contributions |
| §1 Introduction | Yes | Yes | Fully represented | Problem, motivation, gap, contributions |
| §2.1 Web Navigation Agents | Yes | Yes | Represented in compressed form | Prior-work categories summarized |
| §2.2 Website Representations | Yes | Yes | Represented in compressed form | DOM-compression context retained |
| §2.3 Conversational Interfaces | Yes | Yes | Represented in compressed form | Dialogue benchmark positioning retained |
| §3 WEBLINX | Yes | Yes | Fully represented | Dataset, collection, splits |
| §3.1 Actions/states | Yes | Yes | Fully represented | State variables and history |
| §4 Evaluation | Yes | Yes | Fully represented | All central metrics and scores |
| §5.1 DMR | Yes | Yes | Fully represented | Architecture, rationale, loss, speed |
| §5.2 Modeling actions | Yes | Yes | Fully represented | Modalities and model families |
| §6.1 Quantitative results | Yes | Yes | Fully represented | Aggregate and supplementary results |
| §6.2 Qualitative assessment | Yes | Yes | Fully represented | Click, text input, say, submit |
| §7 Discussion | Yes | Yes | Fully represented | Findings and limitations |
| §8 Conclusion | Yes | Yes | Fully represented | Conclusions and future work |
| Impact Statement | Yes | Yes | Fully represented | Employment, misuse, unintended action, supervision, privacy |
| References, pp. 10–16 | Yes, text | No individual entries | Deliberately compressed | Bibliographic support, not separate findings |
| Contents, pp. 17–18 | Yes, text | Yes | Deliberately compressed | Used for inventory |
| Appendix A.1 | Yes | Yes | Fully represented | Tables 6–9 and statistical interpretation |
| Appendix A.2 | Yes | Yes | Fully represented | Category logic; Table 11 compressed |
| Appendix A.3 | Yes | Yes | Fully represented | Processing by model |
| Appendix A.4 | Yes | Yes | Fully represented | Regex parsing, coordinate mapping, URL segmentation |
| Appendix A.5 | Yes | Yes | Fully represented | Selection, recording, curation, pay |
| Appendix A.6 | Yes | Yes | Fully represented | Full/evaluated action distinctions |
| Appendix A.7 | Yes | Yes | Represented in compressed form | All 155 entries inspected; list not reproduced |
| Appendix B.1 | Yes, text | Yes | Fully represented | Four OTR changes |
| Appendix B.2 | Yes, text | Yes | Fully represented | Strategic truncation procedure |
| Appendix B.3 | Yes | Yes | Fully represented | Modality taxonomy |
| Appendix B.4/B.4.1 | Yes | Yes | Fully represented | Equations, ranker comparison, speed |
| Appendix B.5 | Yes | Yes | Represented in compressed form | Prompt structure summarized |
| Appendix B.6 | Yes | Yes | Fully represented | All model implementations |
| Appendix B.7 | Yes | Yes | Fully represented | Table 14 and common settings |
| Appendix B.8 | Yes, partial visual | Yes | Represented in compressed form | p. 33 text-only; examples summarized |
| Appendix B.9 | Yes | Yes | Fully represented | Table 15 |
| Appendix C.1–C.4 | Yes | Yes | Fully represented | Representation, modality, size, generalization |
| Appendix C.5 | Yes | Yes | Fully represented | Figures 10–11, Table 19 |
| Appendix C.6 | Yes | Yes | Fully represented | Equations and Table 20 |
| Appendix C.7 | Yes, partial visual | Yes | Fully represented | Table 21 and prompt design; p. 42 text-only |
| Appendix D | Yes | Yes | Represented in compressed form | All Tables 22–30 inspected; selected cells and global patterns retained |
| Appendix E | Yes, text only | Yes | Represented in compressed form | Operational instructions and constraints |
| Figures 1–11 | Yes, visual | Yes | Fully represented | Each individually audited |
| Tables 1–21 | Yes | Yes | Fully represented or explicitly compressed | Each individually interpreted |
| Tables 22–30 | Yes | Yes | Represented in compressed form | Dense per-intent matrices not transcribed cell by cell |
| Major equations | Yes | Yes | Fully represented | E1–E9 |
| Formal algorithms | None | N/A | Not present | Procedures exist, no numbered pseudocode |
| Explicit research question | Yes | Yes | Fully represented | RQ1 |
| Explicit hypotheses | Yes | Yes | Fully represented | None stated |
| Major experiments | Yes | Yes | Fully represented | X1–X11 |
| Major contributions | Yes | Yes | Fully represented | Conceptual through empirical |
| Author-stated limitations | Yes | Yes | Fully represented | Separate from analyst observations |
| Supplied supplementary material | Yes | Yes | Fully represented | Appendix C supplied |
| External code/data/models/videos | No | No | Missing from supplied material | Only availability statement provided |

## Missing or inaccessible material

- No pages are missing from the supplied text.
- Thirteen pages were not visually rendered: pp. 9, 11, 14–18, 27, 33, 42, and 48–50.
- The unrendered pages contain the conclusion/impact statement, references, contents, OTR/truncation text, part of a prompt example, the end of the D&E prompt, and annotator instructions. They were inspected through supplied native text only.
- No separate supplementary files, executable code, dataset records, browser recordings, annotation interface, trained models, or external website snapshots were supplied.
- The paper mentions released artifacts and external URLs, but closed-document mode precluded inspecting them.

## Uncertain interpretations

- Figure 2’s split counts conflict with Table 8’s unique-demonstration counts. Overlapping category assignments may explain this, but the paper does not say so.
- The DMR loss is described as mean-squared error, while the displayed equation shows one candidate-level squared error without an explicit mean/sum.
- Mathematical notation may have minor extraction artifacts, including spacing, subscripts, and symbols.
- Table 4 contains a garbled screenshot footnote marker in extraction; the surrounding prose and visual make its meaning clear.
- Table 17’s prose refers to “Table 5.2,” apparently a mistaken section/table reference.
- Figure 4’s caption says “predicting click actions” although it contains click, text-input, and `say` examples.
- “All models” and “19 models” sometimes refer to model variants rather than unique architectural families; the paper separately states eight architectures.

## Deliberately compressed material

- The reference list was not summarized citation by citation.
- Table 12’s 155 website rows and Table 11’s 50 subcategory rows were inspected but summarized structurally.
- Tables 22–27 contain hundreds of per-intent values; important patterns and selected values were preserved rather than reproducing every cell.
- Prompt templates and multi-page sample inputs were described by structure instead of copied verbatim.
- Appendix E’s installation and Zoom click-by-click instructions were compressed to their methodological and validity implications.
- Repeated main-text and appendix statements were integrated rather than restated separately.

## Potential omissions

No known substantive section, figure, table, major equation, experiment, contribution, author-stated limitation, or supplied appendix is absent from this analysis. Dense bibliographic entries, website rows, prompt text, and detailed result matrices were deliberately compressed as disclosed above. The inaccessible external artifacts prevent assessing actual dataset contents, code correctness, model reproducibility, licensing details beyond the paper, or live-system behavior.