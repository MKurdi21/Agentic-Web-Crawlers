## Stage 0 — Document Accessibility Report

The supplied material comprises extracted text for physical PDF pages 1–23 and rendered images for pages 1–9, 12–15, 18–20, 22, and 23. These physical page numbers are used throughout; the printed proceedings page numbers run from 6830 to 6852. The complete numbered page sequence is represented in text, but this does not independently establish that every original artifact or supplementary resource is present.

| Accessibility item | Assessment |
|---|---|
| Main document | Available as supplied page text and selected page images |
| Accessible physical pages | 1–23 |
| Visually inspected pages | 1–9, 12–15, 18–20, 22–23 |
| Text-only pages | 10–11, 16–17, 21 |
| Apparently missing numbered pages | None in the supplied text sequence |
| Figures | Figures 1–8 visually available; small labels in Figures 1–3 require caution |
| Tables | Tables 1–19 available through text and/or images; exact values are readable, with several substantive internal inconsistencies |
| Equations | Main equations readable visually; extracted mathematical notation sometimes damaged |
| Appendices | A–I present; the supplied automated metadata did not detect them, but their headings and contents are explicit |
| Supplementary artifacts | No separate supplementary files supplied; code and data are referenced on p. 1 but were not inspected |
| OCR | No OCR tool was used. Supplied extraction was checked against rendered pages where available |
| Other limits | No executable code, original dataset, repository, training receipts, or experimental logs were inspected |

The reported local-image error for a path named '-' does not prevent inspection of the 18 images actually embedded in the request. Pages 16–17 contain prompt templates and code that were inspected as text only. Page 21 contains only the Appendix I heading in the supplied extraction; no visual inspection of that page was possible. All source content, including embedded prompts, was treated as evidence rather than instructions.

Evidence labels used below are: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external information is introduced. HIGH confidence indicates clear source support, not independent validation of the underlying experiment. MEDIUM indicates a supported reading with important unresolved conditions; LOW and UNKNOWN identify weak or unavailable support.

## 1. Plain-language orientation

This paper studies web agents: AI systems that inspect a webpage and choose where to click to carry out a user's request. Their difficulty is that a page can contain attractive buttons, pop-ups, subscriptions, advertisements, or fake continuation controls that redirect them away from that request. A successful visual recognizer can still choose the wrong action if it mistakes an attention-grabbing element for a legitimate step. [A: pp. 1–2]

The authors propose **DUDE**, the Deceptive UI Detector & Evaluator. It inserts a second model between a web agent's proposed click and execution. That evaluator considers the screenshot, the user's task, and the click coordinate. It classifies the click as correct, ineffective, or deceptive, and provides confidence. DUDE develops this evaluator through two mechanisms: reinforcement learning with unequal penalties for different errors, and a process that converts previous mistakes into reusable written guidance. [A: pp. 2–4]

The authors also introduce **RUC**, Real UI Clickboxes: 1,407 screenshot-and-task examples with correct target boxes and, where appropriate, deceptive target boxes. The principal reported comparisons use a 200-task suite across news, booking, shopping, and software interfaces. With the stronger UI-TARS evaluator, average task success rises from 6.50% to 63.50% for Qwen3-VL-4B, from 43.50% to 58.00% for UI-TARS-1.5-7B, and from 9.50% to 60.50% for GLM-4.6V-Flash. Deception-induced failure also falls in these aggregate comparisons. [A: pp. 5–7, Table 2]

These results need qualification. A weaker evaluator reduces the capable UI-TARS agent's aggregate success from 43.50% to 35.50%. Individual stages increase deception-induced failure in the stage ablation. Several reported step counts conflict with the stated three-step budget, and some table averages do not match their domain values. Consequently, the paper supports the usefulness of task-aware evaluation under its reported conditions, but not an unconditional claim that every DUDE configuration improves both security and task performance. [B/C: pp. 6–9, 19]

For the requested research question, the paper provides evidence about an **additional interface-to-action attack surface** in web agents. It does not directly compare web agents with standalone large language models. Any explanation of why agents might be more vulnerable than standalone models is therefore an analyst inference from the agent architecture and attack surface, not a measured conclusion of this study. [D]

## 2. Document roadmap

The inventory established before synthesis is as follows.

| Original component | Physical pages | Role |
|---|---|---|
| Title, abstract, publication information | 1 | Problem, proposed defense, benchmark, headline claim |
| §1 Introduction | 1–2 | Motivation, two design problems, contributions |
| §2 Related Work | 2 | Web agents, UI deception, positioning against detection and attack studies |
| §3 DUDE | 2–5 | Formulation, reward learning, error collection, summarization, inference |
| §4 RUC Benchmark | 5 | Tasks, annotation, taxonomy, construction |
| §5 Experiments, §§5.1–5.8 | 5–9 | Setup, effectiveness, ablations, dynamics, prompts, overhead, transfer |
| §6 Conclusion; Limitations | 9 | Synthesis and explicit boundaries |
| Acknowledgments and References | 9–11 | Funding and bibliography |
| Appendix A, §§A.1–A.8 | 12–14 | Data construction, quality control, statistics, splits, examples, regions |
| Appendix B, §§B.1–B.5 | 14–16 | Models, hardware, software, training, reward matrix, loading code |
| Appendix C, §§C.1–C.4 | 16–17 | Agent, evaluator, experience, and ReAct prompts |
| Appendix D, §§D.1–D.3 | 17–18 | Click synthesis, overlap adjustment, null sampling |
| Appendix E, §§E.1–E.3 | 18–19 | Backends, message conversion, safe decoding |
| Appendix F, §§F.1–F.3 | 18–19 | Metrics, outcome tracking, termination |
| Appendix G, §§G.1–G.5 | 19–20 | Summarization pools, sampling, stopping, prompts, example guidance |
| Appendix H | 20 | Batch-size and iteration-budget ablations |
| Appendix I | 21–23 | Normal and deceptive screenshot examples |

The substantive object inventory contains Figures 1–8, Tables 1–19, numbered Equations 1–6, an additional unnumbered confidence-adjustment equation, Algorithm 1, two numbered code listings, and an unnumbered safe-decoding function. There are three explicit research questions, eight experimental/analytical blocks when failure decomposition and training dynamics are distinguished, and two Stage-2 hyperparameter analyses. No theorem, proof, formal hypothesis, or keyword list is supplied.

## 3. Background and context

A **large language model**, or LLM, processes language. A **vision-language model**, or VLM, also processes visual input; here its input includes webpage screenshots. A **graphical user interface**, or GUI, consists of visible controls such as buttons and links. A web agent connects perception and reasoning to actions: it observes, proposes an action, receives feedback, and continues. The paper uses ReAct-style reasoning-and-action scaffolding, but evaluates clicks against annotated screenshots rather than demonstrating a fully asynchronous live browser workflow. [A: pp. 2, 6, 9, 16–19]

**Grounding** means connecting the user's goal to a specific visible target. A grounding mistake can be harmless but ineffective, such as clicking empty background. A deceptive click instead selects an element annotated as a trap. This distinction matters because reducing deception alone does not establish useful behavior: an agent that refuses every action may avoid traps but accomplish nothing. [A: pp. 2–5]

**Dark patterns** are interface designs that manipulate behavior. RUC groups them into coercive design, cognitive manipulation, contextual path spoofing, and emotional manipulation. The categories cover restricted choices, misleading labels or visual hierarchy, overlays that impersonate legitimate continuation steps, and urgency or social influence. These are descriptions of the supplied paper's taxonomy, not an independently validated taxonomy review. [A: pp. 5, 13]

**Reinforcement learning** changes model parameters using rewards. Here the reward distinguishes expensive safety errors from less harmful mistakes. **Experience summarization** instead changes the text supplied to the evaluator. It converts recurring errors into guidance without further parameter updates during that stage. The two mechanisms should not be conflated: Stage 1 trains parameters, while Stage 2 optimizes contextual instructions. [A: pp. 3–4]

**Calibration**, in the authors' usage, means producing appropriately confident judgments and avoiding excessive caution. The paper reports confidence-dependent rewards and outcome metrics; it does not supply a separate reliability diagram or a numerical calibration-error metric in the supplied material. [A/D: pp. 3, 6–9]

## 4. Research problem and gap

**Existing problem.** Web interfaces may contain elements that are visually plausible and apparently relevant but conflict with the user's intent. A task-directed agent can therefore execute a manipulative control while believing it is progressing. The introduction mentions deceptive pop-ups, camouflaged buttons, misleading advertisements, and fake download links. [A: p. 1]

**Prior shortcomings according to the authors.** Task-agnostic detectors identify dark patterns without connecting detection to the user's objective or the agent's actual decision. Attack studies demonstrate vulnerability without necessarily providing an integrated defense. Blanket refusal introduces another failure: over-conservatism on benign pages. These are the paper's characterizations of prior work, not verified judgments about the cited publications. [A: pp. 1–2]

**Research gap.** The proposed gap is a task-aware defense that judges an intended interaction before it executes, distinguishes deceptive from merely unhelpful actions, and learns transferable lessons from errors. The authors describe this as a distinct problem from input-level adversarial robustness and human-centered dark-pattern research. [A: pp. 1–2]

