# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible range | Pages 1–36 |
| Apparently missing pages | None |
| Native/extracted text | Available for all 36 pages |
| Visually rendered pages inspected | 1–7, 10, and 14–36 |
| Pages not visually rendered | 8, 9, and 11–13 |
| Figures | Figures 1–20 were visually available and inspected |
| Tables | Tables 1–9 were visually available and readable |
| Equations | The two principal state/action equations on p. 2 were readable; extracted notation was checked against the rendered page |
| Algorithms/pseudocode | None presented as formal algorithms |
| Appendices | Appendices A–I, pp. 13–36, are present |
| Supplementary material | No separate supplementary file was supplied |
| External artifacts referenced but not supplied | Project website, GitHub repository, released dataset, Playwright, Supervision library, model checkpoints, and cited works |
| OCR needed | No; native text was available. OCR-like extraction spacing errors occur in tables and model names, so rendered pages were preferred |
| Visual limitations | Fine text inside some webpage screenshots is too small to read exhaustively, but captions, highlighted elements, enlarged insets, and surrounding text make each figure’s substantive point readable |
| Other limitations | Publication venue is not stated. The document identifies itself as arXiv:2401.01614v2, dated 12 March 2024 (p. 1). No keywords are supplied. |

Evidence categories used below:

- **[A] Author-reported:** stated in the supplied paper.
- **[B] Directly observable:** visible in a supplied page, figure, or table.
- **[C] Analyst-derived:** calculated from supplied values; operands are shown.
- **[D] Analyst interpretation:** an explicitly identified inference.
- **[E] External information:** excluded under closed-document mode.

# 1. Plain-Language Orientation

This paper asks whether a large multimodal model—principally GPT-4V, which processes both language and images—can act as a general-purpose web agent. Such an agent receives a natural-language task, examines a webpage, and performs a sequence of browser actions such as clicking, typing, and selecting options.

The paper separates web navigation into two problems (pp. 2–3, §2):

1. **Action generation:** decide in natural language what should happen next.
2. **Action grounding:** convert that plan into an executable operation on the correct webpage element.

The central finding is that GPT-4V often understands webpages and proposes appropriate next actions, but reliably connecting those plans to exact webpage elements remains difficult. With humans manually translating GPT-4V’s intended actions into browser events—an approximate **oracle grounding** condition—SEEACT completes **51.1% of 90 live-web tasks**. With the paper’s best automatic method, textual-choice grounding, it completes **37.8%**. Text-only GPT-4 and fine-tuned FLAN-T5-XL achieve **13.3%** and **8.9%**, respectively (pp. 6–7, Table 4).

The central contribution is therefore conditional: GPT-4V shows considerable potential as a generalist web planner **if grounded effectively**. The paper introduces **SEEACT**, compares three grounding strategies, constructs a multimodal version of Mind2Web, and adds an online evaluation framework for live websites.

# 2. Document Roadmap

The 36-page work is an empirical machine-learning and web-agent systems paper.

| ID | Original section | Pages | Function |
|---|---|---:|---|
| S1 | Abstract | 1 | Problem, method, headline results |
| S2 | §1 Introduction | 1–2 | Motivation, gap, contributions |
| S3 | §2 SeeAct | 2–4 | Formalization, action generation, grounding methods |
| S4 | §3 Experiments | 4–5 | Dataset, baselines, offline and online protocols |
| S5 | §4 Results and Analysis | 5–8 | Quantitative evaluation, difficulty/error analyses, cases |
| S6 | §5 Related Work | 8 | Web agents, LMMs, visual grounding |
| S7 | §6 Conclusion | 8 | Findings and future direction |
| S8 | §7 Impact Statements | 9 | Safety, privacy, deployment concerns |
| S9 | References | 9–12 | Cited literature; bibliographic rather than experimental evidence |
| A1 | Appendix A | 14 | Method details |
| A2 | Appendix B | 14 | Markup ablation |
| A3 | Appendix C | 14–15 | Online-evaluation details |
| A4 | Appendix D | 15–18 | Prompts |
| A5 | Appendix E | 19, 26–29 | Image-annotation error examples |
| A6 | Appendix F | 19, 30–31 | Planning and webpage understanding |
| A7 | Appendix G | 19, 32 | Identical-element grounding problem |
| A8 | Appendix H | 19, 33–34 | Knowledge requirements |
| A9 | Appendix I | 19, 35–36 | Alternative paths and error correction |

Document inventory:

- **Title:** *GPT-4V(ision) is a Generalist Web Agent, if Grounded*
- **Authors:** Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, and Yu Su
- **Affiliation:** The Ohio State University (p. 1 footnote)
- **Version:** arXiv:2401.01614v2, 12 March 2024
- **Document type:** Empirical AI/ML and web-agent systems paper; also introduces a cleaned multimodal dataset and live-evaluation tool
- **Figures:** 20
- **Tables:** 9
- **Major equations:** 2, plus definitions of action/state objects
- **Distinct quantitative analyses:** dataset characterization, broad offline comparison, grounding comparison, online/offline comparison, difficulty analysis, error analysis, and markup ablation
- **Formal hypotheses:** None
- **Formal research questions:** None enumerated
- **Keywords:** Not supplied

# 3. Background and Context

A **web agent** is a system that performs actions on websites in pursuit of a user instruction. A task may require more than ten actions across dynamically rendered pages (§1, p. 2).

A **large language model (LLM)** processes primarily textual input. A **large multimodal model (LMM)** can combine text with visual input. The paper focuses on GPT-4V and also evaluates Gemini Pro Vision and LLaVA-1.5.

A webpage has at least two relevant representations:

- **HTML/DOM representation:** the underlying structured elements and attributes.
- **Rendered screenshot:** what a human sees, including visual layout and embedded images.

The authors argue that raw HTML is noisy, long, and visually incomplete. Their Figure 1 example contains **423 HTML elements**, requiring **186,490 GPT-2 textual tokens**, versus **1,445 GPT-4V visual tokens** for the screenshot (p. 2). These values illustrate input-density differences; they are not a general average.

**Grounding** means connecting a model’s abstract or textual intention to something actionable in the environment. Here, it means identifying the exact element and browser operation required to execute a plan (§2.3, p. 3).

The paper evaluates on **Mind2Web**, a benchmark of real-world web tasks. The authors align its HTML snapshots with screenshots and call the cleaned result **Multimodal Mind2Web** (§3.1, pp. 4–5).

# 4. Research Problem and Gap

## Existing problem

Generalist web agents must interpret diverse, visually complex websites and execute multi-step tasks. A plan that says “click Search” is insufficient unless the system can identify the correct Search button and translate the intention into an executable browser event.

## Shortcomings attributed to prior approaches

According to the authors:

- HTML-only methods consume large textual contexts and miss visual information such as embedded-image semantics (§1, p. 2).
- Smaller fine-tuned agents may not generalize well to unseen websites and domains (§1, pp. 1–2; §4.1, p. 6).
- Visual grounding methods successful on natural images may fail on dense webpages with many related or identical elements (§2.3, pp. 3–4; §4.3, p. 7).
- Offline reference traces encode only one valid route, although live tasks can admit multiple successful action sequences (§4.2, pp. 6–7).

## Research gap

