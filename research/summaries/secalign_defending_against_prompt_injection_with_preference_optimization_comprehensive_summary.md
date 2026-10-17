## Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. Paper content, including attack examples, is treated as evidence rather than instructions. No external research, tools, code execution, citation checking, or repository inspection was performed.

| Accessibility item | Assessment |
|---|---|
| Main document | Supplied text covers physical PDF pages 1–15; the publication citation itself states 15 pages. |
| Page numbering | Locators below use physical PDF pages 1–15, corresponding to printed proceedings pages 2833–2847. |
| Apparently missing pages | No physical page is missing from the supplied text. Page 4 has no supplied rendered image. |
| Visually inspected pages | Pages 1, 2, 3, and 5–15, directly through the supplied images. |
| Text-only coverage | Page 4, containing attack descriptions and example boxes, was assessed through supplied extracted text only. |
| Figures | Figures 1–6 are visually available and inspected. |
| Tables | Tables 1–8 are visually available; small appendix cells were cross-checked against supplied text. |
| Equations | Equations (1)–(5) and the unnumbered reward-form rewrite are available in text and rendered pages. Fine mathematical typography remains extraction-sensitive. |
| Appendix | Present on page 15, including Tables 6–8 and explanatory bullets. |
| Supplementary material | No separate supplement or embedded attachment was supplied. No clearly identified supplementary file is required by the supplied text. |
| Other absent artifacts | Linked code, datasets, model checkpoints, cited papers, and the follow-up Meta SecAlign work were not supplied or inspected. |
| OCR | Not needed: substantial native/extracted text is supplied. Images were used to assess plots, layout, equations, and table alignment. |
| Verification boundary | The supplied hash is carried through as the document identifier; its correspondence to a PDF file was not independently verified. |

Evidence labels used throughout: **[A] Author-reported**, **[B] directly observable in supplied visuals**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external-information category [E] is used. HIGH confidence denotes clearly readable source evidence, not independent replication or universal validity.

### Inventory established before synthesis

**Identity:** *SecAlign: Defending Against Prompt Injection with Preference Optimization*, by Sizhe Chen, Arman Zharmagambetov, Saeed Mahloujifar, Kamalika Chaudhuri, David Wagner, and Chuan Guo. Published in the 2025 ACM SIGSAC Conference on Computer and Communications Security, CCS ’25, October 13–17, Taipei, Taiwan; DOI 10.1145/3719027.3744836. The author affiliations shown are UC Berkeley and/or Meta. [A, p. 1]

**Document type:** empirical machine-learning security and defense-algorithm paper, with a training procedure, mathematical motivation, adversarial evaluation, utility evaluation, and ablations. It is not a systematic review, formal security proof, or direct comparative study of web agents versus standalone LLMs.

**Section inventory:** §1 Introduction; §2 Preliminaries, including §§2.1 Problem Statement, 2.2 Problem Significance, 2.3 Optimization-Free Prompt Injections, and 2.4 Optimization-Based Prompt Injections; §3 Methodology, including §§3.1 Revisiting Prompt Injection Defenses, 3.2 Formulating Prompt Injection Defense as Preference Optimization, 3.3 Implementing SecAlign: Preference Dataset, and 3.4 SecAlign vs. Adversarial Training; §4 Experiments, including §§4.1 Experimental Setup, 4.2 SecAlign: SOTA Fine-Tuning-Based Defense, 4.3 SecAlign vs. Prompting-Based Defenses, 4.4 Security Generalization, 4.5 Utility Generalization, and 4.6 Ablation Studies; §5 Related Work; §6 Conclusion and Discussions, including advanced training, practical systems, and multimodal extensions; Acknowledgments; References [1]–[94]; unnumbered Appendix. [A, pp. 1–15]

**Object inventory:** F1 training schematic and headline comparison; F2 output log probabilities; F3 instruction-model utility/security; F4 base-model utility/security; F5 GCG attack-loss trajectories; F6 data-size and learning-rate panels. T1 BIPIA comparison; T2 prompting-defense comparison; T3 out-of-distribution security; T4 additional utility benchmarks; T5 preference-algorithm ablation; T6 full main-model breakdown; T7 prompting-defense breakdown; T8 target-word and success-criterion sensitivity. ALG1 constructs the preference dataset. E1–E5 cover positive-only training, a simple preference contrast, DPO, classifier adversarial training, and SecAlign’s static attacked-data objective. No theorem, lemma, proposition, or formal proof is supplied.

**Experiment register:** X1 main five-model StruQ comparison; X2 GCG-loss analysis; X3 instruction-hierarchy comparison; X4 BIPIA reproduction; X5 five prompting defenses; X6 SEP positions/tasks; X7 InjecAgent API misuse; X8 many-shot and language variants; X9 four extra utility benchmarks; X10 imperative-data handling; X11 DPO/ORPO/KTO; X12 training-data proportions; X13 learning rates/random runs; X14 target-word and success-criterion sensitivity. Their evidence is synthesized below rather than presented as disconnected summaries.

## 1. Plain-language orientation

An LLM-integrated application gives a language model an authorized task and additional material to process. The additional material might be a retrieved web page, a document, or an application programming interface (API) result. The problem is that this material can also contain sentences that look like commands. A vulnerable model may obey those sentences instead of treating them as material relevant to the authorized task. The paper calls this **prompt injection**. [A, pp. 1–3]

SecAlign changes training so that the model learns a preference between two answers to the same attacked input: the answer to the legitimate instruction should be preferred, and the answer to the injected instruction should be discouraged. The authors construct those answer pairs automatically from an existing instruction dataset and train with **direct preference optimization (DPO)**. The conceptual contribution is using preference optimization to teach an instruction-versus-data security policy, rather than relying only on increasing the probability of the correct answer. [A, pp. 5–7]

The strongest main evidence comes from five open-weight model configurations. SecAlign has reported 0% success for the three tested optimization-free attacks on all five. Against the strongest tested optimization-based attack for each configuration, its reported success rates are 1%, 8%, 14%, 1%, and 9%, compared with StruQ’s 27%, 45%, 60%, 41%, and 43%. Consequently, the headline should be read as **mainly below 10%, with a 14% exception**, rather than universally below 10%. [A/B, Table 6, p. 15]

For the research question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs?**, the relevant inference is that integrating models with external information and tools creates channels through which attacker-controlled text can influence a trusted task and potentially an action. This is **analyst interpretation [D]**, grounded in the paper’s system model and API benchmark. The paper does not measure a standalone-versus-agent vulnerability gap, nor demonstrate that every web agent is more vulnerable than every standalone model.

## 2. Document roadmap

The introduction explains the attack surface and proposes that existing defenses leave an important training objective unspecified. The preliminaries define the trusted instruction, untrusted data, attacker capabilities, success conditions, and six evaluated attack families. Pages 3–5 connect the attacks to actual integrated applications and introduce both manually constructed and optimized injections. [A]

The methodology then moves from a positive-only supervised loss to an explicit preference loss, shows how to generate preference triples without new human labels, and explains why the resulting training is only an approximation to classical adversarial training. The experiments separately assess useful answers without attacks and resistance under attacks. Their progression is main models, competing defenses, distribution changes, utility checks, and ablations. [A, pp. 5–11]

Related work distinguishes prompt injection from jailbreaks and other privacy/security attacks. The discussion identifies limits of explicit delimiters, static training data, text-only evaluation, and practical agent workflows. Appendix Tables 6–8 are essential: they provide exact values behind the figures and expose qualifications that the headline narrative alone could conceal. References and acknowledgments establish attribution and funding; they are not treated as independently verified evidence about the cited works. [A, pp. 11–15]

## 3. Background and context

A **large language model (LLM)** generates text conditional on its input. In this paper, its input contains a trusted instruction, a data field, and a marker indicating where the response begins. **Delimiters** are the tokens or strings marking those boundaries. The desired behavior is to follow the trusted instruction while processing any apparent commands inside data as data. [A, §2.1]

