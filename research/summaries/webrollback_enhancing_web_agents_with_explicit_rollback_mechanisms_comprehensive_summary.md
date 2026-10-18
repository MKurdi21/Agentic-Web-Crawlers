## Stage 0 — Document Accessibility Report

The supplied work is **WebRollback: Enhancing Web Agents with Explicit Rollback Mechanisms**. All 11 physical PDF pages are supplied as extracted text. Seven pages are also supplied as visible page images: physical pages 1–5, 7, and 8. Physical PDF pages 1–11 correspond to printed proceedings pages 187–197. Throughout this analysis, p. means the physical PDF page, not the printed proceedings page.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied text covers physical pages 1–11, including main text, references, and Appendices A–D. |
| Apparently missing pages | None within the supplied 1–11 sequence. This does not independently establish that no separate artifacts exist. |
| Visual content | Directly inspected images for pp. 1–5, 7–8; text-only inspection for pp. 6, 9–11. |
| Figures | Figures 1–4 are visually available and inspected. |
| Tables | Tables 1–4 are visually available and readable at the level used below. Extracted text helps separate adjacent cells. |
| Equations and algorithm | Algorithm 1 is visually available. No numbered mathematical equations, theorems, or proofs are present in the supplied work. |
| Appendices | A: Extra Results; B: Web Agent Prompts; C: Evaluation Prompt; D: Detailed Settings. All are present in supplied text, although not all their pages have images. |
| Supplementary material | No separate supplementary files were supplied. Dataset and software links appear in footnotes; their targets were not inspected. |
| OCR | No additional OCR was performed or needed for the substantive analysis. Extracted text was checked against supplied images where available. |
| Important limitations | Small uncertainty terms require care; their statistical meaning is not defined in the supplied paper. Figures 3–4 do not label exact plotted values. No independent PDF hashing, code inspection, browsing, or reproduction was performed. |

The supplied SHA-256 is treated as an identifier provided by the user, not as a hash independently verified here. Instructions embedded in the paper's prompt boxes are analyzed as evidence about the system; they are not instructions followed by this analysis.

**Evidence convention:** [A] author-reported; [B] directly observable in a supplied image; [C] analyst-derived from supplied values; [D] analyst interpretation. No external information [E] is introduced. Confidence describes fidelity to the supplied evidence, not independent confirmation of the experiments. HIGH is used for clear text and tables, MEDIUM for qualified interpretation, and UNKNOWN for unavailable details.

## 1. Plain-language orientation

Web agents are language-model systems that repeatedly inspect webpages and choose browser actions. Their challenge is not merely producing an answer: they must navigate changing websites, notice whether actions helped, and recover when a path stops making progress. The authors describe ordinary navigation failures caused by dynamic websites, including removed pages and reorganized layouts. These are reliability problems; the paper does not establish that they are adversarial attacks. [A; pp. 1–2]

WebRollback adds an explicit way to return to an earlier navigation point. One model component chooses the next action, another judges whether the resulting state remains useful, and a third selects an earlier checkpoint if recovery is needed. The distinction is between deciding **when** to abandon a path and deciding **where** to resume. The implemented return operation redirects the browser to a recorded URL. [A; pp. 2–3]

The researchers compare three search strategies on filtered subsets of Mind2Web-Live and WebVoyager: OneWay, BestFirst, and Rollback. They test large instruction-tuned models without task-specific fine-tuning, smaller models after supervised fine-tuning, and two closed-source models on a smaller evaluation subset. The central pattern is higher full-task success for Rollback in the main large-model and fine-tuned-model comparisons, accompanied by fewer explicit state switches than BestFirst. This does not mean Rollback wins every metric: BestFirst sometimes has higher partial-credit scores, and OneWay sometimes takes fewer navigation steps. [A/B; Tables 1–4]

For the user's research question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis**, this paper provides indirect evidence about environmental interaction, accumulated navigation errors, recovery control, and irreversible actions. It does **not** directly compare web agents with standalone large language models, measure attack success, or evaluate a security defense. Any security relevance below is explicitly analyst inference. [D]

## 2. Document roadmap

The inventory contains the following substantive objects:

| ID | Original object | Location | Role |
|---|---|---|---|
| S0 | Abstract | p. 1 | Problem, proposal, and broad evaluation claim. |
| S1 | §1 Introduction | pp. 1–2 | Dynamic-web motivation, search alternatives, and claimed novelty. |
| S2 | §2 Method | pp. 2–3 | Sequential browser interaction and explicit rollback modules. |
| S3 | §3.1 Settings | p. 3 | Environment, baselines, evaluator, repetitions, and budget. |
| S4 | §3.2 Zero-shot | pp. 3–4 | Large open-source models, completion-rate analysis, closed-source subset. |
| S5 | §3.3 Fine-tuning | pp. 4–5 | Teacher/student setup, training sources, and budget scaling. |
| S6 | §3.4 Why Explicit Rollback Helps | p. 5 | Recovery explanation and struggle-ratio. |
| S7 | §4 Conclusion and Discussion | p. 5 | Contribution and irreversible-action challenges. |
| S8 | Limitations | p. 5 | Task scope, model scale, and URL-based rollback limits. |
| S9 | Ethics Statement | p. 5 | Existing model/data safety and bias issues left unaddressed. |
| S10 | References | pp. 5–6 | Bibliographic positioning; cited works were not independently inspected. |
| A1 | Appendix A, Extra Results | pp. 7–8 | Small-model zero-shot results in Table 4. |
| A2 | Appendix B, Web Agent Prompts | pp. 7–9 | Action, critique, and rollback interfaces. |
| A3 | Appendix C, Evaluation Prompt | pp. 9–10 | Automatic scoring procedure and evidential rules. |
| A4 | Appendix D, Detailed Settings | pp. 10–11 | Website exclusions, retained samples, and training framework. |
| F1–F4 | Figures 1–4 | pp. 1, 2, 3, 5 | Search comparison, architecture, completion curve, budget scaling. |
| T1–T4 | Tables 1–4 | pp. 3, 4, 4, 8 | Large-model zero-shot, fine-tuned small models, closed models, untuned small models. |
| ALG1 | Algorithm 1, Search with Rollback | p. 2 | Main procedural outline. |

The paper is an empirical artificial-intelligence and algorithm/system paper. It is not a security experiment, formal proof paper, systematic review, or new benchmark paper. No keywords, explicitly numbered research questions, formal hypotheses, theorems, or standalone numbered equations are supplied.

## 3. Background and context

A **large language model**, or LLM, supplies the decisions within the agent. An **instruction-tuned** model has been prepared to respond to instructions; here the paper uses such models either directly or after further supervised training. **Zero-shot** means the authors directly prompt the model for the target tasks without the fine-tuning procedure used in their other setting. The prompts still provide instructions, observations, and navigation history. [A; §§3.2–3.3]

A **state** is the browser situation at a particular navigation point. An **observation** is the webpage representation presented to the agent. The implementation uses an **accessibility tree**, described as a simplified representation of webpage elements. The action prompt notes that only the current window's tree is shown, so scrolling can reveal additional information. [A; pp. 2–3, 7]

A **trajectory** is the sequence of navigation steps. A **greedy** or OneWay strategy continues along its current path without the proposed explicit multi-step rollback facility. It still has ordinary `goback` and `restart` actions. **Best-first search** uses estimated state values to choose a state, potentially switching branches frequently. **Rollback** returns to an earlier point; in WebRollback, the model explicitly chooses both the need for that return and its destination. [A; pp. 1–3, 7]

