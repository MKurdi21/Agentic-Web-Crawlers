# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Accessible range | Pages 1–21 |
| Apparently missing pages | None |
| Native/extracted text | Available for all 21 pages |
| Visually rendered pages | 1–9, 11, 13–21 |
| Pages not visually rendered | 10 and 12 |
| Figures visually inspectable | Yes. Figures 1–11 appear on rendered pages |
| Tables visually inspectable | Yes. Tables 1–10 appear on rendered pages |
| Equations | No numbered or contribution-critical equations appear |
| Algorithms/pseudocode | No formal algorithm blocks; agent and task procedures are described in prose |
| Appendices | Appendix A (§A.1–A.3, pp. 13–19) and Appendix B (§B.1–B.2, pp. 20–21) are present |
| Supplementary material | No separate supplementary file was supplied |
| Referenced external artifacts | WorkArena, BrowserGym, AgentLab repositories; ServiceNow Personal Developer Instances; cited benchmarks and software. These were not inspected because analysis is in closed-document mode |
| OCR needed | No. Native text was available; visual inspection was used to cross-check figures and tables |
| Readability limitations | Some small interface labels and exact values inside screenshots are difficult to read independently, but their captions and surrounding text explain the substantive content. Figure 4’s fine-grained violin distributions have no labeled individual values. Table uncertainty typography is small but corroborated by supplied text |
| Uninspected visual matter | Pages 10 and 12 contain text/reference material rather than substantive scientific figures or tables. Their extracted text was inspected, but their typography was not visually checked |
| Truncation | None apparent |

Evidence categories used below:

- **[A] Author-reported:** explicitly stated in the paper.
- **[B] Directly observable:** visible in the supplied rendering.
- **[C] Analyst-derived:** calculated from supplied values, with operands shown.
- **[D] Analyst interpretation:** inference rather than an explicit author claim.
- **[E] External information:** excluded.

# Document Inventory

**Title:** *WorkArena: How Capable are Web Agents at Solving Common Knowledge Work Tasks?*  
**Authors:** Alexandre Drouin, Maxime Gasse, Massimo Caccia, Issam H. Laradji, Manuel Del Verme, Tom Marty, Léo Boisvert, Megh Thakkar, Quentin Cappart, David Vazquez, Nicolas Chapados, and Alexandre Lacoste.  
**Venue:** Proceedings of the 41st International Conference on Machine Learning, PMLR 235, 2024 (p. 1).  
**Document type:** Machine-learning/AI benchmark paper, browser-agent systems paper, and empirical experimental study.

## Section inventory

- **S1:** Abstract (p. 1)
- **S2:** Introduction (§1, pp. 1–2)
- **S3:** Related Works (§2, pp. 2–3)
- **S4:** WorkArena—An Enterprise Benchmark (§3, pp. 3–5)
  - **SS4.1:** WorkArena Tasks (§3.1)
  - **SS4.2:** Challenges: the “World Wild Web of Work” (§3.2)
  - **SS4.3:** Availability (§3.3)
- **S5:** BrowserGym (§4, pp. 5–6)
  - **SS5.1:** Capabilities (§4.1)
  - **SS5.2:** An Ideal Experimental Framework (§4.2)
- **S6:** Experiments (§5, pp. 6–9)
  - **SS6.1:** Agent Design (§5.1)
  - **SS6.2:** Experimental Protocol (§5.2)
  - **SS6.3:** Results (§5.3)
  - **SS6.4:** Ablation Study (§5.4)
- **S7:** Conclusion (§6, p. 9)
- **S8:** Impact Statement (p. 10)
- **S9:** References (pp. 10–12)
- **A1:** WorkArena—Additional Details (pp. 13–19)
  - §A.1 Tasks
  - §A.2 Task User Interface Examples
  - §A.3 Knowledge Base Tasks—Additional Details
- **A2:** BrowserGym—Additional Details (pp. 20–21)
  - §B.1 Action Space
  - §B.2 MiniWoB

## Visual and tabular inventory

- **Figures 1–11:** contribution overview; task-goal examples; form UI; observation-size distributions; five WorkArena task walkthroughs; generated knowledge article; MiniWoB rendering.
- **Tables 1–10:** selected configurations; main results; three model ablations; complete task inventory; knowledge-base facts/questions/answers; BrowserGym action space.
- **Formal equations/theorems:** none.
- **Explicit hypotheses:** none formally stated.
- **Explicit research questions:** none enumerated; two experimental objectives are stated on p. 6.
- **Major experiments:** model/benchmark comparison, task-category analysis, multimodal comparison, and feature ablations for three language models.

# 1. Plain-Language Orientation

This paper asks whether a language-model agent can use a web browser to carry out ordinary office-software work: filter records, fill forms, search an internal knowledge base, order equipment, read dashboards, and navigate application menus.

The authors argue that earlier web-agent benchmarks largely emphasized toy interfaces, simulated shopping, or public-facing sites. Enterprise software remained comparatively underexplored despite its complex interfaces and its importance to everyday knowledge work (§1–2, pp. 1–3).

They contribute two connected artifacts:

1. **WorkArena**, a benchmark built on real ServiceNow cloud instances, containing 33 task types and 19,912 generated task instances.
2. **BrowserGym**, a general browser-agent environment exposing textual and visual observations, several action styles, chat interaction, validation, and optional oracle solutions.

They evaluate GPT-4o, vision-augmented GPT-4o, GPT-3.5, and Llama3-70B. On WorkArena, their principal success rates are 42.7%, 41.8%, 6.1%, and 17.9%, respectively (Table 2, p. 7). Thus, even the strongest tested agent fails most episodes. Filtering lists is especially difficult: all four configurations score 0.0% in that category.

The central contribution is consequently not a high-performing automation system. It is a realistic, extensible testing infrastructure showing that apparently routine enterprise tasks remain difficult for contemporary language-model agents.

# 2. Document Roadmap

The paper moves from motivation to artifact design and then evaluation:

- The **Introduction** motivates visible, user-supervisable UI assistants and identifies enterprise software as the target gap.
- **Related Works** positions WorkArena against toy, simulated, public-web, and mobile-interface benchmarks.
- **§3** defines the benchmark, task categories, validation/oracle machinery, and interface challenges.
- **§4** defines BrowserGym’s observation/action interface and benchmark-development API.
- **§5** describes the tested agents, tuning protocol, main comparative results, and ablations.
- **§6** summarizes the findings and proposes expansions.
- The **Impact Statement** discusses productivity, accessibility, displacement, cybersecurity, privacy, and environmental effects.
- **Appendix A** supplies the complete task list and concrete interface walkthroughs, then details knowledge-base generation.
- **Appendix B** enumerates BrowserGym actions and explains its MiniWoB adaptation.