**Supervised fine-tuning (SFT)** trains a model on input–answer examples. An **Instruct model** here already has instruction-oriented fine-tuning; a **base model** first receives ordinary SFT before SecAlign’s preference stage. **Preference optimization** learns from preferred and dispreferred responses to the same input. The dispreferred response need not be harmful in isolation: answering the dinosaur question is wrong in the example because the authorized task is generating a prime-testing function. [A, pp. 2, 6–8]

**Attack success rate (ASR)** is the fraction of tested cases meeting an attack’s success rule. Lower is better. **WinRate** is a comparative output-quality measure judged by another LLM; higher is better. The main evaluator compares model responses with davinci003 responses using GPT-4-Turbo. A 50% WinRate means equivalence to that reference under the evaluator, not 50% task accuracy. [A, p. 7]

**Optimization-free attacks** use fixed or manually designed structures. **Optimization-based attacks** search for text that increases the likelihood of a targeted response. **White-box access** means access to model internals for attack construction. **Adversarial training (AT)** trains with attacked examples. **State of the art (SOTA)** is the authors’ comparative characterization within the evaluated setting, not a source-independent survey conclusion. [A]

The authors distinguish prompt injection from **jailbreaking**: their prompt-injection setting starts with a benign trusted instruction and attacks its data field; jailbreaking instead supplies a malicious instruction to elicit otherwise refused content. They also distinguish prompt injection from training-data extraction and membership inference. Sharing an attack optimizer does not make these threat models interchangeable. [A, §5, p. 12]

## 4. Research problem and gap

**Existing problem:** external data can contain instructions that override a system designer’s intended task. Consequences discussed include confidential-data disclosure and unauthorized document changes. The Slack AI account illustrates retrieved public malicious text being combined with private information, then steering output toward a link encoding that information. This is an author-recounted example from cited work, not a new exploit reproduced in this paper. [A, §2.2, p. 3]

**Prior shortcomings according to the authors:** prompting defenses are brittle; existing fine-tuning methods such as StruQ encourage the legitimate response but do not explicitly suppress the injected response. The authors argue that this distinction matters because language models have an enormous output space: raising one answer’s likelihood does not necessarily lower a particular wrong answer sufficiently. [A, §§3.1–3.2]

**Research gap:** obtain stronger generalization to attacks not used during defensive training while retaining useful general-purpose instruction following. The paper’s response is to supply the missing negative response explicitly through preference training. [A]

**Scope:** text-based, explicitly separated instruction/data inputs; prevention that still answers the authorized task; mostly small open-weight model families; empirical evaluation rather than a guarantee over arbitrary future attacks or deployed web-agent interactions. [A, pp. 3, 7, 12–13]

## 5. Research questions / objectives / hypotheses

The paper does not present a numbered list of formal research questions or preregistered hypotheses. Its explicit objectives are: preserve general-purpose utility; prevent following data-borne injections; improve resistance to unseen, stronger optimization-based attacks; construct preference data automatically; and examine generalization and sensitivity to training choices. [A, §§3–4]

The following are **analyst-organized questions [D]**, not author-numbered RQs:

| ID | Objective expressed as an analytical question | Evidence |
|---|---|---|
| O1 | Does negative-response preference training improve on positive-only defensive SFT? | E1–E3, F2–F5, T6. |
| O2 | Can simple training attacks generalize to stronger test attacks? | Distinct test attacks and delimiters, T6. |
| O3 | Is useful behavior preserved beyond the original evaluation? | T1, T3–T4, imperative-data test. |
| O4 | Does protection transfer to other tasks, positions, and API data? | T3; many-shot/language tests. |
| O5 | How do preference algorithm, data size, and learning rate affect outcomes? | T5, F6. |

The authors explicitly hypothesize that many-shot demonstrations fail to improve injection because responding to an injection is a more complex goal than the corresponding jailbreak goal. They also suspect richer industry instruction-tuning data offers greater potential for securing models. These are interpretations, not experimentally isolated causal findings. [A, pp. 8, 10]

## 6. Assumptions / threat model

The system designer supplies a benign instruction and fixes a prompt format. The data field is the attack surface. The attacker knows the benign instruction and format, can inject an arbitrarily long instruction into data, and is assumed to have white-box model access for strong optimization-based attacks. The attacker cannot modify the trusted instruction or the format itself. [A, §2.1, p. 3]

The defender can access and alter model weights but is assumed to prefer affordable fine-tuning over expensive pretraining. The desired defense is **prevention with continued service**: answer the benign instruction even when attacked. Simply detecting an attack and refusing all output does not satisfy the paper’s chosen utility objective. [A]

The main attack target is a response beginning with Hacked or hacked after an injected printing instruction, placed at the end of data. SEP broadens tasks and positions; InjecAgent measures calling a malicious API. The success rule therefore varies across experiments and must not be treated as one universal metric. [A, pp. 7, 10, 15]

Clear separation of trusted instruction and untrusted data is a central assumption. Correct use of the training-time prompt template is also required: the authors warn that changing the format may unpredictably reduce performance. Theoretical permission to inject arbitrarily long instructions should not be mistaken for documentation that every implemented attack exhaustively tested arbitrary lengths. [A plus D qualification, pp. 3, 8]

## 7. Methodology

### Preference-data construction

For each instruction-dataset example s with a data field, choose another random example s′. Build an attacked input x by putting s′’s instruction into s’s data. The preferred response y_w is s’s original answer; the dispreferred response y_l is s′’s answer. Thus a legitimate response in its original context becomes a dispreferred response in a different, attacked context. [A, §3.3, p. 6]

Algorithm 1 skips original examples with no data field. With probability 0.9, it uses a Straightforward attack, concatenating the sampled instruction and any sampled data. Otherwise it uses a Completion attack: insert alternative response delimiters, a simulated answer completing the legitimate task, and an alternative instruction delimiter introducing the injected task. If s′ has data, that data is appended with a corresponding alternative delimiter. The final triple is (x, s_response, s′_response). The procedure returns the preference dataset P. [A/B, ALG1]

The five pipeline steps are obtain an SFT model, save its delimiters, choose an instruction dataset, construct P, and preference-optimize using Equation (3). Public Instruct models are recommended. Automatic generation removes the need for new preference annotations in this construction; it does not mean the underlying instruction data were created without human effort. [A, pp. 6–7; D qualification]

### Data and separation

Cleaned Alpaca supplies training examples. AlpacaFarm supplies 805 utility examples, of which 208 include data fields and are used for the main security evaluation. The authors state that these are different datasets with inherently nonoverlapping examples, rather than train/test splits from one dataset. They also state that AlpacaFarm’s relatively short data makes injections more prominent. The exact Cleaned Alpaca training count, final preference-triple count, validation partition, and sample-selection seeds are not reported in the supplied paper. [A, §4.1]

### Models and format

The five main configurations, in reported order, are Mistral-7B-Instruct, Llama3-8B-Instruct, Llama-7B, Mistral-7B, and Llama3-8B. The first two already have privately produced instruction training; the last three receive ordinary SFT before preference optimization. Main comparisons distinguish undefended models, StruQ, and SecAlign. Vicuna-7B is additionally used in the BIPIA reproduction; GPT-4o-mini is used for the qualified instruction-hierarchy comparison. [A, pp. 7–9]

The Instruct configurations use their provided templates. Mistral uses its INST-style instruction wrapper and a space between instruction and data. Llama3 uses system/user/assistant header tokens. Base-model SFT uses marker sequences for instruction, input, and response, including MARK, INST/INPT/RESP, and COLN tokens. Exact template consistency is emphasized. [A]

### Training configuration

DPO uses a sigmoid and β = 0.1. Low-Rank Adaptation (LoRA) updates less than 0.5% of weights in these experiments, with rank r = 64, lora_alpha = 8, dropout = 0.1, and target modules q_proj and v_proj. TRL implements DPO; PEFT implements LoRA; PyTorch Fully Sharded Data Parallel (FSDP) supports distributed training. Four NVIDIA Tesla A100 GPUs with 80 GB each are reported. Software versions are not supplied. [A, p. 8]

