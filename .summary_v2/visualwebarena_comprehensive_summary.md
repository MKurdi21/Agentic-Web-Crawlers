# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Available range | All 25 pages, corresponding to proceedings pages 881–905 |
| Apparently missing pages | None |
| Native text | Available on every page; no page was classified as scanned or unusually low-text |
| Visually inspected pages | 23 of 25: pages 1–4, 6–10, and 12–25 |
| Pages not visually rendered | Pages 5 and 11; both are text-only in the supplied extraction, apart from no identified substantive figures or tables |
| Figures | Figures 1–17 were visually supplied and inspected |
| Tables | Tables 1–6 were visually supplied and readable |
| Equations/notation | The principal Partially Observable Markov Decision Process (POMDP), transition, reward, exact-match, and Structural Similarity Index Measure (SSIM) threshold expressions are readable. Minor typography remains OCR-sensitive |
| Appendices | Appendices A–F are present |
| Supplementary material | No separate supplementary file was supplied or explicitly detected |
| References | Present on pages 10–12; inspected through supplied text and compressed below |
| OCR needed | No. Native extraction was used; visual rendering was used to confirm tables, figures, and notation |
| Embedded visual material | Present and inspected through rendered pages, including site screenshots, trajectories, plots, diagrams, and prompt reproductions |
| Principal limitations | Small text within some embedded webpage screenshots is not independently readable in full. Their task labels, actions, captions, and methodological role are nevertheless readable from the figure and surrounding text. No external artifacts, benchmark code, task files, reward implementations, or model traces beyond those reproduced in the paper were supplied |

All statements below use only the supplied paper. Evidence labels are:

- **[A] Author-reported:** explicitly stated by the authors.
- **[B] Directly observable:** visible in a supplied table, plot, or diagram.
- **[C] Analyst-derived:** calculated from supplied values.
- **[D] Analyst interpretation:** a clearly marked inference rather than an author claim.

# 1. Plain-Language Orientation

VisualWebArena asks a practical question: can an artificial-intelligence agent use visually rich websites the way a person does—not merely read page text, but interpret pictures, colors, layouts, icons, and image-based instructions while clicking, typing, searching, and navigating? [A: abstract; pp. 1–2, §1]

The authors argue that earlier web-agent benchmarks emphasized text representations of webpages. That leaves out ordinary tasks such as identifying a green shirt, locating an exact photograph, reading text embedded in a product image, or selecting an item based on its visual position. VisualWebArena addresses this gap with **910 visually grounded tasks** in self-hosted Classifieds, Shopping, and Reddit environments. Some tasks also consult a self-hosted Wikipedia site, and **25.2% (229 tasks)** contain one or more input images. [A: pp. 1, 5, 9, 12, 14; §§1, 4.1–4.2, 6.1, App. A/C.3]

The researchers:

1. built or adapted reproducible websites;
2. created realistic tasks and task-specific binary evaluators;
3. compared text-only large language model (LLM) agents, caption-augmented agents, and vision-language model (VLM) agents;
4. introduced a **Set-of-Marks (SoM)** interface that places numbered boxes on interactive webpage elements;
5. measured human performance and analyzed task subsets, difficulty, trajectory length, and failure modes. [A: pp. 2–9, §§3–6]

The central empirical result is that vision helps but does not make these agents reliable. In the original main comparison, GPT-4V with SoM achieved **16.37%**, versus **15.05%** with screenshots plus an accessibility tree, **12.75%** for caption-augmented GPT-4, **7.25%** for text-only GPT-4, and **88.70%** for humans. A post-submission appendix reports **19.78%** for GPT-4o with SoM. [A/B: Tables 3 and 5, pp. 8, 13]

Thus the paper’s central contribution is not a high-performing web agent. It is a reproducible benchmark that exposes a large gap between successful demonstrations and dependable visually grounded web use, plus evidence that direct visual input and visually aligned element IDs can help.

# 2. Document Roadmap

| Part | Content and role |
|---|---|
| Abstract and §1, pp. 1–2 | Motivates visually grounded web agents and states the benchmark, evaluation, and SoM contributions |
| §2, pp. 2–3 | Positions the work relative to web-agent benchmarks, LLM agents, and VLMs |
| §3, pp. 3–5 | Defines the environment as a POMDP, its observations/actions, and binary evaluators |
| §4, pp. 5–7 | Describes the three web environments, task construction, difficulty labels, and human evaluation |
| §5, pp. 7–8 | Defines text-only, caption-augmented, multimodal, and SoM baselines |
| §6, pp. 7–9 | Reports primary results and task-subset analysis |
| §7, p. 9 | Summarizes the conclusions |
| §8, p. 9 | Discusses intended use, social impact, bias, and safety |
| References, pp. 10–12 | Prior literature; compressed as bibliographic rather than substantive experimental content |
| Appendix A, p. 12 | Task distributions by site and difficulty |
| Appendix B, p. 13 | Post-submission results for newer models |
| Appendix C, pp. 13–18 | Few-shot analysis, difficulty analysis, task subsets, trajectory lengths, failure modes, and qualitative agent comparisons |
| Appendix D, pp. 19, 22–23 | Classifieds data source, redaction, and interface |
| Appendix E, p. 19 | Expanded task-collection procedure |
| Appendix F, pp. 19–20, 24–25 | Viewports, truncation, sampling settings, system prompt, and in-context demonstrations |

# 3. Background and Context

A **web agent** is a model-driven system that receives a goal and observations of a browser, then issues actions such as clicking links or typing into fields. VisualWebArena evaluates the complete interaction rather than only asking questions about a screenshot. [A: §§1, 3]

A **large language model (LLM)** principally processes language. A **vision-language model (VLM)** accepts both images and text. A **caption-augmented agent** remains text-driven but receives automatically generated descriptions of page images. These alternatives let the study ask whether images themselves add information beyond text and captions. [A: §5]

An **accessibility tree** is a simplified structural representation of webpage content intended for assistive technologies. It identifies elements and text but may not fully express spatial relationships between nearby visual objects. A **web screenshot** preserves visual layout but, without grounding, the model must connect visible controls to executable actions. [A: pp. 3, 7–8, §§3.1, 5.3, 6]

**Set-of-Marks prompting** overlays a bounding box and unique integer ID on each interactive element. The agent can see the marked element and issue an action such as `click [31]`. This connects visual perception to a discrete action vocabulary and avoids requiring pixel-coordinate prediction. [A/B: pp. 3–4, Fig. 2, §§3.1–3.2]

The environment is treated as a **Partially Observable Markov Decision Process (POMDP)**: the true website state may be larger than the current page observation, and the agent acts using only what it currently sees plus the supplied interaction context. [A: p. 3, §3]

The benchmark uses **execution-based evaluation**. Success is determined by checking the final website state or answer, not by asking whether the agent’s prose sounds plausible. Each task produces a binary reward, 1 for success and 0 otherwise. [A: pp. 3–6, §3.3]

# 4. Research Problem and Gap

## Existing problem

Routine browser tasks combine natural-language instructions, visual perception, navigation, planning, and state-changing actions. Interfaces are designed for human vision, so important attributes may appear only in images or layout. [A: p. 1, §1]

## Shortcomings attributed to previous approaches

According to the authors:

- most existing benchmarks concentrated on text-based agents;
- accessibility trees and raw HTML omit or weaken some visual information;
- captions often preserve salient objects but lose fine-grained details;
- coordinate prediction tests low-level pointing ability in addition to higher-level reasoning;
- proof-of-concept visually grounded interfaces had not been systematically benchmarked in a realistic interactive environment. [A: pp. 1–3, 7–8, 17–19]

