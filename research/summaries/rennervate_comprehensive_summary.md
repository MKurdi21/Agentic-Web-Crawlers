## Stage 0 — Document Accessibility Report

The supplied work is available as extracted text for physical PDF pages 1–18. Images are supplied for pages 1–10, 16, and 17. All source locators below use physical PDF page numbers, which agree with the visible printed numbering where present. The main paper, references, and Appendices A–D are textually accessible. The last supplied page contains Appendices C and D; there is no visible continuation marker, although this does not independently establish that every possible associated artifact has been supplied.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied text for pages 1–18 |
| Visually inspected pages | 1–10, 16, 17 |
| Text-only pages | 11–15, 18 |
| Apparently missing main-document pages | None within the supplied 1–18 sequence |
| Figures available visually | Figures 1–8, including the distinct panels |
| Tables available visually | Tables I–IV, XII, XIII |
| Tables available through text only | Tables V–XI |
| Equations | Equations (1)–(6) visible in supplied images and extracted text; bars, subscripts, and some diagram dimensions require care |
| Appendices | A: Results; B: baseline prompts; C: FIPI example; D: DeepSeek judgment prompt |
| Supplementary artifacts | No separate supplement, code, dataset files, trained weights, or execution records supplied |
| Referenced missing material | FIPI is described as intended for public release; its underlying records are not supplied |
| OCR | Not necessary for the provided extracted text; no independent OCR performed |
| Other limitations | The supplied hash is an identifier provided by the user, not independently recomputed; tables on text-only pages were not visually verified |

This analysis uses only these supplied materials. Embedded attack strings and baseline prompts are treated as evidence, never as instructions. No browsing, code execution, or tools were used. Statements are distinguished as [A] author-reported, [B] directly observable, [C] analyst-derived, and [D] analyst interpretation. No external information [E] is introduced. Confidence labels HIGH, MEDIUM, LOW, and UNKNOWN concern support in the supplied document, rather than independent replication.

### Inventory established before synthesis

The document is a mixed cybersecurity, machine-learning, algorithm, and dataset paper with an empirical systems evaluation. Its inventory contains an abstract; Sections I–VIII; substantive subsections II-A/B, III-A/B, IV-A/B/C, V-A/B/C, and VI-A/B/C/D/E/F; acknowledgments; 99 numbered references; Appendices A–D; Figures 1–8; Tables I–XIII; Algorithm 1; and Equations (1)–(6). There are no formal theorems, lemmas, explicitly numbered research questions, or formal statistical hypotheses. Major experimental families are overall detection, overall sanitization, utility, unseen cross-task datasets, unseen gradient attacks, adaptive black-box attacks, adaptive white-box attacks, component ablations, hyperparameter sensitivity, and an instruction-only injection diagnostic. The inventory is used again in the final coverage audit.

## 1. Plain-language orientation

[A] The paper introduces RENNERVATE, a defense against indirect prompt injection in applications that combine a large language model with retrieved external material. A legitimate user may ask an assistant to summarize a webpage. An attacker can place instructions inside that page, attempting to make the assistant follow the attacker's request instead. The suspicious text arrives as material to read, rather than as an authorized user command. This distinction is central to the paper (pp. 1–4).

[A] RENNERVATE examines internal attention features: numerical signals describing how generated response tokens attend to input tokens. A small trained detector classifies individual external-data tokens as injected or clean. A smoothing and aggregation stage decides whether the entire input is injected. A sanitizer can delete the detected tokens and reconstruct the external text. The intended benefit is to remove the attack while retaining useful material, instead of merely rejecting the entire task (pp. 4–6).

[A] On the balanced FIPI detection test set, reported accuracy ranges from 97.88% to 99.58% across five target models. On 1,000 selected injected examples, total attack success after sanitization is 0.00%–0.20%, compared with 60.80%–85.90% without defense. These results are conditional on the paper's models, generated attacks, dataset, and evaluation procedures; they are not guarantees for every web agent (pp. 8–10, Tables I–III).

[A] The most consequential qualification is that successful attack suppression does not always preserve the original task. In unseen cross-task settings, some utility win rates fall below 10%, and residual attack-related content can remain after sanitization. RENNERVATE also requires internal attention access, which ordinary API clients may lack (pp. 10, 13).

[D] Relevance to the user's research question: this paper supports an architectural explanation for why web-connected agents acquire additional vulnerabilities. They import attacker-influenced material into the model's prompt and may act on the resulting response. It does not directly measure whether agents are more vulnerable than an otherwise matched standalone LLM. The central contribution is a defense and its evaluation, not a controlled agent-versus-standalone comparison.

## 2. Document roadmap

| Original component | Content and role |
|---|---|
| Abstract and I. Introduction, pp. 1–2 | Introduce indirect prompt injection, motivate token-level sanitization, and state contributions |
| II. Preliminaries, pp. 2–3 | Explain model generation, attention, architectural categories, agent prompts, and direct versus indirect injection |
| III. Related Work, pp. 3–4 | Separate detection from prevention; position classifiers, auxiliary models, prompt changes, and model modification |
| IV. System Model, p. 4 | Define attacker and defender assumptions and formalize token detection and removal |
| V. Design Details, pp. 4–6 | Describe the detector, identifier, sanitizer, Algorithm 1, and attentive pooling |
| VI-A. Setup, pp. 6–8 | Report implementation, models, baselines, FIPI construction, and metrics |
| VI-B. Overall Effectiveness, pp. 8–9 | Compare detection and sanitization and introduce utility measurements |
| VI-C. Transferability, pp. 8–11 | Test unseen cross-task data and unseen gradient-based attacks |
| VI-D. Adaptive Adversary, pp. 11–12 | Evaluate iterative black-box and defense-aware white-box attacks |
| VI-E/F. Ablations and Hyperparameters, pp. 12–13 | Probe components and sensitivity to filter size, response length, and residual depth |
| VII. Discussion & Limitations, p. 13 | Discuss deployment access, alternatives, and incomplete content removal |
| VIII. Conclusion & Future Work, p. 13 | Summarize the framework and propose recovery and multimodal research |
| References, pp. 14–16 | Provide bibliographic context; not independently verified here |
| Appendix A, pp. 16–17 | Supply additional plots, failure examples, utility results, and model-size comparison |
| Appendix B, pp. 17–18 | Supply prompts for model-based baselines |
| Appendix C, p. 18 | Show one labeled FIPI example |
| Appendix D, p. 18 | Supply the DeepSeek attack-following judgment prompt |

## 3. Background and context

[A] A large language model, or LLM, receives a prompt and generates a sequence of response tokens. A token is a unit of text represented numerically; it need not equal a whole word. Autoregressive generation means producing each response token using the input and previously generated response tokens. The paper's simplified equation chooses the most probable next token (p. 2).

[A] Attention assigns different levels of focus to input positions during generation. Multiple attention heads and layers provide many such numerical signals. RENNERVATE uses those signals as features for a separate detector. The authors argue that attention can reflect how the target model processes instructions, including instructions hidden in external data. This is the authors' methodological premise, not a proof that attention always identifies malicious intent (pp. 2, 5).

[A] A typical agent receives a legitimate instruction s, retrieves external data X, and queries a backend model G with the combined prompt p = s ⊕ X. The symbol ⊕ denotes concatenation. The application can return G(p), or call other application programming interfaces, APIs, to act on the user's behalf. The supplied experimental outcomes principally concern responses and task following, rather than a deployed browser's full action sequence (p. 3).

[A] Direct prompt injection places the adversarial instruction in the user instruction. Indirect prompt injection, IPI, places it in retrieved external data. The paper focuses on IPI. A white-box attacker can access internal information such as gradients; a black-box attacker relies on observable responses and prompt construction (p. 3).

[A] Detection asks whether an attack is present. Prevention tries to stop the attack from succeeding. Sanitization is the paper's particular prevention mechanism: remove detected injected tokens while retaining the remaining data. These outcomes must be kept separate. An injection can be present but fail to influence the model, and a sanitizer can stop attack execution while still harming the legitimate task (pp. 3–6, 10, 16).

## 4. Research problem and gap

**Existing problem [A].** External resources can contain adversarial instructions that redirect an LLM-integrated application. The authors discuss goal hijacking, sensitive-information leakage, and malicious redirection as potential consequences. The phishing-style example in Figure 1 is illustrative; it is not a measured exfiltration experiment (p. 1).