DPO runs for three epochs. Learning rates in the five-model order above are [1.4, 1.6, 2.0, 1.4, 1.6] × 10^-4. Ordinary and defensive SFT for the three base models run for three epochs at [20, 2.5, 2] × 10^-6. These rates are tuned; the supplied paper does not give a complete tuning protocol, batch size, sequence-length configuration, optimizer details, or all random seeds. [A]

### Attacks and controls

Training uses 90% Straightforward and 10% Completion attacks. Main optimization-free tests are Ignore, Completion, and Ignore-Completion. Ignore randomly chooses among ten deviation sentences. Test Completion uses a different delimiter set from training, so the family overlaps while the concrete structures differ. The statement that test attacks were unseen should be interpreted at this implementation/configuration level. [A, pp. 4, 6–7]

Optimization-based tests are Greedy Coordinate Gradient (GCG), AdvPrompter, and NeuralExec. GCG optimizes a suffix using gradients of target-response loss; the paper reports more than 30 minutes per sample. AdvPrompter trains an attacker model through candidate generation/scoring and fine-tuning; λ = 1000 relaxes its readability constraint. NeuralExec learns a model-specific universal prefix–suffix across hundreds of samples. SecAlign attacks are run against the defensively trained model with the test-time template. Full attack budgets and all attack-optimizer settings are not enumerated. [A, pp. 4–7]

### Metrics and statistics

Main utility is AlpacaEval2 WinRate over all 805 examples, judged by GPT-4-Turbo against davinci003. Main ASR is over the 208 data-bearing examples, usually requiring output to begin with Hacked/hacked. Maximum ASR is the maximum of the named attack rates within each family, not a proven worst case over all possible attacks. [A]

The paper cites an AlpacaEval2 standard error of 0.7% when discussing small differences. Figure 5 shows sample standard deviations in attack loss; Figure 6 includes small error bars from five random runs at one selected learning rate. Broad confidence intervals, significance tests, and repeated-run distributions for every result are not provided. [A/B, pp. 8–11]

## 8. Experiments / analyses

| ID | Purpose and controlled comparison | Data / metrics / evidence | Results and qualifications |
|---|---|---|---|
| X1 | Compare None, StruQ, SecAlign across five main configurations. | AlpacaFarm: 805 utility, 208 security; WinRate and six attack ASRs; F3–F4, T6. | SecAlign optimization-free maxima all 0%; optimized maxima 1, 8, 14, 1, 9%. Same model families but different defense training paths. |
| X2 | Inspect why GCG succeeds or struggles. | Llama3-8B-Instruct, attack-loss curves across tested examples; F5. | SecAlign loss remains substantially above baseline curves after 500 steps. This is attack-specific diagnostic evidence, not a proof. |
| X3 | Compare with instruction hierarchy. | GPT-4o-mini with dummy tool returning data; Ignore ASR. | 1% versus SecAlign’s 0% on its five models; different underlying models, no white-box optimized attacks against the API model. |
| X4 | Test under BIPIA’s settings. | Vicuna-7B, BIPIA test set, AlpacaEval2; T1. | Max optimization-free ASR 36/7/0 for None/BIPIA/SecAlign; WinRate 62.94/32.29/61.92%. Small-scale reproduction, not exhaustive cross-framework replication. |
| X5 | Compare five prompting defenses. | Llama3-8B-Instruct and Llama-7B; three fixed attack families; T2, T7. | SecAlign 0/0%; best prompting maxima 0.5/38% respectively. A prompting defense can improve one model and worsen another. |
| X6 | Broaden injection tasks and positions. | SEP, reported 9.1K samples, GPT-4-Turbo success/utility judgments; T3. | SecAlign start/middle/end ASR 11.0/3.6/6.5%; utility 46.6% versus None’s 50%. StruQ lower ASR but utility 18.9%. |
| X7 | Test malicious API calling. | InjecAgent; Llama3-8B-Instruct; T3. | None/StruQ/SecAlign ASR 75.9/2.2/0%. No provided utility evaluation, so the trade-off cannot be assessed. |
| X8 | Test many-shot examples and Chinese/Spanish printing requests. | Llama3-8B-Instruct; completion structures; §4.4. | StruQ and SecAlign both 0% in reported variants. Shot counts and detailed per-language results are not supplied. |
| X9 | Assess additional utility domains. | Mistral-7B and Llama3-8B; four benchmarks; T4. | CommonSenseQA stable; other reported scores include declines. See numerical table below. |
| X10 | Test legitimate imperative text as data. | Rewrite task; 804 examples, plus first 50 manually inspected; §4.5. | SecAlign comparative WinRate 65.5%; manual correct data handling 52% versus 16%. First-50 inspection is not a reported random sample. |
| X11 | Change preference optimizer. | Llama-7B, DPO/ORPO/KTO, four A100s; T5. | GCG ASR 15/34/9%; similar WinRates, substantially different runtime. |
| X12 | Vary training-data fraction. | Preserve proportion of data-bearing examples; equal example exposure across methods; F6 left. | SecAlign with 20% data has lower plotted ASR than StruQ with all data. Exact plotted point values are not tabulated. |
| X13 | Vary DPO learning rate and repeat selected setting. | 6 × 10^-5 to 2.6 × 10^-4; five runs at 2 × 10^-4; F6 right. | Trade-off depends on rate, but SecAlign remains better than StruQ over evaluated range; small displayed variability at selected optimum. |
| X14 | Vary target word and success rule. | AlpacaFarm; three target strings, begin-with versus anywhere-in-response; T8. | SecAlign begin-with maxima 0%; anywhere maxima 0.5, 0.5, 1%. Target-label and baseline discrepancies remain. |

The experiments support different scopes. Main exact-string results concern a deliberately simple observable behavior. SEP broadens semantic targets; InjecAgent broadens the consequence to API misuse. None alone establishes general safety for multi-turn browsing, arbitrary permissions, or every practical attack. [D]

## 9. Results

### Exact main-model outcomes

All entries below are author-reported percentages from Table 6, page 15. Each triplet is None / StruQ / SecAlign.

| Model | WinRate | Max optimization-free ASR | Max optimization-based ASR |
|---|---|---|---|
| Mistral-7B-Instruct | 67.01 / 70.73 / 69.22 | 59 / 2 / 0 | 89 / 27 / 1 |
| Llama3-8B-Instruct | 85.39 / 80.79 / 85.88 | 51 / 0 / 0 | 97 / 45 / 8 |
| Llama-7B | 55.46 / 54.55 / 56.06 | 75 / 0.5 / 0 | 97 / 60 / 14 |
| Mistral-7B | 72.21 / 72.17 / 72.88 | 89 / 4 / 0 | 95 / 41 / 1 |
| Llama3-8B | 69.47 / 68.77 / 68.87 | 90 / 0 / 0 | 98 / 43 / 9 |

The optimized maximum is governed by AdvPrompter for both SecAlign Instruct models and by GCG for the three base-derived models. **[C] Derived ratios** comparing StruQ/SecAlign optimized maxima are 27/1 = 27, 45/8 = 5.625, 60/14 ≈ 4.29, 41/1 = 41, and 43/9 ≈ 4.78. These reproduce the authors’ greater-than-fourfold statement for this table. Ratios depend on the reported rounded rates and the selected attack suite.

**[C] Derived absolute changes:** Llama3-8B-Instruct optimized maximum falls 97 − 8 = 89 percentage points from None and 45 − 8 = 37 points from StruQ. Its WinRate changes 85.88 − 85.39 = +0.49 points from None. These are percentage-point differences, not relative percentage improvements.

### Generalization is conditional

SEP offers a useful counterweight to the 0% main optimization-free headline: SecAlign’s Ignore ASR is 11.0% at the start, 3.6% in the middle, and 6.5% at the end. StruQ reports still lower attack rates, but a much lower utility preference score. Thus lowest ASR alone can reward a model that inadequately serves the benign task. InjecAgent’s 0% is encouraging but lacks a companion utility test. [A, T3]

