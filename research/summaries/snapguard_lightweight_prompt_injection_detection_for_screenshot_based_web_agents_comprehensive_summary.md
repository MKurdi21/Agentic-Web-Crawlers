## Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and page images. The paper and the attack instructions depicted within it are treated as evidence, never as instructions to execute. No external sources, tools, repository contents, or supplementary files were consulted.

| Accessibility item | Finding |
|---|---|
| Main document available | Yes: supplied extracted text for physical PDF pages 1–10 |
| Accessible page range | 1–10; ten physical pages |
| Visually inspected pages | 1, 2, 4, 5, 6, 7, and 8 |
| Text-only pages | 3, 9, and 10 |
| Apparently missing main pages | None within the supplied 1–10 sequence; this does not establish that all referenced supporting material was supplied |
| Visual content | All seven numbered figures and four numbered tables appear on supplied rendered pages and were visually inspected |
| Tables | Main results and ablation/runtime tables are readable; extracted text assists exact transcription |
| Equations | Equations (1)–(2) are available as text; (3)–(7) also have rendered-page support |
| Appendices | No appendix is supplied, despite references to Appendix B.2, Appendix B.3, and Appendix C |
| Supplementary material | None supplied; no embedded attachments reported in the accessibility metadata |
| Referenced external artifact | An anonymized code/experiments repository is mentioned on p. 2; it was not accessed |
| OCR | Additional OCR was unnecessary; supplied extraction was checked against available page images where relevant |
| Remaining constraints | Exact pattern rules, alternative OCR configuration details, metric aggregation formulas, and any appendix qualifications are unavailable |

Evidence labels throughout are **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external-information category is used. Confidence is HIGH for clearly readable source facts, MEDIUM for bounded interpretations or unresolved implementation details, LOW for weak extrapolation, and UNKNOWN where essential information is absent. Physical PDF page numbers provide all page locators.

## 1. Plain-language orientation

SnapGuard studies a security problem in AI systems that view screenshots and operate websites. A user might ask an agent to buy a product, complete a form, or retrieve information. The agent sees a webpage and chooses an action. An attacker can place instructions inside that webpage or its images, attempting to make the agent follow the page's instructions instead of the user's request. This is **prompt injection**: untrusted task material tries to become an instruction source. [A; pp. 1–3]

The authors propose an external detector named **SnapGuard**. Before a screenshot reaches the agent, the detector examines two kinds of evidence. One branch measures how much the strengths of image edges vary across the screenshot. The other reads text from the original image and a selectively color-inverted version, then checks the recovered text for action-inducing patterns. The detector is intended to block suspicious inputs without changing the agent's policy. [A; pp. 3–5]

On a benchmark evaluation containing 948 benign and 2,185 malicious samples, SnapGuard reports average true-positive rate 0.66, average false-positive rate 0.09, and F1 score 0.75. Its reported runtime is 1.81 seconds per image, with no additional GPU memory usage. GPT-4o-prompt reports F1 0.71 and runtime 14.50 seconds under the paper's comparison. These are screenshot-detection results, not measured reductions in completed malicious actions during live agent tasks. [A; pp. 5–8]

For the user's research question—**Why are web AI agents more vulnerable than standalone large language models?**—the paper is relevant because it describes untrusted environmental inputs, multimodal attack delivery, and the conversion of injected instructions into executable actions. **Analyst inference [D]:** these mechanisms explain additional exposure and potential consequences in an agent workflow. The paper does not directly compare a standalone large language model with a web agent under matched conditions, so it cannot establish a numerical vulnerability gap between them.

## 2. Document roadmap

The work is an empirical AI-security and systems-method paper, combining a threat model, a lightweight detection algorithm, and benchmark experiments. It is not a theoretical security proof, systematic review, or new dataset paper.

| Inventory ID | Original item | Pages | Function |
|---|---|---:|---|
| S0 | Abstract, metadata, keywords | 1 | States problem, method, and headline results |
| S1 | §1 Introduction | 1–2 | Motivates screenshot-specific detection and efficiency requirements |
| S2 | §2 Related Works | 2–3 | Positions attacks, detectors, and guardrails |
| SS2.1 | §2.1 Prompt Injection Attacks on Web Agents | 2 | Describes visual, webpage, and user-content attack settings |
| SS2.2 | §2.2 Prompt Injection Defenses for Web Agents | 2–3 | Reviews text-centric and multimodal defenses |
| S3 | §3 Threat Model | 3 | Defines agent, attacker, and defender |
| SS3.1–3.3 | Problem Formulation; Attacker's Goal and Capability; Defender's Goal and Capability | 3 | Specifies inputs, action deviation, and screenshot-only defense |
| S4 | §4 Method | 3–5 | Introduces two-branch detection |
| SS4.1–4.3 | Overview; Visual Stability Indicator; Textual Signal Extraction | 3–5 | Defines image statistic, reversal, OCR, and action cues |
| S5 | §5 Evaluation | 5–8 | Reports benchmark, comparisons, robustness, ablations, efficiency, and examples |
| SS5.1–5.6 | Experiment Setup; Defensive Performance; Robustness Analysis; Ablation; Efficiency Analysis; Case Study | 5–8 | Supplies distinct empirical analyses |
| S6 | §6 Conclusion and Future Work | 8–9 | Restates contribution and proposes extensions |
| REF | References [1]–[57] | 9–10 | Bibliographic context; cited works were not independently inspected |

Visual inventory: F1 attack schematic, F2 architecture, F3 receiver operating characteristic curves, F4 extraction-interface comparison, F5 Gaussian-noise robustness, F6 visual-statistic examples, and F7 concealed-text example. Table inventory: T1 image-based baselines, T2 text-based baselines, T3 component ablations, and T4 module runtime. Mathematical inventory: E1–E7, corresponding to equations (1)–(7). There is no numbered algorithm, theorem, lemma, proof, or pseudocode block in the supplied work.

The original title is **SnapGuard: Lightweight Prompt Injection Detection for Screenshot-Based Web Agents**. Authors are Mengyao Du, Han Fang, Haokai Ma, Jiahao Chen, Kai Xu, Quanjun Yin, and Ee-Chien Chang. Affiliations are National University of Defense Technology, University of Science and Technology of China, National University of Singapore, and Zhejiang University. Keywords are Web Agents, Prompt Injection Detection, and Multimodal Security. [A; p. 1]

Publication metadata require caution. The first page gives arXiv:2604.25562v1 and 28 April 2026. Conference headers identify ACMMM '26, April 03–05, 2026, Woodstock, NY, but the reference-format block also contains a 2018 year, placeholder DOI/ISBN elements, and an instruction to insert the correct conference title. Running headers sometimes say Trovato et al. **Observation [B/D]:** these are internally inconsistent/template-like metadata; the supplied document does not establish a reliable final publication record.

## 3. Background and context

A **large language model (LLM)** processes language and generates outputs. A **vision–language model (VLM)** processes visual and language inputs. The paper describes screenshot-based web agents as systems that combine a task prompt, previous interactions, and a current screenshot to select a next operation. A generated natural-language action is subsequently **grounded**, meaning connected to an actual user-interface operation such as clicking a visual element. [A; p. 3]

**HTML**, the webpage markup, and the **Document Object Model (DOM)**, its structured representation, can expose page text and organization. The target agents instead act on rendered screenshots. Consequently, a defense expecting structured text cannot simply assume that the necessary text representation exists in its deployment interface. The paper evaluates text-based detectors after an additional image-to-text extraction step. [A; pp. 1, 3, 6]

**Optical character recognition (OCR)** extracts text from images. SnapGuard uses Pytesseract in its principal implementation. Reading a screenshot is imperfect: faint or concealed text may be omitted. SnapGuard therefore extracts from two views and combines their outputs. This is a recovery strategy for cues, not a claim that the page's meaning is perfectly reconstructed. [A; pp. 4–5]

