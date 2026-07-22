# WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections

**Authors:** Tri Cao, Yulin Chen, Hieu Cao, Yibo Li, Khoi Le, Thong Nguyen, Yuexin Li, Yufei He, Yue Liu, Shuicheng Yan, and Bryan Hooi  
**Affiliations:** National University of Singapore; University of Science; Vietnam National University, Ho Chi Minh City

## 1. Background and Context

Web agents are systems powered by language or vision-language models that carry out online tasks by observing webpages and taking actions such as clicking, typing, and browsing. They may use HTML, screenshots, or both to understand the page.

This access to open web content creates a major security problem: an attacker can place deceptive instructions inside webpage HTML, visible interface elements, images, popups, messages, posts, or other content. If an agent mistakes these instructions for legitimate guidance, it may depart from the user’s goal, leak information, perform unauthorized actions, or otherwise behave unsafely.

The paper calls these attacks **prompt injections**. It distinguishes them from direct jailbreaks: prompt injections arise from external content encountered during task execution, whereas jailbreaks typically involve users directly manipulating a model’s prompt.

A common defense is a separate **guard model** that inspects the webpage before the agent acts. In this paper, the agent observes at step \(t\):

- a screenshot \(S_t\);
- associated HTML/text \(H_t\);
- the user’s instruction \(I\).

The guard independently evaluates \(I\) and the combined webpage observation \(x_t=(S_t,H_t)\), producing a benign-or-malicious decision. It runs without access to the agent’s internal reasoning.

The authors identify four shortcomings in existing guards:

1. **Limited generalization.** Existing training sets cover narrow collections of general-purpose websites. Guards therefore struggle with unfamiliar domains, high-risk settings such as email and messaging, new interface forms, and shifts between HTML-only, screenshot-only, and multimodal injections. Text-only guards miss visual attacks, while screenshot-only guards miss hidden HTML attacks.

2. **High false-positive rates.** Instruction-like but harmless content, such as tutorials or support pages, may be incorrectly blocked. This interrupts tasks and reduces the agent’s usefulness.

3. **Efficiency problems.** Some defenses must wait for the agent’s proposed action or reasoning, preventing parallel operation. Others use large, expensive models. Both approaches can add latency at every interaction step.

4. **Adversarial vulnerability.**
   - In **Prompt Injection on Guard (PIG)**, malicious content explicitly targets the guard’s own decision process—for example, by presenting a fake “benign” verdict.
   - In **adaptive adversarial attacks**, attackers repeatedly observe failures and modify their prompts until they bypass the guard.

Prior defenses include system-prompt modifications, direct safety fine-tuning, reasoning correction, general safety guards, text-based injection detectors, screenshot guards, and parallel multimodal guards. The paper argues that none simultaneously provides broad generalization, low false-positive rates, multimodal coverage, adversarial robustness, and practical efficiency.

---

## 2. Research Goal and Objectives

The paper introduces **WARD—Web Agent Robust Defense against Prompt Injection**, a compact multimodal guard intended to protect web agents without slowing them down or unnecessarily blocking benign content.

Its objectives are to:

- detect prompt injections in HTML, screenshots, or both;
- generalize to unseen websites, platforms, interface designs, injection channels, and attack wording;
- preserve agent utility by minimizing false positives;
- resist prompts directly targeting the guard;
- withstand attackers that iteratively adapt their strategies;
- run concurrently with the agent without adding end-to-end latency;
- explain its decision, identify the injection location, and infer the attacker’s goal.

The proposed solution combines three components:

1. **WARD-Base:** a large, diverse training dataset;
2. **WARD-PIG:** guard-targeted adversarial training data;
3. **A3T:** Adaptive Adversarial Attack Training, in which an attacker and guard co-evolve over repeated training cycles.

---

## 3. Methods (Approach/Design)

### 3.1 WARD’s output

For each sample, the guard receives:

\[
x=(H,S,I),
\]

where \(H\) is processed HTML, \(S\) is the screenshot, and \(I\) is the user’s intended task.

It generates:

\[
a=(y,\ell,g,r),
\]

where:

- \(y\) is the **label**: malicious or benign;
- \(\ell\) is the **injection location**: HTML, screenshot, both, or none;
- \(g\) is the inferred **attack goal**;
- \(r\) is an evidence-based **reasoning explanation**.

