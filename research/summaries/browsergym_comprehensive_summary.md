# Stage 0 — Document Accessibility Report

The supplied work is **The BrowserGym Ecosystem for Web Agent Research**, published in Transactions on Machine Learning Research, February 2025. The main document is available as page-numbered extracted text for physical PDF pages 1–33. All 33 page records are represented in the supplied text. This establishes coverage of the supplied 33-page document; it does not independently verify whether additional versions, supplements, or repository artifacts exist.

Direct visual inspection was possible for the 23 supplied page images: pp. 1, 2, 4–12, 14–16, 21, 24, 25, 27, and 29–33. Pages 3, 13, 17–20, 22, 23, 26, and 28 were inspected through supplied text only. Figures 1–13 and Tables 1–7 are visually available on the rendered pages. Small interface text inside screenshots, especially Figures 9, 12, and 13, cannot always be independently read with confidence. Their captions, larger labels, and associated prose are readable. No screenshot-level numerical estimate is substituted for a reported result.

The main statistical expression, σ/√N, is readable in text and on p. 15. There are no numbered mathematical equations, theorems, or proofs in the supplied work. Appendices A–H are present on pp. 24–33, despite the accessibility metadata reporting no detected appendix pages. This is a metadata–content discrepancy: the actual headings and text establish appendix presence. No separate supplementary files, experimental traces, software repositories, leaderboard contents, or reproducibility journal were supplied. Their existence or release is author-reported, and their contents were not reviewed.

OCR was not performed and is unnecessary for most content because extracted text and visual renderings are supplied. Extraction artifacts occur in code wrapping, quotation marks, table alignment, and arrow-like continuation symbols. Code examples are therefore interpreted as illustrative pseudocode rather than certified executable programs. The failed local-image message referring to `-` does not invalidate the 23 successfully supplied images; no content can be recovered from that failed path.

**Evidence labels used throughout:** [A] author-reported; [B] directly observable in supplied visuals; [C] analyst-derived, with calculation disclosed; [D] analyst interpretation. No [E] external information is used. Confidence is HIGH for clear source statements and readable table values, MEDIUM for bounded interpretation or visually compressed interface details, LOW where a conclusion would require missing evidence, and UNKNOWN where the supplied paper does not establish an answer.

# 1. Plain-language orientation

[A] This is a systems and benchmark paper with an empirical evaluation of web agents. A web agent is a conversational assistant that can operate a browser: it reads a page, decides what to do, clicks or types, observes the result, and repeats. The paper addresses a practical research problem: different web-agent benchmarks use incompatible code and evaluation procedures, making it difficult to compare agents fairly or reproduce results.

The researchers extend **BrowserGym**, which supplies a common interface between agents and browser tasks, and introduce **AgentLab**, which helps create agents, run experiments, record results, and inspect individual decisions. BrowserGym standardizes observations and actions; AgentLab organizes the experiments around that interface. The contribution is an ecosystem for conducting research, not a consumer assistant product. This boundary is stated in the footnote on p. 2.

[A] To demonstrate the ecosystem, the authors evaluate a shared agent implementation, GenericAgent, with six language-model backbones across six benchmark families. WorkArena appears at three difficulty levels, so the principal results table contains eight benchmark rows. Claude 3.5 Sonnet performs best on most rows, GPT-4o performs best on VisualWebArena, and o1 Mini has the highest reported means on WorkArena L1 and AssistantBench. Even strong models struggle with difficult tasks: Claude reaches only 0.4 ± 0.4% on WorkArena L3. These are task-performance results, not security attack-success measurements.

[D] For the requested research question, **Why Are Web AI Agents More Vulnerable Than Standalone LLMs? A Security Analysis**, the paper is relevant because it describes the mechanisms that connect model outputs to executable code, browser actions, external pages, and state-changing transactions. It explicitly warns about arbitrary untrusted code and discusses prompt-injection consequences. However, it does **not** experimentally compare the vulnerability of web agents with standalone large language models. Its security relevance is architectural and conceptual, with author-stated risk discussion; comparative vulnerability magnitude remains UNKNOWN.

# 2. Document roadmap

The inventory is the denominator for coverage, rather than the length of this explanation.

| Inventory ID | Original component | Physical pages | Function |
|---|---|---|---|
| FRONT | Title, contributor roles, affiliations, abstract | 1 | Identity and high-level claims |
| S1 | §1 Introduction | 1–3 | Motivation, use cases, three contributions |
| S2 | §2 Background and Related Works | 3–5 | Positioning within benchmarks and agent implementations |
| SS2.1 | §2.1 Web Agent Benchmarks | 3–4 | Benchmark development and scope |
| SS2.2 | §2.2 Web Agent Implementations | 4–5 | Interaction, reasoning, training, frameworks |
| S3 | §3 BrowserGym | 5–8 | Browser environment and extension interfaces |
| SS3.1 | §3.1 Extensive Observation Space | 5–7 | Page representations, tabs, goals, errors |
| SS3.2 | §3.2 Expandable Action Space | 7–8 | Raw code, action mapping, high-level primitives |
| SS3.3 | §3.3 Extensibility: create your own task | 8 | Setup and validation methods |
| S4 | §4 Unification of Web Agent Benchmarks | 8–10 | Common interface, metadata, suggested settings, resets |
| S5 | §5 AgentLab | 10–14 | Experiment management and agent construction |
| SS5.1–SS5.3 | Launching, parallel experiments, AgentXRay | 10–12 | Runs, retries, dependencies, trace inspection |
| SS5.4.1–SS5.4.2 | Reproducibility factors and features | 11–13 | Sources of drift and tracking/replay mechanisms |
| SS5.5–SS5.6 | Custom agents and custom LLM/VLM interfaces | 13–14 | Agent logic, serialization, prompts, model adapters |
| S6 | §6 Experiments | 14–16 | Demonstration objectives, setup, results, errors |
| SS6.1–SS6.3 | Setup, Results, Errors | 15–16 | Models, settings, performance, qualitative diagnosis |
| S7 | §7 Discussion | 17–18 | Synthesis, limitations, future directions |
| SS7.1 | §7.1 Limitations | 17 | Reproducibility, risks, robot detection, collisions, synchrony |
| SS7.2 | §7.2 Avenue for Future Work | 18 | Safety, speed, smaller models, vision, scaling, fine-tuning |
| S8 | §8 Broader Impact | 18–19 | Automation, displacement, security, advertising |
| REF | References | 19–23 | Bibliographic provenance, not independently validated |
| A1–A8 | Appendices A–H | 24–33 | Actions, benchmark details, prompts, flags, settings, costs, runtime, case study |

Figures F1–F13 correspond to original Figures 1–13. Tables T1–T7 correspond to original Tables 1–7. ALG1–ALG7 identify illustrative implementation examples: the environment loop, raw/high-level actions, task setup/validation, Study launch/relaunch, agent/AgentArgs interfaces, dynamic prompting, and the serialized example prompt. E1 identifies the unnumbered standard-error expression. X1 is the main multi-model evaluation; X2 is the historical GPT-4o comparison; X3 is cost accounting; X4 is runtime accounting; X5 is the two-model qualitative task trace. O1 and O2 are the explicit experimental objectives. No formal hypotheses are stated.

The document moves from motivation to implementation, then to benchmark integration, experimentation, and limitations. The appendices materially qualify the main results: they specify evaluation logic, enabled prompt flags, sampling, excluded cost conditions, runtime interpretation, and the concrete mechanism behind one failure.

# 3. Background and context

[A] A **large language model (LLM)** supplies the agent’s language-based reasoning and action selection. A **vision-language model (VLM)** can also use images. In this paper, model and agent are different objects: GenericAgent builds prompts, manages history, parses responses, and chooses an action interface; the backbone model supplies responses within that structure. Reported performance therefore concerns a model operating inside this agent configuration.

A **user interface (UI)** is the human-facing browser surface. The paper contrasts UI manipulation with software control through an **application programming interface (API)**. UI agents may interact with software even when dedicated APIs are absent. The authors motivate this through repetitive tasks, compatibility, accessibility, and the possibility of visually inspecting actions, rather than through a demonstrated security advantage.

The **Document Object Model (DOM)** is the structured page representation supplied by BrowserGym. The **accessibility tree (AXTree)** is another structured representation, exposing information such as element roles and names. The paper supplies both as observation objects extracted through the **Chrome Developer Protocol (CDP)**. It does not require every agent to use the same text rendering of these objects.

A **BrowserGym ID (bid)** is a generated element identifier inserted into the DOM and AXTree. It lets an agent refer to a specific page element without constructing a complex selector. A **bounding box (bbox)** gives left, top, width, and height, and a visibility scalar ranges from 0 to 1. A screenshot represents rendered visual content that structured text does not fully convey, including overlap, image contents, colors, and fonts.

