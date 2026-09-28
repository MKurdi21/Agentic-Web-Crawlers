# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible page range | All 27 PDF pages, corresponding to proceedings pages 6864–6890 |
| Apparently missing pages | None |
| Native/extracted text | Available for all 27 pages |
| Visually rendered pages | 24 of 27: PDF pages 1–9 and 13–27 |
| Pages not visually rendered | PDF pages 10–12, containing the ethics statement, references, and no numbered substantive figures or tables |
| Figures visually available | Yes. Figures 1–28 are visible on rendered pages |
| Tables readable | Yes. Tables 1–4 are present in extracted text and rendered pages; Table 1 is dense but its entries are recoverable |
| Equations readable | Partially. The three interaction equations in §3.2 are readable, but the PDF extraction loses some typographic spacing and displays an apparent duplicated word (“The the model”) |
| Algorithms/pseudocode | No formal numbered algorithm is present |
| Appendices | Appendices A–F are present on PDF pages 13–27 |
| Supplementary material | No separate supplementary file was supplied |
| Referenced external artifacts | A code/data repository, Selenium, GPT-4V-Act, the OpenAI Assistant API, and cited datasets/services are referenced but were not supplied as artifacts |
| OCR needed | No. Native text was adequate; visual inspection was used for figures and tables |
| Other limitations | Many appendix trajectory screenshots contain very small webpage text. Their action labels and captions are readable, but not every underlying webpage detail can be independently verified at full fidelity from the rendered pages. The paper reports that code and data “will be released,” but the repository contents were not inspected. |

Evidence labels used below:

- **[A] Author-reported:** stated in the paper’s text, captions, tables, footnotes, or appendices.
- **[B] Directly observable:** visible in a supplied figure, diagram, or table.
- **[C] Analyst-derived:** computed from supplied values, with operands shown.
- **[D] Analyst interpretation:** an inference rather than an explicit author claim.
- No external information is introduced.

# 1. Plain-Language Orientation

WebVoyager is a web-browsing agent built around a **large multimodal model (LMM)**—a model that processes both images and text. Given a natural-language task, it opens a real website, observes a screenshot plus short descriptions of interactive elements, reasons about the next step, and performs actions such as clicking, typing, scrolling, or returning an answer (§§1, 3; Figures 1–2).

The paper addresses two linked problems:

1. Earlier web agents often operated on text-only representations, simplified simulators, static snapshots, or prescribed “golden” action paths.
2. Real web tasks can have many valid routes and open-ended answers, making step-by-step matching an incomplete evaluation method (§1).

The authors therefore contribute:

- the WebVoyager agent;
- a 643-task benchmark spanning 15 live websites;
- a trajectory-level automatic evaluation procedure using GPT-4V;
- experiments against GPT-4 (All Tools), a text-only WebVoyager configuration, GAIA tasks, and SeeAct tasks;
- an error taxonomy based on 300 sampled tasks.

The principal author-reported result is a **59.1% human-evaluated task-success rate** on the new benchmark, versus **40.1%** for text-only WebVoyager and **30.8%** for GPT-4 (All Tools) (p. 7, Table 1). The full-trajectory GPT-4V evaluator agrees with consolidated human judgments on **85.3%** of 300 evaluated tasks and has **Cohen’s κ = 0.70** (p. 7, Table 2).

The central contribution is not merely using screenshots. It is the integration of real-web interaction, screenshot-based visual grounding, element-associated text, a compact browser action language, a diverse live-site benchmark, and outcome-oriented trajectory evaluation.

# 2. Document Roadmap

The paper is organized as follows:

1. **Abstract and Introduction** (pp. 1–2): motivate multimodal, end-to-end web navigation and summarize contributions and headline results.
2. **Related Work** (pp. 2–3): position WebVoyager against simulators, text-based agents, screenshot-only agents, and contemporaneous multimodal agents.
3. **WebVoyager** (pp. 3–4):
   - §3.1 browsing environment;
   - §3.2 interaction formulation;
   - §3.3 observation space;
   - §3.4 action space.
4. **Benchmark for WebVoyager** (pp. 4–5):
   - §4.1 website selection;
   - §4.2 task construction;
   - §4.3 answer annotation.
5. **Experiment** (pp. 5–9):
   - datasets, metric, and implementation details;
   - §5.1 human and automatic evaluation;
   - §5.2 main results;
   - §5.3 discussion;
   - §5.4 error analysis.
6. **Conclusion, Limitations, and Ethics Statement** (pp. 9–10).
7. **References** (pp. 10–12).
8. **Appendices A–F** (pp. 13–27):
   - A: agent prompt;
   - B: automatic-evaluator prompt;
   - C: detailed action definitions;
   - D: successful trajectories;
   - E: additional related work;
   - F: representative error cases.

# 3. Background and Context

A **web agent** is a system that interprets a user instruction and operates a browser to accomplish it. Successful navigation may require planning, understanding webpage structure, selecting controls, entering information, and recognizing when the task is finished (§2).

Several representations are relevant:

- **HTML (HyperText Markup Language):** the structural source of a webpage.
- **DOM (Document Object Model):** a tree representation of the webpage’s elements.
- **Accessibility tree:** a textual, accessibility-oriented representation of controls and content.
- **Screenshot:** the browser’s rendered visual output.
- **Visual grounding:** associating an intended action with the correct visible interface element.
- **Set-of-Mark prompting:** marking candidate interface elements with numbered labels so the model can refer to them unambiguously (§3.3).
- **ReAct prompting:** eliciting a reasoning or “Thought” before an “Action” (§3.2).
- **Task Success Rate:** the fraction of tasks judged successfully completed; it does not reward shorter or otherwise optimal action paths (§5).

The paper’s central representational argument is that webpages are designed for human visual use. Flattening them into long HTML or accessibility-tree text can obscure spatial organization, while screenshots can preserve layout and visual grouping. Conversely, screenshots can make dense small text difficult to recognize. WebVoyager therefore combines screenshots with auxiliary element text (§§1, 3.3, 5.2–5.3).

For evaluation, the paper distinguishes:

- **stepwise/offline evaluation:** comparing predicted actions with one predefined trajectory;
- **end-to-end evaluation:** judging whether the final task was completed, regardless of which valid route the agent followed (§1);
- **human evaluation:** humans inspect all actions and screenshots;
- **automatic multimodal evaluation:** an LMM inspects the instruction, response, and screenshots (§5.1).

# 4. Research Problem and Gap

## Existing problem

Real websites are dynamic and difficult to automate. They contain pop-ups, advertisements, changing content, calendars, small controls, nested scroll areas, and multiple possible paths to the same answer (§3.1).

## Shortcomings attributed to previous approaches

According to the authors:

- text-based systems must process complex and verbose HTML;
- simulator-based studies do not capture all live-web difficulties;
- static snapshots do not test sustained interaction;
- screenshot-only or single-modality approaches omit useful information;
- stepwise evaluation against one golden trajectory penalizes alternative valid plans;
- the strongest contemporaneous SeeAct configuration still uses a separate fine-tuned cross-encoder to select candidate elements (§§1–2).

## Research gap

The paper identifies a need for a unified system that:

- operates on the open web;
- uses visual and textual observations;
- completes tasks end-to-end without intermediate human intervention;
- does not require a separately trained visual element selector;
- can be evaluated fairly when multiple action paths or answers are valid.

## Motivation

A practical web agent should work with the same rendered environment humans encounter and should access current web information. It should also be evaluated by task completion rather than imitation of one reference path (§§1, 3.1).

## Scope

