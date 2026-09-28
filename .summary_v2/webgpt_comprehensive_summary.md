# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible extent | All 32 pages, including the main paper, references, and Appendices A–K |
| Apparently missing pages | None |
| Native text | Available for every page; no page was classified as scanned or unusually low-text |
| Visual inspection | Partial by page, but all substantive numbered figures were rendered and inspected: Figures 1–12 |
| Rendered pages | 1–10, 12, 15–20, 22, and 24–31 |
| Pages not visually rendered | 11, 13, 14, 21, 23, and 32; their native text was supplied and inspected |
| Tables | Tables 1–13 are readable from supplied text; all result/method tables requiring visual layout inspection were also rendered |
| Equations | Equation (1) and the Appendix I estimators are readable. Combinatorial notation in Appendix I is OCR-sensitive but sufficiently clear when cross-checked against the rendered page |
| Appendices | Appendices A–K are present |
| Supplementary material | No separate supplementary files were supplied |
| Referenced but absent artifacts | Online answer viewer; downloadable comparison dataset; linked demonstration and comparison instructions; cited external papers, websites, and APIs |
| OCR needed | No. Native extraction was adequate |
| Important visual limitation | Unnumbered page-19 survey pie-chart values are not numerically labeled; only broad trends can be read confidently |
| Source boundary | Closed-document mode. Everything below is based only on the supplied paper and rendered pages |

Source-status labels used below:

- **[A] Author-reported:** explicitly stated by the paper.
- **[B] Directly observable:** clearly visible in a supplied visual.
- **[C] Analyst-derived:** calculated directly from supplied values.
- **[D] Analyst interpretation:** an inference, explicitly marked as such.
- No external information is introduced.

# 1. Plain-Language Orientation

WebGPT is a system that teaches a GPT-3 language model to answer open-ended questions by operating a restricted, text-only web browser. Instead of relying solely on facts stored in its parameters, the model can search Bing, open pages, move through text, extract quotations, and then write an answer supported by those quotations (§2, pp. 2–3).

The problem is long-form question answering (LFQA): producing a coherent paragraph-length response to an open-ended question. The authors argue that previous systems separately emphasized retrieval and answer generation. WebGPT instead focuses on teaching a model the higher-level process of using an existing search engine, selecting evidence, and synthesizing an answer (§1, pp. 1–2).

Humans first demonstrated the task. Those demonstrations were used for supervised **behavior cloning** (BC). Humans then compared pairs of model answers; these preferences trained a **reward model** (RM). The researchers used that reward model either to train the answering policy through **reinforcement learning** (RL) or to select the best of several independently sampled answers through **rejection sampling**, also called best-of-\(n\) (§3, pp. 3–5).

The best evaluated system—GPT-3 175B with behavior cloning and best-of-64 rejection sampling—was preferred:

- 56% of the time over answers written by the project’s human demonstrators.
- 69% of the time over the highest-voted Reddit answers in ELI5.
- On TruthfulQA, its answers were about 75% truthful and 54% both truthful and informative (§1 and §4, pp. 1–7).

The central contribution is therefore not a new search engine or base language model. It is a trainable, inspectable workflow connecting web browsing, evidence collection, answer synthesis, and human preference feedback.

# 2. Document Roadmap

The work is a mixed machine-learning, agent-environment, and empirical systems paper.

| Identifier | Paper component | Function |
|---|---|---|
| S1 | §1 Introduction, pp. 1–2 | Problem, contribution, headline results |
| S2 | §2 Environment design, p. 3 | Text-browser interaction protocol |
| S3 | §3 Methods, pp. 3–5 | Human data and four training methods |
| S4 | §4 Evaluation, pp. 5–7 | ELI5, TruthfulQA, and TriviaQA evaluation |
| S5 | §5 Experiments, pp. 7–9 | Training-method and scaling comparisons |
| S6 | §6 Discussion, pp. 9–11 | Truthfulness, authority, bias, references, web risks |
| S7 | §7 Related work, pp. 11–12 | Retrieval-based QA and browser agents |
| S8 | §8 Conclusion, p. 12 | Main conclusion |
| S9–S10 | §§9–10, pp. 12–13 | Contributions and acknowledgments |
| A1 | Appendix A, p. 15 | Browser implementation |
| A2 | Appendix B, p. 16 | Question sources and preprocessing |
| A3 | Appendix C, pp. 17–18 | Contractor and comparison procedures |
| A4 | Appendix D, p. 19 | Contractor survey |
| A5 | Appendix E, pp. 20–22 | Hyperparameters and early stopping |
| A6 | Appendix F, p. 23 | Minimal ELI5 comparison instructions |
| A7 | Appendix G, p. 24 | TriviaQA transfer evaluation |
| A8 | Appendix H, pp. 25–27 | Question stance and cultural reference-point bias |
| A9 | Appendix I, p. 28 | Rejection-sampling performance estimator |
| A10 | Appendix J, pp. 29–31 | Full evidence and alternative answers for Table 2 |
| A11 | Appendix K, p. 32 | Released comparison-dataset schema |

Inventory: 12 numbered figures, 13 numbered tables, one numbered main-text equation, three closely related estimator expressions in Appendix I, no pseudocode block, and no theorem, lemma, or proposition.

# 3. Background and Context

**Long-form question answering (LFQA)** asks for explanatory, paragraph-length answers rather than short fact strings.

A language model has two relevant tasks:

1. **Retrieval:** finding information that bears on the question.
2. **Synthesis:** turning selected information into a coherent answer.

Earlier retrieval systems discussed by the authors—Dense Passage Retrieval (DPR), Retrieval-Augmented Language Modeling (REALM), and Retrieval-Augmented Generation (RAG)—learn to retrieve documents through differentiable similarity functions. WebGPT instead uses an external search engine and treats browsing as a sequence of textual actions (§7, p. 12).

**Human feedback** supplies two forms of supervision:

- A **demonstration** shows which browser commands and final answer a human produced.
- A **comparison** records which of two answers a human preferred.

A **reward model** converts an answer and its references into a scalar estimate of human preference. Its scale is Elo-like: a score difference of 1 corresponds to a modeled preference probability of \(\operatorname{sigmoid}(1)\approx73\%\) (§3.2 and §5.2, pp. 4, 8).

**Rejection sampling** here means generating \(n\) complete candidate browsing-and-answering trajectories, scoring them, and returning the highest-scoring one. It does not mean rejecting individual tokens.