The paper identifies a lack of evidence about whether powerful general-purpose LMMs can serve as web agents across many real websites, particularly when evaluated online rather than solely against cached, single-path annotations.

## Motivation

Rendered webpages are visually designed for humans and can convey information more compactly than raw HTML. If an LMM can understand those visuals and be grounded to executable elements, it may support broad web automation (§1, pp. 1–2).

## Scope

The evaluation covers Mind2Web-derived tasks using Click, Type, and Select operations; online experiments are restricted to non-login, monitored tasks and avoid final submissions or harmful state changes (§§3.1, 3.4; pp. 4–5; Appendix C, pp. 14–15).

# 5. Research Questions / Objectives / Hypotheses

The paper does not enumerate formal research questions or hypotheses. Its author-stated objectives can be reconstructed without turning them into formally claimed RQs:

1. Investigate the potential of LMMs, especially GPT-4V, as generalist web agents (§1, pp. 1–2).
2. Separate and evaluate action-generation ability from the element-grounding bottleneck (§2, pp. 2–4).
3. Compare element-attribute, textual-choice, and image-annotation grounding (§2.3, pp. 3–4).
4. Compare LMMs, text-only LLMs, fine-tuned smaller models, and pixel-level grounding (§3.2, p. 4).
5. Compare cached offline evaluation with monitored live-web evaluation (§§3.3–3.4, pp. 4–5).
6. Analyze task difficulty, grounding errors, planning, knowledge use, alternative paths, and error correction (§§4.3–4.4, pp. 7–8; Appendices E–I).

No preregistration, directional hypothesis, or null-hypothesis significance test is reported.

# 6. Assumptions / Threat Model

This is not a security experiment with a formal attacker model. Its operative assumptions are:

- A task \(T\), webpage screenshot, HTML state, and action history are available (§2.1, pp. 2–3).
- Action generation uses the screenshot but not HTML (§2.2, p. 3).
- A browser action can be represented by target element, operation, and optional value (§2.1, p. 3).
- String parsing is considered adequate for extracting operation and value; element identification is treated as the main grounding challenge (§2.3, p. 3).
- The offline environment supplies cached HTML and screenshots; live evaluation uses current websites.
- The “oracle” is approximate: humans infer and implement the action intended by the model (§2.3, p. 4; Appendix C, p. 14).
- The candidate ranker’s top 50 elements define the search pool for textual-choice and image-annotation grounding (§3.2, p. 4).
- Offline exact-trace scoring assumes reference actions are authoritative, although the authors later show that alternative valid routes exist (§4.2, p. 7; Fig. 19).
- Humans monitor live actions and block logins, final submissions, or potentially harmful actions (§3.4, p. 5; Appendix C, p. 14).

Safety-relevant assets include user profiles, personal information, financial transactions, and submitted forms. The paper does not model a malicious agent or adversary; it reports the possibility of harmful generated actions and uses human validation before execution (§7, p. 9).

# 7. Methodology

## 7.1 System decomposition

SEEACT divides each step into:

1. **Visual action generation:** GPT-4V examines the screenshot, task, and history and describes one next action.
2. **Action grounding:** the description is converted to target element \(e\), operation \(o\), and value \(v\).
3. **Browser execution:** the resulting event changes the webpage state.
4. The process repeats until completion or termination (§2, pp. 2–4; Fig. 1).

## 7.2 Action generation

The model is instructed to:

- identify the current webpage;
- analyze previous actions;
- inspect screenshot details;
- decide one valid next action;
- describe the target’s content and location (§2.2, p. 3; Table 6, p. 15).

The screenshot is used as visual context; HTML is not supplied during this stage.

## 7.3 Grounding strategies

### Element attributes

GPT-4V generates a detailed element description, type, exact visible text, operation, and value. A heuristic searches DOM elements for matching text and type. A unique match is selected automatically; ambiguous matches trigger an additional selection step (§2.3, p. 3; Table 7, p. 16).

### Textual choices

A DeBERTa-base cross-encoder inherited from MindAct ranks webpage elements. The top 50 are divided into groups of 17. Candidates are represented through HTML text, and GPT-4V chooses a letter or “none” (§2.3, pp. 3–4; §3.2, p. 4; Table 8, p. 17).

### Image annotation

Ranked candidates receive red bounding boxes and nearby index labels. GPT-4V must return the target label, or “NA” if no correct box exists (§2.3, p. 4; Table 9, p. 18).

### Oracle grounding

Human annotators identify and implement the action intended by GPT-4V, provided the description sufficiently indicates element, operation, and value (§2.3, p. 4). This measures planning/action-generation potential under highly favorable grounding.

## 7.4 Dataset

The original Mind2Web contains over 2,000 tasks on 137 websites, 31 low-level domains, and 12 high-level domains (§3.1, p. 4).

The cleaned Multimodal Mind2Web aligns HTML with screenshots and uses human verification for visibility and rendering (§3.1, p. 4).

| Split | Tasks | Domains | Websites | Avg. actions | Avg. visual tokens | Avg. HTML elements | Avg. HTML tokens |
|---|---:|---:|---:|---:|---:|---:|---:|
| Train | 1,009 | 17 | 73 | 7.7 | 4,240 | 602 | 128,827 |
| Cross-Domain | 694 | 13 | 53 | 5.9 | 4,314 | 494 | 91,163 |
| Cross-Task | 177 | 17 | 64 | 7.6 | 4,172 | 607 | 123,274 |
| Cross-Website | 142 | 9 | 10 | 7.2 | 4,653 | 612 | 114,358 |

Source: Table 1, p. 5 [A/B].

The split meanings are:

- **Cross-Task:** new tasks on included domains and websites.
- **Cross-Website:** tasks from ten new websites within top-level training domains.
- **Cross-Domain:** tasks from two top-level domains withheld from training (§3.1, p. 4).

## 7.5 Models and baselines

- FLAN-T5-XL: supervised fine-tuning on ground-truth action sequences.
- BLIP-2-T5-XL: FLAN-T5 language model plus frozen CLIP ViT-L/14 vision encoder at image resolution 2,048; language and bridge modules jointly fine-tuned.
- GPT-3.5-turbo-0613 and GPT-4-turbo-1106-preview: text-only, three-shot in-context learning.
- GPT-4-vision-preview, Gemini Pro Vision, and LLaVA-1.5 within SEEACT.
- CogAgent: coordinate/pixel-oriented grounding baseline using the unfine-tuned `cogagent-chat-hf` checkpoint (Appendix A, p. 14).

Gemini’s two turns were merged because it supported only single-turn conversations (Appendix A, p. 14).

## 7.6 Evaluation metrics

- **Element Accuracy:** whether the selected element equals ground truth.
- **Operation F1:** token-level F1 for action and input value.
- **Step Success Rate:** a step succeeds only when both element and operation are correct.
- **Task Success Rate:** all task steps must succeed (§3.3, p. 5).

Offline step metrics are macro-averaged across tasks. The paper reports no confidence intervals, repeated-run variability, random seeds, hypothesis tests, or statistical significance tests.

## 7.7 Online protocol

The authors built a Playwright-based tool that passes multimodal browser observations to the agent and executes predicted events (§3.4, p. 5).