The study covers non-login, non-CAPTCHA information-seeking and interaction tasks on 15 sites. The action space omits some human browser actions, including dragging. The agent supports basic text and PDF file analysis, but not all file types or video (pp. 9–10, Limitations).

# 5. Research Questions / Objectives / Hypotheses

The paper does not state formal numbered research questions or hypotheses.

Its explicit and implicit objectives are:

- **O1 [A]:** Build an LMM-powered agent that completes open-web tasks autonomously from start to finish (§§1, 3).
- **O2 [A]:** Determine whether combining screenshots and textual element information improves task success over text-only input (§§1, 5.2–5.3).
- **O3 [A]:** Create a diverse benchmark of real-world tasks across representative websites (§4).
- **O4 [A]:** Test whether GPT-4V can evaluate complete web trajectories with substantial agreement with humans (§§1, 5.1–5.2).
- **O5 [A]:** Characterize important sources of failure (§5.4).
- **O6 [A]:** Test generalization on GAIA, the SeeAct online task set, and two non-English trajectory examples (§5 and Appendix D).

No preregistered hypothesis, statistical null hypothesis, or significance threshold is reported.

# 6. Assumptions / Threat Model

This is not a security experiment with a formal attacker model. Its operational assumptions are:

- Websites are accessed live through Selenium (§3.1).
- Interactive elements can generally be identified from their web-element types and marked with labels (§3.3).
- A screenshot plus auxiliary element text contains enough information for the model to choose actions.
- Only the three most recent webpage observations need be retained; all prior thoughts and actions remain in context (§3.2).
- A maximum of 15 steps is sufficient for the evaluated tasks (§5).
- Tasks requiring login or CAPTCHA are excluded (§4.1).
- When CAPTCHA blocks access, the agent should seek alternative sources rather than bypass it (p. 3, footnote 4).
- All interactions remain in one browser tab (§3.3).
- For auto-evaluation, screenshots are treated as authentic. If response text conflicts with a screenshot, the screenshot prevails; if the response adds information absent from the screenshot, the evaluator prompt directs the model to believe it (p. 15, Figure 8).

Safety-relevant assets and risks identified by the authors include confidential information, unauthorized or malicious downloads, fake server requests, and fake user activity (p. 10). Their safeguards are restricting tasks to non-login activity, monitoring online evaluations, and manually checking task queries for harmful content.

# 7. Methodology

## 7.1 Study design

This is a combined **AI systems, benchmark, and empirical evaluation paper**. It implements an agent, constructs an evaluation dataset, evaluates several configurations, validates an automatic evaluator, and conducts qualitative and quantitative error analysis.

## 7.2 System architecture and interaction cycle

At each step:

1. Selenium presents the current live webpage.
2. A rule-based JavaScript tool extracts interactive elements.
3. The system overlays black boxes and numerical tags on those elements.
4. The agent receives:
   - the current screenshot;
   - element type and text;
   - possible `aria-label` comments;
   - recent observations;
   - full thought/action history.
5. The backbone LMM produces a natural-language thought and one action.
6. The action executes.
7. The resulting observation returns to the model.
8. The loop ends on `ANSWER` or at the 15-step limit (§§3.1–3.4; Figures 1–2, 7).

Execution errors are included in the next prompt so the model can retry, but each retry consumes one step (§3.3).

## 7.3 Observation design

Screenshots are the primary input. Text supplements the screenshot rather than replacing it. Numerical labels provide a stable pointer from model output to webpage controls.

The authors report choosing black borders and label backgrounds empirically because a single black color yielded higher success than multicolor labeling (§3.3). No numeric ablation supporting this observation is reported.

## 7.4 Action space

The supported actions are:

| Action | Function | Exact appendix format |
|---|---|---|
| Click | Activate a link or button | `Click [Numerical_Label]` |
| Input | Select field, clear it, type content, then press Enter | `Type [Numerical_Label]; [Content]` |
| Scroll | Scroll the window or a selected scrollable region | `Scroll [Numerical_Label or WINDOW]; [up or down]` |
| Wait | Allow loading | `Wait` |
| Back | Return to previous page | `GoBack` |
| Jump to search | Restart from Google Search | `Google` |
| Answer | Finish and report the result | `ANSWER; [Content]` |

If a clicked link downloads a PDF, its contents are parsed through the OpenAI Assistant API and added to the observation (Appendix C, p. 13).

## 7.5 Benchmark construction

The benchmark includes 15 sites: Allrecipes, Amazon, Apple, ArXiv, BBC News, Booking, Cambridge Dictionary, Coursera, ESPN, GitHub, Google Flights, Google Map, Google Search, Huggingface, and Wolfram Alpha (§4.1).

Construction proceeds in three stages (Figure 3):

1. Humans sample and rewrite seed tasks from Mind2Web for several sites.
2. GPT-4 Turbo generates about 100 tasks over 20 iterations from in-context seeds; humans verify and revise them.
3. More varied Task Pool examples are used for additional generation; humans check answer availability and repetition.

The final dataset contains **643 tasks**, with **40–45 tasks per website** (§4.2; Table 1 caption).

For diversity checking, all-mpnet-base-v2 computes pairwise similarity among the 643 questions:

- 206,403 pairs total;
- 49 pairs above 0.8 similarity;
- 140 pairs between 0.7 and 0.8;
- the authors state that all such pairs were manually checked and accepted;
- 99.68% of pairs are reported below 0.6 similarity (§4.2).

## 7.6 Answer annotation

Answers are labeled:

- **Golden:** a comprehensive set of responses considered stable in the short term.
- **Possible:** used for open-ended tasks, tasks with multiple acceptable answers, or real-time answers that may change (§4.3).

Only **22.3%** of tasks have Golden answers; the remaining **77.7% [C]** have Possible answers (`100 − 22.3 = 77.7` percentage points).

## 7.7 Models and configurations

The main backbone is GPT-4 Turbo with vision (`gpt-4-vision-preview`), treated by the authors as equivalent to GPT-4V for this study (§5).

Additional backbone experiments use:

- Claude 3 Opus;
- GPT-4o.

Baselines are:

- GPT-4 (All Tools);
- text-only WebVoyager, which receives the accessibility tree.

## 7.8 Experimental parameters

- browser viewport: **1024 × 768 pixels**;
- generation temperature: **1**;
- maximum trajectory: **15 steps**;
- GPT-4V evaluator temperature: **0**;
- automatic evaluator inputs: task, final response, and last `k` screenshots, with `k = 1, 2, 3`, or the full trajectory;
- automatic evaluation repeated three times for means and standard deviations in Table 1 (§5; Appendix B).

No hardware specification, runtime, inference cost, browser/driver version, model snapshot date beyond model names, random seed, or statistical significance test is reported.

## 7.9 Evaluation datasets and metrics

Evaluation uses:

- the new 643-task benchmark;
- 90 GAIA Level 1 and Level 2 web tasks;
- 50 SeeAct online-evaluation tasks (§5).

The main metric is binary **Task Success Rate**. Human evaluators inspect complete trajectories. Three annotators independently judge a 300-task subset; their pre-discussion Fleiss’s κ is **0.70** (p. 6, footnote 7).

# 8. Experiments / Analyses

## X1 — Main benchmark comparison

**Purpose:** Compare multimodal WebVoyager against GPT-4 (All Tools) and text-only WebVoyager.

**Data:** 643 tasks, 15 sites, 40–45 tasks per site.

**Metric:** Human-evaluated Task Success Rate.

**Result:** Overall success is 59.1% for WebVoyager, 40.1% for text-only WebVoyager, and 30.8% for GPT-4 (All Tools) (Table 1).

