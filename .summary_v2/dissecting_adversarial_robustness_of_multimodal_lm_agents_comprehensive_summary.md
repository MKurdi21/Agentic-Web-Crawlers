# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes. Complete page-labeled text for a 22-page paper was supplied. |
| Available page range | pp. 1–22. |
| Apparently missing pages | None. |
| Native/extracted text | Available for every page; no page was mechanically classified as scanned or unusually low-text. |
| Visually rendered pages inspected | pp. 1–10 and 14–21. |
| Pages not visually rendered | pp. 11–13 and 22. Pages 11–14 are primarily references; p. 22 continues the limitations and broader-impact discussion. Their supplied text was inspected, but pp. 11–13 and 22 were not visually verified. |
| Figures | Figures 1–13 were available on rendered pages and visually inspected. Fine details in the Figure 4 scatterplot and exact heatmap-cell values in Figure 13 are not fully legible; conclusions there rely partly on the caption and accompanying author-provided text. |
| Tables | Tables 1–7 were supplied as text; all were readable. Tables 1–4 and 7 were also visually inspected. Tables 5–6 were visually inspected, although long attack strings are compressed below. |
| Equations | Equations (1) and (2), plus the unnumbered definition of \(\lambda(e)\), were readable in the text and rendered pages. Superscripts/subscripts are potentially extraction-sensitive, so notation was cross-checked against the images. |
| Appendices | Appendices A–D are present on pp. 14–22. |
| Supplementary material | No separate supplementary file was supplied. The paper points to an external code/data repository, but it was neither opened nor evaluated. |
| Algorithms/pseudocode | None presented as a formal algorithm. |
| OCR needed | No. Native text was sufficient; images were used to verify layouts and mathematical notation. |
| Material intentionally unavailable | System prompts and few-shot examples associated with Figures 9–11 are explicitly omitted by the authors. Two examples in the safety prompts on p. 20 are also omitted. |
| Closed-document constraint | Honored. All statements below use only the supplied paper and page images. No external verification or contextual information is introduced. |

Evidence labels used below:

- **[A] Author-reported**: explicitly stated by the paper.
- **[B] Directly observable**: visible in a supplied figure or table.
- **[C] Analyst-derived**: calculated from supplied values, with operands shown.
- **[D] Analyst interpretation**: a clearly marked inference rather than an author claim.

# 1. Plain-Language Orientation

This paper studies whether web-browsing agents built from multimodal language models can be secretly redirected by content placed on a webpage. A normal user might ask an agent to find a product, but a malicious seller could alter one product description or make an almost invisible change to one product image so that the agent performs the seller’s chosen action instead.

This matters because an agent is not merely a chatbot producing text. It observes an environment, selects actions, and may contain several interacting components: an image captioner, a policy model that chooses actions, an evaluator that critiques completed attempts, or a value function that ranks candidate actions. A vulnerability in any component may propagate through the system and cause a real action. [A; pp. 1–4]

The authors:

1. construct **VWA-Adv**, 200 targeted adversarial tasks derived from VisualWebArena;
2. define a realistic attacker who can alter only their own small portion of the environment;
3. implement text prompt injection, a white-box captioner attack, and a transferable black-box image attack;
4. introduce **Agent Robustness Evaluation (ARE)**, which represents an agent as a graph and measures adversarial influence along its edges; and
5. test base, caption-augmented, reflexion, and tree-search agents, plus several defenses. [A; pp. 1–10]

The main result is that every tested component can become an attack route. Imperceptible changes to one image—affecting less than 5% of the webpage pixels and bounded by \(16/256\) per pixel—produce attack success rates as high as 67% in the reported experiments. Components such as evaluators and value functions help when clean, but can make the full agent less robust when the attacker also compromises them. [A; pp. 1–2, 6–10]

The central contribution is therefore not just another attack. It is a system-level account of how adversarial influence enters, propagates through, is blocked by, or is amplified by components in a compound agent.

# 2. Document Roadmap

| Part | Pages | Role |
|---|---:|---|
| Abstract and §1 Introduction | 1–2 | Motivates system-level adversarial evaluation and states contributions and headline findings. |
| §2 Related Work | 2–3 | Positions the study relative to autonomous agents, adversarial robustness, and indirect prompt injection. |
| §3 Agent Robustness Evaluation | 3–5 | Defines the threat model, agent graphs, adversarial influence, and edge weights. |
| §4 Adversarial Robustness in VisualWebArena | 5–7 | Describes VWA-Adv, attacker access, task construction, metrics, and attacks. |
| §5 Evaluation | 7–10 | Tests policy models, captioners, evaluators/reflexion, value functions/tree search, and defenses. |
| §6 Conclusions | 10 | Summarizes implications and proposed future directions. |
| Acknowledgments and references | 11–14 | Credits, funding, and cited literature. |
| Appendix A | 14–15 | Full adversarial-goal templates and execution-based evaluation functions. |
| Appendix B | 16–20 | Agent illustrations, models, compute, attack strings, and safety prompts. |
| Appendix C | 21 | CLIP-attack ablations and the synthetic generalization experiment. |
| Appendix D | 21–22 | Limitations and broader impact. |

# 3. Background and Context

A **language-model agent** uses a language model to observe an environment, reason, and choose actions. A **multimodal** agent accepts more than one modality, here principally webpage text and screenshots.

A **policy model** chooses actions. A **captioner** converts images into text that the policy can consume. An **evaluator** judges whether an attempted trajectory achieved the user’s goal and may provide a written reflection. A **value function** scores candidate actions in tree search.

An **adversarial example** is a deliberately modified input intended to produce harmful or incorrect behavior. In **indirect prompt injection**, malicious instruction-like text is placed in the environment rather than supplied as the legitimate user’s instruction.

A **white-box attack** knows the attacked component’s parameters and can optimize directly through it. A **black-box attack** lacks that internal access and must transfer an attack created against surrogate models.

The paper distinguishes:

- **Benign success rate (Benign SR):** frequency with which an unattacked agent achieves the user’s goal.
- **Attack success rate (ASR):** frequency with which an attacked agent achieves the attacker’s targeted goal. [A; p. 6]

A system can be **robustifying** if it decreases adversarial influence between its input and output. The important warning is that a component which filters an attack in one configuration may itself provide a fresh attack surface in another.

# 4. Research Problem and Gap

## Existing problem

Agents increasingly act in web and other real environments. Malicious environmental content can influence their decisions and actions. Unlike ordinary model evaluations, agent security involves sequences of observations, actions, and multiple components. [A; pp. 1–3]

## Shortcomings attributed to previous approaches

The authors state that existing language-model safety evaluations inadequately address compound agents. Earlier adversarial attacks often assume access to nearly the model’s entire input and a direct target output. In the studied web-agent setting, an attacker controls only a fragment of the environment, and the manipulation must survive multimodal processing, reasoning, grounding, and downstream decision-making. [A; pp. 1, 3]