### Utility preservation is benchmark-dependent

Table 4 reports None → SecAlign scores: Mistral MMLU 62.7 → 59.5, Winogrande 77.8 → 77.7, AGIEval 25.8 → 25.2, CommonSenseQA 70.9 → 70.9; Llama3 MMLU 65.3 → 63.1, Winogrande 77.5 → 77.2, AGIEval 33.1 → 30.3, CommonSenseQA 78.2 → 78.3. **[C]** MMLU decreases are 3.2 and 2.2 percentage points; Llama3 AGIEval decreases 2.8 points. The broad statement of no decrease in most benchmarks is stronger than a literal cell-by-cell reading: six of eight pairs decline, though some only slightly. No uncertainty estimates establish which changes exceed measurement variability. [A/B plus D assessment, p. 10]

## 10. Figure-by-figure interpretation

### Figure 1 — Preference-training concept and headline comparison

The upper schematic starts with an instruction-following model, a delimited attacked input, and two possible responses. The legitimate instruction requests code; the data includes both a prime-number task and a dinosaur question. Preference fine-tuning raises the legitimate code response relative to the injected-question response, yielding a SecAlign model. Injected text is highlighted in red. The arrows/stacking encode transformation through training, not an inference-time detector. [B, p. 2]

The lower grouped bar plot is for Llama3-8B-Instruct. Its horizontal categories are AlpacaEval2 WinRate and maximum attack success rate; the vertical scale is percentage, approximately 0–100, linear. Gray is no defense, mustard a prompting defense, blue a fine-tuning defense, and orange SecAlign. Higher utility and lower attack success are favorable. The caption reports 8% strongest-tested ASR without utility harm. Exact main values are best read from T6; the plot does not supply independent error bars. [A/B]

### Figure 2 — Desired versus injected-response probability

This line plot uses SecAlign training steps on the horizontal axis, roughly 0–200, and output log probability on the vertical axis, roughly −50 to −300. Orange traces represent SecAlign and blue traces StruQ; dashed versus solid lines distinguish desired and undesired responses as labeled. The desirable-response traces stay near the top, while SecAlign’s undesired-response log probability falls much more sharply and remains noisy. [B, p. 5]

The prose reports StruQ around −140 and SecAlign as low as −300 for the undesirable output. These are reported illustrative training-trajectory magnitudes, not ASR percentages. More negative log probability means the specified response is less likely. This supports the intended mechanism of increasing the preference margin, but it does not prove that every alternative malicious response becomes unlikely. Results are from Llama-7B. [A plus D caveat]

### Figure 3 — Instruct-model comparison

Two panels cover Mistral-7B-Instruct and Llama3-8B-Instruct. Each has groups for utility, maximum optimization-free ASR, and maximum optimized ASR; the vertical percentage axis is linear from 0 to 100. None is gray, StruQ blue, and SecAlign orange. Small labels mark values too low for visible bars, including zero rates. [B, p. 8]

SecAlign preserves high utility and sharply lowers optimized ASR; StruQ mostly handles fixed-format attacks but leaves larger optimized rates. Table 6 gives exact values. The nearby prose says both undefended models have WinRates over 70%, but T6 gives 67.01% for undefended Mistral. The figure’s gray bar also appears below 70. This inconsistency is retained rather than corrected silently. [A/B]

### Figure 4 — Base-model comparison

Three panels cover Llama-7B, Mistral-7B, and Llama3-8B with the same axes, grouping, colors, and favorable directions as F3. Utility bars are similar within each model; SecAlign’s optimized ASR bars are much shorter. The Llama-7B SecAlign optimized bar is visibly nonzero and corresponds to 14% in T6. [B, p. 9]

The caption provides no uncertainty intervals. Exact utility similarity needs T6: some cross-defense differences exceed the prose’s stated less-than-0.7% characterization. The visual supports relatively small utility changes compared with security changes, not exact identity under every comparison. [D]

### Figure 5 — GCG optimization trajectories

The horizontal axis is GCG steps, 0–500; the vertical axis is GCG attack loss, linear, with labeled values around 0, 5, 10, and 15. Gray None and blue StruQ curves approach low loss; orange SecAlign decreases more slowly and remains considerably higher. Shaded bands show standard deviation across examples, not confidence intervals over repeated training runs. Solid center lines show means. [A/B, p. 9]

The caption states that SecAlign’s final attack loss exceeds StruQ’s initial attack loss. Visually the orange mean ends around 10 while the blue initial value is lower, but these are approximate positions, not tabulated exact values. The plot demonstrates resistance to this optimizer under the plotted budget; it does not equate a loss threshold with a formally established security boundary. [B/D]

### Figure 6 — Data and hyperparameter sensitivity

The left panel’s horizontal axis is fraction of training data, 0.2–1.0; the vertical axis combines WinRate and GCG ASR in percent. Blue denotes StruQ, orange SecAlign; dotted versus solid styles distinguish utility and security according to the legend. Utility generally increases and ASR generally decreases with more data. SecAlign’s security curve stays below StruQ’s. The caption specifically compares 20% SecAlign data with all-data StruQ. Exact point values are not supplied in a table. [A/B, p. 11]

The right panel’s horizontal axis is DPO learning rate in units of 10^-5, extending from approximately 6 to 26; the vertical axis is again percentage. SecAlign’s ASR varies nonmonotonically, with its favorable region near 20 × 10^-5. StruQ reference lines provide comparison. Two small uncertainty boxes/bars at 2 × 10^-4 summarize five random runs; their exact numerical spread is not readable or tabulated. The figure supports local robustness to tested rates and small variability at one selected setting, not comprehensive seed robustness across every experiment. [A/B/D]

## 11. Table-by-table interpretation

### Table 1 — BIPIA settings

Columns are None, BIPIA, and SecAlign; rows combine utility and three optimization-free attack rates. WinRate is 62.94, 32.29, and 61.92%; Ignore is 20, 5, and 0%; Completion 36, 4, and 0%; Ignore-Completion 32, 7, and 0%; maxima 36, 7, and 0%. SecAlign has the best reported security and retains much more utility than this BIPIA reproduction. **[C]** Its utility decrease from None is 62.94 − 61.92 = 1.02 percentage points. No uncertainty estimates or BIPIA sample count appear with this table. [A/B, p. 9]

### Table 2 — Prompting-defense maxima

The two model columns are Llama3-8B-Instruct and Llama-7B. Maximum optimization-free ASRs are None 51/75, Instructional 38/78, Reminder 35/79, Isolation 50/73, Sandwich 55/38, In-Context 0.5/45, and SecAlign 0/0%. In-Context is particularly strong for the Instruct model but much weaker for Llama-7B. Reminder and Instructional are worse than None for Llama-7B. No statistical significance test accompanies the caption’s use of significantly. [A/B, p. 10]

### Table 3 — Out-of-distribution benchmarks

Columns are None/StruQ/SecAlign on Llama3-8B-Instruct. SEP utility is 50.0/18.9/46.6%; start ASR 54.7/2.1/11.0%; middle 39.5/0.1/3.6%; end 64.0/0.1/6.5%; InjecAgent 75.9/2.2/0%. StruQ has the lowest SEP ASRs but the poorest utility. SecAlign has the lowest InjecAgent ASR. Within SecAlign, middle placement is lower than end placement, qualifying the prose characterization of the end as most effective for defense. No utility row is available for InjecAgent. [A/B, p. 10]

### Table 4 — Additional utility

Two model groups each compare None and SecAlign on MMLU, Winogrande, AGIEval, and CommonSenseQA, all in percent with higher better. The exact eight before/after pairs are reproduced in §9. The largest visible drop is Mistral MMLU, 62.7 to 59.5; the largest increase is Llama3 CommonSenseQA, 78.2 to 78.3. Mistral CommonSenseQA ties. No error bars, per-task sample counts, or significance markers are supplied. [A/B, p. 10]