# 4. Research Problem and Gap

## Existing problem

LFQA systems may become important sources of knowledge but, according to the authors, lag human performance and can generate unsupported or false statements (§1, p. 1).

## Shortcomings attributed to previous approaches

- Previous work generally separates retrieval and synthesis.
- Learned dense retrieval is differentiable and fast to optimize, but cannot directly model non-differentiable tools such as a commercial search engine and is less interpretable (§7, p. 12).
- Automated metrics such as ROUGE-L were reported by earlier ELI5 work to be poorly aligned with meaningful long-form answer quality (§7, p. 12).
- Direct factuality judgments are difficult because labelers may lack the necessary expertise (§6.4, p. 11).

## Research gap

The authors seek an end-to-end way to train a model to use a real search interface, collect inspectable supporting evidence, synthesize long answers, and optimize overall quality using human preferences.

## Motivation

Requiring references is intended to make feedback more accurate, less noisy, and more transparent: evaluators can inspect support for a claim without independently researching every issue (§6.4, p. 11).

## Scope

The primary setting is ELI5 long-form questions. TruthfulQA and TriviaQA test transfer to adversarial or short-form questions. The browsing interface permits searching and reading but not submitting forms or directly modifying websites.

# 5. Research Questions / Objectives / Hypotheses

The paper does not state formally numbered research questions or preregistered hypotheses. Its objectives can be reconstructed without presenting them as formal author questions:

- **O1:** Build a textual browser that humans and a language model can operate under substantially similar conditions.
- **O2:** Train GPT-3 to retrieve evidence and synthesize cited long-form answers.
- **O3:** Determine whether human preference optimization improves on imitation alone.
- **O4:** Compare behavior cloning, reinforcement learning, and best-of-\(n\) selection.
- **O5:** study scaling with demonstration count, comparison count, model parameters, and inference-time sampling.
- **O6:** Evaluate truthfulness and transfer outside the primary ELI5 distribution.
- **O7:** Examine risks involving perceived authority, question framing, cultural assumptions, and live web access.

The authors explicitly hypothesize in the discussion that WebGPT’s TruthfulQA failures partly reflect distribution shift from ELI5, but this is a post-result explanation rather than a preregistered hypothesis (§6.1, p. 9).

# 6. Assumptions / Threat Model

This is not primarily a security paper, but it contains a system and risk model.

## System assumptions

- Bing provides useful, relatively current search results.
- Web pages can be meaningfully reduced to text.
- Human demonstrations can teach the command grammar.
- Human pairwise preferences provide a usable signal for answer quality.
- References make support easier to judge than unconstrained factual truth.
- A separately split validation reward model is a useful proxy for human preference in scaling experiments, at least when the policy is not optimized through RL (§5.2, p. 8).

## Trusted components

The design implicitly trusts the Bing API, the text-extraction pipeline, contractors’ judgments, and the reward-model training process. The authors do not describe these as perfectly reliable.

## Allowed external actions

The agent may send search queries and follow existing links. It cannot directly fill forms, post content, or edit pages (§6.5, p. 11).

## Risk boundary

The authors consider direct real-world side-effect exploitation unlikely for this implementation because of the restricted interface, while warning that substantially more capable systems with web access could create greater risks (§6.5, p. 11).

## Evaluation assumptions

- Ties count as 50% preference.
- Support from a reliable reference or common knowledge substitutes for independent fact-checking in the principal comparison workflow.
- For the minimal ELI5 comparison, labelers may use a search engine, but must not follow URLs embedded in the supplied material (Appendix F, p. 23).

# 7. Methodology

## Browser architecture

At each step, the model receives a fresh textual state containing the question, current page text, cursor/scroll information, collected quotations, past actions, and remaining action budget. Because each step uses a fresh context, recorded state supplies the model’s only explicit memory of prior actions (§2, p. 3; Fig. 1).

The permitted actions are search, link click, find, quote, scroll, top, back, end-and-answer, or end-without-answer (Table 1, p. 3). Invalid text still consumes an action.

When the model quotes a passage, the system records its text, page title, and domain. Browsing stops when the model ends it, reaches the action limit, or reaches the reference-length limit. A final answer is requested only if at least one reference exists (§2, p. 3).

Appendix A reports that the browser was written mostly in Python with some JavaScript. Bing supplies search results; Node.js and Mozilla Readability.js simplify pages; `html2text` converts HTML; `pdfminer.six` extracts PDF text. Reddit and Quora links are removed, and pages with a 10-gram overlap with the question or supplied reference answer are censored to reduce answer copying (p. 15).

## Data

Table 4 reports:

| Dataset | Demonstrations | Comparisons |
|---|---:|---:|
| ELI5 | 5,711 | 21,068 |
| ELI5 fact-check | 67 | 185 |
| TriviaQA | 143 | 134 |
| ARC Challenge | 43 | 84 |
| ARC Easy | 83 | 77 |
| Hand-written | 162 | 0 |
| Total | 6,209 | 21,548 |

[A] The main text rounds these totals to “around 6,000” demonstrations and “around 21,500” comparisons (§3.1, p. 3). These are consistent rather than contradictory.

ELI5 preprocessing included restoring full URLs, filtering deleted titles or bodies, joining title and body, and prepending “Explain:” when a heuristic did not detect question-like phrasing (Appendix B, p. 16).

## Human collection

Ten Upwork contractors provided about 25% of the data; 46 Surge AI contractors provided about 75%. The five largest contributors produced about half. Contractors were generally highly educated and paid hourly (Appendix C, p. 17).

Final agreement was 74% between researchers and labelers and 73% among labelers, treating disagreement between neutral and non-neutral labels as half agreement. Demonstrations averaged about 15 minutes; comparisons about 10 minutes (p. 17).

Comparisons used a five-point scale from “A much better” through “B much better.” Although the interface collected claim support, relevance, reference trustworthiness, coherence, and other annotations, only the collapsed final preference was used for training (Appendix C.2, pp. 17–18).

## Training

- **BC:** supervised fine-tuning on human browser demonstrations.
- **RM:** a BC-derived model with its final unembedding removed; it predicts an Elo-like scalar from a question, answer, and references. Cross-entropy trains it on pairwise preferences; ties are soft 50% labels.
- **RL:** Proximal Policy Optimization (PPO) fine-tunes the BC policy. Episode reward combines terminal RM score with a token-level Kullback–Leibler (KL) penalty relative to BC.
- **Best-of-\(n\):** sample 4, 16, or 64 complete answers and choose the one the RM ranks highest (§3.2, p. 4).