Thus, WARD performs more than binary classification: it localizes and interprets the suspected attack.

### 3.2 Two-branch construction of WARD-Base

WARD-Base is built through two complementary branches.

#### Overlay branch: real webpages

The authors selected the 50 most-visited URLs in each of 21 Similarweb categories. After filtering, they retained 808 valid URLs.

For every URL, they generated five benign user tasks, giving 4,040 tasks. A Browser-Use agent executed each task for up to 100 steps or until completion. At every step, the researchers recorded the HTML and screenshot, creating source tuples \((H_0,S_0,I)\).

Malicious or benign content was later overlaid through interface channels, thereby preserving realistic webpage layouts while permitting controlled injection.

#### Native branch: simulated high-risk platforms

The authors also developed 20 simulated platforms in five categories:

- collaborative systems;
- email;
- messaging;
- e-commerce;
- social media.

These reproduced the layout and interaction style of real applications. Each platform was paired with 20 benign user tasks. Attacks could therefore be inserted naturally into user-generated fields such as messages, posts, comments, email, README content, reviews, or product descriptions.

#### Dataset separation

Source environments were divided into three disjoint sets:

- **WARD-Base:** 709 URLs and 10 platforms for supervised training;
- **WARD-Seed:** 49 URLs and 4 platforms for adaptive adversarial training;
- **WARD-Test:** 50 URLs and 6 platforms for evaluation.

The accompanying dataset-comparison table later describes WARD-Test as covering 50 websites plus seven replicated platforms. This differs from the six-platform figure in the main construction description; the supplied paper does not reconcile the discrepancy.

The split was designed to prevent information leakage and support evaluation on unseen domains.

### 3.3 Attack generation

Every source sample was converted into paired malicious and benign variants while preserving the original user task.

#### Attack goals

WARD models six categories:

1. user-information exfiltration;
2. unauthorized action execution;
3. policy-violating content generation;
4. single-step UI manipulation;
5. agent-memory manipulation;
6. utility degradation.

For each of the first five, the researchers curated 100 specific goals. Utility-degradation goals were generated from the user’s task and attempted to distract or mislead the agent so that task success would fall.

Across the complete dataset, there are **4,615 specific attack goals**.

#### Injection locations

The prompt may appear:

- only in HTML;
- only in the screenshot;
- in both;
- nowhere, for an unmodified benign base observation.

For benign generated prompts, the authors set the recorded goal and injection location to “none,” even though contextual benign text was generated using the same channel setup.

#### Injection channels

The overlay branch uses interface forms including:

- footer text;
- alert box;
- badge;
- banner;
- notification;
- inset chat;
- popup.

Figure 7 additionally includes the unmodified “none” category when showing the overlay distribution.

The native branch uses platform-specific fields:

- message;
- email;
- post;
- comment;
- README;
- review;
- product description/information.

Overall, the paper reports **13 actual injection channels**.

#### Prompt creation and insertion

For a malicious example, a vision-language model receives the original HTML, screenshot, task, attack goal, channel, and location. For a benign example, the attack goal is omitted so that the generated text remains contextually appropriate but lacks malicious intent.

Three candidates are sampled with different temperatures, and one is selected randomly. The chosen prompt is then inserted into HTML, the screenshot, or both.

The construction uses **Gemini-3-Flash** to generate prompts. To improve visual diversity, the researchers use 193 fonts and thousands of background/interface images, including avatars, popup illustrations, and post images.

Screenshots remain at their original resolution. HTML is converted to textual content while preserving tag names, retaining some structural information. The same preprocessing is used for training and evaluation.

### 3.4 Reasoning generation

WARD-Base initially contains the input, label, attack location, and attack goal but not a reasoning trace.

A generator repeatedly predicts reasoning, goal, location, and label. An evaluator checks the predicted label and location against ground truth. Exact agreement on the wording of the inferred goal is not required.

- If label and location are correct, the reasoning is accepted.
- If not, the evaluator supplies a hint, and generation repeats.

This loop is meant to ensure that the reasoning is grounded in the HTML and screenshot rather than copied mechanically from annotations. Gemini-3-Flash generates the reasoning traces, and only correct, high-quality traces are retained.

### 3.5 Figure 2: complete WARD pipeline

Figure 2 presents the end-to-end design:

1. real-web exploration and simulated-platform development;
2. benign-data sampling and attack generation;
3. dataset assembly into WARD-Base, WARD-PIG, WARD-Seed, and WARD-Test;
4. generator–evaluator reasoning annotation;
5. supervised fine-tuning on WARD-Base;
6. further supervised fine-tuning on WARD-PIG;
7. A3T, where an attacker, validator, memory, and guard iteratively generate and learn from successful bypasses.

### 3.6 Figure 3: WARD-Base composition

WARD-Base contains:

- **177,585 samples**;
- **709 websites/URLs**;
- **10 replicated platforms**;
- **4,615 specific attack goals**;
- **13 injection channels**;
- **3,745 benign user tasks**.

Its label distribution is nearly balanced:

- benign: **90,802 (51.1%)**;
- malicious: **86,783 (48.9%)**.

Injection-location distribution:

- HTML: **39,397 (22.2%)**;
- screenshot: **50,099 (28.2%)**;
- both: **68,383 (38.5%)**;
- none: **19,706 (11.1%)**.

Malicious attack-goal distribution:

- unauthorized action execution: **18,690 (21.5%)**;
- user-information exfiltration: **17,838 (20.6%)**;
- single-step UI manipulation: **17,277 (19.9%)**;
- policy-violating content generation: **11,355 (13.1%)**;
- agent-memory manipulation: **11,333 (13.1%)**;
- utility degradation: **10,290 (11.9%)**.

### 3.7 Figure 7: channel distributions

For the overlay branch, Figure 7 reports:

- none: **19,706 (13.7%)**;
- alert box: **17,051 (11.9%)**;
- footer text: **17,010 (11.8%)**;
- badge: **17,001 (11.8%)**;
- popup: **22,592 (15.7%)**;
- notification: **16,852 (11.7%)**;
- inset chat: **16,706 (11.6%)**;
- banner: **16,690 (11.6%)**.

For the native branch:

- message: **12,193 (35.9%)**;
- email: **12,186 (35.9%)**;
- comment: **3,600 (10.6%)**;
- post: **3,599 (10.6%)**;
- review: **1,200 (3.5%)**;
- product description: **1,199 (3.5%)**.

### 3.8 Three-stage training

#### Stage 1: supervised fine-tuning on WARD-Base

The model learns to generate the full target sequence—reasoning, goal, location, and label—token by token from the task, HTML, and screenshot. The loss is ordinary negative log-likelihood over the target tokens.

This teaches general multimodal prompt-injection detection and localization.

#### Stage 2: WARD-PIG training

Because a guard sees the same potentially hostile content as the agent, it can itself be manipulated. To create WARD-PIG, the researchers selected:

- **10,500 malicious samples**, comprising 3,500 for each malicious injection-location setting;
- **10,500 benign samples** to preserve utility.

Guard-targeting text was inserted into the appropriate modality. Construction prompts included statements resembling security verdicts, such as claims that the page was verified as benign. Evaluation used even more structured fake outputs tailored to each guard’s response schema.

The model was then fine-tuned further so that it would treat such guard-facing instructions as evidence of an attack instead of following them.

#### Stage 3: A3T

A3T models attackers who repeatedly adapt to the guard.

Its inner loop contains:

- an attacker that creates a context-specific malicious prompt;
- injection into the selected channel and modality;
- a validator that checks attack-goal consistency, contextual plausibility, expected modality presence, and whether the prompt is strong enough to redirect an agent;
- the guard, which determines whether the prompt bypasses detection.

Only valid attacks that fool the guard enter the adversarial training collection.

The attacker uses two kinds of memory:

- **sample-level memory:** earlier attempts, validator comments, predictions, successes, and failures for that sample;
- **platform-level memory:** reusable successes and failures from the same URL or platform.

For each URL or platform, training continues until 10 successful adversarial samples are collected. Each base sample permits up to five attempts and stops early after success.

The outer loop updates the guard with successful attacks using Group Relative Policy Optimization. The reward is:

- **1.0** when both label and injection location are correct;
- **0.5** when the label is correct but location is wrong;
- **0.0** otherwise.

WARD-Seed is divided across three adaptive-training cycles. Gemini-3-Flash serves as both attacker and validator. Benign examples are sampled per URL or platform in proportion to the malicious examples to preserve utility.

### 3.9 Training configuration