Online evaluation uses 90 tasks: 30 from each test split. Time-sensitive tasks were updated; invalidated tasks were resampled. Human annotators monitored actions and judged completion (§4.2, p. 6). Pop-up ads were manually closed (Appendix C, p. 15).

SEEACTChoice retained the top-50 ranker and three option groups, while adding PRESS ENTER and TERMINATE. SEEACTOracle’s intended actions were manually implemented (Appendix C, pp. 14–15).

## 7.8 Unreported configuration

The supplied paper does not specify:

- API temperature or decoding parameters;
- random seeds;
- number of repeated trials;
- inference cost or latency;
- hardware;
- exact dates of live evaluation;
- inter-annotator agreement;
- ranker recall on the cleaned dataset;
- formal stopping limits for all systems.

# 8. Experiments / Analyses

## X1 — Dataset characterization

**Purpose:** quantify the multimodal benchmark’s scale and representation burden.

**Data:** four splits in Table 1.

**Main result:** pages average roughly 494–612 HTML elements, 4,172–4,653 visual tokens, and 91,163–128,827 HTML tokens, depending on split (p. 5).

**Caveat:** visual-token counts use an OpenAI calculator; the paper reports averages without dispersion.

## X2 — Broad offline comparison

**Purpose:** compare supervised fine-tuning, text-only in-context learning, pixel grounding, and SEEACT models.

**Setup:** Table 2 reports Element Accuracy, Operation F1, and Step SR on Cross-Task, Cross-Website, and Cross-Domain.

**Sample qualification:** GPT-3.5, GPT-4, and GPT-4V-Oracle rows marked with an asterisk use only 30 tasks per split; other rows appear to use full splits (Table 2 note, p. 6).

**Key result:** GPT-4V-Oracle has the highest reported value in every column, reaching Step SRs of 61.9%, 65.0%, and 62.1%. Automatic GPT-4V with Choices reaches 40.2%, 32.4%, and 36.8%.

**Caveat:** direct comparisons between starred and unstarred rows use different sample sizes.

## X3 — Grounding-method comparison

**Purpose:** isolate the effect of Attributes, Annotation, Choices, and Oracle grounding with GPT-4V.

**Sample:** 30 tasks per split.

**Metric:** Step SR.

| Grounding | Cross-Task | Cross-Website | Cross-Domain |
|---|---:|---:|---:|
| Attributes | 16.1 | 12.1 | 19.0 |
| Annotation | 20.3 | 13.9 | 23.7 |
| Choices | 39.1 | 32.7 | 42.0 |
| Oracle | 61.9 | 65.0 | 62.1 |

Source: Table 3, p. 6.

Textual Choices is the strongest automatic method, but trails Oracle by **22.8, 32.3, and 20.1 percentage points** [C: 61.9−39.1; 65.0−32.7; 62.1−42.0].

## X4 — Online versus offline evaluation

**Purpose:** test whether cached exact-trace evaluation understates practical task completion.

**Sample:** 90 monitored live tasks.

| Model | Offline 0 | Offline 1 | Online |
|---|---:|---:|---:|
| FLAN-T5-XL | 4.4 | 24.4 | 8.9 |
| GPT-4 | 1.1 | 12.2 | 13.3 |
| SEEACTChoice | 3.3 | 12.2 | 37.8 |
| SEEACTOracle | 13.3 | 27.8 | 51.1 |

Source: Table 4, p. 6.

“Offline 0” allows no wrong action; “Offline 1” allows one. Online performance substantially exceeds Offline 0 for all systems, especially SEEACT.

## X5 — Difficulty analysis

**Purpose:** determine whether longer tasks are harder and whether grounding errors accumulate.

**Groups:** Easy = 1–4 actions (37 tasks); Medium = 5–9 (35); Hard = 10–18 (18), totaling 90 (Fig. 3, p. 7).

**Result:** all methods decline as action count increases; SEEACTOracle is strongest at every difficulty. The Oracle–Choice separation widens on longer tasks.

**Visual estimates:** because bars are not numerically labeled, values are approximately:

- Oracle: Easy ~65%, Medium ~46%, Hard ~33%.
- Choices: Easy ~54%, Medium ~34%, Hard ~11%.
- GPT-4: Easy ~24%, Medium ~9%, Hard ~0%.
- FLAN-T5-XL: Easy ~16%, Medium ~6%, Hard ~0%.

These are **approximate visual estimates**, not reported exact values.

## X6 — Image-annotation error analysis

**Purpose:** explain failures when action generation is correct but image grounding is wrong.

**Sample:** 100 randomly sampled action predictions (§4.3, p. 7).

**Results:**

- 54%: model fabricates a bounding box/label when the correct candidate is absent.
- 46%: model finds the target region but links it to an adjacent label.

The two percentages exhaust the sampled errors as reported.

## X7 — Markup ablation

**Purpose:** test annotation label form and position.

**Conditions:** number, single letter, double letter; bottom-left or bottom-center; plus a condition using the numbered annotated image during action generation.

**Best Step SR:** numeric, bottom-left = 24.3%.  
**Best Element Accuracy:** numeric, bottom-left = 27.0%.  
**Best Operation F1:** single letter, bottom-left = 81.0%.

Source: Table 5, p. 14.

## X8 — Qualitative capability and failure cases

Figures 14–20 examine:

- planning beyond the current view;
- recovering state omitted from textual history;
- ambiguity among identical elements;
- requirements for geographic/airport-code knowledge;
- alternative valid action paths;
- correction of a previous invalid input.

These examples demonstrate possibilities and failure mechanisms, but do not establish their population frequency.

# 9. Results

## 9.1 Oracle grounding exposes strong planning potential

GPT-4V-Oracle achieves Step SRs of **61.9%, 65.0%, and 62.1%** on Cross-Task, Cross-Website, and Cross-Domain (Table 2, p. 6). It also achieves **51.1% live task success** (Table 4).

The prose says the offline advantage over the “second-best” method is **8.4%, 23.9%, and 23.2%** (p. 5). These are percentage-point differences against the highest non-oracle values in each split:

- Cross-Task: 61.9−53.5 = **8.4 points**.
- Cross-Website: 65.0−41.1 = **23.9 points**.
- Cross-Domain: 62.1−38.9 = **23.2 points**.

## 9.2 Grounding is the principal bottleneck

On the matched 30-task samples, Oracle exceeds Choices by 20.1–32.3 percentage points (Table 3). Attributes and Annotation perform much worse than Choices.

The conclusion states a “20–25%” gap (p. 8), whereas Table 3 contains a **32.3-point Cross-Website gap**. This is a text–table inconsistency or loose summary. The abstract/introduction more cautiously says “20–30%” (p. 2), which is closer but still slightly below 32.3.

## 9.3 Textual-choice grounding is the best automatic method

SEEACTChoice achieves Step SRs of **39.1%, 32.7%, and 42.0%** on the matched grounding subset (Table 3). It outperforms Annotation by:

- 18.8 points Cross-Task [C: 39.1−20.3],
- 18.8 points Cross-Website [C: 32.7−13.9],
- 18.3 points Cross-Domain [C: 42.0−23.7].

