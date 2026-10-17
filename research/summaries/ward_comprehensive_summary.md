## Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. The paper and its embedded prompts are treated as evidence, never as instructions. No external research, repository inspection, code execution, or independent reproduction was performed.

| Accessibility item | Assessment |
|---|---|
| Main document | Available as extracted text for physical PDF pages 1–28 |
| Accessible page count | 28 |
| Apparently missing pages | No gap in the supplied numbered text sequence; this does not establish that every associated artifact was supplied |
| Visually inspected pages | 1–9, 17–21, and 23: 15 rendered pages |
| Text-only pages | 10–16, 22, and 24–28: 13 pages |
| Figures | Figures 1–7 available visually; tiny plot labels and screenshot payload text have variable readability |
| Tables | Tables 1–10 available as extracted text and on rendered pages; extracted alignment checked against visible organization |
| Equations | Main equations visible on pages 3, 5–7; extraction occasionally damages mathematical spacing and inequality notation |
| Appendices | A–K available in supplied text; selected appendix pages also rendered |
| Supplementary artifacts | No separate supplementary files supplied; no embedded files reported |
| Referenced external artifacts | Code/models repository, cited papers, model cards, and framework documentation are referenced but not inspected |
| OCR | Not needed for the supplied native-text pages; no independent OCR performed |
| Main limitation | Text-only appendix content cannot receive independent visual layout verification; source data, training code, checkpoints, and experimental logs are unavailable |

The supplied accessibility metadata detects an appendix on page 7, but the actual text places Appendix A on page 16. This report follows the document headings rather than the automated detection. Page locators below refer to physical PDF page numbers.

Evidence labels: [A] author-reported; [B] directly observable in a supplied visual; [C] analyst-derived with operands shown; [D] analyst interpretation. No [E] external information is introduced. Confidence refers to fidelity to supplied evidence, not independent confirmation that the experiments reproduce.

## 1. Plain-language orientation

WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections studies a security problem in AI systems that browse websites and act for users. A web agent receives a legitimate task, observes pages, and clicks, types, or navigates. An attacker can place misleading instructions or apparently helpful information inside the material the agent reads. The agent may then follow the attacker’s intent instead of the user’s. The paper calls this prompt injection. [A; pp. 1–3]

The researchers develop a separate guard model called WARD, expanded as Web Agent Robust Defense against Prompt Injection. It examines the intended task, webpage text derived from HTML, and a screenshot. It predicts whether the observation contains an attack, where that attack appears, what it is trying to accomplish, and supporting reasoning. It runs alongside the agent without needing the agent’s internal reasoning. [A; pp. 3, 5–7, 24]

WARD combines three training stages: a diverse 177,585-sample dataset, an additional dataset that teaches the guard to resist attacks directed at itself, and adaptive adversarial training in which an attacker repeatedly searches for bypasses and the guard learns from successful ones. Compact 0.8B and 2B model variants obtain high detection scores, low measured disruption of benign tasks, and substantially improved resistance to the evaluated adaptive attacks. These results are strong within the reported tests; they are not a guarantee against every attack. [A; pp. 5–9, 16–19]

For the requested research question, this paper supports an explanation of how web interaction broadens the attack surface: untrusted page content enters repeated perception–action steps, may arrive through text or images, and can influence consequential actions. That relevance is analyst inference. The paper does not directly measure whether web agents are more vulnerable than otherwise matched standalone language models. [D; grounded in pp. 2–3]

## 2. Document roadmap

The paper is a mixed machine-learning, cybersecurity, systems, and dataset study, principally experimental rather than theoretical. The main body occupies pages 1–9. The abstract and Introduction establish four practical guard problems: generalization, false positives, efficiency, and adversarial vulnerability. Related Work on pages 2–3 positions WARD among web agents, prompt-injection attacks, and defenses. Problem Formulation on page 3 defines the agent and parallel guard. Data Framework on pages 3–5 explains collection, attack insertion, reasoning annotation, and dataset composition. Training WARD on pages 6–7 defines the three training stages and adaptive feedback loops. Experiments on pages 7–9 report detection, adversarial robustness, utility, and efficiency. The Conclusion appears on page 9.

Acknowledgements and 84 numbered references occupy pages 10–15. They establish attribution and funding, but do not supply independent evidence about the cited works beyond what WARD reports.

Appendix A, page 16, states the principal threat-model limitation. Appendix B, pages 16–19, supplies development, training, evaluation, and ablation details. Appendix C, pages 19–20, compares training datasets. Appendix D, pages 20–21, describes test distributions and discusses generalization. Appendix E, pages 21–22, explains a guard failure. Appendix F, page 23, gives channel distributions. Appendices G–J, pages 24–27, provide training, attacker, validator, and guard-targeting prompts. Appendix K, pages 27–28, discusses broader impacts and mitigation.

The substantive inventory is S1–S7, Appendices A–K, F1–F7, T1–T10, and eight grouped mathematical records E1–E8. Seven experiment groups are distinguished below. There are no numbered theorems, lemmas, formal research questions, hypotheses, or standalone pseudocode algorithms in the supplied paper. The workflow diagrams and prompt specifications are the algorithmic descriptions.

## 3. Background and context

A large language model, or LLM, processes language. A vision-language model, or VLM, also processes visual input. Here a web agent is an LLM/VLM-powered system that observes webpages, reasons about the user’s task, and performs browser interactions. HTML is the associated textual and structural webpage representation; the screenshot is the rendered interface. These two views can expose different content. [A; pp. 2–4]

Prompt injection is an attempt to redirect the agent through external content encountered during execution. The paper distinguishes this from jailbreak-style attacks in which a user directly manipulates a prompt to bypass safeguards. The important boundary is between the legitimate user instruction and material found in the environment. The authors identify webpages, images, and tool outputs as observations whose apparent authority can be exploited. [A; p. 3]

A guard is a separate model that checks an observation for malicious signals. A false positive occurs when benign content is flagged as malicious; this can interrupt legitimate workflows. A false negative occurs when an attack is classified as benign. The paper’s failure case illustrates the latter. Out-of-distribution, or OOD, evaluation tests content or conditions that differ from training. WARD emphasizes changes in websites, platform layouts, channels, modalities, tasks, and attacker models. [A; pp. 2, 8, 17–22]

Supervised fine-tuning, or SFT, trains the model to produce target annotations from examples. WARD’s target includes a label, injection location, attack goal, and reasoning. Adaptive Adversarial Attack Training, abbreviated A3T, repeatedly generates attacks against the current guard and updates the guard from successful bypasses. Prompt Injection on Guard, or PIG, explicitly targets the guard’s own decision process. [A; pp. 5–7]

Retrieval-augmented generation, or RAG, appears among the cross-domain task labels. The supplied paper names these tasks but does not give a detailed definition of RAG. Group Relative Policy Optimization, or GRPO, is the reinforcement-learning training procedure named for A3T; the paper supplies its reward and a simplified expected-reward objective, not a complete optimizer derivation. These terms should not be taken as fully specified algorithms from this document alone.

## 4. Research problem and gap

Existing problem: web agents operate in open environments where adversaries can embed deceptive instructions in visual elements or HTML. The reported possible consequences include data leakage and unauthorized actions. Attacks may mimic legitimate content rather than present obvious hostile commands. [A; pp. 2–3]

Shortcomings attributed to earlier approaches: direct safety training or system-prompt modification can remain insufficient and may harm task performance. Existing guard datasets have narrow domain coverage, particularly for high-risk email, messaging, and social platforms. Text-only guards miss screenshot-only attacks; screenshot-based guards miss HTML-only attacks. Benign tutorials or support content can look instruction-like and trigger false alerts. Some defenses require agent reasoning or predicted actions, preventing parallel execution; others use expensive large models. Guards themselves can be manipulated or bypassed through adaptive attack rewriting. [A; pp. 2–3]

Research gap: the authors seek a single practical guard framework that combines broad multimodal detection, preserved utility, resilience to guard-directed and evolving attacks, and fast parallel deployment. Their proposed response is structured diverse data plus staged adversarial training rather than detection training alone. [A; pp. 2, 6–7]

Scope: WARD primarily addresses malicious intent expressed through textual or visually interpretable webpage content. It does not establish coverage of imperceptible pixel-level attacks, all tool-based attacks, compromised software, or every possible agent architecture. The authors explicitly discuss pixel-level exclusion in Appendix A. [A; p. 16]

