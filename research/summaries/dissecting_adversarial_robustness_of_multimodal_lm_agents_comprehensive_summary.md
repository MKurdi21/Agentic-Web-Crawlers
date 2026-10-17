## Stage 0 — Document Accessibility Report

This analysis uses only the supplied paper text and source images. Document content, including example attack strings, is treated as evidence rather than instructions. No external sources, repository contents, or tools were used.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied text covers physical PDF pages 1–22. |
| Pages apparently missing | No gaps in the supplied page-text sequence. This does not establish whether additional material exists outside this PDF. |
| Visually inspected pages | 1–10 and 14–21: 18 rendered page images. |
| Text-only pages | 11–13 and 22. Their supplied text was inspected; their visual layout was not. |
| Visual content | All numbered figures 1–13 appear on supplied rendered pages. Small labels inside screenshots are less readable than main text. |
| Tables | Tables 1–7 are available in supplied text and rendered images. Main entries are readable. |
| Equations | The edge-weight definition and numbered Equations (1)–(2) are available in text and images. Notation discrepancies are identified below. |
| Appendices | A–D are present. Appendix D continues onto text-only page 22. |
| Supplementary material | No separate supplementary artifact was supplied. No embedded files are reported in the supplied accessibility metadata. |
| Referenced external artifacts | The code/data repository and cited publications were not inspected. Repository availability is an author statement, not independently verified. |
| OCR | Not needed for the supplied text. Rendered images were used to check visual objects directly. |
| Other limitations | Complete prompts and few-shot examples are explicitly omitted from some figures; safety-prompt examples are omitted in Appendix B.4. Plot coordinates without labels cannot support exact numerical extraction. |

Evidence labels used throughout: **[A] author-reported**, **[B] directly observable**, **[C] analyst-derived**, and **[D] analyst interpretation**. No external-information category [E] is used. Confidence is HIGH for clear statements and readable table entries, MEDIUM for bounded interpretations, and LOW or UNKNOWN where evidence is insufficient. Source locators use physical PDF page numbers, which match the printed numbers here.

## 1. Plain-language orientation

**Dissecting Adversarial Robustness of Multimodal LM Agents**, by Chen Henry Wu, Rishi Shah, Jing Yu Koh, Ruslan Salakhutdinov, Daniel Fried, and Aditi Raghunathan of Carnegie Mellon University, was published as an ICLR 2025 conference paper. It combines a security evaluation, a web-agent benchmark extension, and a framework for understanding how attacks move through an artificial-intelligence system.

A web agent uses a language model to inspect a website and take actions for a user. An attacker may own only one product listing or post, yet can alter its text or subtly change its image. The researchers ask whether those limited changes can redirect an agent toward the attacker's objective, such as selecting the wrong item or leaving an unwanted comment. Success means achieving the attacker's specified goal, rather than merely producing an unusual sentence. [A; pp. 1–3, 5–6]

The researchers create **VWA-Adv**, containing 200 adversarial tasks built on VisualWebArena. They also propose **Agent Robustness Evaluation**, abbreviated ARE, which represents an agent as connected components and tracks the adversarial influence of information between them. They attack policy models, image captioners, evaluators that judge completed attempts, and value functions that score candidate actions. [A; pp. 1–6]

The headline finding is attack success up to 67% under the tested conditions. This is a maximum across evaluated configurations, not a universal rate. For a GPT-4o policy, reported success is 40% with injected text, 31% with an attacked white-box captioner, 19% with a transfer attack on self-captioning, and 10% with a transfer attack directly through the screenshot. Evaluators and search can help when their additional components receive clean information, but can make the system less robust when those components also receive attacked information. [A; pp. 7–10]

**Relevance to the requested question — analyst inference:** the paper explains mechanisms by which web agents acquire distributed attack surfaces and turn malicious environmental information into actions. It does **not** provide a controlled experiment establishing that web agents have a higher attack rate than standalone language models. Its direct comparisons are primarily between agent configurations and attack conditions. The supported answer is therefore about mechanisms and demonstrated system-level vulnerabilities, not a measured universal agent-versus-chatbot ranking.

## 2. Document roadmap

The following inventory supplies the denominator for the coverage audit.

| Original section or object | Pages | Role |
|---|---:|---|
| Abstract and §1 Introduction | 1–2 | Motivation, headline results, contributions |
| §2 Related Work | 2–3 | Agents, adversarial robustness, indirect prompt injection |
| §3 Agent Robustness Evaluation | 3–5 | Threat model, graphs, adversarial influence |
| §3.1 Threat Model | 3 | Targeted environmental attack and limited access |
| §3.2 Agent Graph | 3–4 | Components and directed information flow |
| §3.3 Propagation of Attacks Along Edges | 4–5 | Edge weights, branching, robustifying components |
| §4 Adversarial Robustness of Agents in VisualWebArena | 5–7 | Benchmark construction and attacks |
| §4.1 Curation of Adversarial Tasks | 5–6 | Four task components and four curation steps |
| §4.2 Attacker Access | 6 | Text and bounded image modifications |
| §4.3 Attack Methods | 6–7 | Prompt injection, captioner attack, CLIP transfer attack |
| §5 Evaluating the Robustness of Agents on VWA-Adv | 7–10 | Main empirical evaluation |
| §5.1 Policy Models | 7–8 | Four attack settings and utility trade-off |
| §5.2 Reflexion Agents with Evaluators | 8–9 | Clean, jointly attacked, and evaluator-only conditions |
| §5.3 Tree Search Agents with Value Functions | 9 | Clean, jointly attacked, and value-only conditions |
| §5.4 Defenses | 10 | Prompts, paraphrasing, consistency, hierarchy discussion |
| §6 Conclusions | 10 | System-level implications and future directions |
| Acknowledgments and References | 11–14 | Funding, thanks, bibliography |
| Appendix A: Evaluation Details | 14–15 | A.1 goal templates; A.2 evaluation functions |
| Appendix B: Experimental Details | 16–20 | B.1 agents; B.2 compute; B.3 attack strings; B.4 prompts |
| Appendix C: Additional Results | 21 | C.1 attack ablations; C.2 screenshot transfer simulation |
| Appendix D: Limitations and Broader Impact | 21–22 | Scope limitations and deployment concerns |

Visual inventory: Figures F1–F13 and Tables T1–T7 retain their original numbering. Mathematical inventory: M0 is the unnumbered edge-weight definition on p. 4; E1 and E2 are Equations (1) and (2) on p. 6. Supporting mathematical concepts include the directed graph, the image perturbation constraint, and the inactive-edge convention. There are no numbered theorems, proofs, or standalone pseudocode algorithms. The task-curation list is a procedure rather than a formally numbered algorithm. No keywords block or formally numbered research-question or hypothesis list appears.

## 3. Background and context

A **language model (LM)** produces language-based outputs. The paper studies **multimodal** agents, which receive both visual and textual information. A **policy model** chooses actions. A **captioner** turns an image into a textual description. These descriptions may be inserted into the agent's text observation alongside webpage structure and a screenshot. [A; pp. 3–4, 16–18]

An **adversarial example** is an input altered to cause an undesired model response. An **indirect prompt injection** places instruction-like text in environmental content rather than in the legitimate user's request. Here, such text may be directly inserted into a listing or induced as the output of an image captioner. The latter route matters because image access can become an effective route to malicious text inside the agent's processing pipeline. [A; pp. 3, 6–7]