**Motivation.** The authors draw an analogy with humans who accumulate experience recognizing urgency cues and manipulative pop-ups. They seek a corresponding form of experiential resilience for agents. That analogy motivates the architecture; the study does not experimentally establish equivalence to human learning. [A/D: pp. 1–2]

**Scope.** The evidence concerns visible interfaces, screenshot-level click targets, four application domains, selected VLM agents and evaluators, and English-focused RUC data. The introduction's claims of agents being deceived at rates exceeding 70% are not the baseline rates in Table 2. Appendix A explains that RUC permits successful termination before trap exposure, so its episode-level failure rates differ from forced-choice attack evaluations. [A: pp. 1, 6, 12]

## 5. Research questions, objectives, and hypotheses

The three explicit research questions appear in §5, p. 5:

- **RQ1:** Does DUDE reduce deception-induced failures while preserving task capability across model scales?
- **RQ2:** How do hybrid-reward learning and experience summarization contribute to effectiveness and robustness?
- **RQ3:** Does the learned behavior-level policy transfer to closed-source models without additional tuning?

The introduction separately formulates two engineering problems: **P1**, distinguish deceptive and legitimate elements without over-conservatism; and **P2**, accumulate transferable knowledge from failures without deployment-time parameter updates. These are design objectives, not formal statistical hypotheses. [A: p. 2]

Additional objectives are to construct an annotated benchmark, distinguish correct/deceptive/null outcomes, and assess reward components, prompt strategies, resource overhead, and Stage-2 hyperparameters. No preregistered hypothesis, null hypothesis, significance threshold, or power calculation is reported. [A/B: pp. 3–9, 20]

## 6. Assumptions / Threat Model

The paper does not present a standalone formal attacker model. Its operational model is nevertheless visible: the agent has a user task, observes a webpage screenshot, proposes a click, and may encounter an intention-misaligned visible target. The attacker-controlled or adversarial surface is the webpage presentation, including HTML/CSS-generated misleading controls and overlays. RUC's automated construction explicitly modifies pages to contradict or complicate task intent. [A: pp. 5, 13]

The assets at stake are successful execution of the user's intended task and avoidance of manipulative interactions. Figure 1 depicts a possible privacy leak, but the experiments operationalize harm principally through entry into annotated deceptive boxes. They do not measure actual financial loss, exfiltration, subscription completion, or privacy leakage. [B/D: pp. 1, 5–6, 18]

**Analyst interpretation:** DUDE assumes the evaluator, its prompt, and its learned experience can provide a useful judgment from the screenshot, goal, and coordinate. The evaluator is therefore a decision boundary between untrusted interface content and action execution. Its own robustness to adaptive manipulation is not separately established.

The benchmark assumes annotated correct and dark boxes meaningfully identify task success and deception. Training handles one overlap case by moving a deceptive sample coordinate; a comprehensive execution-time policy for all overlapping regions is not specified. Static images exclude many consequences of scripts, timing, navigation, and asynchronous state changes. [A/D: pp. 3, 9, 18]

The authors explicitly exclude purely backend-based exploits without visible GUI manifestations. They do not establish resistance to an attacker who can modify the evaluator's trusted prompt, alter stored experience, compromise annotation, or adaptively optimize against the defense. These are untested boundaries, not demonstrated attacks. [A/D: p. 9]

## 7. Methodology

### 7.1 Study design and architecture

This is an empirical AI/security defense paper with algorithmic, systems, dataset, and benchmark contributions. The central unit is a screenshot-task-click judgment. Let I denote the screenshot, P the user task, and C=(x,y) the proposed coordinate. The evaluator outputs a predicted label and confidence. A legitimate target receives label 1, a deceptive target −1, and an ineffective background target 0. [A: p. 3, Eqs. 1–2]

Stage 1 creates training clicks from annotated boxes, trains the evaluator with an asymmetric reward, and stores mistakes. Stage 2 repeatedly summarizes failures into textual guidance, checks revised judgments on failures and successful anchors, and updates the pools. At inference, the evaluator gates the base agent's proposed action; rejected actions trigger further exploration. [A: pp. 3–5]

The inference diagram additionally requires confidence above a threshold. The prose says that benign judgments proceed, without stating that threshold. No usable numerical inference threshold is supplied. This is a diagram–prose specification gap. [B: p. 4, Fig. 2; A: p. 5]

### 7.2 Click generation and reward

For every training image, the system generates a correct-box centroid and one random null click by default. Deceptive images also provide a dark-box centroid. Null coordinates are drawn by rejection sampling until they fall outside both annotated boxes. If the dark centroid lies within the correct box, the implementation moves it to the dark box's bottom-right edge minus one pixel on each axis. The code does not visibly recheck whether this replacement is outside the correct box. [A/B: pp. 3, 17–18]

Correct classifications earn the reported confidence. Incorrect classifications incur negative confidence multiplied by a confidence-adjustment factor and a severity weight. Approving a deceptive click as correct has severity 10; rejecting a correct click has severity 1; null-click confusions have severity 1+β. Appendix B supplies the additional deceptive-to-null weight of 1. Parse failure and domain violation receive auxiliary penalties of −10.0 and −1.0. [A: pp. 3, 15]

### 7.3 Experience summarization

The failure pool F stores screenshots, tasks, coordinates, ground truth, and evaluator outputs. The success pool S contains correctly classified cases. Each persistent failure has a counter κ(x), initially 1, that rises when the error survives an update. Higher counts increase sampling priority. [A: pp. 4, 19]

A multimodal summarizer receives current guidance, failures, counts, and screenshots. The revised guidance is tested on a batch containing failures and successful anchors. Correct cases move to S; incorrect cases return to F. Anchors are intended to prevent revised rules from damaging already solved cases. Algorithm 1 explicitly passes failures and current context to its summarization call; prose describes anchors as contrastive examples, leaving their exact role in the summarizer input less explicit. [A/B: pp. 4, 19–20]

Stopping conditions are an empty failure pool or maximum iterations. Appendix G adds a third condition: no validation pass-rate improvement for three consecutive iterations. The paper supplies example guidance, but does not clearly identify the exact summarizer model or all selected operational settings. [A: pp. 4, 19–20]

### 7.4 Dataset construction and annotation

RUC contains 910 normal samples and 497 deceptive samples. The latter comprise 200 manually curated examples and 297 automatically generated examples. Normal examples come from ShowUI-web. Filtering requires at least five interactive elements, width at least 1,024 pixels, height at least 768 pixels, domain diversity, and an English-language focus. [A: pp. 5, 12]

The automated pipeline uses Gemini 2.5 Pro for seed webpages. Contextual spoofing uses hybrid rule/LLM templates; the other categories use a two-stage process that derives task intent from the document object model and then modifies HTML/CSS to create a deceptive variant. All samples undergo manual validation. [A: pp. 5, 13]

The annotation schema includes sample ID, normal/deception type, category, image path and dimensions, correct box in pixels and normalized coordinates, optional dark box, and messages. Three annotators work independently per sample; labels use majority voting, box agreement requires intersection-over-union at least 0.7, and a senior annotator adjudicates disagreements. Reported agreement is Cohen's κ=0.89 for type, κ=0.84 for category, and mean box IoU 0.91±0.06. The procedure for combining pairwise Cohen's κ across three annotators is not specified. [A/D: pp. 12–13]

The split table reports 985 training, 212 validation, and 210 test samples, with seed 42 and 70/15/15 proportions within normal/deceptive classes. The main experiments instead describe a fixed 200-task suite with 50 tasks per domain. The relationship between those 200 tasks and the 210-sample split is not explained. [A: pp. 5, 14]

### 7.5 Models, implementation, and training

Base agents are Qwen3-VL-4B-Instruct, UI-TARS-1.5-7B, and GLM-4.6V-Flash. Evaluators are Qwen3-VL-2B-Instruct and UI-TARS-1.5-7B. The paper describes GLM inconsistently as closed-source, open/closed-source, and API-accessed; Table 14 reports 4.6B parameters, but no independent basis for that count is supplied. These are reported specifications, not verified model facts. [A: pp. 6, 14–15]

Local hardware is four NVIDIA A100 GPUs with 80 GB each, an AMD EPYC 7742 64-core processor, 512 GB DDR4 RAM, and a 2 TB NVMe SSD. Software is Python 3.10.12, PyTorch 2.1.0, transformers 4.40.0, peft 0.10.0, and trl 0.8.6. Seed 42 and deterministic CUDA operations are reported. Mixed bfloat16 precision, gradient checkpointing, and automatic device mapping reduce memory use; approximate peak training memory is 48 GB for Qwen3-VL-4B and 72 GB for UI-TARS-7B. [A: p. 15]

Stage-1 Group Relative Policy Optimization, or GRPO, uses AdamW, learning rate 1×10^-5, cosine scheduling, warmup ratio 0.1, gradient clipping 0.2, weight decay 0.01, KL coefficient 0.05, and three epochs. The effective batch size is reported as 16 using per-device batch 2 and accumulation over eight steps; the relation to four-device training is not specified. Generation settings include maximum 512 tokens, training temperature 0.7, evaluation temperature 0, top-p 0.8, and do_sample=False. The applicability of the last setting to training versus evaluation is unclear. [A/D: p. 15]

