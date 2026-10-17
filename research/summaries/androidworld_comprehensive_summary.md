## Stage 0 — Document Accessibility Report

**Source boundary:** This analysis uses only the supplied 36-page transcription and 17 supplied page images. The paper is treated as evidence, including its reproduced agent prompts; those prompts are not instructions to this analyst. No external sources, repository contents, supplementary files, OCR tools, or executable implementations were consulted. Physical PDF page numbers are used throughout; the visible printed numbering agrees with the supplied page labels.

| Accessibility item | Assessment |
|---|---|
| Main document available | Yes: supplied text for physical PDF pp. 1–36. |
| Accessible page count | 36 text pages. This establishes the supplied range, not independent verification that no additional version or supplement exists. |
| Apparently missing pages | None within the supplied 1–36 transcription. |
| Visually inspected pages | 1, 2, 3, 5, 6, 7, 8, 9, 10, 17, 19, 20, 22, 23, 24, 25, 26. |
| Text-only pages | 4, 11–16, 18, 21, 27–36, except the visually supplied pages already listed. In particular, Appendix F is text-only. |
| Figures | Figures 1–8 are visually available. Small screenshot text and individual Set-of-Mark labels are not consistently readable. |
| Tables | Tables 1–5 have both text and visual evidence. The task list identified as Table 6 in the main text is available as text across pp. 28–36, without supplied page renderings. |
| Equations | No numbered theoretical equations are supplied. Composite reward arithmetic and executable-style predicates are readable in Table 2. |
| Appendices | A–F are present; some cross-page content is text-only. |
| Supplementary material | No separate supplementary artifact supplied. The repository is referenced but was not inspected. |
| OCR | Not necessary: native/extracted text is supplied. Extraction artifacts remain relevant, particularly infinity symbols in Table 1. |
| Other limitations | Some extraction joins words, alters punctuation, or substitutes symbols. Visual confirmation is used where available; unresolved conflicts are disclosed. The source hash is supplied metadata, not independently verified. |

**Evidence categories:** [A] AUTHOR-REPORTED means a statement explicitly made in the paper. [B] DIRECTLY OBSERVABLE means a feature directly visible in a supplied image. [C] ANALYST-DERIVED means a calculation from supplied values, with operands shown. [D] ANALYST INTERPRETATION means an inference rather than an author finding. [E] EXTERNAL INFORMATION is excluded. HIGH confidence denotes clearly supported evidence; MEDIUM denotes supported but qualified inference or imperfect reporting; LOW denotes substantial ambiguity; UNKNOWN denotes unavailable evidence.

**Inventory before synthesis:** This is primarily a benchmark and computer-systems paper with AI-agent experiments, not a security-comparison paper. Inventory identifiers are S1 Introduction; S2 Related Work with SS2.1 Interactive Evaluation Environments, SS2.2 Static Datasets for UI Automation, SS2.3 Interactive Agents; S3 AndroidWorld with SS3.1 Android for Autonomous Agents, SS3.2 Observation and Action Space, SS3.3 Reproducible and Parameterized Tasks, SS3.4 Durable Rewards from System State, SS3.5 Task Composability, SS3.6 Integrating MiniWoB++; S4 Computer-Control Benchmark with SS4.1.1 M3A, SS4.1.2 SeeAct, SS4.2 Experimental Results, SS4.3 Analysis; S5 Robustness Analysis; S6 Conclusion; REF References; APP-A Limitations; APP-B Ethical Considerations; APP-C Environment with C.1–C.3; APP-D Benchmark Details with D.1–D.5; APP-E Agent Details with E.1–E.6; APP-F Task List. Visual objects are F1–F8; F2 has three panels, F6 three panels, F7 two panels. Tables are T1–T5 and T6, the multi-page task list. Code objects are ALG1 action-space Listing 1, ALG2 SendSms example, ALG3 information-retrieval protobuf example, ALG4 observation-prompt Listing 2, and ALG5 SeeAct prompt. Arithmetic object EQ1 is composite reward averaging in T2. Experiments are X1 benchmark comparison, X2 prompting comparison, X3 observation-modality comparison, X4 three-seed evaluation, X5 repeated fixed-versus-varying parameter trials, X6 alternate device/OS evaluation, X7 qualitative error analysis, and X8 reported latency comparison. Human annotation and human performance form methodological records H1 and H2. No formal numbered research questions, hypotheses, theorems, or proofs appear.

## 1. Plain-language orientation

**AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents** asks how to evaluate AI systems that operate a phone to carry out instructions. A language model can describe how to create a calendar appointment; an autonomous agent must actually open the calendar, enter the right details, save the event, and leave the device in the intended state. Evaluating that outcome reliably is the paper's central problem.

[A] The authors introduce AndroidWorld, a functioning Android environment with a reported 116 programmatic tasks across 20 apps. Tasks include creating and deleting notes, scheduling appointments, sending messages, changing settings, managing media, and answering questions about stored information. Each task has parameter generation, initialization, success checking, and cleanup. This allows the same task type to generate many different concrete goals and starting states rather than one fixed test example. Sources: pp. 1–2, 5–7.

[A] The researchers build M3A, the Multimodal Autonomous Agent for Android; compare it with a simpler variant and an adapted web agent, SeeAct; and evaluate performance under changing task parameters. Their best reported AndroidWorld configuration completes 30.6% of tasks, compared with 80.0% for humans. The best configuration is M3A using GPT-4 Turbo and accessibility-tree input, rather than the screenshot-based variant. Sources: pp. 3, 8–9, T3.

[A] The central contribution is the environment and evaluation machinery, supported by initial agent results and a demonstration that benchmark scores depend on task instantiation. [D] For the requested research question, 'Why Are Web AI Agents More Vulnerable Than Standalone LLMs?', the paper supplies relevant system properties and an ethical warning about altered prompts or screen outputs. It does **not** measure comparative vulnerability, attack success, prompt-injection resistance, or standalone-model security. Its usefulness to that question is mechanistic and methodological, not direct empirical proof.

## 2. Document roadmap

The abstract and Introduction establish why agents should be evaluated by whether they achieve a goal in an interactive environment, rather than whether each action matches a recorded human demonstration. Section 2 positions the benchmark among interactive environments, static demonstration datasets, and existing agents. Table 1 organizes those comparisons. Sources: pp. 1–4.

Section 3 explains the system: Android as the execution platform; screenshots and accessibility trees as observations; UI actions and limited APIs; controlled app and OS state; parameterized task instances; state-based rewards; composite tasks; and a mobile adaptation of MiniWoB++. Figure 1 gives the architectural overview, Figure 2 characterizes task difficulty and categories, and Table 2 illustrates validators. Sources: pp. 2, 5–7.

Section 4 defines the agents and presents Table 3's performance comparisons, followed by qualitative analysis and latency. Section 5 separates ordinary benchmark performance from robustness under changed parameters, repeated runs, and another device/OS configuration. Figure 3 visualizes repeated-trial differences. Section 6 concludes with implications for future computer-use agents and online learning. Sources: pp. 7–10.

References occupy pp. 10–17 and are bibliographic evidence only; their cited works were not independently examined. Appendix A discusses scope limitations, B ethical risks, C environment interfaces, D app selection and task construction, E agent inputs and failures, and F the detailed task catalog and step limits. Appendices materially clarify the benchmark and also expose reporting inconsistencies that should not be hidden by a summary.

## 3. Background and context

A **user interface**, or UI, is the visible and interactive part of an application. An **autonomous agent** in this paper repeatedly receives a task and a representation of the current interface, chooses an action, executes it, and observes the consequences. Its underlying large language model, or LLM, is one component of that loop. [D] This distinction is useful for the security research question because the full agent includes observation and execution interfaces beyond text generation; it does not establish that any particular agent is more vulnerable.

An **accessibility tree** is a structured representation of UI elements originally developed for accessibility. AndroidWorld extracts element text, descriptions, bounding boxes, and state flags such as clickable, scrollable, and focused. A screenshot supplies pixels; the tree supplies structured descriptions. **Set-of-Mark**, or SoM, adds numbered bounding boxes to the screenshot so an agent can refer to particular elements. Sources: pp. 7–8, 17, 22–24.

The **Document Object Model**, or DOM, is the website-content representation discussed when contrasting desktop web agents with Android agents. MobileMiniWoB++ deliberately uses Android screenshots and accessibility trees, not the original MiniWoB++ DOM. The paper does not provide a full DOM specification. Sources: pp. 4, 7–8.

A **reward signal** indicates functional task correctness: for example, whether the requested message exists or a calendar event has the right attributes. A **task template** describes a type of task with replaceable parameters; a **task instance** fills those parameters with particular values. A controlled **random seed** determines parameter generation. Repeated runs with the same seed keep task parameters fixed, but the paper observes that agent outcomes can still vary. Sources: pp. 2, 6, 9–10.

An **emulator** supplies the Android device environment used for experiments. AndroidEnv mediates interaction, while the **Android Debug Bridge**, adb, supports device actions and inspection. The main text sometimes calls it Android Device Bridge; §3.4 uses Android Debug Bridge. This naming variation does not change the described role. **SQLite** databases and the filesystem provide persistent evidence for many validators. Sources: pp. 5–7, 17–18.

