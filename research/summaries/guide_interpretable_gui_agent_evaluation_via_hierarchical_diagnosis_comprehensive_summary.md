## Stage 0 — Document Accessibility Report

This analysis uses only the supplied document text and eight supplied page images. No tools, browsing, external literature, or workspace material were used. Document content is treated as evidence, never as instructions. Physical PDF page numbers, rather than manuscript running headers, are used throughout.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied text for physical pages 1–9 |
| Accessible page count | 9 |
| Visually inspected pages | 1–8, from the supplied page images |
| Text-only coverage | Page 9, containing references 12–29 |
| Apparently missing main-text pages | None apparent between the supplied numbered pages; this does not establish that the original source contains no additional material |
| Visual content | All three substantive figures are available visually; Tables 1–6 are also visible |
| Tables readable | Yes, using the supplied images and extracted text together |
| Equations readable | Equations 1–4 are identifiable; extracted mathematical spacing and indexing are imperfect, so interpretation is checked against the rendered pages |
| Appendices | No appendix is supplied |
| Supplementary material | None supplied; no embedded supplementary files are indicated in the accessibility metadata |
| Referenced but absent material | Section 4.5 explicitly says the segmentation-quality evaluation prompt is provided in an Appendix; that Appendix is absent |
| OCR needed | No additional OCR was performed or necessary for the main text; visual inspection was necessary for corrupted figure text |
| Extraction limitations | Figure 2 has garbled extracted labels; Figure 3 has encoded glyph strings instead of readable plot labels |
| Other limitations | Tiny illustrative interface text in Figure 2 is not all confidently readable; page 9 has no supplied rendering |

The prompt includes an image-loading error for a path represented as '-'. It does not prevent inspection of the eight images actually displayed. The supplied source hash is preserved as an identifier; it was not independently recomputed.

Evidence categories used below are: **[A] Author-reported**, **[B] Directly observable**, **[C] Analyst-derived**, and **[D] Analyst interpretation**. No **[E] External information** is introduced. Confidence describes how confidently the supplied evidence supports a statement, not whether the authors' scientific conclusions have been independently established.

### Working inventory and extraction ledger

The work is an empirical artificial-intelligence evaluation-method paper with an algorithmic/system architecture, three benchmark evaluations, ablations, and a segmentation-quality study. It is not a security experiment, a standalone-language-model comparison, a formal theoretical paper, or a systematic review.

| ID | Original object | Physical pages | Extracted role |
|---|---|---|---|
| META | Title, authors, affiliations, arXiv identifier | 1 | Document identity |
| ABS | Abstract | 1 | Problem, three-stage method, benchmark overview |
| S1 | 1 Introduction | 1–2 | Motivation, gap, four contribution bullets |
| S2.1 | 2.1 GUI Agents | 2 | Agent and benchmark context |
| S2.2 | 2.2 GUI Agent Evaluation | 2–3 | Evaluation categories and GUIDE positioning |
| S2.3 | 2.3 Hierarchical Decomposition in LLM Agent Systems | 3–4 | Planning, reasoning, memory, error recovery |
| S3.1 | 3.1 Problem Formulation | 4 | Trajectories and evaluation function |
| S3.2 | 3.2 Module 1: Trajectory Segmentation | 4–5 | Boundaries, subtask descriptions, text-only segmentation |
| S3.3 | 3.3 Module 2: Subtask Diagnosis | 5 | Multimodal diagnostic triples |
| S3.4 | 3.4 Module 3: Overall Summary | 5 | Learned aggregation and design rationale |
| S4.1 | 4.1 Experimental Setup | 5–6 | Datasets, baselines, metrics, implementation |
| S4.2 | 4.2 Main Results | 6–7 | Three benchmark comparisons |
| S4.3 | 4.3 Long-Trajectory Analysis | 7 | Length-group accuracy |
| S4.4 | 4.4 Ablation Study | 7 | Four modified configurations versus full GUIDE |
| S4.5 | 4.5 Segmentation Quality Validation | 7–8 | Quality scoring and human agreement |
| S4.6 | 4.6 Discussion | 8 | Domain-knowledge failures and proposed adaptation |
| S5 | 5 Conclusion | 8 | Main synthesis |
| REF | References 1–29 | 8–9 | Bibliographic context, not independently inspected cited works |
| F1 | Figure 1, four panels | 2 | Comparison of evaluator input and processing paradigms |
| F2 | Figure 2, three stages | 3 | GUIDE architecture and illustrative wrong-user failure |
| F3 | Figure 3, three panels | 4 | Industrial dataset length, outcome, and success distributions |
| T1–T6 | Tables 1–6 | 5–8 | All quantitative comparisons and validation distributions |
| E1–E4 | Equations 1–4 | 4–5 | Trajectory, decomposition, segment, diagnosis definitions |
| X1–X3 | Main industrial, web, and mobile evaluations | 5–7 | Evaluator performance against trajectory labels |
| X4 | Long-trajectory analysis | 7 | Association between trajectory length and accuracy |
| X5 | Ablation analysis | 7 | Contribution of segmentation, diagnosis, and summarization |
| X6 | Segmentation-quality analysis | 8 | Automated segment usability with a human spot-check |
| APP-MISSING | Referenced Appendix prompt | 8 reference | Missing from supplied material |

There are no numbered algorithms, pseudocode blocks, formal theorems, lemmas, or propositions. There are no explicitly numbered research questions or formal statistical hypotheses. The substantive footnote is the equal-contribution marker for the first two authors. Publication boilerplate, repeated running headers, and decorative robot characters are accounted for but do not supply experimental evidence.

## 1. Plain-language orientation

**[A]** GUIDE evaluates whether a software-controlling artificial-intelligence agent actually accomplished its assigned task. A graphical user interface, or GUI, is the visible interface containing pages, buttons, fields, menus, and other controls. An agent can inspect screenshots and then click, type, scroll, or navigate. Its trajectory is the record of these observations and actions.

The paper addresses a problem with evaluating long trajectories. Giving a language-model evaluator the entire history in one large request can overload its context, and returning only success or failure does little to explain a mistake. The authors propose splitting the completed history into meaningful subtasks, diagnosing each subtask with its screenshots, and combining the diagnoses into an overall decision. This is retrospective evaluation: GUIDE examines an already executed trajectory rather than planning the agent's future actions.

**[A]** The principal results are 95.80% evaluator accuracy on 932 industrial e-commerce trajectories; 89.21% precision on 1,302 web-agent trajectories from AGENTREWARDBENCH; and 94.9 ± 0.3% mean accuracy on 480 AndroidBench trajectories over three independent evaluation runs. These are measurements of the evaluator's judgments against labels, not the agents' own task-success rates. The central contribution is a three-stage, training-free evaluation architecture that combines task judgments with localized error explanations and corrective recommendations. [pp. 1–2, 5–8]

**[D] Research relevance.** For the user's question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis,' this work offers indirect evidence about evaluating agents that act through long sequences of changing interface states. It does not establish a security vulnerability comparison. No attack experiment, malicious-content condition, attacker capability model, or standalone large language model control group is supplied. Its strongest relevance is methodological: diagnosing where a multi-step agent goes wrong requires richer evidence than checking a single answer.

## 2. Document roadmap

The abstract and Introduction explain why long, visually grounded trajectories are difficult to judge and why a binary verdict is insufficient for development. The Introduction also lists four contributions: a three-stage framework, length robustness, structured step-level failure analysis, and benchmark performance. [pp. 1–2]

Related Work separates GUI agents, GUI evaluation methods, and hierarchical decomposition. Its purpose is to position GUIDE relative to rule-based checks, language-model judges, selected-frame methods, reward models, and decomposition used during execution. These descriptions are the authors' account of cited literature; this analysis does not treat the referenced works as separately supplied evidence. [pp. 2–4]

The GUIDE Framework introduces the trajectory notation and then describes segmentation, subtask diagnosis, and overall summarization. Experiments supplies datasets and implementation, followed by main results, length analysis, ablation, segmentation validation, and a failure discussion. The Conclusion repeats the main contribution and performance claims. References begin on page 8 and continue on page 9. The Appendix mentioned in Section 4.5 is not present. [pp. 4–9]

## 3. Background and context

**[A]** A large language model, or LLM, reasons over language. A vision-language model, or VLM, additionally processes visual observations. The paper also uses MLLM for a multimodal large language model in its segmentation-quality validation. A GUI agent uses such models to perceive software states and choose executable actions. The evaluation problem is whether the sequence accomplished the requested goal, rather than whether each action matched one predefined script. [pp. 1–3, 8]

An **observation** is a screen state, usually a screenshot and optionally an accessibility tree. An accessibility tree is a structured representation of interface elements; the paper names it as optional but does not detail its format. An **action** is an operation such as clicking, typing, or scrolling. A **subtask** is a meaningful local portion of the larger workflow. A **long-horizon task** requires many actions and may pass through several application states. [pp. 1, 4]