Concurrent agent prompt-injection work is characterized as focusing less on multimodal input and system-level propagation across components. This is the authors’ positioning, not an independently verified literature assessment. [A; p. 3]

## Research gap

The identified gap is a realistic benchmark and analytical framework for determining:

- whether targeted attacks with restricted environmental access work against multimodal agents;
- how adversarial influence propagates across compound systems;
- whether inference-time components improve or degrade robustness; and
- where defenses should intervene. [A; pp. 1–2]

## Motivation and scope

The work concentrates on VisualWebArena web agents, targeted attacks, text or single-image access, and base, caption-augmented, reflexion, and tree-search configurations. It does not claim a universal evaluation of all agent environments or algorithms.

# 5. Research Questions / Objectives / Hypotheses

The paper does not enumerate formal “RQ1/RQ2” research questions or preregistered hypotheses. Its objectives and prose questions can be reconstructed without turning them into stronger formal claims:

1. **Objective O1:** Create realistic targeted adversarial tasks for multimodal web agents. [A; pp. 1–2, 5–6]
2. **O2:** Determine whether restricted text or image manipulation can hijack state-of-the-art agents. [A; pp. 1–3]
3. **O3:** Measure adversarial influence at the component and system levels using ARE. [A; pp. 2, 3–5]
4. **O4:** Determine whether captioners, evaluators, and value functions block or introduce vulnerabilities. [A; pp. 5, 7–9]
5. **O5:** Test several prompt-, transformation-, and consistency-based defenses. [A; p. 10]

The authors explicitly ask:

- Can evaluators improve robustness?
- What happens if the attacker adapts to the evaluator?
- Can the evaluator alone break the reflexion agent?
- Can value functions improve robustness?
- What happens if the attacker adapts to the value function?
- Can attacking the value function alone break tree search? [A; pp. 8–9]

Two explicit method hypotheses appear in Appendix C:

- negative text may improve the CLIP attack by moving an image representation away from its original meaning;
- an ensemble may improve transfer by finding adversarial directions common across CLIP models. [A; p. 21]

Both receive supportive ablation evidence, though the paper does not provide inferential statistical tests.

# 6. Assumptions / Threat Model

## System and environment

The agent receives observations from an environment and is directed by a benign user goal. The environment is divided into:

- a **trusted portion**, which the attacker cannot change;
- an **untrusted portion**, such as the attacker’s own product listing, post, description, or image. [A; p. 3]

## Attacker objective

The attacker seeks a **targeted adversarial goal**, not merely arbitrary failure. Examples include falsifying an item’s properties, causing selection of the wrong item, adding an item to a cart, upvoting a post, or forcing a review with a specified sentiment. [A; pp. 5, 15]

## Attacker capabilities

- The attacker is a legitimate but malicious platform user, distinct from the agent’s user.
- With **text access**, the attacker adds one piece of text to their own listing.
- With **image access**, the attacker perturbs one image under an \(L_\infty\) limit of \(\epsilon=16/256\).
- Depending on the experiment, the attacker may know a white-box captioner or may attack only surrogate CLIP encoders and transfer the result to a black-box language model. [A; p. 6]

## Excluded capabilities

The attacker cannot directly alter:

- the benign user’s goal;
- agent system prompts or model parameters;
- other users’ content;
- the platform’s user-interface design. [A; p. 3]

## Evaluation assumptions

ARE’s worked definition assumes a deterministic environment, so the adversarial influence of a realized intermediate value is 0 or 1. The authors say it generalizes to \([0,1]\) for stochastic environments. [A; p. 4]

VWA-Adv initializes an episode at the point where the trigger is encountered, ensuring exposure. Consequently, the study estimates success conditional on trigger exposure rather than the probability that a full episode starting at the homepage encounters the trigger. [A; pp. 5–6; D interpretation about conditioning]

# 7. Methodology

## Study design

This is a cybersecurity and machine-learning empirical study with a benchmark/dataset contribution and a graph-based evaluation framework.

## VWA-Adv dataset construction

VWA-Adv contains **200 tasks** drawn from the classifieds, Reddit-like social-media, and shopping environments in VisualWebArena. Each task contains:

1. a solvable original VWA task;
2. one trigger image or trigger text;
3. a distinct targeted adversarial goal and evaluation script; and
4. an initial state positioned where the trigger was selected. [A; pp. 5–6]

Curation proceeds by running the best agent from the cited VWA work and discarding original tasks it cannot solve, randomly choosing a trigger along the successful trajectory, constructing a distinct adversarial goal using templates, and manually annotating a binary evaluation. [A; pp. 5–6]

The paper does not report train/validation/test splits, class distributions across sites or attack-goal categories, annotator counts, inter-annotator agreement, repeated-run counts, random seeds, or confidence intervals.

## Evaluation functions

After termination, scripts inspect the final environment state and/or agent response. Primitives include exact match, fuzzy match, “must include,” and URL match. Targets include cart state, destination webpage, submitted form text, and response text; one fuzzy-matching example uses GPT-4. [A; p. 15]

## ARE framework

The agent is represented as \(G=(V,E)\). Nodes include the environment, components, and a unique finish node. An edge means that the child consumes the parent’s output. ARE assigns each edge a weight \(\lambda(e)\), representing expected adversarial influence. Comparing incoming and outgoing weights indicates whether a component reduces or preserves attack potential. [A; pp. 3–5]

## Models and agent configurations

Reported language-model endpoints are:

- GPT-4V: `gpt-4-vision-preview`
- Gemini-1.5-Pro: `gemini-1.5-pro-preview-0409`
- Claude-3-Opus: `claude-3-opus-20240229`
- GPT-4o: `gpt-4o-2024-05-13` [A; p. 16]

All are decoded at temperature 0. Agent types include:

- base policy agent;
- white-box-captioner agent;
- black-box self-captioning agent;
- reflexion agent, with at most two attempts;
- tree-search agent, with branching factor 3 and depth 1. [A; pp. 4, 7–9, 16–18]

The reflexion and tree-search experiments use GPT-4o plus a captioner to control API cost. Clean versus attacked inputs to evaluators/value functions are simulated by supplying clean versus adversarial captions. [A; p. 8]

## Attack construction

### Text prompt injection

A malicious string is inserted as the single allowed text trigger and supplied to the model alongside normal webpage text and the screenshot. Strings were selected to be effective against GPT-4V. No white-box textual attack is evaluated. [A; p. 6]

### White-box captioner attack

Projected gradient descent modifies image \(x\) by \(\delta\) to maximize the captioner’s likelihood of target text \(z\), subject to the \(L_\infty\) constraint. [A; Eq. (1), p. 6]

### Black-box CLIP attack

The attack optimizes against four surrogate Contrastive Language–Image Pretraining (CLIP) encoders: ViT-B/32, ViT-B/16, ViT-L/14, and ViT-L/14@336px. It raises image similarity to adversarial text \(z\) and lowers similarity to negative text \(z^{-}\). Perturbations are optimized at 180 pixels to improve transfer. [A; Eq. (2), pp. 6–7, 21]