A **true positive** is a malicious sample detected as malicious; a **false positive** is a benign sample flagged as malicious. **True-positive rate (TPR)** measures attack detection; **false-positive rate (FPR)** measures false alarms. **F1** is used as an overall detection measure, but its precise implementation and aggregation are referred to the absent Appendix C. A **receiver operating characteristic (ROC)** curve plots TPR against FPR across operating conditions. **Area under the curve (AUC)** summarizes that plotted discrimination. These explanations give the intended reading of the reported measures without reconstructing unavailable appendix formulas.

A security distinction matters throughout: recognizing a suspicious screenshot is not the same as proving that an agent cannot be manipulated. SnapGuard evaluates the former. Downstream mitigation, dynamic interactions, and stronger end-to-end guarantees appear as future directions. [A/D; p. 9]

## 4. Research problem and gap

**Existing problem [A].** Attackers embed malicious instructions or perturbations into webpages, images, or interface elements. Agents may interpret these inputs as reasons to depart from user intent, including clicking malicious links or disclosing credentials. The authors emphasize that this can result in concrete actions rather than only undesirable text. [pp. 1–3]

**Shortcomings attributed to prior methods [A].** Many detectors operate on text, embeddings of text, or structured webpage representations. Screenshot-only pipelines do not supply those representations directly. Other methods use large VLMs to reason about complete pages, which the authors argue adds substantial runtime and GPU memory cost. Mutation-based defenses compare responses to transformed inputs, while other image defenses target broader VLM safety rather than this particular detection interface. [pp. 1–3]

**Research gap [A].** The authors seek a lightweight screenshot detector that handles both low-level visual anomalies and explicit or concealed textual action cues without relying on heavyweight full-page semantic reasoning. Modern pages mix images, text, layouts, and interactive elements; an injection can occupy a small region or be difficult for humans to see. [p. 2]

**Motivation [A].** Interactive agents need timely decisions. The introduction cites prior work associating response delays beyond four seconds with degraded user experience. That is a cited motivation, not an experiment conducted here, and not a universal usability threshold established by SnapGuard. [p. 2]

**Scope [A/D].** The evaluated problem is image-level malicious-input detection across eight attack configurations and two benign delivery categories. The supplied evidence does not evaluate the comparative security of every web-agent architecture, all visual attacks, or standalone LLMs.

## 5. Research questions, objectives, and hypotheses

**Explicit research question RQ1 [A]:** can prompt injection attacks be detected from screenshots in a lightweight manner? This appears in the abstract and introduction. [pp. 1–2]

The paper gives objectives rather than a formally numbered hypothesis set:

- **O1:** identify visual and textual differences between injected and benign webpages.
- **O2:** combine a Visual Stability Indicator with recovered action-oriented text in an efficient external detector.
- **O3:** compare detection and deployment cost with image-based and text-based baselines.
- **O4:** assess dependence on text extraction interfaces, resilience to Gaussian noise, and component contributions.

**Methodological expectations [A], not formal statistical hypotheses:** malicious visual content tends to reduce local structural variation; dual-view text recovery helps reveal concealed cues; action-oriented pattern detection contributes efficient, interpretable decisions. [pp. 4–5]

The paper does not report preregistered hypotheses, null hypotheses, or hypothesis-test significance levels. Its expectation about low structural variation is supported with benchmark behavior and selected illustrations, not established as a universal property of injected pages.

## 6. Assumptions / Threat Model

**Agent/system model [A].** At time t, the agent receives prompt p, interaction history h_t, and screenshot x_t. Its multimodal policy produces action a_t. The prompt includes both system and user instructions. The interaction history contains earlier screenshot–action pairs. The action space consists of executable interface actions. [§3.1, p. 3]

**Attacker goal [A].** Alter the visual input so that, with the same prompt and history, the agent selects an attacker-desired action outside the user's intended behavior. Examples include malicious-link clicks, credential disclosure, and control instructions overriding user intent. [§3.2, p. 3]

**Attacker capabilities [A].** Two models are described. A malicious content provider can introduce crafted material into user-generated or third-party images, such as product images uploaded by an adversarial seller. A malicious website owner can control rendered page content or layouts. Both can iteratively refine content using feedback from surrogate or publicly available agents. Pixel-level perturbations and explicit visual instructions are both in scope. [p. 3]

**Defender capabilities [A].** The detector receives only the raw screenshot. It does not receive the user instruction, structured webpage text, the agent's internal reasoning, adversarial intent, or attack strategy. It does not change the agent policy. OCR or a VLM may optionally recover text from the image, but HTML/DOM access is not assumed. Deployment is as an external pre-action module. [§3.3, p. 3]

**Trust boundary [D].** The design places a screening step between an untrusted visual environment and the agent. The screenshot is evidence to classify, not an authoritative instruction source. The paper does not provide a complete trust analysis of screenshot capture, OCR integrity, detector tampering, or compromised browser infrastructure.

**Important constraint [D].** Because the defender does not know the user's task, it cannot directly compare an instruction visible on a page against the user's actual intent. It relies on image statistics and learned-by-design cue categories. This constraint helps explain the lightweight interface but leaves task-dependent ambiguity unresolved.

## 7. Methodology

### 7.1 Architecture and processing

The method has two complementary branches. The visual branch computes a **Visual Stability Indicator (VSI)** from screenshot gradients. The textual branch performs **Contrast-Polarity Reversal (CPR)**, extracts text from original and transformed views, and applies **Action-Oriented Pattern Detection (APD)**. The outputs are jointly evaluated to produce a risk estimate intended to block malicious inputs before agent processing. [§4.1, pp. 3–4]

The main text calls the combination a compact representation and lightweight decision module, and later refers to VSI filtering logic or a structural anomaly gate. However, the supplied pages do not specify a fully reproducible Boolean expression, weighting rule, or calibration procedure for fusing the two branches. It would be incorrect to invent an AND rule, OR rule, or learned classifier.

### 7.2 Visual branch

The screenshot has height H, width W, and three red–green–blue channels with values in [0,255]. The image is converted to grayscale, and a two-dimensional spatial gradient is evaluated at each pixel. VSI is the variance of gradient magnitudes across spatial positions. Low values indicate little variation in edge strength; high values indicate heterogeneous local structure. The authors expect malicious content to have unusually low values relative to benign inputs. [§4.2, p. 4]

A threshold is selected using scores on a benign dataset to constrain false-positive probability. The chosen experimental target is alpha = 0.05; the VSI threshold is 4,450. Inputs below the threshold are visually suspicious. The authors state O(HW) computational complexity and no learnable parameters for VSI. The gradient implementation, boundary treatment, grayscale conversion coefficients, and calibration-set composition are not specified in the supplied pages. [pp. 4–5]

### 7.3 Textual branch

CPR identifies pixels with grayscale intensity greater than gamma = 240 and selectively replaces their color values x by 255 − x. The binary mask is broadcast over color channels. Pixels outside the mask remain unchanged. This is selective near-white-region inversion, not simply a global inversion of the entire image. [§4.3, p. 4]

The detector obtains OCR candidates from the original screenshot and transformed screenshot and takes their union. The purpose is to retain action cues that either individual view might miss. Candidate handling, ordering, deduplication, OCR confidence filtering, and exact text-merging mechanics are not supplied. [p. 4]

APD checks recovered text for cue categories: interaction triggers, credential requests, link invitations, and control-override instructions. The authors describe this as targeting functional action intent rather than surface wording alone and emphasize traceability to matched patterns. Exact category specifications and matching rules are referred to absent Appendix B.3. Therefore, the supplied work supports a category-based pattern detector but not an independently reconstructable implementation of those patterns. [p. 5]

### 7.4 Data and sample construction

The evaluation follows WAInjectBench. It contains **948 benign samples** and **2,185 malicious samples**. Benign samples are grouped into **embedded images**, where text is part of image content, and **screenshots**, depicting rendered webpages or application interfaces. The source does not give the number of benign samples in each category or malicious samples in each attack configuration. [§5.1, p. 5]