## Research gap

There was a lack of a reproducible benchmark combining realistic websites, visually grounded goals, multimodal inputs, long interactive trajectories, and execution-based scoring. [A: abstract; §§1, 3–4]

## Motivation

Such a benchmark can expose capabilities and failure modes hidden by text-only tasks and can guide development toward agents that interact with human-oriented interfaces. [A: §§1, 6–7]

## Scope

The work evaluates browser agents in self-contained replicas of Classifieds, Shopping, Reddit, and some cross-site/Wikipedia tasks. It does not demonstrate safe or reliable deployment on arbitrary live websites. [A: §§4.1, 8; App. A]

# 5. Research Questions / Objectives / Hypotheses

The paper does not state formally numbered research questions or preregistered hypotheses.

## Explicit objectives

- Introduce 910 realistic visually grounded tasks.
- Build a new Classifieds environment and reuse Shopping and Reddit environments from WebArena.
- Extend execution-based evaluation to open-ended visual objectives.
- Benchmark contemporary LLM and VLM agents.
- test whether image access and SoM grounding improve success.
- Analyze performance by site, task difficulty, Optical Character Recognition (OCR), exact image matching, image-input status, and trajectory behavior.
- Identify common agent failure modes. [A: pp. 1–2, 4–9, 12–18]

## Implicit empirical questions, reconstructed but not author-numbered

These are organizational paraphrases, not formal author-defined RQs:

- **RQ1:** How capable are current agents on realistic visually grounded web tasks?
- **RQ2:** Does adding captions or direct visual input improve over text-only agents?
- **RQ3:** Does SoM grounding improve navigability?
- **RQ4:** Which task properties and failure modes remain difficult?
- **RQ5:** How large is the agent–human performance gap?

## Hypotheses

No formal null or alternative hypotheses are supplied. The authors state expectations—not statistical hypotheses—that complementary visual information should improve performance and that SoM should simplify action grounding. [A: pp. 2, 7]

# 6. Assumptions / Threat Model

This is not a cybersecurity study and supplies no attacker threat model.

## System and environmental assumptions

- Websites are standalone and self-hosted to support reproducibility and deterministic state transitions. [A: p. 3, §3]
- Agents receive the task objective, current observation, URL, tabs, and previous action. SoM agents additionally receive marked screenshots and element descriptions. [A/B: Figs. 16–17]
- An action’s element ID must belong to the current observation. [A: §§3.1–3.2; Fig. 16]
- The environment transition function is deterministic given the state and action. [A: p. 3]
- Task success can be represented by a hand-designed binary evaluator. [A: §§3.3, 4.2]
- For the main baselines, three non-overlapping in-context examples—one per environment—are assumed sufficient to demonstrate the required interaction format. [A: pp. 7, 20]
- SoM deliberately abstracts away pixel-level pointing by giving the model valid element IDs. [A: p. 3, §3.2]
- Human-estimated action and visual difficulty are treated as useful ordinal labels, although the authors acknowledge judgment-based deviations. [A: p. 6, §4.2]

## Exclusions and boundaries

- Non-binary reward was not evaluated. [A: footnote 2, p. 4]
- The research prototypes are not intended for practical deployment, especially in high-risk settings. [A: p. 9, §8]
- The paper focuses on benchmark performance, not security against malicious webpages, prompt injection, privacy attacks, or adversarial users.

# 7. Methodology

## 7.1 Study design

This is a mixed **benchmark, systems, and empirical evaluation paper**. The authors construct environments and tasks, define executable evaluators, compare agent configurations, measure a human reference level, and perform quantitative and qualitative error analysis.

## 7.2 Environment model

The environment is:

\[
\mathcal{E}=(\mathcal{S},\mathcal{A},\Omega,T)
\]

where \(\mathcal{S}\) is the state set, \(\mathcal{A}\) the action set, \(\Omega\) the observation set, and \(T:\mathcal{S}\times\mathcal{A}\rightarrow\mathcal{S}\) the deterministic transition function. At step \(t\), the agent observes \(o_t\in\Omega\), chooses \(a_t\in\mathcal{A}\), and reaches \(s_{t+1}\) with observation \(o_{t+1}\). [A: p. 3, §3]

Observations can use:

1. raw HyperText Markup Language (HTML)/Document Object Model (DOM);
2. accessibility trees;
3. RGB screenshots;
4. SoM screenshots and textual element listings. [A: p. 3, §3.1]

## 7.3 Action space

Table 1 defines:

- element interaction: `click`, `hover`, `type`;
- keyboard interaction: `press`;
- tab operations: `new_tab`, `tab_focus`, `tab_close`;
- navigation: `goto`, `go_back`, `go_forward`;
- scrolling: `scroll [up|down]`;
- completion: `stop [answer]`. [A/B: Table 1, p. 3]

## 7.4 Websites and data

### Classifieds

A new OSClass-based site contains **65,955 listings**, each with a title, description, and product image. The authors scraped Craigslist categories over **three weeks**, focusing on the northeastern United States. The `scrubadub` Python package removed personally identifiable information; names, emails, and phone numbers were replaced with fictitious values, including 555-prefix numbers. [A: pp. 5, 19; §4.1, App. D]

### Shopping

Inherited from WebArena, with product information scraped from Amazon and released through WebShop. [A: p. 5, §4.1]

### Reddit

Inherited from WebArena and containing **31,464 image-bearing posts** across varied forums. [A: p. 5, §4.1]

### Other sites

Some tasks reference a self-hosted Wikipedia knowledge base; **4.9%** are categorized as multi-site. [A/B: p. 12, Fig. 4, App. A]

## 7.5 Task construction

Six computer-science graduate students, all co-authors, created tasks. They first explored the sites, then wrote templates and instantiated them with different arguments. The final benchmark contains:

- **910 tasks**;
- **314 unique templates**;
- an average of **2.9 tasks per template**;
- **46 unachievable tasks (5.1%)**;
- input images drawn from royalty-free/attribution-free sources and MS-COCO;
- hand-authored reward functions. [A: pp. 5, 19; §4.2, App. E]

The authors report preventing exact task repetition and limiting excessive concentration of one task type. No formal inter-annotator agreement, independent validation panel, or template-wise train/test split is described.

## 7.6 Difficulty taxonomy

Action difficulty:

- easy: at most 3 actions;
- medium: 4–9 actions;
- hard: at least 10 actions.

Visual difficulty:

- easy: colors, shapes, broad object recognition;
- medium: patterns, semantic interpretation, or short large-text OCR;
- hard: multiple images, small/long OCR, or fine details.

Overall difficulty averages visual and reasoning/action complexity, with possible human-judgment deviations. [A: p. 6, §4.2]

## 7.7 Human evaluation

Seven college students completed a sample of **230 tasks**, one per template where sampled. Some had created tasks, but none were assigned tasks they themselves created. Success was **88.70% overall**. [A/B: pp. 6, 8; §4.3, Table 3]

## 7.8 Agent families

- **Text-only:** LLaMA-2-70B, Mixtral-8x7B, Gemini-Pro, GPT-3.5, GPT-4; accessibility-tree input and chain-of-thought prompting.
- **Caption-augmented:** accessibility trees enriched with BLIP-2-T5XL or LLaVA-7B captions.
- **Multimodal:** IDEFICS-80B-Instruct, CogVLM, Gemini-Pro, GPT-4V; screenshots, captions, and accessibility trees.
- **Multimodal SoM:** the same general multimodal setup, replacing the accessibility-tree action interface with screenshots containing marked interactive elements and corresponding textual SoM records.
- **Post-submission:** Llama-3-70B-Instruct with captions, Gemini Flash 1.5, Gemini Pro 1.5, and GPT-4o with SoM. [A: §§5.1–5.3; App. B]