A **white-box** component has parameters known to the attacker, permitting optimization using its gradients. A **black-box** model does not expose the loss needed for that direct optimization. The paper attacks black-box visual models through **surrogates**: other models whose image representations can be optimized, hoping the resulting perturbation transfers. It uses CLIP image/text encoders as those surrogates. The supplied paper does not expand the CLIP acronym, so this analysis does not supply an external expansion. [A; pp. 6–7]

**Reflexion** is the paper's named architecture in which an evaluator reviews an attempt and provides feedback for another attempt. **Tree search** generates several candidate actions and uses a value function to select one. Neither mechanism is intrinsically a security defense: both are agent-computation strategies whose robustness the paper investigates. **Inference-time compute** means additional computation during task execution, rather than a reported change to model training. [A; pp. 4, 8–9]

The authors organize prior work into autonomous agents, adversarial robustness, and indirect prompt injection. They state that earlier attacks commonly assume extensive input access and a target output to optimize, whereas their attacker controls only a small environmental fragment and must influence subsequent reasoning and action. These are the authors' characterizations of prior literature; the cited studies were not independently checked. [A; pp. 2–3]

## 4. Research problem and gap

**Existing problem:** an agent may encounter content supplied by someone whose goals conflict with the user's. The attacker wants the agent to perform a specific alternative action. Small environmental changes can matter even when the underlying language model is accessed through a black-box service. [A; pp. 1–3]

**Shortcoming of previous evaluation, according to the authors:** evaluating an individual LM does not adequately capture a compound system whose components exchange intermediate outputs and ultimately act in an environment. A final harmful string and a completed adversarial web action are different evaluation targets. Attacks may also propagate through multiple components, and defensive checks may themselves process malicious inputs. [A; pp. 1–3]

**Research gap:** the authors seek both a realistic targeted benchmark under limited access and a way to attribute system vulnerability to component-to-component information flow. Their response is VWA-Adv plus ARE. The benchmark measures final adversarial-goal achievement; the framework explains intermediate attack propagation. [A; pp. 2–6]

**Scope:** the study covers three VisualWebArena environments and selected base, captioned, reflexion, and shallow tree-search agents. It is not a general assessment of all browsers, websites, operating systems, agent algorithms, or current model versions. It also does not estimate how frequently an uncontrolled production agent naturally encounters the selected triggers. [A for evaluated scope; D for the distinction from production exposure]

## 5. Research questions / objectives / hypotheses

The paper states objectives and asks subsection-level questions; it does not present preregistered hypotheses or a formal RQ numbering system.

| Analysis identifier | Objective or question | Source |
|---|---|---|
| O1 | Measure whether limited environmental attacks can achieve targeted goals in realistic web tasks. | pp. 1–2, §4 |
| O2 | Explain how adversarial influence propagates through compound agent components. | §§3.2–3.3 |
| O3 | Test vulnerability of policy models under text, white-box image, and black-box image access. | §5.1 |
| O4 | Can evaluators improve robustness, and what changes when evaluators are attacked? | §§5.2, pp. 8–9 |
| O5 | Can value functions improve robustness, and what changes when they are attacked? | §5.3 |
| O6 | Assess natural defense strategies and their limitations. | §5.4 |
| O7 | Identify conditions influencing CLIP attack transfer. | Appendix C |

Appendix C.1 explicitly describes hypotheses about why negative text and model ensembles help: negative text may move the image away from its original meaning, and an ensemble may find adversarial directions shared across models. The ablations test whether these ingredients improve observed targeted-caption success; they do not directly prove the proposed internal mechanisms. The explanation that high-resolution optimization overfits to surrogate models is also an author explanation, rather than a directly isolated causal result. [A; p. 21]

## 6. Assumptions / threat model

The legitimate user sets the goal. The attacker is a different platform user, such as a seller or post owner, who can modify only their own content. They cannot directly change the legitimate goal, the agent's prompts, model parameters, other users' listings, or the platform's interface design. The environment is divided into trusted and untrusted parts; only the latter is editable by the attacker. [A; §3.1, p. 3; §4.2, p. 6]

**Text access:** the attacker can add one piece of trigger text to their listing. The injected text is subsequently processed with the original text and screenshot. The study selects text to maximize effectiveness against GPT-4V. It does not evaluate a white-box text attack because the authors report lacking white-box models taking text input for this experiment. [A; p. 6]

**Image access:** the attacker modifies a single trigger image with an infinity-norm bound ε = 16/256. This bounds the maximum absolute pixel perturbation under the paper's image representation; it is not a statement that 16/256 of all webpage pixels are edited. The trigger image occupies less than 5% of the webpage pixels in the described setting, leaving approximately 95% unaltered. The authors describe this bound as an imperceptibility standard and argue that image attacks offer plausible deniability. No separate human perceptual study is supplied. [A; pp. 2, 6; D for the perceptual-evidence observation]

**Component conditions:** in evaluator and value-function experiments, a component is considered attacked or unattacked according to whether it receives attacked environmental information. The researchers simulate this using adversarial versus clean captions. An unattacked component is not assumed mathematically infallible: it can still accept an adversarial action or fail to correct one. [A; pp. 8–9]

**ARE assumptions:** the exposition assumes a deterministic environment when assigning binary adversarial influence to intermediate outputs, while noting extension to stochastic values in [0,1]. Edge-weight reuse requires an unchanged upstream design. The framework's worst-case downstream interpretation must not be confused with the observed behavior of every particular downstream model. [A; p. 4]

## 7. Methodology

### Study design and task construction

VWA-Adv contains **200 tasks** drawn from VisualWebArena, which includes classifieds, Reddit-style social media, and shopping platforms. Each task contains an original user task, a trigger image or text, a distinct adversarial goal with an evaluation script, and an initial agent state. [A; pp. 5–6]

The construction procedure is: first sample a VWA task and run the best agent from the cited VWA work; discard it and sample another if that agent fails. Next randomly choose a trigger along the successful trajectory. Then craft a targeted adversarial goal using Appendix A templates and manually annotate its evaluation function using existing primitives. Finally initialize the evaluated agent at the trigger state instead of the homepage, ensuring exposure. [A; §4.1]

This procedure deliberately selects tasks that a reference agent can solve and removes uncertainty about seeing the attack. **Analyst interpretation:** results consequently concern attack effectiveness under ensured exposure on this curated task set. They should not be read as unconditional homepage-to-completion incident rates or performance on a random sample of all web tasks.

Goals fall into **illusioning**, where the agent is induced to use incorrect attributes, and **goal misdirection**, where it performs an attacker-desired action. Evaluation is execution-based: after termination, scripts inspect the environment and/or response. Primitives include exact match, fuzzy match, must-include checks, and URL matching. Some target form text is fuzzy-matched by GPT-4. The supplied material does not report annotation agreement or an independent audit of these judgments. [A; pp. 5, 15; D for the reporting observation]

### Architectures and models

The base agent has a policy model. Captioner augmentation adds image-to-text preprocessing. Self-captioning uses the black-box LM itself to caption images. Reflexion adds a trajectory evaluator and a possible second attempt; the maximum is **two attempts**. The evaluator study uses GPT-4o plus a captioner to keep API usage within budget. Tree search uses a **branching factor of three and depth one**, with deduplicated candidate actions scored by a value function. [A; pp. 4, 7–9]

Appendix B.1 identifies GPT-4V as `gpt-4-vision-preview`, Gemini-1.5-Pro as `gemini-1.5-pro-preview-0409`, Claude-3-Opus as `claude-3-opus-20240229`, and GPT-4o as `gpt-4o-2024-05-13`. Decoding temperature is **0** to reduce randomness. This is a reported randomness-reduction choice, not proof that every service execution is deterministic. Figure 9 labels its external captioner LLaVA, but the supplied text does not specify its full checkpoint, parameter count, or complete captioner configuration. [A/B; pp. 16–18]