**Caveat:** The benchmark contains mostly Possible rather than fixed Golden answers, so judgment depends on trajectory-level human assessment.

## X2 — Per-website comparison

**Purpose:** Determine where vision and direct interaction help or struggle.

WebVoyager’s human-evaluated success rates range from **38.6% on ESPN** to **76.7% on Google Search**. It exceeds both listed baselines on 13 of 15 sites. Exceptions:

- Allrecipes: 53.3%, below text-only’s 55.6%;
- ESPN: 38.6%, above text-only’s 36.4% but below neither? It still exceeds both baselines; the prose describes it as “similar” to text-only.

GitHub, Cambridge Dictionary, and Wolfram Alpha show relatively small multimodal/text-only gaps. The authors associate these cases with text-heavy pages (§5.2).

## X3 — GAIA evaluation

**Purpose:** Assess performance outside the newly constructed benchmark.

**Data:** 90 Level 1 and Level 2 GAIA web tasks, beginning from Google Search.

**Results (Figure 5):**

| System | Level 1 | Level 2 |
|---|---:|---:|
| GPT-4V (All Tools) | 23.1% | 12.5% |
| WebVoyager text-only | 19.2% | 12.5% |
| WebVoyager | 38.5% | 15.6% |

The gain is much larger on Level 1 than Level 2.

## X4 — SeeAct task-set comparison

**Purpose:** Compare WebVoyager with a contemporaneous autonomous visual web agent.

**Data:** 50 SeeAct online-evaluation tasks.

**Result:** WebVoyager obtains 30% versus 26% for the best SeeAct autonomous agent (§5.2).

No uncertainty interval or paired-task significance analysis is provided.

## X5 — GPT-4V evaluator validation

**Purpose:** Test whether an LMM can replace or supplement expensive human trajectory evaluation.

**Data:** 300 tasks with consolidated human labels.

**Conditions:** last 1, 2, or 3 screenshots, or full trajectory.

**Results (Table 2):**

| Input | GPT-4V success rate | Human agreement | Cohen’s κ |
|---|---:|---:|---:|
| `k=1` | 47.7% | 75.3% | 0.51 |
| `k=2` | 55.3% | 79.7% | 0.59 |
| `k=3` | 54.3% | 81.3% | 0.62 |
| Full | 58.3% | 85.3% | 0.70 |

More trajectory context monotonically improves agreement and κ, although the evaluator’s own success-rate estimate falls slightly from 55.3% at `k=2` to 54.3% at `k=3`.

## X6 — Evaluator/backbone cross-comparison

**Purpose:** Test whether automatic success estimates depend on the evaluator model and whether evaluators favor their own outputs.

Table 3 crosses three agent backbones with three evaluators:

| Agent backbone | GPT-4V evaluator | Claude-3-Opus evaluator | GPT-4o evaluator |
|---|---:|---:|---:|
| GPT-4V | 57.1 | 55.1 | 63.0 |
| Claude-3-Opus | 52.8 | 61.6 | 55.4 |
| GPT-4o | 55.5 | 54.9 | 64.1 |

The paper reports κ with humans of 0.60 for Claude-3-Opus and 0.72 for GPT-4o, versus 0.70 for GPT-4V. The authors interpret GPT-4o as more lenient, GPT-4V as stricter, and Claude as displaying a pronounced preference for its own trajectories (§5.2).

## X7 — Website complexity analysis

**Purpose:** Relate success to average completed-trajectory length and average number of interactive elements.

**Evidence:** Figure 6 plots one point per website. Color encodes success.

**Result:** The authors say websites toward the lower-left—shorter trajectories and fewer elements—generally have higher success (§5.3). This is descriptive; no correlation coefficient, fitted regression, or significance test is supplied.

## X8 — Error analysis

**Purpose:** Classify major failures.

**Data:** 300 sampled benchmark tasks; categories were manually assigned to failed cases.

**Distribution (Table 4):**

- Navigation Stuck: 44.4%;
- Visual Grounding Issue: 24.8%;
- Hallucination: 21.8%;
- Prompt Misalignment: 9.0%.

These sum to **100.0% [C]**. Appendix F supplies one visual example per category.

# 9. Results

## 9.1 Main overall result

WebVoyager achieves **59.1%**, compared with **40.1%** for text-only and **30.8%** for GPT-4 (All Tools) (p. 7, Table 1).

Derived comparisons:

- versus text-only: **+19.0 percentage points [C]** (`59.1 − 40.1`);
- relative increase over text-only: **47.4% [C]** (`19.0 / 40.1 × 100`);
- versus GPT-4 (All Tools): **+28.3 percentage points [C]** (`59.1 − 30.8`);
- relative increase over GPT-4 (All Tools): **91.9% [C]** (`28.3 / 30.8 × 100`).

The paper uses “significantly outperforming” informally; no statistical significance test is reported.

## 9.2 Website-level results

Human-evaluated Table 1 results are:

| Website | GPT-4 All Tools | Text-only | WebVoyager |
|---|---:|---:|---:|
| Allrecipes | 11.1% | **55.6%** | 53.3% |
| Amazon | 17.1% | 31.7% | **58.5%** |
| Apple | 44.2% | 34.9% | **65.1%** |
| ArXiv | 14.0% | 32.6% | **51.2%** |
| GitHub | 48.8% | 61.0% | **63.4%** |
| Booking | 22.7% | 2.3% | **43.2%** |
| ESPN | 31.8% | 36.4% | **38.6%** |
| Coursera | 31.0% | 23.8% | **73.8%** |
| Cambridge Dictionary | 25.6% | 62.8% | **65.1%** |
| BBC News | 9.5% | 45.2% | **61.9%** |
| Google Flights | 2.4% | 7.1% | **59.5%** |
| Google Map | 53.7% | 61.0% | **70.7%** |
| Google Search | 60.5% | 67.4% | **76.7%** |
| Huggingface | 37.2% | 20.9% | **44.2%** |
| Wolfram Alpha | 52.2% | 58.7% | **63.0%** |
| Overall | 30.8% | 40.1% | **59.1%** |

The largest multimodal-over-text-only gap is on Google Flights: **52.4 percentage points [C]** (`59.5 − 7.1`). Booking also shows a large **40.9-point [C]** difference (`43.2 − 2.3`). These support the authors’ claim that vision helps with calendars and complex graphical controls.

## 9.3 Automatic-evaluation results

The GPT-4V full-trajectory evaluator produces overall means of:

- text-only: 44.3% ± 0.6%;
- GPT-4V-backed WebVoyager: 57.1% ± 0.2%;
- Claude-backed WebVoyager: 52.8% ± 1.4%;
- GPT-4o-backed WebVoyager: 55.5% ± 0.8% (Table 1).

These are automatic estimates, not the principal human labels.

## 9.4 Context improves evaluator alignment

Full trajectories yield 85.3% agreement and κ = 0.70, compared with 75.3% and κ = 0.51 from one screenshot (Table 2). The evidence supports the narrower conclusion that more trajectory evidence improves this evaluator’s correspondence with these consolidated human labels.

## 9.5 Backbone-specific failure on Google Flights

Under GPT-4V automatic evaluation:

- GPT-4V backbone: 51.6% ± 1.4%;
- Claude backbone: 15.1% ± 5.5%;
- GPT-4o backbone: 28.6% ± 0.0% (Table 1).

The authors attribute GPT-4o’s decline to failure to set “one way” correctly and Claude’s decline to element-interaction difficulty. These are trajectory-review interpretations, not controlled causal tests (§5.2).

## 9.6 Failure composition