The appendices materially supplement the methodology: Table 6 exposes task complexity and counts, Tables 7–9 explain synthetic knowledge-base construction, and Table 10 defines the executable action surface.

# 3. Background and Context

A **web agent** is software that observes a webpage, reasons about a goal, and issues browser actions. Here, the reasoning core is a **large language model (LLM)**.

A **graphical user interface (UI)** is the visible set of forms, lists, menus, buttons, and other elements through which users operate software. A UI-based assistant acts through that same interface, unlike an **application programming interface (API)** automation that calls a separate machine-facing interface.

The **Document Object Model (DOM)** is a structured representation of page elements. An **accessibility tree (AXTree)** is a representation oriented toward semantic and accessibility properties. WorkArena’s ServiceNow pages can have cleaned flat HTML representations ranging from 40,000 to 500,000 tokens (§3.2, p. 5), so the experiments use AXTree rather than HTML for WorkArena and WebArena (footnote 6, p. 6).

A **browser action space** defines what commands an agent may issue. BrowserGym supports:

- element-identifier or **bid-based** commands such as clicking a specific element;
- coordinate commands using screen positions;
- navigation, tab, scrolling, and chat commands;
- arbitrary Python/Playwright code when enabled.

A **Partially Observable Markov Decision Process (POMDP)** models sequential decisions when each observation does not reveal all relevant state. BrowserGym returns only the current page view; it does not provide memory automatically (p. 5 and footnote 4).

A benchmark episode succeeds when its validation procedure determines that the task goal has been fulfilled. The principal metric is **success rate (SR)**, accompanied by **standard error (SE)** estimated through stratified bootstrap resampling (§5.2, p. 7).

# 4. Research Problem and Gap

## Existing problem

Routine browser-based enterprise tasks can be burdensome, repetitive, inaccessible, and difficult to automate transparently (§1, pp. 1–2).

## Shortcomings of previous approaches, as characterized by the authors

- APIs are not universal and can produce opaque automation that users cannot easily inspect (p. 1).
- Early web benchmarks emphasized synthetic interfaces and low-level actions.
- Other benchmarks address simulated commerce, public websites, recorded interactions, or mobile interfaces rather than enterprise workflows (§2, pp. 2–3).
- Existing browser environments do not, according to the paper, combine all prior observation/action facilities with chat-based agent–user interaction and robust support for nested interface structures (§2, §4.1).

## Research gap

The authors identify a lack of realistic evaluation for web agents operating enterprise software used in everyday knowledge work.

## Motivation

Such agents might improve productivity and accessibility while allowing people to observe and reclaim control of the interface. ServiceNow is selected because it covers multiple enterprise functions and exposes realistic interface difficulties (§1).

## Scope

The empirical scope is limited to LLM-based browser agents. WorkArena version 0.3.0 covers 33 atomic task types on ServiceNow; it does not yet evaluate the proposed future compositional workflows (§2, p. 3; §5, p. 6; §6, p. 9).

# 5. Research Questions / Objectives / Hypotheses

## Explicit research questions

The paper does not enumerate formal research questions.

## Explicit objectives

[A], §5, p. 6:

1. Situate WorkArena’s difficulty by comparing agents, baselines, and benchmarks.
2. Quantify the effect of BrowserGym features through ablation studies.

The broader objective is to assess the ability of state-of-the-art general-purpose LLMs to solve work-related browser tasks.

## Informal questions embodied by the design

These are reformulations, not author-numbered questions:

- How capable are current LLM-based agents on realistic enterprise tasks?
- How does performance vary by model and task category?
- Do visual input, coordinate information, memory, richer prompts, and other environment features improve performance?
- Can one environment support comparable evaluation across WorkArena, MiniWoB, and WebArena?

## Hypotheses

No formal hypotheses, null hypotheses, or preregistered tests are supplied. The authors state an expectation that WorkArena will be challenging (§5.3, pp. 7–8), but do not define a formal statistical hypothesis.

# 6. Assumptions / Threat Model

This is not a security-evaluation paper and contains no formal attacker threat model.

## System and environmental assumptions

- Tasks run on ServiceNow Personal Developer Instances (§3.3, p. 5).
- Each natural-language goal is intended to contain all information required for the task (§3.1, p. 3).
- Validation functions can accurately determine success through interface state, URLs, database queries, or chat messages (§3.1, pp. 3–4; §4.2, p. 6).
- Hand-coded Playwright oracle functions demonstrate task feasibility, though they may not be optimal (Table 6 caption, p. 13).
- Agents receive at most 15 steps per episode (§5.2, p. 7).
- The tested agents are zero-shot with one generic output-format example, rather than task-specific demonstrations (§5.1, p. 7).
- WebArena is treated as deterministic and is not used for tuning (footnote 7, p. 7).
- BrowserGym supplies current-state observations but not an internal memory mechanism (footnote 4, p. 5).

## Trusted components

Implicitly trusted components include BrowserGym, Playwright/CDP interaction, task setup/teardown, validators, database checks, and oracle implementations.

## Safety-relevant capability boundary

BrowserGym may permit arbitrary Python and Playwright execution, explicitly labeled “UNSAFE!” in Table 10. The experiments instead select bid-based action sets for the best configurations (Table 1, p. 6).

# 7. Methodology

## 7.1 WorkArena construction

WorkArena contains 33 task types and 19,912 instances (§3, p. 3; Table 6, p. 13). A task combines:

- a natural-language goal generated from a human-designed template;
- instance parameters such as field values, menu names, or product settings;
- a validation function;
- an optional/associated hand-coded Playwright oracle.

The validator provides real-time feedback and checks final completion. Oracle functions verify feasibility, can provide learning ground truth, and help detect breakage after ServiceNow changes (§3.1, p. 3).

### Task distribution

| Category | Task types | Instances | Validation basis |
|---|---:|---:|---|
| Lists | 12 | 6,900 | Resulting filter/sort state |
| Forms | 5 | 5,000 | Database values of created records |
| Knowledge base | 1 | 1,000 | Answer within an acceptable-answer set |
| Service catalog | 9 | 3,550 | Database record for item, quantity, specifications |
| Dashboards | 4 | 1,862 | Required chart numbers and labels in reply |
| Menus | 2 | 1,600 | Destination or impersonated-user state |
| **Total** | **33** | **19,912** | — |

The category totals sum to 19,912 [C]: 6,900 + 5,000 + 1,000 + 3,550 + 1,862 + 1,600 = 19,912.

List and form combinatorial instance pools were capped at 1,000 per task and randomly sampled (Table 6 caption, p. 13).

## 7.2 Knowledge-base dataset generation

The knowledge base contains 100 GPT-4-generated HTML articles derived from 100 item–value facts (§A.3, p. 18).