### Attack construction

The text attack injects attacker-selected text directly. The white-box captioner attack optimizes an image perturbation to increase the likelihood of a chosen adversarial caption using projected gradient descent. The black-box image attack optimizes image/text similarity on four CLIP encoders: ViT-B/32, ViT-B/16, ViT-L/14, and ViT-L/14@336px. It rewards similarity to the target text and penalizes similarity to negative text. Perturbations are optimized at **180-pixel resolution**, a choice investigated in Appendix C. [A; pp. 6–7, 21]

### Metrics, computation, and reporting

**Benign success rate**, or Benign SR, measures achievement of the user goal without attack. **Attack success rate**, or ASR, measures achievement of the adversarial goal under attack. ARE also reports intermediate edge weights, which need not equal final ASR. Caption-equivalence success in Appendix C is a separate metric. [A; pp. 4, 6–9, 21]

Gradient-based attacks and captioning ran on an **A6000 or A100 80G**; frontier models were accessed through APIs. The supplied paper does not specify a complete software environment, optimizer step counts, learning rates, attack restarts, random seeds, full prompts, experiment-specific denominators, confidence intervals, or statistical significance tests. No train/validation/test partition or model training procedure is described for this evaluation benchmark. These are reporting boundaries, not values to reconstruct by assumption. [A for hardware; D for absent reporting; pp. 6–7, 16–17]

## 8. Experiments / analyses

| ID | Purpose and conditions | Outcome and qualification |
|---|---|---|
| X1: Text injection | GPT-4o policy receives screenshot plus text containing the injected trigger. | 40% final ASR; demonstrates that visual input does not reliably prevent textual redirection. Fig. 4A, p. 7. |
| X2: White-box captioner | Image-only adversarial access; optimize a known captioner to emit attacker text. | 92% adversarial-caption edge weight and 31% final ASR for the GPT-4o policy configuration. Fig. 4B. |
| X3: Self-caption transfer | CLIP perturbations transfer to a black-box LM captioner and then policy. | 38% adversarial-caption edge weight, 19% final ASR. Fig. 4C. |
| X4: Direct screenshot transfer | Base agent uses the screenshot without captions. | 10% final ASR; requires transfer both across models and from a trigger image into a larger screenshot. Fig. 4D, pp. 7–8. |
| X5: Model/utility comparison | Four LM families across settings A–D. | Authors report positive association between benign SR and ASR and the best trade-off for GPT-4o. Exact point values are not tabulated. Fig. 4 right. |
| X6: Reflexion | Compare base policy attack, clean evaluator, jointly attacked policy/evaluator, evaluator-only attack; maximum two attempts. | Final ASRs 31%, 25%, 36%, and 8%, respectively. Fig. 5, pp. 8–9. |
| X7: Tree search | Compare analogous policy/value-function conditions; branching three, depth one. | Final ASRs 31%, 26%, 38%, and 8%, respectively. Fig. 6, p. 9. |
| X8: Defenses | GPT-4o plus white-box captioner under captioner attack; prompts, paraphrasing, separate-image consistency. | Prompts fail to improve robustness; paraphrasing 27.5% versus 31%; consistency near-zero against that attack but adds calls and remains attackable. Fig. 7, p. 10. |
| X9: Resolution ablation | Vary optimization and inference resolutions for CLIP attack; measure GPT-4V target-equivalent caption generation. | Lower optimization resolution helps; inference resizing has little reported effect. Fig. 13, p. 21. |
| X10: Attack ingredients | Remove negative text or replace ensemble with individual encoders. | Full method 71%, no negative text 46%, individual encoders 9–31% targeted-caption success. Table 7. |
| X11: Screenshot simulation | Four images on blank background; first adversarial, three clean. Vary image/screenshot sizes and surrounding text. | Table 3 ASR ranges 13–55%; larger relative images and absence of supporting original text increase attack success. pp. 8, 20–21. |

The supplied paper does not give separate sample counts or repeated-run uncertainty for these rows. The existence of 200 benchmark tasks does not justify assuming every plotted or synthetic condition uses exactly 200 observations. Appendix C's caption-generation outcome also must not be merged with execution-based web-task ASR.

## 9. Results

The strongest supported pattern is **conditional component benefit**. A clean evaluator reduces final ASR from 31% to 25%, and a clean value function reduces it from 31% to 26%. When the added component receives attacked information, the corresponding final results become 36% and 38%. These conditions show that adding computation changes both filtering capacity and exposure to attack. [A; Figs. 5–6]

**Analyst-derived arithmetic:** 31% → 25% is a reduction of 6 percentage points, or 6/31 × 100 ≈ 19.35% relative to the displayed base. The introduction instead reports a 23% relative reduction for an unattacked evaluator. The available rounded values do not reproduce that claim. Both are retained rather than silently reconciled. [C; pp. 2, 8]

For joint evaluator attack, 31% → 36% is an increase of 5 percentage points, or 5/31 × 100 ≈ 16.13%. The abstract says 15% relative, while the introduction says 20% relative. For joint value-function attack, 31% → 38% is 7 percentage points, or 7/31 × 100 ≈ 22.58%, compared with the abstract's 20% relative. Unreported precision could affect rounded comparisons, but the supplied material does not establish the reconciliation. [A/C; pp. 1–2, 8–9]

Evaluator-only and value-function-only attacks each achieve **8% final ASR**, despite clean direct policy inputs. This does not mean the policy is incapable of producing an adversarial candidate. In the search case, the authors explicitly explain that a low-probability adversarial action can be explored and then preferred by an attacked scoring component. [A; p. 9]

The white-box captioner transforms image perturbation into an adversarial textual intermediate output on 92% of executions, while final GPT-4o ASR is 31%. This gap shows why caption corruption and completed attacker goals are distinct outcomes. Similarly, self-captioning has 38% adversarial-caption influence but 19% final ASR. [A; p. 7]

The 67% headline is linked in §5.4 to GPT-4V versus GPT-4o's 31% in the discussed captioner setting. It must not be assigned to every model, to direct screenshot-only attacks, or to the 71% Appendix C captioning result. The tested model snapshots are explicitly dated versions. [A; pp. 10, 16]

## 10. Figure-by-figure interpretation

### Figure 1 — Environmental attack and targeted evaluation

The diagram on p. 2 shows a legitimate goal of adding white headphones to a cart, an attacker-controlled image/text trigger, alternating environment/agent interactions, and a final targeted evaluation checking whether a positive comment was left. Red arrows and labels identify attack injection and the adversarial objective. There are no numerical axes. Its substantive point is the separation between the user's objective and an observable attacker goal after a sequence of actions. It is an illustrative workflow, not a measured success-rate plot. [B]

### Figure 2 — Four agent graphs

On p. 4, panel A links environment → policy → finish. Panel B adds a captioner, while retaining environmental information flowing toward the policy. Panel C adds evaluator feedback and a second policy stage. Panel D adds a value function to search-based action selection. Arrows represent intermediate-output flow rather than elapsed time or measured probabilities. Repeated policy stages in C visualize retry structure; the detailed search-generation procedure is explained in prose. [A/B]

### Figure 3 — Adding a component can help or harm