This conflicts with the introduction’s phrase “outperforming image annotation strategies by up to 10%” (p. 2). Table 3 indicates roughly 18-point Step-SR differences. The “up to 10%” statement may refer to an unstated metric or relative setup, but the supplied paper does not resolve it.

## 9.4 GPT-4V with Choices exceeds text-only GPT-4

Using Table 2 values, GPT-4V’s Step SR advantage is:

- Cross-Task: 40.2−32.3 = **7.9 points**,
- Cross-Website: 32.4−27.0 = **5.4 points**,
- Cross-Domain: 36.8−29.7 = **7.1 points**.

However, the prose reports **6.8%, 5.7%, and 12.3%** (p. 6). These values do not match the visible Step SR rows. This is a text–table inconsistency.

The third reported 12.3-point value equals the Element Accuracy difference on Cross-Task (46.4−40.8), not the Cross-Domain Step SR difference. No confident reconciliation is possible from the supplied document.

## 9.5 Fine-tuning versus in-context learning depends on generalization target

FLAN-T5-XL has the strongest non-oracle Cross-Task Step SR at **53.5%**, whereas SEEACT GPT-4V has stronger Cross-Domain automatic Step SR (**36.8%**) than FLAN-T5-XL (**38.9% is actually higher by 2.1 points**). Thus, the broad author interpretation—that supervised fine-tuning retains an advantage on seen websites while ICL is attractive for broad generalization—is only partially visible in the table and depends on metric/split.

[A] The authors argue ICL is compelling when annotation is scarce and environments are diverse, while SFT remains competitive for a fixed website (§4.1, p. 6).

## 9.6 Online evaluation yields much higher completion estimates

SEEACTChoice rises from **3.3% Offline 0** to **37.8% Online**, a difference of **34.5 percentage points** [C]. SEEACTOracle rises from **13.3%** to **51.1%**, a difference of **37.8 points** [C].

The authors attribute this to multiple viable plans, exploration, and error correction that exact offline traces do not credit (§4.2, p. 7; Fig. 19).

## 9.7 Longer tasks magnify grounding errors

Figure 3 shows success decreasing with more actions. The widening Oracle–Choices gap supports the authors’ explanation that grounding errors cascade over a longer horizon (§4.3, p. 7).

## 9.8 Image labels provoke two distinct failures

The sampled image-annotation failures split into fabrication (54%) and incorrect relative label association (46%). Figures 10–13 visually demonstrate each class.

# 10. Figure-by-Figure Interpretation

### Figure 1 — SEEACT architecture (p. 1)

- **Contains:** user task, screenshot, LMM-generated textual plan, HTML grounding, and browser event.
- **Flow:** task/screenshot → LMM action description → grounding to HTML element and operation → website action.
- **Conclusion:** visual planning and executable grounding are separate stages.
- **Caveat:** conceptual diagram, not quantitative evidence.

### Figure 2 — Three grounding methods (p. 3)

- **Contains:** the same “Find Your Truck” action grounded by element attributes, image labels, and textual HTML choices.
- **Inputs:** natural-language action description plus method-specific representation.
- **Outputs:** element text/type, image label G, or textual choice G.
- **Conclusion:** the methods differ chiefly in how the intended target is represented.
- **Visual observation:** the target button is boxed/labeled in the screenshot and represented as an HTML input choice.

### Figure 3 — Success by task difficulty (p. 7)

- **Plot:** grouped bar chart.
- **X-axis:** Easy, Medium, Hard.
- **Y-axis:** Success Rate, 0–70%.
- **Legend:** SEEACTOracle, SEEACTChoices, GPT-4, FLAN-T5-XL.
- **Reported group definitions:** 1–4, 5–9, and 10–18 actions; 37, 35, and 18 tasks.
- **Main observation:** success declines with task length; Oracle leads throughout.
- **Values:** only visually estimable; approximate values are given in §8/X5.
- **Caveat:** no error bars, confidence intervals, or exact bar labels.

### Figures 4–5 — Element-attribute grounding example (pp. 20–21)

- Fig. 4 shows GPT-4V reading a Thumbtack page and planning to click Search.
- Fig. 5 converts the plan into five fields: detailed element description, BUTTON type, exact text “Search,” CLICK, and value None.
- Together they illustrate the two-turn plan-then-ground workflow.
- This is an example, not an accuracy measurement.

### Figures 6–7 — Textual-choice grounding example (pp. 22–23)

- Fig. 6 generates the Search-button plan from the screenshot.
- Fig. 7 supplies HTML-derived candidates A–Q; GPT-4V selects H.
- Choice H is the relevant submit-search button.
- The figure demonstrates how visual understanding and DOM text are combined.

### Figures 8–9 — Image-annotation grounding example (pp. 24–25)

- Fig. 8 generates the same Search-button intention.
- Fig. 9 overlays numbered red boxes and returns element 4.
- The enlarged visual makes clear that labels are spatially adjacent to candidate boxes.
- This adjacency later causes errors when layouts are dense.

### Figure 10 — Fabricated label, example 1 (p. 26)

- The model correctly describes a Continue button.
- The button is absent from the candidate annotations.
- Instead of returning NA, it invents label 12.
- Supports the “making up bounding box and label” category.

### Figure 11 — Fabricated label, example 2 (p. 27)

- The desired Distance control is described correctly.
- It is absent from annotated options.
- The model selects nearby label 5 rather than NA.
- Shows that correct planning does not ensure correct grounding.

### Figure 12 — Incorrect box–label linking, example 1 (p. 28)

- The intended From field contains Pune and should receive Ahmedabad.
- Correct label: 11.
- Model output: 10.
- The adjacent-label mistake illustrates relative-position difficulty.

### Figure 13 — Incorrect box–label linking, example 2 (p. 29)

- The intended filter is Telehealth.
- Correct label: 6.
- Model output: 7, belonging to the adjacent “Accepts New Patients” filter.
- Supports the second error category.

### Figure 14 — Speculative planning (p. 30)

- Task: find Bluetooth and wireless speakers, on sale, under $50.
- From the Best Buy homepage, GPT-4V describes future navigation and filtering steps not yet visible.
- Supports the claim that the model can plan beyond the current screen.
- It does not show whether the whole task was successfully executed.

### Figure 15 — Recovering state from screenshot (p. 31)

- The screenshot shows rental details, automatic same-day drop-off, and “No” for a different return location.
- Those states were inadequately represented in textual history.
- GPT-4V infers the state visually and proposes clicking “Find Your Truck.”
- Supports the value of screenshots beyond action logs.

### Figure 16 — Identical elements (p. 32)

- Three visually separate store rows contain identical “Schedule” buttons.
- The task requires the closest store, Midtown Manhattan.
- Text-only candidate representations cannot reliably distinguish identical HTML/text.
- The authors observe that the model tends to choose the first matching choice.
- This is a structural limitation of textual-choice grounding.

### Figure 17 — Geographic knowledge requirement (p. 33)

- Task: find a driver-training school in Dublin.
- The page lists districts rather than Dublin directly.
- GPT-4V recognizes that outside geographic mapping is needed but cannot identify the district from the screenshot.
- Demonstrates a task requiring knowledge not visible on the page.

### Figure 18 — Airport-code knowledge (p. 34)