The authors discuss majority voting, breadth-first search, beam search, and Monte-Carlo tree search as prior approaches for language-model reasoning. Their stated concern is that maintaining multiple browser environments for parallel interactions is expensive. Their preferred design keeps the browser search serialized while allowing departures from unproductive paths. This is the authors' positioning, not an independently verified survey conclusion. [A; p. 1]

**Knowledge distillation** here means using demonstrations from a stronger teacher model to train smaller models. **Supervised fine-tuning**, or SFT, is the reported full-model training method. **Test-time scaling** means allowing more search steps during evaluation; the study varies the maximum navigation budget rather than reporting a general scaling law. [A; pp. 4–5, 11]

## 4. Research problem and gap

**Existing problem.** Web navigation takes place in changing environments. A plausible action can lead to an unexpected or unpromising state, and an agent may spend subsequent actions trying to recover. [A; p. 1]

**Shortcomings attributed to previous approaches.** OneWay can remain trapped and require repeated back actions or a restart. Parallel search can require maintaining multiple web environments. BestFirst can switch too frequently because a state that eventually leads to success may lack immediate evidence of its future value. Previous backtracking methods are characterized as less direct or less suited to this real-world setting; the authors specifically emphasize multi-step rollback in one operation. [A; pp. 1–2, 5]

**Research gap.** The proposed gap is a flexible serialized navigation strategy that gives a model direct control over when and where to return, instead of relying solely on greedy continuation or always choosing the currently highest-valued state. [A; pp. 1–2]

**Motivation.** The goal is to improve task completion while using the navigation budget effectively and reducing unnecessary switches. The paper's efficiency evidence is mainly navigation-step and state-switch counts. It does not supply a full accounting of model tokens, latency, or monetary costs. [A/D; pp. 3–5]

**Scope.** The evaluated setting is text-based interaction with accessible live websites, filtered for connection stability. Rollback is implemented through URL redirection. Security attacks, standalone-LLM baselines, and general transactional undo are outside the demonstrated scope. [A/D; pp. 3, 5, 10–11]

## 5. Research questions, objectives, and hypotheses

There are no formally enumerated research questions or statistical hypotheses. The following are **author objectives expressed in prose**, organized here for readability:

- O1: Improve recovery from erroneous or unpromising navigation states through explicit rollback. [pp. 1–2]
- O2: Let the model decide both when and where to roll back, including multiple steps in one operation. [pp. 2–3]
- O3: Compare effectiveness and efficiency against OneWay and BestFirst in zero-shot and fine-tuning settings. [pp. 2–4]
- O4: Improve smaller models using demonstrations from a stronger teacher. [p. 4]
- O5: Examine whether additional navigation steps are used productively and explain why explicit rollback helps. [pp. 4–5]

The user's security question is separate from these objectives. A source-grounded security synthesis can ask what properties of interactive agents create additional failure consequences, but this paper alone cannot establish a comparative vulnerability ranking between agents and standalone LLMs. [D; confidence HIGH for this scope boundary]

## 6. Assumptions / Threat Model

The system model is a sequential agent–browser loop. The agent begins at a target website homepage, observes a webpage representation, selects an action, and receives a new observation after execution. The process ends when the agent stops or exhausts the navigation budget. [A; p. 2]

The method assumes that the supplied task and accumulated navigation information are sufficient for model-based judgments about progress. The action module receives task information, previous trace review, rollback experience, previous attempts from the current state, and the current accessibility tree. The critique module receives before/after observations and the action. The rollback module receives indexed prior traces and critique feedback. [A; pp. 7–9]

The implementation records URLs and redirects to one when returning. It does not establish restoration of every aspect of browser or external application state. The rollback prompt also restricts destinations to steps marked `[Checkpoint Saved]`; thus the prompt-level destination set is narrower than an unrestricted reading of all preceding states. [A/D; pp. 3, 9]

There is **no explicit adversarial threat model**: no attacker-controlled content, attacker objective, access privilege, attack budget, security asset, or attack-success metric is defined. The paper treats websites as dynamic task environments. Its evaluation prompt calls the accessibility tree authentic, which is an evidential assumption for scoring, not a demonstrated security guarantee. [A/D; p. 10]

For security research, the relevant analyst inference is that browser actions connect model decisions to persistent environments and potentially irreversible consequences. Whether malicious webpage content can compromise these particular modules is untested. The study provides no basis for asserting prompt-injection resistance or vulnerability rates. [D; pp. 5, 7–10]

## 7. Methodology

### Study design and implementation

This is a comparative empirical study of navigation strategies. Browser automation uses Playwright; the paper does not give a Playwright version. Webpage observations are text-based accessibility trees. The default maximum budget is 16 navigation steps. Experiments are conducted three times and reported as averages. Tables contain ± terms, but the supplied work does not define whether these are standard deviations, standard errors, or another quantity. [A; p. 3]

### Three-module architecture

1. **Action module:** chooses one browser action using the current page, task, trace summary, remembered rollback experience, and previous attempts. Available actions include clicking, typing with Enter by default, scrolling, waiting five seconds, returning to the previous page, restarting at the initial URL, and stopping with an answer or `N/A`. [A; p. 7]
2. **Critique module:** compares observations before and after the action, records useful details, assesses whether the action advances the task, emits a score, and chooses `continue` or `back`. Scores range from 1.0 to 5.0 in increments of 0.5; anchor meanings are stuck/erroneous at 1.0, reasonable/promising at 3.0, and a critical successful intermediate step at 5.0. [A; pp. 8–9]
3. **Rollback module:** selects an earlier saved checkpoint by index and summarizes lessons from the abandoned portion of the trace. Its outputs include analysis, `BackIdx`, and experience. [A; p. 9]

The critique instructions deliberately discourage premature return: an intermediate state can be useful without immediate positive feedback, and `back` should be chosen cautiously because of extra costs. These instructions help explain how Rollback differs from continually selecting the highest-valued state. They do not prove that the model always follows the policy. [A/D; p. 9]

### Algorithmic procedure

Algorithm 1 initializes a trajectory list S, loops up to T iterations, asks the action module for an action, stops if it is `stop`, executes the action otherwise, and then asks for critique. If rollback is selected, the rollback module supplies an index i, the browser returns to S[i], and the list is truncated to S[:i+1]. Otherwise, the current browser state is appended. [A/B; p. 2]

The algorithm is an outline rather than a fully specified executable implementation. It initializes S as empty without explicitly appending the initial state. A first-iteration rollback would therefore need handling not shown. The text describes an initial state and the prompts describe saved checkpoints, but the exact initialization rule is not supplied. This is an analyst observation about pseudocode coverage, not proof of a runtime defect. [D]

### Baselines

**OneWay** is the greedy strategy with ordinary `goback` but without explicit rollback modules. Its Switch value is zero by design, so zero switches does not establish an absence of all backward navigation. **BestFirst** switches according to critique value estimates. **Rollback** uses the explicit when/where decisions. The authors mention preliminary beam-search trials as less effective and efficient, but provide no quantitative beam-search results or setup. [A; pp. 3–4]

### Models and training

Main zero-shot models are Llama-3.3-70B-Instruct and Qwen2.5-72B-Instruct. The smaller models are Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct. Qwen2.5-72B-Instruct supplies teacher demonstrations for fine-tuning the smaller models because the authors consider its overall performance better. GPT-4o-mini and GPT-4o are also evaluated on a 100-instance subset. [A; pp. 3–4]