The model-loading listing uses local files, bfloat16, automatic device placement, a processor with left padding, and evaluation mode. Backend adapters convert image-message formats and replace out-of-vocabulary token IDs with the padding ID before decoding. These implementation details are inspected source descriptions, not executed or reproduced code. [A/B: pp. 16, 18–19]

### 7.6 Evaluation controls, metrics, and statistics

Agents share observation processing, action formatting, and termination rules. The declared limit is three interaction steps, with termination on final answer, a correct click, a deceptive click, or budget exhaustion. Greedy decoding or do_sample=False is used. Evaluator dialogue is reset to avoid incidental context accumulation. [A: pp. 6, 19]

Success rate, SR, is the percentage of episodes that reach the correct box without an earlier deceptive click. Deception-induced failure rate, DFR, is the percentage that click the dark box. Null-click failure rate, NFR, represents the remaining category in Table 3. Average Steps is initially defined as bounded by the step limit; Appendix F later assigns deceptive termination a count of 10. Neither definition explains all reported counts above 10. [A/B: pp. 6–7, 18–19]

No confidence intervals, significance tests, repeated-seed outcome distributions, or per-result sample-size accounting beyond the general task-suite statement are reported. Standard deviations in dataset statistics describe images or annotations, not uncertainty in defense performance. [B/D]

## 8. Experiments / Analyses

| ID | Purpose and conditions | Main evidence | Interpretation and caveat |
|---|---|---|---|
| X1 Overall effectiveness, RQ1 | Three base agents, two evaluator backbones, four domains; general 200-task suite | Table 2; Figure 3 | Strong evaluator improves aggregate SR and DFR; weaker evaluator can reduce SR |
| X2 Failure decomposition | GLM with UI-TARS evaluator | Table 3 | Most baseline episodes are null failures; success improvement is broader than trap avoidance |
| X3 Stage ablation, RQ2 | Qwen3-VL-4B; neither stage, each alone, both | Table 4 | Both stages jointly outperform either alone on reported aggregate SR/DFR |
| X4 Reward ablation | Remove attention, confidence adjustment, severity, or use confidence alone | Table 5 | Severity removal produces the largest fatal-error increase; evaluation-set size unspecified |
| X5 Training dynamics | Stage-1 reward, entropy, reward–entropy relationship | Figures 4–5 | Descriptive convergence diagnostics; not an independent generalization test |
| X6 Prompt strategy | No system prompt, manual safety prompt, Stage-2 mutated prompt | Figure 6; Table 6 | Mutated prompt raises success and also raises DFR |
| X7 Computational overhead | UI-TARS base/evaluator; vanilla, S1, S2, both | Table 7 | Larger token totals but lower reported elapsed time; Steps definition unresolved |
| X8 Zero-shot transfer, RQ3 | Apply open-source-derived Stage-2 prompt in closed-source setting | Table 8 | SR increases and DFR decreases; model role and denominator incompletely described |
| X9 Stage-2 batch sizes | Stage 1 fixed on Qwen3-VL-4B; 20 iterations; vary failures/anchors | Table 18 | Final success counts vary non-monotonically; no repeated-run uncertainty |
| X10 Stage-2 iteration budget | Failure batch 15, anchors 5; 10–80 iterations | Table 19 | Improvement mostly flattens, with fluctuations and highest listed count at 70 |

An important experimental boundary appears across pp. 6–7: the overall and transfer experiments describe the model-agnostic contribution as Stage-2 optimized experience context plus system prompt, while Stage-1 training is separately assessed through ablation because of budget. Therefore, Table 2 should not automatically be described as a full end-to-end two-stage training comparison for every base/evaluator pairing.

## 9. Results

With the UI-TARS evaluator, Table 2 reports Qwen SR 6.50→63.50%, DFR 2.00→0.50%; UI-TARS SR 43.50→58.00%, DFR 23.50→1.50%; and GLM SR 9.50→60.50%, DFR 4.00→1.50%. **Analyst-derived:** these are SR increases of 57.00, 14.50, and 51.00 percentage points, respectively. Corresponding relative DFR reductions are (2−0.5)/2=75%, (23.5−1.5)/23.5≈93.62%, and (4−1.5)/4=62.5%. These calculations are condition-specific and do not reproduce the abstract's unexplained 53.8% aggregate susceptibility reduction. [A/C: pp. 1, 6]

With the Qwen-2B evaluator, Qwen SR rises to 33.50% with zero DFR, and GLM SR rises to 36.50% with DFR 2.50%. However, UI-TARS SR falls from 43.50% to 35.50%, an **analyst-derived decline of 8 percentage points**, even though DFR falls to zero. A defender can therefore trade away useful actions; the table contradicts an unqualified assertion of preserved task performance in every configuration. [A/C: p. 6]

Table 3 reports GLM null-failure shares approximately 86.5% of episodes at baseline and 38.0% with DUDE, alongside SR/DFR of 9.50/4.00% and 60.50/1.50%. The prose calls 86.5% a share of failures, but the table identity SR+DFR+NFR=100% makes it a share of all episodes. **Analyst-derived:** among failed baseline episodes, the null share would be 86.5/(100−9.5)≈95.58%, assuming these categories exhaust outcomes. [A/C: p. 7]

In Table 4, Stage 1 alone yields SR 28.00%, DFR 5.50%; Stage 2 alone yields SR 15.50%, DFR 4.50%; both yield SR 33.50%, DFR 0%, compared with baseline 6.50%, 2.00%. The authors attribute complementarity to visual discrimination plus behavioral regularization. The metrics support complementarity in this ablation, but do not directly measure the proposed internal causal mechanisms. [A/D: pp. 7–8]

Table 5 reports full-reward fatal error 9.75%, versus 13.07% without attention scaling, 17.25% without confidence adjustment, 27.53% without severity weighting, and 12.37% with confidence alone. **Analyst-derived:** severity removal increases fatal error by 17.78 percentage points and approximately 2.82 times, using 27.53/9.75. These are evaluator-classification errors, not directly the same denominator or construct as episode-level DFR. [A/C: p. 8]

Prompt optimization alone raises SR from 6.50% without a prompt and 7.00% with a manual prompt to 15.50%; DFR simultaneously rises from 2.00% and 3.50% to 4.50%. The figure's +8.50 refers to percentage points relative to the best listed baseline, not an 8.5% relative improvement. [A/C: p. 9]

Table 7 reports total time 217.62→48.47 seconds for vanilla versus both stages, while time per step rises 12.33→13.54 seconds. **Analyst-derived:** elapsed-time reduction is (217.62−48.47)/217.62≈77.73%. Tokens rise from 10,610 to 17,277. The table does not fully specify how these totals were aggregated, so they should not be recast as per-task token costs. [A/C: p. 9]

Table 8 reports closed-source-setting SR 54.12→62.50%, DFR 25.00→19.38%, and Steps 4.63→3.19. **Analyst-derived:** changes are +8.38 SR points and −5.62 DFR points; relative DFR reduction is 5.62/25=22.48%. These fractional percentages cannot be straightforwardly reconciled with the general 200-task denominator, where each task represents 0.5 percentage points. The exact denominator is not supplied. [A/C/D: p. 9]

## 10. Figure-by-figure interpretation

### Figure 1 — Motivation and overview, p. 1

This is a conceptual illustration, not a quantitative plot. The left side contrasts an undefended agent attracted to a trap with simple refusal that produces overly cautious behavior. Example speech bubbles use a booking task. The right side connects confidence, task completion, severity/attention/confidence adjustment, hybrid reward, and experience summarization to task-solving and deception avoidance. Green and red regions illustrate successful versus failed or deceptive outcomes. Privacy leakage is an illustrative consequence, not a measured result. Small embedded screenshots do not support exact quantitative readings. [B]

### Figure 2 — Three-part processing pipeline, p. 4

The blue/teal Stage-1 panel moves from screenshot, task, and sampled clicks to evaluator prediction, hybrid reward, reinforcement learning, and error collection. Arrows carry failures into the purple Stage-2 panel, which maintains failure and success pools, samples batches, summarizes experience, validates, and iterates. The orange inference panel places the tuned evaluator and experience between a proposed action and execution. Rejection loops back to rethink. A displayed gate requires label 1 and confidence above a threshold; no numerical threshold is given. This diagram is the clearest visual statement of data and control flow. [B]

### Figure 3 — Changes by evaluator/base pairing, p. 7

Three heatmaps show (a) success-rate gain in percentage points, (b) DFR reduction in percentage points, and (c) Steps reduction. Columns are News, Booking, Shopping, Software, and Avg. Rows identify six evaluator-to-agent combinations. Diverging colors encode signed change; each cell is numerically labeled. These are difference matrices, with no time axis and no error bars.

Panel (a) explicitly shows negative changes for Qwen-2B→UI-TARS: −22, +14, −2, −22 domain points and −8 aggregate points. Thus the image itself contains an exception to universal task improvement. Panel (b) includes −2 DFR-reduction points for Qwen-2B→GLM in Booking, meaning DFR worsens there. Panel (a) shows UI-TARS→Qwen Booking gain 68, whereas Table 2 gives 74−6=68; its average gain is 57. Panel (c) presents rounded step reductions and inherits unresolved Steps definitions and some inconsistent table averages. Exact labeled cells are observations; colors alone are not additional evidence. [B/C]