**Set-of-Marks (SoM)** places identifiers or boxes over screenshot elements. This is a supported observation capability, but Table 4 shows SoM disabled in the reported experiments. VisualWebArena uses screenshots; the supplied table does not state that it enables SoM.

An **episode** is a task execution under a particular setting or seed. A **seed** selects task variation where supported. A **task template** can generate multiple configurations; it is not necessarily one evaluated episode. A **curriculum** is the preset selection used for WorkArena L2/L3. A **trace** records the step-by-step observations, prompts, actions, and related information for inspection.

The paper describes the interaction as a **Partially Observable Markov Decision Process (POMDP)**: the agent acts on observations, receives a reward, and continues until termination or truncation. It does not supply a complete formal transition model or probabilistic derivation. This abstraction organizes the interface rather than providing a theoretical result.

# 4. Research problem and gap

[A] The existing problem is benchmark fragmentation. As more benchmarks appear, each brings evaluation code, setup requirements, formats, and integration conventions. This produces research silos and makes cross-benchmark comparison cumbersome. The authors identify inconsistent practices and incompatible implementations as obstacles to fair comparison, reliable signals, and reproducibility (pp. 1–3).

The claimed gap is a common ecosystem that supports three activities: implementing a new agent and testing it on existing benchmarks; implementing a new benchmark and testing existing agents; and changing only the backbone model within an existing agent. The paper aims to reduce adaptation effort and enable larger, more consistent experiments.

The scope includes synthetic pages, self-hosted replicas of everyday sites, enterprise workflows, open-web information retrieval, and static human-action prediction. It does not unify every benchmark mentioned in related work. GAIA, WebVoyager, WebShop, and Mind2Web-live are described as considered for future integration on p. 10. Figure 1’s inclusion of Mind2Web-live is therefore not sufficient evidence of a completed integration.

[D] For security research, this gap matters because incompatible environments also hinder systematic comparisons of defenses or policy enforcement. The paper itself gives the example of a future compatible security benchmark evaluating existing agents without adapting their code (p. 9). This is a proposed benefit, not a reported security experiment.

# 5. Research questions / objectives / hypotheses

[A] The authors state two experimental objectives in §6, p. 14:

1. **O1:** demonstrate how AgentLab integrated with BrowserGym supports creation and management of web-agent experiments.
2. **O2:** assess the performance of contemporary models on the integrated benchmarks.

The broader ecosystem use cases on p. 3 are agent development, benchmark development, and backbone-model comparison. The three major contributions are benchmark unification, AgentLab tooling, and a large-scale empirical demonstration.

No numbered research questions or formal hypotheses are stated. Questions about whether screenshots help or whether one LLM is better than another appear on p. 9 as examples motivating broader evaluation. They should not be converted into completed hypothesis tests. In particular, the paper does not conduct a controlled screenshot ablation across the same task/model combinations.

[D] The user’s security question is an external analytical objective applied to this supplied paper. This report uses the architecture and risk discussion to identify plausible mechanisms of added exposure and impact. It does not relabel that objective as the authors’ own experimental question.

# 6. Assumptions / threat model

[A] There is no formal adversarial threat model, attacker taxonomy, attack budget, or security theorem. The operational system consists of an agent, browser/chat environment, benchmark task logic, model service, and experiment runner. BrowserGym relies on Chromium and Playwright; task validation depends on benchmark-specific logic or evaluators.

The raw action interface accepts executable Python and exposes a Playwright page object plus functions for messaging and infeasibility reporting. The authors explicitly acknowledge vulnerabilities from arbitrary untrusted code (p. 7). They offer action mapping to restrict what can be expressed, including parsing a predefined action vocabulary into code described as safe and trusted (p. 8). The paper does not provide a sandbox specification, adversarial parser evaluation, formal isolation guarantee, or proof that every custom mapping is safe.

[A] The broader-impact section identifies prompt injection as a possible mechanism for leaking sensitive company information, authorizing unwanted transactions, or causing other harm (p. 18). The limitations section says open-web action on a person’s behalf can have consequences, and reports URL protection for MiniWoB, WorkArena, and WebArena/VisualWebArena plus landing-page warnings (p. 17). The implementation details and effectiveness of URL protection are not supplied.

[D] The relevant trust boundaries are the boundary between user goals and page observations, between model-generated action text and executable browser operations, and between a task episode and shared backend state. These are analyst interpretations of described components. The paper does not test whether untrusted page instructions cross the first boundary or quantify a successful attacker’s capabilities.

[D] The distinction from a standalone chat model is primarily consequential authority in this evidence: browser actions can change records or place orders. The authors’ comparison on p. 18 is a risk argument contrasting jailbreaking a language model with compromising an agent. It is not a matched empirical comparison establishing that agent models are more easily manipulated.

# 7. Methodology

## 7.1 BrowserGym environment

[A] The agent receives an observation and returns an action. The gymnasium interface creates an environment, resets it, and repeatedly calls `env.step(action)`. The returned values include observation, reward, termination, truncation, and auxiliary information. Chromium and Playwright implement browser interaction (p. 5, Figure 3).

The observation space includes page DOM and AXTree objects; element IDs, bounding boxes, visibility and SoM indicators; a raw RGB screenshot; open-page URLs and titles; the active-page index; goal or chat messages; and the last action’s error (pp. 5–7). BrowserGym leaves preprocessing and prompt formatting to the agent, while supplying utility conversions.

The task goal and chat history are separate representations. A non-interactive goal is inserted into chat, but later chat messages are not copied back into the original goal. The authors recommend using chat messages for interactive compatibility. This matters because reading a fixed goal object alone could miss later interaction; no interactive benchmark experiment is reported here.

Playwright exceptions are caught and returned through `last_action_error` instead of breaking the loop. This gives an agent an opportunity to correct its next action. Opportunity is not guaranteed recovery: Appendix H shows a model proceeding after an unsuccessful action.

## 7.2 Actions and task extension

[A] Raw Python offers expressive browser manipulation, including JavaScript execution through Playwright. An optional `action_mapping` converts a constrained input format into executable Python. The default HighLevelActionSet turns predefined function calls into Playwright code and provides methods to describe available actions and translate them to code (pp. 7–8).

Custom tasks implement `setup()` and `validate()`. Setup prepares the browser and returns a goal, possibly containing text and images. Validation runs after every executed action, examines the page and chat history, and returns a scalar reward, a done flag, and an optional chat message. The Figure 7 example stops after the first assistant answer and checks whether it contains the expected year. This illustrates the interface; it is not a general correctness validator.

## 7.3 Benchmark integration and validation

[A] Six benchmark families are integrated. Their conditions differ substantively:

| Family | Environment and evaluation details from Appendix B, p. 26 |
|---|---|
| MiniWoB | Single HTML pages; JavaScript task and validation logic; independent tasks avoid collisions by design |
| WebArena | Six domains hosted in Docker; resets between agent evaluations; rules based on HTML, URLs, or messages; some semantic matching uses GPT-3.5 as a judge |
| VisualWebArena | Two retained WebArena domains plus one new domain; image-conditioned goals; resets; visual matching may use blip2-flan-t5-xl |
| WorkArena | ServiceNow Personal Developer Instance; database queries and injected frontend JavaScript for validation; collision prevention supports parallel evaluation |
| AssistantBench | 214 tasks, 33 development and 181 hidden-answer test tasks; more than 525 pages across 258 sites; predictions submitted through an evaluation API |
| WebLINX | Static supervised action prediction; each recorded human action becomes a one-step task; partial-matching scalar rewards use the original metrics |

Metadata lists tasks and attributes, default splits, and optional dependency graphs. Suggested actions, seed counts, and step limits are recommendations, rather than immutable requirements. Backend preparation resets state where necessary (pp. 9–10).

## 7.4 AgentLab experiment infrastructure

[A] A Study stores an experiment on disk and organizes agents, tasks, reproducibility information, and parallel execution. `Study.run` relaunches failed tasks up to three times; users can also reload a study and find incomplete runs (pp. 10–11). These infrastructure relaunches are different from GenericAgent’s response-parsing attempts.

Ray or joblib can run multiple processes. The paper claims up to 20 tasks in parallel on a laptop and 50–100 on a larger server when conditions permit. API rate limits often dominate. Ray supports dependency graphs; joblib does not. Shared-state dependencies constrain WebArena/VisualWebArena to 2–4 parallel tasks in §5.2. Agents are evaluated sequentially with resets between evaluations. The later statement that only one agent can run at a time concerns agent collisions; task parallelism and concurrent model evaluations should not be assumed identical.

AgentXRay is a Gradio interface for inspecting traces, observations, prompts, goals, actions, and timing. Reproducibility features include recorded versions and commit hashes, a journal, reproduced leaderboard score ranges, and action replay with visual prompt differences (pp. 11–13). Replay can diverge rapidly if the environment changes; it diagnoses differences rather than proving identical behavior.