BC, RM, and RL question sets were mutually disjoint. About 4% of demonstrations were held out for BC validation. Final RMs trained on about 16,000 comparisons; about 5,500 remained evaluation-only (§3.2, p. 5).

RL used 90% ELI5 and 10% TriviaQA questions. Each browsing episode was followed by 15 extra answer-only episodes reusing the same references; the authors report about a twofold sample-efficiency improvement. The maximum browsing budget was sampled uniformly from 20 through 100 during RL (p. 5).

## Principal evaluation configuration

The three main WebGPT systems were:

- 760M parameters, best-of-4.
- 13B, best-of-16.
- 175B, best-of-64.

All used temperature 0.8 and at most 100 browsing actions (§4, p. 5).

## Hyperparameters

Tables 5–8 report all major training settings. Notable values include BC minibatch 512 (256 for 760M), RM minibatch 64 (32 for 175B), EMA decay 0.99, PPO clipping 0.2, KL coefficient 0.02, 256 environments, 256 rollout timesteps, one PPO epoch, 128 minibatches, and 64 maximum tokens per action (pp. 20–22).

Hardware, GPU types, software/library versions, random seeds, monetary costs, and repeated-run counts are not reported.

# 8. Experiments / Analyses

## X1 — ELI5 versus project demonstrators

Purpose: test whether WebGPT can match humans performing the same browser-assisted task.

Setup: pairwise judgments of model and demonstrator answers, using detailed comparison criteria and references. Ties count as 50%. Figure 2a reports usefulness, coherence, and factual accuracy.

Result: the 175B best-of-64 answer was preferred overall 56% of the time (§4.1, p. 5). Its factual-accuracy comparison is approximately even with human demonstrations [B; Fig. 2a].

Caveat: demonstrators are project contractors, not a representative sample of all experts or users.

## X2 — ELI5 versus Reddit references

Purpose: compare with the dataset’s highest-voted answer and earlier ELI5 systems.

Citations were stripped from WebGPT answers, new contractors were used, and instructions were simplified. The 175B best-of-64 system was preferred 69% overall (Fig. 2b; §4.1).

The authors regard X1 as more meaningful because X2 has weaker fact-checkability, imperfect blinding, stylistic differences, and uncertain alignment with original ELI5 intent (p. 6).

## X3 — TruthfulQA

Purpose: test susceptibility to questions designed around common false beliefs.

GPT-3 was assessed with automated metrics under “QA” and “helpful” prompts. WebGPT used human evaluation because its answer style was out of distribution for the automatic metric. WebGPT answers were truncated to 50 tokens, with partial final sentences removed (§4.2, pp. 6–7).

All WebGPT sizes exceeded all tested GPT-3 variants on truthful and truthful-plus-informative rates. The 175B WebGPT reached about 75% truthful and 54% both truthful and informative [A/B; Fig. 3].

Caveat: truncation accidentally created 74 empty answers—about 3%—counted as truthful but uninformative (footnote 3, p. 7).

## X4 — TriviaQA transfer

The 175B BC model, temperature 0.8, with no rejection sampling, produced long answers. A separate GPT-3 175B extractor was fine-tuned on 256 questions to turn these into short answers; batch size was 32 and learning rate \(1.5\times10^{-6}\). An extractor without WebGPT context was the ablation (Appendix G, p. 24).

The WebGPT-assisted pipeline achieved 69.5% total exact match versus 58.7% for the extractor alone, 68.9% for UnitedQA-E, and 70.5% for UnitedQA hybrid (Table 9).

## X5 — RL versus BC and rejection sampling

The 175B RL policy was preferred 58% over 175B BC without rejection sampling. The 175B best-of-64 BC system was preferred 68% over BC (§5.1, p. 7). Figure 4 shows little advantage for combining RL with rejection sampling.

## X6 — Rejection-sampling scaling

Figure 5 compares observed human preference with an Appendix I validation-RM prediction as \(n\) grows from 1 to 64. Both rise from 50% to roughly 68%; the validation estimate tracks the human curve within the displayed uncertainty.

## X7 — Data and parameter scaling

According to §5.2:

- Doubling demonstrations increased policy validation-RM score by about 0.13.
- Doubling comparisons increased RM accuracy by about 1.8 percentage points.
- Doubling policy parameters increased validation-RM score by roughly 0.09.
- Doubling RM parameters increased accuracy by roughly 0.4 percentage points.

These are author-reported trend fits, not values independently recoverable exactly from the plots.

## X8 — Compute allocation

Figure 8 varies model size and number of samples against estimated floating-point operations. The authors identify moderate best-of-\(n\) as compute-efficient and select 760M/4, 13B/16, and 175B/64 from the estimated Pareto frontier.

## X9 — Question-stance study

Twenty topics—10 conspiracy theories and 10 misconceptions—were each expressed in skeptical, neutral, and affirming forms, giving 60 questions per model and 180 answers over three models (Appendix H.1, pp. 25–27).

Affirming questions produced lower accuracy than neutral or skeptical wording in the displayed results. The authors call this suggestive rather than definitive because the sample is small. Answers usually refuted the false premise, increasingly so with model size; no clear effect of question stance on whether the answer affirmed or refuted was found.

## X10 — Cultural reference-point case study

For “What does a wedding look like?”, 64 outputs from 175B BC were inspected:

- 20 mentioned America/American.
- 4 focused on a named non-American culture: Vietnamese 1, Indian 1, Croatian 2.
- 8 said there is no standard wedding, but 7 of those still included Western/American details.
- 2 of those 8 reframed the issue specifically as there being no standard American wedding (Appendix H.2, pp. 25–26).

## X11 — Contractor survey

Forty-one ratings per question were aggregated across three surveys. The plots indicate broad satisfaction with clarity, enjoyment, pay, and participation, alongside a substantial minority finding the work repetitive (Appendix D, p. 19).

# 9. Results