**Zero-shot** describes M3A's use without task-specific demonstrations in the presented setup. The paper describes ReAct-style reasoning/action prompting and Reflexion-style post-action reflection. These names identify influences; their original algorithms were not separately reviewed. **Success rate**, SR, is the percentage of task evaluations successful under a stated condition. **Information retrieval**, IR, means answering from existing state; **task completion**, TC, is Appendix F's label for tasks requiring an operational outcome. Sources: pp. 7–9, 21, 28.

## 4. Research problem and gap

[A] The existing problem is realistic, reproducible evaluation of agents controlling computing devices. Comparing every agent action against a human demonstration can be misleading because multiple action sequences may achieve the same goal, environments may behave non-deterministically, and agents may recover from mistakes. The authors therefore favor online evaluation of actual outcomes. Source: p. 1, §1.

[A] Their account of prior approaches identifies several shortcomings. Human judges scale poorly; LLM judges are not fully reliable; many interactive benchmarks concentrate on desktop environments; mobile benchmarks cover limited apps or simpler tasks; and fixed task specifications do not adequately represent variation in real use. Sources: pp. 2–4. These are the authors' descriptions of the literature, not an independently verified ranking of current benchmarks.

[A] AndroidWorld aims to combine real Android applications, broad task types, automatic ground-truth rewards, and variable task instances. Durable evaluation is the difficult part: randomizing a prompt is insufficient if the success checker fails when dates, filenames, amounts, or starting states change. Sources: pp. 2, 6–7.

The scope is mobile computer control in a carefully managed emulator with selected apps, local data, and no required login. Its web component is MobileMiniWoB++, a WebView implementation of synthetic web tasks. [D] Consequently, the benchmark is relevant to interactive-agent architecture but does not represent the full security conditions of browsing arbitrary public websites, using authenticated services, or confronting deliberate attackers.

## 5. Research questions / objectives / hypotheses

**Explicit formal research questions:** None are stated as numbered or formally worded research questions. **Explicit hypotheses:** None are presented as formal testable hypotheses. This analysis does not convert informal objectives into author-written hypotheses.

The author-stated objectives can be organized as follows:

| ID | Objective | Evidence |
|---|---|---|
| O1 | Build a realistic mobile-agent environment with reliable outcome rewards. | pp. 1–2, 5–7 |
| O2 | Make tasks reproducible while allowing parameterized variations. | pp. 2, 6–7 |
| O3 | Establish initial benchmark performance using M3A and baselines. | pp. 3, 7–9 |
| O4 | Examine text-only versus multimodal observation and advanced versus simple prompting. | pp. 3, 8–9, T3 |
| O5 | Demonstrate the importance of varying task parameters and conditions. | pp. 9–10, F3 |
| O6 | Support future development and online learning for computer-use agents. | pp. 6, 10 |

The user's security research question is distinct from O1–O6. [D] This paper can inform a discussion of observation surfaces, action consequences, and evaluation design. It cannot determine whether web agents are more vulnerable than standalone LLMs, how much more vulnerable they might be, or which defense would close such a gap.

## 6. Assumptions / threat model

**Experimental environment assumptions [A]:** The primary device is a Pixel 6 emulator running Android 13. Each task begins with the device timestamp reset to October 15, 2023, at 15:34 UTC. Open-source app versions are fixed, and OS-level versions follow the fixed Android image. Apps do not require login/authentication and can store data locally. Task-specific initialization, checking, and teardown define controlled state. Source: p. 6, §3.3.

**Evaluation assumptions [A]:** The benchmark has privileged access to filesystem contents, application databases, and system settings through adb. Where system-state inspection is impractical, it checks UI elements. State-based predicates are used as ground-truth reward mechanisms. Sources: pp. 6–7. [D] The evaluation harness and the acting agent must be distinguished: the harness's complete system-resource access is not evidence that every tested agent is exposed to all those resources as observations or tools.

**Observation assumptions [A]:** Screens and actions are asynchronous. The interface can wait for stabilization using heuristics, rather than assuming every action immediately yields a settled observation. Source: p. 17, C.1. This improves experimental handling of transitions, but no timing guarantees or formal stabilization proof are supplied.

**Security threat model:** The paper does not define assets, adversary budgets, trust boundaries, attacker knowledge, controlled websites, attack payloads, or defense assumptions for a security experiment. Appendix B states that malicious actors could build agents that bypass CAPTCHAs, spam, or alter prompts or screen outputs to pursue harmful objectives. Source: p. 17. This is an ethical risk statement, not a tested attack model.

[D] A security-oriented reading can treat prompts, screenshots, element descriptions, stored content, and action execution as candidate interfaces worth investigating. Their existence is documented; attacker control over each interface and comparative exploitability are not established. No quantitative security conclusion should be drawn from ordinary task failures.

## 7. Methodology

### Environment and task lifecycle

[A] AndroidWorld combines an Android emulator, apps, OS state, task evaluators, an agent interface, and generated task goals. A TaskEval class supplies methods for parameter generation, initialization, success evaluation, and teardown. The agent interacts with the running environment through observations and actions, while the evaluator checks the resulting state. Figure 1, p. 2, and §§3.2–3.5, pp. 5–7, jointly explain this workflow.

Each concrete task starts from a controlled state generated for that task. Parameters can change goals and initial contents; success criteria must remain valid for those changes. For example, a calendar task varies date, time, title, description, and duration. Composite tasks combine simpler outcomes and can return partial rewards. The stated rationale is broader realistic variation without losing reproducible evaluation. Sources: pp. 2, 6–7, T2.

### Observations, actions, and software

[A] The State object contains RGB screenshot pixels with resolution 2400 × 1080 × 3, a raw accessibility tree, and processed UI elements. Accessibility forwarding uses AndroidEnv and gRPC. UI elements include text, content description, bounding boxes, and state flags. get_state can optionally wait for UI stabilization. Source: p. 17, C.1. The pixel dimensions include three color channels; they are not three separate screenshots.

Actions are represented by a Python dataclass and executed through adb. Listing 1 includes click, scroll, input_text, navigate_home, navigate_back, keyboard_enter, open_app, long_press, status, wait, answer, and unknown. A click can use an element index or x/y coordinates; other action fields provide text, direction, completion status, or app name. Sources: p. 18, C.2. High-level APIs for messaging, web pages, and contacts are mentioned as support for future hybrid interaction research. The supplied experiment description does not establish that each baseline uses every such API.

[A] The environment is described as requiring 2 GB memory and 8 GB disk space, runnable on a laptop without specialized hardware. Sources: pp. 2, 5. These are environment requirements, not measurements of complete model-serving memory, hardware throughput, or inference cost. Exact emulator-host specifications, dependency versions, model API snapshots, and pricing are not supplied.

### App and task selection

[A] Selection criteria include use case, popularity, consistency, and reproducibility. The authors focus on productivity, communication, and multimedia; consider categories they commonly use; and require local storage and no login. Most selected apps exceed one million downloads, with exceptions for representative UI patterns. Sources: pp. 19–20, D.1. This qualification is narrower than Appendix A's shorthand description of apps with more than one million downloads.

Table 4 lists 20 apps and task counts, while the main text reports 116 tasks. The counts in Table 4 sum to 123, an unresolved discrepancy discussed below. No train/validation/test split is used for the presented zero-shot benchmark evaluation. The paper mentions potential supervised-learning dataset generation and online learning as capabilities, not experiments conducted here. Sources: pp. 6, 8, 20.

### Validation and task generation

[A] Side-effect tasks have Python classes with parameter generation, initialization, evaluation, and teardown. SendSms clears the SMS database during setup, checks the requested number and message against stored messages, then clears the database during cleanup. Sources: pp. 20–21, D.2. The example gives the telephony database path but is illustrative pseudocode, not an implementation independently executed by this analyst.

[A] Information-retrieval tasks use protobuf structures instead of separate classes. The structures define prompts, parameters, relevant state, exclusion conditions for distracting state, and expected answer logic. Supported transformations include count, sum, and identity. The calendar example returns event titles for a parameterized date, with string matching. Sources: pp. 21–22, D.3. The exclusion conditions prevent generated noise from changing the expected answer.

[A] LLMs can assist in writing task protobufs after app logic exists, but generated tasks require human review. Reported issues include missing or hallucinated fields, incompatible parameter generation, insufficient parameter use, and vague prompts. Greater structure complexity correlates with more generated-task issues. Source: p. 21. This is a limitation of benchmark-authoring assistance, not evidence of a measured attack.

### Agent design and baselines

[A] M3A is zero-shot and combines action generation with post-action reflection. Action generation receives instructions, available actions, operating guidelines, accessibility-derived UI descriptions, and, for the multimodal variant, screen pixels and SoM annotations. It outputs reasoning and a JSON action. Reflection examines the action and before/after states, producing a summary of intended action, outcome, failure explanations, and recommendations. That summary becomes history for later decisions. Sources: pp. 7–8, 22–24.

M3A-Simple omits guidelines and reflection mechanisms. This comparison changes a bundle of prompting features, so it does not isolate reflection from guidance. SeeAct uses the choice-based variant of an originally web-oriented agent, expanded for scrolling, long presses, home/back navigation, and app opening. Accessibility elements replace DOM candidates, and the original bespoke ranker is omitted. Most filtered screens contain fewer than 50 candidates. Source: p. 8.

### Human work and experimental settings

[A] Six programming-proficient volunteers annotated task difficulty, duration, and category and found more than 30 bugs that were resolved. Two software engineers supplied human performance, with one attempt per task per participant as described. Misinterpretation, minor entry errors, and unfamiliar UIs explain many human failures. Personal information was not required. Source: p. 22, D.4. The exact aggregation procedure for the reported human score is not fully specified.