Navigation getting stuck is the largest category at 44.4%, followed by visual grounding at 24.8%, hallucination at 21.8%, and prompt misalignment at 9.0% (Table 4).

# 10. Figure-by-Figure Interpretation

## Figure 1 — Overall WebVoyager workflow

- **Type:** architecture/workflow diagram.
- **Contains:** user query, observation, thought, action, browser, available websites, screenshot, and textual web-element descriptions.
- **Flow:** user sends a query; browser returns screenshot and element text; the model reasons; one action executes; observations cycle back until an answer is returned.
- **Example:** finding a two-year PS4 protection price of `$30.99`.
- **Support:** establishes the iterative perception–reasoning–action loop.
- **Status:** diagram structure and labels are visually readable [B]; example value is caption-reported [A].

## Figure 2 — Labeled webpage screenshot

- **Type:** annotated browser screenshot.
- **Contains:** black bounding boxes and numerical tags over interactive elements.
- **Purpose:** demonstrate Set-of-Mark-style grounding.
- **Observation:** multiple interface regions, including navigation controls and form fields, receive numbered labels [B].
- **Caveat:** the screenshot is illustrative, not a quantitative accuracy test.

## Figure 3 — Benchmark construction flow

- **Type:** multi-stage flowchart.
- **Stages:** human-written seeds → GPT-4 generation → manual quality filtering → Task Pool → further generation and online answer checking → final tasks.
- **Feedback:** generated, validated tasks return to the pool as in-context examples.
- **Support:** makes clear that the dataset is semi-automatic rather than wholly synthetic.
- **Caveat:** exact counts at each filtering stage are not shown.

## Figure 4 — Successful Apple trajectory

- **Type:** six-step screenshot sequence.
- **Task:** locate Smart Folio for iPad pickup near ZIP 90038.
- **Actions:** click Accessories; type product; click result; select Apple Valley Fair; enter ZIP; answer.
- **Outcome:** “Apple Tower Theatre.”
- **Purpose:** concrete example of end-to-end interaction and labeled-element selection.
- **Caveat:** the caption asserts correctness; the small screenshot text is not independently readable in every detail.

## Figure 5 — GAIA task success

- **Type:** grouped bar chart.
- **X-axis:** GAIA Level 1 and Level 2.
- **Y-axis:** Task Success Rate (%), linear scale from 0 to 40.
- **Series:** GPT-4V (All Tools), text-only WebVoyager, multimodal WebVoyager.
- **Exact labels:** Level 1 = 23.1%, 19.2%, 38.5%; Level 2 = 12.5%, 12.5%, 15.6%.
- **Conclusion:** multimodal WebVoyager leads on both levels; all systems are considerably lower on Level 2.
- **Status:** values are visually readable [B] and caption/text-supported [A].

## Figure 6 — Website factors related to success

- **Type:** scatterplot.
- **X-axis:** average trajectory length, approximately 3–10.
- **Y-axis:** average number of elements per step, approximately 20–70+.
- **Color:** Task Success Rate, about 30–80, with darker red representing higher success.
- **Points:** one labeled point per website.
- **Observations:** Booking lies at high trajectory length and high element count; ESPN has very high elements per step; several high-success sites occupy lower or middle complexity regions.
- **Conclusion:** the authors report broad alignment between lower interaction complexity and greater success.
- **Caveat:** no formal trend line or coefficient is reported; exact coordinates are not labeled and are therefore only approximate visual estimates.

## Figure 7 — WebVoyager system prompt

- **Type:** prompt excerpt.
- **Contains:** observation description, allowed actions, strict formats, one-action-per-step rule, generic browsing guidance, and mandatory `Thought`/`Action` response structure.
- **Purpose:** constrain model outputs into executable browser commands.
- **Caveat:** ellipses show that the displayed prompt is abbreviated.

## Figure 8 — GPT-4V evaluator prompt

- **Type:** prompt excerpt.
- **Inputs:** web task instruction, result screenshots, final response.
- **Decision:** `SUCCESS` or `NOT SUCCESS`.
- **Important rules:** do not browse; do not assume unseen facts; require completion of every subtask; prefer screenshot over contradictory response; accept response-only information if no screenshot contradiction exists.
- **Caveat:** the last rule creates an evidentiary asymmetry that can allow unsupported response text to be accepted.

## Figures 9–24 — Successful trajectory gallery

These figures primarily demonstrate breadth across sites and languages. Each consists of ordered screenshots with action captions.

| Figure | Site/task | Steps | Caption-reported outcome |
|---|---|---:|---|
| 9 | Allrecipes baked salmon | 6 | Baked Dijon Salmon; 4.6 stars; 15 minutes |
| 10 | Amazon green Xbox controller | 3 | Velocity Green controller; 4.7/5 |
| 11 | ArXiv non-English abstract separator | 7 | separator line `"-----"` |
| 12 | BBC Music News headline | 3 | Taylor Swift |
| 13 | Booking, Jakarta hotel | 9 | OYO 3755 Sweet Home; US$14/three nights |
| 14 | Cambridge Dictionary animal quiz | 12 | 6/6 |
| 15 | Coursera finance course | 5 | Xi Yang and two other courses |
| 16 | ESPN NBA teams | 5 | 30 teams; New York Knicks and New Orleans Pelicans |
| 17 | GitHub climate-data project | 5 | `resource-watch/resource-watch`; 63 stars |
| 18 | Google Map airport route | 4 | MA-1A S; approximately 8 minutes |
| 19 | Google Flights price graph | 11 | generic statement that two-month trends were analyzed |
| 20 | Google Search comedy films | 5 | five listed films |
| 21 | Huggingface model/license search | 6 | `replit/replit-code-v1-3b`; 703 likes |
| 22 | Wolfram Alpha simplification | 3 | `(x−4)^5 + 3(x−4)^3 + 7` |
| 23 | Chinese Google Flights task | 8 | 17:35; Shenzhen Airlines; HK$2,680 |
| 24 | Spanish dictionary task | 3 | pronunciation, noun gender, and sustainability definition |

Important caveats:

- These are selected success examples, not a representative performance sample.
- Figure 19’s response says only that trends were analyzed; it does not state the trends. On the face of the supplied caption, this answer appears less informative than the instruction requests. The paper nevertheless presents it as a successful example. This is a caption–task tension, not enough evidence to overturn the authors’ classification.
- Figure 23 describes a requested “night” departure but reports 17:35. Whether that satisfies the original Chinese instruction is not discussed.
- Underlying web facts can be time-sensitive.

## Figure 25 — Google Flights visual-grounding failure

- **Task:** lowest one-way JFK–Heathrow fare on January 22.
- **Observed failure:** selects December 22 rather than January 22 and fails to correct it.
- **Purpose:** show calendar-label confusion and incorrect element selection.

## Figure 26 — Allrecipes navigation-stuck failure

- **Task:** find a highly rated Beef Wellington recipe and list ingredients.
- **Trajectory:** repeated downward and upward scrolling.
- **Failure:** cannot locate the relevant ingredient section before the step budget is exhausted.
- **Purpose:** show uncertainty about scroll direction and region.

## Figure 27 — Coursera hallucination/incomplete-answer failure

- **Task:** report course duration and total quizzes across assessments.
- **Response:** reports only that Module 1 has three quizzes.
- **Failure:** omits other modules and course duration.
- **Purpose:** demonstrate a plausible but incomplete answer.

## Figure 28 — BBC prompt-misalignment failure

- **Task:** give Scottish Premiership team count and the latest Hibernian match start time.
- **Response:** gives 12 teams but tells the user further interaction is needed for the start time.
- **Failure:** terminates while explicitly acknowledging incompleteness.
- **Purpose:** illustrate premature `ANSWER`.

