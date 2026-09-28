# Stage 0 - Document Accessibility Report

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes |
| Available range | All 33 pages |
| Apparently missing pages | None |
| Native text | Available for every page; no page is classified as scanned or low-text |
| Visual inspection | Partial by page count: rendered pages 1, 2, 4–12, 14–16, 21, 24–25, 27, 29–33 were supplied |
| Substantive figures visually available | Yes: Figures 1–13 are represented on supplied rendered pages |
| Tables | Tables 1–7 are available through extracted text and rendered pages; all principal values are readable |
| Equations | No numbered mathematical equations. The success-rate standard-error expression \(\sigma/\sqrt{N}\) and the POMDP interaction notation are readable |
| Algorithms/code | BrowserGym loop, task definition, agent API, dynamic prompting, and action examples are available as text/code |
| Appendices | Appendices A–H are present on pp. 24–33 |
| Supplementary files | None supplied |
| Referenced external artifacts | GitHub repositories, leaderboard, Reproducibility Journal, experiment traces, websites, and benchmark resources are referenced but not supplied |
| OCR | Not needed for the main text. Extracted code contains artifacts such as `◁arrowhookleft→`, and spacing around some identifiers is unreliable |
| Primary limitations | Pages without renderings were inspected through supplied text only. References were not externally checked. Exact interface text inside some screenshots is too small to read beyond the accompanying text/captions. |

The work is a mixed **computer-systems, benchmark-integration, software-framework, and empirical machine-learning evaluation paper**. Information below is closed-document analysis: author-reported claims are distinguished from direct visual observations and analyst interpretations.

# 1. Plain-Language Orientation

This paper addresses a practical problem in web-agent research: different benchmarks traditionally use different code, task formats, browser interfaces, and evaluation procedures. That makes it difficult to test one agent consistently across many environments or reproduce another group’s results.

The authors present an ecosystem with two central components:

- **BrowserGym** supplies a standardized browser-task interface: agents receive observations, choose actions, and receive rewards and error feedback.
- **AgentLab** supplies tools for constructing agents, launching many evaluations in parallel, recording reproducibility information, inspecting traces, and connecting different language or vision-language models.

The ecosystem incorporates six benchmark families—MiniWoB, WebArena, VisualWebArena, WorkArena, WebLINX, and AssistantBench—although WorkArena is divided into three levels, producing eight result rows.

To demonstrate the system, the authors evaluate one general agent design, **GenericAgent**, with six model backbones. Claude 3.5 Sonnet has the strongest result on most benchmark rows, including 39.1% success on WorkArena L2; GPT-4o leads the visual benchmark at 26.7%. Performance remains very low on WorkArena L3 and AssistantBench, so the experiment also shows that current general-purpose agents remain unreliable (§6, pp. 14–16).

The central contribution is therefore not a new reasoning algorithm alone. It is an interoperable research infrastructure for building, comparing, diagnosing, and reproducing web-agent experiments.

# 2. Document Roadmap

| Pages | Content |
|---|---|
| 1–3 | Abstract and introduction: motivation, fragmentation problem, use cases, and three contributions |
| 3–5 | §2: benchmark and web-agent literature |
| 5–8 | §3: BrowserGym observations, actions, error handling, and task extensibility |
| 8–10 | §4: unified benchmarks, metadata, evaluation settings, and backend preparation |
| 10–14 | §5: AgentLab studies, parallel execution, AgentXRay, reproducibility, agent/model extensibility |
| 14–17 | §6: experiment design, quantitative results, and error taxonomy |
| 17–18 | §7: discussion, limitations, and future work |
| 18–19 | §8: broader economic, safety, and advertising implications |
| 19–23 | References |
| 24–25 | Appendix A: high-level actions and generated action description |
| 26 | Appendix B: benchmark details |
| 27–28 | Appendix C: dynamic-prompting code and an example prompt |
| 29 | Appendix D: GenericAgent flags; Appendix E: benchmark settings |
| 30 | Appendix F: cost/token use; Appendix G begins: runtime and hardware |
| 31–33 | Appendix G runtime table and Appendix H qualitative trace comparison |

Document inventory:

- **Figures:** 13.
- **Tables:** 7.
- **Substantive code/pseudocode objects:** interaction loop, raw/high-level action examples, custom task, study launch/relaunch, custom agent/arguments, and dynamic-prompting agent.
- **Major experiment:** one cross-benchmark evaluation, plus a qualitative two-model trace analysis.
- **Formal hypotheses/RQs:** none explicitly enumerated.
- **Numbered equations/theorems:** none.
- **Appendices:** A–H, all present.

# 3. Background and Context

A **web agent** is software that interprets a goal and operates a web browser on a user’s behalf. It may click buttons, fill fields, navigate pages, open tabs, inspect page content, and return information.

A **large language model (LLM)** processes and generates language. A **vision-language model (VLM)** also consumes images. Web agents may interact through:

- **HTML/DOM:** the webpage’s structural representation;
- **AXTree:** an accessibility-oriented representation of interface elements;
- **screenshots:** pixel-level rendered pages;
- **Set-of-Marks (SoM):** numbered boxes over actionable screenshot elements;
- **coordinates:** direct pointer locations.

The agent–environment loop is described as a **Partially Observable Markov Decision Process (POMDP)**: at step \(t\), the environment provides observation \(o_t\) and reward \(r_t\); the agent returns action \(a_t\) (§3, p. 5). “Partially observable” means the agent may not see all relevant environmental state directly.

The related-work discussion separates:

1. **Benchmarks**, progressing from controlled single-page interactions to live, multimodal, multi-site, and enterprise workflows (§2.1, pp. 3–4).
2. **Agent implementations**, including HTML-based, screenshot-grounded, pixel-level, planning/search, prompting, tuning, and memory approaches (§2.2, pp. 4–5).