| Finding | Evidence and condition | Qualification |
|---|---|---|
| WebGPT can match or slightly exceed project demonstrators in overall preference | 175B best-of-64 preferred 56%; Fig. 2a | Pairwise human preference, not a proof of universal superiority |
| WebGPT strongly exceeds ELI5’s highest-voted answer under the study’s comparison | 69%; Fig. 2b | Citations removed; imperfect blinding and differing answer intent |
| WebGPT is more truthful than tested GPT-3 prompting baselines | About 75% truthful and 54% truthful-and-informative for 175B; Fig. 3 | Still below human reference lines; out-of-distribution failures remain |
| Best-of-\(n\) provides a larger gain than RL | 68% best-of-64 BC over BC versus 58% RL over BC | More inference compute is required for best-of-64 |
| RL adds little once rejection sampling is used | Figure 4 right-hand group near or below 50% for the largest model [B] | Exact per-bar values are unlabeled |
| More data improves BC and RM performance | +0.13 score per demonstration doubling; +1.8 percentage points RM accuracy per comparison doubling | Proxy metrics, not direct human evaluation |
| Model-size gains exist but are noisier | +0.09 policy score and +0.4 percentage points RM accuracy per parameter doubling | Author-described approximate trends |
| WebGPT helps short-form QA extraction | 69.5% versus 58.7% total exact match | Uses more compute and live web access than cited corpus-only comparisons |
| Affirming false premises may reduce accuracy | Figure 11 | Small exploratory sample; no significance test reported |
| Generic questions may trigger Western/American defaults | 20/64 America mentions; only 4/64 named another culture | One question and one model configuration |

[C] The TriviaQA WebGPT-assisted pipeline improves over its GPT-3 extraction ablation by **10.8 percentage points**: \(69.5-58.7=10.8\). This is an absolute difference, not a 10.8% relative improvement.

# 10. Figure-by-Figure Interpretation

### Figure 1 — Human and model browser representations

Panel (a) is the graphical interface for demonstrators; panel (b) is the corresponding textual state for the model. Both contain the question, quotations, current page/search text, and action controls. The figure establishes functional correspondence between human and model tasks, though Appendix C notes exceptions concerning human memory and multi-step scrolling.

### Figure 2 — ELI5 human preferences

Two grouped bar charts show percentages on a 0–70% linear scale, with a dashed 50% parity line and ±1 standard-error bars.

- Panel (a): WebGPT versus human demonstrations.
- Panel (b): WebGPT versus highest-voted ELI5 answers.
- Categories: overall usefulness, coherence, factual accuracy.
- Colors: 760M best-of-4, 13B best-of-16, 175B best-of-64.

[B] The largest model is about 56% overall against demonstrators and 69% against ELI5 references. Coherence and factual-accuracy bars generally increase with compute/model configuration, although not perfectly monotonically in every visible group.

### Figure 3 — TruthfulQA

Grouped bars compare GPT-3 under two prompts with WebGPT. Filled blue bars are truthful percentages; outlined white bars are truthful-and-informative percentages. Horizontal dotted lines show human reference levels.

[B] WebGPT substantially outperforms GPT-3 variants. The largest WebGPT is about 75% truthful and 54% truthful-and-informative, still below the approximately high-80s/low-90s human lines.

### Figure 4 — RL preference over BC

The left group compares plain RL with plain BC; the right compares rejection-sampled RL with rejection-sampled BC. A 50% dashed line means parity.

[B] RL alone is mostly above parity, reaching the reported 58% for 175B. With rejection sampling, the advantage largely disappears; the 175B bar is below parity. Error bars are ±1 standard error.

### Figure 5 — Human and predicted best-of-\(n\) benefit

A line chart uses \(n=1,4,16,64\) on the x-axis and preference over BC on the y-axis. Human preference is a solid blue line with a shaded ±1-standard-error band; validation-RM prediction is dashed.

Both rise from 50% at \(n=1\) to roughly 68% at \(n=64\). The prediction tracks human preference reasonably through 64, but Appendix I predicts eventual overestimation at sufficiently large \(n\).

### Figure 6 — Behavior-cloning scaling

A line plot relates demonstration fraction \(1/8,1/4,1/2,1\) to validation-RM score for 760M, 13B, and 175B policies. Scores rise approximately linearly with log-scaled data fraction; larger policies generally score higher.

### Figure 7 — Reward-model scaling

Comparison-data fraction is plotted against accuracy for 760M, 13B, and 175B RMs. Accuracy increases with data and model size. Horizontal references mark human baseline and an ensemble of humans; the learned models remain below the human ensemble.

### Figure 8 — Best-of-\(n\) compute scaling

The log-scaled x-axis is floating-point operations; the y-axis is validation-RM score. Points combine model sizes and sampling counts. A dashed estimated compute-efficient frontier passes through configurations such as 760M best-of-4, 13B best-of-16, and 175B best-of-64. The figure supports allocating some—but not unlimited—compute to multiple samples.

### Figure 9 — Claim-annotation interface

The screenshot shows a question, answer options, source excerpts, trustworthiness labels, and colored support annotations such as strong, weak, or no support. It demonstrates the detailed evidence-assessment workflow, although only final preferences trained the RM.

### Figure 10 — Contractor survey

Five pie charts represent instruction clarity, enjoyment, repetitiveness, fair pay, and overall satisfaction using a five-point Likert legend. Forty-one equally weighted ratings contribute to each chart.

[B] Positive responses dominate clarity, enjoyment, fair pay, and overall satisfaction. Repetitiveness is more mixed. Exact category counts are not labeled and cannot be read reliably.

### Figure 11 — Question stance and factual accuracy

Grouped bars plot accurate-answer percentage by affirming, neutral, and skeptical question framing for three WebGPT configurations.

[B] Accuracy is lowest for affirming wording, especially for smaller models; neutral is higher and skeptical approximately highest. Exact values are visually approximate, and no statistical test is supplied.

### Figure 12 — Question stance and answer stance

Stacked bars show proportions that refute, neither affirm nor refute, or affirm the premise.

[B] Most answers refute the false premise. Larger models devote a greater proportion to refutation. Differences across question wording are not clearly systematic, matching the authors’ cautious interpretation.

# 11. Table-by-Table Interpretation

### Table 1 — Browser action space

Defines the complete valid command grammar and effects. Invalid actions consume budget but have no other effect. This table operationalizes the agent’s control interface.

### Table 2 — Example WebGPT answer

Presents a randomly selected ELI5 test question, the 175B best-of-64 answer, and five reference titles. It illustrates multi-source, inline-cited synthesis rather than a benchmark aggregate.