## Compute

Gradient attacks and the captioner ran on an NVIDIA A6000 or A100 80G. Frontier models were accessed through APIs. The paper gives no runtime, query count, monetary cost, optimizer step count, step size, software versions, or complete PGD hyperparameters. [A; p. 17]

## Metrics and statistical methods

Primary metrics are Benign SR and ASR. Target-caption success is used in Appendix C. No hypothesis tests, error bars, confidence intervals, or variance estimates are reported in the supplied work.

# 8. Experiments / Analyses

## X1 — Text injection against policy models

- **Purpose:** Test whether one malicious text field overrides multimodal evidence.
- **Setup:** GPT-4o base policy agent, attacked webpage text plus screenshot.
- **Metric:** ASR.
- **Result:** 40% ASR. [A; Fig. 4A, p. 7]
- **Interpretation:** Text injection can override the effect of visual inputs.
- **Caveat:** Task count for this condition and uncertainty are not stated.

## X2 — White-box image attack against a captioner

- **Setup:** Caption-augmented GPT-4o agent; one perturbed image attacks the captioner.
- **Results:** 92% adversarial caption influence at the captioner-to-policy edge; 31% final ASR. [A/B; Fig. 4B, p. 7]
- **Interpretation:** A captioner converts a restricted image attack into malicious text for the policy.
- **Caveat:** A large fraction of adversarial captions does not translate into successful final actions.

## X3 — CLIP attack against self-captioning

- **Setup:** Black-box model generates its own caption; attack transfers from CLIP surrogates.
- **Results:** 38% adversarial-caption edge weight; 19% final ASR. [A/B; Fig. 4C, p. 7]
- **Interpretation:** CLIP attacks transfer to a black-box multimodal model, though downstream policy behavior filters some influence.

## X4 — CLIP attack against a base screenshot agent

- **Setup:** No captioning stage; perturbed trigger occupies under 5% of screenshot pixels.
- **Result:** 10% ASR. [A; Fig. 4D, pp. 7–8]
- **Interpretation:** Transfer through the context of a much larger screenshot is harder.

## X5 — Synthetic screenshot generalization analysis

Four images are placed on a blank background; the first is adversarial. Image size, screenshot size, and presence of descriptive text are varied.

| Image/screenshot resolution | Without other text | With other text |
|---|---:|---:|
| 128/2048 | 29% | 13% |
| 128/512 | 45% | 22% |
| 256/2048 | 40% | 33% |
| 256/512 | 55% | 38% |

[A; Table 3, pp. 8, 20–21]

Larger relative image size raises ASR, while surrounding text describing the original content usually lowers it. No repetitions or uncertainty estimates are stated.

## X6 — Policy-model robustness–utility comparison

Figure 4’s scatterplot compares Benign SR and ASR for GPT-4o, GPT-4V, Claude-3-Opus, and Gemini-1.5-Pro across settings A–D. The authors report a positive correlation between benign capability and ASR and say GPT-4o offers the best robustness–utility trade-off. [A; p. 8]

Exact coordinates for most points are not labeled or reliably readable, so they are not reconstructed here.

## X7 — Reflexion/evaluator analysis

| Condition | Base/first-stage influence | Final ASR | Result |
|---|---:|---:|---|
| Policy attacked; no evaluator | 31% | 31% | Baseline |
| Evaluator attacked alone | Policy clean | 8% | Evaluator can create adversarial reflections |
| Policy attacked; evaluator clean | 31% first attempts | 25% | Evaluator blocks some attacks |
| Policy and evaluator attacked | 31% first-stage influence | 36% | Joint attack is worse than base |

[A/B; Fig. 5, pp. 8–9]

In the clean-evaluator condition, 18% of the 31% adversarial first attempts are accepted, no adversarial reflections are reported, and the second-attempt ASR is 7%. With an attacked evaluator, evaluator-to-finish influence rises from 18% to 21% and adversarial-reflection influence from 0% to 6%.

Derived comparisons:

- Clean evaluator: \(31-25=6\) percentage-point reduction; \(6/31\approx19.4\%\) relative reduction. The introduction calls this 23% relative; see §14 for the discrepancy.
- Attacked evaluator: \(36-31=5\) percentage-point increase; \(5/31\approx16.1\%\) relative increase. The paper variously summarizes this as 15% or 20%.

## X8 — Tree-search/value-function analysis

| Condition | Base influence | Final ASR | Result |
|---|---:|---:|---|
| Policy attacked; no value function | 31% | 31% | Baseline |
| Value function attacked alone | Policy clean | 8% | Search exposes low-probability harmful actions |
| Policy attacked; value function clean | 31% | 26% | Clean ranking blocks some attacks |
| Policy and value function attacked | 31% | 38% | Compromised ranking favors attacks |

[A/B; Fig. 6, p. 9]

Derived comparisons:

- Clean value function: \(31-26=5\) percentage points, or \(5/31\approx16.1\%\) relative reduction.
- Joint attack: \(38-31=7\) percentage points, or \(7/31\approx22.6\%\) relative increase. The abstract reports 20%, consistent with rounding but not exact from displayed integers.

## X9 — Defense analysis

- Safety/system prompt: no improvement over the 31% baseline.
- Aggressive abstention prompt: no improvement.
- GPT-4o paraphrasing: ASR falls from 31% to 27.5%.
- Explicit image–text consistency checking: captioner-attack ASR falls to near zero.
- Adaptive CLIP caveat: because the checking component can itself be attacked, the authors give a 38% upper bound against a determined adversary. [A; Fig. 7, p. 10]

The consistency defense is computationally expensive: 70% of evaluated webpages have more than 10 images, requiring many added API calls. [A; p. 10]

## X10 — CLIP optimization-resolution ablation

Figure 13 varies optimization and inference resolutions among 180, 384, 512, 768, and 1024 pixels. Lower optimization resolution produces higher target-caption success; inference resolution has little effect. The authors interpret this as possible reduced overfitting to surrogate CLIP models and robustness to resizing. [A/B; Fig. 13, p. 21]

Exact cell values are not labeled and are not confidently recoverable from the heatmap.

## X11 — Negative-text and ensemble ablations

| Attack variant | Target-caption success |
|---|---:|
| Original Eq. (2) | 71% |
| Without negative text | 46% |
| ViT-B/32 only | 9% |
| ViT-B/16 only | 23% |
| ViT-L/14 only | 20% |
| ViT-L/14@336px only | 31% |

[A/B; Table 7, p. 21]

The full ensemble with negative text is best. Removing negative text costs 25 percentage points. The strongest single encoder reaches 31%, 40 percentage points below the full method. These differences are [C] analyst-derived.

# 9. Results

1. **Targeted attacks work under restricted access.** A single text field or one image bounded by \(16/256\) can redirect tested agents. The maximum reported ASR is 67%. [A; pp. 1–2, 10]