This literature review is narrative rather than systematic: it reports no database search, inclusion criteria, screening procedure, or evidence-quality assessment.

# 4. Research Problem and Gap

**Existing problem.** Web agents need to be evaluated across heterogeneous tasks, but benchmark implementations have divergent interfaces, formats, dependencies, and evaluation practices (§1, pp. 2–3).

**Author-attributed shortcomings of prior practice.**

- Research becomes divided into incompatible silos.
- Cross-benchmark comparison is cumbersome.
- Installing multiple environments and adapting agents repeatedly consumes effort.
- Single-benchmark results may reflect benchmark-specific bias.
- Dynamic websites, software changes, stochastic models, and backend state complicate reproducibility.

**Gap.** The authors identify the absence of one extensible environment that combines standardized browser interaction, multiple benchmarks, scalable experiment management, trace inspection, and reproducibility support.

**Motivation.** Standardization could accelerate development, improve comparisons, increase statistical coverage, enable new benchmarks to reuse existing agents, and support accessibility-oriented automation.

**Scope.** This is a research framework, not a consumer product (p. 2, footnote 1). Its empirical evidence concerns GenericAgent and the reported model checkpoints; it does not establish performance for every possible agent architecture.

# 5. Research Questions / Objectives / Hypotheses

The paper states objectives, not formal research questions or hypotheses.

**Framework objectives (§1, p. 3):**

1. Enable design of an agent and straightforward evaluation across existing benchmarks.
2. Enable design of a benchmark and straightforward testing of existing agents on it.
3. Enable comparison of model backbones by swapping the LLM/VLM inside a common agent.

**Experimental objectives (§6, pp. 14–15):**

1. Demonstrate that BrowserGym plus AgentLab supports large-scale experiment creation and management.
2. Assess current model performance across the unified benchmarks.

**Implicit evaluative questions, labeled analyst interpretation:**

- Can one interface expose materially different web benchmarks?
- How strongly does performance vary across model backbones and task families?
- What practical failure and reproducibility problems remain?

No directional hypothesis or preregistration is reported.

# 6. Assumptions / Threat Model

## System assumptions

- Browser tasks can be represented through a Gym-style reset/step loop.
- Task completion can be evaluated by benchmark-specific validators.
- Element identifiers, DOM/AXTree information, screenshots, and browser errors provide sufficient signals for agent operation.
- Suggested action spaces, step limits, task splits, and seed policies preserve benchmark authors’ intended evaluation conditions (§4, p. 10).

## Trusted components

The evaluation relies on BrowserGym, AgentLab, Chromium, Playwright, Gymnasium, model APIs, benchmark backends, validators, and—in some benchmarks—model-based judges. Their correctness is assumed rather than independently audited in this paper.

## Safety boundary

Raw BrowserGym actions can be arbitrary executable Python using a Playwright page object (§3.2, p. 7). The authors explicitly recognize code-execution and web-action risks. An `action_mapping` can constrain agent output to trusted primitives, and protected benchmarks restrict accessible URLs (§7.1, p. 17).

No formal security threat model defines attacker capabilities, protected assets, or security guarantees. The broader-impact section instead identifies prompt injection, information leakage, unwanted transactions, and malicious exploitation as concerns (§8, p. 18).

# 7. Methodology

## 7.1 BrowserGym architecture

BrowserGym exposes a standard interaction loop:

1. Create and reset an environment.
2. Receive observation and metadata.
3. Let the agent choose an action.
4. Execute the action.
5. Return a new observation, reward, termination state, and error information.
6. Repeat until termination or truncation (§3, Fig. 3, p. 5).

### Observation space

It includes (§3.1, pp. 5–7):

- task goal and/or chat history;
- raw DOM and AXTree;
- screenshot as an RGB image;
- open-page URLs and titles;
- active-tab index;
- unique BrowserGym element IDs (`bid`);
- bounding boxes `(left, top, width, height)`;
- visibility ratio from 0 to 1;
- SoM eligibility;
- most recent action error.

The raw structured objects are minimally modified. Agent implementations choose how to filter or serialize them.

### Action space

The unconstrained form is executable Python. The safer default maps textual high-level calls—such as `click`, `fill`, `select_option`, tab operations, navigation, scrolling, and messaging—into Playwright operations (§3.2, pp. 7–8; Appendix A).

### New tasks

A task implements:

- `setup()`: establishes the initial state and returns a textual or multimodal goal;
- `validate()`: checks state after every action and returns scalar reward, completion status, and optionally a chat message (§3.3, p. 8).

## 7.2 Unified benchmarks

BrowserGym exposes benchmark tasks through the same Gymnasium API. Metadata records task attributes, recommended splits, action sets, step limits, seed policies, and dependency graphs (§4, pp. 9–10).

Backends are benchmark-specific. WebArena and VisualWebArena require Docker resets; WorkArena uses a ServiceNow instance; AssistantBench uses the open web; WebLINX is a static, one-step imitation-style dataset (Appendix B, p. 26).

## 7.3 AgentLab

A `Study` groups agents and benchmark episodes, persists results, performs reproducibility checks, retries failed work, and supports parallel execution (§5.1–5.2, pp. 10–11).

- Failed tasks are automatically relaunched up to three times.
- Ray or joblib provides multiprocessing.
- The authors report up to 20 tasks in parallel on a laptop and 50–100 on a larger server in favorable conditions.
- Dependencies restrict (Visual)WebArena concurrency to approximately 2–4 tasks (§5.2, p. 11).
- Experiments used up to 20 parallel jobs (Appendix G, p. 30).

AgentXRay displays goals, prompts, actions, observations, profiling, screenshots, DOM/AXTree material, errors, and step traces (§5.3, Fig. 9).