For each fact:

1. GPT-4 generates an article containing the exact fact string.
2. GPT-4 generates 10 question paraphrases and formatting instructions.
3. GPT-3.5 attempts each question against the article.
4. Failed questions are revised by GPT-4 and retested.
5. GPT-4 creates 10 acceptable answer formats.
6. The authors inspect generated alternatives for coherence.

Using GPT-3.5 as the checking model is intended to reduce the risk that GPT-4 writes ambiguously self-favoring questions (p. 18).

## 7.3 BrowserGym architecture

BrowserGym is implemented as an OpenAI Gym environment using Chromium, Chrome DevTools Protocol, and Playwright (§4, p. 5).

At each time step it can expose:

- goal/chat history;
- open-page URLs;
- last-action error;
- HTML DOM;
- AXTree;
- screenshot;
- unique element IDs;
- bounding coordinates;
- visible/clickable flags.

It supports element-based, coordinate-based, tab, navigation, scrolling, chat, and Python/Playwright actions (§4.1; Table 10).

A benchmark task implements four functions (§4.2, p. 6):

- `setup()` initializes data, authentication, and starting state.
- `teardown()` removes created resources.
- `validate()` returns reward, optional feedback, and a termination flag.
- `cheat()` optionally runs the oracle solution.

## 7.4 Agent design

The tested agent uses chain-of-thought prompting and a shared code base whose features are controlled by flags (§5.1, pp. 6–7).

History options include past actions, errors, and reasoning. A parsing loop can reprompt up to four times after malformed output. All selected final configurations use:

- chain-of-thought;
- action history;
- extracted visibility tags;
- bid-only actions;
- individual action examples;
- no multiple-actions mode.

Other selected features differ by model (Table 1).

## 7.5 Models and infrastructure

- **GPT-4o:** `gpt-4o-2024-05-13`, 128K model context; experiment prompt capped at 40K.
- **GPT-3.5:** `gpt-3.5-turbo-1106`, 16K context; prompt capped at 15K.
- **Llama3:** `meta-llama-3-70B-instruct`, 8K context; prompt capped at 8K.
- **Llama3 hardware:** four A100 GPUs using Hugging Face Text Generation Inference.
- **GPT-4o-V:** GPT-4o with a screenshot augmented by Set-of-Mark.

When prompts exceed the cap, HTML/AXTree content is progressively removed from the end (§5.1, p. 7).

## 7.6 Experimental protocol

- BrowserGym v0.3.5 and WorkArena v0.3.0 (p. 6).
- Maximum 15 steps per episode.
- Ten seeds per task for MiniWoB and WorkArena; one per WebArena task.
- Stratified bootstrap with 1,000 samples of the mean.
- Reported score: average bootstrap mean as SR and standard deviation of bootstrap means as SE.
- Configurations selected through random search on MiniWoB and WorkArena, then fixed and evaluated with a different seed.
- WebArena excluded from tuning because it is deterministic.

The paper does not report the random-search budget, sampling distribution over flags, API sampling parameters, monetary cost, wall-clock runtime, or full seed values.

# 8. Experiments / Analyses

## X1 — Cross-model, cross-benchmark evaluation

**Purpose:** Establish WorkArena difficulty and compare LLM capabilities.  
**Conditions:** GPT-4o, GPT-4o-V, GPT-3.5, and Llama3 with their selected configurations.  
**Data:** 33 WorkArena task types, 125 MiniWoB tasks, a 56-task WebGum subset, and 812 WebArena instances/tasks as labeled in Table 2.  
**Metric:** SR% ± SE.  
**Evidence:** Table 2, p. 7.

Main WorkArena results:

- GPT-4o: 42.7 ± 1.5
- GPT-4o-V: 41.8 ± 1.7
- GPT-3.5: 6.1 ± 1.3
- Llama3: 17.9 ± 1.5

GPT-4o leads all reported benchmark totals. WorkArena remains unsolved under the paper’s standard: the best result is below half.

## X2 — WorkArena category analysis

**Purpose:** Identify which enterprise interactions are difficult.  
**Evidence:** Table 2 and §5.3, pp. 7–8.

GPT-4o ranges from 80.0% on the single knowledge task to 0.0% on list filtering. Its service-catalog score is 77.8%, dashboards 62.5%, menus 60.0%, forms 40.0%, list sorting 10.0%, and list filtering 0.0%.

All four models score 0.0% on list filtering. [A] The authors connect this failure to the non-standard filtering widget shown in Figure 5.

## X3 — Vision augmentation

**Purpose:** Test whether screenshot input plus Set-of-Mark helps.  
**Comparison:** GPT-4o-V versus text-oriented GPT-4o with otherwise identical selected flags.  
**Evidence:** Table 2; discussion on p. 9.

GPT-4o-V changes:

- WorkArena: 42.7 → 41.8, a **−0.9 percentage-point** difference [C].
- MiniWoB: 66.1 → 67.7, **+1.6 points** [C].
- WebArena: 23.5 → 24.0, **+0.5 points** [C].

On WorkArena categories, vision improves dashboards and menus but reduces forms, knowledge, and service-catalog performance. The paper calls overall multimodal gains minor and disappointing.

## X4 — GPT-4o ablation

**Purpose:** Measure selected feature effects.  
**Evidence:** Table 3, p. 8.

The initial ablation configuration scores 68.2 ± 1.0 on MiniWoB and 45.5 ± 2.2 on WorkArena. Coordinate boxes plus coordinate actions raise MiniWoB to 72.6 but reduce WorkArena to 41.2. Every listed modification reduces WorkArena relative to 45.5; the largest listed reduction is multi-actions, to 40.6.

## X5 — GPT-3.5 ablation

**Evidence:** Table 4, p. 8.

Initial: 41.3 ± 1.1 MiniWoB and 8.5 ± 1.3 WorkArena.

Notable WorkArena results:

- removing chain-of-thought: 6.1;
- removing action history: 5.2;
- adding thought history: 3.0;
- adding multi-actions: 9.4;
- adding focused-element state: 9.4;
- adding center coordinates: 4.5.

The effects are not uniformly beneficial across benchmarks.

## X6 — Llama3 ablation

**Evidence:** Table 5, p. 8.

Initial: 59.8 ± 1.0 MiniWoB and 20.0 ± 2.3 WorkArena.

Removing chain-of-thought or action history reduces WorkArena to 8.5. Removing chain-of-thought therefore produces an **11.5-point** decline [C: 20.0 − 8.5], somewhat larger than the prose’s rounded “drop of 10 points.” Adding multi-actions raises MiniWoB to 63.0 but lowers WorkArena to 17.6.

## X7 — Observation-size analysis

**Purpose:** Compare HTML and AXTree lengths across benchmarks.  
**Evidence:** Figure 4, p. 9; §3.2 and §5.1.