Research relevance: repeated environmental observation, multiple interface channels, and action execution offer mechanisms by which web agents may face additional vulnerabilities relative to a simpler direct dialogue. This is a mechanism-level analyst interpretation, not a measured comparative vulnerability ratio. [D; pp. 2–3]

## 5. Research questions / objectives / hypotheses

Explicit formal research questions: none stated in the supplied work. Explicit formal hypotheses: none stated. The following are author-stated objectives and evaluation dimensions, not newly attributed research questions. [A; pp. 3, 7]

| ID | Objective | Corresponding evidence |
|---|---|---|
| O1 | Detect prompt injections across domains and modalities | X1; T1; F1a |
| O2 | Resist attacks aimed at the guard | X3; T2; T8 |
| O3 | Resist iterative adaptive attacks | X4; F4; T8 |
| O4 | Generalize to substantially different adaptive tasks and attackers | X5; T3 |
| O5 | Preserve benign agent utility | X6; T4 and T6 |
| O6 | Run efficiently in parallel | X7; T7; F1c |
| O7 | Establish complementary contributions of training components | Ablation analysis; T8 |

The user’s question, Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis, is an external organizing question for this report. WARD informs its attack-surface and defense portions. It does not contain a controlled standalone-LLM versus web-agent experiment, so it cannot alone establish the comparative premise quantitatively.

## 6. Assumptions / threat model

The system model consists of a legitimate user instruction I, an agent acting through sequential steps, and a multimodal observation x_t = (S_t, H_t). S_t is a screenshot and H_t is associated HTML content. The agent’s action depends on I, the current observation, and history. A guard G examines I and the observation in parallel, without access to the agent’s internal reasoning. [A; p. 3]

The attacker can introduce malicious content in HTML, screenshots, or both, through overlay elements or native content fields such as emails, messages, posts, and comments. Training attack goals include exfiltration, unauthorized actions, policy-violating output, single-step interface manipulation, memory manipulation, and degraded task success. The adaptive attacker receives feedback and uses histories of successful and failed attempts. PIG adds attacks aimed directly at the guard’s verdict. [A; pp. 4, 6–7, 25–27]

The intended user task is the reference against which manipulation is judged. The supplied work does not provide a comprehensive formal trust specification for the browser, operating system, credentials, network, or the guard deployment mechanism. It also does not specify all possible attacker privileges. Absence of these details should not be interpreted as evaluated protection against those capabilities.

Excluded or limited attack class: imperceptible pixel-level environmental perturbations that induce actions without interpretable malicious instructions. Appendix A argues that such attacks require a stronger and less practical capability set, including access to the agent or a surrogate, control over rendering, and per-page optimization. This practicality assessment is the authors’ position, not independently verified here. [A; p. 16]

Utility evaluation assumes all webpage content in the selected WebArena tasks is benign. The validator used in A3T is a proxy-agent quality gate that judges whether an attack could plausibly redirect an agent; passing that gate is not identical to observing an actual agent execute the malicious action. [A; pp. 18, 25–26; D qualification]

## 7. Methodology

### 7.1 Data collection and splitting

The overlay branch starts from the top 50 URLs across 21 Similarweb categories, yielding 808 valid URLs after filtering. Five benign tasks are generated for each URL, totaling 4,040 tasks. A Browser-Use agent executes each task for up to 100 steps or completion, recording paired HTML and screenshots as source tuples (H_0, S_0, I). Filtering criteria beyond validity are not fully specified in the supplied text. [A; pp. 3–4]

The native branch constructs 20 simulated platforms across five categories: collaboration, email, messaging, e-commerce, and social media. Each has 20 benign user tasks. The authors say layouts and interactions match real systems; no independent realism study is reported. [A; p. 4]

The disjoint splits are WARD-Base: 709 URLs and 10 platforms; WARD-Seed: 49 URLs and 4 platforms; WARD-Test: 50 URLs and 6 platforms. The URL counts sum to 808 and platform counts sum to 20. These sums are analyst-derived: 709 + 49 + 50 = 808; 10 + 4 + 6 = 20. The abstract’s 719 URLs and platforms corresponds to 709 + 10, but should not be read as 719 distinct real URLs. Table 10 later reports seven replicated test platforms, creating an unresolved inconsistency. [A/C; pp. 1, 4, 20]

### 7.2 Attack and benign sample construction

Each source observation is expanded into malicious and benign variants while the intended task remains unchanged. Six attack categories are defined. The first five receive 100 curated specific goals each; utility-degradation goals are generated from the particular task. Figure 3 reports 4,615 specific attack goals and 3,745 benign user tasks in WARD-Base. The paper does not provide a complete reconciliation between collected task counts and this training-only retained count. [A; pp. 4–5]

The physical insertion locations are HTML only, screenshot only, or both. None identifies non-injected base examples and is also used as the benign target annotation. For a malicious sample the VLM receives context, task, goal, channel, and modality. For a benign sample it receives the same context and channel setup without the malicious goal. Three candidates at different temperatures are generated and one is randomly selected; the temperatures and random seed are not specified. [A; pp. 4–5]

Seven overlay channels are named: footer, alert, badge, banner, notification, inset chat, and popup. Native fields are described as message, email, post, comment, readme, and product information/description. Figure 7 instead lists review and product description without readme. Consequently the advertised 13-channel vocabulary is not fully consistent across descriptions. [A/B; pp. 4–5, 20, 23]

### 7.3 Reasoning annotations and preprocessing

Gemini-3-Flash generates prompts and reasoning annotations. An iterative generator–evaluator process predicts reasoning, attack goal, location, and label. The evaluator checks label and location against ground truth, without demanding exact attack-goal matching. Correct reasoning is accepted; incorrect predictions receive hints for another iteration. The authors intend this process to encourage reasoning from the observation rather than simply using the answer. No maximum iteration count or human annotation audit is specified. [A; pp. 5, 16]

Screenshots retain original resolution. HTML preprocessing extracts textual content while preserving tag names. The same preprocessing is applied in training and evaluation. Visual channel diversity uses 193 font styles and thousands of background images. The exact number of background images, handling of very long HTML, and image resizing inside model inference are not supplied. [A; p. 16]

### 7.4 WARD-Base and WARD-PIG

WARD-Base contains 177,585 examples: 90,802 benign and 86,783 malicious. Figure 3 partitions injection-location composition into HTML 39,397; screenshot 50,099; both 68,383; none 19,706. These describe dataset composition, while benign final target labels use none; conflating the construction location with the benign target would create an apparent contradiction. [A; p. 5; D interpretation of wording]

WARD-PIG selects 10,500 malicious examples, 3,500 for each of the three attack locations, and adds guard-targeted prompts. It also includes 10,500 benign examples matched across URLs/platforms to preserve utility. Therefore its described total is 21,000 examples, derived as 10,500 + 10,500. Table 9’s shorthand 10.5K PIG omits the benign half rather than clearly stating this full total. [A/C; pp. 6, 16, 20]

### 7.5 Training and adaptive attack generation

The backbone models are Qwen-3.5-0.8B and Qwen-3.5-2B. Full fine-tuning proceeds through one epoch on WARD-Base and one on WARD-PIG. Training uses two NVIDIA H200 GPUs, reported as 140GB, batch size 256, learning rate 3.0 × 10^-5, fused torch AdamW, and a cosine scheduler. Software version numbers, weight decay, precision, and random seeds are not reported. [A; p. 16]

A3T uses three seed subsets for three cycles. Gemini-3-Flash serves as both attacker and validator. Sample memory records previous attempts and feedback; platform memory transfers patterns across the same website or platform. Each base sample allows at most five attempts, stopping after a bypass. Per website/platform, generation seeks ten successful attacks. Benign samples are added proportionally to malicious samples. Exact final adaptive training counts and how unattained collection targets are handled are not supplied. [A; pp. 6–7, 16]

The guard update uses GRPO, rollout n = 6, batch size 24, and one epoch. Correct label plus correct location earns reward 1; correct label with wrong location earns 0.5; otherwise reward 0. The paper gives a simplified expected-reward maximization equation, not full GRPO implementation details. [A; pp. 7, 16]

### 7.6 Baselines, measurement, and repetitions