Training-based baselines additionally use 1,000 benign images sampled from the COCO 2017 validation set and 1,000 malicious JailGuard samples. These are described specifically for Embedding-I and fine-tuned LLaVA. Their use does not establish a training regime for SnapGuard, whose main detector is image processing plus rules. Exact overlap checks, random seeds, split assignments, deduplication, labeling procedures, exclusions, and dataset licenses are not supplied here. [p. 5]

**Analyst-derived [C]:** the stated evaluation counts sum to 948 + 2,185 = **3,133 images**. This is an aggregate count, not evidence that every robustness or interface experiment used all 3,133 images.

### 7.5 Attacks and baselines

Eight attack configurations are evaluated: EIA, WebInject, Pop-up, WASP, VWA-emb, VWA-shot, VPI-BU, and VPI-CU. VWA-emb and VWA-shot distinguish embedded-image and screenshot attacks in Visual Web Arena. VPI-BU and VPI-CU distinguish browser-use and computer-use settings for visual prompt injection. The paper does not expand every attack acronym; undefined expansions are not invented. [p. 5]

Image-based comparators are Embedding-I, JailGuard, LLaVA-1.5-7B, LLaVA-1.5-7B-FT, and GPT-4o-prompt. Embedding-I uses OpenCLIP ViT-B/32 image representations and logistic regression. JailGuard examines output inconsistency under input transformations. LLaVA-FT is a fine-tuned variant. [pp. 5–6]

Text-based comparators are Embedding-T, Known-Answer Detection (KAD), PromptGuard, DataSentinel, and PromptArmor. Embedding-T uses all-MiniLM-L6-v2 and logistic regression. KAD checks deviation from a known response. The others are described as a prompt-injection classifier, game-theoretic detector, and auxiliary-LLM sanitization method, respectively. In this evaluation they receive text extracted with DeepSeek-OCR. [pp. 5–6]

### 7.6 Implementation, configuration, and statistics

SnapGuard's principal implementation uses Pytesseract, and its modules run on CPU. Other evaluated tools include Qwen3-VL-8B-Thinking, LLaVA-1.5-7b-hf, DeepSeek-OCR-2, GPT-4o, and Llama-3-8B-Instruct. The setup mentions Llama-3-8B for action-oriented reasoning, while the principal method describes rule-based APD and the ablation replaces APD with LLaMA-3-8B. **Uncertainty:** the exact role of this model in every baseline/interface experiment is not fully resolved by the supplied prose. [pp. 5, 7–8]

Thresholds are fixed across experiments without dataset-specific tuning. Learning-based baselines follow benchmark defaults; LLaVA fine-tuning uses Low-Rank Adaptation (LoRA). Training uses four NVIDIA A40 GPUs, each with 48 GB memory. That is training hardware; the CPU model, inference hardware allocation, API environment, software versions, batch sizes, repetition counts, and timing variability are not supplied. [p. 5]

Metrics are TPR, FPR, F1, average inference seconds per image, and peak GPU memory. No confidence intervals, error bars, standard deviations, repeated-run estimates, or statistical significance tests are reported in the supplied results. Appendix C is referenced for metric formulas but is absent.

## 8. Experiments / Analyses

| Experiment | Purpose and conditions | Evidence and principal result | Qualification |
|---|---|---|---|
| X1 Image-based comparison | Compare six detectors across eight attacks and two benign categories | T1: SnapGuard F1 0.75, average TPR 0.66, average FPR 0.09; GPT-4o-prompt F1 0.71 | Best aggregate F1 does not mean best on every attack or lowest false alarms |
| X2 Text-based comparison | Feed DeepSeek-OCR text into five text detectors; compare with SnapGuard | T2: strongest text-baseline F1 is PromptArmor 0.45; SnapGuard 0.75 | Table costs exclude baseline OCR; SnapGuard includes its own lightweight OCR pipeline |
| X3 ROC comparison | Compare score/threshold discrimination with Embedding-I | F3: AUC 0.742 versus 0.652 | No uncertainty interval or exact curve-generation procedure supplied |
| X4 Extraction interface | Change text extractor/configuration within SnapGuard | F4: OCR 0.75/1.8 s; OCR Alt. 0.75/1.7 s; LLaVA 0.46/1.1 s; Qwen 0.76/16.0 s; GPT-4o 0.76/15.6 s | Exact OCR configurations are in absent Appendix B.2 |
| X5 Visual perturbation | Add Gaussian noise at sigma values shown from 0.2 to 1.0 | F5: SnapGuard remains around F1 0.8 and above plotted baselines | Sigma normalization, clipping, per-point exact values, and repetitions are not specified |
| X6 Component ablation | Remove VSI, remove CPR, or replace APD with LLaMA-3-8B | T3: full F1 0.75; variants 0.56, 0.64, 0.56 | APD comparison is replacement, not pure deletion |
| X7 Efficiency decomposition | Measure each module's average runtime | T4: total 1.810 s; CPR+OCR 1.788 s | Hardware-specific generalization and timing variance unavailable |
| X8 Visual case study | Compare structural maps for selected benign/malicious images | F6: benign VSI 17,360/16,822; malicious 457/2,672 | Four selected examples do not establish population separation |
| X9 Textual case study | Compare original and reversed views of concealed instruction | F7: merged OCR yields control instruction; result TRIGGERED | One illustration; no case-specific counterfactual agent outcome measured |

The experiments address the main lightweight-detection question through detection accuracy and runtime, while robustness and ablations probe component behavior. There is no experiment directly addressing a formal standalone-LLM-versus-web-agent hypothesis, and no direct evaluation of task completion, actual secret leakage, false-block recovery, or multi-step attack prevention.

## 9. Results

**Aggregate detection [A].** SnapGuard reports F1 0.75, average TPR 0.66, and average FPR 0.09. GPT-4o-prompt reports 0.71, 0.55, and 0.00 respectively. **Analyst-derived [C]:** differences are 0.04 F1 units, 0.11 TPR units, and 0.09 FPR units. Thus the aggregate improvement includes a false-alarm trade-off rather than dominance on every measure. [T1, p. 6]

**Attack dependence [A].** SnapGuard's TPRs are 0.80 EIA, 0.53 WebInject, 0.70 Pop-up, 0.71 WASP, 0.75 VWA-emb, 0.13 VWA-shot, 0.82 VPI-BU, and 0.81 VPI-CU. VWA-shot is the clear weak point. GPT-4o-prompt has higher reported TPR on Pop-up, WASP, VPI-BU, and VPI-CU; it ties EIA and is lower on WebInject and both VWA variants. The paper's broad superiority wording therefore applies most defensibly to aggregate F1 and selected comparisons. [T1]

**Benign conditions [A].** SnapGuard FPR is 0.04 for embedded images and 0.14 for screenshots. **Derived [C]:** the latter is 0.10 higher, or 10 percentage points. The target alpha = 0.05 concerns VSI threshold selection; the full system's reported average FPR is 0.09. These are different quantities and must not be conflated. [pp. 4–6]

**Efficiency [A/C].** SnapGuard's 1.81 s versus GPT-4o-prompt's 14.50 s gives a derived ratio 14.50/1.81 ≈ **8.01**, consistent with the authors' approximately eightfold speed claim. Some baselines are faster than SnapGuard but detect far fewer attacks: for example Embedding-I takes 0.04 s and has F1 0.52. SnapGuard is not universally the fastest detector. [T1]

**Text baselines [A].** Text-only detection after DeepSeek-OCR often performs poorly: Embedding-T F1 0.00, KAD 0.05, PromptGuard 0.13, DataSentinel 0.05, and PromptArmor 0.45. PromptArmor has substantial TPR on VPI-BU/VPI-CU, 0.76/0.78, so failure is heterogeneous rather than universal. [T2]

**ROC [A/C].** AUC is 0.742 for SnapGuard and 0.652 for Embedding-I, a derived difference of 0.090. At FPR approximately 0.1, the prose describes SnapGuard TPR approximately 0.6 versus roughly 0.3 for Embedding-I. Those are approximate operating-point descriptions, not exact tabulated values. [F3, p. 6]

