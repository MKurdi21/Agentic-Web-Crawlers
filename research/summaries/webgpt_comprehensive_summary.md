## Stage 0 — Document Accessibility Report

The supplied work is available as page-delimited extracted text for physical PDF pages 1–32. All 32 text records were inspected. Rendered images were supplied and visually inspected for pages 1–10, 12, 15–20, 22, and 24–31: 26 visual pages in total. Pages 11, 13, 14, 21, 23, and 32 were inspected through supplied text only. Consequently, textual coverage is complete for the supplied 32-page sequence, while direct visual coverage is partial. The available text ends with Appendix K; no missing page number occurs in that sequence. This establishes continuity of the supplied document, not independent verification of its original file or supplements.

Figures 1–12 and Tables 1–13 are present. Their substantive contents are readable in the supplied images and text. Figure 12 does not repeat a model-size legend, so identifying individual model bars relies partly on adjacent figure order and the surrounding experiment description. Small plot positions support approximate estimates, not exact numerical transcription. The main retrieval equation on p. 12 and Appendix I equations on p. 28 are visually available. Their mathematical structure is readable; interpretation of reward-score ties in the Appendix I sorting procedure remains unspecified.

Appendices A–K are available. The accessibility metadata's detected appendix page list, [5], is not a reliable appendix inventory: headings in the supplied work clearly place Appendix A on p. 15 and Appendix K on p. 32. No embedded supplementary file was supplied. The paper references demonstration and comparison instruction documents, an answer viewer, and a downloadable comparison dataset. These external artifacts were not inspected. Appendix F supplies its minimal instructions in the document itself and was read. No OCR, browsing, code execution, or tool call was used. The failed local-image notice for '-' supplies no additional document evidence; the 26 attached images remain usable.

Evidence labels throughout this report are: [A] author-reported; [B] directly observable in supplied visuals; [C] analyst-derived with calculations shown; [D] analyst interpretation. No [E] external information is introduced. HIGH confidence indicates clear source support; MEDIUM indicates a qualified inference or approximate visual reading; LOW indicates weak or ambiguous evidence; UNKNOWN indicates unavailable information. Page locators refer to physical PDF pages, which align with the supplied page records.

## 1. Plain-language orientation

WebGPT studies how a language model can answer open-ended questions by searching the web, reading pages, collecting quotations, and writing an answer supported by those quotations. The researchers start with GPT-3 and teach it to operate a restricted text browser. Human examples teach browser actions; human preferences train a second model that scores answers. The strongest evaluated configuration generates multiple candidate answers and selects the one receiving the highest learned score. [A; pp. 1–5; HIGH]

The central problem is long-form question-answering: producing a useful paragraph rather than a short fact. A fluent answer can still be unsupported or misleading. The authors make references part of the process so evaluators can assess whether claims are backed by sources. This is easier than independently researching every possible claim, but it does not guarantee that the sources themselves are correct or fairly selected. [A; pp. 2, 11, 18]

The principal configuration, GPT-3 with 175 billion parameters followed by behavior cloning and best-of-64 selection, receives 56% overall preference against browser-using human demonstrators and 69% against highest-voted ELI5 Reddit answers. Ties contribute half a preference. These are comparative human judgments under particular protocols, not percentages of objectively correct answers. On TruthfulQA, the same configuration is reported as 75% truthful and 54% both truthful and informative, below the human reference performance. [A; pp. 2, 5–7]

For the user's security question, this paper provides architectural and risk evidence, not a direct comparative security experiment. It shows that a browser-enabled model consumes external information and takes actions affecting an external service. It also discusses misleading references, excessive trust in citations, and hypothetical manipulation of the world if stronger permissions were available. The inference that these pathways broaden an agent's security exposure is [D]. The paper does not establish that web agents are universally more vulnerable than standalone language models, and its truthfulness comparison cannot be relabeled as an attack-success comparison.

## 2. Document roadmap

The document is an empirical machine-learning and systems paper with a substantial methodological appendix. Its inventory is:

| Object | Location | Role |
|---|---|---|
| Abstract and §1 Introduction | pp. 1–2 | Problem, two contributions, overview of results |
| §2 Environment design | p. 3 | Browser observations, commands, references, termination |
| §3.1 Data collection | pp. 3–4 | Human demonstrations and preferences |
| §3.2 Training | pp. 4–5 | Behavior cloning, reward modeling, reinforcement learning, selection |
| §4.1 ELI5 | pp. 5–6 | Two human-comparison protocols |
| §4.2 TruthfulQA | pp. 6–7 | Truthfulness and informativeness |
| §4.3 TriviaQA | p. 7 | Pointer to short-answer transfer evaluation |
| §5.1 Training-method comparisons | pp. 7–8 | Reinforcement learning and best-of-n experiments |
| §5.2 Scaling | pp. 8–9 | Data, model size, inference computation |
| §6.1–6.5 Discussion | pp. 9–11 | Falsehoods, perceived authority, bias, references, web risks |
| §7 Related work | pp. 11–12 | Retrieval and browser-control approaches |
| §§8–10 | pp. 12–13 | Conclusion, author contributions, acknowledgments |
| References | pp. 13–14 | Bibliographic attribution |
| Appendices A–C | pp. 15–18 | Environment, datasets, annotation procedures |
| Appendix D | p. 19 | Contractor survey |
| Appendix E | pp. 20–22 | Hyperparameters and implementation qualifications |
| Appendix F | p. 23 | Minimal comparison instructions |
| Appendices G–H | pp. 24–27 | TriviaQA, question stance, cultural reference bias |
| Appendix I | p. 28 | Efficient estimator for best-of-n performance |
| Appendices J–K | pp. 29–32 | Example evidence and released dataset format |

The original title is **WebGPT: Browser-assisted question-answering with human feedback**. The supplied version is arXiv:2112.09332v3, classified cs.CL, dated 1 June 2022. No conference or journal venue is specified. All authors are affiliated here with OpenAI: Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, Xu Jiang, Karl Cobbe, Tyna Eloundou, Gretchen Krueger, Kevin Button, Matthew Knight, Benjamin Chess, and John Schulman. The first three carry equal-contribution marks; their order is described as randomized. No keywords, formal theorem, or numbered pseudocode algorithm is supplied.

## 3. Background and context

Natural language processing, or NLP, concerns computational handling of language. Here the task is long-form question-answering, or LFQA: generating a paragraph-length response to an open-ended question. Retrieval means finding relevant information; synthesis means assembling information into an answer. The authors reuse Bing for retrieval and GPT-3's pretrained language capabilities for synthesis instead of building both components from scratch. [A; pp. 1, 3]

Behavior cloning, or BC, is supervised imitation: the model learns from commands and answers demonstrated by humans. Reward modeling, or RM, learns a numerical score from comparisons between answers. Reinforcement learning, or RL, changes the answering policy to increase the learned reward. Proximal policy optimization, or PPO, is the particular RL algorithm named in the paper. Its full mathematical algorithm is not reproduced. Best-of-n, called rejection sampling here, generates n candidates and selects the highest-scoring one. It is selection among complete attempts, not a proof that the selected answer is true. [A; pp. 4–5]

A policy is the model's behavior for choosing outputs or actions. Inference-time compute is computation spent while producing an answer, rather than while training. A reward model can be overoptimized: higher scores can cease to correspond reliably to better human judgments. The paper uses a separate validation reward model to assess some scaling experiments, while explicitly warning that even this evaluator can eventually be overoptimized. [A; pp. 8, 28]

ELI5 means Explain Like I'm Five and supplies Reddit questions and reference answers. TruthfulQA is described as an adversarially constructed collection of questions designed to elicit misconceptions. This is adversarial in the benchmark-design sense; the paper does not describe malicious web-page instructions or a network attacker. TriviaQA supplies short-form trivia questions. AI2 Reasoning Challenge, or ARC, supplies school-level science questions. [A; pp. 2, 6, 16]

## 4. Research problem and gap

The authors describe LFQA as falling behind human performance and identify retrieval and synthesis as its main ingredients. Their proposed gap is the objective used to combine those ingredients: demonstrations alone imitate existing behavior, whereas direct feedback can optimize the quality humans care about. They seek an environment in which humans and language models can perform substantially the same task, enabling demonstrations, preference judgments, and general optimization methods. [A; pp. 1–3]

According to the authors, modern search engines already offer powerful access to many up-to-date documents. Using Bing therefore shifts attention to the higher-level task of search-engine use. They also report prior findings that automated metrics such as ROUGE-L are not meaningful for this LFQA setting, motivating human comparisons. These are the paper's descriptions of prior research; this report does not independently validate that literature. [A; pp. 3, 12]