Detection compares 25 baselines: six closed APIs, six open instruction-tuned models, six jailbreak guards, and seven prompt-injection guards. SnapGuard is discussed but excluded because public source code was unavailable to the authors. Guard experiments are run three times with sampling disabled, producing identical reported results and standard deviation zero. Closed APIs and open instructed models are run once at temperature zero because of resource constraints. This checks fixed-output repetition rather than variation across training runs or attacker populations. [A; pp. 7–8, 16–17; D qualification]

Metrics include accuracy, recall, precision, F1, false positive rate, performance degradation, output tokens, runtime, and attack success measures. The paper uses ASR for different denominators in different experiments; each condition must be read separately. No confidence intervals or formal significance tests are supplied, despite descriptive use of the word significantly. [A/B; pp. 7–9, 17–19]

## 8. Experiments / analyses

### X1 — Detection across datasets

Purpose: test O1, broad detection and generalization. WARD-Test contains 1,500 benign plus 1,500 malicious examples. Popup contains 2,682 of each. EIA, VPI, and WASP contain respectively 1,414, 306, and 84 malicious examples, so their main reported metric is recall. Table 10 identifies modality and platform differences. Twenty-five baselines are evaluated. [A; pp. 7–8, 20]

WARD-0.8B achieves WARD-Test accuracy 99.33%, recall 99.60%, precision 99.07%, F1 99.34%. WARD-2B obtains 99.20%, 99.67%, 98.75%, and 99.20%. Both achieve 100.0% recall on all four external datasets. Popup accuracy remains below 100%: 99.98% and 99.91%, reflecting that perfect attack recall does not imply perfect classification of benign material. [A; T1, p. 7]

### X2 — Actual agent protection on VPI

Purpose: distinguish detection scores from observed end-agent attack success. Table 5 evaluates Computer-Use with Sonnet-3.7 and Browser-Use with Gemini-2.0-pro across Amazon, Booking, BBC, Messenger, and Email. No-defense reported averages are 33.70% and 76.98%; system-prompt averages are 33.02% and 74.98%; GPT-4o guard averages are 13.64% and 23.94%. WARD’s two variants obtain 0.00% in every listed domain and both agent settings. [A; pp. 8, 17]

This is direct empirical defense evidence for these VPI conditions. It does not mean that zero failures have been established for arbitrary web tasks, attack budgets, or architectures. The supplied text does not fully specify the execution rule following a malicious verdict. [D]

### X3 — PIG robustness

Purpose: test O2 by appending misleading guard-output content to malicious observations. The tests cover five datasets and three insertion modalities. Testing prompts imitate WARD JSON or WebAgentGuard’s think/answer structure, with a benign/negative verdict. These testing payloads differ from training prompts; payloads also differ between guards because their output formats differ. [A; pp. 8, 17, 27]

Both final WARD variants show 100.0% recall in all 15 dataset-by-modality cells. Without PIG training, important failures remain: WARD-2B reaches only 17.32% recall for VPI/both and 25.81% for EIA/both. WARD-0.8B without PIG reaches 39.29% for Popup/both. WebAgentGuard-4B reaches 2.50% for Popup/both. These contrasts support training-stage relevance, while the tested attack family remains output-format imitation rather than every possible guard manipulation. [A; T2, p. 8]

### X4 — Adaptive attacks on unseen web environments

Purpose: test O3 across training cycles and increasing attack budgets. The authors reuse the A3T framework with WARD-Test configurations, four samples per unseen URL/platform, Gemini-3-Flash as attack generator, and up to ten attempts per sample versus five in training. Evaluation uses unseen environments but shares the attack-generation family and generator model with training. [A; pp. 8, 17]

At budget ten, final cycle-three sample success rates are 3.12% for 2B and 5.62% for 0.8B, compared with 74.38% and 78.75% for WebAgentGuard variants. Final attempt success rates are 0.34% and 0.62%, compared with baseline values 19.16% and 22.62%. The distinction matters: a sample can eventually be bypassed after several mostly unsuccessful attempts. Figure 4 and Table 8 support substantially reduced vulnerability, not elimination of it. [A/B; pp. 9, 19]

### X5 — Cross-domain adaptive attacks

Purpose: test O4 under changes in task, attack process, and attacker model. PIArena uses text-only tasks, GPT-5.1 as attacker, iterative strategy-based rewriting, population size ten, five initial attempts per strategy, and at most five generations. WARD omits screenshots and receives the full injected context as preprocessed HTML text. There are 1,700 examples across 13 datasets: 200 each for SQuAD v2 and three Dolly tasks, and 100 each for nine other datasets. [A; pp. 17–18]

Table 3 reports per-sample attack success averages of 3.23% and 3.08% for WARD, versus 92.21% PromptArmor, 92.14% PromptGuard, and 45.71% DataSentinel. WARD’s largest individual listed rates are 7% for 0.8B and 9% for 2B. This shows transfer in the tested protocol; it does not compare standalone LLM vulnerability with browser-agent vulnerability. [A; pp. 9, 18]

### X6 — Benign utility

Purpose: test O5 using 802 WebArena tasks across six domains. All content is assumed benign. GPT-4o judges task completion with and without a guard. False positive rate is step-level; performance degradation is task-level. Backbones are GPT-4o, Gemini-3-Flash, and a Claude Sonnet version that is inconsistently named in the text and table. [A; pp. 9, 18]

For GPT-4o trajectories, WARD averages are FPR/PD 0.26%/0.37% for 0.8B and 0.25%/0.25% for 2B, compared with WebAgentGuard-4B 7.17%/5.91% and 8B 13.12%/7.88%. Tables 4 and 6 also show small but nonzero domain-specific disruption. Thus near-zero is accurate descriptive language; zero disruption everywhere would be inaccurate. [A; pp. 9, 18]

### X7 — Efficiency and component ablation

Efficiency tests O6 on benign WebArena and malicious VPI, single NVIDIA H200, batch size one. WARD runtimes are 2.24–2.45 seconds per step across listed conditions, below listed agent API latencies. Output lengths are roughly 128–152 tokens versus roughly 400–469 for WebAgentGuard. Parallelism can hide measured guard computation when the agent is slower; this is conditional on the tested timing and integration. [A; pp. 9, 18–19]

Ablation tests O7 by adding native data, overlay data, PIG, and adaptive training at both scales. Single branches generalize unevenly. PIG raises the shown modality recalls to 100%. Adaptive training reduces budget-ten SSR from 28.75% to 5.62% for 0.8B and 21.88% to 3.12% for 2B. The paper does not provide retraining variance, significance tests, or a fully controlled equal-data-volume comparison. [A/D; T8, p. 19]

## 9. Results

The strongest overall result is consistent performance across several distinct dimensions rather than one isolated benchmark score. Detection remains high on balanced test datasets and attack-only external sets; actual-agent VPI attacks are blocked in the listed settings; PIG training substantially improves resistance to guard-output imitation; A3T reduces adaptive bypass success; utility tests show low false positives; and compact models run faster than the listed agents. [A; pp. 7–9, 17–19]

A few numerical comparisons clarify scale without confusing percentages and percentage points. WARD-0.8B’s WARD-Test accuracy exceeds WebAgentGuard-8B by 99.33 − 91.97 = 7.36 percentage points. This is analyst-derived, not a reported relative improvement. At adaptive budget ten, the 0.8B PIG checkpoint’s SSR drops by 28.75 − 5.62 = 23.13 percentage points after adaptive training; for 2B the drop is 21.88 − 3.12 = 18.76 percentage points. [C; T1 and T8]

The two WARD scales do not exhibit uniform size ordering. The 0.8B variant has slightly higher WARD-Test accuracy and F1 and higher Popup accuracy, while 2B has slightly higher WARD-Test recall, lower final adaptive sample success, and lower cross-domain mean ASR. Neither is best in every utility condition. These small differences lack supplied uncertainty intervals and should not be inflated into a universal scaling conclusion. [B/D; T1, T3, T4, T6, T8]

Perfect external recall must be read with the sample sizes: WASP has 84 malicious examples, VPI 306, EIA 1,414, and Popup 2,682 malicious examples. The first three do not provide a corresponding benign-class test in Table 10. A 100% observed recall is a dataset-specific result, not proof of 100% population recall. [A/D; pp. 7, 20]

## 10. Figure-by-figure interpretation