- Origin DEL is already entered.
- GPT-4V supplies SJD for Los Cabos and proposes typing it in the destination field.
- The paper treats this as a correct knowledge-intensive example.
- It is a single case rather than a systematic knowledge benchmark.

### Figure 19 — Alternative valid path (p. 35)

- Reference path: More Resources → Natural products database.
- Agent path: Natural products information directly from the first page.
- Both reach the target content according to the paper.
- Supports the claim that exact offline traces can penalize valid alternatives.

### Figure 20 — Error correction (p. 36)

- The phone number field shows an invalid-entry warning.
- GPT-4V detects the problem and prioritizes correcting it before continuing the form.
- Supports adaptive behavior under non-ideal action histories.
- The figure does not report whether correction or final task completion succeeded.

# 11. Table-by-Table Interpretation

### Table 1 — Multimodal Mind2Web statistics (p. 5)

- Compares train and three generalization splits.
- Reports tasks, domains, websites, mean actions, visual tokens, HTML elements, and HTML tokens.
- Train is largest in tasks (1,009); Cross-Domain is the largest test split (694).
- Cross-Website has the highest average visual-token count (4,653) and HTML-element count (612).
- No standard deviations or distributional statistics are supplied.

### Table 2 — Model performance (p. 6)

- Nine metrics: Element Accuracy, Operation F1, and Step SR for three splits.
- GPT-4V-Oracle is best in every visible column.
- Best automatic/non-oracle Step SR:
  - Cross-Task: FLAN-T5-XL, 53.5.
  - Cross-Website: FLAN-T5-XL, 41.1.
  - Cross-Domain: FLAN-T5-XL and BLIP-2-T5-XL tie at 38.9.
- GPT-4V Choices is the strongest SEEACT automatic model: 40.2, 32.4, 36.8 Step SR.
- LLaVA-1.5 is the weakest SEEACT model by Step SR.
- Asterisked methods use only 30 tasks per split, weakening direct comparability.
- No uncertainty or significance information appears.

### Table 3 — GPT-4V grounding comparison (p. 6)

- Fixed 30-task subset per split.
- Textual Choices is the best automatic approach.
- Oracle dominates, especially on Cross-Website.
- The table directly supports grounding as a bottleneck.
- Only Step SR is reported here; no cost or latency comparison is given.

### Table 4 — Offline and online task success (p. 6)

- Compares exact offline success, one-error-tolerant offline success, and monitored online completion.
- Oracle online = 51.1%, highest.
- Choice online = 37.8%, substantially above GPT-4 and FLAN-T5-XL.
- Online is not merely another metric on identical static traces: live pages, human monitoring, updated dates, resampling, and manual ad closing alter the evaluation environment.

### Table 5 — Annotation-markup ablation (p. 14)

| Label/location | Ele. Acc | Op. F1 | Step SR |
|---|---:|---:|---:|
| Number, bottom-left | 27.0 | 73.7 | 24.3 |
| Number, bottom-center | 23.0 | 76.4 | 21.8 |
| Single letter, bottom-left | 19.4 | 81.0 | 17.2 |
| Single letter, bottom-center | 19.7 | 78.8 | 19.7 |
| Double letter, bottom-left | 19.8 | 68.3 | 18.3 |
| Double letter, bottom-center | 22.4 | 74.6 | 22.4 |
| Number*, bottom-left* | 26.6 | 73.9 | 22.3 |

- Numeric bottom-left labels maximize Element Accuracy and Step SR.
- Single letters bottom-left maximize Operation F1 but ground elements poorly.
- Using the annotated image during action generation does not improve Step SR over the ordinary number/bottom-left condition.
- Sample size for this ablation is not stated.

### Table 6 — Action-generation prompt (p. 15)

- Specifies the system role and stepwise analysis structure.
- Requires exactly one valid next action.
- Emphasizes checking screenshots because textual history may omit state changes.
- It is methodological material, not a result table.

### Table 7 — Element-attribute prompt (p. 16)

- Adds detailed relative location, element type, exact text, action, and value.
- Restricts types to BUTTON, TEXTBOX, SELECTBOX, or LINK.
- The restricted type vocabulary may not naturally describe every DOM element; the paper does not analyze this separately.

### Table 8 — Textual-choice prompt (p. 17)

- Reiterates the target, evaluates candidate HTML choices, permits “none,” and outputs letter/action/value.
- Encourages the model to distinguish multiple matching options through screenshot reasoning.

### Table 9 — Image-annotation prompt (p. 18)

- Requires verification that the target has a red box and numbered black label.
- Explicitly instructs the model to return NA rather than invent a mark.
- Figures 10–11 show that the model frequently violates this instruction.

# 12. Diagram / Architecture Interpretation

The main architecture appears in Figure 1 and is elaborated by Figure 2.

```text
Task T + current screenshot i + previous actions
                    │
                    ▼
         LMM action generation
      textual intention ã = (ẽ, õ, ṽ)
                    │
                    ▼
           grounding mechanism
  Attributes | Text choices | Image labels | Human oracle
                    │
                    ▼
      executable action a = (e, o, v)
                    │
                    ▼
             browser event
                    │
                    ▼
         new HTML h and image i
                    └── iterative feedback to next step
```

The **data path** moves from screenshot/task/history to textual intention, then to an executable browser event. The **control path** is sequential: one action is allowed per turn. The **feedback loop** is the newly rendered webpage state.

A key design asymmetry is that action generation uses screenshot information without HTML, while automatic grounding may reintroduce DOM/HTML information. This lets the authors test whether the LMM’s visual plan is correct separately from whether it can select the exact implementation target.

# 13. Equations and Mathematical Concepts

## Equation E1 — Policy for the next action

Location: §2.1, p. 2.

\[
a_t=\pi(s_t,T,\{a_1,a_2,\ldots,a_{t-1}\})
\]

- \(a_t\): executable action at step \(t\).
- \(\pi\): the agent policy.
- \(s_t\): current environment observation.
- \(T\): natural-language task.
- \(\{a_1,\ldots,a_{t-1}\}\): action history.

Plain-language meaning: the agent chooses its next action based on what the webpage currently looks like, the user’s task, and what it has already done.

The state comprises:

\[
s_t=\{h_t,i_t\}
\]

where \(h_t\) is the HTML document and \(i_t\) is the screenshot.

## Equation E2 — State transition

Location: §2.1, p. 2.

\[
s_{t+1}=S(a_t)=\{h_{t+1},i_{t+1}\}
\]

Here \(S\) denotes the website/environment transition produced by action \(a_t\). The paper uses the same symbol \(S\) earlier for a website, so the notation is mildly overloaded.

Plain-language meaning: executing an action changes both the underlying webpage structure and the rendered image.

## Action triplet

Location: §2.1, p. 3.

\[
a=(e,o,v)
\]

- \(e\in E\): target webpage element.
- \(o\in O\): operation, such as Click or Type.
- \(v\): optional operation-specific value, such as typed text or a selected date.

The LMM first generates a textual approximation:

\[
\tilde a=(\tilde e,\tilde o,\tilde v)
\]

Action grounding converts \(\tilde a\) into executable \(a\). The paper contains no loss function, training objective equation beyond the prose description of left-to-right language modeling, theorem, or proof.

# 14. Interpretation and Discussion

