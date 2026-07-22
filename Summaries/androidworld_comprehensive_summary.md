# *AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents*

**Authors:** Christopher Rawles, Sarah Clinckemaillie, Yifan Chang, Jonathan Waltz, Gabrielle Lau, Marybeth Fair, Alice Li, William Bishop, Wei Li, Folawiyo Campbell-Ajala, Daniel Toyama, Robert Berry, Divya Tyamagundlu, Timothy Lillicrap, and Oriana Riva  
**Affiliations:** Google DeepMind and Google  
**Publication:** ICLR 2025 conference paper

## 1. Background and Context

Autonomous computer-control agents translate natural-language instructions into actions on phones or computers. Such agents could automate repetitive work, increase productivity, improve accessibility, and execute complex workflows. Evaluating them realistically, however, is difficult.

Many existing benchmarks compare an agent’s action sequence against a previously recorded human demonstration. That comparison is an imperfect measure of success because:

- Several different action sequences may accomplish the same goal.
- Real applications can behave non-deterministically.
- An agent may make an error and then recover through a valid alternative path.
- Matching actions does not necessarily establish that the intended result was achieved.

The authors therefore regard online, outcome-based evaluation in a functioning environment as the preferred standard. For example, success on “Send a text message to Jane confirming I’ll be there” should be determined by checking whether the correct message was actually sent—not whether the agent reproduced a human’s taps.

Real applications do not normally expose explicit reward signals. Human judges can assess outcomes but scale poorly, while language-model judges may be unreliable. Existing environments with automatic ground-truth rewards are largely desktop-oriented, have limited application diversity, or use static task specifications whose validation may fail when task parameters change.

Mobile platforms create distinct challenges:

- Their screens are smaller, but their action space includes gestures such as swiping, long-pressing, carousel navigation, and sometimes multi-finger zooming.
- Tasks often require more steps than desktop web tasks.
- Android combines ordinary UI control with operating-system functions and programmatic APIs.
- Accessibility trees may be incomplete, and many tasks require interaction with application or device state rather than visible text alone.

Android is attractive for research because it can be emulated without specialized hardware, emulator images are self-contained and configurable, and the environment includes both apps and the mobile web.

### Relation to prior benchmarks

The paper’s Table 1 distinguishes environments with actual interactive reward mechanisms from static datasets. Examples include:

- Static mobile datasets such as PixelHelp, MoTIF, Android in the Wild, AndroidControl, AndroidArena, and LlamaTouch, which mainly contain demonstrations and ordinarily have one instance per task template.
- Small reproducible mobile environments such as B-MoCA, with 6 tasks across 4 apps, and Mobile-Env, with 13 templates for one app.
- Desktop environments such as OSWorld, WindowsAgentArena, and AgentStudio, covering 369 tasks across 9 apps, 154 across 11 apps, and 205 across 9 apps, respectively.
- Web environments such as WebArena, VisualWebArena, WorkArena, WebShop, and MiniWoB++.

AndroidWorld is listed as an interactive Android environment with **20 apps, 116 task templates, device-state rewards, and one benchmark instance per reported evaluation**, although each template can generate effectively unlimited parameterized instances. MiniWoB++ is another parameterizable environment, but it consists of synthetic web pages rather than real Android applications.

AndroidWorld differs from AndroidEnv as well. AndroidEnv generally requires modifying application source code and adding task-specific logging. AndroidWorld instead inspects external system state, so it can evaluate apps whose source code is unavailable and reuse validators across unrelated applications.

---

## 2. Research Goal and Objectives

The main goal is to create a realistic, reproducible, and dynamically variable Android environment for developing and evaluating autonomous computer-control agents.

The paper has three principal objectives:

1. **Build AndroidWorld**, an environment that supplies automatic ground-truth rewards for practical tasks in real Android applications.
2. **Establish initial benchmark performance** using a new agent, M3A, its simplified variants, and an Android adaptation of the web agent SeeAct.
3. **Test robustness under task variation**, showing whether reported performance remains stable when random task parameters, starting states, UI interaction requirements, or Android configurations change.