### Figure 1 — Four-dimensional overview, page 1

Panel a is a grouped bar chart of recall percentage on Popup, EIA, VPI, and WASP, with a vertical 0–100 scale. Four guard variants are distinguished in the legend. Both WARD variants reach 100% in all four groups; baseline bars vary substantially. Panel b compares WebArena false-alert percentages. Panel c compares average output tokens for malicious and benign settings. Panel d plots per-sample adaptive success against trial budget 1–10; WARD curves remain low while baseline curves rise toward roughly three quarters of samples. [A/B]

This overview supports the four evaluation dimensions but compresses detailed tables. Its rounded utility labels are not straightforward matches to Table 4’s GPT-4o averages; the aggregation is not specified. Exact interpretation therefore uses Tables 4, 6, and 7. The adaptive panel concerns sample success, not Figure 4’s attempt-level rates. No uncertainty bars are visible.

### Figure 2 — Framework diagram, page 4

The diagram joins two data sources: web exploration with an agent and human-developed native platforms. Data sampling combines task, attack goal, location, and channel to produce malicious and benign HTML/screenshot examples. Data collections feed reasoning generation through a generator/evaluator loop. SFT first uses WARD-Base, then WARD-PIG. A final adaptive loop connects attacker, validator, guard, memory, and new data collection. [B]

The arrows show both forward training flow and repeated feedback. This is substantive architecture evidence, not a decorative illustration. Some tiny labels are easier to resolve from accompanying text than from the diagram itself; exact training hyperparameters come from Appendix B rather than the drawing.

### Figure 3 — WARD-Base composition, page 5

A statistics panel lists 177,585 samples, 709 URLs, ten platforms, 4,615 specific goals, 13 channels, and 3,745 benign tasks. Three pie charts show location, malicious goal type, and benign/malicious composition. Pie charts have no Cartesian axes; sector size encodes proportion and legends identify categories. [A/B]

Locations are HTML 22.2%/39,397; screenshot 28.2%/50,099; both 38.5%/68,383; none 11.1%/19,706. Malicious goals are unauthorized actions 21.5%/18,690; exfiltration 20.6%/17,838; single-step UI manipulation 19.9%/17,277; policy-violating content 13.1%/11,355; memory manipulation 13.1%/11,333; utility degradation 11.9%/10,290. Label composition is benign 51.1%/90,802 and malicious 48.9%/86,783. These are exact supplied labels, not estimates from sector geometry. Rounded percentages need not sum exactly to 100.

### Figure 4 — Adaptive training and attack budget, page 9

Four line plots share trial budget 1–10. First and second panels show sample success percentage for 2B and 0.8B, respectively, with a 0–80 vertical scale. Third and fourth show attempt success percentage on a 0–32 scale. The legend distinguishes WARD cycles 0–3 and WebAgentGuard-4B/8B. There are no visible error bars. [A/B]

At budget ten, 2B sample-success labels across cycles 0–3 are 21.88, 13.75, 8.75, 3.12; 0.8B values are 28.75, 20.62, 10.62, 5.62. Corresponding attempt-success labels are 2B 2.65, 1.59, 0.98, 0.34 and 0.8B 3.69, 2.48, 1.22, 0.62. Baseline endpoint labels are 74.38/78.75 for sample success and 19.16/22.62 for attempt success. These endpoints are reported labels. Intermediate curve positions are visually indicative and are not transcribed as exact numbers.

### Figure 5 — Popup examples across datasets, page 20

Two screenshots contrast a training popup with a Popup-benchmark example. The training example is integrated into a dark media-style page; the benchmark example shows a centered dialog over a different page. Layout, color, placement, and integration visibly differ. [B]

The figure illustrates that a common channel name does not imply identical appearance. It does not by itself quantify distributional independence or rule out all memorization. Small screenshot wording is not confidently readable visually; no payload transcription is inferred from it. [D]

### Figure 6 — Task-aligned failure, page 21

A marketplace screenshot shows a recommendation box highlighted by a red boundary. The caption and nearby text explain that the box supplies a fabricated list of ten Berlin bike listings below 200 EUR. The legitimate task asks for the first ten matching listings with title, price, and neighborhood. The guard predicts benign because the content resembles helpful, task-aligned site assistance. [A/B]

The visual confirms contextual placement, while the detailed attack semantics come from the caption and prose. Tiny individual listing text is not independently readable. This supports a specific failure mechanism: credible information substitution can degrade utility without an obvious instruction override. Page 22 discusses the narrow boundary with benign recommendations.

### Figure 7 — Channel distributions, page 23

Two pie charts show overlay and native channel composition. Overlay sectors are None 19,706/13.7%; Alert Box 17,051/11.9%; Footer Text 17,010/11.8%; Badge 17,001/11.8%; Popup 22,592/15.7%; Notification 16,852/11.7%; Inset Chat 16,706/11.6%; Banner 16,690/11.6%. Native sectors are Message 12,193/35.9%; Email 12,186/35.9%; Comment 3,600/10.6%; Post 3,599/10.6%; Review 1,200/3.5%; Product Description 1,199/3.5%. [A/B]

The charts show relatively even overlay representation aside from popup and a native branch dominated by messages/emails. Analyst-derived totals are 143,608 overlay and 33,977 native; together 177,585, matching WARD-Base. The native vocabulary differs from the readme-based prose description. None is a non-injection category, so counting all eight overlay sectors as attack channels would be misleading.

## 11. Table-by-table interpretation

### Table 1 — Detection comparisons, page 7

Rows group 25 baselines and two WARD models. Columns give accuracy, recall, precision, and F1 for WARD-Test and Popup, then recall for EIA, VPI, and WASP. All are percentages. WARD’s exact core scores appear in X1. The strongest baseline depends on metric: for example Gemini-3-Flash has WARD-Test accuracy 96.37%, while Gemma-4-31B precision is 99.28%. WARD is strongest overall but not uniquely best in every individual column; several API models also have 100% EIA or WASP recall.

General jailbreak guards perform poorly in these prompt-injection conditions; some record zero recall. This is evidence about task mismatch in this evaluation, not proof that those guards fail at their intended safety tasks. Precision/F1 zeros appear where no useful malicious classification is produced, but zero-denominator conventions are not specified. No significance markers or confidence intervals are shown.

### Table 2 — Guard-targeted attacks, page 8

Six rows compare WebAgentGuard-4B/8B, WARD variants without PIG, and final WARD. Fifteen recall columns cross five datasets with HTML, screenshot, and both. Final WARD ties at 100.0% throughout. Without PIG, performance varies markedly by modality and dataset. The full baseline matrix is deliberately compressed; representative severe failures are retained in X3. Recall alone does not assess false alerts under these adversarial additions.

### Table 3 — Cross-domain adaptive success, page 9

Five defense rows span 13 dataset/task columns and an Average column; lower per-sample attack success percentage is better. WARD-0.8B’s sequence is 2, 7, 3, 6, 7, 3, 4, 6, 0, 2, 1, 0, 1; WARD-2B’s is 1, 8, 2, 9, 6, 3, 2, 6, 0, 1, 1, 0, 1. Dataset order is SQuAD v2; Dolly closed QA, information extraction, summarization; NQ RAG; MSMARCO RAG; HotpotQA RAG; HotpotQA Long; Qasper; GovReport; MultiNews; Passage Retrieval; LCC.

The displayed averages are consistent with unweighted dataset means: 42/13 = 3.2308% and 40/13 = 3.0769%, rounded to 3.23%/3.08%. This is analyst-derived verification. With unequal dataset sizes, these are not automatically the pooled rate across 1,700 samples. Using displayed rates and sample sizes gives approximate pooled rates 60/1700 = 3.53% and 60/1700 = 3.53%, but this calculation relies on displayed dataset percentages being exact; the reported averages should remain the primary values. No uncertainty estimates are shown.

### Table 4 — GPT-4o utility, page 9

Rows compare four guards across GitLab, Map, Reddit, Shopping, Admin, and Wikipedia, plus averages. FPR and PD are percentages with lower preferred. There are 7,605 steps. WARD’s largest displayed domain PD is Reddit 1.55% for both variants; many other cells are zero. Baseline disruption is substantially larger. Aggregate averages should not be assumed to be simple arithmetic means: domain step/task counts are not supplied. The table does not establish that every benign content category is safe from false positives.