An **LLM-as-judge** evaluator uses a model to assess another system's performance. A **monolithic** judgment puts the relevant trajectory into a single context and produces one decision. **Context overload** is the authors' explanation for reduced reliability as that input grows. **Post-hoc diagnosis** means analysis after the actions have occurred. GUIDE's decomposition is based on the completed behavior, rather than a plan of what ought to happen. [pp. 1–3]

**[A]** Rule-based evaluation can compare URLs, Document Object Model states, or database assertions. The authors describe these checks as reproducible but brittle and costly to customize. They describe AgentTrek and Autonomous Evaluation as using final screenshots with action text, and WebJudge as selecting key frames and judging them together. GUIDE instead distributes screenshot-supported evaluation across subtask calls. Process reward models supply intermediate reward signals, but the authors distinguish these from human-readable diagnostic reports. [pp. 2–3, 6]

**[D]** A practical distinction is between evidence about what the interface shows and evidence about what the agent intended to do. A log saying that a user profile was opened does not by itself prove that the correct user's profile was opened. Figure 2 illustrates this distinction. This explanation interprets the supplied example; it adds no outside factual claim.

## 4. Research problem and gap

**Existing problem [A].** GUI tasks can be accomplished through multiple valid action sequences. Their records are multimodal and may contain dozens of screenshots and actions. Human verification is expensive because annotators must replay or inspect the trajectory and understand the task domain. Reliable evaluation therefore has to handle varied paths, visual evidence, and complicated completion criteria. [p. 1]

**Shortcomings of previous approaches according to the authors [A].** Single-context judges lose reliability with longer trajectories. Final-image methods omit intermediate visual context. Rule-based approaches need task-specific engineering. Other approaches may require an execution environment or a trained reward model. A bare success/failure result does not identify which subtask failed, why it failed, or what should have happened instead. [pp. 1–3]

**Research gap [A].** Hierarchical decomposition is familiar on the execution side of agent systems, including planning and memory, but the authors argue it has not been adequately transferred to retrospective evaluation. GUIDE's proposed answer is to decompose the actual completed trajectory and evaluate bounded portions independently. [pp. 1, 3–4]

**Motivation and scope [A].** The goal is accurate and interpretable evaluation for agent research and development across web, mobile, and industrial workflows. The evaluated output is task success, supplemented by diagnostic information. The paper does not scope its objective around confidentiality, integrity attacks, privilege boundaries, adversarial pages, or comparative vulnerability of agents and standalone LLMs.

**[D] Boundary on novelty.** The supplied experiments support comparison with the listed evaluators. Statements that GUIDE is the only approach with certain capabilities, or that those capabilities are absent from all existing evaluators, are broader author positioning claims. A closed-document analysis cannot independently establish exclusivity across the entire literature.

## 5. Research questions / objectives / hypotheses

There are no formal numbered research questions. The following are faithful descriptions of the authors' objectives rather than invented questions attributed to them.

| ID | Objective or hypothesis | Status | Evidence location |
|---|---|---|---|
| O1 | Determine task success more accurately than the compared evaluators | Explicit objective | pp. 1–2, §4.2 |
| O2 | Produce interpretable completion verdicts, root-cause analyses, and corrective recommendations | Explicit objective | pp. 1–2, §3.3 |
| O3 | Maintain evaluator reliability on longer trajectories by segmenting context | Explicit objective and central decomposition hypothesis | p. 7, §4.3 |
| O4 | Establish that all three modules contribute to performance | Experiment purpose | p. 7, §4.4 |
| O5 | Validate that automatically inferred segments are usable | Experiment purpose | pp. 7–8, §4.5 |

The paper calls decomposition robustness a central claim and discusses a decomposition hypothesis in Section 4.3. It does not provide a preregistered hypothesis, null hypothesis, formal significance threshold, or statistical hypothesis test. The benchmark, length, ablation, and segmentation studies address different parts of these objectives.

**[D] Research-question alignment.** The user's security question remains unanswered by the paper itself. A suitable contribution to that review is an explicitly indirect one: evidence that multi-step, visually grounded agent evaluation can fail when compressed into a single judgment, and a method for localizing workflow errors. Treating that finding as evidence of higher attack susceptibility would exceed the supplied experiment.

## 6. Assumptions / threat model

**[A] System model.** GUIDE receives a task description and a recorded action-observation sequence. Observations are screenshots, optionally augmented with an accessibility tree. It can evaluate without replaying the task in an execution environment and without model training or task-specific evaluation rules. Segmentation assumes textual action summaries carry enough information to infer useful semantic boundaries. Diagnosis then uses visual evidence for the inferred segments. [pp. 3–5]

**[A] Judgment assumptions.** Human industrial labels and benchmark-author labels serve as reference outcomes. AndroidBench uses human judgments as the oracle. GUIDE relies on the backbone model's reasoning and on a sufficiently informative task description. Section 4.6 explicitly identifies cases where platform-specific business conventions are not fully encoded in that description. [pp. 5–6, 8]

**[D] Implicit dependencies.** Useful diagnosis depends on the recorded trajectory being sufficiently faithful, the screenshots exposing relevant states, the action summaries being informative, and the evaluator understanding the task. These dependencies follow from the inputs and design; they are not presented as a formal list of author assumptions. The paper does not report a test of corrupted logs, missing screenshots, forged observations, or adversarial evaluator inputs.

**Threat model.** No security threat model is supplied. There are no specified attacker goals, assets, capabilities, permissions, trust boundaries, attack budget, or malicious-content construction procedure. The paper's own instructional priorities inside Module 3 concern resolving task-summary disagreements; they do not establish a security defense against hostile content. Likewise, structured JSON output and parsing retries are implementation mechanisms, not measured protections against attacks.

## 7. Methodology

### Study design

**[A]** This is a comparative evaluator study. GUIDE and baselines judge recorded trajectories, and their judgments are compared with success/failure labels. It combines three domain evaluations, an industrial length-stratified analysis, module ablations, and a separate assessment of segmentation quality. There is no training phase reported for GUIDE. [pp. 3, 5–8]

### Module 1: Trajectory Segmentation

The input is the original task description and a textual representation of the full action sequence, described as an action summary without screenshots. A language model produces ordered segment boundaries and a local subtask description for each segment. The rationale is that action sequences capture semantic transitions while omitting images keeps the first stage lightweight and avoids oversized image-context requests. [pp. 4–5]

The boundaries divide the action history into contiguous subtask units. Every unit has a local goal against which its behavior can be judged. This creates an abstraction layer: the next module need not infer the entire task structure afresh from an undivided trace. The authors claim reduced per-call context, but the exact size of segments, their maximum size, and the number of segments per trajectory are not reported as distributions.

### Module 2: Subtask Diagnosis

The diagnostic input contains the current subtask description, the full list of subtask descriptions for context, the actions in the current segment, corresponding screenshots, and a final-state screenshot. A VLM emits a diagnostic triple: a verdict, an error analysis, and step-level corrective recommendations. Verdicts can be success, partial, or fail. [p. 5]

The authors describe a structured JSON schema requiring a reasoning trace before the verdict and enumeration of problematic steps with root-cause explanations and suggested fixes. This is an author description of model output design; the full diagnosis schema is not reproduced in the supplied pages. The paper argues that providing all subtask descriptions prevents repeated assessment of already addressed objectives. It does not separately measure how often double-counting occurs or how accurately suggested fixes repair agents.

### Module 3: Overall Summary

A language model receives the original task instruction, diagnostic reasoning traces, and step-level issue lists, then produces a binary task verdict with a brief explanation. It does not simply fail the task whenever any subtask failed. This allows recovery from intermediate errors and detection of cases where locally plausible subtasks still miss the overall goal. Module 1's summaries are secondary references; original task instructions and diagnostic evidence take priority when they conflict. [p. 5]

### Datasets and labels

| Dataset | Size and source | Labels and task coverage | Reported conditions |
|---|---|---|---|
| Industrial e-commerce | 932 trajectories collected from an industrial platform | Human success/failure labels; 633 distinct task instructions | Order management, product search, product listing; 345 successes and 587 failures; 5–80 steps; approximately 19 steps on average |
| AGENTREWARDBENCH | 1,302 web trajectories from five benchmarks | Ground truth verified by the respective benchmark authors | AssistantBench, VisualWebArena, WebArena, WorkArena, WorkArena++ |
| AndroidBench | 120 tasks, expanded to 480 trajectories across four policies | Human judgments serve as oracle | Tasks randomly sampled from the Android in the Wild test set; AitW human demonstrations, AutoUI-base, AutoUI-large, CogAgent |

These figures are author-reported. The industrial label counts sum to 932. The Android description is not a contradiction between 120 and 480: 120 tasks are evaluated under four policies, giving 120 × 4 = 480 trajectories. [pp. 5–6]

No GUIDE train/validation/test split is specified, consistent with its training-free use. However, the supplied work does not report industrial collection dates, annotation instructions, number of industrial annotators, adjudication, filtering, exclusion criteria, missing data, leakage precautions, dataset release conditions, or licensing. It also does not enumerate per-benchmark web trajectory counts.

### Baselines