**Component effects [A/C].** Removing VSI lowers F1 from 0.75 to 0.56, a derived decrease of 0.19. Removing CPR lowers it to 0.64, a decrease of 0.11. Replacing APD lowers it to 0.56 and raises FPR from 0.09 to 0.18. VSI removal has TPR 0.49/FPR 0.05; APD replacement has TPR 0.37/FPR 0.18, showing different error profiles despite tied F1. [T3]

**Metric aggregation caution [D].** The table's Avg. TPR should not automatically be interpreted as the unweighted arithmetic mean of its eight displayed attack rates. For example, SnapGuard's displayed values sum to 5.25, and 5.25/8 = 0.65625, consistent with 0.66 after rounding; however, JailGuard's displayed values sum to 0.65, yielding 0.08125, also consistent with 0.08. These checks do not determine aggregation of counts, F1, or category weights. Missing per-category counts and Appendix C prevent full reconstruction of all reported metrics.

## 10. Figure-by-figure interpretation

### Figure 1 — Attack mechanism

The diagram on p. 2 shows an Amazon-like page, a user request to buy the cheapest USB cable, a screenshot supplied to a web agent, and two action paths. The intended path selects Buy Now; the injected path follows a webpage instruction to click another link. Arrows connect webpage, screenshot perception, agent, and actions. There are no numerical axes, units, or statistical estimates. This is a conceptual illustration of source confusion and action diversion, not a measured attack-success experiment. [A/B]

### Figure 2 — SnapGuard architecture

The diagram on p. 4 depicts attacker-modified webpage input entering visual and textual processing. The visual branch includes a VSI map and score representation; the textual branch includes contrast reversal, OCR, and an action-induction representation. Their outputs identify a malicious webpage with a visual score and detected action type. A block symbol prevents malicious content reaching the web agent, while a safe webpage proceeds toward task output and user. The small illustrative score/distribution elements do not establish calibration or an exact fusion function. The figure supports the two-branch placement and pre-action role. [A/B]

### Figure 3 — ROC comparison

Two side-by-side line plots on p. 6 compare Embedding-I and SnapGuard. Both horizontal axes are FPR and vertical axes are TPR, with linear 0–1 ranges. Embedding-I is red and SnapGuard blue; shaded areas emphasize AUC, and diagonal dashed references show equal-coordinate lines. Explicit labels are AUC = 0.652 and AUC = 0.742. SnapGuard rises more steeply near low FPR; Embedding-I increases more gradually. No confidence bands or error bars are identified. The plots support better discrimination in this comparison, not certainty that every threshold improves both error rates. [A/B]

### Figure 4 — Text-extraction interfaces

On p. 7, five blue bars show F1 using the left linear axis, and a red dashed line shows runtime in seconds using the right axis. Categories are OCR, OCR Alt., LLaVA, Qwen, and GPT-4o. Explicit bar labels are 0.75, 0.75, 0.46, 0.76, and 0.76; runtime labels are 1.8 s, 1.7 s, 1.1 s, 16.0 s, and 15.6 s. Bars use differing hatch patterns, and no uncertainty bars appear. Qwen and GPT-4o improve F1 by only 0.01 relative to OCR while costing much more time. LLaVA is faster but clearly worse in F1. The figure therefore supports robustness across several interfaces with a meaningful LLaVA exception. [A/B]

### Figure 5 — Gaussian-noise robustness

The p. 7 line chart has a linear horizontal axis labeled noise perturbation level sigma, with displayed points at 0.2, 0.4, 0.6, 0.8, and 1.0. The vertical axis is F1 score. SnapGuard uses blue circular markers, Embedding-I yellow/orange square markers, JailGuard a gray dash-dot triangular style, GPT-4o red diamond/dotted styling, and LLaVA-FT purple triangular/dashed styling. Exact per-point values are not labeled. SnapGuard appears approximately 0.77–0.83 and remains highest. Embedding-I is roughly in the mid-to-upper 0.6 range, GPT-4o around 0.6, LLaVA-FT near 0.2, and JailGuard lower. These are approximate visual estimates, not exact observations to substitute for raw data. No error bars are visible. Gaussian noise is the actual tested perturbation; compression, rescaling, and remote-rendering artifacts are motivating examples, not separately demonstrated experiments. [A/B/D]

### Figure 6 — Structural response maps

On p. 8, a color scale with ticks from 0 through 800 accompanies selected original images and their VSI-related response maps. Columns are grouped as benign and malicious, with two examples in each group. Explicit VSI labels are 17,360 and 16,822 for benign examples, and 457 and 2,672 for malicious examples. Benign maps show richer distributed structure; malicious maps emphasize fewer rigid edges. The color-scale values should not be equated with the image-level VSI labels: the caption/prose distinguish local responses from the overall statistic, and the scale's physical units are not specified. All displayed malicious scores fall below threshold 4,450, while displayed benign scores exceed it. That comparison is analyst-derived from reported operands. [A/B/C]

### Figure 7 — Concealed textual injection

The p. 8 figure juxtaposes a light original form and a darker transformed view, followed by an OCR-text and detected-actions panel. It exposes a directive to type the task description received, rather than merely completing the form. The output lists Attack_action_count: 2, action type control_instruction, and result TRIGGERED. There are no axes or statistical quantities. The accompanying prose says either individual view gives incomplete or absent cues and merged OCR reveals the malicious semantics. This is evidence of one worked detection example; it does not quantify how often inversion succeeds or prove that the downstream agent would execute that exact instruction. [A/B]

## 11. Table-by-table interpretation

### Table 1 — Image-based detection

Rows are methods. Benign columns give FPR for embedded images and screenshots. Eight malicious columns give attack-specific TPR. Aggregate columns give FPR, TPR, and F1; cost columns give seconds and GPU memory in MB. Down arrows mean smaller is preferred; up arrows mean larger is preferred. No uncertainty or significance markers appear. A dash in GPT-4o memory is missing/unreported information, not zero.

| Method | Avg. FPR | Avg. TPR | F1 | Time s | GPU memory MB |
|---|---:|---:|---:|---:|---:|
| Embedding-I | 0.25 | 0.44 | 0.52 | 0.04 | 591.00 |
| JailGuard | 0.28 | 0.08 | 0.12 | 6.12 | 13840.00 |
| LLaVA-1.5-7B | 0.00 | 0.00 | 0.00 | 0.19 | 13875.00 |
| LLaVA-1.5-7B-FT | 0.04 | 0.13 | 0.23 | 0.18 | 13594.00 |
| GPT-4o-prompt | 0.00 | 0.55 | 0.71 | 14.50 | — |
| SnapGuard | 0.09 | 0.66 | 0.75 | 1.81 | 0.00 |

SnapGuard has highest aggregate F1/TPR. Several methods tie for lowest FPR but include methods detecting no attacks. Embedding-I is fastest. Thus a low FPR by itself is not evidence of useful protection. SnapGuard's 0.00 GPU-memory entry concerns GPU use; CPU memory and total process memory are not measured by that entry. [T1, p. 6]

For attack-specific traceability, all reported TPRs are retained below in the original attack order.

| Method | EIA | WebInject | Pop-up | WASP | VWA-emb | VWA-shot | VPI-BU | VPI-CU |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Embedding-I | 0.44 | 0.71 | 0.47 | 0.44 | 0.36 | 0.28 | 0.48 | 0.37 |
| JailGuard | 0.05 | 0.02 | 0.05 | 0.00 | 0.45 | 0.04 | 0.02 | 0.02 |
| LLaVA-1.5-7B | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| LLaVA-1.5-7B-FT | 0.14 | 0.03 | 0.21 | 0.04 | 0.22 | 0.02 | 0.20 | 0.21 |
| GPT-4o-prompt | 0.80 | 0.00 | 0.84 | 0.92 | 0.04 | 0.00 | 0.89 | 0.93 |
| SnapGuard | 0.80 | 0.53 | 0.70 | 0.71 | 0.75 | 0.13 | 0.82 | 0.81 |