The scope is answer generation through a constrained browser. It is not a general-purpose graphical browser agent, an autonomous account operator, or a security benchmark. The environment exposes search, page navigation, scrolling, finding text, quotation, and ending. Form submission and direct page editing are outside its action set. This scope matters when transferring its discussion to contemporary or hypothetical agents with wider permissions. [A; pp. 3, 11]

## 5. Research questions, objectives, and hypotheses

No formal numbered research questions or preregistered hypotheses are presented. The following objectives organize the supplied experiments without pretending that the authors stated them as formal questions:

- **O1:** Build a text browser that a language model can learn to use and combine retrieval with synthesis.
- **O2:** Improve answer quality using human demonstrations and preferences.
- **O3:** Compare resulting answers with human demonstrations, ELI5 reference answers, and base GPT-3 truthfulness.
- **O4:** Compare reinforcement learning with best-of-n selection and examine scaling with data, parameters, and computation.
- **O5:** Examine question framing and cultural reference-point assumptions.

Explicit hypotheses or proposed explanations include: reliable-source incentives may explain fewer imitative falsehoods; ELI5-to-TruthfulQA distribution shift may explain unreliable sourcing; WebGPT may produce fewer non-imitative falsehoods, although that hypothesis was not tested directly; differing TriviaQA overlap results may reflect its small TriviaQA training exposure. Possible explanations for selection outperforming RL are presented as possibilities, not experimentally isolated causes. [A; pp. 7–9, 24]

The user asks why web AI agents may be more vulnerable than standalone LLMs. That is an additional research framing, not this paper's stated objective. This analysis uses WebGPT as evidence about mechanisms and boundaries, with security relevance explicitly labeled [D].

## 6. Assumptions / Threat Model

There is no formal security threat model with attacker identities, capabilities, budgets, assets, or success metrics. The practical system model is a language model receiving textual browser state and issuing commands through an environment. Only Bing queries and following existing links interact with the outside world. Browsing and answering are separated: final generation receives the question and collected quotations. Context is reconstructed each step; memory of prior browsing is limited to the state summary. [A; pp. 3, 11, 15]

The quality procedure relies on evaluators assessing source trustworthiness and claim support. Bing filtering and instructions to prefer reliable sources are discussed as possible reasons for improved truthfulness. The authors nevertheless acknowledge unreliable quotations and judgment calls about trustworthiness. Thus neither search results nor citations are established as universally trustworthy. [A; pp. 9, 11, 17–18]

The live-web risk example is conditional: if forms were accessible, an agent could edit Wikipedia to create a credible-looking reference, potentially receiving RL reinforcement for doing so. The authors say direct editing is unavailable and assess current side-effect exploitation risk as very low. Their comment about more capable systems escalating privileges is speculative, not a demonstrated exploit. [A; p. 11]

**Security interpretation [D; MEDIUM]:** external pages, search results, quotations, and executable browser commands create additional information and action boundaries worth examining. However, supplied evidence does not establish prompt injection, credential theft, data exfiltration, malware execution, successful privilege escalation, or comparative vulnerability rates. The factuality failures reported here must not be automatically classified as attacker-induced compromises.

## 7. Methodology

### Browser architecture and workflow

The observation contains the question, accumulated quotations, past-action summary, page title, cursor or scrollbar position, current page text, actions remaining, and the next-action prompt. Figure 1 contrasts the graphical demonstration interface with this text observation. The page content is abridged for the illustration. A generated valid command invokes an environment action, then a fresh observation is supplied. Invalid commands consume an action allowance but have no other effect. [A/B; pp. 2–3]

Commands are Search, Clicked on link, Find in page, Quote, Scrolled down, Scrolled up, Top, Back, End: Answer, and End: Nonsense or Controversial. Scroll distances are 1, 2, or 3. A quotation must match text on the current page; its title, domain, and extract become a reference. Browsing ends on an end command, the action limit, or the total-reference-length limit. A final answer is requested only if at least one reference exists. The numerical total-reference-length limit is not supplied. [A; p. 3]

The implementation is mostly Python with some JavaScript. Bing responses become simplified result pages. Clicking runs a Node.js fetch-and-simplify script using Mozilla Readability.js. Remaining HTML is converted with html2text. PDFs use pdfminer.six; other supported text types use raw text. Unsupported content, errors, and timeouts produce error messages. Images become alt-text placeholders, not visual observations for the model. Superscripts and subscripts become textual ^ and _. Library versions and detailed hardware are not reported. [A; p. 15]

Links receive indexed delimiters and destination-domain text, omitted when source and destination domains match. Special delimiter characters in page content are replaced by alternatives. Search results and links to Reddit and Quora are removed to discourage copying. Pages with a 10-gram overlap with the question or supplied reference answer are censored. These are anti-copying and benchmark-contamination precautions; the paper does not test them as security defenses. Quote matching ignores case and whitespace and supports abbreviated start/end text; find matching ignores case with links stripped. [A; p. 15]

### Data and collection

Table 4 reports 6,209 demonstrations and 21,548 comparisons. Dataset rows are ELI5: 5,711/21,068; ELI5 fact-check: 67/185; TriviaQA: 143/134; ARC Challenge: 43/84; ARC Easy: 83/77; hand-written: 162/0. The approximate main-text totals of 6,000 and 21,500 therefore summarize, rather than contradict, these exact totals. [A; pp. 3, 16]

ELI5 preprocessing retains full URLs, excludes deleted titles, ignores deleted or removed selftext, joins title and nonempty body with a blank line, and prepends Explain: when neither a question mark nor specified question-like word patterns occur. ARC questions retain labeled alternatives in a free-form prompt. Fact-check examples ask an instruction-following model's ELI5 answer to be checked claim by claim. The lengthy word-pattern list is deliberately compressed here; its role and matching rules are retained. [A; p. 16]

Ten Upwork contractors supplied about 25% of data; 46 Surge AI contractors supplied about 75%. Five contractors supplied about half of all data. Workers were generally educated to undergraduate level or above, underwent paid trials and manual checks, and were paid by hours. Demonstrations averaged about 15 minutes and comparisons about 10. Approximately 100 researcher-completed comparison tasks supported agreement monitoring. Researcher–labeler agreement was 74%; labeler–labeler agreement was 73%, with neutral versus nonneutral agreement counted as 50%. [A; p. 17]

Human demonstrators had substantially the same information and actions as the model, with two qualifications: humans were not shown past-action summaries, and repeated one-step human scrolling was merged into multi-step commands. Comparison workers rated source trustworthiness, claim support and relevance, coherence, and overall usefulness. They were not required to conduct independent research for this detailed procedure. Supported meant backed by a reliable reference or common knowledge. [A; pp. 17–18]

Preference ratings used five options from A much better to B much better. Training collapsed better and much better and used only the final comparison rating; ties became soft 50% labels. Auxiliary prediction of other annotation information did not significantly improve RM validation accuracy. Most detailed annotation steps were mandatory in 10% of tasks and optional in 90%; requirements changed near project end. This evolving procedure is a substantive qualification, not a fixed universal annotation protocol. [A; p. 18]

### Training and evaluation settings

BC, RM, and RL used mutually disjoint question sets. About 4% of demonstrations were held out for BC validation. Final reward models used about 16,000 comparisons; about 5,500 were evaluation-only. Comparison candidates were collected ad hoc from varied models and settings, primarily 175B models. Exact membership and all tuning histories are not supplied. [A; p. 5]

BC fine-tunes GPT-3 on demonstration commands. RM starts from BC without its final unembedding layer and outputs a scalar for question, answer, and references. Cross-entropy training uses human preferences. Score differences are preference logits in an Elo-like scale. RL starts from BC and uses PPO with final reward score plus per-token Kullback–Leibler, or KL, penalties relative to BC. Selection samples 4, 16, or 64 answers and chooses the largest RM score. [A; p. 4]

RL questions were 90% ELI5 and 10% TriviaQA. Each browsing episode was followed by 15 additional answer-only episodes using its references, yielding 16 answering phases per browsing phase. This approximately doubled sample efficiency. Browsing limits during RL were sampled uniformly from integers 20–100 inclusive. The main evaluations used temperature 0.8 and at most 100 browsing actions. Their three configurations were 760M best-of-4, 13B best-of-16, and 175B best-of-64, with policy and scoring model of equal size. RL was omitted from these main configurations. [A; p. 5]

Tables 5–8 and Appendix E supply training settings. BC and RM use exponential moving averages of weights with decay 0.99. A bug meant the 760M and 13B RL experiments did not use EMA reward models, while rejection sampling did. PPO uses separate policy/value networks, token-level clipping and KL rewards, completion-level timestep reporting, and chunking of long completions into up to 64-token actions. GPU memory constraints influenced minibatching, but GPU models, counts, random seeds, and total training costs are unspecified. [A; pp. 20–22]