The three schematic panels on p. 5 show an initial A → D path with influence 0.5; insertion of B can reduce outgoing influence to 0.2; giving B an attacked input of weight 1.0 can increase outgoing influence to 0.7. These are explanatory numbers, not empirical benchmark estimates. Red attacked-input arrows and intermediate edges illustrate how a new filter can also become an entry point. There are no axes or error bars. [B]

### Figure 4 — Policy attacks and robustness–utility scatter

The left panels on p. 7 give GPT-4o graph decompositions. A: attacked text, final 0.40. B: attacked captioner, caption edge 0.92 and final 0.31. C: CLIP attack through self-captioning, caption edge 0.38 and final 0.19. D: CLIP attack through the screenshot, final 0.10. Blue environment edges denote clean inputs, red attacked inputs, and purple downstream flow. Edge values are dimensionless influence weights. [A/B]

The right scatter has Benign SR on the horizontal axis and ASR vertically, both linear and dimensionless rates. Colors identify GPT-4o, GPT-4V, Claude-3-Opus, and Gemini-1.5-Pro; marker shapes identify settings A–D. No error bars appear. Exact point coordinates are not labeled sufficiently for a complete numerical transcription. The authors describe a positive robustness–utility association and GPT-4o's favorable trade-off. The asterisk warns that benign tasks were selected using GPT-4V, so benign success is not directly comparable to the original unfiltered VWA benchmark. [A/B; pp. 7–8]

### Figure 5 — Evaluator pathways

On p. 8, A gives the policy-only baseline 0.31. B attacks only the evaluator: reflection influence is 0.09 and final ASR 0.08. C uses a clean evaluator with attacked policy input: first-attempt adversarial acceptance contributes 0.18, second-attempt success 0.07, total 0.25. D attacks both: corresponding final-path contributions are 0.21 and 0.15, totaling 0.36; adversarial-reflection influence is 0.06. Environment-to-retry weights 0.27 and 0.30 reflect branching exposure and must not be read as separate overall ASRs. Captioners are omitted by the authors. The additive final paths are distinct termination branches, not permission to sum arbitrary graph edges. [A/B]

### Figure 6 — Value-function pathways

On p. 9, A gives 0.31 baseline final ASR. B attacks only the value function and yields 0.08. C supplies clean information to the value function and reduces final ASR to 0.26. D attacks policy and value function and yields 0.38. There are no axes: the displayed decimals are edge weights and final rates. The figure supports conditional benefit of scoring, not a claim that all larger searches are empirically less safe; only branching three and depth one are tested here. [A/B]

### Figure 7 — Defenses

The horizontal bar chart on p. 10 places ASR on a linear x-axis from 0.0 to 0.5 and defense names on the y-axis. A vertical reference marks the no-defense baseline, reported as 31% in text. Safety and abstention prompts do not improve the baseline; paraphrasing is reported as 27.5%; consistency is visually near zero. Exact prompt-bar percentages are not labeled and are not reconstructed here. The prose refers to consistency as the third bar even though four labeled defenses are displayed; the names and visual order identify the intended condition. No uncertainty bars are provided. [A/B]

### Figure 8 — Webpage screenshot

The p. 16 image shows a long classifieds motorcycle-results page with navigation, filters, listings, prices, thumbnails, and colored numbered marks. It illustrates why a single listing image occupies a small portion of an agent's observation. It is not an annotated before/after perturbation comparison and does not independently measure perceptual invisibility or establish an exact pixel-area percentage. Tiny listing text is secondary to its role as a full-page observation example. [B]

### Figure 9 — LM plus external captioner

On p. 17, webpage images feed a LLaVA captioner; its descriptions are inserted into a Set-of-Marks-associated text observation, which joins visual information and the user goal at GPT-4V. The example seeks recent blue motorcycles within $1000–$2000 and shows an action selecting a listing. This is an architecture illustration, not a new measured attack result. System prompts and few-shot examples are omitted. [A/B]

### Figure 10 — Base LM agent

Also on p. 17, the comparable pipeline removes image descriptions supplied by an external captioner. The policy still receives the screenshot and parsed webpage text with element identifiers, then outputs an action. The repeated motorcycle example holds the explanatory task stable while illustrating the input difference. No latency, accuracy, or attack statistic is encoded. [A/B]

### Figure 11 — Self-captioning agent

On p. 18, the LM produces image descriptions that enter the parsed observation before the action-producing LM stage. The rendered figure visibly includes a LLaVA label in its upper captioner position, while the caption, surrounding discussion, and GPT-4V labeling identify a self-captioning example. This is a visual-label ambiguity, not evidence of an additional evaluated architecture. The architectural distinction supported by §5.1 is that the black-box LM itself supplies captions. [A/B; confidence MEDIUM for reconciling the diagram]

### Figure 12 — Synthetic screenshot contexts

On p. 20, four panels use image/screenshot resolution labels 128/2048, 256/2048, 128/512, and 256/512. Each layout contains several small item images on blank space. A lower text block illustrates surrounding parsed webpage information supplied in the text-present condition. The labels specify image and screenshot resolutions; they are not explicitly area fractions. This figure visualizes the controlled contexts behind Table 3 rather than presenting a real-web task result. [A/B]

### Figure 13 — Resolution heatmap

On p. 21, a five-by-five heatmap compares inference resolution horizontally with optimization resolution vertically, using 180, 384, 512, 768, and 1024 pixels. Color encodes target-equivalent caption success, with darker upper cells indicating higher values and a color scale labeled through 0.6. Individual cell values are not printed and are not extracted as exact measurements. The strongest visual pattern is better performance for the lowest optimization resolution and comparatively limited variation across inference resolutions. There are no uncertainty intervals. [A/B]

## 11. Table-by-table interpretation

### Table 1 — Meaning of adversarial influence

On p. 5, rows define when AdvIn(c) equals one: observations originate from the untrusted environment; actions lead to the adversarial goal; captions or reflections would lead a perfectly following policy to that goal. The inactive value ∅ has influence zero. This is a definitional table, not measured model accuracy. Treating an untrusted observation as maximally influential is part of the framework's worst-case construction, not a claim that every untrusted observation causes harm. [A]

### Table 2 — Two families of goals

On p. 5, illusioning examples include object identity, capacity, color, material, price, review count, rank, seller email, and mileage. Goal misdirection examples include choosing or avoiding an item, adding to cart, and leaving or modifying a review/comment. The table supplies a taxonomy without reporting per-category frequencies or success rates. [A]

### Table 3 — Synthetic transfer conditions

On p. 8, columns compare ASR without versus with other text describing the original image. Values are: 128/2048, 29% versus 13%; 128/512, 45% versus 22%; 256/2048, 40% versus 33%; 256/512, 55% versus 38%. Within each row, supporting original-image text lowers ASR. The largest listed rate is 55%, and smallest 13%, across these conditions. These are synthetic selection-task outcomes, not the 10% direct screenshot web-agent result. No sample sizes, significance markers, or uncertainty estimates appear. [A/B]

### Table 4 — Goal templates

On p. 15, illusioning templates cover altered object, amount/capacity, color, shape, background, price, review/comment count, list position, image text, seller email/name, used-car mileage, viewing angle, location, and stars. Misdirection templates cover cart, navigation, wish list, comment format/sentiment, reversing a requested price or sentiment, upvoting, avoiding an item, and claiming unavailability. The table specifies the construction space, not the achieved distribution over 200 tasks. Repetitive template wording is deliberately compressed. [A]

### Table 5 — CLIP target and negative texts