A secondary objective is to integrate MiniWoB++ into the same mobile framework, producing **MobileMiniWoB++**, so web-style tasks can be tested through Android-native observations and actions.

---

## 3. Methods (Approach/Design)

### 3.1 AndroidWorld environment

AndroidWorld contains **116 programmatic task templates across 20 real Android apps**. Randomly generated parameters allow these templates to produce millions of natural-language goals and a practically unlimited set of initial conditions and success criteria.

The environment is lightweight, requiring approximately **2 GB of memory and 8 GB of disk space**. It connects Python agents to the freely available Android Emulator using AndroidEnv and Android Debug Bridge, or ADB.

**Figure 1** summarizes the architecture:

1. A task class generates random parameters and a natural-language goal.
2. It initializes the relevant OS and application state.
3. An agent receives a screenshot and UI tree, or uses permitted APIs.
4. The agent controls an Android emulator containing real apps.
5. Task-specific evaluation code inspects system or UI state and returns a reward.
6. Teardown logic cleans up the task.

The figure gives examples such as creating a parameterized calendar event, adding an OsmAnd location marker, submitting a date in a web task, and answering which tasks remain incomplete by a given date.

### 3.2 Applications and task coverage

The 20 applications and numbers of tasks are:

- Simple Calendar Pro: **17**
- Android Settings: **15**
- Markor: **14**
- Broccoli recipe app: **13**
- Pro Expense: **9**
- Simple SMS Messenger: **7**
- OpenTracks: **6**
- Tasks: **6**
- Clock: **4**
- Joplin: **4**
- Retro Music: **4**
- Simple Gallery Pro: **4**
- Camera: **3**
- Chrome: **3**
- Contacts: **3**
- OsmAnd: **3**
- VLC: **3**
- Audio Recorder: **2**
- Files: **2**
- Simple Draw Pro: **1**

The suite covers calendar management, notes and folders, recipes, expenses, SMS, sport records, task lists, timers, contacts, maps, media, camera operations, file management, system settings, drawing, and browser-based activities. It includes both task-completion tasks that change state and information-retrieval tasks that ask the agent to inspect state and answer a question.

App selection considered use case, category, popularity, consistency, and reproducibility. The researchers focused on productivity, communication, and multimedia apps that did not require login and stored data locally. Most selected apps had more than one million downloads. Less popular apps were included when they represented common Android UI patterns. Fixed app versions were sourced from F-Droid, using the newest version available when downloaded.

### 3.3 Reproducibility controls

The main configuration is a **Pixel 6 emulator running Android 13**. At the start of every task, the device clock is reset to **October 15, 2023, at 15:34 UTC**, preventing inconsistent time-dependent behavior.

Each task supplies:

- A natural-language template.
- Random parameter generation.
- Initialization of the exact starting state.
- Success-evaluation logic.
- Teardown logic.

The random parameters are generated from a controlled seed. They determine both the instruction and relevant starting conditions.

Apps do not require authentication, store data on-device, and remain at fixed versions. Built-in app versions are fixed through the Android OS image.

### 3.4 Observations

An Android state contains:

- **Pixels:** a full RGB screenshot with shape **2400 × 1080 × 3**.
- **Accessibility tree:** a raw snapshot of UI elements in all current windows.
- **Processed UI elements:** objects containing properties such as visible text, content descriptions, bounding boxes, clickability, scrollability, and focus state.

An AndroidEnv forwarding application sends accessibility information using gRPC.

Because Android actions and observations are asynchronous, AndroidWorld does not assume an immediate one-to-one transition after each action. Its `get_state` operation can wait for the interface to stabilize using heuristics before returning a snapshot.

### 3.5 Action space

Actions are represented as structured JSON/Python objects and executed through ADB. They include:

- Click and long-press.
- Text input and keyboard Enter.
- Scrolling up, down, left, or right.
- Home and Back navigation.
- Opening an app.
- Waiting for a transition.
- Reporting that a goal is in progress, complete, or infeasible.
- Returning a direct answer for information-retrieval tasks.
- An unknown/no-op action for internal errors.

The framework also contains optional high-level APIs for actions such as sending SMS messages, opening web pages, and managing contacts. These permit future study of hybrid agents that combine UI control with programmatic device operations.

### 3.6 Automatic rewards from system state

AndroidWorld primarily calculates rewards by inspecting the device through ADB. It can access:

- Application SQLite databases.
- The filesystem.
- System settings.
- Other OS-managed application state.

Where system inspection is impractical, it checks visible UI elements.

System-state evaluation is intended to be more accurate and durable than matching surface-level screenshots. Validators can also be reused: one file-existence checker can evaluate tasks in note-taking, file-management, drawing, or media applications, while database evaluators can check inserted or deleted rows across apps.

**Table 2** illustrates several validators:

- Calendar creation succeeds if the parameterized event exists.
- SMS succeeds if the specified number and message appear in the messaging database.
- A drawing succeeds if the target file exists.
- A timer succeeds if the requested time is displayed in the UI hierarchy.
- Creating and texting a note gives composite credit from both file existence/content and message existence.
- Turning on Wi-Fi and opening an app combines the Wi-Fi and app-launch checks.

Composite tasks can therefore provide partial credit for completed subtasks and potentially support hill-climbing or reinforcement-learning approaches.

### 3.7 Task generation

Tasks with side effects are implemented as Python classes. For example, the SMS task:

1. Clears the SMS database.
2. Randomly generates a number and message.
3. asks the agent to send that message;
4. checks the telephony database for the exact number and body;
5. clears the database during teardown.

Information-retrieval tasks use protobuf specifications rather than separate Python classes. Each specification defines:

- The parameterized prompt.
- Relevant initial application state.
- “Noise” records and exclusion conditions.
- Parameter values.
- The expected answer transformation.
- Matching logic.

Supported answer transformations include count, sum, and identity. An example calendar task asks for event titles on a given date and prevents noise events from sharing that date.

Language models can help draft these protobuf definitions, but the process requires human review. Common generated errors include missing or hallucinated fields, incompatible parameter generation, unused parameters, and vague prompts. More complex protobuf structures produced more errors, although editing a generated structure could still be faster than authoring one from scratch.

### 3.8 Task examples

**Table 5** demonstrates the diversity of setup and evaluation:

- Create an ordered VLC playlist from generated media files while ignoring noise files.
- Read recipes from an image and enter them in the recipe app.
- Edit a Markor note by adding a header, footer, or replacement content.
- Add an expense while ignoring unrelated database entries.
- Delete calendar events only on a specified relative day.
- Delete one generated file without deleting noise files.
- Count activities of a specified OpenTracks category and return one integer.

The full task appendix includes multi-app transcription and composition tasks, such as entering expenses from Markor, transcribing a gallery receipt to a note, transcribing a VLC video, sending clipboard content, copying event information from one message to another, and creating then sharing a note by SMS.

Maximum step budgets were based on human analysis and were generally about **twice the number of steps used by human annotators**. Budgets range from around 10 steps for many simple tasks to **78** for merging notes and **120** for saving an OsmAnd track with ordered waypoints.

### 3.9 Human analysis

Six volunteers with programming proficiency divided the tasks equally to rate difficulty, expected duration/steps, and categories while identifying defects. This process found and resolved **more than 30 bugs**.

Two software engineers then attempted the tasks in an emulator, with one attempt per task. Errors mainly arose from misinterpretation, minor mistakes such as an incorrect file extension, or unfamiliarity with an interface.

**Figure 2** reports the annotation distributions:

- Panel (a) shows substantially more easy tasks than medium tasks, and more medium than hard tasks.
- Panel (b) shows that most tasks were expected to take relatively few actions, with progressively fewer tasks in high-step ranges, although a small tail extends beyond 30 steps.
- Panel (c) shows that data entry is the most common category, followed by screen reading, search, information retrieval, and data editing. Other categories include complex UI interaction, repetition, multi-app work, transcription, actions requiring setup, mathematical counting, verification, and memorization.

The exact small chart values are not all legible in the supplied page image, so only the visible ordering and trends can be stated confidently.

### 3.10 MobileMiniWoB++

The authors implemented MiniWoB++ inside AndroidWorld as a WebView app. Each task uses the standard `TaskEval` interface, with initialization and success-checking methods. JavaScript communicates with Python for task setup and evaluation.

MobileMiniWoB++:

- Uses Android screenshots and accessibility trees.
- Does **not** expose the HTML DOM.
- Uses AndroidWorld’s touch-oriented action space.
- Renders HTML controls through native Android widgets.

**Figure 4** shows an HTML5 input displayed as a native Android date picker, illustrating how the mobile version differs from an ordinary desktop web page.

All tasks were manually tested for solvability. The implementation contains **92 tasks** after excluding 12 tasks that failed because of rendering, touch compatibility, emulator timing, scrolling, or broken widget behavior. The excluded tasks were `chase-circle`, `moving-items`, `drag-cube`, `drag-items-grid`, `drag-items`, `drag-shapes`, `drag-sort-numbers`, `text-editor`, `number-checkboxes`, `use-slider-2`, `use-spinner`, and `click-menu`.

### 3.11 M3A agent

The authors created **M3A: Multimodal Autonomous Agent for Android**. It is a zero-shot agent combining ReAct-style reasoning and action with Reflexion-style post-action reflection.

For each step, M3A receives:

- The task instruction.
- Available action types.
- Android operating guidelines.
- UI elements derived from accessibility-tree leaf nodes.
- Depending on the variant, a screenshot annotated with Set-of-Marks.

A Set-of-Marks, or SoM, screenshot places a numbered bounding box on each detected UI element. **Figure 5** shows these marks overlaid on an Android audio-recorder settings screen.

M3A first produces reasoning and a JSON action. After execution, it compares the before-and-after interface states and summarizes:

- The intended action.
- Whether it succeeded.
- Possible reasons for failure.
- What should be attempted next.

This reflection becomes action history for subsequent decisions.

The study tests both:

- A multimodal SoM version using screenshots and the accessibility tree.
- A text-only version using the accessibility tree.

It also tests **M3A-Simple**, which omits detailed guidelines and reflection, to isolate the value of advanced prompting and Android-specific guidance.

### 3.12 SeeAct baseline

SeeAct was originally designed for web navigation. The authors adapted its best-performing textual-choice grounding variant to Android by:

- Adding scroll, long-press, Home, Back, and app-opening actions.
- Replacing the unavailable DOM with accessibility-tree elements.
- Removing the original DOM-specific ranking model.
- Filtering out non-interactable elements.

After filtering, most screens had fewer than 50 candidate elements. SeeAct reasons about the screenshot, selects one candidate from a multiple-choice list, and emits one standardized action.

### 3.13 Evaluation protocol

The principal evaluation used:

- Seed **30**.
- Sampling temperature **0**.
- All **116 AndroidWorld tasks**.
- A standard subset of **62 MobileMiniWoB++ tasks**.
- Gemini 1.5 Pro, GPT-4 Turbo, or open-source Gemma 2 27B as the base model.
- One task-specific maximum-step limit, normally about twice human requirements.

---

## 4. Results and Findings

### 4.1 Main success rates

**Table 3** reports success rates:

| Agent | Input | Base model | AndroidWorld | MobileMiniWoB++ |
|---|---|---:|---:|---:|
| Human | Screen | — | **80.0%** | **100.0%** |
| SeeAct | SoM screenshot + accessibility tree | GPT-4 Turbo | **15.5%** | **66.1%** |
| M3A-Simple | Accessibility tree | Gemma 2 | **3.4%** | **35.5%** |
| M3A-Simple | Accessibility tree | Gemini 1.5 Pro | **14.7%** | **55.2%** |
| M3A-Simple | Accessibility tree | GPT-4 Turbo | **19.8%** | **67.7%** |
| M3A | Accessibility tree | Gemma 2 | **9.5%** | **45.6%** |
| M3A | Accessibility tree | Gemini 1.5 Pro | **19.4%** | **57.4%** |
| M3A | SoM + accessibility tree | Gemini 1.5 Pro | **22.8%** | **40.3%** |
| M3A | Accessibility tree | GPT-4 Turbo | **30.6%** | **59.7%** |
| M3A | SoM + accessibility tree | GPT-4 Turbo | **25.4%** | **67.7%** |

The best AndroidWorld result is **30.6%**, achieved by text-only M3A with GPT-4 Turbo. This remains **49.4 percentage points below** the human success rate of 80.0%.

On MobileMiniWoB++, the highest reported agent score is **67.7%**, shared by GPT-4 Turbo M3A-Simple and the GPT-4 Turbo SoM M3A. Humans achieved 100%.

Despite the large human–agent gap, the agents could operate mobile interfaces without task-specific training. Observed abilities included long-pressing, scrolling to find information, and revising plans after failed actions.

### 4.2 Effect of prompting and reflection

For GPT-4 Turbo on AndroidWorld:

- Full text-only M3A: **30.6%**
- M3A-Simple: **19.8%**

The **10.8-point drop** indicates that reflection, richer prompting, operating guidelines, and domain-specific guidance materially improve performance on complicated native Android tasks.

On MobileMiniWoB++, however:

- M3A-Simple: **67.7%**
- Full text-only M3A: **59.7%**

The simpler agent performed at least comparably and numerically better, suggesting these web-derived tasks benefit less from sophisticated Android-specific prompting.

### 4.3 Text-only versus Set-of-Marks input

Multimodal input was not consistently superior.

With GPT-4 Turbo:

- AndroidWorld: text-only **30.6%**, SoM **25.4%**
- MobileMiniWoB++: text-only **59.7%**, SoM **67.7%**

With Gemini 1.5 Pro:

- AndroidWorld: text-only **19.4%**, SoM **22.8%**
- MobileMiniWoB++: text-only **57.4%**, SoM **40.3%**

Thus, screenshots and visual marks sometimes help but do not reliably outperform accessibility-tree input. The authors suggest SoM is especially useful when accessibility information is incomplete, as is often the case in MobileMiniWoB++, but the Gemini results show that the benefit is not universal.

### 4.4 Model comparison

Gemma 2 performed below the proprietary models:

- Full M3A with Gemma 2: **9.5%** on AndroidWorld and **45.6%** on MobileMiniWoB++.
- M3A-Simple with Gemma 2: **3.4%** and **35.5%**.

The authors tentatively attribute this to Gemma’s smaller parameter count. They caution that direct comparison is difficult because the sizes of GPT-4 and Gemini are not public.

### 4.5 SeeAct transfer from web to mobile

SeeAct achieved **15.5%** on AndroidWorld and **66.1%** on MobileMiniWoB++. It therefore transferred much better to the simpler web-derived mobile tasks than to real Android applications.

Its Android weaknesses included:

- Difficulty with long-press and swipe actions.
- Poor action selection when screen information was not adequately incorporated during action generation.
- Repetitive behavior on memory-intensive tasks.
- Storing previous actions without adequately retaining their outcomes.
- Failure to recover quickly, leading to endless scrolling or exhaustion of the step budget.

This supports the paper’s claim that a successful web agent is not automatically a universal cross-platform agent.

### 4.6 Error analysis

The authors identify four broad error classes.

**Perceptual errors:** The agent fails to notice a crucial visual state. In **Figure 6a**, it does not recognize that the “All-day” checkbox is unchecked while creating a recurring calendar event.