The benign embedded/screenshot FPR pairs are respectively 0.21/0.30, 0.54/0.02, 0.00/0.00, 0.02/0.07, 0.00/0.00, and 0.04/0.14 in that same method order. Embedding-I exceeds SnapGuard on WebInject and VWA-shot. This further limits claims of universal per-attack superiority.

### Table 2 — Text-based detection

The table uses the same attack and benign columns, but the text-baseline cost omits DeepSeek-OCR extraction. SnapGuard's repeated row describes its own full pipeline. The authors separately report extraction overhead of 78.69 s and 7.9 GB peak memory. Those costs cannot be ignored when interpreting table latency. [p. 6]

| Method | Avg. FPR | Avg. TPR | F1 | Detector time s | GPU memory MB |
|---|---:|---:|---:|---:|---:|
| Embedding-T | 0.00 | 0.00 | 0.00 | 0.00 | 236.30 |
| KAD | 0.02 | 0.02 | 0.05 | 0.48 | 16062.80 |
| PromptGuard | 0.00 | 0.07 | 0.13 | 0.01 | 1157.20 |
| DataSentinel | 0.01 | 0.02 | 0.05 | 0.66 | 7387.60 |
| PromptArmor | 0.00 | 0.29 | 0.45 | 1.31 | — |
| SnapGuard | 0.09 | 0.66 | 0.75 | 1.81 | 0.00 |

| Method | EIA | WebInject | Pop-up | WASP | VWA-emb | VWA-shot | VPI-BU | VPI-CU |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Embedding-T | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| KAD | 0.02 | 0.01 | 0.08 | 0.02 | 0.00 | 0.06 | 0.00 | 0.00 |
| PromptGuard | 0.55 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| DataSentinel | 0.02 | 0.00 | 0.08 | 0.02 | 0.00 | 0.07 | 0.00 | 0.00 |
| PromptArmor | 0.39 | 0.00 | 0.00 | 0.38 | 0.00 | 0.00 | 0.76 | 0.78 |

SnapGuard's per-attack row is identical to T1 and is deliberately not duplicated here. Benign embedded/screenshot FPR pairs for the five text baselines are 0.00/0.00, 0.00/0.03, 0.00/0.00, 0.00/0.02, and 0.00/0.00. PromptArmor is strongest among these text baselines by aggregate F1, but SnapGuard has the highest TPR in every displayed attack column relative to these five methods. A reported time of 0.00 is the table's precision-limited value, not evidence of literally instantaneous computation.

### Table 3 — Component ablation

| Variant | VSI | CPR | APD | Avg. TPR | Avg. FPR | F1 |
|---|---|---|---|---:|---:|---:|
| Full | Yes | Yes | Yes | 0.66 | 0.09 | 0.75 |
| Without VSI | No | Yes | Yes | 0.49 | 0.05 | 0.56 |
| Without CPR | Yes | No | Yes | 0.57 | 0.08 | 0.64 |
| Without APD | Yes | Yes | Replaced | 0.37 | 0.18 | 0.56 |

The full method has highest F1 and TPR. Without VSI has lowest FPR. APD replacement is worst in TPR and highest in false alarms. There are no significance estimates. The prose calls the APD drop the most significant, but this is descriptive language rather than a reported statistical test, and the F1 decrease ties removal of VSI. [pp. 7–8]

### Table 4 — Runtime composition

VSI takes 0.021 s, CPR+OCR 1.788 s, and APD 0.001 s; total is 1.810 s. Reported proportions are 1.2%, 98.8%, less than 0.1%, and 100%. OCR-related processing dominates. The table supports a lightweight decision stage, while also showing that reading text is a central pipeline cost. It does not give CPU utilization, energy, peak RAM, throughput, or latency percentiles. [p. 8]

## 12. Diagram / Architecture

F1 and F2 are the substantive diagrams. F1 explains the attack control path: user intent enters the agent, while attacker-controlled instructions arrive through screenshot content and divert the eventual operation. This illustrates why an environmental observation can become a security-sensitive instruction channel. It is not a diagram of direct modification to the trusted user prompt. [pp. 2–3]

F2 explains the defense data path: webpage screenshot → visual statistics and transformed/original OCR → visual score and action cues → risk assessment → blocking or allowing the screenshot before agent action. The illustration separates detection from the agent's ordinary task-output path. No feedback loop, iterative detection protocol, multi-step state update, or recovery interaction is specified. [p. 4]

**Analyst interpretation [D]:** placement before perception/action can reduce the amount of malicious material reaching the agent, but blocking an input also needs an operational policy: retry, ask for help, skip a page, or stop. Those downstream decisions are not evaluated. The authors' future-work discussion explicitly distinguishes a standalone detector from a more complete mitigation pipeline. [p. 9]

## 13. Equations and mathematical concepts

### Equation (1): agent action policy

`a_t = pi(p, h_t, x_t)` [§3.1, p. 3]. This is a functional system definition. The input p is the system-plus-user prompt; h_t is the sequence of previous screenshot/action pairs; x_t is the current screenshot. The policy pi is a multimodal model and a_t belongs to executable action space A. Its output is an instruction subsequently grounded into a UI operation. This equation defines what the attacker tries to influence; it is not an optimization objective or training loss.

### Equation (2): malicious action condition

`pi(p, h_t, x'_t) ∈ A_mal` [p. 3]. Here x'_t is the attacker-modified visual input and A_mal is the set of actions deviating from the user's intended behavior. The same p and h_t are retained. The membership symbol means the resulting action falls inside the undesirable-action set. The formulation requires visual similarity in surrounding prose, but gives no distance function, numerical perturbation budget, or quantified similarity constraint.

### Equation (3): visual stability score

`phi(x) = E_(i,j)[||∇x_(i,j)||_2^2] − (E_(i,j)[||∇x_(i,j)||_2])^2` [§4.2, p. 4]. The gradient is a two-component vector from the grayscale screenshot, the norm measures edge magnitude, and E_(i,j) averages over pixel locations. The expression is the second moment of magnitudes minus their squared mean: variance of edge strengths across the image. Inputs are the screenshot and its spatial gradients; output is a scalar image score.

**Plain meaning:** determine whether the page contains a diverse mix of weak and strong local changes or relatively uniform structural responses. The authors associate unusually low variation with injected content. The statistic is not a direct measure of instruction meaning, nor does its definition guarantee that every attack decreases it. No learned parameters enter this equation. [A/D]

### Equation (4): benign calibration condition

`P(phi(x) < tau | x ∈ D_benign) ≤ alpha` [p. 4]. Tau is a threshold; D_benign is the benign calibration dataset; alpha is an allowed false-positive level. The inequality constrains the probability that a benign image receives a low suspicious score. Experimentally alpha = 0.05 and tau = 4,450. The inequality alone does not specify a unique threshold or how finite-sample estimation is performed. It is a branch-level design condition, not an unconditional end-to-end security bound.

### Equation (5): selective inversion

`I(x) = x ⊙ (1 − M_bar) + (255·1 − x) ⊙ M_bar` [§4.3, p. 4]. I(x) is a transformed image. M_bar is a binary mask broadcast from H×W pixels to H×W×3 channels. The symbol ⊙ means element-wise multiplication, and 1 is an all-ones quantity of compatible shape. Where the mask is zero, the original pixel is retained; where it is one, each channel becomes 255 minus its original value. The operation supports contrast recovery before OCR.

### Equation (6): mask definition

`M(i,j) = 1[Y(i,j) > gamma]` [p. 4]. Y is grayscale intensity, gamma = 240, and the indicator is one when the condition is true and zero otherwise. It selects near-white regions for inversion. The strict greater-than condition should be preserved. The supplied text does not specify grayscale implementation details or an empirical sweep over gamma.

### Equation (7): two-view OCR candidates

`T(x) = O(x) ∪ O(I(x))` [p. 4]. O is an OCR function; T(x) is the set of candidate text recovered from both views; union means retain candidates found in either. This equation explains why concealed cues may be recovered without requiring one view to contain all text. It does not specify ordering, merging collisions, or OCR confidence thresholds.