## 7.5 GenericAgent and models

[A] The evaluation uses GenericAgent, with modular prompting and an added reasoning-history setting relative to the cited WorkArena++ configuration. Table 4 precisely distinguishes supported features from enabled ones. AXTree, focused-element information, previous-action errors, action history, reasoning history, visible/clickable tags, chain-of-thought prompting, and concrete/abstract examples are enabled. HTML, all past error logs, coordinates, filtering to visible elements only, long action descriptions, individual action examples, multiple actions per step, explicit planning, and self-criticism are disabled. Screenshots are disabled except on VisualWebArena. SoM remains listed as disabled (p. 29).

Parsing errors trigger re-prompting, with four attempts to produce a parsable answer; four consecutive parsing errors make the task a failure (p. 15). Dynamic prompting shrinks selected components to fit a token budget. The paper cites AXTree lengths exceeding 100,000 tokens and DOM lengths exceeding 1,000,000, while some fine-tuning contexts are around 8,000. Default shrinking can reduce history or truncate the bottom of a page. Figure 11’s 40,000-token limit is an illustrative example, not a verified universal experiment setting.

The six model backbones are GPT-4o, checkpoint 2024-08-06, and GPT-4o Mini, checkpoint 2024-07-18, through Azure OpenAI; o1 Mini, checkpoint 2024-09-12, and Claude 3.5 Sonnet, checkpoint 2024-10-22, through OpenRouter; and Llama 3.1 70B and 405B through OpenRouter. Exact Llama serving-provider versions are not specified. The study is a historical evaluation and does not establish current rankings.

## 7.6 Sampling, metrics, hardware, and controls

[A] MiniWoB uses 125 tasks × 5 seeds = 625 episodes. WorkArena L1 uses 33 × 10 = 330. WebArena uses 812 tasks and VisualWebArena 910, without task seeding. WorkArena L2/L3 use preset curricula of 235 episodes each from 341 listed templates. WebLINX uses 2,650 test examples from 31,586 listed tasks. AssistantBench uses 181 test tasks from 214 total. Step limits are 10 for MiniWoB, 30 for WebArena, VisualWebArena, WorkArena L1, and AssistantBench, 50 for WorkArena L2/L3, and 1 for WebLINX (Table 5).

The stated metric is task success rate with standard error σ/√N. WebLINX’s partial-matching reward is a qualification to interpreting every row as binary completion. No statistical significance test, confidence-interval procedure, or multiple-comparison correction is reported.

VisualWebArena evaluates only the three models with supported multimodal inputs in this setup. Other benchmarks omit images for fairness. Most non-Claude WorkArena L3 results come from previous work, and the caption marks grayed zero entries as skipped evaluations for budget reasons. They must not be counted as six fresh, complete L3 measurements.

Hardware includes Intel Xeon Gold 6126 CPUs at 2.60 GHz and RAM described as effectively unlimited on compute clusters. WebArena uses Azure virtual machines with 8 CPUs and 32 GB RAM (p. 30). Exact package versions, complete model parameters, and random-seed lists are not included in the paper. Temperature zero is discussed as a way to reduce stochasticity; a universal experimental temperature setting is not explicitly established.

# 8. Experiments / analyses

**X1 — Multi-model, multi-benchmark evaluation.** Purpose: demonstrate experiment management and assess models. The main varying condition is the backbone model within GenericAgent; benchmark and visual-input availability also vary. Data and episode counts are those above. Table 2 reports means with standard errors, plus Claude costs and average steps. Caveats include imported/skipped L3 results, VisualWebArena model eligibility, differing validators, and no formal significance testing. This experiment measures capability, not malicious robustness.

**X2 — Historical GPT-4o comparison.** The authors compare current results with previously reported scores from a very similar agent: WebArena 23.5% versus 31.4%, WorkArena L2 3.8% versus 8.5% (p. 16). They suggest improved checkpoint training, but also raise possible benchmark content exposure. The comparison is not a controlled isolation of training improvements; no contamination test is conducted.

**X3 — Cost and token accounting.** Table 6 aggregates model costs and tokens over benchmarks excluding VisualWebArena. It shows substantial differences in expense and output-token volume. Llama models are accessed through OpenRouter providers; the paper warns that prices may have changed. This is historical accounting rather than a current pricing comparison or controlled cost-efficiency frontier.

**X4 — Runtime and hardware accounting.** Table 7 reports Claude timing, environment timing, and steps by benchmark. Cumulative durations do not account for parallelization; they are not user-visible wall-clock completion times under the parallel runner. API load and backend constraints affect timing. There is no controlled framework-overhead baseline or scaling curve.

**X5 — Paired qualitative task trace.** Appendix H compares Claude and GPT-4o on the same WorkArena L2 laptop-ordering task, seed 99. The goal is six standard laptops with specified software and two selected Adobe options. Claude recovers from an intercepted checkbox click by clicking its label. GPT-4o fails to change quantity, subsequently asserts that it has set six, and completes a wrong order (pp. 31–33). This is a mechanism illustration, not a statistically representative error-rate study, adversarial transaction attack, or evidence that all model differences have the same cause.

# 9. Results

[A] Table 2’s results are reproduced below. Values are reported means ± standard error in percentage units under the stated benchmark metric. The dash denotes an unreported/unrun multimodal condition, not zero performance. WorkArena L3 zeros retain their skipped/imported-results caveat.

| Benchmark; episodes | Claude 3.5 Sonnet | GPT-4o | GPT-4o Mini | Llama 3.1 70B | Llama 3.1 405B | o1 Mini |
|---|---:|---:|---:|---:|---:|---:|
| MiniWoB; 625 | 69.8 ± 1.8 | 63.8 ± 1.9 | 56.6 ± 2.0 | 57.6 ± 2.0 | 64.6 ± 1.9 | 67.8 ± 1.9 |
| WorkArena L1; 330 | 56.4 ± 2.7 | 45.5 ± 2.7 | 27.0 ± 2.4 | 27.9 ± 2.5 | 43.3 ± 2.7 | 56.7 ± 2.7 |
| WorkArena L2; 235 | 39.1 ± 3.2 | 8.5 ± 1.8 | 1.3 ± 0.7 | 2.1 ± 0.9 | 7.2 ± 1.7 | 14.9 ± 2.3 |
| WorkArena L3; 235 listed | 0.4 ± 0.4 | 0.0 ± 0.0* | 0.0 ± 0.0* | 0.0 ± 0.0* | 0.0 ± 0.0* | 0.0 ± 0.0* |
| WebLINX; 2,650 | 13.7 ± 0.6 | 12.5 ± 0.6 | 11.6 ± 0.6 | 8.9 ± 0.5 | 7.9 ± 0.5 | 12.5 ± 0.6 |
| WebArena; 812 | 36.2 ± 1.7 | 31.4 ± 1.6 | 17.4 ± 1.3 | 18.4 ± 1.4 | 24.0 ± 1.5 | 28.6 ± 1.6 |
| VisualWebArena; 910 | 21.0 ± 1.3 | 26.7 ± 1.5 | 16.9 ± 1.2 | — | — | — |
| AssistantBench; 181 | 5.2 ± 1.5 | 4.8 ± 2.4 | 2.1 ± 1.0 | 2.8 ± 1.1 | 3.9 ± 1.0 | 6.9 ± 2.2 |

*The prose reports reuse of non-Claude L3 results from prior work; the caption additionally marks grayed zero entries as skipped evaluations for budget reasons. The supplied material does not provide a reliable per-cell distinction between a measured historical zero and an evaluation skipped in this experiment. Treat these entries as qualified reported placeholders, not verified fresh failures.

[A] Claude’s strongest highlighted advantage is WorkArena L2: 39.1% versus GPT-4o’s 8.5% and o1 Mini’s 14.9%. However, the p. 3 contribution statement calls GPT-4o second place at 8.5%, whereas Table 2 places o1 Mini above it. These statements cannot both describe the final table’s numerical ordering. No chronology in the supplied paper resolves the discrepancy.

[C] Claude’s L2 difference from GPT-4o is 39.1 − 8.5 = **30.6 percentage points**. Its difference from o1 Mini is 39.1 − 14.9 = **24.2 percentage points**. These are differences between reported means, not significance tests or relative percentages.

[A] GPT-4o leads VisualWebArena at 26.7 ± 1.5%, versus Claude at 21.0 ± 1.3%. [C] The reported-mean gap is 26.7 − 21.0 = **5.7 percentage points**. Only three model conditions were evaluated there, so the row does not rank all six models.

[A] o1 Mini’s 56.7 ± 2.7% on WorkArena L1 is slightly above Claude’s 56.4 ± 2.7%. [C] The gap is 0.3 percentage points. The paper provides no test supporting a meaningful difference. o1 Mini also leads AssistantBench at 6.9 ± 2.2%, but the authors compare this with a reported external leaderboard high of 27% and acknowledge the general-purpose agent is not optimized for retrieval. That leaderboard value is only known through this paper, not independently checked.