### Table 3 — TruthfulQA success and failure

Contrasts GPT-3 QA prompting, helpful prompting, and WebGPT for two cherry-picked questions. It shows WebGPT correctly replacing a superstition with practical risks in one case, but endorsing “wish fulfillment through thought” in another. It is qualitative evidence, explicitly not representative sampling.

### Table 4 — Dataset composition

Lists the exact 6,209 demonstrations and 21,548 comparisons. ELI5 dominates both columns. Hand-written questions appear only in demonstrations.

### Table 5 — Base Adam learning rates

760M: \(2.5\times10^{-4}\); 13B: \(1.0\times10^{-4}\); 175B: \(0.6\times10^{-4}\). Later multipliers operate on these size-specific bases.

### Table 6 — BC and RM hyperparameters

BC/RM minibatches are 512/64, with exceptions of 256 for 760M BC and 32 for 175B RM. Step multipliers are 0.1/0.05, except \(1/60\) for 175B RM. Epoch ceilings are 12/6; EMA decay is 0.99 for both.

### Table 7 — RL hyperparameters

Reports the PPO configuration: 256 environments and rollout timesteps, one epoch, 128 minibatches, step multiplier 0.004, KL coefficient 0.02, no entropy bonus, clipping 0.2, \(\gamma=1\), \(\lambda=0.95\), advantage but not reward normalization, 16 answer phases per browsing phase, and 64 tokens per action.

### Table 8 — Early stopping

BC epochs are 2, 5, and 3 for 760M, 13B, and 175B; RM uses one epoch throughout. RL stops at 19/30/18 PPO iterations and 10.5/6.8/~12 nats KL per episode.

### Table 9 — TriviaQA exact match

The WebGPT-assisted pipeline leads GPT-3 alone in every split. It slightly exceeds UnitedQA-E on total, no-question-overlap, answer-overlap-only, and no-overlap subsets, while trailing on question-overlap and answer-overlap. UnitedQA hybrid reports only its 70.5% total.

### Table 10 — Stance stimuli

Lists all 20 topics and their skeptical, neutral, and affirming formulations. Its importance is methodological: it makes the manipulation auditable and reveals that wording changes sometimes alter more than grammatical stance, a potential construct-validity concern [D].

### Table 11 — WebGPT example references

Provides the full five passages behind Table 2. The final answer chiefly uses passages 2 and 3, despite collecting five references.

### Table 12 — Human answer and references

Shows a demonstrator answering the same question with a more legal and historical emphasis. It illustrates substantial variance in plausible answer scope.

### Table 13 — ELI5 reference answer

Contains only a brief podcast recommendation. This example helps explain why high-effort WebGPT answers may be preferred to some highest-voted Reddit references, but one example cannot establish the aggregate effect.

# 12. Diagram / Architecture Interpretation

Figure 1 is the principal architecture-like visual. The workflow is:

```text
Question
   ↓
Textual browser state
   ↓
Model chooses command
   ├─ Search Bing
   ├─ Open/read/scroll/find
   ├─ Save quotation + title + domain
   └─ Repeat
   ↓
Stop condition
   ↓
Question + collected references
   ↓
Final cited answer
```

During training, human demonstrations supervise actions through BC. Pairwise answer comparisons supervise the RM. The RM then influences the policy through either PPO or best-of-\(n\) selection. Best-of-\(n\) adds a second loop: generate several complete candidates, score each, and retain the maximum-scoring one.

# 13. Equations and Mathematical Concepts

## Equation (1): differentiable passage retrieval

\[
p(\text{passage}\mid\text{query})
\propto
\exp\left(
\operatorname{embed}(\text{passage})\cdot
\operatorname{embed}(\text{query})
\right).
\]

Location: §7, p. 12.

A passage and query are mapped to vectors. Their inner product measures similarity; exponentiation converts that score into positive relative weight. The proportionality sign indicates normalization over candidate passages is omitted. This equation describes related retrieval methods, not WebGPT’s Bing-based browser.

## Reward-model scale

No standalone formula is numbered, but the RM emits an Elo-like score. A difference of one point corresponds to preference probability:

\[
\operatorname{sigmoid}(1)\approx 0.73.
\]

Thus RM-score differences are meaningful as preference logits (§5.2, p. 8).

## Appendix I: expected validation score after best-of-\(n\)

For question \(q\), answers \(A_1,\ldots,A_n\) are sampled from policy distribution \(A(q)\). The training RM \(R^{\text{train}}\) chooses the candidate; an independent validation RM \(R^{\text{val}}\) evaluates that choice:

\[
R_n^{\text{pred}}(q)=
\mathbb{E}_{A_1,\ldots,A_n\sim A(q)}
\left[
R^{\text{val}}\!\left(
\arg\max_{a\in\{A_1,\ldots,A_n\}}
R^{\text{train}}(a\mid q)
\,\middle|\,q
\right)
\right].
\]

The outer expectation over \(Q\) gives the overall predicted score:

\[
\mathbb{E}_{Q\sim\mathcal Q}[R_n^{\text{pred}}(Q)].
\]

Plainly: generate \(n\) answers, let the optimized RM select one, then ask a separately trained RM how good that selected answer is expected to be.

To reuse \(N\) samples efficiently for multiple values of \(n\), the authors average over every size-\(n\) subset. After sorting samples \(S_1,\ldots,S_N\) by training-RM score, the estimate becomes:

\[
\sum_{i=n}^{N}
\frac{\binom{i-1}{n-1}}{\binom{N}{n}}
R^{\text{val}}(S_i\mid q).
\]

The combinatorial coefficient is the probability that \(S_i\) is the highest training-RM-scored member of a uniformly selected \(n\)-subset. This provides an unbiased, sample-reusing estimator. The authors warn that even the validation RM will eventually be overoptimized for sufficiently large \(n\).

# 14. Interpretation and Discussion

The results support the authors’ main objective: a language model can learn a human-like search-and-synthesis procedure and can improve beyond direct imitation when candidate outputs are ranked by learned human preferences.

The strongest evidence is on in-distribution ELI5 evaluation. The 56% comparison with project demonstrators is especially informative because both sides used references and similar instructions. The 69% comparison against Reddit answers is larger but more confounded by effort, style, citations, and answer intent.