# 11. Table-by-Table Interpretation

## Table 1 — Main benchmark results

- **Rows:** systems/backbones, with human-evaluated rows first and automatically evaluated starred rows below.
- **Columns:** 15 websites plus overall success.
- **Unit:** percent Task Success Rate.
- **Human-evaluated overall best:** WebVoyager, 59.1%.
- **Human-evaluated overall worst:** GPT-4 (All Tools), 30.8%.
- **Website exceptions:** text-only narrowly leads multimodal WebVoyager on Allrecipes.
- **Automatic rows:** report mean ± standard deviation across three GPT-4V-evaluator runs.
- **Important note:** starred and unstarred rows use different evaluation sources and should not be treated as identical measurements.
- **No significance markers:** the table does not report hypothesis tests or confidence intervals.

## Table 2 — GPT-4V/human consistency

- **Rows:** number of screenshots supplied (`k=1`, `2`, `3`, full).
- **Columns:** evaluator success estimate, raw agreement, Cohen’s κ.
- **Best alignment:** full trajectory, 85.3% and κ = 0.70.
- **Worst alignment:** one screenshot, 75.3% and κ = 0.51.
- **Interpretation:** richer evidence improves agreement.
- **Caveat:** raw agreement can be affected by class balance; κ partly adjusts for chance agreement.

## Table 3 — Agent backbone × evaluator

- **Rows:** GPT-4V, Claude-3-Opus, and GPT-4o as WebVoyager backbones.
- **Columns:** the same three models as evaluators.
- **Highest entry:** 64.1, GPT-4o evaluated by GPT-4o.
- **Lowest entry:** 52.8, Claude trajectories evaluated by GPT-4V.
- **Self-evaluation pattern:** every evaluator gives its own backbone its column-highest score:
  - GPT-4V column: GPT-4V backbone 57.1;
  - Claude column: Claude backbone 61.6;
  - GPT-4o column: GPT-4o backbone 64.1.
- **Interpretation:** evaluator identity materially affects estimated performance.
- **Caveat:** Table 3 has no uncertainty measures.

## Table 4 — Failure categories

- **Rows:** Navigation Stuck, Visual Grounding Issue, Hallucination, Prompt Misalignment.
- **Unit:** percentage of classified failures in the sampled analysis.
- **Largest:** Navigation Stuck, 44.4%.
- **Smallest:** Prompt Misalignment, 9.0%.
- **Total:** 100.0% [C].
- **Caveat:** categories are mutually exclusive in the table even though the authors acknowledge conceptual overlap, especially between prompt design, getting stuck, and hallucination.

# 12. Diagram / Architecture Interpretation

The core architecture can be expressed as:

```text
User task
   ↓
Live browser (Selenium)
   ↓
Screenshot + extracted interactive elements
   ↓
Black bounding boxes and numerical labels
   ↓
LMM context:
  current observation
  + last three webpage observations
  + full thought/action history
   ↓
Thought → one formatted action
   ↓
Browser executes action
   ↓
New observation or execution error
   ↺
ANSWER or 15-step limit
```

The **data path** carries screenshots, web-element text, action history, and errors into the model. The **control path** is the formatted action returned to Selenium. Numerical labels form the interface between the visual representation and executable element selection.

There is no learned detector between the screenshot and the action. Instead, a rule-based JavaScript utility identifies interactive elements from webpage element types. This is an important architectural simplification relative to systems that require a trained candidate-element selector (§§2, 3.3).

The benchmark-construction architecture in Figure 3 is a human–model feedback process: human seeds support GPT-4 generation, manual verification turns acceptable generations into new seeds, and those seeds expand later generations.

# 13. Equations and Mathematical Concepts

## E1 — Context at time \(t\)

Location: p. 3, §3.2.

\[
c_t = (o_1, a_1, \ldots, o_{t-1}, a_{t-1}, o_t, I)
\]

- \(c_t\): context given to the model at step \(t\);
- \(o_i\): observation at step \(i\);
- \(a_i\): action at step \(i\);
- \(I\): user instruction;
- output type: an ordered interaction history plus current observation and task.

Plainly: the next decision is based on the instruction, what the agent has seen, and what it has already done.

Implementation qualification: although the formal equation displays the full observation history, the actual system clips outdated webpage observations and retains only the three most recent, while retaining all thoughts and actions (§3.2).

## E2 — Model action selection

\[
a_t = M(c_t)
\]

- \(M\): large multimodal model;
- \(c_t\): current context;
- \(a_t\): selected action.

The action is further decomposed as:

\[
a_t = (s_t,\hat{a}_t)
\]

- \(s_t\): natural-language thought;
- \(\hat{a}_t\): executable action code.

Plainly: the model first states a brief rationale, then emits one command in the required syntax.

## E3 — Environment transition

\[
o_{t+1} = E(o_t,a_t)
\]

- \(E\): browser environment;
- \(o_t\): current observation;
- \(a_t\): executed action;
- \(o_{t+1}\): resulting observation.

This is a state-transition relation: acting on the current webpage produces the next page state or observation.

## Agreement statistics

The paper uses:

- **raw agreement:** fraction of evaluator and human labels that overlap;
- **Cohen’s κ:** agreement corrected for chance between GPT-4V and consolidated human labels;
- **Fleiss’s κ:** multi-rater agreement among the three human annotators.

The formulas are not supplied. Their values are reported in Tables 2 and the accompanying text.

No loss function, training objective, theorem, proof, or optimization algorithm is introduced because WebVoyager is prompted rather than trained in this study.

# 14. Interpretation and Discussion

The evidence supports four main conclusions within the supplied study.

First, visual information is particularly useful for interaction-heavy interfaces. The most striking examples are Google Flights and Booking, where the multimodal system exceeds the text-only system by 52.4 and 40.9 percentage points [C]. The authors connect this to calendars and visually organized controls (§5.3).

Second, visual input alone is not sufficient. Allrecipes is the only site where the text-only configuration leads the human-evaluated multimodal system, and several text-heavy sites show small differences. The authors therefore argue for combining text and vision, not replacing one with the other.

Third, evaluating only the final answer or one screenshot is insufficient for many tasks. Table 2 shows higher agreement as the evaluator receives more trajectory evidence. The evaluator prompt also explicitly checks multi-part completion and screenshot/response discrepancies.

Fourth, interaction planning remains fragile. Nearly half of classified failures are Navigation Stuck errors. The visual grounding and hallucination categories show that successful clicks are not enough: the system must choose the right element, recognize subtle state changes, satisfy every condition, and verify that the answer follows from the page.

Unresolved points include:

- “Significantly” is used without statistical testing.
- Figure 6 provides a descriptive complexity relationship but no quantified association.
- Evaluators exhibit model-dependent scoring and apparent self-preference.
- Figure 19’s reported answer does not verbalize the requested price trends.
- Automatic evaluation’s instruction to believe response-only information may permit unsupported claims.

# 15. Contributions and Novelty

## System contribution

An end-to-end LMM web agent that operates on real websites through Selenium without intermediate human intervention.

## Methodological contribution

A multimodal observation design combining screenshots, numbered element boxes, and auxiliary web-element text.

## Interface contribution

A concise, executable browser action language grounded in numbered screenshot elements.

## Benchmark contribution

A 643-task, 15-website live-web benchmark generated through self-instruction plus human verification.

## Evaluation contribution

A trajectory-level GPT-4V evaluation protocol designed for open-ended tasks and alternative valid action sequences.

## Empirical contribution

Evidence that the multimodal system outperforms the two main baselines overall, with especially large gains on visually complex websites.