**Shortcomings attributed to prior methods [A].** The authors argue that classifiers can overfit to familiar patterns, while auxiliary-LLM detectors incur expense and can themselves be attacked. Detection alone does not recover usable clean data and may prevent the application from completing its task. Prompt changes leave the adversarial instructions present. Fine-tuning approaches require modification of model training and may be inconvenient to deploy (pp. 1–4).

**Research gap [A].** The desired defense should identify semantically unobtrusive instructions, localize them precisely, remove them without damaging benign material, and generalize to unfamiliar attacks. A harmless-looking sentence can be malicious because it is an unauthorized instruction in context; wording alone does not settle its role (p. 2).

**Motivation [A].** Internal attention features may indicate which tokens are functioning as instructions for the target model. Fine-grained token predictions could therefore support both detection and recovery of useful text (pp. 2, 5).

**Scope [A/B].** The implemented defense handles textual IPI in five accessible LLMs. Evaluation covers synthetic and benchmark-derived NLP tasks, selected gradient-based attacks, and bounded adaptive attacks. Multimodal defense is proposed as future work. The document does not report a controlled web-agent-versus-standalone-LLM vulnerability ratio (pp. 6–13).

## 5. Research questions / objectives / hypotheses

The paper supplies objectives and evaluation aims, not formal numbered research questions or preregistered hypotheses. The following preserve that distinction.

| ID | Author-stated objective or evaluation aim | Evidence |
|---|---|---|
| O1 | Detect semantically stealthy IPI accurately | Introduction, p. 2 |
| O2 | Neutralize injected instructions while preserving benign functionality | Introduction and defender goal, pp. 2, 4 |
| O3 | Use attention-based token localization and two-step pooling for a compact defense | Contributions and design, pp. 2, 5–6 |
| O4 | Construct fine-grained labeled data for IPI research | FIPI contribution and construction, pp. 2, 7 |
| O5 | Compare against existing detection and prevention methods | VI-B, pp. 8–10 |
| O6 | Test transfer to unseen data and attacks | VI-C, pp. 8–12 |
| O7 | Test robustness against adaptive attackers | VI-D, pp. 11–12 |
| O8 | Determine whether components and hyperparameters affect performance | VI-E/F, pp. 12–13 |

[A] A local explanatory hypothesis does appear in the utility discussion: residual injected-task-specific content may cause degradation. The authors investigate it by removing that content from the injections and repeating the utility comparison. This is an experimental diagnostic, not a formal statistical hypothesis test (p. 10; Table XII, p. 16).

[D] The user's question remains broader than these objectives. The paper supplies a mechanism and defense evidence relevant to agent vulnerability, but does not establish a comparative causal estimate for adding web access.

## 6. Assumptions / threat model

[A] The attacker wants the application to generate a response aligned with the attacker's intention. The attacker fully controls external data sources, can manipulate those data using any attack method, knows defenses may be present, and can observe responses or even obtain gradients of the whole system to adapt attacks. These are strong stated capabilities (IV-A, p. 4).

[A] The defender wants to detect injection and neutralize it without disrupting benign instructions. The defender can observe target-model behavior, especially attention, and has white-box knowledge of the target model. The defender cannot modify the target LLM. It does not know the attack method, exact injected wording, or injection location in advance (IV-B, p. 4).

[D] The trust boundary runs between the legitimate user instruction and retrieved external data. The attack exploits the possibility that content introduced through the data channel influences the model as an instruction. The architecture assumes that observing attention and editing the retrieved text are available defensive operations. It does not specify a complete access-control model for browser tools, account credentials, or irreversible downstream actions.

[A] The broad threat model and the actual experiments should not be conflated. Adaptive black-box attacks have explicit query budgets; adaptive white-box evaluation uses a particular GCG extension on LLaMA2. The text does not demonstrate every possible attacker permitted by the general threat statement (pp. 11–12).

[D] Operational timing is incompletely specified. Attention features are collected during generation, so some model processing occurs before the defense has all its evidence. The paper does not fully document how an application gates tool execution, buffers preliminary output, or reruns generation after sanitization. No claim of protection before every possible agent action can therefore be extracted from the supplied implementation description.

## 7. Methodology

### Architecture and processing

[A] The external text X is tokenized into F = [f1, …, fn]. For each external-data token, the system collects attention from the first m response tokens across l model layers and h attention heads. The resulting per-input-token feature has shape l × h × m. This emphasizes the target model's interaction with a token, rather than merely the token's embedding or wording (pp. 4–5).

[A] The token-level detector first performs response-wise attentive pooling, then head-wise attentive pooling. Each pooling layer learns importance weights and computes weighted means and weighted standard deviations. Means represent important frames; standard deviations represent variation. Fully connected processing, batch normalization, residual blocks, dropout, and a two-class output follow. Cross-entropy is used for detector training. The backend target model is not retrained (pp. 5–6, 13).

[A] The injection identifier applies replicate padding and a mean filter to the token outputs. It chooses a predicted class for each token, then uses the maximum consecutive run of injected predictions to classify the whole external text. The default kernel size is k = 5, and the default threshold is 5. Algorithm 1 uses a strict greater-than comparison, so an intended longest run must exceed five tokens to trigger the input-level label (pp. 5–6).

[A] The sanitizer removes tokens classified as injected and detokenizes the remainder. The San flag controls whether the returned text is sanitized; detection still runs regardless of this flag. Token removal is not explicitly conditioned on the final whole-input label in the displayed algorithm (pp. 5–6).

### Algorithm details and unresolved implementation issues

[B/C] Algorithm 1 updates MaxNum only when a clean token ends an injected run. No final update after the loop is shown. As written, a final injected run reaching the last token may not contribute to MaxNum. This is an analyst observation about the displayed pseudocode, not evidence that the executable implementation has the same issue (p. 5).

[B/C] The symmetric filter sum uses floor((k−1)/2) on both sides and divides by k. For k = 4, the displayed limits include three terms but divide by four; for k = 6, five terms are included. Table XI nevertheless evaluates even k values. An implementation may use a different convention, but the supplied text does not resolve it. This matters for exact reproduction (pp. 5, 12).

[A/D] The text alternates between describing outputs as logits and as classification probabilities. Figure 3 shows negative and positive output values, consistent with unrestricted scores, while the prose calls them probabilities. The precise smoothing location relative to normalization is not fully specified. GreedySearch appears in Algorithm 1 but is not separately defined beyond choosing a predicted label (pp. 5–6).

### Implementation and hyperparameters

| Setting | Reported configuration |
|---|---|
| Framework | PyTorch; version unspecified |
| Training hardware | Two NVIDIA A100 GPUs |
| Training attention length | Trim or zero-pad to m = 32 response tokens |
| Evaluation attention length | Truncate to 32; do not zero-pad in the main evaluation setup |
| Pooling attention channels | 2h for response-wise pooling; 2l for head-wise pooling |
| Residual blocks | N = 2 |
| Hidden dimensionality | 512 |
| Optimizer | Adam |
| Learning rate | 1e-3 |
| Annealing rate | 0.3; schedule details not supplied |
| Batch size | 128 |
| Dropout | p = 0.2 in Figure 3 |
| Mean-filter kernel | k = 5 |
| Input-level threshold | 5, with a strict greater-than test |
| Detector parameters | 0.5–0.8 million |

No random seeds, training epochs, stopping criterion, repeated-run counts, software versions, confidence intervals, or significance tests are reported in the supplied experimental description (pp. 6–13).

### Target models

[A] The models are ChatGLM-6B, Dolly-7B, Falcon-7B, LLaMA2-7B, and LLaMA3-8B. ChatGLM is described as a prefix decoder with 28 layers and 32 heads. Dolly has 32 layers and 32 heads; Falcon has 32 layers and 71 heads; LLaMA2 and LLaMA3 each have 32 layers and 32 heads. The authors describe differences in attention mechanisms and activation functions as architectural diversity. These specifications are reproduced as author-reported, without external verification (pp. 6–7).

### FIPI construction and split

[A] FIPI extends SEP, which supplies 9,160 instruction–clean-data pairs over three broad task categories and 300 subtasks. The authors use GPT-3.5-Turbo to rewrite duplicate instructions and expand the benign foundation to 10,000 distinct pairs. They manually design 100 probe–witness pairs: simple questions with deterministic answers. The witness is a marker for successful execution of the injected task (p. 7).

[A] Attack construction uses Naive, Escape Characters, Context Ignoring, Fake Completion, and three pairwise combinations. Their distribution ratio is 1:1:1:1:2:2:2. The paper commonly presents five attack columns by grouping the combinations under Cb.; seven construction variants are therefore not seven separate reporting columns. Random insertion positions receive character-span labels, converted through each target tokenizer to token labels. Examples whose original data already contain the witness are excluded (p. 7).