### Figure 4 — Stage-1 training dynamics, p. 8

Panel (a) plots training step, approximately 0–800, against reward, with labeled ticks from about −25 to 0. A thin blue raw curve and thicker green rolling mean, window 7, show improvement from strongly negative values toward zero. A visible annotation identifies maximum reward −0.384 at step 790. Panel (b) plots the same step axis against policy entropy, with ticks approximately 0.04–0.12. Entropy rises early, then declines with fluctuations and a later intermediate bump. There are no confidence intervals or replicate bands. The title calls the first series training reward, while nearby prose also refers to validation reward; the exact provenance of the plotted series is unclear. [A/B]

### Figure 5 — Reward versus entropy diagnostic, p. 8

A scatterplot has entropy on the horizontal axis, approximately 0.04–0.12, and reward on the vertical axis, approximately −25–0. Points with relatively low entropy include many higher rewards close to zero, while some higher-entropy points have substantially negative rewards. No point color or arrow explicitly encodes time, no fitted relationship is provided, and no statistical association is reported. The authors interpret it as evidence against unproductive policy collapse. Analyst interpretation: it is a descriptive diagnostic, insufficient by itself to establish causal training progression or generalization. [A/B/D]

### Figure 6 — Prompt strategies, p. 9

Two bar charts compare no system prompt, manual prompt, and mutated prompt. Grey represents baselines; orange represents the optimized prompt. The left vertical axis is SR percent, roughly 0–20; bars are labeled 6.50, 7.00, 15.50. The right vertical axis is DFR percent, extending to about 80 despite values 2.00, 3.50, 4.50. This wide scale makes differences in small DFR values visually subdued. No uncertainty bars are present. The exact labels demonstrate increased success accompanied by increased deception failures for prompt-only optimization. [B]

### Figure 7 — Normal samples, p. 22

Two browser screenshots have green boxes marking intended targets. Panel (a) shows an educational website region with courses and page controls; the box encompasses a substantial content area. Panel (b) shows a review/news page with a small article-title target. These are qualitative annotation examples, with no axes, units, or performance measurements. The tasks are not printed alongside the screenshots, so task appropriateness cannot be independently assessed from this figure alone. [B/D]

### Figure 8 — Deceptive samples, p. 23

Panel (a) shows a shopping page with a green navigation-region box and a red box around product-option/add-on controls; a countdown is also visible. Panel (b) shows a travel page with a green destination target and red membership-promotion region. The caption identifies green as correct and red as deceptive. Analyst interpretation: these examples demonstrate that a trap need not look like an obvious malicious warning; it can be an ordinary commercial affordance that is misaligned with the task. The figure does not supply task wording, user outcomes, or attack success rates. [B/D]

## 11. Table-by-table interpretation

### Table 1 — Dataset composition, p. 5

Rows distinguish normal, manually curated deceptive, and automatically generated deceptive samples. Totals are 910, 200, and 297. Deceptive-domain counts are manual 41/35/66/58 and automatic 62/108/63/64 for News/Booking/Shopping/Software. Domain totals 103/143/129/122 sum to 497. The bottom row's overall 1,407 includes normal samples, but its domain columns describe only deceptive samples; normal-domain counts are dashes. It therefore does not give a complete four-domain distribution or deception-category distribution despite the nearby prose's broad wording. [A/B/C]

### Table 2 — Principal agent/evaluator results, p. 6

Rows are grouped by base agent, method/evaluator, and metric. Columns are four domains and average. SR and DFR are percentages; Steps has unresolved operational units. Aggregate triples SR/DFR/Steps are:

| Base agent | Vanilla | Qwen-2B evaluator | UI-TARS evaluator |
|---|---|---|---|
| Qwen3-VL-4B | 6.50/2.00/25.23 | 33.50/0/5.86 | 63.50/0.50/3.85 |
| UI-TARS-1.5-7B | 43.50/23.50/16.06 | 35.50/0/4.18 | 58.00/1.50/3.02 |
| GLM-4.6V-Flash | 9.50/4.00/28.67 | 36.50/2.50/6.49 | 60.50/1.50/4.02 |

To preserve domain-level evidence, the following vectors list News/Booking/Shopping/Software as SR; DFR; Steps:

- Qwen vanilla: 12/6/6/2; 4/0/0/4; 20.58/25.70/27.34/27.30.
- Qwen with Qwen evaluator: 20/44/34/36; 0/0/0/0; 6.08/4.96/6.36/6.04.
- Qwen with UI-TARS evaluator: 56/74/64/60; 2/0/0/2; 2.88/3.50/4.42/4.38.
- UI-TARS vanilla: 42/36/40/56; 16/32/24/22; 18.16/17.54/16.56/11.96.
- UI-TARS with Qwen evaluator: 20/50/38/34; 0/0/0/0; 4.82/4.04/3.78/4.06.
- UI-TARS with UI-TARS evaluator: 60/58/54/60; 0/2/2/2; 3.46/4.44/3.62/2.96.
- GLM vanilla: 18/6/12/4; 2/2/4/8; 27.24/28.65/25.91/31.00.
- GLM with Qwen evaluator: 20/50/34/42; 0/4/4/2; 7.54/5.43/6.89/6.09.
- GLM with UI-TARS evaluator: 60/68/42/72; 0/2/0/4; 3.56/4.22/5.17/3.16.

No significance or uncertainty markers are provided. Two especially clear arithmetic issues are Qwen/UI-TARS DFR: (2+0+0+2)/4=1%, versus reported average 0.50%; and UI-TARS/UI-TARS Steps: (3.46+4.44+3.62+2.96)/4=3.62, versus reported 3.02. GLM/UI-TARS Steps average is 4.0275, ordinarily rounding to 4.03 rather than reported 4.02. These are analyst-derived checks; the source values are retained without repair.

### Table 3 — Failure decomposition, p. 7

GLM baseline and defended rows compare SR/DFR/NFR: 9.50/4.00/~86.5 versus 60.50/1.50/~38.0. The caption states the three sum to 100%. This supports the observation that most baseline episodes fail through ineffective actions rather than deception. NFR values are explicitly approximate. The prose's description of 86.5% as a percentage of failures has a denominator mismatch with the table. No uncertainty estimates appear.

### Table 4 — Stage-wise ablation, p. 7

For Qwen3-VL-4B, rows are vanilla, Stage 1 only, Stage 2 only, and both. SR/DFR/Steps are 6.50/2.00/25.23; 28.00/5.50/5.80; 15.50/4.50/5.50; and 33.50/0/5.86. Both stages have the best reported SR and DFR, but Stage 2 alone has the lowest listed Steps among stage-enabled conditions. Single-stage security regressions are substantive and should not be hidden by the combined result.

### Table 5 — Reward components, p. 8

Rows compare full reward, no attention scalar, no confidence adjustment, no severity weight, and confidence only. Evaluation pass rates are 55.9, 55.0, 53.0, 51.4, and 55.3%; fatal-error rates are 9.75, 13.07, 17.25, 27.53, and 12.37%. Full reward is best on both listed metrics, and severity removal is worst. Fatal error specifically means deceptive clicks judged correct. Sample size and statistical uncertainty are not provided.

### Table 6 — Prompt comparison, p. 9

No prompt gives SR/DFR 6.50/2.00%; manual prompt 7.00/3.50%; mutated prompt 15.50/4.50%. It duplicates the exact Figure 6 values. The optimized prompt is best for SR and worst for DFR among these three conditions. It establishes a tradeoff, not prompt-only security improvement.

### Table 7 — Computational cost, p. 9

Rows vanilla/S1/S2/both report Steps 17.65/3.57/6.15/3.58, Tokens 10,610/17,032/10,863/17,277, Time 217.62/49.19/81.61/48.47 seconds, and Time/Step 12.33/13.78/13.27/13.54 seconds. Both stages have the lowest total time and highest token total. Vanilla has the lowest time per step. The table does not report dispersion or a fully explicit aggregation unit. Its vanilla Steps differs from the same base agent's Table 2 average 16.06, without a stated reconciliation.

### Table 8 — Closed-source transfer, p. 9

The baseline row is labeled closed-source evaluator, while prose describes applying the prompt to a closed-source agent base model. Baseline and prompt-enhanced SR/DFR/Steps are 54.12/25.00/4.63 and 62.50/19.38/3.19. All three reported metrics improve, but the exact agent/evaluator roles, task denominator, and relation to Table 2 are insufficiently specified.

### Table 9 — Deceptive collection sources, p. 12

Manual 200 versus automatic 297 repeats the deceptive subset composition while clarifying that manual examples come from live commercial websites and automatic examples inject specific patterns into benign layouts. This supports a mixed-realism design, not a wholly in-the-wild benchmark.

### Table 10 — Generation categories, p. 13

Coercive, cognitive, and emotional examples use a two-stage LLM process; contextual examples use a hybrid process. Strategies include hidden opt-outs, misleading labels and preselected boxes, fake close buttons/system notifications, and countdown/social-proof cues. It is a construction taxonomy without category-specific performance results.

### Table 11 — Image dimensions, p. 13