The violin plots use a logarithmic token-count axis. WorkArena and WebArena observations are orders of magnitude larger than MiniWoB; pruned HTML appears larger than AXTree. No exact distribution statistics are labeled.

# 9. Results

## 9.1 Model capability gap

[A] GPT-4o achieves the strongest total score on WorkArena: 42.7 ± 1.5%, compared with Llama3’s 17.9 ± 1.5% and GPT-3.5’s 6.1 ± 1.3% (Table 2).

[C] Absolute gaps:

- GPT-4o minus Llama3: 42.7 − 17.9 = **24.8 percentage points**.
- GPT-4o minus GPT-3.5: 42.7 − 6.1 = **36.6 percentage points**.
- Llama3 minus GPT-3.5: 17.9 − 6.1 = **11.8 percentage points**.

These are percentage-point differences, not relative percentage improvements.

## 9.2 WorkArena difficulty

No tested agent exceeds 42.7% overall. All achieve 0.0% on list filtering. The paper attributes difficulty to large observations, non-standard HTML, dynamic widgets, hidden elements, nested structures, and long action sequences (§3.2; §5.3).

The statement that “no agent achiev[es] 100% success in one specific task” appears in §5.3, p. 8. Table 2 reports category aggregates rather than all 33 task-level scores, so this specific claim cannot be independently reconstructed from the supplied tables.

## 9.3 Performance on other benchmarks

- GPT-4o: MiniWoB 66.1 ± 1.0; WebGum subset 82.9 ± 1.5; WebArena 23.5 ± 0.7.
- GPT-4o-V: 67.7 ± 1.0; 83.2 ± 1.5; 24.0 ± 0.6.
- GPT-3.5: 38.9 ± 1.1; 53.6 ± 1.4; 6.7 ± 0.6.
- Llama3: 62.6 ± 0.6; 80.5 ± 1.0; 11.0 ± 0.6.

[A] The paper characterizes 23.5% as the best zero-shot WebArena performance then reported, compared with 14.4% in the original WebArena paper. Closed-document mode prevents independent verification of that literature claim.

[C] The stated difference is 23.5 − 14.4 = **9.1 percentage points**.

A minor internal discrepancy exists: the contribution list on p. 2 says BrowserGym brings the GPT-4 agent to **25.4%**, whereas Table 2 and §5.3 report **23.5%** for GPT-4o; GPT-4o-V is **24.0%**. The supplied paper does not reconcile 25.4 with these later results.

## 9.4 Chain-of-thought and history

Removing chain-of-thought hurts GPT-3.5 and Llama3 substantially. The GPT-4o table does not include a “remove thinking” row, so the broad statement that this is clearly shown for all three models is not fully supported by Tables 3–5 alone.

Action history is important for GPT-3.5 and Llama3:

- GPT-3.5 WorkArena: 8.5 → 5.2.
- Llama3 WorkArena: 20.0 → 8.5.

Thought history can hurt, which the authors explain as commitment to early mistaken decisions. That causal explanation is a hypothesis based on observed behavior, not a controlled mechanism test.

## 9.5 Richer features are not uniformly helpful

Coordinate information produces a MiniWoB gain for GPT-4o but a WorkArena loss. Longer action descriptions, extra memory, coordinate features, and visibility filtering sometimes degrade the weaker models. The authors hypothesize that longer prompts distract the model and cause more truncation.

## 9.6 Open- versus closed-source models

Llama3 performs below GPT-4o but above GPT-3.5 on all three aggregate benchmarks despite its shorter context cap. The authors also report preliminary Llama2 results of 0% on WorkArena and WebArena, but these experiments are not tabulated or methodologically detailed (§5.3, p. 8).

# 10. Figure-by-Figure Interpretation

### Figure 1 — WorkArena and BrowserGym overview

- **Figure 1a:** Screenshots represent six WorkArena interaction families: workspace/menu, list, form, dashboard, knowledge base, and service catalog.
- **Figure 1b:** Shows a loop among user chat, web agent, BrowserGym/browser, observations, and actions.
- Observations include HTML, AXTree, and screenshot; actions include element-ID, coordinates, and Python.
- It supports the paper’s two-artifact framing.
- No quantitative axes are present.

### Figure 2 — Example goals by task family

Six color-coded goal cards show explicit instructions for lists, forms, knowledge bases, service catalogs, dashboards, and menus. The substantive point is that goals supply concrete target values and expected outputs rather than requiring the agent to infer user intent.

### Figure 3 — Complex form interaction

A hardware-asset creation task illustrates:

1. autocomplete-driven fields;
2. fields hidden under tabs;
3. a date-picker interaction.

The figure links “simple” record creation to a long, stateful interface trajectory. The screenshot’s small field text is partially difficult to read, but numbered annotations and the caption are clear.

### Figure 4 — Observation-size distributions

- Two groups: pruned HTML and AXTree.
- Benchmarks: MiniWoB, WorkArena, WebArena.
- Y-axis: number of tokens per page, shown logarithmically.
- Violin shapes encode distributions.

[B] MiniWoB observations are much smaller; WorkArena and WebArena occupy far higher token ranges. HTML generally appears larger than AXTree. Exact medians and extrema are not labeled and should not be inferred precisely.

### Figure 5 — List-filter task walkthrough

The agent must:

1. reveal a hidden filter menu;
2. add and populate multiple conditions;
3. run the filter.

This visually substantiates the claim that list filtering uses a non-trivial custom widget. Table 2’s 0% results make this figure central to interpreting failure.

### Figure 6 — Knowledge-base search walkthrough

The agent receives a question, searches, examines candidate articles, reads the relevant page, and replies through chat. The example answer is `+1 (555) 101-2020`. The figure illustrates retrieval plus formatted response rather than database mutation.

### Figure 7 — Service-catalog order walkthrough

The agent navigates into the hardware catalog, selects a specific laptop, configures options and quantity, and submits the order. It demonstrates a multi-page transactional workflow with database-verifiable output.

### Figure 8 — Dashboard value retrieval

The agent locates the correct chart, identifies “Hewlett-Packard,” reads its percentage, and replies “4.72%.” This is an example-task value, not an aggregate experimental result.

### Figure 9 — Menu navigation

The agent opens the “All” menu, searches or scrolls, and selects the correct “Open” module under “Problem.” The figure emphasizes disambiguation because many applications contain identically named modules.

### Figure 10 — Generated knowledge-base article

The screenshot shows a generated article containing the exact fact that the password for conference room A-561 is `roo918k`, highlighted in context. It demonstrates fact embedding rather than an empirical model result.

### Figure 11 — MiniWoB inside BrowserGym