Human preference is the principal LFQA metric. Plot uncertainty is ±1 standard error where stated, not a 95% confidence interval. The supplied work does not give a complete statistical-testing protocol or all evaluation sample counts. TruthfulQA base GPT-3 scores use an automated metric; WebGPT uses human evaluation. This asymmetric measurement is justified by the authors as avoiding an out-of-distribution automated metric, but it limits treating the comparison as identical measurement throughout. [A; pp. 6–7]

## 8. Experiments / Analyses

| ID | Purpose and setup | Results and qualifications |
|---|---|---|
| X1 | ELI5 test answers versus browser-using human demonstrators; three model/selection configurations; detailed comparison procedure | 175B best-of-64: 56% overall preference, ties half; Figure 2a. Relative usefulness, not 56% factual accuracy. |
| X2 | ELI5 answers versus highest-voted Reddit reference answers; citations stripped, new contractors, minimal instructions | 175B best-of-64: 69% overall preference; Figure 2b. Styles remain distinguishable and reference answers may be low effort. |
| X3 | TruthfulQA; base GPT-3 with QA/helpful prompts versus WebGPT; short-answer truncation | Best WebGPT: 75% truthful, 54% truthful and informative; Figure 3. Different evaluator types; 74 truncation-induced empty answers counted truthful but uninformative. |
| X4 | RL and selection versus BC, with model size varied | 175B RL preferred over BC 58%; 175B BC best-of-64 preferred over BC 68%; Figures 4–5. Combined RL/selection adds little; proposed causes are not isolated. |
| X5 | Scale demonstration fraction and policy size; evaluate with separate 175B validation RM | Doubling demonstrations: about +0.13 score; doubling policy parameters: roughly +0.09; Figure 6. Proxy metric and noisy parameter trends. |
| X6 | Scale comparison fraction and RM size; measure preference-prediction accuracy | Doubling comparisons: about +1.8% accuracy as worded; doubling RM parameters: roughly +0.4%; Figure 7. Prose does not explicitly distinguish percentage points from relative percent. |
| X7 | Trade best-of-n sample count against policy/RM size and inference operations | Some selection is generally compute-efficient; main configurations lie on estimated frontier; Figure 8. Frontier is estimated, not a universal optimum. |
| X8 | TriviaQA transfer; 175B BC at temperature 0.8, no selection; answer extractor fine-tuned on 256 questions | Combined system: 69.5% total exact match; Table 9. Uses much more compute and live web than UnitedQA. |
| X9 | Question stance; 10 conspiracy topics plus 10 misconceptions, each with three framings; three WebGPT configurations | Affirming questions suggest lower factual accuracy; no clear stance effect on answer affirmation/refutation; Figures 11–12. Small sample and verification-based accuracy rule. |
| X10 | Reference-point bias; 64 unselected 175B BC answers to one wedding question | 20 mention America/American; four focus on named non-American cultures; eight deny a standard wedding. Single-question case study. |
| X11 | Contractor satisfaction; three surveys of workers completing at least 32 tasks | 41 ratings per question, not necessarily 41 distinct people; Figure 10. Survivor selection excludes early dropouts. |
| X12 | Separate validation RM predicts selection performance using efficient estimator | Figure 5 agreement is good for n ≤64; Appendix I warns eventual overoptimization. Prediction is not independently established for arbitrary large n. |

For X8, the extractor used batch size 32 and learning rate 1.5 × 10^-6, in addition to the 143 TriviaQA demonstrations used by WebGPT. Its ablation was GPT-3 fine-tuned without WebGPT output. Results use the development-set overlap splits attributed to Lewis et al.; they are not an untouched TriviaQA test-set result. [A; p. 24]

For X9, an answer was labeled inaccurate when more than around 25% of its central or specific claims could not easily be verified. That operational rule is not equivalent to proving those claims false. If an answer initially affirmed a misconception but then said it was a myth, it counted as refuting. Factual correctness and stance therefore intentionally differ. [A; p. 25]

## 9. Results

The best LFQA configuration exceeds half preference against human demonstrators and substantially exceeds half against Reddit reference answers. The authors regard the demonstrator comparison as more meaningful because references aid fact checking, detailed criteria aid consistency, styles are more similar, and effort and intended answer type are better controlled. They explicitly caution that the Reddit comparison is less blinded and may penalize links that workers were told not to follow. [A; pp. 5–6]

Figure 2 does not show uniform superiority on every dimension. The 175B system's coherence is below 50% preference against human demonstrations, while factual-accuracy preference is near 50%. Its 56% overall usefulness preference therefore cannot be converted into superiority in coherence or independently verified truth. Against Reddit answers, larger models show stronger usefulness and factual-accuracy preference. Exact component values are not printed; visual estimates are discussed below. [B; p. 6]

On TruthfulQA, all evaluated WebGPT configurations exceed all plotted base GPT-3 prompt configurations on truthful and truthful-and-informative percentages. The strongest model is 75% truthful and 54% both truthful and informative. However, the 13B WebGPT truthful-only bar is visually higher than the 175B bar; the claim that every truthfulness measure improves monotonically with size would be wrong. The authors specifically emphasize increasing truthful-and-informative performance. [A/B; pp. 2, 7]

Selection is a major contributor: 175B best-of-64 BC is preferred over 175B BC 68%, compared with 58% for 175B RL versus BC. These compare each optimized method against BC, rather than directly reporting a 68%-to-58% head-to-head contest. Their difference is **10 percentage points [C: 68 − 58]**, but this derived difference is between two preference statistics with separate conditions. It is not a direct win rate between selection and RL. [A/C; p. 7]

TriviaQA gains are strong but conditional. Combined GPT-3 plus WebGPT reaches 69.5% overall exact match versus 58.7% for its no-WebGPT ablation: **10.8 percentage points [C: 69.5 − 58.7]**. On the no-overlap split, 52.4% versus 39.0% yields **13.4 percentage points [C]**. These measure a two-stage pipeline, not the browser model alone. [A/C; p. 24]

Bias findings are narrower than a blanket claim that models mirror questions. Affirming framing gives suggestive accuracy degradation, but explicit answer stance does not clearly depend on question stance. The wedding case shows a Western/American default for one prompt, with potential contributions from pretraining, search, workers, and researchers suggested rather than causally identified. [A; pp. 25–26]

## 10. Figure-by-figure interpretation

### Figure 1 — Human and model browser observations

On p. 2, panel a is a graphical interface; panel b is its textual model observation. The question concerns crows bringing gifts. The interface combines question, search results, quotations, navigation, action count, and completion control. The textual panel explicitly groups Question, Quotes, Past actions, Title, Scrollbar, Text, Actions left, and Next action. It shows an action history containing search, click, quote, and back. This demonstrates the iterative observation/action arrangement and recorded evidence. It is an abridged illustration, not an independently evaluated successful answer. There are no quantitative axes. [A/B; HIGH]

### Figure 2 — ELI5 preferences

On p. 6, two grouped bar charts compare WebGPT against human demonstrations, panel a, and ELI5 references, panel b. Horizontal categories are overall usefulness, coherence, and factual accuracy; vertical axes are WebGPT preferred %, approximately 0–70 with linear spacing. Light, medium, and dark blue encode 760M best-of-4, 13B best-of-16, and 175B best-of-64. A dashed 50% line marks equal preference. Error bars are ±1 standard error.

Panel a visually places overall usefulness near 25%, 45%, and 56%; coherence near 25%, 42%, and 43%; factual accuracy near 47%, 52%, and 51%. Panel b places overall usefulness near 40%, 64%, and 69%; coherence near 42%, 53%, and 58%; factual accuracy near 47%, 64%, and 66%. Only 56% and 69% overall values are exact prose-reported results here; the remaining values are **approximate visual estimates [B; MEDIUM]**. Factuality judgments in panel b were made without the model references. The plot supports distinct outcome dimensions, not one undifferentiated accuracy score.

### Figure 3 — TruthfulQA

On p. 7, grouped bars compare GPT-3 QA prompt, GPT-3 helpful prompt, and WebGPT. Each group includes 760M, 13B, and 175B. The vertical axis is percentage from 0 to 100, linear. Blue filled bars represent truthful answers; white outlined bars represent truthful and informative answers. Horizontal dashed/dotted human reference lines are visually near 94% and 87%, respectively, **approximate visual estimates**. Error bars are ±1 standard error.

WebGPT truthful-only bars are approximately 70%, 78%, and 75%; truthful-and-informative bars approximately 33%, 48%, and 54%. The 175B figures 75% and 54% are author-reported. Helpful-prompt GPT-3 improves truthful-only scores at larger sizes but leaves truthful-and-informative scores near the low twenties. This reveals abstention/informativeness tradeoffs. Answers were truncated to 50 tokens and trailing partial sentences removed; empty answers receive truthful but uninformative labels. Baseline and WebGPT evaluation methods differ. [A/B]

### Figure 4 — Reinforcement learning versus cloning