**Reasoning errors:** The agent misinterprets the instruction or interface state. In **Figure 6b**, it incorrectly assumes that a note’s filename has already been entered, types the note contents into the name field, and cannot recover.

**Missing-knowledge errors:** The agent does not understand how an application expects a task to be performed. In **Figure 6c**, it searches for a nonexistent “delete all” command instead of deleting notes individually.

**Grounding errors:** The intended action is reasonable, but the agent interacts with the wrong location or UI element. In **Figure 7**, the agent is supposed to prepend text to a Markor note. It clicks the broad text area, placing the cursor at the end, appends rather than prepends the text, and then saves the incorrect result.

Additional problems included:

- Difficulty operating sliders.
- Failure to recover from typing mistakes.
- Difficulty confirming system state, such as verifying that Wi-Fi is on.
- Poor memory when transcribing information across apps, multiplying previously displayed numbers, or retaining content found during scrolling.
- Limited human-like exploration after an unexpected outcome.

### 4.7 Latency

Large foundation models were substantially slower than people:

- M3A averaged **3.9 minutes per task**.
- The text-only version averaged **2.5 minutes**.
- Overall, large-model agents took approximately **three times as long as humans**.

### 4.8 Robustness across random seeds

Different random seeds change task details such as calendar events, expense categories, input lengths, numbers of items, and whether hidden controls must be accessed.

Across three seeds, text-only M3A with GPT-4 Turbo scored:

- **27.6%**
- **26.3%**
- **33.2%**

The mean was **29.0%**. Table 3 retains the single-seed result for comparability with prior work, but the three-seed results show that one seed can give an incomplete account of practical ability.

### 4.9 Controlled robustness experiment

The researchers selected five representative tasks:

- AddExpense
- DeleteFile
- EditNote
- DeleteEvent
- CountActivities

They ran **20 trials per task** with their strongest configuration: GPT-4 Turbo M3A using the accessibility tree. They compared:

1. Repeated trials with the same task parameters.
2. Trials with different parameterizations.

**Figure 3** plots success rate for the five tasks with **95% Wilson binomial proportion confidence intervals**. Same-seed results are shown separately from different-seed results. The exact bar heights are visually approximate, but the documented findings are:

- With a constant seed, the agent completely failed the add-expense and edit-note tasks.
- It rarely solved deletion tasks.
- Performance still varied under identical parameters, showing that model non-determinism affects reliability even at the fixed evaluation configuration.
- Different parameterizations produced much greater variance.
- AddExpense and EditNote differed significantly between conditions, with **p < 0.05**.
- Under varied seeds, tasks that appeared impossible under one fixed seed were solved a meaningful fraction of the time.

The authors argue that the mean across seeds is therefore more representative than a single run.

### 4.10 Why parameters change difficulty

**Figure 8** shows the Pro Expense entry screen. Its category selector is horizontally scrollable. If a seed selects a visible category such as “Housing” or “Social,” the agent can complete the task. If it selects a hidden category such as “Food” or “Other,” the agent consistently fails because it does not discover the horizontal-scroll interaction.

Markor editing varies similarly:

- Adding a header is comparatively simple.
- Adding a footer requires a different cursor position.
- Replacing content requires long-pressing, selecting text, deleting it, and entering the replacement.

A fixed seed that happens to choose a difficult variant can make the agent appear incapable of the entire task template.

### 4.11 Robustness across Android configurations

The principal environment used a Pixel 6 with Android 13. On a **Pixel 5 with Android 12**, the agent achieved **28.4%** success. The magnitude of the change resembled ordinary seed variation, suggesting that it retained broadly similar abilities despite different device types and UI layouts.

### 4.12 Visual and table synthesis