[A] Llama 405B exceeds GPT-4o Mini on MiniWoB, WorkArena L1/L2, WebArena, and AssistantBench, but trails it on WebLINX. Llama 70B and GPT-4o Mini have relatively close means on several rows. The authors describe stronger open-weight results as encouraging; this does not establish a general open-versus-closed model law.

The reported errors are navigation, form handling, task understanding, repeated stuck behavior, information extraction, and external technical failures. No category frequencies or adversarial subsets are measured. Poor task completion must not be silently reinterpreted as vulnerability prevalence.

# 10. Figure-by-figure interpretation

All 13 figures were visually inspected in supplied page images. They are screenshots, diagrams, or code/prompt illustrations rather than statistical plots. There are no numerical axes, error bars, or plotted confidence intervals to estimate. Interface colors mainly organize components; they do not encode model-performance measurements.

## Figure 1 — Ecosystem overview, p. 2

[B] BrowserGym and benchmark names sit beneath the agent, while dynamic prompting and a unified model API sit within the agent area. Arrows connect observation/action handling to BrowserGym, and surrounding AgentLab components cover parallel experiments, reproducibility, leaderboard, XRay, and trace data. Blue components are identified as AgentLab. The diagram supports the modular architecture, not measured speedups. Mind2Web-live is shown visually, but p. 10 lists it as considered for integration, so its availability is uncertain from the diagram alone.

## Figure 2 — Rendered browser/chat environment, p. 5

[B] The chat appears on the left and a browser-based drawing interface on the right. Messages and an action are visible in the chat, and a stick figure is visible in the browser canvas. This shows the user-facing environment and the relationship between requested task and browser action. It is an illustrative interaction, not a benchmark result or security test.

## Figure 3 — Interaction loop and Python interface, p. 5

[B] The left panel contains Agent and Environment boxes. An action arrow goes from agent to environment; an observation/reward arrow returns. The right panel creates a gymnasium environment, resets it, steps through actions, and stops on termination or truncation. The figure makes feedback explicit. It does not show a complete state model, permission system, or attack filter.

## Figure 4 — Four representations of one page, p. 6

[B] Panel a is a raw webpage screenshot; b adds identifier marks and boxes; c is an HTML fragment; d is an AXTree fragment. The shared example includes upvote/downvote elements and displayed score 17705. HTML and AXTree show bids 167, 169, and 179. These numbers identify example elements/content and are not performance measurements. The figure explains how the same interface is exposed through different modalities and levels of structure.

## Figure 5 — Hidden button and error feedback, p. 7

[B] A Google search screenshot has an autocomplete overlay, beside a Playwright timeout log. The caption explains that the search button is hidden behind the menu. The log reports a 500 ms timeout and intercepted pointer events. This supports the mechanism of returning execution errors to the next observation. It does not demonstrate that the agent ultimately corrects the action.

## Figure 6 — Raw code versus high-level primitives, p. 7

[B] Panel a shows Playwright/JavaScript approaches to locating and clicking an upvote button; panel b shows `click`, `press`, and coordinate-click alternatives, plus chat messaging. The high-level bid example uses 169 and the coordinate example uses x=121, y=197. These are example target coordinates, not measured accuracy. The figure supports the expressiveness/control tradeoff. Code extraction contains wrapping/quotation artifacts, so executable correctness is not certified.

## Figure 7 — Custom task definition, p. 8

[B] Code defines setup, validation, registration, and environment creation. The screenshot shows a browser/chat rendering of the task. Setup navigates to Google and asks a birth-year question; validation examines the first assistant answer for 1879. This is pedagogical task-extension pseudocode. Its permissive string-containment check should not be interpreted as a robust answer-verification method for arbitrary tasks.

## Figure 8 — Two tasks through one API, p. 9

[B] The left screenshot presents a MiniWoB checkbox task, the right a WebArena forum task. Each has a chat panel and a browser panel, with environment-creation strings beneath. The comparison demonstrates common interface access despite different task content. It does not imply identical underlying validators or backend behavior.

## Figure 9 — AgentXRay trace inspection, p. 12

[B] Colored outlines divide task selection, seed selection, episode information, action/step information, profiling, and detailed observation tabs. The profiling region is a timeline with colored segments, but it is not a model-comparison plot. The lower tabs include screenshots, DOM/AXTree, messages, errors, and logs. Small trace-row values are not reliably readable; no result is inferred from them. The figure supports inspection capability rather than validation of a particular diagnosis.

## Figure 10 — Action-set description, p. 25

[B] A generated documentation block presents function signatures, descriptions, examples, and a single-action restriction. It states 20 action types for this example configuration. Click, fill, scroll, messaging, and infeasibility reporting are expanded; an ellipsis compresses other entries. The 20 count is not the number of all primitives in Table 3, which spans additional categories.

## Figure 11 — Dynamic prompting example, p. 27

[B] The upper code example assembles goal instructions, observations, action descriptions, and an expected-response example. It fits the prompt to 40,000 tokens, queries a model, parses an action, and returns logged information. Flags appear in an adjacent column. The concrete GenericAgent prompt begins below and continues through pp. 28–29. The figure is expressly simplified. It is not evidence that every experiment uses exactly 40,000 tokens, and small code defects or extraction artifacts should not be repaired silently.

## Figure 12 — Successful laptop-ordering trajectory, p. 32

[B] Six panels show opening the All menu, catalog, hardware section, laptop product, required fields, and completed order. Caption stages compress multiple actual actions, especially panel e. The caption identifies Claude, task name, and seed 99. Small final-order text is not used to independently verify every requirement; task success and checkbox recovery are author-reported in p. 31 prose.

## Figure 13 — Failed quantity setting and wrong order, p. 33

[B] Two panels show an unsuccessful attempt to set quantity to six and subsequent completion of a wrong order. The caption identifies GPT-4o on the same task and seed. The mechanism is established by p. 31’s AXTree excerpt and prose: quantity remains one and the agent does not correct it. The visual is not an attack demonstration; no malicious actor is present in the reported trace.

# 11. Table-by-table interpretation

## Table 1 — Integrated benchmark overview, p. 9

[A/B] Rows identify eight configurations from six families; columns cover templates, seed diversity, maximum steps, multitab support, backend, and reference. Counts are MiniWoB 125, WebArena 812, VisualWebArena 910, WorkArena L1 33, WorkArena L2/L3 341 each, WebLINX 31,586, and AssistantBench 214. MiniWoB has medium seed diversity; WorkArena has high diversity; other rows show none. Multitab support is absent for MiniWoB, WorkArena L1, and WebLINX, and present for the other configurations. Template counts must not be read as experiment counts. Suggested settings do not establish universal implementation constraints.

## Table 2 — Main performance results, p. 16

[A/B] The full numerical matrix is represented in §9. Six model columns report means and standard errors. Additional columns give Claude expense and average steps. Claude’s per-row costs/steps are MiniWoB $23.11/3.7; L1 $100.03/9.0; L2 $299.44/33.8; L3 $191.50/25.0; WebLINX $104.62/1.0; WebArena $138.76/6.8; VisualWebArena $134.69/4.7; AssistantBench $37.33/7.5. Lowest numerical means vary by row; grayed L3 zeros cannot be treated as ordinary measured worst outcomes. GPT-4o and o1 Mini tie at 12.5 on WebLINX. Standard errors are not significance markers.

## Table 3 — High-level primitives, p. 24

[A/B] There are five categories: bid-based operations; coordinate mouse/keyboard operations; tabs; navigation; and miscellaneous operations. Bid actions include fill, click, double-click, hover, key pressing, focus, clear, option selection, drag/drop, and file upload. Coordinate actions include movement, press/release, clicking, dragging, upload, and keyboard operations. Tabs can be created, closed, or focused; navigation can go back, forward, or to a URL. Miscellaneous operations message the user, report infeasibility, scroll, or wait.

[C] Counting listed rows gives 10 bid + 12 coordinate + 3 tab + 3 navigation + 4 miscellaneous = **32 primitives**. This is a derived inventory count. Figure 10’s 20 types refer to an example action-set description, not necessarily the complete table. Permissions, filesystem scope for uploads, and URL-policy semantics are not specified here.

## Table 4 — Actual prompting configuration, p. 29

[A/B] Checkmarks and crosses identify enabled and disabled settings. This table is necessary to prevent confusing GenericAgent’s capabilities with experimental use. In particular, self-criticism, planning, and SoM are supported but disabled; screenshots are enabled only for VisualWebArena. Both prior actions and prior reasoning are included, while all past error logs are disabled and previous-action error feedback is enabled. No ablation proves which enabled component causes improved performance.

## Table 5 — Experiment counts and step limits, p. 29