Autonomous Evaluation uses the final screenshot and preceding action descriptions. AgentTrek uses the final screenshot with the full action sequence. WebJudge uses retrieved key frames. Rule-based evaluation matches expected outcomes deterministically. A Plan&Solve-like baseline first plans subtasks and aligns them with the trajectory; detailed prompts or alignment implementation are absent. Additional AGENTREWARDBENCH comparators include NNetNav, GPT-4o with an accessibility tree, and Claude 3.7 Sonnet. Android historical comparators include QWen-VL, GPT-4V, Captioner + GPT-4, and Captioner + Mixtral. [pp. 5–7]

### Models and implementation

All three default GUIDE modules use gemini-3.0-flash. AGENTREWARDBENCH additionally evaluates GUIDE with o4-mini. Modules request JSON output, and parsing handles code blocks and malformed output. Parse failures permit up to 10 retries with exponential backoff. API temperature is the default; its numerical value is not stated. Hardware, library versions, token budgets, screenshot resolution, seeds, latency, total model calls, monetary cost, and retry frequencies are not specified. [p. 6]

### Metrics and statistical treatment

Accuracy, precision, recall, and F1 are reported with task success as the positive class. **[D, explanatory terminology]** Accuracy measures agreement across all evaluated trajectories; precision concerns how reliably predicted successes are actual successes; recall concerns how many actual successes are recognized; F1 summarizes precision and recall. These meanings explain the table headings rather than introduce additional experimental results.

Android comparisons among the newly evaluated methods use the same backbone and report mean ± standard deviation over three independent runs. Historical Android rows use different backbones. No confidence intervals, statistical significance tests, or paired tests are reported. Segmentation validation reports Cohen's κ for agreement with one human annotator; it does not report a confidence interval or the human-label contingency table. [pp. 6, 8]

## 8. Experiments / analyses

### X1 — Industrial evaluator comparison

**Purpose:** Assess evaluator correctness on multi-step industrial workflows. **Data:** 932 human-labeled trajectories with success as the positive class. **Conditions:** AgentTrek, Plan&Solve-like, Autonomous Evaluation, WebJudge, and full GUIDE. **Metrics:** accuracy, precision, recall, F1. **Evidence:** Table 1, pages 5–6.

GUIDE reports 95.80 accuracy, 95.00 precision, 93.62 recall, and 94.31 F1, all percentages. WebJudge reports 90.45, 84.04, 91.59, and 87.66 respectively. GUIDE leads accuracy, precision, and F1; AgentTrek leads recall at 100.00. The authors interpret AgentTrek's 51.42 precision and 65.02 accuracy as evidence of excessive success predictions. This is a particular industrial result, not a general finding that AgentTrek always behaves that way.

### X2 — Web meta-evaluation

**Purpose:** Evaluate transfer across five web benchmarks. **Data:** 1,302 trajectories. **Conditions:** Six historical comparator rows plus two GUIDE backbones. **Metric:** overall and per-benchmark precision. **Evidence:** Table 2, page 6.

Default GUIDE has overall precision 89.21%; GUIDE with o4-mini has 86.67%; WebJudge with o4-mini has 82.0%; rule-based has 83.8%. Both GUIDE variants have 100.0% precision on AssistantBench and WorkArena. The default variant scores 78.9 on VisualWebArena, 91.7 on WebArena, and 90.9 on WorkArena++. Precision is the reported outcome; no web accuracy, recall, F1, success-prediction counts, or uncertainty estimates appear in this table.

### X3 — Android evaluator comparison

**Purpose:** Assess mobile evaluation across different action-generating policies and repeated evaluator runs. **Data:** 480 trajectories from 120 tasks × four policies. **Conditions:** Same-backbone AgentTrek, WebJudge, and GUIDE, plus historical different-backbone results. **Metric:** mean accuracy ± standard deviation over three independent runs for newly evaluated methods. **Evidence:** Table 3, pages 6–7.

GUIDE's overall accuracy is 94.9 ± 0.3%, compared with WebJudge's 92.6 ± 0.5% and AgentTrek's 92.4 ± 0.1%. GUIDE leads AutoUI-base and CogAgent, ties WebJudge on AutoUI-large, and does not lead the AitW human-demonstration subset. The authors offer an explanation involving exploratory human behavior, but no controlled experiment isolates that mechanism.

### X4 — Length-stratified industrial analysis

**Purpose:** Test the decomposition robustness hypothesis. **Data:** The industrial dataset divided into six length bins. **Conditions:** The five Table 1 methods. **Metric:** accuracy per bin. **Evidence:** Table 4 and Section 4.3, page 7.

GUIDE ranges from 93.2 to 97.6% across bins. WebJudge falls from 92.9% for fewer than 10 steps to 75.0% for 50–80 steps; AgentTrek falls from 81.4 to 34.1%. The endpoints support a larger GUIDE advantage on the longest trajectories. However, neither all individual baseline sequences nor GUIDE's advantage over WebJudge is strictly monotonic across the six bins. Bin counts and uncertainty are not reported in Table 4.

### X5 — Module ablations

**Purpose:** Determine the contribution of segmentation, diagnostic analysis, and learned summarization. **Data:** Industrial dataset. **Manipulation:** Remove or replace one pipeline component; include a naive whole-trajectory judge. **Metrics:** accuracy, precision, recall, F1. **Evidence:** Table 5, page 7.

Removing segmentation lowers accuracy to 74.14%, removing diagnostic analysis to 93.22%, and replacing summary with a strict all-subtasks-success rule to 87.41%. The naive judge scores 85.61%. The authors attribute the particularly poor unsegmented diagnostic configuration to applying a prompt optimized for subtask-length inputs to an entire trajectory. This is an explanation consistent with the result, not an independently measured mechanism.

### X6 — Segmentation-quality validation

**Purpose:** Evaluate whether inferred subtasks are coherent and accurately described. **Data:** Approximately 3.3k industrial subtasks; a sample of 200 also receives human labels. **Conditions:** MLLM score 1–5; usable threshold ≥4; human usable/problematic binary labeling. **Metrics:** score distribution and Cohen's κ. **Evidence:** Table 6 and Section 4.5, page 8.

The evaluator assesses coherence and boundary quality, plus description–behavior alignment. Scores of 5 and 4 account for 96.9% and 2.5%, totaling 99.4% usable. The remaining 0.6% have scores below 4. Agreement with one human annotator is κ = 0.89. The actual evaluation prompt is referenced in an absent Appendix, and the scoring model identity, sampling method, blinding, and detailed human label distribution are not specified.

## 9. Results

The strongest supported result is that the full GUIDE pipeline performs well as an evaluator on the supplied comparisons. Its industrial accuracy and F1 exceed the listed baselines, its web precision is highest overall, and its Android mean accuracy is highest overall. These findings use different metrics and should not be collapsed into one universal percentage. [Tables 1–3]

| Finding | Numeric evidence | Interpretation and qualification |
|---|---|---|
| Industrial accuracy advantage | 95.80 versus 90.45% | Author-reported advantage of 5.35 percentage points over WebJudge |
| Industrial precision/recall balance | GUIDE 95.00 P, 93.62 R; AgentTrek 51.42 P, 100.00 R | GUIDE does not maximize recall, but avoids AgentTrek's low industrial precision |
| Web overall precision lead | GUIDE 89.21%; rule-based 83.8%; WebJudge 82.0% | Highest listed overall precision; rule-based is the highest non-GUIDE overall row |
| Same-backbone web comparison | GUIDE o4-mini 86.67%; WebJudge o4-mini 82.0% | Supports a pipeline advantage with these models; other input/procedure differences remain |
| Android overall advantage | 94.9 ± 0.3 versus 92.6 ± 0.5% | Higher observed mean than same-backbone WebJudge; not a reported significance test |
| Longest industrial bin | GUIDE 93.2%; WebJudge 75.0%; Plan&Solve-like 27.3% | Strong observed long-bin performance; unknown bin-specific uncertainty |
| Segmentation ablation | Full 95.80%; w/o Seg 74.14% | Reported 21.66-point reduction in this ablation configuration |
| Segmentation usability | 99.4% at scores ≥4; human agreement κ = 0.89 | Supports the specified usability rubric, not proof of optimal boundaries or correct diagnoses |

**[C] Derived comparisons, with operands:** Default GUIDE's precision advantage over the highest non-GUIDE overall web row is 89.21 − 83.8 = **5.41 percentage points**. Its advantage over WebJudge is 89.21 − 82.0 = **7.21 points**, rounded to 7.2 in the prose. Same-backbone web improvement is 86.67 − 82.0 = **4.67 points**. Android's mean advantage over WebJudge is 94.9 − 92.6 = **2.3 points**. These are absolute differences in percentage-valued metrics, not relative percentage improvements.

**[C] Derived length gaps:** GUIDE minus WebJudge is 4.7, 2.4, 4.8, 6.6, 10.6, and 18.2 percentage points for the six ascending length bins. Therefore the advantage is larger at the longest endpoint, but it does not grow monotonically: it initially decreases from 4.7 to 2.4. The paper's monotonic-growth wording overstates that part of Table 4.

## 10. Figure-by-figure interpretation