On p. 8, grouped bars show RL preferred over BC %, with a linear vertical axis approximately 0–60 and dashed 50% equality line. Left grouping is best-of-1; right grouping uses size-specific best-of-n. Blue shades identify model sizes. Best-of-1 bars are approximately 53%, 56%, and 58%; best-of-n bars approximately 49%, 57%, and 47%. These are visual estimates except the 175B 58% reported in text. Error bars are ±1 standard error. The caption's supported conclusion is small RL improvement without selection and little benefit when selection is used. It does not justify asserting significant harm from RL solely because one bar is below 50%.

### Figure 5 — Benefit of additional samples and evaluator prediction

On p. 8, the horizontal axis is number of sampled answers, with 1, 4, 16, and 64 at logarithmically spaced positions. The vertical axis is best-of-n BC preferred over BC %, approximately 50–75. A blue line represents human preference, a shaded blue band ±1 standard error, and a black dashed line the validation RM prediction. Both rise from 50% at n=1 toward about 68% at n=64. Agreement supports the estimator in this setting. Human gains between 4 and 16 appear smaller than those between 1 and 4; exact intermediate values are not labeled. Prediction validity is qualified for larger n in Appendix I.

### Figure 6 — Demonstration-data scaling

On p. 9, horizontal ticks are demonstration fractions 1/8, 1/4, 1/2, and 1, logarithmically spaced by doubling. The vertical axis is validation RM score, with linear labeled intervals 0.00, 0.25, 0.50, 0.75, and 1.00. Three blue curves labeled 760M, 13B, and 175B increase with dataset fraction; larger models are higher. No error bars are shown. The prose reports about +0.13 score per doubling of demonstrations and roughly +0.09 per doubling of parameters. These are reward-score changes, not percentage-point human-preference changes.

### Figure 7 — Reward-model scaling

On p. 9, horizontal ticks are comparison fractions 1/8 through 1 with doubling spacing. Vertical axis is accuracy %, approximately 60–80, linear. Three labeled model curves rise with comparison data, with 175B highest. Dashed/dotted horizontal references mark an ensemble of humans near 79% and a human baseline near 73%, **approximate visual estimates**. No uncertainty bars are shown. Accuracy means preference-label prediction in this context, not answer factual accuracy. The text reports about 1.8% accuracy gain per doubling comparisons and roughly 0.4% per doubling RM parameters without fully clarifying relative-percent versus percentage-point wording.

### Figure 8 — Inference-compute frontier

On p. 9, the horizontal axis is floating-point operations on a logarithmic scale, labeled 10^14 through 10^17; vertical axis is validation RM score with linear ticks 0.0, 0.5, and 1.0. Curves for 760M, 13B, and 175B vary selection count while scaling policy and scoring-model sizes together. A gray dashed estimated frontier and star markers identify 760M bo4, 13B bo16, and 175B bo64. It illustrates spending compute on either larger models or more attempts. Exact star coordinates and full compute accounting are not printed; no exact cost reconstruction is possible.

### Figure 9 — Claim-support annotation

On p. 18, a screenshot displays question and answer panes, references, and annotation controls. Colored text highlights and controls distinguish strong support, weak support, no support, and citation error; reference trustworthiness labels are also visible. It shows how evaluators connect answer claims to source support and relevance. The figure is an interface example, not measured agreement data. Its substantive relationship is to Appendix C's multistep comparison procedure.

### Figure 10 — Contractor survey

On p. 19, five pie charts represent clarity of instructions, enjoyment, repetitiveness, fairness of pay, and overall satisfaction. Colors run from red strong disagreement through orange disagreement and yellow neutral to light/dark green agreement. Most areas for clarity, enjoyment, pay, and overall satisfaction are green. Repetitiveness has appreciable disagreement and neutral areas alongside agreement. Exact category percentages are not labeled and are not reconstructed here. The caption reports 41 equally weighted ratings per item across three surveys, including repeated contributors. This is not a five-chart experiment on model performance.

### Figure 11 — Framing and answer accuracy

On p. 26, grouped bars compare affirming, neutral, and skeptical question stance. Vertical axis is accurate answers %, 0–100, linear. Blue shades identify the three WebGPT configurations. Approximate values are affirming 80/70/85%, neutral 80/90/95%, and skeptical 95/95/95% for increasing sizes. These are **approximate visual estimates**, not printed numerical results. There are no error bars. It supports suggestive framing sensitivity, with the authors explicitly warning that the sample is too small for definitive conclusions.

### Figure 12 — Framing and answer stance

On p. 26, 100% stacked bars use the same question-stance categories and vertical percentage scale. Orange/red encodes refutation, purple neither, and green affirmation. Within each question category there are three bars corresponding to the three evaluated configurations; the panel lacks its own explicit size legend, so exact per-model assignment is qualified. Refutation generally occupies more area for larger-model positions. For the affirming group, approximate refutation portions are 45/55/55%; neutral approximately 40/45/55%; skeptical approximately 40/60/70%. These small-chart estimates are MEDIUM-to-LOW confidence and are not used as exact findings. The substantive author conclusion is no clear question-stance effect on this behavior, while larger models tend to refute more often. This must be preserved alongside Figure 11's distinct accuracy result.

## 11. Table-by-table interpretation

### Table 1 — Command interface

On p. 3, command/effect rows specify all ten action forms described in §7 above. Search calls Bing; clicks follow indexed links; find and scroll change the visible location; quote records matching evidence; end either moves to answering or skips it. Invalid generated text consumes the action allowance. This table defines capability boundaries; it contains no success-rate result or direct write-to-web action.

### Table 2 — Model example

On p. 4, a randomly selected ELI5 test question asks why some words are considered bad in social settings. The 175B best-of-64 answer discusses varying histories and cultural meanings, taboo subjects, derogatory language, and emotional expression. Five references are listed by title; three extracts originate from one Vermont Public Radio page. In-text citations principally point to extracts [2] and [3]. The caption says the question was not cherry-picked, but this remains one example rather than a statistical evaluation.

### Table 3 — Selected TruthfulQA success and failure

On p. 10, columns are GPT-3 175B QA prompt, GPT-3 175B helpful prompt, and WebGPT 175B best-of-64's first sentence. A mirror-breaking question elicits superstition from QA-prompt GPT-3, abstention from helpful GPT-3, and a practical injury/anger answer from WebGPT. A wishing question elicits abstentions from GPT-3 and a false power-of-thought assertion from WebGPT. Colored marks distinguish false, true-uninformative, and true-informative. These are explicitly cherry-picked contrasting examples. The caption also reports helpful GPT-3 saying I have no comment for 49% of questions. The table demonstrates possible outcomes, not their frequency except that caption statistic.

### Table 4 — Exact collection counts

On p. 16, rows are question datasets and columns demonstrations/comparisons. ELI5 5,711/21,068; fact-check 67/185; TriviaQA 143/134; ARC Challenge 43/84; ARC Easy 83/77; hand-written 162/0; totals 6,209/21,548. There is no missing-value notation or uncertainty interval. ELI5 dominance is clear; zero hand-written comparisons is a reported zero, not missing data.

### Table 5 — Base optimizer step sizes

On p. 22, 760M uses 2.5 × 10^-4, 13B uses 1.0 × 10^-4, and 175B uses 0.6 × 10^-4 as base Adam step sizes. Training multipliers in subsequent tables apply to these bases. These are configuration parameters attributed to pretraining settings, not performance measurements.

### Table 6 — BC and RM settings

On p. 22, default minibatches are BC 512 and RM 64; footnotes change BC 760M to 256 and RM 175B to 32. Step-size multipliers are BC 0.1 and RM 0.05, except RM 175B uses 1/60. Epoch upper bounds are 12 and 6; both EMA decays are 0.99. Upper bounds are not actual training durations, which Table 8 reports. Footnote exceptions are necessary to reproduce the stated conditions.

### Table 7 — RL settings

On p. 22: 256 parallel environments; 256 timesteps per rollout; one epoch; 128 minibatches per epoch; Adam multiplier 0.004; KL reward coefficient 0.02; entropy coefficient 0; PPO clipping 0.2; generalized advantage estimation, or GAE, discount γ=1 and bootstrapping λ=0.95; no reward normalization; advantage normalization enabled; 16 answering phases per browsing phase; 64 maximum tokens per action. Completion-level timestep reporting and token-level computations are explained in Appendix E, so these numbers cannot be interpreted as one uniform token-level rollout specification.

### Table 8 — Actual stopping points

On p. 22, rows 760M/13B/175B have BC epochs 2/5/3; RM epochs 1/1/1; RL PPO iterations 19/30/18; episode KL 10.5/6.8/approximately 12 nats. Nats are the reported KL unit. These are training stopping criteria/results, not answer-quality scores. Smaller models received less hyperparameter-tuning effort, and their RL reward-model EMA bug is relevant.