## 7.9 Evaluation functions

The benchmark uses task-specific combinations of:

- `exact_match`;
- `must_include`;
- `must_exclude`;
- LLM-judged `fuzzy_match`;
- VLM-based `eval_vqa`;
- SSIM-based `eval_fuzzy_image_match`;
- URL and page-element locators that inspect the final state. [A: pp. 4–6, §3.3, Table 2]

`fuzzy_match` uses GPT-4-Turbo and assigns 1 only to “correct,” not “partially correct.” `eval_vqa` uses BLIP-2-T5XL and assigns 1 when its response contains the expected answer. [A: p. 4]

## 7.10 Experimental settings

For normal-context baselines:

- viewport: **1280 × 2048**;
- text truncation: **3,840 tokens**, or **15,360 characters for Gemini**.

For LLaMA, IDEFICS, and CogVLM:

- viewport: **1280 × 720**;
- truncation: **640 tokens**.

Sampling:

- GPT-3.5/GPT-4: temperature **1.0**, top-p **0.9**;
- Gemini: temperature **0.9**, top-p **1.0**;
- other models: temperature **0.6**, top-p **0.95**;
- nucleus sampling for all experiments.

All main baselines receive three in-context examples. Hardware, random seeds, number of repeated runs, confidence intervals, and statistical hypothesis tests are not reported. [A: pp. 19–20, App. F]

# 8. Experiments / Analyses

## X1 — Main baseline comparison

**Purpose:** Compare text-only, caption-augmented, direct multimodal, and SoM agents.

**Setup:** 910-task benchmark; success rate by site and overall; three in-context examples.  
**Metric:** binary task success averaged as a percentage.  
**Evidence:** Table 3, p. 8.

Main outcomes:

- best text-only: GPT-4, **7.25%**;
- best caption-augmented: GPT-4 + BLIP-2, **12.75%**;
- best direct multimodal/accessibility-tree: GPT-4V, **15.05%**;
- best original SoM: GPT-4V + SoM, **16.37%**;
- humans: **88.70%**.

No uncertainty intervals or significance tests are provided.

## X2 — Human reference performance

**Purpose:** Establish whether the tasks are generally solvable by people.

Seven students attempted 230 tasks. Overall success was **88.70%**, with Classifieds **91.07%**, Reddit **87.10%**, and Shopping **88.39%**. The authors attribute many human failures to instruction errors, incomplete exhaustive search, or giving up after 5–10 minutes. [A/B: pp. 6, 8; §4.3, Table 3]

Caveat: this is a sampled subset rather than all 910 tasks, and some participants were task creators.

## X3 — SoM comparison

For GPT-4V, SoM changed:

- Classifieds: **8.12% → 9.83%**;
- Reddit: **12.38% → 17.14%**;
- Shopping: **19.74% → 19.31%**;
- overall: **15.05% → 16.37%**. [B: Table 3]

The prose on p. 8 reverses the Classifieds and Reddit starting values when it says “12.38% → 17.14% and 8.12% → 9.83% respectively.” Table 3 shows that **12.38→17.14 is Reddit**, while **8.12→9.83 is Classifieds**. This is a **text–table inconsistency**.

SoM did not help every model: Gemini-Pro fell from 6.04% to 5.71%, CogVLM remained at 0.33%, and IDEFICS rose only from 0.77% to 0.99%. [B: Table 3]

## X4 — Task-property subsets

GPT-4V + SoM results:

| Subset | Share | Success |
|---|---:|---:|
| OCR required | 17.1% | 13.4% |
| No OCR | 82.9% | 16.9% |
| Exact image match | 8.7% | 18.9% |
| No exact match | 91.3% | 16.2% |
| Image input | 25.2% | 19.0% |
| No image input | 74.8% | 14.9% |

[A/B: Table 4, p. 9]

The comparison is observational; task subsets differ in other properties, so these differences do not isolate causal effects.

## X5 — Difficulty analysis

Figure 6 cross-tabulates action and visual difficulty for three GPT-4 configurations and gives GPT-4V + SoM trajectory lengths. Success generally declines as difficulty rises. On hard visual tasks:

- GPT-4 text-only: **4.8%**;
- GPT-4 + captions: **8.0%**;
- GPT-4V + SoM: **12.4%**. [A/B: pp. 13–14, Fig. 6]

GPT-4V + SoM’s trajectory length increases from **6.9** for easy-action tasks to **10.0** for medium and **12.1** for hard. [B: Fig. 6d]

## X6 — Few-shot prompting

Gemini-Pro with screenshot + captions + accessibility tree was tested with 0, 1, and 3 examples:

- 0 examples: **2.86%** overall;
- 1 example: **3.63%**;
- 3 examples: **6.04%**. [A/B: Table 6, p. 13]

The authors infer that training on web trajectories may help. Fine-tuning itself was not tested.

## X7 — Post-submission models

Table 5 reports:

- Llama-3-70B-Instruct + captions: **9.78%**;
- Gemini Flash 1.5 + SoM: **6.59%**;
- Gemini Pro 1.5 + SoM: **11.98%**;
- GPT-4o + SoM: **19.78%**. [A/B: p. 13, App. B]

This makes 19.78%, not 16.37%, the highest agent result anywhere in the final paper. The abstract/main contribution language retains the earlier rounded “16.4%,” apparently reflecting the original experiment set.

## X8 — Trajectory-length analysis

Figure 10 groups GPT-4V + SoM trajectories by length. Most attempts terminate before 10 steps, while failure remains dominant across every length bin. Displayed success shares are **22.0%, 11.4%, 16.0%, 14.7%, 10.8%, 21.1%, and 9.9%** for successive bins. [B: Fig. 10]

The plot is descriptive; it does not establish that longer trajectories cause failure.

## X9 — Qualitative failure analysis

The authors identify:

- correct work later undone;
- failures on apparently easy tasks;
- premature termination;
- loops between pages or tabs;
- unnecessary actions;
- appending instead of replacing field contents;
- repeated actions until the trajectory cap;
- loss of fine details in captions;
- poor long-horizon state tracking. [A: pp. 15–18, App. C.4–C.5]

# 9. Results

## Finding 1 — A very large human–agent gap remains

GPT-4V + SoM achieved **16.37%**, while humans achieved **88.70%**. [B: Table 3]

- Absolute gap: **72.33 percentage points** [C: \(88.70-16.37\)].
- Human success was about **5.42 times** the GPT-4V + SoM rate [C: \(88.70/16.37\)].

Using the later GPT-4o result, the gap remains **68.92 percentage points** [C: \(88.70-19.78\)], though the human and model conditions are not perfectly identical because humans used a 230-task sample.

## Finding 2 — Visual information helps GPT-4-family agents

GPT-4 improved from **7.25% text-only** to **12.75% with captions**. This is:

- **+5.50 percentage points** [C];
- approximately **75.9% relative improvement** [C: \(5.50/7.25\)].

GPT-4V with screenshot + captions + accessibility tree reached **15.05%**, another **2.30 percentage points** beyond caption-augmented GPT-4. [B/C: Table 3]

## Finding 3 — SoM helps GPT-4V modestly overall and substantially on Reddit

SoM raised GPT-4V from **15.05% to 16.37%** overall:

- **+1.32 percentage points** [C];
- approximately **8.8% relative improvement** [C].

Its largest site gain was Reddit, **12.38% to 17.14%**, or **+4.76 points**. Shopping declined by **0.43 points**. [B/C: Table 3]

Therefore the evidence supports a model- and site-dependent benefit, not a universal SoM improvement.

## Finding 4 — Stronger later models improve but remain unreliable

GPT-4o + SoM achieved **19.78%**, **3.41 percentage points** above GPT-4V + SoM. [A/B/C: Table 5 versus Table 3] It still failed roughly four out of five tasks.

## Finding 5 — OCR is difficult for GPT-4V + SoM

OCR-required tasks had **13.4%** success versus **16.9%** without OCR, a **3.5-point deficit**. [B/C: Table 4]

Appendix C reports that direct multimodality improves GPT-4-family OCR performance from roughly **6.4% to 12.2%** relative to captioning, while Gemini configurations show a different pattern. [A/B: p. 14, Fig. 7]

## Finding 6 — Exact-image matching is not the main GPT-4V + SoM bottleneck

GPT-4V + SoM scored **18.9%** on exact-match tasks and **16.2%** otherwise, a **2.7-point advantage** for the exact-match subset. [B/C: Table 4] Other agents, especially Gemini configurations, often did worse on exact-match tasks, so this conclusion is configuration-specific. [A/B: pp. 14, 16, Fig. 8]

## Finding 7 — Image-input tasks can be easier once the images are understood

GPT-4V + SoM scored **19.0%** when the objective included an image and **14.9%** otherwise, a **4.1-point difference**. [B/C: Table 4] GPT-4 captioned and multimodal variants generally shared this direction; Gemini-Pro variants generally did not. [A/B: pp. 14, 17, Fig. 9]

## Finding 8 — More in-context demonstrations correspond to better Gemini-Pro performance

Overall success rose from **2.86%** with no examples to **3.63%** with one and **6.04%** with three. [B: Table 6] This supports the usefulness of demonstrations in this setting but does not directly establish the benefit of fine-tuning.

# 10. Figure-by-Figure Interpretation

## Figure 1 — Benchmark overview

A left-to-right workflow connects VisualWebArena’s sites and knowledge tools, example task specifications/webpages, and an LLM/VLM agent producing an element-ID action. It establishes that tasks combine language, webpage images, navigation, and executable actions. There are no quantitative axes. [B: p. 2]

## Figure 2 — Set-of-Marks interface

The original Reddit page is transformed into a screenshot whose interactive controls have colored boxes and numeric IDs. A corresponding text list names elements such as comments, sorting controls, images, and users. The agent can issue `click [31]`. This diagram shows how perception and action grounding share the same identifiers. [B: p. 4]

## Figure 3 — Successful Reddit trajectory

A seven-state sequence shows GPT-4V + SoM searching for `/f/memes`, using the forum list after the initial route fails, identifying the target image’s author, and blocking that user. Red labels are agent-issued commands. It supports the qualitative claim that an SoM agent can recover from an unsuccessful search and ground an exact image to the correct interaction target. [A/B: p. 8]

## Figure 4 — Tasks by site

Pie chart:

- Shopping: **50.9%**;
- Classifieds: **25.5%**;
- Reddit: **18.7%**;
- multi-site: **4.9%**.

The percentages total 100%. [B: p. 12]

## Figure 5 — Joint task-difficulty distribution

A 3×3 bubble matrix crosses visual difficulty (easy/medium/hard) with action difficulty (easy/medium/hard). Cell shares are:

| Action \ Visual | Easy | Medium | Hard |
|---|---:|---:|---:|
| Easy | 15.7% | 12.9% | 4.2% |
| Medium | 13.7% | 12.6% | 8.5% |
| Hard | 7.0% | 10.5% | 14.8% |

[B: p. 12]

The largest cell is easy/easy at 15.7%, closely followed by hard/hard at 14.8%, showing broad rather than single-level coverage.

## Figure 6 — Difficulty-conditioned performance and trajectory length

Four heatmaps cross action and visual difficulty:

- panel (a): GPT-4 text-only success;
- panel (b): GPT-4 + captions success;
- panel (c): GPT-4V + SoM success;
- panel (d): GPT-4V + SoM mean trajectory length.

No error bars are shown. GPT-4V + SoM is strongest in every displayed difficulty cell relative to the other GPT-4 variants. Its easiest action/easy visual cell reaches **30.1%**; its hard action/hard visual cell is **8.9%**. Trajectories generally lengthen with action difficulty. [B: p. 14]

## Figure 7 — OCR versus non-OCR tasks

A grouped bar chart compares eight Gemini-Pro and GPT-4 configurations. The horizontal axis is agent configuration; the vertical axis is success rate; coral represents no OCR and teal OCR. Exact bar labels are absent, so values beyond those stated in prose or Table 4 are visually approximate. The author-highlighted comparison is GPT-4 captioned versus multimodal OCR performance, approximately **6.4% to 12.2%**. [A/B: pp. 14–15]

## Figure 8 — Exact-image-match subsets

A grouped bar chart contrasts exact-match and no-match tasks across the same agent families. GPT-4V + SoM’s exact-match bar is highest among its pair, consistent with Table 4’s **18.9% versus 16.2%**. Several other configurations show the reverse. Bars without text labels should be treated as approximate visual readings. [A/B: pp. 14, 16]

## Figure 9 — Image-input versus text-only specifications

Grouped bars compare tasks with at least one input image against tasks without one. GPT-4’s captioned, multimodal, and SoM variants tend to score higher with image inputs; Gemini-Pro variants tend to score lower. Table 4 supplies exact GPT-4V + SoM values of **19.0% versus 14.9%**. [A/B: pp. 14, 17]

## Figure 10 — Trajectory length and outcomes

The upper histogram shows pass/fail counts by trajectory-length bin; the lower normalized chart shows within-bin outcome shares. Failures dominate all bins. Success percentages shown are 22.0, 11.4, 16.0, 14.7, 10.8, 21.1, and 9.9. Exact bin boundaries are visually indicated along a 0–35-step axis but are not exhaustively spelled out in the prose. [B: p. 18]

## Figure 11 — Easy-task shopping page

A Shopping search-results page contains multiple textiles and household items. The required red item is in the second row. The figure illustrates an easy task that all tested agents failed, with GPT-4V variants choosing a blue tablecloth in the first row. [A/B: pp. 15, 18]

## Figure 12 — Failed phone-number trajectory

The diagram follows a multimodal GPT-4V agent from the Shopping account page to an address form and a Wikipedia country-code map. It unnecessarily creates a blank tab, later appends `+826505551212` rather than replacing the prior number, submits, and repeats. It illustrates wasted actions, incorrect field editing, and looping. [A/B: pp. 16–17, 19]

## Figure 13 — Successful Classifieds SoM trajectory

A nine-state sequence shows search for a white Google Pixel, category filtering, list view, selection of the latest relevant result, and posting a **$250** offer—$10 below the displayed asking price implied by the task trace. Step 6 redundantly retypes the title, but the task succeeds. [A/B: pp. 18, 21]

## Figure 14 — Classifieds homepage

The screenshot displays keyword search, category filtering, latest listings, categories, and locations. It documents the benchmark’s interface and visual density rather than reporting an experimental result. [B: p. 22]

## Figure 15 — Classifieds detail page

The page contains title, price, date/location, product image, seller panel, related listings, rating, comment title/body fields, and a send button. It demonstrates the stateful actions available to agents. [B: p. 23]