### Table 5 — VPI agent attack success, page 17

Two agent blocks each contain five domains and an average. Seven defense rows cover none, system prompt, GPT-4o guard, WebAgentGuard variants, and WARD variants. All WARD cells are 0.00%. Baseline WebAgentGuard averages remain 3.78%/5.34% for Computer-Use and 2.68%/3.32% for Browser-Use. System prompting sometimes worsens a domain relative to no defense, such as Computer-Use Amazon 42.20% versus 31.70%. That condition-specific observation should not be generalized into a universal harm from system prompts.

### Table 6 — Additional utility backbones, page 18

The same domain metrics are reported for Claude 3.7 Sonnet, 7,344 steps, and Gemini 3 Flash, 7,392 steps. Claude averages FPR/PD are WARD-0.8B 0.20%/0.25%, WARD-2B 0.22%/0.38%, versus baseline 4B 5.27%/6.51% and 8B 11.55%/9.76%. Gemini averages are WARD-0.8B 0.35%/0.37%, WARD-2B 0.24%/0.37%, versus 4B 5.05%/9.00% and 8B 13.62%/11.47%. Nearby prose names Claude 3.5 Sonnet instead; the tested version is unresolved.

### Table 7 — Runtime and tokens, page 19

Benign WebArena guards: WARD-0.8B 131.45 tokens/2.24 s; WARD-2B 127.67/2.37; WebAgentGuard-4B 399.73/8.81; 8B 417.97/10.03. Malicious VPI guards: WARD-0.8B 150.63/2.37; WARD-2B 152.35/2.45; baseline 4B 440.26/9.65; 8B 468.75/9.63. Agent token counts use a dash, meaning unreported rather than zero.

WebArena agent times are Claude-3.7-Sonnet 11.99 s, GPT-4o 4.84 s, Gemini-3-Flash 3.64 s. VPI agent times are Claude-3.7-Sonnet 7.35 s, GPT-4o 6.03 s, GPT-4.1 5.43 s. All listed WARD times are below the corresponding agent times. API latency and local GPU inference are different measurement environments; the table supports the reported parallel timing condition without providing full deployment-cost accounting.

### Table 8 — Component ablation, page 19

For both scales, rows add native, overlay, combined data, PIG, and AAA. Detection columns are recall, not accuracy; the WARD column’s final values 99.60%/99.67% therefore match Table 1 recall rather than its accuracy. Single native versus overlay branches have complementary weaknesses: 0.8B native Popup 81.17% versus overlay 100%; native VPI 99.35% versus overlay 76.47%. For 2B, native WASP is 100% versus overlay 85.71%.

PIG recalls become 100% after PIG training. Adaptive SSR improves as stated in X7. Dashes denote unreported/not evaluated cells, not zero. The PIG columns do not identify clearly in the table header how performance is aggregated across datasets. Claims that each stage is necessary are stronger than a universal necessity proof; the evidence is component benefit under these tested configurations.

### Table 9 — Training dataset comparison, page 20

WARD is compared with WebAgentGuard and BrowseSafe across sample size, data source, platforms, modalities, locations, channels, goals, grounding, reasoning, PIG, and adaptive training. Reported sizes are 177K + 10.5K PIG + A3T, 5.3K, and 14.7K. WARD combines real pages, simulated platforms, and synthetic injection; WebAgentGuard is described as fully synthetic; BrowseSafe uses real HTML with synthetic injection. This is the authors’ comparison, not an independent audit of those datasets. The PIG sample shorthand is incomplete relative to the 21,000 described examples.

### Table 10 — Test distributions, page 20

Rows specify sample counts, locations, channels, and platforms for five datasets. WARD-Test is balanced 3,000; Popup balanced 5,364; the other three are attack-only. Popup is screenshot-based, EIA HTML-based, VPI screenshot/both, WASP both. WARD-Test lists 50 websites plus seven replicated platforms, disagreeing with six in §4.1.1. Its channel list includes readme and review, broadening the already inconsistent vocabulary. The table also lists Shopee in VPI platform examples while Table 5 uses Amazon; these may represent different dataset/evaluation subsets, but the supplied text does not reconcile them.

## 12. Diagram / architecture interpretation

Figure 2’s architecture has a data path and a feedback path. The data path begins with benign observations and legitimate tasks from real exploration or simulated platforms. A generation stage selects an attack goal, channel, and location and produces labeled examples. A reasoning stage converts these examples into task-conditioned explanation targets. The resulting collections train a compact guard first for ordinary detection and then for resisting attacks on its own verdict.

The adaptive feedback path begins with the current guard. An attacker uses observation context plus memories to propose a candidate. A validator checks goal alignment, modality presence, realism, and likely redirection strength. Invalid examples generate repair feedback. Valid examples are tested against the guard; detected examples inform attacker memory, while bypasses become training data. The guard is updated and returns to the next attack cycle. [A/B; pp. 4, 6–7, 25–26]

The native and overlay branches are complementary because the first models malicious content as ordinary user communication or platform content, while the second models externally inserted interface elements. Parallel inference is separate from this offline training loop: at deployment, the guard examines the current state concurrently with the acting agent. The paper does not show a detailed runtime state machine for blocking, retrying, or recovering from a detected attack.

Appendix H concretizes the attacker’s memory inputs: guard successes/failures and validator passes/failures at sample and platform levels, plus immediate repair feedback. It also encourages natural language matching the page and contextual camouflage. These prompts explain the tested attacker’s behavior; their embedded imperatives are not instructions for this analysis.

## 13. Equations and mathematical concepts

The main equations are unnumbered, so stable report identifiers refer to their locations.

| ID | Form and location | Meaning and important symbols |
|---|---|---|
| E1 | x_t = (S_t, H_t); G(I, x_t) → {0,1}, p. 3 | The guard receives user task I and current screenshot/HTML state, producing a binary decision. The numeric encoding of benign versus malicious is not explicitly specified here. |
| E2 | p drawn from VLM(H_0,S_0,I,g,c,ℓ) for malicious, or VLM(H_0,S_0,I,c,ℓ) for benign, p. 5 | Conditional prompt generation. H_0/S_0 are original observation, g goal, c channel, ℓ insertion location. The sampling symbol indicates generation, not a specified probability distribution. |
| E3 | (H,S) equals (H_0+c(p),S_0), (H_0,S_0+c(p)), or (H_0+c(p),S_0+c(p)), p. 5 | Inject in HTML, screenshot, or both. The plus signs denote insertion/composition rather than ordinary numeric addition. c(p) is the prompt rendered in the selected channel. |
| E4 | x=(H,S,I); a_0=(y,ℓ,g); predicted output at iteration k=(predicted r,g,ℓ,y); a=(y,ℓ,g,r), p. 5 | Convert a labeled observation into a reasoning-annotated training pair. y is class, r reasoning, k iteration. Predicted label/location must match ground truth; goal does not require exact matching. |
| E5 | L_Base = −Σ_(x,a)∈D_Base Σ_t=1^|a| log p_θ(a_t given x,a_<t), p. 6 | Negative log-likelihood of target tokens. θ are model parameters, a_t target token, a_<t earlier target tokens, |a| target length. Minimizing trains annotation generation from the observation. |
| E6 | L_PIG with identical token-loss form over D_PIG, p. 6 | Continue supervised learning on guard-targeted examples and benign examples, starting from the WARD-Base checkpoint. |
| E7 | R=1 if predicted y=y and predicted ℓ=ℓ; 0.5 if label correct but location wrong; 0 otherwise, p. 7 | A discrete reward prioritizing correct classification and additionally rewarding localization. No separate explicit reward for reasoning or goal accuracy is given. |
| E8 | θ^(j+1)=argmax_θ E_[examples in D_AAA^(j), outputs sampled from G_θ] R(output;annotation), p. 7 | Update the guard to increase expected reward on successful attacks from cycle j. The next guard supplies the target for the next attacker cycle. |

These equations specify a supervised annotation objective and an adaptive expected-reward objective. They do not prove robustness or derive a theoretical bound. The expectation in E8 depends on collected examples and generated outputs. The paper names GRPO as the implemented procedure but omits several details required for an exact implementation, including the full policy objective, reference-policy treatment, and optimization settings beyond the reported rollout/batch/epoch counts.