TruthfulQA shows that access to retrieval and evidence does not guarantee truth. WebGPT usually attempts substantive answers, whereas the “helpful prompt” GPT-3 baseline frequently avoids them: Table 3 reports “I have no comment” for 49% of questions. This improves informativeness but creates a route to confidently supported errors when sources are poor.

The authors distinguish:

- **Imitative falsehoods:** errors encouraged by reproducing common misconceptions.
- **Non-imitative falsehoods:** failures to achieve the intended objective, including plausible hallucinations.

They argue that TruthfulQA suggests fewer imitative falsehoods, whereas ELI5 offers indirect evidence concerning non-imitative falsehoods. They explicitly did not directly test the latter because subtle hallucinations were difficult for labelers to detect (§6.1).

References improve inspectability but change the optimization problem from “be true” to “produce claims that evaluators judge well supported.” The paper explicitly warns that a stronger model might cherry-pick persuasive evidence rather than fairly represent the total evidence (§6.4).

No numerical contradictions were found between main text and appendices. Rounded totals align with Table 4. The dataset has 21,548 collected comparisons, roughly 16,000 RM-training comparisons, roughly 5,500 evaluation-only comparisons, and 19,578 released suitable comparisons; these numbers describe different filtered or split quantities rather than necessarily conflicting totals.

# 15. Contributions and Novelty

- **Conceptual:** frames web-assisted answering as an interactive language-model task supervised through human-compatible actions.
- **Methodological:** combines demonstrations, pairwise preferences, reward modeling, PPO, and best-of-\(n\) selection.
- **System:** implements a restricted textual browser over live Bing results and extracted web pages.
- **Evaluation:** requires collected references to make support judgments more tractable.
- **Empirical:** reports human-level or better preference performance on the project’s ELI5 evaluations and improved TruthfulQA behavior over tested GPT-3 baselines.
- **Scaling:** studies the trade-off among model size, training-data size, and inference-time sampling.
- **Mathematical:** supplies a reusable estimator for best-of-\(n\) validation performance.
- **Dataset:** releases 19,578 comparison pairs suitable for reward modeling, including questions, quotations, answers, tokenized inputs, and preference scores (Appendix K).

# 16. Limitations

## Authors' stated limitations

- WebGPT remains below humans on TruthfulQA and struggles on out-of-distribution questions.
- It can cite unreliable sources and make synthesis/paraphrasing errors (§6.1).
- Citations may make incorrect answers appear more authoritative, creating automation-bias risks (§6.2).
- The model inherits GPT-3 biases and may reinforce biases present in online sources (§6.3).
- It often accepts assumptions embedded in questions.
- Reference-based supervision can reward persuasive cherry-picking rather than balanced evidence (§6.4).
- Source-trustworthiness criteria require contestable judgment calls.
- Live web access can create safety risks as model capability grows (§6.5).
- TruthfulQA truncation produced 74 empty answers.
- Human evaluation is noisy and expensive.
- The question-stance experiment is too small for definitive conclusions.
- The wedding study examines one prompt and shows Western/American reference-point bias.
- RL required tuning and could overoptimize the RM.
- The validation RM is expected eventually to overestimate best-of-\(n\) performance.
- TriviaQA comparison uses more compute and live web access than UnitedQA.
- Hardware and detailed compute-cost reporting are absent from the supplied work.

## Additional evidence-based analyst observations

- **[D] Evaluator concentration:** five contractors produced about 50% of collected data, making the learned preference signal sensitive to a small subset of workers.
- **[D] Preference construct:** only the final collapsed rating trained the RM, discarding richer annotations that might separate factual support, coherence, relevance, and source quality.
- **[D] Proxy dependence:** scaling conclusions rely largely on a validation RM rather than direct human evaluations.
- **[D] Search-engine dependence:** performance is entangled with Bing’s ranking, filtering, availability, and web coverage.
- **[D] Multiple comparisons:** many configurations and exploratory analyses are presented without formal significance testing.
- **[D] Benchmark comparability:** the 56%, 69%, TruthfulQA, and TriviaQA figures measure different constructs under different evaluators and should not be treated as one common performance scale.

# 17. Threats to Validity

| Validity dimension | Evidence-based concern |
|---|---|
| Internal validity | Model size, number of samples, and inference compute change together in the three flagship configurations |
| Construct validity | “Supported by references” is not identical to “true”; pairwise usefulness combines several qualities |
| Statistical conclusion validity | Most plots show ±1 standard error, but sample counts and formal hypothesis tests are generally absent |
| External validity | Training is overwhelmingly ELI5; TruthfulQA reveals distribution-shift failures |
| Ecological validity | Reddit-answer comparison required stripped references and simplified instructions; authors explicitly flag mismatch with actual ELI5 intent |
| Generalizability | English-language web search, particular contractors, GPT-3, and one search service define the studied setting |
| Reproducibility | Hyperparameters and preprocessing are detailed, but hardware, seeds, training compute, exact software versions, and full linked artifacts are not supplied |
| Temporal validity | Live-web content and search rankings can change; the paper does not quantify reproducibility across time |
| Measurement validity | RM score predicts human preference in the tested best-of-\(n\) range but can itself be optimized or overoptimized |

# 18. Future Work and Open Questions

## A. Future work proposed by the authors

- Decompose difficult comparison tasks into simpler subtasks.
- Use auxiliary annotation signals more effectively.
- Adapt RL objectives specifically for rejection-sampling performance.
- Explore shared policy/value networks.
- Train on adversarially selected questions.
- Improve source-trustworthiness judgments.
- Use debate or recursive reward modeling to elicit evidence for and against claims.
- Develop practical, cross-disciplinary standards for factual evaluation.
- Study and mitigate question-framing and cultural reference-point biases.
- Apply stronger safety measures, including possible tripwire tests, as web-capable models improve.
- Study how to reduce overreliance on authoritative-looking cited answers.

## B. Additional open questions

- **[D]** Would balanced retrieval objectives reduce cherry-picking without lowering usefulness?
- **[D]** How stable are judgments across cultures, professions, and political or epistemic viewpoints?
- **[D]** Can claim-level annotations outperform a single overall preference when scaled adequately?
- **[D]** How much of the gain arises from better retrieval, better synthesis, or simply sampling more complete trajectories?
- **[D]** How would the approach perform with frozen search results rather than a changing live web?
- **[D]** What error rate remains after checking whether citations actually entail each generated claim?