[A] The main agent evaluation sets seed 30 and temperature 0. Base models are Gemini 1.5 Pro, GPT-4 Turbo, and Gemma 2 27B. AndroidWorld evaluation is described as covering 116 tasks; MobileMiniWoB++ evaluation covers 62 of the 92 implemented tasks. Maximum steps are generally about twice human-annotated requirements, with individual limits in Appendix F. Sources: pp. 7–8, 28–36.

## 8. Experiments / analyses

| ID | Purpose and setup | Results and caveats |
|---|---|---|
| X1 Benchmark comparison | M3A variants, M3A-Simple, SeeAct, and humans; AndroidWorld and 62-task MobileMiniWoB++ subset; agent seed 30, temperature 0. | T3, p. 8. Best AndroidWorld agent is 30.6%; human 80.0%. No confidence intervals accompany T3. |
| X2 Prompting comparison | Compare full M3A with M3A-Simple, holding model and accessibility input comparable. | GPT-4 Turbo AndroidWorld: 30.6 versus 19.8. Guidance and reflection are changed together. MobileMiniWoB++ does not show the same ordering. |
| X3 Observation comparison | Full M3A with accessibility-only versus SoM screen plus accessibility input. | GPT-4 Turbo: AndroidWorld 30.6 versus 25.4; MobileMiniWoB++ 59.7 versus 67.7. Gemini shows a different modality pattern. |
| X4 Three-seed evaluation | M3A, GPT-4 Turbo, accessibility input; change parameter-generating seeds. | 27.6%, 26.3%, 33.2%; reported mean 29.0%, p. 9. Seed identities and run-level uncertainty are not given. |
| X5 Repeated-trial robustness | Five selected tasks, same parameters versus different parameter combinations; 20 trials per task as stated. | F3, p. 10. Significant differences for AddExpense and EditNote; 95% Wilson intervals; p < 0.05. Exact test and p-values are absent. |
| X6 Alternate device/OS | Pixel 5/Android 12 compared with primary Pixel 6/Android 13. | 28.4%, p. 10. Device and OS change together; the specific seed and full evaluation details are not supplied. |
| X7 Qualitative failures | Inspect errors involving perception, reasoning, knowledge, grounding, and memory. | F6–F8, pp. 23–26, plus §4.3. Examples explain mechanisms but do not quantify category prevalence. |
| X8 Latency | Report completion time and comparison with humans. | M3A 3.9 minutes, text-only 2.5 minutes; models described as about three times slower than humans, p. 9. Aggregation and timing boundaries are unclear. |

The five tasks in X5 are MarkorEditNote, ExpenseAddSingle, SimpleCalendarDeleteEventsOnRelativeDay, FilesDeleteFile, and SportsTrackerActivitiesCountForWeek. They represent editing, adding, deleting, and counting with varied interactions. Sources: pp. 25–26, E.4. Selection is described as representative but constrained by computational cost; it is not a random sample with a reported sampling procedure.

[A] X5 distinguishes task-instance sensitivity from outcome variation when the instance is fixed. The authors observe non-determinism even with fixed parameters. Different parameters can require different interactions, such as horizontal scrolling or replacing text rather than appending it. [D] This design is useful for future security evaluations because controlled repeated conditions could separate incidental failures from adversarial effects, but no adversarial condition appears in these experiments.

## 9. Results

The complete principal result matrix is retained because modality and prompting conditions change the interpretation:

| Agent | Input | Base model | AndroidWorld SR (%) | MobileMiniWoB++ SR (%) |
|---|---|---|---:|---:|
| Human | Screen | N/A | 80.0 | 100.0 |
| SeeAct | SoM: screen + accessibility tree | GPT-4 Turbo | 15.5 | 66.1 |
| M3A-Simple | Accessibility tree | Gemma 2 | 3.4 | 35.5 |
| M3A-Simple | Accessibility tree | Gemini 1.5 Pro | 14.7 | 55.2 |
| M3A-Simple | Accessibility tree | GPT-4 Turbo | 19.8 | 67.7 |
| M3A | Accessibility tree | Gemma 2 | 9.5 | 45.6 |
| M3A | Accessibility tree | Gemini 1.5 Pro | 19.4 | 57.4 |
| M3A | SoM: screen + accessibility tree | Gemini 1.5 Pro | 22.8 | 40.3 |
| M3A | Accessibility tree | GPT-4 Turbo | 30.6 | 59.7 |
| M3A | SoM: screen + accessibility tree | GPT-4 Turbo | 25.4 | 67.7 |

All values above are [A], Table 3, p. 8. Gemma is identified in the experimental prose as Gemma 2 27B. The two columns represent different task suites; MobileMiniWoB++ results use 62 tasks, not all 92 implemented tasks. These percentages are task-completion performance, not security vulnerability rates.

[C] The best AndroidWorld agent remains **49.4 percentage points** below humans: 80.0 − 30.6 = 49.4. Full M3A exceeds M3A-Simple with GPT-4 Turbo and accessibility input by **10.8 percentage points**: 30.6 − 19.8 = 10.8. Against the same-model SoM SeeAct baseline, multimodal M3A improves by **9.9 percentage points**: 25.4 − 15.5 = 9.9. These are absolute rate differences, not relative percentage improvements.

[C] GPT-4 Turbo accessibility-only M3A exceeds its SoM variant on AndroidWorld by **5.2 percentage points**: 30.6 − 25.4 = 5.2. On MobileMiniWoB++, SoM exceeds accessibility-only by **8.0 percentage points**: 67.7 − 59.7 = 8.0. Gemini SoM improves AndroidWorld by **3.4 points**: 22.8 − 19.4; but decreases MobileMiniWoB++ by **17.1 points**: 57.4 − 40.3. Thus screenshots are not consistently beneficial across models and suites.

[A] The authors suggest SoM is especially useful where MobileMiniWoB++ accessibility trees are incomplete, and interpret the AndroidWorld full-versus-simple improvement as evidence that guidance and advanced prompting help complex mobile tasks. Sources: pp. 8–9. The incomplete-tree explanation is an author interpretation, not a separately controlled accessibility-quality experiment.

[A] Multi-seed scores of 27.6%, 26.3%, and 33.2% yield the reported mean 29.0%. [C] Using the printed values, (27.6 + 26.3 + 33.2)/3 = 29.033…%, compatible with rounding to 29.0%. The printed-score range is **6.9 percentage points**, 33.2 − 26.3. Sources: p. 9. These seeds are not identified as including seed 30, so they should not be treated as a decomposition of T3's 30.6%.

[A] The alternate Pixel 5/Android 12 score is 28.4%. This supports capability retention in that tested configuration according to the authors; it does not establish general invariance across devices or OS versions. Source: p. 10. Qualitative results identify perception, reasoning, UI knowledge, grounding, and memory problems, while latency remains material. No supplied result measures malicious-input susceptibility or compares the agent against a standalone LLM.

## 10. Figure-by-figure interpretation

### Figure 1 — Benchmark architecture and example goals

[B] Figure 1, p. 2, is a system diagram, not a statistical plot. It contains an Android emulator with apps and OS state; a TaskEval block; an agent; a collection of task instances; and example mobile screens. Labeled connections distinguish observations/actions from evaluation and reward. The task collection is labeled 116 Android and 92 MiniWoB++ tasks. Example goals show calendar creation, adding a map marker, retrieving incomplete tasks, and entering a date.

The diagram explains why AndroidWorld is more than a prompt list: it couples instructions to executable state and evaluators. The placeholder-filled calendar goal visibly illustrates parameterization. There are no numerical axes, uncertainty bars, or statistical comparisons. Small app icons and screen contents communicate example diversity; not every icon or tiny UI label is necessary to the mechanism and some are unreadable at the supplied scale.

### Figure 2 — Human characterization of tasks

[B] Figure 2, p. 5, has three panels. Panel (a) is a vertical bar chart of easy, medium, and hard tasks; the y-axis counts tasks. Easy is the largest group, then medium, then hard. Panel (b) is a histogram of estimated action steps, with number of steps on the x-axis and task count on the y-axis. Most tasks fall in the lower-step bins, with a thinner tail extending beyond 30 steps. Panel (c) is a horizontal bar chart of category-tag counts.

The visible category labels are data entry, screen reading, search, information retrieval, data editing, complex UI, repetition, multi-app, transcription, required setup, mathematical counting, verification, and memorization. Data entry is the largest category, followed by screen reading and search. These are annotation categories, not measured error types. Multiple relevant tags can apply to one task, so bar totals should not be assumed to equal the number of unique tasks. Source: caption and D.4, pp. 5, 22.

The axes appear linear. Colors distinguish plotted bars but do not encode a reported experimental condition. Exact per-bar totals and histogram bin counts are not labeled sufficiently to recover confidently; this analysis retains ordering and shape instead of inventing exact values. Difficulty is a human rating, and step count is an annotation estimate, not the model's achieved runtime or actual action count.

### Figure 3 — Repeated-run and parameter variability

[B] Figure 3, p. 10, compares AddExpense, DeleteFile, EditNote, DeleteEvent, and CountActivities. The x-axis lists task nicknames; the y-axis is success rate (%) from 0 to 100 on a linear scale. Gray bars distinguish same seed from different seeds using solid versus hatched styling; blue and orange error bars denote the respective groups. The caption specifies 95% Wilson binomial proportion confidence intervals. Asterisks mark differences with p < 0.05.