### Figure 1 — Evaluation paradigms, page 2

**[B]** This is a four-panel process diagram, not a numerical plot. There are no quantitative axes, units, scales, error bars, or confidence intervals. Document stacks, screenshot icons, arrows, scissors, and evaluation boxes encode inputs and processing order. The cream-colored boxes distinguish operations; dashed vertical lines separate methods.

Panel (a), 'LLM method,' sends text operation records directly to evaluation. Panel (b), 'AgentTrek,' adds a last screenshot to the text records. Panel (c), 'WebJudge,' assigns illustrative importance scores to frames at T=1, T=2, and T=3: 0.2, 0.9, and 0.3. The highlighted T=2 frame is marked key, then feeds keypoint extraction. These numbers illustrate selection and are not reported benchmark measurements. Panel (d), GUIDE, splits a full trajectory into three subtask units, diagnoses each, and combines the results into evaluation.

**[A]** The caption contrasts missing visual evidence, final-only visual evidence, selected-frame holistic evaluation, and segmented full-visual evaluation. Its function is to explain the architecture's claimed distinction. It is not empirical evidence that every intermediate screenshot improves accuracy, that three segments are typical, or that GUIDE alone has these properties across all possible evaluators.

### Figure 2 — GUIDE framework, page 3

**[B]** Three broad horizontal bands form a top-to-bottom pipeline: a green Segmenter band, blue-purple Diagnoser band, and purple Summarizer band. Arrows show information moving downward and then into aggregation. There are no statistical axes or measured quantities. Robot mascots visually label the stages and are decorative.

The instruction concerns retrieving today's number-one trending repository and summarizing its owner's top 10 starred repositories. The displayed subtasks are finding GitHub's trending page, accessing user #1's profile, and summarizing the top 10 repositories. The first shown diagnosis reports success. The second reports failure at step 3 because the wrong user, user #2, was clicked; its recommendation is to click user #1. The summarizer combines reports with the instruction into a failed task decision because the target is incorrect.

The figure's tiny final explanation is partially obscured by a stamp and not fully confidently readable. The visible instruction, wrong-user diagnosis, and FAIL decision are enough to interpret its substantive example. The illustrated subtask count and step number are example-specific, not experimental averages. Extracted text contains garbled symbols and interface labels; the supplied visual is used for the architecture and readable example rather than trusting corrupted extraction.

**[A/B]** The caption and method agree on the three modules and their outputs. One important distinction is that the drawing displays a simplified tuple for diagnosis, whereas Equation 4 formally defines verdict, error analysis, and recommendations. The full method, not incidental icon text, establishes the component definitions.

### Figure 3 — Industrial dataset statistics, page 4

**[B] Panel (a), length distribution.** A donut chart places '932 traj.' at its center. Six colored sectors correspond to length groups in the legend. Exact visually readable labels are: <10 steps, 36.3%; 10–20, 27.3%; 20–30, 15.6%; 30–40, 8.2%; 40–50, 8.0%; 50–80, 4.7%. Pale mint, lavender, salmon, blue, teal, and purple distinguish the groups. There is no Cartesian axis or error information. **[C]** The displayed percentages sum to 100.1%, consistent with rounding; exact bin counts cannot be recovered uniquely from rounded percentages.

**[B] Panel (b), success/failure.** A two-sector donut shows 37.0% success in mint and 63.0% failure in salmon. These agree with the reported 345 successes and 587 failures. This is the agents' outcome distribution, not GUIDE's evaluator accuracy.

**[B] Panel (c), success rate by length.** A horizontal lollipop-style plot lists bins vertically and uses horizontal position for success rate. Blue lines and circular markers end at labeled percentages. A dashed vertical reference is marked 'avg'; its precise numeric label is not displayed. An explicit numeric x-axis range is not visible. Values in ascending length order are 39.3, 42.1, 37.9, 28.9, 26.7, and 18.2%. These are exact readable labels, not estimates from marker positions. No uncertainty bars appear.

**Cross-check.** The caption says success decreases monotonically from 39.4% for <10 steps to 18.2% for 50–80. The visual instead shows 39.3%, and the next bin rises to 42.1%. Consequently there are both a caption–visual numeric mismatch and a monotonicity mismatch. The plot supports substantially lower success in the longest groups, but not a strictly decreasing sequence across all groups. The data also do not by themselves establish that length causes difficulty; that causal characterization is the authors' interpretation.

## 11. Table-by-table interpretation

All table entries below are percentages unless marked otherwise. Higher-is-better arrows are author labels. Boldface indicates selected column leaders, not statistical significance. No table marks significance tests.

### Table 1 — Industrial benchmark, page 5

| Method | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| AgentTrek | 65.02 | 51.42 | 100.00 | 67.91 |
| Plan&Solve-like | 82.94 | 72.91 | 85.80 | 78.83 |
| Autonomous Eval | 84.44 | 77.93 | 80.87 | 79.37 |
| WebJudge | 90.45 | 84.04 | 91.59 | 87.66 |
| GUIDE | 95.80 | 95.00 | 93.62 | 94.31 |

GUIDE leads accuracy, precision, and F1; AgentTrek leads recall. AgentTrek is lowest on the other three columns. The result illustrates why success recognition alone is insufficient: perfect recall can coexist with frequent incorrect success predictions. The table supplies no run variation, confidence intervals, or significance information. The Plan&Solve-like implementation is only briefly described in the prose.

### Table 2 — AGENTREWARDBENCH, page 6

| Method | Overall P | AssistantBench | VWA | WA | WorkArena | WorkArena++ |
|---|---:|---:|---:|---:|---:|---:|
| Rule-based† | 83.8 | 25.0 | 85.2 | 79.0 | 100.0 | 83.3 |
| NNetNav† | 52.5 | 20.8 | 54.5 | 54.3 | 77.3 | 43.2 |
| Autonomous Eval† | 67.6 | 83.3 | 61.2 | 67.6 | 96.4 | 59.3 |
| GPT-4o, A11y Tree† | 69.8 | 77.8 | 63.0 | 70.2 | 94.6 | 63.0 |
| Claude 3.7 Sonnet† | 69.4 | 71.4 | 64.8 | 69.3 | 85.3 | 66.7 |
| WebJudge, o4-mini† | 82.0 | 100.0 | 74.5 | 81.2 | 100.0 | 90.0 |
| GUIDE, o4-mini | 86.67 | 100.0 | 76.6 | 89.7 | 100.0 | 87.0 |
| GUIDE, default | 89.21 | 100.0 | 78.9 | 91.7 | 100.0 | 90.9 |

All columns are precision. The dagger means results are taken from reference [9], rather than newly rerun in this paper. Default GUIDE leads overall precision, WA, and WorkArena++; AssistantBench and WorkArena have several ties at 100.0. Rule-based leads VWA at 85.2, exceeding default GUIDE's 78.9. GUIDE o4-mini is below WebJudge on WorkArena++: 87.0 versus 90.0. Therefore neither GUIDE variant dominates every comparator in every column.

NNetNav has the lowest overall precision. The prose calls WebJudge the strongest reported baseline at 82.0, but the rule-based overall row is 83.8. It also calls GPT-4o with an accessibility tree the best prior system at 69.8 without explaining the restriction behind that characterization. The table should govern the precise numerical comparison. No recall or prediction denominators are supplied, so 100% precision cannot be interpreted as all successful tasks being recognized.

### Table 3 — AndroidBench, page 6

| Method | Overall | AitW | AutoUI-base | AutoUI-large | CogAgent |
|---|---|---|---|---|---|
| QWen-VL† | 70.2 | — | — | — | — |
| GPT-4V† | 90.6 | — | — | — | — |
| Captioner + GPT-4† | 89.8 | — | — | — | — |
| Captioner + Mixtral† | 92.9 | — | — | — | — |
| AgentTrek | 92.4 ± 0.1 | 86.1 ± 0.5 | 93.9 ± 0.5 | 99.2 ± 0.0 | 90.3 ± 0.5 |
| WebJudge | 92.6 ± 0.5 | 83.6 ± 1.0 | 93.3 ± 1.7 | 100.0 ± 0.0 | 93.3 ± 0.8 |
| GUIDE | 94.9 ± 0.3 | 85.6 ± 1.9 | 98.1 ± 0.5 | 100.0 ± 0.0 | 95.8 ± 0.9 |

The dagger marks historical results from Pan et al. with different backbones. The remaining rows use gemini-3.0-flash and report mean ± standard deviation over three runs. Dashes mean per-policy values are not supplied, not zero performance. GUIDE leads overall, AutoUI-base, and CogAgent. WebJudge and GUIDE tie at perfect AutoUI-large accuracy. AgentTrek leads the human-demo AitW subset, where GUIDE also has its largest reported standard deviation, 1.9 points. These qualifications temper broad claims of uniformly superior performance.

### Table 4 — Industrial accuracy by trajectory length, page 7