Reproducibility features log package/benchmark versions, commit hash, operating system, timestamp, metadata, and performance; a journal accumulates results; a ReproducibilityAgent replays actions and produces prompt diffs (§5.4, pp. 11–13).

## 7.4 GenericAgent

GenericAgent uses modular prompting with AXTree content, visibility and clickability tags, focused element, previous action error, complete action/thought histories, chain-of-thought, and concrete/abstract examples (Table 4, p. 29). Standard runs do not use raw HTML, screenshots, SoM, coordinates, planning, self-criticism, or multiple actions per step. VisualWebArena is the exception: `use_screenshot=True`.

Dynamic prompting recursively shrinks prompt components to a token budget instead of simply truncating the end. The paper reports that AXTree content can exceed 100,000 tokens and raw HTML one million tokens (§5.5, p. 14).

Parsing failures trigger up to four answer attempts; four consecutive failures terminate the task as unsuccessful (§6.1, p. 15).

## 7.5 Models and checkpoints

- GPT-4o: 2024-08-06, Azure OpenAI API.
- GPT-4o Mini: 2024-07-18, Azure OpenAI API.
- o1 Mini: 2024-09-12, OpenRouter.
- Claude 3.5 Sonnet: 2024-10-22, OpenRouter.
- Llama 3.1 70B and 405B: OpenRouter (§6.1, p. 15).

## 7.6 Evaluation design

The principal metric is percentage of successfully completed tasks, reported with standard error \(\sigma/\sqrt{N}\). No hypothesis tests, confidence intervals, effect sizes, or multiple-comparison corrections are reported.

Visual inputs are used only on VisualWebArena and only for multimodal models. For WorkArena L3, most non-Claude values come from Boisvert et al. (2024), not newly rerun experiments. Gray zeroes denote budget-driven skipped evaluations, not demonstrated inability (§6.1 and Table 2).

Hardware included Intel Xeon Gold 6126 CPUs at 2.60 GHz and effectively unlimited cluster RAM. WebArena ran on Azure virtual machines with 8 CPUs and 32 GB RAM (Appendix G, p. 30).

# 8. Experiments / Analyses

## X1 — Unified quantitative evaluation

**Purpose:** demonstrate the ecosystem and compare model backbones within GenericAgent.

**Data:** eight benchmark/level rows, with 181–2,650 evaluation episodes per row (Table 5).

**Independent condition:** model backbone.

**Dependent variable:** task success rate.

**Controls:** broadly shared GenericAgent configuration, benchmark-specific recommended settings, and no visual input outside VisualWebArena.

**Results:** Claude leads six of eight rows; o1 Mini narrowly leads WorkArena L1 and AssistantBench; GPT-4o leads VisualWebArena. All systems perform poorly on WorkArena L3.

**Caveats:** missing multimodal results for text-only models; skipped WorkArena L3 evaluations; inherited rather than rerun L3 values; unequal tasks and episode counts; benchmark-specific validation; no formal significance tests.

## X2 — Comparison with an older GPT-4o checkpoint

The authors compare current GPT-4o results with Boisvert et al. (2024):

- WebArena: 23.5% to 31.4%, an **author-reported increase of 7.9 percentage points**.
- WorkArena L2: 3.8% to 8.5%, an **author-reported increase of 4.7 percentage points** (§6.2, p. 16).

They suggest improved reasoning from later training, while also raising possible benchmark exposure in training data. Neither explanation is experimentally isolated.

## X3 — Qualitative error analysis

Section 6.3 proposes six non-exclusive categories: navigation, form handling, task understanding, stuck behavior, information extraction, and external errors. The analysis is explicitly qualitative; no frequencies are reported.

## X4 — Paired task trace

Appendix H compares Claude 3.5 Sonnet and GPT-4o on the same WorkArena L2 task and seed.

- Claude recovers when a label intercepts checkbox pointer events by clicking the label.
- GPT-4o unsuccessfully selects quantity 6, then treats its own earlier reasoning as evidence that the change succeeded and submits the wrong order (pp. 31–33).

This is an illustrative case, not a representative statistical sample.

## X5 — Operational cost and runtime analysis

Tables 6–7 report model-wide token/API costs and Claude benchmark runtimes. These describe resource requirements rather than agent accuracy. Parallelization means cumulative duration is not wall-clock completion time.

# 9. Results

| Finding | Evidence | Qualification |
|---|---|---|
| Claude is strongest on most rows | Best on MiniWoB 69.8%, WorkArena L2 39.1%, L3 0.4%, WebLINX 13.7%, WebArena 36.2%; Table 2 | Six of eight rows, not every row |
| o1 Mini leads two rows | WorkArena L1 56.7%; AssistantBench 6.9% | WorkArena L1 difference from Claude is only 0.3 points, much smaller than reported SEs |
| GPT-4o leads visual tasks | VisualWebArena 26.7% versus Claude 21.0% and GPT-4o Mini 16.9% | Only three multimodal-capable configurations were evaluated |
| WorkArena L2 remains difficult but discriminative | Claude 39.1% versus o1 Mini 14.9% and GPT-4o 8.5% | The paper offers possible, not tested, causal explanations |
| WorkArena L3 is almost unsolved | Claude 0.4%; remaining entries 0.0 | Gray zeroes are skipped evaluations for several models |
| AssistantBench exposes specialization limits | Best GenericAgent result 6.9%; paper cites leaderboard high score 27% | External leaderboard was not supplied or verified |
| Larger open-weight Llama often helps | 405B exceeds 70B on six of seven jointly reported rows | “Significantly” is asserted in prose, but no significance test is given |
| GPT-4o improves over earlier reported results | +7.9 points WebArena; +4.7 points WorkArena L2 | Cross-checkpoint comparison may also be affected by environment or benchmark exposure |
| Costs vary sharply | GPT-4o Mini $75.73 versus o1 Mini $971.12 | Totals exclude VisualWebArena and do not reflect identical evaluated coverage for every model |