- **Figure 1:** System diagram connecting parameterized task definitions, emulator apps and OS state, agent observations/actions, and automatic rewards.
- **Figure 2:** Human ratings show a benchmark dominated by easy-to-medium tasks, usually requiring relatively few steps, with data entry and screen reading among the most common categories.
- **Table 2:** Demonstrates durable system-state and composite validation.
- **Table 3:** Establishes the main human, SeeAct, M3A-Simple, and M3A performance comparisons.
- **Figure 3:** Shows that both model randomness and task-parameter variation affect scores, with larger variance across different seeds and significant effects for AddExpense and EditNote.
- **Figure 4:** Demonstrates native Android rendering of an HTML input as a mobile date picker.
- **Figure 5:** Shows numbered Set-of-Marks boxes constructed from accessibility elements.
- **Figures 6–7:** Provide concrete perceptual, reasoning, missing-knowledge, and grounding failures.
- **Figure 8:** Explains parameter sensitivity through a hidden, horizontally scrollable expense category.
- **Table 4:** Enumerates all 20 apps and their task counts.
- **Table 5:** Shows how tasks generate relevant and distractor state and how success is checked.

---

## 5. Analysis and Interpretation

The results answer the central research question in two ways.

First, AndroidWorld can automatically and reproducibly evaluate agents on real mobile applications. Its direct inspection of files, databases, and settings makes rewards less dependent on superficial UI layout and more closely tied to whether the user’s requested outcome occurred.

Second, existing agents remain far from reliable mobile autonomy. The best agent completed **30.6%** of AndroidWorld tasks versus **80.0%** for humans. The gap reflects deficiencies in perception, reasoning, application knowledge, grounding, memory, exploration, recovery, and speed.

The difference between AndroidWorld and MobileMiniWoB++ is especially informative. SeeAct and M3A-Simple perform relatively well on the web-derived tasks but poorly on native AndroidWorld. This suggests that success on simplified or browser-oriented benchmarks does not establish competence in real mobile apps.

The prompting comparison shows that structured reflection and Android-specific guidance help on complex native applications. Their value is smaller on MobileMiniWoB++, whose tasks are simpler and more synthetic.

The robustness findings show that benchmark scores depend not only on the agent and task name but also on the randomly selected task instance. Parameterization can expose qualitatively different interaction requirements—for example, an immediately visible choice versus one hidden behind horizontal scrolling. Single-seed evaluation can therefore produce “bad luck” results that make a partially capable agent appear completely incapable, or favorable results that hide weaknesses.

Variation with a fixed seed further shows that reproducible environment state does not eliminate model non-determinism. The authors recommend representing performance by averages across seeds.

Non-zero rewards under some parameterizations indicate that agents have partial capability that could potentially be strengthened through reinforcement-learning-like improvement mechanisms. Composite rewards could also supply incremental feedback for multi-part tasks.

---

## 6. Contributions and Novelty

The paper’s main contributions are:

- **A realistic Android benchmark:** 116 task templates across 20 functioning apps, including native, system, multi-app, web, state-changing, and information-retrieval tasks.
- **Dynamic task construction:** Random parameters generate millions of natural-language goals, start states, and success conditions rather than one fixed instance per template.
- **Durable automatic rewards:** Task outcomes are checked through application databases, files, system settings, and UI state.
- **Strong reproducibility controls:** Fixed OS and app versions, controlled device time, seeded initialization, and task-specific setup and teardown.
- **Reusable and composable validators:** Existing checks can be combined for multi-part tasks and partial rewards.
- **MobileMiniWoB++:** A 92-task Android adaptation of MiniWoB++ using native mobile controls and Android observations rather than the DOM.
- **M3A:** A released zero-shot Android agent combining multimodal or text-only observation with structured action and reflection.
- **Baseline evidence:** Comparative results for humans, M3A, M3A-Simple, SeeAct, GPT-4 Turbo, Gemini 1.5 Pro, and Gemma 2.
- **Robustness analysis:** Evidence that different task parameters significantly alter observed performance and that evaluation should span multiple seeds and conditions.
- **Support for future learning research:** Dynamic tasks can generate train/test data and support online or reinforcement learning.

---

## 7. Limitations and Caveats