| Method | <10 | 10–20 | 20–30 | 30–40 | 40–50 | 50–80 |
|---|---:|---:|---:|---:|---:|---:|
| AgentTrek | 81.4 | 62.2 | 55.9 | 54.0 | 48.0 | 34.1 |
| Plan&Solve-like | 94.1 | 92.1 | 88.3 | 67.1 | 40.0 | 27.3 |
| Autonomous Eval | 87.9 | 85.0 | 75.2 | 85.5 | 85.3 | 81.8 |
| WebJudge | 92.9 | 92.5 | 89.0 | 89.5 | 85.3 | 75.0 |
| GUIDE | 97.6 | 94.9 | 93.8 | 96.1 | 95.9 | 93.2 |

GUIDE leads every bin. Its minimum is 93.2 and maximum 97.6, a **[C] derived spread of 97.6 − 93.2 = 4.4 points**. Plan&Solve-like has the lowest longest-bin value, 27.3. Autonomous Evaluation and WebJudge have intermediate-bin increases, so baseline degradation is an overall pattern rather than a universal monotonic rule. Bin endpoints are printed as adjacent ranges without a fully explicit inclusivity convention; exact assignment of boundary-length trajectories is not specified. The table provides no bin counts or uncertainty.

### Table 5 — Industrial ablation, page 7

| Variant | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Naive single call | 85.61 | 78.59 | 84.06 | 81.23 |
| Without segmentation | 74.14 | 61.40 | 81.16 | 69.91 |
| Without diagnostic analysis | 93.22 | 88.32 | 94.20 | 91.16 |
| Without summary model | 87.41 | 95.60 | 69.28 | 80.34 |
| Full GUIDE | 95.80 | 95.00 | 93.62 | 94.31 |

Full GUIDE leads accuracy and F1. The strict no-summary rule has the highest precision, 95.60, but the lowest recall, 69.28. Removing diagnostic analysis slightly exceeds full GUIDE's recall, 94.20 versus 93.62, while lowering accuracy and precision. Thus each module improves the overall operating balance rather than every metric individually. **[C]** Accuracy differences from full GUIDE are 10.19 points for Naive, 21.66 for no segmentation, 2.58 for no diagnostic analysis, and 8.39 for no summary, computed by subtracting each row from 95.80.

### Table 6 — Segmentation usability, page 8

| Score | Quality label | Percentage |
|---|---|---:|
| 5 | Highly Usable | 96.9 |
| 4 | Usable | 2.5 |
| 3 | Minor Issues | 0.3 |
| 2 | Risky | 0.2 |
| 1 | Unusable | 0.1 |
| ≥4 | Usable, combined | 99.4 |

This table summarizes the MLLM evaluator's judgments across approximately 3.3k subtasks. **[C]** The combined usable percentage is 96.9 + 2.5 = 99.4; below-threshold scores sum to 0.3 + 0.2 + 0.1 = 0.6. Percentages sum to 100.0. Exact counts cannot be reconstructed because 3.3k is approximate and percentages are rounded. The table does not demonstrate that 99.4% of final task judgments or root-cause explanations are correct.

## 12. Diagram / architecture interpretation

Figures 1 and 2 are the substantive diagrams; their visible details are covered above. The architecture can be traced as a data path:

1. The original task instruction and complete textual action record enter the Segmenter.
2. The Segmenter returns boundaries and inferred subtask descriptions.
3. The boundaries select local action-observation sequences from the recorded trajectory.
4. Each local sequence, its screenshots, its goal, and the full subtask-goal list enter the Diagnoser.
5. The Diagnoser produces a verdict, explanation, and step-level recommendations for each segment.
6. The original task and these diagnoses enter the Summarizer.
7. The Summarizer produces a task-level success/failure judgment and justification.

**[A]** The full subtask list supplies global context to otherwise localized diagnosis. Learned aggregation allows the final decision to consider whether an earlier error was recovered from. This is why the system is not merely a collection of independent binary subtask checks. [p. 5]

**[D]** The supplied workflow is a sequential evaluation pipeline, not a demonstrated online feedback controller. Recommendations could be injected into an agent for refinement according to the authors, but no experiment here measures a feedback loop, agent retraining, or actual repair success. Figure 2's downward arrows show evaluation flow, not proof of an executed remediation cycle.

The diagram also helps bound the context claim: Module 1 still sees the full text action sequence; each diagnosis sees a local screenshot sequence plus global descriptions; Module 3 sees accumulated diagnoses. Reduced image-heavy context per diagnostic call does not establish constant total computational cost.

## 13. Equations and mathematical concepts

### Equation 1 — Trajectory definition, page 4

`τ = (s₀, a₁, s₁, a₂, s₂, …, aₙ, sₙ)`

This defines a sequence, not a loss function or optimization objective. `τ` is the trajectory; `sᵢ` is the screen observation at step `i`; `aᵢ` is the executed action at step `i`; and `n` is the number of actions. The initial observation `s₀` precedes the first action. The final observation `sₙ` follows the last action. Its purpose is to formalize the evidence being evaluated.

Given a task description `t`, the evaluation function `E(t, τ) ∈ {0,1}` decides task success. The paper's intended binary meaning is success/failure, although a separate explicit numeric coding declaration for 0 versus 1 is not supplied. The important distinction is that final task judgment is binary while subtask verdicts are three-valued.

### Equation 2 — Hierarchical evaluation, page 4

`E(t, τ) = Summary({Dᵢ}ᵢ₌₁ᵏ), with Dᵢ = Diagnose(tᵢ, τᵢ)`

Here `k` is the number of subtasks, `tᵢ` the inferred local task description, `τᵢ` its segment, and `Dᵢ` its structured diagnosis. `Diagnose` and `Summary` name model-based operations. The braces denote the collection of diagnoses; the surrounding prose makes clear that the implementation also supplies the original task to the summary model and contextual information to diagnosis. The equation is a simplified architectural definition, not a fully enumerated API signature.

Its input is the decomposed trajectory and task; its intermediate output is a collection of diagnoses; its final output is a binary assessment. No differentiable training objective, convergence condition, theorem, or optimality guarantee is attached to it.

### Equation 3 — Segment construction, page 4

Boundaries are `B = {0 = b₀ < b₁ < … < bₖ = n}`. A segment is:

`τᵢ = (s_(bᵢ₋₁), a_(bᵢ₋₁+1), s_(bᵢ₋₁+1), …, a_(bᵢ), s_(bᵢ))`.

Each `bᵢ` is an action-boundary index. Strictly increasing boundaries create contiguous action intervals and ensure that the last segment reaches the final action. The inferred `tᵢ` describes the segment's goal. **[C/D]** Although the authors call the segments non-overlapping, adjacent mathematical segments share the boundary observation `s_(bᵢ)`: it ends one and starts the next. Their action intervals do not overlap. This is a useful clarification of the displayed formula, not a claim that the implementation duplicates or loses actions.

### Equation 4 — Diagnostic triple, page 5

`Dᵢ = (vᵢ, eᵢ, cᵢ)` with `vᵢ ∈ {success, partial, fail}`.

`vᵢ` is the local completion verdict; `eᵢ` is natural-language analysis of a failure or deficiency; and `cᵢ` is a set of step-level corrective recommendations. The tuple organizes output into whether, why, and what should change. It is not a numeric score or a calibrated probability. The source does not specify a formal objective measure for root-cause correctness or recommendation usefulness.

### Context-complexity argument

**[A]** Section 3.2 states that decomposition reduces the maximum context a subsequent module processes from `O(n)` to `O(n/k)`, and illustrates a 60-step trajectory divided into six ten-step units. **[C]** The step-count ratio is 60/10 = 6, a sixfold reduction in local steps, rather than a tenfold reduction. The source calls it an order-of-magnitude reduction.

**[D]** A maximum segment size of order `n/k` requires sufficiently balanced segments or a size bound; average size alone does not establish the maximum. The paper does not supply that bound. Moreover, the diagnostic calls also receive global subtask descriptions, and summarization sees the accumulated diagnoses. The argument explains why localized processing may help; it is not a measured end-to-end memory, latency, or cost result. No mathematical proof establishes constant per-call context for arbitrarily long trajectories.

## 14. Interpretation and discussion

**[A]** The authors interpret the results as evidence that retrospectively decomposing trajectories makes evaluation both more accurate and more interpretable. Main comparisons address evaluator correctness; length analysis addresses robustness; ablations address pipeline components; segmentation scoring addresses whether the intermediate units are usable. These pieces form a coherent empirical argument, but they do not measure every advertised benefit equally directly.

**[D]** Accuracy and precision gains have direct table support. Interpretability has architectural support and an illustrative report, but there is no developer user study, independent root-cause accuracy score, or measured improvement after following recommendations. The high usability score supports segmentation under its rubric; it should not be substituted for diagnostic explanation validity. Similarly, the domain-knowledge failure discussion is plausible but does not quantify error categories.

### Consistency checks