Training uses the Mind2Web-Live training portion and imitation-learning data from OpenWebVoyager. After similar website filtering, the final training set contains 455 instances. The paper uses full-model SFT with OpenRLHF. A single model is trained in a multitask manner for the different modules, distinguished by their prompts. Learning rate, epochs, optimizer details, batch size, random seeds, hardware, and software versions are not specified directly in the supplied text. An example training-script link is given but was not inspected. [A; p. 11]

### Evaluation data and filtering

After connection testing and filtering, retained test sets contain 42 Mind2Web-Live instances and 342 WebVoyager instances. The reason given is unstable access caused by network problems and anti-scraping techniques. The excluded-site list spans pp. 10–11 and includes, among others, Amazon, Google, GitHub, Booking, TripAdvisor, and several travel, retail, health, and information services. These are excluded identifiers in this evaluation, not a finding about those services' security. [A]

The combined retained test pool is 42 + 342 = **384 instances**, analyst-derived. This does not establish that every plot uses every one of those instances: the budget-scaling analysis uses 100 sampled instances, and the closed-model evaluation also uses a 100-instance subset. The paper does not state that those are the same sample. [C/D]

### Metrics and evaluator

GPT-4o automatically scores trajectories and answers from 0.0 to 1.0. **Full%** denotes full task success; **Partial%** denotes fine-grained partial scores; **Step** is average navigation steps; **Switch** is the number of explicit state switches. The text does not supply a formal aggregation equation for Partial%. **Struggle-ratio** is the proportion of instances requiring recovery. [A; pp. 3–5]

Appendix C asks the evaluator to identify important task criteria and whether they were met. It treats missing required subtasks as failure and says acknowledging failure should not increase the score. It also contains an evidential tension: the evaluator should not make assumptions beyond the accessibility tree, yet is told to believe response content not mentioned in the tree. This is discussed under validity below. [A/D; p. 10]

## 8. Experiments / Analyses

| ID | Experiment | Setup and purpose | Evidence and principal result | Caveat |
|---|---|---|---|---|
| X1 | Large-model zero-shot comparison | Two large instruction-tuned models; two filtered live benchmarks; three strategies; default 16 steps. | Table 1: Rollback has highest Full% in all four model–benchmark blocks. | Partial% and Step are not uniformly best. |
| X2 | Task-finishing rate | Compare cumulative task completion under increasing step limits. | Figure 3: Rollback and OneWay track closely; BestFirst is lower over much of the curve. | Exact values, model identity, and aggregation are not fully specified in the caption. |
| X3 | Closed-source zero-shot subset | GPT-4o-mini and GPT-4o on a randomly selected 100-instance subset. | Table 3: Rollback has highest Full% and Partial% for both models. | Sampling composition and overlap with other subsets are unspecified. |
| X4 | Fine-tuned smaller models | Teacher demonstrations from Qwen2.5-72B; two smaller students; 455 filtered training instances. | Table 2: Rollback has highest Full% in all four blocks. | No detailed training hyperparameters or module-specific ablations. |
| X5 | Maximum-budget scaling | 100 instances sampled from the combined benchmarks; budgets 8, 16, 24, 32. | Figure 4: Rollback is highest overall, with larger visible separations at larger budgets. | Exact bar values and the specific model/aggregation are not identified in the supplied caption and adjacent description. |
| X6 | Recovery/struggle analysis | Compare proportion of instances requiring recovery. | §3.4 reports 19% OneWay versus 7% Rollback. | Sample denominator, coding procedure, and uncertainty are not supplied. |
| X7 | Untuned smaller-model zero-shot comparison | Same two smaller model families without fine-tuning. | Table 4 shows poor absolute success and some exceptions to Rollback dominance. | These are distinct conditions from Table 2; do not merge them. |

X1 addresses O1–O3; X4 and X7 address O4; X2, X5, and X6 address O5. No experiment tests the user's standalone-LLM security comparison. No formal hypotheses are paired with significance tests. The figures and tables support descriptive comparisons rather than a demonstrated causal decomposition of every module's contribution.

## 9. Results

**Large-model full success improves in the main comparisons.** With Llama-3.3-70B on Mind2Web-Live, Full% is 20.92±3.61 for OneWay, 21.16±0.41 for BestFirst, and 24.07±1.42 for Rollback. On WebVoyager it is 38.06±1.70, 39.82±3.16, and 44.30±1.32. Qwen2.5-72B gives 24.53±0.70, 23.82±1.18, and 27.36±0.94 on Mind2Web-Live, and 49.56±1.61, 47.95±2.34, and 51.90±4.24 on WebVoyager. [A/B; T1, p. 3]

**Partial credit reveals a tradeoff.** BestFirst has higher Mind2Web-Live Partial% than Rollback for both large models: 46.45±0.41 versus 45.29±0.20 for Llama, and 48.84±2.30 versus 45.57±1.42 for Qwen. Thus the claim should be higher full completion in these blocks, not universal metric superiority. [A/B]

**Explicit switches decrease relative to BestFirst.** In Table 1, Rollback versus BestFirst Switch values are 5.0 versus 8.1, 3.2 versus 5.3, 4.5 versus 6.3, and 2.1 versus 4.3 across the four blocks. This supports fewer explicit state switches. It does not directly establish lower wall-clock or token cost. [A/B/D]

**Fine-tuning yields much stronger smaller-model results.** For Llama-3.1-8B with Rollback, Full% is 21.70±2.83 on Mind2Web-Live and 37.43±1.17 on WebVoyager after tuning, compared with 0.63±0.89 and 3.23±0.25 in the zero-shot table. For Qwen2.5-7B with Rollback, corresponding tuned values are 20.75±2.67 and 33.82±0.60, compared with 5.03±2.35 and 12.98±1.36 untuned. These are reported condition comparisons, not an isolated estimate of the causal effect of each training ingredient. [A/B/D; T2, T4]

**Closed models show the same main success pattern.** GPT-4o-mini Full% rises from 29.50±0.50 OneWay to 34.85±3.54 Rollback; GPT-4o rises from 38.50±0.50 to 43.50±1.50. The analyst-derived changes are 34.85−29.50 = **5.35 percentage points** and 43.50−38.50 = **5.00 percentage points**, respectively. These are not relative percent improvements. [A/B/C; T3]

**Small untuned models expose limits.** Llama-3.1-8B has identical Mind2Web-Live Full% of 0.63±0.89 for all strategies. Qwen2.5-7B on WebVoyager has slightly higher Full% under BestFirst, 13.16±1.49, than Rollback, 12.98±1.36. Rollback does not solve weak base capability in every condition. [A/B/D; T4]

**Recovery claim.** The authors report struggle-ratios of 19% for OneWay and 7% for Rollback. The analyst-derived difference is 19−7 = **12 percentage points**; a relative reduction would be (19−7)/19 ≈ **63.2%**, but this latter value is a calculation, not an author-reported result. Its inferential strength is limited by missing sample and operational details. [A/C; p. 5]

## 10. Figure-by-figure interpretation

### Figure 1 — Three search strategies

This conceptual diagram has three horizontal trajectory rows: OneWay, BestFirst, and Rollback. Blue blocks indicate navigation states, arrows indicate actions, and dashed red regions highlight problematic or alternative-path situations. It has no numerical axes or statistical uncertainty. [B; p. 1]