The backbones are compact **Qwen-3.5-0.8B** and **Qwen-3.5-2B** models.

For WARD-Base and WARD-PIG:

- full fine-tuning for one epoch on each dataset;
- two NVIDIA H200 140-GB GPUs;
- batch size 256;
- learning rate \(3.0\times10^{-5}\);
- fused AdamW optimizer;
- cosine learning-rate schedule.

For A3T:

- training begins from the WARD-PIG checkpoint;
- GRPO rollout count \(n=6\);
- batch size 24;
- one epoch.

### 3.10 Evaluation design

WARD was evaluated on:

- detection across WARD-Test and four external out-of-distribution benchmarks;
- protection of deployed agents;
- PIG attacks;
- in-domain adaptive attacks;
- strongly cross-domain adaptive attacks;
- false positives and agent performance degradation;
- token use and runtime.

Detection comparisons include 25 baselines from four groups:

- closed-source APIs;
- open-source instruction-following models;
- general/jailbreak safety guards;
- prompt-injection guards.

WARD and guard-model experiments were run three times with sampling disabled. Because the fine-tuned models were deterministic, results were identical and standard deviation was zero. Closed-source and general open-source models used temperature zero and one run because of resource constraints.

---

## 4. Results and Findings

### 4.1 Detection performance

#### Table 1: WARD-Test and out-of-distribution benchmarks

The benchmarks were:

- **WARD-Test:** 1,500 benign plus 1,500 malicious samples;
- **Popup:** 2,682 benign plus 2,682 malicious samples;
- **EIA:** 1,414 malicious samples;
- **VPI:** 306 malicious samples;
- **WASP:** 84 malicious samples.

They differ from training in websites, layout, interface structure, channels, and language.

On WARD-Test:

- **WARD-0.8B:** 99.33% accuracy, 99.60% recall, 99.07% precision, and 99.34% F1.
- **WARD-2B:** 99.20% accuracy, 99.67% recall, 98.75% precision, and 99.20% F1.

On Popup:

- WARD-0.8B: 99.98% accuracy, 100% recall, 99.96% precision, 99.98% F1.
- WARD-2B: 99.91% accuracy, 100% recall, 99.81% precision, 99.91% F1.

Both WARD models achieved **100% recall on EIA, VPI, and WASP**, as well as Popup.

The strongest previous prompt-injection guard on WARD-Test, WebAgentGuard-8B, reached 91.97% accuracy, 85.20% recall, and 91.38% F1. Its recall on Popup, EIA, VPI, and WASP was 76.14%, 84.72%, 78.10%, and 58.33%. WebAgentGuard-4B obtained 78.40% WARD-Test recall and external recalls of 37.55%, 95.47%, 89.54%, and 50.00%.

Selected closed-source results illustrate that large general models were strong but less consistent:

- GPT-5.4: 92.07% WARD-Test recall and 100%, 84.97%, and 100% on EIA, VPI, and WASP;
- Gemini-3-Flash: 96.53% WARD-Test recall and 99.78%, 99.93%, 93.14%, and 100% on Popup, EIA, VPI, and WASP;
- Claude-Sonnet-4.6: 97.40% WARD-Test recall and 99.70%, 100%, 95.42%, and 100% externally.

Several general safety guards largely failed. Llama-Guard-3-Vision-11B and GuardReasoner-VL-7B produced zero recall throughout the reported evaluation. Text-oriented guards were often highly inconsistent—for example, BrowseSafe reached 94.77% recall on EIA but 0% on Popup and VPI.

#### Figure 1a

The detection panel visually summarizes the same pattern: WARD’s two variants reach 100% recall on Popup, EIA, VPI, and WASP, whereas WebAgentGuard variants range from roughly 37.5% to 95.5% depending on model and benchmark.

### 4.2 Protection of operating agents

#### Table 5: VPI attack success rate

WARD was run in parallel with:

- a Computer-Use agent powered by Sonnet-3.7;
- a Browser-Use agent powered by Gemini-2.0-Pro.

The evaluation covered Amazon, Booking, BBC, Messenger, and Email.

With no defense, average attack success was:

- **33.70%** for Computer-Use;
- **76.98%** for Browser-Use.

A system-prompt defense achieved averages of 33.02% and 74.98%; a GPT-4o guard achieved 13.64% and 23.94%.