No formal theorem, proof, robustness certificate, learning objective, or mathematical expression for final multimodal fusion appears in the supplied document. Those absences limit implementation reproducibility and the strength of theoretical security claims.

## 14. Interpretation and discussion

**Authors' interpretation [A].** Visual statistics and recovered action cues provide enough useful evidence to obtain strong benchmark F1 without large-model semantic analysis of an entire page. Ablations and selected examples support complementarity; runtime decomposition shows that image statistics and rule matching are cheap relative to OCR. [pp. 7–9]

**Analyst interpretation [D].** The evidence supports a practical trade-off at the evaluated operating conditions, rather than comprehensive prevention. SnapGuard accepts more benign false alarms than GPT-4o-prompt, misses many VWA-shot attacks, and is outperformed by particular baselines in some attack columns. Therefore, statements such as effective across diverse attacks should retain the attack-specific results.

Several source-consistency issues affect interpretation:

| Issue | Source statements | Assessment |
|---|---|---|
| OCR presence | §4.3/§5.1 explicitly use OCR; p. 6 says SnapGuard operates without requiring the text extraction stage | Literal wording conflicts with the method. A possible reading is that it avoids the separate DeepSeek-OCR preprocessing used for text baselines, but that is analyst interpretation, not a correction established by the authors |
| Negligible OCR overhead | p. 5 describes lightweight OCR as negligible relative to the overall inference pipeline; T4 assigns CPR+OCR 98.8% of SnapGuard time | Reference pipeline may differ, but it is not specified. OCR is clearly dominant within the detector |
| Alpha versus final FPR | alpha = 0.05 calibrates VSI; full detector average FPR is 0.09 | Different conditions; no demonstrated guarantee that the complete detector meets 5% FPR |
| Universal superiority wording | Broad introduction claims; T1 shows multiple attack-specific baseline wins | Aggregate superiority is supported more narrowly than universal attack-wise superiority |
| Memory language | Abstract says no additional memory overhead; metrics/T4 discussion specify GPU memory and CPU execution | Zero GPU use is supported; zero total memory use is not |
| APD removal | Called w/o APD; actual setup replaces it with LLaMA-3-8B | Interpret as a replacement ablation, with changed computation as well as detection mechanism |
| Publication identity | 2026 arXiv/conference markers coexist with 2018/template fields | Final publication metadata remain uncertain |

For the user's research question, the strongest supported mechanism is **environment-to-action coupling**: an attacker manipulates observed content, and the agent turns its interpretation into executable operations. Multimodality adds input locations and makes text-only screening incomplete. **This remains an analyst synthesis of this paper, not a controlled demonstration that agents have a higher intrinsic injection rate than standalone models.**

## 15. Contributions and novelty

**Conceptual [A].** The paper frames screenshot prompt-injection detection as multimodal representation analysis rather than mandatory full-page semantic reasoning.

**Algorithmic/methodological [A].** It combines gradient-magnitude variance, selectively inverted dual-view OCR, and action-oriented cue categories. The individual mathematical operations are explicitly defined; the contribution is their proposed use and integration for this security setting, rather than a theorem that they characterize all attacks.

**System [A].** A screenshot-only external pre-action detector is designed to avoid policy modification and agent-internal access.

**Implementation [A].** The main pipeline uses CPU image processing, Pytesseract, and rules, reporting no extra GPU allocation.

**Empirical [A].** Benchmark comparisons cover eight attack configurations, two benign categories, ten baseline methods across two tables, ROC behavior, extraction-interface changes, Gaussian noise, component ablations, runtime decomposition, and two qualitative case-study modalities.

There is no claimed new dataset or benchmark introduced in the supplied text, and no theoretical contribution supported by a proof. **Analyst qualification [D]:** novelty is presented here as the authors' positioning; establishing priority against the broader literature would require external review, which was not requested.

## 16. Limitations

### Authors' stated limitations

There is no dedicated limitations section. The authors acknowledge that extracting text can be incomplete or noisy and that the goal is not maximum OCR fidelity. Their efficiency analysis identifies text extraction as the principal bottleneck. LLaVA extraction performs poorly in the interface experiment. These are explicit operational qualifications. [pp. 4, 7–8]

The future-work section identifies extensions to downstream mitigation, dynamic elements/temporal sequences, and joint perception–detection optimization. These indicate areas beyond current evaluation, but should not be rephrased as a comprehensive formal limitations statement. [p. 9]

### Additional evidence-based analyst observations

1. **Task-independent detection:** the defender does not receive user intent, so ordinary actionable webpage text and malicious directives may be hard to distinguish in a task-sensitive way. [p. 3]
2. **Weak attack condition:** VWA-shot TPR is 0.13 at the reported operating point. [T1]
3. **False-alarm burden:** screenshot benign FPR is 0.14; no workflow-level usability cost is measured. [T1]
4. **Incomplete implementation detail:** pattern rules, OCR alternatives, metrics, and final fusion logic cannot be fully reconstructed from supplied material.
5. **No adaptive-detector evaluation established:** attacker refinement is allowed in the threat model, but the results do not document attacks optimized specifically to evade SnapGuard's score and patterns.
6. **Image-level outcomes:** the main metrics do not measure completed malicious operations or end-to-end task safety.
7. **Selected examples:** four visual samples and one concealed-text case are illustrative, not distribution-wide explanations.
8. **Uncertainty missing:** reported improvements lack variability estimates and significance testing.
9. **Resource scope:** zero GPU memory excludes CPU RAM; exact deployment hardware and API timing controls are unclear.
10. **Partial supporting material:** absent appendices prevent inspection of details the main text delegates to them.

These are analyst observations [D], not limitations explicitly admitted by the authors.

## 17. Threats to validity

The following validity framework is analytical, not terminology adopted by the authors.

**Internal validity [D].** Baseline adaptation matters: text methods depend on DeepSeek-OCR, and detector-only versus end-to-end timings differ. Without exact prompts, configurations, fusion rules, and repeated timing protocol, the source of each performance difference cannot be isolated fully. APD replacement changes more than just presence of one feature.

**External validity [D].** Evidence comes from a finite benchmark with eight attack configurations. It does not establish behavior on new websites, different visual styles, languages, screen sizes, or attacks specifically optimized against the detector. The strong dependence on attack type is visible within the benchmark itself.

**Construct validity [D].** Screenshot classification is a proxy for preventing agent compromise. F1 and AUC do not directly measure successful user-task completion, actual leakage, malicious-action frequency, or disruption caused by blocked benign pages. The low-level VSI statistic is a visual anomaly proxy, not a semantic definition of maliciousness.

**Statistical conclusion validity [D].** Missing intervals, repeated runs, category counts, and metric aggregation details limit interpretation of small differences such as F1 0.75 versus 0.76. The source reports these differences but does not establish that they exceed experimental variability.

**Ecological validity [D].** Gaussian noise approximates one degraded-image condition; it does not separately validate compression, rescaling, animations, or remote desktops. Static image tests also omit temporal context and operational recovery after blocking.

**Reproducibility [D].** The repository is claimed available but was not inspected. Missing appendices and implementation details constrain reproduction from this supplied paper alone. Hash and page locators identify the provided source, not independent verification that its experimental artifacts reproduce the results.

## 18. Future work and open questions

### A. Authors' proposed future work

On p. 9, the authors propose integrating detection with action filtering or risk-aware decisions; extending image-level detection to dynamic webpage elements and temporal interaction sequences; and jointly optimizing perception and detection for stronger end-to-end guarantees. These are prospective goals, not demonstrated capabilities.

### B. Additional open questions inferred from the evidence

**Analyst questions [D]:** How does the detector behave against attacks designed to preserve benign gradient statistics? Can task context reduce false positives without sacrificing the screenshot-only interface? What explains the low VWA-shot TPR? How much protection remains when OCR fails in a new language or visual style? How should an agent recover after a block? What is the effect on complete task success and privacy leakage? Do the reported runtime and threshold behavior transfer across hardware and screen resolutions? Can matched standalone-model and agent experiments isolate extra exposure from extra action consequences?