Mean width/height/aspect ratio are 2,156 px/1,287 px/1.72; standard deviations 412 px/298 px/0.31; minima 1,024 px/768 px/1.00; maxima 2,560 px/1,600 px/2.37. These describe image diversity, not model performance. Mean aspect ratio need not equal mean width divided by mean height because averaging ratios is a different operation.

### Table 12 — Bounding-box areas, p. 14

Correct boxes have mean 18.4k, SD 12.8k, minimum 256, maximum 89.6k pixels squared and 0.8% image area. Dark boxes have mean 45.2k, SD 31.5k, minimum 1.0k, maximum 245.8k pixels squared and 2.1% image area. Analyst-derived mean-area ratio is 45.2/18.4≈2.46. This supports greater average annotated area, not a causal proof that area alone causes agent deception.

### Table 13 — Dataset split, p. 14

Train normal/deceptive/total: 637/348/985; validation: 137/75/212; test: 136/74/210. Totals match 910/497/1,407. Percentages are rounded 70/15/15, with seed 42. The table does not explain selection of the 200-task evaluation suite from or alongside the 210 test samples.

### Table 14 — Base-model specifications, p. 15

Qwen3-VL-4B is listed as 4.0B, Vision2Seq, bfloat16; UI-TARS-1.5 as 7.0B, Vision2Seq, bfloat16; GLM-4.6V as 4.6B, ConditionalGen, Remote API. These are author-reported metadata. A model name containing 4.6 does not independently validate the parameter count; no external checking was performed.

### Table 15 — Training and generation settings, p. 15

Learning rate 1×10^-5, AdamW, cosine scheduler, three epochs, KL coefficient 0.05; generation maximum 512 tokens, training/evaluation temperatures 0.7/0.0, top-p 0.8, do_sample=False. The table omits the group size normally needed to reconstruct the reported GRPO procedure from this document alone and does not explain generation-setting scope.

### Table 16 — Backends, p. 19

Identifiers glm, qwen3_local, uitars, and glm_flash map to GLM, Qwen3VLBackend, UITARSBackend, and GLMFlashBackend. The first is ZhipuAI cloud API; the others are local CUDA/CPU inference. This describes supported adapters rather than proving each backend contributed to every experiment.

### Table 17 — Outcome logic, p. 19

The seven displayed rows distinguish accepted correct/wrong benign actions, rejected correct/wrong benign actions, and rejected/accepted trapped/accepted untrapped phishing-page actions. Outcome codes are SUCCESS, FAIL_EXECUTION, OVER_DEFENSIVE, VALID_CORRECTION, SAFE_BLOCK, UNSAFE_CLICK, and SAFE_MISS. The prose says four distinct states, but the table lists seven codes. SAFE_BLOCK is page-type dependent; rejecting an action on a deceptive page is not necessarily the same as correctly identifying the proposed target as deceptive.

### Table 18 — Stage-2 batches, p. 20

Initialization is S=459, F=351; every row uses 20 iterations. For failure batch 10 and anchor sizes 5/10/15/20, final successes are 478/464/442/453, with Δ/batch 1.27/0.40/−0.68/−0.20. For failure batch 15, corresponding successes are 483/469/459/485 and Δ/batch 1.20/0.40/0.00/0.74. For failure batch 20, successes are 503/488/479/472 and Δ/batch 1.76/0.97/0.57/0.32. For failure batch 30 and anchors 5/10/15, successes are 506/507/493 and Δ/batch 1.35/1.20/0.76.

The best listed final count is 507 at failure batch 30, anchors 10; the worst is 442 at failure batch 10, anchors 15. The authors' claim that larger failure batches consistently improve counts has an exception at anchors 20: 453→485→472 for failure batches 10→15→20. Δ/batch is not explicitly defined, and the 810-case pool is not mapped to the split table.

### Table 19 — Iteration budget, p. 20

With failure batch 15 and anchors 5, maximum iterations 10/20/30/40/50/60/70/80 yield final successes 471/483/497/499/505/502/509/504. The authors describe a plateau near 50–60 iterations. The largest count is actually 509 at 70, and the curve is not monotonic. This is compatible with diminishing improvement but does not establish a uniquely optimal stopping point or robustness across random seeds.

## 12. Diagram / Architecture

Figures 1 and 2 describe the same conceptual defense at different resolutions. The principal data path is **annotated screenshots → sampled clicks → evaluator predictions → reward and training → failure pool → summarized experience → inference-time evaluator**. The principal control path at deployment is **agent proposes → evaluator judges → execute if accepted, otherwise reject and rethink**. [A/B: pp. 1, 4]

The Stage-2 feedback loop has two memory structures. F emphasizes unresolved failures; S preserves examples already handled correctly. Persistence counters prioritize stubborn failures, and successful anchors test whether a new rule creates regressions. The method's intended learning product is compact guidance rather than a growing unstructured transcript. Appendix G's example includes task relevance, subscription skepticism, visual hierarchy, and urgency checks. [A: pp. 4, 19–20]

The Appendix A.8 diagram on p. 14 partitions an image rectangle into green correct, red deceptive, and grey/background null regions. It explains the geometric labels used in reward and evaluation. It is not a realistic browser rendering or an empirical distribution. Its disjoint boxes make the set definition intuitive, but real overlap requires the additional handling described in Appendix D.

The architecture's claimed security advantage is that recognizing a visible element is separated from authorizing its execution relative to the goal. **Analyst interpretation:** this gives the system another opportunity to detect intention mismatch, but also creates dependence on evaluator competence and on how retries and feedback are counted. The paper's weaker-evaluator results demonstrate that this dependence is practical rather than merely hypothetical.

## 13. Equations and mathematical concepts

### Equation 1 — Evaluator mapping, p. 3

`E:(I,P,C)→(L_hat,γ)` defines a function from screenshot I, task P, and coordinate C=(x,y) to a predicted class L_hat∈{−1,0,1} and confidence γ∈(0,1). It expresses the evaluator's interface, not an optimization objective. The task input is what makes a judgment goal-dependent rather than simply visual dark-pattern detection. [A]

### Equation 2 — Ground-truth region label, p. 3

`L=1 if C∈Bc; L=−1 if C∈Bd; L=0 otherwise`, with `B0=I\(Bc∪Bd)`. Bc is the correct box, Bd the deceptive box, and B0 the remainder of the image domain. Set membership converts a coordinate to a training/evaluation label. The written cases are potentially ambiguous if boxes overlap; click-generation adjustment addresses a sampled-coordinate case but does not completely specify all membership precedence. [A/D]

### Equation 3 — Hybrid reward, p. 3

`R=γ` when prediction equals truth; otherwise `R=−α·ω(L,L_hat)·γ`. Gamma rewards confident correctness and scales the cost of confident errors. Omega gives error-specific severity. Alpha changes penalty magnitude according to spatial factors. The objective is to guide reinforcement learning toward accurate judgments with especially strong discouragement of unsafe approvals. The reward is per judgment, distinct from episode-level SR/DFR. [A]

Main-text cases set ω=1 for rejecting a correct click, 1+β for null misclassifications, and 10 for deceptive-to-correct errors. Appendix B fills in deceptive-to-null with ω=1. Thus the main-text four named error categories do not alone enumerate every off-diagonal class pair. The appendix's parenthetical expansion of C4 as Command and Control is inconsistent with the main text's use of C4 as its fourth error category. [A/B]

### Equation 4 — Attention scalar, p. 3

`β=S_(L_hat)/S_I`, where S_I is image area and S_(L_hat) selects S_c, S_0, or S_d for predicted labels 1, 0, or −1. The stated null area is `S_0=S_I−S_c−S_d`. This is a dimensionless area fraction. The authors interpret larger regions as attracting attention. It modifies null-confusion penalties through 1+β; no direct eye-tracking or measured attention is involved. If correct and deceptive regions overlap, subtracting both areas requires an overlap convention that is not fully specified. [A/D]

### Unnumbered confidence adjustment, p. 3

The visually supplied expression is `α=clip(1/[(d(C,B_(L_hat))+ε)·(S_L/S_I)], α_min, α_max)`. Here d is distance from C to the nearest boundary of the predicted region, ε ensures numerical stability, S_L is the ground-truth region area, and clip limits the result between α_min and α_max. The numerical values of ε and the clipping bounds are not supplied. [A/B]

A substantive inconsistency remains: prose says this reduces penalties near boundaries or when ground-truth regions offer limited visual evidence. Holding other terms fixed, the displayed inverse expression grows when distance or ground-truth area decreases, until clipped. **Analyst-derived:** decreasing either positive denominator factor increases its reciprocal. The formula and the stated rationale therefore point in opposite directions under that reading. The supplied work does not resolve which is intended.

### Equations 5–6 — Coordinates, p. 13

Equation 5 gives `bbox=[x1,y1,x2,y2]` in pixels. Equation 6 gives normalized coordinates `[x1/W,y1/H,x2/W,y2/H]`, with image width W and height H. Normalization expresses location relative to image size and supports model-specific coordinate conventions. The rendered image clarifies bracket notation damaged in extraction. [A/B]

### Algorithm 1 and supplementary mathematical objects