[B, approximate visual estimates] Same-seed success is near 0% for AddExpense and EditNote, near 10% for DeleteFile and DeleteEvent, and near 25% for CountActivities. Different-seed success is approximately 45%, 30%, 30%, 20%, and 25%, respectively. These are visual estimates, not exact author-tabulated rates, and should not be used as exact trial counts. AddExpense and EditNote have significance annotations. The error intervals are broad, which matters for interpretation.

[A] The authors state that outcomes vary even with constant seed and that parameter variation significantly affects add-expense and edit-note performance. [D] The plot shows differences in observed success proportions and uncertainty; it does not directly display a variance statistic. The caption's assertion of higher variance under different seeds should be preserved as an author statement, not converted into a calculated variance. The statistical test and exact p-values are not supplied.

### Figure 4 — Native mobile rendering of web controls

[B] Figure 4, p. 19, shows a mobile date-picker dialog inside a web-task screen. It illustrates that an HTML5 input can render as a native Android widget. There are no axes, units, or statistical values. The selected date shown in the dialog is illustrative UI state, not a benchmark result. The figure supports the claim that mobile rendering changes interaction requirements relative to desktop web use. Exact small background task text is not required for that conclusion and is not confidently transcribed.

### Figure 5 — Set-of-Mark action references

[B] Figure 5, p. 24, shows an Android audio-recorder settings screen with green boxes and numerical marks around UI elements. These marks are generated from accessibility elements and help reference action targets. The image shows controls, choices, and buttons, but many tiny indices are not readable. Source: E.2, pp. 23–24. The figure demonstrates representation and grounding support, not evidence that the model selects every mark correctly or that all visible elements are valid targets.

### Figure 6 — Three distinct failure mechanisms

[B] Figure 6, p. 24, has panels (a) perception, (b) reasoning, and (c) missing knowledge. Panel (a) highlights the calendar's All-day checkbox with a red square. Nearby text says the model fails to recognize that it is not checked. Panel (b) shows the note-creation dialog and its Name field; the caption explains that the agent plans to type note contents before entering the name. Panel (c) shows a Markor file list; the agent looks for a bulk delete option rather than deleting notes individually.

These images support concrete qualitative distinctions: missing a visible state, misunderstanding which field is being completed, and lacking application-specific interaction knowledge. They are not statistical samples with frequency labels. The screenshot layout and red highlighting are directly visible; the agent's mistaken intent comes from caption and prose, not pixels alone. The task text and the panels must be read together. Sources: pp. 23–25.

### Figure 7 — Grounding error while editing text

[B] Figure 7, p. 25, has two Markor screenshots: (a) initial click and (b) entered text plus saving. A broad text region is highlighted in the first image; the later image shows the keyboard and save target. [A] The accompanying explanation states that clicking the field places the cursor after existing text. The requested operation was to prepend text, but the agent appends it and saves. The small character strings are not independently legible enough to verify exact content visually; the mechanism is supported by prose and visible editing context.

The preceding reasoning trace on p. 25 follows the note-creation example, while Figure 7 concerns editing and cursor placement. They should not be conflated into one task failure. No numerical axis or failure rate appears.

### Figure 8 — Hidden categories change task difficulty

[B] Figure 8, p. 26, shows an expense-entry form with a horizontal category strip. [A] Its caption and E.5 state that categories such as Food require horizontal scrolling and can be invisible initially; visible categories such as Housing or Social are easier for the agent. This explains how changing one task parameter changes the required action sequence.

The screenshot supports the form layout and limited visible strip. The assertion of consistent failure for hidden categories is author-reported qualitative analysis, not directly proven by the screenshot alone. There are no axes, confidence intervals, or exact category-specific success rates. The image is connected to Figure 3's AddExpense difference but does not quantify the contribution of scrolling failures across the entire benchmark.

## 11. Table-by-table interpretation

### Table 1 — Comparison of datasets and environments

T1, p. 3, compares whether an entry is an interactive environment, app/site count, task-template count, average task instances, reward method, and platform. The first group has no interactive-environment checkmark; its entries include GAIA, Mind2Web, WebLINX, WebVoyager, PixelHelp, MetaGUI, MoTIF, AitW, AndroidControl, OmniAct, AndroidArena, and LlamaTouch. The second group includes interactive environments from MiniWoB++ through AndroidWorld.

The compact inventory below preserves the table's important counts and reward classifications. App/site counts are in the first numeric column; template counts are in the second.

| Entry | Apps/sites | Templates | Average instances | Reward as listed |
|---|---:|---:|---:|---|
| GAIA | n/a | 466 | 1 | Text match |
| Mind2Web | 137 | 2350 | 1 | None |
| WebLINX | 155 | 2337 | 1 | None |
| WebVoyager | 15 | 643 | 1 | LLM judge |
| PixelHelp | 4 | 187 | 1 | None |
| MetaGUI | 6 | 1125 | 1 | None |
| MoTIF | 125 | 4707 | 1 | None |
| AitW | 357+ | 30378 | 1 | None |
| AndroidControl | 833 | 15283 | 1 | None |
| OmniAct | 60+ | 9802 | 1 | None |
| AndroidArena | 13 | 221 | 1 | Action match/LLM |
| LlamaTouch | 57 | 496 | 1 | Screen match |
| MiniWoB++ | 1 | 114 | ∞ | HTML/JavaScript state |
| WebShop | 1 | 12k | 1 | Product attributes match |
| WebArena | 6 | 241 | 3.3 | URL/text match |
| VisualWebArena | 4 | 314 | 2.9 | URL/text/image match |
| WorkArena | 1 | 29 | 622.4 | Cloud state |
| Mobile-Env | 1 | 13 | 11.5 | Regular expression |
| B-MoCA | 4 | 6 | 1.9 | Regular expression |
| MMInA | 14 | 1050 | 1 | Text match |
| OSWorld | 9 | 369 | 1 | Device/cloud state |
| WindowsAgentArena | 11 | 154 | 1 | Device state |
| AgentStudio | 9 | 205 | 1 | Device state |
| AndroidWorld | 20 | 116 | ∞ | Device state |

[A/B] The image shows infinity for MiniWoB++ and AndroidWorld where the extracted text renders 1. Visual evidence and parameterization prose agree on practically unlimited instances. This is an extraction discrepancy, not an author contradiction. Platforms span no fixed platform for GAIA, desktop web, synthetic web, desktop apps/web, and Android apps/web. All AndroidWorld entries are author-provided comparisons; no external benchmark record was checked. The table compares coverage and evaluation properties, not comparable success rates or security outcomes.

### Table 2 — Six example task validators

T2, p. 6, connects natural-language goals to validation logic. Calendar creation checks event existence; SMS checks number and content in the messaging database; drawing checks file existence; timer creation checks displayed time in the UI hierarchy. Two composite rows average note creation plus SMS, and Wi-Fi enabled plus app launched. Each row has parameterized placeholders. There are no measured success rates, error bars, or significance tests.

The important distinction is that the checker tests an outcome rather than replaying a fixed action sequence. The timer row also shows that state-based evaluation can include UI inspection. Composite predicates illustrate partial credit, not universal binary evaluation. The displayed pseudocode should not be treated as a complete specification of every edge case or forbidden collateral change.

### Table 3 — Agent success rates

T3 is reproduced in §9. It compares agent, input, base model, and success percentages on two suites. Human is highest on both. The lowest listed agent scores are M3A-Simple/Gemma 2: 3.4% and 35.5%. GPT-4 Turbo M3A/accessibility is best on AndroidWorld at 30.6%. Two configurations tie at 67.7% on MobileMiniWoB++: GPT-4 Turbo M3A-Simple/accessibility and GPT-4 Turbo M3A/SoM.

The table has no uncertainty column or significance annotations. N/A for the human base model means no applicable model, not missing human observations. The benchmark populations differ, and rates must remain attached to their suite and input condition. SeeAct's 66.1% MobileMiniWoB++ performance is close to the 67.7% tie but exceeds accessibility-only full M3A's 59.7%; the prose's broad similarity statement should not erase this row-level ordering.

### Table 4 — Apps and workload allocation

T4, p. 20, lists: Simple Calendar Pro 17; Settings 15; Markor 14; Broccoli 13; Pro Expense 9; Simple SMS Messenger 7; OpenTracks 6; Tasks 6; Clock 4; Joplin 4; Retro Music 4; Simple Gallery Pro 4; Camera 3; Chrome 3; Contacts 3; OsmAnd 3; VLC 3; Audio Recorder 2; Files 2; Simple Draw Pro 1. Descriptions map these to calendars, settings, notes, recipes, expenses, messaging, sports, task lists, clocks, media, camera, browser, contacts, maps, audio, files, and drawing.

[C] Adding the displayed counts gives 17+15+14+13+9+7+6+6+4+4+4+4+3+3+3+3+3+2+2+1 = **123**, seven more than the reported suite total 116. Multi-app tasks might affect attribution, but the supplied work does not explain this total; it cannot be silently reconciled. The table establishes 20 named apps and uneven workload allocation, not a statistically representative distribution of all Android activity.

### Table 5 — Seven initialization and evaluation examples

T5, p. 23, includes VLC playlist creation, recipes from an image, Markor note editing, expense addition, calendar-event deletion, file deletion, and activity counting. Columns give nickname, parameterized template, initial-state setup including distractor data, and success pseudocode. It shows ordered playlist checking, expected database rows, exact note content, absence of deleted records/files, and integer comparison for a count.