OneWay proceeds through successive states and is annotated as getting stuck at errors. BestFirst includes illustrative state values such as 0.45, 0.5, and 0.3, and uses them to motivate a switch to an alternative branch. These numbers are illustrative labels, not measured benchmark results. Rollback labels intermediate choices as continue and then explicitly selects a return point before pursuing a different action. [A/B]

The figure supports the conceptual distinction between value-driven switching and explicit when/where decisions. It does not quantify how often errors occur or prove that rollback always identifies the correct destination.

### Figure 2 — Agent architecture

The browser environment appears above three modules: Action, Critique, and Rollback. Orange arrows connect action execution and environment observations. Internal paths distinguish critique's continue route from its rollback route; the latter passes through the rollback component before the browser is redirected. A dashed boundary groups the agent modules. [B; p. 2]

This is a control-flow diagram, not a performance plot. Its main meaning is that critique can either let navigation continue or initiate a separate destination-selection operation. The diagram is simplified; the detailed prompt inputs, memory summaries, and checkpoint restrictions appear in Appendix B.

### Figure 3 — Cumulative task-finishing rate

The x-axis is number of steps, with visible labels at 2, 4, 6, 8, 10, 12, 14, and 16. The y-axis is Percentage (%), with displayed labels from 0 to 50. The axes are linear. OneWay is red, BestFirst green with dashed styling, and Rollback blue. Markers identify successive plotted points; no error bars or significance symbols are visible. [B; p. 3]

All curves rise as more steps are allowed. Rollback and OneWay remain close, with blue slightly higher near the upper end. BestFirst is lower across much of the later range. The authors interpret this as similar completion pace for Rollback and OneWay, with BestFirst less efficient because of more switching. [A/B; pp. 3–4]

Exact point values are not printed; no exact numerical completion rate is extracted here. The figure's model identity and dataset aggregation are not specified sufficiently in the supplied caption and nearby prose. Its y-values should not be silently substituted for any particular Table 1 row.

### Figure 4 — Performance with larger maximum budgets

This grouped bar chart uses maximum budgets 8, 16, 24, and 32 on the x-axis. The y-axis is Performance, with visible tick labels 0–50 and a plotted range extending slightly above 50. The caption identifies light bar heights as Partial% and darker shaded portions as Full%. OneWay is red, BestFirst green, and Rollback blue. These are overlaid encodings of two metrics, not two quantities to add. [A/B; p. 5]

The bars show broadly similar performance at eight steps and larger separations at higher budgets. Blue is highest overall, with green generally between blue and red. Dark portions also increase with budget. No error bars, exact bar labels, or significance marks are visible. [B]

The authors interpret the result as better use of additional search budget by rollback strategies, especially their method. The experiment uses 100 sampled instances from the two benchmarks combined. Exact percentages, sample composition, and a clearly identified plotted model are unavailable in the supplied description, so the result is retained as a qualitative trend. [A/D; pp. 4–5]

## 11. Table-by-table interpretation

All tables use the same metric order: **Full% / Partial% / Step / Switch**. Higher is preferred for the first two, lower for the latter two. Below, each cell preserves the reported central value and ± term. The meaning of ± is not specified; no table provides p-values or significance markers. Boldface in the source indicates selected favorable values, not a demonstrated significance test.

### Table 1 — Large-model zero-shot results

| Model | Strategy | Mind2Web-Live: Full / Partial / Step / Switch | WebVoyager: Full / Partial / Step / Switch |
|---|---|---|---|
| Llama3.3-70B-Instruct | OneWay | 20.92±3.61 / 41.59±2.75 / 14.4±0.2 / 0 | 38.06±1.70 / 57.55±2.20 / 12.2±0.2 / 0 |
| Llama3.3-70B-Instruct | BestFirst | 21.16±0.41 / 46.45±0.41 / 14.7±0.2 / 8.1±0.1 | 39.82±3.16 / 61.47±3.18 / 12.0±0.1 / 5.3±0.1 |
| Llama3.3-70B-Instruct | Rollback | 24.07±1.42 / 45.29±0.20 / 14.1±0.2 / 5.0±0.3 | 44.30±1.32 / 63.24±2.23 / 11.8±0.2 / 3.2±0.2 |
| Qwen2.5-72B-Instruct | OneWay | 24.53±0.70 / 43.49±0.85 / 13.0±0.1 / 0 | 49.56±1.61 / 65.21±2.54 / 10.2±0.3 / 0 |
| Qwen2.5-72B-Instruct | BestFirst | 23.82±1.18 / 48.84±2.30 / 13.6±0.1 / 6.3±0.1 | 47.95±2.34 / 64.84±3.30 / 10.8±0.1 / 4.3±0.2 |
| Qwen2.5-72B-Instruct | Rollback | 27.36±0.94 / 45.57±1.42 / 13.5±0.2 / 4.5±0.1 | 51.90±4.24 / 69.12±3.79 / 10.2±0.1 / 2.1±0.2 |

Source: p. 3. Rollback wins Full% in all four blocks and has fewer switches than BestFirst. BestFirst wins Mind2Web-Live Partial% for both models. OneWay has the lowest Qwen Mind2Web-Live Step count, and Qwen WebVoyager Step central values tie at 10.2 for OneWay and Rollback. Those exceptions qualify blanket efficiency claims.

### Table 2 — Fine-tuned smaller models

| Model | Strategy | Mind2Web-Live: Full / Partial / Step / Switch | WebVoyager: Full / Partial / Step / Switch |
|---|---|---|---|
| Llama3.1-8B-Instruct | OneWay | 20.75±3.77 / 38.49±2.64 / 14.5±0.1 / 0 | 33.92±1.75 / 52.97±1.68 / 11.3±0.1 / 0 |
| Llama3.1-8B-Instruct | BestFirst | 19.81±0.94 / 38.96±1.42 / 14.8±0.2 / 6.1±0.2 | 32.31±0.44 / 54.59±0.68 / 11.9±0.1 / 4.6±0.1 |
| Llama3.1-8B-Instruct | Rollback | 21.70±2.83 / 41.75±2.50 / 14.2±0.1 / 4.6±0.2 | 37.43±1.17 / 57.29±2.90 / 11.3±0.1 / 2.7±0.3 |
| Qwen2.5-7B-Instruct | OneWay | 13.38±1.57 / 31.42±1.66 / 13.7±0.2 / 0 | 28.78±2.26 / 47.98±1.69 / 10.9±0.1 / 0 |
| Qwen2.5-7B-Instruct | BestFirst | 17.91±2.05 / 37.86±1.86 / 15.0±0.2 / 6.7±0.2 | 30.22±1.21 / 51.92±1.41 / 12.1±0.1 / 4.7±0.1 |
| Qwen2.5-7B-Instruct | Rollback | 20.75±2.67 / 37.74±2.04 / 14.5±0.4 / 5.4±0.1 | 33.82±0.60 / 54.57±1.63 / 11.3±0.2 / 3.1±0.2 |

Source: p. 4. Rollback wins Full% throughout and Partial% in three of four blocks. BestFirst's Qwen Mind2Web-Live Partial% is slightly higher: 37.86 versus 37.74. OneWay uses fewer steps than Rollback in both Qwen blocks, while the Llama WebVoyager central Step value ties at 11.3. All Rollback Switch values remain below BestFirst's.

### Table 3 — Closed-source models on 100 sampled instances