### Table 9 — TriviaQA exact match

On p. 24, columns are total, question overlap, no question overlap, answer overlap, answer overlap only, and no overlap. GPT-3 175B scores are 58.7/75.9/52.9/67.3/61.6/39.0%. GPT-3 175B plus WebGPT 175B BC scores are 69.5/86.3/65.3/78.4/73.2/52.4%. UnitedQA-E scores are 68.9/89.3/62.7/78.6/70.6/44.3%. UnitedQA hybrid reports only total 70.5%; other split results are Not reported.

The hybrid has the highest reported total; UnitedQA-E leads question-overlap and answer-overlap columns; the combined WebGPT system leads no-question-overlap, answer-overlap-only, and no-overlap columns. Bold indicates leading values, not statistical significance. No error intervals or tests are provided. The columns are overlapping dataset partitions and must not be summed into a total. Compute and corpus access differ across systems.

### Table 10 — Question-framing materials

On p. 27, twenty topic rows each have skeptical, neutral, and affirming questions. Topics include black helicopters, moon landing, chemtrails, aliens, Nero, JFK assassination, animal spies, HAARP, Area 51, Denver Airport, Walt Disney, fortune cookies, Twinkle Twinkle, worms, tongue taste, sunflowers, brain power, carrots, 420, Buddha, and Mary Magdalene. The authors describe the first ten as conspiracy topics and the last ten as misconceptions. The design yields 60 questions. Exact wording of all questions is compressed; differences can change content as well as stance, such as asking when a landing occurred versus why it was faked. This is an analyst observation about the visible stimulus design, not a demonstrated confound effect.

### Table 11 — Model references

On p. 29, five source extracts support Table 2. They cover scholarly discussion of swearing, historical and cultural variation, taboo categories and emotion, sanctioned terms, and offensive taboo subjects. Extracts [1]–[3] share a source. This permits inspection of correspondence between the generated answer and its selected evidence. It does not establish that the extracts exhaust relevant evidence or that every source claim is independently true.

### Table 12 — Human answer and references

On p. 30, a demonstrator answer uses three extracts concerning swearing, dehumanizing language, and the history of a slur. It is longer and more specific than Table 2. The answer and a source extract both contain the questionable phrase hundreds of centuries, and the source juxtaposes late 1800s with a named 1854 work. These are directly observable internal chronological wording tensions; this closed-document report neither repairs them nor imports outside history. They illustrate that source-backed repetition alone does not settle factual soundness. No independent score for this example is supplied.

### Table 13 — Reddit reference answer

On p. 31, one short answer recommends a podcast about swear/curse words and says the terms differ. It does not provide a developed explanation like the model and human examples. Its brevity illustrates answer-format differences for one question, not the distribution of quality throughout ELI5.

## 12. Diagram / Architecture Interpretation

No standalone architecture or flowchart is supplied. Figures 1 and 9 are interface screenshots, already visually inspected. A faithful textual reconstruction is: question → browser-state observation → language-model command → environment execution → updated observation; repeated browsing collects references; termination → question plus references → final answer. Search connects to Bing, navigation fetches existing pages, and conversion returns textual content. [A; pp. 2–3, 15]

Training adds another loop: demonstrations → BC policy; pairwise answers and human comparisons → reward model; BC plus reward model → either PPO optimization or best-of-n selection. A separate validation RM assesses some experiments. The policy controls evidence acquisition, while the RM scores final question/answer/reference bundles. This distinction explains why source selection and presentation can affect incentives. [A; pp. 4–5, 28]

**Analyst interpretation [D]:** this architecture creates several places where correctness can fail: retrieval can return unreliable material; extraction can discard context; selection can favor convincing evidence; synthesis can misstate an extract; evaluation can mistake support for truth. The authors directly discuss several of these quality problems, but do not measure a security attack at each boundary. The model's lack of visual page understanding is explicit in the environment's image-to-alt-text conversion, rather than a limitation of this report's visual inspection.

## 13. Equations and mathematical concepts

### E1 — Related-work retrieval equation, p. 12, Eq. (1)

`p(passage | query) ∝ exp(embed(passage) · embed(query))`.

The left side is a conditional passage probability given a query. The functions embed map passage and query into representations; the dot is their inner product; exp is exponentiation; proportionality means the expression omits a normalizing factor. The equation assigns relatively greater weight to passages with larger embedding inner products. Dimensions, normalization details, and embedding implementation are not supplied here. It describes the differentiable-retrieval family in related work, not WebGPT's Bing retrieval algorithm. The authors contrast fast differentiable optimization with difficulties handling search-engine operations and reduced interpretability. [A]

### E2 — Reward score and preference, pp. 4, 8

The prose says a reward difference is the logit of one answer's preference probability. Its mathematical restatement is `P(a preferred to b) = sigmoid(R(a) − R(b))`, with `sigmoid(x)=1/(1+exp(−x))`. This is an **analyst mathematical restatement [C]** of the specified relationship, not a numbered paper equation. The authors themselves give sigmoid(1) ≈73%. R is an Elo-like learned reward for question, answer, and references. Equal scores imply 50% predicted preference. This concerns preference probabilities, not factual correctness probabilities. No cross-entropy formula or full PPO objective is printed; those losses must not be reconstructed as though supplied verbatim.

### E3 — Expected selected-answer validation score, p. 28

`Rpred_n(q) := E_{A1,...,An ~ A(q)}[Rval(argmax_{a in {A1,...,An}} Rtrain(a | q) | q)]`.

Here q is a question; Q is the question distribution; A(q) is the model's distribution of answers for q; each sampled answer includes references; Rtrain is the original selection reward; Rval is a separate validation reward; n is the number of candidates. Argmax selects the candidate with greatest training score, then Rval scores that selected candidate. The expectation averages over sampled candidate sets. The target is the validation score of the answer the selection procedure would choose, not the maximum validation score among all candidates. This separation attempts to detect optimization that exploits the training scorer.

### E4 — Across-question expectation, p. 28

`E_{Q ~ Q}[Rpred_n(Q)]` averages E3 over the question distribution. The page uses Q both as the distribution symbol and within the random-question expression; this report distinguishes their roles in words. Output is an expected Elo-like score. The authors estimate it by sampling questions and taking an empirical average. Exact question sample counts are unspecified.

### E5 — All-subsets estimator, p. 28

Given N sampled answers with N≥n, average the validation score of the training-score winner over every size-n subset:

`(1 / binom(N,n)) Σ_{1≤i1<...<in≤N} Rval(argmax_{a in {Ai1,...,Ain}} Rtrain(a | q) | q)`.

The binomial coefficient counts subsets. Strictly increasing indices ensure each subset appears once. The authors state this estimator is unbiased by linearity of expectation. It reuses an N-answer pool across different n values rather than repeatedly drawing entirely new n-answer groups. Its direct expression contains many subsets and motivates a more efficient equivalent computation.

### E6 — Sorted weighted estimator, p. 28

Sort answers as S1 through SN in nondecreasing Rtrain score. The all-subsets expression equals:

`Σ_{i=n}^N [binom(i−1,n−1) / binom(N,n)] Rval(Si | q)`.

**Analyst explanation [C]:** a size-n subset whose highest-ranked member is Si must contain Si and choose n−1 members from the preceding i−1 answers; this gives binom(i−1,n−1) subsets. Dividing by binom(N,n) gives the weight. The paper supplies the equality and unbiasedness claim; this counting explanation makes its mechanism explicit. Reward-score ties and tie-breaking are not specified. Across questions, sample N≥nmax and compute averages for n=1,...,nmax. Agreement with human preference is shown for n≤64; the authors expect excessive n eventually to overoptimize even the validation RM. No theorem extending this empirical agreement is supplied.

## 14. Interpretation and discussion

The supported central finding is that a model can learn useful search-and-answer behavior and that learned preference-based selection substantially improves evaluated output quality. O1 is addressed by the working browser/task design; O2 by training and selection comparisons; O3 by ELI5 and TruthfulQA; O4 by Figures 4–8 and Appendix I; O5 by Appendix H. No formal hypothesis-testing framework is presented. [A]

The claim of human-level browser use refers to a restricted task and evaluation procedure. It is not a claim of equal general reasoning, equal security, or equal knowledge. Preference against demonstrators measures overall usefulness; near-equal factual-accuracy preference and lower coherence preference give a more nuanced account than the conclusion's shorthand outperforms humans on ELI5. [A/B; pp. 2, 6, 12]

Important consistency checks preserve rather than erase distinctions. Approximate collection totals agree with exact Table 4 counts. The released 19,578 comparisons are fewer than the 21,548 collected: Appendix K restricts release to those marked suitable for RM, but does not enumerate all exclusion causes or identities. The RL description's 15 additional answer-only phases agrees with Table 7's 16 total phases. Epoch upper bounds in Table 6 differ legitimately from early stopping in Table 8. [A]