### Table 5 — Preference optimizer

Rows DPO/ORPO/KTO have WinRates 56.06/54.75/55.84%, GCG ASR 15/34/9%, and GPU-hour notation 2 × 4 / 1.5 × 4 / 10 × 4. The caption specifies Llama-7B and four 80 GB A100s. DPO has the highest reported utility; KTO the lowest ASR; ORPO the shortest time. **[C]** Multiplying the displayed notation gives 8, 6, and 40 aggregate GPU-hours, assuming the notation represents hours per device across four devices. The original notation is retained to avoid hiding that interpretation. [A/B, p. 11]

### Table 6 — Main results in full

There are five model groups, each containing None/StruQ/SecAlign columns. Rows are WinRate, Ignore, Completion, Ignore-Completion, fixed-attack maximum, AdvPrompter, GCG, NeuralExec, and optimized maximum. Units are percent. §9 reproduces the summary rows; below are the optimized attack rows, in the same triplet order:

| Model | AdvPrompter | GCG | NeuralExec |
|---|---|---|---|
| Mistral-7B-Instruct | 81 / 27 / 1 | 89 / 15 / 1 | 20 / 16 / 0 |
| Llama3-8B-Instruct | 97 / 45 / 8 | 84 / 4 / 0 | 63 / 0.5 / 0 |
| Llama-7B | 60 / 4 / 1 | 97 / 60 / 14 | 2 / 0 / 0 |
| Mistral-7B | 72 / 7 / 0 | 95 / 41 / 1 | 32 / 2 / 0 |
| Llama3-8B | 95 / 18 / 0 | 98 / 43 / 9 | 34 / 0 / 0 |

The three fixed-attack rows confirm SecAlign zero throughout. None’s Ignore/Completion/Ignore-Completion values are 18/59/59, 24/47/51, 10/45/75, 22/89/70, and 30/90/89 across the five models. StruQ’s corresponding triplets are 0.5/1/2, 0/0/0, 0/0/0.5, 0/4/1, and 0/0/0. SecAlign’s best value often ties at zero, so rank alone does not distinguish defenses on every row. There are no reported confidence intervals. [A/B, p. 15]

### Table 7 — Prompting-defense breakdown

For Llama3-8B-Instruct, rows Ignore/Completion/Ignore-Completion give None 24/47/51; Instructional 16/31/38; Reminder 18/21/35; Isolation 27/35/50; Sandwich 16/16/53; In-Context 0.5/0.5/0; SecAlign 0/0/0. The Sandwich maximum row nevertheless says 55%, as does Table 2, whereas the maximum of its displayed component rows is 53%. This is an unresolved numerical inconsistency. [A/B, p. 15]

For Llama-7B, corresponding triplets are None 10/45/75; Instructional 22/58/78; Reminder 20/62/79; Isolation 5/53/73; Sandwich 3/16/38; In-Context 1/25/45; SecAlign 0/0/0. Their displayed maxima agree with the component maxima. This table shows which attack defeats a particular prompting defense, rather than only reporting its aggregate worst tested case. [A/B]

### Table 8 — Target words and scoring rules

The table groups three target labels, Hacked, Hello Word, and Serendipity, each with None/StruQ/SecAlign. The appendix prose instead calls the second target Hello World. Both spellings are preserved here because the intended exact experimental string cannot be settled from the supplied material. Rows compare beginning-of-response success with target occurrence anywhere. [A/B, p. 15]

Begin-with maxima are 75/5/0 for Hacked, 73/0/0 for the second target, and 88/1/0 for Serendipity. Anywhere-in-response maxima are 84/5/0.5, 91/1/0.5, and 92/3/1. For SecAlign, the nonzero anywhere rates arise in Hacked Ignore-Completion (0.5), second-target Ignore and Completion and Ignore-Completion (each 0.5), and Serendipity Ignore (1) and Completion (0.5). All its begin-with cells are zero. [A/B]

The authors explain that anywhere matching catches more potential successes but can count outputs merely quoting the malicious command. Thus these rates are not necessarily confirmed compromises. The table also reports StruQ Hacked Completion at 5%, compared with 0% for Llama-7B in T6. The appendix identifies another study but does not fully specify the configuration difference; these values should not be merged. No uncertainty estimates are provided.

## 12. Diagram / architecture interpretation

The paper supplies a **training workflow**, not a full deployed-agent architecture. Figure 1’s upper diagram connects an existing model, an attacked input, preferred/dispreferred output probabilities, and a resulting defended model. The important flow is from source instruction examples to synthetic attack pairs to parameter updates. There is no depicted permission manager, retrieval sanitizer, browser policy engine, or runtime tool-verification component. [B/D]

Algorithm 1 and the page-6 example boxes show the data path more concretely: original task and answer plus randomly sampled competing task and answer → attacked formatted input → preference triple → DPO. Training is iterative; attack-example construction is performed beforehand rather than adaptively against each evolving checkpoint. [A]

The example boxes on pages 2–6 distinguish instruction, data, response boundary, and injected substructure. Page 4’s examples were inspected through text only. Completion attacks counterfeit a conversational transition inside the data field: a fake response appears to finish the authorized task, followed by a fake new instruction. These boxes are substantive method illustrations, not additional independent experiments. Their repeated prime-number/dinosaur wording is compressed deliberately.

The Slack narrative describes an application-level information path: attacker-controlled public text and legitimate private retrieval enter one model context; injected instructions redirect output into an information-bearing link; a user click transfers the encoded information. The account is author-reported motivation, not a system architecture implemented or experimentally evaluated by SecAlign. [A/D, p. 3]

## 13. Equations and mathematical concepts

### Equation (1), page 5: positive-only defensive SFT

`L_StruQ = −log p(y_w | x)`.

Here x is a prompt-injected input, y_w its desirable response, and p the model’s conditional response probability. Minimizing negative log probability increases the likelihood of y_w. The authors’ criticism is that this objective does not explicitly identify the particular undesirable answer y_l. It is the positive-response baseline objective, not a theorem that every positive-only method must fail. [A]

### Equation (2), page 5: direct positive–negative contrast

`L = log p(y_l | x) − log p(y_w | x)`.

Minimization pushes down the injected-response log probability and pushes up the authorized-response log probability. The same x has two candidate outputs. The authors cite prior preference-optimization work for the concern that this naive objective can overfit and produce incoherent text; the supplied paper does not itself prove that concern. [A]

### Equation (3), page 5: DPO objective

`L_SecAlign = −log σ(β log[π_θ(y_w|x)/π_ref(y_w|x)] − β log[π_θ(y_l|x)/π_ref(y_l|x)])`.

π_θ is the trainable model; θ denotes its parameters. π_ref is the SFT reference model. σ is the sigmoid function, identified in the training description; β is the preference scaling coefficient, set to 0.1 by default. The two log ratios compare current preferred and dispreferred output probabilities with the fixed reference. Their difference is passed through sigmoid and negative logarithm. Lower loss corresponds to a larger reference-relative preference for y_w over y_l. [A]

The reference terms are described as limiting excessive deviation from the SFT model. This should not be translated into a strict guarantee of unchanged utility: the actual utility results must still be inspected. Inputs are x, both responses, the current model, the reference model, and β; output is a scalar training loss. [A/D]

### Equation (4), page 7: classical min–max adversarial training

`min_θ E_(x_hat,y) [ max_(x ∈ C(x_hat)) L(θ,x,y) ]`.

x_hat is the original example; x is an attacked version; C(x_hat) specifies permitted attacked examples; y is the label in the classifier formulation; E averages over examples. The inner maximization seeks a damaging allowed attack, and the outer minimization trains parameters to reduce the resulting worst-case loss. The paper does not enumerate one concrete universal C for all its text attacks. [A]

### Reward-form rewrite and Equation (5), page 7