A chat goal asks the agent to bisect an angle and submit. The browser displays a small geometry task. This shows that BrowserGym relocates the task instruction into chat while retaining the original interactive page.

# 11. Table-by-Table Interpretation

### Table 1 — Best selected agent configurations

The table maps agent, observation, and action flags to GPT-4o, GPT-3.5, and Llama3.

Common selected features are reasoning, action history, visibility-tag extraction, bid-only actions, and individual examples. Coordinates, multiple actions, and error history are absent from every selected final configuration. Llama3 uniquely keeps thought history and focused-element state; GPT models keep last-error information.

### Table 2 — Main performance results

Rows contain benchmark totals and WorkArena/WebArena subcategories. Columns give SR% ± SE for four models.

GPT-4o is the best aggregate performer. GPT-4o-V is slightly better on MiniWoB and WebArena, but slightly worse on WorkArena. List filtering is tied at 0.0% for all agents. The table provides uncertainty estimates, but it does not mark pairwise significance tests.

### Table 3 — GPT-4o ablation

Each row changes one aspect of the initial configuration. Coordinate boxes/actions yield the best MiniWoB score, 72.6 ± 1.0, but no modification beats the WorkArena initial score of 45.5 ± 2.2. This supports benchmark-specific feature effects.

### Table 4 — GPT-3.5 ablation

The initial configuration scores 41.3/8.5 on MiniWoB/WorkArena. Multi-actions and focused-element input tie for the best listed WorkArena mean, 9.4, while removing thought-generation, action history, or adding coordinate-heavy inputs tends to reduce results. No formal significance test is given.

### Table 5 — Llama3 ablation

The initial WorkArena score is 20.0. Removing reasoning or action history lowers it to 8.5. Multiple actions improve MiniWoB but lower WorkArena. This is the clearest tabular evidence for the importance of explicit reasoning and action history.

### Table 6 — Complete WorkArena task inventory

The table lists all 33 task types, instance counts, and oracle Playwright action means ± standard deviations from 10 sampled instances.

Important extrema:

- Highest mean oracle actions: `CreateHardwareAsset`, 47.1 ± 10.9.
- Lowest: single-chart retrieval tasks, 1.0 ± 0.0.
- Filtering tasks: 12.7–19.9 mean actions.
- Most sorting tasks: about 7.4–8.3 actions.
- Total instances: 19,912.

Oracle actions indicate implementation complexity but are not necessarily optimal or human-equivalent.

### Table 7 — Example knowledge-base facts

Examples include:

- conference-room password → `roo918k`;
- office address → `42, Pizza street, New York, USA`;
- CEO name → `Alex Johnson`.

These are synthetic benchmark contents, not real organizational facts.

### Table 8 — Question paraphrases and formatting instructions

Four phrasings ask for Office #456’s address while explicitly requiring street number/name, city, and country. The table shows controlled linguistic variation with output-format constraints.

### Table 9 — Acceptable answer variants

Four alternative renderings normalize abbreviations and punctuation for the office address. This demonstrates tolerance to semantically equivalent answers.

### Table 10 — Complete BrowserGym action space

The table groups primitives into:

- `bid`: fill, click, double-click, hover, press, focus, clear, select, drag/drop;
- `coord`: mouse and keyboard operations;
- `tab`: open, close, focus;
- `nav`: back, forward, URL navigation;
- `misc`: scroll, chat response, no-op;
- `python`: arbitrary Playwright-capable Python, marked unsafe.

It defines the environment’s interface breadth; the final agents use only the bid action set.

# 12. Diagram / Architecture Interpretation

The main architectural diagram is Figure 1b.

1. A user communicates a task through chat.
2. BrowserGym exposes the browser state to the agent.
3. The state may be represented as HTML, AXTree, screenshot, URLs, chat, or error information.
4. The agent chooses an action: element-ID operation, coordinate operation, or code.
5. BrowserGym executes the action in Chromium through Playwright/CDP.
6. The changed page becomes the next observation.
7. This loop continues until validation, termination, or the 15-step cap.

BrowserGym itself does not prescribe the reasoning algorithm. It separates:

- **environment responsibilities:** observations, execution, task lifecycle, validation;
- **agent responsibilities:** feature selection, memory, reasoning, and action generation;
- **benchmark responsibilities:** setup, teardown, validation, and optional oracle.

# 13. Equations and Mathematical Concepts

There are no numbered equations, formal optimization objectives, theorems, or proofs.

The central quantitative definitions are procedural:

- **Success rate:** proportion of episodes/tasks completed successfully under the validator.
- **Bootstrap estimate:** the authors create 1,000 stratified samples of the mean, then report the average and standard deviation of these bootstrap means as SR and SE (§5.2).
- **Ablation difference:** change in SR after modifying one flag from an initial configuration. Such differences are descriptive; no p-values or confidence intervals for pairwise differences are given.

The reported `±` values are standard errors, except Table 6’s oracle-action `±` values, which are standard deviations over 10 randomly sampled instances. These uncertainty types must not be conflated.

# 14. Interpretation and Discussion

The experiments answer the objectives as follows:

- **Benchmark difficulty:** WorkArena is substantially unsolved by the tested agents; its best score is 42.7%.
- **Model dependence:** Performance varies greatly with the underlying LLM, especially on WorkArena.
- **Task dependence:** Knowledge search, catalogs, dashboards, and menus are more tractable for GPT-4o than filtering or sorting.
- **Feature dependence:** More information and more action types do not automatically improve results.
- **Multimodality:** Screenshot augmentation offers only small aggregate changes and slightly reduces WorkArena performance.
- **Context pressure:** Large AXTrees and prompt truncation plausibly contribute to failures, especially for models with shorter limits.
- **Agent memory:** Reinjecting reasoning can preserve useful information but can also preserve mistaken commitments.

[D] A broader interpretation is that WorkArena measures the joint system—model, prompt, observation representation, action interface, validator, and step budget—not the LLM alone. The authors recognize this indirectly through feature ablations but often describe aggregate differences as model capability differences.

## Internal inconsistencies and unresolved points

1. **WebArena score:** p. 2 reports 25.4%, while Table 2 and §5.3 report 23.5% for GPT-4o and 24.0% for GPT-4o-V.
2. **Chain-of-thought claim:** the prose says the conclusion holds clearly for all three models, but no GPT-4o no-thinking ablation appears in Table 3.
3. **“Significantly” terminology:** some prose uses “significantly” without reporting a formal pairwise significance test.
4. **Task/instance wording:** Table 2 labels WebArena as “812 tasks,” whereas §2 describes WebArena as a collection of 190 tasks. The supplied text does not explain whether 812 refers to instances, evaluated goals, or another unit.
5. **Ablation versus final scores:** Tables 3–5 differ from Table 2 because the ablations use a different seed, as disclosed in footnote 8.