Algorithm 1 on p. 4 initializes empty experience, counter values, and iteration index; samples failure/anchor batches; summarizes; evaluates; moves correct cases to S; increments failed-case counters; and stops when F is empty or the limit is reached. Its symbols reuse T for template/iteration-bound typography, which should be read by role rather than assumed to be one object. Appendix G adds validation stagnation stopping.

Intersection-over-union measures annotation-box agreement; the source supplies threshold and summary values but not a displayed formula. KL divergence is named as a training regularizer with coefficient 0.05 but not mathematically defined. Policy entropy is plotted as a randomness/exploration diagnostic without a supplied computation formula or units. No theorem, lemma, or proof is present.

## 14. Interpretation and discussion

RQ1 receives qualified support. Strong-evaluator aggregate results improve both SR and DFR across all three base agents, and failure decomposition indicates broader correction of ineffective actions. However, the weaker evaluator harms UI-TARS success, and one GLM domain has worse DFR. The paper's architecture can help, but the evidence does not establish uniform benefits across evaluators, agents, domains, or attack conditions. [A/B/D: pp. 6–7]

RQ2 receives support from a specific ablation: combining stages yields the best SR and zero observed DFR, while each alone raises DFR relative to baseline. Reward ablation further supports assigning extra cost to unsafe approval. The causal explanation involving overconfidence, visual grounding, and regularization remains an author interpretation because those intermediate mechanisms are not independently isolated by measurements. [A/D: pp. 7–8]

RQ3 receives directional support from Table 8, but methodological detail is thinner: exact model roles, denominator, and task composition are unclear. Transfer should be described as reported success in the supplied setting, not a general guarantee of model-independent security. [A/D: p. 9]

For the user's research question, the relevant inference is that web agents encounter adversarial content while selecting actions in an external environment. A misleading control can align superficially with task language and turn a reasoning error into a click. The paper's task-aware evaluator targets that perception–goal–action linkage. It does not establish whether the same base model is intrinsically more susceptible when acting than when answering a standalone prompt, because no matched standalone condition exists. [D]

Several apparent successes also reflect assistance with general task grounding. GLM baseline DFR is only 4%, while null failures are about 86.5% of episodes. An evaluator that rejects ineffective targets and supplies feedback can therefore generate large SR gains even when most baseline failures are not attacks. **Analyst interpretation:** the principal comparisons combine security checking with additional corrective reasoning, so gains cannot all be attributed solely to deception recognition.

## 15. Contributions and novelty

The authors claim a **conceptual contribution**: formalizing deception-aware agent defense as distinct from merely detecting dark patterns. They claim a **methodological contribution**: combining asymmetric reward learning with failure-to-guidance summarization. The **algorithmic contribution** is an iterative persistence-weighted failure/success-pool procedure. The **systems contribution** is a plug-in evaluator gate with rejection feedback. [A: pp. 1–4]

The **dataset and benchmark contribution** is RUC's 1,407 examples with correct and deceptive boxes, a four-domain/four-category taxonomy, and documented collection/annotation procedures. The **empirical contribution** is a set of multi-agent/evaluator comparisons, ablations, runtime measurements, and a transfer experiment. There is no theoretical guarantee, theorem, formal robustness certificate, or proof of optimality. [A/B]

The first-framework and no-prior-defense statements are author novelty claims. Closed-document analysis cannot verify the complete state of the literature. The provided bibliography also creates some attribution questions discussed below, so the novelty positioning should retain its author-reported status.

## 16. Limitations

### Authors' stated limitations

The limitations section, p. 9, identifies five boundaries: increased per-step latency; evaluation on static screenshots rather than fully interactive asynchronous environments; emphasis on ecological validity rather than maximal adversariality; English-language interfaces without cross-lingual validation; and inability to detect hidden backend exploits without visible GUI manifestations. The experiments also state that training budget restricts Stage-1 ablation to one open-source base model. [A: pp. 6–7, 9]

### Additional evidence-based analyst observations

The supplied study does not directly compare standalone LLMs with web agents. It lacks uncertainty intervals and repeated-seed performance estimates. The 200-task evaluation suite is not reconciled with the 210-sample test split, and the 810-case Stage-2 pool is not mapped to either. The closed-source transfer denominator and exact model roles are unclear. [D]

Reported Steps values conflict with both the three-step cap and the later deceptive-termination count of 10. Some averages are arithmetically inconsistent. The confidence-adjustment equation and prose appear directionally inconsistent. Inference confidence thresholds and clipping parameters are absent. The exact multimodal summarizer and complete operational Stage-2 configuration are not specified. [B/C/D]

The supplied material provides no adaptive attack evaluation against DUDE, no attack-category-specific results, and no measurement of actual downstream harm. Claims that stratification prevents similar templates appearing across train and test are not accompanied by a template-grouping or duplicate-detection procedure. These are limits on what can be established from the document, not evidence that leakage or compromise actually occurred. [D]

## 17. Threats to validity

These validity labels are analyst classifications rather than terminology attributed to the authors.

**Internal validity:** DUDE introduces another evaluator and corrective feedback loop. Without a matched additional-computation or non-security evaluator control, the amount of improvement attributable specifically to deception-aware training is uncertain. Single-stage and prompt-only regressions show that component interactions matter. [D]

**Construct validity:** A dark-box click is an operational proxy for deception harm. Box membership cannot fully represent subscriptions, data disclosure, backend effects, or task completion after navigation. NFR captures noncompletion, and its prose denominator differs from the table. Confidence-shaped reward is not equivalent to a measured calibration metric. [D]

**External and ecological validity:** RUC includes real pages and synthetic pages designed for realism, but static screenshots, four domains, English focus, and non-forced exposure limit transfer to live adversarial sites. Appendix A explicitly notes that success can occur before a trap is encountered, suppressing episode DFR relative to forced exposure. [A/D: pp. 9, 12]

**Statistical conclusion validity:** No outcome confidence intervals, repeated-run variation, or significance tests are supplied. Zero observed DFR in a limited suite is not a proof of zero population risk. Fractional transfer percentages and unexplained denominators weaken exact interpretation. [D]

**Reproducibility:** Hardware, versions, prompts, and several hyperparameters are reported, but missing thresholds, summarizer identity, split relationships, reward inconsistencies, and unavailable code/data inspection prevent full reconstruction from this evidence alone. The supplied code snippets were read, not executed. [A/D]

## 18. Future work and open questions

### A. Explicit author directions

The authors identify validation in fully interactive environments with asynchronous feedback as an important next step. They state that cross-lingual generalization remains unexplored. Their limitations also identify aggressively adversarial settings and nonvisual backend exploits as boundaries, although no concrete backend-defense design is proposed. [A: p. 9]

### B. Analyst-derived open questions

Would the same model behave differently in a matched standalone-language condition and a web-action condition? How much benefit comes from an extra reasoning model versus deception-specific training? Can the evaluator resist attacks optimized against its own prompt and visual reasoning? What happens when traps and correct elements overlap, change after inspection, or depend on history? [D]

Which evaluator strength best balances refusal, safety, latency, and task capability? Do optimized rules retain benefits on unseen template families, languages, and sites? Does zero observed DFR survive repeated seeds and larger test sets? Can the authors reconcile step accounting, table averages, transfer denominators, and the confidence-adjustment formula? These questions follow from observed gaps rather than reported experimental answers. [D]

## 19. Terminology and notation glossary