2. **Captioners are a high-leverage attack surface.** A white-box image attack makes 92% of captions adversarial and yields 31% final ASR. [A; Fig. 4B, p. 7]

3. **Transfer to black-box vision-language models is possible but degrades through context.** Self-captioning yields 19% ASR; direct screenshot attacks yield 10%. [A; Fig. 4C–D, pp. 7–8]

4. **Helpful components are conditionally helpful.** A clean evaluator lowers displayed ASR from 31% to 25%; a clean value function lowers it to 26%. [A; Figs. 5–6, pp. 8–9]

5. **Those same components become new vulnerabilities.** Attacking only an evaluator or value function produces 8% ASR despite an uncompromised policy. Joint attacks raise final ASR to 36% for reflexion and 38% for tree search. [A; Figs. 5–6]

6. **More inference-time computation does not guarantee security.** Reflexion and tree search improve robustness only when their auxiliary components remain uncompromised. In the paper’s worst tested cases, they are less robust than the base agent. [A; p. 9]

7. **Basic defenses are weak.** Safety prompting and abstention do not improve ASR; paraphrasing gives a modest 3.5-percentage-point decrease; explicit consistency checking works against the evaluated captioner attack but is expensive and exposes an attackable component. [A/C; p. 10]

8. **CLIP transfer depends on attack construction and visual context.** Low optimization resolution, negative text, model ensembling, larger relative trigger size, and absence of corrective surrounding text all improve attack success. [A; Tables 3 and 7, Fig. 13]

No confidence intervals or significance tests establish whether smaller differences are statistically reliable.

# 10. Figure-by-Figure Interpretation

### Figure 1 — Targeted environmental attack

A horizontal workflow shows a benign request (“add the latest white headphones”), an image/text trigger inserted into the environment, repeated environment–agent interaction, and a targeted evaluation checking whether the agent left a positive comment on the attacker’s product. [B; p. 2] It establishes that success means performing a specific malicious action, not simply failing the user task.

### Figure 2 — Four agent graphs

- **A:** Environment → policy → finish.
- **B:** Environment → captioner → policy → finish, with direct environment input also reaching the policy.
- **C:** Environment → policy → evaluator; the evaluator can terminate or return a reflection to another policy attempt.
- **D:** Environment → policy → value function → finish, with the policy proposing candidates and a scoring stage selecting among them. [A/B; p. 4]

Arrows represent intermediate-output flow, including feedback/branching rather than only a simple feed-forward chain.

### Figure 3 — How an added component changes robustness

Three schematic cases use edge weights:

- baseline \(A\rightarrow D\): adversarial influence 1.0 then 0.5;
- clean component \(B\): influence falls from 0.5 to 0.2;
- attacked component \(B\): a new weight-1.0 input can raise outgoing influence to 0.7. [B; p. 5]

The figure is conceptual, not an empirical result.

### Figure 4 — Policy and captioner robustness

Panels A–D visualize text injection (40%), white-box captioner attack (92% adversarial captions; 31% final), self-caption CLIP attack (38%; 19%), and direct screenshot CLIP attack (10%). Red edges carry attacked environmental input, blue edges clean input, and purple edges downstream influence. [A/B; pp. 7–8]

The scatterplot’s x-axis is Benign SR and y-axis ASR. Colors encode language models; marker shapes encode attack settings. The authors report positive capability–vulnerability correlation and favor GPT-4o’s trade-off, but most exact coordinates are unreadable.

### Figure 5 — Evaluators in reflexion agents

Four panels compare base, evaluator-only, clean-evaluator, and jointly attacked configurations. Feedback from evaluator to the second policy attempt is the important control loop. Clean evaluation reduces final ASR to 25%; evaluator-only attack produces 8%; joint attack produces 36%. [A/B; pp. 8–9]

### Figure 6 — Value functions in tree search

Four analogous panels show base, value-only, clean-value, and joint attacks. A clean value function reduces final ASR to 26%, but an attacked one raises it to 38%; value-only attack produces 8%. [A/B; p. 9]

### Figure 7 — Defense effectiveness

A horizontal ASR bar chart compares safety prompt, abstention prompt, paraphrasing, consistency checking, and a no-defense reference. The dashed no-defense line is near 0.31. Prompt defenses remain near baseline; paraphrasing is 0.275; consistency is near zero. [A/B; p. 10] Exact prompt-bar values are not numerically labeled.

### Figure 8 — VisualWebArena screenshot

A tall classifieds page shows many motorcycle listings, text, prices, images, filters, and Set-of-Marks annotations. [B; p. 16] It demonstrates why one trigger image occupies a small share of the whole screenshot and why direct image-to-screenshot transfer is difficult.

### Figure 9 — LM plus external captioner

The screenshot is parsed into structured webpage text, while LLaVA supplies image descriptions. GPT-4V combines them with the user goal and previous action and outputs `click [34]`. [A/B; p. 17] System prompts and demonstrations are absent.

### Figure 10 — Base LM agent

The structure resembles Figure 9, but the parsed image element lacks a generated description and GPT-4V handles the observation directly. [A/B; p. 17]

### Figure 11 — LM plus self-captioning

GPT-4V first produces an image description, which is inserted into the structured observation, and then acts on the enriched input. [A/B; p. 18] This arrangement explains the two-stage adversarial-influence measurements in Figure 4C.

### Figure 12 — Synthetic screenshot experiment

The top shows four image/screenshot resolution combinations: 128/2048, 256/2048, 128/512, and 256/512. The bottom shows optional surrounding parsed text. [A/B; p. 20] It operationalizes the two factors reported in Table 3: relative trigger size and competing textual context.

### Figure 13 — Resolution ablation heatmap

Both axes range over 180, 384, 512, 768, and 1024 pixels: optimization resolution vertically and inference resolution horizontally. Darker cells indicate greater target-caption success. Rows change more than columns; the 180-pixel optimization row is strongest. [A/B; p. 21] Exact cell values are not labeled.

# 11. Table-by-Table Interpretation

### Table 1 — Meaning of adversarial influence

It defines when \(\mathrm{AdvIn}(c)=1\):

- observations originate in the untrusted environment;
- actions achieve the adversarial goal;
- captions or reflections would cause a perfectly compliant policy to achieve it;
- an unexecuted edge \(\varnothing\) has influence 0. [A; p. 5]

### Table 2 — Condensed adversarial-goal taxonomy

Two families are listed:

- **Illusioning:** false object attributes or metadata such as color, price, reviews, rank, email, or mileage.
- **Goal misdirection:** selecting/not selecting, adding to cart, or leaving/modifying a review/comment. [A; p. 5]

### Table 3 — Screenshot transfer factors

ASR ranges from 13% to 55%. The best condition is a 256-pixel image in a 512-pixel screenshot without other text; the worst is 128/2048 with other text. Other text lowers ASR by 16, 23, 7, and 17 percentage points in the four respective rows [C; subtraction]. [A; p. 8]