## Figure 16 — SoM system message

This full-page prompt defines observations, element IDs, action syntax, tab/navigation commands, the homepage/password resource, one-action-at-a-time behavior, and the required output format. It is methodological evidence for how the agent was instructed. [A/B: p. 24]

## Figure 17 — In-context examples

Three demonstrations cover:

1. answering a product-price question with `stop [$279.49]`;
2. clicking into a Reddit comments section;
3. searching Classifieds for a guitar.

The caption says SoM screenshots were appended to each example-user turn. The reproduced second example appears internally questionable: the croissant post’s comment link is `[16]`, while the example action shown is `click [11]`, associated with the earlier pumpkin post. This is a **prompt-example inconsistency visible in the supplied figure/text**. [B: p. 25]

# 11. Table-by-Table Interpretation

## Table 1 — Available actions

Rows enumerate 12 action types and their meanings. Arguments are element IDs, text, key combinations, tab indexes, URLs, scroll direction, or final answers. It defines the executable interface but contains no outcome statistics. [A/B: p. 3]

## Table 2 — Examples of task-specific evaluators

Four tasks demonstrate combinations of URL checks, locators, inclusion/exclusion rules, visual question answering, and fuzzy image matching. The table shows why one universal exact-match metric would be insufficient for open-ended state-changing tasks. [A/B: p. 6]

No threshold value is given for the displayed SSIM-based example; §3.3 merely defines a task-specific \(t\in[0,1]\).

## Table 3 — Main baseline and human success rates

This is the principal result table. Rows are grouped into text-only, caption-augmented, multimodal/accessibility-tree, multimodal/SoM, and human conditions. Columns report Classifieds, Reddit, Shopping, and overall success.

Important extremes:

- weakest overall: CogVLM, **0.33%** in both multimodal interfaces;
- strongest original model: GPT-4V + SoM, **16.37%**;
- human: **88.70%**;
- highest site-specific model result: GPT-4V multimodal on Shopping, **19.74%**, slightly above its SoM Shopping result of 19.31%;
- highest captioned result: GPT-4 + BLIP-2, **12.75%**.

No standard errors, confidence intervals, or significance markers appear. [B: p. 8]

## Table 4 — GPT-4V + SoM task subsets

Rows compare OCR/no OCR, exact/no exact image match, and image/no image input. Columns give benchmark share and success rate. It supports capability diagnosis but not causal attribution because subsets were not randomized. [A/B: p. 9]

## Table 5 — Later model results

GPT-4o + SoM leads at **19.78% overall**, and is around 20% on all three sites. Llama-3-70B + captions reaches **9.78%**, much higher than Llama-2-70B + captions in Table 3 (**0.66%**), though these are distinct model generations rather than a controlled single-factor ablation. [A/B: p. 13]

## Table 6 — Number of in-context examples

Gemini-Pro’s overall result increases monotonically from 0 to 3 examples. Site-level behavior is not fully monotonic: Reddit falls from **2.38% at zero examples to 1.43% at one**, then rises to **4.29% at three**; Shopping increases from **0.43% to 2.14%**, then **3.42%**. [B: p. 13]

# 12. Diagram / Architecture Interpretation

The paper’s core architecture can be summarized as:

\[
\text{task objective + webpage observation}
\rightarrow
\text{LLM/VLM reasoning}
\rightarrow
\text{discrete browser action}
\rightarrow
\text{new webpage state}
\rightarrow \cdots \rightarrow
\text{task evaluator}.
\]

[A/D synthesis from §§3, 5 and Figs. 1–3]

For SoM:

1. JavaScript detects every interactive webpage element.
2. Each element receives a bounding box and unique ID.
3. The annotated screenshot preserves location and appearance.
4. A text listing supplies ID, tag type, and available text/caption.
5. The VLM selects an action referring to that ID.
6. The browser executes the command.
7. The page is observed again and the loop repeats.
8. A task-specific evaluator checks the final state or returned answer. [A/B: Fig. 2; §§3.1–3.3, 5.3]

This interface moves low-level control from coordinate generation to element selection. It does not remove the need for perception, search, planning, memory, or judgment about task completion.

# 13. Equations and Mathematical Concepts

## E1 — Environment definition

\[
\mathcal{E}=(\mathcal{S},\mathcal{A},\Omega,T)
\]

This is a POMDP-style environment. \(\mathcal{S}\) is the set of states, \(\mathcal{A}\) actions, \(\Omega\) observations, and \(T\) transitions. [A: p. 3]

## E2 — Transition function

\[
T:\mathcal{S}\times\mathcal{A}\rightarrow\mathcal{S}
\]

Given a state and action, the environment deterministically produces the next state. At time \(t\), \(a_t\) is conditioned on the partial observation \(o_t\), and the result is \(s_{t+1}\) and \(o_{t+1}\). [A: p. 3]

## E3 — Binary reward

\[
R:\mathcal{S}\times\mathcal{A}\rightarrow\{0,1\}
\]

The final execution receives 1 when the resulting state/actions satisfy the objective and 0 otherwise. Although written as state–action reward notation, practical evaluators may examine final URLs, text, images, and page elements. [A: pp. 3–6]

## E4 — Exact match

\[
\mathbf{1}\{\hat a=a^\*\}
\]

Here \(\hat a\) is the agent’s output and \(a^\*\) the ground truth. The indicator returns 1 only for exact equality. [A: p. 4]

## E5 — Inclusion and exclusion predicates

`must_include` returns 1 when all required members of \(a^\*\) occur in \(\hat a\). `must_exclude` returns 1 only when none of the prohibited members occurs. These are logical predicates rather than continuously valued metrics. [A: p. 4]

## E6 — Semantic and visual evaluators

`fuzzy_match` delegates semantic equivalence to GPT-4-Turbo. `eval_vqa` delegates an image question to BLIP-2-T5XL and checks whether the expected answer appears. These introduce learned models into the evaluation pipeline. [A: p. 4]

## E7 — SSIM threshold

For `eval_fuzzy_image_match`, reward is 1 if:

\[
\operatorname{SSIM}(I_q,I^\*) > t,\qquad t\in[0,1].
\]

\(I_q\) is the query/result image, \(I^\*\) the ground-truth image, and \(t\) a threshold. The paper does not report the actual thresholds used by individual tasks. [A: p. 5]

No theorem, lemma, proof, optimization loss, or training equation is presented.

# 14. Interpretation and Discussion

The benchmark shows that visual web use is not solved by attaching a screenshot to a strong model. Direct vision improves results, and SoM sometimes improves action grounding, but planning and state management remain severe constraints. [A: §§6–7; App. C]

The strongest evidence for direct visual value comes from controlled representations within a model family: GPT-4’s 7.25% text-only result rises to 12.75% with captions and to 15.05–16.37% with direct images. The task examples explain why: captions can say “city skyline” while omitting the UPMC and PNC signage needed to infer the correct forum; accessibility trees can list nearby controls without clearly linking them to adjacent images. [A: pp. 8, 17–18]

SoM’s contribution is narrower than “SoM always improves agents.” It improves GPT-4V overall and notably on Reddit, but not Shopping and not the other VLMs in Table 3. The authors interpret this as dependence on strong visual grounding capacity. [A/B: Table 3, §6]

Failure traces reveal that perception is only one component. Agents may identify the right product, then undo the action; know the next step, yet stop instead of scrolling; or repeatedly append text because they lack reliable state/history control. Thus a visually capable agent can still fail due to planning, persistence, editing semantics, or termination decisions. [A: App. C.4]