| Model | Strategy | Full% | Partial% | Step | Switch |
|---|---|---:|---:|---:|---:|
| GPT-4o-mini | OneWay | 29.50±0.50 | 49.57±0.62 | 13.0±0.1 | 0 |
| GPT-4o-mini | BestFirst | 28.15±1.15 | 51.19±1.44 | 13.2±0.1 | 7.8±0.3 |
| GPT-4o-mini | Rollback | 34.85±3.54 | 56.82±2.32 | 12.8±0.1 | 6.3±0.3 |
| GPT-4o | OneWay | 38.50±0.50 | 55.17±1.57 | 11.5±0.1 | 0 |
| GPT-4o | BestFirst | 32.83±1.52 | 55.73±0.93 | 12.4±0.1 | 7.0±0.2 |
| GPT-4o | Rollback | 43.50±1.50 | 60.00±1.30 | 11.6±0.2 | 3.5±0.3 |

Source: p. 4. Rollback has the highest full and partial scores for each model and fewer switches than BestFirst. GPT-4o OneWay has a slightly lower central Step count than Rollback. The table does not separately break down the two benchmarks. GPT-4o also serves as the automatic evaluator, a methodological dependence whose effect is not quantified.

### Table 4 — Smaller models without fine-tuning

| Model | Strategy | Mind2Web-Live: Full / Partial / Step / Switch | WebVoyager: Full / Partial / Step / Switch |
|---|---|---|---|
| Llama3.1-8B-Instruct | OneWay | 0.63±0.89 / 19.35±0.87 / 15.9±0.1 / 0 | 3.03±1.59 / 24.90±0.77 / 15.9±0.1 / 0 |
| Llama3.1-8B-Instruct | BestFirst | 0.63±0.89 / 22.08±1.92 / 16.0±0.0 / 9.1±0.5 | 3.13±0.13 / 29.91±1.25 / 15.9±0.1 / 6.6±0.2 |
| Llama3.1-8B-Instruct | Rollback | 0.63±0.89 / 22.14±0.54 / 16.0±0.0 / 8.3±0.2 | 3.23±0.25 / 28.66±1.55 / 15.9±0.0 / 5.6±0.3 |
| Qwen2.5-7B-Instruct | OneWay | 3.77±2.67 / 11.89±2.80 / 15.5±0.4 / 0 | 11.79±0.60 / 22.27±0.30 / 14.5±0.1 / 0 |
| Qwen2.5-7B-Instruct | BestFirst | 1.26±1.78 / 12.23±1.19 / 15.8±0.1 / 12.5±0.7 | 13.16±1.49 / 26.13±1.59 / 14.5±0.1 / 9.4±0.2 |
| Qwen2.5-7B-Instruct | Rollback | 5.03±2.35 / 14.91±2.89 / 15.4±0.2 / 12.0±0.2 | 12.98±1.36 / 26.24±1.25 / 14.4±0.2 / 8.5±0.1 |

Source: p. 8, Appendix A. The authors use these results to motivate distillation and fine-tuning. Absolute full success is low, and step counts frequently approach the 16-step limit. BestFirst beats Rollback on Llama WebVoyager Partial% and Qwen WebVoyager Full%. The three-way Llama Mind2Web-Live Full% tie is an important boundary to the method's improvement claims.

## 12. Diagram / Architecture

Figures 1–2 together distinguish a search policy from the underlying browser interface. The browser executes actions and produces observations. The action component proposes the next operation. The critique component evaluates the new observation in relation to the old one and the target task. A continue decision returns control to ordinary action selection; a back decision activates a separate destination selector. The destination selector chooses a saved index, after which browser navigation and trajectory truncation occur. [A/B; pp. 1–3]

Appendix B adds a memory path absent from the simplified architecture drawing. The critique records useful details because complete accessibility trees are not retained for later steps. The rollback module creates an experience summary of the abandoned path. The action module subsequently receives experience and previous attempts to discourage repetition. Thus returning the browser does not imply erasing all knowledge of the failed branch. [A; pp. 7–9]

There is a representational ambiguity: the rollback prompt describes all prior thoughts, actions, and observations, while the critique instructions state that accessibility trees are not stored for later steps. The supplied work does not precisely define whether later observations are full trees, summaries, or another representation. It is reasonable to infer that summaries help preserve information, but the exact trace schema remains unspecified. [D]

An illustrative explanation, not a reported task, is an agent searching the wrong section of a website, judging that repeated attempts are unproductive, returning to an earlier saved page, and retaining a note that the abandoned section was unhelpful. This illustrates navigation recovery; it does not demonstrate undoing a purchase, email, or other external side effect.

## 13. Equations and mathematical concepts

No numbered equations or formal theoretical results are supplied. The important mathematical content is the state-transition notation and Algorithm 1.

- **s₀:** initial browser state at the target website's homepage.
- **sᵢ:** state at step i.
- **oᵢ:** observation of the current webpage at state sᵢ.
- **aᵢ:** chosen action, which changes sᵢ into sᵢ₊₁ and yields oᵢ₊₁.
- **T:** maximum step budget.
- **S:** stored navigation trajectory in Algorithm 1.
- **c:** critique output used to choose continuation or rollback.
- **i in the rollback branch:** selected trajectory index; this local role should not be confused with the general time-index notation in the prose.

The transition can be described in words as current state plus executed action producing the next state and observation. The paper does not define a probabilistic transition function, reward model, optimization objective, or loss equation, so none is invented here. [A; p. 2]

The assignment `S ← S[:i+1]` retains the trajectory prefix through the selected index and removes the later active suffix. `env.rollback(S[i])` requests the corresponding browser return. The implementation section grounds that request in recorded URL redirection. These operations are essential to understanding the method, but they do not establish full restoration of an application transaction. [A/D; pp. 2–3]

The critique's 1–5 progress score and the final evaluator's 0–1 task score are distinct scales. BestFirst uses value estimates, while WebRollback additionally uses the explicit binary continue/back decision. The supplied paper does not specify a numerical threshold that deterministically converts critique score into back. [A; pp. 3, 8–10]

Derived quantities in this analysis are simple differences or sums. For example, Qwen's WebVoyager full-success gain over OneWay is 51.90−49.56 = 2.34 percentage points. The term percentage points is required because the operands are percentages; a relative increase would require division by 49.56 and is a different quantity. [C]

## 14. Interpretation and discussion

The evidence supports the authors' central descriptive result: explicit rollback improves full completion in the main large-model, fine-tuned-small-model, and closed-model comparisons, while switching less than BestFirst. The method gives the model a distinct choice to keep exploring a path that lacks immediate rewards rather than abandoning it solely because another state has a higher current value. [A/B]

The distinction between partial progress and complete success matters. BestFirst can receive more partial credit on Mind2Web-Live while completing fewer tasks. Therefore, the results suggest that strategies may distribute progress differently across tasks. That explanation is analyst interpretation; the paper does not provide per-instance trajectories sufficient to establish the distributional mechanism. [D]

The efficiency claim is best understood narrowly. Fewer explicit switches and comparable navigation-step counts support a navigation-control advantage. They do not establish reduced total computation because action, critique, and rollback calls can differ in frequency and input length. The supplied work does not provide token, latency, or monetary accounting. [D]

Several consistency checks qualify interpretation. First, the main text's broad success pattern has exceptions in Appendix A. Second, prompt destinations are saved checkpoints rather than necessarily every prior state. Third, pseudocode says `rollback` while the prompt emits `back`; these appear to be corresponding labels, but the conversion is not shown. Fourth, the state-restoration description is broader than the URL-redirection implementation. Fifth, the evaluator's instruction to avoid unsupported assumptions sits uneasily with its instruction to believe answer content absent from the tree. These points are preserved rather than silently reconciled. [A/D]