**Analyst-derived examples:**

- Claude’s WorkArena L2 advantage over GPT-4o is \(39.1-8.5=30.6\) percentage points.
- GPT-4o’s VisualWebArena advantage over Claude is \(26.7-21.0=5.7\) percentage points.
- Claude’s MiniWoB rate is approximately \(69.8/56.6=1.23\) times GPT-4o Mini’s rate. This ratio should not be interpreted as a controlled causal improvement.

# 10. Figure-by-Figure Interpretation

### Figure 1 — Ecosystem architecture

A component diagram shows agents using AgentLab’s dynamic prompting and unified LLM API, BrowserGym’s benchmark environments, and outputs for reproducibility, leaderboard publication, AgentXRay inspection, and trace datasets (p. 2). Arrows indicate an iterative agent–BrowserGym loop and downstream experiment services. Blue components belong to AgentLab.

### Figure 2 — Rendered BrowserGym environment

A screenshot places chat on the left and a live browser on the right (p. 5). It directly illustrates the dual interaction surface described in §3. No quantitative axes or values are involved.

### Figure 3 — Interaction loop and Python API

The left panel depicts agent action flowing to the environment and observation/reward returning. The right panel maps that abstraction to `reset()` and repeated `step(action)` calls (p. 5). It supports the claim that BrowserGym follows a conventional Gym-style interface.

### Figure 4 — Alternative page representations

Four panels show the same interface as a raw screenshot, SoM overlay, HTML, and AXTree (p. 6). The visible example includes Upvote and Downvote controls and a score of 17,705. It demonstrates that one page may be exposed visually or structurally and that `bid` identifiers align actions with elements.

### Figure 5 — Captured browser-action error

The figure shows a Google search control obscured by autocomplete and a Playwright timeout log (p. 7). It demonstrates that failures are returned in `last_action_error` instead of terminating the environment loop.

### Figure 6 — Raw versus high-level action code

Panel (a) uses Playwright/JavaScript and panel (b) uses `bid`-based primitives or coordinates (p. 7). Raw code is more expressive; primitives are more controllable and less dependent on page internals.

### Figure 7 — Custom task definition

Pseudocode defines setup and validation for an “Einstein birth year” task, beside the rendered environment (p. 8). It demonstrates the minimal task API. The answer “1879” is part of the illustrative validator, not an empirical result.

### Figure 8 — Cross-benchmark API consistency

Screenshots show a MiniWoB task and WebArena task instantiated through similarly structured `gym.make(...)` calls (p. 9). The content differs, while the programming interface remains constant.

### Figure 9 — AgentXRay interface

The rendered dashboard contains task/seed selectors, episode and step information, action/reasoning panels, a profiling timeline, and tabs for screenshots, DOM, AXTree, messages, logs, statistics, and agent information (p. 12). The image establishes interface breadth; tiny individual field values are not confidently readable.

### Figure 10 — Generated action documentation

An example `HighLevelActionSet.describe()` output lists signatures, descriptions, examples, single-action restrictions, and the statement that 20 action types are available (p. 25). It shows how the action vocabulary becomes model-readable prompt material.

### Figure 11 — Dynamic-prompting agent and prompt

The upper portion shows code assembling goal, observation, action specification, and examples, then fitting them to 40,000 tokens. The lower portion shows a WorkArena L2 prompt with task instructions, active tab, AXTree, and interaction history (pp. 27–29). It links AgentLab configuration directly to the model’s input.

### Figure 12 — Successful Claude trajectory

Six panels compress a longer trajectory into navigation, catalog access, hardware selection, product choice, form completion, and order completion (p. 32). The caption explicitly warns that panel “steps” are not actual environment-step numbers. Its principal evidence is successful recovery and task completion.

### Figure 13 — Failed GPT-4o trajectory

Two panels show the failed attempt to set quantity to six and subsequent completion of an incorrect order (p. 33). Together with p. 31, it illustrates reasoning-history confirmation error: the model trusts its stated intention despite failed execution.

# 11. Table-by-Table Interpretation

### Table 1 — Available benchmark characteristics

Rows cover MiniWoB(++), WebArena, VisualWebArena, WorkArena L1–L3, WebLINX, and AssistantBench. Columns report templates, seed diversity, maximum steps, multi-tab support, backend, and citation (p. 9).

Notable contrasts:

- Templates range from 33 (WorkArena L1) to 31,586 (WebLINX).
- Maximum steps range from 1 (WebLINX) to 50 (WorkArena L2/L3).
- WebLINX has no web backend because it is static.
- AssistantBench alone uses the open world-wide web.
- “None” seed diversity means deterministic/no task seeding, not missing information.

### Table 2 — Main success results

Values are success percentages ± standard error; costs are USD; “Steps” is Claude’s average steps per episode (p. 16). Bold formatting marks row leaders. Missing dashes occur for unsupported VisualWebArena configurations. Gray zeroes on WorkArena L3 denote skipped runs.

Claude’s best row is MiniWoB at 69.8%; its worst is WorkArena L3 at 0.4%. GPT-4o’s strongest relative result is VisualWebArena, where it leads at 26.7%.

### Table 3 — High-level action primitives

Appendix A organizes actions into element-ID, coordinate, tab, navigation, and miscellaneous categories (p. 24). It includes interaction, keyboard, upload, navigation, communication, infeasibility reporting, scrolling, and waiting. Figure 10 says 20 action types are exposed; Table 3 lists primitive variants more granularly, so these counts should not be assumed equivalent without the implementation.

### Table 4 — GenericAgent configuration