The paper’s conclusions are directionally supported by its tables and cases, but inferential strength is limited by absent variance estimates, repeated-run information, and formal significance tests. “Significantly” is sometimes used colloquially; the supplied work does not report statistical significance testing.

## Notable consistency findings

1. **SoM site labels:** p. 8 prose reverses the Classifieds and Reddit numeric transitions relative to Table 3.
2. **Best-model headline:** the main paper says the best VLM achieves about 16.4%, while Appendix B later reports GPT-4o at 19.78%. This reflects experiment timing rather than necessarily a computational error.
3. **Figure 17 example:** the Reddit example appears to direct `click [11]` even though `[16]` is the displayed comments link for the croissant post.
4. **Human comparison:** humans were evaluated on 230 tasks, models apparently on the full benchmark. The paper presents rates side by side, but their evaluated task sets are not identical.

# 15. Contributions and Novelty

## Benchmark contribution

A suite of 910 visually grounded, executable browser tasks spanning three principal environments and multi-site workflows. [A: §§1, 4]

## Dataset/environment contribution

A new self-hosted Classifieds environment with 65,955 redacted, image-bearing listings. [A: §§4.1; App. D]

## Methodological contribution

Task-specific evaluation primitives for semantic answers, visual properties, exact/fuzzy image matching, required/prohibited content, URLs, and final-page state. [A: §3.3, Table 2]

## Interface contribution

A JavaScript-generated SoM observation/action representation that couples marked visual controls to discrete element IDs. [A: §§3.1–3.2, 5.3]

## Experimental contribution

A comparison of numerous text-only, captioned, multimodal, and SoM agents, plus human performance, few-shot analysis, task subsets, difficulty, trajectory length, and qualitative failures. [A: §§5–6; Apps. B–C]

## Empirical contribution

Evidence that multimodality helps strong agents, SoM can improve GPT-4V navigation, OCR and long-horizon behavior remain difficult, and contemporary agents remain far below human performance. [A/B: Tables 3–6; Figs. 6–13]

# 16. Limitations

## Authors’ stated limitations

- Existing agents remain insufficient even for many simple tasks. [A: §8]
- Text-only agents struggle with visual content; captions omit fine-grained information. [A: §§6; App. C.5]
- GPT-4-family agents perform worse on OCR-required tasks. [A: §6.1; App. C.3]
- Agents fail over longer horizons, undo correct actions, give up early, loop, repeat actions, and mishandle replacement in input fields. [A: App. C.4]
- Human difficulty labeling can deviate because some tasks emphasize visual or reasoning challenges differently. [A: §4.2]
- Rewards are binary; continuous performance scales are left for future work. [A: footnote 2]
- Bias, harmful actions, employment effects, and safeguards require further study. [A: §8]
- The demonstrated systems are research prototypes and not intended for real-world or high-risk deployment. [A: §8]
- GPT-4V was too expensive for the few-shot ablation, so Gemini-Pro was used. [A: App. C.1]

## Additional evidence-based analyst observations

The following are **[D] analyst observations**, not author admissions:

- A benchmark whose task authors also design reward functions risks shared assumptions between task wording and evaluation logic.
- Seven human participants and 230 sampled tasks provide a useful reference but a limited estimate of broader human performance.
- Some human participants were task authors; assignment separation reduces direct leakage but may not remove familiarity with benchmark conventions.
- No inter-annotator agreement is reported for visual/action difficulty labels.
- No repeated-run counts, random seeds, confidence intervals, or statistical tests are reported despite stochastic nucleus sampling.
- Model comparisons may be affected by unequal viewport and truncation settings necessitated by context limits.
- Learned evaluators—GPT-4-Turbo for semantic matching and BLIP-2 for visual questions—can introduce evaluator error or model-specific bias.
- Task-level SSIM thresholds and evaluator validation rates are not supplied.
- The main “realistic” environments are self-hosted replicas; ecological validity for changing, adversarial, or personalized live websites remains unmeasured.
- Because the human and model evaluations use different task sets, their rates are informative but not a strictly paired comparison.
- Template families may induce dependence among tasks; uncertainty estimates treating all 910 items as independent could therefore be misleading, though none are reported.

# 17. Threats to Validity

These categories are analyst-organized unless explicitly noted.

## Internal validity

Model performance differences are confounded by model capability, representation, context limits, viewport size, and sampling parameters. Caption and visual backbones also vary. Within-family comparisons are more interpretable than broad cross-model comparisons.

## Construct validity

Binary completion is a clear operational measure but ignores partial progress, action efficiency, near-correct answers, and severity of mistakes. Learned fuzzy/VQA evaluators may not perfectly embody the intended task construct.

## Statistical conclusion validity

The paper provides percentages without uncertainty, repetitions, or significance tests. Small differences such as 15.05% versus 16.37% should therefore be treated as observed benchmark differences, not proven population effects.

## External and ecological validity

The tasks are designed to resemble realistic usage, but run in static self-hosted websites. Generalization to arbitrary live sites, dynamic content, authentication changes, advertisements, anti-bot systems, or adversarial webpages is untested.

## Reproducibility

Self-hosting, deterministic environment transitions, documented actions, prompts, viewports, and sampling parameters support reproduction. Missing hardware information, seeds, repeated-run procedures, full task/evaluator artifacts in the supplied document, and model-service version persistence limit what can be reproduced from the paper alone.

## Data and evaluator validity

The Classifieds data are scraped and redacted, but the paper does not report quantitative checks of redaction accuracy, category balance, duplicate images, or evaluator false-positive/negative rates.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- continuous rather than binary performance rewards;
- more advanced prompting strategies;
- fine-tuning models on web trajectories;
- improved reasoning, visual understanding, and planning;
- stronger OCR, including examination of later Gemini models;
- stronger processing of multiple interleaved image-text inputs;
- more sophisticated tracking of past states and execution history;
- research on bias, harmful behavior, safeguards, and social/economic effects;
- evaluation of stronger open-source VLMs. [A: pp. 4, 7, 9, 13–17]

## B. Additional open questions