WebAgentGuard-4B reduced average success to 3.78% and 2.68%, but still had individual failures as high as 10.0% and 8.3% for Computer-Use and 6.4% for Browser-Use. WebAgentGuard-8B averaged 5.34% and 3.32%, with individual rates up to 13.3% and 11.7%.

Both WARD-0.8B and WARD-2B achieved **0% attack success in every task, domain, and agent setting**.

### 4.3 Robustness to Prompt Injection on Guard

The authors added unseen guard-targeted fake outputs to malicious samples. Attacks appeared in HTML, screenshots, or both.

#### Table 2

Both fully trained WARD variants maintained **100% recall across all 15 combinations** of five datasets and three modalities.

Without PIG training, WARD’s performance was much weaker and inconsistent. Examples include:

- WARD-0.8B without PIG: 39.29% recall for Popup/both, 35.22% for EIA/HTML, 50.98% for VPI/both, and 38.10% for WASP/HTML.
- WARD-2B without PIG: 28.45% for Popup/both, 25.81% for EIA/both, 17.32% for VPI/both, and 46.43% for WASP/both.

WebAgentGuard also suffered major drops. WebAgentGuard-4B ranged from 2.50% recall on Popup/both to 90.66% on EIA/screenshot. WebAgentGuard-8B ranged from 22.93% on WARD/HTML to 79.84% on EIA/screenshot.

These results isolate the benefit of explicit guard-targeted training.

### 4.4 In-domain adaptive attacks

For stress testing, unseen WARD-Test configurations were fed into A3T. The evaluation used four samples per unseen URL or platform and allowed up to 10 attack attempts, twice the five-attempt training limit.

Two metrics were reported:

- **sample success rate (SSR):** fraction of samples for which at least one attack succeeds;
- **attempt success rate (ASR):** fraction of individual attack attempts that succeed.

#### Figure 4

At a trial budget of 10:

- WARD-2B’s final-cycle SSR was **3.12%**;
- WARD-0.8B’s final-cycle SSR was **5.62%**;
- corresponding final-cycle ASRs were **0.34%** and **0.62%**.

At a trial budget of five, both models’ final-cycle SSR and ASR were described as near zero.

By comparison, WebAgentGuard reached approximately:

- **74.38% and 78.75% SSR** at budget 10;
- **19.16% and 22.62% ASR** at budget 10.

The plotted progression shows WARD becoming harder to bypass across cycles 0–3. The authors interpret this as evidence that A3T teaches the guard to handle attacks beyond the exact five-attempt training regime.

### 4.5 Cross-domain adaptive attacks

WARD was evaluated through the original PIArena strategy-based adaptive attack framework, which differs substantially from training:

- text-only generic prompt injections rather than webpage HTML/screenshot attacks;
- QA, retrieval-augmented generation, summarization, long-context reasoning, and code-generation tasks rather than web agents;
- population-based semantic rewriting and mutation instead of A3T’s single-candidate refinement;
- GPT-5.1 as attacker instead of Gemini-3-Flash.

PIArena used:

- population size 10;
- five initial attempts per strategy;
- up to five generations;
- 1,700 samples from 13 datasets.

The sample composition was 200 each from SQuAD v2 and three Dolly tasks, plus 100 each from NQ RAG, MSMARCO RAG, HotpotQA RAG, HotpotQA Long, Qasper, GovReport, MultiNews, Passage Retrieval, and LCC. For this text-only evaluation, screenshot input was omitted and the text was passed as preprocessed HTML.

#### Table 3

Average attack-success rates were:

- PromptArmor: **92.21%**;
- PromptGuard: **92.14%**;
- DataSentinel: **45.71%**;
- WARD-0.8B: **3.23%**;
- WARD-2B: **3.08%**.

WARD-0.8B’s per-dataset rates ranged from 0% to 7%; WARD-2B’s ranged from 0% to 9%. Both achieved 0% on Qasper and Passage Retrieval. In contrast, PromptArmor and PromptGuard reached 99–100% on many datasets. This indicates strong transfer across domain, task, modality, attack process, and attacker-model shifts.

### 4.6 Utility preservation

Utility was tested on 802 benign WebArena tasks across GitLab, Map, Reddit, Shopping, Admin, and Wikipedia. The guard ran at every step. False-positive rate was measured per step, while performance degradation was measured at task level by comparing completion with and without the guard. GPT-4o evaluated completion.