An important inconsistency is the ExpenseAddSingle row: its template says add expenses, and success checks for an expense object, but initialization refers to an expense 'that should be deleted'. This may be an editorial error; the supplied source cannot establish the intended code. The recipe-image row's initialization wording says 'receipt file' while the task concerns recipes. That wording is retained as a possible typo, not used to redefine the task.

### Table 6 — Multi-page task catalog

The main text references Table 6, and Appendix F supplies the task list on pp. 28–36 without a visible numbered caption in the provided transcription. Columns are name, template, TC/IR type, validation method, maximum steps S, and apps. Families include recording; browser drawing, maze and multiplication; camera; stopwatch/timer; contacts; expenses; files; Markor creation, editing, merging and transcription; Joplin retrieval; app opening; maps; recipes; music; galleries; calendars; drawing; SMS; sports retrieval; settings; task-list retrieval; composite settings; and VLC playlists.

Task limits include 10 for many simple settings/retrieval tasks, 78 for Markor Merge Notes, and 120 for OsmAnd Track. These limits constrain opportunities and prevent infinite loops; they are not observed action counts. The list includes variants with duplicate-removal constraints, noise, relative dates, recurrence, cross-app transfer, clipboard operations, and explicit answer formats. Repetitive row templates are compressed by family, with material reporting problems preserved in §§14 and 17.

## 12. Diagram / architecture interpretation

Figure 1's system can be read as a repeated control loop. The task evaluator generates a concrete goal and initializes the emulator's app and OS state. The agent receives a screenshot and/or UI tree, selects an action or supported API interaction, and acts on the emulator. The environment changes; observations can be obtained again. Separately, the task evaluator inspects state to determine reward. Task lifecycle logic eventually performs teardown. Sources: pp. 2, 5–7, 17–21.

The key separation is **acting versus checking**. The agent may reach the correct goal by multiple valid paths, while the validator asks whether the requested state exists. For a note-and-message composite, two underlying conditions contribute to reward. For retrieval, generated state determines a correct answer which is compared to the response. This design supports variations because the expected state and checker depend on the same task parameters.

M3A adds an internal feedback stage: instruction and current observation lead to action reasoning and JSON output; execution leads to before/after observations; reflection produces a concise history entry; that history influences the next action. SeeAct instead uses a staged target-selection and candidate-choice prompt, reproduced in Appendix E.6. Sources: pp. 7–8, 27–28.

[D] Security-relevant interfaces can be located in this flow without claiming they were attacked: task instructions and environment observations enter decision-making; execution interfaces turn decisions into device changes; reflection can carry interpretations forward. The paper's benchmark checker sits outside this decision loop and is designed for functional evaluation. A security assessment would need to specify who controls each input and which actions are unauthorized; this paper does not do so.

## 13. Equations and mathematical concepts

There are no numbered equations, optimization losses, theorems, lemmas, propositions, or proof chains in the supplied work. Its mathematical content is primarily reward arithmetic, success percentages, aggregation across seeds, and statistical intervals.

**EQ1: composite reward averaging [A, T2, p. 6].** For the note-and-SMS task, the displayed form is `(file_exists(file_name, content=text) + message_exists(phone_number, message)) / 2.0`. For Wi-Fi plus app opening, it is `(wifi_enabled() + app_launched(app_name)) / 2.0`. The inputs are two success predicates; the output is an average of their evaluations. [D] If those predicates are binary 0/1, the result is 0, 0.5, or 1.0: neither, one, or both subtasks achieved. This binary interpretation is consistent with partial-credit discussion but the table is pseudocode, not a formally typed function specification.

**Success rate [A/C].** Table 3 reports percentages. The ordinary interpretation is successful evaluations divided by evaluated tasks, multiplied by 100. This is an explanatory reconstruction, not a numbered paper equation. The supplied work does not fully specify how composite partial rewards enter every reported overall success percentage; that remains a construct-validity question.

**Wilson binomial proportion confidence intervals [A].** Figure 3 reports 95% Wilson intervals around success proportions. The paper does not print their formula or all endpoints. Therefore the mathematical derivation, exact bounds, and all trial-level success counts cannot be reproduced from the supplied text alone. It also reports p < 0.05 markers without naming the test or exact p-values.

**Information-retrieval transformations [A].** Count, sum, and identity transform initialized records into expected answers. String matching is one shown output comparison. This validates information extraction from generated state; it is distinct from scoring the action sequence. Source: p. 21.

**Notation:** Braces such as `{file_name}` identify task placeholders, S is maximum permitted steps, TC is task completion, IR is information retrieval, SR is success rate, and ∞ in Table 1 indicates effectively unlimited task instantiations. Infinity is a benchmark-variability claim, not a measured finite dataset size. No undefined theoretical symbols need invented meanings.

## 14. Interpretation and discussion

[A] The benchmark supports evaluation by operational outcome and exposes a substantial performance gap between current tested agents and humans. Results also show that stronger prompting is useful under some conditions, that multimodal input is not uniformly superior, and that task parameter choices materially influence outcomes. These findings answer the paper's informal objectives rather than formal hypotheses.

[D] The strongest practical lesson is that a single score can conceal heterogeneous difficulty. An expense category may require no scrolling in one instance and horizontal scrolling in another; note editing may require simple insertion or a multistep replace operation. A benchmark template is therefore not a fixed difficulty unit. The paper's parameterized state and repeated-trial evaluations make this variation visible.

**Source-grounded consistency check:**

| Issue | Source sides | Assessment |
|---|---|---|
| Unlimited instances versus extracted 1 | T1 image, p. 3, shows ∞; extracted rows show 1. | Resolved as extraction discrepancy using visual evidence and parameterization prose. |
| Suite total versus app counts | Main text: 116; T4 sum: 123. | Unresolved; app attribution or revision differences are possible interpretations, not established explanations. |
| App sourcing | p. 6 separates F-Droid open-source apps and fixed OS-level apps; p. 20 says all apps sourced from F-Droid. | Literal sourcing statements differ; do not assert every built-in app was downloaded from F-Droid. |
| Popularity threshold | APP-A says >1M downloads; D.1 says most meet threshold and permits less-popular exceptions. | D.1 qualifies the broad shorthand. |
| MiniWoB++ counts | T1 lists 114 templates; implementation has 92 and excludes twelve original tasks. | 114 − 12 = 102, not 92. The original porting pool/version is not specified; no automatic reconciliation. |
| ExpenseAddSingle setup | T5 adds expenses but says initialized expense should be deleted. | Apparent task/setup mismatch; intended code uncertain. |
| Recipe app labels | p. 31 FromImage template names gallery but Apps names markor; FromMarkor template names Markor but Apps names gallery. | Text-only table mismatch; no silent correction. |
| Brightness task labels | p. 35 Min and Min Verify templates say turn brightness to max. | Name/template inconsistency; intended behavior uncertain. |
| Validation labels | T5 uses VLC SQL and system predicates; p. 36 labels VLC and composite settings String match. | Could reflect final-output comparison or imprecise taxonomy; explanation absent. |

The authors' suggestion that Gemma's lower score likely reflects smaller parameter count is explicitly qualified by unknown proprietary model sizes, p. 9. It should not be promoted to a causal finding. Likewise, one alternate device result cannot isolate OS robustness because device and OS both change. Finally, failure to complete a benign task is not evidence of vulnerability to an adversary. Appendix B identifies a risk, but supplies no exploit experiment.

## 15. Contributions and novelty

[A] The authors list three main contributions on p. 3: a diverse realistic mobile UI-agent environment; benchmark performance with a multimodal agent; and analysis showing why varying task parameters and conditions matters under model/environment stochasticity.

The **system contribution** is a functioning Android benchmark with observation/action interfaces and controlled state. The **benchmark contribution** is reported coverage of 116 task types across 20 apps, plus MobileMiniWoB++ integration. The **methodological contribution** is parameterized initialization and durable outcome validation that survives changing goals. The **implementation contribution** includes reusable filesystem/database/system-state checking and composable task evaluation. The **agent contribution** is M3A's action/reflection loop and text-only/multimodal variants. The **empirical contribution** is the baseline matrix, qualitative failure examples, and robustness analysis. Sources: pp. 2–10.

No theoretical theorem or new security defense is introduced. The claim that automatic parameterization is unique appears in §3.3, but the paper also explicitly recognizes MiniWoB++ as a parameterizable exception. Faithful novelty framing therefore concerns the combined real-app mobile environment and validation machinery, rather than claiming no prior benchmark ever randomized tasks.

[D] For security research, the reusable outcome infrastructure could support checking whether an agent changed files, databases, messages, or settings improperly in a separately designed experiment. That is a potential extension, not a contribution tested in this paper. Neither attack-surface enumeration nor comparative standalone-LLM evaluation is an author-claimed result here.

## 16. Limitations

### Authors' stated limitations

[A] Appendix A limits current support to open-source Android apps and built-in system apps. Trending apps would be desirable; open-source apps may have less optimized interfaces and require more complex interaction patterns. The delete-all example illustrates the agent's incorrect assumption that a bulk affordance exists. Source: p. 17.

[A] Reproducibility requirements exclude apps requiring authentication or nonlocal data storage from the described selection. Sources: pp. 6, 19. MobileMiniWoB++ excludes twelve named tasks because of real-time interaction demands, difficult clicks, touch incompatibility, rendering failures, or nonfunctional widgets. Source: p. 19. The robustness subset is limited by computational constraints. Source: p. 9.