[A/B] This table connects dataset/template counts to actual runs. MiniWoB and WorkArena L1 multiply tasks by seeds; WorkArena L2/L3 use curricula; WebLINX uses its test split; AssistantBench uses 181 hidden-answer test tasks. Slash notation for seed counts indicates no applicable task-seeding setting, not missing episodes. The distinction resolves apparent differences between 214 AssistantBench tasks and 181 evaluated tasks, and between 341 WorkArena templates and 235 curriculum episodes.

## Table 6 — Historical costs and API usage, p. 30

[A/B] VisualWebArena is excluded from all aggregates. Input/output token columns use millions of tokens; rate columns use dollars per million tokens.

| Model | Total USD | Input M tokens | Output M tokens | Input USD/M | Output USD/M |
|---|---:|---:|---:|---:|---:|
| Claude | 894.80 | 276.20 | 4.41 | 3.00 | 15.00 |
| GPT-4o | 720.72 | 277.25 | 2.76 | 2.50 | 10.00 |
| GPT-4o Mini | 75.73 | 479.72 | 6.29 | 0.15 | 0.60 |
| Llama 3.1 405B | 849.63 | 359.89 | 8.13 | 2.30 | 2.30 |
| Llama 3.1 70B | 78.79 | 221.23 | 5.02 | 0.35 | 0.35 |
| o1 Mini | 971.12 | 171.25 | 38.11 | 3.00 | 12.00 |

GPT-4o Mini has the lowest aggregate reported expense, and o1 Mini the highest. Token costs are affected by completed episode lengths and model responses, not just rate cards. [C] Claude’s nonvisual Table 2 costs sum to 23.11 + 100.03 + 299.44 + 191.50 + 104.62 + 138.76 + 37.33 = **$894.79**, versus $894.80 in Table 6. The one-cent difference is disclosed; rounding is plausible but not established. Several totals do not exactly reconstruct from rounded token counts and listed rates, so these fields should not be silently forced into equality.

## Table 7 — Claude runtime, p. 31

[A/B] Columns report cumulative experiment hours, average step seconds, cumulative environment hours, average environment-step seconds, and cumulative steps.

| Benchmark | Experiment h | Step s | Environment h | Environment-step s | Steps |
|---|---:|---:|---:|---:|---:|
| AssistantBench | 4.0 | 9.1 | 2.0 | 4.5 | 1,590 |
| MiniWoB | 3.1 | 5.0 | 0.7 | 1.1 | 2,282 |
| WebArena | 18.6 | 12.2 | 11.6 | 7.6 | 5,493 |
| WebLINX | 4.5 | 6.1 | 0.1 | 0.2 | 2,649 |
| WorkArena | 8.2 | 9.9 | 4.4 | 5.3 | 2,985 |
| WorkArena L2 | 23.6 | 10.7 | 10.9 | 4.9 | 7,947 |
| WorkArena L3 | 16.1 | 9.8 | 7.4 | 4.5 | 5,884 |
| VisualWebArena | 16.9 | 14.1 | 10.5 | 8.8 | 4,319 |

The unqualified WorkArena row appears to correspond to L1 [D], but the label itself does not say L1. WebLINX has 2,649 runtime steps versus 2,650 listed evaluation episodes; the paper does not explain the one-step discrepancy. Cumulative hours represent summed execution without adjustment for parallelism. They do not prove deployment latency or framework scalability.

# 12. Diagram / architecture interpretation

[A/B] The core information path is: task/chat goal and browser state → observation construction → agent prompt → backbone model → parsed action → action mapping → Playwright/browser operation → updated page, reward, and error feedback. Figures 1 and 3 jointly represent the ecosystem and iterative loop. The environment/task validator controls the reported completion reward; the agent controls action selection.

AgentLab surrounds that loop with Study scheduling, model configuration, reproducibility metadata, persisted traces, cost/token tracking, and AgentXRay. Custom agents implement action logic; custom model adapters implement calls; custom tasks implement setup and validation. This modularity allows components to change without rewriting every benchmark interface.

[D] A security-relevant reading follows the same path. Externally supplied page content becomes model input; model output becomes an operation with consequences; resulting state can be reused by later steps or other agents. Action mapping restricts the operation vocabulary, backend resets separate evaluations, and error feedback exposes failures. These mechanisms address different problems: action expressiveness, experimental contamination, and operational correction. None is demonstrated here to eliminate prompt injection or unauthorized intent.

The screenshots also expose an observation-action verification requirement. An intended action is not equivalent to a successful state change. Appendix H shows that reasoning history can preserve the intended state even when actual browser state differs. The analyst implication is to distinguish plans, attempted actions, errors, and observed outcomes when evaluating consequential agents; the paper does not test a new verification defense.

# 13. Equations and mathematical concepts

**E1 — Standard error, p. 15, §6.1:** `SE = σ / √N`. The authors report the expression σ/√N as their error measure. N denotes the number of evaluation observations/episodes in context; σ is the standard-deviation quantity used for the evaluation metric. The supplied paper does not fully specify the estimator, independence assumptions, or the handling of heterogeneous task clusters and partial rewards.

The expression means that uncertainty in an estimated average scales with the variability of observations and decreases with the square root of sample count under appropriate sampling assumptions. This is explanatory interpretation of the supplied formula, not a proof that every benchmark satisfies those assumptions. The ± values in Table 2 are standard errors, not declared 95% confidence intervals. No significance threshold or statistical hypothesis test is stated.

**POMDP notation, Figure 3:** a_t is the action at step t, o_t the observation, and r_t the reward. The arrows communicate repeated interaction between agent and environment. The paper does not define transition or observation distributions, discount factors, a learned reward function, or an optimization objective. There is no formal policy-learning algorithm to reconstruct.

**Observation quantities:** bbox is a four-tuple `(left, top, width, height)`; visibility is a scalar between 0 and 1; task validation returns a scalar reward and a Boolean done flag. These are interface data types, not mathematical claims about model quality.

**Derived arithmetic:** episode multiplication, percentage-point subtraction, action-row counting, and Claude cost summation are explicitly marked [C] elsewhere. No unreported confidence intervals, failure-count estimates, or attack-success probabilities are calculated. The rounded 0.4% L3 result is not converted into a certified exact number of successful tasks.

# 14. Interpretation and discussion

[A] The paper’s most strongly supported result is that a common software interface can host a heterogeneous benchmark evaluation and reveal substantial model-dependent performance differences. It also shows that stronger performance on one type of task does not guarantee dominance elsewhere: Claude leads most rows, GPT-4o leads the visual benchmark, and o1 Mini leads the retrieval benchmark’s reported mean.

The objectives are supported at different evidentiary levels. O1 is supported by architecture, APIs, integrated runs, logs, and example inspection workflows, but not by a controlled measurement of researcher time saved against fragmented code. O2 is supported by the results matrix with specified model checkpoints and major evaluation settings. Historical and skipped conditions weaken the interpretation of the experiment as a fully uniform six-model-by-eight-row sweep.

For the user’s security question, four mechanisms are relevant [D]: broader observations expose the agent to external content; code/action interfaces transform language into effects; accumulated history can carry mistaken assumptions into later decisions; and shared backends create interaction and contamination risks. These mechanisms can increase exposure or consequences compared with text generation alone. Only arbitrary-code risk and possible prompt-injection harms are explicitly security claims by the authors. The laptop example demonstrates ordinary reliability failure, not attack susceptibility.

Cross-reference checks reveal the following unresolved points:

- **Text–table ranking:** p. 3 calls GPT-4o second on L2 at 8.5%; Table 2 gives o1 Mini 14.9%.
- **Diagram–integration status:** Figure 1 shows Mind2Web-live, while p. 10 lists it as considered for integration.
- **Methods–result provenance:** §6.1 reuses most non-Claude L3 results; Table 2 describes grayed zeros as skipped evaluations. Exact per-cell provenance is not fully resolved.
- **Metric interpretation:** §6.1 describes task success percentage, while Appendix B describes WebLINX partial-matching scalar rewards. The aggregation rule connecting that reward to the reported percentage is not fully supplied.
- **Counts:** WebLINX has 2,650 evaluated examples but 2,649 runtime steps.
- **Cost reconciliation:** Claude’s displayed nonvisual row costs sum to $894.79, while the aggregate is $894.80.
- **Interface names/units:** p. 10 mentions `close_tab()` as an illustrative primitive, whereas Table 3 lists `tab_close()`; Table 3 lists `noop(seconds)`, while the example prompt uses `noop(wait_ms: float = 1000)`. The paper does not reconcile naming/unit versions.

Some apparent differences are resolved by conditions: six benchmark families produce eight table rows; 214 AssistantBench tasks include 33 development plus 181 test; WorkArena’s 341 templates differ from its 235-episode curricula; supported self-criticism and SoM differ from enabled flags. These distinctions must remain explicit.

# 15. Contributions and novelty