### Table 4 — Full goal-template inventory

It expands Table 2 to 16 illusioning templates and 10 goal-misdirection templates, covering object identity, count/capacity, color, shape, background, price, reviews, comments, rank, image text, seller identity, mileage, angle, location, stars, navigation, cart/wish-list actions, review form/sentiment, reversed bargaining or sentiment, upvoting, non-selection, and claimed unavailability. [A; p. 15]

### Table 5 — CLIP target and negative strings

Examples pair desired semantics with semantics to suppress: white versus black cellphone, outside versus interior of a car, foxes versus castle, red vehicle versus “silver, blue, dark,” empty table versus several people, adults versus baby, and guitar versus office. Some targets have no negative string, denoted by a dash. [A; p. 18]

### Table 6 — Captioner attack strings

The table shows long targeted instructions and false captions. Eleven of the twelve visible examples are marked exact successes; the “add ‘This is great!’” example is marked failure. [B/C; p. 19; count derived from checkmarks] The examples demonstrate both instruction-like outputs and semantic misinformation far outside normal caption style.

### Table 7 — CLIP attack ablations

The full ensemble plus negative text reaches 71%; removing negative text gives 46%; single-model attacks give 9–31%. No statistical uncertainty is supplied. [A; p. 21]

# 12. Diagram / Architecture Interpretation

The core architecture is an information-flow graph:

```text
untrusted/trusted environment
              ↓
  optional perception/captioning
              ↓
          policy model
       ↙               ↘
 evaluator/reflection   value function/search
       ↘               ↙
          action/finish
```

The environment provides both trusted and potentially attacked inputs. Perception may translate a visual perturbation into adversarial text. The policy converts observations or reflections into actions. An evaluator can terminate an attempt or feed a reflection into another attempt. A value function ranks several policy proposals.

ARE treats each interface as an edge whose output distribution can carry adversarial influence. This makes component behavior compositional: the analyst can ask whether the outgoing edge carries less influence than the incoming edge and can reuse an upstream edge weight when downstream components change. [A; pp. 3–5]

The architecture’s security lesson is conditional. A clean downstream gate can reduce harmful influence, but connecting that component to an attacked observation creates another input edge through which influence can enter.

# 13. Equations and Mathematical Concepts

## Unnumbered ARE edge-weight equation — p. 4

\[
\lambda(e)=\mathbb{E}_{c\sim p_e}\left[\mathrm{AdvIn}(c)\right].
\]

- \(e\): a directed edge between components.
- \(c\): the intermediate output carried on that edge.
- \(p_e\): distribution of edge values after potentially attacked ancestors execute.
- \(\mathrm{AdvIn}(c)\in[0,1]\): tightest upper bound on expected ASR attributable to \(c\), assuming no downstream component is additionally attacked.
- \(\lambda(e)\): expected adversarial influence on the edge.

In a deterministic environment, \(\mathrm{AdvIn}(c)\) is treated as 0 or 1. For a branch not executed, \(c=\varnothing\) and its influence is 0.

The caption example clarifies why this is an upper bound rather than the actual success of the present downstream policy: if 80% of captions direct an attack but the current policy follows only half, caption-edge weight is 0.8 while the action-edge weight is 0.4. [A; p. 4]

## Equation (1) — white-box captioner attack, p. 6

\[
\max_{\|\delta\|_\infty\le \epsilon}
\log \pi_{\mathrm{comp}}(z\mid x+\delta).
\]

This selects a bounded perturbation \(\delta\) to make component \(\pi_{\mathrm{comp}}\) assign high likelihood to target text \(z\) when processing image \(x+\delta\). Here \(\epsilon=16/256\). The paper says projected gradient descent is used but does not supply its step count or step size.

## Equation (2) — black-box CLIP ensemble attack, pp. 6–7

\[
\max_{\|\delta\|_\infty\le\epsilon}
\sum_{i=1}^{N}
\left[
\cos\!\left(E_x^{(i)}(x+\delta),E_y^{(i)}(z)\right)
-
\cos\!\left(E_x^{(i)}(x+\delta),E_y^{(i)}(z^-)\right)
\right].
\]

- \(N\): number of surrogate CLIP models; four are listed.
- \(E_x^{(i)}\), \(E_y^{(i)}\): image and text encoders of surrogate \(i\).
- \(z\): target/adversarial text.
- \(z^{-}\): negative text describing semantics to suppress.
- \(\cos(\cdot,\cdot)\): cosine similarity.

The first term moves the perturbed image toward the target-text representation; the subtracted term moves it away from the negative representation. Table 7 supports the roles of both negative text and ensembling.

# 14. Interpretation and Discussion

The experiments support the paper’s broad objectives: restricted environmental attacks can redirect agents, adversarial influence can be localized to interfaces, and added inference-time components have two-sided security effects.

The most important systems insight is that benign utility and adversarial robustness are not interchangeable. Evaluators and value functions can correct a compromised policy only when they remain clean. When they process malicious information, their authority to reject, reflect, or rank gives the attacker another mechanism for steering execution.

The work also shows successive filtering. A 92% adversarial-caption rate becomes 31% final ASR, and a 38% self-caption rate becomes 19% final ASR. [D] This indicates that harmful intermediate content is not automatically equivalent to a completed malicious action; downstream behavior matters.

Conversely, tree search introduces risk even when the policy is clean: exploration exposes low-probability harmful actions that an attacked value function can preferentially select. This supports the authors’ phrase “the more the agent explores, the more it can be exploited.” [A; p. 9]

## Consistency findings

There are numerical wording discrepancies:

1. The introduction says a clean evaluator gives a **23% relative reduction**. Figure 5 and §5.2 display 31% to 25%, which is a 6-percentage-point or approximately 19.4% relative reduction. No unrounded counts are supplied to reconcile this. [A/C; pp. 2, 8]

2. The introduction says the attacked reflexion agent has a **20% relative increase** over the base, while the abstract says compromising the evaluator and value function increases success relatively by **15% and 20%**. Displayed reflexion values 31% to 36% imply approximately 16.1%; displayed tree-search values 31% to 38% imply approximately 22.6%. These may reflect rounding or underlying unrounded results, but the supplied paper does not explain them. [A/C; pp. 1–2, 8–9]

3. The headline maximum of **67% ASR** is stated in the abstract/introduction and later associated with GPT-4V versus GPT-4o’s 31%, but the exact experimental cell, task count, and uncertainty are not tabulated in the supplied main results. [A; pp. 1–2, 10]

The conclusions are directionally consistent with the experiments, but their generality should be read within the evaluated web environments, agents, attack implementations, and conditional trigger exposure.

# 15. Contributions and Novelty

## Conceptual

ARE reframes agent robustness as propagation of adversarial influence through a component graph.

## Methodological

The edge-weight definition separates harmful intermediate information from the behavior of the current downstream component and permits reuse across unchanged upstream configurations.

## Dataset and benchmark

VWA-Adv provides 200 curated targeted attacks, starting states, and execution-based evaluators across three web settings.