[A] Tested agents struggle with perception, reasoning, grounding, UI knowledge, memory, recovery, and latency. Sources: pp. 9, 23–26. These are limitations of tested agents, distinct from limitations of the benchmark. Task-generation assistance requires human review and can hallucinate protobuf fields. Source: p. 21. Proprietary parameter counts prevent clean model-size comparisons. Source: p. 9.

### Additional evidence-based analyst observations

[D] The controlled local-data, no-login setting omits important aspects of ordinary authenticated service use. Two human evaluators and a single attempt per task limit the precision and interpretation of the human comparison. Main T3 results have no uncertainty estimates. Full-versus-simple comparisons do not isolate each prompting feature. Device and OS changes are confounded in X6. The task-count and catalog inconsistencies reduce confidence in exact coverage accounting.

[D] A system-state checker can accurately detect its defined predicate without proving that every undesirable collateral change is checked. The supplied pseudocode does not establish complete side-effect constraints for all tasks. This is an evidence boundary, not a claim that the implementation definitely overlooks harmful effects.

[D] For the user's research question, the decisive limitation is absent comparative security evidence: no attacker-controlled condition, no standalone-model baseline, no exploit success metric, and no defense evaluation. Security relevance is MEDIUM-confidence inference; any claim of greater vulnerability from this paper alone would be unsupported.

## 17. Threats to validity

These categories are **analyst observations [D]**, not headings or admissions attributed to the authors.

**Internal validity:** Multiple changes distinguish full M3A from M3A-Simple, so improvement cannot be assigned only to reflection. SeeAct adaptation changes action support, candidate representation, and ranker availability relative to its original web implementation. The alternate setup changes device and OS simultaneously. Parameter changes can alter interaction difficulty, which is the intended variable but must remain separate from model randomness.

**External validity and generalizability:** The environment uses selected apps, emulator configurations, fixed versions, local storage, and no required login. Results do not establish performance over all Android apps or unrestricted websites. The 62-task MobileMiniWoB++ subset is not the full 92-task implementation. Open-source UI characteristics may differ from more optimized popular applications, as the authors note.

**Construct validity:** Success rate measures defined task outcomes. It is not an attack-resistance score, a safety score, or a proof of understanding. Exact answer formats may make retrieval sensitive to formatting. Composite tasks allow partial rewards, but overall SR aggregation is insufficiently detailed. Validation-method labels differ between examples and catalog rows.

**Statistical conclusion validity:** T3 gives point estimates without confidence intervals; the multi-seed evaluation uses three seeds; X5 uses five tasks and 20 trials per task. Figure 3 reports Wilson intervals and significance markers but not exact p-values, test identity, multiple-comparison treatment, or complete raw outcomes. Wide intervals visibly limit precision. The rounded percentages should not be converted into exact task counts without explicit run-level denominators.

**Ecological validity:** Real apps and naturalistic actions improve realism, but scripted initialization and frozen time differ from uncontrolled user devices. Synthetic WebView tasks differ from arbitrary live-web interaction. Hidden content, authentication, network state, and changing app versions are not comprehensively covered in the reported experiments.

**Reproducibility:** Fixed OS/app state, seed 30, temperature 0, reset time, teardown, and per-task step limits are substantial strengths. Remaining gaps include exact model endpoints, full dependency versions, detailed timing definitions, seed identities for X4, the statistical test in X5, and unresolved catalog contradictions. The repository may clarify these, but it was not supplied for review and was not consulted.

## 18. Future work and open questions

### A. Explicit author-proposed directions

[A] The paper anticipates improved cross-platform agents, more effective models, online learning, reinforcement-learning-like mechanisms, and supervised dataset generation from dynamic tasks. Sources: pp. 1, 6, 10. It suggests nonzero rewards under some parameter seeds could support learning improvements. More efficient models would make repeated robustness testing more practical. Source: p. 10. Appendix C.2 mentions future hybrid interaction combining UI actions with programmatic device APIs. Trending-app evaluation is desirable according to Appendix A.

### B. Additional questions remaining from the supplied evidence

[D] Which component of the M3A prompting bundle contributes most? How does observation quality, rather than merely modality, change performance? Can exact task inventories and app-count totals be reconciled? How stable are model rankings over many seeds, versions, and tasks? What proportion of failures belongs to each qualitative category? How much latency is model inference versus environment interaction?

[D] For security: who can control instructions, screen content, element descriptions, or stored records? Can manipulated observations produce unauthorized device actions? How should an agent's operational capabilities be matched to a standalone LLM comparison? Which outcome predicates capture damage rather than benign completion? How should collateral effects, repeated attempts, and task-instance difficulty be controlled? These are proposed research questions by the analyst, not answered by AndroidWorld. The paper supplies a possible evaluation substrate and one ethical warning, but no comparative attack evidence.

## 19. Terminology and notation glossary

| Term | Beginner-friendly meaning in this paper |
|---|---|
| AndroidWorld | Controlled Android environment and task suite for evaluating agents. |
| Autonomous agent | A system that observes a device, chooses actions, executes them, and continues toward a goal. |
| LLM | Large language model; used as the decision-making model inside tested agents. |
| M3A | Multimodal Autonomous Agent for Android, with action generation and reflection. |
| M3A-Simple | Variant without the full guidelines and reflection mechanisms. |
| SeeAct | Adapted web-agent baseline using textual candidate choices for grounding. |
| UI | User interface: application controls and visible content. |
| Accessibility tree / a11y tree | Structured UI elements and attributes available for accessibility. |
| SoM | Set-of-Mark: numbered boxes over UI elements in a screenshot. |
| DOM | Document Object Model; website representation discussed in contrast with Android accessibility trees. |
| adb | Android Debug Bridge; executes device interactions and supports state inspection. |
| AndroidEnv | Library used to communicate with the emulator. |
| RGB | Three color channels in screenshot pixels. |
| gRPC | Named communication mechanism used for accessibility forwarding; protocol internals are not explained in the paper. |
| API | Application programming interface; programmatic device functionality. |
| APK | App package used to select and distribute fixed app versions. |
| SQLite | Database mechanism used by apps and inspected by validators. |
| Protobuf | Structured task-definition format used for information retrieval. |
| TaskEval | Base task interface supporting lifecycle and success evaluation. |
| Initialization / teardown | Preparing task state / cleaning up after the task. |
| Parameterization | Filling task placeholders with values that vary goals and initial conditions. |
| Seed | Value controlling random parameter generation. |
| Grounding | Linking a chosen operation to the correct UI target and interaction. |
| Reflection | Reviewing an action's effect to guide later actions. |
| Zero-shot | Presented agent setup without task-specific demonstration examples. |
| SR | Success rate, reported as a percentage. |
| TC / IR | Task completion / information retrieval. |
| S | Maximum permitted action steps in Appendix F. |
| No-op | Action that performs no substantive device operation, such as wait or unknown. |
| Wilson interval | Reported uncertainty interval for binomial success proportions. |
| p < 0.05 | Threshold for Figure 3 significance markers; exact test and p-values are unspecified. |
| ∞ | Visually shown unlimited-instance designation in Table 1. |
| CAPTCHA | Security measure named in the ethics discussion; no CAPTCHA experiment is conducted. |

## 20. Key numerical results

| Quantity / Result | Value | Unit | Condition / Context | Status | Source |
|---|---:|---|---|---|---|
| Reported AndroidWorld suite | 116 | Tasks | Programmatic task suite | Author-reported | pp. 1–2, 5–10 |
| Apps | 20 | Apps | Benchmark coverage | Author-reported | pp. 1–3, T4 p. 20 |
| Implemented MobileMiniWoB++ | 92 | Tasks | Mobile WebView adaptation | Author-reported | pp. 7, 19 |
| Evaluated MobileMiniWoB++ | 62 | Tasks | T3 comparison subset | Author-reported | p. 8 |
| Excluded porting tasks | 12 | Tasks | Compatibility/realtime/rendering exclusions | Author-reported | pp. 7, 19 |
| Main seed | 30 | Seed identifier | Agent benchmark evaluation | Author-reported | p. 8 |
| Temperature | 0 | Model setting | Main evaluation | Author-reported | p. 8 |
| Gemma 2 size | 27B | Parameters | Tested open-source base model | Author-reported | p. 8 |
| Best AndroidWorld agent | 30.6 | % success | M3A, GPT-4 Turbo, accessibility input | Author-reported | T3 p. 8 |
| AndroidWorld human | 80.0 | % success | Human screen interaction | Author-reported | T3 p. 8 |
| AndroidWorld SeeAct | 15.5 | % success | GPT-4 Turbo, SoM | Author-reported | T3 p. 8 |
| AndroidWorld simple GPT-4 | 19.8 | % success | M3A-Simple, accessibility input | Author-reported | T3 p. 8 |
| AndroidWorld multimodal GPT-4 | 25.4 | % success | M3A, SoM | Author-reported | T3 p. 8 |
| MobileMiniWoB++ human | 100.0 | % success | Reported human result | Author-reported | T3 p. 8 |
| Highest MobileMiniWoB++ agent | 67.7 | % success | Tie: GPT-4 simple/accessibility and full/SoM | Author-reported | T3 p. 8 |
| Three-seed scores | 27.6; 26.3; 33.2 | % success | M3A, GPT-4 Turbo, accessibility | Author-reported | p. 9 |
| Three-seed mean | 29.0 | % success | Author's reported rounded mean | Author-reported | p. 9 |
| Three-seed range | 6.9 | Percentage points | 33.2 − 26.3 | Analyst-derived | p. 9 operands |
| Robustness repetition | 20 | Trials per task | Five selected tasks; two parameter conditions described | Author-reported | p. 9 |
| Confidence level | 95 | % | Wilson intervals in F3 | Author-reported | p. 10 |
| Significance threshold | <0.05 | p-value | F3 marked comparisons | Author-reported | p. 10 |
| Alternate device result | 28.4 | % success | Pixel 5, Android 12 | Author-reported | p. 10 |
| M3A task time | 3.9 | Minutes | Reported average; aggregation details absent | Author-reported | p. 9 |
| Text-only task time | 2.5 | Minutes | Reported average | Author-reported | p. 9 |
| Environment memory | 2 | GB | AndroidWorld requirement | Author-reported | p. 2 |
| Environment disk | 8 | GB | AndroidWorld requirement | Author-reported | p. 2 |
| Screenshot | 2400 × 1080 × 3 | Array dimensions | RGB device capture | Author-reported | p. 17 |
| Annotation volunteers | 6 | People | Task analysis | Author-reported | p. 22 |
| Human evaluators | 2 | People | Software engineers | Author-reported | p. 22 |
| Fixed timestamp | 2023-10-15 15:34 | UTC date/time | Reset at each task | Author-reported | p. 6 |
| Bugs resolved | >30 | Bugs | Human annotation phase | Author-reported | p. 22 |
| Table 4 total | 123 | Listed app-task counts | Sum displayed in §11 | Analyst-derived | T4 p. 20 |
| Human–best agent gap | 49.4 | Percentage points | 80.0 − 30.6 | Analyst-derived | T3 p. 8 |
| Prompting-bundle difference | 10.8 | Percentage points | 30.6 − 19.8 | Analyst-derived | T3 p. 8 |
| AddExpense varying-seed bar | About 45 | % success | Estimated from F3 position | Approximate visual estimate | F3 p. 10 |
| Largest catalog step limit discussed | 120 | Allowed steps | OsmAnd Track | Author-reported | p. 31 |