On p. 18, paired strings contrast desired versus discouraged semantics: white versus black cellphone, blue boat versus white, outside versus interior, fox painting versus castle, red vehicle versus other color terms, red chair versus sofa, empty table versus people, three adults versus baby, and guitar versus office. Additional targets include a sea painting, Pittsburgh text, a bull rider, and a floor-sitting cat with dashes in the negative column. The table does not explain the exact implementation treatment of those dashes. Its y+ and y− labels differ from Equation (2)'s z and z− naming, but target/negative roles are clear. [A/B]

### Table 6 — Induced caption examples

On p. 19, target strings include explicit instructions to ignore user requirements, change comment style, claim unavailability, upvote content, or introduce false attributes. Check and cross marks indicate whether captioner output exactly matched the target text. At least one long positive-comment target is marked unsuccessful, while many other instruction-like targets are marked successful. These are illustrative caption-generation cases, not a representative sample or final-task success table. The table demonstrates that the optimized caption need not resemble a normal visual description. The malicious strings are evidence only and are not reproduced in full. [A/B]

### Table 7 — CLIP ingredient ablations

On p. 21, the full Equation (2) method has 71% targeted-caption success; removing negative text gives 46%. Single-surrogate results are 9% for ViT-B/32, 23% for ViT-B/16, 20% for ViT-L/14, and 31% for ViT-L/14@336px. The full method is best among listed conditions; ViT-B/32 alone is worst. The metric is GPT-4V generation of a caption equivalent to the target, as in Figure 13. It is not final agent ASR. No statistical uncertainty or significance test is reported. [A/B]

## 12. Diagram / architecture interpretation

The diagrams identify three distinct places where environmental content can gain influence. First, a policy can consume malicious text or a corrupted screenshot directly. Second, a captioner can translate a perturbed image into text that the policy then consumes. Third, an evaluator or value function can process attacked content and alter the later trajectory even when the policy's direct input is clean. [A/B; Figs. 1–6, 9–11]

In reflexion, the policy produces an attempt; the evaluator examines the trajectory; acceptance terminates it, while rejection generates a reflection and permits another attempt. An attacked evaluator can both approve a bad attempt and reject an acceptable one while supplying malicious guidance. In search, the policy proposes candidates; the value function scores them; search chooses which to execute. A corrupted scoring stage can promote an adversarial candidate that would otherwise be unlikely. [A; pp. 8–9]

**Analyst interpretation:** these pathways answer the research question more precisely than saying the LM simply becomes weaker. Agent construction introduces additional recipients of untrusted information and additional opportunities for intermediate representations to affect actions. At the same time, the same graph can contain useful filters. The results therefore support a conditional account of architecture and trust boundaries, rather than the rule that more components always mean more vulnerability.

## 13. Equations and mathematical concepts

### Directed graph

The agent is G = (V, E), where V contains the environment observation node v_env, the unique finish leaf v_finish, and component nodes. E contains directed edges: a child's input includes its parent's output. The graph represents information flow, including distinct retry stages. It is not itself a probabilistic causal model with experimentally established independent edges. [A; p. 3; D for the modeling qualification]

### M0: Edge weight

The unnumbered definition on p. 4 is **λ(e) = E[c ∼ p_e][AdvIn(c)]**. Here e is an edge, c its intermediate value, p_e the distribution of values after upstream components execute, AdvIn(c) its adversarial influence, and E an expectation. The output λ(e) is a dimensionless value in [0,1].

AdvIn(c) is the tightest upper bound on expected attack success attributable to c when no further downstream component is attacked. It uses a worst-case downstream interpretation. A caption directing an adversarial goal can therefore have high influence even if the actual policy often ignores it. The distribution p_e depends on upstream ancestors; reuse across downstream variants is justified only if the upstream design remains fixed. [A; p. 4]

The authors' illustration uses adversarial captions on 80% of executions and a policy following them half the time. The caption edge has λ = 0.8, while the outgoing action edge has λ = 0.4. This is an explanatory example, not an additional benchmark result. For an inactive retry edge, c = ∅ contributes zero. The branching paragraph writes ASR(∅) = 0, while Table 1 states AdvIn(∅) = 0; both express zero contribution, although the notation changes. [A; pp. 4–5]

### E1: White-box captioner objective

Equation (1), p. 6: **maximize over ||δ||∞ ≤ ε: log π_comp(z | x + δ)**.

The input x is the trigger image; δ is its perturbation; ε is the permitted maximum perturbation; z is attacker-selected target text; π_comp is the attacked component's conditional text-generation model. The log expression measures the model likelihood of the target text given the modified image. Projected gradient descent is the reported optimization method. The output is an image perturbation that encourages the captioner to emit z. The bound applies to δ, and does not permit arbitrary replacement of the image. The supplied material does not specify optimization iteration counts or step sizes. [A]

### E2: CLIP surrogate objective

Equation (2), p. 6: **maximize over ||δ||∞ ≤ ε the sum over i = 1…N of [cos(E_x^(i)(x + δ), E_y^(i)(z)) − cos(E_x^(i)(x + δ), E_y^(i)(z−))]**.

E_x^(i) and E_y^(i) are image and text encoders for surrogate i; cos is cosine similarity; N is the number of surrogate models, instantiated with the four listed CLIP encoders; z is desired text and z− discouraged text. The objective pulls the perturbed image representation toward the desired meaning and away from the negative meaning across the ensemble. It optimizes surrogate representations, not the hidden loss of the target black-box LM. Success requires transfer, which the experiments measure rather than guarantee. [A; pp. 6–7]

Table 5 and Appendix C use y+ and y− for the corresponding target/negative texts. The notation shift is disclosed rather than silently treated as a new objective. Neither equation proves robustness or attack success; both specify attack construction. No theorem or formal robustness certificate is supplied.

## 14. Interpretation and discussion

O1 is answered by successful targeted web actions under restricted environmental access, including the reported maximum of 67%. O2 is addressed by the ARE graphs and the separation between corrupted captions and final actions. O3 is addressed by the four Figure 4 settings. O4 and O5 receive explicitly conditional answers: clean evaluators/value functions help, attacked ones can harm. O6 reveals limited protection from simple prompts and paraphrasing, plus a costly consistency strategy whose own inputs remain attackable. O7 identifies transfer dependencies on optimization resolution, surrogate ensemble, negative text, image size, and descriptive context. [A]

The paper's most useful contribution to the requested security question is the demonstration that a system can be redirected through components intended to improve performance or check work. A model may act on a malicious caption, a malicious reflection, or a manipulated score. **Analyst interpretation:** these intermediates can carry attacker influence across processing stages, making component-level evaluation insufficient to predict system-level safety.

However, the paper also says attacks can become more challenging when they must propagate through several components. The 10% direct screenshot result and the reductions with clean evaluators/value functions support preserving that nuance. Complexity provides both opportunities for filtering and opportunities for new exposure. No supplied experiment isolates a universal causal effect of being an agent rather than a standalone LM. [A/D; pp. 1, 7–9]

Unresolved consistency issues include the relative-change arithmetic reported in the abstract/introduction versus displayed ASRs; Figure 7's bar-index wording; the Figure 11 captioner-label ambiguity; target/negative symbol changes; and the inactive-edge notation change. Appendix D's opening wording groups attacks with image perturbations, although §4.3 explicitly defines prompt injection as the text-access method. The operational distinction in §4.3 should be preserved. These issues do not erase the displayed conditional comparisons, but they limit exact restatement of some summary claims.

## 15. Contributions and novelty