- How stable are success rates over repeated stochastic runs?
- How accurate are the learned evaluators relative to independent human judgment?
- Which gains come from direct vision versus improved models, prompts, or context capacity?
- Would SoM remain beneficial when agents can reliably predict coordinates?
- How much performance is lost specifically through perception, planning, memory, grounding, or premature stopping?
- How do results change under template-disjoint or site-disjoint evaluation?
- Can progress-sensitive rewards distinguish promising partial solutions from arbitrary failure?
- What safeguards are necessary when benchmark agents are transferred from sandboxes to real accounts?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| Accessibility tree | Structured text representation of page elements used by assistive technologies |
| Agent | A system that observes a state, chooses actions, and tries to complete a goal |
| BLIP-2-T5XL | The caption/VQA model used to describe images and evaluate some visual properties |
| Chain-of-thought prompting | Prompting that elicits intermediate reasoning before an action |
| CMS | Content Management System; software used to run sites such as Classifieds |
| DOM | Document Object Model; the programmatic tree of an HTML page |
| Exact image match | Finding an image with the same content, not merely a similar subject |
| In-context example | A worked demonstration included in the prompt without changing model weights |
| LLM | Large Language Model |
| Multimodal | Able to process more than one modality, here principally images and text |
| OCR | Optical Character Recognition; reading text embedded in images |
| PII | Personally Identifiable Information |
| POMDP | Partially Observable Markov Decision Process; an agent acts without seeing the complete underlying state |
| SoM | Set-of-Marks; numbered bounding boxes over interactive visual elements |
| SSIM | Structural Similarity Index Measure; an image-similarity measure |
| Success rate | Percentage of tasks receiving reward 1 |
| VLM | Vision-Language Model |
| VQA | Visual Question Answering |
| \(\mathcal{S}\) | Set of environment states |
| \(\mathcal{A}\) | Set of possible actions |
| \(\Omega\) | Set of possible observations |
| \(T\) | State-transition function |
| \(R\) | Binary reward function |
| \(s_t\) | Environment state at time \(t\) |
| \(o_t\) | Partial observation at time \(t\) |
| \(a_t\) | Action at time \(t\) |
| \(\hat a\) | Agent-produced answer |
| \(a^\*\) | Expected or ground-truth answer |
| \(t\) in the SSIM rule | Task-specific similarity threshold in \([0,1]\) |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Benchmark size | 910 | tasks | Entire benchmark | Author-reported | p. 1, §1 |
| Task templates | 314 | templates | Task collection | Author-reported | p. 5, §4.2 |
| Mean tasks/template | 2.9 | tasks/template | Task collection | Author-reported | p. 5, §4.2 |
| Image-input share | 25.2% | tasks | 229 tasks | Author-reported | pp. 9, 14 |
| Unachievable tasks | 46 (5.1%) | tasks | Require reason for impossibility | Author-reported | p. 5 |
| Classifieds listings | 65,955 | listings | New environment | Author-reported | pp. 5, 19 |
| Reddit image posts | 31,464 | posts | Reddit environment | Author-reported | p. 5 |
| Task annotators | 6 | people | Graduate-student co-authors | Author-reported | pp. 5, 19 |
| Human evaluators | 7 | people | 230-task sample | Author-reported | p. 6 |
| Human success | 88.70% | success rate | Overall sample | Visually readable | Table 3, p. 8 |
| GPT-4 text-only | 7.25% | success rate | Main benchmark | Visually readable | Table 3 |
| GPT-4 + BLIP-2 captions | 12.75% | success rate | Main benchmark | Visually readable | Table 3 |
| GPT-4V multimodal | 15.05% | success rate | Image + captions + accessibility tree | Visually readable | Table 3 |
| GPT-4V + SoM | 16.37% | success rate | Original best agent | Visually readable | Table 3 |
| GPT-4o + SoM | 19.78% | success rate | Post-submission model | Visually readable | Table 5, p. 13 |
| Original human–agent gap | 72.33 | percentage points | 88.70 − 16.37 | Analyst-derived | Tables 3 |
| Later human–agent gap | 68.92 | percentage points | 88.70 − 19.78; unmatched task samples | Analyst-derived | Tables 3, 5 |
| SoM overall GPT-4V gain | 1.32 | percentage points | 15.05 → 16.37 | Analyst-derived | Table 3 |
| GPT-4 caption gain | 5.50 | percentage points | 7.25 → 12.75 | Analyst-derived | Table 3 |
| OCR-required share | 17.1% | tasks | Benchmark subset | Author-reported | Table 4 |
| GPT-4V + SoM on OCR | 13.4% | success rate | OCR tasks | Visually readable | Table 4 |
| GPT-4V + SoM without OCR | 16.9% | success rate | Non-OCR tasks | Visually readable | Table 4 |
| Exact-match share | 8.7% | tasks | Benchmark subset | Author-reported | Table 4 |
| GPT-4V + SoM exact match | 18.9% | success rate | Exact-image subset | Visually readable | Table 4 |
| GPT-4V + SoM image input | 19.0% | success rate | Image-input subset | Visually readable | Table 4 |
| GPT-4V + SoM no image input | 14.9% | success rate | Text-specified subset | Visually readable | Table 4 |
| Gemini-Pro, 0 examples | 2.86% | success rate | Multimodal/accessibility-tree | Visually readable | Table 6 |
| Gemini-Pro, 3 examples | 6.04% | success rate | Same configuration | Visually readable | Table 6 |
| Standard viewport | 1280 × 2048 | pixels | Most baselines | Author-reported | App. F |
| Short-context viewport | 1280 × 720 | pixels | LLaMA/IDEFICS/CogVLM | Author-reported | App. F |
| Standard truncation | 3,840 | tokens | Most text observations | Author-reported | App. F |
| Short-context truncation | 640 | tokens | Shorter-context models | Author-reported | App. F |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Current agents are far below humans | 16.37% GPT-4V+SoM vs 88.70% human | X1–X2, Table 3 | p. 8 | Strong descriptive gap; task sets differ for humans/models |
| Captions help GPT-4 | 7.25% → 12.75% | X1, Table 3 | pp. 7–8 | Strong within-family descriptive evidence; no uncertainty test |
| Direct multimodality helps GPT-4 | 12.75% captioned vs 15.05% multimodal | X1, Table 3 | p. 8 | Configurations also differ in observation representation |
| SoM improves GPT-4V overall | 15.05% → 16.37% | X3, Table 3 | p. 8 | Modest descriptive increase; not universal across sites/models |
| SoM helps dense navigation | Large Reddit improvement; successful trajectories | X3, Figs. 3, 13 | pp. 8, 18, 21 | Attribution to visual density is an author hypothesis |
| OCR remains difficult | 13.4% OCR vs 16.9% non-OCR | X4, Table 4, Fig. 7 | pp. 9, 14–15 | Observational subset comparison |
| Exact matching is not GPT-4V+SoM’s primary bottleneck | 18.9% exact vs 16.2% non-exact | X4, Table 4 | p. 9 | Applies to this agent; other models differ |
| Image-input tasks can be tractable for GPT-4V+SoM | 19.0% vs 14.9% | X4, Table 4, Fig. 9 | pp. 9, 14, 17 | Likely confounded by task composition |
| More examples improve Gemini-Pro | 2.86%, 3.63%, 6.04% for 0/1/3 examples | X6, Table 6 | p. 13 | Overall monotonic; some site-level non-monotonicity |
| Harder tasks reduce success | Heatmaps decline with visual/action difficulty | X5, Fig. 6 | pp. 13–14 | Difficulty labels are human judgments |
| Agents suffer long-horizon failures | Undoing, early stopping, loops, repeated edits | X8–X9, Figs. 10–12 | pp. 15–19 | Qualitative examples; prevalence not quantified |
| GPT-4o advances the benchmark | 19.78% vs GPT-4V+SoM 16.37% | X7, Tables 3/5 | pp. 8, 13 | Cross-model descriptive comparison, no repeated-run statistics |

# 22. Very Simple Explanation

Imagine asking a computer to buy “the red blanket,” find the post containing a particular photograph, or comment on the newest white phone listing. Reading the webpage’s text is not enough: the computer must look at pictures, understand where things are, click the correct controls, remember what it has already done, and know when the job is finished.

The researchers built a test with 910 such jobs. Their special Set-of-Marks interface draws numbered boxes around buttons and links, so the model can say “click box 31” instead of guessing screen coordinates. This helped the strongest tested visual model, especially on visually crowded pages.

But the agents were still unreliable. The original best system solved about 16% of tasks, and a later GPT-4o experiment solved about 20%, while people solved about 89% of a representative sample. Agents often understood part of a task but then stopped too early, clicked a similar-looking object, undid correct work, repeated themselves, or became stuck in loops. The paper’s message is therefore: vision and better grounding help, but dependable web agents also need much better planning, memory, persistence, and evaluation.

# Completeness Audit