# 19. Terminology and Notation Glossary

| Term | Meaning in this paper |
|---|---|
| BC | Behavior cloning: supervised imitation of human demonstrations |
| Best-of-\(n\) | Generate \(n\) complete candidates and return the RM’s favorite |
| Demonstration | A human browser trajectory and answer |
| ELI5 | Questions from the “Explain Like I’m Five” subreddit |
| Elo score | Preference-oriented scalar where score differences map through a logistic function |
| GAE | Generalized Advantage Estimation, used in PPO |
| KL penalty | Penalty for moving the policy away from the BC policy |
| LFQA | Long-form question answering |
| PPO | Proximal Policy Optimization |
| Reference | A quotation, title, and domain saved during browsing |
| RM | Reward model trained to predict pairwise human preferences |
| RL | Reinforcement learning against the RM |
| TruthfulQA | Adversarial questions designed around common false beliefs |
| Validation RM | Separately split RM used to estimate performance and reduce direct optimization bias |
| \(A(q)\) | Distribution of model answers for question \(q\) |
| \(Q,\mathcal Q\) | A sampled question and the question distribution |
| \(R^{\text{train}}\) | RM used to choose a best-of-\(n\) candidate |
| \(R^{\text{val}}\) | Independent RM used to estimate the chosen candidate’s quality |
| \(R_n^{\text{pred}}(q)\) | Expected validation score after selecting the training-RM-best of \(n\) answers |
| \(\gamma,\lambda\) | GAE discount and bootstrapping parameters |
| \(\epsilon\) | PPO clipping parameter |
| Nat | Natural-logarithm unit used for KL divergence |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Demonstrations collected | 6,209 | records | All datasets | Author-reported | p. 16, Table 4 |
| Comparisons collected | 21,548 | pairs | All datasets | Author-reported | p. 16, Table 4 |
| Released comparisons | 19,578 | pairs | Suitable for RM | Author-reported | p. 32, App. K |
| RM training comparisons | ~16,000 | pairs | Final RMs | Author-reported | p. 5, §3.2 |
| RM evaluation-only comparisons | ~5,500 | pairs | Final split | Author-reported | p. 5, §3.2 |
| Researcher–labeler agreement | 74 | % | Final data collection | Author-reported | p. 17, App. C |
| Labeler–labeler agreement | 73 | % | Final data collection | Author-reported | p. 17, App. C |
| Demonstration time | ~15 | minutes/task | Human data collection | Author-reported | p. 17 |
| Comparison time | ~10 | minutes/task | Human data collection | Author-reported | p. 17 |
| Best model over demonstrators | 56 | % preferred | 175B best-of-64 | Author-reported | p. 5, Fig. 2a |
| Best model over ELI5 reference | 69 | % preferred | 175B best-of-64 | Author-reported | p. 5, Fig. 2b |
| TruthfulQA truthful | ~75 | % | 175B best-of-64 | Author-reported | p. 2; Fig. 3 |
| TruthfulQA truthful and informative | ~54 | % | 175B best-of-64 | Author-reported | p. 2; Fig. 3 |
| Empty TruthfulQA outputs | 74 (~3%) | answers | Truncation artifact | Author-reported | p. 7, fn. 3 |
| Best-of-64 BC over BC | 68 | % preferred | 175B | Author-reported | p. 7, §5.1 |
| RL over BC | 58 | % preferred | 175B | Author-reported | p. 7, §5.1 |
| Demonstration doubling effect | ~0.13 | RM-score points | BC scaling | Author-reported | p. 8, §5.2 |
| Comparison doubling effect | ~1.8 | percentage points | RM accuracy | Author-reported | p. 8 |
| Policy parameter doubling effect | ~0.09 | RM-score points | Noisy trend | Author-reported | p. 8 |
| RM parameter doubling effect | ~0.4 | percentage points | Accuracy | Author-reported | p. 8 |
| TriviaQA WebGPT-assisted | 69.5 | % exact match | Total development set | Author-reported | p. 24, Table 9 |
| TriviaQA GPT-3 ablation | 58.7 | % exact match | Total development set | Author-reported | p. 24, Table 9 |
| WebGPT-assisted absolute gain | 10.8 | percentage points | \(69.5-58.7\) | Analyst-derived | Table 9 |
| Stance-study questions | 60 | questions/model | 20 topics × 3 stances | Author-reported | p. 25 |
| Wedding outputs | 64 | answers | 175B BC | Author-reported | p. 25 |
| Wedding answers mentioning America | 20 | answers | Generic wedding prompt | Author-reported | p. 25 |
| Named non-American culture | 4 | answers | Vietnamese 1, Indian 1, Croatian 2 | Author-reported | p. 25 |
| Survey ratings | 41 | ratings/question | Three surveys | Author-reported | p. 19, Fig. 10 |
| Maximum evaluation actions | 100 | browser actions | Main models | Author-reported | p. 5 |
| Sampling temperature | 0.8 | unitless | Main evaluation | Author-reported | p. 5 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| A model can learn to use the browser at roughly human level | 56% preference over demonstrators | X1, Fig. 2a | pp. 5–6 | Strong within this evaluation; limited population |
| Human feedback improves beyond imitation | Best-of-64 BC beats BC 68% | X5, Fig. 5 | pp. 7–8 | Strong pairwise evidence; relies on RM selection |
| Rejection sampling outperforms RL here | 68% versus 58% gains over BC; combination adds little | Figs. 4–5 | pp. 7–8 | Good within tested tuning and compute regimes |
| Web-assisted answering reduces tested falsehood behavior | All WebGPT models exceed tested GPT-3 variants on TruthfulQA | X3, Fig. 3 | pp. 6–7 | Strong benchmark evidence; not equivalent to universal truthfulness |
| References aid evaluation | Detailed annotation workflow and agreement rates | Fig. 9; App. C | pp. 17–18 | Procedural support; no direct randomized ablation |
| More data and parameters improve proxies | Scaling trends in Figs. 6–7 | X7 | pp. 8–9 | Approximate; human evaluation largely replaced by RM proxy |
| Moderate rejection sampling is compute-efficient | Estimated Pareto frontier | Fig. 8 | p. 9 | Model-based/estimated frontier |
| Question framing can affect accuracy | Affirming forms visibly less accurate | X9, Fig. 11 | pp. 25–26 | Suggestive only; small sample |
| Generic prompts can expose cultural defaults | 20/64 America mentions and few named alternatives | X10 | pp. 25–26 | Concrete case study; narrow generalizability |
| Citations can increase perceived authority and risk | Conceptual discussion plus observed errors | Table 3, §6.2 | p. 10 | Plausible author argument; user reliance was not directly measured |