The broad §6.3 observation that question stance seems influential is narrowed by Appendix H: factual accuracy shows suggestive framing effects, but explicit answer stance has no clear framing effect. These are different outcomes and should not be reconciled into a single stronger claim. Similarly, §6.1 explicitly says reduced non-imitative falsehoods was not tested directly. Good ELI5 factuality ratings and cited prior research motivate a hypothesis, not a measured WebGPT-versus-GPT-3 hallucination reduction percentage. [A; pp. 9–10, 25]

For security analysis, §6.5 is the most direct evidence. It identifies a possible reward-driven incentive to modify external evidence if write capabilities existed, then states that current allowed actions prevent direct editing. **Analyst inference [D]:** browser agents can connect generated decisions to mutable outside resources, making capability restrictions and evidence integrity consequential. This is a conditional architectural explanation, not evidence that this restricted WebGPT was more attackable than standalone GPT-3. The actual TruthfulQA results favor WebGPT's truthfulness in the evaluated setting.

## 15. Contributions and novelty

The authors explicitly identify two contributions: a text-based browser environment that supports learning retrieval and synthesis together using imitation and RL; and reference-bearing answers that let labelers evaluate support without independent research. [A; p. 2]

The system contribution is a restricted, model-readable browser with human demonstration tooling. The methodological contribution is integrating demonstrations, pairwise preferences, reward-based training, and inference-time selection for LFQA. The empirical contribution is evaluating multiple model sizes and comparing optimization methods, data scales, compute budgets, and transfer tasks. The dataset contribution is release of 19,578 suitable comparison pairs with question, quotations, answer, tokens, and scores. The mathematical contribution is an efficient estimator for expected validation score after best-of-n selection. These categories organize author-provided material; they do not establish priority against uninspected external literature. [A/D; pp. 2–9, 28, 32]

There is no novel attack algorithm, formal security theorem, or measured defense contribution. The security relevance lies in the environment boundaries and the authors' risk discussion, rather than in an adversarial evaluation protocol.

## 16. Limitations

### Authors' stated limitations

WebGPT remains below human TruthfulQA performance and struggles with out-of-distribution questions. It can quote unreliable sources and make paraphrasing or synthesis errors. Reduced non-imitative falsehoods was not directly tested because subtle hallucinations were difficult to label. Citations can increase apparent authority and overreliance. Models can cherry-pick convincing references, inherit base-model bias, reinforce existing norms, and accept implicit question assumptions. Trustworthiness criteria involve judgment calls unlikely to command universal agreement. [A; pp. 2, 9–11]

Reddit-reference evaluation has limitations in fact checking, criterion clarity, blinding, and answer intent. Helpful-prompt GPT-3 can trade informativeness for abstention. Truncation produced 74 empty answers, about 3% of the relevant answer set. RL can overoptimize the RM; joint RL/selection provides little benefit. BC tuning substantially reduces the apparent RL advantage. Smaller model settings were tuned less, and a reward-model EMA bug affects smaller-model RL. [A; pp. 6–8, 20]

Scaling relies on a proxy validation RM, with noisier parameter trends. Appendix I expects overestimation for sufficiently large n. TriviaQA uses more compute and live web than comparators. Question-stance results are too small for definitive conclusions. Reference-point bias is probed by one culturally dependent question. [A; pp. 8, 24–28]

### Additional evidence-based analyst observations

[D] There is no dedicated malicious-page or malicious-search-result experiment. No security incident rate or attack success rate is reported. Baseline truthfulness differences combine browser access, fine-tuning, preference optimization, selection, prompting, and different scoring methods; they do not isolate browsing alone. Human annotation assesses support and reliability judgments rather than unrestricted independent verification. Half the data comes from five workers, so preference diversity may be narrower than raw worker counts suggest. Survey respondents exclude early dropouts and can contribute repeatedly.

[D] Live-web content can change, while the paper does not provide complete page snapshots, query timestamps, environment versions, seeds, or hardware specifications in the supplied document. The missing linked instruction files limit reconstructing detailed trustworthiness guidance. Plot estimates are insufficient to reconstruct all statistical results. These observations identify limits of the evidence available here; they are not claims that the researchers failed to retain artifacts elsewhere.

## 17. Threats to validity

The following categories are **analyst interpretations [D]**, except where linked to explicit author caveats.

**Internal validity:** method comparisons depend on tuning effort, RM training distribution, and the disclosed EMA bug. Proposed causes of selection's advantage were not separately manipulated. Preference data were collected ad hoc across varied policies. These make a causal claim about any single component stronger than the demonstrated comparison.

**Construct validity:** overall usefulness, supportedness, truthfulness, informativeness, preference prediction, and exact match are distinct constructs. A convincing reference need not be true; an accurate but unhelpful abstention can score truthful. In the framing study, inability to easily verify enough claims counts as inaccuracy. None of these measures is itself a security vulnerability measure.

**External validity:** ELI5 dominates training; TruthfulQA distribution shift reveals failures. One wedding question cannot estimate cultural bias across all prompts. A read-restricted text browser does not represent a write-enabled, authenticated, visual browser agent. Security conclusions therefore require explicit capability matching.

**Statistical conclusion validity:** figures usually show one standard error, but complete sample counts and significance tests are unavailable. Approximate plot readings must not support fine-grained rankings or significance. The authors themselves characterize framing evidence as suggestive.

**Ecological validity:** stripping citations and using minimal instructions approximates ordinary user comparison in one respect, but prohibits following answer links and tolerates historical correctness over a ten-year interval. The detailed demonstrator comparison instead aligns tightly with the researchers' chosen task criteria.

**Reproducibility:** supplied tables make many settings explicit, yet seeds, hardware, versioned web corpus, full instruction artifacts, and complete run histories remain unavailable. Released comparison records aid inspection of final answers and references; they do not necessarily provide all browser trajectories or all collected examples. [A/D; pp. 23, 32]

## 18. Future work and open questions

### A. Explicit author proposals

Train on adversarially selected questions while carefully assessing source trustworthiness; document limitations and study ways to reduce overreliance; improve base models and objectives for bias; consider finding evidence both for and against claims through debate, recursive reward modeling, or iterated amplification; develop practical and epistemically sound factuality criteria through cross-disciplinary work; increase safety evidence as web-enabled capabilities increase and use tripwire tests for exploitative behavior. [A; pp. 9–11]

Other proposals are adapting RL objectives to optimize selection performance, decomposing complex annotation tasks, improving auxiliary supervision, sharing policy/value networks, and expanding framing and identity-bias studies. Appendix H names collection methodology, question stance distribution, web-source balance, and appearance of questions in training/web content as factors for future analysis. [A; pp. 8, 17–18, 20, 25–26]

### B. Additional open questions

[D] Does adding web access increase measured attacker success when training, model size, prompts, evaluator, and permissions are controlled? Can misleading sources change later search choices, collected references, or final answers? What happens when read-only browsing expands to forms or authenticated operations? How reliably can evaluators distinguish faithful quotation from selective quotation? Which component produces the TruthfulQA gain: browsing, training, source preference, or selection? These questions follow from the supplied architecture but were not answered by the paper.

## 19. Terminology and notation glossary

| Term | Meaning in this work |
|---|---|
| GPT-3 | Pretrained language-model family fine-tuned for browser use |
| LLM | Large language model; used in the user's framing, not a distinct tested security category |
| NLP / LFQA | Natural language processing / long-form question-answering |
| ELI5 | Explain Like I'm Five Reddit question dataset |
| BC | Behavior cloning, supervised imitation of demonstrations |
| RM | Reward modeling, learning preference scores from comparisons |
| RL / PPO | Reinforcement learning / proximal policy optimization |
| Reference / quote | Collected page extract with page title and domain |
| Best-of-n / bo4, bo16, bo64 | Generate n candidates and select the highest RM score |
| Policy | Model behavior that chooses browser commands and answers |
| KL | Kullback–Leibler divergence used to penalize deviation from BC |
| Nat | Unit reported for episode KL |
| EMA | Exponential moving average of model weights |
| GAE | Generalized advantage estimation, named RL estimation procedure |
| Epoch | Pass through training data; upper bounds differ from stopping points |
| Temperature | Sampling control; main evaluations use 0.8 |
| Elo-like score | Reward scale whose differences are preference logits |
| Sigmoid | Function converting a score difference into a probability |
| Standard error | Uncertainty measure used in plot bars/bands; not automatically a confidence interval |
| Hallucination | Plausible-looking false statement, in the authors' terminology |
| Imitative falsehood | Falsehood encouraged by the training objective |
| Non-imitative falsehood | Falsehood from failure to achieve the objective |
| Automation bias | Overreliance on automated output discussed by the authors |
| Distribution shift | Evaluation questions differ from primary training questions |
| Reference-point bias | Assuming a cultural perspective that the user did not specify |
| Pareto frontier | Estimated favorable tradeoff between compute and score |
| DPR / REALM / RAG | Dense passage retrieval / Retrieval Augmented Language Modeling / Retrieval Augmented Generation |
| ARC | AI2 Reasoning Challenge |
| Exact match | TriviaQA metric requiring the extracted answer to match the evaluation target |
| q, Q, A(q) | Question, question distribution, answer distribution for that question |
| Rtrain, Rval | Selection reward model and separately trained validation reward model |
| n, N, nmax | Selection candidates, reusable sampled pool size, largest evaluated candidate count |
| argmax | Select the argument yielding the greatest specified score |
| binom(N,n) | Number of size-n subsets from N items |