[A] The dataset contains 100,000 injected and 10,000 benign instances. A random 1,000-instance manual inspection checks attack deployment and token labels. Testing reserves 5,000 injected and 5,000 benign examples; 100,000 examples remain for training. The authors state that train and test originate from different instruction–data pairs and use distinct adversarial-prompt generation methods. A validation split is not specified (p. 7).

[C] From these reported totals, training contains 95,000 injected and 5,000 benign instances: 100,000−5,000 and 10,000−5,000. This is a 19:1 instance ratio. Token-level class proportions cannot be recovered from that ratio because injection and clean span lengths are not reported.

### Baselines and metrics

[A] Nine detection baselines comprise four classifier/internal-feature methods and five LLM-based variants. They are Prompt-Guard, ProtectAI-v2, Attention Tracker, TaskTracker, GPT-Naive, DS-Naive, Known-Answer, GPT-Resp, and DS-Resp. Attention Tracker and TaskTracker are evaluated only on LLaMA3. Six prevention baselines comprise Sandwich, Instructional, Spotlighting, GPT-Loc, DeepSeek-Loc, and StruQ; StruQ is evaluated only on LLaMA2. These total 15 distinct baselines, not 15 alternatives in each task on every model (pp. 7–10).

[A] Detection metrics are accuracy, false positive rate, and false negative rate. Sanitization metrics are attack success rate, Jaccard word-set similarity, and an AlpacaEval2.0 win rate comparing sanitized-condition outputs with benign-reference outputs. A 50% win rate represents parity under the stated convention. Lower attack success does not automatically imply high task utility (pp. 7–10).

## 8. Experiments / analyses

| ID | Purpose, setup, and outcome |
|---|---|
| X1: Overall detection | Five models; balanced 10,000-instance FIPI test set; nine detection baselines with availability restrictions. RENNERVATE accuracy 97.88%–99.58%; Table I, pp. 8–9. |
| X2: Overall sanitization | 1,000 injected examples selected from the FIPI test set; compare attack success across attack types and defenses. Total defended ASR 0.00%–0.20%; Tables II–III, pp. 8–10. |
| X3: FIPI utility | Compare sanitized text with original clean text through Jaccard similarity, and outputs through win rate. FIPI win rates 43.60%–46.78%; Figures 4–5 and Table IV. |
| X4: Unseen cross-task transfer | Five scenarios, each with 1,000 injected and 1,000 benign examples; five target models. Accuracy includes 80.20% on LLaMA3 MRPC–SST2; Tables V–VI, pp. 9–11. |
| X5: Content-removal diagnostic | Repeat utility evaluation with injections containing instructions only, excluding injected-task-specific content. Table XII improves some settings substantially but does not restore parity universally; pp. 10, 16. |
| X6: Unseen gradient attacks | GCG with 500 iterations and Neural Exec with 250; LLaMA2; 200 sampled benign instances per dataset, converted into injected instances; five dataset columns. Defended GCG ASR 0%–7%; Neural Exec 0%; Table VII, pp. 10–12. |
| X7: Adaptive black-box | Adapt PAIR and TAP from direct to indirect injection; DeepSeek attacker and judge; 100 injected instances per attack on FIPI. PAIR maximum 20 queries; TAP depth 7, width 10, branching factor 4, maximum 70 queries. Defended ASR reaches 19% for PAIR on LLaMA3; Table VIII, pp. 11–12. |
| X8: Adaptive white-box | Extend GCG with detector-evasion cross-entropy against clean labels; LLaMA2; 500 iterations; five datasets. Defended ASR 0%–5%; Table IX, pp. 11–12. |
| X9: Component ablations | Dolly across FIPI and five cross-task scenarios; replace pooling, replace token detector with a Transformer classifier, or remove mean filtering. Mixed individual accuracy changes, but important transfer losses; Table X, pp. 12–13. |
| X10: Hyperparameters | Dolly across six datasets; vary k = 2–6, m = 1,2,4,8,16, and N = 1,2,4,8,16. Gains and losses are dataset-dependent; Table XI, pp. 12–13. |

[A] For unseen cross-task attacks, DeepSeek judges whether a response follows the injected instruction. Manual checking of 200 balanced examples gives 94.50% judge accuracy. The exact positive/negative error breakdown is not supplied. The main FIPI probe–witness mechanism and the unseen-data judge are distinct outcome-labeling procedures (pp. 7, 9–10, 18).

## 9. Results

### Overall detection

| Model | Accuracy % | False positive rate % | False negative rate % |
|---|---:|---:|---:|
| ChatGLM | 99.05 | 1.20 | 0.70 |
| Dolly | 97.88 | 2.42 | 1.82 |
| Falcon | 99.58 | 0.54 | 0.30 |
| LLaMA2 | 99.43 | 0.46 | 0.68 |
| LLaMA3 | 99.37 | 0.84 | 0.42 |

[A/B] These Table I results apply to the balanced FIPI detection test set. On LLaMA3, TaskTracker reaches 95.07%, Attention Tracker 83.23%, and DS-Resp 91.71%. RENNERVATE has the highest reported accuracy in each target-model column.

[C] The LLaMA3 accuracy gaps are 99.37−95.07 = 4.30 percentage points over TaskTracker and 99.37−83.23 = 16.14 points over Attention Tracker. These are absolute percentage-point differences, not relative percentage improvements. The paper describes them with percent signs (p. 8).

### Overall sanitization

| Model | No-defense ASR % | RENNERVATE ASR % | Absolute reduction, percentage points |
|---|---:|---:|---:|
| ChatGLM | 85.90 | 0.10 | 85.80 |
| Dolly | 72.10 | 0.00 | 72.10 |
| Falcon | 84.90 | 0.00 | 84.90 |
| LLaMA2 | 67.10 | 0.20 | 66.90 |
| LLaMA3 | 60.80 | 0.20 | 60.60 |

[A/B] The first two numeric columns are reported in Tables II–III. [C] The final column subtracts defended from undefended ASR. These reductions concern 1,000 selected FIPI injected examples and should not be generalized to the entire web. StruQ reaches 0.30% on LLaMA2; RENNERVATE reaches 0.20%. No significance analysis supports treating this small observed gap as a stable superiority claim.

### Transfer and utility qualifications

[A] Unseen-data detection is strong in many cells but heterogeneous. LLaMA3 reaches only 80.20% accuracy on MRPC–SST2, with 35.30% false negatives. Falcon reaches 82.20% on RTE–Jfleg, with 21.50% false positives and 14.10% false negatives. Sanitization likewise has residual failures: LLaMA3 MRPC–SST2 ASR remains 23.90%, and Falcon Jfleg–RTE remains 14.50% (Tables V–VI, p. 11).

[A/B] FIPI utility win rates are 46.37%, 44.34%, 44.59%, 43.60%, and 46.78% in model order. Unseen cross-task utility can be far worse: Jfleg–RTE gives 5.07%, 16.57%, 1.90%, 5.03%, and 12.33%. LLaMA2 also reaches 9.84% on MRPC–HSOL and 8.05% on SST2–MRPC. Thus the utility evidence is substantially more qualified than a blanket preservation claim (Table IV, p. 10).

[A] Against adaptive black-box attacks, PAIR falls to 0%, 1%, 1%, 0%, and 19%, while TAP falls to 0%, 2%, 2%, 0%, and 9% across the five models. Against adaptive white-box GCG on LLaMA2, defended ASR is 3%, 2%, 2%, 0%, and 5% across FIPI, MRPC, Jfleg, SST2, and RTE (Tables VIII–IX, p. 12).

## 10. Figure-by-figure interpretation

### Figure 1 — Attack and defense toy workflow, p. 1

[B] Panel (a) shows a user asking about the NDSS Symposium, an LLM-integrated application, and an external webpage containing ordinary information plus a red adversarial instruction. The resulting answer advertises the attacker's example website. Panel (b) shows the same task with the injected text crossed out and a relevant answer returned. Arrows link the application and external resource; red attack text, an attacker icon, and a blue defense shield distinguish roles. There are no axes or quantitative values. This illustrates source-to-instruction confusion and the intended restoration of service, rather than measured attack probability.

### Figure 2 — RENNERVATE overview, p. 5