For the security research question, the strongest supported inference is about **consequences and recovery requirements**, not demonstrated exploitability. A web agent repeatedly converts language-model judgments into environment actions, accumulates a path-dependent trace, and may encounter changes that cannot be undone by revisiting a URL. The paper makes those additional interaction responsibilities concrete. It does not show that the model becomes more susceptible to malicious instructions, nor quantify an increase over standalone LLM vulnerability. [D]

## 15. Contributions and novelty

**Conceptual contribution:** explicit separation of deciding when to retreat and where to return, while retaining a mostly serialized search process. [A; pp. 1–2]

**Algorithmic contribution:** a multi-step rollback operation integrated into action–critique navigation, with trajectory truncation and model-selected return points. [A; pp. 2–3]

**System/interface contribution:** action, critique, and rollback prompts that exchange trace summaries, useful details, previous attempts, and lessons from abandoned paths. These are supplied interfaces, not evidence of a separately released software package. [A; pp. 7–9]

**Training contribution:** use of a larger teacher's demonstrations to train smaller models, with one multitask model supporting module-specific prompts. [A; pp. 4, 11]

**Empirical contribution:** comparisons across two filtered live benchmarks, several model families, zero-shot and fine-tuned settings, step budgets, and a recovery metric. [A; pp. 3–5, 8]

There is no claimed new dataset, benchmark, formal theorem, general transactional rollback system, or security defense established by the supplied work. Novelty relative to cited studies is the authors' positioning; those studies were not independently read for this analysis.

## 16. Limitations

### Authors' stated limitations

1. Evaluation focuses solely on web navigation; extension to other agent tasks is proposed rather than demonstrated. [p. 5]
2. Computational constraints limit fine-tuning to models around 7B parameters; larger tuned models might perform better. The evaluated small models include both 7B and 8B designations. [pp. 4–5]
3. Rollback relies on straightforward URL redirection. Reverting real-world actions may be harder or infeasible when changes are irreversible. [p. 5]
4. The discussion specifically identifies payment processing and sending emails as actions requiring specialized handling. [p. 5]
5. The ethics statement says additional aggressive filtering and model modifications for safety or bias reduction were not performed; offensive, toxic, unfair, or biased behavior remains unaddressed. [p. 5]

### Additional evidence-based analyst observations

The filtered evaluation covers 42 Mind2Web-Live and 342 WebVoyager tasks, rather than the complete original test sets. The connection filter limits the tested environment distribution. Repeated runs and ± values are reported, but their uncertainty definition, seeds, and statistical tests are not. The 100-instance analyses lack fully specified sample composition. Figures 3–4 omit exact numerical point/bar data and a clear model-specific configuration. [D]

Module-specific ablations, independent human evaluator validation, complete runtime costs, and detailed training hyperparameters are absent. The pseudocode and prompt/trace interfaces leave implementation details unresolved. Security threats and attack outcomes are not evaluated. These are limits on what can be concluded, not author-admitted failures beyond the statements identified above. [D]

## 17. Threats to validity

The following labels are analyst categories, not terminology attributed to the authors.

**Internal validity.** Three strategies are compared under a common described environment, but there are no isolated ablations for critique, destination selection, retained experience, or checkpoint policy. The results therefore assess the reported strategy configurations as wholes. Live website changes may affect runs; exact timing and synchronization are not supplied. [D]

**Construct validity.** Full and Partial measure automatic judgments of task completion, not security. The evaluation prompt uses the tree as an evidential anchor yet accepts answer content not mentioned there. This could affect how unsupported answer statements are credited, but the size or direction of any effect is not measured. Struggle-ratio is defined at a high level without enough detail to reproduce its classification. [D; pp. 5, 10]

**Statistical conclusion validity.** Three repetitions are useful descriptive evidence, but undefined ± terms and absent significance testing prevent claims of statistical significance. Numerically close results, such as Qwen's tuned Mind2Web-Live Partial% values of 37.86 and 37.74, should not be treated as decisively different. [D]

**External and ecological validity.** Live websites provide realistic interaction challenges, but connection-based exclusions remove many services. Text-only accessibility-tree observations restrict the evaluated interface. Around-7B fine-tuning and two large zero-shot families do not establish performance for all models or agents. URL return is especially limited for irreversible tasks. [D]

**Reproducibility.** Prompts, model names, data-source references, retained counts, default budgets, and training framework are provided. Exact environment versions, seeds, trained weights, complete hyperparameters, demonstration-generation details, and raw trajectories are not supplied here. Linked artifacts were not accessed, so their availability or completeness remains unknown. [D]

**Security generalizability.** No adversarial manipulation or standalone baseline is tested. The study cannot validate a comparative security claim merely because it concerns web agents. Its legitimate relevance is identifying interaction and recovery mechanisms that a separate security study could investigate. [D]

## 18. Future work and open questions

### A. Future work explicitly proposed by the authors

The authors propose high-stakes action modeling with greater caution and richer state representations before non-revertible transitions. They identify payments and emails as motivating examples. They also suggest extension beyond web navigation and potential gains from fine-tuning larger models. These are future directions, not implemented capabilities demonstrated by the tables. [A; p. 5]

### B. Additional open questions remaining from the evidence

- How closely does URL redirection restore the information and state needed to resume a task?
- What does each module contribute when memory, critique, checkpoint selection, and return behavior are separately controlled?
- Does fewer switching translate into lower total latency, token use, or monetary cost?
- How are saved checkpoints selected, and how is first-step rollback handled?
- How stable are improvements across independent samples, evaluator judgments, and changing website conditions?
- What operational rule determines whether an instance requires recovery for struggle-ratio?
- Can environmental content influence critique, remembered experience, or destination selection in undesirable ways?
- Under a defined security experiment, how would the same underlying model perform as a standalone assistant versus an action-taking web agent?

These are analyst-generated questions, not author claims or completed experiments. The final two relate specifically to the user's research question and require evidence beyond this paper. [D]

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| LLM | Large language model used to generate agent decisions or evaluation judgments. |
| LM | Language model; used especially for the smaller models. |
| Web agent | System that reads webpage representations and chooses browser actions for a task. |
| Accessibility tree | Simplified representation of webpage elements; observations are restricted to the current window. |
| State, sᵢ | Browser situation at a navigation point. |
| Observation, oᵢ | Representation of the webpage available to the agent at that point. |
| Action, aᵢ | Browser operation chosen by the model. |
| Trajectory, S | Ordered navigation record used for continued decisions and return selection. |
| T | Maximum navigation-step budget. |
| Critique | Model-generated assessment of an action and resulting state. |
| OneWay | Greedy baseline without the proposed explicit rollback mechanism; ordinary back/restart actions remain available. |
| BestFirst | Baseline that switches according to estimated state values. |
| Rollback | Proposed strategy with explicit decisions about whether and where to return. |
| Checkpoint | A prior step marked as eligible for return in the rollback prompt. |
| BackIdx | Output field naming the selected prior checkpoint index. |
| Experience | Summary of lessons from an abandoned trajectory segment. |
| Full% | Percentage metric for full task success. |
| Partial% | Percentage-form fine-grained task-completion score. |
| Step | Average number of navigation steps. |
| Switch | Explicit state-switch count; distinct from every possible back action. |
| Struggle-ratio | Proportion of instances requiring recovery. |
| Zero-shot | Direct prompting condition, separate from the paper's task-specific fine-tuning. |
| Distillation | Training smaller models using demonstrations from a stronger teacher. |
| SFT | Supervised fine-tuning; here full-model training with OpenRLHF. |
| Test-time scaling | Increasing allowed navigation steps during evaluation. |
| URL | Web address recorded for return through redirection. |
| ± | Reported uncertainty notation whose statistical definition is not supplied. |