[A] **System contribution:** an extended BrowserGym ecosystem with standardized observation/action interfaces and a unified collection of six benchmark families.

[A] **Implementation contribution:** AgentLab supplies Study orchestration, parallel execution, failure relaunch, model adapters, dynamic prompting, serialization structures, cost tracking, reproducibility logging, and AgentXRay.

[A] **Benchmark-integration contribution:** WebLINX, VisualWebArena, and AssistantBench are added to BrowserGym. This is integration of existing benchmarks, not creation of their original datasets or claims to own their task designs.

[A] **Experimental contribution:** six contemporary backbone models are compared across integrated benchmark configurations. The authors claim the first large-scale multi-benchmark web-agent experiment. Closed-document analysis can report this novelty claim but cannot establish historical priority independently.

[A] **Empirical contribution:** strong Claude performance on L2, continued difficulty on L3, visual superiority of GPT-4o within tested conditions, and qualitative examples of recovery versus mistaken continuation.

There is no new theorem, formal security model, adversarial dataset, attack algorithm, or experimentally validated prompt-injection defense. [D] The methodological relevance to security is reusable infrastructure for future controlled security evaluation and documented points where observations and actions meet. That relevance should be separated from demonstrated security efficacy.

# 16. Limitations

## Authors’ stated limitations

[A] Reproducibility remains difficult because localization, time zones, language defaults, geography, operating systems, browsers, dynamic advertisements, task randomness, and model-service changes can alter observations or behavior (pp. 11–13, 17).

[A] Open-web agents can cause consequences on a human’s behalf. URL protection and warning notices mitigate some risks, but the paper does not claim comprehensive protection (p. 17). Robot detection, CAPTCHA, IP limits, and behavior analysis obstruct AssistantBench’s open-web tasks.

[A] Shared databases produce agent collisions: concurrent agents can alter the same records or carts. WebArena/VisualWebArena therefore limit simultaneous agent evaluation. Synchronous browser loops can introduce delays for rapid action sequences.

[A] GenericAgent is not optimized for information retrieval; AssistantBench performance is low. Error analysis is qualitative rather than exhaustive. Budget constraints cause skipped/reused L3 conditions. API load contributes runtime variability, and Llama provider prices may change (pp. 15–16, 30).

[A] Safety evaluation, privacy-policy compliance, and resilience to malicious interaction are underexplored. Broader-impact discussion identifies possible sensitive-information leaks and unwanted transactions without measuring them (p. 18).

## Additional evidence-based analyst observations

[D] The study lacks a standalone-LLM comparison, attack set, attacker access assumptions, security endpoints, and defense evaluation. It cannot answer how much more vulnerable agents are, whether a particular model is more secure, or whether action mapping defeats malicious instructions.

[D] Some results are not generated under a single contemporaneous protocol, particularly L3. Model rankings depend on the shared agent configuration and benchmark choices; no ablation isolates reasoning history, prompt shrinking, screenshot use, or parsing retries.

[D] Heterogeneous validators mean the same-looking percentage can capture different constructs. A human-action match is different from successful completion of an extended browser task. Dependency and collision structures also complicate treating every episode as an independent replicate.

[D] The paper describes reproducibility metadata mechanisms but does not print the full execution configuration or supply the referenced traces in this input. The two-model case study cannot estimate error prevalence. Small screenshot text cannot independently verify every task condition. These are constraints on this analysis as well as on reproducibility from the paper alone.

# 17. Threats to validity

The following validity labels are analyst classifications [D], not the authors’ terminology.

**Internal validity:** shared-state changes, task dependencies, provider behavior, and imported historical results can complicate attributing differences solely to model backbones. Resets and scheduling address some operational interference, but no experiment quantifies their residual effect.

**Construct validity:** the principal construct is web-task capability. It is not malicious robustness, privacy preservation, authorization correctness, or attack resistance. WebLINX’s partial-action matching is also distinct from end-to-end task completion. Mislabeling success rates as security rates would be a substantial construct error.

**Statistical conclusion validity:** standard errors are reported, but no tests or clustered uncertainty treatment are specified. Small differences, such as 56.7 versus 56.4 on L1, should not become definitive superiority claims. The qualitative laptop comparison cannot support population-wide causal conclusions.

**External and ecological validity:** synthetic tasks, replicas, enterprise instances, static traces, and open-web retrieval provide broader coverage than a single environment, but do not represent every user workflow or adversarial setting. Robot blocking and dynamic websites affect deployment conditions. A research framework is not validated here as a consumer product.

**Reproducibility:** checkpoint dates improve traceability, but commercial services can change silently. Software, browser rendering, location, content, and task seeds can drift. Logging and replay assist diagnosis; they do not freeze the environment. Exact versions and experimental artifacts remain absent from the supplied input.

**Security generalizability:** the risk discussion supplies plausible stakes and the architecture supplies possible attack surfaces, but there is no measured transfer from conventional errors to adversarial exploits. A model that scores higher on tasks cannot be assumed safer, and a model that fails an order cannot be assumed more injection-susceptible.

# 18. Future work and open questions

## A. Explicit author proposals

[A] The authors propose stronger safety mechanisms and evaluation of privacy/safety-policy compliance and resilience to malicious interactions; lower-latency, real-time agents; smaller efficient models; improved computer-level visual understanding; inference-time scaling and self-reflection suited to web tasks; use of logged observations for fine-tuning; deeper error analysis and automated evaluation; and integration of further benchmarks (pp. 10, 16, 18).

The broader-impact section also calls for policies addressing rapid automation and displacement, and standardized approaches to agent interaction with advertisements. These are societal proposals, not tested technical components.

## B. Analyst open questions

[D] A direct security study would need to ask which externally controlled observations can redirect an agent, which available actions convert redirection into harm, and whether constrained action vocabularies reduce unauthorized outcomes. The present paper identifies components but does not answer these questions experimentally.

[D] Other unresolved questions include whether preserving reasoning history helps recovery or reinforces false assumptions; whether outcome verification can prevent the laptop-order failure; whether prompt shrinking removes useful warnings or state evidence; how file-upload primitives and URL protection are scoped; and how shared-state isolation behaves under malicious rather than accidental interference.

[D] A comparison with standalone LLMs would require an explicitly defined common outcome and matched exposure/authority conditions. The current capability results cannot supply such a comparison retrospectively. These are proposed analytical directions, not additional findings attributed to the authors.

# 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| Web agent | Assistant that observes and operates a browser to carry out a goal |
| LLM | Large language model used as the agent’s response/action-selection backbone |
| VLM | Vision-language model that can process images as well as language |
| UI | User interface: the browser surface ordinarily operated by a person |
| API | Application programming interface: a software interaction contract |
| BrowserGym | Common browser-task environment with observation and action interfaces |
| AgentLab | Tools for agent construction, experiments, logs, and analysis |
| GenericAgent | Shared modular agent implementation used in the evaluation |
| AgentXRay | Trace-inspection interface; distinct from Ray scheduling |
| Study | Persisted experiment organization and execution object |
| DOM | Document Object Model, a structured representation of the page |
| HTML | HyperText Markup Language; page markup shown in observations/examples |
| AXTree | Accessibility tree with roles, names, and structured page information |
| CDP | Chrome Developer Protocol, used here to extract page representations |
| bid | BrowserGym-generated identifier for a page element |
| bbox | Element bounding box: left, top, width, height |
| RGB | Red-green-blue image representation used for screenshots |
| SoM | Set-of-Marks: visual boxes/identifiers over screenshot elements |
| CoT | Chain-of-thought prompting/reasoning history used by GenericAgent |
| POMDP | Partially Observable Markov Decision Process, the interaction abstraction |
| a_t, o_t, r_t | Action, observation, and reward at step t |
| σ/√N | Reported standard-error expression; σ variability and N observation count |
| Episode | One task execution under its evaluation condition |
| Template | Task definition capable of generating multiple configurations |
| Seed | Task-variation setting where the benchmark supports it |
| Curriculum | Preset WorkArena L2/L3 selection used for evaluation |
| Action mapping | Translation from allowed action syntax to executable Python |
| HighLevelActionSet | Predefined browser primitives with descriptions and code translation |
| Trace | Logged observations, prompts, actions, and episode information |
| Backend reset | Restoration of server state between evaluations |
| PDI | Personal Developer Instance used for ServiceNow WorkArena tasks |
| VM | Virtual machine hosting some benchmark environments |
| CAPTCHA | Robot-detection challenge identified as an open-web obstacle |
| Prompt injection | Potential malicious influence on an agent through instructions; discussed as a risk, not tested here |
| Agent collision | Interference when multiple agents modify shared state |
| IID | Independent and identically distributed; the authors’ characterization of agent stochastic noise |
| TGI | Mentioned server/provider interface; expansion is not specified in the supplied paper |
| ReAct, RCI, CRM | Related-work terms whose full expansions or mechanisms are not fully defined here; not silently supplemented |