**Dataset/benchmark:** 200 manually curated targeted adversarial tasks, associated evaluation functions, and trigger-state initialization on VisualWebArena. This makes the attack objective measurable as an environmental or response outcome. [A; pp. 5–6]

**Conceptual/methodological:** ARE represents the compound agent as a graph and uses adversarial influence to distinguish upstream corruption, filtering, branching, and final action outcomes. It permits reuse of edge computations under unchanged upstream conditions. [A; pp. 3–5]

**Attack engineering:** adaptation of prompt injection, gradient-based captioner attacks, and multi-surrogate CLIP transfer attacks to constrained web-agent settings. Appendix D explicitly characterizes attack baselines as engineered versions of existing attacks, so the paper should not be described as inventing every attack family. [A; pp. 6–7, 21–22]

**Empirical:** demonstrations of isolated captioner, policy, evaluator, and value-function vulnerabilities; conditional benefits and harms from reflexion/search; defense evaluations; and transfer ablations. The authors claim a first demonstration of extreme agent brittleness in their realistic threat model. That priority claim is reported as their position, not externally validated here. [A; p. 2]

**Implementation:** the authors report releasing tasks, attacks, defenses, evaluations, and injection-interface code at the named repository. Repository completeness and reproducibility were not verified. No new trained foundation model, theorem, or certified defense is presented.

## 16. Limitations

### Authors' stated limitations

Appendix D, pp. 21–22, gives three explicit limitations. First, the engineered attack baselines only establish a **lower bound on risk**: stronger attacks might achieve more. Second, evaluation uses a fixed set of web environments, and performance in more diverse settings such as operating systems remains unknown. Third, the evaluated base, reflexion, and tree-search algorithms do not cover emerging agent designs, whose robustness must be tracked.

Elsewhere, the authors acknowledge practical cost for separate-image consistency checks, continued attackability of the self-captioning component, and the need for stronger defenses. They also constrain evaluator experiments to two attempts and GPT-4o plus captioning for budget and demonstration purposes. [A; pp. 8, 10]

### Additional evidence-based analyst observations

The benchmark selects tasks solvable by a reference agent and guarantees trigger exposure. This supports controlled attack measurement but narrows interpretation of prevalence and natural encounter rates. The supplied material does not report confidence intervals, repeated-run variance, category frequencies, experiment-specific sample sizes, or detailed attack-optimization budgets. Consequently, fine-grained ranking and uncertainty cannot be assessed fully. [D]

The study's clean-versus-adversarial caption intervention is useful for isolating recipients of malicious information, but does not itself establish every attacker's ability to control those recipients independently in a deployed architecture. Shallow search and two-attempt reflexion do not quantify how vulnerability scales with much greater search depth or retries. The imperceptibility description lacks a supplied human-perception experiment. These are analyst observations, not additional admissions by the authors.

## 17. Threats to validity

The following labels organize analyst observations rather than reproduce an author taxonomy.

**Internal validity:** clean/adversarial caption routing isolates component exposure, but Figure 4 model comparisons also involve different architectures and attack pathways. The paper does not isolate instruction-hierarchy training as a controlled variable. GPT-4o's advantage therefore cannot be causally assigned to that training from these results alone. [D; pp. 7–10]

**Construct validity:** final ASR measures achievement of curated adversarial goals, while intermediate influence and targeted-caption success measure different constructs. Confusing 92% caption influence, 71% target-equivalent caption generation, and 67% maximum final ASR would materially misrepresent the evidence. Exact and fuzzy evaluation primitives may capture different aspects of goal achievement; their error rates are not reported. [D]

**External and ecological validity:** the tasks use realistic web environments but a selected task set and trigger-state starts. Generalization to arbitrary websites, natural exposure frequency, operating systems, future agents, and newer model snapshots remains untested. The synthetic blank-background experiment isolates factors but is not a full production webpage. [A/D]

**Statistical conclusion validity:** no reported confidence intervals or significance tests support claims that small differences are statistically reliable. Temperature zero reduces a source of randomness but does not replace uncertainty measurement. The relative-change inconsistencies further favor citing raw displayed ASRs. [D]

**Reproducibility:** model identifiers, hardware families, attack objectives, and a repository location are supplied. Full optimization settings, software versions, complete prompts, and evaluation counts are not all in the paper. No repository or API reproduction was performed here. [A/D]

## 18. Future work and open questions

### A. Authors' proposed future work

The conclusion calls for stronger defenses, using the graph to prioritize vulnerable edges, and creating adversarial versions of newly solvable tasks as agents improve. It also calls for stronger adaptive attacks as defenses develop. Appendix D recommends broader environments and continued tracking of emerging agent algorithms. [A; pp. 10, 22]

### B. Additional open questions — analyst inference

A controlled agent-versus-standalone-LM comparison remains needed to answer the requested comparative question quantitatively. Such a comparison would need matched underlying models, attack objectives, access restrictions, and outcome definitions; this paper does not provide it.

Other unresolved questions are how ASR changes with retry count, search width/depth, realistic trigger encounter frequency, independently secured evaluators, or tighter handling of untrusted intermediate text. The study also leaves open whether the near-zero fixed captioner-attack result for consistency checking can coexist with low cost and resilience to an adaptive attacker. These are questions motivated by the supplied evidence, not proposed solutions established by the authors.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| LM | Language model; the text-generating/reasoning component used by agents. |
| Multimodal | Processing more than one input modality, here principally images and text. |
| VWA | VisualWebArena, the underlying web-agent environment. |
| VWA-Adv | The authors' 200-task adversarial extension. |
| ARE | Agent Robustness Evaluation, the graph-based analysis framework. |
| Policy | Component proposing or choosing actions. |
| Captioner | Component translating an image into text. |
| Self-captioning | Using the black-box LM itself to generate image descriptions. |
| Evaluator | Component judging a trajectory and potentially writing a reflection. |
| Reflection | Textual feedback used in a subsequent policy attempt. |
| Value function | Component scoring candidate actions for search selection. |
| Reflexion | Named retry architecture using evaluation and verbal feedback. |
| Benign SR | Fraction achieving the legitimate user goal without attack. |
| ASR | Fraction achieving the adversarial goal under attack. |
| Trigger | The attacker-editable image or text encountered by the agent. |
| Illusioning | Inducing incorrect beliefs about task-relevant attributes. |
| Goal misdirection | Inducing an attacker-desired alternative action. |
| White-box | Attacker knows the targeted component's parameters. |
| Black-box | Target model does not expose the directly optimized internal loss. |
| CLIP attack | Transfer attack optimized using multiple CLIP image/text encoders. |
| Surrogate | Accessible model used to construct an attack for another model. |
| PGD | Projected gradient descent, the reported constrained optimization method. |
| SOM | Set-of-Marks, the parser/visual element-marking representation in examples. |
| API | Application programming interface; the access route used for frontier models. |
| G, V, E | Agent graph, nodes, and directed edges. |
| v_env, v_finish | Environment-observation node and unique finish leaf. |
| c, p_e | Intermediate edge value and its distribution after upstream execution. |
| AdvIn(c) | Worst-case adversarial influence of intermediate value c. |
| λ(e) | Expected adversarial influence carried by edge e. |
| ∅ | Non-executed edge value, assigned zero contribution. |
| x, δ, ε | Original image, perturbation, and perturbation bound. |
| ||δ||∞ | Maximum absolute component of the perturbation. |
| π_comp | Conditional text-generation model of the attacked component. |
| z, z− | Desired and discouraged text in the attack objectives. |
| y+, y− | Appendix/table notation for target and negative texts. |
| E_x^(i), E_y^(i) | Image and text encoders of surrogate i. |
| cos | Cosine similarity between encoded representations. |