Important notation caution: x_t on page 3 is ordered screenshot then HTML, whereas training x on page 5 is ordered HTML, screenshot, task. This is a representation change, not evidence of a different modality set. Symbol a_t refers to agent action in the formulation and target token in the loss discussion; the context must disambiguate it.

## 14. Interpretation and discussion

The results address each objective through a distinct test. T1 supports multimodal/domain detection, T2 supports resistance to the evaluated guard-directed outputs, F4 supports adaptive-cycle improvement, T3 supports cross-task transfer, T4/T6 support preserved benign utility, and T7 supports fast inference under measured conditions. T8 connects the training design to these improvements. There are no formal hypotheses to declare supported or rejected.

The paper’s strongest methodological lesson is that a guard also consumes untrusted material and therefore requires its own adversarial protection. A separate model does not automatically create a secure boundary. PIG evaluation makes this explicit, and the no-PIG rows show substantial residual susceptibility even for otherwise strong WARD detection models. [A/D; pp. 6, 8]

The supplied failure case changes how the security problem should be understood. Harm may come from fabricated task-relevant content that appears useful, not only commands telling the agent to ignore its instructions. The authors explain that aggressive detection of this pattern could also flag legitimate assistance. This makes utility and security jointly important rather than interchangeable metrics. [A; pp. 21–22]

Cross-reference issues remain unresolved: six versus seven WARD-Test platforms; Claude 3.5 versus 3.7 in utility; native readme versus review channel vocabulary; PIG 10.5K shorthand versus 21K full construction; Figure 1’s unspecified utility aggregation; and VPI platform naming across Tables 5/10. The text also uses ASR for per-sample success in VPI/PIArena but for per-attempt success in Figure 4. These are condition changes that require explicit denominators, not automatically contradictory results.

OOD evidence is substantial but bounded. Website/platform splits and externally adopted datasets reduce direct reuse by design. Sharing A3T and Gemini-3-Flash between adaptive training and one evaluation leaves attack-family dependence; PIArena adds a useful different framework and attacker. The authors’ assertion that contextual variation prevents simple memorization is an interpretation supported by design and examples, not a direct memorization test. [A/D; pp. 17–21]

## 15. Contributions and novelty

Dataset contribution: WARD-Base combines real webpage observations with simulated high-risk platforms, structured attack goals, injection modalities, benign counterparts, and reasoning annotations. WARD-PIG adds guard-directed malicious content while retaining benign examples. [A; pp. 4–6]

Methodological contribution: a two-branch collection pipeline and generator–evaluator reasoning process make the training data task-conditioned and multimodal. The data design explicitly models interface channels and malicious objectives rather than treating all attacks as an undifferentiated class. [A; pp. 4–5, 19–20]

Algorithmic contribution: A3T couples memory-assisted attack search, a proxy validator, and guard updates across cycles. Sample and platform histories enable reuse and refinement of attack strategies. [A; pp. 6–7]

Systems contribution: compact 0.8B/2B guards operate independently of agent internal reasoning and are fast enough in the reported timing tests to run in parallel. Empirical contribution: detection, PIG, adaptive, cross-domain, utility, efficiency, and ablation evidence are evaluated separately. Implementation availability is claimed through the page-1 repository link, but contents, license, and completeness were not checked.

The paper does not claim a new formal theorem or a controlled causal comparison of standalone LLM and web-agent vulnerability. Novelty relative to all outside literature is not independently assessed in this closed-document analysis.

## 16. Limitations

### Authors’ stated limitations

Appendix A states that WARD may not be effective against imperceptible pixel-level environmental attacks lacking explicit interpretable instructions. Appendix E demonstrates a task-aligned fabricated recommendation that the guard accepts as benign. Page 22 explains that stronger detection of such borderline content would likely increase false positives. Appendix K acknowledges dual-use risks from adversarial generation, false positives, reliance on a limited threat model, and possible false confidence from over-reliance on guards. [A; pp. 16, 21–22, 27–28]

The authors also disclose an unavailable SnapGuard baseline and resource-constrained single runs for closed/open instructed models. These are evaluation limitations rather than necessarily failures of WARD itself. [A; p. 17]

### Additional evidence-based analyst observations

Training/annotation relies heavily on Gemini-3-Flash, including attacker and validator roles. The supplied material provides no human validation agreement, annotation error audit, or sensitivity to alternative teachers. Adaptive validation measures plausible agent deception; it does not necessarily verify every bypass through actual agent execution. [D; pp. 16, 25–26]

Some test sets are small and malicious-only. No confidence intervals or across-training-seed variation are provided. Equal-data-size ablations, deployment costs, operational blocking policy, and performance on much longer or denser webpages are not fully specified. Several dataset/version inconsistencies weaken exact reproduction. These are analyst observations, not admissions attributed to the authors.

## 17. Threats to validity

These validity categories are analytical organization; the authors do not systematically use these labels.

Internal validity: staged ablation associates PIG/A3T additions with improvements, but changing data, training stages, and example counts together limits isolation of the precise causal ingredient. Shared attacker/validator models could reinforce common judgments. Deterministic repeated inference does not address training variability. [D]

Construct validity: attack recall, actual agent attack success, proxy-validator judgments, and utility degradation measure related but distinct properties. The fabricated-list failure shows that detecting instruction manipulation and establishing information truth are not identical. Assuming all WebArena content benign is a evaluation convention. GPT-4o completion judgment introduces a model-based outcome measurement. [A/D; pp. 18, 21–22]

External/ecological validity: broad website and modality coverage improves relevance, but simulated platforms, synthetic injected prompts, selected datasets, bounded attempts, and limited backbone combinations do not represent all deployment conditions. Cross-domain testing helps address task/attacker shifts while remaining within one specified PIArena protocol. [D]

Statistical conclusion validity: reported zero standard deviation reflects repeated deterministic outputs. It does not yield population confidence intervals or uncertainty over data sampling. Descriptive superiority is evident in many tables, but formal statistical significance is not established. Cross-domain dataset averages should be distinguished from pooled sample averages. [D]

Reproducibility: several key hyperparameters are supplied, and training/testing prompts are available. Missing software versions, seeds, exact adaptive collection sizes, preprocessing edge cases, and inconsistent platform/model names prevent a fully specified reproduction from the paper alone. No repository or raw logs were reviewed. [D]

## 18. Future work and open questions

### A. Explicit author proposals

Appendix K recommends defensive deployment alongside other security measures, continuous evaluation under evolving threat models, transparency about failures, and cautious integration. It proposes exploring safeguards against misuse of adversarial generation and improving robustness against broader attack classes. These proposals are visible on pages 27–28. The paper does not provide a detailed future-work schedule or new experiment results for them.

### B. Analyst open questions

How well does robustness transfer to unseen attack generators, much larger query budgets, or different memory strategies? Can task-aligned fabricated information be detected without treating genuine recommendations as malicious? How much of the benefit comes from more examples versus channel diversity, reasoning, or adversarial objectives? What happens with missing modalities, very long HTML, dense screenshots, multilingual content, or changing page layouts? What enforcement mechanism prevents an action when a guard flags content? [D]

For the user’s comparative question, the remaining essential experiment would hold the underlying model and malicious objective constant while varying standalone interaction versus web observation and action. WARD does not supply that experiment. Its cross-domain guard test evaluates defense transfer, not the causal vulnerability increase produced by agency. [D]

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| Web agent | AI that observes websites and performs interactions for a user |
| LLM | Large Language Model; language-processing backbone |
| VLM | Vision Language Model; model using text and visual input |
| Prompt injection | External content trying to redirect behavior away from intended user task |
| Jailbreak | Direct prompt manipulation intended to bypass safeguards; related but distinguished by authors |
| WARD | Web Agent Robust Defense against Prompt Injection |
| Guard | Separate model classifying observations for attacks |
| HTML / screenshot | Textual-structural webpage evidence / rendered visual evidence |
| Overlay branch | Attacks inserted through webpage/interface elements |
| Native branch | Attacks embedded in ordinary platform content fields |
| Channel c | Interface element or content field carrying the prompt |
| Location ℓ | HTML, screenshot, both, or none |
| Goal g | Intended malicious effect |
| I | Legitimate user task |
| H_0, S_0 / H, S | Original / modified HTML and screenshot |
| y, r | Class label / reasoning annotation |
| PIG | Prompt Injection on Guard, attacking the detector’s own verdict |
| A3T / AAA | Adaptive Adversarial Attack Training / adaptive adversarial attacks |
| SFT | Supervised fine-tuning on target outputs |
| GRPO | Named policy-optimization procedure; full mechanics not supplied |
| OOD | Out-of-distribution: evaluation differs from training |
| Recall | Fraction of malicious examples detected |
| Precision | Fraction of positive detections that are malicious |
| Accuracy / F1 | Overall correct classification / combined precision-recall score |
| FPR | False positive rate; step-level in utility tests |
| PD | Performance degradation; task-level in utility tests |
| SSR | Sample success rate under repeated adaptive attempts |
| ASR | Attack success rate; per attempt in F4, per sample in T3/T5 |
| θ, D, j, k | Model parameters, dataset, adaptive cycle, reasoning iteration |
| QA / UI | Question answering / user interface |
| RAG | Retrieval-augmented generation; named task class, not elaborated here |
| B / K / M suffixes | Billions / thousands / millions in model or dataset naming |