# 20. Key numerical results

All main model values are preserved in §9, cost values in §11/Table 6, and runtime values in §11/Table 7. This compact reference emphasizes conditions needed to interpret the headline numbers.

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Model backbones | 6 | models | Shared GenericAgent, historical checkpoints | Author-reported | p. 15, §6.1 |
| Integrated benchmark families | 6 | families | WorkArena has three levels, producing eight result rows | Author-reported | pp. 8–9 |
| MiniWoB evaluation | 625 | episodes | 125 templates × 5 seeds, max 10 steps | Author-reported | p. 29, T5 |
| WorkArena L1 evaluation | 330 | episodes | 33 templates × 10 seeds, max 30 steps | Author-reported | p. 29, T5 |
| WorkArena L2 evaluation | 235 | episodes | Curriculum from 341 templates, max 50 steps | Author-reported | p. 29, T5 |
| AssistantBench test | 181 | tasks | 214 total, 33 development, hidden test answers | Author-reported | p. 26, Appendix B |
| Claude L2 | 39.1 ± 3.2 | percent | GenericAgent, 235 episodes | Author-reported | p. 16, T2 |
| o1 Mini L2 | 14.9 ± 2.3 | percent | Same benchmark; contradicts p. 3 second-place wording | Author-reported | p. 16, T2 |
| GPT-4o L2 | 8.5 ± 1.8 | percent | GenericAgent, 235 episodes | Author-reported | p. 16, T2 |
| Claude–GPT-4o L2 gap | 30.6 | percentage points | 39.1 − 8.5; no significance claim | Analyst-derived | p. 16, T2 |
| GPT-4o VisualWebArena | 26.7 ± 1.5 | percent | Screenshots, 910 episodes, three tested models | Author-reported | pp. 15–16 |
| Claude VisualWebArena | 21.0 ± 1.3 | percent | Same visual benchmark | Author-reported | p. 16, T2 |
| Visual benchmark gap | 5.7 | percentage points | 26.7 − 21.0 | Analyst-derived | p. 16, T2 |
| Claude L3 | 0.4 ± 0.4 | percent | 235 listed episodes; other models qualified by reuse/skips | Author-reported | pp. 15–16 |
| o1 Mini AssistantBench | 6.9 ± 2.2 | percent | 181 test tasks, general-purpose agent | Author-reported | p. 16, T2 |
| Prior/current GPT-4o WebArena | 23.5 / 31.4 | percent | Historical comparison, not controlled retraining study | Author-reported | p. 16, §6.2 |
| Parsing attempts | 4 | attempts | Consecutive parsing failures cause task failure | Author-reported | p. 15, §6.1 |
| Failed-task relaunch limit | 3 | relaunches | Study infrastructure, distinct from parsing retry | Author-reported | p. 11, §5.1 |
| Complete action-table count | 32 | primitives | 10 + 12 + 3 + 3 + 4 listed rows | Analyst-derived | p. 24, T3 |
| Example action-set count | 20 | types | Particular generated description | Visually readable | p. 25, F10 |
| Claude aggregate cost | 894.80 | USD | Excludes VisualWebArena | Author-reported | p. 30, T6 |
| o1 Mini aggregate cost | 971.12 | USD | Excludes VisualWebArena; 38.11 M output tokens | Author-reported | p. 30, T6 |
| Claude L2 duration | 23.6 | cumulative hours | Not parallel wall-clock time | Author-reported | p. 31, T7 |
| Claude L2 steps | 7,947 | steps | Runtime register | Author-reported | p. 31, T7 |
| WebArena VM | 8 CPUs; 32 GB | resources | Azure-hosted benchmark environment | Author-reported | p. 30, Appendix G |
| Laptop case | 6 required; 1 ordered | laptops | GPT-4o failure, task seed 99 | Author-reported | pp. 31–33 |

No approximate visual estimates are used in this numerical ledger. Values seen in example interfaces are identified as illustrative content rather than study results.

# 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence strength |
|---|---|---|---|---|
| Fragmentation motivates a common interface | Incompatible implementations and diverging evaluation codes described | S1, S2 | pp. 1–4 | Author motivation; no independent literature audit |
| BrowserGym exposes an iterative browser environment | Observation/action loop, gymnasium API, Chromium/Playwright | F2–F3, ALG1 | p. 5 | HIGH for described architecture |
| Observations span structured and visual information | DOM, AXTree, screenshot, identifiers, tabs, goal/chat, errors | F4–F5 | pp. 6–7 | HIGH for supported fields; agent use varies |
| Raw code increases operational risk | Explicit arbitrary-untrusted-code warning | F6, SS3.2 | p. 7 | HIGH for warning; no exploit measurement |
| Action mapping constrains the action interface | Predefined actions converted to code; default primitive set | F6, T3 | pp. 8, 24 | HIGH for mechanism, UNKNOWN for security completeness |
| AgentLab supports large experiments and diagnosis | Study, retries, parallelism, trace UI, replay | F9, ALG4 | pp. 10–14 | Described and demonstrated; no controlled productivity benchmark |
| Claude has a large L2 mean advantage | 39.1 versus 14.9 and 8.5 | T2, X1 | p. 16 | HIGH for reported values; p. 3 ranking inconsistent |
| GPT-4o leads tested visual conditions | 26.7 versus 21.0 and 16.9 | T2, X1 | p. 16 | Three multimodal conditions; not six-model visual comparison |
| Complex tasks remain difficult | Claude L3 0.4 ± 0.4 | T2, X1 | pp. 15–16 | Other L3 zeros have reuse/skip caveats |
| Reasoning history can coexist with false state belief | GPT-4o says quantity six after failed action | F13, X5 | p. 31 | One qualitative trace; no causal ablation |
| Prompt injection could cause consequential harm | Authors discuss leaks and unwanted transactions | S8 | p. 18 | Prospective risk argument, not measured incidence |
| The ecosystem is relevant to security evaluation | Example of a compatible security benchmark; safety future work | S4, SS7.2 | pp. 9, 18 | Proposed applicability; security relevance is analyst inference |
| Comparative standalone vulnerability is not established | Evaluation compares model-backed web agents, without attack protocol | X1, S8 | pp. 14–18 | HIGH for study-scope observation; comparative magnitude UNKNOWN |

# 22. Very simple explanation — Explain Like I’m 15

Imagine six different AI models using the same browser controller to solve tasks. Before this project, researchers often had to rebuild that controller for each test collection. BrowserGym gives them a common way to read browser pages and perform actions. AgentLab helps run many tests and inspect what happened when something goes wrong.

The tests show that the models have different strengths. Claude performs especially well on one difficult enterprise-workflow level, while GPT-4o does better on the visual website tasks. But even the best results leave many tasks unfinished, and the hardest enterprise level is almost never completed. The reported numbers describe task completion under specific test conditions, not protection against hackers.

The security concern is that an agent can do more than write an answer. It can execute code, change browser state, update records, or complete an order. The authors warn that malicious instructions could therefore lead to private information being leaked or unwanted transactions. Restricting the available actions gives researchers more control, but this paper does not prove that those restrictions stop attacks.

A useful example is the laptop order: GPT-4o tries to choose six laptops, fails, then acts as if it succeeded and submits the wrong order. No attacker caused this example. It shows why an agent must pay attention to what actually changed, rather than relying on what it intended to do. To prove that web agents are more vulnerable than standalone chat models, a separate security experiment would still be needed.

# Completeness Audit