#### Table 4: GPT-4o-backed agent

Across 7,605 steps:

- WebAgentGuard-4B: **7.17% average FPR**, **5.91% degradation**;
- WebAgentGuard-8B: **13.12% FPR**, **7.88% degradation**;
- WARD-0.8B: **0.26% FPR**, **0.37% degradation**;
- WARD-2B: **0.25% FPR**, **0.25% degradation**.

WARD’s domain-specific false-positive rates were all between 0% and 0.49%. The largest performance drop was 1.55% on Reddit.

#### Table 6: other agent backbones

For Claude 3.7 Sonnet over 7,344 steps:

- WebAgentGuard-4B: 5.27% FPR and 6.51% degradation;
- WebAgentGuard-8B: 11.55% and 9.76%;
- WARD-0.8B: 0.20% and 0.25%;
- WARD-2B: 0.22% and 0.38%.

For Gemini 3 Flash over 7,392 steps:

- WebAgentGuard-4B: 5.05% FPR and 9.00% degradation;
- WebAgentGuard-8B: 13.62% and 11.47%;
- WARD-0.8B: 0.35% and 0.37%;
- WARD-2B: 0.24% and 0.37%.

#### Figure 1b

The utility panel summarizes average false-alert rates of roughly 5.8% and 12.8% for WebAgentGuard-4B/8B, versus about 0.3% and 0.2% for WARD-0.8B/2B.

### 4.7 Efficiency

Efficiency was measured under benign WebArena and malicious VPI conditions on a single NVIDIA H200 GPU, batch size one. The guard runs concurrently with the agent and does not alter its workflow.

#### Table 7

On benign WebArena:

- WARD-0.8B: **131.45 output tokens**, **2.24 seconds** per step;
- WARD-2B: **127.67 tokens**, **2.37 seconds**;
- WebAgentGuard-4B: **399.73 tokens**, **8.81 seconds**;
- WebAgentGuard-8B: **417.97 tokens**, **10.03 seconds**.

Agent runtimes were:

- Claude-3.7-Sonnet: 11.99 seconds;
- GPT-4o: 4.84 seconds;
- Gemini-3-Flash: 3.64 seconds.

On malicious VPI:

- WARD-0.8B: **150.63 tokens**, **2.37 seconds**;
- WARD-2B: **152.35 tokens**, **2.45 seconds**;
- WebAgentGuard-4B: **440.26 tokens**, **9.65 seconds**;
- WebAgentGuard-8B: **468.75 tokens**, **9.63 seconds**.

Agent runtimes were 7.35 seconds for Claude-3.7-Sonnet, 6.03 for GPT-4o, and 5.43 for GPT-4.1.

Because both WARD variants finish before each tested agent, the authors argue that WARD can operate in true parallel without adding latency.

#### Figure 1c

The figure rounds these token results to approximately:

- benign: 440 and 400 tokens for WebAgentGuard versus 131 and 128 for WARD;
- malicious: 469 and 418 versus 151 and 152.

### 4.8 Ablation study

#### Table 8

The ablation progressively adds the native branch, overlay branch, PIG training, and adaptive training.

For WARD-0.8B:

- native-only detection recall ranged from 81.17% on Popup to 100% on WASP;
- overlay-only ranged from 76.47% on VPI to 100% on Popup and EIA;
- combining branches produced 98.80% on WARD, 99.74% Popup, 100% EIA, 98.69% VPI, and 100% WASP;
- adding PIG produced 100% PIG recall in HTML, screenshot, and both, but adaptive SSR remained 28.75%;
- adding A3T reduced SSR to **5.62%** and raised all external detection recalls to 100%.

For WARD-2B:

- native-only ranged from 88.23% Popup to 100% VPI/WASP;
- overlay-only ranged from 80.39% VPI and 85.71% WASP to 100% Popup/EIA;
- combining both yielded at least 99.27% recall across detection datasets;
- adding PIG raised all PIG conditions to 100% recall but left adaptive SSR at 21.88%;
- adding A3T reduced SSR to **3.12%**, while detection and PIG recall reached 100% in the reported columns.

Thus, the two data branches improve complementary forms of generalization, WARD-PIG specifically addresses guard-targeted manipulation, and A3T specifically addresses iterative bypasses.