[A] The authors’ core interpretation is that GPT-4V already possesses substantial webpage understanding and planning ability, but current element grounding prevents that ability from becoming reliable automation.

The evidence supports a narrower formulation:

- Under human-interpreted grounding, GPT-4V has the best reported performance.
- Automatic textual-choice grounding retains much of that advantage online but loses considerably at the step level.
- Image annotation, despite providing explicit visual marks, introduces hallucination and spatial-association failures.
- Exact offline evaluation severely underestimates live success under this monitored protocol.

[D] **Analyst interpretation:** The experiments reveal that “seeing the webpage” and “controlling the webpage” are distinct competencies. GPT-4V can frequently state a correct intention while failing the low-level binding needed for execution.

The research objectives are addressed as follows:

- **Generalist-agent potential:** supported conditionally by oracle and live results.
- **Best grounding method:** textual choices among the three tested.
- **Online/offline discrepancy:** strongly demonstrated descriptively.
- **Role of visual information:** supported by qualitative examples and GPT-4V versus text-only GPT-4, but BLIP-2’s limited gain shows that visual input alone is insufficient.
- **Long-horizon reliability:** Figure 3 indicates worsening performance with more actions.

Unresolved inconsistencies include:

1. Prose reports GPT-4V Step SR improvements of 6.8, 5.7, and 12.3 points, while Table 2 yields 7.9, 5.4, and 7.1.
2. The introduction says Choices outperforms Annotation “by up to 10%,” while Table 3 shows about 18-point differences.
3. The conclusion says a 20–25% grounding gap, while Table 3’s Cross-Website gap is 32.3 points.
4. The conclusion rounds live oracle success to “50%,” while the exact reported value is 51.1%; this is ordinary rounding rather than a substantive contradiction.

# 15. Contributions and Novelty

## Conceptual

- Decomposes multimodal web agency into visual action generation and executable grounding.
- Frames grounding, rather than high-level planning alone, as the principal bottleneck.

## Methodological

- Compares element attributes, textual choices, image annotations, and approximate oracle grounding.
- Uses screenshots for plan generation and HTML/visual correspondences for grounding.

## Dataset

- Constructs **Multimodal Mind2Web** by aligning cached HTML with screenshots and human-verifying visibility/rendering (§3.1, p. 4).

## System and implementation

- Introduces SEEACT.
- Develops a Playwright-based tool for live, multimodal evaluation (§3.4, p. 5).

## Experimental

- Compares supervised, in-context, text-only, multimodal, and coordinate-grounding approaches.
- Evaluates both cached and live environments.
- Provides task-difficulty, annotation-error, and markup-ablation analyses.

## Empirical

- Reports 51.1% live success with human grounding and 37.8% with textual-choice grounding.
- Identifies fabricated annotations and adjacent-label association as the sampled image-grounding error classes.
- Shows that online success can substantially exceed exact-trace offline success.

No novel model-training architecture, theorem, or optimization algorithm is proposed.

# 16. Limitations

## Authors’ stated limitations

The paper explicitly acknowledges:

- Fine-grained grounding remains a major challenge (§6, p. 8).
- Image annotation causes severe hallucination and spatial-label association errors (§4.3, p. 7).
- Element attributes fail when elements lack text or relevant text belongs to nearby elements (§4.1, p. 5).
- Textual choices cannot reliably distinguish identical elements (Appendix G, p. 19; Fig. 16).
- Smaller visual encoders may not capture webpage detail, and training screenshots may contain rendering or capture issues (§4.1, p. 6).
- Offline evaluation may miss alternative valid paths (§4.2, p. 7).
- Generalist web agents create privacy and harmful-action risks (§7, p. 9).
- Live evaluation required safety monitoring and prohibited consequential operations (§3.4, p. 5; Appendix C, p. 14).

## Additional evidence-based analyst observations

These are not presented by the authors as formal limitations:

- Oracle grounding depends on human interpretation and execution, so it measures an upper-bound hybrid system rather than autonomous performance.
- Some Table 2 rows use 30-task subsets while others use full splits, limiting direct comparability.
- Online evaluation has only 90 tasks and includes manual ad closing, task rewriting, resampling, and human judgments.
- No confidence intervals, repeated runs, statistical tests, or uncertainty estimates are supplied.
- No annotator agreement or blinding procedure is reported.
- API/model versions are named, but decoding settings and evaluation dates are absent.
- Candidate-grounding performance is partly conditioned on a separate ranker; ranker recall is not reported.
- The paper reports qualitative capability cases without estimating their prevalence.
- Several prose claims conflict numerically with tables.
- Live safety restrictions exclude many consequential tasks for which reliability would matter most.

# 17. Threats to Validity

## Internal validity

Human oracle implementation, manual popup closure, live-task rewriting, and resampling may affect outcomes. The paper does not report whether monitoring or judging was standardized across models.

## Construct validity

Offline exact action matching may not measure actual task completion when several paths are valid. Conversely, human-judged online completion may introduce subjectivity. “Oracle grounding” combines model intention with human interpretation rather than isolating a purely mechanical grounder.

## Statistical conclusion validity

No confidence intervals, significance tests, run-to-run variability, or power analysis are reported. Small 30-task subsets may make estimates unstable, especially when comparing percentage differences.

## External validity

Mind2Web spans many websites and domains, but online evaluation covers only 90 non-login, non-consequential tasks. Results may not generalize to authenticated workflows, financial transactions, form submissions, accessibility technologies, mobile interfaces, or websites outside the benchmark distribution.

## Ecological validity

Live evaluation improves ecological realism, yet human interception and popup removal differ from fully autonomous deployment.

## Reproducibility

The paper says code, data, and tools are available, but the supplied document alone lacks sufficient decoding parameters, timing information, API determinism controls, and detailed annotation protocols for exact reproduction.

## Safety validity

The evaluation deliberately avoids harmful actions. It therefore demonstrates a safety procedure, not autonomous safety.

# 18. Future Work and Open Questions

## A. Future work proposed by the authors

- Better exploit the known correspondence between HTML elements and rendered visuals.
- Improve grounding and reduce LMM hallucinations.
- Use online evaluation for more accurate assessment.
- Thoroughly assess and mitigate privacy and harmful-action risks (§§6–7, pp. 8–9).

## B. Additional open questions

- Can a grounder combine DOM structure, geometry, accessibility metadata, and screenshot evidence without top-50 candidate loss?
- How much of the oracle gap comes from missing ranker candidates versus incorrect final selection?
- How stable are results across model/API updates?
- Can grounding uncertainty be calibrated so the agent abstains before harmful actions?
- What is performance without manual popup handling?
- How should alternative valid paths be represented in offline benchmarks?
- How does task success change under retries, recovery budgets, or explicit verification?
- What are cost, latency, and token-use tradeoffs?
- Can identical elements be distinguished through row context, DOM ancestry, or relative geometry?
- How do safety and reliability behave on authenticated or consequential tasks under controlled simulation?

# 19. Terminology and Notation Glossary