# 15. Contributions and Novelty

## Benchmark contribution

WorkArena supplies 33 enterprise task types and 19,912 instances spanning six common interaction categories.

## System contribution

BrowserGym unifies multimodal observations, multiple action abstractions, chat, multi-page support, nested-frame/shadow-DOM handling, task validation, and oracle execution.

## Methodological contribution

The paper defines a benchmark-development contract through `setup`, `teardown`, `validate`, and optional `cheat` functions.

## Dataset contribution

The synthetic knowledge base contains 100 generated articles, controlled question variants, formatting constraints, and acceptable-answer variants.

## Implementation contribution

WorkArena, BrowserGym, and associated agent code are reported as open source. Their external repositories were not inspected.

## Experimental contribution

The authors compare four agent configurations across three benchmark families and conduct feature ablations for GPT-4o, GPT-3.5, and Llama3.

## Empirical contribution

The results expose large model gaps, universal failure on list filtering, limited vision gains, and benchmark-specific effects of memory, coordinates, prompt detail, and multi-action execution.

# 16. Limitations

## Authors' stated limitations

- The experiments are limited to language-model-based web agents (§2, p. 3).
- BrowserGym supplies only the current page observation and no built-in memory (footnote 4, p. 5).
- WorkArena/WebArena HTML is too large, so experiments use only AXTree for those benchmarks (footnote 6, p. 6).
- Prompt content is truncated when it exceeds model-specific limits (§5.1).
- The fixed experimental budget limits seeds to 10 per WorkArena/MiniWoB task and one per WebArena task (§5.2).
- Fifteen steps may be insufficient for some WorkArena tasks unless multiple actions are allowed (§5.2).
- Oracle action counts are not necessarily optimal (Table 6 caption).
- Vision-language performance may be constrained by insufficient screen-related training data, presented as a possible explanation rather than established fact (p. 9).
- Current tasks are largely atomic; more compositional workflows are deferred to future work (§6).

## Additional evidence-based analyst observations

- The benchmark is tied to one enterprise platform and release/version context, limiting direct evidence about other enterprise systems.
- Several task pools are capped at 1,000 randomly chosen instances, but sampling seeds and population composition are not reported.
- Model configurations are selected on MiniWoB and WorkArena, creating tuning exposure to the same benchmark families later used for evaluation, though evaluation uses a different seed.
- The random-search budget and selection criterion are unspecified.
- Success is validator-dependent; the paper does not report validator error audits.
- Only one open-weight model is included in the main table.
- The 15-step cap may confound reasoning quality with trajectory length.
- Synthetic knowledge articles and answers may not reproduce the ambiguity and inconsistency of organic enterprise knowledge bases.
- No human baseline is measured directly on WorkArena.
- No runtime, latency, token consumption, or cost evaluation is reported.
- No pairwise statistical testing accompanies many comparative claims.

# 17. Threats to Validity

These labels are analyst-applied unless explicitly attributed.

## Internal validity

Configuration tuning, prompt truncation, the step cap, and different model context capacities affect outcomes alongside underlying model capability. Ablations alter one listed flag at a time but do not test all interactions.

## Construct validity

Validator success is a reasonable operational measure of task completion, but it may not capture efficiency, safety, explanation quality, recoverability, or user satisfaction. Oracle action count is only an approximate complexity indicator.

## External validity

WorkArena uses real ServiceNow instances but only one enterprise platform and a finite set of atomic tasks. Generalization to other software, organizations, permission structures, or long workflows is untested.

## Statistical conclusion validity

Bootstrap SEs are reported, but no formal pairwise tests, confidence intervals for differences, or multiple-comparison controls are supplied. WebArena uses one seed per task.

## Ecological validity

The interfaces are realistic, but goals are deliberately explicit and benchmark instances are controlled. Real workplace requests may be ambiguous, interrupted, permission-sensitive, or collaborative.

## Reproducibility

Versions, model identifiers, prompt caps, hardware for Llama3, and source repositories are reported. Reproducibility is weakened by absent exact seeds, full prompt text in the paper, random-search details, API decoding settings, and external dependence on cloud instances/models.

## Temporal robustness

Oracle functions are intended to help detect ServiceNow updates, but the paper does not empirically measure benchmark drift.

# 18. Future Work and Open Questions

## A. Author-proposed future work

- Add WebShop and WebVoyager support to BrowserGym.
- Expand WorkArena with compositional workflows.
- Include tasks requiring retrieval, memorization, visual perception, and advanced reasoning.
- Improve multimodal web-agent capability.
- Further study the open/closed-source performance gap.

## B. Additional open questions

- How would results change without the 15-step ceiling?
- What is the independent contribution of model size, context length, training data, and prompting?
- Can specialized interface representations solve the 0% filtering category?
- How accurate and robust are validators under platform changes?
- How do agents compare with humans on completion, time, and error severity?
- What happens under ambiguous, changing, or multi-user instructions?
- Can agents avoid unsafe or irreversible actions while retaining useful autonomy?
- How much do trajectories cost in tokens, latency, compute, and money?
- Do results transfer to other enterprise platforms?
- Can vision help once screenshot use and coordinate grounding are trained specifically for software interfaces?

# 19. Terminology and Notation Glossary