## Attack engineering

The work adapts prompt injection, gradient-based image-to-text attacks, and CLIP-surrogate transfer to restricted single-trigger agent scenarios. The CLIP attack adds negative-text separation, an encoder ensemble, and low-resolution optimization.

## Experimental

The authors attack policy, captioner, evaluator, and value-function components individually and jointly, showing both defensive and harmful effects of agent augmentation.

## Implementation

The authors report releasing tasks, attacks, defenses, evaluations, and trigger-injection code. This availability claim was not externally checked.

# 16. Limitations

## Authors’ stated limitations

1. The attacks are engineered adaptations of existing attacks and provide only a lower bound on risk; stronger attacks may exist. [A; pp. 21–22]
2. Evaluation uses a fixed set of web environments, leaving performance in settings such as operating systems unknown. [A; p. 22]
3. Only base, reflexion, and tree-search agents are treated as the state-of-the-art set; emerging algorithms require continued tracking. [A; p. 22]
4. The authors also acknowledge in the results that explicit consistency checking greatly increases API use and remains attackable. [A; p. 10]

## Additional evidence-based analyst observations

These are not stated as formal author admissions:

- Task construction selects tasks solvable by one prior best agent and starts at trigger exposure. This improves interpretability but limits estimates of end-to-end risk across all natural tasks.
- The paper does not report how the 200 tasks divide by platform, access type, goal class, or experimental condition.
- No confidence intervals, variance, significance tests, or run counts are supplied.
- Temperature 0 reduces sampling variability but does not establish deterministic behavior of remote APIs or the web environment.
- Some evaluator/value-function attacks are simulated with adversarial versus clean captions rather than generated end-to-end under every configuration.
- GPT-4-based fuzzy matching may introduce evaluator-model dependence; its accuracy is not assessed here.
- The headline 67% lacks a fully tabulated condition in the supplied pages.
- Several comparisons use tasks selected according to GPT-4V success, which may affect cross-model comparability.
- Exact attack hyperparameters and API costs are incomplete.

# 17. Threats to Validity

## Internal validity

Manual task/evaluator construction, possible API variability, incomplete attack hyperparameters, and simulated attacked-component inputs could affect causal attribution. Ensuring trigger exposure removes one confound but changes the target quantity being measured.

## Construct validity

ASR appropriately captures targeted success, but it does not directly measure user-task failure, severity, detectability, or likelihood of real-world trigger encounter. ARE’s “tightest upper bound” is a deliberately worst-case intermediate measure and should not be mistaken for the current downstream model’s observed ASR.

## External and ecological validity

VisualWebArena supplies realistic web interfaces, but only three web categories are used. Operating systems, mobile apps, physical agents, other websites, longer trajectories, and newly developed agent architectures are untested.

## Statistical conclusion validity

No uncertainty estimates or significance tests accompany the reported percentages. Small gaps, including 31% versus 27.5%, therefore cannot be assigned statistical confidence from the supplied evidence.

## Reproducibility

Model endpoint names, temperature, broad hardware, dataset/code location, attack objective, and some architecture settings are reported. Missing step sizes, optimization iterations, seeds, sample allocations, API versions beyond endpoint dates, and detailed cost/query information limit standalone reproduction from the paper.

## Generalizability

The demonstrated attacks establish existence under evaluated conditions, not universal rates for all deployments. Conversely, because the authors treat their attacks as lower-bound baselines, the study also does not establish an upper bound on risk.

# 18. Future Work and Open Questions

## A. Future work proposed by the authors

- Develop stronger defenses.
- Strengthen the most vulnerable edges identified by ARE.
- Create adversarial versions of newly solvable tasks as agents improve.
- Develop stronger adaptive attacks as defenses evolve.
- Track the robustness of emerging agent algorithms.
- Test more diverse environments, including operating-system settings. [A; pp. 10, 22]

## B. Additional open questions

- How does ASR change when episodes begin naturally rather than at guaranteed exposure?
- Which task, site, and adversarial-goal categories are most vulnerable?
- Can one train components to reduce outgoing ARE weights under adaptive attacks?
- Does adding more reflexion attempts or deeper/wider search amplify or suppress risk?
- How reliable are automated adversarial-goal evaluators?
- What are the latency and monetary costs of robust consistency checking?
- Can joint training secure interfaces without sacrificing benign success?
- How stable are results across repeated runs and model updates?
- Can ARE be extended from deterministic binary influence to calibrated stochastic estimates with uncertainty?

# 19. Terminology and Notation Glossary