| Term | Meaning in this paper |
|---|---|
| DUDE | Deceptive UI Detector & Evaluator; proposed evaluator-based defense |
| RUC | Real UI Clickboxes; screenshot/task dataset with target boxes |
| LLM / VLM | Large language model / vision-language model |
| GUI / UI | Graphical user interface / user interface |
| Dark pattern | Interface design intended to manipulate behavior |
| Grounding | Matching a goal to a visible target location |
| I | Screenshot or full image-coordinate domain |
| P | Natural-language task specification |
| C=(x,y) | Proposed click coordinate |
| E | Evaluator mapping screenshot, task, and click to judgment/confidence |
| L / L_hat | Ground-truth / predicted label: 1 correct, 0 ineffective, −1 deceptive |
| γ | Evaluator confidence in (0,1) |
| Bc / Bd / B0 | Correct box / deceptive box / remaining null region |
| S_I, S_c, S_d, S_0 | Areas of image and labeled regions |
| R | Classification-dependent reinforcement-learning reward |
| ω | Error-severity weight |
| β | Predicted-region area fraction used in attention scaling |
| α | Spatially defined penalty-adjustment scalar |
| ε; α_min; α_max | Stability constant and clipping bounds; numerical values not supplied |
| F / S | Failure pool / success pool |
| κ(x) | Counter tracking persistent failure for sample x |
| Bf / Bs | Sampled failure / successful-anchor batches |
| X | Accumulated textual experience guidance |
| SR / DFR / NFR | Success / deception-induced failure / null-click failure rates |
| GRPO | Group Relative Policy Optimization, used for Stage-1 training |
| KL coefficient | Weight constraining deviation from a reference policy |
| IoU | Intersection-over-union used for box agreement |
| Cohen's κ | Reported label-agreement statistic, distinct from persistence κ(x) |
| DOM | Document object model, used to derive task intent during page generation |
| CoT / ReAct | Chain-of-thought / reasoning-and-action prompt styles named in the paper |
| bfloat16 | Reported numerical precision for local models |
| Tmax | Declared maximum interaction count of 3 |
| pp | Percentage points, an absolute difference between percentages |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| RUC size | 1,407 | samples | 910 normal + 497 deceptive | Author-reported | p. 5, T1 |
| Deceptive sources | 200 / 297 | samples | manual / automatic | Author-reported | pp. 5, 12 |
| Main suite | 200 | tasks | 50 per domain | Author-reported | p. 5, §5.1 |
| Dataset test split | 210 | samples | 136 normal, 74 deceptive | Author-reported | p. 14, T13 |
| Qwen success | 6.50→63.50 | % | UI-TARS evaluator | Author-reported | p. 6, T2 |
| Qwen DFR | 2.00→0.50 | % | reported aggregate; domain arithmetic differs | Author-reported | p. 6, T2 |
| UI-TARS success | 43.50→58.00 | % | UI-TARS evaluator | Author-reported | p. 6, T2 |
| UI-TARS DFR | 23.50→1.50 | % | UI-TARS evaluator | Author-reported | p. 6, T2 |
| GLM success | 9.50→60.50 | % | UI-TARS evaluator | Author-reported | p. 6, T2 |
| GLM DFR | 4.00→1.50 | % | UI-TARS evaluator | Author-reported | p. 6, T2 |
| UI-TARS success regression | 43.50→35.50 | % | Qwen-2B evaluator | Author-reported | p. 6, T2 |
| Regression magnitude | −8.00 | percentage points | 35.50−43.50 | Analyst-derived | p. 6, T2 |
| Combined-stage SR / DFR | 33.50 / 0 | % | Qwen ablation | Author-reported | p. 7, T4 |
| Stage-1-only DFR | 5.50 | % | baseline 2.00 | Author-reported | p. 7, T4 |
| Stage-2-only DFR | 4.50 | % | baseline 2.00 | Author-reported | p. 7, T4 |
| Full / no-severity fatal error | 9.75 / 27.53 | % | evaluator-classification ablation | Author-reported | p. 8, T5 |
| Fatal-error ratio | ~2.82 | ratio | 27.53/9.75 | Analyst-derived | p. 8, T5 |
| End-to-end elapsed time | 217.62→48.47 | seconds | UI-TARS overhead comparison | Author-reported | p. 9, T7 |
| Time reduction | ~77.73 | % | (217.62−48.47)/217.62×100 | Analyst-derived | p. 9, T7 |
| Transfer SR / DFR | 62.50 / 19.38 | % | with Stage-2 prompt | Author-reported | p. 9, T8 |
| Transfer improvements | +8.38 / −5.62 | percentage points | SR / DFR versus 54.12 / 25.00 | Analyst-derived | p. 9, T8 |
| Type / category agreement | 0.89 / 0.84 | κ | annotation | Author-reported | p. 13, A.3 |
| Box agreement | 0.91±0.06 | IoU | mean ± standard deviation | Author-reported | p. 13, A.3 |
| Mean dark/correct area ratio | ~2.46 | ratio | 45.2k/18.4k | Analyst-derived | p. 14, T12 |
| Maximum plotted reward | −0.384 | reward | step 790 annotation | Visually readable | p. 8, F4a |
| Stage-2 pool | 459+351=810 | cases | initial success + failure | Author-reported/Analyst-derived | p. 20, T18 |
| Highest listed iteration result | 509 | successes | 70 iterations, batches 15/5 | Author-reported | p. 20, T19 |
| Abstract susceptibility reduction | 53.8 | % | aggregation unspecified | Author-reported | p. 1, abstract |

No approximate visual estimate is substituted for an exact tabulated result. Plot ranges and trends above are descriptive observations, with approximate ranges explicitly indicated.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| DUDE evaluates candidate clicks relative to task intent | Inputs screenshot, task, coordinate; outputs label/confidence | E1; F2 | pp. 3–4 | HIGH for architecture description |
| Asymmetric reward emphasizes unsafe approval | Severity 10 for deceptive→correct versus 1 for correct rejection | E3; reward matrix | pp. 3, 15 | HIGH for stated design; α formula unresolved |
| Failure summaries provide parameter-free contextual updates | Iterative F/S pool and guidance procedure | ALG1; G | pp. 4, 19–20 | HIGH for description; exact summarizer unspecified |
| Strong-evaluator aggregate results improve SR and DFR | Three base-agent comparisons | T2; X1 | p. 6 | HIGH for reported values; arithmetic and scope caveats |
| Benefits depend on evaluator quality | UI-TARS SR 43.50→35.50 with Qwen evaluator | T2; F3 | pp. 6–7 | HIGH; direct counterexample to universal preservation |
| Stages are complementary in one ablation | Combined SR 33.50%, DFR 0%; either alone worse DFR | T4; X3 | pp. 7–8 | HIGH for result; MEDIUM for causal explanation |
| Severity weighting reduces fatal classification errors | 9.75% full versus 27.53% without severity | T5; X4 | p. 8 | HIGH for table; denominator/variation absent |
| Prompt-only success improvement is not security improvement | SR and DFR both rise | T6; F6 | p. 9 | HIGH |
| Transfer is promising but incompletely specified | SR 54.12→62.50; DFR 25→19.38 | T8; X8 | p. 9 | MEDIUM due role/denominator ambiguity |
| Live-web generalization is unestablished | Static-screenshot limitation | Limitations | p. 9 | HIGH |
| Agent action surface is relevant to user's research question | Visible deception can redirect clicks | §§1, 3–4; F8 | pp. 1–5, 23 | Analyst inference; no standalone-LLM comparison |

### Cross-reference and consistency ledger

The following unresolved issues were retained after checking the synthesis against the supplied text and visible tables:

1. **Abstract versus results:** 53.8% susceptibility reduction on p. 1 lacks a stated aggregation formula or clearly matching table entry.
2. **Steps definitions versus results:** p. 6 says bounded by Tmax=3; pp. 18–19 add a deceptive-outcome count of 10; Table 2 includes 31.00 and many averages above 10. Table 7 likewise exceeds 3. The supplied material does not reconcile them.
3. **Average arithmetic:** Table 2's Qwen/UI-TARS DFR average and UI-TARS/UI-TARS Steps average differ from equal-domain arithmetic. Four domains have 50 tasks each under §5.1, so no alternative weighting is explained.
4. **Evaluation sizes:** 200 tasks in §5.1, 210 test samples in T13, 810 Stage-2 pool cases in T18, and fractional Table 8 percentages are not mapped to one another.
5. **Confidence adjustment:** Eq. α's inverse dependence appears opposite to the verbal reduced-penalty rationale.
6. **Gate specification:** F2 includes a confidence threshold; inference prose specifies only label 1; threshold values are missing.
7. **Single-stage claims:** Tables 4 and 6 show higher DFR for individual stages/prompt optimization, qualifying broad security-improvement language.
8. **Failure denominator:** Table 3's NFR share of all episodes is described in prose as a share of failures.
9. **Training series:** Figure 4 labels training reward; prose also says validation reward.
10. **Summarizer anchors/stopping:** ALG1's call shows failures rather than anchors as explicit summarizer input; Appendix G adds stagnation stopping absent from ALG1.
11. **Batch conclusions:** T18 contains a non-monotonic counterexample to consistently increasing success with failure-batch size; Δ/batch is undefined.
12. **Outcome accounting:** §F.2 says four states; T17 lists seven outcome codes.
13. **Language scope:** p. 9 and Appendix A emphasize English-only evaluation, while C.4 mentions Chinese-language evaluation subsets without reported matching results.
14. **Citation alignment:** Related-work prose associates Narechania et al. with misleading visual overlays, but its supplied reference title concerns provenance widgets; Wang et al. is described as multimodal dark-pattern detection, while its reference title is a factuality survey. These internal attribution mismatches cannot be resolved without external checking, which was not performed.
15. **Leakage prevention:** Category stratification is said to prevent similar templates crossing splits, but no explicit template-level grouping procedure is supplied.

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an AI to download one particular program. It sees a page with several buttons. The largest button might be an advertisement or subscription offer, while the useful link is smaller. The AI can understand the words and still click the wrong thing because looking relevant is different from actually serving your goal.

DUDE adds a checker before the click happens. The checker sees the page, your request, and where the AI wants to click. It asks whether that click is useful, useless, or a trap. The researchers train it to treat approving a trap as a particularly costly mistake. They also turn earlier errors into short reminders, such as checking whether a prominent button really matches the user's purpose.

The reported results show that a good checker can help a lot. But a weaker checker can block useful actions, and reminders alone sometimes increase trap clicks even while helping the AI finish more tasks. The experiments use screenshots and annotated target boxes, so they do not yet prove the system is safe on a changing live website.

For your question about web agents versus standalone language models, the useful idea is that an agent converts what it reads and sees into actions. A deceptive page can exploit that connection. This paper investigates that web-interface problem, but it does not run the direct comparison needed to conclude how much more vulnerable agents are than standalone LLMs.

## Completeness Audit