| Issue | First evidence | Conflicting or qualifying evidence | Assessment |
|---|---|---|---|
| Short-bin success rate | Figure 3 caption: 39.4% | Figure 3c label: 39.3% | Preserve both; cannot resolve the intended exact value |
| Monotonic agent-success decline | Figure 3 caption | 39.3 then 42.1% in first two bins | Broad long-bin decline, not strictly monotonic |
| Monotonic GUIDE advantage | §4.3 says advantage grows monotonically | Table 4 gaps begin 4.7 then 2.4 points | Monotonic statement contradicted by table |
| Strongest overall web baseline | §4.2 names WebJudge at 82.0% | Table 2 rule-based overall P is 83.8% | WebJudge is not highest non-GUIDE overall row |
| Best prior web system wording | §4.2 names GPT-4o at 69.8% | Several historical rows are higher | Intended restriction is unspecified |
| Web metric in conclusion | §5 claims highest accuracy on AGENTREWARDBENCH | Table 2 and §4.2 report precision | Accuracy claim is not established by supplied web results |
| Context reduction example | §3.2 says order of magnitude | 60 steps divided into ten-step units | Explicit ratio is sixfold |
| Android subset leadership | General robust-performance wording | AgentTrek exceeds GUIDE on AitW | Overall lead does not imply every-subset lead |
| Appendix availability | §4.5 says prompt is in Appendix | No Appendix supplied | Reproducibility material missing |

The industrial 39 errors and 4.2% error rate are compatible with the reported rounded accuracy: **[C]** 39/932 × 100 ≈ 4.1845%, leaving 95.8155% correct. The difference between that value and 95.80% is small, but the supplied work does not explain whether it reflects truncation, aggregation, or another reporting choice. It should not be silently converted into an exact confusion matrix.

For the security research question, **[D]** long workflows create more places for wrong actions and mistaken judgments to appear in the recorded sequence, but these experiments do not measure hostile exploitation. The source supports a distinction between workflow evaluation and isolated answer evaluation. It does not support a quantitative claim that agents are more vulnerable, identify which attack surfaces dominate, or establish that segmentation is a security mitigation.

## 15. Contributions and novelty

**Conceptual [A].** GUIDE transfers hierarchical decomposition from task execution to evaluation of completed trajectories. Its conceptual unit is the observed subtask, rather than a predefined milestone or planned action sequence. [pp. 1–4]

**Methodological/algorithmic [A].** The three-stage pipeline separates semantic segmentation, multimodal diagnosis, and task-level aggregation. A three-valued local verdict and structured recommendations replace a bare binary local judgment. Learned aggregation is designed to distinguish recoverable local errors from final task failure. [pp. 4–5]

**System/implementation [A].** The default implementation uses prompted models and structured JSON, without training, task-specific evaluation rules, or required trajectory replay. Parsing with retries makes the implementation tolerant of malformed model output, although operational robustness is not separately benchmarked. [pp. 3, 6]

**Experimental/empirical [A].** Contributions include the three benchmark comparisons, six-bin length analysis, four ablation configurations, and automated segmentation-quality assessment with a 200-subtask human check. The industrial dataset provides a new evaluated workload in the paper, but a public dataset release, data license, or independent benchmark package is not documented. [pp. 5–8]

There is no formal theoretical contribution, theorem, security attack method, or measured defense contribution. **[D]** The most defensible novelty statement is the proposed combination and its observed behavior against the listed comparisons. Literature-wide claims of being first or uniquely capable cannot be independently verified from this supplied paper alone.

## 16. Limitations

### Authors' stated limitations

**[A]** Section 4.6 identifies domain-specific business knowledge as the dominant source of error among 39 industrial misclassifications. A training-free model can miss platform conventions, implicit order-management completion criteria, or the expected final state of supplier-facing listing operations when the task description does not express them. The authors describe this as a trade-off of zero-shot evaluation. They propose a concise domain-knowledge preamble as a lightweight adaptation, but do not report a test of that proposal. [p. 8]

**[A]** The design rationale acknowledges the computational expense and API-failure risk of including full image sequences for long trajectories. The segmentation-quality subsection also acknowledges that poorly formed segments could degrade diagnosis. The latter concern is investigated with a usability study; the supplied evidence does not establish it is impossible or absent in every domain. [pp. 5, 7–8]

### Additional evidence-based analyst observations

**[D]** Diagnostic faithfulness is not directly quantified. Producing a root-cause explanation does not demonstrate that it is correct, and producing a recommendation does not demonstrate successful repair. There is no user study or measured developer productivity benefit.

**[D]** Reproducibility is limited by missing prompts, unspecified industrial annotation procedures, absent model/version details for the segmentation-quality evaluator, and missing operational settings beyond the default model and temperature. No code or data release is established in the supplied pages.

**[D]** Statistical information is uneven: Android has three-run standard deviations, while industrial, web, length-bin, and ablation results have no reported uncertainty. Web results emphasize precision without recall, making completeness of success detection unknown. Length associations may reflect task mix, class balance, and complexity as well as evaluator context effects.

**[D]** The strongest no-segmentation ablation changes input length while retaining a subtask-oriented prompt. It measures that combined configuration, not a perfectly isolated universal effect of segmentation. The authors explicitly acknowledge the prompt mismatch in explaining the result.

**[D]** Security relevance remains indirect. No adversarial distribution, malicious observation, unauthorized action, data exposure, or standalone-LLM comparison is evaluated. Ordinary task failure and security compromise cannot be equated on the evidence supplied.

## 17. Threats to validity

The following validity categories are analyst-applied; the paper does not present a formal threats-to-validity section.

**Internal validity [D].** Ablations support the importance of the tested pipeline components, but removing segmentation also changes compatibility between prompt structure and input length. Comparisons using different historical backbones or inherited results do not isolate architecture alone. The same-backbone o4-mini web comparison and gemini-3.0-flash Android comparisons reduce one source of confounding, without resolving all procedural differences.

**Construct validity [D].** Agreement on task-success labels is an appropriate measure of evaluator correctness, but it is distinct from agent competence, security robustness, explanation truthfulness, or recommendation effectiveness. The segmentation rubric measures coherence and description alignment, not optimal decomposition or faithful root-cause reasoning. A precision-only web result does not measure all aspects of evaluation quality.

**External and ecological validity [D].** Three domains broaden the empirical scope, but the industrial platform is not fully characterized. Results do not establish performance on unseen platforms with different business rules, arbitrary desktop workflows, much longer trajectories than those reported, or adversarial web content. Human demonstrations are included on Android, yet their lower scores suggest trajectory style can matter.

**Statistical conclusion validity [D].** Three-run standard deviations on Android describe observed run variation. They are not confidence intervals, and a narrower standard deviation by itself does not establish that a performance difference cannot be a statistical artifact. The paper supplies no significance test, paired comparison, length-bin uncertainty, or uncertainty around κ = 0.89.

**Reproducibility [D].** The absent Appendix prevents inspection of the stated segmentation-quality prompt. Missing annotation protocols, exact approximate-subtask counts, sampling details, seeds, retry incidence, and baseline prompts limit precise reproduction. Reliance on API defaults also leaves some settings numerically unspecified in the supplied source.

**Research-question validity [D].** Using this paper as direct evidence that web agents are more vulnerable than standalone LLMs would mismatch the measured construct. A security review can cite it as a diagnostic evaluation method and as evidence about long-trajectory judgment difficulty, while clearly separating that from attack susceptibility.

## 18. Future work and open questions

### A. Future work explicitly proposed by the authors

The concrete proposed improvement is a concise domain-knowledge preamble to reduce business-rule errors without model retraining. Section 3.3 also describes the possibility of feeding structured corrective output back to an agent as refinement context. The latter is a potential application rather than an evaluated improvement in the supplied experiments. [pp. 5, 8]

### B. Additional open questions remaining from the study

**[D]** How accurately do diagnostic explanations identify the true failing step and cause? Do developers find the reports useful, and do recommendations improve agent performance? How do results change with shorter or longer segments, different segmenters, uncertain boundaries, or missing observations? What are latency, API cost, token volume, and retry rates relative to holistic judges?

**[D]** How stable are industrial and web results across evaluator runs? What are web recall and F1, and how many predictions underlie the 100% precision cells? Does domain prompting improve accuracy while preserving cross-domain applicability? How reliable is segmentation-quality assessment under another human annotator or an independent scoring model?

**[D, security-review relevance]** Would hostile interface content influence the evaluator or the acting agent? Can diagnosis separate a benign mistake from an attacker-induced deviation? Would any security benefit survive a controlled comparison with a standalone LLM under matched malicious inputs and capabilities? These are open questions suggested by the user's topic, not experiments or future-work claims made by GUIDE's authors.

## 19. Terminology and notation glossary