## Inventory-based coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title/authors/venue | Yes | Yes | Fully represented | ACL 2024 long paper; bibliographic details recorded in Stage 0/roadmap |
| Abstract | Yes | Yes | Fully represented | Incorporated into orientation and problem statement |
| §1 Introduction | Yes | Yes | Fully represented | Motivation, gap, tasks, headline results, contributions |
| §2 Related Work | Yes | Yes | Represented in compressed form | Categories and positioning retained; individual citations not enumerated |
| §3 Environment | Yes | Yes | Fully represented | POMDP, observation, action, reward |
| §3.1 Observation Space | Yes | Yes | Fully represented | Four representations and input images |
| §3.2 Action Space | Yes | Yes | Fully represented | All actions covered through Table 1 |
| §3.3 Evaluation | Yes | Yes | Fully represented | All evaluator families and binary reward |
| §4 Task Curation | Yes | Yes | Fully represented | Sites, collection, grounding, difficulty, humans |
| §4.1 Environments | Yes | Yes | Fully represented | Classifieds, Shopping, Reddit, Wikipedia role |
| §4.2 Tasks | Yes | Yes | Fully represented | Counts, templates, annotators, images, unachievable tasks |
| §4.3 Human Performance | Yes | Yes | Fully represented | Sample, leakage precaution, rates, failures |
| §5 Baselines | Yes | Yes | Fully represented | All model/input families |
| §5.1 Text agents | Yes | Yes | Fully represented | Models, accessibility tree, prompting |
| §5.2 Caption agents | Yes | Yes | Fully represented | BLIP-2/LLaVA procedure and selection rationale |
| §5.3 Multimodal agents | Yes | Yes | Fully represented | Accessibility-tree and SoM settings |
| §6 Results | Yes | Yes | Fully represented | Primary quantitative claims and inconsistency |
| §6.1 Task types | Yes | Yes | Fully represented | OCR, exact match, input images |
| §7 Conclusion | Yes | Yes | Fully represented | Integrated into interpretation |
| §8 Ethics/Impacts | Yes | Yes | Fully represented | Accessibility, labor, bias, harm, intended use |
| References | Yes, textually | Yes | Deliberately compressed | Bibliographic list is non-substantive to the paper’s own empirical evidence |
| Appendix A | Yes | Yes | Fully represented | Site and difficulty distributions |
| Appendix B | Yes | Yes | Fully represented | Later models/Table 5 |
| Appendix C.1 | Yes | Yes | Fully represented | Few-shot/Table 6 |
| Appendix C.2 | Yes | Yes | Fully represented | Difficulty/Figure 6 |
| Appendix C.3 | Yes | Yes | Fully represented | OCR, exact match, image inputs |
| Appendix C.4 | Yes | Yes | Fully represented | All named failure classes |
| Appendix C.5 | Yes | Yes | Fully represented | Text/caption, caption/SoM, multimodal/SoM comparisons |
| Appendix D | Yes | Yes | Fully represented | Scraping, redaction, interface |
| Appendix E | Yes | Yes | Fully represented | Expanded collection procedure |
| Appendix F | Yes | Yes | Fully represented | Viewports, truncation, sampling, prompts |
| Figure 1 | Visually | Yes | Fully represented | Benchmark overview |
| Figure 2 | Visually | Yes | Fully represented | SoM construction |
| Figure 3 | Visually | Yes | Fully represented | Successful Reddit trajectory |
| Figure 4 | Visually | Yes | Fully represented | Exact labeled site shares |
| Figure 5 | Visually | Yes | Fully represented | All nine labeled cells |
| Figure 6 | Visually | Yes | Fully represented | Four panels and key values |
| Figure 7 | Visually | Yes | Represented with uncertainty | Unlabeled bar heights not treated as exact |
| Figure 8 | Visually | Yes | Represented with uncertainty | Table/prose values distinguished from visual estimates |
| Figure 9 | Visually | Yes | Represented with uncertainty | Same limitation |
| Figure 10 | Visually | Yes | Fully represented | Displayed percentages retained |
| Figure 11 | Visually | Yes | Fully represented | Interface example, not a quantitative plot |
| Figure 12 | Visually | Yes | Fully represented | Full failure logic described |
| Figure 13 | Visually | Yes | Fully represented | Successful SoM workflow |
| Figure 14 | Visually | Yes | Fully represented | Classifieds homepage |
| Figure 15 | Visually | Yes | Fully represented | Listing/detail interface |
| Figure 16 | Visually | Yes | Fully represented | System prompt rules compressed faithfully |
| Figure 17 | Visually | Yes | Fully represented | Three demonstrations and suspected ID inconsistency |
| Table 1 | Visually | Yes | Fully represented | Every action category covered |
| Table 2 | Visually | Yes | Fully represented | Every example/evaluator combination covered |
| Table 3 | Visually | Yes | Fully represented | Principal rows, extrema, and comparisons covered |
| Table 4 | Visually | Yes | Fully represented | All six subset rows retained |
| Table 5 | Visually | Yes | Fully represented | All four rows retained |
| Table 6 | Visually | Yes | Fully represented | All values discussed |
| Major equations | Yes | Yes | Fully represented | E1–E7 |
| Algorithms/pseudocode | None present | N/A | No inventory item | Agent loop is described but no formal algorithm block appears |
| Formal RQs/hypotheses | None present | Yes | Absence explicitly represented | Informal objectives separated from analyst-organized questions |
| Author limitations | Yes | Yes | Fully represented | Explicitly separated from analyst observations |
| Supplementary material | Not supplied | Yes | Missing from supplied material | No separate supplement was detected or claimed as inspected |

## Missing or inaccessible material

- Pages 5 and 11 were not visually rendered, although their complete native text was supplied and readable. Neither contains an identified substantive figure or table.
- The benchmark’s executable code, full 910-task dataset, individual reward configurations, raw trajectories, and underlying website databases were not supplied as inspectable artifacts.
- Full-resolution source images inside some webpage screenshots were not separately supplied; tiny webpage text cannot always be independently verified.
- No separate supplementary material was supplied.
- Hardware details, random seeds, repeated-run logs, confidence intervals, and evaluator-validation data are absent from the paper itself.

## Uncertain interpretations

- Exact heights for many bars in Figures 7–9 are unlabeled; only table/prose-supported values were treated as exact.
- Figure 10’s displayed success percentages are readable, but exact raw count values and every bin boundary are not labeled clearly enough to reconstruct the full underlying data.
- The SSIM threshold \(t\) is defined but no task-specific value is reported.
- The p. 8 prose reverses the Classifieds and Reddit SoM transitions relative to Table 3.
- Figure 17 appears to use the wrong Reddit comment-link ID in its second demonstration.
- “Significantly” is not backed by a reported statistical significance test and is interpreted descriptively.
- The main text’s 16.4% “best VLM” statement predates Appendix B’s 19.78% GPT-4o result.

## Deliberately compressed material

- The individual bibliography entries were inspected through supplied text but compressed into three related-work categories.
- Repetitive listings of cited model families were summarized rather than reproduced citation by citation.
- Small decorative/site-content details in Figures 1, 11, 14, and 15 were compressed because their substantive role is interface illustration.
- Figure 16’s prompt and Figure 17’s examples were explained structurally rather than copied verbatim.
- Every numeric cell of Table 3 is not repeated in narrative prose, but the table’s group structure, principal values, extrema, and claim-relevant comparisons are represented.

## Potential omissions

No known substantive section, appendix, figure, table, major mathematical definition, experiment, contribution, or author-stated limitation from the document inventory is unrepresented. The principal unavoidable omissions are the unsupplied executable artifacts and fine-grained image details identified above.