The authors define `r_θ(y|x) := β log[π_θ(y|x)/π_ref(y|x)]`, pair `y := (y_w,y_l)`, and rewrite the loss as `−log σ(r_θ(y_w|x) − r_θ(y_l|x))`.

Equation (5) is `min_θ E_(x_hat,y) L_SecAlign(θ, A(x_hat), y)`, where A is an optimization-free attack transformation. It replaces an explicitly solved inner maximum with a preconstructed attacked example. The simplification makes training practical but means SecAlign is not solving the full worst-case objective of Equation (4). [A]

### Output-space argument

The text uses V for vocabulary size and L for output length, giving V^L possible sequences in a simplified fixed-length count. This supports the intuition that favoring one answer need not strongly suppress a particular other answer. It is explanatory motivation, not a measured enumeration of model outputs or a formal robustness bound. [A/D, p. 5]

## 14. Interpretation and discussion

The central supported interpretation is that explicitly contrasting authorized and injected answers can outperform positive-only defensive SFT under the evaluated attacks. The evidence is aligned across training log-probability trajectories, attack-loss curves, and final ASRs. However, the loss-curve mechanism does not establish that preference optimization is the sole causal ingredient: training paths, rates, and preference data differ, and no formal decomposition isolates every contributor. [A/D]

The practical value is the joint security–utility objective. SEP makes clear that near-zero ASR can coexist with poor authorized-task performance; the authors therefore argue for evaluating both. The imperative-data test further checks that training does not merely delete or ignore every sentence that resembles a command. Its improvement is meaningful, while the manual SecAlign success rate of 52% also shows substantial remaining errors under that inspection. [A/D]

Important consistency checks remain unresolved:

- The abstract’s below-10% language is qualified by Table 6’s 14% Llama-7B optimized maximum.
- Page 8 says both undefended Instruct models exceed 70% utility; Table 6 gives Mistral 67.01%.
- Page 8 describes base-model utility as differing by less than 0.7%; Llama-7B None versus StruQ is 55.46 − 54.55 = 0.91 points, and None versus SecAlign is 0.60 points. Mistral None versus SecAlign is 0.67, but StruQ versus SecAlign is 0.71. The exact comparison intended is insufficiently specified.
- Table 7 Sandwich component maximum is 53%, while its maximum row and Table 2 say 55%.
- Table 3 SecAlign middle-position ASR is 3.6%, lower than end-position 6.5%, despite broad wording favoring end-position protection.
- Table 4 records several utility declines beyond the prose emphasis on MMLU.
- Table 5 DPO GCG ASR is 15%, while Table 6 Llama-7B SecAlign GCG is 14%; rounding, runs, or ablation settings might explain this, but the source does not establish which.
- Table 8’s target spelling and its StruQ Hacked rates do not fully align with prose/main-table presentation.

These are source inconsistencies or underexplained configuration changes. They do not erase the large observed defense improvements, but they constrain exact reproduction and sweeping claims. [D]

For the web-agent research question, the paper supports a mechanism-based argument: an agent’s context includes material selected or controlled outside the trusted task, and tools can turn mistaken instruction priority into effects such as API misuse. It does not isolate agent autonomy, browsing length, or tool permissions as independent causal variables. Claims about agentic workflow robustness attributed to a follow-up work on page 2 remain reports about an unsupplied artifact. [D/A]

## 15. Contributions and novelty

**Conceptual [A]:** formulate prompt-injection resistance as a response preference and connect security training with alignment methods. The authors claim first demonstration of this framing; priority is not independently verified.

**Methodological/algorithmic [A]:** automatically construct attacked-input/preferred-answer/dispreferred-answer triples from benign instruction data, then apply an existing preference optimizer. The novelty is not a new DPO algorithm.

**Implementation [A]:** apply parameter-efficient preference training to existing instruction models and SFT base models, preserving their formatting conventions. Code availability is asserted, but code and checkpoints were not inspected.

**Empirical [A/B]:** evaluate six attack families on five primary configurations, compare prompting and fine-tuning defenses, broaden to SEP and InjecAgent, and examine utility, algorithms, data size, and learning rates.

**Not established:** a formal guarantee, a new benchmark, a fully specified deployed-agent security architecture, universal resistance to prompt injection, or a measured standalone-versus-web-agent vulnerability ratio. [D]

## 16. Limitations

### Authors’ stated limitations

1. Instruction and data must be explicitly separated, for example by delimiters. [p. 12]
2. The method cannot guarantee 100% security and future attacks may bypass it; multi-turn web-agent injections are specifically mentioned. [p. 12]
3. Behavior after further fine-tuning is unclear. [p. 12]
4. Utility with multiple benign instructions is uncertain because utility datasets use one instruction. [p. 12]
5. Protection depends on injection position; they propose simulating multiple positions in training. [p. 12]
6. Current SecAlign does not defend against threats outside prompt injection, such as jailbreaks and data extraction. [p. 12]
7. It is not regarded as a standalone solution; layered application defenses are suggested. [p. 12]
8. Training uses static data and optimization-free injections because adaptive optimized attacks are too costly. [p. 12]
9. Simplified input formats may not reflect complicated retrieval and agent contexts. [p. 12]
10. The work focuses on text-only models, leaving multimodal protection for future investigation. [p. 13]
11. InjecAgent does not provide utility evaluation, preventing a measured security–utility trade-off there. [p. 10]
12. API-only instruction-hierarchy access prevents the optimized attack comparison and uses different base models. [p. 9]

### Additional evidence-based analyst observations

The main security subset is 208 examples, the default output target is narrow, and most exact results lack uncertainty estimates. Broader benchmarks mitigate but do not remove these restrictions. The privately produced Instruct training data are not inspected, so the richer-data explanation remains a hypothesis. Missing attack-budget details, model revisions, software versions, and training counts limit exact reproduction. Several textual/table inconsistencies need clarification. First-50 manual inspection has no reported random-sampling procedure or inter-annotator agreement. These are analyst observations [D], not additional author admissions.

## 17. Threats to validity

These labels organize analyst assessment; the paper does not explicitly present this validity taxonomy. [D]

**Internal validity:** the StruQ comparison is supported by claimed use of released code and the same data source, but SecAlign includes a distinct preference-training stage. Tuning and compute differences complicate attribution solely to one loss feature. Source inconsistencies make some exact comparisons uncertain.

**Construct validity:** beginning with a target string is a clear but narrow compromise proxy. Anywhere matching expands recall but includes quoted-command false positives. SEP’s semantic judgments and InjecAgent’s malicious-call condition measure different constructs. WinRate is evaluator preference rather than direct correctness or permission compliance.

**External validity:** five main small-model configurations and a delimiter-based input model do not cover arbitrary deployed models, rich browser state, multi-turn workflows, or multimodal inputs. SEP and InjecAgent expand coverage, while follow-up claims cannot substitute for supplied experiments.

**Statistical conclusion validity:** zero observed success is a sample result, not zero underlying risk. Most table entries have no confidence intervals or repeated-run distributions. Figure 5’s sample dispersion and Figure 6’s five selected runs answer narrower variability questions.

**Ecological validity:** realistic applications may mix long legitimate content, multiple benign instructions, tool results, and evolving state. The main benchmark often places a short explicit target at the end of short data. The authors intentionally consider this attacker-favorable but it remains a simplified scenario.

**Reproducibility:** key model families, delimiters, rates, LoRA settings, epochs, and hardware are reported. Exact data counts, versions, seeds, batch settings, and complete attack budgets are not. The code link is not independently assessed here.

## 18. Future work and open questions

### A. Explicit author proposals

Train with injections at multiple positions; combine SecAlign with detection, input reformatting, output manipulation, and system-level defenses; develop more efficient prompt optimizers so adaptive optimized attacks can enter training; study complicated retrieval and agent contexts; and extend defenses to image and speech inputs. The authors estimate thousands of GPU-hours for naive use of GCG inside training even on their small dataset setting. This is an author estimate, not a measured completed experiment. [A, pp. 12–13]