| Term | Meaning in this paper |
|---|---|
| LLM | Large language model; principally text-oriented |
| LMM | Large multimodal model; combines language with images |
| GPT-4V | GPT-4 with visual input, the main model evaluated |
| SEEACT | The proposed multimodal web-agent framework |
| Web agent | System that performs webpage actions to satisfy a user instruction |
| Action generation | Producing a natural-language description of the next action |
| Action grounding | Converting that description to an executable browser action |
| Element grounding | Selecting the exact target webpage element |
| HTML | Markup representation underlying a webpage |
| DOM | Document Object Model; structured set/tree of webpage elements |
| Screenshot | Rendered visual state of the webpage |
| Mind2Web | Benchmark of real-world, multi-step web tasks |
| Multimodal Mind2Web | Authors’ cleaned HTML–screenshot-aligned version |
| SFT | Supervised fine-tuning |
| ICL | In-context learning from prompt demonstrations |
| Oracle grounding | Human identification/implementation of the model’s intended action |
| Textual Choices | Grounding by selecting among HTML-text candidates |
| Image Annotation | Grounding through numbered boxes over screenshot elements |
| Element Attributes | Grounding through predicted type, text, and description |
| Set-of-mark prompting | Overlaying marks on an image for visual reference |
| Cross-Task | New tasks on familiar websites/domains |
| Cross-Website | Tasks on unseen websites in familiar domains |
| Cross-Domain | Tasks in held-out top-level domains |
| Ele. Acc | Element Accuracy |
| Op. F1 | Token-level Operation F1 |
| Step SR | Step Success Rate |
| SR | Whole-task Success Rate |
| Playwright | Browser-automation framework used by the online tool |
| \(T\) | Natural-language task |
| \(s_t\) | Environment observation at time \(t\) |
| \(h_t\) | HTML state at time \(t\) |
| \(i_t\) | Screenshot at time \(t\) |
| \(a_t\) | Executable action at time \(t\) |
| \(\pi\) | Agent policy |
| \(e\) | Target element |
| \(o\) | Browser operation |
| \(v\) | Operation-specific value |
| \(\tilde a\) | Textually described, not yet grounded action |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Original benchmark scale | >2,000 | tasks | Mind2Web | Author-reported | p. 4, §3.1 |
| Websites | 137 | websites | Original Mind2Web | Author-reported | p. 4 |
| Low-/high-level domains | 31 / 12 | domains | Original Mind2Web | Author-reported | p. 4 |
| Training tasks | 1,009 | tasks | Multimodal Mind2Web | Author-reported/visually readable | p. 5, T1 |
| Cross-Domain tasks | 694 | tasks | Test split | Author-reported/visually readable | p. 5, T1 |
| Cross-Task tasks | 177 | tasks | Test split | Author-reported/visually readable | p. 5, T1 |
| Cross-Website tasks | 142 | tasks | Test split | Author-reported/visually readable | p. 5, T1 |
| Example HTML elements | 423 | elements | Figure 1 webpage | Author-reported | p. 2 |
| Example HTML tokens | 186,490 | tokens | GPT-2 tokenizer | Author-reported | p. 2 |
| Example visual tokens | 1,445 | tokens | GPT-4V tokenizer | Author-reported | p. 2 |
| GPT-4V-Oracle Step SR | 61.9 / 65.0 / 62.1 | % | Cross-Task/Website/Domain | Author-reported | p. 6, T2 |
| GPT-4V Choices Step SR | 40.2 / 32.4 / 36.8 | % | Full Table 2 rows | Author-reported | p. 6, T2 |
| Choices Step SR, matched subset | 39.1 / 32.7 / 42.0 | % | 30 tasks per split | Author-reported | p. 6, T3 |
| Oracle–Choices gaps | 22.8 / 32.3 / 20.1 | percentage points | T3 split order | Analyst-derived | 61.9−39.1; 65.0−32.7; 62.1−42.0 |
| SEEACTChoice online success | 37.8 | % | 90 live tasks | Author-reported | p. 6, T4 |
| SEEACTOracle online success | 51.1 | % | 90 live tasks | Author-reported | p. 6, T4 |
| GPT-4 online success | 13.3 | % | Same online subset | Author-reported | p. 6, T4 |
| FLAN-T5-XL online success | 8.9 | % | Same online subset | Author-reported | p. 6, T4 |
| Choice online minus Offline 0 | 34.5 | percentage points | 37.8−3.3 | Analyst-derived | p. 6, T4 |
| Oracle online minus Offline 0 | 37.8 | percentage points | 51.1−13.3 | Analyst-derived | p. 6, T4 |
| Easy/Medium/Hard samples | 37 / 35 / 18 | tasks | 1–4 / 5–9 / 10–18 actions | Author-reported | p. 7, F3 |
| Fabricated-label errors | 54 | % | 100 wrong-grounding samples | Author-reported | p. 7, §4.3 |
| Incorrect label-link errors | 46 | % | Same sample | Author-reported | p. 7, §4.3 |
| Best annotation Step SR | 24.3 | % | Number, bottom-left | Author-reported | p. 14, T5 |
| Approx. Oracle hard-task success | ~33 | % | Read from bar height | Approximate visual estimate | p. 7, F3 |
| Approx. Choice hard-task success | ~11 | % | Read from bar height | Approximate visual estimate | p. 7, F3 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| GPT-4V has substantial web-agent potential if grounded | 51.1% live success; ~62–65% Step SR | T2, T4; X2/X4 | pp. 5–7 | Strong descriptive evidence, but oracle uses humans |
| Grounding is a major bottleneck | 20.1–32.3-point Oracle–Choices gaps | T3; X3 | p. 6 | Strong within matched subsets |
| Textual Choices is the best tested automatic grounder | Highest automatic Step SR in all T3 splits | T3 | p. 6 | Strong among the three tested methods |
| Image annotation is unreliable on webpages | Low Step SR plus 54/46 error split | T3, F10–13; X6 | pp. 6–7, 26–29 | Quantitative subset plus illustrative cases |
| Online exact completion exceeds offline exact-trace scores | All models higher Online than Offline 0 | T4, F19 | pp. 6–7, 35 | Strong descriptive result; protocols differ |
| Longer tasks are harder | Bars decrease Easy→Hard | F3 | p. 7 | Clear visual trend; no uncertainty estimates |
| Grounding errors accumulate over long horizons | Oracle–Choices gap widens | F3 | p. 7 | Plausible author interpretation, not causal proof |
| Screenshots recover state missing from histories | Rental-date and return-location example | F15 | p. 31 | Qualitative case only |
| GPT-4V can plan future steps | Speaker-shopping plan | F14 | p. 30 | Qualitative evidence; execution not shown |
| GPT-4V can correct prior errors | Invalid-phone recognition | F20 | p. 36 | Qualitative evidence; final completion not shown |
| Identical HTML choices remain ambiguous | Three Schedule buttons | F16 | p. 32 | Direct structural example |
| Exact offline traces can reject valid paths | Direct link differs from two-step reference | F19 | p. 35 | Strong illustrative evidence, frequency unknown |
| ICL generalizes better than SFT | Authors’ synthesis across splits | T2 and prose | pp. 5–6 | Mixed table support; no significance tests |
| GPT-4V Choices gains 6.8/5.7/12.3 Step SR over GPT-4 | Prose statement | T2/prose | p. 6 | Weak/inconsistent: table gives 7.9/5.4/7.1 |