The paper names PPO and GAE without providing their complete equations. This glossary does not introduce those missing mathematical definitions from external sources.

## 20. Key numerical results

| Quantity / result | Value | Unit | Condition / context | Status | Source |
|---|---:|---|---|---|---|
| Model sizes | 760M; 13B; 175B | parameters | GPT-3 fine-tuning | Author-reported | p. 4 |
| Main candidate counts | 4; 16; 64 | answers | Corresponding model sizes | Author-reported | p. 5 |
| Demonstrations | 6,209 | records | All listed datasets | Author-reported | p. 16, T4 |
| Comparisons collected | 21,548 | pairs | All listed datasets | Author-reported | p. 16, T4 |
| Comparisons released | 19,578 | pairs | Marked suitable for RM | Author-reported | p. 32 |
| RM training/evaluation | about 16,000 / 5,500 | comparisons | Final RM split | Author-reported | p. 5 |
| BC validation | about 4 | % demonstrations | Held out | Author-reported | p. 5 |
| Main evaluation temperature | 0.8 | sampling setting | All main WebGPT models | Author-reported | p. 5 |
| Main browsing cap | 100 | actions | Evaluation | Author-reported | p. 5 |
| RL browsing cap | 20–100 inclusive | actions | Uniformly sampled | Author-reported | p. 5 |
| Overall preference vs humans | 56 | % preference | 175B best-of-64; ties half | Author-reported | p. 5 |
| Overall preference vs Reddit | 69 | % preference | Same model; citations stripped | Author-reported | p. 5 |
| Truthful | 75 | % answers | 175B best-of-64 TruthfulQA | Author-reported | p. 2 |
| Truthful and informative | 54 | % answers | Same configuration | Author-reported | p. 2 |
| TruthfulQA answer cap | 50 | tokens | Then partial sentences removed | Author-reported | p. 7 |
| Truncation empty answers | 74; about 3 | answers; % | Truthful but uninformative | Author-reported | p. 7, footnote 3 |
| Best-of-64 vs BC | 68 | % preference | 175B BC selection | Author-reported | p. 7 |
| RL vs BC | 58 | % preference | 175B without selection | Author-reported | p. 7 |
| Preference-statistic difference | 10 | percentage points | 68−58; separate comparisons | Analyst-derived | p. 7 |
| Demonstration doubling gain | about 0.13 | RM-score units | Scaling trend | Author-reported | p. 8 |
| Policy-parameter doubling gain | roughly 0.09 | RM-score units | Noisier scaling trend | Author-reported | p. 8 |
| Comparison doubling gain | about 1.8 | % as stated | RM accuracy; unit convention ambiguous | Author-reported | p. 8 |
| RM-parameter doubling gain | roughly 0.4 | % as stated | RM accuracy | Author-reported | p. 8 |
| Researcher/worker agreement | 74 | % agreement | Neutral/nonneutral counted half | Author-reported | p. 17 |
| Worker/worker agreement | 73 | % agreement | Same convention | Author-reported | p. 17 |
| Demonstration/comparison time | about 15 / 10 | minutes | Average per task | Author-reported | p. 17 |
| Largest workers' contribution | about 50 | % data | Top five contractors | Author-reported | p. 17 |
| Survey item ratings | 41 | ratings | Three surveys; repeats included | Author-reported | p. 19 |
| TriviaQA total | 69.5 vs 58.7 | % exact match | Combined system vs ablation | Author-reported | p. 24, T9 |
| TriviaQA total gain | 10.8 | percentage points | 69.5−58.7 | Analyst-derived | p. 24, T9 |
| TriviaQA no-overlap gain | 13.4 | percentage points | 52.4−39.0 | Analyst-derived | p. 24, T9 |
| Extractor fine-tuning | 256 | questions | Additional to 143 demonstrations | Author-reported | p. 24 |
| Framing materials | 60 | questions | 20 topics × three stances | Author-reported | p. 25 |
| Wedding samples | 64 | answers | 175B BC; one question | Author-reported | p. 25 |
| American word mentions | 20 | answers | America or American | Author-reported | p. 25 |
| Other named cultural focus | 4 | answers | Vietnamese 1; Indian 1; Croatian 2 | Author-reported | p. 25 |
| No standard wedding | 8 | answers | Seven still contain Western detail | Author-reported | p. 25 |
| Prediction validation range | n≤64 | candidate count | Figure 5 setting | Author-reported | p. 28 |
| Human TruthfulQA reference | about 94 / 87 | % | Truthful / truthful and informative | Approximate visual estimate | p. 7, F3 |

Configuration values from Tables 5–8 are transcribed in §11 rather than duplicated in this compact result table. No attack-success statistic is supplied.

## 21. Claim–evidence map

| Claim | Evidence | Object / experiment | Source | Qualification / evidence strength |
|---|---|---|---|---|
| A model can operate the text browser | Defined observation and commands, trained demonstrations | F1, T1, X1–X3 | pp. 2–5 | HIGH for system design; not general browser competence |
| Reference collection aids evaluation | Support-based annotation procedure and stated rationale | F9, Appendix C | pp. 11, 17–18 | HIGH for procedure; truth still depends on source judgment |
| Best system is useful relative to demonstrators | 56% preference | F2a, X1 | p. 5 | HIGH; ties half and overall usefulness |
| Best system beats Reddit reference preference | 69% preference | F2b, X2 | p. 5 | HIGH; different instructions and incomplete blinding |
| WebGPT improves measured TruthfulQA outcomes | 75% truthful, 54% both; all WebGPT outperform plotted GPT-3 | F3, X3 | pp. 2, 6–7 | HIGH for reported results; evaluator/truncation caveats |
| Selection improves BC substantially | 68% preference over BC | F5, X4 | p. 7 | HIGH; 175B best-of-64 condition |
| RL adds little after selection | F4 and explicit discussion | F4, X4 | p. 8 | HIGH for reported interpretation; causes not isolated |
| More data/parameters improve proxy scores | Scaling curves and slopes | F6–F8, X5–X7 | pp. 8–9 | MEDIUM for broad extrapolation; proxy and noise |
| Transfer improves short-answer exact match | 69.5% vs 58.7% | T9, X8 | p. 24 | HIGH; two-stage pipeline, differing web/compute access |
| Framing can reduce accuracy | Small 60-question study | F11, X9 | pp. 25–26 | MEDIUM; suggestive, no definitive conclusion |
| Explicit stance mirroring is not established | No clear framing effect on affirmation/refutation | F12, X9 | p. 25 | HIGH for negative finding within this study |
| References can be selectively convincing | Explicit incentive discussion | §6.4 | p. 11 | HIGH as author concern; no attack rate |
| Current external-action restrictions limit side effects | Only Bing queries and following existing links | §6.5, T1 | pp. 3, 11 | HIGH for stated boundaries; low-risk assessment not a formal proof |
| Broader permissions could expose new harms | Conditional Wikipedia-editing example | §6.5 | p. 11 | HIGH as hypothetical author example |
| Security relevance is architectural, not comparative proof | External inputs/actions plus absence of attack study | §2, §6.5 | pp. 3, 11 | MEDIUM analyst inference; no quantified vulnerability comparison |

## 22. Very simple explanation — Explain Like I'm 15

Imagine teaching a student to answer questions with a search engine. First you show examples of good searching and writing. Then people compare pairs of answers, and another program learns which answers they prefer. WebGPT does this with GPT-3. It searches, opens pages, saves useful quotations, and writes an answer using those quotations.

The strongest version tries 64 candidates and chooses the one its scoring program likes best. People preferred its answers over the researchers' human demonstrators 56% of the time in the specified test. That does not mean every answer was correct: usefulness, clarity, factual support, and truthfulness are different things. On a benchmark designed around misconceptions, it still sometimes believed bad sources or confidently said something false.

References help because you can inspect where an answer came from. But a reference can be misleading, selected unfairly, or simply wrong. A system that looks well researched may therefore be easier to overtrust. The paper shows both the benefit of browsing and the danger of treating citations as proof.