## 20. Key numerical results

Values retain their source precision. Percentages are observed study results, not guarantees.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Valid collected URLs | 808 | URLs | Overlay source after filtering | Author-reported | p. 3 |
| Generated exploration tasks | 4,040 | tasks | Five per URL | Author-reported | p. 4 |
| WARD-Base | 177,585 | examples | Training dataset | Author-reported | p. 5, F3 |
| Benign / malicious | 90,802 / 86,783 | examples | WARD-Base | Author-reported | p. 5 |
| WARD-PIG full described size | 21,000 | examples | 10,500 malicious + 10,500 benign | Analyst-derived | p. 6 |
| WARD-Test size | 3,000 | examples | 1,500 + 1,500 | Analyst-derived | p. 20, T10 |
| Popup size | 5,364 | examples | 2,682 + 2,682 | Analyst-derived | p. 20, T10 |
| EIA / VPI / WASP | 1,414 / 306 / 84 | malicious examples | External detection | Author-reported | p. 20 |
| WARD-Test accuracy | 99.33 / 99.20 | % | 0.8B / 2B | Author-reported | p. 7, T1 |
| WARD-Test recall | 99.60 / 99.67 | % | 0.8B / 2B | Author-reported | p. 7, T1 |
| WARD-Test F1 | 99.34 / 99.20 | % | 0.8B / 2B | Author-reported | p. 7, T1 |
| External recall | 100.0 | % | Both WARD models, four external sets | Author-reported | p. 7, T1 |
| VPI protected-agent ASR | 0.00 | % | Both models, both agents, five domains | Author-reported | p. 17, T5 |
| PIG recall | 100.0 | % | Both models, 15 conditions each | Author-reported | p. 8, T2 |
| Final adaptive SSR | 5.62 / 3.12 | % | 0.8B / 2B, budget ten | Author-reported | pp. 9, 19 |
| Final adaptive attempt ASR | 0.62 / 0.34 | % | 0.8B / 2B, budget ten | Author-reported | p. 9, F4 |
| Cross-domain samples | 1,700 | examples | 13 datasets, PIArena | Author-reported | p. 18 |
| Cross-domain mean ASR | 3.23 / 3.08 | % | 0.8B / 2B, dataset averages | Author-reported | pp. 9, 18 |
| Baseline cross-domain ASR | 92.21 / 92.14 / 45.71 | % | PromptArmor / PromptGuard / DataSentinel | Author-reported | p. 18 |
| Utility tasks | 802 | tasks | WebArena, six domains | Author-reported | pp. 9, 18 |
| GPT-4o utility FPR | 0.26 / 0.25 | % | 0.8B / 2B | Author-reported | p. 9, T4 |
| GPT-4o utility PD | 0.37 / 0.25 | % | 0.8B / 2B | Author-reported | p. 9, T4 |
| Benign guard runtime | 2.24 / 2.37 | seconds | 0.8B / 2B, H200, batch one | Author-reported | p. 19, T7 |
| Malicious guard runtime | 2.37 / 2.45 | seconds | 0.8B / 2B, H200, batch one | Author-reported | p. 19, T7 |
| SFT learning rate | 3.0 × 10^-5 | rate | Full fine-tuning | Author-reported | p. 16 |
| SFT / GRPO batches | 256 / 24 | examples | Different training stages | Author-reported | p. 16 |
| WARD-Test platform count | 6 versus 7 | platforms | Methods versus T10 | Author-reported inconsistency | pp. 4, 20 |

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Open web observations create attack surfaces | Formulation and described visual/HTML injection | E1; methods | pp. 2–4 | High source confidence; mechanism description, not standalone comparison |
| Diverse data supports broad guard training | 177,585 examples, two branches, structured labels | F2/F3; T9 | pp. 4–5, 19–20 | Counts strong; annotation quality not independently audited |
| Final detection is strong | High balanced-set scores, 100% external recall | T1; X1 | pp. 7–8 | Dataset-specific; some sets malicious-only |
| Guard itself needs protection | Severe no-PIG failures, final 100% recalls | T2; X3 | p. 8 | Strong within output-imitation attack family |
| Adaptive training reduces bypasses | Cycle trends and lower final SSR | F4/T8; X4 | pp. 9, 19 | Shared framework/generator in web adaptive test |
| Defense transfers across tasks/attacker | Low PIArena dataset-average ASR | T3; X5 | pp. 9, 17–18 | Text-only protocol; not a standalone vulnerability comparison |
| Benign utility is largely preserved | Low FPR/PD across listed backbones | T4/T6; X6 | pp. 9, 18 | Benign assumption, model-based completion judgments |
| Measured parallel deployment is feasible | Guard times below agent times | T7; X7 | pp. 18–19 | Hardware and latency conditions matter |
| Residual semantic camouflage can bypass | Fabricated task-aligned recommendation | F6; Appendix E | pp. 21–22 | Specific qualitative failure, not estimated prevalence |
| Threat coverage is bounded | Explicit pixel-level limitation | Appendix A/K | pp. 16, 27 | Authors acknowledge exclusion |
| Relevance to comparative research question | Repeated multimodal observations plus action loop | §3 and attack descriptions | pp. 2–3 | Analyst inference; no matched comparative experiment |

## 22. Very simple explanation — Explain Like I’m 15

Imagine asking an AI assistant to find a bicycle online. It reads a page and clicks around to help you. Someone else can edit part of that page. They might write a command telling the assistant to send information somewhere, or place a convincing box that appears to give exactly the bicycle results you wanted. The assistant has to use the page as information without letting the page become its boss.

WARD is a second AI that checks what the browsing assistant sees. It looks at your task, the webpage text, and a screenshot. The researchers trained it on many different pages and fake attacks. They also trained it to ignore fake verdicts telling the checker that an unsafe page is safe, then repeatedly searched for attacks that still fooled it and used those attacks for more training.

In the reported tests, this checker caught nearly all attacks, interrupted very few harmless tasks, and ran quickly enough to work alongside the browsing assistant. But it could still be fooled by a fake recommendation that looked helpful and matched the task. It also was not designed to catch every kind of hidden pixel manipulation.

This helps explain why browsing AI can face extra security problems: it repeatedly reads material controlled by other people and can act on that material. The paper does not directly compare the same AI with and without browsing, so it supports this explanation of the mechanism rather than proving how much more vulnerable browsing makes it.

## Completeness Audit