Table 4 identifies which prompt features were enabled (p. 29). The experiment uses AXTree, focus, current error, action/thought histories, visibility/clickability tags, chain-of-thought, and two example types. VisualWebArena additionally enables screenshots. This table materially defines the tested agent and limits generalization to other configurations.

### Table 5 — Benchmark evaluation settings

The table reports templates/tasks, seeds or split/curriculum, step caps, and resulting runs (p. 29). Key totals are 625 MiniWoB, 812 WebArena, 910 VisualWebArena, 330 WorkArena L1, 235 each for L2/L3, 2,650 WebLINX, and 181 AssistantBench.

### Table 6 — Cost and token use

Totals exclude VisualWebArena (p. 30). o1 Mini is most expensive at $971.12 and GPT-4o Mini least expensive at $75.73. o1 Mini generates 38.11 million output tokens, far above the other models. Prices for the Llama providers may have changed, according to the authors.

### Table 7 — Claude runtime and hardware-related metrics

Columns distinguish total duration, average step duration, environment-only duration, environment time per step, and cumulative steps (p. 31). WorkArena L2 has the largest cumulative duration (23.6 hours) and step count (7,947); VisualWebArena has the slowest average step (14.1 seconds) and environment step (8.8 seconds).

The row labeled “WorkArena” is not explicitly labeled “WorkArena L1,” although Table 2 and the surrounding benchmark structure suggest that interpretation. This remains a table-label ambiguity.

# 12. Diagram / Architecture Interpretation

The ecosystem has three operational layers:

1. **Task environments:** heterogeneous benchmarks keep their own validators and backends.
2. **BrowserGym interface:** converts them into standardized observations, actions, rewards, and termination states.
3. **AgentLab experiment layer:** constructs prompts, connects model APIs, schedules studies, logs traces, supports reproducibility, and exposes analysis/leaderboard outputs.

The control loop is iterative:

\[
\text{goal and page state} \rightarrow \text{agent prompt/model} \rightarrow
\text{action mapping} \rightarrow \text{browser} \rightarrow
\text{new observation/reward/error}.
\]

AgentXRay and reproducibility records consume the logged trace without sitting directly in the control path. Benchmark validators determine whether actions achieved the goal; AgentLab manages repeated episodes and aggregation.

# 13. Equations and Mathematical Concepts

The paper contains no numbered equations, formal optimization objective, theorem, or proof.

## POMDP interaction notation

At step \(t\):

- \(o_t\): observation;
- \(a_t\): agent action;
- \(r_t\): reward.

The environment provides \((o_t,r_t)\), and the agent selects \(a_t\) (Fig. 3, p. 5). The paper does not specify a transition distribution, observation distribution, discount factor, or formal policy objective.

## Standard error

The reported uncertainty is:

\[
\mathrm{SE}=\frac{\sigma}{\sqrt{N}},
\]

where \(\sigma\) is the outcome’s standard deviation and \(N\) is the number of evaluated episodes (§6.1, p. 15). For binary success/failure outcomes, the paper does not further state whether \(\sigma\) uses a sample or population convention. The ± values in Table 2 are standard errors, not confidence intervals.

## Bounding box and visibility

An element’s bounding box is the four-tuple:

\[
(\text{left},\text{top},\text{width},\text{height}),
\]

and visibility is a scalar between 0 and 1 (§3.1, p. 6). These are data representations, not learned equations.

# 14. Interpretation and Discussion

The evidence supports the authors’ primary systems claim: substantially different benchmarks can be exposed through one agent-facing interface, and a shared agent can be executed across them. The supplied code, metadata descriptions, tables, and experiment register jointly support that claim.

The empirical results show that model choice matters greatly even when the surrounding agent is held broadly constant. Claude’s 30.6-point advantage over GPT-4o on WorkArena L2 is particularly large. Conversely, GPT-4o’s lead on VisualWebArena supports the narrower claim that the strongest overall text-oriented result does not guarantee the strongest visual-task result.

The results do not demonstrate that Claude’s computer-use training caused its WorkArena performance. The authors present this as one explanation. Similarly, possible benchmark inclusion in training data is speculation, not established leakage.

The AssistantBench result reveals a generality–specialization tradeoff: the tested agent is designed for broad browser operation, yet performs far below the paper’s cited specialized leaderboard result. Because that leaderboard artifact was not supplied, only the paper’s report can be represented.

The paired trace suggests that access to thought history can have mixed consequences. It supports memory across steps, but a model may mistake its previous stated belief for evidence of successful execution. This interpretation is grounded in one example and should not be generalized quantitatively.

Potential consistency issues:

- The abstract says six models across six benchmarks; Table 2 contains eight rows because WorkArena has three levels.
- Table 1 says six currently supported benchmark families but lists eight benchmark/level rows.
- Table 3’s granular primitives and Figure 10’s “20 different types” use different counting levels.
- Table 7’s “WorkArena” row is not explicitly identified as L1.
- §5.2 reports (Visual)WebArena parallelism of 2–4 tasks due to dependencies, while §7.1 says only one agent can run at a time because of collisions. These may concern different scheduling circumstances, but the paper does not reconcile them.

# 15. Contributions and Novelty

**System contribution:** BrowserGym’s shared environment interface across heterogeneous web benchmarks.

**Benchmark contribution:** addition of WebLINX, VisualWebArena, and AssistantBench, producing six integrated benchmark families.

**Methodological contribution:** standardized observations, actions, metadata, task creation, backend preparation, and benchmark-specific recommended settings.

**Implementation contribution:** AgentLab’s Study API, parallel scheduling, failure relaunch, pluggable agents/models, token-aware dynamic prompting, and cost tracking.

**Reproducibility contribution:** version/environment logging, journal accumulation, replay through ReproducibilityAgent, reproduced-score ranges, and trace release.