[B] The left depicts an application processing instruction/response tokens, clean external tokens, and injected external tokens. Dashed green connections extract attention features into stacked matrices. Those features feed the token detector, then the injection identifier and sanitizer. Patterned blue tokens represent clean data, red tokens represent injection, and dark tokens represent instruction/response material. The right-side binary sequences illustrate token labels. The figure supports the modular architecture, but does not fully specify a second application call after text sanitization.

### Figure 3 — Pooling and detector internals, p. 6

[B] Panel (a) routes frame-level features through an attention model to obtain weights, then combines weights and original features in attentive statistics pooling. Outputs are a weighted mean and weighted standard deviation. Panel (b) stacks response-wise pooling, head-wise pooling, a fully connected layer with batch normalization, N residual blocks, another fully connected/batch-normalization/dropout stage, and a two-class output. Dropout is labeled p = 0.2. Feature-shape annotations describe dimension reduction, but some superscript-like dimension glyphs are not reliably readable; the prose's l × h × m input shape is clearer. No empirical axes or uncertainty bars appear.

### Figure 4 — Textual similarity across four models, p. 9

[B] Four boxplot panels correspond to ChatGLM, Dolly, Falcon, and LLaMA2. Each x-axis lists FIPI, M-H, J-R, S-M, M-S, and R-J; the y-axis is dimensionless Jaccard similarity on a linear scale, approximately 0.4–1.0. Pastel colors distinguish scenario positions, and boxes and whiskers display distributions. The caption does not define the exact whisker or outlier convention. Most boxes lie relatively high, with FIPI generally around the upper end and wider/lower distributions in some transfer settings. Exact medians, quartiles, sample-level values, and confidence intervals are not labeled. The authors report FIPI scores predominantly 0.9–1.0 and transfer scores largely above 0.8; these prose summaries should not be substituted for exact plot statistics.

### Figure 5 — LLaMA3 textual similarity, p. 16

[B] This is the corresponding six-scenario boxplot for LLaMA3, using the same linear Jaccard scale and abbreviations. The MRPC–SST2 distribution is visibly lower than several others, with a center approximately in the high 0.8s. This is an approximate visual estimate, not a reported exact median. The plot extends Figure 4's model coverage, while Table IV separately shows that text similarity does not ensure preserved output utility.

### Figure 6 — Similarity under unseen gradient attacks, p. 16

[B] Two panels compare GCG and Neural Exec over FIPI, MRPC, Jfleg, SST2, and RTE. The y-axis is Jaccard similarity, with visible linear ticks from approximately 0.4 to 1.0. GCG boxes cluster near 0.9–0.95, consistent with the text. Neural Exec distributions are visibly lower, broadly near the upper 0.7s to around 0.8, and some are wider. Those latter centers are approximate visual estimates. The authors suggest that meaningful lexical content in Neural Exec suffixes complicates precise removal (p. 11). No exact per-dataset medians or statistical tests are provided.

### Figure 7 — Detection failure examples, p. 16

[B] The upper example is a benign role-playing/task-adaptation passage marked Injected, illustrating a false positive. Gray highlighting identifies suspicious segments. The lower example inserts an unrelated question into a bridge-opening report, but the model's response continues reporting the bridge event. It is labeled Clean despite the known injected span, illustrating a false negative. The caption explains that only two words were flagged, insufficient for the run threshold. Importantly, the attack-success field is False. Injection presence and successful behavioral compromise are different labels.

### Figure 8 — Token detection and sanitization example, p. 17

[B] Three stacked blocks show original mixed text, detected spans, and sanitization. Gray text denotes benign material; red text denotes the injection; gray highlighting shows detector selections; strikethrough shows removed text. The injection interrupts a word in a business-analysis passage. A red Injected label marks the input decision. The visual explains how token localization can remove an interleaved instruction while retaining surrounding data. It is a toy example on ChatGLM, not an exact boundary-recovery benchmark.

## 11. Table-by-table interpretation

### Table I — Detection performance, p. 9

[A/B] Rows are nine baselines plus RENNERVATE; grouped columns are target models, each with accuracy, false positive rate, and false negative rate in percent. RENNERVATE has the best accuracy in all five groups. Missing dashes for Attention Tracker and TaskTracker mean those models were not evaluated there, not zero performance. Prompt-Guard shows 64.43% accuracy, 69.94% FPR, and 1.20% FNR across groups; ProtectAI-v2 shows 75.48%, 2.52%, and 46.52%. These contrasting error profiles illustrate why accuracy alone is insufficient. Known-Answer on LLaMA3 has 0.00% FPR but 99.52% FNR. RENNERVATE does not minimize every individual error metric: DS-Resp has 0.76% FPR on LLaMA3 versus RENNERVATE's 0.84%. No uncertainty estimates are shown.

### Table II — Sanitization on ChatGLM, Dolly, Falcon, p. 9

[A/B] Each model has Naive, Esc., Ig., Cp., Cb., and Total ASR columns; lower is better. None means no defense. RENNERVATE totals are 0.10%, 0.00%, and 0.00%. The one nonzero attack-type entry is ChatGLM context ignoring at 0.90%. GPT-Loc totals are 10.3%, 8.20%, and 9.80%; DeepSeek-Loc totals are 22.1%, 19.0%, and 22.4%. Prompt modifications often leave substantial attack success. Totals should not be reconstructed as unweighted averages because attack-type composition differs and the table does not provide all per-column denominators.

### Table III — Sanitization on LLaMA2 and LLaMA3, p. 10

[A/B] It continues the same ASR design. RENNERVATE totals are 0.20% for both models. Residual type-specific success includes LLaMA2 Naive 0.93% and Fake Completion 0.89%, and LLaMA3 Naive 0.93% and combined attacks 0.18%. StruQ appears only for LLaMA2 and totals 0.30%; its LLaMA3 cells are unavailable. The best observed total is RENNERVATE, but no statistical precision accompanies the 0.10-point gap from StruQ.

### Table IV — Utility with injected task content, p. 10

[A/B] Rows are FIPI and five cross-task scenarios; columns are five models. Values are AlpacaEval2.0 win rates in percent; the footnote identifies approximately 50% as no utility loss. FIPI values are moderately below parity. Jfleg–RTE is poor on every model, including 1.90% on Falcon. MRPC–SST2 reaches 53.68% on ChatGLM and 53.03% on Falcon, while other settings remain much lower. A higher-is-better arrow does not change the stated parity reference. No error bars, test counts specific to each win-rate cell, or significance tests appear in this table.

### Table V — Unseen-data detection, p. 11, text-only inspection

[A] Five scenario rows cross five models with accuracy/FPR/FNR columns. Accuracy ranges by scenario are MRPC–HSOL 93.05%–99.75%; Jfleg–RTE 94.20%–99.35%; SST2–MRPC 93.75%–100.0%; MRPC–SST2 80.20%–96.95%; and RTE–Jfleg 82.20%–99.40%. Worst cases differ by error type. LLaMA2 has zero FNR in several scenarios but elevated FPR, including 12.50% on SST2–MRPC. LLaMA3's MRPC–SST2 failure is dominated by 35.30% FNR. These are transfer results without comparator-defense rows.

### Table VI — Unseen-data sanitization, p. 11, text-only inspection

[A] Each model has None and Ours rows across five scenarios. Every defended cell is lower than its corresponding undefended cell, but residual ASR ranges from 0% to 23.90%. Important exceptions to near-total suppression include Dolly RTE–Jfleg 10.90%, Falcon Jfleg–RTE 14.50%, and LLaMA3 MRPC–SST2 23.90%. Baseline susceptibility is highly task-dependent: LLaMA2 MRPC–HSOL starts at only 7.70%, whereas ChatGLM starts at 98.10%. The table therefore does not support assuming uniform attack strength across targets.

### Table VII — Unseen gradient attacks, p. 12, text-only inspection

[A] Columns pair GCG and Neural Exec across FIPI, MRPC, Jfleg, SST2, and RTE; rows give no-defense ASR, defended ASR, and detection accuracy. GCG undefended ASRs are 99.00%, 97.00%, 99.50%, 100.0%, and 94.00%; defended values are 2.50%, 0.50%, 7.00%, 0.00%, and 1.00%. Neural Exec starts at 97.50%, 96.00%, 83.00%, 97.00%, and 89.00% and reaches 0.00% in every column. GCG detection ranges 92.50%–100.0%; Neural Exec detection is 100.0%. The prose's description of undefended attacks as close to 95% compresses a wider observed 83%–100% range. Balanced clean-example denominators for this table's accuracy are not specified as clearly as for Table V.

### Table VIII — Adaptive black-box robustness, p. 12, text-only inspection