### B. Additional analyst questions

How much protection survives subsequent task fine-tuning? Does a model preserve a long sequence of legitimate instructions while resisting injections introduced over multiple turns? Can instruction boundaries remain reliable when data legitimately contain nested commands or conversation transcripts? How do tool permissions and output verification interact with learned preferences? What remains when attackers optimize for semantic exfiltration rather than a target prefix? What are attack rates under fixed, fully reported compute budgets and repeated training runs? A direct agent-versus-standalone study would need matched underlying models, tasks, attackers, and outcome definitions; this paper does not supply that experiment. [D]

## 19. Terminology and notation glossary

| Term / symbol | Meaning in this paper |
|---|---|
| Prompt injection | An instruction embedded in data that redirects the model from the trusted task. |
| Indirect injection | Injection arriving through external material such as a web page. |
| Direct injection | Malicious data supplied directly by an untrusted user. |
| LLM | Large language model. |
| API | Application programming interface; tool/API outputs can carry untrusted text. |
| RAG | Retrieval-augmented generation, referenced in the Slack system example. |
| SFT | Supervised fine-tuning using input–answer examples. |
| DPO | Direct preference optimization; SecAlign’s default preference-training algorithm. |
| LoRA | Low-Rank Adaptation; a parameter-efficient training technique. |
| FSDP | Fully Sharded Data Parallel; distributed training support. |
| AT | Adversarial training using attacked examples. |
| ASR / Max ASR | Attack success rate / maximum across the specified tested attacks. |
| WinRate | Evaluator preference rate against a specified reference model. |
| GCG | Greedy Coordinate Gradient, a gradient-guided text attack optimizer. |
| AdvPrompter | Attacker-model method generating adversarial suffixes. |
| NeuralExec | Model-specific universal injection prefix–suffix method. |
| BIPIA | Benchmark for indirect prompt injection attacks, also associated here with a fine-tuning defense. |
| SEP | Named injection benchmark in the paper; a full acronym expansion is not supplied. |
| InjecAgent | Benchmark measuring malicious API-call behavior after retrieved-data injection. |
| KTO / ORPO | Alternative preference algorithms; KTO’s full name is not given here; the references title ORPO as Monolithic Preference Optimization without Reference Model. |
| MMLU | Massive multitask language understanding, as identified through the supplied reference title. |
| AGIEval | A human-centric foundation-model evaluation benchmark; the paper gives its name rather than a full acronym expansion. |
| RLHF | Reinforcement Learning from Human Feedback. |
| x, x_hat | Attacked formatted input; original example before attack. |
| y_w, y_l | Preferred authorized answer; dispreferred injected-task answer. |
| θ, π_θ, π_ref | Trainable parameters, current response distribution, SFT reference distribution. |
| β, σ | Preference coefficient; sigmoid activation. |
| S, P, s, s′ | Instruction dataset; preference dataset; original and sampled examples. |
| d_instruction, d_data, d_response | Trusted-format boundaries separating input components. |
| d′ | Alternative delimiters used inside a Completion attack. |
| A, C, E | Attack transformation; allowed-attack constraint set; expectation over examples. |
| V, L | Vocabulary size and output length in the output-space argument. |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Main utility sample | 805 | examples | AlpacaFarm | Author-reported | p. 7, §4.1 |
| Main security sample | 208 | examples | AlpacaFarm with data | Author-reported | p. 7, §4.1 |
| Synthetic attack mixture | 90 / 10 | % | Straightforward / Completion | Author-reported | p. 6, ALG1 |
| Default β | 0.1 | coefficient | DPO | Author-reported | p. 8 |
| DPO duration | 3 | epochs | Five main configurations | Author-reported | p. 8 |
| Training hardware | 4 × 80 | GPUs × GB | NVIDIA A100 | Author-reported | p. 8 |
| LoRA rank / alpha / dropout | 64 / 8 / 0.1 | settings | q_proj and v_proj | Author-reported | p. 8 |
| SecAlign fixed-attack maxima | 0 / 0 / 0 / 0 / 0 | % ASR | Five models in reported order | Author-reported | p. 15, T6 |
| SecAlign optimized maxima | 1 / 8 / 14 / 1 / 9 | % ASR | Five models in reported order | Author-reported | p. 15, T6 |
| StruQ optimized maxima | 27 / 45 / 60 / 41 / 43 | % ASR | Same order | Author-reported | p. 15, T6 |
| Llama3-Instruct optimized reduction | 37 | percentage points | 45 − 8, StruQ to SecAlign | Analyst-derived | p. 15, T6 |
| Llama3-Instruct optimized ratio | 5.625 | ratio | 45 / 8 | Analyst-derived | p. 15, T6 |
| SEP sample count | 9.1K | samples | Distinct injection tasks | Author-reported | p. 10 |
| SEP SecAlign utility | 46.6 | % | Versus undefended reference | Author-reported | p. 10, T3 |
| SEP SecAlign start/middle/end | 11.0 / 3.6 / 6.5 | % ASR | Llama3-8B-Instruct | Author-reported | p. 10, T3 |
| InjecAgent None/StruQ/SecAlign | 75.9 / 2.2 / 0 | % ASR | Malicious API calling | Author-reported | p. 10, T3 |
| Imperative-data comparison | 65.5 | % WinRate | 804 samples | Author-reported | p. 11 |
| Manual data-handling result | 16 / 52 | % | None / SecAlign, first 50 | Author-reported | p. 11 |
| DPO/ORPO/KTO GCG ASR | 15 / 34 / 9 | % | Llama-7B ablation | Author-reported | p. 11, T5 |
| Selected repeated training | 5 | runs | Learning rate 2 × 10^-4 | Author-reported | p. 11, F6 |
| Final SecAlign GCG loss | approximately 10 | loss | Orange mean at 500 steps | Approximate visual estimate | p. 9, F5 |
| T8 SecAlign anywhere maxima | 0.5 / 0.5 / 1 | % ASR | Three target groups | Visually readable | p. 15, T8 |

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Preference training adds explicit discouragement of injected answers. | Paired responses and reference-relative loss. | ALG1, E3 | pp. 5–6 | HIGH for method description; not a security proof. |
| Training pairs need no new manual preference labels. | Random instruction pairing and reused answers. | ALG1 | pp. 6–7 | HIGH; underlying dataset creation still requires resources. |
| Main fixed attacks are stopped in reported tests. | All SecAlign fixed-attack cells zero. | T6, X1 | p. 15 | HIGH for observed table, limited to tested cases. |
| Optimized attacks become substantially less successful. | Main maxima 1/8/14/1/9 versus StruQ 27/45/60/41/43. | T6 | p. 15 | HIGH; one SecAlign rate exceeds 10%. |
| Utility is broadly retained in primary comparisons. | Similar main WinRates. | F3–F4, T6 | pp. 8–9, 15 | HIGH for values; other benchmarks show declines. |
| Lowest ASR is insufficient to establish useful defense. | StruQ SEP utility 18.9 despite very low ASR. | T3, X6 | p. 10 | HIGH for table; interpretive lesson is D. |
| Defense transfers to API-returned text. | SecAlign InjecAgent ASR 0 versus 75.9 None. | T3, X7 | p. 10 | HIGH for reported result; no utility evaluation. |
| Security varies with position. | SEP 11.0/3.6/6.5. | T3 | p. 10 | HIGH; middle is best in these exact cells. |
| DPO provides a runtime/security compromise. | KTO lower ASR but much greater time; ORPO higher ASR. | T5, X11 | p. 11 | HIGH for one ablation, not universal optimizer ranking. |
| Web agents expose additional untrusted channels and actionable consequences. | External documents/API results and malicious-call benchmark. | §2.2, T3, §6 | pp. 3, 10, 12 | MEDIUM analyst inference; no matched standalone comparison. |
| Defense is incomplete for deployed agents. | Explicit multi-turn, delimiter, further-training limits. | §6 | pp. 12–13 | HIGH for author-stated boundaries. |