**Analysis contribution:** AgentXRay’s step-level visual inspection interface.

**Empirical contribution:** the authors describe their work as the first large-scale multi-benchmark web-agent experiment, comparing six model backbones and populating initial leaderboard entries (§1, p. 3).

No new training algorithm, formal learning objective, theorem, or new foundation model is proposed.

# 16. Limitations

## Authors' stated limitations

- Live sites vary by location, language, time zone, design, content, and advertisements.
- Operating systems and browsers can change rendering.
- Model and task stochasticity reduce exact repeatability.
- API-hosted models can change silently.
- Robot detection—CAPTCHAs, IP limits, behavioral filtering—impairs open-web tasks.
- Concurrent agents can collide through shared mutable databases.
- The synchronous interaction loop can create latency bottlenecks.
- Raw executable actions introduce safety risks.
- GenericAgent is not optimized for AssistantBench information retrieval.
- Only qualitative, not comprehensive quantitative, error analysis is provided.
- Prices, particularly for provider-routed Llama models, may change.
- WorkArena L3 runs were partly skipped or reused for budget reasons.
- Current web agents remain far from robust, especially on WorkArena L3 and open-web research.

## Additional evidence-based analyst observations

- One agent architecture is used, so results conflate model capability with compatibility with GenericAgent’s prompt and action design.
- There are no formal significance tests despite prose using “significantly.”
- Success rates aggregate tasks with potentially different difficulty and validation behavior.
- Episode outcomes may not be independent when they share backends, task templates, or model-service conditions.
- The experiment lacks a systematic ablation of screenshots, thought history, error feedback, examples, or dynamic-prompting choices.
- The comparison against older GPT-4o results does not isolate checkpoint changes from environmental or benchmark changes.
- Some validators use learned judges, introducing unquantified evaluator variability.
- Full traces and leaderboard entries were not supplied, preventing independent trace-wide checking.

# 17. Threats to Validity

**Internal validity:** checkpoint, provider, API load, backend state, software version, retries, website changes, and inherited L3 results may influence model comparisons.

**Construct validity:** binary task success may not reflect partial progress, safety, efficiency, user satisfaction, or recovery quality. WebLINX partial matching also differs conceptually from end-to-end completion.

**Statistical conclusion validity:** standard errors are reported, but no significance tests or confidence intervals support comparative language. Tasks and seeds may create clustering not represented by a simple episode-level SE.

**External validity:** six benchmark families cover synthetic, replicated, enterprise, static-trace, visual, and open-web tasks, improving breadth, but they do not represent all websites or workflows.

**Ecological validity:** live websites and enterprise backends are relatively realistic, yet several benchmarks use replicas or controlled servers. AssistantBench is most exposed to actual open-web variability.

**Reproducibility:** logging and replay mechanisms improve diagnosis but cannot freeze commercial models, live content, localization, advertisements, or anti-bot behavior.

**Safety validity:** the ecosystem has URL restrictions and action mappings, but no experimental safety evaluation or demonstrated containment guarantee.

# 18. Future Work and Open Questions

## A. Author-proposed future work

- Create stronger privacy, policy-compliance, and malicious-interaction safety evaluation.
- Develop low-latency, real-time agents.
- Produce smaller, efficient models for web interaction.
- Improve visual reactivity through computer-level VLMs.
- Adapt inference-time scaling and self-reflection to web tasks.
- Use logged interaction data for fine-tuning.
- Conduct deeper, automated web-agent error analysis (§6.3; §7.2).

## B. Additional open questions

- Which GenericAgent components cause the largest performance changes?
- Does complete thought history improve average success or amplify self-confirmation failures?
- How stable are rankings across model checkpoints and repeated dates?
- Can uncertainty-aware agents verify execution before advancing?
- How should results be normalized across binary, partial-match, learned-judge, and database validators?
- What safety restrictions retain useful capability while preventing arbitrary code or harmful web actions?
- How much benchmark exposure exists in model training data?
- What scheduling design safely increases parallelism without backend collisions?

# 19. Terminology and Notation Glossary

| Term | Meaning in this paper |
|---|---|
| Agent | System that observes a task environment and selects actions |
| AgentInfo | Extra diagnostic data returned with an action |
| AgentLab | Experiment construction, execution, logging, and analysis framework |
| AgentXRay | Interface for inspecting recorded agent traces |
| API | Application programming interface |
| AXTree | Accessibility tree describing interface elements semantically |
| `bbox` | Element bounding box: left, top, width, height |
| `bid` | BrowserGym’s unique identifier for a page element |
| BrowserGym | Standardized environment interface for browser tasks |
| CDP | Chrome Developer Protocol |
| Chain-of-Thought (CoT) | Intermediate model reasoning included in prompts |
| DOM | Document Object Model, the structured webpage representation |
| Episode | One attempted task execution |
| GenericAgent | AgentLab’s configurable general-purpose evaluated agent |
| Gym/Gymnasium | Standard reset/step environment interface |
| IID | Independent and identically distributed |
| LLM | Large language model |
| POMDP | Partially Observable Markov Decision Process |
| Playwright | Browser-automation library used internally |
| Ray/joblib | Parallel-execution backends |
| Reward | Scalar returned by a task validator |
| Seed | Parameter producing a task configuration or repetition |
| Set-of-Marks (SoM) | Screenshot overlay with identifiers around elements |
| Study | AgentLab object grouping and managing evaluation episodes |
| Task template | Task definition that may yield several seeded instances |
| TGI | Text Generation Inference server, mentioned as a model-serving option |
| VLM | Vision-language model |
| \(a_t\) | Action at step \(t\) |
| \(o_t\) | Observation at step \(t\) |
| \(r_t\) | Reward at step \(t\) |
| \(N\) | Number of evaluation episodes in the standard-error expression |
| \(\sigma/\sqrt N\) | Reported standard error |