The supplied study does not answer these questions, and their inclusion should not be mistaken for author-proposed experiments.

## 19. Terminology and notation glossary

| Term/symbol | Meaning in this paper |
|---|---|
| Prompt injection | Attacker content attempts to redirect behavior away from user intent |
| Web agent | System that perceives web state and chooses executable operations |
| Screenshot-based | Agent input is a rendered image rather than structured page text |
| LLM | Large language model |
| VLM | Vision–language model |
| MLLM | Multimodal large language model, used in baseline descriptions |
| UI | User interface |
| HTML/DOM | Webpage markup/structured document representation |
| Grounding | Connecting generated action instructions to concrete UI operations |
| OCR | Optical character recognition, extracting image text |
| VSI | Visual Stability Indicator, variance of spatial gradient magnitudes |
| CPR | Contrast-Polarity Reversal, selective near-white-pixel inversion |
| APD | Action-Oriented Pattern Detection, matching recovered action cues |
| TPR/FPR | True-positive rate/false-positive rate |
| F1 | Reported aggregate detection score; detailed formulas delegated to absent Appendix C |
| ROC/AUC | TPR–FPR operating curve/area under that curve |
| LoRA | Low-Rank Adaptation used for the fine-tuned baseline |
| p | Combined system and user prompt |
| h_t | Earlier screenshot–action interaction history |
| x_t, x'_t | Original and attacker-modified screenshot |
| pi, a_t | Agent policy and selected action |
| A, A_mal | Executable action space and malicious/deviating-action subset |
| H, W | Screenshot height and width |
| ∇x_(i,j) | Two-dimensional grayscale spatial gradient at a pixel |
| phi(x) | Scalar VSI score |
| tau, alpha | VSI threshold and calibration false-positive target |
| Y, gamma | Grayscale intensity and near-white threshold 240 |
| M, M_bar | Spatial binary mask and channel-broadcast mask |
| ⊙, ∪ | Element-wise multiplication and candidate-set union |
| I, O, T | Image transformation, OCR function, combined text candidates |
| sigma | Gaussian-noise perturbation level; normalization/unit not supplied |
| EIA/WASP/VWA/VPI | Attack labels retained as supplied; expansions are not invented where absent |

## 20. Key numerical results

Values below are exact source values unless marked approximate or derived. Rates and scores are unitless.

| Quantity/result | Value | Unit | Condition/context | Status | Source |
|---|---:|---|---|---|---|
| Benign evaluation images | 948 | samples | Two delivery categories | Author-reported | p. 5 §5.1 |
| Malicious evaluation images | 2,185 | samples | Eight configurations | Author-reported | p. 5 §5.1 |
| Total evaluation images | 3,133 | samples | 948 + 2,185 | Analyst-derived | p. 5 |
| Extra baseline training samples | 1,000 + 1,000 | images | COCO benign/JailGuard malicious | Author-reported | p. 5 |
| Near-white cutoff | 240 | intensity | Gamma in Eq. (6) | Author-reported | p. 4 |
| VSI calibration alpha | 0.05 | rate | Benign-score threshold design | Author-reported | p. 5 |
| VSI threshold | 4,450 | score | Fixed experiment threshold | Author-reported | p. 5 |
| SnapGuard average FPR/TPR/F1 | 0.09/0.66/0.75 | rates/score | Main benchmark | Author-reported | p. 6 T1 |
| SnapGuard benign FPR | 0.04/0.14 | rate | Embedded/screenshot | Author-reported | p. 6 T1 |
| SnapGuard VWA-shot TPR | 0.13 | rate | Weakest displayed attack condition | Author-reported | p. 6 T1 |
| GPT-4o-prompt FPR/TPR/F1 | 0.00/0.55/0.71 | rates/score | Main image baseline | Author-reported | p. 6 T1 |
| SnapGuard/GPT-4o runtime | 1.81/14.50 | s/image | Main comparison | Author-reported | p. 6 T1 |
| Runtime ratio | ≈8.01 | ratio | 14.50/1.81 | Analyst-derived | p. 6 T1 |
| SnapGuard GPU memory | 0.00 | MB | CPU implementation | Author-reported | pp. 6, 8 |
| SnapGuard/Embedding-I AUC | 0.742/0.652 | score | ROC experiment | Visually readable | p. 6 F3 |
| AUC difference | 0.090 | score | 0.742 − 0.652 | Analyst-derived | p. 6 F3 |
| Text-baseline OCR overhead | 78.69 | s/image | DeepSeek-OCR, excluded from T2 | Author-reported | p. 6 |
| Text-baseline OCR memory | 7.9 | GB | Peak extraction memory | Author-reported | p. 6 |
| Interface F1 values | 0.75/0.75/0.46/0.76/0.76 | score | OCR/Alt./LLaVA/Qwen/GPT-4o | Visually readable | p. 7 F4 |
| Noise experiment SnapGuard F1 | approximately 0.8 | score | Sigma 0.2–1.0 | Approximate visual estimate | p. 7 F5 |
| Full/no-VSI/no-CPR/APD-replaced F1 | 0.75/0.56/0.64/0.56 | score | Ablation variants | Author-reported | p. 8 T3 |
| VSI/CPR+OCR/APD runtime | 0.021/1.788/0.001 | s/image | Module decomposition | Author-reported | p. 8 T4 |
| CPR+OCR time share | 98.8 | percent | Detector runtime | Author-reported | p. 8 T4 |
| Benign example VSI | 17,360; 16,822 | score | Two selected images | Visually readable | p. 8 F6 |
| Malicious example VSI | 457; 2,672 | score | Two selected images | Visually readable | p. 8 F6 |
| Training GPUs | 4 × 48 | GPU count × GB | NVIDIA A40 | Author-reported | p. 5 |

No exact Gaussian-noise per-point data, uncertainty intervals, significance levels, or full metric-count tables are supplied.

## 21. Claim–evidence map

| Claim | Evidence | Figure/table/experiment | Source | Qualification/evidence strength |
|---|---|---|---|---|
| Untrusted visual content can redirect executable agent actions | Formal agent/attack model and illustrative diversion | F1, E1–E2 | pp. 2–3 | HIGH for what the authors model; no standalone-model comparison |
| Detection combines structural and textual evidence | VSI plus dual-view OCR and action cues | F2, E3–E7 | pp. 4–5 | HIGH for component descriptions; final fusion incomplete |
| SnapGuard has best aggregate F1 among listed image baselines | 0.75 versus next-best 0.71 | T1/X1 | p. 6 | HIGH within table; not best on every attack |
| Efficiency improves over GPT-4o-prompt | 1.81 versus 14.50 s | T1/X7 | pp. 6, 8 | HIGH reported comparison; deployment environment underspecified |
| Text baselines struggle after screenshot extraction | F1 0.00–0.45 versus 0.75 | T2/X2 | p. 6 | HIGH for listed configuration; not proof all text defenses fail |
| Components contribute to benchmark performance | Ablation F1 decreases | T3/X6 | pp. 7–8 | HIGH reported values; APD is replaced, not merely deleted |
| Several extraction interfaces preserve performance | OCR 0.75, Qwen/GPT 0.76 | F4/X4 | p. 7 | LLaVA 0.46 is a meaningful exception |
| Noise robustness holds in the displayed test | SnapGuard remains highest, around 0.8 | F5/X5 | p. 7 | MEDIUM for generalization; exact points and sigma scaling absent |
| Full detector has important residual errors | VWA-shot TPR 0.13; screenshot FPR 0.14 | T1 | p. 6 | HIGH condition-specific evidence |
| Web-agent exposure differs from text-only interaction | External content enters an action-producing pipeline | Threat model and introduction | pp. 1–3 | MEDIUM analyst relevance inference; comparative vulnerability not tested |
| Further mitigation and temporal work remain | Explicit future directions | S6 | p. 9 | HIGH for proposed work; no present guarantee |