## Analytical contribution

A four-part failure taxonomy and representative visual examples.

## Scope of novelty claim

The authors position WebVoyager as requiring no additional trained candidate-element-selection module, unlike the best SeeAct configuration described in their related-work comparison (§2). This is an author-positioned comparison, not an independent literature audit.

# 16. Limitations

## Authors’ stated limitations

The authors explicitly acknowledge:

1. **Incomplete action space:** actions such as drag are unsupported; continuous drag distance is difficult to encode as a finite choice (pp. 9–10).
2. **Limited file-format support:** basic text and PDFs are supported, but not every format, especially video (p. 10).
3. **Vision on dense text:** screenshot-based decisions can struggle on text-heavy sites (§5.2).
4. **Navigation loops:** context clipping can contribute to repeated mistakes (§5.4).
5. **Open-source model constraints:** the authors report that then-available open LMMs reduced images to 224×224 or 336×336 and commonly had 4,096-token contexts, while their trajectories required approximately 7,000+ tokens (§5.3).
6. **Safety risks:** malicious downloads, disclosure of confidential information, fake requests, and fake activity require extensive checks before deployment (p. 10).
7. **Website exclusions:** login- and CAPTCHA-requiring sites were omitted (§4.1).

## Additional evidence-based analyst observations

These are not author admissions:

1. **No statistical inference:** performance gaps are reported without confidence intervals for the principal human-evaluated results or paired significance testing.
2. **Dynamic benchmark reproducibility:** live webpages, prices, rankings, and layouts can change, making exact replication difficult.
3. **Benchmark answer uncertainty:** 77.7% of tasks have only Possible answers [C], increasing reliance on evaluator judgment.
4. **Selected trajectory bias:** Figures 4 and 9–24 are successful examples and do not establish typical behavior.
5. **Evaluator circularity:** GPT-4V is both the main agent backbone and an evaluator in several analyses; Table 3 demonstrates evaluator-specific preferences.
6. **Unsupported response acceptance:** Figure 8 instructs the evaluator to believe response content absent from screenshots unless contradicted.
7. **Limited implementation reporting:** hardware, cost, latency, detailed browser versions, random seeds, and exact model snapshots are missing.
8. **No controlled modality ablation beyond text-only:** the paper does not separately quantify screenshot-only, auxiliary-text-only, label-color, or context-clipping choices.
9. **Sampled error analysis:** failure categories come from 300 sampled tasks, but the sampling procedure and annotator agreement for category labels are not specified.
10. **Potential example ambiguity:** Figures 19 and 23 raise questions about whether the displayed answers fully satisfy the stated tasks.

# 17. Threats to Validity

## Internal validity

Changes between live-site runs could affect system comparisons. The paper does not state whether all systems saw identical page states, prices, rankings, or timing conditions.

The GPT-4V evaluator’s judgments depend on prompt rules and screenshot selection. Model self-preference in Table 3 indicates that evaluator identity is a confound.

## Construct validity

Task Success Rate captures completion but not efficiency, safety, robustness, or path quality. The paper explicitly says it does not assess whether the action sequence is optimal (§5).

“Hallucination” includes both incomplete answers and actions taken on the wrong valid field, making the category broader than fabrication alone.

## External validity

The use of real sites supports ecological realism, but the evaluation excludes login, CAPTCHA, dragging, video, and various file formats. Results may not extend to transactional, authenticated, or higher-risk web tasks.

## Statistical conclusion validity

No significance tests, confidence intervals for human-evaluated system differences, or correlation statistics for Figure 6 are reported. Automatic-evaluation standard deviations reflect three evaluator runs, not independent agent reruns.

## Ecological validity

Live websites increase realism. However, ethical restrictions and the informational nature of tasks mean the evaluation does not cover the full consequences of autonomous browser action.

## Reproducibility

The paper supplies prompts and action formats, and says code/data will be released. Reproducibility remains constrained by dynamic websites and missing operational details in the supplied document.

## Generalizability

Two successful non-English examples demonstrate feasibility, but they are not a systematic multilingual evaluation.

# 18. Future Work and Open Questions

## A. Future work explicitly proposed by the authors

- Add richer text extracted from HTML for dense text-heavy pages (§5.2).
- Improve prompts for GPT-4o and Claude, especially for Google Flights (§5.2).
- Develop stronger visual encoders or additional textual inputs (§5.4).
- Improve optimal-trajectory planning and reduce repeated actions (§5.4).
- Add drag operations, potentially using model-selected pixel displacements (Limitations).
- Support more file formats, especially video (Limitations).
- Continue toward more versatile and capable web assistants (§6).

## B. Additional open questions

- How stable are results when the same tasks are rerun across dates and site redesigns?
- Would paired human evaluation confirm the reported system gaps statistically?
- How much does each component contribute: screenshot, element text, numbered marks, thought generation, and context clipping?
- Can evaluation be made less model-dependent and less vulnerable to self-preference?
- How should unsupported final-answer claims be handled when screenshots provide no confirming evidence?
- What is the cost, latency, and environmental footprint per completed task?
- How robust is the system to adversarial webpage text, misleading labels, or prompt injection?
- Can success be evaluated jointly with action efficiency and safety?
- How well does the method generalize across languages in a controlled multilingual benchmark?
- What fraction of failures would disappear with a larger step budget, and what new risks would that introduce?

# 19. Terminology and Notation Glossary