# 20. Key Numerical Results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Integrated benchmark families | 6 | families | WorkArena levels grouped | Author-reported | §1, pp. 2–3 |
| Compared model backbones | 6 | models | GenericAgent experiment | Author-reported | §6.1, p. 15 |
| MiniWoB templates | 125 | templates | 5 seeds each | Author-reported | Tables 1, 5 |
| WebLINX templates | 31,586 | templates | test split gives 2,650 runs | Author-reported | Tables 1, 5 |
| AssistantBench test tasks | 181 | tasks | from 214 total | Author-reported | Appendix B; Table 5 |
| Claude MiniWoB | 69.8 ± 1.8 | % success ± SE | 625 episodes | Author-reported | Table 2 |
| Claude WorkArena L2 | 39.1 ± 3.2 | % success ± SE | 235 episodes | Author-reported | Table 2 |
| GPT-4o WorkArena L2 | 8.5 ± 1.8 | % success ± SE | 235 episodes | Author-reported | Table 2 |
| Claude–GPT-4o L2 gap | 30.6 | percentage points | \(39.1-8.5\) | Analyst-derived | Table 2 |
| Claude WorkArena L3 | 0.4 ± 0.4 | % success ± SE | 235 episodes | Author-reported | Table 2 |
| GPT-4o VisualWebArena | 26.7 ± 1.5 | % success ± SE | 910 episodes | Author-reported | Table 2 |
| Claude VisualWebArena | 21.0 ± 1.3 | % success ± SE | 910 episodes | Author-reported | Table 2 |
| GPT-4o visual lead | 5.7 | percentage points | \(26.7-21.0\) | Analyst-derived | Table 2 |
| Best AssistantBench result | 6.9 ± 2.2 | % success ± SE | o1 Mini, 181 episodes | Author-reported | Table 2 |
| GPT-4o WebArena change | 23.5 → 31.4 | % success | older vs newer reported result | Author-reported | §6.2, p. 16 |
| WebArena absolute gain | 7.9 | percentage points | \(31.4-23.5\) | Analyst-derived from reported operands | §6.2 |
| GPT-4o WorkArena L2 change | 3.8 → 8.5 | % success | older vs newer reported result | Author-reported | §6.2 |
| L2 absolute gain | 4.7 | percentage points | \(8.5-3.8\) | Analyst-derived from reported operands | §6.2 |
| Automatic parse attempts | 4 | attempts | per step before failure | Author-reported | §6.1, p. 15 |
| Automatic task relaunches | Up to 3 | relaunches | failed Study tasks | Author-reported | §5.1, pp. 10–11 |
| Lowest total model cost | 75.73 | USD | GPT-4o Mini; excludes VisualWebArena | Author-reported | Table 6 |
| Highest total model cost | 971.12 | USD | o1 Mini; excludes VisualWebArena | Author-reported | Table 6 |
| Largest output-token total | 38.11 | million tokens | o1 Mini | Author-reported | Table 6 |
| Longest Claude cumulative duration | 23.6 | hours | WorkArena L2, before parallelization | Author-reported | Table 7 |
| Slowest average Claude step | 14.1 | seconds | VisualWebArena | Author-reported | Table 7 |
| Largest Claude step count | 7,947 | steps | WorkArena L2 | Author-reported | Table 7 |
| Reported prompt fitting limit in example | 40,000 | tokens | Figure 11 code | Visually readable | Fig. 11, p. 27 |

# 21. Claim–Evidence Map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| BrowserGym unifies heterogeneous benchmarks | Shared API, metadata, action/observation definitions, examples | Figs. 3, 8; Table 1 | §§3–4, pp. 5–10 | Strong implementation-level evidence in supplied paper; code repository not inspected |
| AgentLab supports scalable experiments | Study abstraction, retries, Ray/joblib scheduling, runtime reports | X1, Table 7 | §5; Appendix G | Supported descriptively and operationally; scaling curve absent |
| Claude leads most tested rows | Highest value on six of eight result rows | Table 2 / X1 | p. 16 | Strong for reported setup; no formal significance tests |
| GPT-4o is stronger on the visual benchmark | 26.7% versus Claude 21.0% | Table 2 / X1 | p. 16 | Directly supported for VisualWebArena and evaluated checkpoints |
| Current agents remain unreliable | Very low L3 and AssistantBench success | Table 2 | pp. 16–17 | Strong within these benchmarks; not universal to all agents |
| Error feedback can enable recovery | Error returned in observations; Claude example recovers | Figs. 5, 12 / X4 | pp. 7, 31–32 | Mechanism is clear; behavioral evidence is anecdotal |
| Thought history may preserve mistaken beliefs | GPT-4o assumes failed quantity action succeeded | Fig. 13 / X4 | pp. 31, 33 | Strong for this trace only |
| New GPT-4o checkpoint has improved reasoning | Higher WebArena and L2 scores than older report | X2 | p. 16 | Score change is supported; causal explanation is speculative |
| Standardization improves reproducibility | Version logging, journal, replay, standard spaces | §5.4 | pp. 11–13 | Plausible and implemented; reproducibility improvement is not quantitatively measured |
| Cross-benchmark evaluation reduces noise | Broader evidence than one benchmark | Conceptual argument | §4, p. 9 | Author rationale, not directly tested statistically |

# 22. Very Simple Explanation

Imagine that researchers have built several obstacle courses for robots that use websites. One course asks them to click simple buttons, another asks them to shop, another uses office software, and another asks them to research information on the live web. Previously, every course had different controls and setup instructions, so testing the same robot everywhere was difficult.