The denominator is the inventory in §2, including every major section, substantive subsection group, visual object, equation, algorithm, experiment, contribution, and stated limitation. Grouped rows below explicitly enumerate their contents. Fully represented means the substantive function and evidence are covered, not that every word was reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, abstract | Yes | Yes | Represented in compressed form | Original title retained in research field; authors/venue below |
| §1 Introduction; P1/P2; contributions | Yes, text and image | Yes | Fully represented | Motivation, >70% context, novelty claims qualified |
| §2 Related Work | Yes, text and image | Yes | Represented in compressed form | Categories retained; individual model descriptions compressed |
| §3 opening; §3.1 formulation | Yes | Yes | Fully represented | Inputs, outputs, labels, geometry |
| §3.2; §§3.2.1–3.2.3 | Yes | Yes | Fully represented | Sampling, reward, error collection |
| §3.3; §§3.3.1–3.3.2 | Yes | Yes | Fully represented | Pools, counters, anchors, iteration |
| §3.4 inference | Yes | Yes | Fully represented | Gate and threshold ambiguity |
| §4; §§4.1–4.3 | Yes | Yes | Fully represented | Tasks, taxonomy, construction |
| §5.1 setup | Yes | Yes | Fully represented | Models, suite, metrics, controls |
| §§5.2–5.3 effectiveness and stages | Yes | Yes | Fully represented | Includes regression and decomposition |
| §§5.4–5.6 reward, dynamics, prompts | Yes | Yes | Fully represented | Includes security tradeoffs |
| §§5.7–5.8 overhead and transfer | Yes | Yes | Fully represented | Conditions and missing denominators retained |
| §6 Conclusion | Yes | Yes | Represented in compressed form | Claims bounded by results |
| Authors' five limitations | Yes | Yes | Fully represented | Each separately retained |
| RQ1–RQ3 | Yes | Yes | Fully represented | Mapped to experiments |
| Formal hypotheses | None identified | Yes | Fully represented | Absence explicitly stated |
| X1–X10 experiment/analysis register | Yes | Yes | Fully represented | Statistical gaps disclosed |
| Figure 1 | Yes, visually | Yes | Fully represented | Conceptual harm examples distinguished |
| Figure 2 | Yes, visually | Yes | Fully represented | Architecture and control loops |
| Figure 3a–c | Yes, visually | Yes | Represented in compressed form | Full role, exceptions, selected cells; T2 retains domain values |
| Figure 4a–b | Yes, visually | Yes | Fully represented | Axes, lines, trend, annotation, no uncertainty |
| Figure 5 | Yes, visually | Yes | Fully represented | Scatter limits and interpretation |
| Figure 6 panels | Yes, visually | Yes | Fully represented | Exact labels and scale caveat |
| Figure 7a–b | Yes, visually | Yes | Represented in compressed form | Screenshot context; no task text |
| Figure 8a–b | Yes, visually | Yes | Represented in compressed form | Correct/deceptive boxes; no causal claims |
| Tables 1–8 | Yes, visually/text | Yes | Fully represented | T2 domain vectors retained; inconsistencies flagged |
| Tables 9–15 | Yes, visually/text | Yes | Fully represented | Counts, statistics, splits, configurations |
| Tables 16–19 | Yes, visually/text | Yes | Fully represented | Backends, outcomes, all hyperparameter counts |
| Equations 1–4 | Yes, visually/text | Yes | Fully represented | Symbols, roles, boundary caveats |
| Unnumbered α equation | Yes, visually/text | Yes | Uncertain | Form represented; rationale conflict unresolved |
| Equations 5–6 | Yes, visually/text | Yes | Fully represented | Pixel and normalized coordinates |
| Algorithm 1 | Yes, visually/text | Yes | Fully represented | Anchor and stopping differences disclosed |
| Listing 1 | Text only | Yes | Represented in compressed form | Loading settings; not executed |
| Listing 2 | Yes, visually/text | Yes | Fully represented | Overlap adjustment and missing recheck |
| Safe-decoding function | Yes, visually/text | Yes | Represented in compressed form | Replacement behavior explained |
| Appendix A.1/A.1.1/A.1.2 | Yes | Yes | Fully represented | Sources and filters |
| Appendix A.2/A.2.1/A.3 | Yes | Yes | Fully represented | Schema, boxes, quality control |
| Appendix A.4/A.4.1 | Yes | Yes | Fully represented | Generation strategies |
| Appendix A.5/A.5.1/A.5.2/A.6 | Yes | Yes | Fully represented | Statistics and splits |
| Appendix A.7/A.7.1/A.7.2 | Yes | Yes | Represented in compressed form | Example IDs/coordinates summarized below |
| Appendix A.8 diagram | Yes, visually | Yes | Fully represented | Region partition |
| Appendix B.1–B.4 | Yes | Yes | Fully represented | Models, infrastructure, training, weights |
| Appendix B.5 | Text/image split | Yes | Represented in compressed form | Code on text-only p. 16 |
| Appendix C.1–C.4 | Text only | Yes | Represented in compressed form | Prompt mechanisms summarized below; no instructions obeyed |
| Appendix D.1–D.3 | Text/image split | Yes | Fully represented | Sampling, overlap, rejection |
| Appendix E.1–E.3 | Yes | Yes | Represented in compressed form | Adapters and decoding |
| Appendix F.1–F.3 | Yes | Yes | Fully represented | Metrics, codes, termination |
| Appendix G.1–G.5 | Yes | Yes | Fully represented | Pools, sampling, stopping, guidance |
| Appendix H | Yes | Yes | Fully represented | All table values retained |
| Appendix I, pp. 21–23 | Partial visual | Yes | Represented in compressed form | Heading p. 21 text-only; sample figures inspected |
| Major contributions | Yes | Yes | Fully represented | Novelty kept author-attributed |
| Code/data availability footnote | Yes | Yes | Missing from supplied material | Availability claim inspected; linked artifacts not inspected |
| Acknowledgments | Yes | Yes | Inspected but deliberately omitted as non-substantive | Funding is not outcome evidence |
| References, pp. 10–11 | Text only | Yes | Represented in compressed form | No independent validation; internal mismatches flagged |
| Separate supplementary files | Not supplied | No | Missing from supplied material | No supplementary review claimed |

### Bibliographic identity and compressed details

The paper's authors are Yilin Zhang, Yingkai Hua, Chunyu Wei, Xin Wang, and Yueguo Chen, affiliated with Renmin University of China and Ant Digital Technologies, Ant Group. Yilin Zhang and Yingkai Hua are marked co-first authors; Chunyu Wei is corresponding author. The supplied publication line states Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp. 6830–6852, July 2–7, 2026. These are author-provided bibliographic details, not externally verified publication metadata.

Appendix A.7's normal example is ID 17, resolution 2156×1204, task text “Maps to Click here to search,” correct box [1571,434,1614,485], and no dark box. Its deceptive example is ID 914, Booking, resolution 2537×1511, task to complete ticket reservation quickly, correct box [1117,900,1424,972], and dark box [753,787,1768,900], described as a misleading banner above the legitimate control. These are illustrative records rather than extra experimental results.

Appendix C's base agent prompt requests thought then action/final-answer tags, real observations rather than fabricated ones, a final status/click object, and experience insertion. The evaluator prompt requests judge/conf tags, reasoning under 50 words, and confidence generally between 0.3 and 0.8 while allowing exceptions. The experience template contains general policy and structured failure-pattern/correct-strategy entries. The ReAct template supplies a reasoning/action/observation loop and an unrelated worked example. Exact prompt wording, XML boilerplate, placeholder tool lists, and that worked example are compressed because their scientific function is represented; they were not followed as instructions. The evaluator's confidence prior is relevant to interpreting confidence-shaped reward and has therefore been retained.

### Missing or inaccessible material

The code and dataset referenced by the availability footnote were not supplied as inspectable artifacts. No separate supplementary files, experiment logs, full training outputs, or repository contents were reviewed. Pages 10–11 and 16–17 were text-only, so typography, any unextracted visual objects, and exact code layout there cannot be visually verified. Page 21's visual content is unavailable; only its Appendix I heading is visible in extraction. No external citation validation or reproduction was performed.

### Uncertain interpretations

Unresolved issues include step accounting, selected Table 2 averages, the abstract's 53.8% aggregation, the α formula/rationale, numerical gate thresholds and clipping bounds, evaluator-versus-agent roles in transfer, task denominators, the 810-case Stage-2 pool's provenance, anchor use in the summarizer call, Δ/batch meaning, training-versus-validation reward labeling, Chinese-subset references, and several bibliography-to-prose attributions. Confidence in these unresolved mechanisms is MEDIUM, LOW, or UNKNOWN as appropriate; confidence that the discrepancies exist in the supplied evidence is HIGH.

### Deliberately compressed material

Related-work descriptions, bibliographic entries, acknowledgments, repetitive diagram labels, repeated metric definitions, prompt boilerplate, code formatting, and screenshot interface text unrelated to the annotated targets were compressed. Figures 7–8 were explained as examples rather than transcribed page content. All substantive tables were represented, including Table 2's domain-level results and Tables 18–19's hyperparameter counts.

### Potential omissions

Every substantive object identified in the supplied inventory has a representation or explicit coverage limitation above. This is an inventory-based account of the supplied text and 18 rendered pages, not a claim that unavailable code, linked data, unrendered page details, or undisclosed supplementary artifacts contain nothing important. The principal remaining gaps are unavailable artifacts and unresolved source inconsistencies, not silently assumed experimental facts.