| Term or symbol | Beginner-friendly meaning in this work |
|---|---|
| GUIDE | GUI Understanding and Interpretable Diagnostic Evaluation |
| GUI | Graphical user interface: visible software controls and states |
| LLM | Large language model |
| VLM | Vision-language model, used for visual observations and reasoning |
| MLLM | Multimodal large language model, used here for quality assessment |
| LLM-as-judge | A model that judges another system's task performance |
| Trajectory | Ordered observations and actions from an executed task |
| Long-horizon | Requiring many actions across a workflow |
| Segmentation | Dividing the completed trajectory into meaningful local units |
| Subtask | A local goal within the overall task |
| Post-hoc | Performed after execution |
| Zero-shot / training-free | Used without domain fine-tuning or newly training GUIDE |
| Backbone | The underlying model powering a module |
| Context window | The input material a model processes in a request |
| Key frame | A selected screenshot considered useful for evaluation |
| Root-cause analysis | Explanation of why a step or subtask was deficient |
| Corrective recommendation | Suggested action or change for addressing an issue |
| JSON | JavaScript Object Notation, the structured output format |
| DOM | Document Object Model, referenced in rule-based interface checks |
| A11y tree | Accessibility tree, a structured interface representation |
| PRM | Process reward model, a related-work evaluation approach |
| VWA / WA | VisualWebArena / WebArena |
| AitW | Android in the Wild; also labels the human-demo policy subset |
| AutoUI-b / AutoUI-l | AutoUI-base / AutoUI-large in Table 3 |
| Acc / P / R / F1 | Accuracy / precision / recall / F1 score |
| pp | Percentage points: an absolute difference between percentages |
| Mean ± std | Average and standard deviation across repeated runs |
| Cohen's κ | Agreement statistic reported for human versus automated binary usability labels |
| t | Original task description |
| τ | Full action-observation trajectory |
| sᵢ / aᵢ | Observation / action at step i |
| n / k | Number of actions / number of subtask segments |
| B / bᵢ | Boundary collection / an individual boundary index |
| tᵢ / τᵢ | Local subtask description / corresponding trajectory segment |
| Dᵢ | Structured diagnosis of subtask i |
| vᵢ / eᵢ / cᵢ | Verdict / error analysis / corrective recommendations |
| E(t, τ) | Binary task-level evaluation function |
| O(n), O(n/k) | Scaling notation used in the authors' context argument |
| † in tables | Historical result imported from a cited paper |
| — in Table 3 | Per-policy value not supplied |

The glossary defines terms needed to read the supplied source. It does not introduce external benchmark facts or independently validate cited systems.

## 20. Key numerical results

This compact ledger distinguishes reported results, visually read labels, and calculations. Full comparison tables are preserved in Section 11.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Industrial trajectories | 932 | trajectories | Collected platform workflow records | Author-reported | p. 5, §4.1 |
| Distinct industrial instructions | 633 | instructions | Industrial dataset | Author-reported | p. 5, §4.1 |
| Industrial successes / failures | 345 / 587 | trajectories | Human labels | Author-reported | p. 5, §4.1 |
| Industrial success / failure shares | 37.0 / 63.0 | % | Dataset outcomes | Author-reported | p. 4, F3; p. 5 |
| Industrial length | 5–80; mean approximately 19 | steps | Full industrial dataset | Author-reported | p. 5, §4.1 |
| Web dataset size | 1,302 across 5 benchmarks | trajectories / benchmarks | AGENTREWARDBENCH | Author-reported | pp. 5–6 |
| Android tasks and trajectories | 120; 480 | tasks / trajectories | Four policies per task | Author-reported | pp. 5–6 |
| Android evaluator repetitions | 3 | runs | New LLM-based comparisons | Author-reported | p. 6, T3 |
| Parse-failure retry limit | Up to 10 | retries | GUIDE JSON parsing | Author-reported | p. 6, §4.1 |
| GUIDE industrial Acc/P/R/F1 | 95.80 / 95.00 / 93.62 / 94.31 | % | Full GUIDE | Author-reported | p. 5, T1 |
| WebJudge industrial accuracy | 90.45 | % | Industrial comparison | Author-reported | p. 5, T1 |
| Industrial accuracy gain | 5.35 | pp | GUIDE versus WebJudge | Author-reported | p. 6, §4.2 |
| GUIDE default web precision | 89.21 | % | Overall AGENTREWARDBENCH | Author-reported | p. 6, T2 |
| GUIDE o4-mini web precision | 86.67 | % | Overall AGENTREWARDBENCH | Author-reported | p. 6, T2 |
| Highest non-GUIDE web precision | 83.8 | % | Rule-based row | Author-reported | p. 6, T2 |
| GUIDE gain over rule-based web row | 5.41 | pp | 89.21 − 83.8 | Analyst-derived | p. 6, T2 |
| GUIDE Android mean accuracy | 94.9 ± 0.3 | % | Mean ± std, 3 runs | Author-reported | p. 6, T3 |
| WebJudge Android mean accuracy | 92.6 ± 0.5 | % | Same backbone, 3 runs | Author-reported | p. 6, T3 |
| GUIDE AitW accuracy | 85.6 ± 1.9 | % | Human-demo subset | Author-reported | p. 6, T3 |
| GUIDE longest-bin accuracy | 93.2 | % | Industrial 50–80 steps | Author-reported | p. 7, T4 |
| WebJudge longest-bin accuracy | 75.0 | % | Industrial 50–80 steps | Author-reported | p. 7, T4 |
| GUIDE length-group range | 93.2–97.6 | % | Six industrial bins | Author-reported | p. 7, §4.3 |
| WebJudge short-to-long drop | 17.9 | pp | 92.9 to 75.0 | Author-reported | p. 7, §4.3 |
| AgentTrek short-to-long drop | 47.3 | pp | 81.4 to 34.1 | Author-reported | p. 7, §4.3 |
| No-segmentation accuracy | 74.14 | % | Industrial ablation | Author-reported | p. 7, T5 |
| No-segmentation accuracy loss | 21.66 | pp | Full 95.80 versus 74.14 | Author-reported | p. 7, §4.4 |
| No-diagnosis / no-summary accuracy | 93.22 / 87.41 | % | Industrial ablations | Author-reported | p. 7, T5 |
| Quality-assessed subtasks | Approximately 3.3k | subtasks | Industrial segmentation | Author-reported | p. 8, §4.5 |
| Human quality-validation sample | 200 | subtasks | One human annotator | Author-reported | p. 8, §4.5 |
| Human/MLLM agreement | 0.89 | Cohen's κ | Binary usable/problematic labels | Author-reported | p. 8, §4.5 |
| Usable segmentation share | 99.4 | % | Scores ≥4 | Author-reported | p. 8, T6 |
| Industrial misclassifications | 39; 4.2 | trajectories; % | GUIDE failure discussion | Author-reported | p. 8, §4.6 |
| Short-bin agent success label | 39.3 | % | Figure label; caption says 39.4 | Visually readable | p. 4, F3c |
| Next-bin agent success label | 42.1 | % | 10–20 steps | Visually readable | p. 4, F3c |
| Longest-bin agent success label | 18.2 | % | 50–80 steps | Visually readable | p. 4, F3c |
| Illustrated local-context ratio | 6 | fold | 60 full steps / 10 local steps | Analyst-derived | p. 4, §3.2 |

No approximate visual estimates are used for quantitative plot values: Figure 3's values are explicitly labeled. Small unreadable diagram text is marked uncertain rather than estimated.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| GUIDE uses three sequential evaluation stages | Method definitions and visible pipeline | F2; E2–E4 | pp. 3–5 | HIGH for architecture; no independent implementation inspection |
| Segmentation uses action text without screenshots | Explicit input description | Module 1 | p. 4, §3.2 | HIGH; sufficiency across all domains remains a claim |
| Diagnosis returns local verdicts, analyses, and fixes | Defined diagnostic triple and structured-output description | E4; F2 | p. 5, §3.3 | HIGH for intended output; correctness of explanations unmeasured |
| Full GUIDE improves industrial accuracy | 95.80 versus WebJudge 90.45 | T1; X1 | pp. 5–6 | HIGH for reported comparison; no uncertainty shown |
| Default GUIDE leads overall web precision | 89.21 exceeds all listed overall rows | T2; X2 | p. 6 | HIGH for table; not a web accuracy result |
| GUIDE improves same-backbone Android mean accuracy | 94.9 ± 0.3 versus 92.6 ± 0.5 | T3; X3 | p. 6 | HIGH for reported means; no significance test |
| GUIDE stays strong in all tested length bins | 93.2–97.6 and leads each column | T4; X4 | p. 7 | HIGH for listed bins; monotonic advantage claim fails |
| Segmentation is important to the tested pipeline | Accuracy 74.14 without segmentation versus 95.80 full | T5; X5 | p. 7 | HIGH for ablation; input/prompt interaction acknowledged |
| Strict aggregation sacrifices success recall | No-summary recall 69.28 versus full 93.62 | T5; X5 | p. 7 | HIGH for result; recovery mechanism not separately counted |
| Most assessed segments are usable | 99.4% scores ≥4; κ = 0.89 on 200 human-checked segments | T6; X6 | p. 8 | HIGH for reported scores; rubric/model details incomplete |
| Domain knowledge is the main reported failure source | Discussion of 39 industrial misclassifications | §4.6 | p. 8 | HIGH for author attribution; category frequencies absent |
| The work informs security analysis only indirectly | Evaluator task framing and non-adversarial benchmark design | S1; S4.1 | pp. 1, 5–6 | MEDIUM analyst inference; no direct vulnerability comparison |
| Long trajectories are not strictly decreasing in agent success | First labels are 39.3 then 42.1 | F3c | p. 4 | HIGH visual observation; caption disagrees |