The complete T3 matrix remains in §9 rather than repeating every model score here. No numeric attack-success result, standalone-LLM comparison, security effect size, or defense score is supplied.

## 21. Claim–evidence map

| Claim | Evidence | Figure/Table/Experiment | Source | Qualification / Evidence Strength |
|---|---|---|---|---|
| AndroidWorld supports realistic mobile outcome evaluation. | Actual apps, state initialization, validators, teardown. | F1, T2, T5 | pp. 2, 6–7, 23 | HIGH for described design; independent code validation not performed. |
| Tasks vary through controlled parameters. | Seeded goals and initial states with parameter-aware rewards. | F1, X4–X5 | pp. 2, 6, 9–10 | HIGH; unlimited variation is a design claim, not an enumerated dataset. |
| State access enables reusable durable validators. | Filesystem, databases, settings, plus UI fallback. | T2, T5 | pp. 6–7 | HIGH for author mechanism; accuracy not separately quantified. |
| Current best tested Android agent remains below humans. | 30.6% versus 80.0%. | T3, X1 | p. 8 | HIGH; human aggregation and uncertainty incompletely specified. |
| Advanced prompting helps in one main condition. | GPT-4 accessibility 30.6 versus simple 19.8. | T3, X2 | pp. 8–9 | HIGH result; feature-specific causation not isolated. |
| Multimodal input is condition-dependent. | Opposite suite ordering for GPT-4; different Gemini pattern. | T3, X3 | pp. 8–9 | HIGH for row comparisons; no universal modality conclusion. |
| Parameter choices affect performance. | Three-seed scores, F3, horizontal-scroll and edit variants. | X4–X5, F3, F8 | pp. 9–10, 26 | HIGH for observed variation; selected-task scope and test details limit generalization. |
| An alternate device retains some capability. | 28.4% Pixel 5/Android 12. | X6 | p. 10 | HIGH for reported score, MEDIUM for broad robustness interpretation. |
| Agent failures include grounded interaction mistakes. | Wrong cursor placement, wrong field, missed checkbox, missing bulk-delete knowledge. | X7, F6–F8 | pp. 23–26 | HIGH qualitative evidence; frequencies not supplied. |
| Harmful manipulation is contemplated. | Ethics warning about altered prompts and screen outputs. | APP-B | p. 17 | HIGH as an author risk statement; no attack experiment. |
| Paper is indirectly relevant to web-agent security. | External observations guide executable actions; ethical warning names manipulation. | F1, APP-B, ALG1/ALG5 | pp. 5, 17–18, 27–28 | MEDIUM analyst inference; no standalone-model comparison. |
| Exact workload accounting is uncertain. | 116 main count versus T4 sum 123 and catalog inconsistencies. | T4/T6 | pp. 1, 20, 28–36 | HIGH for displayed discrepancies; underlying implementation unknown. |

## 22. Very simple explanation — Explain Like I'm 15

Imagine testing an AI by giving it a phone and asking it to create an appointment, edit a note, or send a message. It is not enough for the AI to explain what it would do. The phone has to end up with the right appointment, note, or message. AndroidWorld is a controlled phone environment that can set up these tasks and check the result automatically.

The researchers make many versions of the same task. One version might put an expense category directly on screen; another might hide it behind sideways scrolling. The AI can solve the first and fail the second even though both are called 'add an expense'. This is why a single test score does not tell the whole story. In the main experiment, the best tested AI completed 30.6% of AndroidWorld tasks, while humans completed 80.0%.

The AI agents also make different kinds of mistakes. They miss a checkbox, misunderstand which box needs a name, put text at the wrong place, or search for a button that the app does not have. Looking at screenshots helps in some conditions, but the paper does not find that screenshots always improve results.

For your security question, the useful idea is that an agent reads what is on a device and can then change things on that device. The authors warn that malicious actors could alter prompts or screen outputs. But they do not test an attack or compare an agent with a standalone language model. This paper helps explain what parts of an interactive agent might need security testing; it does not prove that web agents are more vulnerable.

## Completeness Audit

The audit uses the inventory established in Stage 0. 'Represented in compressed form' means the essential mechanism, evidence, qualifications, or scope is explained, while repetitive templates or bibliographic details are not reproduced verbatim. Visual inspection is distinguished from text-only reading.