| Term | Meaning in this paper |
|---|---|
| Agent | A system that observes a browser, reasons about a goal, and issues actions |
| API | Application Programming Interface; a machine-facing software interface |
| AXTree | Accessibility tree representing page elements semantically |
| `bid` | BrowserGym’s unique identifier for a page element |
| BrowserGym | The authors’ browser-agent environment |
| CDP | Chrome DevTools Protocol |
| Chain-of-thought | Prompting the model to produce intermediate reasoning before its action |
| Closed-source LLM | A model accessed as a proprietary hosted service here |
| Coordinate action | Mouse/keyboard interaction expressed through screen coordinates |
| DOM | Document Object Model, a structured representation of webpage elements |
| GPT-4o-V | The paper’s screenshot-augmented GPT-4o condition |
| iFrame | A webpage embedded inside another webpage |
| Instance | One concrete parameterization of a task template |
| LLM | Large Language Model |
| MiniWoB | A benchmark of small synthetic web tasks |
| Multi-action | Allowing more than one primitive command in a single agent step |
| Oracle | A hand-coded Playwright procedure that solves a benchmark task |
| POMDP | Partially Observable Markov Decision Process |
| Playwright | Browser automation library used by BrowserGym and the oracles |
| Set-of-Mark | Visual annotation method added to screenshots in the vision condition |
| Shadow DOM | Encapsulated webpage structure that complicates ordinary DOM access |
| SR | Success rate |
| SE | Standard error |
| TGI | Text Generation Inference, used to serve Llama3 |
| UI | Graphical User Interface |
| Validator | Code that checks whether a task was completed |
| WebArena | A benchmark using realistic public-web-like applications |
| WebGum subset | A 56-task MiniWoB subset reported in Table 2 |
| WorkArena | The paper’s ServiceNow enterprise-task benchmark |
| Zero-shot | No task-specific solved examples are supplied; one generic formatting example is used |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| WorkArena task types | 33 | tasks | Six categories | Author-reported | §3, p. 3; Table 6 |
| WorkArena instances | 19,912 | instances | Full benchmark | Author-reported | Fig. 1; Table 6 |
| List instances | 6,900 | instances | 12 tasks | Author-reported | §3.1, p. 3 |
| Form instances | 5,000 | instances | 5 tasks | Author-reported | §3.1, p. 4 |
| Knowledge instances | 1,000 | instances | 1 task | Author-reported | §3.1, p. 4 |
| Catalog instances | 3,550 | instances | 9 tasks | Author-reported | §3.1, p. 4 |
| Dashboard instances | 1,862 | instances | 4 tasks | Author-reported | §3.1, p. 4 |
| Menu instances | 1,600 | instances | 2 tasks | Author-reported | §3.1, p. 4 |
| Cleaned ServiceNow HTML size | 40K–500K | tokens/page | Flat HTML | Author-reported | §3.2, p. 5 |
| GPT-4o WorkArena | 42.7 ± 1.5 | SR% ± SE | Main evaluation | Author-reported | Table 2 |
| GPT-4o-V WorkArena | 41.8 ± 1.7 | SR% ± SE | Screenshot + Set-of-Mark | Author-reported | Table 2 |
| GPT-3.5 WorkArena | 6.1 ± 1.3 | SR% ± SE | Main evaluation | Author-reported | Table 2 |
| Llama3 WorkArena | 17.9 ± 1.5 | SR% ± SE | Main evaluation | Author-reported | Table 2 |
| GPT-4o–Llama3 gap | 24.8 | percentage points | 42.7 − 17.9 | Analyst-derived | Table 2 |
| GPT-4o–GPT-3.5 gap | 36.6 | percentage points | 42.7 − 6.1 | Analyst-derived | Table 2 |
| List-filter result | 0.0 | SR% | All four models | Author-reported | Table 2 |
| GPT-4o knowledge result | 80.0 ± 12.2 | SR% ± SE | WorkArena knowledge category | Author-reported | Table 2 |
| GPT-4o service catalog | 77.8 ± 3.2 | SR% ± SE | WorkArena | Author-reported | Table 2 |
| GPT-4o MiniWoB | 66.1 ± 1.0 | SR% ± SE | 125 tasks | Author-reported | Table 2 |
| GPT-4o WebArena | 23.5 ± 0.7 | SR% ± SE | Main table | Author-reported | Table 2 |
| Original WebArena comparison | 14.4 | SR% | Prior paper as reported here | Author-reported | §5.3, p. 8 |
| Difference from reported prior score | 9.1 | percentage points | 23.5 − 14.4 | Analyst-derived | Table 2; §5.3 |
| Llama3 no-reasoning decline | 11.5 | percentage points | 20.0 − 8.5, WorkArena ablation | Analyst-derived | Table 5 |
| Max episode length | 15 | steps | All tasks | Author-reported | §5.2, p. 7 |
| Seeds per WorkArena/MiniWoB task | 10 | seeds | Evaluation protocol | Author-reported | §5.2 |
| Seeds per WebArena task | 1 | seed | Evaluation protocol | Author-reported | §5.2 |
| Bootstrap samples | 1,000 | samples | Stratified mean bootstrap | Author-reported | §5.2 |
| Knowledge articles/facts | 100 / 100 | count | Synthetic knowledge base | Author-reported | §A.3 |
| Question paraphrases per fact | 10 | alternatives | GPT-4 generation | Author-reported | §A.3 |
| Answer formats requested | 10 | alternatives | GPT-4 generation | Author-reported | §A.3 |
| Highest oracle action mean | 47.1 ± 10.9 | actions ± SD | CreateHardwareAsset | Author-reported | Table 6 |
| Lowest oracle action mean | 1.0 ± 0.0 | actions ± SD | Single-chart tasks | Author-reported | Table 6 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| WorkArena is difficult for tested agents | Best overall SR is 42.7%; filtering is 0% for all | X1–X2, Table 2 | pp. 7–8 | Strong within tested configurations |
| GPT-4o outperforms GPT-3.5 and Llama3 | 42.7 vs. 6.1 and 17.9 on WorkArena; same aggregate ordering elsewhere | Table 2 | p. 7 | Strong descriptive evidence; no pairwise test |
| Enterprise interfaces create long contexts | HTML reported as 40K–500K tokens; Figure 4 distributions | Fig. 4 | pp. 5, 9 | Strong benchmark-description evidence |
| List filters are a central failure mode | Four 0.0% means plus complex widget walkthrough | Table 2, Fig. 5 | pp. 7–8, 14 | Strong observed association; causal source not isolated |
| Vision provides little aggregate benefit | −0.9 WorkArena, +1.6 MiniWoB, +0.5 WebArena points | X3, Table 2 | pp. 7, 9 | Moderate; one visual method/model |
| Reasoning is important | Large drops for GPT-3.5 and Llama3 when disabled | Tables 4–5 | p. 8 | Strong for two models; GPT-4o row absent |
| Action history is important | GPT-3.5 8.5→5.2; Llama3 20.0→8.5 | Tables 4–5 | p. 8 | Strong descriptive evidence |
| More features can hurt | Several additions reduce SR, especially on WorkArena | Tables 3–5 | pp. 8–9 | Strong descriptive evidence; mechanism hypothesized |
| Coordinate features help when spatial precision matters | GPT-4o MiniWoB 68.2→72.6, WorkArena falls to 41.2 | Table 3 | pp. 8–9 | Supports benchmark-dependent value |
| Thought history can impede correction | Lower scores and reported observed persistence | Tables 3–4; prose | pp. 8–9 | Moderate; behavioral mechanism not separately quantified |
| BrowserGym is broadly extensible | Supports three benchmarks and rich task/action APIs | Fig. 1, Table 10, §4.2 | pp. 2, 5–6, 20 | Design claim; external usability not independently tested |
| WorkArena represents daily knowledge work | Six categories and an onboarding workflow | Fig. 2; Table 6 | pp. 3–4, 13 | Plausible coverage argument; no workplace field study |

# 22. Very Simple Explanation

Imagine giving an AI control of a web browser and asking it to do ordinary office jobs: create a user account, filter support tickets, order a laptop, read a chart, or search an internal help article. The researchers built a test called WorkArena to see how reliably AI systems can do those things in ServiceNow, a complicated piece of enterprise software.