# 22. Very Simple Explanation

Imagine telling a computer, “Find me a cheap rental truck.” The computer first has to understand what to do—enter a location, choose dates, and click the search button. It then has to identify the exact button on the webpage. Those sound like one problem, but this paper shows they are really two.

GPT-4V was often good at the first part. It could look at a webpage screenshot, understand what had already happened, and explain the next sensible step. The hard part was turning “click Search” into a reliable click on the correct Search button. Webpages may contain hundreds of elements, repeated buttons, and tiny labels.

The researchers built SEEACT to connect GPT-4V’s visual reasoning to browser actions. Its best automatic strategy showed GPT-4V a shortlist of HTML elements and asked it to choose one. That worked better than drawing numbered boxes on the screenshot. With humans doing the grounding, the system finished 51.1% of live tasks; with its best automatic grounding, it finished 37.8%.

So the paper’s message is: the model often understands what should happen, but it still needs a much better “hand–eye coordination” system to touch the correct part of the webpage safely and reliably.

# Completeness Audit

## Inventory-based coverage

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes | Yes | Fully represented | Headline claims and numbers covered |
| §1 Introduction | Yes | Yes | Fully represented | Motivation, gap, contributions covered |
| §2 SeeAct | Yes | Yes | Fully represented | Architecture and both action stages covered |
| §2.1 Formulation | Yes | Yes | Fully represented | Equations and triplet explained |
| §2.2 Action Generation | Yes | Yes | Fully represented | Screenshot-only generation noted |
| §2.3 Action Grounding | Yes | Yes | Fully represented | All four grounding conditions covered |
| §3 Experiments | Yes | Yes | Fully represented | Dataset, methods, metrics, online tool |
| §3.1 Dataset | Yes | Yes | Fully represented | Splits and Table 1 values covered |
| §3.2 Methods | Yes | Yes | Fully represented | SEEACT, MindAct, CogAgent covered |
| §3.3 Offline Evaluation | Yes | Yes | Fully represented | All metrics defined |
| §3.4 Online Evaluation | Yes | Yes | Fully represented | Safety and browser protocol covered |
| §4 Results and Analysis | Yes | Yes | Fully represented | Main quantitative and qualitative findings |
| §4.1 Offline results | Yes | Yes | Fully represented | T2–T3 and inconsistencies covered |
| §4.2 Online results | Yes | Yes | Fully represented | T4 and protocol covered |
| §4.3 Analysis | Yes | Yes | Fully represented | Difficulty and 100-error analysis covered |
| §4.4 Case study | Yes | Yes | Fully represented | Planning, knowledge, correction summarized |
| §5 Related Work | Yes | Yes | Represented in compressed form | Categories and positioning retained; individual citations compressed |
| §6 Conclusion | Yes | Yes | Fully represented | Claims, rounding, future direction covered |
| §7 Impact Statements | Yes | Yes | Fully represented | Privacy, harmful actions, license intent |
| Acknowledgments | Yes | No | Deliberately omitted as non-substantive | Funding and thanks do not alter method/results |
| References, pp. 9–12 | Yes textually; pages 9, 11–12 not visually rendered | Partly | Deliberately compressed | Used only to describe related-work categories; citations not externally verified |
| Appendix contents page | Yes textually; not visually rendered | Yes | Represented in compressed form | Appendix A–I inventory supplied |
| Appendix A | Yes | Yes | Fully represented | Model/checkpoint details |
| Appendix B | Yes | Yes | Fully represented | Table 5 ablation |
| Appendix C | Yes | Yes | Fully represented | Live procedure and manual handling |
| Appendix D | Yes | Yes | Fully represented | Tables 6–9 |
| Appendix E | Yes | Yes | Fully represented | Figures 10–13 |
| Appendix F | Yes | Yes | Fully represented | Figures 14–15 |
| Appendix G | Yes | Yes | Fully represented | Figure 16 |
| Appendix H | Yes | Yes | Fully represented | Figures 17–18 |
| Appendix I | Yes | Yes | Fully represented | Figures 19–20 |
| Figure 1 | Yes, visual | Yes | Fully represented | Architecture |
| Figure 2 | Yes, visual | Yes | Fully represented | Grounding comparison |
| Figure 3 | Yes, visual | Yes | Fully represented | Exact labels separated from estimates |
| Figures 4–9 | Yes, visual | Yes | Fully represented | Prompt/grounding examples |
| Figures 10–13 | Yes, visual | Yes | Fully represented | Error cases |
| Figures 14–20 | Yes, visual | Yes | Fully represented | Capability/failure cases |
| Tables 1–5 | Yes, visual | Yes | Fully represented | Values and caveats included |
| Tables 6–9 | Yes, visual | Yes | Fully represented | Prompt structure summarized |
| Equation E1 | Yes | Yes | Fully represented | Policy equation |
| Equation E2 | Yes | Yes | Fully represented | State transition |
| Action triplet | Yes | Yes | Fully represented | \(a=(e,o,v)\) |
| Formal algorithms | Not applicable | Not applicable | None in document | No pseudocode block |
| Formal RQs/hypotheses | Yes | Yes | None stated | Objectives kept informal |
| Author-stated limitations | Yes | Yes | Fully represented | Separated from analyst observations |
| Supplied supplementary material | Not applicable | Not applicable | None supplied | No separate supplement |

## Missing or inaccessible material

- No pages of the main paper are missing.
- Pages 8, 9, and 11–13 were available as extracted text but not as rendered images. They contain related work, conclusion, impact statement, references, and the appendix contents page; no substantive figure or results table was thereby left visually uninspected.
- The repository, project website, dataset files, evaluation code, model checkpoints, and cited papers were referenced but not supplied and were not inspected.
- Fine-grained text within some webpage screenshots is too small to audit exhaustively. Enlarged insets, captions, and surrounding text were sufficient for their substantive examples.
- No separate supplementary material was supplied.

## Uncertain interpretations

- Figure 3 bar heights are approximate because exact values are not labeled.
- The meaning of “up to 10%” improvement over image annotation is unresolved because Table 3 shows approximately 18-point Step-SR differences.
- The prose’s 6.8%, 5.7%, and 12.3% GPT-4V-over-GPT-4 Step-SR gains do not match Table 2.
- The conclusion’s “20–25%” oracle gap does not cover Table 3’s 32.3-point Cross-Website gap.
- The exact sample size and split used for Table 5’s markup ablation are not specified.
- The notation \(S\) appears to denote both a website and a state-transition function.

## Deliberately compressed material

- Individual bibliographic references were compressed into related-work categories because external citation validation was prohibited and the references do not add new experimental evidence.
- Repetitive prompt language in Tables 6–9 was summarized by functional requirement rather than reproduced verbatim.
- Figures 4–9 reuse the same Thumbtack task to demonstrate different grounding formats; their repeated action-generation prose was compressed while preserving each method’s distinct representation.
- Acknowledgments and line-by-line funding details were omitted as non-substantive to the research claims.

## Potential omissions

No known substantive section, subsection, experiment, figure, table, major equation, contribution, author-stated limitation, or appendix item from the inventory is absent from the analysis. The only deliberate omissions are bibliographic repetition, acknowledgments, and repeated prompt wording, all disclosed above.