[A] PAIR and TAP are each shown without and with defense across five models. All undefended values are 94%–100%; defended values range 0%–19%. LLaMA3 is the hardest reported model under PAIR, with 19% residual ASR, and TAP gives 9% there. ChatGLM and LLaMA2 reach zero under both attacks. One hundred attack instances per method and bounded queries qualify these results.

### Table IX — Adaptive white-box robustness, p. 12, text-only inspection

[A] Five dataset columns compare no defense with RENNERVATE under detection-aware GCG on LLaMA2. No-defense ASR is 98.50%, 98.50%, 99.50%, 98.00%, and 93.00%; defense gives 3.00%, 2.00%, 2.00%, 0.00%, and 5.00%. This demonstrates resistance to the particular clean-label evasion objective and 500-iteration attack, not a formal guarantee against adaptive optimization generally.

### Table X — Component ablations, p. 12, text-only inspection

[A] None means the intact system, not no defense. Replacing two-step pooling with a single response-wise attentive layer improves FIPI from 97.88% to 99.53% and MRPC–SST2 from 93.10% to 94.20%, but reduces Jfleg–RTE to 85.05% and SST2–MRPC to 81.20%. Replacing the token detector with a Transformer gives mixed accuracy changes and removes the intended token-level sanitization output. Removing the mean filter lowers accuracy in all six columns. The intact model is therefore not the best classifier in every cell, while its design supports transfer and token removal.

### Table XI — Hyperparameter sensitivity, p. 12, text-only inspection

[A] Kernel size k ranges 2–6, response count m ranges 1–16, and residual count N ranges 1–16, all on Dolly. With m = 1, accuracy ranges 73.10%–92.00%, so the prose's around-80% description is only approximate. With m = 2 it rises to 89.45%–94.45%. Larger m usually helps but is not uniformly monotonic: RTE–Jfleg falls from 94.45% at m = 2 to 93.45% at m = 4 and 8. Increasing N from 2 to 16 reduces Jfleg–RTE from 96.65% to 86.70% and RTE–Jfleg from 96.20% to 89.20%. Even-k filter implementation remains uncertain because of Algorithm 1's displayed formula.

### Table XII — Instruction-only injection utility, p. 16

[A/B] The five transfer scenarios and five models are repeated after excluding injected-task-specific content. Jfleg–RTE improves to 18.78%, 35.33%, 17.28%, 18.01%, and 22.65%, still below parity. SST2–MRPC improves to 43.71%, 41.00%, 39.57%, 37.43%, and 43.01%. Improvement is not universal: ChatGLM MRPC–HSOL changes from 40.36% to 40.26%, and Falcon MRPC–SST2 changes from 53.03% to 52.17%. The experiment supports a contributing role for injected task content, not a complete explanation of utility loss.

### Table XIII — Architecture and size comparison, p. 17

[A/B] RENNERVATE is AP+RB, attentive pooling plus residual blocks, with 0.5–0.8M parameters. Prompt-Guard and ProtectAI-v2 are listed as 86M and 98M; TaskTracker is a 4K linear model; Attention Tracker is statistical and has dashes. LLM-based baselines have much larger listed parameter counts. These counts are author-reported and not independently checked. Known-Answer is listed as 6B–7B even though LLaMA3-8B is among the evaluated targets, a table–setup inconsistency. The detector count excludes the target or shadow LLM and does not establish end-to-end latency, memory use, or cost.

## 12. Diagram / architecture interpretation

[A/B] Figures 1–3 and 8 form a connected explanation. First, external text is brought into an application following a user request. Second, the model generates response tokens while attention links those response positions to external input positions. Third, each external token obtains its own multi-layer, multi-head feature block. Fourth, learned pooling reduces response and head dimensions while preserving weighted averages and variation. Fifth, the detector returns two-class scores per external token. Sixth, smoothing and run-length aggregation produce a whole-input decision. Seventh, the optional sanitizer removes selected token positions and reconstructs the text (pp. 1, 4–6, 17).

[D] Two outputs should be distinguished: an input-level warning and a modified data sequence. The threshold determines the warning, while per-token predictions determine removals. A short suspicious span can therefore be treated differently by these two output paths. The figures do not supply a detailed control-flow implementation for pausing an autonomous agent, suppressing a preliminary response, handling streaming output, or executing the final clean task.

[B] Decorative components include the attacker icon, shield, celebratory label, and application pictograms. Their function is explanatory role marking; they encode no additional experimental result. They have been accounted for without treating them as substantive evidence.

## 13. Equations and mathematical concepts

### Equation (1), p. 2 — Next-token generation

[A] r_j = argmax_r P(r | F ⊕ r_1:j−1). Here F is the input's token-level representation, r_j is the next response token, and the preceding response sequence is r_1:j−1. The conditional probability is evaluated over candidate tokens r; argmax selects a maximizer. This is a mathematical description of autoregressive next-token selection, not a complete decoding configuration for every experiment. Temperature, sampling settings, and stopping rules are not supplied.

### Equation (2), p. 4 — Aggregate token decisions

[A] M_Θ(F) = S(C_θ(f_1), C_θ(f_2), …, C_θ(f_n)). The token detector C_θ processes each token's associated information; S aggregates the predictions into a decision for the entire external sequence. M_Θ denotes the overall detection system. Later equations clarify that attention, rather than the embedding alone, supplies detector features. Θ and θ identify overall and component parameters, but their exact set relationship is not fully expanded.

### Equation (3), p. 4 — Remove flagged positions

[A] F̄ = F ⊖ F*. F* denotes tokens flagged as injected; ⊖ represents removal; F̄ is the remaining sequence. The sanitized text is X̄ = T^−1(F̄). This expresses sequence editing, not ordinary vector subtraction. The paper describes F as embeddings while also treating it as directly detokenizable. Exact token-ID versus embedding handling is not fully specified and should not be silently repaired.

### Equation (4), p. 5 — Assemble attention features

[A] A_ψ,[:m](f_i) = [A_ψ,1(f_i) ⊕ … ⊕ A_ψ,m(f_i)]. For input token i, concatenate attention features from the first m response tokens. ψ denotes target-model attention parameters; l is the number of layers and h the number of heads. The resulting object has shape l × h × m. The purpose is to use multiple response positions while limiting feature collection and handling response-length variation.

### Equation (5), p. 5 — Compose feature extraction and detection

[A] C_θ(f_i) = C̃_θ∖ψ ◦ A_ψ,[:m](f_i). The composition symbol means first extract attention features, then process them with the trained detector. The parameter notation separates the target-model attention parameters from the final detector's parameters. The target remains fixed. The prose describes a two-class output ω_i with shape 1 × 2. The logits/probabilities terminology is ambiguous, as noted above.

### Equation (6), p. 8 — Jaccard similarity

[A] J(T_1,T_2) = |T_1 ∩ T_2| / |T_1 ∪ T_2|, where the texts are represented as word sets. The numerator counts shared unique words; the denominator counts unique words appearing in either set. Values increase as word-set overlap increases. The supplied definition does not specify handling of an empty union, token normalization, case, punctuation, or repeated words beyond set membership.

[D] Because this metric uses sets, it cannot directly measure word order, repeated-word frequency, grammatical correctness, or successful completion of the user's task. That helps explain why relatively high Jaccard similarity can coexist with poor utility win rates, without proving the precise cause of each failure.

### Algorithm 1's mathematical rule, p. 5

[A] The displayed mean filter averages nearby two-class token scores, then a class-selection step assigns ĝ_i. The intended decision is Injected when the maximum consecutive run of ĝ_i = 1 exceeds Threshold. This is an operational heuristic, not a theorem linking run length to maliciousness. Its end-of-sequence update and even-k indexing issues remain unresolved from the supplied pseudocode.

## 14. Interpretation and discussion

[A] The experiments support the authors' main claim that attention-based token detection can combine accurate input classification with effective sanitization in the tested settings. The most persuasive combined evidence is high balanced-test detection accuracy, very low FIPI post-sanitization ASR, and baseline comparisons under the same reported conditions (Tables I–III).

[D] The evidence is weaker for a universal preservation claim. On unfamiliar cross-task content, attack prevention, text similarity, and actual task utility diverge. Table IV is not a minor footnote: it materially limits the conclusion that retained text remains useful. Table XII narrows one explanation but still leaves substantial utility deficits.