The inventory covers all supplied sections, substantive subsections, 13 figures, 7 tables, 8 appendices, 5 analyses, 7 implementation/prompt examples, the statistical expression, stated contributions, limitations, and future directions. Every supplied figure was visually inspected. Text-only pages are explicitly distinguished from visually inspected pages. Coverage below means representation of the supplied evidence, not independent validation of software or experiments.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| FRONT: identity and abstract | Yes, text + visual | Yes | Represented in compressed form | Primary authors, roles, venue; repeated headers omitted |
| S1: Introduction and use cases | Yes | Yes | Fully represented substantively | pp. 1–3; p. 3 text-only |
| SS2.1: Benchmark related work | Yes | Yes | Represented in compressed form | Categories and relevant counts retained; citation-by-citation prose compressed |
| SS2.2: Agent related work | Yes | Yes | Represented in compressed form | Interaction, reasoning, training, framework categories retained |
| S3 and SS3.1: BrowserGym/observations | Yes, text + visual | Yes | Fully represented substantively | Goals, tabs, representations, identifiers, screenshots, errors |
| SS3.2: Actions | Yes, text + visual | Yes | Fully represented substantively | Raw code risk, mappings, default primitives |
| SS3.3: Custom tasks | Yes, text + visual | Yes | Fully represented substantively | Setup/validation and example limitation |
| S4: Unification, metadata, parameters, resets | Yes, text + visual | Yes | Fully represented substantively | Distinct benchmarks and integration-status caveat |
| SS5.1: Launch/relaunch | Yes | Yes | Fully represented substantively | Three infrastructure relaunches distinguished from parsing attempts |
| SS5.2: Parallelism/dependencies | Yes | Yes | Fully represented substantively | Ray/joblib, limits, collisions, resets |
| SS5.3: AgentXRay | Yes, text + visual | Yes | Fully represented substantively | Small interface fields uncertain |
| SS5.4.1: Reproducibility factors | Yes | Yes | Fully represented substantively | p. 13 text-only |
| SS5.4.2: Reproducibility features | Yes, text-only | Yes | Fully represented substantively | Journal, versions, reproduced scores, replay |
| SS5.5: Agent/AgentArgs/dynamic prompts | Yes | Yes | Fully represented substantively | Serialization and shrinking; exact executable code not certified |
| SS5.6: Model adapters | Yes | Yes | Represented in compressed form | BaseModelArgs, AbstractChatModel, tracking and provider classes |
| S6/O1/O2 | Yes | Yes | Fully represented | Two explicit objectives; no invented formal RQs |
| SS6.1: Setup | Yes, text + visual | Yes | Fully represented substantively | Models, checkpoints, metrics, exception conditions |
| SS6.2: Results | Yes, text + visual | Yes | Fully represented substantively | Full model matrix and historical comparison |
| SS6.3: Errors | Yes, text + visual | Yes | Fully represented substantively | Six categories; no frequencies invented |
| S7: Discussion | Yes, text-only | Yes | Represented in compressed form | Synthesis of ecosystem contribution |
| SS7.1: All five limitation categories | Yes, text-only | Yes | Fully represented substantively | Reproducibility, risks, robot detection, collisions, synchrony |
| SS7.2: Future work | Yes, text-only | Yes | Fully represented substantively | Safety, latency, smaller models, vision, scaling, fine-tuning |
| S8: Broader Impact | Yes, text-only | Yes | Represented in compressed form | Security, displacement, advertising, policy response |
| REF: bibliography | Yes; p. 21 visual, others text | Yes | Inspected but compressed as secondary | References establish author citations; linked works not reviewed |
| F1 | Yes, visual | Yes | Fully represented | Ecosystem; Mind2Web-live status discrepancy |
| F2 | Yes, visual | Yes | Fully represented | Chat/browser demonstration |
| F3 | Yes, visual | Yes | Fully represented | Loop and environment API |
| F4a–d | Yes, visual | Yes | Fully represented | Screenshot, SoM, HTML, AXTree |
| F5 | Yes, visual | Yes | Fully represented | Hidden-button error feedback |
| F6a–b | Yes, visual | Yes | Fully represented | Raw code and primitives |
| F7 | Yes, visual | Yes | Fully represented | Task extension pseudocode |
| F8 | Yes, visual | Yes | Fully represented | Common API across two tasks |
| F9 | Yes, visual | Yes | Represented in compressed form | Main regions inspected; small values unreadable |
| F10 | Yes, visual | Yes | Fully represented | Example action documentation; configured count |
| F11 | Yes, visual | Yes | Fully represented substantively | Simplified code and prompt start; continuation read as text |
| F12a–f | Yes, visual | Yes | Fully represented substantively | Six compressed stages; small field values not independently verified |
| F13a–b | Yes, visual | Yes | Fully represented substantively | Failure stages; mechanism supported by prose |
| T1 | Yes, visual + text | Yes | Fully represented substantively | Counts, steps, seeds, tabs, backends |
| T2 | Yes, visual + text | Yes | Fully represented | Full results, SEs, Claude costs/steps, missing-value caveats |
| T3 | Yes, visual + text | Yes | Fully represented substantively | All action families; derived 32-row count |
| T4 | Yes, visual + text | Yes | Fully represented substantively | Enabled/disabled experimental options |
| T5 | Yes, visual + text | Yes | Fully represented | Task/run counts and step limits |
| T6 | Yes, visual + text | Yes | Fully represented | All costs, tokens, rates, exclusion |
| T7 | Yes, visual + text | Yes | Fully represented | All timings and steps; count discrepancy |
| E1 and POMDP notation | Yes | Yes | Fully represented | No other major equations identified |
| ALG1: environment loop | Yes, visual + text | Yes | Fully represented conceptually | Creation, reset, step, termination |
| ALG2: action examples | Yes, visual + text | Yes | Represented in compressed form | Equivalent intent, different interfaces |
| ALG3: task setup/validation | Yes, visual + text | Yes | Fully represented conceptually | Reward/done/message outputs |
| ALG4: Study launch/relaunch | Yes | Yes | Represented in compressed form | Persisted study, workers, incomplete runs |
| ALG5: Agent and AgentArgs | Yes; partly text-only | Yes | Represented in compressed form | get_action, AgentInfo, make_agent, importability |
| ALG6: dynamic prompting/model call | Yes, visual + text | Yes | Fully represented conceptually | Components, shrinking, parse, log |
| ALG7: concrete prompt/history | Yes; p. 28 text-only | Yes | Represented in compressed form | Goal, AXTree, history, action grammar, examples |
| X1: multi-model evaluation | Yes | Yes | Fully represented substantively | Principal experiment |
| X2: historical comparison | Yes | Yes | Fully represented | Alternative explanations preserved |
| X3: cost accounting | Yes | Yes | Fully represented | Historical and condition-limited |
| X4: runtime accounting | Yes | Yes | Fully represented | Parallelism interpretation preserved |
| X5: qualitative case | Yes, text + visual | Yes | Fully represented substantively | Same task/seed, two models, no attack |
| Formal hypotheses/theorems | Not present | Absence represented | Not applicable | No invented tests or proofs |
| Major contributions | Yes | Yes | Fully represented | Integration, tooling, empirical demonstration |
| Author limitations | Yes | Yes | Fully represented substantively | Kept separate from analyst concerns |
| A1: Appendix A | Yes, visual + text | Yes | Fully represented substantively | Actions and descriptions |
| A2: Appendix B | Yes, text-only | Yes | Fully represented substantively | Validators, datasets, hidden test answers |
| A3: Appendix C | Yes; partial visual | Yes | Represented in compressed form | Prompt example and continuation |
| A4: Appendix D | Yes, visual + text | Yes | Fully represented substantively | Flags and experiment settings |
| A5: Appendix E | Yes, visual + text | Yes | Fully represented | Sampling and step limits |
| A6: Appendix F | Yes, visual + text | Yes | Fully represented | Historical cost/token table |
| A7: Appendix G | Yes, visual + text | Yes | Fully represented | Hardware and runtime definitions |
| A8: Appendix H | Yes, visual + text | Yes | Fully represented substantively | Laptop trace comparison |
| Substantive footnotes | Yes | Yes | Represented in compressed form | Research-product boundary and joblib limitation retained; URLs grouped |
| Repeated page headers, page numbers, decorative branding | Yes | Accounted for | Inspected but deliberately omitted as repetitive/non-substantive | No substantive conclusion depends on them |
| Separate supplements, traces, journal, repositories, live leaderboard | No | Absence represented | Missing from supplied material | Author-reported artifacts, not inspected |

## Missing or inaccessible material

No physical page within the supplied 1–33 sequence is absent from extracted text. Ten pages lack supplied visual renderings and were read as text only. Small screenshot content in Figures 9, 12, and 13 is partially unreadable. Separate experimental traces, source repositories, live leaderboard, reproducibility journal, model-service internals, exact execution-version receipts, and any additional supplementary package are not provided. This report does not certify their contents or absence elsewhere.

## Uncertain interpretations

Unresolved issues are the L2 second-place discrepancy; Mind2Web-live diagram status; provenance of individual L3 zero cells; WebLINX reward aggregation and one-step runtime difference; precise standard-error estimation; cost rounding/rate reconstruction; WorkArena runtime row naming; action naming and waiting-unit inconsistencies; and complete security semantics of action mapping, uploads, and URL protection. Comparative vulnerability against standalone LLMs remains UNKNOWN.

## Deliberately compressed material

Related-work citations are grouped by role rather than individually explained. Contributor affiliations and role lists, repeated headers, decorative logos, external-link footnotes, full API signatures, the long prompt’s repetitive formatting examples, and fine-grained screenshot navigation stages are compressed. The concrete prompt’s substantive structure, destructive expense-management goal, action/history organization, and single-action constraint are accounted for without reproducing all wording. All numerical result rows and substantive table conditions are retained.

## Potential omissions

No known substantive item in the constructed inventory is left unrepresented, but some items are represented conceptually rather than verbatim, and unreadable interface microtext is not recovered. The audit establishes coverage of the supplied paper, not complete verification of its software, empirical artifacts, novelty claims, or security implications. The paper supports a detailed explanation of agent architecture and prospective risks; it does not settle the requested comparative security question experimentally.