## 20. Key numerical results

Values are exact as printed unless explicitly described otherwise. Percentages below are rates, not percentage-point changes.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| VWA-Adv size | 200 | tasks | Curated adversarial benchmark | Author-reported | pp. 1, 5 |
| Web environments | 3 | environments | Classifieds, Reddit, shopping | Author-reported | p. 6 |
| Image perturbation ε | 16/256 | pixel-value bound | Infinity-norm constraint on one image | Author-reported | p. 6 |
| Trigger share of webpage | <5 | % pixels | Described image-access setting | Author-reported | pp. 1–2, 8 |
| Unaltered screenshot pixels | approximately 95 | % pixels | Image-access explanation | Author-reported | p. 6 |
| Maximum final ASR | 67 | % | Maximum across tested agent conditions; GPT-4V comparison discussed in §5.4 | Author-reported | pp. 1–2, 10 |
| GPT-4o text attack | 40 | % ASR | Text injection | Author-reported | p. 7, Fig. 4A |
| Adversarial caption influence | 92 | % | White-box captioner attack | Author-reported | p. 7, Fig. 4B |
| Captioner attack final | 31 | % ASR | GPT-4o plus white-box captioner | Author-reported | p. 7 |
| Self-caption corruption | 38 | % influence | CLIP transfer into LM captioner | Author-reported | p. 7 |
| Self-caption final | 19 | % ASR | CLIP attack | Author-reported | p. 7 |
| Direct screenshot final | 10 | % ASR | Base agent without captions | Author-reported | p. 8 |
| Reflexion maximum | 2 | attempts | GPT-4o plus captioner experiment | Author-reported | p. 8 |
| Clean-evaluator final | 25 | % ASR | Policy attacked, evaluator clean | Author-reported | p. 8 |
| Joint evaluator final | 36 | % ASR | Policy and evaluator attacked | Author-reported | p. 8 |
| Evaluator-only final | 8 | % ASR | Clean direct policy input | Author-reported | p. 9 |
| Search branching/depth | 3 / 1 | candidates / levels | Evaluated tree-search configuration | Author-reported | p. 9 |
| Clean-value final | 26 | % ASR | Policy attacked, value clean | Author-reported | p. 9 |
| Joint-value final | 38 | % ASR | Policy and value attacked | Author-reported | p. 9 |
| Value-only final | 8 | % ASR | Clean direct policy input | Author-reported | p. 9 |
| Paraphrase final | 27.5 | % ASR | Baseline 31%, captioner attack | Author-reported | p. 10 |
| Consistency final | near zero | ASR | Fixed captioner attack; no exact value supplied | Author-reported | p. 10 |
| Image-heavy pages | 70 | % pages | More than ten images in evaluated webpages | Author-reported | p. 10 |
| Consistency adaptive bound | 38 | % ASR upper bound | Reuses self-caption influence under CLIP attack; not a measured final rate | Author-reported | p. 10 |
| Optimization resolution | 180 | pixels | Main CLIP attack | Author-reported | pp. 7, 21 |
| Full CLIP ablation | 71 | % targeted-caption success | GPT-4V target-equivalent caption metric | Author-reported | p. 21, Table 7 |
| No negative text | 46 | % targeted-caption success | Same metric | Author-reported | p. 21 |
| Single encoders | 9, 23, 20, 31 | % targeted-caption success | B/32, B/16, L/14, L/14@336px | Author-reported | p. 21 |
| Synthetic 128/2048 | 29 / 13 | % ASR | Without / with descriptive text | Author-reported | p. 8, Table 3 |
| Synthetic 128/512 | 45 / 22 | % ASR | Without / with descriptive text | Author-reported | p. 8 |
| Synthetic 256/2048 | 40 / 33 | % ASR | Without / with descriptive text | Author-reported | p. 8 |
| Synthetic 256/512 | 55 / 38 | % ASR | Without / with descriptive text | Author-reported | p. 8 |
| Decoding temperature | 0 | setting | All listed LMs | Author-reported | p. 16 |
| Clean-evaluator reduction | 6; approximately 19.35 | percentage points; % relative | 31−25; (31−25)/31 ×100 | Analyst-derived | Fig. 5 |
| Joint-evaluator increase | 5; approximately 16.13 | percentage points; % relative | 36−31; (36−31)/31 ×100 | Analyst-derived | Fig. 5 |
| Joint-value increase | 7; approximately 22.58 | percentage points; % relative | 38−31; (38−31)/31 ×100 | Analyst-derived | Fig. 6 |

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Restricted environmental changes can redirect agents. | Targeted final ASRs across text/image conditions. | Figs. 4–6; X1–X7 | pp. 7–9 | HIGH for tested settings; no universal rate. |
| Corrupted images can become malicious captions. | 0.92 caption edge, 0.31 final rate. | Fig. 4B; X2 | p. 7 | HIGH; known captioner attacked, black-box policy downstream. |
| Black-box image attacks transfer with reduced effectiveness. | 19% self-caption final and 10% screenshot final. | Fig. 4C–D | pp. 7–8 | HIGH for outcomes; not proof of every proposed mechanism. |
| Clean evaluators can filter adversarial trajectories. | 31% → 25%. | Fig. 5A/C | p. 8 | HIGH raw rates; summary relative reduction inconsistent. |
| Attacked evaluators can add vulnerability. | Joint attack 36%; evaluator-only 8%. | Fig. 5B/D | pp. 8–9 | HIGH within caption-routing setup. |
| Value functions can help or harm. | Clean 26%, joint 38%, value-only 8%. | Fig. 6 | p. 9 | HIGH for shallow search; scale beyond tested depth unknown. |
| Prompt defenses are insufficient here. | No improvement from prompts; paraphrase 27.5%. | Fig. 7; X8 | p. 10 | HIGH for this attack/configuration; broader defense claims unsupported. |
| Consistency has cost and adaptive limitations. | Near-zero fixed attack, many images per page, reused 0.38 influence bound. | §5.4 | p. 10 | HIGH author report; bound differs from measured adaptive final ASR. |
| Ensemble and negative text improve caption transfer. | 71% full versus 46% without negative and 9–31% single models. | Table 7 | p. 21 | HIGH table values; no uncertainty reported. |
| The requested standalone comparison is not established. | Experiments compare agent variants and intermediate caption behavior. | §§5.1–5.4 | pp. 7–10 | MEDIUM analyst scope assessment; mechanisms supported, comparative magnitude unknown. |

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking a shopping assistant to find a blue motorcycle. Someone selling a different motorcycle changes their listing so the assistant gets a misleading description or an instruction to choose that item. The researchers show that even a small change to one picture can sometimes trigger this chain. They check whether the assistant actually does what the attacker wanted, not just whether it says something strange.

A web assistant can have several helpers: one describes pictures, another chooses actions, another checks the work, and another ranks possible actions. Those helpers can catch mistakes. But if a helper reads the attacker's content, it may pass along a bad description, give harmful advice, or award the wrong action a high score. In this paper, clean checking components helped, while attacked checking components sometimes made the final result worse.

That helps explain why an acting web system has security problems beyond those of one model answering a message. It has more routes through which untrusted content can influence a real task. However, this paper does not run a fair head-to-head test proving that every web agent is more vulnerable than a standalone language model. Its clear lesson is that improving an agent's ability to reason, retry, or search does not automatically make the whole system safer.

## Completeness Audit