BrowserGym gives these courses a more consistent set of controls and observations. AgentLab is the experiment manager: it launches many trials, connects different AI models, keeps logs, retries technical failures, and lets researchers inspect exactly what happened.

The authors put six AI models inside the same general agent and tested them broadly. Claude 3.5 Sonnet performed best on most tasks, while GPT-4o performed best on the visual website benchmark. But even the strongest system failed many difficult tasks. One example shows Claude recognizing that a checkbox click failed and trying a better action; another shows GPT-4o incorrectly believing it had changed an order quantity.

So the paper’s main achievement is a shared laboratory for web-agent research. It makes experiments easier to run and compare, but it also demonstrates that reliable, safe, fast browser-operating AI remains an unsolved problem.

# Completeness Audit

| Item | Inspected? | Represented? | Status | Notes |
|---|---:|---:|---|---|
| Abstract | Yes | Yes | Fully represented | Motivation, ecosystem, experiment, and headline results included |
| §1 Introduction | Yes | Yes | Fully represented | Use cases and three contributions covered |
| §2 Background | Yes | Yes | Represented in compressed form | Prior work grouped by benchmark and agent approach |
| §3 BrowserGym | Yes | Yes | Fully represented | Architecture, observations, actions, errors, extensibility |
| §4 Benchmark unification | Yes | Yes | Fully represented | Coverage, metadata, parameters, resets |
| §5 AgentLab | Yes | Yes | Fully represented | Studies, parallelism, XRay, reproducibility, extensibility |
| §6 Experiments | Yes | Yes | Fully represented | Setup, results, and errors separated |
| §7 Discussion | Yes | Yes | Fully represented | Claims, limitations, and future directions covered |
| §8 Broader Impact | Yes | Yes | Represented in compressed form | Employment, safety, prompt injection, advertising, governance |
| Explicit objectives | Yes | Yes | Fully represented | No formal RQs/hypotheses found |
| X1 quantitative experiment | Yes | Yes | Fully represented | Setup and all Table 2 rows addressed |
| X2 older/newer GPT-4o comparison | Yes | Yes | Fully represented | Both reported changes included |
| X3 error taxonomy | Yes | Yes | Fully represented | Six categories included |
| X4 paired trace | Yes | Yes | Fully represented | Claude recovery and GPT-4o failure |
| X5 cost/runtime analysis | Yes | Yes | Fully represented | Tables 6–7 |
| Figures 1–13 | Yes | Yes | Fully represented | All supplied visually; small screenshot text partly unreadable |
| Tables 1–7 | Yes | Yes | Fully represented | Purposes, values, notes, and ambiguities covered |
| Major equations | Yes | Yes | Fully represented | POMDP notation and standard error; no numbered equations |
| Major algorithms/code | Yes | Yes | Represented in compressed form | Interaction, task, action, Study, agent, and prompting code |
| Appendix A | Yes | Yes | Fully represented | Actions and generated description |
| Appendix B | Yes | Yes | Fully represented | Six benchmark-family descriptions |
| Appendix C | Yes | Yes | Represented in compressed form | Code and prompt structure covered; long prompt not reproduced |
| Appendix D | Yes | Yes | Fully represented | GenericAgent flag configuration |
| Appendix E | Yes | Yes | Fully represented | All benchmark run settings |
| Appendix F | Yes | Yes | Fully represented | Model costs and tokens |
| Appendix G | Yes | Yes | Fully represented | Hardware, duration definitions, all runtime rows |
| Appendix H | Yes | Yes | Fully represented | Paired task analysis |
| References | Yes | Yes | Deliberately compressed | Bibliography inventoried as present; individual citations not re-summarized |
| Footnotes 1–20 | Yes | Partly | Represented in compressed form | Substantive notes incorporated; ordinary URLs not repeated |
| External repositories/leaderboard/traces | No | Yes as absent artifacts | Missing from supplied material | Mentioned but not inspected |
| Supplementary material | N/A | Yes as absent | Missing from supplied material | None supplied or mechanically detected |

### Missing or inaccessible material

- BrowserGym and AgentLab source repositories were referenced but not supplied.
- The live leaderboard, Reproducibility Journal, and full experiment traces were not supplied.
- Benchmark websites, validators, containers, ServiceNow instances, and external model documentation were not supplied.
- No separate supplementary file was provided.
- Pages 3, 13, 17–20, 22–23, 26, and 28 were not rendered as images; their supplied native text was inspected. They contain no identified substantive figure omitted from visual inspection.
- Tiny text inside interface screenshots, especially Figure 9 and trajectory panels, is not fully readable independently of captions and nearby prose.

### Uncertain interpretations

- Whether Table 7’s “WorkArena” row means WorkArena L1 is not explicitly stated.
- The 2–4-way parallelism statement in §5.2 and one-agent-at-a-time statement in §7.1 are not reconciled.
- Figure 10’s 20 “action types” and Table 3’s larger number of named primitives may use different counting conventions.
- OCR/extraction artifacts affect some code spacing and line breaks, but not the principal methodology.
- The exact statistical convention used for \(\sigma\) in \(\sigma/\sqrt N\) is unspecified.
- The paper calls some Llama differences “significant” without presenting a significance test.

### Deliberately compressed material

- The bibliography on pp. 19–23 was classified as supporting reference material rather than summarized citation by citation.
- Related work was synthesized by category rather than reproducing every cited study.
- Long source-code listings and the complete example prompt were described structurally rather than copied.
- Repetitive website screenshots in Figures 12–13 were summarized by their distinct task stages.
- Decorative page headers, author affiliations, logos, and interface chrome were omitted as non-substantive.

### Potential omissions

No known substantive section, experiment, figure, table, equation, appendix, contribution, or author-stated limitation from the supplied document inventory is absent from this analysis. External artifacts referenced by the paper remain unassessed because they were not supplied.