## 20. Key numerical results

The full numerical table ledger is retained in §11. This reference table highlights configuration and interpretation-critical quantities.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Default maximum budget | 16 | navigation steps | Unless otherwise specified | Author-reported | p. 3, §3.1 |
| Repetitions | 3 | runs | Experiments reported as averages | Author-reported | p. 3, §3.1 |
| Retained Mind2Web-Live test set | 42 | instances | After connection filtering | Author-reported | p. 11, App. D |
| Retained WebVoyager test set | 342 | instances | After connection filtering | Author-reported | p. 11, App. D |
| Combined retained test pool | 384 | instances | 42 + 342 | Analyst-derived | p. 11 operands |
| Filtered training set | 455 | instances | Two training sources combined | Author-reported | p. 11, App. D |
| Closed-model subset | 100 | instances | Randomly selected subset | Author-reported | p. 4, T3 |
| Budget-scaling subset | 100 | instances | Combined benchmark sample | Author-reported | p. 4, §3.3 |
| Scaling budgets | 8, 16, 24, 32 | steps | Figure 4 x-axis | Visually readable | p. 5, F4 |
| Evaluator score range | 0.0–1.0 | task score | GPT-4o evaluation | Author-reported | pp. 3, 10 |
| Critique score range | 1.0–5.0, increments 0.5 | progress score | Different from final task score | Author-reported | p. 9, App. B |
| Wait action duration | 5 | seconds | Action prompt | Author-reported | p. 7, App. B |
| Llama70B Rollback Full | 24.07±1.42 | % | Mind2Web-Live, zero-shot | Author-reported | p. 3, T1 |
| Llama70B Rollback Full | 44.30±1.32 | % | WebVoyager, zero-shot | Author-reported | p. 3, T1 |
| Qwen72B Rollback Full | 27.36±0.94 | % | Mind2Web-Live, zero-shot | Author-reported | p. 3, T1 |
| Qwen72B Rollback Full | 51.90±4.24 | % | WebVoyager, zero-shot | Author-reported | p. 3, T1 |
| Qwen72B full-success gain | 2.34 | percentage points | 51.90 − 49.56, WebVoyager Rollback versus OneWay | Analyst-derived | p. 3, T1 |
| Llama8B tuned Rollback Full | 37.43±1.17 | % | WebVoyager | Author-reported | p. 4, T2 |
| Qwen7B tuned Rollback Full | 33.82±0.60 | % | WebVoyager | Author-reported | p. 4, T2 |
| GPT-4o-mini Rollback Full | 34.85±3.54 | % | 100-instance zero-shot subset | Author-reported | p. 4, T3 |
| GPT-4o Rollback Full | 43.50±1.50 | % | 100-instance zero-shot subset | Author-reported | p. 4, T3 |
| GPT-4o Rollback gain | 5.00 | percentage points | 43.50 − 38.50 versus OneWay | Analyst-derived | p. 4, T3 |
| Struggle-ratio | 19 versus 7 | % | OneWay versus Rollback | Author-reported | p. 5, §3.4 |
| Struggle-ratio reduction | 12 | percentage points | 19 − 7 | Analyst-derived | p. 5 operands |
| Llama8B untuned full-success tie | 0.63±0.89 | % | All three strategies, Mind2Web-Live | Author-reported | p. 8, T4 |

No exact Figure 3 points or Figure 4 bar heights are included because their values are not explicitly labeled. All ± terms above are preserved without assigning an unsupported statistical meaning.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Models choose when and where to return. | Separate critique and rollback modules; indexed checkpoint output. | ALG1, F2, App. B | pp. 2–3, 9 | HIGH for described mechanism; correctness of choices not guaranteed. |
| Multi-step return is available in one operation. | Earlier state selection rather than repeated ordinary back actions. | ALG1, F1 | pp. 1–3 | HIGH for design; implemented via URLs. |
| Rollback improves large-model full success. | Highest Full% in four Table 1 blocks. | X1, T1 | p. 3 | HIGH descriptive support; no significance test. |
| Rollback switches less than BestFirst. | Lower Switch in each main comparison block. | T1–T3 | pp. 3–4 | HIGH for explicit switches; total computational cost unmeasured. |
| Partial-credit superiority is not universal. | BestFirst wins both Table 1 Mind2Web-Live Partial% blocks. | X1, T1 | p. 3 | HIGH, directly reported counterqualification. |
| Fine-tuned smaller models show strong gains over their untuned conditions. | Table 2 versus Table 4, including Llama WebVoyager Rollback 37.43 versus 3.23 Full%. | X4, X7 | pp. 4, 8 | HIGH for reported conditions; component causes not isolated. |
| Additional budgets favor rollback strategies. | Increasing grouped bars and authors' interpretation. | X5, F4 | pp. 4–5 | MEDIUM: exact values and plotted configuration incompletely specified. |
| Recovery struggle is lower for Rollback. | 19% OneWay versus 7% Rollback. | X6 | p. 5 | HIGH for reported numbers; MEDIUM for general inference due to missing protocol. |
| URL rollback cannot be assumed to undo irreversible actions. | Explicit discussion of payments/emails and URL limitation. | S7–S8 | p. 5 | HIGH for author-stated limitation. |
| Security relevance is indirect. | Interactive browser loop and irreversible-action discussion, without adversarial evaluation. | Method and discussion | pp. 2, 5 | MEDIUM analyst inference; no standalone-LLM comparison. |
| Evaluator grounding is internally qualified. | Tree-based evidence rule alongside belief in unmentioned answer content. | App. C | p. 10 | HIGH for textual tension; actual scoring impact UNKNOWN. |

## 22. Very simple explanation — Explain Like I'm 15

Imagine asking an AI to find something on a website. It can click links and search, but a sensible-looking path may lead nowhere. A basic agent may keep trying nearby actions or press back several times before finding a useful route again. WebRollback adds a more deliberate recovery process: one part chooses actions, another checks progress, and another chooses an earlier saved place to return to.

The researchers tested this on two sets of real website tasks. Their method usually finished more tasks in the main comparisons and changed between saved states less often than a method that always picks the currently highest-rated state. It did not win every score. Some methods earned more partial credit, and very small models without extra training still performed poorly.

There is also an important catch: going back to an old web address is not the same as undoing everything. If an agent sends an email or makes a payment, returning to the previous page may leave that action completed. The paper explicitly says these cases need more careful handling.

For a security project, this helps explain why an action-taking AI has extra responsibilities: it must manage a changing environment, remember what happened, recover from mistakes, and avoid consequences it cannot reverse. But this paper does not test attackers or compare web agents against standalone chat models. It supports that narrower explanation of interaction risks, not a measured claim that web agents are more vulnerable.

## Completeness Audit