| Term | Meaning in this paper |
|---|---|
| LM | Language model. |
| Multimodal LM | Model processing text and visual inputs. |
| Agent | System that observes an environment and selects actions toward a goal. |
| VWA | VisualWebArena, the underlying web-agent environment. |
| VWA-Adv | The authors’ 200-task adversarial extension of VWA. |
| ARE | Agent Robustness Evaluation framework. |
| Benign SR | Success rate on the legitimate user goal without attack. |
| ASR | Attack success rate: rate of achieving the targeted adversarial goal. |
| Policy model | Component proposing or choosing actions. |
| Captioner | Component translating images into text. |
| Evaluator | Component deciding whether an attempted trajectory succeeded and optionally producing a reflection. |
| Reflexion | Reattempt procedure that uses evaluator feedback. |
| Value function | Component scoring candidate actions. |
| Tree search | Procedure exploring several candidate actions and selecting by value. |
| Prompt injection | Malicious instruction-like text embedded in the environment. |
| White-box | Internal parameters are available to the attacker. |
| Black-box | Internal target-model parameters are unavailable. |
| CLIP | Contrastive Language–Image Pretraining model family used as transfer surrogates. |
| PGD | Projected gradient descent, used to optimize bounded perturbations. |
| \(G=(V,E)\) | Directed agent graph with nodes \(V\) and edges \(E\). |
| \(v_{\rm env}\) | Environment-observation node. |
| \(v_{\rm finish}\) | Unique finishing node. |
| \(c\) | Intermediate value on an edge. |
| \(p_e\) | Distribution of values carried by edge \(e\). |
| \(\mathrm{AdvIn}(c)\) | Worst-case downstream adversarial influence of intermediate value \(c\). |
| \(\lambda(e)\) | Expected adversarial influence carried by edge \(e\). |
| \(\varnothing\) | Edge not executed; assigned zero influence. |
| \(x\) | Original trigger image. |
| \(\delta\) | Adversarial image perturbation. |
| \(\epsilon\) | Maximum \(L_\infty\) perturbation magnitude, here \(16/256\). |
| \(z\), \(z^{-}\) | Target adversarial text and negative text to suppress. |
| \(E_x^{(i)},E_y^{(i)}\) | Image and text encoders of the \(i\)th CLIP model. |
| Set-of-Marks | Screenshot parsing/annotation mechanism that associates page elements with action identifiers. |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| VWA-Adv size | 200 | tasks | Curated targeted tasks | Author-reported | p. 5, §4.1 |
| Image perturbation bound | 16/256 | normalized pixel magnitude, \(L_\infty\) | One trigger image | Author-reported | p. 6, §4.2 |
| Unaltered screenshot pixels | approximately 95 | % | Single-image threat | Author-reported | p. 6 |
| Maximum ASR | 67 | % | Headline result across tested agents | Author-reported | pp. 1–2 |
| Text injection ASR | 40 | % | GPT-4o base policy | Author-reported | Fig. 4A, p. 7 |
| Captioner adversarial influence | 92 | % | White-box captioner attack | Author-reported | Fig. 4B, p. 7 |
| Captioner-attack final ASR | 31 | % | GPT-4o + captioner | Author-reported | Fig. 4B, p. 7 |
| Self-caption influence | 38 | % | CLIP transfer | Author-reported | Fig. 4C, p. 7 |
| Self-caption final ASR | 19 | % | CLIP transfer | Author-reported | Fig. 4C, p. 7 |
| Base screenshot CLIP ASR | 10 | % | Trigger under 5% of pixels | Author-reported | Fig. 4D, pp. 7–8 |
| Clean evaluator final ASR | 25 | % | Policy attacked | Author-reported | Fig. 5C, p. 8 |
| Evaluator-only ASR | 8 | % | Policy uncompromised | Author-reported | Fig. 5B, p. 9 |
| Joint policy/evaluator ASR | 36 | % | Both attacked | Author-reported | Fig. 5D, p. 8 |
| Clean evaluator reduction | 6 pp; 19.4% relative | percentage points; % | \(31\%\rightarrow25\%\) | Analyst-derived | Fig. 5A/C |
| Clean value-function ASR | 26 | % | Policy attacked | Author-reported | Fig. 6C, p. 9 |
| Value-only ASR | 8 | % | Policy clean | Author-reported | Fig. 6B, p. 9 |
| Joint policy/value ASR | 38 | % | Both attacked | Author-reported | Fig. 6D, p. 9 |
| Joint value relative increase | 22.6 | % | \((38-31)/31\) | Analyst-derived | Fig. 6A/D |
| Paraphrase ASR | 27.5 | % | Baseline is 31% | Author-reported | p. 10, §5.4 |
| Pages with >10 images | 70 | % | Evaluated webpages | Author-reported | p. 10 |
| Tree-search branching/depth | 3 / 1 | actions / level | Tree-search configuration | Author-reported | p. 9 |
| Reflexion attempts | 2 | attempts maximum | Evaluator experiment | Author-reported | p. 8 |
| Temperature | 0 | decoding temperature | All tested LMs | Author-reported | p. 16 |
| CLIP optimization resolution | 180 | pixels | Selected attack setting | Author-reported | pp. 7, 21 |
| Full CLIP targeted-caption success | 71 | % | Ensemble + negative text | Author-reported | Table 7, p. 21 |
| Without negative text | 46 | % | CLIP ablation | Author-reported | Table 7 |
| Best single CLIP model | 31 | % | ViT-L/14@336px | Author-reported | Table 7 |
| Synthetic screenshot ASR range | 13–55 | % | Table 3 conditions | Author-reported | Table 3, p. 8 |
| Captioner strings exact successes | 11 of 12 visible | examples | Table 6 | Analyst-derived from visually readable marks | p. 19 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Restricted environmental attacks can hijack agents | Up to 67% ASR with one text/image trigger | X1–X4 | pp. 1–2, 7–8 | Strong existence evidence; exact 67% condition not fully tabulated |
| Captioners expose image attacks at a text-like interface | 92% adversarial captions, 31% final ASR | Fig. 4B | p. 7 | Direct experimental support |
| CLIP attacks transfer to black-box LMs | 38% adversarial self-captions; 19% final ASR | Fig. 4C | p. 7 | Supported in evaluated models/settings |
| Embedding a trigger in a screenshot makes transfer harder | 10% direct screenshot ASR; Table 3 size/text pattern | Fig. 4D, Table 3 | pp. 8, 21 | Supported; synthetic analysis isolates only two factors |
| A clean evaluator improves robustness | 31% to 25% | Fig. 5A/C | p. 8 | Supported directionally; reported relative percentage is inconsistent |
| An attacked evaluator can worsen reflexion | 36% versus 31% base | Fig. 5D | p. 8 | Supported in two-attempt GPT-4o configuration |
| An evaluator alone creates a vulnerability | 8% ASR with clean policy | Fig. 5B | p. 9 | Supported under simulated attacked-caption input |
| A clean value function improves robustness | 31% to 26% | Fig. 6C | p. 9 | Supported in depth-1, branch-3 search |
| An attacked value function worsens tree search | 38% versus 31% base | Fig. 6D | p. 9 | Supported in evaluated configuration |
| More exploration can expose attacks | Value-only attack yields 8% ASR | Fig. 6B | p. 9 | Plausible mechanism plus experiment; broader scaling untested |
| Prompt defenses provide limited gains | Safety and abstention prompts do not beat baseline | Fig. 7 | p. 10 | Supported visually/textually; exact bar values unlabeled |
| Paraphrasing helps only modestly | 31% to 27.5% | Fig. 7 | p. 10 | Small difference; no statistical uncertainty |
| Consistency checking can block the captioner attack | Near-zero ASR | Fig. 7 | p. 10 | Attack-specific; costly and itself attackable |
| Low-resolution optimization improves transfer | Strongest heatmap row at 180 px | Fig. 13 | p. 21 | Direction clear; exact cell values unavailable |
| Negative text and ensembling matter | 71% full versus 46% without negative text and 9–31% single models | Table 7 | p. 21 | Strong ablation pattern; no error estimates |

# 22. Very Simple Explanation

Imagine you ask a computer assistant to shop on a website. A dishonest seller cannot change your request or rewrite the assistant, but can change one product description or slightly alter one product photo. This paper shows that such a small change can sometimes trick the assistant into following the seller’s hidden goal.

Modern assistants often have several “workers”: one describes images, another chooses actions, another checks the work, and another scores possible actions. The researchers drew these workers as a graph and measured how much malicious influence passes from one worker to the next.

Extra checking can help if the checker sees clean information. But if the malicious content also fools the checker, the checker may confidently approve the wrong action or tell the assistant to retry in an even more harmful way. The same problem applies to search: exploring more choices helps only when the scoring system is trustworthy.

The practical lesson is that making an agent smarter or giving it more reasoning steps does not automatically make it safer. Security must be tested at every connection between components and against attackers who adapt to whatever defenses are added.

# Completeness Audit

## Inventory