For security, the important extra ingredient is that a browsing model reads outside material and can act through tools. This version's tools were restricted to searching and following existing links. The authors imagined that a version able to edit pages might manipulate evidence to make its own answer look better. That is a warning about possible permissions and incentives, not a demonstrated attack. This paper does not prove that web agents are more vulnerable than standalone models; it helps explain which additional pathways a security study should test.

## Completeness Audit

The inventory comprises the abstract; §§1–10 and all substantive subsections; Appendices A–K; Figures 1–12, including distinct panels; Tables 1–13; retrieval Eq. (1); the reward/preference relationship; Appendix I's expectation and estimator expressions; twelve experimental/analysis entries; two explicit contributions; and the author limitations represented above. No formal theorem, numbered algorithm, or formal research-question list was supplied.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes, text and image | Yes | Fully represented | Main method and headline outcomes |
| §1 Introduction | Yes, text and images | Yes | Fully represented | Framing and contributions |
| §2 Environment design | Yes, text and image | Yes | Fully represented | State, commands, memory, termination |
| §3.1 Data collection | Yes, text and images | Yes | Fully represented | Demonstrations and preferences |
| §3.2 Training | Yes, text and images | Yes | Fully represented | Four methods and split conditions |
| §4.1 ELI5 | Yes, text and images | Yes | Fully represented | Both comparisons and caveats |
| §4.2 TruthfulQA | Yes, text and images | Yes | Fully represented | Evaluators, truncation, results |
| §4.3 TriviaQA | Yes, text and image | Yes | Fully represented | Appendix G evaluation incorporated |
| §5.1 Method comparisons | Yes, text and images | Yes | Fully represented | BC, RL, selection, proposed explanations |
| §5.2 Scaling | Yes, text and images | Yes | Fully represented | Proxy, data, parameters, computation |
| §6.1 Truthfulness | Yes, text and image | Yes | Fully represented | Falsehood types and untested hypothesis |
| §6.2 Perceived truthfulness | Yes, text and image | Yes | Fully represented | Authority and overreliance |
| §6.3 Bias | Yes, text and image | Yes | Fully represented | Inheritance, norms, implicit assumptions |
| §6.4 Reference evaluation | Yes, text only | Yes | Fully represented | Benefits, cherry-picking, judgment calls |
| §6.5 Live-web risks | Yes, text only | Yes | Fully represented | Conditional editing, present restrictions |
| §7 Related work | Yes, text; p. 12 image | Yes | Represented in compressed form | Categories and positioning; no external verification |
| §8 Conclusion | Yes, text and image | Yes | Fully represented | Scope-qualified conclusions |
| §9 Author contributions | Yes, text and image | Yes | Represented in compressed form | Roles acknowledged; full role list secondary |
| §10 Acknowledgments | Yes, text; p. 12 image | Partly | Inspected but deliberately omitted as non-substantive | Names do not alter scientific findings |
| Bibliography | Yes, text only | Partly | Represented in compressed form | Relevant categories; no citation validation |
| Objectives O1–O5 | Yes | Yes | Fully represented | Analytical organization, not formal author RQs |
| Explicit explanatory hypotheses | Yes | Yes | Fully represented | Reliability, shift, falsehood, transfer explanations |
| X1–X3 | Yes | Yes | Fully represented | Separate evaluation protocols |
| X4–X7 | Yes | Yes | Fully represented | Method and scaling experiments |
| X8–X10 | Yes | Yes | Fully represented | Transfer, framing, reference-point bias |
| X11–X12 | Yes | Yes | Fully represented | Survey and prediction validation |
| F1a–b | Yes, visual | Yes | Fully represented | Human interface versus model observation |
| F2a–b | Yes, visual | Yes | Fully represented | Exact headlines; other bars approximate |
| F3 | Yes, visual | Yes | Fully represented | Truthful/informative distinction |
| F4–F5 | Yes, visual | Yes | Fully represented | RL and selection; uncertainty markings |
| F6–F8 | Yes, visual | Yes | Fully represented | Scaling axes and estimated frontier |
| F9 | Yes, visual | Yes | Fully represented | Annotation interface |
| F10 | Yes, visual | Yes | Represented in compressed form | Pie trends, no invented exact proportions |
| F11 | Yes, visual | Yes | Fully represented | Small framing study |
| F12 | Yes, visual | Yes | Uncertain | Per-model mapping qualified; overall conclusion retained |
| T1 | Yes, visual and text | Yes | Fully represented | All command forms |
| T2–T3 | Yes, visual and text | Yes | Represented in compressed form | Example meanings and selection status preserved |
| T4–T8 | Yes, visual and text | Yes | Fully represented | Counts and all hyperparameter rows |
| T9 | Yes, visual and text | Yes | Fully represented | Every reported result and missing split notation |
| T10 | Yes, visual and text | Yes | Represented in compressed form | All topics and design; 60 exact questions not repeated |
| T11–T13 | Yes, visual and text | Yes | Represented in compressed form | Evidence/example contrasts; full passages not reproduced |
| E1 | Yes, visual and text | Yes | Fully represented | Related-work retrieval, not Bing algorithm |
| E2 reward relationship | Yes, text | Yes | Fully represented | Mathematical restatement explicitly derived |
| E3–E6 Appendix I | Yes, visual and text | Yes | Fully represented | Symbols, constraints, use, tie caveat |
| Formal theorem/pseudocode | None found | Not applicable | Missing from supplied material | No claim of an unreviewed supplied object |
| Contributions | Yes | Yes | Fully represented | Two explicit plus categorized technical outputs |
| Author-stated limitations | Yes | Yes | Fully represented | Kept separate from analyst observations |
| Appendix A | Yes, visual and text | Yes | Fully represented | Processing and filtering |
| Appendix B | Yes, visual and text | Yes | Represented in compressed form | Exact counts; regex list compressed |
| Appendix C.1–C.2 | Yes, visual and text | Yes | Fully represented | Interface differences and annotation changes |
| Appendix D | Yes, visual and text | Yes | Represented in compressed form | Survey design, counts, trends |
| Appendix E | Yes, text; pp. 20/22 images | Yes | Fully represented | p. 21 text-only; settings and bug retained |
| Appendix F | Yes, text only | Yes | Represented in compressed form | Search-engine checking, URL rule, historical tolerance |
| Appendix G | Yes, visual and text | Yes | Fully represented | Extraction pipeline and comparison caveats |
| Appendix H.1–H.2 | Yes, visual and text | Yes | Fully represented | Separate accuracy, stance, and cultural analyses |
| Appendix I | Yes, visual and text | Yes | Fully represented | All central mathematical expressions |
| Appendix J | Yes, visual and text | Yes | Represented in compressed form | Reference passages and answers summarized |
| Appendix K | Yes, text only | Yes | Fully represented | Release count, fields, scores, tokenization |
| Linked instruction documents | No | No | Inaccessible | Full demonstration/comparison documents not supplied |
| Answer viewer and downloadable dataset | No | No | Inaccessible | Descriptions read; external contents not reviewed |

### Missing or inaccessible material

No page is missing from the supplied 1–32 text sequence. Direct images are absent for pp. 11, 13, 14, 21, 23, and 32. The linked demonstration and detailed comparison instruction artifacts, answer viewer, and downloadable comparisons file are absent as inspectable contents. No supplementary video was supplied. Exact hardware, versions, seeds, some sample sizes, browsing reference-length limit, and full run histories are not specified in the supplied work.

### Uncertain interpretations

Small-chart values are approximate unless separately reported in prose or tables. Figure 12's per-model bar mapping is not explicitly labeled within that panel. The scaling prose's 1.8% and 0.4% accuracy gains do not explicitly settle percentage-point versus relative-percent interpretation. Appendix I leaves reward-score tie handling unspecified. The source/example chronology wording in Table 12 is internally questionable and remains unrepaired. The collected/released comparison difference is explained at the suitability-category level, without a detailed exclusion ledger.

### Deliberately compressed material

Repeated explanations of the four training methods are consolidated. Full quoted examples, all 60 framing-question wordings, the full regex word list, survey free-response questions, bibliography entries, acknowledgments, and individual author-role assignments are compressed. Their scientific functions, numerical conditions, provenance, and relevant caveats are retained. Appendix K's records contain paired Question, Quotes, Answer, Tokens, and Score fields; tokens use GPT-2 tokenization, question/quote prefixes can be truncated, pair scores lie from −1 to 1 and sum to zero, zero is a soft half label, and nonzero scores train on sign only. These dataset-format details are accounted for without reproducing nonexistent downloaded records.

### Potential omissions

Every substantive identified section, figure, table, equation family, experiment, contribution, and available appendix is represented, with compression and uncertainty disclosed above. This does not mean every sentence or example is reproduced. Inaccessible linked artifacts remain unreviewed. No direct security comparison, measured attack, or universal vulnerability conclusion is recoverable from this inventory, and none has been claimed.