| Term | Beginner-friendly meaning |
|---|---|
| Agent | A model-driven system that observes an environment and takes actions toward a goal |
| LLM | Large Language Model; a model primarily designed for language |
| LMM | Large Multimodal Model; a model that jointly processes modalities such as images and text |
| GPT-4V | GPT-4 with visual input capability, as named in the paper |
| Web agent | An agent that navigates and interacts with websites |
| End-to-end | Completing the whole task from instruction to answer, not merely predicting one next action |
| Selenium | The browser-automation environment used by WebVoyager |
| HTML | The markup structure underlying webpages |
| DOM tree | Hierarchical representation of webpage elements |
| Accessibility tree | A structured textual representation of interface controls and content |
| Observation | Information received by the agent at a step: screenshot, element text, and history |
| Action space | The set of commands the agent is allowed to execute |
| Visual grounding | Matching an intended action to the correct visible interface element |
| Set-of-Mark prompting | Adding numbered marks to candidate visual elements |
| ReAct | A prompting pattern that alternates reasoning and acting |
| Context clipping | Removing older observations to stay within the model’s input limit |
| Trajectory | Complete sequence of observations and actions for a task |
| Golden answer | A stable, comprehensive set of accepted answers |
| Possible answer | A partial or time-dependent set of acceptable answers |
| Task Success Rate | Percentage of tasks judged successfully completed |
| `k` | Number of final screenshots supplied to the automatic evaluator |
| Agreement | Fraction of labels shared by evaluator and humans |
| Cohen’s κ | Chance-adjusted agreement between two label sources |
| Fleiss’s κ | Agreement statistic for multiple raters |
| \(E\) | Browser environment |
| \(M\) | Multimodal model |
| \(O\) | Observation space |
| \(A\) | Action space |
| \(I\) | User instruction |
| \(o_t\) | Observation at time step \(t\) |
| \(a_t\) | Action at time step \(t\) |
| \(c_t\) | Context supplied to the model at time step \(t\) |
| \(s_t\) | Natural-language thought at step \(t\) |
| \(\hat a_t\) | Executable action code at step \(t\) |
| CAPTCHA | A challenge intended to distinguish humans from automated systems |
| `aria-label` | Accessibility metadata that may describe an interface element |
| Backbone | The underlying multimodal model used to drive WebVoyager |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Benchmark size | 643 | tasks | 15 live websites | Author-reported | p. 5, §4.2 |
| Websites | 15 | sites | New benchmark | Author-reported | p. 4, §4.1 |
| Tasks per site | 40–45 | tasks | Table 1 evaluation | Author-reported | p. 7, Table 1 caption |
| Golden-answer share | 22.3 | % | Benchmark | Author-reported | p. 5, §4.3 |
| Possible-answer share | 77.7 | % | `100 − 22.3` | Analyst-derived | p. 5, §4.3 |
| Pairwise comparisons | 206,403 | pairs | 643 task questions | Author-reported | p. 5, §4.2 |
| Similarity > 0.8 | 49 | pairs | Diversity check | Author-reported | p. 5, §4.2 |
| Similarity 0.7–0.8 | 140 | pairs | Diversity check | Author-reported | p. 5, §4.2 |
| Similarity < 0.6 | 99.68 | % of pairs | Diversity check | Author-reported | p. 5, §4.2 |
| WebVoyager overall success | 59.1 | % | Human evaluation | Author-reported | p. 7, Table 1 |
| Text-only overall success | 40.1 | % | Human evaluation | Author-reported | p. 7, Table 1 |
| GPT-4 All Tools overall success | 30.8 | % | Human evaluation | Author-reported | p. 7, Table 1 |
| Gain over text-only | 19.0 | percentage points | `59.1 − 40.1` | Analyst-derived | p. 7, Table 1 |
| Gain over All Tools | 28.3 | percentage points | `59.1 − 30.8` | Analyst-derived | p. 7, Table 1 |
| Relative gain over text-only | 47.4 | % | `19.0/40.1 × 100` | Analyst-derived | p. 7, Table 1 |
| Relative gain over All Tools | 91.9 | % | `28.3/30.8 × 100` | Analyst-derived | p. 7, Table 1 |
| GAIA Level 1 success | 38.5 | % | WebVoyager | Visually readable / author-reported | p. 8, Fig. 5 |
| GAIA Level 2 success | 15.6 | % | WebVoyager | Visually readable / author-reported | p. 8, Fig. 5 |
| SeeAct-task success | 30 | % | WebVoyager, 50 tasks | Author-reported | p. 6, §5.2 |
| Best SeeAct autonomous agent | 26 | % | Same task set | Author-reported | p. 6, §5.2 |
| Human-evaluator subset | 300 | tasks | Three annotators | Author-reported | p. 6, §5.1 |
| Human pre-discussion Fleiss κ | 0.70 | κ | Three annotators | Author-reported | p. 6, footnote 7 |
| Full GPT-4V/human agreement | 85.3 | % | Full trajectory | Author-reported | p. 7, Table 2 |
| Full GPT-4V/human κ | 0.70 | κ | Full trajectory | Author-reported | p. 7, Table 2 |
| GPT-4o/human κ | 0.72 | κ | Full trajectory | Author-reported | p. 7, §5.2 |
| Claude/human κ | 0.60 | κ | Full trajectory | Author-reported | p. 7, §5.2 |
| Maximum trajectory | 15 | steps | All experiments | Author-reported | p. 5, Experimental Details |
| Browser size | 1024 × 768 | pixels | Agent environment | Author-reported | p. 5 |
| Agent temperature | 1 | temperature setting | Generation | Author-reported | p. 5 |
| Evaluator temperature | 0 | temperature setting | Automatic evaluation | Author-reported | p. 13, Appendix B |
| Navigation Stuck | 44.4 | % of classified failures | Error analysis | Author-reported | p. 9, Table 4 |
| Visual Grounding Issue | 24.8 | % | Error analysis | Author-reported | p. 9, Table 4 |
| Hallucination | 21.8 | % | Error analysis | Author-reported | p. 9, Table 4 |
| Prompt Misalignment | 9.0 | % | Error analysis | Author-reported | p. 9, Table 4 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| Multimodal WebVoyager outperforms the two main baselines overall | 59.1% vs 40.1% and 30.8% | X1, Table 1 | p. 7 | Strong descriptive evidence on this benchmark; no significance test |
| Vision is especially valuable on visually complex interfaces | Google Flights: 59.5% vs 7.1%; Booking: 43.2% vs 2.3% | X2, Table 1 | p. 7 | Strong site-level association; component causality not isolated |
| Text remains important | Allrecipes text-only 55.6% vs multimodal 53.3%; small gaps on several text-heavy sites | X2 | pp. 6–8 | Supports a mixed-modality argument; no screenshot-only ablation |
| Direct website access matters | GPT-4 All Tools performs poorly on several sites it cannot directly manipulate | Discussion + Table 1 | p. 8 | Authors’ diagnosis based on experience; not a controlled access ablation |
| GPT-4V can approximate human trajectory evaluation | 85.3% agreement, κ = 0.70 with full trajectory | X5, Table 2 | p. 7 | Promising but imperfect; evaluated on 300 tasks |
| More trajectory evidence improves evaluator alignment | Agreement 75.3% → 85.3%; κ 0.51 → 0.70 | X5, Table 2 | p. 7 | Strong monotonic agreement/κ pattern |
| Evaluator identity affects measured success | Table 3 varies scores by evaluator; each evaluator favors its own backbone | X6, Table 3 | p. 7 | Clear descriptive pattern; mechanism untested |
| More complex webpages/tasks tend to be harder | Figure 6 relates longer trajectories and more elements to lower success | X7, Figure 6 | p. 8 | Qualitative/descriptive; no correlation coefficient |
| Getting stuck is the largest failure source | 44.4% of classified failures | X8, Table 4 | p. 9 | Directly reported; sample-selection details limited |
| WebVoyager works beyond English in examples | One Chinese and one Spanish successful trajectory | Figures 23–24 | pp. 24–25 | Demonstration only, not a multilingual benchmark |
| The system completes tasks end-to-end | Numerous successful live-site trajectories | Figures 4, 9–24 | pp. 6, 16–25 | Demonstrates feasibility; selected examples do not establish frequency |
| The action architecture needs broader capabilities and safety checks | Missing drag/video support and stated deployment risks | Limitations/Ethics | pp. 9–10 | Explicit author acknowledgment |

# 22. Very Simple Explanation

Imagine giving a computer this instruction: “Go to a travel site, find a flight with these dates, inspect the price chart, and tell me what you found.” Older systems often read a giant textual description of the webpage. WebVoyager instead looks at a screenshot, while also receiving short text descriptions of clickable items. Every button and field is given a number, so the model can say things like “Click 16” or “Type Athens into box 14.”

The computer repeats a loop: look at the page, think about the next move, perform one action, and look again. The researchers tested it on 643 tasks across 15 real websites. It completed 59.1% successfully, compared with 40.1% for a text-only version and 30.8% for GPT-4 with its then-available tools.

The researchers also asked another vision-capable model to grade completed browsing sessions. When that grader saw the full sequence of screenshots, it agreed with people 85.3% of the time. That is useful, but it is not perfect, and different model graders sometimes favored their own model’s work.

The main lesson is that seeing the webpage helps a lot—especially for calendars, maps, and visually complicated controls—but text is still needed. The agent can get lost, click the wrong nearby control, stop too early, or give an answer that sounds convincing without satisfying every part of the task.

# Completeness Audit

## Inventory