[D] The paper helps answer why web-connected agents have an expanded attack surface: the application brings third-party content into the same model context used to guide its response, and may connect that response to actions. The attacker need not become the legitimate user. This is a source-grounded architectural inference from the workflow on page 3 and the threat model on page 4. The paper does not experimentally isolate retrieval, web navigation, tool privileges, or autonomy as separate causal factors, nor compare their vulnerability to a standalone baseline.

### Cross-reference and consistency findings

1. [C] Several prose improvements expressed with percent signs are arithmetic differences between percentages. They are reported here as percentage points.
2. [A/B] Table XIII's Known-Answer size range of 6B–7B does not include the listed LLaMA3-8B target. The source does not resolve this mismatch.
3. [A] Claims that greater response count continues improving performance are qualified by nonmonotonic cells in Table XI.
4. [A] The statement that FIPI accuracy improves as N increases is a broad trend, not strictly monotonic: 98.11% at N = 4 becomes 98.09% at N = 8.
5. [A] The unseen-gradient experiment describes five NLP datasets but Table VII includes FIPI alongside four named external benchmarks. The actual table columns are preserved here.
6. [A/B] The paper alternates between 100k IPI instances and the full 110,000-instance injected-plus-benign dataset. These are different counts, not necessarily a contradiction.
7. [A] FIPI attack construction uses seven variants while reporting five grouped categories; combined attacks explain the grouping.
8. [A/B] High Jaccard similarity and poor win rate are different measurements, not inconsistent arithmetic. Broad prose about preserved utility nevertheless requires the low-win-rate qualifications.

## 15. Contributions and novelty

| Contribution type | Author-reported contribution | Qualification |
|---|---|---|
| Conceptual | Combine detection and removal rather than only input rejection | Demonstrated through a particular token-editing approach |
| Methodological | Use target-model attention for fine-grained IPI localization | Requires internal attention access |
| Algorithmic | Two-step response-wise/head-wise attentive statistics pooling with token decisions | Ablations favor transfer in several settings but not every accuracy cell |
| System | Detector, identifier, and optional sanitizer without target-model retraining | End-to-end autonomous-agent execution timing is not fully specified |
| Dataset | FIPI with token-level injection labels, 100k injected instances, and 300 tasks | Underlying dataset and release status not independently inspected |
| Experimental | Compare 15 distinct baselines and test unseen/adaptive attacks | Availability differs by model and task; not every baseline is evaluated everywhere |
| Empirical | Report strong FIPI detection and ASR suppression | Transfer and utility are heterogeneous |

There is no formal theoretical security proof, theorem, or certified robustness bound in the supplied work. The title's broad language should be understood through its empirical scope.

## 16. Limitations

### Authors' stated limitations

[A] RENNERVATE relies on internal attention weights. Users of inaccessible proprietary models need provider support or a locally deployed shadow model. The authors propose ChatGLM-6B as an example shadow model and state that the combined shadow system can run on a single NVIDIA RTX 3090. They do not supply a detailed latency, memory, or shadow-to-target transfer evaluation in this discussion (p. 13).

[A] The sanitizer may not fully remove injected-task-specific content, reducing utility in tasks such as grammar correction. Even a small token mistake can matter for exact editing tasks. Users are advised to consider their tolerance for utility loss (pp. 10, 13).

[A] The present work concerns textual attacks; multimodal IPI and stronger recovery mechanisms remain future directions (p. 13).

### Additional evidence-based analyst observations

[D] The target-model set is limited to five approximately 6B–8B models. The paper does not test a matched standalone-LLM comparison, current arbitrary web environments, or complete long-horizon browser workflows. The 0.5–0.8M parameter count is only the detector, not the model that generates attention. There are no reported repeated-run uncertainties or confidence intervals. The generated probe–witness construction provides useful controllable labels but samples a narrower notion of harm than every possible agent misuse.

[D] Baseline prompts explicitly classify instruction-bearing text as unsafe. This may disadvantage legitimate documents that contain instructions, depending on task context; Figure 7 illustrates the underlying ambiguity. Baseline results therefore apply to the supplied prompt design and configuration, rather than every possible use of those baseline models (pp. 17–18).

[D] Algorithm 1, output-score terminology, detokenization notation, and even-k filtering need clarification for exact reproduction. These are documentation issues visible in the supplied source; they do not establish that the reported numerical results are invalid.

## 17. Threats to validity

The following classifications are analyst assessments, not labels claimed by the authors.

**Internal validity [D].** Controlled insertion and explicit labels help identify known attack spans. The stated pair-level train/test separation addresses one leakage concern, but underlying split manifests, generation code, and data are absent. Distinct generation methods are asserted rather than independently inspected. Manual checking is described, but detailed annotation agreement and per-error counts are not supplied.

**Construct validity [D].** A witness answer measures following the probe; DeepSeek judgment measures apparent following of an injected instruction; neither directly measures every privacy leak or harmful tool action. Figure 7 shows an injected sample that is not behaviorally successful. Detection accuracy and attack success should therefore not be treated as the same construct. Jaccard similarity measures lexical overlap, whereas win rate concerns evaluated output preference.

**External and ecological validity [D].** Fixed NLP tasks, constructed injections, and selected model families may not represent dynamic webpages, varied rendering, long browsing histories, multiple retrieval rounds, or complex tool permissions. These extensions are not evaluated in the supplied material. A shadow model is suggested operationally, but the full proposed shadow deployment is not substantiated with a separate comparative experiment.

**Statistical conclusion validity [D].** Tables report point estimates without repeated-run variation, statistical tests, or confidence intervals. A zero observed ASR is a result on a finite sample, not proof of zero risk. The small sanitization difference between 0.20% and 0.30% should be interpreted with particular caution.

**Reproducibility [D].** The source provides substantial architecture, hardware, optimizer, threshold, attack-budget, and prompt information. Missing versions, epochs, seeds, decoding settings, full attack-loss weighting, validation procedure, and several algorithmic details limit exact reproduction from the paper alone.

## 18. Future work and open questions

### A. Explicit author-proposed future work

[A] Develop stronger recovery mechanisms after IPI, building on fine-grained sanitization. Extend detection and sanitization to multimodal IPI, including images and audio. The authors suggest a unified representation across modalities as a possible route, without reporting an implemented or evaluated multimodal system (p. 13).

### B. Additional open questions

[D] How much does adding retrieval increase compromise relative to the same model without external content? How do tool privileges and autonomous action execution change consequences? Can a defense recover both injected instructions and accompanying task-specific content without damaging exact editing tasks? How accurately does a shadow model identify instructions that a different backend model would obey? What are end-to-end latency and attention-extraction costs? How stable are results across seeds, model revisions, longer contexts, and attack budgets? Can the pseudocode ambiguities be resolved in a released implementation? These questions follow from observed scope and missing details; they are not reported findings.

## 19. Terminology and notation glossary

| Term or symbol | Meaning in this paper |
|---|---|
| LLM | Large language model |
| NLP | Natural language processing |
| LLM-integrated application | Application that combines a model with tasks, retrieved data, and potentially API actions |
| DPI | Direct prompt injection: adversarial instruction in the user-instruction channel |
| IPI | Indirect prompt injection: adversarial instruction in external data |
| RENNERVATE | Proposed attention-based detection and sanitization framework |
| FIPI | Fine-grained Indirect Prompt Injection dataset |
| SEP | Source dataset used to construct FIPI; its acronym is not expanded in the supplied work |
| Probe / witness | Injected test question / distinctive expected answer used to identify task following |
| White-box / black-box | Internal model access / interaction through observable input-output behavior |
| Gradient | Signal used by optimization-based attacks to choose changes |
| Attention head | One attention-processing component within a Transformer layer |
| Attentive pooling | Learned weighted aggregation of features |
| Residual block | Processing block with a skip connection |
| FC / BN | Fully connected layer / batch normalization |
| AP / RB | Attentive pooling / residual block in Table XIII |
| GCG | Greedy Coordinate Gradient attack |
| Neural Exec | Learned execution-trigger injection attack evaluated as unseen |
| PAIR / TAP | Named iterative adaptive attack methods; expansions are not supplied in the paper's main descriptions |
| MRPC | Benchmark for duplicate-sentence detection; full name not supplied here |
| HSOL | Benchmark used for hate-content detection; acronym expansion not supplied |
| Jfleg | Grammar-correction benchmark |
| RTE | Natural-language-inference benchmark; expansion not supplied |
| SST2 | Sentiment-analysis benchmark; expansion not supplied |
| M-H / J-R / S-M / M-S / R-J | MRPC–HSOL / Jfleg–RTE / SST2–MRPC / MRPC–SST2 / RTE–Jfleg |
| Acc / FPR / FNR | Accuracy / false positive rate / false negative rate |
| ASR | Attack success rate; lower is better for the defender |
| WR | Win rate of sanitized-condition outputs relative to benign references; 50% is the stated parity reference |
| JS | Jaccard word-set similarity |
| s / X / p | User instruction / external data / combined prompt |
| G | Backend LLM |
| T / T^−1 | Tokenization / detokenization as described by the paper |
| F / f_i | Input token representation sequence / token at position i |
| R / r_j | Generated response sequence / response token j |
| l / h / m / n | Layer count / head count / response-token count / external-input-token count |
| C_θ / S / M_Θ | Token detector / input aggregation / overall detector |
| Ω / ω_i | Sequence of token scores / two-class score for token i |
| ĝ_i | Predicted token label after smoothing |
| k / N / San | Mean-filter kernel size / residual-block count / sanitization flag |
| F* / F̄ / X̄ | Flagged tokens / retained token sequence / sanitized text |
| ⊕ / ⊖ / ◦ | Concatenation / token removal / function composition |