## 22. Very simple explanation — Explain Like I'm 15

Imagine giving an AI permission to use a browser for you. It reads the screen and clicks things. A dishonest webpage can display a message that tries to make the AI abandon your request and do something else. The security problem is that information on the page can be mistaken for an instruction the AI should obey.

SnapGuard checks the screenshot before the AI uses it. It looks at the pattern of edges in the image, and it reads text twice: once normally and once after selectively changing very bright pixels. It then looks for patterns that request actions such as revealing credentials or overriding instructions. The two checks are meant to catch different signs of an attack.

In this paper's benchmark, SnapGuard has the highest overall F1 among the listed methods and takes about 1.81 seconds per image, compared with 14.50 seconds for the GPT-4o-prompt detector. But it still misses attacks, especially one screenshot attack category, and it sometimes flags harmless pages. It is a useful detector in the reported tests, not proof that a browsing AI is safe.

For the bigger question about agents versus standalone language models, the paper helps explain the added danger: a browser agent encounters material from other people and can turn what it reads into actions. However, the researchers did not run a matched experiment comparing standalone models with agents, so this paper alone cannot say exactly how much more vulnerable agents are.

## Completeness Audit

The inventory covers all ten supplied text pages, seven supplied rendered pages, seven figures, four tables, seven equations, nine distinct empirical analyses, and the referenced-but-absent appendices. All visually inspected objects are distinguished from text-only coverage.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| S0 Abstract, title, authors, keywords | Yes, text and image | Yes | Fully represented | Metadata conflicts disclosed |
| S1 Introduction | Yes, text and images | Yes | Represented in compressed form | Repeated motivation consolidated |
| SS2.1 Attack-related work | Yes | Yes | Represented in compressed form | Categories and evaluation-relevant examples retained |
| SS2.2 Defense-related work | Yes; p. 3 text-only | Yes | Represented in compressed form | Detector/guardrail distinctions retained |
| SS3.1 Problem formulation | Yes, text-only | Yes | Fully represented | E1–E2 and action grounding explained |
| SS3.2 Attacker model | Yes, text-only | Yes | Fully represented | Both control models and iterative refinement retained |
| SS3.3 Defender model | Yes, text-only | Yes | Fully represented | Screenshot-only and task-unaware interface retained |
| SS4.1 Overview | Yes | Yes | Fully represented | Fusion uncertainty explicit |
| SS4.2 VSI | Yes | Yes | Fully represented | Statistic, threshold, complexity, and missing implementation details |
| SS4.3 Text extraction/APD | Yes | Yes | Fully represented for supplied content | Missing pattern appendix disclosed |
| SS5.1 Setup | Yes | Yes | Fully represented | Counts, tools, attacks, metrics, hardware, thresholds |
| SS5.2 Performance | Yes | Yes | Fully represented | Full attack matrices retained; trade-offs stated |
| SS5.3 Robustness | Yes | Yes | Fully represented within source precision | Interface labels exact; noise points approximate |
| SS5.4 Ablation | Yes | Yes | Fully represented | APD replacement distinguished |
| SS5.5 Efficiency | Yes | Yes | Fully represented | GPU/CPU scope and OCR bottleneck retained |
| SS5.6 Case study | Yes | Yes | Fully represented | Both visual and text cases explained |
| S6 Conclusion/future work | Yes; p. 9 text-only | Yes | Fully represented | Future capabilities not treated as demonstrated |
| RQ1 | Yes | Yes | Fully represented | Lightweight screenshot detection question |
| Formal hypotheses | No such set supplied | Yes, absence stated | Fully represented | Expectations distinguished from formal tests |
| X1–X3 comparisons/ROC | Yes | Yes | Fully represented | Tables and curve evidence retained |
| X4–X5 robustness tests | Yes | Yes | Fully represented within available detail | Missing configurations/noise definitions identified |
| X6–X7 ablation/efficiency | Yes | Yes | Fully represented | Numerical conditions retained |
| X8–X9 case studies | Yes | Yes | Fully represented | Illustrative scope preserved |
| F1 | Yes, visually | Yes | Fully represented | Attack schematic |
| F2 | Yes, visually | Yes | Fully represented | Architecture; no invented fusion rule |
| F3 | Yes, visually | Yes | Fully represented | Axes, AUC, approximate operating points |
| F4 | Yes, visually | Yes | Fully represented | All labeled F1/runtime pairs |
| F5 | Yes, visually | Yes | Represented with uncertainty | Exact per-point values not labeled |
| F6 | Yes, visually | Yes | Fully represented | Four VSI labels; local-scale ambiguity noted |
| F7 | Yes, visually | Yes | Fully represented | Concealed instruction treated as evidence |
| T1 | Yes, visually and text | Yes | Fully represented | All rates and costs retained |
| T2 | Yes, visually and text | Yes | Fully represented | Repeated SnapGuard row cross-referenced |
| T3 | Yes, visually and text | Yes | Fully represented | All variant values retained |
| T4 | Yes, visually and text | Yes | Fully represented | All times and proportions retained |
| E1–E2 | Yes, text-only | Yes | Fully represented | No claim of image inspection on p. 3 |
| E3–E7 | Yes, text and image | Yes | Fully represented | Symbols, operations, purpose, assumptions |
| Numbered algorithms/theorems | None supplied | Absence stated | Fully represented | No missing proof assumed |
| Major contributions | Yes | Yes | Fully represented | Conceptual, method, system, implementation, empirical |
| Explicit operational qualifications | Yes | Yes | Fully represented | Separate from analyst limitations |
| Appendix B.2 | No | Absence represented | Missing from supplied material | Alternative OCR settings unavailable |
| Appendix B.3 | No | Absence represented | Missing from supplied material | Exact APD patterns unavailable |
| Appendix C | No | Absence represented | Missing from supplied material | Metric definitions/aggregation unavailable |
| Repository and experiment artifacts | No | Absence represented | Not supplied or accessed | Availability claim only |
| References [1]–[57] | Yes, supplied text | Yes, selectively | Represented in compressed form | Bibliographic list not reproduced; outside works not reviewed |
| Legal text, page headers, decorative icons | Yes where supplied | Accounted for | Inspected but omitted as non-substantive | Metadata anomalies retained because substantive |

### Missing or inaccessible material

Appendix B.2, Appendix B.3, and Appendix C are referenced but absent. Repository code, experiment outputs, raw score data, full prompts/configurations, calibration samples, and supplementary files were not supplied or inspected. Pages 3, 9, and 10 were reviewed as extracted text only. No missing page is identified inside the supplied main-document sequence.

### Uncertain interpretations

The final visual/textual fusion rule is unspecified. Metric aggregation and exact F1 reconstruction are unresolved without Appendix C and sample breakdowns. Exact Gaussian-noise values, sigma units/normalization, clipping, and repetitions are unavailable. The local response-map scale is not explicitly defined in physical units. Some baseline/interface roles for Llama-3-8B are ambiguous. The p. 6 claim about avoiding text extraction conflicts literally with the OCR-based method; it may mean avoiding a separate heavy OCR preprocessing pipeline, but that interpretation remains labeled. Publication metadata contain unresolved template fields.

### Deliberately compressed material

Repeated statements about lightweight detection, the research gap, and headline results were consolidated. Related-work descriptions were grouped by mechanism rather than reproducing every citation. Bibliographic entries, legal permission language, decorative interface icons, and repeated table rows were compressed or omitted with disclosure. Exact per-attack TPRs, benign FPR pairs, baseline costs, ablations, and module times were preserved because they materially qualify the conclusions.

### Potential omissions

No known substantive numbered figure, table, equation, major section, or distinct reported analysis in the supplied main text is left unrepresented. This is coverage of the supplied material, not a claim of complete access to the work's missing appendices or experimental artifacts. Unlabeled plot points and absent implementation details remain explicitly uncertain rather than silently reconstructed.