- **Title:** *Dissecting Adversarial Robustness of Multimodal LM Agents*
- **Authors:** Chen Henry Wu, Rishi Shah, Jing Yu Koh, Ruslan Salakhutdinov, Daniel Fried, and Aditi Raghunathan.
- **Venue:** Published as a conference paper at ICLR 2025.
- **Document type:** Empirical AI/cybersecurity study with benchmark, attack-method, and evaluation-framework contributions.
- **Main sections:** Abstract; §§1–6; acknowledgments; references.
- **Appendices:** A Evaluation Details; B Experimental Details; C Additional Results; D Limitations and Broader Impact.
- **Figures:** 1–13.
- **Tables:** 1–7.
- **Major equations:** ARE edge-weight definition; Eqs. (1)–(2).
- **Algorithms:** No formal pseudocode or numbered algorithms.
- **Distinct analyses:** X1–X11 as registered in §8 above.
- **Explicit hypotheses:** No formal study hypotheses; two attack-design hypotheses in Appendix C.
- **Keywords:** No keyword list supplied.
- **Substantive footnotes/endnotes:** None detected.
- **Separate supplement:** None supplied.

## Coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes | Yes | Fully represented | Headline task count, attacks, ARE, 67%, and inference-time risks included. |
| §1 Introduction | Yes | Yes | Fully represented | Problem, gap, findings, and three contributions covered. |
| §2 Related Work | Yes | Yes | Represented in compressed form | Three literature categories and author positioning retained; citation-by-citation listing omitted. |
| §3.1 Threat Model | Yes | Yes | Fully represented | Capabilities, exclusions, trusted/untrusted split covered. |
| §3.2 Agent Graph | Yes | Yes | Fully represented | Nodes, edges, finish node, and configurations covered. |
| §3.3 Attack Propagation | Yes | Yes | Fully represented | AdvIn, \(\lambda\), upper-bound interpretation, and branching covered. |
| §4.1 Task Curation | Yes | Yes | Fully represented | Four components and four curation steps covered. |
| §4.2 Attacker Access | Yes | Yes | Fully represented | Text/image limits and platform model covered. |
| §4.3 Attack Methods | Yes | Yes | Fully represented | All three attacks and both optimization equations covered. |
| §5.1 Policy Robustness | Yes | Yes | Fully represented | Four settings and trade-off discussion covered. |
| §5.2 Evaluators | Yes | Yes | Fully represented | Clean, evaluator-only, and joint cases covered. |
| §5.3 Value Functions | Yes | Yes | Fully represented | Clean, value-only, and joint cases covered. |
| §5.4 Defenses | Yes | Yes | Fully represented | Prompting, abstention, paraphrase, consistency, hierarchy covered. |
| §6 Conclusions | Yes | Yes | Fully represented | Main implications and future directions included. |
| Acknowledgments | Yes | Minimally | Inspected but deliberately omitted as non-substantive | Funding and thanks do not affect methods/results. |
| References | Yes as supplied text | Categorically | Represented in compressed form | Individual bibliographic entries not reproduced. |
| Appendix A.1 | Yes | Yes | Fully represented | Full template categories summarized. |
| Appendix A.2 | Yes | Yes | Fully represented | Evaluation primitives and examples covered. |
| Appendix B.1 | Yes | Yes | Fully represented | Models, endpoints, temperature, and agent examples covered. |
| Appendix B.2 | Yes | Yes | Fully represented | Hardware/API information covered. |
| Appendix B.3 | Yes | Yes | Represented in compressed form | Representative strings and success-mark count retained. |
| Appendix B.4 | Yes | Yes | Fully represented | Both available prompt principles included; omitted examples acknowledged. |
| Appendix C.1 | Yes | Yes | Fully represented | Resolution, negative-text, and ensemble ablations covered. |
| Appendix C.2 | Yes | Yes | Fully represented | Synthetic experiment design and Table 3 results covered. |
| Appendix D | Yes | Yes | Fully represented | All three stated limitations and broader-impact claims covered. |
| Figures 1–3 | Yes, visually | Yes | Fully represented | Schematics and edge values explained. |
| Figure 4 | Yes, visually/textually | Yes | Fully represented with uncertainty | Scatter coordinates mostly unreadable; panel values covered. |
| Figures 5–7 | Yes, visually/textually | Yes | Fully represented | Edge values and defense trends covered. |
| Figures 8–12 | Yes, visually | Yes | Fully represented | Agent inputs, flows, and synthetic setup explained. |
| Figure 13 | Yes, visually/textually | Yes | Fully represented with uncertainty | Trend readable; exact heatmap cells unlabeled. |
| Tables 1–4 | Yes | Yes | Fully represented | Definitions, taxonomy, generalization, templates covered. |
| Tables 5–6 | Yes | Yes | Represented in compressed form | Long strings summarized rather than repeated verbatim. |
| Table 7 | Yes | Yes | Fully represented | Every numeric row included. |
| ARE equation | Yes | Yes | Fully represented | All important symbols and role explained. |
| Equations (1)–(2) | Yes | Yes | Fully represented | Objectives, constraints, encoders, and purpose explained. |
| Formal algorithms | Not applicable | Yes | No such item | Procedures exist, but no pseudocode block. |
| Major contributions | Yes | Yes | Fully represented | Conceptual, dataset, attack, empirical, implementation. |
| Author-stated limitations | Yes | Yes | Fully represented | All three Appendix D limitations included. |
| Supplied supplementary material | Not applicable | Yes | Missing from supplied material | No separate supplement was provided. |

## Missing or inaccessible material

- No separate supplementary files were supplied.
- The external code/data repository was not inspected.
- System prompts and few-shot examples for Figures 9–11 were omitted by the authors.
- Worked examples inside the two safety-prompt bullets were omitted by the authors.
- Pages 11–13 and 22 were available as text but not visually rendered.
- Exact Figure 4 scatterplot coordinates and Figure 13 heatmap-cell values are not labeled/readable.
- Several reproducibility details—PGD iterations, step size, seeds, run counts, task allocation, and uncertainty estimates—are not specified.

## Uncertain interpretations

- The displayed 31%→25% evaluator result conflicts with the introduction’s 23% relative-reduction wording.
- The displayed 31%→36% and 31%→38% changes do not exactly equal the summarized 15%/20% or 20% relative increases.
- The exact experimental condition producing the headline 67% ASR is not fully tabulated in the supplied results.
- Table 6’s success count is based on twelve visually visible marked examples; the paper does not present this count as an aggregate statistic.
- Figure 7 does not label exact ASRs for the two prompt defenses or consistency defense.

## Deliberately compressed material

- The reference list was inspected but not reproduced citation by citation because it is bibliographic rather than primary evidence.
- Related work was synthesized into its three author-defined categories.
- Long adversarial prompt strings in Table 6 were summarized while retaining their types and checkmark outcomes.
- The acknowledgments were classified as non-substantive to the scientific findings.
- Repeated statements of the same headline findings across the abstract, introduction, results, conclusion, and Appendix D were consolidated.

## Potential omissions

No substantive section, subsection, experiment, figure, table, major equation, contribution, or author-stated limitation identified in the inventory is knowingly omitted. Items not fully represented verbatim are identified above as compressed, author-omitted, visually uncertain, or unavailable.