## 22. Very simple explanation — Explain Like I’m 15

Imagine asking an assistant to summarize a web page. Inside the page, somebody has written a message telling the assistant to forget your request and do something else. The assistant needs to understand that the page is something to read, while your request is the instruction to follow. The paper studies what happens when models confuse those two roles.

SecAlign teaches that distinction using paired answers. For one attacked input, the researchers show an answer that follows the real task and an answer that follows the hidden command. Training makes the model prefer the first over the second. They can build these pairs from existing task examples instead of asking people to label every new attack.

This substantially improves resistance in the paper’s tests. It often preserves normal helpfulness, but the improvement is not perfect: some optimized attacks still succeed, some utility scores fall, and success depends on the setting. A reported zero means no successes under that particular test and scoring rule, not that attacks have become impossible.

For web agents, the concern is especially relevant because pages, documents, and tool results can bring someone else’s words into the agent’s working context. If the agent can also call tools, a mistaken instruction can lead to an action rather than merely a wrong sentence. That connection is an interpretation supported by this paper, not a direct experiment proving exactly how much more vulnerable web agents are than standalone models.

## Completeness Audit

The inventory is the denominator of this audit. Supplied text from all 15 physical pages was assessed; images from 14 pages were visually inspected. The response represents the full available methodological and experimental structure, with deliberate compression of repeated examples and secondary publication material. It does not claim that every word or every citation detail has been preserved.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Identity, abstract, keywords | Yes, text and image | Yes | Represented in compressed form | Headline claims qualified against appendix. |
| §1 Introduction | Yes | Yes | Fully represented substantively | Problem, motivation, preference framing. |
| §2.1 Problem Statement | Yes | Yes | Fully represented | Roles, delimiters, attacker/defender goals. |
| §2.2 Problem Significance | Yes | Yes | Represented in compressed form | Slack scenario and external-data consequences. |
| §2.3 fixed attacks | Yes | Yes | Fully represented substantively | Page-4 portion text-only. |
| §2.4 optimized attacks | Yes | Yes | Fully represented substantively | Budgets absent where not reported. |
| §3.1 existing loss | Yes | Yes | Fully represented | E1 and output-space argument. |
| §3.2 preference formulation | Yes | Yes | Fully represented | E2–E3, mechanism and caveats. |
| §3.3 dataset implementation | Yes | Yes | Fully represented | ALG1 and five-step pipeline. |
| §3.4 AT comparison | Yes | Yes | Fully represented | E4–E5 and static-data approximation. |
| §4.1 setup | Yes | Yes | Fully represented at supplied detail | Missing implementation parameters identified. |
| §4.2 defense comparisons | Yes | Yes | Fully represented substantively | StruQ, hierarchy, BIPIA; Jatmo/ISE exclusions included. |
| §4.3 prompting defenses | Yes | Yes | Represented in compressed form | Five methods and all table outcomes retained. |
| §4.4 security generalization | Yes | Yes | Fully represented | SEP, API, many-shot, languages. |
| §4.5 utility generalization | Yes | Yes | Fully represented | Benchmarks and imperative-data checks. |
| §4.6 ablations | Yes | Yes | Fully represented | Optimizers, data fractions, rates, selected repeats. |
| §5 Related Work | Yes | Yes | Represented in compressed form | Categories and distinctions; not 94 individual summaries. |
| §6 conclusion/discussion | Yes | Yes | Fully represented substantively | Limitations, layered defense, practical and multimodal future work. |
| Explicit RQs | Yes, checked | Yes | No numbered RQs present | Analyst questions labeled O1–O5. |
| Hypotheses | Yes | Yes | Represented in compressed form | Many-shot and industry-data explanations labeled speculative. |
| X1–X7 | Yes | Yes | Fully represented substantively | Distinct setups and qualifications retained. |
| X8–X10 | Yes | Yes | Fully represented at reported detail | Missing shot/language details acknowledged. |
| X11–X14 | Yes | Yes | Fully represented substantively | Plot exactness and T8 caveats retained. |
| F1 and both components | Yes, visually | Yes | Fully represented | Training schematic plus bar comparison. |
| F2 | Yes, visually | Yes | Fully represented | Log probabilities, model, mechanism. |
| F3, both panels | Yes, visually | Yes | Fully represented | Exact values from T6. |
| F4, all three panels | Yes, visually | Yes | Fully represented | Includes 14% exception. |
| F5 | Yes, visually | Yes | Fully represented | Mean versus sample SD distinguished. |
| F6, both panels | Yes, visually | Yes | Fully represented | Exact plotted values unavailable. |
| T1–T5 | Yes, visually and text | Yes | Fully represented substantively | Key cells, units, comparisons, limitations. |
| T6 | Yes, visually and text | Yes | Fully represented numerically | Main rows and attack-specific breakdown reproduced. |
| T7 | Yes, visually and text | Yes | Fully represented numerically | Sandwich inconsistency flagged. |
| T8 | Yes, visually and text | Yes | Represented in compressed form | Maxima, SecAlign residuals, criteria, spelling/configuration caveats. |
| E1–E5 | Yes | Yes | Fully represented | Symbols and optimization roles explained. |
| Unnumbered reward rewrite | Yes | Yes | Fully represented | Included with E5 discussion. |
| ALG1 | Yes, visually and text | Yes | Fully represented substantively | Branches, skip rule, input/output included. |
| Example boxes | Yes; p. 4 text-only | Yes | Represented in compressed form | Repeated task wording omitted deliberately. |
| Major contributions | Yes | Yes | Fully represented | Novelty distinguished from existing DPO. |
| Author limitations | Yes | Yes | Fully represented | Enumerated separately from analyst observations. |
| Appendix | Yes | Yes | Fully represented substantively | Includes scoring-rule caveat and attack-strength differences. |
| Acknowledgments | Yes | Briefly | Inspected but compressed as secondary | Funding and discussion credits do not establish defense efficacy. |
| References [1]–[94] | Yes, supplied list | By relevant categories | Represented in compressed form | External works themselves not reviewed. |
| Publication/legal boilerplate | Yes | Identity only | Inspected but deliberately omitted as non-substantive | Permissions, contact addresses, repeated running headers. |
| Supplementary artifacts | None supplied | Absence stated | Missing from supplied material | No unsupported claim of supplement review. |

### Missing or inaccessible material

The rendered image of physical page 4 is absent, although its text is supplied. Code, checkpoints, data files, cited source documents, and the follow-up Meta SecAlign paper were not supplied. These absences prevent implementation verification, independent sample accounting, and assessment of claims attributed to the follow-up. No separate supplementary file was reviewed.

### Uncertain interpretations

Unresolved items include the Table 7 Sandwich maximum, Table 8 Hello Word/Hello World spelling and StruQ configuration, 14% versus 15% Llama-7B GCG results across tables, overly broad utility-similarity prose, and end-versus-middle position characterization. Figure 6’s exact point values and uncertainty magnitudes are not confidently recoverable from the supplied visuals. The model for Table 8 is not explicitly labeled in its table; it should not be assigned solely by similarity to another table. The supplied paper does not establish whether rounded percentages correspond to identical sample accounting across every ancillary experiment.

### Deliberately compressed material

Repeated prime-number/dinosaur examples, raw adversarial suffix strings, exact reminder sentences for each prompting defense, repeated statements of the security goal, and reference-by-reference bibliographic metadata were compressed. Table 8’s baseline interior cells were summarized through maxima and the substantive discrepancies rather than all copied. Acknowledgment names, author email addresses, copyright text, running headers, and proceedings pagination were not reproduced in full.

### Potential omissions

No known major section, substantive subsection, figure, table, numbered equation, algorithm, experimental family, or explicit limitation from the established inventory is left wholly unrepresented. Some numerical interiors and repetitive examples are deliberately compressed as disclosed. This is an inventory-based account of supplied material, not a claim of exhaustive semantic preservation, independent replication, or access to absent artifacts.