- **Title:** *WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models*
- **Authors:** Hongliang He, Wenlin Yao, Kaixin Ma, Wenhao Yu, Yong Dai, Hongming Zhang, Zhenzhong Lan, Dong Yu.
- **Venue:** Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics, Volume 1: Long Papers, pp. 6864–6890, August 11–16, 2024.
- **Document type:** AI systems + benchmark + empirical evaluation paper.
- **Accessible length:** 27 PDF pages.
- **Major sections:** Abstract; §§1–6; Limitations; Ethics Statement; References; Appendices A–F.
- **Figures:** 28.
- **Tables:** 4.
- **Major equations:** three interaction relations in §3.2, plus one action decomposition.
- **Formal algorithms/theorems:** none.
- **Distinct analyses:** main benchmark, per-site comparison, GAIA, SeeAct, evaluator validation, evaluator/backbone matrix, complexity analysis, error analysis.
- **Explicit formal RQs/hypotheses:** none.
- **Separate supplementary file:** none supplied.

## Coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes | Yes | Fully represented | Headline problem, method, and results included |
| §1 Introduction | Yes | Yes | Fully represented | Motivation, gap, contributions, evaluation rationale |
| §2 Related Work | Yes | Yes | Represented in compressed form | Major categories and author-positioned distinctions retained |
| §3 WebVoyager | Yes | Yes | Fully represented | Architecture and interaction cycle covered |
| §3.1 Browsing Environment | Yes | Yes | Fully represented | Selenium, live web, CAPTCHA policy |
| §3.2 Interaction Formulation | Yes | Yes | Fully represented | Equations, ReAct, and context clipping |
| §3.3 Observation Space | Yes | Yes | Fully represented | Screenshots, marks, text, one-tab restriction, error feedback |
| §3.4 Action Space | Yes | Yes | Fully represented | All seven actions included |
| §4 Benchmark | Yes | Yes | Fully represented | Site scope and construction |
| §4.1 Website Selection | Yes | Yes | Fully represented | All 15 sites and exclusions |
| §4.2 Data Construction | Yes | Yes | Fully represented | Three stages and diversity figures |
| §4.3 Annotation Process | Yes | Yes | Fully represented | Golden/Possible scheme |
| §5 Experiment | Yes | Yes | Fully represented | Data, models, metric, parameters |
| §5.1 Evaluation Methods | Yes | Yes | Fully represented | Human and automatic evaluation |
| §5.2 Results | Yes | Yes | Fully represented | Main, GAIA, SeeAct, evaluator results |
| §5.3 Discussion | Yes | Yes | Fully represented | Direct interaction, modalities, complexity, open models |
| §5.4 Error Analysis | Yes | Yes | Fully represented | Categories, proportions, mechanisms |
| §6 Conclusion | Yes | Yes | Fully represented | Claims preserved without strengthening |
| Limitations | Yes | Yes | Fully represented | Both capability and safety limitations |
| Ethics Statement | Text inspected; page not visually rendered | Yes | Fully represented from native text | Non-login restriction, monitoring, manual task review |
| References | Text inspected; pages not visually rendered | Partly | Deliberately compressed | Bibliography was not reproduced entry by entry |
| Appendix A | Yes | Yes | Fully represented | Prompt design and Figure 7 |
| Appendix B | Yes | Yes | Fully represented | Evaluation prompt and temperature |
| Appendix C | Yes | Yes | Fully represented | Exact action formats and PDF handling |
| Appendix D | Yes | Yes | Represented in compressed form | Every successful trajectory, Figures 9–24, accounted for |
| Appendix E | Yes | Yes | Represented in compressed form | Added visual-agent and LMM context summarized |
| Appendix F | Yes | Yes | Fully represented | All four error examples |
| Figure 1 | Yes, visual | Yes | Fully represented | Workflow |
| Figure 2 | Yes, visual | Yes | Fully represented | Labeled screenshot |
| Figure 3 | Yes, visual | Yes | Fully represented | Dataset flow |
| Figure 4 | Yes, visual | Yes | Fully represented | Apple trajectory |
| Figure 5 | Yes, visual | Yes | Fully represented | Axes and all six values |
| Figure 6 | Yes, visual | Yes | Fully represented | Axes, encoding, qualitative pattern |
| Figures 7–8 | Yes, visual | Yes | Fully represented | Agent/evaluator prompts |
| Figures 9–24 | Yes, visual | Yes | Represented in compressed form | Every task, step count, and outcome inventoried |
| Figures 25–28 | Yes, visual | Yes | Fully represented | Every error case explained |
| Table 1 | Yes, visual and text | Yes | Fully represented | All human results; key automatic results and uncertainty |
| Table 2 | Yes, visual and text | Yes | Fully represented | Every row and metric |
| Table 3 | Yes, visual and text | Yes | Fully represented | Full 3×3 matrix |
| Table 4 | Yes, visual and text | Yes | Fully represented | Every category and proportion |
| Interaction equations | Yes | Yes | Fully represented | Symbols and implementation qualification |
| Algorithms | Not applicable | Yes | No formal algorithm present | Procedural loop described instead |
| Formal RQs/hypotheses | Not applicable | Yes | Explicitly identified as absent | Objectives reconstructed without inventing formal RQs |
| Main benchmark experiment | Yes | Yes | Fully represented | X1–X2 |
| GAIA experiment | Yes | Yes | Fully represented | X3 |
| SeeAct comparison | Yes | Yes | Fully represented | X4 |
| Evaluator validation | Yes | Yes | Fully represented | X5 |
| Evaluator/backbone analysis | Yes | Yes | Fully represented | X6 |
| Complexity analysis | Yes | Yes | Fully represented | X7 |
| Error analysis | Yes | Yes | Fully represented | X8 |
| Major contributions | Yes | Yes | Fully represented | System, benchmark, evaluation, empirical |
| Author-stated limitations | Yes | Yes | Fully represented | Capability, file types, safety, exclusions |
| Supplementary material | No separate file supplied | Yes | Missing from supplied material | No supplementary file identified in the record |

## Missing or inaccessible material

- PDF pages 10–12 were not visually rendered. Their native text was supplied and inspected; these pages contain the ethics statement and references, not numbered substantive visuals.
- The linked code/data repository was not supplied or inspected.
- Referenced software and external datasets were not supplied as artifacts.
- No independent supplementary file was supplied.
- Fine webpage text within many appendix screenshots is too small for complete independent reading, although captions, action labels, and major visible states are readable.

## Uncertain interpretations

- Figure 6’s exact point coordinates are unlabeled; only qualitative relationships and approximate positions can be read.
- Figure 19’s final response does not state the price trends it was asked to analyze, despite being presented as a success.
- Figure 23 reports 17:35 for a task translated as requesting departure “at night”; the paper does not discuss whether this satisfies the constraint.
- The formal context equation shows complete historical observations, whereas implementation text says older webpage observations are clipped. This is best understood as an abstract formulation qualified by the actual context-management policy.
- “Significantly outperforming” is not backed by a reported statistical significance test.
- The reported 99.68% below-0.6 similarity is retained as an author-reported value; the paper does not provide the full similarity distribution required to independently recompute it.

## Deliberately compressed material

- The complete bibliography was treated as supporting scholarly apparatus and not reproduced reference by reference.
- Appendix E’s literature discussion was synthesized by category.
- Successful trajectory Figures 9–24 were individually inventoried in a compact table rather than narrating every click separately.
- Repetitive screenshot details in trajectory galleries were compressed because their substantive contribution is demonstration of site breadth and action sequences.

## Potential omissions

No known substantive section, subsection, experiment, numbered figure, table, major equation, contribution, author-stated limitation, or appendix from the supplied inventory is unrepresented. The principal remaining limits concern unrendered reference pages, unavailable external artifacts, and small webpage text within appendix screenshots.