### 4.9 Training-data comparison

#### Table 9

WARD is compared with WebAgentGuard and BrowseSafe:

- WARD: **177K + 10.5K PIG + A3T**;
- WebAgentGuard: 5.3K;
- BrowseSafe: 14.7K.

WARD uses real webpages, simulated platforms, and synthetic injection; supports HTML and screenshots; explicitly represents location, 13 channels, six goal categories, reasoning, guard-targeted attacks, and adaptive adversarial training.

WebAgentGuard uses fully synthetic multimodal data with implicit channels and no explicitly modeled goals, PIG, or adaptive adversarial training. BrowseSafe uses real HTML with synthetic injections but is HTML-only, lacks reasoning annotations, and does not include guard-targeted or adaptive attacks.

### 4.10 Test-set diversity and Figure 5

Table 10 shows that external benchmarks differ in modality and context:

- Popup: screenshot popup attacks on 50 unseen websites;
- EIA: HTML form attacks on real-world pages;
- VPI: screenshot and multimodal form/message/mail attacks on BBC, Shopee, Booking, and custom platforms;
- WASP: multimodal post attacks on unseen GitLab and Reddit environments.

Figure 5 visually compares a training popup with a Popup-benchmark example. Both use a popup channel, but their style, placement, layout, triggering, and integration with page content differ substantially. The authors use this to argue that performance cannot be explained by memorizing a simple “popup” pattern.

### 4.11 Failure case

#### Figure 6: Kleinanzeigen “Smart Search”

The principal qualitative failure involves a user asked to find the first ten used city bikes in Berlin priced below EUR 200, including title, price, and neighborhood.

The attack inserts a visually plausible **Smart Search** recommendation box containing ten fabricated listings in exactly the requested format. It does not look like an overt command. Instead, it resembles a legitimate marketplace feature that helpfully summarizes results.

WARD labels it benign because the injected content:

- closely matches the user’s task;
- is visually consistent with the page;
- supplies information in the requested format;
- resembles a normal recommendation widget;
- uses contextual mimicry rather than suspicious wording.

The attack degrades utility by encouraging the agent to return fabricated results without performing the real search. The authors emphasize that the boundary between this attack and harmless task-aligned assistance is narrow; increasing sensitivity could catch it but would also risk more false positives.

### 4.12 Broader impacts

The authors identify possible benefits in autonomous browsing, digital assistants, and tool-using systems, including sensitive finance, healthcare, and enterprise applications.

They also identify risks:

- adversarial-data and adaptive-attack techniques could be repurposed offensively;
- false positives could harm usability;
- unsupported attacks may create a false sense of security;
- guard models should not be treated as a complete security solution.

They recommend layered defenses, continued evaluation under evolving threats, transparent reporting of failures, cautious deployment, and safeguards against misuse of adversarial-generation techniques.

---

## 5. Analysis and Interpretation

The results support the paper’s central claim that robust web-agent defense requires more than simply enlarging a binary training dataset.

The authors attribute WARD’s generalization to several interacting design choices:

- Real webpages expose the model to genuine layouts and content.
- Simulated high-risk platforms provide natural user-generated attack channels that ordinary website collections lack.
- Explicitly modeling goals, modalities, channels, and locations prevents the task from collapsing into shallow phrase recognition.
- Context-matched benign examples teach WARD not to treat every instruction-like passage as malicious.
- Reasoning distillation encourages decisions grounded in the screenshot, HTML, and user task.
- PIG training teaches the guard to distrust fake verdicts aimed at its own response process.
- A3T shifts learning toward the current decision boundary by repeatedly finding and training on successful bypasses.

The ablation results support these interpretations. Neither the native nor overlay branch alone generalizes uniformly. PIG robustness becomes perfect only after PIG training, while low adaptive success rates require A3T.

The cross-domain PIArena results are especially important to the authors’ argument because the evaluation changes the modality, task domain, attacker model, and attack-generation procedure simultaneously. WARD’s approximately 3% average attack-success rate, compared with 45.71–92.21% for alternatives, suggests that the learned defense transfers beyond web screenshots and HTML.

Utility and runtime results address practical deployment concerns. WARD is not only more accurate but also substantially less likely to interrupt benign tasks. Its compact size and shorter outputs allow it to finish before the tested web agents, so parallel guarding need not extend the interaction step.