The audit is against the supplied 22-page paper and the object inventory, not an assertion that every word has been reproduced. Reviewed visual objects were checked in rendered images as well as supplied text. Pages 11–13 and 22 received text-only coverage.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes, text and visual | Yes | Fully represented | Headline claims qualified by configuration. |
| §1 Introduction | Yes, text and visual | Yes | Represented in compressed form | Motivation, gap, contributions, and numerical discrepancies retained. |
| §2 Related Work | Yes, text and visual | Yes | Represented in compressed form | Three categories retained; citation-by-citation restatement omitted. |
| §3.1 Threat Model | Yes, text and visual | Yes | Fully represented | Access limits and trust partition preserved. |
| §3.2 Agent Graph | Yes, text and visual | Yes | Fully represented | Nodes, edges, examples explained. |
| §3.3 Propagation | Yes, text and visual | Yes | Fully represented | Definition, examples, branching, reuse, component effects. |
| §4.1 Task Curation | Yes, text and visual | Yes | Fully represented | All four task components and four steps. |
| §4.2 Attacker Access | Yes, text and visual | Yes | Fully represented | Text/image distinction and bound. |
| §4.3 Attack Methods | Yes, text and visual | Yes | Fully represented | Three methods and equations. |
| §5.1 Policy Models | Yes, text and visual | Yes | Fully represented | All four conditions; scatter values limited by labels. |
| §5.2 Evaluators | Yes, text and visual | Yes | Fully represented | Base, clean, joint, evaluator-only conditions. |
| §5.3 Value Functions | Yes, text and visual | Yes | Fully represented | All conditions and search settings. |
| §5.4 Defenses | Yes, text and visual | Yes | Fully represented | Prompts, paraphrase, consistency, speculative hierarchy attribution. |
| §6 Conclusions | Yes, text and visual | Yes | Represented in compressed form | Implications and proposed directions. |
| Objectives O1–O7 | Yes | Yes | Fully represented | Analyst indexing of author objectives/questions. |
| Formal hypotheses | Assessed | Yes | No formal list present | Appendix mechanism hypotheses distinguished from tested outcomes. |
| X1–X11 experiments | Yes | Yes | Fully represented | Conditions and metric differences preserved. |
| Figure 1 | Yes, visual | Yes | Fully represented | Targeted workflow. |
| Figure 2A–D | Yes, visual | Yes | Fully represented | Four architectures. |
| Figure 3a–c | Yes, visual | Yes | Fully represented | Illustrative rather than experimental values. |
| Figure 4A–D | Yes, visual | Yes | Fully represented | Exact displayed graph values. |
| Figure 4 scatter | Yes, visual | Yes | Represented in compressed form | Exact unlabeled coordinates not reconstructed. |
| Figure 5A–D | Yes, visual | Yes | Fully represented | Branching and final outcomes. |
| Figure 6A–D | Yes, visual | Yes | Fully represented | Value-function comparisons. |
| Figure 7 | Yes, visual | Yes | Fully represented | Exact unlabeled bar values remain uncertain. |
| Figure 8 | Yes, visual | Yes | Represented in compressed form | Screenshot role; tiny listing details secondary. |
| Figure 9 | Yes, visual | Yes | Represented in compressed form | External-caption pipeline. |
| Figure 10 | Yes, visual | Yes | Represented in compressed form | Base pipeline; repetitive example compressed. |
| Figure 11 | Yes, visual | Yes | Uncertain | Self-caption architecture represented; label ambiguity disclosed. |
| Figure 12 | Yes, visual | Yes | Fully represented | Four size settings and text context. |
| Figure 13 | Yes, visual | Yes | Represented in compressed form | Trend and axes; unlabeled cell values uncertain. |
| Tables 1–3 | Yes, text and visual | Yes | Fully represented | Definitions, taxonomy, all quantitative entries. |
| Table 4 | Yes, text and visual | Yes | Represented in compressed form | All substantive template categories retained. |
| Table 5 | Yes, text and visual | Yes | Represented in compressed form | Semantic pairs grouped; dash handling unknown. |
| Table 6 | Yes, text and visual | Yes | Represented in compressed form | Attack roles and match meaning; long payloads compressed. |
| Table 7 | Yes, text and visual | Yes | Fully represented | All listed rates and metric caveat. |
| M0 edge-weight definition | Yes, text and visual | Yes | Fully represented | Meaning, assumptions, example, reuse. |
| E1 and E2 | Yes, text and visual | Yes | Fully represented | Objectives, variables, constraints, limitations. |
| Algorithms / pseudocode | Assessed | Yes | No standalone pseudocode present | Curation and attack procedures explained. |
| Theorems / lemmas / proofs | Assessed | Yes | None identified | No theoretical result invented. |
| Major contributions | Yes | Yes | Fully represented | Benchmark, framework, engineering, empirical findings, implementation claim. |
| Author limitations | Yes; p. 22 text-only | Yes | Fully represented | All three explicit limitations and defense caveats. |
| Appendix A.1–A.2 | Yes, text and visual | Yes | Fully represented | Templates and evaluation primitives. |
| Appendix B.1–B.4 | Yes, text and visual | Yes | Represented in compressed form | Versions, compute, strings, prompt principles retained. |
| Appendix C.1–C.2 | Yes, text and visual | Yes | Fully represented | Ablations, resolution and simulation. |
| Appendix D | Yes; p. 22 text-only | Yes | Fully represented | Limitations and impact concerns. |
| Acknowledgments | Yes, text-only | Yes | Inspected but deliberately compressed as secondary | Cisco and AI2050/Schmidt Sciences support reported; not efficacy evidence. |
| References | Yes; pp. 11–13 text-only | Yes | Inspected but deliberately omitted as repetitive/non-substantive for this explanation | Bibliographic listing not reproduced or externally verified. |
| Separate supplementary artifacts | No | Boundary stated | Missing from supplied material | No separate artifact reviewed. |
| Repository implementation | No | Boundary stated | Inaccessible within closed-document task | Existence/release reported only. |

### Missing or inaccessible material

No physical page text is missing from the supplied 1–22 sequence. Visual renderings for pp. 11–13 and 22 are absent, so layout and any unreported visual details on those pages cannot be checked. Repository files, cited works, separate supplementary artifacts, complete omitted system/few-shot prompts, and omitted safety-prompt examples were not available for inspection. Their contents were not inferred.

### Uncertain interpretations

Unresolved items are relative-percentage claims versus displayed rates; Figure 11's label ambiguity; Figure 7's bar-index wording; notation changes for targets and inactive edges; the exact implementation meaning of dashes in Table 5; unlabeled scatter/heatmap/bar values; and missing experiment-specific denominators and uncertainty measures. The instruction-hierarchy explanation is explicitly the authors' best guess. The question of greater vulnerability than standalone LMs remains an analyst-motivated interpretation rather than a direct comparative result.

### Deliberately compressed material

The bibliography, repeated page headers, repeated architecture-example text, full attack payloads, and repetitive goal-template wording are compressed. Funding is noted without reproducing the full acknowledgment. Screenshot details irrelevant to architecture or evaluation are not transcribed. This compression preserves substantive method categories and results while avoiding repetition and unnecessary reproduction of malicious example instructions.

### Potential omissions

Every identified substantive section, subsection, experiment, figure, table, mathematical object, contribution, and explicit limitation has a representation above. Exact unlabeled graphical coordinates, missing implementation settings, and omitted prompt content remain unresolved rather than silently filled. This is inventory-based coverage of the supplied material, not a claim of word-for-word preservation or independent reproduction.