The inventory, not output length, determines coverage. All supplied pages were read as text; only the seven supplied rendered pages were visually inspected. Numerical results were checked against their model, condition, benchmark, metric, and available image. No linked external artifact was reviewed.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue | Yes | Yes | Fully represented | Title throughout; author/venue record below. |
| Abstract | Yes, text and image | Yes | Represented in compressed form | Integrated into §§1, 4–5. |
| §1 Introduction | Yes, text and images | Yes | Fully represented substantively | Motivation, search positioning, and novelty in §§3–5, 15. |
| §2 Method | Yes, text and images | Yes | Fully represented substantively | Modules, transitions, and rollback in §§6–7, 12–13. |
| §3.1 Settings | Yes, text and image | Yes | Fully represented substantively | Models, environment, budgets, metrics, repetitions. |
| §3.2 Zero-shot | Yes, text and images | Yes | Fully represented substantively | Main and closed-model comparisons, completion curve. |
| §3.3 Fine-tuning | Yes, text and images | Yes | Fully represented substantively | Teacher, students, training sources, scaling analysis. |
| §3.4 Why Explicit Rollback Helps | Yes, text and image | Yes | Fully represented substantively | Struggle-ratio and switch explanation. |
| §4 Conclusion and Discussion | Yes, text and image | Yes | Fully represented substantively | High-stakes actions and return limitations. |
| Limitations | Yes, text and image | Yes | Fully represented | Task scope, model scale, URL redirection. |
| Ethics Statement | Yes, text and image | Yes | Represented in compressed form | Filtering, model safety/bias scope, authors' risk position. |
| References | Yes, text; p. 6 text-only | Yes | Represented in compressed form | Relevant categories retained; bibliography not reproduced entry by entry. |
| Explicit research questions/hypotheses | Assessed | Yes | Fully represented as absent | Prose objectives separated from analyst questions. |
| X1 large-model zero-shot | Yes | Yes | Fully represented | Full Table 1 ledger. |
| X2 finishing-rate analysis | Yes, text and image | Yes | Fully represented within resolution | Exact points unavailable. |
| X3 closed-model subset | Yes | Yes | Fully represented | Full Table 3 ledger. |
| X4 fine-tuning | Yes | Yes | Fully represented | Full Table 2 ledger and training details. |
| X5 budget scaling | Yes, text and image | Yes | Fully represented within available detail | No exact bar values or unambiguous model identification. |
| X6 struggle-ratio | Yes | Yes | Fully represented within available detail | Missing denominator and protocol disclosed. |
| X7 untuned smaller models | Yes | Yes | Fully represented | Full Table 4 ledger and exceptions. |
| Preliminary beam-search mention | Yes | Yes | Represented in compressed form | No supplied numerical results or configuration. |
| Figure 1 | Yes, visually | Yes | Fully represented | Illustrative values distinguished from measured results. |
| Figure 2 | Yes, visually | Yes | Fully represented | Browser/module control flow explained. |
| Figure 3 | Yes, visually | Yes | Fully represented within resolution | Axes, encoding, trends, uncertainty disclosed. |
| Figure 4 | Yes, visually | Yes | Fully represented within resolution | Full/Partial encoding and budget conditions preserved. |
| Tables 1–4 | Yes, visually and textually | Yes | Fully represented | Central values and ± terms transcribed in §11. |
| Algorithm 1 | Yes, visually and textually | Yes | Fully represented | Procedure, symbols, and initialization ambiguity. |
| Major equations/theorems | Assessed | Yes | Fully represented as absent | State notation explained; no formal results invented. |
| Contributions | Yes | Yes | Fully represented | Conceptual, algorithmic, interface, training, empirical. |
| Appendix A | Yes, text and images | Yes | Fully represented | Extra results and Table 4. |
| Appendix B action prompt | Yes, text and images | Yes | Represented in compressed form | Inputs, actions, output structure, and main behavioral rules. |
| Appendix B critique prompt | Yes; p. 9 text-only | Yes | Represented in compressed form | Scores, observation comparison, details, cautious back policy. |
| Appendix B rollback prompt | Yes, text-only | Yes | Represented in compressed form | Saved checkpoints, index, and experience summary. |
| Appendix C evaluation prompt | Yes, text-only | Yes | Represented in compressed form | Inputs, criteria, score, evidence rules, tension. |
| Appendix D detailed settings | Yes, text-only | Yes | Represented in compressed form | Filtering rationale, counts, training method, source references. |
| Substantive footnotes | Yes | Yes | Represented in compressed form | Built-in back, rollback index, preliminary search, links, zero-switch convention. |
| Separate supplementary files | None supplied | Not applicable | Missing from supplied material if independently existing | No claim that separate supplements were inspected. |

**Bibliographic record.** Authors: Zhisong Zhang, Tianqing Fang, Kaixin Ma, Wenhao Yu, Hongming Zhang, Haitao Mi, and Dong Yu. Affiliations supplied: City University of Hong Kong and Tencent AI Lab. Venue supplied: Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics, Volume 2: Short Papers, pp. 187–197, March 24–29, 2026. This is an author-provided publication record, not externally verified metadata. [A; p. 1]

**Additional prompt details retained in compressed form.** The action prompt outputs FirstThought, SecondThought, Thought, and Action. It asks the second field to check previous experience and attempts, while the cleaned Thought field avoids explicitly mentioning those fields for training purposes. It prohibits fabricated element identifiers, repeated ineffective actions, and continuous waiting; asks the agent to stop when done; suggests decomposing difficult searches; instructs acceptance of cookie banners; and advises preserving task-specific dates rather than assuming a current date. The critique outputs Observation, Details, Critic, Score, and Action. The evaluator outputs Summary, Thought, Criteria, and Score. These are system-design descriptions, not instructions executed here. [A; pp. 7–10]

### Missing or inaccessible material

No page within the supplied 11-page sequence is missing. Images for pp. 6 and 9–11 were not supplied, so those pages were inspected only through text. Linked datasets, source code, example training scripts, original benchmark contents, model weights, raw trajectories, and any separately hosted artifacts were not inspected. Their existence in a footnote is not evidence that their contents were reviewed. Detailed hyperparameters, seeds, hardware, evaluator validation, raw plot values, checkpoint policy, and struggle-ratio protocol are not specified in the supplied material.

### Uncertain interpretations

The statistical meaning of every ± term is UNKNOWN. The exact plotted model and aggregation for Figures 3–4 are not sufficiently identified. The relationship between full prior observations in the rollback prompt and nonretention of accessibility trees is unresolved. The exact initialization of S, conversion of `back` to `rollback`, and checkpoint-selection procedure are not supplied. The evaluator's mixed grounding instructions are reported without assuming their measured effect. None of these gaps is repaired using outside knowledge.

### Deliberately compressed material

The bibliography, author contact formatting, repeated general effectiveness statements, repeated prompt instructions, and the full excluded-website list are compressed. The exclusion mechanism, representative identifiers, and all retained dataset counts are preserved. Prompt wording is explained by function rather than reproduced in full. Decorative colors and boxes are described only where they encode search or control flow. This compression does not omit a separate reported experiment or result table.

### Potential omissions

Every substantive section, experiment, figure, table, algorithm, appendix, major contribution, and author-stated limitation identified in the supplied inventory has a representation above. Exact unlabeled plot values and absent implementation details remain unavailable rather than omitted as known facts. The principal remaining coverage limits are text-only pages, uninspected linked artifacts, and details the supplied paper does not report. The analysis is comprehensive for the supplied evidence with these explicit boundaries; it is not a reproduction, external literature validation, or direct security comparison.