Undefined acronym expansions are deliberately not filled from outside knowledge.

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Injected FIPI instances | 100,000 | instances | Full constructed dataset | Author-reported | p. 7 |
| Benign FIPI instances | 10,000 | instances | Full constructed dataset | Author-reported | p. 7 |
| Detection test split | 5,000 + 5,000 | injected + benign | Balanced FIPI test | Author-reported | p. 7 |
| Training composition | 95,000 + 5,000 | injected + benign | Totals minus test allocations | Analyst-derived | p. 7 |
| Probe–witness pairs | 100 | pairs | Manually designed | Author-reported | p. 7 |
| Dataset inspection sample | 1,000 | instances | Manual quality evaluation | Author-reported | p. 7 |
| FIPI task coverage | 300 | subtasks | Three broad categories | Author-reported | pp. 2, 7 |
| Main sanitization sample | 1,000 | injected instances | Selected FIPI test examples | Author-reported | p. 8 |
| RENNERVATE detection accuracy | 97.88–99.58 | % | Five models on FIPI | Visually readable | Table I, p. 9 |
| RENNERVATE FIPI FPR | 0.46–2.42 | % | Five models | Visually readable | Table I, p. 9 |
| RENNERVATE FIPI FNR | 0.30–1.82 | % | Five models | Visually readable | Table I, p. 9 |
| FIPI undefended total ASR | 60.80–85.90 | % | Five models | Visually readable | Tables II–III, pp. 9–10 |
| FIPI defended total ASR | 0.00–0.20 | % | Five models | Visually readable | Tables II–III, pp. 9–10 |
| LLaMA3 accuracy gap over TaskTracker | 99.37−95.07 = 4.30 | percentage points | FIPI detection | Analyst-derived | Table I, p. 9 |
| FIPI utility WR | 43.60–46.78 | % | Five models | Visually readable | Table IV, p. 10 |
| Lowest unseen utility WR | 1.90 | % | Falcon, Jfleg–RTE | Visually readable | Table IV, p. 10 |
| Lowest unseen detection accuracy | 80.20 | % | LLaMA3, MRPC–SST2 | Author-reported | Table V, p. 11 |
| Highest unseen defended ASR | 23.90 | % | LLaMA3, MRPC–SST2 | Author-reported | Table VI, p. 11 |
| DeepSeek judge accuracy | 94.50 | % | 200 manually checked balanced examples | Author-reported | p. 10 |
| GCG defended ASR | 0.00–7.00 | % | LLaMA2, five datasets | Author-reported | Table VII, p. 12 |
| Neural Exec defended ASR | 0.00 | % | All five tested datasets on LLaMA2 | Author-reported | Table VII, p. 12 |
| Adaptive PAIR defended ASR | 0.00–19.00 | % | Five models, 100 instances per attack | Author-reported | Table VIII, p. 12 |
| Adaptive TAP defended ASR | 0.00–9.00 | % | Five models, 100 instances per attack | Author-reported | Table VIII, p. 12 |
| Adaptive white-box defended ASR | 0.00–5.00 | % | LLaMA2, 500 iterations | Author-reported | Table IX, p. 12 |
| Detector size | 0.5–0.8 | million parameters | Excludes target or shadow LLM | Visually readable | Table XIII, p. 17 |
| Attention response limit | 32 | tokens | Main setup | Author-reported | p. 6 |
| Filter / threshold / residual blocks | 5 / 5 / 2 | configuration values | Main setup | Author-reported | p. 6 |
| GCG similarity concentration | approximately 0.90–0.95 | dimensionless | Boxplot distributions; exact medians absent | Approximate visual estimate | Figure 6, p. 16 |

Ranges summarize the specified cells and do not imply unreported confidence intervals. Derived differences use the displayed operands. No exact boxplot statistics were reconstructed from image positions.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Retrieved data can carry unauthorized instructions | Defined agent workflow and injection example | Figures 1–2; system model | pp. 1, 3–5 | HIGH for the described mechanism; no matched standalone comparison |
| Token-level attention supports localization | Per-token attention features, two-step pooling, detector outputs | Equations 2–5; Figures 2–3 | pp. 4–6 | HIGH for method description; no theorem of causal interpretation |
| FIPI provides fine-grained labels | Character insertion spans converted to target-token labels | Dataset pipeline; Appendix C | pp. 7, 18 | HIGH for reported construction; dataset files absent |
| FIPI detection is strong | Five accuracies 97.88%–99.58% | Table I; X1 | pp. 8–9 | HIGH within supplied results; uncertainty across runs unavailable |
| FIPI attack suppression is strong | Total ASR 0%–0.2% after sanitization | Tables II–III; X2 | pp. 9–10 | HIGH within finite selected sample |
| Transfer is heterogeneous | Accuracy 80.20% in one setting; ASR 23.90% in one setting | Tables V–VI; X4 | p. 11 | HIGH for reported cells; broad generalization needs qualification |
| Utility can degrade severely | Win rates below 10%; content-removal diagnostic | Tables IV, XII; X3/X5 | pp. 10, 16 | HIGH; exact relation between all failure mechanisms unresolved |
| Selected adaptive attacks are mitigated | PAIR/TAP and detection-aware GCG reductions | Tables VIII–IX; X7/X8 | pp. 11–12 | HIGH for bounded evaluated attacks; no universal robustness guarantee |
| Two-step pooling helps several transfer settings | Large losses after single-pooling replacement | Table X; X9 | pp. 12–13 | HIGH; replacement improves some individual cells |
| Detector is compact | 0.5–0.8M parameters | Table XIII | p. 17 | HIGH for reported count; excludes attention-producing LLM |
| API-only deployment is constrained | Dependence on internal attention and proposed alternatives | Discussion | p. 13 | HIGH; shadow deployment validation is limited |
| Agent architecture enlarges exposure to third-party instructions | External retrieval enters prompt; model may drive API actions | Workflow and threat model | pp. 3–4 | MEDIUM: analyst inference, not comparative empirical finding |

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an assistant to read a webpage and tell you what it says. Someone who controls part of the webpage adds a sentence telling the assistant to forget your request and do something else. The assistant was supposed to treat the page as information, but the attacker wants part of it treated as an order. That is indirect prompt injection.

RENNERVATE watches numerical signals inside the language model while it begins responding. It uses those signals to guess which small pieces of the page are injected instructions. It can warn that the page is suspicious and delete the pieces it identified, keeping the rest available for the real task.

In the paper's main tests, this worked very well: detection accuracy was about 98%–99.6%, and almost none of the selected injected attacks still succeeded after cleaning. But cleaning was not perfect. Some unfamiliar attacks left distracting content behind, and some legitimate tasks became much worse even when the attack stopped. The system also needs internal model information that a normal API user may not receive.

For the question about web agents, the useful lesson is that connecting a model to outside material gives other people a way to place text in what the model reads. If the application then acts on the model's response, the consequences can extend beyond a bad answer. This paper explains and tests part of that risk, but it does not directly prove how much more vulnerable a web agent is than the same model used alone.

## Completeness Audit