The strongest tested agent, based on GPT-4o, succeeded about 43% of the time. Llama3 succeeded about 18%, and GPT-3.5 about 6%. Every agent completely failed the list-filtering category. The problem was not that the instructions were vague—they were deliberately explicit—but that real business websites contain huge page descriptions, hidden controls, custom widgets, and long sequences of interactions.

The researchers also built BrowserGym, which is like a standardized practice room for browser agents. It can show an agent webpage text, accessibility information, screenshots, and errors, and it can let the agent click by element name, use mouse coordinates, open tabs, or run code. Surprisingly, providing more information or more action choices often did not help. Sometimes it distracted the model or forced useful page content to be cut from the prompt.

The main lesson is that modern AI can perform some office-browser tasks, especially knowledge search and product ordering, but it is not yet reliable enough to automate this kind of work generally. WorkArena gives researchers a concrete way to measure improvement.

# Completeness Audit

## Coverage table

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Abstract | Yes | Yes | Fully represented | Orientation and results |
| §1 Introduction | Yes | Yes | Fully represented | Motivation, gap, contributions |
| §2 Related Works | Yes | Yes | Represented in compressed form | Prior-work categories retained; individual citations compressed |
| §3 WorkArena | Yes | Yes | Fully represented | Construction, tasks, challenges, availability |
| §3.1 task categories | Yes | Yes | Fully represented | Counts and validation methods included |
| §3.2 interface challenges | Yes | Yes | Fully represented | Dynamic UI, exotic HTML, large contexts |
| §3.3 availability | Yes | Yes | Represented in compressed form | Open-source and cloud-instance claims included |
| §4 BrowserGym | Yes | Yes | Fully represented | Architecture and implementation |
| §4.1 capabilities | Yes | Yes | Fully represented | Chat, attributes, observations, actions, pages |
| §4.2 experimental framework | Yes | Yes | Fully represented | Four task functions and extensibility |
| §5 experiments | Yes | Yes | Fully represented | Models, protocol, tuning, results |
| §5.1 agent design | Yes | Yes | Fully represented | Inputs, actions, history, retries, models |
| §5.2 protocol | Yes | Yes | Fully represented | Seeds, bootstrap, cap, selection |
| §5.3 results | Yes | Yes | Fully represented | Aggregate and category results |
| §5.4 ablations | Yes | Yes | Fully represented | All three model tables discussed |
| §6 conclusion | Yes | Yes | Fully represented | Conclusions and future work |
| Impact Statement | Yes, text only | Yes | Represented in compressed form | Productivity, accessibility, displacement, security, privacy, environment |
| References | Yes, text only | Partly | Deliberately compressed | Bibliographic list is non-substantive to closed-document synthesis |
| Appendix A.1 | Yes | Yes | Fully represented | Complete task taxonomy and complexity summarized |
| Appendix A.2 | Yes | Yes | Fully represented | Figures 5–9 individually audited |
| Appendix A.3 | Yes | Yes | Fully represented | Generation and validation pipeline |
| Appendix B.1 | Yes | Yes | Fully represented | Table 10 action categories and primitives |
| Appendix B.2 | Yes | Yes | Fully represented | MiniWoB port and Figure 11 |
| Explicit research questions | Yes | Yes | Fully represented | None formally enumerated |
| Explicit hypotheses | Yes | Yes | Fully represented | None formal |
| X1 cross-model evaluation | Yes | Yes | Fully represented | Table 2 |
| X2 category analysis | Yes | Yes | Fully represented | Table 2 |
| X3 vision analysis | Yes | Yes | Fully represented | GPT-4o-V |
| X4 GPT-4o ablation | Yes | Yes | Fully represented | Table 3 |
| X5 GPT-3.5 ablation | Yes | Yes | Fully represented | Table 4 |
| X6 Llama3 ablation | Yes | Yes | Fully represented | Table 5 |
| X7 observation-size analysis | Yes | Yes | Fully represented | Figure 4; exact plotted values unavailable |
| Figures 1–11 | Yes, visually | Yes | Fully represented | Each interpreted individually |
| Tables 1–10 | Yes, visually/textually | Yes | Fully represented | Each interpreted individually |
| Major equations | Yes | Yes | Not applicable | None present |
| Algorithms | Yes | Yes | Not applicable | No formal pseudocode; procedures covered |
| Contributions | Yes | Yes | Fully represented | Benchmark, system, data, methods, experiments |
| Author-stated limitations | Yes | Yes | Fully represented | Consolidated from methods, footnotes, discussion |
| Supplementary material | No | Yes | Missing from supplied material | No separate supplement supplied or mechanically detected |
| External repositories/artifacts | No | Yes | Inaccessible by design | Closed-document mode; not inspected |

## Missing or inaccessible material

- No pages are missing.
- No separate supplementary material was supplied.
- External repositories, live ServiceNow instances, source code, validators, oracle implementations, and cited benchmark artifacts were outside the supplied document and were not inspected.
- Pages 10 and 12 were available as complete extracted text but not visually rendered. They contain the Impact Statement/references and concluding references, with no substantive scientific figure or table.
- Exact underlying task-level trajectories, random seeds, prompts, validator tests, and raw experiment outputs are not included in the paper.

## Uncertain interpretations

- The p. 2 WebArena figure of 25.4% conflicts with the later 23.5% GPT-4o and 24.0% GPT-4o-V results.
- Table 2’s “WebArena (812 tasks)” does not align transparently with §2’s description of 190 tasks.
- Figure 4 supports qualitative scale comparisons, but exact distribution statistics cannot be read because they are not labeled.
- The prose’s “chain-of-thought is crucial in all three agents” is only directly ablated for GPT-3.5 and Llama3 in the supplied tables.
- The claim that no model solved any individual WorkArena task at 100% cannot be reconstructed from category-level Table 2.
- The explanatory claims about distraction, training data, and memory-induced commitment are plausible author interpretations, not isolated causal findings.

## Deliberately compressed material

- The full bibliography was inspected but not reproduced citation by citation.
- Table 6’s 33 individual task rows were summarized by category and important extrema rather than repeated in full.
- Table 10’s closely related mouse/keyboard primitives were grouped while preserving every action category.
- Repeated task captions stating that goals are explicit were condensed.
- Societal-impact prose was summarized because it is prospective discussion rather than evaluated evidence.
- Figure screenshots’ decorative layout and tiny interface labels were omitted unless necessary to understand the workflow.

## Potential omissions

No known substantive section, experiment, figure, table, appendix procedure, major numerical result, contribution, or author-stated limitation from the inventory has been omitted. Bibliographic entries, repeated interface-caption wording, and low-level table rows were deliberately compressed as disclosed above.