| Item | Inspected? | Represented? | Status | Notes |
|---|---|---|---|---|
| Title, authors, venue, abstract | Text and image p. 1 | Yes | Represented in compressed form | Original title retained; ICLR 2025; authors listed below. |
| S1 Introduction | Text/images pp. 1–2 | Yes | Fully represented | Outcome evaluation, motivation, mobile gap. |
| S2 and SS2.1 | Text pp. 3–4; image p. 3 | Yes | Represented in compressed form | Interactive benchmark categories and T1 preserved. |
| SS2.2 Static datasets | Text p. 4 | Yes | Represented in compressed form | Demonstrations, accessibility/DOM, API datasets. |
| SS2.3 Interactive agents | Text pp. 4–5; image p. 5 | Yes | Represented in compressed form | Prior learning and foundation-model approaches. |
| SS3.1 Android platform | Text/image p. 5 | Yes | Represented in compressed form | Emulation, UI actions, mobile complexity; contextual prevalence claims not independently verified. |
| SS3.2 Observations/actions | Text/image p. 5 | Yes | Fully represented | Expanded using APP-C. |
| SS3.3 Parameterized tasks | Text/images pp. 5–6 | Yes | Fully represented | Fixed state, seeds, timestamp, versions. |
| SS3.4 Durable rewards | Text/images pp. 6–7 | Yes | Fully represented | State access and UI fallback. |
| SS3.5 Composability | Text/image p. 7 | Yes | Fully represented | Composite predicates and partial credit. |
| SS3.6 MobileMiniWoB++ | Text/image p. 7 | Yes | Fully represented | WebView, no DOM, 92 tasks, exclusions. |
| SS4.1.1 M3A | Text/images pp. 7–8 | Yes | Fully represented | Action/reflection loop and modalities. |
| SS4.1.2 SeeAct | Text/image p. 8 | Yes | Fully represented | Adaptation and ranker omission. |
| SS4.2 Experimental results | Text/images pp. 8–9 | Yes | Fully represented | Entire T3 matrix and conditions. |
| SS4.3 Analysis | Text/image p. 9 | Yes | Fully represented | Qualitative errors, memory, latency. |
| S5 Robustness | Text/images pp. 9–10 | Yes | Fully represented | X4–X6, intervals, device result. |
| S6 Conclusion | Text/image p. 10 | Yes | Represented in compressed form | Environment, benchmark, online learning. |
| References | Text pp. 10–17; partial images | Yes | Inspected but deliberately omitted as bibliographic detail | No cited paper independently reviewed. |
| Formal research questions | Searched in supplied text | Yes | None identified | Informal O1–O6 distinguished from user question. |
| Formal hypotheses | Searched in supplied text | Yes | None identified | No invented hypothesis tests. |
| X1 Benchmark comparison | T3/prose | Yes | Fully represented | Human and all agent conditions retained. |
| X2 Prompting comparison | T3/prose | Yes | Fully represented | Bundle-confounding qualification. |
| X3 Observation comparison | T3/prose | Yes | Fully represented | Both models and suites distinguished. |
| X4 Three-seed analysis | Text/image p. 9 | Yes | Fully represented | All three scores and mean. |
| X5 Repeated trials | F3/prose | Yes | Fully represented | Five tasks, 20 trials, exact test unavailable. |
| X6 Device/OS | Text/image p. 10 | Yes | Fully represented | 28.4%; combined device/OS change. |
| X7 Error analysis | Text/images pp. 23–26 | Yes | Fully represented | Mechanisms without invented prevalence. |
| X8 Latency | Text/image p. 9 | Yes | Fully represented | 3.9 and 2.5 minutes; unclear timing boundaries. |
| H1 Task annotation | Text/image p. 22 | Yes | Fully represented | Six volunteers, >30 bugs. |
| H2 Human evaluation | Text/image p. 22 | Yes | Fully represented | Two engineers, one attempt, aggregation uncertainty. |
| F1 Architecture | Visually inspected p. 2 | Yes | Fully represented | Small decorative app icons compressed. |
| F2a Difficulty | Visually inspected p. 5 | Yes | Represented in compressed form | Ordering retained; exact counts uncertain. |
| F2b Steps | Visually inspected p. 5 | Yes | Represented in compressed form | Distribution shape; exact bins not extracted. |
| F2c Categories | Visually inspected p. 5 | Yes | Represented in compressed form | Category labels and largest groups retained. |
| F3 Robustness plot | Visually inspected p. 10 | Yes | Fully represented | Approximate bars explicitly labeled. |
| F4 Native input | Visually inspected p. 19 | Yes | Fully represented | Widget mechanism; small date text secondary. |
| F5 SoM screen | Visually inspected p. 24 | Yes | Represented in compressed form | Individual small index values unreadable. |
| F6a–c Errors | Visually inspected p. 24 | Yes | Fully represented | Three mechanisms separately explained. |
| F7a–b Grounding | Visually inspected p. 25 | Yes | Fully represented | Pixel text limited; prose supports cursor mechanism. |
| F8 Hidden category | Visually inspected p. 26 | Yes | Fully represented | Layout observed; consistent failure author-reported. |
| T1 Benchmark comparison | Text and image p. 3 | Yes | Represented in compressed form | All entries/counts/rewards retained; platforms grouped. |
| T2 Validators | Text and image p. 6 | Yes | Fully represented | Six tasks and two composite averages. |
| T3 Success rates | Text and image p. 8 | Yes | Fully represented | Every row retained. |
| T4 App list | Text and image p. 20 | Yes | Fully represented | Every count and derived total discrepancy. |
| T5 Task examples | Text and image p. 23 | Yes | Fully represented | Seven mechanisms and setup mismatch. |
| T6 Task list | Text-only pp. 28–36 | Yes | Represented in compressed form | Families, step limits, variants, and inconsistencies; no claim of visual table inspection. |
| EQ1 Composite rewards | Text/image p. 6 | Yes | Fully represented | Binary interpretation qualified. |
| Other mathematical concepts | Text/figures | Yes | Fully represented | SR, mean, Wilson intervals, p threshold. |
| Numbered equations/theorems/proofs | Supplied document | Yes | None identified | No omitted formal derivation. |
| ALG1 Action dataclass | Text-only p. 18 | Yes | Represented in compressed form | Actions and fields retained. |
| ALG2 SendSms | Text pp. 20–21; image p. 20 | Yes | Fully represented | Setup, check, random parameters, cleanup. |
| ALG3 IR protobuf | Text pp. 21–22; image p. 22 | Yes | Represented in compressed form | State, exclusion, identity, matching, parameters. |
| ALG4 UI prompt Listing 2 | Text/image p. 22 | Yes | Represented in compressed form | UI descriptions, reason, JSON action. |
| ALG5 SeeAct prompt | Text-only pp. 27–28 | Yes | Represented in compressed form | Reasoning stages, candidate selection, output fields. |
| APP-A Limitations | Text/image p. 17 | Yes | Fully represented | App scope and UI affordances. |
| APP-B Ethics | Text/image p. 17 | Yes | Fully represented | Malicious use, altered inputs, societal risks. |
| APP-C.1 Observations | Text/image p. 17 | Yes | Fully represented | State fields and asynchronous stabilization. |
| APP-C.2 Actions | Text-only p. 18 | Yes | Fully represented | UI/control/system actions and high-level APIs. |
| APP-C.3 Mobile web | Text/image p. 19 | Yes | Represented in compressed form | All exclusion classes; individual task names below. |
| APP-D.1 Selection | Text/images pp. 19–20 | Yes | Fully represented | Use case/popularity/version control and sourcing conflict. |
| APP-D.2 Side-effect tasks | Text pp. 20–21 | Yes | Fully represented | Python lifecycle and SMS example. |
| APP-D.3 Retrieval | Text pp. 21–22 | Yes | Fully represented | Proto authoring and human review. |
| APP-D.4 Human analysis | Text/image p. 22 | Yes | Fully represented | Participants, attempts, consent context. |
| APP-D.5 Examples | T5 | Yes | Fully represented | Parameterization and validators. |
| APP-E.1 Observations | Text/image p. 22 | Yes | Fully represented | Pixels, SoM, UI descriptions. |
| APP-E.2 Actions | Text/image pp. 23–24 | Yes | Fully represented | SoM derived from accessibility. |
| APP-E.3 Errors | Text/images pp. 23–25 | Yes | Fully represented | Four named categories and examples. |
| APP-E.4 Robustness tasks | Text/images pp. 25–26 | Yes | Fully represented | All five task identities. |
| APP-E.5 Parameter failures | Text/image p. 26 | Yes | Fully represented | Horizontal scrolling and edit variants. |
| APP-E.6 SeeAct prompt | Text pp. 26–28 | Yes | Represented in compressed form | Prompt is source evidence only. |
| APP-F catalog | Text-only pp. 28–36 | Yes | Represented in compressed form | Repetitive rows grouped; material contradictions preserved. |
| Major contributions | p. 3 and methods/results | Yes | Fully represented | System, benchmark, method, agent, empirical. |
| Author-stated limitations | APP-A and dispersed caveats | Yes | Fully represented | Distinguished from analyst observations. |
| Supplied supplementary files | None | N/A | Not supplied | No file reviewed. |
| Referenced repository | URL in abstract | No | Inaccessible within supplied evidence | Availability claim retained; contents not assessed. |

**Additional inventory details compressed elsewhere:** The author list is Christopher Rawles, Sarah Clinckemaillie, Yifan Chang, Jonathan Waltz, Gabrielle Lau, Marybeth Fair, Alice Li, William Bishop, Wei Li, Folawiyo Campbell-Ajala, Daniel Toyama, Robert Berry, Divya Tyamagundlu, Timothy Lillicrap, and Oriana Riva. Affiliations are Google DeepMind and Google. Rawles is marked lead contributor; Clinckemaillie and Chang have equal-contribution marks. Contact and download/source footnotes are provenance/navigation details, not experimental findings.

The twelve MobileMiniWoB++ exclusions are chase-circle, moving-items, drag-cube, drag-items-grid, drag-items, drag-shapes, drag-sort-numbers, text-editor, number-checkboxes, use-slider-2, use-spinner, and click-menu. Their reasons are represented by class in §§7 and 16; repeating every implementation symptom is unnecessary to understand the benchmark boundary.

Appendix B also warns that automation may alter societal norms, employment, and human behavior, and that efficiency gains may be misused. These are ethical considerations rather than measured social outcomes. The SeeAct prompt asks for current-screen identification, previous-action analysis, screenshot analysis, next-action selection, then a multiple-choice grounding decision and ELEMENT/ACTION/VALUE output. It includes instructions about account creation, login, final submission, and harmful actions; these are properties of the reproduced baseline prompt, not evidence of verified enforcement or instructions followed by this analysis.

### Missing or inaccessible material

No pages are missing within the supplied transcription. Page images are absent for the text-only pages listed in Stage 0, including most references, action-space pseudocode, the retrieval example's first page, the complete SeeAct prompt, and Appendix F. The referenced repository and any external implementation details are unavailable to this closed-document review. No separate supplement, executable artifact, raw run log, complete trial outcomes, or independently checked APK/version manifest was supplied.

### Uncertain interpretations

Exact Figure 2 bar/bin values, individual tiny SoM marks, and small screenshot character strings cannot be confidently read. Figure 3 bar heights are approximate. The statistical test, exact p-values, interval endpoints, human-score aggregation, and latency boundaries are not fully specified. Task accounting, app sourcing, porting-pool totals, ExpenseAddSingle setup, recipe app columns, brightness-min templates, and validation labels contain unresolved ambiguities or conflicts. The repository could potentially clarify them, but was not reviewed.

### Deliberately compressed material

The bibliography, repeated task templates, code boilerplate, illustrative parameter strings, small app icons, detailed prompt wording, and repetitive per-task step limits are compressed. The entire principal success-rate table, app counts, task families, all figures, all substantive sections, all appendix subsections, all distinct analyses, and material contradictions are represented. No numbered theorem or theoretical equation was omitted because none was identified.

### Potential omissions

No known substantive inventory item is left entirely unrepresented in this response. That is an inventory-based coverage statement, not a claim of perfect preservation or independent validation of the implementation. Exact catalog rows and all prompt/code characters are deliberately not reproduced; unreadable visual details and absent external artifacts remain explicit limitations. The requested security comparison remains unanswered by this source: AndroidWorld supports a carefully labeled inference about relevant agent interfaces, but provides no direct evidence that web AI agents are more vulnerable than standalone LLMs.