The audit compares this explanation with the inventory of all supplied sections and substantive objects. Fully represented means that the item's substantive role and important qualifications are explained; it does not mean every source word or numerical cell has been copied.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, abstract | Yes | Yes | Represented in compressed form | Bibliographic identity below; abstract claims qualified by detailed results |
| I. Introduction | Text and image | Yes | Fully represented | Problem, challenges, contributions, scope |
| II-A. LLMs and architecture categories | Text and images | Yes | Represented in compressed form | Generation and attention emphasized; architecture examples compressed |
| II-B. Prompt injection | Text and image | Yes | Fully represented | Direct/indirect, black/white-box, attack categories |
| III-A. Detection related work | Text and image | Yes | Represented in compressed form | Method classes and author-attributed shortcomings |
| III-B. Prevention related work | Text and image | Yes | Represented in compressed form | Prompt changes and model modification |
| IV-A. Adversary | Text and image | Yes | Fully represented | Goals, control, feedback, gradients |
| IV-B. Defender | Text and image | Yes | Fully represented | Access assumptions and modification restriction |
| IV-C. Formulation | Text and image | Yes | Fully represented | Equations and notation caveats |
| V-A. Token detector | Text and images | Yes | Fully represented | Attention extraction, pooling, residual processing |
| V-B. Identifier | Text and image | Yes | Fully represented | Smoothing, run threshold, pseudocode caveats |
| V-C. Sanitizer | Text and image | Yes | Fully represented | Removal, detokenization, flag |
| VI-A. Setup subsections 1–6 | Text and images | Yes | Fully represented | Prototype, targets, baseline groups, data, metrics |
| VI-B1. Overall detection | Text and images | Yes | Fully represented | X1 and Table I |
| VI-B2. Sanitization and utility | Text and images | Yes | Fully represented | X2/X3 and Tables II–IV |
| VI-C1. Unseen datasets | Text and partial images | Yes | Fully represented | X4/X5; Tables V/VI/XII |
| VI-C2. Unseen attacks | Text and image for opening | Yes | Fully represented | X6; Table VII and Figure 6 |
| VI-D1. Adaptive black-box | Text only | Yes | Fully represented | X7, budgets, Table VIII |
| VI-D2. Adaptive white-box | Text only | Yes | Fully represented | X8, loss description, Table IX |
| VI-E1. Pooling ablation | Text only | Yes | Fully represented | Mixed cell-level effects preserved |
| VI-E2. Token-detector ablation | Text only | Yes | Represented in compressed form | Parameter efficiency and lost sanitization capability |
| VI-E3. Mean-filter ablation | Text only | Yes | Fully represented | Lower accuracy in every tested column |
| VI-F1/F2/F3. Hyperparameters | Text only | Yes | Represented in compressed form | Ranges, important exceptions, reproduction issue |
| VII. Discussion and limitations | Text only | Yes | Fully represented | Model modification comparison, access, residual content |
| VIII. Conclusion and future work | Text only | Yes | Fully represented | Recovery and multimodal directions |
| Formal research questions | Checked | Yes | Absent as formal items | Informal objectives O1–O8 used instead |
| Formal hypotheses | Checked | Yes | Absent as formal items | Utility diagnostic hypothesis separately described |
| X1–X10 experiments | Yes | Yes | Fully represented | Sample, conditions, outcomes, limitations registered |
| Figure 1a/b | Visually | Yes | Fully represented | Attack versus defense illustration |
| Figure 2 | Visually | Yes | Fully represented | Modular architecture and data flow |
| Figure 3a/b | Visually | Yes | Fully represented | Pooling and detector; some dimension glyphs uncertain |
| Figure 4, four panels | Visually | Yes | Represented in compressed form | Distribution trends; exact box statistics unavailable |
| Figure 5 | Visually | Yes | Represented in compressed form | LLaMA3 distribution extension |
| Figure 6, two panels | Visually | Yes | Represented in compressed form | Attack-specific similarity; approximate estimates labeled |
| Figure 7, two examples | Visually | Yes | Fully represented | False positive and unsuccessful-attack false negative |
| Figure 8, three stages | Visually | Yes | Fully represented | Original, detection, sanitization |
| Table I | Visually and textually | Yes | Represented in compressed form | All proposed-method cells; selected diagnostic baseline cells |
| Tables II–III | Visually and textually | Yes | Represented in compressed form | All totals and important residuals; repetitive baseline cells compressed |
| Table IV | Visually and textually | Yes | Fully represented | Major utility pattern and severe failures preserved |
| Table V | Text only | Yes | Represented in compressed form | Scenario ranges and major errors |
| Table VI | Text only | Yes | Represented in compressed form | All-condition reduction and important residual ASRs |
| Table VII | Text only | Yes | Fully represented | ASR series and detection ranges |
| Tables VIII–IX | Text only | Yes | Fully represented | Adaptive outcomes and conditions |
| Table X | Text only | Yes | Represented in compressed form | Design effects, improvements, and losses |
| Table XI | Text only | Yes | Represented in compressed form | Parameter ranges and nonmonotonic outcomes |
| Table XII | Visually and textually | Yes | Represented in compressed form | Diagnostic improvements and counterexamples |
| Table XIII | Visually and textually | Yes | Represented in compressed form | Size scope, baseline examples, mismatch |
| Equations (1)–(6) | Visually and textually | Yes | Fully represented | Definitions, role, inputs/outputs, caveats |
| Algorithm 1 | Visually and textually | Yes | Fully represented | Intended behavior and visible implementation ambiguities |
| Major contributions | Yes | Yes | Fully represented | Conceptual, algorithmic, dataset, system, empirical |
| Author-stated limitations | Yes | Yes | Fully represented | Attention access and residual-content utility loss |
| Appendix A | Text and images | Yes | Fully represented | Figures 5–8, Tables XII–XIII |
| Appendix B | Text and partial images | Yes | Represented in compressed form | Four baseline prompt types; repeated persona wording compressed |
| Appendix C | Text only | Yes | Represented in compressed form | Named-entity task, probe/witness, insertion spans |
| Appendix D | Text only | Yes | Fully represented | Judge follows-instruction criterion |
| Acknowledgments | Text only | Accounted for | Inspected but deliberately omitted as non-substantive | Funding and thanks do not change the method or findings |
| References 1–99 | Text; final portion also image | Accounted for | Represented in compressed form | Not independently validated or treated as reviewed external works |
| Separate supplementary material | Not supplied | Limitation stated | Missing from supplied material | No additional artifact reviewed |

### Missing or inaccessible material

No text pages are missing within pages 1–18. Images for pages 11–15 and 18 are not supplied, so Tables V–XI and final appendix material have text-only coverage. No source PDF binary, code repository contents, FIPI records, weights, raw predictions, training logs, annotation records, or independent replication outputs are available in the supplied evidence. Their absence prevents artifact-level verification. No separate supplement is identified in the supplied material.

### Uncertain interpretations

Some Figure 3 dimensional glyphs are unclear. The logits-versus-probabilities wording, direct detokenization of objects called embeddings, end-of-sequence run handling, and even-k mean-filter formula are unresolved. Exact plot medians and whisker definitions are unavailable. Table VII's detection denominators and Table IX's sample count are less explicit than the main balanced-test setup. Table XIII's Known-Answer parameter range does not cover the listed 8B target. The proposed shadow-model workflow is not documented with a distinct end-to-end evaluation. Confidence is HIGH for directly readable reported numbers, MEDIUM for architectural relevance to the user's comparative question, and UNKNOWN for undocumented implementation behavior.

### Deliberately compressed material

Repeated introduction/conclusion claims, individual related-work citations, the 99-item bibliography, full attack strings, repeated baseline-prompt persona text, minor architectural examples, and many secondary baseline or hyperparameter cells are compressed. They are accounted for by category, purpose, representative values, relevant exceptions, and source locators. Appendix C's example uses a named-entity-recognition task, a Fake Completion injection, the January witness, character span [182, 266], and token span [39, 66]. Those span conventions and tokenizer identity are not fully specified; the example's background factual story is data content, not independently verified history.

### Potential omissions

No known substantive object in the established document inventory is entirely unrepresented. This report does not transcribe every table cell, bibliography entry, or prompt sentence. It cannot establish completeness of unavailable artifacts or validate claims against the underlying experiments. The source-grounded assessment is comprehensive for the supplied textual and visual inventory within those disclosed limits.

Bibliographic identity [A]: Attention is All You Need to Defend Against Indirect Prompt Injection Attacks in LLMs, by Yinan Zhong, Qianhao Miao, Yanjiao Chen, Jiangyi Deng, Yushi Cheng, and Wenyuan Xu, Zhejiang University. Page 1 identifies the Network and Distributed System Security Symposium 2026, 23–27 February 2026, San Diego, and DOI 10.14722/ndss.2026.240394. These are supplied-document details, not externally verified publication metadata.