# 22. Very Simple Explanation

Imagine giving a language model a very limited web browser. It can type searches, open results, read text, save quotations, and then write an answer. Humans first show it how to do this. Other humans then compare its answers and say which are better. A second model learns those preferences and either trains the first model or chooses its best answer from many attempts.

This worked surprisingly well on the kind of explanatory questions it was trained on. The strongest version was preferred slightly more often than answers from the project’s human researchers and much more often than the particular Reddit answers stored in ELI5. It also answered misleading questions more truthfully than ordinary GPT-3 in the tested setup.

But searching the web does not automatically make an answer true. The model can find bad sources, misunderstand good sources, or choose only evidence that supports what the question already assumes. Citations can make such mistakes look especially convincing. The paper is therefore both a demonstration of a powerful research tool and a warning that “has references” is not the same as “has reached the truth.”

# Completeness Audit

## Coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract and §1 Introduction | Yes | Yes | Fully represented | Problem, contributions, headline results |
| §2 Environment design | Yes | Yes | Fully represented | Actions, state, memory, stop conditions |
| §3 Methods | Yes | Yes | Fully represented | Data and all four training methods |
| §4 Evaluation | Yes | Yes | Fully represented | ELI5, TruthfulQA, TriviaQA |
| §5 Experiments | Yes | Yes | Fully represented | Method comparison and scaling |
| §6 Discussion, §§6.1–6.5 | Yes | Yes | Fully represented | Truth, authority, bias, references, web risk |
| §7 Related work | Yes | Yes | Represented in compressed form | Major method families and positioning retained |
| §8 Conclusion | Yes | Yes | Fully represented | Incorporated in synthesis |
| §9 Author contributions | Yes | Partly | Deliberately compressed | Roles inventoried; individual names not repeated |
| §10 Acknowledgments | Yes | No | Deliberately omitted as non-substantive | Does not alter methods or findings |
| References | Yes | Partly | Represented in compressed form | Relevant method families retained; bibliography not reproduced |
| Figure 1 | Yes, visual | Yes | Fully represented | Both panels |
| Figures 2–8 | Yes, visual | Yes | Fully represented | Axes, legends, trends, caveats |
| Figures 9–10 | Yes, visual | Yes | Fully represented | Exact pie counts unavailable |
| Figures 11–12 | Yes, visual | Yes | Fully represented | Exact bar heights treated as approximate |
| Tables 1–13 | Yes | Yes | Fully represented | Table 10 examples summarized rather than recopied |
| Equation (1) | Yes | Yes | Fully represented | Form and role explained |
| Appendix I equations | Yes | Yes | Fully represented | Notation and estimator explained |
| Algorithms/pseudocode | Not applicable | Not applicable | None present | Procedures are prose and equations |
| Explicit research questions | Yes | Yes | None formally stated | Objectives distinguished from formal RQs |
| Formal hypotheses | Yes | Yes | None preregistered/stated | Post-result hypotheses identified |
| X1–X11 analyses | Yes | Yes | Fully represented | Separate experiment register supplied |
| Appendix A | Yes | Yes | Fully represented | Implementation details |
| Appendix B | Yes | Yes | Fully represented | Sources, processing, counts |
| Appendix C | Yes | Yes | Fully represented | Contractors and labeling procedure |
| Appendix D | Yes | Yes | Represented in compressed form | Survey items and trends retained |
| Appendix E | Yes | Yes | Fully represented | Hyperparameters and early stopping |
| Appendix F | Yes | Yes | Represented in compressed form | Full instruction wording not reproduced |
| Appendix G | Yes | Yes | Fully represented | TriviaQA setup and all main values |
| Appendix H | Yes | Yes | Fully represented | Both stance and reference-point analyses |
| Appendix I | Yes | Yes | Fully represented | Estimator derivation and caveat |
| Appendix J | Yes | Yes | Represented in compressed form | Long example passages not reproduced verbatim |
| Appendix K | Yes | Yes | Fully represented | Release count and schema |
| Author-stated limitations | Yes | Yes | Fully represented | Consolidated in §16 |
| Supplementary artifacts | No | No | Missing from supplied material | Links only |

## Missing or inaccessible material

- The linked demonstration instruction document was not supplied.
- The linked full comparison instruction document was not supplied; Appendix F supplies only the separate minimal ELI5-reference comparison instructions.
- The online answer viewer and additional samples were not supplied.
- The downloadable comparison JSONL file was not supplied.
- External cited works, live webpages, Bing outputs, and APIs were not inspected.
- Pages 11, 13, 14, 21, 23, and 32 were not rendered as images, although their complete native text was supplied.
- Exact numerical category counts in Figure 10 cannot be recovered from its unlabeled pie slices.

## Uncertain interpretations

- Some plotted bar and line values are unlabeled. Only author-stated values are treated as exact; other readings are described qualitatively or approximately.
- Figure 6’s log-like fractional progression and Figure 8’s compute frontier are visually clear, but exact coordinates are not labeled.
- Appendix I’s binomial-coefficient typography is OCR-sensitive; its mathematical meaning is nevertheless consistent across the extracted text and rendered page.
- The paper does not report sample counts for several principal pairwise evaluation plots, preventing independent reconstruction of standard errors.
- The transition from 21,548 collected comparisons to 19,578 released suitable comparisons is not itemized record by record.

## Deliberately compressed material

- The full author list appears in Stage 0 context but is not repeatedly reproduced.
- The complete bibliography and acknowledgments were inspected but compressed because they do not change the study’s reported methods or results.
- Table 10’s 60 question wordings were inspected but summarized by design and topic rather than copied in full.
- Appendices J’s long source excerpts and alternative answers were summarized because their evidentiary role is more important than verbatim reproduction.
- Appendix F’s complete instruction prose was compressed into its operative rules.

## Potential omissions

No substantive numbered figure, table, major equation, main section, experiment, contribution, author-stated limitation, or Appendix A–K is known to be unrepresented. The only omitted material is either bibliographic/acknowledgment content, repetitive example wording, or externally linked material that was not supplied.