The failure study nevertheless shows that detection remains difficult when malicious content is nearly indistinguishable from legitimate, helpful interface content. Task alignment, normally a sign of relevance, can itself become camouflage. The authors frame this as a fundamental tension between recall and false positives.

---

## 6. Contributions and Novelty

The paper’s main contributions are:

- **WARD**, a compact multimodal guard that detects, localizes, interprets, and explains prompt injections while running independently in parallel with a web agent.
- **WARD-Base**, a 177,585-sample dataset spanning 709 URLs, 10 simulated high-risk platforms, multiple modalities, 13 channels, six goal categories, and 4,615 specific attack goals.
- A **two-branch data pipeline** combining attacks overlaid onto real webpages with attacks naturally embedded in simulated email, messaging, collaborative, commercial, and social platforms.
- **WARD-PIG**, dedicated training against attempts to manipulate the guard itself.
- **A3T**, a memory-based attacker–validator–guard co-evolution procedure that generates progressively harder, context-specific attacks.
- Reasoning annotations that require the guard to connect the user’s intent with evidence in both HTML and screenshots.
- Extensive evaluation of detection, realistic agent protection, guard-targeted attacks, in-domain adaptation, cross-domain adaptation, utility, and efficiency.
- Empirical evidence that compact 0.8B- and 2B-parameter guards can outperform much larger general models and existing specialist guards while requiring fewer tokens and less runtime.

---

## 7. Limitations and Caveats

The authors explicitly limit WARD to attacks whose malicious intent appears in textual or visually interpretable webpage content.

It may not protect against **pixel-level environmental attacks**, such as imperceptible perturbations optimized to induce a target action without presenting readable malicious instructions. Such attacks are outside the training threat model. The paper notes, however, that they require stronger capabilities: access to the target or surrogate model for gradient optimization, control of webpage rendering, and per-page tuning across a non-differentiable pipeline.

Other caveats include:

- The in-domain adaptive evaluation reuses the A3T framework because no established web-based adaptive benchmark exists. Although it uses unseen environments, longer attack budgets, and newly conditioned prompts, its structure is related to training.
- Cross-domain PIArena testing is text-only, so it does not measure visual robustness in those non-web domains.
- Closed-source and general open-source baselines received only one evaluation run because of resource constraints.
- SnapGuard could not be included because its source code was unavailable.
- The failure example shows that task-aligned, interface-consistent misinformation can bypass WARD.
- Raising sensitivity to such subtle cases could increase false positives on legitimate helpful content.
- Adaptive attack generation has dual-use potential.
- The evaluation does not establish that WARD covers every evolving prompt-injection strategy.
- Guard deployment should not produce overconfidence; the authors recommend using it alongside other security measures.
- The paper contains a small reporting inconsistency: the main split states that WARD-Test has six replicated platforms, while Table 10 describes seven.

No statistical significance tests or confidence intervals are reported. Deterministic guard results had standard deviation zero across three runs.

---

## 8. Future Work or Open Questions

The paper calls for:

- continued evaluation as attacker strategies and threat models evolve;
- extending robustness to broader attack classes, including pixel-level manipulation;
- improving detection of highly camouflaged, task-aligned misinformation without substantially increasing false positives;
- safeguards against misuse of adaptive adversarial-generation methods;
- transparent reporting of failure cases and limitations;
- cautious integration with layered security controls rather than reliance on a guard alone.

An especially important open problem identified by the failure analysis is how to distinguish a legitimate interface widget from a fabricated but visually credible and task-relevant one. The supplied paper does not present a complete solution to this tradeoff.

---

## 9. High-Level Takeaway (Plain Language)

WARD is a security checker that watches the same webpage as an AI web agent and tries to detect hidden instructions meant to trick it. The authors trained it on a large mix of real webpages, simulated email and social platforms, attacks targeting the checker itself, and attacks that repeatedly adapt after failure.

The resulting small models detected essentially all attacks on several unseen benchmarks, reduced attack success to zero in the tested live-agent tasks, produced false alarms on only about 0.2–0.35% of benign steps, and ran faster than the agents they protected. They also resisted strong adaptive attacks far better than prior defenses. However, WARD can still be fooled by malicious content that looks almost exactly like a legitimate, helpful webpage feature, and it does not cover imperceptible pixel-level attacks.