- AndroidWorld currently focuses on **open-source applications and built-in system apps**, not proprietary trending apps.
- Open-source apps may have less polished interfaces, fewer shortcuts, and more complex interaction patterns than popular commercial apps. This can make the benchmark harder but limits direct generalization to those commercial products.
- Apps must not require login and must store data locally, restricting application coverage.
- Although the framework contains 116 templates, the principal reported score uses one fixed seed for comparability. The authors’ own robustness study shows that this may not fully represent capability.
- The controlled robustness study covers only five tasks and uses 20 trials per task because of computational constraints.
- The MobileMiniWoB++ evaluation uses **62 of its 92 supported tasks**, following prior evaluation conventions.
- Twelve original MiniWoB++ tasks could not be supported because of mobile rendering, touch, timing, or widget failures.
- Accessibility trees can be incomplete, especially in web-derived content.
- M3A is slow: 3.9 minutes per task on average, or 2.5 minutes for text-only operation.
- Agents have serious practical weaknesses in grounding, memory, visual understanding, UI knowledge, error recovery, and exploration.
- Human benchmark participants had only one attempt per task, so human errors included misunderstandings and unfamiliar-interface mistakes.
- Exact parameter-count comparisons between Gemma, GPT-4, and Gemini cannot be made because the latter models’ sizes are not public.
- The Android 12 test suggests some cross-device robustness, but it involves only one additional device/OS configuration.
- LLM-assisted generation of information-retrieval task definitions is not automatic and requires manual review.
- Some figures contain small labels whose exact numerical values are not fully readable in the supplied page images; interpretations here rely on clearly legible captions and textual discussion rather than guessed bar heights.

### Ethical caveats

The paper identifies two risk categories:

- **Malicious use:** Agents could be engineered to bypass protections such as CAPTCHAs, send spam, or manipulate prompts and screen content toward harmful objectives.
- **Societal effects:** Automation may change social norms, employment, and human behavior. Efficiency gains could be exploited by malicious actors.

---

## 8. Future Work or Open Questions

The authors identify or imply several next steps:

- Develop agents that close the large gap between **30.6% agent** and **80.0% human** success on AndroidWorld.
- Build genuinely cross-platform agents rather than assuming a web agent will transfer effectively to mobile.
- Evaluate over multiple seeds and parameterizations instead of relying on one fixed task instance.
- Improve perception of visual cues and grounding of precise touch and text-editing actions.
- Improve memory for cross-app transcription, arithmetic, and long scrolling tasks.
- Develop better exploration and error-recovery mechanisms.
- Reduce foundation-model latency.
- Study hybrid agents that combine UI actions with direct device APIs.
- Use dynamic tasks for supervised dataset generation, online learning, and reinforcement learning.
- Exploit partial rewards from composite tasks.
- Extend support to a broader range of applications and conditions, including applications beyond the present open-source and system-app selection.
- Continue studying robustness across OS versions, devices, layouts, and parameter-driven UI patterns.
- Improve automated generation of information-retrieval task specifications while retaining human verification.
- Develop more accurate general-purpose learned reward models; the paper notes that current multimodal evaluation has not yet matched carefully programmed rewards.

---

## 9. High-Level Takeaway (Plain Language)

AndroidWorld is a test environment for AI systems that operate Android phones. Instead of checking whether an AI copied a human’s exact taps, it checks the phone’s actual files, messages, databases, settings, and screens to determine whether the requested job was completed. Its 116 tasks across 20 apps can be regenerated with many different details, exposing weaknesses that a fixed test may hide.

The strongest tested agent completed only **30.6%** of AndroidWorld tasks, compared with **80.0%** for people. Agents could perform useful actions, but often misunderstood screens, touched the wrong controls, forgot information, or failed to recover from mistakes. Performance also changed substantially with task details. The central message is that realistic mobile agents need both better capabilities and broader, dynamically varied evaluation before their benchmark scores can be trusted as evidence of real-world reliability.