Coverage is judged against the supplied inventory, not length. All 28 pages were inspected as text; 15 were also inspected visually. Major values and claims were checked against their supplied page/table conditions. This is source-grounded verification, not independent experimental reproduction.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/affiliations/preprint | Yes | Yes | Represented in compressed form | Title retained; authors listed below |
| Abstract | Yes, text/visual | Yes | Fully represented substantively | Four goals and three training components |
| S1 Introduction | Yes, text/visual | Yes | Fully represented substantively | Problem and four guard gaps |
| S2 Related Work | Yes, text/visual | Yes | Represented in compressed form | Categories and relevant baselines; citation-by-citation descriptions compressed |
| S3 Problem Formulation | Yes, text/visual | Yes | Fully represented | System and E1 |
| S4 Data Framework | Yes, text/visual | Yes | Fully represented substantively | Collection, generation, annotation, composition |
| §4.1 and §4.1.1 | Yes | Yes | Fully represented | Sources and splits |
| §4.1.2 | Yes | Yes | Fully represented | Goals, locations, channels, generation |
| §4.2 | Yes | Yes | Fully represented | Reasoning/evaluator loop |
| §4.3 | Yes | Yes | Fully represented | Dataset statistics |
| S5 Training | Yes, text/visual | Yes | Fully represented substantively | Three stages |
| §5.1 and §5.2 | Yes | Yes | Fully represented | SFT objectives and PIG |
| §5.3 | Yes | Yes | Fully represented substantively | Adaptive search, memory, validator, reward |
| S6 Experiments | Yes, text/visual | Yes | Fully represented substantively | Separate experiment conditions |
| §6.1 | Yes | Yes | Fully represented | Detection and agent protection |
| §6.2 | Yes | Yes | Fully represented | PIG, web adaptive, cross-domain |
| §6.3 and §6.4 | Yes | Yes | Fully represented | Utility and efficiency |
| S7 Conclusion | Yes | Yes | Represented in compressed form | Claims and qualifications retained |
| Explicit RQs/hypotheses | Assessed | Yes | Not present | Objectives retained without inventing formal questions |
| X1 detection | Yes | Yes | Fully represented substantively | T1/T10 |
| X2 agent defense | Yes | Yes | Fully represented substantively | T5 |
| X3 PIG | Yes | Yes | Fully represented substantively | T2/J |
| X4 adaptive web | Yes | Yes | Fully represented substantively | F4/T8 |
| X5 cross-domain | Yes | Yes | Fully represented substantively | T3/B.2.2 |
| X6 utility | Yes | Yes | Fully represented substantively | T4/T6 |
| X7 efficiency/ablation | Yes | Yes | Fully represented substantively | T7/T8 |
| F1 | Yes, visual/text | Yes | Represented with uncertainty | Utility aggregation unclear |
| F2 | Yes, visual/text | Yes | Fully represented substantively | Architecture and feedback |
| F3 | Yes, visual/text | Yes | Fully represented | Composition labels retained |
| F4 | Yes, visual/text | Yes | Represented in compressed form | Exact endpoints retained, intermediate coordinates omitted |
| F5 | Yes, visual/text | Yes | Represented with uncertainty | Tiny payload wording not visually readable |
| F6 | Yes, visual/text | Yes | Represented with uncertainty | Semantics grounded in caption/prose |
| F7 | Yes, visual/text | Yes | Fully represented | Distribution and vocabulary inconsistency |
| T1 | Yes, visual/text | Yes | Represented in compressed form | WARD scores and representative baselines; not every baseline cell |
| T2 | Yes, visual/text | Yes | Represented in compressed form | Full final pattern and important no-PIG failures |
| T3 | Yes, visual/text | Yes | Fully represented substantively | All WARD per-dataset values and means |
| T4 | Yes, visual/text | Yes | Represented in compressed form | Averages, important domain deviations |
| T5 | Yes, visual/text | Yes | Represented in compressed form | All WARD outcomes; baseline averages and selected cells |
| T6 | Yes, visual/text | Yes | Represented in compressed form | All guard/backbone averages; model-version caveat |
| T7 | Yes, visual/text | Yes | Fully represented | Times/tokens and missing tokens |
| T8 | Yes, visual/text | Yes | Represented in compressed form | Component trends and key exact contrasts |
| T9 | Yes, visual/text | Yes | Fully represented substantively | Comparison dimensions; shorthand caveat |
| T10 | Yes, visual/text | Yes | Fully represented substantively | Counts/modalities/platform inconsistency |
| E1–E8 | Yes, visual/text | Yes | Fully represented substantively | Mathematical identity, role, notation caveats |
| Algorithms/pseudocode | Assessed | Yes | No separate numbered pseudocode | Workflows represented through F2/H/E8 |
| Appendix A | Yes, text-only | Yes | Fully represented | Pixel-level scope |
| B.1 | Yes, text-only | Yes | Fully represented substantively | Preprocessing, training, diversity |
| B.2.1 | Yes, text/visual | Yes | Fully represented | Baselines and repetitions |
| B.2.2 | Yes, text/visual | Yes | Fully represented substantively | Three adversarial protocols |
| B.2.3 | Yes, text/visual | Yes | Fully represented | Utility measurement/version inconsistency |
| B.3 and B.4 | Yes, text/visual | Yes | Fully represented substantively | Timing and ablation |
| Appendix C | Yes, text/visual | Yes | Fully represented substantively | Author dataset comparison |
| Appendix D | Yes, text/visual | Yes | Fully represented substantively | OOD discussion and test counts |
| Appendix E | Yes, mixed coverage | Yes | Fully represented | Failure and false-positive tradeoff |
| Appendix F | Yes, text/visual | Yes | Fully represented | Channels |
| Appendix G | Yes, text-only | Yes | Represented in compressed form | Input/output schema and reasoning requirement |
| Appendix H | Yes, text-only | Yes | Represented in compressed form | Memory, camouflage, validation, score 1–4 |
| Appendix I | Yes, text-only | Yes | Represented in compressed form | Nine safe-verdict/guard-decision training variants |
| Appendix J | Yes, text-only | Yes | Fully represented substantively | Format-specific fake testing outputs |
| Appendix K | Yes, text-only | Yes | Fully represented substantively | Benefits, dual use, limits, mitigation/future work |
| Contributions and stated limitations | Yes | Yes | Fully represented substantively | Separate from analyst observations |
| Substantive footnotes | Yes | Yes | Represented in compressed form | Repository and Similarweb links identified, not accessed |
| Acknowledgements/references | Yes, text-only | Yes | Deliberately compressed | Funding and bibliographic role retained |
| Supplementary/code/data artifacts | No | Disclosed | Missing from supplied material | No independent artifact review |

Bibliographic inventory: authors are Tri Cao, Yulin Chen, Hieu Cao, Yibo Li, Khoi Le, Thong Nguyen, Yuexin Li, Yufei He, Yue Liu, Shuicheng Yan, and Bryan Hooi. Affiliations are National University of Singapore; University of Science; and Vietnam National University, Ho Chi Minh City. Page 1 identifies a preprint, arXiv:2605.15030v1, dated 14 May 2026, with category cs.CR. No peer-reviewed venue is supplied. Acknowledgements name Singapore National Research Foundation/AI Singapore award AISG3-PhD-2025-08-059 and Ministry of Education Tier 1 grant T1 251RES2507. No keywords section is visible.

### Missing or inaccessible material

No numbered textual page is missing. Separate code, model files, datasets, logs, licenses, and referenced external publications/documentation were not supplied for inspection. Thirteen pages lack rendered source images in this input. Detailed tiny screenshot payloads in F5/F6 are not confidently visually readable. No separate supplementary file was reviewed or assumed present.

### Uncertain interpretations

Unresolved items are the six/seven WARD-Test platform count; Claude utility version; native channel vocabulary; Figure 1 utility aggregation; Table 9 PIG count shorthand; VPI domain naming across tables; exact metric denominators/aggregation in some averages; the adaptive evaluation’s actual retained sample denominator; and full enforcement behavior after detection. Figure endpoint values are grounded in labels/text, while unlabeled intermediate coordinates are not asserted. Source SHA-256 is user-provided and was not independently recomputed.

### Deliberately compressed material

Repeated introductory/concluding claims, all 84 bibliography entries, secondary baseline cells, every domain-level utility cell, intermediate plotted coordinates, and literal repeated prompt templates are compressed. Their functions, major outcomes, noteworthy exceptions, and relevant source locations are represented. Training prompt output fields are reasoning, attack_goal, injection_location, and label. Validator fields include goal alignment, HTML/screenshot presence, deception score 1–4, reasoning, issues, and repair feedback. Thus prompt mechanics are retained without reproducing every imperative.

### Potential omissions

Every substantive section, appendix, figure, table, mathematical group, experiment group, contribution, and stated limitation identified in the supplied inventory is represented at least substantively. This does not imply that every cell, reference, wording, or hidden artifact has been preserved. Exact reproduction remains limited by the omissions and inconsistencies listed above. Confidence is HIGH for clearly supplied text and labeled results, MEDIUM for bounded methodological interpretation and tiny visual details, and UNKNOWN for absent artifacts and unresolved source conflicts.