These evidence-strength assessments concern traceability within the supplied work. They do not substitute for independent reproduction or verification of the referenced baselines.

## 22. Very simple explanation — Explain Like I'm 15

Imagine an AI using a website to finish a complicated errand. It opens pages, clicks things, fills fields, and checks results. To decide whether it succeeded, someone must inspect the whole history. Looking only at its final screen can miss an earlier mistake, and asking another AI to read a huge history at once can also produce wrong judgments.

GUIDE breaks that history into smaller jobs. One model identifies the jobs from the action log. Another looks at each job's actions and screenshots, says whether it worked, and describes mistakes and possible fixes. A final model checks the original goal and combines the reports. It can recognize that an early mistake was later corrected, or that several apparently successful steps still concerned the wrong target.

In the supplied tests, this approach usually judged task success more accurately than the compared methods. On the industrial dataset it was about 95.8% accurate, and it stayed above 93% in every reported length group. But those numbers describe the judge's accuracy, not how often the acting AI succeeded. Some findings concern precision instead of accuracy, and the paper has a few mismatches between its wording and its tables or plot labels.

For a security project, the useful lesson is that an agent's behavior must be examined across the entire workflow, with enough evidence to locate a deviation. This paper does not show that attackers can exploit agents more easily than standalone language models. It supplies a way to investigate ordinary workflow failures; determining vulnerability would require security experiments that are absent here.

## Completeness Audit

The following audit uses the inventory as its denominator. 'Fully represented' means that the substantive content necessary for this analysis is represented, not that every original word has been reproduced.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| META: title, authors, affiliations, publication marker | Yes | Yes | Fully represented | Identity below; no confirmed conference venue |
| ABS: abstract | Yes | Yes | Represented in compressed form | Core framing, method, and findings preserved |
| S1: Introduction | Yes | Yes | Fully represented | Motivation, gap, and four contribution categories |
| S2.1: GUI Agents | Yes | Yes | Represented in compressed form | Named context and agent modalities; cited papers not independently reviewed |
| S2.2: GUI Agent Evaluation | Yes | Yes | Fully represented | Rules, judges, final images, key frames, reward signals |
| S2.3: Hierarchical Decomposition | Yes | Yes | Represented in compressed form | Planning, reasoning, memory, and error-recovery categories |
| S3.1: Problem Formulation | Yes | Yes | Fully represented | Inputs, trajectory, binary evaluation |
| S3.2: Trajectory Segmentation | Yes | Yes | Fully represented | Text-only inputs, boundaries, rationale, context caveats |
| S3.3: Subtask Diagnosis | Yes | Yes | Fully represented | Inputs, three verdicts, explanation and recommendation structure |
| S3.4: Overall Summary | Yes | Yes | Fully represented | Learned aggregation, recovery rationale, evidence priority |
| S4.1: Experimental Setup | Yes | Yes | Fully represented | Datasets, labels, baselines, metrics, model, retries, missing settings |
| S4.2: Main Results | Yes | Yes | Fully represented | All three benchmark conditions and tables |
| S4.3: Long-Trajectory Analysis | Yes | Yes | Fully represented | All bin results and nonmonotonic gap correction |
| S4.4: Ablation Study | Yes | Yes | Fully represented | All variants and metrics |
| S4.5: Segmentation Validation | Yes | Yes | Fully represented for supplied content | Absent Appendix explicitly excluded |
| S4.6: Discussion | Yes | Yes | Fully represented | Domain-knowledge failures and proposed preamble |
| S5: Conclusion | Yes | Yes | Represented in compressed form | Repeated synthesis compressed; web metric mismatch flagged |
| F1a–F1d | Visually | Yes | Fully represented | Four paradigms; illustrative scores distinguished |
| F2 | Visually | Yes | Fully represented at substantive level | Tiny final explanation partly obscured; architecture and example readable |
| F3a–F3c | Visually | Yes | Fully represented | All readable labels; caption conflicts preserved |
| T1 | Visually and text | Yes | Fully represented | All numeric cells |
| T2 | Visually and text | Yes | Fully represented | All numeric cells, inherited-result marker, leaders and exceptions |
| T3 | Visually and text | Yes | Fully represented | All values and standard deviations; missing cells explained |
| T4 | Visually and text | Yes | Fully represented | All length-bin values |
| T5 | Visually and text | Yes | Fully represented | All ablation values |
| T6 | Visually and text | Yes | Fully represented | All score percentages and threshold |
| E1 | Visually and text | Yes | Fully represented | Trajectory definition |
| E2 | Visually and text | Yes | Fully represented | Hierarchical judgment and simplified signature |
| E3 | Visually and text | Yes | Fully represented | Boundary construction and shared observations |
| E4 | Visually and text | Yes | Fully represented | Diagnostic triple |
| X1 industrial comparison | Yes | Yes | Fully represented | Purpose, setup, results, qualifications |
| X2 web comparison | Yes | Yes | Fully represented | Precision-only conditions preserved |
| X3 Android comparison | Yes | Yes | Fully represented | Four policies, repeated runs, historical backbones |
| X4 length analysis | Yes | Yes | Fully represented | Association distinguished from causal proof |
| X5 ablations | Yes | Yes | Fully represented | Prompt/input confounding identified |
| X6 segmentation validation | Yes | Yes | Fully represented | Rubric, 200-subtask check, κ, missing protocol |
| Explicit research questions | Checked | Yes | No formal questions present | Objectives represented without inventing author questions |
| Hypotheses | Checked | Yes | Fully represented | Informal decomposition hypothesis; no formal statistical test |
| Algorithms/pseudocode | Checked | Yes | No numbered algorithm present | Procedural architecture described |
| Theorems/lemmas/propositions | Checked | Yes | None present | No theoretical claims invented |
| Major contributions | Yes | Yes | Fully represented | Conceptual, methodological, implementation, empirical |
| Author-stated limitations | Yes | Yes | Fully represented | Business knowledge, image-context burden, segment-quality concern |
| Equal-contribution footnote | Yes | Yes | Fully represented | First two authors marked equal contributors |
| REF: references 1–29 | Yes | Yes | Represented in compressed form | Bibliography inspected; individual cited papers not supplied |
| Page 9 appearance | No visual supplied | No | Inaccessible visually | Text references inspected; layout not assessed |
| APP-MISSING: quality prompt Appendix | No | No | Missing from supplied material | Explicit reference on page 8 |
| Supplied supplementary material | None | Not applicable | None supplied | No supplementary review claimed |
| Decorative robots, stamps, repeated headers | Yes where visible | Accounted for | Inspected but deliberately omitted as non-substantive | Stamp contributes a visible FAIL cue; artwork supplies no scientific measurement |

### Document identity

**Original title:** GUIDE: Interpretable GUI Agent Evaluation via Hierarchical Diagnosis. **Authors:** Yuwen Zhai, Runze Li, Liang Wang, Nian Shi, Liwu Xu, Wei Zhang, Ran Lin, Bo Xu, and Benlei Cui. Yuwen Zhai and Runze Li are marked equal contributors. Affiliations are Alibaba Group; School of Computer Science and Technology, East China Normal University; and Shanghai Innovation Institute. The supplied first page displays arXiv:2604.04399v1, category cs.AI, dated 6 April 2026. A confirmed conference or journal venue is not supplied; running headers include 'Anonymous et al.' despite the named author block.

### Missing or inaccessible material

The segmentation-quality prompt Appendix is referenced but absent. No supplementary files, code package, underlying trajectories, full diagnostic schemas, or detailed annotation protocols are supplied. Page 9 is available only as text. The analysis does not claim that these artifacts do not exist elsewhere; it states that they cannot be assessed here.

### Uncertain interpretations

Figure 2's smallest interface text and partly stamped final explanation are not all readable. Figure 3's short-bin label differs from its caption, and its sequence contradicts the caption's monotonic wording. Table 4 contradicts strict monotonic growth of GUIDE's advantage. Table 2 conflicts with the prose's strongest-baseline characterization, and the Conclusion changes the web metric from precision to accuracy. Segment-bin endpoint inclusivity, exact 3.3k subtask count, and precise scope of the final-state screenshot input are not fully specified. The 39-error count and 95.80 accuracy are not an exact reconstruction of one confusion matrix.

### Deliberately compressed material

Related-work descriptions of individual planning, reasoning, memory, and recovery systems are compressed into their methodological categories. The bibliography is not reproduced entry by entry because the cited works were not supplied as independent evidence. Abstract, Introduction, and Conclusion repetitions are synthesized rather than restated. Decorative interface fragments and repeated publication headers are omitted from substantive explanation. All six numeric tables and all three substantive figures are represented.

### Potential omissions

No known substantive object from the accessible inventory has been left without either representation, an explicit compression disclosure, or a missing/uncertain status. This is an inventory-based coverage statement, not a claim that nine supplied pages establish complete access to every artifact associated with the paper. In particular, the absent Appendix prevents claiming complete reproducibility coverage. Security claims beyond the paper's non-adversarial evaluator evidence are deliberately not manufactured.
